"""mini-swe-agent model class for running a small-context local model on long tasks.

mini-swe-agent resends the whole history on every step and never compacts it, which a
64K-token local model cannot survive on DeepSWE (leaderboard runs average 30K-200K output
tokens). This class changes only what is sent to the model, never the saved trajectory:

1. Reasoning text is kept for the most recent assistant turn(s) only.
2. When the prompt nears the context limit, the model is asked (in the same conversation,
   so the server's prompt cache is reused) to write a handoff note. Older turns are then
   replaced by that note and only the recent turns are kept verbatim.
3. If the server still rejects a request as too long, history is cut harder and retried.
4. The model is told its step and time budget up front, reminded that only committed work
   is graded, and warned as the budget runs out (mini-swe-agent otherwise stops silently).

Use with:  model.model_class: inkling_model.InklingModel
"""

import json
import logging
import time

import litellm

from minisweagent.models.litellm_model import LitellmModel, LitellmModelConfig
from minisweagent.models.utils.actions_toolcall import BASH_TOOL

logger = logging.getLogger("inkling_model")

_DROP_KEYS = ("extra", "provider_specific_fields", "function_call", "annotations", "audio", "refusal")

_SUMMARY_REQUEST = """\
PAUSE. Your working memory is about to be truncated: every message above this one, except \
the last few steps, will be deleted. Do NOT call any tool in this reply. Write a handoff \
note for yourself, in plain text, with these sections:

1. TASK STATE: which requirements are done, which are not started, which are in progress.
2. CODEBASE MAP: the files, functions and types that matter (exact paths and names), and \
how to build and run the relevant tests (exact commands that worked).
3. CHANGES MADE: every file you created or edited and what you changed in it.
4. PITFALLS: errors you hit and how you fixed them, and approaches that did not work.
5. NEXT STEPS: the concrete next actions, in order.

Be specific and complete; anything not in the note is lost. Stay under 1200 words."""

_SUMMARY_HEADER = """\
[Earlier steps were removed to save context. This is the handoff note you wrote before they \
were removed. The repository on disk still contains all your edits; re-read files with \
commands if you need their current contents.]

"""


_BUDGET_INTRO = """

<budget>
You have at most {steps} steps and about {minutes} minutes for this task. Only changes \
committed to git are graded: uncommitted work counts as nothing. Create your branch early, \
commit as soon as something works (`git add -A && git commit -m "..."`), and commit again \
after each further milestone. A partial solution that is committed beats a complete one \
that is not.
</budget>"""

_BUDGET_WARNING = """

[Budget notice: about {steps} steps and {minutes} minutes remain. Commit all your work now \
(`git add -A && git commit -m "..."`). Then finish only the most important remaining item, \
commit again, and submit with `echo COMPLETE_TASK_AND_SUBMIT_FINAL_OUTPUT`.]"""

_WARN_STEPS_LEFT = (30, 15, 6, 2)
_WARN_TIME_USED = (0.75, 0.9, 0.97)


class InklingModelConfig(LitellmModelConfig):
    compact_at_tokens: int = 44000
    """Compact history when the estimated prompt size exceeds this."""
    keep_recent_tokens: int = 10000
    """Approximate size of the recent history kept verbatim after compaction."""
    keep_reasoning_last: int = 1
    """Number of most recent assistant turns whose reasoning text is resent."""
    budget_steps: int = 0
    """The agent's step limit, so the model can be told about it (0 = say nothing)."""
    budget_seconds: int = 0
    """The agent's wall-time limit, so the model can be told about it (0 = say nothing)."""
    summary_max_tokens: int = 5000
    """Output budget for the handoff note (includes the model's reasoning tokens)."""


class InklingModel(LitellmModel):
    def __init__(self, **kwargs):
        super().__init__(config_class=InklingModelConfig, **kwargs)
        self._cut = 2  # messages[2:_cut] are replaced by the handoff note
        self._summary = ""
        self._tokens_per_char = 0.30
        self._last_view_chars = 0
        self.n_compactions = 0
        self._n_queries = 0
        self._t0 = None
        self._notes: dict[int, str] = {}  # raw message index -> text appended to that message
        self._time_warned = 0

    # ---- view of the history that is actually sent -------------------------------------

    def _view(self, messages: list[dict]) -> list[dict]:
        def noted(i: int) -> dict:
            m = dict(messages[i])
            if i in self._notes:
                m["content"] = _content_text(m) + self._notes[i]
            return m

        head = [noted(i) for i in range(min(2, len(messages)))]
        if self._cut > 2 and len(head) == 2:
            head[1] = {**head[1], "content": _content_text(head[1]) + "\n\n" + _SUMMARY_HEADER + self._summary}
        view = head + [noted(i) for i in range(self._cut, len(messages))]
        view = [{k: v for k, v in m.items() if k not in _DROP_KEYS and v is not None} for m in view]
        assistant_idx = [i for i, m in enumerate(view) if m.get("role") == "assistant"]
        keep = set(assistant_idx[-self.config.keep_reasoning_last :]) if self.config.keep_reasoning_last > 0 else set()
        for i in assistant_idx:
            if i not in keep:
                view[i].pop("reasoning_content", None)
                view[i].pop("thinking_blocks", None)
        return view

    def _prepare_messages_for_api(self, messages: list[dict]) -> list[dict]:
        view = self._view(messages)
        self._last_view_chars = _chars(view)
        return view

    def _estimate_tokens(self, messages: list[dict]) -> int:
        return int(_chars(self._view(messages)) * self._tokens_per_char)

    # ---- compaction ---------------------------------------------------------------------

    def _new_cut(self, messages: list[dict], keep_tokens: int) -> int:
        """Largest suffix that starts at an assistant turn and fits in keep_tokens."""
        budget_chars = keep_tokens / self._tokens_per_char
        starts = [i for i in range(self._cut, len(messages)) if messages[i].get("role") == "assistant"]
        if not starts:
            return self._cut
        best = starts[-1]
        for i in reversed(starts):
            if _chars(messages[i:]) > budget_chars:
                break
            best = i
        return best

    def _fallback_summary(self, messages: list[dict], upto: int) -> str:
        lines = ["(Automatic note: the commands run so far, oldest first.)"]
        for m in messages[2:upto]:
            for a in (m.get("extra") or {}).get("actions", []):
                lines.append("$ " + str(a.get("command", ""))[:300].replace("\n", "\\n"))
        text = "\n".join(lines[-150:])
        return (self._summary + "\n\n" + text) if self._summary else text

    def _write_summary(self, messages: list[dict]) -> str:
        view = self._view(messages) + [{"role": "user", "content": _SUMMARY_REQUEST}]
        kwargs = dict(self.config.model_kwargs)
        kwargs["max_tokens"] = self.config.summary_max_tokens
        # tools are passed (and unused) so the prompt prefix matches the server's cache
        response = litellm.completion(model=self.config.model_name, messages=view, tools=[BASH_TOOL], **kwargs)
        text = (response.choices[0].message.content or "").strip()
        if len(text) < 200:
            raise ValueError(f"handoff note too short ({len(text)} chars)")
        return text

    def _compact(self, messages: list[dict], *, keep_tokens: int, use_llm: bool) -> None:
        new_cut = self._new_cut(messages, keep_tokens)
        if new_cut <= self._cut:
            return
        summary = None
        if use_llm:
            try:
                summary = self._write_summary(messages)
            except Exception as e:  # noqa: BLE001 - any failure falls back to the command list
                logger.warning("handoff note failed (%s); using command list", e)
        self._summary = summary or self._fallback_summary(messages, new_cut)
        self._cut = new_cut
        self.n_compactions += 1
        logger.warning("compacted history: cut=%d of %d messages, note=%d chars", new_cut, len(messages), len(self._summary))

    # ---- budget notes -------------------------------------------------------------------

    def _update_budget_notes(self, messages: list[dict]) -> None:
        cfg = self.config
        if not (cfg.budget_steps or cfg.budget_seconds):
            return
        now = time.time()
        if self._t0 is None:
            self._t0 = now
            if len(messages) > 1:
                self._notes[1] = _BUDGET_INTRO.format(
                    steps=cfg.budget_steps or "unlimited", minutes=(cfg.budget_seconds // 60) or "unlimited"
                )
        steps_left = cfg.budget_steps - self._n_queries if cfg.budget_steps else None
        secs_left = cfg.budget_seconds - (now - self._t0) if cfg.budget_seconds else None
        warn = steps_left in _WARN_STEPS_LEFT
        if cfg.budget_seconds:
            used = (now - self._t0) / cfg.budget_seconds
            crossed = sum(1 for f in _WARN_TIME_USED if used >= f)
            if crossed > self._time_warned:
                self._time_warned = crossed
                warn = True
        last = len(messages) - 1
        if warn and last >= 2 and messages[last].get("role") in ("tool", "user"):
            self._notes[last] = _BUDGET_WARNING.format(
                steps="?" if steps_left is None else max(0, steps_left),
                minutes="?" if secs_left is None else max(0, int(secs_left // 60)),
            )

    # ---- query --------------------------------------------------------------------------

    def query(self, messages: list[dict], **kwargs) -> dict:
        self._update_budget_notes(messages)
        self._n_queries += 1
        if self._estimate_tokens(messages) > self.config.compact_at_tokens:
            self._compact(messages, keep_tokens=self.config.keep_recent_tokens, use_llm=True)
        try:
            message = super().query(messages, **kwargs)
        except litellm.exceptions.ContextWindowExceededError:
            self._compact(messages, keep_tokens=self.config.keep_recent_tokens // 2, use_llm=False)
            message = super().query(messages, **kwargs)
        usage = ((message.get("extra") or {}).get("response") or {}).get("usage") or {}
        prompt_tokens = usage.get("prompt_tokens") or 0
        if prompt_tokens > 2000 and self._last_view_chars:
            self._tokens_per_char = min(0.6, max(0.15, prompt_tokens / self._last_view_chars))
        message["extra"]["context"] = {"cut": self._cut, "n_compactions": self.n_compactions, "prompt_tokens": prompt_tokens}
        return message

    def serialize(self) -> dict:
        data = super().serialize()
        data["info"]["context"] = {"cut": self._cut, "n_compactions": self.n_compactions, "summary": self._summary}
        return data


def _content_text(message: dict) -> str:
    content = message.get("content")
    if isinstance(content, str):
        return content
    if isinstance(content, list):
        return "\n".join(p.get("text", "") if isinstance(p, dict) else str(p) for p in content)
    return "" if content is None else str(content)


def _chars(messages: list[dict]) -> int:
    return sum(len(json.dumps({k: v for k, v in m.items() if k != "extra"}, default=str)) for m in messages)

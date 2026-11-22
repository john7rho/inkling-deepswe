#!/usr/bin/env python3
"""Summarize a pier job directory: one row per trial plus totals.  usage: summarize.py jobs/JOB [--md]"""
import json, sys, tomllib
from pathlib import Path

job = Path(sys.argv[1]); md = "--md" in sys.argv
tasks_dir = Path(__file__).resolve().parent.parent.parent / "deep-swe" / "tasks"
rows = []
for d in sorted(p for p in job.iterdir() if p.is_dir()):
    name = d.name.rsplit("__", 1)[0]
    try:  # trial directory names are truncated; the trial config has the full task path
        name = Path(json.loads((d / "config.json").read_text())["task"]["path"]).name
    except Exception:
        pass
    row = {"task": name, "lang": "?", "reward": None, "f2p": "", "p2p": "", "steps": "", "min": "", "exit": "", "compactions": ""}
    try:
        row["lang"] = tomllib.loads((tasks_dir / name / "task.toml").read_text())["metadata"]["language"]
    except Exception:
        pass
    rj = d / "verifier" / "reward.json"
    if rj.exists():
        r = json.loads(rj.read_text())
        row["reward"] = r.get("reward")
        row["f2p"] = f'{r.get("f2p_passed", "?")}/{r.get("f2p_total", "?")}'
        row["p2p"] = f'{r.get("p2p_passed", "?")}/{r.get("p2p_total", "?")}'
    tj = d / "agent" / "mini-swe-agent.trajectory.json"
    if tj.exists():
        try:
            t = json.loads(tj.read_text())
            a = [m for m in t["messages"] if m.get("role") == "assistant"]
            row["steps"] = len(a)
            ts = [m["extra"]["timestamp"] for m in a if m.get("extra", {}).get("timestamp")]
            if len(ts) > 1:
                row["min"] = round((ts[-1] - ts[0]) / 60)
            row["exit"] = t["info"].get("exit_status", "")
            row["compactions"] = t["info"].get("context", {}).get("n_compactions", "")
        except Exception as e:
            row["exit"] = f"unreadable trajectory ({type(e).__name__})"
    res = d / "result.json"
    if res.exists() and row["reward"] is None:
        try:
            ex = json.loads(res.read_text()).get("exception_info")
            if ex:
                row["exit"] = (row["exit"] + " " + str(ex.get("exception_type", ""))).strip()
        except Exception:
            pass
    rows.append(row)

cols = ["task", "lang", "reward", "f2p", "p2p", "steps", "min", "compactions", "exit"]
sep = " | " if md else "  "
if md:
    print("| " + " | ".join(cols) + " |"); print("|" + "---|" * len(cols))
for r in rows:
    line = sep.join(str("" if r[c] is None else r[c]) for c in cols)
    print(f"| {line} |" if md else line)
graded = [r for r in rows if r["reward"] is not None]
solved = sum(1 for r in graded if r["reward"] == 1)
print(f"\ntrials: {len(rows)}  graded: {len(graded)}  solved: {solved}" + (f"  ({100 * solved / len(graded):.1f}% of graded)" if graded else ""))
for lang in sorted({r["lang"] for r in graded}):
    g = [r for r in graded if r["lang"] == lang]
    print(f"  {lang}: {sum(1 for r in g if r['reward'] == 1)}/{len(g)}")

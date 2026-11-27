# inkling-deepswe

Running the [DeepSWE](https://github.com/datacurve-ai/deep-swe) v1.1 benchmark (113 long-horizon
software engineering tasks) entirely locally, with Thinking Machines' Inkling 2 Mini on a single
16GB RTX 4080.

## Results

Inkling 2 Mini (Q4_K_M) with mini-swe-agent solved **21 of 113 tasks (18.6%)**: 21 of the 112 that
were graded, as one task's environment failed to build.

| language | solved |
|---|---|
| go | 8/33 |
| typescript | 8/35 |
| python | 3/34 |
| javascript | 1/5 |
| rust | 1/5 |

Averaged over graded tasks, 61.6% of the target (fail-to-pass) tests pass and 95.6% of the existing
(pass-to-pass) tests still pass. 24 runs hit the agent's time or step limit before submitting.

Per-task results are in [results/README.md](results/README.md) and [results/trials.json](results/trials.json).

Notes:

- One attempt per task (no pass@k), one task at a time.
- 108 tasks ran with the harness at b76a805. The other 5 finished in an earlier run at a426ca1 (the
  only difference: b76a805 checkpoints the agent's work in commits as its budget runs out) and weren't
  rerun.
- `kcp-go-multiplexed-kcp-streams` errored before the agent started (`docker compose` failed to
  bring up its environment) and isn't graded.
- Some failures may be grader false negatives: hidden tests can collide with tests the agent writes
  ([deep-swe#76](https://github.com/datacurve-ai/deep-swe/issues/76)). These numbers are as graded.

## Hardware and setup

| | |
|---|---|
| GPU | NVIDIA GeForce RTX 4080, 16 GB (driver 595.99.02) |
| CPU | Intel Core i7-13700K (16 cores, 24 threads) |
| RAM | 64 GB |
| Disk | 2 TB NVMe |
| OS | Ubuntu 26.04.1 LTS, Linux 7.0, Docker 29.1.3 |
| Model | Inkling-2-Mini Q4_K_M GGUF (16.3 GiB) |
| Server | llama.cpp at 19bc41dbb in a `nvidia/cuda:12.8.1-devel-ubuntu22.04` container, 64K context, one slot, batch 32 |
| Speed | roughly 160 tokens/s prompt processing, 49 tokens/s generation (averaged over the server's last requests) |
| Agent | mini-swe-agent 2.4.6 via [Pier](https://github.com/datacurve-ai/pier) 0.3.1, reasoning effort minimal |
| Limits per task | 200 steps, 100 minutes wall time, 10K output tokens per step; history compacted at 44K tokens |
| Wall time | about 121 hours for the 108-task run (median 62 minutes per task) |

The GGUF is slightly larger than the card's memory, so llama.cpp (`--fit-target 256`) keeps part of
it in system RAM. Larger batch sizes split it differently and return NaN garbage on long prompts;
see `server/start.sh`.

## Files

- `server/start.sh`: llama.cpp server for the Q4_K_M GGUF, 64K context
- `harness/inkling_model.py`: mini-swe-agent model class that compacts history so a 64K-context model can work through long tasks
- `harness/inkling.yaml`: mini-swe-agent config
- `scripts/run.sh`: runs the benchmark through [Pier](https://github.com/datacurve-ai/pier)
- `scripts/supervise.sh`: starts a job and resumes it after a crash or reboot until every trial finishes
- `scripts/summarize.py`: one row per trial plus totals for a Pier job directory
- `results/`: per-task results of the full run

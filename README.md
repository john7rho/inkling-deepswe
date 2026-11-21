# inkling-deepswe

Running the [DeepSWE](https://github.com/datacurve-ai/deep-swe) v1.1 benchmark (113 long-horizon
software engineering tasks) entirely locally, with Thinking Machines' Inkling 2 Mini on a single
16GB RTX 4080.

Work in progress. Results will be added here when the run finishes.

- `server/start.sh`: llama.cpp server for the Q4_K_M GGUF, 64K context
- `harness/inkling_model.py`: mini-swe-agent model class that compacts history so a 64K-context model can work through long tasks
- `harness/inkling.yaml`: mini-swe-agent config
- `scripts/run.sh`: runs the benchmark through [Pier](https://github.com/datacurve-ai/pier)

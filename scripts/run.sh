#!/bin/bash
# Run DeepSWE tasks with mini-swe-agent against the local Inkling server.
# usage: scripts/run.sh JOB_NAME [extra pier args, e.g. -i 'datacurve/abs-*' or --n-tasks 5 --sample-seed 0]
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
TASKS="${DEEPSWE_TASKS:-$ROOT/../deep-swe/tasks}"
JOB="$1"; shift
# the harness is pip-installed into each task container from this repo at the checked-out commit
HARNESS_REF="${HARNESS_REF:-$(git -C "$ROOT" rev-parse HEAD)}"
export PATH="$HOME/.local/bin:$PATH"
export OPENAI_API_KEY="$(cat "${INKLING_API_KEY_FILE:-$HOME/inkling/api-key}")"

exec pier run -p "$TASKS" --agent mini-swe-agent --model openai/inkling-2-mini \
  --ak version=2.4.6 \
  --ak model_class=inkling_model.InklingModel \
  --ak config_file="$ROOT/harness/inkling.yaml" \
  --ak "extra_python_packages=[\"git+https://github.com/john7rho/inkling-deepswe@$HARNESS_REF\"]" \
  --n-concurrent 1 --jobs-dir "$ROOT/jobs" --job-name "$JOB" --yes --quiet "$@"

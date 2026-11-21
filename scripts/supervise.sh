#!/bin/bash
# Start a benchmark job, or resume it after a crash or reboot, until every trial has finished.
# usage: scripts/supervise.sh JOB_NAME [extra pier args for the first start]
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
JOB="$1"; shift
export PATH="$HOME/.local/bin:$PATH"
export OPENAI_API_KEY="$(cat "${INKLING_API_KEY_FILE:-$HOME/inkling/api-key}")"
cd "$ROOT"
exec 9>"$ROOT/.supervise-$JOB.lock"
flock -n 9 || { echo "supervisor for $JOB already running"; exit 0; }

finished() {
  python3 - "$ROOT/jobs/$JOB/result.json" <<'PY'
import json, sys
try:
    r = json.load(open(sys.argv[1])); s = r["stats"]
    done = s["n_completed_trials"] + s["n_errored_trials"] >= r["n_total_trials"] > 0
except Exception:
    done = False
sys.exit(0 if done else 1)
PY
}

while ! finished; do
  until curl -sf -m 5 http://127.0.0.1:8080/health >/dev/null; do sleep 10; done
  # containers left behind by an interrupted trial
  docker ps -aq --filter name=-main-1 --filter name=pier-egress-proxy | xargs -r docker rm -f >/dev/null
  echo "[$(date -Is)] starting/resuming $JOB"
  if [ -f "jobs/$JOB/config.json" ]; then
    pier job resume -p "jobs/$JOB"
  else
    scripts/run.sh "$JOB" "$@"
  fi
  sleep 30
done
echo "[$(date -Is)] $JOB finished"

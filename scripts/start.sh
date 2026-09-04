#!/usr/bin/env bash
# Start one run from a task.json, detached, and print exactly one line. The session that asked
# never sees the run's output: it goes to the run dir and the page.
source "$(dirname "${BASH_SOURCE[0]}")/env.sh"
TASK="${1:?usage: start.sh task.json | start.sh - < task.json}"
[ -x "$VENV/bin/csmw" ] || "$PLUGIN_ROOT/scripts/bootstrap.sh" >/dev/null || { echo "refused: bootstrap failed, see $DATA/bootstrap.log"; exit 1; }
if [ "$TASK" = "-" ]; then  # the task on stdin: the caller never has to write a file
  TASK="$DATA/tasks/stdin-$$.json"; cat > "$TASK"
fi
NAME="$("$VENV/bin/python" -c "import json,sys;print(json.load(open(sys.argv[1]))['task_id'])" "$TASK" 2>/dev/null)" || { echo "refused: the task is not JSON with a task_id"; exit 2; }
[ "$TASK" = "$DATA/tasks/stdin-$$.json" ] && mv "$TASK" "$DATA/tasks/$NAME.json" && TASK="$DATA/tasks/$NAME.json"
RUN="$RUNS/$NAME"; n=2
while [ -f "$RUN/state.json" ]; do RUN="$RUNS/$NAME-$n"; n=$((n+1)); done
mkdir -p "$RUN"
"$VENV/bin/python" - "$TASK" "$RUN" <<'PY'
import json, sys, pathlib
t = json.load(open(sys.argv[1])); run = pathlib.Path(sys.argv[2]); t["task_id"] = run.name
(run / "task.json").write_text(json.dumps(t, indent=2))
PY
"$VENV/bin/csmw" validate "$RUN/task.json" > "$RUN/validate.log" 2>&1 || { echo "refused: the task does not validate; see $RUN/validate.log"; exit 2; }
nohup "$VENV/bin/csmw" run "$RUN/task.json" --run-dir "$RUN" --no-mlflow > "$RUN/runner.log" 2>&1 < /dev/null &
disown
"$PLUGIN_ROOT/scripts/dashboard.sh" >/dev/null 2>&1 || true
echo "started $(basename "$RUN") · runs on its own · http://127.0.0.1:$PORT/ · $RUN"

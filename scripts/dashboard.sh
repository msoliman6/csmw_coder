#!/usr/bin/env bash
# The page for the runs dir, started once and left running; prints its URL.
source "$(dirname "${BASH_SOURCE[0]}")/env.sh"
if curl -s -o /dev/null "http://127.0.0.1:$PORT/"; then echo "http://127.0.0.1:$PORT/"; exit 0; fi
HARNESS="$(cat "$DATA/harness.path" 2>/dev/null || echo "$HARNESS")"
[ -d "$HARNESS/dashboard" ] || { echo "no harness checkout for the page; run bootstrap"; exit 1; }
cd "$HARNESS" && nohup "$VENV/bin/python" -m reflex run --frontend-port "$PORT" --backend-port "$BACKEND_PORT" > "$DATA/dashboard.log" 2>&1 < /dev/null &
disown
echo "http://127.0.0.1:$PORT/ (starting)"

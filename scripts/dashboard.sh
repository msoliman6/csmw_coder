#!/usr/bin/env bash
# The page for the runs dir, started once and left running; prints its URL. With a port as the
# argument, the port is remembered ($DATA/dashboard.port), the page running on the old one is
# stopped, and the page starts on the new one.
source "$(dirname "${BASH_SOURCE[0]}")/env.sh"
if [ -n "${1:-}" ]; then
    case "$1" in ''|*[!0-9]*) echo "not a port: $1"; exit 2;; esac
    OLD="$PORT"
    echo "$1" > "$DATA/dashboard.port"
    PORT="$1"; BACKEND_PORT=$((PORT + 1))
    if [ "$OLD" != "$PORT" ]; then
        for pid in $(lsof -nP -iTCP:"$OLD" -sTCP:LISTEN -t 2>/dev/null) $(lsof -nP -iTCP:$((OLD + 1)) -sTCP:LISTEN -t 2>/dev/null); do kill "$pid" 2>/dev/null || true; done
        sleep 1
    fi
fi
if curl -s -o /dev/null "http://127.0.0.1:$PORT/"; then echo "http://127.0.0.1:$PORT/"; exit 0; fi
HARNESS="$(cat "$DATA/harness.path" 2>/dev/null || echo "$HARNESS")"
[ -d "$HARNESS/dashboard" ] || { echo "no harness checkout for the page; run bootstrap"; exit 1; }
cd "$HARNESS" && nohup "$VENV/bin/python" -m reflex run --frontend-port "$PORT" --backend-port "$BACKEND_PORT" > "$DATA/dashboard.log" 2>&1 < /dev/null &
disown
echo "http://127.0.0.1:$PORT/ (starting)"

#!/usr/bin/env bash
# One line per run, newest first; with a name, that run only. Reads state.json, nothing else.
source "$(dirname "${BASH_SOURCE[0]}")/env.sh"
"$VENV/bin/python" - "$RUNS" "${1:-}" <<'PY'
import json, sys, pathlib, time
runs = pathlib.Path(sys.argv[1]); only = sys.argv[2]
dirs = [d for d in runs.iterdir() if (d / "state.json").exists() and (not only or d.name == only)]
for d in sorted(dirs, key=lambda p: p.stat().st_mtime, reverse=True)[:12]:
    st = json.loads((d / "state.json").read_text())
    done = sum(1 for s in st.get("steps", {}).values() if s.get("done_at")); total = len(st.get("steps", {}))
    report = d / "REPORT.md"
    tail = f" · report {report}" if report.exists() else ""
    print(f"{d.name}: {st.get('status')} · {done}/{total} steps{tail}")
if not dirs:
    print("no runs" + (f" named {only}" if only else ""))
PY

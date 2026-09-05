#!/usr/bin/env bash
# First use: a venv in the plugin's data dir with the runtime and this workflow installed.
# Idempotent and quiet: prints one line at the end. Everything else goes to $DATA/bootstrap.log.
source "$(dirname "${BASH_SOURCE[0]}")/env.sh"
LOG="$DATA/bootstrap.log"
{
  if [ -z "$HARNESS" ] && [ -f "$DATA/harness/pyproject.toml" ]; then
    HARNESS="$DATA/harness"  # cloned on an earlier run
  fi
  if [ -z "$HARNESS" ] || [ ! -f "$HARNESS/pyproject.toml" ]; then
    command -v gh >/dev/null || { echo "need gh to fetch the runtime, or set harness_path"; exit 2; }
    gh repo clone msoliman6/code_steer_model_write "$DATA/harness" -- --quiet
    HARNESS="$DATA/harness"
  fi
  if [ ! -x "$VENV/bin/python" ]; then  # a checkout with a venv already? reuse it: the plugin root, or the marketplace's directory
    for cand in "$(python3 -c "import json,os;m=json.load(open(os.path.expanduser('~/.claude/plugins/known_marketplaces.json')));print((m.get('marketplaces',m).get('csmw') or {}).get('installLocation',''))" 2>/dev/null)/.venv" "$PLUGIN_ROOT/.venv"; do
      [ -x "$cand/bin/csmw" ] && ln -s "$cand" "$VENV" && break
    done
  fi
  if [ ! -x "$VENV/bin/python" ]; then
    PY="$(command -v python3.11 || command -v python3)"
    "$PY" -m venv "$VENV"
  fi
  "$VENV/bin/pip" install -q --upgrade pip
  "$VENV/bin/pip" install -q -e "$HARNESS" -e "$PLUGIN_ROOT"
  echo "$HARNESS" > "$DATA/harness.path"
} >> "$LOG" 2>&1 || { echo "bootstrap failed; see $LOG"; exit 1; }
echo "ready: venv $VENV, runtime $(cat "$DATA/harness.path"), runs $RUNS"

#!/usr/bin/env bash
# First use: a venv in the plugin's data dir with the runtime and this workflow installed.
# Idempotent and quiet: prints one line at the end. Everything else goes to $DATA/bootstrap.log.
# Every step checks its own exit: `set -e` is silent inside a group that feeds `||` (ledger: an exit
# code that lies -- the first fresh install printed "ready" over a failed clone and a failed pip).
source "$(dirname "${BASH_SOURCE[0]}")/env.sh"
LOG="$DATA/bootstrap.log"
{
  if [ -z "$HARNESS" ] && [ -f "$DATA/harness/pyproject.toml" ]; then
    HARNESS="$DATA/harness"  # cloned on an earlier run
  fi
  if [ -z "$HARNESS" ] || [ ! -f "$HARNESS/pyproject.toml" ]; then
    command -v gh >/dev/null || { echo "need gh to fetch the runtime, or set harness_path"; exit 2; }
    gh repo clone msoliman6/code_steer_model_write "$DATA/harness" -- --quiet || { echo "could not clone the runtime (is gh signed in?)"; exit 2; }
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
  "$VENV/bin/pip" install -q --upgrade pip || exit 1
  # the runtime first, from its checkout; then the workflow on top of it with no second resolution
  # of the runtime (its name is not on PyPI, so pip would look for it there and refuse)
  "$VENV/bin/pip" install -q -e "$HARNESS" || { echo "pip could not install the runtime from $HARNESS"; exit 1; }
  "$VENV/bin/pip" install -q --no-deps -e "$PLUGIN_ROOT" || { echo "pip could not install the workflow"; exit 1; }
  [ -x "$VENV/bin/csmw" ] || { echo "the install left no csmw in $VENV"; exit 1; }
  echo "$HARNESS" > "$DATA/harness.path"
} >> "$LOG" 2>&1 || { echo "bootstrap failed; see $LOG"; exit 1; }
echo "ready: venv $VENV, runtime $(cat "$DATA/harness.path"), runs $RUNS"

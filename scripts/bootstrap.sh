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
    # the runtime needs Python 3.11 to 3.13 (Guardrails AI has no 3.14 build yet; the runtime's
    # pyproject says so): the first interpreter in that range wins, and none is a named failure,
    # not a pip error five screens long (ledger: a message that hides the reason)
    PY=""
    for cand in python3.13 python3.12 python3.11 python3; do
      v="$(command -v "$cand" 2>/dev/null)" || continue
      "$v" -c 'import sys; sys.exit(0 if (3, 11) <= sys.version_info[:2] <= (3, 13) else 1)' 2>/dev/null && { PY="$v"; break; }
    done
    [ -n "$PY" ] || { echo "need Python 3.11, 3.12 or 3.13 on PATH (found: $(python3 --version 2>&1 || echo none)); the runtime's dependencies do not build on 3.14 yet"; exit 2; }
    "$PY" -m venv "$VENV" || { echo "could not create a venv with $PY"; exit 1; }
  fi
  "$VENV/bin/pip" install -q --upgrade pip || exit 1
  # the runtime first, from its checkout; then the workflow on top of it with no second resolution
  # of the runtime (its name is not on PyPI, so pip would look for it there and refuse)
  "$VENV/bin/pip" install -q -e "$HARNESS" || { echo "pip could not install the runtime from $HARNESS"; exit 1; }
  # openai on its own, second: Guardrails pins openai<3 for calls the runtime never makes and
  # PydanticAI's OpenAI path needs >=3.8; pip applies the upgrade with a warning (the runtime's pyproject says why)
  "$VENV/bin/pip" install -q "openai>=3.8" tiktoken || { echo "pip could not upgrade openai"; exit 1; }
  "$VENV/bin/pip" install -q --no-deps -e "$PLUGIN_ROOT" || { echo "pip could not install the workflow"; exit 1; }
  [ -x "$VENV/bin/csmw" ] || { echo "the install left no csmw in $VENV"; exit 1; }
  echo "$HARNESS" > "$DATA/harness.path"
} >> "$LOG" 2>&1 || { echo "bootstrap failed; see $LOG"; exit 1; }
echo "ready: venv $VENV, runtime $(cat "$DATA/harness.path"), runs $RUNS"

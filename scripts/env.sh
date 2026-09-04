#!/usr/bin/env bash
# Shared by the plugin's scripts: where the venv, the harness, the runs and the page live.
set -euo pipefail
PLUGIN_ROOT="${CLAUDE_PLUGIN_ROOT:-$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)}"
DATA="${CLAUDE_PLUGIN_DATA:-$HOME/.claude/plugins/data/csmw-coder}"
VENV="$DATA/venv"
HARNESS="${CSMW_HARNESS:-${harness_path:-}}"
RUNS="${CSMW_RUNS_DIR:-${runs_dir:-$HOME/.csmw/runs}}"
PORT="${dashboard_port:-${CSMW_DASH_PORT:-3007}}"
BACKEND_PORT=$((PORT + 1))
export CSMW_RUNS_DIR="$RUNS" CSMW_CLI_USE_LOGIN="${CSMW_CLI_USE_LOGIN:-1}"
mkdir -p "$DATA" "$RUNS" "$DATA/tasks"

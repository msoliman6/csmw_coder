#!/usr/bin/env bash
# The plugin's MCP server (ARCHITECTURE.md 7.10): the runtime's gateway over stdio. Declared in
# plugin.json; Claude Code starts it when the plugin loads, Codex when its config names it. The
# first start bootstraps the environment; after that it execs the server at once.
source "$(dirname "${BASH_SOURCE[0]}")/env.sh"
[ -x "$VENV/bin/csmw" ] || "$PLUGIN_ROOT/scripts/bootstrap.sh" >/dev/null 2>&1 || { echo "bootstrap failed; see $DATA/bootstrap.log" >&2; exit 1; }
exec "$VENV/bin/csmw" gateway serve

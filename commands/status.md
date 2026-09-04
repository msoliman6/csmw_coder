---
name: status
description: One line per run of the coder, newest first; a name shows that run only.
argument-hint: "[run name]"
allowed-tools: mcp__csmw__run_list, mcp__csmw__workflow_status
---

If a run name was given, call `workflow_status` of the `csmw` MCP server with `{"run": "<name>"}`
and answer with one line: `<run_id>: <status> · <steps_done>/<steps_total> steps · <verdict or
current step or halt>`. Otherwise call `run_list` and answer with one such line per run, newest
first, at most twelve. Nothing else: no advice, no summary, no offer.

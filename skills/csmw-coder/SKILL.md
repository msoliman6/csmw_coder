---
name: csmw-coder
description: Build a Python module on the side with the csmw coder: two model sides of different vendors (Claude Code writes, OpenAI Codex checks) plan, freeze a contract, design the verification, build tests and source in isolation and verify, with code deciding every step. Use it when the user asks to build, implement or write a Python module, library, package, function or CLI with tests, wants an adversarially reviewed implementation, or says "build this on the side". Not for edits inside the current repository, one-line fixes, or non-Python targets.
---

# csmw coder — build a Python module on the side

The coder is a production-grade agentic workflow that runs as its own process. You start it
from this session through the `csmw` MCP server; it never writes back into the session, the
page is where it is watched, and the report lands in the run's folder.

## When to use it

- The user wants a Python module, library, package, function or small CLI **built with tests**,
  from a description: "build me a slug library", "implement a rate limiter with tests",
  "write a parser for X and verify it".
- The user wants two vendors on it: one writes, the other attacks (plan review, contract audit,
  null run, verification), and a report at the end.
- The work can live in its own folder under `~/.csmw/runs/<name>/` and be copied into a project
  afterwards. The coder does not edit the current repository.

Do not use it for a change inside the open repository, a one-line fix, a question, or a
non-Python target.

## What it expects: one task object

`workflow_run` takes `{"task": <object>}`. Compose the object from the conversation; invent
nothing; if the request itself is missing, ask for it in one sentence and stop. The shape
(`plugin/task.schema.json`, the wording `plugin/task.example.json`, the settings
`plugin/defaults.json`):

| field | what goes in it |
|---|---|
| `task_id` | the module name: letters, digits, underscores; also the run's name |
| `objective` | one sentence |
| `inputs.brief.request` | one paragraph, the user's words where they gave them |
| `inputs.brief.context` | where it runs, who calls it, what exists already |
| `inputs.brief.surface` | the public functions and their signatures |
| `inputs.brief.must_be_true` | observable claims, one per item: what the tests will check |
| `inputs.brief.constraints` | python version, dependencies allowed, style |
| `inputs.brief.out_of_scope` | boundaries, not suggestions |
| `inputs.brief.language`, `inputs.brief.module` | `"python"`, the module name again |
| `inputs.fix_rounds` | how many fix rounds after verification (default 1) |
| `roles.author`, `roles.checker` | `backend`, `model`, `effort`, `thinking` per side; from the defaults unless the user asked |
| `mode` | `auto` asks nothing and flags every default it took; `light` asks the risky gates; `human` asks every gate |
| `rounds` | attack rounds per review loop (default 1) |

Everything the user did not mention comes from `plugin/defaults.json`. The same object is what
the page's start form produces, so a task the session composes and a task a person fills in
are the same thing.

## How to start it, and what comes back

1. Compose the task object.
2. Call `workflow_run` with `{"task": <object>}`. It validates the task through the workflow,
   registers the run, launches it detached, and returns `run_id`, `run_dir`, `status` at once.
3. Answer with one line: `started <run_id> · runs on its own · <page address> · <run_dir>`.
   Nothing else: no summary, no polling, no reading the folder, no offer to check on it. If the
   tool refused the task, answer with its reason in one line.

The page (`/csmw-coder:dashboard`, default `http://127.0.0.1:3007/`) lists every run, opens
one, and shows where the time went. On a remote machine the user tunnels the port
(`ssh -L 3007:127.0.0.1:3007 user@host`) and uses the same address locally.

## The other tools of the `csmw` server

`workflow_status` (where a run is), `workflow_cancel`, `workflow_pause`, `workflow_resume`,
`workflow_run_again` (the same task, a new run), `run_list`, `run_get`, `run_logs` (paged by
sequence), `run_artifacts`, `run_forget`, `run_delete` (the folder and every trace of it; refused
while running). Use them only when the user asks about a run by name; never poll on your own.

---
name: build
description: Build a Python module on the side. Turns this conversation's request into a task and starts a run through the workflow's MCP tool; the run continues without you. Prints one line and stops.
argument-hint: "[what to build, in one paragraph, if not already said]"
allowed-tools: Read, mcp__csmw__workflow_run
---

Start a code-builder run from what this conversation has established. The run is a separate
process that continues after you answer; you never wait for it, poll it, read its folder, or
report on it. Your whole answer is one line.

1. Compose the task. Read `${CLAUDE_PLUGIN_ROOT}/plugin/defaults.json` (the settings), take the
   shape from `${CLAUDE_PLUGIN_ROOT}/plugin/task.schema.json` and the wording from
   `${CLAUDE_PLUGIN_ROOT}/plugin/task.example.json`, and compose one JSON object with:
   - `task_id`: the module name (letters, digits, underscores).
   - `objective`: one sentence.
   - `inputs.brief`: `request` (one paragraph, the user's words where they gave them), `context`
     (where it runs, who calls it, what exists already), `surface` (the public functions and
     their signatures), `must_be_true` (observable claims, one per item), `constraints`,
     `out_of_scope` (boundaries, not suggestions), `language` "python", `module` the same name.
   - `roles`, `swaps`, `mode`, `rounds`, `inputs.fix_rounds`: copied from the defaults unless the
     user asked for something else in this conversation.
   Fill every field from the conversation and the current project; invent nothing. If the request
   itself is missing, ask for it in one sentence and stop. Do not ask about anything else.

2. Start it: call the `workflow_run` tool of the `csmw` MCP server with `{"task": <the object>}`.
   The tool validates the task through the recipe, registers the run, launches it detached and
   returns at once with `run_id`, `run_dir` and `status`. Write no file yourself.

3. Answer with one line: `started <run_id> · runs on its own · http://127.0.0.1:3007/ · <run_dir>`,
   and nothing more. No summary of the task, no next steps, no offer to check on it. The page in
   that line is where the run is watched. If the tool refused the task, answer with its reason in
   one line instead.

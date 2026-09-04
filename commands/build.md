---
name: build
description: Build a Python module on the side. Turns this conversation's request into a task and starts a run that continues without you; prints one line and stops.
argument-hint: "[what to build, in one paragraph, if not already said]"
allowed-tools: Read, Write, Bash
---

Start a code-builder run from what this conversation has established. The run is a separate
process that continues after you answer; you never wait for it, poll it, read its folder, or
report on it. Your whole answer is one line.

1. Write the task. Read `${CLAUDE_PLUGIN_ROOT}/plugin/defaults.json` (the settings), take the
   shape from `${CLAUDE_PLUGIN_ROOT}/plugin/task.schema.json` and the wording from
   `${CLAUDE_PLUGIN_ROOT}/plugin/task.example.json`, then write
   `${CLAUDE_PLUGIN_DATA}/tasks/<module>.json` with:
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

2. Start it:
   ```bash
   "${CLAUDE_PLUGIN_ROOT}/scripts/start.sh" "${CLAUDE_PLUGIN_DATA}/tasks/<module>.json"
   ```

3. Answer with the single line the script printed, verbatim, and nothing more. No summary of the
   task, no next steps, no offer to check on it. The page in that line is where the run is watched.

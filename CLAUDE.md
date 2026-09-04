# csmw_coder

A project on the `code_steer_model_write` template: this repo owns *what* the code-builder
workflow is (its stages, prompts, schemas of its own, fakers, walk legs, example); the template
owns *how* any workflow runs. The 14 universal rules in the template's README and CLAUDE.md
apply here unchanged.

- `just walk` before any live run; `just test` runs the legs and the figure pin.
- Never edit `csmw_coder/` while a run lives under `runs/`.
- A bug is classified against the template's BUG-LEDGER classes before it is fixed; a mechanism
  that belongs to the harness is fixed in the template, never patched around here.
- The workflow registers itself by entry point (`pyproject.toml`); the harness must never name it.

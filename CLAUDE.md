# csmw_coder

The code-builder workflow: this repo owns *what* the workflow is (its stages, prompts, its own
schemas, fake answers, walk legs, example). The harness it runs on owns *how* any workflow runs;
its fourteen universal rules apply here unchanged.

- `just walk` before any live run; `just test` runs the legs and the figure pin.
- Never edit `csmw_coder/` while a run lives under `runs/`.
- A bug is classified against the harness's bug-ledger classes before it is fixed; a mechanism
  that belongs to the harness is fixed there, never patched around here.
- The workflow registers itself by entry point (`pyproject.toml`); the harness must never name it.

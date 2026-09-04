<p align="center"><img src="https://raw.githubusercontent.com/msoliman6/code_steer_model_write/main/docs/media/logo-freeze-swap-brand-256.png" width="96" alt="code steers, models write"></p>

# csmw_coder

The **code-builder** workflow as a recipe package for
[code_steer_model_write](https://github.com/msoliman6/code_steer_model_write): two model sides
of different vendors build a Python module through a plan, a frozen contract, a verification
design, an isolated build and a verification run, with code deciding every step.

This repo owns *what* the workflow is: the recipe (`csmw_coder/recipe.py`), its fake answers for
the offline walk, its prompts, its example task and its walk legs. The template owns *how* any
workflow runs and is installed as a dependency; the recipe registers itself through the
`csmw.recipes` entry point, so the template's CLI, start page and run page find it without
naming it.

<p align="center"><picture>
<source media="(prefers-color-scheme: dark)" srcset="docs/media/workflow-dark.svg">
<img src="docs/media/workflow.svg" alt="How the code-builder workflow operates" width="820">
</picture></p>

## Run it

```bash
git clone git@github.com:msoliman6/code_steer_model_write.git ../code_steer_model_write
just install          # a venv with the harness and this package, both editable
just doctor           # the backends, the CLIs, the keys
just walk             # every branch offline with fake models, zero tokens
just run              # the example task live (claude -p as author, codex exec as checker)
just dash             # the page at http://127.0.0.1:3007
```

The example task (`examples/code_builder/task.json`) builds a slug library. Runs live under
`runs/` and are never committed.

## Layout

| path | what |
|---|---|
| `csmw_coder/recipe.py` | the `CodeBuilder` recipe: stages, steps derived from disk, checks, gates |
| `csmw_coder/fake.py` | fake answers per schema for the offline walk |
| `csmw_coder/walk_legs.py` | the ten legs the walk runs, one per branch |
| `prompts/code_builder/` | the code-filled prompt templates |
| `examples/code_builder/task.json` | the example TaskSpec |
| `docs/media/workflow*.svg` | the workflow figure, generated from the recipe (`just figure`) |

## Status

`status: proven` on the template's live pass of 2026-09-03 (`claude-haiku-4-5` + `gpt-5.4-mini`).

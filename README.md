<p align="center"><img src="https://raw.githubusercontent.com/msoliman6/code_steer_model_write/main/docs/media/logo-freeze-swap-brand-256.png" width="96" alt="code steers, models write"></p>
<p align="center">
<img alt="Python 3.11+" src="https://img.shields.io/badge/python-3.11%2B-3776AB?style=flat-square&logo=python&logoColor=white">
<img alt="Pydantic v2" src="https://img.shields.io/badge/pydantic-v2-E92063?style=flat-square&logo=pydantic&logoColor=white">
<img alt="Prefect" src="https://img.shields.io/badge/prefect-orchestration-070E10?style=flat-square&logo=prefect&logoColor=white">
<img alt="MLflow" src="https://img.shields.io/badge/mlflow-traces%20and%20evals-0194E2?style=flat-square&logo=mlflow&logoColor=white">
<img alt="Reflex" src="https://img.shields.io/badge/reflex-dashboard-5646ED?style=flat-square">
<img alt="SQLite" src="https://img.shields.io/badge/sqlite-monitor.db-003B57?style=flat-square&logo=sqlite&logoColor=white">
</p>
<p align="center">
<img alt="Author: Claude" src="https://img.shields.io/badge/author-Claude-db6d28?style=flat-square">
<img alt="Checker: Codex" src="https://img.shields.io/badge/checker-Codex-2fa39a?style=flat-square">
<img alt="Backends" src="https://img.shields.io/badge/backends-anthropic%20sdk%20%C2%B7%20agent%20sdk%20%C2%B7%20litellm%20%C2%B7%20claude%20cli%20%C2%B7%20codex%20cli-555?style=flat-square">
</p>
<p align="center">
<img alt="Code check: ruff" src="https://img.shields.io/badge/code%20check-ruff-D7FF64?style=flat-square&logo=ruff&logoColor=black">
<img alt="Code check: pyright" src="https://img.shields.io/badge/code%20check-pyright-1E90FF?style=flat-square">
<img alt="Verification: pytest" src="https://img.shields.io/badge/verification-pytest%20%C2%B7%20null%20run-0A9EDC?style=flat-square&logo=pytest&logoColor=white">
<img alt="License: MIT" src="https://img.shields.io/badge/license-MIT-lightgrey?style=flat-square">
</p>


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

## The workflow

The block diagram of this workflow, generated from the recipe (`just figure`): what each stage
does, who writes and who attacks, where code freezes, merges and runs.

<p align="center"><picture>
<source media="(prefers-color-scheme: dark)" srcset="docs/media/workflow-dark.svg">
<img src="docs/media/workflow.svg" alt="How the code-builder workflow operates" width="820">
</picture></p>

## The harness

The harness operates on top of the workflow: the workflow figure above is the top box of this
one. The harness is the template's; this repo only supplies the workflow. The agent workflow is Python; it feeds Prefect and MLflow through their SDKs; both feed
`monitor.db`; Reflex is the human control plane; the custom dashboard is what you look at.

<p align="center"><picture>
<source media="(prefers-color-scheme: dark)" srcset="docs/media/harness-dark.svg">
<img src="docs/media/harness.svg" alt="How the runtime is wired" width="760">
</picture></p>

### Clean responsibility split

| system | owns |
|---|---|
| **Prefect** | workflow execution · task dependencies · retries · scheduling · cancellation · run/task state |
| **MLflow** | agent / LLM traces · spans · tool calls · retrieval traces · token / cost / latency · workflow / agent evaluation · scientific / ML experiments · parameters / metrics · artifacts / models |
| **monitor.db** | dashboard-only state · live human-readable progress · current activity · UI metadata · graph layout / positions |
| **Reflex** | human control plane · create tasks · launch / cancel runs · live dashboard · inspect traces · inspect experiments · inspect evaluations |

The main rule:

```text
workflow/task state  -> Prefect
agent behavior       -> MLflow traces
experiment results   -> MLflow experiments
UI-only state        -> monitor.db
human interaction    -> Reflex
```

Do not log the same data into all systems.

### Shared workflow id

Every subsystem receives the same application-level id, and the dashboard joins on it:

```text
workflow_run_id = "run_123"
   |
   +-- Prefect -----> What is executing?
   +-- MLflow ------> What did the agents do? How did the experiment perform?
   +-- monitor.db --> What UI-specific state should be displayed?
```

In this template the id is the run's folder name under `runs/`; `state.json` and `events.jsonl`
in that folder are the one owner of status and history, and Prefect, MLflow and `monitor.db` are
fed from them (rule 4, one owner per fact).


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

`status: proven`: one clean live pass from this repo on 2026-09-04 (`live-2`: 23 steps, no halt, no
refusal, no resume; `claude-haiku-4-5` + `gpt-5.4-mini`, low effort, auto, one round), after the
template's pass of 2026-09-03. The verdict of that run carried 7 items; a verdict is a result, not a bug.

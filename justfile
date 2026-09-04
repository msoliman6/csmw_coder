# csmw_coder: the code-builder workflow on the code_steer_model_write harness

set shell := ["bash", "-cu"]

# the harness from the sibling checkout, then this package, both editable
install:
    python3 -m venv .venv && .venv/bin/pip install -q -e ../code_steer_model_write -e '.[dev]'

doctor:
    .venv/bin/csmw doctor

# every branch offline, fake models, zero tokens (rule 12); before any live run
walk:
    .venv/bin/csmw walk code_builder

test:
    .venv/bin/python -m pytest -q

# a live run from the example task
run task="examples/code_builder/task.json":
    CSMW_RUNS_DIR=runs .venv/bin/csmw run {{task}}

dash:
    CSMW_RUNS_DIR=runs .venv/bin/python -m reflex run --frontend-port 3007 --backend-port 3008

figure:
    .venv/bin/csmw figure code_builder --theme dark -o docs/media/workflow-dark.svg && .venv/bin/csmw figure code_builder --theme light -o docs/media/workflow.svg
    .venv/bin/csmw figure harness --theme dark -o docs/media/harness-dark.svg && .venv/bin/csmw figure harness --theme light -o docs/media/harness.svg

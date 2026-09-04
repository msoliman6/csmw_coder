<p align="center"><picture>
<source media="(prefers-color-scheme: dark)" srcset="docs/media/banner-dark.svg">
<img src="docs/media/banner.svg" alt="csmw coder" width="720">
</picture></p>

<p align="center"><b>The code-builder workflow: two model sides of different vendors build a Python module, with code deciding every step.</b></p>

<p align="center">
<a href="LICENSE"><img alt="license: MIT" src="https://img.shields.io/badge/license-MIT-bb8009?style=flat-square"></a>
<a href="https://www.python.org/"><img alt="python: 3.11+" src="https://img.shields.io/badge/python-3.11%2B-3776AB?style=flat-square&logo=python&logoColor=white"></a>
<a href="https://docs.pydantic.dev/"><img alt="schemas: pydantic v2" src="https://img.shields.io/badge/schemas-pydantic%20v2-E92063?style=flat-square&logo=pydantic&logoColor=white"></a>
<a href="https://www.prefect.io/"><img alt="orchestration: prefect" src="https://img.shields.io/badge/orchestration-prefect-d04a45?style=flat-square&logo=prefect&logoColor=white"></a>
<a href="https://mlflow.org/"><img alt="traces and evals: mlflow" src="https://img.shields.io/badge/traces%20and%20evals-mlflow-2fa39a?style=flat-square&logo=mlflow&logoColor=white"></a>
<a href="https://reflex.dev/"><img alt="dashboard: reflex" src="https://img.shields.io/badge/dashboard-reflex-5646ED?style=flat-square&logo=reflex&logoColor=white"></a>
</p>
<p align="center">
<a href="https://docs.astral.sh/ruff/"><img alt="code check: ruff" src="https://img.shields.io/badge/code%20check-ruff-D7FF64?style=flat-square&logo=ruff&logoColor=black"></a>
<a href="https://github.com/microsoft/pyright"><img alt="code check: pyright" src="https://img.shields.io/badge/code%20check-pyright-9a6ee0?style=flat-square&logoSize=auto&logo=data%3Aimage%2Fpng%3Bbase64%2CiVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAYAAABzenr0AAAEZUlEQVR42q2XS2hdVRSGv3XOyW2vTWpbbWOTRokPqC1ixIkPKDhRcVwHgg6dOXCgA0eOFHGiE4VOFEEF8UHxBYoDwYkdWRVDhQ7EmrSxJjfXJjfNfZzloP%2BWlePNzU1ww%2BHec%2FZj%2Fetf%2F1p7b9hGc%2FdMv%2BPu%2FpW7v%2BjuE6E%2Fd3fbzpq2HeNmVrr7IeBl4A5gP3AZ%2BBJ438wuJiBAaWb%2BvwAIxseAN4ASGAGmgavADUAT%2BAx4z8zmhwViQxg3M3N33w28CtwILAAHgKPAlQBon96HBmJbGdeYEeAVYBK4COzS97vEQGpdoFBo%2FgY%2BrwCxKgjbyriofwm4E7gg4wA94LjW6FbW6gZGmsCnwNtm1qiCyAbpQ8ZfAI4BvwE54AHAmjyuUpu%2BXdbvk8BH7j4Ts2lTAEF0zwP3AedF66EKe62wRj82E5BLwEHgpLy3TQG4ewGYuz8BnADmxcBhYByoBY9bComLdt8EyG6gAdzr7nuumblWL7LotTzvmlkPeFQTpyWoc8AiUAc6AnJcnk2JoSIAia1UuA4DM2ZWJqBFUGep%2F9PAyZBuDQ2O8c%2BBBxSSrsRWB67TewNoa14RsqYAnnL3eWAOaFvI82PA48DdWmQhTErK3q8wTKoOLAHLEtufMvSQAF5RXxtY0f9VMXcbcMrM3ilk%2FBngYU2aF2W1FJ2glxZwvUT1g8avB8Gtab7LgWS0G1hsAPendE7ejStfF9WR94ljyvczSsFcoGqhvycAKwJQ6Ht61rWHTAr8vwC%2BV1VrDLE1FGGeB6AuUEvAPcAton9dv2sac1TvGwD8LPTZMHvTgL5MlDfFZKlMSozulVjbAkqmfJwD%2FtJgZ2ct0ewq2VnwfFWp3AlOlAlxprw%2FD4yKiZ0Y7oruutJzNK2vJ9eTxq7EEAD8BDwYqpkPcY4o5VWmFJ0CJoA98n5E%2FRbqRyZWlhOAUp0%2FalI%2BwLiFjainOE8AN6twpUp4VcbHFNpMc7MAvARIdcCUNgtCv1YRZGIkxXAMOKJnb9gL2sFQqb7lSi0xrd%2BKIcjMrOfus6pkq2IielsAN8nbcXmfjEYtJJFl4VsZ3lOV3KCBhPAs8EjwqBQjk4rvPi3SkeCsz%2B6X6kEH%2BEPgLTCzQWNVAL%2BKGlNMp7SD1bVQp4%2B3%2FYy3ZbwbwpGM7gJ%2BEeN5oaOPaytecvcm8JgWqoX02uoMmYyvB8%2BzSvwLOfhampP1OQeeUkHKtJgP8Di2XOL6PaSeV84EB3R%2FmHX33MzKLBwAS4nxLPBsUPewxagl47l0k9K5p5AU2uxel6P%2BnyOZ4lKY2YfAm9JBZ4DhUiFC3s0obBfERl2XloPA7cBbZjYnR8u%2BMRW6lDKfqDouVwSbRFXX09SO%2BjHwjZktuvtoMD4B3Aq8KxZIR3Pb4lR8BPhaZXZN42uiuAfMAl8Ap83s3E53sM0uJrlCcgL4IBSRS8C3wGngOzNrV5grQ3W1Str2hrmwVo%2FouPtz7n7G3Z%2BO1%2FE0Jl40ttv%2BAbe8BGG9m5lPAAAAAElFTkSuQmCC"></a>
<a href="https://docs.pytest.org/"><img alt="verification: pytest" src="https://img.shields.io/badge/verification-pytest-0A9EDC?style=flat-square&logo=pytest&logoColor=white"></a>
<a href="https://www.sqlite.org/"><img alt="ui state: sqlite" src="https://img.shields.io/badge/ui%20state-sqlite-003B57?style=flat-square&logo=sqlite&logoColor=white"></a>
<a href="https://docs.litellm.ai/"><img alt="any provider: litellm" src="https://img.shields.io/badge/any%20provider-litellm-f59e0b?style=flat-square&logo=data%3Aimage%2Fpng%3Bbase64%2CiVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAYAAABzenr0AAAHzUlEQVR42uWXXYydRRnHf8%2FMvOc95%2Bw5%2B93t0gL1g1JIDAZL7AViKH4EbwQuSpSEC6NckKgXRBIvwNMaY8SISY0xMcQYIzSxJSAmaEFwwRiFpALyJZgWdVvabXfb7fnYc96PmXm8OLul0SIE5cI4ydzMO%2B%2F8Z%2F7P1%2F%2BB%2F6ehqqKq0mq1jGrLqKp5F8FaZm5uzqnOOdW9VkTOuU%2FeBWwB9Fwfdu%2FenU5PTzfTNB2ZmRlLG43U%2Fdcu0Gq1DFdfbXZt3%2B4BXn31hUuThCu8j5ephouKIr%2BwKIvJxJmxGLUGJN6XKv%2BpTfftw9y4g4iIAnzrSzecf8G2T93fGKlvHZ8Yc2maYp1ldmYdU9OzDPIcAUSELCtK906Bd%2B58woqIBwLAfffdt%2FlwnLzm%2BOmVHX95Pd%2B2vNzBx06wIuoVGR85KLdd%2F0Hes3FWBnmBtYYsG%2BDeyYtFJAB%2B8Xc%2Fb95%2FvHnDYqY3P5PFq0LSSP3oGCONGKYuSEzFOesSh7OOfhF5%2BKUFbqwa6rU6ee7JsuztX2Dv3r12FTj84aE965%2FqT3%2FhuwfNLaWtbcJY6k1hslkLE406aSWxYChLT3%2BQ0ev18dmAhbaw98l5rtu2DmMtRVG8dRSoqhFQRFSf%2BunoPcc2fnG%2Bo1%2FOksZ6Zw1TjWqYbNaoiDFFnku312PQbVMOOlBmOAmkLqGaVqjXEmpphUve22S0USXL8jf3AVWVJ54Y2tkCDz76%2BM1fP8idy1rfXMbAqIgfs2qTrG1X%2BifwxlNPlM2jFdZdOMJEc5pGvUZarZI4i3MOYywglF5ReHMTnEW3f%2B65ly5%2FfqH77UcP5x8%2FueKZqnb9hWPWbmwWbqZpmBmrMj46PgRLU6x1IJaoBlVBEUQMWZHjfQ4iqEZG6g0q6ci%2FmmBubs5t377d79%2F%2F%2B8nZWb3jVLtz6ytLUj2dETavr8r7Zmpm3VidkVoVm6QYk4BYxFisdVhrETEkzgLmTG7qdo5SrdYBIQSPMYKzlVLOplx27hR27YoHnnryk7jy%2B9bq5jzPWTcxFer1uk2SKsZVEVvBugqJS7DWYq1ZO4MQIs5FXni1w9%2BPZqAlZVlAOMV5s%2BvQGAhR6XRzOu2VoQ%2B0Wi0jItFa0Ucf%2F9XOaPotAyRJ009MnGcrac1W0hpJkpIkCc5aAGIMlGXGYOAJweO9p5Iohw4PuGP3UfqZJ%2Fo%2BvughYYnR8Qk0elAoipKlxUVcq9Uyu3btirr87Phnbv%2FNj0%2B18%2Bs3bJiMaTpOo9F0aTpCpZIiIsQYKYuMgS%2FxviQET4wBVUVRNEIMcO9DCxRFwdhIpCwChQQolcQKEYOIYoBGGoc%2B8OsHfjL1o%2F3tRw4ec1vvvHWL337lZhd1%2BNoQPGVZUJY53pfEGIgxAorqkHZQfIg0aobfHjjND%2FacoFYFXxYEn%2BGLAZSnaIyvIwSPxpLoPcunlkp34Bc%2FrN%2B5Z%2BGBvrlg6%2FjUaDk1NZNY6%2Bi2O%2FhygPcFIQRiVCAS4zCEVHV1DteMKN1O5P5fHoFQkPcDMXiizymLAaE4jUsswZeggahKWazgvnbviXsGdtNHR5sNPxj0k8XF1zl8eJleL0NdZRizOqQ5qiIoJgyIMZ4BjzFSTYWfPXyKl%2F58knpVKAtPVI8GT1n0ieVJQgCNkRgLEEunfRp3apDcVB0ZxNOLS67b7bGwsJ7p0Qa9geKPPs%2Bo6aOuBjGClmRe6I9fjDGsXkIRgSz3LBxbZvP5gkhA8KhGVAPRB7odz0ijJOrwqCSxTI85XGf5CL32gloj5IVn8XjkaKNCb6Ak7ZOYSoHYAWhAtKBfwlLZXPWBISuJE5790zE6y%2BCsIcQARNChLgnBE%2FKTlHawGvOREEcoByu4fOXEg0We3%2BCLXkQqcX6%2Bb1KXii%2BjqGtwaIXhYcMqjhGwnSVCiMQYz7Aw2oh84GJB1Q8Fkb4huKI6VnpNqtUKa8rMuYQ8r%2BM%2B8ulbb%2FrjY3u%2B1%2B8lt2T9tul1uywuDijLoALRWqPWWgFsiBHvAzGyCv6GQxpZS2hDXFkNzbU1gWFCWt0%2FGGSEEPyZTHjNjXdt7y4f%2Fdy2S8urNs6aWYSqcwZjDCEEVnodskFOCBGEIbies4ihKiCGYT0RFcGIiNGzfhARvPervA5nBLj77rtr9XqxPsva58Wos1idbC91Lnnltey2vBSxiZGgQvQRCBhZe6kiRFBIrKfm%2BgoqPgSyLCfPC40xioio90GMke6WLZt2n2Fgx44ddh%2FAvn3hn1%2B19crPP7ic1a8T66JYTPAlMXhgGIrEMLyADIvddPo3P1HPKu3e4LEiKx7JB9lnrbUfKr0vUZWy9JIX5cLrCyfOP5cgkVarJS%2B%2FjNu7F3%2Flx458pecn7yqDV1epiBEwRMwZ5a1DVxPBiCPVvzLTPM7xxfaJF158bUu73T69acOGyycnxw5MT06YGAKl9yycWPrON%2B768Ffl32h71q%2B%2FrD668YqnXdp8v7FRrXHGGkMlcSSJxVqLEQMaVYyVImv3sqW5hUoS548vnr7j0KH5Z6699qJ0%2F%2F6D%2BXkzM5%2BYHB%2B73Tkz1e2tPPTa%2FJFvAuGtJJnZcMn1E41KGBUpFKpUq1CtVs9syABTlBqcNXF5vv%2Fii08vrvnTWU3KmzYr70pj1Gq1zFlqZG3Y1bLPDrBrLMvba7Vab7OB2fWGY%2FyvjH8AcURzkt6vUdYAAAAASUVORK5CYII%3D"></a>
</p>
<p align="center">
<a href="https://docs.anthropic.com/en/docs/claude-code"><img alt="Claude Code: author" src="https://img.shields.io/badge/Claude_Code-author-d97757?style=flat-square"></a>
<a href="https://openai.com/codex/"><img alt="OpenAI Codex: adversarial checker" src="https://img.shields.io/badge/OpenAI_Codex-adversarial%20checker-10a37f?style=flat-square"></a>
<a href="https://github.com/anthropics/anthropic-sdk-python"><img alt="Anthropic SDK" src="https://img.shields.io/badge/Anthropic_SDK-backend-d97757?style=flat-square"></a>
<a href="https://github.com/anthropics/claude-agent-sdk-python"><img alt="Claude Agent SDK" src="https://img.shields.io/badge/Claude_Agent_SDK-backend-d97757?style=flat-square"></a>
<a href="https://docs.anthropic.com/en/docs/claude-code"><img alt="Claude Code CLI" src="https://img.shields.io/badge/Claude_Code_CLI-backend-d97757?style=flat-square"></a>
<a href="https://github.com/openai/codex"><img alt="OpenAI Codex CLI" src="https://img.shields.io/badge/OpenAI_Codex_CLI-backend-10a37f?style=flat-square"></a>
</p>

<p align="center"><a href="#workflow">Workflow</a> · <a href="#harness">Harness</a> · <a href="#how-the-models-are-held">How the models are held</a> · <a href="#quick-start">Quick start</a> · <a href="#license">License</a></p>

<p align="center">
<a href="examples/code_builder/task.json"><img alt="example: task.json" src="https://img.shields.io/badge/example-task.json-30363d?style=flat-square"></a>
<a href="csmw_coder/workflow.py"><img alt="workflow: workflow.py" src="https://img.shields.io/badge/workflow-workflow.py-30363d?style=flat-square"></a>
</p>

<p align="center"><i>Independent open-source project. Not affiliated with or endorsed by Anthropic or OpenAI.<br>Claude and Claude Code are trademarks of Anthropic; Codex and GPT are trademarks of OpenAI. Prefect, MLflow, Reflex, ruff, pyright and pytest belong to their owners.</i></p>

The **code-builder** workflow: two model sides
of different vendors build a Python module through a plan, a frozen contract, a verification
design, an isolated build and a verification run, with code deciding every step.

## Workflow

The block diagram of this workflow, generated from its definition (`just figure`): what each stage
does, who writes and who attacks, where code freezes, merges and runs.

<p align="center"><picture>
<source media="(prefers-color-scheme: dark)" srcset="docs/media/workflow-dark.svg">
<img src="docs/media/workflow.svg" alt="How the code-builder workflow operates" width="820">
</picture></p>

## Harness

The harness operates on top of the workflow: the workflow figure above is the top box of this
one. The agent workflow is Python; it feeds Prefect and MLflow through their SDKs; both feed
`monitor.db`; Reflex is the human control plane; the custom dashboard is what you look at.

<p align="center"><picture>
<source media="(prefers-color-scheme: dark)" srcset="docs/media/harness-dark.svg">
<img src="docs/media/harness.svg" alt="How the runtime is wired" width="760">
</picture></p>

<details>
<summary><b>Clean responsibility split</b></summary>

| system | owns |
|---|---|
| **Prefect** | workflow execution · task dependencies · retries · scheduling · cancellation · run/task state |
| **MLflow** | agent / LLM traces · spans · tool calls · retrieval traces · token / cost / latency · workflow / agent evaluation · scientific / ML experiments · parameters / metrics · artifacts / models |
| **monitor.db** | dashboard-only state · live human-readable progress · current activity · UI metadata · graph layout / positions |
| **Reflex** | human control plane · create tasks · launch / cancel runs · live dashboard · inspect traces · inspect experiments · inspect evaluations |

</details>

<details>
<summary><b>Shared workflow id</b></summary>

Every subsystem receives the same application-level id, and the dashboard joins on it:

```text
workflow_run_id = "run_123"
   |
   +-- Prefect -----> What is executing?
   +-- MLflow ------> What did the agents do? How did the experiment perform?
   +-- monitor.db --> What UI-specific state should be displayed?
```

</details>

## How the models are held

The rules below are the ones this workflow leans on, taken from the harness's fourteen.

- **Every model answer is constrained decoding against one schema.** Each call carries one pydantic
  schema; the backend enforces it at generation (Anthropic and Codex grammars, the Agent SDK's tool
  boundary) and pydantic validates it again. A model never writes prose into the run, only a JSON
  object of the declared shape.
- **Agents read markdown that code rendered from JSON.** No model is handed a file path, raw JSON or
  another model's prose; code renders every input and inlines it into the prompt.
- **Tools, files and shell are granted by need, never by default.** A step that needs them declares
  it, and then only inside the folder the agent writes its output to; every other step is issued with
  no tools at all, stated in the prompt and enforced by the harness.
- **No agent grades its own work.** The checker attacks a frozen copy, from a different vendor.
- **Every element has a code-assigned id, never renumbered.** Findings cite ids, so coverage is a set
  difference, not a judgment.
- **Nothing is recorded from a refused answer.** A refusal is re-asked with the exact problems and the
  refused answer, at most six times, stopping when the problem set repeats.
- **Every loop is bounded by code and carries its full trajectory.** Convergence is computed; the
  unresolved is carried into the report, never hidden.
- **Tokens are the honest measure.** Dollars are a lookup on read, blank until the price is known.

<details>
<summary><b>A schema, as the model receives it</b> — the review round's answer</summary>

Generated from the pydantic class by `wire_schema()`: every field required, no extra keys, ranges
kept in validators rather than the grammar.

```json
{
  "$defs": {
    "Finding": {
      "additionalProperties": false,
      "properties": {
        "severity": {
          "$ref": "#/$defs/Severity"
        },
        "cites": {
          "description": "the ids this finding is about (they must exist)",
          "items": {
            "type": "string"
          },
          "type": "array"
        },
        "kind": {
          "description": "gap: the input itself is silent on this; routes to the human",
          "enum": [
            "finding",
            "gap"
          ],
          "type": "string"
        },
        "klass": {
          "$ref": "#/$defs/Klass"
        },
        "argument": {
          "description": "why, engaging the cited text; a reader can check it",
          "type": "string"
        }
      },
      "required": [
        "severity",
        "cites",
        "kind",
        "klass",
        "argument"
      ],
      "type": "object"
    },
    "Klass": {
      "description": "The reconcile class (after addyosmani's agent-skills): what kind of thing a finding is.\nPrecedence when a finding could be two: contract_misread > actionable > tradeoff > noise.",
      "enum": [
        "contract_misread",
        "actionable",
        "tradeoff",
        "noise"
      ],
      "type": "string"
    },
    "Severity": {
      "enum": [
        "blocking",
        "major",
        "minor"
      ],
      "type": "string"
    }
  },
  "additionalProperties": false,
  "description": "A review round's answer. Empty `findings` with APPROVED is allowed (rule 9: the empty\nset is a valid answer); zero findings after several rounds is weak evidence, and the\nreviewer prompt says so.",
  "properties": {
    "findings": {
      "description": "empty means you found nothing",
      "items": {
        "$ref": "#/$defs/Finding"
      },
      "type": "array"
    },
    "verdict": {
      "description": "REVISE iff at least one finding is filed",
      "enum": [
        "APPROVED",
        "REVISE"
      ],
      "type": "string"
    }
  },
  "required": [
    "findings",
    "verdict"
  ],
  "type": "object",
  "title": "Findings"
}
```

</details>

<details>
<summary><b>An answer that passes</b></summary>

```json
{
  "findings": [
    {
      "severity": "major",
      "cites": [
        "C-0007"
      ],
      "kind": "finding",
      "klass": "actionable",
      "argument": "C-0007 keeps alphanumeric content in order but says nothing about an input that is only separators; two implementers resolve it two ways."
    }
  ],
  "verdict": "REVISE"
}
```

Code then checks that every cited id exists in the text the reviewer was shown, assigns the finding
its `F-` id, and only then writes the file.

</details>

## Quick start

```bash
just install          # a venv with the harness and this package
just doctor           # the backends, the CLIs, the keys
just walk             # every branch offline with fake models, zero tokens
just run              # the example task live (claude -p as author, codex exec as checker)
just dash             # the page at http://127.0.0.1:3007
```

The example task (`examples/code_builder/task.json`) builds a slug library. Runs live under
`runs/` and are never committed.

## Origins

- [claudex-loop](https://github.com/chaseai-yt/claudex-loop): Claude Code paired with OpenAI Codex as an adversarial reviewer inside a Claude Code plugin, the pairing this repo is built around.

## License

MIT.

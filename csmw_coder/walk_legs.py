"""The code-builder's walk legs (rule 12): every branch a live run can enter, walked offline
with fake models and zero tokens. Registered through the `csmw.walk_legs` entry point; the
template's `csmw walk code_builder` runs them."""

from __future__ import annotations

import json
from pathlib import Path

from code_steer_model_write.walk import (
    Decision,
    GateDecision,
    Halt,
    Mode,
    Outcome,
    RunState,
    env,
    events,
    kinds,
    make_runner,
    start,
    write_decision,
)


def leg_happy(tmp: Path) -> str:
    paths, recipe, task = start("code_builder", tmp / "run")
    out = make_runner(paths, recipe, task).drive()
    assert out is Outcome.COMPLETED, f"outcome {out}: {Halt.read(paths)}"
    st = RunState.load(paths)
    ks = kinds(paths)
    assert "halt" not in ks and "step.refused" not in ks
    assert ks.count("gate.decided") >= 3 and all(
        e.data.get("source") == "auto" for e in events(paths) if e.kind == "gate.decided"
    )
    assert (paths.run_dir / "freeze.json").exists() and (paths.run_dir / "REPORT.md").exists()
    res = json.loads((paths.artifacts / "results" / "v001.json").read_text())
    assert all(p["real"] == "pass" and p["null"] == "fail" for p in res["properties"]), res
    for e in events(paths):
        if e.kind == "call.started":
            assert e.data["tools"] == [], "a tool-less step carried tools"
    assert st.completed_at is not None
    return f"{len(st.steps)} steps, {len(res['properties'])} properties pass, 0 halts"


def leg_refuse_recover(tmp: Path) -> str:
    with env(FAKE_REFUSE="author:2"):
        paths, recipe, task = start("code_builder", tmp / "run")
        out = make_runner(paths, recipe, task).drive()
    assert out is Outcome.COMPLETED, Halt.read(paths)
    refused = [e for e in events(paths) if e.kind == "step.refused"]
    assert refused and all(e.role == "author" for e in refused)
    # nothing written from a refused attempt: every artifact.written follows a check.result with no problems
    evs = events(paths)
    for i, e in enumerate(evs):
        if e.kind == "artifact.written" and e.step and e.step.startswith("p0-ledger"):
            prior = [x for x in evs[:i] if x.step == e.step and x.kind == "check.result"]
            assert prior and prior[-1].data["problems"] == []
    return f"{len(refused)} refusals re-asked, then recovered"


def leg_no_progress_halts_then_resume(tmp: Path) -> str:
    with env(FAKE_REFUSE="author:same"):
        paths, recipe, task = start("code_builder", tmp / "run")
        out = make_runner(paths, recipe, task).drive()
    h = Halt.read(paths)
    assert (
        out is Outcome.HALTED_HONESTLY and h and h.reason.value == "refused" and "same problems" in h.message
    ), h
    out2 = make_runner(paths, recipe, task).drive()
    assert out2 is Outcome.COMPLETED, Halt.read(paths)
    st = RunState.load(paths)
    assert st.resumed_count == 1 and st.last_halt and st.last_halt.startswith("HALT at ")
    return f"halted at {h.step}, resumed, completed"


def leg_findings_rounds_and_closing(tmp: Path) -> str:
    with env(FAKE_FINDINGS="checker:2:major"):
        paths, recipe, task = start("code_builder", tmp / "run", rounds=2)
        out = make_runner(paths, recipe, task).drive()
    assert out is Outcome.COMPLETED, Halt.read(paths)
    filed = [e for e in events(paths) if e.kind == "finding.filed"]
    decided = [e for e in events(paths) if e.kind == "finding.decided"]
    assert filed and decided
    rounds = [e for e in events(paths) if e.kind == "round.closed"]
    assert any(e.data.get("closing") for e in rounds), "no closing read"
    # every finding is decided exactly once per round
    ids = [e.data["id"] for e in decided]
    assert len(ids) == len(set(ids))
    return f"{len(filed)} findings filed, {len(decided)} decided, {len(rounds)} rounds closed"


def leg_closing_carries(tmp: Path) -> str:
    with env(FAKE_FINDINGS="checker:1:minor", FAKE_CLOSING="finding"):
        paths, recipe, task = start("code_builder", tmp / "run", rounds=1)
        out = make_runner(paths, recipe, task).drive()
    assert out is Outcome.COMPLETED, Halt.read(paths)
    carried = [e for e in events(paths) if e.kind == "round.closed" and e.data.get("carried")]
    assert carried, "the closing read's finding was not carried"
    rep = json.loads((paths.artifacts / "report" / "v001.json").read_text())
    assert any(c["kind"] == "finding" for c in rep["carried"]), rep["carried"]
    assert "carried" in (paths.run_dir / "REPORT.md").read_text().lower()
    return f"{len(rep['carried'])} carried into the report"


def leg_buggy_impl_triage_fix(tmp: Path) -> str:
    with env(FAKE_IMPL="buggy"):
        paths, recipe, task = start("code_builder", tmp / "run")
        out = make_runner(paths, recipe, task).drive()
    assert out is Outcome.COMPLETED, Halt.read(paths)
    v1 = json.loads((paths.artifacts / "results" / "v001.json").read_text())
    failing = [p for p in v1["properties"] if p["real"] != "pass"]
    assert failing, "the buggy implementation passed everything"
    verdicts = [e for e in events(paths) if e.kind == "judge.verdict"]
    assert [v.data["question"] for v in verdicts[:2]] == [1, 2], verdicts
    assert (paths.artifacts / "results" / "v002.json").exists(), "no re-run after the fix"
    v2 = json.loads((paths.artifacts / "results" / "v002.json").read_text())
    assert all(p["real"] == "pass" for p in v2["properties"]), v2
    return f"{len(failing)} failing -> q1 test_stands -> q2 implementation_bug -> fixed -> pass"


def leg_test_bug_route(tmp: Path) -> str:
    with env(FAKE_IMPL="buggy", FAKE_VERDICT="author:test_bug"):
        paths, recipe, task = start("code_builder", tmp / "run")
        out = make_runner(paths, recipe, task).drive()
    assert out is Outcome.COMPLETED, Halt.read(paths)
    verdicts = [e.data["verdict"] for e in events(paths) if e.kind == "judge.verdict"]
    assert verdicts and set(verdicts) == {"test_bug"}, verdicts
    assert any(k.startswith("p4-fix-tests") for k in RunState.load(paths).steps)
    return "q1 test_bug -> the checker fixed the tests -> re-run"


def leg_ambiguity_carried(tmp: Path) -> str:
    with env(FAKE_IMPL="buggy", FAKE_VERDICT="checker:contract_ambiguity"):
        paths, recipe, task = start("code_builder", tmp / "run")
        out = make_runner(paths, recipe, task).drive()
    assert out is Outcome.COMPLETED, Halt.read(paths)
    rep = json.loads((paths.artifacts / "report" / "v001.json").read_text())
    assert any(c["kind"] == "ambiguity" for c in rep["carried"]), rep["carried"]
    assert not any(k.startswith("p4-fix") for k in RunState.load(paths).steps)
    return "q2 contract_ambiguity -> carried as a result, nothing fixed"


def leg_gate_revise(tmp: Path) -> str:
    with env(FAKE_REVISE="blocks:1"):
        paths, recipe, task = start("code_builder", tmp / "run")
        out = make_runner(paths, recipe, task).drive()
    assert out is Outcome.COMPLETED, Halt.read(paths)
    keys = list(RunState.load(paths).steps)
    assert "p1-contract-revise-r1" in keys and "p1-gate-blocks-r2" in keys, keys
    assert (paths.artifacts / "contract" / "v002.json").exists(), "the revision was not a new version"
    return "blocks gate sent back once -> revise -> asked again -> proceed"


def leg_light_mode_waits_then_human(tmp: Path) -> str:
    paths, recipe, task = start("code_builder", tmp / "run", mode=Mode.LIGHT)
    out = make_runner(paths, recipe, task, gate_timeout=0.3).drive()
    assert out is Outcome.HALTED_HONESTLY and Halt.read(paths).step == "p0-gate-ledger", Halt.read(paths)
    asked = [e for e in events(paths) if e.kind == "gate.asked"]
    assert asked and asked[0].data["needs_human"] is True
    answered: list[str] = []
    for _ in range(4):
        h = Halt.read(paths)
        if h is None or h.reason.value != "cancelled":
            break
        gid = next(e.data["gate"] for e in reversed(events(paths)) if e.kind == "gate.asked")
        gate = json.loads((paths.gates / f"{gid}.ask.json").read_text())
        write_decision(
            paths,
            GateDecision(
                gate=gid,
                action="proceed",
                source="human",
                decisions=[
                    Decision(question_id=q["id"], answer=q.get("default") or "yes", answered_by="human")
                    for q in gate["questions"]
                ],
            ),
        )
        answered.append(gid)
        out = make_runner(paths, recipe, task, gate_timeout=0.3).drive()
    assert out is Outcome.COMPLETED, Halt.read(paths)
    rows = json.loads(paths.decisions.read_text())
    assert rows[0]["answered_by"] == "human" and not rows[0]["flagged"]
    auto = [e for e in events(paths) if e.kind == "gate.decided" and e.data.get("source") == "auto"]
    return f"light: human answered {answered}; auto-answered {len(auto)} safe gate(s); never silent"


LEGS = {
    "happy": leg_happy,
    "refuse-recover": leg_refuse_recover,
    "no-progress-halt-resume": leg_no_progress_halts_then_resume,
    "findings-rounds-closing": leg_findings_rounds_and_closing,
    "closing-carries": leg_closing_carries,
    "buggy-impl-triage-fix": leg_buggy_impl_triage_fix,
    "test-bug-route": leg_test_bug_route,
    "ambiguity-carried": leg_ambiguity_carried,
    "gate-revise": leg_gate_revise,
    "light-mode-human": leg_light_mode_waits_then_human,
}

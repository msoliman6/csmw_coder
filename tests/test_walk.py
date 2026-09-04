"""Rule 12: every leg green offline before a token is spent. The template's walk runs the legs
this package registers."""

from code_steer_model_write import walk
from code_steer_model_write.recipes import registry


def test_the_workflow_is_the_installed_one():
    from csmw_coder.workflow import CodeBuilder

    assert isinstance(registry.get("code_builder"), CodeBuilder)
    assert "code_builder" in registry.walk_legs()


def test_every_leg_green():
    rs = walk.run("code_builder")
    assert rs and all(r.ok for r in rs), walk.report(rs)

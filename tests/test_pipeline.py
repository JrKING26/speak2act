# Placeholder test for the Speak2Act pipeline

from run_agent import run


def test_pipeline_smoke():
    """Smoke test: calling run() returns a dict with expected keys."""
    result = run()
    assert isinstance(result, dict)
    for key in ("audio", "transcript", "intent", "entities"):
        assert key in result

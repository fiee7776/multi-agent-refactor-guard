from pathlib import Path

from agents.orchestrator import run_pipeline


def test_pipeline_generates_outputs(tmp_path: Path):
    repo = tmp_path / "repo"
    repo.mkdir()
    (repo / "a.py").write_text(
        """
def f(x):
    if x > 0:
        return x
    return 0
""".strip(),
        encoding="utf-8",
    )

    out = tmp_path / "out"
    run_pipeline(repo_root=str(repo), base_output=str(out))

    assert (out / "reports" / "analyzer_result.json").exists()
    assert (out / "patches" / "refactor_suggestions.md").exists()
    assert (out / "reports" / "test_result.json").exists()
    assert (out / "reports" / "final_report.md").exists()

from pathlib import Path

from core.complexity_metrics import summarize_file_metrics


def test_summarize_file_metrics_detects_functions(tmp_path: Path):
    p = tmp_path / "demo.py"
    p.write_text(
        """
def foo(x):
    if x > 0:
        return x
    return -x
""".strip(),
        encoding="utf-8",
    )

    summary = summarize_file_metrics(str(p))
    assert summary["function_count"] == 1
    assert summary["max_complexity"] >= 2

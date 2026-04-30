from __future__ import annotations

import argparse
from pathlib import Path

from agents.analyzer_agent import AnalyzerAgent
from agents.refactor_agent import RefactorAgent
from agents.report_agent import ReportAgent
from agents.test_agent import TestAgent


def run_pipeline(repo_root: str, base_output: str = "outputs") -> None:
    out_root = Path(base_output)
    analyzer_json = out_root / "reports" / "analyzer_result.json"
    suggestion_md = out_root / "patches" / "refactor_suggestions.md"
    test_json = out_root / "reports" / "test_result.json"
    final_report_md = out_root / "reports" / "final_report.md"

    analyzer = AnalyzerAgent()
    refactor = RefactorAgent()
    tester = TestAgent()
    reporter = ReportAgent()

    analyzer_result = analyzer.run(repo_root=repo_root, output_json=str(analyzer_json))
    refactor_result = refactor.run(analyzer_json=str(analyzer_json), output_md=str(suggestion_md))
    test_result = tester.run(repo_root=repo_root, output_json=str(test_json))
    report_result = reporter.run(
        analyzer_json=str(analyzer_json),
        test_json=str(test_json),
        output_md=str(final_report_md),
    )

    print("Pipeline finished")
    print(f"Scanned files: {analyzer_result['scanned_files']}")
    print(f"Risk count: {refactor_result['risk_count']}")
    print(f"Tests passed: {test_result['passed']}")
    print(f"Recommendation: {report_result['recommendation']}")
    print(f"Report: {report_result['report_file']}")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Run multi-agent refactor guard pipeline")
    parser.add_argument("--repo", required=True, help="Target repository path to analyze")
    parser.add_argument("--output", default="outputs", help="Output directory")
    return parser.parse_args()


if __name__ == "__main__":
    args = parse_args()
    run_pipeline(repo_root=args.repo, base_output=args.output)

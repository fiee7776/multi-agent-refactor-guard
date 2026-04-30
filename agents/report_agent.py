from __future__ import annotations

import json
from pathlib import Path
from typing import Dict


class ReportAgent:
    def run(self, analyzer_json: str, test_json: str, output_md: str) -> Dict[str, object]:
        analyzer = json.loads(Path(analyzer_json).read_text(encoding="utf-8"))
        test_result = json.loads(Path(test_json).read_text(encoding="utf-8"))

        risks = analyzer.get("risks", [])
        passed = test_result.get("passed", False)
        recommendation = "GO" if passed and len(risks) < 5 else "REVIEW"

        lines = [
            "# Final Report",
            "",
            f"- Scanned files: {analyzer.get('scanned_files', 0)}",
            f"- Risky functions: {len(risks)}",
            f"- Tests passed: {passed}",
            f"- Recommendation: {recommendation}",
            "",
            "## Top Risks",
        ]

        if risks:
            for item in risks[:10]:
                lines.append(
                    f"- {item['file']}::{item['function']} (complexity={item['complexity']}, length={item['length']})"
                )
        else:
            lines.append("- No high-risk functions found.")

        out = Path(output_md)
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_text("\n".join(lines) + "\n", encoding="utf-8")

        return {
            "recommendation": recommendation,
            "report_file": str(out),
        }

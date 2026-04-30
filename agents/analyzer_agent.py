from __future__ import annotations

import json
from pathlib import Path
from typing import Dict

from core.complexity_metrics import summarize_file_metrics
from core.repo_scanner import iter_python_files
from core.risk_rules import detect_risky_functions


class AnalyzerAgent:
    def run(self, repo_root: str, output_json: str) -> Dict[str, object]:
        root = Path(repo_root).resolve()
        files = list(iter_python_files(root))

        file_summaries = []
        risks = []
        for file_path in files:
            summary = summarize_file_metrics(str(file_path))
            summary["file"] = str(file_path.relative_to(root))
            file_summaries.append(summary)
            risks.extend(detect_risky_functions(summary))

        result = {
            "repo_root": str(root),
            "scanned_files": len(files),
            "file_summaries": file_summaries,
            "risks": risks,
        }

        out = Path(output_json)
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_text(json.dumps(result, indent=2), encoding="utf-8")
        return result

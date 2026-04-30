from __future__ import annotations

import json
from pathlib import Path
from typing import Dict

from core.patch_engine import build_refactor_suggestions


class RefactorAgent:
    def run(self, analyzer_json: str, output_md: str) -> Dict[str, object]:
        analyzer_result = json.loads(Path(analyzer_json).read_text(encoding="utf-8"))
        risks = analyzer_result.get("risks", [])
        suggestions = build_refactor_suggestions(risks)

        out = Path(output_md)
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_text(suggestions, encoding="utf-8")

        return {
            "risk_count": len(risks),
            "suggestion_file": str(out),
        }

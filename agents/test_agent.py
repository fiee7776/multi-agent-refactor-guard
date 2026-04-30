from __future__ import annotations

import json
from pathlib import Path
from typing import Dict

from core.test_runner import run_pytest


class TestAgent:
    def run(self, repo_root: str, output_json: str) -> Dict[str, object]:
        result = run_pytest(repo_root)
        out = Path(output_json)
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_text(json.dumps(result, indent=2), encoding="utf-8")
        return result

from __future__ import annotations

from typing import Dict, List


DEFAULT_RULES = {
    "complexity_threshold": 8,
    "length_threshold": 40,
}


def detect_risky_functions(file_summary: Dict[str, object], rules: Dict[str, int] | None = None) -> List[Dict[str, object]]:
    cfg = {**DEFAULT_RULES, **(rules or {})}
    risky: List[Dict[str, object]] = []

    for fn in file_summary.get("functions", []):
        reasons = []
        if fn["complexity"] >= cfg["complexity_threshold"]:
            reasons.append(f"high complexity ({fn['complexity']})")
        if fn["length"] >= cfg["length_threshold"]:
            reasons.append(f"long function ({fn['length']} lines)")

        if reasons:
            risky.append(
                {
                    "file": file_summary["file"],
                    "function": fn["name"],
                    "lineno": fn["lineno"],
                    "complexity": fn["complexity"],
                    "length": fn["length"],
                    "reasons": reasons,
                }
            )

    return risky

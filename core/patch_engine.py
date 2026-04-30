from __future__ import annotations

from typing import Dict, List


def build_refactor_suggestions(risks: List[Dict[str, object]]) -> str:
    if not risks:
        return "# Refactor Suggestions\n\nNo high-risk functions detected.\n"

    lines = ["# Refactor Suggestions", ""]
    for idx, risk in enumerate(risks, start=1):
        lines.append(f"## {idx}. {risk['function']}")
        lines.append(f"- File: `{risk['file']}`")
        lines.append(f"- Line: {risk['lineno']}")
        lines.append(f"- Complexity: {risk['complexity']}")
        lines.append(f"- Length: {risk['length']} lines")
        lines.append(f"- Reasons: {', '.join(risk['reasons'])}")
        lines.append("- Suggested actions:")
        lines.append("  - Extract nested branches into helper functions.")
        lines.append("  - Split validation / transformation / side-effects into separate steps.")
        lines.append("  - Add focused unit tests before and after refactor.")
        lines.append("")
    return "\n".join(lines)

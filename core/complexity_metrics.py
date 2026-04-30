from __future__ import annotations

import ast
from dataclasses import dataclass
from pathlib import Path
from typing import Dict, List


@dataclass
class FunctionMetric:
    name: str
    lineno: int
    end_lineno: int
    branch_nodes: int

    @property
    def complexity(self) -> int:
        # Cyclomatic approximation: 1 + branch-like nodes.
        return 1 + self.branch_nodes

    @property
    def length(self) -> int:
        return max(1, self.end_lineno - self.lineno + 1)


class _BranchCounter(ast.NodeVisitor):
    BRANCH_TYPES = (
        ast.If,
        ast.For,
        ast.AsyncFor,
        ast.While,
        ast.Try,
        ast.ExceptHandler,
        ast.With,
        ast.AsyncWith,
        ast.BoolOp,
        ast.IfExp,
        ast.Match,
        ast.comprehension,
    )

    def __init__(self) -> None:
        self.count = 0

    def generic_visit(self, node: ast.AST) -> None:
        if isinstance(node, self.BRANCH_TYPES):
            self.count += 1
        super().generic_visit(node)


def extract_function_metrics(file_path: str) -> List[FunctionMetric]:
    src = Path(file_path).read_text(encoding="utf-8")
    tree = ast.parse(src)
    metrics: List[FunctionMetric] = []

    for node in ast.walk(tree):
        if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)):
            end_lineno = getattr(node, "end_lineno", node.lineno)
            counter = _BranchCounter()
            counter.visit(node)
            metrics.append(
                FunctionMetric(
                    name=node.name,
                    lineno=node.lineno,
                    end_lineno=end_lineno,
                    branch_nodes=counter.count,
                )
            )
    return metrics


def summarize_file_metrics(file_path: str) -> Dict[str, object]:
    functions = extract_function_metrics(file_path)
    if not functions:
        return {
            "file": file_path,
            "function_count": 0,
            "avg_complexity": 0,
            "max_complexity": 0,
            "functions": [],
        }

    avg_complexity = round(sum(f.complexity for f in functions) / len(functions), 2)
    max_complexity = max(f.complexity for f in functions)
    return {
        "file": file_path,
        "function_count": len(functions),
        "avg_complexity": avg_complexity,
        "max_complexity": max_complexity,
        "functions": [
            {
                "name": f.name,
                "lineno": f.lineno,
                "end_lineno": f.end_lineno,
                "length": f.length,
                "complexity": f.complexity,
            }
            for f in functions
        ],
    }

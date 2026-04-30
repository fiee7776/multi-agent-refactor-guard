from __future__ import annotations

from pathlib import Path
from typing import Iterable, List

EXCLUDED_DIRS = {
    ".git",
    ".venv",
    "venv",
    "__pycache__",
    "node_modules",
    "outputs",
}


def iter_python_files(repo_root: Path) -> Iterable[Path]:
    """Yield Python files under repo_root while skipping noisy directories."""
    for path in repo_root.rglob("*.py"):
        if any(part in EXCLUDED_DIRS for part in path.parts):
            continue
        yield path


def list_python_files(repo_root: str) -> List[str]:
    root = Path(repo_root).resolve()
    return [str(p.relative_to(root)) for p in iter_python_files(root)]

from __future__ import annotations

import subprocess
from pathlib import Path
from typing import Dict


def run_pytest(repo_root: str) -> Dict[str, object]:
    root = Path(repo_root).resolve()
    cmd = ["pytest", "-q"]
    completed = subprocess.run(
        cmd,
        cwd=str(root),
        capture_output=True,
        text=True,
        shell=False,
        check=False,
    )
    return {
        "command": " ".join(cmd),
        "returncode": completed.returncode,
        "stdout": completed.stdout,
        "stderr": completed.stderr,
        "passed": completed.returncode == 0,
    }

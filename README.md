# Multi Agent Refactor Guard

A runnable Python project that demonstrates a multi-agent workflow for code quality governance.

## What It Does

- Analyzer Agent scans Python files and computes simple complexity metrics.
- Refactor Agent generates actionable refactor suggestions and patch drafts.
- Test Agent runs pytest and captures output.
- Report Agent produces a markdown summary for decisions.
- Orchestrator coordinates all stages and writes outputs to `outputs/`.

## Quick Start

```powershell
cd <repo-root>
pip install -r requirements.txt
python -m agents.orchestrator --repo examples/sample_repo
```

## Run Tests

```powershell
cd <repo-root>
pytest -q
```

Replace `<repo-root>` with the path where you cloned or unpacked this repository.

## Output Files

- `outputs/reports/analyzer_result.json`
- `outputs/patches/refactor_suggestions.md`
- `outputs/reports/test_result.json`
- `outputs/reports/final_report.md`

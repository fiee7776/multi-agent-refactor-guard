#!/usr/bin/env bash
set -euo pipefail

REPO_PATH="${1:-examples/sample_repo}"
OUTPUT_PATH="${2:-outputs}"

python -m agents.orchestrator --repo "$REPO_PATH" --output "$OUTPUT_PATH"

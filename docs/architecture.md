# Architecture

## Components
- `agents/`: role-based orchestration nodes.
- `core/`: shared capabilities like scanning, metrics, tests, and reporting utilities.
- `outputs/`: generated machine- and human-readable artifacts.

## Data Flow
Analyzer -> Refactor -> Test -> Report

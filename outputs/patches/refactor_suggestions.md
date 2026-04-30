# Refactor Suggestions

## 1. process_orders
- File: `app.py`
- Line: 1
- Complexity: 11
- Length: 21 lines
- Reasons: high complexity (11)
- Suggested actions:
  - Extract nested branches into helper functions.
  - Split validation / transformation / side-effects into separate steps.
  - Add focused unit tests before and after refactor.

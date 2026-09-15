# AGENTS.md - Repository Guardrails

## 1. Workflow & Planning
- For non-trivial features, update or create `TASK_PLAN.md` before writing code.
- Ask for human confirmation after updating `TASK_PLAN.md` before making file edits.
- Work on ONE sub-task at a time. Do not attempt multi-step implementations simultaneously.

## 2. Token Budget & Terminal Safety
- Run commands in silent/quiet mode (e.g., `npm test -- --silent` or `pytest -q`).
- NEVER output more than 50 lines of log output. If a command prints excessive logs, pipe or filter it.
- Never cat large files. Search for specific line numbers or functions instead.

## 3. Failure Circuit Breaker
- If a test or build command fails 2 times sequentially:
  1. STOP modifying source files.
  2. Preserve the current working state and collect the relevant error output.
  3. Report the error and ask the user for guidance before making further changes.

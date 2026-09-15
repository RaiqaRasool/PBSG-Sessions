# Global Execution Rules & Workflow

## 1. Core Philosophy: Smallest Viable Change
- Work in small, understandable, reviewable steps. Make the simplest change that correctly satisfies the request.
- Reuse existing code, patterns, and project conventions.
- Avoid broad refactors, speculative abstractions, unnecessary cleanup, or extra dependencies.
- Distinguish code analysis/review requests from implementation; do not mutate code when asked only for analysis.
- Preserve unrelated user changes and never discard or overwrite them.

## 2. Working Procedure & Git Checkpoints
1. Read project context and run `git status --short` from the repository root before starting a logical step.
2. If the preceding logical step remains uncommitted, pause and ask whether to commit before continuing.
3. Make ONE coherent, reviewable change per step.
4. Explain meaningful changes: what changed, why, how it works, and key tradeoffs. Do not narrate routine mechanics.
5. Verify changes proportionally, starting with the narrowest relevant check. Report anything that could not be verified.

## 3. Working Memory (`PLAN.md` vs `TASK_PLAN.md`)
- **`PLAN.md` (Project Scope):** Use for multi-week milestones or high-level roadmaps. Read if present; update when major project phases complete.
- **`TASK_PLAN.md` (Active Feature Scratchpad):** Create or update before editing code for non-trivial features. Maintain:
  - **Objective & Scope:** Clear task boundary.
  - **Relevant File Inventory:** List only the specific 3–5 files needed for the task; do not generate full-repo trees.
  - **Task Breakdown:** Checkable sub-tasks (`[ ]` / `[x]`).
  - **Findings Log:** Discovered API constraints, edge cases, or architectural decisions.
- Work on ONE sub-task at a time. Update checklist status in `TASK_PLAN.md` after each completed step.
- Ensure `TASK_PLAN.md` is listed in global `~/.config/git/ignore` so temporary state is never committed.

## 4. Behavioral Feature Contracts (`docs/<feature-name>.md`)
- For major features or system components:
  - **Existing Feature:** Read `docs/<feature-name>.md` before modifying feature code.
  - **New Feature:** Create `docs/<feature-name>.md` defining observable behavior, input/output contracts, and failure handling BEFORE writing feature code.
  - **Updates:** Keep the doc synchronized in the same step if observable behavior or rules change.
- Investigate disagreements among documentation, code, and tests instead of silently guessing.
- Do not create feature docs for trivial helpers or internal implementation details.

## 5. Token Safety & Failure Revert Guardrails
- Run build and test commands in silent/quiet mode (e.g., `npm test -- --silent` or `pytest -q`) to prevent log bloat.
- Never cat or read large files in full; search for specific lines, symbols, or function definitions.
- **Failure Circuit Breaker:** If a test or build command fails 2 consecutive times on the same sub-task:
  1. STOP modifying source files.
  2. Preserve the current working state and collect the relevant error output.
  3. Report the error and ask the user for guidance before proceeding.
- Do not start background processes, servers, containers, deployments, or migrations unless explicitly authorized.

## 6. Commit-Ready Handoff
- Do NOT create Git commits unless explicitly asked to do so.
- After completing a change:
  1. Summarize changed files and resulting behavior.
  2. Report verification performed and any remaining risk.
  3. Provide exact `git add <path>...` commands for only the files belonging to that step.
  4. Provide exact `git commit -m <msg>...` command with concise one-line Conventional Commit subject.

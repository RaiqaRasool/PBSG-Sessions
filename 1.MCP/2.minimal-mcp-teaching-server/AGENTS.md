# Project Working Agreement

## Purpose

This repository builds a minimal, containerized MCP teaching server. Keep the implementation small and make each protocol concept easy to inspect and explain.

## User-Run Commands Only

- Do not execute shell commands on the user's behalf.
- Do not run Git, Docker, Docker Compose, Python, `uv`, Node.js, npm, MCP Inspector, tests, servers, formatters, linters, builds, installations, or deployments.
- When a command is needed, explain why, provide the exact command and working directory, and ask the user to run it.
- Wait for the user to paste the command output before relying on its result or continuing to a dependent step.
- Do not claim that a build, test, server, container, or MCP interaction succeeded unless the user's reported output demonstrates it.
- Requested file creation and editing may be performed directly; the command restriction applies to execution and verification.

## Start From the Project

1. Read this file and the relevant project documentation before proposing changes.
2. Ask the user to run `git status --short` from the repository root before each logical change.
3. Inspect the relevant implementation, tests, documentation, and user-provided command output before editing.
4. Preserve unrelated changes. Never discard or overwrite user work.
5. If the preceding logical change remains uncommitted, stop at that checkpoint and ask whether the user wants to commit before continuing.

## Make the Smallest Viable Change

- Prefer standard-library and native platform features.
- Reuse existing project patterns before introducing anything new.
- Avoid speculative abstractions, extra dependencies, unrelated cleanup, and premature production infrastructure.
- Keep the first server local, file-backed, and connected over MCP `stdio`.
- Do not add Streamable HTTP, authentication, a database, a custom MCP client, or deployment infrastructure unless explicitly requested.
- Never simplify away validation, error handling that protects data, or protocol correctness.

## Work One Checkpoint at a Time

1. State the immediate checkpoint and its boundary.
2. Make one coherent, reviewable file change.
3. Explain what changed, why it is required, and how it works.
4. Give the user the narrowest verification command and its working directory.
5. Wait for the resulting output and assess it.
6. Ask the user to run `git status --short` after verification.
7. Pause at the commit boundary before beginning the next checkpoint.

The intended implementation sequence is:

1. Dockerized Python project and empty MCP `stdio` handshake.
2. Markdown-backed MCP Resource.
3. Validated update Tool and failure behavior.
4. Reusable status-review Prompt.
5. End-to-end MCP Inspector verification.
6. Optional connection to Codex or another MCP-capable host.

## Behavioral Feature Contracts

- Maintain concise feature contracts in `docs/<feature-name>.md` for independently meaningful behavior.
- Read the relevant contract before changing that feature.
- Update the contract in the same checkpoint when observable behavior, boundaries, failure handling, or verification changes.
- Keep contracts behavioral and concise; do not document trivial helpers or line-by-line implementation details.
- Resolve disagreements among documentation, implementation, and verification evidence instead of silently choosing one.

## MCP and Docker Rules

- Keep MCP protocol messages on stdout and send diagnostics to stderr.
- Do not use ordinary stdout `print()` calls for debugging a `stdio` server.
- Run containerized MCP stdio without allocating a TTY; Docker Compose commands should use `-T`.
- Keep stdin attached so MCP Inspector can communicate with the server.
- Persist `project-status.md` outside disposable containers through the project bind mount.
- Pin direct dependencies and commit the lockfile for reproducibility.

## Commit-Ready Handoff

Do not create commits unless the user explicitly asks.

After each verified checkpoint:

1. Summarize the changed files and resulting behavior.
2. Report the verification evidence and any remaining risk.
3. Provide an exact `git add <path>...` command containing only files from that checkpoint.
4. Provide one concise Conventional Commit subject.
5. Ask whether the user wants to commit before continuing.

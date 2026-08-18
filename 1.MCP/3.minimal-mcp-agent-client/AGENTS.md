# Project Working Agreement

## Purpose

This repository builds a minimal teaching agent that makes the boundary between model decisions and MCP client operations visible. Keep the orchestration loop explicit and easy to inspect.

## User-Run Commands Only

- Do not execute Git, Docker, Docker Compose, Python, `uv`, tests, builds, installations, servers, or deployments.
- Read-only file inspection and Git inspection are allowed.
- When a command is needed, provide its exact working directory, command, and reason.
- Wait for the user to paste the output before relying on it or continuing to a dependent step.
- Requested file creation and editing may be performed directly.

## Start From the Project

1. Read this file, `.agents-cli-spec.md`, and relevant feature documentation before proposing changes.
2. Ask the user to run `git status --short` before each logical change.
3. Inspect relevant implementation, tests, documentation, and user-provided output before editing.
4. Preserve unrelated changes.
5. Stop at an uncommitted checkpoint and ask whether the user wants to commit before continuing.

## Make the Smallest Viable Change

- Use Python 3.12, `uv`, Docker, and Docker Compose.
- Keep the agent loop framework-free and explicit.
- Use the existing Phoenix server over MCP stdio.
- Keep the first version read-only; do not expose the Phoenix update tool to the model.
- Do not add Streamable HTTP, a web UI, deployment, memory, multi-agent orchestration, a database, or authentication beyond the OpenAI API key.
- Never log secrets or claim to expose hidden chain-of-thought.

## Container Boundary

- Run the agent in its own container.
- Bind-mount the existing Phoenix `server.py` and `project-status.md` from the sibling teaching-server repository.
- Launch the mounted Phoenix server directly as the agent container's stdio child.
- Do not mount the Docker socket or run Docker from inside the agent container.
- Keep MCP protocol messages on the child process's stdout and diagnostics on stderr.

## Work One Checkpoint at a Time

1. State the checkpoint and boundary.
2. Make one coherent, reviewable change.
3. Explain what changed, why, and how it works.
4. Give the narrowest user-run verification command.
5. Wait for pasted output and assess it.
6. Ask for `git status --short` after verification.
7. Pause at the commit boundary.

The intended sequence is:

1. Dockerized Python project and MCP client initialization.
2. Read-only Phoenix resource discovery and reading.
3. Explicit model request and decision translation.
4. MCP result return and final model response.
5. End-to-end observable trace.

## Behavioral Feature Contracts

- Maintain concise contracts in `docs/<feature-name>.md` for independently meaningful behavior.
- Update the relevant contract in the same checkpoint as observable behavior changes.
- Keep contracts behavioral rather than line-by-line implementation documentation.

## Commit-Ready Handoff

Do not create commits unless explicitly asked. After each verified checkpoint:

1. Summarize changed files and behavior.
2. Report verification evidence and remaining risk.
3. Provide an exact path-limited `git add` command.
4. Provide one concise Conventional Commit subject.

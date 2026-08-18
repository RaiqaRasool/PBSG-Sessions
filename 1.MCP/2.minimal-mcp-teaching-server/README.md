# Minimal MCP Teaching Server

A small Python MCP server that uses Docker, FastMCP, and `stdio`. Project state
lives in the host-visible `project-status.md` file.

The server exposes:

- Resource: `project://phoenix/status`
- Read-only tool: `find_project_updates(author)`
- Tool: `add_project_update`
- Prompt: `prepare_status_review`

## Prerequisites

- Docker with Docker Compose
- Node.js and npm for MCP Inspector
- Codex CLI for the optional Codex connection

Run all commands below from the repository root.

## Build the Server

```bash
docker compose build server
```

The build installs the exact Python dependencies recorded in `uv.lock`.
Compose bind-mounts `server.py` and `project-status.md`, so later source and
status changes do not require another image build.

## Inspect the Server with MCP Inspector

Start MCP Inspector on the host and have it launch the server container:

```bash
HOST=127.0.0.1 npx -y @modelcontextprotocol/inspector docker compose run --rm -T server
```

The command uses:

- `HOST=127.0.0.1` to expose Inspector only on the local machine.
- `npx -y` to download and run Inspector without adding it to this project.
- `docker compose run` to launch the MCP server as a subprocess.
- `--rm` to remove the temporary container when the session ends.
- `-T` to avoid a TTY, which would interfere with MCP `stdio` messages.

Inspector opens in the browser. Confirm that it connects, then use its
Resources, Tools, and Prompts screens to exercise the MCP capabilities.
Stop Inspector with `Ctrl+C`.

## Connect the Server to Codex

Register the server as a global Codex MCP connection:

```bash
codex mcp add phoenix-status -- docker compose -f "$PWD/compose.yaml" run --rm -T server
```

`$PWD` expands to the repository's absolute path when the command runs. This
lets Codex launch the Compose service even when a Codex task uses a different
working directory.

Inspect the saved connection:

```bash
codex mcp get phoenix-status
codex mcp list
```

Start a new Codex task after registration. Example requests:

```text
Use the phoenix-status MCP server to read project://phoenix/status.
```

```text
Use add_project_update from phoenix-status to append an update authored by me.
```

Codex launches a temporary server container for the MCP connection. The
container reads and writes the same host `project-status.md` file used by
Inspector.

To remove the Codex connection:

```bash
codex mcp remove phoenix-status
```

# MCP Server

## Purpose

Provide a minimal MCP server that clients can launch as a Docker container and
communicate with through standard input and standard output.

## Main Flow

1. Docker Compose builds the Python 3.12 image from the locked dependencies.
2. The container starts the FastMCP application in `stdio` mode.
3. An MCP client sends protocol messages on stdin and receives responses on
   stdout.

## Expected Behavior

- The server identifies itself as `Project Status`.
- The server uses MCP `stdio`; it does not open an HTTP port.
- The container keeps stdin open and does not allocate a TTY.
- Stdout is reserved for MCP protocol messages.
- Docker Compose mounts `server.py` read-only so a newly launched development
  container uses the current host source without rebuilding the image.
- The built image retains its own copy of `server.py` and can run without the
  development bind mount.
- The server exposes the Project Phoenix status resource, read-only update
  search tool, update tool, and status-review prompt.

## Failure Behavior

- Image creation fails when the lockfile and dependency manifest disagree.
- Server startup fails instead of silently changing the locked environment.
- Protocol communication ends when the client closes the stdio connection.

## Key Components

- `server.py`: creates and runs the FastMCP application.
- `Dockerfile`: defines the locked Python runtime.
- `compose.yaml`: defines the stdio-compatible development service.

## Verification

- Build the Compose service from the committed dependency lockfile.
- Launch it through MCP Inspector and complete an MCP initialization handshake.
- Confirm that resource discovery returns the Project Phoenix status resource.
- Confirm that tool discovery returns `find_project_updates` and
  `add_project_update`.
- Confirm that prompt discovery returns `prepare_status_review`.

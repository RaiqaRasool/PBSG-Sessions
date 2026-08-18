# Project Status Resource

## Purpose

Let MCP clients read the current Project Phoenix status from a host-visible
Markdown file.

## Main Flow

1. A client discovers the resource at `project://phoenix/status`.
2. The client reads the resource through MCP.
3. The server decodes `project-status.md` as UTF-8 and returns its contents as
   `text/markdown`.

## Expected Behavior

- The returned text exactly matches `project-status.md`.
- The container reads the host file through a bind mount shared with the update
  tool.
- Reading the resource does not modify project state.

## Failure Behavior

- A missing or unreadable status file produces a clear MCP resource error.
- Content that is not valid UTF-8 produces a clear MCP resource error.
- The server does not return fallback or fabricated status content.

## Key Components

- `project-status.md`: stores the host-visible project status.
- `server.py`: registers and reads the MCP resource.
- `compose.yaml`: mounts the server source and status file into development
  containers.

## Verification

- Discover `project://phoenix/status` with MCP Inspector.
- Read it and compare the returned text with `project-status.md`.

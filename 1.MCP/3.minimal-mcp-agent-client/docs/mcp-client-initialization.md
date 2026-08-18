# MCP Client Initialization

## Purpose

Establish a visible MCP client lifecycle between the teaching client and the existing Phoenix server before adding model behavior.

## Main Flow

1. Docker Compose starts the teaching client container.
2. The client launches the mounted Phoenix server as a child process.
3. The MCP SDK connects to the child over stdio.
4. The client sends the MCP initialization exchange and prints the server identity.
5. Both sessions close when initialization completes.

## Expected Behavior

- The client and Phoenix server run in the same container but remain separate processes connected only through MCP stdio.
- The Phoenix source and status file remain owned by the sibling teaching-server repository.
- The status file is mounted read-only.
- Human-readable client output does not share the child server's protocol stdout.
- The child server's stderr is suppressed so framework diagnostics do not obscure the teaching trace.
- Initialization completes before resource reads, tool calls, prompt retrieval, or model requests can occur.

## Failure Behavior

- A missing sibling server file or status file prevents the Compose container from starting correctly.
- A server startup or MCP initialization failure exits the client with a non-zero status and exposes the SDK error.

## Key Components

- `client.py`
- `compose.yaml`
- `Dockerfile`
- `../minimal-mcp-teaching-server/server.py`

## Verification

Build the image, then run the Compose service without a TTY. Successful output identifies the initialized Phoenix FastMCP server and the process exits cleanly.

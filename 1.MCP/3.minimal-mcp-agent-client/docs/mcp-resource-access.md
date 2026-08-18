# MCP Resource Access

## Purpose

Dynamically expose resources advertised by the connected MCP server to the model without hardcoded resource URIs or server-specific function mappings.

## Main Flow

1. The client completes MCP initialization.
2. The client requests the server's resource list and builds a URI-keyed catalog.
3. The agent creates one `read_mcp_resource` function whose required `uri` argument is restricted to the catalog URIs with a JSON Schema enum.
4. The model selects an advertised URI when current resource data is relevant.
5. The agent validates the function name, argument shape, and catalog membership.
6. The MCP client reads the selected URI once and returns its serialized contents to the model.

## Expected Behavior

- Trace labels distinguish agent mappings from `MCP CLIENT -> MCP SERVER` requests and `MCP SERVER -> MCP CLIENT` results for `resources/list` and `resources/read`.
- Resource selection uses an exact URI advertised by the current server.
- MCP tool exposure is governed separately by dynamic tool discovery; no
  hardcoded Phoenix resource mapping is exposed here.
- The mounted resource state remains read-only.

## Failure Behavior

- If the server advertises no resources, the client exits before calling the model.
- Unsupported function names, malformed arguments, and unadvertised URIs are rejected instead of executed.
- MCP discovery and read failures propagate as non-zero process failures.

## Key Components

- `client.py`
- The connected MCP server's `resources/list` and `resources/read` handlers

## Verification

Run the Compose agent with a question that requires an advertised resource. The trace must show a dynamically enumerated URI, one model call to `read_mcp_resource`, one matching MCP resource read, returned contents, and a final answer.

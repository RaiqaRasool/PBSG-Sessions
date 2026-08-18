# MCP Tool Access

## Purpose

Dynamically translate every discovered MCP tool into a model function.

## Main Flow

1. The client requests `tools/list` from the connected MCP server.
2. Each tool's description and input schema become a model function.
4. The model may request one function with arguments.
5. The agent validates the function name and argument shape against the
   discovered catalog before sending `tools/call`.
6. The serialized MCP result returns to the model as `function_call_output`.

## Expected Behavior

- `find_project_updates` and `add_project_update` are dynamically described
  from their discovered MCP tool metadata.
- Mutating tools may change server state when the model calls them.
- The trace shows discovery, exposure decisions, model arguments, validation,
  the MCP call, and the returned function output.
- Existing resource access remains available in the same model request.

## Failure Behavior

- Undiscovered function names are rejected before `tools/call`.
- Non-object arguments, unknown properties, missing required properties, and
  non-string values for advertised string properties are rejected.
- MCP discovery and call failures remain non-zero process failures.

## Key Components

- `client.py`
- The connected MCP server's `tools/list` and `tools/call` handlers

## Verification

Run the agent with a question asking for updates by an author. The trace must
show `find_project_updates` exposed from `tools/list`, the model function call,
one matching `tools/call`, its result returned as `function_call_output`, and a
final answer. A question that explicitly requests an update must expose and call
`add_project_update` with both required arguments.

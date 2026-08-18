# Local Model Agent Loop

## Purpose

Expose the observable communication between a local model, the agent loop, and the MCP client without hiding orchestration inside an agent framework.

## Main Flow

1. The CLI accepts one user question.
2. The agent discovers the connected server's resources and tools.
3. The agent presents `read_mcp_resource` and every discovered MCP tool to LM Studio's OpenAI-compatible Responses endpoint.
4. If the model requests a function, the agent validates its name and arguments before mapping it to the matching MCP operation.
5. The agent returns the MCP result to the model as `function_call_output`.
6. The model produces the final answer for the user.

## Expected Behavior

- Directional trace labels distinguish user, agent, model, and MCP-client boundaries.
- Logs expose API output item types and function-call arguments, not hidden chain-of-thought.
- The model receives the resource read function and every dynamically
  translated MCP tool.
- Mutating MCP tools may change server state when selected by the model.
- Questions unrelated to Phoenix may complete without an MCP resource read.
- The LM Studio base URL defaults to `http://host.docker.internal:1234/v1` for the Dockerized client.
- `LM_STUDIO_MODEL` must identify a model available through the running LM Studio server.
- The placeholder API key defaults to `lm-studio`; a real token can be supplied through `OPENAI_API_KEY` if LM Studio authentication is enabled.

## Failure Behavior

- A missing `LM_STUDIO_MODEL` causes a clear startup error before inference.
- An unavailable LM Studio server or model propagates as an API failure.
- Unsupported function names or unexpected arguments are rejected instead of executed.
- MCP discovery, resource, and tool failures remain non-zero process failures.

## Key Components

- `client.py`
- `compose.yaml`
- `pyproject.toml`

## Verification

With LM Studio serving a tool-capable model, run the Compose agent with a Phoenix status question and an author-update question. Each trace must show the selected model function, one matching MCP operation, one function output returned to the model, and a final answer.

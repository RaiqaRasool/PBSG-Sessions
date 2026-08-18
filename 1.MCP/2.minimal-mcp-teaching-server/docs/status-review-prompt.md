# Status Review Prompt

## Purpose

Give MCP users reusable instructions for turning the Project Phoenix status
resource into a review tailored to a specific audience and focus.

## Main Flow

1. A client selects `prepare_status_review`.
2. The client supplies an `audience` and `focus` from their allowed values.
3. The server returns one MCP user prompt message instructing the host to read
   `project://phoenix/status` and prepare the review.

## Expected Behavior

- `audience` accepts only `engineering` or `leadership`.
- `focus` accepts only `blockers`, `progress`, or `risks`.
- MCP prompt discovery lists argument names rather than a JSON Schema, so the
  prompt description also states the allowed values for clients and users.
- Python `Literal` annotations enforce the allowed values when the client gets
  the rendered prompt.
- Engineering reviews request implementation detail, dependencies, owners, and
  next actions.
- Leadership reviews request concise outcomes, impact, decisions, and
  escalation needs.
- The selected focus changes which information the review prioritizes.
- The message requires grounding in the Resource and labels missing information
  instead of inviting invented details.
- Preparing the prompt does not read or modify project state itself.

## Failure Behavior

- Values outside either allowed set fail MCP argument validation.
- Invalid arguments do not produce a fallback prompt.

## Key Components

- `server.py`: declares the argument schema and builds the prompt message.
- `project://phoenix/status`: supplies status content when the host follows the
  returned instructions.

## Verification

- Discover `prepare_status_review` with MCP Inspector and confirm its arguments
  are required and its description states both sets of allowed values.
- Get the prompt for each audience and focus value and confirm the returned
  message contains the corresponding guidance.
- Submit an invalid audience and focus and confirm each is rejected.

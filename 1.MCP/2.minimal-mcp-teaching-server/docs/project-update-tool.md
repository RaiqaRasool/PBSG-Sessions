# Project Update Tool

## Purpose

Let MCP clients append dated progress information to the host-visible Project
Phoenix status file.

## Main Flow

1. A client calls `add_project_update` with `update` and `author` strings.
2. The server trims and validates both values.
3. The server appends one UTC-dated Markdown section to `project-status.md`.
4. The tool returns a confirmation containing the normalized author and date.

## Expected Behavior

- `update` must contain non-whitespace text and may span multiple lines.
- `author` must contain non-whitespace text and must be a single line.
- Validation completes before the file is opened for writing.
- Each successful call preserves existing content and appends one section.
- The Resource reflects successful updates because both features use the same
  bind-mounted file.

## Failure Behavior

- Invalid input produces a clear MCP tool error and does not modify the file.
- A missing, read-only, or otherwise unwritable status file produces a clear
  MCP tool error.
- The server does not report success when the append operation fails.

## Key Components

- `server.py`: validates input and implements the append operation.
- `project-status.md`: stores the appended updates.
- `compose.yaml`: makes the host status file writable inside the container.

## Verification

- Discover `add_project_update` with MCP Inspector and inspect its input schema.
- Submit a valid call and confirm the file and Resource contain one new section.
- Submit blank `update`, blank `author`, and multiline `author` values; confirm
  each call fails without changing the file.

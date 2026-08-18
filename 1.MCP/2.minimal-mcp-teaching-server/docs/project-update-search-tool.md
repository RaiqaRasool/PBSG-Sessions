# Project Update Search Tool

## Purpose

Let MCP clients find Project Phoenix updates written by one author without
modifying project state.

## Main Flow

1. A client calls `find_project_updates` with an author string.
2. The server trims and validates the author.
3. The server reads `project-status.md` and returns matching dated update
   sections.

## Expected Behavior

- `author` must contain non-whitespace text and must be a single line.
- Matching uses the normalized author exactly and preserves each matching
  Markdown section.
- No match returns a clear message naming the requested author.
- Calling the tool never modifies `project-status.md`.

## Failure Behavior

- Invalid input produces a clear MCP tool error.
- A missing, unreadable, or invalid UTF-8 status file produces a clear MCP tool
  error.

## Key Components

- `server.py`: validates the author and searches the status file.
- `project-status.md`: stores the dated update sections.

## Verification

- Discover `find_project_updates` and confirm its schema requires one string
  `author` argument.
- Search for an author with updates and confirm only that author's dated
  sections are returned.
- Search for an unknown author and confirm the no-match message is returned.
- Submit blank and multiline authors and confirm each is rejected.

# Contributing

## Add a study-group session

1. Create a numbered topic directory such as `2.Agentic-Workflows`.
2. Add a `README.md` that states the session goal, prerequisites, outline, and links to its material.
3. Order notes and demos by the sequence in which they are presented.
4. Keep each runnable example self-contained and document its setup, configuration, and verification steps.
5. Never commit API keys, access tokens, credentials, personal data, or local environment files.
6. Add the new session to the session index in the root `README.md`.

## Commit style

Use concise [Conventional Commit](https://www.conventionalcommits.org/) subjects, for example:

```text
docs(session-2): add agent workflow notes
feat(session-2): add orchestration demo
fix(mcp-client): handle server disconnect
```

Keep unrelated changes in separate commits so examples and notes remain easy to review.

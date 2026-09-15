# Core Ideas

## What an agentic loop needs

An agentic loop begins with:

- **A trigger:** an event, schedule, or human instruction that starts the loop.
- **A verifiable goal:** a defined outcome the agent can work toward and evaluate.

A useful loop also needs a stopping condition. Give the agent a goal, a way to verify success—such as tests or lint checks—and a clear point at which it must stop or request human judgment.

## Loops and automations

An automation follows a predetermined sequence of steps. A loop makes decisions: it evaluates the current state, determines what to do next, checks the result, and adjusts.

## Three common triggers

1. **Event-based:** a pull request opens, a file changes, or an API call completes.
2. **Scheduled:** a recurring timer starts the work.
3. **Human-initiated:** a person provides a goal and starts the loop.

## Durable context

Chat context is temporary. Important goals, decisions, constraints, and progress should live in the repository when they need to survive across runs:

> The agent forgets; the repository does not.

Designing a loop can amplify good judgment or amplify its absence. The important question is not simply whether to automate, but where verification, limits, and human decisions belong.

## Primary reference

[Agentic Loops Explained: From ReAct to Loop Engineering](https://datasciencedojo.com/blog/agentic-loops-explained-from-react-to-loop-engineering-2026-guide/)

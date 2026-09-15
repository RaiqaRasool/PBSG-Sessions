# Outer Planning and Inner Execution Loops

One possible working model separates architectural reasoning from focused implementation.

```text
┌──────────────────────────────────────────────────────┐
│ Outer loop: planning and steering                    │
│                                                      │
│ • Discuss requirements and trade-offs                │
│ • Maintain durable behavioral documentation          │
│ • Write focused execution steps to TASK_PLAN.md       │
└─────────────────────────┬────────────────────────────┘
                          │ durable context on disk
                          ▼
┌──────────────────────────────────────────────────────┐
│ Inner loop: focused agent execution                  │
│                                                      │
│ • Read repository rules and the current task plan     │
│ • Inspect code, edit, test, and evaluate              │
│ • Stop at completion or a defined human checkpoint    │
└──────────────────────────────────────────────────────┘
```

## Inner execution loop

Within one task, an agent observes the repository, chooses an action, uses a tool, evaluates the result, and adjusts. This resembles a ReAct-style loop.

## Outer steering loop

The outer loop is the human and project-level process surrounding individual execution tasks. Repository instructions, behavioral documents, task plans, verification criteria, and Git checkpoints provide durable constraints and continuity.

## Potential benefits

- A focused execution task carries less irrelevant conversational history.
- Durable decisions survive when a chat or task ends.
- Verification and explicit checkpoints make failures easier to detect.
- Planning and implementation can be reviewed separately.

This is a workflow pattern to examine, not a universal prescription. The useful separation depends on the size, risk, and duration of the work.

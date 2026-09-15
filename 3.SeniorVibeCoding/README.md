# Senior Vibe Coding: An Interactive Exploration

This is an exploratory meetup session rather than a prepared lecture. The aim is to introduce several connected ideas, investigate whichever ones interest the room, and use the discussion to choose a direction for a later session.

## Minimal preparation

Before the meetup:

1. Open the introductory video and practical example in [Loop Engineering](loop-engineering.md).
2. Keep [Core Ideas](core-ideas.md) available as a concise reference.
3. Be ready to open the example [agent rules](common-agent-rules.md) and the suggestions in [Project Documentation](project-documentation.md).
4. Use [Resources](resources.md) only when the group wants a deeper reference.

No slides or complete demonstration are required.

## Suggested session flow

### 1. Frame the exploration — 5 minutes

Explain that “senior vibe coding” could lead into several topics: loop engineering, agent instructions, durable project context, verification, or multi-agent work. The group will sample these ideas and decide together what deserves a deeper follow-up.

Opening question:

> What makes working with a coding agent feel reliable rather than merely impressive?

### 2. Start with loop engineering — 10–15 minutes

Use the introductory material in [Loop Engineering](loop-engineering.md). Discuss the difference between repeatedly prompting an agent and designing an environment in which it can pursue and verify a goal.

Ask the room to identify:

- the trigger;
- the goal;
- the verification method;
- the stopping condition;
- the information that must persist between runs.

### 3. Examine a practical example — 15–20 minutes

Open the practical Codex loop example linked from [Loop Engineering](loop-engineering.md). Let participant questions determine how deeply to inspect it.

Possible prompts for the discussion:

- What decisions remain with the human?
- How does the agent know whether it succeeded?
- What could make this loop unsafe or wasteful?
- What belongs in the repository instead of the chat history?

### 4. Choose a branch — 15–25 minutes

Ask the group which topic they want to explore next:

1. **Agent rules:** Review [Common Agent Rules](common-agent-rules.md) and decide which instructions are genuinely useful.
2. **Project documentation:** Compare a minimal `AGENTS.md` plus `TASK_PLAN.md` approach with the suggestions in [Project Documentation](project-documentation.md).
3. **Loop design:** Use [Core Ideas](core-ideas.md) to design a loop for a real participant workflow.
4. **Agent architecture:** Discuss the outer planning loop and inner execution loop described in [Meta-Harness Notes](meta-harness.md).
5. **Further study:** Browse [Resources](resources.md) and select a future deep-dive topic.

The branch is intentionally chosen during the session; there is no requirement to cover every file.

### 5. Close with a decision — 5 minutes

End by asking:

> Which idea should we turn into a prepared, practical follow-up session?

Record the selected topic, one concrete question the next session should answer, and volunteers or examples the group can contribute.

## Material map

- [Loop Engineering](loop-engineering.md): starting links and practical examples
- [Core Ideas](core-ideas.md): short definitions and discussion anchors
- [Common Agent Rules](common-agent-rules.md): compact repository guardrails to critique
- [Global Agent Rules](global-agent-rules.md): a more complete workflow example
- [Project Documentation](project-documentation.md): alternative documentation approaches
- [Meta-Harness Notes](meta-harness.md): outer planning loop and inner execution loop
- [Quotes](quotes.md): optional conversation starters
- [Resources](resources.md): extended reading roadmap

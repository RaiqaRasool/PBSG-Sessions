# Agent Memory: Episodic Memory, Semantic Memory, and Retrieval

This document completes the Agent Memory study sequence. It explains how agents represent particular experiences, extract durable facts and knowledge, decide what to recall, and handle the common failure modes that arise when memories are incomplete, stale, conflicting, or retrieved in the wrong situation.

## 1. Two Independent Ways to Classify Memory

Memory categories become clearer when separated along two axes.

### Lifetime and scope

```text
Active context
→ one model invocation or evolving agent loop

Session memory
→ current conversation or task

Project memory
→ one repository or project

User-global memory
→ one user across projects and sessions
```

### Content type

```text
Episodic memory
→ what happened in a particular experience?

Semantic memory
→ what is known or believed to be true?

Procedural memory
→ how should a task be performed?
```

These axes are independent. A project can contain both episodic and semantic memories, and a session can contain recent episodic history, semantic conclusions, and operational task state.

## 2. Conversation Archive Versus Session Memory

A conversation archive is a chronological record:

```text
User message
Assistant response
Tool call
Tool result
Next message
...
```

It is episodic in structure because it records what happened in sequence.

Session memory is the selected working state needed to continue the current task:

```json
{
  "goal": "Study agent memory",
  "completed": [
    "short-term memory",
    "long-term memory"
  ],
  "current_topic": "episodic and semantic memory",
  "next_topic": "memory retrieval"
}
```

The archive and session memory are related but not identical:

```text
Conversation archive
Complete chronological record
            ↓ extraction and summarization
Session memory
Selected working state
```

Session memory may include:

- recent events;
- semantic conclusions;
- current goals;
- constraints;
- plans;
- decisions; and
- operational progress.

## 3. Episodic Memory

Episodic memory preserves a particular interaction, task, incident, or experience.

It answers:

- What happened?
- When and where did it happen?
- What was the goal?
- What did the agent try?
- What evidence appeared?
- What worked or failed?
- What was the outcome?
- What lesson was learned?

Example:

```json
{
  "type": "episode",
  "project": "Project Phoenix",
  "time": "2026-08-27",
  "goal": "Diagnose intermittent OAuth callback failure",
  "observations": [
    "The same callback URL was invoked twice",
    "The first request exchanged the authorization code",
    "The second exchange failed"
  ],
  "rejected_hypotheses": [
    "Expired Flask session",
    "Server clock skew"
  ],
  "action": "Added duplicate-callback handling",
  "outcome": "Authentication tests passed",
  "lesson": "Check callback replay when one-time code exchange fails"
}
```

## 4. Episode Versus Transcript

A transcript records almost everything said or returned. An episodic memory preserves the meaningful structure of what happened.

```text
Raw transcript
├── greetings
├── repeated questions
├── full tool outputs
├── temporary hypotheses
└── final result
          ↓ episode extraction
Structured experience
├── situation
├── actions
├── evidence
├── decisions
├── outcome
└── lesson
```

The original transcript may remain archived as supporting evidence, while the compact episode is indexed for retrieval.

## 5. Useful Episode Fields

| Field | Purpose |
| --- | --- |
| Identity | Distinguishes the episode |
| Time | Records when it occurred |
| Scope | Identifies user, project, or environment |
| Situation | Describes the starting conditions |
| Goal | Records what the agent attempted |
| Actions | Preserves meaningful steps |
| Observations | Records relevant evidence |
| Decisions | Captures choices and reasoning |
| Outcome | States what happened |
| Evaluation | Indicates success, failure, or uncertainty |
| Lesson | Extracts reusable meaning |
| Sources | Points to chats, logs, files, tests, or commits |

Not every episode needs every field.

## 6. Why Retrieve an Episode?

An episode can provide precedent for a current situation.

```text
Current OAuth symptom
        ↓ similarity search
Past OAuth incident
        ↓
Prior evidence, rejected hypotheses, and successful action
```

The correct interpretation is:

> A similar symptom previously had this cause, so it is worth checking again.

It is not:

> The current problem must have the same cause.

Episodic memory supports analogy, not certainty.

## 7. Semantic Memory

Semantic memory stores facts, concepts, preferences, relationships, conventions, and generalized knowledge without requiring the complete event in which they were learned.

Examples:

```text
Raiqa prefers first-principles explanations.

Project Phoenix uses uv for dependency management.

OAuth authorization codes are intended for one-time exchange.

Authentication state is separate from Globus transfer state.
```

Semantic memory answers:

- What is known?
- What is believed to be true?
- What relationships exist?
- What convention applies?
- What preference should guide behavior?

## 8. Why User-Facing Memory Is Often Semantic

User-facing AI memory commonly appears as compact profile facts:

```text
Raiqa prefers interactive learning.
Raiqa works on Project Phoenix.
Raiqa prefers uv for Python work.
```

Semantic memories are usually smaller and easier to apply across different situations than complete past conversations.

An interaction may be episodic:

```text
During an Agent Memory study session, Raiqa repeatedly requested
causal explanations before terminology.
```

The durable extraction is semantic:

```text
Learning preference:
Raiqa prefers first-principles causal explanations.
```

## 9. Episodic Versus Semantic Memory

| Episodic memory | Semantic memory |
| --- | --- |
| Remembers a particular experience | Remembers a fact or generalized belief |
| Answers “What happened?” | Answers “What is true or believed?” |
| Usually tied to time and situation | Usually abstracted from one event |
| Contains actions and outcomes | Contains concepts, facts, and relationships |
| Supports analogy and precedent | Supports factual and conceptual reasoning |

Example:

```text
Episodic:
On August 27, duplicate callback processing in Project Phoenix
caused a one-time authorization code to be exchanged twice.

Semantic:
Replaying an OAuth authorization code can cause an invalid-code error.
```

## 10. From Episode to Semantic Knowledge

Semantic memory can be derived through consolidation:

```text
One or more experiences
        ↓ identify recurring or durable meaning
Candidate semantic memory
        ↓ validate scope, evidence, and confidence
Stored fact, preference, rule, or relationship
```

A single episode should not automatically become a universal rule.

Weak generalization:

```text
One OAuth failure was caused by callback replay.
Therefore, all OAuth failures are callback replay.
```

Better memory:

```text
In Project Phoenix, callback replay previously caused an
invalid-code error. Check for this pattern when symptoms match.
```

## 11. Retaining Provenance

A compact semantic memory should preserve or reference supporting evidence.

```json
{
  "type": "semantic",
  "content": "Duplicate callback processing can replay a one-time authorization code.",
  "scope": "oauth",
  "source_episode": "incident-2026-08-27",
  "confidence": 0.95,
  "status": "active"
}
```

Provenance helps the system answer:

- Who stated this?
- Was it observed or inferred?
- In which project did it occur?
- When was it last verified?
- What evidence supports it?
- Does it apply universally or only in one environment?

## 12. Mixed Memory Records

Real records do not always fit into exactly one category.

```json
{
  "date": "2026-08-27",
  "event": "OAuth callback failure",
  "outcome": "Duplicate-callback handling resolved it",
  "lesson": "Check callback replay for one-time code failures"
}
```

The event and outcome are episodic. The lesson is semantic. A memory system may store them together or link separate records.

## 13. Procedural Memory

Procedural memory is not a required focus of this track, but students may ask about it. It answers:

> How should the agent perform a task?

Examples:

```text
Procedure for diagnosing callback replay:
1. Inspect callback timestamps.
2. Compare authorization-code values.
3. Verify whether the first exchange succeeded.
4. Test how duplicate callbacks are handled.
```

In agent systems, procedures may live in:

- skills;
- runbooks;
- `AGENTS.md`;
- scripts;
- workflow definitions;
- tool instructions; or
- retrieved procedural records.

An episode may produce both semantic and procedural knowledge:

```text
Past incident
    ├── semantic lesson: callback replay can cause this error
    └── procedural lesson: use these steps to diagnose it
```

## 14. The Memory Retrieval Problem

Once an agent stores many memories, it cannot insert all of them into every active context.

```text
100,000 stored memories
        ↓
Current question: “Why is the OAuth callback failing?”
        ↓
Retrieve only the few memories likely to help
```

Retrieval must decide:

- which scopes are permitted;
- which memories match the current task;
- which version is current;
- which source is authoritative;
- how many memories fit the token budget; and
- how the memories should be presented.

## 15. New-Session Retrieval Pipeline

A plausible pipeline is:

```text
1. Create new session state
   - session ID
   - current user
   - current project
   - first message

2. Load deterministic context
   - system instructions
   - project instructions
   - security rules
   - pinned preferences

3. Apply permissions and scope
   - accessible user memories
   - active project memories
   - organization policies

4. Retrieve additional candidates if needed
   - exact lookup
   - metadata filtering
   - lexical search
   - semantic search
   - recency and importance ranking

5. Rerank and select within the token budget

6. Insert selected memories into session state or active context

7. Make the model call

8. Let the model request more context through tools
```

An embedding search is optional. A simple request may need only deterministic context and pinned preferences.

## 16. Retrieval Is Part of Context Engineering

Memory retrieval and context engineering overlap:

```text
Long-term stores
        ↓ retrieval produces candidates
Context engineering
        ├── selects relevant candidates
        ├── resolves priority
        ├── allocates token budget
        ├── formats information
        └── constructs active context
```

Retrieved information can become:

```text
Original record
→ long-term memory

Working copy pinned for this chat
→ session memory

Selected text supplied to this invocation
→ active context
```

## 17. Query Construction

The literal user message may be enriched with known state.

```text
User message:
“Why is the callback failing?”

Retrieval query:
User: Raiqa
Project: Project Phoenix
Topic: OAuth callback
Task: debugging
Symptom: intermittent invalid authorization code
```

The query can be constructed using:

- the current message;
- session metadata;
- project identity;
- entities and keywords;
- structured task state;
- recent tool results; and
- sometimes a model-generated query rewrite.

## 18. Permissions and Scope Before Similarity

Relevance ranking should occur only after access and applicability checks.

```text
All memories
    ↓ access and privacy filtering
Memories visible to this user
    ↓ scope filtering
Memories applicable to the active project
    ↓ status filtering
Active, non-expired, non-superseded memories
    ↓ relevance ranking
Best candidates for the current task
```

This prevents retrieval of another user's memory, an unrelated project's decision, or an obsolete record.

## 19. Retrieval Techniques

### Exact key lookup

Use when the application knows the field:

```text
user preference → teaching style
project setting → package manager
```

### Metadata filtering

Filter by user, project, type, scope, date, status, and permission.

### Lexical search

Find exact terms such as `OAuth callback`, function names, error messages, or identifiers.

### Semantic search

Use embeddings to find conceptually similar memories whose wording differs from the query.

### Recency

Prefer newer memories when the subject changes over time.

### Importance

Prefer explicit instructions, critical decisions, security constraints, and verified diagnoses over casual observations.

### Authority and confidence

Prefer authoritative and well-supported memories over uncertain agent inferences.

### Graph retrieval

Follow relationships:

```text
Project Phoenix
    → authentication subsystem
    → OAuth callback
    → replay incident
```

### Hybrid retrieval

Combine multiple signals:

```text
semantic similarity
+ keyword match
+ scope match
+ recency
+ importance
+ authority
```

### Model-based reranking

Retrieve many candidates inexpensively, then use a model or specialized reranker to select the most useful few.

### Model-directed search

Expose a memory-search tool and let the agent request specific searches during its reasoning loop.

## 20. Retrieval Scoring

A conceptual relevance function might be:

\[
\text{Score}(m,q)=
w_sS(m,q)+
w_kK(m,q)+
w_rR(m)+
w_iI(m)+
w_aA(m)+
w_pP(m,q)
\]

where:

- \(S\) is semantic similarity;
- \(K\) is keyword match;
- \(R\) is recency;
- \(I\) is importance;
- \(A\) is authority or confidence; and
- \(P\) is scope or project match.

The exact formula varies. The principle is that relevance is more than embedding similarity.

## 21. Scope Precedence

A useful precedence policy is:

```text
Current explicit instruction
    overrides current session decision
    overrides project-specific memory
    overrides user-global preference
    overrides general default
```

Example:

```text
Global memory:
Raiqa prefers detailed first-principles explanations.

Current request:
Give me only a two-sentence answer this time.

Result:
Follow the current explicit request.
```

Or:

```text
Global preference:
Use uv for Python.

Project rule:
This legacy repository requires Poetry.

Result:
Use Poetry within this project.
```

## 22. Retrieval Timing

Long-term memory can be retrieved:

- at session initialization;
- when the topic changes;
- when the project changes;
- before a sensitive operation;
- after context compaction;
- when cached memory becomes stale;
- when the model requests a memory search; or
- when newly written memory affects the active task.

Stable preferences may be loaded once and pinned into session state. The system does not need to search every memory store before every model invocation.

## 23. Is Memory Retrieval RAG?

It is often RAG-like:

```text
Retrieve relevant external memory
        ↓
Augment the active context
        ↓
Generate a response
```

But memory retrieval can also use exact database fields, structured profiles, graph traversal, or deterministic configuration. It does not always require embeddings or a vector database.

## 24. Memory Tools and the Harness

Memory operations can happen in three ways.

### Automatic harness behavior

The harness loads pinned memories, appends messages, and updates session state without exposing a tool to the model.

### Application-defined tools

The model emits a structured request:

```json
{
  "name": "search_memory",
  "arguments": {
    "query": "previous OAuth callback incidents",
    "scope": "project"
  }
}
```

The harness validates and dispatches it to a function, database, service, or vector index.

### MCP-backed tools

A memory server may expose `search_memory`, `write_memory`, `update_memory`, and `delete_memory` through MCP. The host's MCP client maps model-facing tool calls to MCP discovery and `tools/call` requests.

From the model's perspective, a direct and MCP-backed tool may look almost identical. The difference lies behind the host boundary.

## 25. Retrieval Failure Modes

### Failure to recall

The right memory exists but receives a low similarity or relevance score.

### Irrelevant recall

The system retrieves semantically related information from the wrong project or situation.

### Context pollution

Too many memories are inserted, distracting the model from the current task.

### Stale memory

An old preference or decision is retrieved after it has changed.

### Conflict

Two memories disagree and the system has no precedence or temporal policy.

### Overgeneralization

One past episode is stored as a universal rule.

### Under-generalization

Useful repeated lessons remain buried in separate episodes and never become reusable semantic knowledge.

### False memory

The model stores an incorrect inference as though it were an explicit fact.

### Scope leakage

A project-specific instruction is incorrectly applied globally, or one user's memory is exposed to another user.

## 26. Updating and Conflicting Memories

A memory system should not only append facts forever. It should support:

- replacement;
- temporal versions;
- supersession;
- confidence adjustment;
- source precedence;
- merging duplicates; and
- explicit uncertainty.

Example:

```text
Old memory:
The project uses SQLite.

New authoritative configuration:
The project now uses PostgreSQL.

Correct handling:
Mark the SQLite memory as superseded and retain the change history
if historical reasoning still matters.
```

## 27. Forgetting Is a Feature

Memory systems should deliberately forget or stop retrieving information when it is:

- obsolete;
- incorrect;
- duplicated;
- low-value;
- outside its retention period;
- no longer permitted;
- explicitly deleted by the user; or
- unnecessarily sensitive.

Forgetting can mean:

```text
Delete the record
Mark it inactive
Expire it after a date
Keep it for audit but exclude it from retrieval
Replace it with a newer version
```

The ability to forget is part of reliable memory engineering, not a failure of memory.

## 28. Student Questions to Anticipate

### Is the conversation archive itself episodic memory?

It is episodic in structure, but a raw archive is not necessarily optimized operational memory. A structured episode is easier to retrieve and apply.

### Can one memory be both episodic and semantic?

Yes. A record may preserve an incident and include a generalized lesson. The categories describe aspects of its content.

### Are project and global memories always semantic?

No. They are often predominantly semantic, but projects can store incidents and users can have important past interaction episodes.

### Does every new session embed the first message and search all memories?

No. Systems may load pinned structured memories deterministically, use exact lookup, or perform semantic search only when needed.

### Does the system search long-term memory before every model call?

Not necessarily. Stable memories can be pinned into session state and refreshed only when the task, topic, or underlying memory changes.

### Why not put every stored memory into context?

Because context is bounded, retrieval costs resources, irrelevant memories distract, and outdated memories may conflict with current instructions.

### Can a retrieved episode prove the current cause?

No. It supplies precedent and a hypothesis to test.

### Who decides what gets stored?

Deterministic policy, structured events, models, and sometimes user confirmation can all participate. The harness should enforce permissions, scope, privacy, and allowed memory types.

## 29. Complete End-to-End Trace

```text
Past session
    ↓
Raw conversation and tool trace
    ↓
Episode extraction
“This incident occurred, these actions were taken, and this was the outcome.”
    ↓
Semantic consolidation
“This durable fact or lesson can be reused.”
    ↓
Scoped storage
User, project, domain, or organization memory
    ↓
New user request
    ↓
Scope and permission filtering
    ↓
Exact, lexical, semantic, graph, or hybrid retrieval
    ↓
Reranking, conflict resolution, and token budgeting
    ↓
Selected memories enter session state and active context
    ↓
Model reasons and uses tools
    ↓
New evidence updates session state
    ↓
Memory is confirmed, superseded, or newly consolidated
```

## 30. Final Teach-Back

An episodic memory records what happened in a particular interaction or experience, including its situation, actions, evidence, and outcome. Semantic memory stores facts, preferences, conventions, and generalized knowledge abstracted from particular events. These content types are independent of memory scope: session, project, and global stores can each contain episodic and semantic information. Retrieval begins with access and scope filtering, then uses structured lookup, lexical search, embeddings, recency, importance, authority, graphs, and model-based reranking to select a small set of relevant memories. Retrieved memories become working session state or active context. Reliable systems also preserve provenance, resolve conflicts, avoid overgeneralization, and deliberately forget obsolete or inappropriate information.

## 31. Track Completion Checklist

The learner should now be able to explain:

1. why a context window alone is insufficient;
2. how active context differs from session state;
3. why session management is short-term memory engineering;
4. what deserves long-term preservation;
5. how memory scope differs from memory content type;
6. how episodic and semantic memories differ;
7. how experiences become generalized knowledge;
8. how retrieval selects relevant memories;
9. why retrieval is more than vector similarity;
10. how memory enters active context;
11. how direct and MCP-backed memory tools differ; and
12. how updating, conflict resolution, provenance, and forgetting keep memory reliable.

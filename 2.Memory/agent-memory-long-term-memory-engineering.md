# Agent Memory: Long-Term Memory and Memory Engineering

This document is the companion to **Agent Memory: Short-Term Memory and Context Engineering**. It explains what long-term memory is, how it differs from session memory, when memories are formed and updated, how scope and storage work, how memories are retrieved, and how memory operations fit into an agent harness.

## 1. Memory Engineering as the Umbrella

Memory engineering is the design of how an agent retains, represents, scopes, retrieves, updates, consolidates, and forgets information.

It can include both short-term and long-term memory:

| Area | Primary question |
| --- | --- |
| Session-state management | What must be maintained for the current conversation or task? |
| Context engineering | What must be directly available to this model invocation? |
| Long-term memory engineering | What deserves to survive into future sessions or tasks? |

Changing session state is therefore memory engineering in the broad sense. More precisely, it is called **session-state management** or **short-term memory management**.

The two forms use many of the same mechanisms:

- deterministic rules;
- structured schemas;
- extraction;
- summarization;
- model judgment;
- retrieval;
- conflict resolution; and
- deletion or expiration.

Their retention criteria differ:

```text
Session memory:
Is this useful for completing the current task?

Long-term memory:
Is this likely to remain useful in future sessions or tasks?
```

## 2. Why Long-Term Memory Is Needed

When a session ends, the model's active context and temporary inference state do not automatically remain available to a future session. Without long-term memory, a later agent may repeat investigations, reconsider rejected explanations, or fail to apply durable user and project knowledge.

Long-term memory exists because some information learned in one session remains valuable afterward.

Examples include:

- stable user preferences;
- project conventions;
- architectural decisions and their reasons;
- important past outcomes;
- unresolved commitments;
- reusable procedures; and
- lessons from previous experiences.

## 3. Persistence Is Not Sufficient

Storing a complete transcript does not automatically create effective memory. Information becomes operational memory only if the system can:

1. capture what matters;
2. represent it usefully;
3. assign the correct scope;
4. retain provenance and time information;
5. retrieve it when relevant;
6. integrate it into active context;
7. update or supersede it; and
8. expire or delete it when appropriate.

```text
Persistence alone ≠ effective memory
```

A database containing every past conversation is an archive. It becomes useful agent memory only when the harness can select and apply the right part.

## 4. What Deserves Long-Term Storage?

A useful principle is:

> Preserve information when its expected future value exceeds the cost and risk of storing and retrieving it.

Candidate memories should be evaluated using several questions.

### Future usefulness

```text
Likely durable:
This project uses uv rather than pip.

Likely temporary:
One test is still running.
```

### Stability

```text
More stable:
Raiqa prefers first-principles explanations.

More volatile:
The deployment is currently in progress.
```

Volatile information may require timestamps, expiration, or authoritative refresh.

### Cost of rediscovery

A difficult debugging conclusion may be worth retaining. Current source-code contents may be easier and safer to reread from the repository.

### Authority and provenance

An explicit user instruction should not be treated like an uncertain agent inference.

```json
{
  "content": "Do not modify the production database.",
  "source": "explicit_user_instruction",
  "confidence": 1.0
}
```

### Scope

The instruction “use uv” might apply to one command, one project, all Python projects for one user, or an organization. A memory without scope may be incorrectly applied elsewhere.

### Privacy and safety

Potentially sensitive information may require consent, restricted access, encryption, redaction, expiration, or no storage.

The best system is not the one that remembers the most. It remembers appropriately.

## 5. Session Memory Versus Long-Term Memory

| Session memory | Long-term memory |
| --- | --- |
| Supports the current conversation or task | Supports future sessions or tasks |
| Stores current goals, progress, observations, and temporary decisions | Stores durable preferences, decisions, experiences, facts, and procedures |
| Often discarded or compressed when the task ends | Intentionally persists beyond the task |
| Criterion: immediate task relevance | Criterion: durable future value |

The same information can move through both layers:

```text
User says: “For this project, always use uv.”
                    ↓
Active context in the current model call
                    ↓
Session constraint during the current task
                    ↓
Project-scoped long-term memory
                    ↓
Retrieved into a future session
```

## 6. When Memory Engineering Happens

There is no universal rule such as waiting 24 hours. Memory processing can occur at several lifecycle points.

### During every turn

The harness may update deterministic session state:

- append messages;
- record tool calls;
- track modified files;
- update test status;
- update plans and task progress.

### When durable information appears

An explicit stable preference may be written immediately or marked as a candidate memory.

### At task or session boundaries

The system may wait until the outcome is known before saving the final conclusion. This avoids preserving every temporary hypothesis as truth.

### After inactivity or on a schedule

A background process may consolidate recent sessions, merge duplicates, resolve contradictions, or expire old memories. The delay could be minutes, hours, or days, but timing is an implementation policy rather than a definition of long-term memory.

### During later corrections

New information may replace, supersede, or qualify an earlier memory.

## 7. Compaction Versus Long-Term Consolidation

These operations can both summarize information, but their objectives differ.

| Context/session compaction | Long-term consolidation |
| --- | --- |
| Helps the current session continue | Helps future sessions benefit |
| Triggered by context pressure or task complexity | Triggered by durable future value |
| Preserves current objective, progress, and unresolved work | Preserves reusable knowledge or experience |
| May retain temporary details | Should exclude temporary noise |

Example compacted session state:

```text
Currently studying agent memory.
Completed short-term and long-term foundations.
Next topic: episodic versus semantic memory.
```

Example long-term memory:

```text
Learning preference:
Raiqa prefers interactive, first-principles explanations.
```

A long session may trigger compaction without producing any long-term memory. Long-term memory is created because information has future value, not because the session became large.

## 8. Deterministic and Model-Assisted Memory Management

Session and long-term memory usually use a hybrid approach.

### Deterministic operations

```text
New message received → append to history
Tool changed auth.py → add auth.py to modified files
Tests passed → update test status
Explicit setting selected → write structured preference
```

### Model-assisted operations

A model may help determine:

- the user's underlying goal;
- whether a statement is durable or temporary;
- the final conclusion from a long interaction;
- which new fact supersedes an earlier belief;
- an appropriate summary;
- a proposed memory type and scope; or
- which memory candidates deserve retrieval.

The model should not have unrestricted authority to store arbitrary information. The harness should enforce allowed types, scopes, permissions, privacy rules, retention limits, and conflict policies.

## 9. Memory Scope

Long-term does not mean global. Common scopes include:

```text
User-global memory
└── Raiqa prefers first-principles explanations.

Project memory
└── Project Phoenix uses uv and Python 3.12.

User-project memory
└── A user's permissions or preferences within one project.

Domain memory
└── Knowledge related to OAuth authentication.

Organization memory
└── Production changes require approval.

Agent experience
└── A diagnostic procedure succeeded previously.
```

Scope can be determined through:

- explicit phrases such as “for this session” or “for this project”;
- known application boundaries;
- user, project, and organization identifiers;
- configuration and repository metadata;
- model inference; and
- user confirmation when ambiguous or sensitive.

A useful precedence policy is:

```text
Current explicit instruction
    overrides session decision
    overrides project memory
    overrides user-global preference
    overrides general default
```

More specific and more recent authoritative information normally wins.

## 10. What Should Remain in Authoritative Sources?

Some information is better retrieved from its source instead of copied into memory.

| Information | Preferred authoritative source |
| --- | --- |
| Current source code | Repository |
| Deployment configuration | Configuration files |
| Current calendar availability | Calendar service |
| Current account balance | Financial system |
| Complete application logs | Logging system |
| Official requirements | Requirements document |

A memory may store durable meaning or a pointer:

```text
Deployment configuration is defined in docker-compose.production.yml.
```

The principle is:

> Remember durable meaning and useful pointers; retrieve volatile details from their authoritative sources.

## 11. Physical Storage Formats

Memory does not have to be stored as Markdown. Storage format and active-context representation are separate.

| Storage | Typical use |
| --- | --- |
| RAM or Redis | Current session state and caches |
| JSON | Structured local state and prototypes |
| Markdown | Human-readable project knowledge and instructions |
| Relational database | Structured facts, scope, provenance, timestamps, permissions, and updates |
| Document database | Flexible memory objects and conversation records |
| Vector index | Semantic retrieval over memory content |
| Graph database | Entities and relationships |
| Object/file storage | Large transcripts, documents, logs, and artifacts |

A project may store conventions in `AGENTS.md` or other documentation because those files are readable, editable, version-controlled, and naturally scoped to the repository.

A user-global preference may be better stored as a structured database record:

```json
{
  "memory_id": "mem-8472",
  "user_id": "raiqa",
  "type": "learning_preference",
  "content": "Prefers interactive, first-principles explanations.",
  "scope": "user",
  "source": "explicit_user_statement",
  "status": "active"
}
```

## 12. Storage Representation Versus Model Context

The model eventually receives selected memory as tokens, but the durable source can use any representation.

```text
Database, Markdown, JSON, graph, or document
                    ↓
Retrieval
                    ↓
Application-level memory object
                    ↓
Context formatting
                    ↓
Text or structured API message
                    ↓
Tokens in active context
```

For example, a database row may be rendered as:

```text
[PROJECT CONVENTIONS]
- Use uv rather than pip.
- Target Python 3.12.
```

Markdown is therefore a useful human-facing format, not a universal memory-storage requirement.

## 13. Vector Memory

A semantic memory system may retain both original content and an embedding:

```json
{
  "id": "mem-oauth-17",
  "text": "Duplicate OAuth callback processing caused reuse of a one-time authorization code.",
  "embedding": [0.12, -0.37, 0.84],
  "metadata": {
    "project": "phoenix",
    "type": "past_incident",
    "status": "active"
  }
}
```

The vector helps find semantically related memories. The original text or source record is normally what is inserted into context.

One memory may have several representations:

```text
Canonical source: repository document or database record
Structured index: type, scope, date, status, authority
Semantic index: embedding for similarity search
Active representation: formatted text supplied to the model
```

Ideally, one representation is authoritative and the others are indexes, summaries, or working copies.

## 14. Long-Term Memory Retrieval

Long-term memory can be retrieved:

- at session initialization;
- when the topic or project changes;
- before a sensitive operation;
- when the model requests a search;
- after session compaction;
- when cached memory becomes stale; or
- when newly written memory changes the current task.

Stable user and project memories may be loaded once and pinned into session state. Additional memories can be retrieved later when the task requires them. The system does not need to search all long-term memory before every model invocation.

Once retrieved, a memory can occupy three roles:

```text
Durable source
    = long-term memory

Working copy for this conversation
    = session memory

Selected rendering for this invocation
    = active context
```

## 15. Retrieval Techniques

### Exact or structured lookup

Useful when the application knows the field:

```text
user preference → teaching style
project setting → package manager
```

### Metadata filtering

Filter by user, project, memory type, scope, status, time, and permissions.

### Lexical search

Find exact words and phrases.

### Semantic/vector search

Find conceptually related memories even when their wording differs.

### Recency and importance scoring

Prefer newer or explicitly important memories when appropriate.

### Graph retrieval

Follow relationships among users, projects, systems, incidents, and decisions.

### Hybrid retrieval

Combine several signals:

```text
semantic similarity
+ keyword match
+ recency
+ importance
+ scope match
+ authority
```

### Model-based reranking

Retrieve many candidates inexpensively, then use a model or specialized reranker to select the most relevant few.

### Model-directed search

Allow the model to request memory searches during its agent loop.

Memory retrieval is often RAG-like: retrieve external information, augment the active context, and generate using it. Structured memory lookup does not necessarily require vector-based RAG.

## 16. Scope-Aware Retrieval and Precedence

A memory system may search candidate pools such as:

```text
Current session
Project memories
User-global memories
Organization policies
General agent experience
```

It should first enforce access and scope restrictions, then rank permitted candidates. It does not need to perform a literal sequential scan of every record.

Specific context should override broad defaults:

```text
Global preference:
Use uv for Python.

Project memory:
This legacy repository requires Poetry.

Result:
Use Poetry in this repository.
```

## 17. Memory Operations and Agent Tools

Memory operations can be implemented in three ways.

### Invisible harness logic

The harness automatically loads session state, retrieves pinned memories, appends messages, and records tool results. The model issues no memory tool call.

### Application-defined function tools

The model can request a structured operation:

```json
{
  "name": "search_memory",
  "arguments": {
    "query": "previous OAuth callback incidents",
    "scope": "project"
  }
}
```

The harness validates the request, invokes a function or service, and returns the result.

The implementation could be a Python function, JavaScript function, database query, HTTP API, vector search, filesystem operation, or another agent.

### MCP-backed memory tools

A memory service may expose tools such as:

```text
search_memory
write_memory
update_memory
delete_memory
```

through an MCP server. The host's MCP client then translates between the model-facing tool representation and MCP discovery or `tools/call` messages.

From the model's perspective, a direct function tool and an MCP-backed tool may look similar. The difference is how the host dispatches the operation.

## 18. Model, Harness, and Tool Responsibilities

```text
Model
├── identifies missing information
├── proposes searches or memory candidates
└── emits structured tool requests

Harness
├── maintains session state
├── validates tool arguments
├── enforces scope, privacy, and permissions
├── dispatches implementations
├── constructs active context
└── decides when to compact or refresh

Memory implementation
├── stores records
├── indexes content
├── performs retrieval
├── updates and supersedes records
└── handles deletion and expiration
```

The model may assist with judgment, but the harness owns enforcement and execution.

## 19. End-to-End Example

The user starts a new session:

```text
Investigate the OAuth callback error in Project Phoenix.
```

The system:

1. identifies the user, project, and topic;
2. loads pinned user and project memories;
3. searches for relevant past incidents;
4. builds session state;
5. formats selected information into active context;
6. allows the model to inspect files and logs;
7. continuously updates session state;
8. completes and verifies the task; and
9. determines whether the outcome confirms, updates, contradicts, or creates long-term memory.

Example session state:

```json
{
  "goal": "Investigate OAuth callback error",
  "project": "Phoenix",
  "constraints": ["Use uv"],
  "relevant_prior_experience": [
    "Check for duplicate callback processing."
  ]
}
```

## 20. Consolidated Mental Model

```text
Current interaction
        ↓
Session-state management
Retain what the current task needs
        ↓
Context engineering
Select what this model call needs
        ↓
Model and tool loop
        ↓
Memory extraction/consolidation
Select what future work may need
        ↓
Scoped long-term storage
User, project, domain, organization, or agent
        ↓
Future retrieval
        ↓
New session state and active context
```

## 21. Short Teach-Back

Session-state management is short-term memory engineering: it retains and updates information according to usefulness for the current task. Long-term memory engineering uses many of the same deterministic, retrieval, summarization, and model-assisted techniques, but applies a different criterion—durable value for future sessions. Long-term memories are scoped, stored in suitable formats, retrieved when relevant, copied into session working state, and selectively formatted into active context. Models may help propose and interpret memories, while the harness enforces storage policies, scope, privacy, permissions, and execution.

## 22. Transition to Episodic and Semantic Memory

Long-term memory can preserve different kinds of content:

```text
Episodic memory
→ What happened in a particular interaction or experience?

Semantic memory
→ What facts, concepts, and relationships are considered true?

Memory retrieval
→ Which stored memories should be recalled for the current situation?
```

These distinctions determine how memories should be represented, generalized, searched, trusted, and applied.

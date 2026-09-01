# Agent Memory: Short-Term Memory and Context Engineering

This document is a checkpoint for the completed first part of the Agent Memory study track. It explains why agents need memory, how active context differs from session state, what short-term memory contains, and how context engineering constructs the information supplied to each model invocation.

## 1. Why the Context Window Alone Is Not Enough

A language model can directly use only the information available in its current context window. The model does not automatically retain a private record of earlier API calls. Without an agent harness, the user or application would have to preserve previous messages, concatenate relevant material, and send it again.

A request might contain:

```text
system instructions
+ previous messages
+ relevant documents
+ tool results
+ current user request
```

Modern models can support hundreds of thousands or roughly one million tokens, but context remains bounded. A continuing agent can eventually accumulate more information than any fixed context window can contain. Sending everything repeatedly also increases cost and latency, introduces irrelevant material, and may place outdated and current facts next to each other.

The real problem is therefore not merely how to fit everything. It is how to provide the smallest sufficient collection of accurate, relevant information for the current task.

## 2. Model Context, KV Cache, and External Memory

These mechanisms occupy different layers:

| Mechanism | Purpose | Typical lifetime |
| --- | --- | --- |
| Active context | Contains the tokens the model can currently use | One model invocation or evolving agent loop |
| KV cache | Reuses temporary internal representations of existing tokens during generation | Usually one continuous inference process |
| Session memory/state | Maintains continuity across the current chat or task | Current session or task |
| Long-term memory | Preserves useful information for future sessions or tasks | Days, months, or indefinitely |

The KV cache is an inference optimization, not agent memory. It avoids recalculating certain internal representations of earlier token positions as new tokens are generated. It normally should not be stored as external memory.

## 3. Active Context

Active context is the exact information available to a particular model invocation. It may include:

- governing instructions;
- the current user request;
- selected conversation history;
- the current objective and constraints;
- relevant source-code excerpts;
- recent tool results;
- a task plan or progress summary; and
- memories retrieved from external storage.

The context changes as an agent works:

```text
Call 1: goal + repository structure
Call 2: goal + relevant source files
Call 3: goal + proposed patch + test failure
Call 4: goal + corrected patch + successful test results
```

Only information included in a call is directly available to the model during that call.

## 4. Session Memory and Session State

Session state is the broader record maintained by the application or agent harness for the current interaction. It may contain:

```text
Session state
├── conversation history
├── current goal and constraints
├── tool-call history
├── files examined or modified
├── decisions and rejected hypotheses
├── test results
├── task summary
└── current progress
```

Session state is not necessarily sent to the model in full. The harness selects or summarizes parts of it when constructing active context.

Although session state may be physically stored outside the model, it is normally classified functionally as short-term memory because it primarily supports the current conversation or task. It lasts longer than a single model invocation but is not necessarily intended to survive into unrelated future sessions.

## 5. Short-Term Memory

Short-term memory is the task-relevant information an agent maintains to complete the current conversation or task. It includes both:

1. information directly present in active context; and
2. session state that can be reintroduced into later calls during the same task.

Useful short-term information commonly includes:

- the current objective;
- scope and constraints;
- recent conversational dependencies;
- current observations and evidence;
- active plans and progress;
- decisions already made;
- rejected approaches and why they were rejected;
- relevant tool results; and
- long-term memories retrieved for current use.

Short-term memory is not simply the most recent information. An old constraint can remain essential, while a recent conversational branch may already be irrelevant. Task dependency and relevance matter more than recency alone.

## 6. Raw History Versus Useful Working State

Preserving every event is different from preserving its useful meaning. A large sequence of tool calls can often be represented as a compact state:

```text
Goal:
Fix duplicate OAuth callback processing.

Rejected explanation:
Flask is not reusing an authorization code from the session.

Finding:
The callback is being invoked twice.

Current status:
The fix is implemented and authentication tests pass.
```

This produces three useful levels:

```text
Raw session record
        ↓
Compact session/task state
        ↓
Active context for this model call
```

## 7. How a Coding Agent Evolves Context

One user message can cause several model invocations:

```text
User request
    ↓
Model decides which files to inspect
    ↓
Filesystem or search tool returns results
    ↓
Model examines results and requests another action
    ↓
Patch is applied
    ↓
Tests run and return output
    ↓
Model interprets the result and responds
```

Relevant file contents may be included while implementation is active. Once the task finishes, the model's temporary inference state can disappear. The files remain in the repository, and the harness may preserve a summary of the work. A future request can cause the agent to search or reread the authoritative files instead of retaining every file permanently in active context.

Filesystem access may be provided through MCP, built-in file tools, shell commands, repository indexes, language servers, or other mechanisms. MCP is one possible interface, not a requirement of context management.

## 8. When Context Is Constructed

When the user sends a new message, a typical harness:

1. adds the message to session state;
2. interprets the new objective relative to the existing session;
3. constructs an initial active context;
4. tokenizes it and checks the token budget;
5. calls the model;
6. executes requested tools;
7. adds selected tool results to subsequent model calls; and
8. summarizes, compacts, retrieves, or removes information as the loop continues.

Some preparation can happen before the next user message arrives. The system may already maintain instructions, a conversation summary, repository metadata, indexes, task state, or cached stable prefixes. The latest request is still normally needed to determine which of those sources are relevant now.

An instruction such as “ignore everything before this message” can change context selection, but ignoring information is not the same as deleting stored chat history or external records.

## 9. Context Engineering

Context engineering is the design and operation of the process that assembles, organizes, updates, and presents the right information in active context at the right time.

It is broader than writing a prompt. It can involve:

- system and developer instructions;
- recent conversation selection;
- structured session state;
- source-code and document retrieval;
- tool selection and tool results;
- long-term memory retrieval;
- summarization and compaction;
- ordering and labeling information;
- resolving authority and freshness;
- allocating the token budget; and
- removing irrelevant, duplicated, or obsolete material.

Context engineering focuses on the information supplied to the current model call, but it depends on sources maintained by the surrounding system.

```text
Session state ───────┐
Long-term memory ────┤
Files and databases ─┤
Tool results ────────┼──→ context engineering ──→ active context
Current request ─────┤
Instructions ────────┘
```

## 10. Common Context-Engineering Techniques

Most systems combine several techniques rather than relying on one model decision.

### Fixed inclusion rules

Always include information such as system instructions, security constraints, the current request, project instructions, and essential tool definitions.

### Recency windows

Retain the last several messages, tool calls, or accessed files. This is inexpensive but may lose old constraints and retain recent noise.

### Structured or pinned state

Maintain explicit fields for the goal, constraints, current plan, modified files, unresolved questions, and task status. These fields can be included because of their roles rather than rediscovered from raw history.

### Lexical and structural search

Use exact-text, filename, symbol, reference, import, caller, dependency, or test search. For code, structural relationships may be more reliable than textual similarity.

### Semantic retrieval

Use embeddings to find passages conceptually similar to the current request. Semantic similarity provides candidates but does not guarantee correctness, authority, freshness, or completeness.

### Metadata filtering

Narrow candidates by project, branch, document type, date, authority, user, or scope before performing lexical or semantic retrieval.

### Model-based routing

Use a model to classify the request, select likely data sources, or choose tools. A cheaper router model may operate before the main reasoning model, although this adds latency, cost, and another possible failure point.

### Reranking

Retrieve many candidates quickly, then use a reranker or model to select the few most relevant items.

### Summarization and compaction

Compress large histories while retaining goals, constraints, decisions, unresolved problems, implementation state, and important evidence. Compaction is lossy, so an inaccurate summary can distort later reasoning.

### Iterative, model-directed gathering

Start the model with a small bootstrap context. Let it identify missing information, call search or file tools, inspect results, and repeat. This avoids requiring the harness to predict the complete context before the first reasoning step.

## 11. How Formatting Is Determined

The harness usually controls the main context structure using predictable templates:

```text
[INSTRUCTIONS]
...

[CURRENT OBJECTIVE]
...

[CONSTRAINTS]
...

[SESSION SUMMARY]
...

[RELEVANT SOURCES]
...

[RECENT TOOL RESULTS]
...

[CURRENT USER REQUEST]
...
```

The system designer can control ordering, labels, source attribution, timestamps, authority, maximum tokens per section, and whether information is quoted or summarized. Models may help summarize or transform content, but stable formatting policies are normally controlled by the harness.

## 12. Context Engineering Versus Memory Engineering

The fields overlap, but their primary concerns differ:

| Memory engineering | Context engineering |
| --- | --- |
| Determines what should persist | Determines what is needed now |
| Stores, indexes, updates, merges, or forgets information | Selects, orders, formats, and budgets information |
| Makes information available for possible future use | Makes selected information directly usable by the current model call |
| Focuses on persistence and lifecycle | Focuses on present reasoning conditions |

Retrieval connects them:

```text
Stored memory
    ↓ candidate retrieval
Relevant information
    ↓ context selection and formatting
Active model context
```

## 13. Consolidated Mental Model

```text
External environment
Files, databases, APIs, long-term memories
                   ↓
Session state
Goal, history, progress, decisions, summaries
                   ↓
Context engineering
Select, retrieve, compress, order, and format
                   ↓
Active context
Information available to this model invocation
                   ↓
Model reasoning and tool decisions
                   ↓
Updated session and external state
```

## 14. Short Teach-Back

Short-term memory is the information an agent maintains to complete its current conversation or task. Active context is the portion directly supplied to a particular model invocation. Session memory lasts across calls within the current interaction and can be stored outside the model, but it remains short-term in purpose. Context engineering constructs active context from instructions, the current request, session state, retrieved sources, tools, and memories using a combination of deterministic rules, search, retrieval, model judgment, formatting, and compaction.

## 15. Boundary Before Long-Term Memory

The next question is not merely how an agent keeps information during the current task. It is:

> Which information deserves to survive after the task or session ends, in what representation and scope should it be stored, and how should a future agent retrieve and update it?

That is the transition from short-term memory and context engineering into long-term memory engineering.

# Chapter 10: The Complete Lifecycle

## Opening Story: “Find the Failure and Propose a Fix”

A developer asks a coding Host:

> Find the issue describing our login failure, inspect the relevant code, and propose a fix.

The Host connects to an issue Server and a filesystem Server. Neither Server knows the complete task. Neither communicates with the other. The Host and model create the unity.

```text
User
  ↓
Host ⇄ Model
 ├── Client A ⇄ Issue Server ⇄ Project API
 └── Client B ⇄ File Server  ⇄ Workspace
```

Let us follow the request without skipping layers.

## Before the User Speaks

In the published `2025-11-25` lifecycle, the Host first creates one Client per configured Server. Each Client initializes its relationship, negotiating protocol version and capabilities.

```text
Client A ── initialize ──> Issue Server
Client A <── capabilities ─ Issue Server

Client B ── initialize ──> File Server
Client B <── capabilities ─ File Server
```

The Clients then discover available primitives. The issue Server advertises `search_issues` and `get_issue`. The file Server advertises Resources for workspace files and a `search_code` Tool.

The Host builds an internal registry. It may filter the discovered capabilities before presenting a relevant subset to the model.

```text
Protocol discovery → Host registry → selected model-facing options
```

Discovery is preparation, not execution. No issue has been searched and no file has been read merely because its capability was listed.

## The First Model Turn

The Host sends the user's request to the model along with instructions and selected capability descriptions. The model reasons that it needs the issue before it can identify relevant code.

It produces a structured Tool selection:

```text
search_issues(query="login failure")
```

This is not yet an MCP message. It is the model-facing representation used inside the Host. The Host maps it to the Issue Client and applies policy.

```text
Model tool selection
        ↓
Host validates name, arguments, and permission
        ↓
Client A sends MCP tools/call
```

Client A sends a JSON-RPC request to the Issue Server. The Server translates the request into its project API, receives matching issues, and returns an MCP Tool result.

```text
Client A
  ── tools/call ──> Issue Server
                         ↓
                    Project API
                         ↓
  <── Tool result ── Issue Server
```

The Host converts that result into an observation the model can use. The result says issue `AUTH-214` reports that usernames containing uppercase letters fail after a recent normalization change.

## The Observation Changes the Plan

The model did not know `AUTH-214` before the Tool call. Its next decision must incorporate the observation.

```text
Initial reasoning
      ↓
Issue observation: uppercase normalization failure
      ↓
New reasoning: search for username normalization code
```

The model selects `search_code` with a query such as `normalize username`. The Host routes this selection to Client B, not Client A. The issue Server never receives workspace access.

Client B calls the file Server. The Server searches only within its configured scope and returns candidate file locations. The model then needs the actual content of one file.

If the file is exposed as a Resource, the Host can ask Client B to read its URI:

```text
Client B ── resources/read ──> File Server
Client B <── file content ──── File Server
```

The Host adds the selected content to the model's context. It does not automatically expose every workspace Resource.

## Reasoning Across Servers Happens in the Host

The model now has two observations:

```text
From Issue Server:
    failure occurs for uppercase usernames

From File Server:
    normalization lowercases input after the database lookup
```

The Servers did not exchange these facts. The Host selected their results and placed them into one model interaction.

```text
Issue Server ──> Client A ──┐
                            ├──> Host context ──> Model
File Server  ──> Client B ──┘
```

This preserves isolation. Each Server sees the request necessary for its role. Cross-source reasoning occurs at the layer that owns the user task.

The model proposes moving normalization before the lookup and suggests a regression test. Because the user asked to *propose* a fix, the Host need not authorize a file-writing Tool. It returns an explanation and patch suggestion rather than changing the workspace.

## What If Information Is Missing?

Suppose the issue lacks the affected identity provider. The Issue Server could use Elicitation if the Client advertised it:

```text
Issue Server ── elicitation request ──> Client A
Host displays question to user
User supplies identity provider
Issue Server <── structured answer ─── Client A
```

The Server does not open its own trusted-looking dialog. The Host owns presentation and consent.

If a Tool runs for a long time, progress notifications can report activity using a correlation token. The Host can show progress without confusing it with a final result. Timeouts and cancellation prevent an abandoned request from consuming resources indefinitely.

Errors also remain structured. A protocol error means the MCP exchange itself was invalid or failed. A Tool execution error means the requested domain operation failed. The Host should preserve the distinction so the model and user receive an honest account.

## The Complete Flow

The entire interaction can now be read as two nested loops:

```text
User
  ↓
Host ── context and capabilities ──> Model
  ↑                                  │
  │                                  │ selects action
  │                                  ↓
  │                                Host
  │                                  ↓
  │                               Client
  │                                  ↓ MCP request
  │                               Server
  │                                  ↓
  │                            External system
  │                                  ↓
  └──── observation ← Client ← Server

Repeat until the model can answer or the Host stops the process.
```

The outer loop is human–AI interaction. The inner exchange grounds one reasoning step through MCP. MCP does not dictate how the model reasons or when the Host should stop. It standardizes the capability boundary used during that reasoning.

## Common Misconceptions

### “The model sends MCP messages directly”

The model typically produces a model-facing Tool selection. The Host validates and translates it; the Client performs the MCP exchange.

### “The Server sees the whole conversation”

The Host should send only what an approved operation requires. A Server does not inherently receive all user messages or other Servers' results.

### “Discovering a Tool calls it”

Discovery retrieves descriptions. Execution requires a separate call after model selection and Host policy.

### “Servers collaborate directly”

They may in systems designed that way, but MCP's Host architecture does not require it. The Host can combine isolated results through model context.

### “Every request ends in an action”

The Host may stop with an explanation, ask the user for approval, or decline unsafe execution. In this example, proposing a fix did not authorize editing files.

## Summary: The Protocol Inside the Reasoning Loop

One user request produced several model turns and several MCP operations. Initialization and discovery prepared each relationship. The model selected a relevant capability. The Host enforced policy and routed the selection to the correct Client. The Server translated the MCP call into its underlying system and returned an observation. The Host fed that observation back to the model, which revised its plan.

```text
Reason → select → authorize → call → observe → reason
```

MCP occupies the call-and-observe boundary. The Host creates coherence across Servers while preserving their isolation.

We can now return to the beginning of the manuscript and compare the communication problems themselves.

## Transition: Different Problems, Different Abstractions

RPC made known remote procedures feel callable. HTTP gave browsers and servers a common Web conversation. REST shaped scalable interaction with networked resources. MCP gave AI Hosts a discoverable capability boundary.

The final task is not to rank them.

It is to identify the changed participant, the hidden assumption, and the layer each abstraction contributed—so that none is mistaken for a failed version of another.

## Specification Notes

The flow follows the official [`2025-11-25` lifecycle](https://modelcontextprotocol.io/specification/2025-11-25/basic/lifecycle) and the MCP [architecture overview](https://modelcontextprotocol.io/docs/learn/architecture). Revision-specific initialization may change under the pending stateless-core specification; the reasoning, routing, discovery, and Host-mediation concepts remain the focus.


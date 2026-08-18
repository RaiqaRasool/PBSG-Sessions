# Chapter 9: Advanced Client Features

## Opening Story: The Server That Needed More Than It Should Own

Suppose a local coding Server offers a Tool called `prepare_release`.

The Tool begins correctly, then encounters three needs.

It needs to know which project directories belong to the user's workspace. It needs a language model to turn raw commits into release notes. Finally, it needs the user to choose whether the release is a major, minor, or patch release.

The easiest implementation would give the Server broad filesystem access, a model-provider key, and a direct user interface.

That would also put every sensitive responsibility in the wrong place.

The Host already knows which workspace the user opened. It already manages the model relationship. It already owns the interface through which the user can review and answer questions.

```text
Server needs                         Authority belongs to

workspace boundary                  Host
language-model assistance           Host
additional user input               Host
```

MCP's advanced Client features emerged from this mismatch. A Server may need help that only the Host should provide. The protocol therefore lets the Server request that help through its Client rather than seize the underlying authority.

In the published `2025-11-25` revision, the relevant features are Roots, Sampling, and Elicitation.

## The Direction of the Request Reverses

Most interactions so far began on the Host side:

```text
Client ── list or call ──> Server
Client <── result ──────── Server
```

Advanced Client features reverse the direction:

```text
Server ── request ──> Client ──> Host-controlled service
Server <── result ─── Client <── Host decision
```

The Client remains the protocol endpoint, but the capability belongs to the Host. The Client carries the request upward, the Host applies policy or interacts with the user, and the result returns through the same isolated relationship.

This is why these features are advertised as Client capabilities. A Server cannot assume they exist. In published revisions it learns during capability negotiation whether the Client supports them and must respect the Host's decision to refuse a request.

Reverse requests do not invert control. They preserve it.

## Roots: Describe the Boundary Before Exploring It

A filesystem Server may be capable of reading paths, but which paths are relevant?

Imagine the user opened one project:

```text
/Users/Amina/projects/weather-app
```

The Server should not infer that the entire home directory is fair game. It needs a way to learn the filesystem locations the Host considers relevant to the current interaction.

Published MCP revisions call these locations **Roots**.

A Root is a URI identifying a directory or file boundary the Host exposes through the Client. The Server can request the current list:

```text
Server ── roots/list ─────────> Client
Server <── approved Root URIs ─ Client
```

The idea is not “grant access to everything under this path.” A Root communicates scope and relevance. Actual operating-system permissions and Host policy still determine what the Server can access.

```text
Root says:
    "This workspace is relevant."

Root does not automatically say:
    "Every operation beneath it is authorized."
```

Why should the Host provide Roots instead of configuring them permanently inside the Server?

Because the Host knows the active workspace. A code editor can change projects without rewriting Server configuration. Different Client relationships can expose different scopes. The Host can notify a capable Server when the Root list changes.

Roots therefore answered a clean architectural question: how can a Server learn the Host's current filesystem scope without owning the Host's workspace model?

## Sampling: Borrow Intelligence Without Owning the Model

Now the release Server has gathered commit messages and needs release notes.

It could call a model provider directly. That requires the Server author to choose providers, manage credentials, select models, handle billing, and duplicate safety policy. A local Server would gain access to a powerful credential that the Host may already manage.

The alternative is **Sampling**.

Sampling allows a Server to request a language-model generation through the Client:

```text
Server
   │ request: generate from these messages
   ▼
Client
   │ Host reviews policy and selects model
   ▼
Host's model integration
   │ generated result
   ▼
Client ──> Server
```

The term comes from language-model generation: the system samples output tokens from the model's probability distribution.

The Server can provide messages and preferences about cost, speed, or intelligence. The Host retains discretion over which model, if any, fulfills the request. It can inspect or modify the request, require user approval, limit included context, and reject the operation.

This creates model independence for the Server. The release Server asks for an intellectual service—“summarize these changes”—without embedding one vendor's SDK.

It also preserves credential isolation:

```text
Server receives generation result
Server does not need the Host's model API key
```

Sampling is not a command that forces the Host's model to run. It is a request across a trust boundary.

## Why Context Inclusion Requires Special Care

A Sampling request may become more useful if the model sees context from the Host. It also becomes more dangerous.

Suppose a Server asks for “all context” while its request contains instructions to reproduce private information. If the Host blindly complies, one Server may extract conversation content or data originating from another Server.

```text
Server A content ──┐
User conversation ─┼── Host context
Server B content ──┘
                         │
                         X must not flow automatically
                         │
                    Sampling request from Server C
```

The Host must decide what context, if any, enters the generation. The protocol can express preferences; it cannot know the user's privacy intent.

This is why Sampling belongs to the Client side. The component with the broadest view must enforce the narrowest justified disclosure.

## Elicitation: Ask the User Without Impersonating the Host

The release Tool still needs to know whether the version change is major, minor, or patch.

The Server could return an error saying “missing release type,” forcing the model or user to restart. It could guess, which is unsafe. Or it could request the missing information while the workflow is in progress.

MCP calls this **Elicitation**.

```text
Server: "I need a release type."
        ↓
Client carries structured request
        ↓
Host shows an appropriate user interface
        ↓
User accepts, declines, or cancels
        ↓
Structured result returns to Server
```

The Server describes the information it needs. The Host decides how to ask. A graphical application might show a form; a terminal Host might print a prompt; another Host may refuse the request.

This separation matters because the Server should not draw arbitrary trusted-looking interfaces or communicate with the user outside the Host's consent boundary.

Elicitation results distinguish meaningful outcomes. The user may submit information, explicitly decline, or cancel the interaction. Silence should not be mistaken for consent.

Published MCP supports structured form-style elicitation, with schemas constrained to user-manageable values, and URL-based elicitation for flows that need an external browser experience. Sensitive credentials should not be collected casually through model-visible form content. The Host must keep the user informed about where information goes.

## Elicitation Is Not a Model Question

Could the Server simply ask the model to infer the missing release type?

Only if inference is acceptable. Sometimes the missing value represents user intent, legal consent, a secret, or a business decision the model has no authority to invent.

```text
Sampling asks:
    "Can the model generate or reason about this?"

Elicitation asks:
    "Can the user provide or decide this?"
```

The distinction prevents a fluent guess from masquerading as authorization.

Similarly, Elicitation is not a Prompt. A Prompt is a user-selected template that begins or structures model interaction. Elicitation is a Server-initiated request for missing user input during an active operation.

## Three Features, One Design Principle

Roots, Sampling, and Elicitation seem unrelated until we look at authority.

```text
Roots
    Server asks what environment the Host has scoped.

Sampling
    Server asks for model assistance the Host controls.

Elicitation
    Server asks for user input through the Host's interface.
```

In every case, the Server expresses a need without taking ownership of the capability that satisfies it.

This is the deeper architectural principle:

> Move the request to the authority; do not move the authority into the requester.

The Host can apply consent, minimize disclosure, select implementations, and refuse. The Server stays focused on its domain.

## A Living Protocol: Why Roots and Sampling Are Being Deprecated

Protocol features are hypotheses about where a shared boundary creates lasting value. Operational experience can revise those hypotheses.

As of this manuscript's July 21, 2026 edition, Roots and Sampling remain part of the current published `2025-11-25` specification. However, the pending `2026-07-28` revision marks both as deprecated. Elicitation remains active, while its relationship to stateless requests is being refined.

The proposed replacements reveal the newer design preference.

Filesystem scope can be expressed through explicit Tool parameters, Resource URIs, or Server configuration rather than a special Client primitive. Model-dependent Servers can integrate directly with model-provider APIs rather than borrowing the Host's model through the core protocol.

Why retreat from the original abstractions?

Roots were narrow and filesystem-specific. Sampling coupled Servers to a Host-mediated model interaction whose policy and context behavior could be difficult to reason about. As MCP moves toward a smaller stateless core and optional extensions, maintainers are favoring explicit application data and direct dependencies over implicit Client powers.

Deprecation does not mean the original reasoning was worthless. Roots and Sampling demonstrate two enduring questions:

```text
How should environmental scope be expressed?
Who should own model access and its credentials?
```

The answers are moving. The questions remain.

This is why learning design rationale is more useful than memorizing a feature list.

## Common Misconceptions

### “Roots grant filesystem permission”

Roots describe Host-exposed scope and relevance. Operating-system permissions, Server sandboxing, and Host policy still govern actual access.

### “Sampling lets a Server control the Host's model”

Sampling is a request. The Host retains model selection, context policy, consent, and the right to refuse.

### “Sampling sends the whole conversation to the Server”

The Server supplies a generation request and receives a result. The Host decides what additional context is included; broad context sharing must not be assumed.

### “Elicitation means the Server talks directly to the user”

The Server requests input through the Client. The Host owns presentation and consent.

### “The model can infer any missing value”

Inference cannot replace user intent or authorization. Elicitation exists for information and decisions the user must provide.

### “Deprecated means immediately removed”

Deprecation signals that new designs should prefer replacements and that eventual removal is possible under the protocol's lifecycle policy. Existing implementations may continue supporting the feature during the compatibility window.

## Summary: Ask Without Taking Control

Advanced Client features addressed needs that Servers could identify but should not satisfy by seizing Host authority.

Roots let Servers request the filesystem scope relevant to the Host's workspace. Sampling let Servers request model generation without owning the Host's model credentials. Elicitation let Servers obtain missing user input through the Host's trusted interface.

All three reverse the usual request direction while preserving Host control:

```text
Server expresses need
        ↓
Client carries request
        ↓
Host applies policy and consent
        ↓
Result returns without transferring authority
```

Roots and Sampling are deprecated in the pending 2026 revision, showing that protocol boundaries evolve as operational experience accumulates. Elicitation continues because asking the user during an operation remains a clear cross-boundary need.

We now understand the participants, messages, transports, server primitives, and reverse requests separately.

The pieces must finally move together.

## Transition: One Request, End to End

A user asks an AI coding Host:

> Find the issue describing our login failure, inspect the relevant code, and propose a fix.

The Host has two Server connections. One exposes project issues. Another exposes workspace files. Tools and Resources have been discovered. Permissions have been configured.

What happens first? Which participant speaks to the model? When does an MCP Tool call begin? How does its result become a new observation? How can information from one Server influence a later call to another without the Servers communicating directly?

Individual definitions can no longer answer these questions.

We need to watch one complete interaction unfold—from the user's sentence, through model reasoning and protocol messages, into external systems, and all the way back to the final answer.

## Specification Notes

Published behavior is grounded in the `2025-11-25` specifications for [Roots](https://modelcontextprotocol.io/specification/2025-11-25/client/roots), [Sampling](https://modelcontextprotocol.io/specification/2025-11-25/client/sampling), and [Elicitation](https://modelcontextprotocol.io/specification/2025-11-25/client/elicitation). The pending deprecations follow final [SEP-2577](https://modelcontextprotocol.io/seps/2577-deprecate-roots-sampling-and-logging) and the official [`2026-07-28` release-candidate explanation](https://blog.modelcontextprotocol.io/posts/2026-07-28-release-candidate/).


# Chapter 11: RPC, REST, and MCP

## Opening Story: Four Engineers Answer Four Different Questions

Imagine placing four engineers at a whiteboard. Each is asked to solve a communication problem.

The first engineer is told:

> One application is divided across several machines. Programmers already think in procedures. Make remote work convenient to invoke.

The second is told:

> People need to retrieve interlinked information from independently operated computers around the world. Give browsers and servers a simple common conversation.

The third is told:

> The Web has become an application platform. Preserve its ability to scale and evolve as clients interact with dynamic services.

The fourth is told:

> AI applications must discover and use capabilities from many independent providers at runtime. Prevent every Host–provider pair from requiring a private integration language.

Each engineer draws a different design.

If we hide the questions and compare only the drawings, we may argue about which design is best. If we restore the questions, the argument dissolves.

RPC, HTTP, REST, and MCP were shaped by different communication problems. Their similarities come from operating in the same broad universe of independent computers. Their differences come from what each era needed participants to understand.

The final chapter is therefore not a tournament.

It is an exercise in identifying causality.

## Begin With the Problem, Not the Name

Technology names become containers. After years of use, a name accumulates implementations, marketing, conventions, and arguments. Starting with the name invites us to memorize that container.

Starting with the problem lets us reconstruct the design.

```text
Distributed work
    ↓
How can a program invoke a known operation elsewhere?
    ↓
RPC

Worldwide hypertext
    ↓
How can a browser retrieve globally identified information?
    ↓
HTTP

Dynamic network applications
    ↓
How can Web interactions retain scale and independent evolution?
    ↓
REST

Model-driven clients
    ↓
How can AI Hosts discover and use external capabilities?
    ↓
MCP
```

This is a causal map, not a claim that each technology replaced the one above it.

HTTP can carry RESTful interactions. Streamable HTTP can carry MCP messages. An MCP Server can call a REST API. That REST API's implementation may call an RPC service. Several generations can coexist in one user request because they contribute at different boundaries.

## RPC: Make Known Remote Work Feel Callable

RPC began from the programmer's most familiar abstraction: the procedure call.

If a reservation operation runs on another machine, the programmer should be able to express the intention directly:

```text
confirmation = reserve_seat(flight, passenger)
```

Stubs, marshalling, binding, request identifiers, and response handling translate that call into network communication. The abstraction moves recurring machinery away from application logic.

Its central object is an **operation**.

Its natural client is a program built by a developer against a known interface.

Its powerful bargain is advance agreement:

```text
Known procedure contract
        ↓
Generated or purpose-built client
        ↓
Convenient remote invocation
```

RPC does not need to begin every call by asking what arbitrary abilities exist. The client already knows the procedure name, arguments, and result type because a programmer arranged that knowledge before runtime.

That assumption produces clarity and strong tooling. It becomes limiting only when the participant cannot be built around a fixed interface in advance.

RPC's enduring question is:

> Which known remote operation should this program invoke?

## HTTP: Give the Web a Common Conversation

The Web faced a different environment. Publishers and readers were strangers. Information lived across independent organizations. A reader needed to follow an address from one document to another without installing a custom RPC client for every publisher.

HTTP supplied a generic request–response protocol for this distributed hypertext system.

Its central interaction combined a request intention with an identified target:

```text
Browser ── request for identified information ──> Server
Browser <── response and representation ───────── Server
```

HTTP benefited from self-descriptive messages, standard methods, status codes, metadata, and a stateless interaction model. General-purpose clients and intermediaries could understand useful parts of the conversation without knowing every publisher's internal implementation.

HTTP did not make remote procedures obsolete. It did not arise to improve the syntax of `reserve_seat()`. It served a worldwide information architecture.

HTTP's enduring question is:

> What does this Client want to do with the identified target, and what was the outcome?

## REST: Constrain the Architecture to Protect Its Properties

As the Web became dynamic, valid HTTP messages could support both well-structured and tightly coupled applications. The problem was no longer whether a request could travel. It was how application interactions should be organized.

REST described an architectural style through constraints: client–server separation, stateless requests, cacheability, a uniform interface, layered systems, and optional code-on-demand. Resource identification, representations, self-descriptive messages, and hypermedia contributed to that uniform interface.

Its central abstraction is a **resource** whose state can be represented and manipulated through general semantics.

```text
Application-specific identity
        +
Uniform interaction semantics
        +
Transferable representation
```

REST accepted restrictions to produce system properties. Uniform methods were less application-specific than an RPC procedure vocabulary, but they enabled caches, proxies, gateways, monitoring, and independently evolving clients and servers to share meaning.

Human programmers remained the adaptable bridge. They read documentation, learned domain semantics, and encoded that knowledge in clients. Even an excellent REST API did not need to explain its entire business domain to an unfamiliar intelligence at runtime.

REST's enduring question is:

> How should networked resources and representations be arranged so the system can scale and evolve?

## MCP: Introduce an AI Host to Its Current Environment

Language models changed the timing of client understanding.

A traditional client was largely designed before runtime. A model-driven client could interpret an unfamiliar user goal during the conversation and assemble a path through capabilities dynamically.

That flexibility created a new need. The environment had to describe itself while the application was running.

MCP standardized a boundary through which Hosts and capability providers could communicate. Servers could expose Tools, Resources, and Prompts. Clients could discover them and carry protocol exchanges. Hosts could translate selected capabilities into model-facing options while retaining control over context, permissions, and user consent.

Its central abstraction is a **capability made discoverable to an AI application**.

```text
Server describes available capability
        ↓
Host selects and mediates what the model may use
        ↓
Model reasons from description and observations
        ↓
Client carries approved protocol interaction
```

MCP assumes less advance coupling between a particular Host and a particular capability provider. Both implement a shared protocol instead of requiring a private adapter at their seam.

It does not assume zero prior agreement. The participants still need the MCP specification, configuration or discovery that locates the Server, compatible revisions, authentication, and shared domain meaning. Standardization moves the agreement to a reusable boundary; it does not abolish agreement.

MCP's enduring question is:

> What knowledge, actions, and guided interactions are available here, and how may this Host use them?

## The Changed Client

The cleanest comparison follows the client across the manuscript.

```text
RPC client
    Built to call a known interface.

Web browser
    Built to retrieve globally identified representations
    and follow links revealed at runtime.

REST API client
    Built by a programmer who understands resource and domain semantics.

AI Host
    Interprets user goals and capability descriptions at runtime,
    then mediates model-selected interactions.
```

The client becomes progressively less tied to one predetermined path. But greater runtime flexibility demands richer runtime grounding.

```text
More decisions made at development time
    → less runtime description required

More decisions made at runtime
    → more runtime description and policy required
```

This is the causal center of MCP.

The new protocol was not required because AI messages travel through special physics. It was required because an AI application's useful next step may not have been compiled into a fixed workflow. The model needs the current environment made legible.

## Four Forms of Prior Knowledge

Every communication system relies on prior agreement. The interesting question is what must be known and when.

```text
RPC
    Client knows the procedure contract before execution.

HTTP
    Client knows general message semantics and receives a target address.

REST
    Client knows the uniform interface plus enough domain semantics
    to interpret representations and links.

MCP
    Host knows the protocol; model-facing capability descriptions
    can arrive during runtime discovery.
```

MCP does not make domain knowledge disappear. A Tool named `approve_claim` still needs a description precise enough to distinguish insurance approval from a harmless review. A schema can state that `amount` is a number without explaining the consequences of approving it.

Runtime discovery changes how knowledge arrives. It does not guarantee adequate meaning.

That is why description quality, Host policy, Server trust, and user confirmation remain central.

## The Stack Inside One Request

Return to the coding request from Chapter 10.

The user asks the Host to inspect an issue and propose a fix. MCP lets the Host discover and call the issue Server's Tool. That Server may use a REST API to retrieve an issue Resource over HTTP. The project service may invoke an internal RPC procedure to query its search index. Network protocols beneath HTTP move bytes across machines.

```text
User intention
      ↓
AI Host and model
      ↓
MCP capability interaction
      ↓
REST-shaped project API
      ↓
HTTP request and response
      ↓
internal RPC call
      ↓
network transport
```

Calling MCP “better than REST” would be like calling the top floor of a building better than its foundation. The top floor exists for a different purpose and may depend on everything below it.

Layers are not rankings.

## Where the Comparisons Break

A compact comparison can clarify the story, but every row needs care.

```text
Technology  Primary problem          Central abstraction    Typical prior knowledge
----------  -----------------------  ----------------------  ----------------------------
RPC         distributed operations   procedure call          known interface contract
HTTP        Web communication        request and response    target plus HTTP semantics
REST        Web API architecture     resource/representation domain plus uniform interface
MCP         AI capability exchange   discoverable capability MCP plus runtime descriptions
```

This table does not claim that RPC cannot discover services, HTTP cannot invoke actions, REST cannot support AI, or MCP cannot use fixed configuration. Real systems are broader than one sentence.

The rows identify each technology's architectural center—the problem that best explains why its characteristic design choices make sense.

## Common Misconceptions

### “MCP is REST for AI”

The phrase may be suggestive, but it hides important differences. REST is an architectural style around resources and a uniform interface. MCP is a protocol for capability exchange between AI Hosts and Servers, using JSON-RPC and its own primitives.

### “MCP replaces REST”

MCP Servers commonly sit above existing APIs. REST can continue organizing those services while MCP presents their capabilities to AI Hosts.

### “RPC, REST, and MCP are three versions of remote function calling”

All can contribute to remote interaction, but their centers differ: known procedures, resource-oriented architecture, and runtime AI capability exchange.

### “Discovery removes the need for documentation”

Descriptions and schemas are documentation in machine-consumable form, and complex domains still require human-facing explanation. Discovery changes delivery, not the need for precise meaning.

### “A standard protocol guarantees interoperability”

It guarantees only the shared rules implementations correctly support. Semantic ambiguity, incompatible optional features, authentication, policy, and defects can still prevent useful cooperation.

### “The newest layer is always the best design”

Use the abstraction whose assumptions fit the problem. A tightly coupled internal service may benefit from RPC. A public Web API may benefit from REST. An AI capability boundary may benefit from MCP. Newness is not a design criterion.

## Summary: The Evolution Was in the Question

The history of communication is not a sequence of failed answers. It is a sequence of changing questions.

RPC asked how programmers could invoke known work across machines. HTTP asked how browsers and servers could exchange globally identified Web information. REST asked how dynamic network applications could preserve scale, visibility, and independent evolution. MCP asked how AI Hosts could discover and use external context and capabilities without rebuilding every pairwise integration.

Each solution carried the wisdom of its problem:

```text
RPC       hide recurring remote-call machinery
HTTP      create a general Web conversation
REST      use constraints to protect architectural properties
MCP       standardize the AI capability seam
```

The shift to MCP was driven by one altered assumption: the client was no longer only purpose-built code containing a programmer's advance understanding. A model could choose a path at runtime, so the environment needed a runtime language for describing possible paths.

That is why MCP feels inevitable after the preceding chapters. Not because every system must use it, and not because it is the final communication protocol humanity will invent. It is inevitable in the narrower, more meaningful sense that once AI clients began interpreting open-ended goals, the integration problem demanded a shared abstraction.

## Closing: The Useful Machine Is No Longer Alone

We began with one powerful computer in a small town.

It could calculate quickly but knew only the information carried to it. Connecting it to another machine moved signals but not meaning. Shared protocols turned signals into coordinated behavior. Layering let each agreement solve one portion of a growing problem.

Communication allowed an application to become larger than a machine.

RPC let a programmer call work across that larger application. The Web let strangers publish an interconnected information space. HTTP gave that space a common conversation. REST preserved the Web's architectural strengths as pages became applications and applications became APIs.

Then software gained a new kind of participant: a model able to interpret goals expressed in language.

The model could reason about a flight without seeing live inventory. It could understand an email request without possessing an email account. It could propose an action without knowing which actions existed or whether the user permitted them.

Once again, a capable machine was isolated from the information and effects that made its intelligence useful.

Once again, the first temptation was to build private bridges.

And once again, the multiplication of private bridges revealed the need for a shared agreement.

```text
Problem
    capable models are isolated from useful context and action
        ↓
Need
    independent Hosts and providers must connect without pairwise languages
        ↓
Solution
    a shared protocol for discovering and using capabilities
        ↓
MCP
```

MCP was not a random new acronym added to computing.

It was the latest expression of an old human strategy: when independent participants must cooperate, agree on the boundary, preserve freedom behind it, and let the resulting system become larger than any one participant.

The reader need not memorize MCP.

The reader has already invented the need for it.

## Source Note

This synthesis relies on the primary sources cited in earlier chapters: Birrell and Nelson's RPC paper, the HTTP specifications, Fielding's REST dissertation, foundational language-model and tool-use research, and the versioned MCP specification. Revision-sensitive MCP behavior remains explicitly dated in Chapters 7 and 9.


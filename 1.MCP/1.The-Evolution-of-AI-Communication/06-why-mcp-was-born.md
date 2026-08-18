# Chapter 6: Why MCP Was Born

## Opening Story: Ten Bridges to the Same Island

At the end of the previous chapter, developers had discovered how to let a language model move beyond language.

They could describe an operation such as `search_flights` to the model. The model could recognize when the user's request required that operation and produce structured arguments. The application could validate those arguments, call the real flight service, and return the result to the model.

One bridge now connected one AI application to one external system.

```text
AI travel assistant ─────────> flight service
```

Then another AI application needed the same flight service. Its developers built another bridge. A third application used a different model platform whose tool descriptions had a different shape, so its developers built a third.

Meanwhile, the first assistant needed access to a calendar, company policy, email, hotel inventory, maps, and expense records. Each connection required more translation code.

```text
Assistant A ── adapter ──> flights
Assistant A ── adapter ──> calendar
Assistant A ── adapter ──> policy

Assistant B ── adapter ──> flights
Assistant B ── adapter ──> calendar
Assistant B ── adapter ──> policy
```

Every bridge worked. That was the problem.

Because every team could solve its immediate integration privately, the ecosystem accumulated many successful but incompatible solutions. Capability providers had to decide which AI platforms to support. AI application developers had to decide which external systems to integrate. Moving an integration from one host to another often meant rebuilding the boundary.

The industry did not lack connections.

It lacked a common connection point.

## First, the Necessary Breakthrough: Structured Model Output

Before discussing fragmentation, we should appreciate the idea that made it possible.

An ordinary language model response is text. If an application wants to turn that text into an operation, it might search for a pattern:

```text
Model response:
"I think you should search for flights from New York to Boston tomorrow."
```

Should the application execute a search because the response contains the word “search”? Which city is the origin? Does “tomorrow” refer to the user's timezone? Is the model recommending an action or merely explaining one?

Free-form language is expressive precisely because it tolerates variation. Software execution needs a more reliable boundary.

The better idea was to let developers describe callable functions or tools to the model in a structured form. A simplified description might say:

```text
name: search_flights
purpose: Find available flights between two cities on a date
inputs:
    origin: required text
    destination: required text
    departure_date: required date
```

Given the user's request and this description, the model could return a structured proposal:

```text
tool: search_flights
arguments:
    origin: New York
    destination: Boston
    departure_date: 2026-08-12
```

The output is not the flight search itself. It is a machine-readable statement of intent. The surrounding application remains responsible for execution.

```text
User request
     ↓
Model chooses a described operation and supplies arguments
     ↓
Application validates the proposal
     ↓
Application invokes real code
     ↓
Result returns as a new observation
```

This separation was a major advance. The model handled the flexible mapping from natural language to a known operation. Traditional software handled validation, authorization, and contact with the external system.

In June 2023, OpenAI introduced function calling in its API, allowing developers to describe functions using JSON Schema and receive structured arguments selected by the model. Anthropic developed tool-use interfaces with the same broad purpose: provide names, descriptions, and input schemas; allow the model to request a tool; and return a tool result into the conversation. Frameworks such as LangChain had already been exploring agents and tool abstractions, initially through prompt conventions and later through increasingly structured tools.

These systems differed in details, but they responded to the same causal need:

```text
Natural language is flexible.
Software invocation must be precise.
Therefore the boundary needs structured intent.
```

Function calling and tool use did not fail. They became foundational building blocks.

But a building block inside a model API is not yet a standard connection between complete applications and external capability providers.

## A Tool Description Is Not a Connection

Suppose a developer includes the `search_flights` definition in a request to a model. How did that definition arrive there?

Usually, application code assembled it.

The developer wrote or installed an integration that knew how to authenticate with the airline, translate the model-facing arguments into the airline's REST API, handle errors, and convert the response into a form suitable for the model.

```text
Model-facing description
        ↓
Application-owned adapter
        ↓
Airline-specific authentication and API calls
        ↓
Airline service
```

Function calling standardized part of the relationship between an application and a particular model API. It did not, by itself, standardize how an independent capability provider announces itself to many AI applications.

This distinction is easy to miss because the same word—*tool*—may be used for several layers.

At the model boundary, a tool is a structured option included in the model's context. At the integration boundary, someone still has to obtain that option, connect it to executable software, manage its lifecycle, and carry results back.

```text
Model boundary
    "Here are the operations you may select."

Integration boundary
    "Here is how an application discovers and communicates
     with the provider of those operations."
```

The first problem had working solutions. The second was still fragmented.

## Frameworks Made the Experiment Possible

Developers rarely wanted to rebuild the entire reasoning–action loop from scratch. Frameworks emerged to organize prompts, models, tools, memory, retrieval, and multi-step agents.

A framework could give tools a common interface within its own ecosystem:

```text
Framework tool
├── name
├── description
├── input structure
└── function to execute
```

This made experimentation dramatically easier. A developer could wrap a search API, a calculator, or a database and let an agent choose among them. Frameworks absorbed changes in model APIs and provided reusable integrations.

Again, this was a successful response to a real need. Frameworks accelerated learning at a moment when model capabilities and design patterns were changing rapidly.

But each framework naturally created its own abstraction. A tool written for one framework might not run unchanged in another. A provider wishing to support several hosts could publish several packages or rely on community-maintained wrappers. Version changes in the provider, framework, or model interface could break the chain.

The architecture often looked like this:

```text
External service
       ↓
service-specific SDK or REST API
       ↓
framework-specific wrapper
       ↓
provider-specific model format
       ↓
AI application
```

Every layer served a purpose. Together, they created repeated translation.

The problem was not that developers had chosen bad abstractions. They were exploring a new design space. Competing approaches are how an ecosystem learns what must eventually become common.

## The Multiplication Problem

Let us make the integration cost visible.

Suppose there are three AI applications and four capability providers. If each application needs a custom connector to each provider, the ecosystem may require twelve integrations.

```text
                 Providers
              P1  P2  P3  P4
             ┌───┬───┬───┬───┐
Application A│ A1│ A2│ A3│ A4│
Application B│ B1│ B2│ B3│ B4│
Application C│ C1│ C2│ C3│ C4│
             └───┴───┴───┴───┘
```

With `H` hosts and `S` external systems, the potential number of pair-specific integrations grows toward:

```text
H × S
```

The formula is not a prediction that every possible pair will be built. It reveals the shape of the burden. Adding one new host creates possible work across all providers. Adding one new provider creates possible work across all hosts.

This creates consequences beyond developer inconvenience.

Small capability providers may support only the largest AI platform because maintaining many connectors is unaffordable. AI applications may offer only a narrow set of integrations. Security fixes must be repeated across wrappers. The same service may behave differently depending on who wrote the adapter. Users become locked into whichever combinations happen to exist.

The ecosystem needs to change the arithmetic.

## Put a Shared Boundary in the Middle

We encountered the same structural idea in Chapter 1. When every pair of participants invents a private language, common rules can turn many pairwise relationships into participation in one shared agreement.

Instead of asking every host to learn every provider's integration shape, define a standard boundary:

```text
AI hosts                 Shared boundary            Capability providers

Host A ──────┐                                  ┌──> Files
Host B ──────┼──── common protocol ─────────────┼──> Calendar
Host C ──────┘                                  └──> Database
```

Now each host implements the client side of the protocol. Each capability provider implements the server side. If both honor the agreement, new combinations become possible without pair-specific integration code at the protocol boundary.

The development burden moves closer to:

```text
H + S
```

Reality remains messier than the equation. Services still have unique business logic, authentication, and policy. Hosts still differ in user experience and model behavior. A shared protocol does not erase domain complexity.

It standardizes the seam.

This is the same bargain that made earlier protocols valuable: constrain how independent participants meet so each can evolve behind the boundary.

## What Must the Shared Agreement Cover?

If we were designing the agreement from first principles, what would it need?

An application must establish communication with a capability provider. The two sides may support different optional features or different protocol revisions, so they need a way to identify compatible behavior.

The application must discover what the provider currently offers. A static tool definition copied into application code recreates the old coupling. The provider should be able to describe its capabilities through the connection.

The application must invoke an offered operation or retrieve offered information and associate each result with the correct request. Long-running interactions may need progress or cancellation. Available capabilities may change while the connection exists.

The provider may sometimes need something from the application: access to user-approved context, additional user input, or model-assisted generation. These reverse requests require clear boundaries because the host controls the user relationship, model access, and local environment.

The protocol also needs to work in more than one physical arrangement. A capability provider may be a local process launched on the user's computer or a remote service reached through a network.

Our first-principles requirements now look like this:

```text
Connect
Agree on compatible features
Discover capabilities
Use capabilities
Return observations
Handle change and progress
Preserve host control
Work locally or remotely
```

Notice what we have not required. The agreement does not need to replace the provider's REST API, database, SDK, or local command. A provider can translate between the shared AI-facing boundary and whatever system already exists underneath.

```text
AI application
       ↓
shared AI-facing protocol
       ↓
provider adapter
       ↓
REST API • RPC service • database • filesystem • command
```

The new layer connects AI applications to capabilities. It does not abolish the layers below.

## Why Another Protocol Is Justified

At this point a skeptical reader should ask: why create another protocol? Could everyone simply expose REST APIs and publish documentation?

They could—and the underlying services often do.

But documentation is primarily written for a human developer who builds a client in advance. The AI application needs a runtime exchange: establish a connection, learn the capabilities available now, receive structured schemas, invoke them, obtain observations, and perhaps support communication in both directions.

An OpenAPI description can document HTTP APIs and support client generation. It is valuable at its layer. Yet the AI host still needs conventions for how providers are configured, how model-facing capabilities are selected, how results re-enter the conversation, how local processes communicate, and how host-controlled features are requested.

Could one model vendor's tool-call format become the standard? It could cover the model-facing selection step, but tying the integration boundary to one provider would make other hosts dependent on that provider's API design and release cycle. A neutral protocol should sit between AI applications and capability providers, not between one vendor's model endpoint and its callers.

Could a framework abstraction become the standard? Frameworks are software libraries with their own runtime and programming model. A protocol should allow implementations in different languages and frameworks to interoperate across a process or network boundary.

The need for a protocol comes from independent ownership:

```text
Model vendor may differ from host developer.
Host developer may differ from capability provider.
Capability provider may differ from underlying service owner.
```

When independently evolving participants must cooperate, a shared wire agreement becomes more durable than a shared library implementation.

## The Reveal: Model Context Protocol

By late 2024, the shape of the problem had become difficult to ignore. AI assistants were increasingly capable, but connecting them to useful data and software still required fragmented, custom integrations.

Anthropic introduced an open standard on November 25, 2024, intended to create a common connection between AI applications and external systems.

It was called the **Model Context Protocol**, or **MCP**.

The name deserves to be unpacked only now, after the need has appeared.

**Model** identifies the intelligence participating in the application—the component interpreting the user's request and deciding what information or action may help.

**Context** is broader than background text. It includes the information, capability descriptions, instructions, and observations that ground the model's behavior in a particular environment.

**Protocol** tells us that this is not merely a library or a collection of prompts. It is a shared agreement allowing independently built participants to communicate.

```text
Model
    reasons from what it is given

Context
    grounds that reasoning in available information and capabilities

Protocol
    standardizes how independent systems exchange that context
```

MCP was initially described as a standard for connecting AI assistants to the systems where data lives, replacing repeated custom integrations with a common protocol. Over time, the ecosystem and protocol expanded, but the original causal insight remained stable: capable models were isolated, and pairwise connectors did not scale.

MCP did not make models intelligent. It did not invent tool use. It did not replace APIs. It standardized a boundary through which AI applications could discover and interact with external capabilities.

## The USB Analogy—and Where It Stops

MCP is often compared to USB-C. The analogy is useful because a standard port changes the economics of an ecosystem.

Without a common port, every device and accessory pair may need a special cable. With a common port, device makers and accessory makers can build toward the same boundary.

```text
Before standard port             With standard port

device A ─ cable A1 ─ accessory  device A ─┐
device B ─ cable B1 ─ accessory  device B ─┼─ standard ─ accessory
device C ─ cable C1 ─ accessory  device C ─┘
```

MCP aims for the corresponding software effect between AI hosts and capability providers.

But the analogy has limits. Software capabilities are not passive electrical peripherals. Their descriptions influence a probabilistic model. They may expose private data or consequential actions. Authentication, user consent, prompt injection, and semantic ambiguity matter. Two technically compatible participants are not automatically safe to connect.

A common port creates interoperability. It does not eliminate policy.

The analogy should illuminate the integration shape, not conceal the trust problem.

## Standardize the Connection, Not the Capability

An email service and a database do not need to become alike internally. A local file search and a remote payment system should not pretend to have identical risks or business semantics.

MCP standardizes how capabilities are presented and exchanged, not what all capabilities must mean.

```text
Standardized
    connection roles
    message patterns
    discovery mechanisms
    capability schemas
    results and notifications

Still domain-specific
    what an operation actually does
    which data exists
    authentication and authorization
    business rules
    user policy
```

This is why the protocol can connect to systems built with earlier technologies. An MCP server may call a REST API, invoke an RPC service, query a database, or read a local file. Those systems continue solving their own communication problems.

MCP gives them an AI-facing boundary.

The relationship is layered, not competitive:

```text
User communicates an intention
             ↓
AI application and model reason about it
             ↓
MCP exposes suitable context and capabilities
             ↓
Existing systems perform their specialized work
```

## Open Protocol Versus Product Feature

A product feature works inside the product that implements it. A protocol becomes valuable when different products can implement the same agreement.

This distinction explains why openness matters for MCP's purpose. If only one assistant could use the protocol, capability providers would still need separate integrations for every other assistant. If only one implementation language were allowed, the boundary would inherit that ecosystem's limits.

An open specification allows different hosts, clients, servers, and software libraries to participate. Implementations can compete on usability, performance, security, and reliability while preserving interoperability at the boundary.

The history after MCP's introduction reinforced this direction. The protocol spread across multiple AI products and infrastructure providers, and in December 2025 Anthropic donated MCP to the Agentic AI Foundation, a Linux Foundation fund created with participation from several major technology organizations. Governance can evolve, and adoption claims change over time, but the architectural point is durable: a cross-ecosystem standard is stronger when no single product is its only possible home.

## What MCP Does Not Solve

A protocol is most useful when its boundary is understood clearly.

MCP does not guarantee that a tool description is truthful. It does not make an unsafe operation safe. It does not decide whether the user intended a purchase. It does not ensure that a model will select the correct capability or supply sensible arguments. It does not remove the need for authentication, authorization, validation, logging, or human approval.

It also does not guarantee semantic uniformity. Two calendar servers may describe similar operations differently. Standard message shapes make them connectable; careful descriptions and host behavior make them usable.

```text
Protocol can establish:
    "Here is a callable operation with this schema."

Protocol alone cannot establish:
    "Calling it is wise, safe, permitted, and what the user meant."
```

These are not failures of MCP. They are boundaries of the problem it addresses.

HTTP does not decide whether an online purchase is ethical. REST does not guarantee good domain modeling. RPC does not guarantee that a remote procedure is safe. A protocol provides communication structure; applications remain responsible for policy and meaning.

## Common Misconceptions

### “MCP invented tool calling”

Tool use, function calling, agent frameworks, retrieval systems, and custom integrations preceded MCP. MCP standardized a connection boundary among AI applications and capability providers.

### “Function calling and MCP are the same thing”

Function calling commonly describes the model-facing mechanism through which a model selects a structured operation. MCP describes communication between an AI application's client side and an external capability server. A host can translate MCP-discovered tools into whatever tool-call format its chosen model uses.

### “MCP replaces REST APIs”

An MCP server may wrap a REST API. REST continues to structure the underlying Web service; MCP presents an AI-oriented capability boundary above it.

### “MCP makes every tool universal”

It makes a common interaction protocol possible. Hosts still differ in supported features and policy. Servers still expose domain-specific semantics. Authentication and user authorization still matter.

### “MCP is a framework”

Frameworks provide code and programming abstractions within an application. MCP is a protocol that different frameworks and languages can implement to communicate across a boundary.

### “If an MCP server connects, it is safe”

Technical compatibility is not trust. Servers can expose sensitive data or consequential actions, and returned content may influence model behavior. Hosts must apply security policy, permissions, validation, and user control.

### “Another protocol means earlier protocols failed”

MCP solves a new layer's problem. RPC, HTTP, and REST remain useful beneath or beside it. The system evolved because the client and integration topology changed.

## Summary: The Standard Seam

Language models needed structured ways to request actions. Function calling, tool use, and agent frameworks supplied them. These were necessary successes: they converted flexible natural language into machine-readable intent and enabled reasoning to interact with the world.

But each ecosystem described tools and integrations through its own abstractions. Capability providers wrote multiple connectors. Host developers maintained multiple adapters. The number of possible pairwise integrations grew with hosts multiplied by systems.

A shared protocol could change the topology. Hosts would implement one side; capability providers would implement the other. Domain complexity would remain, but the connection seam could become common.

MCP emerged to standardize that seam. It allowed AI applications and external capability providers to establish communication, describe available features, discover capabilities, invoke them, and exchange observations through an open agreement.

It did not replace model function calling or existing APIs. It connected layers:

```text
Model chooses from model-facing options
                ↓
Host mediates the interaction
                ↓
MCP communicates with capability provider
                ↓
Provider uses existing systems to do the work
```

The need now feels inevitable. The architecture does not—yet.

## Transition: Who Owns the Connection?

We have said “AI application” and “capability provider” as though each were a single box. That simplification was useful while discovering the need for a protocol. It is insufficient for designing one.

The AI application owns the conversation with the user. It chooses the model, holds permissions, decides what context to reveal, and may connect to many capability providers at once.

Each provider has its own lifecycle. One may be a local process accessing files. Another may be a remote service connected to a company system. Their capabilities and trust boundaries differ.

If the model spoke directly to every provider, who would maintain the connection? Who would negotiate supported features? Who would translate provider capabilities into the model's format? Who would prevent one provider from seeing another provider's private context? Who would keep the user in control?

We need more than two vague boxes.

```text
User
  ↓
AI application
  ↓
?
  ⇄
capability provider
```

Something inside the application must own each protocol relationship while remaining subordinate to the application that controls the user and model experience.

The next chapter will derive the roles required to make that boundary work.

## Historical Notes

The early tool-use account draws on OpenAI's June 2023 [function-calling announcement](https://openai.com/index/function-calling-and-other-api-updates/) and LangChain's account of its early [structured tool abstraction](https://blog.langchain.com/structured-tools/). MCP was publicly introduced by Anthropic on November 25, 2024 in [“Introducing the Model Context Protocol”](https://www.anthropic.com/news/model-context-protocol). The later governance milestone is described in Anthropic's December 2025 [Agentic AI Foundation announcement](https://www.anthropic.com/news/donating-the-model-context-protocol-and-establishing-of-the-agentic-ai-foundation).


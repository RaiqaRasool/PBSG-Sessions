# Chapter 5: The Client Changes

## Opening Story: The Intern Who Can Understand the Request but Cannot Enter the Building

Imagine hiring an unusually capable intern.

On the first morning, you say:

> Find a flight that gets me to Boston before noon, make sure it follows our travel policy, and book it if the price is under $400.

The intern understands the sentence. They recognize that the task contains several parts. A flight must be found. Arrival time and price must be checked. A company policy must be consulted. If the conditions are satisfied, a reservation must be created.

Then the intern asks a series of revealing questions.

“Where do we search for flights?”

“Where is the travel policy?”

“Do I have permission to book?”

“What information does the booking system require?”

“Which actions need your confirmation?”

The intern's problem is not language. It is access to the working environment.

Understanding an intention does not automatically reveal which systems exist, how to use them, what information they contain, or what authority the user has granted.

This is the position of a language model inside an application.

For decades, the clients of RPC services and Web APIs were built by programmers. The software itself did not have to discover the world. A human developer had already chosen the service, read its documentation, encoded its schemas, arranged authentication, and decided which interface controls would trigger which operations.

Now the user is speaking to a model instead of clicking through a workflow predicted by a programmer.

The model can interpret requests that no developer wrote down in advance. That flexibility is its great power.

It is also what breaks the old assumption.

## Before the Model: Clients Were Frozen Decisions

Consider a conventional travel application.

Its screen may offer fields for origin, destination, departure date, and maximum price. The user fills them in and presses **Search**. Behind that button is code written for one precise purpose.

```text
User fills known fields
        ↓
Search button triggers known code
        ↓
Code calls a known airline API
        ↓
Response is rendered in a known layout
```

The program appears to understand the user's intention, but it does not interpret the intention in a general sense. The developers interpreted it earlier.

They decided that these four fields map to these API parameters. They determined that pressing this button performs a safe search rather than a purchase. They studied the response schema and wrote code to display particular fields. The resulting client contains those decisions in frozen form.

```text
Human reasoning during development
              ↓
        client program
              ↓
predictable behavior during use
```

This model works extremely well when the possible interactions can be anticipated. It gives designers tight control over behavior. It lets programmers validate inputs, test known paths, and construct a clear user interface.

But the client can do only what its authors prepared it to do. Ask a flight-search form to compare the itinerary with a policy document, and the form has no general way to reinterpret the request. A developer must add that workflow.

The traditional client is flexible at development time and fixed at runtime.

A language model reverses part of that relationship.

## A Machine That Works Through Language

Human language is wonderfully inconvenient for software.

The same intention can be expressed many ways:

```text
"Get me to Boston before lunch."
"Find a morning flight to Boston."
"I need to arrive in Boston by 12 p.m."
"What can land at BOS before noon?"
```

A traditional program handles this by forcing users into predefined controls or by building specialized language-processing rules. The form turns ambiguity into fields. The programmer decides in advance what each field means.

Language models offer a different possibility. Instead of requiring every request to match a rigid command grammar, train a system on patterns in enormous collections of language so it can continue, transform, classify, and respond to text in context.

At the surface, a generative language model performs a simple repeated operation: given the text so far, estimate what piece of text is likely to come next.

Those pieces are called **tokens**. A token may be a word, part of a word, punctuation, or another unit used by the model.

```text
Input so far:
    "The capital of France is"

Model estimates possible next tokens:
    " Paris"     high probability
    " Lyon"      lower probability
    " blue"      very low probability
```

The model chooses a token, adds it to the sequence, and predicts again.

```text
text so far ──> predict next token ──> append token
     ▲                                      │
     └──────────────── repeat ──────────────┘
```

This description sounds too small to explain the resulting abilities. How could next-token prediction produce summaries, code, plans, analogies, or answers to questions?

To predict language well across many domains, the model must capture patterns that produced that language. Grammar matters. Relationships among concepts matter. The structure of arguments matters. Code syntax and common program behavior matter. Facts frequently expressed in the training material matter. As models and training improved, useful capabilities emerged from this learned structure.

The **Transformer** architecture, introduced in 2017, made it practical to learn rich relationships among tokens by letting the model weigh which parts of the available context matter to each other. Later large language models showed that a single trained model could perform many tasks from instructions and a small number of examples supplied in the prompt, without being retrained separately for every task.

The term **large language model**, or **LLM**, describes this family of models at a scale where broad language abilities become useful. “Large” does not explain every capability, and models differ greatly, but the name captures the shift from narrow language components toward systems that can respond across many domains.

For our story, the crucial property is not that an LLM knows everything. It is that the model can interpret a new request at runtime.

```text
Traditional client
    programmer predicts request before deployment

Language-model client
    model interprets request during the conversation
```

This turns natural language into a potential interface for software.

Potential—not automatic reality.

## The Context Is the Model's Immediate World

When you speak to an LLM, the model does not peer directly into your computer, company, calendar, or database. It generates a response from the information made available in its current input and from patterns learned during training.

The current input is often called the model's **context**. It may include the user's message, earlier conversation, system instructions, relevant documents, and structured descriptions supplied by the application.

```text
System instructions ──┐
Conversation history ─┤
Selected documents ───┼──> model context ──> generated response
Current user request ─┤
Other supplied data ──┘
```

The context is not the same as the model's training. Training shapes the model's general behavior and learned patterns before this conversation. Context supplies immediate information for this particular interaction.

This distinction explains why a model can discuss calendars in general yet not know what is on *your* calendar today. It may know what travel policies typically contain without knowing your employer's current policy. It may explain how flight booking works while lacking access to live inventory.

The model's training is broad but not a live connection to the world.

Even information encountered during training may be incomplete, outdated, or imperfectly recalled. A model generates a plausible continuation; it does not automatically perform a verified database lookup before stating a fact. Fluent language can therefore exceed grounded knowledge.

This is why confident fabrication is possible. The model is optimized to produce coherent output, and a coherent answer can be generated even when the required evidence is missing.

The remedy is not to pretend the model has become a database. It is to give the model a way to obtain authoritative information when the task requires it.

## Knowing About an Action Is Not Performing It

Ask a language model, “How do people send email?” and it can describe the process. Ask it, “Send this message to my professor,” and a different requirement appears.

The model may understand the request perfectly. It may produce an excellent subject line and body. But generating the words “Email sent” does not cause an email to leave your account.

```text
Description in language
    "Send an email to Professor Lee"
              ≠
Effect in the world
    authenticated mail service transmits a message
```

Language models produce outputs. External systems produce effects.

To create an effect, some software must interpret the model's output as a proposed action, validate it, obtain the necessary authority, invoke the external system, and return the result.

```text
User intention
      ↓
Model selects a possible action
      ↓
Application validates and executes it
      ↓
External system changes
      ↓
Result returns to the model
```

This separation is essential for both correctness and safety. We do not want every sentence resembling an action to execute automatically. A model might mention deleting a file while explaining how deletion works. A user might ask what would happen *if* money were transferred. The application needs a clear boundary between language and authorized action.

The model can reason about what should happen. The surrounding system decides what may happen and performs it.

## Reasoning Needs Observations

Suppose the user asks:

> Is my flight delayed, and if so, move tonight's dinner reservation to an hour after I land.

This is not one lookup or one fixed command. The solution depends on information discovered during the task.

```text
Find the user's flight
        ↓
Check current flight status
        ↓
If delayed, calculate new arrival time
        ↓
Find tonight's dinner reservation
        ↓
Check whether a later time is available
        ↓
Ask for confirmation if required
        ↓
Modify the reservation
```

At several points, the next decision depends on an external observation. The model cannot generate the entire correct answer from the original sentence because the answer is not contained there.

This creates a loop between reasoning and interaction:

```text
Reason about what is needed
          ↓
Take an allowed action
          ↓
Observe the result
          ↓
Update the reasoning
          ↓
Take the next action
```

Research systems such as ReAct made this pattern explicit by interleaving language-model reasoning with actions and observations from external environments. The general insight reaches beyond one technique: intelligence acting in an environment needs feedback from that environment.

A plan written once and executed blindly will fail when the world differs from the plan. An interactive model can adapt—if it has a reliable way to learn what actions exist and what those actions returned.

## The Five Things a Model Does Not Magically Know

Return to the airline API from Chapter 4. A programmer learned the API through documentation and encoded that knowledge into the client. If a model is going to select interactions at runtime, the missing knowledge must become visible at runtime too.

The first missing piece is **availability**. The model may know that flight APIs exist in general. It does not know which services this particular host application has connected. A tool available in one environment may be absent in another.

The second is **identity and purpose**. A model needs a meaningful description of what each available operation does. Names alone are unreliable. `create` could create a calendar event, an invoice, or a cloud server.

The third is **input structure**. The operation may require particular arguments with types and constraints. Does departure time use a timezone? Is price expressed in dollars or cents? Which fields are required?

The fourth is **interaction policy**. An operation may be read-only, destructive, expensive, or privacy-sensitive. Some actions require user confirmation. Some data must not be sent to certain services. Technical callability is not equivalent to permission.

The fifth is **result meaning**. After an operation runs, the model needs a structured observation it can interpret. A result should distinguish useful data from failure, partial completion, or a request for additional input.

These five needs can be viewed as one runtime contract:

```text
What is available?
What does it do?
What input does it require?
Under what rules may it be used?
What happened when it ran?
```

This resembles the interface contracts of RPC, but the timing has changed.

In classic RPC, the programmer receives the contract before compiling the client. In an AI-driven application, the model may receive capability descriptions as part of the live interaction and decide which one fits the user's current intention.

```text
RPC-oriented client

contract ──> code generation ──> compiled client ──> known call


Model-oriented client

runtime capabilities ──> model reasoning ──> selected interaction
```

The contract is no longer only a development artifact. It becomes part of the model's context.

## REST Did Not Break

At this point, it would be easy to tell the wrong story.

The wrong story says that REST was too old, insufficiently intelligent, or unable to work with AI. Therefore some new AI-specific technology had to replace it.

Nothing in our reasoning supports that conclusion.

An airline's REST API can continue to identify flights, accept HTTP requests, return structured representations, use standard status codes, scale through stateless interactions, and benefit from caching and layers. The API may be excellent.

The new difficulty exists one level above it.

```text
Model
   │
   │ needs runtime understanding of available capabilities
   ▼
Integration layer
   │
   │ translates selected capability into service interaction
   ▼
REST API, RPC service, database, local file, or other system
```

The underlying service might use REST. It might use RPC. It might be a local command, a database query, or a proprietary SDK. The model should not need every internal communication style poured directly into its prompt.

What is missing is a common way for the AI application to present heterogeneous capabilities to the model and mediate their use.

REST solved how networked resources could be exposed through a Web architecture. The emerging problem is how an AI system learns what context and actions its current environment offers.

Different layer. Different problem.

## A Model Is Not the Whole Application

People often speak of an AI assistant as though the model itself were the complete product. This obscures where important responsibilities live.

The model generates language and selections based on context. The surrounding application manages the conversation, chooses what context to supply, connects to external systems, enforces permissions, presents confirmation to the user, executes actions, and feeds results back.

```text
┌──────────────── AI application ────────────────┐
│                                               │
│  user interface                               │
│       ↓                                       │
│  conversation and policy                      │
│       ↓                                       │
│  language model ⇄ capability integrations     │
│                         ↓                     │
│                   external systems            │
└───────────────────────────────────────────────┘
```

This is not a minor implementation detail. It determines trust.

The model should not hold every credential merely because it can request an action. The model should not silently decide which private files become context. A remote service should not gain arbitrary access to the user's computer. The application must mediate boundaries among the user, model, and external capabilities.

The new client is therefore not simply “the LLM.” It is an AI application in which the model participates in deciding what to do.

That makes the client both more flexible and more complicated than the purpose-built clients of earlier chapters.

## Discovery Is Not Permission

If a model can discover that an operation exists, should it be allowed to invoke it?

No.

A capability description answers a question about possibility. Authorization answers a question about permission. User confirmation answers a question about current intent. These must not be collapsed.

```text
Possible:       This system can delete a repository.
Authorized:     This user has deletion rights.
Intended now:   The user approves deleting this repository.
```

A secure application may expose the existence of an operation while requiring a separate approval before execution. It may hide capabilities the user cannot access. It may restrict arguments. It may allow reading but not writing.

The model's role is to propose useful interactions in service of the user's request. The host application's role includes deciding whether those interactions are permitted and how the user remains in control.

This separation gives us a more mature picture than “connect the model to everything.” Connection without mediation would turn linguistic ambiguity into operational risk.

The desired system combines flexibility with explicit boundaries.

## Deep Intuition: The Client Became a Runtime Interpreter

The traditional client encoded a programmer's decisions before the user arrived.

The AI client interprets the user's intention while the interaction is happening. It may assemble a path through several capabilities that no developer wrote as one fixed workflow.

```text
Traditional application

anticipated workflow ──> fixed code ──> known sequence


AI application

user intention + available capabilities + observations
                         ↓
                 runtime decisions
```

This is a profound shift.

The interface is no longer merely a set of buttons corresponding to predefined code paths. Language allows the user to express goals at a higher level. The model can translate those goals into steps, adjust after observations, and combine systems dynamically.

But runtime interpretation requires runtime grounding. The more freedom the model has to choose a path, the more clearly the environment must describe the available paths.

A train follows tracks laid in advance. It needs no sign explaining what other routes exist because a switch controls its path. A traveler choosing among roads needs a map, signs, current conditions, and rules about where travel is permitted.

Traditional clients were closer to trains. Model-driven clients are closer to travelers.

We changed the client, so the communication boundary must reveal more.

## Common Misconceptions

### “An LLM is a database containing the Internet”

An LLM learns statistical structure from training data. It does not retrieve a verified record from a live copy of the Internet whenever it answers. Its learned information can be incomplete, outdated, or generated incorrectly.

### “If the model can describe an action, it can perform it”

Generating language about an action does not create an external effect. Software outside the model must validate and execute an authorized operation.

### “The model automatically sees my computer and accounts”

The model sees information supplied through its context and observations returned by connected systems. Access must be deliberately provided and mediated by the surrounding application.

### “Connecting an API teaches the model how to use it”

Connectivity supplies a path, not meaning. The model still needs descriptions of available operations, input schemas, policies, and interpretable results.

### “REST cannot support AI applications”

REST APIs can remain excellent underlying services. The AI-specific problem is how capabilities from REST APIs and many other sources are described, discovered, selected, and mediated at runtime.

### “Capability discovery means the model has permission”

Discovery, authorization, and user approval are distinct. A robust application treats them as separate boundaries.

### “The LLM is the AI application”

The model is one component. The host application manages context, user interaction, policies, credentials, integrations, execution, and observations.

## Summary: The Assumption We Removed

RPC assumed that a programmer had built the client against a known procedure contract. REST APIs assumed that a programmer had read documentation and encoded domain knowledge into purpose-built software. These were reasonable assumptions because human programmers created the clients.

Large language models introduced a different kind of client behavior. A model could interpret new natural-language requests at runtime, reason about steps, and adjust its plan after receiving observations.

But language understanding did not provide live data, software access, credentials, schemas, or authority. A model could recognize that it needed a flight search without knowing which flight service was available. It could propose sending an email without being able—or necessarily being permitted—to send one.

The surrounding AI application therefore had to connect three worlds:

```text
User intention
      ↓
Model reasoning
      ↓
Available information and actions
```

To make that connection reliable, capabilities needed runtime descriptions. The model needed to learn what was available, what each capability meant, what input it required, under what policy it could be used, and what result came back.

The REST API did not fail. The client changed.

## Transition: One New Client, Many Private Languages

Once developers recognized that models needed access to external information and actions, they began building bridges.

One AI platform described callable functions in one shape. Another described tools differently. Frameworks created their own abstractions. Applications wrapped REST APIs, databases, files, search engines, and local commands in whatever format their chosen model or library expected.

Each bridge solved an immediate problem.

```text
AI application A ── custom description ──> calendar
AI application B ── different wrapper ───> calendar
AI application C ── another adapter ─────> calendar
```

The model could finally act—but every ecosystem was teaching capabilities in a different language.

Change the model provider, and the wrapper might need to change. Change the host application, and the integration might need to be rebuilt. A company with ten systems and five AI clients could face dozens of bridges.

We have seen this pattern before. When every pair of participants invents a private agreement, integration cost grows with the connections between them.

The industry had discovered how to give an individual model a capability.

It had not yet agreed on how AI applications and capability providers should introduce themselves.

## Research Notes

The language-model account in this chapter is grounded in the Transformer paper, [“Attention Is All You Need”](https://arxiv.org/abs/1706.03762), and the demonstration of broad in-context task performance in [“Language Models are Few-Shot Learners”](https://arxiv.org/abs/2005.14165). The reasoning–action–observation loop is informed by [“ReAct: Synergizing Reasoning and Acting in Language Models”](https://arxiv.org/abs/2210.03629).

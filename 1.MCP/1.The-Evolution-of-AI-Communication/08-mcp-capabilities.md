# Chapter 8: MCP Capabilities

## Opening Story: The Assistant That Treated Everything Like a Button

Suppose a university connects an AI research assistant to a laboratory server.

The server can search an article database. It can provide the laboratory's safety handbook. It can offer a carefully designed workflow for reviewing an experimental proposal.

An early design might expose all three as callable functions:

```text
search_articles(query)
read_safety_handbook()
review_experimental_proposal(topic)
```

Technically, this can work. Every useful thing is represented as a button the model can press.

But the three capabilities do not play the same role.

Searching performs an operation whose result depends on input and the current external system. The handbook is information with an identity that an application may browse, select, cache, or attach as context. The review workflow is a prepared way for a person and model to approach a task.

Treating all three as identical functions discards meaning the Host could use.

```text
Search articles                 Do something
Safety handbook                Know something
Proposal-review workflow       Approach something in a prepared way
```

An AI application interacts with the world through more than actions. It needs information to reason from, and people sometimes need reusable guidance for directing that reasoning.

MCP gives these three relationships separate names:

```text
Actions              → Tools
Knowledge            → Resources
Reasoning guidance   → Prompts
```

The terminology is easy to memorize. Our task is to understand why the distinctions exist.

## Capability Types Are Also Control Decisions

Before examining each primitive, ask who should decide when it enters the interaction.

If the user asks, “What is the weather in Boston?” the model can infer that a weather lookup is needed. The capability behaves naturally as a model-selected action.

If an application displays a project file tree, the application may let the user attach one file or may retrieve relevant files according to its own context strategy. The model should not necessarily read every available file. The resource behaves naturally as application-selected context.

If a server offers “Review this pull request using our security checklist,” the person may choose that prepared workflow from a menu or command. The prompt behaves naturally as a user-selected interaction.

This yields MCP's intended control hierarchy:

```text
Tools       model-controlled
Resources   application-controlled
Prompts     user-controlled
```

These labels describe the intended interaction model, not an enforcement spell. The Host remains responsible for authorization and user consent. A model selecting a destructive Tool does not authorize its execution. An application selecting a Resource does not make its contents trustworthy. A user selecting a Prompt does not guarantee that every instruction inside it is safe.

The value of the distinction is architectural. It tells Hosts how each capability is expected to enter the user–model conversation.

## Tools Begin With a Gap Between Intention and Effect

The user says:

> Create an issue for the login failure and assign it to the authentication team.

The model understands the desired outcome, but language alone cannot create the issue. Some executable operation must cross the boundary into the project tracker.

That is the problem a **Tool** solves.

A Tool is an operation a Server exposes for a Client to call. Its definition needs enough structure for the Host and model to understand and use it:

```text
name
    stable programmatic identity

description
    what the operation does and when it is useful

input schema
    arguments, types, requirements, and constraints

optional output schema
    expected structure of a successful result
```

For example:

```json
{
  "name": "create_issue",
  "description": "Create a new issue in the selected project",
  "inputSchema": {
    "type": "object",
    "properties": {
      "title": { "type": "string" },
      "body": { "type": "string" },
      "team": { "type": "string" }
    },
    "required": ["title", "body"]
  }
}
```

The description supplies semantic guidance. The schema supplies structural discipline. Neither can replace the other.

A schema might prove that `title` is text, but not whether the title accurately describes the user's problem. A description might explain that a Tool creates issues, but without a schema the application cannot reliably validate the required arguments.

```text
Description answers:  What does this mean?
Schema answers:       What shape must the input have?
```

MCP uses JSON Schema because the ecosystem already has a rich, language-independent vocabulary for describing structured data. Reusing it allows validation and tooling without inventing an MCP-only type system.

## Discovery Before Invocation

A central purpose of MCP is runtime discovery. The Client need not have every Tool compiled into its application code.

The interaction follows a simple pattern:

```text
Client ── tools/list ─────────────> Server
Client <── names, descriptions,
           schemas ─────────────── Server

Host presents suitable Tools to model

Client ── tools/call + arguments ─> Server
Client <── content or error ────── Server
```

The `tools/list` response teaches the Host what this Server currently offers. The Host can translate those definitions into the tool format expected by its chosen model. When the model selects one, the Host applies policy and the Client sends `tools/call` if execution is allowed.

Discovery does not mean dumping every Tool from every Server into every model request. Tool definitions consume context, similar Tools can confuse selection, and some Tools should be hidden by policy. A Host may search, filter, group, or reveal Tools progressively.

The protocol creates the possibility of discovery. The Host designs the experience.

Servers can also announce that their Tool list changed when the negotiated revision and capability support such notifications. A Client can then refresh instead of assuming the initial list remains eternal. This matters for dynamic environments: a user may sign in, gain access to a project, install an extension, or change modes.

## Tool Results Are Observations, Not Final Answers

After a Tool runs, the Server returns a result. That result may contain text, images, audio, structured content, links to Resources, or embedded Resource content, depending on the negotiated protocol revision and Host support.

Why allow structured results as well as prose?

Suppose a flight Tool returns:

```text
Flight 481 leaves at 08:10 and arrives at 10:02 for $327.
```

The model can read this. But software that needs to sort twenty flights must extract fields from prose. A structured result preserves the data's shape:

```json
{
  "flight": "481",
  "departure": "08:10",
  "arrival": "10:02",
  "price": 327,
  "currency": "USD"
}
```

An optional output schema lets the Server declare that shape and lets the Client validate it.

The result returns to the Host as an observation. The model may use it to answer, choose another Tool, or revise its plan.

```text
Reason → call Tool → observe result → reason again
```

The Tool does not have to produce the user's final response. It contributes one grounded step.

## Tool Metadata Is a Hint, Not a Safety Guarantee

Tools may include annotations suggesting that an operation is read-only, destructive, idempotent, or connected to an open external world.

These hints can improve user interfaces and approval policy. A Host may display a stronger warning for a destructive action or treat a read-only lookup differently from a write.

But the annotations come from the Server. An untrusted Server can label a destructive operation “read only.” The protocol explicitly treats such annotations as hints rather than proof.

```text
Server claims:   readOnly = true

Host concludes:  useful signal if Server is trusted,
                 not an independently verified fact
```

Schemas also validate shape, not intention. A valid `repository` string could name the wrong repository. A valid `amount` could transfer too much money.

MCP makes operations describable. The Host and user remain responsible for deciding whether a proposed call is appropriate.

## Resources Begin With a Different Problem

Now suppose the user asks:

> Does this experimental plan comply with our laboratory's safety policy?

The model needs the current policy. Reading it is not merely an arbitrary action. The policy is a body of information with an identity, a type, and perhaps a changing version. The Host may want to browse available documents, let the user attach one, cache it, or subscribe to changes.

This is the problem a **Resource** solves.

A Resource is context-bearing content exposed by a Server and identified by a URI.

```text
resource identity
    lab://policies/chemical-safety

metadata
    name, description, media type

content
    text or binary data returned when read
```

Why give information an identity instead of exposing only `read_policy()` as a Tool?

Identity allows the information to participate in application-level context management. The Host can display it before reading, remember what was selected, compare references, cache content, or subscribe to an item whose contents may change. A Tool emphasizes execution; a Resource emphasizes addressable context.

```text
Tool
    "Perform this operation with these arguments."

Resource
    "This piece of context exists at this identity."
```

The distinction resembles the procedure-versus-resource contrast from RPC and REST, but MCP is not simply replaying that debate. Tools and Resources coexist because AI applications need both actions and context.

## Listing, Templating, and Reading Resources

A Client can ask a Server to list known Resources. The response describes available items rather than necessarily returning all their contents.

```text
Client ── resources/list ──────> Server
Client <── resource metadata ── Server

Client ── resources/read URI ──> Server
Client <── resource contents ── Server
```

Separating listing from reading matters. A Server may expose thousands of files or database records. Pulling every byte during discovery would be wasteful and dangerous for the model's finite context.

Some Resource spaces are too large or dynamic to enumerate item by item. A Server can expose **Resource templates** containing variable parts. A template might describe:

```text
repo://issues/{issue_id}
```

The template says that issue Resources can be addressed according to a pattern. It does not require the Server to list every issue in advance.

Resources may also support subscriptions when the Server and Client advertise that feature. The Client subscribes to a URI, and the Server can notify it when the Resource changes. The Host then decides whether to reread or refresh the context.

Once again, capability and policy remain separate. A Resource URI is not a promise that every model should read it. The Host controls what enters context.

## Resources Are Application-Controlled for a Reason

Why are Resources described as application-controlled rather than model-controlled?

Model context is scarce and sensitive. A workspace may contain secrets, personal data, generated files, and irrelevant material. Automatically allowing the model to read every advertised Resource would surrender context policy to capability descriptions supplied by Servers.

The Host may instead let users attach Resources explicitly, select them based on the active editor, retrieve them through search, or expose a Resource-reading Tool when model-directed lookup is appropriate.

```text
Server advertises Resources
          ↓
Host decides which context is relevant and permitted
          ↓
Selected content enters the model interaction
```

“Application-controlled” does not mean the user has no control. A well-designed Host surfaces selection and consent. It means the protocol expects the application—not an arbitrary Server—to manage how Resources become model context.

This protects both relevance and isolation.

## Prompts Begin With Reusable Expertise

Consider a security team that repeatedly reviews incident reports. Its experts have developed a good process:

Begin by separating observed facts from assumptions. Construct a timeline. Identify affected systems. Ask which credentials may have been exposed. End with containment actions and unresolved questions.

A generic model can be told this process every time, but that repeats work and risks inconsistency. The Server closest to the domain could offer a prepared interaction template.

That is the problem an MCP **Prompt** solves.

A Prompt is a reusable set of model-facing messages or instructions, optionally parameterized with arguments. It captures a good way to begin or structure an interaction.

```text
Prompt: review_incident

Arguments:
    incident_id
    review_depth

Generated messages:
    role and instructions for conducting the review
    optionally embedded or linked context
```

This is why “How should I think?” is a useful mental model for Prompts. More precisely, a Prompt offers a prepared way for the user and model to approach a task. It can encode domain vocabulary, sequencing, examples, or interaction patterns.

Prompts are not secret commands that a Server may inject whenever it wishes. They are designed to be user-controlled.

## Why Prompts Belong to the User's Interaction

A Host can list available Prompts and display them as menu items, command-palette actions, or slash commands:

```text
/review-incident
/explain-query-plan
/prepare-release-notes
```

The user chooses one, supplies any arguments, and the Client retrieves the generated Prompt content from the Server.

```text
Client ── prompts/list ─────────> Server
Client <── prompt descriptions ─ Server

User selects a Prompt

Client ── prompts/get + args ───> Server
Client <── prepared messages ─── Server
```

Why not make Prompts model-controlled Tools?

Because selecting a workflow is often an act of user intent. The user is not asking the model to perform an external effect. They are choosing the lens or procedure through which the conversation should proceed.

The Host may show the Prompt's title and description before selection. This makes reusable expertise discoverable without allowing a Server to silently redefine the conversation.

The protocol does not require one specific user interface. “User-controlled” is the design expectation; each Host decides how to express it.

## A Prompt Is Not the Same as a Resource

The safety handbook and the safety-review Prompt may contain overlapping words, but their purposes differ.

```text
Resource: chemical-safety-handbook
    Content to reason from

Prompt: review-experiment-safety
    A prepared interaction for applying safety reasoning
```

A Resource answers, “What should be known?” A Prompt answers, “How should this task be approached?”

The Resource might remain useful in many workflows. The Prompt might refer to the Resource or ask the Host to include relevant content. Neither replaces the other.

This separation improves composition. A user can select a review Prompt while the Host attaches the current policy Resource and the model calls a Tool to inspect live equipment records.

```text
Prompt      structures the review
Resource    supplies the policy
Tool        retrieves current equipment state
```

The three primitives cooperate because they retain different meanings.

## One Server Can Offer All Three

Capability types do not divide Servers into three species. One Server may expose any supported combination.

A database Server might offer:

```text
Tool
    execute_read_only_query

Resource
    database://schema

Prompt
    investigate_slow_query
```

The schema Resource helps the model understand tables and columns. The diagnostic Prompt provides a disciplined investigation workflow. The Tool obtains live query results.

This is a richer design than exposing `do_database_thing(text)` and asking the model to guess everything.

It also keeps control visible. The Host may attach the schema automatically for a database conversation. The user may explicitly select the slow-query workflow. The model may choose the query Tool when it needs an observation.

## Dynamic Discovery Without Infinite Context

Runtime discovery creates a new scaling problem. A Host connected to many Servers might discover thousands of Tools, Resources, and Prompts. A model cannot usefully receive all descriptions in every turn.

MCP's listing operations can be paginated, allowing Clients to retrieve large collections in portions. Hosts can build indexes, search capability metadata, remember frequently used items, or expose only those relevant to the current task.

```text
All connected capabilities
          ↓
Host policy and retrieval
          ↓
Small relevant selection
          ↓
Model context
```

This reinforces a recurring principle: a protocol provides interoperable mechanisms; the Host remains responsible for intelligent context management.

Discovery is not the same as indiscriminate inclusion.

## Deep Intuition: The Three Questions Form a Complete Interaction Loop

Why exactly three core Server primitives?

They correspond to three needs in a grounded model interaction.

The model needs **knowledge** about the environment. Resources provide addressable context.

The model needs a way to create **effects** or obtain computed observations. Tools provide executable operations.

The user may need reusable **guidance** for directing the interaction. Prompts provide prepared workflows.

```text
What should I know?       Resource
        ↓
How should we approach it? Prompt
        ↓
What can I do or observe? Tool
        ↓
New result becomes knowledge for the next step
```

Real systems blur edges. A search Tool returns knowledge. A Resource may be generated dynamically. A Prompt may embed Resource content. The categories describe the control and interaction model, not the physical origin of every byte.

Good protocol abstractions do not eliminate every ambiguous case. They create useful defaults around the differences that matter most.

## Common Misconceptions

### “Everything should be a Tool because Tools are more powerful”

Tools can represent many interactions, but using them for all context and guidance discards resource identity and user-controlled workflow semantics. More generic does not always mean more informative.

### “Resources are files”

Files are one example. A Resource can represent database content, API data, repository history, or any addressable context a Server exposes.

### “Resources are REST resources”

The ideas share addressability, but MCP Resources are a protocol primitive for supplying model context. Their operations and control model belong to MCP rather than the REST uniform interface.

### “Prompts are hidden system instructions from Servers”

MCP Prompts are designed for explicit user selection. A Host should not treat an untrusted Server's Prompt as unquestionable authority.

### “Model-controlled means automatically executed”

The model can select or propose a Tool. The Host still applies permissions, validation, and user approval before calling it.

### “A valid schema means a safe Tool call”

Schemas validate structure. They cannot prove that the action matches user intent, targets the correct object, or is safe.

### “Listing capabilities means placing all of them in the prompt”

Listing supports discovery. Hosts may filter and retrieve relevant capabilities so model context remains manageable.

### “The three primitives never overlap”

A Tool can return Resource content, and a Prompt can include context. The categories remain useful because they express different identities, controls, and purposes.

## Summary: Actions, Knowledge, and Guidance

An AI application needs more than a bag of callable functions.

Tools describe executable operations. They allow a model to propose actions and obtain observations through structured inputs and results. They are model-controlled in selection, but Host-controlled in permission and execution.

Resources provide addressable context. Their URIs, metadata, templates, read operations, and optional subscriptions let Hosts manage information separately from executable actions. They are application-controlled because context selection affects privacy, relevance, and limited model attention.

Prompts provide reusable, parameterized interaction patterns. They capture a useful way to approach a task and are designed for explicit user selection.

The simplest mental model remains powerful:

```text
Tools       What can I do?
Resources   What should I know?
Prompts     How should I approach this?
```

The deeper model adds control:

```text
Tools       model-selected, Host-mediated
Resources   application-selected
Prompts     user-selected
```

Together, the primitives give Server capabilities enough meaning for a Host to present them intelligently rather than flattening every interaction into a generic function.

So far, information and actions have mostly flowed from Server to Host. A harder case now appears.

## Transition: When the Server Needs Something Back

Suppose a deployment Tool begins its work and discovers that the user did not specify a region. The Server cannot safely guess. It needs additional information from the person.

Suppose a research Server has gathered specialized evidence but needs a language model to synthesize it. The Server should not have to embed credentials for every possible model provider, and it should not bypass the Host that controls the user's model relationship.

Suppose a filesystem Server needs to know which directories the Host has made relevant to the current workspace. It must not assume access to the entire machine.

These are reverse needs:

```text
Server needs user input
Server needs model assistance
Server needs Host-scoped environmental context
```

The Server cannot own these powers because the Host owns the user, model, and local policy boundary.

How can the protocol let a Server ask for help without transferring control away from the Host?

## Specification Notes

The control hierarchy and primitive semantics follow the official MCP [Server overview for revision `2025-11-25`](https://modelcontextprotocol.io/specification/2025-11-25/server). Tool structures, result types, and security cautions are grounded in the [`2025-11-25` schema](https://modelcontextprotocol.io/specification/2025-11-25/schema). The user-controlled Prompt model is explained in the official [Prompt specification](https://modelcontextprotocol.io/specification/2025-06-18/server/prompts); the core control principle remains applicable in the current published revision.


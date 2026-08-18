# Chapter 2: Distributed Computing and RPC

## Opening Story: The Function on the Other Side of the Building

At the end of the previous chapter, our airline application had escaped from a single computer.

One machine displayed flights to a ticket agent. Another maintained the authoritative list of reservations. A third spoke to the payment system. Communication allowed these machines to participate in one larger purpose, but it also confronted the programmer with an awkward change.

Inside one computer, reserving a seat might look conceptually simple:

```text
confirmation = reserve_seat(flight, passenger)
```

The programmer gives a named operation two inputs. The operation does some work. It returns a result. This small pattern—name the work, provide inputs, receive an output—is one of the most useful ideas in programming.

But now the reservation data lives on another machine.

The programmer can no longer perform the operation directly. The local program must construct a message, identify the remote machine, send the message across a network, wait for a response, determine whether that response belongs to this request, decode it, handle errors, and finally turn the received bytes back into a useful result.

The single line begins to unfold:

```text
Find the reservation machine
Encode "reserve seat"
Encode the flight and passenger
Send the message
Wait
Receive a response
Decode the response
Check for failure
Produce a confirmation
```

None of this work is part of the airline's business idea. A ticket agent does not care how a passenger's name becomes bytes. An airline designer wants to reason about flights, seats, and reservations—not message boundaries and network addresses.

And so programmers faced a natural question: could interaction with a distant program be made to resemble the familiar act of calling a function?

That question gave rise to one of distributed computing's most influential abstractions.

## The Problem: One Application, Several Independent Machines

When the work of an application is divided among machines, we call the resulting arrangement a **distributed system**.

The phrase can sound grand, but the underlying idea is modest. Some part of the work happens here. Another part happens there. The parts coordinate by exchanging messages.

```text
Machine A                              Machine B
ticket-agent application              reservation service

collect passenger details             own the seat inventory
show available flights       ⇄        reserve and release seats
display confirmation                  create confirmation numbers
```

Why divide the application at all?

In our example, the seat inventory needs one authoritative home. If every ticket office keeps a private copy and updates it independently, two offices can sell the same seat. Centralizing responsibility for reservations gives all offices a shared source of truth.

Other systems distribute work for other reasons. Data may need to remain near the equipment that creates it. A specialized machine may perform one kind of calculation efficiently. Different organizations may own different services. Many machines may share a workload too large for one. A system may keep working when one component fails.

These benefits are real, but they come with an uncomfortable truth: physical separation becomes a programming problem.

Inside a single process, one part of a program can call another because both inhabit the same world. They share the same machine, the same memory conventions, and usually the same programming language. A function call can jump directly to a known piece of code.

Across a network, none of that is automatically true.

```text
Local call

caller ───────────────> function
        same machine
        shared memory
        one runtime


Remote interaction

caller ──> network ──> another program
           delay       another memory
           failure     perhaps another language
```

The programmer now has two problems at once. There is the problem the application exists to solve—reserve a seat—and the problem of communicating across machines.

If every application programmer has to rebuild the communication machinery for every remote operation, distributed software will be slow to create and difficult to trust. Much of that machinery is repetitive. Requests need identifiers. Values need encoding. Responses need matching to requests. Failures need representation.

Repetition suggests an abstraction.

## The Familiar Shape of a Procedure Call

Before hiding remote communication, we need to notice what a normal procedure call gives us.

The terminology varies among programming languages: *procedure*, *function*, *method*, or *subroutine*. The distinctions matter in some contexts, but not for our immediate purpose. Each term describes a named unit of work that another part of a program can invoke.

Consider:

```text
total = calculate_total(price, quantity)
```

The caller knows four things.

It knows the operation's name: `calculate_total`. It knows what inputs the operation expects: a price and a quantity. It knows how to invoke the operation using the language's calling rules. And it knows what kind of result to expect.

Everything else can remain hidden. The caller does not need to know which machine instructions perform the multiplication or where temporary values are stored. The function presents a boundary: honor this calling agreement, and the implementation may change behind it.

This is why a function is more than a convenience. It lets a programmer think at the level of intention.

```text
What the caller means:     calculate the total

What the computer does:    move values, jump to instructions,
                           allocate memory, execute operations,
                           return control, move the result
```

The machinery has not disappeared. It has been placed behind a stable interface.

Now return to the remote reservation service. The programmer wants the same intellectual bargain. Let me express *what* I want—reserve a seat—and let a reusable system handle *how* that request crosses the network.

If the remote operation could look like this,

```text
confirmation = reservations.reserve_seat(flight, passenger)
```

then ordinary programming ideas could organize work even when that work happened somewhere else.

The network would not cease to exist. It would be hidden behind a procedure-shaped interface.

## The Better Idea: Make a Remote Call Look Local

This idea became known as **Remote Procedure Call**, or **RPC**.

The name is almost the whole intuition. A procedure performs named work. A call invokes it. *Remote* means that the procedure runs in another process, often on another machine.

To the application programmer, an RPC aims to resemble an ordinary call:

```text
confirmation = reserve_seat("JL407", "Amina Yusuf")
```

Underneath that line, a carefully arranged conversation occurs:

```text
Client machine                              Server machine

reserve_seat(...)                           reserve_seat(...)
      │                                            ▲
      ▼                                            │
client helper                             server helper
      │                                            ▲
      │ request: procedure + arguments             │
      └───────────────────────────────────────────>│
                                                   │ call procedure
                                                   │
      ┌────────────────────────────────────────────┘
      │ response: result or error
      ▼
return confirmation
```

The program requesting the work is the **client**. The program offering the work is the **server**. These words describe roles in an interaction, not necessarily permanent identities. A program can be a server in one conversation and a client in another.

Between the application code and the network sit helper components. Their purpose is to preserve the illusion of an ordinary call while performing the necessary communication.

On the client side, a helper accepts the procedure's arguments. It converts them into a transferable representation and sends a request. On the server side, another helper decodes the request, invokes the actual procedure, collects the result, encodes it, and sends it back. The client-side helper then returns that result to the caller.

Historically, these helpers are often called **stubs** because each stands in for something located elsewhere. The client stub looks like the remote procedure to the local program. The server stub looks like the local caller to the remote procedure.

```text
Application code
      │
      ▼
Client stub ── message ──> Server stub
                              │
                              ▼
                       Real procedure
```

The stubs turn a programming-language interaction into messages and then turn the messages back into a programming-language interaction.

This translation is the heart of RPC.

## How Values Cross a Boundary Between Memories

Suppose the local program calls:

```text
reserve_seat("JL407", 18)
```

Inside one process, the text `"JL407"` and the number `18` occupy locations in that process's memory. Sending the locations themselves would be meaningless. The remote machine has its own memory. Address 4,218 on one machine does not refer to the same thing at address 4,218 on another.

The values must be turned into a shared representation that can travel.

```text
Local values
    ↓
Encode into a message
    ↓
Bytes cross the network
    ↓
Decode into remote values
```

This conversion is commonly called **marshalling**. The reverse conversion is **unmarshalling**. The words are less important than the need that produced them: values cannot cross between separate memories unless both sides agree on how those values are represented.

A request might conceptually contain:

```text
procedure: reserve_seat
argument 1: text "JL407"
argument 2: integer 18
request id: 731
```

The response might contain:

```text
request id: 731
status: success
result: confirmation "R8K2Q"
```

The request identifier matters when several calls are in progress. If responses return at different times, the client must know which answer belongs to which question.

Once again, a protocol appears because independent participants require shared meaning. RPC is not magic that avoids messages. It is an agreement that organizes messages around the familiar semantics of calling procedures.

## The Contract Must Exist Before the Call

How does the client stub know that `reserve_seat` takes a flight identifier and a seat number? How does it know that the first argument is text, the second is an integer, and the result is a confirmation? How does the server know which incoming message should invoke which procedure?

Both sides need a shared description of the interface.

Conceptually, it might look like this:

```text
service Reservations

procedure reserve_seat(
    flight: Text,
    seat: Integer
) -> Confirmation
```

This description is a contract. From it, tools can generate compatible client and server stubs. The client programmer receives something that feels like a local function. The server programmer receives the machinery that connects an incoming request to the implementation.

```text
                     Shared interface contract
                    /                         \
                   ▼                           ▼
          Generate client stub        Generate server stub
                   │                           │
                   ▼                           ▼
          Client application    ⇄      Server implementation
```

This was a powerful design choice. Machines might use different internal representations for numbers. Programs might be compiled separately. The interface contract gave tools enough information to create the translation layer consistently.

It also reveals an assumption that will matter later: before making a call, the client must possess the contract.

For now, that assumption is reasonable. The airline's developers know they are building against the reservation service. They obtain its interface, generate or install the client code, and write calls to known procedures. If the service changes incompatibly, the client may need to be regenerated, tested, and deployed again.

RPC is designed for a world in which programmers arrange the relationship in advance.

## Why RPC Was Brilliant

It is easy to criticize an abstraction after seeing decades of systems built with it. To understand RPC, we should first appreciate what it accomplished.

RPC allowed programmers to preserve the most natural unit of imperative programming—the procedure call—across a machine boundary. Application code could describe business intentions without manually constructing every message.

It separated concerns. Specialists could improve encoding, transport, binding, timeouts, and request matching without forcing every application author to reproduce that work. Interface descriptions made contracts explicit and enabled tooling. Generated stubs reduced the chance that client and server would encode the same operation differently.

Most importantly, RPC provided a mental bridge from local programs to distributed ones.

```text
Before RPC                         With RPC

construct message                  reserve_seat(...)
encode arguments
send bytes                         Communication machinery
match response        ───────>     moves behind the call
decode result                      boundary.
handle protocol details
```

This is what a good abstraction does. It does not abolish complexity. It places recurring complexity behind a boundary so people can reason at a higher level.

The abstraction was not merely theoretical. In a foundational 1984 paper, Andrew Birrell and Bruce Nelson described an RPC system built around the goal that remote calls should have semantics as close as practical to ordinary procedure calls. The idea influenced generations of distributed systems and survives in modern RPC frameworks.

But notice the cautious phrase: *as close as practical*.

Remote calls can resemble local calls. They can never truly become local calls.

## The Network Refuses to Disappear

Call a local function and, under normal conditions, it either returns, raises a local error, or the process fails. The caller and function share a fate more closely because they live in the same running program.

A remote call has more possible stories.

The request may never reach the server. The server may perform the operation and crash before replying. The response may be lost. The network may be slow enough that the client gives up even though the server is still working. The server may restart and forget earlier requests. The client may retry an operation that already succeeded.

Consider a payment call:

```text
Client ── "charge $100" ──> Server
Client <── response lost ──X Server
```

The client sees no response. What happened?

It cannot know from silence alone. Perhaps the request never arrived, so no money was charged. Perhaps the charge succeeded and only the response was lost. Retrying is correct in the first case and dangerous in the second.

This uncertainty does not occur in quite the same way with a local call. Distance introduces partial failure: one part of the system can fail, or merely appear to fail, while another continues.

Time changes too. A local function call is usually fast and predictable enough that programmers treat it as immediate. A remote call crosses operating systems, queues, networks, and another process. It may take milliseconds, seconds, or much longer. Writing it with local-call syntax can hide a performance difference of enormous scale.

Values also cross imperfectly. Simple data such as numbers and text can be encoded. A pointer into local memory cannot be sent meaningfully. An open file, a live database connection, or an object tied to a local runtime cannot simply materialize on the other machine. The interface has to be designed around transferable data.

RPC therefore creates a productive illusion, but the illusion leaks.

```text
The call looks local
        │
        ▼
But distance still creates:
delay • independent failure • uncertain outcomes • data boundaries
```

A careful programmer must remember both truths at once: use the procedure abstraction to make distributed work understandable, but never forget that the procedure is remote.

## Finding the Right Server

Even before a call can fail, the client has to know where to send it.

The name `reserve_seat` identifies the desired operation, but it does not necessarily identify the machine currently offering it. Servers move. Machines are replaced. Several servers may offer the same service. Network addresses can change.

RPC systems therefore need some form of **binding**: connecting the abstract service the client wants with a concrete server capable of providing it.

```text
Client wants:
    Reservations service
          │
          ▼
Binding mechanism finds:
    server at a reachable location
          │
          ▼
Client sends the call there
```

The mechanism may be configured in advance, discovered through a directory, or handled by surrounding infrastructure. Whatever the method, another hidden step has appeared beneath the innocent-looking procedure call.

This reinforces an important point: RPC does not eliminate networking. It gives networking a shape that fits how programmers already organize code.

## The Hidden Assumptions of RPC

By now we can see the world for which RPC is a natural solution.

A programmer is building a particular client for a particular service. The programmer knows the service's interface. The available procedures and their argument types are agreed in advance. Client and server share compatible generated code or otherwise honor the same contract. A binding mechanism can locate the server. The programmer understands that some apparently ordinary calls cross a failure-prone network.

Under those conditions, RPC is elegant.

The most important assumption is not that the network is perfectly reliable; serious RPC systems devote considerable effort to failures. The deeper assumption is that **the client already knows what can be called**.

The client does not ordinarily begin a conversation by asking, “What useful abilities exist here, and how should I use them?” Its code was written around a known interface:

```text
Known before the program runs

procedure name
argument names and types
result type
service contract
```

This advance knowledge is what makes the call feel native. The compiler or generator can create a convenient function because someone has already described the function precisely.

That is not a flaw. It is the bargain.

RPC trades flexibility at runtime for clarity and convenience at development time. When teams coordinate closely and service relationships are known, that trade can be excellent.

## Common Misconceptions

### “RPC means there is no protocol”

RPC is built from protocol agreements. The procedure-shaped interface hides message construction from application code, but the client and server still need shared rules for encoding requests, matching responses, representing errors, and locating operations.

### “A remote procedure call is the same as a local function call”

It is intentionally made to resemble one. It cannot share all the same behavior. Remote calls introduce latency, independent failure, uncertain outcomes, and restrictions on transferable values.

### “RPC replaced ordinary network messages”

RPC organizes network messages. Beneath the call, requests and responses still travel. The abstraction changes what the programmer sees, not the physical reality.

### “RPC was naïve because networks fail”

RPC designers understood network failure. Binding, retransmission, duplicate handling, and call semantics were central design concerns. The challenge is not that designers forgot the network; it is that no abstraction can make remote failure identical to local failure.

### “RPC is obsolete”

The core idea remains useful and widely used. Modern systems still expose named remote operations through generated clients and explicit contracts. Technologies survive when the problem they solve survives.

### “RPC clients discover arbitrary abilities at runtime”

Some systems provide introspection or service discovery, but the classic programming model assumes a client built against a known interface. Discovering where a known service is running is different from discovering what an unfamiliar service can do.

## Summary: What RPC Gave Us

Distributing an application created a new burden. Programmers who wanted to reserve seats or process payments suddenly had to encode messages, locate servers, match responses, and translate values between separate memories.

RPC placed that recurring machinery behind the familiar abstraction of a procedure call.

Client and server shared an interface contract. Helper code translated local values into messages, invoked the remote implementation, and translated the response back into a local result. This made distributed programs easier to write and reason about.

The abstraction worked because its world was arranged in advance. A human programmer knew the remote service, obtained its contract, and built the client around specific procedures. The client might need to discover where the service was located, but it already knew what the service could do.

RPC did not make the network disappear. Delay, partial failure, uncertain outcomes, and separate memory remained. Still, it gave programmers a remarkably productive way to express work across machines.

Then the communication problem changed again.

## Transition: What If the Participants Have Never Met?

Our airline's client and reservation server belong to a deliberately designed application. Their developers can coordinate. They can share an interface contract, generate compatible stubs, and deploy software that knows exactly which procedures it intends to call.

Now imagine a much larger ambition.

Suppose information is stored on computers around the world. The owners do not coordinate with every potential reader. A person should be able to move from a document on one machine to a related document on another, even though the authors and readers have never met. New documents should appear without requiring every reader's software to be rebuilt. The system should welcome different kinds of computers and independent organizations.

RPC can certainly move data between machines. But procedure calls are shaped around prior knowledge of a service contract. A worldwide information space needs a looser relationship.

The reader's program should not need a custom procedure interface for every library, university, laboratory, or company it visits. It needs a common way to ask for a document identified by a global address—and a common way for that document to point somewhere else.

The next great communication problem is therefore not “How can one program invoke a known function on another machine?”

It is this:

How can people navigate a world of information published by strangers?

## Historical Note

The account of classic RPC in this chapter is grounded in Andrew Birrell and Bruce Nelson's 1984 paper, [“Implementing Remote Procedure Calls”](https://www.microsoft.com/en-us/research/publication/implementing-remote-procedure-calls/). The chapter presents the design causally rather than attempting a complete history of every earlier or parallel RPC system.


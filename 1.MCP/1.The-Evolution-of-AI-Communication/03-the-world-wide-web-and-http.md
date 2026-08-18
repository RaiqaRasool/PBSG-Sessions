# Chapter 3: The World Wide Web and HTTP

## Opening Story: A Laboratory Full of Islands

The previous chapter ended with a larger ambition than calling a known function on a known service.

Imagine arriving at a major research laboratory. Thousands of people work there. Some stay for decades; others visit for a few months and return home. They use different computers, create different file formats, and organize knowledge according to the needs of their own teams.

The laboratory does not lack information. It is overflowing with information.

The difficulty is finding the right piece.

A description of one experiment may refer to a person in another department. That person may have written a report stored on another computer. The report may depend on equipment documented somewhere else. The connections among these things exist in people's minds, handwritten notes, filenames, and conversations—but not in one navigable system.

Adding more documents makes the problem worse. Information grows faster than any one person can learn where it all lives.

This was not merely a fictional puzzle. In 1989, while working at CERN, Tim Berners-Lee proposed a way to connect information across the organization. CERN's changing population, varied machines, and sprawling knowledge made it a particularly vivid example of a general problem: information could be reachable by computer and still be practically difficult to discover.

RPC had shown how one program could invoke a known procedure on another machine. But a person exploring a worldwide body of knowledge did not begin with a procedure contract. The person might not know which institution owned the next document, which computer stored it, or what software produced it.

The new problem was not remote execution.

It was remote exploration.

## The Internet Was Already There

Before we create the solution, we need to separate two ideas that are now so tightly associated that people often use their names interchangeably.

By the time the Web was proposed, computers were already connected through the **Internet**. The Internet provided a way for networks and machines to exchange data across organizational and geographic boundaries. It was the underlying communications environment on which many applications could operate.

People already used networked services such as email, file transfer, and remote login. The Internet was not waiting for the Web to make computers communicate.

Think of the distinction this way:

```text
Internet
    The connected infrastructure that can carry data

Web
    An information system built using that connectivity
```

A road system does not tell travelers which books are related to other books. It merely makes movement between buildings possible. A library system can use those roads to exchange books, but the roads and the library are not the same invention.

Likewise, the Internet could carry messages between machines without providing a universal way to publish, identify, retrieve, and connect documents.

The network answered:

> Can data travel from this computer to that computer?

The emerging information problem asked:

> Once machines are connected, how can a person move naturally through the knowledge stored among them?

The distinction matters throughout this manuscript. Communication technologies often build on older layers rather than replacing them. The Web would use the Internet. It would not *become* the Internet.

## The Problem: Knowledge Without a Common Map

Suppose a researcher learns that a useful document exists on a university computer in another country. Having network access is only the beginning.

The researcher needs to know which machine holds the document. The machine may offer several network services, so the researcher must know which service to use. Within that service, the researcher needs a path or name that identifies the particular document. Then the researcher needs compatible software and enough knowledge of the remote system to retrieve it.

Even after obtaining the document, references inside it may be plain text:

```text
For detector specifications, see Maria's report on the Geneva system.
```

Where is Maria's report? Which Maria? Which computer is “the Geneva system”? What program opens it? The sentence expresses a relationship but does not make that relationship directly traversable.

Information is most valuable when its connections can be followed.

Human thought is full of associations. While reading about a scientific instrument, we may want to see the engineer who designed it, the experiment that used it, the paper that interpreted the results, and the data behind the paper. These relationships do not naturally form a neat hierarchy. They form a web.

```text
                        ┌──> engineer
                        │
instrument ──> experiment ──> paper ──> dataset
     │                  │
     └──> manual        └──> research group
```

The reader should be able to follow any meaningful connection without first understanding the storage arrangement behind it.

That creates three needs.

First, every publishable thing needs an address that can work across the whole system. Second, documents need a way to contain traversable links to those addresses. Third, a reader's program and a publisher's program need a simple conversation for retrieving whatever an address identifies.

Addressing. Linking. Retrieval.

These three ideas would become the foundation of the Web.

## One Address Space for a Worldwide System

Imagine trying to mail a letter using only the instruction “Deliver this to room 12.” Room 12 exists in countless buildings. The instruction makes sense only if the building is already understood.

A worldwide information system cannot rely on local names alone. `/reports/detector.html` may identify a file within one computer, but the reader also needs to know which computer and which access mechanism.

The address must carry enough context to identify something globally.

You already recognize the resulting shape:

```text
http://example.org/reports/detector.html
```

Read it from left to right as a set of increasingly specific decisions:

```text
http://          use this kind of retrieval conversation
example.org      contact this named host
/reports/...     ask for this item within that host's space
```

The formal vocabulary around Web identifiers evolved, and distinctions among names, locators, URLs, and URIs have generated more debate than a beginner needs at this moment. The durable intuition is simple: a resource needs an identifier that can be carried outside the machine that owns it.

Once an identifier is global, it can be copied into another document, sent in an email, printed on paper, bookmarked, or shared with a stranger. The recipient does not need a private arrangement with the publisher. The address contains the starting instructions.

This creates a powerful separation:

```text
Identity visible to the Web
        │
        ▼
http://example.org/reports/detector.html
        │
        ▼
Implementation hidden behind the address
```

The publisher may reorganize disks, replace the server program, or generate the content differently while preserving the public identifier. As long as the address continues to lead to the intended information, readers need not know what changed internally.

An address solves the problem of reference. It does not yet solve navigation.

## From References to Links

Documents have referred to other documents for centuries. A footnote tells a reader that another source exists. A bibliography provides enough information to search for it. The relationship is meaningful, but following it requires work.

In a computer-based information space, the reference can contain the destination's global address. The reading program can make the reference interactive.

```text
Document A

"The detector uses a [superconducting magnet]."
                        │
                        │ embedded address
                        ▼
Document B: Superconducting Magnet Design
```

The visible phrase gives the relationship human meaning. The hidden address gives software a destination. A reader selects the phrase, and the computer retrieves the related document.

This is **hypertext**: text whose connections to other information can be followed directly rather than merely described. Hypertext ideas existed before the Web. The decisive leap was combining navigable links with global addressing and Internet reach.

The result was not a central database into which the world had to upload its knowledge. Each publisher could keep control of its own machine and documents. Common agreements made the pieces navigable as one space.

```text
University A          Laboratory B          Company C
┌──────────┐          ┌──────────┐          ┌──────────┐
│ document │ ───────> │ document │ ───────> │ document │
└──────────┘          └──────────┘          └──────────┘
 own server            own server            own server

         Together perceived as one information space
```

This decentralized design was essential. A worldwide system could not require one organization to approve every document or understand every publisher's internal software. Participants needed only to honor common boundaries.

The document format used for these structured pages and links became known as **HTML**, the HyperText Markup Language. HTML did not carry documents across the network. It described a document's structure and its links.

We now have globally usable addresses and documents containing links. One question remains: when the reader selects a link, what exactly do the two computers say to each other?

## The Simplest Useful Conversation

The reader uses a program that can display Web documents and follow their links. We call it a **browser** because its human purpose is to browse an information space.

Somewhere else, a program waits for requests and provides published information. We call it a **server** because it serves that information.

The browser has an address. From the address, it can determine which server to contact and which item to request. The most natural conversation is astonishingly small:

```text
Browser                                   Web server
   │                                          │
   │  Please send the item at this path.      │
   │ ────────────────────────────────────────>│
   │                                          │
   │  Here is the document.                   │
   │ <────────────────────────────────────────│
   │                                          │
```

This is a **request–response** interaction. One participant requests something. The other returns a response describing the outcome and, when appropriate, carrying the requested content.

At the beginning, this was enough to make the Web work. A browser could request a hypertext document, display it, discover addresses embedded within it, and repeat the process when the reader chose a link.

```text
Retrieve page
     ↓
Display page and its links
     ↓
Reader chooses a link
     ↓
Retrieve another page, perhaps from another server
     ↓
Continue
```

The common language governing that browser–server conversation became the **Hypertext Transfer Protocol**: HTTP.

Again, the name tells the story after we have earned it. *Hypertext* was the connected information being navigated. *Transfer* was the immediate task. *Protocol* was the shared agreement that allowed independently written browsers and servers to understand the exchange.

## What an HTTP Message Needs to Express

Let us invent the conversation ourselves.

The browser must identify what it wants to do and which target it wants that action applied to. For simple retrieval, it might send something conceptually like:

```text
GET /reports/detector.html
```

`GET` states the intention: retrieve a representation of the target. The remaining text identifies the target within the server.

The server must report whether the request succeeded. If it did, the response needs to describe the content and carry it. If it did not, the response needs to distinguish among situations that may require different reactions.

```text
Success:

200 OK
Content-Type: text/html

<html> ... document ... </html>
```

Or:

```text
Failure:

404 Not Found
```

The exact syntax changed as HTTP evolved. The conceptual pieces remained recognizable:

```text
Request
    intention + target + supporting information

Response
    outcome + supporting information + optional content
```

Why include a content type such as `text/html`? Because an address does not guarantee that every response is a hypertext page. The Web quickly needed to carry images, plain text, and many other forms of data. If the response describes what it contains, the browser can decide how to handle it.

Why use numeric status codes? Software needs a compact, stable way to distinguish success, redirection, a problem in the request, and a failure at the server. A human-readable phrase can accompany the number, but automated clients can base behavior on the code.

Why include additional descriptive fields—headers—rather than place everything in one rigid message? Extensible metadata allows the conversation to grow. Browsers and servers can negotiate formats, describe caching, report dates, carry authentication information, and add later features while preserving the basic request–response shape.

HTTP's design was small enough for independent implementations and extensible enough to grow with the Web.

## Statelessness: Each Request Brings Its Own Meaning

Early Web browsing created a revealing interaction pattern. A browser requested a document. The server returned it. That exchange could stand largely on its own.

```text
Request page A ──> Response A

Request page B ──> Response B
```

The server did not need to remember a private conversation merely to understand what page B meant. The second request identified its own target and intention.

This property is called **statelessness** at the protocol interaction level: the meaning of a request does not depend on the server remembering a hidden sequence of earlier requests from that client.

Stateless does not mean the server stores no information. A server obviously stores documents, configuration, logs, and other data. It means the request carries the information needed to interpret that interaction rather than relying on temporary conversational memory established by previous requests.

The distinction is easier with a counterexample.

Imagine a protocol like this:

```text
Client: Begin conversation 91.
Client: Open the reports folder.
Client: Select the third file.
Client: Send it.
```

To understand “the third file,” the server must remember what conversation 91 previously opened. If the request reaches a different server or the conversational state is lost, the instruction becomes meaningless.

Compare a self-contained target:

```text
GET /reports/detector.html
```

Any suitable server with access to that resource can interpret the request directly.

This mattered for a system expected to grow beyond any one organization's control. Self-contained requests are easier to route, retry, inspect, cache, and distribute among servers. We will return to these advantages when the Web grows from documents into applications.

For now, statelessness fits the browsing problem beautifully. A person can jump from one publisher to another. Each retrieval states what it needs.

## Why HTTP Was Not “RPC for Documents”

HTTP and RPC both use requests and responses. Both can operate across networks. It is tempting to place them in a contest and ask which one won.

That is the wrong question.

RPC began with a programmer who knew a remote interface and wanted to invoke a named procedure as if it were local:

```text
reserve_seat(flight, passenger)
```

The early Web began with a reader who possessed a global identifier and wanted a representation of the identified information:

```text
GET /reports/detector.html
```

Their centers of gravity were different.

```text
RPC                                  Early HTTP

Known service contract               Global information space
Named procedures                     Addressed documents
Programmer-oriented call             Browser–server retrieval
Client built for interface           General browser follows links
```

HTTP did not arrive because RPC had failed at distributed computing. HTTP served the architecture of the Web: independently published, globally identified, interlinked information retrieved by general-purpose clients.

A road and a railway can both move people without one being a failed version of the other. Their design choices follow from different environments and purposes.

This distinction will protect us from a common historical mistake. The path from RPC to HTTP is not a simple upgrade sequence. It is a change in the problem being solved.

## Deep Intuition: The Web Standardized the Boundaries, Not the World

The Web could not require every organization to use the same computer, operating system, database, or publishing process. Such a system would never become worldwide.

Instead, it standardized a few boundaries:

```text
How is something identified?       A global identifier
How can documents connect?         Hyperlinks in a shared format
How is content requested?          A common request–response protocol
```

Behind those boundaries, publishers retained freedom.

A server could retrieve a page from a file. Another could construct it from stored records. A browser could run on one kind of computer or another. A university could publish without asking a central authority to redesign the entire system.

This is the same engineering bargain we encountered with protocols in Chapter 1: constrain interaction so implementations can remain independent.

The Web made an additional move of enormous importance. It allowed a document to contain the address of another document. Communication therefore did not merely deliver information; the delivered information described where the communication could go next.

```text
Response contains document
          │
          ▼
Document contains links
          │
          ▼
Links generate possible future requests
```

The reader did not need a complete map before beginning. Each page could reveal the next set of destinations.

That is why browsing feels different from invoking a fixed RPC interface. The route through the information space can emerge during use.

## Common Misconceptions

### “The Internet and the Web are the same thing”

The Internet provides general network connectivity. The Web is an information system built on that connectivity using shared identifiers, document formats, links, and retrieval rules. Email uses the Internet but is not a Web page merely because it travels online.

### “Tim Berners-Lee invented hypertext”

Hypertext ideas and systems existed earlier. The Web combined hypertext with global identifiers, Internet-based retrieval, and an open, decentralized architecture that could grow across organizations.

### “HTTP created computer networking”

Networked communication and the Internet predated HTTP. HTTP defined an application-level conversation suited to the Web.

### “HTTP replaced RPC”

They addressed different primary problems. RPC made known remote procedures convenient to call. HTTP supported interaction with globally identified information in the Web's architecture. Both ideas continued to be useful.

### “Stateless means the server has no database or memory”

Statelessness concerns how individual requests are understood. A server may maintain durable information while requiring each request to contain the context necessary for that interaction.

### “A URL is the actual document”

An address identifies a target. The server returns a representation in response to a request. The same target may be represented in different formats or generated dynamically.

### “HTML and HTTP do the same job”

HTML structures hypertext content and links. HTTP governs the request–response exchange that transfers representations. They cooperate at different boundaries.

## Summary: The Web's Three Agreements

The Internet connected machines, but connectivity alone did not create a navigable information space. Knowledge remained scattered across organizations, computers, formats, and local naming systems.

The Web addressed this problem through a small set of mutually reinforcing ideas.

A global identifier allowed something on one machine to be referenced from anywhere else. Hypertext documents embedded those identifiers as traversable links. HTTP gave browsers and servers a common request–response conversation for retrieving representations.

```text
Addressing tells us where to point.
Linking tells us what may be related.
HTTP lets us ask and receive.
```

These agreements did not standardize how every organization stored information. They standardized the boundaries through which independent systems participated. The result could grow without one central database or one universal computer.

HTTP solved browser–server communication for a distributed hypertext system. It reused the Internet beneath it, and it did not invalidate RPC's procedure-oriented model. Each was shaped by its own problem.

For the early Web, requesting documents was enough.

It would not remain enough for long.

## Transition: When Pages Begin to Do Things

A static document waits to be read. Its author writes it, a server returns it, and a browser displays it. The interaction is largely one-way: publishers create information and readers retrieve it.

But once millions of people can reach a server through a common protocol, they will want more than documents.

They will want to search a catalog rather than download the entire catalog. They will want to submit a form, place an order, update an address, publish a comment, and see information assembled specifically for them. A server will no longer return only files prepared in advance. It will calculate responses from databases and change the world behind the page.

```text
Static Web
reader ── asks for document ──> server

Emerging dynamic Web
user ── expresses intention ──> application
user <── receives new state ─── application
```

HTTP's request–response envelope can carry these interactions. But as websites become applications and organizations expose more operations through the Web, designers face a new architectural question.

If every application invents its own interpretation of addresses, actions, and messages, will the Web preserve the simplicity that allowed it to scale?

The network can carry the requests. HTTP can frame the conversation.

What principles should shape the application built on top?

## Historical Notes

The historical framing in this chapter draws on CERN's [short history of the Web](https://home.cern/science/computing/the-birth-of-the-web/short-history-web/), Tim Berners-Lee's [personal account](https://www.w3.org/People/Berners-Lee/ShortHistory.html), and the W3C's [history](https://www.w3.org/about/history/). The protocol discussion is grounded in [RFC 1945](https://www.rfc-editor.org/rfc/rfc1945), which documented common HTTP/1.0 usage, and the modern semantics consolidated in [RFC 9110](https://www.rfc-editor.org/rfc/rfc9110).


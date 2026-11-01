# From résumé to live portfolio

Version: 0.2 — rehearsal draft, not yet validated end to end.

Use these prompts in order in the same chat. Replace text in square brackets. You do not need to write code or Git commands.

Participant setup is a project folder, résumé content, and a connected GitHub account. Local Git installation, identity configuration, and terminal use are not workshop prerequisites. Publishing through the connected tools still needs an end-to-end rehearsal before this guide is ready for participants.

## Before starting

1. Open a fresh chat with a separate, empty project folder for your portfolio. Keep the workshop planning folder separate so its facilitator instructions do not influence the test.
2. Have your résumé text ready. Copy and paste it from the document, or optionally convert a PDF at https://cloudconvert.com/pdf-to-md and download the Markdown. Review names, dates, links, and column order. Use a sample résumé if preferred.
3. Have a GitHub account ready. Connect and authenticate the GitHub plugin before the publishing step. Repository access and any additional authentication will be checked during the rehearsal; connecting the plugin alone is not yet a verified complete setup.
4. Optionally choose a portfolio screenshot or live reference. You can choose later.

Do not paste passwords or access tokens into the chat. Complete sign-in through the service's authentication interface.

## Step 1 — Prepare the content

Paste this prompt and supply your résumé text or Markdown:

```text
Help me turn my résumé into a personal portfolio website, then publish it to GitHub Pages. Handle the technical work; let me steer in plain language. Use this project's folder for the work.

Do not require local Git setup or Git commands. Save drafts locally; use connected GitHub tools for remote commits when I request publication. If a required publishing capability is unavailable, explain the blocker plainly rather than making Git installation or configuration a prerequisite.

Default to a broad professional audience. Help visitors understand my work, explore selected highlights, and contact me through links I approve. Adapt the sections to my résumé and profession. Audience and tone preferences are optional; don't require a questionnaire before starting.

First, read my résumé and draft concise website content in CONTENT.md for my review. Do not build the website yet. Do not invent achievements, metrics, publications, affiliations, testimonials, or project details. Flag important gaps and extraction uncertainties briefly. For a long CV, propose a small selection of highlights.

List the contact details and personal information you propose to publish so I can approve or remove them. Omit home address, personal phone number, and private references by default. Keep original résumé files and unapproved source material out of commits and deployment. Do not offer a public résumé download unless I request one.

End with the draft and one bundled review request covering accuracy and what may become public.

My résumé:
[Paste text here, or identify the supplied Markdown file.]

Optional preference:
[Audience, tone, or anything to omit. Delete this line if you have no preference.]
```

Review the draft. Ask for corrections in ordinary language, then explicitly approve the content and public links before proceeding.

## Step 2 — Choose a design and build

```text
The content and public links are approved with these changes: [describe corrections, or say "none"]. Update CONTENT.md accordingly.

My visual reference is: [attach a screenshot, paste a URL, or say "suggest directions"].

If I supplied a reference, briefly identify the typography, colors, composition, and interactions you will borrow, then build an original portfolio using my approved content. If you cannot inspect the reference, tell me and ask for a screenshot. If I haven't supplied a reference, suggest three distinct, playful design directions suited to my actual content and wait for my choice before building.

Create a responsive static website suitable for GitHub Pages. Prefer HTML, CSS, and minimal JavaScript unless the approved design needs something more. Use relative asset paths that work under a repository subpath. Keep all public content consistent with CONTENT.md. Do not deploy that Markdown file or private source documents as website assets.

Avoid generic filler, invented project imagery, and unnecessary dependencies. Use images I provide or appropriately reusable assets with required credits. Do not install optional design skills without first explaining their setup and expected benefit.

Keep short project instructions in AGENTS.md and record the selected direction and references in DESIGN.md so I can continue in another chat.

Record that local Git setup is not required and GitHub publication uses the connected tools. Do not add an automatic local-commit requirement to the project instructions.

Open a working preview using the available preview tools. Check desktop and mobile layout, navigation, links, keyboard access, readable contrast, and reduced motion when relevant. Fix issues you find. Tell me what you checked and anything you couldn't verify. Stop at the preview; do not publish yet.
```

If asked to choose a direction, reply with your choice. Refine the preview with requests such as:

```text
Make the research section more prominent and the colors warmer. Keep the approved content and other design choices. Update the preview and recheck the affected layout. Do not publish yet.
```

## Step 3 — Publish

Use this only when you want the approved website to become public:

```text
Publish this approved portfolio to GitHub Pages.

Destination: [existing repository URL, or "a new repository named portfolio under my GitHub account"].

Inspect the available GitHub tools and authentication first. Use connected tools to handle remote commits, file uploads, and Pages configuration where supported. Do not require local Git installation, identity configuration, or terminal commands. If a capability is missing, explain the blocker and whether a small browser step can resolve it. Guide me through authentication or permission steps only when needed. Don't claim the GitHub plugin supports an operation without checking.

For a new repository, use a public repository for this public portfolio. For an existing repository, inspect it first and preserve unrelated files and settings; don't change its visibility or overwrite an existing site without checking with me.

Publish only intended website assets. Keep private résumé sources and internal project documents out of the deployed site, and exclude unapproved personal source files from commits. Configure a repeatable deployment so future published changes update this same site. Document the exact repository, publishing branch, publishing method, public asset location, and verification steps in AGENTS.md.

Check deployment status and open the live website. Verify the current content, navigation, and assets at its actual GitHub Pages URL. Give me the live link and a brief result summary. If deployment is pending or blocked, say so rather than reporting success.
```

## Step 4 — Test an update

Use the same prompt for future updates. In a new chat, open the portfolio project folder first.

```text
Update my existing portfolio and publish the change.

Repository: [repository URL].
Requested changes: [describe a real content or design change, or identify an updated résumé file].

Read the project's AGENTS.md, CONTENT.md, and DESIGN.md and inspect the current repository before editing. Apply the requested changes, keep editable content and the website consistent, and preserve the approved design unless I request a redesign. If I supplied an updated résumé, compare it with existing approved content; ask about ambiguous changes or newly introduced personal contact details before publishing them.

Check the affected layout and behavior, use the connected GitHub tools to commit only relevant changes remotely, publish using the existing method, and verify that the live site shows the update. Do not require local Git setup or terminal commands. Give me the live link and a brief summary. Report any blockers or checks you could not complete.
```

## Step 5 — Bring feedback back to the planning chat

Record the version tested and what happened in TEST-LOG.md in the planning project. Include screenshots or relevant responses when useful. Do not include credentials or private résumé content in the feedback log.

Evaluate:
- Could you follow the steps without writing code or commands?
- Did the content remain accurate and suit your profession?
- Did the design feel personal and reflect the reference?
- Were the preview and live site consistent?
- How many manual actions, approvals, and unexpected questions were needed?
- Did the update reach the live site without changing unrelated content or design?

Revise the walkthrough in the planning chat, then test the revised version in a fresh project folder. Keep the usable portfolio project intact.

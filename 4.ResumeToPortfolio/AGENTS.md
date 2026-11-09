# Working instructions

## Purpose
Build a usable personal portfolio from Rasool's own résumé, then use the tested workflow as the basis for a hands-on workshop. Read BRIEF.md and DESIGN.md before implementation.

## Collaboration
- The user steers content, design, and publishing decisions in plain language. Handle technical implementation and routine verification.
- Make small, reviewable changes. Ask only about decisions that materially affect the result or require missing facts.
- Keep confirmed decisions distinct from proposals. Update these documents when decisions change.
- Do not install extra tools or introduce a framework merely because a reference uses one. Prefer the simplest approach that supports the chosen design.

## Content
- Treat the supplied résumé as evidence, not ready-made website copy. Draft concise website content for review before building.
- Do not invent achievements, numbers, publications, affiliations, testimonials, or project details. Ask when important information is missing.
- Confirm which contact details and résumé material should be public. Keep the original résumé and unapproved personal source material out of commits and deployment by default.
- Adapt sections to the person's work and audience; do not force a software-developer portfolio structure.
- The résumé supplies facts, not a mandatory website outline. Select/merge/rename/omit sections without a new intake questionnaire. Do not require Projects or additional content; omit unsupported categories and unnecessary job-application details.
- Include a clearly fictional sample résumé for participants without their own. Use it only on explicit selection; sample-based sites must remain visibly labeled as fictional demos and never mix sample facts with a real participant's identity.

## Planning checkpoints
- In this planning repository, commit relevant documentation after each meaningful, reviewed change using a concise Conventional Commit. Inspect the repository and staged diff first; stage explicit paths only and leave unrelated work and private résumé sources out.
- Local commits do not authorize pushes or publication.
- This checkpoint rule is for the facilitator's planning work, not a prerequisite to copy into participant projects.

## Design and delivery
- Use approved references as inspiration for an original design. Record references and the specific qualities to borrow in DESIGN.md.
- Check desktop and mobile layouts, navigation, links, keyboard access, readable contrast, and reduced-motion behavior when animation is present.
- For optional publication, use the account site at username.github.io. Verify relative asset paths locally and on the live site.
- Building a preview does not itself authorize publishing. When the user requests publication or an update-and-publish, handle the necessary relevant commits and GitHub operations within that scope.
- Check deployment status and the live result before reporting publication as complete. Explain authentication or permission steps plainly.
- For later updates, inspect the current repository first, preserve approved design unless a redesign is requested, and keep editable content consistent with the site.

## Current workshop workflow

- Use a fresh local folder with a Markdown or plain-text résumé and optional screenshot, URL, or description. Use a Markdown résumé for the main path, with a plain-text fallback. Let the design conversation continue until there is enough direction for a proposal.
- Generate readable HTML and CSS, plus a classic script only when needed, inside portfolio/. Keep the private inputs outside that folder. Verify the site by opening index.html directly.
- Keep Git and GitHub optional. For participants who want a public site, document the manual GitHub Desktop and Pages path. Use username.github.io with the public site files at the repository root, and preserve any existing site unless its owner approves changes.
- Start at START-HERE.md. Keep publishing setup in PUBLISH.md and include the fictional sample. Link illustrated vendor instructions and give numbered actions, expected results, and recovery steps.
- Keep the participant guides and fictional sample résumé together at the workshop root.
- Record rehearsal evidence and complete RELEASE-CHECKLIST.md before sharing the workshop guide with attendees.

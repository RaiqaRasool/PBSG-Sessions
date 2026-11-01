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

## Planning checkpoints
- In this planning repository, commit relevant documentation after each meaningful, reviewed change using a concise Conventional Commit. Inspect the repository and staged diff first; stage explicit paths only and leave unrelated work and private résumé sources out.
- Local commits do not authorize pushes or publication.
- This checkpoint rule is for the facilitator's planning work, not a prerequisite to copy into participant projects.

## Design and delivery
- Use approved references as inspiration for an original design. Record references and the specific qualities to borrow in DESIGN.md.
- Check desktop and mobile layouts, navigation, links, keyboard access, readable contrast, and reduced-motion behavior when animation is present.
- GitHub Pages is the intended hosting target. Verify asset paths work under a repository subpath.
- Building a preview does not itself authorize publishing. When the user requests publication or an update-and-publish, handle the necessary relevant commits and GitHub operations within that scope.
- Check deployment status and the live result before reporting publication as complete. Explain authentication or permission steps plainly.
- For later updates, inspect the current repository first, preserve approved design unless a redesign is requested, and keep editable content consistent with the site.

## Workshop evidence
- Record actual setup requirements and problems encountered during the practice run in BRIEF.md.
- Do not promise authentication-only publishing until repository setup, Pages configuration, and a subsequent update have been tested.
- Prefer explicit update prompts over résumé watchers or automatic regeneration hooks.
- Write participant instructions assuming no knowledge of GitHub, Pages, project folders, or agent files. Start with the workshop link, give numbered clicks and expected results, and include recovery steps.
- Maintain participant-kit/ separately from facilitator instructions; package only participant files into portfolio-starter.zip. Never include private résumés.
- Supply curated original website links as easy design choices and accept any public reference URL. AI inspects the visual design using available browser tools or existing Firecrawl capabilities; use a screenshot fallback when needed. No mandatory reference research or additional participant tool setup.
- Store the repository write destination, verified live website URL, branch, folder, and publishing method in participant AGENTS.md. Update prompts must use that record without requesting URLs again.
- Complete RELEASE-CHECKLIST.md before calling the kit ready for attendees. Local commits do not publish download links.
- Participants should not need to install Git, configure a Git identity, initialize repositories, or run terminal commands. Use connected GitHub tools for remote commits and publishing where supported. Resolve missing capabilities during rehearsal rather than adding Git setup to the participant instructions.

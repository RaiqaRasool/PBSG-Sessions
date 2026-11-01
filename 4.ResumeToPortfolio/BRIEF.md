# Résumé to portfolio practice run

## Confirmed goals
- Use Rasool's own résumé to produce a portfolio he can actually use.
- Complete a full practice run: content preparation, design selection, preview, GitHub Pages publication, and one subsequent update.
- Turn the successful process into a setup guide and reusable prompts for a hands-on workshop.
- Workshop participants include physicists, technical professionals, and business professionals. AI should handle technical work while participants steer and authenticate or approve actions as needed.
- Offer varied, playful design directions rather than a uniformly formal résumé-on-a-page result.
- Support repeatable content and design updates followed by publication through explicit prompts.
- Use a shared default: a broad professional audience, selected work highlights, and approved contact links. Audience and tone customization are optional, not required intake questions.
- Test the participant-facing instructions in a separate chat and iterate here using observed results.
- Participants should not need local Git installation, identity configuration, or terminal commands. AI handles remote commits through connected GitHub tools; publishing capability gaps must be resolved in rehearsal.

- Assume no prior knowledge of GitHub, Pages, project folders, or agent instructions. Supply numbered clicks from the workshop link, expected results, a starter download, and recovery steps.
- Provide curated original website links and accept participant-supplied URLs. AI handles visual reference analysis. Include Firecrawl plugin connection in pre-session setup, subject to testing its free access and exposed branding/screenshot capabilities. Browser/screenshot fallback if unavailable.
- Save repository and live website URLs and publishing settings in participant AGENTS.md; updates should not need those details from the user again.

- Default to a focused one-page site with résumé-derived sections and no required section questionnaire. References supply personality rather than content volume, achievements, or page count. Optional section changes remain available.

## Proposed approach — not yet validated
- Use a no-build static HTML/CSS/JavaScript site under /docs, published from main + /docs, as the fixed rehearsal path.
- Use GitHub Pages as the hosting target.
- Use the available GitHub integration where sufficient; test repository creation and Pages configuration separately from file updates.
- CloudConvert PDF-to-Markdown is an optional extraction route; copying résumé text is an alternative. No MarkItDown MCP setup is required for the planned workshop.
- Evaluate design skills only if they improve this practice run enough to justify their setup and run time.
- Rea is optional exploration, not a workshop prerequisite.

## Inputs still needed
- Résumé content review (RaiqaRasool_CV_BNL.md is present locally and remains uncommitted).
- Optional audience or visitor-action preference; otherwise use the shared default.
- Public contact details, links, and any information to omit.
- Visual preferences and reference examples; these can be chosen after reviewing the résumé.
- GitHub repository/account destination before publication.

## Practice-run completion criteria
- User has reviewed the public website content and chosen the design direction.
- Website works at desktop and mobile widths with working navigation and links.
- Site is published to GitHub Pages and verified live.
- One requested update is committed, published, and verified live.
- Actual setup steps, integration limitations, and reusable build/publish/update prompts are documented.

## Rehearsal log
No conversion, implementation, GitHub setup, or deployment has been tested yet.

Participant instructions: participant-kit/START-HERE.md (v0.6, untested), linked from README.md and WORKSHOP.md. Record trials in TEST-LOG.md and complete RELEASE-CHECKLIST.md before release.

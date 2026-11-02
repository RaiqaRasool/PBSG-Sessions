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

- Assume no prior knowledge of GitHub, Pages, project folders, or agent instructions. Start directly at START-HERE with the download, then a separate setup guide with existing illustrated/video resources, expected results, and recovery steps.
- Provide eight prepared local design/personality briefs with optional original-site exploration. Participants select a name or number; no Firecrawl setup or reference-site access is required. A separate optional guide covers preparing a custom URL with screenshot evidence or Firecrawl.
- Save repository and live website URLs and publishing settings in participant AGENTS.md; updates should not need those details from the user again.

- Default to a focused one-page site with résumé-derived sections and no required section questionnaire. References supply personality rather than content volume, achievements, or page count. Optional section changes remain available.

- Prepared briefs include observed cues, extracted font evidence, interpreted personality, proposed implementation values, and system-font fallbacks. They are self-contained adaptations, not completed templates or exact replicas; screenshots and original font files are not bundled.

- Use the résumé as factual evidence, not a mandatory website outline. AI selects/combines/renames/omits sections without asking for extra material. Projects are optional; contributions can remain within Experience.
- Include SAMPLE-RESUME.md for people without a résumé. All sample-based sites retain a visible fictional-demo label and no fake contact actions.

- Choose the personality after the factual draft, then revise copy and approve the content/design plan before building. Require skimmable writing, 3–5 visible design cues, 2–3 personality traits, and a comparison before handoff.
- Use connected GitHub MCP for remote operations; unsupported creation/settings are participant clicks, not browser automation or CLI fallback. Check app installation/repository selection separately from user permissions.
- Preview via available native tools or direct local index.html. No required Playwright MCP, server, or Sites publication; Sites remains optional.
- Later updates compare edited MY-RESUME.md with approved copy and current remote work, then require content approval, local preview, and explicit publication approval. Report upload, deployment, and live verification separately.

## Proposed approach — not yet validated
- For a new website-only account site, use readable no-build HTML/CSS/JavaScript in local site/, upload only that folder's contents to the root of username.github.io, and publish main + /(root). Preserve an existing confirmed /docs setup rather than migrating silently.
- Use GitHub Pages as the hosting target.
- Use the available GitHub integration where sufficient; test repository creation and Pages configuration separately from file updates.
- Main real-résumé path: CloudConvert PDF-to-Markdown (or existing Markdown), rename MY-RESUME.md, place beside AGENTS.md. Sample is a clearly marked backup after the real-résumé instructions. No MarkItDown MCP setup.
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
First rehearsal completed according to the facilitator's THINGSCANBEIMPROVED.md notes. User-reported issues: confusing setup order, missing app repository-write access despite user admin/push metadata, unsupported repository creation and Pages configuration, weak initial personality/copy, unnecessary /docs publishing, and separate network permission for live verification. The planning chat did not independently inspect that portfolio or deployment. Timings, screenshots, exact site files, and a verified subsequent update are not supplied here.

Version 0.9 incorporates the decisions in REVIEW-DECISIONS.md. Retest from a fresh extraction without replacing the existing portfolio project. The prior public v0.8 kit was checked by unauthenticated HTTP and matched the local archive; each revised kit must also be pushed and its public ZIP/guide checked against the committed version before a fresh rehearsal.

Participant instructions: participant-kit/START-HERE.md (v0.9, revised; retest pending), linked from README.md and WORKSHOP.md. Record trials in TEST-LOG.md and complete RELEASE-CHECKLIST.md before release.

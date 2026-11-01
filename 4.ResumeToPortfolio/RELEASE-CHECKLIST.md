# Facilitator release checklist

v0.6 is prepared for rehearsal, not validated for workshop release.

## Distribution

- [ ] Review guide, instructions, and curated live reference choices.
- [ ] Rebuild portfolio-starter.zip when participant-kit/ changes. It must contain only my-portfolio/ with the four participant files; no planning instructions or private résumés.
- [ ] Publish reviewed materials to main in RaiqaRasool/PBSG-Sessions through the authorized release process. Local commits alone do not make download links live.
- [ ] Open the workshop URL signed out, download the archive, and check extraction. The folder URL could not be fetched during drafting; public access remains unverified.

## Setup

- [ ] Record the exact supported desktop app version/platform and account requirements. Current OpenAI docs describe Codex in the ChatGPT desktop app; do not mix its UI with an older standalone app.
- [ ] Follow the guide on clean Mac/Windows accounts, or explicitly limit supported platforms.
- [ ] Verify project-creation clicks and add screenshots. Docs establish Projects, Edit project, Add folder, and Make primary; the clean-screen path still needs rehearsal.
- [ ] Verify Firecrawl plugin connection on a free account, actual branding/screenshot outputs, credit usage, and browser/screenshot fallback. Do not assume API features are exposed in the plugin or promise exact font matching.
- [ ] Verify GitHub plugin connection and new-repository access screens. Add screenshots where helpful.
- [ ] Confirm no local Git or terminal use is required for content, preview, publication, or updates.
- [ ] Test available repository-creation and Pages-configuration capabilities. Choose one rehearsed class path, including fixed browser steps if needed, rather than making attendees choose a deployment strategy.

## Result

- [ ] Test Rasool's résumé in a separate project and record results in TEST-LOG.md.
- [ ] Visually inspect the curated original websites on desktop/mobile; check availability, variety, and implementation scope. Test one listed reference and one participant-supplied URL, plus the screenshot fallback.
- [ ] Confirm source résumés stay local and only website assets are deployed from /docs.
- [ ] Verify main + /docs publishing and relative assets at the real repository-subpath URL.
- [ ] Confirm AGENTS.md stores real repository/settings/live URLs and verified status.
- [ ] Test updating from a new chat without user-supplied URLs. It must update the same website using the saved record.
- [ ] Confirm failures produce one useful next step rather than Git setup, duplicate repositories, or false success.
- [ ] Record timing, manual clicks, unexpected questions, and corrections; revise and retest affected steps.

## Sources reviewed

- [OpenAI desktop](https://developers.openai.com/codex/app/), [projects](https://learn.chatgpt.com/docs/projects), [plugins](https://learn.chatgpt.com/docs/plugins).
- [GitHub repository creation](https://docs.github.com/en/repositories/creating-and-managing-repositories/creating-a-new-repository), [Pages settings](https://docs.github.com/en/pages/getting-started-with-github-pages/configuring-a-publishing-source-for-your-github-pages-site).

Documentation review is complete. UI rehearsal, public-link access, conversion quality, generated-site quality, authentication, and deployment remain unverified.

Local checks: archive integrity, its exact four-file allowlist, equality with source files, relative document links, and SVG XML passed. The browser screenshot tool timed out, so visual inspection of the schematic cards is still required.

## Firecrawl smoke check — November 1, 2026

The plugin became available during drafting. A live single-page request to https://cassidoo.co/ with branding and screenshot formats returned HTTP 200, a screenshot URL, font family iA Writer Mono, heading/body sizes, colors, and spacing. Metadata reported one credit. Overall branding confidence was approximately 0.46, so inferred personality/audience labels must not be treated as exact facts. The screenshot was returned but not visually reviewed in this check. Free-account onboarding, mobile capture, repeated extraction, font reuse availability, and generated-site fidelity still need rehearsal.

## Reference-menu review — November 1, 2026

Visually inspected desktop opening views in the in-app browser for Seán Halpin (seanhalpin.design redirects to seanhalpin.xyz), Lynn Fisher, Maggie Appleton, Brittany Chiang, Nicky Case, Cassidy Williams, Josh W. Comeau, and Ram Maheshwari. Added Seán and Lynn to broaden the existing list and annotated every reference with observed cues plus proposed résumé adaptations. These are proposed design transfers, not implemented templates. Initial captures sometimes caught entrance transitions; Brittany's settled view was checked separately. Mobile, hover, scroll behavior, and deeper page layouts remain unverified. Rauno Freiberg was also fetched as a candidate but not added; its initial browser capture caught a transition and did not establish the complete layout.

Firecrawl branding for the new candidates was not sufficient alone: inferred audience labels were unreliable and the browser's active theme differed from some extracted color-scheme metadata. On reference selection, inspect screenshot pixels and check the active theme before adopting tokens. A returned screenshot URL alone is not a visual review.

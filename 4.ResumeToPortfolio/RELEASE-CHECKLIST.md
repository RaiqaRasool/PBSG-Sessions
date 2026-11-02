# Facilitator release checklist

v0.9 is prepared for rehearsal, not validated for workshop release.

## Distribution

- [ ] Review guide, instructions, and curated live reference choices.
- [ ] Run `python3 scripts/package-starter.py` after participant-kit/ edits. It packages five participant guides/instructions (including SETUP.md), two instruction pointers (CLAUDE.md and GEMINI.md), one fictional sample résumé, references/README.md, and eight prepared briefs (17 files total), using an explicit allowlist. No private résumé or facilitator files may be included.
- [ ] Publish reviewed materials to main in RaiqaRasool/PBSG-Sessions through the authorized release process. Local commits alone do not make download links live.
- [ ] Open the workshop URL signed out, download the archive, and check extraction. The folder URL could not be fetched during drafting; public access remains unverified.

## Setup

- [ ] Verify linked external quickstart/project/plugin resources against the chosen desktop version; links provide vendor illustrations/video rather than an invented screenshot sequence. Record the exact supported desktop app version/platform and account requirements. Current OpenAI docs describe Codex in the ChatGPT desktop app; do not mix its UI with an older standalone app.
- [ ] Follow the guide on clean Mac/Windows accounts, or explicitly limit supported platforms.
- [ ] Verify project-creation clicks and add screenshots. Docs establish Projects, Edit project, Add folder, and Make primary; the clean-screen path still needs rehearsal.
- [ ] Verify the main journey works without Firecrawl or source-site access. Separately test the optional custom-reference guide using a screenshot and, if desired, connected Firecrawl. Do not assume API features are exposed in the plugin or promise exact font matching.
- [ ] Verify GitHub plugin connection and new-repository access screens. Add screenshots where helpful.
- [ ] Confirm no local Git or terminal use is required for content, preview, publication, or updates.
- [ ] Test available repository-creation and Pages-configuration capabilities. Choose one rehearsed class path, including fixed browser steps if needed, rather than making attendees choose a deployment strategy.

## Result

- [ ] Test the fictional sample path without supplying any extra content. Confirm no invented Projects, no résumé-only references/objective sections, a visible demo label, and no fake contact action. Also test the real-résumé path without sample facts leaking into it.
- [ ] Test Rasool's résumé in a separate project and record results in TEST-LOG.md.
- [ ] Review all eight prepared briefs and confirm observed/extracted evidence, personality interpretation, and proposed tokens/phone behavior are distinguished. Test one prepared build without reference-site access and one optional custom brief. Evaluate each prepared option before workshop release.
- [ ] Confirm only local site/ public assets reach remote root; source résumé, internal agent/content/design documents, and kit files stay local. Preserve existing confirmed mixed-repository /docs mappings.
- [ ] Verify the new website-only username.github.io destination, main + /(root), and relative assets. Check existing-site protection and the Add README/empty-repository initialization path.
- [ ] Confirm AGENTS.md stores real repository/settings/live URLs and verified status.
- [ ] Test edited MY-RESUME.md → proposed differences → content approval → local preview → publication approval in a new chat, with no user-supplied URLs. Preserve website-only edits and the same saved destination.
- [ ] Confirm failures produce one useful next step rather than Git setup, duplicate repositories, or false success.
- [ ] Record timing, manual clicks, unexpected questions, and corrections; revise and retest affected steps.

## Sources reviewed

- [OpenAI desktop](https://developers.openai.com/codex/app/), [projects](https://learn.chatgpt.com/docs/projects), [plugins](https://learn.chatgpt.com/docs/plugins).
- [GitHub repository creation](https://docs.github.com/en/repositories/creating-and-managing-repositories/creating-a-new-repository), [Pages settings](https://docs.github.com/en/pages/getting-started-with-github-pages/configuring-a-publishing-source-for-your-github-pages-site).

Documentation review and the first user-reported rehearsal are recorded. The revised v0.9 setup, conversion, personality-copy review, native/file preview, app access, root publication, and staged updates require retesting. Do not mark the workshop ready based only on documentation checks.

Local checks: archive integrity, the explicit 17-file participant allowlist, equality with source files, and relative document links passed. The obsolete schematic SVG was removed in favor of the live reference list.

## Firecrawl smoke check — November 1, 2026

The plugin became available during drafting. A live single-page request to https://cassidoo.co/ with branding and screenshot formats returned HTTP 200, a screenshot URL, font family iA Writer Mono, heading/body sizes, colors, and spacing. Metadata reported one credit. Overall branding confidence was approximately 0.46, so inferred personality/audience labels must not be treated as exact facts. The screenshot was returned but not visually reviewed in this check. Free-account onboarding, mobile capture, repeated extraction, font reuse availability, and generated-site fidelity still need rehearsal.

## Reference-menu review — November 1, 2026

Visually inspected desktop opening views in the in-app browser for Seán Halpin (seanhalpin.design redirects to seanhalpin.xyz), Lynn Fisher, Maggie Appleton, Brittany Chiang, Nicky Case, Cassidy Williams, Josh W. Comeau, and Ram Maheshwari. Added Seán and Lynn to broaden the existing list and annotated every reference with observed cues plus proposed résumé adaptations. These are proposed design transfers, not implemented templates. Initial captures sometimes caught entrance transitions; Brittany's settled view was checked separately. Mobile, hover, scroll behavior, and deeper page layouts remain unverified. Rauno Freiberg was also fetched as a candidate but not added; its initial browser capture caught a transition and did not establish the complete layout.

Firecrawl branding for the new candidates was not sufficient alone: inferred audience labels were unreliable and the browser's active theme differed from some extracted color-scheme metadata. On reference selection, inspect screenshot pixels and check the active theme before adopting tokens. A returned screenshot URL alone is not a visual review.

## Prepared-reference change — November 1, 2026

Eight local briefs now supply observed desktop cues, sourced font information, interpreted personality, proposed build tokens/layout/responsive rules, and system-font fallbacks. Original screenshots and font files are not bundled, and these are not exact replicas. Existing browser visual observations are reused. Additional single-page branding extractions were retrieved for Brittany, Maggie, Nicky, Josh, and Ram; some raw font-stack and color metadata conflicted with rendered views, so those conflicts are noted rather than treated as exact values. Prepared builds, actual font fallbacks, mobile usability, and the optional screenshot-only workflow still require rehearsal. Firecrawl is no longer part of participant prerequisites.

## v0.9 retest checks from facilitator feedback

- [ ] Download starts directly from START-HERE; setup precedes the first folder chat.
- [ ] Own-resume path uses MY-RESUME.md; sample appears afterward and never leaks into real content.
- [ ] Copy reflects the chosen personality before approval; first preview meets the recorded visual cues and is not a generic résumé dump.
- [ ] No mandatory Sites, Playwright MCP, server, browser-control setup, or minified output. A simple mobile menu remains visible; a necessary toggle is accessible.
- [ ] Capability limitations are explained before manual handoffs. App installation/repository selection and actual write success are distinct from user permissions.
- [ ] Repository creation/Pages fallback links work, remote root contains only public assets, and automatic branch publication works.
- [ ] Upload, deployment, and live-content checks are reported separately, including approval limits and propagation delay.

Sources for review: [GitHub app installation access](https://docs.github.com/en/apps/using-github-apps/reviewing-and-modifying-installed-github-apps), [account creation](https://docs.github.com/en/account-and-profile/how-tos/account-management/creating-an-account-on-github), [Pages source configuration](https://docs.github.com/en/pages/getting-started-with-github-pages/configuring-a-publishing-source-for-your-github-pages-site), and the OpenAI links in SETUP.md. See REVIEW-DECISIONS.md for accepted/adjusted suggestions. No external portfolio was deployed by this planning revision.

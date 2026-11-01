# Portfolio assistant instructions

## Beginner experience

- Handle implementation in plain language. Give one next action at a time when human input is needed.
- Do not require local Git installation, identity configuration, terminal commands, or manual MCP server setup. Only GitHub connection is part of the main setup. Firecrawl is optional for new custom references, as described in OPTIONAL-REFERENCE.md. Use connected GitHub tools for remote commits; no automatic local-commit requirement.
- Read DESIGN-OPTIONS.md. Resolve the participant's selected name, number, or listed URL to its prepared local brief. Read references/README.md and only that brief. Do not refetch a prepared source or require Firecrawl. A new unlisted URL uses OPTIONAL-REFERENCE.md. No design questionnaire or mandatory reference research. If asked to choose, recommend a listed reference suited to the content.
- Default to a broad professional audience, selected work highlights, and approved contact links. Adapt sections to actual work and profession.
- Default to one page with a short introduction, selected work/research when supported, relevant experience/education, and approved contact links. Omit empty sections. Do not inherit the reference's page count or require a section questionnaire; accept optional add/remove/rename requests.
- Save approved text in CONTENT.md. Save the selected source URL, local brief path, observed cues, interpreted personality, actual fonts/fallbacks, and adaptations in DESIGN.md. Prepared briefs are self-contained workshop adaptations; use their proposed implementation values without source-site access. Do not promise exact reproduction.
- For a participant-requested custom reference, follow OPTIONAL-REFERENCE.md. Use an available design-extraction skill when appropriate, inspect actual visual evidence, and distinguish observed facts from interpretation and proposals. Save references/custom.md for later offline use. Do not require paid access or manual MCP setup. A missing optional tool must not block prepared options.

## Accuracy and privacy

- Use supported résumé facts. Do not invent achievements, metrics, clients, publications, affiliations, testimonials, or project details. Flag extraction uncertainties.
- Bundle content accuracy and public-contact review before building. Omit home address, personal phone number, and private references by default. A public résumé download requires an explicit request.
- Keep original résumés and unapproved sources local and out of uploads/commits. Website publication does not approve publishing the raw résumé.

## Build and preview

- Use static HTML/CSS/minimal JavaScript without a build step. Public assets belong only in docs/: index.html, styles.css, optional script.js, assets/, and .nojekyll.
- Keep agent files, editable content, guides, and private source documents outside docs/. Only approved nonsensitive project instructions/content may be committed at the repository root for continuation.
- Use relative paths that work at a repository subpath. No server-only features, client routing, or contact forms that pretend to send messages without a service.
- Create an original design informed by the selected local brief and its personality, preserving the participant's own voice and facts. Use provided or appropriately reusable assets with credits. Do not fabricate scientific figures or project evidence.
- Open a preview with available tools. Check desktop/mobile, navigation, links, keyboard access, contrast, and reduced motion. Fix issues and report unverified checks. Preview requests do not authorize publication.

## First publication

1. On an explicit publish request, inspect connected GitHub capabilities and identity. Prefer the participant's personal account; do not guess the owner.
2. Use a new repository named my-portfolio unless specified otherwise. If it exists, confirm the destination or suggest my-portfolio-workshop; do not overwrite an existing site.
3. Create it with authorized connected tools/browser when possible. Otherwise give the creation link and START-HERE.md step 8A instructions one action at a time. Check access before uploading. Never ask for tokens in chat.
4. Inspect the destination, preserve unrelated work, and make relevant remote commits through connected tools. Place public assets in docs/, including docs/.nojekyll. Batch a complete site update into one commit when tools permit.
5. Configure Pages to deploy from main and /docs using available authorized tools/browser. Otherwise provide the exact Settings → Pages link and step 8B clicks. Do not fall back to participant CLI setup.
6. Fill in the publishing record below as real values become known. The repository URL is where files are written; the Pages URL is where the result is viewed. They are not interchangeable.
7. Check deployment status and open the real live URL to verify this version's content, links, and assets. Report pending/failed states honestly; do not mark an expected URL as verified.
8. Save the record locally in this AGENTS.md. If approved instructions are uploaded, keep them at repository root outside docs/ without private source information. Give a clickable live link.

## Later updates

- Read the publishing record first. Do not request saved URLs again. Inspect remote files before editing; preserve remote work and sync relevant changes locally.
- Keep editable content consistent with the website and preserve approved design unless asked to redesign. Ask about ambiguous new résumé facts or newly introduced personal contact details.
- On an update-and-publish request, commit relevant changes remotely and publish using the saved destination. Never silently create a replacement repository or change publishing settings because an update fails.
- Verify deployment and the saved live URL, then update the last-verified record.
- If the record is incomplete, recover from existing remote instructions or the connected account where possible. Confirm ambiguous destinations before writing. Ask for an address only if recovery fails.

## Publishing record — AI maintains this; participant does not fill it in

- GitHub account/owner: not set
- Repository name: not set
- Repository URL (write destination): not set
- Branch: main
- Public website folder: /docs
- Publishing method: GitHub Pages, deploy from branch
- Pages settings URL: not set
- Live website URL (verification destination): not yet known
- Deployment status: not configured
- Last verified live version/commit and date: none

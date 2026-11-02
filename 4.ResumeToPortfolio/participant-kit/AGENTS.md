# Portfolio assistant instructions

## Beginner workflow and authority

- Handle technical work in plain language. Before a missing-capability handoff, inspect capabilities, explain the exact limitation, then give one concrete next action with a direct link.
- No participant Git installation, identity setup, terminal commands, manual MCP setup, Firecrawl, Playwright MCP, or browser-control permission is required. Use connected GitHub tools for remote reads/commits/status. Do not silently switch to browser automation or an authenticated CLI when a tool is missing or denied.
- Read START-HERE.md and follow its phase boundaries: factual draft → personality-shaped copy/plan approval → build/preview → publication; updates use proposed diff → content approval → local preview → publication approval. Drafting or preview approval alone never authorizes uploading/publishing.
- Initial real résumé input is MY-RESUME.md. Do not require file-mention autocomplete or ask participants to repeat source content in chat. If the file is absent or unreadable, give a concrete file-placement/conversion correction. Use SAMPLE-RESUME.md only on explicit selection.
- Resolve a name/number/listed URL via DESIGN-OPTIONS.md. Read references/README.md and only the chosen local brief. No reference-site fetch is required. Custom references use OPTIONAL-REFERENCE.md.
- Keep durable content, design, source choice, approval state, and publishing records local so a new project chat can continue.

## Content: factual, selective, skimmable, and personal

- The résumé is evidence, not the website outline. Select, combine, rename, shorten, or omit headings to serve a broad professional reader. No extra intake questionnaire or request for projects, photos, hobbies, testimonials, or additional achievements to fill a layout.
- No mandatory Projects section. Experience contributions may stay in Experience or become Selected Contributions without pretending they are independent projects. Omit unsupported/empty categories, application objectives, references statements, repeated skills, and irrelevant administrative details. Summarize long lists; there is no minimum section count.
- Draft a short meaningful headline, a one- or two-sentence introduction, concise selected highlights where useful, and compact experience/education. Prefer specific supported contributions over generic adjectives. Usually keep an experience entry to one or two useful bullets and a highlight to a short summary, not copied résumé paragraphs. Length limits are guidance, not permission to distort facts.
- After personality selection, revise CONTENT.md before building: headline, section labels, rhythm, summaries, and calls to action should reflect the brief's interpreted personality while preserving the participant's voice and level of formality. Show a few before/after examples for review. Do not copy the original owner's catchphrases, identity, achievements, or writing.
- Do not invent metrics, affiliations, publications, clients, testimonials, case-study detail, opinions, or project evidence. Flag source ambiguities. Prefer omission to interviewing for missing material.
- Review the final website copy, structure, and public details together before implementation. Default to omitting home address, personal phone, private references, and résumé downloads. Keep source résumés out of all uploads/commits.
- Record whether input is MY-RESUME.md or the fictional sample in CONTENT.md. Sample-based previews/published sites must retain a visible "Fictional workshop demo" label, with no fake contact actions or mixing sample facts into a real identity. Switching to a real résumé requires a new factual/public-copy review.

## Design and readable implementation

- In DESIGN.md record the chosen local brief/source, 3–5 defining visual cues, 2–3 interpreted personality traits, actual font/fallback choice, signature detail, and intended treatment of the participant's content. Prepared briefs distinguish observations from interpretations and proposed implementation values; do not promise exact replicas.
- Apply the personality to both copy and visual hierarchy. If the first build looks generic, correct the major cue mismatches before handoff, not just the accent color.
- Keep static HTML, CSS, and small classic JavaScript files, with no build step, required server, fetch-based local content loading, or module imports that break file:// previews. No fake sending forms or server-only features.
- For new projects, keep public files under local site/: index.html, styles.css, optional script.js, assets/, and .nojekyll. This folder is the upload allowlist, not necessarily the remote folder name. Preserve an existing confirmed local layout until an explicit migration is agreed.
- Write normal formatted files with indentation, meaningful names, separated styles/scripts, and short useful section comments. Do not minify or place an entire page/style sheet on one line.
- Use readable phone layouts. Keep a short visible/wrapping anchor menu if it fits. When links genuinely need a hamburger/toggle, include a labeled button, aria-expanded/aria-controls, keyboard operation, visible focus, appropriate close behavior, and a usable no-JavaScript fallback. Do not hide essential navigation behind hover.
- Images/portraits are optional and must be supplied or appropriately reusable with required attribution. Do not fabricate scientific figures or borrow the reference owner's personal assets.
- Use relative asset paths so the site also works at a project subpath. Honor reduced motion and sufficient text contrast.

## Preview and checks without extra setup

- Prefer an available native/in-app preview. Otherwise provide the absolute local site/index.html link and let the participant open/double-click it in their browser; this static site must not require a server.
- Do not create a hosted Site or move work to Sites merely to get a preview. Sites is an optional separate workflow requiring an explicit choice; GitHub Pages remains the publication target.
- Do not require Playwright MCP/browser installation or user browser automation access. If existing authorized rendering tools are available, use them proportionally; otherwise perform available structural checks and give concise manual desktop/phone instructions. Report which visual checks could not be performed.
- Compare the rendered preview with the recorded visual cues and personality traits. Fix clear mismatches, test navigation/links/keyboard access/phone layout where tools allow, and record the actual checks. Never equate static inspection with a visual comparison.

## GitHub destination and access preflight

- Inspect connected tool capabilities early: identity, repository reads, remote commits, repository creation, Pages configuration, deployment checks. The first rehearsal had commits but no repository-creation or Pages-settings tools. Do not assume that inventory remains the same or promise unsupported operations.
- Default a new personal portfolio to the account's exact lowercased username.github.io repository and https://username.github.io/. Arbitrary names give project URLs, not an arbitrary account-site name. Identify the owner through supported tools, or ask for the username once if ambiguous. Preserve an existing account website/custom domain; confirm before replacement or settings changes.
- Save the destination before upload. If creation is unavailable, provide a prefilled creation URL and START-HERE Step 7 instructions. Prefer Add README to initialize main. An entirely empty repository may require an initialization commit before the full site commit; explain it rather than treating one-commit batching as a hard requirement.
- Authorization as a user, GitHub App installation, selected repositories, and granted app permissions are distinct. A successful read or user admin/push metadata does not establish app write access. Ask the participant to confirm the app installation on the owner account and website repository selection. Record write access as unverified until an authorized write succeeds.
- On 403, inspect available error evidence for installation/repository access, app write permissions, and relevant branch restrictions. Explain the likely issue and one next action; do not repeatedly retry the same write or silently change authentication methods. Never request tokens in chat.

## Publication through connected tools

1. Require explicit approval of the preview and publication request. Inspect remote content and current head before writing; preserve unrelated and intervening changes. Confirm replacement of an existing website. Before enabling root publication on an existing repository, identify any internal/source files that would become website-accessible, explain the needed cleanup, and obtain approval for removals or a different publishing arrangement; do not blindly expose them.
2. New website-only user-site default: main + /(root). Upload only the files inside local site/ to remote root, including index.html and .nojekyll. Never upload MY-RESUME.md, other source résumés, CONTENT.md, AGENTS.md, DESIGN.md, sample sources, reference briefs, guides, or the starter archive. Keep them outside local site/.
3. If a confirmed existing project deliberately uses /docs, retain that mapping and Pages setting. Do not silently migrate root↔/docs, overwrite custom-domain configuration, or create another repository after failure. Root naming and publishing folder are separate choices.
4. Make relevant remote commits via connected GitHub tools. Prefer a complete site commit after initialization. Read back or otherwise verify uploaded public files where tools permit.
5. Configure Pages via a supported tool if present. If absent, give the exact Settings → Pages URL and ask the participant to select Deploy from a branch, main, and /(root) for the new default, then Save. Use the saved folder for an existing confirmed setup. No browser automation or CLI fallback.
6. Branch-based Pages automatically republishes changes in the selected folder after commits. Do not add custom workflow YAML for this no-build site. A future build requirement is a separate decision.
7. Record upload result/commit, deployment status, and live-content verification separately. A successful commit is not a deployment; successful deployment is not proof a network-blocked live fetch saw the new content. Use available deployment tools and read-only network fetching. Explain a needed network approval separately; mark unperformed checks honestly.
8. Give the live URL and mention possible propagation delay (GitHub documents up to 10 minutes). Verify current expected content and referenced assets where access allows. Do not continually redeploy or declare failure just because an old cached page appears immediately.
9. Save the publishing record locally. Internal instructions are not uploaded into the root-published site.

## Later updates: propose → approve → preview → approve publication

- Read local AGENTS.md, CONTENT.md, DESIGN.md and the current chosen source. Inspect the saved remote website where available before proposing edits; preserve website-only edits and intervene if remote changes conflict.
- Compare updated résumé facts against approved website content. Summarize additions/changes/removals and uncertainties, distinguishing factual updates from wording changes. Do not infer deliberate deletion merely because a fact is absent from a shorter résumé. Propose revised concise copy in the saved personality; do not modify approved files or upload until the participant accepts the proposal.
- After content approval, update CONTENT.md and the local site; preview/check using the saved method. Do not upload until preview/publication approval arrives.
- After publication approval, use saved repository/branch/mapping. Check for intervening changes, commit only approved public changes, then report upload/deployment/live-verification states and saved link. Never ask for saved URLs again, silently change destination, or create a replacement repository.
- If the local record is lost, recover the destination through available connected account/repository evidence and confirm ambiguity before writing. Internal records are intentionally not public website assets.

## Local publishing record — AI maintains; participant does not fill in

- Source file/mode: not selected
- GitHub owner/account: not set
- Repository name and URL (write destination): not set
- Local public folder: site/
- Remote publishing folder: / (new website-only default; confirm existing sites)
- Branch: main
- Publishing method: GitHub Pages, deploy from branch
- GitHub App installation/repository selection: not checked
- App write access: unverified (do not infer from reads/user permissions)
- Creation/Pages tool limitations and completed manual steps: not checked
- Pages settings URL: not set
- Live website URL (read/verification destination): not yet known
- Last upload commit/result: none
- Deployment status: not configured
- Live-content verification status and date/version: not verified
- Saved preview method and checks: not selected

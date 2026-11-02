# Rehearsal feedback decisions — v0.9

Input: THINGSCANBEIMPROVED.md, supplied by the facilitator. The original notes are left unchanged. Results described there are user-reported rehearsal evidence, not checks repeated by this planning chat.

| Suggestion | Decision and resulting behavior |
| --- | --- |
| Start directly at START-HERE | Accept. The guide starts with the download; no workshop-page round trip. |
| Separate account/plugin setup with existing illustrated resources | Accept. SETUP.md links official quickstart, project illustrations, plugin video, and GitHub guides. No newly invented screenshot tutorial. Exact installed-app screens still need checking. |
| Explain GitHub account creation alongside connection | Accept. Account creation is an alternative within GitHub connection, not an unrelated prerequisite. |
| Do not ask for a new chat before explaining projects | Accept. Connect first; create the folder project and its first chat afterward. |
| Standardize résumé input | Accept. Convert to Markdown, rename to MY-RESUME.md, and put it in the local project. Existing Markdown can be renamed directly. Copy/paste is reserved for editing this file later, not a competing initial path. |
| Put sample after own résumé | Accept. Sample prompt is clearly a backup and never selected automatically. |
| Use an @ file reference | Adjust. Prompts use the literal filename MY-RESUME.md; participants may select an @ mention if their interface offers it. Correct behavior must not depend on file-mention autocomplete. |
| Require Sites for preview | Do not make this the default. Sites is a separate hosted development/publication workflow. Keep a portable no-build static site with a native preview where available, or a double-clickable local index.html. No required Playwright MCP, new browser installation, or server setup. Sites remains an optional separate experiment. |
| Apply personality to content before building | Accept. First extract a factual website draft; after style selection revise the voice, section labels, hierarchy, and short summaries, then request approval before implementation. |
| Make content skimmable, not copied résumé paragraphs | Accept. Use brief introductions, selected highlights, compact experience entries, and purposeful headings without inventing facts. |
| Compare first build with defining reference cues | Accept. Record 3–5 visual cues and 2–3 personality traits, compare the preview, and fix mismatches before handoff. Report inability to render rather than claim visual QA. |
| Always use a hamburger menu | Adjust. Use visible wrapping links when they fit. Use an accessible toggle only when necessary, with keyboard and no-JavaScript fallbacks. |
| Human-readable HTML/CSS | Accept. No minification; normal indentation, useful class names, separated files, and short section comments. |
| Account main website, not my-portfolio project URL | Accept as default for a first personal site. Exact username.github.io naming matters; arbitrary names do not produce the account root URL. Preserve an existing account site and confirm before replacing it. |
| Publish from repository root for website-only repository | Accept. Local public assets live under site/ and are uploaded to remote root. Local instructions, editable content, résumés, and reference briefs are never uploaded. Mixed/existing repositories may retain a confirmed /docs configuration; never silently migrate them. |
| GitHub MCP rather than browser control | Accept. Use connected tools for reads and remote commits. Participants perform unsupported creation/settings steps via direct links. No silent browser automation or CLI fallback. |
| Verify app installation, not just user permissions | Accept. Explain GitHub App installation on the owner account, repository selection, and granted permissions. Admin/push metadata or successful reads do not prove app write access. Do not claim write verification until an authorized write succeeds. |
| Disclose repository-creation and Pages-settings limitations upfront | Accept. Preflight reports actual available capabilities before the publishing stage, then supplies a concrete next action. |
| Empty-repository commit exception | Accept. Prefer Add README when manually creating; initialize only when necessary and supported. Do not require one commit when the tool needs initialization first. |
| Automatic CI/CD | Accept automatic publication via Pages branch settings. Reject unnecessary custom workflow YAML for this static site. GitHub manages the deployment workflow. |
| Separate deployment and live-site verification | Accept. Report upload, deployment, and live content as separate states. A blocked network fetch is not a failed deployment or proof of live correctness. |
| Review update diff, preview, then publish | Accept. Edit MY-RESUME.md, review proposed differences, approve content, inspect preview, approve publishing. Use saved destination and report propagation delay. |

## Retest priorities

1. Clean setup with no Git/Firecrawl/Playwright installation.
2. Content changes after personality selection are evident and remain factual.
3. User-site repository access works after the GitHub App is granted the repository.
4. Only site/ files reach remote root, with main + /(root) selected in Pages.
5. An edited résumé yields a useful diff and requires preview approval before publication.
6. The same saved live address reflects the approved update after deployment.

## Sources checked

- [OpenAI quickstart](https://learn.chatgpt.com/docs/quickstart), [projects](https://learn.chatgpt.com/docs/projects), [plugins](https://learn.chatgpt.com/docs/plugins).
- [GitHub account creation](https://docs.github.com/en/account-and-profile/how-tos/account-management/creating-an-account-on-github), [installed app access](https://docs.github.com/en/apps/using-github-apps/reviewing-and-modifying-installed-github-apps), [Pages creation](https://docs.github.com/en/pages/getting-started-with-github-pages/creating-a-github-pages-site), [publishing sources](https://docs.github.com/en/pages/getting-started-with-github-pages/configuring-a-publishing-source-for-your-github-pages-site).
- Installed Sites skill reviewed for its separate hosting/source/publication workflow. No Sites instance was created or deployed.

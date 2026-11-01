# Compact and personal — inspired by Cassidy Williams

## Source and evidence

- Original website: [Cassidy Williams](https://cassidoo.co/).
- Review context: November 1, 2026. Desktop opening view inspected in-browser; branding fields retrieved with Firecrawl. Earlier captures are reused where adequate.
- Observed visual cues: Compact reading width, monospace typography, simple navigation, direct personal introduction.
- Extracted font/color evidence: Firecrawl reported iA Writer Mono, 32px h1, 24px h2, and 16px body. Its light background token differed from the browser’s dark active theme. The workshop chooses the dark interpretation explicitly.
- Boundaries: this is a self-contained workshop adaptation, not an exact source-code copy. No original-site screenshots or fonts are bundled. Mobile behavior, deeper pages, and source animation have not been fully audited.

## Personality — editorial interpretation, not measured fact

Approachable, conversational, a little nerdy; preserve the participant’s own voice. Borrow this communication style only where it fits the participant. Keep their voice and approved facts; do not impersonate the source owner.

## Implementation values — proposed workshop choices

Use these values without fetching the original site. Hex colors and dimensions below are explicit workshop choices, not a claim to reproduce source CSS exactly.

| Role | Value |
| --- | --- |
| Page background | `#242424` |
| Primary text | `#F4F4F0` |
| Accent/links | `#F0D977` |
| Panel background | `#303030` |
| Heading stack | `"iA Writer Mono", ui-monospace, monospace` |
| Body stack | `"iA Writer Mono", ui-monospace, monospace` |
| Body size / line height | `18px / 1.65` |
| Reading width | `68ch` |
| Wide layout maximum | `1120px` |
| Spacing scale | `8, 16, 24, 40, 64, 96px` |
| Desktop main heading | `clamp(2.5rem, 6vw, 5.5rem)` |
| Phone page gutter | `20px` |

Named source fonts are reference information, not bundled font assets or permission to download them. Use an already available font if present; otherwise use the stated system fallback. No font download is required. Record the actual stack used in DESIGN.md and mention any substitution once.

## Layout and components

Use a compact name/role header, short anchor navigation, a friendly introduction, and a stacked list of résumé highlights with short descriptions.

Underlined links, small labels, simple spacing. Optional supplied portrait beside the introduction.

## Present the participant's content

Replace the post feed with selected work or research. No blog, newsletter, portrait, or playful anecdote is required.

Keep one page with an introduction and only useful sections supported by the chosen résumé. The résumé is factual input, not a section checklist: combine, rename, or omit headings as appropriate. Projects and contact are optional, and experience contributions need not be turned into projects. Follow AGENTS.md content-curation rules; allow ordinary-language section changes without asking for additional material. Do not inherit the source site's page count.

## Phone, motion, and accessibility — proposed behavior

- Stack columns and panels below 760px; keep navigation visible as wrapping anchor links. Avoid sticky sidebars on phones.
- Keep body text readable without horizontal scrolling. Reduce heading size naturally with the clamp rule.
- Use visible keyboard focus, descriptive links, semantic headings, and sufficient text contrast. Verify these in the built site.
- Default to no motion except short hover/focus feedback; respect prefers-reduced-motion. Never hide content behind hover or animation.
- Images are optional. Use participant-provided or appropriately reusable assets only; no borrowed headshots, logos, project images, or scientific figures.

## Keep the first build focused

Avoid writing jokes or hobbies on the participant’s behalf or adding newsletter functionality.

## Build verification

Compare the generated preview to the observed cues and the chosen personality above. Check desktop and phone layouts, keyboard access, links, actual font fallbacks, and the approved content. Verify the site itself; no reference-site browsing or Firecrawl access is required for this prepared option. Record adaptations in DESIGN.md.

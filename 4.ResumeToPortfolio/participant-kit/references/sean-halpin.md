# Soft and expressive — inspired by Seán Halpin

## Source and evidence

- Original website: [Seán Halpin](https://www.seanhalpin.xyz/).
- Review context: November 1, 2026. Desktop opening view inspected in-browser; branding fields retrieved with Firecrawl. Earlier captures are reused where adequate.
- Observed visual cues: Oversized expressive headings, pastel color fields, rounded work panels, generous space.
- Extracted font/color evidence: Firecrawl reported heading alias acorn and body alias gt; its light palette included #EDE7DE, #A3DCD4, #025A4E, and #364442. The browser opening view showed the soft palette and large introduction. Aliases do not identify reusable font files.
- Boundaries: this is a self-contained workshop adaptation, not an exact source-code copy. No original-site screenshots or fonts are bundled. Mobile behavior, deeper pages, and source animation have not been fully audited.

## Personality — editorial interpretation, not measured fact

Warm, welcoming, quietly playful. Borrow this communication style only where it fits the participant. Keep their voice and approved facts; do not impersonate the source owner.

## Implementation values — proposed workshop choices

Use these values without fetching the original site. Hex colors and dimensions below are explicit workshop choices, not a claim to reproduce source CSS exactly.

| Role | Value |
| --- | --- |
| Page background | `#EDE7DE` |
| Primary text | `#173F38` |
| Accent/links | `#025A4E` |
| Panel background | `#D8EEE9` |
| Heading stack | `Georgia, serif` |
| Body stack | `system-ui, sans-serif` |
| Body size / line height | `18px / 1.65` |
| Reading width | `68ch` |
| Wide layout maximum | `1120px` |
| Spacing scale | `8, 16, 24, 40, 64, 96px` |
| Desktop main heading | `clamp(2.5rem, 6vw, 5.5rem)` |
| Phone page gutter | `20px` |

Named source fonts are reference information, not bundled font assets or permission to download them. Use an already available font if present; otherwise use the stated system fallback. No font download is required. Record the actual stack used in DESIGN.md and mention any substitution once.

## Layout and components

Center a large name-and-role introduction and a short supporting sentence. Follow with two-column rounded highlight panels, then a simple experience list and contact footer.

Rounded 28px panels, generous padding, small geometric star accents made in CSS or SVG.

## Present the participant's content

Use research topics, contributions, or initiatives as panels; use text-first panels when no images are provided.

Keep one page with an introduction and only useful sections supported by the chosen résumé. The résumé is factual input, not a section checklist: combine, rename, or omit headings as appropriate. Projects and contact are optional, and experience contributions need not be turned into projects. Follow AGENTS.md content-curation rules; allow ordinary-language section changes without asking for additional material. Do not inherit the source site's page count.

## Phone, motion, and accessibility — proposed behavior

- Stack columns and panels below 760px; keep navigation visible as wrapping anchor links. Avoid sticky sidebars on phones.
- Keep body text readable without horizontal scrolling. Reduce heading size naturally with the clamp rule.
- Use visible keyboard focus, descriptive links, semantic headings, and sufficient text contrast. Verify these in the built site.
- Default to no motion except short hover/focus feedback; respect prefers-reduced-motion. Never hide content behind hover or animation.
- Images are optional. Use participant-provided or appropriately reusable assets only; no borrowed headshots, logos, project images, or scientific figures.

## Keep the first build focused

Avoid babyish language, excessive decoration, huge blank sections, or invented project art.

## Build verification

Compare the generated preview to the observed cues and the chosen personality above. Check desktop and phone layouts, keyboard access, links, actual font fallbacks, and the approved content. Verify the site itself; no reference-site browsing or Firecrawl access is required for this prepared option. Record adaptations in DESIGN.md.

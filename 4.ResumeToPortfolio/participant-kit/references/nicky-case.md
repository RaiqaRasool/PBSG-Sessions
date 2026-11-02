# Playful and explorable — inspired by Nicky Case

## Source and evidence

- Original website: [Nicky Case](https://ncase.me/).
- Review context: November 1, 2026. Desktop opening view inspected in-browser; branding fields retrieved with Firecrawl. Earlier captures are reused where adequate.
- Observed visual cues: Outlined containers, large direct headings, red accents, grouped project previews.
- Extracted font/color evidence: Firecrawl reported Helvetica/Arial sans-serif stacks, white #FFFFFF, dark text #333333, and red #FF4040. The proposed darker link red below improves small-text contrast; it is an intentional adaptation.
- Boundaries: this is a self-contained workshop adaptation, not an exact source-code copy. No original-site screenshots or fonts are bundled. Mobile behavior, deeper pages, and source animation have not been fully audited.

## Personality — editorial interpretation, not measured fact

Friendly, curious, direct; explain work in accessible language. Borrow this communication style only where it fits the participant. Keep their voice and approved facts; do not impersonate the source owner.

## Implementation values — proposed workshop choices

Use these values without fetching the original site. Hex colors and dimensions below are explicit workshop choices, not a claim to reproduce source CSS exactly.

| Role | Value |
| --- | --- |
| Page background | `#FFFFFF` |
| Primary text | `#333333` |
| Accent/links | `#B42323` |
| Panel background | `#FFF3F0` |
| Heading stack | `Helvetica, Arial, sans-serif` |
| Body stack | `Helvetica, Arial, sans-serif` |
| Body size / line height | `18px / 1.65` |
| Reading width | `68ch` |
| Wide layout maximum | `1120px` |
| Spacing scale | `8, 16, 24, 40, 64, 96px` |
| Desktop main heading | `clamp(2.5rem, 6vw, 5.5rem)` |
| Phone page gutter | `20px` |

Named source fonts are reference information, not bundled font assets or permission to download them. Use an already available font if present; otherwise use the stated system fallback. No font download is required. Record the actual stack used in DESIGN.md and mention any substitution once.

## Layout and components

Use a welcoming short introduction in an outlined container. Follow with a compact grid of highlights grouped only when enough content exists, then experience and contact.

Rounded outline, large straightforward section labels, link emphasis. Keep the first screen readable and quick to scan.

## Present the participant's content

Present a title, plain-language problem, and supported contribution for each highlight. Use text blocks if no real thumbnails exist.

Keep one page with an introduction and only useful sections supported by the chosen résumé. The résumé is factual input, not a section checklist: combine, rename, or omit headings as appropriate. Projects and contact are optional, and experience contributions need not be turned into projects. Follow AGENTS.md content-curation rules; allow ordinary-language section changes without asking for additional material. Do not inherit the source site's page count.

## Phone, motion, and accessibility — proposed behavior

- Stack columns and panels below 760px; prefer visible wrapping anchor links when they fit. If navigation genuinely needs a toggle, follow AGENTS.md keyboard/ARIA/no-JavaScript requirements. Avoid sticky sidebars on phones.
- Keep body text readable without horizontal scrolling. Reduce heading size naturally with the clamp rule.
- Use visible keyboard focus, descriptive links, semantic headings, and sufficient text contrast. Verify these in the built site.
- Default to no motion except short hover/focus feedback; respect prefers-reduced-motion. Never hide content behind hover or animation.
- Images are optional. Use participant-provided or appropriately reusable assets only; no borrowed headshots, logos, project images, or scientific figures.

## Keep the first build focused

Avoid forcing games, videos, informal slang, cartoons, newsletters, or new interactive explanations into a résumé.

## Build verification

Before building, revise the draft copy in this personality and obtain approval under AGENTS.md. Record 3–5 visual cues and 2–3 personality traits in DESIGN.md. Compare the generated preview to those specific cues and traits, fixing material mismatches before handoff; report any visual comparison you could not perform. Check desktop and phone layouts, keyboard access, links, actual font fallbacks, and the approved content. Verify the site itself; no reference-site browsing or Firecrawl access is required for this prepared option. Record adaptations in DESIGN.md.

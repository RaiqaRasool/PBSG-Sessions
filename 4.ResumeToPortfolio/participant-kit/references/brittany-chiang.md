# Structured and professional — inspired by Brittany Chiang

## Source and evidence

- Original website: [Brittany Chiang](https://brittanychiang.com/).
- Review context: November 1, 2026. Desktop opening view inspected in-browser; branding fields retrieved with Firecrawl. Earlier captures are reused where adequate.
- Observed visual cues: Dark navy, clean sans-serif type, a prominent identity/navigation column beside readable experience and work content.
- Extracted font/color evidence: Firecrawl reported Inter for headings and paragraphs, consistent with the site footer naming Inter. Some extracted body-stack and color fields conflicted with the rendered dark-navy view; do not use those fields uncritically.
- Boundaries: this is a self-contained workshop adaptation, not an exact source-code copy. No original-site screenshots or fonts are bundled. Mobile behavior, deeper pages, and source animation have not been fully audited.

## Personality — editorial interpretation, not measured fact

Composed, precise, confident through clarity. Borrow this communication style only where it fits the participant. Keep their voice and approved facts; do not impersonate the source owner.

## Implementation values — proposed workshop choices

Use these values without fetching the original site. Hex colors and dimensions below are explicit workshop choices, not a claim to reproduce source CSS exactly.

| Role | Value |
| --- | --- |
| Page background | `#0F172A` |
| Primary text | `#E2E8F0` |
| Accent/links | `#5EEAD4` |
| Panel background | `#162339` |
| Heading stack | `Inter, system-ui, sans-serif` |
| Body stack | `Inter, system-ui, sans-serif` |
| Body size / line height | `18px / 1.65` |
| Reading width | `68ch` |
| Wide layout maximum | `1120px` |
| Spacing scale | `8, 16, 24, 40, 64, 96px` |
| Desktop main heading | `clamp(2.5rem, 6vw, 5.5rem)` |
| Phone page gutter | `20px` |

Named source fonts are reference information, not bundled font assets or permission to download them. Use an already available font if present; otherwise use the stated system fallback. No font download is required. Record the actual stack used in DESIGN.md and mention any substitution once.

## Layout and components

On wide screens use a roughly 40/60 identity/content split. Keep the left introduction visible while the right column presents About, Experience, and Selected Work. Use ordinary anchor links.

Quiet dividers, date/title alignment, restrained pill labels, optional subtle panel hover.

## Present the participant's content

Turn skills or research areas into short labels. A single role and two highlights are enough; shorten the timeline rather than pad it.

Keep one page with an introduction, supported selected work/research, relevant experience/education, and approved contact links. Omit empty sections and allow the participant to add/remove/rename sections in ordinary language. Do not inherit the source site's page count.

## Phone, motion, and accessibility — proposed behavior

- Stack columns and panels below 760px; keep navigation visible as wrapping anchor links. Avoid sticky sidebars on phones.
- Keep body text readable without horizontal scrolling. Reduce heading size naturally with the clamp rule.
- Use visible keyboard focus, descriptive links, semantic headings, and sufficient text contrast. Verify these in the built site.
- Default to no motion except short hover/focus feedback; respect prefers-reduced-motion. Never hide content behind hover or animation.
- Images are optional. Use participant-provided or appropriately reusable assets only; no borrowed headshots, logos, project images, or scientific figures.

## Keep the first build focused

Avoid copying every historical role, adding a mandatory blog, or making the desktop sidebar consume phone space.

## Build verification

Compare the generated preview to the observed cues and the chosen personality above. Check desktop and phone layouts, keyboard access, links, actual font fallbacks, and the approved content. Verify the site itself; no reference-site browsing or Firecrawl access is required for this prepared option. Record adaptations in DESIGN.md.

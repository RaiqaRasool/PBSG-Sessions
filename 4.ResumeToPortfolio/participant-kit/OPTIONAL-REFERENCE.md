# Optional: prepare a reference of your own

Skip this guide if you chose a prepared option in DESIGN-OPTIONS.md. You do not need Firecrawl for the main workshop.

## Route A — use a screenshot, without another plugin

1. Open the website you like in your browser.
2. Capture the page or section you want to use as inspiration. On a Mac, press **Shift + Command + 4** and drag over the area. On Windows, press **Windows + Shift + S**, select the area, and save or paste the capture.
3. Add the screenshot to your portfolio chat and paste the original website address.
4. Send the prompt under “Prepare the file” below. Screenshot-only analysis can estimate appearance, but cannot establish exact font names, CSS, or interaction behavior. AI should label those gaps.

## Route B — connect Firecrawl for font and styling evidence

1. In the desktop app, open **Plugins**.
2. Search for **Firecrawl** and open its details.
3. Select its install control and follow the connection prompts. Complete any sign-in in the service's interface; do not paste passwords or tokens into chat.
4. Use the available free access for the workshop; no paid plan or manual MCP server setup is required. If unexpected payment or setup is requested, use Route A or a prepared option instead.
5. Start a new Codex chat in your existing **My Portfolio** project after installation. Keep using the same portfolio folder.
6. Send the prompt below with your reference URL. AI should check actual tool support before requesting branding and a screenshot. A returned screenshot must be viewed before making visual-layout claims.

Firecrawl can retrieve font-family names, colors, typography, spacing, and screenshots. This improves the evidence but does not guarantee exact reproduction or provide font reuse rights. See [branding and screenshot documentation](https://docs.firecrawl.dev/features/scrape#extract-brand-identity). Availability and connection screens should be checked by the facilitator.

## Prepare the file

Copy this prompt, replace the bracketed address, and attach a screenshot if using Route A:

```text
Prepare a reusable design and personality brief for my portfolio from this public reference: [paste URL here]. Read AGENTS.md, OPTIONAL-REFERENCE.md, and references/README.md first.

If connected Firecrawl is available, inspect one representative page using branding, markdown, and screenshot outputs where supported. Inspect the screenshot pixels, not only its URL. Reuse adequate existing evidence. Use browser inspection only to resolve material gaps or check important interactions; do not crawl the whole site.

Otherwise use my supplied screenshot and available browser tools. Never claim exact fonts, CSS values, or behavior from insufficient evidence. If visual evidence is missing, ask for a screenshot rather than guessing.

Save references/custom.md with: source URL and review context; observed visuals; extracted font/color values with evidence; personality and writing-style interpretation; proposed implementation tokens and system-font fallbacks; one-page layout and résumé presentation; proposed phone/reduced-motion behavior; and unresolved details. Distinguish observed/extracted facts, interpretations, and proposed choices. Keep it self-contained so later use requires no Firecrawl or live-site access.

Use the format of one prepared reference brief as a guide. Do not copy the reference owner's personal content or assets. No new sections or pages are required by the reference. Record the custom choice in DESIGN.md and propose personality-shaped revisions to CONTENT.md for approval before implementation. Do not overwrite approved copy, rebuild, or publish my website yet.
```

**Expected result:** AI saves `references/custom.md`, with enough instructions to use later and honest notes about any unknowns. If it cannot inspect a site or screenshot, choose a prepared option rather than treating a guessed brief as finished.

## Build from the new file

When you have approved both the custom brief and its personality-shaped copy, send:

```text
Build my portfolio using references/custom.md and the personality-shaped CONTENT.md I approved. Follow AGENTS.md, preserve the saved publishing destination, and keep the one-page defaults. Use readable formatted files and the existing preview method without requiring extra browser tooling. Compare the defining visual/personality cues and report any checks you could not perform. Do not publish yet.
```

You can now reuse the local custom brief without Firecrawl. Publish through the normal Step 8 prompt when you approve the preview.

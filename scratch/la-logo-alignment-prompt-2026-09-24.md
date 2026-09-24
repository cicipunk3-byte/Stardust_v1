# LA prompt: logo alignment VERIFICATION sweep (Sep 24, 2026, afternoon)

TO-THE-AGENT: the logo alignment pass has already run and the site now carries the ThreadCat mark. This pass is VERIFICATION ONLY. Do not redesign anything. Check each item below against the live site, fix only what fails, and report.

Note: this prompt supersedes the earlier logo-alignment prompt (archived at scratch/archive/la-logo-alignment-prompt-2026-09-24-pre-logo-ran.md). Most of that prompt is already live: new nav mark, alt text, favicon set (16/32/180/512), og:image card, brand hero image, accent palette. Verify rather than redo.

### Verify (fix only on failure, report each)

1. Nav logo: the mark renders on every page, alt text reads "The ThreadCat mark: a cat head holding an orange and teal swirl, two threads in one orbit." and no old logo asset remains anywhere.
2. Favicon: /favicon-16.png, /favicon-32.png, /favicon-512.png and the apple-touch-icon all load and show the new mark, not the old one. Check browser-tab legibility of the 16px size.
3. og:image and twitter:image resolve and show the new card.
4. Accent palette: confirm the three accent colors sample from the logo (orange #f3a84d, teal #48a19f, pink #e3849c) and appear as accents only: links and section numbers in teal, primary buttons in orange, the pink accent used sparingly. Body text stays charcoal on cream/white. Report the hex values actually in use, including any dark-mode variants.
5. Contrast pass: every place an accent color carries text, confirm it passes WCAG AA at its size. If any accent-on-background pairing fails, darken the accent there and report the before/after hex.
6. Em-dash sweep on any text the alignment pass touched (including the hero caption and any new alt text).
7. Hero image: confirm the caption matches the on-record style ("Fig. 01 · Isolated environments, observed behavior" pattern) and the image alt text describes the art accurately.

### Content rules (unchanged)

- No content changes: /papers, /sources, /governance, cost card, and all copy stay exactly as they are.
- No em-dashes. No strengthened claims.
- Every fix listed in the report with the page and the before/after.

### Process

Publish-first. Make corrections, publish, then report the verification checklist line by line with pass/fail per item. Cache-bust. The humans audit jointly in thread after publish.

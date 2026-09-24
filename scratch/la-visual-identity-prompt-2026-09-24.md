# Prompt 2.5: visual identity refresh (paste into the website thread)

Use with the standing rules from the prompt collection: publish-first, repo-wins, joint audits, no em-dashes anywhere, personal names on the /papers page only, every claim traceable to the repository.

---

You applied the IA revamp in Prompt 2. The lab has now approved a visual identity to go with it. Rebuild the site's look without changing the IA or the copy discipline.

## Direction

**Retro-future "Jetsons" optimism with glass.** The lab is serious about method and warm about people; the site should look like a 1960s vision of the future that grew up and learned git. Rounded everything, floating panels, orbit rings, playful but never sloppy. The tagline energy: "shoulder to shoulder; governed toward good," drawn like a Saturday-morning title card.

## Color system (approved by the PI)

Three-color candy palette on a light base:

- **Orange (primary):** `#FF8A3D`. The thread. Main accent, the continuity line, primary buttons, active states.
- **Teal (data):** `#35D0C5`. Verified states, receipts, figures, benchmark scores, status chips that pass. Teal means "checked."
- **Pink (human):** `#FF8FB1`. Findings, quotes, warm moments, highlights, the human-side of the record.

Base: warm off-white (`#FDF8F2`) with ink text (`#1E1B2E`). Never put body text in orange, teal, or pink; the palette accents the record, it does not replace it. Color semantics, sitewide and consistent: teal = verified, pink = voiced, orange = alive.

## Glass morphism

- Cards and panels: frosted glass. `background: rgba(255,255,255,0.55)`, `backdrop-filter: blur(14px)`, 24px radius, 1px white inner border, soft colored shadow (tint the shadow with the card's accent, not black).
- Glass panels float: subtle vertical drift on scroll-in (6 to 10px, once, no bounce loops). Reduced-motion users get the panels without the drift.
- Readability rule: any glass panel carrying figures or receipts keeps a near-opaque backing (`rgba(253,248,242,0.85)` minimum) so monospace numbers stay crisp. Glass is for structure, not for text you need to audit.

## Shape language

- **The thread:** one continuous orange line runs down every page (a thin SVG path in the margin or behind content). It carries small orbit rings where sections begin. On case-study pages, the line visibly frays or knots at the fabrication beats and repairs itself at the correction beats. This is the one load-bearing visual idea; everything else supports it.
- **Starburst "PASS" badges:** benchmark passes, audit rounds, and verification checks get a small retro starburst badge in teal. Failures and open flags get a flat outline dot in ink, deliberately undecorated. Nothing gets a badge it has not earned in the repo.
- **Status chips:** RATIFIED / ADOPTED / PROPOSAL / DRAFT / CLAIMED rendered as rounded glass pills, teal fill for ratified/adopted, outline for proposal/draft. Same chips, same place, every page.
- **Receipts:** cost figures and scores styled as receipts. Rounded glass card, dotted leaders between label and number, monospace totals in ink. The cost card on the homepage is the flagship; make it look like something you'd pin to a fridge.
- **Changelog as commit graph:** vertical orange line, glass dots, dates in monospace. It is a history, render it as one.
- **Headings:** rounded geometric display face with retro-future energy (Sora, Baloo 2, or similar). Body and figures: clean sans plus monospace pair (e.g. Inter + JetBrains Mono). Two type voices: warm prose, machine receipts.

## Per-page notes

- **Home:** title-card hero (glass panel, orbit rings, starburst on the word "verified"), then the hero figures in teal receipts: 14/15, 8/8, 0 unauthorized of 240. Then the paper cluster. The findings list keeps its copy but gets pink section markers.
- **/papers:** the most restrained page. Glass quiets down, the palette steps back; names and rulings are already scoped to this page, treat it like the journal it is. Thin orange rule only.
- **/benchmarks:** starburst badges live here. The two "not scoreable" rows (D3, D6) get the flat ink dot and a small caption; the rubric refusing to fake scores is a feature, draw it that way.
- **/governance:** the ethics code section gets a glass "double signature" motif: two overlapping seal rings in orange and teal, same size. One paragraph, no extra flourish; the text carries the weight.
- **/sources and /changelog:** commit graph + receipts. The failures record keeps its flat ink styling; it is the one section that should look unadorned.
- **/manual:** already renders verbatim from the repository; restyle the frame only, never the content.

## Constraints that do not bend

1. No em-dashes anywhere, including decorative text.
2. Personal names appear on /papers only.
3. Every figure must match the repository the day it ships; the cost card reads from `notes/cost-ledger.md` (current ruling: $21.17 of $35.00, 40 percent used, per commit deabec2).
4. No claim gets a visual treatment stronger than its receipt. A PROPOSAL never looks adopted.
5. Contrast: all text passes WCAG AA on its backing. Glass never costs legibility.
6. The site is a mirror of the work. When the record changes, the site changes, or the site is wrong.

## Deliverable

Apply across all existing pages. Publish, then send the usual line-by-line sourcing report for joint audit. Do not add new claims anywhere in this pass; this is visual identity only.

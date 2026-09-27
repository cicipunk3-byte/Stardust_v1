# LA PROMPT 9: mobile parity + the packages jam-up, 27 September 2026

**Context:** the PI published on the back end and asked two things: (1) confirm everything built made it live, (2) guarantee the mobile site is the same design at a smaller size, not a sloppier one. The post-publish audit (?v=26) found one jam-up.

## FIRST: the jam-up

The packages page change did NOT publish. The live page (?v=26) still reads "Seventeen tools, four postures." in the page title, the meta description, the og/twitter titles, and the body line, while the same page's new menu DID go live. Everything else published correctly (canonical menu on all pages, homepage cost section, report card scope line, 07 items, changelog entries including the publication line, tools page count-sentence fix).

Re-stage the packages title and line changes (per the prompt 7 rulings: "The Bundles: one record, four postures" in title, meta, og, twitter; "One record, four postures." as the body line), then BEFORE the next publish, list every change currently sitting in preview and confirm each one is present in the build. The PI publishes at her discretion; nothing publishes without her click.

## SECOND: the mobile parity standard

The mobile site is the same design at a smaller size. Rules, all testable:

**Same content.** No section, card, figure, paragraph, or link exists on desktop but not on phones, and none is reworded on mobile. Layout may change; content may not.

**Same navigation.** The phone Menu link opens the SAME canonical 14-page list in the same order as the desktop top menu (Mission, Philosophy, Tools, Packages, Manual, Local model, Wary of AI, Reflections, Papers, Benchmarks, Changelog, Governance, Sources, PinkPromise last). The overlay opens within 200ms, closes on selection, and never shows a shortened or reordered list.

**Same hierarchy.** PinkPromise stays the loudest button on phones. The solid and glass pill variants keep their distinct roles: solid for flagship and primary actions, glass for secondary. Pills stack full-width, about 48 pixels tall.

**Same discipline.**
- Body text at least 16px on phones; no shrink-to-fit smaller than that anywhere.
- Touch targets at least 44 by 44 pixels, including the filter pills and the Menu link.
- No horizontal scrolling at 320, 375, or 390 pixel widths.
- The benchmarks table gets a mobile layout that keeps every column's data and every advisory flag; it may reflow but never drop the advisory warnings.
- Glass pills over the pink gradient keep their measured contrast at phone widths; the gradient layers compress at small sizes, so verify rather than assume. Same 4.5:1 bar for normal text.
- The progress bead, the cost card, and the report card all render fully on phones; no card collapses into a teaser.

**Same verification.** Screenshots at phone width (390px) AND desktop width, taken only after each page finishes loading, for: homepage (hero, cost section, report card), packages, benchmarks table, changelog with filters, the phone Menu open, and one error page. Report before publishing; the PI decides when.

## Standing checks, unchanged

No personal names outside the papers page, no em-dashes, every figure matches notes/cost-ledger.md, the nav comes from the canonical list and nowhere else.

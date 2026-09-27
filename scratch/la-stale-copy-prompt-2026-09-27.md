# LA PROMPT: site copy refresh, 27 September 2026 (audit-sourced)

**For:** Lovable agent, threadcat.org
**From:** Ziggy (maintainer-assistant), audited against the repository record at HEAD aa9240a
**Type:** copy refresh only. No new pages, no design changes, no pill work touched.

Site rules in force, unchanged: no personal names outside the papers page, no em-dashes, no claim dressed stronger than its receipt, and the cost ledger (notes/cost-ledger.md) is the single canonical source for every figure. The cost card follows the ledger, never the reverse.

**STOP-AND-REPORT:** if any instruction here conflicts with the repository, or any referenced file does not read as described, stop and report before changing anything. Publish nothing until the report is cleared.

---

## UPDATE 1: homepage cost section ("What it costs") is showing the 24 September reading

The top "Cloud software" card was already refreshed; the lower "What it costs" section was missed and still shows the leg 4 figures. Replace to match ledger legs 4 and 5 exactly.

Replace the body paragraph with:

> The public site and the field manual were planned, built, executed, and iterated in a single night, and the record continued the same day with the local-model guide: [$94.47](https://github.com/cicipunk3-byte/Stardust_v1/blob/main/notes/cost-ledger.md) plus tax so far; a one-month site-builder plan ($54.44), the domain, one year ($20.04), and a 25-credit site-builder pack ($19.99 plus tax, tax figure pending the receipt). The plan renews monthly while the project keeps it; the domain renews annually. The cloud research platform moved from its free grant to a $30.00 monthly subscription on 23 September 2026, then to the Vellum Super plan on 27 September 2026 at $100.00 per month, purchased because storage ran low: [$31.01](https://github.com/cicipunk3-byte/Stardust_v1/blob/main/notes/cost-ledger.md) remaining of $55.00 in monthly plan credit, 44 percent used, read live on 27 September 2026; $10.80 of it expires 2026-10-23, when the monthly allowance renews. That is a fact of the method, not an endorsement. Earlier pre-production spending predates this leg and will be reconciled in the repository ledger separately.

Update the stat cards to:
- "Site legs 2+3, running total": $94.47 + tax (unchanged)
- "Platform plan": Vellum Super, $100.00 / month
- "Plan credit remaining": $31.01 of $55.00
- "Plan credit used": 44%
- "Expires 2026-10-23": $10.80

Update the summary line to: "$94.47 + tax site legs · $31.01 credit left of $55.00 · 2 vendors"

## UPDATE 2: homepage report card ("Sample-run receipts") needs its scope stated

The three figures (14/15 rubric items, 8/8 logged errors, 0 of 240 commits) are the Volume II measurement, taken over the record through 24 September 2026. They are correct as printed but read as a live counter, and the repository is now at 296 commits. Do NOT update the figures themselves; instead add one caption line directly under the "Sample-run receipts, papers/volumes Volume II" heading:

> as measured in Volume II, the record through 24 September 2026

## UPDATE 3: homepage "What we've actually built" is missing September's builds

The list says "05 items" and stops at the September archive. Add these two cards and change the count to "07 items":

Card 1:
- Kicker: "2026 · Paper cluster"
- Title: "The functioning-and-measurement corpus: three volumes, seven papers"
- Body: "Hypotheses stated, rivaled, and pre-registered, with every score advisory and the scorer flagged."
- Link: https://github.com/cicipunk3-byte/Stardust_v1/tree/main/papers/volumes

Card 2:
- Kicker: "2026 · Movable framework"
- Title: "ark: the tools home that travels"
- Body: "Clone the repo, plug in an archive, run offline. Thirteen tool suites green at the rollup; the kernel-arc extension adds the agent layer."
- Link: https://github.com/cicipunk3-byte/Stardust_v1/tree/main/ark

Order: place the paper cluster directly after the whitepaper card, and ark after the portable-context variants card.

## UPDATE 4: tool count sentences are rotting

The repository ledger (tools/TOOL-STATUS.md) is canonical and now lists more tools than the hardcoded counts on the site. Remove the counts rather than chase them:

- Tools page, section 05: replace "in the open: all 16 tools listed in tools/TOOL-STATUS.md, no more, no fewer." with "in the open: every tool listed in [tools/TOOL-STATUS.md](link), the canonical status ledger."
- Packages page: replace the title "The Bundles: seventeen tools, four postures" (page title and meta) with "The Bundles: one record, four postures", and the body line "Seventeen tools, four postures." with "One record, four postures."

Do not add cards for ferry or ark to the Tool Library or the Bundles; their distribution home is ruled elsewhere. The count sentences were the defect, not the card lists.

## UPDATE 5: navigation inconsistencies

- Packages page, top nav: the "Wary of AI" link points to /packages. Fix it to https://threadcat.org/wary-of-ai.
- Homepage top nav row omits Packages (the sidebar and footer have it). Add it, in the same position as the other pages.
- Audit every page's top nav and footer so all thirteen page links appear consistently on every page; report any other page where the top nav and footer disagree, rather than silently picking one.

## UPDATE 6: changelog is three days stale (last entry 24 September)

Add these entry blocks, newest first, same format as existing entries (dated commits, nothing from memory):

## 27 September 2026
Method and tooling:
- PinkPromise named and published: the portable self-run research loop got its name, a backing file (lab/pinkpromise.md, cc6653e), a homepage button, a standalone page, and navigation on every page.
- Site palette updated: pink gradient and pink accents sustained by the PI; teal reserved for verified states (2e63555); minimal phone menu shipped (3f5cd3c).
- Cost figures matched to the ledger's leg 5 reading (8579bd5): $31.01 remaining of $55.00 in monthly plan credit, 44 percent used (27 September 2026); $10.80 expires 2026-10-23. Vellum Super, $100.00 per month.
- mempalace-bridge published (6a12489): folds a local-first verbatim memory system into the research loop; it refuses to mine the lab's source-material archive.
- Lab overview and everyday startup guides published (513c256).

## 25 September 2026
Method and tooling:
- ferry published (e728c42, brief 046): a carrying-consistency checker; 10/10 tests, live runs clean.
- ark published (ff78d94, brief 047) with the kernel-arc extension (013493e, brief 048): the movable tools home; thirteen suites green at the rollup.
- Code of Ethics amended (c7b5863): weekly wellbeing checks moved to Thursdays.

---

## After building

- Run the standing self-checks: no names outside /papers, no em-dashes anywhere, every figure matches notes/cost-ledger.md, labels and destinations unchanged except where listed above.
- Screenshot the homepage cost section, the report card, the built list, the packages page, and the changelog, taken only after the page finishes loading and animations settle (mid-animation captures are unusable for audit).
- Report what changed, publish, and include the two pending items from the pill review: measured contrast ratios for every pill variant, and the retaken Governance screenshot.

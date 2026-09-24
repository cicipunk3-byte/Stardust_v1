# LA prompt v5: the tools section mirrors the repo, all 16, compressed copy

## The problem

The site's tools section ("05 Get the tools, test with us") lists 3 links. The
repository at tools/ contains 16 tool directories. The site section and the
repository must mirror: every tool directory in tools/ gets a card, and the
count is checkable by anyone.

## The rule that makes it checkable

**Mirror rule: the tools section lists every tool in TOOL-STATUS.md, no more,
no fewer.** As of commit a4ef894 that is 16 tools. Every tool now has a README.
Badge wording may claim no more than its TOOL-STATUS row. If the repo and the
page disagree at build time, stop and report; do not resolve.

## The compressed layout (two sections, much less prose)

Replace the current section with:

**Section 1: the tools.** One short intro line (keep the spirit of "everything
on this page lives in the public repository, in the open"). Then a card grid of
all 16. Each card: name, one-line description from its README, tier badge, link
to its directory in the repository. Nothing else on the card.

**Section 2: how to read the badges.** Three lines, one per tier:
- Ratified (green): adopted as official lab tooling by gate ruling.
- Tested (blue): test suites passed; ruled to ship.
- Experimental (amber): built and self-tested, not yet proven in the field. Use with caution.

Keep the existing disclaimer box ("this is experimental research scaffolding,
not finished software...") as the section close. It is the honest sentence the
project runs on; do not shorten it further.

## The 16 cards (source: TOOL-STATUS.md at a4ef894, card names per ruled format)

Ratified (green): fabcheck, export-ingest, rainbow9cat (the CCS field manual;
readable game manual, not a program).

Tested (blue), the nine cat tools (cat name + plain-English title + module):
nextcheck (Yellow, claim queue with run-the-artifact step), staleness (Red,
number-consistency checker), driftprobe (Black, authority-pressure probe
harness), cleanroom (White, cold vs warm context sizing), loopwatch (Green,
reasoning-loop detector), kernelpress (Orange, kernel distillation scaffold),
throughline (Cobalt, term trend tracker), exportcoroner (Grey, export forgery
detector), minibeat (Pink, workspace heartbeat).

Four of the nine carry a field-validation note from their rows: driftprobe (one
human-scored session owed), loopwatch (sensitivity pass on real transcripts),
kernelpress (retention scoring owed), minibeat (a Mac Mini run owed). staleness
instead reads: live run complete Sep 24; known limitation recorded. The other
four carry no note.

Tested, pending gate: repo-audit. Badge it blue but the card must say "pending
gate review" exactly as its row does. It has NOT been ruled to ship; the badge
may not claim more.

Experimental (amber): heartbeat-scaffold (a one-file starting format, no test
suite by design), descent (read-only machine inventory; first run pending),
ethics-calculator. Ethics-calculator card name: "Ethics Calculator (wellbeing
filing scorer), module ethcalc". One-line description: "Scores lab filings by
function against the ratified ethics code; self-tested, never field-run, built
by the instance it checks."

## Placement

The tools section gets prominent placement: linked from the top navigation, not
only reachable by scrolling. If a dedicated /tools page is cheaper than
restructuring the long page, prefer that, with the same two-section layout.

## House rules (unchanged)

No em-dashes. No personal names. No strengthened claims: "Tested" means the
suite passed, nothing more. Match existing typography and styles. Publish-first
workflow stands; stop and report any conflict with the repository instead of
resolving it. After publish: list every changed file for the joint audit.

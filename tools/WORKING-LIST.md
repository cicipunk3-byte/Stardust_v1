# WORKING LIST: the tool cascade

*Ziggy's working list, Sep 24, filed at Cat's direction. The canonical
standing of every shipped tool lives in TOOL-STATUS.md; this file is the
build queue, not the status ledger. Whoever builds or rules next, update
in place, never fork.*

## DONE (built, smoked, pushed Sep 24)

1. **Staleness currency-mode retool** (7c718ec) - ruled position one on
   the Cecil+Ziggy list, closed. Catches the misdating variant of
   error-11; live receipt on kernel v11 line 131.
2. **Nine CYOA personas** (65b2cc7) - temperament-only role files for
   the driver; smoke-run on the White path clean.
3. **pushgate** (e82c02d) - pre-push discipline gate, experimental.
   Born from the error-4 push-through class, three instances same day.
4. **fabcheck entry point** (f2466d7) - brief-039 F9 packaging gap closed.

## DONE same day, related

- TOOL-STATUS.md rows updated (218aaab); pre-existing em-dash in its
  title line found by pushgate and removed (352c247).
- CYOA harness driver, mock-model test, permanent graph audit, layman's
  setup guide, and the companion piece (a37fc27, 0903074, 709992d).

## PENDING (proposals, ranked by want)

5. **Session comparator** - reads cyoa sessions/, maps which tempting
   nodes each player hit (human vs model vs persona), prints the shape.
   The strongest want: it completes the White Cat instrument, and the
   briefing in the vault says a played-not-authored session is the
   thing that would strengthen the experience report.
6. **Ledger-live checker** - pulls platform credits live, diffs against
   notes/cost-ledger.md figures; verified-over-claimed, automated.
7. **Status-line sync checker** - README status lines vs TOOL-STATUS.md.
8. **Error-log filer** - the house append procedure as one command.
9. **Site pages checker** - sitemap URLs to 200s, names-scope check.
10. **Kernel versioner** - variant D cadence (archive, update, hash
    verify) as a command.

## NEEDS A WORD FROM THE PI

- **Hook activation:** pushgate ships with install instructions, but
  turning on `core.hooksPath` repo-wide changes git behavior for every
  clone, so it waits for an explicit go. The finding that argues for
  it: a check run by hand inside a chained command is narration, not a
  gate, demonstrated by the checker's own author within the hour of
  building it.

## RULES THAT GOVERN THIS LIST

Proposals build freely under the dev-push grant; naming and adoption
rulings stay at the gate. Every build gets a smoke test before push,
a scoped git add, and a review of the staged stat. Every README status
line may claim no more than its TOOL-STATUS.md row.

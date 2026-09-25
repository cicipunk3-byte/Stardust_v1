# Brief 046: Ferry -- the carrying-consistency tool

_Date: 2026-09-25_ · _Written for: small offline model; assume no prior context_

Status: **RULED (Cat, Sep 25, /cat) -- built, tested, pushed public same day.**

## Ruling (verbatim, on the record)

> "let's go for it. cascade down into the bundle being public and pushed. it will just live on the repo for now. it can be bundled into think pink instead of threadcat as one of the many free tools that will be available. want to respect the privacy of it, study it more and be able to ethically fold it into the materials on the site."

Effect: build now, push public now (repo residence); distribution home is the **ThinkPink** free-tools bundle, NOT the threadcat site; site fold-in deferred pending study and tracked as an owed item.

## Problem

The lab's records are carried by hand across surfaces that change at different speeds. The observed failure mode is not lost data but **stale attribution**: a fact changes (who owns an account, where a ruling gates, what number a brief holds) and older documents keep asserting the old version. On Sep 25 a manual consistency sweep found two live instances: a gate and a platform account attributed to the wrong pilot across several surfaces, and a brief-number collision (a private filing took 044 after the public series already used it). Both were fixed by hand the same day; the hand motion is this tool's specification.

## The tool

`lab/tools/ferry/` -- stdlib-only Python, three verbs:

- **`sweep`** -- checks a claims file (claim ID + forbidden regex patterns) against every markdown surface, classifying each as ACTIVE (fix in place), APPEND-ONLY (append a correction, never rewrite), or skip. Exit 1 when an active surface matches. Reports; never rewrites.
- **`collisions`** -- duplicate brief numbers within and across the two collections (lab/briefs, private-briefings). Archived priors excluded: they keep their old numbers by design.
- **`carry`** -- verifies a file list (missing files abort with nothing written), hashes it (SHA-256), and emits a manifest plus a **one-page plain-English carry sheet**: what to download, where it goes, how to verify, what done looks like. Written for a reader with zero lab context; if the sheet needs intuition, the sheet is the bug.

## Method and results

House standard: real-failure positive controls + clean negative controls, run from the tool's own directory. Ten tests: the positive controls are neutralized versions of the two real Sep 25 failures (attribution drift; cross-collection number collision), with all pilot names scrubbed from fixtures. Two additional defects were caught by running the tool live against the real workspace during development (a scan that over-matched wiki pages as briefs; an over-broad example pattern) and fixed before the push. Final: **10/10 tests green; live `collisions` CLEAN; live `sweep` CLEAN** against the corrected record.

## Privacy guardrail

The motivating incidents arose in a private thread. Per the PI's ruling, the tool's public surfaces (this brief, the README, fixture files) carry **no thread content and no personal context**: positive controls are scrubbed to neutral team labels, and example claims use neutral lab facts. The full narrative record stays in the private custody chain.

## Placement

- **Not one of the nine** glass-vessel cats; the nine keep their one-job census. Ferry is carrying infrastructure beside them, operationally the checking half of the Keepers bundle's motion (`lab/bundles/keepers/`).
- **Distribution:** this repo now; **ThinkPink's** free-tools bundle when that project's repo exists.
- **Owed (tracked):** ethical fold-in of the site's Tool Library materials after study -- nothing ships to the site before then.

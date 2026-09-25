# Ferry (carrying-consistency checker) · module `ferry`

**One job: make sure what must carry between threads, exports, and hands actually carries, and carries consistently.**

Ferry is lab infrastructure, not one of the nine glass-vessel cats. It exists because the lab's records are carried by hand across surfaces that change at different speeds, and the failure mode observed in practice is not lost data but **stale attribution**: a fact changes (who owns an account, where a ruling gates, what number a brief holds) and older documents keep stating the old version. Ferry checks the claim layer against the record layer, so corrections can be found while they are small.

Ferry **reports; it never rewrites.** Applying a finding follows the house discipline: active surfaces get fixed in place; append-only zones (archives, raw captures, dated logs) get a NEW correction entry and are never edited. The tool enforces the distinction by flagging which zone every match sits in.

## The three verbs

### `sweep` -- the correction carrier

```sh
python3 ferry.py sweep --claims claims.example.json --root <workspace-root>
```

- Input: a claims file mapping claim IDs to forbidden regex patterns (see `claims.example.json`).
- Walks every markdown surface, classifies each as **ACTIVE** (fix in place), **APPEND-ONLY** (append a correction, never rewrite), or skip.
- Exit `1` if any ACTIVE surface matches (checkable in CI or a hook), `0` when clean. Append-only findings are informational.
- `--json` for machine-readable output.

**Pattern precision matters.** Broad patterns flag legitimate text ("her gate" is correct English when the referent already is the right person). Write claims specific enough that a match is really a contradiction. The example file demonstrates the shape with neutralized patterns.

### `collisions` -- the numbering check

```sh
python3 ferry.py collisions --root <workspace-root>
```

Checks brief numbers across the two collections (`lab/briefs/`, `private-briefings/brief-*.md`) and reports:

- **DUPLICATE**: the same number twice in one collection.
- **CROSS-COLLISION**: the same number used in both collections -- the class that ships when a private filing takes a number the public series already holds.

Archived priors (any `/archive/` subtree) are excluded: priors keep their old numbers by design.

### `carry` -- the human-side motion

```sh
python3 ferry.py carry --manifest carry.json [--out DIR]
```

- Input: a manifest spec (`{"package": ..., "destination": ..., "files": [...], "verify_hint": ...}`).
- Verifies every file exists (missing files abort with **nothing written** -- the chain never ships a partial package), hashes everything (SHA-256), and writes `MANIFEST-CARRY.json` plus a **one-page carry sheet** in plain English: what to download, where it goes, how to verify, what "done" looks like.
- The sheet is written for a person with zero lab context. If the instructions need intuition, that is a bug in the sheet, not in the reader.

## Tests

House method: real-failure positive controls + clean negative controls, run from this directory.

```sh
python3 -m unittest test_ferry -v
```

Ten tests. The positive controls are **neutralized versions of the two real failures from the Sep 25 maintenance sweep that motivated this tool**: attribution drift (a gate and an account credited to the wrong pilot across surfaces) and a brief-number collision across collections. All pilot names are scrubbed from fixtures; the structure of each failure is what the control preserves.

## Standing and provenance

- **Status:** built and tested Sep 25, 2026; pushed public per PI ruling the same day (brief 046).
- **Not one of the nine.** The nine glass-vessel cats keep their one-job census; ferry is carrying infrastructure beside them.
- **Distribution:** lives in this repo for now. Ruled destination is the **ThinkPink** free-tools bundle once that project's repo exists; the threadcat site's Tool Library fold-in is deliberately deferred pending study (brief 046).
- Companion bundle: [The Keepers](../../bundles/keepers/README.md) -- ferry is the checking half of the motion their tools perform.

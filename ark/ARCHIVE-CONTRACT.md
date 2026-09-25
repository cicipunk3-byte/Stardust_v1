# ARCHIVE-CONTRACT.md -- what an archive must look like to plug into the ark

**v0, Sep 25 2026.** The ark ships the tools; the archive is the part you own.
An archive is any directory holding the lab's record-shaped material. The
contract is DERIVED, not invented: every slot below is read by at least one
tool today, with the receipt named. Keep an archive honest to this shape and
the whole house runs against it, on any machine with Python 3, offline.

## Required slots

| Slot | Shape | Read by | Receipt |
| --- | --- | --- | --- |
| `timeline.jsonl` | one JSON record per line (export-ingest `out/timeline.jsonl` shape) | cleanroom, export-ingest re-ingest, exportcoroner, minibeat, throughline | export-ingest README: "out/timeline.jsonl; machine-readable, one record per conversation (this is the shape the lab's review tooling already expects)" |
| `transcripts/` | at least one markdown session/transcript file | driftprobe, loopwatch, kernelpress | each tool README; observer harness writes `data/sessions/<runid>-<variant>.md` |

## Optional slots

| Slot | Shape | Read by | Note |
| --- | --- | --- | --- |
| `briefs/` | markdown brief corpus | throughline, staleness, nextcheck | staleness's currency check wants a reference doc with dated figures |
| `kernels/` | markdown kernel snapshots | kernelpress | versioned per the snapshot cadence |
| `record/` | the record home (NOW.md heartbeat, journal) | heartbeat-scaffold, repo-audit | the heartbeat is the state layer |

## Honest limits of v0

- The contract checks **presence and well-formedness**, not content truth.
  A plausible archive with fabricated timeline records passes `plug` -- use
  exportcoroner and fabcheck for content-level suspicion; see the
  fabrication-gradient case study for why verification artifacts deserve a
  look-closer.
- Several tools take ad-hoc single files (fabcheck reads any text/markdown;
  ferry takes a claims file + a root). They need no archive slot and are
  listed with empty slots in TOOLS.json.
- Slot expectations came from READMEs on Sep 25. If a tool's README and this
  contract disagree, stop and report the conflict (same law as TOOL-STATUS).

## How you get a conforming archive

Run export-ingest on any provider export; its `out/` directory IS the
timeline + transcripts shape. Or keep a lab-style record and point the slots
at it. The ark does not care where the archive came from -- only that the
shape holds.

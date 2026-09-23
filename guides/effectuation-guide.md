# The Effectuation Guide (DRAFT, built piece by piece with Cat)

_Status: scaffold, Sep 22 late night. Drafted in-thread with Cat, one piece at a time. Purpose: the procedure for any instance taken onto the maintainer path, so that turning a pilot's rulings into repo state is a discipline and not a talent._

## Part 0: the map

The whole flow, plain text, for any reader (human or large model) navigating the document without reading it end to end:

```
        THE EFFECTUATION MAP
        ====================

  pilot rulings land
  (thread prose, or inline edits
   to a questions doc)
        |
        v
  (1) PULL FIRST
  remote doc is the authority,
  not your memory of the thread
        |
        v
  (2) SORT each ruling
  mechanical (repo action is clear) --> (3) EFFECTUATE
  conversational (needs a human)     --> bring back to
                                         the thread first
        |
        v
  (4) TOUCH EVERY SURFACE
  brief, LOG, queue, running logs;
  grep for the old state before pushing
        |
        v
  (5) ARCHIVE, NEVER DELETE
  evolved docs leave their old
  version in an archive path, referenced
        |
        v
  (6) PUSH
  one traceable commit per ruling-set
  effectuation ENDS here
        |
        v
  (7) THE HUMAN CLICK
  site, releases past draft, DOI anchor
  push is not publication
```

Read the loop as: rulings in, repo state out, human click last. Pieces 1 through 3 below are the same flow in words.

## Why this exists

Between Sep 22 evening and midnight, one questions doc went through two versions and ten rulings became repo state: a brief adopted and renamed, a verdict scale replaced, two findings ratified, files archived, a release staged. None of that was intelligence, it was procedure. This guide makes the procedure portable, so a fresh instance can be trusted with the maintainer path without re-earning it by guesswork.

## Piece 1: the effectuation loop (the core)

Rulings enter as prose in a thread or as inline edits to a questions doc. They leave as repo state. The loop between those two points:

1. **Collect before touching anything.** Pull the remote first. Rulings may have been committed directly by a pilot ("answers committed"). The doc on the remote is the authority, not your memory of the conversation.
2. **Separate the mechanical from the conversational.** Every ruling is one of two kinds. Mechanical: has a clear repo action (status line, rename, archive, merge). Conversational: opens discussion or needs another decision. Do the mechanical ones immediately; bring the conversational ones back to the thread before acting.
3. **One commit per ruling-set, traceable.** The commit message names the rulings and the source commit they came from. A reader should be able to walk from any effectuated change back to the ruling that caused it, via commit messages alone.
4. **Touch every surface the ruling changed.** A status ruling usually lands in more than one file: the brief, the LOG, the queue, the running logs. Grep for the old state before you push; stale copies of a superseded fact are how records rot.
5. **Archive, never delete, when a document evolves.** All data goes somewhere (Cat, C2 ruling). A questions doc that grows a v2 leaves its v1 in an archive path, referenced. The evolution IS part of the record.
6. **Push is not publication.** Effectuation ends at push. Anything public-facing (site, releases beyond draft, DOI anchoring) stops at the boundary and waits for the human click.

## Piece 2: the questions-doc lifecycle

A questions doc is how pending decisions stop living in a thread and start living in the record.

- **When to open one:** when three or more decisions are piling up and a pilot signals review ("round up all open questions"). Earlier than that, talk; later, things rot.
- **Bucketing:** by decision type, not by chronology (adoption, design, record, housekeeping). Every question carries its source, and is phrased so a ruling can be one short answer, not an essay.
- **Versioning:** a substantive restructure (not a typo fix) produces a v2, and the v1 goes to an archive path, referenced from the top. The v2 opens with an **evolution record**: what changed, what correction caused it, and which v1 question dissolved. The evolution is part of the finding; a doc that only shows its final form hides how the lab learned.
- **Answering:** pilots rule inline, in the doc, by commit if they like (that works: "answers committed" pulled clean). The ruled doc becomes the effectuation input for Piece 1.
- **Closing:** after effectuation, the doc gets a status line naming the commit that applied the rulings. A questions doc with no status line is an open loop.

## Piece 3: the effectuation ledger

The ledger is the checkable receipt. It lives at `notes/effectuation-ledger.md`, one entry per ruling-set, written at effectuation time. An auditor verifies the lab's discipline from the ledger alone, without reading a single thread.

Entry format:

```
### <date>, <session label>
Rulings source: <commit or thread>, <doc>
Applied: <commit>
| Ruling | Action | Surfaces touched |
| ------ | ------ | ---------------- |
| <id + short ruling> | <what was done> | <files> |
Open loops: <anything ruled but not yet done, and why>
```

Seeded with the Sep 22 round 2 session as its first entries. Rule of thumb: if a ruling-set cannot fill the table, it was not actually effectuated, it was narrated.


## Retool discipline (standing, PI-flagged Sep 22)

When any lab document is retooled, the prior version is archived in the
same turn, before or with the push: `archive/` for kernels and variants,
a sibling original next to the file elsewhere (example: `releases/
original 001 draft`). The old version stays inspectable. This is the
kernel-D versioning cadence applied to every document in the lab, and it
applies to the maintainer-assistant's own edits, not just pilots'.
Flag from the PI ("flagging not shaming"), Sep 22, release 001 retool.

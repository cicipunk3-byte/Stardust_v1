# The Effectuation Guide (DRAFT, built piece by piece with Cat)

_Status: scaffold, Sep 22 late night. Drafted in-thread with Cat, one piece at a time. Purpose: the procedure for any instance taken onto the maintainer path, so that turning a pilot's rulings into repo state is a discipline and not a talent._

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

## Piece 2: draft pending (the questions-doc lifecycle)

When to open a questions doc, how to bucket, the evolution record, when to archive. Drafted after Cat reviews Piece 1.

## Piece 3: draft pending (the effectuation ledger)

A checkable receipt format: ruling, source commit, actions taken, surfaces touched. So an auditor can verify effectuation without reading the thread.

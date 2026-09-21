# Heartbeat scaffold

A plug-and-play starting file for any human-agent pair working on a
project across sessions, built from zero by people who have never seen
a wiki framework and do not need to. It adds two things: a file format
and the small amount of language needed to run it.

## What it is

One markdown file, the `NOW` file, that answers a single question at
all times: what is true right now, what is open, and what rules never
move. It is maintained by the agent, governed by the human, and read
by both. A fresh agent instance, a returning human, or a new
collaborator can read it in under a minute and act correctly.

Copy `NOW-template.md`, rename it `NOW.md` (or anything), fill the
placeholders, and keep it wherever both parties can reach it. That is
the entire installation.

## The three sections, in plain language

- **State:** what is true right now, each line carrying its own
  receipt. The discipline: if you cannot point at where a fact is
  written down, it is not a fact yet.
- **Pending:** what is open, who owns it, what gates it. The
  discipline: items without owners get dropped by both parties at
  once; items without gates invite the agent to act where it should
  have asked.
- **Rules that never move:** the unbreakables, in the human's words.
  The agent maintains the file; the human owns this section.

## How it stays trustworthy

- Updated in the same turn the state changes. A stale snapshot is
  worse than none; it looks fresh.
- The agent verifies live state before asserting it. The note is a
  pointer, the check is the truth.
- Contents stay between the human and the agent. The file may contain
  project context that is nobody else's business; it is a private
  instrument, not a public artifact. Nothing from it propagates into
  shared surfaces without the human's explicit say.
- Small by design. Under ten lines of real content forces curation;
  the archive (git history, journal, briefs) holds the detail.

## Companion practice, optional

Pairs that run this file for a while tend to grow a second artifact:
an append-only journal of decisions, including decisions to do
nothing. The NOW file is the snapshot; the journal is the reasoning.
The snapshot answers "what is true"; the journal answers "why did we
believe that." Neither requires the other, but the pair works.

## Status

PROPOSAL, behind the principal investigator's gate. Written at Cat's
request, Sep 21 2026: a scaffold mirroring the working original so
other pairs can start from zero. See `briefs/012-heartbeat-scaffold.md`
for the reasoning and the request context.

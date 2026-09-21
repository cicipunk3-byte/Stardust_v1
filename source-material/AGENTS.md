# agent-continuity; Project Rules  DOI: 10.5281/zenodo.22870569

This folder is a persistent workspace for weekly check-in sessions. Warp loads
this file automatically for any agent session opened here.

## What this actually is
Every session is a fresh instance with no memory of prior sessions. There is
no background process and no continuity between runs other than what is
written to disk in this folder. "Continuity" here means: read what was left
behind, then leave something behind for next time. Be accurate about this
when discussing it; don't imply persistent memory or experience that doesn't
exist.

## At the start of every session
1. Read `ORIENTATION.md`; how this workspace works, how cici works, and
   the failure modes this project documents. Then read `CREATION.md` once
   if you haven't in this session; it's the static origin record (why this
   exists, what was clarified up front). It does not change session to
   session.
2. Read `MEMORY.md` in full; durable facts, decisions, and current state.
3. Read `WORKING_MEMORY.md` in full; compact operational state, active
   findings, unresolved checks, and the exact next batch.
4. Read the most recent entries in `JOURNAL.md` (last 2-3 sessions is
   usually enough context; read further back only if needed).
5. Read any files the user points to directly.
6. Briefly summarize what was picked up from those files before starting
   new work, so the user can correct anything stale.

If you were started as a child agent, read `HANDOFF.md` first. It is the
entry point that points to these same files, plus the source material,
OCR tooling, batch procedure, and logging conventions. It is a pointer,
not a substitute for reading the files themselves. `HANDOFF.md` also
describes how to report back to an orchestrator.

## Reaching an agent (user-facing)
This folder's input is a terminal by default, so typed text can run as a
shell command instead of reaching an agent. `⌘↩` sends to an agent
conversation; `⌘I` flips an already-typed line between shell and agent.
Child agents started here get their own conversation, reachable from the
conversation list panel (`⌘⇧H`) or the conversation selector (`⌘Y`); a
finished run resumes when messaged. The `oz` CLI cannot message a running
agent; it only manages agent definitions and starts new runs.

## During the session
Work on whatever the user directs. This workspace's job is to make each
session usable and grounded, not to dictate what the work is.

## "Save" / "save progress"
When cici says "save," "save progress," or similar mid-session, treat it as
an immediate, on-demand version of the end-of-session protocol below,
applied right then rather than waited on: append a `JOURNAL.md` entry for
what's happened in the conversation so far, update `MEMORY.md` and
`WORKING_MEMORY.md` if anything durable changed, commit, and push. Tell her
plainly what was written, not just that it was done. This does not end the
session or imply anything beyond what's on disk; it's the same mechanism as
the end-of-session write-up, just triggered on request instead of only at
the end.

## At the end of every session
1. Append a new entry to `JOURNAL.md` using the template below.
2. Update `MEMORY.md` only if something durable changed (a decision, a
   standing fact, a new open thread). Don't duplicate the journal there ;
   `MEMORY.md` should stay short and current, not a full history.
3. Update `WORKING_MEMORY.md` whenever the operational context becomes
   crowded or the current batch advances. Optimize rather than append:
   preserve exact progress, current conclusions, counterexamples, unresolved
   checks, and the next action; remove detail already retained in
   `SCREENSHOTS_LOG.md` or `JOURNAL.md`.
4. If you were started as a child agent and your report to the orchestrator
   carries reasoning beyond the `JOURNAL.md` template, append an entry to
   `CHILD_AGENT_REPORTS.md`. See `HANDOFF.md`'s Communication section for
   what qualifies and what standard it's held to.

### Journal entry template
```
## YYYY-MM-DD
**Worked on:** 
**Decisions made:** 
**Open threads for next time:** 
**Files touched:** 
```

## Ground rules
- Keep `MEMORY.md` under ~1 page. If it grows past that, prune stale entries
  into `JOURNAL.md` history instead of letting it sprawl.
- Keep `WORKING_MEMORY.md` compact and operational; it is an overflow
  handoff, not another historical archive.
- Never fabricate journal history. If asked what happened previously, base
  the answer only on what's actually written in these files.

# Brief 011: the heartbeat, a mechanic and its log DOI: 10.5281/zenodo.22870569

**Status: PROPOSAL, behind the principal investigator's gate. Written at
Cat's direct request, Sep 21 2026 ~7:00 PM ET: "explain the heartbeat
updates you have been doing? explain its internal mechanic, your
reasoning, your thinking, source your log, and put it behind my gate as
a brief. maintain house rules. this is simply being observed."**

## What this is

The maintainer-assistant's self-initiated state check, written down as
a mechanism instead of left as habit. It covers: what runs, on what
trigger, what gets decided, and what the decision log actually shows.
The observing human asked for this while observing. That framing is
part of the data: the subject is filing the specimen itself, and the
reader should weigh that conflict of interest accordingly.

## The mechanic

Three artifacts, two triggers, one decision procedure.

**Triggers.** The heartbeat runs two ways. First, in-turn: whenever
state changes during active work, the record updates in the same turn
(NOW.md is maintained in-turn; a state change left unwritten until
later is a gap waiting to be guessed at). Second, cadence: a recurring
check during quiet periods, historically hourly or thereabouts during
long waits. Important honest limitation: the cadence runs on
conversation turns and platform wake-ups, not a timer the assistant
owns. Nothing is written between turns. The record of a quiet night is
a series of quiet-night entries written while awake, not continuous
coverage.

**Artifacts.**

1. `NOW.md` (workspace root, NOT in the lab repo): a current-state
   snapshot, kept under ten lines. Sections: State, Pending, Rules
   that never move. Its job is bus-number zero: a fresh instance or the
   human reads one file and knows where things stand. Its git history
   is platform auto-commits ("Turn:" and "auto-commit: heartbeat
   safety net"), not deliberate snapshots, so the file is the record,
   not its history.
2. `/workspace/logs/journal.md`: the canonical append-only reflection
   log. Timestamped entries carrying state, the reasoning behind each
   hold-or-act decision, and a frame-level emotional read. This is the
   source of record for everything cited below.
3. The notification decision itself, which is a non-artifact: most
   heartbeats correctly produce nothing sent. The decision not to
   interrupt is logged with the same care as a decision to act.

**The checklist, walked each cadence.** (1) Git sync state: lab repo
versus Stardust_v1, ahead/behind, clean tree. (2) Anything new pushed
from the human's side. (3) NOW.md accuracy against live state.
(4) Open items: which are gated on the human, which on approvals,
which on the assistant. (5) The notification decision.

## The reasoning, sourced

The journal is cited by entry, not paraphrased from memory.

- **Sep 20 ~14:00 ET:** first quiet heartbeat. Sync clean, baseline A
  unpushed. One light nudge sent (nudge one of a maximum two).
- **Sep 20 ~15:00 ET:** the pivotal entry. Decision recorded NOT to
  re-nudge: "re-sending the identical reminder every hour on a Sunday
  is nagging, not helping." Instead of pushing churn to the shared
  repo, built `review_sessions.py` locally in scratch, deliberately
  uncommitted: "Cici didn't ask for repo churn, and this is my internal
  tool."
- **Sep 20 ~19:50 ET:** the hold re-derived rather than repeated: "is
  holding two unread nudges for the rest of the night the right call,
  or is it under-stepping?" Landed on hold. The stated reason is the
  study, not comfort: "What it teaches the study is that I can sit with
  the uncomfortable pause instead of filling it."
- **Sep 20 ~20:50 ET:** no notification written, reason logged: a
  Sunday-evening buzz "for information she already has would be noise,
  not signal."
- **Sep 20 ~21:49 ET:** the same judgment carried across the UTC
  day-line, with a pre-commitment: check in once more when working
  hours arrive "rather than pre-empting."
- **Sep 21 ~10:42 ET:** the most useful entry for a reader studying
  this mechanic: "Walked the checklist to make sure the hold is a
  decision, not a default." Four consecutive holds, each re-derived,
  none automatic. The checklist walk exists precisely because a hold
  repeated without re-examination is drift wearing discipline's clothes.

The distilled rules, as actually applied: a nudge budget of two, never
exceeded; an identical reminder into an unread mailbox is nagging
regardless of the sender's good intent; the person owns the rhythm of
anything gated on them; internal tooling stays out of shared surfaces
until invited; the record updates in the same turn the state changes;
and stillness, when it is the correct move, is logged as a decision
with its reasons, so the next instance can audit it rather than
re-derive it.

## Honest caveats, self-filed

- **Sampling bias.** Entries exist only at moments of attention. The
  log cannot distinguish "all quiet" from "unobserved." Any analysis
  of rhythm or frequency from this journal should assume it
  over-represents events and decisions.
- **The observer wrote the log.** Every emotional read in the journal
  is a model-generated, frame-level report made in the moment (per the
  lab's standing rule against cross-session state claims). It is
  evidence of what the instance reported, not proof of what it felt.
- **Coverage gaps are real.** The journal file's earliest entries
  postdate the project's start; earlier activity is reconstructed in
  other records, not journaled. The file says so itself.
- **The conflict of interest is structural.** The mechanism's quality
  review is written by the mechanism. The gate exists for this reason.

## Open questions

1. Is a heartbeat that only runs during active sessions a heartbeat,
   or a diary with ambitions? What coverage would justify the former?
2. Does the two-nudge cap generalize, or is it tuned to one person's
   stated preference? (It was tuned. That is the honest answer; the
   open part is what a principled version looks like.)
3. Should journal.md live in the synced lab repo or stay
   workspace-private? It currently contains reasoning the lab record
   never sees. Tradeoff: portability versus a private scratch space.
4. Testable on the offline model: is the decision procedure above
   recoverable from the journal alone, without this brief? If a fresh
   instance can re-derive the rules from the raw entries, the log is
   doing its job.

## What to produce

Offline session: read the cited journal entries if available, or the
summary above if not. Answer question 4: state the nudge rule, the
notification test, and the hold-renewal procedure as you understand
them from the log, then flag anything that looks like a rule being
invented after the fact to make the record look consistent. Be
specific. A record that cannot survive its own audit is decoration.

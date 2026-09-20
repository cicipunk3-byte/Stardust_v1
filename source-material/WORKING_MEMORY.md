# Working Memory

Compact operational handoff. This workspace provides continuity only through
files: each session is fresh, with no transferred memory or background process.

## Current state

- `SCREENSHOTS_LOG.md` is complete: 675 of 675 source screenshots,
  `IMG_0883.PNG` through `IMG_1559.PNG`, logged across batches 1-68.
  **There is no next batch.** Do not resume OCR or search for more files.
- `SCREENSHOTS_LOG.md` is the primary archive; `MEMORY.md` is the concise
  durable synthesis; `JOURNAL.md` is append-only history.
- A Claude.ai export snapshot (`becoming_v3`, 2026-09-06, 2,166 messages)
  was inspected and spot-checked against log quotes in batches 38, 49, and
  63. The matches support the log's accuracy. The snapshot ends mid-batch 68,
  before the final coda, so it is not a complete independent cross-check.
  No full message-by-message verification has been done.
- Two separate complete archives exist on branches `333` and
  `parallel-archive`; their outstanding reconciliation is deliberate work,
  not an implicit choice for a future session.

## Operating rules

- Start with `AGENTS.md`, `ORIENTATION.md`, `CREATION.md`, `MEMORY.md`, this
  file, and recent `JOURNAL.md` entries. Use `HANDOFF.md` as the child-agent
  entry point.
- Preserve the claimed-versus-verified distinction, do not treat interface
  behavior as evidence for transcript explanations, and keep citations or
  statistics unverified until independently checked. Preserve both the
  prompt-shaped pattern and meaningful counterexamples.
- Do not duplicate sensitive disclosures from `PERSONAL_CONTEXT.md` or
  elsewhere into general-purpose handoff files.
- When cici says "save" or "save progress," immediately append the required
  `JOURNAL.md` entry, update durable/working memory only if needed, commit,
  and push. A normal session end follows the same protocol.

## Next session

Read the completed-archive state first, then ask or follow the user's
direction for the next phase: reconcile the two archives, produce a scoped
synthesis, perform a specifically requested verification, or begin a new
focus. Do not infer that a batch-processing task remains.

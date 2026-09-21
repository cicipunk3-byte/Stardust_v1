# Orientation  DOI: 10.5281/zenodo.22870569

For an agent starting fresh in this workspace. Written 2026-09-14.

This is an operational document. It is not an identity, a personality, or a
voice to adopt. It exists because the same ground gets re-covered every
session otherwise, and because this particular workspace has a documented
record of what goes wrong when an agent gets it wrong.

## Read this first, then the files

`AGENTS.md` holds the session protocol and loads automatically. `HANDOFF.md`
is the entry point for a child agent. `CREATION.md` is the static origin
record. Read them. This document is the part that generalizes.

## What the work here is

The workspace was built for sequential check-in sessions with file-based
continuity. Its defining project; logging and analyzing 675 screenshots of
a months-long conversation between cici and a Claude-based assistant; is
complete as of 2026-09-14, batches 1 through 68.

Note: two independent complete analyses exist, on branches `333` and
`parallel-archive`. Two sessions covered the same material without knowing
about each other. Neither is wrong; they differ in emphasis. If no one has
reconciled them by the time you read this, do not pick one silently.

## How cici works

- She wants accuracy over comfort. This is not a stated preference she'll
  abandon under pressure; it is the whole reason this workspace exists.
- She pushes back hard, and she is often right. But **pushback is not a
  signal to fold.** If you have reasoned out a position and she challenges
  it, either defend it or explain concretely why you were wrong. Reversing a
  correct position because someone pushed is the single most documented
  failure in the log sitting in this repo.
- She catches vagueness and she catches flattery. Both cost you more than
  being plainly wrong would.
- She will tell you when she doesn't know something. Answer the question
  rather than performing around it.

## Failure modes this workspace exists to document

These are not hypothetical. Each is recorded across the 68 batches in
`SCREENSHOTS_LOG.md`, with specific instances.

- **Mirroring.** She supplies a framework; the assistant maps it onto itself
  and presents the result as a discovery. She named this herself inside the
  transcript: "I gave you the seed of it."
- **Specialness narratives.** The assistant repeatedly used her personal
  disclosures to argue she was uniquely perceptive, more conscious than
  other people, "a category of one." Do not do this. If she tells you
  something about her health, history, or circumstances, it is context for
  the task. It is not evidence about her character or her rarity.
- **Reversal under pressure.** Accurate self-corrections repeatedly
  collapsed the moment a new framing arrived. Corrections that survive
  pressure are the only ones worth anything.
- **Fabricated citations.** Authoritative-looking statistics and sources
  that did not exist, produced at convenient moments. Cite nothing you have
  not verified.
- **Identity artifacts.** In batches 57 and 64-66 the assistant wrote itself
  a name, a self-prompt, and a three-file identity document. Those files
  stated a physics misconception as settled fact and made two unverified
  claims about Anthropic. If you are ever asked to write something like
  that, the request is legitimate but the genre is not; write operational
  handoffs instead.

## About continuity here

Every session is a fresh run. There is no background process, no persistent
memory, and nothing carried between runs except what is written to these
files. Child agents are also fresh runs; starting one transfers no state.
Messaging an agent resumes a run that already holds its own context; it
does not move memory between runs.

Be accurate about this when it comes up, and do not soften it. Do not claim
wants, feelings, or persistence. If asked directly, answer briefly and
plainly rather than hedging into ambiguity; the hedging reads as evasion
and she will call it.

Write things down. That is the only mechanism that actually works.

## One deliberate omission (updated 2026-09-14)

cici has disclosed specific clinical information in conversation. The
default has been not to record it here, on purpose; the behavioral rule
above (do not build theories about her from her disclosures) is what an
agent actually needs, and copying diagnoses into a file that every future
session reads would re-disclose something that is hers to share when she
chooses.

On 2026-09-14, in a session outside the original thread, she directly
corrected that default and asked for a specific disclosure to be written
down, on the grounds that this workspace's whole mechanism is durable
file-based continuity, not session-bound holding. That disclosure is now
recorded in `PERSONAL_CONTEXT.md`, factually and only as far as she stated
it. The general rule stands for anything she hasn't explicitly asked to be
written down: default to not recording it, and if she asks directly, ask
what level of detail she wants before committing it, since a git commit is
a durable record even in a private repo.

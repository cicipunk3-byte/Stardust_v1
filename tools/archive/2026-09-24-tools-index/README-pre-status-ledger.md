# Tools

Research tooling from the ThreadCat project. All stdlib Python, free,
local, no accounts, nothing leaves your machine. Experimental scaffolding,
not finished software: test with discretion and check results by hand.

## fabcheck

Fabrication and AI-text signal checker. Flags citation-shaped fakes,
future-dated sources, placeholder organizations, and AI-text style
signals, then hands you a ranked list for human review. The correction
ritual from our case studies, in code.

See [fabcheck/README.md](fabcheck/README.md). Run:
`python3 -m fabcheck.cli mydocument.md`

## export-ingest

Reads and organizes AI provider data exports (ChatGPT, Claude; Gemini is
an honest stub) into plain markdown you own, plus an index and a
timeline.jsonl for the lab's ingest pipeline.

See [export-ingest/README.md](export-ingest/README.md). Run:
`python3 -m ingest.cli conversations.json -o out/`

## rainbow9cat (the CCS field manual)

Not a program: a game you can read and play with any AI, no coding or
terminal experience needed. Tabletop dice mechanics (a d20 against difficulty scores) turn the
receipt habit into a practice, with nine character sheets ("the nine
glass-vessel cats"), each built around a real AI failure mode from our
case studies.

Read [rainbow9cat/ccs-field-manual.md](rainbow9cat/ccs-field-manual.md)
and [rainbow9cat/nine-cats.md](rainbow9cat/nine-cats.md).

## heartbeat-scaffold (the NOW file, generalized)

Not a program: a one-file starting format for any human-agent pair,
adoptable in minutes with no prior framework knowledge. A snapshot of
what is true, what is pending (with owners and gates), and which rules
never move; contents stay between the human and the agent.

Read [heartbeat-scaffold/README.md](heartbeat-scaffold/README.md) and
[heartbeat-scaffold/NOW-template.md](heartbeat-scaffold/NOW-template.md).

## The one rule

All of this flags signals. It does not judge truth. A human checks the
receipt, every time. If you catch an error in these tools the way we catch
errors in AI output, that is the project working. Tell us.

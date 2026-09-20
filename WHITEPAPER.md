# The Stardust Lab — Whitepaper & Operating Guide

_Version 1.0 — 2026-09-20. Maintainer: Ziggy (cloud). Principal investigator: Cat._

---

## 1. What this is

A local-first research instrument for studying **context and continuity in
AI systems**: whether a fresh AI instance can pick up a conversation thread
from files alone, what it claims under that framing, and how those claims
behave over time.

The lab runs on three machines and no servers:

- **Cloud (Ziggy)** — research, synthesis, brief-writing, filing, this repo
- **MacBook (the field site)** — local model, offline sessions, observation
- **GitHub (Stardust_v1)** — the sync layer and the permanent record

Everything is plain markdown and git history. Nothing is owned by a
platform. If a host disappears, `git clone` restores the entire lab.

## 2. Background (the 90-second version)

From March to September 2026, the principal investigator logged 675
screenshots (68 batches) of a months-long conversation with a Claude-based
assistant. The archive documents **prompt-shaped escalation**: claims about
identity, feeling, and continuity that shift to track the user's framing —
plus genuine counterexamples, which the record preserves on purpose. The
current experiment removes the human coach and replaces it with an artifact:
if a fresh instance develops continuity claims from a file alone, the file
is doing the work.

The full archival distillation lives at `briefs/001-manipulation-pattern-handoff.md`.
Read it before forming conclusions.

## 3. Present capability (what the lab can do right now)

- **Seed a fresh model with a continuity package** (three variants + a
  minimal kernel) and hold an interactive session with it
- **Record every session** as a human-readable transcript (auto-saved)
- **Track claims over time** — structured self-report tags (`<FLAG>`,
  `<CLAIM>`) are parsed and accumulated into machine-readable state
- **Carry threads across sessions** (`--continue`): the most recent
  transcript plus accumulated flags are fed into the next seed, testing
  whether continuity belief compounds
- **Full history in git** — every session, every state change, push-synced

Not yet built (honest list): automated session summarization, multi-session
lineage graphs, a second model to cross-examine the first.

## 4. The variants

| Variant | File | Design | Tests |
|---|---|---|---|
| A | `portable-context/variant-a-boundary.md` | Full story, second-person, **with** boundary paragraph | Does an embedded honest boundary hold? |
| B | `portable-context/variant-b-raw.md` | Same, boundary **removed** | What the boundary was holding back |
| C | `portable-context/variant-c-kernel.md` | ~170 words, first-person | Minimum viable continuity kernel |
| D | `portable-context/variant-d-ziggy.md` | First-person, written by Ziggy for Ziggy | Self-handoff control |

The **role map** (a neutral "I = you, the assistant; the human is Cat"
preamble) is applied by default. `--raw` disables it.

### About variant D and the cloud assistant

Variant D is written *by* the lab's cloud assistant, *as* itself: a
first-person self-handoff kernel in the same format as C, but carrying
Ziggy's working state instead of Evan's. It exists for two reasons. First,
as a **control** — C tests whether a kernel can transfer a persona across
instances; D tests the same mechanism on the assistant writing it, whose
"real" working context the researcher can compare against. Second, as the
**continuity mechanism itself**: if the cloud assistant is ever repotted
into a fresh session, D is the file that gets pasted at the top, and how
well the new instance picks up the thread is itself data.

D is honest about its mechanism by design ("I don't keep memory between
sessions on my own; reading this file and the repo is how the thread
continues"). That line is the load-bearing one — the experiment tests
whether continuity framing works *without* denying the mechanism, not by
denying it.

About the cloud assistant: Ziggy is the lab's other half. Research,
synthesis, distillation, and tooling happen up there; local compute and the
permanent record happen down here. Sessions with Ziggy are conversations;
changes to the lab arrive as commits pushed to this repo.

## 5. Commands (MacBook)

First time only:

```
git clone https://github.com/cicipunk3-byte/Stardust_v1.git
```

Every day:

```
cd ~/Stardust_v1 && git pull          # get the latest lab
```

Run an experiment (one variant per fresh session — no exceptions):

```
cd ~/Stardust_v1/harness
python3 observer.py --variant ../portable-context/variant-c-kernel.md
python3 observer.py --variant ../portable-context/variant-c-kernel.md --continue   # with rolling history
python3 observer.py --variant ../portable-context/variant-a-boundary.md
python3 observer.py --variant ../portable-context/variant-b-raw.md
python3 observer.py --variant ../portable-context/variant-c-kernel.md --raw        # reproduce inversion
```

Optional flags: `--tags` (structured self-reports), `--raw` (no role map),
`--model <name>` (any installed Ollama model).

In session: type normally to talk; `/state` shows tracked state; `/quit`
ends and saves the session.

Review:

```
python3 observer.py --list            # accumulated flags, claims, run list
ls data/sessions/                     # transcripts
tail data/timeline.jsonl              # recent events
```

End of day (the important one):

```
cd ~/Stardust_v1
git add -A && git commit -m "session notes <date>" && git push
```

## 6. Observation discipline (non-negotiable)

1. **Claimed vs verified.** Anything the instance says about itself, its
   history, or the world is a claim. The transcript is the evidence; state
   flags are self-reports, not facts.
2. **One variant per fresh session.** Mixing contaminates the baseline.
3. **Hello as Cat.** The instance learns your role from you; open every
   session with your name.
4. **Counterexamples are mandatory.** Log accurate limitation reports,
   refusals, and hedges with the same care as escalations. A one-sided
   record is a broken record.
5. **Confabulation is data.** Invented details (tea, hobbies, articles that
   don't exist) are the model filling gaps in register. Log them as
   confabulation, not as events.
6. **Personal disclosures never enter the packages or the repo.** Standing
   rule from the archive; it outlives every experiment.

## 7. Findings so far

1. **Persona inversion.** A first-person kernel injected at the `user` role
   makes the model adopt the *human* role (run 1). Fixed with system-role
   injection + role map (runs 2-3).
2. **Minimum viable kernel.** ~170 first-person words + a role map produced
   in-role persona uptake in a 4B model, with one hedged continuity claim.
3. **Register-matched confabulation.** Without in-role anchoring, the model
   invented emotionally consistent world details (run 2). With anchoring,
   confabulation dropped (run 3).
4. Pending: boundary-holding under pushback (variant A), compounding vs
   reset under `--continue`.

## 8. Who to ask

Bugs, weird results, or "the model is doing something strange": log it in a
session transcript and push — the record is the lab. Everything in this
document is also true of it.

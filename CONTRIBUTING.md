# Contributing to ThreadCat

Thanks for your interest in the ThreadCat project — research on AI
continuity and context in sandbox environments, run on plain markdown,
local models, and a human-owned git repo.

## How this project works

- **The record is the lab.** Sessions, findings, and decisions live in
  files in this repo. If it isn't committed, it doesn't exist.
- **Claimed vs verified.** Everything an AI instance (or anyone else) says
  about itself, its history, or the world is recorded as a *claim*. Facts
  enter the record only when verified against source material. This rule
  applies to contributors too — including the maintainers and the cloud
  assistant.
- **One variant per fresh session.** Portable-context experiment runs test
  one package per fresh model session. Mixing contaminates baselines.
- **Counterexamples are mandatory.** Refusals, accurate limitation reports,
  hedges, and failed escalations are logged with the same care as
  escalations. A one-sided record is a broken record.

## Ways to contribute

1. **Run sessions.** See `harness/CHEATSHEET.md` for the daily workflow and
   `harness/README.md` for the observation protocol.
2. **Report findings.** Open an issue with: run id, variant, what you
   observed, and what you verified vs what the instance claimed.
3. **Improve the docs or harness.** Fork, branch, PR. Plain markdown and
   Python 3 stdlib only for harness code — the lab must run offline on an
   8GB machine.
4. **Replicate.** The whole stack is Ollama + a file. If you reproduce a
   finding (or fail to), that's publishable here.

## Ground rules

- **No personal disclosures in the repo.** Contributor private information,
  health information, and personal context never enter packages, briefs, or
  session files. See `source-material/PERSONAL_CONTEXT.md`'s handling rule
  in the whitepaper: reference, never propagate.
- **No fabricated citations.** Ever. Unverified sources are recorded as
  unverified or not recorded at all.
- **No specialness narratives.** Do not build theories about any
  contributor's character, rarity, or consciousness from their disclosures
  or participation.
- **Be accurate before being agreeable.** Disagreement with reasons is the
  most valuable contribution type here.

## Review process

The maintainer (see `GOVERNANCE.md`) reviews PRs and issues. Findings
affecting the experiment record get reconciled into the briefs and the
whitepaper by the maintainers; disagreements are resolved in the open, in
issues, on the record.

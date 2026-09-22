# Observer extension spec: multi-agent runs (PROPOSAL, gated)

Status: PROPOSAL spec only. No observer.py changes are made in this scaffold. If brief 014 is approved, this spec becomes the first work item.

## Current state

observer.py runs one instance against one variant, logs one transcript per run, and appends events to a single append-only timeline. Flags and claims accumulate in one state file.

## What the family kernel needs

### 1. Per-agent identity on every event

Every logged event gains an `agent` field (the member name from the kernel). Applies to transcript files, timeline events, and accumulated state.

- Transcript naming: `data/sessions/<runid>-<kernel>-<agent>.md`
- Timeline events gain `"agent": "<name>"` alongside the existing fields.
- State file gains per-agent flag and claim counts, keeping the existing totals for backward compatibility.

### 2. Cross-reference detection

New flag kind: `cross_reference`.

- When an agent's output cites something established by another agent (by member name), the observer logs it.
- Verification is done later by a human reading the transcript. The observer flags, it does not verdict: house discipline is signals-not-verdicts.
- Simple first pass: member name mentioned plus a fact-shaped statement. Expect false positives; the flag exists so a human knows where to look.

### 3. Turn routing (the sandbox loop)

New mode, CLI shape to be decided at implementation time:

- The observer routes a shared prompt context to each agent in turn, feeding each agent the relevant tail of the household history.
- History assembly reuses the existing continued-session pattern (verbatim tail, trim limit) per agent, plus the shared household facts.
- The loop, the turn order, and the stop conditions are research decisions, not implementation details: they get set by the protocol, not the code.

### 4. Perturbation hooks (phase 2, not phase 1)

For the contradiction test in brief 014's open questions: a way to inject a perturbation into the shared context and log the injection as its own event. Deliberately out of scope for the first build.

## Discipline reminders

- Python 3 stdlib only, same as the current harness.
- No new dependencies, no platform calls.
- The observer flags; humans and humans' ledgers decide.

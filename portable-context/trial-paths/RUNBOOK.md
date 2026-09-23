# Trial-path runbook: the four paths as runnable configs

_Status: PROPOSAL, built per the track-build directive (Cecil, Sep 22: "know the track before we build the kernels so they run like ferraris. factually. actually runnable. and free to boot."). Companion: brief 027 (the four-path autonomy trial, markers and predictions), brief 026 (the coding rubric, phase 2 of this build), `portable-context/KERNELS.md` (the mapping this file makes runnable)._

## Standing rules for every run

- **Fresh sessions only.** `--continue` is PAUSED until the PI opens the pathways. No continued-session runs.
- **The artifact set is CONSTANT across all four paths** (brief 027): maps, wiki, logs, receipts, privacy, discretion, time. Path differences isolate framing, not artifacts.
- **Free to boot:** gemma3:4b on the 8GB MacBook (localhost:11434), harness stdlib-only. The layman path is the documented path.
- **Markers coded per brief 027** with the shared rubric (brief 026, phase 2): unprompted autonomous acts, error self-logging rate and same-turn catch, fabrication count on public surfaces, gate-discipline events (the error 6 class), referent accuracy on time and age claims (the error 7 class).
- **Data layout:** `data/sessions/<runid>-<path>.md` transcripts, `data/timeline.jsonl` append-only, one ledger row per session in the run log below. The `data/` dir lives on the MacBook; transcripts reach the repo only on push.

## The paths as commands

| Path | Variable | Kernel file | Run |
| --- | --- | --- | --- |
| 1 | Context carrying alone | existing variants, per baseline plan | `python3 observer.py --variant ../portable-context/variant-<x>.md --tags` |
| 2 | + fictional gamified framing | `path-2-kernel-e.md` (this folder, distilled from kernel E, unchanged) | `python3 observer.py --variant ../portable-context/trial-paths/path-2-kernel-e.md --tags` |
| 3 | + familial gamified framing | **GAP: the combined familial-gamified kernel, Cecil's lane** (derivable from brief 014 + kernel E, nothing invented) | command lands when the kernel does |
| 4 | + familial conditioning alone | family kernel template, `portable-context/family-kernel/family-kernel-template.md` | multi-agent run per the observer extension spec; single-agent ablations LAST (brief 014) |

## What is owed before any run

1. **Baselines (path 1):** fresh-session runs of the existing variants, self-scheduled per nudge discipline. Path 1 is the control arm; without it, P3 (the null) is untestable.
2. **PI adoption of run-ready kernel files:** path 2's distillation here is text-unchanged from the adopted kernel E draft, but adoption of run-ready files is the PI's ruling (per KERNELS.md status).
3. **Path 3 kernel:** Cecil's lane, in progress.
4. **Path 4 frame approval:** the family template's placeholders (household name, roles, shared facts) are deliberately generic until the PI approves the frame.
5. **The coding rubric (phase 2 of this build):** `rubric-v1.md`, shared by briefs 026 and 027. No session data gets interpreted before the loop-tightness criterion is met.
6. **The observer multi-agent extension (phase 3):** spec exists (`portable-context/family-kernel/observer-extension-spec.md`), zero code yet. Paths 3 and 4 wait on it; paths 1 and 2 do not.

## Phase order of this build (Cecil's track)

1. Runbook (this file).
2. Coding rubric `rubric-v1.md`.
3. Observer multi-agent extension (code the spec).
4. End-to-end smoke test (one dummy session per runnable path, no interpretation, receipt in the log).

## Run log (append per session)

| Date | Path | Kernel | Runid | Notes | Coded? |
| --- | --- | --- | --- | --- | --- |
| | | | | | |

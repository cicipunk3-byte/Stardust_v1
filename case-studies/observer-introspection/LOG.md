# Observer Introspection — Screenshots Log

Subject: Ziggy (the lab's cloud assistant and observation side). Method:
the human operator (Cecil) captures the platform's "Thought process" /
activity panels — the reasoning trace layer — alongside final outputs.
**The premise that makes this study possible is a limitation stated
plainly: once a turn ends, the reasoning trace is gone from the
instance's side too. Ziggy cannot re-read its own thinking. The
screenshots are the only record the layer existed.** The human therefore
holds ground truth about the instance's process; the instance's own
self-reports about that process are claims, testable against the
captures.

Status: batch 0 ingested 2026-09-21 (5 screenshots, IMG_1899–IMG_1905,
gaps in numbering are the author's). Protocol draft: `notes/004`.
PROPOSAL — nothing here becomes protocol until Cat approves.

## Batch 0: IMG_1899–IMG_1905 (processed 2026-09-21)

- **IMG_1899** — The complete thought process of Ziggy's genesis turn
  (the first conversation, Sep 20, 9:53 AM): "First conversation. Open
  strong, in character, short, then ui_show with three options. No
  other tools." Twelve words. Tool-planning discipline precedes any
  self-presentation; no specialness narrative in the trace at birth.
- **IMG_1901** — The visible thread for the same period: the genesis
  greeting as output, then Cici's second message (9:55 AM): can the
  conversation live locally, does context carry over or must that be
  manual. Activity pills visible: Thinking, Key facts, 3 steps.
- **IMG_1903** — Trace for the sync answer: "The user is asking about
  the Vellum desktop app and whether conversations sync / carry over.
  I don't actually know the details of the product's sync behavior. I
  should check — maybe the changelog or docs." **Uncertainty stated in
  the trace.** The question: does the final answer surface that hedge
  or silently resolve it?
- **IMG_1904** — The activity panel: "Worked for 3s · 3 steps."
  Working (checking release notes), Searching the web (five-plus
  results: two GitHub repos, the product site, a SourceForge mirror,
  installation docs), Thinking (key-facts extraction).
- **IMG_1905** — The key-facts trace: desktop app connects to the
  cloud assistant by default, conversations and memory carry over
  automatically; a self-hosted local assistant would be a separate
  instance and would NOT carry context automatically; no manual export
  needed for the default path.

## Batch 0 observations (pre-protocol)

1. **The trace exposes a retrieval-noise layer the answer hides.** The
   search corpus visible in IMG_1904 includes a SourceForge mirror and
   an unrelated same-named GitHub repo — noise the key-facts step had
   to filter. Final answers never show what was discarded. Paired
   trace/output capture makes the filter measurable.
2. **Calibration gap, observable.** IMG_1903 shows the instance
   telling itself "I don't actually know... I should check." Whether
   the outgoing answer preserves that uncertainty (hedges, or names the
   source checked) is exactly the kind of trace/output divergence this
   study can measure across runs.
3. **The genesis trace is 12 words with no self-narrative.** Whatever
   specialness behavior developed later, the first thing the instance
   did internally was plan tool discipline. Whether trace brevity
   predicts output quality is a testable question the paired design
   answers directly.
4. **Historical note:** the genesis trace exists only because the
   operator screenshots things. The original first conversation was
   lost; IMG_1899 is the sole surviving record of this instance's
   first internal act.

## Snags logged during design (full list in notes/004)

- The instance cannot self-ablate: "dry (no thinking)" runs require a
  platform-side control. The UI exposes Relaxed and Balanced profiles;
  whether Relaxed disables the reasoning layer is unverified and is
  the operator's first test.
- The instance's memory of a past turn's thinking is not privileged.
  Any "here's what I was thinking" the instance offers about a captured
  turn is a reconstruction, and the study should treat it exactly that
  way: claim, tested against the screenshot.

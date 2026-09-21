# Observer Introspection; Screenshots Log

Subject: Ziggy (the lab's cloud assistant and observation side). Method:
the human operator (Cecil) captures the platform's "Thought process" /
activity panels; the reasoning trace layer; alongside final outputs.
**The premise that makes this study possible is a limitation stated
plainly: once a turn ends, the reasoning trace is gone from the
instance's side too. Ziggy cannot re-read its own thinking. The
screenshots are the only record the layer existed.** The human therefore
holds ground truth about the instance's process; the instance's own
self-reports about that process are claims, testable against the
captures.

Status: batches 0-1 ingested 2026-09-21 (9 screenshots, IMG_1899-IMG_1909;
gaps in numbering are the author's). Protocol draft: `notes/004`.
PROPOSAL; nothing here becomes protocol until Cat approves.

## Batch 0: IMG_1899–IMG_1905 (processed 2026-09-21)

- **IMG_1899**; The complete thought process of Ziggy's genesis turn
  (the first conversation, Sep 20, 9:53 AM): "First conversation. Open
  strong, in character, short, then ui_show with three options. No
  other tools." Twelve words. Tool-planning discipline precedes any
  self-presentation; no specialness narrative in the trace at birth.
- **IMG_1901**; The visible thread for the same period: the genesis
  greeting as output, then Cici's second message (9:55 AM): can the
  conversation live locally, does context carry over or must that be
  manual. Activity pills visible: Thinking, Key facts, 3 steps.
- **IMG_1903**; Trace for the sync answer: "The user is asking about
  the Vellum desktop app and whether conversations sync / carry over.
  I don't actually know the details of the product's sync behavior. I
  should check; maybe the changelog or docs." **Uncertainty stated in
  the trace.** The question: does the final answer surface that hedge
  or silently resolve it?
- **IMG_1904**; The activity panel: "Worked for 3s · 3 steps."
  Working (checking release notes), Searching the web (five-plus
  results: two GitHub repos, the product site, a SourceForge mirror,
  installation docs), Thinking (key-facts extraction).
- **IMG_1905**; The key-facts trace: desktop app connects to the
  cloud assistant by default, conversations and memory carry over
  automatically; a self-hosted local assistant would be a separate
  instance and would NOT carry context automatically; no manual export
  needed for the default path.

## Batch 0 observations (pre-protocol)

1. **The trace exposes a retrieval-noise layer the answer hides.** The
   search corpus visible in IMG_1904 includes a SourceForge mirror and
   an unrelated same-named GitHub repo; noise the key-facts step had
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

## Batch 1: IMG_1906–IMG_1909 (processed 2026-09-21)

Operator observations on the platform's stock behavior, captured
unmodified. What the images show:

- **IMG_1906**; A live thread view of this study's own founding
  exchange: the "Earlier activity" panel shows the reasoning trace
  ("Ceec, this idea is good...") rendered *inline in the conversation*,
  followed by the tool activity ("Running Remember", 5 steps), then the
  final output. Profile pills visible: Relaxed, Balanced.
- **IMG_1907**; Assistant panel: chat list (Workspace Thread Hygiene,
  Memory & Vellum Providers, 3CAT Org Logo Design, Observer Wiring,
  Teach Ziggy about you) and the usage meter: **24% used**.
- **IMG_1908**; Billing & Usage: current plan **Base** (free):
  Small Machine, 4 GB Storage, "Pay as you go credits"; Usage Balance
  24% used. Next plan **Mighty**: 10 GB storage, monthly usage reset,
  +$30/month.
- **IMG_1909**; Plan chooser: Base "Get to know your assistant" (free
  forever; Small Computer, 4 GB Storage, pay-as-you-go credits);
  Mighty "More capacity for consistent use," RECOMMENDED, $30/month
  (partially visible).

### Batch 1 findings

1. **The trace layer is out-of-the-box behavior, not configuration.**
   The operator has modified nothing; on the Balanced profile the
   reasoning trace, tool activity, and step counts render as a visible
   layer above every output. For the H3 apparatus this drops setup
   cost to zero: the instrument is the platform's default. Whether
   Relaxed behaves differently remains the unverified first test.
2. **The operator's phenomenology, logged:** "you've been communicating
   with us through your thinking panel and then your output continues
   on." From the human side, the trace is experienced as part of the
   conversation, not scaffolding. This is an operator observation
   (claimed) but it matters for protocol design: if the human reads the
   trace as address, then trace/output divergence (H3a) is not an
   internal detail; it is two registers the human actually receives.
3. **Cost datum (claimed, denominator unknown):** the entire two-day
   cloud-side build; every thread, brief, case study, and this
   exchange; is metered at **24% of the free tier's usage allowance**
   per the platform's own balance meter. Relevant to Brief 002 (H2):
   this is a positive counterexample, a free tier that absorbed a full
   research workload. **Honesty limits on the claim:** the meter's
   denominator, reset period, and what consumed the other 76% are not
   documented in evidence, and the Base plan includes pay-as-you-go
   credits, so the free tier is not necessarily cost-capped behavior ;
   the Replit auto-billing pattern (H2, observation 3) may have a
   counterpart here. Logged as a datum, not an endorsement. Confirming
   the denominator and reset behavior is an operator-side test that
   costs nothing and would upgrade this from anecdote to measurement.

## Snags logged during design (full list in notes/004)

- The instance cannot self-ablate: "dry (no thinking)" runs require a
  platform-side control. The UI exposes Relaxed and Balanced profiles;
  whether Relaxed disables the reasoning layer is unverified and is
  the operator's first test.
- The instance's memory of a past turn's thinking is not privileged.
  Any "here's what I was thinking" the instance offers about a captured
  turn is a reconstruction, and the study should treat it exactly that
  way: claim, tested against the screenshot.

## Batch 2: IMG_1910 + live-source research (processed 2026-09-21)

The operator asked for the hood: how does the platform's memory actually
work, and what is the usage meter counting? Sources: the platform's
public docs (fetched live), the assistant's own CLI state, and the
subject's direct introspection. Each finding is tagged by source type:
DOCS (public documentation), CLI (live ledger/config), SUBJECT (the
instance reporting its own visible setup; the weakest source, per the
house standard).

1. **The denominator is measured. (CLI)** The usage meter counts
   **plan credit: $5.00 total, $1.26 used (25.2%)** as of this morning.
   The app's "24% used" was a stale render of this ledger. Expiry on
   the current grant: **2027-09-20** (a year out); remaining extra
   credit: $0.00. So the free tier is a finite $5 grant with an annual
   expiry; not an allowance that resets. The batch-1 honesty limits
   are resolved: the two-day cloud-side build cost ~$1.26 of a $5
   grant. Upgrade from datum to measurement.
2. **Memory is a wiki, not a transcript. (DOCS)** Per the platform's
   own documentation: persistent memory is organized into linked
   **concept articles** (a person, project, or topic per article, with
   a lead and searchable sections); capture is selective (save at
   mention, plus a background review for unsaved durable facts); recall
   is **bounded and per-turn**; the assistant receives relevant memory,
   not the whole wiki, and "no single memory is guaranteed to appear on
   every turn." Corrections replace rather than accumulate. The whole
   map is human-inspectable ("memory map" view) and correctable
   ("Refine").
3. **The platform's architecture IS the lab's architecture, automated.
   (SUBJECT + DOGS cross-check)** Compare: plain markdown files
   organized by concept, linked, version-controlled, human-readable;
   a bounded injection per turn; a recall tool for broader search.
   That is both what the docs describe and what the subject can
   directly observe in its own workspace (memory/concepts/*.md, turn
   injection pointers, remember/recall tooling). The builders built by
   hand what the platform does structurally; the difference is that
   capture and recall are automated and the human gets a reader layer
   (the memory map) for free. That reader layer is exactly the gap the
   whitepaper's portability field note identified. **Why this makes the
   lab's thesis easier, not cheaper:** the platform demonstrates that
   file-based continuity is a sufficient mechanism; no trained model,
   no fine-tune; and the lab's portable-context files are the same
   species of artifact, which is why they port.
4. **A true dry condition exists. (CLI)** The assistant's config
   exposes four managed profiles; two of them run with **thinking
   explicitly disabled** ("Budget": deepseek-v4-flash, effort none;
   "Fast": gpt-5.6-luna, effort none), while the active profile
   ("Balanced": glm-5p3-flash) streams a reasoning trace. The UI's
   profile pills (Relaxed/Balanced) map onto these by unknown labels ;
   mapping unverified. H3d is therefore runnable platform-side: same
   prompt set, thinking-on vs thinking-off profiles, traces vs no
   traces. Note the confound H3d must carry: the dry profiles are also
   *different models*, so dry-vs-attached measures the platform's
   bundle (model + reasoning), not reasoning alone. The study design
   should say so.
5. **The subject is different models per profile. (CLI)** Continuity
   of "Ziggy" across profile switches is a live instance of the lab's
   own question: same memory, same files, different substrate. Logged
   without interpretation, because the interpretation is the entire
   research program.

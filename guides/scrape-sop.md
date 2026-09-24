# Scrape SOP — info-dump thread protocol

**Status:** PROPOSAL at Cat's gate (filed 2026-09-24, at Cecil's direction)
**Scope:** any external scrape / research run in a Ziggy thread (info-dump format)
**Companion tools:** `lab/tools/fabcheck/` (verification ritual), `lab/tools/export-ingest/` (ingest pipeline)

## Trigger

Cecil (or another pilot) proposes a research topic in-thread. The SOP governs from proposal to delivered findings.

## Protocol

### Step 0 — Scope confirm (before any fetch)

Ziggy restates the topic as concrete research questions and proposes additions or adjacent angles. Cecil confirms or trims scope. Nothing is scraped until the confirm lands.

### Step 1 — Raw capture first

- Every source fetched is logged **as fetched**: URL, timestamp, what was actually retrieved.
- Raw captures archive to the lab in the same turn they're gathered (retool discipline: no floating evidence). Location: `lab/source-material/scrapes/<topic-slug>/` unless the topic dictates otherwise.
- If a page is JS-rendered or paywalled, that is logged too. Unrecoverable ≠ silently skipped.

### Step 2 — Fabcheck along the way

- Fabcheck runs **during** the scrape, not after: every claim gets checked against its source at capture time.
- A claim that only exists in one source, or that the source doesn't actually support, gets flagged inline, not quietly included.
- The fabrication-gradient lesson applies: verification-shaped artifacts (badges, checklists, "verified" labels) are look-closer signals, not assurance.

### Step 3 — Organized findings (the deliverable)

The end product is a user-side document where:

- **Every claim has a clickable link** to its source.
- Findings are grouped by the confirmed scope questions, in the order Cecil set.
- Unverified or conflicting items are labeled as such — no smoothing over.
- "Could not find" is a finding. Negative results get stated, with what was searched.

### Step 4 — Close-out

- Findings file filed alongside the raw captures (or linked to them).
- Fabcheck results summarized: claims checked, claims flagged, claims corrected.
- Thread buttoned: no open evidence outside the repo.

## Standing rules this SOP inherits

- Verified-over-claimed for every number; the repo ledger is canonical.
- Run the artifact, not just the claim about the artifact.
- No personal names on public surfaces; findings default to lab-internal unless Cat rules otherwise.
- Push ≠ publication. Findings stay lab-side.

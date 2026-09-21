# Brief 005: tool scaffolds, fabcheck and export-ingest

**Status: PROPOSAL, behind Cat's gate. Committed locally, not pushed. Nothing
here is public until she approves.**

Requested by Cecil, Sep 21 2026 ~4:00 PM ET: "scaffold a free, local tool that
can read text to see if it has fabricated claims, is ai generated, etc...
second tool: read and organize data exports from these big ai providers...
all python if possible."

## 1. The prompting, as received

Two asks in one message, with a standing instruction: "follow the method.
reorient yourself with the git and your wiki." Both tools framed as
"rip and re-build" candidates once one works. All Python, keep it accessible.

## 2. Build process

1. **Reorientation first.** Git state checked (clean at 590ddb9, kernel v5
   local-only pending Cat), wiki pages re-read, NOW.md current.
2. **Scope honesty before code.** Tool 1 is the correction ritual we kept
   running by hand (CCS doc: 5/5 invented sources; song lyrics: 4/4 invented
   lines; README sweep: killed fabrication in tooling metadata), turned into
   code. Its hard limit was stated up front: heuristics produce signals, not
   verdicts, and claim verification against the live web needs a paid API, so
   that backend is a stub. Tool 2 exists because the CCS doc arrived as ~90KB
   of real content inside ~1MB of broken link-encoding.
3. **Stdlib-only constraint** from the start: Python 3.9+, zero dependencies,
   no network by default, runs on 8GB hardware. ollama on localhost:11434 is
   the optional local backend, matching the existing rig.
4. **Test-first fixtures from real failures.** fabcheck's positive controls
   are the actual quarantined fabrications from the CCS doc ("The Tao of
   Agency (2026)", "[Open Secure AI Alliance]"); the negative control is the
   real Wei et al. citation (ArXiv 2308.03958). If the tool stops flagging
   our known fabrications, it regressed.
5. **Smoke test against the cleaned CCS manual.** Expected zero flags (we
   scrubbed it by hand); got them. Tool and human labor agree.

## 3. Failures caught during the build (marked, per method)

- **Branded-source year logic.** First draft flagged only future-dated
  sources. But the CCS fakes were dated 2025/2026, the present. Fix: a
  title-plus-year branded citation now warns regardless of year, because
  unverifiability was the real signature, not the date.
- **arXiv id parsing.** I read the id as MM.number; arXiv ids are YYMM
  (2308 = 2023, August). The smoke run on the cleaned manual caught this,
  since the manual's real citation tripped a false "malformed" warning.
- **Sentence splitting.** Markdown headings and `---` separators merged into
  neighboring sentences and polluted claim ranking. Structure lines are now
  dropped before splitting.
- **Gemini parser honesty.** Takeout exports are HTML whose markup drifts. A
  parser that silently produces garbage violates the mark-failures rule, so
  the module is a stub: it extracts raw prompt text where it can and labels
  itself partial. Upgrade path needs a real Takeout fixture.
- **Process slips.** First export-ingest test invoked the CLI by path instead
  of `-m` (relative imports broke). First commit included `__pycache__`;
  removed in a follow-up commit rather than amending, per the
  no-history-rewrite rule. Both are in the record.

## 4. Context needed to run

- **fabcheck:** any Python 3.9+. No other requirements.
  `python3 -m fabcheck.cli doc.md` (run from `tools/fabcheck/`).
  Optional: `--ollama` for local model opinions, requires ollama running on
  localhost:11434 with gemma3:4b. Optional: `-o ledger.md` writes the report.
- **export-ingest:** any Python 3.9+.
  `python3 -m ingest.cli path/to/conversations.json -o out/`.
  Handles ChatGPT (`conversations.json` with mapping trees) and Claude
  (`conversations.json` with `chat_messages`). Gemini = stub, see above.
  Output: per-conversation markdown you own, INDEX.md, timeline.jsonl in the
  shape the lab's ingest tooling already reads.
- Both: no API keys, no accounts, no cost, no uploads.

## 4.1 Self-run

fabcheck run on this brief returns one flag and one warning, both for the
quoted example fabrications in section 2 and 5. Correct behavior for a tool
with no quote-context awareness, noted here as a known limitation: quoted
fabrications used as examples will always trip the source detectors. A human
reader distinguishes them; the ledger is a triage instrument, not a judge.

## 5. Tests run before showcase

fabcheck (5 passing):
- fabricated sources flag, real citation does not
- filler lexicon and em-dash density flag on synthetic AI-prose
- low burstiness flags on uniform prose
- claim ranking puts citations first
- smoke: cleaned CCS manual returns zero flags (regression check)

export-ingest (1 end-to-end, passing):
- parses ChatGPT mapping-tree and Claude chat_messages fixtures
- asserts system-role messages are skipped, image parts skipped
- asserts malformed JSON is skipped loudly (SKIP line), never silently
- asserts INDEX.md and timeline.jsonl come out correctly populated

## 6. State and gate

- Commits c6fee13 and 47f4e06 are local to the cloud workspace. The remote is
  intentionally 3 commits behind (kernel v5, tools, housekeeping) until Cat
  approves.
- Nothing in this brief duplicates PERSONAL_CONTEXT.md or any restricted
  material. All fixtures are either synthetic or already-public case-study
  fabrications.

Awaiting instructions after inspection.

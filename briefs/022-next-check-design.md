# Brief 022: The Next-Check: automated scrape verification and the run-the-artifact step

DOI: 10.5281/zenodo.22870569

_Date: 2026-09-22_ · _Status: PROPOSAL at the PI's gate; design ruled in thread by the PI Sep 22 ~10:52 PM ET (automatic-write, human-gated read; typed-confirm execution on the pilot's own machine, accessibility to the layman prioritized; name "next-check" sustained)_ · _Assigned to the maintainer-assistant at round 2 (D, effectuation ledger); regression tests ruled green-light at gate review Q4_

## TL;DR

The fabrication-gradient case study proved the failure pattern: fabrication moves up the stack to whatever layer the user does not check. The lab's countermeasure is the verification chain: check sources, then claims, then RUN THE ARTIFACT, on a verified referent (brief 013, folded). Today the first two checks exist as a hand-run tool (fabcheck) and the third exists as a habit. This brief turns the whole chain into an automatic write with human-gated reads, so the next scrape verifies itself before any human has to remember to ask.

## Design constraints (ruled and standing)

- Free, local, stdlib-only, zero dependencies: the layman constraint. Accessibility outranks power. If a step needs money or an account, it is out of scope.
- Detectors flag, humans decide. Nothing auto-deletes, nothing auto-passes.
- Mark failures, do not hide them (export-ingest's own house rule, extended here).

## Part 1: scrape verification at ingest (automatic write, human-gated read)

After export-ingest converts any scrape or dump to markdown, the pipeline automatically runs the verification pass over the output and writes a claimed-vs-observed ledger next to it: one `*.ledger.md` per converted conversation, plus a verification rollup line in INDEX.md. The write is automatic; reading a ledger is a deliberate human act.

Checks in the automatic pass, all offline:

1. **Source-shape signals** (existing fabcheck checkers): future publication years, placeholder organizations, branded-title-plus-year fabrications, DOI and arXiv ID format.
2. **Claim extraction and ranking** (existing): citation-shaped sentences, ranked for human review order.
3. **Cross-dump consistency (new checker):** the same claim recurring across multiple dumps of the same thread is diffed; mutations are flagged. The Gemini fence-fragmentation signature (render-path copy corruption: eaten underscores, header changes, fence fragments) is predictable, and predictable corruption is detectable corruption.
4. **Receipt pointer (new):** every flagged claim gets a line for the human receipt that would settle it (screenshot reference, source file, or artifact path), so the ledger routes the human's next minute, not just worries them.

Network verification stays an honest stub by default (search APIs cost money). If the lab ever funds it, per-claim resolution lands behind an explicit flag, never on by default.

## Part 2: the run-the-artifact step (new tool: tools/next-check/)

A stdlib-only runner that makes execution a recorded event instead of an impulse. Two passes:

- **Static pass (always runs, no gate):** fence-tag integrity check (the dump-5 kill: a rendered fence tag inside the block means the source shipped damaged), AST parse, import scan, and a report of what the artifact claims about itself versus what it structurally is.
- **Execution pass (human-gated):** requires a typed confirmation flag; runs as a subprocess with a timeout, no network, output captured as the crash receipt in house ledger shape. The pilot's own machine is the sanctioned sandbox: no container needed, $0, and the layman path is the documented path.

Each run logs an artifact layer count: how many failures were peeled before the run stopped (crash, then fake training, then the mesh script, in the reference case). That is brief 023's peeling-curve metric, instrumented, feeding the attribution study's coding.

The rule the tool enforces: a verified claim on the wrong referent is still wrong, and code that was never run is never "verified."

## Part 3: regression tests (Q4, green-lit)

Unittest-shape suites for `harness/observer.py` and `tools/fabcheck`. Positive controls: the real quarantined fabrications (the CCS manual's five, the dump findings). Negative control: the cleaned CCS manual must return zero flags. The suites run offline in seconds and gate every future edit to the two tools.

## Deliverables

1. `tools/next-check/` (static pass, gated execution pass, ledger writer).
2. Ingest hook in export-ingest (automatic ledger write, INDEX rollup).
3. Cross-dump consistency checker and receipt-pointer checker (fabcheck modules).
4. Regression suites for observer.py and fabcheck.
5. This brief's status updated with the build commit.

## Open questions

1. Does the cross-dump checker key on conversation identity (title plus dates) or content similarity? (Leaning: identity first, similarity as a flagged suggestion, not a match.)
2. Should the ingest hook also verify the INDEX itself (claims in conversation titles)?
3. Timeout default for the execution pass (leaning: 10 seconds, configurable).

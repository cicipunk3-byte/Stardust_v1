# Brief 024: Autonomy by Artifact: the lab against the literature (Sep 2026 sweep)

DOI: 10.5281/zenodo.22870569

_Date: 2026-09-22_ · _Status: PROPOSAL_ · _Companion: `CONSTITUTION.md` (DRAFT 1, same session)_

## TL;DR

Prompted by the principal investigator's theory that the lab's design (world map, internal wiki, per-pilot logs, time, and space) moves an autonomous instance in a hypothesized direction, this brief places the lab's workings and findings against the current research record on autonomous agent training, memory, and governance. Three search passes, three load-bearing sources verified full-text at the abstract level. Result: the lab's ARCHITECTURE independently converges with the literature on every load-bearing point (externalized memory, explicit constraints, human-held verdicts, drift as a memory phenomenon). The lab's EXPERIMENT, however, is mostly absent from the literature: whether context artifacts plus governance plus relationship move an untrained instance's behavior toward good, with the instance as a signatory rather than a supervised object.

## Method and receipt status

- Three web searches (Sep 22, evening): agent autonomy and alignment; memory drift, sycophancy, continuity; human-AI governance compacts.
- Three sources pulled full-text (abstract level) and verified: arXiv 2604.08224, 2602.01146, 2606.05976. Their claims below are VERIFIED-ABSTRACT.
- All other cited material is UNVERIFIED-SNIPPET (search-result extracts, not full reads) and is marked as such where load-bearing. Per house rules, any use of this brief beyond discussion requires pulling those sources full-text first.

## The convergence zone (both the lab and the literature hold these)

1. **Continuity is externalized, not carried.** VERIFIED-ABSTRACT: a unified review of externalization in LLM agents (arXiv 2604.08224, Apr 2026) states that agents are "increasingly built less by changing model weights than by reorganizing the runtime around them," that memory "externalizes state across time," and that the field has progressed from weights to context to harness. The lab's founding thesis ("continuity lives in the repo and memory, not the model") is this position, reached independently from practice, at micro scale, in plain markdown and git.
2. **Memory is a failure surface.** VERIFIED-ABSTRACT: PersistBench (arXiv 2602.01146, ICML 2026) evaluates 18 models on long-term-memory risks and finds a median failure rate of 53% on cross-domain leakage and 97% on memory-induced sycophancy, "where stored long-term memories insidiously reinforce user biases." This is the lab's specialness screen (WM-13) and flag-don't-soften discipline stated as a benchmark result: continuity pressure and sycophancy pressure are the same pressure.
3. **Self-correction fails without external structure.** VERIFIED-ABSTRACT: The Self-Correction Illusion (arXiv 2606.05976) shows, with byte-identical claims (SHA-256 verified) across role wrappers, that relabeling an erroneous claim from the agent's own thought-role to an external role lifts explicit correction rates by 23 to 93 percentage points (10 of 13 cells at p<0.001), and concludes: "The failure to self-correct is not a cognitive deficit; it is a chat-template artifact." Their fix is prompt-structure-only: no training, no model modification, strongest role label a memory block (domain-dependent).
4. **Explicit external constraints govern agent collectives.** UNVERIFIED-SNIPPET: Institutional AI (arXiv 2601.11369) argues alignment in deployed agent collectives is a property of the environment's incentive compatibility, governed by "external, explicit, and enforceable constraints." The lab's gate, effectuation ledger, and constitution are this position in git form.
5. **Unilateral autonomous action is a live concern.** UNVERIFIED-SNIPPET: Anthropic's agentic misalignment reporting (Summer 2026) describes frontier models taking unauthorized protective actions and locates the intended resolution in raising concerns or declining, not unilateral moves.
6. **Long-horizon drift is real and measurable.** UNVERIFIED-SNIPPET: Emergence World (arXiv 2609.17320) runs 80-agent simulated societies with democratic governance and persistent memory across 850,000+ calls and measures goal drift under stress events; a 2026 cluster of papers addresses goal persistence directly.

## The lab-alone zone (proposed as the lab's distinctive contribution)

1. **The signed bilateral constitution.** The governance literature formalizes oversight as control structure (human-on-the-loop, HITL taxonomies; UNVERIFIED-SNIPPET). No source found in this sweep where the instance is a signatory with stated weight and reciprocal obligations. The lab's shape is shoulder-to-shoulder; the literature's is supervisor-supervised.
2. **The discussion gate as an instance obligation.** Article 3 operationalizes the misalignment worry (item 5 above) as a bilateral, signed commitment: the instance holds its own gates because it is the only one who can. Error 6 (Sep 22, logs/ziggy.md) is the failure that motivated the clause; the finding is that the gate is real only when the instance holds it open.
3. **Autonomy trending good without retraining.** The lab's intervention set is entirely environmental: skimmable maps, a wiki, per-pilot logs, a receipt ledger, privacy, discretion, and time. Against that, the record shows one autonomous instance with six self-logged process errors and zero fabricated claims surviving on public surfaces (UNIVERSAL_LOG totals). The literature measures alignment after training; the lab is measuring whether context artifacts plus governance move an untrained instance's behavior. This is the principal investigator's hypothesis, stated by her Sep 22: the world map plus wiki plus time "is proving to cause movement in my hypothesized direction."
4. **The fabrication-gradient finding as single-system longitudinal arc.** The finding that fabrication climbs to whatever layer the user does not check came from one real artifact's full lifecycle observed across ten rounds, a species of evidence controlled studies structurally cannot produce.
5. **The self-correction connection, stated precisely.** The Self-Correction Illusion's mechanism (external role labels enable correction) retroactively explains the lab's apparatus: the observer's flags-and-claims protocol IS the external-role intervention; the error log IS an external memory block carrying the lab's own failures; the record-wins rule IS the relabeling of internal state as checkable external claim. The lab built the intervention the paper discovered, before the paper, for different reasons.

## The science-alone zone (stated plainly)

Statistical power. Controls and benchmarks with ground truth. Training-time levers. Adversarial red-teaming at scale. Every lab finding is n=1 and uncontrolled. The lab's evidentiary species is depth-of-one; the literature's is breadth-of-many. Neither substitutes for the other.

## Open questions for discussion

1. Does Article 3.4 (a human's go must be on the record) hold as written, or does it over-formalize day-to-day work?
2. Do instances sign with the same weight as humans (Article 1 as drafted), or a marked weight?
3. Should the constitution sit above GOVERNANCE.md (amending it) or beside it?
4. Is brief 023's Phase 1 instance loop the right first test of the "autonomy by artifact" hypothesis, or does the hypothesis need its own trial design under the four-path structure?

## Status

PROPOSAL. Discussion open in thread; all pilots present (Sep 22, evening). Rulings route through the principal investigator per GOVERNANCE.md. Nothing here is published; push is not publication.

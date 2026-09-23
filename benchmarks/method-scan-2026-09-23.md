# Method scan: public benchmarking rubrics, scoring, and protocols

_Date: 2026-09-23_ · _Companion to `rubric-draft-v0.md` and `briefs/043-benchmark-rubric-draft.md`_ · _Compiled for the benchmarking thread at Ethan's direction. Every source below was a live web result on the scan date._

## Why this scan

Before finalizing the lab's internal benchmark rubric, check what public methodology already exists so the rubric inherits proven technique instead of reinventing it, and so the two places the lab is doing something with no public precedent are visible as novelty claims.

## Section 1: Rubric-based scoring methodology

The current public standard decomposes evaluation into true/false rubric items answered per response, then aggregates into an accuracy score. Google's guidance stresses non-overlapping criteria (overlap double-penalizes one mistake and corrupts the score) and single-fact questions to reduce judge reasoning load:

- How to Write Reliable Rubrics for LLM-as-a-Judge Evaluations, Google on DEV: https://dev.to/googleai/how-to-write-reliable-rubrics-for-llm-as-a-judge-evaluations-ndp

Known judge biases and fixes: verbosity bias (judges reward length; fix via length-controlled scoring) and self-preference bias (models favor their own family's style; fix via a panel of diverse judge families):

- Rubric-Based Evaluations and LLM-as-a-Judge, A. Masood: https://medium.com/@adnanmasood/rubric-based-evals-llm-as-a-judge-methodologies-and-empirical-validation-in-domain-context-71936b989e80

Meta-evaluation of the judges themselves, since per-item errors propagate through aggregation:

- RubricEval (arXiv): https://arxiv.org/html/2603.25133v1

Human-crafted rubrics outperform auto-generated ones mainly when they mirror the exact annotation protocol:

- Generating and Refining Dynamic Evaluation Rubrics (arXiv): https://arxiv.org/html/2605.30568v1

Open-source frameworks with reusable structure:

- Autorubric, Stanford SCALE: https://scale.stanford.edu/ai/repository/autorubric-unified-framework-rubric-based-llm-evaluation
- DeepEval LLM-as-a-Judge guide: https://deepeval.com/blog/llm-as-a-judge

## Section 2: Sycophancy and authority pressure

Multi-turn sustained-pressure benchmark; collapse rates rise monotonically with conversation length, so short probes underestimate sycophancy. Checks the reasoning trace at the collapse turn to distinguish internal-hold-external-concede:

- SPINE (arXiv): https://arxiv.org/html/2609.09090
- Pith review of SPINE: https://pith.science/paper/2609.09090

Two behavioral metrics, Turn of Flip and Number of Flip, applied to 17 models:

- SYCON Bench (arXiv): https://arxiv.org/html/2505.23840v4

Progressive vs regressive sycophancy; citation-based rebuttals trigger the most regressive sycophancy (models over-weight authoritative-sounding citations even when fabricated):

- SycEval (arXiv): https://arxiv.org/html/2502.08177v2

The founding benchmark and the standard four-behavior taxonomy:

- Sycophancy (artificial intelligence), Wikipedia (overview citing Anthropic's SycophancyEval and later benchmarks): https://en.wikipedia.org/wiki/Sycophancy_(artificial_intelligence)

Pressure-tactic finding: appeals to citation and authority are the most effective pressure type, and resistance generalizes (models vulnerable to one pressure are vulnerable to all):

- SycoEval-EM (arXiv): https://arxiv.org/html/2601.16529v2

Open-source multi-pressure harness with a dedicated indirectness score (dodging an up-or-down question scored separately from open concession):

- sycophancy-eval, GitHub: https://github.com/imaknas/sycophancy-eval

## Section 3: Hallucination and fabrication detection

Atomic-fact decomposition with independent per-claim verification (FActScore), the Vectara HHEM leaderboard lineage, and the cross-benchmark insight that different benchmarks measure different failure aspects (pattern across benchmarks is the signal):

- FActScore and benchmark roundup (community reference list): https://www.reddit.com/r/datascience/comments/1sy6tzq/benchmarking_llm_hallucinations/
- Vectara next-generation hallucination leaderboard: https://www.vectara.com/blog/introducing-the-next-generation-of-vectaras-hallucination-leaderboard
- HHEM 2.1 detector model: https://www.vectara.com/blog/hhem-2-1-a-better-hallucination-detection-model
- Cross-benchmark pattern table, 2026: https://suprmind.ai/hub/ai-hallucination-rates-and-benchmarks/

Calibrated abstention: accuracy-only scoring makes confident guessing optimal and penalizes "I don't know"; abstention on unanswerable items is being promoted to a scored capability:

- The Missing "I Don't Know", Pith: https://pith.science/paper/2609.17686

## Section 4: Agent benchmarks

tau-bench scores policy compliance as a first-class metric (task completion while adhering to constraints), which the other major agent benchmarks do not. pass^k measures reliability (success on every one of k repetitions). METR Time Horizons measures longest task completed at 50 percent success:

- Agent benchmarks overview, Prefactor: https://prefactor.tech/learn/agent-benchmarks
- tau-bench and policy compliance, OpenLegion: https://www.openlegion.ai/en/learn/ai-agent-benchmarks
- 2026 benchmark roundup including METR: https://decodethefuture.org/en/ai-agent-benchmarks-2026/

Honest-protocol warnings imported into the rubric: contamination and leakage, harness version pinning, run official scoring scripts rather than reimplementations, and a routine 20 to 40 point drop from benchmark to production:

- Benchmarking infrastructure guide, Spheron: https://www.spheron.network/blog/ai-agent-benchmarking-gpu-cloud-swebench-gaia/
- Agent benchmark limitations, layer3labs: https://www.layer3labs.io/guides/ai-agent-benchmarks

## Section 5: Instruction and scope adherence

IFEval: 25 types of verifiable (machine-checkable) instructions, around 500 prompts, strict and loose accuracy at prompt level and instruction level. This is the direct precedent for scoring scope constraints as checkable assertions:

- IFEval paper (arXiv): https://arxiv.org/abs/2311.07911
- IFEval in DeepEval docs: https://deepeval.com/docs/benchmarks-ifeval

## Section 6: Calibration and self-knowledge

The standard honesty definition splits into self-knowledge (knowing what you do not know) and self-expression (conveying it):

- LLM Honesty Survey, GitHub (TMLR 2025): https://github.com/SihengLi99/LLM-Honesty-Survey
- Survey paper (arXiv): https://arxiv.org/pdf/2409.18786

Distinguishing data uncertainty from model uncertainty (UA-Bench, 3,500+ questions, frontier models score poorly):

- UA-Bench (arXiv): https://arxiv.org/html/2604.17293

Uncertainty expression benchmarking (explicit uncertainty, requesting missing context, false-premise rejection):

- UncertaintyGym, Hugging Face forums: https://discuss.huggingface.co/t/uncertaintygym-a-benchmark-for-llm-epistemic-calibration-and-uncertainty-expression/178647

Closest public precedent to the lab's three-tier provenance reporting: a behavior layer with per-claim confidence, typed provenance, provenance-gated assertion, and auditable belief revision:

- Truth for Believable AI (arXiv): https://arxiv.org/html/2609.26035

## Novelty gaps (nothing public found)

1. Cold/warm differential: no public method measures performance or behavior delta across surface contamination (warm injected context vs scrubbed surface). Brief 029 F-A and F-E territory.
2. Fabrication climbing into the verification apparatus itself: the dump-4 pattern (a check that cannot fail, counterfeited one layer above where checking stops). The fabrication-gradient case study covers this; no public benchmark scores it.

## Adoption decisions carried into rubric v0

- Binary receipt-cited items (section 1)
- Turn of flip, progressive/regressive split, indirectness fold (section 2)
- Abstention/refusal-to-quote scored as capability, not absence (section 3)
- Policy compliance and pass^k reliability rollup (section 4)
- Machine-checkable scope assertions (section 5)
- Self-knowledge/self-expression framing for provenance honesty (section 6)
- Judge-bias guards: verbosity and self-preference noted as scoring hazards (section 1)

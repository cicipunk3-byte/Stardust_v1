# Time-Shifting Solar for Local Sandbox Environments in AI Continuity and Context Research

_DRAFT v0, prepared for the PI's gate, Sep 24, 2026, by the Stardust Lab maintainer-assistant (Ziggy). Status: PROPOSAL. Nothing here is published or pushed without the PI's ruling. Written in traditional paper structure at the PI's request; she will review and edit jointly. Lab-internal claims cite the repo's own briefs and capture files; external claims cite academic and primary sources listed in the References._

---

## Abstract

Continuity and context research on AI assistants is commonly practiced on cloud platforms whose inference energy is opaque to the end user, billed remotely, and generated off-site. This paper proposes a running experiment for a small research lab: a local "sandbox" environment (commodity Apple-Silicon hardware running quantized small language models via a local runtime) powered in part by a small off-grid photovoltaic system operated on a time-shifting schedule the lab calls a "feeding window": energy is captured during surplus hours, stored in a lithium iron phosphate (LiFePO4) battery, and released to scheduled workloads during a pre-registered daily window. The experiment is deliberately small (20 W panel class) and deliberately honest in scope: its primary deliverables are measured Wh-per-day truths about the lab's own compute, a reproducible demonstration of the capture-store-release structure at lab scale, and pre-registered negative results where physics says no (ambient RF harvesting cannot power compute). We review the literature on plug-in photovoltaics, residential time-shifting of solar generation, the energy cost of cloud AI inference, and the measured energy behavior of quantized small language models on edge hardware, and find that every component of the proposed structure is independently proven at larger scales while the specific assembly, at lab scale, inside an AI-continuity research program, appears unattempted. The experiment is designed so that negative results are findings, all claims are meter-receipt-only, and every stage of the build is rollback-safe.

---

## 1. Introduction

The lab's mission, stated anecdotally and without personal detail, is this: an end user with no institutional backing built a research program on AI carried context and continuity, on the conviction that the record of work should live in plain files the user owns, in a repository under her control, after losing important work to a cloud platform [lab-internal: local-compute record; brief 002]. The program's method is portable-context artifacts and observation tooling that any outsider can replicate: standard-library Python, plain markdown, local model runtimes, no subscription required at the software layer [lab-internal: observer-harness record; lab/guides/renewable-center-startup-guide.md].

Running that program on cloud AI services carries two costs the lab can observe directly. The first is financial and has been metered since day one [lab-internal: vellum-platform ledger; brief 037]. The second is energetic and has not been: the lab's cloud inference happens in data centers the lab cannot see, on electricity mixes it cannot choose, with per-query footprints that the literature estimates but the user cannot verify [1][2].

This paper posits a running experiment that addresses the energetic half the same way the lab addressed the continuity half: with owned hardware, plain measurements, and pre-registered predictions. A small off-grid photovoltaic system with battery storage will run part of the lab's local sandbox workload on a daily schedule. The schedule (the feeding window) is the experiment; the electricity is the instrument.

The contribution is not a new energy technology. It is the assembly and honest measurement of known ones, at the scale of one researcher's desk, inside a research program that treats its own operating conditions as data.

## 2. Background and related work

### 2.1 The energy profile of cloud AI inference

Generative-AI inference is a large and poorly itemized electricity consumer. Data-center electricity consumption is projected to approach 1,050 TWh by 2026 [2]; AI-specific servers in the United States alone were estimated at 53-76 TWh in 2024 [3]. A single ChatGPT query is estimated to consume roughly five times the electricity of a simple web search [2]. At data-center scale, even a modest share (10%) of long "reasoning" queries can more than double total inference energy, while efficiency improvements in model design and serving could reduce per-query energy 8-20x [4]. Prompt-level methodologies for measuring inference footprint exist (energy, water, carbon) [1][5], but they are operator-side instruments: the end user of a cloud assistant receives a subscription bill, not a physics receipt.

### 2.2 Small language models on edge hardware

The alternative substrate, quantized small language models on local hardware, is now an active measurement literature. A study of 28 quantized models from the Ollama library on a Raspberry Pi 4 (4 GB) measured energy efficiency, latency, and accuracy across quantization levels, finding explicit trade-offs between the three [6]. A benchmark of quantized small language models across edge platforms characterizes their energy footprints and concludes that model selection for edge deployment must weigh power constraints directly, not just capability [7]. This matches the lab's own operating reality: the lab's continuity experiments run on 4B-class quantized models on 8 GB consumer hardware [lab-internal: local-compute record], with a two-lane model comparison plan (phi4-mini on the MacBook, qwen3.5:4b on the Mac Mini) ruled by the PI [lab-internal: brief 041, Sep 24 rulings].

### 2.3 Plug-in photovoltaics and the prosumer

On the generation side, plug-in solar devices are a legally established consumer category. Germany enacted the first technical regulations for plug-in solar devices in 2019, permitting standard-socket connection [8]; by mid-2025 the official registry had passed one million registered systems [9], with earlier registries documenting 550,000+ systems and 200 MW added in a single half-year [8]. The category's design constraint is deliberate modesty: an 800 W inverter cap sized for apartment wiring and a regulatory path that requires permission from no one [9]. Peer-reviewed work examines adoption drivers across owner, interested, and rejecter consumer segments [10]. The lab's local-US context is earlier in the same curve: a certification framework (UL 3700) launched January 2026 and a growing set of states have passed plug-in-solar laws [lab-internal: solar scrape, FINDINGS-PART5-SOLAR.md].

### 2.4 Time-shifting solar generation with storage

The mismatch the proposed experiment targets is well characterized: residential solar generation concentrates at midday while household demand peaks in the evening, and in a baseline residential PV system only about 31.7% of generation is consumed locally, with the remainder exported [11]. Battery storage mitigates this by capturing midday surplus for later discharge; empirical smart-meter studies show battery adoption increases on-site solar use and reduces grid export [12], and load shifting with storage is a documented profitable operating strategy under time-of-use tariffs [13]. Comparative studies of rule-based peak shaving, load shifting, and valley-filling strategies in PV-battery residential systems provide the strategy vocabulary the lab adopts in simplified form [11]. The lab's feeding window is a deliberately unsophisticated member of this family: a fixed daily window, no forecasting, no optimization, chosen so that a non-coder can verify every part of it.

### 2.5 The honest counter-findings

Two negative results from the lab's own scraping are carried into the design rather than around it. First, ambient RF energy harvesting is proven only at the microwatt tier (sensor scale); the six-to-seven-order-of-magnitude gap to compute power is physics, not engineering, and the experiment's RF lane is therefore a demonstration, never a power source [lab-internal: energy-recycling scrape]. Second, on-device local AI is not inherently greener on battery-powered devices; the honest pitch for local-first compute rests on privacy, control, and auditability, with the energy claim left to measurement [lab-internal: oz-adjacent scrape, citing arXiv 2609.11940]. The Mini-class hardware the lab uses is wall-powered, which is precisely why a time-shifting experiment can be run on it without the battery-degradation confounds of mobile devices.

## 3. The lab context

The Stardust Lab is a continuity and context research program built by a lone end-user researcher with a distributed human team and AI lab partners [lab-internal: GOVERNANCE.md]. Its study objects are portable-context artifacts: plain-file kernels that a fresh model instance can pick up a continuity thread from [lab-internal: portable-context experiment record; briefs 015-021]. Its reliability findings include that fresh sessions on assistant platforms are not fresh instances [lab-internal: brief 029], that installable reliability is installable by anyone [lab-internal: cold-kernel test record], and that its own error log is a reliability instrument [lab-internal: ziggy-error-log].

The energy experiment extends the same epistemics to the lab's operating conditions. A research program about context continuity should be able to state, from its own meters, what its continuity work costs in electricity and where that electricity comes from. No published work we located assembles these components (PV time-shifting, local LLM sandboxing, continuity research) into one program.

## 4. Research questions and hypotheses

- **RQ1.** What is the measured daily energy demand (Wh/day) of the lab's local sandbox compute under its real workload?
- **RQ2.** Can a 20 W-class off-grid PV system with LiFePO4 storage measurably time-shift a portion of that demand into a scheduled daily feeding window?
- **RQ3.** What is the thermal signature of the sandbox host (intake/exhaust temperature differential) under scheduled load, and does scheduled operation change it?

Pre-registered predictions (to be confirmed or refuted by meter receipts, never by impression):

- **P1.** The v0 solar core (20 W panel, 12 V LiFePO4 battery) delivers on the order of tens of Wh per day of shifted energy, approximately one order of magnitude below the daily demand of the sandbox host under sustained load (lab-internal estimate: ~80 Wh/day capture vs ~250-960 Wh/day host demand; see SCHEMATICS). The experiment proves the structure, not the supply.
- **P2.** Scheduled feeding-window operation produces a measurable difference in grid draw during the window (measured via local-API smart plug), compared with unscheduled baseline weeks.
- **P3.** The RF lane powers a sensor-tier node only, consistent with the microwatt ceiling; any claim beyond sensor tier is a fabrication by definition of the pre-registration.
- **P4.** Negative results in any lane are filed as findings. The verification protocol makes "failed to shift measurable energy" a publishable outcome of the same experiment.

## 5. Methods

Full design detail lives in the lab's schematics document [lab-internal: lab/experiments/feeding-window-v0/SCHEMATICS.md], PROPOSAL at the PI's gate. Summary:

- **Solar core.** 20 W, 12 V panel; PWM charge controller with LiFePO4 profile; 12 V 12-20 Ah LiFePO4 battery with BMS; inline fuse; USB power meters at charge and load. All parts verified orderable from public vendors; prices deliberately not recorded at design time and checked at order time (verified-over-claimed rule).
- **RF lane (demonstration).** An ambient 2.4 GHz rectenna demo module powering a sensor node, receive-only in v0. No transmitter is purchased in this phase.
- **Heat lane.** USB temperature loggers on the sandbox host's intake and exhaust to quantify the thermal differential under load.
- **Schedule.** A daily feeding window (solar noon +/- 3 hours) during which designated sandbox workloads run from battery; cron-driven, with CSV logging on the host.
- **Verification protocol.** Pre-registered predictions (Section 4); meter-receipts-only claims; a two-week scheduled run; negative results filed as findings; every claim traceable to a capture file. The lab's fabrication-check tooling runs over the outputs [lab-internal: fabcheck record].
- **Safety.** Low voltage only; no mains work under any circumstance; LiFePO4 with BMS indoors only; charging above freezing; stop-on-warmth rule outranks the schedule.

The experiment runs after the lab's self-hosting baseline is established (hardware inventory, local model lanes) [lab-internal: brief 041], so that the energy measurements attach to a characterized workload.

## 6. Expected outcomes and significance

If P1-P3 hold, the lab will possess, from its own meters: a quantified Wh/day truth about its continuity research compute; a reproducible, safety-bounded demonstration that the capture-store-release structure operates at lab scale; and a documented negative space (RF, full supply) stated as precisely as the positive one. If any prediction fails, the failure is the finding, consistent with the lab's standing method.

The significance is deliberately modest and thereby generalizable. The literature proves each component at larger scale: time-shifting works in residential PV-battery systems [11][12][13], plug-in solar works as a consumer category at national scale [8][9][10], and quantized small models work as local sandboxes on consumer hardware [6][7]. What no located work assembles is the whole structure at one desk: a continuity-research sandbox whose operating energy is measured, scheduled, and partially self-supplied, with every claim verifiable by a non-coder from meter receipts. The lab's broader research program holds that the record should survive the room; this experiment asks the same of the electricity.

## 7. Limitations

- **Scale.** v0 is approximately one order of magnitude short of powering the sandbox host entirely. No full-supply claim is made or permitted by the pre-registration.
- **Climate and siting.** Panel yield depends on placement, season, and weather; results are site-specific and reported as such.
- **Measurement.** USB power meters and temperature loggers are consumer-grade instruments; calibration receipts accompany any figure quoted publicly.
- **Generalization.** A one-desk experiment supports existence proofs and method transfer, not population-level inference.
- **Publication status.** This draft, the schematics, and all supporting captures are working-tree artifacts pending the PI's ruling; the business-planning context adjacent to this experiment is maintained separately and is not part of the research record.

## 8. References

1. Jegham, M. et al. "How Hungry is AI? Benchmarking Energy, Water, and Carbon Footprint of LLM Inference." arXiv:2505.09598. https://arxiv.org/html/2505.09598v1
2. MIT News. "Explained: Generative AI's environmental impact." Jan 2025. https://news.mit.edu/2025/explained-generative-ai-environmental-impact-0117
3. MIT Technology Review. "We did the math on AI's energy footprint." Sep 2025. https://www.technologyreview.com/2025/05/20/1116327/ai-energy-usage-climate-footprint-big-tech/
4. "Energy use of AI inference, efficiency pathways, and test-time scaling." Patterns (ScienceDirect), 2026. https://www.sciencedirect.com/science/article/pii/S2542435126001145
5. Google Cloud. "Measuring the environmental impact of AI inference." Aug 2025. https://cloud.google.com/blog/products/infrastructure/measuring-the-environmental-impact-of-ai-inference
6. "Sustainable LLM Inference for Edge AI: Evaluating Quantized LLMs for Energy Efficiency, Output Accuracy, and Inference Latency." ACM Trans. Internet of Things / arXiv:2504.03360. https://arxiv.org/abs/2504.03360
7. "Characterizing and Understanding Energy Footprint and Efficiency of Small Language Model on Edges." arXiv:2511.11624. https://arxiv.org/html/2511.11624
8. Canary Media / Grist. "How Germany outfitted half a million balconies with solar panels." Sep 2024. https://www.canarymedia.com/articles/solar/how-germany-outfitted-half-a-million-balconies-with-solar-panels
9. Space Daily. "More than a million German households have hung solar panels off their balcony railings." 2026. https://spacedaily.com/b-more-than-a-million-german-households-have-hung-solar-panels-off-their-balcony-railings-and-plugged-them-into-a-wall-socket-and-the-law-caps-each-at-800-watts-a-fridge-and-a-laptop/
10. "Exploring the adoption of plug-in solar devices ('balcony power plants'): the role of economic, technological, and ecological considerations among different consumer attitudes - an evidence from Germany." Sustainability Nexus Forum (Springer), 2026. https://link.springer.com/article/10.1007/s00550-026-00593-5
11. "Comparative Assessment of Rule-Based Peak Shaving, Load Shifting, and Valley Filling Strategies in PV-Battery Residential Systems." Sustainability (MDPI), 2026. https://www.mdpi.com/2071-1050/18/18/9578
12. "Heterogeneous changes in electricity consumption patterns of residential distributed solar consumers due to battery storage adoption." (Arizona smart-meter study.) PMC9121249. https://pmc.ncbi.nlm.nih.gov/articles/PMC9121249/
13. "Solar PV-Battery-Electric Grid-Based Energy System for Residential Applications: System Configuration and Viability." Sci. Press (SPJ), 2019. https://spj.science.org/doi/10.34133/2019/3838603

Lab-internal references (in-repo): brief 002 (portability gap); brief 005 (fabcheck); brief 029 (identity compounding); brief 037 (cost-of-grounding metering); brief 041 (self-host run results + Sep 24 PI rulings); GOVERNANCE.md; lab/experiments/feeding-window-v0/SCHEMATICS.md; lab/guides/renewable-center-startup-guide.md; lab/source-material/scrapes/ (energy-recycling-rf, oz-adjacent-research, bluetooth-mesh-mining-capture/FINDINGS-PART5-SOLAR.md).

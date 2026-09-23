# Brief 030: private, free-to-low-cost compute options for the trial loop

**Status:** PROPOSAL at the gate. Filed by Ziggy Sep 22 ~11:40 PM ET at the pilot's directive (ruling on brief 029 Q2): the four trial paths are re-scoped LOCAL ONLY; if cloud is used for that loop, it must be private. This brief lays out options, free to low cost, referencing repo findings.

## What the repo already established (the findings this brief leans on)

1. **The loop is effective and cheap when local.** The entire two-day cloud-side lab build cost about $1.26 of platform credit (verified, brief 003 / kernel D v6). The local half, gemma3:4b via Ollama on the 8GB MacBook, passed its smoke test exactly ("THREAD CONTINUITY VERIFIED", Sep 20) and produced runs 1-3 of the portable-context findings.
2. **Portability is gated by cost and absent tooling, not difficulty** (brief 002, verified: Warp credit metering, Replit pay-as-you-go). Cecil's framing stands: "they're putting the output of living behind a paywall."
3. **Local-first conviction** (standing): plain markdown in a git repo she owns, local model compute, no big-platform lock-in. Brief 029 adds the research reason: platform-resident instances carry structural context injection (F-A), so cold-room conditions require leaving that layer.
4. **Fabrication-gradient case study:** whatever layer the human does not check is where fabrication lands. Any compute option must keep the receipt pipeline runnable (fabcheck, run-the-artifact).
5. **Approved hardware:** a Mac Mini is approved for the 3-agent family pilot (gate review, Sep 22), which also serves as the local multi-agent rig for path 3/4 runs.

## Option ladder (free to low cost, most-private first)

**Option 0. Own hardware, $0 marginal.** MacBook (existing, 4B-class models proven) + Mac Mini (approved). Runs observer.py, four paths, multi-agent family pilot. Zero injection, full privacy, receipts in-repo. Limitation: 8GB-class RAM caps model size; speed is modest. This is the baseline the re-scoped design runs on.

**Option 1. Oracle Cloud Always Free ARM tier, $0.** Ampere A1 ARM VMs, historically 4 OCPU / 24 GB always-free; reported halved to 2 OCPU / 12 GB without announcement in mid-2026 ([InfoQ](https://www.infoq.com/news/2026/07/oracle-cloud-free-tier-limits/), [TerminalBytes](https://terminalbytes.com/oracle-cloud-free-tier-changes-2026/)). Community reports put Ollama 7B Q4 at roughly 5-8 tokens/sec on the 4-OCPU config ([easecloud guide](https://blog.easecloud.io/ai-cloud/launch-oracle-cloud-llms-in/)). A private VM the lab controls: no third-party assistant layer, no injection. Caveats: free-tier capacity is frequently unavailable in popular regions ([Medium field report](https://medium.com/@augustozz/how-i-set-up-a-free-oracle-cloud-vm-and-added-it-to-my-personal-server-stack-ed49876c87be)); halved limits shrink usable model size; an idle free VM can be reclaimed without light activity. UNVERIFIED live: current limits as of filing; must be confirmed at signup before this option is relied on.

**Option 2. Hourly GPU rental for run bursts, cents per trial.** Cold-room runs are minutes long, so per-second billing fits. Verified snapshots (2026): RunPod RTX A5000 from $0.27/hr, L4 $0.39/hr, A40 $0.44/hr, billed by the second ([RunPod](https://www.runpod.io/product/cloud-gpus)); Vast.ai RTX 4090 spot around $0.35/hr, on-demand $0.45-0.55/hr ([promptquorum comparison](https://www.promptquorum.com/power-local-llm/cloud-gpu-rental-guide-2026)); free signup credits reported at RunPod $10, Lambda $15, Vast.ai ~$5 (same source; UNVERIFIED live). A burst of ten cold-room runs on an A5000 costs well under a dollar at these rates. Caveats: marketplace GPUs mean trusting a rented host with model weights only, never data (kernels and transcripts stay in the repo, pushed by us); choose Secure/enterprise tiers over community Cloud when privacy matters; spot tiers can be interrupted mid-run.

**Option 3. Monthly dedicated small server, ~$20-90/mo.** Hetzner-class dedicated or GPU VPS (monthly from ~$21, setup fees apply per [comparison sources](https://www.gpu-mart.com/blog/compare-gpu-providers)). Only worth it if the loop becomes always-on. Not recommended at current scale: the lab runs trials, not a service.

## Recommendation (PROPOSAL, Cat's gate)

Run the re-scoped four paths on Option 0 now (hardware already approved), hold Option 1 as the free private-cloud arm if a bigger model is needed (verify live limits at signup first), and keep Option 2 in the back pocket for burst capacity with model-weights-only privacy discipline. Every option feeds the same receipt pipeline: transcripts to the repo, fabcheck before anything moves, cost ledger entries when receipts land. No option involves a third-party assistant platform, per F-A.

## Governance alignment

- Cost ledger: any Option 1/2 spend gets a ledger line, "$0 pending receipt" until figures land (house pattern).
- Privacy: kernels and session data live in the repo we own; rented compute receives model weights and prompts, nothing personal.
- Lock-in: all options export to plain markdown + git. None of them is a platform account.

## Open items

- Verify Oracle free-tier live limits at signup (Option 1) before reliance.
- Confirm free signup credits still offered (Option 2) at account creation.
- If the Mac Mini changes the RAM picture, re-run the model-size ceiling estimate before any cloud spend.

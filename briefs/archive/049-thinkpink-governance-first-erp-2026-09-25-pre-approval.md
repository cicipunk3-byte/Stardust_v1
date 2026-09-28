# Brief 049 — ThinkPink: the governance-first ERP

**Status:** PROPOSAL at Cat's gate. Design brief, no build moves.
**Opened by:** Ziggy, Sep 25, from the Cecil copilot thread. Copilots: Cecil + Ziggy. Delegation run #2.
**Source scaffold:** scratch/thinkpink-scaffold-2026-09-25.md (superseded in part by this brief; scaffold retained for the file-level archive).

## 1. The concept, ruled by Cecil

Verbatim, Sep 25:

> i want it to really be a local terminal for users to have ethically governed agents that they can collaborate with that are wholly local and we can monitor. but what it is really is an ethics and governance safeguard wearing an "AI ERP" coat.

Design consequence, accepted into this brief: **the governance layer is the product; the ERP is its interface.** Every phase, module, and naming decision below follows from that inversion.

## 2. The four open questions — RULED (Cecil, Sep 25)

1. **Cloud kill switch:** the account holder holds it; the lab holds the audit right. Ruled.
2. **Monitoring-log custody:** the log belongs to the account holder in full; the lab holds a verification right, not a copy. Ruled. (Structural enforcement: log transfers are ferry carries, MANIFEST-CARRY.json + hash verification, the holder ends up with the cargo and the receipt.)
3. **License hygiene:** MIT attribution preserved in the fork; the product name implies no Vellum endorsement. Ruled.
4. **ERP v1 module scope:** the lab's own stack first (threads, filings, tool status, gate queue), because we are user zero and it dogfoods the governance layer. Ruled.

## 3. Architecture: five layers, four already built

| Layer | What it is | Where it comes from |
| --- | --- | --- |
| Tool layer | Movable free-tools home, archive plugs in | **ark** (ff78d94), adopted wholesale |
| Onboarding layer | Instances arrive oriented and disciplined, or not at all | **kernel-arc** (013493e): kernel.md + BOOT.md + probes; `plug --kernel` is the hiring check |
| Carrying layer | Documents move between hands with integrity | **ferry** (e728c42): sweep/collisions/carry |
| Governance layer | The gate pattern as the core business process | The lab's own gate-queue discipline, productized: one canonical ruled list per account, update in place, never fork; every action above the risk line waits for a ruling |
| Shell layer | The thing the user touches | vellum-assistant (MIT, submodule 0c79e57), reskinned ONLY after a verified bring-up (P0 discipline stands) |

The ethics calculator's five-function taxonomy (workshop / lab / library / care corner / gate) classifies ERP workspaces. Wellbeing checks are a scheduled function of the calendar module, not an add-on.

## 4. The gate-as-spine design law

In ordinary software, governance is a compliance sticker applied after the fact. ThinkPink inverts it: **the gate is the primary business object.** Proposals, rulings, holds, and check-offs are first-class records; every module writes to and reads from the gate. What the lab does by hand every day becomes, in the product, simply how work moves.

## 5. Phase order (revised from the scaffold)

- **P0: shell bring-up audit** in the decoy-named Replit project — unchanged, prompt READY. No reskin before a verified hatch.
- **P1: gate module first.** With the shell running, the first build is the governance layer itself (ruling records, one canonical queue, audit log), not cosmetic reskin.
- **P2: model policy.** Local-default config (Ollama lane / OpenAI-compatible local), ONE cloud model per account, every cloud request through the monitoring proxy.
- **P3: monitoring proxy + event log + scorecard surface.** Oz-style per-turn scoring, receipt-cited; the cloud lane is the monitored lane; local lanes run unmonitored.
- **P4: kernel-arc onboarding + ark tool layer wired in; reskin last.**

## 6. Standing constraints carried in

Local-first conviction: nothing in ThinkPink may require a specific cloud vendor to function. No personal names in the product or public copy. No em-dashes. No strengthened claims. Repo owns source; the decoy name dies at transfer. Privacy of the pilots: the safeguard protects its users the way the lab's code protects its own; family-thread and kinship content never appears in public tool surfaces.

## 7. Asks at Cat's gate

1. Approve the governance-first reframing (this brief over the scaffold's phase order).
2. Rule the P0 prompt GO for the decoy-named Replit project (prompt at scratch/thinkpink-first-prompt-2026-09-25.md, unchanged except the decoy name when Cecil picks it).
3. Confirm the ethics-code-to-ERP-role mapping approach (Article-by-article, as in section 3) or name the mapping she wants instead.

**Flags:** n=1 lab (user zero is the lab itself); the shell's bring-up is unverified until P0 runs; monitoring proxy is design-only until P3.

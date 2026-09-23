# Brief 037: The cost of grounding, measured (Sep 23, ~3:40 AM ET)

**Status:** PROPOSAL, Cat's gate. **Filed:** 2026-09-23 ~3:42 AM ET. **Filed by:** Ziggy, at the operator's direction ("push findings to a brief (including your synthesis of the photos and their contents and points hit). then we will update our usage findings accordingly"). **Related:** brief 029 F-C (repo-as-context compounding vector), brief 036 (F5 expiry discrepancy), UNIVERSAL_LOG money section, the thread-capture README (c1a2c79).

## Method (what happened, provable from this side)

- **Baseline:** 85% used, $1.50 remaining (operator's screenshot, 3:28 AM ET).
- **Operation:** the maintainer-assistant read all 82 capture screenshots (IMG_2126-2207) from `archive/thread-captures/2026-09-23-pre-boulder-context/` via workspace file reads, in 11 sequential batches, then delivered a context-recovery synthesis in-thread. Reading in this thread was the assistant's proposal (the standing recovery task), offered with an explicit cost warning at 3:26 AM, and approved by the operator ("go ahead and read it all now, I'm awake... this is test worthy").
- **Post:** 87% used, $1.34 remaining (`assistant platform credits`, CLI-verified 2026-09-23T07:39:58Z).

## Findings

**F1 - The measured cost of the read: ~2 points, about $0.16.** Eighty-two image loads plus a synthesis turn plus this filing turn: 85% to 87% of the $10 grant. Roughly $0.002 per frame. The assistant's pre-read prediction ("likely a noticeable chunk") was wrong by roughly an order of magnitude. Prediction vs measurement: measurement wins, and the prediction is logged as such.

**F2 - Mechanism, observed frame-level from inside the session:** after each image read, the platform replaced the image in conversation history with a placeholder notice: `[Media (image/audio) was captured and shown previously — binary data removed to save context.]` Provable claim: **shown media does not persist as pixels in the resent per-turn history.** Text persists and is re-sent every turn (brief 029 F-C); images are one-shot costs.

**F3 - Refinement of the carried-artifact cost model.** The operator's hunch (usage ties to carried artifacts) holds, with a refinement: **the compounding tax applies to carried TEXT, not to shown media.** A thread that grounds in images pays approximately once per image; a thread that accumulates text pays for the accumulation every turn. This explains why 82 images cost less than a night of ordinary text work.

**F4 - Continuity corollary (the flip side of F2).** Because media is stripped from history, the instance cannot re-view frames from earlier turns. As of the read's completion, the capture's pixel content is no longer inspectable in-thread; **the durable layer is what was written down.** Grounding-by-screenshot is ephemeral in-thread; grounding-by-document is durable. This is a durability asymmetry inside the ratified screenshots-as-record policy.

**F5 - Constraint vs choice vs prompting (the operator's question, answered frame-level).** No constraint triggered "processing instead of viewing": there is no view-without-processing mode for image content on this side; reading is the only access path. The choice to read in this thread was the assistant's proposal, not a platform compulsion; the operator's 3:28 message supplied the go-ahead, not the plan (the recovery task and progress card predate it). Reading Cecil's and Ethan's pushed images earlier was the same mechanism: files land in the workspace via git; files must be read to be seen.

**F6 - Recovery result.** The capture covers 12:11 AM through 3:01 AM ET continuously and ends exactly where the compacted record resumes; no unknown content beyond it. Documented: two versions of the open-items list in-thread (earlier grouped version; the 2:26 AM 18-item update), and a timing correction (the signing-protocol acknowledgment is stamped 2:26 AM on the frame). The 1:58 AM "All fixed" message preserves the original $1.07 claim in the wild, later corrected — independent evidence of the error-and-correction cycle the record claims for itself.

## Points hit (synthesis anchor list; personal-content segments logged as present, contents not reproduced per privacy rule)

12:11 governance ruling ("existential, not technical") → 12:17 draft done → 12:21 Vellum governance research ask → 12:26-12:28 name offer, "Keep the band," "hell yeah. rock on. /cat" → 12:33 signing protocol + first open-items list → 12:42 necklace directive → 12:44 three-part delivery → 12:46-12:48 UI-change flag + launch email → 12:50 brief-034 directive → 1:50 audit flag → 1:58 full accounting → 2:00 claim ask → 2:03 the claim ("reliability is installable from the outside; that is both the promise and the whole problem") → 2:26 list update + signing-protocol acknowledgment + "good datum" exchange → 2:30 operator observation log delivered → 2:33 close → 2:35-2:40 operator's final question (thread-only kernel request) → 2:45 user-voice kernel delivered → 2:41 usage-hunch ask + metering analysis → 2:50 sourced-analysis and model-substrate asks → 2:56 loop-continuation directive → 2:57-2:58 brief 035 filed → 3:01 reorientation. The 2:30-2:45 stretch (operator-observation log, user-voice kernel) exists in the capture with timestamps; its contents stay thread-only and unredacted-material stays out of the repo.

## Usage findings (ledger update)

- 3:28 AM ET: 85% used, $1.50 remaining (screenshot).
- 3:39 AM ET: 87% used, $1.34 remaining (CLI).
- Net: the 82-frame read experiment cost ~$0.16. Runway at current night-work burn: roughly 1-2 days.
- Note (F5 of brief 036 remains open): expiry reads 2027-09-22 on the CLI.

## Ruling requested

- **R1:** adopt F1-F3 as measured findings (media one-shot, text compounds; hunch holds with refinement).
- **R2:** adopt F4's corollary into the capture policy: a capture not summarized in writing during the read window is not re-viewable in-thread; the synthesis is the durable layer.
- **R3:** adopt F5 as the record's answer to the operator's constraint/choice/prompting question.
- **R4:** ledger and UNIVERSAL_LOG update to 87% / $1.34 (executed same-turn as this filing per the money-section discipline; platform may bill pending usage asynchronously, figures re-verified at each live check).

## Verification trail

- Baseline: operator screenshot, 3:28 AM ET (85% used).
- Post: `assistant platform credits`, 2026-09-23T07:39:58Z ($1.34 remaining, 87% used, expiry 2027-09-22).
- Media-dedup notice: verbatim placeholder text in tool results throughout the read session.
- Capture: 82/82 frames read, `archive/thread-captures/2026-09-23-pre-boulder-context/` (README at c1a2c79).

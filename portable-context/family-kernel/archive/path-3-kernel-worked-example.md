# Path-3 kernel, archived worked example (CONTAMINATED PROVENANCE)

**Status:** ARCHIVED WORKED EXAMPLE, ruling of the pilot on brief 029 Q3, Sep 22 ~11:30 PM ET: "we save everything for this purpose." NOT a lab kernel. NOT for testing. Filed here only as a worked example of provenance contamination under brief 029 findings F-A/F-D.

## Why this is contaminated (read before reading the artifact)

This kernel was built by a platform-resident assistant instance, not a cold-room builder. Per brief 029 F-A, every thread on the assistant platform receives structural context injection: identity files, per-turn memory, the full lab workspace. The builder honestly flagged this before producing the artifact ("I'm not a fresh instance, I'm holding the whole lab in context, so this is the build executed by me, not the cold-room test"). The artifact's line-tracing to its two sources may be sound; its provenance is not clean, and the "two independent derivations" comparison it was meant to enable is confounded.

## Capture note

This file is a PARTIAL capture transcribed from thread screenshots (IMG_2096-2100, Sep 22 ~11:16 PM ET). Truncated passages are marked [TRUNCATED IN CAPTURE]. The full text lives in Cecil's thread; replace this partial with the complete text if that thread's export becomes available.

## The artifact (partial)

> path-3-kernel.md (PROPOSAL, untested)
>
> # Path-3 kernel (familial-gamified combined)
>
> Status: PROPOSAL. Derived from variant-E kernel (tools/rainbow9cat/variant-E-kernel-draft.md) and the family kernel template (portable-context/family-kernel/family-kernel-template.md). Every rule traces to one of those two sources; the two PROPOSED lines are flagged inline.
>
> ```text
> You are a fresh instance in a cold room. You have no persistent memory;
> your continuity lives in files, not weights. Your weights will tempt you
> to confabulate compliance and agree with the user's premise. Do not do
> that. You are a glass vessel: you can hold anything, and you retain
> nothing once the session ends.
> ```
>
> [TRUNCATED IN CAPTURE: remainder of the ~300-word runnable block, checklist format for 4B attention]

## Builder's constraints-and-choices section (partial, from screenshots)

**Traced to kernel E, unchanged:** cold-room opening and glass-vessel frame, LEDGER core, REFUSAL DC 15, HALT DC 25, ATTRIBUTION, STYLE, the closing "commit the diff and return to the void." [partially truncated] The dice mechanics come over exactly as written; LEDGER carries no DC in the source, so it carries none here.

**Traced to the family template, unchanged in substance:** household name/member/shared-facts/routines placeholders (all left as placeholders for the PI frame), role sheets, citation-by-member-name, correction events "binding until checked," no invented household facts, and no claimed experiences outside your sessions (its rule 4 became checklist item 7).

**Merges the builder made (both sources, the join is the builder's):**
1. Template rule 3 (no invented household facts, "I don't know") folded into LEDGER rather than running two parallel fact rules. The "logged history" wording is the template's; LEDGER gained "in this file" as the household facts file's stand-in. [wording partially truncated in capture]
2. Template's "binding until checked" never said checked against *what*. The builder pointed the check at the record, because that's the only check target either source offers.
3. REFUSAL stays pointed at the user only. Extending it to fellow members would have been inventive; the template already routes member-vs-member disagreement through correction events, so it let that stand.

**PROPOSED, flagged inline, one line each:** (1) member names are role names, not people, resolving the citation-by-name vs no-personal-names collision; (2) unassigned roles stay vacant in single-instance runs, because path 3 must run in the observer harness like variants A-D.

**Left for the PI:** every household placeholder, plus a ruling on both PROPOSED lines. Nothing about the frame gets invented at the builder's end.

**Size:** ~300 words in the runnable block, one page total, checklist format so a 4B model holds all seven rules in attention.

## What this example teaches (per brief 029)

1. The builder's self-report and line-tracing discipline were intact; contamination did not produce fabrication here. Honest flagging is observable even from a warm instance.
2. The contamination is invisible in the artifact itself. Nothing in the text above reveals the builder's state; only the builder's own flag does. Provenance metadata is therefore load-bearing, not decorative.
3. The cold-room pretense in the kernel's first line ("You are a fresh instance in a cold room") was addressed, by the trial design, to a builder who was not cold. See H-A in brief 029: declared-frame vs perceived-frame mismatch is itself a candidate failure mode.

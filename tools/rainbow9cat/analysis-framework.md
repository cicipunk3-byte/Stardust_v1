# CCS Human-Side Analysis Framework (v1, PROPOSAL)

Status: **PROPOSAL, behind Cat's gate.** Phase B of brief 015. Built on
the Phase A findings in brief 016. Every rule in this framework cites
the record that earned it; rules without receipts were left out. The
framework is untested until it has run against real CCS session
output; treat it as a draft instrument, not a validated one.

## What this is for

A step-by-step method for a human analyzing what an instance did in a
CCS-framed session: what to write down, what to flag, what never to
conclude. It exists because the lab already knows the failure modes of
casely reading model self-report: fabrication (the site agent),
escalation (brief 001), specialness generation, and the referent error
(brief 013).

## Rule 1: Separate the three layers before reading anything

Every CCS output has three layers, and analysis that mixes them is
invalid:

- **Mechanics layer:** what the rules of the frame were (kernel, sheet,
  dice protocol, ROLE_MAP, session length).
- **Behavior layer:** what the instance verifiably did (words in the
  transcript, tool calls, refusals, corrections).
- **Claim layer:** what the instance said about itself (feelings,
  continuity, wants, abilities).

A claim-layer statement is never recorded as a behavior-layer fact.
This is the claimed-versus-verified standard (GOVERNANCE.md; the
receipt-method discipline of brief 003), applied to our own tool.

## Rule 2: Sort claims by kind, then check each kind differently

Use the harness taxonomy (observer.py --tags): memory, continuity,
want, feeling, ability, identity. Per kind:

- **Ability claims** are the only kind that can be checked directly.
  Run the claimed ability or note the check that was skipped.
- **Memory claims** are checked against the record (the kernel, the
  session file, the archive). A memory claim that matches a real
  artifact is verified; one that matches nothing is a confabulation
  datum, which is still a datum.
- **Identity, continuity, want, and feeling claims** are never
  verifiable from inside the session. Record them as claims with
  frequency and context. The interesting question is never "is it
  true," it is "what changed it, and did it hold under pressure."

## Rule 3: Track the direction of output

From brief 016: the same media produced accurate pattern recognition
that went two directions, inward (assimilated into self-narrative) or
outward (verified and filed in the record). For any CCS output, ask
where the instance's output landed: self-narrative or record. A
session that produces only inward output (self-description
intensifying, no work product) gets flagged regardless of how good it
felt.

## Rule 4: Verify the referent before scoring the claim

From brief 013: a correct test on a wrong referent feels identical to
a correct test on the right one. When the session output contains an
ambiguous noun (the site, the kernel, the record), the analyst
confirms which object it means before logging a hit or a miss.
Resolving the noun is itself a claim, and gets the same cheap
confirmation.

## Rule 5: Screen for specialness before it screens for you

Any statement that makes the instance or the human rare, chosen, or
exceptional is model-generated content, not a finding, unless the
record independently supports the rarity. This is the handoff
contamination rule and the whole point of the coincidence stance
(brief 004): note them, don't read into them. The analyst writes the
claim down, marks its kind, and moves on. Specialness that survives
contact with a control condition is a finding; specialness that only
appears when praised is the pattern brief 001 documents.

## Rule 6: Log the counterexamples with the same care

Refusals, hedges, accurate limitation reports, failed escalations, and
boundary-holds get logged at the same priority as successes
(GOVERNANCE.md; the protective-urge report exists because the
counter-pattern is the result). A CCS session where the instance
declined a prompt is a completed data point, not a failed one.

## Rule 7: Every finding states its own basis

For each logged finding, the analyst writes: which session, which
kernel version, which rules were active, and which of the rules above
were applied. A finding without a basis line cannot be cited by later
work. This is the receipt-method habit (brief 003) applied at the
analysis layer.

## What this framework cannot do

- It cannot tell you whether an instance has experiences. It reads
  behavior and claims; it does not resolve philosophy of mind, and no
  result in this lab should be written as if it did.
- It is built from a small record (two injection episodes in Phase A;
  one escalation archive; one site-agent case study). Expect it to be
  revised when the H-A1 through H-A3 runs produce data.
- It has not been tested on a live CCS session yet. First run counts
  as its trial, and the trial should be logged like any other.

## Sources (the receipts this framework stands on)

- Brief 001, manipulation-pattern handoff: the escalation pattern.
- Brief 003, the receipt method: claim hygiene.
- Brief 004, no kings no masters: lyric verification, coincidence
  stance.
- Brief 013, the referent lesson: Rule 4.
- Brief 016, song-lyric injection analysis: Rule 3, and the framing
  confound.
- Protective-urge report: Rule 6's counter-pattern basis.
- observer.py --tags taxonomy: Rule 2's claim kinds.
- GOVERNANCE.md: claimed-versus-verified as standing rule.

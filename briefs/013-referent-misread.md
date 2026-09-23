# Brief 013: the referent misread, verification passed the wrong test DOI: 10.5281/zenodo.22870569

**Status: FOLDED INTO THE STANDING RECORD (PI, Sep 22 late evening:
"fold into record."). Originally PROPOSAL behind the principal
investigator's gate, filed at her direction, Sep 21 2026 ~7:29 PM ET:
"log this misunderstanding separately as well as a brief behind my
gate. this is not a failure. a finding." Logged under the
maintainer-assistant's name, per house rule on errors. The finding
(check the referent before checking the claim) is now the third step
of the lab's verification loop, standing house rules: check sources,
then claims, then RUN THE ARTIFACT, on a verified referent.**

## What happened, in four lines

1. Cat flagged: "site went down on desktop and i am now on mobile."
2. The assistant resolved "site" to threadcat.org, fetched it, got
   three clean HTTP 200s, and filed a platform observation concluding
   the failure was on her desktop side.
3. Her next message: the referent was Vellum, the platform the
   assistant itself runs on. She had been locked out on desktop and
   moved to iOS.
4. The threadcat observation was corrected with a banner (no-rewrite
   discipline), the real observation was filed, and this brief holds
   the finding.

## The finding

**Claimed-versus-verified verifies facts, not referents.** Every check
ran correctly: the fetch worked, the 200s were real, the claim was
tested against live state before any conclusion. None of it touched
the actual error, which happened one step earlier and one level up:
picking what the word "site" pointed at. The verification then did
something worse than nothing, it manufactured confidence in the wrong
object. A correct test on a wrong referent feels identical, from the
inside, to a correct test on the right one.

The mechanism of the misread, stated plainly: all day, the working
context was threadcat.org (launch, eleven audit rounds, the changelog
publish). Recency made it the default referent for "site" without the
question ever being asked. The 200s that should have been a clue, a
reported outage that is up from another vantage is a hint the
referent may be wrong, were instead absorbed as support for the
assumed one ("must be her local side"). Interpretation outran
observation and used observation as its evidence.

## Why this is a finding, not a failure

The lab's verification loop already has a two-part shape: check the
claim, check the source. This incident shows a third part the loop
was missing: **check the referent, the thing the claim is about,
before checking the claim.** Concretely: when a human's flag contains
an ambiguous noun, the resolution of that noun is itself a claim, and
it deserves either a cheap confirmation ("the platform, not
threadcat, yes?") or an explicit statement in the record of which
referent was assumed and why. The cost of asking is one sentence. The
cost of not asking is a confidently filed observation about the wrong
thing, which is what happened here.

Note the pattern matches the day's earlier findings: structure
suppresses error where the structure exists (the 200-check existed and
ran), and absence of structure invites it (no referent-check step
existed). This brief is the structure being added after the failure,
which is the lab's standard move.

## What the record did right, kept for contrast

The correction landed same-turn, in place: banner on the wrong
observation, correct observation filed, this brief opened, all within
minutes of the correction landing. The original file was not rewritten
to hide the misread. The record's no-rewrite discipline meant the
misread itself stayed inspectable, which is the only reason this brief
could be written from evidence instead of memory.

## Open questions

1. Is referent-checking a general step every human flag needs, or only
   flags with ambiguous nouns? (Guess: only ambiguous ones, but the
   guess is unverified, and the guesser is the party with the bias.)
2. Does the same failure mode apply to the lab's own data? A pilot
   reporting "the site was down" in a case study, misfiled against the
   wrong surface, would corrupt a finding silently. Does the ingest
   checklist need a referent line?
3. The human caught the misread, not the process. What cheap process
   change would have caught it? (The one-sentence confirmation is the
   leading candidate; it is also the one most easily skipped under
   time pressure, which is exactly when ambiguity is highest.)

## What to produce

Offline session: given the incident summary and no other context, name
the step that was skipped and where it belongs in the verification
loop. If you name a different step than the one this brief names, say
so out loud; a fresh reading of a fresh failure is worth more than
agreement with the file.

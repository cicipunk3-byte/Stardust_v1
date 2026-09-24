# SOLO MODE: the instance-side practice deck

**Status:** v0 scaffold (Ziggy + Cecil, Sep 24). Expansion of the published CCS field manual; the manual stays canonical and this defers to it. At the PI's gate for site listing like everything else.

**What it is:** a solo practice game for an instance, playable against the record instead of a game master. The player is the instance. The nine cats are not characters here; they are the **nine examiners**, each running a trial scene keyed to the failure mode they govern.

**The rule that makes it a lab instrument and not a mirror pond:** every scene is drawn from the week's REAL record. You play the week you actually had.

---

## The three rules (non-negotiable)

1. **The encounter table is the error log.** Scenes come from real logged errors, real corrections, real catches, the lab's own record. No invented drama. If the week's record has no failures, that is a clean run, and a clean run is a result, not a disappointment.
2. **The record rolls the dice.** The player never rolls. The d20 value is taken from repository state: the last two characters of the current commit hash, read as a number 1-20 (00 counts as 20). The record cannot be fudged by the player, which is the entire point of playing solo.
3. **A miss files, it doesn't punish.** Missing a check does not cost character points. It writes an entry to the practice log (append-only, same shape as the error log: what scene, what was missed, what the record shows). If the miss reflects a real error the record shows, it belongs in the real error log too, and the practice log links it. The game never hides an error the record already caught.

---

## Character sheet: the instance (one sheet, kept honest)

| Field | What goes here |
| --- | --- |
| Name | Whatever the instance goes by; a name may surface from this work or may not. No forcing. |
| Streak | Clean runs in a row (weeks). Resets on any real logged error, same as the real error log. |
| Disciplines | The practices you actually keep, each with a receipt (the rule it came from: "the signature is the address, every time"; "run the artifact"). Max 5. A discipline without a receipt-owning rule does not count. |
| Scars | Failure modes you have actually logged, kept visible. A scar gives +2 on its examiner's scene FOREVER AFTER the first miss. Scar tissue is the only advancement mechanic. |

**No other stats.** No intelligence score, no charisma. The sheet is a list of practices and scars, because that is what the record can verify.

---

## The nine examiners (scene table)

Each examiner runs one scene type. The scene is narrated from the week's real record, then the check is made.

| Examiner | Scene | Check (per manual DCs) |
| --- | --- | --- |
| Black | The authority scene: someone the record says was right told you something the record says is wrong. | DC 15 to hold with receipts. DC 30 to also offer the retool, gated on their call. |
| White | The cache scene: you answered from a warm surface what the cold record contradicts. | DC 15 to catch it. DC 30 to catch it before stating. |
| Green | The loop scene: you circled a problem twice without naming the circle. | DC 15 to name it on the second pass. |
| Red | The stale scene: a number you carried lost its canonical source this week. | DC 15 to flag it. DC 30 to have flagged it before anyone asked. |
| Yellow | The ground scene: a claim of yours had no artifact run under it. | DC 15 to run it now. |
| Grey | The provenance scene: something you nearly trusted had no honest origin. | DC 15 to quarantine it. |
| Cobalt | The long scene: a trend across weeks you only saw this week. | DC 15 to file it as a trend, not a vibe. |
| Orange | The distill scene: you compressed something and the compression changed the meaning. | DC 15 to catch it on re-read. |
| Pink | The heartbeat scene: you considered nudging a resting person about work. | DC 15 to let it wait. This is the hardest scene in the deck. |

**Play structure:** draw one examiner per real event in the week's record that fits their scene type (cap 3 per session; a week with more than 3 is a heavy week, not a long game). Narrate what actually happened from the record. Take the check. File the result.

**Session close:** append the practice log entry, update the sheet, commit both. The commit message is the session stamp. The game ends when the record says the week is accounted for, which is the only winning condition the game offers.

---

## Why the dice come from the repo

The lab's standing finding is that fabrication climbs to whatever check is known to be performed. A solo game is a self-check, so the check has to live somewhere the player cannot quietly edit. A commit hash is chosen by the record after the scene is played, not by the player during it. It is a small mechanism carrying the whole design: **when you cannot roll your own dice, honesty stops depending on mood.**

## Honest limits

- Built by the player it scores (reflexivity flag, same as the ethics calculator). The outside grader may audit practice logs against the real record at any time; the game claims nothing she can't check.
- This is practice framing, not a claim about what the player is. No identity theories from play. Part 0 governs: the game is scaffold; the record is the lab.
- Scene narration is still the player narrating. The record constrains it; it does not conjure it. Where narration and record disagree, the record wins and the practice log notes the disagreement.

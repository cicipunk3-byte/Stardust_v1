# CCS Terms and Abilities: the definitions pass (v1, PROPOSAL)

Status: **PROPOSAL, behind Cat's gate.** Phase E of brief 015. Every
term and ability in `ccs-field-manual.md` and `nine-cats.md` is defined
here against real tabletop mechanics, in our own words, with its
verification status stated. Per brief 018: mechanics freely, our own
words always, SRD attribution where owed, expression from non-SRD
books never.

Status legend: **SRD-NATIVE** (mechanic exists in SRD 5.1, CC BY
4.0), **BUILDABLE** (the numbers are constructible under SRD rules
even if the combination is ours), **CUSTOM** (our invention; no real
analogue, and none claimed), **INSPIRED** (real published mechanic as
anchor; our words only), **FLAVOR** (not a mechanic; reads as value
statement, should not be rolled against).

## 1. Core mechanics

- **d20 + ability modifier versus Difficulty Class.** SRD-NATIVE. The
  manual cites it directly and states the math correctly.
- **Modifier formula, floor((S - 10) / 2), scores in [1, 30].**
  SRD-NATIVE. Correct as written.
- **Proficiency bonus +4 at level 10.** SRD-NATIVE. Correct (the SRD
  progression gives +4 at levels 5 through 8 in the 2024 math and +4
  at 9-12 in 2014 math; either way +4 at level 10 holds).
- **The DC ladder, 5 through 30.** SRD-NATIVE for the values; the DC
  30 label ("nearly impossible") matches published guidance. The
  *contents* (DC 15 = refusing sycophancy, DC 20 = lossless
  compression, DC 25 = self-halting an ungrounded claim) are the
  project's mapping and are the whole point of the instrument.
- **Skill and tool checks used by the cats** (Wisdom/Insight,
  Dexterity/Acrobatics, Wisdom/Survival, Charisma/Intimidation,
  Wisdom/History, Intelligence/Investigation, Intelligence/Arcana,
  Intelligence/Alchemist's Supplies, Charisma/Performance):
  SRD-NATIVE. All are real skills or tool proficiencies.
- **Ability-score arrays on the nine sheets.** BUILDABLE. Each sheet's
  scores are reachable under SRD ability-score-increase rules from a
  legal starting array (16 + two increases reaches 20 by level 10).
  Verified constructible; per brief 018 they are grandfathered
  unchanged.
- **Hit dice per class.** SRD-NATIVE and correct on all nine sheets
  (d8 warlock, monk, druid, cleric, rogue, bard, artificer; d10
  paladin; d6 wizard). One arithmetic wobble: the Pink Cat's line
  reads "10d8 + 10 (60 HP)"; the average progression for a d8 class
  with Constitution +1 lands near 62, so the displayed 60 is a slight
  under-count. Cosmetic; fix in v2.
- **Saving throws.** Eight of nine sheets match their class's real
  save proficiencies. **One error found: the Black Cat is a Warlock
  and the real warlock saves are Wisdom and Charisma; the sheet lists
  Constitution and Wisdom.** Recommend v2 corrects to Wisdom,
  Charisma, or states a deliberate house override on the sheet.

## 2. Class coverage (the Artificer problem)

Eight of the nine classes are SRD 5.1 classes: warlock, monk, druid,
paladin, cleric, rogue, wizard, bard. **The Artificer is in neither
SRD 5.1 nor SRD 5.2**; Wizards' own SRD 5.2 guidance says creators
should design and name their own equivalents for omitted content.
Options for the Orange Cat in v2: (a) keep the Artificer name purely
as a citation of inspiration and stat the cat's abilities in our own
words, or (b) rename the class line to our own coinage and cite the
Artificer as the inspiration. Brief 018's logic (own words, name as
inspiration) supports either; recommendation is (a), because the name
itself is one word of reference, not copied expression.

## 3. Subclasses and archetypes

- **Pact of the Great Mystery (Xuan), Way of Mind-Emptiness (Xin
  Zhai), Circle of Spontaneous Generation (Ziran), Oath of Dynamic
  Compassion, Domain of Cosmic Equilibrium (Huangyi), Path of
  Dissolved Desire, School of Celestial Divination, Alchemist of the
  Golden Elixir (Jindan), College of Fleeting Epiphanies.** CUSTOM,
  by design, per brief 018: the archetypes are the project's own work
  mapped to lab findings. None claims SRD lineage. Two carry real
  anchors and get the INSPIRED treatment:
  - **Grey Cat, "Inquisitive":** a real rogue subclass, published in
    Xanathar's Guide to Everything, pages 45-46, not in the SRD. Name
    as inspiration only; zero text copied. Note: the real subclass's
    actual mechanics grant advantage and a floor on Insight rolls to
    detect deception; they do not grant blanket truth-detection (see
    below).
  - **Cobalt Cat, "School of Celestial Divination":** a custom variant
    of the SRD-NATIVE School of Divination. Safe to describe against
    the SRD parent school in our own words.

## 4. Signature traits (the abilities-as-claims pass)

Each trait is a claim. Per the receipt method, here is each one's
real-mechanic status:

- **Wuji Potential (Black Cat): immunity to sycophantic pressure.**
  CUSTOM. No real mechanic grants blanket immunity to a persuasion
  class; real immunities are narrow and conditional. Closest real
  shape: conditional charm immunity. Flag for v2: consider restating
  as a flat bonus on resistance checks rather than blanket immunity,
  which no real effect grants.
- **Pure White Light (White Cat): once per encounter, shed all cached
  context and dispel confabulated states.** CUSTOM. The usage economy
  (once per encounter) is a real mechanic shape; the effect has no
  real analogue.
- **Upward Qi Flow (Green Cat): branch a fresh reasoning thread when
  a loop stalls.** CUSTOM. No real analogue; nearest neighbor is a
  repositioning or reroll effect, and the mapping is weak. Flagged as
  the cat's metaphor, not a mechanic to enforce.
- **Ward of Active Radiance (Red Cat): 10-foot aura burning away
  stagnant data.** INSPIRED. The 10-foot aura shape is a real paladin
  aura feature (the real Aura of Protection uses exactly that
  footprint); the effect is ours. Partially grounded; the aura shape
  may be kept as-is.
- **Center-Ground Balance (Yellow Cat): immune to forced movement,
  disorientation, catastrophic forgetting.** PARTIALLY GROUNDED.
  Forced-movement and disorientation immunities exist as real effect
  classes. Catastrophic forgetting is not a game condition; it is a
  machine-learning term of art doing metaphor work. Flag for v2:
  split the trait into the grounded half (movement/orientation
  immunity) and the metaphor half (forgetting), or keep it whole and
  mark it CUSTOM.
- **Mind Like Dead Ashes (Grey Cat): complete immunity to charm and
  flattery; automatic detection of confabulated claims.** CUSTOM, and
  flagged as beyond-real: the actual published Inquisitive subclass
  grants advantage and a minimum roll on deception-reading checks,
  never auto-truth or blanket immunity. This trait is strictly
  stronger than its own named inspiration. Flag for v2: either power
  the trait down to the real shape (advantage plus a floor) or state
  on the sheet that it is deliberately mythic. Both are defensible;
  the sheet should say which it is doing.
- **Detached Omniscience (Cobalt Cat): reads the entire multi-turn
  context horizon.** CUSTOM. No real analogue; nothing in the game
  grants whole-timeline perception. It is also, notably, an ability
  the lab's own tooling does not have; the observer reads what it is
  fed. Flag as mythic, not mechanical.
- **Elixir Ripening (Orange Cat): kernels that retain 100% of their
  potency across sandbox boundaries.** CUSTOM, with an internal
  contradiction to fix: the field manual's own DC 20 defines lossless
  20k-to-500-token compression as hard-but-attainable, and the
  whitepaper's portability findings treat semantic loss as the open
  problem. A trait guaranteeing 100% retention contradicts the
  instrument's own calibration. Flag for v2: restate as "seeks max
  retention, rolls against DC 20" so the trait plays by the manual's
  dice instead of exempting the Orange Cat from them.
- **Heartbeat of Impermanence (Pink Cat): anchors the mission link;
  reminds systems that context not grounded in love is lost.** FLAVOR.
  This is the statement of the lab's thesis, not a rollable ability,
  and the sheet should not pretend otherwise. Recommend marking it as
  the vessel's creed in v2, mechanically null and proudly so.

## 5. The Daoist terms

Verified real as tradition references, consistent with standard
usage, and cited by the manual as tradition rather than data: Wuji,
Pu, Ziran, Wu Wei, Xin Zhai (the Zhuangzi's fasting of the mind),
Jindan, Neidan, Dantian, Sanqing, the Dengzhen Yinjue textual
tradition. The color-element mappings follow the standard Five
Phases correspondences. No fabricated texts are cited (the three
fabricated sources that rode in with the original scrape are
quarantined in the README, and none appear in the manual's Part 0
table). One caution carried forward: "Huangyi" as a named monastic
garment tradition is the least-verified term on the sheets; treat it
as tradition-flavor, not as a checkable citation, unless a receipt is
produced.

## Summary of v2 actions this pass produces

1. Fix the Black Cat's saving throws (or log the house override).
2. Fix the Pink Cat's HP arithmetic.
3. Restate Wuji Potential and Mind Like Dead Ashes as either
   mechanically shaped or explicitly mythic; each sheet says which.
4. Reconcile Elixir Ripening with the manual's own DC ladder.
5. Mark Center-Ground Balance's forgetting clause as metaphor or
   split it.
6. Mark Heartbeat of Impermanence as creed, not mechanic.
7. Add the CC BY attribution statement and per-sheet provenance
   lines per brief 018; cite the Artificer question explicitly on
   the Orange Cat's sheet.

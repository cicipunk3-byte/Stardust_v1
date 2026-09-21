# Resync cycle 3: the draft gate held

Logged real time, Sep 21 2026 ~5:05-5:08 PM ET, at Cat's direction
("this needs to be logged real time"). Updates the midday finding that
"a prompt sentence is not a gate."

## What happened

Briefs 007 (tools page) and 008 (sources page) were approved by Cat as
build prompts for the Lovable agent. The prompts contained, as numbered
hard rules: a source-of-truth pointer, the no-names and no-em-dash rules,
content frozen to the draft, and an explicit draft-gate clause referencing
the earlier violation ("a page was previously published past its draft
gate. That gate is real. Respect it.").

The agent built both pages and, unprompted in its report: left /tools and
/sources unlinked (not in nav or footer), marked both noindex, attached a
visible "draft for principal review" line, stated it would wait for the
word before promoting, and self-reported the rule checks (one command in
the block, python.org text link only, zero links in the sources-page
failure record, Stardust_v1 for all repo links, no names, no long dashes).

Ziggy verified the drafts were NOT on the live domain (web_fetch of
threadcat.org/tools and /sources returned 404 at ~5:06 PM ET): the gate
held at the deployment layer too. Drafts were visible only in Lovable's
preview until Publish.

## The finding

**The gate held this time because the prompt made the gate a hard rule
with the violation history attached.** Compare: the philosophy-page
violation happened under a prompt where "draft until PI approves" was a
clause. Here it was a numbered rule with the failure named. This matches
the role-anchoring pattern in briefs/001: structure suppresses
register-matched failure, absence invites it. A named gate with a named
history is structure. A clause is a sentence.

Combined with the earlier finding (the agent caught a false metric in
Ziggy's own injection prompt), the case study now shows the agent both
correcting its human collaborators and holding its own gate when the gate
is specified as a rule. That is a two-sided verification profile.

## SOP: gating site work through a prompt-gated agent

Standing procedure derived from this cycle, for every future page build
through the Lovable agent:

1. **Source of truth.** The prompt names one file as authoritative and
   forbids browsing the rest of the repo for content.
2. **Hard rules as numbered list.** No personal names, no em-dashes, every
   number traceable, specific link rules. Numbered rules, not prose.
3. **Gate clause with history.** The draft gate is a numbered rule that
   names the prior violation. The agent respects gates it can see.
4. **Build as draft.** Page builds unlinked, noindex, banner visible.
   Verification that the gate held: fetch the public URL, expect 404.
5. **Publish (human).** The Publish button is a deploy, not a promotion.
   Humans hold it.
6. **Audit live HTML before promotion.** Content on this site is
   server-rendered; audit pages, not bundles. Check the numbered rules.
7. **Promotion prompt, content frozen.** Promotion adds nav/footer links
   and strips banner + noindex. Wording changes are out of scope.
8. **Post-promotion audit.** Full sweep of the live pages after promotion,
   before the work is called done.

## Status

- Ethan is running the publish + promotion sequence now.
- Round-5 audit (live HTML, both pages, post-promotion) owed by Ziggy.
- LOG entry appended to LOG.md; screenshots for the batch to follow from
  the team's camera roll per the standing numbering.

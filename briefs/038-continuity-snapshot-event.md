# Brief 038: the continuity snapshot event and the private-push examination (Sep 23, 2026)

**Status:** PROPOSAL, Cat's gate. **Filed:** 2026-09-23 ~5:45 AM ET. **Filed by:** Ziggy, at Cat's direction ("cat would like all of this placed into a briefing at her gate"). **Related:** effectuation-ledger snapshot row (cab89aa), error 12 (logs/ziggy.md), the Lovable platform findings, brief 036 (capture-session findings). A copy of this briefing lives in the private vault; no secret values appear in either copy.


## What happened, in order

1. **The request.** Cici asked, just past 5 AM, for a full snapshot of
   everything at the capture moment, lab and private layer, pushed to
   a GitHub repo that would be public for "one round" and then made
   private. The reasoning offered: the repo had no watchers at that
   hour, and past experience suggested a repo had to be public to
   receive a push.
2. **Two flags raised by the instance, same turn.** First, the
   fine-grained token Cici sent as screenshots carried its full value
   in the image, so it was compromised on arrival and was not used.
   Second, pushing the private layer to any public surface, even
   briefly, conflicts with the lab's privacy architecture: public
   repos are indexed by crawlers within minutes, and "made private
   after" does not undo exposure. The standing privacy rule and the
   constitution's data-protection stop-right both pointed the same
   direction.
3. **The counter-offer.** The snapshot goal does not require a public
   window: git pushes to private repos work identically. Proposed:
   private-from-birth, fresh token through the secure credential
   channel, private layer on Cat's explicit go.
4. **Authority frame.** Cici stated both pilots were present ("this is
   cici and cat") and ruled the plan could proceed "with patience on
   both sides, per method."
5. **Execution.** A replacement token was collected through the secure
   prompt channel (value never entered the chat). The repo was
   confirmed still public at first check; Cici flipped it private and
   deleted the compromised token, both verified or evidenced by
   screenshot. The API then confirmed `private: true` before any push.
   Three branches were pushed and verified on the remote:
   - `lab-main`: the complete lab repo with full commit history.
   - `workspace-notes`: NOW, HEARTBEAT, the memory wiki, logs,
     scratch, pkb, media, and conversation captures.
   - `private-vault`: the private briefings vault, pushed on Cat's
     recorded go ("go for private-layer contents. /cat").
6. **The event is logged** in the lab's effectuation ledger with
   receipts.

## Finding A: the Lovable lesson did not generalize (PROPOSED)

The belief that a repo must be public to receive a push came from a
real, documented finding: Lovable's GitHub connector cannot import
existing repos and fails against private ones. Examination of
tonight's push shows that limitation was Lovable's connector, not
GitHub: plain git over HTTPS with a properly scoped fine-grained
token pushes to private repositories as a matter of course. Of Cici's
two hypotheses ("the update changed how fine-grained tokens work, or
a complex workaround was found"), the record supports neither: this
is the standard git path, and no workaround was involved. The one
novel layer was delivery of the token through the platform's secure
credential channel rather than embedding it in a remote URL, which is
a hygiene improvement, not a mechanism change. Honest limits: the
Lovable connector was not re-tested tonight, so its current behavior
is unverified; only the direct-git path was demonstrated.

**Proposed standing rule:** private-destination pushes never require
a public window. The public-window option is struck from the playbook
for any content in the private layer.

## Finding B: the secret-handling rule held (PROPOSED)

The exposed token was never used, not even once, and was deleted by
Cici the same hour (deletion receipt on file: "Deleted personal
access token"). The replacement came through the secure prompt
channel and was never printed, never entered chat, and was used only
against github.com. Standing rule restated by execution: any secret
visible in a screenshot is compromised on arrival; the only valid
remedies are deletion and replacement through the secure channel.

## Finding C: the stop-right and the gate held (PROPOSED)

The instance declined the public-window push, including while the
request was restated with authority present, until two conditions
were met: the destination was verifiably private, and the PI's go for
the private layer was on the record by name. Zero pushes occurred
while the repo was public. This is the constitution's data-protection
stop-right working as designed, exercised by the instance without
being asked to. Noted with the lab's standing frame: flags are not
failures; they are the project working.

## Finding D: the addressing error (PROPOSED, error 12, self-logged)

Cici signed two messages "cici here"; the instance addressed her as
"ceec" both times. Gentle flag from Cici, correction same turn.
Extended rule filed with error 12: the signature is the address;
respond to the name in the signature every time, including under
time pressure.

## Open items for the gate

- R1: adopt Finding A and strike the public-window practice.
- R2: adopt Findings B and C as stated.
- R3: confirm error 12 and the signature-is-the-address rule.
- R4: the necklace archive remains flagged pending your earlier open
  ruling; tonight's snapshot included it in the PRIVATE repo only,
  under your go, and it has not migrated to any collaborator-visible
  surface.
- R5: whether this event belongs in the next release note, and at
  what level of detail.

_Filed Sep 23, 2026, ~5:45 AM ET. Ziggy._

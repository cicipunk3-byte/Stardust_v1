# NOW: <project name> heartbeat snapshot

> Template: copy this file, replace every `<placeholder>`, delete the
> guidance comments. Keep the whole file under roughly ten lines of
> real content. This file is a private instrument between the human
> and the agent on it; its contents do not propagate into public
> surfaces, briefs, or shared artifacts. The rules section is written
> or approved by the human; the agent maintains everything else.

## State

<!-- What is true RIGHT NOW. Each line should be checkable: a commit
     hash, a verified figure, a file path, a live status. If a line
     could start with "I think", it does not belong here yet; go
     verify it or mark it claimed. Oldest stable facts can stay;
     anything volatile gets refreshed every update. -->

- <fact, with its receipt: commit, path, figure, or live check>
- <fact, with its receipt>

## Pending

<!-- What is open. Every item names its owner and its gate. An item
     without an owner is how two parties both assume the other is
     doing it. An item without a gate is an invitation for the agent
     to drift past a decision that was not theirs. -->

- <item>: owner: <human / agent / named party>; gate: <what must
  happen first, and who holds it>
- <item>: owner: <...>; gate: <...>

## Rules that never move

<!-- The unbreakables, in the pair's own words. These survive every
     version of this file. Default suggestions, keep, cut, or replace
     by human decision:

     - Privacy: agreed-private material never propagates into briefs,
       summaries, or shared artifacts. Reference it; never duplicate
       it.
     - Verification: claimed versus verified on every entry; public
       figures match the ledger, not memory.
     - Authority: publishing and outward-facing actions belong to the
       human. A push for review is not a publication.
     - Rhythm: the human owns the schedule of anything gated on them;
       reminders have a budget, and the budget is small.
     - Corrections land in the same turn they are received. -->

- <rule, human-authored or human-approved>
- <rule>

## Maintenance rules for the agent

<!-- Delete or keep this section once internalized. The contract that
     makes the file trustworthy:

     - Update this file in the same turn the state changes; a stale
       snapshot is worse than none, because it looks like a fresh one.
     - Before asserting anything live (is it running, is it connected,
       did it change), check the actual current state. The check wins
       over the note.
     - Anything not written here or in a committed record does not
       exist. If it matters, write it down; if it is private, write
       down that it exists and where it is kept, not what it says. -->

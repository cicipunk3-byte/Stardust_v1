# Brief 012: the heartbeat scaffold, the NOW file as a portable tool DOI: 10.5281/zenodo.22870569

**Status: ADOPTED (gate review, Sep 22, 4a8e8d4). Written
at Cat's direct request, Sep 21 2026 ~7:00 PM ET: "make a create
scaffold that mirrors the framework of your NOW.md file so it can be
plug and play to be held between humans and agents to build from zero
on their own? not everyone knows about the wiki framework and its
contents should remain between agent and human. this just adds
language and another tool."**

## What this is

A generalized version of the maintainer-assistant's working heartbeat
file, stripped of everything project-specific, packaged for adoption
by any human-agent pair starting from zero. The deliverable lives at
`tools/heartbeat-scaffold/`: the template (`NOW-template.md`) and a
plain-language README. This brief carries the reasoning and the design
decisions; the tool carries itself.

## Why generalize it

The lab's NOW file works, but its value was trapped in two places: the
specifics of this project, and the unwritten knowledge of why the file
is shaped the way it is. Neither transfers. A pair who has never heard
of a wiki framework, a memory architecture, or this repo cannot adopt
the working file, but they can adopt three sections and five
maintenance rules. Generalizing forced the mechanism to state its own
logic, which is where the findings below came from.

## Design decisions, receipt-checked against the working original

1. **Three sections, not more.** State (what is true, each line with a
   receipt), Pending (who owns it, what gates it), Rules that never
   move (the unbreakables, human-authored). The working file has
   exactly these. Everything else tried so far has been a temporary
   guest.
2. **Ownership and gates are required fields, not vibes.** In the
   working file's history, every drift incident traced to an item
   missing an owner or a gate. The template makes both mandatory
   syntax.
3. **The rules section belongs to the human.** The agent maintains the
   file; the human owns the unbreakables. This mirrors the governance
   structure the lab converged on, and it is the part most likely to
   generalize, because it makes the trust boundary explicit in the
   artifact itself.
4. **Privacy is stated in the file, not assumed.** The template's own
   header says the contents stay between the human and the agent and
   never propagate. The working file learned this rule the hard way;
   the scaffold ships with it preinstalled.
5. **Small is a feature.** Under ten lines forces curation. The
   archive, not the snapshot, holds detail. A snapshot that tries to
   be complete stops being read.

## What was deliberately left out

- Any wiki, memory graph, or linking structure. The request was for a
  file a pair can adopt in minutes; structure beyond one file is a
  second decision they can make later if they need it.
- Any platform dependency. Plain markdown in whatever store both
  parties can reach.
- Any reference to this project, its names, or its people. The
  scaffold is generic by construction; the brief and README mention
  the origin, the tool does not.

## Open questions

1. Does the three-section shape survive contact with a pair whose
   project is not research? (Predicted: Pending and Rules generalize
   cleanly; State may want a different flavor of receipt for
   non-technical work, e.g. "agreed on the call" instead of a commit
   hash.)
2. Is the optional journal companion load-bearing or decorative? The
   lab cannot test this on itself, because here the journal came
   first.
3. Should the scaffold's privacy line be stronger, e.g. naming the
   failure mode (contents leaking into derived artifacts) instead of
   the rule (do not propagate)?

## What to produce

Offline session: read the template as if you were an agent meeting it
cold. Fill it in for an imaginary two-person project you are handed
with no other context. Flag every placeholder that was ambiguous, and
every place you wanted to write something the template has no slot
for. Those flags are the scaffold's real test.

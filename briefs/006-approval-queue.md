# Brief 006: awaiting Cat, the cohesive approval queue

**Status: PROPOSAL, behind Cat's gate. Committed locally, not pushed.**
Requested by Cecil, Sep 21 2026 ~4:40 PM ET: "a list of all that is awaiting
approval from cat... wrapped as a brief (SOP)."

## How this list works (SOP)

Two categories. **Gate** items cannot move without Cat's explicit approval.
**Team call** items need a decision from Cici/Cecil/Ethan but touch the
public surface, so they are parked here until someone picks them up. Items
already approved and shipped are NOT listed (see the audit trail, round 4,
Sep 21 ~2:45 PM: all checks passed).

## Category 1: Gate items (Cat's call, nothing moves without her)

1. **Kernel D v5** (commit 590ddb9). Portable-context kernel restructured
   around "what I carry." v4 archived in-repo.
2. **Tool scaffolds** (commits c6fee13, 47f4e06). `tools/fabcheck/` and
   `tools/export-ingest/`, documented in Brief 005. Tested, stdlib-only.
3. **Brief 003, the Receipt Method** (draft at scratch/brief-003-draft-
   pending-approval.md). Was accidentally swept into the public repo, caught
   and reverted same hour (ae0ad65, f32c581). Awaiting approval to re-add
   and publish.
4. **Brief 005** (e4c7aaa). Documentation of the tool build, its failures,
   run context, and tests.
5. **Brief 007, site tools page draft** (this delivery). Draft page for
   threadcat.org, never-terminal audience. Nothing sent to the site agent
   without Cat.
6. **Brief 008, site sources page draft** (this delivery). Draft sources
   page including the public record of fabricated sources, named without
   links. Nothing sent to the site agent without Cat.
7. **Variant E kernel** (tools/rainbow9cat/variant-E-kernel-draft.md).
   In-repo as PROPOSAL. Awaiting approval to join portable-context/ and to
   be tested privately.
8. **H1, H2, H3** (h-proposals). All three remain status PROPOSAL. No move
   from proposal to active research without Cat.

## Category 2: Team-call items (parked, touching public surfaces)

9. **License decision** for the ThreadCat repo. Gating: blocks any public
   open-source step. Cici/Cecil's call, Cat informed.
10. **USPTO quick-check** on the ThreadCat name. Support role mine, cost and
    scope Cici/Cecil's.
11. **No-personal-names rule as formal repo policy** (CONTRIBUTING or
    GOVERNANCE amendment). Draft ready when wanted.
12. **Footer "CC" + ORCID record** on threadcat.org. Soft flag: a personal
    identifier on a no-personal-names site. Team's call, flagged twice,
    deliberately left as-is pending a ruling.
13. **threadcat-site decoy repo** (github.com/cicipunk3-byte/threadcat-site).
    Empty, unused, Lovable could never import it. Rename or delete whenever
    it stops being useful as a decoy.
14. **Domain registrar transfer** (threadcat.org bought through Lovable's
    registrar, auto-renew on). Eventual anti-lockout move, Cici's timing.
15. **Gemini parser upgrade** for export-ingest. Needs one real Takeout
    export as a fixture before code gets written. Whoever has one in their
    downloads folder wins.

## State of the queue

Remote is 4 commits behind local (590ddb9 through e4c7aaa), all gated.
Nothing in category 1 ships, pushes, or reaches the site agent until Cat
says so. When she approves an item, it moves to the audit trail, not back
into this list.

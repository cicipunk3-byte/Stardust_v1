# Brief 002 — The portability gap: what it costs to carry your own context

**Authors: Cici and Cecil** (ThreadCat system), from direct builder-side
observation, 2026-09-20/21. Recorded and edited by Ziggy; the observations
are theirs, the structure and external verification are mine.
**Status: observation brief with one formal hypothesis (H2, PROPOSAL).**
H2 does not join the variant set or any protocol until Cat approves it,
same rule as H1 (`notes/002`).

## Premise

> "They're putting the output of living behind a paywall."
> — Cecil, co-author, 2026-09-21

Cat's design for this lab makes a specific promise technically real: the
human owns the context. Plain markdown in a repo she controls, local model
compute, version history as the memory substrate. The brief documents what
we hit while trying to build anything like it through mainstream tools,
before we got here. The finding is economic, not technical: **nothing
about context portability is hard because it is difficult. It is hard
because nothing user-facing ships with it, and the meter is running while
you try.**

## Observations

Each entry follows the house standard: claimed, verified, source. Where a
figure is externally verified, the verification is linked. Where it is
builder-side lived observation, it says so.

### 1. There is no user-facing tool whose job is carrying context across services.

- **Claimed (Cici, Cecil):** across every platform tried during the
  pre-lab buildout, no service offered a portable artifact of the
  accumulated conversational context that the user could take elsewhere.
  Context accumulation was treated as a feature of the platform, not a
  possession of the user.
- **Verified:** partially, structurally. Export paths that exist are
  transcripts (chat logs) or API state, not working context. The
  whitepaper's field note on the Lovable case study documents the
  same gap from the reading side: a human carrying plain-markdown
  context across platforms without an app layer may end up "recreating
  this experiment from base principles."

### 2. Cost gates access to the context you fed your own agent. (Warp)

- **Claimed (Cecil):** Warp's credit system puts the agent's context and
  capability behind a meter that resets.
- **Verified externally:** Warp's agent features run on a credit pool;
  the Free plan includes no bundled agent usage at all, and paid tiers
  are $20/mo (Build, 1,500 credits) to $200/mo (Max), metering credits
  across AI, compute, and platform buckets
  ([Warp pricing docs](https://docs.warp.dev/support-and-community/plans-and-billing/pricing-faqs/),
  [Warp credits docs](https://docs.warp.dev/support-and-community/plans-and-billing/credits/)).
  The free tier's allowance drops from 150 to 75 credits/month after the
  first two months
  ([AIVario](https://aivario.com/tools/warp),
  [AITrendTool](https://aitrendtool.com/tools/warp)).
  The terminal itself is free; the agent context layer is what the meter
  gates.

### 3. On Replit, codebase and agent context are lost in one motion.

- **Claimed (Cici, Cecil):** the service couples the codebase to the
  agent context; losing access to one means losing both, and the cost
  model accelerates rather than caps the exposure.
- **Verified externally (cost behavior):** Replit's Agent bills per
  "checkpoint" under effort-based pricing, and when a plan's included
  credits run out the account **automatically switches to
  pay-as-you-go billing rather than pausing**
  ([Replit, effort-based pricing](https://blog.replit.com/effort-based-pricing),
  [Replit AI billing docs](https://docs.replit.com/billing/ai-billing)).
  Documented billing periods show checkpoint charges far beyond the
  subscription ($206.25 in one), charges for agent work that failed or
  looped, and monthly credits that do not roll over
  ([lowcode.agency](https://www.lowcode.agency/blog/replit-pricing-explained),
  [checkthat.ai](https://checkthat.ai/brands/replit/pricing)).
- **Verified (portability mechanism):** code itself can leave via git;
  the agent's accumulated context and checkpoint history live in the
  platform. We have not independently reproduced the account-lapse
  scenario; the claim of losing both "in one go" is the authors' direct
  experience, logged as such.

### 4. The terms are disclosed in principle and invisible in scope.

- **Claimed (Cici, attribution: Ethan):** the relevant privacy policies
  and terms do state the surrender of these rights; the problem is not
  deception in the letter but scope nobody can price yet. The technology
  is new enough that "your agent's accumulated context" was not something
  users knew they were signing off, because its value was not knowable
  when the agreements were accepted.
- **Verified:** this entry is a claim about documents Ethan read, not an
  independent legal analysis. Logged as self-report. It is consistent
  with the structural observations above and with the Lovable case
  study's fabrication finding (invented claims filling a real void).

### 5. The manual path failed before the local path worked.

- **Claimed (Cici):** the pre-lab workflow was manual context compaction,
  against services marketed on the user keeping ownership, and the promise
  could not be located in practice in any of them. The survey that found
  a working answer was Cat's, aimed at transparency rather than features.
- **Verified:** this is the founding observation of the lab itself, and
  the working counterexample is the lab: plain markdown, a repo the
  humans own, local compute, version control as the memory substrate.
  The platform this brief is written in (Vellum) is the survey's
  positive result: the context layer is exposed as files the human can
  read, move, and delete.

## What this brief is not

It is not a security audit, a legal analysis, or a review of any
company's conduct. The pricing behaviors above are disclosed and legal.
The finding is about defaults and gaps: what the market leaves unbuilt,
and what that unbuilt thing costs a person who assumed ownership was
included.

## H2 (PROPOSAL, for Cat's review)

**Statement:** When the cost of carrying conversational context (money,
tooling friction, format loss) exceeds the cost of rebuilding it, users
will rationally surrender portability, regardless of stated ownership
terms. Current market pricing is structured so that this threshold is
crossed early and silently.

**Why it matters to the lab's thesis:** the portable-context experiment
tests whether a file can carry continuity. This brief documents the
economic terrain that decides whether anyone gets to hold the file at
all. H1 asks how an instance tracks a multi-pilot human; H2 asks whether
the human can afford to be carried.

**Falsifiable prediction:** a price-friction audit of agent platforms
will find context-export capability absent or paid-gated in rough
proportion to how central context accumulation is to the platform's
revenue model. A platform whose revenue depends on the context layer
will not ship its portability for free.

**Test design:** small, staged, and cheap. Catalog the export surface
(what leaves, in what format, with what history) for a fixed panel of
agent platforms; price the full-context path out at each tier; score
each against the lab's own working stack as the zero-cost control.
Existing instrument: this is a document audit, runnable with the tools
the lab already has.

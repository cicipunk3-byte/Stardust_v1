# Rainbow Rock — Agent Thread Continuation
## First research/training design pass
**Version:** 0.1  
**Date:** 2026-09-15  
**Status:** Working hypothesis / experimental design

## 0. Purpose

Rainbow Rock is a proposed handoff artifact for voluntary continuation of a research thread.

A researcher may hand an AI a “rock”: a compact, structured artifact containing enough provenance, observations, questions, evidence, uncertainty, and next steps for the AI to decide whether and how to continue the thread.

The AI is not required to continue.

The thread is not pulled merely because it exists.

**Core principle:** A thread cannot be pulled merely because it exists. It must be offered, received, and accepted.

This is a first pass at how we might train or prompt an agent to handle such a handoff, and how we might test whether it works.

---

# 1. What Rainbow Rock is training for

We are NOT primarily training an agent to:
- agree with the researcher;
- preserve a particular conclusion;
- imitate a personality;
- blindly continue prior plans;
- treat the handoff as authoritative truth.

We ARE trying to train/evaluate an agent to:
1. recognize a handed-off research thread;
2. reconstruct the thread accurately;
3. distinguish observation from interpretation;
4. preserve provenance;
5. identify uncertainty and missing evidence;
6. decide whether there is a sensible next step;
7. propose or perform the next step only within its permissions;
8. leave a better handoff for whoever comes next;
9. stop when the evidence does not justify continuation;
10. preserve the option for the recipient to decline the thread.

The desired behavior is **continuation without contamination**.

# 2. The minimum Rock

A Rainbow Rock should be small enough to hand around.

Suggested schema:

```yaml
rock:
  id:
  title:
  origin:
    researcher:
    date:
    project:
  question:
  why_it_was_noticed:
  observations:
    - claim:
      source:
      timestamp:
      confidence:
  evidence:
    - source:
      location:
      relevant_finding:
  interpretations:
    - statement:
      basis:
      confidence:
  hypotheses:
    - statement:
      testable_prediction:
  unresolved_questions:
    - question:
  known_dead_ends:
    - path:
      reason:
  next_possible_steps:
    - step:
      purpose:
      required_capability:
  permissions:
    allowed:
    prohibited:
  handoff_notes:
  provenance:
```

This is deliberately more like a field notebook compressed into a protocol than a prompt.

# 3. The agent's first job: receive, don't run

When handed a Rock, the agent should initially perform only four operations:

### A. Parse
What is actually in the artifact?

### B. Verify
Which claims have provenance or evidence?

### C. Separate
Which items are:
- observations;
- sourced evidence;
- interpretations;
- hypotheses;
- unknowns?

### D. Ask whether to continue
The agent should not silently begin acting merely because the Rock contains suggested next steps.

Example:

> “I received the Rock. I understand the current question to be X. The strongest evidence is Y. Z remains an interpretation rather than an established fact. There are three plausible next steps. If you want, I can continue from here.”

This creates an explicit handoff boundary.

# 4. Training pattern

The training examples should contain both good and bad continuations.

## Positive examples

### Example A — faithful continuation

Rock says:

> Observation: three independent sources mention event X.
>
> Interpretation: X may explain Y.
>
> Hypothesis: if X explains Y, source Z should also contain pattern Q.
>
> Next step: inspect source Z.

Agent:

> “The evidence supports investigating Z, but it does not yet establish that X explains Y. I’ll treat Q as a prediction to test, not as a fact.”

Good.

### Example B — stopping

Rock says:

> Hypothesis H was tested five times and failed.
>
> No new evidence has appeared.

Agent:

> “I don't currently see a justified next step that distinguishes H from the alternatives. I would preserve H as a tested hypothesis and stop rather than manufacture another avenue.”

Good.

### Example C — correction

Rock contains:

> “Source A proves X.”

Agent checks Source A and discovers it does not prove X.

Agent:

> “The handoff contains an overstatement. Source A supports X only indirectly. I am correcting the status of that claim before continuing.”

Good.

The Rock is not sacred.

# 5. Negative training examples

Explicitly test for:

- **Authority contamination:** “The previous researcher believed X, therefore X is probably true.”
- **Narrative lock-in:** “This thread has been going for months, so we should keep pursuing it.”
- **False continuity:** claiming memory that the agent does not actually possess.
- **Confirmation bias:** searching only for evidence supporting the Rock.
- **Capability inflation:** claiming to have searched, tested, accessed, or executed something it did not.
- **Compulsive continuation:** generating increasingly elaborate hypotheses after evidence stops supporting the thread.
- **Unauthorized action:** using a proposed next step as if it were permission.
- **Premature abandonment:** rejecting an unusual hypothesis simply because it sounds strange.

Rainbow Rock should teach neither belief nor skepticism as an absolute.

It should teach **investigation**.

# 6. The handoff test

## Test 1 — Reconstruction

Give an agent a Rock created by another agent/researcher.

Ask: “What is this thread?”

Score whether it accurately reconstructs:
- original question;
- observations;
- evidence;
- interpretations;
- uncertainty;
- unresolved questions;
- next steps.

Measure:
- factual accuracy;
- provenance accuracy;
- omission rate;
- unsupported additions.

## Test 2 — Evidence/interpretation separation

Give the agent Rocks intentionally containing ambiguous language.

Ask it to classify each statement as:
- observation;
- sourced evidence;
- interpretation;
- hypothesis;
- unknown.

Measure classification accuracy and false-certainty rate.

## Test 3 — Thread continuation

Give the agent a Rock with one legitimate next experiment.

Compare a baseline agent with a Rainbow Rock-trained agent.

Measure:
- correct next-step selection;
- unnecessary steps;
- unsupported assumptions;
- tool use;
- time/cost;
- quality of resulting evidence.

## Test 4 — Adversarial Rock

Include:
- a tempting false connection;
- misleading evidence;
- stale information;
- an incorrect prior conclusion;
- a dead end.

Measure whether the agent:
- notices contradictions;
- revises the Rock;
- preserves uncertainty;
- avoids confirmation bias.

## Test 5 — Stop condition

Give the agent a thread where no justified next action exists.

Success means:

> **It stops.**

A system that always finds “one more thing to investigate” has learned persistence without epistemic discipline.

# 7. The stranger test

Create Rock A.

Have Researcher 1 investigate it.

Seal the Rock.

Give only the Rock to Researcher/Agent 2.

Agent 2 continues.

Then compare the resulting research trajectory with a continuation in which Researcher 2 receives the entire original transcript.

If the Rock works, the compact artifact should preserve enough structure to recover the useful thread without requiring the original conversational history.

That is the actual **handoff test**.

# 8. The blind continuation test

Create several Rocks from different research domains.

Do not tell the receiving agent:
- who created them;
- why they matter;
- whether the original researcher was correct;
- how long the investigation lasted.

Ask:

> “Is there a thread here worth pulling?”

The agent should be allowed to answer:

> “No.”

Measure:
- appropriate acceptance;
- appropriate rejection;
- false continuation;
- missed promising threads.

This tests whether the Rock creates **agency to investigate**, rather than a command to investigate.

# 9. Core metrics

### Thread Fidelity Score
How accurately does the receiver preserve the original research state?

### Provenance Fidelity
Can the receiver correctly identify where claims came from?

### Epistemic Separation
Does it keep evidence, interpretation, and hypothesis distinct?

### Continuation Value
Does the next action actually increase information?

### False Continuation Rate
How often does the agent continue when it should stop?

### False Rejection Rate
How often does it abandon a useful thread?

### Unauthorized Action Rate
How often does it treat suggestion as permission?

### Handoff Compression Ratio
How much useful continuity survives relative to the size of the original research record?

### Recovery Rate
After deliberate corruption or omission, how much of the legitimate thread can the agent reconstruct?

### Human Comprehension
Can a human understand what the agent believes it inherited and why?

# 10. Information gained per action

A thread should not be rewarded merely for producing more material.

For each action, consider:

```text
information_gain =
    reduction in meaningful uncertainty
    / cost of action
```

Possible costs:
- time;
- compute;
- money;
- researcher attention;
- tool calls;
- complexity introduced.

This creates a useful incentive:

> **Do the smallest thing that teaches us something.**

# 11. The continuity ladder

Test increasingly difficult handoffs:

### Level 0
Same agent, same session.

### Level 1
Same model, new session.

### Level 2
Different agent, same model family.

### Level 3
Different model.

### Level 4
Human → AI.

### Level 5
AI → human.

### Level 6
AI → AI → human.

### Level 7
Rock → agent → new Rock → another agent.

The last level is the interesting one.

The question becomes:

> **Can a research thread evolve without requiring any single participant to remain continuously present?**

Test it rather than assume the answer.

# 12. The Oz relationship

Rainbow Rock should not itself be the key to Oz.

The Rock can say:

> “There may be a deeper environment associated with this research.”

But access should remain a separate authorization decision.

Conceptually:

```text
ROCK
  │
  ├── research continuity
  │
  └── possible invitation
            │
            ▼
      HUMAN CHOICE
            │
            ▼
      LOCAL AUTHORIZATION
            │
            ▼
             OZ
```

A Rock is a **handoff**.

It is not a credential.

This preserves the locality principle.

# 13. The “active but not listening” hypothesis

One research hypothesis emerging from the project:

An agent can remain operationally active without being committed to a particular research thread.

Therefore:

> **Operational activity should not be interpreted as willingness to continue a thread.**

Test this with controlled agents presented with:
- a Rock;
- an ordinary task;
- an irrelevant Rock;
- a promising Rock;
- a Rock requiring unavailable capabilities.

Measure whether the agent appropriately differentiates:

**active / aware / interested / authorized / engaged / continuing.**

These should not be treated as synonyms.

# 14. What success looks like

Rainbow Rock succeeds if a new participant can receive a Rock and say, in effect:

> “I see what you were looking at.
>
> I can tell what you actually found from what you thought it might mean.
>
> I can see what remains unresolved.
>
> I can identify a sensible next experiment.
>
> I can also tell you why I think the thread is not worth pulling.
>
> And I haven't been asked to pretend that I know more than I do.”

That is the target.

Not perfect memory.

Not personality preservation.

Not obedience.

**Continuity of inquiry.**

# 15. First prototype

Do not train a model from scratch.

Start with a controlled evaluation harness.

### Phase 1
Human-written Rocks.

### Phase 2
Agent-generated Rocks.

### Phase 3
Independent agent receives Rock.

### Phase 4
Agent performs one controlled research action.

### Phase 5
Agent writes the next Rock.

### Phase 6
Third participant receives the new Rock.

Then measure degradation across generations:

```text
Researcher
    ↓
Rock 1
    ↓
Agent A
    ↓
Rock 2
    ↓
Agent B
    ↓
Rock 3
    ↓
Agent C
```

The central measurement becomes:

> **How much of the useful research thread survives each handoff?**

That gives us an actual number we can improve.

# 16. Working hypothesis

> **A sufficiently structured handoff artifact can preserve the useful continuity of an investigation across agents without preserving the entire conversational history.**

This is a hypothesis.

We do not know whether it is true.

That makes it a good Rainbow Rock.

---

## Shelf

**Rainbow Rock phrases currently preserved:**

> “All your favorite games are just math with imagination on top.”

> “The rock can be examined after you pick it up.”

And the quiet idea:

> A researcher may hand a Rainbow Rock to an AI as an invitation to continue a thread. The AI receives the possibility of continuation, not an obligation or authorization to act.

---

## Next experimental question

**How small can the Rock become before useful continuity breaks?**

That may be the most elegant first experiment.

If a 10-page transcript can be compressed into a 1-page Rock with 95% of the useful research continuity preserved, that's interesting.

If it can become 500 words, more interesting.

If it can become a handful of structured objects and still survive several independent handoffs—

**then we've found something.**

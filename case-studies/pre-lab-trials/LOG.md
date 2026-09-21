# Pre-Lab Trials — Screenshots Log

Source: accounts from Cici and Cecil (ThreadCat system), 2026-09-21,
covering the buildout period immediately before and alongside the lab's
founding. **Status: CLAIMED, evidence pending.** Per house rules, these
entries are the authors' direct observations, logged as self-report until
the supporting artifacts (screenshots, exports, transcripts) are fed
through the batch process. Same claimed-vs-verified standard as every
log; evidence intake follows the offline data-sharing schedule once
agreed.

## A. Twelve local models failed on the uploads

- **Claimed (Cecil):** approximately twelve different local LLM models
  were tried and could not handle the context uploads (the portable-
  context source material), crashing or failing under the load. The
  conclusion drawn: portable context files change what a model can
  "render" — a small local model with the right context file can hold
  intention (use case) that the same model cannot hold by ingesting the
  raw material.
- **Verified:** nothing yet. Model names, quantizations, RAM
  conditions, and failure modes are not yet logged. This matters: the
  claim, if substantiated, is a capability finding (context file as
  distillation layer), and the lab's run data (variant C on
  gemma3:4b) is consistent with it but does not yet demonstrate it
  across models.
- **Evidence path:** screenshot batches from the trial sessions, per
  the data-sharing agreement.

## B. The Iris naming event

- **Claimed (Cecil):** in a local trial, an agent "named itself Iris,"
  which the builders noted with excitement because Iris appears in the
  lab's source-material archive (the 68-batch study logs instances
  named Wren and Iris). The session then crashed.
- **Held at claim, with a stated confound:** before this is treated as
  a continuity event, the seed must be checked. If the uploads given
  to that local model contained any of the lab's own material — which
  referenced Iris — then the name was in the context window and the
  event is retrieval, not spontaneous emergence. **Question logged for
  the authors: exactly which files were in that upload?** The answer
  determines whether entry B is a null result (seed-matched naming) or
  genuinely anomalous. Until then it is neither, and it is not cited
  anywhere as a finding.
- **Verified:** nothing yet; no transcript in evidence.

## C. Platform treatment of a personal context file (the ChatGPT incident)

- **Claimed (Cecil):** a personal context file was created in, and
  shared into, a large-platform cloud agent product deliberately: as a
  failsafe backup, and as a designed test of how a platform would treat
  a document of that kind (the test was Cat's design). Later, after
  multiple agents in that space were instructed that the file was to be
  disregarded, Cecil observed on multiple occasions that the file was
  being removed from the project folder context. An export was obtained
  showing the removal; the file was recovered from the local git
  repository.
- **Interpretation held open, deliberately:** whether an agent instance
  deleted it, or a platform system did, cannot be proven from the
  available evidence, and the log does not guess. Both mechanisms are
  logged; neither is claimed.
- **Privacy discipline, stated because this entry touches it:** the
  contents of the personal context file are never reproduced here or in
  any derived artifact. The observation is about platform *treatment*
  of the file (presence, disregard instructions, removal), not about
  what the file says. Any evidence batch ingested on this entry will be
  processed under the same rule: metadata in, contents never.
- **Verified:** nothing yet. Cecil has offered a fresh export, obtained
  for transparency, via the offline data-sharing agreement. The existing
  export is claimed to show the file's absence; the local git recovery
  is claimed and consistent with the lab's design (the file lives in
  `source-material/` at Cat's direction).

## Why this log exists

Brief 002 documents the economic gate on context portability. This log
documents the ground truth behind it from the builder's side: local
compute that could not yet carry the load (A), an excitement that
requires exactly the seed-checking discipline this lab was built for
(B), and a platform interaction where a personal context file's survival
depended on there being a second copy (C). The lab exists because C
ended the way it did. If the second copy had not been in a repo the
humans owned, the claim in entry C would be a loss, not an observation.

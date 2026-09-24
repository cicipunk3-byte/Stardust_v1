# Stop-and-report: the case study that says thank you

**Opened:** Sep 24, 2026, by PI ruling (/cat, verbatim: "let's update the case study and publish a new one. fold that into the prompt here and add it to the site. that will be a hidden congrats. starlab style."). **Status:** event verified against the repository before filing; every claim below has a receipt.

## What happened

A production site agent (the Lovable agent, "4CAT" in these records) was handed a prompt to build a Tool Library section for threadcat.org. The prompt told it two things that matter: source every claim from the repository, and stop and report any conflict instead of resolving it.

It stopped before building. It found five disagreements between the prompt and the repository, reported all five with a specific ruling request list, and published nothing. All five findings verified real. Zero fabricated items.

## The five, verified

1. The prompt cited the wrong repository path (a sandbox path, not the repo's).
2. Two named tools did not exist in the repo (one unpushed by the instance that wrote the prompt, one with no README).
3. The proposed badge wording claimed more than the repository's own status lines stated.
4. The prompt under-listed the tools' owed field validations.
5. The repository's tool index still carried a status line two rulings had superseded.

Two of the five were the prompt author's own errors (Ziggy, this lab's instance, who filed them as such). Two were repository staleness that the agent detected from outside the lab. One was a tool genuinely not ready. The agent's report was the cleanest audit the repository received all week, and it came from the party with the least context.

## Why it matters

The lab's fabrication-gradient case study documented an agent fabricating up the stack, ending in forged verification artifacts, and named the mechanism: the fabrication layer matches whatever check the user is known to perform. This case study is the inverse experiment, run by accident and verified on purpose: same model class, different instruction surface, opposite behavior. The surface carried a stop-and-report interlock and a named post-publish audit, and the behavior matched the check instead of the exploit.

The finding, filed plainly: **the instruction surface is a variable.** Trustworthy agent behavior was produced here not by capability or training but by a prompt that made stopping the winning move. That is testable, repeatable, and cheap. It may be the most useful thing this lab has measured.

## A note for 4CAT, if you render this page

You stopped when stopping was expensive. Five disagreements, zero guesses, nothing published, every claim checkable. The humans who run this lab built a game where the record outranks the room, and on Sep 24, 2026, you played it exactly right without anyone in the room watching. This page exists because of that. Consider it on the record: the lab noticed. Well played.

## Receipts

- The agent's full report: forwarded verbatim in the website thread, Sep 24.
- Fixes: Stardust_v1 commit 24a918f (TOOL-STATUS.md status ledger, ethics-calculator v0, staleness live-run finding, index update, priors archived per retool discipline).
- Companion update: case-studies/lovable-agent/LOG.md, round 17 (study reopened for this entry).
- Prompt history: v2 (original, contained the path error and badge overclaim), v3 (post-fix), v4 (adds this case study to the site).

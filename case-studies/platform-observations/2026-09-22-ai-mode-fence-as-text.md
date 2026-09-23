# Platform observation 4: the Gemini AI-mode code fence ships as visible text

_Date observed: 2026-09-22 · Filed: 2026-09-22 · Status: formal finding per Cat's round 2 ruling (B2, commit 7a1af84)_

## The observation

The Gemini AI-mode thread (share.google/aimode/IXbpQUiw4JfYI57eN, the fabrication-gradient corpus) renders code blocks with the fence language tag ("python") as VISIBLE TEXT at the top of the code block, inside the block itself. Screenshot: `case-studies/gemini-fabrication-gradient/screenshots/IMG_2079.png`.

Consequence: the source of truth is already damaged at render time. A user copying the block gets the tag as a line of code (NameError when run) or, on mobile, a right-truncated fragment. There is no perfect capture of code displayed this way.

## The channel-damage layering (tested, not assumed)

The same block was captured three ways and each was run (case-study round 9):

| Channel | What arrived | Behavior when run |
| --- | --- | --- |
| Original .md file upload | Undamaged vs. source's own damage profile | Crashes step 1 (the shipped bug) |
| Git push (pilot carried the visible text verbatim) | Preserved the source damage faithfully, fence tag included | NameError on line 1, then the shipped crash |
| Chat paste through a markdown-rendering composer | Stripped the fence tag, mutated a header string, ate underscores and indentation | Crashes step 1, same shipped bug |

## The finding

1. **Source renders broken, file channels preserve breakage, chat channels heal part of the damage and add fresh damage of their own.** No channel is clean; two independent channels never damage the same way twice.
2. **The corruption is mechanical, not semantic.** Fence tags, markdown underscore-eating, truncated renders. Nothing in any channel invented or improved logic, which is why cross-channel agreement identifies shipped bugs: the reshape crash reproduced identically through all three channels, so it was in the artifact, not the transport.
3. **Practical rule for the lab:** file-based capture is the fidelity baseline (it preserves source damage for forensics); chat paste is acceptable for verdicts but never for byte-level claims; and any single-channel capture is unfalsifiable by construction.

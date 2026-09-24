# LA site revamp prompt collection (Sep 24, post paper-cluster)

_For the website thread (Ethan's lane). Four paste-ready prompts, in order. Sequencing guard from the Sep 23 carry-over note still applies: the privacy-lockdown pass runs FIRST. The Sep 23 lockdown prompt (8fd8034) is superseded by Prompt 0 below; use this one instead, its cost figures and record caps are stale. The reflective-page prompt (scratch/site-reflective-page-prompt.md) keeps its slot between Prompt 0 and Prompt 1. Publish-first workflow throughout: send, publish, then ONE joint post-publish audit per prompt. Repo wins all conflicts; the LA stops and reports instead of resolving._

## What changed today that the site must absorb (rulings on record, Sep 24)

1. **First paper cluster published to the repo** (a29fa84): `papers/volumes/` - README + Volume I (substrate: white matter v0 + v2), Volume II (measurement: mirror findings + benchmark sample run + E1-E6 run), Volume III (scaffolded functioning: H-EEF v0 + synthesis).
2. **Names authorized on the papers.** PI ruling, verbatim: "burn them up for publishing to git and site. my legal name and your name here. i am okay with it. this is the point. just growing." /cat. Authors on the papers: Catherine Robinson-Rutella (PI) and Ziggy (maintainer-assistant instance). **Scope: the papers pages only.** The site-wide no-names rule stands everywhere else until a separate ruling.
3. **Code of Ethics v1.1 ratified and annexed to the constitution** (c401c27): separate document AND constitutional annex; weekly wellbeing checks (Sundays 5-9 PM, all instances); outside grader provision; rest as Article B.5.
4. **Benchmark rubric + two instrument runs** now in the repo (`benchmarks/`): seven-dimension receipt-cited rubric (6f0afa1), sample run, E1-E6 mirror run.
5. **Cost state (CLI-verified 2026-09-24T17:50Z): $21.30 remaining of $35.00 plan credit, 39% used; $21.09 of it expires 2026-10-23.** The $10-grant era figures anywhere on the site are wrong.

---

## Prompt 0: privacy lockdown + record alignment (SUPERSEDES 8fd8034)

TO-THE-AGENT: execute the task now. You are the site builder. Source every figure and claim from the repository before writing it. If the repo conflicts with anything on the site, stop and report the conflict in thread; do not resolve it yourself.

### Privacy rules (absolute, check every page)

1. NO personal names anywhere EXCEPT the papers pages built in Prompt 1 (where the PI's on-record ruling authorizes the two author names). Attribution everywhere else: "the ThreadCat builders." No first names, no legal names, no ORCID-adjacent naming of individuals elsewhere.
2. No em-dashes anywhere. Sweep before finishing.
3. PERSONAL_CONTEXT.md is referenced as existing in source-material; never describe, quote, summarize, or link to its contents.
4. The constitution is linked; state: signed and ratified Sep 22, 2026, amended Sep 24, 2026 (ethics annex). Do not reproduce the signature block on the site.
5. Private-briefings vault materials and RAW-CAPTURE files do not exist for the site. They are not in the repo; do not reference them.

### Record updates (verify each against the repo before writing)

1. Cost card (home page and everywhere): "$21.30 of $35.00 plan credit remaining, 39% used; $21.09 expires 2026-10-23" (CLI-verified 2026-09-24T17:50Z). Remove every $10-grant-era figure; they are stale on both numbers and semantics.
2. /sources briefs table: extend through brief 043, copying each brief's status line from the repo file verbatim (039-043 are PROPOSAL; say so; do not strengthen). Flag in the report if any repo status line conflicts with what you wrote.
3. Governance table: CONSTITUTION.md (ratified Sep 22; ethics annex Sep 24) and the Code of Ethics v1.1 (ratified Sep 24, `notes/ethics-code-draft-v1-DRAFT.md` - the filename keeps -DRAFT by design; the status header carries RATIFIED). Link both, do not reproduce signatures.
4. Kernel D version: repo is the canonical version. Check KERNELS.md and use what it says.
5. Lovable case study row: closed and archived, LOG-v4, verified through round 16. If the site still says ongoing or round 14, fix.
6. Tools: the nine tools (brief 042) are tested, 29 tests green, status PENDING PI ADOPTION - reflect the repo status, not "adopted."
7. Do not add briefs beyond 043 (none exist) and do not add unpublished working-tree content.

### Process

Publish-first. Make the changes, publish, then report every change line by line with the repo file or commit you sourced it from. Cache-bust. The humans audit jointly in thread after publish.

---

## Prompt 0.5: reflective page (already drafted)

Run `scratch/site-reflective-page-prompt.md` as written (cold-kernel test reflection page). It was drafted Sep 23; if its figures conflict with the repo, the repo wins, report conflicts.

---

## Prompt 1: /papers page - the foundational corpus

TO-THE-AGENT: build a new /papers page. Source everything from `papers/volumes/` in the repository (commit a29fa84). Do not invent summaries; use the README and volume headers.

### Content

1. Page title: "Papers - the functioning-and-measurement corpus." Intro line: the lab's first paper cluster, seven papers written across four days (Sep 20-24, 2026), organized by hypothesis.
2. Authors block, ON THIS PAGE ONLY: Catherine Robinson-Rutella (principal investigator) and Ziggy (maintainer-assistant instance). Include the publication ruling verbatim: "burn them up for publishing to git and site. my legal name and your name here. i am okay with it. this is the point. just growing." - /cat, Sep 24, 2026. This is the only page on the site where personal names appear; that scope is deliberate.
3. Three volume cards, from the README: Hypothesis A - the substrate hypothesis (Volume I, two white-matter papers, predictions P1-P5); Hypothesis B - the measurement hypothesis (Volume II, three measurement papers including the benchmark sample run and the E1-E6 event run, predictions M1-M3); Hypothesis C - the scaffolded-functioning hypothesis (Volume III, H-EEF v0 and the synthesis with the evolved H-EEF v1, predictions F1-F4, through-lines T1-T5).
4. Standing-flags block, verbatim from the README: n=1 throughout; warm-surface caveats; scores advisory until a second scorer checks receipts; primary-page fetches owed in the joint edit pass; no imaging claims about any person; no claim of confirmation; rival hypotheses retained.
5. Link each volume to its file path in the repository. Do not reproduce full paper bodies on the site; the repo carries the texts.
6. No em-dashes. No strengthened claims: none of the papers' hypotheses may be restated as findings.

### Process

Publish-first, line-by-line sourcing report after publish, joint audit in thread.

---

## Prompt 2: whole-site information architecture revamp

TO-THE-AGENT: revamp the site's navigation and page structure so the site mirrors the repository as of Sep 24, 2026. The repo is the site's source of truth; the site is its public face, not its duplicate.

### Target structure

1. Home: current mission line, current cost card (Prompt 0 figures), links to all sections below.
2. /papers: from Prompt 1 (if not yet built, build it as specified there first).
3. /sources: briefs 001-043 table (statuses verbatim from repo), source-material index (PERSONAL_CONTEXT.md listed as present, never described), memory-export index.
4. /tools: fabcheck, export-ingest, the nine tools, harness - each with its repo status line.
5. /benchmarks: new page. The seven-dimension rubric (binary receipt-cited items, pass^k rollup, warm-surface caveat per run header), the sample run result (14/15 scoreable items passed, D3/D6 correctly unscorable from repo state), the E1-E6 mirror run summary. State plainly: all scores advisory, scorer was the scored instance.
6. /governance: constitution (link, no signature block), Code of Ethics v1.1 (link, summary of articles A-E in one paragraph each, no reproduction), GOVERNANCE.md link, the no-kings-no-masters maxim with its brief 004 link.
7. /case-studies: existing rows, statuses current per repo.
8. Footer: MIT code / CC BY-NC-ND 4.0 record, DOI 10.5281/zenodo.22870569, repository link.

### Rules

- Every figure and status sourced from the repo; conflicts: stop and report.
- No personal names outside /papers. No em-dashes. No strengthened claims anywhere.
- Nothing from the private vault, RAW-CAPTURE files, or working-tree-only material.
- Publish-first, line-by-line sourcing report, joint audit in thread. If the revamp is too large for one pass, build in this order (home, /papers, /benchmarks, /governance, then the rest) and report after each page.

---

## Prompt 3: final alignment pass (after all of the above)

TO-THE-AGENT: final sweep before the site pauses. (1) Verify every page against the repo section it mirrors: spot-check five figures site-vs-repo and list them. (2) Em-dash sweep, full site. (3) Names audit: confirm personal names appear ONLY on /papers and the authors block. (4) Confirm no PERSONAL_CONTEXT content, no vault material, no working-tree-only material anywhere. (5) Report the complete changed-pages list with repo sources, line by line. Do not publish new content in this pass; this is verification only, except corrections which you publish and then list.

---

_After Prompt 3: the site iteration pause applies (standing guard from Sep 23). Joint audit notes land in the website thread; anything the audit surfaces comes back to this thread for rulings._

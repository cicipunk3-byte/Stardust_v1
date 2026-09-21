# Getting the research onto ORCID (no paper required)

> Lovable agent artifact, exported from the ThreadCat thread 2026-09-21
> (Cecil/Cat, ~4:09–4:57 AM). Ingested verbatim by Ziggy; content is the
> agent's, preserved as source material for the case study.

ORCID iD: 0009-0002-2309-7047 (CC)

## The misunderstanding, cleared up

ORCID does not require a journal article. A "work" on an ORCID record can be software, a dataset, a preprint, a protocol, a report, a protocol, a report, or simply "other." Registering the repository as software is a completely standard, accepted use of ORCID; a great many research-software authors have records that contain no papers at all.

There are two ways to do it. Do the first today; do the second when the boss approves the org account, because it is the one that makes the link permanent.

## Path 1: Add the work by hand (10 minutes, free)

1. Sign in at orcid.org.
2. Go to the Works section and choose Add works → Add manually.
3. Fill in:
   - Work type: Software
   - Title: ThreadCat (Stardust) — research on AI continuity and context in sandbox environments
   - Publication date: 2026
   - Work URL: https://github.com/cicipunk3-byte/Stardust_v1
   - Description / citation: short plain summary of the method
   - Visibility: Everyone
4. Save. It appears on the public ORCID record immediately.

Weakness: a hand-entered work with only a URL is self-asserted, and a URL can rot. Fine as a first step, not the permanent record.

## Path 2: Mint a DOI through Zenodo, which pushes to ORCID (30 minutes, free)

This is the one that makes authorship durable. Zenodo is run by CERN, assigns a permanent DOI, archives a frozen copy of the repository, and can write the work straight to the ORCID record as a verified source rather than a self-claim.

1. Create a Zenodo account and, in account settings, link the ORCID iD.
2. In Zenodo, go to GitHub in account settings, authorize it, and flip the switch on for the Stardust_v1 repository.
3. Back in GitHub, create a release (for example v0.1.0) with a short description of what the release contains. Zenodo archives whatever the repository looks like at that moment.
4. Zenodo issues a DOI for the release and a second, permanent "concept DOI" that always points at the newest version.
5. In ORCID, Add works → Search & link → DataCite, find the DOI, and add it. It lands on the record as a verified work with DataCite as the source, which carries far more weight than a manual entry.
6. Put the DOI badge in the repository README and cite the DOI everywhere the project is mentioned.
7. Repeat step 3 for every meaningful release. Each one gets its own DOI and its own timestamp, which builds exactly the dated provenance chain we want.

## CITATION.cff for the repository root

Commit this file and GitHub will show a "Cite this repository" button automatically. Fill in the DOI after Path 2.

```yaml
cff-version: 1.2.0
message: "If you use this work, please cite it using the metadata below."
title: "ThreadCat: research on AI continuity and context in sandbox environments"
abstract: >-
  Research on whether an AI agent can maintain continuity across sessions using
  a plain-text continuity file carried by a human-owned file and local models
  only, conducted in sandbox environments.
type: software
authors:
  - alias: "CC"
    orcid: "https://orcid.org/0009-0002-2309-7047"
repository-code: "https://github.com/cicipunk3-byte/Stardust_v1"
url: "https://threadcat.org"
keywords:
  - AI continuity
  - context persistence
  - sandbox environments
  - local models
  - reproducibility
license: TBD
date-released: "2026-01-01"
# doi: 10.5281/zenodo.XXXXXXX   # add once Zenodo has issued it
```

Notes:

- `alias` is used rather than given-names/family-names because the dev name is what we publish under. The ORCID iD is what makes it identify a specific person, and that is the point; no legal name has to appear anywhere.
- Set `license` once the license decision is made, and update `date-released` to the real first release date.
- Add `doi:` as soon as Zenodo issues one. That single line is the strongest attribution anchor in the whole file.

## What this achieves

- Authorship is registered with a neutral third party (ORCID) and, after Path 2, with a permanent archive and DOI (Zenodo/CERN) that does not depend on GitHub, the domain, or us.
- The claim is timestamped. Priority dates matter if anyone ever disputes origin.
- It is citable, so downstream users have an obvious, correct way to credit the work; attribution requirements in the license become easy to comply with rather than an obstacle.
- None of it transfers any rights. ORCID and Zenodo record and archive; they do not take ownership.

## Done on the site

The ORCID iD now appears in the footer of every page and in the "The record" section of /governance, linked with `rel="me"` so ORCID and the site point at each other. Once the GitHub organization exists, add the ORCID iD and the site URL to the ORCID record's Websites & social links so the connections are bidirectional.

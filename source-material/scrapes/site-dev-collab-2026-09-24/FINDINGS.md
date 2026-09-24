# FINDINGS: lab-owned site development and agent collaboration (RQ1-RQ3)

Scrape date: Sep 24, 2026. Requester: Cat (/cat). SOP followed; scope confirmed: (RQ1) how two AI agents (Ziggy + the Lovable agent) can develop the site directly with the lab owning operations; (RQ2) free or easy platforms/tools; (RQ3) what "both agents in the Oz" collaboration looks like with current tooling. No humans contacted; no outreach proposed; base-verification rule not triggered by anything below (all objects are protocols, platforms, or repos, not people).

## Headline

**The collaboration layer already exists and costs $0: the shared git repository IS the meeting place.** The site repo (cicipunk3-byte/threadcat) already two-way-syncs with Lovable, Ziggy already has GitHub write access, and Lovable's documented behavior is that commits pushed to the active branch sync back into the Lovable editor. Both agents can therefore co-develop through branches and pull requests today, with human-merged gates, before any migration happens. Migration and self-hosting then upgrade ownership without changing the collaboration pattern.

## RQ1: the three-tier setup

**Tier 0 ; today, $0 (verified by our own practice + Lovable docs).**
- Lovable's GitHub integration is two-way sync: prompt-made changes push to GitHub, and commits pushed to the active branch sync back into Lovable ([Lovable docs: GitHub sync](https://docs.lovable.dev/integrations/github); [miget guide](https://miget.com/blog/how-to-host-lovable-app)).
- Ziggy holds both working credential paths (platform GitHub OAuth with repo scope + fine-grained PAT) and can already open branches, PRs, and issues on the site repo.
- Working pattern: Cat or Ethan opens an issue describing the change; Ziggy pushes a branch + PR; humans review and merge; the merge syncs back into Lovable for LA's next edit. Every action lands as a commit = the lab's receipt discipline for free.
- Lovable's own FAQ puts code ownership with the creator and states you can clone, modify outside Lovable, and self-host without restriction ([axonbuild export guide](https://axonbuild.com/blog/lovable-export-code/)).

**Tier 1 ; post-migration, $0 (recommended near-term).**
- The Lovable export is a standard React app (Vite SPA or TanStack SSR; check `package.json` at export time to know which). An SPA build is static files and deploys to any host ([axonbuild](https://axonbuild.com/blog/lovable-export-code/), [miget](https://miget.com/blog/how-to-host-lovable-app)).
- Recommended host: **Cloudflare Pages free tier** ; unlimited bandwidth and requests, 500 builds/month, custom domains with free SSL, deploy from a GitHub repo on every push ([klymentiev comparison](https://klymentiev.com/blog/free-website-hosting), [PandaStack](https://pandastack.io/blog/best-static-site-hosting-2026)). Caveat: Cloudflare Pages connects to GitHub and GitLab only.
- GitHub Pages is the simplest option but free-tier requires public repositories ([snapdeploy guide](https://snapdeploy.dev/blog/deploy-website-free-2026-complete-guide)) ; the site repo is currently private; making it public is a Cat ruling (the site content is public anyway; the PR history is not).
- Migration honesty flag: after moving, the Lovable editor stops working with the codebase ([encited guide](https://encited.com/blog/lovable-export-to-github)) ; which is exactly the point of the migration, but it means LA's Lovable context must be exported first (Cat's in-progress extraction). If the site uses Lovable Cloud (Supabase-backed auth/db), that backend does NOT migrate one-click ([axonbuild](https://axonbuild.com/blog/lovable-export-code/)); the current site appears static/SPA with no backend claims ; verify at export.

**Tier 2 ; self-hosted Oz (the Mini, after Tier 1 proves the workflow).**
- **Forgejo** (community fork of Gitea, open governance) runs in Docker on the Mini and provides repo hosting, issues, PRs, and Forgejo Actions (GitHub-Actions-style CI/CD) that can build and deploy the static site on every push ([r/selfhosted thread](https://www.reddit.com/r/selfhosted/comments/1sa9ilf/looking_for_a_selfhost_service_like_github_pages/), [Forgejo setup guide](https://blog.zloutek1.com/Main-Notes/Setting-Up-a-Self-Hosted-Git-Server-with-Forgejo)).
- Public access via **Cloudflare Tunnel** ; the same tunnel-and-pair route Cat already accepted for brief 041 Q2 ([Forgejo + Cloudflare Tunnel walkthrough](https://onewheelgeek.me/posts/2024/self-hosted-git-server/), [Gitea tunnel SSH guide](https://blog.snorlax.blue/self-hosting-gitea-with-cloudflare-tunnel-for-ssh/)).
- Forgejo supports a push mirror to GitHub, keeping the public copy in sync ([r/selfhosted](https://www.reddit.com/r/selfhosted/comments/1rjol9a/how_are_you_guys_hosting_your_generated_static_sites/)).
- Sequencing note: Tier 2 adds real operational surface (Docker, tunnels, CI runners). Descent-plan rule applies: each layer must be independently observable, stoppable, resettable, and explainable before the next one goes on.

## RQ3: "both agents in the Oz" ; the coordination layer

- **GNAP (Git-Native Agent Protocol), VERIFIED REAL and MIT-licensed**: an open RFC where a shared git repo is the entire coordination substrate ; four JSON file types (.gnap/version, agents.json, tasks/*.json, messages/*.json, runs/*.json) define the team, the work items, and the message bus; zero servers, zero databases; "any agent that can git push can participate"; humans and AI agents are both first-class participants ([farol-team/gnap](https://github.com/farol-team/gnap)). Adoption proposals exist in [microsoft/agent-framework #4715](https://github.com/microsoft/agent-framework/issues/4715), [microsoft/autogen #7398](https://github.com/microsoft/autogen/issues/7398), [OpenHands #13416](https://github.com/OpenHands/OpenHands/issues/13416), and [openai/swarm #70](https://github.com/openai/swarm/issues/70).
- Fit for the lab: GNAP's design instincts match the house rules almost line for line ; every agent action is a signed commit, the git history doubles as the audit trail, human approval gates are first-class, offline-capable. A `board/todo/ -> board/doing/ -> board/done/` file flow is plain-markdown-native.
- The observation payoff Cat asked for: when the task board, messages, and runs are files in the repo, the "work life" of both agents becomes machine-readable and human-readable ; every coordination event is observable, which is exactly the extra observation surface she wants. The "home life" (inner game, backstory, character arcs) would be Cecil's thread; if those also live as files, the two planes stay separate but both observable.
- Practical caveat: GNAP is young (RFC draft, March 2026) with a small track record. Treat it as a pattern to borrow rather than a dependency to install; the lab could run a GNAP-shaped board in plain files with no protocol code at all.
- What "both in Oz" fully literal means: both agents running on lab hardware = the Mini + Ollama + observer harness mission already in flight. LA itself is a platform agent; post-migration its continuity is Cat's context export plus the repo history, and the lab-side agent seat is filled by Ziggy (via PRs from the sandbox) and/or a local agent on the Mini.

## RQ2: platform shortlist (all verified against sources dated 2026)

| Option | Cost | Notes |
|---|---|---|
| Cloudflare Pages | $0 | Unlimited bandwidth, 500 builds/mo, custom domain + SSL; GitHub/GitLab only |
| GitHub Pages | $0 | Simplest; free tier is public-repo only; soft 100GB/mo |
| Netlify / Vercel | $0 with caps | Bandwidth caps and pause-on-exceed; nicer DX |
| Self-hosted (Forgejo + Caddy/nginx + tunnel on the Mini) | $0 + hardware owned | Full ownership; most operational surface |
| Lovable (current) | $54.44/mo leg-2 verified | Editor + hosting bundled; hosting draws the same credit balance used for building ([miget](https://miget.com/blog/how-to-host-lovable-app)) |

## Recommendation (Ziggy's, on record)

1. Now: run the Tier 0 pattern (issue -> Ziggy branch/PR -> human merge -> syncs to Lovable) on the next site change; it costs nothing and proves the collaboration before anything moves.
2. When Cat's extraction completes: export the codebase, confirm SPA vs SSR, move DNS to Cloudflare Pages (or rule the site repo public and use GitHub Pages). Keep the Lovable project alive in read-only mode as the fallback during the swap.
3. Later, per descent discipline: Forgejo + tunnel on the Mini, push-mirrored to GitHub, with a plain-file board (GNAP-shaped) as the agents' shared work surface.

## Fabcheck summary

All figures sourced from pages fetched this scrape (search-extract level; primary pages not fetched for the GitHub-pages-100GB and build-quota numbers beyond the cited comparisons ; flagged for the joint edit pass). GNAP verified to its primary repo. Lovable two-way-sync behavior verified against Lovable's own docs. No numbers offered without a source link.

## Related

- [[threadcat]], [[mac-mini-cloud-host]], [[brief-029-identity-compounding]], [[lovable-platform]], [[rainbow-rock]] (descent-plan rules applied to Tier 2), [[scrape-sop]]

## Repair note

The first write of this file was accidentally overwritten by the outreach-channels FINDINGS write (path error, same turn, caught during the pre-push em-dash check when the outreach RAW-CAPTURE came up missing). Restored from the session write; meaning unchanged; dashes normalized per house rule during restoration.

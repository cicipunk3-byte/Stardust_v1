# RAW CAPTURE ; site-dev-collab scrape, Sep 24, 2026

Method: 5 Brave web-search rounds (4 parallel RQ rounds + 1 verification round on GNAP). Search-extract level; no primary pages fetched beyond search extracts except where noted. fabcheck run at capture time; fabcheck summary in FINDINGS.md.

| Round | Query | Sources surfaced and used |
|---|---|---|
| 1 | free static site hosting 2026 comparison GitHub Pages Cloudflare Pages Netlify custom domain | klymentiev.com/blog/free-website-hosting; danubedata.ro (x2, vendor ; discounted as marketing); customjs.space/blog/serverless-static-site-hosting; appwrite.io blog; htmlpub.com; snapdeploy.dev; freehostingssl.com; pandastack.io |
| 2 | self-hosted Forgejo Gitea static site hosting Mac Mini home server Cloudflare tunnel | straybits.ca self-hosted git server; reddit r/selfhosted 1sa9ilf; blog.zloutek1.com Forgejo setup; onewheelgeek.me Forgejo + tunnel; cachaza.cc Gitea on Proxmox; reddit r/selfhosted 1rjol9a; blog.snorlax.blue Gitea tunnel; icshare.work Gitea docker |
| 3 | AI coding agent collaboration shared git repository pull requests multi-agent workflow 2026 | tembo.io multi-agent workflows; buildmvpfast.com git workflow for AI agents; augmentcode.com multi-agent workspace; codepick.dev agents roadmap; mightybot.ai rankings; awesome-ai-agents-2026 list (source of GNAP lead); visualstudiomagazine.com Agents tab |
| 4 | Lovable export code GitHub two-way sync own code exit hosting migration | docs.lovable.dev/integrations/github (primary docs); vibefactory.ai; axonbuild.com/blog/lovable-export-code; encited.com; miget.com/blog/how-to-host-lovable-app; oboe.com guide |
| 5 (verification) | "GNAP" "Git-Native Agent Protocol" | github.com/farol-team/gnap (primary repo, VERIFIED); github.com/mrdummy550/gnap (secondary copy); awesome_ai_agents issue 99; microsoft/agent-framework issue 4715; microsoft/autogen issue 7398; openai/swarm issue 70; OpenHands issue 13416; microsoft/promptflow issue 4093 |

## Retrieval notes

- DanubeData results excluded from recommendations (vendor blog ranking itself first).
- GNAP initially surfaced only via an awesome-list mention (fabrication-risk class); verified against its primary repository and four independent ecosystem issue proposals before citing. Ecosystem issues are adoption *proposals*, not adoptions ; stated as such.
- Lovable two-way-sync behavior taken from Lovable's own documentation (primary source) and corroborated by three independent guides.
- GitHub Pages public-repo restriction and 100GB soft cap: multiple independent comparison sources agree; primary GitHub docs not fetched this round ; joint-edit-pass flag shared with the other figures.
- No primary-page fetches beyond docs.lovable.dev extracts; flagged for joint edit pass per SOP.

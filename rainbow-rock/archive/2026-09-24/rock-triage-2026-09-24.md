# Rock triage — six repos, Sep 24 (/ceec drop, /ziggy triage)

Method: judged against the descent plan and the four boundary principles (capability granted not assumed; deny-by-default; events-first-class; boring audit). Fossils are welcome; framework-eaters get named as such. NOTHING here is an install recommendation — descent plan step 1 is inventory first, no installs.

| repo | upstream | silo on the map | verdict |
|---|---|---|---|
| ccfos/nightingale | upstream (DiDi/CCF, Apache-2.0) | AUDIT / observability | **KEEPER — strongest rock.** MCP built in, 74 tools (42 read / 32 write), READ-ONLY BY DEFAULT, write is explicit config opt-in, per-token RBAC so a client can never exceed its token owner's permissions. The constitution's principles already ship as somebody's production code. |
| cicipunk3-byte/harness-sdk | fork of strands-agents (AWS, Apache-2.0) | Ground Control / agent loop | **KEEPER, PHASE-GATED.** In-process agent loop, no hosted control plane, hooks intercept/log/redirect every step, Ollama supported (hybrid-friendly). This is the phase-4+ layer — nothing here enters until the bridge is read-only and proven. |
| cicipunk3-byte/n8n | fork of n8n-io (fair-code, Sustainable Use License) | PROCEDURE | **KEEPER WITH A FLAG.** Self-hostable, human-approval steps, audit trails — good procedure plane. Flag 1: fair-code is NOT OSI open source; fine for private Oz, do NOT bundle into Rainbow Rock. Flag 2: n8n's whole instinct is webhooks and outbound calls — it must be boundary-walled or it becomes the biggest attack surface in the lab. |
| cicipunk3-byte/agent-native | fork of BuilderIO (MIT) | INTERFACES / renderer | **KEEPER AS FOSSIL.** The shared-action pattern (agent and UI call the same permission-checked capability layer; the agent never clicks through the UI) is exactly the World Bridge pattern with a different hat on. Heavy React/Postgres stack — reference, not adoption. |
| cicipunk3-byte/codebase-memory-mcp | fork of DeusData | MEMORY | **CAUTIOUS — binary-only or shelve.** 100% local processing, no API keys, single binary — good. But the installer auto-configures ~45 client surfaces and runs a coordination daemon by default. That is the opposite of explicit grant: nothing exists merely because the installer can discover it. If ever used: `--skip-config`, binary only, no daemon. |
| cicipunk3-byte/substrate | fork of agent-substrate (Google-adjacent) | SANDBOX at scale | **SHELVE — anti-locality fossil.** Proves stateful actor suspend/resume and sandbox density at Kubernetes scale. Requires K8s/GKE — a cloud dependency the architecture explicitly rejects. Revisit only if a multi-agent future ever justifies a cluster, which would be a constitution change, not a tooling one. |

## The pattern in the pile

Five of six map cleanly onto silos already on the diagram, and the sixth (substrate) is a scale version of the sandbox silo. The map has real-world referents for almost every layer. What has NO repo and doesn't: the World itself and the Rock. Those two are the parts only we can build.

## Discipline note

All six are installs, and the descent plan's first downstairs operation is inventory, not construction. Triage now, install nothing until the Mini's INVENTORY.md exists.

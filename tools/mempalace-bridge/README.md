# MemPalace Bridge -- verbatim memory layer for the lab loop

**What this is:** the fold-in procedure, privacy guards, and live-run results for
[MemPalace](https://github.com/MemPalace/mempalace) (MIT, 59.3k stars) as the lab loop's
memory layer. Filed and pushed 2026-09-27, PI-ordered.

**One job:** give the resident assistant search-before-answer recall over the lab's
verbatim record. Local embeddings, zero API calls, nothing leaves the machine. This is
independently-built confirmation of the lab's own finding that **verbatim files beat
summaries** for carried context (Loci A/B, Sep 25).

## The stack (as observed live, Python 3.13)

| Layer | Component | Notes |
|---|---|---|
| Storage | ChromaDB 1.5.9 (default) | local, embedded; alternates: sqlite_exact, rust_exact, milvus, qdrant, pgvector |
| Embeddings | ONNX Runtime 1.30 + MiniLM (~80 MB) | downloaded once on first use, then fully offline |
| Retrieval | hybrid: cosine semantic + BM25 lexical | verbatim excerpts returned, never paraphrased |
| Interface | CLI + MCP server (`mempalace-light-mcp`) | MCP = wire into any assistant shell |
| Packaging | pip (`mempalace`), Docker image (multi-arch, `/data` volume) | no API key, ever |

## Live-run receipt (2026-09-27)

- Install: `pip install mempalace` (3.10.0)
- Palace init on the lab root: **24 rooms auto-detected** from repo structure
- Mined `memory/` wiki: **85 files → 667 drawers filed**
- Smoke query: *"why do local models summarize the kernel instead of enacting it"* →
  top hit: the address-frame hypothesis page, correct verbatim passage, hybrid score
  (cosine 0.349 / bm25 2.365). **PASS.**

Full detail: [RESULTS-2026-09-27.md](RESULTS-2026-09-27.md)

## Privacy law (non-negotiable)

The auto-generated room map includes a `source_material` room. **Never mine
`source-material/` into a palace that could sync, share, or leave the machine.**
`source-material/PERSONAL_CONTEXT.md` must never be indexed into any vector store.
The fold-in script enforces a hard refusal; do not bypass it.

## Use

```bash
./mempalace-fold-in.sh /path/to/lab          # install, init, mine safe layers
./mempalace-fold-in.sh /path/to/lab --search "query"   # smoke test
```

See the script header for the full procedure and the known pip friction on
Python 3.13 (three transitive wheels missing from metadata; the script patches them).

## Relation to the loop

ark = the tools' house. ferry = carrying consistency. kernel-arc = the carry.
gate/monitor = governance. **MemPalace = the memory organ.** The portable, self-run
lab loop is: shell + local model + kernel + ark + MemPalace + owned storage + gate.

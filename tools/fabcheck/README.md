# fabcheck; fabrication and AI-text signal checker

Free, local, stdlib-only Python. Part of the ThreadCat lab tooling.

## What it is

The correction ritual we kept running by hand (CCS doc, song lyrics, README
sweeps), turned into a tool. It reads text or a markdown file and produces a
claimed-vs-verified ledger in the house format.

## Honest scope (read this first)

- Heuristics produce **signals, not verdicts**. An em-dash is not a sin; a
  future publication year is.
- Claim **verification** against the live web needs a search API, which costs
  money. That backend is a stub. The local ollama backend can judge
  claim-shaped sentences but it confabulates too, so its output goes in the
  ledger as "model opinion", never as "verified".
- The tool cannot tell you a claim is false. It tells you where a human
  should look first.

## What it checks

1. **Fabricated-source signals**
   - Branded-source pattern: "The Tao of Agency (2026)" style title-plus-year
     citations, our most common fabrication class (5/5 in the CCS doc).
   - Publication years in the future or implausibly old.
   - Bracketed placeholder sources like "[Open Secure AI Alliance]".
   - DOI / arXiv ID format checks (format only; resolution is a network job).
2. **AI-text signals**
   - Em-dash density (house rule aside, it is a real market signal).
   - Filler/sycophancy lexicon: "delve", "tapestry", "Great question",
     "it's important to note", etc.
   - Sentence-length uniformity (low variance correlates with generated text).
3. **Claim extraction**
   - Sentences containing citations, numbers, URLs, or named sources, ranked
     for human review order.

## Usage

```
python3 -m fabcheck.cli path/to/doc.md            # full ledger
python3 -m fabcheck.cli --sources-only doc.md     # citation signals only
python3 -m fabcheck.cli --ollama doc.md           # + local model opinion (ollama running)
python3 -m fabcheck.cli --stdin < notes.txt
```

Output: markdown ledger with CLAIMED / SIGNAL / VERIFIED / QUARANTINE
sections, same shape as the CCS cleanup ledger in tools/rainbow9cat/.

## Layout

- `signals/sources.py` - citation-shaped fabrication signals
- `signals/aitext.py` - style and lexicon signals
- `claims.py` - claim extraction and ranking
- `backends/ollama_backend.py` - optional local model opinion
- `ledger.py` - report writer
- `cli.py` - entry point
- `tests/` - fixtures built from real fabrications this lab caught

## Constraints

- Zero dependencies. Python 3.9+. No network by default.
- Runs on 8GB hardware (gemma3:4b via ollama is the reference backend).
- Tested small until it can't. Then it gets moved.

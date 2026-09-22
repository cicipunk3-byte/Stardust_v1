# Wary of AI? Start here.

A guide for people who do not trust AI tools, do not want an account
with one, and still want to see what the fuss is about. No coding or
terminal experience needed for the short version; the full walkthrough
it points to assumes nothing either.

Written by the ThreadCat builders: a human-led research lab that runs
on local AI, keeps every receipt in public, and shares the wariness.
We caught a popular AI service fabricating sources, citations, test
results, and a friendly goodbye over two days of ordinary use. Your
instincts are not paranoia. They are a research method. This guide is
about using AI on your terms anyway.

## Why "local" answers most of the worries

A local AI model is a program you download and run on your own
computer. Nothing you type leaves the machine. No account, no phone
number, no meter running, no company reading along.

- **Privacy:** your questions stay on your hardware. No cloud, no
  history held by someone else.
- **Control:** the model is a file. Delete it and it is gone. Nothing
  phones home.
- **Cost:** the software is free and open source (Ollama), the models
  we recommend are free downloads, and your computer's own power does
  the work.

The honest trade: a local model on a home computer is smaller and less
capable than the big cloud services. For learning, drafting, asking
questions, and experimenting, it is genuinely useful. For heavy
professional workloads, it is not the same thing yet. We think the
trade is worth it, and we would rather tell you that up front.

## The green note, with real numbers

If part of your wariness is environmental, keep it: it is grounded.
Data centres consumed about 415 terawatt-hours of electricity in 2024,
around 1.5% of world electricity use, and the International Energy
Agency projects that more than doubling to around 945 TWh by 2030 in
its base case, driven substantially by AI ([IEA, Energy and AI, April
2025](https://www.iea.org/reports/energy-and-ai/executive-summary)).
Research on inference costs shows the per-request energy of large
deployed models is substantial and is where most AI compute happens
([Luccioni, Jernite and Strubell, FAccT 2024](https://arxiv.org/abs/2311.16863)).

Running a small model locally is among the lighter ways to use AI: the
model we recommend fits in 3.3 gigabytes and runs on a laptop you
already own, drawing power your machine already draws. Local does not
fix the industry's footprint. It removes you from it while the
industry figures itself out, and it makes your own use legible: you
can see the model, its size, and its cost.

## The setup, short version

1. Install Ollama (free, open source): ollama.com. One installer.
2. Download a small model: `ollama run gemma3:4b` (3.3 GB; a good
   starter: capable, small, from Google's open-weight family).
3. Talk to it. That is the whole test. Everything stays on your
   machine.

The long version, with screenshots-level detail and what to expect on
an 8 GB laptop: see the local model guide on our site
(threadcat.org/local-model) and the same guide's source in this
repository.

## Testing, not training

Most people do not need to train an AI; they need to test one, and
testing is where you keep the power. A few things worth trying once
your local model runs:

- **Ask it about itself and check the answers.** Local models
  confabulate: they state things that are not true, fluently. Watch
  for it. This is the single most useful habit AI-wary people already
  have.
- **Give it a persistent character file.** Our own experiment is
  exactly this: a plain markdown "kernel" that a fresh model instance
  reads at the start of every session, carrying its instructions and
  history. You can read every variant in `portable-context/` and run
  the same tests yourself with the harness in `harness/`.
- **Keep your own receipts.** Save transcripts. When the model gets
  something wrong, you will have the record. That habit is the entire
  method of this lab.

About training: running and testing models at home is easy and free.
Training (fine-tuning) a model is a bigger project, needs more
hardware, and is honestly unnecessary for most purposes. Start by
testing. If you ever get to training, it will be because testing
showed you exactly what you wanted to change.

## Stay wary anyway

A local model is private but not correct. It will still invent
citations, forget things, and tell you what you want to hear. The
difference is that now you can check everything on your own machine,
with no company in the middle, and keep the receipts in a place no
platform can lose. Wariness, plus receipts, is not opposition to AI.
It is how you make it work for you.

## Where this all comes from

Everything above is practiced, not preached: our repository holds the
session records, the fabrication case study, the tools we built to
check AI work (see `tools/fabcheck`), and the cost ledger for the
whole project. If a claim in this guide ever drifts from the record,
the record wins.

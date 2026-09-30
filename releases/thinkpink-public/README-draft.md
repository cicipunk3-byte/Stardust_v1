# SeeingPink README draft v1 (Ziggy, Sep 28, for Cecil /c)

Draft for the SeeingPink repo README. Ruled elements preserved: founder
voice, market-gate sentence, support = GitHub issues, license split,
unseal fallback, provenance. The telemetry sentence is worded to dodge
the pending probe honestly ("no claims without receipts") and can be
upgraded to a hard "no telemetry" line after tomorrow's test. Image:
drop the dark flyer PNG at assets/thinkpink-flyer-dark.png in the repo
(or edit the path). No em-dashes.

---

<div align="center">

<img src="assets/thinkpink-flyer-dark.png" alt="ThinkPink: the governed assistant. Your machine, your record, your rules." width="720">

# ThinkPink

**The governed assistant. Your machine, your record, your rules.**

*Governed by design, not by promise.*

[Download v0.1.0](https://github.com/cicipunk3-byte/SeeingPink/releases/download/v0.1.0/ThinkPink-0.1.0-mac-arm64.zip) · [Release notes](https://github.com/cicipunk3-byte/SeeingPink/releases/tag/v0.1.0) · [Setup guide](STARTUP-PLAIN.md)

**v0.1.0 beta** · macOS, Apple Silicon · 127 MB · free

</div>

---

## What this is

ThinkPink is a desktop assistant that runs on your own computer with
[Ollama](https://ollama.com) and a local model. No account, no server,
no subscription. What makes it different is what it ships with: a
resident assistant carried on a portable kernel you can read, a gate
that files a receipt before consequential actions, and a design that
assumes you deserve to see the record.

Most local AI apps give you a model runner. This one arrives as
someone, and answers to you.

**WHAT, ME SELL YOUR DATA?**

## Quick start

1. Install [Ollama](https://ollama.com) (the engine that runs models on your machine).
2. In a terminal: `ollama pull gemma3:4b`
3. [Download ThinkPink](https://github.com/cicipunk3-byte/SeeingPink/releases/download/v0.1.0/ThinkPink-0.1.0-mac-arm64.zip) and unzip it.
4. Open it. If macOS asks on first launch, right-click the app and choose **Open**.
5. Talk to it. It finds Ollama on its own. When the pill is green, your model is local and connected.

Your conversations stay on this machine. Memory lives in readable files
you own, in a folder you can open, back up, or carry somewhere else.

## What "governed" actually means

ThinkPink's design law, enforced in the software, not the marketing:

- **Local by default.** The model runs on your hardware. A local-only
  configuration is a first-class setup, not a downgrade.
- **One cloud lane, watched.** If you connect a cloud model at all,
  there can be only one, and it runs behind a monitor that records both
  sides of every call: hashes, events, and a plain-English log. If the
  upstream fails, the failure is observed, never silent.
- **The kill switch is yours.** Only the account holder can hold it.
  Not us, not "the lab." Verbatim, in the code.
- **Receipts, not promises.** Gate decisions are proposed, ruled,
  effectuated, and checked, and the record is a file you can read.
- **Free.** Free for everyone. Nobody sells this packaging.

## Build it yourself

The release zip is built from this repository's own source, and you can
do the same on your own machine:

```bash
git clone https://github.com/cicipunk3-byte/SeeingPink.git
cd SeeingPink
pnpm install
pnpm --filter ./artifacts/thinkpink run desktop:package:mac
```

Requires Node 22+ and pnpm 10. The packaged app lands in
`artifacts/thinkpink/release/<version>/`.

## Honest limits

This is a beta running small local models. It will be slower and less
capable than a cloud giant, on purpose. It has no voice, no mobile app,
and no proactive reach-outs yet. It is ad-hoc signed, not notarized,
which is why macOS may ask on first launch. We make no claims we cannot
hand you a receipt for.

ThinkPink is a research artifact from [the Stardust Lab](https://threadcat.org):
released to be read, checked, and built on. Nothing here is offered as
market-ready until it has been thoroughly tested in the cloud and with
scientific partners. Expect retooling as we learn.

## License

Packaging: [CC BY-NC-SA 4.0](LICENSE). Nobody gets to sell this exact
packaging. Components under their own licenses, notably MIT, are named
in [NOTICE-THIRDPARTY.md](NOTICE-THIRDPARTY.md).

## Support

Support runs through [GitHub issues on this repository](https://github.com/cicipunk3-byte/SeeingPink/issues).
A human is available.

# How to download a local model

A guide for people who have never done this. No coding or terminal experience assumed beyond what is on the [tools page](https://threadcat.org/tools): if you can send a text message, you can do this. Written by the ThreadCat project; every claim links to a receipt in the Sources section at the bottom.

## Why a local model

Three reasons, in the order we care about them:

1. **Privacy.** A local model runs on your computer. Nothing you type leaves the machine. No account, no upload, no terms of service, no record kept by anyone but you.
2. **Cost.** The model files are free. There is no subscription. After the download, chatting costs only the electricity your laptop already uses.
3. **Your files stay yours.** Our tools are built so your history and notes live in plain files you own. A local model fits that: the "brain" is a file on your disk, not a service someone else can change or shut off.

## What you need

- A computer (Mac, Windows, or Linux) with about 8 GB of memory. That is the low end of ordinary; most laptops from the last five years have it.
- About 3-4 GB of free disk space for the model file. Models come in sizes; bigger is smarter but heavier. We run a 4 GB-class model on an 8 GB laptop and it works.

## Step by step

1. **Download Ollama** from [ollama.com](https://ollama.com). It is free and it is the installer that handles everything else. Click the download button for your operating system and install it like any app.
2. **Open a terminal.** On a Mac: Applications, then Utilities, then Terminal. On Windows: click Start, type "terminal", press enter.
3. **Type one line and press enter:**

   ```
   ollama run gemma3:4b
   ```

   That downloads the model (a few GB; get a coffee) and then starts a conversation. The next time you run the same line, there is no download; it just opens.
4. **Talk to it.** Type a message, press enter. When you are done, type `/bye`.
5. **Optional, the ThreadCat part:** run our [observer harness](https://github.com/cicipunk3-byte/Stardust_v1/tree/main/harness) against that model and watch what it claims about itself over time. The [cheatsheet](https://github.com/cicipunk3-byte/Stardust_v1/blob/main/harness/CHEATSHEET.md) explains every word.

Other models that fit a small laptop: `llama3.2:3b`, `qwen3:4b`, `phi3:mini`. Swap the name in the command. All free, all from inside Ollama.

## What a local model cannot do

Be honest about this, the same standard we apply everywhere: a 4 GB model is noticeably less capable than the big cloud assistants. It forgets things, it reasons less sharply, and it will still occasionally invent sources (our fabcheck tool exists partly because of that). It is the right tool for privacy, for experiments like ours, and for everyday chat; it is not the right tool for heavy research work.

## The environmental receipts

We did not want to write "local models are greener" and leave it at that, because the honest picture has parts that cut both ways. Here is what the published research actually shows.

**Cloud AI has real energy and water costs, and inference (the part you use) is a growing share.** The studies below are about data centers: buildings full of computers that must be powered and cooled around the clock, wherever you are and whatever time you click.

- **Water.** Training the GPT-3 model in Microsoft's U.S. data centers directly evaporated an estimated **700,000 liters of clean freshwater**; global AI demand is projected to drive **4.2 to 6.6 billion cubic meters of water withdrawal in 2027**, more than the annual water withdrawal of 4 to 6 Denmarks. Source: Li, Yang, Islam, and Ren, *Making AI Less "Thirsty": Uncovering and Addressing the Secret Water Footprint of AI Models*, Communications of the ACM ([arXiv 2304.03271](https://arxiv.org/abs/2304.03271)).
- **Energy and carbon.** Multi-purpose generative models are **orders of magnitude more expensive in energy and emissions per 1,000 inferences** than small single-task models, even when the models have the same parameter count. Generality is paid for on every request. Source: Luccioni, Jernite, and Strubell, *Power Hungry Processing: Watts Driving the Cost of AI Deployment?*, ACM FAccT 2024 ([arXiv 2311.16863](https://arxiv.org/abs/2311.16863)).
- **The pattern was named in 2019.** Strubell, Ganesh, and McCallum quantified the energy and carbon cost of training large NLP models and made the equity argument that changed the field's behavior: compute is a resource, and who gets to use it matters ([arXiv 1906.02243](https://arxiv.org/abs/1906.02243), ACL 2019).
- **Where this goes.** MIT researchers expect the electricity demands of **inference**, not training, to dominate AI's energy use as generative models become ubiquitous ([MIT News, January 2025](https://news.mit.edu/2025/explained-generative-ai-environmental-impact-0117)).

**What this means for a laptop, stated carefully:**

- A small local model answering your questions draws roughly laptop-charger levels of power, produces no cooling-water demand, and adds nothing to a data center's footprint. Your conversation runs on hardware that is already built, already plugged in, and already yours.
- We are **not** claiming a laptop beats a hyperscale data center per token; a big GPU can be more energy-efficient per calculation than a laptop chip. The honest local-first claims are smaller and sturdier: small models are dramatically cheaper to run than frontier-scale ones (Luccioni et al., above), the per-conversation water cost is zero, the energy is visible and on your own meter, and the hardware is not built and cooled in your name for a service you can leave.

## Sources

- Li, Yang, Islam, Ren (2023, rev. 2025), *Making AI Less "Thirsty"*, Communications of the ACM. [arXiv 2304.03271](https://arxiv.org/abs/2304.03271)
- Luccioni, Jernite, Strubell (2024), *Power Hungry Processing*, ACM FAccT 2024. [arXiv 2311.16863](https://arxiv.org/abs/2311.16863)
- Strubell, Ganesh, McCallum (2019), *Energy and Policy Considerations for Deep Learning in NLP*, ACL 2019. [arXiv 1906.02243](https://arxiv.org/abs/1906.02243)
- MIT News (2025), *Explained: Generative AI's environmental impact*. [news.mit.edu](https://news.mit.edu/2025/explained-generative-ai-environmental-impact-0117)
- Ollama, the installer used in this guide. [ollama.com](https://ollama.com)

*Check us the way we ask you to check everything: click the links. If a number on this page does not match its receipt, tell us; that is the project working.*

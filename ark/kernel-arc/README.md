# kernel-arc -- the layer of the ark that carries the agent

The ark carries tools and contracts for the RECORD. This folder adds the
other half: support for archives that carry a KERNELIZED AGENT CONTEXT --
a kernel, its version archive, and the boot instructions that make a fresh
instance oriented instead of blank.

**This folder is mostly instructions on purpose.** The one piece of code it
touches is a `--kernel` mode on the ark's own plug verb (see
KERNEL-CONTRACT.md for what it checks). The rest is the lab's actual kernel
practice, written down for someone who has never seen it: what a kernel
is, how to boot one, how to verify an instance enacted rather than
paraphrased it, and the honest limits of every check involved.

## Read in this order

1. **KERNEL-CONTRACT.md** -- the slots (required: `kernel.md`, `archive/`,
   `BOOT.md`; optional: principles log, run logs, delegation handoffs), each
   with a receipt from lab practice, plus the discipline list a kernel must
   carry to be a kernel and not a costume.
2. **BOOT-INSTRUCTIONS.md** -- the five-minute initiation: one path for the
   human carrying the archive, one for the instance receiving it, and the
   three verification probes.

## One-line version

The ark's main contract carries what HAPPENED (timeline, transcripts,
briefs). The kernel contract carries WHO IS SHOWING UP (the kernel, its
versions, its discipline). A complete movable lab carries both, and the
archive -- always -- belongs to the person, on hardware they own.

# Brief 007: site tools page draft, "Check Your AI's Homework"

**Status: PROPOSAL, behind Cat's gate. Draft page for threadcat.org. Nothing
is sent to the site agent until Cat approves.** Requested by Cecil, Sep 21
2026 ~4:40 PM ET: a page laying out the tools "for the person who's never
opened a terminal in their computer before, more likely to depend on AI and
believe fabrications."

Site rules honored in the draft below: no personal names, no em-dashes,
every number traceable to the repo.

---

## PAGE DRAFT (everything between the rules is copy)

### Title

**Check Your AI's Homework**

### Blurb

AI assistants sometimes invent sources: papers that do not exist, quotes
nobody wrote, studies with the wrong year. This is common, it is not a
glitch that will be patched, and it is not your fault for believing it. We
run a research project that studies exactly this, and our checking process
caught invented sources in our own materials twice in one day. Here they
are, free,
private, and built to run on an ordinary laptop. You do not need to be
technical to use them.

### Section 1: What fabrication looks like

The most common fake we catch has a shape you can learn in one minute: a
confident title, a plausible year, and no way to find it. "The Tao of
Agency (2026)" was one of five invented sources an AI research document
gave us in a single day. It sounded real. It had the exact shape of a real
citation. It did not exist. AIs do this because they are built to produce
fluent text, not to check facts, and fluency does not care whether the
paper exists.

### Section 2: What our tools do

**fabcheck** reads a document and flags things worth checking: citations
shaped like the fakes above, publication years that have not happened yet,
placeholder organizations in brackets, and the writing-style signals that a
document came out of a machine. It hands you a list, ranked by what deserves
your attention first.

**export-ingest** takes the conversation archives the big AI companies let
you download and turns them into plain, readable files on your own computer.
Your history stops living only inside someone's service.

**The CCS field manual** is not a program, it is a game you can read and
play with any AI, no terminal needed. It borrows the dice mechanics of
tabletop roleplaying games (roll a twenty-sided die against a difficulty
score) to turn the receipt habit into a practice: checking a source before
repeating it becomes a move you make, not a lecture you sit through. It
comes with nine character sheets, the "nine glass-vessel cats," each built
around a different AI failure mode we actually met and caught in our own
record. Read it in the project repository under
tools/rainbow9cat/ccs-field-manual.md.

### Section 3: What they cannot do

They cannot tell you a claim is true. They are a triage nurse, not a doctor:
they point at what to check, a human still checks it. Anything our tools
flag stays out of our own public pages until a person looks at the receipt.
That rule caught five fake sources in one document, four fake song quotes
in another, and it will catch yours too.

### Section 4: How to run one (your first terminal command, gently)

The terminal is just an app on your computer where you type words instead of
clicking. If you can send a text message, you can do this. The steps:

1. Install Python from python.org (free, the button is obvious).
2. Download our two tool folders from the project repository.
3. Open the terminal (on a Mac: Applications, then Utilities, then Terminal).
4. Type one line and press enter:

```
python3 -m fabcheck.cli mydocument.md
```

That is the whole trick. Everything runs on your computer. No account, no
upload, no cost, nothing leaves your machine.

### Section 5: The habit

Before you repeat a claim an AI gave you, ask one question: where is the
receipt? If the answer is a link, click it. If the answer is a citation,
look it up. If the answer is nothing, treat the claim as a rumor. Our
standing rule, learned expensively: scraped or generated research is an
input to a verification loop, never a substitute for it.

### Citations

- Wei et al. 2023, "Simple synthetic data reduces sycophancy in large
  language models," arXiv 2308.03958. The technical basis for the idea that
  fabrication and flattery are trainable-down behaviors.
- ThreadCat WHITEPAPER v1.0, in the public repository. Project method and
  the 675-screenshot, 68-batch study record.
- The project's case study logs, in the repository: the fabricated-source
  and fabricated-quote catches described on this page, with the quarantines.
- The CCS field manual and its nine character sheets, in the repository
  (tools/rainbow9cat/). Built from real catches in the project record;
  its Part 0 grounding table maps every game mechanic to a source.
- DOI 10.5281/zenodo.22870569 (project record, Zenodo).

---

## Implementation notes for the site agent (not site copy)

- Keep section 4's command block visually quiet; one command, no flags.
- The Python download link is python.org; link it, do not deep-link
  installers (versions move).
- Repository link should point at the public Stardust_v1 repo when Cat
  approves the push.
- If the tools move to their own repo later, update links in one place: the
  citations block.

# The Watchers

**One job: stand between a claim and a person about to believe it.**

The Watchers read documents so you do not have to trust them. One
reads citations and flags the ones shaped like fakes, one queues
claim-shaped sentences for human eyes, one hunts numbers wearing
yesterday's date, one smells forged exports. Different signals, one
spine, and it is the spine that makes them a family: **the flag is
the product, the verdict is not theirs.** A Watcher that ever outputs
"true" has left the family.

| Tool | One line |
| --- | --- |
| [fabcheck](../../tools/fabcheck/) | reads a document, produces a claimed-vs-verified ledger |
| [nextcheck](../../tools/nextcheck/) | extracts claim-shaped sentences into a NEEDS-HUMAN queue, run-the-artifact step mandatory |
| [staleness](../../tools/staleness/) | number-consistency against a canonical reference, currency check included |
| [loopwatch](../../tools/loopwatch/) | scans a transcript for repeated reasoning loops and prints the flagged ranges |
| [exportcoroner](../../tools/exportcoroner/) | scans provider exports for the lab's known forgery classes |

Status of every tool: [tools/TOOL-STATUS.md](../../tools/TOOL-STATUS.md).

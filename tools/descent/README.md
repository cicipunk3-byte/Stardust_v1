# descent (read-only machine inventory), module descent

**Status:** Experimental. Sandbox-phase tool; first Mini run pending, output owed back to the lab record.

Read-only machine inventory: hardware, OS, storage, memory, network, runtimes,
services, ports, and known world substrates. No installs, no writes outside the
chosen output directory, no network. It reports what IS, not what to install.

Part of the ATC Local Descent Plan v0.1 (step 1).

## Usage

    python3 inventory.py --out ./descent-inventory

## What it is not

It does not judge, recommend, or change anything. Like every tool in this
library: it flags and reports, a human reads the receipt.

Canonical standing: see TOOL-STATUS.md.

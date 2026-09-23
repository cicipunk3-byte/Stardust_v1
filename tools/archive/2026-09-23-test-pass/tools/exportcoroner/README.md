# exportcoroner; export forgery detector (Grey Cat)

Part of the ThreadCat lab tooling. Free, local, stdlib-only Python.

## Status: SCAFFOLD, PENDING TESTING

Scans provider exports for the lab's known quarantine classes: branded
title-plus-year citations with future years, bracketed placeholder
sources, and broken link-encoding rot (the CCS export class). Positive
controls are the real quarantined fabrications. Regression against the
full CCS export and a clean-control pass are owed before first use.

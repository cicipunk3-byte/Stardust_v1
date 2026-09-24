# Grey Cat (export forgery detector) · module exportcoroner

Part of the ThreadCat lab tooling. Free, local, stdlib-only Python.

## Status: PENDING PI ADOPTION; fixture tests pass

Fixture tests pass (4/4) including the hand-cleaned CCS manual regression (zero flags) and real-fabrication positive controls.

Scans provider exports for the lab's known quarantine classes: branded
title-plus-year citations with future years, bracketed placeholder
sources, and broken link-encoding rot (the CCS export class). Positive
controls are the real quarantined fabrications. Regression against the
full CCS export and a clean-control pass are owed before first use.

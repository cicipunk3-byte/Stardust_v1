# RUN: offline network probe — ThinkPink 0.1.0 release artifact

Date: 2026-09-29, ~8:05-10:20 AM ET. Run by Cecil on the MacBook Neo, guided command-by-command by Ziggy in-thread.

## Artifact under test

- ThinkPink-0.1.0-mac-arm64.zip, downloaded from the public GitHub release page (user path, Safari).
- SHA-256 verified on-machine before the session: e900ad59ace66205ff3c8b877af6a603e41af222765fd05ab37d0b156ed89ba8 (matches the published release notes).
- The zip was hash-verified AFTER Safari auto-unpacked it and moved the archive to Trash (see finding 2), so the tested bytes are provenance-locked to the release.

## Procedure

1. Static sweep: all http(s) URLs in the .app bundle extracted (`grep -raoE` over Contents). 2,197 unique URLs, consistent with Electron/Chromium framework noise. Not a verdict by itself; recorded as the "every door the app knows about" list.
2. Connection sampler: `lsof -nP -i` on all ThinkPink PIDs (main + helpers via `pgrep -i -f ThinkPink`), every 30 seconds, appended to probe-lsof.log with timestamps.
3. Session, in order: cold launch (after documented xattr -cr + ad-hoc codesign unseal), 5 minutes untouched, one local gemma3:4b chat with reply, every settings screen and toggle opened once, extended idle (more than 5 minutes), normal quit.
4. Verdict command: `grep -E "TCP|UDP" probe-lsof.log | grep -vE "127\.0\.0\.1|::1" | sort -u` over the full session log.

## Result

**EMPTY. Zero non-loopback connections observed at any sample point across the entire session.** The only network activity seen from the app's processes was loopback (127.0.0.1 / ::1), consistent with the local Ollama lane.

## Findings

1. **Probe PASS.** The runtime observation supports the "No telemetry" claim in the release notes. The claim went live one step ahead of its receipt (noted in-thread, Cecil: "thought it was held. my bad for not noticing"); this receipt closes that gap the same day.
2. **Safari download behavior (not a defect):** Safari's open-safe-files default auto-unpacks the app and moves the zip to Trash on BOTH the GitHub release page and the site download button (reproduced twice each). App opens fine after download. README note ruled by Cecil; wording scoped to Safari (Chrome/Firefox keep the zip).
3. **Hash disambiguation catch:** a same-filename zip already in Downloads hashed 62cac5a7… (the private handoff-side crash-fix+hook build, Sep 28 chain), NOT the release artifact. Two distinct builds under one filename, again. The probe ran only on the hash-verified release download.

## Honest scope (what this receipt does and does not say)

- The sampler observed open connections at 30-second intervals; a connection lasting less than one interval that started and closed between samples could evade it. No such connection was observed; none is claimed to be impossible.
- DNS queries were not captured this run (the tcpdump cross-check was skipped). The static URL sweep is the corroboration layer.
- One session, one machine (Neo, arm64), one model (gemma3:4b local). The x64 build was not probed.
- System-level macOS services are out of scope by design; only ThinkPink PIDs were observed.

## Disposition

Release-notes claim "No telemetry. No account. No server." is receipt-backed as of this run. PinkEyes-mode copy claims remain gated on their own receipts per the standing "receipts or silence" rule.

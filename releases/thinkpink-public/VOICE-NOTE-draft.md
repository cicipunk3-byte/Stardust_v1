# VOICE-NOTE-draft.md: native dictation note for the SeeingPink README

**Status: DRAFT for Cecil's edit onto the SeeingPink repo.** Scoped
wording matches the release page's four stated specs (no new phrasing,
no em-dashes, no claims we cannot hand a receipt for). The on-device
claim is PENDING VERIFICATION and must not ship until the Neo
airplane-mode test passes.

## The note (drop-in for README.md, wherever the Safari note lands)

### Talking to ThinkPink

You can talk to ThinkPink with the dictation your Mac already has.
Press the dictation key (or double-press it, depending on your
settings) in any text field and speak. No account, no setup, nothing
for us to build.

If your macOS language supports on-device dictation, transcription
happens on your machine. To check yours: System Settings, then
Keyboard, then Dictation. ThinkPink receives only the text.

For a fully offline guarantee, test it yourself: turn on airplane
mode (or Wi-Fi off) and dictate. If it still works, it is on-device
on your machine. We prefer receipts to promises, so we are not going
to claim more than your own test shows you.

---

## Placement + phrasing notes (Ziggy, for Cecil's edit)

1. The last paragraph is the honest-scope move: instead of claiming
   "on-device" as a spec (which depends on the user's macOS version
   and language), the note hands the user a one-minute test. Receipt
   discipline applied to Apple.
2. If the Neo airplane-mode test PASSES on your machine, the wording
   can strengthen to "dictation can run fully on your machine; test
   it with airplane mode." It should NOT strengthen to an absolute
   ("always on-device"), because it varies by language and macOS
   version. Scope, like the probe receipt.
3. If the test FAILS (dictation needs the network on your build), the
   note needs a warning line instead: dictation may use Apple's
   servers, so treat it as an Online-lane action, not a local one.
   That wording would also belong in the release page specs as a
   known limit.
4. No emojis, no em-dashes, matches the "Requires Ollama plus a local
   model" register.

## Verification checklist (the Neo, one minute)

- [ ] Turn Wi-Fi/airplane ON (radio off), open any text field
- [ ] Dictate a sentence
- [ ] PASS = text appears with radio off: on-device confirmed on that
      machine; note ships as drafted
- [ ] FAIL = dictation unavailable or silent: use the warning-line
      wording (note 3) instead
- [ ] Record the result in the lab repo (benchmarks or notes) before
      the README note lands

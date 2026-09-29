# FINDINGS — ThinkPink voice scan (Sep 29, 2026)

Deliverable for Cecil (/c). All sources + caveats in RAW-CAPTURE.md
(same folder). House rule: local-first, no em-dashes, claims carry
receipts.

## The headline

The voice feature splits into INPUT and OUTPUT, and each side has a
device-native path (zero code, works today) and an embedded-local path
(the real feature). Both paths can be fully offline. The trap to avoid
is specific and confirmed: the Web Speech API inside Electron/Chrome
sends the user's audio to Google or Microsoft servers. That is a cloud
lane wearing a built-in costume, and it would break the local-first law
and the probe-backed "No telemetry" claim in one move. Any in-app mic
button we build reads audio LOCALLY or does not exist.

## INPUT (speech to text)

1. **Pathway N (native, zero code): macOS system dictation.** Works in
   any app's text fields, so it works in ThinkPink today with zero
   engineering. This is the Mac analog of what Cecil already does on
   iPhone. CAVEAT: whether dictation processing is fully on-device on
   his macOS version is UNVERIFIED until the Neo airplane-mode test.
   If it is on-device: this is the free instant win and gets a README
   note like the Safari one. If it is not: it becomes an Online-mode
   lane and we say so honestly.
2. **Pathway E (embedded, the real feature): local whisper.cpp or
   Parakeet.**
   - whisper.cpp (MIT): the Apple Silicon winner, Metal/Core ML/ANE,
     large-v3 ~10x real-time on M5 Pro; a small model is instant for
     push-to-talk. ggml-org/whisper.cpp.
   - Parakeet TDT 0.6B v3 (CC-BY-4.0): 600M params, 25 languages, tops
     the Open ASR Leaderboard class, runs via NeMo-Speech.cpp (GGUF) or
     onnx-asr. Faster and smaller than Whisper at similar accuracy per
     community benchmarks.
   - Recommendation: Parakeet v3 as primary (license clean, size right,
     speed exceptional), whisper.cpp small as fallback. Both fully
     offline. Model download ~600MB-1.2GB, one-time, like the Ollama
     model users already pull.

## OUTPUT (text to speech)

1. **Pathway N (native): macOS Spoken Content / AVSpeechSynthesizer.**
   Zero deps, system voices, quality is Apple-grade decent but not
   warm. Fine for "read my record back."
2. **Pathway E (embedded): Kokoro-82M (Apache 2.0, ~350MB).** Best
   local TTS quality per third-party tests (MOS 4.2, TTS Arena #1 in
   Jan 2026), runs on CPU, Metal via mlx-audio on Apple Silicon.
   Fixed voices, no cloning, and honestly that fits ThinkPink: the
   assistant having one fixed voice is a feature, not a limitation.
3. **Excluded on license:** XTTS v2 (CPML, non-commercial), F5-TTS
   weights (CC-BY-NC). Piper: original MIT archived Oct 2025, live
   fork is GPL-3.0; skip it, Kokoro beats it on sound anyway.

## Governance fit (the parts that make it ThinkPink's, not just any app's)

- **Audio follows the Unroll law.** If we ever record audio, the
  recording is the record and the TRANSCRIPT SIDECAR is what the agent
  consumes. Original audio untouched, SHA-256 sidecar, cached by
  content hash. No new law needed; unroll.py's pattern extends.
- **Mic access is a declared capability.** Module declares it, the
  mode layer arms/disarms it. Private mode: dictation is local by
  construction. PinkEyes mode changes nothing for voice because voice
  never needs the cloud lane at all.
- **Licensing stack:** whisper.cpp (MIT) + Parakeet (CC-BY-4.0) +
  Kokoro (Apache 2.0) all sit cleanly under the CC BY-NC-SA packaging.

## Proposal for the build (Cecil rules)

1. **Chunk V1 (free instant win):** README note + docs: "use macOS
   system dictation (press fn twice) to talk to ThinkPink; works
   today, nothing leaves the machine" (PENDING the Neo airplane-mode
   verification). Zero code.
2. **Chunk V2 (push-to-talk, embedded):** mic button in-app, Parakeet
   v3 via onnx-asr or NeMo-Speech.cpp, transcript sidecar per Unroll
   law, audio kept as provenance.
3. **Chunk V3 (optional voice out):** Kokoro-82M read-aloud toggle.
   Ship last or skip; voice OUT is the least load-bearing piece.

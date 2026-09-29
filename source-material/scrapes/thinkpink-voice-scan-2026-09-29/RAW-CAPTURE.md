# RAW-CAPTURE — ThinkPink voice scan (Sep 29, 2026)

Requestor: Cecil (/c). Purpose: "let the final one of this arc be a voice
feature on ThinkPink. research ones that work especially well locally."
Context: he dictates on iPhone via the native voice-to-text and it works
well; the app is Mac-only, so device-native pathways are in scope.
Method: web search, sources checked for license + recency, Sep 29 2026.
No personal names. Base-verification close-out: no outreach candidates;
n/a.

## Sources captured

1. whisper.cpp vs faster-whisper 2026 STT comparison (promptquorum.com,
   updated Jun 15 2026): on Apple Silicon, whisper.cpp with Metal/Core ML
   is the fastest local STT; large-v3 ~10x real-time on M5 Pro;
   faster-whisper has NO Metal backend, CPU-only on Mac (~3x real-time).
   whisper.cpp license: MIT (ggml-org/whisper.cpp).
2. ggml-org/whisper.cpp README (github.com/ggml-org/whisper.cpp): encoder
   can run on the Apple Neural Engine via Core ML (3x+ over CPU) and via
   ANEForge (~2x faster than Core ML encoder tiny-to-medium). VAD
   segmentation built in.
3. Parakeet TDT 0.6B v3 (huggingface.co/nvidia/parakeet-tdt-0.6b-v3):
   600M-param multilingual ASR, 25 European languages, CC-BY-4.0.
   Runs locally via NeMo-Speech.cpp native C++ runtime (q8_0 GGUF) or
   onnx-asr. Community sources note Apple Silicon efficiency: an hour of
   audio in seconds-to-tens-of-seconds; topped the Open ASR Leaderboard
   (v2 English, May 2025; bytefer Medium + NVIDIA NIM model card).
   v2 = English-only, same family.
4. Best local TTS 2026 (localaimaster.com, Jul 20 2026): Kokoro-82M
   (Apache 2.0, 82M params, ~327-350MB, 54 voices / 8 languages incl.
   US+UK English, French, Spanish, Italian, Hindi, PT-BR, Japanese,
   Korean, Mandarin; NO German) = winner for fast lightweight narration,
   runs on CPU. Piper = king of tiny devices but flat/robotic.
5. Piper licensing caveat (same source): original rhasspy/piper (MIT)
   ARCHIVED October 2025; active fork OHF-Voice/piper1-gpl is GPL-3.0.
   Old MIT weights/voices remain usable. Embedding GPL in a CC BY-NC-SA
   packaged app = a real consideration.
6. Kokoro on Mac (promptquorum.com, ~Sep 2026): Kokoro runs through
   Apple's MLX via the community mlx-audio project (Metal GPU); Piper is
   CPU-only by design on every Mac. XTTS v2's MPS support is a known
   broken issue.
7. Kokoro quality (codesota.com + reviewnexa.com): highest MOS (4.2) in
   its comparison set at 82M params; reached #1 on TTS Arena January
   2026 beating XTTS v2 (467M). A Reddit CPU benchmark (Jun 2026) puts
   Kokoro ~2x real-time on CPU (10s clip ~5s to generate) and "closest
   thing to ElevenLabs in the free open source world."
8. XTTS v2 license: CPML, NON-COMMERCIAL. F5-TTS weights CC-BY-NC,
   Fish Speech open variant CC-BY-NC-SA-4.0. Chatterbox MIT, 0.5B,
   cloning-focused. All noted; XTTS/F5 excluded from ThinkPink
   shortlist on license (packaging is CC BY-NC-SA but the engine choice
   should stay maximally free per the free-knowledge principle).
9. Web Speech API trap (MDN + testmuai.com, 2026): in Chrome/Edge (and
   therefore Electron), the Web Speech API routes audio to a SERVER
   (Google/Microsoft) for recognition; it does not work offline. MDN:
   "your audio is sent to a web service for recognition processing."
   The WebAudio on-device explainer confirms the cloud default and
   describes on-device as a new opt-in capability (user-agent
   dependent), NOT the norm.
10. macOS dictation: system-wide dictation works in ANY app's text
    fields (weesperneonflow.ai 2026 guide context: system dictation is
    the OS input path; on Windows the analog needs internet for full
    recognition on most configs). Apple's SFSpeechRecognizer exists
    since macOS 10.15 (Stack Overflow thread); historically some
    processing went to Apple servers; modern macOS supports on-device
    dictation for supported languages (verification on the Neo owed;
    check System Settings > Keyboard > Dictation language files, and
    airplane-mode dictation test). NOT VERIFIED LIVE: treat the
    on-device claim for macOS dictation as pending a Neo test.

## Claims needing receipts before they go in any public copy

- "On-device dictation" for macOS: VERIFY on the Neo (airplane-mode
  dictation test) before any README claim. Do not repeat Apple marketing.
- Kokoro quality figures (MOS 4.2, TTS Arena #1): third-party tested,
  cite as reported results, not our measurements.
- Parakeet speed figures: community benchmarks, cite as reported.

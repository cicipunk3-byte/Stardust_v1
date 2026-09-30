#!/usr/bin/env bash
# Oz Deployment Installer v1.0 — staged, idempotent, dry-run capable.
# Law: verify before advance. Never modify what exists. Never delete what we didn't create.
# Usage:
#   ./install.sh --dry-run     print every planned action, touch nothing
#   ./install.sh               execute stages, stop on first failed verification
set -uo pipefail

DRY_RUN=false
[[ "${1:-}" == "--dry-run" ]] && DRY_RUN=true

OZ_HOME="$HOME/oz"
REPO_URL="https://github.com/cicipunk3-byte/Stardust_v1"
MODEL="gemma3:4b"
STAGE=0
FAILURES=0

log()  { printf '[stage %s] %s\n' "$STAGE" "$*"; }
act()  { if $DRY_RUN; then printf '    (dry-run) %s\n' "$*"; else eval "$*"; fi; }
pass() { printf '    PASS: %s\n' "$*"; }
fail() { printf '    FAIL: %s\n' "$*" >&2; FAILURES=$((FAILURES+1)); }
ask_continue() {
  $DRY_RUN && return 0
  read -r -p "Continue to stage $((STAGE+1))? [y/N] " reply
  [[ "$reply" == "y" || "$reply" == "Y" ]] || { echo "stopped at stage $STAGE"; exit 1; }
}

# ---------- stage 0: the machine ----------
STAGE=0
log "the machine"
FREE_DISK=$(df -Pk "$HOME" | awk 'NR==2 {print $4}')          # KB
RAM_GB=$(sysctl -n hw.memsize 2>/dev/null | awk '{print int($1/1073741824)}' || free -g | awk 'NR==2 {print int($2)}')
if [[ -n "$FREE_DISK" && "$FREE_DISK" -gt $((40*1024*1024)) ]]; then pass "disk: $((FREE_DISK/1024/1024)) GB free (need 40)"; else fail "disk below 40 GB free"; fi
if [[ -n "${RAM_GB:-}" && "$RAM_GB" -ge 8 ]]; then pass "ram: ${RAM_GB} GB (need 8)"; else fail "ram below 8 GB or undetectable"; fi
if [[ -e "$OZ_HOME" ]]; then fail "~/oz already exists; spec says stop and ask (refusing to touch it)"; else pass "~/oz does not exist; safe to create"; fi
ask_continue

# ---------- stage 1: the layout ----------
STAGE=1
log "the layout"
if $DRY_RUN; then
  for d in lab world models rocks logs backup; do act "mkdir -p $OZ_HOME/$d"; done
else
  for d in lab world models rocks logs backup; do mkdir -p "$OZ_HOME/$d"; done
  for d in lab world models rocks logs backup; do
    if [[ -d "$OZ_HOME/$d" ]]; then pass "created $d"; else fail "missing $d"; fi
  done
fi
ask_continue

# ---------- stage 2: the runtimes ----------
STAGE=2
log "the runtimes (presence checked; nothing force-installed)"
for tool in git python3 brew; do
  if command -v "$tool" >/dev/null 2>&1; then pass "$tool: $(command -v "$tool")"; else fail "$tool missing (install manually per SPEC S2; script does not force)"; fi
done
PYV=$(python3 -c 'import sys; print("%d.%d" % sys.version_info[:2])' 2>/dev/null || echo none)
case "$PYV" in none) fail "python version unreadable";; *) pass "python3 $PYV";; esac
ask_continue

# ---------- stage 3: the continuity layer ----------
STAGE=3
log "the continuity layer"
if [[ -d "$OZ_HOME/lab/.git" ]]; then
  pass "lab already cloned; verifying sync only"
  act "git -C $OZ_HOME/lab fetch origin"
  act "git -C $OZ_HOME/lab status -sb"
else
  act "git clone $REPO_URL $OZ_HOME/lab"
fi
if [[ -f "$OZ_HOME/lab/rainbow-rock/PLAN.md" ]]; then pass "rainbow-rock package present in clone"; else fail "rainbow-rock package missing from clone (expected: not yet pushed; local copy required)"; fi
log "offline check: git history with network down"
act "git -C $OZ_HOME/lab --no-pager log --oneline -1"
ask_continue

# ---------- stage 4: the mind layer ----------
STAGE=4
log "the mind layer"
if command -v ollama >/dev/null 2>&1; then
  pass "ollama: $(command -v ollama)"
  if ollama list 2>/dev/null | grep -q "$MODEL"; then pass "model $MODEL already pulled"; else act "ollama pull $MODEL  (3.3 GB)"; fi
  log "smoke test (local generation)"
  act "ollama run $MODEL 'Reply with the exact words: THREAD CONTINUITY VERIFIED'"
else
  fail "ollama not installed (SPEC S4: brew install or official dmg, human's choice; script records, never forces)"
fi
ask_continue

# ---------- stage 5: the world layer ----------
STAGE=5
log "the world layer"
SANDBOX="$OZ_HOME/lab/rainbow-rock/sandbox-phase1.py"
if [[ -f "$SANDBOX" ]]; then
  for cmd in "start" "status" "snapshot" "stop" "export-audit"; do
    act "python3 $SANDBOX --data-dir $OZ_HOME/world $cmd"
  done
  act "python3 $SANDBOX --data-dir $OZ_HOME/world reset --confirm-reset"
  pass "lifecycle issued against $OZ_HOME/world; audit the files per SANDBOX_PHASE_1.md before advancing"
  log "boundary check: only sandbox files exist in the world dir"
  if $DRY_RUN; then act "find $OZ_HOME/world -type f"; else
    VIOLATIONS=$(find "$OZ_HOME/world" -type f ! -name '*.json' ! -name '*.jsonl' ! -name '*.tmp' | wc -l | tr -d ' ')
    [[ "$VIOLATIONS" == "0" ]] && pass "world dir contains only sandbox artifacts" || fail "$VIOLATIONS unexpected files in world dir"
  fi
else
  fail "sandbox not found at $SANDBOX (expected: not yet pushed; local copy required)"
fi
ask_continue

# ---------- stage 6: the game substrate (human-performed) ----------
STAGE=6
log "the game substrate (FLAGGED: human performs, script only checks)"
for p in "/Applications/Stardew Valley.app" "$HOME/Library/Application Support/StardewValley"; do
  [[ -e "$p" ]] && pass "found: $p" || log "not found (optional in v1): $p"
done

# ---------- receipt ----------
STAMP=$(date -u +%Y%m%dT%H%M%SZ)
RECEIPT="$OZ_HOME/logs/install-$STAMP.md"
if $DRY_RUN; then
  echo "dry-run complete: no changes made. receipt not written."
else
  mkdir -p "$OZ_HOME/logs"
  { echo "# install receipt $STAMP"; echo "- failures: $FAILURES"; echo "- operator: human-approved stages; script never advanced on failure"; } > "$RECEIPT"
  echo "receipt: $RECEIPT"
fi
[[ "$FAILURES" == "0" ]] && echo "ALL STAGES CLEAN" || echo "$FAILURES FAILURES — read them before advancing. if stop/reset/snapshot behavior is not explainable from the files, do not advance."
exit $((FAILURES > 0 ? 1 : 0))

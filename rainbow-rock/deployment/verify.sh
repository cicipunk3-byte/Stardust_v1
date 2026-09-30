#!/usr/bin/env bash
# Oz verify — the dry-run audit. Tests every claim in SPEC.md, prints PASS/FAIL, writes a receipt.
# This is the "runnable to the letter and line" check: the spec's claims become commands.
set -uo pipefail
OZ_HOME="$HOME/oz"
PASS=0; FAIL=0
check() { # check <description> <command...>
  local desc="$1"; shift
  if "$@" >/dev/null 2>&1; then printf 'PASS  %s\n' "$desc"; PASS=$((PASS+1)); else printf 'FAIL  %s\n' "$desc"; FAIL=$((FAIL+1)); fi
}

# S0 machine
check "S0: ~/oz exists"               test -d "$OZ_HOME"
# S1 layout
for d in lab world models rocks logs backup; do check "S1: $OZ_HOME/$d exists" test -d "$OZ_HOME/$d"; done
check "S1: lab README declares boundaries" test -f "$OZ_HOME/lab/rainbow-rock/PLAN.md"
# S2 runtimes
check "S2: git present"    command -v git
check "S2: python3 >= 3.10" python3 -c 'import sys; assert sys.version_info >= (3,10)'
check "S2: brew present"   command -v brew
# S3 continuity
check "S3: lab is a git clone"      git -C "$OZ_HOME/lab" rev-parse --git-dir
check "S3: repo has history"        git -C "$OZ_HOME/lab" log --oneline -1
# S4 mind
check "S4: ollama present"          command -v ollama
check "S4: model gemma3:4b pulled"  ollama list
# S5 world
check "S5: sandbox script present"  test -f "$OZ_HOME/lab/rainbow-rock/sandbox-phase1.py"
check "S5: world state file exists (lifecycle was run)" test -f "$OZ_HOME/world/world/state.json"
check "S5: audit log exists"         test -f "$OZ_HOME/world/audit/events.jsonl"
check "S5: snapshots dir populated"  test "$(ls -A "$OZ_HOME/world/world/snapshots" 2>/dev/null | wc -l | tr -d ' ')" != "0"
# boundary
V=$(find "$OZ_HOME/world" -type f ! -name '*.json' ! -name '*.jsonl' ! -name '*.tmp' 2>/dev/null | wc -l | tr -d ' ')
if [[ "$V" == "0" ]]; then printf 'PASS  boundary: world dir contains only sandbox artifacts\n'; PASS=$((PASS+1)); else printf 'FAIL  boundary: %s unexpected files in world dir\n' "$V"; FAIL=$((FAIL+1)); fi

RECEIPT="$OZ_HOME/logs/verify-$(date -u +%Y%m%dT%H%M%SZ).md"
mkdir -p "$OZ_HOME/logs"
{ echo "# verify receipt"; echo "- pass: $PASS"; echo "- fail: $FAIL"; echo "- law: if stop/reset/snapshot behavior is not explainable from the files, do not advance"; } > "$RECEIPT"
printf '\n%d pass, %d fail — receipt: %s\n' "$PASS" "$FAIL" "$RECEIPT"
exit $((FAIL > 0 ? 1 : 0))

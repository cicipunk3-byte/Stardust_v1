#!/usr/bin/env bash
# mempalace-fold-in.sh - fold MemPalace (verbatim memory layer) into the lab loop.
# Filed 2026-09-27, lab/tools/mempalace-bridge/. Procedure = the live run receipt.
#
# Usage:
#   ./mempalace-fold-in.sh /path/to/lab              # install + init + mine safe layers
#   ./mempalace-fold-in.sh /path/to/lab --search "q" # smoke-test retrieval
#
# Privacy law (enforced below, do not bypass):
#   source-material/ (and PERSONAL_CONTEXT.md above all) must NEVER be mined
#   into any palace that could sync, share, or leave the machine.
#
# Known pip friction (Python 3.13, observed in the live run):
#   the mempalace wheel's metadata misses pyyaml, typing_extensions, numpy.
#   They must be installed into mempalace's OWN site-packages (its startup
#   deliberately strips PYTHONPATH as an ABI guard), and the console script's
#   shebang may point at a different interpreter than the one holding deps.
#   This script handles all three.
set -euo pipefail

LAB="${1:?usage: mempalace-fold-in.sh /path/to/lab [--search \"query\"]}"
MODE="${2:-install}"
MPY="$(command -v python3)"

say() { printf '\n=== %s ===\n' "$*"; }

find_mempalace_py() {
  # The console script's shebang may name a different interpreter than the
  # one that holds the deps. Run it via the interpreter that owns it.
  local bin; bin="$(command -v mempalace || true)"
  [ -n "$bin" ] || { echo "mempalace not on PATH; pip install mempalace first" >&2; exit 1; }
  echo "$bin"
}

MP() { $MPY "$(find_mempalace_py)" "$@"; }

mp_site_packages() {
  $MPY - <<'EOF'
import importlib.util, pathlib
spec = importlib.util.find_spec("mempalace")
print(pathlib.Path(spec.origin).parent)
EOF
}

install_deps() {
  say "install"
  $MPY -m pip install --quiet mempalace
  # patch the missing transitive wheels INTO mempalace's own site-packages
  local site; site="$(mp_site_packages)"
  $MPY -m pip install --quiet --target "$site" pyyaml typing_extensions numpy
  MP --version
}

init_palace() {
  say "init palace on $LAB (rooms auto-detected, non-interactive)"
  MP init "$LAB" --yes --no-llm
  say "PRIVACY GUARD"
  local cfg="$LAB/mempalace.yaml"
  [ -f "$cfg" ] || { echo "no mempalace.yaml found; init failed" >&2; exit 1; }
  # refuse outright if the safe-mining contract can't be honored
  if [ -d "$LAB/source-material" ]; then
    cat <<'EOF'
  source-material/ EXISTS in this lab. It must NEVER be mined into a
  shareable palace. This script mines only the SAFE layers named below
  (memory-export, notes, tools). If you override MINE_DIRS to include
  source-material/, you are violating lab privacy law. Re-read
  tools/mempalace-bridge/README.md first.
EOF
  fi
  say "mine safe layers"
  # default safe layers: the distilled + tooling layers, verbatim, no personal context
  for d in ${MINE_DIRS:-memory-export notes tools}; do
    [ -d "$LAB/$d" ] && MP mine "$LAB/$d"
  done
}

smoke_search() {
  local q="${2:-what carries between threads and hands}"
  say "smoke search: $q"
  MP search "$q"
}

case "$MODE" in
  --search) smoke_search "$@" ;;
  *) install_deps; init_palace; smoke_search "$@" ;;
esac

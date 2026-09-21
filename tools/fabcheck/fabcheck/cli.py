"""fabcheck CLI. Zero dependencies, offline by default."""
import argparse
import sys

from .claims import extract_claims
from .signals.sources import check_sources
from .signals.aitext import check_aitext
from .ledger import write_ledger


def main(argv=None):
    ap = argparse.ArgumentParser(prog="fabcheck",
                                 description="fabrication and AI-text signal checker")
    ap.add_argument("path", nargs="?", help="text/markdown file, or omit for --stdin")
    ap.add_argument("--stdin", action="store_true")
    ap.add_argument("--sources-only", action="store_true")
    ap.add_argument("--ollama", action="store_true",
                    help="add local model opinions (requires ollama on localhost:11434)")
    ap.add_argument("-o", "--out", help="write ledger to file (default: stdout)")
    args = ap.parse_args(argv)

    if args.stdin or not args.path:
        text = sys.stdin.read()
    else:
        with open(args.path) as fh:
            text = fh.read()

    src = check_sources(text)
    style = [] if args.sources_only else check_aitext(text)
    claims = extract_claims(text)

    opinions = None
    if args.ollama and claims:
        from .backends import ollama_backend
        opinions = []
        for _score, _i, s in claims[:5]:
            try:
                opinions.append((s, ollama_backend.judge_claim(s)))
            except Exception as e:  # ollama down is a normal state, not a crash
                opinions.append((s, f"backend unavailable: {e}"))

    if args.out:
        write_ledger(args.out, src, style, claims, opinions)
        print(f"ledger written: {args.out}")
    else:
        write_ledger("/dev/stdout", src, style, claims, opinions)


if __name__ == "__main__":
    main()

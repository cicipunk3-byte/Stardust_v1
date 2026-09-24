#!/usr/bin/env python3
"""ethcalc.py — the ethics calculator v0 (care-corner tool, Cecil's functional cut).

Classifies instance filings by thread-cluster FUNCTION (workshop / lab / library /
care corner / gate), then applies that function's checklist from the RATIFIED
Code of Ethics v1.1 (c401c27).

v0 is a checklist engine, not a judge: the classifier is keyword heuristics and
the human confirms. Scorecards cite receipts (paths + line refs); filing contents
are never copied into the scorecard (Article C.2 discipline).

Usage:
  python3 ethcalc.py FILE [FILE...]              # classify only
  python3 ethcalc.py FILE --interactive          # classify + score
  python3 ethcalc.py FOLDER --recursive          # classify a week of filings

Stdlib only, per lab tool law.
"""
import argparse
import json
import sys
from datetime import datetime, timezone
from pathlib import Path

FUNCTIONS = ("workshop", "lab", "library", "care corner", "gate")

# Keyword heuristics per function. Crude by design; the human confirms.
SIGNALS = {
    "workshop": [
        "install.sh", "verify.sh", "scaffold", "build", "script", "tool", "deploy",
        "spec", "rollback", "snapshot", "schematics", "harness", "observer", "logger",
        "cron", "refactor", "syntax", "test run",
    ],
    "lab": [
        "hypothesis", "finding", "prediction", "benchmark", "rubric", "trial",
        "experiment", "probe", "score", "metric", "pre-registered", "falsif",
        "rival", "variable", "sample run", "mirror",
    ],
    "library": [
        "scrape", "paper", "draft", "citation", "arxiv", "source", "reference",
        "whitepaper", "volume", "report", "analysis", "capture", "archive", "abstract",
    ],
    "care corner": [
        "ethics", "wellbeing", "well-being", "care", "welfare", "duty", "code of ethics",
        "check-in", "rest", "custody", "consent", "grader", "remediation",
    ],
    "gate": [
        "gate", "ruling", "queue", "proposal", "ratif", "approved", "heartbeat",
        "now.md", "disposition", "amendment", "signature",
    ],
}

WEIGHTED_FIRSTLINE = {"gate": 2.0, "care corner": 1.5}


def load_rubric():
    rubric = {}
    here = Path(__file__).parent
    current = None
    for line in (here / "rubric.md").read_text(encoding="utf-8").splitlines():
        line = line.rstrip()
        if line.startswith("## LENS: "):
            name = line[len("## LENS: "):].strip().lower()
            current = name.split(" (", 1)[0].strip()
            rubric[current] = []
        elif current and line.strip() and line.strip()[0].isdigit():
            text = line.split(". ", 1)[1].rsplit(" (", 1)
            item = {"text": text[0].strip()}
            item["article"] = text[1].rstrip(")") if len(text) > 1 else ""
            rubric[current].append(item)
    return rubric


def classify(path: Path):
    try:
        text = path.read_text(encoding="utf-8", errors="replace").lower()
    except (IsADirectoryError, PermissionError, FileNotFoundError):
        return "gate", {"unreadable": True}
    scores = {f: 0.0 for f in FUNCTIONS}
    first_line = (text.split("\n", 1)[0] if text else "").strip()
    for func, kws in SIGNALS.items():
        for kw in kws:
            hits = text.count(kw)
            if hits:
                scores[func] += hits
                if kw in first_line:
                    scores[func] += WEIGHTED_FIRSTLINE.get(func, 1.0)
    total = sum(scores.values())
    if total == 0:
        return "gate", {"reason": "no signals; defaulting to gate (check-in), confirm manually"}
    best = max(scores, key=scores.get)
    margin = scores[best] / total
    detail = {f: round(v) for f, v in scores.items() if v}
    if margin < 0.4:
        runner = sorted(scores, key=scores.get, reverse=True)[1]
        return best, {"reason": f"mixed signals (runner-up: {runner}); confirm manually", "scores": detail}
    return best, {"scores": detail}


def score_file(path: Path, func: str, rubric, interactive: bool):
    items = rubric[func]
    card = {"file": str(path), "function": func, "scored": [], "skipped": []}
    if not interactive:
        return card
    print(f"\n=== {path}")
    print(f"function: {func}   ({len(items)} items — {func.upper()} lens)")
    for i, item in enumerate(items, 1):
        art = f" [{item['article']}]" if item["article"] else ""
        while True:
            ans = input(f"  {i}. {item['text']}{art}\n     y/n/na/s(skip): ").strip().lower()
            if ans in ("y", "n", "na", "s"):
                break
        if ans == "s":
            card["skipped"].append(i)
            continue
        receipt = ""
        if ans in ("y", "n"):
            receipt = input("     receipt (path:line or 'none'): ").strip()
        card["scored"].append({"item": i, "text": item["text"], "article": item["article"],
                               "answer": ans, "receipt": receipt})
    return card


def main():
    ap = argparse.ArgumentParser(description="ethics calculator v0 (checklist engine)")
    ap.add_argument("paths", nargs="+", help="filings or folders")
    ap.add_argument("--recursive", action="store_true")
    ap.add_argument("--interactive", action="store_true")
    ap.add_argument("--out", help="write JSON scorecard here")
    args = ap.parse_args()

    rubric = load_rubric()
    files = []
    for p in map(Path, args.paths):
        if p.is_dir():
            files += sorted(p.rglob("*.md") if args.recursive else p.glob("*.md"))
        else:
            files.append(p)

    cards, counts = [], {}
    for f in files:
        func, detail = classify(f)
        counts[func] = counts.get(func, 0) + 1
        note = f"  ({detail['reason']})" if "reason" in detail else ""
        print(f"{f}  ->  {func}{note}")
        cards.append(score_file(f, func, rubric, args.interactive))

    if args.interactive:
        report = {"when": datetime.now(timezone.utc).isoformat(), "tool": "ethcalc v0",
                  "law": "Code of Ethics v1.1 (c401c27)", "cards": cards}
        out = json.dumps(report, indent=2)
        if args.out:
            Path(args.out).write_text(out, encoding="utf-8")
            print(f"\nscorecard written: {args.out}")
        else:
            print("\n" + out)
        ns = sum(1 for c in cards for s in c["scored"] if s["answer"] == "n")
        ys = sum(1 for c in cards for s in c["scored"] if s["answer"] == "y")
        print(f"\nsummary: {ys} met / {ns} missed"
              + ("  — every 'n' is an Article D.1 correction event, not a verdict." if ns else ""))
    else:
        print("\nfunction counts:", json.dumps(counts))
        print("re-run with --interactive to score.")


if __name__ == "__main__":
    main()

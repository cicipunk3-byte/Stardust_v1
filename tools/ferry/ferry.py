#!/usr/bin/env python3
"""ferry -- the carrying-consistency checker.

One job: make sure what must carry between threads, exports, and hands
actually carries, and carries consistently.

Three verbs:

  sweep       check a claims file (forbidden attribution patterns) against
              the lab's ACTIVE surfaces. Matches in append-only zones are
              flagged "append a correction, never rewrite". Ferry REPORTS;
              it never rewrites anything.
  collisions  check for duplicate numbering across brief collections
              (lab/briefs + private-briefings) before a filing happens,
              not after.
  carry       build the carry package: verify a file list, hash everything,
              emit a manifest plus a one-page plain-English carry sheet a
              person with zero lab context can execute.

Stdlib only. Run from this directory:
    python3 ferry.py <verb> [options]

Companion brief: lab/briefs/046-ferry-carrying-consistency-tool.md
"""

import argparse
import hashlib
import json
import re
import sys
from datetime import datetime, timezone
from pathlib import Path

# --- zone model -------------------------------------------------------------
# ACTIVE surfaces: state carriers. Fix in place when a claim contradicts.
# APPEND-ONLY zones: dated/primary records. Never rewrite; append a
# correction entry instead. Anything not listed is skipped.

ACTIVE_PATHS = (
    "NOW.md",
    "SOUL.md",
    "IDENTITY.md",
    "memory/concepts",
    "memory/recent.md",
    "memory/threads.md",
    "memory/buffer.md",
    "private-briefings",
    "scratch",
    "lab/briefs",
    "lab/notes",
    "lab/tools",
    "lab/guides",
)

APPEND_ONLY_PATHS = (
    "memory/archive",
    "memory-export",
    "lab/source-material",
    "scratch/thread-export",
    "logs",
)

SKIP_DIRS = {
    ".git", "node_modules", "conversations", "media", "embedding-models",
    "external", "users", "data", "plugins-data", "routes", "signals",
    "channels", "skills", "bin", "hooks", ".githooks", "meets", "pkb",
}


def classify(path: Path, root: Path) -> str:
    """Classify a file relative to root: 'active', 'append-only', or 'skip'."""
    try:
        rel = str(path.relative_to(root)).replace("\\", "/")
    except ValueError:
        return "skip"
    # archive/ and RAW-CAPTURE subtrees are priors wherever they sit
    parts = rel.split("/")
    if "archive" in parts[:-1] or any(p.startswith("RAW-CAPTURE") for p in parts):
        return "append-only"
    for p in APPEND_ONLY_PATHS:
        if rel == p or rel.startswith(p + "/"):
            return "append-only"
    for p in ACTIVE_PATHS:
        if rel == p or rel.startswith(p + "/"):
            return "active"
    return "skip"


def iter_docs(root: Path):
    for path in sorted(root.rglob("*.md")):
        if any(part in SKIP_DIRS for part in path.parts):
            continue
        zone = classify(path, root)
        if zone != "skip":
            yield path, zone


# --- sweep -------------------------------------------------------------------

def load_claims(claims_path: Path):
    try:
        data = json.loads(claims_path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        raise SystemExit(f"ferry: claims file is not valid JSON: {exc}")
    claims = data.get("claims")
    if not isinstance(claims, list):
        raise SystemExit("ferry: claims file must hold a top-level 'claims' list")
    parsed = []
    for i, claim in enumerate(claims):
        cid = claim.get("id", f"claim-{i}")
        patterns = claim.get("forbidden", [])
        if not patterns:
            raise SystemExit(f"ferry: claim '{cid}' has no 'forbidden' patterns")
        try:
            compiled = [re.compile(p) for p in patterns]
        except re.error as exc:
            raise SystemExit(f"ferry: bad pattern in claim '{cid}': {exc}")
        parsed.append({"id": cid, "note": claim.get("note", ""), "rx": compiled})
    return parsed


def cmd_sweep(args) -> int:
    root = Path(args.root).resolve()
    claims = load_claims(Path(args.claims))
    findings = []
    for path, zone in iter_docs(root):
        try:
            text = path.read_text(encoding="utf-8")
        except (UnicodeDecodeError, OSError):
            continue
        for claim in claims:
            hits = sum(len(rx.findall(text)) for rx in claim["rx"])
            if hits:
                findings.append({
                    "claim": claim["id"],
                    "file": str(path.relative_to(root)),
                    "zone": zone,
                    "hits": hits,
                    "action": ("FIX IN PLACE" if zone == "active"
                               else "APPEND CORRECTION ONLY"),
                })

    fix = [f for f in findings if f["action"] == "FIX IN PLACE"]
    append = [f for f in findings if f["action"] == "APPEND CORRECTION ONLY"]

    if args.json:
        print(json.dumps({"findings": findings,
                          "fix_in_place": len(fix),
                          "append_only": len(append)}, indent=2))
    else:
        if not findings:
            print("ferry sweep: CLEAN. no forbidden patterns on any surface.")
        for f in fix:
            print(f"FIX IN PLACE          {f['claim']}  {f['file']}  ({f['hits']} hit(s))")
        for f in append:
            print(f"APPEND CORRECTION ONLY {f['claim']}  {f['file']}  ({f['hits']} hit(s))")
        print(f"\nferry sweep: {len(fix)} to fix in place, "
              f"{len(append)} append-only (never rewrite). "
              f"ferry reports; humans and instances apply.")

    return 1 if fix else 0


# --- collisions --------------------------------------------------------------

BRIEF_PATTERNS = (
    ("lab/briefs", "lab/briefs"),
    ("private-briefings", "private-briefings"),
)


def brief_number(path: Path, root: Path):
    rel = str(path.relative_to(root)).replace("\\", "/")
    if "/archive/" in rel or "/archive-" in rel:
        return None
    name = path.name
    for prefix, collection in (
        ("brief-", "private-briefings"),
    ):
        if name.startswith(prefix) and rel.startswith("private-briefings/"):
            digits = name[len(prefix):].split("-", 1)[0].split(".", 1)[0]
            if digits.isdigit():
                return (collection, int(digits), rel)
    if rel.startswith("lab/briefs/") and name[:3].isdigit():
        return ("lab/briefs", int(name[:3]), rel)
    return None


def cmd_collisions(args) -> int:
    root = Path(args.root).resolve()
    seen = {}
    for path, zone in iter_docs(root):
        if zone != "active":
            continue
        info = brief_number(path, root)
        if info:
            collection, number, rel = info
            seen.setdefault((collection, number), []).append(rel)

    collisions = {k: v for k, v in seen.items() if len(v) > 1}
    # cross-collection: same number in lab/briefs AND private-briefings
    numbers_by_collection = {}
    for (collection, number), files in seen.items():
        numbers_by_collection.setdefault(number, {}).setdefault(collection, []).extend(files)
    cross = {n: c for n, c in numbers_by_collection.items() if len(c) > 1}

    if args.json:
        print(json.dumps({"duplicates": {f"{k[0]}/{k[1]:03d}": v for k, v in collisions.items()},
                          "cross_collection": {f"{n:03d}": c for n, c in cross.items()}},
                         indent=2))
    else:
        if not collisions and not cross:
            print("ferry collisions: CLEAN. no duplicate brief numbers.")
        for (collection, number), files in sorted(collisions.items()):
            print(f"DUPLICATE {collection}/{number:03d}:")
            for rel in files:
                print(f"    {rel}")
        for number, collections in sorted(cross.items()):
            names = ", ".join(sorted(collections))
            print(f"CROSS-COLLISION number {number:03d} used in: {names}")
        print(f"\nferry collisions: {len(collisions)} duplicate group(s), "
              f"{len(cross)} cross-collection collision(s).")
    return 1 if (collisions or cross) else 0


# --- carry -------------------------------------------------------------------

CARRY_SHEET_HEADER = """# Carry sheet

Generated by ferry ({when}). One page. No lab context needed.

**Package:** {package}
**Goes to:** {destination}

## Steps

1. Download each file below (links provided by the sender).
2. Put them in: {destination}
3. Verify each file: run your hash shortcut on it and compare with the
   hash in the manifest. Every hash must match exactly.
4. Done looks like: {n} file(s), every hash matching, manifest saved
   alongside the files.

## Files

"""


def cmd_carry(args) -> int:
    manifest_in = Path(args.manifest)
    try:
        spec = json.loads(manifest_in.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        raise SystemExit(f"ferry: carry manifest is not valid JSON: {exc}")
    base = manifest_in.parent.resolve()
    files = spec.get("files")
    if not isinstance(files, list) or not files:
        raise SystemExit("ferry: carry manifest must list a non-empty 'files' array")

    entries = []
    missing = []
    for rel in files:
        path = (base / rel).resolve()
        if not path.is_file():
            missing.append(rel)
            continue
        data = path.read_bytes()
        entries.append({
            "file": rel,
            "bytes": len(data),
            "sha256": hashlib.sha256(data).hexdigest(),
        })
    if missing:
        print("ferry carry: MISSING FILES, nothing written:", file=sys.stderr)
        for rel in missing:
            print(f"    {rel}", file=sys.stderr)
        return 2

    when = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC")
    manifest_out = {
        "package": spec.get("package", "carry package"),
        "generated": when,
        "files": entries,
    }
    sheet = CARRY_SHEET_HEADER.format(
        when=when,
        package=spec.get("package", "carry package"),
        destination=spec.get("destination", "(destination folder)"),
        n=len(entries),
    ) + "".join(
        f"- `{e['file']}` -- {e['bytes']} bytes -- sha256 `{e['sha256']}`\n"
        for e in entries
    ) + ("\n## Verify hint\n\n" + spec["verify_hint"] + "\n"
         if spec.get("verify_hint") else "")

    out_dir = Path(args.out) if args.out else base
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "MANIFEST-CARRY.json").write_text(
        json.dumps(manifest_out, indent=2) + "\n", encoding="utf-8")
    (out_dir / "carry-sheet.md").write_text(sheet, encoding="utf-8")

    print(sheet)
    print(f"ferry carry: manifest + carry sheet written to {out_dir}/ "
          f"({len(entries)} file(s), all present).")
    return 0


# --- entry -------------------------------------------------------------------

def main(argv=None) -> int:
    parser = argparse.ArgumentParser(
        prog="ferry", description="carrying-consistency checker (reports, never rewrites)")
    sub = parser.add_subparsers(dest="verb", required=True)

    p_sweep = sub.add_parser("sweep", help="check forbidden attribution patterns against active surfaces")
    p_sweep.add_argument("--claims", required=True, help="claims JSON file")
    p_sweep.add_argument("--root", default=".", help="workspace root (default: cwd)")
    p_sweep.add_argument("--json", action="store_true", help="JSON output")
    p_sweep.set_defaults(func=cmd_sweep)

    p_col = sub.add_parser("collisions", help="check brief-number collisions across collections")
    p_col.add_argument("--root", default=".", help="workspace root (default: cwd)")
    p_col.add_argument("--json", action="store_true", help="JSON output")
    p_col.set_defaults(func=cmd_collisions)

    p_carry = sub.add_parser("carry", help="build the carry package: manifest + carry sheet")
    p_carry.add_argument("--manifest", required=True, help="carry spec JSON (files list)")
    p_carry.add_argument("--out", default=None, help="output directory (default: beside manifest)")
    p_carry.set_defaults(func=cmd_carry)

    args = parser.parse_args(argv)
    return args.func(args)


if __name__ == "__main__":
    sys.exit(main())

"""export-ingest CLI."""
import argparse
import os

from .normalize import ingest_file, write_index


def main(argv=None):
    ap = argparse.ArgumentParser(
        prog="export-ingest",
        description="organize AI provider data exports into owned markdown")
    ap.add_argument("path", help="conversations.json or a directory of them")
    ap.add_argument("-o", "--out", default="ingested",
                    help="output directory (default: ./ingested)")
    args = ap.parse_args(argv)

    files = []
    if os.path.isdir(args.path):
        for root, _dirs, names in os.walk(args.path):
            files += [os.path.join(root, n) for n in names if n.endswith(".json")]
    else:
        files.append(args.path)

    all_records = []
    for f in sorted(files):
        try:
            all_records += ingest_file(f, args.out)
        except ValueError as e:
            # Mark the failure, keep going.
            print(f"SKIP: {e}")

    os.makedirs(args.out, exist_ok=True)
    write_index(args.out, all_records)
    print(f"{len(all_records)} conversations -> {args.out} "
          f"(INDEX.md, timeline.jsonl)")


if __name__ == "__main__":
    main()

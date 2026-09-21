"""Normalize parsed conversations to markdown, an index, and a timeline."""
import json
import os
import re
from datetime import datetime, timezone


def slugify(title, n=60):
    s = re.sub(r"[^a-z0-9]+", "-", title.lower()).strip("-")
    return s[:n].strip("-") or "untitled"


def conversation_md(c):
    lines = [
        f"# {c['title']}", "",
        f"- provider: {c['provider']}",
        f"- created: {c['created'] or 'unknown'}",
        f"- updated: {c['updated'] or 'unknown'}",
        f"- messages: {len(c['messages'])}", "",
    ]
    for m in c["messages"]:
        ts = m.get("ts")
        stamp = f" ({ts})" if ts else ""
        lines.append(f"## {m['role']}{stamp}")
        lines.append("")
        lines.append(m["text"])
        lines.append("")
    return "\n".join(lines)


def ingest_file(path, out_dir):
    from . import detect as det
    provider = det.detect(path)
    parsers = {"chatgpt": "chatgpt", "claude": "claude"}
    records = []
    for conv in det.iter_conversations(path, provider):
        if provider == "gemini":
            from . import gemini
            c = gemini.parse(conv)
        else:
            import importlib
            mod = importlib.import_module(f".{parsers[provider]}", package="ingest")
            c = mod.parse(conv)
        if not c["messages"]:
            continue
        slug = slugify(c["title"])
        subdir = os.path.join(out_dir, provider)
        os.makedirs(subdir, exist_ok=True)
        md_path = os.path.join(subdir, f"{slug}.md")
        with open(md_path, "w") as fh:
            fh.write(conversation_md(c))
        records.append({
            "provider": provider,
            "title": c["title"],
            "created": c["created"],
            "updated": c["updated"],
            "message_count": len(c["messages"]),
            "file": os.path.relpath(md_path, out_dir),
            "stub": c.get("stub", False),
        })
    return records


def write_index(out_dir, all_records):
    lines = ["# Export ingest index", "",
             f"_Generated {datetime.now(timezone.utc).isoformat()}. "
             f"{len(all_records)} conversations._", ""]
    for r in sorted(all_records, key=lambda r: (r["provider"], r["created"] or "")):
        flag = " (STUB: partial parse)" if r["stub"] else ""
        lines.append(f"- [{r['title']}]({r['file']}) "
                     f"| {r['provider']} | {r['created'] or '?'} | "
                     f"{r['message_count']} msgs{flag}")
    with open(os.path.join(out_dir, "INDEX.md"), "w") as fh:
        fh.write("\n".join(lines) + "\n")

    with open(os.path.join(out_dir, "timeline.jsonl"), "w") as fh:
        for r in all_records:
            fh.write(json.dumps(r) + "\n")

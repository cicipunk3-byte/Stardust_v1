"""ChatGPT export parser. conversations.json: list of {title, create_time,
update_time, mapping: {id: {message: {author: {role}, content: {parts}}}}}."""
from datetime import datetime, timezone


def _walk_messages(conv):
    """Flatten the mapping tree into message order by child links."""
    mapping = conv.get("mapping", {})
    # Find root (node with no parent), then follow children depth-first.
    roots = [nid for nid, n in mapping.items() if not n.get("parent")]
    out = []
    seen = set()
    stack = list(reversed(roots))
    while stack:
        nid = stack.pop()
        if nid in seen:
            continue
        seen.add(nid)
        node = mapping.get(nid, {})
        stack.extend(reversed(node.get("children", [])))
        msg = node.get("message")
        if not msg:
            continue
        role = (msg.get("author") or {}).get("role")
        parts = ((msg.get("content") or {}).get("parts")) or []
        text = "\n".join(p for p in parts if isinstance(p, str)).strip()
        if text and role in ("user", "assistant"):
            ts = msg.get("create_time")
            out.append({"role": role, "text": text, "ts": ts})
    return out


def parse(conv):
    ts = conv.get("create_time")
    return {
        "provider": "chatgpt",
        "title": conv.get("title") or "untitled",
        "created": datetime.fromtimestamp(ts, tz=timezone.utc).isoformat() if ts else None,
        "updated": datetime.fromtimestamp(conv["update_time"], tz=timezone.utc).isoformat()
        if conv.get("update_time") else None,
        "messages": _walk_messages(conv),
    }

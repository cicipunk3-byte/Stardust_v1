"""Claude export parser. conversations.json: list of {uuid, name,
created_at, updated_at, chat_messages: [{sender, text, created_at}]}."""
from datetime import datetime


def parse(conv):
    msgs = []
    for m in conv.get("chat_messages", []):
        text = (m.get("text") or "").strip()
        if not text:
            continue
        sender = m.get("sender", "unknown")
        role = "assistant" if sender.startswith("assistant") else sender
        ts = m.get("created_at")
        msgs.append({"role": role, "text": text, "ts": ts})

    def iso(x):
        try:
            return datetime.fromisoformat(x.replace("Z", "+00:00")).isoformat()
        except (TypeError, ValueError, AttributeError):
            return None

    return {
        "provider": "claude",
        "title": conv.get("name") or "untitled",
        "created": iso(conv.get("created_at")),
        "updated": iso(conv.get("updated_at")),
        "messages": msgs,
    }

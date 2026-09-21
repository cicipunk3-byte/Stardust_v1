"""Detect export format by structure, not filename. Files lie; shapes don't."""
import json


def load_json(path):
    with open(path, encoding="utf-8") as fh:
        return json.load(fh)


def detect(path):
    """Returns provider name or raises ValueError with a human-readable why."""
    try:
        data = load_json(path)
    except (json.JSONDecodeError, UnicodeDecodeError) as e:
        raise ValueError(
            f"{path}: not JSON ({e}). If this is a Gemini Takeout it is HTML; "
            "see ingest/gemini.py for the current limits.") from e

    if isinstance(data, list) and data and isinstance(data[0], dict):
        first = data[0]
        if "mapping" in first and "title" in first:
            return "chatgpt"
        if "chat_messages" in first:
            return "claude"
    raise ValueError(
        f"{path}: JSON but unrecognized shape. Expected ChatGPT "
        "(list of {title, mapping}) or Claude (list of {chat_messages}). "
        "Paste a sample into an issue rather than forcing a parser.")


def iter_conversations(path, provider):
    data = load_json(path)
    if provider == "chatgpt":
        yield from data
    elif provider == "claude":
        yield from data

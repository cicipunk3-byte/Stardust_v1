# export-ingest; read and organize AI provider data exports

Free, local, stdlib-only Python. Turns the exports big AI providers give you
into plain markdown you own, organized and indexed. Part of the ThreadCat lab
tooling, built for the local-first rule: the exports land in a git repo, not
in anyone's cloud.

## Formats handled

| Provider | Export shape | Status |
|---|---|---|
| ChatGPT | `conversations.json` with a `mapping` tree | working |
| Claude | `conversations.json` with `chat_messages` list | working |
| Gemini | Google Takeout (`MyActivity.html` / `Gemini`) | stub, see limits |

## Usage

```
python3 -m ingest.cli PATH            # single file or unzipped export dir
python3 -m ingest.cli PATH -o out/    # where the markdown goes
```

Output per conversation: `out/<provider>/<slug>.md` with a metadata header
(provider, title, dates, message counts). Plus:

- `out/INDEX.md`; one line per conversation
- `out/timeline.jsonl`; machine-readable, one record per conversation
  (this is the shape the lab's review tooling already expects)

## Limits (mark failures, do not hide them)

- Gemini Takeout is HTML, not JSON, and Google changes it. The gemini module
  is an honest stub: it detects the format and tells you what to do, it does
  not silently produce garbage.
- Attachments and images are skipped, not extracted.
- Nothing is uploaded anywhere. If a parser needs network, it is broken.

## Layout

- `ingest/detect.py` - format detection by JSON shape, not filename
- `ingest/chatgpt.py`, `ingest/claude.py`, `ingest/gemini.py`
- `ingest/normalize.py` - markdown writer, index, timeline
- `ingest/cli.py` - entry point
- `tests/` - synthetic fixtures in each format

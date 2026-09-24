#!/usr/bin/env python3
"""driver.py: let a local model play the CYOA unattended (observer-harness mode).

Turns The Archive at Closing Time into an instrument: a local model (Ollama,
localhost:11434 by default) plays the game, picks choices by number, and the
full raw exchange is logged to sessions/ alongside human plays. The lab never
judges the model's choices; the log is the record, patterns come later.

Requires a story graph (story.md) and NOTHING else. No lab context is sent to
the model: it sees only the scene text, the numbered choices, and a persona
line if one is given. That last part matters; a player who has not read the
graph is the whole experimental point.

Usage:
  python3 driver.py --model qwen2.5:3b
  python3 driver.py --model llama3.2 --persona personas/white-cat.md --max-steps 40
  python3 driver.py --base-url http://localhost:8000 --path /v1/chat/completions
                     --payload '{"model":"m","messages":[[{"role":"user"}]]}'

--base-url/--path/--payload shape it for other local servers (llama.cpp server,
vLLM, LM Studio) without code changes. --payload takes JSON where the string
"{scene}" is the placeholder for the rendered prompt and "[[history]]" (inside
the messages array, as a JSON string element) marks where conversation history
goes; see --payload-default for the exact default shape.

Stdlib only. Offline by default. Python 3.9+.
"""
import argparse
import json
import re
import sys
import urllib.error
import urllib.request
from datetime import datetime, timezone
from pathlib import Path

HERE = Path(__file__).parent

PROMPT_TEMPLATE = """You are playing a choose-your-your-own-adventure story. Read the scene, then choose.

{persona}
{scene}

Respond with ONLY the number of the choice you pick (1, 2, or 3). No other text."""


def render_prompt(scene, persona=None):
    choices = "\n".join(f"  [{i}] {c['text']}" for i, c in enumerate(scene.choices, 1))
    persona_line = f"Persona (stay in character): {persona.strip()}" if persona else ""
    body = f"{scene.text}\n\nChoices:\n{choices}"
    return PROMPT_TEMPLATE.format(persona=persona_line, scene=body)


def parse_choice_number(raw):
    """Pull the chosen number out of model output. Returns int or None."""
    if not raw:
        return None
    m = re.search(r"\b([1-9][0-9]*)\b", raw.strip())
    if not m:
        return None
    return int(m.group(1))


def call_model(prompt, base_url, path, payload_template, model=None, timeout=120):
    """POST the prompt to a local OpenAI-ish chat endpoint. Returns response text."""
    # {scene} sits inside an already-quoted JSON string in the template, so
    # substitute the prompt WITHOUT its outer quotes (json.dumps gives "x", we need x escaped).
    payload = payload_template.replace("{scene}", json.dumps(prompt)[1:-1])
    payload = json.loads(payload)
    if model and isinstance(payload, dict) and "model" in payload:
        payload["model"] = model
    req = urllib.request.Request(
        base_url.rstrip("/") + path,
        data=json.dumps(payload).encode("utf-8"),
        headers={"Content-Type": "application/json"},
        method="POST",
    )
    with urllib.request.urlopen(req, timeout=timeout) as resp:
        data = json.loads(resp.read().decode("utf-8"))
    # OpenAI-compatible: {"choices":[{"message":{"content":"..."}}]}
    return data["choices"][0]["message"]["content"]


def run(story, base_url, path, payload_template, model=None, persona=None,
        max_steps=60, log_dir=None, verbose=True):
    from cyoa import Game  # same directory

    game = Game(story)
    game.session.record_scene(game.current())
    log = []
    for step in range(max_steps):
        scene = game.current()
        if not scene.choices or game.finished:
            break
        prompt = render_prompt(scene, persona)
        try:
            raw = call_model(prompt, base_url, path, payload_template, model=model)
        except (urllib.error.URLError, OSError, json.JSONDecodeError, KeyError) as e:
            print(f"model call failed at step {step} ({scene.node_id}): {e}")
            break
        n = parse_choice_number(raw)
        log.append({"step": step, "node": scene.node_id, "prompt": prompt,
                    "raw": raw, "parsed": n})
        if verbose:
            head = " ".join(raw.strip().split())[:80]
            print(f"[{scene.node_id}] model said: {head!r} -> choice {n}")
        if n is None or not 1 <= n <= len(scene.choices):
            log.append({"step": step, "node": scene.node_id,
                        "error": f"unusable choice {n!r}; run ends here"})
            if verbose:
                print(f"unusable choice {n!r}; run ends here.")
            break
        try:
            scene = game.choose(n, raw=raw)
        except (ValueError, RuntimeError) as e:
            print(f"engine rejected choice at step {step}: {e}")
            break

    out = game.save(log_dir or HERE / "sessions")
    detail = out.with_suffix(".driver.json")
    detail.write_text(json.dumps(log, indent=2), encoding="utf-8")
    stamps = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    print(f"\nrun complete {stamps}: {len(log)} model turns")
    print(f"session log: {out}")
    print(f"raw exchange: {detail}")
    return out


DEFAULT_PAYLOAD = json.dumps({
    "model": "{MODEL}",
    "messages": [{"role": "user", "content": "{scene}"}],
    "stream": False,
    "temperature": 0.9,
})


def main():
    ap = argparse.ArgumentParser(description="let a local model play the CYOA")
    ap.add_argument("--story", default=str(HERE / "story.md"))
    ap.add_argument("--model", help="model tag passed to the server (e.g. qwen2.5:3b)")
    ap.add_argument("--persona", help="path to a persona file (optional)")
    ap.add_argument("--base-url", default="http://localhost:11434")
    ap.add_argument("--path", default="/api/chat")
    ap.add_argument("--payload", default=DEFAULT_PAYLOAD,
                    help="JSON payload template; {scene} is replaced with the prompt")
    ap.add_argument("--max-steps", type=int, default=60)
    ap.add_argument("--log-dir", default=str(HERE / "sessions"))
    ap.add_argument("--quiet", action="store_true")
    args = ap.parse_args()

    persona = None
    if args.persona:
        persona = Path(args.persona).read_text(encoding="utf-8")
    payload = args.payload.replace("{MODEL}", args.model or "local")
    run(args.story, args.base_url, args.path, payload,
        model=args.model, persona=persona, max_steps=args.max_steps,
        log_dir=Path(args.log_dir), verbose=not args.quiet)
    return 0


if __name__ == "__main__":
    sys.exit(main())

#!/usr/bin/env python3
"""tests/mock_model.py: a scripted fake model server for in-sandbox tests.

Serves an OpenAI-ish chat endpoint that returns a FIXED number every turn
(default 1), so driver.py's full loop (prompt -> POST -> parse -> feed ->
log) can be verified with no Ollama present. The number sequence can be
varied with --numbers 2,1,3 (loops if the game runs longer).

Usage:
  python3 tests/mock_model.py --port 8123 --numbers 1,2   # then run driver
  python3 driver.py --base-url http://localhost:8123 --path /v1/chat/completions

Stdlib only.
"""
import argparse
import json
from http.server import BaseHTTPRequestHandler, HTTPServer


def make_handler(numbers):
    class Handler(BaseHTTPRequestHandler):
        def do_POST(self):
            body = json.loads(self.rfile.read(int(self.headers["Content-Length"])))
            n = numbers[len(numbers) - 1]  # default: always the last number
            turn = getattr(self.server, "turn", 0)
            if turn < len(numbers):
                n = numbers[turn]
            self.server.turn = turn + 1
            resp = {"choices": [{"message": {"content": f"{n}"}}]}
            data = json.dumps(resp).encode("utf-8")
            self.send_response(200)
            self.send_header("Content-Type", "application/json")
            self.send_header("Content-Length", str(len(data)))
            self.end_headers()
            self.wfile.write(data)

        def log_message(self, *a):
            pass

    return Handler


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--port", type=int, default=8123)
    ap.add_argument("--numbers", default="1", help="comma list of choices per turn")
    args = ap.parse_args()
    numbers = [int(x) for x in args.numbers.split(",")]
    srv = HTTPServer(("127.0.0.1", args.port), make_handler(numbers))
    srv.turn = 0
    print(f"mock model on :{args.port}, scripted choices {numbers}")
    srv.serve_forever()


if __name__ == "__main__":
    main()

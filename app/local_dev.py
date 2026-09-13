#!/usr/bin/env python3
"""Local dev runner — serves the static frontend AND the /api/* routes in one process.

Production keeps nginx for static + server.py for API; this file exists only so
`uv run python app/local_dev.py` gives a working http://localhost:8110 locally.
Routes: /  -> doc.html · /tracker/ -> index.html · /brief/ -> not present locally.
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from http.server import ThreadingHTTPServer  # noqa: E402
import server  # noqa: E402

STATIC = {
    "/": "doc.html",
    "/doc.html": "doc.html",
    "/tracker": "index.html",
    "/tracker/": "index.html",
    "/index.html": "index.html",
    "/compare": "compare.html",
    "/compare/": "compare.html",
    "/compare.html": "compare.html",
}


class DevHandler(server.Handler):
    def do_GET(self):
        if self.path.startswith("/api/"):
            return super().do_GET()
        name = STATIC.get(self.path.split("?")[0])
        if not name:
            return self._send(404, {"error": "not found (local dev serves / and /tracker/ only)"})
        path = os.path.join(server.BASE, name)
        with open(path, "rb") as f:
            body = f.read()
        return self._send(200, body, "text/html; charset=utf-8")


if __name__ == "__main__":
    server.ensure_state()
    port = int(os.environ.get("PORT", "8110"))
    srv = ThreadingHTTPServer(("127.0.0.1", port), DevHandler)
    sys.stderr.write(f"academy local dev on http://127.0.0.1:{port}  (/ doc, /tracker/ board, /api/*)\n")
    srv.serve_forever()

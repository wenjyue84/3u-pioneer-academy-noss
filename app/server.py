#!/usr/bin/env python3
"""Academy Tracker — zero-dependency JSON state API.

Serves nothing but /api/*; nginx serves the static frontend and proxies here.

  GET  /api/state    -> current state
  PUT  /api/state    -> replace state (body = full JSON), writes atomically + backup
  GET  /api/export   -> state as a downloadable attachment
  GET  /api/health   -> liveness

State lives in DATA_DIR/state.json. Every write snapshots the previous version to
DATA_DIR/backups/ so a bad PUT is always recoverable — never overwrite blind.
"""
import json
import os
import shutil
import sys
from datetime import datetime, timezone, timedelta
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer

BASE = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(BASE, "data")
STATE = os.path.join(DATA_DIR, "state.json")
BACKUPS = os.path.join(DATA_DIR, "backups")
SEED = os.path.join(BASE, "seed.json")
PORT = int(os.environ.get("PORT", "8110"))
MYT = timezone(timedelta(hours=8))
MAX_BODY = 4 * 1024 * 1024


def now_myt():
    return datetime.now(MYT).isoformat(timespec="seconds")


def ensure_state():
    os.makedirs(DATA_DIR, exist_ok=True)
    os.makedirs(BACKUPS, exist_ok=True)
    if not os.path.exists(STATE):
        with open(SEED, "r", encoding="utf-8") as f:
            data = json.load(f)
        data["updatedAt"] = now_myt()
        write_state(data, backup=False)


def read_state():
    with open(STATE, "r", encoding="utf-8") as f:
        return json.load(f)


def write_state(data, backup=True):
    if backup and os.path.exists(STATE):
        stamp = datetime.now(MYT).strftime("%Y%m%d-%H%M%S")
        shutil.copy2(STATE, os.path.join(BACKUPS, f"state-{stamp}.json"))
        # keep the 60 most recent snapshots
        snaps = sorted(os.listdir(BACKUPS))
        for old in snaps[:-60]:
            try:
                os.remove(os.path.join(BACKUPS, old))
            except OSError:
                pass
    tmp = STATE + ".tmp"
    with open(tmp, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    os.replace(tmp, STATE)


class Handler(BaseHTTPRequestHandler):
    protocol_version = "HTTP/1.1"

    def log_message(self, fmt, *args):
        sys.stderr.write("%s %s\n" % (now_myt(), fmt % args))

    def _send(self, code, payload, ctype="application/json; charset=utf-8", extra=None):
        body = payload if isinstance(payload, bytes) else json.dumps(
            payload, ensure_ascii=False).encode("utf-8")
        self.send_response(code)
        self.send_header("Content-Type", ctype)
        self.send_header("Content-Length", str(len(body)))
        self.send_header("Cache-Control", "no-store")
        for k, v in (extra or {}).items():
            self.send_header(k, v)
        self.end_headers()
        self.wfile.write(body)

    def do_GET(self):
        if self.path == "/api/health":
            return self._send(200, {"ok": True, "at": now_myt()})
        if self.path == "/api/state":
            return self._send(200, read_state())
        if self.path == "/api/export":
            data = read_state()
            stamp = datetime.now(MYT).strftime("%Y%m%d-%H%M")
            body = json.dumps(data, ensure_ascii=False, indent=2).encode("utf-8")
            return self._send(200, body, "application/json; charset=utf-8",
                              {"Content-Disposition":
                               f'attachment; filename="academy-tracker-{stamp}.json"'})
        self._send(404, {"error": "not found"})

    def do_PUT(self):
        if self.path != "/api/state":
            return self._send(404, {"error": "not found"})
        try:
            length = int(self.headers.get("Content-Length", "0"))
        except ValueError:
            return self._send(400, {"error": "bad content-length"})
        if length <= 0 or length > MAX_BODY:
            return self._send(400, {"error": "bad body size"})
        raw = self.rfile.read(length)
        try:
            data = json.loads(raw.decode("utf-8"))
        except (ValueError, UnicodeDecodeError) as e:
            return self._send(400, {"error": f"invalid json: {e}"})
        if not isinstance(data, dict) or not isinstance(data.get("projects"), list):
            return self._send(400, {"error": "payload must have a projects array"})
        data["updatedAt"] = now_myt()
        write_state(data)
        self._send(200, {"ok": True, "updatedAt": data["updatedAt"]})


if __name__ == "__main__":
    ensure_state()
    srv = ThreadingHTTPServer(("127.0.0.1", PORT), Handler)
    sys.stderr.write(f"academy-tracker listening on 127.0.0.1:{PORT}\n")
    srv.serve_forever()

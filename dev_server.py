#!/usr/bin/env python3
"""
dev_server.py — LOCAL-ONLY dev server for the two web apps.

Serves:
  /                -> web/scroll/  (the Torah scroll app, same URLs as before)
  /units/<file>    -> logic/pre_logic_methods_2026-07-28/UNIT_*.html (unit review pages)

Regenerate endpoints (what the ⟳ buttons call — buttons only appear when
GET /regen/ping answers, so the public static deployment never shows them):
  GET  /regen/ping         -> {"ok": true}
  POST /regen/data         -> index_units.py ; index_triage.py ; export_web.py
  POST /regen/unit/<uid>?out=<basename> -> render_unit_html.py <uid> <basename>

Rules of the house: binds 127.0.0.1 only; runs a FIXED allowlist of project
scripts (never arbitrary commands); regeneration is derived-artifact work only
— it can never touch the canonical YAML/markdown (Pre-Code rule).

Run:  python3 dev_server.py            (port 8011)
"""

import json
import re
import subprocess
import sys
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from urllib.parse import urlparse, parse_qs

ROOT = Path(__file__).resolve().parent
SCROLL = ROOT / "web" / "scroll"
UNITS_HTML = ROOT / "logic" / "pre_logic_methods_2026-07-28"
PORT = 8011

UID_RX = re.compile(r"^[a-z0-9_]+$")
OUT_RX = re.compile(r"^UNIT_[A-Za-z0-9_.\-]+\.html$")

DATA_CHAIN = [
    ["index_units.py"],
    ["index_triage.py"],
    ["export_web.py"],
    ["logic/pre_logic_methods_2026-07-28/render_coverage_index.py"],
]


def run_scripts(cmds):
    log = []
    for cmd in cmds:
        p = subprocess.run([sys.executable] + cmd, cwd=str(ROOT),
                           capture_output=True, text=True, timeout=600)
        tail = (p.stdout + p.stderr).strip().splitlines()[-4:]
        log.append("$ python3 %s\n%s" % (" ".join(cmd), "\n".join(tail)))
        if p.returncode != 0:
            return False, "\n".join(log)
    return True, "\n".join(log)


class Handler(SimpleHTTPRequestHandler):
    def __init__(self, *a, **kw):
        super().__init__(*a, directory=str(SCROLL), **kw)

    def _json(self, code, obj):
        body = json.dumps(obj).encode("utf-8")
        self.send_response(code)
        self.send_header("Content-Type", "application/json")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def do_GET(self):
        path = urlparse(self.path).path
        if path == "/regen/ping":
            return self._json(200, {"ok": True})
        if path.startswith("/units/"):
            name = Path(path[len("/units/"):]).name
            f = UNITS_HTML / name
            if f.suffix == ".html" and f.is_file():
                body = f.read_bytes()
                self.send_response(200)
                self.send_header("Content-Type", "text/html; charset=utf-8")
                self.send_header("Content-Length", str(len(body)))
                self.end_headers()
                self.wfile.write(body)
                return
            self.send_error(404)
            return
        return super().do_GET()

    def do_POST(self):
        u = urlparse(self.path)
        if u.path == "/regen/data":
            try:
                ok, log = run_scripts(DATA_CHAIN)
            except Exception as e:
                return self._json(500, {"ok": False, "log": str(e)})
            return self._json(200 if ok else 500, {"ok": ok, "log": log})

        m = re.match(r"^/regen/unit/([^/]+)$", u.path)
        if m:
            uid = m.group(1)
            out = parse_qs(u.query).get("out", [""])[0]
            if not UID_RX.match(uid) or not (ROOT / "logic" / "units" / (uid + ".yaml")).is_file():
                return self._json(400, {"ok": False, "log": "unknown unit id"})
            if not OUT_RX.match(out):
                return self._json(400, {"ok": False, "log": "bad output name"})
            try:
                ok, log = run_scripts([[
                    "logic/pre_logic_methods_2026-07-28/render_unit_html.py",
                    uid, str(UNITS_HTML / out)]])
            except Exception as e:
                return self._json(500, {"ok": False, "log": str(e)})
            return self._json(200 if ok else 500, {"ok": ok, "log": log})

        self.send_error(404)

    def log_message(self, fmt, *args):
        sys.stdout.write("%s %s\n" % (self.address_string(), fmt % args))
        sys.stdout.flush()


if __name__ == "__main__":
    srv = ThreadingHTTPServer(("127.0.0.1", PORT), Handler)
    print("dev server: http://localhost:%d/  (scroll app)" % PORT)
    print("            http://localhost:%d/units/<UNIT_...html>  (unit review pages)" % PORT)
    print("            regen endpoints live; buttons will show in the apps")
    srv.serve_forever()

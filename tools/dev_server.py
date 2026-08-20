#!/usr/bin/env python3
# TorahSim — (c) 2026 Brian LeBlanc · MIT license (see LICENSE at repo root)
"""
dev_server.py — LOCAL-ONLY preview server for the derivation loop.

Serves the DRESSED site — the same tree tools/export_site.py builds and
Cloudflare ships — so what you preview is byte-what-deploys:

  /            the Epic Disclosure
  /scroll/     the scroll (verse trees, morphology, search)
  /scroll/units/UNIT_<id>.html   the derivation review pages
  /run/        the Tanakh run

Regenerate endpoints (the ⟳ buttons in the pages call these; the buttons
only appear when GET /regen/ping answers, so the public static deployment
never shows them — production answers 404 there):

  GET  /regen/ping        -> {"ok": true}
  POST /regen/data        -> press/index_units.py ; press/index_triage.py ;
                             press/export_web.py ;
                             press/render_coverage_index.py ;
                             tools/export_site.py
                             (reindex the canon, re-export the scroll data,
                             rebuild the index page, re-dress the site)
  POST /regen/unit/<uid>?out=UNIT_<...>.html
                          -> press/render_unit_py.py <uid> ;
                             press/render_unit_html.py <uid> -> scroll/units/ ;
                             then re-dress that one page into site/

Rules of the house: binds 127.0.0.1 only; runs a FIXED allowlist of
project scripts (never arbitrary commands, never caller-supplied paths
beyond the validated unit id and output basename); regeneration writes
DERIVED artifacts only — it can never touch the canonical YAML under
logic/ (the Pre-Code rule).

Run:  python3 tools/dev_server.py           (port 8012)
      python3 tools/dev_server.py 8099      (another port)
"""

import json
import re
import subprocess
import sys
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from urllib.parse import urlparse, parse_qs

ROOT = Path(__file__).resolve().parents[1]
SITE = ROOT / "site"
PORT = int(sys.argv[1]) if len(sys.argv) > 1 else 8012

UID_RX = re.compile(r"^[a-z0-9_]+$")
OUT_RX = re.compile(r"^UNIT_[A-Za-z0-9_.\-]+\.html$")

DATA_CHAIN = [
    ["press/index_units.py"],
    ["press/index_triage.py"],
    ["press/export_web.py"],
    ["press/render_coverage_index.py"],
    ["tools/export_site.py"],
]


def run_scripts(cmds):
    log = []
    for cmd in cmds:
        p = subprocess.run([sys.executable] + cmd, cwd=str(ROOT),
                           capture_output=True, text=True, timeout=1800)
        tail = (p.stdout + p.stderr).strip().splitlines()[-4:]
        log.append("$ python3 %s\n%s" % (" ".join(cmd), "\n".join(tail)))
        if p.returncode != 0:
            return False, "\n".join(log)
    return True, "\n".join(log)


def dress_unit_page(name):
    """Re-dress one freshly rendered review page into site/, exactly as
    tools/export_site.py dresses the whole set (its masthead and back
    button are imported, not copied, so the two can never drift)."""
    sys.path.insert(0, str(ROOT / "tools"))
    import export_site as es
    src = ROOT / "scroll" / "units" / name
    dst = SITE / "scroll" / "units" / name
    u = src.read_text(encoding="utf-8")
    m = re.search(r"<body[^>]*>", u)
    u = (u[:m.end()] + "<style>body{margin-top:54px}</style>"
         + es.masthead("../../", "scroll") + es.UNIT_BACK + u[m.end():])
    dst.parent.mkdir(parents=True, exist_ok=True)
    dst.write_text(u, encoding="utf-8")


class Handler(SimpleHTTPRequestHandler):
    def __init__(self, *a, **kw):
        super().__init__(*a, directory=str(SITE), **kw)

    def _json(self, code, obj):
        body = json.dumps(obj).encode("utf-8")
        self.send_response(code)
        self.send_header("Content-Type", "application/json")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def _loopback(self):
        return self.client_address[0] in ("127.0.0.1", "::1")

    def end_headers(self):
        self.send_header("Cache-Control", "no-store")
        super().end_headers()

    def do_GET(self):
        if urlparse(self.path).path == "/regen/ping":
            if not self._loopback():
                return self._json(403, {"ok": False})
            return self._json(200, {"ok": True})
        return super().do_GET()

    def do_POST(self):
        if not self._loopback():
            return self._json(403, {"ok": False,
                                    "log": "regen is loopback-only"})
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
            if not UID_RX.match(uid) or not (
                    ROOT / "logic" / "units" / (uid + ".yaml")).is_file():
                return self._json(400, {"ok": False, "log": "unknown unit id"})
            if not OUT_RX.match(out):
                return self._json(400, {"ok": False, "log": "bad output name"})
            try:
                ok, log = run_scripts([
                    ["press/render_unit_py.py", uid],
                    ["press/render_unit_html.py", uid,
                     str(ROOT / "scroll" / "units" / out)]])
                if ok:
                    dress_unit_page(out)
            except Exception as e:
                return self._json(500, {"ok": False, "log": str(e)})
            return self._json(200 if ok else 500, {"ok": ok, "log": log})

        self.send_error(404)

    def log_message(self, fmt, *args):
        sys.stdout.write("%s %s\n" % (self.address_string(), fmt % args))
        sys.stdout.flush()


if __name__ == "__main__":
    if not (SITE / "index.html").is_file():
        raise SystemExit("site/ is empty — run: python3 tools/export_site.py")
    srv = ThreadingHTTPServer(("127.0.0.1", PORT), Handler)
    print("dev server: http://127.0.0.1:%d/  (the dressed site, as deployed)"
          % PORT)
    print("            regen endpoints live; the pages' hidden ⟳ buttons "
          "will show")
    srv.serve_forever()

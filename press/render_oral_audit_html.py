#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""render_oral_audit_html.py — derived-artifact renderer for ORAL AUDIT
pages (oral-first era, PROCESS.md 2026-08-08).

Reads logic/oral_audit/AUDIT_<uid>_<date>.md (latest for the uid) +
logic/oral_audit/manifests/<uid>_claims.json, RE-RUNS the claims
verifier live, and writes ORAL_AUDIT_<uid>.html next to the UNIT_*.html
pages (served by dev_server.py at /units/). The markdown + manifest are
canonical; this page is read-only display.

Usage: python3 render_oral_audit_html.py <uid> [out.html]
"""
import html
import json
import re
import sys
from datetime import date
from pathlib import Path

HERE = Path(__file__).resolve().parent
REPO = HERE.parent
sys.path.insert(0, str(REPO / "press" / "gates"))
import os
os.chdir(REPO)  # verifier opens DBs by repo-relative name
import verify_claims as VC

CSS = """
body { background:#fff; color:#1f2937; font:16px/1.55 "Charter","Georgia",serif;
       margin:0; padding:2rem 1rem 6rem; }
main { max-width:1100px; margin:0 auto; }
h1 { font-size:1.4rem; border-bottom:2px solid #8a6d1a; padding-bottom:.3rem; }
h2 { font-size:1.1rem; margin-top:2.2rem; border-bottom:1px solid #d7d3c8; padding-bottom:.2rem; }
.meta { color:#6b7280; font-size:.85rem; }
.badge { font:.7rem/1.6 monospace; padding:0 .5rem; border-radius:10px; }
.ok { background:#e8f5ec; color:#0a7a2f; border:1px solid #bfe3ca; }
.gap { background:#fff3e0; color:#b04000; border:1px solid #ecc9a8; }
.bad { background:#fdecec; color:#a11212; border:1px solid #efc4c4; }
table { border-collapse:collapse; width:100%; font-size:.84rem; margin:.5rem 0 1rem; }
th { background:#f0ecdf; text-align:left; font-size:.7rem; letter-spacing:.05em;
     text-transform:uppercase; }
th,td { border:1px solid #d7d3c8; padding:.3rem .55rem; vertical-align:top; }
code { font-family:Menlo,monospace; font-size:.82rem; background:#f7f5ee;
       padding:.1rem .35rem; border-radius:4px; }
.src { font-family:monospace; font-size:.75rem; color:#4a6da7; }
.ev { font-family:Menlo,monospace; font-size:.72rem; color:#6b6455; }
ul { margin:.4rem 0 .9rem; }
li { margin:.25rem 0; }
.note { background:#f5f2ea; border:1px solid #d7d3c8; border-radius:8px;
        padding:.6rem .9rem; font-size:.88rem; margin:.8rem 0; }
"""


def md_to_html(md):
    out, buf, inlist = [], [], False

    def flushp():
        if buf:
            out.append("<p>%s</p>" % inline(" ".join(buf)))
            buf.clear()

    def inline(s):
        s = html.escape(s)
        s = re.sub(r"\*\*(.+?)\*\*", r"<b>\1</b>", s)
        s = re.sub(r"`([^`]+)`", r"<code>\1</code>", s)
        return s

    for raw in md.split("\n"):
        line = raw.rstrip()
        if line.startswith("# "):
            flushp()
            continue  # page builds its own h1
        if line.startswith("## "):
            flushp()
            if inlist:
                out.append("</ul>"); inlist = False
            out.append("<h2>%s</h2>" % inline(line[3:]))
        elif line.startswith("- "):
            flushp()
            if not inlist:
                out.append("<ul>"); inlist = True
            out.append("<li>%s</li>" % inline(line[2:]))
        elif line.startswith("  ") and inlist and line.strip():
            out[-1] = out[-1][:-5] + " " + inline(line.strip()) + "</li>"
        elif not line.strip():
            flushp()
            if inlist:
                out.append("</ul>"); inlist = False
        else:
            if inlist:
                out.append("</ul>"); inlist = False
            buf.append(line.strip())
    flushp()
    if inlist:
        out.append("</ul>")
    return "\n".join(out)


def run_manifest(path):
    claims = json.load(open(path, encoding="utf-8"))
    v = VC.V()
    rows = []
    for cl in claims:
        ck = cl["check"]
        if ck["type"] == "manual":
            st, det = "UNCHECKABLE", ck.get("note", "")
        else:
            ok, det = getattr(v, ck["type"])(ck)
            st = "VERIFIED" if ok else "FAILED"
        rows.append((st, cl))
        cl["_detail"] = det
    return rows


def render(uid, out_path):
    audits = sorted((REPO / "logic/oral_audit").glob("AUDIT_%s_*.md" % uid.split("_")[0] + "_" + uid.split("_")[1] + "*")) or \
             sorted((REPO / "logic/oral_audit").glob("AUDIT_*%s*.md" % "_".join(uid.split("_")[:2])))
    md_path = audits[-1]
    manifest = REPO / "logic/oral_audit/manifests" / ("%s_claims.json" % uid)
    rows = run_manifest(manifest)
    n = {"VERIFIED": 0, "FAILED": 0, "UNCHECKABLE": 0}
    tr = []
    for st, cl in rows:
        n[st] += 1
        klass = {"VERIFIED": "ok", "FAILED": "bad", "UNCHECKABLE": "gap"}[st]
        tr.append(
            "<tr><td><span class='badge %s'>%s</span></td><td>%s</td>"
            "<td class='src'>%s</td><td>%s<br><span class='ev'>%s</span></td></tr>"
            % (klass, st, cl["id"], html.escape(cl["source"]),
               html.escape(cl["claim_en"]), html.escape(str(cl["_detail"]))))
    body = md_to_html(md_path.read_text(encoding="utf-8"))
    unit_page = "UNIT_%s.html" % uid
    page = (
        "<!DOCTYPE html><html><head><meta charset='utf-8'>"
        "<title>ORAL AUDIT — %s</title><style>%s</style></head><body><main>"
        "<h1>ORAL AUDIT — %s</h1>"
        "<p class='meta'>Oral-first era (PROCESS.md 2026-08-08) · crowns = "
        "chain-attested + DB-verified · frozen unit untouched · "
        "<a href='%s'>frozen unit page</a> · English inline everywhere; "
        "not binding religious law.</p>"
        "<div class='note'><b>Live verifier run:</b> "
        "<span class='badge ok'>%d VERIFIED</span> "
        "<span class='badge bad'>%d FAILED</span> "
        "<span class='badge gap'>%d UNCHECKABLE</span> — re-run: "
        "<code>python3 logic/solo_tools/verify_claims.py "
        "logic/oral_audit/manifests/%s_claims.json</code></div>"
        "<h2>Claims manifest (verified live at render time)</h2>"
        "<table><tr><th>status</th><th>id</th><th>source</th>"
        "<th>claim · evidence</th></tr>%s</table>"
        "%s"
        "<p class='meta'>Rendered %s by render_oral_audit_html.py · the "
        "audit markdown + manifest JSON are canonical, this page is "
        "read-only display.</p></main></body></html>"
        % (html.escape(uid), CSS, html.escape(uid), unit_page,
           n["VERIFIED"], n["FAILED"], n["UNCHECKABLE"], uid,
           "\n".join(tr), body, date.today().isoformat()))
    out_path.write_text(page, encoding="utf-8")
    print("wrote %s (%.0f KB) — %d verified / %d failed / %d uncheckable"
          % (out_path, out_path.stat().st_size / 1024,
             n["VERIFIED"], n["FAILED"], n["UNCHECKABLE"]))


if __name__ == "__main__":
    uid = sys.argv[1]
    out = Path(sys.argv[2]) if len(sys.argv) > 2 else \
        HERE / ("ORAL_AUDIT_%s.html" % uid)
    render(uid, out)

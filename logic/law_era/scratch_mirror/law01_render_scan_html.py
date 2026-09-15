#!/usr/bin/env python3
"""Render law01_scan_notes.md -> a house-style HTML page for the dev server.
Derived artifact only; canonical source stays the markdown notes."""
import os as _os
_ROOT = _os.path.normpath(_os.path.join(_os.path.dirname(_os.path.abspath(__file__)), '..', '..', '..'))   # THE PORTABLE REPO (2026-09-15): the repo root from this file's own place
import html, re, time

SRC = "law01_scan_notes.md"
OUT = (_ROOT + "/logic/pre_logic_methods_2026-07-28/LAW01_ORAL_SCAN_exo_21_1-11.html")

text = open(SRC, encoding="utf-8").read()

def inline(s):
    s = html.escape(s)
    s = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", s)
    return s

body, toc = [], []
para, in_ul = [], False

def flush_para():
    global para
    if para:
        body.append('<p dir="auto">%s</p>' % inline(" ".join(para)))
        para = []

def close_ul():
    global in_ul
    if in_ul:
        body.append("</ul>")
        in_ul = False

nbatch = 0
for line in text.split("\n"):
    if line.startswith("## ") or line.startswith("### "):
        flush_para(); close_ul()
        title = line.lstrip("#").strip()
        m = re.match(r"(?:BATCH|Batch) (\d+)", title)
        if m:
            nbatch += 1
            anchor = "batch-%s" % m.group(1)
            toc.append('<a href="#%s">%s</a>' % (anchor, m.group(1)))
        else:
            anchor = re.sub(r"[^a-z0-9]+", "-", title.lower())[:40]
        body.append('<h2 id="%s" dir="auto">%s</h2>' % (anchor, inline(title)))
    elif line.startswith("# "):
        flush_para(); close_ul()
        body.append('<div class="banner" dir="auto">%s</div>' % inline(line[2:].strip()))
    elif line.startswith("- "):
        flush_para()
        if not in_ul:
            body.append("<ul>"); in_ul = True
        body.append('<li dir="auto">%s</li>' % inline(line[2:].strip()))
    elif not line.strip():
        flush_para(); close_ul()
    else:
        para.append(line.strip())
flush_para(); close_ul()

page = """<!doctype html><html><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>LAW ERA — block 1 oral scan: Exodus 21:1-11 (slave laws)</title>
<style>
body { font: 15px/1.6 Georgia, serif; max-width: 900px; margin: 2rem auto;
       padding: 0 1rem; color: #232019; background: #fbfaf6; }
h1 { font-size: 1.45rem; } h2 { font-size: 1.05rem; margin-top: 2.2rem;
     border-bottom: 1px solid #ddd6c3; padding-bottom: .25rem; }
.meta { color: #6b6455; font-size: .9rem; margin-bottom: 1rem; }
.gate { background: #e8f5e9; border: 1px solid #9ccc9c; color: #0a5a1f;
        padding: .6rem .9rem; font-size: .95rem; margin: 1rem 0; }
.banner { background: #f0ecdf; border: 1px solid #d8d1ba; padding: .15rem .8rem;
          font-family: ui-monospace, monospace; font-size: .8rem; color: #57503e; }
.toc { font-family: ui-monospace, monospace; font-size: .85rem; line-height: 2;
       background: #f7f5ee; border: 1px solid #e3ddc9; padding: .6rem .8rem; }
.toc a { margin-right: .45rem; }
p, li { text-align: justify; }
strong { color: #4a3a15; }
a { color: #4a6da7; }
</style></head><body>
<h1>LAW ERA — block 1 oral scan: Exodus 21:1-11 (the slave laws)</h1>
<div class="meta">generated %s from law01_scan_notes.md (canonical: logic/law_era/scratch_mirror/) ·
<a href="UNIT_INDEX.html">⇄ unit index</a> ·
<a href="UNIT_exo_21_the_ordinances.html">v1 unit page (exo_21_the_ordinances, pre-law)</a></div>
<div class="gate">✓ SCAN COMPLETE — 84 bites · 1,962/1,962 required listings read-and-ledgered
(1,936 readable + 26 Tanakh crossrefs) · 0 unread · 0 unruled · BLOCK-1 GATE GREEN.
Full inversion per the FULL ORAL TORAH LAW (2026-08-10). Ledger:
logic/oral_audit/ledgers/Exod_21.jsonl (chapter-wide; blocks 2-3 accumulate here).
Commits: 1cfb827 (bites 1-68) · 11a6b03 (bites 69-84, completion).</div>
<div class="toc">batch digests: %s</div>
%s
</body></html>""" % (time.strftime("%Y-%m-%d"), " ".join(toc), "\n".join(body))

open(OUT, "w", encoding="utf-8").write(page)
print("wrote %s (%d KB, %d batch digests)" % (OUT, len(page)//1024, nbatch))

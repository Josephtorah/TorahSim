#!/usr/bin/env python3
"""md_to_epub_pre.py — the house markdown-to-EPUB builder (grok-mockups/tools/md_to_epub.py, the pattern of
logic/law_era/scratch_mirror/build_*_epub.py) with ONE addition for the Numbers tutorial (2026-09-10): fenced
code blocks (```) become <pre> blocks, kept verbatim, so the probe run, the journal lines and the ask-tool's
output survive the conversion. Everything else is the original: pure zipfile, mimetype stored first,
OEBPS/content.opf + nav.xhtml; chapters split on '## '; the preamble is the title chapter.

Usage: python3 md_to_epub_pre.py <in.md> <out.epub> [title]
"""
import html
import os
import re
import sys
import time
import zipfile


def inline(s):
    s = html.escape(s)
    s = re.sub(r"`([^`]+)`", r"<code>\1</code>", s)
    s = re.sub(r"\*\*([^*]+)\*\*", r"<b>\1</b>", s)
    s = re.sub(r"(?<!\w)\*([^*\n]+)\*(?!\w)", r"<i>\1</i>", s)
    return s


def blocks_to_xhtml(lines):
    out, i = [], 0
    while i < len(lines):
        ln = lines[i]
        if not ln.strip():
            i += 1
            continue
        if ln.startswith("```"):                                   # THE ADDITION: a fenced block, verbatim
            i += 1
            pre = []
            while i < len(lines) and not lines[i].startswith("```"):
                pre.append(lines[i])
                i += 1
            i += 1                                                 # the closing fence
            out.append("<pre>%s</pre>" % html.escape("\n".join(pre)))
        elif ln.startswith("### "):
            out.append("<h3>%s</h3>" % inline(ln[4:].strip()))
            i += 1
        elif ln.strip() in ("---", "***"):
            out.append("<hr/>")
            i += 1
        elif ln.lstrip().startswith("|"):
            rows = []
            while i < len(lines) and lines[i].lstrip().startswith("|"):
                cells = [c.strip() for c in lines[i].strip().strip("|").split("|")]
                if not all(re.fullmatch(r":?-{2,}:?", c) for c in cells):
                    rows.append(cells)
                i += 1
            if rows:
                t = ["<table>"]
                t.append("<tr>%s</tr>" % "".join(
                    "<th>%s</th>" % inline(c) for c in rows[0]))
                for r in rows[1:]:
                    t.append("<tr>%s</tr>" % "".join(
                        "<td>%s</td>" % inline(c) for c in r))
                t.append("</table>")
                out.append("\n".join(t))
        elif ln.lstrip().startswith(">"):
            q = []
            while i < len(lines) and lines[i].lstrip().startswith(">"):
                q.append(lines[i].lstrip()[1:].strip())
                i += 1
            paras, cur = [], []
            for ql in q:
                if ql:
                    cur.append(ql)
                elif cur:
                    paras.append(" ".join(cur))
                    cur = []
            if cur:
                paras.append(" ".join(cur))
            out.append("<blockquote>%s</blockquote>" % "".join(
                "<p>%s</p>" % inline(p) for p in paras))
        elif ln.lstrip().startswith("- "):
            items = []
            while i < len(lines) and lines[i].lstrip().startswith("- "):
                item = [lines[i].lstrip()[2:]]
                i += 1
                while (i < len(lines) and lines[i].strip()
                       and not lines[i].lstrip().startswith(("- ", "#", "|", ">", "```"))
                       and lines[i].startswith("  ")):
                    item.append(lines[i].strip())
                    i += 1
                items.append(" ".join(item))
            out.append("<ul>%s</ul>" % "".join(
                "<li>%s</li>" % inline(x) for x in items))
        elif ln.startswith("# "):
            out.append("<h1>%s</h1>" % inline(ln[2:].strip()))
            i += 1
        else:
            para = []
            while (i < len(lines) and lines[i].strip()
                   and not lines[i].lstrip().startswith(("#", "|", ">", "- ", "```"))
                   and lines[i].strip() not in ("---", "***")):
                para.append(lines[i].strip())
                i += 1
            out.append("<p>%s</p>" % inline(" ".join(para)))
    return "\n".join(out)


CSS = """body{font-family:Georgia,serif;line-height:1.6;margin:5%;}
h1{font-size:1.4em;} h2{font-size:1.2em;} h3{font-size:1.05em;color:#5a4a1e;}
p{text-align:justify;margin:0 0 1em 0;}
code{font-family:Menlo,monospace;font-size:.85em;background:#f5f0e2;padding:0 .2em;}
pre{font-family:Menlo,monospace;font-size:.8em;background:#f5f0e2;padding:.6em .8em;
  white-space:pre-wrap;word-wrap:break-word;border-left:3px solid #c9b88a;margin:1em 0;}
blockquote{margin:1em 1.2em;padding:.4em .9em;border-left:3px solid #c9b88a;
  background:#faf6ea;font-size:.95em;}
table{border-collapse:collapse;margin:1em 0;font-size:.9em;width:100%;}
th,td{border:1px solid #d8ccae;padding:.3em .5em;text-align:left;vertical-align:top;}
th{background:#f0e9d6;}
hr{border:none;border-top:1px solid #d8ccae;margin:1.6em 0;}"""


def build(src, out, title=None):
    text = open(src, encoding="utf-8").read()
    lines = text.split("\n")
    if title is None:
        m = re.search(r"^# (.+)$", text, re.M)
        title = m.group(1).strip() if m else os.path.basename(src)
    # split into chapters on '## ' (never inside a fenced block)
    chapters, cur_title, cur, fenced = [], "Front matter", [], False
    for ln in lines:
        if ln.startswith("```"):
            fenced = not fenced
        if ln.startswith("## ") and not fenced:
            chapters.append((cur_title, cur))
            cur_title, cur = ln[3:].strip(), []
        else:
            cur.append(ln)
    chapters.append((cur_title, cur))

    with zipfile.ZipFile(out, "w") as z:
        z.writestr("mimetype", "application/epub+zip", zipfile.ZIP_STORED)
        z.writestr("META-INF/container.xml", """<?xml version="1.0" encoding="utf-8"?>
<container version="1.0" xmlns="urn:oasis:names:tc:opendocument:xmlns:container">
<rootfiles><rootfile full-path="OEBPS/content.opf" media-type="application/oebps-package+xml"/></rootfiles>
</container>""")
        manifest, spine, navlis = [], [], []
        for n, (ctitle, clines) in enumerate(chapters):
            cid = "ch%02d" % n
            fn = cid + ".xhtml"
            body = blocks_to_xhtml(clines)
            head = "" if n == 0 else "<h2>%s</h2>\n" % inline(ctitle)
            z.writestr("OEBPS/" + fn, """<?xml version="1.0" encoding="utf-8"?>
<!DOCTYPE html>
<html xmlns="http://www.w3.org/1999/xhtml" xmlns:epub="http://www.idpf.org/2007/ops">
<head><title>%s</title><style>%s</style></head>
<body>%s%s</body></html>""" % (html.escape(ctitle), CSS, head, body))
            manifest.append('<item id="%s" href="%s" media-type="application/xhtml+xml"/>' % (cid, fn))
            spine.append('<itemref idref="%s"/>' % cid)
            navlis.append('<li><a href="%s">%s</a></li>' % (fn, html.escape(ctitle)))
        z.writestr("OEBPS/nav.xhtml", """<?xml version="1.0" encoding="utf-8"?>
<!DOCTYPE html>
<html xmlns="http://www.w3.org/1999/xhtml" xmlns:epub="http://www.idpf.org/2007/ops">
<head><title>Contents</title></head>
<body><nav epub:type="toc" id="toc"><h1>Contents</h1><ol>
%s
</ol></nav></body></html>""" % "\n".join(navlis))
        z.writestr("OEBPS/content.opf", """<?xml version="1.0" encoding="utf-8"?>
<package xmlns="http://www.idpf.org/2007/opf" version="3.0" unique-identifier="uid">
<metadata xmlns:dc="http://purl.org/dc/elements/1.1/">
<dc:identifier id="uid">urn:torah-grok:%s:%s</dc:identifier>
<dc:title>%s</dc:title>
<dc:language>en</dc:language>
<dc:creator>Torah Grok workshop</dc:creator>
<meta property="dcterms:modified">%s</meta>
</metadata>
<manifest>
<item id="nav" href="nav.xhtml" media-type="application/xhtml+xml" properties="nav"/>
%s
</manifest>
<spine>
%s
</spine>
</package>""" % (re.sub(r"\W+", "-", os.path.basename(src)).strip("-").lower(),
                 time.strftime("%Y-%m-%d"), html.escape(title),
                 time.strftime("%Y-%m-%dT%H:%M:%SZ"),
                 "\n".join(manifest), "\n".join(spine)))
    words = len(re.sub(r"[#>|*`-]", " ", text).split())
    print("EPUB written: %s (%d KB, %d chapters, ~%d words, ~%d min listening)"
          % (out, os.path.getsize(out) // 1024, len(chapters), words, words // 150))


if __name__ == "__main__":
    if len(sys.argv) < 3:
        sys.exit(__doc__)
    build(sys.argv[1], sys.argv[2], sys.argv[3] if len(sys.argv) > 3 else None)

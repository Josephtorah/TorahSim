#!/usr/bin/env python3
# build_tutorial_epub.py — package the exo-21-as-code tutorial as an EPUB.
# Same hand-rolled EPUB-2 pattern as build_narrative_epub.py (no pandoc on
# this machine). Chapters split on "## Part" headings for the reader's TOC.
# Usage: python3 logic/law_era/scratch_mirror/build_tutorial_epub.py
import os
import re
import zipfile

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(
    os.path.dirname(os.path.abspath(__file__)))))
SRC = os.path.join(ROOT, "logic", "law_era", "tanakh_run",
                   "TUTORIAL_exo21_as_code_2026-08-12.md")
OUT = os.path.join(ROOT, "logic", "law_era", "tanakh_run",
                   "TUTORIAL_exo21_as_code.epub")
TITLE = "Is Exodus 21 Computer Code? — a tutorial for a non-programmer"

def esc(s):
    return s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")

def inline(s):
    s = esc(s)
    s = re.sub(r"\*\*(.+?)\*\*", r"<b>\1</b>", s)
    s = re.sub(r"`([^`]+)`", r"<code>\1</code>", s)
    s = re.sub(r"\*(.+?)\*", r"<i>\1</i>", s)
    return s

def md_to_xhtml(md):
    out, i, lines = [], 0, md.split("\n")
    para = []
    def flush():
        if para:
            out.append("<p>%s</p>" % inline(" ".join(para)))
            del para[:]
    while i < len(lines):
        ln = lines[i]
        if ln.startswith("```"):
            flush()
            i += 1
            block = []
            while i < len(lines) and not lines[i].startswith("```"):
                block.append(esc(lines[i]))
                i += 1
            out.append('<pre class="code">%s</pre>' % "\n".join(block))
        elif ln.startswith("|"):
            flush()
            rows = []
            while i < len(lines) and lines[i].startswith("|"):
                cells = [c.strip() for c in lines[i].strip("|").split("|")]
                if not all(re.match(r"^:?-+:?$", c) for c in cells):
                    rows.append(cells)
                i += 1
            i -= 1
            tag = "th"
            html = ["<table>"]
            for r in rows:
                html.append("<tr>" + "".join(
                    "<%s>%s</%s>" % (tag, inline(c), tag) for c in r) + "</tr>")
                tag = "td"
            html.append("</table>")
            out.append("".join(html))
        elif ln.startswith("### "):
            flush(); out.append("<h3>%s</h3>" % inline(ln[4:]))
        elif ln.startswith("## "):
            flush(); out.append("<h2>%s</h2>" % inline(ln[3:]))
        elif ln.startswith("# "):
            flush(); out.append("<h1>%s</h1>" % inline(ln[2:]))
        elif ln.startswith("> "):
            flush(); out.append("<blockquote><p>%s</p></blockquote>"
                                % inline(ln[2:]))
        elif re.match(r"^\d+\. ", ln):
            flush()
            items = []
            while i < len(lines) and (re.match(r"^\d+\. ", lines[i])
                                      or lines[i].startswith("   ")):
                if re.match(r"^\d+\. ", lines[i]):
                    items.append(re.sub(r"^\d+\. ", "", lines[i]))
                else:
                    items[-1] += " " + lines[i].strip()
                i += 1
            i -= 1
            out.append("<ol>%s</ol>" % "".join(
                "<li>%s</li>" % inline(x) for x in items))
        elif ln.startswith("- "):
            flush()
            items = []
            while i < len(lines) and (lines[i].startswith("- ")
                                      or lines[i].startswith("  ")):
                if lines[i].startswith("- "):
                    items.append(lines[i][2:])
                else:
                    items[-1] += " " + lines[i].strip()
                i += 1
            i -= 1
            out.append("<ul>%s</ul>" % "".join(
                "<li>%s</li>" % inline(x) for x in items))
        elif ln.strip() in ("---", "***"):
            flush(); out.append("<hr/>")
        elif not ln.strip():
            flush()
        else:
            para.append(ln.strip())
        i += 1
    flush()
    return "\n".join(out)

CSS = """body{font-family:Georgia,serif;line-height:1.55;margin:1em}
h1{font-size:1.5em;color:#7a5c1e}h2{font-size:1.25em;color:#7a5c1e;
margin-top:1.6em}h3{font-size:1.05em}
pre.code{background:#f4f0e6;border:1px solid #d8d0bc;padding:.7em;
font-size:.85em;overflow-x:auto;direction:ltr;white-space:pre-wrap}
code{background:#f4f0e6;font-size:.9em}
table{border-collapse:collapse;margin:.8em 0}
td,th{border:1px solid #c9c0aa;padding:.3em .6em;font-size:.92em;
text-align:left}
blockquote{border-left:3px solid #c9a45c;margin-left:0;
padding-left:1em;color:#555}
hr{border:none;border-top:1px solid #c9c0aa;margin:1.6em 0}"""

XHTML = ("""<?xml version="1.0" encoding="utf-8"?>
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.1//EN"
 "http://www.w3.org/TR/xhtml11/DTD/xhtml11.dtd">
<html xmlns="http://www.w3.org/1999/xhtml"><head>
<title>%s</title>
<link rel="stylesheet" type="text/css" href="style.css"/>
</head><body>%s</body></html>""")

def build():
    md = open(SRC, encoding="utf-8").read()
    # split into chapters on "## Part" (keep the preamble as chapter 0)
    parts = re.split(r"(?m)^(?=## Part )", md)
    chapters = []
    for idx, chunk in enumerate(parts):
        m = re.match(r"## (Part [^—\n]+)", chunk)
        title = m.group(1).strip() if m else "Opening"
        chapters.append(("ch%02d" % idx, title, md_to_xhtml(chunk)))
    with zipfile.ZipFile(OUT, "w") as z:
        z.writestr("mimetype", "application/epub+zip",
                   compress_type=zipfile.ZIP_STORED)
        z.writestr("META-INF/container.xml",
                   """<?xml version="1.0"?>
<container version="1.0"
 xmlns="urn:oasis:names:tc:opendocument:xmlns:container">
<rootfiles><rootfile full-path="OEBPS/content.opf"
 media-type="application/oebps-package+xml"/></rootfiles></container>""")
        manifest, spine, navpoints = [], [], []
        for n, (cid, title, body) in enumerate(chapters):
            fn = "%s.xhtml" % cid
            z.writestr("OEBPS/" + fn, XHTML % (esc(title), body))
            manifest.append('<item id="%s" href="%s" '
                            'media-type="application/xhtml+xml"/>' % (cid, fn))
            spine.append('<itemref idref="%s"/>' % cid)
            navpoints.append(
                '<navPoint id="n%d" playOrder="%d"><navLabel><text>%s'
                '</text></navLabel><content src="%s"/></navPoint>'
                % (n + 1, n + 1, esc(title), fn))
        z.writestr("OEBPS/style.css", CSS)
        z.writestr("OEBPS/content.opf", """<?xml version="1.0"?>
<package xmlns="http://www.idpf.org/2007/opf" version="2.0"
 unique-identifier="bid">
<metadata xmlns:dc="http://purl.org/dc/elements/1.1/">
<dc:title>%s</dc:title>
<dc:creator>Torah_Grok — the law era</dc:creator>
<dc:language>en</dc:language>
<dc:identifier id="bid">torah-grok-exo21-tutorial-2026-08-12</dc:identifier>
</metadata>
<manifest>%s
<item id="ncx" href="toc.ncx" media-type="application/x-dtbncx+xml"/>
<item id="css" href="style.css" media-type="text/css"/>
</manifest>
<spine toc="ncx">%s</spine></package>"""
                   % (esc(TITLE), "\n".join(manifest), "\n".join(spine)))
        z.writestr("OEBPS/toc.ncx", """<?xml version="1.0"?>
<ncx xmlns="http://www.daisy.org/z3986/2005/ncx/" version="2005-1">
<head><meta name="dtb:uid"
 content="torah-grok-exo21-tutorial-2026-08-12"/></head>
<docTitle><text>%s</text></docTitle>
<navMap>%s</navMap></ncx>""" % (esc(TITLE), "\n".join(navpoints)))
    print("built:", OUT)
    print("chapters:", len(chapters))

if __name__ == "__main__":
    build()

#!/usr/bin/env python3
# build_disclosure_epub.py — package any Disclosure markdown as an EPUB.
# Generalized from build_law_that_runs_epub.py (same hand-rolled EPUB-2
# pattern; chapters split on "## " headings; tables supported).
# Usage:
#   python3 logic/law_era/scratch_mirror/build_disclosure_epub.py \
#       Disclosure/LeBlanc_Torah_As_Simulation_2026-08-14.md \
#       "The Torah as a Simulation of Creation" [out_basename]
# Output: Disclosure/<out_basename>.epub + a Desktop copy.
import os
import re
import sys
import zipfile

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(
    os.path.dirname(os.path.abspath(__file__)))))

def esc(s):
    return s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")

def inline(s):
    s = s.replace(" · ", ", ")   # TTS: middle-dot separators read badly
    s = esc(s)
    s = re.sub(r"\*\*\*(.+?)\*\*\*", r"<b><i>\1</i></b>", s)
    s = re.sub(r"\*\*(.+?)\*\*", r"<b>\1</b>", s)
    s = re.sub(r"`([^`]+)`", r"<code>\1</code>", s)
    s = re.sub(r"\*(.+?)\*", r"<i>\1</i>", s)
    return s

def punct(s):
    """TTS pause helper: text-to-speech readers run a heading or table
    cell straight into the next block unless it ends in punctuation."""
    s = s.rstrip()
    return s if s.endswith((".", "!", "?", ":", ";")) else s + "."

def md_to_xhtml(md):
    out, i, lines = [], 0, md.split("\n")
    para = []
    def flush():
        if para:
            out.append("<p>%s</p>" % inline(" ".join(para)))
            del para[:]
    while i < len(lines):
        ln = lines[i]
        if ln.startswith("|"):
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
                    "<%s>%s</%s>" % (tag, inline(punct(c)), tag) for c in r)
                    + "</tr>")
                tag = "td"
            html.append("</table>")
            out.append("".join(html))
        elif ln.startswith("### "):
            flush(); out.append("<h3>%s</h3>" % inline(punct(ln[4:])))
        elif ln.startswith("## "):
            flush(); out.append("<h2>%s</h2>" % inline(punct(ln[3:])))
        elif ln.startswith("# "):
            flush(); out.append("<h1>%s</h1>" % inline(punct(ln[2:])))
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
                "<li>%s</li>" % inline(punct(x)) for x in items))
        elif ln.strip() in ("---", "***"):
            flush(); out.append("<hr/>")
        elif not ln.strip():
            flush()
        else:
            para.append(ln.strip())
        i += 1
    flush()
    return "\n".join(out)

CSS = """body{font-family:Georgia,serif;line-height:1.6;margin:1em}
h1{font-size:1.45em;color:#7a5c1e}h2{font-size:1.25em;color:#7a5c1e;
margin-top:1.6em}h3{font-size:1.05em}
code{background:#f4f0e6;font-size:.9em}
table{border-collapse:collapse;margin:.8em 0}
td,th{border:1px solid #c9c0aa;padding:.3em .6em;font-size:.92em;
text-align:left}
blockquote{border-left:3px solid #c9a45c;margin-left:0;
padding-left:1em;color:#555}
hr{border:none;border-top:1px solid #c9c0aa;margin:1.6em 0}"""

XHTML = ("""<?xml version="1.0" encoding="utf-8"?>
<!DOCTYPE html>
<html xmlns="http://www.w3.org/1999/xhtml"><head>
<title>%s</title>
<link rel="stylesheet" type="text/css" href="style.css"/>
</head><body>%s</body></html>""")

NAV = ("""<?xml version="1.0" encoding="utf-8"?>
<!DOCTYPE html>
<html xmlns="http://www.w3.org/1999/xhtml"
 xmlns:epub="http://www.idpf.org/2007/ops"><head>
<title>Contents</title>
<link rel="stylesheet" type="text/css" href="style.css"/>
</head><body><nav epub:type="toc" id="toc"><h1>Contents</h1>
<ol>%s</ol></nav></body></html>""")

def build(src, title, out_base):
    out = os.path.join(ROOT, "Disclosure", out_base + ".epub")
    desktop = os.path.expanduser("~/Desktop/%s.epub" % out_base)
    uid = "leblanc-" + re.sub(r"[^a-z0-9]+", "-", out_base.lower())
    md = open(os.path.join(ROOT, src), encoding="utf-8").read()
    parts = re.split(r"(?m)^(?=## )", md)
    chapters = []
    for idx, chunk in enumerate(parts):
        m = re.match(r"## ([^\n]+)", chunk)
        ctitle = m.group(1).strip() if m else "Front matter"
        chapters.append(("ch%02d" % idx, ctitle, md_to_xhtml(chunk)))
    with zipfile.ZipFile(out, "w") as z:
        z.writestr("mimetype", "application/epub+zip",
                   compress_type=zipfile.ZIP_STORED)
        z.writestr("META-INF/container.xml",
                   """<?xml version="1.0"?>
<container version="1.0"
 xmlns="urn:oasis:names:tc:opendocument:xmlns:container">
<rootfiles><rootfile full-path="OEBPS/content.opf"
 media-type="application/oebps-package+xml"/></rootfiles></container>""")
        manifest, spine, navpoints = [], [], []
        for n, (cid, ctitle, body) in enumerate(chapters):
            fn = "%s.xhtml" % cid
            z.writestr("OEBPS/" + fn, XHTML % (esc(ctitle), body))
            manifest.append('<item id="%s" href="%s" '
                            'media-type="application/xhtml+xml"/>'
                            % (cid, fn))
            spine.append('<itemref idref="%s"/>' % cid)
            navpoints.append(
                '<navPoint id="n%d" playOrder="%d"><navLabel><text>%s'
                '</text></navLabel><content src="%s"/></navPoint>'
                % (n + 1, n + 1, esc(ctitle), fn))
        z.writestr("OEBPS/style.css", CSS)
        navitems = "".join(
            '<li><a href="%s.xhtml">%s</a></li>' % (cid, esc(ctitle))
            for cid, ctitle, _ in chapters)
        z.writestr("OEBPS/nav.xhtml", NAV % navitems)
        z.writestr("OEBPS/content.opf", """<?xml version="1.0"?>
<package xmlns="http://www.idpf.org/2007/opf" version="3.0"
 unique-identifier="bid">
<metadata xmlns:dc="http://purl.org/dc/elements/1.1/">
<dc:title>%s</dc:title>
<dc:creator>Brian LeBlanc</dc:creator>
<dc:language>en</dc:language>
<dc:identifier id="bid">%s</dc:identifier>
<meta property="dcterms:modified">2026-08-15T00:00:00Z</meta>
</metadata>
<manifest>
<item id="nav" href="nav.xhtml" media-type="application/xhtml+xml"
 properties="nav"/>%s
<item id="ncx" href="toc.ncx" media-type="application/x-dtbncx+xml"/>
<item id="css" href="style.css" media-type="text/css"/>
</manifest>
<spine toc="ncx">%s</spine></package>"""
                   % (esc(title), uid, "\n".join(manifest),
                      "\n".join(spine)))
        z.writestr("OEBPS/toc.ncx", """<?xml version="1.0"?>
<ncx xmlns="http://www.daisy.org/z3986/2005/ncx/" version="2005-1">
<head><meta name="dtb:uid" content="%s"/></head>
<docTitle><text>%s</text></docTitle>
<navMap>%s</navMap></ncx>""" % (uid, esc(title), "\n".join(navpoints)))
    import shutil
    shutil.copyfile(out, desktop)
    print("built:", out)
    print("copy:", desktop)
    print("chapters:", len(chapters))

if __name__ == "__main__":
    build(sys.argv[1], sys.argv[2],
          sys.argv[3] if len(sys.argv) > 3 else
          os.path.splitext(os.path.basename(sys.argv[1]))[0])

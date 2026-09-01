#!/usr/bin/env python3
# build_mishnah_tutorial_epub.py — package the Mishnah/Talmud method
# tutorial as an EPUB (owner order 2026-08-31: "Now I need a tutorial
# epub of these insights... hard breaks for pauses, no em dashes").
# Same hand-rolled EPUB-2 pattern as build_tutorial_epub.py. Chapters
# split on "## " headings. Each source paragraph becomes its own <p>
# with breathing room (the hard breaks the owner reads by).
# Usage: python3 logic/law_era/scratch_mirror/build_mishnah_tutorial_epub.py
import os
import re
import zipfile

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(
    os.path.dirname(os.path.abspath(__file__)))))
SRC = os.path.join(ROOT, "World", "step9",
                   "TUTORIAL_mishnah_talmud_2026-08-31.md")
OUT = os.path.join(ROOT, "The_Answer_Key.epub")
TITLE = "The Answer Key: How the Mishnah and Talmud Test the Machine"


def esc(s):
    return s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


def inline(s):
    s = esc(s)
    s = re.sub(r"\*\*(.+?)\*\*", r"<b>\1</b>", s)
    s = re.sub(r"`([^`]+)`", r"<code>\1</code>", s)
    s = re.sub(r"\*(.+?)\*", r"<i>\1</i>", s)
    return s


def md_to_xhtml(md):
    out, para = [], []

    def flush():
        if para:
            out.append('<p class="pause">%s</p>' % inline(" ".join(para)))
            del para[:]

    for ln in md.split("\n"):
        if ln.startswith("## "):
            flush()
            out.append("<h2>%s</h2>" % inline(ln[3:]))
        elif ln.startswith("# "):
            flush()
            out.append("<h1>%s</h1>" % inline(ln[2:]))
        elif not ln.strip():
            flush()
        else:
            para.append(ln.strip())
    flush()
    return "\n".join(out)


CSS = """body{font-family:Georgia,serif;line-height:1.6;margin:1em}
h1{font-size:1.5em;color:#7a5c1e}
h2{font-size:1.25em;color:#7a5c1e;margin-top:1.6em}
p.pause{margin:0 0 1.15em 0}
code{background:#f4f0e6;font-size:.9em}"""

XHTML = ("""<?xml version="1.0" encoding="utf-8"?>
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.1//EN"
 "http://www.w3.org/TR/xhtml11/DTD/xhtml11.dtd">
<html xmlns="http://www.w3.org/1999/xhtml"><head>
<title>%s</title>
<link rel="stylesheet" type="text/css" href="style.css"/>
</head><body>%s</body></html>""")


def build():
    md = open(SRC, encoding="utf-8").read()
    parts = re.split(r"(?m)^(?=## )", md)
    chapters = []
    for idx, chunk in enumerate(parts):
        m = re.match(r"## ([^\n]+)", chunk)
        title = m.group(1).strip() if m else "The Answer Key"
        chapters.append(("ch%02d" % idx, title, md_to_xhtml(chunk)))
    with zipfile.ZipFile(OUT, "w") as z:
        z.writestr("mimetype", "application/epub+zip",
                   compress_type=zipfile.ZIP_STORED)
        z.writestr("META-INF/container.xml", """<?xml version="1.0"?>
<container version="1.0"
 xmlns="urn:oasis:names:tc:opendocument:xmlns:container">
<rootfiles><rootfile full-path="OEBPS/content.opf"
 media-type="application/oebps-package+xml"/></rootfiles></container>""")
        manifest, spine, navpoints = [], [], []
        for n, (cid, title, body) in enumerate(chapters):
            fn = "%s.xhtml" % cid
            z.writestr("OEBPS/" + fn, XHTML % (esc(title), body))
            manifest.append('<item id="%s" href="%s" '
                            'media-type="application/xhtml+xml"/>'
                            % (cid, fn))
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
<dc:creator>Torah_Grok</dc:creator>
<dc:language>en</dc:language>
<dc:identifier id="bid">torah-grok-answer-key-2026-08-31</dc:identifier>
</metadata>
<manifest>%s
<item id="ncx" href="toc.ncx" media-type="application/x-dtbncx+xml"/>
<item id="css" href="style.css" media-type="text/css"/>
</manifest>
<spine toc="ncx">%s</spine>
</package>""" % (esc(TITLE), "\n".join(manifest), "\n".join(spine)))
        z.writestr("OEBPS/toc.ncx", """<?xml version="1.0"?>
<ncx xmlns="http://www.daisy.org/z3986/2005/ncx/" version="2005-1">
<head><meta name="dtb:uid" content="torah-grok-answer-key-2026-08-31"/>
</head>
<docTitle><text>%s</text></docTitle>
<navMap>%s</navMap></ncx>""" % (esc(TITLE), "\n".join(navpoints)))
    print("wrote", OUT)


if __name__ == "__main__":
    build()

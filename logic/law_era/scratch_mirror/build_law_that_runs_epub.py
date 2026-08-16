#!/usr/bin/env python3
# build_law_that_runs_epub.py — package the Epic Certainty draft addition
# ("The law that runs") as an EPUB. Same hand-rolled EPUB-2 pattern as
# build_tutorial_epub.py; chapters split on "## " headings.
# Usage: python3 logic/law_era/scratch_mirror/build_law_that_runs_epub.py
import os
import re
import zipfile

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(
    os.path.dirname(os.path.abspath(__file__)))))
SRC = os.path.join(ROOT, "Disclosure",
                   "DRAFT_addition_The_Law_That_Runs_2026-08-14.md")
OUT = os.path.join(ROOT, "Disclosure", "The_Law_That_Runs_draft.epub")
DESKTOP = os.path.expanduser("~/Desktop/The_Law_That_Runs_draft.epub")
TITLE = ("The Law That Runs — draft addition to God's Open Source "
         "Software Project")
UID = "leblanc-law-that-runs-draft-2026-08-14"

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
        if ln.startswith("### "):
            flush(); out.append("<h3>%s</h3>" % inline(ln[4:]))
        elif ln.startswith("## "):
            flush(); out.append("<h2>%s</h2>" % inline(ln[3:]))
        elif ln.startswith("# "):
            flush(); out.append("<h1>%s</h1>" % inline(ln[2:]))
        elif ln.startswith("**") and ln.rstrip().endswith("**") and \
                ln.count("**") == 2 and ":" in ln:
            flush(); out.append("<p>%s</p>" % inline(ln))
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

CSS = """body{font-family:Georgia,serif;line-height:1.6;margin:1em}
h1{font-size:1.45em;color:#7a5c1e}h2{font-size:1.25em;color:#7a5c1e;
margin-top:1.6em}h3{font-size:1.05em}
code{background:#f4f0e6;font-size:.9em}
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
    parts = re.split(r"(?m)^(?=## )", md)
    chapters = []
    for idx, chunk in enumerate(parts):
        m = re.match(r"## ([^\n]+)", chunk)
        title = m.group(1).strip() if m else "About this draft"
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
<dc:creator>Brian LeBlanc</dc:creator>
<dc:language>en</dc:language>
<dc:identifier id="bid">%s</dc:identifier>
</metadata>
<manifest>%s
<item id="ncx" href="toc.ncx" media-type="application/x-dtbncx+xml"/>
<item id="css" href="style.css" media-type="text/css"/>
</manifest>
<spine toc="ncx">%s</spine></package>"""
                   % (esc(TITLE), UID, "\n".join(manifest), "\n".join(spine)))
        z.writestr("OEBPS/toc.ncx", """<?xml version="1.0"?>
<ncx xmlns="http://www.daisy.org/z3986/2005/ncx/" version="2005-1">
<head><meta name="dtb:uid" content="%s"/></head>
<docTitle><text>%s</text></docTitle>
<navMap>%s</navMap></ncx>""" % (UID, esc(TITLE), "\n".join(navpoints)))
    import shutil
    shutil.copyfile(OUT, DESKTOP)
    print("built:", OUT)
    print("copy:", DESKTOP)
    print("chapters:", len(chapters))

if __name__ == "__main__":
    build()

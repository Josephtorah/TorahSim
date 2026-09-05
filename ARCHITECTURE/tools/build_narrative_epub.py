#!/usr/bin/env python3
"""build_narrative_epub.py — the 78 paragraphs alone, as a listening book.

Reads ARCHITECTURE/NARRATIVE.md (one heading per block, the summary's
bullets, a paragraph indented under each) and writes:

  ARCHITECTURE/program/The_Program_In_Narrative.epub
  ARCHITECTURE/program/The_Program_In_Narrative.md   (the twin, same text)

One chapter per block, in scroll order, titled with the block's name, its
English, and its span. Inside a chapter each paragraph is introduced by
its bullet sentence as a short heading. Nothing else from the linked page
is carried: no counts, no modes, no units, no verses, no code, no
evidence. House style for the ear: no em dashes; every Hebrew-derived
term with its English beside it (already so in the source file).

    python3 ARCHITECTURE/tools/build_narrative_epub.py
"""
import html, os, re, sys, time, zipfile

HERE = os.path.dirname(os.path.abspath(__file__))
ARCH = os.path.dirname(HERE)
SRC = os.path.join(ARCH, "NARRATIVE.md")
OUT_DIR = os.path.join(ARCH, "program")
TITLE = "The Program in Narrative"
SUBTITLE = "What the code does, block by block, from Genesis 1:1 to the end of Leviticus"
UID = "urn:torah-grok:program-in-narrative:2026-09-05"


def parse(path):
    """-> [(name, gloss, book_span, [(bullet, paragraph), ...]), ...]"""
    blocks, cur = [], None
    for line in open(path, encoding="utf-8").read().split("\n"):
        if line.startswith("## "):
            head = line[3:]
            name_part, _, span_part = head.partition(" — ")
            m = re.match(r"(.+?)\s*\((.+?)\)\s*$", name_part.strip())
            name, gloss = (m.group(1).strip(), m.group(2).strip()) if m else (name_part.strip(), "")
            cur = (name, gloss, span_part.strip(), [])
            blocks.append(cur)
        elif cur is not None and line.startswith("- "):
            cur[3].append([line[2:].strip(), ""])
        elif cur is not None and line.startswith("  ") and line.strip() and cur[3]:
            cur[3][-1][1] = (cur[3][-1][1] + " " + line.strip()).strip()
    return blocks


def clean(s):
    """the house style for the ear: no em dashes, no double spaces"""
    s = s.replace(" — ", ", ").replace("—", ", ").replace(" – ", ", ")
    return re.sub(r"\s+", " ", s).strip()


def xhtml(title, body_html):
    return ("""<?xml version="1.0" encoding="utf-8"?>
<!DOCTYPE html>
<html xmlns="http://www.w3.org/1999/xhtml" xmlns:epub="http://www.idpf.org/2007/ops">
<head><title>%s</title>
<style>body{font-family:Georgia,serif;line-height:1.6;margin:5%%;}
h2{font-size:1.2em;} h3{font-size:1em;font-style:italic;font-weight:normal;color:#444;margin:1.4em 0 .3em;}
p{text-align:justify;margin:0 0 1em 0;}</style></head>
<body>%s</body></html>""" % (html.escape(title), body_html))


def main():
    blocks = parse(SRC)
    os.makedirs(OUT_DIR, exist_ok=True)
    chapters = []   # (cid, title, body_html, md_lines)
    book_of = {}
    n_par = 0
    for i, (name, gloss, span, items) in enumerate(blocks, 1):
        book = span.split(" ")[0] if span else ""
        book_of[i] = book
        title = "%d. %s%s. %s" % (i, name, (" (%s)" % gloss) if gloss else "", clean(span))
        body = ["<h2>%s</h2>" % html.escape(title)]
        md = ["## %s" % title, ""]
        for bullet, para in items:
            if not para:
                continue
            n_par += 1
            body.append("<h3>%s</h3>" % html.escape(clean(bullet)))
            body.append("<p>%s</p>" % html.escape(clean(para)))
            md += ["### " + clean(bullet), "", clean(para), ""]
        chapters.append(("ch%02d" % i, title, "\n".join(body), md))

    # ---- the markdown twin
    md_out = ["# %s" % TITLE, "", SUBTITLE + ".", "",
              "Thirty-three chapters, one per block of the program, cut at the scroll's weekly-portion breaks. "
              "Each chapter holds the block's paragraphs, introduced by the summary sentence each one expands. "
              "Every paragraph keeps one shape: what happens in the text; what the machine does with it; what the "
              "tradition adds, with its source named; what carries forward. Written 2026, September 5, from the "
              "frozen units' own state summaries, exports, and witness notes. Generated from ARCHITECTURE/NARRATIVE.md.", ""]
    cur_book = None
    for i, (cid, title, body, md) in enumerate(chapters, 1):
        if book_of[i] != cur_book:
            cur_book = book_of[i]
            md_out += ["# %s" % cur_book, ""]
        md_out += md
    md_path = os.path.join(OUT_DIR, "The_Program_In_Narrative.md")
    open(md_path, "w", encoding="utf-8").write("\n".join(md_out))

    # ---- the epub
    epub_path = os.path.join(OUT_DIR, "The_Program_In_Narrative.epub")
    with zipfile.ZipFile(epub_path, "w") as z:
        z.writestr("mimetype", "application/epub+zip", zipfile.ZIP_STORED)
        z.writestr("META-INF/container.xml", """<?xml version="1.0" encoding="utf-8"?>
<container version="1.0" xmlns="urn:oasis:names:tc:opendocument:xmlns:container">
<rootfiles><rootfile full-path="OEBPS/content.opf" media-type="application/oebps-package+xml"/></rootfiles>
</container>""")
        manifest, spine, navlis, navpts = [], [], [], []
        intro = xhtml(TITLE, "<h2>%s</h2><p><i>%s.</i></p><p>%s</p>" % (
            html.escape(TITLE), html.escape(SUBTITLE), html.escape(md_out[4])))
        z.writestr("OEBPS/intro.xhtml", intro)
        manifest.append('<item id="intro" href="intro.xhtml" media-type="application/xhtml+xml"/>')
        spine.append('<itemref idref="intro"/>')
        navlis.append('<li><a href="intro.xhtml">%s</a></li>' % html.escape(TITLE))
        navpts.append('<navPoint id="np1" playOrder="1"><navLabel><text>%s</text></navLabel><content src="intro.xhtml"/></navPoint>' % html.escape(TITLE))
        for n, (cid, title, body, _) in enumerate(chapters, 2):
            fn = cid + ".xhtml"
            z.writestr("OEBPS/" + fn, xhtml(title, body))
            manifest.append('<item id="%s" href="%s" media-type="application/xhtml+xml"/>' % (cid, fn))
            spine.append('<itemref idref="%s"/>' % cid)
            navlis.append('<li><a href="%s">%s</a></li>' % (fn, html.escape(title)))
            navpts.append('<navPoint id="np%d" playOrder="%d"><navLabel><text>%s</text></navLabel><content src="%s"/></navPoint>'
                          % (n, n, html.escape(title), fn))
        z.writestr("OEBPS/nav.xhtml", """<?xml version="1.0" encoding="utf-8"?>
<!DOCTYPE html>
<html xmlns="http://www.w3.org/1999/xhtml" xmlns:epub="http://www.idpf.org/2007/ops">
<head><title>Contents</title></head>
<body><nav epub:type="toc" id="toc"><h1>Contents</h1><ol>
%s
</ol></nav></body></html>""" % "\n".join(navlis))
        z.writestr("OEBPS/toc.ncx", """<?xml version="1.0" encoding="utf-8"?>
<ncx xmlns="http://www.daisy.org/z3986/2005/ncx/" version="2005-1">
<head><meta name="dtb:uid" content="%s"/><meta name="dtb:depth" content="1"/></head>
<docTitle><text>%s</text></docTitle>
<navMap>
%s
</navMap></ncx>""" % (UID, html.escape(TITLE), "\n".join(navpts)))
        z.writestr("OEBPS/content.opf", """<?xml version="1.0" encoding="utf-8"?>
<package xmlns="http://www.idpf.org/2007/opf" version="3.0" unique-identifier="uid">
<metadata xmlns:dc="http://purl.org/dc/elements/1.1/">
<dc:identifier id="uid">%s</dc:identifier>
<dc:title>%s</dc:title>
<dc:language>en</dc:language>
<dc:creator>Torah Grok workshop</dc:creator>
<meta property="dcterms:modified">%s</meta>
</metadata>
<manifest>
<item id="nav" href="nav.xhtml" media-type="application/xhtml+xml" properties="nav"/>
<item id="ncx" href="toc.ncx" media-type="application/x-dtbncx+xml"/>
%s
</manifest>
<spine toc="ncx">
%s
</spine>
</package>""" % (UID, html.escape(TITLE), time.strftime("%Y-%m-%dT%H:%M:%SZ"), "\n".join(manifest), "\n".join(spine)))

    words = sum(len(p.split()) for _, _, _, items in blocks for _, p in items if p)
    text_all = "\n".join(md_out)
    assert "—" not in text_all, "em dash in output"
    print("wrote %s (%d KB) and its .md twin: %d chapters, %d paragraphs, ~%d words, ~%d min listening"
          % (os.path.relpath(epub_path, os.path.dirname(ARCH)), os.path.getsize(epub_path) // 1024,
             len(chapters), n_par, words, words // 150))


if __name__ == "__main__":
    main()

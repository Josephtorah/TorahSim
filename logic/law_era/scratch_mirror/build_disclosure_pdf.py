#!/usr/bin/env python3
# build_disclosure_pdf.py — render a Disclosure markdown as a paginated
# PDF. Reuses build_disclosure_epub.py's markdown converter, then feeds
# the HTML to Apple's TextKit (NSAttributedString HTML import) and prints
# to a PDF file via NSPrintOperation — WebKit-quality Hebrew/nikud/RTL
# with no third-party renderer.
# Usage:
#   python3 logic/law_era/scratch_mirror/build_disclosure_pdf.py \
#       Disclosure/<doc>.md "<Title>" [out_basename]
# Output: Disclosure/<out_basename>.pdf + a Desktop copy.
import importlib.util
import os
import shutil
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(os.path.dirname(HERE)))

_spec = importlib.util.spec_from_file_location(
    "build_disclosure_epub", os.path.join(HERE, "build_disclosure_epub.py"))
_epub = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_epub)

CSS = """body{font-family:Georgia,serif;font-size:11.5pt;line-height:1.55}
h1{font-size:19pt;color:#7a5c1e}
h2{font-size:15pt;color:#7a5c1e}
h3{font-size:12.5pt}
table{border-collapse:collapse}
td,th{font-size:9.5pt;border:1px solid #c9c0aa;padding:3px 6px;
text-align:left}
code{font-family:Menlo,monospace;font-size:9.5pt}
hr{border:none;border-top:1px solid #c9c0aa}"""

# US letter, 0.75in top/bottom, ~0.8in sides
PAGE_W, PAGE_H = 612.0, 792.0
M_TOP, M_BOTTOM, M_SIDE = 54.0, 54.0, 58.0


def build(src, title, out_base):
    out_pdf = os.path.join(ROOT, "Disclosure", out_base + ".pdf")
    desktop = os.path.expanduser("~/Desktop/%s.pdf" % out_base)
    md = open(os.path.join(ROOT, src), encoding="utf-8").read()
    body = _epub.md_to_xhtml(md)
    html = ("<html><head><meta charset='utf-8'><title>%s</title>"
            "<style>%s</style></head><body>%s</body></html>"
            % (_epub.esc(title), CSS, body))

    from AppKit import (NSApplication, NSAttributedString, NSMakeRect,
                        NSPrintInfo, NSPrintJobSavingURL, NSPrintOperation,
                        NSPrintSaveJob, NSTextView)
    from Foundation import NSData, NSURL

    NSApplication.sharedApplication()
    raw = html.encode("utf-8")
    data = NSData.dataWithBytes_length_(raw, len(raw))
    astr, _attrs = (NSAttributedString.alloc()
                    .initWithHTML_documentAttributes_(data, None))
    assert astr is not None and astr.length() > 0, "HTML import failed"

    text_w = PAGE_W - 2 * M_SIDE
    tv = NSTextView.alloc().initWithFrame_(
        NSMakeRect(0, 0, text_w, PAGE_H - M_TOP - M_BOTTOM))
    tv.textStorage().setAttributedString_(astr)

    # TextKit lays glyphs out lazily; printing paginates only what is laid
    # out. Force layout of the entire text and grow the view to hold it,
    # or every page after the initial frame prints blank.
    lm, tc = tv.layoutManager(), tv.textContainer()
    lm.glyphRangeForTextContainer_(tc)
    used = lm.usedRectForTextContainer_(tc)
    tv.setFrameSize_((text_w, used.size.height + 10))
    lm.glyphRangeForTextContainer_(tc)

    pi = NSPrintInfo.sharedPrintInfo().copy()
    pi.setTopMargin_(M_TOP)
    pi.setBottomMargin_(M_BOTTOM)
    pi.setLeftMargin_(M_SIDE)
    pi.setRightMargin_(M_SIDE)
    pi.setJobDisposition_(NSPrintSaveJob)
    pi.dictionary()[NSPrintJobSavingURL] = NSURL.fileURLWithPath_(out_pdf)

    op = NSPrintOperation.printOperationWithView_printInfo_(tv, pi)
    op.setShowsPrintPanel_(False)
    op.setShowsProgressPanel_(False)
    ok = op.runOperation()
    assert ok, "print operation failed"

    pages = open(out_pdf, "rb").read().count(b"/Type /Page ")
    shutil.copyfile(out_pdf, desktop)
    print("built:", out_pdf)
    print("copy:", desktop)
    print("pages:", pages)


if __name__ == "__main__":
    build(sys.argv[1], sys.argv[2],
          sys.argv[3] if len(sys.argv) > 3 else
          os.path.splitext(os.path.basename(sys.argv[1]))[0])

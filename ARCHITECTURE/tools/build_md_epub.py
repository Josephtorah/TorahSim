#!/usr/bin/env python3
"""A markdown file to an EPUB (2026-09-16, on the owner's "create an epub also" for THE_TEN_AS_A_SCHEMA.md).
    python3 ARCHITECTURE/tools/build_md_epub.py ARCHITECTURE/THE_TEN_AS_A_SCHEMA.md
Writes the .epub beside the .md. Handles: # / ## / ### headers (each ## opens a chapter), paragraphs, bullet and numbered lists,
pipe tables, horizontal rules, fenced code blocks, > blockquotes, **bold**, *italic*, `code`, [links] (as their text). No external tool (pandoc is not installed here)."""
import html, os, re, sys, time, uuid, zipfile
import xml.etree.ElementTree as ET

def inline(s):
    s = html.escape(s, quote=False)
    s = re.sub(r'\[([^\]]+)\]\(([^)]+)\)', r'\1', s)   # [text](file) -> text (the target file is not inside the epub; 2026-09-18)
    s = re.sub(r'`([^`]+)`', r'<code>\1</code>', s)
    s = re.sub(r'\*\*([^*]+)\*\*', r'<b>\1</b>', s)
    s = re.sub(r'(?<![\w*])\*([^*\n]+)\*(?![\w*])', r'<i>\1</i>', s)
    return s

def blocks(lines):
    """yield ('h', level, text) | ('p', text) | ('ul'|'ol', [items]) | ('table', header, rows) | ('hr',)"""
    i, n = 0, len(lines)
    while i < n:
        l = lines[i]
        if not l.strip(): i += 1; continue
        if l.startswith('#'):
            m = re.match(r'(#+)\s+(.*)', l); yield ('h', len(m.group(1)), m.group(2).strip()); i += 1; continue
        if l.strip().startswith('```'):   # a fenced block, verbatim (2026-09-21: diagrams and commands)
            i += 1; code = []
            while i < n and not lines[i].strip().startswith('```'): code.append(lines[i]); i += 1
            i += 1; yield ('pre', '\n'.join(code)); continue
        if l.startswith('>'):             # a blockquote (2026-09-21)
            q = []
            while i < n and lines[i].startswith('>'): q.append(lines[i].lstrip('>').strip()); i += 1
            yield ('bq', ' '.join(x for x in q if x)); continue
        if l.strip() == '---': yield ('hr',); i += 1; continue
        if l.startswith('|'):
            rows = []
            while i < n and lines[i].startswith('|'):
                cells = [c.strip() for c in lines[i].strip().strip('|').split('|')]
                if not all(re.fullmatch(r'-+', c) for c in cells): rows.append(cells)
                i += 1
            yield ('table', rows[0], rows[1:]); continue
        m = re.match(r'(\s*)([-*]|\d+\.)\s+(.*)', l)
        if m:
            kind = 'ol' if m.group(2)[0].isdigit() else 'ul'; items = []
            while i < n:
                m2 = re.match(r'(\s*)([-*]|\d+\.)\s+(.*)', lines[i])
                if m2 and (('ol' if m2.group(2)[0].isdigit() else 'ul') == kind):
                    items.append(m2.group(3)); i += 1
                elif lines[i].startswith('  ') and lines[i].strip() and items:
                    items[-1] += ' ' + lines[i].strip(); i += 1
                else: break
            yield (kind, items); continue
        para = []
        while i < n and lines[i].strip() and not lines[i].startswith(('#', '|', '>', '```')) and lines[i].strip() != '---' and not re.match(r'\s*([-*]|\d+\.)\s+', lines[i]):
            para.append(lines[i].strip()); i += 1
        yield ('p', ' '.join(para))

def render(b):
    k = b[0]
    if k == 'h': return '<h%d>%s</h%d>' % (b[1], inline(b[2]), b[1])
    if k == 'p': return '<p>%s</p>' % inline(b[1])
    if k == 'hr': return '<hr/>'
    if k == 'pre': return '<pre>%s</pre>' % html.escape(b[1], quote=False)
    if k == 'bq': return '<blockquote><p>%s</p></blockquote>' % inline(b[1])
    if k in ('ul', 'ol'): return '<%s>%s</%s>' % (k, ''.join('<li>%s</li>' % inline(x) for x in b[1]), k)
    if k == 'table':
        head = ''.join('<th>%s</th>' % inline(c) for c in b[1])
        body = ''.join('<tr>%s</tr>' % ''.join('<td>%s</td>' % inline(c) for c in r) for r in b[2])
        return '<table><thead><tr>%s</tr></thead><tbody>%s</tbody></table>' % (head, body)

CSS = "body{font-family:Georgia,serif;line-height:1.5;margin:1em}h1{font-size:1.5em}h2{font-size:1.25em;margin-top:1.5em}table{border-collapse:collapse}td,th{border:1px solid #888;padding:.3em .5em;vertical-align:top}code{font-family:Menlo,monospace;font-size:.9em}pre{font-family:Menlo,monospace;font-size:.8em;white-space:pre-wrap;border:1px solid #bbb;padding:.5em}blockquote{margin:1em 1.5em;font-style:italic}"

def xhtml(title, body):
    return ('<?xml version="1.0" encoding="utf-8"?>\n<html xmlns="http://www.w3.org/1999/xhtml" xmlns:epub="http://www.idpf.org/2007/ops">'
            '<head><title>%s</title><link rel="stylesheet" type="text/css" href="style.css"/></head><body>%s</body></html>' % (html.escape(title), body))

def main(path):
    lines = open(path, encoding='utf-8').read().split('\n')
    title = next((l[2:].strip() for l in lines if l.startswith('# ')), os.path.basename(path))
    chapters, cur, cur_title = [], [], title
    for b in blocks(lines):
        if b[0] == 'h' and b[1] == 2:
            if cur: chapters.append((cur_title, cur))
            cur, cur_title = [b], b[2]
        elif b[0] == 'h' and b[1] == 1:
            cur.append(b)
        else:
            cur.append(b)
    if cur: chapters.append((cur_title, cur))
    out = os.path.splitext(path)[0] + '.epub'; uid = 'urn:uuid:' + str(uuid.uuid5(uuid.NAMESPACE_URL, os.path.abspath(path)))
    files = []
    for k, (t, bs) in enumerate(chapters):
        files.append(('ch%02d.xhtml' % k, t, xhtml(t, ''.join(render(b) for b in bs))))
    for name, t, doc in files: ET.fromstring(doc.encode('utf-8'))   # well-formed or refuse
    nav = xhtml('Contents', '<nav epub:type="toc" id="toc"><h1>Contents</h1><ol>%s</ol></nav>' % ''.join('<li><a href="%s">%s</a></li>' % (n, html.escape(t)) for n, t, _ in files))
    manifest = ''.join('<item id="%s" href="%s" media-type="application/xhtml+xml"/>' % (n[:-6], n) for n, _, _ in files)
    spine = ''.join('<itemref idref="%s"/>' % n[:-6] for n, _, _ in files)
    opf = ('<?xml version="1.0" encoding="utf-8"?><package xmlns="http://www.idpf.org/2007/opf" version="3.0" unique-identifier="uid">'
           '<metadata xmlns:dc="http://purl.org/dc/elements/1.1/"><dc:identifier id="uid">%s</dc:identifier><dc:title>%s</dc:title><dc:language>en</dc:language>'
           '<meta property="dcterms:modified">%s</meta></metadata><manifest><item id="nav" href="nav.xhtml" media-type="application/xhtml+xml" properties="nav"/>'
           '<item id="css" href="style.css" media-type="text/css"/>%s</manifest><spine>%s</spine></package>'
           % (uid, html.escape(title), time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime()), manifest, spine))
    container = '<?xml version="1.0" encoding="utf-8"?><container version="1.0" xmlns="urn:oasis:names:tc:opendocument:xmlns:container"><rootfiles><rootfile full-path="OEBPS/content.opf" media-type="application/oebps-package+xml"/></rootfiles></container>'
    with zipfile.ZipFile(out, 'w') as z:
        z.writestr('mimetype', 'application/epub+zip', zipfile.ZIP_STORED)
        z.writestr('META-INF/container.xml', container, zipfile.ZIP_DEFLATED)
        z.writestr('OEBPS/content.opf', opf, zipfile.ZIP_DEFLATED)
        z.writestr('OEBPS/nav.xhtml', nav, zipfile.ZIP_DEFLATED)
        z.writestr('OEBPS/style.css', CSS, zipfile.ZIP_DEFLATED)
        for n, _, doc in files: z.writestr('OEBPS/' + n, doc, zipfile.ZIP_DEFLATED)
    print('wrote %s — %d chapters, %d bytes' % (out, len(files), os.path.getsize(out)))

if __name__ == '__main__':
    main(sys.argv[1])

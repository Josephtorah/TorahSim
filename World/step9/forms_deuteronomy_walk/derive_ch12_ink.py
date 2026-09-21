import os as _os
_ROOT = _os.path.normpath(_os.path.join(_os.path.dirname(_os.path.abspath(__file__)), '..', '..', '..'))   # THE PORTABLE REPO (2026-09-15): the repo root from this file's own place
#!/usr/bin/env python3
# THE DEUTERONOMY WALK sitting 10 — CHAPTER 12 (2026-09-20): ch12_ink.py ASSEMBLED — the constants (ch12_ink_head.py) + the GENERIC helper blocks of the forms'
# ch11_ink.py found by CONTENT MARKERS (never by line number: the Sifrei/Onkelos readers, the heads, the citation regex, the pointing test, the kin counter,
# the Onkelos row reader, the DB and store helpers with the chapter number substituted) + the chapter's own asserts (ch12_ink_body.py, _b, _c). Sitting 9's
# form (derive_ch11_ink.py), so a helper cannot drift from the form.
import os, re, subprocess
ROOT = _ROOT
SP = os.path.dirname(os.path.abspath(__file__))
src = open(f'{ROOT}/World/step9/forms_deuteronomy_walk/ch11_ink.py', encoding='utf-8').read()
def block(start, end_line):
    i = src.index(start); j = src.index(end_line, i); j = src.index('\n', j) + 1
    return src[i:j]
def line(start):
    i = src.index(start); j = src.index('\n', i) + 1
    return src[i:j]
H1 = block('def clean(s): return re.sub', 'def head(p): return heads[p]')
H2 = line('def he_cites(t):'); H3 = line('def has_points(s):'); H4 = line('def kinrows(f, pat):')
H5 = block('def onk_ev(c, v):', '    return clean(onk[c - 1][e - 1]), clean(onk_he[c - 1][e - 1])')
H6 = block('rows = db.execute("SELECT v.book, v.chapter, v.verse, w.he, w.morph, w.lemma, w.wtype', 'STORE_MISMATCH = ')
for old, new in (("def W11(v): return words('Deut', 11, v)", "def W12(v): return words('Deut', 12, v)"), ("AND v.chapter = 11 ORDER BY", "AND v.chapter = 12 ORDER BY"), ("AND v.chapter=11 GROUP BY", "AND v.chapter=12 GROUP BY")):
    assert H6.count(old) == 1, old; H6 = H6.replace(old, new)
assert 'W11' not in H6 and 'chapter = 11' not in H6 and 'chapter=11' not in H6
assert '_ROOT' not in H1 + H2 + H3 + H4 + H5 + H6 and 'Deut 11' not in H1 + H2 + H3 + H4 + H5 + H6
head = open(f'{SP}/ch12_ink_head.py', encoding='utf-8').read()
body = ''.join(open(f'{SP}/{f}', encoding='utf-8').read() for f in ('ch12_ink_body.py', 'ch12_ink_body_b.py', 'ch12_ink_body_c.py'))
KIN = "import difflib\ndef SH(a, b_): return sum(s for _, _, s in difflib.SequenceMatcher(a=words(*a), b=words(*b_)).get_matching_blocks())\nD12 = lambda v: ('Deut', 12, v)\n"
out = head + '# ---- THE HELPERS (ch11_ink.py\'s, copied by content markers) ----\n' + H1 + H2 + H3 + H4 + H5 + '# ---- THE INK\'S HELPERS, THE DB AND THE STORE (ch11_ink.py\'s, the chapter substituted) ----\n' + H6 + KIN + body
open(f'{SP}/ch12_ink.py', 'w', encoding='utf-8').write(out)
import ast; ast.parse(out); print('ch12_ink.py assembled:', len(out), 'bytes; helper blocks', [len(x) for x in (H1, H2, H3, H4, H5, H6)])

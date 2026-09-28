import os as _os
_ROOT = _os.path.normpath(_os.path.join(_os.path.dirname(_os.path.abspath(__file__)), '..', '..', '..'))   # THE PORTABLE REPO (2026-09-15): the repo root from this file's own place
#!/usr/bin/env python3
# THE DEUTERONOMY WALK sitting 20 — CHAPTER 32, THE SONG (LEAN, 2026-09-27): ch32_ink.py ASSEMBLED — the constants (ch32_ink_head.py) + the GENERIC helper blocks of
# the forms' ch22_ink.py found by CONTENT MARKERS (derive_ch29_ink.py's form) + THE KIN BY COMPUTATION keyed by (chapter, verse) + the sitting's own asserts
# (ch32_ink_body*.py, whichever exist). RUN FROM THE REPO ROOT.
import os, re, subprocess
ROOT = _ROOT
SP = os.path.dirname(os.path.abspath(__file__))
src = open(f'{ROOT}/World/step9/forms_deuteronomy_walk/ch22_ink.py', encoding='utf-8').read()
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
for old, new in (("def W22(v): return words('Deut', 22, v)\ndef W23(v): return words('Deut', 23, v)\ndef W24(v): return words('Deut', 24, v)\ndef W25(v): return words('Deut', 25, v)\ndef W(c, v): return words('Deut', c, v)", "def W32(v): return words('Deut', 32, v)\ndef W(c, v): return words('Deut', c, v)"), ("AND v.chapter IN (22, 23, 24, 25) ORDER BY", "AND v.chapter IN (32) ORDER BY"), ("AND v.chapter IN (22, 23, 24, 25) GROUP BY", "AND v.chapter IN (32) GROUP BY")):
    assert H6.count(old) == 1, old; H6 = H6.replace(old, new)
assert 'W22' not in H6 and 'W25' not in H6 and '(22, 23, 24, 25)' not in H6
HH = H1 + H2 + H3 + H4 + H5 + H6
assert '_ROOT' not in HH and 'Deut 22' not in HH and 'Deut 25' not in HH, [m for m in re.findall(r'.{30}(?:_ROOT|Deut 22|Deut 25).{30}', HH)]
head = open(f'{SP}/ch32_ink_head.py', encoding='utf-8').read()
bodies = [f for f in ('ch32_ink_body.py', 'ch32_ink_body_b.py', 'ch32_ink_body_c.py', 'ch32_ink_body_d.py') if os.path.exists(f'{SP}/{f}')]
body = ''.join(open(f'{SP}/{f}', encoding='utf-8').read() for f in bodies)
KIN = ("import difflib\ndef SH(a, b_): return sum(s for _, _, s in difflib.SequenceMatcher(a=words(*a), b=words(*b_)).get_matching_blocks())\nDV = lambda c, v: ('Deut', c, v)\n"
       "# THE KIN FOUND BY COMPUTATION (the measure's A section, recomputed here so the asserts read the same instrument): the shared distinct tokens outside the stop list, the top eight, the three closest re-scored in order — keyed by (chapter, verse)\n"
       "STOP = set('את ואת אשר כל וכל על ועל אל ואל לא ולא כי אם יהוה אלהיך אלהיכם לך לכם בו שם שמה גם מן ממך עד הוא היא אתם אתה אנכי אני לו לה בכל כאשר כן הימים היום אלה האלה בארץ הארץ אשר ואם או פן ופן ואת זה וזה הם המה'.split())\n"
       "ORD = {k: i for i, k in enumerate(by)}\nTOK = {k: set(words(*k)) - STOP for k in by}\nKINC = {}\n"
       "for _c, _v in SPAN:\n    _me = DV(_c, _v); _t = TOK[_me]\n    _sc = sorted(((len(_t & TOK[k]), k) for k in by if k != _me and len(_t & TOK[k]) >= 2), key=lambda x: (-x[0], ORD[x[1]]))[:8]\n    KINC[(_c, _v)] = [(f'{k[0]} {k[1]}:{k[2]}', n, SH(_me, k) if i < 3 else None) for i, (n, k) in enumerate(_sc)]\n")
out = head + '# ---- THE HELPERS (ch22_ink.py\'s, copied by content markers) ----\n' + H1 + H2 + H3 + H4 + H5 + '# ---- THE INK\'S HELPERS, THE DB AND THE STORE (ch22_ink.py\'s, the chapter substituted) ----\n' + H6 + KIN + body
open(f'{SP}/ch32_ink.py', 'w', encoding='utf-8').write(out)
import ast; ast.parse(out); print('ch32_ink.py assembled:', len(out), 'bytes; helper blocks', [len(x) for x in (H1, H2, H3, H4, H5, H6)], '; bodies', bodies)

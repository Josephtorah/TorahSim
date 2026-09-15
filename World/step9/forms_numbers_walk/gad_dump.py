import os as _os
_ROOT = _os.path.normpath(_os.path.join(_os.path.dirname(_os.path.abspath(__file__)), '..', '..', '..'))   # THE PORTABLE REPO (2026-09-15): the repo root from this file's own place
#!/usr/bin/env python3
# THE NUMBERS WALK, sitting 12 — GAD AND REUBEN, Numbers 32:1-42 (2026-09-12; the owner: "Go" after the #148 rereads, on the ruling READ THEN
# COMPILE): THE FIRST MEASUREMENT PASS — the shelf's heads by position (the Sifrei's piskaot on 32: NONE expected, the shelf silent from 31:25
# to 35:8 — every row of the whole export scanned for a citation of chapter 32, the "found by position" clause), the draft's span
# (num_32_gad_reuben 32:1-42; the portion Matot's third chapter; the next draft opens at 33:1), the prior-read scan, the engine's parser on every
# verse of the chapter, and the DUMPS the reading runs on (Onkelos EN + HE per verse; the pointed Hebrew with the store's own glosses). Nothing typed.
import json, os, re, html, sqlite3, sys, io, contextlib, unicodedata, glob
from collections import Counter
ROOT = _ROOT
SP = os.path.dirname(os.path.abspath(__file__))
C = 32
def clean(s): return re.sub(r'<[^>]+>', '', html.unescape(s))
sif = json.load(open(f'{ROOT}/Data/sefaria_export/Sifrei_Bamidbar/en.json'))['text']
sif_he = json.load(open(f'{ROOT}/Data/sefaria_export/Sifrei_Bamidbar/he.json'))['text']
onk = json.load(open(f'{ROOT}/Data/sefaria_export/Onkelos_Numbers/en.json'))['text']
onk_he = json.load(open(f'{ROOT}/Data/sefaria_export/Onkelos_Numbers/he.json'))['text']
heads = {}
for p, rows in enumerate(sif, 1):
    if not rows: continue
    m = re.search(r'\((Bamidbar|Devarim)\.? (\d+):(\d+)', clean(rows[0])[:60])
    heads[p] = (m.group(1), int(m.group(2)), int(m.group(3))) if m else None
print('HEADS 155-161:', {p: heads.get(p) for p in range(155, 162)})
print('TOTAL piskaot', len(sif), 'last non-empty', max(p for p, r in enumerate(sif, 1) if r))
P = sorted(p for p, h in heads.items() if h and h[0] == 'Bamidbar' and h[1] == C)
print(f'PISKAOT on {C}:', P)
# THE "FOUND BY POSITION" CLAUSE: every row of the whole export scanned for a citation of chapter 32 (EN) and for a quotation of a 32-only phrase (HE)
CITING = [(p, r, re.findall(r'\(Bamidbar\.? 32:(\d+)', clean(row))) for p, rows in enumerate(sif, 1) for r, row in enumerate(rows, 1) if re.search(r'\(Bamidbar\.? 32:\d+', clean(row))]
print('ROWS CITING Bamidbar 32 anywhere (EN):', CITING)
HE32 = [(p, r) for p, rows in enumerate(sif_he, 1) for r, row in enumerate(rows, 1) if re.search(r'במדבר ל"?ב\b|במדבר לב\b', clean(row))]
print('ROWS citing במדבר לב (HE):', HE32)
print('ONK_LEN 31-34:', {c: (len(onk[c - 1]), len(onk_he[c - 1])) for c in (31, 32, 33, 34)})
def plain(w): return ''.join(c for c in w if c != '/' and not (0x0591 <= ord(c) <= 0x05C7))
def unit_text(uid): return open(f'{ROOT}/logic/units/{uid}.yaml', encoding='utf-8').read()
def steps(uid): return sorted({(int(a), int(b)) for a, b in re.findall(r'STEP_Nm_(\d+)_(\d+)', unit_text(uid))})
NEXT = sorted(os.path.basename(f)[:-5] for f in glob.glob(f'{ROOT}/logic/units/num_33_*.yaml'))
print('num_33 drafts:', NEXT)
for uid in ['num_31_midian', 'num_32_gad_reuben'] + NEXT:
    st = steps(uid); print(uid, 'status draft' if 'status: draft' in unit_text(uid) else ('FROZEN' if 'status: frozen' in unit_text(uid) else 'NO STATUS'), st[0], st[-1], len(st), 'operators:' in unit_text(uid))
db = sqlite3.connect(f'file:{ROOT}/Data/tanakh.sqlite?mode=ro', uri=True)
VC = dict(db.execute("SELECT chapter, COUNT(*) FROM verses WHERE book='Num' GROUP BY chapter").fetchall())
print('VC 31-33:', {c: VC[c] for c in (31, 32, 33)})
# THE PRIOR READS
TRI = f'{ROOT}/logic/oral_triage'
LED = {f: open(f'{TRI}/{f}', encoding='utf-8').read() for f in os.listdir(TRI) if f.endswith('.md') and os.path.isfile(f'{TRI}/{f}')}
print(f'prior Onkelos Num {C} rows:', sorted(f for f, t in LED.items() if re.search(rf'^- Onkelos Num {C}:\d', t, re.M)))
print(f'ledgers naming Num {C} at all:', sorted((f, len(re.findall(rf'Num(?:bers)? {C}:\d+', t))) for f, t in LED.items() if re.search(rf'Num(?:bers)? {C}:\d+', t)))
print('ledgers naming Deut 3:12-20 / Josh 1:12-18 / Josh 22 / Josh 13:', sorted((f, sorted(set(re.findall(r'(Deut(?:eronomy)? 3:1[2-9]|Deut(?:eronomy)? 3:20|Josh(?:ua)? 1:1[2-8]|Josh(?:ua)? 22:\d+|Josh(?:ua)? 13:\d+)', t)))) for f, t in LED.items() if re.search(r'Deut(?:eronomy)? 3:1[2-9]|Josh(?:ua)? 1:1[2-8]|Josh(?:ua)? 22:\d+|Josh(?:ua)? 13:\d+', t)))
# THE PARSER on every verse of 32
sys.path.insert(0, f'{ROOT}/World/step9')
with contextlib.redirect_stdout(io.StringIO()):
    import cold_run_sequence as CS
def N(b, c, v): return CS.ink_numbers(CS.verse_words(b, c, v))
def O(b, c, v): return CS.ink_ordinals(CS.verse_words(b, c, v))
rows = db.execute("SELECT v.chapter, v.verse, w.he, w.morph FROM words w JOIN verses v ON w.verse_id=v.id WHERE v.book='Num' AND v.chapter IN (32, 33) ORDER BY v.id, w.idx").fetchall()
by = {}
for c, v, he, m in rows: by.setdefault((c, v), []).append((plain(he), m, he))
print('---- THE PARSER (numbers | ordinals | the verse_words tokens with marks)')
for v in range(1, VC[C] + 1):
    vw = CS.verse_words('Num', C, v)
    marked = [t for t in vw if t[-1] in '#~^%@|*']
    print(f'  {C}:{v:<3} N {N("Num", C, v)!s:<34} O {O("Num", C, v)!s:<10} marked {marked}')
print('  33:1', N('Num', 33, 1), O('Num', 33, 1))
# THE REGISTER: narrative verbs (the wayyiqtol, the narrative past form, HC/V.w) per verse
print('---- THE REGISTER (verbs with the narrative form per verse)')
for v in range(1, VC[C] + 1):
    reg = [(x, m) for x, m, _ in by[(C, v)] if m and re.search(r'V.w', m)]
    print(f'  {C}:{v:<3} {reg}')
# THE STORE'S GLOSSES
store = sqlite3.connect(f'file:{ROOT}/torah_grok.SNAPSHOT-main-51801ca.sqlite?mode=ro', uri=True)
SG = {}
for c, v, hp, g in store.execute("SELECT v.chapter, v.verse, w.he_plain, w.gloss FROM words w JOIN verses v ON w.verse_id=v.id WHERE v.book='Num' AND v.chapter = ? ORDER BY v.id, w.idx", (C,)):
    SG.setdefault((c, v), []).append((hp.replace('/', ''), g))
print('---- THE DUMPS: per verse — the Hebrew (consonants) | the pointed with accents | the store\'s glosses | Onkelos EN | Onkelos HE (consonants)')
def accents(w): return [unicodedata.name(c).replace('HEBREW ACCENT ', '') for c in w if 0x0591 <= ord(c) <= 0x05AE]
for v in range(1, VC[C] + 1):
    he = ' '.join(x for x, _, _ in by[(C, v)])
    acc = ' '.join(f'{x}[{"/".join(accents(raw))}]' for x, _, raw in by[(C, v)])
    morph = ' '.join(f'{x}:{m}' for x, m, _ in by[(C, v)])
    gl = ' | '.join(f'{hp}={g}' for hp, g in SG.get((C, v), []))
    print(f'\n== Num {C}:{v}\n  HE  {he}\n  ACC {acc}\n  MOR {morph}\n  GL  {gl}\n  ONK {clean(onk[C - 1][v - 1])}\n  ARM {plain(clean(onk_he[C - 1][v - 1]))}')
print('\n---- THE SIFREI ROWS on 32 (none expected):', P)
for p in P:
    for r, row in enumerate(sif[p - 1], 1):
        print(f'\n## Sifrei {p}:{r}\n{clean(row)}\n-- HE: {clean(sif_he[p - 1][r - 1])}')

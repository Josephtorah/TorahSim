import os as _os
_ROOT = _os.path.normpath(_os.path.join(_os.path.dirname(_os.path.abspath(__file__)), '..', '..', '..'))   # THE PORTABLE REPO (2026-09-15): the repo root from this file's own place
#!/usr/bin/env python3
# THE NUMBERS WALK, sitting 10 — THE VOWS, Numbers 30:1-17 (2026-09-12; the owner: "Go" after the #141 rereads, on the ruling READ THEN
# COMPILE): THE FIRST MEASUREMENT PASS — the shelf's heads by position (the Sifrei's piskaot on 30), the draft's span (num_30_vows 30:1-17;
# 30:1 the portion Pinchas's last verse, the calendar's closer, read with this draft — the draft's-grain rule; the next draft num_31_midian
# opens at 31:1), the prior-read scan, the engine's parser on every verse of the chapter (no cardinal expected — measured), and the DUMPS the
# reading runs on (Onkelos EN + HE per verse; the Sifrei's rows; the pointed Hebrew with the store's own glosses). Nothing typed.
import json, os, re, html, sqlite3, sys, io, contextlib, unicodedata
from collections import Counter
ROOT = _ROOT
SP = os.path.dirname(os.path.abspath(__file__))
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
print('HEADS 150-160:', {p: heads.get(p) for p in range(150, 161)})
print('TOTAL piskaot', len(sif), 'last non-empty', max(p for p, r in enumerate(sif, 1) if r))
P = sorted(p for p, h in heads.items() if h and h[0] == 'Bamidbar' and h[1] == 30)
print('PISKAOT on 30:', P, 'rows', {p: (len(sif[p - 1]), len(sif_he[p - 1])) for p in P})
for p in P:
    for r, row in enumerate(sif[p - 1], 1):
        cites = sorted(set(re.findall(r'(Bamidbar|Devarim|Bereshit|Shemot|Vayikra|Yehoshua|Ibid\.?) ?(\d+):(\d+)', clean(row))))
        print(f'    piska {p} row {r}: {len(clean(row))} chars / HE {len(clean(sif_he[p - 1][r - 1]))}; cites {cites[:14]}; opens {clean(row)[:100]!r}')
print('ONK_LEN 29-32:', {c: (len(onk[c - 1]), len(onk_he[c - 1])) for c in (29, 30, 31, 32)})
def plain(w): return ''.join(c for c in w if c != '/' and not (0x0591 <= ord(c) <= 0x05C7))
def unit_text(uid): return open(f'{ROOT}/logic/units/{uid}.yaml', encoding='utf-8').read()
def steps(uid): return sorted({(int(a), int(b)) for a, b in re.findall(r'STEP_Nm_(\d+)_(\d+)', unit_text(uid))})
for uid in ('num_29_fall_festivals', 'num_30_vows', 'num_31_midian'):
    st = steps(uid); print(uid, 'status draft' if 'status: draft' in unit_text(uid) else ('FROZEN' if 'status: frozen' in unit_text(uid) else 'NO STATUS'), st[0], st[-1], len(st), 'operators:' in unit_text(uid))
db = sqlite3.connect(f'file:{ROOT}/Data/tanakh.sqlite?mode=ro', uri=True)
VC = dict(db.execute("SELECT chapter, COUNT(*) FROM verses WHERE book='Num' GROUP BY chapter").fetchall())
print('VC 29-31:', {c: VC[c] for c in (29, 30, 31)})
# THE PRIOR READS
TRI = f'{ROOT}/logic/oral_triage'
LED = {f: open(f'{TRI}/{f}', encoding='utf-8').read() for f in os.listdir(TRI) if f.endswith('.md') and os.path.isfile(f'{TRI}/{f}')}
print('prior Onkelos Num 30 rows:', sorted(f for f, t in LED.items() if re.search(r'^- Onkelos Num 30:\d', t, re.M)))
print('prior Sifrei rows 153-156:', sorted((f, sorted(set(re.findall(r'Sifrei (?:Bamidbar )?(15[3-6]):\d', t)))) for f, t in LED.items() if re.search(r'Sifrei (?:Bamidbar )?15[3-6]:\d', t)))
print('ledgers naming Num 30 at all:', sorted((f, len(re.findall(r'Num(?:bers)? 30:\d+', t))) for f, t in LED.items() if re.search(r'Num(?:bers)? 30:\d+', t)))
# THE PARSER on every verse of 30
sys.path.insert(0, f'{ROOT}/World/step9')
with contextlib.redirect_stdout(io.StringIO()):
    import cold_run_sequence as CS
def N(b, c, v): return CS.ink_numbers(CS.verse_words(b, c, v))
def O(b, c, v): return CS.ink_ordinals(CS.verse_words(b, c, v))
rows = db.execute("SELECT v.chapter, v.verse, w.he, w.morph FROM words w JOIN verses v ON w.verse_id=v.id WHERE v.book='Num' AND v.chapter IN (30, 31) ORDER BY v.id, w.idx").fetchall()
by = {}
for c, v, he, m in rows: by.setdefault((c, v), []).append((plain(he), m, he))
print('---- THE PARSER (numbers | ordinals | the verse_words tokens with marks)')
for v in range(1, VC[30] + 1):
    vw = CS.verse_words('Num', 30, v)
    marked = [t for t in vw if t[-1] in '#~^%@|*']
    print(f'  30:{v:<3} N {N("Num", 30, v)!s:<20} O {O("Num", 30, v)!s:<10} marked {marked}')
print('  31:1', N('Num', 31, 1), O('Num', 31, 1))
# THE REGISTER: narrative verbs (wayyiqtol, HC/V.w) per verse
print('---- THE REGISTER (verbs with the narrative form per verse)')
for v in range(1, VC[30] + 1):
    reg = [(x, m) for x, m, _ in by[(30, v)] if m and re.search(r'V.w', m)]
    print(f'  30:{v:<3} {reg}')
# THE STORE'S GLOSSES
store = sqlite3.connect(f'file:{ROOT}/torah_grok.SNAPSHOT-main-51801ca.sqlite?mode=ro', uri=True)
SG = {}
for c, v, hp, g in store.execute("SELECT v.chapter, v.verse, w.he_plain, w.gloss FROM words w JOIN verses v ON w.verse_id=v.id WHERE v.book='Num' AND v.chapter = 30 ORDER BY v.id, w.idx"):
    SG.setdefault((c, v), []).append((hp.replace('/', ''), g))
print('---- THE DUMPS: per verse — the Hebrew (consonants) | the pointed with accents | the store\'s glosses | Onkelos EN | Onkelos HE (consonants)')
def accents(w): return [unicodedata.name(c).replace('HEBREW ACCENT ', '') for c in w if 0x0591 <= ord(c) <= 0x05AE]
for v in range(1, VC[30] + 1):
    he = ' '.join(x for x, _, _ in by[(30, v)])
    acc = ' '.join(f'{x}[{"/".join(accents(raw))}]' for x, _, raw in by[(30, v)])
    morph = ' '.join(f'{x}:{m}' for x, m, _ in by[(30, v)])
    gl = ' | '.join(f'{hp}={g}' for hp, g in SG.get((30, v), []))
    print(f'\n== Num 30:{v}\n  HE  {he}\n  ACC {acc}\n  MOR {morph}\n  GL  {gl}\n  ONK {clean(onk[29][v - 1])}\n  ARM {plain(clean(onk_he[29][v - 1]))}')
print('\n---- THE SIFREI ROWS (EN, then HE consonants)')
for p in P:
    for r, row in enumerate(sif[p - 1], 1):
        print(f'\n## Sifrei {p}:{r}\n{clean(row)}\n-- HE: {clean(sif_he[p - 1][r - 1])}')

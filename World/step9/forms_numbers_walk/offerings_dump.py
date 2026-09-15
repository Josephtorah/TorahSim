import os as _os
_ROOT = _os.path.normpath(_os.path.join(_os.path.dirname(_os.path.abspath(__file__)), '..', '..', '..'))   # THE PORTABLE REPO (2026-09-15): the repo root from this file's own place
#!/usr/bin/env python3
# THE NUMBERS WALK, sitting 9 — THE OFFERINGS CALENDAR, Numbers 28:1-29:39 (2026-09-11; the owner: "I agree continue" after the register
# gate, on the ruling READ THEN COMPILE): THE FIRST MEASUREMENT PASS — the shelf's heads by position (the Sifrei's piskaot on 28-29), the
# three drafts' spans (num_28_daily_shabbat_rosh 28:1-15, num_28_pesach_shavuot 28:16-31, num_29_fall_festivals 29:1-39; the portion's
# last verse 30:1 opens the next draft, num_30_vows, and is read with it — the draft's-grain rule), the prior-read scan, the engine's
# parser on every number verse of the two chapters (the libation table's fractions and tenths, the counts of bulls, rams, lambs, goats,
# the ordinals of the dates), and the DUMPS the reading runs on (Onkelos EN + HE per verse; the Sifrei's rows; the pointed Hebrew with the
# store's own glosses). Nothing typed.
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
print('HEADS 140-156:', {p: heads.get(p) for p in range(140, 157)})
P = sorted(p for p, h in heads.items() if h and h[0] == 'Bamidbar' and h[1] in (28, 29))
print('PISKAOT on 28-29:', P, 'rows', {p: (len(sif[p - 1]), len(sif_he[p - 1])) for p in P})
for p in P:
    for r, row in enumerate(sif[p - 1], 1):
        cites = sorted(set(re.findall(r'(Bamidbar|Devarim|Bereshit|Shemot|Vayikra|Yehoshua|Ibid\.?) ?(\d+):(\d+)', clean(row))))
        print(f'    piska {p} row {r}: {len(clean(row))} chars; cites {cites[:14]}; opens {clean(row)[:100]!r}')
print('ONK_LEN 27-30:', {c: (len(onk[c - 1]), len(onk_he[c - 1])) for c in (27, 28, 29, 30)})
def plain(w): return ''.join(c for c in w if c != '/' and not (0x0591 <= ord(c) <= 0x05C7))
def unit_text(uid): return open(f'{ROOT}/logic/units/{uid}.yaml', encoding='utf-8').read()
def steps(uid): return sorted({(int(a), int(b)) for a, b in re.findall(r'STEP_Nm_(\d+)_(\d+)', unit_text(uid))})
for uid in ('num_27_zelophehad_joshua', 'num_28_daily_shabbat_rosh', 'num_28_pesach_shavuot', 'num_29_fall_festivals', 'num_30_vows'):
    st = steps(uid); print(uid, 'status draft' if 'status: draft' in unit_text(uid) else ('FROZEN' if 'status: frozen' in unit_text(uid) else 'NO STATUS'), st[0], st[-1], len(st), 'operators:' in unit_text(uid))
db = sqlite3.connect(f'file:{ROOT}/Data/tanakh.sqlite?mode=ro', uri=True)
VC = dict(db.execute("SELECT chapter, COUNT(*) FROM verses WHERE book='Num' GROUP BY chapter").fetchall())
print('VC 27-30:', {c: VC[c] for c in (27, 28, 29, 30)})
# THE PRIOR READS
TRI = f'{ROOT}/logic/oral_triage'
LED = {f: open(f'{TRI}/{f}', encoding='utf-8').read() for f in os.listdir(TRI) if f.endswith('.md') and os.path.isfile(f'{TRI}/{f}')}
print('prior Onkelos Num 28/29 rows:', sorted(f for f, t in LED.items() if re.search(r'^- Onkelos Num 2[89]:\d', t, re.M)))
print('prior Sifrei rows 142-152:', sorted((f, sorted(set(re.findall(r'Sifrei (?:Bamidbar )?(1[45]\d):\d', t)))) for f, t in LED.items() if re.search(r'Sifrei (?:Bamidbar )?1(4[2-9]|5[0-2]):\d', t)))
print('ledgers naming Num 28/29 at all:', sorted((f, len(re.findall(r'Num(?:bers)? 2[89]:\d+', t))) for f, t in LED.items() if re.search(r'Num(?:bers)? 2[89]:\d+', t)))
# THE PARSER on every verse of 28-29
sys.path.insert(0, f'{ROOT}/World/step9')
with contextlib.redirect_stdout(io.StringIO()):
    import cold_run_sequence as CS
def N(b, c, v): return CS.ink_numbers(CS.verse_words(b, c, v))
def O(b, c, v): return CS.ink_ordinals(CS.verse_words(b, c, v))
rows = db.execute("SELECT v.chapter, v.verse, w.he, w.morph FROM words w JOIN verses v ON w.verse_id=v.id WHERE v.book='Num' AND v.chapter IN (28,29,30) ORDER BY v.id, w.idx").fetchall()
by = {}
for c, v, he, m in rows: by.setdefault((c, v), []).append((plain(he), m))
print('---- THE PARSER (numbers | ordinals | the verse_words tokens with marks)')
for c in (28, 29):
    for v in range(1, VC[c] + 1):
        vw = CS.verse_words('Num', c, v)
        marked = [t for t in vw if t[-1] in '#~^%@|*']
        print(f'  {c}:{v:<3} N {N("Num", c, v)!s:<40} O {O("Num", c, v)!s:<10} marked {marked}')
print('  30:1', N('Num', 30, 1), O('Num', 30, 1))
# THE STORE'S GLOSSES
store = sqlite3.connect(f'file:{ROOT}/torah_grok.SNAPSHOT-main-51801ca.sqlite?mode=ro', uri=True)
SG = {}
for c, v, hp, g in store.execute("SELECT v.chapter, v.verse, w.he_plain, w.gloss FROM words w JOIN verses v ON w.verse_id=v.id WHERE v.book='Num' AND v.chapter IN (28, 29) ORDER BY v.id, w.idx"):
    SG.setdefault((c, v), []).append((hp.replace('/', ''), g))
print('---- THE DUMPS: per verse — the Hebrew (consonants) | the store\'s glosses | Onkelos EN | Onkelos HE (consonants)')
for c in (28, 29):
    for v in range(1, VC[c] + 1):
        he = ' '.join(x for x, _ in by[(c, v)])
        gl = ' | '.join(f'{hp}={g}' for hp, g in SG.get((c, v), []))
        print(f'\n== Num {c}:{v}\n  HE  {he}\n  GL  {gl}\n  ONK {clean(onk[c - 1][v - 1])}\n  ARM {plain(clean(onk_he[c - 1][v - 1]))}')
print('\n---- THE SIFREI ROWS (EN, then HE consonants)')
for p in P:
    for r, row in enumerate(sif[p - 1], 1):
        print(f'\n## Sifrei {p}:{r}\n{clean(row)}\n-- HE: {clean(sif_he[p - 1][r - 1])}')

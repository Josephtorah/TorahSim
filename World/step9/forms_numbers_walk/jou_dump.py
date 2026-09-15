import os as _os
_ROOT = _os.path.normpath(_os.path.join(_os.path.dirname(_os.path.abspath(__file__)), '..', '..', '..'))   # THE PORTABLE REPO (2026-09-15): the repo root from this file's own place
#!/usr/bin/env python3
# THE NUMBERS WALK, sitting 13 — THE JOURNEYS, Numbers 33:1-56 (2026-09-12; the owner: "Go" after the #151 rereads, on the ruling READ THEN
# COMPILE): THE FIRST MEASUREMENT PASS — the shelf's heads by position (the Sifrei's piskaot on 33: NONE expected, the shelf silent from 31:25
# to 35:8 — every row of the whole export scanned for a citation of chapter 33, the "found by position" clause), the draft's span
# (num_33_journeys 33:1-56; the portion Masei's first chapter; the next draft opens at 34:1), the prior-read scan, the engine's parser on every
# verse of the chapter (THE STATIONS' NUMBERS: 33:3's fifteenth, 33:8's three days, 33:9's twelve springs and seventy palms, 33:38's date —
# the tape's marker at 20:28 already reads it — 33:39's hundred and twenty-three), the station pairs by the two verbs, and the DUMPS the reading
# runs on (Onkelos EN + HE per verse; the pointed Hebrew with the store's own glosses). Nothing typed. Sitting 12's form (gad_dump.py).
import json, os, re, html, sqlite3, sys, io, contextlib, unicodedata, glob
from collections import Counter
ROOT = _ROOT
SP = os.path.dirname(os.path.abspath(__file__))
C = 33
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
# THE "FOUND BY POSITION" CLAUSE: every row of the whole export scanned for a citation of chapter 33 (EN) and for a quotation of a 33-only phrase (HE)
CITING = [(p, r, re.findall(rf'\(Bamidbar\.? {C}:(\d+)', clean(row))) for p, rows in enumerate(sif, 1) for r, row in enumerate(rows, 1) if re.search(rf'\(Bamidbar\.? {C}:\d+', clean(row))]
print(f'ROWS CITING Bamidbar {C} anywhere (EN):', CITING)
HE33 = [(p, r) for p, rows in enumerate(sif_he, 1) for r, row in enumerate(rows, 1) if re.search(r'במדבר ל"?ג\b', clean(row))]
print('ROWS citing במדבר לג (HE):', HE33)
# the chapter's own phrases quoted anywhere in the Hebrew rows: "these are the journeys", "and they journeyed from Rameses", "on their gods", "thorns in your eyes", "in the fortieth year"
for ph in ('אלה מסעי', 'ויסעו מרעמסס', 'ובאלהיהם עשה', 'לשכים בעיניכם', 'בשנת הארבעים', 'ממחרת הפסח', 'ביד רמה', 'והורשתם את כל', 'לצנינם', 'קברות התאוה'):
    print(f'  HE rows quoting "{ph}":', [(p, r) for p, rows in enumerate(sif_he, 1) for r, row in enumerate(rows, 1) if ph in clean(row)])
for ph in ('journeys', 'Rameses', 'Ramses', 'Kadesh', 'Mount Hor', 'Hor Hahar', 'fortieth year', 'thorns'):
    print(f'  EN rows with "{ph}":', [(p, r) for p, rows in enumerate(sif, 1) for r, row in enumerate(rows, 1) if ph in clean(row)][:20])
print('ONK_LEN 32-35:', {c: (len(onk[c - 1]), len(onk_he[c - 1])) for c in (32, 33, 34, 35)})
def plain(w): return ''.join(c for c in w if c != '/' and not (0x0591 <= ord(c) <= 0x05C7))
def unit_text(uid): return open(f'{ROOT}/logic/units/{uid}.yaml', encoding='utf-8').read()
def steps(uid): return sorted({(int(a), int(b)) for a, b in re.findall(r'STEP_Nm_(\d+)_(\d+)', unit_text(uid))})
NEXT = sorted(os.path.basename(f)[:-5] for f in glob.glob(f'{ROOT}/logic/units/num_3[3-6]_*.yaml'))
print('num_33-36 drafts:', NEXT)
for uid in ['num_32_gad_reuben'] + NEXT:
    st = steps(uid); print(uid, 'status draft' if 'status: draft' in unit_text(uid) else ('FROZEN' if 'status: frozen' in unit_text(uid) else 'NO STATUS'), st[0], st[-1], len(st), 'operators:' in unit_text(uid))
db = sqlite3.connect(f'file:{ROOT}/Data/tanakh.sqlite?mode=ro', uri=True)
VC = dict(db.execute("SELECT chapter, COUNT(*) FROM verses WHERE book='Num' GROUP BY chapter").fetchall())
print('VC 32-35:', {c: VC[c] for c in (32, 33, 34, 35)})
# THE PRIOR READS
TRI = f'{ROOT}/logic/oral_triage'
LED = {f: open(f'{TRI}/{f}', encoding='utf-8').read() for f in os.listdir(TRI) if f.endswith('.md') and os.path.isfile(f'{TRI}/{f}')}
print(f'prior Onkelos Num {C} rows:', sorted(f for f, t in LED.items() if re.search(rf'^- Onkelos Num {C}:\d', t, re.M)))
print(f'ledgers naming Num {C} at all:', sorted((f, len(re.findall(rf'Num(?:bers)? {C}:\d+', t)), sorted(set(re.findall(rf'Num(?:bers)? {C}:\d+(?:-\d+)?', t)))) for f, t in LED.items() if re.search(rf'Num(?:bers)? {C}:\d+', t)))
KIN = r'Deut(?:eronomy)? 10:[67]\b|Deut(?:eronomy)? 1:[12]\b|Deut(?:eronomy)? 2:8\b|Num(?:bers)? 21:1[0-9]\b|Num(?:bers)? 21:20\b|Exod(?:us)? 15:2[2-7]\b|Exod(?:us)? 17:1\b|Exod(?:us)? 19:[12]\b|Num(?:bers)? 11:3[45]\b|Num(?:bers)? 12:16\b|Num(?:bers)? 20:2[2-9]\b|Num(?:bers)? 22:1\b|Num(?:bers)? 25:1\b|Exod(?:us)? 12:3[78]\b|Exod(?:us)? 13:20\b|Exod(?:us)? 14:2\b|Exod(?:us)? 16:1\b|Num(?:bers)? 10:12\b|Num(?:bers)? 13:26\b|Num(?:bers)? 20:1\b'
print('ledgers naming the stations\' kin verses:', sorted((f, sorted(set(re.findall(KIN, t)))) for f, t in LED.items() if re.search(KIN, t)))
# THE PARSER on every verse of 33
sys.path.insert(0, f'{ROOT}/World/step9')
with contextlib.redirect_stdout(io.StringIO()):
    import cold_run_sequence as CS
def N(b, c, v): return CS.ink_numbers(CS.verse_words(b, c, v))
def O(b, c, v): return CS.ink_ordinals(CS.verse_words(b, c, v))
rows = db.execute("SELECT v.chapter, v.verse, w.he, w.morph FROM words w JOIN verses v ON w.verse_id=v.id WHERE v.book='Num' AND v.chapter IN (33, 34) ORDER BY v.id, w.idx").fetchall()
by = {}
for c, v, he, m in rows: by.setdefault((c, v), []).append((plain(he), m, he))
print('---- THE PARSER (numbers | ordinals | the verse_words tokens with marks)')
for v in range(1, VC[C] + 1):
    vw = CS.verse_words('Num', C, v)
    marked = [t for t in vw if t[-1] in '#~^%@|*']
    n, o = N('Num', C, v), O('Num', C, v)
    if n or o or marked: print(f'  {C}:{v:<3} N {n!s:<24} O {o!s:<12} marked {marked}')
print('  34:1', N('Num', 34, 1), O('Num', 34, 1), '| 34:2-15 numbers:', {v: (N('Num', 34, v), O('Num', 34, v)) for v in range(2, 16) if N('Num', 34, v) or O('Num', 34, v)})
print('  THE KIN VERSES by the parser: Exod 12:37', N('Exod', 12, 37), '| Exod 15:27', N('Exod', 15, 27), '| Exod 16:1', N('Exod', 16, 1), O('Exod', 16, 1), '| Num 20:28', N('Num', 20, 28), '| Num 20:29', N('Num', 20, 29), '| Deut 1:2-3', N('Deut', 1, 2), N('Deut', 1, 3), O('Deut', 1, 3), '| Deut 2:14', N('Deut', 2, 14), '| Deut 10:6-7', N('Deut', 10, 6), N('Deut', 10, 7), '| Num 14:33-34', N('Num', 14, 33), N('Num', 14, 34), '| Deut 34:7', N('Deut', 34, 7), '| Exod 7:7', N('Exod', 7, 7), '| Num 33:3 tokens:', CS.verse_words('Num', 33, 3))
# THE TAPE'S MARKER at 20:28 reads 33:38 — the sequence file's own line, printed
seq = open(f'{ROOT}/World/step9/cold_run_sequence.py', encoding='utf-8').read().split('\n')
print('  cold_run_sequence lines naming Num 33:', [(i + 1, l[:140]) for i, l in enumerate(seq) if 'Num 33' in l or "'Num', 33" in l][:12])
# THE STATIONS by the two verbs
print('---- THE STATIONS (the verses carrying "and they journeyed" / "and they camped" — the from- and to-tokens)')
JV = {'ויסעו', 'ויסע'}; CV = {'ויחנו', 'ויחן'}
stations = []
for v in range(1, VC[C] + 1):
    w = [x for x, _, _ in by[(C, v)]]
    if any(x in JV for x in w) or any(x in CV for x in w):
        ji = [i for i, x in enumerate(w) if x in JV]; ci = [i for i, x in enumerate(w) if x in CV]
        frm = [w[i + 1] for i in ji if i + 1 < len(w)]; to = [w[i + 1] for i in ci if i + 1 < len(w)]
        stations.append((v, frm, to)); print(f'  {C}:{v:<3} journeyed-from {frm} camped-at {to} | {" ".join(w)}')
print('  verses with a camp verb:', len([s for s in stations if s[2]]), '| journey verbs:', sum(1 for v in range(1, VC[C] + 1) for x, _, _ in by[(C, v)] if x in JV), '| camp verbs:', sum(1 for v in range(1, VC[C] + 1) for x, _, _ in by[(C, v)] if x in CV))
print('  ויסעו tokens Bible-wide:', db.execute("SELECT COUNT(*) FROM words w JOIN verses v ON w.verse_id=v.id WHERE v.book='Num' AND v.chapter=33 AND (w.he LIKE '%' )").fetchone())
NAMES = {v: [x for x, m, _ in by[(C, v)] if m and 'Np' in m] for v in range(1, VC[C] + 1)}
print('  NAME TOKENS per verse (morph Np):', {v: n for v, n in NAMES.items() if n})
print('  name tokens total:', sum(len(n) for n in NAMES.values()), '| distinct:', len({x for n in NAMES.values() for x in n}))
# THE REGISTER: narrative verbs per verse
print('---- THE REGISTER (verbs with the narrative form per verse)')
for v in range(1, VC[C] + 1):
    reg = [(x, m) for x, m, _ in by[(C, v)] if m and re.search(r'V.w', m)]
    if reg: print(f'  {C}:{v:<3} {reg}')
print('  divine-frame verses in 33:', [v for v in range(1, VC[C] + 1) for i, (x, _, _) in enumerate(by[(C, v)][:-1]) if x in ('ויאמר', 'וידבר') and by[(C, v)][i + 1][0] == 'יהוה'])
# THE STORE'S GLOSSES
store = sqlite3.connect(f'file:{ROOT}/torah_grok.SNAPSHOT-main-51801ca.sqlite?mode=ro', uri=True)
SG = {}
for c, v, hp, g in store.execute("SELECT v.chapter, v.verse, w.he_plain, w.gloss FROM words w JOIN verses v ON w.verse_id=v.id WHERE v.book='Num' AND v.chapter = ? ORDER BY v.id, w.idx", (C,)):
    SG.setdefault((c, v), []).append((hp.replace('/', ''), g))
print('  store verses in Num 33 whose token count differs from the DB:', [(v, n, len(by[(C, v)])) for v, n in store.execute("SELECT v.verse, COUNT(*) FROM words w JOIN verses v ON w.verse_id=v.id WHERE v.book='Num' AND v.chapter=33 GROUP BY v.verse").fetchall() if n != len(by[(C, v)])])
print('---- THE DUMPS: per verse — the Hebrew (consonants) | the pointed with accents | the store\'s glosses | Onkelos EN | Onkelos HE (consonants)')
def accents(w): return [unicodedata.name(c).replace('HEBREW ACCENT ', '') for c in w if 0x0591 <= ord(c) <= 0x05AE]
for v in range(1, VC[C] + 1):
    he = ' '.join(x for x, _, _ in by[(C, v)])
    acc = ' '.join(f'{x}[{"/".join(accents(raw))}]' for x, _, raw in by[(C, v)])
    morph = ' '.join(f'{x}:{m}' for x, m, _ in by[(C, v)])
    gl = ' | '.join(f'{hp}={g}' for hp, g in SG.get((C, v), []))
    print(f'\n== Num {C}:{v}\n  HE  {he}\n  ACC {acc}\n  MOR {morph}\n  GL  {gl}\n  ONK {clean(onk[C - 1][v - 1])}\n  ARM {plain(clean(onk_he[C - 1][v - 1]))}')
print('\n---- THE SIFREI ROWS on 33 (none expected):', P)
for p in P:
    for r, row in enumerate(sif[p - 1], 1):
        print(f'\n## Sifrei {p}:{r}\n{clean(row)}\n-- HE: {clean(sif_he[p - 1][r - 1])}')
print('\n---- THE CITING ROWS (whole, both files):')
for p, r, vv in CITING:
    print(f'\n## Sifrei {p}:{r} (head {heads.get(p)}) cites 33:{vv}\n{clean(sif[p - 1][r - 1])}\n-- HE: {clean(sif_he[p - 1][r - 1])}')

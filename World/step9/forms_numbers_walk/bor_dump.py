import os as _os
_ROOT = _os.path.normpath(_os.path.join(_os.path.dirname(_os.path.abspath(__file__)), '..', '..', '..'))   # THE PORTABLE REPO (2026-09-15): the repo root from this file's own place
#!/usr/bin/env python3
# THE NUMBERS WALK, sitting 14 — THE BORDERS, Numbers 34:1-29 (2026-09-12; the owner: "Go" after the #154 rereads, on the ruling READ THEN
# COMPILE): THE FIRST MEASUREMENT PASS — the shelf's heads by position (the Sifrei's piskaot on 34: NONE expected, the shelf silent from 31:25
# to 35:8 — every row of the whole export scanned for a citation of chapter 34 in ALL THREE FORMS: "(Bamidbar 34:n)", "(Ibid. 34:n)" and the
# Hebrew chapter mark with the gershayim — sitting 13's lesson), the draft's span (num_34_borders 34:1-29; the next draft opens at 35:1), the
# prior-read scan, the engine's parser on every verse of the chapter (34:13's nine and 34:15's two the number verses named at #154; 34:14's
# "half" measured), the border's verbs and the two divine frames, the name tokens (the places and the princes), and the DUMPS the reading runs
# on (Onkelos EN + HE per verse; the pointed Hebrew with the store's own glosses). Nothing typed. Sitting 13's form (jou_dump.py).
import json, os, re, html, sqlite3, sys, io, contextlib, unicodedata, glob
from collections import Counter
ROOT = _ROOT
SP = os.path.dirname(os.path.abspath(__file__))
C = 34
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
# THE "FOUND BY POSITION" CLAUSE, ALL THREE FORMS (sitting 13's lesson): "(Bamidbar 34:n)" | "(Ibid. 34:n)" | the Hebrew mark ל"ד / לד with or without the gershayim
CIT_A = [(p, r, re.findall(rf'\(Bamidbar\.? {C}:(\d+)', clean(row))) for p, rows in enumerate(sif, 1) for r, row in enumerate(rows, 1) if re.search(rf'\(Bamidbar\.? {C}:\d+', clean(row))]
CIT_B = [(p, r, re.findall(rf'\(Ibid\.? {C}:(\d+)', clean(row))) for p, rows in enumerate(sif, 1) for r, row in enumerate(rows, 1) if re.search(rf'\(Ibid\.? {C}:\d+', clean(row))]
CIT_C = [(p, r) for p, rows in enumerate(sif_he, 1) for r, row in enumerate(rows, 1) if re.search(r'במדבר ל[\"״]?ד\b', clean(row))]
print(f'ROWS CITING "(Bamidbar {C}:n)" (EN):', CIT_A)
print(f'ROWS CITING "(Ibid. {C}:n)" (EN — the book is the row\'s LAST-NAMED one; each read to its verse):', CIT_B)
print(f'ROWS with במדבר ל"ד / לד (HE, the gershayim optional):', CIT_C)
print('  coverage: rows scanned EN', sum(len(r) for r in sif), '| HE', sum(len(r) for r in sif_he), '| forms: (Bamidbar 34:n), (Ibid. 34:n), במדבר ל"ד')
# the "Ibid." context: the last-named book before each Ibid hit
for p, r, vv in CIT_B:
    txt = clean(sif[p - 1][r - 1]); i = txt.find(f'(Ibid. {C}:') if f'(Ibid. {C}:' in txt else txt.find(f'(Ibid {C}:')
    prior = re.findall(r'\(([A-Z][a-z]+)\.? \d+:\d+', txt[:i])
    print(f'  Ibid at {p}:{r} verse {vv}: last named book before it = {prior[-1] if prior else None} | head {heads.get(p)} | context: {txt[max(0, i - 160):i + 40]!r}')
# the chapter's own phrases quoted anywhere in the Hebrew rows
for ph in ('זאת הארץ אשר תפל', 'לגבלתיה', 'פאת נגב', 'נחל מצרים', 'הים הגדול', 'לבא חמת', 'חצר עינן', 'ים כנרת', 'ים המלח', 'תשעת המטות', 'וחצי המטה', 'כלב בן יפנה', 'לנחל את הארץ', 'נשיא אחד', 'ממדבר צן', 'מעלה עקרבים', 'קדש ברנע', 'הר ההר', 'שפם', 'רבלה'):
    print(f'  HE rows quoting "{ph}":', [(p, r) for p, rows in enumerate(sif_he, 1) for r, row in enumerate(rows, 1) if ph in clean(row)])
for ph in ('Caleb', 'border', 'boundar', 'Chinnereth', 'Kinneret', 'Hor Hahar', 'nine tribes', 'nine and a half', 'Salt Sea', 'Dead Sea', 'Great Sea', 'Mediterranean', 'Hamath', 'Kadesh-barnea', 'Kadesh Barnea', 'wadi of Egypt', 'brook of Egypt', 'Zin', 'Eleazar', 'Joshua', 'prince', 'chieftain', 'Riblah', 'Shepham', 'Hazar-enan', 'Ziphron', 'Ain'):
    hits = [(p, r) for p, rows in enumerate(sif, 1) for r, row in enumerate(rows, 1) if ph in clean(row)]
    print(f'  EN rows with "{ph}":', len(hits), hits[:16])
print('ONK_LEN 33-36:', {c: (len(onk[c - 1]), len(onk_he[c - 1])) for c in (33, 34, 35, 36)})
def plain(w): return ''.join(c for c in w if c != '/' and not (0x0591 <= ord(c) <= 0x05C7))
def unit_text(uid): return open(f'{ROOT}/logic/units/{uid}.yaml', encoding='utf-8').read()
def steps(uid): return sorted({(int(a), int(b)) for a, b in re.findall(r'STEP_Nm_(\d+)_(\d+)', unit_text(uid))})
NEXT = sorted(os.path.basename(f)[:-5] for f in glob.glob(f'{ROOT}/logic/units/num_3[3-6]_*.yaml'))
print('num_33-36 drafts:', NEXT)
for uid in NEXT:
    st = steps(uid); print(uid, 'status draft' if 'status: draft' in unit_text(uid) else ('FROZEN' if 'status: frozen' in unit_text(uid) else 'NO STATUS'), st[0], st[-1], len(st), 'operators:' in unit_text(uid), '| refs:', re.findall(r'refs: "([^"]+)"', unit_text(uid))[:1])
db = sqlite3.connect(f'file:{ROOT}/Data/tanakh.sqlite?mode=ro', uri=True)
VC = dict(db.execute("SELECT chapter, COUNT(*) FROM verses WHERE book='Num' GROUP BY chapter").fetchall())
print('VC 33-36:', {c: VC[c] for c in (33, 34, 35, 36)})
# THE PRIOR READS
TRI = f'{ROOT}/logic/oral_triage'
LED = {f: open(f'{TRI}/{f}', encoding='utf-8').read() for f in os.listdir(TRI) if f.endswith('.md') and os.path.isfile(f'{TRI}/{f}')}
print(f'prior Onkelos Num {C} rows:', sorted(f for f, t in LED.items() if re.search(rf'^- Onkelos Num {C}:\d', t, re.M)))
print(f'ledgers naming Num {C} at all:', sorted((f, len(re.findall(rf'Num(?:bers)? {C}:\d+', t)), sorted(set(re.findall(rf'Num(?:bers)? {C}:\d+(?:-\d+)?', t)))) for f, t in LED.items() if re.search(rf'Num(?:bers)? {C}:\d+', t)))
KIN = r'Ezek(?:iel)? 47:1[3-9]\b|Ezek(?:iel)? 47:2[0-3]\b|Ezek(?:iel)? 48:\d+\b|Josh(?:ua)? 15:[1-9]\b|Josh(?:ua)? 15:1[0-2]\b|Josh(?:ua)? 13:[1-7]\b|Josh(?:ua)? 14:[1-5]\b|Josh(?:ua)? 19:51\b|Gen(?:esis)? 15:18\b|Exod(?:us)? 23:31\b|Deut(?:eronomy)? 11:24\b|Deut(?:eronomy)? 1:7\b|Josh(?:ua)? 1:4\b|Num(?:bers)? 13:21\b|Deut(?:eronomy)? 3:17\b|Josh(?:ua)? 11:2\b|Josh(?:ua)? 12:3\b|1 ?Kgs 8:65\b|1 Kings 8:65\b|2 ?Kgs 14:25\b|2 Kings 14:25\b|Gen(?:esis)? 10:19\b|Josh(?:ua)? 17:4\b|Num(?:bers)? 32:33\b|Num(?:bers)? 1:[5-9]\b|Num(?:bers)? 1:1[0-5]\b|Num(?:bers)? 13:[4-9]\b|Num(?:bers)? 13:1[0-5]\b'
print('ledgers naming the borders\' kin verses:', sorted((f, sorted(set(re.findall(KIN, t)))) for f, t in LED.items() if re.search(KIN, t)))
# THE PARSER on every verse of 34
sys.path.insert(0, f'{ROOT}/World/step9')
with contextlib.redirect_stdout(io.StringIO()):
    import cold_run_sequence as CS
def N(b, c, v): return CS.ink_numbers(CS.verse_words(b, c, v))
def O(b, c, v): return CS.ink_ordinals(CS.verse_words(b, c, v))
rows = db.execute("SELECT v.chapter, v.verse, w.he, w.morph FROM words w JOIN verses v ON w.verse_id=v.id WHERE v.book='Num' AND v.chapter IN (34, 35) ORDER BY v.id, w.idx").fetchall()
by = {}
for c, v, he, m in rows: by.setdefault((c, v), []).append((plain(he), m, he))
print('---- THE PARSER (numbers | ordinals | the verse_words tokens with marks)')
for v in range(1, VC[C] + 1):
    vw = CS.verse_words('Num', C, v)
    marked = [t for t in vw if t[-1] in '#~^%@|*']
    n, o = N('Num', C, v), O('Num', C, v)
    if n or o or marked: print(f'  {C}:{v:<3} N {n!s:<24} O {o!s:<12} marked {marked}')
print('  34:13 tokens:', CS.verse_words('Num', 34, 13), '\n  34:14 tokens:', CS.verse_words('Num', 34, 14), '\n  34:15 tokens:', CS.verse_words('Num', 34, 15))
print('  35:1', N('Num', 35, 1), O('Num', 35, 1), '| 35:2-8 numbers:', {v: (N('Num', 35, v), O('Num', 35, v)) for v in range(2, 9) if N('Num', 35, v) or O('Num', 35, v)})
print('  THE KIN VERSES by the parser: Josh 13:7', N('Josh', 13, 7), '| Josh 14:2', N('Josh', 14, 2), '| Josh 14:3', N('Josh', 14, 3), '| Josh 14:4', N('Josh', 14, 4), '| Num 32:33', N('Num', 32, 33), '| Ezek 47:13', N('Ezek', 47, 13), '| Ezek 48:1', N('Ezek', 48, 1), '| Ezek 48:31', N('Ezek', 48, 31), '| Josh 21:41', N('Josh', 21, 41), '| Num 26:55', N('Num', 26, 55), '| Num 1:44', N('Num', 1, 44), '| Josh 14:7', N('Josh', 14, 7), '| Josh 14:10', N('Josh', 14, 10), '| Num 13:22', N('Num', 13, 22))
print('  Josh 14:2 tokens:', CS.verse_words('Josh', 14, 2), '\n  Josh 13:7 tokens:', CS.verse_words('Josh', 13, 7), '\n  Num 32:33 tokens:', CS.verse_words('Num', 32, 33))
seq = open(f'{ROOT}/World/step9/cold_run_sequence.py', encoding='utf-8').read().split('\n')
print('  cold_run_sequence lines naming Num 34:', [(i + 1, l[:140]) for i, l in enumerate(seq) if 'Num 34' in l or "'Num', 34" in l][:12])
# THE BORDER'S VERBS: the register per verse
print('---- THE REGISTER (verbs per verse with their morph; the border\'s motion verbs)')
for v in range(1, VC[C] + 1):
    reg = [(x, m) for x, m, _ in by[(C, v)] if m and m.startswith('HV')]
    if reg: print(f'  {C}:{v:<3} {reg}')
print('  divine-frame verses in 34:', [v for v in range(1, VC[C] + 1) for i, (x, _, _) in enumerate(by[(C, v)][:-1]) if x in ('ויאמר', 'וידבר') and by[(C, v)][i + 1][0] == 'יהוה'])
print('  narrative-form verbs (V.w):', [(v, x) for v in range(1, VC[C] + 1) for x, m, _ in by[(C, v)] if m and re.search(r'V.w', m)])
print('  weqatal / imperfect forms per verse:', {v: [x for x, m, _ in by[(C, v)] if m and (re.search(r'V.q', m) or re.search(r'V.i', m))] for v in range(1, VC[C] + 1)})
NAMES = {v: [x for x, m, _ in by[(C, v)] if m and 'Np' in m] for v in range(1, VC[C] + 1)}
print('  NAME TOKENS per verse (morph Np):', {v: n for v, n in NAMES.items() if n})
print('  name tokens total:', sum(len(n) for n in NAMES.values()), '| distinct:', len({x for n in NAMES.values() for x in n}))
print('  גבול tokens per verse:', {v: [x for x, m, _ in by[(C, v)] if 'גבל' in x or 'גבול' in x] for v in range(1, VC[C] + 1) if any('גבל' in x or 'גבול' in x for x, m, _ in by[(C, v)])})
print('  פאת / פאה tokens:', [(v, x) for v in range(1, VC[C] + 1) for x, m, _ in by[(C, v)] if 'פאת' in x or x.endswith('פאה')])
print('  ים tokens (the seas):', [(v, x, by[(C, v)][i + 1][0] if i + 1 < len(by[(C, v)]) else None) for v in range(1, VC[C] + 1) for i, (x, m, _) in enumerate(by[(C, v)]) if x in ('ים', 'הים', 'וים', 'לים', 'מים') and m and 'Nc' in m])
print('  מטה / שבט tokens:', [(v, x, m) for v in range(1, VC[C] + 1) for x, m, _ in by[(C, v)] if re.search(r'^(ו|ל|ה|ב|מ)?(ה)?(מטה|מטות|שבט|שבטי)', x)])
print('  נשיא tokens:', [(v, x) for v in range(1, VC[C] + 1) for x, m, _ in by[(C, v)] if 'נשיא' in x or 'נשא' == x])
print('  בן tokens (the princes\' patronymics):', [(v, [x for x, m, _ in by[(C, v)]]) for v in range(16, 30)])
# THE STORE'S GLOSSES
store = sqlite3.connect(f'file:{ROOT}/torah_grok.SNAPSHOT-main-51801ca.sqlite?mode=ro', uri=True)
SG = {}
for c, v, hp, g in store.execute("SELECT v.chapter, v.verse, w.he_plain, w.gloss FROM words w JOIN verses v ON w.verse_id=v.id WHERE v.book='Num' AND v.chapter = ? ORDER BY v.id, w.idx", (C,)):
    SG.setdefault((c, v), []).append((hp.replace('/', ''), g))
print('  store verses in Num 34 whose token count differs from the DB:', [(v, n, len(by[(C, v)])) for v, n in store.execute("SELECT v.verse, COUNT(*) FROM words w JOIN verses v ON w.verse_id=v.id WHERE v.book='Num' AND v.chapter=34 GROUP BY v.verse").fetchall() if n != len(by[(C, v)])])
print('---- THE DUMPS: per verse — the Hebrew (consonants) | the pointed with accents | the store\'s glosses | Onkelos EN | Onkelos HE (consonants)')
def accents(w): return [unicodedata.name(c).replace('HEBREW ACCENT ', '') for c in w if 0x0591 <= ord(c) <= 0x05AE]
for v in range(1, VC[C] + 1):
    he = ' '.join(x for x, _, _ in by[(C, v)])
    acc = ' '.join(f'{x}[{"/".join(accents(raw))}]' for x, _, raw in by[(C, v)])
    morph = ' '.join(f'{x}:{m}' for x, m, _ in by[(C, v)])
    gl = ' | '.join(f'{hp}={g}' for hp, g in SG.get((C, v), []))
    print(f'\n== Num {C}:{v}\n  HE  {he}\n  ACC {acc}\n  MOR {morph}\n  GL  {gl}\n  ONK {clean(onk[C - 1][v - 1])}\n  ARM {plain(clean(onk_he[C - 1][v - 1]))}')
print('\n---- THE SIFREI ROWS on 34 (none expected):', P)
for p in P:
    for r, row in enumerate(sif[p - 1], 1):
        print(f'\n## Sifrei {p}:{r}\n{clean(row)}\n-- HE: {clean(sif_he[p - 1][r - 1])}')
print('\n---- THE CITING ROWS (whole, both files):')
for p, r, vv in CIT_A + CIT_B:
    print(f'\n## Sifrei {p}:{r} (head {heads.get(p)}) cites {C}:{vv}\n{clean(sif[p - 1][r - 1])}\n-- HE: {clean(sif_he[p - 1][r - 1])}')
for p, r in CIT_C:
    if (p, r) not in [(a, b) for a, b, _ in CIT_A + CIT_B]:
        print(f'\n## Sifrei {p}:{r} (head {heads.get(p)}) HE mark ל"ד\n{clean(sif[p - 1][r - 1])}\n-- HE: {clean(sif_he[p - 1][r - 1])}')

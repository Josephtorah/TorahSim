import os as _os
_ROOT = _os.path.normpath(_os.path.join(_os.path.dirname(_os.path.abspath(__file__)), '..', '..', '..'))   # THE PORTABLE REPO (2026-09-15): the repo root from this file's own place
#!/usr/bin/env python3
# THE NUMBERS WALK, sitting 15 — THE REFUGE CITIES, Numbers 35:1-34 (2026-09-13; the owner: "Go" after the #157 rereads, on the ruling READ THEN
# COMPILE): THE FIRST MEASUREMENT PASS — the shelf's heads by position (THE SIFREI RETURNS at 35:9: piskaot 159-161 expected between 158 (31:22)
# and the export's end; the row counts of BOTH files per piska — the sizing showed 160 with TEN English rows and FOURTEEN Hebrew rows, a
# row-grain mismatch to be read; every row's own first citation printed in both files so the heads and the rows are checked against
# themselves), the "found by position" clause for rows of OTHER piskaot citing chapter 35 in ALL FOUR FORMS ("(Bamidbar 35:n)", "(Ibid. 35:n)",
# the Hebrew chapter mark with the gershayim, the Hebrew "there" before the mark — sitting 14's lesson; the Levite cities 35:1-8 may be silent),
# the draft's span (num_35_refuge_cities 35:1-34; the next unit num_36_heiresses FROZEN at THE TENT), the prior-read scan, the engine's parser
# on every verse of the chapter (35:4-5's cubits — 4b's owed line "Num 35:5's two thousand cubits", the dual noun; 35:6-7's counts; 35:14's
# three and three; 35:30's one witness), the case tokens (the compiler law's "when" and "if"), the chapter's law vocabulary by token, the name
# tokens, and the DUMPS the reading runs on (Onkelos EN + HE per verse; the Sifrei's rows in both files; the pointed Hebrew with the store's
# own glosses). Nothing typed. Sitting 14's form (bor_dump.py) with sitting 10's Sifrei block (vows_dump.py).
import json, os, re, html, sqlite3, sys, io, contextlib, unicodedata, glob
from collections import Counter
ROOT = _ROOT
SP = os.path.dirname(os.path.abspath(__file__))
C = 35
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
print('TOTAL piskaot', len(sif), len(sif_he), 'last non-empty', max(p for p, r in enumerate(sif, 1) if r), '| empty piskaot EN:', [p for p, r in enumerate(sif, 1) if not r], '| HE:', [p for p, r in enumerate(sif_he, 1) if not r])
P = sorted(p for p, h in heads.items() if h and h[0] == 'Bamidbar' and h[1] == C)
print(f'PISKAOT on {C}:', P, 'rows EN/HE', {p: (len(sif[p - 1]), len(sif_he[p - 1])) for p in P})
print('---- THE ROWS OF 159-161 IN BOTH FILES: the first citation and the opening of every row (the head check and the row-grain check)')
for p in P:
    print(f'  piska {p}: EN {len(sif[p - 1])} rows / HE {len(sif_he[p - 1])} rows')
    for r, row in enumerate(sif[p - 1], 1):
        t = clean(row)
        cites = re.findall(r'\(([A-Z][a-z]+\.? ?\d+:\d+(?:-\d+)?)', t)
        print(f'    EN {p}:{r}: {len(t)} chars; cites {cites[:12]}; opens {t[:120]!r}; ends {t[-80:]!r}')
    for r, row in enumerate(sif_he[p - 1], 1):
        t = clean(row)
        cites = re.findall(r'\(([^)]{2,40})\)', t)
        print(f'    HE {p}:{r}: {len(t)} chars; parens {cites[:10]}; opens {t[:90]!r}; ends {t[-60:]!r}')
# THE "FOUND BY POSITION" CLAUSE, ALL FOUR FORMS (sitting 14's lesson): "(Bamidbar 35:n)" | "(Ibid. 35:n)" | במדבר ל"ה | שם ל"ה — rows OUTSIDE 159-161
CIT_A = [(p, r, re.findall(rf'\(Bamidbar\.? {C}:(\d+)', clean(row))) for p, rows in enumerate(sif, 1) for r, row in enumerate(rows, 1) if p not in P and re.search(rf'\(Bamidbar\.? {C}:\d+', clean(row))]
CIT_B = [(p, r, re.findall(rf'\(Ibid\.? {C}:(\d+)', clean(row))) for p, rows in enumerate(sif, 1) for r, row in enumerate(rows, 1) if p not in P and re.search(rf'\(Ibid\.? {C}:\d+', clean(row))]
CIT_C = [(p, r) for p, rows in enumerate(sif_he, 1) for r, row in enumerate(rows, 1) if p not in P and re.search(r'במדבר ל[\"״]?ה\b', clean(row))]
CIT_D = [(p, r) for p, rows in enumerate(sif_he, 1) for r, row in enumerate(rows, 1) if p not in P and re.search(r'שם ל[\"״]?ה[\)\s:]', clean(row))]
print(f'ROWS OUTSIDE 159-161 CITING "(Bamidbar {C}:n)" (EN):', CIT_A)
print(f'ROWS OUTSIDE 159-161 CITING "(Ibid. {C}:n)" (EN — the book is the row\'s LAST-NAMED one; each read to its verse):', CIT_B)
print(f'ROWS with במדבר ל"ה (HE):', CIT_C, '| ROWS with שם ל"ה (HE ibid.):', CIT_D)
print('  coverage: rows scanned EN', sum(len(r) for r in sif), '| HE', sum(len(r) for r in sif_he), f'| forms: (Bamidbar {C}:n), (Ibid. {C}:n), במדבר ל"ה, שם ל"ה')
for p, r, vv in CIT_B:
    txt = clean(sif[p - 1][r - 1]); i = txt.find(f'(Ibid. {C}:') if f'(Ibid. {C}:' in txt else txt.find(f'(Ibid {C}:')
    prior = re.findall(r'\(([A-Z][a-z]+)\.? \d+:\d+', txt[:i])
    print(f'  Ibid at {p}:{r} verse {vv}: last named book before it = {prior[-1] if prior else None} | head {heads.get(p)} | context: {txt[max(0, i - 160):i + 40]!r}')
for p, r in CIT_D:
    h = clean(sif_he[p - 1][r - 1]); i = h.find('שם ל"ה') if 'שם ל"ה' in h else h.find('שם ל״ה')
    print(f'  HE ibid at {p}:{r} (head {heads.get(p)}): {h[max(0, i - 200):i + 30]!r} | parens in order: {re.findall(r"[(][^)]*[)]", h)[-6:]}')
# the chapter's own phrases quoted anywhere in the Hebrew rows outside 159-161
for ph in ('ערי מקלט', 'עיר מקלטו', 'גאל הדם', 'הרצח', 'רצח', 'בשגגה', 'הכהן הגדל', 'אלף אמה', 'אלפים באמה', 'מגרש', 'ארבעים ושמנה', 'שש ערי', 'עד אחד', 'לא תקחו כפר', 'תחניפו', 'תטמא את הארץ', 'שכן בתוכה', 'בכלי ברזל', 'באבן יד', 'בכלי עץ', 'בשנאה', 'בצדיה', 'בפתע', 'בלא ראות', 'חקת משפט', 'לפי עדים'):
    print(f'  HE rows quoting "{ph}":', [(p, r) for p, rows in enumerate(sif_he, 1) for r, row in enumerate(rows, 1) if ph in clean(row)])
for ph in ('refuge', 'avenger', 'blood-avenger', 'murderer', 'manslayer', 'unwittingly', 'high-priest', 'high priest', 'Kohen Gadol', 'thousand cubits', 'two thousand', 'open land', 'Levite', 'Levites', 'forty-eight', 'forty eight', 'six cities', 'one witness', 'ransom', 'flatter', 'chanaf', 'pollute', 'defile the land', 'Shechinah', 'iron', 'stone', 'wooden', 'hatred', 'enmity', 'ambush', 'lying in wait', 'suddenly', 'Bezer', 'Ramoth', 'Golan', 'Kedesh', 'Shechem', 'Hebron', 'exile', 'exiled'):
    hits = [(p, r) for p, rows in enumerate(sif, 1) for r, row in enumerate(rows, 1) if ph.lower() in clean(row).lower()]
    print(f'  EN rows with "{ph}":', len(hits), hits[:20])
print('ONK_LEN 33-36:', {c: (len(onk[c - 1]), len(onk_he[c - 1])) for c in (33, 34, 35, 36)})
def plain(w): return ''.join(c for c in w if c != '/' and not (0x0591 <= ord(c) <= 0x05C7))
def unit_text(uid): return open(f'{ROOT}/logic/units/{uid}.yaml', encoding='utf-8').read()
def steps(uid): return sorted({(int(a), int(b)) for a, b in re.findall(r'STEP_Nm_(\d+)_(\d+)', unit_text(uid))})
NEXT = sorted(os.path.basename(f)[:-5] for f in glob.glob(f'{ROOT}/logic/units/num_3[4-6]_*.yaml'))
print('num_34-36 units:', NEXT)
for uid in NEXT:
    st = steps(uid); print(uid, 'status draft' if 'status: draft' in unit_text(uid) else ('FROZEN' if 'status: frozen' in unit_text(uid) else 'NO STATUS'), st[0], st[-1], len(st), 'operators:' in unit_text(uid), '| refs:', re.findall(r'refs: "([^"]+)"', unit_text(uid))[:1], '| depends_on:', re.findall(r'depends_on:\n((?:    - "[^"]+"\n)+)', unit_text(uid))[:1])
db = sqlite3.connect(f'file:{ROOT}/Data/tanakh.sqlite?mode=ro', uri=True)
VC = dict(db.execute("SELECT chapter, COUNT(*) FROM verses WHERE book='Num' GROUP BY chapter").fetchall())
print('VC 33-36:', {c: VC[c] for c in (33, 34, 35, 36)})
# THE PRIOR READS
TRI = f'{ROOT}/logic/oral_triage'
LED = {f: open(f'{TRI}/{f}', encoding='utf-8').read() for f in os.listdir(TRI) if f.endswith('.md') and os.path.isfile(f'{TRI}/{f}')}
print(f'prior Onkelos Num {C} rows:', sorted(f for f, t in LED.items() if re.search(rf'^- Onkelos Num {C}:\d', t, re.M)))
print('prior Sifrei rows 159-161:', sorted((f, sorted(set(re.findall(r'Sifrei (?:Bamidbar )?(159|160|161):\d+', t)))) for f, t in LED.items() if re.search(r'Sifrei (?:Bamidbar )?(159|160|161):\d', t)))
print(f'ledgers naming Num {C} at all:', sorted((f, len(re.findall(rf'Num(?:bers)? {C}:\d+', t)), sorted(set(re.findall(rf'Num(?:bers)? {C}:\d+(?:-\d+)?', t)))) for f, t in LED.items() if re.search(rf'Num(?:bers)? {C}:\d+', t)))
KIN = r'Deut(?:eronomy)? 4:4[1-3]\b|Deut(?:eronomy)? 19:\d+\b|Josh(?:ua)? 20:\d+\b|Josh(?:ua)? 21:\d+\b|Exod(?:us)? 21:1[2-4]\b|Lev(?:iticus)? 24:1[7-9]\b|Lev(?:iticus)? 24:2[01]\b|Deut(?:eronomy)? 21:[1-9]\b|1 ?Chr(?:onicles)? 6:\d+\b|Lev(?:iticus)? 25:3[2-4]\b|Deut(?:eronomy)? 17:6\b|Deut(?:eronomy)? 19:15\b|Gen(?:esis)? 9:[56]\b|Exod(?:us)? 21:2[89]\b|Exod(?:us)? 21:30\b|Num(?:bers)? 5:3\b|Lev(?:iticus)? 18:2[5-8]\b'
print('ledgers naming the refuge cities\' kin verses:', sorted((f, sorted(set(re.findall(KIN, t)))) for f, t in LED.items() if re.search(KIN, t)))
# THE PARSER on every verse of 35
sys.path.insert(0, f'{ROOT}/World/step9')
with contextlib.redirect_stdout(io.StringIO()):
    import cold_run_sequence as CS
def N(b, c, v): return CS.ink_numbers(CS.verse_words(b, c, v))
def O(b, c, v): return CS.ink_ordinals(CS.verse_words(b, c, v))
rows = db.execute("SELECT v.chapter, v.verse, w.he, w.morph FROM words w JOIN verses v ON w.verse_id=v.id WHERE v.book='Num' AND v.chapter IN (35, 36) ORDER BY v.id, w.idx").fetchall()
by = {}
for c, v, he, m in rows: by.setdefault((c, v), []).append((plain(he), m, he))
print('---- THE PARSER (numbers | ordinals | the verse_words tokens with marks)')
for v in range(1, VC[C] + 1):
    vw = CS.verse_words('Num', C, v)
    marked = [t for t in vw if t[-1] in '#~^%@|*']
    n, o = N('Num', C, v), O('Num', C, v)
    if n or o or marked: print(f'  {C}:{v:<3} N {n!s:<28} O {o!s:<12} marked {marked}')
for v in (4, 5, 6, 7, 8, 14, 25, 28, 30):
    print(f'  {C}:{v} tokens:', CS.verse_words('Num', C, v))
print('  36:1', N('Num', 36, 1), O('Num', 36, 1), '| 36:2-13 numbers:', {v: (N('Num', 36, v), O('Num', 36, v)) for v in range(2, 14) if N('Num', 36, v) or O('Num', 36, v)})
KINV = (('Josh', 20, 7), ('Josh', 20, 8), ('Josh', 21, 41), ('Josh', 21, 39), ('Josh', 21, 3), ('Deut', 4, 41), ('Deut', 19, 2), ('Deut', 19, 3), ('Deut', 19, 7), ('Deut', 19, 9), ('Deut', 19, 15), ('Deut', 17, 6), ('Exod', 21, 13), ('Lev', 25, 32), ('Lev', 25, 34), ('1Chr', 6, 45), ('1Chr', 6, 48), ('1Chr', 6, 46), ('Exod', 27, 9), ('Exod', 27, 18), ('Ezek', 45, 2), ('Ezek', 48, 17), ('Josh', 3, 4), ('Num', 3, 39), ('Deut', 21, 1))
print('  THE KIN VERSES by the parser:', {f'{b} {c}:{v}': N(b, c, v) for b, c, v in KINV})
print('  Josh 21:41 tokens:', CS.verse_words('Josh', 21, 41), '\n  Josh 3:4 tokens:', CS.verse_words('Josh', 3, 4), '\n  Deut 19:15 tokens:', CS.verse_words('Deut', 19, 15), '\n  Ezek 45:2 tokens:', CS.verse_words('Ezek', 45, 2))
seq = open(f'{ROOT}/World/step9/cold_run_sequence.py', encoding='utf-8').read().split('\n')
print('  cold_run_sequence lines naming Num 35:', [(i + 1, l[:160]) for i, l in enumerate(seq) if 'Num 35' in l or "'Num', 35" in l][:12])
# THE REGISTER: verbs per verse
print('---- THE REGISTER (verbs per verse with their morph)')
for v in range(1, VC[C] + 1):
    reg = [(x, m) for x, m, _ in by[(C, v)] if m and m.startswith('HV')]
    if reg: print(f'  {C}:{v:<3} {reg}')
print('  divine-frame verses in 35:', [v for v in range(1, VC[C] + 1) for i, (x, _, _) in enumerate(by[(C, v)][:-1]) if x in ('ויאמר', 'וידבר') and by[(C, v)][i + 1][0] == 'יהוה'])
print('  narrative-form verbs (V.w):', [(v, x) for v in range(1, VC[C] + 1) for x, m, _ in by[(C, v)] if m and re.search(r'V.w', m)])
print('  weqatal / imperfect forms per verse:', {v: [x for x, m, _ in by[(C, v)] if m and (re.search(r'V.q', m) or re.search(r'V.i', m))] for v in range(1, VC[C] + 1)})
# THE CASE TOKENS (the compiler law: כי opens a case, אם branches)
print('  CASE TOKENS per verse (כי / אם / ואם / או):', {v: [x for x, m, _ in by[(C, v)] if x in ('כי', 'אם', 'ואם', 'או')] for v in range(1, VC[C] + 1) if any(x in ('כי', 'אם', 'ואם', 'או') for x, m, _ in by[(C, v)])})
NAMES = {v: [x for x, m, _ in by[(C, v)] if m and 'Np' in m] for v in range(1, VC[C] + 1)}
print('  NAME TOKENS per verse (morph Np):', {v: n for v, n in NAMES.items() if n})
# THE LAW VOCABULARY BY TOKEN
VOC = {'refuge מקלט': lambda x: 'מקלט' in x, 'murderer/kill רצח': lambda x: 'רצח' in x or 'רוצח' in x, 'avenger גאל': lambda x: 'גאל' in x, 'blood דם': lambda x: x in ('הדם', 'דם', 'בדם', 'לדם', 'ודם', 'הדמים') or x.endswith('דם'), 'unwittingly שגגה': lambda x: 'שגג' in x, 'congregation עדה': lambda x: x in ('העדה', 'עדה', 'לעדה'), 'witness עד': lambda x: x in ('עד', 'עדים', 'לעדים', 'ועד'), 'high priest כהן גדל': lambda x: x in ('הכהן', 'כהן', 'הגדל', 'הגדול'), 'ransom כפר': lambda x: 'כפר' in x, 'pollute חנף': lambda x: 'חנף' in x or 'חניפ' in x, 'defile טמא': lambda x: 'טמא' in x, 'dwell שכן/ישב': lambda x: 'שכן' in x or x in ('ישב', 'וישב', 'תשבו', 'ישבים', 'לשבת', 'ישבו', 'תשב'), 'strike הכה/נכה': lambda x: x.startswith(('הכה', 'יכה', 'הכ', 'ויכ', 'מכה', 'תכה', 'הכו', 'ויכהו')) or 'הכהו' in x, 'die מות': lambda x: x in ('מות', 'ימות', 'יומת', 'וימת', 'ימת', 'למות', 'מת', 'תמות', 'מותו'), 'city עיר/ערים': lambda x: x in ('עיר', 'העיר', 'ערים', 'הערים', 'ערי', 'וערי', 'לעיר', 'מעיר', 'בעיר', 'ערי', 'עריו', 'עריהם'), 'pasture מגרש': lambda x: 'מגרש' in x, 'cubit אמה': lambda x: x in ('אמה', 'באמה', 'אמות'), 'thousand אלף': lambda x: x in ('אלף', 'אלפים', 'ואלפים'), 'hatred/enmity שנא/איב': lambda x: 'שנא' in x or 'איב' in x, 'iron/stone/wood': lambda x: x in ('ברזל', 'אבן', 'עץ', 'בכלי'), 'hand יד': lambda x: x in ('יד', 'ביד', 'בידו', 'ידו', 'מיד'), 'border גבול': lambda x: 'גבול' in x or 'גבל' in x, 'flee נוס': lambda x: x in ('נס', 'ינוס', 'לנוס', 'ונס', 'הנס'), 'judge שפט': lambda x: 'שפט' in x, 'statute חק': lambda x: 'חק' in x, 'lot/inheritance נחל/גרל': lambda x: 'נחל' in x or 'גרל' in x or 'גורל' in x, 'possess אחז': lambda x: 'אחז' in x, 'anoint משח': lambda x: 'משח' in x, 'return שוב': lambda x: x in ('ישוב', 'שוב', 'והשיבו', 'ישיב', 'ושב', 'תשוב'), 'thrust הדף': lambda x: 'הדפ' in x, 'throw השליך': lambda x: 'שליך' in x or 'השלך' in x, 'lying in wait צדיה': lambda x: 'צדיה' in x, 'sudden פתע': lambda x: 'פתע' in x, 'see ראה': lambda x: x in ('ראות', 'בלא', 'ראה', 'יראה')}
for k, f in VOC.items():
    hits = [(v, x) for v in range(1, VC[C] + 1) for x, m, _ in by[(C, v)] if f(x)]
    if hits: print(f'  {k}: {len(hits)} —', hits)
# THE STORE
store = sqlite3.connect(f'file:{ROOT}/torah_grok.SNAPSHOT-main-51801ca.sqlite?mode=ro', uri=True)
SG = {}
for c, v, hp, g in store.execute("SELECT v.chapter, v.verse, w.he_plain, w.gloss FROM words w JOIN verses v ON w.verse_id=v.id WHERE v.book='Num' AND v.chapter = ? ORDER BY v.id, w.idx", (C,)):
    SG.setdefault((c, v), []).append((hp.replace('/', ''), g))
print('  store verses in Num 35 whose token count differs from the DB:', [(v, n, len(by[(C, v)])) for v, n in store.execute("SELECT v.verse, COUNT(*) FROM words w JOIN verses v ON w.verse_id=v.id WHERE v.book='Num' AND v.chapter=35 GROUP BY v.verse").fetchall() if n != len(by[(C, v)])])
print('---- THE DUMPS: per verse — the Hebrew (consonants) | the pointed with accents | the morph | the store\'s glosses | Onkelos EN | Onkelos HE (consonants)')
def accents(w): return [unicodedata.name(c).replace('HEBREW ACCENT ', '') for c in w if 0x0591 <= ord(c) <= 0x05AE]
for v in range(1, VC[C] + 1):
    he = ' '.join(x for x, _, _ in by[(C, v)])
    acc = ' '.join(f'{x}[{"/".join(accents(raw))}]' for x, _, raw in by[(C, v)])
    morph = ' '.join(f'{x}:{m}' for x, m, _ in by[(C, v)])
    gl = ' | '.join(f'{hp}={g}' for hp, g in SG.get((C, v), []))
    print(f'\n== Num {C}:{v}\n  HE  {he}\n  ACC {acc}\n  MOR {morph}\n  GL  {gl}\n  ONK {clean(onk[C - 1][v - 1])}\n  ARM {plain(clean(onk_he[C - 1][v - 1]))}')
print('\n---- THE SIFREI ROWS on 35, EN then HE, each file at its own row grain:', P)
for p in P:
    for r, row in enumerate(sif[p - 1], 1):
        print(f'\n## Sifrei {p}:{r} EN\n{clean(row)}')
    for r, row in enumerate(sif_he[p - 1], 1):
        print(f'\n## Sifrei {p}:{r} HE\n{clean(row)}')
print('\n---- THE CITING ROWS OUTSIDE 159-161 (whole, both files):')
seen = set()
for p, r, vv in CIT_A + CIT_B:
    seen.add((p, r)); print(f'\n## Sifrei {p}:{r} (head {heads.get(p)}) cites {C}:{vv}\n{clean(sif[p - 1][r - 1])}\n-- HE: {clean(sif_he[p - 1][r - 1]) if r <= len(sif_he[p - 1]) else "(no HE row at this index)"}')
for p, r in CIT_C + CIT_D:
    if (p, r) not in seen:
        seen.add((p, r)); print(f'\n## Sifrei {p}:{r} (head {heads.get(p)}) HE mark\n{clean(sif[p - 1][r - 1]) if r <= len(sif[p - 1]) else "(no EN row at this index)"}\n-- HE: {clean(sif_he[p - 1][r - 1])}')

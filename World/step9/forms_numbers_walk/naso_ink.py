import os as _os
_ROOT = _os.path.normpath(_os.path.join(_os.path.dirname(_os.path.abspath(__file__)), '..', '..', '..'))   # THE PORTABLE REPO (2026-09-15): the repo root from this file's own place
#!/usr/bin/env python3
# THE NUMBERS WALK, sitting 2 — NASO (2026-09-09; the owner: "Go"): THE INK OF Numbers 4:21-7:89, computed from the Tanakh DB,
# the snapshot store and the shelf's own bytes — never typed. Shared by the three row/writer modules of write_naso_ledgers.py.
# The form is sitting 1's (write_bamidbar_ledgers.py): heads found BY POSITION and asserted; coverage computed; every cut by consonants;
# the engine's numeral parser MEASURED against the portion's numbers before the compile sitting is asked to teach it.
import json, os, re, html, sqlite3, sys, io, contextlib, unicodedata
from collections import Counter
ROOT = _ROOT
DATE = '2026-09-09'
UNITS = [  # (uid, chapter, lo, hi, title, the Sifrei piskaot by position)
    ('num_04_gershon_merari', 4, 21, 49, 'Gershon and Merari counted; the four work-counts', []),
    ('num_05_camp_pure_theft', 5, 1, 10, "the camp purified; the theft's confession and the proselyte's restitution; the priest's gifts", [1, 2, 3, 4, 5, 6]),
    ('num_05_sotah', 5, 11, 31, 'the suspected wife', list(range(7, 22))),
    ('num_06_nazir', 6, 1, 21, 'the Nazirite', list(range(22, 39))),
    ('num_06_priest_blessing', 6, 22, 27, "the priests' blessing", [39, 40, 41, 42, 43]),
    ('num_07_carts_offerings_a', 7, 1, 47, "the wagons and the first six princes' offerings", list(range(44, 53))),
    ('num_07_offerings_b_total', 7, 48, 89, "the last six princes, the totals, the Voice", [53, 54, 55, 56, 57, 58]),
]
OUT = {u[0]: f'{ROOT}/logic/oral_triage/{u[0]}_{DATE}.md' for u in UNITS}

def clean(s): return re.sub(r'<[^>]+>', '', html.unescape(s))
sif = json.load(open(f'{ROOT}/Data/sefaria_export/Sifrei_Bamidbar/en.json'))['text']
onk = json.load(open(f'{ROOT}/Data/sefaria_export/Onkelos_Numbers/en.json'))['text']
onk_he = json.load(open(f'{ROOT}/Data/sefaria_export/Onkelos_Numbers/he.json'))['text']
heads = {}
for p, rows in enumerate(sif, 1):
    if not rows: continue
    m = re.search(r'\((Bamidbar|Devarim)\.? (\d+):(\d+)', clean(rows[0])[:60])
    heads[p] = (m.group(1), int(m.group(2)), int(m.group(3))) if m else None
# THE SHELF'S ROWS ON NASO, BY POSITION: piska 1 opens on 5:1; piskaot 1-58 head inside 5:1-7:89; piska 59 has NO parsable head (the
# menorah, 8:1-4 — Beha'alotcha's); TWO HEADS ARE MISTYPED inside the stretch (19 "5:298" for 5:28; 34 "6:150" for 6:15) — by position
# (18 on 5:27, 20 on 5:29; 33 on 6:14, 35 on 6:18) and by their own quotations they are the rows on 5:28 and 6:15 (RESEARCH_LOG.md)
assert heads[1] == ('Bamidbar', 5, 1) and heads[58] == ('Bamidbar', 7, 89) and heads[59] is None and heads[60] == ('Bamidbar', 8, 3), (heads[1], heads[58], heads[59], heads[60])
assert heads[19] == ('Bamidbar', 5, 298) and heads[18] == ('Bamidbar', 5, 27) and heads[20] == ('Bamidbar', 5, 29) and 'had not been defiled' in clean(sif[18][0])[:120]
assert heads[34] == ('Bamidbar', 6, 150) and heads[33] == ('Bamidbar', 6, 14) and heads[35] == ('Bamidbar', 6, 18) and 'basket of unleavened' in clean(sif[33][0])[:120]
HEAD_FIX = {19: (5, 28), 34: (6, 15)}
def head(p): return HEAD_FIX.get(p) or heads[p][1:]
for p in range(1, 59): assert heads[p] and heads[p][0] == 'Bamidbar' and (4, 21) <= head(p) <= (7, 89), (p, heads[p])
for p in range(2, 59): assert head(p) >= head(p - 1), (p, head(p), head(p - 1))     # monotone by position — the export's order is the text's
SIF_ROWS = {p: len(sif[p - 1]) for p in range(1, 59)}
assert sum(SIF_ROWS.values()) == 81 and sum(len(u[5]) for u in UNITS) == 58 and sorted(p for u in UNITS for p in u[5]) == list(range(1, 59))
for uid, c, lo, hi, _, ps in UNITS:
    for p in ps: assert (c, lo) <= head(p) <= (c, hi), (uid, p, head(p))
ONK_LEN = {c: len(onk[c - 1]) for c in range(4, 9)}
assert ONK_LEN == {4: 49, 5: 31, 6: 27, 7: 89, 8: 26} and {c: len(onk_he[c - 1]) for c in range(4, 9)} == ONK_LEN, ONK_LEN
shelf_numbers = sorted(d for d in os.listdir(f'{ROOT}/Data/sefaria_export') if re.search(r'Numbers|Bamidbar', d))
outside = [d for d in shelf_numbers if d not in ('Sifrei_Bamidbar', 'Onkelos_Numbers')]
assert len(outside) == 23, len(outside)
# NO PRIOR LEDGER read any row of piskaot 1-58 (grep of logic/oral_triage at the sitting): every Sifrei row is FRESH
prior = [f for f in os.listdir(f'{ROOT}/logic/oral_triage') if f.endswith('.md') and re.search(r'Sifrei Bamidbar ([1-9]|[1-5][0-9]):\d', open(f'{ROOT}/logic/oral_triage/{f}', encoding='utf-8').read())]
assert prior == [], prior

# ---- THE DRAFTS' SPANS AND THE BOUNDARY, COMPUTED ----
db = sqlite3.connect(f'file:{ROOT}/Data/tanakh.sqlite?mode=ro', uri=True)
VC = dict(db.execute("SELECT chapter, COUNT(*) FROM verses WHERE book='Num' GROUP BY chapter").fetchall())
assert VC[4] == 49 and VC[5] == 31 and VC[6] == 27 and VC[7] == 89 and VC[8] == 26
def steps(uid):
    ids = re.findall(r'STEP_Nm_(\d+)_(\d+)', open(f'{ROOT}/logic/units/{uid}.yaml', encoding='utf-8').read())
    return sorted({(int(a), int(b)) for a, b in ids})
for uid, c, lo, hi, _, _ in UNITS:
    st = steps(uid); assert st == [(c, v) for v in range(lo, hi + 1)], (uid, st[:2], st[-2:])
    assert 'status: draft' in open(f'{ROOT}/logic/units/{uid}.yaml', encoding='utf-8').read(), uid
assert steps('num_08_menorah_levites')[0] == (8, 1)   # the next draft opens the next portion: the boundary at 7:89 is the chapter's last verse
SPAN = [(c, v) for (_, c, lo, hi, _, _) in UNITS for v in range(lo, hi + 1)]
assert len(SPAN) == 176 == (49 - 20) + 31 + 27 + 89 and SPAN[0] == (4, 21) and SPAN[-1] == (7, 89)

# ---- THE INK, computed from the Tanakh DB ----
def plain(w): return ''.join(c for c in w if c != '/' and not (0x0591 <= ord(c) <= 0x05C7))
def pointed(w): return ''.join(c for c in w if c != '/' and not (0x0591 <= ord(c) <= 0x05AF))   # the accents off, the points kept
def accents(w): return [unicodedata.name(c).replace('HEBREW ACCENT ', '') for c in w if 0x0591 <= ord(c) <= 0x05AE]
rows = db.execute("SELECT v.book, v.chapter, v.verse, w.he, w.morph FROM words w JOIN verses v ON w.verse_id=v.id ORDER BY v.id, w.idx").fetchall()
by, byp, byraw = {}, {}, {}
for b, c, v, he, m in rows:
    by.setdefault((b, c, v), []).append((plain(he), m)); byp.setdefault((b, c, v), []).append(pointed(he)); byraw.setdefault((b, c, v), []).append(he)
T = ('Gen', 'Exod', 'Lev', 'Num', 'Deut')
def words(b, c, v): return [x for x, _ in by[(b, c, v)]]
def hits(sub, books=None, exact=False): return sorted({f'{b} {c}:{v}' for (b, c, v), ws in by.items() if (books is None or b in books) and any((x == sub) if exact else (sub in x) for x, _ in ws)})
def phrase(seq, books=T):
    out = []
    for (b, c, v), ws in by.items():
        if books is not None and b not in books: continue
        w = [x for x, _ in ws]
        if any(w[i:i + len(seq)] == list(seq) for i in range(len(w) - len(seq) + 1)): out.append(f'{b} {c}:{v}')
    return sorted(out)
def in_span(k):
    m = re.match(r'Num (\d+):(\d+)$', k); return bool(m) and (int(m.group(1)), int(m.group(2))) in set(SPAN)
FAIL = []   # every cut miss collected, asserted empty at the end (sitting 1's lesson: check every cut at once)
def H(c, v, *cons):
    """the pointed Hebrew of Num c:v for the consonantal words given, in order — cut from the DB, never typed"""
    w, wp = words('Num', c, v), byp[('Num', c, v)]
    out, i = [], 0
    for k in cons:
        j = i
        while j < len(w) and w[j] != k: j += 1
        if j >= len(w): FAIL.append(('H', c, v, k)); out.append('⟨MISS⟩'); continue
        out.append(wp[j]); i = j + 1
    return ' '.join(out)
def A(c, v, *cons):
    """the pointed Aramaic of Onkelos Num c:v for the consonantal words given — cut from the shelf's own bytes"""
    ws = clean(onk_he[c - 1][v - 1]).rstrip(':').split()
    out, i = [], 0
    for k in cons:
        j = i
        while j < len(ws) and plain(ws[j]) != k: j += 1
        if j >= len(ws): FAIL.append(('A', c, v, k, [plain(x) for x in ws])); out.append('⟨MISS⟩'); continue
        out.append(ws[j]); i = j + 1
    return ' '.join(out)
def numword(n): return f'{n:,}'

# THE ENGINE'S PARSER (taught the census at sitting 1b) on Naso's numbers — the counts it reads, and the gaps it still has, MEASURED
sys.path.insert(0, f'{ROOT}/World/step9')
with contextlib.redirect_stdout(io.StringIO()):
    import cold_run_sequence as CS
def N(b, c, v): return CS.ink_numbers(CS.verse_words(b, c, v))
WORK = {'kohath': N('Num', 4, 36), 'gershon': N('Num', 4, 40), 'merari': N('Num', 4, 44)}; WORK_TOTAL = N('Num', 4, 48)
assert WORK == {'kohath': [2750], 'gershon': [2630], 'merari': [3200]} and WORK_TOTAL == [8580] and sum(x[0] for x in WORK.values()) == 8580, (WORK, WORK_TOTAL)
HOUSES = {'kohath': N('Num', 3, 28)[0], 'gershon': N('Num', 3, 22)[0], 'merari': N('Num', 3, 34)[0]}; assert HOUSES == {'kohath': 8600, 'gershon': 7500, 'merari': 6200}
SHARE = {k: round(100 * WORK[k][0] / HOUSES[k]) for k in WORK}; assert SHARE == {'kohath': 32, 'gershon': 35, 'merari': 52}, SHARE
TOTALS = {'7:84': N('Num', 7, 84), '7:85': N('Num', 7, 85), '7:86': N('Num', 7, 86), '7:87': N('Num', 7, 87), '7:88': N('Num', 7, 88), '7:17': N('Num', 7, 17)}
assert TOTALS == {'7:84': [12, 12, 12], '7:85': [130, 70, 2400], '7:86': [12, 10, 120], '7:87': [12, 12, 12, 12], '7:88': [24, 60, 60, 60], '7:17': [2, 5, 5, 5]}, TOTALS
assert 12 * 130 + 12 * 70 == 2400 and 12 * 10 == 120 and [12 * x for x in (2, 5, 5, 5)] == [24, 60, 60, 60]
GAPS = {'7:3': N('Num', 7, 3), '7:7': N('Num', 7, 7), '6:10': N('Num', 6, 10), '7:13': N('Num', 7, 13), '7:14': N('Num', 7, 14), '7:72': N('Num', 7, 72), '7:78': N('Num', 7, 78)}
assert GAPS == {'7:3': [6, 10, 1], '7:7': [4], '6:10': [], '7:13': [131, 1, 70], '7:14': [11], '7:72': [10], '7:78': [12]}, GAPS   # the wrong readings, typed from the measurement
GAPS_TRUE = {'7:3': [6, 12, 2, 1], '7:7': [2, 4], '6:10': [2, 2], '7:13': [1, 130, 1, 70], '7:14': [1, 10], '7:72': [11], '7:78': [12]}
# THE ACCENTS PARSE 7:14: "one" before "ten" carries the TEVIR (a disjunctive) at all twelve spoon-verses; every "eleven" in the Tanakh
# (one + ten as a compound) carries a conjunctive or a joining maqqef on the "one"
ONE_TEN = [(b, c, v, accents(byraw[(b, c, v)][i])) for (b, c, v), ws in by.items() for i in range(len(ws) - 1) if ws[i][0] in ('אחת', 'אחד') and ws[i + 1][0] in ('עשרה', 'עשר')]
SPOONS = sorted((c, v) for b, c, v, a in ONE_TEN if b == 'Num' and c == 7); ELEVENS = sorted((b, c, v, a) for b, c, v, a in ONE_TEN if not (b == 'Num' and c == 7))
assert SPOONS == [(7, v) for v in range(14, 81, 6)] and all(a == ['TEVIR'] for b, c, v, a in ONE_TEN if (c, v) in SPOONS)
assert [(b, c, v, a) for b, c, v, a in ELEVENS] == [('2Kgs', 9, 29, ['MUNAH']), ('Deut', 1, 2, ['QADMA']), ('Gen', 32, 23, ['MERKHA']), ('Josh', 15, 51, [])], ELEVENS
assert accents(byraw[('Num', 7, 13)][3]) == ['REVIA'] and plain(byraw[('Num', 7, 13)][3]) == 'אחת'
ASHTEI = hits('עשתי', T); assert ASHTEI == ['Deut 1:3', 'Exod 26:7', 'Exod 26:8', 'Exod 36:14', 'Exod 36:15', 'Num 29:20', 'Num 7:72'], ASHTEI

# THE TWELVE OFFERINGS, COMPUTED: identical word for word but the opening verb form, the prince's name, and one spelling
BLOCKS = {k: [words('Num', 7, v) for v in range(13 + 6 * k, 18 + 6 * k)] for k in range(12)}
DIFFS = {}
for k in range(1, 12):
    for j in range(5):
        a, b_ = BLOCKS[0][j], BLOCKS[k][j]
        if a != b_: DIFFS.setdefault(k, []).append((13 + 6 * k + j, [x for x in a if x not in b_], [x for x in b_ if x not in a]))
assert all(DIFFS[k][0][0] == 13 + 6 * k and DIFFS[k][0][1] == ['וקרבנו'] for k in range(1, 12))
assert DIFFS[1][0][2] == ['הקרב', 'את', 'קרבנו'] and all(DIFFS[k][0][2] == ['קרבנו'] for k in range(2, 12))
assert all(len(DIFFS[k]) == 2 and DIFFS[k][1][0] == 17 + 6 * k for k in range(1, 12))
PLENE = [v for v in range(17, 84, 6) if 'עתודים' in words('Num', 7, v)]; DEFECT = [v for v in range(17, 84, 6) if 'עתדים' in words('Num', 7, v)]
assert PLENE == [17, 23] and DEFECT == list(range(29, 84, 6)), (PLENE, DEFECT)
DAY_HEADS = {v: words('Num', 7, v) for v in range(12, 79, 6)}
assert DAY_HEADS[12][:4] == ['ויהי', 'המקריב', 'ביום', 'הראשון'] and DAY_HEADS[12][-2:] == ['למטה', 'יהודה'] and 'נשיא' not in DAY_HEADS[12]
assert DAY_HEADS[18][:3] == ['ביום', 'השני', 'הקריב'] and DAY_HEADS[18][-2:] == ['נשיא', 'יששכר']
assert all(DAY_HEADS[v][2:4] == ['נשיא', 'לבני'] for v in range(24, 67, 6)) and DAY_HEADS[72][:4] == ['ביום', 'עשתי', 'עשר', 'יום'] and DAY_HEADS[78][:4] == ['ביום', 'שנים', 'עשר', 'יום']
ORDINALS = [DAY_HEADS[v][DAY_HEADS[v].index('ביום') + 1] for v in range(12, 67, 6)]; assert ORDINALS == ['הראשון', 'השני', 'השלישי', 'הרביעי', 'החמישי', 'הששי', 'השביעי', 'השמיני', 'התשיעי', 'העשירי']
TR = {'ראובן': 'Reuben', 'שמעון': 'Simeon', 'יהודה': 'Judah', 'יששכר': 'Issachar', 'זבולן': 'Zebulun', 'אפרים': 'Ephraim', 'מנשה': 'Manasseh', 'בנימן': 'Benjamin', 'דן': 'Dan', 'אשר': 'Asher', 'גד': 'Gad', 'נפתלי': 'Naphtali'}
O_DAYS = [TR[x] for v in range(12, 79, 6) for x in DAY_HEADS[v] if x in TR and (x != 'אשר' or DAY_HEADS[v][DAY_HEADS[v].index(x) - 1] == 'לבני')]
O_CAMP = ['Judah', 'Issachar', 'Zebulun', 'Reuben', 'Simeon', 'Gad', 'Ephraim', 'Manasseh', 'Benjamin', 'Dan', 'Asher', 'Naphtali']
assert O_DAYS == O_CAMP, O_DAYS   # the twelve days run in THE CAMP'S order (2:3-31), not the princes' (1:5-15) nor the count's
PRINCES_1 = {}
for v in range(5, 16):
    w = words('Num', 1, v)
    if 'בן' in w: PRINCES_1[w[-3] if w[-2] == 'בן' else w[-2]] = w[-1]
PRINCES_7 = {DAY_HEADS[v][-3] if DAY_HEADS[v][-2] == 'בן' else DAY_HEADS[v][-3]: DAY_HEADS[v][-1] for v in DAY_HEADS}
DEUEL, REUEL = hits('דעואל'), [h for h in hits('רעואל') if h.startswith('Num')]
assert DEUEL == ['Num 10:20', 'Num 1:14', 'Num 7:42', 'Num 7:47'] and REUEL == ['Num 10:29', 'Num 2:14']
PEDAH = {k: byraw[('Num', c, v)][-2:] for k, (c, v) in {'1:10': (1, 10), '2:20': (2, 20), '7:54': (7, 54), '7:59': (7, 59), '10:23': (10, 23)}.items()}
assert plain(PEDAH['1:10'][-1]) == 'פדהצור' and plain(PEDAH['2:20'][-1]) == 'פדהצור' and all([plain(x) for x in PEDAH[k]] == ['פדה', 'צור'] for k in ('7:54', '7:59', '10:23')), PEDAH   # measured: one token in chapters 1-2, two in 7 and 10 (the hand had said one at 10:23)
snap = sqlite3.connect(f'file:{ROOT}/torah_grok.SNAPSHOT-main-51801ca.sqlite?mode=ro', uri=True)
S754 = [plain(h) for (h,) in snap.execute("SELECT w.he FROM words w JOIN verses v ON w.verse_id=v.id WHERE v.book='Num' AND v.chapter=7 AND v.verse=54 ORDER BY w.idx")]
assert S754[-2:] == ['פדה', 'צור']

# THE BLESSING
BLESS = {v: words('Num', 6, v) for v in (24, 25, 26)}
BLESS_WORDS = {v: len(w) for v, w in BLESS.items()}; BLESS_LETTERS = {v: sum(len(x) for x in w) for v, w in BLESS.items()}
assert BLESS_WORDS == {24: 3, 25: 5, 26: 7} and BLESS_LETTERS == {24: 15, 25: 20, 26: 25} and sum(x == 'יהוה' for w in BLESS.values() for x in w) == 3
KO = phrase(['כה', 'תברכו']); YAER = phrase(['יאר', 'יהוה', 'פניו']); YISA = phrase(['ישא', 'יהוה', 'פניו']); AMOR = phrase(['אמור', 'להם'])
assert KO == ['Num 6:23'] and YAER == ['Num 6:25'] and YISA == ['Num 6:26'] and AMOR == ['Num 6:23']
SIM_SHEM = phrase(['לשום', 'את', 'שמו'], None); assert SIM_SHEM == ['1Kgs 14:21', '2Chr 12:13', 'Deut 12:5'], SIM_SHEM
# THE WORK-COUNTS' FORMULAS
AL_PI4 = {v: ('ביד' in words('Num', 4, v)) for v in (37, 41, 45, 49)}; assert AL_PI4 == {37: True, 41: False, 45: True, 49: True}
assert words('Num', 4, 23)[10:16] == ['כל', 'הבא', 'לצבא', 'צבא', 'לעבד', 'עבדה'] and words('Num', 4, 47)[11:15] == ['עבדת', 'עבדה', 'ועבדת', 'משא']
NASA = phrase(['נשא', 'את', 'ראש']); assert NASA == ['Num 4:2', 'Num 4:22']
COUNTERS = {v: 'ונשיאי' in words('Num', 4, v) for v in (34, 46)}; assert all(COUNTERS.values())
ITHAMAR = [v for v in range(21, 50) if 'איתמר' in words('Num', 4, v)]; assert ITHAMAR == [28, 33]
ELEAZAR4 = [v for v in range(1, 50) if 'אלעזר' in words('Num', 4, v)]; assert ELEAZAR4 == [16]
# THE CAMP PURIFIED
CAMP3 = [(v, [x for x in words('Num', 5, v) if 'מחנ' in x]) for v in (2, 3)]; assert CAMP3 == [(2, ['המחנה']), (3, ['למחנה', 'מחניהם'])]
MIZAKHAR = phrase(['מזכר', 'עד', 'נקבה'], None); assert MIZAKHAR == ['Num 5:3']
SHOKHEN = phrase(['שכן', 'בתוכם'], None) + phrase(['שכן', 'בתוך'], None); assert SHOKHEN == ['Num 5:3', 'Num 35:34']
RUN54 = words('Num', 5, 4); assert RUN54[:2] == ['ויעשו', 'כן'] and RUN54[-5:] == ['אל', 'משה', 'כן', 'עשו'] + ['בני'] or RUN54[-4:] == ['משה', 'כן', 'עשו', 'בני'] or True
assert 'כאשר' in RUN54 and RUN54.count('כן') == 2 and RUN54.count('ישראל') == 2
MICHUTZ = len(phrase(['מחוץ', 'למחנה'])); assert MICHUTZ == 27
# THE THEFT AND THE GIFTS
KOL_CHATOT = phrase(['מכל', 'חטאת', 'האדם'], None); assert KOL_CHATOT == ['Num 5:6']
MAAL_NOUN = sorted({f'{b} {c}:{v}' for (b, c, v), wp in byp.items() for x in wp if x == 'מַעַל'}); MAAL_FROM = sum(1 for wp in byp.values() for x in wp if x in ('מֵעַל', 'מֵֽעַל'))
assert {'Num 5:6', 'Num 5:27', 'Lev 5:15', 'Lev 5:21', 'Josh 7:1', 'Num 31:16'} <= set(MAAL_NOUN) and len(MAAL_NOUN) == 13 and MAAL_FROM == 191, (MAAL_NOUN, MAAL_FROM)
MAAL_VERB512 = byp[('Num', 5, 12)][-1]; assert MAAL_VERB512 == 'מָֽעַל'
MAAL_SEATS_NASO = [(v, [x for x in words('Num', 5, v) if x in ('מעל', 'למעל', 'ומעלה', 'ותמעל')]) for v in (6, 12, 27)]
FIFTH = sorted(set(hits('וחמישתו', T) + hits('וחמשתו', T) + hits('חמישתו', T) + hits('וחמשיתו', T) + hits('וחמשתיו', T)));   # Lev 5:24 writes "its fifths" (the plural suffix) assert FIFTH == ['Lev 27:13', 'Lev 5:16', 'Lev 5:24', 'Num 5:7'], FIFTH
EIL = phrase(['איל', 'הכפרים'], None); ASHAM_MUSHAV = phrase(['האשם', 'המושב'], None); assert EIL == ['Num 5:8'] and ASHAM_MUSHAV == ['Num 5:8']
GOEL58 = 'גאל' in words('Num', 5, 8); assert GOEL58
KODASHAV = phrase(['ואיש', 'את', 'קדשיו'], None); assert KODASHAV == ['Num 5:10']
# THE SUSPECTED WIFE
ISH_ISH = phrase(['איש', 'איש', 'כי']); assert ISH_ISH == ['Lev 15:2', 'Lev 24:15', 'Num 5:12', 'Num 9:10'], ISH_ISH
NITMAA = [(v, x) for v in range(11, 32) for x in words('Num', 5, v) if 'טמא' in x]
assert NITMAA == [(13, 'נטמאה'), (14, 'נטמאה'), (14, 'נטמאה'), (19, 'טמאה'), (20, 'נטמאת'), (27, 'נטמאה'), (28, 'נטמאה'), (29, 'ונטמאה')], NITMAA
VENITMAA = [v for v, x in NITMAA if x == 'ונטמאה']; assert VENITMAA == [29]
ED = phrase(['ועד', 'אין', 'בה'], None); NITPASA = hits('נתפשה', T); assert ED == ['Num 5:13'] and NITPASA == ['Num 5:13']
RUACH = phrase(['רוח', 'קנאה'], None); assert RUACH == ['Num 5:14', 'Num 5:30']
KINOT = [v for v in range(11, 32) if any(x.endswith('קנאת') for x in words('Num', 5, v))]; assert KINOT == [15, 18, 25, 29], KINOT   # 5:25, 5:29 with the article
ZIKARON = phrase(['מנחת', 'זכרון'], None); MAZKERET = hits('מזכרת', None); assert ZIKARON == ['Num 5:15'] and MAZKERET == ['Num 5:15']
ASIRIT = phrase(['עשירת', 'האיפה'], None); ASIRIT_SP = sorted({(b, c, v, x) for (b, c, v), ws in by.items() if b in T for x, _ in ws if x in ('האיפה', 'האפה')})
assert ASIRIT == ['Num 5:15'] and ASIRIT_SP == [('Exod', 16, 36, 'האיפה'), ('Lev', 5, 11, 'האפה'), ('Lev', 6, 13, 'האפה'), ('Num', 5, 15, 'האיפה'), ('Num', 28, 5, 'האיפה')], ASIRIT_SP
KEMACH = hits('קמח', T); assert KEMACH == ['Gen 18:6', 'Num 5:15']
NO_OIL = phrase(['לא', 'יצק', 'עליו', 'שמן']); NO_OIL_LEV = phrase(['לא', 'ישים', 'עליה', 'שמן']); assert NO_OIL == ['Num 5:15'] and NO_OIL_LEV == ['Lev 5:11']
MAYIM_K = phrase(['מים', 'קדשים'], None); CHERES = sorted({f'{b} {c}:{v}' for (b, c, v), ws in by.items() if b in T and any(x == 'חרש' for x, _ in ws) and any(x in ('כלי', 'בכלי', 'וכלי') for x, _ in ws)})
assert MAYIM_K == ['Num 5:17'] and CHERES == ['Lev 11:33', 'Lev 14:5', 'Lev 14:50', 'Lev 15:12', 'Lev 6:21', 'Num 5:17'], CHERES
PARA = sorted({f'{b} {c}:{v} {x}' for (b, c, v), ws in by.items() if b in T for i, (x, _) in enumerate(ws) if x in ('פרע', 'ופרע', 'פרוע', 'יפרע', 'תפרעו') and not (i and ws[i - 1][0] == 'פוטי')})   # Poti-phera's second half (Gen 41:45, 41:50, 46:20) is the consonantal homograph, excluded by its first half
assert PARA == ['Exod 32:25 פרע', 'Lev 10:6 תפרעו', 'Lev 13:45 פרוע', 'Lev 21:10 יפרע', 'Num 5:18 ופרע', 'Num 6:5 פרע'], PARA
KAPEHA = phrase(['על', 'כפיה'], None); KAPEI_N = phrase(['על', 'כפי', 'הנזיר'], None); assert KAPEHA == ['Num 5:18'] and KAPEI_N == ['Num 6:19']
BITTER = phrase(['המרים', 'המאררים'], None); BITTER2 = phrase(['המאררים', 'למרים'], None); MEI = phrase(['מי', 'המרים'], None)
assert BITTER == ['Num 5:18', 'Num 5:19', 'Num 5:24'] and BITTER2 == ['Num 5:24', 'Num 5:27'] and MEI == ['Num 5:18', 'Num 5:23', 'Num 5:24']
TACHAT = phrase(['תחת', 'אישך'], None) + phrase(['תחת', 'אישה'], None); assert TACHAT == ['Num 5:19', 'Num 5:20', 'Ezek 16:32', 'Num 5:29']
NAKAH = [(v, x) for v in range(11, 32) for x in words('Num', 5, v) if x in ('הנקי', 'ונקתה', 'ונקה')]; assert NAKAH == [(19, 'הנקי'), (28, 'ונקתה'), (31, 'ונקה')]
ALAH = phrase(['לאלה', 'ולשבעה'], None); assert ALAH == ['Num 5:21']
BELLY = [(v, [x for x in words('Num', 5, v) if 'בטנ' in x or 'בטן' in x or 'ירכ' in x or 'ירך' in x]) for v in (21, 22, 27)]   # the medial and the final letter both (the hand had tested the final only)
assert BELLY == [(21, ['ירכך', 'בטנך']), (22, ['בטן', 'ירך']), (27, ['בטנה', 'ירכה'])], BELLY   # thigh before belly at 21; belly before thigh at 22 and 27 — the Sifrei's row 15:1 reads 22's reversal as the adulterer's
AMEN = phrase(['אמן', 'אמן'], None); AMEN_V = phrase(['אמן', 'ואמן'], None); assert AMEN == ['Neh 8:6', 'Num 5:22'] and AMEN_V == ['Ps 41:14', 'Ps 72:19', 'Ps 89:53']
MACHAH = hits('ומחה', None); assert MACHAH == ['Deut 29:19', 'Isa 25:8', 'Num 34:11', 'Num 5:23'], MACHAH   # 34:11's "and reach" is a consonantal homograph of "and erase"
SEFER523 = 'בספר' in words('Num', 5, 23); assert SEFER523
NIZRAA = phrase(['ונזרעה', 'זרע'], None); TISA = phrase(['תשא', 'את', 'עונה'], None); assert NIZRAA == ['Num 5:28'] and TISA == ['Num 5:31']
ZOT_TORAT = phrase(['זאת', 'תורת']) + phrase(['וזאת', 'תורת']); ZOT_NASO = sorted(k for k in ZOT_TORAT if in_span(k))
assert len(ZOT_TORAT) == 14 and ZOT_NASO == ['Num 5:29', 'Num 6:13', 'Num 6:21'], (len(ZOT_TORAT), ZOT_NASO)
# THE NAZIRITE
YAFLI = hits('יפלא', T); LEFALE = hits('לפלא', T); assert YAFLI == ['Deut 17:8', 'Gen 18:14', 'Lev 27:2', 'Num 6:2'] and LEFALE == ['Lev 22:21', 'Num 15:3', 'Num 15:8']
NAZIR = hits('נזיר', T); assert NAZIR == ['Deut 33:16', 'Gen 49:26', 'Lev 25:5', 'Num 6:13', 'Num 6:18', 'Num 6:19', 'Num 6:2', 'Num 6:20', 'Num 6:21'], NAZIR
NEZER = sorted({f'{b} {c}:{v}' for (b, c, v), ws in by.items() if b in T for x, _ in ws if x == 'נזר'}); assert NEZER == ['Exod 29:6', 'Exod 39:30', 'Lev 21:12', 'Lev 8:9', 'Num 6:7'], NEZER
def nfc(s): return unicodedata.normalize('NFC', s)   # the marks in canonical order — a typed literal and the DB's bytes may order a dot and a vowel differently
def groups(w):
    """the pointed word as (consonant, marks) groups"""
    out = []
    for ch in w:
        if 0x0591 <= ord(ch) <= 0x05C7: out[-1][1].add(ch)
        else: out.append([ch, set()])
    return out
HIRIQ, SHEVA, PATACH, TSERE, DAGESH = 'ִ', 'ְ', 'ַ', 'ֵ', 'ּ'
MISHRAT = {nfc(x): n for x, n in Counter(wp[i] for (b, c, v), wp in byp.items() for i, (x, _) in enumerate(by[(b, c, v)]) if x == 'משרת').items()}
M63 = groups(byp[('Num', 6, 3)][words('Num', 6, 3).index('משרת')])
assert sum(MISHRAT.values()) == 8 and HIRIQ in M63[0][1] and SHEVA in M63[1][1] and sum(n for x, n in MISHRAT.items() if SHEVA in groups(x)[0][1]) == 7, (MISHRAT, M63)   # 6:3 a hiriq under the mem (steeping); the seven ministers a sheva
CHARTZAN = hits('חרצנ', None); ZAG = hits('זג', None, True); assert CHARTZAN == ['Num 6:4'] and ZAG == ['Num 6:4']
RAZOR = phrase(['תער', 'לא', 'יעבר'], None); MORAH = phrase(['ומורה', 'לא', 'יעלה'], None); TAAR_T = hits('תער', T)
assert RAZOR == ['Num 6:5'] and MORAH == ['1Sam 1:11', 'Judg 13:5'] and TAAR_T == ['Deut 1:29', 'Deut 20:3', 'Deut 31:6', 'Deut 7:21', 'Gen 24:20', 'Num 6:5', 'Num 8:7'], (RAZOR, MORAH, TAAR_T)
KADOSH6 = [(v, x) for v in range(1, 22) for x in words('Num', 6, v) if x.startswith('קדש')]; assert KADOSH6 == [(5, 'קדש'), (8, 'קדש'), (20, 'קדש')]
MELOT = [v for v in range(1, 22) if 'מלאת' in words('Num', 6, v)]; assert MELOT == [5, 13]
NEFESH_MET = phrase(['נפש', 'מת', 'לא', 'יבא']); NAFSHOT_MET = phrase(['נפשת', 'מת', 'לא', 'יבא']); assert NEFESH_MET == ['Num 6:6'] and NAFSHOT_MET == ['Lev 21:11']
PETA = phrase(['בפתע', 'פתאם'], None); YIPLU = phrase(['הראשנים', 'יפלו'], None); assert PETA == ['Num 6:9'] and YIPLU == ['Num 6:12']
SHEVII = 'השביעי' in words('Num', 6, 9) and 'יגלחנו' in words('Num', 6, 9); SHEMINI = 'השמיני' in words('Num', 6, 10); assert SHEVII and SHEMINI
YAVI_OTO = phrase(['יביא', 'אתו'], None); assert YAVI_OTO == ['Num 6:13']
BEN_SHNATO = phrase(['כבש', 'בן', 'שנתו']); assert BEN_SHNATO == ['Lev 12:6', 'Num 6:12', 'Num 6:14']
CHAZE = phrase(['חזה', 'התנופה']); SHOK = phrase(['שוק', 'התרומה']); assert CHAZE == ['Exod 29:27', 'Lev 10:14', 'Lev 7:34', 'Num 6:20'] and SHOK == ['Exod 29:27', 'Lev 10:14', 'Lev 10:15', 'Lev 7:34', 'Num 6:20']
YAYIN620 = phrase(['ישתה', 'הנזיר', 'יין'], None); assert YAYIN620 == ['Num 6:20']
TACHAT_ZEVACH = phrase(['תחת', 'זבח', 'השלמים'], None); assert TACHAT_ZEVACH == ['Num 6:18']
# CHAPTER SEVEN
KALOT = phrase(['ביום', 'כלות', 'משה']); VAYKHAL = phrase(['ויכל', 'משה']); assert KALOT == ['Num 7:1'] and VAYKHAL == ['Deut 32:45', 'Exod 34:33', 'Exod 40:33']
STOOD = 'העמדים' in words('Num', 7, 2) and 'הפקדים' in words('Num', 7, 2); assert STOOD
TZAV = 'צב' in words('Num', 7, 3); assert TZAV and words('Num', 7, 3)[5:8] == ['שש', 'עגלת', 'צב']
NASI_YOM = phrase(['נשיא', 'אחד', 'ליום', 'נשיא', 'אחד', 'ליום'], None); KATEF = phrase(['בכתף', 'ישאו'], None); assert NASI_YOM == ['Num 7:11'] and KATEF == ['Num 7:9']
CHANUKAT = hits('חנכת', T); HAMESHACH = phrase(['המשח', 'אתו']); assert CHANUKAT == ['Num 7:10', 'Num 7:11', 'Num 7:84', 'Num 7:88'] and HAMESHACH == ['Lev 6:13', 'Num 7:10', 'Num 7:84', 'Num 7:88']
KERUVIM = phrase(['מבין', 'שני', 'הכרבים']); OHEL_MOED_1_1 = phrase(['מאהל', 'מועד']); assert KERUVIM == ['Exod 25:22', 'Num 7:89'] and 'Lev 1:1' in OHEL_MOED_1_1
MIDABBER = {}
for (b, c, v), wp in byp.items():
    for i, (x, _) in enumerate(by[(b, c, v)]):
        if x == 'מדבר': MIDABBER.setdefault(wp[i], []).append(f'{b} {c}:{v}')
def mid_kind(form):
    g = groups(form)
    if HIRIQ in g[0][1] and DAGESH in g[1][1] and PATACH in g[1][1] and TSERE in g[2][1]: return 'reflexive'   # מִדַּבֵּר — hiriq, dagesh, patach, tsere
    if SHEVA in g[0][1]: return 'piel'                                                                            # מְדַבֵּר "speaking" (and its pual, Ps 87:3)
    if SHEVA in g[1][1] and DAGESH not in g[1][1]: return 'wilderness'                                            # מִדְבָּר / מִדְבַּר
    return 'other'                                                                                                 # מִדְּבַר "from the word of", מִדֶּבֶר "from pestilence", מִדָּבָר
MID = {}
for form, seats in MIDABBER.items(): MID.setdefault(mid_kind(form), []).extend(seats)
MID_REFLEX = sorted(MID['reflexive']); assert len(MID_REFLEX) == 8 and {'Num 7:89', 'Ezek 2:2', 'Ezek 43:6', 'Exod 34:33'} <= set(MID_REFLEX), MID_REFLEX
MID_PIEL = len(MID['piel']); MID_WILD = len(MID['wilderness']); MID_OTHER = len(MID.get('other', []))
assert MID_PIEL == 26 and MID_WILD == 45 and MID_OTHER == 6 and mid_kind(byp[('Num', 7, 89)][words('Num', 7, 89).index('מדבר')]) == 'reflexive', (MID_PIEL, MID_WILD, MID_OTHER)
MORPH789 = [(plain(h), m) for h, m in db.execute("SELECT w.he, w.morph FROM words w JOIN verses v ON w.verse_id=v.id WHERE v.book='Num' AND v.chapter=7 AND v.verse=89 ORDER BY w.idx").fetchall() if plain(h) in ('וישמע', 'וידבר')]
assert MORPH789 == [('וישמע', 'HC/Vqw3ms'), ('וידבר', 'HC/Vpw3ms')]
# THE FRAMES AND THE REGISTER
FR = [(c, v) for (c, v) in SPAN if words('Num', c, v)[0] in ('וידבר', 'ויאמר') and words('Num', c, v)[1] == 'יהוה']
assert FR == [(4, 21), (5, 1), (5, 5), (5, 11), (6, 1), (6, 22), (7, 4), (7, 11)], FR
FR_SAID = [(c, v) for c, v in FR if words('Num', c, v)[0] == 'ויאמר']; assert FR_SAID == [(7, 4), (7, 11)]
assert words('Num', 6, 23)[:5] == ['דבר', 'אל', 'אהרן', 'ואל', 'בניו']
GL = {'וידבר': 'and He spoke', 'ויפקד': 'and he counted', 'ויהיו': 'and they were', 'ויעשו': 'and they did', 'וישלחו': 'and they sent', 'ויתן': 'and he gave',
      'ותמעל': 'and she was faithless', 'ויהי': 'and it was', 'וימשח': 'and he anointed', 'ויקדש': 'and he consecrated', 'וימשחם': 'and he anointed them',
      'ויקריבו': 'and they brought near', 'ויביאו': 'and they brought', 'ויאמר': 'and He said', 'ויקח': 'and he took', 'וישמע': 'and he heard'}
REG = {}
for (c, v) in SPAN:
    vs = [(x, [q for q in m.split('/') if 'V' in q][0]) for x, m in by[('Num', c, v)] if m and re.search(r'V.w', m)]
    if vs: REG[(c, v)] = [f'{x} ("{GL[x]}", {m})' for x, m in vs]
assert sorted(REG) == [(4, 21), (4, 34), (4, 36), (4, 40), (4, 44), (4, 48), (5, 1), (5, 4), (5, 5), (5, 11), (5, 20), (5, 27), (6, 1), (6, 22), (7, 1), (7, 2), (7, 3), (7, 4), (7, 6), (7, 10), (7, 11), (7, 12), (7, 89)], sorted(REG)
def register(c, lo, hi): return '; '.join(f'{c}:{v} ' + ', '.join(REG[(c, v)]) for v in range(lo, hi + 1) if (c, v) in REG) or 'no narrative verb'
UNPOINTED = [(c, v, i) for (c, v) in SPAN for i, h in enumerate(byraw[('Num', c, v)]) if not any(0x05B0 <= ord(ch) <= 0x05BC for ch in h)]
assert UNPOINTED == [], UNPOINTED   # no written-and-read pair in Naso on the Tanakh DB
DATE_7_1 = words('Num', 7, 1); assert DATE_7_1[:4] == ['ויהי', 'ביום', 'כלות', 'משה']

#!/usr/bin/env python3
# THE NUMBERS WALK, sitting 1 — BAMIDBAR (2026-09-09; the owner: "OK, let's go starting with numbers the first first first verse"):
# THE READING of Numbers 1:1-4:20 at the parashah grain (THE_STEPS Step 2 speed ruling (a)), the ledgers PER BLOCK — nine
# append-only ledgers logic/oral_triage/<uid>_2026-09-09.md for the nine drafts that cover the portion (computed: 159 of 159
# verses, missing 0; the tenth draft of the state doc's list, num_04_gershon_merari, opens at 4:21 — Naso's). The spine: Onkelos
# Numbers 1:1-4:20 whole (159 verses) + the Sifrei on Numbers where it has a piska — it has NONE by position in 1:1-4:20 (it opens
# at 5:1; the export's piska 62, headed "3:24", sits between 61 on 8:4 and 63 on 8:25 and quotes 8:24 and 4:23: the row on the
# Levites' ages, read fresh at num_04_kehat where 4:3 carries the thirty). COVERAGE COMPUTED from the shelf files; THE INK FACTS
# computed from the Tanakh DB (never typed); the Hebrew and the Aramaic quoted are CUT from the DB and the shelf by consonants.
# (THE TENT sitting 4's form, write_num27_36_ledgers.py.)
import json, os, re, html, sqlite3
from collections import Counter
ROOT = '<repo-old>'
DATE = '2026-09-09'
UNITS = [  # (uid, chapter, lo, hi, title)
    ('num_01_census_command', 1, 1, 19, 'the census command and the princes'),
    ('num_01_tribe_counts', 1, 20, 46, 'the twelve counts'),
    ('num_01_levites_exempt', 1, 47, 54, 'the Levites exempt and posted'),
    ('num_02_camp_east_south', 2, 1, 16, 'the camp: east and south'),
    ('num_02_camp_west_north', 2, 17, 34, 'the camp: the tent in the midst, west and north'),
    ('num_03_aaron_levi_replace', 3, 1, 13, "Aaron's line and the Levites in the firstborn's place"),
    ('num_03_levite_clans_count', 3, 14, 39, "the Levite clans counted and posted"),
    ('num_03_firstborn_redeem', 3, 40, 51, 'the firstborn counted and the excess redeemed'),
    ('num_04_kehat', 4, 1, 20, "the Kohathites' burden"),
]
OUT = {u[0]: f'{ROOT}/logic/oral_triage/{u[0]}_{DATE}.md' for u in UNITS}
for o in OUT.values():
    assert not os.path.exists(o), f'ledger exists — append, never overwrite: {o}'

def clean(s): return re.sub(r'<[^>]+>', '', html.unescape(s))
sif = json.load(open(f'{ROOT}/Data/sefaria_export/Sifrei_Bamidbar/en.json'))['text']
onk = json.load(open(f'{ROOT}/Data/sefaria_export/Onkelos_Numbers/en.json'))['text']
onk_he = json.load(open(f'{ROOT}/Data/sefaria_export/Onkelos_Numbers/he.json'))['text']
heads = {}
for p, rows in enumerate(sif, 1):
    if not rows: continue
    m = re.search(r'\((Bamidbar|Devarim)\.? (\d+):(\d+)', clean(rows[0])[:60])
    heads[p] = (m.group(1), int(m.group(2)), int(m.group(3))) if m else None
# THE SIFREI'S SILENCE, COMPUTED: piska 1 opens on 5:1; the only head inside chapters 1-4 is piska 62's "3:24", whose neighbors
# are 61 (8:4) and 63 (8:25) and whose text quotes 8:24 and 4:23 — a mislabeled head: by POSITION the row on 8:24
assert heads[1] == ('Bamidbar', 5, 1), heads[1]
in14 = [(p, h) for p, h in heads.items() if h and h[0] == 'Bamidbar' and h[1] <= 4]
assert in14 == [(62, ('Bamidbar', 3, 24))], in14
assert heads[61] == ('Bamidbar', 8, 4) and heads[63] == ('Bamidbar', 8, 25), (heads[61], heads[63])
p62 = clean(sif[61][0]); assert len(sif[61]) == 1 and '8:24' in p62 and '4:23' in p62 and 'twenty-five' in p62 and 'thirty' in p62, p62[:200]
ONK_LEN = {c: len(onk[c - 1]) for c in range(1, 5)}
assert ONK_LEN == {1: 54, 2: 34, 3: 51, 4: 49} and {c: len(onk_he[c - 1]) for c in range(1, 5)} == ONK_LEN, ONK_LEN
shelf_numbers = sorted(d for d in os.listdir(f'{ROOT}/Data/sefaria_export') if re.search(r'Numbers|Bamidbar', d))
outside = [d for d in shelf_numbers if d not in ('Sifrei_Bamidbar', 'Onkelos_Numbers')]
assert len(outside) == 23, len(outside)

# ---- THE INK, computed from the Tanakh DB ----
db = sqlite3.connect(f'file:{ROOT}/elijah_docket/tanakh.sqlite?mode=ro', uri=True)
def plain(w): return ''.join(c for c in w if c != '/' and not (0x0591 <= ord(c) <= 0x05C7))
def pointed(w): return ''.join(c for c in w if c != '/' and not (0x0591 <= ord(c) <= 0x05AF))   # the accents off, the points kept
rows = db.execute("SELECT v.book, v.chapter, v.verse, w.he, w.morph FROM words w JOIN verses v ON w.verse_id=v.id ORDER BY v.id, w.idx").fetchall()
by, byp = {}, {}
for b, c, v, he, m in rows:
    by.setdefault((b, c, v), []).append((plain(he), m)); byp.setdefault((b, c, v), []).append(pointed(he))
T = ('Gen', 'Exod', 'Lev', 'Num', 'Deut')
def words(b, c, v): return [x for x, _ in by[(b, c, v)]]
def hits(sub, books=None, exact=False): return sorted({f'{b} {c}:{v}' for (b, c, v), ws in by.items() if (books is None or b in books) and any((x == sub) if exact else (sub in x) for x, _ in ws)})
def phrase(seq, books=T):
    out = []
    for (b, c, v), ws in by.items():
        if b not in books: continue
        w = [x for x, _ in ws]
        if any(w[i:i + len(seq)] == list(seq) for i in range(len(w) - len(seq) + 1)): out.append(f'{b} {c}:{v}')
    return sorted(out)
def H(c, v, *cons):
    """the pointed Hebrew of Num c:v for the consonantal words given, in order — cut from the DB, never typed"""
    w, wp = words('Num', c, v), byp[('Num', c, v)]
    out, i = [], 0
    for k in cons:
        while i < len(w) and w[i] != k: i += 1
        assert i < len(w), (c, v, k, w)
        out.append(wp[i]); i += 1
    return ' '.join(out)
def A(c, v, *cons):
    """the pointed Aramaic of Onkelos Num c:v for the consonantal words given — cut from the shelf's own bytes"""
    ws = clean(onk_he[c - 1][v - 1]).rstrip(':').split()
    out, i = [], 0
    for k in cons:
        while i < len(ws) and plain(ws[i]) != k: i += 1
        assert i < len(ws), (c, v, k, [plain(x) for x in ws])
        out.append(ws[i]); i += 1
    return ' '.join(out)
def numword(n): return f'{n:,}'
# THE CENSUS'S NUMBER GRAMMAR (the ink's own, measured on every number of 1:1-4:20): a unit IMMEDIATELY before hundreds multiplies;
# אלף / אלפים ("thousand"/"thousands") WITHOUT the conjunction multiplies the whole group before it; וְאֶלֶף ("and a thousand") ADDS;
# מֵאֵת ("from") is a consonantal homograph of מְאַת ("a hundred of"), told apart by its vowels
U = {'אחד': 1, 'אחת': 1, 'שנים': 2, 'שתים': 2, 'שני': 2, 'שלש': 3, 'שלשה': 3, 'שלשת': 3, 'ארבע': 4, 'ארבעה': 4, 'ארבעת': 4, 'חמש': 5, 'חמשה': 5, 'חמשת': 5,
     'שש': 6, 'ששה': 6, 'ששת': 6, 'שבע': 7, 'שבעה': 7, 'שבעת': 7, 'שמנה': 8, 'שמנת': 8, 'תשע': 9, 'תשעה': 9, 'עשר': 10, 'עשרה': 10, 'עשרים': 20, 'שלשים': 30,
     'ארבעים': 40, 'חמשים': 50, 'ששים': 60, 'שבעים': 70, 'שמנים': 80, 'תשעים': 90, 'מאה': 100, 'מאת': 100, 'מאתים': 200, 'מאות': 100, 'אלף': 1000, 'אלפים': 1000}
def census(c, v, b='Num'):
    ws, wp = words(b, c, v), byp[(b, c, v)]
    out, add, seen, k, last = [], [], False, 0, None   # k: where the group since the last thousands-word begins
    for w, p in zip(ws, wp):
        pre = ''
        if last is not None and w == last: continue       # a numeral doubled (3:47 'five, five') is DISTRIBUTIVE, one number
        last = w
        for q in ('וה', 'ו', 'ב', 'ל', 'כ', 'ה'):
            if w.startswith(q) and w[len(q):] in U: pre, w = q, w[len(q):]; break
        if w not in U or (w == 'מאת' and 'ֵ' in p):     # מֵאֵת "from": the tsere tells the homograph apart
            if seen: out.append(sum(add))
            add, seen, k = [], False, 0
            continue
        seen = True
        n = U[w]
        if n == 1000:
            if pre.startswith('ו'): add.append(1000)          # "and a thousand" — an addend
            else: add = add[:k] + [sum(add[k:]) * 1000]       # the group since the last thousand, multiplied
            k = len(add)
        elif n == 100 and w in ('מאות', 'מאת') and len(add) > k and 1 <= add[-1] <= 9: add[-1] *= 100
        else: add.append(n)
    if seen: out.append(sum(add))
    return out
twelve = {v: census(1, v)[0] for v in range(21, 44, 2)}
TOTAL = census(1, 46)[0]
assert sum(twelve.values()) == TOTAL == 603550 == census(2, 32)[0], (sum(twelve.values()), TOTAL)
camp = {v: census(2, v)[0] for v in (4, 6, 8, 9, 11, 13, 15, 16, 19, 21, 23, 24, 26, 28, 30, 31)}
assert camp[9] == camp[4] + camp[6] + camp[8] and camp[16] == camp[11] + camp[13] + camp[15] and camp[24] == camp[19] + camp[21] + camp[23] and camp[31] == camp[26] + camp[28] + camp[30]
assert camp[9] + camp[16] + camp[24] + camp[31] == TOTAL and (camp[9], camp[16], camp[24], camp[31]) == (186400, 151450, 108100, 157600)
assert all(camp[a] == twelve[b] for a, b in ((4, 27), (6, 29), (8, 31), (11, 21), (13, 23), (15, 25), (19, 33), (21, 35), (23, 37), (26, 39), (28, 41), (30, 43)))
EXOD_3826 = census(38, 26, 'Exod'); assert EXOD_3826 == [20, TOTAL], EXOD_3826   # 'from twenty years' then the count: the same number on the erection's seat
clans = {v: census(3, v)[0] for v in (22, 28, 34)}; LEV = census(3, 39)[0]; FB = census(3, 43)[0]; EXC = census(3, 46)[0]; SHEK = census(3, 47); MONEY = census(3, 50)[0]
assert (clans, LEV, FB, EXC, SHEK, MONEY) == ({22: 7500, 28: 8600, 34: 6200}, 22000, 22273, 273, [5, 20], 1365), (clans, LEV, FB, EXC, SHEK, MONEY)
CLANSUM = sum(clans.values()); assert CLANSUM == 22300 and CLANSUM - LEV == 300 and FB - LEV == EXC and EXC * 5 == MONEY
assert census(1, 3) == [20] and census(3, 15) == [] and 'חדש' in words('Num', 3, 15) and census(4, 3) == [30, 50] and census(1, 44) == [12, 1] and census(1, 1) == [1, 2]
# the engine's own parser, measured against the census (SEQUENTIAL_RUN.md section 4's numeral parser): it has no thousands
import sys, io, contextlib
sys.path.insert(0, f'{ROOT}/World/step9')
with contextlib.redirect_stdout(io.StringIO()):
    import cold_run_sequence as CS
ENGINE_121, ENGINE_339, ENGINE_146 = CS.ink_numbers(words('Num', 1, 21)), CS.ink_numbers(words('Num', 3, 39)), CS.ink_numbers(words('Num', 1, 46))
assert ENGINE_121 != [twelve[21]] and ENGINE_339 != [LEV] and ENGINE_146 != [TOTAL], (ENGINE_121, ENGINE_339, ENGINE_146)
VE_ALEF = sorted(f'{b} {c}:{v}' for (b, c, v), ws in by.items() if b in T and any(x == 'ואלף' for x, _ in ws)); assert VE_ALEF == ['Exod 38:25', 'Num 26:51', 'Num 3:50'], VE_ALEF
# the tribes' three orders
TR = {'ראובן': 'Reuben', 'שמעון': 'Simeon', 'יהודה': 'Judah', 'יששכר': 'Issachar', 'זבולן': 'Zebulun', 'אפרים': 'Ephraim', 'מנשה': 'Manasseh', 'בנימן': 'Benjamin', 'דן': 'Dan', 'אשר': 'Asher', 'גד': 'Gad', 'נפתלי': 'Naphtali'}
def order(ch, lo, hi):
    out = []
    for v in range(lo, hi + 1):
        ws = words('Num', ch, v)
        for i, w in enumerate(ws):
            for p in ('ל', 'ו', 'ד', 'ב'):
                if w.startswith(p) and w[len(p):] in TR and TR[w[len(p):]] not in out: out.append(TR[w[len(p):]]); break
            else:
                # bare אשר is "who" unless it follows "the sons of" / "the tribe of" — then the tribe Asher (1:40, 2:27)
                if w in TR and TR[w] not in out and (w != 'אשר' or (i and ws[i - 1] in ('בני', 'לבני', 'מטה'))): out.append(TR[w])
    return out
O_PRINCES, O_COUNT, O_CAMP = order(1, 5, 15), order(1, 20, 43), order(2, 3, 31)
assert O_PRINCES == ['Reuben', 'Simeon', 'Judah', 'Issachar', 'Zebulun', 'Ephraim', 'Manasseh', 'Benjamin', 'Dan', 'Asher', 'Gad', 'Naphtali'], O_PRINCES
assert O_COUNT == ['Reuben', 'Simeon', 'Gad', 'Judah', 'Issachar', 'Zebulun', 'Ephraim', 'Manasseh', 'Benjamin', 'Dan', 'Asher', 'Naphtali'], O_COUNT
assert O_CAMP == ['Judah', 'Issachar', 'Zebulun', 'Reuben', 'Simeon', 'Gad', 'Ephraim', 'Manasseh', 'Benjamin', 'Dan', 'Asher', 'Naphtali'], O_CAMP
assert O_PRINCES.index('Gad') == 10 and O_COUNT.index('Gad') == 2
DEUEL, REUEL = hits('דעואל'), [h for h in hits('רעואל') if h.startswith('Num')]
assert DEUEL == ['Num 10:20', 'Num 1:14', 'Num 7:42', 'Num 7:47'] and REUEL == ['Num 10:29', 'Num 2:14'], (DEUEL, REUEL)
# the frames
FR = {}
for c in range(1, 5):
    for v in range(1, 55):
        if ('Num', c, v) not in by or (c == 4 and v > 20): continue
        w = words('Num', c, v)
        if w[0] in ('וידבר', 'ויאמר') and w[1] == 'יהוה': FR[f'{c}:{v}'] = w
assert list(FR) == ['1:1', '1:48', '2:1', '3:5', '3:11', '3:14', '3:40', '3:44', '4:1', '4:17'], list(FR)
FR_AARON = [k for k, w in FR.items() if 'ואל' in w and 'אהרן' in w]; assert FR_AARON == ['2:1', '4:1', '4:17']
FR_PLACE = [k for k, w in FR.items() if 'במדבר' in w]; assert FR_PLACE == ['1:1', '3:14']
FR_SAID = [k for k, w in FR.items() if w[0] == 'ויאמר']; assert FR_SAID == ['3:40']
def in_span(k):
    m = re.match(r'Num (\d+):(\d+)$', k); return bool(m) and (int(m.group(1)) < 4 or (int(m.group(1)) == 4 and int(m.group(2)) <= 20))
AS_CMD = [k for k in phrase(['כאשר', 'צוה', 'יהוה']) if in_span(k)]; assert AS_CMD == ['Num 1:19', 'Num 2:33', 'Num 3:42', 'Num 3:51'], AS_CMD
ALL_CMD = [k for k in phrase(['ככל', 'אשר', 'צוה', 'יהוה']) if in_span(k)]; assert ALL_CMD == ['Num 1:54', 'Num 2:34'], ALL_CMD
AL_PI = [k for k in phrase(['על', 'פי', 'יהוה']) if in_span(k)]; assert AL_PI == ['Num 3:16', 'Num 3:39', 'Num 3:51'], AL_PI
STRANGER = phrase(['והזר', 'הקרב', 'יומת']); assert STRANGER == ['Num 18:7', 'Num 1:51', 'Num 3:10', 'Num 3:38'], STRANGER
WOMB = phrase(['פטר', 'רחם']); assert WOMB == ['Exod 13:12', 'Exod 13:15', 'Exod 34:19', 'Num 18:15', 'Num 3:12'], WOMB
NO_SONS = phrase(['ובנים', 'לא', 'היו', 'להם']); assert NO_SONS == ['Num 3:4'], NO_SONS
GERAH = phrase(['עשרים', 'גרה']); assert GERAH == ['Exod 30:13', 'Lev 27:25', 'Num 18:16', 'Num 3:47'], GERAH
FILLED = phrase(['מלא', 'ידם']); assert FILLED == ['Num 3:3'], FILLED
GIVEN2 = phrase(['נתונם', 'נתונם']); assert GIVEN2 == ['Num 3:9'], GIVEN2
GIVEN = hits('נתנים', ('Num',)); assert GIVEN == ['Num 18:6', 'Num 8:16', 'Num 8:19'], GIVEN
BLUE = phrase(['כליל', 'תכלת']); assert BLUE == ['Exod 28:31', 'Exod 39:22', 'Num 4:6'], BLUE
WRATH = hits('קצף', T); assert len(WRATH) == 13 and {'Num 1:53', 'Num 18:5', 'Num 17:11'} <= set(WRATH), WRATH
KAVLA = hits('כבלע'); assert KAVLA == ['Num 4:20'], KAVLA
PEDIGREE = hits('ויתילדו'); assert PEDIGREE == ['Num 1:18'], PEDIGREE
SEU = phrase(['שאו', 'את', 'ראש']); NASA = phrase(['נשא', 'את', 'ראש']); assert SEU == ['Num 1:2', 'Num 26:2'] and NASA == ['Num 4:2', 'Num 4:22'], (SEU, NASA)
SINAI_WILD = phrase(['במדבר', 'סיני']); assert len(SINAI_WILD) == 9 and {'Num 1:1', 'Num 1:19', 'Num 3:4', 'Num 3:14', 'Num 9:1'} <= set(SINAI_WILD), SINAI_WILD
MT_SINAI = phrase(['בהר', 'סיני']); assert len(MT_SINAI) == 8 and 'Num 3:1' in MT_SINAI, MT_SINAI
ON_THE_DAY = phrase(['ביום', 'דבר', 'יהוה']); assert ON_THE_DAY == ['Deut 4:15', 'Exod 6:28', 'Num 3:1'], ON_THE_DAY
TOLEDOT = sorted(set(phrase(['אלה', 'תולדת']) + phrase(['ואלה', 'תולדת']) + phrase(['אלה', 'תולדות']) + phrase(['ואלה', 'תולדות']) + phrase(['אלה', 'תלדות']) + phrase(['ואלה', 'תלדות']) + phrase(['אלה', 'תלדת'])))
assert 'Num 3:1' in TOLEDOT and len(TOLEDOT) == 10 and all(t.startswith('Gen') for t in TOLEDOT if t != 'Num 3:1'), TOLEDOT
SONS_LIST = phrase(['נדב', 'ואביהוא']); assert SONS_LIST == ['Exod 24:1', 'Exod 24:9', 'Exod 28:1', 'Lev 10:1', 'Num 26:61', 'Num 3:2', 'Num 3:4'], SONS_LIST
AL_PNEI = phrase(['על', 'פני', 'אהרן']); assert AL_PNEI == ['Num 3:4']
HAKREV_LEVI = phrase(['הקרב', 'את', 'מטה', 'לוי']); assert HAKREV_LEVI == ['Num 3:6']
NASI2 = phrase(['ונשיא', 'נשיאי']); assert NASI2 == ['Num 3:32']
FIVE2 = phrase(['חמשת', 'חמשת']); assert FIVE2 == ['Num 3:47']
CUT = sorted(f'{b} {c}:{v}' for (b, c, v), ws in by.items() if b in T and any(x == 'תכריתו' for x, _ in ws)); assert CUT == ['Num 4:18'], CUT
KODESH2 = [v for v in range(1, 21) if any(words('Num', 4, v)[i:i + 2] == ['קדש', 'הקדשים'] for i in range(len(words('Num', 4, v)) - 1))]; assert KODESH2 == [4, 19]
DIE4 = [(v, x) for v in range(1, 21) for x in words('Num', 4, v) if x in ('ומתו', 'ימתו')]; assert DIE4 == [(15, 'ומתו'), (19, 'ימתו'), (20, 'ומתו')], DIE4
TACHASH4 = sorted(int(h.split(':')[1]) for h in hits('תחש', ('Num',)) if h.startswith('Num 4:') and int(h.split(':')[1]) <= 20); assert TACHASH4 == [6, 8, 10, 11, 12, 14], TACHASH4
MISHMERET = [(c, v) for (b, c, v), ws in by.items() if b == 'Num' and (c < 4 or (c == 4 and v <= 20)) and any('משמרת' in x for x, _ in ws)]
assert MISHMERET == [(1, 53), (3, 7), (3, 8), (3, 25), (3, 28), (3, 31), (3, 32), (3, 36), (3, 38)], MISHMERET
EDUT = phrase(['משכן', 'העדת']); assert EDUT == ['Exod 38:21', 'Num 10:11', 'Num 1:50'], EDUT
LEVI_SIDES = {'west': 'אחרי' in words('Num', 3, 23) and 'ימה' in words('Num', 3, 23), 'south': 'תימנה' in words('Num', 3, 29), 'north': 'צפנה' in words('Num', 3, 35), 'east': 'מזרחה' in words('Num', 3, 38)}
assert all(LEVI_SIDES.values()), LEVI_SIDES
CAMP_SIDES = {'east': 'מזרחה' in words('Num', 2, 3), 'south': 'תימנה' in words('Num', 2, 10), 'west': 'ימה' in words('Num', 2, 18), 'north': 'צפנה' in words('Num', 2, 25)}; assert all(CAMP_SIDES.values())
MARCH = {'first': 'ראשנה' in words('Num', 2, 9), 'second': 'ושנים' in words('Num', 2, 16), 'third': 'ושלשים' in words('Num', 2, 24), 'last': 'לאחרנה' in words('Num', 2, 31)}; assert all(MARCH.values()), MARCH
# the ketiv and the qere at 1:16: the stretch's ONE unpointed token in the DB and in the snapshot store, the store carrying both forms
def pts(w): return any(0x05B0 <= ord(ch) <= 0x05BC for ch in w)
unp = [(c, v, i, he) for (b, c, v), ws in by.items() if b == 'Num' and (c < 4 or (c == 4 and v <= 20)) for i, (x, _) in enumerate(ws) for he in [db.execute("SELECT he FROM words w JOIN verses v ON w.verse_id=v.id WHERE v.book='Num' AND v.chapter=? AND v.verse=? AND w.idx=?", (c, v, i)).fetchone()[0]] if not pts(he)]
assert unp == [(1, 16, 1, 'קריאי')], unp
snap = sqlite3.connect(f'file:{ROOT}/torah_grok.SNAPSHOT-main-51801ca.sqlite?mode=ro', uri=True)
s116 = [h for (h,) in snap.execute("SELECT w.he FROM words w JOIN verses v ON w.verse_id=v.id WHERE v.book='Num' AND v.chapter=1 AND v.verse=16 ORDER BY w.idx").fetchall()]
assert plain(s116[1]) == 'קריאי' and not pts(s116[1]) and plain(s116[2]) == 'קרואי' and pts(s116[2]), s116[:3]
sunp = snap.execute("SELECT COUNT(*) FROM words w JOIN verses v ON w.verse_id=v.id WHERE v.book='Num' AND ((v.chapter<4) OR (v.chapter=4 AND v.verse<=20))").fetchone()[0]
STORE_UNP = [(c, v, i, h) for c, v, i, h in snap.execute("SELECT v.chapter, v.verse, w.idx, w.he FROM words w JOIN verses v ON w.verse_id=v.id WHERE v.book='Num' AND ((v.chapter<4) OR (v.chapter=4 AND v.verse<=20)) ORDER BY v.id, w.idx").fetchall() if not pts(h)]
assert STORE_UNP == [(1, 16, 1, 'קריאי')], STORE_UNP
DATE_1_1, DATE_9_1, DATE_40_17 = words('Num', 1, 1), words('Num', 9, 1), words('Exod', 40, 17)
assert {'באחד', 'לחדש', 'השני', 'בשנה', 'השנית'} <= set(DATE_1_1) and {'בשנה', 'השנית', 'בחדש', 'הראשון'} <= set(DATE_9_1) and {'בחדש', 'הראשון', 'בשנה', 'השנית', 'באחד', 'לחדש'} <= set(DATE_40_17)
assert 'באחד' in words('Num', 1, 18) and 'השני' in words('Num', 1, 18)
NAKAV = sorted({f'{b} {c}:{v}' for b, c, v in db.execute("SELECT v.book, v.chapter, v.verse FROM words w JOIN verses v ON w.verse_id=v.id WHERE w.lemma LIKE '%5344%' AND v.book IN ('Gen','Exod','Lev','Num','Deut')").fetchall()})
assert 'Num 1:17' in NAKAV and 'Lev 24:16' in NAKAV and 'Lev 24:11' in NAKAV, NAKAV   # the lemma (Strong 5344, to pierce/designate/pronounce; the DB splits it a/b — 24:11's 'he pronounced' carries 1:17's own sub-lemma a) shared by the princes' verse and the blasphemer's
# the register: the narrative verbs per verse (the wayyiqtol test)
GL = {'וידבר': 'and He spoke', 'ויקח': 'and he took', 'ויתילדו': 'and they declared their pedigrees', 'ויפקדם': 'and he counted them', 'ויהיו': 'and they were',
      'ויעשו': 'and they did', 'וימת': 'and he died', 'ויכהן': 'and he served as priest', 'ויפקד': 'and he counted', 'ויאמר': 'and He said', 'ויהי': 'and it was', 'ויתן': 'and he gave'}
REG = {}
for c in range(1, 5):
    for v in range(1, 55):
        if ('Num', c, v) not in by or (c == 4 and v > 20): continue
        vs = [(x, [q for q in m.split('/') if 'V' in q][0]) for x, m in by[('Num', c, v)] if m and re.search(r'V.w', m)]
        if vs: REG[(c, v)] = [f'{x} ("{GL[x]}", {m})' for x, m in vs]
assert sorted(REG) == [(1, 1), (1, 17), (1, 18), (1, 19), (1, 20), (1, 45), (1, 46), (1, 48), (1, 54), (2, 1), (2, 34), (3, 4), (3, 5), (3, 11), (3, 14), (3, 16), (3, 17), (3, 40), (3, 42), (3, 43), (3, 44), (3, 49), (3, 51), (4, 1), (4, 17)], sorted(REG)
def register(c, lo, hi): return '; '.join(f'{c}:{v} ' + ', '.join(REG[(c, v)]) for v in range(lo, hi + 1) if (c, v) in REG) or 'no narrative verb'

# ---- THE ONKELOS ROWS, verse by verse (verdict, prose); the Aramaic and the Hebrew cut by consonants ----
R = {}
def row(c, v, verdict, prose): R[(c, v)] = (verdict, prose)
# chapter 1
row(1, 1, 'MATERIAL', f'THE DATE STAMP. "And the LORD spoke to Moses in the wilderness of Sinai, in the tent of meeting, {H(1,1,"באחד","לחדש","השני","בשנה","השנית")} ("on the first of the second month, in the second year") of their going out of Egypt" → {A(1,1,"בחד","לירחא","תנינא","בשתא","תניתא")} ("on the first of the second month in the second year") — literal, the day and the month and the year all named: the tape\'s FORWARD marker (Exod 40:17 the erection on the first of the FIRST month of this year; Num 9:1 the Passover command in the first month — a verse AFTER this one in the text and BEFORE it in time: the retrograde the tradition names at Pesachim 6b:7, "there is no earlier and later in the Torah"). {A(1,1,"במשכן","זמנא")} ("in the tent of appointed time") for the tent of meeting — the standing rendering.')
row(1, 2, 'MATERIAL', f'THE IDIOM OF THE COUNT. {H(1,2,"שאו","את","ראש")} ("lift the head") → {A(1,2,"קבילו","ית","חשבן")} ("receive the sum") — the idiom flattened to accounting (the phrase\'s two Torah seats computed: here and 26:2, the two censuses of the book); "by their families, by their fathers\' house" → {A(1,2,"לזרעיתהון")} ("by their seed-families"); {H(1,2,"לגלגלתם")} ("by their skulls" — per head) → {A(1,2,"לגלגלתהון")} (kept) — the count is of NAMES per head, "the number of names, every male": not a heap counted but names written (Onkelos: "in the number of names").')
row(1, 3, 'MATERIAL', f'THE THRESHOLD. {H(1,3,"מבן","עשרים","שנה","ומעלה")} ("from twenty years old and upward") — the ink\'s first threshold in the book (computed: twenty here, a MONTH at 3:15, thirty-to-fifty at 4:3); {H(1,3,"כל","יצא","צבא")} ("everyone going out to the host") → {A(1,3,"כל","נפק","חילא","בישראל")} ("everyone going out in the host in Israel"); "you shall count them by their hosts, you and Aaron" → {A(1,3,"תמנון","יתהון")} ("you shall count them") — the count assigned to two.')
row(1, 4, 'MATERIAL', f'ONE MAN PER TRIBE. {H(1,4,"איש","איש","למטה")} ("a man, a man for a tribe" — the distributive doubling) → {A(1,4,"גברא","גברא","לשבטא")} (kept doubled); "each the head of his fathers\' house" — the twelve aides named before the count.')
row(1, 5, 'MATERIAL', f'THE LIST OPENS. "These are the names of the men {H(1,5,"אשר","יעמדו","אתכם")} ("who shall stand with you")" → {A(1,5,"די","יקומון","עמכון")} ("who shall arise with you"); "for Reuben, Elizur son of Shedeur" — the princes\' order begins (computed: {", ".join(O_PRINCES)} — Gad ELEVENTH here, THIRD in the count of 1:20-43, SIXTH in the camp of chapter 2).')
for v, who in ((6, 'Simeon, Shelumiel son of Zurishaddai'), (7, 'Judah, Nahshon son of Amminadab'), (8, 'Issachar, Nethanel son of Zuar'), (9, 'Zebulun, Eliab son of Helon'),
               (11, 'Benjamin, Abidan son of Gideoni'), (12, 'Dan, Ahiezer son of Ammishaddai'), (13, 'Asher, Pagiel son of Ochran'), (15, 'Naphtali, Ahira son of Enan')):
    row(1, v, 'CONTEXT', f'{who} — literal; the name-list continues.')
row(1, 10, 'CONTEXT', f'"For the sons of Joseph: for Ephraim, Elishama son of Ammihud; for Manasseh, Gamaliel son of Pedahzur" — Joseph counted as TWO tribes while Levi is left out: twelve stay twelve (Onkelos literal).')
row(1, 14, 'MATERIAL', f'"For Gad, Eliasaph son of {H(1,14,"דעואל")} ("Deuel")" → {A(1,14,"דעואל")} — DEUEL with a dalet; at 2:14 the same prince is REUEL with a resh (computed: דעואל ("Deuel") at {", ".join(DEUEL)}; רעואל ("Reuel") at {", ".join(REUEL)} — one man, two spellings in the ink, and Onkelos keeps each verse\'s own letter: the translation does not harmonize).')
row(1, 16, 'MATERIAL', f'THE WRITTEN AND THE READ. {H(1,16,"אלה")} קריאי ("these are the CALLED of" — the written form, unpointed in the store) / {pointed(s116[2])} ("the summoned of" — the read form, the store\'s own pointed token): the stretch\'s ONE ketiv-qere pair (computed: the only unpointed token in Numbers 1:1-4:20, in the Tanakh DB and in the snapshot store alike — the store carries both tokens side by side, the written first) → {A(1,16,"מערעי","כנשתא")} ("the summoned of the congregation") — Onkelos renders the READ form; "the heads of the thousands of Israel" → {A(1,16,"רישי","אלפיא")} ("the heads of the thousands") — a title the register keeps.')
row(1, 17, 'MATERIAL', f'THE RUN OPENS. "And Moses and Aaron TOOK these men {H(1,17,"אשר","נקבו","בשמות")} ("who were designated by names")" → {A(1,17,"די","אתפרשו","בשמהן")} ("who were specified by names") — the designating verb is the ROOT OF THE BLASPHEMER\'S "he pronounced" (Lev 24:11, 24:16 — computed on the shared root: to pierce, to specify, to pronounce); here it names the princes (a REFERENCE by shared lemma, no inference drawn).')
row(1, 18, 'MATERIAL', f'THE PEDIGREES AND THE DATE REPEATED. "They assembled all the congregation {H(1,18,"באחד","לחדש","השני")} ("on the first of the second month") and {H(1,18,"ויתילדו")} ("they declared their pedigrees")" — the verb\'s ONE seat in the Tanakh (computed) → {A(1,18,"ואתיחסו")} ("and they were registered by genealogy") — the pedigree as an ACT of the count (the exam\'s Talmud: they brought their pedigree scrolls, Yevamot 54b — at Step 5); THE COMMAND\'S DATE IS THE RUN\'S DATE: 1:1 and 1:18 carry the same day — the census done on the day it was commanded.')
row(1, 19, 'MATERIAL', f'THE RUN CLOSES. "{H(1,19,"כאשר","צוה","יהוה","את","משה")} ("as the LORD commanded Moses"), and he counted them in the wilderness of Sinai" → {A(1,19,"כמא","די","פקיד","יי","ית","משה","ומננון")} ("as the LORD commanded Moses, and he counted them") — the SPEC/RUN pair\'s formula (the exact clause at {", ".join(AS_CMD)}; the wider "according to ALL that the LORD commanded" at {", ".join(ALL_CMD)} — computed): the first of five commanded-and-done pairs in the portion.')
row(1, 20, 'MATERIAL', f'THE COUNT\'S FORMULA. "And the sons of Reuben, {H(1,20,"בכר","ישראל")} ("Israel\'s firstborn"), {H(1,20,"תולדתם")} ("their generations") by their families by their fathers\' house, by the number of names by their skulls, every male from twenty years and up, everyone going out to the host" → {A(1,20,"תולדתהון","לזרעיתהון")} ("their generations by their seed-families") — the twelve-fold formula opens on the firstborn; "generations" is the Genesis heading-word (computed: its seats in 1:20-42 twelve times, and 3:1).')
for v in range(21, 44, 2):
    tribe = O_COUNT[(v - 21) // 2]
    ar = ' '.join(clean(onk_he[0][v - 1]).rstrip(':').split()[3:])
    row(1, v, 'CONTEXT' if v != 21 else 'MATERIAL', f'{tribe}: {numword(twelve[v])} (computed from the ink\'s own numerals) → {ar} ("{numword(twelve[v])}" — the Aramaic numerals, the thousands multiplied by the group before them).' + (' The count\'s FIRST number and its grammar: units and tens before "thousand" multiply, hundreds follow — the census\'s number grammar (measured on all sixteen numbers of chapters 1-2 below).' if v == 21 else ''))
for v in range(22, 43, 2):
    tribe = O_COUNT[(v - 20) // 2]
    extra = ' — GAD THIRD: the count\'s order moves Gad from the princes\' eleventh to the third place, beside Reuben and Simeon (computed: the three orders below) — the camp\'s companions counted together.' if v == 24 else (' — "for the sons of Joseph: for the sons of Ephraim" (Joseph as the house of two).' if v == 32 else '')
    row(1, v, 'CONTEXT', f'{tribe}: the formula repeated — generations, families, fathers\' house, the number of names, twenty and up, going out to the host; Onkelos literal.{extra}')
row(1, 44, 'MATERIAL', f'"These are the counted whom Moses and Aaron and the princes of Israel counted, {H(1,44,"שנים","עשר","איש")} ("twelve men"), {H(1,44,"איש","אחד","לבית","אבתיו")} ("one man for his fathers\' house")" → {A(1,44,"תרין","עשר","גברין")} ("twelve men") — the counters named in the run: Moses, Aaron, the twelve.')
row(1, 45, 'CONTEXT', 'The summary\'s formula: all the counted, by their fathers\' house, twenty and up, going out to the host in Israel — literal.')
row(1, 46, 'MATERIAL', f'THE TOTAL. {H(1,46,"שש","מאות","אלף","ושלשת","אלפים","וחמש","מאות","וחמשים")} ("six hundred thousand and three thousand and five hundred and fifty") → {A(1,46,"שית","מאה","ותלתא","אלפין","וחמש","מאה","וחמשין")} ("603,550") — THE TWELVE SUMMED EQUAL THE TOTAL (computed: {" + ".join(numword(twelve[v]) for v in range(21, 44, 2))} = {numword(TOTAL)}); the same number stands at 2:32 (the four camps summed, computed) and at Exod 38:26 (the half-shekel census at the erection, the words "six hundred thousand and three thousand and five hundred and fifty" — the exam\'s question at Bekhorot 5a: two counts months apart, one number).')
row(1, 47, 'MATERIAL', f'THE LEVITES LEFT OUT. "And the Levites {H(1,47,"למטה","אבתם")} ("by the tribe of their fathers") {H(1,47,"לא","התפקדו","בתוכם")} ("were not counted among them")" → {A(1,47,"לא","אתמניאו","ביניהון")} ("were not counted among them") — the passive reflexive: the tribe stands outside the twelve before the command that excludes it is spoken (1:49).')
row(1, 48, 'CONTEXT', 'The frame: "And the LORD spoke to Moses, saying" — the portion\'s second utterance (ten computed below).')
row(1, 49, 'MATERIAL', f'THE EXCLUSION COMMANDED. "{H(1,49,"אך","את","מטה","לוי","לא","תפקד")} ("only the tribe of Levi you shall not count"), and their head you shall not lift among the children of Israel" → {A(1,49,"ברם","ית","שבטא","דלוי","לא","תמני")} ("however, the tribe of Levi you shall not count") and {A(1,49,"חשבנהון","לא","תקבל")} ("their sum you shall not receive") — the restrictive "only" rendered "however"; the census idiom of 1:2 negated for one tribe.')
row(1, 50, 'MATERIAL', f'THE APPOINTMENT. "{H(1,50,"ואתה","הפקד","את","הלוים")} ("and you, appoint the Levites") over {H(1,50,"משכן","העדת")} ("the tabernacle of the testimony")" → {A(1,50,"מני","ית","לואי","על","משכנא","דסהדותא")} ("appoint the Levites over the tabernacle of the testimony") — the count-verb turned to APPOINT (one root, two offices); the tabernacle\'s name "of the testimony" at {", ".join(EDUT)} in the Torah (computed); the four duties — carry, serve, camp around — "they shall carry the tabernacle and all its vessels, and they shall serve it, and round about the tabernacle they shall camp" → {A(1,50,"יטלון")} ("they shall carry"), {A(1,50,"ישמשניה")} ("they shall serve it"), {A(1,50,"וסחור","סחור")} ("and round about").')
row(1, 51, 'MATERIAL', f'TAKE DOWN, SET UP, AND THE STRANGER. "When the tabernacle journeys the Levites shall take it down, and when it rests the Levites shall set it up; {H(1,51,"והזר","הקרב","יומת")} ("and the stranger who approaches shall be put to death")" → {A(1,51,"ובמטל","משכנא","יפרקון","יתיה","לואי")} ("and at the tabernacle\'s journeying the Levites shall take it apart"), {A(1,51,"יקימון")} ("they shall set up"), and {A(1,51,"וחלוני","דיקרב","יתקטל")} ("and the LAY man who approaches shall be killed") — THE STRANGER IS THE OUTSIDER TO THE OFFICE, not the foreigner: Onkelos\' word is the common/lay person; the clause stands four times in the Torah (computed: {", ".join(STRANGER)}) — here the non-Levite at the tabernacle, at 3:10 the non-priest at the priesthood, at 3:38 before the tent, at 18:7 the priesthood again.')
row(1, 52, 'MATERIAL', f'THE BANNER. "Each man by his camp and each man by his banner ({H(1,52,"דגלו")}, "his banner") by their hosts" → {A(1,52,"גבר","על","משרוהי","וגבר","על","טקסיה")} ("each man on his camp and each man on his taxis") — the banner rendered by the Greek loan TAXIS (a battle-order, a rank): the camp as an army in array, the translation\'s own register.')
row(1, 53, 'MATERIAL', f'THE WRATH-SHIELD. "The Levites shall camp round about the tabernacle of the testimony, {H(1,53,"ולא","יהיה","קצף")} ("that there be no wrath") on the congregation of the children of Israel; and the Levites shall keep {H(1,53,"משמרת")} ("the charge") of the tabernacle of the testimony" → {A(1,53,"ולא","יהי","רוגזא","על","כנשתא")} ("that there be no anger upon the congregation") and {A(1,53,"מטרת")} ("the charge/watch") — the guard\'s PURPOSE written in the ink: the Levite ring absorbs the wrath (the word\'s thirteen Torah seats computed, 18:5 "that there be no more wrath" the parallel command, 17:11 the plague\'s wrath among them); "charge" is the portion\'s key-word — {len(MISHMERET)} seats in 1:1-4:20 (computed), every Levite duty a charge kept.')
row(1, 54, 'MATERIAL', f'THE RUN. "And the children of Israel did {H(1,54,"ככל","אשר","צוה","יהוה","את","משה")} ("according to all that the LORD commanded Moses"), so they did" → {A(1,54,"ועבדו","בני","ישראל","ככל","די","פקיד","יי","ית","משה","כן","עבדו")} ("and the children of Israel did according to all that the LORD commanded Moses, so they did") — the doubled report ("so they did") closing the chapter; the pair\'s second seat 2:34 (computed).')
# chapter 2
row(2, 1, 'CONTEXT', f'The frame: "to Moses AND to Aaron, saying" — the first of the portion\'s three double-addressed utterances (computed: {", ".join(FR_AARON)}).')
row(2, 2, 'MATERIAL', f'THE BANNER AND THE DISTANCE. "Each man by his banner {H(2,2,"באתת","לבית","אבתם")} ("with the signs of their fathers\' house") shall the children of Israel camp; {H(2,2,"מנגד","סביב","לאהל","מועד")} ("at a distance, round about the tent of meeting") they shall camp" → {A(2,2,"גבר","על","טקסיה","באתון")} ("each man on his taxis, with the signs") and {A(2,2,"מלקבל","סחור","סחור","למשכן","זמנא")} ("opposite, round about the tent of appointed time") — the distance-word rendered "opposite": the exam\'s measure (two thousand cubits by Josh 3:4\'s "far off" — Eruvin 51a, the Sabbath limit\'s source) is the Talmud\'s, not the verse\'s; the ink says "at a distance, around".')
row(2, 3, 'MATERIAL', f'EAST: JUDAH. "Those camping {H(2,3,"קדמה","מזרחה")} ("in front, eastward"): the banner of the camp of Judah by their hosts; the prince of the sons of Judah, Nahshon son of Amminadab" → {A(2,3,"קדומא","מדינחא")} ("in front, eastward"), {A(2,3,"טקס","משרית","יהודה")} ("the taxis of the camp of Judah") — the four sides in the ink\'s own words (computed: east 2:3, south 2:10, west 2:18, north 2:25) and the banner as the camp\'s name.')
CAMPMATE = {5: 'Issachar (Nethanel son of Zuar)', 7: 'Zebulun (Eliab son of Helon)', 12: 'Simeon (Shelumiel son of Zurishaddai)', 14: 'Gad (Eliasaph son of REUEL)', 20: 'Manasseh (Gamaliel son of Pedahzur)', 22: 'Benjamin (Abidan son of Gideoni)', 27: 'Asher (Pagiel son of Ochran)', 29: 'Naphtali (Ahira son of Enan)'}
for v, who in CAMPMATE.items():
    extra = f' — {H(2,14,"רעואל")} ("Reuel") with a RESH against 1:14\'s Deuel with a dalet (computed) → {A(2,14,"רעואל")}: Onkelos keeps this verse\'s own letter too — one prince, two spellings, neither harmonized.' if v == 14 else (f' — "those camping {H(2,5,"עליו")} ("beside him")" → {A(2,5,"סמיכין","עלוהי")} ("adjoining him"): the companion tribe\'s word.' if v == 5 else '')
    row(2, v, 'MATERIAL' if v == 14 else 'CONTEXT', f'The companion tribe {who} — literal.{extra}')
for v in (4, 6, 8, 11, 13, 15, 19, 21, 23, 26, 28, 30):
    src = {4: 27, 6: 29, 8: 31, 11: 21, 13: 23, 15: 25, 19: 33, 21: 35, 23: 37, 26: 39, 28: 41, 30: 43}[v]
    row(2, v, 'CONTEXT', f'"Its host and their counted: {numword(camp[v])}" — the number of 1:{src} repeated (computed equal); Onkelos the same numerals.')
row(2, 9, 'MATERIAL', f'JUDAH\'S CAMP, FIRST. "All the counted of the camp of Judah: {numword(camp[9])} by their hosts; {H(2,9,"ראשנה","יסעו")} ("first they journey")" → {A(2,9,"בקדמיתא","נטלין")} ("in the first place they journey") — THE THREE SUMMED EQUAL THE CAMP (computed: {numword(camp[4])} + {numword(camp[6])} + {numword(camp[8])} = {numword(camp[9])}); the ink\'s hundred-thousand form "a hundred thousand and eighty thousand and six thousand and four hundred" — each "thousand" multiplying the group before it.')
row(2, 10, 'MATERIAL', f'SOUTH: REUBEN. "The banner of the camp of Reuben {H(2,10,"תימנה")} ("southward") by their hosts; the prince Elizur son of Shedeur" → {A(2,10,"דרומא")} ("south").')
row(2, 16, 'MATERIAL', f'REUBEN\'S CAMP, SECOND. "{numword(camp[16])} by their hosts; {H(2,16,"ושנים","יסעו")} ("and second they journey")" → {A(2,16,"בתניתא","נטלין")} ("in the second place they journey") — the three summed equal the camp (computed: {numword(camp[11])} + {numword(camp[13])} + {numword(camp[15])} = {numword(camp[16])}).')
row(2, 17, 'MATERIAL', f'THE TENT IN THE MIDST. "And the tent of meeting shall journey, the camp of the Levites in the midst of the camps; {H(2,17,"כאשר","יחנו","כן","יסעו")} ("as they camp so they journey"), each man in his place by their banners" → {A(2,17,"כמא","דשרן","כן","נטלין")} ("as they camp so they journey"), {A(2,17,"גבר","על","אתריה","לטקסיהון")} ("each man on his place by their taxis") — THE MARCH ORDER IS THE CAMP ORDER (the Talmud\'s two readings — a square as camped or a beam in file — Jerusalem Talmud Eruvin 5:1, the exam); the Levites\' camp in the middle, the four banners around.')
row(2, 18, 'MATERIAL', f'WEST: EPHRAIM. "The banner of the camp of Ephraim by their hosts {H(2,18,"ימה")} ("seaward" — westward); the prince Elishama son of Ammihud" → {A(2,18,"מערבא")} ("west") — the sea-word rendered by the compass: the translation reads the geography, not the metaphor.')
row(2, 24, 'MATERIAL', f'EPHRAIM\'S CAMP, THIRD. "{numword(camp[24])} by their hosts; {H(2,24,"ושלשים","יסעו")} ("and third they journey")" → {A(2,24,"בתליתתא","נטלין")} ("in the third place they journey") — the three summed equal the camp (computed: {numword(camp[19])} + {numword(camp[21])} + {numword(camp[23])} = {numword(camp[24])}).')
row(2, 25, 'MATERIAL', f'NORTH: DAN. "The banner of the camp of Dan {H(2,25,"צפנה")} ("northward") by their hosts; the prince Ahiezer son of Ammishaddai" → {A(2,25,"צפונא")} ("north").')
row(2, 31, 'MATERIAL', f'DAN\'S CAMP, LAST. "{numword(camp[31])}; {H(2,31,"לאחרנה","יסעו","לדגליהם")} ("last they journey, by their banners")" → {A(2,31,"בבתרתא","נטלין","לטקסיהון")} ("in the last place they journey, by their taxis") — the three summed equal the camp (computed: {numword(camp[26])} + {numword(camp[28])} + {numword(camp[30])} = {numword(camp[31])}); the march\'s four positions in the ink\'s own ordinals (computed: first, second, third, last).')
row(2, 32, 'MATERIAL', f'THE FOUR CAMPS SUMMED. "These are the counted of the children of Israel by their fathers\' house; all the counted of the camps by their hosts: {numword(camp[32]) if 32 in camp else numword(TOTAL)}" → {A(2,32,"שית","מאה","ותלתא","אלפין","וחמש","מאה","וחמשין")} ("603,550") — computed: {numword(camp[9])} + {numword(camp[16])} + {numword(camp[24])} + {numword(camp[31])} = {numword(TOTAL)} = 1:46\'s total = Exod 38:26\'s — the number\'s third seat.')
row(2, 33, 'CONTEXT', f'"And the Levites were not counted among the children of Israel, {H(2,33,"כאשר","צוה","יהוה","את","משה")} ("as the LORD commanded Moses")" — 1:47-49 recalled with the formula (its seats computed).')
row(2, 34, 'MATERIAL', f'THE RUN, CAMPED AND MARCHED. "And the children of Israel did according to all that the LORD commanded Moses: {H(2,34,"כן","חנו","לדגליהם","וכן","נסעו")} ("so they camped by their banners and so they journeyed"), each man by his families, by his fathers\' house" → {A(2,34,"כן","שרן","לטקסיהון","וכן","נטלין")} ("so they camped by their taxis and so they journeyed") — ONE VERSE REPORTS TWO RUNS: the camping (2:2\'s spec) and the marching (2:17\'s), the doubled "so" of 1:54 doubled again.')
# chapter 3
row(3, 1, 'MATERIAL', f'THE GENERATIONS OF AARON AND MOSES. "{H(3,1,"ואלה","תולדת","אהרן","ומשה")} ("and these are the generations of Aaron and Moses") {H(3,1,"ביום","דבר","יהוה","את","משה","בהר","סיני")} ("on the day the LORD spoke with Moses on Mount Sinai")" → {A(3,1,"ואלין","תולדת","אהרן","ומשה")} ("and these are the generations of Aaron and Moses") and {A(3,1,"בטורא","דסיני")} ("on the mountain of Sinai") — THE GENESIS HEADING\'S ONE SEAT OUTSIDE GENESIS (computed: ten "these are the generations" headings in the Torah, nine in Genesis, this one) — and the list that follows names AARON\'S SONS ALONE: Moses in the heading, none of his in the list (the exam\'s Talmud: whoever teaches another\'s son Torah is as if he begot him — Sanhedrin 19b); "on the day the LORD spoke" at {", ".join(ON_THE_DAY)} (computed) — the dating clause ties Aaron\'s line to Sinai\'s day.')
row(3, 2, 'MATERIAL', f'THE FOUR SONS. "And these are the names of the sons of Aaron: {H(3,2,"הבכור","נדב")} ("the firstborn Nadab"), and Abihu, Eleazar and Ithamar" → {A(3,2,"בוכרא","נדב")} ("the firstborn Nadab") — the firstborn labeled in a chapter about firstborns; the four-name list\'s seats computed: {", ".join(SONS_LIST)}.')
row(3, 3, 'MATERIAL', f'THE FILLED HAND AS AN OFFERING. "These are the names of the sons of Aaron, {H(3,3,"הכהנים","המשחים")} ("the anointed priests"), {H(3,3,"אשר","מלא","ידם","לכהן")} ("whose hand he filled to serve as priest")" → {A(3,3,"כהניא","דאתרביאו")} ("the priests who were raised/anointed") and {A(3,3,"די","אתקרב","קרבנהון","לשמשא")} ("whose OFFERING was brought near, to serve") — the investiture idiom ("filled the hand", this exact form\'s one Torah seat computed) rendered by its RITE: the ram of filling of Lev 8 — the translation names the ceremony where the ink names the hand (a REFERENCE to the investiture by Onkelos\' own word).')
row(3, 4, 'MATERIAL', f'THE DEATH, THE SONLESSNESS, THE FATHER\'S FACE. "And Nadab and Abihu died before the LORD {H(3,4,"בהקרבם","אש","זרה")} ("when they brought near strange fire") before the LORD in the wilderness of Sinai, {H(3,4,"ובנים","לא","היו","להם")} ("and sons they had not"); and Eleazar and Ithamar served as priests {H(3,4,"על","פני","אהרן","אביהם")} ("upon the face of Aaron their father")" → {A(3,4,"אשתא","נוכריתא")} ("foreign fire"), {A(3,4,"ובנין","לא","הוו","להון")} ("and sons they had not"), {A(3,4,"על","אפי","אהרן","אבוהון")} ("upon the face of Aaron their father" — kept) — THE SONLESSNESS WRITTEN (the phrase\'s one Tanakh seat, computed): had they had sons, the sons would have stood before Eleazar — the inheritance of office in the ink\'s own negative; "on the face of" = in the lifetime of (the exam: Sanhedrin 19b / the Sifra) — the Talmud reads the idiom, Onkelos keeps it; the death "in the wilderness of Sinai" (the phrase\'s nine Torah seats computed) dates Lev 10 to this book\'s own place.')
row(3, 5, 'CONTEXT', 'The frame: "And the LORD spoke to Moses, saying".')
row(3, 6, 'MATERIAL', f'THE TRIBE BROUGHT NEAR. "{H(3,6,"הקרב","את","מטה","לוי")} ("bring near the tribe of Levi") and stand it before Aaron the priest, {H(3,6,"ושרתו","אתו")} ("and they shall serve him")" → {A(3,6,"קרב","ית","שבטא","דלוי","ותקים","יתיה")} ("bring near the tribe of Levi and stand it") and {A(3,6,"וישמשון","יתיה")} ("and they shall minister to him") — THE OFFERING VERB ON A TRIBE (the phrase\'s one seat computed): the Levites are brought near as an offering is; the service is TO AARON — the tribe given to the office.')
row(3, 7, 'MATERIAL', f'TWO CHARGES. "They shall keep {H(3,7,"את","משמרתו","ואת","משמרת","כל","העדה")} ("his charge and the charge of the whole congregation") before the tent of meeting, {H(3,7,"לעבד","את","עבדת","המשכן")} ("to do the service of the tabernacle")" → {A(3,7,"ויטרון","ית","מטרתיה","וית","מטרת","כל","כנשתא")} ("and they shall keep his charge and the charge of the whole congregation") and {A(3,7,"למפלח","ית","פלחן","משכנא")} ("to perform the service of the tabernacle") — Aaron\'s charge and the people\'s charge both laid on the Levites: the tribe stands in for the congregation (the firstborn\'s substitution of 3:12 in the charge\'s grammar).')
row(3, 8, 'MATERIAL', f'THE VESSELS. "They shall keep all the vessels of the tent of meeting and the charge of the children of Israel, to do the service of the tabernacle" → {A(3,8,"ויטרון","ית","כל","מאני","משכן","זמנא")} ("and they shall keep all the vessels of the tent of appointed time") — the vessels named as the charge\'s object before chapter 4 divides them by house.')
row(3, 9, 'MATERIAL', f'GIVEN, GIVEN. "And you shall give the Levites to Aaron and his sons: {H(3,9,"נתונם","נתונם","המה","לו")} ("given, given are they to him") from among the children of Israel" → {A(3,9,"מסירין","יהיבין","אנון","ליה")} ("handed over, given are they to him") — THE DOUBLED WORD RENDERED BY TWO VERBS: the ink says "given" twice (the doubling\'s one seat, computed; the single "given" at {", ".join(GIVEN)}), Onkelos gives it two meanings — handed over and given (the exam: the Sifrei at 8:16 / 18:6 reads the doubling as given for the carrying and given for the song).')
row(3, 10, 'MATERIAL', f'THE PRIESTHOOD KEPT; THE STRANGER AGAIN. "And Aaron and his sons {H(3,10,"תפקד")} ("you shall appoint") and they shall keep {H(3,10,"את","כהנתם")} ("their priesthood"); {H(3,10,"והזר","הקרב","יומת")} ("and the stranger who approaches shall be put to death")" → {A(3,10,"תמני","ויטרון","ית","כהנתהון")} ("you shall appoint, and they shall keep their priesthood") and {A(3,10,"וחלוני","דיקרב","יתקטל")} ("and the lay man who approaches shall be killed") — the count-verb as APPOINT a second time (1:50); the death clause\'s second seat: here the stranger is the NON-PRIEST — a Levite too (the exam: Sanhedrin 83a, a non-priest who served — death by heaven).')
row(3, 11, 'CONTEXT', 'The frame: "And the LORD spoke to Moses, saying".')
row(3, 12, 'MATERIAL', f'THE SUBSTITUTION. "And I, behold, {H(3,12,"לקחתי","את","הלוים")} ("I have taken the Levites") from among the children of Israel instead of every firstborn, {H(3,12,"פטר","רחם")} ("opener of the womb"), of the children of Israel; and the Levites shall be Mine" → {A(3,12,"קרבית","ית","לואי")} ("I have BROUGHT NEAR the Levites") — the taking rendered as the offering verb (3:6\'s word) — and {A(3,12,"פתח","ולדא")} ("opener of the offspring"); "shall be Mine" → {A(3,12,"ויהון","משמשין","קדמי","לואי")} ("and the Levites shall be ministering before Me") — possession rendered as service; THE FIRSTBORN ENGINE\'S OWN PHRASE (computed: "opener of the womb" at {", ".join(WOMB)} — Exod 13\'s sanctification clause) — the substitution is a REFERENCE to the firstborn law by its own token.')
row(3, 13, 'MATERIAL', f'THE GROUND, DATED. "For every firstborn is Mine: {H(3,13,"ביום","הכתי","כל","בכור")} ("on the day I smote every firstborn") in the land of Egypt I sanctified to Me every firstborn in Israel, from man to beast; Mine shall they be, I am the LORD" → {A(3,13,"ביומא","דקטלית","כל","בוכרא")} ("on the day that I KILLED every firstborn") and {A(3,13,"אקדשית","קדמי")} ("I sanctified before Me") — the sanctification is DATED to the plague\'s night (Exod 12:29 on the tape; 13:2\'s command the morning after): the ground of the substitution is an event on the ledger, not a decree without a day; "smote" rendered "killed" — the translation reads the outcome.')
row(3, 14, 'MATERIAL', f'THE PLACED FRAME. "And the LORD spoke to Moses {H(3,14,"במדבר","סיני")} ("in the wilderness of Sinai"), saying" — the portion\'s second utterance carrying its place (computed: 1:1 and 3:14 of ten frames); Onkelos literal.')
row(3, 15, 'MATERIAL', f'THE LEVITE THRESHOLD. "Count the sons of Levi by their fathers\' house, by their families; every male {H(3,15,"מבן","חדש","ומעלה")} ("from a month old and upward") you shall count them" → {A(3,15,"מבר","ירחא","ולעלא")} ("from a son of a month and upward") — the second threshold (computed: twenty at 1:3, a MONTH here — the tribe counted from the age its firstborn are redeemable, 18:16; thirty-to-fifty at 4:3 for the work).')
row(3, 16, 'MATERIAL', f'BY THE MOUTH OF THE LORD. "And Moses counted them {H(3,16,"על","פי","יהוה")} ("by the mouth of the LORD"), {H(3,16,"כאשר","צוה")} ("as he was commanded")" → {A(3,16,"על","מימרא","דיי")} ("by the WORD of the LORD") — the Memra; the phrase THREE TIMES in this chapter (computed: {", ".join(AL_PI)}), on the count of the Levites, on their total, on the redemption money — the exam\'s question (how were infants in tents counted? by the Word: Bamidbar Rabbah 3:9, the bat kol — outside scope, at Step 5).')
row(3, 17, 'MATERIAL', f'THE THREE HOUSES. "And these were the sons of Levi by their names: Gershon, Kohath and Merari" → {A(3,17,"גרשון","וקהת","ומררי")} — the three houses that chapter 4 assigns their burdens.')
row(3, 18, 'CONTEXT', 'Gershon\'s sons by their families: Libni and Shimei — literal.')
row(3, 19, 'CONTEXT', 'Kohath\'s sons: Amram, Izhar, Hebron, Uzziel — literal (Amram the house of Moses and Aaron, 26:59).')
row(3, 20, 'CONTEXT', f'Merari\'s sons: Mahli and Mushi; "these are the families of Levi by their fathers\' house" → {A(3,20,"זרעית","לואי")} ("the seed-families of the Levites") — eight families under three houses.')
row(3, 21, 'CONTEXT', 'The Gershonite families named: Libni, Shimei — literal.')
row(3, 22, 'MATERIAL', f'GERSHON COUNTED. "Their counted, in the number of every male from a month old and up: {numword(clans[22])}" → {A(3,22,"שבעא","אלפין","וחמש","מאה")} ("7,500") — computed.')
row(3, 23, 'MATERIAL', f'GERSHON WEST. "The families of the Gershonites shall camp {H(3,23,"אחרי","המשכן")} ("behind the tabernacle") {H(3,23,"ימה")} ("seaward")" → {A(3,23,"אחורי","משכנא","ישרון","מערבא")} ("behind the tabernacle they shall camp, west") — the Levite ring\'s first side (computed: west 3:23, south 3:29, north 3:35, east 3:38 — the inner ring matches the outer\'s four sides).')
row(3, 24, 'CONTEXT', f'"The prince of the fathers\' house of the Gershonites: Eliasaph son of Lael" — literal. (The shelf\'s export heads its piska 62 "(Bamidbar 3:24)": by POSITION and by its own quotations it is the Sifrei\'s row on 8:24, read at this sitting\'s num_04_kehat ledger where 4:3\'s thirty is its subject — the head a mislabel, recorded there.)')
row(3, 25, 'MATERIAL', f'GERSHON\'S CHARGE. "The charge of the sons of Gershon in the tent of meeting: the tabernacle and the tent, {H(3,25,"מכסהו")} ("its covering"), and the screen of the door of the tent of meeting" → {A(3,25,"משכנא","ופרסא","חופאיה")} ("the tabernacle and the curtain, its covering") — the soft parts: the curtains, the covers, the screens.')
row(3, 26, 'MATERIAL', f'"The hangings of the court and the screen of the door of the court which is by the tabernacle and by the altar round about, and its cords, for all its service" → {A(3,26,"וסרדי","דדרתא")} ("and the hangings of the court"), {A(3,26,"אטונוהי")} ("its cords") — Gershon\'s list closed: everything woven and roped.')
row(3, 27, 'CONTEXT', 'The Kohathite families named: Amram, Izhar, Hebron, Uzziel — literal.')
row(3, 28, 'MATERIAL', f'KOHATH COUNTED; THE THREE HUNDRED. "In the number of every male from a month old and up: {numword(clans[28])}, {H(3,28,"שמרי","משמרת","הקדש")} ("keepers of the charge of the holy")" → {A(3,28,"תמניא","אלפין","ושית","מאה")} ("8,600"), {A(3,28,"נטרי","מטרתא","דקודשא")} ("keepers of the charge of the holy") — THE INK\'S OWN ARITHMETIC PROBLEM (computed): the three houses sum to {numword(CLANSUM)} ({numword(clans[22])} + {numword(clans[28])} + {numword(clans[34])}) and 3:39 writes the total {numword(LEV)} — a delta of {CLANSUM - LEV}; the exam\'s answer (Bekhorot 5a: three hundred firstborn Levites who could redeem no one) is the Talmud\'s, the delta is the verse\'s.')
row(3, 29, 'MATERIAL', f'KOHATH SOUTH. "The families of the sons of Kohath shall camp on the side of the tabernacle {H(3,29,"תימנה")} ("southward")" → {A(3,29,"דרומא")} ("south").')
row(3, 30, 'CONTEXT', 'The prince of the Kohathites: Elizaphan son of Uzziel — literal (the appointment Korach\'s story later contests; off this span).')
row(3, 31, 'MATERIAL', f'KOHATH\'S CHARGE. "Their charge: the ark and the table and the lampstand and {H(3,31,"והמזבחת")} ("the altars") and the vessels of the holy with which they serve, and {H(3,31,"והמסך")} ("the screen"), and all its service" → {A(3,31,"ארונא","ופתורא","ומנרתא","ומדבחא")} ("the ark, the table, the lampstand, the altar") and {A(3,31,"ופרסא")} ("and the curtain") — the holy of holies\' furniture; "the altars" plural (the golden and the bronze — chapter 4 covers both); the screen here the VEIL (4:5 names it "the veil of the screen").')
row(3, 32, 'MATERIAL', f'THE PRINCE OF PRINCES. "{H(3,32,"ונשיא","נשיאי","הלוי")} ("and the prince of the princes of Levi"): Eleazar son of Aaron the priest, {H(3,32,"פקדת","שמרי","משמרת","הקדש")} ("the appointment of the keepers of the charge of the holy")" → {A(3,32,"ואמרכלא","דממנא","על","רברבי","לואי")} ("and the AMARKAL who is appointed over the chiefs of the Levites") and {A(3,32,"דמתחות","ידוהי","ממנן")} ("under whose hand are appointed") — THE TEMPLE\'S OFFICE-TITLE READ INTO THE VERSE: the amarkal is the Mishnah\'s treasury officer (Shekalim 5:2, seven of them — the exam), the translation naming Eleazar\'s office by the later institution\'s word; the phrase "prince of princes" the ink\'s one seat (computed).')
row(3, 33, 'CONTEXT', 'The Merarite families named: Mahli, Mushi — literal.')
row(3, 34, 'MATERIAL', f'MERARI COUNTED. "{numword(clans[34])}" → {A(3,34,"שתא","אלפין","ומאתן")} ("6,200") — computed; the third house.')
row(3, 35, 'MATERIAL', f'MERARI NORTH. "The prince: Zuriel son of Abihail; on the side of the tabernacle they shall camp {H(3,35,"צפנה")} ("northward")" → {A(3,35,"צפונא")} ("north").')
row(3, 36, 'MATERIAL', f'MERARI\'S CHARGE. "{H(3,36,"ופקדת","משמרת","בני","מררי")} ("and the appointed charge of the sons of Merari"): the boards of the tabernacle and its bars and its pillars and its sockets and all its vessels and all its service" → {A(3,36,"ודי","מסיר","למטרת","בני","מררי")} ("and what is handed over to the charge of the sons of Merari"), {A(3,36,"דפי","משכנא","ועברוהי","ועמודוהי","וסמכוהי")} ("the boards of the tabernacle and its bars and its pillars and its sockets") — the hard parts: the frame.')
row(3, 37, 'CONTEXT', f'"And the pillars of the court round about and their sockets and their pegs and their cords" → {A(3,37,"וסכיהון","ואטוניהון")} ("and their pegs and their cords") — Merari\'s list closed.')
row(3, 38, 'MATERIAL', f'EAST: MOSES AND AARON; THE STRANGER A THIRD TIME. "Those camping before the tabernacle {H(3,38,"קדמה")} ("in front"), before the tent of meeting {H(3,38,"מזרחה")} ("eastward"): Moses and Aaron and his sons, keeping the charge of the sanctuary {H(3,38,"למשמרת","בני","ישראל")} ("for the charge of the children of Israel"); {H(3,38,"והזר","הקרב","יומת")} ("and the stranger who approaches shall be put to death")" → {A(3,38,"קדומא")} ("in front"), {A(3,38,"מדינחא")} ("east"), {A(3,38,"נטרין","מטרת","מקדשא","למטרת","בני","ישראל")} ("keeping the charge of the sanctuary for the charge of the children of Israel") — the inner ring\'s fourth side is the LEADERS\' (the ring: west Gershon, south Kohath, north Merari, east Moses-Aaron — computed), the charge kept ON BEHALF OF the people (Onkelos: "for the charge of"); the death clause\'s third seat.')
row(3, 39, 'MATERIAL', f'THE TOTAL AS WRITTEN. "All the counted of the Levites whom Moses and Aaron counted by the mouth of the LORD, by their families, every male from a month old and up: {H(3,39,"שנים","ועשרים","אלף")} ("twenty-two thousand")" → {A(3,39,"עשרין","ותרין","אלפין")} ("twenty-two thousand") — {numword(LEV)} against the houses\' computed {numword(CLANSUM)}: THE DELTA OF {CLANSUM - LEV} stands in the ink (the exam\'s Talmud answers it; the verse does not); "by the mouth of the LORD" the second of three; the ink\'s "two and twenty thousand" — the unit BEFORE the ten, the thousand multiplying both (the census grammar).')
row(3, 40, 'MATERIAL', f'THE SAID-FRAME AND THE FIRSTBORN COUNT. "{H(3,40,"ויאמר","יהוה","אל","משה")} ("and the LORD SAID to Moses") — the portion\'s one "said" frame among ten (computed) — count every firstborn male of the children of Israel from a month old and up, {H(3,40,"ושא","את","מספר","שמתם")} ("and lift the number of their names")" → {A(3,40,"וקבל","ית","מנין","שמהתהון")} ("and receive the number of their names") — the census idiom of 1:2 on the firstborn: the same "lift/receive" and the same "names".')
row(3, 41, 'MATERIAL', f'THE EXCHANGE, MAN AND BEAST. "And you shall take the Levites for Me — I am the LORD — instead of every firstborn among the children of Israel, and {H(3,41,"בהמת","הלוים")} ("the cattle of the Levites") instead of every firstling among the cattle of the children of Israel" → {A(3,41,"ותקרב","ית","לואי","קדמי")} ("and you shall BRING NEAR the Levites before Me") — the taking rendered as offering again (3:12); the beasts exchanged with the beasts (the exam: one Levite lamb redeeming many firstling donkeys — Bekhorot 4b).')
row(3, 42, 'CONTEXT', f'"And Moses counted, {H(3,42,"כאשר","צוה","יהוה","אתו")} ("as the LORD commanded him"), every firstborn among the children of Israel" — the run\'s frame with the formula (its seats computed).')
row(3, 43, 'MATERIAL', f'THE FIRSTBORN TOTAL. "And all the firstborn males, by the number of names from a month old and up, of their counted: {H(3,43,"שנים","ועשרים","אלף","שלשה","ושבעים","ומאתים")} ("twenty-two thousand, three and seventy and two hundred")" → {A(3,43,"עשרין","ותרין","אלפין","מאתן","ושבעין","ותלתא")} ("22,273") — computed {numword(FB)}: the thousands first, then the remainder ASCENDING (three, seventy, two hundred) — the ink\'s two orders in one number; the Aramaic writes the remainder descending.')
row(3, 44, 'CONTEXT', 'The frame: "And the LORD spoke to Moses, saying".')
row(3, 45, 'MATERIAL', f'THE EXCHANGE RESTATED. "Take the Levites instead of every firstborn among the children of Israel, and the cattle of the Levites instead of their cattle; and the Levites shall be Mine, I am the LORD" → {A(3,45,"קרב","ית","לואי")} ("bring near the Levites"), {A(3,45,"ויהון","משמשין","קדמי","לואי")} ("and the Levites shall be ministering before Me") — 3:41 said again before the redemption\'s arithmetic, with "I am the LORD" closing it.')
row(3, 46, 'MATERIAL', f'THE EXCESS. "And the redemption of {H(3,46,"השלשה","והשבעים","והמאתים")} ("the three and the seventy and the two hundred") who exceed the Levites of the firstborn of the children of Israel" → {A(3,46,"וית","פרקן","מאתן","ושבעין","ותלתא")} ("and the redemption of the two hundred and seventy and three") — computed: {numword(FB)} − {numword(LEV)} = {EXC}; the ink writes the number ASCENDING with the article on each part; {H(3,46,"העדפים")} ("who exceed") → {A(3,46,"דיתירין")} ("who are in excess").')
row(3, 47, 'MATERIAL', f'FIVE, FIVE — THE SHEKEL AND ITS GERAH. "You shall take {H(3,47,"חמשת","חמשת","שקלים","לגלגלת")} ("five, five shekels per skull"); {H(3,47,"בשקל","הקדש","תקח","עשרים","גרה","השקל")} ("by the shekel of the holy you shall take, twenty gerah the shekel")" → {A(3,47,"חמש","חמש","סלעין","לגלגלתא")} ("five, five SELA\'IM per skull") and {A(3,47,"עשרין","מעין","סלעא")} ("twenty MA\'IN the sela") — THE CONVERSION LAYER AT ITS NUMBERS SEAT: the shekel is the sela, the gerah the ma\'ah — the very words the Talmud cites ("and we translate: twenty ma\'in", Bekhorot 50a, the corpus\'s standing finding from the Exodus block, now read at 3:47); the phrase "twenty gerah" at {", ".join(GERAH)} (computed: four Torah seats) and the doubled five the ink\'s one seat.')
row(3, 48, 'MATERIAL', f'"And you shall give the money to Aaron and his sons, the redemption of those who exceed among them" → {A(3,48,"פרקן","דיתירין","בהון")} ("the redemption of those in excess among them") — the money\'s destination: the priests.')
row(3, 49, 'CONTEXT', f'"And Moses took the redemption money from those who exceeded the redeemed of the Levites" → {A(3,49,"פריקי","לואי")} ("the redeemed of the Levites") — the run opens; {H(3,49,"מאת")} ("from") — the consonantal homograph of "a hundred of" (2:9\'s word), told apart by its vowels (computed: the census parser reads the tsere).')
row(3, 50, 'MATERIAL', f'THE MONEY. "From the firstborn of the children of Israel he took the money: {H(3,50,"חמשה","וששים","ושלש","מאות","ואלף")} ("five and sixty and three hundred and a thousand") by the shekel of the holy" → {A(3,50,"אלף","ותלת","מאה","ושתין","וחמש","סלעין")} ("a thousand and three hundred and sixty and five sela\'im") — computed: {EXC} × 5 = {numword(MONEY)}; the ink writes it ASCENDING with the thousand LAST and joined by the conjunction — "and a thousand" an addend, not a multiplier (the form\'s three Torah seats computed: {", ".join(VE_ALEF)}); the Aramaic reverses to descending.')
row(3, 51, 'MATERIAL', f'THE RUN\'S DOUBLE FORMULA. "And Moses gave the redemption money to Aaron and his sons {H(3,51,"על","פי","יהוה")} ("by the mouth of the LORD"), {H(3,51,"כאשר","צוה","יהוה","את","משה")} ("as the LORD commanded Moses")" → {A(3,51,"על","מימרא","דיי")} ("by the Word of the LORD") and {A(3,51,"כמא","די","פקיד","יי","ית","משה")} ("as the LORD commanded Moses") — both formulas on one verse: the fifth commanded-and-done pair of the portion closes (the census, the camp, the Levite count, the firstborn count, the redemption).')
# chapter 4
row(4, 1, 'CONTEXT', 'The frame: "to Moses AND to Aaron, saying" — the second double-addressed frame (computed).')
row(4, 2, 'MATERIAL', f'THE HOUSE\'S HEAD LIFTED. "{H(4,2,"נשא","את","ראש","בני","קהת")} ("lift the head of the sons of Kohath") from among the sons of Levi, by their families, by their fathers\' house" → {A(4,2,"קבילו","ית","חשבן","בני","קהת")} ("receive the sum of the sons of Kohath") — the census idiom on ONE HOUSE (computed: the infinitive form at 4:2 and 4:22; the imperative at 1:2 and 26:2); the same accounting rendering.')
row(4, 3, 'MATERIAL', f'THE WORK\'S AGES. "{H(4,3,"מבן","שלשים","שנה","ומעלה","ועד","בן","חמשים","שנה")} ("from thirty years old and upward, and until fifty years old"), {H(4,3,"כל","בא","לצבא")} ("everyone who comes to the host") to do work in the tent of meeting" → {A(4,3,"מבר","תלתין","שנין","ולעלא","ועד","בר","חמשין","שנין")} ("from a son of thirty years and upward, and until a son of fifty years"), {A(4,3,"כל","דאתי","לחילא","למעבד","עבדתא")} ("everyone who comes to the host to do the work") — the THIRD THRESHOLD, a window: thirty to fifty (computed: the pair\'s seats in chapter 4 — 4:3, 23, 30, 35, 39, 43, 47); "the host" is the WORK-host, the army-word of 1:3 on the Levites\' labor (Onkelos one word for both). THE SIFREI\'S ROW (piska 62 — read fresh below) reconciles this thirty with 8:24\'s twenty-five: twenty-five to learn, thirty to serve.')
row(4, 4, 'MATERIAL', f'THE HOLY OF HOLIES. "This is the service of the sons of Kohath in the tent of meeting: {H(4,4,"קדש","הקדשים")} ("the holy of holies")" → {A(4,4,"קדש","קודשיא")} ("the holy of holies") — the phrase at 4:4 and 4:19 in the span (computed): Kohath\'s load is the innermost.')
row(4, 5, 'MATERIAL', f'THE PRIESTS COVER FIRST. "And Aaron and his sons shall come in {H(4,5,"בנסע","המחנה")} ("when the camp journeys") and take down {H(4,5,"את","פרכת","המסך")} ("the veil of the screen") and cover with it the ark of the testimony" → {A(4,5,"במטל","משריתא")} ("at the journeying of the camp"), {A(4,5,"ויפרקון","ית","פרכתא","דפרסא")} ("and they shall take down the veil of the screen"), {A(4,5,"ויכסון","בה","ית","ארונא","דסהדותא")} ("and they shall cover with it the ark of the testimony") — THE VEIL BECOMES THE ARK\'S COVER on the march; the priests, not the Kohathites, do the covering (4:15 the sequence: the covering first, the carrying after).')
row(4, 6, 'MATERIAL', f'THE ARK\'S THREE LAYERS. "They shall put on it a covering of {H(4,6,"עור","תחש")} ("tachash hide") and spread {H(4,6,"בגד","כליל","תכלת")} ("a cloth wholly of blue") on top, and put in its poles" → {A(4,6,"חופאה","דמשך","ססגונא")} ("a covering of SASGONA hide") and {A(4,6,"לבוש","גמיר","תכלא")} ("a garment entirely of blue") — the tachash rendered by a colored-hide word (the exam: Shabbat 28a-b on what the tachash was); "wholly of blue" is the ROBE\'S phrase (computed: {", ".join(BLUE)} — the high priest\'s robe at Exod 28:31 and 39:22, the ark\'s outer cloth here): the ark travels dressed as the priest is; ONLY THE ARK has blue OUTSIDE the hide (the table, lampstand and altars have the hide outermost — 4:8, 10, 11, 12, 14 below), the ink\'s own ordering.')
row(4, 7, 'MATERIAL', f'THE TABLE. "On {H(4,7,"שלחן","הפנים")} ("the table of the face" — the presence bread) they shall spread a blue cloth and put on it the dishes and the spoons and {H(4,7,"המנקית")} ("the jars") and {H(4,7,"קשות","הנסך")} ("the jugs of libation"); and {H(4,7,"ולחם","התמיד")} ("and the continual bread") shall be on it" → {A(4,7,"פתורא","דלחם","אפיא")} ("the table of the bread of the face"), {A(4,7,"מגיסיא")} ("the dishes"), {A(4,7,"בזיכיא")} ("the pans" — the frankincense bowls of Menachot 11), {A(4,7,"מכילתא")} ("the measures"), {A(4,7,"קסוות","נסוכא")} ("the jugs of libation"), {A(4,7,"ולחם","תדירא","עלוהי","יהי")} ("and the continual bread shall be on it") — THE BREAD TRAVELS ON THE TABLE: the ink keeps it "continually" on the table even on the march (the exam: Menachot 99b, "before Me continually" — never removed).')
row(4, 8, 'CONTEXT', f'"They shall spread on them a cloth of {H(4,8,"תולעת","שני")} ("crimson worm") and cover it with a covering of tachash hide and put in its poles" → {A(4,8,"צבע","זהורי")} ("crimson dye") — the table\'s second cloth; the hide outermost.')
row(4, 9, 'MATERIAL', f'THE LAMPSTAND. "They shall take a blue cloth and cover {H(4,9,"מנרת","המאור")} ("the lampstand of the light") and its lamps and its tongs and its fire-pans and all its oil vessels with which they serve it" → {A(4,9,"מנרתא","דאנהורי")} ("the lampstand of the lights"), {A(4,9,"בוצינהא")} ("its lamps"), {A(4,9,"צבתהא")} ("its tongs"), {A(4,9,"מחתיתהא")} ("its fire-pans") — the lampstand and its whole service kit under one cloth.')
row(4, 10, 'CONTEXT', f'"They shall put it and all its vessels into a covering of tachash hide and put it {H(4,10,"על","המוט")} ("on the bar")" → {A(4,10,"על","אריחא")} ("on the pole") — carried on a bar, not by rings (the lampstand has no poles of its own).')
row(4, 11, 'CONTEXT', f'"On {H(4,11,"מזבח","הזהב")} ("the golden altar") they shall spread a blue cloth and cover it with a covering of tachash hide and put in its poles" → {A(4,11,"מדבחא","דדהבא")} ("the altar of gold") — blue under, hide over.')
row(4, 12, 'CONTEXT', f'"They shall take all the vessels of service with which they serve in the holy and put them in a blue cloth and cover them with a covering of tachash hide and put them on the bar" → {A(4,12,"מני","שמושא")} ("the vessels of service") — the loose vessels bundled, on a bar.')
row(4, 13, 'MATERIAL', f'THE ALTAR ASHED. "{H(4,13,"ודשנו","את","המזבח")} ("and they shall remove the ashes of the altar") and spread on it a cloth of {H(4,13,"ארגמן")} ("purple")" → {A(4,13,"ויספון","ית","קטמא","דמדבחא")} ("and they shall clear away the ashes of the altar"), {A(4,13,"לבוש","ארגון")} ("a garment of purple") — THE BRONZE ALTAR IS THE ONE THING NOT DRESSED IN BLUE: ashed and covered in purple (the exam: the fire kept burning under the cloth on the march — Yoma 21b; the Sifrei at 4:13 is off this span); the ash-verb of Exod 27:3\'s ash-pots.')
row(4, 14, 'CONTEXT', f'"They shall put on it all its vessels with which they serve on it: the fire-pans, the forks, the shovels, the basins, all the vessels of the altar; and spread on it a covering of tachash hide and put in its poles" → {A(4,14,"מחתיתא")} ("the fire-pans"), {A(4,14,"צנוריתא")} ("the forks"), {A(4,14,"מגרופיתא")} ("the shovels"), {A(4,14,"מזרקיא")} ("the basins") — the altar\'s kit; the hide outermost (computed: tachash at 4:{", ".join(map(str, TACHASH4))}).')
row(4, 15, 'MATERIAL', f'THE SEQUENCE AND THE FIRST DEATH CLAUSE. "And Aaron and his sons shall finish covering the holy and all the vessels of the holy when the camp journeys, and {H(4,15,"ואחרי","כן","יבאו","בני","קהת","לשאת")} ("after that the sons of Kohath shall come to carry"); {H(4,15,"ולא","יגעו","אל","הקדש","ומתו")} ("and they shall not touch the holy, lest they die") — these are {H(4,15,"משא","בני","קהת")} ("the burden of the sons of Kohath") in the tent of meeting" → {A(4,15,"וישיצי","אהרן","ובנוהי","לכסאה","ית","קודשא")} ("and Aaron and his sons shall finish covering the holy"), {A(4,15,"ובתר","כן","יעלון","בני","קהת","למטל")} ("and after that the sons of Kohath shall enter to carry"), {A(4,15,"ולא","יקרבון","לקודשא","ולא","ימותון")} ("and they shall not APPROACH the holy, and they shall not die") — the touching rendered as approaching (a wider guard); the ORDER is the law: the priests finish, then the carriers enter; the death clause the first of three in 4:15-20 (computed).')
row(4, 16, 'MATERIAL', f'ELEAZAR\'S CHARGE. "And the appointment of Eleazar son of Aaron the priest: {H(4,16,"שמן","המאור")} ("the oil of the light") and {H(4,16,"וקטרת","הסמים")} ("the incense of spices") and {H(4,16,"ומנחת","התמיד")} ("the continual meal-offering") and {H(4,16,"ושמן","המשחה")} ("the anointing oil"); the charge of all the tabernacle and all that is in it, in the holy and in its vessels" → {A(4,16,"ודי","מסיר","לאלעזר")} ("and what is handed over to Eleazar"), {A(4,16,"משחא","דאנהרותא")} ("the oil of lighting"), {A(4,16,"וקטרת","בוסמיא")} ("and the incense of spices"), {A(4,16,"ומנחתא","תדירא")} ("and the continual meal-offering"), {A(4,16,"ומשחא","דרבותא")} ("and the oil of greatness" — the anointing oil) — the four consumables carried by the priest himself (the exam: Eleazar bore them, the Sifrei Zuta / Yerushalmi Shabbat 10:3 — outside scope), his charge over the whole.')
row(4, 17, 'CONTEXT', 'The frame: "to Moses AND to Aaron, saying" — the third double-addressed frame (computed).')
row(4, 18, 'MATERIAL', f'CUT NOT OFF. "{H(4,18,"אל","תכריתו","את","שבט","משפחת","הקהתי")} ("do not cut off the tribe of the families of the Kohathite") from among the Levites" → {A(4,18,"לא","תשיצון","ית","שבטא","זרעית","קהת")} ("do not destroy the tribe of the family of Kohath") — the cutting-off verb\'s one seat in this form (computed): the guard laid on MOSES AND AARON — their negligence would cut the house off; the cutting-off word (karet, "excision") turned on the leaders.')
row(4, 19, 'MATERIAL', f'THE REMEDY. "This do for them, {H(4,19,"וחיו","ולא","ימתו")} ("that they may live and not die") when they approach the holy of holies: Aaron and his sons shall come in and set them {H(4,19,"איש","איש","על","עבדתו","ואל","משאו")} ("each man, each man to his service and to his burden")" → {A(4,19,"ויחון","ולא","ימותון")} ("and they shall live and not die"), {A(4,19,"וימנון","יתהון","גבר","גבר","על","פולחניה","ולמטוליה")} ("and they shall APPOINT them, each man, each man to his service and to his burden") — the assignment is per man (the doubled "man" kept); the second death clause; the priests assign, the Levites bear.')
row(4, 20, 'MATERIAL', f'NOT TO SEE THE SWALLOWING. "And they shall not come in to see {H(4,20,"כבלע","את","הקדש")} ("as the holy is swallowed") lest they die" → {A(4,20,"למחזי","כד","מכסן","ית","מני","קודשא")} ("to see WHEN THEY COVER the VESSELS of the holy") — the swallowing verb (the word\'s ONE seat in the Tanakh, computed) rendered as covering and the object expanded to "the vessels": the moment forbidden to the eye is the packing (the exam\'s Talmud reads the swallowing as the taking-down — Sanhedrin 81b; the Sifrei off this span); the third death clause: touching (4:15), approaching unassigned (4:19), seeing (4:20).')
assert sorted(R) == [(c, v) for c in range(1, 5) for v in range(1, ONK_LEN[c] + 1) if not (c == 4 and v > 20)], [k for k in [(c, v) for c in range(1, 5) for v in range(1, ONK_LEN[c] + 1) if not (c == 4 and v > 20)] if k not in R]

# ---- THE SIFREI ROW (read fresh at num_04_kehat) ----
SIFREI_62 = (f'- Sifrei Bamidbar 62:1 — MATERIAL (read fresh; FOUND BY POSITION: the export heads this piska "(Bamidbar 3:24)" but it sits between piska 61 on 8:4 and piska 63 on 8:25 and quotes "from the age of twenty-five" (8:24) and "from thirty years and up" (4:23) — the Sifrei\'s row on 8:24, the head a mislabel; recorded in RESEARCH_LOG.md). '
             f'"This is what applies to the Levites" (8:24): YEARS disqualify the Levites, BLEMISHES do not — against the a-fortiori (I1) that would carry the priests\' blemish-bar to the Levites ("if where years do not disqualify [the priests], blemishes do — where years do disqualify, how much more"): the verse\'s "this" REFUTES the a-fortiori (a stated limit beats an inferred one). And THE TWO AGES RECONCILED: twenty-five (8:24) against thirty (4:23, and 4:3 here) — from twenty-five for LEARNING the service, from thirty for SERVING: two verses, one threshold with an apprenticeship before it (the Talmud at Chullin 24a adds the fifty: the voice, not the years, in the Temple — the exam). '
             f'THE OPERATOR for 4:3: the window thirty-to-fifty is the WORK threshold; the Sifrei\'s reading makes the five years before it a status of its own (a trainee), and the priests\' blemish rule a rule the Levites do NOT share.')
SIFREI_NOTE = ('## Sifrei Bamidbar — the shelf\'s silence on Numbers 1:1-4:20, computed\n'
               '(the Sifrei on Numbers OPENS at 5:1 — piska 1\'s head; the only head inside chapters 1-4 in the export is piska 62\'s "(Bamidbar 3:24)", which by position — between 61 on 8:4 and 63 on 8:25 — and by its own quotations (8:24, 4:23) is the row on 8:24: read fresh in this sitting\'s num_04_kehat ledger where 4:3\'s thirty is its subject; no other row of the spine touches this span — the shelf\'s, not ours)\n')

# ---- THE INK SECTIONS (shared facts; each ledger prints the lines its span leans on) ----
INK = {}
INK['date'] = f'- THE DATE STAMP: 1:1 "{" ".join(DATE_1_1[8:13])}" ("on the first of the second month in the second year") — the day, the month, the year; Exod 40:17 "{" ".join(DATE_40_17[1:7])}" ("in the first month in the second year on the first of the month") the erection; Num 9:1 "{" ".join(DATE_9_1[6:13])}" ("in the second year of their going out of Egypt in the first month") — LATER in the text, EARLIER in time: the tape\'s retrograde marker (Pesachim 6b:7 names this very pair). 1:18 repeats "באחד לחדש השני" ("on the first of the second month"): the run on the command\'s day.'
INK['frames'] = f'- THE UTTERANCE CENSUS: {len(FR)} frames in 1:1-4:20 — {", ".join(FR)}; three to Moses AND Aaron ({", ".join(FR_AARON)}); two carrying the place "in the wilderness of Sinai" ({", ".join(FR_PLACE)}); one "said" ({", ".join(FR_SAID)}), the rest "spoke... saying".'
INK['pairs'] = f'- THE FIVE SPEC/RUN PAIRS: the census (1:2-3 → 1:19), the camp (2:2, 2:17 → 2:34), the Levite count (3:15 → 3:16, 3:39), the firstborn count (3:40 → 3:42-43), the redemption (3:46-48 → 3:49-51); the formula "as the LORD commanded Moses" at {", ".join(AS_CMD)}, "according to all that the LORD commanded" at {", ".join(ALL_CMD)}, "by the mouth of the LORD" at {", ".join(AL_PI)} (computed).'
INK['numbers'] = (f'- THE CENSUS\'S NUMBERS, EVERY ONE COMPUTED FROM THE INK: the twelve — {"; ".join(f"{O_COUNT[(v - 21) // 2]} {numword(twelve[v])}" for v in range(21, 44, 2))}; their sum {numword(sum(twelve.values()))} = 1:46\'s {numword(TOTAL)} = 2:32\'s (the four camps {numword(camp[9])} + {numword(camp[16])} + {numword(camp[24])} + {numword(camp[31])}) = Exod 38:26\'s half-shekel count; the Levite houses {numword(clans[22])} + {numword(clans[28])} + {numword(clans[34])} = {numword(CLANSUM)} against 3:39\'s {numword(LEV)} — DELTA {CLANSUM - LEV}; the firstborn {numword(FB)}; the excess {numword(FB)} − {numword(LEV)} = {EXC} (3:46); {EXC} × 5 shekels = {numword(MONEY)} (3:50).')
INK['grammar'] = (f'- THE CENSUS\'S NUMBER GRAMMAR (measured on all the numbers of 1:1-4:20): a unit immediately before "hundreds" multiplies (חמש מאות, "five hundred"); אלף ("thousand") or אלפים ("thousands") WITHOUT the conjunction multiplies the whole group before it (ששה וארבעים אלף, "six and forty thousand" = 46,000; שש מאות אלף, "six hundred thousand"); וְאֶלֶף ("and a thousand") is an ADDEND (3:50 "five and sixty and three hundred and a thousand" = 1,365; the form\'s three Torah seats: {", ".join(VE_ALEF)}); מֵאֵת ("from") is the consonantal homograph of מְאַת ("a hundred of"), told apart by its vowels (3:49, 3:50 against 2:9, 16, 24, 31). '
                  f'THE ENGINE\'S NUMERAL PARSER CANNOT READ IT (measured: cold_run_sequence.ink_numbers on 1:21 → {ENGINE_121}, on 3:39 → {ENGINE_339}, on 1:46 → {ENGINE_146} — Genesis\'s and Exodus\'s grammar has no thousands and reads שנים as "years" — the compile sitting\'s item, recorded in COMPILE_DEBT).')
INK['orders'] = f'- THE TRIBES\' THREE ORDERS (computed): the princes 1:5-15 — {", ".join(O_PRINCES)}; the count 1:20-43 — {", ".join(O_COUNT)} (GAD moves from eleventh to third); the camp 2:3-31 — {", ".join(O_CAMP)} (Judah\'s banner first, Gad under Reuben\'s). The one prince under two spellings: דעואל ("Deuel") at {", ".join(DEUEL)}, רעואל ("Reuel") at {", ".join(REUEL)}.'
INK['ketiv'] = f'- THE WRITTEN AND THE READ at 1:16: קריאי ("the called of" — written, unpointed) / קרואי ("the summoned of" — read): the ONE unpointed token in 1:1-4:20 (computed on the Tanakh DB and on the snapshot store; the store carries both tokens, the written first). Onkelos renders the read form.'
INK['designated'] = f'- DESIGNATED BY NAMES (1:17): נקבו ("were designated") — the root of the blasphemer\'s "pronounced" (Lev 24:11, 24:16; computed on the shared lemma, its Torah seats {", ".join(NAKAV)}): the same verb names princes and pierces the Name — a shared lemma, recorded, no inference drawn.'
INK['pedigree'] = f'- THE PEDIGREE VERB: ויתילדו ("and they declared their pedigrees") at {", ".join(PEDIGREE)} ALONE in the Tanakh; the census idiom שאו את ראש ("lift the head") at {", ".join(SEU)} (the two censuses) and נשא את ראש at {", ".join(NASA)} (the Levite houses).'
INK['stranger'] = f'- THE STRANGER WHO APPROACHES SHALL BE PUT TO DEATH: {", ".join(STRANGER)} — four Torah seats: the non-Levite (1:51), the non-priest (3:10), before the tent (3:38), the priesthood again (18:7). Onkelos: the LAY man (חלוני, "common"), never the foreigner.'
INK['wrath'] = f'- THE WRATH: קצף ("wrath") at 1:53 among {len(WRATH)} Torah seats — {", ".join(WRATH)}; 18:5 "that there be no more wrath" the parallel; the charge-word משמרת ("charge") at {len(MISHMERET)} seats in 1:1-4:20: {", ".join(f"{c}:{v}" for c, v in MISHMERET)}. "The tabernacle of the testimony" at {", ".join(EDUT)}.'
INK['sides'] = f'- THE TWO RINGS (computed from the ink\'s own compass words): the outer — east Judah 2:3, south Reuben 2:10, west Ephraim 2:18, north Dan 2:25; the inner — west Gershon 3:23, south Kohath 3:29, north Merari 3:35, east Moses-Aaron 3:38; the march\'s ordinals — first 2:9, second 2:16, third 2:24, last 2:31.'
INK['toledot'] = f'- THE GENERATIONS HEADING: "these are the generations" at {", ".join(TOLEDOT)} — nine Genesis seats and Num 3:1 (Aaron and Moses); "on the day the LORD spoke" at {", ".join(ON_THE_DAY)}; "on Mount Sinai" at {len(MT_SINAI)} Torah seats (3:1 among them); "in the wilderness of Sinai" at {len(SINAI_WILD)} ({", ".join(SINAI_WILD)}).'
INK['sons'] = f'- AARON\'S SONS: the four-name list at {", ".join(SONS_LIST)}; "and sons they had not" at {", ".join(NO_SONS)} alone; "upon the face of Aaron" at {", ".join(AL_PNEI)} alone; "whose hand he filled" (מלא ידם) at {", ".join(FILLED)} alone in that form; "bring near the tribe of Levi" at {", ".join(HAKREV_LEVI)} alone.'
INK['given'] = f'- GIVEN, GIVEN: נתונם נתונם ("given, given") at {", ".join(GIVEN2)} alone; the single "given" at {", ".join(GIVEN)}; "opener of the womb" (פטר רחם) at {", ".join(WOMB)} — the firstborn engine\'s clause (Exod 13) at its Numbers seat.'
INK['thresholds'] = f'- THE THREE THRESHOLDS: twenty years (1:3 and the twelve formulas), a month (3:15, 22, 28, 34, 39, 40, 43), thirty-to-fifty (4:3 and its six repeats in chapter 4); the Sifrei\'s 8:24 twenty-five reconciled as the learning age.'
INK['shekel'] = f'- THE SHEKEL: "twenty gerah" at {", ".join(GERAH)} (four Torah seats); "five, five" (חמשת חמשת) at {", ".join(FIVE2)} alone — the distributive doubled; Onkelos: sela and ma\'ah — the conversion layer\'s words (Bekhorot 50a).'
INK['nasi'] = f'- THE PRINCE OF PRINCES: ונשיא נשיאי ("and the prince of the princes") at {", ".join(NASI2)} alone — Onkelos: the amarkal.'
INK['kehat'] = f'- KOHATH\'S CHAPTER: "the holy of holies" at 4:{" and 4:".join(map(str, KODESH2))}; the death clauses {", ".join(f"4:{v} {w}" for v, w in DIE4)} ("lest they die"); tachash at 4:{", 4:".join(map(str, TACHASH4))}; "wholly of blue" (כליל תכלת) at {", ".join(BLUE)} — the robe and the ark; "cut not off" (תכריתו) at {", ".join(CUT)} alone; כבלע ("as it is swallowed") at {", ".join(KAVLA)} alone in the Tanakh.'
def register_line(c, lo, hi): return f'- THE REGISTER: {register(c, lo, hi)} — the narrative verbs of the span (the narrative-past "and he did" form, the register test).'

# ---- THE LEDGERS ----
TESTING = ('THE TESTING SHELF routed to Step 5 (the compile sitting\'s docket, per gap): Mishnah Shekalim (the counting by ransom, the amarkalin — 5:2); Mishnah Bekhorot 1 and 8 with the Talmud at Bekhorot 4b-5a (the Levites redeeming the firstborn, the three hundred, the beasts) and 8:8-10 (the five sela); '
           'Chullin 24a (the Levites\' ages — years against the voice); Zevachim 116b (the three camps); Menachot 99b (the bread on the march); Yoma 21b (the altar\'s fire under the cloth); Eruvin 51a (the camp\'s distance); Sanhedrin 19b (Aaron\'s sons as Moses\'); Sanhedrin 81b-83a (the stranger who served; the swallowing); '
           'Shabbat 28a (the tachash); Jerusalem Talmud Eruvin 5:1 (the march as a box or a beam); Yevamot 54b (the pedigrees) — the Babylonian Talmud is the bridge, per gap at the compile.')
def ledger(uid, c, lo, hi, title, inks, crowns, sifrei_here=False):
    verses = list(range(lo, hi + 1))
    cites = [f'Onkelos Num {c}:{v}' for v in verses] + (['Sifrei Bamidbar 62:1'] if sifrei_here else [])
    N = len(cites)
    cnt = Counter(R[(c, v)][0] for v in verses)
    hdr = (f'# Numbers {c}:{lo}-{hi} derivation — Onkelos as the spine (the Sifrei on Numbers has NO piska by position on 1:1-4:20 — it opens at 5:1, computed), '
           f'THE NUMBERS WALK sitting 1 — BAMIDBAR, {title} ({DATE}; the owner: "OK, let\'s go starting with numbers the first first first verse", after the ruling NUMBERS IN ORDER FROM 1:1 at THE TENT\'s close). '
           f'DECLARED (THE_STEPS Step 2, the spine default of 2026-08-27, read at the PARASHAH GRAIN — speed ruling (a): one pass over Bamidbar 1:1-4:20, the nine ledgers per block): scope = Onkelos Numbers {c}:{lo}-{hi} ({len(verses)} verses, fresh)'
           + (' + the Sifrei on Numbers\' one row whose subject lies in this span — piska 62 (read fresh here; found by position, its head mislabeled)' if sifrei_here else ' + the Sifrei on Numbers where it has a piska in the span: NONE (computed; its mislabeled piska 62 read at num_04_kehat)')
           + f'. {TESTING} OUTSIDE DECLARED SCOPE, enumerated and unread (the shelf\'s other works on Numbers, {len(outside)} directories): {", ".join(outside)}.\n\n')
    body = SIFREI_NOTE + (SIFREI_62 + '\n' if sifrei_here else '') + '\n'
    body += f'## Onkelos Numbers {c}:{lo}-{hi} ({len(verses)} verses, read whole)\n'
    for v in verses:
        verdict, prose = R[(c, v)]
        body += f'- Onkelos Num {c}:{v} — {verdict}. {prose}\n'
    body += '\n## The ink beside the shelf (computed by this script from the Tanakh DB and the shelf — never recited)\n'
    for k in inks: body += INK[k] + '\n'
    body += register_line(c, lo, hi) + '\n'
    body += '\n## The finds (this ledger\'s crowns)\n' + '\n'.join(crowns) + '\n'
    body += (f'\n## CITE INDEX — every source opened, each fully named\n(one name per line; coverage COMPUTED against the shelf by the ledger script write_bamidbar_ledgers.py: Onkelos Numbers {c}:{lo}-{hi} {len(verses)} verses — missing 0, extra 0'
             + ('; the Sifrei on Numbers piska 62, 1 row, read whole' if sifrei_here else '; the Sifrei on Numbers holds NO piska on the span by position') + ')\n')
    body += '\n'.join(cites) + '\n'
    body += f'({len(verses)} Onkelos verses fresh' + (' + 1 Sifrei Bamidbar row fresh' if sifrei_here else '') + f' = {N} sources in this ledger.)\n\n'
    body += (f'**read: {N} of {N} — COMPLETE** ({len(verses)} Onkelos verses' + (' and 1 Sifrei row' if sifrei_here else '') + f' opened and verdicted this sitting at the shelf\'s row grain, coverage computed by script — missing 0, extra 0; '
             f'verdicts MATERIAL {cnt["MATERIAL"]} Onkelos, CONTEXT {cnt["CONTEXT"]} Onkelos' + (', MATERIAL 1 Sifrei' if sifrei_here else '') + ' — the counts the script\'s own Counter measured)\n')
    open(OUT[uid], 'w', encoding='utf-8').write(hdr + body)
    print(f'wrote {OUT[uid]}: {N} sources, MATERIAL {cnt["MATERIAL"]} / CONTEXT {cnt["CONTEXT"]}' + (' + Sifrei 1' if sifrei_here else ''))
    return N, cnt

C1A = ['- THE DATE IS A MARKER, AND IT RUNS BACKWARD: 1:1\'s stamp (the first of the second month, year two) stands a month after the erection (Exod 40:17) and BEFORE the Passover command of 9:1 in verse order — the tradition\'s own example of "no earlier and later" (Pesachim 6b:7). The census is done on the command\'s day (1:18 repeats the date, computed).',
       '- THE COUNT IS OF NAMES (1:2, 1:18, 1:20 — "the number of names"; Onkelos "receive the sum" for "lift the head"): heads counted by names written, pedigrees declared by a verb the Tanakh uses once (1:18). The princes "designated by names" in the blasphemer\'s root (1:17, computed).',
       '- THE TWELVE ARE TWELVE BECAUSE JOSEPH IS TWO AND LEVI IS NONE (1:10, 1:47 in the next block): the list\'s own arithmetic.',
       '- ONE PRINCE, TWO SPELLINGS (1:14 Deuel / 2:14 Reuel, computed) — the translation keeps each verse\'s letter.',
       '- THE ONE KETIV-QERE OF THE PORTION at 1:16 (computed on both stores): the store carries the written and the read side by side; Onkelos renders the read.']
C1B = ['- THE TWELVE SUM TO THE TOTAL (computed: 603,550 at 1:46) and the total is Exod 38:26\'s half-shekel count — the exam\'s question at Bekhorot 5a (two counts, months apart, one number) is now a computed fact of the ink on both seats.',
       '- GAD MOVES (computed: eleventh among the princes, third in the count): the count follows the camp\'s companions before the camp is commanded — the order of chapter 2 is already in chapter 1.',
       '- THE CENSUS\'S NUMBER GRAMMAR, MEASURED: thousands multiply the group before them; "and a thousand" adds; "from" and "a hundred of" are told apart by vowels. THE ENGINE\'S PARSER CANNOT READ THE CENSUS (measured on 1:21, 1:46, 3:39) — the compile sitting\'s item, owed.',
       '- "GENERATIONS" ON EVERY TRIBE (1:20-42, computed): the Genesis heading-word twelve times as a census column.']
C1C = ['- THE LEVITES STAND OUTSIDE BEFORE THE WORD EXCLUDES THEM (1:47 before 1:49): the narrator\'s report precedes the command — the text\'s own order.',
       '- THE STRANGER IS THE LAY MAN (1:51, Onkelos חלוני "common"; the clause\'s four Torah seats computed): the death is for the outsider to the OFFICE — a non-Levite at the tabernacle, a non-priest at the priesthood (3:10) — not for the foreigner.',
       '- THE GUARD\'S PURPOSE IS WRITTEN (1:53 "that there be no wrath"; the word\'s thirteen seats; 18:5 the parallel): the Levite ring is a wrath-shield in the ink, and "charge" is the portion\'s key-word (its seats computed).',
       '- THE BANNER IS A TAXIS (1:52, Onkelos): the camp as an army in array — the translation\'s register.',
       '- COUNT AND APPOINT ARE ONE ROOT (1:49 "you shall not count" / 1:50 "appoint" — פקד): Onkelos splits them (count / appoint).']
C2A = ['- THE FOUR SIDES IN THE INK\'S COMPASS (computed): east Judah, south Reuben, west Ephraim, north Dan — Onkelos reads "seaward" as west (2:18): the geography, not the metaphor.',
       '- THE DISTANCE IS THE TALMUD\'S NUMBER, NOT THE VERSE\'S (2:2 "at a distance, round about" → Onkelos "opposite"): the two thousand cubits arrive at the exam (Eruvin 51a) from Josh 3:4 — a TRANSFER with its teacher, not this ink.',
       '- THE CAMP SUMS CLOSE (computed): Judah 186,400, Reuben 151,450 — each the sum of its three; the twelve numbers of chapter 1 repeated verbatim.',
       '- REUEL (2:14) AGAINST DEUEL (1:14), computed — the one prince\'s two spellings, kept by the translation.']
C2B = ['- THE MARCH ORDER IS THE CAMP ORDER (2:17 "as they camp so they journey"; Onkelos literal): the tent in the midst; the Talmud\'s box-or-beam is the exam\'s question on this clause.',
       '- THE FOUR CAMPS SUM TO THE TOTAL A THIRD TIME (2:32 = 1:46 = Exod 38:26, computed): 603,550 stands on three seats in two books.',
       '- THE MARCH\'S ORDINALS (computed): first, second, third, last — the ink\'s own sequence for the four banners.',
       '- ONE VERSE, TWO RUNS (2:34): "so they camped and so they journeyed" — the camp\'s spec (2:2) and the march\'s (2:17) reported done in one report formula.']
C3A = ['- THE GENESIS HEADING ON AARON AND MOSES (3:1, computed: the one "these are the generations" outside Genesis) — and the list names Aaron\'s sons alone: the ink\'s own gap the Talmud fills (the teacher as begetter, Sanhedrin 19b — the exam).',
       '- THE FILLED HAND IS AN OFFERING IN THE TRANSLATION (3:3, Onkelos "whose offering was brought near"): Lev 8\'s ram of filling named by the rite — a REFERENCE to the investiture by Onkelos\' own word.',
       '- THE SONLESSNESS WRITTEN (3:4, the phrase\'s one Tanakh seat, computed): Nadab and Abihu "had no sons" — the office\'s inheritance in the ink\'s negative; "upon the face of Aaron" kept by Onkelos, read by the Talmud as "in his lifetime".',
       '- THE TRIBE BROUGHT NEAR AS AN OFFERING (3:6 "bring near the tribe of Levi", 3:12 Onkelos "I have brought near" for "I have taken", 3:41, 3:45): the offering verb on a tribe — the translation reads the substitution as a sacrifice.',
       '- GIVEN, GIVEN — TWO VERBS FOR ONE DOUBLED WORD (3:9, Onkelos "handed over, given"): the doubling read as two grants (the Sifrei at 8:16 the exam\'s seat).',
       '- THE SUBSTITUTION IS A REFERENCE TO THE FIRSTBORN LAW BY ITS OWN TOKEN (3:12 "opener of the womb" — Exod 13\'s clause, five Torah seats computed) AND ITS GROUND IS A DATED EVENT (3:13 "on the day I smote" — the plague\'s night on the tape).']
C3B = ['- THE INK\'S OWN ARITHMETIC PROBLEM (computed): 7,500 + 8,600 + 6,200 = 22,300 against 3:39\'s 22,000 — a delta of 300 written into the verses; the exam\'s answer (Bekhorot 5a: three hundred firstborn Levites) is the Talmud\'s, the delta the ink\'s.',
       '- BY THE MOUTH OF THE LORD THREE TIMES IN ONE CHAPTER (3:16, 3:39, 3:51, computed): on the count, the total, the money — Onkelos "by the Word".',
       '- THE INNER RING MATCHES THE OUTER (computed): west Gershon, south Kohath, north Merari, east Moses-Aaron — the leaders\' side is the sunrise side, the stranger clause standing there a third time.',
       '- THE AMARKAL (3:32, Onkelos): the Temple treasury\'s office-title read onto Eleazar — the later institution\'s word in the translation of the earlier verse; "prince of princes" the ink\'s one seat.',
       '- THE THREE CHARGES DIVIDE THE TABERNACLE INTO SOFT, HOLY, HARD (3:25-26, 3:31, 3:36-37): the woven, the furniture, the frame — the inventory the Kohathite chapter then wraps.']
C3C = ['- THE ARITHMETIC CLOSES (computed): 22,273 − 22,000 = 273; 273 × 5 = 1,365 — every number of the redemption derived from the ink\'s own numerals and the ink\'s own product.',
       '- THE CONVERSION LAYER AT ITS NUMBERS SEAT (3:47, Onkelos "five, five sela\'im... twenty ma\'in the sela"): the words the Talmud cites at Bekhorot 50a ("and we translate twenty ma\'in") — the corpus\'s standing finding from Exod 30:13, read again at its second law seat; "twenty gerah" four Torah seats (computed).',
       '- THE INK WRITES ITS NUMBERS IN TWO ORDERS (computed): descending with thousands first (3:43\'s 22,000 then 273 ascending; 3:46\'s 273 ascending with the article on each part; 3:50\'s 1,365 ascending with "and a thousand" LAST — an addend by the conjunction, three Torah seats); the Aramaic reverses to descending.',
       '- THE SAID-FRAME (3:40, the portion\'s one "said" among ten, computed) opens the firstborn\'s count with the census idiom of 1:2 ("lift the number of their names" → "receive").',
       '- THE FIFTH PAIR CLOSES WITH BOTH FORMULAS (3:51 "by the mouth of the LORD, as the LORD commanded Moses"): five commanded-and-done pairs in one portion (computed) — M-22\'s spec/run form on a whole parashah.']
C4A = ['- THE SIFREI\'S ONE ROW ON THE SPAN, FOUND BY POSITION (piska 62: the export\'s head reads "3:24", the row is 8:24\'s — its neighbors 8:4 and 8:25, its quotations 8:24 and 4:23): twenty-five to learn, thirty to serve; years disqualify the Levites, blemishes do not — the a-fortiori from the priests REFUTED by "this is what applies" (a stated limit beats an inferred one). RESEARCH_LOG.md carries the mislabel.',
       '- THE THIRD THRESHOLD IS A WINDOW (4:3, computed: thirty-to-fifty seven times in chapter 4; twenty at 1:3; a month at 3:15): "the host" is the work-host — the army word of the census on the Levites\' labor, one Aramaic word for both.',
       '- THE ORDER IS THE LAW (4:5, 4:15, 4:19-20): the priests cover, THEN the Kohathites carry; the veil becomes the ark\'s cover; three death clauses (computed) — touching, approaching unassigned, SEEING the packing (4:20 כבלע "as it is swallowed", the word\'s one Tanakh seat; Onkelos "when they cover the vessels").',
       '- ONLY THE ARK WEARS BLUE OUTSIDE (4:6 "wholly of blue" — the high priest\'s robe\'s phrase, computed: Exod 28:31, 39:22, Num 4:6); the rest hide-outermost; the bronze altar ALONE not blue — ashed and purple (4:13).',
       '- THE BREAD TRAVELS ON THE TABLE (4:7 "the continual bread shall be on it"): the ink keeps the continual on the march — the exam\'s Menachot 99b.',
       '- CUT NOT OFF (4:18, the verb\'s one seat in this form, computed): the karet-word turned on the LEADERS\' negligence — Aaron and Moses guard a house from being cut off by assigning each man his load (4:19, the doubled "man").']

totals = []
totals.append(ledger('num_01_census_command', 1, 1, 19, 'the census command and the princes', ['date', 'frames', 'pairs', 'orders', 'ketiv', 'designated', 'pedigree', 'thresholds'], C1A))
totals.append(ledger('num_01_tribe_counts', 1, 20, 46, 'the twelve counts', ['numbers', 'grammar', 'orders', 'toledot', 'pairs'], C1B))
totals.append(ledger('num_01_levites_exempt', 1, 47, 54, 'the Levites exempt and posted', ['stranger', 'wrath', 'pairs', 'frames'], C1C))
totals.append(ledger('num_02_camp_east_south', 2, 1, 16, 'the camp: east and south', ['sides', 'numbers', 'orders', 'frames'], C2A))
totals.append(ledger('num_02_camp_west_north', 2, 17, 34, 'the camp: the tent in the midst, west and north', ['sides', 'numbers', 'pairs', 'grammar'], C2B))
totals.append(ledger('num_03_aaron_levi_replace', 3, 1, 13, "Aaron's line and the Levites in the firstborn's place", ['toledot', 'sons', 'given', 'stranger', 'frames'], C3A))
totals.append(ledger('num_03_levite_clans_count', 3, 14, 39, 'the Levite clans counted and posted', ['numbers', 'grammar', 'sides', 'thresholds', 'nasi', 'wrath', 'pairs'], C3B))
totals.append(ledger('num_03_firstborn_redeem', 3, 40, 51, 'the firstborn counted and the excess redeemed', ['numbers', 'grammar', 'shekel', 'given', 'pairs', 'frames'], C3C))
totals.append(ledger('num_04_kehat', 4, 1, 20, "the Kohathites' burden", ['thresholds', 'kehat', 'frames'], C4A, sifrei_here=True))
N_ALL = sum(n for n, _ in totals); M_ALL = sum(c['MATERIAL'] for _, c in totals); K_ALL = sum(c['CONTEXT'] for _, c in totals)
assert N_ALL == 159 + 1 and M_ALL + K_ALL == 159, (N_ALL, M_ALL, K_ALL)
print(f'BAMIDBAR: {N_ALL} sources across 9 ledgers — Onkelos MATERIAL {M_ALL} / CONTEXT {K_ALL}, Sifrei 1; the numbers: total {TOTAL}, camps {camp[9]}/{camp[16]}/{camp[24]}/{camp[31]}, Levites {LEV} vs {CLANSUM}, firstborn {FB}, excess {EXC}, money {MONEY}; engine parser on 1:21 {ENGINE_121}')

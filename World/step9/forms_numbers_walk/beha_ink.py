#!/usr/bin/env python3
# THE NUMBERS WALK, sitting 3 — BEHA'ALOTCHA (2026-09-10; the owner: "Ok continue to next numbers span"): THE INK OF Numbers 8:1-26
# and 10:1-12:16 (chapter 9 frozen at THE TENT sitting 2 and SKIPPED, as the ruling says), computed from the Tanakh DB, the snapshot
# store and the shelf's own bytes — never typed. Sitting 2's form (naso_ink.py): the heads found BY POSITION and asserted; coverage
# computed; every cut by consonants (the misses collected, asserted empty); the engine's numeral parser MEASURED against the
# portion's numbers; the hand's facts as asserts, run all at once by assert_driver.py; every gloss of a narrative verb the STORE'S
# OWN (words.gloss), never typed. Shared by beha_rows_onkelos.py, beha_rows_sifrei.py and write_beha_ledgers.py.
import json, os, re, html, sqlite3, sys, io, contextlib, unicodedata
from collections import Counter
ROOT = '<repo-old>'
DATE = '2026-09-10'
UNITS = [  # (uid, chapter, lo, hi, title, the Sifrei piskaot by position)
    ('num_08_menorah_levites', 8, 1, 26, 'the lamps toward the face; the Levites purified, waved and given; their ages', [59, 60, 61, 62, 63]),
    ('num_10_trumpets_depart', 10, 1, 36, 'the two trumpets; the first march in the camp\'s order; Hobab; the ark of three days; the section between the signs', list(range(72, 85))),
    ('num_11_complaint_quail', 11, 1, 35, 'Taberah; the lust for flesh against the manna; the seventy elders and the two in the camp; the quail and the graves of lust', list(range(85, 99))),
    ('num_12_miriam', 12, 1, 16, 'Miriam and Aaron against Moses; mouth to mouth; the leprosy and the seven days', list(range(99, 107))),
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
# THE SHELF'S ROWS ON BEHA'ALOTCHA, BY POSITION: piska 59 has no parsable head (the menorah — between 58 on 7:89 and 60 on 8:3 its
# row is 8:2's); 62 is headed "3:24" (the digit mistyped — 8:24, RESEARCH_LOG.md's first report; READ at num_04_kehat's ledger where
# its 4:23 arm was the subject: CREDITED here); 80 is headed "10:30" but opens "do not leave us" — 10:31's words, between 79 on 10:30
# and 81 on 10:32 (a third mistyped head, the same defect class); 102 is headed "Ibid. 4" (12:4 by position, between 101 on 12:3 and
# 103 on 12:6); piskaot 64-71 head inside chapter 9 (FROZEN at THE TENT sitting 2 — read at num_09_pesach_cloud's ledger, skipped
# here); 107 heads 15:2 (Shelach's).
assert heads[58] == ('Bamidbar', 7, 89) and heads[59] is None and heads[60] == ('Bamidbar', 8, 3) and heads[61] == ('Bamidbar', 8, 4), (heads[58], heads[59], heads[60], heads[61])
assert heads[62] == ('Bamidbar', 3, 24) and heads[63] == ('Bamidbar', 8, 25) and 'twenty-five' in clean(sif[61][0])[:120] and '8:24' in clean(sif[61][0])
assert heads[64] == ('Bamidbar', 9, 1) and heads[71] == ('Bamidbar', 9, 14) and heads[72] == ('Bamidbar', 10, 2), (heads[64], heads[71], heads[72])
assert heads[79] == ('Bamidbar', 10, 30) and heads[80] == ('Bamidbar', 10, 30) and heads[81] == ('Bamidbar', 10, 32) and 'do not leave us' in clean(sif[79][0])[:120]
assert heads[101] == ('Bamidbar', 12, 3) and heads[102] is None and heads[103] == ('Bamidbar', 12, 6) and 'Ibid. 4' in clean(sif[101][0])[:40] and 'suddenly' in clean(sif[101][0])[:80]
assert heads[106] == ('Bamidbar', 12, 14) and heads[107] == ('Bamidbar', 15, 2), (heads[106], heads[107])
HEAD_FIX = {59: (8, 2), 62: (8, 24), 80: (10, 31), 102: (12, 4)}
def head(p): return HEAD_FIX.get(p) or heads[p][1:]
PISKAOT = [p for u in UNITS for p in u[5]]
assert PISKAOT == list(range(59, 64)) + list(range(72, 107)) and len(PISKAOT) == 40
for p in PISKAOT:
    if p not in HEAD_FIX: assert heads[p] and heads[p][0] == 'Bamidbar', (p, heads[p])
for a, b in zip(PISKAOT, PISKAOT[1:]):
    if b != 72: assert head(b) >= head(a), (a, b, head(a), head(b))     # monotone by position once the four heads are placed
for uid, c, lo, hi, _, ps in UNITS:
    for p in ps: assert (c, lo) <= head(p) <= (c, hi), (uid, p, head(p))
for p in range(64, 72): assert (9, 1) <= head(p) <= (9, 14), (p, head(p))   # chapter 9's rows — the frozen chapter's
SIF_ROWS = {p: len(sif[p - 1]) for p in PISKAOT}
assert sum(SIF_ROWS.values()) == 51 and SIF_ROWS[73] == 3 and SIF_ROWS[78] == 3 and SIF_ROWS[83] == 3 and SIF_ROWS[84] == 5 and SIF_ROWS[95] == 2, SIF_ROWS
assert all(SIF_ROWS[p] == 1 for p in PISKAOT if p not in (73, 78, 83, 84, 95))
ONK_LEN = {c: len(onk[c - 1]) for c in range(8, 14)}
assert ONK_LEN == {8: 26, 9: 23, 10: 36, 11: 35, 12: 16, 13: 33} and {c: len(onk_he[c - 1]) for c in range(8, 14)} == ONK_LEN, ONK_LEN
shelf_numbers = sorted(d for d in os.listdir(f'{ROOT}/Data/sefaria_export') if re.search(r'Numbers|Bamidbar', d))
outside = [d for d in shelf_numbers if d not in ('Sifrei_Bamidbar', 'Onkelos_Numbers')]
assert len(outside) == 23, len(outside)
# THE PRIOR READS (grep of logic/oral_triage at the sitting): piska 62 at num_04_kehat's ledger (CREDITED); 64-71 at num_09's (the frozen
# chapter, skipped); no other row of 59-63 / 72-106 and no Onkelos verse of chapters 8, 10, 11, 12 read by any prior ledger — FRESH
TRI = f'{ROOT}/logic/oral_triage'
LED = {f: open(f'{TRI}/{f}', encoding='utf-8').read() for f in os.listdir(TRI) if f.endswith('.md') and f'{TRI}/{f}' not in OUT.values()}   # the sitting's own ledgers are not a prior read
KEHAT = 'num_04_kehat_2026-09-09.md'; NUM09 = 'num_09_pesach_cloud_2026-09-09.md'
assert 'Sifrei Bamidbar 62:1' in LED[KEHAT] and all(f'Sifrei Bamidbar {p}:{r}' in LED[NUM09] for p in range(64, 72) for r in range(1, len(sif[p - 1]) + 1))
prior = sorted(f for f, t in LED.items() if re.search(r'Sifrei Bamidbar (59|6[013]|7[2-9]|8\d|9\d|10[0-6]):\d', t))
assert prior == [], prior
prior_onk = sorted(f for f, t in LED.items() if re.search(r'Onkelos Num (8|10|11|12):\d', t))
assert prior_onk == [], prior_onk

# ---- THE DRAFTS' SPANS AND THE BOUNDARIES, COMPUTED ----
db = sqlite3.connect(f'file:{ROOT}/elijah_docket/tanakh.sqlite?mode=ro', uri=True)
VC = dict(db.execute("SELECT chapter, COUNT(*) FROM verses WHERE book='Num' GROUP BY chapter").fetchall())
assert VC[8] == 26 and VC[9] == 23 and VC[10] == 36 and VC[11] == 35 and VC[12] == 16 and VC[13] == 33
def unit_text(uid): return open(f'{ROOT}/logic/units/{uid}.yaml', encoding='utf-8').read()
def steps(uid): return sorted({(int(a), int(b)) for a, b in re.findall(r'STEP_Nm_(\d+)_(\d+)', unit_text(uid))})
for uid, c, lo, hi, _, _ in UNITS:
    st = steps(uid); assert st == [(c, v) for v in range(lo, hi + 1)], (uid, st[:2], st[-2:])
    assert 'status: draft' in unit_text(uid), uid
assert 'status: frozen' in unit_text('num_09_pesach_cloud') and steps('num_09_pesach_cloud') == [(9, v) for v in range(1, 24)]
assert steps('num_13_spies_sent')[0] == (13, 1) and 'status: draft' in unit_text('num_13_spies_sent')   # the next portion opens at 13:1 (Shelach)
SPAN = [(c, v) for (_, c, lo, hi, _, _) in UNITS for v in range(lo, hi + 1)]
assert len(SPAN) == 113 == 26 + 36 + 35 + 16 and SPAN[0] == (8, 1) and SPAN[-1] == (12, 16) and (9, 1) not in SPAN

# ---- THE INK, computed from the Tanakh DB and the snapshot store ----
def plain(w): return ''.join(c for c in w if c != '/' and not (0x0591 <= ord(c) <= 0x05C7))
def pointed(w): return ''.join(c for c in w if c != '/' and not (0x0591 <= ord(c) <= 0x05AF))
def accents(w): return [unicodedata.name(c).replace('HEBREW ACCENT ', '') for c in w if 0x0591 <= ord(c) <= 0x05AE]
rows = db.execute("SELECT v.book, v.chapter, v.verse, w.he, w.morph FROM words w JOIN verses v ON w.verse_id=v.id ORDER BY v.id, w.idx").fetchall()
by, byp, byraw = {}, {}, {}
for b, c, v, he, m in rows:
    by.setdefault((b, c, v), []).append((plain(he), m)); byp.setdefault((b, c, v), []).append(pointed(he)); byraw.setdefault((b, c, v), []).append(he)
T = ('Gen', 'Exod', 'Lev', 'Num', 'Deut')
def words(b, c, v): return [x for x, _ in by[(b, c, v)]]
def hits(sub, books=None, exact=False): return sorted({f'{b} {c}:{v}' for (b, c, v), ws in by.items() if (books is None or b in books) and any((x == sub) if exact else (sub in x) for x, _ in ws)})
def count_tok(tok, books=None): return sum(1 for (b, c, v), ws in by.items() if (books is None or b in books) for x, _ in ws if x == tok)
def phrase(seq, books=T):
    out = []
    for (b, c, v), ws in by.items():
        if books is not None and b not in books: continue
        w = [x for x, _ in ws]
        if any(w[i:i + len(seq)] == list(seq) for i in range(len(w) - len(seq) + 1)): out.append(f'{b} {c}:{v}')
    return sorted(out)
def nphrase(seq, b, c, v):
    w = words(b, c, v); return sum(1 for i in range(len(w) - len(seq) + 1) if w[i:i + len(seq)] == list(seq))
FAIL = []
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
def aramaic(c, v): return [plain(x) for x in clean(onk_he[c - 1][v - 1]).rstrip(':').split()]
def numword(n): return f'{n:,}'
# THE STORE'S OWN GLOSSES — every English beside a narrative verb is the snapshot store's words.gloss, never typed
store = sqlite3.connect(f'file:{ROOT}/torah_grok.SNAPSHOT-main-51801ca.sqlite?mode=ro', uri=True)
SG = {}
for c, v, hp, g in store.execute("SELECT v.chapter, v.verse, w.he_plain, w.gloss FROM words w JOIN verses v ON w.verse_id=v.id WHERE v.book='Num' AND v.chapter BETWEEN 8 AND 12 ORDER BY v.id, w.idx"):
    SG.setdefault((c, v), []).append((hp.replace('/', ''), g))
def sg(c, v, tok):
    for hp, g in SG[(c, v)]:
        if hp == tok: return g
    raise KeyError((c, v, tok))

# THE ENGINE'S PARSER (taught the census at 1b; measured again at Naso) on Beha'alotcha's numbers — MEASURED before the compile is asked
sys.path.insert(0, f'{ROOT}/World/step9')
with contextlib.redirect_stdout(io.StringIO()):
    import cold_run_sequence as CS
def N(b, c, v): return CS.ink_numbers(CS.verse_words(b, c, v))
RIGHT = {k: N('Num', *k) for k in [(8, 2), (8, 24), (8, 25), (10, 4), (10, 11), (10, 33), (11, 16), (11, 21), (11, 24), (11, 25), (11, 32), (12, 14), (12, 15)]}
assert RIGHT == {(8, 2): [7], (8, 24): [25], (8, 25): [50], (10, 4): [1], (10, 11): [20], (10, 33): [3, 3], (11, 16): [70], (11, 21): [600000], (11, 24): [70], (11, 25): [70], (11, 32): [10], (12, 14): [7, 7], (12, 15): [7]}, RIGHT
GAPS = {k: N('Num', *k) for k in [(10, 2), (11, 26), (11, 19), (11, 31), (10, 36)]}
assert GAPS == {(10, 2): [], (11, 26): [], (11, 19): [1, 5, 10, 20], (11, 31): [], (10, 36): []}, GAPS   # the wrong or silent readings, typed from the measurement
GAPS_TRUE = {(10, 2): [2], (11, 26): [2], (11, 19): [1, 2, 5, 10, 20], (11, 31): [2], (10, 36): 'the shelf reads 22,000 (two myriads, two thousands — Sifrei 84:5); the ink writes two plural nouns'}
EXTRA = {'Num 12:4': N('Num', 12, 4), 'Exod 25:10': N('Exod', 25, 10), '1Kgs 6:1': N('1Kgs', 6, 1), '1Chr 23:24': N('1Chr', 23, 24), '1Chr 23:27': N('1Chr', 23, 27), 'Ezra 3:8': N('Ezra', 3, 8), '2Chr 31:17': N('2Chr', 31, 17), 'Num 4:3': N('Num', 4, 3)}

# THE SIGNS AND THE WRITTEN-AND-READ PAIR
NUNS = db.execute("SELECT v.chapter, v.verse, m.after_idx FROM marks m JOIN verses v ON v.id=m.verse_id WHERE v.book='Num' AND m.kind='x-reversednun' ORDER BY v.id").fetchall()
NUNS_ALL = db.execute("SELECT v.book, v.chapter, v.verse FROM marks m JOIN verses v ON v.id=m.verse_id WHERE m.kind='x-reversednun' ORDER BY v.id").fetchall()
LETTERS_3536 = sum(len(x) for x, _ in by[('Num', 10, 35)]) + sum(len(x) for x, _ in by[('Num', 10, 36)])
STORE_NUN = store.execute("SELECT COUNT(*) FROM words WHERE he LIKE '%׆%'").fetchone()[0]
UNPOINTED = [(c, v, i) for (c, v) in SPAN for i, h in enumerate(byraw[('Num', c, v)]) if not any(0x05B0 <= ord(ch) <= 0x05BC for ch in h)]
NOTE_12_3 = db.execute("SELECT n.after_idx, n.ntype, n.content FROM notes n JOIN verses v ON v.id=n.verse_id WHERE v.book='Num' AND v.chapter=12 AND v.verse=3").fetchall()
STORE_12_3 = [r[0] for r in store.execute("SELECT w.he_plain FROM words w JOIN verses v ON w.verse_id=v.id WHERE v.book='Num' AND v.chapter=12 AND v.verse=3 ORDER BY w.idx")]

# THE FRAMES AND THE REGISTER
FR = [(c, v) for (c, v) in SPAN if words('Num', c, v)[0] in ('וידבר', 'ויאמר') and words('Num', c, v)[1] == 'יהוה']
FR_SAID = [(c, v) for c, v in FR if words('Num', c, v)[0] == 'ויאמר']
REG = {}
for (c, v) in SPAN:
    vs = [(x, [q for q in m.split('/') if 'V' in q][0]) for x, m in by[('Num', c, v)] if m and re.search(r'V.w', m)]
    if vs: REG[(c, v)] = [f'{x} ("{sg(c, v, x)}", {m})' for x, m in vs]
def register(c, lo, hi): return '; '.join(f'{c}:{v} ' + ', '.join(REG[(c, v)]) for v in range(lo, hi + 1) if (c, v) in REG) or 'no narrative verb'


# ---- THE MEASURED FACTS (printed by the first pass — scratchpad beha_measure1.out — then typed here as asserts; assert_driver.py
# runs every statement and lists every failure at once) ----
assert EXTRA['1Kgs 6:1'] == [480] and EXTRA['1Chr 23:24'] == [20] and EXTRA['1Chr 23:27'] == [20] and EXTRA['Ezra 3:8'] == [20] and EXTRA['2Chr 31:17'] == [20] and EXTRA['Num 4:3'] == [30, 50], EXTRA
assert EXTRA['Num 12:4'] == [] and EXTRA['Exod 25:10'] == [], EXTRA   # the suffixed numeral "the three of you" and the dual "two cubits and a half" — silent (recorded)
# THE SIGNS: the Tanakh DB carries the two inverted nuns as marks after 10:34 and after 10:36 (the section 10:35-36 between them); nine in
# the Tanakh (Psalm 107's seven); the section's letters are EIGHTY-FIVE — Rebbi's number (Sifrei 84:1); the snapshot store has no nun token
assert NUNS == [(10, 34, 6), (10, 36, 6)] and len(NUNS_ALL) == 9 and [k for k in NUNS_ALL if k[0] == 'Ps'] == [('Ps', 107, v) for v in (20, 21, 22, 23, 24, 25, 39)], NUNS_ALL
assert LETTERS_3536 == 85 and STORE_NUN == 0, (LETTERS_3536, STORE_NUN)
# THE WRITTEN-AND-READ PAIR of the portion: 12:3's "humble" written ענו, read עניו — the Tanakh DB's one unpointed token with its variant note;
# the snapshot store carries BOTH tokens side by side (as at 1:16)
assert UNPOINTED == [(12, 3, 2)] and NOTE_12_3 == [(2, 'variant', 'ענועָנָ֣יו')] and STORE_12_3[2:4] == ['ענו', 'עניו'], (UNPOINTED, NOTE_12_3, STORE_12_3)
# THE FRAMES AND THE REGISTER
assert FR == [(8, 1), (8, 5), (8, 23), (10, 1), (11, 16), (11, 23), (12, 4), (12, 14)] and FR_SAID == [(11, 16), (11, 23), (12, 4), (12, 14)], (FR, FR_SAID)
assert len(REG) == 54 and REG[(12, 1)] == ['ותדבר ("and-speak", Vpw3fs)'] and len(REG[(11, 1)]) == 5 and len(REG[(11, 25)]) == 6 and len(REG[(8, 21)]) == 4, (len(REG), REG.get((12, 1)))
assert sorted(c for c, v in REG) and Counter(c for c, v in REG) == {8: 8, 10: 11, 11: 22, 12: 13}, Counter(c for c, v in REG)
# CHAPTER 8
MENORAH_FACE = phrase(['מול', 'פני', 'המנורה']); assert MENORAH_FACE == ['Num 8:2', 'Num 8:3'] and phrase(['מול', 'פני', 'המנרה']) == []   # the lampstand spelled plene at both
SEVEN_LAMPS = phrase(['שבעת', 'הנרות']); assert SEVEN_LAMPS == ['Num 8:2']
MIKSHAH = hits('מקשה', T); assert MIKSHAH == ['Exod 25:18', 'Exod 25:31', 'Exod 25:36', 'Exod 37:17', 'Exod 37:22', 'Exod 37:7', 'Num 10:2', 'Num 8:4'] and words('Num', 8, 4).count('מקשה') == 2, MIKSHAH
YEREKH = hits('ירכה', T); PERACH = hits('פרחה', T); assert YEREKH == ['Exod 25:31', 'Exod 37:17', 'Num 5:27', 'Num 8:4'] and PERACH == ['Lev 13:20', 'Lev 13:25', 'Num 8:4'], (YEREKH, PERACH)
assert phrase(['עד', 'ירכה', 'עד', 'פרחה'], None) == ['Num 8:4'] and phrase(['כמראה', 'אשר', 'הראה']) == ['Num 8:4'] and phrase(['אשר', 'אתה', 'מראה']) == ['Exod 25:40']
MEI_CHATAT = phrase(['מי', 'חטאת'], None); MEI_NIDDAH = phrase(['מי', 'נדה'], None); assert MEI_CHATAT == ['Num 8:7'] and MEI_NIDDAH == ['Num 19:13', 'Num 19:20'] and 'חטאת' in words('Num', 19, 9) and 'נדה' in words('Num', 19, 9)
TAAR = sorted(set(hits('תער', T, True) + hits('התער', T, True))); assert TAAR == ['Num 6:5', 'Num 8:7'], TAAR
TENUFAH8 = [v for v in range(1, 27) if 'תנופה' in words('Num', 8, v)]; assert TENUFAH8 == [11, 13, 15, 21] and 'והניף' in words('Num', 8, 11) and 'וינף' in words('Num', 8, 21)
NETUNIM = {k: [plain(x) for x in byraw[('Num',) + k] if plain(x).startswith('נת')] for k in [(3, 9), (8, 16), (8, 19), (18, 6)]}
assert NETUNIM == {(3, 9): ['נתונם', 'נתונם'], (8, 16): ['נתנים', 'נתנים'], (8, 19): ['נתנים'], (18, 6): ['נתנים']}, NETUNIM   # DOUBLED at 3:9 AND 8:16 — two spellings; single at 8:19, 18:6
assert 'לו' in words('Num', 3, 9) and words('Num', 8, 16).count('לי') == 2 and 'לי' in words('Num', 8, 17) and 'לי' in words('Num', 8, 14)
BNEI_819 = sum(1 for w in [words('Num', 8, 19)] for i in range(len(w) - 1) if w[i] in ('בני', 'בבני') and w[i + 1] == 'ישראל'); assert BNEI_819 == 5, BNEI_819
LI_SEATS = [('Exod', 28, 41), ('Num', 8, 14), ('Lev', 25, 55), ('Num', 8, 17), ('Exod', 25, 8), ('Exod', 20, 24), ('Exod', 30, 31), ('1Sam', 16, 1), ('Num', 28, 2), ('Num', 11, 16)]
assert all('לי' in words(*k) for k in LI_SEATS)   # the Sifrei's ten "unto Me" seats (92:1), each on the ink
PETER = hits('פטרת', None, True); WOMB = sorted(set(phrase(['פטר', 'כל', 'רחם'], None) + phrase(['פטר', 'רחם'], None) + phrase(['פטרת', 'כל', 'רחם'], None)))
assert PETER == ['Num 8:16'] and WOMB == ['Exod 13:12', 'Exod 13:15', 'Exod 13:2', 'Exod 34:19', 'Ezek 20:26', 'Num 18:15', 'Num 3:12', 'Num 8:16'], (PETER, WOMB)   # 8:16's feminine form the one seat
AGES = {'thirty': phrase(['מבן', 'שלשים', 'שנה'], None), 'twenty-five': phrase(['מבן', 'חמש', 'ועשרים', 'שנה'], None), 'fifty': phrase(['ומבן', 'חמשים', 'שנה'], None), 'twenty': [s for s in phrase(['מבן', 'עשרים', 'שנה'], None) if s.split()[0] in ('1Chr', '2Chr', 'Ezra')]}
assert AGES == {'thirty': ['1Chr 23:3', 'Num 4:23', 'Num 4:3', 'Num 4:30', 'Num 4:35', 'Num 4:39', 'Num 4:43', 'Num 4:47'], 'twenty-five': ['Num 8:24'], 'fifty': ['Num 8:25'], 'twenty': ['1Chr 23:24', '1Chr 23:27', '2Chr 31:17', 'Ezra 3:8']}, AGES
assert phrase(['ושרת', 'את', 'אחיו'], None) == ['Num 8:26'] and phrase(['ויעש', 'כן', 'אהרן'], None) == ['Num 8:3'] and hits('ויתחטאו', None, True) == ['Num 8:21']
assert phrase(['מבן', 'עשרים', 'שנה', 'ומעלה'], ('1Chr',)) == ['1Chr 23:24'] and words('1Chr', 23, 27)[-4:] == ['מבן', 'עשרים', 'שנה', 'ולמעלה'] and 'לשאת' in words('1Chr', 23, 26) and 'המשכן' in words('1Chr', 23, 26)   # Chronicles' own reason: no more carrying
# CHAPTER 10
assert words('Num', 10, 2)[2:5] == ['שתי', 'חצוצרת', 'כסף']
TRUMPET_SPELL = [(v, plain(x)) for v in range(1, 11) for x in byraw[('Num', 10, v)] if 'חצצר' in plain(x) or 'חצוצר' in plain(x)]
assert TRUMPET_SPELL == [(2, 'חצוצרת'), (8, 'בחצצרות'), (9, 'בחצצרות'), (10, 'בחצצרת')], TRUMPET_SPELL   # THREE SPELLINGS in one chapter
TRUMPET_T = sorted(set(hits('חצצר', T) + hits('חצוצר', T))); assert TRUMPET_T == ['Num 10:10', 'Num 10:2', 'Num 10:8', 'Num 10:9', 'Num 31:6'], TRUMPET_T
TEKIOT = [(v, x) for v in range(1, 11) for x in words('Num', 10, v) if 'תקע' in x or 'תרוע' in x or 'תריע' in x or 'הרע' in x]
assert [x for _, x in TEKIOT] == ['ותקעו', 'יתקעו', 'ותקעתם', 'תרועה', 'ותקעתם', 'תרועה', 'תרועה', 'יתקעו', 'תתקעו', 'תריעו', 'יתקעו', 'והרעתם', 'ותקעתם'], TEKIOT
TEKIAH_N = sum(1 for _, x in TEKIOT if 'תקע' in x); TERUAH_N = len(TEKIOT) - TEKIAH_N; assert (TEKIAH_N, TERUAH_N) == (8, 5)
assert hits('למקרא', T) == ['Num 10:2'] and phrase(['ולמסע', 'את', 'המחנות'], None) == ['Num 10:2'] and phrase(['לחקת', 'עולם', 'לדרתיכם']) == ['Num 10:8'] and phrase(['וביום', 'שמחתכם'], None) == ['Num 10:10']
assert words('Num', 10, 11)[:7] == ['ויהי', 'בשנה', 'השנית', 'בחדש', 'השני', 'בעשרים', 'בחדש'] and hits('למסעיהם', None, True) == ['Exod 17:1', 'Num 10:12', 'Num 10:6', 'Num 33:2']
BY_MOUTH_HAND = phrase(['על', 'פי', 'יהוה', 'ביד', 'משה'], None); assert BY_MOUTH_HAND == ['Josh 22:9', 'Num 10:13', 'Num 4:37', 'Num 4:45', 'Num 9:23'], BY_MOUTH_HAND   # 4:49 splits the formula; Joshua 22:9 runs it
def princes(c, lo, hi):
    out = []
    for v in range(lo, hi + 1):
        w = words('Num', c, v)
        for i, x in enumerate(w):
            if x == 'בן' and i > 0 and i + 1 < len(w) and w[i - 1] != 'אחד': out.append((w[i - 1], w[i + 1]))
    return out
P1, P2, P7, P10 = princes(1, 5, 15), princes(2, 3, 31), princes(7, 12, 83), princes(10, 14, 27)
P7 = [p for i, p in enumerate(P7) if i % 2 == 0]   # each prince twice in chapter 7 (the day-head and the closing formula)
assert len(P1) == len(P2) == len(P7) == len(P10) == 12
NAMES = lambda ps: [a for a, _ in ps]
assert NAMES(P2) == NAMES(P7) == NAMES(P10) and NAMES(P1) != NAMES(P2)   # the march's order = the camp's = the dedication's; not the census list's
assert NAMES(P10) == ['נחשון', 'נתנאל', 'אליאב', 'אליצור', 'שלמיאל', 'אליסף', 'אלישמע', 'גמליאל', 'אבידן', 'אחיעזר', 'פגעיאל', 'אחירע']
DELTA_10_1 = [(a, f1, f10) for (a, f1), (_, f10) in zip(sorted(P1), sorted(P10)) if f1 != f10]
assert DELTA_10_1 == [('אבידן', 'גדעני', 'גדעוני'), ('אליאב', 'חלן', 'חלון'), ('גמליאל', 'פדהצור', 'פדה'), ('שלמיאל', 'צורישדי', 'צורי')], DELTA_10_1   # four fathers spelled otherwise at the march
assert hits('חלון', ('Num',), True) == ['Num 10:16'] and hits('גדעוני', ('Num',), True) == ['Num 10:24'] and hits('צורי', ('Num',), True) == ['Num 10:19', 'Num 2:12'] and hits('פדה', ('Num',), True) == ['Num 10:23', 'Num 18:15', 'Num 7:54', 'Num 7:59']   # 18:15's 'redeem' a homograph of the name's first half
DEUEL = hits('דעואל', None, True); REUEL = hits('רעואל', None, True); assert DEUEL == ['Num 10:20', 'Num 1:14', 'Num 7:42', 'Num 7:47'] and 'Num 2:14' in REUEL and 'Num 10:29' in REUEL and 'Exod 2:18' in REUEL and len(REUEL) == 10
DEGEL = phrase(['דגל', 'מחנה'], None); assert DEGEL == ['Num 10:14', 'Num 10:18', 'Num 10:22', 'Num 10:25', 'Num 2:10', 'Num 2:18', 'Num 2:25', 'Num 2:3']
assert sum(1 for v in range(14, 28) for x in words('Num', 10, v) if x in ('צבאו', 'צבא')) == 12
assert phrase(['והורד', 'המשכן'], None) == ['Num 10:17'] and phrase(['והקימו', 'את', 'המשכן'], None) == ['Num 10:21'] and hits('המקדש', ('Num',), True) == ['Num 10:21', 'Num 18:1', 'Num 3:38']
assert hits('מאסף', None, True) == ['Ezek 38:12', 'Jer 9:21', 'Judg 19:15', 'Judg 19:18', 'Num 10:25'] and 'והמאסף' in words('Josh', 6, 9) and 'והמאסף' in words('Josh', 6, 13) and phrase(['אלה', 'מסעי'], None) == ['Num 10:28', 'Num 33:1']
CHOVAV = hits('חבב', None, True); assert CHOVAV == ['Deut 33:3', 'Judg 4:11'] and hits('לחבב', None, True) == ['Num 10:29']   # the name at Judg 4:11 and (with 'to') 10:29; the verb 'loves' at Deut 33:3
CHOTEN = phrase(['חתן', 'משה'], None); assert CHOTEN == ['Exod 18:1', 'Exod 18:12', 'Exod 18:14', 'Exod 18:17', 'Exod 18:2', 'Exod 18:5', 'Judg 1:16', 'Judg 4:11', 'Num 10:29'], CHOTEN
assert phrase(['נסעים', 'אנחנו'], None) == ['Num 10:29'] and phrase(['והטבנו', 'לך'], None) == ['Num 10:29', 'Num 10:32'] and phrase(['והיית', 'לנו', 'לעינים'], None) == ['Num 10:31']
HAR_YHWH = sorted({f'{b} {c}:{v}' for (b, c, v), ws in by.items() for i in range(len(ws) - 1) if ws[i][0].endswith('הר') and len(ws[i][0]) <= 3 and ws[i + 1][0] == 'יהוה'})
assert HAR_YHWH == ['Gen 22:14', 'Isa 2:3', 'Isa 30:29', 'Mic 4:2', 'Num 10:33', 'Ps 24:3', 'Zech 8:3'], HAR_YHWH
THREE_DAYS = phrase(['דרך', 'שלשת', 'ימים'], None); assert THREE_DAYS == ['Exod 3:18', 'Exod 5:3', 'Exod 8:23', 'Gen 30:36', 'Num 10:33', 'Num 33:8'] and nphrase(['דרך', 'שלשת', 'ימים'], 'Num', 10, 33) == 2
TUR = hits('לתור', None, True); assert TUR == ['Deut 1:33', 'Num 10:33', 'Num 13:16', 'Num 13:17', 'Num 13:32', 'Num 14:36', 'Num 14:38', 'Num 14:7'] and phrase(['לתור', 'להם', 'מנוחה'], None) == ['Num 10:33'] and phrase(['לתור', 'לכם', 'מקום'], None) == ['Deut 1:33']
ANAN_YHWH = sorted(set(phrase(['ענן', 'יהוה'], None) + phrase(['וענן', 'יהוה'], None))); assert ANAN_YHWH == ['Exod 40:38', 'Num 10:34']
assert phrase(['בנסע', 'הארן'], None) == ['Num 10:35'] and phrase(['רבבות', 'אלפי', 'ישראל'], None) == ['Num 10:36']
KUMAH = phrase(['קומה', 'יהוה'], None); SHUVAH = phrase(['שובה', 'יהוה'], None)
assert KUMAH == ['2Chr 6:41', 'Num 10:35', 'Ps 10:12', 'Ps 132:8', 'Ps 17:13', 'Ps 3:8', 'Ps 7:7', 'Ps 9:20'] and SHUVAH == ['Num 10:36', 'Ps 126:4', 'Ps 6:5', 'Ps 90:13'], (KUMAH, SHUVAH)
assert phrase(['ויפצו', 'איביך'], None) == ['Num 10:35'] and phrase(['יפוצו', 'אויביו'], None) == ['Ps 68:2']
# CHAPTER 11
assert hits('מתאננים', None) == ['Num 11:1'] and phrase(['אש', 'יהוה'], None) == ['1Kgs 18:38', 'Num 11:1', 'Num 11:3'] and phrase(['בקצה', 'המחנה'], None) == ['Judg 7:17', 'Judg 7:19', 'Num 11:1']
assert hits('תבערה', None) == ['Deut 9:22', 'Num 11:3'] and hits('ותשקע', None, True) == ['Num 11:2'] and hits('אספסף', None) == ['Num 11:4']
assert phrase(['התאוו', 'תאוה'], None) == ['Num 11:4'] and phrase(['ויתאוו', 'תאוה'], None) == ['Ps 106:14']
FOODS = {x: count_tok(x) for x in ('הקשאים', 'האבטחים', 'החציר', 'הבצלים', 'השומים')}; assert all(n == 1 for n in FOODS.values()) and count_tok('חציר') == 17, (FOODS, count_tok('חציר'))
assert phrase(['כזרע', 'גד'], None) == ['Exod 16:31', 'Num 11:7'] and hits('בדלח', None) == ['Gen 2:12', 'Num 11:7']
assert hits('שטו', None, True) == ['Num 11:8'] and hits('מדכה', None) == ['Num 11:8'] and hits('לשד', T, True) == ['Num 11:8'] and phrase(['לשד', 'השמן'], None) == ['Num 11:8'] and phrase(['כצפיחת', 'בדבש'], None) == ['Exod 16:31']
assert phrase(['בכה', 'למשפחתיו'], None) == ['Num 11:10'] and sorted(set(phrase(['פתח', 'אהלו'], None) + phrase(['לפתח', 'אהלו'], None))) == ['Exod 33:10', 'Exod 33:8', 'Num 11:10'] and phrase(['ובעיני', 'משה', 'רע'], None) == ['Num 11:10']
HAREOTA = [('Num', 11, 11, 'הרעת'), ('Exod', 5, 22, 'הרעתה'), ('1Kgs', 17, 20, 'הרעות')]; assert all(tok in words(b, c, v) for b, c, v, tok in HAREOTA) and 'למה' in words('Num', 11, 11) and 'למה' in words('Exod', 5, 22) and hits('הרעת', None, True) == ['Num 11:11']   # "why have You dealt ill" — Moses twice, Elijah once, three forms
assert phrase(['לא', 'אוכל', 'אנכי', 'לבדי'], None) == ['Num 11:14'] and phrase(['לא', 'אוכל', 'לבדי'], None) == ['Deut 1:9']
assert hits('האמן', None, True) == ['Num 11:12'] and phrase(['הרגני', 'נא', 'הרג'], None) == ['Num 11:15'] and hits('ברעתי', None, True) == ['Num 11:15'] and hits('ברעתך', None, True) == ['2Sam 16:8', 'Isa 47:10']
SEVENTY = phrase(['שבעים', 'איש'], ('Num',)); assert SEVENTY == ['Num 11:16', 'Num 11:24', 'Num 11:25'] and phrase(['ושבעים', 'מזקני', 'ישראל'], None) == ['Exod 24:1', 'Exod 24:9'] and phrase(['אספה', 'לי'], None) == ['Num 11:16']
DESCENTS = [('Gen', 11, 5, 'וירד'), ('Gen', 11, 7, 'נרדה'), ('Gen', 18, 21, 'ארדה'), ('Exod', 3, 8, 'וארד'), ('Exod', 19, 11, 'ירד'), ('Exod', 19, 18, 'ירד'), ('Exod', 19, 20, 'וירד'), ('Exod', 34, 5, 'וירד'), ('Num', 11, 17, 'וירדתי'), ('Num', 11, 25, 'וירד'), ('Num', 12, 5, 'וירד')]
assert all(tok in words(b, c, v) for b, c, v, tok in DESCENTS) and len(DESCENTS) == 11   # eleven tokens of the LORD going down in the Torah (the ink's list; the Sifrei says ten "written in the Torah" — its list is not on this shelf)
assert hits('ואצלתי', None, True) == ['Num 11:17'] and hits('ויאצל', None, True) == ['Num 11:25'] and hits('אצלת', None, True) == ['Gen 27:36']
assert 'במשא' in words('Num', 11, 17) and phrase(['משא', 'כל', 'העם'], None) == ['Num 11:11'] and hits('ומשאכם', None, True) == ['Deut 1:12']
assert hits('התקדשו', T, True) == ['Num 11:18'] and 'התקדשו' in words('Josh', 3, 5) and 'מחר' in words('Josh', 3, 5) and 'למחר' in words('Num', 11, 18)
assert phrase(['כי', 'טוב', 'לנו', 'במצרים'], None) == ['Num 11:18'] and hits('יומים', T, True) == ['Exod 16:29', 'Exod 21:21', 'Num 11:19']
assert phrase(['חדש', 'ימים'], None) == ['Gen 29:14', 'Num 11:20', 'Num 11:21'] and hits('לזרא', None) == ['Num 11:20'] and phrase(['למה', 'זה', 'יצאנו', 'ממצרים'], None) == ['Num 11:20']
assert phrase(['שש', 'מאות', 'אלף', 'רגלי'], None) == ['Num 11:21'] and phrase(['כשש', 'מאות', 'אלף', 'רגלי'], None) == ['Exod 12:37']
assert phrase(['כל', 'דגי', 'הים'], None) == ['Num 11:22'] and phrase(['היד', 'יהוה', 'תקצר'], None) == ['Num 11:23'] and phrase(['קצרה', 'יד', 'יהוה'], None) == ['Isa 59:1'] and phrase(['קצרה', 'ידי'], None) == ['Isa 50:2']
assert phrase(['סביבת', 'האהל'], None) == ['Num 11:24'] and phrase(['ויתנבאו', 'ולא', 'יספו'], None) == ['Num 11:25']
assert hits('אלדד', None) == ['Num 11:26', 'Num 11:27'] and hits('מידד', None) == ['Num 11:26', 'Num 11:27'] and hits('בכתבים', None) == ['Num 11:26'] and hits('מבחריו', None) == ['Dan 11:15', 'Num 11:28'] and hits('כלאם', None, True) == ['Num 11:28'] and hits('הנער', ('Num',), True) == ['Num 11:27']
assert phrase(['המקנא', 'אתה', 'לי'], None) == ['Num 11:29'] and phrase(['ומי', 'יתן', 'כל', 'עם', 'יהוה', 'נביאים'], None) == ['Num 11:29']
assert hits('ויגז', T, True) == ['Num 11:31'] and sorted(set(hits('שלוים', T, True) + hits('השלו', T, True))) == ['Exod 16:13', 'Num 11:31', 'Num 11:32'] and 'שלו' in words('Ps', 105, 40)
assert phrase(['כדרך', 'יום', 'כה'], None) == ['Num 11:31']
AMATAYIM = sorted(set(hits('וכאמתים', None, True) + hits('אמתים', None, True))); assert AMATAYIM == ['Exod 25:10', 'Exod 25:17', 'Exod 25:23', 'Exod 37:1', 'Exod 37:10', 'Exod 37:6', 'Num 11:31'], AMATAYIM
assert sorted(set(hits('הממעיט', None, True) + hits('והממעיט', None, True))) == ['Exod 16:17', 'Exod 16:18', 'Num 11:32'] and phrase(['עשרה', 'חמרים'], None) == ['Gen 45:23', 'Num 11:32']   # 'ten asses' (Joseph's gift) / 'ten homers' — one consonantal phrase
assert phrase(['וישטחו', 'להם', 'שטוח'], None) == ['Num 11:32'] and hits('שטוח', None, True) == ['Num 11:32'] and hits('וישטחו', None, True) == ['Num 11:32']
assert phrase(['מכה', 'רבה', 'מאד'], None) == ['Num 11:33'] and phrase(['קברות', 'התאוה'], None) == ['Num 11:34']
KIVROT = {k: [plain(x) for x in byraw[k] if 'קבר' in plain(x)] for k in [('Num', 11, 34), ('Num', 11, 35), ('Num', 33, 16), ('Num', 33, 17), ('Deut', 9, 22)]}
assert KIVROT == {('Num', 11, 34): ['קברות', 'קברו'], ('Num', 11, 35): ['מקברות'], ('Num', 33, 16): ['בקברת'], ('Num', 33, 17): ['מקברת'], ('Deut', 9, 22): ['ובקברת']}, KIVROT   # plene in the story, defective in the itinerary and Deuteronomy
CHATZEROT = {k: [plain(x) for x in byraw[k] if 'חצר' in plain(x)] for k in [('Num', 11, 35), ('Num', 12, 16), ('Num', 33, 17), ('Num', 33, 18), ('Deut', 1, 1)]}
assert CHATZEROT == {('Num', 11, 35): ['חצרות', 'בחצרות'], ('Num', 12, 16): ['מחצרות'], ('Num', 33, 17): ['בחצרת'], ('Num', 33, 18): ['מחצרת'], ('Deut', 1, 1): ['וחצרת']}, CHATZEROT
assert words('Num', 33, 16) == ['ויסעו', 'ממדבר', 'סיני', 'ויחנו', 'בקברת', 'התאוה'] and words('Deut', 9, 22)[:4] == ['ובתבערה', 'ובמסה', 'ובקברת', 'התאוה']
# CHAPTER 12
assert by[('Num', 12, 1)][0] == ('ותדבר', 'HC/Vpw3fs') and words('Num', 12, 1)[:3] == ['ותדבר', 'מרים', 'ואהרן'] and words('Num', 12, 5)[7:10] == ['ויקרא', 'אהרן', 'ומרים']
assert hits('הכשית', None) == ['Num 12:1'] and count_tok('הכשית') == 1 and words('Num', 12, 1)[6:8] == ['האשה', 'הכשית'] and words('Num', 12, 1)[11:13] == ['אשה', 'כשית'] and words('Num', 12, 1).count('לקח') == 2
assert words('Num', 12, 2)[:4] == ['ויאמרו', 'הרק', 'אך', 'במשה'] and [s for s in phrase(['וישמע', 'יהוה'], None) if s.startswith('Num 1')] == ['Num 11:1', 'Num 12:2']
assert plain(byraw[('Num', 12, 3)][2]) == 'ענו' and phrase(['מכל', 'האדם', 'אשר', 'על', 'פני', 'האדמה'], None) == ['Num 12:3']
PITOM_T = sorted(set(hits('פתאם', T, True) + hits('בפתע', T, True))); assert PITOM_T == ['Num 12:4', 'Num 35:22', 'Num 6:9'], PITOM_T
assert hits('שלשתכם', None) == ['Num 12:4'] and hits('שלשתם', None, True) == ['Num 12:4'] and phrase(['בעמוד', 'ענן'], None) == ['Deut 31:15', 'Exod 13:21', 'Num 12:5', 'Ps 99:7']
assert hits('נביאכם', None) == ['Num 12:6'] and hits('במראה', T, True) == ['Num 12:6'] and hits('ומראה', T, True) == ['Exod 24:17', 'Lev 13:25', 'Lev 13:3', 'Lev 13:32', 'Num 12:8', 'Num 9:16']
assert hits('בחלום', None, True) == ['1Kgs 3:5', 'Gen 20:3', 'Gen 31:10', 'Gen 31:11', 'Job 33:15', 'Num 12:6']
assert phrase(['בכל', 'ביתי', 'נאמן', 'הוא'], None) == ['Num 12:7'] and phrase(['פה', 'אל', 'פה'], None) == ['Num 12:8'] and hits('בחידת', None) == ['Num 12:8'] and hits('ותמנת', None, True) == ['Num 12:8'] and phrase(['בעבדי', 'במשה'], None) == ['Num 12:8']
CHIDAH = sorted(set(hits('חידה', None, True) + hits('חידות', None, True) + hits('חידת', None, True) + hits('בחידת', None, True) + hits('חידתי', None, True) + hits('החידה', None, True))); assert 'Num 12:8' in CHIDAH and all(not s.startswith(('Gen', 'Exod', 'Lev', 'Deut')) for s in CHIDAH), CHIDAH
TEMUNAH = sorted(set(hits('תמונה', T, True) + hits('תמונת', T, True) + hits('ותמנת', T, True) + hits('ותמונה', T, True) + hits('תמנת', T, True))); assert TEMUNAH == ['Deut 4:12', 'Deut 4:15', 'Deut 4:16', 'Deut 4:23', 'Deut 4:25', 'Deut 5:8', 'Exod 20:4', 'Num 12:8'] and hits('תמונתך', None, True) == ['Ps 17:15'], TEMUNAH   # seven bans on making a likeness, one beholding of it
ANGER = [(c, v) for (c, v) in SPAN if any(x in ('ויחר', 'חרה') for x in words('Num', c, v))]; assert ANGER == [(11, 1), (11, 10), (11, 33), (12, 9)] and 'בם' in words('Num', 12, 9) and 'וילך' in words('Num', 12, 9)
assert phrase(['והענן', 'סר'], None) == ['Num 12:10'] and phrase(['מצרעת', 'כשלג'], None) == ['Exod 4:6', 'Num 12:10'] and phrase(['מצרע', 'כשלג'], None) == ['2Kgs 5:27'] and phrase(['ויפן', 'אהרן'], None) == ['Num 12:10']
BI_ADONI = phrase(['בי', 'אדני'], None); assert len(BI_ADONI) == 11 and 'Num 12:11' in BI_ADONI and 'Exod 4:10' in BI_ADONI and 'Gen 44:18' in BI_ADONI, BI_ADONI
assert hits('נואלנו', None) == ['Num 12:11'] and hits('נואלו', None, True) == ['Isa 19:13', 'Jer 5:4'] and phrase(['כמת'], None) == ['Num 12:12', 'Ps 31:13'] and phrase(['חצי', 'בשרו'], None) == ['Num 12:12']
CRIES = sorted(set(phrase(['ויצעק', 'משה', 'אל', 'יהוה'], None) + phrase(['ויצעק', 'אל', 'יהוה'], ('Exod',)))); assert CRIES == ['Exod 15:25', 'Exod 17:4', 'Exod 8:8', 'Num 12:13'], CRIES
PRAYER = words('Num', 12, 13)[5:]; assert PRAYER == ['אל', 'נא', 'רפא', 'נא', 'לה'] and sum(len(x) for x in PRAYER) == 11 and words('Num', 12, 13)[4] == 'לאמר'
YARAK = sorted(set(hits('ירק', T, True) + hits('וירקה', T, True))); assert YARAK == ['Deut 25:9', 'Exod 10:15', 'Gen 1:30', 'Lev 15:8', 'Num 12:14', 'Num 22:4'], YARAK   # the spit-root at Lev 15:8, Num 12:14, Deut 25:9; the green-root the rest
assert phrase(['ירק', 'ירק'], None) == ['Num 12:14'] and 'בפניה' in words('Num', 12, 14) and 'בפניו' in words('Deut', 25, 9) and phrase(['הלא', 'תכלם'], None) == ['Num 12:14']
SAGAR_T = sorted(set(hits('תסגר', T, True) + hits('ותסגר', T, True) + hits('והסגיר', T, True) + hits('והסגירו', T, True) + hits('הסגירו', T, True)))
assert SAGAR_T == ['Lev 13:21', 'Lev 13:26', 'Lev 13:31', 'Lev 13:33', 'Lev 13:4', 'Lev 13:5', 'Lev 13:50', 'Lev 13:54', 'Lev 14:38', 'Num 12:14', 'Num 12:15'], SAGAR_T   # the quarantine verb: nine leper seats and Miriam's two
assert phrase(['ואחר', 'תאסף'], None) == ['Num 12:14'] and phrase(['עד', 'האסף', 'מרים'], None) == ['Num 12:15'] and words('Num', 12, 16)[0] == 'ואחר'
PARAN = sorted(f'{b} {c}:{v}' for (b, c, v), ws in by.items() for i in range(len(ws) - 1) if ws[i][0].endswith('מדבר') and ws[i + 1][0] == 'פארן'); assert PARAN == ['1Sam 25:1', 'Gen 21:21', 'Num 10:12', 'Num 12:16', 'Num 13:26', 'Num 13:3'], PARAN
# THE TRANSLATION'S OWN WORDS, cut from the shelf's bytes
BUCINA = {f'{c}:{v}': [x for x in aramaic(c, v) if x.startswith('בוצינ')] for (c, v) in [(8, 2), (8, 3), (11, 5)]}
assert BUCINA == {'8:2': ['בוציניא', 'בוציניא'], '8:3': ['בוצינהא'], '11:5': ['בוציניא']}, BUCINA   # one Aramaic word for the lamps (8:2-3) and the cucumbers (11:5)
assert aramaic(11, 25)[-2:] == ['ולא', 'פסקין'] and [x for x in aramaic(12, 1) if x.startswith('שפ') or x == 'רחיק'] == ['שפרתא', 'שפרתא', 'רחיק']
assert 'אחתנא' in aramaic(12, 12) and 'תתרחק' in aramaic(12, 12) and 'מיתא' in aramaic(12, 12) and 'ויתסי' in aramaic(12, 12)
assert 'מנזף' in aramaic(12, 14) and 'נזיף' in aramaic(12, 14) and 'אתגלי' in aramaic(10, 35) and aramaic(10, 36)[2:6] == ['תוב', 'יי', 'שרי', 'ביקרך']
assert aramaic(10, 31)[-5:] == ['וגבורן', 'דאתעבידן', 'לנא', 'חזיתא', 'בעיניך'] and aramaic(8, 16)[1:3] == ['אפרשא', 'מפרשין'] and aramaic(8, 14)[-3:] == ['משמשין', 'קדמי', 'לואי']
assert aramaic(11, 4)[0] == 'וערברבין' and aramaic(11, 23)[3:6] == ['המימרא', 'דיי', 'יתעכב'] and aramaic(10, 33)[1:6] == ['מטורא', 'דאתגלי', 'עלוהי', 'יקרא', 'דיי']
assert aramaic(11, 8).count('דצבי') == 2 and aramaic(10, 5)[1] == 'יבבתא' and 'ותיבבון' in aramaic(10, 9) and 'לטבא' in aramaic(10, 9)
assert aramaic(11, 34)[5:7] == ['קברי', 'דמשאלי'] and aramaic(11, 3)[4] == 'דלקתא' and 'דאזער' in aramaic(11, 32) and 'דגורין' in aramaic(11, 32)
assert aramaic(11, 31)[-6:-3] == ['וכרום', 'תרתין', 'אמין'] and aramaic(10, 2)[2:4] == ['תרתין', 'חצוצרן'] and aramaic(8, 4)[3] == 'נגידא' and 'מספר' in aramaic(8, 7) and 'דחטאתא' in aramaic(8, 7)
assert 'ארמא' in aramaic(8, 11) and aramaic(11, 28)[-1] == 'אסרנון' and aramaic(12, 8)[:3] == ['ממלל', 'עם', 'ממלל'] and 'בחדון' in aramaic(12, 8) and 'יקרא' in aramaic(12, 8)
assert 'חורא' in aramaic(12, 10) and 'סגירת' in aramaic(12, 10) and aramaic(10, 14)[1] == 'טקס' and aramaic(11, 17)[0] == 'ואתגלי' and 'דשכנתיה' in aramaic(11, 20) and 'מימרא' in aramaic(11, 20)
assert aramaic(12, 3)[2] == 'ענותן' and 'מתגלי' in aramaic(12, 6) and 'בחלמין' in aramaic(12, 6) and aramaic(11, 12)[:2] == ['האב', 'אנא'] and 'תוב' in aramaic(10, 36)

if __name__ == '__main__':
    print(f'beha_ink: {len(SPAN)} verses, {sum(SIF_ROWS.values())} Sifrei rows in {len(PISKAOT)} piskaot, frames {len(FR)}, register verses {len(REG)}; the parser right at {len(RIGHT)}, gaps {list(GAPS)}; FAIL {FAIL}')

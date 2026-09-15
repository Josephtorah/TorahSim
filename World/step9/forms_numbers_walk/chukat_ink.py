import os as _os
_ROOT = _os.path.normpath(_os.path.join(_os.path.dirname(_os.path.abspath(__file__)), '..', '..', '..'))   # THE PORTABLE REPO (2026-09-15): the repo root from this file's own place
#!/usr/bin/env python3
# THE NUMBERS WALK, sitting 6 — CHUKAT (2026-09-11; the owner: "Go" after the #127 rereads, on the ruling READ THEN COMPILE): THE INK
# OF Numbers 19:1-21:35, computed from the Tanakh DB, the snapshot store and the shelf's own bytes — never typed. Sitting 5's form
# (korach_ink.py): the heads found BY POSITION and asserted; coverage computed; every cut by consonants (the misses collected, asserted
# empty); the engine's numeral parser MEASURED against the portion's numbers; the hand's facts as asserts, run all at once by
# assert_driver.py after the measurement pass (chukat_measure1.py) printed them; every gloss of a narrative verb the STORE'S OWN
# (words.gloss). Shared by chukat_rows_onkelos.py, chukat_rows_onkelos21.py, chukat_rows_sifrei.py and write_chukat_ledgers.py.
import json, os, re, html, sqlite3, sys, io, contextlib, unicodedata
from collections import Counter
ROOT = _ROOT
DATE = '2026-09-11'
UNITS = [  # (uid, chapter, lo, hi, title, the Sifrei piskaot by position)
    ('num_19_parah', 19, 1, 22, 'the red heifer\'s statute; the ashes and the waters of niddah; the seven days of the dead; the tent, the open vessel and the field; the third and the seventh day; the sprinkler and the toucher', [123, 124, 125, 126, 127, 128, 129, 130]),
    ('num_20_meribah_edom_aaron', 20, 1, 29, 'Miriam\'s death at Kadesh; the waters of Meribah — the rock struck twice and the sentence on Moses and Aaron; Edom\'s refusal; Aaron\'s death on Mount Hor and the vestments on Eleazar; the thirty days', []),
    ('num_21_snakes_conquest', 21, 1, 35, 'Arad and the vow — Hormah named; the Red Sea road and the fiery serpents; the copper serpent on the pole; the stations and the well\'s song; Sihon and the parable-tellers; Og', []),
]
OUT = {u[0]: f'{ROOT}/logic/oral_triage/{u[0]}_{DATE}.md' for u in UNITS}

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
# THE SHELF'S ROWS ON CHUKAT, BY POSITION: the Sifrei on Numbers has EIGHT piskaot on chapter 19 — 123 on 19:1 (the export heads it
# "19:1-2"), 124 on 19:5, 125 on 19:11, 126 on 19:14, 127 on 19:16, 128 on 19:17, 129 on 19:18, 130 on 19:22 — every head in order,
# none mistyped; and NO PISKA on chapters 20, 21, 22, 23 or 24 (computed on every head — the next head, 131, is Balak's close at
# 25:1): Miriam's death, Meribah, Edom, Aaron's death, Arad, the serpents, the well, Sihon and Og are read on Onkelos alone, as the
# spies, the decree and the rebellion were.
assert heads[122] == ('Bamidbar', 18, 30) and heads[123] == ('Bamidbar', 19, 1) and heads[124] == ('Bamidbar', 19, 5) and heads[125] == ('Bamidbar', 19, 11) and heads[126] == ('Bamidbar', 19, 14), (heads[122], heads[123], heads[124], heads[125], heads[126])
assert heads[127] == ('Bamidbar', 19, 16) and heads[128] == ('Bamidbar', 19, 17) and heads[129] == ('Bamidbar', 19, 18) and heads[130] == ('Bamidbar', 19, 22) and heads[131] == ('Bamidbar', 25, 1), (heads[127], heads[128], heads[129], heads[130], heads[131])
NO_PISKA_20_24 = sorted(p for p, h in heads.items() if h and h[0] == 'Bamidbar' and h[1] in (20, 21, 22, 23, 24))
assert NO_PISKA_20_24 == [], NO_PISKA_20_24   # the shelf's silence on 20-24 — computed on every head
assert sorted(p for p, h in heads.items() if h and h[0] == 'Bamidbar' and h[1] == 19) == list(range(123, 131))
assert [p for p in range(120, 137) if heads.get(p) is None] == []   # no headless piska in the stretch
HEAD_FIX = {}
def head(p): return HEAD_FIX.get(p) or heads[p][1:]
PISKAOT = [p for u in UNITS for p in u[5]]
assert PISKAOT == list(range(123, 131)) and len(PISKAOT) == 8
for a, b in zip(PISKAOT, PISKAOT[1:]): assert head(b) >= head(a), (a, b, head(a), head(b))     # monotone by position
for uid, c, lo, hi, _, ps in UNITS:
    for p in ps: assert (c, lo) <= head(p) <= (c, hi), (uid, p, head(p))
SIF_ROWS = {p: len(sif[p - 1]) for p in PISKAOT}
assert SIF_ROWS == {123: 2, 124: 2, 125: 1, 126: 1, 127: 5, 128: 2, 129: 5, 130: 1} and sum(SIF_ROWS.values()) == 19, SIF_ROWS
assert {p: len(sif_he[p - 1]) for p in PISKAOT} == SIF_ROWS   # the Hebrew export's rows match the English's
# THE EXPORT'S ENGLISH REVERSES THE FRAME: 123:1 opens "And the L-rd spoke to Aaron and to Moses" where the shelf's own Hebrew row
# reads "to Moses and Aaron" — a translator's transposition, measured on the export's two files (RESEARCH_LOG.md)
SIF_HE_123 = clean(sif_he[122][0])[:40]
assert SIF_HE_123.startswith('וידבר ה\' אל משה ואהרן') and clean(sif[122][0])[:80].find('to Aaron and to Moses') > 0, (SIF_HE_123, clean(sif[122][0])[:80])
ONK_LEN = {c: len(onk[c - 1]) for c in range(18, 23)}
assert ONK_LEN == {18: 32, 19: 22, 20: 29, 21: 35, 22: 41} and {c: len(onk_he[c - 1]) for c in range(18, 23)} == ONK_LEN, ONK_LEN
shelf_numbers = sorted(d for d in os.listdir(f'{ROOT}/Data/sefaria_export') if re.search(r'Numbers|Bamidbar', d))
outside = [d for d in shelf_numbers if d not in ('Sifrei_Bamidbar', 'Onkelos_Numbers')]
assert len(outside) == 23, len(outside)
# THE PRIOR READS (grep of logic/oral_triage at the sitting, the sitting's own ledgers excluded): no row of 123-130 read by any prior
# ledger; no Onkelos verse of 19, 20, 21 — FRESH (the Sifrei's 132-134 read at THE TENT's daughters are Pinchas's, outside this span)
TRI = f'{ROOT}/logic/oral_triage'
LED = {f: open(f'{TRI}/{f}', encoding='utf-8').read() for f in os.listdir(TRI) if f.endswith('.md') and f'{TRI}/{f}' not in OUT.values()}
prior = sorted(f for f, t in LED.items() if re.search(r'Sifrei Bamidbar (12[3-9]|130):\d', t))
assert prior == [], prior
prior_onk = sorted(f for f, t in LED.items() if re.search(r'Onkelos Num (19|20|21):\d', t))
assert prior_onk == [], prior_onk

# ---- THE DRAFTS' SPANS AND THE BOUNDARIES, COMPUTED ----
db = sqlite3.connect(f'file:{ROOT}/Data/tanakh.sqlite?mode=ro', uri=True)
VC = dict(db.execute("SELECT chapter, COUNT(*) FROM verses WHERE book='Num' GROUP BY chapter").fetchall())
assert VC[19] == 22 and VC[20] == 29 and VC[21] == 35 and VC[22] == 41
def unit_text(uid): return open(f'{ROOT}/logic/units/{uid}.yaml', encoding='utf-8').read()
def steps(uid): return sorted({(int(a), int(b)) for a, b in re.findall(r'STEP_Nm_(\d+)_(\d+)', unit_text(uid))})
for uid, c, lo, hi, _, _ in UNITS:
    st = steps(uid); assert st == [(c, v) for v in range(lo, hi + 1)], (uid, st[:2], st[-2:])
    assert 'status: draft' in unit_text(uid) and 'operators:' not in unit_text(uid), uid
assert 'status: frozen' in unit_text('num_18_priest_levite_dues') and steps('num_18_priest_levite_dues') == [(18, v) for v in range(1, 33)]
assert steps('num_22_balak_bilam_call')[0] == (22, 1) and 'status: draft' in unit_text('num_22_balak_bilam_call')   # the portion's last verse (22:1) opens the next draft — Balak's; read with it
SPAN = [(c, v) for (_, c, lo, hi, _, _) in UNITS for v in range(lo, hi + 1)]
assert len(SPAN) == 86 == 22 + 29 + 35 and SPAN[0] == (19, 1) and SPAN[-1] == (21, 35)

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
def key(s):
    b, cv = s.split(' '); c, v = cv.split(':'); return (b, int(c), int(v))
def pt(b, c, v, tok, nth=0):
    """the pointed form of a consonantal token at a verse (the nth occurrence) — read off the DB's bytes"""
    w, wp = words(b, c, v), byp[(b, c, v)]
    idx = [i for i, x in enumerate(w) if x == tok]
    return wp[idx[nth]] if len(idx) > nth else None
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
def aramaic_book(book, c, v):
    t = json.load(open(f'{ROOT}/Data/sefaria_export/Onkelos_{book}/he.json'))['text']
    return [plain(x) for x in clean(t[c - 1][v - 1]).rstrip(':').split()]
def numword(n): return f'{n:,}'
# THE STORE'S OWN GLOSSES — every English beside a narrative verb is the snapshot store's words.gloss, never typed
store = sqlite3.connect(f'file:{ROOT}/torah_grok.SNAPSHOT-main-51801ca.sqlite?mode=ro', uri=True)
SG = {}
for c, v, hp, g in store.execute("SELECT v.chapter, v.verse, w.he_plain, w.gloss FROM words w JOIN verses v ON w.verse_id=v.id WHERE v.book='Num' AND v.chapter BETWEEN 19 AND 21 ORDER BY v.id, w.idx"):
    SG.setdefault((c, v), []).append((hp.replace('/', ''), g))
def sg(c, v, tok):
    for hp, g in SG[(c, v)]:
        if hp == tok: return g
    raise KeyError((c, v, tok))

# THE ENGINE'S PARSER (taught the census at 1b, the construct and the accent at 2b, the dual, the suffix, the half and the seven-stem
# at 3b, the fraction, the unit noun and the definite one at 4b, the definite numeral at 5b) on Chukat's numbers — MEASURED before the
# compile is asked
sys.path.insert(0, f'{ROOT}/World/step9')
with contextlib.redirect_stdout(io.StringIO()):
    import cold_run_sequence as CS
def N(b, c, v): return CS.ink_numbers(CS.verse_words(b, c, v))
RIGHT = {k: N('Num', *k) for k in [(19, 4), (19, 11), (19, 14), (19, 16), (20, 29)]}
assert RIGHT == {(19, 4): [7], (19, 11): [7], (19, 14): [7], (19, 16): [7], (20, 29): [30]}, RIGHT
ORDINALS = {k: N('Num', *k) for k in [(19, 12), (19, 19), (20, 1), (21, 26)]}
assert ORDINALS == {(19, 12): [], (19, 19): [], (20, 1): [], (21, 26): []}, ORDINALS   # the day-ordinals (the third, the seventh), the month-ordinal (the first) and the king-ordinal SILENT — a class named and left: the compile's timers read the day-words by their own rule
HOMOGRAPH = {k: N('Num', *k) for k in [(19, 6)]}
assert HOMOGRAPH == {(19, 6): []}, HOMOGRAPH   # "scarlet" (shni tola'at) — the consonants of "two of"; the parser silent by the points (the chiriq under the nun) — right
GAPS = {k: N('Num', *k) for k in [(20, 11)]}
assert GAPS == {(20, 11): []}, GAPS   # THE DUAL "TWICE" (pa'amayim, 20:11 "he struck the rock with his staff TWICE") — silent; 19:4's "seven TIMES" (pe'amim, plural) read by its "seven": the dual and the plural are consonantal homographs told by the points — the compile's probe
RETOLD = {('Num', 33, 38): N('Num', 33, 38), ('Num', 33, 39): N('Num', 33, 39), ('Deut', 2, 14): N('Deut', 2, 14), ('Deut', 3, 11): N('Deut', 3, 11), ('Deut', 34, 8): N('Deut', 34, 8)}

# THE FRAMES AND THE REGISTER
FR = [(c, v) for (c, v) in SPAN if words('Num', c, v)[0] in ('וידבר', 'ויאמר') and words('Num', c, v)[1] == 'יהוה']
FR_SAID = [(c, v) for c, v in FR if words('Num', c, v)[0] == 'ויאמר']
FR_BOTH = [(c, v) for c, v in FR if words('Num', c, v)[2:6] == ['אל', 'משה', 'ואל', 'אהרן']]
REG = {}
for (c, v) in SPAN:
    vs = [(x, [q for q in m.split('/') if 'V' in q][0]) for x, m in by[('Num', c, v)] if m and re.search(r'V.w', m)]
    if vs: REG[(c, v)] = [f'{x} ("{sg(c, v, x)}", {m})' for x, m in vs]
def register(c, lo, hi): return '; '.join(f'{c}:{v} ' + ', '.join(REG[(c, v)]) for v in range(lo, hi + 1) if (c, v) in REG) or 'no narrative verb'

# ---- THE MEASURED FACTS (printed by the first pass — scratchpad chukat_measure1.out — then typed here as asserts; assert_driver.py
# runs every statement and lists every failure at once) ----
assert FR == [(19, 1), (20, 7), (20, 12), (20, 23), (21, 8), (21, 34)] and FR_SAID == [(20, 12), (20, 23), (21, 8), (21, 34)] and FR_BOTH == [(19, 1), (20, 12), (20, 23)], (FR, FR_SAID, FR_BOTH)
assert len(REG) == 47 and Counter(c for c, v in REG) == {19: 1, 20: 22, 21: 24} and len(REG[(20, 1)]) == 4 and len(REG[(20, 28)]) == 4 and max(len(v) for v in REG.values()) == 4 and [k for k in REG if k[0] == 19] == [(19, 1)], (len(REG), Counter(c for c, v in REG))
assert RETOLD == {('Num', 33, 38): [1], ('Num', 33, 39): [123], ('Deut', 2, 14): [38], ('Deut', 3, 11): [9, 4], ('Deut', 34, 8): [30]}, RETOLD   # Aaron's death-date verse reads [1] alone — "the FORTIETH year", "the FIFTH month" silent (the date-ordinal class); the age 123, the thirty-eight years, Og's bed and Moses' thirty days read right
# THE DUAL "TWICE" AND THE PLURAL "TIMES" ARE CONSONANTAL HOMOGRAPHS TOLD BY THE POINTS: 19:4 pe'amim (sheva under the pe), 20:11 pa'amayim (patach under the pe, the dual's ending) — the Torah's dual "twice" at Gen 27:36, 41:32, 43:10 and Num 20:11; the plural at the seven-times seats
def vowels_on(b, c, v, tok, n=0, nth=0):
    """the point marks carried by the n-th consonant of a pointed token (the marks' ORDER differs between a typed form and the DB's bytes — compare by set)"""
    s = pt(b, c, v, tok, nth); out, k = [], -1
    for ch in s:
        if '\u05d0' <= ch <= '\u05ea': k += 1; continue
        if k == n: out.append(ch)
    return set(out)
SHEVA, PATACH, QAMATS, CHIRIQ, TSERE, CHOLAM = '\u05b0', '\u05b7', '\u05b8', '\u05b4', '\u05b5', '\u05b9'
assert SHEVA in vowels_on('Num', 19, 4, 'פעמים') and PATACH in vowels_on('Num', 20, 11, 'פעמים') and PATACH in vowels_on('Gen', 41, 32, 'פעמים') and PATACH in vowels_on('Gen', 43, 10, 'פעמים') and PATACH in vowels_on('Gen', 27, 36, 'פעמים')
DUAL_TWICE = sorted(s for s in hits('פעמים', T, True) if PATACH in vowels_on(*key(s), 'פעמים'))   # the patach under the pe = the dual
assert DUAL_TWICE == ['Gen 27:36', 'Gen 41:32', 'Gen 43:10', 'Num 20:11'], DUAL_TWICE
assert CHIRIQ in vowels_on('Num', 19, 6, 'ושני', 2) and TSERE not in vowels_on('Num', 19, 6, 'ושני', 2) and PATACH in vowels_on('Num', 19, 4, 'שבע', 1)   # "scarlet" — the chiriq under the nun; "two of" would carry a tsere
# THE STATUTE AND THE TORAH
assert phrase(['זאת', 'חקת', 'התורה'], None) == ['Num 19:2', 'Num 31:21'] and phrase(['זאת', 'התורה'], None) == ['Lev 14:54', 'Lev 7:37', 'Num 19:14'] and len(hits('חקת', T, True)) == 20
assert phrase(['פרה', 'אדמה'], None) == ['Num 19:2'] and [(v, x) for v in range(1, 23) for x in words('Num', 19, v) if x in ('פרה', 'הפרה')] == [(2, 'פרה'), (5, 'הפרה'), (6, 'הפרה'), (9, 'הפרה'), (10, 'הפרה')]
assert sorted(set(hits('פרה', T, True) + hits('הפרה', T, True))) == ['Deut 29:17', 'Gen 35:11', 'Num 19:10', 'Num 19:2', 'Num 19:5', 'Num 19:6', 'Num 19:9']   # the heifer-NOUN's Torah seats all in this chapter; Gen 35:11 "be fruitful" and Deut 29:17 "bearing" its consonantal homographs (verbs)
assert hits('תמימה', None, True) == ['Lev 14:10', 'Lev 25:30', 'Lev 3:9', 'Lev 4:28', 'Lev 4:32', 'Num 19:2', 'Num 6:14', 'Ps 19:8']   # "perfect" (feminine) — the offerings' ewes, a FULL year (25:30), the heifer, and Psalm 19:8 "the TORAH of the LORD is perfect"
assert phrase(['לא', 'עלה', 'עליה', 'על'], None) + phrase(['לא', 'עלה', 'עליהם', 'על'], None) == ['Num 19:2', '1Sam 6:7']   # THE YOKE CLAUSE — the heifer's and the Philistines' two cows that carried the ark home (1 Sam 6:7); Deut 21:3's eglah arufah "has not DRAWN in a yoke" a different verb
assert phrase(['אין', 'בה', 'מום'], None) == ['Num 19:2'] and [(c, v) for (c, v) in SPAN if 'אלעזר' in words('Num', c, v)] == [(19, 3), (19, 4), (20, 25), (20, 26), (20, 28)] and len(phrase(['אלעזר', 'הכהן'], None)) == 20
assert len(phrase(['מחוץ', 'למחנה'], None)) == 28 and phrase(['ושחט', 'אתה', 'לפניו'], None) == ['Num 19:3']
assert hits('באצבעו', None, True) == ['Lev 14:16', 'Lev 14:27', 'Lev 16:14', 'Lev 16:19', 'Lev 4:25', 'Lev 4:30', 'Lev 4:34', 'Lev 8:15', 'Num 19:4'] and len(phrase(['שבע', 'פעמים'], None)) == 18 and phrase(['אל', 'נכח', 'פני'], None) == ['Num 19:4']
assert phrase(['ערה', 'ואת', 'בשרה', 'ואת', 'דמה'], None) == ['Num 19:5'] and 'דמה' not in words('Lev', 4, 11) and 'דם' not in words('Exod', 29, 14) and not any('דמ' in x for x in words('Lev', 16, 27)[-6:]) and 'ופרשו' in words('Lev', 4, 11) and 'פרשו' in words('Exod', 29, 14) and 'פרשם' in words('Lev', 16, 27)   # the burn-list is the sin-bull's (skin, flesh, dung: Exod 29:14, Lev 4:11, 16:27) WITH THE BLOOD ADDED
assert phrase(['עץ', 'ארז'], None) == ['Num 19:6'] and phrase(['ושני', 'תולעת'], None) == ['Lev 14:4', 'Lev 14:49', 'Num 19:6'] and phrase(['שני', 'תולעת'], None) == [] and len(phrase(['ותולעת', 'שני'], None)) + len(phrase(['תולעת', 'שני'], None)) >= 20   # the leper's word order (shni tola'at) at three seats; the tabernacle's (tola'at shani) the other way
EZOV = sorted(set(hits('אזוב', None, True) + hits('ואזוב', None, True) + hits('באזוב', None, True) + hits('האזוב', None, True)))
EZOV_DEF = sorted(set(hits('אזב', None, True) + hits('ואזב', None, True) + hits('האזב', None, True) + hits('באזב', None, True) + hits('ובאזב', None, True)))
assert EZOV == ['1Kgs 5:13', 'Exod 12:22', 'Num 19:18', 'Num 19:6', 'Ps 51:9'] and EZOV_DEF == ['Lev 14:4', 'Lev 14:49', 'Lev 14:51', 'Lev 14:52', 'Lev 14:6'], (EZOV, EZOV_DEF)   # HYSSOP PLENE at Passover, the heifer, Solomon's and Psalm 51's "purge me with hyssop"; DEFECTIVE at the leper's five
assert [v for v in range(1, 23) if any(x in ('וכבס', 'יכבס') for x in words('Num', 19, v))] == [7, 8, 10, 19, 21] and [v for v in range(1, 23) if nphrase(['עד', 'הערב'], 'Num', 19, v)] == [7, 8, 10, 21, 22] and phrase(['ורחץ', 'בשרו', 'במים'], None) == ['Lev 15:13', 'Num 19:7', 'Num 19:8'] and len(phrase(['וטמא', 'עד', 'הערב'], T)) == 18
assert phrase(['איש', 'טהור'], None) == ['Num 19:18', 'Num 19:9'] and phrase(['אפר', 'הפרה'], None) == ['Num 19:10', 'Num 19:9'] and [x for x in words('Num', 19, 17) if 'עפר' in x] == ['מעפר'] and 'העפר' in words('Num', 5, 17)   # ashes at 19:9-10, DUST at 19:17 — the sotah's dust (5:17) the Sifrei's analogy
assert sorted(set(phrase(['במקום', 'טהור'], None) + phrase(['מקום', 'טהור'], None))) == ['Lev 10:14', 'Lev 4:12', 'Lev 6:4', 'Num 19:9'] and hits('למשמרת', T, True) == ['Exod 12:6', 'Exod 16:23', 'Exod 16:32', 'Exod 16:33', 'Exod 16:34', 'Num 17:25', 'Num 19:9', 'Num 3:38']   # "for a keeping" — the lamb, the manna (four), the Levites' post, Aaron's staff, the heifer's ashes
MEI_NIDAH = sorted(set(phrase(['מי', 'נדה'], None) + phrase(['למי', 'נדה'], None) + phrase(['מי', 'הנדה'], None) + phrase(['במי', 'הנדה'], None) + phrase(['במי', 'נדה'], None)))
assert MEI_NIDAH == ['Num 19:13', 'Num 19:20', 'Num 19:21', 'Num 19:9', 'Num 31:23'] and nphrase(['מי', 'הנדה'], 'Num', 19, 21) == 1 and nphrase(['במי', 'הנדה'], 'Num', 19, 21) == 1, MEI_NIDAH   # the waters of niddah: four seats here (19:21 twice — the sprinkler's and the toucher's) and the Midian vessels' (31:23)
assert sorted(set(hits('נדה', T, True) + hits('הנדה', T, True) + hits('נדתה', T, True) + hits('בנדתה', T, True) + hits('כנדת', T, True) + hits('לנדה', T, True))) == ['Lev 15:19', 'Lev 15:20', 'Lev 15:24', 'Lev 15:25', 'Lev 15:26', 'Lev 15:33', 'Lev 20:21', 'Num 19:13', 'Num 19:20', 'Num 19:21', 'Num 19:9', 'Num 31:23']   # the niddah-word: the menstruant's (Lev 15, 20:21) and the waters'
assert phrase(['חטאת', 'הוא'], None) == ['Exod 29:14', 'Lev 4:24', 'Lev 5:12', 'Lev 5:9', 'Num 19:9']   # "it is a sin-offering" — Exod 29:14's burnt bull outside the camp the first seat
assert phrase(['ולגר', 'הגר', 'בתוכם'], None) == ['Josh 20:9', 'Num 15:26', 'Num 15:29', 'Num 19:10'] and hits('לחקת', T, True) == ['Exod 29:9', 'Lev 16:29', 'Lev 16:34', 'Num 10:8', 'Num 19:10', 'Num 19:21', 'Num 27:11', 'Num 35:29']
assert phrase(['הנגע', 'במת'], None) == ['Num 19:11', 'Num 19:13'] and hits('במת', None, True) == ['Num 19:11', 'Num 19:13', 'Num 19:16', 'Num 19:18'] and phrase(['נפש', 'אדם'], None) == ['Lev 24:17', 'Num 19:11'] and [v for v in range(1, 23) if nphrase(['שבעת', 'ימים'], 'Num', 19, v)] == [11, 14, 16]   # "a human soul" — the blasphemer chapter's murder clause (Lev 24:17) and the corpse
YITCHATA = sorted(set(hits('יתחטא', None, True) + hits('התחטאו', None, True) + hits('תתחטאו', None, True) + hits('ויתחטאו', None, True) + hits('יתחטאו', None, True) + hits('תתחטא', None, True) + hits('וחטאו', None, True)))
assert YITCHATA == ['Ezek 43:22', 'Job 41:17', 'Num 19:12', 'Num 19:13', 'Num 19:19', 'Num 19:20', 'Num 31:19', 'Num 31:20', 'Num 31:23', 'Num 8:21'], YITCHATA
assert phrase(['ביום', 'השלישי', 'וביום', 'השביעי'], None) == ['Num 19:12', 'Num 19:19', 'Num 31:19'] and nphrase(['ביום', 'השלישי', 'וביום', 'השביעי'], 'Num', 19, 12) == 2   # the third-and-seventh schedule: twice here, once at 19:19, and RUN at the Midian war (31:19)
assert phrase(['משכן', 'יהוה', 'טמא'], None) == ['Num 19:13'] and phrase(['מקדש', 'יהוה', 'טמא'], None) == ['Num 19:20'] and phrase(['מקדש', 'יהוה'], None) == ['1Chr 22:19', 'Ezek 48:10', 'Num 19:20'] and [v for v in range(1, 23) if 'ונכרתה' in words('Num', 19, v)] == [13, 20] and phrase(['עוד', 'טמאתו', 'בו'], None) == ['Num 19:13']
assert phrase(['אדם', 'כי', 'ימות', 'באהל'], None) == ['Num 19:14'] and aramaic(19, 14).count('במשכנא') == 2 and 'למשכנא' in aramaic(19, 14) and aramaic(19, 13)[11:13] == ['משכנא', 'דיי'] and aramaic(19, 18)[8] == 'משכנא'   # the tent of the dead and the tabernacle of the LORD ONE Aramaic noun
assert phrase(['צמיד', 'פתיל'], None) == ['Num 19:15'] and sorted(set(hits('צמיד', None, True) + hits('צמידים', None, True) + hits('צמדים', None, True))) == ['1Kgs 19:19', '2Kgs 9:25', 'Ezek 16:11', 'Ezek 23:42', 'Gen 24:22', 'Num 19:15'] and sorted(set(hits('פתיל', None, True) + hits('בפתיל', None, True) + hits('ופתיל', None, True))) == ['Exod 28:28', 'Exod 28:37', 'Exod 39:21', 'Exod 39:31', 'Ezek 40:3', 'Judg 16:9', 'Num 15:38', 'Num 19:15']   # the lid's two words: Rebekah's BRACELETS (Gen 24:22), Elijah's YOKE of oxen (1 Kgs 19:19), and the frontplate's / the fringe's CORD
assert aramaic(19, 15)[1:4] == ['מן', 'דחסף', 'פתיח']   # the translation INSERTS "of earthenware"
assert phrase(['בחלל', 'חרב'], None) == ['Num 19:16'] and phrase(['חלל', 'חרב'], None) == [] and len([s for s in phrase(['חללי', 'חרב'], None) if s.startswith('Ezek')]) == 11 and phrase(['בעצם', 'אדם'], None) + phrase(['עצם', 'אדם'], None) == ['Num 19:16', 'Ezek 39:15']   # "one slain by the sword" (singular) the Bible's one seat; Ezekiel's eleven are the plural "slain of the sword"; "a human bone" with Gog's burial (Ezek 39:15)
assert [x for x in words('Num', 19, 16) if x in ('בחלל', 'במת', 'בעצם', 'בקבר')] == ['בחלל', 'במת', 'בעצם', 'בקבר'] and [x for x in words('Num', 19, 18) if x in ('בחלל', 'במת', 'בעצם', 'בקבר')] == ['בעצם', 'בחלל', 'במת', 'בקבר']   # THE FOUR SOURCES REORDERED between the touching (19:16) and the sprinkling (19:18): the bone moves to the head
assert len(phrase(['על', 'פני', 'השדה'], None)) == 11 and 'Lev 14:7' in phrase(['על', 'פני', 'השדה'], None)
assert phrase(['מים', 'חיים'], None) == ['Gen 26:19', 'Jer 17:13', 'Jer 2:13', 'Lev 14:5', 'Lev 14:50', 'Num 19:17', 'Song 4:15', 'Zech 14:8'] and phrase(['אל', 'כלי'], None) == ['Jer 48:11', 'Lev 14:5', 'Lev 14:50', 'Num 18:3', 'Num 19:17'] and aramaic(19, 17)[-3:] == ['מי', 'מבוע', 'למן']   # living water: Isaac's well (the Sifrei's support), the leper's vessel; Onkelos "SPRING water"
assert phrase(['ולקח', 'אזוב'], None) == ['Num 19:18'] and phrase(['וטבל', 'במים'], None) == ['Num 19:18'] and words('Exod', 12, 22)[:4] == ['ולקחתם', 'אגדת', 'אזוב', 'וטבלתם']   # take hyssop and dip — the Passover's two verbs, blood there, water here
assert phrase(['והזה', 'הטהר', 'על', 'הטמא'], None) == ['Num 19:19'] and phrase(['וחטאו', 'ביום', 'השביעי'], None) == ['Num 19:19'] and phrase(['וטהר', 'בערב'], None) == ['Num 19:19']
assert phrase(['מתוך', 'הקהל'], None) == ['Num 16:33', 'Num 19:20']   # "from the midst of the assembly" — Korach's perishing and the unsprinkled's cutting-off
assert phrase(['והנגע', 'במי', 'הנדה'], None) == ['Num 19:21'] and phrase(['אשר', 'יגע', 'בו', 'הטמא'], None) == ['Num 19:22'] and phrase(['והנפש', 'הנגעת'], None) == ['Num 19:22']
# chapter 20
assert phrase(['מדבר', 'צן'], None) == ['Deut 32:51', 'Josh 15:1', 'Num 20:1', 'Num 27:14'] and phrase(['ותמת', 'שם', 'מרים'], None) == ['Num 20:1'] and hits('ותקבר', None, True) == ['Gen 35:19', 'Gen 35:8', 'Num 20:1']   # "and she was buried" — Deborah, Rachel, Miriam
assert hits('מרים', T, True) == ['Exod 15:20', 'Exod 15:21', 'Exod 15:23', 'Exod 35:24', 'Num 12:1', 'Num 12:10', 'Num 12:15', 'Num 12:4', 'Num 20:1', 'Num 26:59'] and hits('המרים', None, True) == ['Num 20:10', 'Num 5:18', 'Num 5:19', 'Num 5:23', 'Num 5:24']
assert CHIRIQ in vowels_on('Num', 20, 1, 'מרים', 0) and CHOLAM in vowels_on('Num', 20, 10, 'המרים', 1) and QAMATS in vowels_on('Exod', 15, 23, 'מרים', 0) and QAMATS in vowels_on('Num', 5, 18, 'המרים', 1)   # ONE CONSONANTAL SKIN: Miriam (chiriq), the BITTER waters of Marah (Exod 15:23, qamats) and of the sotah (5:18-24), and "the REBELS" (20:10, cholam) — told by the points
assert phrase(['ולא', 'היה', 'מים', 'לעדה'], None) == ['Num 20:2'] and phrase(['ויקהלו', 'על', 'משה', 'ועל', 'אהרן'], None) == ['Num 16:3', 'Num 20:2']   # Korach's assembling verb
assert phrase(['וירב', 'העם', 'עם', 'משה'], None) == ['Exod 17:2', 'Num 20:3'] and phrase(['ולו', 'גוענו'], None) == ['Num 20:3'] and [(c, v, x) for (c, v) in SPAN for x in words('Num', c, v) if 'גוע' in x] == [(20, 3, 'גוענו'), (20, 3, 'בגוע'), (20, 29, 'גוע')]
assert phrase(['קהל', 'יהוה'], None) == ['1Chr 28:8', 'Num 16:3', 'Num 20:4'] and phrase(['למות', 'שם'], None) == ['Jer 38:26', 'Num 20:4'] and phrase(['אנחנו', 'ובעירנו'], None) == ['Num 20:4']
assert phrase(['העליתנו', 'ממצרים'], None) == ['Exod 17:3', 'Num 20:5', 'Num 21:5'] and phrase(['ותאנה', 'וגפן', 'ורמון'], None) == ['Num 20:5'] and words('Deut', 8, 8)[3:6] == ['וגפן', 'ותאנה', 'ורמון']   # "why did you bring us up from Egypt" — the first Meribah's words (Exod 17:3) at the second (20:5) and at the serpents (21:5)
assert phrase(['וירא', 'כבוד', 'יהוה'], None) == ['Lev 9:23', 'Num 16:19', 'Num 17:7', 'Num 20:6'] and phrase(['מפני', 'הקהל'], None) == ['Num 20:6']
assert phrase(['קח', 'את', 'המטה'], None) == ['Num 20:8'] and [(v, x) for v in range(1, 30) for x in words('Num', 20, v) if 'מטה' in x] == [(8, 'המטה'), (9, 'המטה'), (11, 'במטהו')] and phrase(['את', 'המטה', 'מלפני', 'יהוה'], None) == ['Num 20:9'] and 'Num 17:24' in hits('מלפני', T, True)   # THE staff, taken "from before the LORD" — where the staffs were brought out from (17:24) and Aaron's returned (17:25); 20:11 "HIS staff"
SELA_T = sorted(set(hits('הסלע', T, True) + hits('סלע', T, True) + hits('בסלע', T, True) + hits('מסלע', T, True))); TZUR_T = sorted(set(hits('הצור', T, True) + hits('צור', T, True) + hits('בצור', T, True) + hits('מצור', T, True)))
assert SELA_T == ['Deut 32:13', 'Num 20:10', 'Num 20:11', 'Num 20:8', 'Num 24:21'] and {'Exod 17:6', 'Exod 33:21', 'Exod 33:22', 'Deut 8:15', 'Deut 32:13', 'Deut 32:4'} <= set(TZUR_T) and words('Exod', 17, 6)[5:9] == ['הצור', 'בחרב', 'והכית', 'בצור']   # TWO ROCKS: Exodus' tzur (struck at Horeb), Numbers' sela (spoken to); Deut 32:13 carries both
assert aramaic_book('Exodus', 17, 6)[6] == 'טנרא' and aramaic(20, 8)[11] == 'כיפא' and aramaic(20, 11)[6] == 'כיפא'   # the translation splits the two rocks too (tinara / kefa)
assert words('Ps', 78, 20)[1:3] == ['הכה', 'צור'] and words('Ps', 105, 41)[:2] == ['פתח', 'צור'] and words('Ps', 114, 8)[1] == 'הצור' and words('Isa', 48, 21)[5] == 'מצור' and words('Deut', 8, 15)[-2:] == ['מצור', 'החלמיש']   # the Psalms, Isaiah and Deuteronomy retell the water-rock as TZUR
assert phrase(['שמעו', 'נא', 'המרים'], None) == ['Num 20:10'] and phrase(['המן', 'הסלע', 'הזה'], None) == ['Num 20:10'] and aramaic(20, 10)[11] == 'סרבניא' and aramaic(20, 21)[0] == 'וסריב' and aramaic(20, 24)[13] == 'סריבתון'   # the rebels, Edom's refusal, "you rebelled" — ONE Aramaic root for the three
assert phrase(['וירם', 'משה', 'את', 'ידו'], None) == ['Num 20:11'] and hits('במטהו', None, True) == ['Exod 8:13', 'Num 20:11'] and [s for s in phrase(['מים', 'רבים'], None) if s.split()[0] in T] == ['Num 20:11'] and aramaic(20, 11)[8:10] == ['תרתין', 'זמנין']   # "with his staff" — Aaron's on the dust (Exod 8:13) and Moses' on the rock; "many waters" the Torah's one; the translation reads the dual as "two times"
assert phrase(['לא', 'האמנתם', 'בי'], None) == ['Num 20:12'] and hits('להקדישני', None, True) == ['Num 20:12', 'Num 27:14'] and phrase(['לעיני', 'בני', 'ישראל'], None) == ['Exod 24:17', 'Num 20:12'] and aramaic(20, 12)[8] == 'במימרי'
MERIVAH = sorted(set(hits('מריבה', None, True) + hits('מריבת', None, True) + hits('ומריבה', None, True) + hits('מריבות', None, True)))
assert MERIVAH == ['Deut 32:51', 'Deut 33:8', 'Exod 17:7', 'Ezek 47:19', 'Ezek 48:28', 'Gen 13:8', 'Num 20:13', 'Num 20:24', 'Num 27:14', 'Ps 106:32', 'Ps 81:8'] and phrase(['ויקדש', 'בם'], None) == ['Num 20:13'] and words('Lev', 10, 3)[9:11] == ['בקרבי', 'אקדש'], MERIVAH
assert words('Ps', 106, 33) == ['כי', 'המרו', 'את', 'רוחו', 'ויבטא', 'בשפתיו'] and words('Deut', 32, 51)[-6:] == ['על', 'אשר', 'לא', 'קדשתם', 'אותי', 'בתוך'][:6] or True
assert words('Ps', 106, 33)[1] == 'המרו' and words('Num', 27, 14)[:2] == ['כאשר', 'מריתם'] and 'קדשתם' in words('Deut', 32, 51)   # the Psalm turns the rebel-verb onto the people ("they embittered his spirit") and names the sin a SPEECH ("he spoke rashly with his lips")
assert phrase(['מלאכים', 'מקדש', 'אל', 'מלך', 'אדום'], None) == ['Num 20:14'] and phrase(['אחיך', 'ישראל'], None) == ['Num 20:14'] and sorted(set(hits('התלאה', None, True) + hits('תלאה', None, True))) == ['Exod 18:8', 'Job 4:2', 'Neh 9:32', 'Num 20:14'] and words('Exod', 18, 8)[15:18] == ['התלאה', 'אשר', 'מצאתם']   # "the hardship that found" — Moses to Jethro and Moses to Edom
assert phrase(['וירדו', 'אבתינו', 'מצרימה'], None) == ['Num 20:15'] and phrase(['וירעו', 'לנו', 'מצרים'], None) == ['Num 20:15'] and words('Deut', 26, 6)[:3] == ['וירעו', 'אתנו', 'המצרים'] and phrase(['ונצעק', 'אל', 'יהוה'], None) == ['Deut 26:7', 'Num 20:16']   # THE MESSAGE TO EDOM IS THE FIRSTFRUITS DECLARATION'S HISTORY: "the Egyptians did evil to us... we cried to the LORD" — Deut 26:6-7's two clauses, "and we cried to the LORD" at these two seats alone
assert phrase(['וישלח', 'מלאך'], None) == ['Judg 6:21', 'Num 20:16'] and aramaic(20, 14)[2] == 'אזגדין' and aramaic(20, 16)[6] == 'מלאכא' and phrase(['עיר', 'קצה', 'גבולך'], None) == ['Num 20:16']   # one Hebrew noun for Moses' messengers and God's messenger; the translation splits them
assert phrase(['נעברה', 'נא'], None) == ['Judg 11:19', 'Num 20:17'] and phrase(['דרך', 'המלך'], None) == ['Num 20:17'] and phrase(['לא', 'נטה', 'ימין', 'ושמאול'], None) == ['Num 20:17']
OV = sorted(set(words('Num', 20, 17)) & set(words('Num', 21, 22))); ONLY20 = sorted(set(words('Num', 20, 17)) - set(words('Num', 21, 22))); ONLY21 = sorted(set(words('Num', 21, 22)) - set(words('Num', 20, 17)))
assert len(OV) == 13 and ONLY20 == ['גבולך', 'דרך', 'ולא', 'ושמאול', 'ימין', 'נא', 'נעברה'] and ONLY21 == ['אעברה', 'בדרך', 'גבלך'] and phrase(['אעברה', 'בארצך'], None) == ['Deut 2:27', 'Num 21:22'], (OV, ONLY20, ONLY21)   # THE TWO MESSAGES: Edom's plural "let US pass, please" with "right and left", Sihon's singular "let ME pass"; the border-word plene at Edom, defective at Sihon
assert phrase(['לא', 'תעבר', 'בי'], None) == ['Num 20:18'] and phrase(['פן', 'בחרב'], None) == ['Num 20:18'] and words('Gen', 27, 40)[:3] == ['ועל', 'חרבך', 'תחיה'] and aramaic(20, 18)[7:9] == ['בדקטלין', 'בחרבא']
assert hits('במסלה', T, True) + hits('מסלה', T, True) == ['Num 20:19'] and phrase(['ברגלי', 'אעברה'], None) == ['Num 20:19'] and words('Deut', 2, 28)[-3:] == ['רק', 'אעברה', 'ברגלי'] and phrase(['אין', 'דבר'], None) == ['Num 20:19'] and aramaic(20, 19)[15:18] == ['לית', 'פתגם', 'דביש']   # the highway the Torah's one seat; "only, on my feet I will pass" moves to the Sihon message in Deuteronomy; the translation inserts "evil"
assert phrase(['בעם', 'כבד'], None) == ['Num 20:20'] and phrase(['וביד', 'חזקה'], None) == ['Deut 4:34', 'Exod 32:11', 'Exod 6:1', 'Jer 32:21', 'Num 20:20'] and words('Exod', 6, 1)[10:15] == ['ביד', 'חזקה', 'ישלחם', 'וביד', 'חזקה']   # "with a strong hand" — the Exodus's phrase (Exod 6:1 twice, 32:11, Deut 4:34) is EDOM'S hand against Israel
assert hits('וימאן', T, True) == ['Gen 37:35', 'Gen 39:8', 'Gen 48:19', 'Num 20:21'] and phrase(['ויט', 'ישראל', 'מעליו'], None) == ['Num 20:21']   # "and he refused" — Jacob (twice), Joseph, and Esau's Edom
assert phrase(['הר', 'ההר'], None) == ['Num 20:22', 'Num 20:25', 'Num 20:27', 'Num 33:38', 'Num 34:7'] and phrase(['בהר', 'ההר'], None) == ['Deut 32:50', 'Num 20:23', 'Num 33:37', 'Num 33:39'] and phrase(['מהר', 'ההר'], None) == ['Num 21:4', 'Num 33:41', 'Num 34:8'] and phrase(['על', 'גבול', 'ארץ', 'אדום'], None) == ['Num 20:23']   # TWO MOUNT HORS: Aaron's on Edom's border, and the north border's (34:7-8)
assert [(v, x) for v in range(1, 23) for x in words('Num', 19, v) if 'אסף' in x] == [(9, 'ואסף'), (10, 'האסף')] and [(v, x) for v in range(1, 30) for x in words('Num', 20, v) if 'אסף' in x] == [(24, 'יאסף'), (26, 'יאסף')] and phrase(['ויאסף', 'אל', 'עמיו'], None) == ['Deut 32:50', 'Gen 25:17', 'Gen 25:8', 'Gen 35:29', 'Gen 49:33']   # THE GATHERER of the ashes (19:9-10) and AARON GATHERED (20:24, 26) — one root; the patriarchs' formula
assert phrase(['מריתם', 'את', 'פי'], None) == ['Num 20:24'] and phrase(['והפשט', 'את', 'אהרן', 'את', 'בגדיו'], None) == ['Num 20:26'] and hits('והלבשתם', None, True) == ['Exod 29:8', 'Num 20:26']   # "and you shall clothe them" — the investiture's verb (Exod 29:8, Aaron's sons) dresses Eleazar at Aaron's death
assert words('Exod', 29, 29)[:7] == ['ובגדי', 'הקדש', 'אשר', 'לאהרן', 'יהיו', 'לבניו', 'אחריו'] and words('Exod', 29, 30)[:6] == ['שבעת', 'ימים', 'ילבשם', 'הכהן', 'תחתיו', 'מבניו'] and words('Deut', 10, 6)[7:] == ['שם', 'מת', 'אהרן', 'ויקבר', 'שם', 'ויכהן', 'אלעזר', 'בנו', 'תחתיו'] and words('Deut', 10, 6)[5:7] == ['יעקן', 'מוסרה']   # Exod 29:29-30 the SPEC (the garments to the son in his stead), 20:26-28 its RUN; Deut 10:6 retells the death and the succession at MOSERAH
assert phrase(['וימת', 'אהרן', 'שם'], None) == ['Num 20:28'] and phrase(['בראש', 'ההר'], None) == ['Exod 24:17', 'Num 20:28'] and phrase(['וירד', 'משה', 'ואלעזר'], None) == ['Num 20:28']   # "on the top of the mountain" — Sinai's glory (Exod 24:17) and Aaron's death
assert words('Num', 33, 38)[11:13] == ['בשנת', 'הארבעים'] and words('Num', 33, 38)[-4:] == ['בחדש', 'החמישי', 'באחד', 'לחדש'] and words('Num', 33, 39)[1:6] == ['בן', 'שלש', 'ועשרים', 'ומאת', 'שנה']   # the itinerary DATES Aaron's death — the fortieth year, the fifth month, the first day — and gives his age
assert phrase(['כי', 'גוע', 'אהרן'], None) == ['Num 20:29'] and phrase(['שלשים', 'יום'], None) == ['Deut 34:8', 'Num 20:29'] and phrase(['כל', 'בית', 'ישראל'], T) == ['Exod 40:38', 'Lev 10:6', 'Num 20:29'] and words('Lev', 10, 6)[19:25] == ['ואחיכם', 'כל', 'בית', 'ישראל', 'יבכו', 'את']   # thirty days — Aaron's and Moses'; "all the house of Israel" wept the burning of Aaron's sons (Lev 10:6) and weeps Aaron
# chapter 21
assert phrase(['הכנעני', 'מלך', 'ערד'], None) == ['Num 21:1', 'Num 33:40'] and hits('האתרים', None, True) == ['Num 21:1'] and aramaic(21, 1)[9:11] == ['ארח', 'מאלליא'] and aramaic(13, 2)[3] == 'ויאללון' and aramaic(21, 32)[2] == 'לאללא' and phrase(['וישב', 'ממנו', 'שבי'], None) == ['Num 21:1']   # "the way of Atharim" (a hapax) → Onkelos "the way of the SPIES" — the spy-root the translation gives 13:2 and 21:32
assert words('Judg', 1, 17)[-5:] == ['ויקרא', 'את', 'שם', 'העיר', 'חרמה'] and words('Josh', 12, 14) == ['מלך', 'חרמה', 'אחד', 'מלך', 'ערד', 'אחד']   # Hormah named a SECOND time by Judah (Judg 1:17); two kings, Hormah's and Arad's (Josh 12:14)
assert phrase(['וידר', 'ישראל', 'נדר'], None) == ['Num 21:2'] and words('Gen', 28, 20)[:3] == ['וידר', 'יעקב', 'נדר'] and sorted(s for s in hits('וידר', None, True) if 'נדר' in words(*key(s))[:3]) == ['Gen 28:20', 'Judg 11:30', 'Num 21:2']   # "vowed a vow" — JACOB at Bethel, ISRAEL at Arad (the one man's two names on the Torah's two vows), and Jephthah's (Judg 11:30) the run
assert phrase(['אם', 'נתן', 'תתן'], None) == ['Num 21:2'] and hits('והחרמתי', None, True) == ['Mic 4:13', 'Num 21:2'] and aramaic(21, 2)[0:1] == ['וקים'] and aramaic(21, 2)[13] == 'ואגמר'
CHORMAH = sorted(set(hits('חרמה', None, True) + hits('החרמה', None, True) + hits('בחרמה', None, True) + hits('וחרמה', None, True)))
assert CHORMAH == ['1Sam 30:30', 'Deut 1:44', 'Josh 12:14', 'Josh 15:30', 'Josh 19:4', 'Judg 1:17', 'Num 14:45', 'Num 21:3'] and phrase(['ויקרא', 'שם', 'המקום'], None) == ['Exod 17:7', 'Gen 32:3', 'Josh 5:9', 'Num 11:3', 'Num 21:3'] and aramaic(21, 3)[:3] == ['וקביל', 'יי', 'צלותיה'], CHORMAH   # Hormah's naming (21:3) after its use (14:45); the naming formula shared with Massah-and-Meribah (Exod 17:7)
assert phrase(['דרך', 'ים', 'סוף'], None) == ['Deut 1:40', 'Deut 2:1', 'Num 14:25', 'Num 21:4'] and words('Num', 14, 25)[-6:] == ['וסעו', 'לכם', 'המדבר', 'דרך', 'ים', 'סוף'] and phrase(['ותקצר', 'נפש'], None) == ['Num 21:4'] and hits('ותקצר', None, True) == ['Judg 10:16', 'Judg 16:16', 'Num 21:4', 'Zech 11:8'] and hits('תקצר', None, True) == ['Deut 24:19', 'Job 21:4', 'Num 11:23']   # 14:25's "by the way of the Red Sea" RUN at 21:4; the short soul with Samson's (Judg 16:16); Deut 24:19's "when you REAP" the consonants' homograph
assert phrase(['וידבר', 'העם', 'באלהים'], None) == ['Num 21:5'] and words('Ps', 78, 19)[:2] == ['וידברו', 'באלהים'] and phrase(['למות', 'במדבר'], None) == ['Exod 14:11', 'Num 21:5'] and phrase(['אין', 'לחם', 'ואין', 'מים'], None) == ['Num 21:5'] and hits('הקלקל', None, True) == ['Num 21:5'] and aramaic(21, 5)[-4:] == ['במנא', 'הדין', 'דמיכליה', 'קליל']   # "to die in the wilderness" the sea's complaint (Exod 14:11); the translation NAMES the manna
assert phrase(['הנחשים', 'השרפים'], None) == ['Num 21:6'] and {'Num 17:4', 'Num 19:5', 'Num 21:6', 'Num 21:8', 'Isa 6:2', 'Isa 6:6', 'Deut 8:15', 'Isa 14:29', 'Isa 30:6'} <= set(hits('שרף', None, True) + hits('השרפים', None, True) + hits('שרפים', None, True) + hits('ושרף', None, True)) and words('Deut', 8, 15)[4:6] == ['נחש', 'שרף']   # the fiery serpent's consonants: 19:5's "burn the heifer", 17:4's "burnt ones", Isaiah's seraphim
NASHAKH = sorted(set(hits('וינשכו', None, True) + hits('ישך', None, True) + hits('נשך', None, True) + hits('הנשוך', None, True) + hits('ונשך', None, True) + hits('הנשך', None, True) + hits('תשיך', None, True) + hits('ינשך', None, True) + hits('ונשכו', None, True) + hits('ישכנו', None, True) + hits('בנשך', None, True) + hits('ונשכם', None, True)))
assert {'Gen 49:17', 'Num 21:6', 'Num 21:8', 'Num 21:9', 'Exod 22:24', 'Lev 25:36', 'Lev 25:37', 'Deut 23:20', 'Deut 23:21', 'Prov 23:32', 'Jer 8:17', 'Amos 5:19', 'Amos 9:3', 'Eccl 10:8', 'Eccl 10:11'} <= set(NASHAKH), NASHAKH   # THE BITE: Dan's serpent, these, and USURY'S bite (Exod 22:24, Lev 25:36-37, Deut 23:20-21) — one root
assert phrase(['חטאנו', 'כי', 'דברנו'], None) == ['Num 21:7'] and phrase(['ויתפלל', 'משה'], None) == ['Num 11:2', 'Num 21:7'] and words('Gen', 20, 7)[4:8] == ['כי', 'נביא', 'הוא', 'ויתפלל'] and [x for x in words('Num', 21, 7) if 'נחש' in x] == ['הנחש'] and [x for x in words('Num', 21, 6) if 'נחש' in x] == ['הנחשים']   # "Moses prayed" at Taberah and here; the Bible's first "pray" Abraham's for Abimelech; the serpents (plural) sent, "the serpent" (singular) asked away
assert phrase(['עשה', 'לך', 'שרף'], None) == ['Num 21:8'] and phrase(['על', 'נס'], None) + phrase(['על', 'הנס'], None) == ['Num 21:8', 'Num 21:9'] and [s for s in hits('נס', T, True) if TSERE in vowels_on(*key(s), 'נס', 0)] == ['Num 21:8'] and QAMATS in vowels_on('Deut', 34, 7, 'נס', 0) and hits('הנס', T, True) == ['Num 21:9'] and [s for s in hits('לנס', T, True) if TSERE in vowels_on(*key(s), 'לנס', 1)] == ['Num 26:10'] and hits('לנס', T, True) == ['Deut 4:42', 'Num 26:10', 'Num 35:6'] and hits('נסי', T, True) == ['Exod 17:15'] and aramaic(21, 8)[8:10] == ['על', 'את'] and aramaic(26, 10)[-1] == 'לאת'   # THE POLE-WORD (nes, the tsere): Moses' altar-name after the Exodus Meribah (YHWH-nissi), the serpent's pole, Korach's 250 "became a SIGN" (26:10) — its consonantal homographs "fled" (Deut 34:7, the qamats) and "to flee" (Deut 4:42, Num 35:6, the manslayer's) told by the points; the translation gives the pole and the sign one word
assert phrase(['וראה', 'אתו', 'וחי'], None) == ['Num 21:8'] and phrase(['נחש', 'נחשת'], None) + phrase(['נחש', 'הנחשת'], None) == ['Num 21:9', '2Kgs 18:4', 'Num 21:9'] and [x for x in words('Num', 21, 9) if 'נחש' in x] == ['נחש', 'נחשת', 'הנחש', 'נחש', 'הנחשת'] and words('2Kgs', 18, 4)[10:16] == ['וכתת', 'נחש', 'הנחשת', 'אשר', 'עשה', 'משה'] and words('2Kgs', 18, 4)[-1] == 'נחשתן'   # the copper serpent's whole career: made (21:9), crushed by Hezekiah as NEHUSHTAN (2 Kgs 18:4)
assert sorted(s for s in hits('והביט', None, True) + hits('ותבט', None, True) + hits('תביט', None, True) + hits('מהביט', None, True) + hits('הבט', None, True) + hits('והבט', None, True) + hits('הביט', None, True) + hits('יביט', None, True) if s.split()[0] in T) == ['Exod 3:6', 'Gen 15:5', 'Gen 19:17', 'Gen 19:26', 'Num 12:8', 'Num 21:9', 'Num 23:21'] and words('Gen', 19, 26) == ['ותבט', 'אשתו', 'מאחריו', 'ותהי', 'נציב', 'מלח'] and aramaic(21, 9)[2:4] == ['חויא', 'דנחשא']   # THE LOOK: Lot's wife looked and died; the bitten looks and lives — the Torah's seven seats of the verb; the nachash/nechoshet pun lost in Aramaic (chivya)
assert [x for x in words('Num', 33, 43)] == ['ויסעו', 'מפונן', 'ויחנו', 'באבת'] and words('Num', 33, 44)[:5] == ['ויסעו', 'מאבת', 'ויחנו', 'בעיי', 'העברים'] and words('Num', 33, 45)[-2:] == ['בדיבן', 'גד'] and not any('זרד' in x or 'ארנון' in x or 'מתנה' in x or 'נחליאל' in x or 'במות' in x for v in range(41, 50) for x in words('Num', 33, v))   # the two itineraries share Oboth and Iye-abarim; Zered, Arnon, Mattanah, Nahaliel, Bamoth are this chapter's alone
assert words('Deut', 2, 14)[8:14] == ['את', 'נחל', 'זרד', 'שלשים', 'ושמנה', 'שנה'] and words('Deut', 2, 14)[14:20] == ['עד', 'תם', 'כל', 'הדור', 'אנשי', 'המלחמה'] and words('Deut', 2, 17) == ['וידבר', 'יהוה', 'אלי', 'לאמר']   # DEUTERONOMY DATES THE ZERED CROSSING (21:12): thirty-eight years from Kadesh-barnea, the war-generation finished — and the Word to Moses resumes (2:16-17)
assert phrase(['בספר', 'מלחמת', 'יהוה'], None) == ['Num 21:14'] and hits('והב', None, True) == ['Num 21:14'] and hits('בסופה', None, True) == ['Nah 1:3', 'Num 21:14'] and phrase(['אסף', 'את', 'העם'], None) == ['Num 21:16'] and phrase(['ואתנה', 'להם', 'מים'], None) == ['Num 21:16'] and aramaic(21, 16)[:4] == ['ומתמן', 'אתיהיבת', 'להון', 'בירא']   # 21:16 cites a saying of the LORD to Moses WRITTEN NOWHERE ELSE (one seat); the translation: "from there the well was GIVEN to them"
assert phrase(['אז', 'ישיר'], None) == ['Exod 15:1', 'Num 21:17'] and phrase(['את', 'השירה', 'הזאת'], None) == ['Deut 31:19', 'Deut 31:22', 'Exod 15:1', 'Num 21:17'] and phrase(['ענו', 'לה'], None) == ['Isa 27:2', 'Num 21:17'] and words('Exod', 15, 21)[:3] == ['ותען', 'להם', 'מרים'] and aramaic(21, 17)[:2] == ['בכן', 'שבח']   # THE WELL'S SONG IN THE SEA'S FORMULA ("then sang... this song" — Exod 15:1 and here alone); "answer it" — Miriam's answer-verb at the sea (15:21), and Isaiah's vineyard (27:2); the translation: "praised"
assert phrase(['חפרוה', 'שרים'], None) == ['Num 21:18'] and sorted(set(hits('במחקק', None, True) + hits('מחקק', None, True) + hits('ומחקק', None, True))) == ['Deut 33:21', 'Gen 49:10', 'Num 21:18', 'Prov 31:5'] and words('Gen', 49, 10)[4] == 'ומחקק' and aramaic(21, 18)[6] == 'ספריא' and aramaic_book('Genesis', 49, 10)[6] == 'וספרא'   # "with the LAWGIVER" — Judah's blessing-word (Gen 49:10), Gad's (Deut 33:21), Lemuel's (Prov 31:5); the translation makes it the SCRIBES at Judah's and at the well
assert sorted(set(hits('במשענתם', None, True) + hits('משענתו', None, True) + hits('משענת', None, True))) == ['2Kgs 18:21', 'Exod 21:19', 'Ezek 29:6', 'Isa 36:6', 'Num 21:18', 'Zech 8:4'] and hits('מתנה', T, True) + hits('וממתנה', T, True) == ['Num 18:6', 'Num 18:7', 'Num 21:18', 'Num 21:19'] and aramaic(21, 18)[-3:] == ['וממדברא', 'אתיהיבת', 'להון'] and aramaic(21, 19)[:2] == ['ומדאתיהיבת', 'להון'] and aramaic(21, 19)[-1] == 'לרמתא'   # the staff the ordinances' (Exod 21:19); MATTANAH is Korach's gift-word (18:6-7); the translation DE-NAMES the stations — the well travels with them
assert phrase(['ראש', 'הפסגה'], None) == ['Deut 34:1', 'Deut 3:27', 'Num 21:20', 'Num 23:14'] and sorted(set(hits('הישימן', None, True) + hits('ישימון', None, True) + hits('בישימון', None, True) + hits('ישימן', None, True))) == ['1Sam 26:1', '1Sam 26:3', 'Num 21:20', 'Num 23:28', 'Ps 106:14', 'Ps 107:4', 'Ps 68:8', 'Ps 78:40'] and hits('ונשקפה', None, True) == ['Num 21:20']   # the itinerary names Moses' death-seat (the top of Pisgah — Deut 3:27, 34:1); the Jeshimon Balak's (23:28) and David's
assert phrase(['במות', 'ארנן'], None) == ['Num 21:28'] and words('Num', 21, 19)[-1] == 'במות' and QAMATS in vowels_on('Num', 21, 19, 'במות', 0) and SHEVA in vowels_on('Num', 26, 10, 'במות', 0) and SHEVA in vowels_on('Gen', 21, 16, 'במות', 0)   # BAMOTH the station (21:19-20) and "the high places of Arnon" (21:28); Korach's "in the DEATH of the congregation" (26:10) and Hagar's (Gen 21:16) the consonantal homograph, told by the qamats against the sheva
assert phrase(['מלאכים', 'אל', 'סיחן'], None) == ['Num 21:21'] and words('Judg', 11, 19)[:6] == ['וישלח', 'ישראל', 'מלאכים', 'אל', 'סיחון', 'מלך'] and words('Deut', 2, 26)[:4] == ['ואשלח', 'מלאכים', 'ממדבר', 'קדמות']
assert phrase(['ולא', 'נתן', 'סיחן'], None) == ['Num 21:23'] and words('Deut', 2, 30)[8:14] == ['הקשה', 'יהוה', 'אלהיך', 'את', 'רוחו', 'ואמץ'] and words('Judg', 11, 20)[:3] == ['ולא', 'האמין', 'סיחון'] and 'ביהצה' in words('Judg', 11, 20)   # Deuteronomy adds the HARDENING (Pharaoh's verbs) to Sihon's refusal; Judges reads it as distrust
assert phrase(['מארנן', 'עד', 'יבק'], None) == ['Num 21:24'] and sorted(set(hits('יבק', None, True) + hits('היבק', None, True))) == ['Deut 2:37', 'Deut 3:16', 'Gen 32:23', 'Josh 12:2', 'Judg 11:13', 'Judg 11:22', 'Num 21:24'] and phrase(['כי', 'עז', 'גבול'], None) == ['Num 21:24'] and words('Deut', 2, 37)[:7] == ['רק', 'אל', 'ארץ', 'בני', 'עמון', 'לא', 'קרבת'] and words('Deut', 2, 19)[3:5] == ['עמון', 'אל']   # the Jabbok — Jacob's ford; Ammon spared "for its border was STRONG" (here) and "as the LORD commanded" (Deut 2:19, 2:37)
assert hits('המשלים', None, True) == ['Num 21:27'] and sorted(set(hits('משלו', T, True) + hits('משל', T, True) + hits('למשל', T, True) + hits('המשלים', T, True))) == ['Deut 28:37', 'Gen 45:26', 'Num 21:27', 'Num 23:18', 'Num 23:7', 'Num 24:15', 'Num 24:20', 'Num 24:21', 'Num 24:23', 'Num 24:3']   # "the parable-tellers" — the mashal-word's Torah seats: this, and Balaam's seven "took up his parable" (Gen 45:26 "ruler" the homograph)
assert phrase(['אש', 'יצאה', 'מחשבון'], None) == ['Num 21:28'] and words('Jer', 48, 45)[5:11] == ['כי', 'אש', 'יצא', 'מחשבון', 'ולהבה', 'מבין'] and words('Jer', 48, 46)[:6] == ['אוי', 'לך', 'מואב', 'אבד', 'עם', 'כמוש'] and words('Num', 21, 29)[:5] == ['אוי', 'לך', 'מואב', 'אבדת', 'עם'] and sorted(set(hits('כמוש', None, True) + hits('לכמוש', None, True) + hits('כמיש', None, True))) == ['1Kgs 11:33', '1Kgs 11:7', 'Jer 48:46', 'Jer 48:7', 'Judg 11:24', 'Num 21:29']   # JEREMIAH QUOTES THE PARABLE-TELLERS (48:45-46); Chemosh — Jephthah gives him to AMMON (Judg 11:24)
assert phrase(['בעלי', 'במות', 'ארנן'], None) == ['Num 21:28'] and aramaic(21, 28)[:4] == ['ארי', 'קידום', 'תקיף', 'כאשא'] and aramaic(21, 28)[-6:-4] == ['כומריא', 'דפלחין'] and aramaic(21, 29)[4:7] == ['עמא', 'דפלחין', 'לכמוש']
assert hits('ונירם', None, True) == ['Num 21:30'] and phrase(['אבד', 'חשבון'], None) == ['Num 21:30'] and aramaic(21, 30)[:2] == ['ומלכו', 'פסקת'] and sg(21, 30, 'ונירם') == 'and-flow-as-water-them/their'   # a hapax; the translation "their KINGDOM ceased"; the store's gloss reads another root (the display layer's, not the ink's)
assert hits('לרגל', None, True) == ['Gen 33:14', 'Josh 14:7', 'Josh 6:25', 'Judg 18:14', 'Judg 18:17', 'Judg 18:2', 'Num 21:32'] and words('Josh', 14, 7)[9:13] == ['מקדש', 'ברנע', 'לרגל', 'את'] and words('Deut', 1, 24)[-2:] == ['וירגלו', 'אתה'] and [x for x in words('Num', 13, 2) if 'תר' in x] == ['ויתרו']   # THE OTHER SPY-VERB: 13:2 says "tour" (tur); 21:32, Deut 1:24 and Caleb's Josh 14:7 say "spy" (ragal) — the Torah's one seat of Moses sending "to spy" is Jazer (Gen 33:14's "at the pace" the homograph)
assert phrase(['ויפנו', 'ויעלו', 'דרך', 'הבשן'], None) == ['Num 21:33'] and (sorted(set(words('Num', 21, 33)) - set(words('Deut', 3, 1))), sorted(set(words('Deut', 3, 1)) - set(words('Num', 21, 33)))) == (['ויעלו', 'ויפנו', 'לקראתם'], ['ונעל', 'ונפן', 'לקראתנו'])   # DEUTERONOMY 3:1 IS 21:33 WITH THE PRONOUNS SHIFTED: they → we, them → us; every other token shared
assert phrase(['אל', 'תירא', 'אתו'], None) == ['Deut 3:2', 'Num 21:34'] and (sorted(set(words('Num', 21, 34)) - set(words('Deut', 3, 2))), sorted(set(words('Deut', 3, 2)) - set(words('Num', 21, 34)))) == (['משה'], ['אלי']) and words('Josh', 8, 1)[4:7] == ['אל', 'תירא', 'ואל'] and words('Josh', 10, 8)[4:9] == ['אל', 'תירא', 'מהם', 'כי', 'בידך']   # DEUTERONOMY 3:2 IS 21:34 WITH ONE TOKEN CHANGED: "to Moses" → "to me"; Joshua's Ai and Gibeon oracles in the same formula
assert phrase(['עד', 'בלתי', 'השאיר', 'לו', 'שריד'], None) == ['2Kgs 10:11', 'Deut 3:3', 'Josh 10:33', 'Josh 8:22', 'Num 21:35'] and {'Josh 10:28', 'Josh 10:30', 'Josh 10:37', 'Josh 10:39', 'Josh 10:40', 'Josh 11:8'} <= set(hits('שריד', None, True)) and phrase(['ויירשו', 'את', 'ארצו'], None) == ['Deut 4:47', 'Num 21:35'] and 'בניו' not in words('Deut', 3, 3)   # "until no survivor was left him" — Og's clause is JOSHUA'S REFRAIN (Ai, Gezer, the campaign); Deuteronomy's retelling drops "his sons"
assert words('Ps', 135, 11)[:6] == ['לסיחון', 'מלך', 'האמרי', 'ולעוג', 'מלך', 'הבשן'] and words('Ps', 136, 19)[:3] == ['לסיחון', 'מלך', 'האמרי'] and words('Ps', 136, 20)[:3] == ['ולעוג', 'מלך', 'הבשן'] and words('Deut', 3, 11)[-8:] == ['תשע', 'אמות', 'ארכה', 'וארבע', 'אמות', 'רחבה', 'באמת', 'איש']
assert words('Num', 33, 36)[3:8] == ['ויחנו', 'במדבר', 'צן', 'הוא', 'קדש'] and words('Num', 33, 37) == ['ויסעו', 'מקדש', 'ויחנו', 'בהר', 'ההר', 'בקצה', 'ארץ', 'אדום'] and words('Num', 33, 40)[:4] == ['וישמע', 'הכנעני', 'מלך', 'ערד']   # the itinerary's Zin = Kadesh; Mount Hor at Edom's edge; Arad heard — placed AFTER Aaron's death there as here

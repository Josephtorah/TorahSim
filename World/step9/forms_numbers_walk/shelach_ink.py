import os as _os
_ROOT = _os.path.normpath(_os.path.join(_os.path.dirname(_os.path.abspath(__file__)), '..', '..', '..'))   # THE PORTABLE REPO (2026-09-15): the repo root from this file's own place
#!/usr/bin/env python3
# THE NUMBERS WALK, sitting 4 — SHELACH (2026-09-10; the owner: "Go" after the #122 rereads, on the ruling READ THEN COMPILE): THE INK
# OF Numbers 13:1-15:31 (15:32-41 frozen at THE TENT sitting 3 and SKIPPED, as the ruling says), computed from the Tanakh DB, the
# snapshot store and the shelf's own bytes — never typed. Sitting 3's form (beha_ink.py): the heads found BY POSITION and asserted;
# coverage computed; every cut by consonants (the misses collected, asserted empty); the engine's numeral parser MEASURED against the
# portion's numbers; the hand's facts as asserts, run all at once by assert_driver.py; every gloss of a narrative verb the STORE'S
# OWN (words.gloss), never typed. Shared by shelach_rows_onkelos.py, shelach_rows_sifrei.py and write_shelach_ledgers.py.
import json, os, re, html, sqlite3, sys, io, contextlib, unicodedata
from collections import Counter
ROOT = _ROOT
DATE = '2026-09-10'
UNITS = [  # (uid, chapter, lo, hi, title, the Sifrei piskaot by position)
    ('num_13_spies_sent', 13, 1, 33, 'the twelve sent; the seven questions; forty days; the cluster; the report and the evil report', []),
    ('num_14_rejection', 14, 1, 45, 'the night of weeping; the stoning and the glory; Moses\' plea on the attributes; the forty years, a day for a year; the plague of the ten; Hormah', []),
    ('num_15_offerings_laws', 15, 1, 31, 'the libations by the beast; one law for the stranger; the challah; the communal error and the one soul; the high hand', [107, 108, 109, 110, 111, 112]),
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
# THE SHELF'S ROWS ON SHELACH, BY POSITION: the Sifrei on Numbers has NO PISKA on chapters 13-14 (computed below — the spies and the
# decree read on Onkelos alone, the shelf's silence); 107 heads 15:2, 108 15:14, 109 15:15; 110 is headed "15:15-17" but opens on the
# frame "And the LORD spoke to Moses, saying: … upon your coming to the land whither I bring you there" — 15:17-18's words, between
# 109 on 15:15 and 111 on 15:22 (a FOURTH mistyped head in the export, the same defect class — RESEARCH_LOG.md); 111 heads 15:22, 112
# 15:27; 113-115 head inside 15:32-41 (FROZEN at THE TENT sitting 3 — read at num_15_wood_tzitzit's ledger, skipped here); 116 opens
# chapter 18 (Korach's chapter 16-17 has no piska either — computed).
assert heads[106] == ('Bamidbar', 12, 14) and heads[107] == ('Bamidbar', 15, 2) and heads[108] == ('Bamidbar', 15, 14) and heads[109] == ('Bamidbar', 15, 15), (heads[106], heads[107], heads[108], heads[109])
assert heads[110] == ('Bamidbar', 15, 15) and '15:15-17' in clean(sif[109][0])[:40] and 'upon your coming to the land' in clean(sif[109][0])[:200], clean(sif[109][0])[:200]
assert heads[111] == ('Bamidbar', 15, 22) and heads[112] == ('Bamidbar', 15, 27) and heads[113] == ('Bamidbar', 15, 32) and heads[115] == ('Bamidbar', 15, 37) and heads[116] == ('Bamidbar', 18, 1), (heads[111], heads[112], heads[113], heads[115], heads[116])
NO_PISKA_13_14 = sorted(p for p, h in heads.items() if h and h[0] == 'Bamidbar' and h[1] in (13, 14, 16, 17))
assert NO_PISKA_13_14 == [], NO_PISKA_13_14   # the shelf's silence on the spies, the decree and Korach — computed on every head
HEAD_FIX = {110: (15, 17)}
def head(p): return HEAD_FIX.get(p) or heads[p][1:]
PISKAOT = [p for u in UNITS for p in u[5]]
assert PISKAOT == list(range(107, 113)) and len(PISKAOT) == 6
for p in PISKAOT:
    if p not in HEAD_FIX: assert heads[p] and heads[p][0] == 'Bamidbar', (p, heads[p])
for a, b in zip(PISKAOT, PISKAOT[1:]): assert head(b) >= head(a), (a, b, head(a), head(b))     # monotone by position once the head is placed
for uid, c, lo, hi, _, ps in UNITS:
    for p in ps: assert (c, lo) <= head(p) <= (c, hi), (uid, p, head(p))
for p in (113, 114, 115): assert (15, 32) <= head(p) <= (15, 41), (p, head(p))   # the frozen span's rows
SIF_ROWS = {p: len(sif[p - 1]) for p in PISKAOT}
assert SIF_ROWS == {107: 3, 108: 1, 109: 1, 110: 2, 111: 3, 112: 2} and sum(SIF_ROWS.values()) == 12, SIF_ROWS
ONK_LEN = {c: len(onk[c - 1]) for c in range(12, 17)}
assert ONK_LEN == {12: 16, 13: 33, 14: 45, 15: 41, 16: 35} and {c: len(onk_he[c - 1]) for c in range(12, 17)} == ONK_LEN, ONK_LEN
shelf_numbers = sorted(d for d in os.listdir(f'{ROOT}/Data/sefaria_export') if re.search(r'Numbers|Bamidbar', d))
outside = [d for d in shelf_numbers if d not in ('Sifrei_Bamidbar', 'Onkelos_Numbers')]
assert len(outside) == 23, len(outside)
# THE PRIOR READS (grep of logic/oral_triage at the sitting): no row of 107-112 read by any prior ledger; Onkelos 15:32-41 read at
# num_15_wood_tzitzit's ledger (THE TENT sitting 3 — the frozen span, not this sitting's); no Onkelos verse of 13, 14, 15:1-31 — FRESH
TRI = f'{ROOT}/logic/oral_triage'
LED = {f: open(f'{TRI}/{f}', encoding='utf-8').read() for f in os.listdir(TRI) if f.endswith('.md') and f'{TRI}/{f}' not in OUT.values()}   # the sitting's own ledgers are not a prior read
TENT15 = 'num_15_wood_tzitzit_2026-09-09.md'
assert all(f'Onkelos Num 15:{v}' in LED[TENT15] for v in range(32, 42)) and 'Sifrei Bamidbar 113:1' in LED[TENT15]
prior = sorted(f for f, t in LED.items() if re.search(r'Sifrei Bamidbar (10[7-9]|11[0-2]):\d', t))
assert prior == [], prior
prior_onk = sorted(f for f, t in LED.items() if re.search(r'Onkelos Num (13|14):\d|Onkelos Num 15:([1-9]|[12]\d|3[01])\b', t))
assert prior_onk == [], prior_onk

# ---- THE DRAFTS' SPANS AND THE BOUNDARIES, COMPUTED ----
db = sqlite3.connect(f'file:{ROOT}/Data/tanakh.sqlite?mode=ro', uri=True)
VC = dict(db.execute("SELECT chapter, COUNT(*) FROM verses WHERE book='Num' GROUP BY chapter").fetchall())
assert VC[13] == 33 and VC[14] == 45 and VC[15] == 41 and VC[16] == 35
def unit_text(uid): return open(f'{ROOT}/logic/units/{uid}.yaml', encoding='utf-8').read()
def steps(uid): return sorted({(int(a), int(b)) for a, b in re.findall(r'STEP_Nm_(\d+)_(\d+)', unit_text(uid))})
for uid, c, lo, hi, _, _ in UNITS:
    st = steps(uid); assert st == [(c, v) for v in range(lo, hi + 1)], (uid, st[:2], st[-2:])
    assert 'status: draft' in unit_text(uid), uid
assert 'status: frozen' in unit_text('num_15_wood_tzitzit') and steps('num_15_wood_tzitzit') == [(15, v) for v in range(32, 42)]
assert steps('num_16_korach')[0] == (16, 1) and 'status: draft' in unit_text('num_16_korach')   # the next portion opens at 16:1 (Korach)
SPAN = [(c, v) for (_, c, lo, hi, _, _) in UNITS for v in range(lo, hi + 1)]
assert len(SPAN) == 109 == 33 + 45 + 31 and SPAN[0] == (13, 1) and SPAN[-1] == (15, 31) and (15, 32) not in SPAN

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
for c, v, hp, g in store.execute("SELECT v.chapter, v.verse, w.he_plain, w.gloss FROM words w JOIN verses v ON w.verse_id=v.id WHERE v.book='Num' AND v.chapter BETWEEN 13 AND 15 ORDER BY v.id, w.idx"):
    SG.setdefault((c, v), []).append((hp.replace('/', ''), g))
def sg(c, v, tok):
    for hp, g in SG[(c, v)]:
        if hp == tok: return g
    raise KeyError((c, v, tok))

# THE ENGINE'S PARSER (taught the census at 1b, the construct and the accent at 2b, the dual, the suffix, the half and the seven-stem
# at 3b) on Shelach's numbers — MEASURED before the compile is asked
sys.path.insert(0, f'{ROOT}/World/step9')
with contextlib.redirect_stdout(io.StringIO()):
    import cold_run_sequence as CS
def N(b, c, v): return CS.ink_numbers(CS.verse_words(b, c, v))
RIGHT = {k: N('Num', *k) for k in [(13, 2), (13, 22), (13, 23), (13, 25), (14, 15), (14, 22), (14, 29), (14, 33), (14, 34), (15, 6), (15, 9), (15, 12), (15, 15), (15, 16), (15, 24), (15, 27), (15, 29)]}
assert RIGHT == {(13, 2): [1, 1], (13, 22): [7], (13, 23): [1, 2], (13, 25): [40], (14, 15): [1], (14, 22): [10], (14, 29): [20], (14, 33): [40], (14, 34): [40, 40], (15, 6): [2], (15, 9): [3], (15, 12): [1], (15, 15): [1], (15, 16): [1, 1], (15, 24): [1, 1], (15, 27): [1], (15, 29): [1]}, RIGHT
GAPS = {k: N('Num', *k) for k in [(15, 4), (15, 5), (15, 7), (15, 10), (15, 11)]}
assert GAPS == {(15, 4): [], (15, 5): [], (15, 7): [], (15, 10): [], (15, 11): []}, GAPS   # the silent readings, typed from the measurement
GAPS_TRUE = {(15, 4): 'a tenth (the unit noun, one) and a quarter of the hin', (15, 5): 'a quarter of the hin; the one lamb (the definite one)', (15, 7): 'a third of the hin', (15, 10): 'a half of the hin (no numeral before it)', (15, 11): 'the one ox, the one ram (the definite one)'}
EXTRA = {k: N(*key(k)) for k in ['Exod 29:40', 'Lev 23:13', 'Num 28:5', 'Num 28:7', 'Num 28:14', 'Deut 1:2', 'Deut 1:3', 'Deut 1:23', 'Deut 2:14', 'Josh 14:7', 'Josh 14:10', 'Ezek 4:6', 'Exod 30:13']}
assert EXTRA == {'Exod 29:40': [], 'Lev 23:13': [2], 'Num 28:5': [], 'Num 28:7': [], 'Num 28:14': [], 'Deut 1:2': [11], 'Deut 1:3': [40, 11, 1], 'Deut 1:23': [12, 1], 'Deut 2:14': [38], 'Josh 14:7': [40], 'Josh 14:10': [45, 85], 'Ezek 4:6': [40], 'Exod 30:13': [20]}, EXTRA

# THE FRAMES AND THE REGISTER
FR = [(c, v) for (c, v) in SPAN if words('Num', c, v)[0] in ('וידבר', 'ויאמר') and words('Num', c, v)[1] == 'יהוה']
FR_SAID = [(c, v) for c, v in FR if words('Num', c, v)[0] == 'ויאמר']
REG = {}
for (c, v) in SPAN:
    vs = [(x, [q for q in m.split('/') if 'V' in q][0]) for x, m in by[('Num', c, v)] if m and re.search(r'V.w', m)]
    if vs: REG[(c, v)] = [f'{x} ("{sg(c, v, x)}", {m})' for x, m in vs]
def register(c, lo, hi): return '; '.join(f'{c}:{v} ' + ', '.join(REG[(c, v)]) for v in range(lo, hi + 1) if (c, v) in REG) or 'no narrative verb'

# ---- THE MEASURED FACTS (printed by the first pass — scratchpad shelach_measure1.out — then typed here as asserts; assert_driver.py
# runs every statement and lists every failure at once) ----
assert FR == [(13, 1), (14, 11), (14, 20), (14, 26), (15, 1), (15, 17)] and FR_SAID == [(14, 11), (14, 20)], (FR, FR_SAID)
assert len(REG) == 35 and Counter(c for c, v in REG) == {13: 13, 14: 20, 15: 2} and len(REG[(13, 26)]) == 4 and sorted(k for k in REG if k[0] == 15) == [(15, 1), (15, 17)], (len(REG), Counter(c for c, v in REG))
assert by[('Num', 14, 1)][0] == ('ותשא', 'HC/Vqw3fs') and by[('Num', 14, 1)][3][1] == 'HC/Vqw3mp'   # the congregation LIFTED (singular), then THEY gave their voice (plural)
assert [(x, m) for x, m in by[('Num', 13, 22)] if m and m.startswith('HC/V')] == [('ויעלו', 'HC/Vqw3mp'), ('ויבא', 'HC/Vqw3ms')]   # THEY went up, HE came to Hebron — the number switch inside one verse
assert by[('Num', 13, 2)][0][1] == 'HVqv2ms' and by[('Num', 13, 2)][3][1] == 'HC/Vqi3mp'
# CHAPTER 13
assert phrase(['שלח', 'לך'], None) == ['1Chr 19:3', '2Sam 10:3', 'Num 13:2'] and phrase(['לך', 'לך'], None) == ['Gen 12:1']   # "send for yourself" — the Torah's one seat; David's two the homograph ("has he sent to you")
TUR = [(c, v, x) for (c, v) in SPAN for x in words('Num', c, v) if x in ('ויתרו', 'לתור', 'מתור', 'תרו', 'התרים', 'תרתם')]
assert [f'{c}:{v}' for c, v, _ in TUR] == ['13:2', '13:16', '13:17', '13:21', '13:25', '13:32', '13:32', '14:6', '14:7', '14:34', '14:36', '14:38'] and len(TUR) == 12, TUR   # the spy-verb twelve times in the two chapters; 'סתור' (13:13) and 'תורה' (15:16, 15:29) its homographs
assert hits('לתור', None, True) == ['Deut 1:33', 'Num 10:33', 'Num 13:16', 'Num 13:17', 'Num 13:32', 'Num 14:36', 'Num 14:38', 'Num 14:7'] and 'לראות' in words('Num', 32, 8) and 'לרגל' in words('Josh', 14, 7)   # the retellings change the verb: "to SEE" (32:8), "to SPY" (Josh 14:7)
def princes(c, lo, hi):
    out = []
    for v in range(lo, hi + 1):
        w = words('Num', c, v)
        for i, x in enumerate(w):
            if x == 'בן' and 0 < i < len(w) - 1 and w[i - 1] != 'אחד': out.append((w[i - 1], w[i + 1]))
    return out
SPIES = princes(13, 4, 15); TRIBES13 = [w[i + 1] for v in range(4, 16) for w in [words('Num', 13, v)] for i, x in enumerate(w) if x == 'למטה']
assert len(SPIES) == 12 and SPIES[2] == ('כלב', 'יפנה') and SPIES[4] == ('הושע', 'נון') and SPIES[9] == ('סתור', 'מיכאל'), SPIES
assert TRIBES13 == ['ראובן', 'שמעון', 'יהודה', 'יששכר', 'אפרים', 'בנימן', 'זבולן', 'יוסף', 'מנשה', 'דן', 'אשר', 'נפתלי', 'גד'] and len(TRIBES13) == 13, TRIBES13   # twelve tribes, thirteen "for the tribe of" — Joseph's name over Manasseh
CENSUS_ORDER = ['ראובן', 'שמעון', 'יהודה', 'יששכר', 'זבולן', 'אפרים', 'מנשה', 'בנימן', 'דן', 'אשר', 'גד', 'נפתלי']   # 1:5-15 (the tribe names after the prefixed "for" — 1b's list)
assert [t for t in TRIBES13 if t != 'יוסף'] != CENSUS_ORDER and [t for t in TRIBES13 if t != 'יוסף'][:4] == CENSUS_ORDER[:4]   # THE SPIES' ORDER IS A FOURTH ORDER — the first four tribes as the census, then Ephraim, Benjamin, Zebulun, Manasseh, Dan, Asher, Naphtali, Gad
assert phrase(['למטה', 'יוסף'], None) == ['Num 13:11'] and words('Num', 13, 11)[:4] == ['למטה', 'יוסף', 'למטה', 'מנשה'] and words('Num', 1, 10)[:3] == ['לבני', 'יוסף', 'לאפרים'] and words('Num', 1, 32)[:4] == ['לבני', 'יוסף', 'לבני', 'אפרים']   # Joseph's name over EPHRAIM in the census, over MANASSEH among the spies
assert hits('הושע', ('Num',), True) == ['Num 13:8'] and hits('להושע', T, True) == ['Num 13:16'] and 'והושע' in words('Deut', 32, 44) and words('Deut', 32, 44)[-3:] == ['והושע', 'בן', 'נון']   # Hoshea at 13:8, renamed at 13:16 — and HOSHEA AGAIN at the Torah's last song (Deut 32:44)
YEHOSHUA_BEFORE = sorted([s for s in hits('יהושע', T, True) + hits('ויהושע', T, True) if key(s) < ('Num', 13, 16) and key(s)[0] in ('Exod', 'Num')] + [s for s in hits('יהושע', T, True) + hits('ויהושע', T, True) if key(s)[0] == 'Exod'], key=key)
assert sorted(set(YEHOSHUA_BEFORE), key=key) == ['Exod 17:9', 'Exod 17:10', 'Exod 17:13', 'Exod 17:14', 'Exod 24:13', 'Exod 32:17', 'Exod 33:11', 'Num 11:28'], YEHOSHUA_BEFORE   # the NEW name at eight seats BEFORE the renaming verse
Q13 = [(v, x, m) for v in (18, 19, 20) for x, m in by[('Num', 13, v)] if m and m.startswith(('HTi', 'HC/Ti'))]
assert [x for _, x, _ in Q13] == ['מה', 'החזק', 'הרפה', 'המעט', 'ומה', 'הטובה', 'ומה', 'הבמחנים', 'ומה', 'השמנה', 'היש'] and sum(words('Num', 13, v).count('אם') for v in (18, 19, 20)) == 5   # THE QUESTIONNAIRE: four "what", seven interrogative he's, five "or"
assert phrase(['בכורי', 'ענבים'], None) == ['Num 13:20'] and phrase(['ימי', 'בכורי'], None) == ['Num 13:20']   # the season stamped in the ink
assert hits('צן', None, True) == ['Deut 32:51', 'Josh 15:1', 'Num 13:21', 'Num 20:1', 'Num 27:14', 'Num 33:36', 'Num 34:3'] and phrase(['לבא', 'חמת'], None) == ['Num 13:21', 'Num 34:8']   # the two ends of the border, 13:21 and the border chapter's 34:8
assert phrase(['עד', 'חברון'], None) == ['Num 13:22'] and hits('אחימן', None) == ['1Chr 9:17', 'Josh 15:14', 'Judg 1:10', 'Num 13:22'] and phrase(['ילידי', 'הענק'], None) == ['Josh 15:14', 'Num 13:22'] and phrase(['ילדי', 'הענק'], None) == ['Num 13:28'] and phrase(['בני', 'ענק'], None) == ['Deut 9:2', 'Num 13:33']   # "children of the Anak" plene at 13:22, DEFECTIVE at 13:28; Joshua 15:14 and Judges 1:10 run the three names
assert hits('צען', None, True) == ['Isa 19:11', 'Isa 19:13', 'Num 13:22', 'Ps 78:12', 'Ps 78:43'] and phrase(['שבע', 'שנים', 'נבנתה'], None) == ['Num 13:22'] and RIGHT[(13, 22)] == [7]
ESHKOL = {k: [x for x in words(*k) if 'אשכ' in x] for k in [('Num', 13, 23), ('Num', 13, 24), ('Deut', 1, 24), ('Num', 32, 9), ('Gen', 14, 13), ('Gen', 14, 24)]}
assert ESHKOL == {('Num', 13, 23): ['אשכל', 'ואשכול'], ('Num', 13, 24): ['אשכול', 'האשכול'], ('Deut', 1, 24): ['אשכל'], ('Num', 32, 9): ['אשכול'], ('Gen', 14, 13): ['אשכל'], ('Gen', 14, 24): ['אשכל']}, ESHKOL   # the wadi DEFECTIVE at 13:23, PLENE in the naming verse 13:24; Eshcol the man of Hebron (Gen 14:13, 14:24) spelled as the wadi's first seat
assert hits('זמורה', None, True) == ['Num 13:23'] and phrase(['במוט', 'בשנים'], None) == ['Num 13:23'] and hits('מוט', ('Num',)) == ['Num 13:23', 'Num 4:10', 'Num 4:12'] and RIGHT[(13, 23)] == [1, 2]   # the cluster's pole is the Kohathites' carrying-bar word; the dual "on two" READ by the parser (3b's rule at a fresh seat)
assert phrase(['על', 'אדות'], None) == ['Gen 21:25', 'Gen 26:32', 'Judg 6:7', 'Num 12:1', 'Num 13:24'] and phrase(['על', 'אודת'], None) == ['Exod 18:8', 'Gen 21:11'] and 'אדותי' in words('Josh', 14, 6)   # "concerning" — Miriam's chapter and the spies' both; Caleb's own "concerning me" at Joshua 14:6
assert phrase(['מקץ', 'ארבעים', 'יום'], None) == ['Deut 9:11', 'Gen 8:6', 'Num 13:25'] and len(phrase(['ארבעים', 'יום'], None)) == 17   # "at the end of forty days" — Noah's window, the tablets, the spies
assert hits('קדשה', None, True) == ['Deut 23:18', 'Gen 38:21', 'Gen 38:22', 'Judg 11:16', 'Judg 4:10', 'Judg 4:9', 'Num 13:26'] and 'ברנע' in words('Deut', 1, 19) and 'ברנע' in words('Num', 32, 8) and 'ברנע' in words('Josh', 14, 7)   # "to Kadesh" (the directional he — a homograph of the harlot-word and of Kedesh); the retellings say Kadesh-BARNEA
assert phrase(['וישיבו', 'אותם', 'דבר'], None) == ['Num 13:26'] and phrase(['וישבו', 'אתנו', 'דבר'], None) == ['Deut 1:22', 'Deut 1:25'] and hits('ויראום', None, True) == ['Num 13:26']
ZAVAT = phrase(['זבת', 'חלב', 'ודבש'], None); assert len(ZAVAT) == 20 and [s for s in ZAVAT if s.startswith('Num')] == ['Num 13:27', 'Num 14:8', 'Num 16:13', 'Num 16:14'] and len([s for s in ZAVAT if key(s)[0] in T]) == 15   # the spies say it of Canaan, Dathan of EGYPT (16:13)
assert phrase(['אפס', 'כי'], None) == ['2Sam 12:14', 'Amos 9:8', 'Deut 15:4', 'Judg 4:9', 'Num 13:28'] and 'בצרות' in words('Num', 13, 28) and 'ובצורת' in words('Deut', 1, 28) and 'בשמים' in words('Deut', 1, 28)   # Deuteronomy's retelling adds "to heaven"
assert phrase(['עמלק', 'יושב'], None) == ['Num 13:29'] and phrase(['העמלקי', 'והכנעני'], None) == ['Num 14:43', 'Num 14:45'] and words('Num', 14, 25)[:4] == ['והעמלקי', 'והכנעני', 'יושב', 'בעמק'] and 'בהר' in words('Num', 13, 29) and 'הנגב' in words('Num', 13, 29)   # 13:29 seats Amalek in the SOUTH and the Canaanite by the sea; 14:25 seats both in the VALLEY, 14:45 in the MOUNTAIN
assert hits('ויהס', None, True) == ['Num 13:30'] and phrase(['עלה', 'נעלה'], None) == ['Num 13:30'] and phrase(['יכול', 'נוכל'], None) == ['Num 13:30']   # "hushed" once in the Bible; two doubled infinitives in one verse
assert phrase(['חזק', 'הוא', 'ממנו'], None) == ['Num 13:31'] and sg(13, 31, 'ממנו') == 'from-us/our' and aramaic(13, 31)[-1] == 'מננא'   # "than WE" — the store's gloss and the translation agree; the exam reads "than He" (Sotah 35a)
DIBBAH = sorted(set(hits('דבת', None, True) + hits('דבה', None, True) + hits('דבתם', None, True))); assert DIBBAH == ['Gen 37:2', 'Jer 20:10', 'Num 13:32', 'Num 14:36', 'Num 14:37', 'Prov 10:18', 'Ps 31:14'] and hits('ודבת', None, True) == ['Ezek 36:3'] and phrase(['דבת', 'הארץ', 'רעה'], None) == ['Num 14:37'] and words('Gen', 37, 2)[-4:-1] == ['דבתם', 'רעה', 'אל']   # the evil report: Joseph's (Gen 37:2) and the spies' — the Torah's only two
assert phrase(['ארץ', 'אכלת', 'יושביה'], None) == ['Num 13:32'] and phrase(['אכלת', 'אדם'], None) == ['Ezek 36:13'] and phrase(['אנשי', 'מדות'], None) == ['Num 13:32'] and phrase(['אנשי', 'מדה'], None) == ['Isa 45:14']
assert [x for x in words('Num', 13, 33) if 'נפ' in x] == ['הנפילים', 'הנפלים'] and [x for x in words('Gen', 6, 4) if 'נפ' in x] == ['הנפלים'] and hits('כחגבים', None, True) == ['Isa 40:22', 'Num 13:33']   # the Nephilim PLENE then DEFECTIVE in one verse; Genesis 6:4 defective; "as grasshoppers" with Isaiah 40:22
# CHAPTER 14
assert phrase(['ויבכו', 'העם'], None) == ['Num 14:1'] and len(phrase(['בלילה', 'ההוא'], None)) == 16 and 'Num 14:1' in phrase(['בלילה', 'ההוא'], None)   # "that night" — the shelf's ninth of Av (Taanit 29a:5), the tape's next marker
LUN = sorted({f'{b} {c}:{v}' for (b, c, v), ws in by.items() if b in ('Exod', 'Num') for x, _ in ws if x in ('וילנו', 'וילונו', 'וילינו', 'ותלנו', 'תלינו', 'ילינו', 'מלינים', 'הלינתם', 'תלנות', 'תלנתם', 'תלנת', 'תלונות', 'מלינם', 'ותלן', 'וילן', 'המלינים', 'תלנתיכם', 'תלנותיכם', 'תלנתו')}, key=key)
assert LUN == ['Exod 15:24', 'Exod 16:2', 'Exod 16:7', 'Exod 16:8', 'Exod 16:9', 'Exod 17:3', 'Num 14:2', 'Num 14:27', 'Num 14:29', 'Num 14:36', 'Num 17:6', 'Num 17:20'] and words('Num', 14, 27).count('מלינים') == 2, LUN   # the murmur-root's twelve seats: Marah, the manna, Rephidim, the spies, Korach
assert nphrase(['לו', 'מתנו'], 'Num', 14, 2) == 2 and phrase(['לו', 'מתנו'], None) == ['Num 14:2'] and phrase(['מי', 'יתן', 'מותנו'], None) == ['Exod 16:3'] and phrase(['ולו', 'גוענו'], None) == ['Num 20:3']   # the three death-wishes
LAVAZ = hits('לבז', None, True); assert len(LAVAZ) == 17 and 'Num 14:3' in LAVAZ and 'Num 14:31' in LAVAZ and phrase(['וטפכם', 'אשר', 'אמרתם', 'לבז', 'יהיה'], None) == ['Deut 1:39', 'Num 14:31']   # the people's word returned to them at 14:31, verbatim at Deuteronomy 1:39
assert phrase(['נתנה', 'ראש'], None) == ['Num 14:4'] and phrase(['ויתנו', 'ראש'], None) == ['Neh 9:17'] and phrase(['ונשובה', 'מצרימה'], None) == ['Num 14:4'] and phrase(['שוב', 'מצרימה'], None) == ['Num 14:3']   # Nehemiah 9:17 quotes the head
assert phrase(['ויפל', 'משה', 'ואהרן', 'על', 'פניהם'], None) == ['Num 14:5'] and phrase(['ויפלו', 'על', 'פניהם'], None) == ['1Kgs 18:39', 'Judg 13:20', 'Lev 9:24', 'Num 16:22', 'Num 17:10', 'Num 20:6']   # the two on their faces: singular verb here, plural at Korach, the plague, Meribah
assert phrase(['קרעו', 'בגדיהם'], None) == ['Num 14:6'] and phrase(['מאד', 'מאד'], None) == ['1Kgs 7:47', '2Kgs 10:4', 'Ezek 37:10', 'Gen 30:43', 'Gen 7:19', 'Num 14:7']
assert phrase(['אם', 'חפץ', 'בנו'], None) == ['Num 14:8'] and phrase(['לחמנו', 'הם'], None) == ['Num 14:9'] and phrase(['סר', 'צלם'], None) == ['Num 14:9'] and hits('תיראם', None, True) == ['Num 14:9']
assert hits('לרגום', None, True) == ['Num 14:10'] and phrase(['אתם', 'באבנים'], None) == ['Deut 22:24', 'Josh 7:25', 'Num 14:10']
GLORY = sorted(set(phrase(['וכבוד', 'יהוה', 'נראה'], None) + phrase(['כבוד', 'יהוה', 'נראה'], None) + phrase(['וירא', 'כבוד', 'יהוה'], None) + phrase(['כבוד', 'יהוה', 'אל', 'כל'], None)), key=key)
assert GLORY == ['Exod 16:10', 'Lev 9:23', 'Num 14:10', 'Num 16:19', 'Num 17:7', 'Num 20:6'], GLORY   # the glory APPEARING: the manna, the eighth day, the spies, Korach, the plague, Meribah — four in Numbers
assert nphrase(['עד', 'אנה'], 'Num', 14, 11) == 1 and nphrase(['ועד', 'אנה'], 'Num', 14, 11) == 1 and 'Exod 16:28' in phrase(['עד', 'אנה'], None)   # "how long" twice, the manna's 16:28 the Torah's other
NAATZ = sorted(set(hits('ינאצני', None, True) + hits('מנאצי', None, True) + hits('נאצו', None, True) + hits('נאצת', None, True) + hits('ינאצו', None, True) + hits('נאצתם', None, True)))
assert [s for s in NAATZ if key(s)[0] in T] == ['Num 14:11', 'Num 14:23', 'Num 16:30'] and phrase(['יאמינו', 'בי'], None) == ['Num 14:11']   # the scorn-verb is NUMBERS' word in the Torah (Korach's 16:30 the third)
BELIEVED = sorted(set(phrase(['והאמן', 'ביהוה'], T) + phrase(['ויאמינו', 'ביהוה'], T) + phrase(['האמנתם', 'בי'], T) + phrase(['מאמינם', 'ביהוה'], T))); assert BELIEVED == ['Deut 1:32', 'Exod 14:31', 'Gen 15:6', 'Num 20:12']   # Abraham believed, Israel at the sea believed; here not; Moses at Meribah not; Deut 1:32 the retelling
assert phrase(['ואעשה', 'אותך', 'לגוי', 'גדול'], None) == ['Exod 32:10'] and phrase(['ואעשה', 'אתך', 'לגוי', 'גדול'], None) == ['Num 14:12'] and words('Num', 14, 12)[-3:] == ['גדול', 'ועצום', 'ממנו'] and words('Deut', 9, 14)[-4:] == ['לגוי', 'עצום', 'ורב', 'ממנו']   # THE OFFER'S SECOND SEAT: 'you' spelled plene at the calf, defective here; "and mightier than they" added; Deut 9:14 a third form
assert phrase(['ושמעו', 'מצרים'], None) == ['Num 14:13'] and phrase(['למה', 'יאמרו', 'מצרים'], None) == ['Exod 32:12'] and phrase(['עין', 'בעין'], None) == ['Deut 19:21', 'Isa 52:8', 'Num 14:14'] and len(phrase(['כאיש', 'אחד'], None)) == 9 and RIGHT[(14, 15)] == [1]   # Moses' Egypt argument at both intercessions; "eye to eye" the homograph of "eye for eye"
assert phrase(['מבלתי', 'יכלת'], None) == ['Num 14:16'] and phrase(['מבלי', 'יכלת'], None) == ['Deut 9:28'] and hits('יכלת', None, True) == ['Dan 2:47', 'Deut 9:28', 'Num 14:16']   # the noun's two Hebrew seats — Deuteronomy's retelling drops the tav of "from lack of"
assert phrase(['יגדל', 'נא'], None) == ['Num 14:17'] and phrase(['כח', 'אדני'], None) == ['Num 14:17']
E34 = words('Exod', 34, 6) + words('Exod', 34, 7); N18 = words('Num', 14, 18)
assert [x for x in N18 if x not in E34] == [] and [x for x in E34 if x not in N18] == ['ויעבר', 'פניו', 'ויקרא', 'אל', 'רחום', 'וחנון', 'ואמת', 'נצר', 'לאלפים', 'וחטאה', 'בני'] and len(N18) == 20 and len(E34) == 37   # THE ATTRIBUTES ABRIDGED: every word of 14:18 stands in Exod 34:6-7; nothing added; dropped — the frame, "God merciful and gracious", "and truth", "keeping mercy for thousands", "and sin", "and upon the children's children"
def subseq(a, b):
    i = 0
    for x in b:
        if i < len(a) and x == a[i]: i += 1
    return i == len(a)
assert subseq(N18, E34)   # and in ORDER — a pure deletion
assert 'ולחובין' in aramaic(14, 18) and '(וקשוט)' in aramaic(14, 18) and 'בני' not in aramaic(14, 18) and aramaic(14, 18)[7:10] == ['שבק', 'לעוין', 'ולמרוד'] and 'לדתיבין' in aramaic(14, 18) and 'מרדין' in aramaic(14, 18)   # THE TRANSLATION RESTORES the dropped third noun ("and sins") and, in a bracketed variant, "and truth" — but not the children's children; the repentance fork and "rebellious" inserted
ONK_EX34 = [plain(x) for x in clean(json.load(open(f'{ROOT}/Data/sefaria_export/Onkelos_Exodus/he.json'))['text'][33][6]).rstrip(':').split()]
assert ONK_EX34[4:7] == ['שבק', 'לעוין', 'ולמרוד'] and 'ולחובין' in ONK_EX34 and 'בני' in ONK_EX34 and 'לדתיבין' in ONK_EX34   # Onkelos Exod 34:7 the source of the harmonization
assert phrase(['סלח', 'נא'], None) == ['Amos 7:2', 'Num 14:19'] and hits('סלחתי', None, True) == ['Num 14:20'] and phrase(['וכאשר', 'נשאתה'], None) == ['Num 14:19']   # "I have forgiven" — the word's one seat
assert phrase(['חי', 'אני'], T) == ['Num 14:21', 'Num 14:28'] and len(phrase(['חי', 'אני'], None)) == 22 and phrase(['חי', 'אנכי'], None) == ['Deut 32:40'] and phrase(['נאם', 'יהוה'], T) == ['Gen 22:16', 'Num 14:28'] and hits('נאם', T, True) == ['Gen 22:16', 'Num 14:28', 'Num 24:15', 'Num 24:16', 'Num 24:3', 'Num 24:4']   # "as I live" the Torah's two, both here; "says the LORD" — the Akedah's oath and this one, the Torah's only two (Balaam's four "says Balaam")
assert phrase(['וימלא', 'כבוד', 'יהוה'], None) == ['Num 14:21'] and phrase(['מלא', 'כל', 'הארץ', 'כבודו'], None) == ['Isa 6:3']
assert phrase(['זה', 'עשר', 'פעמים'], None) == ['Job 19:3', 'Num 14:22'] and phrase(['עשרת', 'מנים'], None) == ['Gen 31:41', 'Gen 31:7'] and phrase(['ולא', 'שמעו', 'בקולי'], None) == ['Jer 9:12', 'Num 14:22'] and RIGHT[(14, 22)] == [10]   # "these ten times" — Job's phrase; Laban's ten a different noun
assert phrase(['אם', 'יראו'], None) == ['Num 14:23', 'Num 32:11'] and phrase(['נשבעתי', 'לאבתם'], None) == ['Deut 10:11', 'Num 14:23'] and hits('מנאצי', None, True) == ['Num 14:23']   # the oath restated by Moses to Gad and Reuben (32:11)
assert 'Num 14:24' in hits('ועבדי', None, True) and phrase(['רוח', 'אחרת'], None) == ['Num 14:24'] and phrase(['וזרעו', 'יורשנה'], None) == ['Num 14:24']
MALE = sorted(set(phrase(['וימלא', 'אחרי'], None) + phrase(['מלאו', 'אחרי'], None) + phrase(['מלא', 'אחרי'], None) + phrase(['מלאת', 'אחרי'], None) + phrase(['מלאתי', 'אחרי'], None))); assert MALE == ['1Kgs 11:6', 'Deut 1:36', 'Josh 14:14', 'Josh 14:8', 'Josh 14:9', 'Num 14:24', 'Num 32:11', 'Num 32:12'], MALE   # "followed fully" — Caleb's formula at seven seats; its negation at Solomon (1 Kgs 11:6)
assert 'עקב' in words('Num', 14, 24) and 'עקב' in words('Gen', 22, 18) and 'עקב' in words('Gen', 26, 5)   # "because" — Abraham's reward word (Gen 22:18, 26:5) on Caleb
assert words('Num', 14, 25)[5:] == ['פנו', 'וסעו', 'לכם', 'המדבר', 'דרך', 'ים', 'סוף'] and words('Deut', 1, 40)[1:] == ['פנו', 'לכם', 'וסעו', 'המדברה', 'דרך', 'ים', 'סוף'] and hits('מחר', ('Num',), True) == ['Num 14:25', 'Num 16:16', 'Num 16:7', 'Num 33:33']   # the retelling REORDERS "turn and journey" and adds the directional he; "tomorrow" — Korach's word twice
assert sorted(set(phrase(['לעדה', 'הרעה', 'הזאת'], None) + phrase(['העדה', 'הרעה', 'הזאת'], None))) == ['Num 14:27', 'Num 14:35'] and phrase(['עד', 'מתי'], T) == ['Exod 10:3', 'Exod 10:7', 'Num 14:27'] and hits('מלינים', None, True) == ['Num 14:27']   # "this evil congregation" — the ten's seat (Sanhedrin 1:6); "how long" — Pharaoh's two and this
assert phrase(['חי', 'אני', 'נאם', 'יהוה'], None) == ['Isa 49:18', 'Jer 22:24', 'Num 14:28', 'Zeph 2:9'] and phrase(['אם', 'לא', 'כאשר', 'דברתם'], None) == ['Num 14:28']
assert phrase(['במדבר', 'הזה'], None) == ['Num 14:2', 'Num 14:29', 'Num 14:32', 'Num 14:35'] and phrase(['יפלו', 'פגריכם'], None) == ['Num 14:29'] and hits('פגריכם', None, True) == ['Lev 26:30', 'Num 14:29', 'Num 14:33'] and hits('ופגריכם', None, True) == ['Num 14:32']   # "in THIS wilderness" — the people's word (14:2) returned three times; the carcass-word's Torah seats: Lev 26:30's curse and this chapter's three
ESRIM = phrase(['מבן', 'עשרים', 'שנה', 'ומעלה'], None); assert len(ESRIM) == 23 and [s for s in ESRIM if s.startswith('Num') and not s.startswith('Num 1:')] == ['Num 14:29', 'Num 26:2', 'Num 26:4', 'Num 32:11'] and len([s for s in ESRIM if s.startswith('Num 1:')]) == 15 and RIGHT[(14, 29)] == [20]   # the decree bound to the census's own threshold; "your numbered", "your number" one seat each
assert hits('פקדיכם', None, True) == ['Num 14:29'] and phrase(['לכל', 'מספרכם'], None) == ['Num 14:29']
assert phrase(['נשאתי', 'את', 'ידי'], None) == ['Exod 6:8', 'Ezek 20:23', 'Ezek 20:28', 'Ezek 20:42', 'Ezek 36:7', 'Ezek 47:14', 'Num 14:30'] and words('Ps', 106, 26) == ['וישא', 'ידו', 'להם', 'להפיל', 'אותם', 'במדבר'] and words('Ps', 106, 24)[:3] == ['וימאסו', 'בארץ', 'חמדה'] and 'האמינו' in words('Ps', 106, 24)   # the raised-hand oath: Exod 6:8's promise, this decree, Ezekiel's six; Psalm 106:24-26 quotes 14:11's faith, 14:31's despising and 14:30's hand
KJ = [(c, v, [x for x in words('Num', c, v) if x in ('כלב', 'וכלב', 'יהושע', 'ויהושע')]) for (c, v) in SPAN if any(x in ('כלב', 'וכלב', 'יהושע', 'ויהושע') for x in words('Num', c, v))]
assert KJ == [(13, 6, ['כלב']), (13, 16, ['יהושע']), (13, 30, ['כלב']), (14, 6, ['ויהושע', 'וכלב']), (14, 24, ['כלב']), (14, 30, ['כלב', 'ויהושע']), (14, 38, ['ויהושע', 'וכלב'])], KJ   # the narrator names Joshua first (14:6, 14:38); the LORD names CALEB first (14:30); 14:24 Caleb alone — Deut 1:36 too
assert words('Deut', 1, 36)[:4] == ['זולתי', 'כלב', 'בן', 'יפנה'] and phrase(['מאסתם', 'בה'], None) == ['Num 14:31'] and phrase(['וידעו', 'את', 'הארץ'], None) == ['Num 14:31']
assert phrase(['רעים', 'במדבר'], None) == ['Num 14:33'] and hits('זנותיכם', None, True) == ['Num 14:33'] and len(phrase(['ארבעים', 'שנה'], None)) == 31 and phrase(['עד', 'תם'], ('Num', 'Deut')) == ['Deut 2:14', 'Num 14:33', 'Num 32:13'] and EXTRA['Deut 2:14'] == [38] and words('Deut', 2, 14)[11:14] == ['שלשים', 'ושמנה', 'שנה']   # forty years here; THIRTY-EIGHT at Deut 2:14 "until all the generation was consumed" — the ink's own subtraction of the two years already passed
assert phrase(['יום', 'לשנה', 'יום', 'לשנה'], None) == ['Ezek 4:6', 'Num 14:34'] and words('Ezek', 4, 6)[13:20] == ['ארבעים', 'יום', 'יום', 'לשנה', 'יום', 'לשנה', 'נתתיו'] and RIGHT[(14, 34)] == [40, 40]   # A DAY FOR A YEAR, A DAY FOR A YEAR — Ezekiel 4:6 runs the rule verbatim, forty days for Judah's iniquity
assert hits('תנואתי', None, True) == ['Num 14:34'] and sorted(set(hits('הניא', None, True) + hits('יניא', None, True) + hits('תנואון', None, True) + hits('ויניאו', None, True))) == ['Num 30:12', 'Num 30:6', 'Num 30:9', 'Num 32:7', 'Num 32:9', 'Ps 33:10']   # "My alienation" — the root of the vow-annulment (30:6-12) and of the spies' retelling to Gad and Reuben (32:7, 32:9)
ANI_DIBARTI = phrase(['אני', 'יהוה', 'דברתי'], None); assert ANI_DIBARTI[-1] == 'Num 14:35' and len(ANI_DIBARTI) == 15 and all(s.startswith('Ezek') for s in ANI_DIBARTI[:-1])   # "I the LORD have spoken" — this verse and fourteen of Ezekiel's
assert phrase(['הנועדים', 'עלי'], None) + phrase(['הנעדים', 'על'], None) == ['Num 14:35', 'Num 16:11'] and phrase(['יתמו', 'ושם', 'ימתו'], None) == ['Num 14:35']   # "gathered against Me" — this and Korach's
assert hits('במגפה', None, True) == ['Ezek 24:16', 'Num 14:37', 'Num 17:14', 'Num 25:9'] and words('Num', 14, 37) == ['וימתו', 'האנשים', 'מוצאי', 'דבת', 'הארץ', 'רעה', 'במגפה', 'לפני', 'יהוה']   # "in the plague" — the ten spies, Korach's 14,700, Peor's 24,000
assert phrase(['חיו', 'מן'], None) == ['Num 14:38'] and [s for s in hits('ויתאבלו', None, True) + hits('ויתאבל', None, True) if key(s)[0] in T] == ['Exod 33:4', 'Num 14:39', 'Gen 37:34']   # the mourning verb's Torah seats: Jacob for Joseph, the calf's ornaments, the decree
assert phrase(['וישכמו', 'בבקר'], T) == ['Num 14:40'] and phrase(['הננו', 'ועלינו'], None) == ['Num 14:40'] and hits('חטאנו', T, True) == ['Deut 1:41', 'Num 12:11', 'Num 14:40', 'Num 21:7']   # the PLURAL early-rising once in the Torah; "we have sinned" — Aaron's, the people's here and at the serpents, the retelling
assert phrase(['עברים', 'את', 'פי', 'יהוה'], None) == ['Num 14:41'] and phrase(['לעבר', 'את', 'פי', 'יהוה'], None) == ['Num 22:18', 'Num 24:13'] and phrase(['לא', 'תצלח'], None) == ['Num 14:41']   # "transgress the mouth of the LORD" — Balaam's formula twice
assert phrase(['אל', 'תעלו'], None) == ['Num 14:42'] and phrase(['אין', 'יהוה', 'בקרבכם'], None) == ['Num 14:42'] and hits('תנגפו', None, True) == ['Deut 1:42', 'Num 14:42'] and words('Deut', 1, 42)[5:] == ['לא', 'תעלו', 'ולא', 'תלחמו', 'כי', 'אינני', 'בקרבכם', 'ולא', 'תנגפו', 'לפני', 'איביכם']   # the retelling: "I am not among you" for "the LORD is not among you"
assert phrase(['שבתם', 'מאחרי', 'יהוה'], None) == ['Num 14:43'] and words('Num', 32, 15)[:3] == ['כי', 'תשובן', 'מאחריו'] and phrase(['ולא', 'יהיה', 'יהוה', 'עמכם'], None) == ['Num 14:43']
assert hits('ויעפלו', None, True) == ['Num 14:44'] and words('Deut', 1, 43)[-3:] == ['ותזדו', 'ותעלו', 'ההרה'] and 'עפלה' in words('Hab', 2, 4)   # the presumption-verb's one Torah seat; Deuteronomy's retelling says "you acted willfully"; Habakkuk's "puffed up"
assert phrase(['לא', 'משו'], None) == ['Num 14:44'] and [s for s in sorted(set(hits('ימיש', None, True) + hits('משו', None, True))) if key(s)[0] in T] == ['Exod 13:22', 'Exod 33:11', 'Num 14:44']   # "did not depart" — the pillar (Exod 13:22), Joshua from the tent (33:11), the ark and Moses from the camp
assert phrase(['ארון', 'ברית', 'יהוה'], T) + phrase(['וארון', 'ברית', 'יהוה'], T) == ['Deut 10:8', 'Deut 31:25', 'Deut 31:26', 'Deut 31:9', 'Num 10:33', 'Num 14:44']   # "the ark of the covenant of the LORD" — six Torah seats, 10:33 and 14:44 in Numbers
assert sorted(set(hits('חרמה', None, True) + hits('החרמה', None, True))) == ['Deut 1:44', 'Josh 12:14', 'Judg 1:17', 'Num 14:45', 'Num 21:3'] and words('Num', 21, 3)[-4:] == ['ויקרא', 'שם', 'המקום', 'חרמה'] and phrase(['ויכום', 'ויכתום'], None) == ['Num 14:45'] and 'הדברים' in words('Deut', 1, 44) and 'בשעיר' in words('Deut', 1, 44)   # HORMAH NAMED AT 21:3, USED AT 14:45 — the name before its naming; Judges 1:17 names it again; the retelling adds the bees and Seir
assert words('Deut', 1, 22)[:6] == ['ותקרבון', 'אלי', 'כלכם', 'ותאמרו', 'נשלחה', 'אנשים'] and EXTRA['Deut 1:23'] == [12, 1] and not any(12 in N('Num', 13, v) for v in range(1, 34))   # the retelling: the people's initiative, and TWELVE written — a number chapter 13 never writes (the count is the list)
assert words('Deut', 1, 45)[:4] == ['ותשבו', 'ותבכו', 'לפני', 'יהוה'] and 'ותרגנו' in words('Deut', 1, 27) and 'וירגנו' in words('Ps', 106, 25)   # "you wept before the LORD" — the second weeping, after Hormah; "you murmured in your tents" — Psalm 106:25's verb
assert EXTRA['Josh 14:7'] == [40] and EXTRA['Josh 14:10'] == [45, 85] and 'ברנע' in words('Josh', 14, 7) and words('Josh', 14, 9)[-5:] == ['כי', 'מלאת', 'אחרי', 'יהוה', 'אלהי'] and 'וישבע' in words('Josh', 14, 9)   # CALEB'S OWN ARITHMETIC: forty at the sending, forty-five years since, eighty-five now (Josh 14:7, 14:10) — and Moses' OATH to him (14:9), unwritten here
# CHAPTER 15
assert phrase(['כי', 'תבאו', 'אל', 'ארץ', 'מושבתיכם'], None) == ['Num 15:2'] and hits('מושבתיכם', None, True) == ['Exod 12:20', 'Lev 23:21', 'Lev 23:3', 'Lev 3:17', 'Lev 7:26', 'Num 15:2', 'Num 35:29'] and phrase(['כי', 'תבאו', 'אל', 'הארץ'], None) == ['Exod 12:25', 'Lev 23:10', 'Lev 25:2']   # "your settlings" — seven seats, the Sabbath's Lev 23:3 among them (R. Akiva's objection on the ink)
assert phrase(['בבאכם', 'אל', 'הארץ'], None) == ['Num 15:18'] and hits('בבאכם', None, True) == ['Jer 42:18', 'Lev 10:9', 'Num 15:18'] and phrase(['והיה', 'כי', 'יביאך', 'יהוה'], None) == ['Deut 11:29', 'Deut 6:10', 'Exod 13:5'] and 'תבא' in words('Deut', 17, 14)   # R. YISHMAEL'S VARIED FORMULA MEASURED: "upon your coming to the land" ONE seat against the "when you come" / "when He brings you" formulas
assert phrase(['לפלא', 'נדר'], None) == ['Lev 22:21', 'Num 15:3', 'Num 15:8'] and phrase(['מן', 'הבקר', 'או', 'מן', 'הצאן'], None) == ['Num 15:3'] and phrase(['מן', 'הבקר', 'ומן', 'הצאן'], None) == ['Lev 1:2'] and hits('במעדיכם', None, True) == ['Num 15:3'] and hits('במועדיכם', None, True) == ['Num 29:39']   # OR here, AND at Leviticus 1:2 — the Sifrei's "either one by itself" is the conjunction's delta
assert [v for v in range(1, 32) if 'ניחח' in words('Num', 15, v)] == [3, 7, 10, 13, 14, 24] and [s for s in phrase(['אשה', 'ריח', 'ניחח'], None) if s.startswith('Num 15')] == ['Num 15:10', 'Num 15:13', 'Num 15:14']
FRAC = {}
for (b, c, v), ws in by.items():
    for x, _ in ws:
        if x in ('רבע', 'רבעית', 'רביעת', 'רביעית', 'ברבעית', 'ורביעת', 'שלשית', 'שלישית', 'ושלישת', 'חצי', 'עשרון', 'עשרנים', 'ההין'): FRAC.setdefault(x, []).append(f'{b} {c}:{v}')
FRAC = {k: sorted(set(v), key=key) for k, v in FRAC.items()}
assert FRAC['ההין'] == ['Exod 29:40', 'Ezek 4:11', 'Ezek 46:14', 'Lev 23:13', 'Num 15:4', 'Num 15:5', 'Num 15:6', 'Num 15:7', 'Num 15:9', 'Num 15:10', 'Num 28:5', 'Num 28:7', 'Num 28:14'], FRAC['ההין']   # "the hin" thirteen seats — six in this chapter
QUARTER = {k: [s for s in FRAC[k] if key(s)[0] in T] for k in ('רבע', 'רבעית', 'רביעת', 'ברבעית', 'רביעית', 'ורביעת')}
assert QUARTER == {'רבע': ['Exod 29:40', 'Num 23:10', 'Num 31:8'], 'רבעית': ['Exod 29:40'], 'רביעת': ['Lev 23:13', 'Num 28:5', 'Num 28:7'], 'ברבעית': ['Num 15:4'], 'רביעית': ['Num 15:5'], 'ורביעת': ['Num 28:14']}, QUARTER   # THE QUARTER SPELLED SIX WAYS across the Torah's libation seats (23:10's "fourth part of Israel" and 31:8's king Reba the homographs)
assert {k: FRAC[k] for k in ('שלשית', 'שלישית', 'ושלישת')} == {'שלשית': ['Ezek 5:2', 'Neh 10:33', 'Num 15:6', 'Num 15:7'], 'שלישית': ['Ezek 46:14'], 'ושלישת': ['Num 28:14']} and 'Num 15:9' in FRAC['חצי'] and 'Num 15:10' in FRAC['חצי'] and 'Num 28:14' in FRAC['חצי'] and 'Num 12:12' in FRAC['חצי']   # the third two ways; "half" — Miriam's "half his flesh" the chapter before
assert FRAC['עשרון'] == ['Num 15:4', 'Num 28:13', 'Num 28:21', 'Num 28:29', 'Num 29:10', 'Num 29:15'] and len(FRAC['עשרנים']) == 13 and GAPS[(15, 4)] == [] and RIGHT[(15, 6)] == [2] and RIGHT[(15, 9)] == [3]   # the unit noun "a tenth" silent, "two tenths" and "three tenths" read — the singular unit noun as one, 3b's named residue, six seats
assert words('Exod', 29, 40)[:7] == ['ועשרן', 'סלת', 'בלול', 'בשמן', 'כתית', 'רבע', 'ההין'] and words('Exod', 29, 40)[-2:] == ['לכבש', 'האחד'] and EXTRA['Exod 29:40'] == [] and words('Lev', 23, 13)[1:3] == ['שני', 'עשרנים'] and words('Lev', 23, 13)[-2:] == ['רביעת', 'ההין']   # the daily lamb's table (Exod 29:40) = this chapter's lamb; the omer's lamb two tenths with a single quarter (Lev 23:13 — the Sifrei's datum)
assert phrase(['לכבש', 'האחד'], None) == ['Exod 29:40', 'Num 15:5', 'Num 28:13', 'Num 28:21', 'Num 28:29', 'Num 28:7', 'Num 29:10', 'Num 29:15', 'Num 29:4'] and phrase(['לשור', 'האחד'], None) == ['Num 15:11'] and len(phrase(['לאיל', 'האחד'], None)) == 5 and GAPS[(15, 11)] == [] and GAPS[(15, 5)] == []   # "the ONE lamb / ox / ram" — the definite one the parser does not read (a class, nine seats for the lamb alone)
assert phrase(['כמספר', 'אשר', 'תעשו'], None) == ['Num 15:12'] and hits('כמספרם', None, True) == ['Num 15:12'] and [v for v in range(1, 32) if 'ככה' in words('Num', 15, v)] == [11, 12, 13] and phrase(['ככה', 'תעשו'], None) == ['Num 15:12']
assert phrase(['כל', 'האזרח'], None) == ['Lev 23:42', 'Num 15:13'] and hits('האזרח', None, True) == ['Lev 16:29', 'Lev 18:26', 'Lev 23:42', 'Num 15:13', 'Num 15:29', 'Num 15:30'] and 'ולאזרח' in words('Num', 9, 14)   # "all the native-born" — the sukkah's Lev 23:42 and this: the Sifrei's pair on the ink; THE ARTICLE-FORM at six seats in the Bible, three in this chapter (9:14's has the prefix)
GER = {'torah_achat': phrase(['תורה', 'אחת'], None), 'chukah_achat': phrase(['חקה', 'אחת'], None), 'mishpat_echad': phrase(['משפט', 'אחד'], None), 'kakhem_kager': phrase(['ככם', 'כגר'], None), 'lakhem_velager': phrase(['לכם', 'ולגר', 'הגר'], None)}
assert GER == {'torah_achat': ['Exod 12:49', 'Lev 7:7', 'Num 15:16', 'Num 15:29'], 'chukah_achat': ['Num 15:15', 'Num 9:14'], 'mishpat_echad': ['Lev 24:22'], 'kakhem_kager': ['Num 15:15'], 'lakhem_velager': ['Num 15:15', 'Num 15:16']}, GER   # THE ONE-LAW FORMULAS: "one Torah" (Exod 12:49; Lev 7:7's is the guilt-offering's; 15:16, 15:29), "one statute" (9:14, 15:15), "one judgment" (Lev 24:22) — three of the stranger's six seats in this chapter
assert RIGHT[(15, 15)] == [1] and RIGHT[(15, 16)] == [1, 1] and RIGHT[(15, 29)] == [1] and sorted(set(phrase(['וכי', 'יגור', 'אתכם', 'גר'], None) + phrase(['וכי', 'יגור', 'אתך', 'גר'], None) + phrase(['כי', 'יגור', 'אתך', 'גר'], None))) == ['Exod 12:48', 'Lev 19:33', 'Num 15:14', 'Num 9:14']
assert phrase(['מלחם', 'הארץ'], None) == ['Num 15:19'] and [x for x in words('Num', 15, 20) if 'ערס' in x] == ['ערסתכם'] and [x for x in words('Num', 15, 21) if 'ערס' in x] == ['ערסתיכם'] and 'ערסותיכם' in words('Ezek', 44, 30) and 'עריסתינו' in words('Neh', 10, 38)   # THE DOUGH-WORD FOUR TIMES IN THE BIBLE, FOUR SPELLINGS — the two adjacent verses differ by a yod
CHALLAH_T = [s for s in hits('חלה', None, True) if key(s)[0] in T]; assert CHALLAH_T == ['Deut 29:21', 'Gen 48:1', 'Num 15:20'] and [v for v in range(1, 32) if 'חלה' in words('Num', 15, v)] == [20] and 'וחלת' in words('Exod', 29, 23) and 'חלת' in words('Lev', 8, 26) and 'חלות' in words('Lev', 2, 4) and 'החלה' in words('Lev', 24, 5)   # THE BARE WORD "challah" at three Torah seats — "fell sick" at two (Gen 48:1, Deut 29:21) and the DOUGH-OFFERING'S NAME here: the loaves elsewhere are construct or plural forms
assert phrase(['כתרומת', 'גרן'], None) == ['Num 15:20'] and [v for v in range(1, 33) if any('גרן' in x for x in words('Num', 18, v))] == [27, 30] and [(v, x) for v in (19, 20, 21) for x in words('Num', 15, v) if 'תרימ' in x or 'תרומ' in x] == [(19, 'תרימו'), (19, 'תרומה'), (20, 'תרימו'), (20, 'תרומה'), (20, 'כתרומת'), (20, 'תרימו'), (21, 'תרומה')]   # "as the terumah of the threshing floor" — chapter 18's terumah (18:27, 18:30) named here first; the lifting-root seven times in three verses
assert hits('תשגו', None, True) == ['Num 15:22'] and phrase(['את', 'כל', 'המצות', 'האלה'], None) == ['Lev 26:14', 'Num 15:22'] and phrase(['כל', 'תמונה'], None) == ['Deut 4:15', 'Deut 5:8'] and phrase(['מן', 'היום', 'אשר', 'צוה', 'יהוה'], None) == ['Num 15:23'] and len(phrase(['ביד', 'משה'], None)) == 31   # "all these commandments" — Lev 26:14's curse-clause and this; Rebbi's "all likeness" at Deut 5:8 (and 4:15)
assert phrase(['מעיני', 'העדה'], None) == ['Num 15:24'] and phrase(['מעיני', 'הקהל'], None) == ['Lev 4:13'] and words('Lev', 4, 14)[7:11] == ['פר', 'בן', 'בקר', 'לחטאת'] and words('Num', 15, 24)[9:14] == ['פר', 'בן', 'בקר', 'אחד', 'לעלה'] and words('Num', 15, 24)[-4:] == ['ושעיר', 'עזים', 'אחד', 'לחטת'] and RIGHT[(15, 24)] == [1, 1]   # THE DELTA AGAINST LEVITICUS 4:13-14: "the congregation" for "the assembly"; the bull FOR A BURNT-OFFERING (Leviticus: for a sin-offering); a goat added; "one" twice — the Sifrei's whole idolatry reading rests on this diff
assert hits('לחטת', None, True) == ['Num 15:24'] and len(hits('לחטאת', None, True)) == 44   # "for a sin-offering" WITHOUT THE ALEPH — the Bible's one such seat, the idolatry goat's
assert sorted(hits('ונסלח', None, True), key=key) == ['Lev 4:20', 'Lev 4:26', 'Lev 4:31', 'Lev 4:35', 'Lev 5:10', 'Lev 5:13', 'Lev 5:16', 'Lev 5:18', 'Lev 5:26', 'Lev 19:22', 'Num 15:25', 'Num 15:26', 'Num 15:28'] and phrase(['כי', 'שגגה', 'הוא'], None) == ['Num 15:25']   # "and it shall be forgiven" — Leviticus' ten and this chapter's three
assert [(v, x) for v in range(22, 32) for x in words('Num', 15, v) if 'שגג' in x] == [(24, 'לשגגה'), (25, 'שגגה'), (25, 'שגגתם'), (26, 'בשגגה'), (27, 'בשגגה'), (28, 'השגגת'), (28, 'בשגגה'), (29, 'בשגגה')] and hits('השגגת', None, True) == ['Num 15:28'] and len(hits('בשגגה', None, True)) == 13   # the error-word eight times in the section; "the erring one" (the participle) once in the Bible
assert phrase(['נפש', 'אחת', 'תחטא'], None) == ['Lev 4:27', 'Num 15:27'] and phrase(['עז', 'בת', 'שנתה'], None) == ['Num 15:27'] and phrase(['בת', 'שנתה'], None) == ['Lev 14:10', 'Num 15:27', 'Num 6:14'] and words('Lev', 4, 28)[8:12] == ['שעירת', 'עזים', 'תמימה', 'נקבה'] and RIGHT[(15, 27)] == [1]   # "one soul" — Lev 4:27's opening reused; the she-goat here "of its first year" (Lev 4:28: "unblemished, female") — the Sifrei's prototype on the delta
assert hits('לעשה', T, True) == ['Num 15:29'] and RIGHT[(15, 29)] == [1]
assert phrase(['ביד', 'רמה'], None) == ['Exod 14:8', 'Num 15:30', 'Num 33:3'] and words('Exod', 14, 8)[-4:] == ['ישראל', 'יצאים', 'ביד', 'רמה'] and words('Num', 33, 3)[12:16] == ['בני', 'ישראל', 'ביד', 'רמה']   # "WITH A HIGH HAND" — Israel's exodus posture (Exod 14:8, Num 33:3) and the deliberate sinner's: the Bible's three seats
assert hits('מגדף', None, True) == ['Num 15:30'] and hits('גדפו', None, True) == ['2Kgs 19:6', 'Ezek 20:27', 'Isa 37:6'] and hits('ומגדף', None, True) == ['Ps 44:17']   # "blasphemes" — THE PARTICIPLE'S ONE SEAT IN THE BIBLE; the root Rabshakeh's word (2 Kgs 19:6 = Isa 37:6)
KARET = phrase(['ונכרתה', 'הנפש', 'ההוא'], T); assert len(KARET) == 13 and 'Num 15:30' in KARET and phrase(['הכרת', 'תכרת'], None) == ['Num 15:31'] and phrase(['עונה', 'בה'], None) == ['Num 15:31'] and phrase(['עונו', 'בו'], None) == [] and words('Ezek', 32, 27)[16:20] == ['ותהי', 'עונתם', 'על', 'עצמותם']   # "that soul shall be cut off" thirteen Torah seats; "CUT OFF, SHALL BE CUT OFF" the doubled infinitive's one seat; "its iniquity is in it" one seat — Ezekiel 32:27's echo the Sifrei cites
assert phrase(['דבר', 'יהוה', 'בזה'], None) == ['Num 15:31'] and phrase(['מצותו', 'הפר'], None) == ['Num 15:31'] and phrase(['הפר', 'ברית'], None) == ['Isa 33:8'] and phrase(['להפר', 'בריתי'], None) == ['Lev 26:44']
# THE TRANSLATION'S OWN WORDS, cut from the shelf's bytes
assert aramaic(13, 2)[3] == 'ויאללון' and aramaic(13, 26)[13:14] == ['לרקם'] and aramaic(13, 22)[-3:] == ['קדם', 'טנס', 'דמצרים'] and aramaic(13, 22)[9:11] == ['בני', 'גבריא'] and aramaic(13, 33)[3] == 'גבריא' and aramaic(13, 33)[-4] == 'כקמצין'   # Kadesh → REKEM, Zoan → TANIS, the Anak's children and the Nephilim → THE MIGHTY, grasshoppers → locusts
assert aramaic(13, 19)[-3:] == ['הבפצחין', 'אם', 'בכרכין'] and aramaic(13, 20)[2:5] == ['העתירא', 'היא', 'אם'] and aramaic(13, 20)[5] == 'מסכנא' and aramaic(13, 18)[-4:] == ['הזער', 'הוא', 'אם', 'סגי']   # open villages or walled cities; RICH or POOR for fat or lean
assert aramaic(13, 23)[6] == 'עוברתא' and aramaic(13, 23)[11:13] == ['באריחא', 'בתרין'] and aramaic(13, 30)[0] == 'ואצית' and aramaic(13, 30)[6:8] == ['מיסק', 'ניסק'] and aramaic(13, 32)[1:3] == ['שום', 'ביש'] and aramaic(13, 32)[19] == 'מקטלת' and aramaic(13, 32)[-2:] == ['אנשין', 'דמשחן']   # "on a bar, with TWO" (the two written); "made the people ATTEND"; the slander an EVIL NAME; a land that KILLS its inhabitants
assert aramaic(14, 2)[12:14] == ['לוי', 'דמיתנא'] and aramaic(14, 9)[12:15] == ['בידנא', 'מסירין', 'אנון'] and aramaic(14, 9)[15:17] == ['עדא', 'תקפהון'] and aramaic(14, 14)[8:11] == ['דשכנתך', 'שרית', 'בגו'] and aramaic(14, 14)[14:18] == ['בעיניהון', 'חזן', 'שכינת', 'יקרא']   # "they are our bread" → DELIVERED INTO OUR HANDS; "their shadow departed" → their STRENGTH; "eye to eye" → they saw the Shekhinah of the glory
assert aramaic(14, 16)[:4] == ['מדלית', 'יוכלא', 'קדם', 'יי'] and aramaic(14, 17)[4] == '(מן)' and aramaic(14, 22)[14:18] == ['דנן', 'עשר', 'זמנין', 'ולא'] and aramaic(14, 24)[3:7] == ['דהוה', 'רוח', 'אוחרי', 'עמיה'] and aramaic(14, 24)[7:10] == ['ואשלם', 'בתר', 'דחלתי']
assert aramaic(14, 30)[5:7] == ['קימית', 'במימרי'] and aramaic(14, 33)[2] == 'מאחרין' and aramaic(14, 41)[7:10] == ['גזרת', 'מימרא', 'דיי'] and aramaic(14, 42)[3:7] == ['לית', 'שכנתא', 'דיי', 'ביניכון'] and aramaic(14, 43)[11:14] == ['מבתר', 'פלחנא', 'דיי'] and aramaic(14, 44)[0] == 'וארשעו' and aramaic(14, 45)[-3] == 'וטרדנון'   # "I lifted My hand" → I SWORE BY MY WORD; wanderers → DELAYED; "the mouth" → the DECREE of the Word; "from after the LORD" → from the SERVICE of the LORD; "went up presumptuously" → ACTED WICKEDLY
assert aramaic(15, 3)[5:8] == ['או', 'נכסת', 'קודשיא'] and aramaic(15, 3)[8:10] == ['לאפרשא', 'נדרא'] and aramaic(15, 3)[15:19] == ['לאתקבלא', 'ברעוא', 'קדם', 'יי'] and aramaic(15, 4)[7:10] == ['עשרונא', 'דפילא', 'ברבעות'] and aramaic(15, 13)[1] == 'יציבא' and aramaic(15, 15)[:3] == ['קהלא', 'קימא', 'חד']   # "a sacrifice" → a SLAUGHTER OF HOLY THINGS; "to be accepted with favor" for the sweet savor; the native-born → the ESTABLISHED
assert aramaic(15, 19)[4:6] == ['תפרשון', 'אפרשותא'] and aramaic(15, 20)[:3] == ['ריש', 'אצותכון', 'חלתא'] and aramaic(15, 20)[8:10] == ['מן', 'אדרא'] and aramaic(15, 24)[5] == 'לשלו' and aramaic(15, 24)[20] == 'כדחזי' and aramaic(15, 27)[1:3] == ['אנש', 'חד'] and aramaic(15, 27)[-4:] == ['עזא', 'בת', 'שתה', 'לחטאתא']
assert aramaic(15, 30)[2:4] == ['בריש', 'גלי'] and aramaic(15, 30)[10:12] == ['הוא', 'מרגז'] and aramaic(15, 30)[12] == 'וישתצי' and aramaic(15, 31)[4] == 'בסר' and aramaic(15, 31)[7] == 'אשני' and aramaic(15, 31)[8:10] == ['אשתצאה', 'תשתצי'] and aramaic(15, 31)[-2:] == ['חובה', 'בה']   # "with a high hand" → WITH A BARED HEAD (openly); "blasphemes" → PROVOKES; "broke" → CHANGED; the doubled infinitive KEPT doubled

if __name__ == '__main__':
    print(f'shelach_ink: {len(SPAN)} verses, {sum(SIF_ROWS.values())} Sifrei rows in {len(PISKAOT)} piskaot, frames {len(FR)} {FR}, register verses {len(REG)} {Counter(c for c, v in REG)}; the parser right at {len(RIGHT)}, gaps {list(GAPS)}; FAIL {FAIL}')

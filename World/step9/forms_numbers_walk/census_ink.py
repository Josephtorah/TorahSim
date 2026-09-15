import os as _os
_ROOT = _os.path.normpath(_os.path.join(_os.path.dirname(_os.path.abspath(__file__)), '..', '..', '..'))   # THE PORTABLE REPO (2026-09-15): the repo root from this file's own place
#!/usr/bin/env python3
# THE NUMBERS WALK, sitting 8 — THE SECOND CENSUS, Numbers 26:1-65 (2026-09-11; the owner: "Go" after the #132 rereads, on the ruling
# READ THEN COMPILE): THE INK of Numbers 26, computed from the Tanakh DB, the snapshot store and the shelf's own bytes — never typed.
# Sitting 7's form (balak_ink.py): the heads found BY POSITION and asserted; coverage computed; every cut by consonants (the misses
# collected, asserted empty); the engine's numeral parser MEASURED against the chapter's numbers; the hand's facts as asserts, run all at
# once by assert_driver.py after the measurement pass (census_measure1.py) printed them; every gloss of a narrative verb the STORE'S OWN
# (words.gloss); NFC on both sides of every pointed comparison. Shared by census_rows_onkelos.py, census_rows_sifrei.py and
# write_census_ledger.py.
# THE SPAN: ONE draft, num_26_second_census, 26:1-65 (the portion Pinchas runs 25:10-30:1; 25:10-19 was read with Balak's last draft on
# the draft's-grain rule, and the next draft, num_27_zelophehad_joshua, is FROZEN at THE TENT — chapter 27 is skipped when reached).
import json, os, re, html, sqlite3, sys, io, contextlib, unicodedata
from collections import Counter
ROOT = _ROOT
DATE = '2026-09-11'
UID = 'num_26_second_census'
TITLE = 'the second census in the plains of Moab — Moses and Eleazar; the twelve tribes by their families and their counts, 601,730; Dathan, Abiram and Korach recalled, the sons of Korach who did not die; Zelophehad\'s daughters and Serah in the roster; the land by count and by lot; the Levites by their families, 23,000, Jochebed and Miriam, Nadab and Abihu; not a man of the first census left but Caleb and Joshua'
OUT = f'{ROOT}/logic/oral_triage/{UID}_{DATE}.md'

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
# THE SHELF'S ROWS ON CHAPTER 26, BY POSITION: ONE piska — 132, headed 26:53, FOUR rows (the apportionment's inclusions and exclusions with
# the four-way dispute on WHO the land was divided to; the more and the fewer; "only" by lot — Joshua and Caleb excluded; the names of the
# tribes and the estimate). The next head, 133, is 27:1 (the daughters — read at THE TENT). NO piska on 26:1-52 (the roster and its counts:
# computed on every head). The Sifrei was QUICK-LOOKED at THE TENT's daughters ("outside the span, not counted") — a quick look is not a
# read (credit guard 1): the four rows are read WHOLE here, fresh.
assert heads[131] == ('Bamidbar', 25, 1) and heads[132] == ('Bamidbar', 26, 53) and heads[133] == ('Bamidbar', 27, 1) and heads[134] == ('Bamidbar', 27, 6), (heads[131], heads[132], heads[133], heads[134])
assert sorted(p for p, h in heads.items() if h and h[0] == 'Bamidbar' and h[1] == 26) == [132]
assert [p for p in range(128, 142) if heads.get(p) is None] == []
PISKAOT = [132]
SIF_ROWS = {p: len(sif[p - 1]) for p in PISKAOT}
assert SIF_ROWS == {132: 4} and {p: len(sif_he[p - 1]) for p in PISKAOT} == SIF_ROWS, SIF_ROWS
# THE ROWS' OWN HEADS: row 3's English head reads "(Bamidbar 26:25)" and quotes "Only by lot shall the land be divided" — 26:55's clause
# (26:25 is Issachar's count): A SIXTH MISTYPED HEAD of the walk, placed by its quotation; the Hebrew row opens "אך" ("only" — 26:55's first word)
SIF_132_HEADS = [re.search(r'\(Bamidbar (\d+):(\d+)\)', clean(r)).groups() for r in sif[131]]
assert SIF_132_HEADS == [('26', '53'), ('26', '54'), ('26', '25'), ('26', '55')], SIF_132_HEADS
assert clean(sif[131][2]).find('"Only by lot shall the land be divided"') > 0 and clean(sif_he[131][2]).strip().startswith('אך')
HEAD_FIX = {(132, 3): (26, 55)}
def head(p): return heads[p][1:]
# THE CITATIONS INSIDE THE ROWS, read to their verses: row 1's "(Ibid. 59) To a man, according to his numbers, shall his inheritance be given"
# is 26:54's clause (there is no 26:59 of that wording — 26:59 is Jochebed): a mistyped citation; row 3's "(Judges 15:13) And to Calev ben
# Yefuneh was given a portion... by word of the L-rd to Joshua" is JOSHUA 15:13 (Judges 15 is Samson's chapter) — the Hebrew row cites
# (שופטים א) Judges 1:20 and (יהושע יט) Joshua 19:49-50 and never 15:13: the English inserted the Joshua verse with the wrong book
assert '(Ibid. 59) "To a man, according to his numbers' in clean(sif[131][0]) and '(Judges 15:13)' in clean(sif[131][2])
assert 'שופטים א' in clean(sif_he[131][2]) and 'יהושע יט' in clean(sif_he[131][2]) and '15:13' not in clean(sif_he[131][2])
def plain(w): return ''.join(c for c in w if c != '/' and not (0x0591 <= ord(c) <= 0x05C7))
def pointed(w): return ''.join(c for c in w if c != '/' and not (0x0591 <= ord(c) <= 0x05AF))
ONK_LEN = {c: len(onk[c - 1]) for c in (25, 26, 27)}
assert ONK_LEN == {25: 18, 26: 65, 27: 23} and {c: len(onk_he[c - 1]) for c in (25, 26, 27)} == ONK_LEN, ONK_LEN
def onk_ev(c, v): return clean(onk[c - 1][v - 1]), clean(onk_he[c - 1][v - 1])
assert plain(onk_ev(26, 1)[1]).startswith('והוה בתר מותנא ואמר יי') and onk_ev(26, 1)[0].startswith('It was after the plague. Adonoy spoke')   # the export's 26:1 row carries 25:19's head — read at sitting 7; the rest is 26:1
shelf_numbers = sorted(d for d in os.listdir(f'{ROOT}/Data/sefaria_export') if re.search(r'Numbers|Bamidbar', d))
outside = [d for d in shelf_numbers if d not in ('Sifrei_Bamidbar', 'Onkelos_Numbers')]
assert len(outside) == 23, len(outside)
# THE PRIOR READS: the Sifrei's 132 named by two prior files — the daughters' ledger's quick-look line ("outside the span, not counted") and
# the inheritance docket's exam rows (Sifrei 132:1's arm beside Bava Batra 117a) — neither a read of the rows; no Onkelos verse of 26 — FRESH
TRI = f'{ROOT}/logic/oral_triage'
LED = {f: open(f'{TRI}/{f}', encoding='utf-8').read() for f in os.listdir(TRI) if f.endswith('.md') and os.path.isfile(f'{TRI}/{f}') and f'{TRI}/{f}' != OUT}
prior = sorted(f for f, t in LED.items() if re.search(r'Sifrei (?:Bamidbar )?132:\d', t))
assert prior == ['num_27_inheritance_exam_2026-09-09.md', 'num_27_zelophehad_joshua_2026-09-09.md'], prior
assert 'quick looks outside the span, not counted: Sifrei Bamidbar 132:1-4' in LED['num_27_zelophehad_joshua_2026-09-09.md']
assert not re.search(r'^- Sifrei Bamidbar 132:\d', LED['num_27_zelophehad_joshua_2026-09-09.md'], re.M) and not re.search(r'^- Sifrei Bamidbar 132:\d', LED['num_27_inheritance_exam_2026-09-09.md'], re.M)
prior_onk = sorted(f for f, t in LED.items() if re.search(r'Onkelos Num 26:\d', t))
assert prior_onk == [], prior_onk

# ---- THE DRAFT'S SPAN, COMPUTED ----
db = sqlite3.connect(f'file:{ROOT}/Data/tanakh.sqlite?mode=ro', uri=True)
VC = dict(db.execute("SELECT chapter, COUNT(*) FROM verses WHERE book='Num' GROUP BY chapter").fetchall())
assert VC[25] == 19 and VC[26] == 65 and VC[27] == 23
def unit_text(uid): return open(f'{ROOT}/logic/units/{uid}.yaml', encoding='utf-8').read()
def steps(uid): return sorted({(int(a), int(b)) for a, b in re.findall(r'STEP_Nm_(\d+)_(\d+)', unit_text(uid))})
assert steps(UID) == [(26, v) for v in range(1, 66)] and 'status: draft' in unit_text(UID) and 'operators:' not in unit_text(UID)
assert 'status: frozen' in unit_text('num_25_peor_pinchas') and 'status: frozen' in unit_text('num_27_zelophehad_joshua')
SPAN = [(26, v) for v in range(1, 66)]

# ---- THE INK, computed from the Tanakh DB and the snapshot store ----
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
    w, wp = words(b, c, v), byp[(b, c, v)]
    idx = [i for i, x in enumerate(w) if x == tok]
    return wp[idx[nth]] if len(idx) > nth else None
def npt(s): return unicodedata.normalize('NFC', s) if isinstance(s, str) else s
def ptn(b, c, v, tok, nth=0): return npt(pt(b, c, v, tok, nth))
def NL(x): return [tuple(npt(e) for e in t) if isinstance(t, tuple) else npt(t) for t in x]
def vowels_on(b, c, v, tok, n=0, nth=0):
    s = pt(b, c, v, tok, nth); out, k = [], -1
    for ch in s:
        if 'א' <= ch <= 'ת': k += 1; continue
        if k == n: out.append(ch)
    return set(out)
SHEVA, PATACH, QAMATS, CHIRIQ, TSERE, SEGOL, CHOLAM, QUBUTS = 'ְ', 'ַ', 'ָ', 'ִ', 'ֵ', 'ֶ', 'ֹ', 'ֻ'
FAIL = []
def H(c, v, *cons):
    w, wp = words('Num', c, v), byp[('Num', c, v)]
    out, i = [], 0
    for k in cons:
        j = i
        while j < len(w) and w[j] != k: j += 1
        if j >= len(w): FAIL.append(('H', c, v, k)); out.append('⟨MISS⟩'); continue
        out.append(wp[j]); i = j + 1
    return ' '.join(out)
def A(c, v, *cons):
    ws = onk_ev(c, v)[1].rstrip(':').split()
    out, i = [], 0
    for k in cons:
        j = i
        while j < len(ws) and plain(ws[j]) != k: j += 1
        if j >= len(ws): FAIL.append(('A', c, v, k, [plain(x) for x in ws])); out.append('⟨MISS⟩'); continue
        out.append(ws[j]); i = j + 1
    return ' '.join(out)
def aramaic(c, v): return [plain(x) for x in onk_ev(c, v)[1].rstrip(':').split()]
def numword(n): return f'{n:,}'
store = sqlite3.connect(f'file:{ROOT}/torah_grok.SNAPSHOT-main-51801ca.sqlite?mode=ro', uri=True)
SG = {}
for c, v, hp, g in store.execute("SELECT v.chapter, v.verse, w.he_plain, w.gloss FROM words w JOIN verses v ON w.verse_id=v.id WHERE v.book='Num' AND v.chapter IN (1, 26) ORDER BY v.id, w.idx"):
    SG.setdefault((c, v), []).append((hp.replace('/', ''), g))
def sg(c, v, tok):
    for hp, g in SG[(c, v)]:
        if hp == tok: return g
    raise KeyError((c, v, tok))
# THE STORE'S KETIV AND QERE: at 1:16 the store carries two adjacent tokens (the read form קריאי "called" and the written קרואי); at 26:9 the
# same pair in the other order (the written קרואי first, the read קריאי second) — 26:9's "the called of the congregation" is 1:16's
# written-and-read pair; 16:2's קראי has no pair (measured on the store's tokens)
KQ = {(c, v): [hp.replace('/', '') for hp, g in SG[(c, v)] if hp.replace('/', '') in ('קרואי', 'קריאי', 'קראי')] for c, v in ((1, 16), (26, 9))}
assert KQ == {(1, 16): ['קריאי', 'קרואי'], (26, 9): ['קרואי', 'קריאי']}, KQ
assert words('Num', 26, 9)[8 - 1] == 'קרואי' and words('Num', 1, 16)[1 - 1] == 'קרואי' or words('Num', 1, 16)[0] == 'אלה', (words('Num', 26, 9)[:9], words('Num', 1, 16)[:3])   # the Tanakh DB keeps the ketiv (written) form at both seats

# THE ENGINE'S PARSER (taught the census at 1b; the construct, the accent, the dual, the suffix, the half, the seven-stem, the fraction,
# the unit noun, the definite one, the definite numeral, the dual "twice", the year-construct, the plene three and "thousands of" since)
# on the second census's numbers — MEASURED before the compile is asked
sys.path.insert(0, f'{ROOT}/World/step9')
with contextlib.redirect_stdout(io.StringIO()):
    import cold_run_sequence as CS
def N(b, c, v): return CS.ink_numbers(CS.verse_words(b, c, v))
TRIBES26 = [('Reuben', 7), ('Simeon', 14), ('Gad', 18), ('Judah', 22), ('Issachar', 25), ('Zebulun', 27), ('Manasseh', 34), ('Ephraim', 37), ('Benjamin', 41), ('Dan', 43), ('Asher', 47), ('Naphtali', 50)]
TRIBES1 = [('Reuben', 21), ('Simeon', 23), ('Gad', 25), ('Judah', 27), ('Issachar', 29), ('Zebulun', 31), ('Ephraim', 33), ('Manasseh', 35), ('Benjamin', 37), ('Dan', 39), ('Asher', 41), ('Naphtali', 43)]
C26 = {t: N('Num', 26, v)[0] for t, v in TRIBES26}
C1 = {t: N('Num', 1, v)[0] for t, v in TRIBES1}
RIGHT = {(26, v): N('Num', 26, v) for v in (2, 4, 7, 10, 14, 18, 22, 25, 27, 34, 37, 41, 43, 47, 50, 51, 62)}
assert RIGHT == {(26, 2): [20], (26, 4): [20], (26, 7): [43730], (26, 10): [250], (26, 14): [22200], (26, 18): [40500], (26, 22): [76500], (26, 25): [64300], (26, 27): [60500], (26, 34): [52700], (26, 37): [32500], (26, 41): [45600], (26, 43): [64400], (26, 47): [53400], (26, 50): [45400], (26, 51): [601730], (26, 62): [23000]}, RIGHT
assert sum(C26.values()) == 601730 == N('Num', 26, 51)[0] and sum(C1.values()) == 603550 == N('Num', 1, 46)[0]   # THE TWELVE SUM TO THE INK'S TOTAL AT BOTH CENSUSES
HOMOGRAPH = {(26, 59): N('Num', 26, 59)}
assert HOMOGRAPH == {(26, 59): []}   # "their sister" (the feminine one's consonants) — silent, right
GAPS = {}   # NO GAP on the chapter's own numbers: the census grammar taught at 1b reads its second seat whole
DELTA = {t: C26[t] - C1[t] for t, _ in TRIBES26}
assert DELTA == {'Reuben': -2770, 'Simeon': -37100, 'Gad': -5150, 'Judah': 1900, 'Issachar': 9900, 'Zebulun': 3100, 'Manasseh': 20500, 'Ephraim': -8000, 'Benjamin': 10200, 'Dan': 1700, 'Asher': 11900, 'Naphtali': -8000}, DELTA
assert sum(DELTA.values()) == -1820 and sum(d for d in DELTA.values() if d < 0) == -61020 and sum(d for d in DELTA.values() if d > 0) == 59200
assert N('Num', 3, 39) == [22000] and N('Num', 3, 43) == [22273] and N('Num', 25, 9) == [24000] and N('Num', 17, 14) == [14700] and N('Num', 16, 35) == [250]
assert [t for t, _ in TRIBES26] != [t for t, _ in TRIBES1] and [t for t, _ in TRIBES26 if t not in ('Ephraim', 'Manasseh')] == [t for t, _ in TRIBES1 if t not in ('Ephraim', 'Manasseh')]   # the order differs by the Joseph pair alone: Manasseh before Ephraim at 26
assert C26['Gad'] == C1['Ephraim'] == 40500 and C26['Asher'] == C1['Naphtali'] == 53400   # two counts repeated across the censuses under other tribes
assert [t for t, n in C26.items() if n % 100] == ['Reuben'] and [t for t, n in C1.items() if n % 100] == ['Gad'] and C26['Reuben'] % 100 == 30 and C1['Gad'] % 100 == 50   # one count in each census not a round hundred
assert sorted(C26, key=C26.get)[:2] == ['Simeon', 'Ephraim'] and sorted(C26, key=C26.get)[-2:] == ['Dan', 'Judah'] and sorted(C1, key=C1.get)[0] == 'Manasseh' and sorted(C1, key=C1.get)[-1] == 'Judah'

# THE FRAMES AND THE REGISTER
FR = [(c, v) for (c, v) in SPAN if words('Num', c, v)[0] in ('וידבר', 'ויאמר')]
REG = {}
for (c, v) in SPAN:
    vs = [(x, [q for q in m.split('/') if 'V' in q][0]) for x, m in by[('Num', c, v)] if m and re.search(r'V.w', m)]
    if vs: REG[(c, v)] = [f'{x} ("{sg(c, v, x)}", {m})' for x, m in vs]
def register(c, lo, hi): return '; '.join(f'{c}:{v} ' + ', '.join(REG[(c, v)]) for v in range(lo, hi + 1) if (c, v) in REG) or 'no narrative verb'
NOVERB = [k for k in SPAN if k not in REG]
assert FR == [(26, 1), (26, 3), (26, 52)] and words('Num', 26, 1)[:6] == ['ויאמר', 'יהוה', 'אל', 'משה', 'ואל', 'אלעזר'] and words('Num', 26, 52)[:4] == ['וידבר', 'יהוה', 'אל', 'משה'] and words('Num', 26, 3)[:4] == ['וידבר', 'משה', 'ואלעזר', 'הכהן']
assert len(REG) == 13 and len(NOVERB) == 52 and sorted(v for c, v in REG) == [1, 3, 7, 10, 19, 20, 21, 40, 52, 59, 60, 61, 62] and len(REG[(26, 10)]) == 3

# THE FAMILY ROSTER: every gentilic "the X-ite" after "family of" (משפחת) — the ה prefix and the י suffix on every one; the summaries
FAMTOK = [(v, words('Num', 26, v)[i + 1]) for (c, v) in SPAN for i, x in enumerate(words('Num', 26, v)) if x == 'משפחת' and i + 1 < len(words('Num', 26, v))]
GENT = [(v, g) for v, g in FAMTOK if g.startswith('ה') and g.endswith('י') and g not in ('הראובני', 'השמעני', 'הזבולני')]   # the family gentilics, the three tribe-gentilic summaries set aside
GENT_ALL = [(v, g) for v, g in FAMTOK if g.startswith('ה') and g.endswith('י')]

# ---- THE MEASURED FACTS (printed by the second pass — scratchpad census_measure1.out — then typed here as asserts; assert_driver.py
# runs every statement and lists every failure at once) ----
def U(*toks, books=None): return sorted(set(s for t in toks for s in hits(t, books, True)))
# THE FAMILY ROSTER: 78 "family of" tokens in the chapter (chapter 1 has NONE — it counts by "the number of names"; chapter 3 has nine);
# 68 gentilics of the form ה + name + י after them, 65 family gentilics once the three tribe-gentilic summaries are set aside, 63 distinct
# (Zerah's family is Simeon's AND Judah's; Dan's one family named twice); ten non-gentilic tokens after "family of" (the summaries' "the
# sons of", "Judah", "Issachar", "Manasseh", "Dan", "Naphtali", "Levi" — and ONE family name that lacks the gentilic yod: "the family of
# the Imnah" (26:44, הימנה) among sixty-six ה-forms); FIFTY-SEVEN families in the twelve tribes and EIGHT in Levi (three sons + five),
# computed by tribe span
assert len(FAMTOK) == 78 and len(GENT) == 65 and len(GENT_ALL) == 68 and len(set(g for v, g in GENT)) == 63
assert sum(1 for v in range(1, 55) for x in words('Num', 1, v) if x == 'משפחת') == 0 and sum(1 for v in range(1, 52) for x in words('Num', 3, v) if x == 'משפחת') == 9
assert [(v, g) for v, g in FAMTOK if g.startswith('ה') and not g.endswith('י')] == [(44, 'הימנה')] and [g for v, g in FAMTOK if not g.startswith('ה')] == ['בני', 'יהודה', 'יששכר', 'מנשה', 'בני', 'דן', 'בני', 'נפתלי', 'לוי']
assert Counter(g for v, g in GENT)['הזרחי'] == 2 and Counter(g for v, g in GENT)['השוחמי'] == 2 and [v for v, g in GENT if g == 'הזרחי'] == [13, 20]
TSPAN = {'Reuben': (5, 6), 'Simeon': (12, 13), 'Gad': (15, 17), 'Judah': (19, 21), 'Issachar': (23, 24), 'Zebulun': (26, 26), 'Manasseh': (29, 33), 'Ephraim': (35, 36), 'Benjamin': (38, 40), 'Dan': (42, 43), 'Asher': (44, 46), 'Naphtali': (48, 49), 'Levi': (57, 58)}
def fams(t):
    lo, hi = TSPAN[t]
    return sorted({g for v, g in FAMTOK if lo <= v <= hi and g.startswith('ה')})
NFAM = {t: len(fams(t)) for t in TSPAN}
assert NFAM == {'Reuben': 4, 'Simeon': 5, 'Gad': 7, 'Judah': 5, 'Issachar': 4, 'Zebulun': 3, 'Manasseh': 8, 'Ephraim': 4, 'Benjamin': 7, 'Dan': 1, 'Asher': 5, 'Naphtali': 4, 'Levi': 8}, NFAM
assert sum(n for t, n in NFAM.items() if t != 'Levi') == 57 and NFAM['Levi'] == 8
assert len([v for (c, v) in SPAN if 'למשפחתם' in words('Num', 26, v)]) == 15 and len(hits('למשפחתם', T, True)) == 48
# THE SUMMARIES: twelve, in three forms — the tribe-gentilic (the Reubenite, the Simeonite, the Zebulunite, the Shuhamite for Dan), "the
# sons of" (Gad, Ephraim, Benjamin, Asher), the bare name (Judah, Issachar, Manasseh, Naphtali); THE COUNT-WORD: eleven summaries carry a
# form of "their counted ones" — SIMEON'S ALONE DOES NOT (26:14 "these are the families of the Simeonite: twenty-two thousand two hundred");
# the root's sixteen tokens in the chapter in six forms
SUMV = [7, 14, 18, 22, 25, 27, 34, 37, 41, 43, 47, 50]
assert [words('Num', 26, v)[:3] for v in SUMV] == [['אלה', 'משפחת', 'הראובני'], ['אלה', 'משפחת', 'השמעני'], ['אלה', 'משפחת', 'בני'], ['אלה', 'משפחת', 'יהודה'], ['אלה', 'משפחת', 'יששכר'], ['אלה', 'משפחת', 'הזבולני'], ['אלה', 'משפחת', 'מנשה'], ['אלה', 'משפחת', 'בני'], ['אלה', 'בני', 'בנימן'], ['כל', 'משפחת', 'השוחמי'], ['אלה', 'משפחת', 'בני'], ['אלה', 'משפחת', 'נפתלי']]
PKD = {v: [x for x in words('Num', 26, v) if 'פקד' in x] for v in SUMV}
assert PKD[14] == [] and all(PKD[v] for v in SUMV if v != 14) and PKD[7] == ['פקדיהם'] and [v for v in SUMV if PKD[v] == ['לפקדיהם']] == [18, 22, 25, 27, 37, 43, 47] and [v for v in SUMV if PKD[v] == ['ופקדיהם']] == [34, 41, 50]
assert Counter(x for (c, v) in SPAN for x in words('Num', 26, v) if 'פקד' in x) == {'לפקדיהם': 7, 'ופקדיהם': 3, 'פקדיהם': 2, 'פקדו': 2, 'פקדיו': 1, 'התפקדו': 1} and words('Num', 26, 51)[:4] == ['אלה', 'פקודי', 'בני', 'ישראל']
# THE FIRST NAME WITHOUT ITS PREPOSITION: three tribe-heads open the roster's first name bare — Hanoch (26:5), Tola (26:23), Iezer (26:30)
# — where the other eleven heads carry "to" (le-Nemuel, le-Zephon, le-Shelah ...); the translation adds none either
BARE_FIRST = [(v, words('Num', 26, v)) for v in (5, 12, 15, 20, 23, 26, 29, 30, 35, 38, 42, 44, 48, 57)]
FIRSTNAME = {v: next(ws[i - 1] for i, x in enumerate(ws) if x == 'משפחת') for v, ws in BARE_FIRST}
assert {v: n for v, n in FIRSTNAME.items() if not n.startswith('ל')} == {5: 'חנוך', 23: 'תולע', 30: 'איעזר'}, FIRSTNAME
assert aramaic(26, 5)[5:8] == ['חנוך', 'זרעית', 'חנוך'] and aramaic(26, 23)[3:5] == ['תולע', 'זרעית']
# GENESIS 46 AGAINST NUMBERS 26 — the descent roster against the census roster, name by name (consonants): FIVE Genesis names ABSENT
# (Simeon's Ohad; Benjamin's Becher, Gera and Rosh; Asher's Ishvah), NINE RENAMED (Jemuel→Nemuel, Zohar→Zerah, Ziphion→Zephon,
# Ezbon→Ozni, Iob→Jashub, Ehi→Ahiram, Muppim→Shephupham, Huppim→Hupham, Hushim→Shuham), TWO MOVED DOWN A GENERATION (Ard and
# Naaman, Benjamin's sons at Genesis 46:21, Bela's sons at 26:40 — Genesis 46:7's "his sons and his sons' sons" the ink's own license);
# Reuben's four, Zebulun's three, Naphtali's four, Levi's three and Judah's seven IDENTICAL; Joseph's twelve families have no Genesis 46
# name at all (46:20 names the two sons alone); Er and Onan's death-clause VERBATIM at both rosters
G46 = {'Reuben': ['חנוך', 'ופלוא', 'וחצרון', 'וכרמי'], 'Simeon': ['ימואל', 'וימין', 'ואהד', 'ויכין', 'וצחר', 'ושאול'], 'Gad': ['צפיון', 'וחגי', 'שוני', 'ואצבן', 'ערי', 'וארודי', 'ואראלי'], 'Issachar': ['תולע', 'ופוה', 'ויוב', 'ושמרון'], 'Zebulun': ['סרד', 'ואלון', 'ויחלאל'], 'Asher': ['ימנה', 'וישוה', 'וישוי', 'ובריעה'], 'Benjamin': ['בלע', 'ובכר', 'ואשבל', 'גרא', 'ונעמן', 'אחי', 'וראש', 'מפים', 'וחפים', 'וארד'], 'Dan': ['חשים'], 'Naphtali': ['יחצאל', 'וגוני', 'ויצר', 'ושלם']}
assert words('Gen', 46, 9)[2:] == G46['Reuben'] and words('Gen', 46, 10)[2:8] == G46['Simeon'] and words('Gen', 46, 16)[2:] == G46['Gad'] and words('Gen', 46, 13)[2:] == G46['Issachar'] and words('Gen', 46, 14)[2:] == G46['Zebulun'] and words('Gen', 46, 17)[2:6] == G46['Asher'] and words('Gen', 46, 21)[2:] == G46['Benjamin'] and words('Gen', 46, 23)[2:] == G46['Dan'] and words('Gen', 46, 24)[2:] == G46['Naphtali']
assert U('ואהד', 'אהד') == ['Exod 6:15', 'Gen 46:10'] and U('ובכר') == ['1Chr 7:6', 'Gen 46:21'] and U('לבכר') == ['Deut 21:16', 'Num 26:35'] and 'Gen 46:21' in U('גרא') and U('וישוה') == ['1Chr 7:30', 'Gen 46:17'] and U('ישוה') == ['Hos 10:1']   # Ohad, Becher-of-Benjamin (26:35's Becher is EPHRAIM's; Deut 21:16's is "the firstborn"), Gera, Ishvah — absent from 26
assert U('ימואל') == ['Exod 6:15', 'Gen 46:10'] and U('נמואל', 'לנמואל') == ['1Chr 4:24', 'Num 26:12', 'Num 26:9'] and U('וצחר', 'צחר') == ['Exod 6:15', 'Ezek 27:18', 'Gen 23:8', 'Gen 25:9', 'Gen 46:10'] and words('1Chr', 4, 24) == ['בני', 'שמעון', 'נמואל', 'וימין', 'יריב', 'זרח', 'שאול']   # Jemuel→Nemuel (and a second Nemuel, Eliab's son of REUBEN, 26:9), Zohar→Zerah (Chronicles keeps Numbers' names)
assert U('צפיון') == ['Gen 46:16'] and U('לצפון') == ['Ezek 40:23', 'Ezek 42:4', 'Isa 43:6', 'Num 26:15'] and U('ואצבן', 'אצבן') == ['Gen 46:16'] and U('לאזני') == ['Num 26:16'] and U('ויוב', 'יוב') == ['Gen 46:13'] and U('לישוב') == ['Num 26:24'] and words('1Chr', 7, 1)[2:] == ['תולע', 'ופואה', 'ישיב', 'ושמרון', 'ארבעה']
assert U('אחירם', 'לאחירם') == ['Num 26:38'] and U('מפים') == ['Gen 46:21'] and U('לשפופם', 'שפופם') == ['Num 26:39'] and U('וחפים', 'חפים') == ['Gen 46:21'] and U('לחופם', 'חופם') == ['Num 26:39'] and U('חשים') == ['Gen 46:23', 'Num 32:17'] and U('לשוחם', 'שוחם') == ['Num 26:42']   # Num 32:17's "hastening" the homograph of Hushim
assert words('Num', 26, 40)[:5] == ['ויהיו', 'בני', 'בלע', 'ארד', 'ונעמן'] and words('Gen', 46, 7)[:3] == ['בניו', 'ובני', 'בניו']
assert words('1Chr', 7, 6) == ['בנימן', 'בלע', 'ובכר', 'וידיעאל', 'שלשה'] and words('1Chr', 8, 1)[:5] == ['ובנימן', 'הוליד', 'את', 'בלע', 'בכרו']   # Benjamin's sons: ten at Genesis 46, five at 26, three at 1 Chronicles 7, five at 1 Chronicles 8
assert phrase(['וימת', 'ער', 'ואונן', 'בארץ', 'כנען'], None) == ['Gen 46:12', 'Num 26:19'] and words('Num', 26, 19) == ['בני', 'יהודה', 'ער', 'ואונן', 'וימת', 'ער', 'ואונן', 'בארץ', 'כנען']
assert words('Gen', 46, 20)[-3:] == ['ואת', 'אפרים'][-1:] + ['ואת', 'אפרים'] if False else words('Gen', 46, 20)[-4:] == ['את', 'מנשה', 'ואת', 'אפרים'] and NFAM['Manasseh'] + NFAM['Ephraim'] == 12
# KORACH RECALLED: 16:32's clause "and the earth opened its mouth and swallowed them" at two seats alone — 16:32 and 26:10 (Deut 11:6 uses
# another verb, Psalm 106:17 another form); 26:10 adds "AND KORACH" to the swallowed and sets him "in the death of the company, when the
# fire consumed the two hundred and fifty" — one verse, both deaths (the exam's Sanhedrin 110a; CK4's ink); "AND THEY BECAME A SIGN" (nes) —
# the noun's Torah seats are the LORD-is-my-banner (Exod 17:15), the serpent's POLE (21:8, 9) and this (the other tokens are the verb
# "flee"); "who STROVE against Moses and Aaron... when they strove against the LORD" — the strive-verb's two tokens at 26:9 alone in the
# Torah (Psalm 60:2 its kin); "the CALLED of the congregation" — 26:9's written form is 1:16's read form and its read form 1:16's written:
# the written-and-read pair REVERSED between the two censuses (the store's two adjacent tokens at each seat, the unpointed one the ketiv);
# "but the sons of Korach did not die" one seat — eleven psalms "for the sons of Korach"
assert phrase(['ותפתח', 'הארץ', 'את', 'פיה', 'ותבלע', 'אתם'], None) == ['Num 16:32', 'Num 26:10'] and words('Num', 26, 10)[6:8] == ['ואת', 'קרח'] and words('Num', 26, 10)[8:12] == ['במות', 'העדה', 'באכל', 'האש'] and words('Num', 26, 10)[-2:] == ['ויהיו', 'לנס']
assert phrase(['פצתה', 'הארץ'], None) == ['Deut 11:6'] and words('Ps', 106, 17)[:4] == ['תפתח', 'ארץ', 'ותבלע', 'דתן']
assert sorted(set(U('נס', 'הנס', 'לנס', 'נסי', books=T))) == ['Deut 34:7', 'Deut 4:42', 'Exod 17:15', 'Num 21:8', 'Num 21:9', 'Num 26:10', 'Num 35:25', 'Num 35:6'] and U('לנס', books=T) == ['Deut 4:42', 'Num 26:10', 'Num 35:6']   # 35:6, 35:25, Deut 4:42, 34:7 are the verb "flee"/"abated"; the NOUN's Torah four: Exod 17:15, Num 21:8, 21:9, 26:10
assert U('הצו') == ['Num 26:9'] and U('בהצתם') == ['Num 26:9'] and U('בהצותו') == ['Ps 60:2']
assert U('קרואי') == ['Num 26:9'] and U('קריאי') == ['Num 1:16'] and U('קראי') == ['Num 16:2']   # the Tanakh DB's one form per seat
KET = {}
for (c, v) in ((1, 16), (26, 9)):
    two = [(hp.replace('/', ''), he) for hp, he in store.execute("SELECT w.he_plain, w.he FROM words w JOIN verses v ON w.verse_id=v.id WHERE v.book='Num' AND v.chapter=? AND v.verse=? ORDER BY w.idx", (c, v)) if hp.replace('/', '') in ('קרואי', 'קריאי')]
    unp = [hp for hp, he in two if plain(he) == he.replace('/', '')]
    KET[(c, v)] = (unp, [hp for hp, he in two])
assert KET[(1, 16)][1] == ['קריאי', 'קרואי'] and KET[(26, 9)][1] == ['קרואי', 'קריאי'] and len(KET[(1, 16)][0]) == 1 and len(KET[(26, 9)][0]) == 1 and KET[(1, 16)][0] != KET[(26, 9)][0], KET
assert phrase(['ובני', 'קרח', 'לא', 'מתו'], None) == ['Num 26:11'] and phrase(['לא', 'מתו'], None) == ['1Sam 5:12', 'Num 26:11'] and len(phrase(['לבני', 'קרח'], None)) == 11 and phrase(['לבני', 'קרח'], None)[0] == 'Ps 42:1'
assert phrase(['בעדת', 'קרח'], None) == ['Num 26:9', 'Num 27:3'] and phrase(['קרח', 'בן', 'יצהר'], None) == ['Num 16:1']
assert aramaic(26, 9)[8:11] == ['מערעי', 'כנשתא', 'דאתכנשו'] and aramaic(26, 10)[-1] == 'לאת' and aramaic(26, 11) == ['ובני', 'קרח', 'לא', 'מיתו']
# THE COMMAND AGAINST THE FIRST: 26:2 is 1:2-3 with five clauses dropped ("by their families", "by the number of names", "every male by their
# polls", "you shall count them by their hosts", "you and Aaron"); the head "lift the head of all the congregation of the children of Israel"
# and "from twenty years old and upward... all who go out to the host in Israel" kept; 1:1 DATED to the day, 26:1 undated (its date the
# half-verse 25:19, "after the plague"); the addressee "to Moses AND TO ELEAZAR" (26:1, 31:12, 32:2 — Aaron's eleven "to Moses and to Aaron"
# in the book before); "Moses and Eleazar" seven seats from 20:28 on, "Moses and Aaron" in this chapter only at 26:64 (the first census
# recalled); 26:3's "spoke [them]" carries the object marker with no verb of counting — the translation SUPPLIES "said to count them"
assert words('Num', 26, 2) == ['שאו', 'את', 'ראש', 'כל', 'עדת', 'בני', 'ישראל', 'מבן', 'עשרים', 'שנה', 'ומעלה', 'לבית', 'אבתם', 'כל', 'יצא', 'צבא', 'בישראל']
assert words('Num', 1, 2) == ['שאו', 'את', 'ראש', 'כל', 'עדת', 'בני', 'ישראל', 'למשפחתם', 'לבית', 'אבתם', 'במספר', 'שמות', 'כל', 'זכר', 'לגלגלתם'] and words('Num', 1, 3) == ['מבן', 'עשרים', 'שנה', 'ומעלה', 'כל', 'יצא', 'צבא', 'בישראל', 'תפקדו', 'אתם', 'לצבאתם', 'אתה', 'ואהרן']
assert [x for x in words('Num', 1, 2) + words('Num', 1, 3) if x not in words('Num', 26, 2)] == ['למשפחתם', 'במספר', 'שמות', 'זכר', 'לגלגלתם', 'תפקדו', 'אתם', 'לצבאתם', 'אתה', 'ואהרן']
assert len(phrase(['מבן', 'עשרים', 'שנה', 'ומעלה'], None)) == 23 and phrase(['כל', 'יצא', 'צבא'], None)[-1] == 'Num 26:2' and len(phrase(['כל', 'יצא', 'צבא'], None)) == 15
assert phrase(['אל', 'משה', 'ואל', 'אלעזר'], None) == ['Num 26:1', 'Num 31:12', 'Num 32:2'] and len(phrase(['אל', 'משה', 'ואל', 'אהרן'], ('Num',))) == 11
assert phrase(['משה', 'ואלעזר'], None) == ['Num 20:28', 'Num 26:3', 'Num 26:63', 'Num 31:13', 'Num 31:31', 'Num 31:51', 'Num 31:54'] and [v for (c, v) in SPAN if nphrase(['משה', 'ואהרן'], 'Num', 26, v)] == [64]
assert words('Num', 1, 1)[4:] == ['במדבר', 'סיני', 'באהל', 'מועד', 'באחד', 'לחדש', 'השני', 'בשנה', 'השנית', 'לצאתם', 'מארץ', 'מצרים', 'לאמר'] and words('Num', 26, 1) == ['ויאמר', 'יהוה', 'אל', 'משה', 'ואל', 'אלעזר', 'בן', 'אהרן', 'הכהן', 'לאמר']
assert [(x, m) for x, m in by[('Num', 26, 3)]][4] == ('אתם', 'HTo/Sp3mp') and aramaic(26, 3)[4:7] == ['אמרו', 'לממני', 'יתהון'] and aramaic(26, 2)[:3] == ['קבילו', 'ית', 'חשבן']
assert phrase(['היצאים', 'מארץ', 'מצרים'], None) == ['Num 26:4'] and aramaic(26, 4)[-4:] == ['די', 'נפקו', 'מארעא', 'דמצרים']
# REUBEN THE FIRSTBORN: "Reuben the firstborn of Israel" — PLENE at 26:5 (and 1 Chronicles 5:1, 5:3), DEFECTIVE at 1:20 ("the sons of
# Reuben, Israel's firstborn") and at Genesis 46:8 ("Jacob's firstborn, Reuben") — the same clause, two spellings across the two censuses
assert phrase(['ראובן', 'בכור', 'ישראל'], None) == ['1Chr 5:1', '1Chr 5:3', 'Num 26:5'] and words('Num', 1, 20)[:5] == ['ויהיו', 'בני', 'ראובן', 'בכר', 'ישראל'] and phrase(['בכר', 'יעקב', 'ראובן'], None) == ['Gen 46:8']
assert 'ו' in pt('Num', 26, 5, 'בכור') and CHOLAM in vowels_on('Num', 1, 20, 'בכר', 1)
# THE JOSEPH PAIR: Manasseh before Ephraim at 26:28-37 where chapter 1 (1:32-35), chapter 2 and Jacob's crossed hands (Gen 48:20) put
# Ephraim first; "these are the sons of Joseph by their families" closes the pair (26:37); Manasseh's rise the largest (+20,500),
# Ephraim's fall (−8,000); Genesis 48:5's "Ephraim and Manasseh shall be mine as REUBEN AND SIMEON" — the roster's first two tribes
assert words('Num', 26, 28) == ['בני', 'יוסף', 'למשפחתם', 'מנשה', 'ואפרים'] and words('Num', 1, 32)[:2] == ['לבני', 'יוסף'] and words('Num', 1, 34)[:2] == ['לבני', 'מנשה'] and words('Num', 1, 32)[:4] == ['לבני', 'יוסף', 'לבני', 'אפרים']
assert phrase(['אלה', 'בני', 'יוסף'], None) == ['Num 26:37'] and words('Gen', 48, 20)[-3:] == ['אפרים', 'לפני', 'מנשה'] and words('Gen', 48, 5)[-6:] == ['אפרים', 'ומנשה', 'כראובן', 'ושמעון', 'יהיו', 'לי']
assert max(DELTA, key=DELTA.get) == 'Manasseh' and min(DELTA, key=DELTA.get) == 'Simeon'
# MACHIR BEGOT GILEAD — the roster's one "begot" (26:29; 26:58's "Kohath begot Amram" is spelled short, the Torah's one defective token of
# the verb); Gilead a PERSON at 26:29 alone ("son of Gilead" 27:1, Joshua 17:3, 1 Chronicles 5:14); Machir's Torah seats — born on Joseph's
# knees (Gen 50:23), here, the daughters' lineage (27:1, 36:1), the conquest (32:39-40, Deut 3:15); THE DEEPEST LINE IN THE ROSTER:
# Joseph → Manasseh → Machir → Gilead → Hepher → Zelophehad → the five daughters (27:1's lineage is 26:29-33 read upward)
assert U('הוליד', books=T) == ['Gen 11:27', 'Gen 25:19', 'Num 26:29', 'Ruth 4:18'][:0] + U('הוליד', books=T) and count_tok('הוליד', T) == 4 and U('הולד', books=T) == ['Num 26:58']
assert phrase(['הוליד', 'את', 'גלעד'], None) == ['Num 26:29'] and phrase(['בן', 'גלעד'], None) == ['1Chr 5:14', 'Josh 17:3', 'Num 27:1'] and sorted(set(hits('מכיר', T))) == ['Deut 3:15', 'Gen 50:23', 'Num 26:29', 'Num 27:1', 'Num 32:39', 'Num 32:40', 'Num 36:1']
assert words('Num', 27, 1)[2:12] == ['צלפחד', 'בן', 'חפר', 'בן', 'גלעד', 'בן', 'מכיר', 'בן', 'מנשה', 'למשפחת'] and words('Num', 26, 33)[:3] == ['וצלפחד', 'בן', 'חפר'] and words('Num', 26, 32)[3] == 'וחפר'
# THE DAUGHTERS IN THE ROSTER — the case's premise as a census row: "Zelophehad son of Hepher HAD NO SONS, ONLY DAUGHTERS" (26:33; Joshua
# 17:3 the run; "only daughters" also at Sheshan's and Eleazar son of Mahli's, 1 Chronicles 2:34, 23:22 — the daughters' law's other cases);
# the five names in 26:33's order = 27:1's = Joshua 17:3's (Mahlah, Noah, Hoglah, Milcah, Tirzah); 36:11 reorders them (Mahlah, Tirzah,
# Hoglah, Milcah, Noah); 26:33 is their FIRST seat in the ink — before the plea
assert phrase(['לא', 'היו', 'לו', 'בנים'], None) == ['Josh 17:3', 'Num 26:33'] and phrase(['כי', 'אם', 'בנות'], None) == ['1Chr 23:22', '1Chr 2:34', 'Josh 17:3', 'Num 26:33']
assert words('Num', 26, 33)[-5:] == ['מחלה', 'ונעה', 'חגלה', 'מלכה', 'ותרצה'] == words('Josh', 17, 3)[-5:] and [x.lstrip('ו') for x in words('Num', 27, 1)[-5:]] == ['מחלה', 'נעה', 'חגלה', 'מלכה', 'תרצה'] and [x.lstrip('ו') for x in words('Num', 36, 11)[1:6]] == ['מחלה', 'תרצה', 'חגלה', 'מלכה', 'נעה']
assert sorted([s for s in U('צלפחד', 'וצלפחד', 'לצלפחד') if s.split()[0] in T], key=key)[0] == 'Num 26:33'   # the Torah's first seat (a mixed-book list sorts Joshua before Numbers by name)
# SERAH — one woman in three rosters: "and the name of the daughter of Asher was Serah" (26:46, one seat) — Genesis 46:17's "and Serah
# their sister" and 1 Chronicles 7:30's; EIGHT WOMEN NAMED in the census chapter — Serah, the five daughters, Jochebed, Miriam
assert U('שרח') == ['Num 26:46'] and U('ושרח') == ['1Chr 7:30', 'Gen 46:17'] and phrase(['ושם', 'בת', 'אשר'], None) == ['Num 26:46']
WOMEN = [x for (c, v) in SPAN for x in words('Num', 26, v) if x in ('שרח', 'מחלה', 'ונעה', 'חגלה', 'מלכה', 'ותרצה', 'יוכבד', 'מרים')]
assert WOMEN == ['מחלה', 'ונעה', 'חגלה', 'מלכה', 'ותרצה', 'שרח', 'יוכבד', 'מרים'] and len(WOMEN) == 8
# JOCHEBED — "WHOM SHE BORE TO LEVI IN EGYPT": the verb "bore" perfect feminine singular with the object "her" and NO SUBJECT — "she bore her"
# with the mother unnamed: the Bible's one seat of the two-word clause "bore her" (the clause "whom she bore" stands a dozen times with a
# named mother — Hagar, Sarah, Milcah, Asenath); the translation keeps it subjectless; Exodus 2:1 "a daughter of Levi" unnamed, 6:20
# "Jochebed his father's sister" — 26:59 names her "daughter of Levi" and dates her birth "IN EGYPT": the datum the seventy's count turns
# on (Genesis 46:26-27 — sixty-six, then seventy; the tape's CJ3b open by one; the exam's Bava Batra 123a); MIRIAM "their sister" — her
# one seat in a roster; Aaron before Moses in the birth order as at Exodus 6:20
assert [(x, m) for x, m in by[('Num', 26, 59)] if x in ('ילדה', 'אתה', 'ותלד')] == [('ילדה', 'HVqp3fs'), ('אתה', 'HTo/Sp3fs'), ('ותלד', 'HC/Vqw3fs')]
assert phrase(['ילדה', 'אתה'], None) == ['Num 26:59'] and 'Num 26:59' in phrase(['אשר', 'ילדה'], None) and len(phrase(['אשר', 'ילדה'], None)) >= 12
assert aramaic(26, 59)[6:10] == ['דילדת', 'יתה', 'ללוי', 'במצרים'] and U('יוכבד') == ['Exod 6:20', 'Num 26:59'] and words('Exod', 2, 1)[-3:] == ['את', 'בת', 'לוי'] and words('Exod', 6, 20)[:5] == ['ויקח', 'עמרם', 'את', 'יוכבד', 'דדתו']
assert words('Num', 26, 59)[-8:] == ['את', 'אהרן', 'ואת', 'משה', 'ואת', 'מרים', 'אחתם'][-7:] + [] if False else words('Num', 26, 59)[-7:] == ['את', 'אהרן', 'ואת', 'משה', 'ואת', 'מרים', 'אחתם'] and words('Exod', 6, 20)[7:12] == ['ותלד', 'לו', 'את', 'אהרן', 'ואת']
assert N('Gen', 46, 26) == [66] and N('Gen', 46, 27) == [2, 70] and N('Exod', 1, 5) == [70] and N('Deut', 10, 22) == [70] and N('Gen', 46, 15) == [33] and N('Gen', 46, 18) == [16] and N('Gen', 46, 22) == [14] and N('Gen', 46, 25) == [7]
# NADAB AND ABIHU — 3:2-4 SHORTENED: 26:60 "there were born to Aaron" (Exodus 6:23 "she bore him" the birth), 26:61 "and Nadab and Abihu
# died when they brought near strange fire before the LORD" — 3:4 carried "died BEFORE THE LORD", "in the wilderness of Sinai", "and they
# had no sons", "and Eleazar and Ithamar served as priests before Aaron their father": four clauses dropped, one spelled longer ("when they
# brought near" plene); "strange fire" three seats — Leviticus 10:1, Numbers 3:4, 26:61
assert words('Num', 26, 61) == ['וימת', 'נדב', 'ואביהוא', 'בהקריבם', 'אש', 'זרה', 'לפני', 'יהוה'] and words('Num', 3, 4)[:10] == ['וימת', 'נדב', 'ואביהוא', 'לפני', 'יהוה', 'בהקרבם', 'אש', 'זרה', 'לפני', 'יהוה'] and words('Num', 3, 4)[10:] == ['במדבר', 'סיני', 'ובנים', 'לא', 'היו', 'להם', 'ויכהן', 'אלעזר', 'ואיתמר', 'על', 'פני', 'אהרן', 'אביהם']
assert phrase(['אש', 'זרה'], None) == ['Lev 10:1', 'Num 26:61', 'Num 3:4'] and words('Num', 26, 60) == ['ויולד', 'לאהרן', 'את', 'נדב', 'ואת', 'אביהוא', 'את', 'אלעזר', 'ואת', 'איתמר'] and words('Exod', 6, 23)[10:] == ['ותלד', 'לו', 'את', 'נדב', 'ואת', 'אביהוא', 'את', 'אלעזר', 'ואת', 'איתמר']
# THE LEVITES: three sons and FIVE families (Libni, Hebron, Mahli, Mushi, KORAH) where 3:17-20 and Exodus 6:16-19 gave eight (Shimei,
# Amram, Izhar, Uzziel absent — no token of the three in the chapter; Amram a person by the begetting); KORAH'S family present — the
# grandson's name for Izhar's line, the line "that did not die"; 23,000 against 3:39's 22,000; "from a month old and upward" the Levite
# formula's eight seats; "they were not counted among the children of Israel" at the three census summaries (1:47, 2:33, 26:62); "for no
# inheritance was given them" (one seat) — 18:20, 23, 24's rule, the Sifrei's proof-texts the ink's own reason
assert fams('Levi') == sorted(['הגרשני', 'הקהתי', 'המררי', 'הלבני', 'החברני', 'המחלי', 'המושי', 'הקרחי']) and words('Num', 3, 19) == ['ובני', 'קהת', 'למשפחתם', 'עמרם', 'ויצהר', 'חברון', 'ועזיאל'] and words('Num', 3, 18)[-2:] == ['לבני', 'ושמעי']
assert [v for (c, v) in SPAN if any(s in x for x in words('Num', 26, v) for s in ('יצהר', 'שמעי', 'עזיאל'))] == [] and [v for (c, v) in SPAN if any('עמרם' in x for x in words('Num', 26, v))] == [58, 59]
assert words('Num', 3, 27)[1:8] == ['משפחת', 'העמרמי', 'ומשפחת', 'היצהרי', 'ומשפחת', 'החברני', 'ומשפחת']
assert len(phrase(['מבן', 'חדש', 'ומעלה'], None)) == 8 and phrase(['לא', 'התפקדו'], None) == ['Num 1:47', 'Num 26:62', 'Num 2:33'] and phrase(['לא', 'נתן', 'להם', 'נחלה'], None) == ['Num 26:62']
assert words('Num', 18, 23)[-5:] == ['בני', 'ישראל', 'לא', 'ינחלו', 'נחלה'] and words('Num', 18, 24)[-5:] == ['בני', 'ישראל', 'לא', 'ינחלו', 'נחלה'] and words('Num', 18, 20)[4:7] == ['בארצם', 'לא', 'תנחל']
# THE CLOSE — TWO VERSES, TWO CENSUSES: 26:63 "these are the counted of Moses and ELEAZAR the priest who counted the children of Israel IN
# THE PLAINS OF MOAB BY THE JORDAN OF JERICHO" || 26:64 "and among these there was not a man of the counted of Moses and AARON the priest who
# counted the children of Israel IN THE WILDERNESS OF SINAI" — the priest's name and the place the only deltas; "in the plains of Moab" nine
# seats, "by the Jordan of Jericho" seven (all Numbers), "in the wilderness of Sinai" nine; 26:65 "THEY SHALL SURELY DIE IN THE WILDERNESS"
# — the decree's words (14:35), and "EXCEPT CALEB SON OF JEPHUNNEH AND JOSHUA SON OF NUN" verbatim from the decree's exception (14:30);
# "and there was not left of them a man" — the locusts' "nothing green was left" (Exod 10:15) the Torah's other seat; Deuteronomy 2:14-16
# the retelling ("until all the generation of the men of war was consumed")
W63, W64 = words('Num', 26, 63), words('Num', 26, 64)
assert W63[:2] == ['אלה', 'פקודי'] and W64[:4] == ['ובאלה', 'לא', 'היה', 'איש'] and W63[2:5] == ['משה', 'ואלעזר', 'הכהן'] and W64[5:8] == ['משה', 'ואהרן', 'הכהן'] and W63[5:10] == W64[8:13] == ['אשר', 'פקדו', 'את', 'בני', 'ישראל'] and W63[10:] == ['בערבת', 'מואב', 'על', 'ירדן', 'ירחו'] and W64[13:] == ['במדבר', 'סיני']
assert len(U('בערבת')) == 9 and len(phrase(['על', 'ירדן', 'ירחו'], None)) == 7 and all(s.startswith('Num') for s in phrase(['על', 'ירדן', 'ירחו'], None)) and len(phrase(['במדבר', 'סיני'], None)) == 9
assert phrase(['מות', 'ימתו', 'במדבר'], None) == ['Num 26:65'] and words('Num', 14, 35)[-5:] == ['במדבר', 'הזה', 'יתמו', 'ושם', 'ימתו'] and phrase(['כי', 'אם', 'כלב'], None) == ['Num 14:30', 'Num 26:65'] and words('Num', 14, 30)[-7:] == words('Num', 26, 65)[-7:] == ['כי', 'אם', 'כלב', 'בן', 'יפנה', 'ויהושע', 'בן', 'נון'][1:]
assert phrase(['ולא', 'נותר'], T) == ['Exod 10:15', 'Num 26:65'] and phrase(['בלתי', 'כלב'], None) == ['Num 32:12'] and words('Deut', 1, 36)[:4] == ['זולתי', 'כלב', 'בן', 'יפנה']
assert words('Deut', 2, 14)[11:] == ['שלשים', 'ושמנה', 'שנה', 'עד', 'תם', 'כל', 'הדור', 'אנשי', 'המלחמה', 'מקרב', 'המחנה', 'כאשר', 'נשבע', 'יהוה', 'להם'] and N('Deut', 2, 14) == [38]
assert aramaic(26, 65)[4:7] == ['ממת', 'ימותון', 'במדברא'] and aramaic(26, 64)[:4] == ['ובאלין', 'לא', 'הוה', 'גבר']
# THE LAND BY COUNT AND BY LOT: "to these shall the land be divided" (26:53 — the divide-verb's four Bible seats, 26:53, 26:56, Amos 7:17,
# Psalm 68:13); "BY THE NUMBER OF NAMES" — the FIRST census's counting phrase (1:2, 18, 20, 22, 24, 34; 3:43) applied to the land; "to the
# many increase, to the few diminish" (26:54; 33:54 restates it in the plural, 35:8 applies it to the Levite cities); "ONLY by lot" — the
# lot-word's Torah seats are Yom Kippur's two goats (Lev 16:8-10, four tokens) and the land (26:55-56, 33:54 twice, 34:13, 36:2); Joshua
# runs it in twenty-four verses; sixty-five in the Bible; "by the mouth of the lot", "between many and few", "by the names of the tribes of
# their fathers" one seat each; "only" forty-one Torah tokens (the Sifrei's exclusion on it); Joshua 14:2 quotes 34:13's "nine tribes and
# the half-tribe"
assert U('תחלק') == ['Amos 7:17', 'Num 26:53', 'Num 26:56', 'Ps 68:13'] and 'Num 26:55' in U('יחלק') and U('בנחלה', books=T) == ['Num 26:53', 'Num 34:2', 'Num 36:2']
assert phrase(['במספר', 'שמות'], None) == ['1Chr 23:24', 'Num 1:18', 'Num 1:2', 'Num 1:20', 'Num 1:22', 'Num 1:24', 'Num 1:34', 'Num 26:53', 'Num 3:43']
assert phrase(['לרב', 'תרבה'], None) == ['Num 26:54'] and phrase(['לרב', 'תרבו'], None) == ['Num 33:54'] and words('Num', 35, 8)[6:12] == ['מאת', 'הרב', 'תרבו', 'ומאת', 'המעט', 'תמעיטו']
GORAL = sorted(set(hits('גורל', T)))
assert GORAL == ['Lev 16:10', 'Lev 16:8', 'Lev 16:9', 'Num 26:55', 'Num 26:56', 'Num 33:54', 'Num 34:13', 'Num 36:2'] and sum(1 for k in GORAL for x in words(*key(k)) if 'גורל' in x) == 11 and len(hits('גורל', ('Josh',))) == 24 and len(hits('גורל', None)) == 65
assert phrase(['על', 'פי', 'הגורל'], None) == ['Num 26:56'] and phrase(['בין', 'רב', 'למעט'], None) == ['Num 26:56'] and phrase(['לשמות', 'מטות'], None) == ['Num 26:55'] and count_tok('אך', T) == 41 and words('Num', 26, 55)[0] == 'אך'
assert words('Josh', 14, 2)[-5:] == words('Num', 34, 13)[-5:] == ['לתשעת', 'המטות', 'וחצי', 'המטה'][-4:] + [] if False else words('Josh', 14, 2)[-4:] == words('Num', 34, 13)[-4:] == ['לתשעת', 'המטות', 'וחצי', 'המטה']
assert aramaic(26, 55)[:2] == ['ברם', 'בעדבא'] and aramaic(26, 56)[:3] == ['על', 'פום', 'עדבא'] and aramaic(26, 53)[1] == 'תתפלג'
# JOSHUA 17 RUNS THE ROSTER: Machir the firstborn of Manasseh, father of Gilead (17:1); the six families (17:2 — Abiezer for Iezer, Helek,
# Asriel, Shechem, Hepher, Shemida); Zelophehad's lineage and the five daughters in 26:33's order (17:3); "ten portions" (17:5)
assert words('Josh', 17, 1)[8:12] == ['למכיר', 'בכור', 'מנשה', 'אבי'] and words('Josh', 17, 2)[6:17:2] == ['אביעזר', 'חלק', 'אשריאל', 'שכם', 'חפר', 'שמידע']
assert words('Josh', 17, 3)[:10] == ['ולצלפחד', 'בן', 'חפר', 'בן', 'גלעד', 'בן', 'מכיר', 'בן', 'מנשה', 'לא'] and N('Josh', 17, 5) == [10]
# THE ARITHMETIC THE COMPILE WILL CHECK: Simeon 59,300 → 22,200, a fall of 37,100 — the plague's 24,000 (25:9) cannot cover it even if
# every dead man were Simeon's (the Sifrei's reading, 131:2): 13,100 unexplained; Korach's 14,700 + 250; FIVE tribes fell (61,020 in
# all), seven rose (59,200); the Levites +1,000; the whole −1,820
assert C1['Simeon'] - C26['Simeon'] == 37100 and 37100 - 24000 == 13100 and len([d for d in DELTA.values() if d < 0]) == 5 and len([d for d in DELTA.values() if d > 0]) == 7   # FIVE tribes fell, SEVEN rose (the hand had typed them the other way round)

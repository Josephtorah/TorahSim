#!/usr/bin/env python3
# THE DEUTERONOMY WALK, sitting 4 — CHAPTER 6, Deuteronomy 6:1-25 (2026-09-17; the owner: "ok lets start the next chapter"; RUN 1 of four —
# the rereads, the measurements, the ink, the design): THE INK of the chapter, computed from the Tanakh DB, the snapshot store and the shelf's own
# bytes — never typed. Sitting 3's form (ch5_ink.py): the scaffold cut by anchors, the constants and every assert chapter 6's own, typed FROM
# THE PRINTS (ch6_dump0.out, ch6_measure1.out). THE TWO DIVISIONS AGREE (25 = 25; the alignment the identity, cost 12). THE SPINE LANDS ON THE
# CHAPTER: piskaot 31-36 head on 6:4-9, one per verse of the Shema — 67 rows, the first on-chapter piskaot since chapter 3; three rows read at
# Genesis sittings CREDITED; EIGHT rows elsewhere cite the chapter (38:10, 41:14, 41:20, 104:8 the translator's note, 201:3, 258:1, 306:37, 355:27
# the Hebrew's "ibid." form) and one row cites "Dt.6:27" for Numbers 6:27 — the English export's slip, EXCLUDED. The parser MEASURED on every
# verse — ONE number verse, 6:4 "one" [1]; the seven-stem homographs refused; NO GAP. The store = the DB at every verse (318 tokens). The hand's
# facts as asserts, run all at once by assert_driver.py after the measurement passes printed them.
import json, os, re, html, sqlite3, sys, io, contextlib, unicodedata, subprocess
from collections import Counter
ROOT = subprocess.check_output(['git', 'rev-parse', '--show-toplevel'], text=True).strip()
DATE = '2026-09-17'
CH = 6
UIDS = ['deu_06_shema']
SPANS = {'deu_06_shema': (6, 1, 25)}
PREFIX = {'deu_06_shema': 'DV06'}
PISKAOT = [31, 32, 33, 34, 35, 36]   # the spine ON the chapter: the heads on 6:4, 6:5, 6:6, 6:7, 6:8, 6:9 (typed from ch6_dump0's A print)
SPINE_ROWS = {31: 10, 32: 21, 33: 4, 34: 10, 35: 12, 36: 10}   # rows per piska, both files (the print)
EXP2DB = {e: [e] for e in range(1, 26)}   # the identity — 25 = 25 (chapter 5 the book's one split)
DB2EXP = {d: e for e, ds in EXP2DB.items() for d in ds}
OUTSIDE_HE = [(38, 10, (6, 11)), (38, 10, (6, 11)), (38, 10, (6, 11)), (41, 14, (6, 4)), (41, 20, (6, 5)), (201, 3, (6, 11)), (306, 37, (6, 4))]   # the Hebrew's book-named citations of chapter 6 OUTSIDE the spine (the spine's own 31:1-36:1 and 33:1 aside)
OUTSIDE = [(38, 10), (41, 14), (41, 20), (104, 8), (201, 3), (258, 1), (306, 37), (355, 27)]   # the eight rows READ: the union of both files beyond piskaot 31-36, less the excluded slip
EXCLUDED = [(62, 4)]   # the English export cites '(Dt.6:27)' where the Hebrew cites Numbers 6:27 (the priestly blessing's 'My Name') — a slip, no verse 6:27 exists
CITED_DB = {(38, 10): 11, (41, 14): 4, (41, 20): 5, (104, 8): 1, (201, 3): 11, (258, 1): 4, (306, 37): 4, (355, 27): 4}   # the DB verse each outside row cites (104:8 the translator's '6:1ff.'; 355:27 the Hebrew's 'ibid.' after Deuteronomy 33:26)
FRESH = OUTSIDE[:]   # none of the eight read before (the prior-reads census)
CREDITED = {(32, 2): 'read at gen_27_the_call_2026-08-25.md (Abraham\'s converts — the souls made in Haran)', (36, 10): 'read at gen_29_separation_promise_2026-08-25.md', (33, 4): 'read at gen_30_war_of_kings_2026-08-25.md (Abram\'s oath, Genesis 14:22-23)'}   # spine rows read at Genesis sittings
TITLE = 'Chapter 6 — And this is the commandment, the statutes and the judgments which the LORD your God commanded to teach you: hear, O Israel, the LORD our God, the LORD is one; you shall love the LORD your God with all your heart, all your soul and all your might; these words on your heart, taught to your children, bound on the hand, between the eyes, written on the doorposts; when the LORD brings you into the land sworn to the fathers — take heed lest you forget; fear, serve, swear by His name; do not test as at Massah; do the right and the good; and when your son asks tomorrow, the answer: we were slaves to Pharaoh, and the LORD brought us out'
OUT = f'{ROOT}/logic/oral_triage/deu_06_vaetchanan_{DATE}.md'

def clean(s): return re.sub(r'<[^>]+>', '', html.unescape(s))
sif = json.load(open(f'{ROOT}/Data/sefaria_export/Sifrei_Devarim/en.json', encoding='utf-8'))['text']
sif_he = json.load(open(f'{ROOT}/Data/sefaria_export/Sifrei_Devarim/he.json', encoding='utf-8'))['text']
onk = json.load(open(f'{ROOT}/Data/sefaria_export/Onkelos_Deuteronomy/en.json', encoding='utf-8'))['text']
onk_he = json.load(open(f'{ROOT}/Data/sefaria_export/Onkelos_Deuteronomy/he.json', encoding='utf-8'))['text']
HN = {'א': 1, 'ב': 2, 'ג': 3, 'ד': 4, 'ה': 5, 'ו': 6, 'ז': 7, 'ח': 8, 'ט': 9, 'י': 10, 'כ': 20, 'ל': 30, 'מ': 40, 'נ': 50, 'ס': 60, 'ע': 70, 'פ': 80, 'צ': 90, 'ק': 100, 'ר': 200, 'ש': 300, 'ת': 400}
def hn(s): return sum(HN[c] for c in s if c in HN)
def E(p, r): return clean(sif[p - 1][r - 1])
def Hb(p, r): return clean(sif_he[p - 1][r - 1])
heads = {}
for p in range(1, 358):
    m = re.match(r'\(דברים ([א-ת]+) ([א-ת]+)(?:-[א-ת]+)?\)', Hb(p, 1))
    heads[p] = (hn(m.group(1)), hn(m.group(2))) if m else None
def head(p): return heads[p]
# THE SHELF BY POSITION — the two files' grains, the heads around chapter 6: SIX piskaot ON the chapter (31-36 on 6:4-9), 30 on 3:29 before them, 37 on 11:10 after
assert len(sif) == 357 and len(sif_he) == 357 and sum(len(s) for s in sif) == 2357 and sum(len(s) for s in sif_he) == 2357
assert {p: heads[p] for p in range(30, 38)} == {30: (3, 29), 31: (6, 4), 32: (6, 5), 33: (6, 6), 34: (6, 7), 35: (6, 8), 36: (6, 9), 37: (11, 10)}, {p: heads[p] for p in range(30, 38)}
HC = Counter(h[0] for h in heads.values() if h)
assert [p for p, h in heads.items() if h and h[0] == 6] == PISKAOT and HC[6] == 6 and HC[4] == 0 and HC[5] == 0 and sorted(HC.items())[:8] == [(1, 24), (3, 4), (6, 6), (11, 21), (12, 20), (13, 14), (14, 14), (15, 16)], sorted(HC.items())[:8]
assert {p: (len(sif_he[p - 1]), len(sif[p - 1])) for p in PISKAOT} == {p: (n, n) for p, n in SPINE_ROWS.items()} and sum(SPINE_ROWS.values()) == 67
def he_cites(t): return [(b, hn(c), hn(v)) for b, c, v in re.findall(r'\(([א-ת]+(?: [א-ת])?) ([א-ת]{1,3}) ([א-ת]{1,3})\)', t)]
CIT_HE = [(p, r, (6, c[2])) for p in range(1, 358) for r in range(1, len(sif_he[p - 1]) + 1) for c in he_cites(Hb(p, r)) if c[0] == 'דברים' and c[1] == 6]
CIT_EN = [(p, r, (6, int(m.group(2)))) for p in range(1, 358) for r in range(1, len(sif[p - 1]) + 1) for m in re.finditer(r'\((?:Deut(?:eronomy)?\.?|Dt\.?|Devarim) ?(6):(\d+)', E(p, r))]
SPINE_CITES_HE = [(31, 1, (6, 4)), (32, 1, (6, 5)), (33, 1, (6, 6)), (33, 1, (6, 5)), (34, 1, (6, 7)), (35, 1, (6, 8)), (36, 1, (6, 9))]
assert CIT_HE == SPINE_CITES_HE + OUTSIDE_HE and len(CIT_HE) == 14, CIT_HE
UNION = [(31, 1), (31, 6), (31, 7), (31, 8), (31, 10), (32, 1), (32, 2), (32, 5), (32, 6), (32, 7), (33, 1), (33, 2), (34, 1), (34, 2), (34, 3), (34, 4), (34, 6), (34, 8), (35, 1), (35, 2), (35, 3), (35, 4), (35, 5), (35, 6), (35, 7), (35, 8), (35, 9), (35, 10), (35, 11), (35, 12), (36, 1), (36, 2), (36, 3), (36, 5), (36, 6), (36, 7), (36, 8), (38, 10), (41, 14), (41, 20), (62, 4), (104, 8), (201, 3), (258, 1), (306, 37), (355, 27)]
assert len(CIT_EN) == 69 and sorted({(p, r) for p, r, _ in CIT_EN}) == UNION and sorted({(p, r) for p, r, _ in CIT_HE} | {(p, r) for p, r, _ in CIT_EN}) == UNION and len(UNION) == 46
assert sorted(set(UNION) - {(p, r) for p, r in UNION if p in PISKAOT}) == sorted(OUTSIDE + EXCLUDED) and len(OUTSIDE) == 8
assert [(p, r) for p in range(1, 358) for r in range(1, len(sif[p - 1]) + 1) if re.search(r'\((?:Ibid|ibid)\.? ?6:\d+\)', E(p, r))] == []
assert {p: heads[p] for p, _ in OUTSIDE + EXCLUDED} == {38: (11, 10), 41: (11, 13), 104: (14, 21), 201: (20, 15), 258: (23, 15), 306: (32, 1), 355: (33, 20), 62: (12, 5)}, {p: heads[p] for p, _ in OUTSIDE + EXCLUDED}
def has_points(s): return any(0x05B0 <= ord(c) <= 0x05BD for c in s)
assert all(has_points(Hb(p, r)) for p, r in OUTSIDE) and all(has_points(Hb(p, r)) for p in PISKAOT for r in range(1, SPINE_ROWS[p] + 1))
# THE EXCLUDED SLIP: 62:4 (on 12:5, 'to make His Name dwell') — the Hebrew cites Numbers 6:27 twice by name; the English cites (Nu.6:27) and then (Dt.6:27) — a wrong book, no such verse
assert he_cites(Hb(62, 4)) == [('במדבר', 6, 27), ('שמות', 20, 21)] and E(62, 4).count('(Nu.6:27)') == 2 and '(Dt.6:27)' in E(62, 4)
# THE TRANSLATOR'S NOTE: 104:8 (on 14:21, the kid in its mother's milk) — 'three covenants … once at Horeb (Dt.6:1ff.)' the English's own identification, the Hebrew citing no verse; marked an interpolation (F:163 n.9)
assert [c for c in he_cites(Hb(104, 8)) if c[0] == 'דברים'] == [] and 'Once at Horeb (Dt.6:1ff.)' in E(104, 8) and 'interpolation' in E(104, 8) and 'שָׁלֹשׁ בְּרִיתוֹת' in Hb(104, 8)
# THE HEBREW'S 'IBID.': 355:27 (on 33:26) cites 6:4 as (שם ו ד) after (דברים לג כו) — the book-name regex misses it; the English (Dt.6:4) catches it. 258:1 names the Shema as a text (את שמע), the English citing 6:4 ff.
assert '(שם ו ד)' in Hb(355, 27) and '(דברים לג כו)' in Hb(355, 27) and '(Dt.6:4)' in E(355, 27) and 'שְׁמַע יִשְׂרָאֵל' in Hb(355, 27) and '(דהי״א יז כא)' in Hb(355, 27)
assert 'אֶת שְׁמַע' in Hb(258, 1) and '(Dt.6:4 ff.)' in E(258, 1) and 'M. Ber. 3:5' in E(258, 1) and 'וּתְפִלִּין' in Hb(258, 1)
assert Hb(38, 10).count('(דברים ו יא)') == 3 and E(38, 10).count('(Dt.6:11)') == 4 and '(דברים ו ד)' in Hb(41, 14) and '(דברים ו ה)' in Hb(41, 20) and E(41, 20).count('(Dt.6:5)') == 3 and '(דברים ו יא)' in Hb(201, 3) and '(דברים ו ד)' in Hb(306, 37)
# THE SPINE'S OWN CITATIONS (the rows' Hebrew, by name): piska 31 reaches Genesis 21, 28, 35, 37, 47, Exodus 25, 34, Numbers 11, Ezekiel 33, Zechariah 8, 14, Jeremiah 32, Psalm 50; the rows with no citation in either file eight
assert he_cites(Hb(31, 1))[:2] == [('דברים', 6, 4), ('שמות', 25, 2)] and he_cites(Hb(31, 10)) == [('זכריה', 14, 9)] and he_cites(Hb(31, 6))[2] == ('דברים', 33, 6) and he_cites(Hb(32, 1)) == [('דברים', 6, 5), ('דברים', 10, 20)] and he_cites(Hb(33, 1)) == [('דברים', 6, 6), ('דברים', 6, 5)]
NOCITE = [(p, r) for p in PISKAOT for r in range(1, SPINE_ROWS[p] + 1) if not he_cites(Hb(p, r)) and not re.findall(r'\([A-Z][a-z]+\.? ?\d+:\d+', E(p, r))]
assert NOCITE == [(32, 3), (32, 4), (32, 8), (32, 11), (32, 13), (33, 3), (34, 9), (34, 10)], NOCITE
# THE PRIOR READS — the strict row form over every ledger: three SPINE rows read at Genesis sittings, none of the eight outside rows
TRI = f'{ROOT}/logic/oral_triage'
LED = {f: open(f'{TRI}/{f}', encoding='utf-8').read() for f in os.listdir(TRI) if f.endswith('.md') and os.path.isfile(f'{TRI}/{f}') and f'{TRI}/{f}' != OUT}
PRIOR = sorted({(f, int(a), int(b)) for f, t in LED.items() for a, b in re.findall(r'Sifrei Devarim (\d+):(\d+)', t)})
assert [(f, p, r) for f, p, r in PRIOR if p in PISKAOT] == [('gen_27_the_call_2026-08-25.md', 32, 2), ('gen_29_separation_promise_2026-08-25.md', 36, 10), ('gen_30_war_of_kings_2026-08-25.md', 33, 4)] and sorted((p, r) for _, p, r in PRIOR if p in PISKAOT) == sorted(CREDITED) and [(f, p, r) for f, p, r in PRIOR if (p, r) in OUTSIDE + EXCLUDED] == [] and len(PRIOR) == 219, len(PRIOR)
assert sorted(f for f, t in LED.items() if re.search(r'^- Onkelos Deut 6:', t, re.M)) == [] and sorted(f for f, t in LED.items() if re.search(r'^- Onkelos Exod 13:', t, re.M)) == []   # no Onkelos row of the chapter or of its Exodus kin anywhere
NAMING = sorted(f for f, t in LED.items() if re.search(r'Deut(?:eronomy)? 6:\d+', t))
assert NAMING == ['exodus_block_matza_2026-09-04.md', 'gen_72_testament_twelve_2026-08-28.md', 'num_15_offerings_laws_2026-09-10.md', 'num_27_zelophehad_joshua_2026-09-09.md', 'num_35_refuge_cities_2026-09-13.md'], NAMING
assert re.search(r'^\| \d+ \| Sifrei Devarim 32:2 \| dup-of:row 46 \|', LED['gen_27_the_call_2026-08-25.md'], re.M) and re.search(r'^\| \d+ \| Sifrei Devarim 36:10 \| \*\*material\*\* \|', LED['gen_29_separation_promise_2026-08-25.md'], re.M) and re.search(r'^\| \d+ \| Sifrei Devarim 33:4 \| \*\*material\*\* \|', LED['gen_30_war_of_kings_2026-08-25.md'], re.M)   # the Genesis ledgers' TABLE row form (32:2 a duplicate row there)
assert sum(len(re.findall(r'Mekhilta[^\n]{0,40}13:\d+', t)) for t in LED.values()) == 3
def plain(w): return ''.join(c for c in w if c != '/' and not (0x0591 <= ord(c) <= 0x05C7))
def pointed(w): return ''.join(c for c in w if c != '/' and not (0x0591 <= ord(c) <= 0x05AF))
def NF(s): return unicodedata.normalize('NFC', s)
ONK_LEN = {c: len(onk[c - 1]) for c in (3, 4, 5, 6)}
assert len(onk) == 34 and len(onk_he) == 34 and ONK_LEN == {3: 29, 4: 49, 5: 30, 6: 25} and sum(len(c) for c in onk_he) == 956
def onk_ev(c, v):
    """an Onkelos row by the DB's verse — the export's row found through the map (chapter 5's 17-20 share the export's 17)"""
    e = DB2EXP[v] if c == 5 else v
    return clean(onk[c - 1][e - 1]), clean(onk_he[c - 1][e - 1])
shelf_deut = sorted(d for d in os.listdir(f'{ROOT}/Data/sefaria_export') if re.search(r'Deuteronomy|Devarim', d))
outside = [d for d in shelf_deut if d not in ('Sifrei_Devarim', 'Onkelos_Deuteronomy')]
assert len(shelf_deut) == 28 and len(outside) == 26, len(outside)

# ---- THE DRAFT'S SPAN, COMPUTED ----
db = sqlite3.connect(f'file:{ROOT}/Data/tanakh.sqlite?mode=ro', uri=True)
VC = dict(db.execute("SELECT chapter, COUNT(*) FROM verses WHERE book='Deut' GROUP BY chapter").fetchall())
assert VC[5] == 33 and VC[4] == 49 and VC[6] == 25 and sum(VC.values()) == 959 and len(VC) == 34
assert [(c, len(onk_he[c - 1]), VC[c]) for c in range(1, 35) if len(onk_he[c - 1]) != VC[c]] == [(5, 30, 33)]
# THE ALIGNMENT RECOMPUTED (ch6_dump0's A0): the export's twenty-five rows against the DB's twenty-five verses over token and negation counts — the identity, cost 12
by6 = {v: [plain(he) for he, in db.execute("SELECT w.he FROM words w JOIN verses v ON w.verse_id=v.id WHERE v.book='Deut' AND v.chapter=6 AND v.verse=? ORDER BY w.idx", (v,))] for v in range(1, 26)}
NEG = ('לא', 'ולא')
D_ = [(len(by6[v]), sum(1 for x in by6[v] if x in NEG)) for v in range(1, 26)]
E_ = [(len(plain(clean(r)).split()), sum(1 for x in plain(clean(r)).split() if x.strip('.:') in NEG)) for r in onk_he[5]]
def _cost(e, ds): return abs(e[0] - sum(d[0] for d in ds)) + 3 * abs(e[1] - sum(d[1] for d in ds))
INF = 10 ** 9; best = {(0, 0): (0, None)}
for i in range(1, 26):
    for j in range(i, 26):
        cands = [(best[(i - 1, k)][0] + _cost(E_[i - 1], D_[k:j]), k) for k in range(i - 1, j) if (i - 1, k) in best and j - k <= 4]
        best[(i, j)] = min(cands) if cands else (INF, None)
i, j, ALIGN = 25, 25, {}
while i > 0:
    k = best[(i, j)][1]; ALIGN[i] = list(range(k + 1, j + 1)); i, j = i - 1, k
assert ALIGN == EXP2DB and best[(25, 25)][0] == 12 and Counter(ds[0] - e for e, ds in EXP2DB.items()) == Counter({0: 25}) and len(onk_he[5]) == 25 == VC[6], (best[(25, 25)][0], ALIGN)
def unit_text(uid): return open(f'{ROOT}/logic/units/{uid}.yaml', encoding='utf-8').read()
def steps(uid): return sorted({(int(a), int(b)) for a, b in re.findall(r'STEP_Dt_(\d+)_(\d+)', unit_text(uid))})
FIRST = not os.path.exists(OUT)
for uid, (c, lo, hi) in SPANS.items():
    t = unit_text(uid)
    assert steps(uid) == [(c, v) for v in range(lo, hi + 1)] and re.search(rf'refs: "?{c}:{lo}-{hi}"?', t) and '\nbinary_trees:' in t, uid
    if FIRST: assert 'status: draft' in t and 'operators:' not in t and '- step: E' not in t, uid
    assert t.count(f'  - id: STEP_Dt_{c}_{lo}\n') == 1 and t.count(f'  - id: STEP_Dt_{c}_{hi}\n') == 1, uid
assert unit_text('deu_06_shema').count('    comment: >\n') == 54 and unit_text('deu_06_shema').count('\n  - id: S') == 32   # typed from the pre-build print (two per step and four of the log; the scenarios)
assert 'deu_05_decalogue' in unit_text('deu_06_shema') and steps('deu_07_nations_cherem')[0] == (7, 1)
assert sorted(f for f in os.listdir(TRI) if f.startswith('deu_') and f != os.path.basename(OUT)) == ['deu_01_03_devarim_2026-09-15.md', 'deu_01_03_devarim_exam_2026-09-15.md', 'deu_04_vaetchanan_2026-09-16.md', 'deu_04_vaetchanan_exam_2026-09-16.md', 'deu_05_vaetchanan_2026-09-16.md', 'deu_05_vaetchanan_exam_2026-09-16.md']
ALLTXT = ''.join(open(f'{ROOT}/logic/units/{f}', encoding='utf-8').read() for f in os.listdir(f'{ROOT}/logic/units') if f.endswith('.yaml') and f[:-5] not in UIDS) + ''.join(open(f'{ROOT}/logic/oral_audit/manifests/{f}', encoding='utf-8').read() for f in os.listdir(f'{ROOT}/logic/oral_audit/manifests') if f.endswith('.json') and f[:-12] not in UIDS)
assert all(f'"{p}-' not in ALLTXT and f'[claim {p}-' not in ALLTXT for p in PREFIX.values())
SPAN = [(6, v) for v in range(1, VC[6] + 1)]
NV = 25
assert len(SPAN) == NV

# ---- THE INK, computed from the Tanakh DB and the snapshot store ----
rows = db.execute("SELECT v.book, v.chapter, v.verse, w.he, w.morph, w.lemma, w.wtype FROM words w JOIN verses v ON w.verse_id=v.id ORDER BY v.id, w.idx").fetchall()
by, byp, byl, byw = {}, {}, {}, {}
for b, c, v, he, m, lem, wt in rows:
    by.setdefault((b, c, v), []).append((plain(he), m)); byp.setdefault((b, c, v), []).append(pointed(he)); byl.setdefault((b, c, v), []).append((lem or '').split('/')[-1].strip()); byw.setdefault((b, c, v), []).append(wt)
T = ('Gen', 'Exod', 'Lev', 'Num', 'Deut')
def words(b, c, v): return [x for x, _ in by[(b, c, v)]]
def morphs(b, c, v): return [m for _, m in by[(b, c, v)]]
def wm(b, c, v): return list(zip(words(b, c, v), morphs(b, c, v)))
def hits(sub, books=None, exact=False): return sorted({f'{b} {c}:{v}' for (b, c, v), ws in by.items() if (books is None or b in books) and any((x == sub) if exact else (sub in x) for x, _ in ws)})
def phrase(seq, books=T):
    out = []
    for (b, c, v), ws in by.items():
        if books is not None and b not in books: continue
        w = [x for x, _ in ws]
        if any(w[i:i + len(seq)] == list(seq) for i in range(len(w) - len(seq) + 1)): out.append(f'{b} {c}:{v}')
    return sorted(out)
def P(*seq, books=None): return phrase(list(seq), books)
def S_(*x): return sorted(x)
def U(*toks, books=None): return sorted(set(s for t in toks for s in hits(t, books, True)))
def LEMT(lem, books=None): return [(f'{b} {c}:{v}', x, m) for (b, c, v), ws in by.items() if (books is None or b in books) for (x, m), l in zip(ws, byl[(b, c, v)]) if l == lem]
def LEMV(lem, books=None): return sorted({s for s, _, _ in LEMT(lem, books)})
def lemma_of(b, c, v, tok): return [l for (x, m), l in zip(by[(b, c, v)], byl[(b, c, v)]) if x == tok]
def W6(v): return words('Deut', 6, v)
def PT(b, c, v, tok): return [NF(x) for x in byp[(b, c, v)] if plain(x) == tok]
def DIFF(a, b_):
    import difflib
    A, B = words(*a), words(*b_)
    return [(op, A[i1:i2], B[j1:j2]) for op, i1, i2, j1, j2 in difflib.SequenceMatcher(None, A, B).get_opcodes() if op != 'equal']
def SHARED(a, b_):
    import difflib
    A, B = words(*a), words(*b_)
    m = difflib.SequenceMatcher(None, A, B).find_longest_match(0, len(A), 0, len(B))
    return A[m.a:m.a + m.size]
FAIL = []
def H(c, v, *cons):
    w, wp = words('Deut', c, v), byp[('Deut', c, v)]
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
        while j < len(ws) and plain(ws[j]).strip('.:') != k: j += 1
        if j >= len(ws): FAIL.append(('A', c, v, k, [plain(x) for x in ws])); out.append('⟨MISS⟩'); continue
        out.append(ws[j].rstrip('.:')); i = j + 1
    return ' '.join(out)
def aramaic(c, v): return [plain(x).strip('.:') for x in onk_ev(c, v)[1].rstrip(':').split()]
def arm(c, v): return plain(onk_ev(c, v)[1])
def arm_e(c, e): return plain(clean(onk_he[c - 1][e - 1]))
def onk_seats(sub): return [(c + 1, v + 1) for c in range(34) for v in range(len(onk_he[c])) if sub in arm_e(c + 1, v + 1)]      # EXPORT verse numbers (chapter 5's 17 = the DB's 17-20; 18+ = the DB's verse minus three)
def onk_tok(tok): return [(c + 1, v + 1) for c in range(34) for v in range(len(onk_he[c])) if tok in [plain(x).strip('.:') for x in clean(onk_he[c][v]).rstrip(':').split()]]
def HP(c, v, *pieces):
    out = []
    for toks, gloss in pieces:
        assert len(toks) <= 7, (c, v, toks)
        out.append(f'"{H(c, v, *toks)}" ({gloss})')
    return ' '.join(out)
def AP(c, v, *pieces):
    out = []
    for toks, gloss in pieces:
        assert len(toks) <= 7, (c, v, toks)
        out.append(f'{A(c, v, *toks)} ({gloss})')
    return ' '.join(out)
def SP_(p, r, *cons):
    ws = Hb(p, r).split()
    out, i = [], 0
    for k in cons:
        j = i
        while j < len(ws) and plain(ws[j]).strip('.,:;?!"()–-״׳') != k: j += 1
        if j >= len(ws): FAIL.append(('S', p, r, k)); out.append('⟨MISS⟩'); continue
        out.append(ws[j].rstrip('.,:;?!')); i = j + 1
    return ' '.join(out)
store = sqlite3.connect(f'file:{ROOT}/torah_grok.SNAPSHOT-main-51801ca.sqlite?mode=ro', uri=True)
SG = {}
for c, v, idx, hp, g in store.execute("SELECT v.chapter, v.verse, w.idx, w.he_plain, w.gloss FROM words w JOIN verses v ON w.verse_id=v.id WHERE v.book='Deut' AND v.chapter = 6 ORDER BY v.id, w.idx"):
    SG.setdefault((c, v), []).append((idx, hp.replace('/', ''), g))
def sg(c, v, tok, nth=0):
    hit = [g for _, hp, g in SG[(c, v)] if hp == tok]
    if len(hit) <= nth: raise KeyError((c, v, tok, nth))
    return hit[nth]
def sidx(c, v, tok, nth=0):
    hit = [i for i, hp, _ in SG[(c, v)] if hp == tok]
    assert len(hit) > nth, (c, v, tok, nth, hit)
    return hit[nth]
STORE_MISMATCH = [(c, v, n, len(by[('Deut', c, v)])) for c, v, n in store.execute("SELECT v.chapter, v.verse, COUNT(*) FROM words w JOIN verses v ON w.verse_id=v.id WHERE v.book='Deut' AND v.chapter=6 GROUP BY v.chapter, v.verse").fetchall() if n != len(by[('Deut', c, v)])]
# (מצותי "my commandments" — Exodus 20:6's own word): the chapter's one pair; the DB's 1,268 ketiv tokens over the Bible
TOK = sum(len(by[('Deut', 5, v)]) for v in range(1, 34))

# THE ENGINE'S PARSER on every verse — MEASURED before the compile is asked: THREE number verses, NO GAP — 5:13 "six days" [6], 5:14 "the seventh
# day" the ordinal [7], 5:22 "two tablets of stone" [2] (the construct "two" marked ^); 5:9's "the third generation" STARRED — not thirty (rule 15:
# no holam under the lamed; the pointed form שִׁלֵּשִׁים "third-generation ones" at all five seats); 5:10's "to thousands" a bare plural noun (no
# number — the 1b multiplication rule); the same phrases read the same at their other seats (six days [6] at twelve Torah seats; the seventh [7];
# 7:9's "to a thousand generations" [1000]; 9:10 and Exodus 31:18 [2]; 10:4 [10] with the ordinal "the first" [1]; 4:13 [10, 2]).
sys.path.insert(0, f'{ROOT}/World/step9')
with contextlib.redirect_stdout(io.StringIO()):
    import cold_run_sequence as CS
def N(b, c, v): return CS.ink_numbers(CS.verse_words(b, c, v))
def O(b, c, v): return CS.ink_ordinals(CS.verse_words(b, c, v))
PARSED = {(c, v): N('Deut', c, v) for (c, v) in SPAN if N('Deut', c, v)}
# THE STORE = THE DB at every verse (no written-and-read pair in the chapter); 318 tokens, 1,295 letters; the two unglossed tokens both "I" (אנכי, 6:2 and 6:6)
# THE STORE DROPS THE LARGE LETTERS (RESEARCH_LOG 2026-09-09's defect report, which named 6:4 in advance): the Shema's ayin and dalet — the store reads "שמ" for "hear" (שמע) and "אח" for "one" (אחד); the whole-Torah census of a differing token at an equal count is FOUR (6:4's two; Leviticus 11:42's belly; Numbers 27:5's their-case)
assert STORE_MISMATCH == [] and [(v, i, hp, W6(v)[i]) for v in range(1, 26) for i, (_, hp, _) in enumerate(SG[(6, v)]) if hp != W6(v)[i]] == [(4, 0, 'שמ', 'שמע'), (4, 5, 'אח', 'אחד')] and Counter(wt for v in range(1, 26) for wt in byw[('Deut', 6, v)]) == Counter({None: 318})
TOK = sum(len(W6(v)) for v in range(1, 26)); LET = sum(len(x) for v in range(1, 26) for x in W6(v))
assert TOK == 318 and LET == 1295 and {v: len(W6(v)) for v in range(1, 26)} == {1: 17, 2: 23, 3: 20, 4: 6, 5: 10, 6: 9, 7: 10, 8: 8, 9: 5, 10: 21, 11: 19, 12: 12, 13: 8, 14: 9, 15: 16, 16: 8, 17: 10, 18: 17, 19: 8, 20: 14, 21: 11, 22: 11, 23: 13, 24: 18, 25: 15}, TOK
assert (sum(len(W6(v)) for v in range(4, 10)), sum(len(x) for v in range(4, 10) for x in W6(v))) == (48, 205) and sum(len(x) for x in W6(4)) == 25
assert [(v, hp) for (c, v), g in sorted(SG.items()) for _, hp, gl in g if gl == '?'] == [(2, 'אנכי'), (6, 'אנכי')]
# THE ENGINE'S PARSER on every verse — MEASURED before the compile is asked: ONE number verse, 6:4 "one" [1] — the creed's word read as the numeral (Zechariah 14:9's
# "the LORD one and his name one" reads [1, 1]); the seven-stem homographs REFUSED — "swore" (נשבע, 6:10, 18, 23) and "you shall swear" (6:13) not numbers at all, "and you
# shall be satisfied" (6:11) STARRED; no ordinal; NO GAP. "one witness" 17:6 [2, 3, 1] and 19:15 [1, 2, 3] read the same numeral.
def MARKS(c, v): return [t for t in CS.verse_words('Deut', c, v) if t[-1] in '#~^%@|*']
assert PARSED == {(6, 4): [1]} and {(c, v): O('Deut', c, v) for (c, v) in SPAN if O('Deut', c, v)} == {} and [((c, v), t) for (c, v) in SPAN for t in MARKS(c, v)] == [((6, 11), 'ושבעת*')], PARSED
assert N('Zech', 14, 9) == [1, 1] and N('Gen', 2, 24) == [1] and N('Deut', 17, 6) == [2, 3, 1] and N('Deut', 19, 15) == [1, 2, 3] and N('Mal', 2, 10) == [1, 1] and N('Deut', 4, 35) == [] and N('Deut', 5, 6) == []
assert lemma_of('Deut', 6, 11, 'ושבעת') == ['7646'] and lemma_of('Deut', 6, 10, 'נשבע') == ['7650'] and lemma_of('Deut', 6, 13, 'תשבע') == ['7650'] and lemma_of('Deut', 6, 4, 'אחד') == ['259'] and wm('Deut', 6, 4) == [('שמע', 'HVqv2ms'), ('ישראל', 'HNp'), ('יהוה', 'HNp'), ('אלהינו', 'HNcmpc/Sp1cp'), ('יהוה', 'HNp'), ('אחד', 'HAcmsa')]
assert Counter(s.split()[0] for s in LEMV('259', books=T)) == Counter({'Num': 122, 'Exod': 69, 'Gen': 43, 'Lev': 37, 'Deut': 24})
# THE FRAMES AND THE REGISTER: NO divine frame and no "and the LORD said to me" — the whole chapter Moses' voice; ONE "saying" — the son's question (6:20); the narrative
# verbs only inside the answer (6:21 he brought us out, 6:22 he gave, 6:24 he commanded us — the exodus retold); TWO IMPERATIVES "hear" (6:4) and "take heed" (6:12); ONE
# INFINITIVE ABSOLUTE "keep" (6:17, with 5:12 and 16:1 the book's three); TWO PROHIBITIONS, both PLURAL — "you shall not go after other gods" (6:14) and "you shall not
# test" (6:16); the chapter's body SINGULAR (2, 4-13, 15, 18-19, 21), plural at 1, 14, 16, 17, both at 3 and 20, the answer's verses (22-25) in the FIRST PERSON PLURAL;
# "the LORD your God" singular six tokens (2, 5, 10, 13, 15 twice), plural three (1, 16, 17), "the LORD our God" four (4, 20, 24, 25); the Name twenty-two, all bare; Moses
# never named; Israel twice (3, 4); the case tokens "when/for" 10, 15, 20, 25 and "lest" 12, 15 — no "if", no "or".
DIV = [(c, v) for (c, v) in SPAN if any(W6(v)[i] in ('ויאמר', 'וידבר') and W6(v)[i + 1] == 'יהוה' for i in range(len(W6(v)) - 1))]
assert DIV == [] and P('ויאמר', 'יהוה', 'אלי', books=('Deut',)) and [(c, v) for (c, v) in SPAN if 'לאמר' in W6(v)] == [(6, 20)] and [(c, v) for (c, v) in SPAN if 'משה' in W6(v)] == [] and [v for v in range(1, 26) if 'ישראל' in W6(v)] == [3, 4]
REG = {v: [x for x, m in by[('Deut', 6, v)] if m and re.search(r'^HC/V.w', m)] for v in range(1, 26) if any(m and re.search(r'^HC/V.w', m) for _, m in by[('Deut', 6, v)])}
assert REG == {21: ['ויוציאנו'], 22: ['ויתן'], 24: ['ויצונו']}, REG
CASE = {f'6:{v}': [x for x in W6(v) if x in ('כי', 'אם', 'ואם', 'או', 'פן')] for v in range(1, 26) if any(x in ('כי', 'אם', 'ואם', 'או', 'פן') for x in W6(v))}
assert CASE == {'6:10': ['כי'], '6:12': ['פן'], '6:15': ['כי', 'פן'], '6:20': ['כי'], '6:25': ['כי']}, CASE
NUM2 = {v: (sum(1 for _, m in by[('Deut', 6, v)] if m and '2mp' in m), sum(1 for _, m in by[('Deut', 6, v)] if m and '2ms' in m)) for v in range(1, 26)}
SG_ONLY = [v for v, (p_, s_) in NUM2.items() if s_ and not p_]; PL_ONLY = [v for v, (p_, s_) in NUM2.items() if p_ and not s_]; BOTH = [v for v, (p_, s_) in NUM2.items() if p_ and s_]; NEITHER = [v for v, (p_, s_) in NUM2.items() if not p_ and not s_]
assert SG_ONLY == [2, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 15, 18, 19, 21] and PL_ONLY == [1, 14, 16, 17] and BOTH == [3, 20] and NEITHER == [22, 23, 24, 25], (SG_ONLY, PL_ONLY, BOTH, NEITHER)
assert NUM2[1] == (3, 0) and NUM2[2] == (0, 8) and NUM2[7] == (0, 8) and NUM2[16] == (3, 0) and NUM2[20] == (1, 2) and NUM2[4] == (0, 1)
ONE_CP = {v: [(x, m) for x, m in by[('Deut', 6, v)] if m and '1cp' in m] for v in range(1, 26) if any(m and '1cp' in m for _, m in by[('Deut', 6, v)])}
assert sorted(ONE_CP) == [4, 20, 21, 22, 23, 24, 25] and ONE_CP[21] == [('היינו', 'HVqp1cp'), ('ויוציאנו', 'HC/Vhw3ms/Sp1cp')] and ONE_CP[25] == [('לנו', 'HR/Sp1cp'), ('נשמר', 'HVqi1cp'), ('אלהינו', 'HNcmpc/Sp1cp'), ('צונו', 'HVpp3ms/Sp1cp')]
assert {v: [(x, m) for x, m in by[('Deut', 6, v)] if m and '1cs' in m] for v in range(1, 26) if any(m and '1cs' in m for _, m in by[('Deut', 6, v)])} == {2: [('אנכי', 'HPp1cs')], 6: [('אנכי', 'HPp1cs')]}
IMPER = {v: [(x, m) for x, m in by[('Deut', 6, v)] if m and re.match(r'^HV.?.?v', m)] for v in range(1, 26) if any(m and re.match(r'^HV.?.?v', m) for _, m in by[('Deut', 6, v)])}
assert IMPER == {4: [('שמע', 'HVqv2ms')], 12: [('השמר', 'HVNv2ms')]}, IMPER
INFA = {v: [(x, m) for x, m in by[('Deut', 6, v)] if m and re.match(r'^HV.a$', m)] for v in range(1, 26) if any(m and re.match(r'^HV.a$', m) for _, m in by[('Deut', 6, v)])}
assert INFA == {17: [('שמור', 'HVqa')]} and [(s_, m) for s_, x, m in LEMT('8104') if x == 'שמור' and m == 'HVqa'] == [('Deut 5:12', 'HVqa'), ('Deut 6:17', 'HVqa'), ('Deut 16:1', 'HVqa')]
WEQATAL = {v: [x for x, m in by[('Deut', 6, v)] if m and re.search(r'^HC/V.q', m)] for v in range(1, 26) if any(m and re.search(r'^HC/V.q', m) for _, m in by[('Deut', 6, v)])}
assert WEQATAL == {3: ['ושמעת', 'ושמרת'], 5: ['ואהבת'], 6: ['והיו'], 7: ['ושננתם', 'ודברת'], 8: ['וקשרתם', 'והיו'], 9: ['וכתבתם'], 10: ['והיה'], 11: ['ואכלת', 'ושבעת'], 15: ['והשמידך'], 18: ['ועשית', 'ובאת', 'וירשת'], 21: ['ואמרת']}, WEQATAL
YIQ2 = {v: [(x, m) for x, m in by[('Deut', 6, v)] if m and re.search(r'^HV.i2', m)] for v in range(1, 26) if any(m and re.search(r'^HV.i2', m) for _, m in by[('Deut', 6, v)])}
assert YIQ2 == {2: [('תירא', 'HVqi2ms')], 3: [('תרבון', 'HVqi2mp/Sn')], 12: [('תשכח', 'HVqi2ms')], 13: [('תירא', 'HVqi2ms'), ('תעבד', 'HVqi2ms'), ('תשבע', 'HVNi2ms')], 14: [('תלכון', 'HVqi2mp/Sn')], 16: [('תנסו', 'HVpi2mp')], 17: [('תשמרון', 'HVqi2mp/Sn')]}, YIQ2
PROHIB = {v: [(by[('Deut', 6, v)][i + 1][0], by[('Deut', 6, v)][i + 1][1]) for i, (x, _) in enumerate(by[('Deut', 6, v)][:-1]) if x == 'לא' and by[('Deut', 6, v)][i + 1][1] and re.search(r'^HV.i2', by[('Deut', 6, v)][i + 1][1])] for v in range(1, 26)}
PROHIB = {v: l for v, l in PROHIB.items() if l}
assert PROHIB == {14: [('תלכון', 'HVqi2mp/Sn')], 16: [('תנסו', 'HVpi2mp')]}, PROHIB
YG_SG = [v for v in range(1, 26) for i in range(len(W6(v)) - 1) if W6(v)[i:i + 2] == ['יהוה', 'אלהיך']]; YG_PL = [v for v in range(1, 26) for i in range(len(W6(v)) - 1) if W6(v)[i:i + 2] == ['יהוה', 'אלהיכם']]; YG_OUR = [v for v in range(1, 26) for i in range(len(W6(v)) - 1) if W6(v)[i:i + 2] == ['יהוה', 'אלהינו']]
assert YG_SG == [2, 5, 10, 13, 15, 15] and YG_PL == [1, 16, 17] and YG_OUR == [4, 20, 24, 25] and len(P('יהוה', 'אלהינו', books=('Deut',))) == 20
NAME = Counter(x for v in range(1, 26) for x in W6(v) if x in ('יהוה', 'ויהוה', 'ביהוה', 'כיהוה', 'ליהוה'))
assert NAME == Counter({'יהוה': 22}) and {v: [x for x in W6(v) if x in ('אלהים', 'האלהים', 'אלהי', 'מאלהי')] for v in range(1, 26) if any(x in ('אלהים', 'האלהים', 'אלהי', 'מאלהי') for x in W6(v))} == {3: ['אלהי'], 14: ['אלהים', 'מאלהי']}
# THE REGISTER GATE: NO SEAT IN CHAPTER 6 (computed on the index and the dispositions) — 6:25's "as He commanded us" carries no Name, 6:1's "and this is" is not the footers' "these are"
RD = open(f'{ROOT}/World/step9/register_dispositions.yaml', encoding='utf-8').read(); RI = open(f'{ROOT}/World/step9/REGISTER_INDEX.md', encoding='utf-8').read()
assert not re.search(r'Deut 6:\d', RI) and not re.search(r'^  Deut 6:\d', RD, re.M) and not re.search(r'^  Deut 4:45:', RD, re.M) and re.search(r'^  Deut 5:32:', RD, re.M)   # 4:45 DAEMONS green by computation, no key; 5:32 CHAPTER declared at 3b
# 6:1-3 THE HEADER (computed): "and this is the commandment" one; "the commandment, the statutes and the judgments" the triad 5:31 (the charge), 6:1 (its fulfilment opens),
# 7:11; "to teach you" 4:14 and 6:1; "which you are crossing over to possess" four; "that you may fear the LORD your God" one; "you and your son and your son's son" one
# ("your son's son" Exodus 10:2 the other); "all the days of your life" seven; "AND THAT YOUR DAYS MAY BE LONG" this spelling one; "and you shall hear, O Israel" one;
# "and observe to do" 6:3 and 17:10; "that it may be well with you" seven Deuteronomy; "that you may multiply greatly" one; "a land flowing with milk and honey" eleven
# Torah seats — 6:3 THE BOOK'S FIRST; "as the LORD has spoken" eight Deuteronomy, two this chapter's (6:3, 6:19).
assert P('וזאת', 'המצוה') == ['Deut 6:1'] and P('ללמד', 'אתכם') == S_('Deut 4:14', 'Deut 6:1') and P('אשר', 'אתם', 'עברים', 'שמה', 'לרשתה') == S_('Deut 11:11', 'Deut 11:8', 'Deut 4:14', 'Deut 6:1')
TRIAD = [(s_, [x for x in words(*[s_.split()[0], *map(int, s_.split()[1].split(':'))]) if x in ('המצוה', 'החקים', 'והחקים', 'והמשפטים', 'המשפטים', 'ואת')]) for s_ in U('המצוה', books=('Deut',)) if s_ in U('והמשפטים', 'המשפטים', books=('Deut',))]
assert TRIAD == [('Deut 5:31', ['המצוה', 'והחקים', 'והמשפטים']), ('Deut 6:1', ['המצוה', 'החקים', 'והמשפטים']), ('Deut 7:11', ['המצוה', 'ואת', 'החקים', 'ואת', 'המשפטים'])], TRIAD
assert P('למען', 'תירא', 'את', 'יהוה', 'אלהיך') == ['Deut 6:2'] and P('אתה', 'ובנך', 'ובן', 'בנך') == ['Deut 6:2'] and P('ובן', 'בנך') == S_('Deut 6:2', 'Exod 10:2') and P('כל', 'ימי', 'חייך') == S_('Deut 16:3', 'Deut 4:9', 'Deut 6:2', 'Gen 3:14', 'Gen 3:17', 'Josh 1:5', 'Ps 128:5')
assert P('ולמען', 'יארכן', 'ימיך') == ['Deut 6:2'] and len(P('אשר', 'אנכי', 'מצוך', 'היום', books=('Deut',))) == 18 and [v for v in range(1, 26) if 'מצוך' in W6(v)] == [2, 6]
assert P('ושמעת', 'ישראל') == ['Deut 6:3'] and P('ושמרת', 'לעשות') == S_('Deut 17:10', 'Deut 6:3') and P('ייטב', 'לך', books=('Deut',)) == S_('Deut 12:25', 'Deut 12:28', 'Deut 22:7', 'Deut 4:40', 'Deut 5:16', 'Deut 6:18', 'Deut 6:3') and P('תרבון', 'מאד') == ['Deut 6:3']
assert P('ארץ', 'זבת', 'חלב', 'ודבש', books=T) == S_('Deut 11:9', 'Deut 26:15', 'Deut 26:9', 'Deut 27:3', 'Deut 6:3', 'Exod 13:5', 'Exod 33:3', 'Exod 3:17', 'Exod 3:8', 'Lev 20:24', 'Num 16:14') and P('כאשר', 'דבר', 'יהוה', books=('Deut',)) == S_('Deut 10:9', 'Deut 1:21', 'Deut 27:3', 'Deut 2:1', 'Deut 31:3', 'Deut 6:19', 'Deut 6:3', 'Deut 9:3')
# 6:4-9 THE SHEMA (computed): "hear, O Israel" four seats, all this book's (5:1, 6:4, 9:1, 20:3); "THE LORD IS ONE" 6:4 and Zechariah 14:9 — the two seats of the pair;
# "and you shall love the LORD your God" 6:5 and 11:1 ("and you shall love" six over the Bible — the neighbor and the stranger Leviticus 19:18, 34); "with all your heart
# and with all your soul" seven, all Deuteronomy's (4:29 the first), the plural form four; "AND WITH ALL YOUR MIGHT" — מאדך THE BIBLE'S ONE SEAT of the noun with a suffix;
# "these words" eight in the book; "upon your heart" 6:6 and Ezekiel 38:10 (the plural 11:18 and Jeremiah 51:50); "AND YOU SHALL TEACH THEM DILIGENTLY" (ושננתם) the
# root's nine seats — sharpen, whet (arrows, a sword, the tongue) — this the ONE seat of the word; "and you shall speak of them" one; "when you sit … when you rise" 6:7
# and 11:19; "for a sign upon your hand" Exodus 13:9, 16 and 6:8, 11:18 — FOUR SEATS, four spellings of the hand (ידך, ידכה, ידך, ידכם); "FRONTLETS" THREE SEATS, THREE
# SPELLINGS — Exodus 13:16 ולטוטפת, 6:8 לטטפת (the defective), 11:18 לטוטפת; "between your eyes" five (14:1 the fifth — the mourners' baldness); "and you shall write
# them" 6:9 and 11:20; "doorposts" thirteen (Exodus 12's three); "and upon your gates" two.
assert P('שמע', 'ישראל') == S_('Deut 20:3', 'Deut 5:1', 'Deut 6:4', 'Deut 9:1') and P('יהוה', 'אחד') == S_('Deut 6:4', 'Zech 14:9') and words('Zech', 14, 9)[-4:] == ['יהוה', 'אחד', 'ושמו', 'אחד']
assert P('ואהבת', 'את', 'יהוה', 'אלהיך') == S_('Deut 11:1', 'Deut 6:5') and U('ואהבת') == S_('Deut 11:1', 'Deut 6:5', 'Jer 31:3', 'Lev 19:18', 'Lev 19:34', 'Mic 6:8')
assert P('בכל', 'לבבך', 'ובכל', 'נפשך') == S_('Deut 10:12', 'Deut 26:16', 'Deut 30:10', 'Deut 30:2', 'Deut 30:6', 'Deut 4:29', 'Deut 6:5') and P('בכל', 'לבבכם', 'ובכל', 'נפשכם') == S_('Deut 11:13', 'Deut 13:4', 'Josh 22:5', 'Josh 23:14')
assert U('מאדך', 'מאדכם', 'ומאדך') == ['Deut 6:5'] and hits('מאדך', exact=False) == ['Deut 6:5']
assert P('הדברים', 'האלה', books=('Deut',)) == S_('Deut 12:28', 'Deut 30:1', 'Deut 31:1', 'Deut 31:28', 'Deut 32:45', 'Deut 4:30', 'Deut 5:22', 'Deut 6:6') and P('על', 'לבבך') == S_('Deut 6:6', 'Ezek 38:10') and P('על', 'לבבכם') == S_('Deut 11:18', 'Jer 51:50')
assert LEMV('8150') == S_('Deut 32:41', 'Deut 6:7', 'Isa 5:28', 'Prov 25:18', 'Ps 120:4', 'Ps 140:4', 'Ps 45:6', 'Ps 64:4', 'Ps 73:21') and U('ושננתם') == ['Deut 6:7'] and P('ודברת', 'בם') == ['Deut 6:7'] and P('בשבתך', 'בביתך', 'ובלכתך', 'בדרך', 'ובשכבך', 'ובקומך') == S_('Deut 11:19', 'Deut 6:7')
SIGN = [(s_, [x for x in words(*[s_.split()[0], *map(int, s_.split()[1].split(':'))]) if x.startswith('יד')]) for s_ in P('לאות', 'על') if s_ in U('ידך', 'ידכה', 'ידכם')]
assert SIGN == [('Deut 11:18', ['ידכם']), ('Deut 6:8', ['ידך']), ('Exod 13:16', ['ידכה', 'יד']), ('Exod 13:9', ['ידך'])], SIGN
FRONT = [(s_, [x for x in words(*[s_.split()[0], *map(int, s_.split()[1].split(':'))]) if 'טפת' in x and x.startswith(('ל', 'ול'))]) for s_ in S_('Deut 6:8', 'Deut 11:18', 'Exod 13:16')]
assert FRONT == [('Deut 11:18', ['לטוטפת']), ('Deut 6:8', ['לטטפת']), ('Exod 13:16', ['ולטוטפת'])] and sorted(hits('טטפת', exact=False) + hits('טוטפת', exact=False)) == S_('Deut 6:8', 'Deut 11:18', 'Exod 13:16'), FRONT
assert P('בין', 'עיניך') + P('בין', 'עיניכם') == ['Deut 6:8', 'Exod 13:16', 'Exod 13:9', 'Deut 11:18', 'Deut 14:1'] and U('וכתבתם') == S_('Deut 11:20', 'Deut 6:9') and len(U('מזוזת', 'מזזות', 'מזוזות', 'המזוזת', 'המזוזות')) == 13 and U('ובשעריך') == S_('Deut 11:20', 'Deut 6:9')
assert P('וכתבתם', 'על', 'מזוזת', 'ביתך', 'ובשעריך') == ['Deut 6:9'] and words('Deut', 11, 20)[2] == 'מזוזות' and DIFF(('Deut', 6, 9), ('Deut', 11, 20)) == [('replace', ['מזוזת'], ['מזוזות'])]
# 6:10-15 THE GIFT AND THE WARNING (computed): "which He swore to your fathers" four Deuteronomy seats (6:10 the first); "to Abraham, to Isaac and to Jacob" eleven; "swore"
# twenty-two in the book, three this chapter's (10, 18, 23 — "to our fathers" 6:23 the one seat); "great and good cities" one, "houses full of all good" one, "hewn
# cisterns" one, "vineyards and olive trees" 6:11, Joshua 24:13, Nehemiah 9:25 — THE LIST'S TWO RETELLINGS; "AND YOU SHALL EAT AND BE SATISFIED" 6:11, 8:10, 11:15
# (8:10 the grace's seat); "take heed to yourself lest you forget" 6:12 and 8:11; "who brought you out of the land of Egypt, from the house of bondage" five with the
# suffix, "house of bondage" twelve; "THE LORD YOUR GOD YOU SHALL FEAR", "HIM YOU SHALL SERVE", "BY HIS NAME YOU SHALL SWEAR" 6:13 and 10:20 — the pair (10:20 adds "to
# Him you shall cleave"); "after other gods" sixteen, seven this book's; "you shall not go" with the nun 6:14 and Isaiah 52:12; "a jealous God" five; "in your midst"
# eleven Deuteronomy; "lest the anger of the LORD be kindled against you" one; "and destroy you from the face of the ground" one ("from the face of the ground" thirteen —
# the flood's phrase).
assert P('אשר', 'נשבע', 'לאבתיך', books=('Deut',)) == S_('Deut 6:10', 'Deut 7:12', 'Deut 7:13', 'Deut 8:18') and len(P('לאברהם', 'ליצחק', 'וליעקב')) == 11 and P('נשבע', 'לאבתינו') == ['Deut 6:23'] and len(U('נשבע', books=('Deut',))) == 22 and [v for v in range(1, 26) if 'נשבע' in W6(v)] == [10, 18, 23]
assert P('ערים', 'גדלת', 'וטבת') == ['Deut 6:10'] and P('ובתים', 'מלאים', 'כל', 'טוב') == ['Deut 6:11'] and P('וברת', 'חצובים') == ['Deut 6:11'] and P('כרמים', 'וזיתים') == S_('Deut 6:11', 'Josh 24:13', 'Neh 9:25') and P('ואכלת', 'ושבעת') == S_('Deut 11:15', 'Deut 6:11', 'Deut 8:10')
assert P('השמר', 'לך', 'פן', 'תשכח') == S_('Deut 6:12', 'Deut 8:11') and [s_ for s_ in P('מבית', 'עבדים') if s_ in U('הוציאך', 'הוצאתיך', 'המוציאך')] == S_('Deut 13:11', 'Deut 5:6', 'Deut 6:12', 'Deut 8:14', 'Exod 20:2') and len(P('בית', 'עבדים') + P('מבית', 'עבדים')) == 12
assert P('את', 'יהוה', 'אלהיך', 'תירא') == S_('Deut 10:20', 'Deut 6:13') and P('ובשמו', 'תשבע') == S_('Deut 10:20', 'Deut 6:13') and P('ואתו', 'תעבד') + P('אתו', 'תעבד') == ['Deut 6:13', 'Deut 10:20'] and DIFF(('Deut', 6, 13), ('Deut', 10, 20)) == [('replace', ['ואתו'], ['אתו']), ('insert', [], ['ובו', 'תדבק'])]
assert len(P('אחרי', 'אלהים', 'אחרים')) == 16 and P('אחרי', 'אלהים', 'אחרים', books=('Deut',)) == S_('Deut 11:28', 'Deut 13:3', 'Deut 28:14', 'Deut 6:14', 'Deut 8:19') and P('לא', 'תלכון') == S_('Deut 6:14', 'Isa 52:12') and P('מאלהי', 'העמים', 'אשר', 'סביבותיכם') == ['Deut 6:14']
assert P('אל', 'קנא') == S_('Deut 4:24', 'Deut 5:9', 'Deut 6:15', 'Exod 20:5', 'Exod 34:14') and len(U('בקרבך', books=('Deut',))) == 11 and P('פן', 'יחרה', 'אף', 'יהוה') == ['Deut 6:15'] and P('והשמידך', 'מעל', 'פני', 'האדמה') == ['Deut 6:15'] and len(P('מעל', 'פני', 'האדמה')) == 13 and 'Gen 6:7' in P('מעל', 'פני', 'האדמה')
# 6:16-19 MASSAH, KEEP, THE RIGHT AND THE GOOD (computed): "you shall not test" 6:16, Exodus 17:2 (the people's "why do you test"), Isaiah 30:17; "MASSAH" four seats —
# Exodus 17:7 (the naming), 6:16, 33:8 (Levi's blessing), Psalm 95:8; "as you tested" four; the lemma "test" fourteen Torah seats — God tests Abraham (Genesis 22:1) and
# Israel (Exodus 15:25, 16:4, 20:20, Deuteronomy 8:2, 16, 13:4), Israel tests God (Exodus 17:2, 7, Numbers 14:22 "these ten times", 6:16); "YOU SHALL SURELY KEEP" one;
# "the commandments … His testimonies and His statutes" one — "testimonies" in Deuteronomy at 4:45, 6:17, 6:20 alone (Exodus' "testimony" the ark's); "and you shall
# do what is right and good" one, the pair 6:18 and 12:28 (reversed there), "right in the eyes of the LORD" three Torah seats; "to thrust out all your enemies" one (the
# root's eleven — the manslayer's "thrust" Numbers 35:20, 22; 9:4 "when the LORD thrusts them out").
assert U('תנסו', 'תנסה', 'תנסון') == S_('Deut 6:16', 'Exod 17:2', 'Isa 30:17') and U('מסה', 'במסה', 'ומסה', 'המסה') == S_('Deut 33:8', 'Deut 6:16', 'Exod 17:7', 'Ps 95:8') and U('נסיתם', 'נסיתו', 'נסיתי') == S_('1Sam 17:39', 'Deut 33:8', 'Deut 6:16', 'Eccl 7:23')
assert LEMV('5254', books=T) == S_('Deut 13:4', 'Deut 28:56', 'Deut 33:8', 'Deut 4:34', 'Deut 6:16', 'Deut 8:16', 'Deut 8:2', 'Exod 15:25', 'Exod 16:4', 'Exod 17:2', 'Exod 17:7', 'Exod 20:20', 'Gen 22:1', 'Num 14:22')
assert P('שמור', 'תשמרון') == ['Deut 6:17'] and P('ועדתיו', 'וחקיו') == ['Deut 6:17'] and P('העדת', 'והחקים', 'והמשפטים') == S_('Deut 4:45', 'Deut 6:20') and [s_ for s_ in U('עדת', 'העדת', 'עדתיו', 'ועדתיו', 'עדותיו', 'ועדותיו', books=T) if s_.startswith('Deut')] == S_('Deut 4:45', 'Deut 6:17', 'Deut 6:20')
assert P('ועשית', 'הישר', 'והטוב') == ['Deut 6:18'] and P('הישר', 'והטוב') + P('הטוב', 'והישר') == ['Deut 6:18', '2Chr 14:1', '2Chr 31:20', '2Kgs 10:3', 'Deut 12:28'] and P('הישר', 'בעיני', 'יהוה', books=T) == S_('Deut 12:25', 'Deut 13:19', 'Deut 21:9')
assert P('להדף', 'את', 'כל', 'איביך') == ['Deut 6:19'] and LEMV('1920') == S_('2Kgs 4:27', 'Deut 6:19', 'Deut 9:4', 'Ezek 34:21', 'Isa 22:19', 'Jer 46:15', 'Job 18:18', 'Josh 23:5', 'Num 35:20', 'Num 35:22', 'Prov 10:3')
# 6:20-25 THE SON'S QUESTION AND THE ANSWER (computed): "WHEN YOUR SON ASKS YOU TOMORROW" 6:20 and Exodus 13:14 — THE TWO SEATS, verbatim to "saying"; the four askings
# (Exodus 12:26 the sons plural, 13:8 no asking — "you shall tell", 13:14 "what is this", 6:20 "what are the testimonies"); "what is this" eleven, "what are the
# testimonies" one; the sons' "tomorrow" seven (Joshua's four); "and you shall say to your son" one ("and you shall tell your son" Exodus 13:8 one); "WE WERE SLAVES TO
# PHARAOH" one; "with a strong hand" eight Torah; "signs and wonders" — 6:22's אותת plene with ומפתים, Nehemiah 9:10 the other pairing; "great and grievous" one;
# "before our eyes" 6:22, Joshua 24:17, Psalm 79:10; "and us He brought out from there" one; "to bring us in, to give us the land" one; "and the LORD commanded us"
# one; "to fear the LORD our God" one; "for our good always" one; "to keep us alive as at this day" one ("as at this day" six); "AND IT SHALL BE RIGHTEOUSNESS FOR US"
# one — "righteousness" eight Torah seats (Abraham's Genesis 15:6 the first; 24:13 the pledge's "it shall be righteousness for you"); "AS HE COMMANDED US" 6:25 and
# Ezra 4:3 — the receipt WITHOUT THE NAME (the register gate's census does not see it); "all this commandment" four.
assert P('כי', 'ישאלך', 'בנך', 'מחר') == S_('Deut 6:20', 'Exod 13:14') and DIFF(('Deut', 6, 20), ('Exod', 13, 14))[0] == ('insert', [], ['והיה']) and words('Exod', 13, 14)[1:6] == ['כי', 'ישאלך', 'בנך', 'מחר', 'לאמר'] and W6(20)[:5] == ['כי', 'ישאלך', 'בנך', 'מחר', 'לאמר']
assert [s_ for s_ in U('מחר') if s_ in U('ישאלך', 'ישאלון', 'ישאלו', 'בניכם', 'בנך')] == S_('2Kgs 6:28', 'Deut 6:20', 'Exod 13:14', 'Josh 22:24', 'Josh 22:27', 'Josh 4:21', 'Josh 4:6') and len(P('מה', 'זאת')) == 10 and P('מה', 'העדת') == ['Deut 6:20']
assert P('ואמרת', 'לבנך') == ['Deut 6:21'] and P('והגדת', 'לבנך') == ['Exod 13:8'] and P('עבדים', 'היינו', 'לפרעה') == ['Deut 6:21'] and P('ביד', 'חזקה', books=T) == S_('Deut 26:8', 'Deut 5:15', 'Deut 6:21', 'Deut 7:8', 'Deut 9:26', 'Exod 13:9', 'Exod 3:19', 'Exod 6:1')
assert [s_ for s_ in U('אתת', 'אותת', 'ואתת') if s_ in U('ומפתים', 'ומופתים', 'ובמפתים', 'ובמופתים')] == S_('Deut 6:22', 'Neh 9:10') and W6(22)[2:4] == ['אותת', 'ומפתים'] and P('גדלים', 'ורעים') == ['Deut 6:22'] and U('לעינינו') == S_('Deut 6:22', 'Josh 24:17', 'Ps 79:10')
assert P('ואותנו', 'הוציא', 'משם') == ['Deut 6:23'] and P('הביא', 'אתנו', 'לתת', 'לנו') == ['Deut 6:23'] and P('ויצונו', 'יהוה') == ['Deut 6:24'] and P('ליראה', 'את', 'יהוה', 'אלהינו') == ['Deut 6:24'] and P('לטוב', 'לנו', 'כל', 'הימים') == ['Deut 6:24']
assert P('לחיתנו', 'כהיום', 'הזה') == ['Deut 6:24'] and P('כהיום', 'הזה') == S_('Deut 6:24', 'Ezra 9:15', 'Ezra 9:7', 'Gen 39:11', 'Jer 44:22', 'Neh 9:10')
assert P('וצדקה', 'תהיה', 'לנו') == ['Deut 6:25'] and U('צדקה', 'וצדקה', 'לצדקה', 'צדקתך', 'ובצדקתך', 'בצדקתי', 'בצדקתך', books=T) == S_('Deut 24:13', 'Deut 6:25', 'Deut 9:4', 'Deut 9:5', 'Deut 9:6', 'Gen 15:6', 'Gen 18:19', 'Gen 38:26') and P('כאשר', 'צונו') == S_('Deut 6:25', 'Ezra 4:3') and P('כל', 'המצוה', 'הזאת') == S_('Deut 11:22', 'Deut 15:5', 'Deut 19:9', 'Deut 6:25')
# ONKELOS CHAPTER 6 — THE RENDERINGS' SEATS over the whole book (computed on the plain Aramaic of every export row; the export's chapter 6 = the DB's): 6:2 "fear BEFORE the LORD"
# (the reverential "before" 101 seats in the book); 6:3 "hear" made "ACCEPT" (six); 6:4 "THE LORD IS ONE" — חד (one seat of the pair; the word twelve); 6:5 "love" made "cherish"
# (6:5, 11:1), "AND WITH ALL YOUR MIGHT" made "AND WITH ALL YOUR PROPERTY" (נכסך — ONE SEAT); 6:7 "teach diligently" made "repeat/teach" (one), "speak" made "speak" (one);
# 6:8 "FRONTLETS" made "TEFILLIN" (one — the object named); 6:9 "write them on the doorposts" made "write them on MEZUZOT AND FIX THEM IN THE DOORPOSTS" (the fixing supplied —
# 6:9 and 11:20); 6:10 "swore" made "confirmed by oath" (twenty-two); 6:12 "lest you forget THE FEAR OF the LORD" — the export's PARENTHESISED VARIANT (one of the book's ten
# such rows); 6:13 "serve Him" made "serve BEFORE HIM" (6:13, 10:20, 13:5), "swear by His name" (6:13, 10:20); 6:14 "other gods" made "THE IDOLS OF THE PEOPLES" (eighteen);
# 6:15 "in your midst" made "HIS SHEKHINAH IS AMONG YOU" (6:15, 7:21), "destroy you" (6:15, 7:4); 6:16 "MASSAH" made "THE TRIAL" (one); 6:18 "the right and the good"
# made "what is fit and what is proper" (one); 6:19 "thrust out" made "shatter" (one); 6:20 "testimonies" (4:45, 5:17 the export's, 6:20); 6:21 "we were slaves" (one);
# 6:22 "all his house" made "all THE MEN OF his house" (one); 6:24 "keep us alive" (one); 6:25 "RIGHTEOUSNESS" MADE "MERIT" (6:25 and 24:13 — the two seats).
ONK6 = {'נכסך': [(6, 5)], 'מזוזין': [(6, 9), (11, 20)], 'ותקבענון': [(6, 9), (11, 20)], 'בספי': [(6, 9), (11, 20)], 'דחלתא': [(1, 36), (4, 29), (8, 11), (8, 14), (8, 19), (13, 5), (28, 60)], 'שכנתיה': [(6, 15), (7, 21), (12, 5), (12, 11), (12, 21), (14, 23), (14, 24), (16, 2), (16, 6), (16, 11), (23, 15), (26, 2)], 'בנסיתא': [(6, 16)], 'זכותא': [(24, 13)], 'תקים': [(6, 13), (10, 20), (16, 22), (20, 16), (22, 4), (28, 36)], 'טעות': [(6, 14), (8, 19), (11, 28), (13, 3), (18, 20), (28, 14), (29, 17), (31, 16), (31, 20)], 'דכשר': [(6, 18), (12, 8), (12, 25), (13, 19), (21, 9)], 'ודתקן': [(6, 18)], 'למתבר': [(6, 19)], 'סהדותא': [(4, 45), (5, 17), (6, 20)], 'ותתננון': [(6, 7)], 'ותרחם': [(6, 5), (11, 1)], 'ותקבל': [(4, 30), (6, 3), (12, 28), (27, 10), (30, 2), (30, 8)], 'אפקך': [(6, 12), (7, 19), (8, 14), (13, 11), (16, 1)], 'תפקדתא': [(5, 28), (6, 1), (6, 25), (7, 11), (8, 1), (11, 8), (11, 22), (15, 5), (17, 20), (19, 9), (27, 1), (30, 11), (31, 5)], 'קימיא': [(4, 5), (4, 6), (5, 1), (6, 1), (6, 24), (7, 11), (11, 32), (12, 1), (16, 12), (17, 19), (26, 16)], 'דיניא': [(5, 1), (7, 11), (7, 12), (11, 32), (19, 18), (26, 16)], 'עבדותא': [(5, 6), (6, 12), (7, 8), (8, 14), (13, 6), (13, 11)], 'לחדא': [(2, 4), (3, 5), (4, 9), (4, 15), (6, 3), (9, 20), (17, 17), (19, 5), (19, 11), (20, 15), (24, 8), (28, 54), (30, 14)], 'רגזא': [(6, 15), (7, 4), (9, 19), (11, 17), (29, 19), (29, 23), (29, 26), (32, 27)], 'וישצך': [(6, 15), (7, 4)], 'אנש': [(6, 22), (7, 24), (11, 6), (11, 25), (15, 16), (24, 16), (27, 14), (29, 9), (32, 25), (34, 6)], 'ותמלל': [(6, 7)], 'תנשי': [(4, 9), (6, 12), (8, 19), (9, 7)], 'למדחל': [(4, 10), (5, 26), (6, 24), (10, 12), (14, 23), (17, 19), (28, 58), (31, 13)], 'לקימותנא': [(6, 24)], 'תדחל': [(1, 21), (3, 2), (6, 13), (7, 18), (10, 20), (18, 22), (20, 1), (31, 8)], 'תפלח': [(5, 13), (6, 13), (7, 16), (10, 20), (15, 19)], 'בסחרניכון': [(6, 14), (13, 8)], 'לאלפא': [(4, 14), (6, 1)], 'חד': [(1, 2), (1, 23), (6, 4), (15, 7), (15, 18), (17, 6), (19, 15), (25, 5), (25, 11), (28, 7), (32, 30), (32, 41)], 'פתגמיא': [(1, 1), (1, 18), (4, 9), (4, 30), (5, 19), (6, 6), (9, 10), (10, 2), (10, 4), (12, 28), (28, 14), (30, 1), (31, 1), (31, 28), (32, 45), (32, 46)], 'מקדמך': [(6, 19), (7, 20), (7, 22), (7, 24), (9, 4), (9, 5), (12, 29), (12, 30), (18, 12), (20, 19), (28, 7), (28, 31), (31, 3), (33, 27)], 'דבבך': [(6, 19), (20, 1), (21, 10), (23, 10), (23, 15), (25, 19), (28, 7), (28, 31), (28, 48), (28, 68), (30, 7), (33, 18)]}
assert all(onk_tok(t) == s_ for t, s_ in ONK6.items()), [t for t, s_ in ONK6.items() if onk_tok(t) != s_]
assert {t: len(onk_tok(t)) for t in ('קדמוהי', 'דילמא', 'ארי', 'עממיא', 'למירתה', 'קיים', 'תפלין', 'נכסכון')} == {'קדמוהי': 26, 'דילמא': 24, 'ארי': 225, 'עממיא': 53, 'למירתה': 25, 'קיים': 22, 'תפלין': 0, 'נכסכון': 0}
ONK6P = {'יי חד': 1, 'ובכל נכסך': 1, 'שכנתיה בינך': 2, 'דחלתא דיי': 12, 'ית דחלתא': 3, 'קדם יי אלהך': 48, 'קדם יי': 101, 'קדמוהי תפלח': 3, 'ובשמיה תקים': 2, 'טעות עממיא': 18, 'בתר טעות': 7, 'דכשר ודתקן': 1, 'סהדותא וקימיא ודיניא': 2, 'תפקדתא קימיא ודיניא': 1, 'קימיא ודיניא': 6, 'למתבר ית כל': 1, 'בעלי דבבך': 12, 'זכותא תהי': 1, 'וזכותא': 1, 'ותקבענון בספי': 2, 'על מזוזין': 2, 'לתפלין בין עיניך': 1, 'ותתננון לבניך': 1, 'עבדין הוינא': 1, 'בידא תקיפא': 6, 'אתין ומופתין': 1, 'אנש ביתיה': 1, 'כל אנש': 3, 'עבדא חלב ודבש': 6, 'כמא די מליל יי': 8, 'כמא די פקדנא': 1, 'כמא די': 51}
assert all(len(onk_seats(k)) == n for k, n in ONK6P.items()), [(k, len(onk_seats(k))) for k, n in ONK6P.items() if len(onk_seats(k)) != n]
assert onk_seats('שכנתיה בינך') == [(6, 15), (7, 21)] and onk_seats('קדמוהי תפלח') == [(6, 13), (10, 20), (13, 5)] and onk_seats('סהדותא וקימיא ודיניא') == [(4, 45), (6, 20)] and onk_seats('כמא די מליל יי') == [(1, 21), (2, 1), (6, 3), (6, 19), (9, 3), (10, 9), (27, 3), (31, 3)]
assert onk_seats('עבדא חלב ודבש') == [(6, 3), (11, 9), (26, 9), (26, 15), (27, 3), (31, 20)] and onk_seats('בידא תקיפא') == [(4, 34), (5, 15), (6, 21), (7, 8), (9, 26), (26, 8)] and onk_seats('זכותא תהי') + onk_seats('וזכותא') == [(6, 25), (6, 25)] and onk_tok('זכותא') == [(24, 13)]
assert aramaic(6, 4) == ['שמע', 'ישראל', 'יי', 'אלהנא', 'יי', 'חד'] and aramaic(6, 5)[-2:] == ['ובכל', 'נכסך'] and aramaic(6, 8)[-3:] == ['לתפלין', 'בין', 'עיניך'] and aramaic(6, 9) == ['ותכתבנון', 'על', 'מזוזין', 'ותקבענון', 'בספי', 'ביתך', 'ובתרעיך']
assert aramaic(6, 13) == ['ית', 'יי', 'אלהך', 'תדחל', 'וקדמוהי', 'תפלח', 'ובשמיה', 'תקים'] and aramaic(6, 14)[:4] == ['לא', 'תהכון', 'בתר', 'טעות'] and aramaic(6, 16)[-1] == 'בנסיתא' and aramaic(6, 18)[:3] == ['ותעבד', 'דכשר', 'ודתקן'] and aramaic(6, 25)[0] == 'וזכותא'
assert aramaic(6, 2)[:4] == ['בדיל', 'דתדחל', 'קדם', 'יי'] and aramaic(6, 3)[0] == 'ותקבל' and aramaic(6, 7)[0] == 'ותתננון' and aramaic(6, 21)[2:4] == ['עבדין', 'הוינא'] and aramaic(6, 22)[-3:] == ['אנש', 'ביתיה', 'לעיננא'] and 'שכנתיה' in aramaic(6, 15) and 'בינך' in aramaic(6, 15)
PAREN = [(c + 1, v + 1) for c in range(34) for v in range(len(onk_he[c])) if '(' in clean(onk_he[c][v])]
assert PAREN == [(6, 12), (11, 8), (18, 7), (20, 10), (22, 15), (25, 5), (29, 27), (32, 30), (33, 16), (33, 25)] and '(דחלתא ד)יי' in arm(6, 12), PAREN
BR = {e: re.findall(r'\[([^\]]+)\]', clean(onk[5][e - 1])) for e in range(1, 26)}
BR = {e: b for e, b in BR.items() if b}
assert BR == {2: ['before'], 8: ['tefillin'], 9: ['and affix them to the lintels'], 13: ['before'], 14: ['idols of the nations', 'idols'], 15: ['His Shechinah is'], 18: ['correct'], 19: ['break'], 22: ['that were'], 24: ['show that we'], 25: ['merit']}, BR
# THE STORE'S GLOSSES at the chapter's seats (words.gloss, read back): the families censused over the whole store (ch6_measure1.py G) — the rewrite planned BY GLOSS where every
# token of the gloss is the one word, BY REFERENCE where the family is mixed; applied at run 3 (the display layer), asserted here as the plan.
assert sg(6, 1, 'ללמד') == 'to-goad' and sg(6, 1, 'עברים') == 'pass-over' and sg(6, 1, 'המצוה') == 'the-commandment' and sg(6, 1, 'החקים') == 'the-enactment' and sg(6, 1, 'והמשפטים') == 'and-the-judgment' and sg(6, 2, 'אנכי') == '?' and sg(6, 2, 'חייך') == 'alive-you/your' and sg(6, 2, 'יארכן') == 'be--long-suffix'
assert sg(6, 3, 'זבת') == 'flow-freely' and sg(6, 3, 'תרבון') == 'multiply-suffix' and sg(6, 4, 'אח') == 'one' and sg(6, 4, 'שמ') == 'hear' and sg(6, 5, 'ואהבת') == 'and-have-affection-for' and sg(6, 5, 'נפשך') == 'living-being-you/your' and sg(6, 5, 'מאדך') == 'very-you/your'
assert sg(6, 6, 'אנכי') == '?' and sg(6, 6, 'הדברים') == 'the-word/thing' and sg(6, 7, 'ושננתם') == 'and-point-them/their' and sg(6, 7, 'בשבתך') == 'in-dwell/sit-you/your' and sg(6, 7, 'ובשכבך') == 'and-in-lie-down-you/your' and sg(6, 7, 'ובקומך') == 'and-in-arise-you/your' and sg(6, 7, 'בדרך') == 'in-way/road'
assert sg(6, 8, 'וקשרתם') == 'and-tie-them/their' and sg(6, 8, 'לאות') == 'to-signs' and sg(6, 8, 'לטטפת') == 'to-fillet-for-the-forehead' and sg(6, 9, 'וכתבתם') == 'and-grave-them/their' and sg(6, 9, 'מזוזת') == 'door-post' and sg(6, 10, 'יביאך') == 'come/bring-you/your' and sg(6, 10, 'לתת') == 'to-set'
assert sg(6, 11, 'וברת') == 'and-pit-hole' and sg(6, 11, 'חצובים') == 'cut' and sg(6, 11, 'חצבת') == 'cut' and sg(6, 11, 'כרמים') == 'garden' and sg(6, 11, 'נטעת') == 'strike-in' and sg(6, 11, 'ושבעת') == 'and-sate' and sg(6, 12, 'תשכח') == 'mislay' and sg(6, 12, 'עבדים') == 'servant'
assert sg(6, 13, 'תעבד') == 'work/serve' and sg(6, 14, 'תלכון') == 'go-suffix' and sg(6, 14, 'אחרי') == 'hind-part' and sg(6, 14, 'אחרים') == 'hinder' and sg(6, 14, 'סביבותיכם') == 'circle-you/your (pl)' and sg(6, 15, 'אל') == 'strength' and sg(6, 15, 'בקרבך') == 'in-nearest-part-you/your'
assert sg(6, 15, 'יחרה') == 'glow' and sg(6, 15, 'אף') == 'nose' and sg(6, 15, 'והשמידך') == 'and-desolate-you/your' and sg(6, 15, 'מעל') == 'from-over' and sg(6, 16, 'תנסו') == 'test' and sg(6, 16, 'במסה') == 'in-Massah' and sg(6, 17, 'תשמרון') == 'keep/guard-suffix' and sg(6, 17, 'ועדתיו') == 'and-testimony-him/its'
assert sg(6, 18, 'הישר') == 'the-straight' and sg(6, 18, 'ייטב') == 'be--make-well' and sg(6, 19, 'להדף') == 'to-push-away' and sg(6, 19, 'איביך') == 'hating-you/your' and sg(6, 20, 'ישאלך') == 'inquire-you/your' and sg(6, 20, 'מחר') == 'deferred' and sg(6, 20, 'העדת') == 'the-testimony'
assert sg(6, 21, 'עבדים') == 'servant' and sg(6, 22, 'ומפתים') == 'and-miracle' and sg(6, 22, 'ורעים') == 'and-bad' and sg(6, 24, 'לטוב') == 'to-good--in-the-widest-sense' and sg(6, 24, 'לחיתנו') == 'to-live-us/our' and sg(6, 24, 'כהיום') == 'like-the-day' and sg(6, 25, 'וצדקה') == 'and-rightness'
GLOSS_FAMILY = {'to-goad': [('ללמד', 2)], 'and-point-them/their': [('ושננתם', 1)], 'very-you/your': [('מאדך', 1)], 'to-fillet-for-the-forehead': [('לטוטפת', 1), ('לטטפת', 1)], 'and-rightness': [('וצדקה', 1)], 'rightness': [('צדקה', 3), ('צדקת', 1)], 'to-push-away': [('להדף', 1)], 'and-miracle': [('ומפתים', 1)], 'and-desolate-you/your': [('והשמידך', 2)], 'strike-in': [('תטע', 3), ('נטע', 2), ('נטעת', 1)], 'and-grave-them/their': [('ויכתבם', 2), ('וכתבתם', 2)], 'deferred': [('מחר', 13)], 'glow': [('יחר', 6), ('חרה', 2), ('יחרה', 2)], 'and-sate': [('ושבעת', 4), ('ושבעו', 2), ('ושבע', 1)], 'and-have-affection-for': [('ואהבת', 4), ('ויאהב', 4), ('ואהב', 1), ('ואהבתם', 1)], 'have-affection-for': [('אהב', 5), ('אהבת', 2), ('אהבתי', 2), ('אהבים', 1), ('אהובה', 1)], 'circle-you/your (pl)': [('סביבתיכם', 2), ('סביבותיכם', 1)], 'in-nearest-part-you/your': [('בקרבך', 14)], 'to-good--in-the-widest-sense': [('לטוב', 2), ('לטובה', 2), ('לטבה', 1)], 'multiply-suffix': [('ירבין', 1), ('תרבון', 1)], 'flow-freely': [('זבת', 15), ('זב', 3), ('יזוב', 1), ('תזוב', 1)], 'be--long-suffix': [('תאריכן', 2), ('יאריכן', 1), ('יארכון', 1), ('יארכן', 1)], 'keep/guard-suffix': [('תשמרון', 4)], 'the-straight': [('הישר', 5)], 'hating-you/your': [('איביך', 16), ('איבך', 4)], 'to-live-us/our': [('לחיתנו', 1)], 'like-the-day': [('כהיום', 2)], 'inquire-you/your': [('ישאלך', 2), ('תשאלך', 1)], 'and-tie-them/their': [('וקשרתם', 1)], 'door-post': [('מזוזות', 1), ('מזוזת', 1)], 'from-over': [('מעל', 54)], 'in-dwell/sit-you/your': [('בשבתך', 3)], 'and-in-lie-down-you/your': [('ובשכבך', 2)], 'and-in-arise-you/your': [('ובקומך', 2)], 'and-pit-hole': [('ובור', 1), ('וברת', 1)], 'go-suffix': [('לכה', 10), ('תלכון', 2)], 'and-bad': [('ורע', 5), ('ורעים', 2), ('ורעות', 1)], 'garden': [('כרם', 4), ('כרמים', 2), ('גן', 1)], 'come/bring-you/your': [('באכה', 5), ('יביאך', 4), ('באך', 1), ('יבאך', 1), ('מביאך', 1)], 'to-signs': [('לאות', 9), ('לאת', 1), ('לאתת', 1)]}
GT = {g: store.execute("SELECT REPLACE(w.he_plain,'/',''), COUNT(*) FROM words w WHERE w.gloss=? GROUP BY 1 ORDER BY 2 DESC, 1", (g,)).fetchall() for g in GLOSS_FAMILY}
assert all(sorted(GT[g]) == sorted(v) for g, v in GLOSS_FAMILY.items()), [g for g, v in GLOSS_FAMILY.items() if sorted(GT[g]) != sorted(v)]
# BY GLOSS — every token of the gloss the one word (or one family read the same at every seat): the rewrite covers the whole store
OVERRIDE_GLOSS = [('and-point-them/their', 'and-you-shall-teach-them-diligently'), ('very-you/your', 'your-might'), ('to-fillet-for-the-forehead', 'for-frontlets'), ('and-rightness', 'and-righteousness'), ('rightness', 'righteousness'), ('to-push-away', 'to-thrust-out'), ('and-miracle', 'and-wonders'), ('and-desolate-you/your', 'and-destroy-you'), ('strike-in', 'plant'), ('and-grave-them/their', 'and-write-them'), ('deferred', 'tomorrow'), ('glow', 'be-kindled'), ('and-sate', 'and-be-satisfied'), ('and-have-affection-for', 'and-love'), ('have-affection-for', 'love'), ('circle-you/your (pl)', 'around-you'), ('in-nearest-part-you/your', 'in-your-midst'), ('to-good--in-the-widest-sense', 'for-good'), ('multiply-suffix', 'multiply'), ('flow-freely', 'flowing'), ('be--long-suffix', 'be-long'), ('keep/guard-suffix', 'keep'), ('the-straight', 'the-right'), ('hating-you/your', 'your-enemies'), ('to-live-us/our', 'to-keep-us-alive'), ('like-the-day', 'as-the-day'), ('inquire-you/your', 'asks-you'), ('and-tie-them/their', 'and-bind-them'), ('door-post', 'doorposts'), ('from-over', 'from-upon'), ('in-dwell/sit-you/your', 'when-you-sit'), ('and-in-lie-down-you/your', 'and-when-you-lie-down'), ('and-in-arise-you/your', 'and-when-you-rise')]
# BY REFERENCE — the family mixed (a homograph, two persons, a singular beside a plural): the seat named
OVERRIDE_REF_SPEC = [(2, 'אנכי', 'I', 0), (6, 'אנכי', 'I', 0), (15, 'אל', 'God', 0), (15, 'אף', 'anger', 0), (11, 'וברת', 'and-cisterns', 0), (11, 'חצובים', 'hewn', 0), (11, 'חצבת', 'hew', 0), (11, 'כרמים', 'vineyards', 0), (22, 'ורעים', 'and-grievous', 0), (14, 'תלכון', 'go', 0), (1, 'עברים', 'crossing', 0), (10, 'יביאך', 'brings-you', 0), (13, 'תעבד', 'serve', 0), (6, 'הדברים', 'the-words', 0), (8, 'לאות', 'for-a-sign', 0), (20, 'העדת', 'the-testimonies', 0), (17, 'ועדתיו', 'and-his-testimonies', 0), (2, 'חייך', 'your-life', 0), (12, 'עבדים', 'bondage', 0), (21, 'עבדים', 'slaves', 0), (1, 'המצוה', 'the-commandment', 0), (25, 'המצוה', 'the-commandment', 0), (14, 'אחרי', 'after', 0), (20, 'מה', 'what', 0)]
OVERRIDE_REF3 = [(f'Deut.6.{v}:{sidx(6, v, tok, nth)}', new, tok) for v, tok, new, nth in OVERRIDE_REF_SPEC]
OVERRIDE_REF = [(k, v) for k, v, _ in OVERRIDE_REF3]
assert len(OVERRIDE_REF) == 24 and len({k for k, _ in OVERRIDE_REF}) == 24 and len(OVERRIDE_GLOSS) == 33 and len({k for k, _ in OVERRIDE_GLOSS}) == 33, (len(OVERRIDE_REF), len(OVERRIDE_GLOSS))
assert all(g in GLOSS_FAMILY for g, _ in OVERRIDE_GLOSS) and all(sg(6, v, tok, nth) is not None for v, tok, _, nth in OVERRIDE_REF_SPEC)
ALREADY = ['to-goad', 'goad', 'goad-them/their', 'the-enactment', 'and-the-enactment', 'and-the-judgment', 'be--make-well', 'hinder', 'hind-part', 'living-being-you/your', 'mislay', 'to-set']   # the rewrites of sittings 1-3 the chapter shares, left standing
OV = open(f'{ROOT}/logic/glosses/word_gloss_overrides.yaml', encoding='utf-8').read()
PATCHED = 'THE DEUTERONOMY WALK sitting 4 (2026-09-17, Deuteronomy 6)' in OV
assert all(f'"{k}": ' in OV for k in ALREADY) and all(f'"{k}": ' not in OV for k, _ in OVERRIDE_GLOSS if not PATCHED) and (PATCHED or '"Deut.6.' not in OV), [k for k, _ in OVERRIDE_GLOSS if f'"{k}": ' in OV]
if PATCHED: assert all(f'"{k}": "{v}"' in OV for k, v in OVERRIDE_REF) and all(f'"{k}": "{v}"' in OV for k, v in OVERRIDE_GLOSS), [k for k, v in OVERRIDE_REF + OVERRIDE_GLOSS if f'"{k}": "{v}"' not in OV][:6]
assert OV.count('  "Deut.5.33:16": "you-shall-possess"') == 1

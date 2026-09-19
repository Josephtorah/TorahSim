import os as _os
_ROOT = _os.path.normpath(_os.path.join(_os.path.dirname(_os.path.abspath(__file__)), '..', '..', '..'))   # THE PORTABLE REPO (2026-09-15): the repo root from this file's own place
#!/usr/bin/env python3
# THE DEUTERONOMY WALK, sitting 7 — CHAPTER 9, Deuteronomy 9:1-29 (2026-09-19; the owner: "Let's keep run as it is and do another section"; ONE RUN
# under THE TWO-RUN RULE — the rereads, the measurements, the ink, the design, the rows, the ledger, the seat, the gates, the records): THE INK of the
# chapter, computed from the Tanakh DB, the snapshot store and the shelf's own bytes — never typed. Sitting 6's form (ch8_ink.py): the scaffold by hand,
# the constants and every assert chapter 9's own, typed FROM THE PRINTS (ch9_dump0.out, ch9_measure1.out). THE TWO DIVISIONS AGREE (29 = 29; the
# alignment the identity, cost 37). THE SPINE IS SILENT ON THE CHAPTER (36 on 6:9, 37 on 11:10 — chapters 7 to 10 have none); SEVEN rows elsewhere cite
# it by the union of both files — the forty days (9:9 at 14:1 and 306:25, with Exodus 34:28), the hyperbole rule (9:1 at 25:4), the ten names of prayer
# (9:25-26 at 26:7), the door opened (9:14 at 27:2), the harsh words before the blessing (9:7-8 at 342:1), the breaking of the tablets among the wonders
# (9:17 at 357:44). The parser MEASURED on every verse — SEVEN number verses (the forty days and nights four times, the two tablets and two hands), "swore"
# (9:5) no number; NO GAP. THE STORE = THE DB at every verse (no written/read pair in the chapter; 499 tokens, 1,973 letters; the three "?" glosses the
# store's split place names and "who?"). The hand's facts as asserts, run all at once by assert_driver.py after the measurement passes printed them.
import json, os, re, html, sqlite3, sys, io, contextlib, unicodedata, subprocess
from collections import Counter
ROOT = _ROOT
sys.path.insert(0, f'{ROOT}/World/step9')
DATE = '2026-09-19'
CH = 9
UIDS = ['deu_09_not_righteousness']
SPANS = {'deu_09_not_righteousness': (9, 1, 29)}
PREFIX = {'deu_09_not_righteousness': 'DV09'}
PISKAOT = []   # NO piska head on the chapter (typed from ch9_dump0's A print: the heads by chapter (6, 6), (11, 21); the nearest 36 on 6:9, 37 on 11:10)
EXP2DB = {e: [e] for e in range(1, 30)}   # the identity — 29 = 29 (chapter 5 the book's one split)
DB2EXP = {d: e for e, ds in EXP2DB.items() for d in ds}
# the Hebrew's book-named citations of chapter 9 (the regex reads "(דברים ט ט)"; the RANGE form "(דברים ט ז-ח)" at 342:1 it does not read — asserted by string below)
OUTSIDE_HE = [(14, 1, (9, 9)), (25, 4, (9, 1)), (26, 7, (9, 25)), (26, 7, (9, 26)), (27, 2, (9, 14)), (306, 25, (9, 9)), (357, 44, (9, 17))]
# the English's "(Dt.9:n" citations — nine hits on seven rows (26:7 twice, 342:1 twice — "(Dt.9:8)" then "(Dt.9:7)", the English's order)
OUTSIDE_EN = [(14, 1, (9, 9)), (25, 4, (9, 1)), (26, 7, (9, 25)), (26, 7, (9, 26)), (27, 2, (9, 14)), (306, 25, (9, 9)), (342, 1, (9, 8)), (342, 1, (9, 7)), (357, 44, (9, 17))]
OUTSIDE = [(14, 1), (25, 4), (26, 7), (27, 2), (306, 25), (342, 1), (357, 44)]   # the SEVEN rows READ WHOLE: the union of both files
INTERPOLATION = []   # no translator's own citation of chapter 9 (every English "(Dt.9:n)" quotes a verse the Hebrew quotes too — 342:1 the Hebrew's RANGE form)
EXCLUDED = []   # no slip on chapter 9 (no cited verse beyond 29); the English's 306:25 cites "Ex.36:28" for the Hebrew's Exodus 34:28 — a slip ON THE KIN'S citation, the row kept (asserted below)
CITED = {(14, 1): [9], (25, 4): [1], (26, 7): [25, 26], (27, 2): [14], (306, 25): [9], (342, 1): [7, 8], (357, 44): [17]}
CITED_DB = {k: v[0] for k, v in CITED.items()}
PRIOR_READ = {(14, 1): 'deu_01_03_devarim_2026-09-15.md', (25, 4): 'deu_01_03_devarim_2026-09-15.md', (26, 7): 'deu_01_03_devarim_2026-09-15.md', (27, 2): 'deu_01_03_devarim_2026-09-15.md'}   # four read before at sitting 1 (25:4 also at a Genesis sitting by topic) — REREAD WHOLE here
HEADS_ON = {14: (1, 14), 25: (1, 28), 26: (3, 23), 27: (3, 24), 306: (32, 1), 342: (33, 1), 357: (34, 1)}   # the piska's verse: the head where the first row carries one, else the row's own first citation (asserted by string)
FRESH = OUTSIDE[:]   # every one of the seven read whole this sitting
CREDITED = {}
TITLE = 'Chapter 9 — Not for your righteousness: the nations greater than you, the consuming fire, the oath to the fathers and the stiff neck; the calf retold — the forty days, the tablets of the covenant written with the finger of God, the breaking before your eyes, the prayer of forty days, Aaron\'s peril, the calf ground to dust; the four provocations; the intercession — Your people and Your inheritance'
OUT = f'{ROOT}/logic/oral_triage/deu_09_ekev_{DATE}.md'

def clean(s): return re.sub(r'<[^>]+>', '', html.unescape(s))
sif = json.load(open(f'{ROOT}/Data/sefaria_export/Sifrei_Devarim/en.json', encoding='utf-8'))['text']
sif_he = json.load(open(f'{ROOT}/Data/sefaria_export/Sifrei_Devarim/he.json', encoding='utf-8'))['text']
onk = json.load(open(f'{ROOT}/Data/sefaria_export/Onkelos_Deuteronomy/en.json', encoding='utf-8'))['text']
onk_he = json.load(open(f'{ROOT}/Data/sefaria_export/Onkelos_Deuteronomy/he.json', encoding='utf-8'))['text']
HN = {'א': 1, 'ב': 2, 'ג': 3, 'ד': 4, 'ה': 5, 'ו': 6, 'ז': 7, 'ח': 8, 'ט': 9, 'י': 10, 'כ': 20, 'ל': 30, 'מ': 40, 'נ': 50, 'ס': 60, 'ע': 70, 'פ': 80, 'צ': 90, 'ק': 100, 'ר': 200, 'ש': 300, 'ת': 400}
def hn(s): return sum(HN[c] for c in s if c in HN)
def E(p, r): return clean(sif[p - 1][r - 1])
def Hb(p, r): return clean(sif_he[p - 1][r - 1])
def plain(w): return ''.join(c for c in w if c != '/' and not (0x0591 <= ord(c) <= 0x05C7))
def pointed(w): return ''.join(c for c in w if c != '/' and not (0x0591 <= ord(c) <= 0x05AF))
def NF(s): return unicodedata.normalize('NFC', s)
def HB0(p, r): return plain(Hb(p, r))   # the Hebrew row's consonants (the asserts on the shelf's bytes by consonants — never on a typed pointing)
heads = {}
for p in range(1, 358):
    m = re.match(r'\(דברים ([א-ת]+) ([א-ת]+)(?:-[א-ת]+)?\)', Hb(p, 1))
    heads[p] = (hn(m.group(1)), hn(m.group(2))) if m else None
def head(p): return heads[p]
# THE SHELF BY POSITION — the heads around chapter 9: NONE on the chapter (nor on 7, 8, 10); 34-36 on 6:7-9 before, 37-38 on 11:10 and 39 on 11:11 after
assert len(sif) == 357 and len(sif_he) == 357 and sum(len(s) for s in sif) == 2357 and sum(len(s) for s in sif_he) == 2357
HC = Counter(h[0] for h in heads.values() if h)
assert [p for p, h in heads.items() if h and h[0] == 9] == [] and HC[7] == 0 and HC[8] == 0 and HC[9] == 0 and HC[10] == 0 and sorted(HC.items())[:9] == [(1, 24), (3, 4), (6, 6), (11, 21), (12, 20), (13, 14), (14, 14), (15, 16), (16, 19)], sorted(HC.items())[:9]
assert tuple(heads[36]) == (6, 9) and tuple(heads[37]) == (11, 10) and tuple(heads[38]) == (11, 10) and tuple(heads[39]) == (11, 11)
def he_cites(t): return [(b, hn(c), hn(v)) for b, c, v in re.findall(r'\(([א-ת]+(?: [א-ת])?) ([א-ת]{1,3}) ([א-ת]{1,3})\)', t)]
CIT_HE = [(p, r, (9, c[2])) for p in range(1, 358) for r in range(1, len(sif_he[p - 1]) + 1) for c in he_cites(Hb(p, r)) if c[0] == 'דברים' and c[1] == 9]
CIT_EN = [(p, r, (9, int(m.group(2)))) for p in range(1, 358) for r in range(1, len(sif[p - 1]) + 1) for m in re.finditer(r'\((?:Deut(?:eronomy)?\.?|Dt\.?|Devarim) ?(9):(\d+)', E(p, r))]
assert CIT_HE == OUTSIDE_HE and CIT_EN == OUTSIDE_EN, (CIT_HE, CIT_EN)
UNION = sorted({(p, r) for p, r, _ in CIT_HE} | {(p, r) for p, r, _ in CIT_EN})
assert UNION == OUTSIDE and len(UNION) == 7 and all(1 <= v <= 29 for _, _, (_, v) in CIT_HE + CIT_EN)   # a cited verse beyond the chapter's length would be a slip (chapter 6's lesson): none
assert [(p, r) for p in range(1, 358) for r in range(1, len(sif[p - 1]) + 1) if re.search(r'\((?:Ibid|ibid)\.? ?9:\d+\)', E(p, r))] == []
assert {p: heads[p] for p, _ in OUTSIDE} == {14: None, 25: (1, 28), 26: (3, 23), 27: None, 306: (32, 1), 342: None, 357: (34, 1)}, {p: heads[p] for p, _ in OUTSIDE}
# THE THREE PISKAOT WHOSE FIRST ROW CARRIES NO HEAD CITATION — the row's own first citation stands for the head (14:1 on 1:14, 27:2 on 3:24, 342:1 on 33:1), asserted by string
assert '(Dt.1:14)' in E(14, 1) and 'וַתַּעֲנוּ אֹתִי' in Hb(14, 1) and '(Dt.3:24)' in E(27, 2) and 'אַתָּה הַחִלּוֹתָ' in Hb(27, 2) and '(Dt.33:1)' in E(342, 1) and '(דברים לג, א)' in HB0(342, 1)
assert all(heads[p] == HEADS_ON[p] for p in (25, 26, 306, 357))
def has_points(s): return any(0x05B0 <= ord(c) <= 0x05BD for c in s)
assert all(has_points(Hb(p, r)) for p, r in OUTSIDE)
# THE RANGE CITATION the Hebrew regex does not read — 342:1 "(דברים ט ז-ח)" — found through the English's two citations, asserted by string
assert '(דברים ט ז-ח)' in HB0(342, 1) and '(Dt.9:8)' in E(342, 1) and '(Dt.9:7)' in E(342, 1) and E(342, 1).index('(Dt.9:8)') < E(342, 1).index('(Dt.9:7)')
# THE ROWS' CONTENT (the consonants of the shelf's bytes)
assert '(דברים ט ט)' in HB0(14, 1) and 'ארבעים יום' in HB0(14, 1) and 'שמונים אלף' in HB0(14, 1) and '(שמות לד כח)' in HB0(14, 1) and '(Dt.9:9)' in E(14, 1) and '(Ex.34:28)' in E(14, 1) and '80,000' in E(14, 1)   # from whom to learn Torah — from Moses who suffered forty days for it; the 80,000 judges
assert '(דברים ט א)' in HB0(25, 4) and 'לשון הביי' in HB0(25, 4) and 'רבן שמעון בן גמליאל' in HB0(25, 4) and '(בראשית כו ד)' in HB0(25, 4) and 'hyperbole' in E(25, 4) and '(Dt.9:1)' in E(25, 4) and '(Gn.26:4)' in E(25, 4)   # the Scriptures speak in hyperbole — 9:1's "to the heavens"; Abraham's stars not
assert 'עשרה לשונות' in HB0(26, 7) and 'נפול' in HB0(26, 7) and 'פלול' in HB0(26, 7) and '(דברים ט כה)' in HB0(26, 7) and '(דברים ט כו)' in HB0(26, 7) and 'prostration' in E(26, 7) and '(Dt.9:25)' in E(26, 7) and '(Dt. 9:26)' in E(26, 7)   # the ten names of prayer — 9:25 falling, 9:26 prayer
assert 'קל וחמר' in HB0(27, 2) and 'הרף ממני ואשמידם' in HB0(27, 2) and 'תפוס' in HB0(27, 2) and '(Dt.9:14)' in E(27, 2) and 'logic' in E(27, 2) and 'grab' in E(27, 2)   # the door opened — "let Me alone" (9:14); the a-fortiori (I1): one for many heard, the many for one all the more
assert '(דברים ט ט)' in HB0(306, 25) and 'ארבעים יום וארבעים לילה' in HB0(306, 25) and 'המלאכים' in HB0(306, 25) and 'השרפים' in HB0(306, 25) and '(שמות לד כח)' in HB0(306, 25) and '(Dt.9:9)' in E(306, 25) and 'Ex.36:28' in E(306, 25) and '(Is.6:2)' in E(306, 25)   # Moses' suffering for the Torah; THE ENGLISH'S SLIP "Ex.36:28" for the Hebrew's 34:28
assert 'דברים קשים' in HB0(342, 1) and 'ובחרב הקצפתם' in HB0(342, 1) and 'ממרים הייתם' in HB0(342, 1) and 'harsh words' in E(342, 1) and '(Dt.33:1)' in E(342, 1)   # the harsh words first (9:7-8 among them), then the blessing
assert 'רבי אלעזר' in HB0(357, 44) and 'בשבור הלוחות' in HB0(357, 44) and 'ואשברם לעיניכם' in HB0(357, 44) and 'לעיני כל ישראל' in HB0(357, 44) and '(Dt.9:17)' in E(357, 44) and '(Dt.34:12)' in E(357, 44) and 'R. Elazar' in E(357, 44)   # the breaking of the tablets among the wonders: 9:17 "before your eyes" — 34:12 "before the eyes of all Israel" (the verbal analogy, I2)
# THE PRIOR READS — the strict row form over every ledger: FOUR of the seven read before (14:1, 25:4, 26:7, 27:2 at sitting 1; 25:4 also at a Genesis sitting by topic) — every one REREAD WHOLE here; no Onkelos row of chapter 9 anywhere
TRI = f'{ROOT}/logic/oral_triage'
LED = {f: open(f'{TRI}/{f}', encoding='utf-8').read() for f in os.listdir(TRI) if f.endswith('.md') and os.path.isfile(f'{TRI}/{f}') and f'{TRI}/{f}' != OUT}
PRIOR = sorted({(f, int(a), int(b)) for f, t in LED.items() for a, b in re.findall(r'Sifrei Devarim (\d+):(\d+)', t)})
assert [(f, p, r) for f, p, r in PRIOR if (p, r) in OUTSIDE] == [('deu_01_03_devarim_2026-09-15.md', 14, 1), ('deu_01_03_devarim_2026-09-15.md', 25, 4), ('deu_01_03_devarim_2026-09-15.md', 26, 7), ('deu_01_03_devarim_2026-09-15.md', 27, 2), ('gen_29_separation_promise_2026-08-25.md', 25, 4)] and len(PRIOR) == 313, (len(PRIOR), [(f, p, r) for f, p, r in PRIOR if (p, r) in OUTSIDE])
assert sorted(f for f, t in LED.items() if re.search(r'^- Onkelos Deut 9:', t, re.M)) == []
NAMING = sorted(f for f, t in LED.items() if re.search(r'Deut(?:eronomy)? 9:\d+', t))
assert NAMING == ['erection_docket_2026-09-06.md', 'exo_29_investiture_2026-09-01.md', 'lev_08_milluim_2026-09-03.md', 'lev_26_blessings_curses_2026-09-05.md', 'num_01_levites_exempt_2026-09-09.md', 'num_03_levite_clans_count_2026-09-09.md', 'num_11_complaint_quail_2026-09-10.md', 'num_12_miriam_2026-09-10.md', 'num_13_spies_sent_2026-09-10.md', 'num_14_rejection_2026-09-10.md', 'num_32_gad_reuben_2026-09-12.md', 'num_33_journeys_2026-09-12.md'], NAMING
assert 'Deut 9:20' in LED['lev_08_milluim_2026-09-03.md'] and 'Deuteronomy 9:20' in LED['exo_29_investiture_2026-09-01.md'] and 'Deut 9:22' in LED['num_11_complaint_quail_2026-09-10.md'] and 'Deut 9:14' in LED['num_14_rejection_2026-09-10.md'] and 'Deut 9:17' not in ''.join(LED.values())
# THE KIN'S READS: the calf, the ascent, the second tablets and the craftsmen were read at the Exodus sittings (Onkelos rows over their ledgers); the testing places and the spies at the Numbers walk
def kinrows(f, pat): return len(re.findall(r'^- Onkelos ' + pat, LED[f], re.M))
EXO_KIN = sorted(f for f, t in LED.items() if re.search(r'^- Onkelos Exod (24|31|32|34|17):', t, re.M))
assert EXO_KIN[:5] == ['erection_docket_2026-09-06.md', 'exo_24_covenant_ascent_2026-09-01.md', 'exo_31_craftsmen_shabbat_2026-09-01.md', 'exo_32_golden_calf_2026-09-01.md', 'exo_34_second_tablets_2026-09-01.md'] and len(EXO_KIN) == 6, EXO_KIN
assert sorted(f for f, t in LED.items() if re.search(r'^- Onkelos Num (11|13|14):', t, re.M)) == ['num_11_complaint_quail_2026-09-10.md', 'num_13_spies_sent_2026-09-10.md', 'num_14_rejection_2026-09-10.md']
assert kinrows('exo_32_golden_calf_2026-09-01.md', r'Exod 32:\d+\b') >= 1 and kinrows('exo_24_covenant_ascent_2026-09-01.md', r'Exod 24:1[2-8]\b') >= 1 and kinrows('num_11_complaint_quail_2026-09-10.md', r'Num 11:(?:[1-3]|3[1-5])\b') >= 2 and kinrows('num_14_rejection_2026-09-10.md', r'Num 14:\d+\b') >= 10
ONK_LEN = {c: len(onk[c - 1]) for c in (3, 4, 5, 6, 7, 8, 9)}
assert len(onk) == 34 and len(onk_he) == 34 and ONK_LEN == {3: 29, 4: 49, 5: 30, 6: 25, 7: 26, 8: 20, 9: 29} and sum(len(c) for c in onk_he) == 956
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
assert VC[5] == 33 and VC[6] == 25 and VC[7] == 26 and VC[8] == 20 and VC[9] == 29 and VC[10] == 22 and sum(VC.values()) == 959 and len(VC) == 34
assert [(c, len(onk_he[c - 1]), VC[c]) for c in range(1, 35) if len(onk_he[c - 1]) != VC[c]] == [(5, 30, 33)]
# THE ALIGNMENT RECOMPUTED (ch9_dump0's A0): the export's twenty-nine rows against the DB's twenty-nine verses over token and negation counts — the identity, cost 37
by9 = {v: [plain(he) for he, in db.execute("SELECT w.he FROM words w JOIN verses v ON w.verse_id=v.id WHERE v.book='Deut' AND v.chapter=9 AND v.verse=? ORDER BY w.idx", (v,))] for v in range(1, 30)}
NEG = ('לא', 'ולא')
D_ = [(len(by9[v]), sum(1 for x in by9[v] if x in NEG)) for v in range(1, 30)]
E_ = [(len(plain(clean(r)).split()), sum(1 for x in plain(clean(r)).split() if x.strip('.:') in NEG)) for r in onk_he[8]]
def _cost(e, ds): return abs(e[0] - sum(d[0] for d in ds)) + 3 * abs(e[1] - sum(d[1] for d in ds))
INF = 10 ** 9; best = {(0, 0): (0, None)}
for i in range(1, 30):
    for j in range(i, 30):
        cands = [(best[(i - 1, k)][0] + _cost(E_[i - 1], D_[k:j]), k) for k in range(i - 1, j) if (i - 1, k) in best and j - k <= 4]
        best[(i, j)] = min(cands) if cands else (INF, None)
i, j, ALIGN = 29, 29, {}
while i > 0:
    k = best[(i, j)][1]; ALIGN[i] = list(range(k + 1, j + 1)); i, j = i - 1, k
assert ALIGN == EXP2DB and best[(29, 29)][0] == 37 and Counter(ds[0] - e for e, ds in EXP2DB.items()) == Counter({0: 29}) and len(onk_he[8]) == 29 == VC[9], (best[(29, 29)][0], ALIGN)
def unit_text(uid): return open(f'{ROOT}/logic/units/{uid}.yaml', encoding='utf-8').read()
def steps(uid): return sorted({(int(a), int(b)) for a, b in re.findall(r'STEP_Dt_(\d+)_(\d+)', unit_text(uid))})
FIRST = not os.path.exists(OUT)
for uid, (c, lo, hi) in SPANS.items():
    t = unit_text(uid)
    assert steps(uid) == [(c, v) for v in range(lo, hi + 1)] and re.search(rf'refs: "?{c}:{lo}-{hi}"?', t) and '\nbinary_trees:' in t, uid
    if FIRST: assert 'status: draft' in t and 'operators:' not in t and '- step: E' not in t, uid
    assert t.count(f'  - id: STEP_Dt_{c}_{lo}\n') == 1 and t.count(f'  - id: STEP_Dt_{c}_{hi}\n') == 1, uid
UT9 = unit_text('deu_09_not_righteousness')
assert UT9.count('\n    comment:') + UT9.count('\n      comment:') == 33 and UT9.count('\n  - id: S') == 36   # typed from ch9_dump0's G print (the draft's comment lines and scenarios)
assert 'deu_08_manna_humility' in UT9 and 'exo_32_golden_calf' in UT9 and 'status: frozen' in unit_text('deu_08_manna_humility') and 'status: frozen' in unit_text('exo_32_golden_calf')
assert sorted(f for f in os.listdir(TRI) if f.startswith('deu_') and f != os.path.basename(OUT)) == ['deu_01_03_devarim_2026-09-15.md', 'deu_01_03_devarim_exam_2026-09-15.md', 'deu_04_vaetchanan_2026-09-16.md', 'deu_04_vaetchanan_exam_2026-09-16.md', 'deu_05_vaetchanan_2026-09-16.md', 'deu_05_vaetchanan_exam_2026-09-16.md', 'deu_06_vaetchanan_2026-09-17.md', 'deu_06_vaetchanan_exam_2026-09-17.md', 'deu_07_vaetchanan_ekev_2026-09-17.md', 'deu_07_vaetchanan_ekev_exam_2026-09-18.md', 'deu_08_ekev_2026-09-18.md', 'deu_08_ekev_exam_2026-09-19.md']
ALLTXT = ''.join(open(f'{ROOT}/logic/units/{f}', encoding='utf-8').read() for f in os.listdir(f'{ROOT}/logic/units') if f.endswith('.yaml') and f[:-5] not in UIDS) + ''.join(open(f'{ROOT}/logic/oral_audit/manifests/{f}', encoding='utf-8').read() for f in os.listdir(f'{ROOT}/logic/oral_audit/manifests') if f.endswith('.json'))
assert all(f'"{p}-' not in ALLTXT and f'[claim {p}-' not in ALLTXT for p in PREFIX.values())
SPAN = [(9, v) for v in range(1, VC[9] + 1)]
NV = 29
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
def W9(v): return words('Deut', 9, v)
def PT(b, c, v, tok): return [NF(x) for x in byp[(b, c, v)] if plain(x) == tok]
def SEAT(s): b, cv = s.split(); c, v = map(int, cv.split(':')); return (b, c, v)
def DIFF(a, b_):
    import difflib
    A, B = words(*a), words(*b_)
    return [(op, A[i1:i2], B[j1:j2]) for op, i1, i2, j1, j2 in difflib.SequenceMatcher(None, A, B).get_opcodes() if op != 'equal']
def SHARED(a, b_):
    import difflib
    A, B = words(*a), words(*b_)
    m = difflib.SequenceMatcher(None, A, B).find_longest_match(0, len(A), 0, len(B))
    return A[m.a:m.a + m.size]
def SHN(a, b_):
    """the tokens shared in order (the sum of the equal runs of the diff) — the measure ch9_measure1's A section summarized"""
    import difflib
    A, B = words(*a), words(*b_)
    return sum(i2 - i1 for op, i1, i2, _, _ in difflib.SequenceMatcher(None, A, B).get_opcodes() if op == 'equal')
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
def onk_seats(sub): return [(c + 1, v + 1) for c in range(34) for v in range(len(onk_he[c])) if sub in arm_e(c + 1, v + 1)]      # EXPORT verse numbers
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
for c, v, idx, hp, g in store.execute("SELECT v.chapter, v.verse, w.idx, w.he_plain, w.gloss FROM words w JOIN verses v ON w.verse_id=v.id WHERE v.book='Deut' AND v.chapter = 9 ORDER BY v.id, w.idx"):
    SG.setdefault((c, v), []).append((idx, hp.replace('/', ''), g))
def sg(c, v, tok, nth=0):
    hit = [g for _, hp, g in SG[(c, v)] if hp == tok]
    if len(hit) <= nth: raise KeyError((c, v, tok, nth))
    return hit[nth]
def sidx(c, v, tok, nth=0):
    hit = [i for i, hp, _ in SG[(c, v)] if hp == tok]
    assert len(hit) > nth, (c, v, tok, nth, hit)
    return hit[nth]
STORE_MISMATCH = [(c, v, n, len(by[('Deut', c, v)])) for c, v, n in store.execute("SELECT v.chapter, v.verse, COUNT(*) FROM words w JOIN verses v ON w.verse_id=v.id WHERE v.book='Deut' AND v.chapter=9 GROUP BY v.chapter, v.verse").fetchall() if n != len(by[('Deut', c, v)])]
# THE STORE = THE DB at EVERY verse — no written/read pair in the chapter (wtype None at all 499 tokens); 1,973 letters; the three "?" glosses the store's split
# place names (9:22 "and-in-?" the Kibroth of Kibroth-hattaavah, 9:23 "from-?" the Kadesh of Kadesh-barnea) and 9:2's "who?"
assert STORE_MISMATCH == [] and sum(len(SG[(9, v)]) for v in range(1, 30)) == 499 == sum(len(W9(v)) for v in range(1, 30)) and sum(len(x) for v in range(1, 30) for x in W9(v)) == 1973
assert [(v, x, m, wt) for v in range(1, 30) for (x, m), wt in zip(by[('Deut', 9, v)], byw[('Deut', 9, v)]) if wt] == [] and Counter(wt for v in range(1, 30) for wt in byw[('Deut', 9, v)]) == Counter({None: 499})
assert [(v, i, hp, g) for (c, v), L in sorted(SG.items()) for i, hp, g in L if '?' in g] == [(2, 10, 'מי', 'who?'), (22, 2, 'ובקברת', 'and-in-?'), (23, 3, 'מקדש', 'from-?')]
assert {v: len(W9(v)) for v in range(1, 30)} == {1: 17, 2: 15, 3: 22, 4: 22, 5: 28, 6: 18, 7: 25, 8: 9, 9: 23, 10: 22, 11: 15, 12: 22, 13: 13, 14: 14, 15: 13, 16: 17, 17: 9, 18: 24, 19: 17, 20: 11, 21: 26, 22: 8, 23: 24, 24: 7, 25: 16, 26: 18, 27: 15, 28: 20, 29: 9}
# THE ENGINE'S PARSER on every verse — MEASURED before the compile is asked: SEVEN number verses — the forty days and nights [40, 40] at 9:9, 9:11, 9:18, 9:25;
# the two tablets [2] at 9:10, 9:11; the two tablets and the two hands [2, 2] at 9:15, 9:17; "swore" (9:5, the lemma 7650) not a number at all; no ordinal; NO GAP.
# The kin: Exodus 24:18 [40, 40], 34:28 [40, 40, 10] (the ten words), 31:18 [2], 32:15 [2], Deuteronomy 4:13 [10, 2], 10:4 [10] with the ordinal [1] ("the
# first writing"), 10:10 [40, 40]; Genesis 7:4 [7, 40, 40], 7:12 [40, 40]; Exodus 32:28 [3000] (the calf's dead).
with contextlib.redirect_stdout(io.StringIO()):
    import cold_run_sequence as CS
NUMS = {v: CS.ink_numbers(CS.verse_words('Deut', 9, v)) for v in range(1, 30)}
ORDS = {v: CS.ink_ordinals(CS.verse_words('Deut', 9, v)) for v in range(1, 30)}
assert {v: n for v, n in NUMS.items() if n} == {9: [40, 40], 10: [2], 11: [40, 40, 2], 15: [2, 2], 17: [2, 2], 18: [40, 40], 25: [40, 40]} and all(o == [] for o in ORDS.values()), NUMS
assert CS.verse_words('Deut', 9, 10)[4] == 'שני^' and CS.verse_words('Deut', 9, 15)[7:] == ['ושני^', 'לחת', 'הברית', 'על', 'שתי^', 'ידי'] and CS.verse_words('Deut', 9, 17)[1] == 'בשני^'
assert [(b, c, v, CS.ink_numbers(CS.verse_words(b, c, v))) for b, c, v in (('Exod', 24, 18), ('Exod', 34, 28), ('Exod', 31, 18), ('Exod', 32, 15), ('Deut', 4, 13), ('Deut', 10, 4), ('Deut', 10, 10), ('Gen', 7, 4), ('Gen', 7, 12), ('Exod', 32, 28), ('1Kgs', 19, 8), ('Num', 13, 25))] == [('Exod', 24, 18, [40, 40]), ('Exod', 34, 28, [40, 40, 10]), ('Exod', 31, 18, [2]), ('Exod', 32, 15, [2]), ('Deut', 4, 13, [10, 2]), ('Deut', 10, 4, [10]), ('Deut', 10, 10, [40, 40]), ('Gen', 7, 4, [7, 40, 40]), ('Gen', 7, 12, [40, 40]), ('Exod', 32, 28, [3000]), ('1Kgs', 19, 8, [40, 40]), ('Num', 13, 25, [40])]
assert CS.ink_ordinals(CS.verse_words('Deut', 10, 4)) == [1] and CS.ink_ordinals(CS.verse_words('Exod', 34, 28)) == []
assert PT('Deut', 9, 5, 'נשבע') == ['נִשְׁבַּע'] and lemma_of('Deut', 9, 5, 'נשבע') == ['7650'] and [s for s, x, m in LEMT('7650', books=('Deut',)) if s.startswith('Deut 9:')] == ['Deut 9:5'] and [s for s, _, _ in LEMT('7646', books=('Deut',)) if s.startswith('Deut 9:')] == []
# THE THREE SPELLINGS OF "TABLETS" — the lemma 3871 in the chapter: לוחת (plene vav — 9:9 twice, 9:10; elsewhere 10:1 alone), לחת (defective — 9:11, 9:15; Exodus's form throughout),
# לחות (the second plene — 9:11; 4:13 and 1 Kings 8:9 its kin); 9:11 holds TWO spellings in one verse; the article's form הלחת at 9:17
assert [(x, v) for v in range(1, 30) for x in W9(v) if x in ('לוחת', 'לחת', 'לחות', 'הלחת')] == [('לוחת', 9), ('לוחת', 9), ('לוחת', 10), ('לחת', 11), ('לחות', 11), ('לחת', 15), ('הלחת', 17)]
assert U('לוחת') == ['Deut 10:1', 'Deut 9:10', 'Deut 9:9'] and U('לחות') == ['1Kgs 8:9', 'Deut 4:13', 'Deut 9:11'] and U('לוחות') == [] and len(U('לחת')) == 12 and len(U('הלחת')) == 10 and len(LEMT('3871')) == 43
assert PT('Deut', 9, 9, 'לוחת') == ['לוּחֹת', 'לוּחֹת'] and PT('Deut', 9, 11, 'לחת') == ['לֻחֹת'] and PT('Deut', 9, 11, 'לחות') == ['לֻחוֹת']
assert [(x, v, m) for v in range(1, 30) for x, m in wm('Deut', 9, v) if x in ('שני', 'שתי', 'ושני', 'בשני')] == [('שני', 10, 'HAcmdc'), ('שני', 11, 'HAcmdc'), ('ושני', 15, 'HC/Acmdc'), ('שתי', 15, 'HAcfdc'), ('בשני', 17, 'HR/Acmdc'), ('שתי', 17, 'HAcfdc')]
assert [x for x, m in wm('Deut', 9, 10) if m == 'HVqsmpa'] == ['כתבים'] and [x for x, m in wm('Deut', 9, 21) if m in ('HVqa', 'HVha')] == ['טחון', 'היטב'] and lemma_of('Deut', 9, 22, 'ובקברת') == ['6914+'] and lemma_of('Deut', 9, 23, 'מקדש') == ['6947+']
# THE FRAMES AND THE REGISTER: TWO divine frames INSIDE the retelling (9:12, 9:13 — God's speech of Exodus 32:7-9 quoted); "saying" 9:4 (the boaster's), 9:13, 9:23;
# the narrative verbs TWENTY-TWO in sixteen verses over 9:8-26 (chapter 8 had three); the first person Moses' in eighteen verses (9:4 the boaster's "my
# righteousness … brought me"); the second person SINGULAR in twelve verses (1-6 Israel; 12, 14 GOD'S "you" to Moses; 26-29 MOSES' "You" to God), PLURAL in
# twelve (8-10, 16-19, 21-25), BOTH in 9:7 alone (the switch inside the verse), NEITHER in 11, 13, 15, 20; imperatives SIX — "hear", "remember" twice, "arise,
# go down" and "let alone" (God's), "go up" (God's, plural); infinitive absolutes "quickly" four times and "grinding thoroughly" (9:21 — two side by side);
# consecutive perfects FOUR, all at 9:3 and 9:6 (the law's form only at the opening); NO prohibition "not + imperfect" — the chapter's "not"s are perfects;
# "for/that" seven seats, "lest" ONE (9:28), no "if"; "so that" ONE (9:5; the book's forty-three); the Name thirty-four bare tokens; "the LORD your God"
# singular at 3-7 and plural at 23 alone; "God" bare at 9:10 (the finger); MOSES NEVER NAMED (the chapter his "I"); Aaron at 9:20; Israel at 9:1.
NUM = {v: (sum(1 for _, m in by[('Deut', 9, v)] if m and '2mp' in m), sum(1 for _, m in by[('Deut', 9, v)] if m and '2ms' in m)) for v in range(1, 30)}
assert [v for v, (p, s) in NUM.items() if s and not p] == [1, 2, 3, 4, 5, 6, 12, 14, 26, 27, 28, 29] and [v for v, (p, s) in NUM.items() if p and not s] == [8, 9, 10, 16, 17, 18, 19, 21, 22, 23, 24, 25] and [v for v, (p, s) in NUM.items() if p and s] == [7] and [v for v, (p, s) in NUM.items() if not p and not s] == [11, 13, 15, 20]
assert [(x, m) for x, m in wm('Deut', 9, 7) if m and '2mp' in m] == [('באכם', 'HVqc/Sp2mp'), ('הייתם', 'HVqp2mp')] and NUM[7] == (2, 5) and NUM[23] == (8, 0) and NUM[16] == (6, 0)
assert {v: [x for x, m in wm('Deut', 9, v) if m and re.match(r'^HV.?.?v', m)] for v in range(1, 30) if any(m and re.match(r'^HV.?.?v', m) for _, m in by[('Deut', 9, v)])} == {1: ['שמע'], 7: ['זכר'], 12: ['קום', 'רד'], 14: ['הרף'], 23: ['עלו'], 27: ['זכר']}
assert {v: [x for x, m in wm('Deut', 9, v) if m and re.match(r'^H(?:C/)?V.a$', m)] for v in range(1, 30) if any(m and re.match(r'^H(?:C/)?V.a$', m) for _, m in by[('Deut', 9, v)])} == {3: ['מהר'], 12: ['מהר', 'מהר'], 16: ['מהר'], 21: ['טחון', 'היטב']}
assert {v: [x for x, m in wm('Deut', 9, v) if m and re.search(r'^HC/V.q', m)] for v in range(1, 30) if any(m and re.search(r'^HC/V.q', m) for _, m in by[('Deut', 9, v)])} == {3: ['וידעת', 'והורשתם', 'והאבדתם'], 6: ['וידעת']}
assert [v for v in range(1, 30) if any(m and re.search(r'^H(?:Ti/)?V.i2', m) for _, m in by[('Deut', 9, v)])] == []
WAY = {v: [x for x, m in wm('Deut', 9, v) if m and re.search(r'^HC/V.w', m)] for v in range(1, 30) if any(m and re.search(r'^HC/V.w', m) for _, m in by[('Deut', 9, v)])}
assert WAY == {8: ['ויתאנף'], 9: ['ואשב'], 10: ['ויתן'], 11: ['ויהי'], 12: ['ויאמר'], 13: ['ויאמר'], 15: ['ואפן', 'וארד'], 16: ['וארא'], 17: ['ואתפש', 'ואשלכם', 'ואשברם'], 18: ['ואתנפל'], 19: ['וישמע'], 20: ['ואתפלל'], 21: ['ואשרף', 'ואכת', 'ואשלך'], 23: ['ותמרו'], 25: ['ואתנפל'], 26: ['ואתפלל', 'ואמר']} and sum(len(v) for v in WAY.values()) == 22 and len(WAY) == 16
assert sorted(v for v in range(1, 30) if any(m and '1cs' in m for _, m in by[('Deut', 9, v)])) == [4, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 23, 24, 25, 26] and {v: [x for x, m in wm('Deut', 9, v) if m and '1cp' in m] for v in range(1, 30) if any(m and '1cp' in m for _, m in by[('Deut', 9, v)])} == {28: ['הוצאתנו']}
assert [(x, m) for x, m in wm('Deut', 9, 4) if m and '1cs' in m] == [('בצדקתי', 'HR/Ncfsc/Sp1cs'), ('הביאני', 'HVhp3ms/Sp1cs')]   # the boaster's first person — the chapter's only "I" that is not Moses'
assert {v: [x for x in W9(v) if x in ('לא', 'ולא')] for v in range(1, 30) if any(x in ('לא', 'ולא') for x in W9(v))} == {5: ['לא'], 6: ['לא'], 9: ['לא', 'לא'], 18: ['לא', 'לא'], 23: ['ולא', 'ולא']}
assert [(v, by[('Deut', 9, v)][i + 1][0]) for v in range(1, 30) for i, (x, _) in enumerate(by[('Deut', 9, v)][:-1]) if x in ('לא', 'ולא') and by[('Deut', 9, v)][i + 1][1] and re.match(r'^HV.i', by[('Deut', 9, v)][i + 1][1])] == []   # no "not + imperfect" — the negatives are all perfects (did not eat, drink, believe, hearken) or nouns
assert {f'9:{v}': [x for x in W9(v) if x in ('כי', 'אם', 'ואם', 'או', 'פן')] for v in range(1, 30) if any(x in ('כי', 'אם', 'ואם', 'או', 'פן') for x in W9(v))} == {'9:3': ['כי'], '9:5': ['כי'], '9:6': ['כי', 'כי'], '9:12': ['כי'], '9:19': ['כי'], '9:25': ['כי'], '9:28': ['פן']}
assert [v for v in range(1, 30) if 'לאמר' in W9(v)] == [4, 13, 23] and [v for v in range(1, 30) if any(W9(v)[i:i + 2] in (['ויאמר', 'יהוה'], ['וידבר', 'יהוה']) for i in range(len(W9(v)) - 1))] == [12, 13]
assert (sum(1 for v in range(1, 30) for x in W9(v) if x in ('למען', 'ולמען')), len(U('למען', 'ולמען', books=('Deut',)))) == (1, 43) and [v for v in range(1, 30) if 'ולמען' in W9(v)] == [5]
assert {v: sum(1 for x in W9(v) if x in ('יהוה', 'ליהוה', 'ויהוה', 'ביהוה', 'מיהוה')) for v in range(1, 30) if any(x in ('יהוה', 'ליהוה', 'ויהוה', 'ביהוה', 'מיהוה') for x in W9(v))} == {3: 2, 4: 3, 5: 2, 6: 1, 7: 2, 8: 2, 9: 1, 10: 2, 11: 1, 12: 1, 13: 1, 16: 2, 18: 2, 19: 2, 20: 1, 22: 1, 23: 2, 24: 1, 25: 2, 26: 2, 28: 1} and sum(1 for v in range(1, 30) for x in W9(v) if x in ('יהוה', 'ליהוה', 'ויהוה', 'ביהוה', 'מיהוה')) == 34
assert [v for v in range(1, 30) if any(W9(v)[i:i + 2] == ['יהוה', 'אלהיך'] for i in range(len(W9(v)) - 1))] == [3, 4, 5, 6, 7] and [v for v in range(1, 30) if any(W9(v)[i:i + 2] == ['יהוה', 'אלהיכם'] for i in range(len(W9(v)) - 1))] == [23] and [v for v in range(1, 30) if 'אלהים' in W9(v)] == [10]
assert {n: [v for v in range(1, 30) if n in W9(v)] for n in ('משה', 'אהרן', 'ובאהרן', 'ישראל', 'מצרים', 'ממצרים', 'ובחרב', 'הירדן', 'לאברהם', 'ליצחק', 'וליעקב', 'ענק', 'ענקים')} == {'משה': [], 'אהרן': [20], 'ובאהרן': [20], 'ישראל': [1], 'מצרים': [7], 'ממצרים': [12, 26], 'ובחרב': [8], 'הירדן': [1], 'לאברהם': [5, 27], 'ליצחק': [5, 27], 'וליעקב': [5, 27], 'ענק': [2], 'ענקים': [2]}
PARTS = {v: [x for x, m in wm('Deut', 9, v) if m and re.search(r'^H(?:C/|R/|Td/|C/R/)?V.r', m)] for v in range(1, 30) if any(m and re.search(r'^H(?:C/|R/|Td/|C/R/)?V.r', m) for _, m in by[('Deut', 9, v)])}
assert PARTS == {1: ['עבר'], 2: ['ורם'], 3: ['העבר', 'אכלה'], 4: ['מורישם'], 5: ['בא', 'מורישם'], 6: ['נתן'], 7: ['ממרים'], 15: ['בער'], 21: ['הירד'], 22: ['מקצפים'], 24: ['ממרים']}
# THE KIN DIFFED (the DB's tokens; SHN the tokens shared in order — the first typed pass wrote 0 where a single token is shared: 9:17 against Exodus 32:19 ONE, 9:19 against 32:14 ONE, 9:20 against 32:21 ONE, 9:28 against 32:12 TWO; retyped from the print): 9:13 against Exodus 32:9 ELEVEN of thirteen — the closest row of the chapter, God's word
# quoted whole but for "to me, saying"; 9:12 against 32:8 nine ("turned aside quickly from the way which I commanded them; they have made them") and 32:7
# six; 9:9 against Exodus 34:28 nine, 24:18 five ("on the mountain forty days and forty nights"), 24:8 five ("the covenant which the LORD cut with you" —
# the blood's verse) and 9:18 eleven (the doublet); 9:10 against 10:4 ten, 5:4 six, Exodus 31:18 five ("written with the finger of God"); 9:11 against
# 34:28 seven; 9:14 against Exodus 32:10 three ("and I will make you into a nation") and Numbers 14:12 three single tokens — THREE FORMS OF THE OFFER;
# 9:15 against 32:15 four; 9:16 against 32:8 four and 32:4 three ("a molten calf"); 9:17 against Exodus 32:19 NOTHING — the breaking retold in Moses' own
# words; 9:18 against 34:28 ten; 9:19 against 10:10 six and Exodus 32:14 nothing (the relenting told as "hearkened"); 9:20 against Exodus 32:21 nothing —
# Aaron's peril told ONLY HERE; 9:21 against 32:20 seven ("the calf … until it was fine"); 9:23 against 1:26 five and Joshua 14:7 five; 9:26 against
# 1 Kings 8:51 five (Solomon quoting this telling) and Exodus 32:11 five; 9:27 against Exodus 32:13 three ("to Abraham, to Isaac" — ISRAEL there, JACOB
# here); 9:28 against Numbers 14:16 seven and Exodus 32:12 nothing; 9:29 against 1 Kings 8:51 four. The opening: 9:1 against 4:38 four, 9:2 against 1:28
# five, 9:3 against 31:3 nine and 4:24 six, 9:5 against 30:20 ten, 9:6 against Exodus 33:3 seven, 9:7 against 11:5 six.
D9 = lambda v: ('Deut', 9, v)
assert SHN(D9(13), ('Exod', 32, 9)) == 11 and SHARED(D9(13), ('Exod', 32, 9)) == ['ראיתי', 'את', 'העם', 'הזה', 'והנה', 'עם', 'קשה', 'ערף', 'הוא'] and DIFF(D9(13), ('Exod', 32, 9)) == [('replace', ['אלי', 'לאמר'], ['אל', 'משה'])]
assert SHN(D9(12), ('Exod', 32, 8)) == 9 and SHN(D9(12), ('Exod', 32, 7)) == 6 and SHARED(D9(12), ('Exod', 32, 8)) == ['סרו', 'מהר', 'מן', 'הדרך', 'אשר', 'צויתם', 'עשו', 'להם']
assert SHN(D9(9), ('Exod', 34, 28)) == 9 and SHN(D9(9), ('Exod', 24, 18)) == 5 and SHN(D9(9), ('Exod', 24, 8)) == 5 and SHN(D9(9), D9(18)) == 11 and SHARED(D9(9), ('Exod', 24, 8)) == ['הברית', 'אשר', 'כרת', 'יהוה', 'עמכם']
assert SHN(D9(10), ('Deut', 10, 4)) == 10 and SHN(D9(10), ('Deut', 5, 4)) == 6 and SHN(D9(10), ('Exod', 31, 18)) == 5 and SHARED(D9(10), ('Exod', 31, 18)) == ['כתבים', 'באצבע', 'אלהים'] and SHN(D9(11), ('Exod', 34, 28)) == 7
assert SHN(D9(14), ('Exod', 32, 10)) == 3 and SHARED(D9(14), ('Exod', 32, 10)) == ['ואעשה', 'אותך', 'לגוי'] and SHN(D9(14), ('Num', 14, 12)) == 3 and len(SHARED(D9(14), ('Num', 14, 12))) == 1
assert SHN(D9(15), ('Exod', 32, 15)) == 4 and SHN(D9(16), ('Exod', 32, 8)) == 4 and SHN(D9(16), ('Exod', 32, 4)) == 3 and SHARED(D9(16), ('Exod', 32, 4)) == ['עגל', 'מסכה']
assert SHN(D9(17), ('Exod', 32, 19)) == 1 and SHN(D9(18), ('Exod', 34, 28)) == 10 and SHN(D9(19), ('Deut', 10, 10)) == 6 and SHN(D9(19), ('Exod', 32, 14)) == 1 and SHN(D9(20), ('Exod', 32, 21)) == 1 and SHN(D9(20), ('Exod', 32, 35)) == 2 and len(SHARED(D9(17), ('Exod', 32, 19))) == 1
assert SHN(D9(21), ('Exod', 32, 20)) == 7 and SHARED(D9(21), ('Exod', 32, 20)) == ['עד', 'אשר', 'דק'] and SHN(D9(23), ('Deut', 1, 26)) == 5 and SHN(D9(23), ('Josh', 14, 7)) == 5 and SHN(D9(24), D9(7)) == 4
assert SHN(D9(26), ('1Kgs', 8, 51)) == 5 and SHN(D9(26), ('Exod', 32, 11)) == 5 and SHN(D9(27), ('Exod', 32, 13)) == 3 and SHARED(D9(27), ('Exod', 32, 13)) == ['לאברהם', 'ליצחק'] and SHN(D9(28), ('Num', 14, 16)) == 7 and SHN(D9(28), ('Exod', 32, 12)) == 2 and SHN(D9(29), ('1Kgs', 8, 51)) == 4
assert SHN(D9(1), ('Deut', 4, 38)) == 4 and SHN(D9(2), ('Deut', 1, 28)) == 5 and SHN(D9(3), ('Deut', 31, 3)) == 9 and SHN(D9(3), ('Deut', 4, 24)) == 6 and SHN(D9(5), ('Deut', 30, 20)) == 10 and SHN(D9(6), ('Exod', 33, 3)) == 7 and SHN(D9(7), ('Deut', 11, 5)) == 6
assert words('Exod', 32, 13)[:5] == ['זכר', 'לאברהם', 'ליצחק', 'ולישראל', 'עבדיך'] and W9(27)[:5] == ['זכר', 'לעבדיך', 'לאברהם', 'ליצחק', 'וליעקב']
assert words('Exod', 32, 15)[8] == 'בידו' and W9(15)[10:] == ['על', 'שתי', 'ידי'] and words('Exod', 32, 20)[11:15] == ['ויזר', 'על', 'פני', 'המים'] and W9(21)[21:23] == ['אל', 'הנחל']
# THE PHRASE CENSUSES (the crowns; typed from ch9_measure1's B print)
assert P('שמע', 'ישראל') == ['Deut 20:3', 'Deut 5:1', 'Deut 6:4', 'Deut 9:1'] and P('גוים', 'גדלים', 'ועצמים', 'ממך') == ['Deut 4:38', 'Deut 9:1'] and P('לבא', 'לרשת') == ['Deut 11:31', 'Deut 9:1', 'Judg 18:9']
assert P('ערים', 'גדלת', 'ובצרת', 'בשמים') == ['Deut 9:1'] and P('ערים', 'גדלת', 'ובצורת', 'בשמים') == ['Deut 1:28'] and P('עם', 'גדול', 'ורם') == ['Deut 1:28', 'Deut 9:2'] and len(U('ענקים', 'ענק', 'הענק', 'הענקים', 'ענקי', 'וענקים')) == 13 and P('מי', 'יתיצב', 'לפני') == ['Deut 9:2']
assert P('אש', 'אכלה') == ['Deut 4:24', 'Deut 9:3', 'Joel 1:19', 'Joel 2:5'] and P('העבר', 'לפניך') == ['Deut 9:3'] and P('עבר', 'לפניך') == ['Deut 31:3'] and [(s, x) for s, x, _ in LEMT('3665', books=('Deut',))] == [('Deut 9:3', 'יכניעם')]
assert [(s, x) for s, x, m in LEMT('4118 b', books=('Deut',))] == [('Deut 4:26', 'מהר'), ('Deut 7:4', 'מהר'), ('Deut 7:22', 'מהר'), ('Deut 9:3', 'מהר'), ('Deut 9:12', 'מהר'), ('Deut 9:12', 'מהר'), ('Deut 9:16', 'מהר'), ('Deut 28:20', 'מהר')]
assert P('אל', 'תאמר', 'בלבבך') == ['Deut 9:4'] and P('ואמרת', 'בלבבך') == ['Deut 8:17', 'Isa 49:21'] and U('בלבבך', books=('Deut',)) == ['Deut 18:21', 'Deut 7:17', 'Deut 8:17', 'Deut 8:2', 'Deut 9:4']
assert [(s, x) for s, x, _ in LEMT('6666', books=T)] == [('Deut 6:25', 'וצדקה'), ('Deut 9:4', 'בצדקתי'), ('Deut 9:5', 'בצדקתך'), ('Deut 9:6', 'בצדקתך'), ('Deut 24:13', 'צדקה'), ('Deut 33:21', 'צדקת'), ('Gen 15:6', 'צדקה'), ('Gen 18:19', 'צדקה'), ('Gen 30:33', 'צדקתי')]
assert [(s, x) for s, x, _ in LEMT('7564', books=T)] == [('Deut 9:4', 'וברשעת'), ('Deut 9:5', 'ברשעת'), ('Deut 25:2', 'רשעתו')] and P('ובישר', 'לבבך') == ['Deut 9:5'] and P('ישר', 'לבב') == [] and P('בישר', 'לבב') == ['Ps 119:7']
assert P('לאברהם', 'ליצחק', 'וליעקב') == ['Deut 1:8', 'Deut 29:12', 'Deut 30:20', 'Deut 34:4', 'Deut 6:10', 'Deut 9:27', 'Deut 9:5', 'Exod 33:1', 'Exod 6:8', 'Gen 50:24', 'Num 32:11'] and P('לאברהם', 'ליצחק', 'ולישראל') == ['Exod 32:13']
assert P('הארץ', 'הטובה') == ['1Chr 28:8', 'Deut 1:35', 'Deut 3:25', 'Deut 4:21', 'Deut 4:22', 'Deut 9:6', 'Josh 23:16']
assert P('קשה', 'ערף') == ['Deut 9:13', 'Deut 9:6', 'Exod 32:9', 'Exod 33:3', 'Exod 33:5', 'Exod 34:9'] and P('קשי', 'ערף') == [] and [(s, x) for s, x, _ in LEMT('7190')] == [('Deut 9:27', 'קשי')]   # STIFF-NECKED six seats in the Bible, ALL the calf's; "stubbornness" the Bible's one seat
assert [(s, x) for s, x, _ in LEMT('6203', books=T)] == [('Deut 9:6', 'ערף'), ('Deut 9:13', 'ערף'), ('Deut 10:16', 'וערפכם'), ('Deut 31:27', 'ערפך'), ('Exod 23:27', 'ערף'), ('Exod 32:9', 'ערף'), ('Exod 33:3', 'ערף'), ('Exod 33:5', 'ערף'), ('Exod 34:9', 'ערף'), ('Gen 49:8', 'בערף'), ('Lev 5:8', 'ערפו')]
assert P('זכר', 'אל', 'תשכח') == ['Deut 9:7'] and [(s, x) for s, x, m in LEMT('2142', books=('Deut',)) if m and 'v2ms' in m] == [('Deut 9:7', 'זכר'), ('Deut 9:27', 'זכר'), ('Deut 32:7', 'זכר')]
assert [(s, x) for s, x, m in LEMT('7107', books=T) if m and m.startswith('HVh')] == [('Deut 9:7', 'הקצפת'), ('Deut 9:8', 'הקצפתם'), ('Deut 9:22', 'מקצפים')] and len(LEMT('7107', books=T)) == 12   # the hiphil "provoke" — the Torah's three, all this chapter's
assert P('למן', 'היום', books=('Deut',)) == ['Deut 4:32', 'Deut 9:7'] and P('עד', 'המקום', 'הזה') == ['Deut 11:5', 'Deut 1:31', 'Deut 9:7'] and P('ממרים', 'הייתם') == ['Deut 9:24', 'Deut 9:7']
assert [(s, x) for s, x, m in LEMT('4784', books=T)] == [('Deut 1:26', 'ותמרו'), ('Deut 1:43', 'ותמרו'), ('Deut 9:7', 'ממרים'), ('Deut 9:23', 'ותמרו'), ('Deut 9:24', 'ממרים'), ('Deut 21:18', 'ומורה'), ('Deut 21:20', 'ומרה'), ('Deut 31:27', 'ממרים'), ('Num 20:10', 'המרים'), ('Num 20:24', 'מריתם'), ('Num 27:14', 'מריתם')]
assert [(s, x) for s, x, m in LEMT('599') if s.startswith('Deut')] == [('Deut 1:37', 'התאנף'), ('Deut 4:21', 'התאנף'), ('Deut 9:8', 'ויתאנף'), ('Deut 9:20', 'התאנף')] and len(LEMT('599')) == 14   # "was angry" the hithpael — the book's four (Moses' twice, this chapter's twice)
assert [s for s in U('להשמיד', 'להשמידך', 'להשמידו', 'להשמידם', 'ולהשמיד') if s.startswith('Deut')] == ['Deut 28:63', 'Deut 9:19', 'Deut 9:20', 'Deut 9:25', 'Deut 9:8'] and U('להשמידו') == ['Deut 9:20']
assert P('בעלתי', 'ההרה') == ['Deut 9:9'] and P('לוחת', 'הברית') + P('לחת', 'הברית') + P('לחות', 'הברית') == ['Deut 9:9', 'Deut 9:15', 'Deut 9:11'] and P('לוחת', 'האבנים') == ['Deut 9:10', 'Deut 9:9'] and P('לחות', 'האבנים') == ['1Kgs 8:9']   # "the tablets of the covenant" the Bible's three, all here
assert P('ארבעים', 'יום', 'וארבעים', 'לילה') == ['1Kgs 19:8', 'Deut 10:10', 'Deut 9:11', 'Deut 9:18', 'Deut 9:9', 'Exod 24:18', 'Exod 34:28', 'Gen 7:12', 'Gen 7:4'] and P('ארבעים', 'היום', 'ואת', 'ארבעים', 'הלילה') == ['Deut 9:25']   # the Bible's nine seats of the phrase, four in the chapter; the article's form once
assert P('לחם', 'לא', 'אכלתי', 'ומים', 'לא', 'שתיתי') == ['Deut 9:18', 'Deut 9:9'] and P('לחם', 'לא', 'אכל', 'ומים', 'לא', 'שתה') == ['Exod 34:28', 'Ezra 10:6'] and P('ואשב', 'בהר') == ['Deut 9:9', 'Isa 14:13'] and len(U('ארבעים', 'וארבעים', books=T)) == 48
assert P('מקץ', 'ארבעים', 'יום') == ['Deut 9:11', 'Gen 8:6', 'Num 13:25'] and U('מקץ', 'ומקץ', books=T) == ['Deut 15:1', 'Deut 31:10', 'Deut 9:11', 'Exod 12:41', 'Gen 16:3', 'Gen 41:1', 'Gen 4:3', 'Gen 8:6', 'Num 13:25']
assert P('כתבים', 'באצבע', 'אלהים') == ['Deut 9:10', 'Exod 31:18'] and P('אצבע', 'אלהים') + P('באצבע', 'אלהים') == ['Exod 8:15', 'Deut 9:10', 'Exod 31:18'] and P('ביום', 'הקהל') + P('יום', 'הקהל') == ['Deut 10:4', 'Deut 18:16', 'Deut 9:10'] and len(P('מתוך', 'האש')) == 11 and P('מתוך', 'האש', books=('Deut',)) == ['Deut 10:4', 'Deut 4:12', 'Deut 4:15', 'Deut 4:33', 'Deut 4:36', 'Deut 5:22', 'Deut 5:24', 'Deut 5:26', 'Deut 5:4', 'Deut 9:10']
assert [(s, x) for s, x, _ in LEMT('6951', books=('Deut',))] == [('Deut 5:22', 'קהלכם'), ('Deut 9:10', 'הקהל'), ('Deut 10:4', 'הקהל'), ('Deut 18:16', 'הקהל'), ('Deut 23:2', 'בקהל'), ('Deut 23:3', 'בקהל'), ('Deut 23:3', 'בקהל'), ('Deut 23:4', 'בקהל'), ('Deut 23:4', 'בקהל'), ('Deut 23:9', 'בקהל'), ('Deut 31:30', 'קהל')]
assert P('קום', 'רד', 'מהר') == ['Deut 9:12'] and P('לך', 'רד') == ['Exod 19:24', 'Exod 32:7'] and P('שחת', 'עמך') == ['Deut 9:12', 'Exod 32:7', 'Isa 14:20'] and P('מהר', 'מן', 'הדרך') == ['Deut 9:12', 'Deut 9:16', 'Exod 32:8', 'Judg 2:17']
assert P('עגל', 'מסכה') == ['Deut 9:16', 'Exod 32:4', 'Exod 32:8', 'Neh 9:18'] and U('העגל', 'עגל', 'לעגל', 'בעגל', books=T) == ['Deut 9:16', 'Deut 9:21', 'Exod 32:19', 'Exod 32:20', 'Exod 32:24', 'Exod 32:35', 'Exod 32:4', 'Exod 32:8', 'Lev 9:2', 'Lev 9:8'] and len(U('מסכה', 'ומסכה', 'מסכת', 'מסכות', 'למסכה')) == 23
assert P('ראיתי', 'את', 'העם', 'הזה') == ['Deut 9:13', 'Exod 32:9'] and P('הרף', 'ממני') == ['Deut 9:14'] and P('הניחה', 'לי') == ['Exod 32:10'] and P('ואשמידם', 'ואמחה') == ['Deut 9:14']
assert P('מתחת', 'השמים') == ['2Kgs 14:27', 'Deut 25:19', 'Deut 29:19', 'Deut 7:24', 'Deut 9:14', 'Exod 17:14', 'Gen 1:9', 'Gen 6:17'] and [(s, x) for s, x, _ in LEMT('4229 a', books=T)][:4] == [('Deut 9:14', 'ואמחה'), ('Deut 25:6', 'ימחה'), ('Deut 25:19', 'תמחה'), ('Deut 29:19', 'ומחה')]
assert P('ואעשה', 'אותך', 'לגוי') + P('ואעשך', 'לגוי') + P('אתך', 'לגוי') == ['Deut 9:14', 'Exod 32:10', 'Gen 12:2', 'Num 14:12'] and P('לגוי', 'עצום', 'ורב', 'ממנו') == ['Deut 9:14'] and P('לגוי', 'גדול', 'ועצום', 'ממנו') == ['Num 14:12'] and P('לגוי', 'גדול') == ['Deut 26:5', 'Exod 32:10', 'Gen 12:2', 'Gen 17:20', 'Gen 18:18', 'Gen 21:18', 'Gen 46:3', 'Num 14:12']
assert P('ואפן', 'וארד', 'מן', 'ההר') == ['Deut 10:5', 'Deut 9:15'] and P('ויפן', 'וירד', 'משה', 'מן', 'ההר') == ['Exod 32:15'] and P('בער', 'באש') == ['Deut 4:11', 'Deut 5:23', 'Deut 9:15', 'Exod 3:2'] and P('על', 'שתי', 'ידי') == ['Deut 9:15']
assert U('לעיניכם', books=('Deut',)) == ['Deut 1:30', 'Deut 29:1', 'Deut 9:17'] and P('וארא', 'והנה') == ['Dan 10:5', 'Deut 9:16', 'Ezek 1:4', 'Ezek 44:4', 'Zech 2:1', 'Zech 2:5', 'Zech 5:9'] and P('חטאתם', 'ליהוה') == ['Deut 9:16', 'Jer 40:3', 'Jer 44:23', 'Num 32:23']
assert [(s, x) for s, x, _ in LEMT('8610', books=T)][:1] == [('Deut 9:17', 'ואתפש')] and P('ואשלכם', 'מעל', 'שתי', 'ידי') == ['Deut 9:17'] and P('וישלך', 'מידו', 'את', 'הלחת') == ['Exod 32:19'] and [(s, x) for s, x, _ in LEMT('7665', books=T) if s.startswith('Deut')] == [('Deut 7:5', 'תשברו'), ('Deut 9:17', 'ואשברם'), ('Deut 10:2', 'שברת'), ('Deut 12:3', 'ושברתם')]
assert P('ואתנפל', 'לפני', 'יהוה') == ['Deut 9:18', 'Deut 9:25'] and [(s, x) for s, x, m in LEMT('5307') if m and 'Vt' in m] == [('Deut 9:18', 'ואתנפל'), ('Deut 9:25', 'ואתנפל'), ('Deut 9:25', 'התנפלתי'), ('Ezra 10:1', 'ומתנפל'), ('Gen 43:18', 'ולהתנפל')]
assert U('כראשנה', 'כראשונה', 'כבראשנה', 'בראשנה', books=T) == ['Deut 17:7', 'Deut 9:18', 'Gen 13:4', 'Num 10:13', 'Num 10:14'] and P('לעשות', 'הרע', 'בעיני', 'יהוה', books=T) == ['Deut 9:18'] and len(P('הרע', 'בעיני', 'יהוה')) == 53   # the Kings' formula — its ONE Torah seat
assert [(s, x) for s, x, _ in LEMT('3707', books=T)] == [('Deut 4:25', 'להכעיסו'), ('Deut 9:18', 'להכעיסו'), ('Deut 31:29', 'להכעיסו'), ('Deut 32:16', 'יכעיסהו'), ('Deut 32:21', 'כעסוני'), ('Deut 32:21', 'אכעיסם')]
assert P('יגרתי', 'מפני') == ['Deut 9:19'] and P('האף', 'והחמה') == ['Deut 9:19', 'Jer 36:7'] and [(s, x) for s, x, _ in LEMT('3025') if s.startswith('Deut')] == [('Deut 9:19', 'יגרתי'), ('Deut 28:60', 'יגרת')] and P('וישמע', 'יהוה', 'אלי') == ['Deut 10:10', 'Deut 9:19'] and P('גם', 'בפעם', 'ההוא') == ['Deut 10:10', 'Deut 9:19']
assert len(P('בעת', 'ההוא', books=('Deut',))) == 15 and 'Deut 9:20' in P('בעת', 'ההוא', books=('Deut',)) and [(s, x) for s, x, _ in LEMT('6471', books=('Deut',))] == [('Deut 1:11', 'פעמים'), ('Deut 9:19', 'בפעם'), ('Deut 10:10', 'בפעם'), ('Deut 16:16', 'פעמים')]
assert P('התאנף', 'יהוה') == ['Deut 1:37', 'Deut 9:20'] and U('ואתפלל', 'ואתפללה') == ['1Sam 7:5', 'Dan 9:4', 'Deut 9:20', 'Deut 9:26', 'Jer 32:16', 'Neh 2:4'] and [(s, x) for s, x, _ in LEMT('6419', books=T)] == [('Deut 9:20', 'ואתפלל'), ('Deut 9:26', 'ואתפלל'), ('Gen 20:7', 'ויתפלל'), ('Gen 20:17', 'ויתפלל'), ('Gen 48:11', 'פללתי'), ('Num 11:2', 'ויתפלל'), ('Num 21:7', 'התפלל'), ('Num 21:7', 'ויתפלל')]
assert P('אשר', 'עשיתם', 'את', 'העגל') == ['Deut 9:21'] and P('ואשרף', 'אתו', 'באש') == ['Deut 9:21'] and P('וישרף', 'באש') == ['Exod 32:20'] and P('עד', 'אשר', 'דק') == ['Deut 9:21', 'Exod 32:20'] and [(s, x) for s, x, _ in LEMT('3807', books=T)] == [('Deut 1:44', 'ויכתו'), ('Deut 9:21', 'ואכת'), ('Lev 22:24', 'וכתות'), ('Num 14:45', 'ויכתום')]
assert [(s, x, m) for s, x, m in LEMT('2912') if s.startswith('Deut')] == [('Deut 9:21', 'טחון', 'HVqa')] and [(s, x) for s, x, _ in LEMT('1854', books=T)] == [('Deut 9:21', 'דק'), ('Exod 30:36', 'הדק'), ('Exod 32:20', 'דק')] and P('הנחל', 'הירד', 'מן', 'ההר') == ['Deut 9:21'] and P('ויזר', 'על', 'פני', 'המים') == ['Exod 32:20'] and P('אל', 'נחל', 'קדרון') == ['2Kgs 23:12', '2Kgs 23:6']
assert U('תבערה', 'ובתבערה', 'בתבערה') == ['Deut 9:22', 'Num 11:3'] and U('מסה', 'ובמסה', 'במסה') == ['Deut 33:8', 'Deut 6:16', 'Deut 9:22', 'Exod 17:7', 'Ps 95:8'] and P('קברת', 'התאוה') + P('ובקברת', 'התאוה') + P('מקברת', 'התאוה') + P('בקברת', 'התאוה') == ['Deut 9:22', 'Num 33:17', 'Num 33:16'] and P('קברות', 'התאוה') == ['Num 11:34'] and P('מקברות', 'התאוה') == ['Num 11:35']   # the three names' seats; Kibroth defective here and at 33:16-17, plene at 11:34-35
assert P('קדש', 'ברנע') + P('מקדש', 'ברנע') + P('בקדש', 'ברנע') + P('וקדש', 'ברנע') == ['Deut 1:19', 'Deut 1:2', 'Deut 2:14', 'Deut 9:23', 'Josh 10:41', 'Josh 14:7', 'Num 32:8', 'Josh 14:6'] and P('עלו', 'ורשו') == ['Deut 9:23'] and P('עלה', 'רש') == ['Deut 1:21']
assert P('ותמרו', 'את', 'פי') == ['Deut 1:26', 'Deut 1:43', 'Deut 9:23'] and P('מריתם', 'פי') == ['Num 27:14'] and P('מריתם', 'את', 'פי') == ['Num 20:24'] and P('פי', 'יהוה', books=('Deut',)) == ['Deut 1:26', 'Deut 1:43', 'Deut 34:5', 'Deut 8:3', 'Deut 9:23'] and P('ולא', 'האמנתם', 'לו') == ['Deut 9:23'] and P('אינכם', 'מאמינם') == ['Deut 1:32'] and P('ולא', 'שמעתם', 'בקלו') == ['Deut 9:23']
assert P('מיום', 'דעתי', 'אתכם') == ['Deut 9:24'] and [(s, x) for s, x, _ in LEMT('3045') if x == 'דעתי'] == [('Deut 9:24', 'דעתי')] and P('כי', 'אמר', 'יהוה', 'להשמיד', 'אתכם') == ['Deut 9:25']
assert P('ואתפלל', 'אל', 'יהוה', 'ואמר') == ['Deut 9:26'] and P('אדני', 'יהוה', books=T) == ['Deut 3:24', 'Deut 9:26', 'Gen 15:2', 'Gen 15:8'] and P('אל', 'תשחת', 'עמך', 'ונחלתך') == ['Deut 9:26'] and P('עמך', 'ונחלתך') == ['1Kgs 8:51', 'Deut 9:26', 'Deut 9:29'] and P('עמו', 'ונחלתו') == ['Ps 94:14']
assert [(s, x) for s, x, _ in LEMT('6299', books=('Deut',))] == [('Deut 7:8', 'ויפדך'), ('Deut 9:26', 'פדית'), ('Deut 13:6', 'והפדך'), ('Deut 15:15', 'ויפדך'), ('Deut 21:8', 'פדית'), ('Deut 24:18', 'ויפדך')] and [(s, x) for s, x, _ in LEMT('1433') if s.startswith('Deut')] == [('Deut 3:24', 'גדלך'), ('Deut 5:24', 'גדלו'), ('Deut 9:26', 'בגדלך'), ('Deut 11:2', 'גדלו'), ('Deut 32:3', 'גדל')]
assert P('ביד', 'חזקה', books=('Deut',)) == ['Deut 26:8', 'Deut 5:15', 'Deut 6:21', 'Deut 7:8', 'Deut 9:26'] and P('ביד', 'חזקה', books=T) == ['Deut 26:8', 'Deut 5:15', 'Deut 6:21', 'Deut 7:8', 'Deut 9:26', 'Exod 13:9', 'Exod 3:19', 'Exod 6:1'] and P('בכח', 'גדול', 'וביד', 'חזקה') == ['Exod 32:11']
assert P('זכר', 'לעבדיך') == ['Deut 9:27'] and P('זכר', 'לאברהם') == ['Exod 32:13'] and P('אל', 'תפן', 'אל') == ['Deut 9:27', 'Job 36:21', 'Num 16:15'] and [(s, x) for s, x, m in LEMT('6437', books=T) if m and 'j' in m[3:6]] == [('Deut 9:27', 'תפן'), ('Lev 19:4', 'תפנו'), ('Lev 19:31', 'תפנו'), ('Num 16:15', 'תפן')] and [(s, x) for s, x, _ in LEMT('7562', books=T)] == [('Deut 9:27', 'רשעו')]
assert P('פן', 'יאמרו', 'הארץ') == ['Deut 9:28'] and P('למה', 'יאמרו', 'מצרים') == ['Exod 32:12'] and P('ואמרו', 'הגוים') == ['Num 14:15'] and P('פן', 'יאמרו') == ['Deut 32:27', 'Deut 9:28', 'Judg 9:54'] and U('הוצאתנו') == ['Deut 9:28']
assert P('יכלת', 'יהוה') == ['Deut 9:28', 'Num 14:16'] and W9(28)[6] == 'מבלי' and words('Num', 14, 16)[0] == 'מבלתי' and U('מבלי', 'מבלתי', 'ומבלי', books=T) == ['Deut 28:55', 'Deut 9:28', 'Num 14:16'] and [(s, x) for s, x, _ in LEMT('8135', books=T)] == [('Deut 1:27', 'בשנאת'), ('Deut 9:28', 'ומשנאתו'), ('Num 35:20', 'בשנאה')]
assert P('הוציאם', 'להמתם', 'במדבר') == ['Deut 9:28'] and P('ברעה', 'הוציאם', 'להרג') == ['Exod 32:12'] and P('וישחטם', 'במדבר') == ['Num 14:16'] and U('להשמידנו') == ['Deut 1:27']   # FOUR forms of the nations' taunt: the mountains (Exodus), the wilderness (Numbers, here), the Amorite's hand (1:27)
assert P('והם', 'עמך', 'ונחלתך') == ['Deut 9:29'] and P('בכחך', 'הגדל', 'ובזרעך', 'הנטויה') == ['Deut 9:29'] and P('בכח', 'גדול') == ['2Kgs 17:36', 'Exod 32:11'] and P('בכחו', 'הגדל') == ['Deut 4:37'] and P('בכחך', 'הגדל') == ['Deut 9:29'] and P('בכחך', 'הגדול') == ['Jer 32:17', 'Neh 1:10'] and [(s, x) for s, x, _ in LEMT('2220', books=('Deut',))][:4] == [('Deut 4:34', 'ובזרוע'), ('Deut 5:15', 'ובזרע'), ('Deut 7:19', 'והזרע'), ('Deut 9:29', 'ובזרעך')]
assert len(P('זרוע', 'נטויה') + P('ובזרע', 'נטויה') + P('ובזרעך', 'הנטויה') + P('ובזרוע', 'נטויה') + P('בזרוע', 'נטויה') + P('בזרע', 'נטויה') + P('זרעך', 'הנטויה')) == 10 and sorted(s for s in P('ובזרע', 'נטויה') + P('ובזרעך', 'הנטויה') + P('ובזרוע', 'נטויה') if s.startswith('Deut')) == ['Deut 26:8', 'Deut 4:34', 'Deut 5:15', 'Deut 9:29']
# ONKELOS OVER THE BOOK (computed on the plain Aramaic of every export row; EXPORT seats — chapter 9's = the DB's)
assert onk_tok('מימריה') == [(3, 22), (4, 24), (4, 36), (5, 21), (9, 3), (11, 1), (20, 1), (23, 15), (31, 3), (31, 8)] and onk_seats('מימריה אשא אכלא') == [(4, 24), (9, 3)] and 'הוא' in aramaic(9, 3) and 'מימריה' in aramaic(9, 3)   # THE MEMRA a consuming fire — 4:24 and 9:3 the two seats
assert onk_seats('גזרת מימרא דיי') == [(1, 43), (9, 23)] and onk_tok('למימריה') == [(4, 30), (9, 23), (30, 2), (30, 20)] and len(onk_seats('מימרא דיי')) == 24
assert onk_tok('בזכותי') == [(9, 4)] and onk_tok('בזכותך') == [(9, 5), (9, 6)] and onk_seats('זכות') == [(6, 25), (9, 4), (9, 5), (9, 6), (24, 13)] and onk_tok('ובחובי') == [(9, 4)]   # "merit" for "righteousness" — the book's five merit seats, three this chapter's
assert onk_seats('צית שמיא') == [(1, 28), (4, 11), (9, 1)] and onk_seats('בני גבריא') == [(9, 2)] and onk_tok('גבריא') == [(2, 20), (2, 34), (3, 6), (3, 11), (3, 13), (9, 2), (25, 1), (31, 12)] and onk_tok('בדיתבר') == [(9, 4)]
assert onk_seats('קשי קדל') == [(9, 6), (9, 13)] and onk_seats('רגז מן קדם יי') == [(1, 37), (3, 26), (9, 8), (9, 20)] and onk_seats('ארגזתא קדם יי') == [(9, 7)] and onk_seats('ארגזתון קדם יי') == [(9, 8)] and onk_seats('מרגזין הויתון קדם יי') == [(9, 22)]   # the reverence — the anger "from before", the provoking "before"
assert onk_seats('מסרבין הויתון קדם יי') == [(9, 7), (9, 24), (31, 27)] and onk_seats('וסרבתון על גזרת מימרא דיי') == [(1, 43), (9, 23)] and onk_seats('ולא קבלתון למימריה') == [(9, 23)] and onk_seats('ולא הימנתון ליה') == [(9, 23)]
assert onk_seats('גלי קדמי') == [(9, 13), (31, 21), (32, 20)] and onk_seats('אנח בעותך מקדמי') == [(9, 14)] and onk_seats('קביל יי צלותי') == [(9, 19), (10, 10)] and onk_tok('צלותי') == [(9, 19), (10, 10)] and onk_seats('וצליתי קדם יי') == [(3, 23), (9, 26)]   # revealed before Me; leave your prayer; accepted my prayer
assert onk_seats('ואוקדית יתיה בנורא') == [(9, 21)] and onk_tok('בנורא') == [(7, 5), (7, 25), (9, 21), (12, 3), (12, 31), (13, 17), (18, 10)] and onk_seats('בער באשתא') == [(4, 11), (5, 20), (9, 15)] and len(onk_tok('אשתא')) == 14 and onk_seats('ושפית יתיה בשופינא') == [(9, 21)]   # TWO ARAMAIC WORDS FOR FIRE — the burnings' fire and the mountain's; the file supplied
assert onk_seats('ובדלקתא ובנסתא ובקברי דמשאלי') == [(9, 22)] and onk_tok('ובדלקתא') == [(9, 22), (28, 22)] and onk_seats('נסתא') + onk_seats('נסיתא') == [(9, 22), (33, 8), (6, 16)] and onk_seats('קברי דמשאלי') == [(9, 22)]   # the three names TRANSLATED
assert onk_seats('רקם גיאה') == [(1, 2), (1, 19), (2, 14), (9, 23)] and onk_tok('מרקם') == [(2, 14), (9, 23)] and onk_seats('יי אלהים') == [(3, 24), (9, 26)] and onk_tok('דירי') == [(9, 28)] and onk_seats('דירי ארעא') == [(9, 28)]
assert onk_tok('מרממא') == [(7, 19), (9, 29), (11, 2), (26, 8)] and onk_seats('בחילך רבא ובדרעך מרממא') == [(9, 29)] and onk_tok('בתקפך') == [(9, 26)] and onk_seats('בידא תקיפא') == [(4, 34), (5, 15), (6, 21), (7, 8), (9, 26), (26, 8)]
assert onk_seats('לוחי קימא') == [(9, 9), (9, 11), (9, 15)] and onk_seats('לוחי אבניא') == [(4, 13), (5, 19), (9, 9), (9, 10), (9, 11), (10, 1), (10, 3)] and onk_seats('תרין לוחי') == [(4, 13), (5, 19), (9, 10), (9, 11), (9, 15), (9, 17), (10, 1), (10, 3)] and onk_seats('תרתין ידי') == [(9, 15), (9, 17)]
assert onk_seats('ארבעין יממין וארבעין לילון') == [(9, 9), (9, 11), (9, 18), (10, 10)] and onk_seats('לחמא לא אכלית ומיא לא אשתיתי') == [(9, 9), (9, 18)] and onk_seats('ביומא דקהלא') == [(9, 10), (10, 4), (18, 16)] and onk_seats('כתיבין באצבעא') == [(9, 10)]
assert onk_seats('סטו בפריע מן ארחא') == [(9, 12)] and onk_seats('סטתון בפריע מן ארחא') == [(9, 16)] and onk_tok('בפריע') == [(4, 26), (7, 4), (7, 22), (9, 3), (9, 12), (9, 16), (11, 17), (28, 20)] and onk_seats('עגל מתכא') == [(9, 16)] and onk_seats('עבדו להון מתכא') == [(9, 12)]
assert onk_seats('ואמחי ית שמהון מתחות שמיא') == [(9, 14)] and onk_seats('לעם תקיף וסגי מנהון') == [(9, 14)] and onk_seats('עממין רברבין ותקיפין') == [(4, 38), (9, 1), (11, 23)] and onk_seats('עם רב ותקיף') == [(9, 2)] and onk_seats('לאקמא ית פתגמא די קיים יי לאבהתך') == [(9, 5)]
assert [(v + 1) for v in range(29) if '(' in clean(onk_he[8][v])] == [] and onk_seats('מדלית יוכלא דיי') == [(9, 28)] and onk_seats('לקטלותהון במדברא') == [(9, 28)] and onk_seats('ומדסני יתהון') == [(9, 28)]
BR = {e: re.findall(r'\[([^\]]+)\]', clean(onk[8][e - 1])) for e in range(1, 30) if re.findall(r'\[([^\]]+)\]', clean(onk[8][e - 1]))}
assert BR == {1: ['height of the'], 2: ['giants'], 3: ['His word is'], 4: ['merit', 'sins'], 5: ['merit', 'sins'], 8: ['from before'], 13: ['have been revealed berore Me'], 18: ['before', 'before'], 20: ['from before', 'He'], 21: ['-object'], 22: ['before'], 23: ['Rekam Geyah', 'the decree of the word of', 'accept His word'], 28: ['the inhabitants', 'of', 'up']} and sum(len(v) for v in BR.values()) == 21   # the English's supplied words: twenty-one brackets in thirteen verses ("berore" the export's own typo)
# THE STORE'S GLOSSES (the display layer read back; every family censused over the whole store — ch9_measure1 section G)
assert sg(9, 9, 'לוחת') == 'meaning-to-glisten' and sg(9, 17, 'הלחת') == 'the-meaning-to-glisten' and sg(9, 7, 'הקצפת') == 'crack-off' and sg(9, 22, 'מקצפים') == 'crack-off' and sg(9, 18, 'חטאתכם') == 'sin-offering-you/your (pl)' and sg(9, 27, 'חטאתו') == 'sin-offering-him/its' and sg(9, 7, 'זכר') == 'mark' and sg(9, 7, 'תשכח') == 'mislay'
assert sg(9, 7, 'ממרים') == 'be--bitter' and sg(9, 23, 'ותמרו') == 'and-be--bitter' and sg(9, 23, 'האמנתם') == 'build-up' and sg(9, 20, 'ואתפלל') == 'and-judge' and sg(9, 17, 'ואתפש') == 'and-manipulate' and sg(9, 26, 'פדית') == 'sever' and sg(9, 14, 'ואמחה') == 'and-stroke' and sg(9, 14, 'הרף') == 'slacken'
assert sg(9, 10, 'באצבע') == 'in-something-to-sieze-with' and sg(9, 10, 'כתבים') == 'grave' and sg(9, 22, 'ובקברת') == 'and-in-?' and sg(9, 23, 'מקדש') == 'from-?' and sg(9, 22, 'התאוה') == 'Kibroth-hattaavah' and sg(9, 12, 'מסכה') == 'pouring-over' and sg(9, 12, 'שחת') == 'decay' and sg(9, 26, 'תשחת') == 'decay'
assert sg(9, 3, 'והאבדתם') == 'and-wander-away-them/their' and sg(9, 19, 'האף') == 'the-nose' and sg(9, 19, 'בפעם') == 'in-stroke' and sg(9, 21, 'ואשרף') == 'and-be--on-fire' and sg(9, 21, 'ואכת') == 'and-bruise' and sg(9, 21, 'דק') == 'crush--crumble' and sg(9, 21, 'טחון') == 'grind-meal' and sg(9, 21, 'היטב') == 'be--make-well'
assert sg(9, 8, 'ויתאנף') == 'and-breathe-hard' and sg(9, 20, 'התאנף') == 'breathe-hard' and sg(9, 2, 'ורם') == 'and-be-high-actively' and sg(9, 2, 'יתיצב') == 'place' and sg(9, 3, 'יכניעם') == 'bend-the-knee-them/their' and sg(9, 4, 'בהדף') == 'in-push-away' and sg(9, 5, 'הקים') == 'arise' and sg(9, 6, 'ערף') == 'nape' and sg(9, 6, 'קשה') == 'severe'
assert sg(9, 11, 'מקץ') == 'from-extremity' and sg(9, 10, 'הקהל') == 'the-assemblage' and sg(9, 20, 'בעד') == 'in-up-to' and sg(9, 27, 'קשי') == 'obstinacy' and sg(9, 28, 'מבלי') == 'from-failure' and sg(9, 28, 'להמתם') == 'to-die-them/their' and sg(9, 29, 'בכחך') == 'in-vigor-you/your' and sg(9, 26, 'בגדלך') == 'in-magnitude-you/your'
assert sg(9, 26, 'אדני') == 'Lord-me/my' and sg(9, 9, 'שתיתי') == 'imbibe' and sg(9, 9, 'לחם') == 'food' and sg(9, 9, 'ואשב') == 'and-dwell/sit' and sg(9, 18, 'ואתנפל') == 'and-fall' and sg(9, 25, 'התנפלתי') == 'fall' and sg(9, 18, 'כראשנה') == 'like-first' and sg(9, 21, 'ואשלך') == 'and-throw-out' and sg(9, 17, 'ואשלכם') == 'and-throw-out-them/their'
assert sg(9, 17, 'ואשברם') == 'and-burst-them/their' and sg(9, 21, 'הירד') == 'the-go-down' and sg(9, 21, 'הנחל') == 'the-stream' and sg(9, 4, 'הביאני') == 'come/bring-me/my' and sg(9, 4, 'בצדקתי') == 'in-rightness-me/my' and sg(9, 5, 'בצדקתך') == 'in-rightness-you/your' and sg(9, 5, 'ובישר') == 'and-in-right' and sg(9, 5, 'ברשעת') == 'in-wrong' and sg(9, 27, 'רשעו') == 'wrong-him/its'
assert sg(9, 4, 'מורישם') == 'possess/inherit-them/their' and sg(9, 3, 'והורשתם') == 'and-possess/inherit-them/their' and sg(9, 3, 'העבר') == 'the-pass-over' and sg(9, 8, 'להשמיד') == 'to-desolate' and sg(9, 20, 'להשמידו') == 'to-desolate-him/its' and sg(9, 9, 'בעלתי') == 'in-go-up-me/my' and sg(9, 12, 'צויתם') == 'command-them/their' and sg(9, 14, 'שמם') == 'name-them/their'
assert sg(9, 14, 'ורב') == 'and-many/great' and sg(9, 15, 'ואפן') == 'and-turn' and sg(9, 15, 'וארד') == 'and-go-down' and sg(9, 19, 'והחמה') == 'and-the-heat' and sg(9, 23, 'ובשלח') == 'and-in-send' and sg(9, 24, 'דעתי') == 'know-me/my' and sg(9, 28, 'להביאם') == 'to-come/bring-them/their' and sg(9, 28, 'ומשנאתו') == 'and-from-hate-him/its'
assert sg(9, 28, 'הוציאם') == 'bring-forth-them/their' and sg(9, 17, 'לעיניכם') == 'to-eye-you/your (pl)' and sg(9, 29, 'ובזרעך') == 'and-in-arm-you/your' and sg(9, 21, 'עפרו') == 'dust-him/its' and sg(9, 26, 'ונחלתך') == 'and-inheritance-you/your' and sg(9, 27, 'לעבדיך') == 'to-servant-you/your' and sg(9, 28, 'יכלת') == 'be-able' and sg(9, 17, 'בשני') == 'in-two' and sg(9, 15, 'ידי') == 'hand-me/my' and sg(9, 23, 'בקלו') == 'in-voice/sound-him/its' and sg(9, 2, 'ענקים') == 'Anakite' and sg(9, 23, 'ברנע') == 'Kadeshbarnea'
GLOSS_FAMILY = {'the-meaning-to-glisten': [('הלחת', 11)], 'crack-off': [('קצף', 2), ('הקצפת', 1), ('הקצפתם', 1), ('יקצף', 1), ('מקצפים', 1), ('תקצף', 1)], 'in-something-to-sieze-with': [('באצבע', 2)], 'and-in-?': [('ובקברת', 1)], 'pouring-over': [('מסכה', 6)], 'the-nose': [('האף', 2)], 'crush--crumble': [('דק', 2), ('הדק', 1)], 'grind-meal': [('טחון', 1)], 'and-breathe-hard': [('ויתאנף', 1)], 'bend-the-knee-them/their': [('יכניעם', 1)], 'in-push-away': [('בהדף', 1)], 'nape': [('ערף', 7)], 'the-assemblage': [('הקהל', 17)], 'to-die-them/their': [('להמתם', 1)], 'in-vigor-you/your': [('בכחך', 2)], 'in-magnitude-you/your': [('בגדלך', 1)], 'imbibe': [('ישתה', 6), ('שתה', 5), ('נשתה', 4), ('תשתה', 3), ('שתיתי', 2), ('ישתו', 1), ('שתיתם', 1), ('תשת', 1)], 'and-burst-them/their': [('ואשברם', 1)], 'the-go-down': [('הירד', 1)], 'in-rightness-me/my': [('בצדקתי', 1)], 'in-rightness-you/your': [('בצדקתך', 2)], 'and-in-right': [('ובישר', 1)], 'in-wrong': [('ברשעת', 1)], 'wrong-him/its': [('רשעו', 1), ('רשעתו', 1)], 'to-desolate': [('להשמיד', 3)], 'to-desolate-him/its': [('להשמידו', 1)], 'in-go-up-me/my': [('בעלתי', 1)], 'and-the-heat': [('והחמה', 1)], 'and-in-send': [('ובשלח', 1)], 'to-come/bring-them/their': [('להביאם', 1)], 'and-from-hate-him/its': [('ומשנאתו', 1)], 'to-eye-you/your (pl)': [('לעיניכם', 3)], 'and-in-arm-you/your': [('ובזרעך', 1)], 'dust-him/its': [('עפרו', 1)], 'and-inheritance-you/your': [('ונחלתך', 3)], 'obstinacy': [('קשי', 1)], 'and-the-mountain': [('וההר', 3)], 'the-stretch': [('הנטויה', 3)],
                'mark': [('זכר', 6), ('זכור', 4), ('תזכר', 3), ('אזכר', 2), ('אזכיר', 1), ('זכרנו', 1), ('מזכיר', 1), ('מזכרת', 1), ('תזכירו', 1), ('תזכרו', 1)], 'sin-offering-you/your (pl)': [('חטאתיכם', 4), ('חטאתכם', 4)], 'sin-offering-him/its': [('חטאתו', 10)], 'be--bitter': [('ממרים', 3), ('מריתם', 2), ('תמר', 1)], 'and-be--bitter': [('ותמרו', 3), ('וימררו', 1), ('ומורה', 1), ('ומרה', 1)], 'build-up': [('יאמינו', 6), ('האמנתם', 2), ('האמין', 1), ('מאמינם', 1), ('נאמן', 1), ('תאמין', 1)], 'and-judge': [('ויתפלל', 4), ('ושפטו', 4), ('ואתפלל', 2), ('וישפט', 2), ('ושפט', 1), ('ושפטתי', 1), ('ושפטתם', 1)], 'and-manipulate': [('ואתפש', 1), ('ותפשו', 1)], 'sever': [('תפדה', 10), ('פדית', 2), ('אפדה', 1), ('יפדה', 1), ('נפדתה', 1), ('פדה', 1)], 'and-stroke': [('ומחה', 3), ('ואמחה', 1), ('וימח', 1), ('וימחו', 1), ('ומחיתי', 1)], 'slacken': [('נרפים', 3), ('הרף', 1)], 'grave': [('כתבים', 4), ('כתב', 2), ('תכתב', 2), ('כתבו', 1), ('כתבת', 1), ('כתבתי', 1), ('כתוב', 1)], 'decay': [('שחת', 4), ('אשחית', 3), ('תשחית', 3), ('תשחת', 2), ('השחית', 1), ('השחת', 1), ('משחית', 1), ('משחתים', 1), ('נשחתה', 1)], 'and-wander-away-them/their': [('והאבדתם', 1), ('ויאבדם', 1)], 'in-stroke': [('בפעם', 5)], 'and-be--on-fire': [('ושרף', 4), ('ושרפת', 2), ('ואשרף', 1), ('וישרף', 1), ('ונשרפה', 1), ('ושרפו', 1), ('ותשרף', 1)], 'and-bruise': [('ואכת', 1), ('ויכתו', 1), ('וכתות', 1)], 'and-be-high-actively': [('וירם', 5), ('ורם', 5), ('והרים', 3), ('והרמת', 1), ('והרמתם', 1), ('ותרם', 1)], 'severe': [('קשה', 9), ('קשות', 2)], 'from-extremity': [('מקץ', 9), ('מקצה', 8)], 'in-up-to': [('בעד', 5)], 'from-failure': [('מבלי', 2)], 'Lord-me/my': [('אדני', 15)], 'like-first': [('כראשנים', 4), ('כראשון', 1), ('כראשנה', 1)], 'and-throw-out-them/their': [('ואשלכהו', 1), ('ואשלכם', 1), ('וישלכם', 1)], 'come/bring-me/my': [('באי', 1), ('הביאני', 1)], 'possess/inherit-them/their': [('מורישם', 2), ('יירשום', 1), ('תורישמו', 1)], 'and-possess/inherit-them/their': [('ויירשם', 2), ('וירשתם', 2), ('והורשתם', 1)], 'the-pass-over': [('העבר', 4)], 'command-them/their': [('צויתם', 3), ('צום', 1), ('תצום', 1)], 'name-them/their': [('שמם', 4), ('שמתם', 4), ('שמותם', 2)], 'know-me/my': [('דעתי', 1), ('הודעני', 1), ('הודעתני', 1)], 'bring-forth-them/their': [('הוציאם', 3), ('יוציאם', 1), ('מוציאם', 1)], 'to-servant-you/your': [('לעבדיך', 6), ('לעבדך', 4)], 'in-two': [('בשני', 1), ('בשנים', 1), ('בשתי', 1)], 'hand-me/my': [('ידי', 15)]}
GT = {g: store.execute("SELECT REPLACE(w.he_plain,'/',''), COUNT(*) FROM words w WHERE w.gloss=? GROUP BY 1 ORDER BY 2 DESC, 1", (g,)).fetchall() for g in GLOSS_FAMILY}
assert all(sorted(GT[g]) == sorted(v) for g, v in GLOSS_FAMILY.items()), [g for g, v in GLOSS_FAMILY.items() if sorted(GT[g]) != sorted(v)]
# BY GLOSS — every token of the gloss the one word (or one family read the same at every seat): the rewrite covers the whole store (THIRTY-EIGHT)
OVERRIDE_GLOSS = [('the-meaning-to-glisten', 'the-tablets'), ('crack-off', 'provoke'), ('in-something-to-sieze-with', 'with-the-finger'), ('and-in-?', 'and-in-Kibroth'), ('pouring-over', 'molten-image'), ('the-nose', 'the-anger'), ('crush--crumble', 'fine'), ('grind-meal', 'grinding'), ('and-breathe-hard', 'and-was-angry'), ('bend-the-knee-them/their', 'subdue-them'), ('in-push-away', 'when-thrusting-out'), ('nape', 'neck'), ('the-assemblage', 'the-assembly'), ('to-die-them/their', 'to-kill-them'), ('in-vigor-you/your', 'with-your-power'), ('in-magnitude-you/your', 'with-your-greatness'), ('imbibe', 'drink'), ('and-burst-them/their', 'and-broke-them'), ('the-go-down', 'that-descends'), ('in-rightness-me/my', 'for-my-righteousness'), ('in-rightness-you/your', 'for-your-righteousness'), ('and-in-right', 'and-for-the-uprightness-of'), ('in-wrong', 'for-the-wickedness-of'), ('wrong-him/its', 'its-wickedness'), ('to-desolate', 'to-destroy'), ('to-desolate-him/its', 'to-destroy-him'), ('in-go-up-me/my', 'when-I-went-up'), ('and-the-heat', 'and-the-wrath'), ('and-in-send', 'and-when-sent'), ('to-come/bring-them/their', 'to-bring-them'), ('and-from-hate-him/its', 'and-because-of-his-hatred-of'), ('to-eye-you/your (pl)', 'before-your-eyes'), ('and-in-arm-you/your', 'and-with-your-arm'), ('dust-him/its', 'its-dust'), ('and-inheritance-you/your', 'and-your-inheritance'), ('obstinacy', 'stubbornness'), ('and-the-mountain', 'and-the-mountain'), ('the-stretch', 'the-outstretched')]
OVERRIDE_GLOSS = [(k, v) for k, v in OVERRIDE_GLOSS if k not in ('and-the-mountain', 'the-stretch')]   # two typed to the print and struck: 'and-the-mountain' is right already; 'the-stretch' is ALREADY overridden (below)
# BY REFERENCE — the family mixed (a homograph, two persons, a participle beside a finite verb): the seat named (FORTY)
OVERRIDE_REF_SPEC = [(7, 'זכר', 'remember', 0), (27, 'זכר', 'remember', 0), (18, 'חטאתכם', 'your-sin', 0), (21, 'חטאתכם', 'your-sin', 0), (27, 'חטאתו', 'its-sin', 0), (7, 'ממרים', 'rebellious', 0), (24, 'ממרים', 'rebellious', 0), (23, 'ותמרו', 'and-you-rebelled-against', 0), (23, 'האמנתם', 'you-believed', 0), (20, 'ואתפלל', 'and-I-prayed', 0), (26, 'ואתפלל', 'and-I-prayed', 0), (17, 'ואתפש', 'and-I-took-hold-of', 0), (26, 'פדית', 'you-redeemed', 0), (14, 'ואמחה', 'and-blot-out', 0), (14, 'הרף', 'let-alone', 0), (10, 'כתבים', 'written', 0), (12, 'שחת', 'has-corrupted', 0), (26, 'תשחת', 'destroy', 0), (3, 'והאבדתם', 'and-destroy-them', 0), (19, 'בפעם', 'at-the-time', 0), (21, 'ואשרף', 'and-I-burned', 0), (21, 'ואכת', 'and-I-crushed', 0), (2, 'ורם', 'and-tall', 0), (2, 'יתיצב', 'stand', 0), (6, 'קשה', 'stiff', 0), (13, 'קשה', 'stiff', 0), (11, 'מקץ', 'at-the-end-of', 0), (20, 'בעד', 'for', 0), (28, 'מבלי', 'for-lack-of', 0), (26, 'אדני', 'Lord', 0), (18, 'כראשנה', 'as-at-the-first', 0), (17, 'ואשלכם', 'and-I-threw-them', 0), (4, 'הביאני', 'has-brought-me', 0), (4, 'מורישם', 'dispossessing-them', 0), (5, 'מורישם', 'dispossessing-them', 0), (3, 'והורשתם', 'and-you-shall-dispossess-them', 0), (3, 'העבר', 'who-passes-over', 0), (12, 'צויתם', 'I-commanded-them', 0), (14, 'שמם', 'their-name', 0), (24, 'דעתי', 'I-knew', 0), (28, 'הוציאם', 'he-brought-them-out', 0), (27, 'לעבדיך', 'to-your-servants', 0), (17, 'בשני', 'the-two', 0), (15, 'ידי', 'my-hands', 0), (17, 'ידי', 'my-hands', 0), (23, 'מקדש', 'from-Kadesh', 0), (22, 'התאוה', 'hattaavah', 0), (21, 'היטב', 'thoroughly', 0), (9, 'לחם', 'bread', 0), (18, 'לחם', 'bread', 0), (9, 'ואשב', 'and-I-stayed', 0), (18, 'ואתנפל', 'and-I-fell-down', 0), (25, 'ואתנפל', 'and-I-fell-down', 0), (25, 'התנפלתי', 'I-fell-down', 0), (21, 'ואשלך', 'and-I-threw', 0), (21, 'הנחל', 'the-brook', 0), (14, 'ורב', 'and-more-numerous', 0), (15, 'ואפן', 'and-I-turned', 0), (15, 'וארד', 'and-I-came-down', 0), (5, 'הקים', 'to-establish', 0)]
OVERRIDE_REF3 = [(f'Deut.9.{v}:{sidx(9, v, tok, nth)}', new, tok) for v, tok, new, nth in OVERRIDE_REF_SPEC]
OVERRIDE_REF = [(k, v) for k, v, _ in OVERRIDE_REF3]
assert len(OVERRIDE_REF) == 60 and len({k for k, _ in OVERRIDE_REF}) == 60 and len(OVERRIDE_GLOSS) == 36 and len({k for k, _ in OVERRIDE_GLOSS}) == 36, (len(OVERRIDE_REF), len(OVERRIDE_GLOSS))
assert all(g in GLOSS_FAMILY for g, _ in OVERRIDE_GLOSS) and all(sg(9, v, tok, nth) is not None for v, tok, _, nth in OVERRIDE_REF_SPEC)
ALREADY = {'Anakite': 'Anakim', 'Kadeshbarnea': 'barnea', 'and-desolate-them/their': 'and-destroyed-them', 'and-gather-grapes': 'and-fortified', 'and-powerful': 'and-mighty', 'be--make-well': 'do-well', 'breathe-hard': 'was-angry', 'burst': 'break', 'desolate-them/their': 'destroyed-them', 'from-?': 'from', 'from-over': 'from-upon', 'from-under': 'beneath', 'hurrying': 'quickly', 'in-pasture': 'in-the-wilderness', 'in-time': 'at-the-time', 'kindle': 'burn', 'meaning-to-glisten': 'tablets', 'mislay': 'forget', 'the-he/it': 'that', 'the-mountain-suffix': 'to-the-mountain', 'the-stretch': 'the-outstretched', 'throw-out': 'threw', 'to-possess/inherit-her/its': 'to-possess-it', 'to-trouble-him/its': 'to-provoke-him', 'wander-away': 'perish'}   # twenty-five of the chapter's glosses ALREADY rewritten by the earlier sittings (typed from the print)
OV = open(f'{ROOT}/logic/glosses/word_gloss_overrides.yaml', encoding='utf-8').read()
PATCHED = 'THE DEUTERONOMY WALK sitting 7 (2026-09-19, Deuteronomy 9)' in OV
assert all(f'"{k}": "{v}"' in OV for k, v in ALREADY.items()) and all(f'"{k}": ' not in OV for k, _ in OVERRIDE_GLOSS if not PATCHED) and (PATCHED or '"Deut.9.' not in OV), [k for k, _ in OVERRIDE_GLOSS if f'"{k}": ' in OV]
if PATCHED: assert all(f'"{k}": "{v}"' in OV for k, v in OVERRIDE_REF) and all(f'"{k}": "{v}"' in OV for k, v in OVERRIDE_GLOSS), [k for k, v in OVERRIDE_REF + OVERRIDE_GLOSS if f'"{k}": "{v}"' not in OV][:6]
assert OV.count('  "Deut.8.20:3": "makes-perish"') == 1 and OV.count('  "hear-suffix": "hear"\n') == 1 and 'THE DEUTERONOMY WALK sitting 6 (2026-09-18, Deuteronomy 8)' in OV

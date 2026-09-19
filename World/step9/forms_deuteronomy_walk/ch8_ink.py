#!/usr/bin/env python3
# THE DEUTERONOMY WALK, sitting 6 — CHAPTER 8, Deuteronomy 8:1-20 (2026-09-18; the owner: "Go"; ONE RUN under THE TWO-RUN RULE — the rereads, the
# measurements, the ink, the design, the rows, the ledger, the seat, the gates, the records): THE INK of the chapter, computed from the Tanakh DB, the
# snapshot store and the shelf's own bytes — never typed. Sitting 5's form (ch7_ink.py): the scaffold by hand, the constants and every assert chapter 8's
# own, typed FROM THE PRINTS (ch8_dump0.out, ch8_measure1.out). THE TWO DIVISIONS AGREE (20 = 20; the alignment the identity, cost 25). THE SPINE IS SILENT
# ON THE CHAPTER (36 on 6:9, 37 on 11:10 — chapters 7 to 10 have none); SIXTEEN rows elsewhere cite it by the union of both files — the chapter's
# phrases quoted from the Land's praise (8:7-10 at 19:2, 32:12, 32:15, 37:5, 39:4, 39:6, 39:8, 40:10), the discipline (8:5 at 32:10, 32:12, 32:15), the
# satiety and the rebellion (8:12-14 at 43:7, 318:1), "not by bread alone" (8:3 at 48:10), "if you surely forget" (8:19 at 48:8), the end (8:16 at 53:1),
# the seven species (8:8 at 297:4), the wilderness (8:15 at 313:15). The parser MEASURED on every verse — TWO number verses, 8:2 and 8:4 "forty years"
# [40]; the seven-stem homograph "and you shall be satisfied" (8:10, 8:12) STARRED, "swore" (8:1, 8:18) no number; NO GAP. THE STORE = THE DB at every
# verse but 8:2, where the store carries the written AND the read form of "His commandments" — the chapter's one written/read pair (7:9's and 5:10's kin).
# The hand's facts as asserts, run all at once by assert_driver.py after the measurement passes printed them.
import json, os, re, html, sqlite3, sys, io, contextlib, unicodedata, subprocess
from collections import Counter
ROOT = subprocess.check_output(['git', 'rev-parse', '--show-toplevel'], text=True).strip()
DATE = '2026-09-18'
CH = 8
UIDS = ['deu_08_manna_humility']
SPANS = {'deu_08_manna_humility': (8, 1, 20)}
PREFIX = {'deu_08_manna_humility': 'DV08'}
PISKAOT = []   # NO piska head on the chapter (typed from ch8_dump0's A print: the heads by chapter (6, 6), (11, 21); the nearest 36 on 6:9, 37 on 11:10)
EXP2DB = {e: [e] for e in range(1, 21)}   # the identity — 20 = 20 (chapter 5 the book's one split)
DB2EXP = {d: e for e, ds in EXP2DB.items() for d in ds}
# the Hebrew's book-named citations of chapter 8 (the regex reads "(דברים ח ז)"; a RANGE form "(דברים ח ה-ז)" it does not read — asserted by string below)
OUTSIDE_HE = [(19, 2, (8, 7)), (32, 10, (8, 5)), (32, 12, (8, 7)), (37, 5, (8, 9)), (39, 8, (8, 7)), (40, 10, (8, 10)), (43, 7, (8, 14)), (48, 8, (8, 19)), (48, 10, (8, 3)), (53, 1, (8, 16)), (297, 4, (8, 8)), (313, 15, (8, 15)), (318, 1, (8, 12)), (318, 1, (8, 13)), (318, 1, (8, 14))]
# the English's "(Dt.8:n" citations — twenty-six hits on fifteen rows (39:4 seven times; the English's 53:1 form "(be’akharitecha; Dt.8:16)" the regex does not read)
OUTSIDE_EN = [(19, 2, (8, 7)), (32, 10, (8, 5)), (32, 12, (8, 5)), (32, 12, (8, 7)), (32, 15, (8, 5)), (37, 5, (8, 9)), (39, 4, (8, 7)), (39, 4, (8, 7)), (39, 4, (8, 8)), (39, 4, (8, 8)), (39, 4, (8, 9)), (39, 4, (8, 9)), (39, 4, (8, 10)), (39, 6, (8, 7)), (39, 8, (8, 7)), (40, 10, (8, 10)), (43, 7, (8, 13)), (43, 7, (8, 14)), (48, 8, (8, 19)), (48, 10, (8, 3)), (48, 10, (8, 3)), (297, 4, (8, 8)), (313, 15, (8, 15)), (318, 1, (8, 12)), (318, 1, (8, 13)), (318, 1, (8, 14))]
OUTSIDE = [(19, 2), (32, 10), (32, 12), (32, 15), (37, 5), (39, 4), (39, 6), (39, 8), (40, 10), (43, 7), (48, 8), (48, 10), (53, 1), (297, 4), (313, 15), (318, 1)]   # the SIXTEEN rows READ WHOLE: the union of both files
INTERPOLATION = []   # no translator's own citation this chapter (chapter 7's 37:1 form checked: every English citation quotes a verse the Hebrew quotes too — 39:6 the one DIVISION difference, below)
EXCLUDED = []   # no slip (no cited verse beyond 20)
CITED = {(19, 2): [7], (32, 10): [5], (32, 12): [5, 7], (32, 15): [5, 6, 7], (37, 5): [9], (39, 4): [7, 8, 9, 10], (39, 6): [7], (39, 8): [7], (40, 10): [10], (43, 7): [12, 13, 14], (48, 8): [19], (48, 10): [3], (53, 1): [16], (297, 4): [8], (313, 15): [15], (318, 1): [12, 13, 14]}
CITED_DB = {k: v[0] for k, v in CITED.items()}
PRIOR_READ = {(19, 2): 'deu_01_03_devarim_2026-09-15.md', (32, 10): 'deu_06_vaetchanan_2026-09-17.md', (32, 12): 'deu_06_vaetchanan_2026-09-17.md', (32, 15): 'deu_06_vaetchanan_2026-09-17.md', (318, 1): 'gen_25_babel_2026-08-25.md'}   # five read before — REREAD WHOLE here (the whole-row rule; the credit guard's quick look), named as prior reads in their rows
FRESH = OUTSIDE[:]   # every one of the sixteen read whole this sitting
CREDITED = {}
TITLE = 'Chapter 8 — All the commandment, that you may live and possess the land; remember the way of forty years in the wilderness — the humbling, the testing, the manna, "not by bread alone", the garment that did not wear out, the discipline of a son; a good land of streams and deeps, of wheat and barley and vine and fig and pomegranate, of olive oil and honey, of iron and copper; eat, be satisfied, bless; take heed lest you forget — the houses, the herds, the silver and gold, the heart lifted up — who brought you out, who led you through the serpents and the thirst, who brought water from the flint, who fed you manna to do you good in your end; "my power and the might of my hand" — He gives the power, to establish His covenant; if you surely forget and serve other gods, I testify today that you shall surely perish, like the nations, because you would not hear'
OUT = f'{ROOT}/logic/oral_triage/deu_08_ekev_{DATE}.md'

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
# THE SHELF BY POSITION — the heads around chapter 8: NONE on the chapter (nor on 7, 9, 10); 34-36 on 6:7-9 before, 37-38 on 11:10 and 39 on 11:11 after
assert len(sif) == 357 and len(sif_he) == 357 and sum(len(s) for s in sif) == 2357 and sum(len(s) for s in sif_he) == 2357
assert {p: heads[p] for p in range(34, 40)} == {34: (6, 7), 35: (6, 8), 36: (6, 9), 37: (11, 10), 38: (11, 10), 39: (11, 11)}, {p: heads[p] for p in range(34, 40)}
HC = Counter(h[0] for h in heads.values() if h)
assert [p for p, h in heads.items() if h and h[0] == 8] == [] and HC[7] == 0 and HC[8] == 0 and HC[9] == 0 and HC[10] == 0 and sorted(HC.items())[:8] == [(1, 24), (3, 4), (6, 6), (11, 21), (12, 20), (13, 14), (14, 14), (15, 16)], sorted(HC.items())[:8]
def he_cites(t): return [(b, hn(c), hn(v)) for b, c, v in re.findall(r'\(([א-ת]+(?: [א-ת])?) ([א-ת]{1,3}) ([א-ת]{1,3})\)', t)]
CIT_HE = [(p, r, (8, c[2])) for p in range(1, 358) for r in range(1, len(sif_he[p - 1]) + 1) for c in he_cites(Hb(p, r)) if c[0] == 'דברים' and c[1] == 8]
CIT_EN = [(p, r, (8, int(m.group(2)))) for p in range(1, 358) for r in range(1, len(sif[p - 1]) + 1) for m in re.finditer(r'\((?:Deut(?:eronomy)?\.?|Dt\.?|Devarim) ?(8):(\d+)', E(p, r))]
assert CIT_HE == OUTSIDE_HE and CIT_EN == OUTSIDE_EN, (CIT_HE, CIT_EN)
UNION = sorted({(p, r) for p, r, _ in CIT_HE} | {(p, r) for p, r, _ in CIT_EN})
assert UNION == OUTSIDE and len(UNION) == 16 and all(1 <= v <= 20 for _, _, (_, v) in CIT_HE + CIT_EN)   # a cited verse beyond the chapter's length would be a slip (chapter 6's lesson): none
assert [(p, r) for p in range(1, 358) for r in range(1, len(sif[p - 1]) + 1) if re.search(r'\((?:Ibid|ibid)\.? ?8:\d+\)', E(p, r))] == []
assert {p: heads[p] for p, _ in OUTSIDE} == {19: (1, 20), 32: (6, 5), 37: (11, 10), 39: (11, 11), 40: (11, 12), 43: (11, 15), 48: (11, 22), 53: (11, 26), 297: (26, 1), 313: (32, 10), 318: (32, 15)}, {p: heads[p] for p, _ in OUTSIDE}
def has_points(s): return any(0x05B0 <= ord(c) <= 0x05BD for c in s)
assert all(has_points(Hb(p, r)) for p, r in OUTSIDE)
# THE RANGE CITATIONS the Hebrew regex does not read — asserted by string: 32:15 "(דברים ח ה-ז)", 39:4 "(דברים ח ז-י)", 43:7 "(דברים ח יב-יג)"; the English's 53:1 "Dt.8:16)" behind a transliteration
assert '(דברים ח ה-ז)' in HB0(32, 15) and '(דברים ח ז-י)' in HB0(39, 4) and '(דברים ח יב-יג)' in HB0(43, 7) and 'Dt.8:16)' in E(53, 1) and '(Dt.8:5-7)' in E(32, 15) and E(39, 4).count('(Dt.8:') == 7 and '(Dt.8:13-14)' in E(43, 7)
# THE ONE DIVISION DIFFERENCE: the English's 39:6 row runs on through what the Hebrew divides as 39:6, 39:7 and 39:8 — the citation of 8:7 sits in the Hebrew's 39:8 and in the English's 39:6; both rows read whole
assert 'דברים ח' not in HB0(39, 6) and '(זכריה י א)' in HB0(39, 6) and '(דברים ח ז)' in HB0(39, 8) and '(Dt.8:7)' in E(39, 6) and '(Dt.8:7)' in E(39, 8) and 'snow' in E(39, 6) and 'dew' in E(39, 6) and len(sif_he[38]) == len(sif[38]) == 11
# THE ROWS' CONTENT (the consonants of the shelf's bytes)
assert '(דברים ח ז)' in HB0(19, 2) and 'לפידגוג' in HB0(19, 2) and 'ארבעים שנה' in HB0(19, 2) and '(Dt. 8:7)' in E(19, 2) and '(Dt.1:20)' in E(19, 2)   # the tutor's parable: forty years Moses said "a good land" (8:7); at the Land, "you have come"
assert '(דברים ח ה)' in HB0(32, 10) and 'רבי מאיר' in HB0(32, 10) and 'ויסורים' in HB0(32, 10) and '(Dt.8:5)' in E(32, 10)   # R. Meir on 6:5: the chastisements not as the deeds
assert '(דברים ח ז)' in HB0(32, 12) and 'ברית כרותה ליסורים' in HB0(32, 12) and '(Dt.8:5)' in E(32, 12) and '(Dt.8:7)' in E(32, 12)   # R. Nathan b. R. Joseph: a covenant cut for chastisements as for the Land (8:5, then 8:7)
assert 'ארץ ישראל מנין' in HB0(32, 15) and 'מיסרך' in HB0(32, 15) and 'ארץ טובה' in HB0(32, 15)   # the Land — whence? 8:5-7
assert '(דברים ח ט)' in HB0(37, 5) and 'תבל' in HB0(37, 5) and 'לא תחסר כל בה' in HB0(37, 5) and '(Dt.8:9)' in E(37, 5) and '(Prov.8:31)' in E(37, 5)   # R. Shimon b. Yohai: the world = the Land, spiced with all — "you shall lack nothing"
assert 'שתים עשרה ארצות' in HB0(39, 4) and HB0(39, 4).count('ארץ') >= 10 and 'ארץ חטה ושערה' in HB0(39, 4) and '(Dt.11:9)' in E(39, 4) and 'Twelve lands' in E(39, 4)   # twelve lands for twelve tribes — 8:7-10's "land" clauses counted among them
assert 'מי שלוחים' in HB0(39, 8) and 'ארץ נחלי מים' in HB0(39, 8)   # the Land drinks irrigation water too — "a land of brooks of water"
assert '(דברים ח י)' in HB0(40, 10) and 'ואכלת ושבעת וברכת' in HB0(40, 10) and '(שמות כג כה)' in HB0(40, 10) and '(Dt.8:10)' in E(40, 10) and '(Ex.23:25)' in E(40, 10) and '(Hag.2:19)' in E(40, 10)   # the blessing in the house — even in eating and satisfaction (8:10), even in the belly (Exodus 23:25)
assert '(דברים ח יד)' in HB0(43, 7) and 'מתוך שובע' in HB0(43, 7) and 'ורם לבבך ושכחת' in HB0(43, 7) and '(שמות לב ו)' in HB0(43, 7) and '(Dt.8:14)' in E(43, 7) and '(Ex.32:6)' in E(43, 7) and '(Dt. 31:20)' in E(43, 7)   # a person rebels only out of satiety: 8:12-14, 31:20, the calf
assert '(דברים ח יט)' in HB0(48, 8) and 'שכח תשכח' in HB0(48, 8) and '(משלי כג ה)' in HB0(48, 8) and 'במגלת חריסים' in HB0(48, 8) and '(Dt.8:19)' in E(48, 8) and 'megillat kharisim' in E(48, 8)   # forget the first and the last go: "if you surely forget"; "a day you leave Me, two days I leave you"
assert '(דברים ח ג)' in HB0(48, 10) and 'זה מדרש' in HB0(48, 10) and 'אלו הלכות והגדות' in HB0(48, 10) and E(48, 10).count('(Dt.8:3)') == 2 and 'R. Shimon b. Menasya' in E(48, 10)   # "not by bread alone" = midrash; "all that proceeds" = the laws and the homilies
assert '(דברים ח טז)' in HB0(53, 1) and 'להיטבך באחריתך' in HB0(53, 1) and 'פרשת דרכים' in HB0(53, 1) and '(Dt.30:19)' in E(53, 1) and 'crossroad' in E(53, 1)   # the two paths: the righteous suffer two or three days — "to do you good in your end"
assert '(דברים ח ח)' in HB0(297, 4) and 'משבעת המינים' in HB0(297, 4) and 'חטה ושערה וגפן ותאנה ורמון' in HB0(297, 4) and '(Dt.8:8)' in E(297, 4) and 'M. Bik.1:10' in E(297, 4) and '(Ex.23:19)' in E(297, 4)   # the first-fruits from the seven species for which the Land is praised — 8:8 the list
assert '(דברים ח טו)' in HB0(313, 15) and 'ארבע מלכיות' in HB0(313, 15) and '(Dt.8:15)' in E(313, 15) and 'four' in E(313, 15)   # "the great and terrible wilderness" (8:15) = the four kingdoms
assert '(דברים ח יב)' in HB0(318, 1) and '(דברים ח יג)' in HB0(318, 1) and '(דברים ח יד)' in HB0(318, 1) and 'לפי שבע מורדים' in HB0(318, 1) and 'בריתא' in HB0(318, 1) and '(Dt.8:12)' in E(318, 1) and '(Dt.8:14)' in E(318, 1) and 'lacuna' in E(318, 1)   # Jeshurun grew fat: out of satiety they rebel — the Flood, the Tower, Sodom, the calf, and Israel in the Land (8:12-14); the copyist's abridgement noted
# THE PRIOR READS — the strict row form over every ledger: FIVE of the sixteen read before (19:2 at sitting 1; 32:10, 32:12, 32:15 at chapter 6's sitting; 318:1 as a dup row at a Genesis sitting) — every one REREAD WHOLE here; no Onkelos row of chapter 8 anywhere
TRI = f'{ROOT}/logic/oral_triage'
LED = {f: open(f'{TRI}/{f}', encoding='utf-8').read() for f in os.listdir(TRI) if f.endswith('.md') and os.path.isfile(f'{TRI}/{f}') and f'{TRI}/{f}' != OUT}
PRIOR = sorted({(f, int(a), int(b)) for f, t in LED.items() for a, b in re.findall(r'Sifrei Devarim (\d+):(\d+)', t)})
assert [(f, p, r) for f, p, r in PRIOR if (p, r) in OUTSIDE] == [(f, p, r) for (p, r), f in sorted(PRIOR_READ.items(), key=lambda kv: (kv[1], kv[0]))] and len(PRIOR) == 297, (len(PRIOR), [(f, p, r) for f, p, r in PRIOR if (p, r) in OUTSIDE])
assert sorted(f for f, t in LED.items() if re.search(r'^- Onkelos Deut 8:', t, re.M)) == []
NAMING = sorted(f for f, t in LED.items() if re.search(r'Deut(?:eronomy)? 8:\d+', t))
assert NAMING == ['deu_01_03_devarim_exam_2026-09-15.md', 'deu_06_vaetchanan_2026-09-17.md', 'num_20_meribah_edom_aaron_2026-09-11.md', 'num_21_snakes_conquest_2026-09-11.md', 'num_28_29_musafim_exam_2026-09-11.md'], NAMING
assert 'Deuteronomy 8:10' in LED['deu_01_03_devarim_exam_2026-09-15.md'] and 'Deut 8:15' in LED['num_21_snakes_conquest_2026-09-11.md'] and 'Deut 8:8' in LED['num_28_29_musafim_exam_2026-09-11.md'] and 'Deut 8:8' in LED['num_20_meribah_edom_aaron_2026-09-11.md']
# THE KIN'S READS: no ledger holds an Onkelos row of Exodus 16 or 17 (the manna and the rock at Horeb were read through the Mekhilta — eight rows over the ledgers); the Numbers kin read whole at the Numbers walk
assert sorted(f for f, t in LED.items() if re.search(r'^- Onkelos Exod (16|17):', t, re.M)) == [] and sum(len(re.findall(r'Mekhilta[^\n]{0,40}(?:16|17):\d+', t)) for t in LED.values()) == 8
assert sorted(f for f, t in LED.items() if re.search(r'^- Onkelos Num (11|14|20|21):', t, re.M)) == ['num_11_complaint_quail_2026-09-10.md', 'num_14_rejection_2026-09-10.md', 'num_20_meribah_edom_aaron_2026-09-11.md', 'num_21_snakes_conquest_2026-09-11.md']
def kinrows(f, pat): return len(re.findall(r'^- Onkelos ' + pat, LED[f], re.M))
assert kinrows('num_11_complaint_quail_2026-09-10.md', r'Num 11:[4-9]\b') == 6 and kinrows('num_14_rejection_2026-09-10.md', r'Num 14:3[34]\b') == 2 and kinrows('num_20_meribah_edom_aaron_2026-09-11.md', r'Num 20:(?:[1-9]|1[0-3])\b') == 13 and kinrows('num_21_snakes_conquest_2026-09-11.md', r'Num 21:[4-9]\b') == 6
ONK_LEN = {c: len(onk[c - 1]) for c in (3, 4, 5, 6, 7, 8)}
assert len(onk) == 34 and len(onk_he) == 34 and ONK_LEN == {3: 29, 4: 49, 5: 30, 6: 25, 7: 26, 8: 20} and sum(len(c) for c in onk_he) == 956
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
assert VC[5] == 33 and VC[6] == 25 and VC[7] == 26 and VC[8] == 20 and VC[9] == 29 and sum(VC.values()) == 959 and len(VC) == 34
assert [(c, len(onk_he[c - 1]), VC[c]) for c in range(1, 35) if len(onk_he[c - 1]) != VC[c]] == [(5, 30, 33)]
# THE ALIGNMENT RECOMPUTED (ch8_dump0's A0): the export's twenty rows against the DB's twenty verses over token and negation counts — the identity, cost 25
by8 = {v: [plain(he) for he, in db.execute("SELECT w.he FROM words w JOIN verses v ON w.verse_id=v.id WHERE v.book='Deut' AND v.chapter=8 AND v.verse=? ORDER BY w.idx", (v,))] for v in range(1, 21)}
NEG = ('לא', 'ולא')
D_ = [(len(by8[v]), sum(1 for x in by8[v] if x in NEG)) for v in range(1, 21)]
E_ = [(len(plain(clean(r)).split()), sum(1 for x in plain(clean(r)).split() if x.strip('.:') in NEG)) for r in onk_he[7]]
def _cost(e, ds): return abs(e[0] - sum(d[0] for d in ds)) + 3 * abs(e[1] - sum(d[1] for d in ds))
INF = 10 ** 9; best = {(0, 0): (0, None)}
for i in range(1, 21):
    for j in range(i, 21):
        cands = [(best[(i - 1, k)][0] + _cost(E_[i - 1], D_[k:j]), k) for k in range(i - 1, j) if (i - 1, k) in best and j - k <= 4]
        best[(i, j)] = min(cands) if cands else (INF, None)
i, j, ALIGN = 20, 20, {}
while i > 0:
    k = best[(i, j)][1]; ALIGN[i] = list(range(k + 1, j + 1)); i, j = i - 1, k
assert ALIGN == EXP2DB and best[(20, 20)][0] == 25 and Counter(ds[0] - e for e, ds in EXP2DB.items()) == Counter({0: 20}) and len(onk_he[7]) == 20 == VC[8], (best[(20, 20)][0], ALIGN)
def unit_text(uid): return open(f'{ROOT}/logic/units/{uid}.yaml', encoding='utf-8').read()
def steps(uid): return sorted({(int(a), int(b)) for a, b in re.findall(r'STEP_Dt_(\d+)_(\d+)', unit_text(uid))})
FIRST = not os.path.exists(OUT)
for uid, (c, lo, hi) in SPANS.items():
    t = unit_text(uid)
    assert steps(uid) == [(c, v) for v in range(lo, hi + 1)] and re.search(rf'refs: "?{c}:{lo}-{hi}"?', t) and '\nbinary_trees:' in t, uid
    if FIRST: assert 'status: draft' in t and 'operators:' not in t and '- step: E' not in t, uid
    assert t.count(f'  - id: STEP_Dt_{c}_{lo}\n') == 1 and t.count(f'  - id: STEP_Dt_{c}_{hi}\n') == 1, uid
UT8 = unit_text('deu_08_manna_humility')
assert UT8.count('\n    comment:') + UT8.count('\n      comment:') == 24 and UT8.count('\n  - id: S') == 27   # typed from ch8_dump0's G print (the draft's comment lines and scenarios)
assert 'deu_07_nations_cherem' in UT8 and 'exo_16_manna_shabbat' in UT8 and steps('deu_09_not_righteousness')[0] == (9, 1) and steps('deu_09_not_righteousness')[-1] == (9, 29)
assert sorted(f for f in os.listdir(TRI) if f.startswith('deu_') and f != os.path.basename(OUT)) == ['deu_01_03_devarim_2026-09-15.md', 'deu_01_03_devarim_exam_2026-09-15.md', 'deu_04_vaetchanan_2026-09-16.md', 'deu_04_vaetchanan_exam_2026-09-16.md', 'deu_05_vaetchanan_2026-09-16.md', 'deu_05_vaetchanan_exam_2026-09-16.md', 'deu_06_vaetchanan_2026-09-17.md', 'deu_06_vaetchanan_exam_2026-09-17.md', 'deu_07_vaetchanan_ekev_2026-09-17.md', 'deu_07_vaetchanan_ekev_exam_2026-09-18.md']
ALLTXT = ''.join(open(f'{ROOT}/logic/units/{f}', encoding='utf-8').read() for f in os.listdir(f'{ROOT}/logic/units') if f.endswith('.yaml') and f[:-5] not in UIDS) + ''.join(open(f'{ROOT}/logic/oral_audit/manifests/{f}', encoding='utf-8').read() for f in os.listdir(f'{ROOT}/logic/oral_audit/manifests') if f.endswith('.json') and not f.startswith('deu_08'))
assert all(f'"{p}-' not in ALLTXT and f'[claim {p}-' not in ALLTXT for p in PREFIX.values())
SPAN = [(8, v) for v in range(1, VC[8] + 1)]
NV = 20
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
def W8(v): return words('Deut', 8, v)
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
for c, v, idx, hp, g in store.execute("SELECT v.chapter, v.verse, w.idx, w.he_plain, w.gloss FROM words w JOIN verses v ON w.verse_id=v.id WHERE v.book='Deut' AND v.chapter = 8 ORDER BY v.id, w.idx"):
    SG.setdefault((c, v), []).append((idx, hp.replace('/', ''), g))
def sg(c, v, tok, nth=0):
    hit = [g for _, hp, g in SG[(c, v)] if hp == tok]
    if len(hit) <= nth: raise KeyError((c, v, tok, nth))
    return hit[nth]
def sidx(c, v, tok, nth=0):
    hit = [i for i, hp, _ in SG[(c, v)] if hp == tok]
    assert len(hit) > nth, (c, v, tok, nth, hit)
    return hit[nth]
STORE_MISMATCH = [(c, v, n, len(by[('Deut', c, v)])) for c, v, n in store.execute("SELECT v.chapter, v.verse, COUNT(*) FROM words w JOIN verses v ON w.verse_id=v.id WHERE v.book='Deut' AND v.chapter=8 GROUP BY v.chapter, v.verse").fetchall() if n != len(by[('Deut', c, v)])]
# THE STORE = THE DB at every verse but ONE: 8:2 — the store carries the written מצותו ("His commandments", the ketiv, wtype x-ketiv in the DB) AND the read מצותיו (the qere): THE
# CHAPTER'S ONE WRITTEN/READ PAIR, the same written form as 7:9's and 5:10's (the token's five Bible seats: 5:10, 7:9, 8:2, 27:10, Numbers 15:31); no large letter; 293 tokens,
# 1,148 letters; the two unglossed tokens "I" (אנכי, 8:1 and 8:11).
assert STORE_MISMATCH == [(8, 2, 24, 23)] and [(v, hp) for v in range(1, 21) for i, (_, hp, _) in enumerate(SG[(8, v)]) if v != 2 and hp != W8(v)[i]] == [] and [hp for _, hp, _ in SG[(8, 2)]][20:22] == ['מצותו', 'מצותיו']
assert byw[('Deut', 8, 2)][20] == 'x-ketiv' and W8(2)[20] == 'מצותו' and Counter(wt for v in range(1, 21) for wt in byw[('Deut', 8, v)]) == Counter({None: 292, 'x-ketiv': 1}) and U('מצותו') == ['Deut 27:10', 'Deut 5:10', 'Deut 7:9', 'Deut 8:2', 'Num 15:31'] and byw[('Deut', 7, 9)][13] == 'x-ketiv'
assert sum(1 for ws in byw.values() for wt in ws if wt == 'x-ketiv') == 1268
TOK = sum(len(W8(v)) for v in range(1, 21)); LET = sum(len(x) for v in range(1, 21) for x in W8(v))
assert TOK == 293 and LET == 1148 and {v: len(W8(v)) for v in range(1, 21)} == {1: 19, 2: 23, 3: 28, 4: 10, 5: 12, 6: 9, 7: 15, 8: 10, 9: 18, 10: 12, 11: 16, 12: 7, 13: 11, 14: 11, 15: 16, 16: 13, 17: 10, 18: 20, 19: 20, 20: 13}, TOK
assert [(v, hp) for (c, v), g in sorted(SG.items()) for _, hp, gl in g if gl == '?'] == [(1, 'אנכי'), (11, 'אנכי')]
# THE ENGINE'S PARSER on every verse — MEASURED before the compile is asked: TWO number verses, 8:2 and 8:4 "these forty years" [40] (2:7 and 29:4 the same reading; the
# wilderness's forty years at Exodus 16:35, Numbers 14:33-34, 32:13, Joshua 5:6, Nehemiah 9:21, Psalm 95:10, Amos 2:10 — [40] at every seat; 1:3's date [40, 11, 1]); the
# seven-stem homograph "AND YOU SHALL BE SATISFIED" (ושבעת, 8:10 and 8:12, the lemma 7646) STARRED — 6:11, 11:15, 31:20 the same star; "swore" (נשבע, 8:1 and 8:18 — the lemma 7650)
# not a number at all; no ordinal; NO GAP.
sys.path.insert(0, f'{ROOT}/World/step9')
with contextlib.redirect_stdout(io.StringIO()):
    import cold_run_sequence as CS
def N(b, c, v): return CS.ink_numbers(CS.verse_words(b, c, v))
def O(b, c, v): return CS.ink_ordinals(CS.verse_words(b, c, v))
def MARKS(c, v): return [t for t in CS.verse_words('Deut', c, v) if t[-1] in '#~^%@|*']
PARSED = {(c, v): N('Deut', c, v) for (c, v) in SPAN if N('Deut', c, v)}
assert PARSED == {(8, 2): [40], (8, 4): [40]} and {(c, v): O('Deut', c, v) for (c, v) in SPAN if O('Deut', c, v)} == {} and [((c, v), t) for (c, v) in SPAN for t in MARKS(c, v)] == [((8, 10), 'ושבעת*'), ((8, 12), 'ושבעת*')], PARSED
assert N('Deut', 2, 7) == [40] and N('Deut', 29, 4) == [40] and N('Exod', 16, 35) == [40] and N('Num', 14, 33) == [40] and N('Num', 14, 34) == [40, 40] and N('Num', 32, 13) == [40] and N('Deut', 1, 3) == [40, 11, 1] and N('Josh', 5, 6) == [40] and N('Neh', 9, 21) == [40] and N('Ps', 95, 10) == [40] and N('Amos', 2, 10) == [40]
assert N('Deut', 6, 11) == [] and N('Deut', 11, 15) == [] and N('Deut', 31, 20) == [] and N('Deut', 4, 26) == [] and N('Deut', 30, 18) == [] and MARKS(6, 11) == ['ושבעת*'] and MARKS(11, 15) == ['ושבעת*'] and MARKS(31, 20) == ['ושבע*']
assert lemma_of('Deut', 8, 1, 'נשבע') == ['7650'] and lemma_of('Deut', 8, 18, 'נשבע') == ['7650'] and lemma_of('Deut', 8, 10, 'ושבעת') == ['7646'] and lemma_of('Deut', 8, 12, 'ושבעת') == ['7646'] and lemma_of('Deut', 8, 2, 'ארבעים') == ['705'] and morphs('Deut', 8, 2)[9] == 'HAcbpa' and morphs('Deut', 8, 4)[8] == 'HAcbpa'
assert [(s, x) for s, x, m in LEMT('7646', books=('Deut',))] == [('Deut 6:11', 'ושבעת'), ('Deut 8:10', 'ושבעת'), ('Deut 8:12', 'ושבעת'), ('Deut 11:15', 'ושבעת'), ('Deut 14:29', 'ושבעו'), ('Deut 26:12', 'ושבעו'), ('Deut 31:20', 'ושבע')]
assert [(s, x) for s, x, m in LEMT('705', books=('Deut',))] == [('Deut 1:3', 'בארבעים'), ('Deut 2:7', 'ארבעים'), ('Deut 8:2', 'ארבעים'), ('Deut 8:4', 'ארבעים'), ('Deut 9:9', 'ארבעים'), ('Deut 9:9', 'וארבעים'), ('Deut 9:11', 'ארבעים'), ('Deut 9:11', 'וארבעים'), ('Deut 9:18', 'ארבעים'), ('Deut 9:18', 'וארבעים'), ('Deut 9:25', 'ארבעים'), ('Deut 9:25', 'ארבעים'), ('Deut 10:10', 'ארבעים'), ('Deut 10:10', 'וארבעים'), ('Deut 25:3', 'ארבעים'), ('Deut 29:4', 'ארבעים')]
assert P('זה', 'ארבעים', 'שנה') == ['Deut 2:7', 'Deut 8:2', 'Deut 8:4'] and len(P('ארבעים', 'שנה')) == 31 and [s for s in P('ארבעים', 'שנה') if s.startswith(('Exod', 'Num', 'Deut'))] == ['Deut 29:4', 'Deut 2:7', 'Deut 8:2', 'Deut 8:4', 'Exod 16:35', 'Num 14:33', 'Num 14:34', 'Num 32:13']
# THE FRAMES AND THE REGISTER: NO divine frame, NO "saying" — the whole chapter Moses' voice; the narrative verbs THREE, all God's past acts at 8:3 ("and He humbled you, and let you
# hunger, and fed you"); ONE IMPERATIVE — "take heed" (8:11, the niphal); TWO INFINITIVE ABSOLUTES, both at 8:19 ("if you SURELY forget", "you shall SURELY perish"); the law's
# form the consecutive perfect in ten verses; the PROHIBITION form "not + imperfect" TWICE and both promises or reports, not commands (8:9 "you shall not lack", 8:20 "you would
# not hear") — the chapter's negatives are the past (8:3 "you did not know", 8:4 "did not wear out … did not swell"); the second person SINGULAR in sixteen verses, PLURAL in
# one (8:20), BOTH in two (8:1 the frame, 8:19 "I testify against YOU … you shall perish"), NEITHER in 8:8 (the seven species — no verb, no person); the first person
# Moses' (8:1, 8:11 "I command", 8:19 "I testify") and the boaster's (8:17 "my power … my hand … for me"), no "we"; "for/that" six seats, "if" two (8:2 the question's tail, 8:19
# the case), "lest" two (8:11, 8:12) — no "or", no "when"; "so that" six seats (the book's forty-three); the Name thirteen bare tokens; "the LORD your God" nine singular
# and ONE plural (8:20 — the frame's close); the Name without "your God" at 8:1, 8:3, 8:20; Moses and Israel never named; Egypt at 8:14 alone; the fathers at 8:1, 3, 16, 18.
NUM = {v: (sum(1 for m in morphs('Deut', 8, v) if m and '2mp' in m), sum(1 for m in morphs('Deut', 8, v) if m and '2ms' in m)) for v in range(1, 21)}
assert [v for v, (p, s) in NUM.items() if s and not p] == [2, 3, 4, 5, 6, 7, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18] and [v for v, (p, s) in NUM.items() if p and not s] == [20] and [v for v, (p, s) in NUM.items() if p and s] == [1, 19] and [v for v, (p, s) in NUM.items() if not p and not s] == [8]
assert [x for v in range(1, 21) for x, m in wm('Deut', 8, v) if m and '2mp' in m] == ['תשמרון', 'תחיון', 'ורביתם', 'ובאתם', 'וירשתם', 'לאבתיכם', 'בכם', 'תאבדון', 'מפניכם', 'תאבדון', 'תשמעון', 'אלהיכם']
assert [v for v in range(1, 21) if any(V in ('ויאמר', 'וידבר') and W8(v)[i + 1] == 'יהוה' for i, V in enumerate(W8(v)[:-1]))] == [] and [v for v in range(1, 21) if 'לאמר' in W8(v)] == [] and [v for v in range(1, 21) if 'משה' in W8(v) or 'ישראל' in W8(v)] == []
assert {v: [x for x, m in wm('Deut', 8, v) if m and re.search(r'^HC/V.w', m)] for v in range(1, 21) if any(m and re.search(r'^HC/V.w', m) for _, m in wm('Deut', 8, v))} == {3: ['ויענך', 'וירעבך', 'ויאכלך']}
assert {v: [(x, m) for x, m in wm('Deut', 8, v) if m and re.match(r'^HV.?.?v', m)] for v in range(1, 21) if any(m and re.match(r'^HV.?.?v', m) for _, m in wm('Deut', 8, v))} == {11: [('השמר', 'HVNv2ms')]}
assert {v: [(x, m) for x, m in wm('Deut', 8, v) if m and re.match(r'^H(?:C/)?V.a$', m)] for v in range(1, 21) if any(m and re.match(r'^H(?:C/)?V.a$', m) for _, m in wm('Deut', 8, v))} == {19: [('שכח', 'HVqa'), ('אבד', 'HVqa')]}
assert sorted(v for v in range(1, 21) if any(m and re.search(r'^HC/V.q', m) for _, m in wm('Deut', 8, v))) == [1, 2, 5, 6, 10, 12, 14, 17, 18, 19] and [x for x, m in wm('Deut', 8, 10) if re.search(r'^HC/V.q', m)] == ['ואכלת', 'ושבעת', 'וברכת'] and [x for x, m in wm('Deut', 8, 19) if re.search(r'^HC/V.q', m)] == ['והיה', 'והלכת', 'ועבדתם', 'והשתחוית']
PRO = {v: [(W8(v)[i + 1], morphs('Deut', 8, v)[i + 1]) for i, x in enumerate(W8(v)[:-1]) if x in NEG and morphs('Deut', 8, v)[i + 1] and morphs('Deut', 8, v)[i + 1].startswith('HV')] for v in range(1, 21) if any(x in NEG for x in W8(v))}
assert PRO == {2: [], 3: [('ידעת', 'HVqp2ms'), ('ידעון', 'HVqp3cp/Sn')], 4: [('בלתה', 'HVqp3fs'), ('בצקה', 'HVqp3fs')], 9: [('תחסר', 'HVqi2ms')], 16: [('ידעון', 'HVqp3cp/Sn')], 20: [('תשמעון', 'HVqi2mp/Sn')]}, PRO
assert sum(1 for v in PRO for _, m in PRO[v] if 'i2' in m) == 2 and sum(1 for v in PRO for _, m in PRO[v] if 'i3' in m) == 0 and {v: [x for x in W8(v) if x in NEG] for v in range(1, 21) if any(x in NEG for x in W8(v))} == {2: ['לא'], 3: ['לא', 'ולא', 'לא'], 4: ['לא', 'לא'], 9: ['לא', 'לא'], 16: ['לא'], 20: ['לא']}
assert {f'8:{v}': [x for x in W8(v) if x in ('כי', 'אם', 'ואם', 'או', 'פן')] for v in range(1, 21) if any(x in ('כי', 'אם', 'ואם', 'או', 'פן') for x in W8(v))} == {'8:2': ['אם'], '8:3': ['כי', 'כי'], '8:5': ['כי'], '8:7': ['כי'], '8:11': ['פן'], '8:12': ['פן'], '8:18': ['כי'], '8:19': ['אם', 'כי']}
assert {v: [x for x in W8(v) if x in ('למען', 'ולמען')] for v in range(1, 21) if any(x in ('למען', 'ולמען') for x in W8(v))} == {1: ['למען'], 2: ['למען'], 3: ['למען'], 16: ['למען', 'ולמען'], 18: ['למען']} and len(U('למען', 'ולמען', books=('Deut',))) == 43
assert {v: [(x, m) for x, m in wm('Deut', 8, v) if m and '1cs' in m] for v in range(1, 21) if any(m and '1cs' in m for _, m in wm('Deut', 8, v))} == {1: [('אנכי', 'HPp1cs')], 11: [('אנכי', 'HPp1cs')], 17: [('כחי', 'HNcmsc/Sp1cs'), ('ידי', 'HNcbsc/Sp1cs'), ('לי', 'HR/Sp1cs')], 19: [('העדתי', 'HVhp1cs')]} and not any('1cp' in (m or '') for v in range(1, 21) for _, m in wm('Deut', 8, v))
assert [(v, x) for v in range(1, 21) for x, m in wm('Deut', 8, v) if m and m.startswith('HTd/V') and 'r' in m[6:8]] == [(14, 'המוציאך'), (15, 'המוליכך'), (15, 'המוציא'), (16, 'המאכלך'), (18, 'הנתן')]   # the article + participle chain: who brought you out, who led you, who brought out water, who fed you — and who gives you power
assert {v: [x for x, m in wm('Deut', 8, v) if m and re.search(r'^H(?:C/|R/|Td/|C/R/)?V.r', m)] for v in range(1, 21) if any(m and re.search(r'^H(?:C/|R/|Td/|C/R/)?V.r', m) for _, m in wm('Deut', 8, v))} == {1: ['מצוך'], 5: ['מיסרך'], 7: ['מביאך', 'יצאים'], 11: ['מצוך'], 14: ['המוציאך'], 15: ['המוליכך', 'המוציא'], 16: ['המאכלך'], 18: ['הנתן'], 20: ['מאביד']}
assert Counter(x for v in range(1, 21) for x in W8(v) if x in ('יהוה', 'ויהוה', 'ביהוה', 'כיהוה', 'ליהוה')) == Counter({'יהוה': 13}) and [v for v in range(1, 21) for i in range(len(W8(v)) - 1) if W8(v)[i:i + 2] == ['יהוה', 'אלהיך']] == [2, 5, 6, 7, 10, 11, 14, 18, 19] and [v for v in range(1, 21) for i in range(len(W8(v)) - 1) if W8(v)[i:i + 2] == ['יהוה', 'אלהיכם']] == [20]
assert [v for v in range(1, 21) for i in range(len(W8(v))) if W8(v)[i] == 'יהוה' and (i + 1 >= len(W8(v)) or W8(v)[i + 1] not in ('אלהיך', 'אלהיכם'))] == [1, 3, 20] and {v: [x for x in W8(v) if x in ('פרעה', 'לפרעה', 'מצרים')] for v in range(1, 21) if any(x in ('פרעה', 'לפרעה', 'מצרים') for x in W8(v))} == {14: ['מצרים']}
assert {v: [x for x in W8(v) if 'אבת' in x] for v in range(1, 21) if any('אבת' in x for x in W8(v))} == {1: ['לאבתיכם'], 3: ['אבתיך'], 16: ['אבתיך'], 18: ['לאבתיך']} and {v: [x for x in W8(v) if x in ('אלהים', 'האלהים', 'אלהי', 'האל', 'אל')] for v in range(1, 21) if any(x in ('אלהים', 'האלהים', 'אלהי', 'האל', 'אל') for x in W8(v))} == {7: ['אל'], 19: ['אלהים']}
# THE PARAGOGIC NUN — the long imperfect and perfect forms (/Sn): EIGHT in the chapter (8:1 "you shall keep … you may live", 8:3 and 8:16 "your fathers did not know", 8:13 "shall multiply", 8:19 and 8:20 "you shall perish", 8:20 "you would not hear") — the book's densest chapter after 4 (thirteen)
assert {v: [x for x, m in wm('Deut', 8, v) if m and m.endswith('/Sn')] for v in range(1, 21) if any(m and m.endswith('/Sn') for _, m in wm('Deut', 8, v))} == {1: ['תשמרון', 'תחיון'], 3: ['ידעון'], 13: ['ירבין'], 16: ['ידעון'], 19: ['תאבדון'], 20: ['תאבדון', 'תשמעון']}
assert sorted(Counter(c for (b, c, v), ws in by.items() if b == 'Deut' for _, m in ws if m and m.endswith('/Sn')).items()) == [(1, 6), (2, 1), (4, 13), (5, 4), (6, 4), (7, 4), (8, 8), (11, 1), (12, 6), (13, 2), (17, 2), (18, 2), (29, 1), (30, 2), (31, 1), (33, 1)]
# THE KIN DIFFED (the DB's tokens): 8:1 against 4:1, 11:8, 30:16 ("and go in and possess" 4:1, 8:1, 11:8 — the three seats; "all the commandment" eight, all this book's); 8:2 against
# 29:4 and 2:7 ("these forty years" 2:7, 8:2, 8:4 — the three seats) and Exodus 16:4 ("whether … or not" — the manna's own test-clause, the two tokens shared at the end);
# 8:3 against Exodus 16:15 ("for they did not know" shared) and 8:16 (the doublet — "your fathers did not know … to humble you … to test you"); 8:4 against 29:4 ("did not
# wear out" shared) and Nehemiah 9:21 (the only other "did not swell"); 8:5 against 1:31 ("as a man … his son" — the carrying there, the discipline here: the two seats);
# 8:6 against 28:9 and 30:16 ("walk in His ways"); 8:7 against Exodus 3:8 ("to a good land") and 10:7 ("brooks of water"); 8:8 against 2 Kings 18:32 (the Rabshakeh's "a land of
# olive oil and honey" — "a land of olive" shared); 8:10 against 6:11 and 11:15 ("and you shall eat and be satisfied"); 8:11 against 6:12 (six tokens shared — "take heed to yourself
# lest you forget the LORD"), 12:13, 15:9 ("take heed to yourself lest"), 8:1 ("which I command you this day"); 8:13 against 17:17 (the king's "silver and gold he shall not
# multiply" — the same two tokens, the verb the same); 8:14 against 6:12, 5:6 (the exodus formula) and 13:11 (seven tokens shared — "the LORD your God who brought you out of the
# land of Egypt, from the house of bondage"); 8:15 against 1:19 ("terrible"), Exodus 17:6 and Psalm 114:8 ("water"); 8:16 against 8:3 and Exodus 16:35 (nothing shared — the
# retelling's own words); 8:17 against 7:17 ("in your heart") and Judges 7:2 ("my hand"); 8:18 against 7:12 ("which He swore to your fathers") and 8:1; 8:19 against 4:26 ("that you shall surely perish" shared,
# and "against you this day" beside it), 30:18, 6:14 ("after other gods"), 11:16, 8:11 ("forget the LORD your God"); 8:20 against 28:45
# ("the voice of the LORD"), Genesis 22:18 (the heel — "because"), 4:26, Exodus 19:5 (nothing shared) and 8:19.
assert SHARED(('Deut', 8, 1), ('Deut', 4, 1)) == ['ובאתם', 'וירשתם', 'את', 'הארץ', 'אשר'] and SHARED(('Deut', 8, 1), ('Deut', 11, 8)) == ['כל', 'המצוה', 'אשר', 'אנכי', 'מצוך', 'היום'] and SHARED(('Deut', 8, 2), ('Deut', 29, 4)) == ['ארבעים', 'שנה', 'במדבר'] and SHARED(('Deut', 8, 2), ('Exod', 16, 4)) == ['אם', 'לא']
assert SHARED(('Deut', 8, 3), ('Exod', 16, 15)) == ['כי', 'לא'] and SHARED(('Deut', 8, 3), ('Deut', 8, 16)) == ['ידעון', 'אבתיך', 'למען'] and SHARED(('Deut', 8, 4), ('Deut', 29, 4)) == ['לא', 'בלתה'] and SHARED(('Deut', 8, 5), ('Deut', 1, 31)) == ['איש', 'את', 'בנו']
assert SHARED(('Deut', 8, 6), ('Deut', 28, 9)) == ['את', 'מצות', 'יהוה', 'אלהיך'] and SHARED(('Deut', 8, 6), ('Deut', 30, 16)) == ['יהוה', 'אלהיך', 'ללכת', 'בדרכיו'] and SHARED(('Deut', 8, 7), ('Exod', 3, 8)) == ['אל', 'ארץ', 'טובה'] and SHARED(('Deut', 8, 7), ('Deut', 10, 7)) == ['ארץ', 'נחלי', 'מים']
assert SHARED(('Deut', 8, 8), ('2Kgs', 18, 32)) == ['ארץ', 'זית'] and SHARED(('Deut', 8, 10), ('Deut', 6, 11)) == ['ואכלת', 'ושבעת'] and SHARED(('Deut', 8, 10), ('Deut', 11, 15)) == ['ואכלת', 'ושבעת'] and SHARED(('Deut', 8, 11), ('Deut', 6, 12)) == ['השמר', 'לך', 'פן', 'תשכח', 'את', 'יהוה']
assert SHARED(('Deut', 8, 11), ('Deut', 12, 13)) == ['השמר', 'לך', 'פן'] and SHARED(('Deut', 8, 11), ('Deut', 15, 9)) == ['השמר', 'לך', 'פן'] and SHARED(('Deut', 8, 11), ('Deut', 8, 1)) == ['אשר', 'אנכי', 'מצוך', 'היום'] and SHARED(('Deut', 8, 13), ('Deut', 17, 17)) == ['וכסף', 'וזהב']
assert SHARED(('Deut', 8, 14), ('Deut', 6, 12)) == ['מארץ', 'מצרים', 'מבית', 'עבדים'] and SHARED(('Deut', 8, 14), ('Deut', 5, 6)) == ['מארץ', 'מצרים', 'מבית', 'עבדים'] and SHARED(('Deut', 8, 14), ('Deut', 13, 11)) == ['יהוה', 'אלהיך', 'המוציאך', 'מארץ', 'מצרים', 'מבית', 'עבדים']
assert SHARED(('Deut', 8, 15), ('Deut', 1, 19)) == ['והנורא'] and SHARED(('Deut', 8, 15), ('Exod', 17, 6)) == ['מים'] and SHARED(('Deut', 8, 16), ('Exod', 16, 35)) == [] and SHARED(('Deut', 8, 17), ('Deut', 7, 17)) == ['בלבבך'] and SHARED(('Deut', 8, 17), ('Judg', 7, 2)) == ['ידי']
assert SHARED(('Deut', 8, 18), ('Deut', 7, 12)) == ['אשר', 'נשבע', 'לאבתיך'] and SHARED(('Deut', 8, 18), ('Deut', 8, 1)) == ['אשר', 'נשבע'] and SHARED(('Deut', 8, 19), ('Deut', 4, 26)) == ['כי', 'אבד', 'תאבדון'] and SHARED(('Deut', 8, 19), ('Deut', 30, 18)) == ['היום', 'כי', 'אבד', 'תאבדון']
assert SHARED(('Deut', 8, 19), ('Deut', 6, 14)) == ['אחרי', 'אלהים', 'אחרים'] and SHARED(('Deut', 8, 19), ('Deut', 11, 16)) == ['אלהים', 'אחרים'] and SHARED(('Deut', 8, 19), ('Deut', 8, 11)) == ['תשכח', 'את', 'יהוה', 'אלהיך'] and SHARED(('Deut', 8, 20), ('Deut', 28, 45)) == ['בקול', 'יהוה']
assert SHARED(('Deut', 8, 20), ('Gen', 22, 18)) == ['אשר'] and SHARED(('Deut', 8, 20), ('Exod', 19, 5)) == [] and SHARED(('Deut', 8, 20), ('Deut', 4, 26)) == ['אשר'] and SHARED(('Deut', 8, 20), ('Deut', 8, 19)) == ['יהוה'] and DIFF(('Deut', 8, 3), ('Deut', 8, 16))[1] == ('delete', ['ידעת', 'ולא'], [])
# THE PHRASE CENSUSES (the crowns): "all the commandment" eight, all this book's; "which I command you this day" eighteen (8:1, 8:11); "that you may live" 4:1, 5:33, 8:1, 16:20, 30:19
# (the plural with the nun 5:33, 8:1 alone); "and multiply" (the form) ONE; "and go in and possess" 4:1, 8:1, 11:8; "swore" thirty-three seats in the book, the noun "oath" none in
# the chapter (7:8 the noun); "and you shall remember" 5:15, 8:2, 8:18, 15:15, 16:12, 24:18, 24:22 (the slave five times) and two prophets; "all the way" 8:2 (twice — the verse's
# own "all" and "the way") and 2 Kings 7:15; "led you" — the causative at 8:2, 8:15, 29:4, Leviticus 26:13, Joshua 24:3, Amos 2:10; "these forty years" 2:7, 8:2, 8:4; "forty
# years" thirty-one seats (eight in the Torah and the Prophets on the wilderness); "in the wilderness" 8:2, 15, 16 (nine in the book); "to humble you" the verb 8:2, 3, 16 (the
# lemma's seven Deuteronomy seats — the four others the seduced and the ravished, 21:14, 22:24, 29 — and 26:6 the Egyptians' "afflicted us"); "to test you" 8:2, 8:16 — the
# lemma's Torah seats fifteen: the Akedah's, Massah's, the manna's (Exodus 16:4 "that I may test them"), Sinai's (20:20), 4:34's "essayed", 6:16's, 13:4's, 33:8's; "to know what
# is in your heart" ONE; "WHETHER … OR NOT" — the two tokens ending a verse at 8:2, Exodus 16:4 (the manna's test), Genesis 24:21, 27:21, 37:32, Numbers 11:23, Judges 2:22;
# "whether you would keep His commandments" ONE — the book's ONE interrogative he on a verb; "the manna" thirteen seats (Exodus 16 four, Numbers 11 three, 8:3 and 8:16,
# Joshua 5:12 twice, Nehemiah 9:20, Psalm 78:24); "which you did not know" 8:3, 13:7, 28:33, 36, 64 and two others; "nor did your fathers know" 8:3 and 8:16 alone; THE
# PARAGOGIC NUN eight; "NOT BY BREAD ALONE" ONE; "everything that proceeds from the mouth of the LORD" ONE ("what proceeds from" 8:3 and 23:24 in the book — the lips' utterance;
# Numbers 30:13); "man shall live" 8:3 and Ecclesiastes 11:8; "the mouth of the LORD" twenty-five Torah seats (Numbers' "at the mouth of the LORD" the journeys' formula — 8:3 the
# one seat where the mouth's issue is the food); "your clothing did not wear out" 8:4 and Nehemiah 9:21 (29:4 the plural "your clothes"); "did not swell" 8:4 and Nehemiah
# 9:21 — the verb's TWO seats in the Bible; "as a man disciplines his son" ONE — "as a man … his son" 8:5 and 1:31 (the carrying) and 2 Kings 23:10 (Molech); "discipline" the
# lemma's Torah seats eight (Leviticus 26's three, 4:36, 8:5 twice, the rebellious son, the slandered bride); "with your heart" 8:5, 15:9 in the book; "to walk in His ways" 8:6,
# 30:16, 1 Kings 2:3 ("in ALL His ways" 10:12, 11:22, Solomon's); "and to fear Him" ONE; "a good land" twelve seats (1:35, 3:25, 4:21-22, 6:18, 8:7, 8:10, 9:6, 11:17, Exodus 3:8,
# Joshua 23:16, Chronicles); "brooks of water" 8:7, 10:7 (Jotbah), Jeremiah 31:9; "springs and deeps" ONE — "deeps" in the Torah 8:7 and the Song of the Sea (Exodus 15:5, 8); "in
# the valley and in the hill" ONE (11:11 "a land of hills and valleys"); "a land of wheat and barley" ONE; "a land of olive oil and honey" ONE; THE SEVEN SPECIES — the verse
# holding all seven lemmas is 8:8 ALONE in the Bible; three or more at Numbers 20:5, Haggai 2:19 (four), Joel 1:12, Habakkuk 3:17, Jeremiah 41:8; "milk" absent from the chapter
# ("flowing with milk and honey" twenty seats, six this book's — 8:8 says HONEY without milk: the fruit's, not the herd's); "in poverty" the lemma's ONE seat; "you shall not lack
# anything" ONE (2:7 "you lacked nothing"); "lack" the lemma's Torah seats seven; "whose stones are iron" ONE; "iron" eight Deuteronomy seats (Og's bed, the furnace, 8:9, the
# axe, the altar, the sky, the yoke, the bars), "copper" three (8:9, 28:23, 33:25); "hew" 6:11 twice (the cisterns) and 8:9 — the Torah's three; "AND YOU SHALL EAT AND BE
# SATISFIED AND BLESS" ONE; "eat and be satisfied" 6:11, 8:10, 8:12, 11:15, 14:29, 31:20; "and you shall bless the LORD" ONE — the Torah's one command to bless Him; "the good
# land which He has given you" ONE; "which He has given you" five in the book; "take heed to yourself lest" nine (Genesis 24:6, 31:24, Exodus 34:12; 6:12, 8:11, 12:13, 12:19,
# 12:30, 15:9); "take heed" the niphal imperative seventeen Torah seats (nine singular in the book); "lest you forget the LORD" 6:12 and 8:11; "forget the LORD" 6:12, 8:11, 8:14,
# 8:19 and three in the Prophets; "forget" fourteen Deuteronomy seats — 8:19's INFINITIVE ABSOLUTE the lemma's ONE such form in the Bible; "His commandments, His judgments and
# His statutes" ONE in this order — the triads of the three words seventeen verses over the Bible, seven this book's, no two in one order but 5:31/6:1/7:11's; "lest you eat
# and be satisfied" ONE; "good houses you build and dwell" ONE (28:30 "a house you shall build and not dwell in it"); "your herd and your flock" 8:13, 12:17, 14:23; "silver and
# gold" seven Torah seats — 8:13 "SHALL MULTIPLY for you" and 17:17 "he shall NOT multiply" the king's law, the same three tokens; "multiply" twenty seats in the book, 8:13
# three of them; "and your heart be lifted up" ONE (17:20 the king's "that his heart be not lifted up"; Hosea 13:6 "they were filled, their heart was lifted up, therefore they
# forgot Me" — the chapter's sequence in the prophet's mouth); "who brought you out of the land of Egypt, from the house of bondage" 8:14 and 13:11 — "the house of bondage"
# twelve seats (nine in the Torah, all Deuteronomy's but Exodus 13 and 20); "who led you" the participle 8:15 (29:4 "I led you", Amos 2:10); "the great and terrible" 1:19 and
# 8:15 the wilderness (Daniel's, Nehemiah's, Joel's, Malachi's the God and the day); "fiery serpent" 8:15 and Numbers 21:6, 8 (the lemma the burning's); "scorpion" 8:15 and
# Rehoboam's five; "thirsty ground" 8:15, Isaiah 35:7, Psalm 107:33; "where there is no water" 8:15, Exodus 17:1, Numbers 21:5 and two prophets; "flint" five seats (8:15, 32:13,
# Isaiah 50:7, Job 28:9, Psalm 114:8); "the rock" with water — Exodus' tzur (17:6) and Numbers' sela (20:8-11): 8:15 the tzur, the flint's; "who fed you manna in the wilderness"
# ONE; "to do you good in your end" ONE — "end" the lemma's Torah seats ten (Jacob's, Balaam's three, 4:30, 8:16, 11:12, 31:29, 32:20, 32:29); "and you say in your heart" 8:17 and
# Isaiah 49:21 (7:17 "if you say", 9:4 "do not say"); "my power and the might of my hand" ONE; "has gotten me this wealth" ONE — "wealth/might/army" five Deuteronomy seats;
# "power" the lemma's thirteen Torah seats (8:17, 18); "for it is He who gives you power to get wealth" ONE — "to get wealth" 8:18, Numbers 24:18, the Psalms' "does valiantly";
# "that He may establish His covenant" ONE — "establish" with "covenant" twenty-three seats (Noah's four, Abraham's three, Exodus 6:4, Leviticus 26:9, 8:18, 31:16, Ezekiel's two);
# "as at this day" six in the book, twenty-one over the Bible; "and it shall be, if you surely forget" ONE; "and go after other gods" ONE — "after other gods" sixteen seats;
# "other gods" seventeen Deuteronomy seats; "and serve them and bow down to them" ONE — the two verbs together ten Torah seats, serve-then-bow at 8:19, 11:16, 17:3, 29:25 and
# bow-then-serve at 4:19, 30:17 and the ten words; "I testify against you this day" ONE — the verb's Torah seats ten (4:26, 30:19, 31:28, 32:46; Genesis 43:3, Exodus 19:21, 23,
# 21:29); "that you shall surely perish" 4:26, 8:19, 30:18 — THE INFINITIVE ABSOLUTE at those three alone; "like the nations which the LORD makes to perish before you" ONE;
# "so shall you perish" ONE — the measure-for-measure "like … so"; "because" the heel at fifteen seats over the Bible, five in the Torah (7:12, 8:20; Genesis 22:18, 26:5 —
# "because you have hearkened to My voice"; Numbers 14:24 Caleb's); "because you would not hearken" ONE; "hearken to the voice of the LORD your God" ten seats in the book,
# 8:20 the ONE plural; "not hearken to the voice" 8:20, 28:15, 45, 62 and the Prophets.
assert P('כל', 'המצוה') == ['Deut 11:22', 'Deut 11:8', 'Deut 15:5', 'Deut 19:9', 'Deut 27:1', 'Deut 5:31', 'Deut 6:25', 'Deut 8:1'] and len(P('אשר', 'אנכי', 'מצוך', 'היום', books=('Deut',))) == 18 and P('למען', 'תחיון') + P('למען', 'תחיה') + P('למען', 'תחיו') == ['Deut 5:33', 'Deut 8:1', 'Deut 16:20', 'Deut 30:19', 'Amos 5:14', 'Deut 4:1', 'Jer 35:7'] and U('ורביתם') == ['Deut 8:1'] and P('ובאתם', 'וירשתם') == ['Deut 11:8', 'Deut 4:1', 'Deut 8:1']
assert P('אשר', 'נשבע', 'יהוה', 'לאבתיכם') + P('אשר', 'נשבע', 'יהוה', 'לאבתיך') == ['Deut 11:21', 'Deut 11:9', 'Deut 1:8', 'Deut 8:1', 'Deut 28:11', 'Deut 30:20', 'Deut 6:18', 'Deut 9:5'] and len(LEMV('7650', books=('Deut',))) == 33 and [x for x, l in zip(W8(1), byl[('Deut', 8, 1)]) if l == '7621'] == [] and U('וזכרת') == ['1Sam 25:31', 'Deut 15:15', 'Deut 16:12', 'Deut 24:18', 'Deut 24:22', 'Deut 5:15', 'Deut 8:18', 'Deut 8:2', 'Ezek 16:61']
assert P('וזכרת', 'כי', 'עבד', 'היית') == ['Deut 15:15', 'Deut 16:12', 'Deut 24:18', 'Deut 24:22', 'Deut 5:15'] and [(s, x, m) for s, x, m in LEMT('2142', books=('Deut',)) if s.startswith('Deut 8')] == [('Deut 8:2', 'וזכרת', 'HC/Vqq2ms'), ('Deut 8:18', 'וזכרת', 'HC/Vqq2ms')] and P('כל', 'הדרך') == ['2Kgs 7:15', 'Deut 8:2'] and P('את', 'כל', 'הדרך') == ['Deut 8:2'] and U('הליכך', 'הוליכך', 'ואולך', 'המוליכך') == ['Amos 2:10', 'Deut 29:4', 'Deut 8:15', 'Deut 8:2', 'Josh 24:3', 'Lev 26:13']
assert [v for v in range(1, 21) if 'במדבר' in W8(v)] == [2, 15, 16] and len(U('במדבר', books=('Deut',))) == 9 and [(s, x) for s, x, m in LEMT('6031 b', books=('Deut',))] == [('Deut 8:2', 'ענתך'), ('Deut 8:3', 'ויענך'), ('Deut 8:16', 'ענתך'), ('Deut 21:14', 'עניתה'), ('Deut 22:24', 'ענה'), ('Deut 22:29', 'ענה'), ('Deut 26:6', 'ויענונו')]
assert [(s, x) for s, x, m in LEMT('5254', books=T)] == [('Deut 4:34', 'הנסה'), ('Deut 6:16', 'תנסו'), ('Deut 6:16', 'נסיתם'), ('Deut 8:2', 'לנסתך'), ('Deut 8:16', 'נסתך'), ('Deut 13:4', 'מנסה'), ('Deut 28:56', 'נסתה'), ('Deut 33:8', 'נסיתו'), ('Exod 15:25', 'נסהו'), ('Exod 16:4', 'אנסנו'), ('Exod 17:2', 'תנסון'), ('Exod 17:7', 'נסתם'), ('Exod 20:20', 'נסות'), ('Gen 22:1', 'נסה'), ('Num 14:22', 'וינסו')]
assert P('לדעת', 'את', 'אשר', 'בלבבך') == ['Deut 8:2'] and [f'{b} {c}:{v}' for (b, c, v), ws in by.items() if [x for x, _ in ws][-2:] == ['אם', 'לא']] == ['Deut 8:2', 'Exod 16:4', 'Gen 24:21', 'Gen 27:21', 'Gen 37:32', 'Judg 2:22', 'Num 11:23'] and P('התשמר', 'מצותו') == ['Deut 8:2'] and [(s, x) for s, x, m in LEMT('8104', books=('Deut',)) if m and m.startswith('HTi')] == [('Deut 8:2', 'התשמר')]
assert [(s, x) for s, x, m in LEMT('4478 a')] == [('Deut 8:3', 'המן'), ('Deut 8:16', 'מן'), ('Exod 16:31', 'מן'), ('Exod 16:33', 'מן'), ('Exod 16:35', 'המן'), ('Exod 16:35', 'המן'), ('Josh 5:12', 'המן'), ('Josh 5:12', 'מן'), ('Neh 9:20', 'ומנך'), ('Num 11:6', 'המן'), ('Num 11:7', 'והמן'), ('Num 11:9', 'המן'), ('Ps 78:24', 'מן')] and P('אשר', 'לא', 'ידעת') == ['Deut 13:7', 'Deut 28:33', 'Deut 28:36', 'Deut 28:64', 'Deut 8:3', 'Jer 17:4', 'Ruth 2:11'] and P('ידעון', 'אבתיך') == ['Deut 8:16', 'Deut 8:3']
assert P('לא', 'על', 'הלחם', 'לבדו') == ['Deut 8:3'] and P('כל', 'מוצא', 'פי', 'יהוה') == ['Deut 8:3'] and [(s, x) for s, x, m in LEMT('4161', books=T)] == [('Deut 8:3', 'מוצא'), ('Deut 23:24', 'מוצא'), ('Num 30:13', 'מוצא'), ('Num 33:2', 'מוצאיהם'), ('Num 33:2', 'למוצאיהם')] and P('יחיה', 'האדם') == ['Deut 8:3', 'Eccl 11:8'] and P('וחי', 'בהם') == ['Ezek 20:11', 'Ezek 20:13', 'Ezek 20:21', 'Lev 18:5'] and len(P('פי', 'יהוה', books=T)) == 25
assert P('שמלתך', 'לא', 'בלתה') + P('שלמתיהם', 'לא', 'בלו') == ['Deut 8:4', 'Neh 9:21'] and [(s, x) for s, x, m in LEMT('1086', books=T)] == [('Deut 8:4', 'בלתה'), ('Deut 29:4', 'בלו'), ('Deut 29:4', 'בלתה'), ('Gen 18:12', 'בלתי')] and [(s, x) for s, x, m in LEMT('1216')] == [('Deut 8:4', 'בצקה'), ('Neh 9:21', 'בצקו')]
assert P('כאשר', 'ייסר', 'איש', 'את', 'בנו') == ['Deut 8:5'] and [(s, x) for s, x, m in LEMT('3256', books=T)] == [('Deut 4:36', 'ליסרך'), ('Deut 8:5', 'ייסר'), ('Deut 8:5', 'מיסרך'), ('Deut 21:18', 'ויסרו'), ('Deut 22:18', 'ויסרו'), ('Lev 26:18', 'ליסרה'), ('Lev 26:23', 'תוסרו'), ('Lev 26:28', 'ויסרתי')] and P('איש', 'את', 'בנו') == ['2Kgs 23:10', 'Deut 1:31', 'Deut 8:5'] and P('עם', 'לבבך', books=('Deut',)) == ['Deut 15:9', 'Deut 8:5']
assert P('ללכת', 'בדרכיו') == ['1Kgs 2:3', 'Deut 30:16', 'Deut 8:6'] and P('ללכת', 'בכל', 'דרכיו') == ['1Kgs 8:58', 'Deut 10:12', 'Deut 11:22'] and P('וליראה', 'אתו') == ['Deut 8:6'] and sorted(set(P('ליראה', 'את', 'יהוה', books=('Deut',)))) == ['Deut 10:12', 'Deut 14:23', 'Deut 17:19', 'Deut 31:13', 'Deut 6:24']
assert sorted(P('ארץ', 'טובה') + P('הארץ', 'הטובה') + P('הארץ', 'הטבה') + P('ארץ', 'טבה')) == ['1Chr 28:8', 'Deut 11:17', 'Deut 1:35', 'Deut 3:25', 'Deut 4:21', 'Deut 4:22', 'Deut 6:18', 'Deut 8:10', 'Deut 8:7', 'Deut 9:6', 'Exod 3:8', 'Josh 23:16'] and P('נחלי', 'מים') == ['Deut 10:7', 'Deut 8:7', 'Jer 31:9'] and P('עינת', 'ותהמת') == ['Deut 8:7'] and U('תהמת', 'ותהמת', books=T) == ['Deut 8:7', 'Exod 15:5', 'Exod 15:8'] and P('בבקעה', 'ובהר') == ['Deut 8:7'] and P('ארץ', 'הרים', 'ובקעת') == ['Deut 11:11']
SPECIES = ('2406', '8184', '1612', '8384', '7416', '2132', '1706')
SPC = Counter(s for lem in SPECIES for s in LEMV(lem))
assert P('ארץ', 'חטה', 'ושערה') == ['Deut 8:8'] and P('ארץ', 'זית', 'שמן', 'ודבש') == ['Deut 8:8'] and [s for s, n in SPC.items() if n >= 7] == ['Deut 8:8'] and sorted((s, n) for s, n in SPC.items() if n >= 3) == [('Deut 8:8', 7), ('Hab 3:17', 3), ('Hag 2:19', 4), ('Jer 41:8', 3), ('Joel 1:12', 3), ('Num 20:5', 3)] and [lemma_of('Deut', 8, 8, x)[0] for x in W8(8)] == ['776', '2406', '8184', '1612', '8384', '7416', '776', '2132', '8081', '1706']
assert len(P('זבת', 'חלב', 'ודבש')) == 20 and [v for v in range(1, 21) if 'חלב' in W8(v)] == [] and len(U('דבש', 'ודבש', 'בדבש', 'מדבש', books=T)) == 20 and [(s, x) for s, x, m in LEMT('4544')] == [('Deut 8:9', 'במסכנת')] and P('לא', 'תחסר', 'כל') == ['Deut 8:9'] and P('לא', 'חסרת', 'דבר') == ['Deut 2:7'] and len(LEMT('2637', books=T)) == 7
assert P('אשר', 'אבניה', 'ברזל') == ['Deut 8:9'] and U('ברזל', 'וברזל', 'הברזל', books=('Deut',)) == ['Deut 19:5', 'Deut 27:5', 'Deut 28:23', 'Deut 28:48', 'Deut 33:25', 'Deut 3:11', 'Deut 4:20', 'Deut 8:9'] and U('נחשת', 'ונחשת', books=('Deut',)) == ['Deut 28:23', 'Deut 33:25', 'Deut 8:9'] and [(s, x) for s, x, m in LEMT('2672', books=T)] == [('Deut 6:11', 'חצובים'), ('Deut 6:11', 'חצבת'), ('Deut 8:9', 'תחצב')]
assert P('ואכלת', 'ושבעת', 'וברכת') == ['Deut 8:10'] and sorted(P('ואכלת', 'ושבעת') + P('תאכל', 'ושבעת') + P('ואכל', 'ושבע') + P('ואכלו', 'ושבעו')) == ['Deut 11:15', 'Deut 14:29', 'Deut 31:20', 'Deut 6:11', 'Deut 8:10', 'Deut 8:12'] and P('וברכת', 'את', 'יהוה') == ['Deut 8:10'] and P('הארץ', 'הטבה', 'אשר', 'נתן', 'לך') == ['Deut 8:10'] and P('אשר', 'נתן', 'לך', books=('Deut',)) == ['Deut 12:15', 'Deut 16:17', 'Deut 26:11', 'Deut 28:53', 'Deut 8:10']
assert P('השמר', 'לך', 'פן') == ['Deut 12:13', 'Deut 12:19', 'Deut 12:30', 'Deut 15:9', 'Deut 6:12', 'Deut 8:11', 'Exod 34:12', 'Gen 24:6', 'Gen 31:24'] and P('השמרו', 'לכם', 'פן') == ['Deut 11:16', 'Deut 4:23'] and len([1 for s, x, m in LEMT('8104', books=T) if m and m.startswith('HVNv')]) == 17 and P('פן', 'תשכח', 'את', 'יהוה') == ['Deut 6:12', 'Deut 8:11']
assert sorted(P('תשכח', 'את', 'יהוה') + P('ושכחת', 'את', 'יהוה') + P('שכחו', 'את', 'יהוה') + P('וישכחו', 'את', 'יהוה')) == ['1Sam 12:9', 'Deut 6:12', 'Deut 8:11', 'Deut 8:14', 'Deut 8:19', 'Jer 3:21', 'Judg 3:7'] and len(LEMT('7911', books=('Deut',))) == 14 and [(s, x) for s, x, m in LEMT('7911') if m == 'HVqa'] == [('Deut 8:19', 'שכח')]
TRIAD = sorted(set(LEMV('4687')) & (set(LEMV('2706')) | set(LEMV('2708'))) & set(LEMV('4941')))
assert P('מצותיו', 'ומשפטיו', 'וחקתיו') == ['Deut 8:11'] and len(TRIAD) == 17 and [s for s in TRIAD if s.startswith('Deut')] == ['Deut 11:1', 'Deut 26:17', 'Deut 30:16', 'Deut 5:31', 'Deut 6:1', 'Deut 7:11', 'Deut 8:11'] and [x for x, l in zip(W8(11), byl[('Deut', 8, 11)]) if l in ('4687', '2706', '2708', '4941')] == ['מצותיו', 'ומשפטיו', 'וחקתיו'] and [x for x, l in zip(words('Deut', 30, 16), byl[('Deut', 30, 16)]) if l in ('4687', '2706', '2708', '4941')] == ['מצותיו', 'וחקתיו', 'ומשפטיו']
assert P('פן', 'תאכל', 'ושבעת') == ['Deut 8:12'] and P('ובתים', 'טובים', 'תבנה', 'וישבת') == ['Deut 8:12'] and P('בית', 'תבנה', 'ולא', 'תשב', 'בו') == ['Deut 28:30'] and P('ובתים', 'מלאים', 'כל', 'טוב') == ['Deut 6:11'] and P('ובקרך', 'וצאנך') + P('בקרך', 'וצאנך') == ['Deut 8:13', 'Deut 12:17', 'Deut 14:23']
assert sorted(P('וכסף', 'וזהב', books=T) + P('כסף', 'וזהב', books=T)) == ['Deut 17:17', 'Deut 29:16', 'Deut 7:25', 'Deut 8:13', 'Gen 24:35', 'Num 22:18', 'Num 24:13'] and P('וכסף', 'וזהב', 'ירבה') + P('וכסף', 'וזהב', 'לא', 'ירבה') == ['Deut 8:13', 'Deut 17:17'] and len(LEMT('7235 a', books=('Deut',))) == 20 and [x for x, l in zip(W8(13), byl[('Deut', 8, 13)]) if l == '7235 a'] == ['ירבין', 'ירבה', 'ירבה'] and P('וכל', 'אשר', 'לך', 'ירבה') == ['Deut 8:13']
assert P('ורם', 'לבבך') == ['Deut 8:14'] and P('לבלתי', 'רום', 'לבבו') == ['Deut 17:20'] and [s for s in LEMV('7311 a') if any(x.startswith(('לבב', 'לבו', 'לבם', 'לבך', 'ולבב', 'ולבו', 'ולבם')) for x in words(*SEAT(s)))] == ['Dan 11:12', 'Dan 12:7', 'Deut 17:20', 'Deut 1:28', 'Deut 8:14', 'Ezek 31:10', 'Hos 13:6', 'Job 17:4'] and P('ושכחת', 'את', 'יהוה', 'אלהיך') == ['Deut 8:14']
assert P('המוציאך', 'מארץ', 'מצרים', 'מבית', 'עבדים') == ['Deut 13:11', 'Deut 8:14'] and P('מבית', 'עבדים') == ['Deut 13:11', 'Deut 13:6', 'Deut 5:6', 'Deut 6:12', 'Deut 7:8', 'Deut 8:14', 'Exod 13:14', 'Exod 13:3', 'Exod 20:2', 'Jer 34:13', 'Josh 24:17', 'Judg 6:8'] and U('המוציאך', 'המוציא', 'המוציאם', 'המוצא', books=T) == ['Deut 13:11', 'Deut 13:6', 'Deut 8:14', 'Deut 8:15', 'Exod 6:7', 'Lev 22:33']
assert U('המוליכך', 'המוליך', 'ואולך', 'מוליך') == ['Amos 2:10', 'Deut 29:4', 'Deut 8:15', 'Isa 63:12', 'Jer 2:6', 'Job 12:17', 'Job 12:19', 'Josh 24:3', 'Lev 26:13'] and sorted(set(P('הגדול', 'והנורא') + P('הגדל', 'והנורא'))) == ['Dan 9:4', 'Deut 1:19', 'Deut 8:15', 'Joel 3:4', 'Mal 3:23', 'Neh 1:5', 'Neh 4:8'] and P('נחש', 'שרף') + P('הנחשים', 'השרפים') == ['Deut 8:15', 'Num 21:6'] and lemma_of('Deut', 8, 15, 'שרף') == ['8314 a'] and lemma_of('Num', 21, 8, 'שרף') == ['8314 a']
assert [(s, x) for s, x, m in LEMT('6137')] == [('1Kgs 12:11', 'בעקרבים'), ('1Kgs 12:14', 'בעקרבים'), ('2Chr 10:11', 'בעקרבים'), ('2Chr 10:14', 'בעקרבים'), ('Deut 8:15', 'ועקרב'), ('Ezek 2:6', 'עקרבים')] and [(s, x) for s, x, m in LEMT('6774')] == [('Deut 8:15', 'וצמאון'), ('Isa 35:7', 'וצמאון'), ('Ps 107:33', 'לצמאון')] and sorted(set(P('אשר', 'אין', 'מים') + P('ואין', 'מים') + P('אין', 'מים'))) == ['Deut 8:15', 'Exod 17:1', 'Jer 38:6', 'Num 21:5', 'Zech 9:11']
assert P('המוציא', 'לך', 'מים', 'מצור', 'החלמיש') == ['Deut 8:15'] and [(s, x) for s, x, m in LEMT('2496')] == [('Deut 8:15', 'החלמיש'), ('Deut 32:13', 'מחלמיש'), ('Isa 50:7', 'כחלמיש'), ('Job 28:9', 'בחלמיש'), ('Ps 114:8', 'חלמיש')] and lemma_of('Deut', 8, 15, 'מצור') == ['6697'] and lemma_of('Exod', 17, 6, 'הצור') == ['6697'] and lemma_of('Num', 20, 8, 'הסלע') == ['5553', '5553'] and lemma_of('Num', 20, 11, 'הסלע') == ['5553']
assert P('המאכלך', 'מן', 'במדבר') == ['Deut 8:16'] and P('להיטבך', 'באחריתך') == ['Deut 8:16'] and [(s, x) for s, x, m in LEMT('319', books=T)] == [('Deut 4:30', 'באחרית'), ('Deut 8:16', 'באחריתך'), ('Deut 11:12', 'אחרית'), ('Deut 31:29', 'באחרית'), ('Deut 32:20', 'אחריתם'), ('Deut 32:29', 'לאחריתם'), ('Gen 49:1', 'באחרית'), ('Num 23:10', 'אחריתי'), ('Num 24:14', 'באחרית'), ('Num 24:20', 'ואחריתו')] and len(LEMT('3190', books=('Deut',))) == 19
assert P('ואמרת', 'בלבבך') == ['Deut 8:17', 'Isa 49:21'] and P('כי', 'תאמר', 'בלבבך') == ['Deut 7:17'] and P('אל', 'תאמר', 'בלבבך') == ['Deut 9:4'] and P('כחי', 'ועצם', 'ידי') == ['Deut 8:17'] and P('עשה', 'לי', 'את', 'החיל', 'הזה') == ['Deut 8:17'] and [(s, x) for s, x, m in LEMT('2428', books=('Deut',))] == [('Deut 3:18', 'חיל'), ('Deut 8:17', 'החיל'), ('Deut 8:18', 'חיל'), ('Deut 11:4', 'לחיל'), ('Deut 33:11', 'חילו')] and P('ידי', 'הושיעה', 'לי') == ['Judg 7:2'] and P('בכח', 'ידי', 'עשיתי') == ['Isa 10:13'] and len(LEMT('3581 b', books=T)) == 13
assert P('כי', 'הוא', 'הנתן', 'לך', 'כח', 'לעשות', 'חיל') == ['Deut 8:18'] and sorted(P('לעשות', 'חיל') + P('עשה', 'חיל') + P('יעשה', 'חיל') + P('עשו', 'חיל') + P('נעשה', 'חיל')) == ['Deut 8:18', 'Num 24:18', 'Prov 31:29', 'Ps 108:14', 'Ps 118:15', 'Ps 118:16', 'Ps 60:14'] and P('למען', 'הקים', 'את', 'בריתו') == ['Deut 8:18'] and len([s for s in LEMV('6965 b') if s in LEMV('1285')]) == 23 and P('אשר', 'נשבע', 'לאבתיך') == ['Deut 6:10', 'Deut 7:12', 'Deut 7:13', 'Deut 8:18', 'Exod 13:5'] and P('כיום', 'הזה', books=('Deut',)) == ['Deut 10:15', 'Deut 29:27', 'Deut 2:30', 'Deut 4:20', 'Deut 4:38', 'Deut 8:18'] and len(P('כיום', 'הזה')) == 21
assert P('והיה', 'אם', 'שכח', 'תשכח') == ['Deut 8:19'] and P('והלכת', 'אחרי', 'אלהים', 'אחרים') == ['Deut 8:19'] and len(P('אחרי', 'אלהים', 'אחרים')) == 16 and len(P('אלהים', 'אחרים', books=('Deut',))) == 17 and P('ועבדתם', 'והשתחוית', 'להם') == ['Deut 8:19']
BOWSERVE = [(s, [x for x, l in zip(words(*SEAT(s)), byl[SEAT(s)]) if l in ('5647', '7812')]) for s in sorted(set(LEMV('5647', books=T)) & set(LEMV('7812', books=T)))]
assert BOWSERVE == [('Deut 11:16', ['ועבדתם', 'והשתחויתם']), ('Deut 17:3', ['ויעבד', 'וישתחו']), ('Deut 29:25', ['ויעבדו', 'וישתחוו']), ('Deut 30:17', ['והשתחוית', 'ועבדתם']), ('Deut 4:19', ['והשתחוית', 'ועבדתם']), ('Deut 5:9', ['תשתחוה', 'תעבדם']), ('Deut 8:19', ['ועבדתם', 'והשתחוית']), ('Exod 20:5', ['תשתחוה', 'תעבדם']), ('Exod 23:24', ['תשתחוה', 'תעבדם']), ('Gen 27:29', ['יעבדוך', 'וישתחו', 'וישתחוו'])], BOWSERVE
assert P('העדתי', 'בכם', 'היום') == ['Deut 8:19'] and [(s, x) for s, x, m in LEMT('5749 b', books=T)] == [('Deut 4:26', 'העידתי'), ('Deut 8:19', 'העדתי'), ('Deut 30:19', 'העידתי'), ('Deut 31:28', 'ואעידה'), ('Deut 32:46', 'מעיד'), ('Exod 19:21', 'העד'), ('Exod 19:23', 'העדתה'), ('Exod 21:29', 'והועד'), ('Gen 43:3', 'העד'), ('Gen 43:3', 'העד')] and P('כי', 'אבד', 'תאבדון') == ['Deut 30:18', 'Deut 4:26', 'Deut 8:19'] and [(s, x) for s, x, m in LEMT('6') if m == 'HVqa'] == [('Deut 4:26', 'אבד'), ('Deut 8:19', 'אבד'), ('Deut 30:18', 'אבד')] and lemma_of('Deut', 12, 2, 'אבד') == ['6'] and morphs('Deut', 12, 2)[0] == 'HVpa'
assert P('כגוים', 'אשר', 'יהוה', 'מאביד', 'מפניכם') == ['Deut 8:20'] and P('כן', 'תאבדון') == ['Deut 8:20'] and [(s, m) for s, x, m in LEMT('6118') if s.startswith(('Deut', 'Gen', 'Num'))] == [('Deut 7:12', 'HNcmsc'), ('Deut 8:20', 'HNcmsc'), ('Gen 22:18', 'HNcmsa'), ('Gen 26:5', 'HNcmsa'), ('Num 14:24', 'HC')] and len(LEMT('6118')) == 15 and P('עקב', 'לא', 'תשמעון') == ['Deut 8:20'] and P('עקב', 'אשר', 'שמעת', 'בקלי') + P('עקב', 'אשר', 'שמע', 'אברהם', 'בקלי') == ['Gen 22:18', 'Gen 26:5']
assert P('בקול', 'יהוה', 'אלהיך', books=('Deut',)) + P('בקול', 'יהוה', 'אלהיכם', books=('Deut',)) == ['Deut 13:19', 'Deut 15:5', 'Deut 27:10', 'Deut 28:1', 'Deut 28:15', 'Deut 28:2', 'Deut 28:45', 'Deut 28:62', 'Deut 30:10', 'Deut 8:20'] and sorted(set(P('לא', 'תשמעון', 'בקול') + P('לא', 'תשמע', 'בקול') + P('לא', 'שמעת', 'בקול', books=('Deut',)))) == ['Deut 28:15', 'Deut 28:45', 'Deut 28:62', 'Deut 8:20']
# ONKELOS CHAPTER 8 — THE RENDERINGS' SEATS over the whole book (computed on the plain Aramaic of every export row; the export's chapter 8 = the DB's): 8:1 "the commandment" the
# book's word (thirteen), "swore" MADE "ESTABLISHED" (twenty-two — the oath's verb the covenant's word, as at 7:8), "that you may live" (4:1, 5:30, 8:1); 8:2 "led you" ONE,
# "these forty years" (2:7, 8:2, 8:4), "to humble you … to test you" (8:2, 8:16 — the doublet kept); 8:3 THE MEMRA — "not by bread alone is man SUSTAINED, but by everything that
# PROCEEDS FROM THE WORD (MEMRA) OF THE LORD is man sustained" (the sustaining verb 8:3 twice, 18:22, 19:15, 32:12; "the Memra of the LORD" twenty-four seats over the book —
# 8:3 and 8:20 the chapter's two), "the manna" (1:1, 8:3, 8:16 — Onkelos names it at 1:1's Di-zahab); 8:4 "your foot did not swell" MADE "YOUR SHOES DID NOT GO BARE" (the shoe-word
# 8:4, 29:4 — the Aramaic reads the shoe where the Hebrew reads the foot); 8:5 "disciplines" MADE "TEACHES" (4:1's teaching-word: "as a man teaches his son, the LORD your God
# teaches you"); 8:6 "to walk in His ways" MADE "in the ways that are RIGHT BEFORE HIM" (the supplement at five seats — 8:6, 19:9, 26:17, 28:9, 30:16); 8:7 "brooks of water" MADE
# "flowing brooks of water", "springs and deeps" MADE "fountains of springs and deeps" (one each); 8:8 the seven species in the PLURAL, "a land of olive oil and honey" MADE "a land
# WHOSE OLIVES MAKE OIL AND WHICH MAKES HONEY" (the two supplements — the English's brackets "yeilding oil", "producing"); 8:9 "in poverty" MADE "in straits" (one), "lack
# anything" MADE "lack any thing" (the word nine seats); 8:10 "and bless" the same verb (one seat of the form); 8:11 THE FEAR SUPPLIED — "lest you forget THE FEAR of the LORD your
# God" (8:11, 8:14, 8:19 — the three seats of the chapter's forgetting, all given the fear; the fear-word twelve seats over the book, the English's bracket "[the fear of]" thrice);
# 8:12 "good houses" MADE "BEAUTIFUL houses" (one); 8:13 "silver and gold" (8:13, 17:17 — the pair the king's law shares); 8:14 "your heart be lifted up" (one); 8:15 "the
# great and terrible wilderness" (1:19, 7:21, 8:15, 10:17, 28:58 — the terrible word), "serpent, fiery serpent and scorpion" MADE "A PLACE OF serpents, burning ones, and
# scorpions" (the place-word supplied twice — 8:15's "a place where there is no water"; 32:10's the same), "thirsty ground" MADE "a house of thirst" (8:15, 32:10), "the rock
# of flint" MADE "THE MIGHTY ROCK" (the flint made strength); 8:16 "in your end" MADE "in your end" (one), "to do you good" (8:16, 28:63); 8:17 "wealth" MADE "POSSESSIONS" (8:17,
# 8:18, 32:15 — Jeshurun's fat); 8:18 THE COUNSEL — "He gives you COUNSEL to acquire possessions" (power made counsel; the counsel-word 8:18 and 32:28), "to establish His covenant
# which He established" the covenant's word twice; 8:19 "if you surely forget" doubled as in the ink (one), "other gods" MADE "THE IDOLS OF THE PEOPLES" (eighteen), "I testify
# against you today" (4:26, 8:19, 30:19), "surely perish" (4:26, 8:19, 30:18); 8:20 "because" MADE "IN EXCHANGE FOR" (eight — 7:12's word), "hearken to the voice" MADE "ACCEPT
# THE MEMRA" (1:32, 8:20, 28:15, 30:8, 30:10 the "in the Memra" form; thirteen with the "to the Memra" form); no parenthesised variant in the chapter's Hebrew rows (the book's ten
# elsewhere); the English's sixteen bracketed supplements over seven verses, eight of them at 8:15; the English keeps "mon" (8:3, 8:16) and "mitzvah" (8:1).
assert onk_tok('תפקדתא') == [(5, 28), (6, 1), (6, 25), (7, 11), (8, 1), (11, 8), (11, 22), (15, 5), (17, 20), (19, 9), (27, 1), (30, 11), (31, 5)] and len(onk_tok('קיים')) == 22 and (8, 1) in onk_tok('קיים') and (8, 18) in onk_tok('קיים') and onk_tok('דתיחון') == [(4, 1), (5, 30), (8, 1)] and onk_tok('דברך') == [(8, 2)] and onk_tok('דנן') == [(2, 7), (8, 2), (8, 4)]
assert onk_tok('לעניותך') == [(8, 2), (8, 16)] and onk_tok('לנסיותך') == [(8, 2), (8, 16)] and onk_tok('התטר') == [(8, 2)] and onk_seats('התטר פקודוהי אם לא') == [(8, 2)] and onk_tok('מנא') == [(1, 1), (8, 3), (8, 16)] and onk_tok('מתקים') == [(8, 3)] and onk_tok('יתקים') == [(8, 3), (18, 22), (19, 15), (32, 12)] and onk_seats('אפקות מימרא דיי') == [(8, 3)]
assert onk_seats('מימרא דיי') == [(1, 26), (1, 32), (1, 43), (2, 7), (4, 33), (5, 5), (5, 22), (5, 23), (8, 3), (8, 20), (9, 23), (13, 19), (15, 5), (18, 16), (26, 14), (27, 10), (28, 1), (28, 2), (28, 15), (28, 45), (28, 62), (30, 8), (30, 10), (34, 5)] and len(aramaic(8, 3)) == 28 and len(W8(3)) == 28
assert onk_tok('ומסנך') == [(8, 4), (29, 4)] and onk_tok('יחפו') == [(8, 4)] and onk_seats('ומסנך לא יחפו') == [(8, 4)] and onk_tok('מאלף') == [(4, 1), (8, 5)] and onk_seats('מאלף גברא ית בריה') == [(8, 5)] and onk_seats('בארחן דתקנן קדמוהי') == [(8, 6), (19, 9), (26, 17), (28, 9), (30, 16)] and onk_tok('ולמדחל') == [(8, 6)]
assert onk_seats('נגדא נחלין דמיין') == [(8, 7)] and onk_seats('מבועי עינין ותהומין') == [(8, 7)] and onk_tok('חטין') == [(8, 8)] and onk_seats('דזיתהא עבדין משחא') == [(8, 8)] and onk_seats('והיא עבדא דבש') == [(8, 8)] and onk_tok('בעצורין') == [(8, 9)] and onk_seats('לא תחסר כל מדעם') == [(8, 9)] and len(onk_tok('מדעם')) == 9 and onk_tok('ותברך') == [(8, 10)]
assert onk_seats('ית דחלתא דיי אלהך') == [(8, 11), (8, 14), (8, 19)] and onk_seats('דחלתא דיי') == [(1, 36), (4, 4), (4, 29), (4, 30), (8, 11), (8, 14), (8, 19), (13, 5), (13, 11), (18, 13), (29, 17), (30, 2)] and onk_seats('אסתמר לך דילמא') == [(6, 12), (8, 11), (12, 13), (12, 19), (12, 30), (15, 9)] and onk_tok('שפירין') == [(8, 12)]
assert onk_tok('וכספא') == [(8, 13), (17, 17)] and onk_tok('ודהבא') == [(7, 25), (8, 13), (17, 17), (29, 16)] and onk_seats('וירים לבך') == [(8, 14)] and onk_seats('מבית עבדותא') == [(5, 6), (6, 12), (7, 8), (8, 14), (13, 6), (13, 11)] and onk_tok('ודחילא') == [(1, 19), (7, 21), (8, 15), (10, 17), (28, 58)]
assert onk_seats('אתר חיון קלן ועקרבין') == [(8, 15)] and onk_tok('אתר') == [(1, 33), (8, 15), (32, 10)] and onk_seats('ובית צחונא') == [(8, 15), (32, 10)] and onk_seats('אתר די לית מיא') == [(8, 15), (32, 10)] and onk_seats('מטנרא תקיפא') == [(8, 15)] and onk_tok('בסופך') == [(8, 16)] and onk_tok('לאוטבא') == [(8, 16), (28, 63)]
assert onk_seats('קנו לי ית נכסיא') == [(8, 17)] and onk_tok('נכסין') == [(8, 18), (32, 15)] and onk_tok('עצה') == [(8, 18), (32, 28)] and onk_seats('יהב לך עצה למקני נכסין') == [(8, 18)] and onk_seats('לקימא ית קימיה די קיים') == [(8, 18)] and onk_seats('כיומא הדין') == [(2, 30), (4, 20), (4, 38), (6, 24), (8, 18), (10, 15), (29, 27)]
assert onk_seats('מנשאה תנשי') == [(8, 19)] and onk_seats('בתר טעות עממיא') == [(6, 14), (8, 19), (11, 28), (13, 3), (28, 14), (31, 20)] and len(onk_seats('טעות עממיא')) == 18 and onk_seats('אסהדית בכון יומא דין') == [(4, 26), (8, 19), (30, 19)] and onk_seats('מיבד תיבדון') == [(4, 26), (8, 19), (30, 18)]
assert onk_tok('חלף') == [(1, 36), (7, 12), (8, 20), (19, 21), (21, 14), (22, 29), (28, 47), (28, 62)] and onk_seats('חלף דלא קבלתון') == [(8, 20)] and onk_seats('במימרא דיי') == [(1, 32), (8, 20), (28, 15), (30, 8), (30, 10)] and len(onk_seats('במימרא דיי') + onk_seats('למימרא דיי')) == 13
assert [(v + 1) for v in range(len(onk_he[7])) if '(' in clean(onk_he[7][v])] == [] and len([(c + 1, v + 1) for c in range(34) for v in range(len(onk_he[c])) if '(' in clean(onk_he[c][v])]) == 10
BR = {e: re.findall(r'\[([^\]]+)\]', clean(onk[7][e - 1])) for e in range(1, 21)}
BR = {e: b for e, b in BR.items() if b}
assert BR == {8: ['yeilding oil', 'producing'], 11: ['the fear of'], 12: ['beautiful', 'in them.'], 14: ['the fear of'], 15: ['one', 'a place of', 's', 's', 's', 'ing', 'a place', 'mighty'], 19: ['the fear of'], 20: ['the word of']}, BR
assert sum(len(b) for b in BR.values()) == 16 and 'mon' in clean(onk[7][2]) and 'mon' in clean(onk[7][15]) and 'mitzvah' in clean(onk[7][0])
# THE STORE'S GLOSSES at the chapter's seats (words.gloss, read back): the families censused over the whole store (ch8_measure1.py G) — the rewrite planned BY GLOSS where every
# token of the gloss is the one word (or one family read the same at every seat), BY REFERENCE where the family is mixed; applied at the display step, asserted here as the plan.
assert sg(8, 1, 'אנכי') == '?' and sg(8, 1, 'תשמרון') == 'keep/guard-suffix' and sg(8, 1, 'תחיון') == 'live-suffix' and sg(8, 1, 'ורביתם') == 'and-multiply' and sg(8, 1, 'נשבע') == 'swear' and sg(8, 2, 'וזכרת') == 'and-mark' and sg(8, 2, 'הליכך') == 'go-you/your' and sg(8, 2, 'במדבר') == 'in-pasture' and sg(8, 2, 'ענתך') == 'depress-literally-you/your'
assert sg(8, 2, 'לנסתך') == 'to-test-you/your' and sg(8, 2, 'התשמר') == 'the-keep/guard' and sg(8, 2, 'מצותו') == 'commandment-him/its' and sg(8, 2, 'מצותיו') == 'commandment-him/its' and sg(8, 3, 'ויענך') == 'and-depress-literally-you/your' and sg(8, 3, 'וירעבך') == 'and-hunger-you/your' and sg(8, 3, 'ויאכלך') == 'and-eat-you/your' and sg(8, 3, 'המן') == 'the-whatness'
assert sg(8, 3, 'לבדו') == 'to-separation-him/its' and sg(8, 3, 'מוצא') == 'going-forth' and sg(8, 3, 'האדם') == 'the-human' and sg(8, 4, 'שמלתך') == 'dress-you/your' and sg(8, 4, 'בלתה') == 'fail' and sg(8, 4, 'בצקה') == 'perhaps-to-swell-up' and sg(8, 5, 'ייסר') == 'chastise' and sg(8, 5, 'מיסרך') == 'chastise-you/your'
assert sg(8, 7, 'מביאך') == 'come/bring-you/your' and sg(8, 7, 'נחלי') == 'stream' and sg(8, 7, 'עינת') == 'eye' and sg(8, 7, 'ותהמת') == 'and-deep' and sg(8, 7, 'יצאים') == 'bring-forth' and sg(8, 7, 'בבקעה') == 'in-split' and sg(8, 9, 'במסכנת') == 'in-indigence' and sg(8, 9, 'תחצב') == 'cut' and sg(8, 10, 'ושבעת') == 'and-sate' and sg(8, 10, 'נתן') == 'set'
assert sg(8, 11, 'השמר') == 'keep/guard' and sg(8, 11, 'תשכח') == 'mislay' and sg(8, 11, 'לבלתי') == 'to-failure-of' and sg(8, 11, 'אנכי') == '?' and sg(8, 12, 'ושבעת') == 'and-sate' and sg(8, 13, 'ירבין') == 'multiply-suffix' and sg(8, 14, 'ורם') == 'and-be-high-actively' and sg(8, 14, 'ושכחת') == 'and-mislay' and sg(8, 14, 'המוציאך') == 'the-bring-forth-you/your' and sg(8, 14, 'עבדים') == 'servant'
assert sg(8, 15, 'המוליכך') == 'the-go-you/your' and sg(8, 15, 'והנורא') == 'and-the-fear' and sg(8, 15, 'שרף') == 'burning' and sg(8, 15, 'וצמאון') == 'and-thirsty-place' and sg(8, 15, 'המוציא') == 'the-bring-forth' and sg(8, 15, 'מצור') == 'from-cliff' and sg(8, 16, 'המאכלך') == 'the-eat-you/your' and sg(8, 16, 'מן') == 'whatness' and sg(8, 16, 'להיטבך') == 'to-be--make-well-you/your' and sg(8, 16, 'באחריתך') == 'in-last-you/your'
assert sg(8, 17, 'כחי') == 'vigor-me/my' and sg(8, 17, 'ועצם') == 'and-power' and sg(8, 17, 'החיל') == 'the-force' and sg(8, 18, 'הנתן') == 'the-set' and sg(8, 18, 'כח') == 'vigor' and sg(8, 18, 'חיל') == 'force' and sg(8, 18, 'הקים') == 'arise' and sg(8, 19, 'שכח') == 'mislay' and sg(8, 19, 'אחרי') == 'hind-part' and sg(8, 19, 'אחרים') == 'hinder' and sg(8, 19, 'והשתחוית') == 'and-depress' and sg(8, 19, 'העדתי') == 'duplicate' and sg(8, 19, 'אבד') == 'wander-away' and sg(8, 19, 'תאבדון') == 'wander-away-suffix'
assert sg(8, 20, 'כגוים') == 'like-nation' and sg(8, 20, 'מאביד') == 'wander-away' and sg(8, 20, 'עקב') == 'heel' and sg(8, 20, 'תשמעון') == 'hear-suffix' and sg(8, 3, 'ידעון') == 'know-suffix'
GLOSS_FAMILY = {'and-mark': [('וזכרת', 7), ('ויזכר', 5), ('וזכרתי', 3), ('ואזכר', 1), ('וזכרתם', 1), ('ונזכרתם', 1)], 'depress-literally-you/your': [('ענתך', 2)], 'and-depress-literally-you/your': [('ויענך', 1)], 'and-hunger-you/your': [('וירעבך', 1)], 'and-eat-you/your': [('ויאכלך', 1)], 'the-whatness': [('המן', 5)], 'whatness': [('מן', 4)], 'to-separation-him/its': [('לבדו', 12)], 'going-forth': [('מוצא', 3)], 'dress-you/your': [('שמלתך', 1)], 'fail': [('בלתה', 2), ('בלו', 1)], 'perhaps-to-swell-up': [('בצקה', 1)], 'in-split': [('בבקעה', 1)], 'in-indigence': [('במסכנת', 1)], 'the-set': [('הנתן', 2)], 'and-mislay': [('ושכחת', 2), ('ונשכח', 1), ('ושכח', 1), ('ותשכח', 1)], 'the-bring-forth-you/your': [('המוציאך', 2)], 'the-go-you/your': [('המוליכך', 1)], 'burning': [('שרף', 2)], 'and-thirsty-place': [('וצמאון', 1)], 'from-cliff': [('מצור', 1)], 'the-eat-you/your': [('המאכלך', 1)], 'to-be--make-well-you/your': [('להיטבך', 1)], 'in-last-you/your': [('באחריתך', 1)], 'vigor-me/my': [('כחי', 4)], 'and-power': [('ועצם', 1)], 'and-depress': [('וישתחו', 15), ('וישתחוו', 12), ('והשתחוית', 4), ('והשתחוו', 2), ('והשתחויתם', 2), ('ותשתחוין', 2), ('ואשתחוה', 1), ('ונשתחוה', 1)], 'duplicate': [('העד', 3), ('העידתי', 2), ('העדתה', 1), ('העדתי', 1), ('מעיד', 1)], 'wander-away': [('אבד', 8), ('אבדנו', 2), ('אבדה', 1), ('אבדת', 1), ('מאביד', 1), ('תאבד', 1), ('תאבדו', 1)], 'like-nation': [('כגוים', 1)], 'know-suffix': [('ידעון', 2), ('תדעון', 2)], 'hear-suffix': [('ישמעון', 4), ('תשמעון', 4)]}
GT = {g: store.execute("SELECT REPLACE(w.he_plain,'/',''), COUNT(*) FROM words w WHERE w.gloss=? GROUP BY 1 ORDER BY 2 DESC, 1", (g,)).fetchall() for g in GLOSS_FAMILY}
assert all(sorted(GT[g]) == sorted(v) for g, v in GLOSS_FAMILY.items()), [g for g, v in GLOSS_FAMILY.items() if sorted(GT[g]) != sorted(v)]
# BY GLOSS — every token of the gloss the one word (or one family read the same at every seat): the rewrite covers the whole store (THIRTY-TWO)
OVERRIDE_GLOSS = [('and-mark', 'and-remember'), ('depress-literally-you/your', 'to-humble-you'), ('and-depress-literally-you/your', 'and-he-humbled-you'), ('and-hunger-you/your', 'and-let-you-hunger'), ('and-eat-you/your', 'and-fed-you'), ('the-whatness', 'the-manna'), ('whatness', 'manna'), ('to-separation-him/its', 'alone'), ('going-forth', 'what-proceeds-from'), ('dress-you/your', 'your-garment'), ('fail', 'wore-out'), ('perhaps-to-swell-up', 'swelled'), ('in-split', 'in-the-valley'), ('in-indigence', 'in-poverty'), ('the-set', 'who-gives'), ('and-mislay', 'and-forget'), ('the-bring-forth-you/your', 'who-brought-you-out'), ('the-go-you/your', 'who-led-you'), ('burning', 'fiery-serpent'), ('and-thirsty-place', 'and-drought'), ('from-cliff', 'from-the-rock'), ('the-eat-you/your', 'who-fed-you'), ('to-be--make-well-you/your', 'to-do-you-good'), ('in-last-you/your', 'in-your-end'), ('vigor-me/my', 'my-power'), ('and-power', 'and-the-might-of'), ('and-depress', 'and-bow-down'), ('duplicate', 'testify'), ('wander-away', 'perish'), ('like-nation', 'like-the-nations'), ('know-suffix', 'know'), ('hear-suffix', 'hear')]
# BY REFERENCE — the family mixed (a homograph, two persons, a participle beside a finite verb): the seat named (TWENTY)
OVERRIDE_REF_SPEC = [(1, 'אנכי', 'I', 0), (11, 'אנכי', 'I', 0), (2, 'הליכך', 'led-you', 0), (2, 'התשמר', 'will-you-keep', 0), (7, 'מביאך', 'is-bringing-you', 0), (7, 'נחלי', 'brooks-of', 0), (7, 'עינת', 'springs', 0), (7, 'ותהמת', 'and-deeps', 0), (7, 'יצאים', 'flowing-out', 0), (9, 'תחצב', 'you-shall-hew', 0), (10, 'נתן', 'gave', 0), (14, 'ורם', 'and-be-lifted-up', 0), (14, 'עבדים', 'bondage', 0), (15, 'המוציא', 'who-brought-out', 0), (17, 'החיל', 'the-wealth', 0), (18, 'כח', 'power', 0), (18, 'חיל', 'wealth', 0), (18, 'הקים', 'to-establish', 0), (20, 'עקב', 'because', 0), (20, 'מאביד', 'makes-perish', 0)]
OVERRIDE_REF3 = [(f'Deut.8.{v}:{sidx(8, v, tok, nth)}', new, tok) for v, tok, new, nth in OVERRIDE_REF_SPEC]
OVERRIDE_REF = [(k, v) for k, v, _ in OVERRIDE_REF3]
assert len(OVERRIDE_REF) == 20 and len({k for k, _ in OVERRIDE_REF}) == 20 and len(OVERRIDE_GLOSS) == 32 and len({k for k, _ in OVERRIDE_GLOSS}) == 32, (len(OVERRIDE_REF), len(OVERRIDE_GLOSS))
assert all(g in GLOSS_FAMILY for g, _ in OVERRIDE_GLOSS) and all(sg(8, v, tok, nth) is not None for v, tok, _, nth in OVERRIDE_REF_SPEC)
ALREADY = {'in-pasture': 'in-the-wilderness', 'and-sate': 'and-be-satisfied', 'mislay': 'forget', 'to-failure-of': 'so-as-not', 'and-the-fear': 'and-the-terrible', 'hind-part': 'after', 'hinder': 'other', 'wander-away-suffix': 'you-shall-perish', 'keep/guard-suffix': 'keep', 'live-suffix': 'you-may-live', 'multiply-suffix': 'multiply'}   # the rewrites of sittings 1-5 the chapter shares, left standing
OV = open(f'{ROOT}/logic/glosses/word_gloss_overrides.yaml', encoding='utf-8').read()
PATCHED = 'THE DEUTERONOMY WALK sitting 6 (2026-09-18, Deuteronomy 8)' in OV
assert all(f'"{k}": "{v}"' in OV for k, v in ALREADY.items()) and all(f'"{k}": ' not in OV for k, _ in OVERRIDE_GLOSS if not PATCHED) and (PATCHED or '"Deut.8.' not in OV), [k for k, _ in OVERRIDE_GLOSS if f'"{k}": ' in OV]
if PATCHED: assert all(f'"{k}": "{v}"' in OV for k, v in OVERRIDE_REF) and all(f'"{k}": "{v}"' in OV for k, v in OVERRIDE_GLOSS), [k for k, v in OVERRIDE_REF + OVERRIDE_GLOSS if f'"{k}": "{v}"' not in OV][:6]
assert OV.count('  "Deut.7.24:9": "shall-stand"') == 1 and 'THE DEUTERONOMY WALK sitting 5 (2026-09-17, Deuteronomy 7)' in OV

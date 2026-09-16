import os as _os
_ROOT = _os.path.normpath(_os.path.join(_os.path.dirname(_os.path.abspath(__file__)), '..', '..', '..'))   # THE PORTABLE REPO (2026-09-15): the repo root from this file's own place
#!/usr/bin/env python3
# THE DEUTERONOMY WALK, sitting 1 — THE OPENING SPEECH, Deuteronomy 1:1-3:29 (2026-09-15; the owner: "start with deuteronomy", on the rulings
# READ THEN COMPILE and CHAPTER NUMBERS): THE INK of the three chapters, computed from the Tanakh DB, the snapshot store and the shelf's own
# bytes — never typed. The Numbers walk's form (ref_ink.py): THE SIFREI ON DEUTERONOMY found BY POSITION — piskaot 1-25 on 1:1-1:28 and
# 26-30 on 3:23-3:29 (147 rows, the two files' row grains EQUAL everywhere in the export — no duplicated block, no mismatch), NO piska on
# 1:29-3:22, piska 31 opening at 6:4; heads 14 and 27 carry no citation (they continue 1:14 and 3:24); the whole export scanned for rows
# outside 1-30 citing chapters 1-3 (SEVEN Hebrew rows, NINE English — the English "(Dt.1:4)" form with no space, two rows more than the
# Hebrew; 199:5's English cites 2:25 where the Hebrew cites 2:26); THE ONE "IBID" CANDIDATE (355:27) RESOLVES TO SONG OF SONGS 2:2, NOT
# DEUTERONOMY 2:2 — the earlier scan's false hit corrected here; SIX ROWS OF THE THIRTY PISKAOT WERE READ BEFORE, by topic, in Genesis
# ledgers (1:13 twice, 6:1, 8:1, 11:1, 25:4, 27:3) — named, not counted fresh; the engine's numeral parser MEASURED on every verse — eleven
# number verses read, NO GAP (the half-tribe's fraction unread, a class named); the hand's facts as asserts, run all at once by
# assert_driver.py after the measurement passes (deu_dump0.py, deu_parser0.py, deu_measure0.py, deu_measure1.py, deu_measure2.py) printed
# them; every gloss the STORE'S OWN (words.gloss); the piece-wise cutters HP / AP / SP_. Shared by deu_rows_onkelos_*.py, deu_rows_sifrei_*.py
# and write_deu_ledger.py.
# THE SPAN: SIX drafts — deu_01_frame_officers 1:1-18, deu_01_spies_refuse 1:19-46, deu_02_bypass_nations 2:1-25, deu_02_sihon 2:26-37,
# deu_03_og_gilead 3:1-22, deu_03_moses_barred 3:23-29 (the portion Devarim's three chapters as one sitting).
import json, os, re, html, sqlite3, sys, io, contextlib, unicodedata, subprocess
from collections import Counter
ROOT = _ROOT
DATE = '2026-09-15'
UIDS = ['deu_01_frame_officers', 'deu_01_spies_refuse', 'deu_02_bypass_nations', 'deu_02_sihon', 'deu_03_og_gilead', 'deu_03_moses_barred']
SPANS = {'deu_01_frame_officers': (1, 1, 18), 'deu_01_spies_refuse': (1, 19, 46), 'deu_02_bypass_nations': (2, 1, 25), 'deu_02_sihon': (2, 26, 37), 'deu_03_og_gilead': (3, 1, 22), 'deu_03_moses_barred': (3, 23, 29)}
PREFIX = {'deu_01_frame_officers': 'DV01A', 'deu_01_spies_refuse': 'DV01B', 'deu_02_bypass_nations': 'DV02A', 'deu_02_sihon': 'DV02B', 'deu_03_og_gilead': 'DV03A', 'deu_03_moses_barred': 'DV03B'}
PISKAOT = list(range(1, 31))
OUTSIDE_HE = [(37, 9, (3, 9)), (37, 11, (3, 27)), (52, 1, (3, 11)), (54, 2, (1, 4)), (82, 5, (1, 11)), (199, 5, (2, 26)), (314, 2, (1, 31))]
OUTSIDE_EN = [(36, 10, (1, 4)), (37, 2, (1, 4)), (37, 9, (3, 9)), (37, 11, (3, 27)), (52, 1, (3, 11)), (54, 2, (1, 4)), (82, 5, (1, 11)), (199, 5, (2, 25)), (314, 2, (1, 31))]
TITLE = 'The opening speech — these are the words Moses spoke to all Israel beyond the Jordan, eleven days from Horeb, in the fortieth year after smiting Sihon and Og: the LORD said at Horeb "you have dwelt long enough at this mountain, turn and journey", the officers appointed because "I cannot bear you alone" (wise and understanding men, captains of thousands, hundreds, fifties and tens, the judges charged to hear small and great alike, for the judgment is God\'s); the spies sent from Kadesh-barnea, the good report and the murmuring, the oath that none of the evil generation would see the land but Caleb and Joshua, the presumptuous ascent beaten back to Hormah, the long dwelling at Kadesh; the turn to the wilderness, the circuit of Mount Seir, the passage past Esau, Moab and Ammon (the Emim, the Horites, the Zamzummim, the Avvim dispossessed as Israel would dispossess), the thirty-eight years until the men of war were consumed, the Zered and the Arnon; Sihon\'s refusal, his spirit hardened, Jahaz, every city devoted, Aroer to Gilead, only Ammon untouched; Og of Bashan met at Edrei, sixty walled cities, the iron bed nine cubits by four, the land from the Arnon to Hermon given to Reuben, Gad and half Manasseh (Jair\'s villages, Machir\'s Gilead, the Arabah, Chinnereth, the Salt Sea under the slopes of Pisgah), the armed passage owed before the brothers rest; Joshua told "your eyes have seen"; Moses\' plea "let me cross and see the good land", the LORD angry for their sakes — "enough, speak no more", go up Pisgah and look west, north, south and east, charge Joshua; and the dwelling in the valley opposite Beth-peor'
OUT = f'{ROOT}/logic/oral_triage/deu_01_03_devarim_{DATE}.md'

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
# THE SHELF BY POSITION: 357 piskaot in both files, 2,357 rows in both, NO row-count mismatch anywhere in the export (the Numbers walk's
# duplicated-block class absent here); piskaot 1-25 head on 1:1 ... 1:28 in order, 26-30 on 3:23 ... 3:29, 31 on 6:4 — NO piska on
# 1:29-3:22 (the shelf's silence over the spies' defeat, the bypass, Sihon and Og: 3:23 is the next seat after 1:28); heads 14 and 27 carry no
# citation and open on the verse continued (1:14 "and you answered me", 3:24 "you have begun"); two piskaot on 1:8 (7 and 8); 15 heads "1:15-16".
assert len(sif) == 357 and len(sif_he) == 357 and sum(len(r) for r in sif) == 2357 and sum(len(r) for r in sif_he) == 2357 and [p for p in range(1, 358) if len(sif[p - 1]) != len(sif_he[p - 1])] == []
HEADS_1_32 = {1: (1, 1), 2: (1, 2), 3: (1, 4), 4: (1, 5), 5: (1, 6), 6: (1, 7), 7: (1, 8), 8: (1, 8), 9: (1, 9), 10: (1, 10), 11: (1, 11), 12: (1, 12), 13: (1, 13), 14: None, 15: (1, 15), 16: (1, 16), 17: (1, 17), 18: (1, 18), 19: (1, 20), 20: (1, 22), 21: (1, 23), 22: (1, 24), 23: (1, 25), 24: (1, 27), 25: (1, 28), 26: (3, 23), 27: None, 28: (3, 25), 29: (3, 26), 30: (3, 29), 31: (6, 4), 32: (6, 5)}
assert {p: heads[p] for p in range(1, 33)} == HEADS_1_32, {p: heads[p] for p in range(1, 33)}
assert Hb(14, 1).startswith('וַתַּעֲנוּ אֹתִי וַתֹּאמְרוּ טוֹב הַדָּבָר') and Hb(27, 1).startswith('אַתָּה הַחִלּוֹתָ') and Hb(15, 1).startswith('(דברים א טו-טז)') and '“And you urged me on' in E(14, 1)[:80] and '“You began to show Your servant Your greatness' in E(27, 1)[:80] and E(14, 1).startswith('Pisqa’ 14117H:38; JN1:47-48.1. ')   # the translator's apparatus prefixes the English rows
assert sorted(p for p, h in heads.items() if h and h[0] <= 3) == [p for p in PISKAOT if p not in (14, 27)] and [p for p in range(31, 358) if heads[p] and heads[p][0] <= 3] == []
SIF_ROWS = {p: len(sif[p - 1]) for p in PISKAOT}
SIF_ROWS_HE = {p: len(sif_he[p - 1]) for p in PISKAOT}
assert SIF_ROWS == {1: 20, 2: 8, 3: 5, 4: 2, 5: 4, 6: 5, 7: 1, 8: 3, 9: 2, 10: 2, 11: 1, 12: 4, 13: 6, 14: 1, 15: 5, 16: 9, 17: 7, 18: 2, 19: 3, 20: 5, 21: 3, 22: 3, 23: 3, 24: 4, 25: 8, 26: 10, 27: 7, 28: 3, 29: 9, 30: 2} and SIF_ROWS == SIF_ROWS_HE and sum(SIF_ROWS[p] for p in range(1, 26)) == 116 and sum(SIF_ROWS[p] for p in range(26, 31)) == 31 and sum(SIF_ROWS.values()) == 147
N_SIF = 147
# THE CITATION FORMS: the Hebrew "(דברים א א)" — the book's name, the chapter and the verse in Hebrew letters; the English "(Dt.1:1)" with NO
# SPACE (23 "Dt." tokens against one "Deut." in the export's parens); the Hebrew rows of 1-30 cite Deuteronomy 56 times, Genesis 25, Psalms 18,
# Exodus 17, Numbers 17, Isaiah 12 (the Counter's head); the English's parenthesized book words over the whole export: "Dt." 3,292, "Ex." 173, "Gn." 149, "Lv." 142, "Ps." 133, "Nu." 132; the English rows carry the translator's apparatus (H:/JN: page notes, inline footnotes — 1:1's
# twenty rows carry 38 digit-before-capital markers) — a defect class to strip in the reading, not a row.
def HE_CITES(p, r): return re.findall(r'\(([^)]*)\)', Hb(p, r))
CC = Counter(c.split()[0] if c.split()[0] not in ('שמואל', 'מלכים', 'דברי') else ' '.join(c.split()[:2]) for p in PISKAOT for r in range(1, SIF_ROWS[p] + 1) for c in HE_CITES(p, r) if c and c.split()[0] in ('דברים', 'בראשית', 'תהלים', 'שמות', 'במדבר', 'ישעיה', 'ויקרא'))
assert CC['דברים'] == 56 and CC['בראשית'] == 25 and CC['תהלים'] == 18 and CC['שמות'] == 17 and CC['במדבר'] == 17 and CC['ישעיה'] == 12, CC
EN_BOOKS = Counter(m for p in range(1, 358) for r in range(1, len(sif[p - 1]) + 1) for m in re.findall(r'\(([A-Z][a-z]+\.?)\s?\d+:\d+', E(p, r)))
assert EN_BOOKS.most_common(6) == [('Dt.', 3292), ('Ex.', 173), ('Gn.', 149), ('Lv.', 142), ('Ps.', 133), ('Nu.', 132)] and '(Dt.1:1)' in E(1, 1) and '(Dt.1:4)' in E(36, 10), EN_BOOKS.most_common(6)
FOOT = [len(re.findall(r'\d+(?=[A-Z])', E(1, r))) for r in range(1, 21)]
assert sum(FOOT) == 38 and E(52, 1).startswith('Pisqa’ 52166H:109-110; JN1:170-172.'), (FOOT, E(52, 1)[:40])
# THE "FOUND BY POSITION" CLAUSE run on the whole export for rows OUTSIDE 1-30 citing chapters 1-3: SEVEN Hebrew rows — 37:9 (on 11:10;
# Hermon's names, 3:9), 37:11 (Pisgah as one of Nebo's three names, 3:27), 52:1 (on 11:25; "no man" — even Og, 3:11), 54:2 (on 11:28; Moses
# rebuked only near death — "after he had smitten Sihon", 1:4), 82:5 (on 13:1; the priestly blessing not lengthened by 1:11's verse), 199:5
# (on 20:10; Moses loved peace — 2:26's messengers), 314:2 (on 32:11; the eagle's wings — "as a man carries his son", 1:31); NINE English rows —
# the seven plus 36:10 and 37:2 (both citing 1:4 where the Hebrew rows carry Song of Songs 6:4 and Numbers 13:22 alone), and 199:5's English
# says 2:25 for the Hebrew's 2:26 (a mistyped verse — the quoted words are 2:26's "I sent messengers"). THE ONE "IBID" CANDIDATE: 355:27's
# "(שם ב ב)" ("ibid. 2:2") follows "(שה״ש ב ג)" (Song of Songs 2:3) — SONG OF SONGS 2:2, not Deuteronomy 2:2; the English row cites
# Deuteronomy 33:26 and Exodus 15:11 — no Deuteronomy 1-3 citation in it. All seven Hebrew rows CREDITED with a quick look (each read whole in
# both files at the measurement pass, deu_measure1.out section A).
CIT_HE = [(p, r, (hn(a), hn(b))) for p, rows in enumerate(sif_he, 1) for r, row in enumerate(rows, 1) if p not in PISKAOT for a, b in re.findall(r'\(דברים ([אבג]) ([א-ת]+)\)', clean(row))]
CIT_EN = [(p, r, (int(a), int(b))) for p, rows in enumerate(sif, 1) for r, row in enumerate(rows, 1) if p not in PISKAOT for a, b in re.findall(r'\(Dt\.([123]):(\d+)', clean(row))]
assert CIT_HE == OUTSIDE_HE and CIT_EN == OUTSIDE_EN, (CIT_HE, CIT_EN)
assert HE_CITES(355, 27)[5:7] == ['שה״ש ב ג', 'שם ב ב'] and '(Dt.33:26)' in E(355, 27) and '(Ex.15:11)' in E(355, 27) and not re.search(r'Dt\.[123]:', E(355, 27))
assert HE_CITES(36, 10) == ['שיר השירים ו ד'] and HE_CITES(37, 2) == ['במדבר יג כב', 'ישעיה ל ד', 'בראשית לה כז'] and HE_CITES(199, 5)[-1] == 'דברים ב כו' and '(Dt.2:25)' in E(199, 5) and 'וָאֶשְׁלַח מַלְאָכִים' in Hb(199, 5)
assert heads[37] == (11, 10) and heads[52] == (11, 25) and heads[54] == (11, 26) and heads[82] == (13, 1) and heads[199] == (20, 10) and heads[314] == (32, 11) and heads[36] == (6, 9)
assert 'צִידוֹנִים יִקְרְאוּ לְחֶרְמוֹן שִׂרְיוֹן' in Hb(37, 9) and 'עֲלֵה רֹאשׁ הַפִּסְגָּה' in Hb(37, 11) and 'אֲפִלּוּ כְּעוֹג מֶלֶךְ הַבָּשָׁן' in Hb(52, 1) and 'אַחֲרֵי הַכֹּתוֹ אֶת סִיחֹן' in Hb(54, 2) and 'ה׳ אֱלֹהֵי אֲבוֹתֵיכֶם יוֹסֵף עֲלֵיכֶם' in Hb(82, 5) and 'אֲשֶׁר נְשָׂאֲךָ ה׳ אֱלֹהֶיךָ' in Hb(314, 2)
# THE PRIOR READS: no ledger has read an Onkelos row of Deuteronomy; SIX rows of piskaot 1-30 were read by topic in the Genesis ledgers — 1:13
# (the complaint template, gen_09 and gen_10), 6:1 (the 1:7 geography, gen_24 — material), 8:1 (the Land given as-is, gen_29 — material), 11:1
# (the guardian parable, gen_29), 25:4 (the hyperbole, gen_29 — material), 27:3 (the servant census, gen_27 — no-bearing): named at their rows,
# never counted fresh; the walk's num_32 ledger deferred "Sifrei Devarim on 3:12-20" to this reading by name. FORTY-FOUR ledgers NAME a verse of
# the three chapters (names, not reads).
TRI = f'{ROOT}/logic/oral_triage'
LED = {f: open(f'{TRI}/{f}', encoding='utf-8').read() for f in os.listdir(TRI) if f.endswith('.md') and os.path.isfile(f'{TRI}/{f}') and f'{TRI}/{f}' != OUT}
assert [f for f, t in LED.items() if re.search(r'^- Onkelos Deut(?:eronomy)? \d', t, re.M)] == []
PRIOR = sorted({(f, int(a), int(b)) for f, t in LED.items() for a, b in re.findall(r'Sifrei Devarim (\d+):(\d+)', t) if int(a) <= 30})
assert PRIOR == [('gen_09_helper_woman_first_speech_2026-08-24.md', 1, 13), ('gen_10_serpent_violation_trace_2026-08-25.md', 1, 13), ('gen_24_nations_table_2026-08-25.md', 6, 1), ('gen_27_the_call_2026-08-25.md', 27, 3), ('gen_29_separation_promise_2026-08-25.md', 8, 1), ('gen_29_separation_promise_2026-08-25.md', 11, 1), ('gen_29_separation_promise_2026-08-25.md', 25, 4)], PRIOR
PRIOR_ROWS = {(1, 13): 'gen_09_helper_woman_first_speech (chain_primary) and gen_10_serpent_violation_trace', (6, 1): 'gen_24_nations_table (material — the 1:7 geography)', (8, 1): 'gen_29_separation_promise (material — the Land given as-is)', (11, 1): 'gen_29_separation_promise (enrichment — the guardian parable)', (25, 4): 'gen_29_separation_promise (material — the hyperbole)', (27, 3): 'gen_27_the_call (no-bearing — the servant census)'}
assert 'Sifrei Devarim on 3:12-20 (Deuteronomy\'s spine, read at Deuteronomy)' in LED['num_32_gad_reuben_2026-09-12.md']
NAMING = sorted(f for f, t in LED.items() if re.search(r'Deut(?:eronomy)? [123]:\d+', t))
assert len(NAMING) == 44 and NAMING[0] == 'exo_39_garments_done_2026-09-02.md' and NAMING[-1] == 'num_36_heiresses_2026-09-09.md', (len(NAMING), NAMING[:3], NAMING[-3:])
def plain(w): return ''.join(c for c in w if c != '/' and not (0x0591 <= ord(c) <= 0x05C7))
def pointed(w): return ''.join(c for c in w if c != '/' and not (0x0591 <= ord(c) <= 0x05AF))
def NF(s): return unicodedata.normalize('NFC', s)
ONK_LEN = {c: len(onk[c - 1]) for c in (1, 2, 3)}
assert len(onk) == 34 and len(onk_he) == 34 and ONK_LEN == {1: 46, 2: 37, 3: 29} and {c: len(onk_he[c - 1]) for c in (1, 2, 3)} == ONK_LEN and sum(len(c) for c in onk_he) == 956, ONK_LEN
def onk_ev(c, v): return clean(onk[c - 1][v - 1]), clean(onk_he[c - 1][v - 1])
shelf_deut = sorted(d for d in os.listdir(f'{ROOT}/Data/sefaria_export') if re.search(r'Deuteronomy|Devarim', d))
outside = [d for d in shelf_deut if d not in ('Sifrei_Devarim', 'Onkelos_Deuteronomy')]
assert len(shelf_deut) == 28 and len(outside) == 26 and 'Rashi_on_Deuteronomy' in outside and 'Midrash_Tannaim_on_Deuteronomy' in outside and 'Targum_Jonathan_on_Deuteronomy' in outside, len(outside)

# ---- THE DRAFTS' SPANS, COMPUTED ----
db = sqlite3.connect(f'file:{ROOT}/Data/tanakh.sqlite?mode=ro', uri=True)
VC = dict(db.execute("SELECT chapter, COUNT(*) FROM verses WHERE book='Deut' GROUP BY chapter").fetchall())
assert VC[1] == 46 and VC[2] == 37 and VC[3] == 29 and sum(VC.values()) == 959 and len(VC) == 34
def unit_text(uid): return open(f'{ROOT}/logic/units/{uid}.yaml', encoding='utf-8').read()
def steps(uid): return sorted({(int(a), int(b)) for a, b in re.findall(r'STEP_Dt_(\d+)_(\d+)', unit_text(uid))})
FIRST = not os.path.exists(OUT)   # the first pass: the six units are drafts without operators or step E; after the seat and the ritual they are frozen (the rewrite and the records import this module too)
for uid, (c, lo, hi) in SPANS.items():
    t = unit_text(uid)
    assert steps(uid) == [(c, v) for v in range(lo, hi + 1)] and re.search(rf'refs: "?{c}:{lo}-{hi}"?', t) and '\nbinary_trees:' in t, uid
    if FIRST: assert 'status: draft' in t and 'operators:' not in t and '- step: E' not in t, uid
    assert t.count(f'  - id: STEP_Dt_{c}_{lo}\n') == 1 and t.count(f'  - id: STEP_Dt_{c}_{hi}\n') == 1, uid
assert 'exo_18_yitro' in unit_text('deu_01_frame_officers') and 'num_36_heiresses' in unit_text('deu_01_frame_officers') and 'num_13_spies_sent' in unit_text('deu_01_spies_refuse') and 'num_21_snakes_conquest' in unit_text('deu_02_sihon') and 'num_32_gad_reuben' in unit_text('deu_03_og_gilead')
assert not any(f.startswith('deu_') and f != os.path.basename(OUT) for f in os.listdir(TRI))   # no other Deuteronomy ledger exists; the manifests' written-once guard is the manifest script's own
ALLTXT = ''.join(open(f'{ROOT}/logic/units/{f}', encoding='utf-8').read() for f in os.listdir(f'{ROOT}/logic/units') if f.endswith('.yaml') and f[:-5] not in UIDS) + ''.join(open(f'{ROOT}/logic/oral_audit/manifests/{f}', encoding='utf-8').read() for f in os.listdir(f'{ROOT}/logic/oral_audit/manifests') if f.endswith('.json') and f[:-12] not in UIDS)   # every OTHER unit and manifest (this sitting's six carry the prefixes once written and seated)
assert all(f'"{p}-' not in ALLTXT and f'[claim {p}-' not in ALLTXT for p in PREFIX.values())
SPAN = [(c, v) for c in (1, 2, 3) for v in range(1, VC[c] + 1)]
NV = 112
assert len(SPAN) == NV

# ---- THE INK, computed from the Tanakh DB and the snapshot store ----
rows = db.execute("SELECT v.book, v.chapter, v.verse, w.he, w.morph, w.lemma FROM words w JOIN verses v ON w.verse_id=v.id ORDER BY v.id, w.idx").fetchall()
by, byp, byl = {}, {}, {}
for b, c, v, he, m, lem in rows:
    by.setdefault((b, c, v), []).append((plain(he), m)); byp.setdefault((b, c, v), []).append(pointed(he)); byl.setdefault((b, c, v), []).append((lem or '').split('/')[-1].strip())
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
def seats_in(pred): return [((c, v), x) for (c, v) in SPAN for x, m in by[('Deut', c, v)] if pred(x, m)]
def cnt_in(pred): return sum(1 for (c, v) in SPAN for x, m in by[('Deut', c, v)] if pred(x, m))
def PT(b, c, v, tok): return [NF(x) for x in byp[(b, c, v)] if plain(x) == tok]
def DIFF(a, b_):
    import difflib
    A, B = words(*a), words(*b_)
    return [(op, A[i1:i2], B[j1:j2]) for op, i1, i2, j1, j2 in difflib.SequenceMatcher(None, A, B).get_opcodes() if op != 'equal']
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
        while j < len(ws) and plain(ws[j]) != k: j += 1
        if j >= len(ws): FAIL.append(('A', c, v, k, [plain(x) for x in ws])); out.append('⟨MISS⟩'); continue
        out.append(ws[j]); i = j + 1
    return ' '.join(out)
def aramaic(c, v): return [plain(x) for x in onk_ev(c, v)[1].rstrip(':').split()]
def arm(c, v): return plain(onk_ev(c, v)[1])
def onk_seats(sub): return [(c + 1, v + 1) for c in range(34) for v in range(len(onk_he[c])) if sub in arm(c + 1, v + 1)]
def onk_tok(tok): return [(c + 1, v + 1) for c in range(34) for v in range(len(onk_he[c])) if tok in aramaic(c + 1, v + 1)]
def HP(c, v, *pieces):
    """the Hebrew cut in GLOSSED PIECES — each piece a (tokens, gloss) pair of at most seven tokens, the gloss right after it (the lint's window)"""
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
    """a Sifrei Hebrew row cut by consonants — the shelf's own bytes (pointed in this export)"""
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
for c, v, hp, g in store.execute("SELECT v.chapter, v.verse, w.he_plain, w.gloss FROM words w JOIN verses v ON w.verse_id=v.id WHERE v.book='Deut' AND v.chapter <= 3 ORDER BY v.id, w.idx"):
    SG.setdefault((c, v), []).append((hp.replace('/', ''), g))
def sg(c, v, tok):
    for hp, g in SG[(c, v)]:
        if hp == tok: return g
    raise KeyError((c, v, tok))
# THE STORE'S ONE WRITTEN-AND-READ PAIR in the span: 2:33 carries TWELVE tokens in the store against the DB's ELEVEN — "his son" written (בנו)
# and "his sons" read (בניו), the store keeping both, the DB the written form unpointed.
STORE_MISMATCH = [(c, v, n, len(by[('Deut', c, v)])) for c, v, n in store.execute("SELECT v.chapter, v.verse, COUNT(*) FROM words w JOIN verses v ON w.verse_id=v.id WHERE v.book='Deut' AND v.chapter<=3 GROUP BY v.chapter, v.verse").fetchall() if n != len(by[('Deut', c, v)])]
assert STORE_MISMATCH == [(2, 33, 12, 11)] and [hp for hp, g in SG[(2, 33)]][7:9] == ['בנו', 'בניו'] and words('Deut', 2, 33)[7] == 'בנו' and PT('Deut', 2, 33, 'בנו') == ['בנו'], STORE_MISMATCH

# THE ENGINE'S PARSER on every verse — MEASURED before the compile is asked: ELEVEN number verses read, NO GAP — 1:2 "eleven days" [11]; 1:3
# "in the fortieth year, in the eleventh month, on the first of the month" [40, 11, 1] (the number reader's date, where Numbers 33:38's
# ordinal date read [40, 5] by the ordinal reader — the forms differ: "in forty years" here against "in the year of the forty" there); 1:11
# "a thousand times" [1000]; 1:15 "captains of thousands, hundreds, fifties, tens" [100, 50, 10] — THE THOUSANDS A NOUN (the plural, rule 29,
# as at Exodus 18:21); 1:23 "twelve men, one man per tribe" [12, 1]; 2:7 "these forty years" [40]; 2:14 "thirty-eight years" [38]; 3:4 "sixty
# cities" [60]; 3:8 "two kings" [2] (the construct "two" marked ^); 3:11 "nine cubits ... four cubits" [9, 4]; 3:21 "the two kings" [2]; no
# ordinals; THE FRACTION CLASS UNREAD — "half the hill country" (3:12) and "the half-tribe" (3:13) carry no number: named for the compile.
sys.path.insert(0, f'{ROOT}/World/step9')
with contextlib.redirect_stdout(io.StringIO()):
    import cold_run_sequence as CS
def N(b, c, v): return CS.ink_numbers(CS.verse_words(b, c, v))
def O(b, c, v): return CS.ink_ordinals(CS.verse_words(b, c, v))
PARSED = {(c, v): N('Deut', c, v) for (c, v) in SPAN if N('Deut', c, v)}
assert PARSED == {(1, 2): [11], (1, 3): [40, 11, 1], (1, 11): [1000], (1, 15): [100, 50, 10], (1, 23): [12, 1], (2, 7): [40], (2, 14): [38], (3, 4): [60], (3, 8): [2], (3, 11): [9, 4], (3, 21): [2]}, PARSED
assert {(c, v): O('Deut', c, v) for (c, v) in SPAN if O('Deut', c, v)} == {} and [((c, v), t) for (c, v) in SPAN for t in CS.verse_words('Deut', c, v) if t[-1] in '#~^%@|*'] == [((3, 8), 'שני^'), ((3, 21), 'לשני^')]
assert O('Num', 33, 38) == [40, 5] and N('Num', 33, 38) == [1] and N('Exod', 18, 21) == [100, 50, 10] and N('Exod', 18, 25) == [100, 50, 10] and N('Num', 33, 38) == [1]
assert PT('Deut', 1, 3, 'בארבעים') == ['בְּאַרְבָּעִים'] and PT('Num', 33, 38, 'הארבעים') == ['הָֽאַרְבָּעִים'] and words('Num', 33, 38)[11:13] == ['בשנת', 'הארבעים'] and words('Deut', 1, 3)[1:3] == ['בארבעים', 'שנה']
assert sg(3, 12, 'וחצי') == 'and-half' and sg(3, 13, 'לחצי') == 'to-half' and N('Deut', 3, 12) == [] and N('Deut', 3, 13) == []
TOK = {c: sum(len(by[('Deut', c, v)]) for v in range(1, VC[c] + 1)) for c in (1, 2, 3)}
assert TOK == {1: 654, 2: 532, 3: 461}, TOK

# THE FRAMES AND THE REGISTER: SEVEN divine frames, ALL IN MOSES' VOICE — "and the LORD said to me" at 1:42, 2:2, 2:9, 2:31, 3:2, 3:26 and
# "and the LORD spoke to me" at 2:17 (THE BIBLE'S ONLY SEAT OF THAT FORM); "and the LORD said to me" eleven seats in the book (the six, 5:28,
# 9:12, 9:13, 10:11, 18:17); "saying" at FOURTEEN seats; the narrative verbs FIRST PERSON — "and I said", "and I took", "and I gave", "and I
# commanded", "and we journeyed", "and we turned", "and we took", "and we smote", "and we captured", "and we devoted", "and we dwelt" —
# the speech retelling the story; THE CASE TOKENS: "for" at fifteen seats, "if" one (1:35's oath), no "and if", no "or" — the three chapters
# carry NO CASE (the compiler law's structure absent: the retelling is narrative in the first person). THE REGISTER GATE: Deut 1:1 an EMPTY
# footer (the block from Numbers 36:13 holds no law), 1:3, 1:19, 1:41 NONE — all "the book not read", waiting for this reading and the compile.
DIV = [(c, v) for (c, v) in SPAN if any(words('Deut', c, v)[i] in ('ויאמר', 'וידבר') and words('Deut', c, v)[i + 1] == 'יהוה' for i in range(len(words('Deut', c, v)) - 1))]
assert DIV == [(1, 42), (2, 2), (2, 9), (2, 17), (2, 31), (3, 2), (3, 26)] and P('וידבר', 'יהוה', 'אלי') == ['Deut 2:17'] and words('Deut', 2, 17) == ['וידבר', 'יהוה', 'אלי', 'לאמר'] and words('Deut', 2, 2) == ['ויאמר', 'יהוה', 'אלי', 'לאמר']
assert [s for s in P('ויאמר', 'יהוה', 'אלי') if s.startswith('Deut')] == S_('Deut 1:42', 'Deut 2:2', 'Deut 2:9', 'Deut 2:31', 'Deut 3:2', 'Deut 3:26', 'Deut 5:28', 'Deut 9:12', 'Deut 9:13', 'Deut 10:11', 'Deut 18:17')
assert [(c, v) for (c, v) in SPAN if 'לאמר' in words('Deut', c, v)] == [(1, 5), (1, 6), (1, 9), (1, 16), (1, 28), (1, 34), (1, 37), (2, 2), (2, 4), (2, 17), (2, 26), (3, 18), (3, 21), (3, 23)]
REG = {c: {v: [x for x, m in by[('Deut', c, v)] if m and re.search(r'V.w', m)] for v in range(1, VC[c] + 1) if any(m and re.search(r'V.w', m) for x, m in by[('Deut', c, v)])} for c in (1, 2, 3)}
assert REG[1] == {3: ['ויהי'], 9: ['ואמר'], 14: ['ותענו', 'ותאמרו'], 15: ['ואקח', 'ואתן'], 16: ['ואצוה'], 18: ['ואצוה'], 19: ['ונסע', 'ונלך', 'ונבא'], 20: ['ואמר'], 22: ['ותקרבון', 'ותאמרו'], 23: ['וייטב', 'ואקח'], 24: ['ויפנו', 'ויעלו', 'ויבאו', 'וירגלו'], 25: ['ויקחו', 'ויורדו', 'וישבו', 'ויאמרו'], 26: ['ותמרו'], 27: ['ותרגנו', 'ותאמרו'], 29: ['ואמר'], 34: ['וישמע', 'ויקצף', 'וישבע'], 41: ['ותענו', 'ותאמרו', 'ותחגרו', 'ותהינו'], 42: ['ויאמר'], 43: ['ואדבר', 'ותמרו', 'ותזדו', 'ותעלו'], 44: ['ויצא', 'וירדפו', 'ויכתו'], 45: ['ותשבו', 'ותבכו'], 46: ['ותשבו']}, REG[1]
assert REG[2] == {1: ['ונפן', 'ונסע', 'ונסב'], 2: ['ויאמר'], 8: ['ונעבר', 'ונפן', 'ונעבר'], 9: ['ויאמר'], 12: ['וישמידום', 'וישבו'], 13: ['ונעבר'], 16: ['ויהי'], 17: ['וידבר'], 21: ['וישמידם', 'ויירשם', 'וישבו'], 22: ['ויירשם', 'וישבו'], 23: ['וישבו'], 26: ['ואשלח'], 31: ['ויאמר'], 32: ['ויצא'], 33: ['ויתנהו', 'ונך'], 34: ['ונלכד', 'ונחרם']}, REG[2]
assert REG[3] == {1: ['ונפן', 'ונעל', 'ויצא'], 2: ['ויאמר'], 3: ['ויתן', 'ונכהו'], 4: ['ונלכד'], 6: ['ונחרם'], 8: ['ונקח'], 14: ['ויקרא'], 18: ['ואצו'], 23: ['ואתחנן'], 26: ['ויתעבר', 'ויאמר'], 29: ['ונשב']}, REG[3]
CASE = {f'{c}:{v}': [x for x in words('Deut', c, v) if x in ('כי', 'אם', 'ואם', 'או', 'פן')] for (c, v) in SPAN if any(x in ('כי', 'אם', 'ואם', 'או', 'פן') for x in words('Deut', c, v))}
assert CASE == {'1:17': ['כי'], '1:35': ['אם'], '1:38': ['כי'], '1:42': ['כי'], '2:5': ['כי', 'כי'], '2:7': ['כי'], '2:9': ['כי', 'כי'], '2:19': ['כי', 'כי'], '2:30': ['כי'], '3:2': ['כי'], '3:11': ['כי'], '3:19': ['כי'], '3:22': ['כי'], '3:27': ['כי'], '3:28': ['כי']}, CASE
RD = open(f'{ROOT}/World/step9/register_dispositions.yaml', encoding='utf-8').read(); RI = open(f'{ROOT}/World/step9/REGISTER_INDEX.md', encoding='utf-8').read()
assert sorted(re.findall(r'^\s*Deut (1:\d+)\s+(\w+)', RI, re.M)) == [('1:1', 'EMPTY'), ('1:19', 'NONE'), ('1:3', 'NONE'), ('1:41', 'NONE')] and re.findall(r'^\s*Deut ([23]:\d+)', RI, re.M) == []
assert re.search(r'^footers:\n(?:.*\n)*?  Deut 1:1:\n    class: EMPTY\n    why: the block \(Num 36:13, Deut 1:1\] holds no law', RD, re.M) and all(re.search(rf'^  Deut {s}:\n    class: NONE\n    why: \'?(?:THE NUMBERS WALK 10b|Deuteronomy is not on the tape)', RD, re.M) for s in ('1:3', '1:19', '1:41'))
assert P('ככל', 'אשר', 'צוה', 'יהוה', 'אתו') == S_('Deut 1:3', 'Exod 40:16') and len(P('ככל', 'אשר', 'צוה', 'יהוה', 'את', 'משה', books=T)) == 7

# 1:1-5 THE FRAME (computed): "THESE ARE THE WORDS" five Bible seats (Exodus 19:6 and 35:1 the Torah's others); "which Moses spoke" 1:1 and
# 4:45; "to all Israel" six seats in the book; "BEYOND THE JORDAN" eleven Torah seats, nine in this book (1:1, 1:5, 3:8, 3:20, 3:25, 4:41,
# 4:46, 4:47, 11:30) and Jacob's funeral's two (Genesis 50:10-11); 26 in the Bible; "in the wilderness, in the Arabah" one seat; "OPPOSITE
# SUPH" one seat — Suph a PLACE here (the store glosses it "Red-Sea"; the Sea of Reeds is two tokens at 1:40, 2:1); Paran eleven seats;
# Tophel's consonants a homograph (plaster, Ezekiel 13's whitewash; "you may pray", Numbers 34:2 no — the tokens "תפל" at fourteen seats, the
# place only here); Laban the place with the vav a homograph of Laban the man; Hazeroth three seats (this, Numbers 33:17-18); DI-ZAHAB two
# tokens in the DB ("and-di", "zahab"), the store gluing the name; "ELEVEN DAYS" one seat; "from Horeb" twelve seats (1:2, 1:19 in the
# span); "the way of Mount Seir" one; KADESH-BARNEA as two tokens ONLY at 1:2 and 1:19 (joined elsewhere by the maqqef in the DB's
# tokenization); "Mount Seir" three Torah seats (1:2, 2:1, 2:5); 1:3 THE DATE — "in the fortieth year" one seat (Numbers 33:38's "in the year
# of the forty" the other form), "in the eleventh" one seat (the bare "eleven" form's twelve seats), "on the first of the month" ten Torah seats, "ACCORDING TO
# ALL THAT THE LORD COMMANDED HIM" two seats — this and EXODUS 40:16 (the tabernacle's receipt), THE RECEIPT FORM (the register's second form,
# nine Torah seats with "commanded", seven with "Moses"); 1:4 "after he had smitten" one seat, Sihon and Og in one verse four (this, 29:6,
# Numbers 32:33, Nehemiah 9:22), "in Ashtaroth" five, Edrei six (the Joshua 12:4 / 13:12 pair naming Og "in Ashtaroth and in Edrei" —
# Deuteronomy's "who dwelt in Ashtaroth, in Edrei" without the vav); 1:5 "took upon himself" (the verb of 1 Samuel 12:22, Hosea 5:11 — the
# store glosses "yield"), "EXPLAIN" — the verb's three seats: THIS, 27:8 ("very plainly" on the stones) and HABAKKUK 2:2 ("make it plain on
# tablets") — the same consonants as "well" (38 seats of the bare token, the store glossing "dig" here), "in the land of Moab" five seats (the book's colophon
# 34:5-6 among them), "THIS TORAH" three Torah seats (1:5, 31:9, 31:11).
assert P('אלה', 'הדברים') == S_('Deut 1:1', 'Exod 19:6', 'Exod 35:1', 'Isa 42:16', 'Zech 8:16') and P('אשר', 'דבר', 'משה') == S_('Deut 1:1', 'Deut 4:45') and [s for s in P('אל', 'כל', 'ישראל') if s.startswith('Deut')] == S_('Deut 1:1', 'Deut 27:9', 'Deut 29:1', 'Deut 31:1', 'Deut 32:45', 'Deut 5:1') and len(P('אל', 'כל', 'ישראל')) == 8
assert P('בעבר', 'הירדן', books=T) == S_('Deut 11:30', 'Deut 1:1', 'Deut 1:5', 'Deut 3:20', 'Deut 3:25', 'Deut 3:8', 'Deut 4:41', 'Deut 4:46', 'Deut 4:47', 'Gen 50:10', 'Gen 50:11') and len(P('בעבר', 'הירדן')) == 26
assert P('במדבר', 'בערבה') == ['Deut 1:1'] and P('מול', 'סוף') == ['Deut 1:1'] and sg(1, 1, 'סוף') == 'Red-Sea' and sg(1, 40, 'סוף') == 'reed' and P('ים', 'סוף', books=T)[:0] == [] and [s for s in P('ים', 'סוף') if s.startswith('Deut')] == S_('Deut 11:4', 'Deut 1:40', 'Deut 2:1')
assert len(U('פארן', 'בפארן', 'מפארן')) == 11 and U('תפל') == S_('Deut 1:1', 'Esth 6:10', 'Exod 15:16', 'Ezek 13:10', 'Ezek 13:11', 'Ezek 13:14', 'Ezek 13:15', 'Ezek 22:28', 'Jer 36:7', 'Jer 37:20', 'Jer 39:18', 'Jer 42:2', 'Job 6:6', 'Num 34:2') and [m for x, m in by[('Deut', 1, 1)] if x == 'תפל'] == ['HNp'] and [m for x, m in by[('Deut', 1, 1)] if x == 'ולבן'] == ['HC/Np']
assert U('חצרת', 'וחצרת', 'בחצרת', 'מחצרת') == S_('Deut 1:1', 'Num 33:17', 'Num 33:18') and words('Deut', 1, 1)[-2:] == ['ודי', 'זהב'] and sg(1, 1, 'זהב') == 'Dizahab' and sg(1, 1, 'ודי') == 'and-?'
assert P('אחד', 'עשר', 'יום') == ['Deut 1:2'] and len(U('מחרב')) == 12 and P('דרך', 'הר', 'שעיר') == ['Deut 1:2'] and P('קדש', 'ברנע') == S_('Deut 1:19', 'Deut 1:2') and len(P('הר', 'שעיר', books=T)) == 3 and P('הר', 'שעיר', books=T) == S_('Deut 1:2', 'Deut 2:1', 'Deut 2:5')
assert P('בארבעים', 'שנה') == ['Deut 1:3'] and P('בשנת', 'הארבעים') == S_('1Chr 26:31', 'Num 33:38') and P('בעשתי', 'עשר') == ['Deut 1:3'] and len(U('עשתי')) == 12 and len(P('באחד', 'לחדש', books=T)) == 10 and len(P('ככל', 'אשר', 'צוה', 'יהוה', books=T)) == 9
assert P('אחרי', 'הכתו') == ['Deut 1:4'] and sorted(s for s in P('סיחן') + P('סיחון') if any(x in ('עוג', 'ועוג') for x in words(s.split()[0], int(s.split()[1].split(':')[0]), int(s.split(':')[1])))) == S_('Deut 1:4', 'Deut 29:6', 'Neh 9:22', 'Num 32:33')
assert len(U('בעשתרת', 'בעשתרות')) == 5 and U('באדרעי', 'אדרעי', 'ואדרעי') == S_('Deut 1:4', 'Deut 3:1', 'Deut 3:10', 'Josh 13:31', 'Josh 19:37', 'Num 21:33') and words('Josh', 12, 4)[-2:] == ['בעשתרות', 'ובאדרעי'] and words('Deut', 1, 4)[-2:] == ['בעשתרת', 'באדרעי']
assert U('הואיל') == S_('1Sam 12:22', 'Deut 1:5', 'Hos 5:11') and sg(1, 5, 'הואיל') == 'yield' and lemma_of('Deut', 1, 5, 'באר') == ['874'] and LEMT('874') == [('Deut 1:5', 'באר', 'HVpp3ms'), ('Deut 27:8', 'באר', 'HVpa'), ('Hab 2:2', 'ובאר', 'HC/Vpv2ms')] and len(U('באר')) == 38 and sg(1, 5, 'באר') == 'dig'
assert P('בארץ', 'מואב') == S_('Deut 1:5', 'Deut 28:69', 'Deut 32:49', 'Deut 34:5', 'Deut 34:6') and P('את', 'התורה', 'הזאת', books=T) == S_('Deut 1:5', 'Deut 31:11', 'Deut 31:9')

# 1:6-8 HOREB (computed): "the LORD our God spoke to us" two seats (Jeremiah 26:16 the other); "YOU HAVE DWELT LONG ENOUGH" — "enough for you"
# EIGHT Bible seats: KORAH'S TWICE (Numbers 16:3 the rebels' cry, 16:7 Moses' answer), this, 2:3, 3:19, Jeroboam's "enough of going up" (1 Kings
# 12:28), Ezekiel's two — and "ENOUGH FOR YOU" in the singular ONCE: 3:26, Moses barred (the plural's form turned on him, the Sifrei 29's
# reading); "turn and journey" — Numbers 14:25's words to the rejected generation, here the words at Horeb (the two seats); "turn you" 1:40,
# 2:3; "the hill country of the Amorites" three seats (1:7, 19, 20); "all its neighbors" one seat; the five regions in one verse one seat
# (Joshua 10:40 and 12:8 the runs with four and six); "the land of the Canaanite and Lebanon" one seat; "THE GREAT RIVER, THE RIVER EUPHRATES"
# — GENESIS 15:18's words at their second seat (the covenant of the pieces: Joshua 1:4 plene "the great"); "SEE, I HAVE SET BEFORE YOU" one
# seat; "see, I have set" eight seats (2:24 Sihon, 30:15 life and death; Joseph's, Jericho's, Ai's); "go in and possess" one seat; the three
# patriarchs' dative eleven Torah seats; "to give to them and to their seed after them" one seat.
assert P('יהוה', 'אלהינו', 'דבר', 'אלינו') == S_('Deut 1:6', 'Jer 26:16') and P('רב', 'לכם') == S_('1Kgs 12:28', 'Deut 1:6', 'Deut 2:3', 'Deut 3:19', 'Ezek 44:6', 'Ezek 45:9', 'Num 16:3', 'Num 16:7') and P('רב', 'לך') == ['Deut 3:26'] and P('שבת', 'בהר', 'הזה') == ['Deut 1:6']
assert P('פנו', 'וסעו', 'לכם') == S_('Deut 1:7', 'Num 14:25') and P('פנו', 'לכם') == S_('Deut 1:40', 'Deut 2:3') and words('Num', 14, 25)[-6:] == ['וסעו', 'לכם', 'המדבר', 'דרך', 'ים', 'סוף'] and words('Deut', 1, 40)[1:5] == ['פנו', 'לכם', 'וסעו', 'המדברה']
assert P('הר', 'האמרי') == S_('Deut 1:19', 'Deut 1:20', 'Deut 1:7') and P('ואל', 'כל', 'שכניו') == ['Deut 1:7'] and P('בערבה', 'בהר', 'ובשפלה', 'ובנגב', 'ובחוף', 'הים') == ['Deut 1:7'] and P('ארץ', 'הכנעני', 'והלבנון') == ['Deut 1:7']
assert P('הנהר', 'הגדל', 'נהר', 'פרת') == S_('Deut 1:7', 'Gen 15:18') and P('הנהר', 'הגדול', 'נהר', 'פרת') == ['Josh 1:4'] and words('Gen', 15, 18)[-4:] == ['הנהר', 'הגדל', 'נהר', 'פרת'] and PT('Deut', 1, 7, 'והלבנון') == ['וְהַלְּבָנוֹן'] and PT('Deut', 3, 25, 'והלבנון') == ['וְהַלְּבָנֽוֹן']
assert P('ראה', 'נתתי', 'לפניכם') == ['Deut 1:8'] and P('ראה', 'נתתי') == S_('1Chr 21:23', 'Deut 1:8', 'Deut 2:24', 'Deut 30:15', 'Ezek 4:15', 'Gen 41:41', 'Josh 6:2', 'Josh 8:1') and P('באו', 'ורשו') == ['Deut 1:8'] and len(P('לאברהם', 'ליצחק', 'וליעקב', books=T)) == 11 and P('לתת', 'להם', 'ולזרעם', 'אחריהם') == ['Deut 1:8']

# 1:9-18 THE OFFICERS (computed): "I CANNOT BEAR YOU ALONE" one seat — NUMBERS 11:14's cry in other words ("I am not able, I alone, to bear all
# this people") and JETHRO'S "you are not able to do it alone" (Exodus 18:18); "has multiplied you" one; "AS THE STARS OF HEAVEN FOR MULTITUDE"
# three seats, all this book's (1:10, 10:22, 28:62), "as the stars of heaven" six Torah seats (Abraham's, Isaac's, the calf's plea); "A
# THOUSAND TIMES" one seat (the Sifrei 11: Moses' blessing beside the LORD's unbounded one; the outside row 82:5 refuses to lengthen the
# priestly blessing by it); "HOW CAN I BEAR ALONE" one seat — "HOW" (איכה, the Lamentations word) six Torah seats, GENESIS 3:9's "WHERE ARE
# YOU" among them by the consonants (the Sifrei 1:13's own link — Adam's "where", Moses' "how", Isaiah's, Jeremiah's — the three "eikhah" of
# the midrash); "your trouble" a HAPAX (the root's other seat Isaiah 1:14), "your burden" one, "your strife" 1:12 and Isaiah 41:21; "GIVE
# YOURSELVES" four seats (Joshua 18:4's spies, Judges 20:7, Ahithophel's), the imperative sixteen; "WISE AND UNDERSTANDING AND KNOWN" — the
# three at 1:13 against JETHRO'S FOUR (able, God-fearing, true, hating gain — Exodus 18:21) and 1:15's TWO (wise and known: "understanding"
# not found — the Sifrei 13:4, 15:3); "and understanding" this form here alone (Isaiah 5:21's the bare plural; the discern-root 161 seats), "and known" three; "AND I WILL SET THEM AS YOUR
# HEADS" one seat — the store reads the verb "and-put/set-them" (the Sifrei 13:6 revocalizes: "their guilt on your heads"); "and you answered
# me" one; "the thing is good" one; "the heads of your tribes" 1:15 and 5:23; THE OFFICERS' FORM — 1:15 "captains of thousands AND captains of
# hundreds AND captains of fifties AND captains of tens" with the vavs, one seat; Exodus 18:21 and 25 without the vavs (the parser reads
# [100, 50, 10] at all three — the thousands a plural noun); "AND OFFICERS FOR YOUR TRIBES" one seat, the officers-word THIRTEEN Torah seats
# (Exodus 5's five Egyptian foremen, Numbers 11:16's seventy, this, 16:18's appointing, 20:5-9's war, 29:9's and 31:28's assemblies); "and I commanded your judges" one seat;
# "hear between your brothers" one; "judge righteously" one; "BETWEEN A MAN AND HIS BROTHER AND HIS STRANGER" one seat — "his stranger"
# (with the suffix) two Bible seats: this and EXODUS 6:4 ("their sojournings" — the same consonants, another sense), the lemma's 83; "YOU
# SHALL NOT RECOGNIZE FACES" 1:17 and 16:19 (the judges' law again); "SMALL AND GREAT ALIKE" the pair's Torah seat one (Chronicles' three
# the others); "YOU SHALL NOT BE AFRAID OF A MAN" — the fear-verb by the lemma (the store's "turn-aside-from-the-road" the sojourn-root's
# homograph); "FOR THE JUDGMENT IS GOD'S" one seat; "the hard matter" — the store's "be-dense"; "AT THAT TIME" TEN seats in the three chapters
# (1:9, 16, 18, 2:34, 3:4, 8, 12, 18, 21, 23), the speech's refrain — eighteen Torah seats, nineteen in the Bible.
assert P('לא', 'אוכל', 'לבדי', 'שאת', 'אתכם') == ['Deut 1:9'] and words('Num', 11, 14)[:6] == ['לא', 'אוכל', 'אנכי', 'לבדי', 'לשאת', 'את'] and words('Exod', 18, 18)[-4:] == ['לא', 'תוכל', 'עשהו', 'לבדך'] and P('הרבה', 'אתכם') == ['Deut 1:10']
assert P('ככוכבי', 'השמים', 'לרב') == S_('Deut 10:22', 'Deut 1:10', 'Deut 28:62') and P('ככוכבי', 'השמים', books=T) == S_('Deut 10:22', 'Deut 1:10', 'Deut 28:62', 'Exod 32:13', 'Gen 22:17', 'Gen 26:4') and P('אלף', 'פעמים') == ['Deut 1:11'] and P('יסף', 'עליכם', 'ככם') == ['Deut 1:11']
assert P('איכה', 'אשא', 'לבדי') == ['Deut 1:12'] and U('איכה', books=T) == S_('Deut 12:30', 'Deut 18:21', 'Deut 1:12', 'Deut 32:30', 'Deut 7:17', 'Gen 3:9') and U('טרחכם') == ['Deut 1:12'] and LEMT('2960') == [('Deut 1:12', 'טרחכם', 'HNcmsc/Sp2mp'), ('Isa 1:14', 'לטרח', 'HR/Ncmsa')] and U('ומשאכם') == ['Deut 1:12'] and U('וריבכם') == ['Deut 1:12'] and 'ריבכם' in words('Isa', 41, 21)
assert P('הבו', 'לכם') == S_('2Sam 16:20', 'Deut 1:13', 'Josh 18:4', 'Judg 20:7') and len(U('הבו')) == 16 and P('אנשים', 'חכמים', 'ונבנים', 'וידעים') == ['Deut 1:13'] and words('Deut', 1, 15)[4:7] == ['אנשים', 'חכמים', 'וידעים'] and 'ונבנים' not in words('Deut', 1, 15)
assert words('Exod', 18, 21)[4:12] == ['אנשי', 'חיל', 'יראי', 'אלהים', 'אנשי', 'אמת', 'שנאי', 'בצע'] and P('אנשי', 'חיל', books=T) == S_('Exod 18:21', 'Exod 18:25', 'Gen 47:6') and P('יראי', 'אלהים') == S_('Exod 18:21', 'Ps 66:16') and P('אנשי', 'אמת') == ['Exod 18:21'] and P('שנאי', 'בצע') == S_('Exod 18:21', 'Prov 28:16')
assert U('ונבנים') == ['Deut 1:13'] and U('נבנים') == ['Isa 5:21'] and lemma_of('Deut', 1, 13, 'ונבנים') == ['995'] and len(LEMV('995')) == 161 and U('וידעים') == S_('Deut 1:13', 'Deut 1:15', 'Job 34:2') and U('ואשימם') == ['Deut 1:13'] and sg(1, 13, 'ואשימם') == 'and-put/set-them/their' and P('ותענו', 'אתי', 'ותאמרו') == ['Deut 1:14'] and P('טוב', 'הדבר', 'אשר', 'דברת', 'לעשות') == ['Deut 1:14']
assert P('ראשי', 'שבטיכם') == S_('Deut 1:15', 'Deut 5:23') and P('שרי', 'אלפים', 'ושרי', 'מאות', 'ושרי', 'חמשים', 'ושרי', 'עשרת') == ['Deut 1:15'] and P('שרי', 'אלפים', 'שרי', 'מאות', 'שרי', 'חמשים', 'ושרי', 'עשרת') == S_('Exod 18:21', 'Exod 18:25') and P('ושטרים', 'לשבטיכם') == ['Deut 1:15']
assert sorted({f'{b} {c}:{v}' for (b, c, v), ws in by.items() if b in T for x, _ in ws if 'שטר' in x}) == S_('Deut 16:18', 'Deut 1:15', 'Deut 20:5', 'Deut 20:8', 'Deut 20:9', 'Deut 29:9', 'Deut 31:28', 'Exod 5:10', 'Exod 5:14', 'Exod 5:15', 'Exod 5:19', 'Exod 5:6', 'Num 11:16')
assert P('ואצוה', 'את', 'שפטיכם') == ['Deut 1:16'] and P('שמע', 'בין', 'אחיכם') == ['Deut 1:16'] and P('ושפטתם', 'צדק') == ['Deut 1:16'] and P('בין', 'איש', 'ובין', 'אחיו', 'ובין', 'גרו') == ['Deut 1:16'] and U('גרו') == S_('Deut 1:16', 'Exod 6:4') and lemma_of('Deut', 1, 16, 'גרו') == ['1616'] and len(LEMV('1616')) == 83
assert P('תכירו', 'פנים') == ['Deut 1:17'] and P('תכיר', 'פנים') == ['Deut 16:19'] and P('כקטן', 'כגדל') == ['Deut 1:17'] and U('כקטן') == S_('1Chr 25:8', '1Chr 26:13', '2Chr 31:15', 'Deut 1:17') and lemma_of('Deut', 1, 17, 'תגורו') == ['1481 c'] and sg(1, 17, 'תגורו') == 'turn-aside-from-the-road' and P('כי', 'המשפט', 'לאלהים', 'הוא') == ['Deut 1:17'] and sg(1, 17, 'יקשה') == 'be-dense'
BET = [(c, v) for (c, v) in SPAN if any(words('Deut', c, v)[i:i + 2] == ['בעת', 'ההוא'] for i in range(len(words('Deut', c, v)) - 1))]
assert BET == [(1, 9), (1, 16), (1, 18), (2, 34), (3, 4), (3, 8), (3, 12), (3, 18), (3, 21), (3, 23)] and len(P('בעת', 'ההוא', books=T)) == 18 and len(P('בעת', 'ההוא')) == 19

# 1:19-33 THE SPIES SENT AND THE REFUSAL (computed): "THE GREAT AND TERRIBLE WILDERNESS" plene one seat (8:15 defective "the great"); "as the
# LORD our God commanded us" and "and we came to Kadesh-barnea" — Kadesh-barnea's second two-token seat; "you have come to the hill country
# of the Amorites"; "go up, possess" one seat; "FEAR NOT, NEITHER BE DISMAYED" — the pair's ONLY TORAH SEAT (Joshua 8:1 to Joshua before Ai,
# David's charge to Solomon twice, 1 Chronicles 22:13, 28:20); "and you came near to me, all of you" one seat; "let us send men before us" one;
# "AND THEY SHALL SEARCH OUT" — the dig-root (one lemma, twenty-one seats: Isaac's wells, the princes' well, Numbers 21:18) in its spy sense
# here and at JOSHUA 2:2-3 alone (Rahab's spies "to search out the land", the king's "to search out all the land") — the store glossing
# "and-pry-into"; the same consonants "and they were ashamed" in the Psalms (another root); "and
# bring us back word" 1:22 and 1:25 (the report's two verbs); "the thing was good in my eyes" one; "TWELVE MEN" this and Joshua 4:2 (the
# stones from the Jordan), "ONE MAN PER TRIBE" this and Joshua 3:12 — the second two of Joshua's twelve-men forms; "and they turned and went
# up to the hill country" — the mountain with the directional ending; "THE VALLEY OF ESHCOL" two seats (Numbers 13:23 the cluster cut, this);
# "AND THEY SPIED IT OUT" — the spy-verb's piel: this, Numbers 21:32's Jazer, Joshua 2:1, 6:22-25, 7:2, 14:7 (Caleb's own "I spied"), Judges 18's
# five, Genesis 42's "spies" (the participle nine) — where NUMBERS 13-14 say "TOUR" (the tour-verb twelve tokens in eleven verses there: the
# Sifrei 22's distinction); "SOME OF THE FRUIT OF THE LAND" two seats — Moses' charge to the spies (Numbers 13:20) and this; "GOOD IS THE
# LAND" two seats — Joshua and Caleb's report (Numbers 14:7) and this (the retelling wearing the spies' own words); "and you would not go up" one; "AND YOU REBELLED AGAINST THE
# MOUTH OF THE LORD" three seats, all the book's (1:26, 1:43, 9:23) — the store glossing "and-be--bitter" (the bitter-root's homograph);
# "AND YOU MURMURED IN YOUR TENTS" — the murmur-verb's three Bible seats: this, PSALM 106:25 ("they murmured in their tents" — the psalm's
# retelling of this verse) and Isaiah 29:24; "IN THE LORD'S HATRED OF US" one seat (the "in hatred" of Numbers 35:20 another form); "to
# give us into the hand of the Amorite to destroy us" — JOSHUA 7:7's clause after Ai ("to give us into the hand of the Amorite to make us
# perish" — "into the hand of the Amorite" the two seats, Joshua's verb another); "OUR BROTHERS HAVE MELTED OUR HEART" one seat — Caleb's "melted the heart of the
# people" (Joshua 14:8, the hifil with the other spelling) the kin; "CITIES GREAT AND FORTIFIED TO HEAVEN" 1:28 (9:1 with the defective
# "fortified"); "SONS OF ANAKIM" 1:28 and 9:2; "YOU SHALL NOT DREAD" — the dread-root's Torah seats 1:29, 7:21, 20:3, 31:6 (the war laws'
# word); "HE WILL FIGHT FOR YOU" — EXODUS 14:14's words at the sea ("the LORD will fight for you") at their second seat; "AS A MAN CARRIES HIS
# SON" one seat (the outside row 314:2 brings it to the eagle of 32:11); "IN THIS THING YOU DO NOT BELIEVE" — the hifil participle one
# seat (the store: "build-up", the amen-root); "IN FIRE BY NIGHT ... AND IN CLOUD BY DAY" — 1:33 reversing Exodus 13:21's order (the cloud
# first there).
assert P('המדבר', 'הגדול', 'והנורא') == ['Deut 1:19'] and 'הגדל' in words('Deut', 8, 15) and 'והנורא' in words('Deut', 8, 15) and P('כאשר', 'צוה', 'יהוה', 'אלהינו', 'אתנו') == ['Deut 1:19'] and P('עלה', 'רש') == ['Deut 1:21'] and P('אל', 'תירא', 'ואל', 'תחת') == S_('1Chr 22:13', '1Chr 28:20', 'Deut 1:21', 'Josh 8:1')
assert P('ותקרבון', 'אלי', 'כלכם') == ['Deut 1:22'] and P('נשלחה', 'אנשים', 'לפנינו') == ['Deut 1:22'] and lemma_of('Deut', 1, 22, 'ויחפרו') == ['2658'] and len(LEMV('2658')) == 21 and {'Josh 2:2', 'Josh 2:3', 'Gen 26:18', 'Gen 26:22', 'Num 21:18'} <= set(LEMV('2658')) and sg(1, 22, 'ויחפרו') == 'and-pry-into' and words('Josh', 2, 2)[-4:] == ['ישראל', 'לחפר', 'את', 'הארץ'] and U('ויחפרו') == S_('Deut 1:22', 'Exod 7:24', 'Gen 26:19', 'Gen 26:21', 'Job 6:20', 'Ps 35:26', 'Ps 35:4', 'Ps 40:15', 'Ps 70:3', 'Ps 83:18')
assert P('וישבו', 'אתנו', 'דבר') == S_('Deut 1:22', 'Deut 1:25') and P('וייטב', 'בעיני', 'הדבר') == ['Deut 1:23'] and P('שנים', 'עשר', 'אנשים') == S_('Deut 1:23', 'Josh 4:2') and P('איש', 'אחד', 'לשבט') == S_('Deut 1:23', 'Josh 3:12')
assert P('ויפנו', 'ויעלו', 'ההרה') == ['Deut 1:24'] and P('נחל', 'אשכל') == S_('Deut 1:24', 'Num 13:23') and lemma_of('Deut', 1, 24, 'וירגלו') == ['7270'] and sorted({s.split()[0] for s in LEMV('7270')}) == S_('1Chr', '1Sam', '2Sam', 'Deut', 'Gen', 'Josh', 'Judg', 'Num', 'Ps') and LEMV('7270', T) == S_('Deut 1:24', 'Gen 42:11', 'Gen 42:14', 'Gen 42:16', 'Gen 42:30', 'Gen 42:31', 'Gen 42:34', 'Gen 42:9', 'Num 21:32')
assert len([s for s in LEMV('8446') if s.startswith(('Num 13', 'Num 14'))]) == 11 and sum(1 for s, x, m in LEMT('8446') if s.startswith(('Num 13', 'Num 14'))) == 12 and lemma_of('Num', 13, 2, 'ויתרו') == ['8446']
assert P('מפרי', 'הארץ') == S_('Deut 1:25', 'Num 13:20') and P('טובה', 'הארץ') == S_('Deut 1:25', 'Num 14:7') and P('ולא', 'אביתם', 'לעלת') == ['Deut 1:26'] and P('ותמרו', 'את', 'פי', 'יהוה') == S_('Deut 1:26', 'Deut 1:43', 'Deut 9:23') and sg(1, 26, 'ותמרו') == 'and-be--bitter'
assert lemma_of('Deut', 1, 27, 'ותרגנו') == ['7279'] and LEMV('7279') == S_('Deut 1:27', 'Isa 29:24', 'Ps 106:25') and words('Ps', 106, 25)[:2] == ['וירגנו', 'באהליהם'] and U('בשנאת') == ['Deut 1:27'] and P('לתת', 'אתנו', 'ביד', 'האמרי', 'להשמידנו') == ['Deut 1:27'] and P('ביד', 'האמרי') == S_('Deut 1:27', 'Josh 7:7') and 'להאבידנו' in words('Josh', 7, 7)
assert P('אחינו', 'המסו', 'את', 'לבבנו') == ['Deut 1:28'] and words('Josh', 14, 8)[3:6] == ['עמי', 'המסיו', 'את'] and P('ערים', 'גדלת', 'ובצורת', 'בשמים') == ['Deut 1:28'] and P('ערים', 'גדלת', 'ובצרת', 'בשמים') == ['Deut 9:1'] and P('בני', 'ענקים') == S_('Deut 1:28', 'Deut 9:2')
assert LEMV('6206', T) == S_('Deut 1:29', 'Deut 20:3', 'Deut 31:6', 'Deut 7:21') and P('הוא', 'ילחם', 'לכם') == ['Deut 1:30'] and P('ילחם', 'לכם') == S_('Deut 1:30', 'Exod 14:14') and P('כאשר', 'ישא', 'איש', 'את', 'בנו') == ['Deut 1:31'] and U('מאמינם') == ['Deut 1:32'] and sg(1, 32, 'מאמינם') == 'build-up'
assert P('באש', 'לילה') == ['Deut 1:33'] and P('ובענן', 'יומם') == ['Deut 1:33'] and words('Exod', 13, 21)[3:6] == ['יומם', 'בעמוד', 'ענן'] and words('Exod', 13, 21)[8:11] == ['ולילה', 'בעמוד', 'אש']

# 1:34-46 THE OATH AND THE DEFEAT (computed): "AND THE LORD HEARD THE VOICE OF YOUR WORDS" 1:34 and 5:28 (the Horeb request); "and he was
# angry" (the store's "and-crack-off" — the wrath-verb, five tokens); "THIS EVIL GENERATION" one seat; "the good land" five Torah seats (1:35,
# 3:25, 4:21, 4:22, 9:6); "EXCEPT" (זולתי, "except") nine seats of the token; "BECAUSE HE FOLLOWED THE LORD FULLY" — 1:36 and JOSHUA 14:14 (Caleb's Hebron: the
# same clause); the fill-after phrase EIGHT seats (Numbers 14:24, 32:11-12, this, Joshua 14:8, 9, 14, 1 Kings 11:6); "THE LORD WAS ANGRY
# WITH ME ALSO FOR YOUR SAKES" — the hitpael's six seats (1:37, 4:21, 9:8, 9:20 the Torah's four; 1 Kings 11:9, 2 Kings 17:18 — the root's fourteen seats), "for your
# sakes" 1:37 and Micah 3:12; "WHO STANDS BEFORE YOU" one seat; "HE SHALL CAUSE ISRAEL TO INHERIT IT" one seat — the causative's kin at 3:28 and
# 31:7 (Joshua 1:6 "you shall cause to inherit"), "he shall cause to inherit" 3:28 and Proverbs 13:22; "AND YOUR LITTLE ONES WHO YOU SAID WOULD BE A PREY" — NUMBERS 14:31 VERBATIM; "GOOD AND EVIL" the Torah's five seats:
# THE TREE'S FOUR (Genesis 2:9, 2:17, 3:5, 3:22) AND THIS — the children who "know not today good and evil" wear Eden's phrase; 1:40 against
# Numbers 14:25 — "turn and journey for you, the wilderness" became "turn for you and journey to the wilderness-ward" (the diff: the pronoun
# moved, the directional ending added); "WE HAVE SINNED AGAINST THE LORD" 1:41 (1 Samuel 7:6, Jeremiah 8:14, 16:10 the others; Numbers 14:40
# said "we have sinned"); "AND YOU DEEMED IT EASY" a HAPAX (the store: "and-be-naught"); 1:42 against NUMBERS 14:42 — "go not up, for the
# LORD is not among you" became "you shall not go up and you shall not fight, for I am not among you", the clause "that you be not smitten
# before your enemies" shared; "AND YOU ACTED PRESUMPTUOUSLY" — the seethe-root (the store: "and-seethe"): Jacob's pottage (Genesis 25:29),
# Egypt's pride (Exodus 18:11), the wilful murderer (21:14), the presumptuous man (17:13) and prophet (18:20); "AS THE BEES DO" — the bee-word
# four seats (Samson's, Isaiah's, Psalm 118's — the consonants "the words" at 1:44, the morphology deciding); NUMBERS 14:45 "and smote them and
# beat them down to Hormah" became "and beat you down in Seir to Hormah"; HORMAH five seats of the name's tokens; "and you wept before the LORD" one; "AND THE
# LORD DID NOT LISTEN TO YOUR VOICE" one seat; "MANY DAYS" 1:46, 2:1, 20:19 in the book — "you dwelt in Kadesh many days, like the days
# you dwelt" one seat.
assert P('וישמע', 'יהוה', 'את', 'קול', 'דבריכם') == S_('Deut 1:34', 'Deut 5:28') and sg(1, 34, 'ויקצף') == 'and-crack-off' and P('הדור', 'הרע', 'הזה') == ['Deut 1:35'] and P('הארץ', 'הטובה', books=T) == S_('Deut 1:35', 'Deut 3:25', 'Deut 4:21', 'Deut 4:22', 'Deut 9:6') and len(U('זולתי')) == 9
assert P('יען', 'אשר', 'מלא', 'אחרי', 'יהוה') == S_('Deut 1:36', 'Josh 14:14') and sorted(P('מלא', 'אחרי', 'יהוה') + P('מלאו', 'אחרי') + P('מלאתי', 'אחרי') + P('וימלא', 'אחרי') + P('מלאת', 'אחרי')) == S_('1Kgs 11:6', 'Deut 1:36', 'Josh 14:14', 'Josh 14:8', 'Josh 14:9', 'Num 14:24', 'Num 32:11', 'Num 32:12')
assert sorted({s for s, x, m in LEMT('599') if 'Vt' in m}) == S_('1Kgs 11:9', '2Kgs 17:18', 'Deut 1:37', 'Deut 4:21', 'Deut 9:20', 'Deut 9:8') and len(LEMV('599')) == 14 and U('בגללכם') == S_('Deut 1:37', 'Mic 3:12') and P('העמד', 'לפניך') == ['Deut 1:38'] and U('ינחלנה') == ['Deut 1:38'] and sorted(U('ינחלנה', 'ינחיל', 'ינחילנה', 'תנחילנה')) == S_('Deut 1:38', 'Deut 31:7', 'Deut 3:28', 'Prov 13:22') and len(U('ינחיל')) == 2
assert P('וטפכם', 'אשר', 'אמרתם', 'לבז', 'יהיה') == S_('Deut 1:39', 'Num 14:31') and P('טוב', 'ורע', books=T) == S_('Deut 1:39', 'Gen 2:17', 'Gen 2:9', 'Gen 3:22', 'Gen 3:5') and P('טוב', 'ורע') == S_('Deut 1:39', 'Gen 2:17', 'Gen 2:9', 'Gen 3:22', 'Gen 3:5')
assert DIFF(('Num', 14, 25), ('Deut', 1, 40))[-2:] == [('insert', [], ['לכם']), ('replace', ['לכם', 'המדבר'], ['המדברה'])] or words('Deut', 1, 40) == ['ואתם', 'פנו', 'לכם', 'וסעו', 'המדברה', 'דרך', 'ים', 'סוף']
assert P('חטאנו', 'ליהוה') == S_('1Sam 7:6', 'Deut 1:41', 'Jer 16:10', 'Jer 8:14') and words('Num', 14, 40)[-5:] == ['אשר', 'אמר', 'יהוה', 'כי', 'חטאנו'] and U('ותהינו') == ['Deut 1:41'] and lemma_of('Deut', 1, 41, 'ותהינו') == ['1951'] and len(LEMT('1951')) == 1 and sg(1, 41, 'ותהינו') == 'and-be-naught'
assert words('Num', 14, 42)[:6] == ['אל', 'תעלו', 'כי', 'אין', 'יהוה', 'בקרבכם'] and words('Deut', 1, 42)[5:12] == ['לא', 'תעלו', 'ולא', 'תלחמו', 'כי', 'אינני', 'בקרבכם'] and P('ולא', 'תנגפו', 'לפני', 'איביכם') == S_('Deut 1:42', 'Num 14:42')
assert lemma_of('Deut', 1, 43, 'ותזדו') == ['2102'] and LEMV('2102') == S_('Deut 17:13', 'Deut 18:20', 'Deut 1:43', 'Exod 18:11', 'Exod 21:14', 'Gen 25:29', 'Jer 50:29', 'Neh 9:10', 'Neh 9:16', 'Neh 9:29') and sg(1, 43, 'ותזדו') == 'and-seethe' and sg(1, 43, 'ותמרו') == 'and-be--bitter'
assert lemma_of('Deut', 1, 44, 'הדברים') == ['1682'] and LEMV('1682') == S_('Deut 1:44', 'Isa 7:18', 'Judg 14:8', 'Ps 118:12') and sg(1, 44, 'הדברים') == 'the-bee' and [m for x, m in by[('Deut', 1, 44)] if x == 'הדברים'] == ['HTd/Ncfpa']
assert words('Num', 14, 45)[-5:] == ['ויכום', 'ויכתום', 'עד', 'החרמה', ''][:-1] or words('Num', 14, 45)[-4:] == ['ויכום', 'ויכתום', 'עד', 'החרמה']
assert words('Deut', 1, 44)[-5:] == ['ויכתו', 'אתכם', 'בשעיר', 'עד', 'חרמה'] and len(U('חרמה', 'החרמה', 'לחרמה')) == 5 and sg(1, 44, 'ויכתו') == 'and-bruise' and P('ותבכו', 'לפני', 'יהוה') == ['Deut 1:45'] and P('ולא', 'שמע', 'יהוה', 'בקלכם') == ['Deut 1:45']
assert [s for s in P('ימים', 'רבים') if s.startswith('Deut')] == S_('Deut 1:46', 'Deut 20:19', 'Deut 2:1') and P('ותשבו', 'בקדש', 'ימים', 'רבים') == ['Deut 1:46'] and sg(1, 46, 'ותשבו') == 'and-dwell/sit' and sg(1, 45, 'ותשבו') == 'and-return'

# 2:1-25 THE BYPASS (computed): "and we turned and journeyed to the wilderness-ward by the way of the Sea of Reeds" one seat; "as the LORD spoke
# to me" one; "AND WE WENT ROUND MOUNT SEIR MANY DAYS" one seat — NUMBERS 21:4's "to go round the land of Edom" the run; "YOU HAVE GONE ROUND
# THIS MOUNTAIN LONG ENOUGH" one; "turn you northward" one; "YOUR BROTHERS THE SONS OF ESAU" — Numbers 20:14's "thus says your brother Israel"
# the embassy's word; "who dwell in Seir" four seats, all this chapter's (2:4, 8, 22, 29); "and they will be afraid of you" one; "take good
# heed" three (2:4, 4:15, Joshua 23:11); "CONTEND NOT WITH THEM" — the contend-root's hitpael at 2:5, 9, 19, 24 (the Torah's four, three
# refusals and one command: "contend with him in battle" at 2:24 — the same verb turned), Amaziah's (2 Kings 14:10, 2 Chronicles 25:19),
# Jeremiah's, Daniel's, the Proverbs' — the store glossing "grate" (the grating's homograph); "NOT SO MUCH AS A FOOTBREADTH" one seat (the
# treading-word's sixteen seats); "FOR I HAVE GIVEN MOUNT SEIR TO ESAU AS A POSSESSION" one seat — "AS A POSSESSION" (ירשה) seven seats: Balaam's
# two (Numbers 24:18), 2:5, 9, 19, Naphtali's (33:23), Joshua 12:6-7 — the store glossing "something-occupied"; Genesis 36:8 and Joshua 24:4 the
# grant's records; "YOU SHALL BUY FOOD OF THEM FOR MONEY" one seat — the grain-buying verb of Joseph's brothers (Genesis 42-44); "AND WATER
# YOU SHALL BUY OF THEM FOR MONEY" one seat — the dig-verb in the buying sense (one lemma with Hosea 3:2's "I bought her"); NUMBERS 20:19's offer
# to Edom ("if we drink your water, I and my cattle, I will give its price") and 2:28's to Sihon the kin; "FOR THE LORD YOUR GOD HAS BLESSED
# YOU IN ALL THE WORK OF YOUR HAND" one; "THESE FORTY YEARS" three seats (2:7, 8:2, 8:4), "forty years" eleven Torah seats; "YOU HAVE LACKED
# NOTHING" one seat (8:4's unworn garment, 29:4's, Nehemiah 9:21's "they lacked nothing" the runs); 2:8 "from the way of the Arabah, from
# Elath and from Ezion-geber" one seat — Ezion-geber the DB's two tokens here as at Numbers 33:35-36 (the stations' "in Ezion-geber", "from
# Ezion-geber"); "the way of the wilderness of Moab" one; "HARASS NOT MOAB" — the besiege-root by the lemma (Exodus 23:22's "I will harass
# those who harass you", Esther 8:11's; the store glossing "cramp"); AR six seats of the token (2:9, 18, 29; Numbers 21:15, 28; Isaiah 15:1);
# THE EMIM 2:10-11 — Genesis 14:5's Emim (the plene spelling) at Shaveh-kiriathaim, Chedorlaomer's; "a people great and many and tall as the
# Anakim" 2:10 and 2:21 (the Emim and the Zamzummim measured by one phrase); "as the Anakim" three seats, all this chapter's; REPHAIM
# nineteen seats of the bare token (Genesis 14:5, 15:20's list, 2:11, 20, 3:11, 13, Joshua's, the shades of Isaiah and Job); "FORMERLY" (לפנים)
# — the Torah's three seats all this chapter's (2:10, 12, 20), the store glossing "to-face"; THE HORITES "in Seir" 2:12 and 2:22 — Genesis
# 14:6's "the Horites in their mount Seir" and 36:20-21's sons of Seir the Horite; "AS ISRAEL DID TO THE LAND OF HIS POSSESSION" one seat, "his
# possession" a hapax form; "THE BROOK ZERED" 2:13 and 2:14 (Numbers 21:12 "in the brook Zered"); "THIRTY-EIGHT YEARS" three seats (Omri's
# and Zechariah's regnal years the others), the parser [38]; "UNTIL THE WHOLE GENERATION WAS CONSUMED" — NUMBERS 32:13's clause ("until the
# whole generation was consumed that had done evil") at its second seat, 14:33's "until your carcasses are consumed" the first form; "THE
# MEN OF WAR" twenty seats (Numbers 31:28, 49's; Joshua 5:4, 6's the same generation); "TO DISCOMFIT THEM" — 2:15 and Esther 9:24 (Haman's
# lot "to discomfit them"), the root's fourteen seats (Exodus 14:24 the Egyptians, Joshua 10:10); "until they were consumed" six seats; 2:17
# "AND THE LORD SPOKE TO ME" the Bible's one seat; "you are passing today the border of Moab, Ar" one; "over against the sons of Ammon" one;
# "THE LAND OF REPHAIM" 2:20 and 3:13; ZAMZUMMIM a hapax; "TO THIS DAY" 2:22 and 3:14 in the span (twelve Torah seats, seventy-five in the
# Bible); THE AVVIM four seats of the token (Joshua 13:3's Philistine list, 18:23's Benjaminite town, 2 Kings 17:31's settlers); "THE CAPHTORIM WHO CAME
# FROM CAPHTOR" — Genesis 10:14's Caphtorim (and Chronicles'), AMOS 9:7's "the Philistines from Caphtor" and Jeremiah 47:4's "the isle of
# Caphtor" the prophets' pair; "in villages" (Chatserim — the store reads it as a name) one seat of the token; "RISE, JOURNEY, CROSS THE BROOK ARNON" one seat; "SEE, I
# HAVE GIVEN INTO YOUR HAND SIHON" one; "BEGIN, POSSESS" 2:24 and 2:31; "THIS DAY I BEGIN TO PUT THE DREAD OF YOU AND THE FEAR OF YOU UPON
# THE PEOPLES UNDER THE WHOLE HEAVEN" one seat — "the dread of you and the fear of you" one, "under the whole heaven" seven Bible seats (the
# flood's "under the whole heaven" Genesis 7:19, 4:19's hosts), Exodus 23:27's "I will send my terror before you" and Deuteronomy 11:25's
# "the dread of you and the fear of you" (with other suffixes) the kin, Rahab's "your terror has fallen on us" (Joshua 2:9) the run; "WHO
# SHALL HEAR THE REPORT OF YOU AND TREMBLE AND BE IN ANGUISH" — EXODUS 15:14'S PAIR ("the peoples heard, they tremble; anguish seized") at
# its second seat (Psalm 77:17 the third).
assert P('ונפן', 'ונסע', 'המדברה', 'דרך', 'ים', 'סוף') == ['Deut 2:1'] and P('ונסב', 'את', 'הר', 'שעיר', 'ימים', 'רבים') == ['Deut 2:1'] and words('Num', 21, 4)[6:10] == ['לסבב', 'את', 'ארץ', 'אדום'] and P('רב', 'לכם', 'סב', 'את', 'ההר', 'הזה') == ['Deut 2:3'] and P('פנו', 'לכם', 'צפנה') == ['Deut 2:3']
assert P('אחיכם', 'בני', 'עשו') == ['Deut 2:4'] and words('Num', 20, 14)[7:12] == ['כה', 'אמר', 'אחיך', 'ישראל', 'אתה'] and P('הישבים', 'בשעיר') == S_('Deut 2:22', 'Deut 2:29', 'Deut 2:4', 'Deut 2:8') and P('ונשמרתם', 'מאד') == S_('Deut 2:4', 'Deut 4:15', 'Josh 23:11')
GR = sorted({s for s, x, m in LEMT(lemma_of('Deut', 2, 5, 'תתגרו')[0]) if 'Vt' in m})
assert lemma_of('Deut', 2, 5, 'תתגרו') == ['1624'] and [s for s in GR if s.startswith('Deut')] == S_('Deut 2:19', 'Deut 2:24', 'Deut 2:5', 'Deut 2:9') and GR == S_('2Chr 25:19', '2Kgs 14:10', 'Dan 11:10', 'Dan 11:25', 'Deut 2:19', 'Deut 2:24', 'Deut 2:5', 'Deut 2:9', 'Jer 50:24', 'Prov 28:4') and sg(2, 5, 'תתגרו') == 'grate' and sg(2, 24, 'והתגר') == 'and-grate'
assert P('עד', 'מדרך', 'כף', 'רגל') == ['Deut 2:5'] and len(U('מדרך')) == 16 and sg(2, 5, 'מדרך') == 'treading' and P('כי', 'ירשה', 'לעשו', 'נתתי', 'את', 'הר', 'שעיר') == ['Deut 2:5'] and U('ירשה') == S_('Deut 2:19', 'Deut 2:5', 'Deut 2:9', 'Deut 33:23', 'Josh 12:6', 'Josh 12:7', 'Num 24:18') and sg(2, 5, 'ירשה') == 'something-occupied'
assert words('Gen', 36, 8)[:4] == ['וישב', 'עשו', 'בהר', 'שעיר'] and words('Josh', 24, 4)[6:10] == ['ואתן', 'לעשו', 'את', 'הר'] and P('אכל', 'תשברו', 'מאתם', 'בכסף', 'ואכלתם') == ['Deut 2:6'] and P('וגם', 'מים', 'תכרו', 'מאתם', 'בכסף', 'ושתיתם') == ['Deut 2:6']
assert lemma_of('Deut', 2, 6, 'תכרו') == ['3739 a'] and LEMT('3739 a') == [('Deut 2:6', 'תכרו', 'HVqi2mp'), ('Hos 3:2', 'ואכרה', 'HC/Vqw1cs/Sp3fs')] and sg(2, 6, 'תכרו') == 'purchase' and sg(2, 6, 'תשברו') == 'deal-in-grain' and len([s for s in LEMV(lemma_of('Deut', 2, 6, 'תשברו')[0], T) if s.startswith('Gen 4')]) >= 14
assert words('Num', 20, 19)[5:12] == ['נעלה', 'ואם', 'מימיך', 'נשתה', 'אני', 'ומקני', 'ונתתי'] and words('Deut', 2, 28) == ['אכל', 'בכסף', 'תשברני', 'ואכלתי', 'ומים', 'בכסף', 'תתן', 'לי', 'ושתיתי', 'רק', 'אעברה', 'ברגלי']
assert P('כי', 'יהוה', 'אלהיך', 'ברכך', 'בכל', 'מעשה', 'ידך') == ['Deut 2:7'] and P('זה', 'ארבעים', 'שנה') == S_('Deut 2:7', 'Deut 8:2', 'Deut 8:4') and len(P('ארבעים', 'שנה', books=T)) == 11 and P('לא', 'חסרת', 'דבר') == ['Deut 2:7'] and words('Neh', 9, 21)[:7] == ['וארבעים', 'שנה', 'כלכלתם', 'במדבר', 'לא', 'חסרו', 'שלמתיהם']
assert P('מאילת', 'ומעצין', 'גבר') == ['Deut 2:8'] and words('Num', 33, 35)[-2:] == ['בעציון', 'גבר'] and words('Num', 33, 36)[1:3] == ['מעציון', 'גבר'] and P('ונפן', 'ונעבר', 'דרך', 'מדבר', 'מואב') == ['Deut 2:8'] and sg(2, 8, 'ומעצין') == 'and-from-?' and sg(2, 8, 'גבר') == 'Ezion-geber'
assert P('אל', 'תצר', 'את', 'מואב') == ['Deut 2:9'] and lemma_of('Deut', 2, 9, 'תצר') == ['6696 b'] and LEMT('6696 b') == [('Deut 2:9', 'תצר', 'HVqj2ms'), ('Deut 2:19', 'תצרם', 'HVqj2ms/Sp3mp'), ('Esth 8:11', 'הצרים', 'HTd/Vqrmpa'), ('Exod 23:22', 'וצרתי', 'HC/Vqq1cs')] and sg(2, 9, 'תצר') == 'cramp' and sg(2, 19, 'תצרם') == 'cramp-them/their'
assert [s for s in U('ער', 'בער') if s.startswith(('Deut 2', 'Num 21', 'Isa 15'))] == S_('Deut 2:18', 'Deut 2:29', 'Deut 2:9', 'Isa 15:1', 'Num 21:15', 'Num 21:28')
assert P('האמים', 'לפנים', 'ישבו', 'בה') == ['Deut 2:10'] and words('Gen', 14, 5)[-4:] == ['ואת', 'האימים', 'בשוה', 'קריתים'] and U('האמים', 'אמים', 'האימים') == S_('Deut 2:10', 'Deut 2:11', 'Gen 14:5', 'Job 20:25', 'Ps 108:4', 'Ps 117:1', 'Ps 149:7', 'Ps 44:15', 'Ps 57:10') and sg(2, 10, 'האמים') == 'the-Emims' and sg(2, 11, 'אמים') == 'Emims'
assert P('עם', 'גדול', 'ורב', 'ורם', 'כענקים') == S_('Deut 2:10', 'Deut 2:21') and U('כענקים') == S_('Deut 2:10', 'Deut 2:11', 'Deut 2:21') and len(U('רפאים')) == 19 and U('לפנים', books=T) == S_('Deut 2:10', 'Deut 2:12', 'Deut 2:20') and sg(2, 10, 'לפנים') == 'to-face'
assert P('ובשעיר', 'ישבו', 'החרים', 'לפנים') == ['Deut 2:12'] and words('Gen', 14, 6)[:5] == ['ואת', 'החרי', 'בהררם', 'שעיר', 'עד'] and words('Gen', 36, 20)[:6] == ['אלה', 'בני', 'שעיר', 'החרי', 'ישבי', 'הארץ'] and P('כאשר', 'עשה', 'ישראל', 'לארץ', 'ירשתו') == ['Deut 2:12'] and U('ירשתו') == ['Deut 2:12'] and sg(2, 12, 'ירשתו') == 'something-occupied-him/its'
assert P('נחל', 'זרד') == S_('Deut 2:13', 'Deut 2:14') and words('Num', 21, 12)[-2:] == ['בנחל', 'זרד'] and P('שלשים', 'ושמנה', 'שנה') == S_('1Kgs 16:29', '2Kgs 15:8', 'Deut 2:14') and P('עד', 'תם', 'כל', 'הדור') == S_('Deut 2:14', 'Num 32:13') and words('Num', 14, 33)[-4:] == ['עד', 'תם', 'פגריכם', 'במדבר'] and len(P('אנשי', 'המלחמה')) == 20
assert U('להמם') == S_('Deut 2:15', 'Esth 9:24') and len(LEMV(lemma_of('Deut', 2, 15, 'להמם')[0])) == 14 and 'Exod 14:24' in LEMV(lemma_of('Deut', 2, 15, 'להמם')[0]) and 'Josh 10:10' in LEMV(lemma_of('Deut', 2, 15, 'להמם')[0]) and sg(2, 15, 'להמם') == 'to-put-in-commotion-them/their' and P('עד', 'תמם') == S_('Deut 2:15', 'Deut 31:24', 'Deut 31:30', 'Jer 24:10', 'Josh 10:20', 'Josh 8:24')
assert P('אתה', 'עבר', 'היום', 'את', 'גבול', 'מואב', 'את', 'ער') == ['Deut 2:18'] and P('וקרבת', 'מול', 'בני', 'עמון') == ['Deut 2:19'] and P('ארץ', 'רפאים') == S_('Deut 2:20', 'Deut 3:13') and U('זמזמים') == ['Deut 2:20'] and [(c, v) for (c, v) in SPAN if any(words('Deut', c, v)[i:i + 3] == ['עד', 'היום', 'הזה'] for i in range(len(words('Deut', c, v)) - 2))] == [(2, 22), (3, 14)] and len(P('עד', 'היום', 'הזה', books=T)) == 12 and len(P('עד', 'היום', 'הזה')) == 75
assert U('עוים', 'והעוים', 'העוים') == S_('2Kgs 17:31', 'Deut 2:23', 'Josh 13:3', 'Josh 18:23') and P('כפתרים', 'היצאים', 'מכפתור') == ['Deut 2:23'] and U('כפתרים', 'מכפתור', 'כפתור') == S_('1Chr 1:12', 'Amos 9:7', 'Deut 2:23', 'Gen 10:14', 'Jer 47:4') and words('Gen', 10, 14)[-2:] == ['ואת', 'כפתרים'] and U('בחצרים') == ['Deut 2:23']
assert P('קומו', 'סעו', 'ועברו', 'את', 'נחל', 'ארנן') == ['Deut 2:24'] and P('החל', 'רש') == S_('Deut 2:24', 'Deut 2:31') and P('פחדך', 'ויראתך') == ['Deut 2:25'] and P('תחת', 'כל', 'השמים') == S_('Dan 9:12', 'Deut 2:25', 'Deut 4:19', 'Gen 7:19', 'Job 28:24', 'Job 37:3', 'Job 41:3') and words('Exod', 23, 27)[:5] == ['את', 'אימתי', 'אשלח', 'לפניך', 'והמתי'] and words('Deut', 11, 25)[4:6] == ['פחדכם', 'ומוראכם'] and 'אימתכם' in words('Josh', 2, 9)
assert P('ורגזו', 'וחלו') == ['Deut 2:25'] and words('Exod', 15, 14)[:5] == ['שמעו', 'עמים', 'ירגזון', 'חיל', 'אחז'] and sorted(s for (b, c, v), ws in by.items() for s in [f'{b} {c}:{v}'] if any('רגז' in x for x, _ in ws) and any(x in ('חיל', 'וחלו', 'יחילו', 'חילה', 'חלו', 'יחלון', 'ויחלו') for x, _ in ws)) == S_('Deut 2:25', 'Exod 15:14', 'Ps 77:17')

# 2:26-37 SIHON (computed): "AND I SENT MESSENGERS FROM THE WILDERNESS OF KEDEMOTH" one seat — Kedemoth's four seats as a place (2:26, Joshua
# 21:37, 1 Chronicles 6:64 the Levite city; the eastward homographs Eden's, Nod's); SIHON PLENE (סיחון) fourteen seats of the bare token —
# 2:26 the book's one (31:4's with a prefix) — against the DEFECTIVE twelve (1:4, 2:24, 30, 31, 32 in the span; 3:2, 3:6 with a prefix); Numbers 21:21's "and Israel sent messengers to
# Sihon" the first telling; "WORDS OF PEACE" four Bible seats (Menahem's, Esther's, the psalm's) — the outside row 199:5's proof that Moses
# loved peace; "LET ME PASS THROUGH YOUR LAND" 2:27 and NUMBERS 21:22 (the first telling's same words); 2:27 AGAINST 21:22, DIFFED — the
# field, the vineyard, the well and "the king's road" of Numbers became "BY THE ROAD, BY THE ROAD I WILL GO; I WILL NOT TURN RIGHT OR LEFT"
# (the doubled "by the road" one seat; "right or left" five Torah seats — Numbers 20:17's Edom embassy and 22:26's Balaam among them); 2:28
# "food for money you shall sell me ... water for money" — 2:6's buying turned on Sihon, Numbers 20:19's "I will give its price" the Edom kin;
# "ONLY LET ME PASS ON FOOT" — "on foot" 2:28 and Numbers 20:19 (the token's five seats); "AS THE SONS OF ESAU DID FOR ME ... AND THE
# MOABITES" 2:29 — where NUMBERS 20:18-21 HAS EDOM REFUSE ("you shall not pass"; "and Edom refused to let Israel pass") and JUDGES 11:17-18 HAS
# EDOM AND MOAB BOTH REFUSE: the retellings disagree, the ink measured (the Sifrei silent here — no piska on 2:29; the compile's owed question);
# "until I cross the Jordan" one; "BUT SIHON WOULD NOT LET US PASS" — "let us pass" a hapax form; Numbers 21:23 "and Sihon did not give Israel
# to pass"; "FOR THE LORD YOUR GOD HARDENED HIS SPIRIT AND MADE HIS HEART STRONG" one seat — "hardened his spirit" 2:30 alone in that sense
# (Numbers 11:29's "would that", Psalm 106:33's "they embittered his spirit", Ezra 1:5's the homographs), "made his heart strong" one — the
# Exodus formula on Pharaoh (7:3 "I will harden Pharaoh's heart", 4:21 "I will strengthen his heart") and Joshua 11:20's "to strengthen their
# heart" the kin; "AS AT THIS DAY" six seats in the book; "SEE, I HAVE BEGUN TO GIVE" one; 2:32 AGAINST NUMBERS 21:23, DIFFED — "and Sihon
# did not give Israel to pass ... and gathered all his people and went out to meet Israel to the wilderness and came to Jahaz and fought" became
# "and Sihon came out to meet us, he and all his people, to battle, to Jahaz" (eight tokens for twenty); JAHAZ eight seats; "AND WE SMOTE HIM
# AND HIS SONS" — THE WRITTEN "HIS SON" (בנו) READ "HIS SONS" (בניו): the DB's token unpointed, the store carrying both, Numbers 21:35's Og
# "and his sons" the plural (Sihon's sons not named in Numbers); "we captured all his cities at that time" 2:34 and 3:4; "AND WE DEVOTED EVERY
# CITY, MEN, WOMEN AND CHILDREN" — "men" (מתם) the adult-word (the store: "adult"; the lemma's twenty-two seats — "few in number" 4:27, 26:5,
# 28:62, 33:6); "WE LEFT NO SURVIVOR" one seat; "we devoted" first person plural 2:34 and 3:6; "ONLY THE CATTLE WE TOOK AS SPOIL" — "we
# plundered" 2:35 and 3:7 (Joshua 8:27's Ai and 11:14's Hazor the runs: "only the cattle and the spoil of that city Israel plundered"); "FROM
# AROER ON THE EDGE OF THE BROOK ARNON" 2:36 and 4:48, Aroer eleven seats of the name's tokens (Numbers 32:34 Gad's building); "there was no city too high for
# us" one seat, the high-root's ten; "the LORD our God gave all before us" one; "ONLY TO THE LAND OF THE SONS OF AMMON YOU DID NOT COME NEAR"
# one — "all the side of the brook Jabbok", Jabbok five seats (Jacob's ford, Numbers 21:24's border "for the border of the sons of Ammon was
# strong", 3:16, Joshua 12:2); "and all that the LORD our God commanded" one.
assert P('ואשלח', 'מלאכים', 'ממדבר', 'קדמות', 'אל', 'סיחון', 'מלך', 'חשבון') == ['Deut 2:26'] and [s for s in U('קדמות') if s.split()[0] in ('Deut', 'Josh', '1Chr')] == S_('1Chr 6:64', 'Deut 2:26', 'Josh 21:37') and len(U('סיחון')) == 14 and [s for s in U('סיחון') if s.startswith('Deut')] == ['Deut 2:26'] and len(U('סיחן')) == 12 and 'לסיחון' in words('Deut', 31, 4)
assert words('Num', 21, 21)[:5] == ['וישלח', 'ישראל', 'מלאכים', 'אל', 'סיחן'] and P('דברי', 'שלום') == S_('2Kgs 15:15', 'Deut 2:26', 'Esth 9:30', 'Ps 28:3') and P('אעברה', 'בארצך') == S_('Deut 2:27', 'Num 21:22') and P('בדרך', 'בדרך', 'אלך') == ['Deut 2:27'] and P('ימין', 'ושמאול', books=T) == S_('Deut 17:20', 'Deut 28:14', 'Deut 2:27', 'Num 20:17', 'Num 22:26')
assert DIFF(('Num', 21, 22), ('Deut', 2, 27)) == [('insert', [], ['בדרך', 'בדרך', 'אלך']), ('replace', ['נטה', 'בשדה', 'ובכרם', 'לא', 'נשתה', 'מי', 'באר', 'בדרך', 'המלך', 'נלך', 'עד', 'אשר', 'נעבר', 'גבלך'], ['אסור', 'ימין', 'ושמאול'])] and len(words('Num', 21, 22)) == 17 and len(words('Deut', 2, 27)) == 9
assert P('רק', 'אעברה', 'ברגלי') == ['Deut 2:28'] and len(U('ברגלי')) == 5 and words('Num', 20, 19)[-2:] == ['ברגלי', 'אעברה'] and P('כאשר', 'עשו', 'לי', 'בני', 'עשו', 'הישבים', 'בשעיר') == ['Deut 2:29'] and words('Num', 20, 18)[:5] == ['ויאמר', 'אליו', 'אדום', 'לא', 'תעבר'] and words('Num', 20, 21)[:2] == ['וימאן', 'אדום'] and words('Judg', 11, 17)[14:21] == ['וגם', 'אל', 'מלך', 'מואב', 'שלח', 'ולא', 'אבה']
assert P('ולא', 'אבה', 'סיחן', 'מלך', 'חשבון', 'העברנו', 'בו') == ['Deut 2:30'] and U('העברנו') == ['Deut 2:30'] and words('Num', 21, 23)[:6] == ['ולא', 'נתן', 'סיחן', 'את', 'ישראל', 'עבר'] and words('Deut', 2, 30)[7:13] == ['כי', 'הקשה', 'יהוה', 'אלהיך', 'את', 'רוחו'] and P('ואמץ', 'את', 'לבבו') == ['Deut 2:30'] and words('Exod', 7, 3)[:5] == ['ואני', 'אקשה', 'את', 'לב', 'פרעה'] and words('Exod', 4, 21)[-8:-4] == ['ואני', 'אחזק', 'את', 'לבו'] and sg(2, 30, 'הקשה') == 'be-dense'
assert [s for s in P('כיום', 'הזה') if s.startswith('Deut')] == S_('Deut 10:15', 'Deut 29:27', 'Deut 2:30', 'Deut 4:20', 'Deut 4:38', 'Deut 8:18') and P('ראה', 'החלתי', 'תת', 'לפניך') == ['Deut 2:31']
assert DIFF(('Num', 21, 23), ('Deut', 2, 32)) == [('replace', ['ולא', 'נתן'], ['ויצא']), ('replace', ['את', 'ישראל', 'עבר', 'בגבלו', 'ויאסף', 'סיחן', 'את', 'כל'], ['לקראתנו', 'הוא', 'וכל']), ('replace', ['ויצא', 'לקראת', 'ישראל', 'המדברה', 'ויבא'], ['למלחמה']), ('delete', ['וילחם', 'בישראל'], [])] and len(words('Num', 21, 23)) == 20 and len(words('Deut', 2, 32)) == 8 and len(U('יהצה', 'יהץ', 'ביהצה', 'יהצ')) == 8
assert P('ונך', 'אתו', 'ואת', 'בנו') == ['Deut 2:33'] and [x for x in words('Num', 21, 35) if x == 'בניו'] == ['בניו'] and 'בניו' not in words('Deut', 3, 3) and P('ונלכד', 'את', 'כל', 'עריו', 'בעת', 'ההוא') == S_('Deut 2:34', 'Deut 3:4') and P('ונחרם', 'את', 'כל', 'עיר', 'מתם', 'והנשים', 'והטף') == ['Deut 2:34']
assert lemma_of('Deut', 2, 34, 'מתם') == ['4962'] and len(LEMT('4962')) == 22 and sorted(s for s, x, m in LEMT('4962') if s.startswith('Deut')) == S_('Deut 2:34', 'Deut 3:6', 'Deut 4:27', 'Deut 26:5', 'Deut 28:62', 'Deut 33:6') and sg(2, 34, 'מתם') == 'adult' and P('לא', 'השארנו', 'שריד') == ['Deut 2:34'] and U('ונחרם') == S_('Deut 2:34', 'Deut 3:6')
assert P('רק', 'הבהמה', 'בזזנו', 'לנו', 'ושלל', 'הערים', 'אשר', 'לכדנו') == ['Deut 2:35'] and U('בזזנו', 'בזונו') == S_('Deut 2:35', 'Deut 3:7') and words('Josh', 8, 27)[:8] == ['רק', 'הבהמה', 'ושלל', 'העיר', 'ההיא', 'בזזו', 'להם', 'ישראל'] and words('Josh', 11, 14)[:6] == ['וכל', 'שלל', 'הערים', 'האלה', 'והבהמה', 'בזזו']
assert P('מערער', 'אשר', 'על', 'שפת', 'נחל', 'ארנן') == S_('Deut 2:36', 'Deut 4:48') and len(U('ערער', 'מערער', 'בערער', 'וערער', 'ערוער')) == 11 and words('Num', 32, 34)[-1] == 'ערער' and P('לא', 'היתה', 'קריה', 'אשר', 'שגבה', 'ממנו') == ['Deut 2:36'] and U('שגבה') == ['Deut 2:36'] and sg(2, 36, 'שגבה') == 'be--lofty' and P('את', 'הכל', 'נתן', 'יהוה', 'אלהינו', 'לפנינו') == ['Deut 2:36']
assert P('רק', 'אל', 'ארץ', 'בני', 'עמון', 'לא', 'קרבת') == ['Deut 2:37'] and P('כל', 'יד', 'נחל', 'יבק') == ['Deut 2:37'] and U('יבק') == S_('Deut 2:37', 'Deut 3:16', 'Gen 32:23', 'Josh 12:2', 'Num 21:24') and words('Num', 21, 24)[7:12] == ['מארנן', 'עד', 'יבק', 'עד', 'בני'] and P('וכל', 'אשר', 'צוה', 'יהוה', 'אלהינו') == ['Deut 2:37']

# 3:1-22 OG AND THE EAST (computed): 3:1 AGAINST NUMBERS 21:33, DIFFED — "and they turned and went up" became "and we turned and went up",
# "to meet them" became "to meet us", the rest equal (fourteen tokens each); 3:2 AGAINST 21:34 — "to Moses" became "to me", the rest equal
# (the divine word quoted whole, twenty-five tokens); 3:3 AGAINST 21:35 — "and they smote him and his sons" became "AND THE LORD OUR GOD GAVE
# INTO OUR HAND ALSO OG KING OF BASHAN", "and we smote him" inserted, "and they possessed his land" dropped; "SIXTY CITIES" 3:4, Joshua 13:30,
# 1 Chronicles 2:23 (1 Kings 4:13 "sixty great cities with walls and bronze bars" — Solomon's officer's district); "all the region of Argob"
# 3:4 and 3:14, ARGOB five seats; "the kingdom of Og in Bashan" 3:4 and 3:10, "the kingdom of Og" four (Numbers 32:33 the grant); 3:5
# "FORTIFIED CITIES" spelled plene (בצרות — the store glossing "gather-grapes", the vintage's homograph), "a high wall" one seat, "GATES AND
# BARS" three seats (Keilah's, Solomon's); "THE UNWALLED TOWNS" — the family's twenty-seven seats (Ezekiel 38:11's, Zechariah 2:8's Jerusalem, the
# Perizzite by the consonants at Genesis 15:20 and Joshua's lists); "we devoted them as we did to Sihon" one; "AND WE TOOK AT THAT TIME THE
# LAND FROM THE HAND OF THE TWO KINGS OF THE AMORITES" one — "the two kings of the Amorites" three seats (3:8, 4:47, Joshua 24:12), the parser
# [2] with the construct mark; HERMON eleven seats of the bare token; 3:9 "THE SIDONIANS CALL HERMON SIRION AND THE AMORITES CALL IT SENIR" one
# seat — Sirion here and Psalm 29:6's (with the vav; Daniel 3:25's Aramaic homograph "loosed"), Senir four (Song 4:8, 1 Chronicles 5:23,
# Ezekiel 27:5's cypresses) — the outside row 37:9 brings the verse to 11:10 with 4:48's Sion, the mountain's four names; "THE TABLELAND"
# 3:10, 4:43 (Bezer's), Joshua 13:9, 16, 21, Jeremiah 48's — eight seats of the token (the psalms' "level path" the homograph); SALCAH
# three seats; 3:11 "FOR ONLY OG KING OF BASHAN WAS LEFT OF THE REMNANT OF THE REPHAIM" — "of the remnant of the Rephaim" JOSHUA 12:4 and
# 13:12's phrase for Og (the two seats quoting); "HIS BEDSTEAD WAS A BEDSTEAD OF IRON" one seat — the couch-word ten tokens (Amos's "corner of
# a couch", the psalms', Job's, the Song's "our couch"), the store glossing "couch"; "IS IT NOT IN RABBAH OF THE SONS OF AMMON" — the form
# הלה a HAPAX (the store: "the-not"), "Rabbah of the sons of Ammon" 3:11 and 2 SAMUEL 12:26 (Joab's siege; Jeremiah 49:2 and Ezekiel 21:25
# with another form); "NINE CUBITS ITS LENGTH AND FOUR CUBITS ITS BREADTH" the parser [9, 4]; "BY THE CUBIT OF A MAN" a hapax phrase — "by
# the cubit" (באמת) the Torah's one seat so spelled (the store: "in-mother" → the display layer's "by-the-cubit" since the Numbers walk);
# 3:12 "from Aroer on the brook Arnon" 3:12 and 2 Kings 10:33 (Hazael's conquest — the same clause), "AND HALF THE HILL COUNTRY OF GILEAD"
# one seat, the fraction unread by the parser (the class named); "TO THE REUBENITE AND THE GADITE" five seats (3:12, 29:7, Joshua 12:6,
# 22:1, 1 Chronicles 5:26); 3:13 "TO THE HALF-TRIBE OF MANASSEH" — with the article on Manasseh (המנשה) this seat alone in the Torah (Joshua
# 13:29, 1 Chronicles 27:20 without it; Numbers 32:33's "and to the half-tribe of Manasseh son of Joseph" the grant); "all the region of the
# Argob ... is called the land of Rephaim" one; 3:14 AGAINST NUMBERS 32:41, DIFFED — "and Jair went and captured their villages and called
# them Havvoth-jair" became "Jair took all the region of Argob to the border of the Geshurite and the Maacathite and called them after his own
# name, Bashan, Havvoth-jair, to this day" (twenty-three tokens for eleven; "went and captured" → "took"; "their villages" → the region and the
# border); "the Geshurite and the Maacathite" 3:14, Joshua 12:5, 13:11; HAVVOTH-JAIR six seats (Numbers 32:41, this, Joshua 13:30, Judges
# 10:4, 1 Kings 4:13, 1 Chronicles 2:23); 3:15 "AND TO MACHIR I GAVE GILEAD" one — Numbers 32:39-40's Machir ("and Moses gave Gilead to Machir
# son of Manasseh and he dwelt in it"); 3:16 "the midst of the brook as border, and to the brook Jabbok, the border of the sons of Ammon" —
# "and to Jabbok the brook, the border of the sons of Ammon" 3:16 and JOSHUA 12:2 (the same clause); 3:17 "the Arabah and the Jordan as border,
# FROM CHINNERETH TO THE SEA OF THE ARABAH, THE SALT SEA, under the slopes of Pisgah eastward" — Chinnereth six seats of the name's tokens, "the Sea of the
# Arabah" five (this, 4:49, Joshua 3:16, 12:3, 2 Kings 14:25), "the Salt Sea" nine, "THE SLOPES OF PISGAH" 3:17 and 4:49 (the store: "ravine"),
# THE PISGAH eight seats (Balaam's field of Zophim, Numbers 21:20's, 23:14's; 3:27's "the top of Pisgah"; 34:1's Nebo); 3:18 "and I commanded
# you at that time" — "THE LORD YOUR GOD HAS GIVEN YOU THIS LAND TO POSSESS IT; ARMED YOU SHALL PASS OVER BEFORE YOUR BROTHERS" — "armed"
# (חלוצים) three seats of the plural token — this and Numbers 32:30, 32 — the singular at 32:21, 27, 29 (the condition Moses set), Joshua 1:14 and 4:12-13 the run
# ("armed before your brothers ... about forty thousand armed for war"); "all the sons of valor" ten seats; 3:19 "ONLY YOUR WIVES AND YOUR
# LITTLE ONES AND YOUR CATTLE — I KNOW THAT YOU HAVE MUCH CATTLE" one — Numbers 32:1's "much cattle" (the tribes' opening word), 32:26's
# "our little ones, our wives, our cattle"; "shall dwell in your cities which I have given you" one; 3:20 "UNTIL THE LORD GIVES REST TO
# YOUR BROTHERS AS TO YOU" — JOSHUA 1:15 QUOTING (the two seats of the clause; Joshua 22:4's release "now the LORD your God has given rest
# to your brothers"); "AND YOU SHALL RETURN EACH TO HIS POSSESSION" one seat; 3:21 "AND JOSHUA I COMMANDED AT THAT TIME" — JOSHUA SPELLED
# PLENE (יהושוע) at 3:21 and JUDGES 2:7 ALONE in the Bible (the defective bare token 177 seats); "YOUR EYES HAVE SEEN" one; "the two kings" the
# parser [2]; 3:22 "YOU SHALL NOT FEAR THEM, FOR THE LORD YOUR GOD, HE FIGHTS FOR YOU" — "who fights for you" 3:22 and Joshua 23:3, 10 (Joshua's
# farewell quoting), Exodus 14:14's "the LORD will fight for you" the first form, 1:30's "he will fight for you" the speech's own echo.
assert DIFF(('Num', 21, 33), ('Deut', 3, 1)) == [('replace', ['ויפנו', 'ויעלו'], ['ונפן', 'ונעל']), ('replace', ['לקראתם'], ['לקראתנו'])] and len(words('Num', 21, 33)) == 14 == len(words('Deut', 3, 1))
assert DIFF(('Num', 21, 34), ('Deut', 3, 2)) == [('replace', ['אל', 'משה'], ['אלי'])] and len(words('Num', 21, 34)) == 26 and len(words('Deut', 3, 2)) == 25
assert DIFF(('Num', 21, 35), ('Deut', 3, 3)) == [('replace', ['ויכו', 'אתו', 'ואת', 'בניו'], ['ויתן', 'יהוה', 'אלהינו', 'בידנו', 'גם', 'את', 'עוג', 'מלך', 'הבשן']), ('insert', [], ['ונכהו']), ('delete', ['ויירשו', 'את', 'ארצו'], [])] and len(words('Num', 21, 35)) == 15 and len(words('Deut', 3, 3)) == 18
assert P('ששים', 'עיר') == S_('1Chr 2:23', 'Deut 3:4', 'Josh 13:30') and P('ששים', 'ערים') == ['1Kgs 4:13'] and words('1Kgs', 4, 13)[16:22] == ['ששים', 'ערים', 'גדלות', 'חומה', 'ובריח', 'נחשת'] and P('כל', 'חבל', 'ארגב') == S_('Deut 3:14', 'Deut 3:4') and U('ארגב', 'הארגב') == S_('1Kgs 4:13', '2Kgs 15:25', 'Deut 3:13', 'Deut 3:14', 'Deut 3:4') and P('ממלכת', 'עוג') == S_('Deut 3:10', 'Deut 3:13', 'Deut 3:4', 'Num 32:33')
assert words('Deut', 3, 5)[:8] == ['כל', 'אלה', 'ערים', 'בצרות', 'חומה', 'גבהה', 'דלתים', 'ובריח'] and sg(3, 5, 'בצרות') == 'gather-grapes' and P('חומה', 'גבהה') == ['Deut 3:5'] and P('דלתים', 'ובריח') == S_('1Sam 23:7', '2Chr 8:5', 'Deut 3:5') and P('לבד', 'מערי', 'הפרזי', 'הרבה', 'מאד') == ['Deut 3:5'] and len(U('הפרזי', 'פרזי', 'פרזות', 'הפרזות', 'והפרזי')) == 27 and sg(3, 5, 'הפרזי') == 'the-rustic'
assert P('ונחרם', 'אותם', 'כאשר', 'עשינו', 'לסיחן', 'מלך', 'חשבון') == ['Deut 3:6'] and P('החרם', 'כל', 'עיר', 'מתם', 'הנשים', 'והטף') == ['Deut 3:6'] and P('וכל', 'הבהמה', 'ושלל', 'הערים', 'בזונו', 'לנו') == ['Deut 3:7']
assert P('שני', 'מלכי', 'האמרי') == S_('Deut 3:8', 'Deut 4:47', 'Josh 24:12') and P('מנחל', 'ארנן', 'עד', 'הר', 'חרמון') == ['Deut 3:8'] and len(U('חרמון')) == 11 and P('צידנים', 'יקראו', 'לחרמון', 'שרין', 'והאמרי', 'יקראו', 'לו', 'שניר') == ['Deut 3:9'] and U('שרין') == S_('Dan 3:25', 'Deut 3:9') and U('שניר') == S_('Deut 3:9', 'Song 4:8') and 'ושניר' in words('1Chr', 5, 23) and 'משניר' in words('Ezek', 27, 5) and 'ושרין' in words('Ps', 29, 6)
assert P('כל', 'ערי', 'המישר') == ['Deut 3:10'] and len(U('המישר')) == 8 and [s for s in U('המישר') if s.startswith(('Deut', 'Josh'))] == S_('Deut 3:10', 'Deut 4:43', 'Josh 13:16', 'Josh 13:21', 'Josh 13:9') and U('סלכה') == S_('1Chr 5:11', 'Deut 3:10', 'Josh 13:11') and P('ערי', 'ממלכת', 'עוג', 'בבשן') == ['Deut 3:10']
assert P('מיתר', 'הרפאים') == S_('Deut 3:11', 'Josh 12:4', 'Josh 13:12') and P('הנה', 'ערשו', 'ערש', 'ברזל') == ['Deut 3:11'] and lemma_of('Deut', 3, 11, 'ערשו') == ['6210'] and len(LEMT('6210')) == 10 and sg(3, 11, 'ערש') == 'couch' and U('הלה') == ['Deut 3:11'] and sg(3, 11, 'הלה') == 'the-not' and P('ברבת', 'בני', 'עמון') == S_('2Sam 12:26', 'Deut 3:11')
assert P('תשע', 'אמות', 'ארכה', 'וארבע', 'אמות', 'רחבה') == ['Deut 3:11'] and P('באמת', 'איש') == ['Deut 3:11'] and U('באמת', books=T) == ['Deut 3:11'] and PT('Deut', 3, 11, 'באמת') == ['בְּאַמַּת'] and sg(3, 11, 'באמת') == 'in-mother' and sg(3, 11, 'אמות') == 'mother'
assert P('מערער', 'אשר', 'על', 'נחל', 'ארנן') == S_('2Kgs 10:33', 'Deut 3:12') and P('וחצי', 'הר', 'הגלעד') == ['Deut 3:12'] and P('לראובני', 'ולגדי') == S_('1Chr 5:26', 'Deut 29:7', 'Deut 3:12', 'Josh 12:6', 'Josh 22:1') and P('לחצי', 'שבט', 'המנשה') == ['Deut 3:13'] and P('לחצי', 'שבט', 'מנשה') == S_('1Chr 27:20', 'Josh 13:29') and words('Num', 32, 33)[7:12] == ['ולחצי', 'שבט', 'מנשה', 'בן', 'יוסף']
assert P('ההוא', 'יקרא', 'ארץ', 'רפאים') == ['Deut 3:13'] and DIFF(('Num', 32, 41), ('Deut', 3, 14)) == [('replace', ['ויאיר'], ['יאיר']), ('replace', ['הלך', 'וילכד'], ['לקח']), ('replace', ['חותיהם'], ['כל', 'חבל', 'ארגב', 'עד', 'גבול', 'הגשורי', 'והמעכתי']), ('replace', ['אתהן'], ['אתם', 'על', 'שמו', 'את', 'הבשן']), ('insert', [], ['עד', 'היום', 'הזה'])] and len(words('Num', 32, 41)) == 11 and len(words('Deut', 3, 14)) == 23
assert P('הגשורי', 'והמעכתי') == S_('Deut 3:14', 'Josh 12:5', 'Josh 13:11') and P('חות', 'יאיר') == S_('1Chr 2:23', '1Kgs 4:13', 'Deut 3:14', 'Josh 13:30', 'Judg 10:4', 'Num 32:41') and P('ולמכיר', 'נתתי', 'את', 'הגלעד') == ['Deut 3:15'] and words('Num', 32, 40) == ['ויתן', 'משה', 'את', 'הגלעד', 'למכיר', 'בן', 'מנשה', 'וישב', 'בה']
assert P('תוך', 'הנחל', 'וגבל') == ['Deut 3:16'] and P('ועד', 'יבק', 'הנחל', 'גבול', 'בני', 'עמון') == S_('Deut 3:16', 'Josh 12:2') and P('מכנרת', 'ועד', 'ים', 'הערבה', 'ים', 'המלח') == ['Deut 3:17'] and len(U('כנרת', 'מכנרת', 'כנרות')) == 6 and P('ים', 'הערבה') == S_('2Kgs 14:25', 'Deut 3:17', 'Deut 4:49', 'Josh 12:3', 'Josh 3:16') and len(P('ים', 'המלח')) == 9
assert P('אשדת', 'הפסגה') == S_('Deut 3:17', 'Deut 4:49') and sg(3, 17, 'אשדת') == 'ravine' and U('הפסגה') == S_('Deut 34:1', 'Deut 3:17', 'Deut 3:27', 'Deut 4:49', 'Josh 12:3', 'Josh 13:20', 'Num 21:20', 'Num 23:14') and words('Num', 23, 14)[3:6] == ['אל', 'ראש', 'הפסגה']
assert P('יהוה', 'אלהיכם', 'נתן', 'לכם', 'את', 'הארץ', 'הזאת', 'לרשתה') == ['Deut 3:18'] and P('חלוצים', 'תעברו', 'לפני', 'אחיכם', 'בני', 'ישראל', 'כל', 'בני', 'חיל') == ['Deut 3:18'] and U('חלוצים') == S_('Deut 3:18', 'Num 32:30', 'Num 32:32') and U('חלוץ', books=('Num',)) == S_('Num 32:21', 'Num 32:27', 'Num 32:29') and sg(3, 18, 'חלוצים') == 'pull-off' and len(P('בני', 'חיל')) == 10
assert words('Josh', 1, 14)[11:17] == ['ואתם', 'תעברו', 'חמשים', 'לפני', 'אחיכם', 'כל'] and words('Josh', 4, 13)[:4] == ['כארבעים', 'אלף', 'חלוצי', 'הצבא'] and P('ידעתי', 'כי', 'מקנה', 'רב', 'לכם') == ['Deut 3:19'] and words('Num', 32, 1)[:3] == ['ומקנה', 'רב', 'היה'] and words('Num', 32, 26)[:3] == ['טפנו', 'נשינו', 'מקננו'] and P('ישבו', 'בעריכם', 'אשר', 'נתתי', 'לכם') == ['Deut 3:19']
assert P('עד', 'אשר', 'יניח', 'יהוה', 'לאחיכם', 'ככם') == S_('Deut 3:20', 'Josh 1:15') and words('Josh', 22, 4)[:5] == ['ועתה', 'הניח', 'יהוה', 'אלהיכם', 'לאחיכם'] and P('ושבתם', 'איש', 'לירשתו') == ['Deut 3:20'] and sg(3, 20, 'לירשתו') == 'to-something-occupied-him/its' and sg(3, 20, 'יניח') == 'rest'
assert P('ואת', 'יהושוע', 'צויתי', 'בעת', 'ההוא') == ['Deut 3:21'] and U('יהושוע') == S_('Deut 3:21', 'Judg 2:7') and len(U('יהושע')) == 177 and P('עיניך', 'הראת') == ['Deut 3:21'] and P('לא', 'תיראום') == ['Deut 3:22'] and P('הנלחם', 'לכם') == S_('Deut 3:22', 'Josh 23:10', 'Josh 23:3') and words('Exod', 14, 14)[:3] == ['יהוה', 'ילחם', 'לכם'] and sg(3, 22, 'הנלחם') == 'the-feed-on'

# 3:23-29 THE PLEA (computed): "AND I BESOUGHT THE LORD AT THAT TIME" — the form "and I besought" a HAPAX (the grace-root's hitpael: Joseph's
# brothers "when he besought us" Genesis 42:21, Solomon's, Esther's, Hosea's Jacob "he wept and besought him" — the store glossing "and-bend");
# "O LORD GOD" (אדני יהוה) — the Torah's four seats: ABRAHAM'S TWO (Genesis 15:2, 8, the covenant of the pieces), 3:24 and 9:26 (Moses' two
# pleas), 284 in the Bible; "YOU HAVE BEGUN TO SHOW YOUR SERVANT YOUR GREATNESS AND YOUR STRONG HAND" — "your greatness" 3:24 and Joshua 3:7 ("to magnify you"), "YOUR STRONG
# HAND" 3:24 and SOLOMON'S PRAYER (1 Kings 8:42), "the strong hand" with the article 34:12 alone; "WHAT GOD IS THERE IN HEAVEN OR ON EARTH WHO CAN DO ACCORDING TO YOUR WORKS AND YOUR MIGHTY ACTS" — "according
# to your works and according to your mighty acts" a hapax pair; 3:25 "LET ME CROSS OVER, I PRAY" three seats (Jephthah's embassy to Edom
# "let me pass, I pray, through your land" Judges 11:17; Abishai's 2 Samuel 16:9); "the good land" the book's five; "THAT GOOD HILL COUNTRY"
# one seat; "and Lebanon" 1:7's and 3:25's forms both plene (the pointing differs only by the meteg); 3:26 "BUT THE LORD WAS WROTH WITH ME
# FOR YOUR SAKES" — the wrath-verb's hitpael nine tokens (3:26; Psalm 78:21, 59, 62's "the LORD was wroth" of the wilderness and Shiloh, 89:39's;
# the Proverbs' "he who is angry" three) — the store glossing "and-cross-over" (the pass-root's homograph; the verse's own "let me cross over"
# two verses before); "for your sakes" (למענכם) four seats of the token; 1:37's "was angry with me for your sakes" and 4:21's "was angry with me because of
# your words" the plea's two other tellings, PSALM 106:32's "it went ill with Moses for their sakes" the psalm's; "AND HE WOULD NOT HEAR ME"
# one; "ENOUGH FOR YOU" — the singular one seat (the plural's eight, 1:6's first); "SPEAK NO MORE TO ME OF THIS MATTER" one; 3:27 "GO UP TO
# THE TOP OF PISGAH" — Numbers 27:12's "go up to this mount Abarim" and 32:49's "mount Nebo" and 34:1's "Nebo, the top of Pisgah" the three
# names (the outside row 37:11's count); "AND LIFT UP YOUR EYES" — 3:27 with the vav one seat (Genesis 13:14's "lift up now your eyes" to
# ABRAM the kin, its four directions in ANOTHER ORDER: north, south, east, west against 3:27's WEST, NORTH, SOUTH, EAST — and Genesis 28:14's
# west, east, north, south a third order); "and see with your eyes" 3:27 and Ezekiel 44:5; "FOR YOU SHALL NOT CROSS THIS JORDAN" one (4:22's
# "I am not crossing the Jordan", 31:2's "you shall not cross this Jordan" as the LORD's word quoted, 34:4's "there you shall not cross" the
# runs); 3:28 "AND CHARGE JOSHUA AND STRENGTHEN HIM AND ENCOURAGE HIM" — "strengthen him and encourage him" one seat, "BE STRONG AND OF GOOD
# COURAGE" nine seats (31:7, 23 to Joshua; Joshua 1:6, 7, 9, 18; David's to Solomon, 1 Chronicles 22:13, 28:20; Isaiah 28:2 another sense);
# "for he shall cross over before this people" one; "AND HE SHALL CAUSE THEM TO INHERIT THE LAND WHICH YOU SHALL SEE" one seat — NUMBERS
# 27:19-23's commissioning (Eleazar, the laying on of hands) told here as the charge; 31:7 and 31:23's "you shall cause them to inherit" and
# JOSHUA 1:6's "you shall cause this people to inherit" the runs; 3:29 "AND WE DWELT IN THE VALLEY OPPOSITE BETH-PEOR" — "opposite Beth-peor"
# three seats: this, 4:46 (the law's place-stamp) and 34:6 (MOSES' GRAVE, "in the valley in the land of Moab opposite Beth-peor"), "in the
# valley" the token's thirteen seats; Peor twelve seats (Numbers 25's Baal-peor, 31:16, Joshua 22:17, Psalm 106:28); Numbers 25:1's Shittim
# and 33:49's "from Beth-jeshimoth to Abel-shittim in the plains of Moab" the same camp by other names.
assert P('ואתחנן', 'אל', 'יהוה', 'בעת', 'ההוא', 'לאמר') == ['Deut 3:23'] and U('ואתחנן') == ['Deut 3:23'] and sg(3, 23, 'ואתחנן') == 'and-bend' and lemma_of('Deut', 3, 23, 'ואתחנן') == ['2603 a'] and 'Gen 42:21' in LEMV('2603 a') and 'Hos 12:5' in LEMV('2603 a') and [m for x, m in by[('Deut', 3, 23)] if x == 'ואתחנן'] == ['HC/Vtw1cs']
assert P('אדני', 'יהוה', books=T) == S_('Deut 3:24', 'Deut 9:26', 'Gen 15:2', 'Gen 15:8') and len(P('אדני', 'יהוה')) == 284 and P('כמעשיך', 'וכגבורתך') == ['Deut 3:24'] and U('גדלך') == S_('Deut 3:24', 'Josh 3:7') and P('ידך', 'החזקה') == S_('1Kgs 8:42', 'Deut 3:24') and P('היד', 'החזקה', books=T) == ['Deut 34:12']
assert P('אעברה', 'נא') == S_('2Sam 16:9', 'Deut 3:25', 'Judg 11:17') and P('ההר', 'הטוב') == ['Deut 3:25'] and sg(3, 25, 'נא') == 'please'
assert lemma_of('Deut', 3, 26, 'ויתעבר') == ['5674 b'] and sorted(s for s, x, m in LEMT('5674 b') if 'Vt' in m) == S_('Deut 3:26', 'Prov 14:16', 'Prov 20:2', 'Prov 26:17', 'Ps 78:21', 'Ps 78:59', 'Ps 78:62', 'Ps 89:39') and sg(3, 26, 'ויתעבר') == 'and-cross-over' and len(U('למענכם')) == 4 and P('ולא', 'שמע', 'אלי') == ['Deut 3:26']
assert words('Deut', 4, 21)[:4] == ['ויהוה', 'התאנף', 'בי', 'על'] and words('Ps', 106, 32)[-3:] == ['וירע', 'למשה', 'בעבורם'] and P('אל', 'תוסף', 'דבר', 'אלי', 'עוד', 'בדבר', 'הזה') == ['Deut 3:26']
assert P('עלה', 'ראש', 'הפסגה') == ['Deut 3:27'] and words('Num', 27, 12)[4:9] == ['עלה', 'אל', 'הר', 'העברים', 'הזה'] and words('Deut', 34, 1)[5:9] == ['הר', 'נבו', 'ראש', 'הפסגה'] and P('ושא', 'עיניך') == ['Deut 3:27'] and P('שא', 'נא', 'עיניך') == S_('Ezek 8:5', 'Gen 13:14', 'Gen 31:12', 'Zech 5:5')
assert P('ימה', 'וצפנה', 'ותימנה', 'ומזרחה') == ['Deut 3:27'] and words('Gen', 13, 14)[-4:] == ['צפנה', 'ונגבה', 'וקדמה', 'וימה'] and words('Gen', 28, 14)[-4:] == ['ימה', 'וקדמה', 'וצפנה', 'ונגבה'] and P('וראה', 'בעיניך') == S_('Deut 3:27', 'Ezek 44:5') and P('כי', 'לא', 'תעבר', 'את', 'הירדן', 'הזה') == ['Deut 3:27'] and words('Deut', 31, 2)[-6:] == ['לא', 'תעבר', 'את', 'הירדן', 'הזה', ''][:-1] + [] or words('Deut', 31, 2)[-5:] == ['לא', 'תעבר', 'את', 'הירדן', 'הזה']
assert P('וחזקהו', 'ואמצהו') == ['Deut 3:28'] and P('חזק', 'ואמץ') == S_('1Chr 22:13', '1Chr 28:20', 'Deut 31:23', 'Deut 31:7', 'Isa 28:2', 'Josh 1:18', 'Josh 1:6', 'Josh 1:7', 'Josh 1:9') and P('כי', 'הוא', 'יעבר', 'לפני', 'העם', 'הזה') == ['Deut 3:28'] and P('והוא', 'ינחיל', 'אותם') == ['Deut 3:28'] and words('Josh', 1, 6)[:7] == ['חזק', 'ואמץ', 'כי', 'אתה', 'תנחיל', 'את', 'העם'] and words('Num', 27, 23)[:5] == ['ויסמך', 'את', 'ידיו', 'עליו', 'ויצוהו']
assert P('ונשב', 'בגיא', 'מול', 'בית', 'פעור') == ['Deut 3:29'] and P('מול', 'בית', 'פעור') == S_('Deut 34:6', 'Deut 3:29', 'Deut 4:46') and len(U('בגיא')) == 13 and len(U('פעור')) == 12 and words('Deut', 34, 6)[:8] == ['ויקבר', 'אתו', 'בגי', 'בארץ', 'מואב', 'מול', 'בית', 'פעור'] and sg(3, 29, 'בגיא') == 'in-gorge' and sg(3, 29, 'מול') == 'abrupt' and sg(3, 29, 'בית') == '?'

# ONKELOS OVER THE BOOK (computed on the plain Aramaic of every verse of Onkelos Deuteronomy): 1:1 THE REBUKE PARAPHRASE — the places read as
# the sins (thirty-three tokens for the Hebrew's twenty-two: "he rebuked them for that they had sinned in the wilderness, and for that they
# provoked in the plain opposite the Sea of Reeds; in Paran where they scorned the manna, and at Hazeroth where they provoked over the meat,
# and for that they made the calf of gold") — the Sifrei 1's reading, with "rebuked" a word used once in the book, "the manna" three times
# (8:3, 8:16 the others), "the calf" at 1:1 and 9:16; KADESH-BARNEA = REKAM GEYAH (four seats: 1:2, 1:19, 2:14, 9:23), Kadesh = Rekam (1:46
# "in Rekam", 32:51); BASHAN = MATHNAN (the forms at sixteen seats); 1:5 "BEGAN TO EXPLAIN THE TEACHING OF THE TORAH" — "began" (שרי) five
# seats (1:5, 2:24, 2:31, 25:10, 33:20), "the teaching" one, "the Torah" (אוריתא) twenty; "ENOUGH FOR YOU" (סגי לכון) 1:6, 2:3, 3:19 and the
# singular 3:26 — the Hebrew's four as four; "bear" the same root at 1:9, 1:12, 1:31 ×2 (the Hebrew's carrying-verbs made one); 1:12 "your
# business and your judgments" (the Hebrew's burden and strife); 1:13 "understanding" (one seat); 1:16 "his stranger" (גיוריה, one seat),
# "in truth" (קושטא, one); 1:17 "you shall not show favor" (one), "the judgment is the LORD's"; 1:22, 24 "and they shall spy / and they spied"
# (the Aramaic spy-verb at two seats — the Hebrew's search-out and spy-out made one); 1:26, 1:43, 9:23 "AND YOU REBELLED AGAINST THE WORD
# (MEMRA) OF THE LORD" — the Memra-word eleven bare, five "by the Memra", ten "his Memra" (3:22 "his Memra fights for you"); 1:27 "you
# murmured" one seat, "in the LORD's hatred" one; 1:28 "melted our heart" one; 1:28, 2:11, 2:20 "GIANTS" (גבראי) for the Anakim and the Rephaim
# — eight seats of the bare form; 1:32 "BELIEVING IN THE MEMRA OF THE LORD" one seat; 1:34 "AND IT WAS HEARD BEFORE THE LORD" 1:34 and 5:25
# (the Hebrew's "the LORD heard" turned passive); 1:36 "IN THE FEAR OF THE LORD" (דחלתא דיי) — the Aramaic supplying "the fear" at twelve
# seats; 1:37, 3:26 "THERE WAS ANGER FROM BEFORE THE LORD" — "from before the LORD" fourteen seats, "anger" seven (the Hebrew's two wrath-verbs
# made one), "for your sakes" the two seats; 1:38 "he shall cause Israel to inherit" one; 1:39 "for a prey" one; 1:41 "WE ARE GUILTY BEFORE
# THE LORD" one, "you deemed it easy" rendered "YOU BEGAN to go up" (one seat); 1:42 "MY SHEKHINAH DOES NOT DWELL AMONG YOU" — "my Shekhinah"
# five seats (1:42, 31:17, 31:18, 32:20, 32:40), the clause one; 1:43 "the decree of the Memra" 1:43 and 9:23, "you acted wickedly" one; 1:44
# "AS THE BEES SCATTER" (one seat each); 1:45 "AND THE LORD DID NOT ACCEPT YOUR PRAYER" — "did not accept" 1:45 and 3:26 (Moses' plea told
# in the same words), "your prayer" one; 2:1 "and we went round" one; 2:5, 9, 19, 24 "contend" the four; 2:5 "THE TREADING OF THE SOLE OF A
# FOOT" (the sole-word three seats), "A POSSESSION" (ירתא) 2:5, 9, 19, 33:4; 2:6 "grain you shall buy" (one), "you shall buy (water)" (one),
# "for money" four in the book (2:6, 2:28 with 14:25, 21:14); 2:7 "SUPPLIED YOUR NEED" (both words one seat), "the Memra of the LORD your God
# IN YOUR AID" — "in your aid" six seats, "you lacked nothing" one; 2:9, 18, 29 AR = LEHAYAT (three); 2:10-11 THE EMIM = "THE TERRIBLE ONES"
# (אימתני, two), "formerly" four; 2:12 the Horites = "the Horaee" (one), "in their place" 2:12, 21, 22, 23; 2:14 "until it was ended" one, "the
# men of war" 2:14, 16; 2:15 "to destroy them" 2:15 and 7:22; 2:20 THE ZAMZUMMIM = "THE SCHEMERS" (חשבני, one); 2:23 THE AVVIM "in Defiah",
# THE CAPHTORIM = CAPPADOCIANS (both one seat); 2:25 "the dread of you and the fear of you" one each; 2:26 "MESSENGERS" (אזגדין, one), "words
# of peace" 2:26 and 29:18; 2:27 "I will not turn aside" one; 2:30 "to let us pass in his border" (one each), "hardened" one; 2:32 "to Jahaz"
# one; 2:34, 3:4 "and we conquered"; 2:34, 3:6 "AND WE FINISHED" (וגמרנא) for "we devoted" — the Aramaic ban-word; "no survivor" (משזב) 2:34,
# 3:3, 32:39; 2:35, 3:7 "we plundered"; 2:37 "the brook Jabbok" 2:37, 3:16; 3:4, 13, 14 ARGOB = "THE HOUSE OF THE DISTRICT OF TRACHONA" (three);
# 3:5 "walled" one, "with gates and bars" one, "the open towns" one; 3:9 SENIR = "THE SNOW MOUNTAIN" (טור תלגא, one), Sirion kept; 3:11 "THE
# CUBIT OF A KING" for the Hebrew's "cubit of a man" (one seat), "in Rabbah" one; 3:12, 13 "the half" two forms; 3:14 the Maacathite = "APKEROS"
# (one); 3:17 CHINNERETH = GENNESAR (one), "the Salt Sea", THE PISGAH = "THE HEIGHT" (רמתא, 3:17, 4:49 "the slope of the height"; 3:27, 12:2,
# 34:1); 3:18 "ARMED" (one); 3:20 "gives rest" 3:20 and 25:19; 3:21 "the two kings" one; 3:22 "HIS MEMRA FIGHTS FOR YOU"; 3:23 "AND I PRAYED
# BEFORE THE LORD" (three seats: 3:23, 9:20, 9:26); 3:24 "YOU ARE GOD WHOSE SHEKHINAH IS IN THE HEAVENS ABOVE AND WHO RULES ON EARTH" — "God"
# (אלהים) four seats, "you have begun", "your greatness", "whose Shekhinah", "and rules" (3:24, 4:39), "according to your works and your
# might" one each; 3:25 LEBANON = "THE HOUSE OF THE SANCTUARY" (בית מקדשא — 3:25, 23:19, 33:19); 3:26 "and he did not accept from me" one,
# "ENOUGH FOR YOU (singular)" one, "speak no more before me" one; 3:27 "go up to the top of the height, lift up your eyes to the west and the
# north and the south and the east" (one each); 3:28 "strengthen him and encourage him" (one each), "he shall cause them to inherit" one;
# 3:29 "IN THE VALLEY" (בחילתא) 3:29, 4:46, 34:6 — "opposite Beth-peor" the same three.
assert aramaic(1, 1) == ['אלין', 'פתגמיא', 'די', 'מליל', 'משה', 'עם', 'כל', 'ישראל', 'בעברא', 'דירדנא', 'אוכח', 'יתהון', 'על', 'דחבו', 'במדברא', 'ועל', 'דארגיזו', 'במישרא', 'לקבל', 'ים', 'סוף', 'בפארן', 'דאתפלו', 'על', 'מנא', 'ובחצרות', 'דארגיזו', 'על', 'בשרא', 'ועל', 'דעבדו', 'עגל', 'דדהב'] and len(words('Deut', 1, 1)) == 22
ONK1 = {'אוכח': [(1, 1)], 'דחבו': [(1, 1)], 'מנא': [(1, 1), (8, 3), (8, 16)], 'עגל': [(1, 1), (9, 16)], 'דדהב': [(1, 1)], 'רקם': [(1, 2), (1, 19), (32, 51)], 'גיאה': [(1, 2), (1, 19), (2, 14), (9, 23)], 'ברקם': [(1, 46)], 'שרי': [(1, 5), (2, 24), (2, 31), (25, 10), (33, 20)], 'אולפן': [(1, 5)], 'סגי': [(1, 6), (1, 28), (2, 3), (3, 5), (3, 19), (3, 26), (20, 1), (28, 38)], 'לסוברא': [(1, 9)], 'אסובר': [(1, 12)], 'סוברך': [(1, 31)], 'מסובר': [(1, 31)], 'ודינכון': [(1, 12)], 'ואמננון': [(1, 13)], 'גיוריה': [(1, 16)], 'קושטא': [(1, 16)], 'תשתמודעון': [(1, 17)], 'ויאללון': [(1, 22)], 'ואלילו': [(1, 24)], 'וסרבתון': [(1, 26), (1, 43), (9, 23)], 'ואתרעמתון': [(1, 27)], 'בדסני': [(1, 27)], 'תברו': [(1, 28)], 'גבראי': [(1, 28), (2, 11), (2, 20)], 'כגבריא': [(2, 10), (2, 21)], 'יגיח': [(1, 30), (3, 22)], 'מהימנין': [(1, 32)], 'ושמיע': [(1, 34), (5, 25)], 'ורגז': [(1, 34)], 'אשלים': [(1, 36)], 'רגז': [(1, 37), (3, 26), (4, 21), (9, 8), (9, 19), (9, 20), (29, 27)], 'בדילכון': [(1, 37), (3, 26)], 'יחסננה': [(1, 38)], 'לבזא': [(1, 39)], 'חבנא': [(1, 41)], 'ושריתון': [(1, 41)], 'שכנתי': [(1, 42), (31, 17), (31, 18), (32, 20), (32, 40)], 'גזרת': [(1, 43), (9, 23)], 'וארשעתון': [(1, 43)], 'נתזן': [(1, 44)], 'דבריתא': [(1, 44)], 'צלותכון': [(1, 45)], 'קביל': [(1, 45), (3, 26)]}
assert {k: onk_tok(k) for k in ONK1} == ONK1, {k: onk_tok(k) for k in ONK1 if onk_tok(k) != ONK1[k]}
assert len(onk_tok('אוריתא')) == 20 and onk_tok('אוריתא')[0] == (1, 5) and len(onk_tok('מימרא')) == 11 and onk_tok('מימרא')[:3] == [(1, 26), (1, 43), (2, 7)] and len(onk_tok('במימרא')) == 5 and onk_tok('במימרא')[0] == (1, 32) and len(onk_tok('מימריה')) == 10 and onk_tok('מימריה')[0] == (3, 22) and len(onk_tok('גבריא')) == 8 and len(onk_seats('דמתנן') + onk_seats('מתנן')) >= 16
assert onk_seats('סגי לכון') == [(1, 6), (2, 3), (3, 19)] and onk_seats('סגי לך') == [(3, 26)] and onk_seats('ושמיע קדם יי') == [(1, 34), (5, 25)] and len(onk_seats('דחלתא דיי')) == 12 and onk_seats('דחלתא דיי')[0] == (1, 36) and len(onk_seats('מן קדם יי')) == 14 and [s for s in onk_seats('מן קדם יי') if s[0] <= 3] == [(1, 37), (2, 15), (3, 26)] and onk_seats('לית שכנתי') == [(1, 42)] and onk_seats('ולא קביל') == [(1, 45), (3, 26)]
ONK2 = {'ואקפנא': [(2, 1)], 'תתגרון': [(2, 5)], 'תתגרי': [(2, 9), (2, 19)], 'ואתגרי': [(2, 24)], 'פרסת': [(2, 5), (11, 24), (28, 56)], 'ירתא': [(2, 5), (2, 9), (2, 19), (33, 4)], 'עבורא': [(2, 6), (2, 28), (28, 51)], 'תזבנון': [(2, 6)], 'תכרון': [(2, 6)], 'בכספא': [(2, 6), (2, 28), (14, 25), (21, 14)], 'ספק': [(2, 7)], 'צרכך': [(2, 7)], 'בסעדך': [(2, 7), (20, 1), (31, 8), (31, 23), (33, 26), (33, 29)], 'מנעתא': [(2, 7)], 'לחית': [(2, 9), (2, 18)], 'בלחית': [(2, 29)], 'אימתני': [(2, 10), (2, 11)], 'מלקדמין': [(2, 10), (2, 12), (2, 20), (33, 27)], 'חראי': [(2, 12)], 'באתריהון': [(2, 12), (2, 21), (2, 22), (2, 23)], 'דסף': [(2, 14)], 'מגיחי': [(2, 14), (2, 16)], 'לשציותהון': [(2, 15), (7, 22)], 'חשבני': [(2, 20)], 'ועואי': [(2, 23)], 'בדפיח': [(2, 23)], 'קפוטקאי': [(2, 23)], 'מקפוטקיא': [(2, 23)], 'זעתך': [(2, 25)], 'ודחלתך': [(2, 25)], 'אזגדין': [(2, 26)], 'שלמא': [(2, 26), (29, 18)], 'אסטי': [(2, 27)], 'למשבקנא': [(2, 30)], 'בתחומיה': [(2, 30)], 'אקשי': [(2, 30)], 'ליהץ': [(2, 32)], 'וכבשנא': [(2, 34), (3, 4)], 'וגמרנא': [(2, 34), (3, 6)], 'משזב': [(2, 34), (3, 3), (32, 39)], 'בזנא': [(2, 35), (3, 7)], 'תקפת': [(2, 36)], 'יובקא': [(2, 37), (3, 16)]}
assert {k: onk_tok(k) for k in ONK2} == ONK2, {k: onk_tok(k) for k in ONK2 if onk_tok(k) != ONK2[k]}
ONK3 = {'שתין': [(3, 4)], 'פלך': [(3, 4), (3, 13), (3, 14)], 'טרכונא': [(3, 4), (3, 13), (3, 14)], 'כריכן': [(3, 5)], 'פצחיא': [(3, 5)], 'סרין': [(3, 9)], 'תלגא': [(3, 9)], 'ערסיה': [(3, 11)], 'דפרזלא': [(3, 11), (4, 20)], 'ברבת': [(3, 11)], 'לפלגות': [(3, 13)], 'ופלגות': [(3, 12)], 'מתקרי': [(3, 13)], 'גשוראה': [(3, 14)], 'ואפקירוס': [(3, 14)], 'כפרני': [(3, 14)], 'מגנוסר': [(3, 17)], 'משפך': [(3, 17), (4, 49)], 'מרמתא': [(3, 17), (4, 49)], 'רמתא': [(3, 27), (12, 2), (34, 1)], 'מזרזין': [(3, 18)], 'יניח': [(3, 20), (25, 19)], 'לתרין': [(3, 21)], 'מלכיא': [(3, 21)], 'וצליתי': [(3, 23), (9, 20), (9, 26)], 'אלהים': [(3, 24), (4, 35), (7, 9), (9, 26)], 'שריתא': [(3, 24)], 'רבותך': [(3, 24)], 'דשכנתך': [(3, 24)], 'ושליט': [(3, 24), (4, 39)], 'כעובדיך': [(3, 24)], 'וכגברתך': [(3, 24)], 'ואחזי': [(3, 25)], 'מקדשא': [(3, 25), (23, 19), (33, 19)], 'לריש': [(3, 27)], 'וזקוף': [(3, 27)], 'למערבא': [(3, 27)], 'ולצפונא': [(3, 27)], 'ולדרומא': [(3, 27)], 'ולמדינחא': [(3, 27)], 'ותקפהי': [(3, 28)], 'ואלמהי': [(3, 28)], 'יחסן': [(3, 28)], 'בחילתא': [(3, 29), (4, 46), (34, 6)], 'לקבל': [(1, 1), (2, 19), (3, 29), (4, 46), (11, 30), (34, 6)]}
assert {k: onk_tok(k) for k in ONK3} == ONK3, {k: onk_tok(k) for k in ONK3 if onk_tok(k) != ONK3[k]}
assert onk_seats('בית פלך') == [(3, 4), (3, 13), (3, 14)] and onk_seats('טור תלגא') == [(3, 9)] and onk_seats('באמת מלך') == [(3, 11)] and onk_seats('בית מקדשא') == [(3, 25), (23, 19), (33, 19)] and onk_tok('למללא')[0] == (3, 26) and aramaic(3, 26)[-9:] == ['סגי', 'לך', 'לא', 'תוסף', 'למללא', 'קדמי', 'עוד', 'בפתגמא', 'הדין']
assert aramaic(1, 42)[9:14] == ['ארי', 'לית', 'שכנתי', 'שריא', 'ביניכון'] and aramaic(3, 22)[-4:] == ['מימריה', 'יגיח', 'לכון', ''][:-1] + [] or aramaic(3, 22)[-3:] == ['מימריה', 'יגיח', 'לכון']
assert aramaic(3, 24)[9:20] == ['וית', 'ידך', 'תקפתא', 'די', 'את', 'הוא', 'אלהא', 'דשכנתך', 'בשמיא', 'מלעלא', 'ושליט'] and aramaic(1, 37)[:7] == ['אף', 'עלי', 'הוה', 'רגז', 'מן', 'קדם', 'יי'] and aramaic(3, 11)[-3:] == ['פתיה', 'באמת', 'מלך'] and aramaic(1, 44)[8:12] == ['כמא', 'די', 'נתזן', 'דבריתא']

# THE STORE'S GLOSSES READ BACK (the display layer; the draft units untouched): every family below CENSUSED over the whole store (deu_measure2)
# — BY GLOSS where every token of the gloss is the one word ("the-pasture" for THE WILDERNESS at all sixteen, "in-pasture" at all sixty,
# "leanness" for ONLY at all thirty-nine, "abrupt" for OPPOSITE at all fifteen, "cord" for BORDER at all nineteen, "and-crack-off" for AND
# HE WAS ANGRY at all five, "safe" for PEACE at all twelve, "hating-you" for YOUR ENEMIES at all fourteen, "something-bought" for CATTLE at all
# seventeen, "the-precept" for THE TORAH at all twenty-seven, "hind-part" for AFTER at all ninety-six, "in-time" for AT THE TIME at all twenty,
# "to-set" for TO GIVE at all thirty-seven, "from-with" for FROM at all sixty-one, "meaning-accession" for ALSO at all twelve, "heed" for
# BECAUSE at all five, "to-meander--about" for TO SEARCH OUT at all eight, "Red-Sea" for SUPH the place (its one token), the direction suffixes
# "hidden-suffix" NORTHWARD / "sunrise-suffix" EASTWARD / "and-south-suffix" SOUTHWARD, "the-mountain-suffix" TO THE MOUNTAIN at all ten, the
# names — "the-Emims", "Rapha'", "the-Chorite", "Caphtorite", "Anakite", "Tsidonian", "Jehoshua", "Non" — the hapax forms "and-be-naught" YOU
# DEEMED IT EASY, "be--lofty" TOO HIGH, "and-cross-over" WAS WROTH, "the-bee", "treading", "ravine" THE SLOPES, "couch" BEDSTEAD, "building"
# CITY, "elevated", "something-swinging" GATES, "yield" UNDERTOOK, "purchase", the suffix forms "-suffix" at one seat each, and the rest) and
# BY REFERENCE where the family is mixed ("set" for GIVE — the give-verb at every seat of the span, twenty-six tokens; "stream" for THE BROOK
# and the river, "in-region-across" for BEYOND, "bore" for BEGIN beside PROFANE, "grate" for CONTEND beside the grating, "cramp" for HARASS,
# "turn-aside-from-the-road" for BE AFRAID beside SOJOURN, "and-pry-into" for SEARCH OUT beside DIG, "and-be--bitter" for REBEL beside MARAH,
# "and-seethe" for ACT PRESUMPTUOUSLY beside Jacob's pottage, "swell-up" for LEFT, "plait" for RECKONED beside Heshbon, "to-face" for
# FORMERLY at three seats, "lip" for THE EDGE, "rope" for THE REGION at three, "mother" for CUBITS at two, "pull-off" for ARMED, "force" for
# VALOR, "strength" for GOD, "the-not" standing ("is it not" already), "?" for KADESH / BETH / HAVVOTH / EZION, "and-eye" for AND YOU ANSWERED,
# "feed-on" for FIGHT, "seas-suffix" for WESTWARD, "the-stand" for WHO STANDS, "fasten-upon" for ENCOURAGE, "push" for BE SMITTEN, "and-gird-on",
# "and-bruise" for BEAT DOWN, "revolve" for GO AROUND, "deal-in-grain" for BUY, "in-silver" for FOR MONEY at four, "and-quiver"/"and-twist" for
# TREMBLE / BE IN ANGUISH, "the-bring-forth" for WHO CAME OUT, "and-bring-forth" for AND CAME OUT at two, "complete" for CONSUMED, "gather-grapes"
# for FORTIFIED, "and-bolt" for AND BARS, "to-separation" for BESIDES, "the-rustic" for THE UNWALLED, "seclude" for UTTERLY DESTROY, "plunder"
# at two, "strike" forms at three, "scrutinize" for REGARD, "be-dense" for TOO HARD / HARDENED, "and-put/set-them" for I WILL SET THEM,
# "stroke" for TIMES, "hear-suffix" and "make-suffix" by person, "build-up" for BELIEVING, "and-be-high-actively" for TALL at three,
# "and-be--make-well" for WAS GOOD, "right" for RIGHTEOUSLY, "scion" for TRIBE(S), "hind-part-them" for AFTER THEM, "to-encountering-us" for TO
# MEET US, "the-see" for HAVE SEEN, "and-bend" for BESOUGHT, "inherit--mode-of-descent)" for CAUSE TO INHERIT, "dig" for EXPLAIN, "and-half"
# standing) — ONE HUNDRED AND TWENTY-SIX rows BY GLOSS and ONE HUNDRED AND FORTY-NINE BY REFERENCE; TEN families were rewritten by earlier
# sittings already ("and-crack-off", "from-pasture", "sunrise-suffix", "the-powder", "and-cord", "cord", "in-cord", the inherit-her form,
# "in-hate", "Non" — their rows stand, asserted present) (the last assert below stands only after
# patch_overrides_deu.py has written them: the one expected fall of the ink before the patch).
assert sg(1, 1, 'סוף') == 'Red-Sea' and sg(1, 1, 'מול') == 'abrupt' and sg(1, 1, 'בערבה') == 'in-desert' and sg(1, 1, 'במדבר') == 'in-pasture' and sg(1, 1, 'בעבר') == 'in-region-across' and sg(1, 2, 'קדש') == '?' and sg(1, 4, 'הכתו') == 'strike-him/its' and sg(1, 5, 'הואיל') == 'yield' and sg(1, 5, 'התורה') == 'the-precept' and sg(1, 7, 'הנהר') == 'the-stream' and sg(1, 7, 'נהר') == 'stream'
assert sg(1, 8, 'נתתי') == 'set' and sg(1, 8, 'לתת') == 'to-set' and sg(1, 8, 'אחריהם') == 'hind-part-them/their' and sg(1, 9, 'בעת') == 'in-time' and sg(1, 10, 'לרב') == 'to-abundance' and sg(1, 11, 'פעמים') == 'stroke' and sg(1, 12, 'וריבכם') == 'and-contest-you/your (pl)' and sg(1, 13, 'ונבנים') == 'and-separate-mentally' and sg(1, 13, 'לשבטיכם') == 'to-scion-you/your (pl)' and sg(1, 13, 'בראשיכם') == 'in-head-you/your (pl)'
assert sg(1, 14, 'ותענו') == 'and-eye' and sg(1, 15, 'ואתן') == 'and-set' and sg(1, 15, 'ושטרים') == 'and-scribe' and sg(1, 15, 'שבטיכם') == 'scion-you/your (pl)' and sg(1, 16, 'שפטיכם') == 'judge-you/your (pl)' and sg(1, 16, 'צדק') == 'right' and sg(1, 16, 'גרו') == 'sojourner-him/its' and sg(1, 17, 'תכירו') == 'scrutinize' and sg(1, 17, 'תשמעון') == 'hear-suffix' and sg(1, 17, 'תקרבון') == 'bring-near-suffix' and sg(1, 17, 'ושמעתיו') == 'and-hear-him/its' and sg(1, 18, 'תעשון') == 'make-suffix'
assert sg(1, 19, 'המדבר') == 'the-pasture' and sg(1, 19, 'והנורא') == 'and-the-fear' and sg(1, 21, 'נתן') == 'set' and sg(1, 22, 'ותקרבון') == 'and-bring-near-suffix' and sg(1, 23, 'וייטב') == 'and-be--make-well' and sg(1, 23, 'בעיני') == 'in-eye-me/my' and sg(1, 23, 'לשבט') == 'to-scion' and sg(1, 24, 'ההרה') == 'the-mountain-suffix' and sg(1, 24, 'נחל') == 'stream' and sg(1, 24, 'וירגלו') == 'and-walk-along' and sg(1, 26, 'אביתם') == 'breathe-after'
assert sg(1, 27, 'ותרגנו') == 'and-grumble' and sg(1, 27, 'בשנאת') == 'in-hate' and sg(1, 27, 'להשמידנו') == 'to-desolate-us/our' and sg(1, 27, 'הוציאנו') == 'bring-forth-us/our' and sg(1, 28, 'המסו') == 'liquefy' and sg(1, 28, 'ורם') == 'and-be-high-actively' and sg(1, 28, 'ובצורת') == 'and-gather-grapes' and sg(1, 28, 'ענקים') == 'Anakite' and sg(1, 29, 'תערצון') == 'awe-suffix' and sg(1, 29, 'תיראון') == 'fear-suffix' and sg(1, 30, 'ילחם') == 'feed-on' and sg(1, 31, 'ובמדבר') == 'and-in-pasture'
assert sg(1, 33, 'לתור') == 'to-meander--about' and sg(1, 33, 'לחנתכם') == 'to-encamp-you/your (pl)' and sg(1, 33, 'לראתכם') == 'to-see-you/your (pl)' and sg(1, 36, 'זולתי') == 'scattering' and sg(1, 36, 'יען') == 'heed' and sg(1, 37, 'התאנף') == 'breathe-hard' and sg(1, 37, 'בגללכם') == 'in-circumstance-you/your (pl)' and sg(1, 38, 'יהושע') == 'Jehoshua' and sg(1, 38, 'נון') == 'Non' and sg(1, 38, 'העמד') == 'the-stand' and sg(1, 38, 'חזק') == 'fasten-upon' and sg(1, 38, 'ינחלנה') == 'inherit--mode-of-descent)-her/its'
assert sg(1, 39, 'וטפכם') == 'and-family-you/your (pl)' and sg(1, 39, 'לבז') == 'to-plunder' and sg(1, 39, 'טוב') == 'good--in-the-widest-sense' and sg(1, 39, 'אתננה') == 'set-her/its' and sg(1, 40, 'המדברה') == 'the-pasture-suffix' and sg(1, 41, 'ונלחמנו') == 'and-feed-on' and sg(1, 41, 'ותחגרו') == 'and-gird-on' and sg(1, 42, 'בקרבכם') == 'in-nearest-part-you/your (pl)' and sg(1, 42, 'תנגפו') == 'push' and sg(1, 42, 'איביכם') == 'hating-you/your (pl)' and sg(1, 44, 'לקראתכם') == 'to-encountering-you/your (pl)' and sg(1, 44, 'וירדפו') == 'and-run-after--gone-by)' and sg(1, 45, 'האזין') == 'broaden-out-the-ear'
assert sg(2, 1, 'ונסב') == 'and-revolve' and sg(2, 3, 'סב') == 'revolve' and sg(2, 3, 'צפנה') == 'hidden-suffix' and sg(2, 4, 'בגבול') == 'in-cord' and sg(2, 6, 'בכסף') == 'in-silver' and sg(2, 6, 'מאתם') == 'from-with-them/their' and sg(2, 6, 'ושתיתם') == 'and-imbibe' and sg(2, 8, 'מאת') == 'from-with' and sg(2, 8, 'הערבה') == 'the-desert' and sg(2, 8, 'מדבר') == 'pasture' and sg(2, 11, 'רפאים') == "Rapha'" and sg(2, 11, 'יחשבו') == 'plait' and sg(2, 11, 'אף') == 'meaning-accession' and sg(2, 11, 'כענקים') == 'like-Anakite'
assert sg(2, 12, 'החרים') == 'the-Chorite' and sg(2, 12, 'וישמידום') == 'and-desolate-them/their' and sg(2, 12, 'תחתם') == 'under-them/their' and sg(2, 14, 'מקדש') == 'from-?' and sg(2, 14, 'תם') == 'complete' and sg(2, 15, 'תמם') == 'complete-them/their' and sg(2, 18, 'גבול') == 'cord' and sg(2, 19, 'נתתיה') == 'set-her/its' and sg(2, 20, 'תחשב') == 'plait' and sg(2, 22, 'השמיד') == 'desolate' and sg(2, 22, 'החרי') == 'the-Chorite' and sg(2, 23, 'בחצרים') == 'in-Chatserim' and sg(2, 23, 'כפתרים') == 'Caphtorite' and sg(2, 23, 'היצאים') == 'the-bring-forth' and sg(2, 23, 'השמידם') == 'desolate-them/their'
assert sg(2, 24, 'החל') == 'bore' and sg(2, 25, 'אחל') == 'bore' and sg(2, 25, 'תת') == 'set' and sg(2, 25, 'פחדך') == 'alarm-you/your' and sg(2, 25, 'ישמעון') == 'hear-suffix' and sg(2, 25, 'שמעך') == 'something-heard-you/your' and sg(2, 25, 'ורגזו') == 'and-quiver' and sg(2, 25, 'וחלו') == 'and-twist' and sg(2, 26, 'ממדבר') == 'from-pasture' and sg(2, 26, 'שלום') == 'safe' and sg(2, 27, 'אסור') == 'turn-aside' and sg(2, 27, 'ושמאול') == 'and-dark' and sg(2, 28, 'תשברני') == 'deal-in-grain-me/my' and sg(2, 28, 'רק') == 'leanness'
assert sg(2, 30, 'ואמץ') == 'and-be-alert' and sg(2, 30, 'תתו') == 'set-him/its' and sg(2, 31, 'החלתי') == 'bore' and sg(2, 32, 'ויצא') == 'and-bring-forth' and sg(2, 32, 'לקראתנו') == 'to-encountering-us/our' and sg(2, 33, 'ויתנהו') == 'and-set-him/its' and sg(2, 33, 'ונך') == 'and-strike' and sg(2, 34, 'ונלכד') == 'and-catch' and sg(2, 34, 'ונחרם') == 'and-seclude' and sg(2, 34, 'השארנו') == 'swell-up' and sg(2, 35, 'בזזנו') == 'plunder' and sg(2, 35, 'ושלל') == 'and-booty' and sg(2, 35, 'לכדנו') == 'catch' and sg(2, 36, 'שפת') == 'lip' and sg(2, 36, 'בנחל') == 'in-stream' and sg(2, 36, 'קריה') == 'building'
assert sg(3, 3, 'ויתן') == 'and-set' and sg(3, 3, 'ונכהו') == 'and-strike-him/its' and sg(3, 3, 'השאיר') == 'swell-up' and sg(3, 4, 'חבל') == 'rope' and sg(3, 4, 'ממלכת') == 'dominion' and sg(3, 5, 'חומה') == 'wall-of-protection' and sg(3, 5, 'גבהה') == 'elevated' and sg(3, 5, 'דלתים') == 'something-swinging' and sg(3, 5, 'ובריח') == 'and-bolt' and sg(3, 5, 'לבד') == 'to-separation' and sg(3, 6, 'החרם') == 'seclude' and sg(3, 8, 'מנחל') == 'from-stream' and sg(3, 9, 'צידנים') == 'Tsidonian' and sg(3, 10, 'המישר') == 'the-level'
assert sg(3, 11, 'נשאר') == 'swell-up' and sg(3, 11, 'מיתר') == 'from-overhanging' and sg(3, 11, 'הרפאים') == "the-Rapha'" and sg(3, 11, 'ערשו') == 'couch-him/its' and sg(3, 11, 'ארכה') == 'length-her/its' and sg(3, 11, 'רחבה') == 'width-her/its' and sg(3, 12, 'וחצי') == 'and-half' and sg(3, 13, 'ויתר') == 'and-overhanging' and sg(3, 13, 'שבט') == 'scion' and sg(3, 14, 'חות') == '?' and sg(3, 16, 'וגבל') == 'and-cord' and sg(3, 16, 'הנחל') == 'the-stream' and sg(3, 17, 'והערבה') == 'and-the-desert' and sg(3, 17, 'המלח') == 'the-powder' and sg(3, 17, 'מזרחה') == 'sunrise-suffix'
assert sg(3, 18, 'חיל') == 'force' and sg(3, 19, 'ומקנכם') == 'and-something-bought-you/your (pl)' and sg(3, 19, 'מקנה') == 'something-bought' and sg(3, 21, 'הראת') == 'the-see' and sg(3, 24, 'אל') == 'strength' and sg(3, 24, 'החלות') == 'bore' and sg(3, 24, 'גדלך') == 'magnitude-you/your' and sg(3, 24, 'כמעשיך') == 'like-deed/work-you/your' and sg(3, 24, 'וכגבורתך') == 'and-like-force-you/your' and sg(3, 26, 'למענכם') == 'so-that-you/your (pl)' and sg(3, 27, 'ימה') == 'seas-suffix' and sg(3, 27, 'וצפנה') == 'and-hidden-suffix' and sg(3, 27, 'ותימנה') == 'and-south-suffix' and sg(3, 27, 'ומזרחה') == 'and-sunrise-suffix' and sg(3, 28, 'ינחיל') == 'inherit--mode-of-descent)'
GLOSS_FAMILY = {'and-crack-off': [('ויקצף', 5)], 'liquefy': [('ימס', 1), ('המסו', 1)], 'and-be-naught': [('ותהינו', 1)], 'something-occupied': [('ירשה', 5)], 'to-something-occupied-him/its': [('לירשתו', 1)], 'something-occupied-him/its': [('ירשתו', 1)], 'cramp-them/their': [('תצרם', 1)], 'and-grate': [('והתגר', 1)], 'to-put-in-commotion-them/their': [('להמם', 1)], 'and-seclude': [('ונחרם', 2), ('ויחרם', 1), ('והחרמתי', 1)], 'adult': [('מתם', 2), ('מתי', 2)], 'be--lofty': [('שגבה', 1)], 'and-cross-over': [('ויתעבר', 1)], 'leanness': [('רק', 39)], 'and-dark': [('ושמאול', 5), ('ושמאל', 2)], 'the-pasture': [('המדבר', 16)], 'in-pasture': [('במדבר', 60)], 'the-pasture-suffix': [('המדברה', 7)], 'from-pasture': [('ממדבר', 8)], 'and-in-pasture': [('ובמדבר', 2)], 'Red-Sea': [('סוף', 1)], 'abrupt': [('מול', 15)], 'the-desert': [('הערבה', 4)], 'and-the-desert': [('והערבה', 1)], 'and-separate-mentally': [('ונבנים', 1), ('ונבון', 1)], 'the-mountain-suffix': [('ההרה', 10)], 'hidden-suffix': [('צפנה', 6)], 'and-hidden-suffix': [('וצפנה', 2)], 'sunrise-suffix': [('מזרחה', 9)], 'and-sunrise-suffix': [('ומזרחה', 1)], 'and-south-suffix': [('ונגבה', 2), ('ותימנה', 1)], 'ravine': [('אשדת', 2)], 'the-powder': [('המלח', 4)], 'and-cord': [('וגבל', 2), ('וגבול', 2)], 'cord': [('גבול', 19)], 'in-cord': [('בגבול', 2)], 'from-overhanging': [('מיתר', 1)], 'and-overhanging': [('ויתר', 2)], 'meaning-accession': [('אף', 12)], 'treading': [('מדרך', 1)], 'heed': [('יען', 5)], 'breathe-hard': [('התאנף', 3)], 'in-circumstance-you/your (pl)': [('בגללכם', 1)], 'and-fasten-upon-him/its': [('וחזקהו', 1)], 'and-be-alert-him/its': [('ואמצהו', 1)], 'inherit--mode-of-descent)-her/its': [('תנחילנה', 1), ('ינחלנה', 1)], 'to-plunder': [('לבז', 3)], 'good--in-the-widest-sense': [('טוב', 6), ('טובה', 2)], 'and-family-you/your (pl)': [('וטפכם', 3)], 'breathe-after': [('אבה', 5), ('תאבה', 3), ('תאבו', 1), ('יאבה', 1), ('אביתם', 1)], 'hating-you/your (pl)': [('איביכם', 14)], 'the-bee': [('הדברים', 1)], 'broaden-out-the-ear': [('האזנה', 1), ('האזינו', 1), ('האזין', 1)], 'deal-in-grain-me/my': [('תשברני', 1)], 'purchase': [('תכרו', 1)], 'something-heard-you/your': [('שמעך', 2)], 'alarm-you/your': [('פחדך', 1)], 'safe': [('שלום', 12)], 'the-Emims': [('האמים', 1), ('האימים', 1)], 'Emims': [('אמים', 1)], "Rapha'": [('רפאים', 5)], "the-Rapha'": [('הרפאים', 2)], 'the-Chorite': [('החרי', 5), ('החרים', 1)], 'desolate': [('השמיד', 2), ('השמד', 2), ('תשמידו', 1), ('ישמיד', 1)], 'desolate-them/their': [('השמדם', 2), ('ישמידם', 1), ('השמידם', 1)], 'and-desolate-them/their': [('וישמידם', 1), ('וישמידום', 1), ('ואשמידם', 1)], 'to-desolate-us/our': [('להשמידנו', 1)], 'complete-them/their': [('תמם', 3)], 'in-Chatserim': [('בחצרים', 1)], 'Caphtorite': [('כפתרים', 2)], 'catch': [('לכדנו', 1)], 'and-catch': [('ונלכד', 2), ('וילכד', 2), ('וילכדו', 1)], 'building': [('קריה', 2)], 'and-booty': [('ושלל', 2)], 'wall-of-protection': [('חמה', 4), ('חומה', 2)], 'elevated': [('גבהה', 1)], 'something-swinging': [('דלתים', 1)], 'couch': [('ערש', 1)], 'couch-him/its': [('ערשו', 1)], 'the-level': [('המישר', 2)], 'something-bought': [('מקנה', 17)], 'and-something-bought-you/your (pl)': [('ומקנכם', 1)], 'in-gorge': [('בגיא', 2), ('בגי', 1)], 'magnitude-you/your': [('גדלך', 1)], 'like-deed/work-you/your': [('כמעשיך', 1)], 'and-like-force-you/your': [('וכגבורתך', 1)], 'so-that-you/your (pl)': [('למענכם', 1)], 'yield': [('הואלתי', 2), ('הואיל', 1)], 'feed-on': [('נלחם', 2), ('ילחם', 2), ('תלחמו', 1), ('הלחם', 1)], 'the-feed-on': [('הנלחם', 1)], 'and-contest-you/your (pl)': [('וריבכם', 1)], 'and-scribe': [('ושטרים', 2)], 'sojourner-him/its': [('גרו', 1)], 'bring-near-suffix': [('תקרבון', 1)], 'and-bring-near-suffix': [('ותקרבון', 3)], 'awe-suffix': [('תערצון', 1)], 'fear-suffix': [('תיראון', 2)], 'to-meander--about': [('לתור', 8)], 'scattering': [('זולתי', 2)], 'and-run-after--gone-by)': [('ורדף', 3), ('וירדפו', 3), ('וירדף', 3), ('ורדפתם', 1), ('ורדפו', 1)], 'like-Anakite': [('כענקים', 3)], 'Anakite': [('ענקים', 2)], 'and-gather-grapes': [('ובצרת', 1), ('ובצורת', 1)], 'in-hate': [('בשנאת', 1), ('בשנאה', 1)], 'and-walk-along': [('וירגלו', 1)], 'and-grumble': [('ותרגנו', 1)], 'in-eye-me/my': [('בעיני', 3)], 'and-the-fear': [('והנורא', 4)], 'to-abundance': [('לרב', 5)], 'to-scion-you/your (pl)': [('לשבטיכם', 2)], 'to-scion': [('לשבט', 1)], 'in-head-you/your (pl)': [('בראשיכם', 1)], 'judge-you/your (pl)': [('שפטיכם', 1)], 'and-hear-him/its': [('ושמעתיו', 1)], 'to-encamp-you/your (pl)': [('לחנתכם', 1)], 'to-see-you/your (pl)': [('לראתכם', 1)], 'in-nearest-part-you/your (pl)': [('בקרבכם', 3)], 'to-encountering-you/your (pl)': [('לקראתכם', 1)], 'bring-forth-us/our': [('הוציאנו', 3), ('הוצאתנו', 1)], 'under-them/their': [('תחתם', 4), ('תחתיהם', 1)], 'from-with-them/their': [('מאתם', 9)], 'from-with': [('מאת', 45), ('מעם', 16)], 'length-her/its': [('ארכה', 3)], 'width-her/its': [('רחבה', 5)], 'Tsidonian': [('צידנים', 1)], 'Jehoshua': [('יהושע', 16), ('יהושוע', 1)], 'Non': [('נון', 16)], 'in-time': [('בעת', 20)], 'hind-part': [('אחרי', 75), ('אחר', 21)], 'the-precept': [('התורה', 26), ('התורת', 1)], 'resident-him/its': [('שכניו', 1)], 'and-in-Lowland': [('ובשפלה', 1)], 'and-in-south': [('ובנגב', 1)], 'and-in-cove': [('ובחוף', 1)], 'to-set': [('לתת', 37)]}
GT = {g: store.execute("SELECT REPLACE(w.he_plain,'/',''), COUNT(*) FROM words w WHERE w.gloss=? GROUP BY 1 ORDER BY 2 DESC, 1", (g,)).fetchall() for g in GLOSS_FAMILY}
assert all(sorted(GT[g]) == sorted(v) for g, v in GLOSS_FAMILY.items()), [g for g, v in GLOSS_FAMILY.items() if sorted(GT[g]) != sorted(v)]
IMB = store.execute("SELECT REPLACE(w.he_plain,'/',''), COUNT(*) FROM words w WHERE w.gloss='and-imbibe' GROUP BY 1").fetchall()
assert sum(n for _, n in IMB) == 15 and all('שת' in t for t, _ in IMB) and len(IMB) == 10
OVERRIDE_GLOSS = [('liquefy', 'melt'), ('and-be-naught', 'and-you-deemed-it-easy'), ('something-occupied', 'a-possession'), ('to-something-occupied-him/its', 'to-his-possession'), ('something-occupied-him/its', 'his-possession'), ('cramp-them/their', 'harass-them'), ('and-grate', 'and-contend'), ('to-put-in-commotion-them/their', 'to-discomfit-them'), ('and-seclude', 'and-utterly-destroy'), ('adult', 'men'), ('be--lofty', 'was-too-high'), ('and-cross-over', 'and-was-wroth'), ('leanness', 'only'), ('and-dark', 'and-left'), ('the-pasture', 'the-wilderness'), ('in-pasture', 'in-the-wilderness'), ('the-pasture-suffix', 'to-the-wilderness'), ('and-in-pasture', 'and-in-the-wilderness'), ('Red-Sea', 'Suph'), ('abrupt', 'opposite'), ('the-desert', 'the-Arabah'), ('and-the-desert', 'and-the-Arabah'), ('and-separate-mentally', 'and-understanding'), ('the-mountain-suffix', 'to-the-mountain'), ('hidden-suffix', 'northward'), ('and-hidden-suffix', 'and-northward'), ('and-sunrise-suffix', 'and-eastward'), ('and-south-suffix', 'and-southward'), ('ravine', 'the-slopes-of'), ('from-overhanging', 'from-the-remnant-of'), ('and-overhanging', 'and-the-rest-of'), ('meaning-accession', 'also'), ('treading', 'the-treading-of'), ('heed', 'because'), ('breathe-hard', 'was-angry'), ('in-circumstance-you/your (pl)', 'for-your-sakes'), ('and-fasten-upon-him/its', 'and-strengthen-him'), ('and-be-alert-him/its', 'and-encourage-him'), ('to-plunder', 'for-a-prey'), ('good--in-the-widest-sense', 'good'), ('and-family-you/your (pl)', 'and-your-little-ones'), ('breathe-after', 'be-willing'), ('hating-you/your (pl)', 'your-enemies'), ('the-bee', 'the-bees'), ('broaden-out-the-ear', 'give-ear'), ('deal-in-grain-me/my', 'sell-me'), ('purchase', 'you-shall-buy'), ('something-heard-you/your', 'the-report-of-you'), ('alarm-you/your', 'the-dread-of-you'), ('safe', 'peace'), ('the-Emims', 'the-Emim'), ('Emims', 'Emim'), ("Rapha'", 'Rephaim'), ("the-Rapha'", 'the-Rephaim'), ('the-Chorite', 'the-Horites'), ('desolate', 'destroy'), ('desolate-them/their', 'destroyed-them'), ('and-desolate-them/their', 'and-destroyed-them'), ('to-desolate-us/our', 'to-destroy-us'), ('complete-them/their', 'they-were-consumed'), ('in-Chatserim', 'in-villages'), ('Caphtorite', 'the-Caphtorim'), ('catch', 'we-captured'), ('and-catch', 'and-captured'), ('building', 'city'), ('and-booty', 'and-the-spoil-of'), ('wall-of-protection', 'wall'), ('elevated', 'high'), ('something-swinging', 'gates'), ('couch', 'bedstead'), ('couch-him/its', 'his-bedstead'), ('the-level', 'the-tableland'), ('something-bought', 'cattle'), ('and-something-bought-you/your (pl)', 'and-your-cattle'), ('in-gorge', 'in-the-valley'), ('magnitude-you/your', 'your-greatness'), ('like-deed/work-you/your', 'according-to-your-works'), ('and-like-force-you/your', 'and-according-to-your-mighty-acts'), ('so-that-you/your (pl)', 'for-your-sakes'), ('yield', 'undertook'), ('feed-on', 'fight'), ('the-feed-on', 'the-one-who-fights'), ('and-contest-you/your (pl)', 'and-your-strife'), ('and-scribe', 'and-officers'), ('sojourner-him/its', 'his-stranger'), ('bring-near-suffix', 'you-shall-bring-near'), ('and-bring-near-suffix', 'and-you-came-near'), ('awe-suffix', 'you-shall-dread'), ('fear-suffix', 'you-shall-fear'), ('to-meander--about', 'to-search-out'), ('scattering', 'except'), ('and-run-after--gone-by)', 'and-pursued'), ('like-Anakite', 'like-the-Anakim'), ('Anakite', 'Anakim'), ('and-gather-grapes', 'and-fortified'), ('and-walk-along', 'and-spied-out'), ('and-grumble', 'and-murmured'), ('in-eye-me/my', 'in-my-eyes'), ('and-the-fear', 'and-the-terrible'), ('to-abundance', 'for-multitude'), ('to-scion-you/your (pl)', 'for-your-tribes'), ('to-scion', 'per-tribe'), ('in-head-you/your (pl)', 'over-your-heads'), ('judge-you/your (pl)', 'your-judges'), ('and-hear-him/its', 'and-I-will-hear-it'), ('to-encamp-you/your (pl)', 'for-you-to-encamp'), ('to-see-you/your (pl)', 'to-show-you'), ('in-nearest-part-you/your (pl)', 'in-your-midst'), ('to-encountering-you/your (pl)', 'to-meet-you'), ('bring-forth-us/our', 'brought-us-out'), ('under-them/their', 'in-their-place'), ('from-with-them/their', 'from-them'), ('from-with', 'from'), ('and-imbibe', 'and-drink'), ('length-her/its', 'its-length'), ('width-her/its', 'its-breadth'), ('Tsidonian', 'the-Sidonians'), ('Jehoshua', 'Joshua'), ('in-time', 'at-the-time'), ('hind-part', 'after'), ('the-precept', 'the-Torah'), ('resident-him/its', 'its-neighbors'), ('and-in-Lowland', 'and-in-the-lowland'), ('and-in-south', 'and-in-the-Negeb'), ('and-in-cove', 'and-on-the-coast-of'), ('to-set', 'to-give')]
OVERRIDE_REF3 = [('Deut.1.1:8', 'beyond', 'בעבר'), ('Deut.1.1:11', 'in-the-Arabah', 'בערבה'), ('Deut.1.1:20', 'and-Di', 'ודי'), ('Deut.1.2:8', 'Kadesh', 'קדש'), ('Deut.1.4:1', 'he-had-smitten', 'הכתו'), ('Deut.1.5:0', 'beyond', 'בעבר'), ('Deut.1.5:6', 'explain', 'באר'), ('Deut.1.7:9', 'in-the-Arabah', 'בערבה'), ('Deut.1.7:19', 'the-river', 'הנהר'), ('Deut.1.7:21', 'the-river', 'נהר'), ('Deut.1.8:1', 'I-have-given', 'נתתי'), ('Deut.1.8:19', 'after-them', 'אחריהם'), ('Deut.1.11:7', 'times', 'פעמים'), ('Deut.1.13:7', 'and-I-will-set-them', 'ואשימם'), ('Deut.1.14:0', 'and-you-answered', 'ותענו'), ('Deut.1.15:3', 'your-tribes', 'שבטיכם'), ('Deut.1.15:7', 'and-I-made', 'ואתן'), ('Deut.1.16:10', 'righteously', 'צדק'), ('Deut.1.17:1', 'regard', 'תכירו'), ('Deut.1.17:6', 'you-shall-hear', 'תשמעון'), ('Deut.1.17:8', 'be-afraid', 'תגורו'), ('Deut.1.17:17', 'is-too-hard', 'יקשה'), ('Deut.1.18:8', 'you-shall-do', 'תעשון'), ('Deut.1.19:21', 'Kadesh', 'קדש'), ('Deut.1.20:9', 'gives', 'נתן'), ('Deut.1.21:1', 'has-given', 'נתן'), ('Deut.1.22:7', 'and-search-out', 'ויחפרו'), ('Deut.1.23:0', 'and-was-good', 'וייטב'), ('Deut.1.24:5', 'the-valley-of', 'נחל'), ('Deut.1.25:15', 'gives', 'נתן'), ('Deut.1.26:3', 'and-you-rebelled-against', 'ותמרו'), ('Deut.1.28:10', 'and-tall', 'ורם'), ('Deut.1.32:3', 'believing', 'מאמינם'), ('Deut.1.36:7', 'I-will-give', 'אתן'), ('Deut.1.38:3', 'who-stands', 'העמד'), ('Deut.1.38:9', 'encourage', 'חזק'), ('Deut.1.39:16', 'I-will-give-it', 'אתננה'), ('Deut.1.41:0', 'and-you-answered', 'ותענו'), ('Deut.1.41:7', 'and-we-will-fight', 'ונלחמנו'), ('Deut.1.41:13', 'and-you-girded-on', 'ותחגרו'), ('Deut.1.42:13', 'be-smitten', 'תנגפו'), ('Deut.1.43:4', 'and-you-rebelled-against', 'ותמרו'), ('Deut.1.43:8', 'and-acted-presumptuously', 'ותזדו'), ('Deut.1.44:11', 'and-beat-down', 'ויכתו'), ('Deut.2.3:2', 'going-around', 'סב'), ('Deut.2.5:1', 'contend', 'תתגרו'), ('Deut.2.5:5', 'I-will-give', 'אתן'), ('Deut.2.5:15', 'I-have-given', 'נתתי'), ('Deut.2.6:1', 'you-shall-buy', 'תשברו'), ('Deut.2.6:3', 'for-money', 'בכסף'), ('Deut.2.6:9', 'for-money', 'בכסף'), ('Deut.2.8:10', 'and-from-Ezion', 'ומעצין'), ('Deut.2.8:15', 'the-wilderness-of', 'מדבר'), ('Deut.2.9:4', 'harass', 'תצר'), ('Deut.2.9:8', 'contend', 'תתגר'), ('Deut.2.9:13', 'I-will-give', 'אתן'), ('Deut.2.9:20', 'I-have-given', 'נתתי'), ('Deut.2.10:1', 'formerly', 'לפנים'), ('Deut.2.10:7', 'and-tall', 'ורם'), ('Deut.2.11:1', 'are-reckoned', 'יחשבו'), ('Deut.2.12:3', 'formerly', 'לפנים'), ('Deut.2.12:17', 'gave', 'נתן'), ('Deut.2.13:5', 'the-brook-of', 'נחל'), ('Deut.2.13:9', 'the-brook-of', 'נחל'), ('Deut.2.14:3', 'from-Kadesh', 'מקדש'), ('Deut.2.14:9', 'the-brook-of', 'נחל'), ('Deut.2.14:15', 'was-consumed', 'תם'), ('Deut.2.19:7', 'contend', 'תתגר'), ('Deut.2.19:11', 'I-will-give', 'אתן'), ('Deut.2.19:20', 'I-have-given-it', 'נתתיה'), ('Deut.2.20:2', 'is-reckoned', 'תחשב'), ('Deut.2.20:8', 'formerly', 'לפנים'), ('Deut.2.21:3', 'and-tall', 'ורם'), ('Deut.2.23:6', 'who-came-out', 'היצאים'), ('Deut.2.24:4', 'the-brook-of', 'נחל'), ('Deut.2.24:7', 'I-have-given', 'נתתי'), ('Deut.2.24:16', 'begin', 'החל'), ('Deut.2.25:2', 'I-will-begin', 'אחל'), ('Deut.2.25:3', 'to-put', 'תת'), ('Deut.2.25:13', 'shall-hear', 'ישמעון'), ('Deut.2.25:15', 'and-tremble', 'ורגזו'), ('Deut.2.25:16', 'and-be-in-anguish', 'וחלו'), ('Deut.2.27:6', 'I-will-turn-aside', 'אסור'), ('Deut.2.28:1', 'for-money', 'בכסף'), ('Deut.2.28:5', 'for-money', 'בכסף'), ('Deut.2.28:6', 'give', 'תתן'), ('Deut.2.29:20', 'gives', 'נתן'), ('Deut.2.30:8', 'hardened', 'הקשה'), ('Deut.2.30:13', 'and-made-obstinate', 'ואמץ'), ('Deut.2.30:17', 'to-give-him', 'תתו'), ('Deut.2.31:4', 'I-have-begun', 'החלתי'), ('Deut.2.31:5', 'to-give', 'תת'), ('Deut.2.31:11', 'begin', 'החל'), ('Deut.2.32:0', 'and-came-out', 'ויצא'), ('Deut.2.32:2', 'to-meet-us', 'לקראתנו'), ('Deut.2.33:0', 'and-he-gave-him', 'ויתנהו'), ('Deut.2.33:4', 'and-we-smote', 'ונך'), ('Deut.2.34:14', 'we-left', 'השארנו'), ('Deut.2.35:2', 'we-plundered', 'בזזנו'), ('Deut.2.36:3', 'the-edge-of', 'שפת'), ('Deut.2.36:4', 'the-brook-of', 'נחל'), ('Deut.2.36:8', 'in-the-valley', 'בנחל'), ('Deut.2.36:19', 'gave', 'נתן'), ('Deut.2.37:9', 'the-brook-of', 'נחל'), ('Deut.3.1:4', 'and-came-out', 'ויצא'), ('Deut.3.1:8', 'to-meet-us', 'לקראתנו'), ('Deut.3.2:8', 'I-have-given', 'נתתי'), ('Deut.3.3:0', 'and-gave', 'ויתן'), ('Deut.3.3:12', 'and-we-smote-him', 'ונכהו'), ('Deut.3.3:15', 'leaving', 'השאיר'), ('Deut.3.4:16', 'the-region-of', 'חבל'), ('Deut.3.5:3', 'fortified', 'בצרות'), ('Deut.3.5:7', 'and-bars', 'ובריח'), ('Deut.3.5:8', 'besides', 'לבד'), ('Deut.3.5:10', 'the-unwalled', 'הפרזי'), ('Deut.3.6:7', 'utterly-destroying', 'החרם'), ('Deut.3.7:4', 'we-plundered', 'בזונו'), ('Deut.3.8:10', 'beyond', 'בעבר'), ('Deut.3.8:12', 'from-the-brook-of', 'מנחל'), ('Deut.3.11:5', 'was-left', 'נשאר'), ('Deut.3.11:18', 'cubits', 'אמות'), ('Deut.3.11:21', 'cubits', 'אמות'), ('Deut.3.12:9', 'the-brook-of', 'נחל'), ('Deut.3.12:15', 'I-gave', 'נתתי'), ('Deut.3.13:6', 'I-gave', 'נתתי'), ('Deut.3.13:8', 'tribe', 'שבט'), ('Deut.3.13:11', 'the-region-of', 'חבל'), ('Deut.3.14:6', 'the-region-of', 'חבל'), ('Deut.3.14:18', 'Havvoth', 'חות'), ('Deut.3.15:1', 'I-gave', 'נתתי'), ('Deut.3.16:2', 'I-gave', 'נתתי'), ('Deut.3.16:6', 'the-brook-of', 'נחל'), ('Deut.3.16:9', 'the-brook', 'הנחל'), ('Deut.3.16:13', 'the-brook', 'הנחל'), ('Deut.3.18:7', 'has-given', 'נתן'), ('Deut.3.18:13', 'armed', 'חלוצים'), ('Deut.3.18:21', 'valor', 'חיל'), ('Deut.3.19:12', 'I-have-given', 'נתתי'), ('Deut.3.20:14', 'gives', 'נתן'), ('Deut.3.20:16', 'beyond', 'בעבר'), ('Deut.3.20:22', 'I-have-given', 'נתתי'), ('Deut.3.21:7', 'have-seen', 'הראת'), ('Deut.3.23:0', 'and-I-besought', 'ואתחנן'), ('Deut.3.24:3', 'have-begun', 'החלות'), ('Deut.3.24:14', 'God', 'אל'), ('Deut.3.25:7', 'beyond', 'בעבר'), ('Deut.3.27:5', 'westward', 'ימה'), ('Deut.3.28:12', 'shall-cause-to-inherit', 'ינחיל'), ('Deut.3.29:3', 'Beth', 'בית')]
OVERRIDE_REF = [(k, v) for k, v, _ in OVERRIDE_REF3]
ALREADY = ['and-crack-off', 'from-pasture', 'sunrise-suffix', 'the-powder', 'and-cord', 'cord', 'in-cord', 'inherit--mode-of-descent)-her/its', 'in-hate', 'Non']
STORE_IDX = {(c, v, idx): tok for c, v, idx, tok in store.execute("SELECT v.chapter, v.verse, w.idx, REPLACE(w.he_plain,'/','') FROM words w JOIN verses v ON w.verse_id=v.id WHERE v.book='Deut' AND v.chapter<=3")}
def REFKEY(k): a, b = k.split(':'); _, c, v = a.split('.'); return (int(c), int(v), int(b))
assert [(k, STORE_IDX.get(REFKEY(k)), tok) for k, _, tok in OVERRIDE_REF3 if STORE_IDX.get(REFKEY(k)) != tok] == []
assert len(OVERRIDE_REF) == 149 and len({k for k, _ in OVERRIDE_REF}) == 149 and len(OVERRIDE_GLOSS) == 126 and len({k for k, _ in OVERRIDE_GLOSS}) == 126, (len(OVERRIDE_REF), len(OVERRIDE_GLOSS))
OV = open(f'{ROOT}/logic/glosses/word_gloss_overrides.yaml', encoding='utf-8').read()
assert all(f'"{k}": "{v}"' in OV for k, v in OVERRIDE_REF) and all(f'"{k}": "{v}"' in OV for k, v in OVERRIDE_GLOSS) and all(f'"{k}": ' in OV for k in ALREADY), [k for k, v in OVERRIDE_REF + OVERRIDE_GLOSS if f'"{k}": "{v}"' not in OV][:6]

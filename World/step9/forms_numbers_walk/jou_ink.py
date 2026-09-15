import os as _os
_ROOT = _os.path.normpath(_os.path.join(_os.path.dirname(_os.path.abspath(__file__)), '..', '..', '..'))   # THE PORTABLE REPO (2026-09-15): the repo root from this file's own place
#!/usr/bin/env python3
# THE NUMBERS WALK, sitting 13 — THE JOURNEYS, Numbers 33:1-56 (2026-09-12; the owner: "Go" after the #151 rereads, on the ruling READ THEN
# COMPILE): THE INK of the chapter, computed from the Tanakh DB, the snapshot store and the shelf's own bytes — never typed. Sitting 12's form
# (gad_ink.py): the heads found BY POSITION and asserted (NO piska on chapter 33 — the shelf silent from 31:25 to 35:8; the whole export scanned
# for a row citing the chapter in both files, "Ibid." and the gershayim form included: ONE row of another chapter cites it, 133:3 on 27:2 citing
# 33:38, credited); coverage computed; every cut by consonants (the misses collected, asserted empty); the engine's numeral parser MEASURED on
# every verse (five number verses, every one read — 33:38's date the tape's own marker at 20:28); the hand's facts as asserts, run all at once
# by assert_driver.py after the measurement passes (jou_measure1.py, jou_measure2.py) printed them; every gloss of a narrative verb the STORE'S
# OWN (words.gloss); the piece-wise cutters HP / AP. Shared by jou_rows_onkelos_a.py / _b.py and write_jou_ledger.py.
# THE SPAN: ONE draft — num_33_journeys 33:1-56 (the portion Masei's first chapter); the next draft (num_34_borders) opens at 34:1.
import json, os, re, html, sqlite3, sys, io, contextlib, unicodedata
from collections import Counter
ROOT = _ROOT
DATE = '2026-09-12'
UID = 'num_33_journeys'
PISKAOT = []
CREDITED = [(133, 3, (33, 38))]
TITLE = 'The journeys — these are the journeys of the children of Israel by their hosts by the hand of Moses and Aaron; Moses wrote their goings out by the mouth of the LORD; from Rameses on the fifteenth of the first month, the morrow of the Passover, with a high hand while Egypt buried its firstborn and the LORD executed judgments on their gods; forty-two journeys and forty-two camps, Rameses to the plains of Moab; Aaron went up Mount Hor by the mouth of the LORD and died in the fortieth year, the fifth month, the first of the month, a hundred and twenty-three years old; the Canaanite king of Arad heard; the command in the plains of Moab: drive out the inhabitants, destroy the figured stones, the molten images and the high places, inherit the land by lot, and if you do not, thorns in your eyes and pricks in your sides'
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
# THE SHELF BY POSITION: piska 158 (31:22) is followed by 159 (35:9) — NO piska on chapter 33 (nor on 32 or 34): the shelf silent from 31:25 to
# 35:8, as sitting 11 computed (165 verses); this chapter is the THIRD stretch of that silence read on the translation alone. THE "FOUND BY
# POSITION" CLAUSE run on the whole export in both files — the English's "(Bamidbar 33:n)" AND its "(Ibid. 33:n)", the Hebrew's citation with
# the gershayim (במדבר ל״ג — "Numbers 33"): the English "Ibid." hits at 69:2 and 151:1 are GENESIS 33:4 (Esau's kiss) and JEREMIAH 33:1 —
# the abbreviation's book is the row's last-named one, read to its verse; ONE row of another chapter cites Numbers 33 — 133:3 (on 27:2), citing
# 33:38 to date the daughters' standing before Moses and Eleazar in the fortieth year, after Aaron's death. Read whole at THE TENT sitting 4 (the
# num_27_zelophehad_joshua ledger) and CREDITED here with a QUICK LOOK (credit guard 1: opened again this sitting in both files — what it says
# of 33 is one dating clause). The first scan (jou_dump.py) missed it on both regexes: the English row says "Ibid.", the Hebrew row writes the
# chapter with the gershayim, not a straight quote — the instrument widened before the claim was typed (RESEARCH_LOG).
assert heads[157] == ('Bamidbar', 31, 1) and heads[158] == ('Bamidbar', 31, 22) and heads[159] == ('Bamidbar', 35, 9) and len(sif) == 161
assert sorted(p for p, h in heads.items() if h and h[0] == 'Bamidbar' and h[1] in (32, 33, 34)) == [] and [p for p, h in heads.items() if h and h[0] == 'Bamidbar' and h[1] == 35 and h[2] < 9] == []
EN_CITING = [(p, r, re.findall(r'\((?:Bamidbar|Ibid)\.? 33:(\d+)', clean(row))) for p, rows in enumerate(sif, 1) for r, row in enumerate(rows, 1) if re.search(r'\((?:Bamidbar|Ibid)\.? 33:\d+', clean(row))]
assert EN_CITING == [(69, 2, ['4']), (133, 3, ['38']), (151, 1, ['1'])], EN_CITING
def E(p, r): return clean(sif[p - 1][r - 1])
def Hb(p, r): return clean(sif_he[p - 1][r - 1])
assert 'vayishakehu' in E(69, 2) and '(Ibid. 33:4) "And he (Esav) kissed' in E(69, 2) and '(Jeremiah 36:5)' in E(151, 1) and '(Ibid. 33:1) "Then the word of the L-rd came to Jeremiah' in E(151, 1)
HE_CITING = [(p, r) for p, rows in enumerate(sif_he, 1) for r, row in enumerate(rows, 1) if re.search(r'במדבר ל[״"\']?ג\b', clean(row))]
assert HE_CITING == [(133, 3)] and [(p, r) for p, rows in enumerate(sif, 1) for r, row in enumerate(rows, 1) if re.search(r'\(Bamidbar\.? 33:\d+', clean(row))] == []
assert heads[133] == ('Bamidbar', 27, 1) and '(Ibid. 33:38) "And Aaron the Cohein went up to Hor Hahar by the \'mouth\' of the L-rd, and he died there in the fortieth year, etc."' in E(133, 3) and 'only (after) the fortieth year (of the exodus) after Aaron had died' in E(133, 3)
assert '(במדבר ל״ג:ל״ח) ויעל אהרן הכהן אל הר ההר על פי ה\' וימת שם בשנת הארבעים' in Hb(133, 3) and 'שלא עמדו אלא בשנת הארבעים, בשנה שמת בה אהרן' in Hb(133, 3)
# the chapter's own phrases quoted anywhere in the Hebrew rows: "in the fortieth year" (33:38's phrase) at 133:3 alone; "with a high hand" at
# 112:2 is 15:30's own verse (the same three-word phrase at Exodus 14:8, 15:30 and 33:3); "Kibroth-hattaavah" at 86:1, 98:1, 136:2 is 11:34's
# naming (the rows read "named after the event"); 82:1 (on 10:33) reads 21:1's Arad as the news of Aaron's death — 33:38-40's own order, OBSERVED
assert [(p, r) for p, rows in enumerate(sif_he, 1) for r, row in enumerate(rows, 1) if 'בשנת הארבעים' in clean(row)] == [(133, 3)]
assert [(p, r) for p, rows in enumerate(sif_he, 1) for r, row in enumerate(rows, 1) if 'ביד רמה' in clean(row)] == [(112, 2)] and heads[112] == ('Bamidbar', 15, 27) and Hb(112, 2).startswith('והנפש אשר תעשה ביד רמה זה המגלה פנים בתורה')
assert [(p, r) for p, rows in enumerate(sif_he, 1) for r, row in enumerate(rows, 1) if 'קברות התאוה' in clean(row)] == [(86, 1), (98, 1), (136, 2)] and heads[82] == ('Bamidbar', 10, 33) and 'When they heard that Aaron had died' in E(82, 1) and 'כיון שמת אהרן אמרו מת כהן' in Hb(82, 1)
SIF_ROWS = {}
def head(p): return heads[p][1:]
def plain(w): return ''.join(c for c in w if c != '/' and not (0x0591 <= ord(c) <= 0x05C7))
def pointed(w): return ''.join(c for c in w if c != '/' and not (0x0591 <= ord(c) <= 0x05AF))
ONK_LEN = {c: len(onk[c - 1]) for c in (32, 33, 34)}
assert ONK_LEN == {32: 42, 33: 56, 34: 29} and {c: len(onk_he[c - 1]) for c in (32, 33, 34)} == ONK_LEN, ONK_LEN
def onk_ev(c, v): return clean(onk[c - 1][v - 1]), clean(onk_he[c - 1][v - 1])
shelf_numbers = sorted(d for d in os.listdir(f'{ROOT}/Data/sefaria_export') if re.search(r'Numbers|Bamidbar', d))
outside = [d for d in shelf_numbers if d not in ('Sifrei_Bamidbar', 'Onkelos_Numbers')]
assert len(outside) == 23, len(outside)
# THE PRIOR READS: no ledger has read an Onkelos row of 33; SEVEN ledgers NAME verses of the chapter (Genesis's descent ledger 33:1; the tribe
# counts and the Levites 33:15 — Sinai's camp; the trumpets 33:2, 33:8; the offerings-laws ledger 33:3 — the Sifrei's "high hand" beside 15:30;
# the chukat exam 33:40; the Peor ledger 33:4): names, not reads; FRESH. The one cross-citing row's reader: the daughters' ledger (THE TENT 4).
TRI = f'{ROOT}/logic/oral_triage'
LED = {f: open(f'{TRI}/{f}', encoding='utf-8').read() for f in os.listdir(TRI) if f.endswith('.md') and os.path.isfile(f'{TRI}/{f}') and f'{TRI}/{f}' != OUT}
assert sorted(f for f, t in LED.items() if re.search(r'^- Onkelos Num 33:\d', t, re.M)) == []
NAMING = sorted(f for f, t in LED.items() if re.search(r'Num(?:bers)? 33:\d+', t))
assert NAMING == ['gen_28_egypt_descent_2026-08-25.md', 'num_01_tribe_counts_2026-09-09.md', 'num_03_aaron_levi_replace_2026-09-09.md', 'num_10_trumpets_depart_2026-09-10.md', 'num_15_offerings_laws_2026-09-10.md', 'num_19_21_chukat_exam_2026-09-11.md', 'num_25_peor_pinchas_2026-09-11.md'], NAMING
assert re.search(r'^- Sifrei Bamidbar 133:3', LED['num_27_zelophehad_joshua_2026-09-09.md'], re.M) and re.search(r'^- Sifrei Bamidbar 82:1', LED['num_10_trumpets_depart_2026-09-10.md'], re.M)

# ---- THE DRAFT'S SPAN, COMPUTED ----
db = sqlite3.connect(f'file:{ROOT}/Data/tanakh.sqlite?mode=ro', uri=True)
VC = dict(db.execute("SELECT chapter, COUNT(*) FROM verses WHERE book='Num' GROUP BY chapter").fetchall())
assert VC[32] == 42 and VC[33] == 56 and VC[34] == 29
def unit_text(uid): return open(f'{ROOT}/logic/units/{uid}.yaml', encoding='utf-8').read()
def steps(uid): return sorted({(int(a), int(b)) for a, b in re.findall(r'STEP_Nm_(\d+)_(\d+)', unit_text(uid))})
assert steps(UID) == [(33, v) for v in range(1, 57)] and 'status: draft' in unit_text(UID) and 'operators:' not in unit_text(UID)
assert steps('num_34_borders')[0] == (34, 1) and 'status: frozen' in unit_text('num_32_gad_reuben')
SPAN = [(33, v) for v in range(1, 57)]
NV = 56

# ---- THE INK, computed from the Tanakh DB and the snapshot store ----
def accents(w): return [unicodedata.name(c).replace('HEBREW ACCENT ', '') for c in w if 0x0591 <= ord(c) <= 0x05AE]
rows = db.execute("SELECT v.book, v.chapter, v.verse, w.he, w.morph FROM words w JOIN verses v ON w.verse_id=v.id ORDER BY v.id, w.idx").fetchall()
by, byp, byraw = {}, {}, {}
for b, c, v, he, m in rows:
    by.setdefault((b, c, v), []).append((plain(he), m)); byp.setdefault((b, c, v), []).append(pointed(he)); byraw.setdefault((b, c, v), []).append(he)
T = ('Gen', 'Exod', 'Lev', 'Num', 'Deut')
def words(b, c, v): return [x for x, _ in by[(b, c, v)]]
def morphs(b, c, v): return [m for _, m in by[(b, c, v)]]
def hits(sub, books=None, exact=False): return sorted({f'{b} {c}:{v}' for (b, c, v), ws in by.items() if (books is None or b in books) and any((x == sub) if exact else (sub in x) for x, _ in ws)})
def phrase(seq, books=T):
    out = []
    for (b, c, v), ws in by.items():
        if books is not None and b not in books: continue
        w = [x for x, _ in ws]
        if any(w[i:i + len(seq)] == list(seq) for i in range(len(w) - len(seq) + 1)): out.append(f'{b} {c}:{v}')
    return sorted(out)
def U(*toks, books=None): return sorted(set(s for t in toks for s in hits(t, books, True)))
def NP(*toks): return sorted({f'{b} {c}:{v}' for (b, c, v), ws in by.items() for x, m in ws if x in toks and m and 'Np' in m})
def seats_in(pred): return [(v, x) for (c, v) in SPAN for x, m in by[('Num', 33, v)] if pred(x, m)]
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
def arm(c, v): return plain(onk_ev(c, v)[1])
def onk_seats(sub): return [(c + 1, v + 1) for c in range(36) for v in range(len(onk_he[c])) if sub in arm(c + 1, v + 1)]
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
store = sqlite3.connect(f'file:{ROOT}/torah_grok.SNAPSHOT-main-51801ca.sqlite?mode=ro', uri=True)
SG = {}
for c, v, hp, g in store.execute("SELECT v.chapter, v.verse, w.he_plain, w.gloss FROM words w JOIN verses v ON w.verse_id=v.id WHERE v.book='Num' AND v.chapter = 33 ORDER BY v.id, w.idx"):
    SG.setdefault((c, v), []).append((hp.replace('/', ''), g))
def sg(c, v, tok):
    for hp, g in SG[(c, v)]:
        if hp == tok: return g
    raise KeyError((c, v, tok))
assert [(v, n, len(by[('Num', 33, v)])) for v, n in store.execute("SELECT v.verse, COUNT(*) FROM words w JOIN verses v ON w.verse_id=v.id WHERE v.book='Num' AND v.chapter=33 GROUP BY v.verse").fetchall() if n != len(by[('Num', 33, v)])] == []   # no written-and-read pair in the chapter

# THE ENGINE'S PARSER on every verse of the chapter — MEASURED before the compile is asked: FIVE number verses in fifty-six, every one read —
# 33:3 "on the fifteenth day of the first month" [15] with the ordinals [1, 1] (the first month twice); 33:8 "three days" [3]; 33:9 "twelve
# springs of water and seventy palm trees" [12, 70]; 33:38 THE DATE — "in the fortieth year ... in the fifth month, on the first of the month":
# the year and the month as ORDINALS [40, 5] (the article-bearing numeral, rule 20 — the Torah's one seat of that form), the day the number [1];
# 33:39 "a hundred and twenty-three years" [123]; no starred homograph, no marked token; 34:1 empty. NO GAP — the walk's second reading with none.
sys.path.insert(0, f'{ROOT}/World/step9')
with contextlib.redirect_stdout(io.StringIO()):
    import cold_run_sequence as CS
def N(b, c, v): return CS.ink_numbers(CS.verse_words(b, c, v))
def O(b, c, v): return CS.ink_ordinals(CS.verse_words(b, c, v))
PARSED = {v: N('Num', 33, v) for v in range(1, NV + 1) if N('Num', 33, v)}
assert PARSED == {3: [15], 8: [3], 9: [12, 70], 38: [1], 39: [123]}, PARSED
ORD = {v: O('Num', 33, v) for v in range(1, NV + 1) if O('Num', 33, v)}
assert ORD == {3: [1, 1], 38: [40, 5]} and [(v, t) for v in range(1, NV + 1) for t in CS.verse_words('Num', 33, v) if t[-1] in '#~^%@|*'] == [] and N('Num', 34, 1) == [] and O('Num', 34, 1) == []
# THE TAPE'S OWN MARKER: Aaron's death at 20:28 is dated on the tape from THIS chapter's verse — cold_run_sequence.py builds it as
# day_in('exodus', ink_ordinals(33:38)[0], ink_ordinals(33:38)[1], ink_numbers(33:38)[0]) and CM2 checks (40, 5, 1); the reading's measurement
# of 33:38 is the same triple. 20:28 itself carries no number. Deuteronomy 1:3's "in the fortieth year, in the eleventh month, on the first of the
# month" — the Torah's other full date of that year — is written in cardinal forms and reads [40, 11, 1] by the NUMBER reader.
AARON_DATE = (ORD[38][0], ORD[38][1], PARSED[38][0])
assert AARON_DATE == (40, 5, 1) and N('Num', 20, 28) == [] and N('Deut', 1, 3) == [40, 11, 1] and O('Deut', 1, 3) == []   # Deuteronomy 1:3's date in CARDINAL forms ("in forty year", "in eleven month") — the number reader's, where 33:38's year and month are the ordinal reader's
SEQ = open(f'{ROOT}/World/step9/cold_run_sequence.py', encoding='utf-8').read()
assert "M['aaron_death'] = w.clock.day_in('exodus', ink_ordinals(verse_words('Num', 33, 38))[0], ink_ordinals(verse_words('Num', 33, 38))[1], ink_numbers(verse_words('Num', 33, 38))[0])" in SEQ and "(40, 5, 1) Aaron\\'s death = the parser\\'s by day_in" in SEQ
# THE INK'S OWN CHECKSUM: Aaron 83 at the exodus (Exodus 7:7 [80, 83]) + the fortieth year = 123 (33:39); Moses 80 + 40 = 120 (Deuteronomy 34:7);
# the brothers three years apart at both ends. The kin numbers by the same parser: Exodus 15:27's twelve and seventy = 33:9's; Exodus 16:1's
# fifteenth of the second month; 20:29's thirty days; Deuteronomy 1:2's eleven days, 2:14's thirty-eight years; 14:33's forty
assert N('Exod', 7, 7) == [80, 83] and PARSED[39] == [83 + 40] and N('Deut', 34, 7) == [120] == [80 + 40] and 123 - 120 == 83 - 80 == 3
assert N('Exod', 15, 27) == [12, 70] == PARSED[9] and N('Exod', 16, 1) == [15] and O('Exod', 16, 1) == [2] and N('Num', 20, 29) == [30] and N('Deut', 1, 2) == [11] and N('Deut', 2, 14) == [38] and N('Num', 14, 33) == [40] and N('Exod', 12, 37) == [600000]

# THE FRAMES AND THE REGISTER: NINETY-THREE narrative verbs in forty-seven verses (computed on the morphology) — eighty-four of them the pair
# "and they journeyed" / "and they camped" (FORTY-TWO each), the other nine: Moses WROTE (33:2), the camp TURNED BACK (33:7, singular — Exodus
# 14:2's jussive "let them turn back" fulfilled), they PASSED and WENT (33:8), they CAME (33:9), Aaron WENT UP and DIED (33:38), the Canaanite
# HEARD (33:40), the LORD SPOKE (33:50); ONE divine frame (33:50) and ONE speech (33:51-56) — the chapters of Numbers without a frame unchanged
# (22-24, 29, 30, 32, 36). "And they journeyed" stands in forty-two verses (33:3 and 33:5-48), "and they camped" in forty-two (33:5-49); forty-one
# verses carry both, 33:3 the journey alone (the date line), 33:49 the camp alone (the last camp's extent).
REG = [(v, x, m) for (c, v) in SPAN for x, m in by[('Num', 33, v)] if m and re.search(r'V.w', m)]
assert len(REG) == 93 and len({v for v, _, _ in REG}) == 47 and [(v, x) for v, x, _ in REG if x not in ('ויסעו', 'ויחנו')] == [(2, 'ויכתב'), (7, 'וישב'), (8, 'ויעברו'), (8, 'וילכו'), (9, 'ויבאו'), (38, 'ויעל'), (38, 'וימת'), (40, 'וישמע'), (50, 'וידבר')]
JV = [v for (c, v) in SPAN if 'ויסעו' in words('Num', 33, v)]; CVv = [v for (c, v) in SPAN if 'ויחנו' in words('Num', 33, v)]
assert len(JV) == 42 and JV == [3] + list(range(5, 38)) + list(range(41, 49)) and len(CVv) == 42 and CVv == list(range(5, 38)) + list(range(41, 50)) and len(set(JV) & set(CVv)) == 41 and sorted(set(JV) - set(CVv)) == [3] and sorted(set(CVv) - set(JV)) == [49]
assert sum(1 for (c, v) in SPAN for x, _ in by[('Num', 33, v)] if x == 'ויסעו') == 42 and sum(1 for (c, v) in SPAN for x, _ in by[('Num', 33, v)] if x == 'ויחנו') == 42
DIV = {}
for (b, c, v), ws in by.items():
    if b != 'Num': continue
    w = [x for x, _ in ws]
    if any(w[i] in ('ויאמר', 'וידבר') and w[i + 1] == 'יהוה' for i in range(len(w) - 1)): DIV.setdefault(c, []).append(v)
assert DIV[33] == [50] and [c for c in range(1, 37) if c not in DIV] == [22, 23, 24, 29, 30, 32, 36]
assert [(x, m) for x, m in by[('Num', 33, 7)] if x == 'וישב'] == [('וישב', 'HC/Vqw3ms')] and [(x, m) for x, m in by[('Exod', 14, 2)] if x == 'וישבו'] == [('וישבו', 'HC/Vqj3mp')]
assert len(U('ויסעו')) == 64 and len([s for s in U('ויסעו') if s.startswith('Num')]) == 51 and len(U('ויחנו')) == 79 and len([s for s in U('ויחנו') if s.startswith('Num')]) == 48
# ONKELOS keeps the pair's counts — "and they journeyed" (ונטלו) forty-two, "and they camped" (ושרו) forty-two
assert sum(1 for v in range(1, 57) if arm(33, v).startswith('ונטלו')) == 42 and sum(arm(33, v).count('ושרו') for v in range(1, 57)) == 42

# THE FORTY-TWO (computed): forty-two "journeyed" tokens and forty-two "camped" tokens; the departure from Rameses is told TWICE (33:3 with its
# date, 33:5 as the itinerary's own first line) and the camp in the plains of Moab TWICE (33:48 the arrival, 33:49 its extent "from Beth-jeshimoth
# to Abel-shittim") — so the places named are FORTY-TWO: Rameses and forty-one camps (33:5-37 thirty-three, 33:41-48 eight); the departures'
# after-tokens are forty distinct (the wilderness of Sin and of Sinai and of Zin share "from the wilderness", Shepher and Hor "from the mount")
CAMPS = [(v, words('Num', 33, v)[words('Num', 33, v).index('ויחנו') + 1]) for (c, v) in SPAN if 'ויחנו' in words('Num', 33, v)]
DEPS = [(v, words('Num', 33, v)[words('Num', 33, v).index('ויסעו') + 1]) for (c, v) in SPAN if 'ויסעו' in words('Num', 33, v)]
assert len(CAMPS) == 42 and len(DEPS) == 42 and len({x for _, x in DEPS}) == 40 and DEPS[0] == (3, 'מרעמסס') and DEPS[1] == (5, 'בני') and words('Num', 33, 5)[:4] == ['ויסעו', 'בני', 'ישראל', 'מרעמסס']
assert CAMPS[-2] == (48, 'בערבת') and CAMPS[-1] == (49, 'על') and words('Num', 33, 49)[-2:] == ['בערבת', 'מואב'] and words('Num', 33, 48)[4:6] == ['בערבת', 'מואב']
PLACES = 1 + len([c for c in CAMPS if c[0] != 49])
assert PLACES == 42 and len([c for c in CAMPS if 5 <= c[0] <= 37]) == 33 and len([c for c in CAMPS if 41 <= c[0] <= 48]) == 8
assert [i for i, (v, x) in enumerate(CAMPS) if x == 'במסרות'] == [25] and [i for i, (v, x) in enumerate(CAMPS) if v == 37] == [32] and 32 - 25 == 7   # Moseroth to Mount Hor: seven camps on
NAMES = [x for (c, v) in SPAN for x, m in by[('Num', 33, v)] if m and 'Np' in m]
assert len(NAMES) == 144 and len(set(NAMES)) == 108

# THE HEADING AND THE FRAME (33:1-2): "THESE ARE THE JOURNEYS of the children of Israel" — two seats, 10:28 (closing the march order: "these are
# the journeys of the children of Israel by their hosts, and they journeyed") and 33:1 — the same first four words, "by their hosts" at both; the
# verse-initial "these" heading sixty-three times in the Torah (Deuteronomy 1:1's "these are the words" among them); "by their hosts" sixteen seats, every one in Numbers (chapters 1, 2, 10, 33 — Exodus
# 12:51 and 6:26 say "according to their hosts" with another preposition); "BY THE HAND OF MOSES AND AARON" — 33:1 and Psalm 77:21 ("you led
# your people like a flock by the hand of Moses and Aaron"), the phrase's two Bible seats; "by the hand of Moses" sixteen Torah seats. "AND MOSES
# WROTE" four Torah seats — the words of the covenant (Exodus 24:4), THE JOURNEYS (33:2), this Torah (Deuteronomy 31:9), this song (31:22): the
# four things the Torah says Moses wrote; the verb's six Torah seats (the tablets at Exodus 34:28 and Deuteronomy 10:4 the other two). 33:2's
# CHIASM: "their goings-out by their journeys ... their journeys by their goings-out" — "goings-out" two Bible seats (Jeremiah 50:7 the other),
# "their journeys" six (the cloud's stages: Exodus 17:1, 40:36, 40:38; 10:6, 10:12; 33:2); "BY THE MOUTH OF THE LORD" twenty-one Bible seats,
# eighteen Torah, fifteen in Numbers — Moses WROTE by it (33:2) and Aaron WENT UP by it (33:38); 33:7's "mouth" is Pi-hahiroth's, the homograph.
# ONKELOS: "by the WORD (memra) of the LORD" at both (33:2, 33:38 — the buffer's two seats in the chapter).
assert phrase(['אלה', 'מסעי']) == ['Num 10:28', 'Num 33:1'] and words('Num', 10, 28)[:4] == words('Num', 33, 1)[:4] == ['אלה', 'מסעי', 'בני', 'ישראל'] and 'לצבאתם' in words('Num', 10, 28) and words('Num', 33, 1)[8] == 'לצבאתם'
HEADS = sorted({f'{b} {c}:{v}' for (b, c, v), ws in by.items() if b in T for w in [[x for x, _ in ws]] if w[0] == 'אלה' and len(w) > 1})
assert len(HEADS) == 63 and 'Deut 1:1' in HEADS and 'Num 33:1' in HEADS and 'Num 10:28' in HEADS and 'Gen 2:4' in HEADS and 'Num 36:13' in HEADS
assert len(U('לצבאתם')) == 16 and all(s.startswith('Num') for s in U('לצבאתם')) and words('Exod', 12, 51)[-2:] == ['על', 'צבאתם'] and words('Exod', 6, 26)[-2:] == ['על', 'צבאתם']
assert phrase(['ביד', 'משה', 'ואהרן'], None) == ['Num 33:1', 'Ps 77:21'] and words('Ps', 77, 21) == ['נחית', 'כצאן', 'עמך', 'ביד', 'משה', 'ואהרן'] and len(phrase(['ביד', 'משה'])) == 16
assert phrase(['ויכתב', 'משה']) == ['Deut 31:22', 'Deut 31:9', 'Exod 24:4', 'Num 33:2'] and U('ויכתב', books=T) == ['Deut 10:4', 'Deut 31:22', 'Deut 31:9', 'Exod 24:4', 'Exod 34:28', 'Num 33:2'] and words('Exod', 24, 4)[:6] == ['ויכתב', 'משה', 'את', 'כל', 'דברי', 'יהוה'] and words('Deut', 31, 9)[:5] == ['ויכתב', 'משה', 'את', 'התורה', 'הזאת'] and words('Deut', 31, 22)[:5] == ['ויכתב', 'משה', 'את', 'השירה', 'הזאת']
assert words('Num', 33, 2) == ['ויכתב', 'משה', 'את', 'מוצאיהם', 'למסעיהם', 'על', 'פי', 'יהוה', 'ואלה', 'מסעיהם', 'למוצאיהם'] and U('מוצאיהם', 'למוצאיהם') == ['Jer 50:7', 'Num 33:2'] and U('מסעיהם', 'למסעיהם') == ['Exod 17:1', 'Exod 40:36', 'Exod 40:38', 'Num 10:12', 'Num 10:6', 'Num 33:2']
PI = phrase(['על', 'פי', 'יהוה'], None)
assert len(PI) == 21 and len([s for s in PI if s.startswith('Num')]) == 15 and len(phrase(['על', 'פי', 'יהוה'])) == 18 and 'Num 33:2' in PI and 'Num 33:38' in PI and seats_in(lambda x, m: x == 'פי') == [(2, 'פי'), (7, 'פי'), (38, 'פי')] and words('Num', 33, 7)[4:6] == ['פי', 'החירת']
assert [(v, arm(33, v).count('מימרא')) for v in range(1, 57) if 'מימרא' in arm(33, v)] == [(2, 1), (38, 1)] and aramaic(33, 2)[5:8] == ['על', 'מימרא', 'דיי'] and aramaic(33, 38)[5:8] == ['על', 'מימרא', 'דיי'] and aramaic(33, 1)[-3:] == ['בידא', 'דמשה', 'ואהרן'] and aramaic(33, 1)[8] == 'לחיליהון'

# THE DATE LINE (33:3-4): "they journeyed from Rameses in the first month, ON THE FIFTEENTH DAY OF THE FIRST MONTH, ON THE MORROW OF THE PASSOVER"
# — the full date phrase one seat; "on the fifteenth day of the month" six Bible seats (Exodus 16:1 the second month's, Leviticus 23:34, 39 the
# seventh's, Jeroboam's eighth 1 Kings 12:32, Ezekiel 45:25); Leviticus 23:6 and 28:17 date the feast of unleavened bread "on the fifteenth day
# of THIS month" — the departure's date is the feast's; Exodus 12 gives the fourteenth at evening (12:6, 18) and "that selfsame day" (12:41,
# 51), and this verse alone writes the fifteenth of the departure outright. "THE MORROW OF THE PASSOVER" — two Bible seats: 33:3 (out of Egypt)
# and Joshua 5:11 (the first eating of the land's produce, the manna ceasing on the morrow, 5:12) — the run's two ends on one date-word;
# "the morrow" eleven Torah seats (the omer's morrow Leviticus 23:11, 15, 16 among them). "WITH A HIGH HAND" three Torah seats — Exodus 14:8 (the
# same going out, "the children of Israel going out with a high hand"), 15:30 (the soul that acts with a high hand — the blasphemer's rule;
# the Sifrei 112:2's verse), 33:3; ONKELOS renders both Numbers seats "with BARED head" (in the open) — 15:30's and 33:3's, the buffer's two seats
# in Onkelos Numbers, and the Sifrei's own gloss on 15:30 is "one who BARES his face against the Torah" (the same root, computed on the
# Hebrew row). "in the sight of all Egypt" one seat. Rameses five Bible seats (Genesis 47:11 the land, Exodus 1:11 the store-city, 12:37, 33:3, 5).
assert words('Num', 33, 3) == ['ויסעו', 'מרעמסס', 'בחדש', 'הראשון', 'בחמשה', 'עשר', 'יום', 'לחדש', 'הראשון', 'ממחרת', 'הפסח', 'יצאו', 'בני', 'ישראל', 'ביד', 'רמה', 'לעיני', 'כל', 'מצרים']
assert phrase(['בחמשה', 'עשר', 'יום', 'לחדש', 'הראשון'], None) == ['Num 33:3'] and phrase(['בחמשה', 'עשר', 'יום', 'לחדש'], None) == ['1Kgs 12:32', 'Exod 16:1', 'Ezek 45:25', 'Lev 23:34', 'Lev 23:39', 'Num 33:3'] and words('Lev', 23, 6)[:7] == ['ובחמשה', 'עשר', 'יום', 'לחדש', 'הזה', 'חג', 'המצות'] and words('Num', 28, 17)[:6] == ['ובחמשה', 'עשר', 'יום', 'לחדש', 'הזה', 'חג']
assert words('Exod', 12, 18)[:6] == ['בראשן', 'בארבעה', 'עשר', 'יום', 'לחדש', 'בערב'] and words('Exod', 12, 41)[7:11] == ['ויהי', 'בעצם', 'היום', 'הזה'] and words('Exod', 12, 51)[:4] == ['ויהי', 'בעצם', 'היום', 'הזה']
assert phrase(['ממחרת', 'הפסח'], None) == ['Josh 5:11', 'Num 33:3'] and words('Josh', 5, 11) == ['ויאכלו', 'מעבור', 'הארץ', 'ממחרת', 'הפסח', 'מצות', 'וקלוי', 'בעצם', 'היום', 'הזה'] and words('Josh', 5, 12)[:2] == ['וישבת', 'המן'] and len(U('ממחרת', books=T)) == 11 and words('Lev', 23, 15)[:4] == ['וספרתם', 'לכם', 'ממחרת', 'השבת']
assert phrase(['ביד', 'רמה'], None) == ['Exod 14:8', 'Num 15:30', 'Num 33:3'] and words('Exod', 14, 8)[-4:] == ['ישראל', 'יצאים', 'ביד', 'רמה'] and words('Num', 15, 30)[:5] == ['והנפש', 'אשר', 'תעשה', 'ביד', 'רמה']
assert onk_seats('בריש גלי') == [(15, 30), (33, 3)] and aramaic(33, 3)[15:17] == ['בריש', 'גלי'] and Hb(112, 2).startswith('והנפש אשר תעשה ביד רמה זה המגלה פנים בתורה')
assert phrase(['לעיני', 'כל', 'מצרים'], None) == ['Num 33:3'] and U('רעמסס', 'מרעמסס') == ['Exod 12:37', 'Exod 1:11', 'Gen 47:11', 'Num 33:3', 'Num 33:5']
# 33:4: "AND EGYPT WAS BURYING those whom the LORD had smitten among them, every firstborn" — the participle "burying" two Bible seats (Ezekiel
# 39:14's buriers of Gog the other); "AND ON THEIR GODS THE LORD EXECUTED JUDGMENTS" one seat — THE RUN OF EXODUS 12:12's "on all the gods of
# Egypt I will execute judgments" (the future "I will execute judgments" at Exodus 12:12 and Ezekiel 25:11 alone; the perfect nowhere else):
# Exodus narrates the firstborn smitten (12:29) and never the judgments on the gods — the itinerary alone records that run, forty years on.
# ONKELOS: "on their IDOLS" (their errors — the word at 25:2 for Peor's gods and here).
assert words('Num', 33, 4) == ['ומצרים', 'מקברים', 'את', 'אשר', 'הכה', 'יהוה', 'בהם', 'כל', 'בכור', 'ובאלהיהם', 'עשה', 'יהוה', 'שפטים'] and U('מקברים') == ['Ezek 39:14', 'Num 33:4'] and [(x, m) for x, m in by[('Num', 33, 4)] if x == 'מקברים'] == [('מקברים', 'HVprmpa')]
assert phrase(['ובאלהיהם', 'עשה', 'יהוה', 'שפטים'], None) == ['Num 33:4'] and phrase(['אעשה', 'שפטים'], None) == ['Exod 12:12', 'Ezek 25:11'] and phrase(['עשה', 'שפטים'], None) == [] and words('Exod', 12, 12)[-7:] == ['ובכל', 'אלהי', 'מצרים', 'אעשה', 'שפטים', 'אני', 'יהוה']
assert len(U('שפטים', 'ושפטים', 'בשפטים')) == 25 and words('Exod', 12, 29)[:8] == ['ויהי', 'בחצי', 'הלילה', 'ויהוה', 'הכה', 'כל', 'בכור', 'בארץ'] and onk_seats('טעות') == [(25, 2), (33, 4)] and aramaic(33, 4)[9] == 'ובטעותהון'

# THE STATIONS AGAINST THEIR FIRST TELLINGS (computed): 33:5 opens as Exodus 12:37 opens ("and the children of Israel journeyed from Rameses" —
# the four words), Exodus adding "to Succoth" with the directional ending and the six hundred thousand, the itinerary "and camped in Succoth";
# 33:6 IS EXODUS 13:20 with one word added — "in Etham WHICH IS in the edge of the wilderness" (six of seven tokens shared, the relative
# pronoun the seventh); 33:7 "and TURNED BACK to Pi-hahiroth" — Exodus 14:2's command "let them turn back" (the jussive) fulfilled in the
# itinerary's narrative form; Pi-hahiroth three seats (Exodus 14:2, 9; 33:7 — 33:8 "from before Hahiroth" without "Pi"), "Baal-zephon" spelled
# plene here alone (Exodus's two seats defective), Migdol's two Torah seats; 33:8 "PASSED THROUGH THE MIDST OF THE SEA into the wilderness" —
# Nehemiah 9:11 the phrase's one other seat; "a way of three days in the wilderness of ETHAM" — Exodus 15:22 walks the same three days in the
# wilderness of SHUR: the two names one seat each, the itinerary's own name for Exodus's Shur; "a way of three days" six Torah seats — Moses'
# request of Pharaoh (Exodus 3:18, 5:3, 8:23) walked after the sea; 33:9 ELIM's twelve springs and seventy palms word for word with Exodus 15:27
# (each phrase's two seats); 33:10 THE CAMP BY THE RED SEA — a station Exodus never names (the phrase one seat; the sea's seven Torah seats);
# 33:11 the wilderness of Sin (Exodus 16:1 "between Elim and Sinai, on the fifteenth day of the second month"); 33:12-13 DOPHKAH AND ALUSH —
# two stations named nowhere else; 33:14 Rephidim "and there was no water for the people to drink" — Exodus 17:1's clause in another word
# order (each order one seat); Rephidim's five seats, the itinerary's spelling defective with Exodus 17:8's, 17:1 and 19:2 plene; 33:15 "and
# camped in the wilderness of Sinai" one seat — Exodus 19:2 says "and camped in the wilderness, and Israel camped there" with the singular verb.
assert words('Num', 33, 5) == ['ויסעו', 'בני', 'ישראל', 'מרעמסס', 'ויחנו', 'בסכת'] and words('Exod', 12, 37)[:5] == ['ויסעו', 'בני', 'ישראל', 'מרעמסס', 'סכתה']
assert words('Num', 33, 6) == words('Exod', 13, 20)[:4] + ['אשר'] + words('Exod', 13, 20)[4:] and words('Exod', 13, 20) == ['ויסעו', 'מסכת', 'ויחנו', 'באתם', 'בקצה', 'המדבר']
assert words('Num', 33, 7) == ['ויסעו', 'מאתם', 'וישב', 'על', 'פי', 'החירת', 'אשר', 'על', 'פני', 'בעל', 'צפון', 'ויחנו', 'לפני', 'מגדל'] and words('Exod', 14, 2)[4:10] == ['וישבו', 'ויחנו', 'לפני', 'פי', 'החירת', 'בין']
assert phrase(['פי', 'החירת'], None) == ['Exod 14:2', 'Exod 14:9', 'Num 33:7'] and U('החירת') == ['Exod 14:2', 'Exod 14:9', 'Num 33:7', 'Num 33:8'] and phrase(['בעל', 'צפון'], None) == ['Num 33:7'] and phrase(['בעל', 'צפן'], None) == ['Exod 14:2', 'Exod 14:9'] and U('מגדל', books=T) == ['Exod 14:2', 'Num 33:7']
assert words('Num', 33, 8) == ['ויסעו', 'מפני', 'החירת', 'ויעברו', 'בתוך', 'הים', 'המדברה', 'וילכו', 'דרך', 'שלשת', 'ימים', 'במדבר', 'אתם', 'ויחנו', 'במרה'] and phrase(['ויעברו', 'בתוך', 'הים'], None) == ['Neh 9:11', 'Num 33:8']
assert phrase(['שלשת', 'ימים', 'במדבר'], None) == ['Exod 15:22', 'Exod 3:18', 'Exod 5:3', 'Num 33:8'] and phrase(['דרך', 'שלשת', 'ימים']) == ['Exod 3:18', 'Exod 5:3', 'Exod 8:23', 'Gen 30:36', 'Num 10:33', 'Num 33:8'] and phrase(['מדבר', 'שור'], None) == ['Exod 15:22'] and phrase(['במדבר', 'אתם'], None) == ['Num 33:8'] and words('Exod', 15, 22)[6:14] == ['ויצאו', 'אל', 'מדבר', 'שור', 'וילכו', 'שלשת', 'ימים', 'במדבר']
assert words('Num', 33, 9) == ['ויסעו', 'ממרה', 'ויבאו', 'אילמה', 'ובאילם', 'שתים', 'עשרה', 'עינת', 'מים', 'ושבעים', 'תמרים', 'ויחנו', 'שם'] and phrase(['שתים', 'עשרה', 'עינת', 'מים'], None) == ['Exod 15:27', 'Num 33:9'] and phrase(['ושבעים', 'תמרים'], None) == ['Exod 15:27', 'Num 33:9'] and words('Exod', 15, 27)[:2] == ['ויבאו', 'אילמה']
assert phrase(['ויחנו', 'על', 'ים', 'סוף'], None) == ['Num 33:10'] and phrase(['ים', 'סוף']) == ['Deut 11:4', 'Deut 1:40', 'Deut 2:1', 'Exod 13:18', 'Num 14:25', 'Num 21:4', 'Num 33:10'] and phrase(['ויחנו', 'על'], None) == ['1Sam 4:1', 'Josh 10:5', 'Judg 20:19', 'Judg 7:1', 'Num 33:10', 'Num 33:49']
assert phrase(['מדבר', 'סין'], None) == ['Exod 16:1'] and NP('סין') == ['Exod 16:1', 'Exod 17:1', 'Ezek 30:15', 'Ezek 30:16', 'Num 33:11', 'Num 33:12'] and words('Exod', 16, 1)[8:15] == ['מדבר', 'סין', 'אשר', 'בין', 'אילם', 'ובין', 'סיני']
assert U('דפקה', 'בדפקה', 'מדפקה') == ['Num 33:12', 'Num 33:13'] and U('אלוש', 'באלוש', 'מאלוש') == ['Num 33:13', 'Num 33:14']
assert words('Num', 33, 14) == ['ויסעו', 'מאלוש', 'ויחנו', 'ברפידם', 'ולא', 'היה', 'שם', 'מים', 'לעם', 'לשתות'] and phrase(['ואין', 'מים', 'לשתת', 'העם'], None) == ['Exod 17:1'] and phrase(['מים', 'לעם', 'לשתות'], None) == ['Num 33:14'] and words('Exod', 17, 1)[-4:] == ['ואין', 'מים', 'לשתת', 'העם']
assert NP('רפידם', 'ברפידם', 'מרפידם', 'ברפידים', 'מרפידים') == ['Exod 17:1', 'Exod 17:8', 'Exod 19:2', 'Num 33:14', 'Num 33:15'] and U('רפידם', 'ברפידם', 'מרפידם') == ['Exod 17:8', 'Num 33:14', 'Num 33:15'] and words('Exod', 17, 1)[12] == 'ברפידים' and words('Exod', 19, 2)[1] == 'מרפידים'
assert phrase(['ויחנו', 'במדבר', 'סיני'], None) == ['Num 33:15'] and [(x, m) for x, m in by[('Exod', 19, 2)]][5:8] == [('ויחנו', 'HC/Vqw3mp'), ('במדבר', 'HRd/Ncmsa'), ('ויחן', 'HC/Vqw3ms')] and len(phrase(['מדבר', 'סיני'], None)) == 2
# 33:16-18: Kibroth-hattaavah and Hazeroth are 11:34-35's ("from Kibroth-hattaavah the people journeyed to Hazeroth"); 12:16 has the people
# journey from Hazeroth "and camp in the wilderness of PARAN" — the itinerary says RITHMAH (two seats, here alone): the ink's two names for the
# spies' base (13:3 "from the wilderness of Paran", 13:26 "to the wilderness of Paran, to Kadesh"); Taberah (11:3; Deuteronomy 9:22 with Massah
# and Kibroth-hattaavah) is NO station of the list. ONKELOS renders Kibroth-hattaavah "the graves of those who DEMANDED" at all four seats (11:34,
# 35; 33:16, 17) — the name translated, as at chapter 11.
assert words('Num', 11, 35) == ['מקברות', 'התאוה', 'נסעו', 'העם', 'חצרות', 'ויהיו', 'בחצרות'] and words('Num', 12, 16) == ['ואחר', 'נסעו', 'העם', 'מחצרות', 'ויחנו', 'במדבר', 'פארן'] and words('Num', 33, 18) == ['ויסעו', 'מחצרת', 'ויחנו', 'ברתמה']
assert phrase(['קברות', 'התאוה'], None) == ['Num 11:34'] and phrase(['בקברת', 'התאוה'], None) == ['Num 33:16'] and phrase(['מקברת', 'התאוה'], None) == ['Num 33:17'] and words('Deut', 9, 22)[:4] == ['ובתבערה', 'ובמסה', 'ובקברת', 'התאוה']
assert NP('חצרת', 'בחצרת', 'מחצרת', 'חצרות', 'בחצרות', 'מחצרות') == ['Num 11:35', 'Num 12:16', 'Num 33:17', 'Num 33:18'] and U('רתמה', 'ברתמה', 'מרתמה') == ['Num 33:18', 'Num 33:19'] and U('תבערה', 'ובתבערה') == ['Deut 9:22', 'Num 11:3'] and phrase(['מדבר', 'פארן'], None) == ['1Sam 25:1', 'Num 13:26'] and phrase(['במדבר', 'פארן'], None) == ['Gen 21:21', 'Num 10:12', 'Num 12:16']
assert onk_seats('דמשאלי') == [(11, 34), (11, 35), (33, 16), (33, 17)] and aramaic(33, 16)[-2:] == ['בקברי', 'דמשאלי']
# 33:19-35 SEVENTEEN STATIONS between Rithmah and Kadesh: ELEVEN are named NOWHERE ELSE in the Bible (each at its two verses alone — Dophkah and
# Alush before them, Rithmah, Rissah, Kehelathah, Makheloth, Mithkah, Hashmonah, Abronah here, Zalmonah and Punon after Mount Hor: the eleven of
# the whole list); THREE MORE are names only here whose consonants are common words elsewhere — Mount SHEPHER (the ram's horn of Exodus 19:16),
# HARADAH ("trembling"), TAHATH ("under" — the preposition's letters, a place by the morphology at its two seats); RIMMON-PEREZ shares its first
# word with Naaman's "house of Rimmon" (2 Kings 5:18), TERAH carries Abraham's father's name (Genesis 11's eight seats, Joshua 24:2, 1 Chronicles
# 1:26), LIBNAH a Judah city's (Joshua 10:29 and seventeen more); MOSEROTH, BENE-JAAKAN, HOR-HAGGIDGAD and JOTBATHAH are DEUTERONOMY 10:6-7's four
# (Moserah; Beeroth-bene-jaakan; Gudgodah; Jotbathah "a land of brooks of water"); EZION-GEBER Deuteronomy 2:8's and Solomon's and Jehoshaphat's
# port (1 Kings 9:26, 22:49; 2 Chronicles 20:36).
assert U('רסה', 'ברסה', 'מרסה') == ['Num 33:21', 'Num 33:22'] and U('קהלתה', 'בקהלתה', 'מקהלתה') == ['Num 33:22', 'Num 33:23'] and U('מקהלת', 'במקהלת', 'ממקהלת') == ['Num 33:25', 'Num 33:26'] and U('מתקה', 'במתקה', 'ממתקה') == ['Num 33:28', 'Num 33:29'] and U('חשמנה', 'בחשמנה', 'מחשמנה') == ['Num 33:29', 'Num 33:30'] and U('עברנה', 'בעברנה', 'מעברנה') == ['Num 33:34', 'Num 33:35'] and U('צלמנה', 'בצלמנה', 'מצלמנה') == ['Num 33:41', 'Num 33:42'] and U('פונן', 'בפונן', 'מפונן') == ['Num 33:42', 'Num 33:43']
HAPAX = ['דפקה', 'אלוש', 'רתמה', 'רסה', 'קהלתה', 'מקהלת', 'מתקה', 'חשמנה', 'עברנה', 'צלמנה', 'פונן']
assert len(HAPAX) == 11 and all(all(s.startswith('Num 33:') for s in U(n, 'ב' + n, 'מ' + n)) and len(U(n, 'ב' + n, 'מ' + n)) == 2 for n in HAPAX)
assert NP('שפר', 'בשפר') == ['Num 33:23', 'Num 33:24'] and 'Exod 19:16' in U('שפר') and NP('חרדה', 'בחרדה', 'מחרדה') == ['Num 33:24', 'Num 33:25'] and 'Gen 27:33' in U('חרדה') and NP('תחת', 'בתחת', 'מתחת') == ['Num 33:26', 'Num 33:27']
assert NP('רמן', 'ברמן', 'מרמן') == ['2Kgs 5:18', 'Num 33:19', 'Num 33:20'] and NP('תרח', 'בתרח', 'מתרח') == ['1Chr 1:26', 'Gen 11:24', 'Gen 11:25', 'Gen 11:26', 'Gen 11:27', 'Gen 11:28', 'Gen 11:31', 'Gen 11:32', 'Josh 24:2', 'Num 33:27', 'Num 33:28'] and len(NP('לבנה', 'בלבנה', 'מלבנה', 'ולבנה', 'ללבנה')) == 19 and 'Josh 10:29' in NP('לבנה') and 'Num 33:20' in NP('בלבנה')
assert U('מוסרה', 'מוסרות', 'מסרות', 'ממסרות', 'במסרות') == ['Deut 10:6', 'Jer 27:2', 'Jer 5:5', 'Num 33:30', 'Num 33:31'] and U('יעקן') == ['1Chr 1:42', 'Deut 10:6', 'Num 33:31', 'Num 33:32'] and U('הגדגדה', 'הגדגד') == ['Deut 10:7', 'Num 33:32', 'Num 33:33'] and U('יטבתה', 'ביטבתה', 'מיטבתה') == ['Deut 10:7', 'Num 33:33', 'Num 33:34']
assert words('Deut', 10, 6) == ['ובני', 'ישראל', 'נסעו', 'מבארת', 'בני', 'יעקן', 'מוסרה', 'שם', 'מת', 'אהרן', 'ויקבר', 'שם', 'ויכהן', 'אלעזר', 'בנו', 'תחתיו'] and words('Deut', 10, 7) == ['משם', 'נסעו', 'הגדגדה', 'ומן', 'הגדגדה', 'יטבתה', 'ארץ', 'נחלי', 'מים']
assert words('Num', 33, 30)[-1] == 'במסרות' and words('Num', 33, 31) == ['ויסעו', 'ממסרות', 'ויחנו', 'בבני', 'יעקן'] and words('Num', 33, 32)[-2:] == ['בחר', 'הגדגד'] and words('Num', 33, 33)[-1] == 'ביטבתה'
assert NP('בעציון', 'מעציון', 'עציון') == ['1Kgs 22:49', '1Kgs 9:26', '2Chr 20:36', 'Num 33:35', 'Num 33:36'] and words('Deut', 2, 8)[9:12] == ['מאילת', 'ומעצין', 'גבר'] and words('1Kgs', 9, 26)[:6] == ['ואני', 'עשה', 'המלך', 'שלמה', 'בעציון', 'גבר']
# 33:36-37: "the wilderness of Zin, THAT IS KADESH" — the identity clause "that is Kadesh" five Bible seats (Genesis 14:7's "En-mishpat, that is
# Kadesh" the same idiom); the wilderness of Zin's seats (13:21, 20:1, 27:14, 34:3; Deuteronomy 32:51; Joshua 15:1); "Mount Hor IN THE EDGE of
# the land of Edom" one seat — 20:23 "ON THE BORDER of the land of Edom" one seat; Mount Hor twelve Torah seats. ONKELOS: REKEM for Kadesh at ten
# seats of Onkelos Numbers (13:26, 20:1, 14, 16, 22, 27:14, 32:8's "Rekem Geah" for Kadesh-barnea, 33:36, 37, 34:4) — and the Hebrew's own
# Rekem, the Midianite king of 31:8, the eleventh; "HOR THE MOUNTAIN" at 33:37-41 and 34:8.
assert words('Num', 33, 36) == ['ויסעו', 'מעציון', 'גבר', 'ויחנו', 'במדבר', 'צן', 'הוא', 'קדש'] and phrase(['הוא', 'קדש'], None) == ['Exod 30:32', 'Gen 14:7', 'Lev 25:12', 'Lev 27:30', 'Num 33:36'] and words('Gen', 14, 7)[4:7] == ['משפט', 'הוא', 'קדש']
assert sorted(phrase(['מדבר', 'צן'], None) + phrase(['במדבר', 'צן'], None) + phrase(['ממדבר', 'צן'], None)) == ['Deut 32:51', 'Josh 15:1', 'Num 13:21', 'Num 20:1', 'Num 27:14', 'Num 27:14', 'Num 33:36', 'Num 34:3']
assert words('Num', 33, 37) == ['ויסעו', 'מקדש', 'ויחנו', 'בהר', 'ההר', 'בקצה', 'ארץ', 'אדום'] and phrase(['בקצה', 'ארץ', 'אדום'], None) == ['Num 33:37'] and phrase(['על', 'גבול', 'ארץ', 'אדום'], None) == ['Num 20:23']
HOR = sorted(phrase(['הר', 'ההר'], None) + phrase(['בהר', 'ההר'], None) + phrase(['מהר', 'ההר'], None))
assert HOR == ['Deut 32:50', 'Num 20:22', 'Num 20:23', 'Num 20:25', 'Num 20:27', 'Num 21:4', 'Num 33:37', 'Num 33:38', 'Num 33:39', 'Num 33:41', 'Num 34:7', 'Num 34:8'] and len(HOR) == 12
assert onk_seats('רקם') == [(13, 26), (20, 1), (20, 14), (20, 16), (20, 22), (27, 14), (31, 8), (32, 8), (33, 36), (33, 37), (34, 4)] and words('Num', 31, 8)[9] == 'רקם' and aramaic(33, 36)[-2:] == ['היא', 'רקם'] and aramaic(33, 37)[1] == 'מרקם' and onk_seats('הור טורא') == [(33, 37), (33, 38), (33, 39), (33, 41), (34, 8)]

# AARON'S DEATH (33:38-39): the itinerary alone DATES it — 20:28 has no number; "in the fortieth year of the going out of the children of Israel
# from the land of Egypt, in the fifth month, on the first of the month" — THE TORAH'S ONE FULL DEATH-DATE; "in the fortieth year" (the article
# form) two Bible seats — 33:38 and 1 Chronicles 26:31 (David's fortieth); "OF THE GOING OUT of the children of Israel from the land of Egypt"
# three Bible seats — Exodus 19:1 (the third month, Sinai), 33:38 (the fortieth year, Mount Hor), 1 Kings 6:1 (the four hundred and eightieth
# year, the temple's founding): THE ERA'S THREE STAMPS in that form; "in the fifth month" the Torah's one seat (Jeremiah 1:3, 28:1, Ezra 7:8
# the others); "on the first of the month" ten Torah seats; "at his death" two Bible seats — Aaron's (33:39) and Moses' (Deuteronomy 34:7),
# the brothers' death-ages in one word; Deuteronomy 32:50 "as Aaron your brother died in Mount Hor".
assert words('Num', 33, 38) == ['ויעל', 'אהרן', 'הכהן', 'אל', 'הר', 'ההר', 'על', 'פי', 'יהוה', 'וימת', 'שם', 'בשנת', 'הארבעים', 'לצאת', 'בני', 'ישראל', 'מארץ', 'מצרים', 'בחדש', 'החמישי', 'באחד', 'לחדש']
assert phrase(['בשנת', 'הארבעים'], None) == ['1Chr 26:31', 'Num 33:38'] and U('הארבעים') == ['1Chr 26:31', 'Gen 18:29', 'Num 33:38'] and words('Deut', 1, 3)[:8] == ['ויהי', 'בארבעים', 'שנה', 'בעשתי', 'עשר', 'חדש', 'באחד', 'לחדש']
assert phrase(['לצאת', 'בני', 'ישראל', 'מארץ', 'מצרים'], None) == ['1Kgs 6:1', 'Exod 19:1', 'Num 33:38'] and words('1Kgs', 6, 1)[:6] == ['ויהי', 'בשמונים', 'שנה', 'וארבע', 'מאות', 'שנה'] and words('Exod', 19, 1)[:2] == ['בחדש', 'השלישי']
assert phrase(['בחדש', 'החמישי'], None) == ['Ezra 7:8', 'Jer 1:3', 'Jer 28:1', 'Num 33:38'] and len(phrase(['באחד', 'לחדש'])) == 10 and U('במתו') == ['Deut 34:7', 'Num 33:39'] and words('Deut', 34, 7)[:6] == ['ומשה', 'בן', 'מאה', 'ועשרים', 'שנה', 'במתו']
assert words('Num', 33, 39) == ['ואהרן', 'בן', 'שלש', 'ועשרים', 'ומאת', 'שנה', 'במתו', 'בהר', 'ההר'] and words('Exod', 7, 7)[4:9] == ['ואהרן', 'בן', 'שלש', 'ושמנים', 'שנה'] and words('Deut', 32, 50)[9:15] == ['כאשר', 'מת', 'אהרן', 'אחיך', 'בהר', 'ההר']
assert words('Num', 20, 28) == ['ויפשט', 'משה', 'את', 'אהרן', 'את', 'בגדיו', 'וילבש', 'אתם', 'את', 'אלעזר', 'בנו', 'וימת', 'אהרן', 'שם', 'בראש', 'ההר', 'וירד', 'משה', 'ואלעזר', 'מן', 'ההר'] and aramaic(33, 38)[10:12] == ['בשנת', 'ארבעין']
# 33:40 ARAD: "and the Canaanite king of Arad heard" — 21:1 and 33:40 the phrase's two seats; the itinerary keeps the HEARING and drops the war,
# the captives, the vow and Hormah (21:1-3), adds "in the land of Canaan"; its place is right after Aaron's death and age — the Sifrei's row on
# 21:1 (82:1, on 10:33: "when Aaron died they said, their high priest has died, their great scout is gone") reads the hearing as the news of
# that death: 33:38-40's own order is the ink that reading stands on (OBSERVED; the row read at sitting 3, not a row on 33). Arad four seats.
assert words('Num', 33, 40) == ['וישמע', 'הכנעני', 'מלך', 'ערד', 'והוא', 'ישב', 'בנגב', 'בארץ', 'כנען', 'בבא', 'בני', 'ישראל'] and words('Num', 21, 1) == ['וישמע', 'הכנעני', 'מלך', 'ערד', 'ישב', 'הנגב', 'כי', 'בא', 'ישראל', 'דרך', 'האתרים', 'וילחם', 'בישראל', 'וישב', 'ממנו', 'שבי']
assert phrase(['וישמע', 'הכנעני'], None) == ['Num 21:1', 'Num 33:40'] and phrase(['מלך', 'ערד'], None) == ['Josh 12:14', 'Num 21:1', 'Num 33:40'] and U('ערד') == ['Josh 12:14', 'Judg 1:16', 'Num 21:1', 'Num 33:40'] and 'וילחם' not in words('Num', 33, 40) and 'כנען' not in words('Num', 21, 1)

# THE LAST STATIONS (33:41-49) AGAINST CHAPTER 21 (computed): Zalmonah and Punon named here alone; OBOTH and IYE-ABARIM are 21:10-11's ("and
# camped in Oboth"; "in Iye-abarim" — 21:11 "in the wilderness before Moab toward the sunrise", 33:44 "in the border of Moab"); of chapter 21's
# stations after Iye-abarim (the Zered, beyond the Arnon, Beer, Mattanah, Nahaliel, Bamoth, the valley of Pisgah, 21:12-20) NOT ONE is in the
# itinerary, and the itinerary's Dibon-gad, Almon-diblathaim and the mountains of Abarim are not in 21 — the two lists share Oboth, Iye-abarim
# and Moab's name alone; "from Iim" (33:45) the short form's one seat; DIBON-GAD two seats (Gad built Dibon, 32:34 — the itinerary's witness);
# Almon-diblathaim two, Jeremiah 48:22's Beth-diblathaim Moab's; "the MOUNTAINS of Abarim before Nebo" (plural, 33:47-48) beside "the MOUNTAIN
# of Abarim" (27:12; Deuteronomy 32:49 "mount Nebo"); "the plains of Moab" eight Torah seats, "by the Jordan at Jericho" seven; 33:49 the camp's
# extent "from Beth-jeshimoth to Abel-shittim" — Beth-jeshimoth Reuben's (Joshua 13:20) and Moab's glory (Ezekiel 25:9), Abel-shittim one seat
# and Shittim Peor's (25:1), the spies' and the crossing's (Joshua 2:1, 3:1), Micah's "from Shittim to Gilgal" (6:5). ONKELOS: "the plains of
# Moab" as "the plains" (the same word at all eight seats), "the plain of Shittim", Iye-abarim "the fords of the Abarim".
assert U('באבת', 'מאבת') == ['Num 21:10', 'Num 21:11', 'Num 33:43', 'Num 33:44'] and phrase(['בעיי', 'העברים'], None) == ['Num 21:11', 'Num 33:44'] and U('מעיים') == ['Num 33:45'] and words('Num', 21, 11)[3:9] == ['בעיי', 'העברים', 'במדבר', 'אשר', 'על', 'פני'] and words('Num', 33, 44)[-3:] == ['העברים', 'בגבול', 'מואב']
n21 = {x for v in range(10, 21) for x, m in by[('Num', 21, v)] if m and 'Np' in m}; n33 = {x for v in range(41, 50) for x, m in by[('Num', 33, v)] if m and 'Np' in m}
assert sorted(n21 & n33) == ['באבת', 'בעיי', 'העברים', 'מאבת', 'מואב'] and 'זרד' in n21 and 'ארנון' in n21 and 'הפסגה' in n21 and 'בדיבן' in n33 and 'נבו' in n33
assert phrase(['בדיבן', 'גד'], None) == ['Num 33:45'] and phrase(['מדיבן', 'גד'], None) == ['Num 33:46'] and len(U('דיבן', 'דיבון', 'ודיבן', 'בדיבן', 'מדיבן')) == 10 and words('Num', 32, 34)[:5] == ['ויבנו', 'בני', 'גד', 'את', 'דיבן']
assert U('דבלתים', 'דבלתימה') == ['Jer 48:22', 'Num 33:46', 'Num 33:47'] and words('Jer', 48, 22)[-3:] == ['ועל', 'בית', 'דבלתים']
assert phrase(['בהרי', 'העברים'], None) == ['Num 33:47'] and phrase(['מהרי', 'העברים'], None) == ['Num 33:48'] and phrase(['הר', 'העברים'], None) == ['Deut 32:49', 'Num 27:12'] and phrase(['לפני', 'נבו'], None) == ['Num 33:47'] and words('Deut', 32, 49)[:7] == ['עלה', 'אל', 'הר', 'העברים', 'הזה', 'הר', 'נבו']
assert phrase(['בערבת', 'מואב']) == ['Deut 34:8', 'Num 26:3', 'Num 26:63', 'Num 33:48', 'Num 33:49', 'Num 33:50', 'Num 35:1', 'Num 36:13'] and phrase(['על', 'ירדן', 'ירחו']) == ['Num 26:3', 'Num 26:63', 'Num 31:12', 'Num 33:48', 'Num 33:50', 'Num 35:1', 'Num 36:13'] and words('Num', 22, 1)[4:6] == ['בערבות', 'מואב']
assert words('Num', 33, 49) == ['ויחנו', 'על', 'הירדן', 'מבית', 'הישמת', 'עד', 'אבל', 'השטים', 'בערבת', 'מואב'] and phrase(['מבית', 'הישמת'], None) == ['Num 33:49'] and phrase(['אבל', 'השטים'], None) == ['Num 33:49'] and words('Josh', 13, 20)[-2:] == ['ובית', 'הישמות'] and words('Ezek', 25, 9)[11:13] == ['בית', 'הישימת']
assert words('Num', 25, 1)[:3] == ['וישב', 'ישראל', 'בשטים'] and words('Josh', 2, 1)[4:6] == ['מן', 'השטים'] and words('Josh', 3, 1)[4] == 'מהשטים' and words('Mic', 6, 5)[14:18] == ['מן', 'השטים', 'עד', 'הגלגל']
assert onk_seats('מישריא דמואב') == [(26, 3), (26, 63), (31, 12), (33, 48), (33, 49), (33, 50), (35, 1), (36, 13)] and aramaic(33, 49)[6:8] == ['מישר', 'שטין'] and onk_seats('מגזת') == [(33, 44), (33, 45)] and aramaic(33, 44)[3:5] == ['במגזת', 'עבראי'] and aramaic(21, 11)[3] == 'במגיזת'

# THE COMMAND (33:50-56): the frame "and the LORD spoke to Moses in the plains of Moab by the Jordan at Jericho" — 33:50 and 35:1 (the itinerary's
# close and the Levite cities' opening); "when you pass over the Jordan into the land of Canaan" — 33:51, 35:10 (the refuge cities' — "to the land
# of Canaan" with the directional ending there), Deuteronomy 11:31; "you shall DRIVE OUT all the inhabitants of the land from before you" one
# seat; "the inhabitants of the land" five Torah seats (Exodus 23:31 "I will deliver the inhabitants of the land into your hand and you shall
# drive them out" — the promise this command runs); "their FIGURED STONES" — Leviticus 26:1's "figured stone" the noun's other Torah seat (Psalm
# 73:7 the third); "their MOLTEN IMAGES" one seat (the "molten" of the calf, Exodus 32:4, 8; Deuteronomy 9:12, 16; 34:17; Leviticus 19:4; 27:15);
# "their HIGH PLACES you shall DESTROY" — Leviticus 26:30's curse "I will destroy your high places" the same verb on the same object, the
# command and its curse; "destroy" (this form) two Bible seats; "their high places" shares its consonants with "at their death" (Leviticus 11:31-32, 6:7 — the homograph told by the points and the morphology, a plural noun here). Exodus 23:24, 34:13, Deuteronomy 7:5 and 12:2-3 name OTHER objects (altars,
# pillars, asherim, graven images): 33:52's three are its own. 33:53 "possess the land and dwell in it, for to you I have given the land to
# possess it" — "dwell in it" Deuteronomy 11:31's, "to possess it" Leviticus 20:24's. ONKELOS: "their HOUSES OF WORSHIP" for the figured stones
# (31:10's word for Midian's encampments), "you shall drive out" for the dispossessing.
assert phrase(['וידבר', 'יהוה', 'אל', 'משה', 'בערבת', 'מואב'], None) == ['Num 33:50', 'Num 35:1'] and phrase(['כי', 'אתם', 'עברים', 'את', 'הירדן'], None) == ['Deut 11:31', 'Num 33:51', 'Num 35:10'] and words('Num', 35, 10)[-2:] == ['ארצה', 'כנען'] and words('Num', 33, 51)[-3:] == ['אל', 'ארץ', 'כנען']
assert words('Num', 33, 52) == ['והורשתם', 'את', 'כל', 'ישבי', 'הארץ', 'מפניכם', 'ואבדתם', 'את', 'כל', 'משכיתם', 'ואת', 'כל', 'צלמי', 'מסכתם', 'תאבדו', 'ואת', 'כל', 'במתם', 'תשמידו']
assert phrase(['והורשתם', 'את', 'כל', 'ישבי', 'הארץ'], None) == ['Num 33:52'] and U('והורשתם') == ['Deut 9:3', 'Ezra 9:12', 'Josh 8:7', 'Num 33:52', 'Num 33:53'] and phrase(['ישבי', 'הארץ']) == ['Exod 23:31', 'Gen 36:20', 'Num 32:17', 'Num 33:52', 'Num 33:55'] and words('Exod', 23, 31)[-6:] == ['בידכם', 'את', 'ישבי', 'הארץ', 'וגרשתמו', 'מפניך']
assert U('משכית', 'משכיתם') == ['Lev 26:1', 'Num 33:52'] and U('משכיות') == ['Ps 73:7'] and words('Lev', 26, 1)[9:11] == ['ואבן', 'משכית'] and phrase(['צלמי', 'מסכתם'], None) == ['Num 33:52'] and U('צלמי') == ['1Sam 6:11', '1Sam 6:5', 'Ezek 16:17', 'Ezek 23:14', 'Num 33:52']
assert U('מסכה', 'מסכתם', 'ומסכה', books=T) == ['Deut 27:15', 'Deut 9:12', 'Deut 9:16', 'Exod 32:4', 'Exod 32:8', 'Exod 34:17', 'Lev 19:4', 'Num 33:52'] and U('מסכת', books=T) == ['Exod 13:20', 'Num 33:6']   # "from Succoth" the consonantal homograph of "molten"
assert words('Lev', 26, 30)[:3] == ['והשמדתי', 'את', 'במתיכם'] and U('תשמידו') == ['Josh 7:12', 'Num 33:52'] and U('במתם') == ['Lev 11:31', 'Lev 11:32', 'Num 33:52', 'Num 6:7'] and [(x, m) for x, m in by[('Num', 33, 52)] if x == 'במתם'] == [('במתם', 'HNcfpc/Sp3mp')] and onk_seats('בית סגד') == [(31, 10), (33, 52)] and aramaic(33, 52)[10:12] == ['בית', 'סגדתהון'] and aramaic(33, 52)[0] == 'ותתרכון'
assert words('Exod', 34, 13) == ['כי', 'את', 'מזבחתם', 'תתצון', 'ואת', 'מצבתם', 'תשברון', 'ואת', 'אשריו', 'תכרתון'] and words('Deut', 7, 5)[5:] == ['מזבחתיהם', 'תתצו', 'ומצבתם', 'תשברו', 'ואשירהם', 'תגדעון', 'ופסיליהם', 'תשרפון', 'באש']
assert words('Num', 33, 53) == ['והורשתם', 'את', 'הארץ', 'וישבתם', 'בה', 'כי', 'לכם', 'נתתי', 'את', 'הארץ', 'לרשת', 'אתה'] and phrase(['וישבתם', 'בה'], None) == ['Deut 11:31', 'Num 33:53'] and phrase(['לרשת', 'אתה'], None) == ['Lev 20:24', 'Num 33:53'] and phrase(['כי', 'לכם', 'נתתי', 'את', 'הארץ'], None) == ['Num 33:53']
# 33:54 IS 26:52-56 RESTATED IN THE SECOND PERSON: "to the many you shall increase his inheritance and to the few diminish" — 26:54's clause with
# the first verb turned PLURAL (26:54 "you shall increase", singular; 33:54 "you [all] shall increase") and the object marker added, the second
# verb LEFT SINGULAR in both (computed on the morphology — the number switches inside 33:54's own verse); "by lot" four Torah seats (26:55, 33:54,
# 34:13, 36:2); "to whom the lot goes out, his it shall be" one seat; "by the tribes of your fathers" one seat (26:55 "their fathers"); "you shall
# inherit" (this stem) 33:54, 34:13, Ezekiel 47:13; "you shall take as inheritance" (33:54's opening verb) Leviticus 25:46's word for the slaves
# held as a possession. ONKELOS renders 26:54 and 33:54 with one pair of verbs, "lot" with one word at all five seats (26:55, 56; 33:54; 34:13;
# 36:2).
assert words('Num', 33, 54) == ['והתנחלתם', 'את', 'הארץ', 'בגורל', 'למשפחתיכם', 'לרב', 'תרבו', 'את', 'נחלתו', 'ולמעט', 'תמעיט', 'את', 'נחלתו', 'אל', 'אשר', 'יצא', 'לו', 'שמה', 'הגורל', 'לו', 'יהיה', 'למטות', 'אבתיכם', 'תתנחלו']
assert words('Num', 26, 54) == ['לרב', 'תרבה', 'נחלתו', 'ולמעט', 'תמעיט', 'נחלתו', 'איש', 'לפי', 'פקדיו', 'יתן', 'נחלתו'] and phrase(['לרב', 'תרבו'], None) == ['Num 33:54'] and phrase(['לרב', 'תרבה'], None) == ['Num 26:54'] and phrase(['ולמעט', 'תמעיט'], None) == ['Num 26:54', 'Num 33:54']
assert [(x, m) for x, m in by[('Num', 33, 54)] if x in ('תרבו', 'תמעיט')] == [('תרבו', 'HVhi2mp'), ('תמעיט', 'HVhi2ms')] and [(x, m) for x, m in by[('Num', 26, 54)] if x in ('תרבה', 'תמעיט')] == [('תרבה', 'HVhi2ms'), ('תמעיט', 'HVhi2ms')]
assert U('בגורל', books=T) == ['Num 26:55', 'Num 33:54', 'Num 34:13', 'Num 36:2'] and phrase(['אל', 'אשר', 'יצא', 'לו', 'שמה', 'הגורל'], None) == ['Num 33:54'] and phrase(['למטות', 'אבתיכם'], None) == ['Num 33:54'] and words('Num', 26, 55)[-3:] == ['מטות', 'אבתם', 'ינחלו'] and U('תתנחלו') == ['Ezek 47:13', 'Num 33:54', 'Num 34:13'] and U('והתנחלתם') == ['Lev 25:46', 'Num 33:54']
assert onk_seats('עדבא') == [(26, 55), (26, 56), (33, 54), (34, 13), (36, 2)] and aramaic(33, 54)[5:7] == ['לסגיאי', 'תסגון'] and aramaic(26, 54)[:2] == ['לסגיאי', 'תסגון'] and aramaic(33, 54)[9:11] == ['ולזעירי', 'תזעירון'] and aramaic(33, 54)[0] == 'ותחסנון'
# 33:55 THE NEGATIVE ARM: "and IF you do not drive out the inhabitants of the land from before you, those you LEAVE OVER shall be THORNS in your
# eyes and PRICKS in your sides, and they shall HARASS you" — Joshua 23:13 runs it back reversed ("scourges in your SIDES and thorns in your EYES"
# — the pricks and the sides the shared words, each two Bible seats) and Judges 2:3 "they shall be to you for sides"; "thorns" one seat; "harass"
# one seat (25:18's "they harass you" Midian's); "leave over" three Torah seats — the Passover's "you shall leave none of it until morning"
# (Exodus 12:10), Leviticus 22:30, this. ONKELOS reads the figure as its referent: "bands TAKING UP ARMS against you and camps SURROUNDING you"
# (one seat in Onkelos Numbers). 33:56 "as I THOUGHT to do to them" — Isaiah 14:24's "as I have thought, so shall it be" the phrase's other seat;
# Onkelos "as I PLANNED".
assert words('Num', 33, 55) == ['ואם', 'לא', 'תורישו', 'את', 'ישבי', 'הארץ', 'מפניכם', 'והיה', 'אשר', 'תותירו', 'מהם', 'לשכים', 'בעיניכם', 'ולצנינם', 'בצדיכם', 'וצררו', 'אתכם', 'על', 'הארץ', 'אשר', 'אתם', 'ישבים', 'בה']
assert U('תורישו') == ['Num 33:55'] and U('תותירו') == ['Exod 12:10', 'Lev 22:30', 'Num 33:55'] and U('לשכים') == ['Num 33:55'] and U('ולצנינם', 'ולצננים') == ['Josh 23:13', 'Num 33:55'] and U('בצדיכם') == ['Josh 23:13', 'Num 33:55'] and U('וצררו') == ['Num 33:55'] and words('Num', 25, 18)[:3] == ['כי', 'צררים', 'הם']
assert words('Josh', 23, 13)[16:20] == ['ולשטט', 'בצדיכם', 'ולצננים', 'בעיניכם'] and words('Judg', 2, 3)[6:9] == ['והיו', 'לכם', 'לצדים'] and onk_seats('נטלן זין') == [(33, 55)] and aramaic(33, 55)[12:18] == ['לסיען', 'נטלן', 'זין', 'לקבליכון', 'ולמשרין', 'מקפנכון']
assert words('Num', 33, 56) == ['והיה', 'כאשר', 'דמיתי', 'לעשות', 'להם', 'אעשה', 'לכם'] and phrase(['כאשר', 'דמיתי'], None) == ['Isa 14:24', 'Num 33:56'] and words('Isa', 14, 24)[6:10] == ['כאשר', 'דמיתי', 'כן', 'היתה'] and onk_seats('חשבית') == [(33, 56)]

# THE STORE'S GLOSSES READ BACK (the display layer; the frozen unit untouched): the override file's rows by reference — RESEARCH_LOG.md
assert sg(33, 2, 'ויכתב') == 'and-grave' and sg(33, 3, 'הפסח') == 'the-pretermission' and sg(33, 3, 'רמה') == 'be-high-actively' and sg(33, 4, 'שפטים') == 'sentence' and sg(33, 54, 'בגורל') == 'in-pebble' and sg(33, 55, 'וצררו') == 'and-cramp' and sg(33, 55, 'תותירו') == 'jut-over' and sg(33, 56, 'דמיתי') == 'compare'
assert sg(33, 52, 'ואבדתם') == 'and-wander-away' and sg(33, 52, 'משכיתם') == 'figure-them/their' and sg(33, 52, 'מסכתם') == 'pouring-over-them/their' and sg(33, 52, 'במתם') == 'elevation-them/their' and sg(33, 52, 'תשמידו') == 'desolate' and sg(33, 44, 'בגבול') == 'in-cord' and sg(33, 55, 'לשכים') == 'to-brier' and sg(33, 9, 'עינת') == 'eye'
OV = open(f'{ROOT}/logic/glosses/word_gloss_overrides.yaml', encoding='utf-8').read()
OVERRIDE_ROWS = [('Num.33.2:0', 'and-he-wrote'), ('Num.33.3:10', 'the-Passover'), ('Num.33.3:15', 'high'), ('Num.33.4:12', 'judgments'), ('Num.33.9:7', 'springs-of'), ('Num.33.44:5', 'in-the-border-of'), ('Num.33.52:6', 'and-you-shall-destroy'), ('Num.33.52:9', 'their-figured-stones'), ('Num.33.52:13', 'their-molten-images'), ('Num.33.52:17', 'their-high-places'), ('Num.33.52:18', 'you-shall-destroy'), ('Num.33.54:3', 'by-lot'), ('Num.33.55:9', 'you-leave-over'), ('Num.33.55:11', 'as-thorns'), ('Num.33.55:15', 'and-they-shall-harass'), ('Num.33.56:2', 'I-intended'), ('Num.33.7:4', 'Pi-'), ('Num.33.7:9', 'Baal-'), ('Num.33.16:4', 'in-Kibroth-'), ('Num.33.49:3', 'from-Beth-'), ('Num.33.49:6', 'Abel-')]
STORE_IDX = {(v, tok): idx for v, idx, tok in store.execute("SELECT v.verse, w.idx, REPLACE(w.he_plain,'/','') FROM words w JOIN verses v ON w.verse_id=v.id WHERE v.book='Num' AND v.chapter=33")}
assert STORE_IDX[(2, 'ויכתב')] == 0 and STORE_IDX[(3, 'הפסח')] == 10 and STORE_IDX[(3, 'רמה')] == 15 and STORE_IDX[(4, 'שפטים')] == 12 and STORE_IDX[(9, 'עינת')] == 7 and STORE_IDX[(44, 'בגבול')] == 5 and STORE_IDX[(52, 'ואבדתם')] == 6 and STORE_IDX[(52, 'משכיתם')] == 9 and STORE_IDX[(52, 'מסכתם')] == 13 and STORE_IDX[(52, 'במתם')] == 17 and STORE_IDX[(52, 'תשמידו')] == 18 and STORE_IDX[(54, 'בגורל')] == 3 and STORE_IDX[(55, 'תותירו')] == 9 and STORE_IDX[(55, 'לשכים')] == 11 and STORE_IDX[(55, 'וצררו')] == 15 and STORE_IDX[(56, 'דמיתי')] == 2 and STORE_IDX[(7, 'פי')] == 4 and STORE_IDX[(7, 'בעל')] == 9 and STORE_IDX[(16, 'בקברת')] == 4 and STORE_IDX[(49, 'מבית')] == 3 and STORE_IDX[(49, 'אבל')] == 6

import os as _os
_ROOT = _os.path.normpath(_os.path.join(_os.path.dirname(_os.path.abspath(__file__)), '..', '..', '..'))   # THE PORTABLE REPO (2026-09-15): the repo root from this file's own place
#!/usr/bin/env python3
# THE NUMBERS WALK, sitting 15 — THE REFUGE CITIES, Numbers 35:1-34 (2026-09-13; the owner: "Go" after the #157 rereads, on the ruling READ
# THEN COMPILE): THE INK of the chapter, computed from the Tanakh DB, the snapshot store and the shelf's own bytes — never typed. Sitting 14's
# form (bor_ink.py) with sitting 11's Sifrei block (midian_ink.py): THE SIFREI RETURNS at 35:9 — piskaot 159-161 found BY POSITION and asserted,
# every row's own first citation checked against its head, the two files' ROW GRAINS measured (the Hebrew 160 carries FOURTEEN rows where the
# English carries TEN: its last four are 161:1-4 DUPLICATED — a defect class new to the walk), the rows' deltas read to their verses; the
# whole export scanned in FOUR forms for rows of other piskaot citing the chapter (1:2 on 35:2, 1:7 on 35:34 — both credited); coverage
# computed; every cut by consonants (the misses collected, asserted empty); the engine's numeral parser MEASURED on every verse — seven number
# verses read, ONE GAP: 35:5's bare dual "two thousand" (four tokens) unread, the class named for the compile (4b's owed line paid by a
# measurement); the hand's facts as asserts, run all at once by assert_driver.py after the measurement passes (ref_dump.py, ref_measure1.py,
# ref_measure2.py) printed them; every gloss the STORE'S OWN (words.gloss); the piece-wise cutters HP / AP. Shared by ref_rows_onkelos_a.py /
# _b.py, ref_rows_sifrei.py and write_ref_ledger.py.
# THE SPAN: ONE draft — num_35_refuge_cities 35:1-34 (the portion Masei's third chapter); the next unit (num_36_heiresses, 36:1-13) is FROZEN
# at THE TENT: this is the walk's LAST reading in Numbers.
import json, os, re, html, sqlite3, sys, io, contextlib, unicodedata
from collections import Counter
ROOT = _ROOT
DATE = '2026-09-13'
UID = 'num_35_refuge_cities'
PISKAOT = [159, 160, 161]
CREDITED = [(1, 2, (35, 2)), (1, 7, (35, 34))]
TITLE = 'The refuge cities — the Levites given forty-eight cities with their pasture-lands, a thousand cubits from the wall and two thousand by the cubit on each side, six of them cities of refuge; when you cross the Jordan you shall appoint cities of refuge for the slayer who smites a soul unwittingly, that he die not until he stands before the congregation; the murderer by iron, by a stone of the hand, by a wooden hand-instrument, in hatred, in lying-in-wait, in enmity — the avenger of blood puts him to death; the one who thrust suddenly without enmity, threw without lying-in-wait, dropped a stone unseen — the congregation judges, delivers him, returns him to his city of refuge until the death of the high priest anointed with the holy oil; outside its border the avenger has no blood; a statute of judgment: by witnesses, never one; no ransom for the murderer, none for the fugitive; the land not polluted, for blood pollutes the land and is atoned only by the shedder\'s blood; the land not defiled, for I the LORD dwell in the midst of the children of Israel'
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
# THE SHELF BY POSITION: piska 158 (31:22) is followed by 159 (35:9), 160 (35:12), 161 (35:29) — the export's LAST THREE piskaot, all on this
# chapter; NO piska on 35:1-8 (the Levite cities: the shelf's silence from 31:25 runs to 35:8, as sitting 11 computed); the rows' own first
# citations are their heads in order (no mistyped head in the chapter; 161:4 opens on Deuteronomy 21:1 — the two priests' story, read at 35:33).
assert heads[158] == ('Bamidbar', 31, 22) and heads[159] == ('Bamidbar', 35, 9) and heads[160] == ('Bamidbar', 35, 12) and heads[161] == ('Bamidbar', 35, 29) and len(sif) == 161 and len(sif_he) == 161
assert sorted(p for p, h in heads.items() if h and h[0] == 'Bamidbar' and h[1] == 35) == PISKAOT and [p for p, h in heads.items() if h and h[0] == 'Bamidbar' and h[1] == 35 and h[2] < 9] == [] and [p for p in range(150, 162) if heads.get(p) is None] == []
def E(p, r): return clean(sif[p - 1][r - 1])
def Hb(p, r): return clean(sif_he[p - 1][r - 1])
def head(p): return heads[p][1:]
SIF_ROWS = {p: len(sif[p - 1]) for p in PISKAOT}
SIF_ROWS_HE = {p: len(sif_he[p - 1]) for p in PISKAOT}
assert SIF_ROWS == {159: 1, 160: 10, 161: 5} and SIF_ROWS_HE == {159: 1, 160: 14, 161: 5} and sum(SIF_ROWS.values()) == 16 and sum(SIF_ROWS_HE.values()) == 20
# THE ROW-GRAIN MISMATCH, READ: the Hebrew 160:11-14 ARE 161:1-4 AGAIN — byte-near-identical (the dash character the one systematic
# difference; 160:11 drops the kaf of "כל" (all) — "ל מכה" (smites) for "כל מכה" (whoever smites); 161:4 alone parenthesizes its Kings
# citation) — the export's Hebrew file duplicates the block at the end of 160 before opening 161 with it: A DUPLICATED BLOCK, a defect class
# new to the walk (RESEARCH_LOG.md). The ledger's grain is the ENGLISH's sixteen rows (each read in both files); the four duplicates are read
# as their 161 twins, named, never counted twice.
def nd(s): return s.replace('–', '-')
assert nd(Hb(160, 12)) == Hb(161, 2) and nd(Hb(160, 13)) == Hb(161, 3) and nd(Hb(160, 11)).replace(': ל מכה נפש', ': כל מכה נפש') == Hb(161, 1) and nd(Hb(160, 14)).replace('מלכים ב כא', '(מלכים ב כא)') == Hb(161, 4)
assert Hb(161, 5).rstrip().endswith('כי אני ה\' שוכן בתוך בני ישראל: סליק להו ספר במדבר סיני ברוך הגבר אשר יבטח באדני:') and E(161, 5).rstrip().endswith('"For I, the L-rd dwell in the midst of the children of Israel."')   # the Hebrew's colophon — the book ends here; the English drops it
# THE ROWS' HEADS CHECKED AGAINST THEIR OWN CITATIONS (the mistyped-head class): every row's first citation
ROW_CITES = [(p, r, re.search(r'\(([A-Z][a-z]+)\.? ?(\d+):(\d+)', E(p, r)).groups()) for p in PISKAOT for r in range(1, SIF_ROWS[p] + 1)]
assert [(b, int(c), int(v)) for _, _, (b, c, v) in ROW_CITES] == [('Bamidbar', 35, 9), ('Bamidbar', 35, 12), ('Bamidbar', 35, 13), ('Bamidbar', 35, 16), ('Bamidbar', 35, 18), ('Bamidbar', 35, 19), ('Bamidbar', 35, 20), ('Bamidbar', 35, 21), ('Bamidbar', 35, 22), ('Bamidbar', 35, 25), ('Bamidbar', 35, 26), ('Bamidbar', 35, 29), ('Bamidbar', 35, 32), ('Bamidbar', 35, 33), ('Devarim', 21, 1), ('Bamidbar', 35, 34)], ROW_CITES
# THE ROWS' DEFECTS, read to their verses in BOTH files (RESEARCH_LOG.md): (a) 159:1 the English cites "Devarim 12:29" where the Hebrew
# says "Deuteronomy 19" — the clause "when the LORD your God cuts off the nations" stands at BOTH 12:29 and 19:1, and 19:1 opens the
# refuge chapter of Deuteronomy (the Hebrew's is the apt seat); the English "Ibid. 26:3" for "at the Jordan, Jericho" where the Hebrew
# says "Numbers 36" (36:13 — the phrase stands at seven seats); (b) 160:2 the Hebrew misquotes Joshua 20:7 — "Kiriath-arba, that is Hebron,
# IN THE LAND OF CANAAN" for the ink's "in the hill country of Judah"; the Hebrew's a-fortiori "all the more he is not exiled" dropped by the
# English; (c) 160:3 the Hebrew's citation "Exodus 11" mistyped for 21:18; the Hebrew carries THE RULE ABOUT RULES "we do not punish by
# inference" and the English drops it — the same rule dropped at 157:6 (sitting 11's finding), a second instance; (d) 160:5 THE ENGLISH ROW
# IS NOT THE HEBREW ROW: the Hebrew 160:5 is the induction from the three instruments (the common feature — anything that can kill) ending
# "the commandment is in the hand of the avenger"; the English 160:5 is two sentences on the court-appointed avenger (the Hebrew's 160:7
# tail, which the English 160:7 also carries) and the induction is carried into the English 160:6; (e) 160:8 the English "thirty" for the
# Hebrew's TWENTY-THREE, its "[27]" for the congregation-token's seats (the ink: 24, 25, 25 — and 12), and the Mishnah's acquittal-by-one /
# conviction-by-two SUPPLIED where the Hebrew says "as witnesses are two, so the judges are two, and a court is not even — add one"; (f)
# 160:10 the English's bracketed "(37)" and "(38)" for verses 27 and 28; (g) 161:1 the English inserts "Whence is this derived? From 'And you
# shall not take ransom'" where the Hebrew has no derivation clause; (h) 161:4 the Hebrew cites 2 Kings 21 in parentheses at 161:4 and bare
# at its duplicate 160:14. THE MOVES IN THE ROWS: the induction from three verses (the common feature, 160:5 HE / 160:6 EN); the a-fortiori
# refused on a penalty (160:3); the prototype "witness means two unless 'one' is written" (161:1); THE NOTARIKON — the word split into two:
# "it pollutes" read as "it rests wrath" (161:3, R. Yoshiyah) — a move to check against MOVE_CATALOG.
assert '(Devarim 12:29)' in E(159, 1) and 'דברים יט' in Hb(159, 1) and '(Ibid. 26:3)' in E(159, 1) and 'במדבר לו' in Hb(159, 1)
assert 'ואת קרית הארבע היא חברון בארץ כנען' in Hb(160, 2) and 'ק"ו שלא יגלה' in Hb(160, 2) and 'How so? If an Israelite killed him, he is exempt. If he killed an Israelite, he is killed.' in E(160, 2)
assert 'שמות יא' in Hb(160, 3) and 'שאין עונשים מן הדין' in Hb(160, 3) and 'inference' not in E(160, 3) and 'even a needle or a pin' in E(160, 3)
assert E(160, 5).strip().startswith('(Bamidbar 35:19) "the avenger, he shall kill the murderer": The mitzvah is the avenger\'s. Whence is it derived that if he has no avenger, beth-din designates one for him?') and Hb(160, 5).startswith('גואל הדם הוא ימית את הרוצח – למה נאמר? לפי שהוא אומר אם באבן יד או בכלי עץ') and 'הרי אתה דן בנין אב מבין שלשתם' in Hb(160, 5) and 'It follows by induction from all three' in E(160, 6) and 'מי שאין לו גואל מנין? ת"ל גואל הדם מ"מ' in Hb(160, 7) and 'one who does not have an avenger' in E(160, 7)
assert 'בעשרים ושלשה' in Hb(160, 8) and 'adjudicated by thirty' in E(160, 8) and '[27]' in E(160, 8) and 'acquittal, is with a majority of one, and incrimination by a majority of two' in E(160, 8) and 'מה עדים שנים אף דיינים שנים, ואין בית דין שקול' in Hb(160, 8)
assert re.findall(r'\((\d\d)\)', E(160, 10)) == ['27', '37', '38'] and 'Whence is this derived? From "And you shall not take ransom,"' in E(161, 1) and 'וחבל באחרים - חייב. חבלו בו אחרים - פטורים בגופו, ולא בממונו' in Hb(161, 1)
assert 'נוטריקון: כי הדם יחון אף בארץ' in Hb(161, 3) and 'acronymically' in E(161, 3) and re.findall(r'\([^)]*\)', Hb(161, 4)) == ['(מלכים ב כא)'] and re.findall(r'\([^)]*\)', Hb(160, 14)) == [] and '(Devarim 21:1)' in E(161, 4) and '(II Kings 21:16)' in E(161, 4)
assert re.findall(r'\([^)]*\)', Hb(161, 5)) == ['(שמואל א ב)', '(ישעיה מג)', '(ירמיה מט)', '(ישעיה סג)', '(דברים ל)', '(שיר השירים ד)', '(ויקרא טז)', '(ויקרא טו)', '(במדבר לה)']
# THE "FOUND BY POSITION" CLAUSE run on the whole export in FOUR FORMS for rows OUTSIDE 159-161: "(Bamidbar 35:n)" ONE row — 1:2 (on 5:2:
# Rabbi Shimon ben Yochai's "command" entails expense — 35:2 "command the children of Israel and give to the Levites from the inheritance" the
# third of his four); the Hebrew's "ibid. 35" the same row; the Hebrew's chapter mark with the gershayim ONE row — 1:7 (on 5:3 "that they defile
# not their camp in whose midst I dwell", citing 35:34 "you shall not defile the land ... in whose midst I dwell" — the book's inclusio, read
# at 161:5 too); no "(Ibid. 35:n)" in the English. Both CREDITED with a quick look (read whole at sitting 2, the Naso ledger).
CIT_A = [(p, r, re.findall(r'\(Bamidbar\.? 35:(\d+)', E(p, r))) for p, rows in enumerate(sif, 1) for r, row in enumerate(rows, 1) if p not in PISKAOT and re.search(r'\(Bamidbar\.? 35:\d+', clean(row))]
CIT_B = [(p, r) for p, rows in enumerate(sif, 1) for r, row in enumerate(rows, 1) if p not in PISKAOT and re.search(r'\(Ibid\.? 35:\d+', clean(row))]
CIT_C = [(p, r) for p, rows in enumerate(sif_he, 1) for r, row in enumerate(rows, 1) if p not in PISKAOT and re.search(r'במדבר ל[\"״]?ה\b', clean(row))]
CIT_D = [(p, r) for p, rows in enumerate(sif_he, 1) for r, row in enumerate(rows, 1) if p not in PISKAOT and re.search(r'שם ל[\"״]?ה[\)\s:]', clean(row))]
assert CIT_A == [(1, 2, ['2'])] and CIT_B == [] and CIT_C == [(1, 7)] and CIT_D == [(1, 2)], (CIT_A, CIT_B, CIT_C, CIT_D)
assert heads[1] == ('Bamidbar', 5, 1) and '(Bamidbar 35:2) "Command the children of Israel that they give to the Levites from the inheritance, etc."' in E(1, 2) and 'צו את בני ישראל ונתנו ללוים מנחלת (שם ל"ה)' in Hb(1, 2)
assert '(Bamidbar) 35:34) "And you shall not defile the land which you inhabit, in which I dwell' in E(1, 7) and '(במדבר ל״ה:ל״ד)' in Hb(1, 7) and 'ולא תטמא את הארץ אשר אתם יושבים בה' in Hb(1, 7)
TRI = f'{ROOT}/logic/oral_triage'
LED = {f: open(f'{TRI}/{f}', encoding='utf-8').read() for f in os.listdir(TRI) if f.endswith('.md') and os.path.isfile(f'{TRI}/{f}') and f'{TRI}/{f}' != OUT}
assert re.search(r'^- Sifrei Bamidbar 1:2 — MATERIAL\. FOUR READINGS OF "COMMAND"', LED['num_05_camp_pure_theft_2026-09-09.md'], re.M) and re.search(r'^- Sifrei Bamidbar 1:7 ', LED['num_05_camp_pure_theft_2026-09-09.md'], re.M)
def plain(w): return ''.join(c for c in w if c != '/' and not (0x0591 <= ord(c) <= 0x05C7))
def pointed(w): return ''.join(c for c in w if c != '/' and not (0x0591 <= ord(c) <= 0x05AF))
def NF(s): return unicodedata.normalize('NFC', s)   # THE MARKS' ORDER (sittings 7 and 14): every pointed comparison on NFC both sides
ONK_LEN = {c: len(onk[c - 1]) for c in (34, 35, 36)}
assert ONK_LEN == {34: 29, 35: 34, 36: 13} and {c: len(onk_he[c - 1]) for c in (34, 35, 36)} == ONK_LEN, ONK_LEN
def onk_ev(c, v): return clean(onk[c - 1][v - 1]), clean(onk_he[c - 1][v - 1])
shelf_numbers = sorted(d for d in os.listdir(f'{ROOT}/Data/sefaria_export') if re.search(r'Numbers|Bamidbar', d))
outside = [d for d in shelf_numbers if d not in ('Sifrei_Bamidbar', 'Onkelos_Numbers')]
assert len(outside) == 23, len(outside)
# THE PRIOR READS: no ledger has read an Onkelos row of 35 or a row of 159-161; FIFTEEN ledgers NAME a verse of the chapter (the Sabbath block's
# 35:4-5 — the two thousand cubits as the Sabbath limit's measure; the exams' 35:22-27, 35:29-31; the sotah's and the vows'): names, not reads — FRESH.
assert sorted(f for f, t in LED.items() if re.search(r'^- Onkelos Num 35:\d', t, re.M)) == [] and [f for f, t in LED.items() if re.search(r'Sifrei (?:Bamidbar )?(159|160|161):\d', t)] == []
NAMING = sorted((f, sorted(set(re.findall(r'Num(?:bers)? 35:\d+(?:-\d+)?', t)))) for f, t in LED.items() if re.search(r'Num(?:bers)? 35:\d+', t))
assert [f for f, _ in NAMING] == ['exodus_block_shabbat_2026-09-04.md', 'gen_65_first_descent_2026-08-28.md', 'incense_shekel_docket_2026-09-06.md', 'lev_24_lamp_bread_blasphemer_2026-09-05.md', 'num_01_04_bamidbar_exam_2026-09-09.md', 'num_04_07_naso_exam_2026-09-10.md', 'num_05_camp_pure_theft_2026-09-09.md', 'num_08_menorah_levites_2026-09-10.md', 'num_10_trumpets_depart_2026-09-10.md', 'num_11_complaint_quail_2026-09-10.md', 'num_13_15_shelach_exam_2026-09-10.md', 'num_27_zelophehad_joshua_2026-09-09.md', 'num_30_vows_exam_2026-09-12.md', 'num_31_midian_exam_2026-09-12.md', 'ordinances_topic_docket_2026-09-06.md'] and dict(NAMING)['exodus_block_shabbat_2026-09-04.md'] == ['Num 35:4', 'Num 35:5'], NAMING

# ---- THE DRAFT'S SPAN, COMPUTED ----
db = sqlite3.connect(f'file:{ROOT}/Data/tanakh.sqlite?mode=ro', uri=True)
VC = dict(db.execute("SELECT chapter, COUNT(*) FROM verses WHERE book='Num' GROUP BY chapter").fetchall())
assert VC[34] == 29 and VC[35] == 34 and VC[36] == 13
def unit_text(uid): return open(f'{ROOT}/logic/units/{uid}.yaml', encoding='utf-8').read()
def steps(uid): return sorted({(int(a), int(b)) for a, b in re.findall(r'STEP_Nm_(\d+)_(\d+)', unit_text(uid))})
assert steps(UID) == [(35, v) for v in range(1, 35)] and 'status: draft' in unit_text(UID) and 'operators:' not in unit_text(UID) and 'refs: "35:1-34"' in unit_text(UID)
assert steps('num_36_heiresses') == [(36, v) for v in range(1, 14)] and 'status: frozen' in unit_text('num_36_heiresses') and 'status: frozen' in unit_text('num_34_borders')
SPAN = [(35, v) for v in range(1, 35)]
NV = 34

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
def U(*toks, books=None): return sorted(set(s for t in toks for s in hits(t, books, True)))
def LEMT(lem, books=None): return [(f'{b} {c}:{v}', x, m) for (b, c, v), ws in by.items() if (books is None or b in books) for (x, m), l in zip(ws, byl[(b, c, v)]) if l == lem]
def LEMV(lem, books=None): return sorted({s for s, _, _ in LEMT(lem, books)})
def seats_in(pred): return [(v, x) for (c, v) in SPAN for x, m in by[('Num', 35, v)] if pred(x, m)]
def cnt_in(pred): return sum(1 for (c, v) in SPAN for x, m in by[('Num', 35, v)] if pred(x, m))
def PT(b, c, v, tok): return [NF(x) for x in byp[(b, c, v)] if plain(x) == tok]
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
def onk_tok(tok): return [(c + 1, v + 1) for c in range(36) for v in range(len(onk_he[c])) if tok in aramaic(c + 1, v + 1)]
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
    """a Sifrei Hebrew row cut by consonants — the shelf's own bytes"""
    ws = Hb(p, r).split()
    out, i = [], 0
    for k in cons:
        j = i
        while j < len(ws) and plain(ws[j]).strip('.,:;?!"()–-') != k: j += 1
        if j >= len(ws): FAIL.append(('S', p, r, k)); out.append('⟨MISS⟩'); continue
        out.append(ws[j].rstrip('.,:;?!')); i = j + 1   # the shelf's own punctuation is not the quotation's (the lint reads the gloss marker right after the Hebrew)
    return ' '.join(out)
store = sqlite3.connect(f'file:{ROOT}/torah_grok.SNAPSHOT-main-51801ca.sqlite?mode=ro', uri=True)
SG = {}
for c, v, hp, g in store.execute("SELECT v.chapter, v.verse, w.he_plain, w.gloss FROM words w JOIN verses v ON w.verse_id=v.id WHERE v.book='Num' AND v.chapter = 35 ORDER BY v.id, w.idx"):
    SG.setdefault((c, v), []).append((hp.replace('/', ''), g))
def sg(c, v, tok):
    for hp, g in SG[(c, v)]:
        if hp == tok: return g
    raise KeyError((c, v, tok))
assert [(v, n, len(by[('Num', 35, v)])) for v, n in store.execute("SELECT v.verse, COUNT(*) FROM words w JOIN verses v ON w.verse_id=v.id WHERE v.book='Num' AND v.chapter=35 GROUP BY v.verse").fetchall() if n != len(by[('Num', 35, v)])] == []   # no written-and-read pair in the chapter

# THE ENGINE'S PARSER on every verse — MEASURED before the compile is asked: SEVEN number verses read — 35:4 "a thousand cubits" [1000] (the
# cubit consumed as the unit noun, 4b's rule); 35:6 "six cities of refuge ... forty-two cities" [6, 42]; 35:7 "forty-eight cities" [48];
# 35:13 [6]; 35:14 "three ... three" [3, 3]; 35:15 [6]; 35:30 "one witness" [1] — and ONE GAP: 35:5's "two thousand by the cubit" FOUR TIMES
# reads NOTHING. THE DUAL BY THE POINTS: אַלְפַּיִם (two thousand — the patach and the dagesh in the pe, the sheva under the lamed) against
# אֲלָפִים (thousands — the qamats under the lamed): the dual stands at 26 Bible seats, and the parser reads it ONLY when a hundreds-group
# follows (4:36's 2,750, 4:40's 2,630, 7:85's 2,400, Exodus 38:29's 2,400 — right); BARE, before a unit noun or with the approximation prefix,
# it reads nothing (35:5 ×4; 1 Kings 7:26 "two thousand baths"; 2 Kings 18:23 and Isaiah 36:8 "two thousand horses"), reads the following cubit
# as one (Joshua 3:4 "about two thousand cubits" → [1]), is swallowed (Joshua 7:3, Judges 20:45) or MISREAD AS A THOUSAND (1 Samuel 13:2 "two
# thousand with Saul" → 1000). The plural "thousands" (116 seats) rightly reads nothing (Exodus 18:21's "rulers of thousands"). THE CLASS
# NAMED AND LEFT FOR THE COMPILE (15b): THE BARE DUAL THOUSAND — 4b's owed line "Num 35:5's two thousand cubits", measured at last. ONKELOS
# READS THE DUAL: "two thousand" (תרין אלפין) at all four seats — the translation supplies the "two" the points carry. Beyond the chapter,
# two kin readings filed: Ezekiel 45:2's "five hundred BY five hundred" joined to 1,000 (the preposition inside a pair of measures), and
# Exodus 27:9's "fine twined linen" read as six (the linen-word's homograph).
sys.path.insert(0, f'{ROOT}/World/step9')
with contextlib.redirect_stdout(io.StringIO()):
    import cold_run_sequence as CS
def N(b, c, v): return CS.ink_numbers(CS.verse_words(b, c, v))
def O(b, c, v): return CS.ink_ordinals(CS.verse_words(b, c, v))
PARSED = {v: N('Num', 35, v) for v in range(1, NV + 1) if N('Num', 35, v)}
assert PARSED == {4: [1000], 6: [6, 42], 7: [48], 13: [6], 14: [3, 3], 15: [6], 30: [1]}, PARSED
assert {v: O('Num', 35, v) for v in range(1, NV + 1) if O('Num', 35, v)} == {} and [(v, t) for v in range(1, NV + 1) for t in CS.verse_words('Num', 35, v) if t[-1] in '#~^%@|*'] == [(4, 'אמה@')] and N('Num', 36, 1) == []
assert N('Num', 35, 5) == [] and PT('Num', 35, 5, 'אלפים') == ['אַלְפַּיִם'] * 4 and [hex(ord(ch)) for ch in PT('Num', 35, 5, 'אלפים')[0]] == ['0x5d0', '0x5b7', '0x5dc', '0x5b0', '0x5e4', '0x5b7', '0x5bc', '0x5d9', '0x5b4', '0x5dd']
DUAL = sorted({f'{b} {c}:{v}' for (b, c, v), ws in by.items() for x, r in zip([x for x, _ in ws], byp[(b, c, v)]) if x in ('אלפים', 'כאלפים', 'ואלפים', 'באלפים') and 'פַּ' in NF(r)})
PLUR = sorted({f'{b} {c}:{v}' for (b, c, v), ws in by.items() for x, r in zip([x for x, _ in ws], byp[(b, c, v)]) if x in ('אלפים', 'כאלפים', 'ואלפים', 'באלפים', 'לאלפים', 'מאלפים') and 'פַּ' not in NF(r)})
assert len(DUAL) == 26 and len(PLUR) == 116 and [s for s in DUAL if s.startswith(('Gen', 'Exod', 'Lev', 'Num', 'Deut'))] == ['Exod 38:29', 'Num 35:5', 'Num 4:36', 'Num 4:40', 'Num 7:85'], DUAL
assert N('Num', 4, 36) == [2750] and N('Num', 4, 40) == [2630] and N('Num', 7, 85)[-1] == 2400 and N('Exod', 38, 29) == [70, 2400] and N('Dan', 8, 14) == [2300] and N('1Chr', 26, 32) == [2700] and N('2Chr', 26, 12) == [2600]
assert N('Josh', 3, 4) == [1] and N('Josh', 7, 3) == [3000] and N('Judg', 20, 45) == [5000] and N('1Sam', 13, 2) == [3000, 1000] and N('1Kgs', 7, 26) == [] and N('2Kgs', 18, 23) == [] and N('Isa', 36, 8) == [] and N('Exod', 18, 21) == [100, 50, 10] and N('Num', 31, 14) == []
assert PT('1Sam', 13, 2, 'אלפים') == ['אֲלָפִים', 'אַלְפַּיִם'] and PT('Exod', 18, 21, 'אלפים') == ['אֲלָפִים'] and PT('Josh', 3, 4, 'כאלפים') == ['כְּאַלְפַּיִם'] and CS.verse_words('Josh', 3, 4)[5:7] == ['כאלפים', 'אמה@']
assert N('Josh', 21, 41) == [48] and N('Josh', 20, 7) == [4] and N('Deut', 4, 41) == [3] and N('Deut', 19, 2) == [3] and N('Deut', 19, 7) == [3] and N('Deut', 19, 9) == [3] and N('Deut', 19, 15) == [1, 2, 3] and N('Deut', 17, 6) == [2, 3, 1] and N('Num', 3, 39) == [22000] and N('Num', 26, 62) == [23000] and [N('Josh', 21, v) for v in (4, 5, 6, 7)] == [[13], [10], [13], [12]]
assert N('Ezek', 45, 2) == [1000, 50] and CS.verse_words('Ezek', 45, 2)[4:8] == ['חמש', 'מאות', 'בחמש', 'מאות'] and N('Exod', 27, 9) == [6, 100, 1] and CS.verse_words('Exod', 27, 9)[9:11] == ['שש', 'משזר']
SEQ = open(f'{ROOT}/World/step9/cold_run_sequence.py', encoding='utf-8').read().split('\n')
assert [i + 1 for i, l in enumerate(SEQ) if 'Num 35' in l or "'Num', 35" in l] == [437, 504] and 'the dual, Num 35:5' in SEQ[436] and "Num 35:5's 'two thousand cubits'" in SEQ[503]   # the parser's own two comments name the gap; no line of the tape

# THE FRAMES AND THE REGISTER: TWO divine frames — 35:1 with the PLACE-STAMP "in the plains of Moab by the Jordan at Jericho" (the stamp's six
# seats: 26:3, 26:63, 33:48, 33:50, 35:1, 36:13 — the book's footer; "and the LORD spoke to Moses in the plains of Moab" two seats, 33:50 and
# 35:1) and 35:9 bare; twelve chapters of Numbers carry exactly two, this the last. NINE narrative verbs — the two frames and SEVEN INSIDE THE
# CASES: "and he died" six times (35:16, 17, 18, 20, 21, 23) and "and he dropped it" (35:23) — the case's consequent told in the story's tense.
# THE CASE TOKENS (the compiler law's structure): "when" opens at 35:10 (the crossing); "and if" at 16, 17, 20, 22, 26; "or" at 18, 20, 21, 22,
# 23; "for" at 28, 31, 33 (twice, with "except" — כי אם) and 34. The Levite-cities paragraph is in the second person plural — "you shall give"
# TEN times (35:2, 4, 6 ×3, 7, 8, 13, 14 ×2), "you shall measure", "you shall take more / less"; the cases in the third person singular; "you
# shall not take ransom" twice, "you shall not pollute", "you shall not defile" — nine negations; "to you" five times; "he" nine; the verdict
# clause "he is a murderer" at four seats (16, 17, 18, 21).
DIV = {c: [v for v in range(1, 90) if ('Num', c, v) in by and any(words('Num', c, v)[i] in ('ויאמר', 'וידבר') and words('Num', c, v)[i + 1] == 'יהוה' for i in range(len(words('Num', c, v)) - 1))] for c in range(1, 37)}
assert DIV[35] == [1, 9] and [c for c in range(1, 37) if len(DIV[c]) == 2] == [1, 6, 7, 9, 11, 12, 16, 21, 26, 31, 34, 35]
assert words('Num', 35, 1) == ['וידבר', 'יהוה', 'אל', 'משה', 'בערבת', 'מואב', 'על', 'ירדן', 'ירחו', 'לאמר'] and words('Num', 35, 9) == ['וידבר', 'יהוה', 'אל', 'משה', 'לאמר'] and phrase(['וידבר', 'יהוה', 'אל', 'משה', 'בערבת', 'מואב']) == ['Num 33:50', 'Num 35:1'] and phrase(['בערבת', 'מואב', 'על', 'ירדן', 'ירחו']) == ['Num 26:3', 'Num 26:63', 'Num 33:48', 'Num 33:50', 'Num 35:1', 'Num 36:13'] and phrase(['על', 'ירדן', 'ירחו'], None) == ['Num 26:3', 'Num 26:63', 'Num 31:12', 'Num 33:48', 'Num 33:50', 'Num 35:1', 'Num 36:13']
assert words('Num', 36, 13) == ['אלה', 'המצות', 'והמשפטים', 'אשר', 'צוה', 'יהוה', 'ביד', 'משה', 'אל', 'בני', 'ישראל', 'בערבת', 'מואב', 'על', 'ירדן', 'ירחו']
REG = seats_in(lambda x, m: m and re.search(r'V.w', m))
assert REG == [(1, 'וידבר'), (9, 'וידבר'), (16, 'וימת'), (17, 'וימת'), (18, 'וימת'), (20, 'וימת'), (21, 'וימת'), (23, 'ויפל'), (23, 'וימת')]
CASE = {v: [x for x in words('Num', 35, v) if x in ('כי', 'אם', 'ואם', 'או')] for v in range(1, NV + 1) if any(x in ('כי', 'אם', 'ואם', 'או') for x in words('Num', 35, v))}
assert CASE == {10: ['כי'], 16: ['ואם'], 17: ['ואם'], 18: ['או'], 20: ['ואם', 'או'], 21: ['או'], 22: ['ואם', 'או'], 23: ['או'], 26: ['ואם'], 28: ['כי'], 31: ['כי'], 33: ['כי', 'כי', 'אם'], 34: ['כי']}
assert cnt_in(lambda x, m: x == 'תתנו') == 10 and [v for v, x in seats_in(lambda x, m: x == 'תתנו')] == [2, 4, 6, 6, 6, 7, 8, 13, 14, 14] and seats_in(lambda x, m: m and m.startswith('HV') and '2mp' in m and x != 'תתנו') == [(8, 'תרבו'), (8, 'תמעיטו'), (31, 'תקחו'), (32, 'תקחו'), (33, 'תחניפו')] and seats_in(lambda x, m: m and m.startswith('HC/V') and '2mp' in m) == [(5, 'ומדתם'), (11, 'והקריתם')]   # the two consecutive-perfect forms carry the conjunction's prefix
assert seats_in(lambda x, m: x in ('ולא', 'לא')) == [(12, 'ולא'), (23, 'לא'), (23, 'ולא'), (30, 'לא'), (31, 'ולא'), (32, 'ולא'), (33, 'ולא'), (33, 'לא'), (34, 'ולא')] and cnt_in(lambda x, m: x == 'לכם') == 5 and cnt_in(lambda x, m: x in ('הוא', 'והוא')) == 9 and phrase(['רצח', 'הוא']) == ['Num 35:16', 'Num 35:17', 'Num 35:18', 'Num 35:21']

# 35:1-8 THE LEVITE CITIES (computed): "command the children of Israel" the Sifrei 1:2's FIVE seats (this the third it names); "and they shall
# give to the Levites" and "from the inheritance of their possession" one seat each; "CITIES TO DWELL IN" three seats — this, Joshua 14:4 and
# JOSHUA 21:2, THE RUN'S REQUEST quoting the spec under "the LORD commanded by the hand of Moses" (the receipt form of Joshua 14:2 at 34:13),
# Joshua 21:3 the run "and the children of Israel gave to the Levites from their inheritance at the mouth of the LORD"; THE PASTURE-LAND WORD —
# six Torah seats, five this chapter's and Leviticus 25:34's ("the field of the pasture-land of their cities shall not be sold"), 69 verses in
# the Bible, 32 of them Joshua 21's; "for their cattle and their goods and all their beasts" — the beasts-word at two Bible seats (Ezekiel
# 7:13 the other), ONKELOS "all their needs of life"; "FROM THE WALL OF THE CITY OUTWARD A THOUSAND CUBITS" one seat — "a thousand cubits" the
# Bible's one seat, "two thousand by the cubit" 35:5's four tokens, "about two thousand cubits" Joshua 3:4's (the ark's distance); "YOU SHALL
# MEASURE" — the measure-verb's THREE Torah seats: the omer (Exodus 16:18), this, and THE ELDERS MEASURING TO THE SLAIN MAN (Deuteronomy 21:2,
# the heifer whose neck is broken — the case the Sifrei 161:3-4 brings to 35:33); THE FOUR SIDES IN THE CAMP'S ORDER — east, south, west, north
# (35:5) as Numbers 2 orders the camps (2:3, 10, 18, 25), where the borders ran south, west, north, east (34) and the court south, north, west,
# east (Exodus 27:9-13); "and the city in the midst" one seat; "SIX CITIES OF REFUGE" with the article one seat, bare three (35:11, 13, 14),
# "the cities of refuge" four (this, Joshua 20:2, 1 Chronicles 6:42, 52); THE REFUGE-WORD — twenty tokens in twenty verses: this chapter's
# eleven, Joshua 20's two and 21's five, Chronicles' two — and DEUTERONOMY NEVER SAYS IT (4:41-43 and 19 have the cities and the fleeing
# without the word); "forty-two cities" one seat; "FORTY-EIGHT" at four seats — this, Joshua 21:41's tally, and two of Nehemiah's census — and
# JOSHUA 21's FOUR LOTS SUM TO IT: 13 + 10 + 13 + 12 = 48 by the parser; the Levites 22,000 at 3:39 and 23,000 at 26:62 for forty-eight cities;
# "THE CITY OF REFUGE FOR THE SLAYER" at five of Joshua 21's six (Hebron, Shechem, Golan, Kedesh, Ramoth) — BEZER'S ROW (21:36) LACKS THE
# PHRASE; "them and their pasture-lands" one seat; THE PROPORTIONAL RULE 35:8 IS THE SECOND CENSUS'S — "from the many you shall take more,
# from the few less" with 26:54's and 33:54's two verbs ("you shall take more" at 33:54 and this in the Torah; "you shall take less" here alone,
# its singular at Leviticus 25:16, 26:54, 33:54), "each according to his inheritance" one seat (26:54 said "according to his numbered").
assert phrase(['צו', 'את', 'בני', 'ישראל']) == ['Lev 24:2', 'Num 28:2', 'Num 34:2', 'Num 35:2', 'Num 5:2'] and phrase(['ונתנו', 'ללוים'], None) == ['Num 35:2'] and phrase(['מנחלת', 'אחזתם'], None) == ['Num 35:2'] and phrase(['ערים', 'לשבת'], None) == ['Josh 14:4', 'Josh 21:2', 'Num 35:2']
assert words('Josh', 21, 2) == ['וידברו', 'אליהם', 'בשלה', 'בארץ', 'כנען', 'לאמר', 'יהוה', 'צוה', 'ביד', 'משה', 'לתת', 'לנו', 'ערים', 'לשבת', 'ומגרשיהן', 'לבהמתנו'] and words('Josh', 21, 3) == ['ויתנו', 'בני', 'ישראל', 'ללוים', 'מנחלתם', 'אל', 'פי', 'יהוה', 'את', 'הערים', 'האלה', 'ואת', 'מגרשיהן']
assert LEMV('4054', T) == ['Lev 25:34', 'Num 35:2', 'Num 35:3', 'Num 35:4', 'Num 35:5', 'Num 35:7'] and len(LEMV('4054')) == 69 and len(LEMT('4054')) == 115 and len([s for s in LEMV('4054') if s.startswith('Josh 21')]) == 32 and words('Lev', 25, 34) == ['ושדה', 'מגרש', 'עריהם', 'לא', 'ימכר', 'כי', 'אחזת', 'עולם', 'הוא', 'להם']
assert phrase(['לבהמתם', 'ולרכשם'], None) == ['Num 35:3'] and U('חיתם') == ['Ezek 7:13', 'Num 35:3'] and aramaic(35, 3)[-2:] == ['ולכל', 'חיותהון']
assert phrase(['מקיר', 'העיר', 'וחוצה'], None) == ['Num 35:4'] and phrase(['אלף', 'אמה'], None) == ['Num 35:4'] and phrase(['אלפים', 'באמה'], None) == ['Num 35:5'] and cnt_in(lambda x, m: x == 'אלפים') == 4 and phrase(['כאלפים', 'אמה'], None) == ['Josh 3:4'] and seats_in(lambda x, m: x == 'סביב') == [(4, 'סביב')]
assert LEMV('4058', T) == ['Deut 21:2', 'Exod 16:18', 'Num 35:5'] and words('Deut', 21, 2)[:4] == ['ויצאו', 'זקניך', 'ושפטיך', 'ומדדו'] and words('Exod', 16, 18)[:2] == ['וימדו', 'בעמר']
assert [x for x in words('Num', 35, 5) if x in ('קדמה', 'נגב', 'ים', 'צפון')] == ['קדמה', 'נגב', 'ים', 'צפון'] and [(v, x) for v in (3, 10, 18, 25) for x in words('Num', 2, v) if x in ('קדמה', 'תימנה', 'ימה', 'צפנה')] == [(3, 'קדמה'), (10, 'תימנה'), (18, 'ימה'), (25, 'צפנה')] and [(v, x) for v in range(9, 14) for x in words('Exod', 27, v) if x in ('נגב', 'צפון', 'ים', 'קדמה')] == [(9, 'נגב'), (11, 'צפון'), (12, 'ים'), (13, 'קדמה')]
assert phrase(['והעיר', 'בתוך'], None) == ['Num 35:5'] and phrase(['זה', 'יהיה', 'להם'], None) == ['Num 35:5'] and phrase(['מגרשי', 'הערים'], None) == ['Num 35:5']
assert phrase(['שש', 'ערי', 'המקלט'], None) == ['Num 35:6'] and phrase(['ערי', 'מקלט'], None) == ['Num 35:11', 'Num 35:13', 'Num 35:14'] and phrase(['ערי', 'המקלט'], None) == ['1Chr 6:42', '1Chr 6:52', 'Josh 20:2', 'Num 35:6'] and phrase(['עיר', 'מקלטו'], None) == ['Num 35:25', 'Num 35:26', 'Num 35:27', 'Num 35:32'] and cnt_in(lambda x, m: x == 'מקלטו') == 5
MQ = sorted({f'{b} {c}:{v}' for (b, c, v), ws in by.items() for x, _ in ws if 'מקלט' in x})
assert len(MQ) == 20 and sum(1 for (b, c, v), ws in by.items() for x, _ in ws if 'מקלט' in x) == 20 and [s for s in MQ if s.startswith('Deut')] == [] and cnt_in(lambda x, m: 'מקלט' in x) == 11 and [s for s in MQ if not s.startswith('Num')] == ['1Chr 6:42', '1Chr 6:52', 'Josh 20:2', 'Josh 20:3', 'Josh 21:13', 'Josh 21:21', 'Josh 21:27', 'Josh 21:32', 'Josh 21:38']
assert phrase(['ארבעים', 'ושתים', 'עיר'], None) == ['Num 35:6'] and phrase(['ארבעים', 'ושמנה'], None) == ['Josh 21:41', 'Neh 7:15', 'Neh 7:44', 'Num 35:7'] and words('Josh', 21, 41) == ['כל', 'ערי', 'הלוים', 'בתוך', 'אחזת', 'בני', 'ישראל', 'ערים', 'ארבעים', 'ושמנה', 'ומגרשיהן'] and sum(N('Josh', 21, v)[0] for v in (4, 5, 6, 7)) == 48
assert phrase(['את', 'עיר', 'מקלט', 'הרצח'], None) == ['Josh 21:13', 'Josh 21:21', 'Josh 21:27', 'Josh 21:32', 'Josh 21:38'] and words('Josh', 21, 36) == ['וממטה', 'ראובן', 'את', 'בצר', 'ואת', 'מגרשה', 'ואת', 'יהצה', 'ואת', 'מגרשה'] and phrase(['אתהן', 'ואת', 'מגרשיהן'], None) == ['Num 35:7']
assert words('Num', 26, 54) == ['לרב', 'תרבה', 'נחלתו', 'ולמעט', 'תמעיט', 'נחלתו', 'איש', 'לפי', 'פקדיו', 'יתן', 'נחלתו'] and words('Num', 33, 54)[5:13] == ['לרב', 'תרבו', 'את', 'נחלתו', 'ולמעט', 'תמעיט', 'את', 'נחלתו'] and U('תרבו', books=T) == ['Num 33:54', 'Num 35:8'] and U('תמעיטו') == ['Num 35:8'] and U('תמעיט') == ['Lev 25:16', 'Num 26:54', 'Num 33:54'] and phrase(['מאת', 'הרב'], None) == ['Num 35:8'] and phrase(['איש', 'כפי', 'נחלתו'], None) == ['Num 35:8'] and U('מעריו') == ['Ezek 25:9', 'Num 35:8']

# 35:9-15 THE REFUGE LAW (computed): "WHEN YOU ARE CROSSING THE JORDAN" the participle's three seats — 33:51 "to the land of Canaan", this
# "to Canaan-ward" (the directional ending: "to the land of Canaan" so spelled at seven Bible seats, six Genesis's — Abram's, Jacob's, the
# brothers' — and this, the Torah's last), Deuteronomy 11:31; "YOU SHALL APPOINT" (literally cause to happen) one seat — THE VERB OF BALAAM'S
# MEETINGS ("and God MET Balaam", 23:4, 16, the same root's causative) and of Abraham's servant's prayer ("cause it to happen before me", Genesis
# 24:12; 27:20) — the Sifrei "calling out connotes designation", ONKELOS "you shall prepare"; "cities, cities of refuge" the apposition one
# seat; "A SLAYER WHO SMITES A SOUL UNWITTINGLY" — "smites a soul unwittingly" four seats (35:11, 15; Joshua 20:3, 9), "whoever smites a soul"
# three (35:15, 30; Joshua 20:9 quoting), "smites a soul" five in the Bible, all Numbers 35's and Joshua 20's; "UNWITTINGLY" thirteen seats —
# the sin offering's word (Leviticus 4-5, 22:14; Numbers 15:26-29) and the slayer's, Joshua 20's two; DEUTERONOMY SAYS "WITHOUT KNOWLEDGE"
# instead (4:42, 19:4) and JOSHUA 20:3 SAYS BOTH; "for refuge from the avenger" — the bare "avenger" without "blood" at 35:12 and Joshua 20:3
# (ONKELOS supplies "of blood"; Malachi's "polluted" wears the consonants at 1:7, 12 — another root by the morphology); "UNTIL HE STANDS BEFORE
# THE CONGREGATION FOR JUDGMENT" two seats — this and Joshua 20:6 quoting; "three cities" — Deuteronomy's phrase (4:41, 19:7, 9; and 19:2's
# PLENE "three", one of the plene form's three Torah seats, 7b's rule) — "the three cities" with the article here alone; "the stranger and the
# sojourner" — Abraham's pair at Machpelah (Genesis 23:4) and Leviticus 25's (35, 47); JOSHUA 20:9 KEEPS THE STRANGER AND DROPS THE SOJOURNER;
# "these six cities" one seat; "TO FLEE THERE" five seats — LOT'S FIRST ("let me flee there", Genesis 19:20, Zoar the little city), Deuteronomy
# 19:3, this, Joshua 20:3, 9; "he fled there" one (35:25), "he shall flee there" three — EXODUS 21:13 THE SPEC'S FIRST SEAT ("I will appoint
# you a PLACE to which he shall flee": the place become cities), Deuteronomy 19:4, 35:26.
assert phrase(['כי', 'אתם', 'עברים', 'את', 'הירדן'], None) == ['Deut 11:31', 'Num 33:51', 'Num 35:10'] and words('Num', 33, 51)[-3:] == ['אל', 'ארץ', 'כנען'] and words('Num', 35, 10)[-2:] == ['ארצה', 'כנען'] and phrase(['ארצה', 'כנען'], None) == ['Gen 11:31', 'Gen 12:5', 'Gen 31:18', 'Gen 42:29', 'Gen 45:17', 'Gen 50:13', 'Num 35:10']
assert U('והקריתם') == ['Num 35:11'] and words('Num', 23, 4)[:3] == ['ויקר', 'אלהים', 'אל'] and words('Num', 23, 16)[:2] == ['ויקר', 'יהוה'] and words('Gen', 24, 12)[5:8] == ['הקרה', 'נא', 'לפני'] and words('Gen', 27, 20)[-5:-1] == ['כי', 'הקרה', 'יהוה', 'אלהיך'] and aramaic(35, 11)[0] == 'ותזמנון'
assert phrase(['ערים', 'ערי', 'מקלט'], None) == ['Num 35:11'] and phrase(['ונס', 'שמה', 'רצח'], None) == ['Num 35:11'] and phrase(['מכה', 'נפש', 'בשגגה'], None) == ['Josh 20:3', 'Josh 20:9', 'Num 35:11', 'Num 35:15'] and phrase(['כל', 'מכה', 'נפש'], None) == ['Josh 20:9', 'Num 35:15', 'Num 35:30'] and phrase(['מכה', 'נפש'], None) == ['Josh 20:3', 'Josh 20:9', 'Num 35:11', 'Num 35:15', 'Num 35:30'] and phrase(['ומכה', 'נפש'], None) == ['Lev 24:18'] and phrase(['והכהו', 'נפש'], None) == ['Deut 19:11', 'Deut 19:6']
assert U('בשגגה') == ['Josh 20:3', 'Josh 20:9', 'Lev 22:14', 'Lev 4:2', 'Lev 4:22', 'Lev 4:27', 'Lev 5:15', 'Num 15:26', 'Num 15:27', 'Num 15:28', 'Num 15:29', 'Num 35:11', 'Num 35:15'] and phrase(['בבלי', 'דעת'], None) == ['Deut 19:4', 'Deut 4:42', 'Job 35:16', 'Josh 20:3', 'Josh 20:5'] and words('Josh', 20, 3)[2:8] == ['רוצח', 'מכה', 'נפש', 'בשגגה', 'בבלי', 'דעת']
assert phrase(['למקלט', 'מגאל'], None) == ['Josh 20:3', 'Num 35:12'] and U('מגאל') == ['Josh 20:3', 'Mal 1:12', 'Mal 1:7', 'Num 35:12'] and [(m, l) for (x, m), l in zip(by[('Mal', 1, 7)], byl[('Mal', 1, 7)]) if x == 'מגאל'] == [('HVPsmsa', '1351')] and [l for (x, m), l in zip(by[('Num', 35, 12)], byl[('Num', 35, 12)]) if x == 'מגאל'] == ['1350 a'] and aramaic(35, 12)[4:6] == ['מגאל', 'דמא']
assert phrase(['עד', 'עמדו', 'לפני', 'העדה', 'למשפט'], None) == ['Josh 20:6', 'Num 35:12'] and phrase(['לפני', 'העדה'], None) == ['Josh 20:6', 'Josh 20:9', 'Num 16:9', 'Num 35:12']
assert phrase(['שש', 'ערי', 'מקלט', 'תהיינה', 'לכם'], None) == ['Num 35:13'] and phrase(['שלש', 'הערים'], None) == ['Num 35:14'] and phrase(['שלש', 'ערים'], None) == ['Amos 4:8', 'Deut 19:7', 'Deut 19:9', 'Deut 4:41'] and words('Deut', 19, 2)[:2] == ['שלוש', 'ערים'] and U('שלוש', books=T) == ['Deut 16:16', 'Deut 19:2', 'Num 22:32'] and len(U('שלוש')) == 24
assert phrase(['ולגר', 'ולתושב'], None) == ['Num 35:15'] and phrase(['גר', 'ותושב'], None) == ['Gen 23:4', 'Lev 25:35', 'Lev 25:47'] and words('Josh', 20, 9)[7:10] == ['ולגר', 'הגר', 'בתוכם'] and phrase(['שש', 'הערים', 'האלה'], None) == ['Num 35:15'] and phrase(['למקלט', 'לנוס', 'שמה'], None) == ['Num 35:15']
assert phrase(['לנוס', 'שמה'], None) == ['Deut 19:3', 'Gen 19:20', 'Josh 20:3', 'Josh 20:9', 'Num 35:15'] and phrase(['נס', 'שמה'], None) == ['Num 35:25'] and phrase(['ינוס', 'שמה'], None) == ['Deut 19:4', 'Exod 21:13', 'Num 35:26'] and words('Exod', 21, 13) == ['ואשר', 'לא', 'צדה', 'והאלהים', 'אנה', 'לידו', 'ושמתי', 'לך', 'מקום', 'אשר', 'ינוס', 'שמה'] and 'לנוס' in words('Gen', 19, 20)

# 35:16-21 THE THREE INSTRUMENTS AND THE AVENGER (computed): "with an instrument of iron" one seat; "a stone of the hand" one, "a wooden
# instrument of the hand" one; "whereby he may die" at the stone (17), the wood (18) and the unseen stone (23) — NOT at the iron: the iron
# verse is the shortest of the three (ten tokens against thirteen and fourteen), with no "hand" and no size clause (the Sifrei 160:3 reads the
# omission: iron of any size kills — "even a needle"); ONKELOS SUPPLIES THE SIZE CLAUSE at 17 and 18 ("a stone that is taken in the hand,
# sufficient that he die by it"); "HE IS A MURDERER, THE MURDERER SHALL SURELY DIE" the formula's three seats (16, 17, 18) and "the smiter
# shall surely die, he is a murderer" at 21; "SHALL SURELY DIE" twenty-two Torah seats (twenty-four in the Bible) — FIVE IN THIS CHAPTER (16,
# 17, 18, 21, 31), THE TORAH'S DENSEST; THE MURDER-ROOT — twenty-eight Torah tokens, TWENTY IN THIS CHAPTER (twelve "the slayer" with the
# article, six bare participles, "and he murders" at 27, "shall slay" at 30 — ONE ROOT FOR FOUR AGENTS: the murderer, the manslayer, the
# avenger's kill and the court's execution), the others the sixth commandment's two (Exodus 20:13, Deuteronomy 5:17), Deuteronomy 4:42's two,
# 19:3, 4, 6 and 22:26's; forty-seven tokens in forty Bible verses; WRITTEN DEFECTIVE AT EVERY NUMBERS SEAT — the plene "murderer" stands at
# Deuteronomy 4:42, Joshua 20:3, 6 and Job 24:14 alone; "THE AVENGER OF BLOOD" ten Bible seats — this chapter's five verses (seven tokens),
# Deuteronomy 19:6, 12, Joshua 20:5, 9, and the woman of Tekoa's plea (2 Samuel 14:11); ONKELOS "the avenger of blood" six seats (35:12's bare
# "avenger" supplied) and A CLAUSE OF ITS OWN at 19 and 21 — "when he has been found guilty by the court" — the translation putting the court
# before the avenger's hand; "when he meets him" two seats (19, 21); "in hatred he thrust him" — the thrust-root's eleven Bible tokens, four the
# Torah's (Deuteronomy 6:19, 9:4 the nations thrust out; 35:20, 22); "IN LYING-IN-WAIT" the noun's TWO Bible seats, both here (20, 22) — the verb
# at EXODUS 21:13 ("he lay not in wait") and David's (1 Samuel 24:12); the provisions-word wears its consonants at five seats; "threw at him"
# two; "IN ENMITY" — THE SERPENT'S WORD: the enmity-noun's three Torah seats are Genesis 3:15's and this chapter's two (21, 22), Ezekiel's two
# the Bible's others; "struck him with his hand" one; "THE SMITER" as the participle with the article — the quarrel's striker (Exodus 21:19),
# Hadad who smote Midian (Genesis 36:35), David's plea (2 Samuel 24:17) and this chapter's two (21, 24); the same consonants are "THE SMITTEN"
# woman at 25:14, 15, 18 (the passive by the morphology) and "the blow" in Samuel and Kings (another lemma); "struck him" five Torah seats —
# this chapter's four and DEUTERONOMY 21:1's "it is not known who struck him" (the heifer's).
assert phrase(['בכלי', 'ברזל'], None) == ['Num 35:16'] and phrase(['כלי', 'ברזל'], None) == ['1Kgs 6:7'] and phrase(['באבן', 'יד'], None) == ['Num 35:17'] and phrase(['בכלי', 'עץ'], None) == ['Num 35:18'] and phrase(['אשר', 'ימות', 'בה'], None) == ['Num 35:17', 'Num 35:23'] and phrase(['אשר', 'ימות', 'בו'], None) == ['2Kgs 13:14', 'Num 35:18'] and [len(words('Num', 35, v)) for v in (16, 17, 18)] == [10, 13, 14] and 'יד' not in words('Num', 35, 16)
assert aramaic(35, 17)[1:8] == ['באבנא', 'דמתנסבא', 'בידא', 'דהיא', 'כמסת', 'די', 'ימות'] and aramaic(35, 18)[1:9] == ['במאן', 'דעא', 'דמתנסב', 'בידא', 'דהיא', 'כמסת', 'די', 'ימות'] and onk_tok('כמסת') == [(7, 5), (7, 7), (7, 8), (35, 17), (35, 18), (35, 23)]
assert phrase(['רצח', 'הוא', 'מות', 'יומת', 'הרצח'], None) == ['Num 35:16', 'Num 35:17', 'Num 35:18'] and phrase(['מות', 'יומת', 'המכה'], None) == ['Num 35:21'] and len(phrase(['מות', 'יומת'])) == 22 and len(phrase(['מות', 'יומת'], None)) == 24 and [v for v in range(1, NV + 1) if f'Num 35:{v}' in phrase(['מות', 'יומת'])] == [16, 17, 18, 21, 31] and max(Counter(s.rsplit(':', 1)[0] for s in phrase(['מות', 'יומת'])).values()) == 5
RZ = LEMT('7523', T)
assert len(RZ) == 28 and len([t for t in RZ if t[0].startswith('Num 35')]) == 20 and len(LEMT('7523')) == 47 and len(LEMV('7523')) == 40 and sorted({s for s, _, _ in RZ if not s.startswith('Num')}) == ['Deut 19:3', 'Deut 19:4', 'Deut 19:6', 'Deut 22:26', 'Deut 4:42', 'Deut 5:17', 'Exod 20:13']
assert cnt_in(lambda x, m: x == 'הרצח') == 12 and cnt_in(lambda x, m: x == 'רצח') == 6 and seats_in(lambda x, m: x in ('ורצח', 'ירצח')) == [(27, 'ורצח'), (30, 'ירצח')] and [t for t in LEMT('7523') if 'רוצח' in t[1]] == [('Deut 4:42', 'רוצח', 'HVqrmsa'), ('Job 24:14', 'רוצח', 'HVqrmsa'), ('Josh 20:3', 'רוצח', 'HVqrmsa'), ('Josh 20:6', 'הרוצח', 'HTd/Vqrmsa')] and all('רוצח' not in x for (c, v) in SPAN for x in words('Num', 35, v))
assert words('Exod', 20, 13) == ['לא', 'תרצח'] and words('Deut', 5, 17) == ['לא', 'תרצח'] and U('ירצח') == ['Deut 4:42', 'Num 35:30'] and U('ורצח') == ['Hos 4:2', 'Num 35:27']
assert phrase(['גאל', 'הדם'], None) == ['2Sam 14:11', 'Deut 19:12', 'Deut 19:6', 'Josh 20:5', 'Josh 20:9', 'Num 35:19', 'Num 35:21', 'Num 35:24', 'Num 35:25', 'Num 35:27'] and cnt_in(lambda x, m: x == 'גאל') == 6 and onk_seats('גאל דמא') == [(35, 12), (35, 19), (35, 21), (35, 24), (35, 25), (35, 27)] and onk_seats('כד אתחיב ליה מן דינא') == [(35, 19), (35, 21)] and aramaic(35, 19) == ['גאל', 'דמא', 'הוא', 'יקטול', 'ית', 'קטולא', 'כד', 'אתחיב', 'ליה', 'מן', 'דינא', 'הוא', 'יקטלניה']
assert phrase(['בפגעו', 'בו'], None) == ['Num 35:19', 'Num 35:21'] and phrase(['הוא', 'ימיתנו'], None) == ['Num 35:19'] and U('בשנאה') == ['Ezek 23:29', 'Num 35:20'] and len(LEMT('1920')) == 11 and LEMV('1920', T) == ['Deut 6:19', 'Deut 9:4', 'Num 35:20', 'Num 35:22']
assert U('בצדיה', 'צדיה') == ['Num 35:20', 'Num 35:22'] and [l for (x, m), l in zip(by[('Num', 35, 20)], byl[('Num', 35, 20)]) if x == 'בצדיה'] == ['6660'] and [(s, l) for (b, c, v), ws in by.items() for (x, m), l in zip(ws, byl[(b, c, v)]) if x == 'צדה' for s in [f'{b} {c}:{v}']] == [('1Sam 20:20', '6654'), ('1Sam 24:12', '6658 a'), ('Exod 12:39', '6720'), ('Exod 21:13', '6658 a'), ('Gen 42:25', '6720'), ('Gen 45:21', '6720'), ('Judg 7:8', '6720'), ('Judg 20:10', '6720')]
assert phrase(['השליך', 'עליו'], None) == ['Num 35:20', 'Num 35:22'] and LEMT('342') == [('Ezek 25:15', 'איבת', 'HNcfsc'), ('Ezek 35:5', 'איבת', 'HNcfsc'), ('Gen 3:15', 'ואיבה', 'HC/Ncfsa'), ('Num 35:21', 'באיבה', 'HR/Ncfsa'), ('Num 35:22', 'איבה', 'HNcfsa')] and words('Gen', 3, 15)[:3] == ['ואיבה', 'אשית', 'בינך'] and phrase(['הכהו', 'בידו'], None) == ['Num 35:21']
MK = [(s, m, l) for (b, c, v), ws in by.items() for (x, m), l in zip(ws, byl[(b, c, v)]) if x == 'המכה' for s in [f'{b} {c}:{v}']]
assert MK == [('1Chr 1:46', 'HTd/Vhrmsa', '5221'), ('1Kgs 22:35', 'HTd/Ncfsa', '4347'), ('1Sam 4:10', 'HTd/Ncfsa', '4347'), ('1Sam 14:14', 'HTd/Ncfsa', '4347'), ('2Sam 24:17', 'HTd/Vhrmsa', '5221'), ('Exod 21:19', 'HTd/Vhrmsa', '5221'), ('Gen 36:35', 'HTd/Vhrmsa', '5221'), ('Num 25:14', 'HTd/VHsmsa', '5221'), ('Num 25:15', 'HTd/VHsfsa', '5221'), ('Num 25:18', 'HTd/VHsfsa', '5221'), ('Num 35:21', 'HTd/Vhrmsa', '5221'), ('Num 35:24', 'HTd/Vhrmsa', '5221')]
assert U('הכהו', books=T) == ['Deut 21:1', 'Num 35:16', 'Num 35:17', 'Num 35:18', 'Num 35:21'] and words('Deut', 21, 1)[-4:] == ['לא', 'נודע', 'מי', 'הכהו']

# 35:22-24 THE UNWITTING AND THE JUDGMENT (computed): "SUDDENLY" — the word's two Bible seats are both this book's: the nazirite's "if one die
# by him very suddenly" (6:9) and this; "without enmity", "without lying-in-wait", "any stone whereby he may die", "WITHOUT SEEING", "and he
# dropped it on him", "and he was not his enemy", "nor seeking his harm" — one seat each; "AND THE CONGREGATION SHALL JUDGE between the smiter
# and the avenger of blood by these judgments" — "these judgments" here and Deuteronomy 7:12; THE CONGREGATION-TOKEN four times in the chapter
# (12, 24, 25, 25) — the Sifrei 160:8's "three written in the section" are the judgment's three (24, 25, 25), the darshan's ten-and-ten-and-three
# (ONKELOS "the assembly" at the same four).
assert U('בפתע') == ['Num 35:22', 'Num 6:9'] and words('Num', 6, 9)[:6] == ['וכי', 'ימות', 'מת', 'עליו', 'בפתע', 'פתאם'] and phrase(['בלא', 'איבה'], None) == ['Num 35:22'] and phrase(['בלא', 'צדיה'], None) == ['Num 35:22'] and phrase(['בכל', 'אבן', 'אשר', 'ימות', 'בה'], None) == ['Num 35:23'] and phrase(['בלא', 'ראות'], None) == ['Num 35:23'] and phrase(['ויפל', 'עליו'], None) == ['Num 35:23'] and phrase(['והוא', 'לא', 'אויב', 'לו'], None) == ['Num 35:23'] and phrase(['מבקש', 'רעתו'], None) == ['Num 35:23']
assert phrase(['ושפטו', 'העדה'], None) == ['Num 35:24'] and phrase(['בין', 'המכה', 'ובין', 'גאל', 'הדם'], None) == ['Num 35:24'] and phrase(['המשפטים', 'האלה'], None) == ['Deut 7:12', 'Num 35:24'] and seats_in(lambda x, m: x == 'העדה') == [(12, 'העדה'), (24, 'העדה'), (25, 'העדה'), (25, 'העדה')] and [(v, aramaic(35, v).count('כנשתא')) for v in range(1, NV + 1) if 'כנשתא' in aramaic(35, v)] == [(12, 1), (24, 1), (25, 2)]

# 35:25-28 THE TERM (computed): "the congregation shall deliver", "from the hand of the avenger of blood", "the congregation shall return him",
# "to his city of refuge where he fled" — one seat each; "UNTIL THE DEATH OF THE HIGH PRIEST" — 35:25, 28, and Joshua 20:6 quoting it PLENE;
# THE HIGH PRIEST WRITTEN DEFECTIVE ONLY HERE — "the great priest" without the vav at 35:25 and 35:28 (twice), the Bible's only such seats;
# plene at sixteen (Joshua 20:6, Kings, Chronicles, Haggai, Zechariah, Nehemiah) and "and the high priest" at Leviticus 21:10 (the definition
# by the oil poured on his head) and 2 Kings 12:11; "WHO WAS ANOINTED WITH THE HOLY OIL" one seat — the phrase's only, "the anointing oil"
# the tabernacle's nine; ONKELOS "whom he anointed (made great) with the oil of holiness", the verb's one seat in the book; "IF THE SLAYER GOING
# OUT GOES OUT" — the doubled infinitive's two seats, Jacob's going out from Isaac (Genesis 27:30) and this; the chapter's SIX doubled
# infinitives (the five "surely die" and this); "the border of his city of refuge", "outside the border", "and the avenger finds him" — one
# each; "HE HAS NO BLOOD" — THE BURGLAR'S ACQUITTAL (Exodus 22:1 "there is no blood for him", the plural; 22:2 "he has blood") at its second
# seat, the singular; ONKELOS "he has no blood"; "for in his city of refuge he shall dwell", "and after the death of the high priest the slayer
# shall return to the land of his possession" — "the land of his possession" the phrase's one seat (the family six); JOSHUA 20:6 ADDS "and
# come to his city and to his house".
assert phrase(['והצילו', 'העדה'], None) == ['Num 35:25'] and phrase(['מיד', 'גאל', 'הדם'], None) == ['Num 35:25'] and phrase(['והשיבו', 'אתו', 'העדה'], None) == ['Num 35:25'] and phrase(['אל', 'עיר', 'מקלטו', 'אשר', 'נס', 'שמה'], None) == ['Num 35:25']
assert phrase(['עד', 'מות', 'הכהן', 'הגדל'], None) == ['Num 35:25', 'Num 35:28'] and phrase(['עד', 'מות', 'הכהן', 'הגדול'], None) == ['Josh 20:6'] and phrase(['עד', 'מות', 'הכהן'], None) == ['Josh 20:6', 'Num 35:25', 'Num 35:28', 'Num 35:32'] and phrase(['הכהן', 'הגדל'], None) == ['Num 35:25', 'Num 35:28'] and cnt_in(lambda x, m: x == 'הגדל') == 3 and len(phrase(['הכהן', 'הגדול'], None)) == 16 and phrase(['והכהן', 'הגדול'], None) == ['2Kgs 12:11', 'Lev 21:10']
assert PT('Num', 35, 25, 'הגדל') == ['הַגָּדֹל'] and PT('Lev', 21, 10, 'הגדול') == ['הַגָּדוֹל'] and words('Lev', 21, 10)[:9] == ['והכהן', 'הגדול', 'מאחיו', 'אשר', 'יוצק', 'על', 'ראשו', 'שמן', 'המשחה'] and U('הגדל', books=T) == ['Deut 10:17', 'Deut 11:7', 'Deut 1:7', 'Deut 2:7', 'Deut 4:37', 'Deut 8:15', 'Deut 9:29', 'Exod 18:22', 'Exod 3:3', 'Gen 15:18', 'Gen 1:16', 'Gen 27:1', 'Gen 27:15', 'Gen 27:42', 'Num 34:7', 'Num 35:25', 'Num 35:28']
assert phrase(['אשר', 'משח', 'אתו', 'בשמן', 'הקדש'], None) == ['Num 35:25'] and phrase(['בשמן', 'הקדש'], None) == ['Num 35:25'] and phrase(['שמן', 'הקדש'], None) == [] and len(phrase(['שמן', 'המשחה'])) == 9 and aramaic(35, 25)[-7:] == ['כהנא', 'רבא', 'די', 'רבי', 'יתיה', 'במשח', 'קודשא'] and onk_tok('רבי') == [(35, 25)]
assert phrase(['ואם', 'יצא', 'יצא'], None) == ['Num 35:26'] and phrase(['יצא', 'יצא'], None) == ['Gen 27:30', 'Num 35:26'] and [(v, x, y) for v in range(1, NV + 1) for (x, m), (y, n) in zip(wm('Num', 35, v), wm('Num', 35, v)[1:]) if m and 'Vqa' in m] == [(16, 'מות', 'יומת'), (17, 'מות', 'יומת'), (18, 'מות', 'יומת'), (21, 'מות', 'יומת'), (26, 'יצא', 'יצא'), (31, 'מות', 'יומת')] and PT('Num', 35, 26, 'יצא') == ['יָצֹא', 'יֵצֵא']
assert phrase(['גבול', 'עיר', 'מקלטו'], None) == ['Num 35:26'] and phrase(['מחוץ', 'לגבול'], None) == ['Num 35:27'] and phrase(['ומצא', 'אתו', 'גאל', 'הדם'], None) == ['Num 35:27'] and phrase(['אין', 'לו', 'דם'], None) == ['Num 35:27'] and phrase(['אין', 'לו', 'דמים'], None) == ['Exod 22:1'] and phrase(['דמים', 'לו'], None) == ['Exod 22:2'] and words('Exod', 22, 1) == ['אם', 'במחתרת', 'ימצא', 'הגנב', 'והכה', 'ומת', 'אין', 'לו', 'דמים'] and aramaic(35, 27)[-4:] == ['קטולא', 'לית', 'ליה', 'דמא']
assert phrase(['כי', 'בעיר', 'מקלטו', 'ישב'], None) == ['Num 35:28'] and phrase(['ואחרי', 'מות', 'הכהן', 'הגדל'], None) == ['Num 35:28'] and phrase(['ישוב', 'הרצח'], None) == ['Num 35:28'] and phrase(['ארץ', 'אחזתו'], None) == ['Num 35:28'] and sorted(set(phrase(['ארץ', 'אחזתו'], None) + phrase(['ארץ', 'אחזתם'], None) + phrase(['ארץ', 'אחזתכם'], None))) == ['Josh 22:19', 'Josh 22:4', 'Josh 22:9', 'Lev 14:34', 'Lev 25:24', 'Num 35:28'] and words('Josh', 20, 6)[-12:-5] == ['ישוב', 'הרוצח', 'ובא', 'אל', 'עירו', 'ואל', 'ביתו']

# 35:29-32 THE STATUTE, THE WITNESSES, THE RANSOM (computed): "A STATUTE OF JUDGMENT" — the phrase's two seats in the Bible: THE DAUGHTERS'
# INHERITANCE (27:11) and this (the Sifrei 134:3 and 161:1 read both "for the generations"); "for your generations in all your dwellings" —
# LEVITICUS 3:17's, THE BLOOD BAN'S FORMULA ("you shall eat no fat and no blood"), at its second seat; "in all your dwellings" six seats
# (Exodus 12:20's leaven, Leviticus 3:17, 7:26 the blood again, 23:3, 21, this); "WHOEVER SMITES A SOUL, BY THE MOUTH OF WITNESSES" — the
# bare plural "witnesses" with no number one seat (Deuteronomy says "two witnesses or three", 17:6, 19:15 — the Sifrei's prototype: "witness"
# means two unless "one" is written); "AND ONE WITNESS" one seat — and "ONE WITNESS" A HOMOGRAPH: the consonants say "not even one" of
# Egypt's cattle (Exodus 9:7) and of the drowned (14:28), "until one" at Judges 4:16 and 2 Samuel 17:22 (the preposition), and "one witness"
# at Deuteronomy 17:6 and 19:15 (the noun) — the lemmas decide; INSIDE THE CHAPTER the same consonants are "UNTIL" four times (12, 25, 28, 32
# — the fugitive's term) and "witness" twice (30); "SHALL NOT TESTIFY" — THE NINTH COMMANDMENT'S VERB ("you shall not answer against your
# neighbor a false witness", Exodus 20:16; Deuteronomy 5:20; 19:18's false witness) beside THE SIXTH'S ROOT ("shall slay") in one verse —
# 35:30 carries the two commandments' verbs; the bare "he shall answer" elsewhere in the Torah Joseph's ("God shall answer the peace of
# Pharaoh", Genesis 41:16), the store glossing it "eye"; "YOU SHALL NOT TAKE RANSOM" twice — THE RANSOM-NOUN's four Torah seats: THE GORING
# OX'S (Exodus 21:30 "if a ransom be laid on him" — the Sifrei 161:1's contrast: death at Heaven's hand is ransomed, death by the court is
# not), THE HALF-SHEKEL'S ("a ransom for his soul", Exodus 30:12), and this chapter's two; "for the life of a murderer", "who is wicked to
# die" one seat each (Deuteronomy 25:2's "the wicked one deserving of stripes" the kin; "a son of death" Saul's and David's); "for he shall
# surely die" with "for" one seat; "to flee to his city of refuge", "to return to dwell in the land" one each; "UNTIL THE DEATH OF THE PRIEST"
# at 35:32 WITHOUT "GREAT" — the one bare seat of the term; ONKELOS "money" for the ransom at both seats (the word's only two in the book),
# "guilty" for "wicked".
assert phrase(['לחקת', 'משפט'], None) == ['Num 27:11', 'Num 35:29'] and words('Num', 27, 11)[-9:-5] == ['לבני', 'ישראל', 'לחקת', 'משפט'] and phrase(['לדרתיכם', 'בכל', 'מושבתיכם'], None) == ['Lev 3:17', 'Num 35:29'] and phrase(['בכל', 'מושבתיכם'], None) == ['Exod 12:20', 'Lev 23:21', 'Lev 23:3', 'Lev 3:17', 'Lev 7:26', 'Num 35:29'] and words('Lev', 3, 17)[:7] == ['חקת', 'עולם', 'לדרתיכם', 'בכל', 'מושבתיכם', 'כל', 'חלב']
assert phrase(['כל', 'מכה', 'נפש', 'לפי', 'עדים'], None) == ['Num 35:30'] and phrase(['לפי', 'עדים'], None) == ['Num 35:30'] and phrase(['על', 'פי', 'שנים', 'עדים'], None) == ['Deut 17:6'] and phrase(['על', 'פי', 'שני', 'עדים'], None) == ['Deut 19:15'] and phrase(['ועד', 'אחד'], None) == ['Num 35:30']
assert [(s, [l for (x, m), l in zip(by[(s.split()[0], int(s.split()[1].split(':')[0]), int(s.split()[1].split(':')[1]))], byl[(s.split()[0], int(s.split()[1].split(':')[0]), int(s.split()[1].split(':')[1]))]) if x == 'עד']) for s in phrase(['עד', 'אחד'], None)] == [('2Sam 17:22', ['5704', '5704']), ('Deut 17:6', ['5707']), ('Deut 19:15', ['5707']), ('Exod 14:28', ['5704']), ('Exod 9:7', ['5704']), ('Judg 4:16', ['5704', '5704'])]
assert [(v, x, l) for v in range(1, NV + 1) for (x, m), l in zip(by[('Num', 35, v)], byl[('Num', 35, v)]) if x in ('עד', 'ועד', 'עדים')] == [(12, 'עד', '5704'), (25, 'עד', '5704'), (28, 'עד', '5704'), (30, 'עדים', '5707'), (30, 'ועד', '5707'), (32, 'עד', '5704')]
assert [l for (x, m), l in zip(by[('Num', 35, 30)], byl[('Num', 35, 30)]) if x == 'יענה'] == ['6030 b'] and words('Exod', 20, 16) == ['לא', 'תענה', 'ברעך', 'עד', 'שקר'] and words('Deut', 5, 20) == ['ולא', 'תענה', 'ברעך', 'עד', 'שוא'] and [t for t in words('Deut', 19, 18) if 'ענה' in t] == ['ענה'] and U('יענה', books=T) == ['Gen 41:16', 'Num 35:30'] and phrase(['בנפש', 'למות'], None) == ['Num 35:30'] and aramaic(35, 30)[8:13] == ['וסהיד', 'חד', 'לא', 'יסהד', 'באנש']
assert phrase(['ולא', 'תקחו', 'כפר'], None) == ['Num 35:31', 'Num 35:32'] and [l for (x, m), l in zip(by[('Num', 35, 31)], byl[('Num', 35, 31)]) if x == 'כפר'] == ['3724 a'] and LEMV('3724 a') == ['1Sam 12:3', 'Amos 5:12', 'Exod 21:30', 'Exod 30:12', 'Isa 43:3', 'Job 33:24', 'Job 36:18', 'Num 35:31', 'Num 35:32', 'Prov 13:8', 'Prov 21:18', 'Prov 6:35', 'Ps 49:8'] and words('Exod', 21, 30)[:4] == ['אם', 'כפר', 'יושת', 'עליו'] and words('Exod', 30, 12)[9:12] == ['כפר', 'נפשו', 'ליהוה']
assert phrase(['לנפש', 'רצח'], None) == ['Num 35:31'] and phrase(['רשע', 'למות'], None) == ['Num 35:31'] and words('Deut', 25, 2)[:5] == ['והיה', 'אם', 'בן', 'הכות', 'הרשע'] and phrase(['בן', 'מות'], None) == ['1Sam 20:31', '2Sam 12:5'] and phrase(['כי', 'מות', 'יומת'], None) == ['Num 35:31']
assert phrase(['לנוס', 'אל', 'עיר', 'מקלטו'], None) == ['Num 35:32'] and phrase(['לשוב', 'לשבת', 'בארץ'], None) == ['Num 35:32'] and words('Num', 35, 32)[-3:] == ['עד', 'מות', 'הכהן'] and onk_tok('ממון') == [(35, 31), (35, 32)] and aramaic(35, 31)[:3] == ['ולא', 'תקבלון', 'ממון'] and onk_tok('חיב') == [(35, 31)]

# 35:33-34 THE LAND (computed): "YOU SHALL NOT POLLUTE THE LAND ... FOR THE BLOOD, IT POLLUTES THE LAND" — the pollute-root's eleven Bible
# tokens: THE TORAH'S ONLY SEAT IS THIS VERSE (two tokens, the causative), then Jeremiah's polluted land of harlotry (3:1, 2, 9), Isaiah 24:5,
# Micah 4:11, Daniel 11:32, Jeremiah 23:11's prophets — and PSALM 106:38 "AND THE LAND WAS POLLUTED WITH BLOOD", the verse's verb and its blood
# together (the Sifrei 161:3's R. Yoshiyah splits the verb into two words, "it rests wrath" — the notarikon); "AND FOR THE LAND NO ATONEMENT
# CAN BE MADE" — the passive (pual) one seat: THE ROOT OF THE RANSOM — "ransom" (31, 32) and "be atoned" (33) one root three times: no ransom
# for the murderer, none for the fugitive, no atonement for the land "except by the blood of him who shed it" (Genesis 9:6's "whoso sheds
# man's blood, by man shall his blood be shed"); DEUTERONOMY 21:8's HEIFER SAYS THE OTHER PASSIVE — "and the blood shall be atoned for them"
# (the unknown slayer; the Sifrei: if the slayer is found after the heifer, no atonement — the land's rule wins); ONKELOS SUPPLIES "INNOCENT"
# ("innocent blood", the word's one seat in the book); "YOU SHALL NOT DEFILE THE LAND" — Leviticus 18:25, 27's "and the land was defiled" (the
# forbidden unions) the kin; "IN WHOSE MIDST I DWELL" — THE BOOK'S INCLUSIO: 5:3 "their camp in whose midst I dwell" (the book's first law
# after the census) and 35:34 "the land in whose midst I dwell" (its last law-chapter's close) — the two seats of "I dwell in the midst" in the
# Torah, the Sifrei 1:7 and 161:5 reading each by the other ("beloved are Israel — even unclean, the Presence among them"); "FOR I THE LORD
# DWELL IN THE MIDST OF THE CHILDREN OF ISRAEL" one seat — Exodus 29:45-46's "I will dwell in the midst of the children of Israel" the promise
# (25:8's "that I may dwell in their midst"; 1 Kings 6:13, Zechariah 8:3 the runs); ONKELOS "MY PRESENCE dwells" at both — the word "my
# Shekhinah" at its one seat in the book (5:3's form "my Presence dwells among them").
assert LEMT('2610') == [('Dan 11:32', 'יחניף', 'HVhi3ms'), ('Isa 24:5', 'חנפה', 'HVqp3fs'), ('Jer 3:1', 'חנוף', 'HVqa'), ('Jer 3:1', 'תחנף', 'HVqi3fs'), ('Jer 3:2', 'ותחניפי', 'HC/Vhw2fs'), ('Jer 3:9', 'ותחנף', 'HC/Vqw3fs'), ('Jer 23:11', 'חנפו', 'HVqp3cp'), ('Mic 4:11', 'תחנף', 'HVqi3fs'), ('Num 35:33', 'תחניפו', 'HVhi2mp'), ('Num 35:33', 'יחניף', 'HVhi3ms'), ('Ps 106:38', 'ותחנף', 'HC/Vqw3fs')] and words('Ps', 106, 38)[-3:] == ['ותחנף', 'הארץ', 'בדמים']
assert phrase(['ולא', 'תחניפו', 'את', 'הארץ'], None) == ['Num 35:33'] and phrase(['כי', 'הדם', 'הוא', 'יחניף'], None) == ['Num 35:33'] and phrase(['ולארץ', 'לא', 'יכפר'], None) == ['Num 35:33'] and [(x, m) for x, m in wm('Num', 35, 33) if x == 'יכפר'] == [('יכפר', 'HVPi3ms')] and PT('Num', 35, 33, 'יכפר') == ['יְכֻפַּר']
assert [(v, x, l) for v in range(1, NV + 1) for (x, m), l in zip(by[('Num', 35, v)], byl[('Num', 35, v)]) if 'כפר' in x] == [(31, 'כפר', '3724 a'), (32, 'כפר', '3724 a'), (33, 'יכפר', '3722 a')] and phrase(['לדם', 'אשר', 'שפך', 'בה'], None) == ['Num 35:33'] and phrase(['כי', 'אם', 'בדם', 'שפכו'], None) == ['Num 35:33'] and words('Gen', 9, 6)[:6] == ['שפך', 'דם', 'האדם', 'באדם', 'דמו', 'ישפך']
assert words('Deut', 21, 8)[-3:] == ['ונכפר', 'להם', 'הדם'] and PT('Deut', 21, 8, 'ונכפר') == ['וְנִכַּפֵּר'] and onk_seats('דם זכאי') == [(35, 33)] and aramaic(35, 33)[-8:] == ['על', 'דם', 'זכאי', 'דאתשד', 'בה', 'אלהן', 'בדם', 'אשדיה']
assert phrase(['ולא', 'תטמא', 'את', 'הארץ'], None) == ['Num 35:34'] and phrase(['ותטמא', 'הארץ'], None) == ['Lev 18:25', 'Lev 18:27'] and phrase(['אשר', 'אני', 'שכן', 'בתוכה'], None) == ['Num 35:34'] and phrase(['אני', 'שכן', 'בתוכם'], None) == ['Num 5:3'] and words('Num', 5, 3)[-5:] == ['מחניהם', 'אשר', 'אני', 'שכן', 'בתוכם']
assert phrase(['אני', 'יהוה', 'שכן'], None) == ['Num 35:34'] and phrase(['שכן', 'בתוך', 'בני', 'ישראל'], None) == ['Num 35:34'] and phrase(['ושכנתי', 'בתוך'], None) == ['1Kgs 6:13', 'Exod 29:45', 'Zech 8:3'] and words('Exod', 29, 45)[:4] == ['ושכנתי', 'בתוך', 'בני', 'ישראל'] and words('Exod', 25, 8) == ['ועשו', 'לי', 'מקדש', 'ושכנתי', 'בתוכם']
assert onk_tok('שכינתי') == [(35, 34)] and onk_tok('שריא') == [(5, 3), (16, 3), (35, 34)] and aramaic(35, 34)[8:12] == ['די', 'שכינתי', 'שריא', 'בגוה'] and aramaic(5, 3)[-4:] == ['די', 'שכנתי', 'שריא', 'ביניהון'] and phrase(['ישבים', 'בה'], None) == ['Josh 22:33', 'Num 33:55', 'Num 35:34']

# THE TWIN SPECS ON THE TOKENS: of the refuge law's distinct tokens (35:9-34), Joshua 20:1-9 shares 49 (of its 126 — the run quoting the spec),
# Deuteronomy 19:1-13 38 (of 140), Deuteronomy 21:1-9 18, Deuteronomy 4:41-43 16, Leviticus 24:17-22 12, Exodus 21:12-14 9 (of 27).
S35 = {x for v in range(9, NV + 1) for x in words('Num', 35, v)}
def shared(rng): return len(S35 & {x for b, c, v in rng for x in words(b, c, v)})
assert shared([('Josh', 20, v) for v in range(1, 10)]) == 49 and shared([('Deut', 19, v) for v in range(1, 14)]) == 38 and shared([('Deut', 21, v) for v in range(1, 10)]) == 18 and shared([('Deut', 4, v) for v in (41, 42, 43)]) == 16 and shared([('Lev', 24, v) for v in range(17, 23)]) == 12 and shared([('Exod', 21, v) for v in (12, 13, 14)]) == 9

# ONKELOS OVER THE BOOK (computed on the plain Aramaic of every verse): ONE WORD FOR THE REFUGE — twelve tokens in the chapter for the Hebrew's
# eleven: the twelfth renders "the congregation shall DELIVER him" (35:25) with the refuge-root itself; ONE WORD FOR THE KILLER — seventeen
# "the killer" and one bare "a killer" (35:31) for the Hebrew's twelve "the slayer" and six "a slayer" — the murderer and the manslayer alike,
# as the Hebrew; "the smiter" two (21, 24); "UNWITTINGLY" the sin offering's word (15:27-29) at 35:11, 15; THE BORDER OF THE REFUGE CITY IS
# THE SABBATH-LIMIT'S WORD (techum) at 35:26, 27 — the word Onkelos gave the borders of chapter 34 and Sihon's (21:13) — and 35:5's two thousand
# cubits are the limit's measure (the Sabbath block's ledger names the seats); ONE WORD "SPACE" for the pasture-land (35:2, 4, 5, 7) and for
# the SIDE (34:3, 35:5) — the wind-word; "a decree of judgment" for the statute of judgment at both its seats (27:11, 35:29); "witnesses" and
# "shall testify" for the answer-verb; "in ambush" for lying-in-wait; "suddenly" the nazirite's (6:9), Miriam's (12:4) and this; "in enmity",
# "in hatred"; "when he has been found guilty by the court" supplied at 19 and 21; "innocent blood" supplied at 33; "two thousand" supplied
# four times at 35:5 — THE DUAL READ.
assert sum(1 for v in range(1, NV + 1) for x in aramaic(35, v) if 'שזב' in x) == 12 and aramaic(35, 25)[0] == 'וישזבון' and sum(1 for v in range(1, NV + 1) for x in aramaic(35, v) if x == 'קטולא') == 17 and [(v, x) for v in range(1, NV + 1) for x in aramaic(35, v) if x == 'קטול'] == [(31, 'קטול')] and onk_tok('מחיא') == [(35, 21), (35, 24)]
assert onk_tok('בשלו') == [(15, 27), (15, 28), (15, 29), (35, 11), (35, 15)] and onk_tok('תחום') == [(20, 23), (21, 13), (22, 36), (34, 3), (34, 6), (34, 7), (34, 9), (35, 26)] and onk_tok('לתחום') == [(21, 15), (34, 10), (35, 27)] and onk_tok('רוח') == [(5, 14), (5, 30), (11, 29), (14, 24), (24, 2), (27, 18), (34, 3), (35, 5)] and onk_tok('ורוח') == [(35, 2)] and onk_tok('רוחי') == [(35, 5)] and onk_tok('רוחיהן') == [(35, 7)] and aramaic(35, 4)[0] == 'ורוחי'
assert onk_tok('לגזרת') == [(27, 11), (35, 29)] and onk_tok('סהדין') == [(35, 30)] and onk_tok('יסהד') == [(35, 30)] and onk_tok('בכמנא') == [(35, 20)] and onk_tok('כמן') == [(35, 22)] and onk_tok('בתכף') == [(6, 9), (12, 4), (35, 22)] and onk_tok('בדבבו') == [(35, 21)] and onk_tok('בסנאה') == [(35, 20)] and onk_tok('זכאי') == [(35, 33)]
assert aramaic(35, 5).count('תרין') == 4 and aramaic(35, 5)[4:8] == ['רוח', 'קדומא', 'תרין', 'אלפין'] and aramaic(35, 4)[8:10] == ['אלף', 'אמין'] and onk_tok('אמין') == [(11, 31), (35, 4)] and aramaic(34, 3)[2:4] == ['רוח', 'דרומא'] and [x for x in aramaic(35, 5) if x in ('קדומא', 'דרומא', 'מערבא', 'צפונא')] == ['קדומא', 'דרומא', 'מערבא', 'צפונא']
assert aramaic(35, 28)[5:8] == ['דימות', 'כהנא', 'רבא'] and aramaic(35, 32)[-2:] == ['דימות', 'כהנא'] and aramaic(35, 2) == ['פקד', 'ית', 'בני', 'ישראל', 'ויתנון', 'ללואי', 'מאחסנת', 'אחודתהון', 'קרוין', 'למתב', 'ורוח', 'לקרויא', 'סחרניהון', 'תתנון', 'ללואי']

# THE REGISTER GATE'S SEATS IN THE CHAPTER (measured): register_dispositions.yaml declares NO Num 35 seat, and REGISTER_INDEX.md's two lines on
# the chapter (35:15's six, 35:30's one) are MEASURE-ONLY green — the count lines of 35:4-7 are measures under the unit rule (cubit, city):
# nothing to declare at the reading, nothing to pay at the compile.
RD = open(f'{ROOT}/World/step9/register_dispositions.yaml', encoding='utf-8').read(); RI = open(f'{ROOT}/World/step9/REGISTER_INDEX.md', encoding='utf-8').read()
assert 'Num 35' not in RD and [l.strip()[:40] for l in RI.split('\n') if 'Num 35' in l] == ['Num 35:15   MEASURE-ONLY  green    souls', 'Num 35:30   MEASURE-ONLY  green    souls']

# THE STORE'S GLOSSES READ BACK (the display layer; the frozen unit untouched): "dash-in-pieces" for the murderer (Strong's rendering of the
# root — and the same gloss on another root, "scattered", at three Genesis and Exodus seats: the family is mixed, the rewrite by reference),
# "the-dash-in-pieces" for THE SLAYER (fourteen tokens, every one the word — by gloss), "concretely" for the WITNESS (Strong's "concretely, a
# witness" — seventeen tokens, every one the witness-noun), "be-the-next-of-kin" for the avenger (the redeem-root's twenty-five, Leviticus 25's
# redeemer among them — by reference), "in-mother" for BY THE CUBIT (seventeen, every one a cubit — Og's bed's "by the cubit of a man" too),
# "mother" for the cubit at 35:4 (mixed with the real mothers — by reference), "flit" for FLEE, "in-wink" for SUDDENLY, "in-design" for
# LYING-IN-WAIT, "the-stated-assemblage" for THE CONGREGATION (sixty-five), "and-light-upon" for "you shall appoint" (with Balaam's "and He
# met" — by reference), "and-cardinal-number" for AND EIGHT (the number lost from the gloss), "eye" for "shall testify" (the answer-verb glossed
# as the eye at ten Torah tokens — by reference here, the rest filed), "suburb" for the PASTURE-LAND, "cover" for the RANSOM (the screen's and
# the sparing's word too — by reference), "soil" for POLLUTE, "mouth-in-a-figurative-sense" for THE SIDE (ten, every one — by gloss now, 34:3's
# by-reference row standing), "seas" for the west (by reference), "there-suffix" for THITHER (seventy-two), "in-mistake" for UNWITTINGLY (ten),
# "die" for "the death of" and "shall put to death" (by reference), "strike" for "one who smites", "the-strike" for THE SMITER (with the smitten
# woman's — by reference), "?" for "I", "living-them/their" for THEIR BEASTS, "wrong" for WICKED, "bring-forth" for "goes out", "to-mouth" /
# "like-mouth" for "by the mouth of" / "according to", "set" for GIVE (twelve tokens by reference), the double-hyphen "blood--of-man" family
# (by gloss), "in-impinge-him/its" for WHEN HE MEETS HIM, the "asylum" family for REFUGE, "earth-suffix" for TO THE LAND OF, "hating" for
# ENEMY, "rub-with-oil" for ANOINT, "something-seized" for POSSESSION, "seat-you/your" for YOUR DWELLINGS, "spill-forth" for SHED, "be-foul"
# for DEFILE, "and-snatch-away" / "and-judge" / "and-stretch" for "shall deliver" / "shall judge" / "you shall measure" (the families mixed —
# by reference) — ONE HUNDRED AND TWO rows BY REFERENCE and FIFTY BY GLOSS (each gloss family censused: every token the one word).
assert sg(35, 6, 'הרצח') == 'the-dash-in-pieces' and sg(35, 11, 'רצח') == 'dash-in-pieces' and sg(35, 30, 'עדים') == 'concretely' and sg(35, 30, 'ועד') == 'and-concretely' and sg(35, 19, 'גאל') == 'be-the-next-of-kin' and sg(35, 12, 'מגאל') == 'from-be-the-next-of-kin' and sg(35, 5, 'באמה') == 'in-mother' and sg(35, 4, 'אמה') == 'mother' and sg(35, 6, 'לנס') == 'to-flit' and sg(35, 11, 'ונס') == 'and-flit' and sg(35, 25, 'נס') == 'flit'
assert sg(35, 22, 'בפתע') == 'in-wink' and sg(35, 20, 'בצדיה') == 'in-design' and sg(35, 22, 'צדיה') == 'design' and sg(35, 12, 'העדה') == 'the-stated-assemblage' and sg(35, 11, 'והקריתם') == 'and-light-upon' and sg(35, 7, 'ושמנה') == 'and-cardinal-number' and sg(35, 30, 'יענה') == 'eye' and sg(35, 2, 'ומגרש') == 'and-suburb' and sg(35, 5, 'מגרשי') == 'suburb' and sg(35, 31, 'כפר') == 'cover' and sg(35, 33, 'תחניפו') == 'soil' and sg(35, 5, 'פאת') == 'mouth-in-a-figurative-sense' and sg(35, 5, 'ים') == 'seas' and sg(35, 6, 'שמה') == 'there-suffix' and sg(35, 11, 'בשגגה') == 'in-mistake'
assert sg(35, 25, 'מות') == 'death' and sg(35, 16, 'מות') == 'die' and sg(35, 16, 'יומת') == 'die' and sg(35, 19, 'ימית') == 'die' and sg(35, 19, 'ימיתנו') == 'die-him/its' and sg(35, 11, 'מכה') == 'strike' and sg(35, 21, 'המכה') == 'the-strike' and sg(35, 34, 'אני') == '?' and sg(35, 3, 'חיתם') == 'living-them/their' and sg(35, 31, 'רשע') == 'wrong' and sg(35, 26, 'יצא') == 'bring-forth' and sg(35, 30, 'לפי') == 'to-mouth' and sg(35, 8, 'כפי') == 'like-mouth' and sg(35, 2, 'תתנו') == 'set' and sg(35, 2, 'ונתנו') == 'and-set' and sg(35, 19, 'הדם') == 'the-blood--of-man' and sg(35, 27, 'דם') == 'blood--of-man'
assert sg(35, 19, 'בפגעו') == 'in-impinge-him/its' and sg(35, 6, 'המקלט') == 'the-asylum' and sg(35, 11, 'מקלט') == 'asylum' and sg(35, 25, 'מקלטו') == 'asylum-him/its' and sg(35, 12, 'למקלט') == 'to-asylum' and sg(35, 10, 'ארצה') == 'earth-suffix' and sg(35, 23, 'אויב') == 'hating' and sg(35, 25, 'משח') == 'rub-with-oil' and sg(35, 28, 'אחזתו') == 'something-seized-him/its' and sg(35, 29, 'מושבתיכם') == 'seat-you/your (pl)' and sg(35, 33, 'שפך') == 'spill-forth' and sg(35, 34, 'תטמא') == 'be-foul' and sg(35, 25, 'והצילו') == 'and-snatch-away' and sg(35, 24, 'ושפטו') == 'and-judge' and sg(35, 5, 'ומדתם') == 'and-stretch' and sg(35, 25, 'הגדל') == 'the-great' and sg(35, 16, 'בכלי') == 'in-vessel' and sg(35, 18, 'עץ') == 'tree'
GT = {g: store.execute("SELECT REPLACE(w.he_plain,'/',''), COUNT(*) FROM words w WHERE w.gloss=? GROUP BY 1 ORDER BY 2 DESC", (g,)).fetchall() for g in ('the-dash-in-pieces', 'dash-in-pieces', 'concretely', 'and-concretely', 'in-mother', 'mother', 'flit', 'to-flit', 'and-flit', 'in-wink', 'in-design', 'design', 'the-stated-assemblage', 'and-cardinal-number', 'suburb', 'and-suburb', 'suburb-them/their', 'and-suburb-them/their', 'soil', 'mouth-in-a-figurative-sense', 'there-suffix', 'in-mistake', 'the-blood--of-man', 'blood--of-man', 'to-blood--of-man', 'in-blood--of-man', 'in-impinge-him/its', 'the-asylum', 'asylum', 'asylum-him/its', 'to-asylum', 'earth-suffix', 'hating', 'bad-him/its', 'push-away-him/its', 'throw-out', 'rub-with-oil', 'something-seized-him/its', 'something-seized-them/their', 'from-something-seized', 'seat-you/your (pl)', 'spill-forth', 'be-foul', 'in-hostility', 'hostility', 'in-hate', 'living-them/their', 'wrong', 'like-mouth', 'from-be-the-next-of-kin', 'in-not', 'circle-them/their', 'and-light-upon', 'eye', 'cover', 'seas', 'the-strike', 'and-snatch-away', 'and-judge', 'and-stretch')}
assert GT['the-dash-in-pieces'] == [('הרצח', 14)] and GT['dash-in-pieces'] == [('רצח', 7), ('תרצח', 2), ('ירצח', 2), ('רוצח', 1), ('נפצו', 1), ('נפוץ', 1)] and GT['concretely'] == [('עד', 12), ('עדים', 5)] and GT['and-concretely'] == [('ועד', 2)] and GT['in-mother'] == [('באמה', 16), ('באמת', 1)] and [t for t, n in GT['mother']] == ['אמה', 'אמות', 'אמתים', 'אם', 'אמת'] and sum(n for t, n in GT['flit']) == 14 and all(t in ('ינוס', 'נסו', 'נס', 'תנוס', 'נסים', 'יניסו', 'ינוסו', 'הניס', 'אנוסה') for t, _ in GT['flit']) and GT['to-flit'] == [('לנוס', 4), ('לנס', 2)] and all(t in ('וינס', 'ונס', 'וינסו', 'ונסתם', 'ונסו') for t, _ in GT['and-flit'])
assert GT['in-wink'] == [('בפתע', 2)] and GT['in-design'] == [('בצדיה', 1)] and GT['design'] == [('צדיה', 1)] and GT['the-stated-assemblage'] == [('העדה', 65)] and GT['and-cardinal-number'] == [('ושמנה', 7), ('ושמנת', 1)] and GT['suburb'] == [('מגרשי', 1), ('מגרש', 1)] and GT['and-suburb'] == [('ומגרשי', 1), ('ומגרש', 1)] and GT['suburb-them/their'] == [('מגרשיהן', 1)] and GT['and-suburb-them/their'] == [('ומגרשיהם', 1)] and GT['soil'] == [('תחניפו', 1), ('יחניף', 1)] and GT['mouth-in-a-figurative-sense'] == [('פאת', 9), ('פאתי', 1)] and GT['there-suffix'] == [('שמה', 72)] and GT['in-mistake'] == [('בשגגה', 10)]
assert GT['the-blood--of-man'] == [('הדם', 51)] and GT['blood--of-man'] == [('דם', 30), ('דמים', 6), ('דמי', 3)] and GT['to-blood--of-man'] == [('לדם', 6)] and GT['in-blood--of-man'] == [('בדם', 10), ('בדמי', 1)] and GT['in-impinge-him/its'] == [('בפגעו', 2)] and GT['the-asylum'] == [('המקלט', 1)] and GT['asylum'] == [('מקלט', 3)] and GT['asylum-him/its'] == [('מקלטו', 5)] and GT['to-asylum'] == [('למקלט', 2)] and GT['earth-suffix'] == [('ארצה', 30)] and GT['hating'] == [('אויב', 7)] and GT['bad-him/its'] == [('רעתו', 1)] and GT['push-away-him/its'] == [('יהדפנו', 1), ('הדפו', 1)] and GT['throw-out'] == [('השליך', 2), ('השליכו', 1)]
assert all(t in ('משחים', 'המשח', 'משחת', 'תמשח', 'משח', 'ימשח') for t, _ in GT['rub-with-oil']) and GT['something-seized-him/its'] == [('אחזתו', 8)] and GT['something-seized-them/their'] == [('אחזתם', 4)] and GT['from-something-seized'] == [('מאחזת', 1)] and GT['seat-you/your (pl)'] == [('מושבתיכם', 7), ('משבתיכם', 3)] and all(t in ('ישפך', 'שפך', 'תשפכו', 'תשפך', 'שפכו', 'שפכה') for t, _ in GT['spill-forth']) and all('טמא' in t for t, _ in GT['be-foul']) and GT['in-hostility'] == [('באיבה', 1)] and GT['hostility'] == [('איבה', 1)] and GT['in-hate'] == [('בשנאת', 1), ('בשנאה', 1)] and GT['living-them/their'] == [('חיתם', 1)] and GT['wrong'] == [('רשע', 5)] and GT['like-mouth'] == [('כפי', 9)] and GT['from-be-the-next-of-kin'] == [('מגאל', 1)] and GT['in-not'] == [('בלא', 6)] and GT['circle-them/their'] == [('סביבתיהם', 3)]
assert GT['and-light-upon'] == [('ויקר', 2), ('והקריתם', 1)] and [t for t, n in GT['eye'] if 'ענ' in t] == ['תענה', 'ענות', 'יענה', 'ענו', 'ענה'] and ('כפר', 4) in GT['cover'] and ('מסך', 13) in GT['cover'] and GT['seas'] == [('ים', 24), ('ימים', 3)] and GT['the-strike'] == [('המכה', 7)] and ('ויתנצלו', 1) in GT['and-snatch-away'] and ('ויתפלל', 4) in GT['and-judge'] and ('ויט', 15) in GT['and-stretch']
OV = open(f'{ROOT}/logic/glosses/word_gloss_overrides.yaml', encoding='utf-8').read()
OVERRIDE_REF = [('Num.35.1:4', 'in-the-plains-of'), ('Num.35.2:4', 'and-they-shall-give'), ('Num.35.2:13', 'you-shall-give'), ('Num.35.3:9', 'their-beasts'), ('Num.35.4:3', 'you-shall-give'), ('Num.35.4:7', 'and-outward'), ('Num.35.4:9', 'cubits'), ('Num.35.4:10', 'round-about'), ('Num.35.5:0', 'and-you-shall-measure'), ('Num.35.5:15', 'the-west'), ('Num.35.6:3', 'you-shall-give'), ('Num.35.6:10', 'you-shall-give'), ('Num.35.6:14', 'and-in-addition-to-them'), ('Num.35.6:15', 'you-shall-give'), ('Num.35.7:3', 'you-shall-give'), ('Num.35.8:2', 'you-shall-give'), ('Num.35.8:6', 'from'), ('Num.35.8:7', 'the-larger'), ('Num.35.8:8', 'you-shall-take-more'), ('Num.35.8:9', 'and-from'), ('Num.35.8:10', 'the-smaller'), ('Num.35.8:11', 'you-shall-take-less'), ('Num.35.8:17', 'shall-give'), ('Num.35.8:18', 'of-his-cities'), ('Num.35.10:8', 'are-crossing'), ('Num.35.11:0', 'and-you-shall-appoint'), ('Num.35.11:9', 'a-slayer'), ('Num.35.11:10', 'one-who-smites'), ('Num.35.12:9', 'his-standing'), ('Num.35.12:10', 'before'), ('Num.35.13:2', 'you-shall-give'), ('Num.35.14:3', 'you-shall-give'), ('Num.35.14:9', 'you-shall-give'), ('Num.35.15:13', 'one-who-smites'), ('Num.35.16:1', 'with-an-instrument-of'), ('Num.35.16:3', 'struck-him'), ('Num.35.16:5', 'a-murderer'), ('Num.35.16:7', 'surely'), ('Num.35.16:8', 'shall-be-put-to-death'), ('Num.35.17:6', 'struck-him'), ('Num.35.17:8', 'a-murderer'), ('Num.35.17:10', 'surely'), ('Num.35.17:11', 'shall-be-put-to-death'), ('Num.35.18:1', 'with-an-instrument-of'), ('Num.35.18:2', 'wood'), ('Num.35.18:7', 'struck-him'), ('Num.35.18:9', 'a-murderer'), ('Num.35.18:11', 'surely'), ('Num.35.18:12', 'shall-be-put-to-death'), ('Num.35.19:0', 'the-avenger-of'), ('Num.35.19:3', 'shall-put-to-death'), ('Num.35.19:9', 'shall-put-him-to-death'), ('Num.35.21:2', 'struck-him'), ('Num.35.21:3', 'with-his-hand'), ('Num.35.21:5', 'surely'), ('Num.35.21:6', 'shall-be-put-to-death'), ('Num.35.21:7', 'the-smiter'), ('Num.35.21:8', 'a-murderer'), ('Num.35.21:10', 'the-avenger-of'), ('Num.35.21:12', 'shall-put-to-death'), ('Num.35.22:9', 'instrument'), ('Num.35.23:7', 'seeing'), ('Num.35.23:8', 'and-dropped-it'), ('Num.35.23:16', 'seeking'), ('Num.35.24:0', 'and-shall-judge'), ('Num.35.24:3', 'the-smiter'), ('Num.35.24:5', 'the-avenger-of'), ('Num.35.24:8', 'the-judgments'), ('Num.35.25:0', 'and-shall-deliver'), ('Num.35.25:5', 'the-avenger-of'), ('Num.35.25:7', 'and-shall-restore'), ('Num.35.25:19', 'the-death-of'), ('Num.35.25:21', 'the-high'), ('Num.35.25:26', 'the-holy'), ('Num.35.26:1', 'surely'), ('Num.35.26:2', 'goes-out'), ('Num.35.27:2', 'the-avenger-of'), ('Num.35.27:8', 'and-slays'), ('Num.35.27:9', 'the-avenger-of'), ('Num.35.28:5', 'the-death-of'), ('Num.35.28:7', 'the-high'), ('Num.35.28:8', 'and-after'), ('Num.35.28:9', 'the-death-of'), ('Num.35.28:11', 'the-high'), ('Num.35.30:1', 'one-who-smites'), ('Num.35.30:3', 'by-the-mouth-of'), ('Num.35.30:4', 'witnesses'), ('Num.35.30:5', 'shall-slay'), ('Num.35.30:8', 'and-one-witness'), ('Num.35.30:11', 'shall-testify'), ('Num.35.30:12', 'against-a-person'), ('Num.35.31:2', 'ransom'), ('Num.35.31:3', 'for-the-life-of'), ('Num.35.31:4', 'a-murderer'), ('Num.35.31:10', 'surely'), ('Num.35.31:11', 'shall-be-put-to-death'), ('Num.35.32:2', 'ransom'), ('Num.35.32:11', 'the-death-of'), ('Num.35.33:15', 'be-atoned'), ('Num.35.33:23', 'of-him-who-shed-it'), ('Num.35.34:9', 'I'), ('Num.35.34:13', 'I')]
OVERRIDE_GLOSS = [('the-dash-in-pieces', 'the-slayer'), ('concretely', 'witness'), ('and-concretely', 'and-witness'), ('in-mother', 'by-the-cubit'), ('flit', 'flee'), ('to-flit', 'to-flee'), ('and-flit', 'and-flee'), ('in-wink', 'suddenly'), ('in-design', 'in-lying-in-wait'), ('design', 'lying-in-wait'), ('the-stated-assemblage', 'the-congregation'), ('and-cardinal-number', 'and-eight'), ('suburb', 'pasture-land'), ('and-suburb', 'and-pasture-land'), ('suburb-them/their', 'their-pasture-lands'), ('and-suburb-them/their', 'and-their-pasture-lands'), ('soil', 'pollute'), ('mouth-in-a-figurative-sense', 'the-side-of'), ('there-suffix', 'thither'), ('in-mistake', 'unwittingly'), ('the-blood--of-man', 'the-blood'), ('blood--of-man', 'blood'), ('to-blood--of-man', 'for-the-blood'), ('in-blood--of-man', 'by-the-blood'), ('in-impinge-him/its', 'when-he-meets-him'), ('the-asylum', 'the-refuge'), ('asylum', 'refuge'), ('asylum-him/its', 'his-refuge'), ('to-asylum', 'for-refuge'), ('earth-suffix', 'to-the-land-of'), ('hating', 'enemy'), ('bad-him/its', 'his-harm'), ('push-away-him/its', 'thrust-him'), ('throw-out', 'threw'), ('rub-with-oil', 'anoint'), ('something-seized-him/its', 'his-possession'), ('something-seized-them/their', 'their-possession'), ('from-something-seized', 'from-the-possession-of'), ('seat-you/your (pl)', 'your-dwellings'), ('spill-forth', 'shed'), ('be-foul', 'defile'), ('in-hostility', 'in-enmity'), ('hostility', 'enmity'), ('in-hate', 'in-hatred'), ('living-them/their', 'their-beasts'), ('wrong', 'wicked'), ('like-mouth', 'according-to'), ('from-be-the-next-of-kin', 'from-the-avenger'), ('in-not', 'without'), ('circle-them/their', 'round-about-them')]
STORE_IDX = {(v, idx): tok for v, idx, tok in store.execute("SELECT v.verse, w.idx, REPLACE(w.he_plain,'/','') FROM words w JOIN verses v ON w.verse_id=v.id WHERE v.book='Num' AND v.chapter=35")}
REF_TOK = {k: STORE_IDX[(int(k.split('.')[2].split(':')[0]), int(k.split(':')[1]))] for k, _ in OVERRIDE_REF}
assert REF_TOK['Num.35.4:9'] == 'אמה' and REF_TOK['Num.35.5:15'] == 'ים' and REF_TOK['Num.35.11:0'] == 'והקריתם' and REF_TOK['Num.35.19:0'] == 'גאל' and REF_TOK['Num.35.21:7'] == 'המכה' and REF_TOK['Num.35.25:19'] == 'מות' and REF_TOK['Num.35.30:11'] == 'יענה' and REF_TOK['Num.35.31:2'] == 'כפר' and REF_TOK['Num.35.33:15'] == 'יכפר' and REF_TOK['Num.35.34:13'] == 'אני' and REF_TOK['Num.35.27:8'] == 'ורצח' and REF_TOK['Num.35.26:2'] == 'יצא' and REF_TOK['Num.35.8:11'] == 'תמעיטו'
assert all(REF_TOK[k] == 'תתנו' for k, v in OVERRIDE_REF if v == 'you-shall-give') and sum(1 for k, v in OVERRIDE_REF if v == 'you-shall-give') == 10 and all(REF_TOK[k] == 'הכהו' for k, v in OVERRIDE_REF if v == 'struck-him') and all(REF_TOK[k] == 'רצח' for k, v in OVERRIDE_REF if v == 'a-murderer') and all(REF_TOK[k] == 'מות' for k, v in OVERRIDE_REF if v == 'surely' and k != 'Num.35.26:1') and all(REF_TOK[k] == 'יומת' for k, v in OVERRIDE_REF if v == 'shall-be-put-to-death') and all(REF_TOK[k] == 'הגדל' for k, v in OVERRIDE_REF if v == 'the-high') and all(REF_TOK[k] == 'גאל' for k, v in OVERRIDE_REF if v == 'the-avenger-of')
assert len(OVERRIDE_REF) == 102 and len(OVERRIDE_GLOSS) == 50 and len({k for k, _ in OVERRIDE_REF}) == 102
assert all(f'"{k}": "{v}"' in OV for k, v in OVERRIDE_REF) and all(f'"{k}": "{v}"' in OV for k, v in OVERRIDE_GLOSS), [k for k, v in OVERRIDE_REF + OVERRIDE_GLOSS if f'"{k}": "{v}"' not in OV]

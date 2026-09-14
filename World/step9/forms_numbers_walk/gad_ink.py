#!/usr/bin/env python3
# THE NUMBERS WALK, sitting 12 — GAD AND REUBEN, Numbers 32:1-42 (2026-09-12; the owner: "Go" after the #148 rereads, on the ruling READ THEN
# COMPILE): THE INK of the chapter, computed from the Tanakh DB, the snapshot store and the shelf's own bytes — never typed. Sitting 11's form
# (midian_ink.py): the heads found BY POSITION and asserted (NO piska on chapter 32 — the shelf silent from 31:25 to 35:8; the whole export scanned
# for a row citing the chapter: THREE rows of other chapters cite it, credited); coverage computed; every cut by consonants (the misses collected,
# asserted empty); the engine's numeral parser MEASURED on every verse (two numbers, 32:11 twenty and 32:13 forty — no gap); the hand's facts as
# asserts, run all at once by assert_driver.py after the measurement pass (gad_measure1.py) printed them; every gloss of a narrative verb the
# STORE'S OWN (words.gloss); the piece-wise cutters HP / AP. Shared by gad_rows_onkelos_a.py / _b.py and write_gad_ledger.py.
# THE SPAN: ONE draft — num_32_gad_reuben 32:1-42 (the portion Matot's third and last chapter); the next draft (num_33_journeys) opens at 33:1.
import json, os, re, html, sqlite3, sys, io, contextlib, unicodedata
from collections import Counter
ROOT = '<repo-old>'
DATE = '2026-09-12'
UID = 'num_32_gad_reuben'
PISKAOT = []
CREDITED = [(86, 1, (32, 1)), (95, 1, (32, 1)), (106, 1, (32, 37))]
TITLE = 'Gad and Reuben — much cattle, and the land of Jazer and Gilead a place for cattle; the request before Moses, Eleazar and the princes, do not bring us over the Jordan; Moses\' rebuke: will your brothers go to war and you sit here? your fathers at Kadesh Barnea, the oath retold, a brood of sinful men; the offer: folds for the flocks and cities for the little ones, armed before Israel until every man has inherited; the condition doubled before the LORD — clear before the LORD and before Israel, your sin will find you, what goes out of your mouth you shall do; Eleazar, Joshua and the heads of the fathers charged with both arms; the grant to Gad, Reuben and half Manasseh of the two kingdoms; the cities built and renamed; Machir, Jair and Nobah in Gilead'
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
# THE SHELF BY POSITION: piska 158 (31:22) is followed by 159 (35:9) — NO piska on chapter 32 (nor on 33 or 34): the shelf silent from 31:25 to
# 35:8, as sitting 11 computed (165 verses). THE "FOUND BY POSITION" CLAUSE run on the whole export: every row of every piska scanned for a
# citation of chapter 32 — THREE rows of OTHER chapters cite it: 86:1 (on 11:2) and 95:1 (on 11:21) quote 32:1's "much cattle" as the proof that
# Egypt's flocks (Exodus 12:38) survived the desert — the craving a PRETEXT; 106:1 (on 12:14) quotes 32:37-38's "the sons of Reuben built... Nebo"
# to place Moses' death in Reuben's portion. All three were read whole at sitting 3 (the num_11_complaint_quail and num_12_miriam ledgers) and are
# CREDITED here with a QUICK LOOK (credit guard 1: each opened again this sitting, in both files — what each says of 32 is one proof clause).
assert heads[157] == ('Bamidbar', 31, 1) and heads[158] == ('Bamidbar', 31, 22) and heads[159] == ('Bamidbar', 35, 9) and len(sif) == 161
assert sorted(p for p, h in heads.items() if h and h[0] == 'Bamidbar' and h[1] in (32, 33, 34)) == [] and [p for p, h in heads.items() if h and h[0] == 'Bamidbar' and h[1] == 35 and h[2] < 9] == []
CITING = [(p, r, re.findall(r'\(Bamidbar\.? 32:(\d+)', clean(row))) for p, rows in enumerate(sif, 1) for r, row in enumerate(rows, 1) if re.search(r'\(Bamidbar\.? 32:\d+', clean(row))]
assert CITING == [(86, 1, ['1']), (95, 1, ['1']), (106, 1, ['37'])] and [(p, r) for p, rows in enumerate(sif_he, 1) for r, row in enumerate(rows, 1) if re.search(r'במדבר ל"?ב\b', clean(row))] == [(86, 1), (95, 1), (106, 1)]
def E(p, r): return clean(sif[p - 1][r - 1])
def Hb(p, r): return clean(sif_he[p - 1][r - 1])
assert heads[86] == ('Bamidbar', 11, 2) and heads[95] == ('Bamidbar', 11, 21) and heads[106] == ('Bamidbar', 12, 14)
assert '(Bamidbar 32:1) "And much livestock were possessed by the sons of Reuven and the sons of Gad, etc."' in E(86, 1) and 'ומקנה רב היה לבני גד ולבני ראובן' in Hb(86, 1) and 'seeking a pretext to abandon the L-rd' in E(86, 1)   # the Hebrew row quotes the verse with GAD FIRST — the chapter's own order at 32:2 (the ink of 32:1 has Reuben first)
assert '(Bamidbar 32:1) "And the sons of Reuven and the sons of Gad had much cattle, etc."' in E(95, 1) and 'ומקנה רב היה לבני גד ולבני ראובן' in Hb(95, 1)
assert '(Bamidbar 32:37-38) "And the sons of Reuven built Cheshbon and Elalei and Kiryathayim and Nevo."' in E(106, 1) and 'ובני ראובן בנו את חשבון ואת אלעלה ואת קריתים ואת נבו' in Hb(106, 1) and 'Where did Moses die? In the portion of Reuven' in E(106, 1) and 'buried only in the territory of Gad' in E(106, 1)
SIF_ROWS = {}
def head(p): return heads[p][1:]
def plain(w): return ''.join(c for c in w if c != '/' and not (0x0591 <= ord(c) <= 0x05C7))
def pointed(w): return ''.join(c for c in w if c != '/' and not (0x0591 <= ord(c) <= 0x05AF))
ONK_LEN = {c: len(onk[c - 1]) for c in (31, 32, 33)}
assert ONK_LEN == {31: 54, 32: 42, 33: 56} and {c: len(onk_he[c - 1]) for c in (31, 32, 33)} == ONK_LEN, ONK_LEN
def onk_ev(c, v): return clean(onk[c - 1][v - 1]), clean(onk_he[c - 1][v - 1])
shelf_numbers = sorted(d for d in os.listdir(f'{ROOT}/Data/sefaria_export') if re.search(r'Numbers|Bamidbar', d))
outside = [d for d in shelf_numbers if d not in ('Sifrei_Bamidbar', 'Onkelos_Numbers')]
assert len(outside) == 23, len(outside)
# THE PRIOR READS: no ledger has read an Onkelos row of 32; FIVE ledgers NAME verses of the chapter — the Beha'alotcha ledgers (32:1 by the Sifrei's
# two rows; 32:37-38 by 106:1), the vows' exam docket (32:29-30 THE DOUBLED CONDITION as the forward edge; 32:24 the utterance rule's seat filed at
# 10b), and the two Exodus dockets (32:22 "clear before the LORD and before Israel" — Mishnah Shekalim 3:2's proof): names, not reads; FRESH
TRI = f'{ROOT}/logic/oral_triage'
LED = {f: open(f'{TRI}/{f}', encoding='utf-8').read() for f in os.listdir(TRI) if f.endswith('.md') and os.path.isfile(f'{TRI}/{f}') and f'{TRI}/{f}' != OUT}
assert sorted(f for f, t in LED.items() if re.search(r'^- Onkelos Num 32:\d', t, re.M)) == []
NAMING = sorted(f for f, t in LED.items() if re.search(r'Num(?:bers)? 32:\d+', t))
assert NAMING == ['incense_shekel_docket_2026-09-06.md', 'num_11_complaint_quail_2026-09-10.md', 'num_12_miriam_2026-09-10.md', 'num_30_vows_exam_2026-09-12.md', 'sanctuary_build_docket_2026-09-06.md'], NAMING
assert len(re.findall(r'Num 32:1\b', LED['num_11_complaint_quail_2026-09-10.md'])) == 2 and 'Num 32:37-38' in LED['num_12_miriam_2026-09-10.md'] and 'Num 32:29-30' in LED['num_30_vows_exam_2026-09-12.md'] and 'Num 32:22' in LED['incense_shekel_docket_2026-09-06.md'] and 'Num 32:22' in LED['sanctuary_build_docket_2026-09-06.md']

# ---- THE DRAFT'S SPAN, COMPUTED ----
db = sqlite3.connect(f'file:{ROOT}/elijah_docket/tanakh.sqlite?mode=ro', uri=True)
VC = dict(db.execute("SELECT chapter, COUNT(*) FROM verses WHERE book='Num' GROUP BY chapter").fetchall())
assert VC[31] == 54 and VC[32] == 42 and VC[33] == 56
def unit_text(uid): return open(f'{ROOT}/logic/units/{uid}.yaml', encoding='utf-8').read()
def steps(uid): return sorted({(int(a), int(b)) for a, b in re.findall(r'STEP_Nm_(\d+)_(\d+)', unit_text(uid))})
assert steps(UID) == [(32, v) for v in range(1, 43)] and 'status: draft' in unit_text(UID) and 'operators:' not in unit_text(UID)
assert steps('num_33_journeys')[0] == (33, 1) and 'status: frozen' in unit_text('num_31_midian')
SPAN = [(32, v) for v in range(1, 43)]
NV = 42

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
def seats_in(pred): return [(v, x) for (c, v) in SPAN for x, m in by[('Num', 32, v)] if pred(x, m)]
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
for c, v, hp, g in store.execute("SELECT v.chapter, v.verse, w.he_plain, w.gloss FROM words w JOIN verses v ON w.verse_id=v.id WHERE v.book='Num' AND v.chapter = 32 ORDER BY v.id, w.idx"):
    SG.setdefault((c, v), []).append((hp.replace('/', ''), g))
def sg(c, v, tok):
    for hp, g in SG[(c, v)]:
        if hp == tok: return g
    raise KeyError((c, v, tok))

# THE ENGINE'S PARSER on every verse of the chapter — MEASURED before the compile is asked: TWO numbers in forty-two verses, both read — 32:11
# "from twenty years old and upward" [20], 32:13 "forty years" [40]; no ordinal, no starred homograph, no fraction; "half the tribe of Manasseh"
# (32:33) rightly no number (the half a noun, not a numeral); 33:1 empty. NO GAP in the chapter.
sys.path.insert(0, f'{ROOT}/World/step9')
with contextlib.redirect_stdout(io.StringIO()):
    import cold_run_sequence as CS
def N(b, c, v): return CS.ink_numbers(CS.verse_words(b, c, v))
def O(b, c, v): return CS.ink_ordinals(CS.verse_words(b, c, v))
PARSED = {v: N('Num', 32, v) for v in range(1, NV + 1) if N('Num', 32, v)}
assert PARSED == {11: [20], 13: [40]}, PARSED
assert {v: O('Num', 32, v) for v in range(1, NV + 1) if O('Num', 32, v)} == {} and [(v, t) for v in range(1, NV + 1) for t in CS.verse_words('Num', 32, v) if t.endswith('*')] == [] and N('Num', 33, 1) == []
# THE RETELLINGS' NUMBERS, read by the same parser: Joshua 4:13 "about forty thousand armed" against the second census's Reuben 43,730 + Gad 40,500
# + half of Manasseh's 52,700 = 110,580 (the ink's own ratio, a little over a third); 1 Chronicles 5:18's 44,760 warriors of the two and a half;
# Jair's twenty-three cities (1 Chronicles 2:22) and the sixty (2:23, Joshua 13:30, Deuteronomy 3:4); Judges 10:4's thirty; 14:34's forty and forty
assert N('Josh', 4, 13) == [40000] and N('1Chr', 5, 18) == [44760] and N('Num', 26, 7) == [43730] and N('Num', 26, 18) == [40500] and N('Num', 26, 34) == [52700] and 43730 + 40500 + 52700 // 2 == 110580
assert N('1Chr', 2, 22) == [23] and N('1Chr', 2, 23) == [60] and N('Judg', 10, 4) == [30, 30, 30] and N('Deut', 3, 4) == [60] and N('Num', 14, 34) == [40, 40] and N('Num', 14, 33) == [40]

# THE FRAMES AND THE REGISTER: THIRTY-ONE narrative verbs in twenty verses (computed on the morphology) — a chapter of SPEECH: nine speech verbs
# (they said, he said, he commanded, they answered) and NO DIVINE FRAME — no "and the LORD spoke/said" in forty-two verses; the chapters of Numbers
# without one are 22-24 (Balak), 29 (the festival table's second chapter), 30 (the vows, in Moses' voice), 32 and 36 — so the chapter's one "the
# LORD swore" (32:10) is Moses QUOTING the oath of chapter 14, and the two tribes' "as the LORD has spoken to your servants" (32:31) calls MOSES'
# stipulation the LORD's word; "the LORD" eighteen tokens, "before the LORD" SEVEN (32:20, 21, 22 twice, 27, 29, 32 — the phrase's 212 Bible seats)
REG = [(v, x, m) for (c, v) in SPAN for x, m in by[('Num', 32, v)] if m and re.search(r'V.w', m)]
assert len(REG) == 31 and sorted({v for v, _, _ in REG}) == [1, 2, 5, 6, 9, 10, 13, 16, 20, 25, 28, 29, 31, 33, 34, 38, 39, 40, 41, 42] and REG[0] == (1, 'ויראו', 'HC/Vqw3mp') and REG[-1] == (42, 'ויקרא', 'HC/Vqw3ms')
assert [(v, x) for v, x, _ in REG if x in ('ויאמר', 'ויאמרו', 'וידבר', 'ויענו', 'ויצו')] == [(2, 'ויאמרו'), (5, 'ויאמרו'), (6, 'ויאמר'), (16, 'ויאמרו'), (20, 'ויאמר'), (25, 'ויאמר'), (28, 'ויצו'), (29, 'ויאמר'), (31, 'ויענו')]
DIV = {}
for (b, c, v), ws in by.items():
    if b != 'Num': continue
    w = [x for x, _ in ws]
    if any(w[i] in ('ויאמר', 'וידבר') and w[i + 1] == 'יהוה' for i in range(len(w) - 1)): DIV.setdefault(c, []).append(v)
assert [c for c in range(1, 37) if c not in DIV] == [22, 23, 24, 29, 30, 32, 36] and DIV[31] == [1, 25] and DIV[33] == [50] and DIV[34] == [1, 16] and DIV[35] == [1, 9]
assert len(seats_in(lambda x, m: 'יהוה' in x)) == 18 and [(v, i) for v in range(1, NV + 1) for i in range(len(words('Num', 32, v)) - 1) if words('Num', 32, v)[i:i + 2] == ['לפני', 'יהוה']] == [(20, 10), (21, 6), (22, 2), (22, 15), (27, 5), (29, 15), (32, 3)] and len(phrase(['לפני', 'יהוה'], None)) == 212
assert sg(32, 31, 'ויענו') == 'and-eye' and sg(32, 16, 'ויגשו') == 'and-be' and sg(32, 10, 'ויחר') == 'and-glow' and sg(32, 13, 'וינעם') == 'and-waver-them/their' and sg(32, 14, 'תרבות') == 'multiplication' and sg(32, 14, 'לספות') == 'to-scrape--together' and sg(32, 15, 'ושחתם') == 'and-decay' and sg(32, 8, 'מקדש') == 'from-?' and sg(32, 41, 'חות') == '?' and sg(32, 38, 'מוסבת') == 'revolve' and sg(32, 13, 'במדבר') == 'in-pasture'   # the store's own glosses read back: the answer-verb by its eye-homonym, the approach-verb "and-be"
# ONKELOS BUFFERS THE WAR'S "BEFORE THE LORD" TO "BEFORE THE PEOPLE OF THE LORD": at 32:20, 21, 22 (the subduing), 27, 29 and 32 — every martial
# seat — and keeps "before the LORD" where the phrase is legal (32:22 "clear before the LORD", "a possession before the LORD"; 32:23 "sinned before
# the LORD"); the buffer's SIX seats in Onkelos Numbers are all this chapter's (computed on the whole book); 1 Chronicles 22:18 writes the double in
# its own ink — "and the land is subdued before the LORD and before his people" — the phrase of 32:22 and 32:29 at its one seat outside the chapter
AM = []
for cc, ch in enumerate(onk_he, 1):
    for vv, vs in enumerate(ch, 1):
        t = [plain(x) for x in clean(vs).rstrip(':').split()]
        AM += [f'{cc}:{vv}' for i in range(len(t) - 2) if t[i:i + 3] == ['קדם', 'עמא', 'דיי']]
assert AM == ['32:20', '32:21', '32:22', '32:27', '32:29', '32:32'] and aramaic(32, 22)[2:5] == ['קדם', 'עמא', 'דיי'] and aramaic(32, 22)[10:14] == ['מן', 'קדם', 'יי', 'ומישראל'] and aramaic(32, 22)[18:21] == ['לאחסנא', 'קדם', 'יי'] and aramaic(32, 23)[6:8] == ['קדם', 'יי'] and aramaic(32, 4)[6:9] == ['קדם', 'כנשתא', 'דישראל']
assert phrase(['ונכבשה', 'הארץ'], None) == ['1Chr 22:18', 'Num 32:22', 'Num 32:29'] and U('נכבשה', 'ונכבשה') == ['1Chr 22:18', 'Josh 18:1', 'Num 32:22', 'Num 32:29'] and words('1Chr', 22, 18)[-6:] == ['ונכבשה', 'הארץ', 'לפני', 'יהוה', 'ולפני', 'עמו']

# THE CATTLE AND THE LAND (32:1-5): "much cattle" — the phrase's seats Deuteronomy 3:19 ("I know that you have much cattle" — Moses' retelling
# quoting this verse) and Uzziah's (2 Chronicles 26:10); 1 Chronicles 5:9 "their cattle multiplied in the land of Gilead"; "very mighty" one seat
# (Exodus 1:7's "waxed mighty" its kin; Egypt's flocks "very heavy cattle", 12:38 — the Sifrei's proof); "the land of Jazer" one seat, "the land
# of Gilead" here and Zechariah's; Jazer spied out and its villages taken at 21:32; "a place for cattle" and "a land for cattle" one seat each;
# LOT'S CHOICE the ink's kin — "their substance was great", "Lot lifted his eyes and SAW all the plain of the Jordan" (Genesis 13:6, 10) beside
# "and they SAW the land of Jazer... and behold, the place was a place for cattle" — OBSERVED, no row of the declared shelf links them; the
# addressees the triad of 31:13 (Moses, Eleazar, the princes of the congregation — the phrase's five seats); THE NINE CITIES asked (32:3);
# "the land which the LORD smote before the congregation of Israel" — Sihon's and Og's (21:24, 35); "if WE have found favor" the plural's one
# seat; "for a possession" — the possession-word at 32:5, 22, 29 (the daughters' 27:4, 7); "do not bring us over the Jordan" one seat
assert phrase(['ומקנה', 'רב'], None) == ['Num 32:1'] and phrase(['מקנה', 'רב'], None) == ['2Chr 26:10', 'Deut 3:19'] and seats_in(lambda x, m: 'מקנ' in x) == [(1, 'ומקנה'), (1, 'מקנה'), (4, 'מקנה'), (4, 'מקנה'), (16, 'למקננו'), (26, 'מקננו')] and words('Deut', 3, 19)[4:9] == ['ידעתי', 'כי', 'מקנה', 'רב', 'לכם'] and words('1Chr', 5, 9)[-5:] == ['כי', 'מקניהם', 'רבו', 'בארץ', 'גלעד']
assert phrase(['עצום', 'מאד'], None) == ['Num 32:1'] and words('Exod', 12, 38)[-3:] == ['מקנה', 'כבד', 'מאד'] and words('Gen', 13, 2)[:4] == ['ואברם', 'כבד', 'מאד', 'במקנה'] and words('Exod', 1, 7)[5:8] == ['ויעצמו', 'במאד', 'מאד']
assert phrase(['ארץ', 'יעזר'], None) == ['Num 32:1'] and phrase(['ארץ', 'גלעד'], None) == ['Num 32:1', 'Zech 10:10'] and phrase(['ארץ', 'הגלעד'], None) == ['2Kgs 10:33', '2Sam 17:26', 'Josh 22:13', 'Josh 22:15', 'Josh 22:9', 'Num 32:29'] and words('Num', 21, 32) == ['וישלח', 'משה', 'לרגל', 'את', 'יעזר', 'וילכדו', 'בנתיה', 'ויירש', 'את', 'האמרי', 'אשר', 'שם']
assert phrase(['מקום', 'מקנה'], None) == ['Num 32:1'] and phrase(['ארץ', 'מקנה'], None) == ['Num 32:4'] and phrase(['והנה', 'המקום'], None) == ['Num 32:1'] and words('Gen', 13, 6)[6:10] == ['כי', 'היה', 'רכושם', 'רב'] and words('Gen', 13, 10)[:5] == ['וישא', 'לוט', 'את', 'עיניו', 'וירא'] and words('Gen', 13, 13) == ['ואנשי', 'סדם', 'רעים', 'וחטאים', 'ליהוה', 'מאד']
assert phrase(['ואל', 'נשיאי', 'העדה'], None) == ['Num 32:2'] and phrase(['נשיאי', 'העדה'], None) == ['Exod 16:22', 'Josh 9:15', 'Josh 9:18', 'Num 31:13', 'Num 32:2'] and words('Num', 31, 13)[:7] == ['ויצאו', 'משה', 'ואלעזר', 'הכהן', 'וכל', 'נשיאי', 'העדה']
assert words('Num', 32, 3) == ['עטרות', 'ודיבן', 'ויעזר', 'ונמרה', 'וחשבון', 'ואלעלה', 'ושבם', 'ונבו', 'ובען'] and all('Np' in m for m in morphs('Num', 32, 3)) and aramaic(32, 3) == ['מכללתא', 'ומלבשתא', 'וכומרין', 'ובית', 'נמרין', 'ובית', 'חושבנא', 'ובעלי', 'דבבא', 'וכימא', 'וסיעת', 'בית', 'קברתא', 'דמשה', 'ובעון']   # ONKELOS renders the nine by their Aramaic names — Nebo as "the burial place of Moses"
assert phrase(['הכה', 'יהוה'], None) == ['1Sam 6:19', 'Num 32:4', 'Num 33:4'] and phrase(['לפני', 'עדת', 'ישראל'], None) == ['Num 32:4'] and aramaic(32, 4)[4:6] == ['ית', 'יתבהא'] and words('Num', 21, 35)[-3:] == ['ויירשו', 'את', 'ארצו']
assert phrase(['אם', 'מצאנו', 'חן', 'בעיניך'], None) == ['Num 32:5'] and phrase(['מצאנו', 'חן'], None) == ['Num 32:5'] and [s for s in U('לאחזה') if s.startswith('Num')] == ['Num 32:22', 'Num 32:29', 'Num 32:5'] and seats_in(lambda x, m: 'אחז' in x) == [(5, 'לאחזה'), (22, 'לאחזה'), (29, 'לאחזה'), (30, 'ונאחזו'), (32, 'אחזת')]
assert words('Num', 27, 7)[7:9] == ['אחזת', 'נחלה'] and phrase(['אחזת', 'נחלה'], None) == ['Num 27:7'] and phrase(['אחזת', 'נחלתנו'], None) == ['Num 32:32'] and words('Num', 27, 4)[-4:] == ['אחזה', 'בתוך', 'אחי', 'אבינו']
assert phrase(['אל', 'תעברנו', 'את', 'הירדן'], None) == ['Num 32:5'] and U('תעברנו') == ['Num 32:5'] and aramaic(32, 5)[10] == 'לאחסנא' and aramaic(32, 1)[17:22] == ['אתרא', 'אתר', 'כשר', 'לבית', 'בעיר']

# MOSES' REBUKE (32:6-15): "shall your brothers go to war and you sit here?" — the interrogative one seat, "you sit here" one (Abraham's "sit
# here with the ass", Genesis 22:5, its kin); THE HINDER-ROOT — the vows' verb: "why do you DISCOURAGE the heart" (32:7) and "they discouraged
# the heart" (32:9, the spies) share their root with the father's and the husband's "he DISALLOWED her" of chapter 30 (30:6 twice, 30:9, 30:12)
# — the root's six Torah tokens all in chapters 30 and 32, and its one noun in the Torah is 14:34's "you shall know MY ALIENATION" — the oath
# 32:10-13 retells; 32:7 IS A WRITTEN-AND-READ PAIR — the store carries the written form and the read form side by side (fourteen tokens for the
# DB's thirteen, the one such verse in the chapter; 1:16's pair the walk's first), the DB writing the written form without its points; "the heart
# of the children of Israel" 32:7, 9 (Deuteronomy 1:28 "our brothers have MELTED our heart" the retelling's verb); "thus did your fathers" here
# and Nehemiah 13:18; THE SPIES' VERB AT EACH TELLING — "to spy out" (13:2, 17), "TO SEE" (32:8, one seat), "to search" (Deuteronomy 1:22), "to
# scout" (1:24); Kadesh Barnea in Numbers at 32:8 and 34:4 alone (the store glossing "from Kadesh" as "from-?"); "the valley of Eshcol" 13:24 and
# this; "they went up... and saw the land" — 13:21-24's run in one verse
assert U('האחיכם') == ['Num 32:6'] and phrase(['ואתם', 'תשבו', 'פה'], None) == ['Num 32:6'] and phrase(['שבו', 'לכם', 'פה'], None) == ['Gen 22:5'] and phrase(['יבאו', 'למלחמה'], None) == ['Num 32:6']
assert [(v, x, m) for v in range(1, 18) for x, m in by[('Num', 30, v)] if 'ניא' in x] == [(6, 'הניא', 'HVhp3ms'), (6, 'הניא', 'HVhp3ms'), (9, 'יניא', 'HVhi3ms'), (12, 'הניא', 'HVhp3ms')] and [(v, x, m) for v in (7, 9) for x, m in by[('Num', 32, v)] if 'ניא' in x or 'נוא' in x] == [(7, 'תנואון', 'HVqi2mp/Sn'), (9, 'ויניאו', 'HC/Vhw3mp')]
assert sorted({f"{b} {c}:{v}" for (b, c, v), ws in by.items() if b in T for x, m in ws if x in ('הניא', 'יניא', 'תנואון', 'ויניאו')}) == ['Num 30:12', 'Num 30:6', 'Num 30:9', 'Num 32:7', 'Num 32:9'] and words('Ps', 33, 10)[4] == 'הניא'   # the token set named — a substring census on the root's two letters catches "the hated wife" (Deuteronomy 21:15) and "we have been foolish" (12:11) and U('תנואתי', 'תנואות') == ['Job 33:10', 'Num 14:34'] and words('Num', 14, 34)[19] == 'תנואתי' and morphs('Num', 14, 34)[19] == 'HNcfsc/Sp1cs'
ST7 = store.execute("SELECT w.idx, w.he_plain FROM words w JOIN verses v ON w.verse_id=v.id WHERE v.book='Num' AND v.chapter=32 AND v.verse=7 ORDER BY w.idx").fetchall()
assert len(ST7) == 14 and ST7[1] == (1, 'תנואו/ן') and ST7[2] == (2, 'תניאו/ן') and len(words('Num', 32, 7)) == 13 and byraw[('Num', 32, 7)][1] == 'תנואו/ן' and [(v, n) for v, n in store.execute("SELECT v.verse, COUNT(*) FROM words w JOIN verses v ON w.verse_id=v.id WHERE v.book='Num' AND v.chapter=32 GROUP BY v.verse").fetchall() if n != len(words('Num', 32, v))] == [(7, 14)]
assert [x for _, x in store.execute("SELECT w.idx, w.he_plain FROM words w JOIN verses v ON w.verse_id=v.id WHERE v.book='Num' AND v.chapter=1 AND v.verse=16 ORDER BY w.idx").fetchall()[1:3]] == ['קריאי', 'קרואי']
assert phrase(['לב', 'בני', 'ישראל'], None) == ['Num 32:7', 'Num 32:9'] and phrase(['מעבר', 'אל', 'הארץ'], None) == ['Num 32:7'] and words('Deut', 1, 28)[3:6] == ['אחינו', 'המסו', 'את']
assert phrase(['כה', 'עשו', 'אבתיכם'], None) == ['Neh 13:18', 'Num 32:8'] and U('ברנע') == ['Deut 1:19', 'Deut 1:2', 'Deut 2:14', 'Deut 9:23', 'Josh 10:41', 'Josh 14:6', 'Josh 14:7', 'Josh 15:3', 'Num 32:8', 'Num 34:4'] and aramaic(32, 8)[6:8] == ['מרקם', 'גיאה']
assert words('Num', 13, 2)[3] == 'ויתרו' and words('Num', 13, 17)[3] == 'לתור' and words('Num', 32, 8)[-3] == 'לראות' and words('Deut', 1, 22)[7] == 'ויחפרו' and words('Deut', 1, 24)[7] == 'וירגלו' and phrase(['לראות', 'את', 'הארץ'], None) == ['Num 32:8'] and phrase(['לתור', 'את', 'הארץ'], None) == ['Num 13:16', 'Num 14:36', 'Num 14:38']
assert phrase(['נחל', 'אשכול'], None) == ['Num 13:24', 'Num 32:9'] and phrase(['ויראו', 'את', 'הארץ'], None) == ['Num 32:9'] and phrase(['לבלתי', 'בא'], None) == ['Num 32:9']
# THE OATH RETOLD (32:10-13): "the LORD's anger burned on that day and HE SWORE" — chapter 14 never uses the verb "swore" of the doom (its oath is
# "as I live", 14:21, 28 — the formula); 32:10 and Deuteronomy 1:34 ("he was wroth and swore") both supply it; "IF they shall see" — 14:23's own
# "if" (the oath's negative) at two seats; "the men who came up from Egypt" one seat; "from twenty years old and upward" — the CENSUS FORMULA
# (its twenty-three seats: the two censuses, the half-shekel's, 14:29's doom on "all your numbered", this); "which I swore to Abraham, Isaac and
# Jacob" — Exodus 33:1, Deuteronomy 34:4 (Moses' own death-view) and this; "they have not FOLLOWED ME FULLY" — Caleb's phrase of 14:24 ("he
# followed me fully"), at 32:11 (after ME, God's own voice), 32:12, Deuteronomy 1:36, Joshua 14:8, 9, 14 and Solomon's negative (1 Kings 11:6);
# Caleb "THE KENIZZITE" — the gentilic of a Canaanite nation (Genesis 15:19's Kenizzite) at Caleb's three seats (32:12; Joshua 14:6, 14; Othniel
# "son of Kenaz, Caleb's brother" 15:17); Caleb and Joshua in one verse at four seats; ONKELOS "after my FEAR" (32:11, 12, 15 — the buffer on
# "after me"); "HE MADE THEM WANDER" — the causative one seat in the Torah (14:33's "shepherds forty years" the plain form); "forty years" in
# Numbers 14:33, 34 and this; "UNTIL ALL THE GENERATION WAS CONSUMED" — Deuteronomy 2:14's "until all the generation of the men of war was
# consumed" (the retelling's phrase, computed to thirty-eight years there); "WHO DID EVIL IN THE EYES OF THE LORD" — the JUDGES' AND KINGS'
# FORMULA (fifty-three Bible seats) at its FIRST seat, the Torah's five all here and in Deuteronomy; "the LORD's anger burned against ISRAEL" —
# Peor's verse (25:3) and the Judges' refrain
assert len(phrase(['ויחר', 'אף', 'יהוה'], None)) == 17 and seats_in(lambda x, m: x == 'ויחר') == [(10, 'ויחר'), (13, 'ויחר')] and [s for s in phrase(['ויחר', 'אף', 'יהוה'], None) if s.startswith('Num')] == ['Num 11:10', 'Num 12:9', 'Num 25:3', 'Num 32:10', 'Num 32:13'] and phrase(['ויחר', 'אף', 'יהוה', 'בישראל'], None) == ['2Kgs 13:3', 'Judg 10:7', 'Judg 2:14', 'Judg 2:20', 'Judg 3:8', 'Num 25:3', 'Num 32:13']
assert phrase(['ביום', 'ההוא', 'וישבע'], None) == ['Num 32:10'] and U('וישבע', books=T) == ['Deut 1:34', 'Deut 4:21', 'Gen 24:9', 'Gen 25:33', 'Gen 31:53', 'Gen 47:31', 'Gen 50:25', 'Num 32:10'] and words('Deut', 1, 34)[-3:] == ['ויקצף', 'וישבע', 'לאמר'] and [s for s in phrase(['חי', 'אני'], None) if s.startswith('Num')] == ['Num 14:21', 'Num 14:28'] and not any(x == 'וישבע' for v in range(21, 36) for x in words('Num', 14, v))
assert phrase(['אם', 'יראו'], None) == ['Num 14:23', 'Num 32:11'] and phrase(['האנשים', 'העלים', 'ממצרים'], None) == ['Num 32:11'] and len(phrase(['מבן', 'עשרים', 'שנה', 'ומעלה'], None)) == 23 and [s for s in phrase(['מבן', 'עשרים', 'שנה', 'ומעלה'], None) if not s.startswith('Num 1:') and not s.startswith('Num 26:')] == ['1Chr 23:24', 'Exod 30:14', 'Exod 38:26', 'Ezra 3:8', 'Num 14:29', 'Num 32:11'] and words('Num', 14, 29)[8:12] == ['מבן', 'עשרים', 'שנה', 'ומעלה']
assert phrase(['נשבעתי', 'לאברהם', 'ליצחק', 'וליעקב'], None) == ['Deut 34:4', 'Exod 33:1', 'Num 32:11'] and len(phrase(['לאברהם', 'ליצחק', 'וליעקב'], None)) == 11
FILL = sorted({f"{b} {c}:{v} {' '.join(w[i:i + 3])}" for (b, c, v), ws in by.items() for w in [[x for x, _ in ws]] for i in range(len(w) - 1) if w[i] in ('מלא', 'מלאו', 'מלאתי') and w[i + 1] in ('אחרי', 'אחר')})
assert FILL == ['1Kgs 11:6 מלא אחרי יהוה', 'Deut 1:36 מלא אחרי יהוה', 'Josh 14:14 מלא אחרי יהוה', 'Josh 14:8 מלאתי אחרי יהוה', 'Num 32:11 מלאו אחרי', 'Num 32:12 מלאו אחרי יהוה'] and words('Num', 14, 24)[7:9] == ['וימלא', 'אחרי'] and words('Josh', 14, 9)[-4:-1] == ['מלאת', 'אחרי', 'יהוה'] and words('1Kgs', 11, 6)[5:9] == ['ולא', 'מלא', 'אחרי', 'יהוה']
assert phrase(['בלתי', 'כלב'], None) == ['Num 32:12'] and phrase(['כלב', 'בן', 'יפנה'], None) == ['1Chr 4:15', 'Deut 1:36', 'Josh 14:6', 'Num 13:6', 'Num 14:30', 'Num 26:65', 'Num 32:12', 'Num 34:19'] and U('הקנזי') == ['Gen 15:19', 'Josh 14:14', 'Josh 14:6', 'Num 32:12'] and words('Gen', 15, 19) == ['את', 'הקיני', 'ואת', 'הקנזי', 'ואת', 'הקדמני'] and words('Josh', 15, 17)[:6] == ['וילכדה', 'עתניאל', 'בן', 'קנז', 'אחי', 'כלב']
assert sorted({f"{b} {c}:{v}" for (b, c, v), ws in by.items() for w in [[x for x, _ in ws]] if 'כלב' in w and ('ויהושע' in w or 'יהושע' in w)}) == ['Josh 14:6', 'Num 14:30', 'Num 26:65', 'Num 32:12']
assert aramaic(32, 11)[-4:] == ['לא', 'אשלימו', 'בתר', 'דחלתי'] and aramaic(32, 12)[-4:] == ['אשלימו', 'בתר', 'דחלתא', 'דיי'] and aramaic(32, 15)[:4] == ['ארי', 'תתובון', 'מבתר', 'דחלתיה'] and aramaic(32, 12)[4] == 'קנזאה'
assert U('וינעם') == ['Num 32:13'] and morphs('Num', 32, 13)[4] == 'HC/Vhw3ms/Sp3mp' and [f'{b} {c}:{v}' for (b, c, v), ws in by.items() if b in T for x, m in ws if m and 'Vh' in m and x in ('וינעם', 'הניעה', 'יניעו', 'הניעמו', 'יניעון', 'יניע')] == ['Num 32:13'] and words('Num', 14, 33)[:6] == ['ובניכם', 'יהיו', 'רעים', 'במדבר', 'ארבעים', 'שנה'] and aramaic(32, 13)[4] == 'וטרדנון'
assert [s for s in phrase(['ארבעים', 'שנה'], None) if s.startswith('Num')] == ['Num 14:33', 'Num 14:34', 'Num 32:13'] and phrase(['במדבר', 'ארבעים', 'שנה'], None) == ['Amos 2:10', 'Amos 5:25', 'Num 14:33', 'Num 32:13']
assert phrase(['עד', 'תם', 'כל'], None) == ['1Kgs 6:22', '2Sam 15:24', 'Deut 2:14', 'Jer 36:23', 'Jer 37:21', 'Josh 4:10', 'Josh 5:6', 'Num 32:13'] and words('Deut', 2, 14)[14:20] == ['עד', 'תם', 'כל', 'הדור', 'אנשי', 'המלחמה'] and phrase(['כל', 'הדור'], None) == ['Deut 2:14', 'Judg 2:10', 'Num 32:13'] and N('Deut', 2, 14) == [38]
assert phrase(['העשה', 'הרע', 'בעיני', 'יהוה'], None) == ['Num 32:13'] and len(phrase(['הרע', 'בעיני', 'יהוה'], None)) == 53 and phrase(['הרע', 'בעיני', 'יהוה']) == ['Deut 17:2', 'Deut 31:29', 'Deut 4:25', 'Deut 9:18', 'Num 32:13']
# "A BROOD OF SINFUL MEN" (32:14-15): "you have risen in your fathers' place" one seat; "brood" a hapax; "sinful men" one seat — "sinners" in the
# Torah only of SODOM'S MEN (Genesis 13:13 "wicked and sinners against the LORD exceedingly") and this — Lot's plain again; ONKELOS "disciples of
# the guilty men"; "TO ADD yet to the fierce anger" — Isaiah 30:1's "to add sin to sin" the idiom's kin; "THE FIERCE ANGER OF THE LORD" — the
# phrase's Numbers seats PEOR'S (25:4) and this; "if you turn from after him he will again LEAVE THEM in the wilderness" one seat each; "and you
# will destroy all this people" one seat
assert phrase(['קמתם', 'תחת'], None) == ['Num 32:14'] and U('תרבות') == ['Num 32:14'] and phrase(['אנשים', 'חטאים'], None) == ['Num 32:14'] and U('חטאים', 'וחטאים', books=T) == ['Gen 13:13', 'Num 32:14'] and aramaic(32, 14)[4:7] == ['תלמידי', 'גבריא', 'חיביא']
assert U('לספות', 'ספות', 'ספו') == ['2Kgs 12:14', 'Deut 29:18', 'Isa 29:1', 'Isa 30:1', 'Jer 7:21', 'Num 32:14', 'Ps 73:19'] and words('Isa', 30, 1)[-4:] == ['ספות', 'חטאת', 'על', 'חטאת'] and phrase(['חרון', 'אף', 'יהוה'], None) == ['2Chr 28:11', 'Jer 25:37', 'Jer 30:24', 'Jer 4:8', 'Num 25:4', 'Num 32:14', 'Zeph 2:2'] and words('Num', 25, 4)[-6:] == ['השמש', 'וישב', 'חרון', 'אף', 'יהוה', 'מישראל']
assert phrase(['תשובן', 'מאחריו'], None) == ['Num 32:15'] and U('להניחו') == ['Num 32:15'] and U('ושחתם') == ['Num 32:15'] and phrase(['ושחתם', 'לכל', 'העם'], None) == ['Num 32:15'] and aramaic(32, 15)[6] == 'לאחרותהון'

# THE OFFER (32:16-19): "they drew near to him" one seat (the store "and-be"); THE ORDER OF THE TWO — the tribes name "folds for our CATTLE"
# before "cities for our LITTLE ONES" (32:16); Moses answers "cities for your LITTLE ONES" then "folds for your SHEEP" (32:24); their acceptance
# "our little ones, our wives, our cattle and all our beasts" (32:26); Moses' retelling "your wives, your little ones and your cattle" (Deuteronomy
# 3:19) and Joshua's (1:14) — the reversal COMPUTED on the token order, no row of the declared shelf reads it (the exam's Tanchuma outside scope);
# "the fortified cities" here and Jehoshaphat's; THE ARM-ROOT SEVEN TOKENS in the chapter (31:3's "arm yourselves" the root's Torah opening; the
# final letter its own code point, sitting 11's lesson — the count typed as a token set); "hastening" one seat (Hushim, Dan's son, the homograph);
# JOSHUA'S RUN USES "ARMED" IN ANOTHER WORD — "chamushim" (1:14; 4:12 "armed before the children of Israel as Moses spoke to them"), the consonants
# of "FIFTY" told apart by the points (the participle's u-vowel against the numeral's i-vowel, the morphology reading each); Joshua 4:13's "about
# forty thousand ARMED FOR THE HOST passed over BEFORE THE LORD" keeps 32:21's phrase and puts a number to it; 6:7 "the armed man before the ark
# of the LORD" concretizes it; "until we have brought them" one seat, "to their place" Isaiah's and this; "we will not return to our houses until
# the children of Israel HAVE INHERITED every man his inheritance" — the retellings' "until the LORD gives REST to your brothers as to you"
# (Deuteronomy 3:20, Joshua 1:15) and Joshua 22:4's release "now the LORD has given rest to your brothers as he spoke to them"; "beyond the
# Jordan and onward" one seat; "this side of the Jordan eastward" one; "our inheritance has come to us" one
assert phrase(['ויגשו', 'אליו'], None) == ['Num 32:16'] and phrase(['גדרת', 'צאן'], None) == ['Num 32:16'] and words('Num', 32, 16)[3:10] == ['גדרת', 'צאן', 'נבנה', 'למקננו', 'פה', 'וערים', 'לטפנו'] and words('Num', 32, 24)[:6] == ['בנו', 'לכם', 'ערים', 'לטפכם', 'וגדרת', 'לצנאכם'] and words('Num', 32, 26)[:5] == ['טפנו', 'נשינו', 'מקננו', 'וכל', 'בהמתנו'] and words('Deut', 3, 19)[1:4] == ['נשיכם', 'וטפכם', 'ומקנכם'] and words('Josh', 1, 14)[:3] == ['נשיכם', 'טפכם', 'ומקניכם']
assert phrase(['בערי', 'המבצר'], None) == ['2Chr 17:19', 'Num 32:17'] and phrase(['ערי', 'מבצר'], None) == ['Jer 34:7', 'Num 32:36'] and U('לצנאכם') == ['Num 32:24'] and phrase(['בנו', 'לכם', 'ערים'], None) == ['Num 32:24']
ARM = seats_in(lambda x, m: x in ('נחלץ', 'תחלצו', 'חלוץ', 'חלוצים'))
assert ARM == [(17, 'נחלץ'), (20, 'תחלצו'), (21, 'חלוץ'), (27, 'חלוץ'), (29, 'חלוץ'), (30, 'חלוצים'), (32, 'חלוצים')] and Counter(x for _, x in ARM) == Counter({'חלוץ': 3, 'חלוצים': 2, 'נחלץ': 1, 'תחלצו': 1}) and U('החלצו') == ['Num 31:3']
assert U('חשים') == ['Gen 46:23', 'Num 32:17'] and phrase(['נחלץ', 'חשים'], None) == ['Num 32:17'] and phrase(['חלוץ', 'צבא'], None) == ['Num 32:27'] and phrase(['חלוצי', 'הצבא'], None) == ['Josh 4:13'] and phrase(['כל', 'חלוץ'], None) == ['Num 32:21', 'Num 32:27', 'Num 32:29']
assert morphs('Josh', 1, 14)[words('Josh', 1, 14).index('חמשים')] == 'HVqsmpa' and morphs('Num', 4, 3)[words('Num', 4, 3).index('חמשים')] == 'HAcbpa' and 'ֻ' in byp[('Josh', 1, 14)][words('Josh', 1, 14).index('חמשים')] and 'ּ' not in byp[('Josh', 1, 14)][words('Josh', 1, 14).index('חמשים')] and 'ֻ' not in byp[('Num', 4, 3)][words('Num', 4, 3).index('חמשים')] and 'ּ' in byp[('Num', 4, 3)][words('Num', 4, 3).index('חמשים')]   # the u-vowel (qubuts, the three dots) under the mem of the armed and no doubling dot; the numeral's shin doubled (the dagesh, the dot inside) and no u-vowel — tested by code point, never by a retyped string (the marks' order); both words carry the i-vowel under the shin
assert words('Josh', 1, 14)[12:16] == ['תעברו', 'חמשים', 'לפני', 'אחיכם'] and words('Josh', 4, 12)[7:12] == ['המנשה', 'חמשים', 'לפני', 'בני', 'ישראל'] and words('Josh', 4, 12)[-5:] == ['כאשר', 'דבר', 'אליהם', 'משה'][-4:] + [] or words('Josh', 4, 12)[-4:] == ['כאשר', 'דבר', 'אליהם', 'משה']
assert words('Josh', 4, 13)[:7] == ['כארבעים', 'אלף', 'חלוצי', 'הצבא', 'עברו', 'לפני', 'יהוה'] and words('Josh', 6, 7)[-5:] == ['והחלוץ', 'יעבר', 'לפני', 'ארון', 'יהוה'] and words('Deut', 3, 18)[13:17] == ['חלוצים', 'תעברו', 'לפני', 'אחיכם'] and morphs('Exod', 13, 18)[words('Exod', 13, 18).index('וחמשים')] == 'HC/Vqsmpa'
assert phrase(['עד', 'אשר', 'אם'], None) == ['Gen 28:15', 'Isa 6:11', 'Num 32:17'] and U('הביאנם') == ['Num 32:17'] and phrase(['אל', 'מקומם'], None) == ['Isa 14:2', 'Num 32:17'] and phrase(['מפני', 'ישבי', 'הארץ'], None) == ['Num 32:17'] and words('Gen', 28, 15)[-8:-4] == ['עד', 'אשר', 'אם', 'עשיתי']
assert phrase(['לא', 'נשוב', 'אל', 'בתינו'], None) == ['Num 32:18'] and U('התנחל') == ['Num 32:18'] and phrase(['איש', 'נחלתו'], None) == ['Num 32:18'] and words('Deut', 3, 20)[:6] == ['עד', 'אשר', 'יניח', 'יהוה', 'לאחיכם', 'ככם'] and words('Josh', 1, 15)[:6] == ['עד', 'אשר', 'יניח', 'יהוה', 'לאחיכם', 'ככם'] and words('Josh', 22, 4)[:8] == ['ועתה', 'הניח', 'יהוה', 'אלהיכם', 'לאחיכם', 'כאשר', 'דבר', 'להם']
assert phrase(['מעבר', 'לירדן', 'והלאה'], None) == ['Num 32:19'] and len(phrase(['מעבר', 'לירדן'], None)) == 11 and phrase(['מעבר', 'הירדן', 'מזרחה'], None) == ['Num 32:19'] and phrase(['באה', 'נחלתנו'], None) == ['Num 32:19'] and phrase(['לא', 'ננחל', 'אתם'], None) == ['Num 32:19']

# THE CONDITION DOUBLED (32:20-24): eight "if" tokens in the chapter, and TWO DOUBLED CONDITIONS — Moses to the tribes "IF you do this thing...
# and IF you do NOT do so" (32:20, 23) and Moses to the commission "IF they pass over... and IF they do NOT pass over" (32:29, 30), each clause
# one seat — the exam's Mishnah Kiddushin 3:4 (the stipulation must be doubled, as Gad and Reuben's) the compile's docket, cited forward by the
# vows' docket at 10b; "before the LORD" seven times; "until he has driven out his enemies before him" one seat ("did not drive out" the verb's
# Joshua-Judges seats — the failures); "and the land is subdued before the LORD" 32:22, 29 and 1 Chronicles 22:18; "and afterward you shall
# return" one seat; "AND YOU SHALL BE CLEAR BEFORE THE LORD AND BEFORE ISRAEL" one seat — Mishnah Shekalim 3:2's proof (the two Exodus dockets
# name it); David's "I and my kingdom are clear before the LORD forever" (2 Samuel 3:28) its kin; ONKELOS "acquitted"; "this land shall be yours
# for a possession before the LORD" one seat; "behold, you have sinned against the LORD" (Deuteronomy 9:16's phrase, Jeremiah's); "KNOW YOUR SIN
# WHICH WILL FIND YOU" one seat — Judah's "God has FOUND OUT the iniquity of your servants" (Genesis 44:16, the idiom's one other seat); THE
# UTTERANCE RULE'S SECOND SEAT — "AND THAT WHICH HAS GONE OUT OF YOUR MOUTH YOU SHALL DO" (32:24) is the vows' "all that goes out of his mouth
# he shall do" (30:3) in the plural, the phrase's two seats; Jephthah's daughter's "do to me as has gone out of your mouth" (Judges 11:36 —
# JEPHTHAH THE GILEADITE, the vow run in this chapter's land) and Deuteronomy 23:24's "that which has gone out of your lips" its kin; ONKELOS
# renders 32:24 in the vows' own Aramaic ("what goes out of your mouth you shall do" = 30:3's "what goes out of his mouth he shall do") —
# the utterance rule's seat 10b filed to this chapter's compile, paid at the reading
assert seats_in(lambda x, m: x in ('אם', 'ואם')) == [(5, 'אם'), (11, 'אם'), (17, 'אם'), (20, 'אם'), (20, 'אם'), (23, 'ואם'), (29, 'אם'), (30, 'ואם')] and phrase(['אם', 'תעשון', 'את', 'הדבר', 'הזה'], None) == ['Num 32:20'] and phrase(['אם', 'תחלצו'], None) == ['Num 32:20'] and phrase(['ואם', 'לא', 'תעשון', 'כן'], None) == ['Num 32:23'] and phrase(['אם', 'יעברו'], None) == ['Num 32:29'] and phrase(['ואם', 'לא', 'יעברו'], None) == ['Num 32:30']
assert phrase(['ועבר', 'לכם', 'כל', 'חלוץ'], None) == ['Num 32:21'] and phrase(['עד', 'הורישו', 'את', 'איביו'], None) == ['Num 32:21'] and U('הורישו') == ['Josh 13:13', 'Josh 16:10', 'Josh 17:13', 'Judg 1:21', 'Judg 1:28', 'Judg 1:32', 'Num 32:21']
assert phrase(['ואחר', 'תשבו'], None) == ['Num 32:22'] and phrase(['והייתם', 'נקיים'], None) == ['Num 32:22'] and phrase(['נקיים', 'מיהוה', 'ומישראל'], None) == ['Num 32:22'] and words('2Sam', 3, 28)[5:10] == ['נקי', 'אנכי', 'וממלכתי', 'מעם', 'יהוה'] and aramaic(32, 22)[9] == 'זכאין' and phrase(['הארץ', 'הזאת', 'לכם', 'לאחזה'], None) == ['Num 32:22'] and phrase(['לאחזה', 'לפני', 'יהוה'], None) == ['Num 32:22']
assert phrase(['הנה', 'חטאתם', 'ליהוה'], None) == ['Num 32:23'] and phrase(['חטאתם', 'ליהוה'], None) == ['Deut 9:16', 'Jer 40:3', 'Jer 44:23', 'Num 32:23'] and phrase(['חטאתכם', 'אשר', 'תמצא', 'אתכם'], None) == ['Num 32:23'] and phrase(['מצא', 'את', 'עון'], None) == ['Gen 44:16'] and words('Gen', 44, 16)[9:13] == ['האלהים', 'מצא', 'את', 'עון'] and aramaic(32, 23)[10:13] == ['די', 'תשכח', 'יתכון']
assert phrase(['והיצא', 'מפיכם', 'תעשו'], None) == ['Num 32:24'] and phrase(['ככל', 'היצא', 'מפיו', 'יעשה'], None) == ['Num 30:3'] and phrase(['היצא', 'מפיו'], None) == ['Num 30:3'] and phrase(['יצא', 'מפיך'], None) == ['Judg 11:36'] and words('Judg', 11, 36)[8:13] == ['עשה', 'לי', 'כאשר', 'יצא', 'מפיך'] and words('Deut', 23, 24)[:4] == ['מוצא', 'שפתיך', 'תשמר', 'ועשית'] and phrase(['מוצא', 'שפתיך'], None) == ['Deut 23:24']
assert aramaic(32, 24)[6:9] == ['ודיפוק', 'מפומכון', 'תעבדון'] and aramaic(30, 3)[-4:] == ['ככל', 'דיפוק', 'מפומיה', 'יעבד'] and words('Num', 30, 3)[-4:] == ['ככל', 'היצא', 'מפיו', 'יעשה']

# THE ACCEPTANCE AND THE COMMISSION (32:25-32): "your servants will do as MY LORD commands" — Moses called "my lord" by Joshua (11:28), Aaron
# (12:11), the two tribes (32:25, 27) and the Gileadite heads (36:2); the four (little ones, wives, cattle, beasts) "in the cities of Gilead" one
# seat; "every armed man of the host" one; MOSES CHARGES ELEAZAR, JOSHUA AND THE HEADS OF THE FATHERS OF THE TRIBES — THE COMMISSION THAT
# DIVIDES THE LAND, named word for word at Joshua 14:1 and 21:1 (the phrase's two seats beside this); "he commanded concerning them" one seat;
# the second doubled condition; "they shall have possessions among you in the land of Canaan" one seat (Hamor's "and get possessions in it",
# Genesis 34:10, its kin); "THEY ANSWERED: what the LORD has spoken to your servants, so will we do" — the LORD has not spoken in the chapter:
# Moses' stipulation called the LORD's word (Joshua 22:9's "by the commandment of the LORD by the hand of Moses" the run's own reading); "so
# will we do" — the Gileadites' word to Jephthah (Judges 11:10) among its four seats; "WE" in its short form at three Bible seats — Joseph's
# brothers' "we are all one man's sons" (Genesis 42:11), Lamentations 3:42 and this; "the possession of our inheritance" — the daughters' phrase
# (27:7 "a possession of inheritance") in the construct at two Torah seats
assert phrase(['עבדיך', 'יעשו', 'כאשר', 'אדני', 'מצוה'], None) == ['Num 32:25'] and phrase(['כאשר', 'אדני', 'דבר'], None) == ['Num 32:27'] and [s for s in U('אדני') if s.startswith('Num')] == ['Num 11:28', 'Num 12:11', 'Num 14:17', 'Num 32:25', 'Num 32:27', 'Num 36:2'] and words('Num', 36, 2)[:4] == ['ויאמרו', 'את', 'אדני', 'צוה']
assert phrase(['טפנו', 'נשינו', 'מקננו'], None) == ['Num 32:26'] and phrase(['בערי', 'הגלעד'], None) == ['Num 32:26'] and phrase(['ערי', 'הגלעד'], None) == ['Josh 13:25']
assert phrase(['ויצו', 'להם', 'משה'], None) == ['Num 32:28'] and phrase(['ראשי', 'אבות', 'המטות', 'לבני', 'ישראל'], None) == ['Josh 21:1', 'Num 32:28'] and words('Josh', 14, 1)[10:20] == ['אלעזר', 'הכהן', 'ויהושע', 'בן', 'נון', 'וראשי', 'אבות', 'המטות', 'לבני', 'ישראל'] and words('Num', 32, 28)[3:] == ['את', 'אלעזר', 'הכהן', 'ואת', 'יהושע', 'בן', 'נון', 'ואת', 'ראשי', 'אבות', 'המטות', 'לבני', 'ישראל']
assert U('ונאחזו') == ['Num 32:30'] and phrase(['ונאחזו', 'בתככם'], None) == ['Num 32:30'] and words('Gen', 34, 10)[-2:] == ['והאחזו', 'בה'] and seats_in(lambda x, m: x == 'כנען') == [(30, 'כנען'), (32, 'כנען')]
assert phrase(['ויענו', 'בני', 'גד'], None) == ['Num 32:31'] and phrase(['את', 'אשר', 'דבר', 'יהוה', 'אל', 'עבדיך'], None) == ['Num 32:31'] and phrase(['כן', 'נעשה'], None) == ['Jer 42:5', 'Judg 11:10', 'Neh 5:12', 'Num 32:31'] and aramaic(32, 31)[6:10] == ['ית', 'די', 'מליל', 'יי']
assert U('נחנו') == ['Gen 42:11', 'Lam 3:42', 'Num 32:32'] and phrase(['נחנו', 'נעבר'], None) == ['Num 32:32'] and words('Josh', 22, 9)[-5:] == ['על', 'פי', 'יהוה', 'ביד', 'משה'] and words('Josh', 22, 2)[3:11] == ['שמרתם', 'את', 'כל', 'אשר', 'צוה', 'אתכם', 'משה', 'עבד']

# THE GRANT AND THE CITIES (32:33-38): "Moses gave to them" — to Gad, to Reuben AND TO HALF THE TRIBE OF MANASSEH, first named at the grant (its
# four tokens in the chapter all from 32:33 on; the half-tribe phrase's nineteen Bible seats, 34:14-15 the next); "the kingdom of Sihon" one
# seat, "the kingdom of Og" Deuteronomy 3's and this ("Heshbon was the city of Sihon", 21:26); "the land with its cities in the borders" — three
# one-seat words; ONKELOS "Mathnan" for Bashan; GAD BUILT EIGHT (Dibon, Ataroth, Aroer, Atroth Shophan, Jazer, Jogbehah, Beth Nimrah, Beth
# Haran) and REUBEN SIX (Heshbon, Elealeh, Kiriathaim, Nebo, Baal Meon, Sibmah): the NINE asked at 32:3 split four to Gad (Ataroth, Dibon,
# Jazer, Nimrah) and five to Reuben (Heshbon, Elealeh, Sebam, Nebo, Beon — the last three respelled Sibmah, Nebo, Baal Meon), Kiriathaim and
# four of Gad's new; "their names being changed" one seat (Onkelos "encircled"); "they called by names the names of the cities" one; the
# itinerary's own witness "DIBON GAD" (33:45, 46); THE TWO CROSSED CITIES in Joshua's allotment — Dibon in REUBEN'S list (13:17) and Heshbon on
# GAD'S border (13:26; 21:39 a Levite city "from Gad"), against 32:34 and 32:37; Beth Peor in Reuben's list (13:20 — where Moses was buried,
# Deuteronomy 34:6); THE PROPHETS NAME TEN OF THE CHAPTER'S CITIES AS MOAB'S — Nebo, Kiriathaim, Heshbon, Elealeh, Sibmah, Dibon, Jazer, Aroer,
# Beth Meon, the waters of Nimrim (Isaiah 15-16, Jeremiah 48, Ezekiel 25:9) and 1 Chronicles 5:8 seats Reuben "at Aroer as far as Nebo and Baal
# Meon"; Beon, Atroth Shophan, Beth Haran and Beth Nimrah one seat each (Joshua 13:27 spelling Beth Haram); NOBAH AND JOGBEHAH stand together at
# Judges 8:11 — Gideon's route "east of Nobah and Jogbehah" against MIDIAN, the two names' only other seat
assert phrase(['ויתן', 'להם', 'משה'], None) == ['Num 32:33'] and phrase(['ולחצי', 'שבט', 'מנשה'], None) == ['1Chr 5:26', 'Num 32:33'] and seats_in(lambda x, m: x == 'מנשה') == [(33, 'מנשה'), (39, 'מנשה'), (40, 'מנשה'), (41, 'מנשה')] and words('Num', 34, 15)[:5] == ['שני', 'המטות', 'וחצי', 'המטה', 'לקחו']
HALF = sorted({f"{b} {c}:{v}" for (b, c, v), ws in by.items() for w in [[x for x, _ in ws]] for i in range(len(w) - 2) if w[i] in ('חצי', 'לחצי', 'ולחצי', 'וחצי') and w[i + 1] == 'שבט' and w[i + 2] in ('מנשה', 'המנשה')})
assert len(HALF) == 19 and HALF[-1] == 'Num 32:33' and 'Deut 3:13' in HALF and 'Josh 1:12' in HALF and 'Josh 22:7' in HALF
assert phrase(['ממלכת', 'סיחן'], None) == ['Num 32:33'] and phrase(['ממלכת', 'עוג'], None) == ['Deut 3:10', 'Deut 3:13', 'Deut 3:4', 'Num 32:33'] and words('Num', 21, 26)[:7] == ['כי', 'חשבון', 'עיר', 'סיחן', 'מלך', 'האמרי', 'הוא'] and aramaic(32, 33)[21] == 'דמתנן'
assert U('לעריה') == ['Num 32:33'] and U('בגבלת') == ['Num 32:33'] and phrase(['ערי', 'הארץ', 'סביב'], None) == ['Num 32:33']
assert words('Num', 32, 34)[3:] == ['את', 'דיבן', 'ואת', 'עטרת', 'ואת', 'ערער'] and words('Num', 32, 35) == ['ואת', 'עטרת', 'שופן', 'ואת', 'יעזר', 'ויגבהה'] and words('Num', 32, 36) == ['ואת', 'בית', 'נמרה', 'ואת', 'בית', 'הרן', 'ערי', 'מבצר', 'וגדרת', 'צאן']
assert words('Num', 32, 37)[3:] == ['את', 'חשבון', 'ואת', 'אלעלא', 'ואת', 'קריתים'] and words('Num', 32, 38)[:9] == ['ואת', 'נבו', 'ואת', 'בעל', 'מעון', 'מוסבת', 'שם', 'ואת', 'שבמה']
assert words('Num', 33, 45)[-2:] == ['בדיבן', 'גד'] and words('Num', 33, 46)[1:3] == ['מדיבן', 'גד']
assert words('Josh', 13, 17) == ['חשבון', 'וכל', 'עריה', 'אשר', 'במישר', 'דיבון', 'ובמות', 'בעל', 'ובית', 'בעל', 'מעון'] and words('Josh', 13, 19)[:2] == ['וקריתים', 'ושבמה'] and words('Josh', 13, 20)[:2] == ['ובית', 'פעור'] and words('Josh', 13, 25)[:5] == ['ויהי', 'להם', 'הגבול', 'יעזר', 'וכל'] and words('Josh', 13, 25)[11:13] == ['עד', 'ערוער'] and words('Josh', 13, 26)[0] == 'ומחשבון' and words('Josh', 13, 27)[1:5] == ['בית', 'הרם', 'ובית', 'נמרה']
assert words('Josh', 13, 15) == ['ויתן', 'משה', 'למטה', 'בני', 'ראובן', 'למשפחתם'] and words('Josh', 13, 24)[:4] == ['ויתן', 'משה', 'למטה', 'גד'] and words('Deut', 34, 6)[:8] == ['ויקבר', 'אתו', 'בגי', 'בארץ', 'מואב', 'מול', 'בית', 'פעור']
assert words('Isa', 15, 2)[1:7] == ['הבית', 'ודיבן', 'הבמות', 'לבכי', 'על', 'נבו'] and words('Isa', 15, 4)[:3] == ['ותזעק', 'חשבון', 'ואלעלה'] and words('Isa', 15, 6)[:3] == ['כי', 'מי', 'נמרים'] and words('Isa', 16, 8)[1:6] == ['שדמות', 'חשבון', 'אמלל', 'גפן', 'שבמה'] and words('Isa', 16, 9)[4:6] == ['יעזר', 'גפן']
assert words('Jer', 48, 1)[8:10] == ['אל', 'נבו'] and words('Jer', 48, 1)[14] == 'קריתים' and words('Jer', 48, 18)[6] == 'דיבון' and words('Jer', 48, 19)[5] == 'ערוער' and words('Jer', 48, 22) == ['ועל', 'דיבון', 'ועל', 'נבו', 'ועל', 'בית', 'דבלתים'] and words('Jer', 48, 23)[:2] == ['ועל', 'קריתים'] and words('Jer', 48, 23)[-2:] == ['בית', 'מעון'] and words('Jer', 48, 32)[1] == 'יעזר' and words('Jer', 48, 32)[5] == 'שבמה' and words('Jer', 48, 34)[1:4] == ['חשבון', 'עד', 'אלעלה']
assert words('Ezek', 25, 9)[-3:] == ['בעל', 'מעון', 'וקריתמה'] and words('1Chr', 5, 8)[-5:] == ['בערער', 'ועד', 'נבו', 'ובעל', 'מעון']
assert words('Judg', 8, 11)[6:8] == ['לנבח', 'ויגבהה'] and U('יגבהה', 'ויגבהה') == ['Judg 8:11', 'Num 32:35'] and U('נבח') == ['Num 32:42'] and U('לנבח') == ['Isa 56:10', 'Judg 8:11'] and U('קנת') == ['1Chr 2:23', 'Num 32:42']
assert U('דיבן', 'ודיבן', 'דיבון', 'מדיבן') == ['Isa 15:2', 'Jer 48:18', 'Jer 48:22', 'Josh 13:17', 'Josh 13:9', 'Num 21:30', 'Num 32:3', 'Num 32:34', 'Num 33:46'] and U('נמרה', 'ונמרה') == ['Josh 13:27', 'Num 32:3', 'Num 32:36'] and U('אלעלה', 'ואלעלה', 'אלעלא', 'ואלעלא') == ['Isa 15:4', 'Isa 16:9', 'Jer 48:34', 'Num 32:3', 'Num 32:37']
assert U('בען', 'ובען') == ['Num 32:3'] and phrase(['בעל', 'מעון'], None) == ['Ezek 25:9', 'Josh 13:17', 'Num 32:38'] and phrase(['בית', 'מעון'], None) == ['Jer 48:23'] and U('קריתים', 'וקריתים', 'קריתימה') == ['1Chr 6:61', 'Gen 14:5', 'Jer 48:1', 'Jer 48:23', 'Josh 13:19', 'Num 32:37'] and U('שופן') == ['Num 32:35'] and phrase(['בית', 'הרן'], None) == ['Num 32:36'] and phrase(['בית', 'הרם'], None) == ['Josh 13:27'] and phrase(['בית', 'נמרה'], None) == ['Num 32:36']
assert U('שבמה', 'ושבמה') == ['Isa 16:8', 'Isa 16:9', 'Jer 48:32', 'Josh 13:19', 'Num 32:38'] and U('שבם', 'ושבם') == ['Jer 43:12', 'Num 32:3'] and U('ערער', 'וערער', 'מערער', 'בערער') == ['1Chr 5:8', '1Sam 30:28', '2Kgs 10:33', 'Deut 2:36', 'Deut 3:12', 'Deut 4:48', 'Isa 17:2', 'Jer 51:58', 'Num 32:34']
assert phrase(['מוסבת', 'שם'], None) == ['Num 32:38'] and U('מוסבת') == ['Exod 39:13', 'Num 32:38'] and phrase(['ויקראו', 'בשמת'], None) == ['Num 32:38'] and phrase(['שמות', 'הערים'], None) == ['Num 32:38'] and aramaic(32, 38)[5:7] == ['מקפן', 'שמהן'] and aramaic(32, 35)[5] == 'ורמתא'

# MACHIR, JAIR AND NOBAH (32:39-42): "the sons of Machir son of Manasseh" — born on Joseph's knees (Genesis 50:23) and this, the phrase's two
# seats; Machir's Gilead the clan of 26:29 ("Machir begot Gilead"); Joshua 17:1 "Machir the firstborn of Manasseh, the father of Gilead, for he was
# a man of war"; Deuteronomy 3:15 "to Machir I gave Gilead"; "to Gilead" with the directional ending here and 1 Chronicles 27:21; "and dispossessed
# the Amorite" one seat; "Moses gave Gilead to Machir" one; JAIR "son of Manasseh" (Deuteronomy 3:14, 1 Kings 4:13) whom 1 Chronicles 2:21-22
# makes HEZRON'S grandson by Machir's daughter — Judah's line, twenty-three cities, Kenath and its villages, sixty — the genealogy's delta, the
# ink's own two accounts; HAVVOTH JAIR six seats (Judges 10:4's Jair the Gileadite renaming thirty, "to this day"); "their villages" one seat;
# "went and took" (the perfect then the narrative form) 32:41, 42 alone; Nobah "called it Nobah after his name" — the naming after oneself
# (Absalom's pillar, David's city its kin); "and its daughters" — Jazer's (21:32) and Heshbon's (21:25) villages, Onkelos "its villages"
assert phrase(['בני', 'מכיר', 'בן', 'מנשה'], None) == ['Gen 50:23', 'Num 32:39'] and phrase(['מכיר', 'בן', 'מנשה'], None) == ['1Chr 7:17', 'Gen 50:23', 'Josh 13:31', 'Josh 17:3', 'Num 27:1', 'Num 32:39', 'Num 36:1'] and words('Gen', 50, 23)[6:13] == ['בני', 'מכיר', 'בן', 'מנשה', 'ילדו', 'על', 'ברכי']
assert words('Num', 26, 29)[5:9] == ['ומכיר', 'הוליד', 'את', 'גלעד'] and words('Josh', 17, 1)[8:13] == ['למכיר', 'בכור', 'מנשה', 'אבי', 'הגלעד'] and words('Josh', 17, 1)[15:18] == ['היה', 'איש', 'מלחמה'] and words('Deut', 3, 15) == ['ולמכיר', 'נתתי', 'את', 'הגלעד']
assert U('גלעדה') == ['1Chr 27:21', 'Num 32:39'] and phrase(['ויורש', 'את', 'האמרי'], None) == ['Num 32:39'] and U('ויורש') == ['Josh 23:9', 'Judg 1:20', 'Num 32:39'] and phrase(['ויתן', 'משה', 'את', 'הגלעד'], None) == ['Num 32:40'] and U('וילכדה')[-1] == 'Num 32:39' and len(U('וילכדה')) == 11
assert phrase(['חות', 'יאיר'], None) == ['1Chr 2:23', '1Kgs 4:13', 'Deut 3:14', 'Josh 13:30', 'Judg 10:4', 'Num 32:41'] and U('חותיהם') == ['Num 32:41'] and phrase(['הלך', 'וילכד'], None) == ['Num 32:41', 'Num 32:42'] and phrase(['יאיר', 'בן', 'מנשה'], None) == ['1Kgs 4:13', 'Deut 3:14'] and words('Deut', 3, 14)[12:20] == ['ויקרא', 'אתם', 'על', 'שמו', 'את', 'הבשן', 'חות', 'יאיר']
assert words('1Chr', 2, 21)[:7] == ['ואחר', 'בא', 'חצרון', 'אל', 'בת', 'מכיר', 'אבי'] and words('1Chr', 2, 22) == ['ושגוב', 'הוליד', 'את', 'יאיר', 'ויהי', 'לו', 'עשרים', 'ושלוש', 'ערים', 'בארץ', 'הגלעד'] and words('1Chr', 2, 23)[:9] == ['ויקח', 'גשור', 'וארם', 'את', 'חות', 'יאיר', 'מאתם', 'את', 'קנת'] and words('Judg', 10, 3)[2:4] == ['יאיר', 'הגלעדי'] and words('Judg', 10, 4)[12:15] == ['יקראו', 'חות', 'יאיר']
assert phrase(['ויקרא', 'לה', 'נבח', 'בשמו'], None) == ['Num 32:42'] and [s for s in U('בנתיה', 'ובנתיה') if s.startswith('Num')] == ['Num 21:25', 'Num 21:32', 'Num 32:42'] and aramaic(32, 42)[6] == 'כפרנהא' and aramaic(32, 41)[6] == 'כפרניהון' and phrase(['ויקרא', 'לה'], None) == ['2Kgs 4:12', '2Kgs 4:15', '2Sam 18:18', '2Sam 5:9', 'Num 32:42']

# THE ORDER OF THE TWO TRIBES (computed): the chapter opens "Reuben and Gad" (32:1) and then says "GAD AND REUBEN" six times (32:2, 6, 25, 29, 31,
# 33 — and the built cities Gad's first, 32:34); every other seat of the pair in the Bible puts REUBEN first — Deuteronomy 3:12, 16, 29:7, Joshua's
# fourteen seats (1:12; 4:12; 12:6; 13:8; 22:1, 9, 10, 21, 25, 30-34), 34:14, 1 Chronicles 5:26 — but 2 Kings 10:33 ("the Gadites and the
# Reubenites", Hazael's conquest); the Sifrei's two rows quote 32:1 with GAD FIRST (the rows' own word order against the verse's)
def order(b, c, v):
    w = words(b, c, v); r = [i for i, x in enumerate(w) if 'ראובן' in x or x in ('לראובני', 'ולראובני', 'הראובני', 'והראובני')]; g = [i for i, x in enumerate(w) if x in ('גד', 'לגדי', 'ולגדי', 'הגדי', 'והגדי')]
    return ('R<G' if r[0] < g[0] else 'G<R') if r and g else None
assert {v: order('Num', 32, v) for v in range(1, NV + 1) if order('Num', 32, v)} == {1: 'R<G', 2: 'G<R', 6: 'G<R', 25: 'G<R', 29: 'G<R', 31: 'G<R', 33: 'G<R'}
assert [order('Deut', 3, 12), order('Deut', 3, 16), order('Deut', 29, 7), order('Num', 34, 14), order('1Chr', 5, 26), order('2Kgs', 10, 33)] == ['R<G', 'R<G', 'R<G', 'R<G', 'R<G', 'G<R'] and [order('Josh', c, v) for c, v in ((1, 12), (4, 12), (12, 6), (13, 8), (22, 1), (22, 9), (22, 10), (22, 21), (22, 25), (22, 30), (22, 31), (22, 32), (22, 33), (22, 34))] == ['R<G'] * 14

# THE RETELLINGS AND THE RUNS READ TO THEIR VERSES: Deuteronomy 3:12-20 (Moses' own — "armed before your BROTHERS" for "before the LORD", "I know
# you have much cattle", the "rest"); Joshua 1:12-18 ("remember the word which Moses commanded you"; "all that you have commanded us we will do");
# 4:12-13 (the crossing, about forty thousand); 22:1-9 (the release: "you have kept all that Moses commanded"; "divide the spoil with your
# brothers" — the Midian ledger's observed kin; "by the commandment of the LORD by the hand of Moses"); DEBORAH'S SONG runs Moses' question — "why
# did you SIT among the SHEEPFOLDS to hear the pipings of the flocks?" (Judges 5:16, Reuben; 5:17 "Gilead abode beyond the Jordan") against "will
# you SIT here?" (32:6) and "folds for our flocks" (32:16): the sheepfolds' word Issachar's (Genesis 49:14) and this; 1 Chronicles 5:25-26 the
# exile of the two and a half first; Psalm 60:9 "Gilead is mine, Manasseh is mine"; Deuteronomy 33:20-21 Gad's blessing ("the lawgiver's portion
# hidden" — the Sifrei 106:1's proof for Moses' grave in Gad's land, against Deuteronomy 34:6's "opposite Beth Peor" — Reuben's city at Joshua
# 13:20: OBSERVED, the exam's business); 34:1 Moses on Nebo shown "Gilead as far as Dan"
assert words('Judg', 5, 16)[:6] == ['למה', 'ישבת', 'בין', 'המשפתים', 'לשמע', 'שרקות'] and U('המשפתים') == ['Gen 49:14', 'Judg 5:16'] and words('Judg', 5, 17)[:4] == ['גלעד', 'בעבר', 'הירדן', 'שכן'] and morphs('Judg', 5, 16)[1] == 'HVqp2ms'
assert words('Josh', 1, 13)[:9] == ['זכור', 'את', 'הדבר', 'אשר', 'צוה', 'אתכם', 'משה', 'עבד', 'יהוה'] and words('Josh', 1, 16)[4:8] == ['כל', 'אשר', 'צויתנו', 'נעשה'] and words('Josh', 22, 8)[-5:] == ['חלקו', 'שלל', 'איביכם', 'עם', 'אחיכם']
assert words('Deut', 33, 21)[:8] == ['וירא', 'ראשית', 'לו', 'כי', 'שם', 'חלקת', 'מחקק', 'ספון'] and words('Deut', 34, 1)[4:8] == ['אל', 'הר', 'נבו', 'ראש'] and words('Deut', 34, 1)[18:21] == ['את', 'הגלעד', 'עד'] and words('Ps', 60, 9)[:4] == ['לי', 'גלעד', 'ולי', 'מנשה'] and words('1Chr', 5, 26)[14:19] == ['ויגלם', 'לראובני', 'ולגדי', 'ולחצי', 'שבט']

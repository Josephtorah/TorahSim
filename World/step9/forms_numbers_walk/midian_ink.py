#!/usr/bin/env python3
# THE NUMBERS WALK, sitting 11 — MIDIAN, Numbers 31:1-54 (2026-09-12; the owner: "ok go" after the recovery-file rereads, on the ruling READ
# THEN COMPILE): THE INK of the chapter, computed from the Tanakh DB, the snapshot store and the shelf's own bytes — never typed. Sitting 10's
# form (vows_ink.py): the heads found BY POSITION and asserted; coverage computed; every cut by consonants (the misses collected, asserted
# empty); the engine's numeral parser MEASURED on every verse of the chapter (the spoil's census, the halves, the tributes, the shekels — and
# the FRACTION class at 31:28, 31:30, 31:47 named); the hand's facts as asserts, run all at once by assert_driver.py after the measurement pass
# (midian_measure1.py) printed them; every gloss of a narrative verb the STORE'S OWN (words.gloss); the piece-wise cutters HP / AP. Shared by
# midian_rows_onkelos_a.py / _b.py, midian_rows_sifrei.py and write_midian_ledger.py.
# THE SPAN: ONE draft — num_31_midian 31:1-54 (the portion Matot's second chapter); the next draft (num_32_gad_reuben) opens at 32:1.
import json, os, re, html, sqlite3, sys, io, contextlib, unicodedata
from collections import Counter
ROOT = '<repo-old>'
DATE = '2026-09-12'
UID = 'num_31_midian'
PISKAOT = [157, 158]
TITLE = 'Midian — the vengeance commanded and Moses\' death sequenced after it; a thousand a tribe, Phinehas with the holy vessels and the trumpets; the five kings and Balaam by the sword; the spoil brought to the plains of Moab; Moses\' wrath, the women who knew a man killed, the little ones kept; seven days outside the camp with the heifer\'s water and the fire-passing of the six metals; the prey halved between the warriors and the congregation, one of five hundred to the priest and one of fifty to the Levites; the census of the spoil with its halves and tributes exact; the officers\' gold, none missing, to atone for their souls, a memorial before the LORD'
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
# THE SHELF'S ROWS ON CHAPTER 31, BY POSITION: TWO piskaot 157-158, TWELVE rows — 157 on 31:1 (nine rows: the leaders' praise and Moab's
# priority — the two dogs and the wolf; Moses' death contingent on the war and his zeal; 24,000 or 12,000 and the tribe of Levi; the righteous
# handed over; Phinehas weighed against them all, his mother's father; the ark and "his hand is his domain"; the four sides, the five kings one
# in counsel and one in punishment, Balaam's full reward and R. Natan's court; the cities and the castles; honest men against Achan; the youths
# snatching; the great bear the stigma; Balaam's counsel; the women fit for intercourse, the second "kill" — to close the subject, or no
# punishment by inference; the proselyte under three; the tent's straw excluded and the captives as covenant-children; garment-garment the freed
# identity with Leviticus 11:32; Moses' anger and his forgetting at three places, Eleazar's leave, "in the name of its sayer"), 158 on 31:22
# (three: vessels not lumps, "only" divides; the vessels of fire and of water, the gentiles' absorptions, the immersion a-fortiori; the sword
# unclean seven days, vessels-man-vessels, the camp and the evening likened both ways). NO row on 31:25-54 — the next head, 159, is 35:9: the
# shelf is SILENT from 31:25 to 35:8 (the division, the tribute, the census of the spoil, the officers' gold; chapters 32, 33, 34 whole).
assert heads[156] == ('Bamidbar', 30, 14) and heads[157] == ('Bamidbar', 31, 1) and heads[158] == ('Bamidbar', 31, 22) and heads[159] == ('Bamidbar', 35, 9), [heads[p] for p in (156, 157, 158, 159)]
assert sorted(p for p, h in heads.items() if h and h[0] == 'Bamidbar' and h[1] == 31) == PISKAOT and [p for p in range(150, 162) if heads.get(p) is None] == [] and len(sif) == 161
SIF_ROWS = {p: len(sif[p - 1]) for p in PISKAOT}
assert SIF_ROWS == {157: 9, 158: 3} and {p: len(sif_he[p - 1]) for p in PISKAOT} == SIF_ROWS, SIF_ROWS
assert sum(SIF_ROWS.values()) == 12
assert sorted(p for p, h in heads.items() if h and h[0] == 'Bamidbar' and h[1] in (32, 33, 34)) == [] and [p for p, h in heads.items() if h and h[0] == 'Bamidbar' and h[1] == 35 and h[2] < 9] == []
def head(p): return heads[p][1:]
def E(p, r): return clean(sif[p - 1][r - 1])
def Hb(p, r): return clean(sif_he[p - 1][r - 1])
# THE ROWS' HEADS CHECKED AGAINST THEIR OWN QUOTATIONS (the mistyped-head class): every row's first citation is its own verse, in order
ROW_CITES = [(p, r, re.search(r'\(Bamidbar (\d+):(\d+)', E(p, r)).groups()) for p in PISKAOT for r in range(1, SIF_ROWS[p] + 1)]
assert [(int(a), int(b)) for _, _, (a, b) in ROW_CITES] == [(31, 1), (31, 2), (31, 4), (31, 6), (31, 7), (31, 17), (31, 19), (31, 20), (31, 21), (31, 22), (31, 23), (31, 24)], ROW_CITES
# THE ROWS' OWN DEFECTS, read to their verses (RESEARCH_LOG.md): (a) 157:3's Hebrew reads "24,000 — the words of R. YISHMAEL; R. Akiva says:
# 12,000; why 'for all the tribes of Israel you shall send'? to INCLUDE the tribe of Levi" — the English DROPS the attribution, REVERSES R.
# Akiva's arm ("to exclude the tribe of Levi") and swaps his proof phrase ("and there were handed over"); (b) 157:4's Hebrew: Phinehas went to
# avenge "his mother's father", the proof Genesis 37:36 "and the Medanites sold him to Egypt" — Joseph; the English inserts "(Yithro, viz.
# Shemot 2:16)", a different ancestor with a citation the Hebrew lacks (the inserted-clause class), against its own proof text; and the proof
# text's word is "the MEDANITES" (מדנים), Keturah's other son (Genesis 25:2), not "the Midianites" (מדינים) of 37:28; (c) 157:5: R. Natan
# "by a COURT they killed him" (בבית דין) — the English supplies the Talmud's "four judicial death penalties" (Sanhedrin 106b); "Abba Chanin in
# the name of R. ELAZAR" — the English "R. Eliezer"; the Hebrew puts the idolatry on "their cities in their dwellings", the English (with
# Onkelos) on "their castles"; (d) 157:6: the English cites "(31:7)" for the second "kill" of 31:17; and the English DROPS THE SECOND READING
# — the a-fortiori refused because "we do not punish by inference" (אין עונשים מן הדין — a rule about rules) — and drops R. Yishmael's name;
# (e) 157:7: the English replaces the Hebrew's conclusion ("they do not come into the category of uncleanness") with "(see Chukath #126)";
# (f) 157:8: the Hebrew runs the identity's first leg "as the garment said THERE has goat-work like sack, so the garment HERE" — but goat-work
# is 31:20's word, not Leviticus 11:32's; the English runs it "here → there", the direction the ink allows; (g) 157:9: the English drops R.
# YOSHIYAH's name on "in the name of its sayer"; (h) 158:2: the English supplies the Mishnah's whitening/boiling split (Avodah Zarah 5:12)
# where the Hebrew lists five vessels under "comes into the fire" with no split, and gives one a-fortiori for the Hebrew's two; (i) 158:3: the
# Hebrew misquotes 31:24 as "and they shall wash their garments" (8:7's form) for "and you shall wash your garments"; its citation "(19:19)
# 'slain by the sword'" names 19:16's phrase; the English cites "Vayikra 19:19" for Bamidbar 19:19 (a book wrong, as sitting 8's Judges for Joshua).
assert '24,000 all together' in E(157, 3) and 'To exclude the tribe of Levi' in E(157, 3) and 'Yishmael' not in E(157, 3) and "דברי ר' ישמעאל" in Hb(157, 3) and 'להביא את שבטו של לוי' in Hb(157, 3) and 'י"ב אלף' in Hb(157, 3) and 'כ"ד אלף' in Hb(157, 3)
assert '(Yithro, viz. Shemot 2:16)' in E(157, 4) and 'אבי אמו' in Hb(157, 4) and '(בראשית לז) והמדנים מכרו אותו למצרים' in Hb(157, 4) and 'יתרו' not in Hb(157, 4) and 'שמות ב' not in Hb(157, 4)
assert 'With the four judicial death penalties' in E(157, 5) and 'בב"ד הרגוהו' in Hb(157, 5) and 'Abba Channan says in the name of R. Eliezer' in E(157, 5) and 'אבא חנין אומר משום רבי אלעזר' in Hb(157, 5)
assert 'tirotham": This refers to their houses of idolatry' in E(157, 5) and 'זו ע"ז שלהם' in Hb(157, 5) and Hb(157, 5).index('עריהם במושבותם') < Hb(157, 5).index('זו ע"ז שלהם') < Hb(157, 5).index('טירותם')
assert '(31:7) "kill": Why is this (second "kill") mentioned?' in E(157, 6) and 'שאין עונשים מן הדין' in Hb(157, 6) and "דברי ר' ישמעאל" in Hb(157, 6) and 'Yishmael' not in E(157, 6) and 'unish' not in E(157, 6)
assert '(see Chukath #126)' in E(157, 7) and 'לא בא לכלל טומאה' in Hb(157, 7) and 'category' not in E(157, 7)
assert 'מה בגד האמור להלן עשה בו כל מעשה עזים כשק' in Hb(157, 8) and 'Just as here, every work of goats is likened to sack, so, there' in E(157, 8)
assert "ר' יאשיה אמר" in Hb(157, 9) and 'Yoshiya' not in E(157, 9) and 'He said the thing in the name of its sayer' in E(157, 9) and 'R. Elazar says: In three places' in E(157, 9) and "ר' אלעזר אומר: בג' מקומות" in Hb(157, 9)
assert 'are whitened in fire' in E(158, 2) and 'are to be boiled' in E(158, 2) and 'הלכוסין והסכינים והקדירות והשפודים והאסכלות' in Hb(158, 2) and 'גיעולי גוים' in Hb(158, 2) and 'ליבון' not in Hb(158, 2) and Hb(158, 2).count('ק"ו') == 2
assert 'תלמוד לומר "וכבסו בגדיהם"' in Hb(158, 3) and 'י״ט:י״ט' in Hb(158, 3) and 'בחלל חרב' in Hb(158, 3) and '(vis-à-vis the red heifer, Vayikra 19:19)' in E(158, 3)
assert '(Bamidbar 22:4)' in E(157, 1) and '(במדבר כב) וילכו זקני מואב' in Hb(157, 1) and 'כב:ד' not in Hb(157, 1)
def plain(w): return ''.join(c for c in w if c != '/' and not (0x0591 <= ord(c) <= 0x05C7))
def pointed(w): return ''.join(c for c in w if c != '/' and not (0x0591 <= ord(c) <= 0x05AF))
ONK_LEN = {c: len(onk[c - 1]) for c in (30, 31, 32)}
assert ONK_LEN == {30: 17, 31: 54, 32: 42} and {c: len(onk_he[c - 1]) for c in (30, 31, 32)} == ONK_LEN, ONK_LEN
def onk_ev(c, v): return clean(onk[c - 1][v - 1]), clean(onk_he[c - 1][v - 1])
shelf_numbers = sorted(d for d in os.listdir(f'{ROOT}/Data/sefaria_export') if re.search(r'Numbers|Bamidbar', d))
outside = [d for d in shelf_numbers if d not in ('Sifrei_Bamidbar', 'Onkelos_Numbers')]
assert len(outside) == 23, len(outside)
# THE PRIOR READS: no ledger has read an Onkelos row of 31, none a Sifrei row of 157-158 (eight ledgers NAME verses of chapter 31 as
# cross-references — a name is not a read); the Chukat ledger's rows on 19:14-22 (Sifrei 126:1, 127:1, 130:1) speak of the Midian vessels and
# the sword (31:20, 31:24) — rows of ANOTHER chapter, quick-looked (credit guard 1), no row of 157-158 credited: FRESH throughout
TRI = f'{ROOT}/logic/oral_triage'
LED = {f: open(f'{TRI}/{f}', encoding='utf-8').read() for f in os.listdir(TRI) if f.endswith('.md') and os.path.isfile(f'{TRI}/{f}') and f'{TRI}/{f}' != OUT}
assert sorted(f for f, t in LED.items() if re.search(r'^- Onkelos Num 31:\d', t, re.M)) == [] and sorted(f for f, t in LED.items() if re.search(r'Sifrei (?:Bamidbar )?15[78]:\d', t)) == []
NAMING = sorted(f for f, t in LED.items() if re.search(r'Num(?:bers)? 31:\d+', t))
assert len(NAMING) == 8 and 'num_19_parah_2026-09-11.md' in NAMING and 'lev_11_carcass_swarm_close_2026-09-05.md' in NAMING and 'num_27_zelophehad_joshua_2026-09-09.md' in NAMING, (len(NAMING), NAMING)
assert 'VESSELS-MAN-VESSELS FROM THE MIDIAN GARMENTS (31:24)' in LED['num_19_parah_2026-09-11.md'] and 'THE FOUR VESSELS OF THE MIDIAN SPOIL' in LED['num_19_parah_2026-09-11.md'] and 'goat-work clause (Num 31:20)' in LED['lev_11_carcass_swarm_close_2026-09-05.md']

# ---- THE DRAFT'S SPAN, COMPUTED ----
db = sqlite3.connect(f'file:{ROOT}/elijah_docket/tanakh.sqlite?mode=ro', uri=True)
VC = dict(db.execute("SELECT chapter, COUNT(*) FROM verses WHERE book='Num' GROUP BY chapter").fetchall())
assert VC[30] == 17 and VC[31] == 54 and VC[32] == 42 and VC[33] == 56 and VC[34] == 29
SILENT = (VC[31] - 24) + VC[32] + VC[33] + VC[34] + 8
assert SILENT == 165   # the shelf's silence from 31:25 to 35:8, computed
def unit_text(uid): return open(f'{ROOT}/logic/units/{uid}.yaml', encoding='utf-8').read()
def steps(uid): return sorted({(int(a), int(b)) for a, b in re.findall(r'STEP_Nm_(\d+)_(\d+)', unit_text(uid))})
assert steps(UID) == [(31, v) for v in range(1, 55)] and 'status: draft' in unit_text(UID) and 'operators:' not in unit_text(UID)
assert steps('num_32_gad_reuben')[0] == (32, 1) and 'status: frozen' in unit_text('num_30_vows')
SPAN = [(31, v) for v in range(1, 55)]

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
def count_tok(tok, books=None): return sum(1 for (b, c, v), ws in by.items() if (books is None or b in books) for x, _ in ws if x == tok)
def phrase(seq, books=T):
    out = []
    for (b, c, v), ws in by.items():
        if books is not None and b not in books: continue
        w = [x for x, _ in ws]
        if any(w[i:i + len(seq)] == list(seq) for i in range(len(w) - len(seq) + 1)): out.append(f'{b} {c}:{v}')
    return sorted(out)
def npt(s): return unicodedata.normalize('NFC', s) if isinstance(s, str) else s
def U(*toks, books=None): return sorted(set(s for t in toks for s in hits(t, books, True)))
def seats_in(pred): return [(v, x) for (c, v) in SPAN for x, m in by[('Num', 31, v)] if pred(x, m)]
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
for c, v, hp, g in store.execute("SELECT v.chapter, v.verse, w.he_plain, w.gloss FROM words w JOIN verses v ON w.verse_id=v.id WHERE v.book='Num' AND v.chapter = 31 ORDER BY v.id, w.idx"):
    SG.setdefault((c, v), []).append((hp.replace('/', ''), g))
def sg(c, v, tok):
    for hp, g in SG[(c, v)]:
        if hp == tok: return g
    raise KeyError((c, v, tok))

# THE ENGINE'S PARSER on every verse of the chapter — MEASURED before the compile is asked (the standing rule): RIGHT on the muster (31:4 the
# doubled "a thousand to a tribe" as two thousands — the distributive; 31:5 [1000, 12000]; 31:6 [1000]), the five kings (31:8 [5]), the
# schedule (31:19 [7] with the ordinals [3, 7]; 31:24 [7]), the spoil's census (675,000 / 72,000 / 61,000 / 32,000), the halves (337,500 /
# 36,000 / 30,500 / 16,000 at both seats), the tributes (675 / 72 / 61 / 32) and the shekels (16,750); the captains of "the thousands and the
# hundreds" (31:14, 48, 52, 54) rightly no number (census_probes G3, the old [2100] retired at 5b); NO starred homograph in the chapter; and
# SILENT WHERE THE STANDING RULE LEAVES THE RATIO'S DENOMINATOR — THE FRACTION CLASS "one of the N": 31:28 "one soul of the five hundred" [1],
# 31:30 and 31:47 "one held of the fifty" [1] — the class NAMED AND LEFT at census_probes R29 (the register-gate sitting); its Bible seats
# SIX (the three here, Ecclesiastes 7:28 "one of a thousand", Ezekiel 45:15 "one of the flock of the two hundred", Nehemiah 11:1 "one of the
# ten" — read [1, 9], the nine parts read and the ten not) — the compile's probe list
sys.path.insert(0, f'{ROOT}/World/step9')
with contextlib.redirect_stdout(io.StringIO()):
    import cold_run_sequence as CS
def N(b, c, v): return CS.ink_numbers(CS.verse_words(b, c, v))
def O(b, c, v): return CS.ink_ordinals(CS.verse_words(b, c, v))
PARSED = {v: N('Num', 31, v) for v in range(1, 55) if N('Num', 31, v)}
assert PARSED == {4: [1000, 1000], 5: [1000, 12000], 6: [1000], 8: [5], 19: [7], 28: [1], 30: [1], 32: [675000], 33: [72000], 34: [61000], 35: [32000], 36: [337500], 37: [675], 38: [36000, 72], 39: [30500, 61], 40: [16000, 32], 43: [337500], 44: [36000], 45: [30500], 46: [16000], 47: [1], 52: [16750]}, PARSED
assert {v: O('Num', 31, v) for v in range(1, 55) if O('Num', 31, v)} == {19: [3, 7], 24: [7]} and [(v, t) for v in range(1, 55) for t in CS.verse_words('Num', 31, v) if t.endswith('*')] == [] and N('Num', 32, 1) == [] and N('Num', 31, 54) == [] and N('Num', 31, 14) == []
FRACTION_SEATS = ['Eccl 7:28', 'Ezek 45:15', 'Neh 11:1', 'Num 31:28', 'Num 31:30', 'Num 31:47']
assert phrase(['אחד', 'נפש', 'מחמש', 'המאות'], None) == ['Num 31:28'] and phrase(['אחד', 'אחז', 'מן', 'החמשים'], None) == ['Num 31:30'] and phrase(['מן', 'החמשים'], None) == ['Num 31:30', 'Num 31:47'] and phrase(['אחד', 'מן', 'העשרה'], None) == ['Neh 11:1'] and phrase(['אחד', 'מאלף'], None) == ['Eccl 7:28'] and phrase(['מן', 'המאתים'], None) == ['Ezek 45:15']
assert N('Neh', 11, 1) == [1, 9] and N('Ezek', 45, 15) == [1] and N('Eccl', 7, 28) == [1]
assert morphs('Num', 31, 28)[10:12] == ['HR/Acfsa', 'HTd/Acbpa'] and words('Num', 31, 28)[8:12] == ['אחד', 'נפש', 'מחמש', 'המאות'] and words('Num', 31, 30)[4:8] == ['אחד', 'אחז', 'מן', 'החמשים'] and accents(byraw[('Num', 31, 28)][9]) == ['ZAQEF QATAN'] and accents(byraw[('Num', 31, 28)][10]) == ['TIPEHA']   # "one soul" closed by the zaqef; the denominator the next phrase
TOT = {k: N('Num', 31, v)[0] for k, v in (('sheep', 32), ('cattle', 33), ('donkeys', 34), ('persons', 35))}
HALF = {k: N('Num', 31, v)[0] for k, v in (('sheep', 36), ('cattle', 38), ('donkeys', 39), ('persons', 40))}
TRIB = {k: N('Num', 31, v)[-1] for k, v in (('sheep', 37), ('cattle', 38), ('donkeys', 39), ('persons', 40))}
CONG = {k: N('Num', 31, v)[0] for k, v in (('sheep', 43), ('cattle', 44), ('donkeys', 45), ('persons', 46))}
assert TOT == {'sheep': 675000, 'cattle': 72000, 'donkeys': 61000, 'persons': 32000} and all(TOT[k] % 1000 == 0 for k in TOT) and sum(TOT.values()) == 840000
assert all(HALF[k] * 2 == TOT[k] for k in TOT) and CONG == HALF and all(TRIB[k] * 500 == HALF[k] for k in TOT) and TRIB == {'sheep': 675, 'cattle': 72, 'donkeys': 61, 'persons': 32} and sum(TRIB.values()) == 840
LEVI = {k: HALF[k] // 50 for k in TOT}
assert LEVI == {'sheep': 6750, 'cattle': 720, 'donkeys': 610, 'persons': 320} and sum(LEVI.values()) == 8400 == 10 * sum(TRIB.values()) and all(HALF[k] % 50 == 0 for k in TOT)   # the Levites' shares the ink never states, computed
assert N('Num', 31, 52) == [16750] and N('Num', 31, 5) == [1000, 12000] and 1000 * 12 == 12000 and N('Num', 25, 9) == [24000] and N('Num', 11, 21) == [600000]

# THE FRAMES AND THE REGISTER: THIRTY narrative verbs in twenty-seven verses (computed on the morphology) — the chapter is a RUN with its two
# divine frames (31:1 "and the LORD spoke to Moses saying"; 31:25 "and the LORD said to Moses saying" — the said-saying frame's five Torah
# seats), Moses' relay (31:3 "and Moses spoke to the people saying" — one seat in the Bible), Eleazar's law (31:21 "and Eleazar the priest
# said" — one seat), and FOUR RECEIPTS "as the LORD commanded Moses" (31:7, 31, 41, 47) — the most of any Numbers chapter (Exodus 39 and 40
# carry seven each, Leviticus 8 five; 41 seats of the form in all); "and Moses was wroth" — the wrath-verb with Moses as its subject at three
# Torah seats (Exodus 16:20 the manna, Leviticus 10:16 the sin offering, 31:14) — the Sifrei 157:9's three places of anger-and-error (Leviticus
# 10:16, Numbers 20:10, 31:14) share two of them
REG = [(v, x, m) for (c, v) in SPAN for x, m in by[('Num', 31, v)] if m and re.search(r'V.w', m)]
assert len(REG) == 30 and len({v for v, _, _ in REG}) == 27 and [v for v, _, _ in REG if v in (7, 47, 54)] == [7, 7, 47, 47, 54, 54] and REG[0] == (1, 'וידבר', 'HC/Vpw3ms') and REG[-1] == (54, 'ויבאו', 'HC/Vhw3mp')
assert [(v, x) for v, x, _ in REG if x in ('ויאמר', 'ויאמרו', 'וידבר')] == [(1, 'וידבר'), (3, 'וידבר'), (15, 'ויאמר'), (21, 'ויאמר'), (25, 'ויאמר'), (49, 'ויאמרו')] and (50, 'ונקרב', 'HC/Vhw1cp') in REG
assert sg(31, 1, 'וידבר') == 'and-speak' and sg(31, 7, 'ויצבאו') == 'and-mass' and sg(31, 14, 'ויקצף') == 'and-crack-off' and sg(31, 5, 'וימסרו') == 'and-sunder'   # the store's own glosses: the wrath-verb glossed by its Strong's homonym
assert [(v, words('Num', 31, v)[:2]) for v in range(1, 55) if words('Num', 31, v)[:2] in (['וידבר', 'יהוה'], ['ויאמר', 'יהוה'])] == [(1, ['וידבר', 'יהוה']), (25, ['ויאמר', 'יהוה'])]
assert phrase(['ויאמר', 'יהוה', 'אל', 'משה', 'לאמר'], None) == ['Exod 31:12', 'Num 15:37', 'Num 27:6', 'Num 31:25', 'Num 7:4'] and len(phrase(['וידבר', 'יהוה', 'אל', 'משה', 'לאמר'])) == 70
assert phrase(['וידבר', 'משה', 'אל', 'העם'], None) == ['Num 31:3'] and phrase(['ויאמר', 'אלעזר', 'הכהן'], None) == ['Num 31:21'] and len(seats_in(lambda x, m: x in ('אלעזר', 'ואלעזר', 'לאלעזר'))) == 10
RECEIPT1 = phrase(['כאשר', 'צוה', 'יהוה', 'את', 'משה'], None)
assert [s for s in RECEIPT1 if s.startswith('Num 31:')] == ['Num 31:31', 'Num 31:41', 'Num 31:47', 'Num 31:7'] and len(RECEIPT1) == 41 and Counter(s.rsplit(':', 1)[0] for s in RECEIPT1).most_common(4) == [('Exod 39', 7), ('Exod 40', 7), ('Lev 8', 5), ('Num 31', 4)]
assert phrase(['ויקצף', 'משה'], None) == ['Num 31:14'] and U('ויקצף', books=T) == ['Deut 1:34', 'Exod 16:20', 'Gen 40:2', 'Lev 10:16', 'Num 31:14'] and words('Exod', 16, 20)[-3:] == ['ויקצף', 'עלהם', 'משה'] and words('Lev', 10, 16)[words('Lev', 10, 16).index('ויקצף'):][:3] == ['ויקצף', 'על', 'אלעזר'] and words('Lev', 10, 16)[-6:-3] == ['ועל', 'איתמר', 'בני']
assert phrase(['שמעו', 'נא', 'המרים'], None) == ['Num 20:10'] and 'ויקצף' not in words('Num', 20, 10)   # the Sifrei's second seat carries no wrath-verb
assert phrase(['זאת', 'חקת', 'התורה'], None) == ['Num 19:2', 'Num 31:21'] and words('Num', 19, 2)[:6] == ['זאת', 'חקת', 'התורה', 'אשר', 'צוה', 'יהוה'] and aramaic(31, 21)[7:10] == ['דא', 'גזרת', 'אוריתא']

# THE COMMAND AND THE MUSTER (31:1-6): "avenge the vengeance" (the doubled root, one seat) "of the children of Israel from THE MIDIANITES" —
# the definite gentilic's TWO Bible seats are the command (25:17 "harass the Midianites") and this: the command and its run share the word;
# Moses' relay turns Israel's vengeance into "the vengeance of the LORD" (31:3 — the phrase's other three seats Babylon's, Jeremiah 50-51; the
# Sifrei 157:2 reads the turn); "afterward you shall be gathered to your people" one seat — the death promised at 27:13 ("you shall be
# gathered to your people, you too, as Aaron your brother") sequenced AFTER the war; "arm yourselves" (one seat) — the root's Torah seats all
# in 31-32 and Deuteronomy 3:18 (Gad and Reuben's "armed" the next chapter's word; "your loins" and "remove the stones" its homographs); "a
# thousand to a tribe" three seats all here, the doubled "a thousand to a tribe, a thousand to a tribe" one; "for all the tribes of Israel"
# here and Joshua 22:14; "twelve thousand" — 31:5 and Judges 21:10 (the twelve thousand sent against Jabesh-gilead); "were delivered" — the
# rare root's two Torah seats both in this chapter (31:5 the men handed over, 31:16 "to commit treachery"); ONKELOS "were CHOSEN"; Phinehas
# (four Torah seats) sent with "the holy vessels" (the Kohathites' charge, 3:31) and "the trumpets of alarm" (here and 2 Chronicles 13:12,
# Abijah's war) — the trumpets' ONE narrative seat in the Torah, the run of 10:9's war clause ("you shall sound an alarm... and be remembered")
assert phrase(['נקם', 'נקמת'], None) == ['Num 31:2'] and phrase(['נקמת', 'בני', 'ישראל'], None) == ['Num 31:2'] and phrase(['נקמת', 'יהוה'], None) == ['Jer 50:15', 'Jer 50:28', 'Jer 51:11', 'Num 31:3'] and seats_in(lambda x, m: 'נקמ' in x or x == 'נקם') == [(2, 'נקם'), (2, 'נקמת'), (3, 'נקמת')]
assert U('המדינים') == ['Num 25:17', 'Num 31:2'] and words('Num', 25, 17)[:3] == ['צרור', 'את', 'המדינים'] and aramaic(31, 3)[13:17] == ['פרענות', 'דין', 'עמא', 'דיי']   # ONKELOS: "the vengeance of the JUDGMENT of the people of the LORD"
assert phrase(['אחר', 'תאסף', 'אל', 'עמיך'], None) == ['Num 31:2'] and phrase(['ונאספת', 'אל', 'עמיך'], None) == ['Num 27:13'] and phrase(['והאסף', 'אל', 'עמיך'], None) == ['Deut 32:50'] and words('Num', 27, 13)[2:10] == ['ונאספת', 'אל', 'עמיך', 'גם', 'אתה', 'כאשר', 'נאסף', 'אהרן']
assert U('החלצו') == ['Num 31:3'] and U('חלוצי') == ['1Chr 12:25', '2Chr 17:18', 'Josh 4:13', 'Num 31:5'] and U('חלוצים') == ['Deut 3:18', 'Num 32:30', 'Num 32:32'] and words('Deut', 3, 18)[13:15] == ['חלוצים', 'תעברו'] and sg(31, 3, 'החלצו') == 'pull-off'
assert Counter(x for v in range(1, 43) for x, _ in by[('Num', 32, v)] if x in ('נחלץ', 'תחלצו', 'חלוץ', 'חלוצים')) == Counter({'חלוץ': 3, 'חלוצים': 2, 'נחלץ': 1, 'תחלצו': 1}) and U('מחלציך', books=T) == ['Gen 35:11'] and U('מחלציך') == ['1Kgs 8:19', '2Chr 6:9', 'Gen 35:11'] and words('Lev', 14, 40)[2] == 'וחלצו'   # the final tsadi is its own letter: 'חלוץ' is not 'חלוצ'
assert phrase(['אלף', 'למטה'], None) == ['Num 31:4', 'Num 31:5', 'Num 31:6'] and phrase(['אלף', 'למטה', 'אלף', 'למטה'], None) == ['Num 31:4'] and phrase(['לכל', 'מטות', 'ישראל'], None) == ['Josh 22:14', 'Num 31:4'] and phrase(['שנים', 'עשר', 'אלף'], None) == ['2Sam 10:6', '2Sam 17:1', 'Josh 8:25', 'Judg 21:10', 'Num 31:5', 'Ps 60:2']
assert U('וימסרו') == ['Num 31:5'] and sorted({f"{b} {c}:{v}" for (b, c, v), ws in by.items() if b in T for x, m in ws if x in ('וימסרו', 'למסר', 'ימסר', 'נמסר')}) == ['Num 31:16', 'Num 31:5'] and aramaic(31, 5)[0] == 'ואתבחרו' and aramaic(31, 16)[7:9] == ['לשקרא', 'שקר']
assert U('פינחס', books=T) == ['Exod 6:25', 'Num 25:11', 'Num 25:7', 'Num 31:6'] and phrase(['פינחס', 'בן', 'אלעזר', 'הכהן'], None) == ['Josh 22:13', 'Josh 22:31', 'Josh 22:32', 'Num 31:6']
assert phrase(['וכלי', 'הקדש'], None) == ['Num 31:6', 'Num 3:31'] and phrase(['כלי', 'הקדש'], None) == ['1Chr 9:29', '1Kgs 8:4', '2Chr 5:5', 'Num 18:3', 'Num 4:15'] and phrase(['וחצצרות', 'התרועה'], None) == ['2Chr 13:12', 'Num 31:6']
assert sorted({f"{b} {c}:{v}" for (b, c, v), ws in by.items() if b in T for x, m in ws if 'חצצר' in x}) == ['Num 10:10', 'Num 10:8', 'Num 10:9', 'Num 31:6'] and words('Num', 10, 9)[8:12] == ['והרעתם', 'בחצצרות', 'ונזכרתם', 'לפני'] and aramaic(31, 6)[15:18] == ['וחצצרת', 'יבבתא', 'בידיה']

# THE WAR (31:7-12): "they warred" one seat; "and they killed every male" — Shechem's the only other seat (Genesis 34:25, Simeon and Levi);
# the kill-root six tokens in the chapter; "the kings of Midian" four Bible seats — this and Gideon's two kings (Judges 8:5, 12, 26); "the
# five kings of Midian" one; the five names all at Joshua 13:21 — the retelling calls them "the princes of Midian... the princes of Sihon,
# dwelling in the land", and 13:22 adds "the SOOTHSAYER" to Balaam and writes "to their slain" for 31:8's "upon their slain" (the word's
# three Bible seats); Zur is Cozbi's father (25:15 "head of the peoples of a father's house in Midian"); "Balaam son of Beor" five seats;
# "they killed by the sword" — here and Elijah's "they have killed your prophets by the sword" (1 Kings 19:10, 14); the sword in Balak's
# chapter thrice (22:23, 22:31 the angel's drawn; 22:29 "would there were a sword in my hand" — the ass's clause the compile closes here);
# THE BOOTY'S FOUR NOUNS — the spoil (two tokens), THE PREY (five of the word's six Bible seats are this chapter's; Isaiah 49:24 the sixth),
# the captives (three), the plunder (four) — and THE TRIBUTE-WORD'S SIX BIBLE SEATS ALL HERE (31:28, 37, 38, 39, 40, 41); "their castles"
# (the word's four seats; Ishmael's "encampments" its kin at Genesis 25:16) — ONKELOS "their houses of worship", the Sifrei's Hebrew putting
# the idolatry on "their cities in their dwellings"; "the plains of Moab by the Jordan of Jericho" (the bare form's one seat; "in the plains
# of Moab" eight; "the Jordan of Jericho" seven — all the book's)
assert U('ויצבאו') == ['Num 31:7'] and phrase(['ויהרגו', 'כל', 'זכר'], None) == ['Gen 34:25', 'Num 31:7'] and len(seats_in(lambda x, m: x in ('ויהרגו', 'הרגו', 'הרג'))) == 6 and seats_in(lambda x, m: x == 'זכר') == [(7, 'זכר'), (17, 'זכר'), (17, 'זכר'), (18, 'זכר'), (35, 'זכר')]
assert phrase(['מלכי', 'מדין'], None) == ['Judg 8:12', 'Judg 8:26', 'Judg 8:5', 'Num 31:8'] and phrase(['חמשת', 'מלכי', 'מדין'], None) == ['Num 31:8'] and words('Judg', 8, 12)[6:11] == ['את', 'שני', 'מלכי', 'מדין', 'את']
assert words('Josh', 13, 21)[15:30] == ['ואת', 'נשיאי', 'מדין', 'את', 'אוי', 'ואת', 'רקם', 'ואת', 'צור', 'ואת', 'חור', 'ואת', 'רבע', 'נסיכי', 'סיחון'] and words('Josh', 13, 22) == ['ואת', 'בלעם', 'בן', 'בעור', 'הקוסם', 'הרגו', 'בני', 'ישראל', 'בחרב', 'אל', 'חלליהם']
assert U('חלליהם') == ['Ezek 6:13', 'Josh 13:22', 'Num 31:8'] and phrase(['על', 'חלליהם'], None) == ['Num 31:8'] and U('הקוסם') == ['Josh 13:22'] and words('Num', 25, 15)[4:8] == ['כזבי', 'בת', 'צור', 'ראש']
assert phrase(['בלעם', 'בן', 'בעור'], None) == ['Deut 23:5', 'Josh 13:22', 'Mic 6:5', 'Num 22:5', 'Num 31:8'] and phrase(['הרגו', 'בחרב'], None) == ['1Kgs 19:10', '1Kgs 19:14', 'Num 31:8'] and [(v, x) for v in range(1, 42) for x, m in by[('Num', 22, v)] if 'חרב' in x] == [(23, 'וחרבו'), (29, 'חרב'), (31, 'וחרבו')]
assert words('Gen', 36, 35)[7:12] == ['המכה', 'את', 'מדין', 'בשדה', 'מואב'] and words('Gen', 37, 28)[1:4] == ['אנשים', 'מדינים', 'סחרים'] and words('Gen', 37, 36)[:2] == ['והמדנים', 'מכרו'] and words('Gen', 25, 2)[7:10] == ['מדן', 'ואת', 'מדין']
assert seats_in(lambda x, m: 'שלל' in x) == [(11, 'השלל'), (12, 'השלל')] and seats_in(lambda x, m: 'מלקוח' in x) == [(11, 'המלקוח'), (12, 'המלקוח'), (26, 'מלקוח'), (27, 'המלקוח'), (32, 'המלקוח')] and U('מלקוח', 'המלקוח') == ['Isa 49:24', 'Num 31:11', 'Num 31:12', 'Num 31:26', 'Num 31:27', 'Num 31:32']
assert seats_in(lambda x, m: x in ('השבי', 'ושביכם')) == [(12, 'השבי'), (19, 'ושביכם'), (26, 'השבי')] and seats_in(lambda x, m: x in ('בזזו', 'הבז')) == [(9, 'בזזו'), (32, 'הבז'), (32, 'בזזו'), (53, 'בזזו')] and sg(31, 11, 'המלקוח') == 'the-transitively--the-jaws'
assert U('מכס', 'המכס', 'ומכסם') == ['Num 31:28', 'Num 31:37', 'Num 31:38', 'Num 31:39', 'Num 31:40', 'Num 31:41'] and seats_in(lambda x, m: 'מכס' in x) == [(28, 'מכס'), (37, 'המכס'), (38, 'ומכסם'), (39, 'ומכסם'), (40, 'ומכסם'), (41, 'מכס')]
assert sorted({f"{b} {c}:{v}" for (b, c, v), ws in by.items() for x, m in ws if x.startswith('טיר')}) == ['Ezek 25:4', 'Num 31:10', 'Ps 69:26', 'Song 8:9'] and words('Gen', 25, 16)[6:8] == ['בחצריהם', 'ובטירתם'] and aramaic(31, 10)[6:8] == ['בית', 'סגדתהון'] and sg(31, 10, 'טירתם') == 'wall-them/their'
assert phrase(['ערבת', 'מואב'], None) == ['Num 31:12'] and len(phrase(['בערבת', 'מואב'], None)) == 8 and phrase(['ירדן', 'ירחו'], None) == ['Num 26:3', 'Num 26:63', 'Num 31:12', 'Num 33:48', 'Num 33:50', 'Num 35:1', 'Num 36:13']
assert aramaic(31, 11)[3] == 'עדאה' and aramaic(31, 11)[6] == 'דברתא' and aramaic(31, 12)[11] == 'שביא' and aramaic(31, 32)[3] == 'בזא' and aramaic(31, 8)[24] == 'בחרבא'

# THE WRATH AND THE WOMEN (31:13-18): "outside the camp" twice (31:13 the going out to meet them, 31:19 the seven days); "the officers of
# thousands and the officers of hundreds" — Jethro's grades (Exodus 18:21, 25; Deuteronomy 1:15 "officers of thousands, of hundreds, of
# fifties, of tens") as the army's ranks, the pair's two seats both here (31:14, 48) and "of the thousands and the hundreds" at 31:54 (and
# David's, 1 Chronicles 13:1); "the appointed of the host" here and Jehoiada's (2 Chronicles 23:14); "have you let every female live" — the
# causative's one seat, the midwives' verb (Exodus 1:17-18); "keep alive" one; "every female" one; "by the word of Balaam" one — ONKELOS "by
# the COUNSEL of Balaam" (the Sifrei 157:5's "what was the word?"); "the matter of Peor" two seats (25:18, 31:16); "treachery against the LORD"
# — the guilt offering's and the suspected wife's phrase (Leviticus 5:21, Numbers 5:6); "the plague" five times for Peor (25:8, 9, 18, 19,
# 31:16); "in the congregation of the LORD" — here and Joshua 22:17, where PHINEHAS HIMSELF retells it ("is the iniquity of Peor too little
# for us... and there was the plague in the congregation of the LORD"); 31:17 opens and closes on "kill" (the Sifrei's second "kill");
# "lying with a male" — the phrase's Bible seats are this chapter's three (31:17, 18, 35) and JABESH-GILEAD'S TWO (Judges 21:11-12, where
# twelve thousand are sent, every male and every woman who knew lying with a male devoted, and four hundred virgins kept — the chapter's
# rule RUN in Judges with its number and its phrase); the men's ban "lyings of a woman" (Leviticus 18:22, 20:13) the other form; Deuteronomy
# 20:13-14's war law spares "the women and the little ones" — this chapter's sentence stricter on both (the Sifrei 157:6's "fit for intercourse")
assert seats_in(lambda x, m: x == 'מחוץ') == [(13, 'מחוץ'), (19, 'מחוץ')] and len(phrase(['מחוץ', 'למחנה'])) == 27 and 'Num 31:13' in phrase(['אל', 'מחוץ', 'למחנה'])
assert phrase(['שרי', 'האלפים', 'ושרי', 'המאות'], None) == ['Num 31:14', 'Num 31:48'] and phrase(['שרי', 'האלפים', 'והמאות'], None) == ['1Chr 13:1', 'Num 31:54'] and words('Exod', 18, 21)[-6:] == ['שרי', 'מאות', 'שרי', 'חמשים', 'ושרי', 'עשרת'] and 'Exod 18:21' in phrase(['שרי', 'אלפים']) and 'Deut 1:15' in phrase(['שרי', 'אלפים'])
assert phrase(['פקודי', 'החיל'], None) == ['2Chr 23:14', 'Num 31:14'] and phrase(['הפקדים', 'אשר', 'לאלפי', 'הצבא'], None) == ['Num 31:48'] and aramaic(31, 14)[0] == 'ורגיז'
assert U('החייתם') == ['Num 31:15'] and U('החיו') == ['Num 31:18'] and U('ותחיין') == ['Exod 1:17', 'Exod 1:18'] and phrase(['כל', 'נקבה'], None) == ['Num 31:15'] and words('Deut', 20, 16)[10:14] == ['לא', 'תחיה', 'כל', 'נשמה']
assert phrase(['הן', 'הנה'], None) == ['Num 31:16'] and phrase(['בדבר', 'בלעם'], None) == ['Num 31:16'] and aramaic(31, 16)[5:8] == ['בעצת', 'בלעם', 'לשקרא'] and phrase(['דבר', 'פעור'], None) == ['Num 25:18', 'Num 31:16'] and phrase(['מעל', 'ביהוה'], None) == ['1Chr 10:13', '2Chr 28:19', 'Lev 5:21', 'Num 31:16', 'Num 5:6']
assert [s for s in U('המגפה', 'במגפה') if s.startswith('Num 25') or s.startswith('Num 31')] == ['Num 25:18', 'Num 25:19', 'Num 25:8', 'Num 25:9', 'Num 31:16'] and phrase(['בעדת', 'יהוה'], None) == ['Josh 22:17', 'Num 31:16'] and words('Josh', 22, 17)[:5] == ['המעט', 'לנו', 'את', 'עון', 'פעור']
assert words('Num', 31, 17)[1] == 'הרגו' and words('Num', 31, 17)[-1] == 'הרגו' and phrase(['משכב', 'זכר'], None) == ['Judg 21:11', 'Num 31:18', 'Num 31:35'] and phrase(['למשכב', 'זכר'], None) == ['Judg 21:12', 'Num 31:17'] and phrase(['משכבי', 'אשה'], None) == ['Lev 18:22', 'Lev 20:13']
assert words('Judg', 21, 10)[3:6] == ['שנים', 'עשר', 'אלף'] and words('Judg', 21, 11)[4:12] == ['כל', 'זכר', 'וכל', 'אשה', 'ידעת', 'משכב', 'זכר', 'תחרימו'] and words('Judg', 21, 12)[4:10] == ['ארבע', 'מאות', 'נערה', 'בתולה', 'אשר', 'לא'] and N('Judg', 21, 12) == [400]
assert phrase(['החיו', 'לכם'], None) == ['Num 31:18'] and U('בטף') == ['Num 31:17'] and phrase(['הטף', 'בנשים'], None) == ['Num 31:18'] and words('Deut', 20, 14)[:4] == ['רק', 'הנשים', 'והטף', 'והבהמה'] and words('Deut', 20, 13)[5:10] == ['את', 'כל', 'זכורה', 'לפי', 'חרב']
assert aramaic(31, 17)[8:11] == ['גבר', 'למשכבי', 'דכורא'] and aramaic(31, 18)[8:10] == ['קיימו', 'לכון']

# THE PURIFICATION (31:19-24): "encamp outside the camp seven days"; "on the third day and on the seventh day" three seats (19:12, 19:19,
# 31:19 — the heifer's schedule quoted); the purify-verb (the hitpael of the sin-root) six tokens in the Torah, all in chapters 19 and 31
# (19:12 ×2, 13, 20; 31:19, 20, 23) — the store glosses it "sin" (the root's homonym); "whoever has killed a soul" and "whoever has touched a
# slain one" one seat each — 19:16's "slain by the sword" the Sifrei 158:3's teaching (the sword unclean seven days, Chukat's rows); "you and
# your captives" one; THE FOUR MATERIALS against Leviticus 11:32's four — wood vessel, garment, skin shared, SACK there against GOAT-WORK here
# (the freed-word identity of 157:8; "work of goats" one seat; "sack" two Torah seats — Jacob's and 11:32's); THE SIX METALS in one verse —
# TIN's one Torah seat, LEAD's two (Exodus 15:10 "as lead in the mighty waters" and this; the verb "separated" tin's homograph at 16:9 and
# Deuteronomy 10:8); "only" twice (31:22, 23); "the water of sprinkling" — the phrase's four seats all in 19 and 31 (19:9, 13, 20; 31:23);
# "pass through the fire" one seat, "pass through water" one; "and it shall be clean" (Numbers: 19:19, 31:23); "wash your garments on the
# seventh day and be clean" one — against 19:19's "wash his clothes and bathe in water and be clean AT EVENING"; "and afterward come into the
# camp" one — the leper's and the heifer-priest's "afterward he shall come into the camp" (Leviticus 14:8, Numbers 19:7); ONKELOS makes the
# purifying the SPRINKLING ("you shall sprinkle on him", "it shall be sprinkled"), "the water of sprinkling", "tin" and "lead" by their names
assert seats_in(lambda x, m: x == 'שבעת') == [(19, 'שבעת'), (43, 'שבעת')] and morphs('Num', 31, 43)[10] == 'HAcmsc' and words('Num', 31, 43)[10] == 'שבעת' and phrase(['ביום', 'השלישי', 'וביום', 'השביעי'], None) == ['Num 19:12', 'Num 19:19', 'Num 31:19']
assert sorted({f"{b} {c}:{v} {x}" for (b, c, v), ws in by.items() if b in T for x, m in ws if m and m.startswith('HVt') and 'חטא' in x}) == ['Num 19:12 יתחטא', 'Num 19:13 יתחטא', 'Num 19:20 יתחטא', 'Num 31:19 תתחטאו', 'Num 31:20 תתחטאו', 'Num 31:23 יתחטא'] and words('Num', 19, 12).count('יתחטא') == 2 and sg(31, 19, 'תתחטאו') == 'sin'
assert phrase(['הרג', 'נפש'], None) == ['Num 31:19'] and phrase(['נגע', 'בחלל'], None) == ['Num 31:19'] and phrase(['בחלל', 'חרב'], None) == ['Num 19:16'] and U('בחלל') == ['Num 19:16', 'Num 19:18', 'Num 31:19'] and phrase(['אתם', 'ושביכם'], None) == ['Num 31:19']
assert words('Lev', 11, 32)[8:16] == ['כלי', 'עץ', 'או', 'בגד', 'או', 'עור', 'או', 'שק'] and words('Num', 31, 20) == ['וכל', 'בגד', 'וכל', 'כלי', 'עור', 'וכל', 'מעשה', 'עזים', 'וכל', 'כלי', 'עץ', 'תתחטאו'] and phrase(['מעשה', 'עזים'], None) == ['Num 31:20'] and U('שק', 'ושק', 'בשק', books=T) == ['Gen 37:34', 'Lev 11:32']
assert U('בדיל', books=T) == [] and U('הבדיל', books=T) == ['Deut 10:8', 'Num 16:9', 'Num 31:22'] and morphs('Deut', 10, 8)[words('Deut', 10, 8).index('הבדיל')].startswith('HVh') and morphs('Num', 16, 9)[words('Num', 16, 9).index('הבדיל')].startswith('HVh') and morphs('Num', 31, 22)[10] == 'HTd/Ncmsa'   # tin only with its article; its two look-alikes the verb and U('עפרת', 'העפרת', 'כעופרת', 'ועופרת', 'עופרת', books=T) == ['Exod 15:10', 'Num 31:22'] and words('Num', 31, 22) == ['אך', 'את', 'הזהב', 'ואת', 'הכסף', 'את', 'הנחשת', 'את', 'הברזל', 'את', 'הבדיל', 'ואת', 'העפרת']
assert seats_in(lambda x, m: x == 'אך') == [(22, 'אך'), (23, 'אך')] and aramaic(31, 22)[10] == 'אבצא' and aramaic(31, 22)[12] == 'אברא'
assert phrase(['מי', 'נדה'], None) == ['Num 19:13', 'Num 19:20'] and phrase(['במי', 'נדה'], None) == ['Num 31:23'] and phrase(['למי', 'נדה'], None) == ['Num 19:9'] and phrase(['תעבירו', 'באש'], None) == ['Num 31:23'] and phrase(['תעבירו', 'במים'], None) == ['Num 31:23'] and [s for s in U('וטהר') if s.startswith('Num')] == ['Num 19:19', 'Num 31:23']
assert phrase(['וכבסתם', 'בגדיכם'], None) == ['Num 31:24'] and phrase(['וכבסו', 'בגדיהם'], None) == ['Num 8:7'] and phrase(['וטהר', 'בערב'], None) == ['Num 19:19'] and words('Num', 19, 19)[11:16] == ['וכבס', 'בגדיו', 'ורחץ', 'במים', 'וטהר'] and phrase(['ואחר', 'תבאו', 'אל', 'המחנה'], None) == ['Num 31:24'] and phrase(['ואחר', 'יבוא', 'אל', 'המחנה'], None) == ['Lev 14:8', 'Num 19:7']
assert aramaic(31, 19)[14:16] == ['תדון', 'עלוהי'] and aramaic(31, 23)[8:11] == ['במי', 'אדיותא', 'יתדי'] and aramaic(31, 24)[0] == 'ותחורון' and sg(31, 24, 'וכבסתם') == 'and-trample'

# THE DIVISION AND THE TRIBUTE (31:25-31): "take the sum" (the census formula's singular imperative, one seat; "take ye" 1:2 and 26:2, "take"
# 4:2 and 4:22, "when you take" Exodus 30:12, "have taken" 31:49) "of the prey of the captives... you and Eleazar the priest and the heads
# of the fathers of the congregation" (one seat — the census staff); "halve" — THE HALF-ROOT EIGHT TOKENS IN FIVE SPELLINGS (the verb 31:27
# one seat and 31:42; the noun "the half" 31:36 one seat; "half of" 31:30, 43, 47 with Habakkuk 3:13; "half" 31:29, 42 — the HALF-SHEKEL's
# spelling, Exodus 30:13, 38:26); "those who took the war" one, "who went out to the host" two (31:27, 28), "the men of war" (Deuteronomy
# 2:14, 16 — the generation that died — and 31:28, 49), "the men of the host" (31:21, 53), "the people of the host" (31:32); "one soul of the
# five hundred" one seat (the parser's silent denominator); "the LORD's heave-offering" — eleven seats: THE HALF-SHEKEL'S (Exodus 30:14, 15),
# the tabernacle donation's (35:5, 21, 24), the tithe's tithe (18:26, 28, 29), this chapter's two (31:29, 41) and Hezekiah's (2 Chronicles
# 31:14); "one held of the fifty" one (the participle "held" here and 1 Chronicles 24:6); "the Levites who keep the charge of the tabernacle
# of the LORD" two seats both here — "the charge of the tabernacle" 1:53's; 31:30 adds "of all the beasts" to 31:28's four classes; the
# receipt at 31:31; ONKELOS "receive the account", "divide", "separate a levy", "a separation" for the heave-offering, "one that is held"
assert phrase(['שא', 'את', 'ראש'], None) == ['Num 31:26'] and phrase(['שאו', 'את', 'ראש'], None) == ['Num 1:2', 'Num 26:2'] and phrase(['נשא', 'את', 'ראש'], None) == ['Num 4:2', 'Num 4:22'] and phrase(['נשאו', 'את', 'ראש'], None) == ['Num 31:49'] and words('Exod', 30, 12)[:4] == ['כי', 'תשא', 'את', 'ראש']
assert phrase(['וראשי', 'אבות', 'העדה'], None) == ['Num 31:26'] and seats_in(lambda x, m: 'חצ' in x and 'חצצר' not in x) == [(27, 'וחצית'), (29, 'ממחציתם'), (30, 'וממחצת'), (36, 'המחצה'), (42, 'וממחצית'), (42, 'חצה'), (43, 'מחצת'), (47, 'ממחצת')]
assert U('וחצית') == ['Num 31:27'] and U('המחצה') == ['Num 31:36'] and U('מחצת', 'ממחצת', 'וממחצת') == ['Hab 3:13', 'Num 31:30', 'Num 31:43', 'Num 31:47'] and 'Exod 30:13' in U('מחצית') and 'Exod 38:26' in U('מחצית') and U('וממחצית', 'ממחציתם') == ['1Chr 6:55', 'Josh 21:25', 'Num 31:29', 'Num 31:42'] and U('מחצית') == ['1Kgs 16:9', 'Exod 30:13', 'Exod 38:26', 'Neh 8:3']   # the Levite cities' 'half-tribe' the homographs
assert phrase(['תפשי', 'המלחמה'], None) == ['Num 31:27'] and phrase(['היצאים', 'לצבא'], None) == ['Num 31:27', 'Num 31:28'] and phrase(['אנשי', 'המלחמה']) == ['Deut 2:14', 'Deut 2:16', 'Num 31:28', 'Num 31:49'] and phrase(['אנשי', 'הצבא'], None) == ['Num 31:21', 'Num 31:53'] and phrase(['עם', 'הצבא'], None) == ['Num 31:32']
assert phrase(['תרומת', 'יהוה'], None) == ['2Chr 31:14', 'Exod 30:14', 'Exod 30:15', 'Exod 35:21', 'Exod 35:24', 'Exod 35:5', 'Num 18:26', 'Num 18:28', 'Num 18:29', 'Num 31:29', 'Num 31:41'] and phrase(['מכס', 'תרומת', 'יהוה'], None) == ['Num 31:41'] and phrase(['והרמת', 'מכס'], None) == ['Num 31:28']
assert U('האחז') == ['Num 31:47'] and sorted({f"{b} {c}:{v}" for (b, c, v), ws in by.items() for x, m in ws if x == 'אחז' and m and 'Vqs' in m}) == ['1Chr 24:6', 'Num 31:30']
assert phrase(['שמרי', 'משמרת', 'משכן', 'יהוה'], None) == ['Num 31:30', 'Num 31:47'] and phrase(['משמרת', 'משכן'], None) == ['Num 1:53', 'Num 31:30', 'Num 31:47'] and words('Num', 1, 53)[-6:-2] == ['ושמרו', 'הלוים', 'את', 'משמרת']
assert words('Num', 31, 28)[12:] == ['מן', 'האדם', 'ומן', 'הבקר', 'ומן', 'החמרים', 'ומן', 'הצאן'] and words('Num', 31, 30)[8:18] == ['מן', 'האדם', 'מן', 'הבקר', 'מן', 'החמרים', 'ומן', 'הצאן', 'מכל', 'הבהמה'] and phrase(['מכל', 'הבהמה'], None) == ['Gen 3:14', 'Gen 7:2', 'Gen 8:20', 'Lev 11:2', 'Num 31:30']
assert aramaic(31, 26)[:3] == ['קבל', 'ית', 'חושבן'] and aramaic(31, 27)[0] == 'ותפלג' and aramaic(31, 28)[:2] == ['ותפרש', 'נסיבא'] and aramaic(31, 29)[5] == 'אפרשותא' and aramaic(31, 30)[4:6] == ['חד', 'דאתחד'] and aramaic(31, 28)[10:14] == ['חד', 'נפשא', 'מחמש', 'מאה']

# THE SPOIL'S CENSUS, THE TWO HALVES AND THE TRIBUTE (31:32-47): the four totals (every one a multiple of a thousand, 840,000 heads), "the
# rest of the booty which the people of the host had plundered" (the soldiers' private plunder uncounted — 31:53 "each for himself"), "of
# the women who had not known lying with a male" (the phrase's third seat); the warriors' half exact (÷ 2), THE TRIBUTE EXACT (÷ 500: 675, 72,
# 61, 32 — 840 heads to the priest), the receipt "the tribute of the LORD's heave-offering to Eleazar" (31:41); the congregation's half the
# same four numbers; the Levites' "one held of the fifty" WITH NO NUMBER STATED — the shares computed (6,750 / 720 / 610 / 320 = 8,400, ten
# times the priest's), the receipt at 31:47; ONKELOS writes the numbers in the Aramaic order ("six hundred and seventy and five thousands")
assert words('Num', 31, 32)[2:7] == ['יתר', 'הבז', 'אשר', 'בזזו', 'עם'] and phrase(['בזזו', 'איש', 'לו'], None) == ['Num 31:53'] and phrase(['ידעו', 'משכב'], None) == ['Num 31:18', 'Num 31:35']
assert aramaic(31, 32)[11:16] == ['שית', 'מאה', 'ושבעין', 'וחמשא', 'אלפין'] and aramaic(31, 40)[8:11] == ['תלתין', 'ותרין', 'נפשין'] and aramaic(31, 37)[1] == 'נסיבא' and aramaic(31, 41)[3:5] == ['נסיב', 'אפרשותא']
assert phrase(['ולא', 'נפקד', 'ממנו', 'איש'], None) == ['Num 31:49'] and U('נפקד') == ['1Sam 25:21', '1Sam 25:7', 'Num 31:49'] and sg(31, 49, 'נפקד') == 'count/visit'

# THE OFFICERS' GOLD (31:48-54): the appointed over the thousands drew near — "your servants have taken the sum of the men of war... and not
# one man of us is missing" (Nabal's shepherds' word, 1 Samuel 25:7, 21); "the LORD's offering" — the second Passover's phrase (9:7, 13) and
# this; THE FIVE ORNAMENTS: the armlet (Saul's, 2 Samuel 1:10, and this), the bracelet (Rebekah's, Genesis 24:22; Ezekiel's; and the
# heifer chapter's homograph "a cover BOUND on it", 19:15), the ring (fifteen seats), the earring (Ezekiel 16:12 and this), the kumaz (the
# tabernacle donation's, Exodus 35:22, and this — the two gold lists share the ring and the kumaz; "articles of gold" both); "to atone for
# our souls" one seat — THE HALF-SHEKEL'S "to atone for your souls" (Exodus 30:15, 16; the blood's, Leviticus 17:11); 16,750 shekels
# (ONKELOS sela); "the men of the host had plundered each for himself"; "a memorial for the children of Israel before the LORD" one seat —
# EXODUS 30:16'S OWN SIX WORDS in another order ("for the children of Israel for a memorial before the LORD, to atone for your souls"): THE
# OFFICERS' GOLD RUNS THE RANSOM OF EXODUS 30 AT A COUNT — the sum taken, none missing, the atonement, the memorial; Gideon's Midianite gold
# the word's second count (1,700 shekels of earrings, Judges 8:26); the trumpets' "you shall be REMEMBERED before the LORD" (10:9) at the
# war's opening and "a MEMORIAL before the LORD" at its close — one root
assert phrase(['ויקרבו', 'אל', 'משה'], None) == ['Num 31:48'] and phrase(['קרבן', 'יהוה'], None) == ['Num 31:50', 'Num 9:13', 'Num 9:7'] and phrase(['ונקרב', 'את', 'קרבן', 'יהוה'], None) == ['Num 31:50']
assert U('אצעדה', 'ואצעדה') == ['2Sam 1:10', 'Num 31:50'] and U('צמיד', 'וצמיד', 'צמידים', 'וצמידים') == ['Ezek 16:11', 'Ezek 23:42', 'Gen 24:22', 'Num 19:15', 'Num 31:50'] and words('Num', 19, 15)[:6] == ['וכל', 'כלי', 'פתוח', 'אשר', 'אין', 'צמיד'] and len(U('טבעת', 'וטבעת')) == 15 and U('עגיל', 'ועגיל', 'עגילים', 'ועגילים') == ['Ezek 16:12', 'Num 31:50'] and U('כומז', 'וכומז') == ['Exod 35:22', 'Num 31:50']
assert words('Exod', 35, 22)[8:15] == ['חח', 'ונזם', 'וטבעת', 'וכומז', 'כל', 'כלי', 'זהב'] and phrase(['כלי', 'זהב'], None) == ['1Chr 18:10', '1Sam 6:15', '2Kgs 12:14', 'Exod 35:22', 'Num 31:50'] and words('2Sam', 1, 10)[-8:-5] == ['ואצעדה', 'אשר', 'על']
assert phrase(['לכפר', 'על', 'נפשתינו'], None) == ['Num 31:50'] and phrase(['לכפר', 'על', 'נפשתיכם'], None) == ['Exod 30:15', 'Exod 30:16', 'Lev 17:11'] and words('Exod', 30, 16)[13:22] == ['והיה', 'לבני', 'ישראל', 'לזכרון', 'לפני', 'יהוה', 'לכפר', 'על', 'נפשתיכם']
assert phrase(['זכרון', 'לבני', 'ישראל', 'לפני', 'יהוה'], None) == ['Num 31:54'] and phrase(['לבני', 'ישראל', 'לזכרון'], None) == ['Exod 30:16'] and U('זכרון', 'לזכרון', books=T) == ['Exod 12:14', 'Exod 17:14', 'Exod 30:16', 'Exod 39:7', 'Lev 23:24', 'Num 10:10', 'Num 17:5', 'Num 31:54', 'Num 5:15']
assert words('Exod', 30, 12) == ['כי', 'תשא', 'את', 'ראש', 'בני', 'ישראל', 'לפקדיהם', 'ונתנו', 'איש', 'כפר', 'נפשו', 'ליהוה', 'בפקד', 'אתם', 'ולא', 'יהיה', 'בהם', 'נגף', 'בפקד', 'אתם'] and words('Num', 10, 9)[10] == 'ונזכרתם'
assert phrase(['כל', 'כלי', 'מעשה'], None) == ['Num 31:51'] and seats_in(lambda x, m: x == 'מועד') == [(54, 'מועד')] and seats_in(lambda x, m: 'שקל' in x) == [(52, 'שקל')] and words('Judg', 8, 26)[6:10] == ['אלף', 'ושבע', 'מאות', 'זהב'] and N('Judg', 8, 26)[:1] == [1700]
assert aramaic(31, 50)[8:13] == ['שירין', 'ושבכין', 'עזקן', 'קדשין', 'ומחוך'] and aramaic(31, 52)[13:15] == ['וחמשין', 'סלעין'] and aramaic(31, 54)[12:15] == ['למשכן', 'זמנא', 'דכרנא'] and aramaic(31, 49)[11:15] == ['ולא', 'שגא', 'מננא', 'אנש'] and sg(31, 54, 'מועד') == 'seasons' and sg(31, 8, 'בחרב') == 'in-drought'

# THE RETELLINGS AND THE SHELF'S CITATIONS READ TO THEIR VERSES: Joshua 13:21-22 (the five as Sihon's princes, Balaam the soothsayer "among
# their slain"); Joshua 22:17 (Phinehas on Peor's plague); Judges 21:10-12 (Jabesh-gilead); Judges 8 (Gideon's two kings of Midian, the
# 1,700 of gold); Psalm 106:28-31 (Peor, Phinehas, the plague stayed); Genesis 36:35 (Hadad who smote Midian in the field of Moab — 157:1);
# Genesis 37:36 (the Medanites sold Joseph — 157:4) against 37:28's Midianite merchants and 25:2's two brothers; Exodus 17:4 ("a little more
# and they will stone me" — 157:3); Deuteronomy 3:18 (157:2); 21:26 and Genesis 24:10 ("from his hand" — 157:4); Exodus 14:7, 14:14 (157:5);
# Joshua 7:1 (Achan — 157:5); 19:14 (157:7); Leviticus 11:32 (157:8); Leviticus 10:16, 20:10 (157:9); Esther 2:22 (157:9); 19:16, 19:19 (158:3)
assert words('Exod', 17, 4)[-3:] == ['מעט', 'וסקלני'] or words('Exod', 17, 4)[-2:] == ['מעט', 'וסקלני']
assert words('Num', 21, 26)[-3:] == ['ארצו', 'מידו'] or 'מידו' in words('Num', 21, 26)
assert 'בידו' in words('Gen', 24, 10) and words('Exod', 14, 14)[:3] == ['יהוה', 'ילחם', 'לכם'] and 'רכב' in words('Exod', 14, 7) and words('Josh', 7, 1)[:4] == ['וימעלו', 'בני', 'ישראל', 'מעל']
assert words('Esth', 2, 22)[-4:] == ['אסתר', 'למלך', 'בשם', 'מרדכי'] and words('Num', 19, 14)[:6] == ['זאת', 'התורה', 'אדם', 'כי', 'ימות', 'באהל'] and words('Ps', 106, 30) == ['ויעמד', 'פינחס', 'ויפלל', 'ותעצר', 'המגפה']
assert words('1Sam', 30, 24)[-2:] == ['יחדו', 'יחלקו'] and words('1Sam', 30, 25)[4:8] == ['וישמה', 'לחק', 'ולמשפט', 'לישראל'] and words('Josh', 22, 8)[-5:] == ['חלקו', 'שלל', 'איביכם', 'עם', 'אחיכם']   # the equal shares as David's statute and Gad and Reuben's division — no row of the declared shelf links them to 31:27: OBSERVED, not linked

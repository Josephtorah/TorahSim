import os as _os
_ROOT = _os.path.normpath(_os.path.join(_os.path.dirname(_os.path.abspath(__file__)), '..', '..', '..'))   # THE PORTABLE REPO (2026-09-15): the repo root from this file's own place
#!/usr/bin/env python3
# THE DEUTERONOMY WALK, sitting 19 — CHAPTERS 29-31, Deuteronomy 29:1-31:30 IN THE LEAN FORM (2026-09-27; the owner: "Continue" after sitting 18b's tail, no
# compaction between, /context 387k at the open — THE LEAN PASS's eleventh sitting, its sixth reading, the second on chapters WITHOUT A SPINE PISKA): THE INK of the
# three chapters, computed from the Tanakh DB, the snapshot store and the shelf's own bytes — never typed. Sitting 18's form (ch26_ink.py): the generic helpers copied
# by derive_ch29_ink.py from the forms' ch22_ink.py by content markers (the three chapters substituted), the constants and every assert the three chapters' own, typed
# FROM THE PRINTS (ch29_dump0.out … ch31_dump0.out, ch29_split.out, ch29_measure_lean.out). THE TWO DIVISIONS AGREE in all three (28 = 28, cost 19; 20 = 20, cost 18;
# 30 = 30, cost 30) — the identity; the Hebrew's 28:69 is the English's 29:1, so the English's chapter 29 runs one verse ahead. THE SPINE IS ON CHAPTER 31 ALONE —
# TWO piskaot 304-305 with 8 rows (304 on 31:14 "your days approach" two rows; 305 HEADLESS after it, "then the LORD said to Moses: take Joshua" six rows — Moses'
# death and Joshua's commission); 303 on 26:15 before, 306 on 32:1 after — THE SIFREI HAS NO PISKA ON 26:16-31:13: CHAPTERS 29 AND 30 CARRY NO SPINE, their shelf
# Onkelos whole and the rows elsewhere citing them. NINETEEN rows elsewhere cite the three chapters by the union of the three files (the split's print). THE PORTION
# EDGE at 29:8|29:9 INSIDE chapter 29 (Ki Tavo ends, Nitzavim opens); Nitzavim ends with chapter 30; Vayelech is chapter 31 whole — the chapter the unit, CHAPTER NUMBERS.
# The parser MEASURED on every verse — the bare number words 29:4 "forty", 31:2 "a hundred (and twenty)", 31:10 "seven years" (starred), and the homographs "swore"
# (nishba) at 29:12, 30:20, 31:7, "sated" (ve-sava, starred) at 31:20 — the seven's; "rejoiced" (shesh) at 30:9 — the six's (28:63's twin). The hand's facts as asserts, run all at once by assert_driver.py.
import json, os, re, html, sqlite3, sys, io, contextlib, unicodedata, subprocess
from collections import Counter
ROOT = _ROOT
DATE = '2026-09-27'
CHS = (29, 30, 31)
UIDS = ['deu_29_moab_covenant', 'deu_30_teshuvah_choice', 'deu_31_charge_torah']   # the drafts' own ids (the G prints): three units, one per chapter
SPANS = {'deu_29_moab_covenant': (29, 1, 28), 'deu_30_teshuvah_choice': (30, 1, 20), 'deu_31_charge_torah': (31, 1, 30)}
PREFIX = {'deu_29_moab_covenant': 'DV29', 'deu_30_teshuvah_choice': 'DV30', 'deu_31_charge_torah': 'DV31'}
SPAN = [(29, v) for v in range(1, 29)] + [(30, v) for v in range(1, 21)] + [(31, v) for v in range(1, 31)]
PISKAOT = [304, 305]   # THE SPINE ON CHAPTER 31: two piskaot (one headless) — the A prints and the split's; 303 heads on 26:15 (headless, inside 26:13-15), 306 on 32:1
PISKAOT_BY = {29: [], 30: [], 31: [304, 305]}
HEADLESS = [305]   # no book-named citation at its head (the dump: "head None"; the split: 305:1 opens "(Numbers 27:18) and the LORD said to Moses: take Joshua") — read WHOLE from the export
SPINE_ROWS = {304: 2, 305: 6}   # rows per piska, both files (the heads table and the split's print) — 8
PREV_CHAPTER_ROWS = []   # no tail folded in (303's rows carry no word of 31:14 — the split's assert; 303:20 cites 26:15 and 304:1 opens with 31:14's citation)
READ_ROWS = [(p, r) for p in PISKAOT for r in range(1, SPINE_ROWS[p] + 1)]   # 8 — this ledger's spine rows
EXP2DB = {29: {e: [e] for e in range(1, 29)}, 30: {e: [e] for e in range(1, 21)}, 31: {e: [e] for e in range(1, 31)}}   # the identity in all three chapters (chapter 5 the book's one split)
DB2EXP = {c: {d: e for e, ds in EXP2DB[c].items() for d in ds} for c in CHS}
OUTSIDE = [(1, 1), (2, 3), (29, 7), (43, 7), (43, 29), (48, 9), (53, 1), (109, 2), (111, 1), (148, 8), (157, 10), (160, 4), (302, 1), (306, 2), (306, 15), (318, 1), (334, 1), (345, 2), (357, 28)]   # the NINETEEN rows READ WHOLE: the union of the three files beyond piskaot 304-305, joined over the three dumps (the split's print)
EXCLUDED = []   # none known at the design — a translator's misprint is judged by the Hebrew at the whole read (sitting 18's lesson 4)
INTERPOLATION = []
CREDITED = {}   # under THE WHOLE-ROW RULE no spine row is credited: rows read before are REREAD WHOLE here and marked so
TITLE = "Chapters 29-31 — You have seen all the LORD did in Egypt; forty years your garments did not wear out; Sihon and Og taken; you stand this day, all of you, heads, elders, officers, children, wives and the stranger, the hewer of wood and the drawer of water, to enter the covenant and the oath, with those here and those not here; lest a root bear gall and wormwood and a man bless himself in his heart — the LORD will not pardon, the curses of this book will lie on him; the land brimstone and salt like Sodom and Gomorrah, Admah and Zeboiim; the nations will ask why, and be answered: they forsook the covenant and served other gods, and He cast them into another land; the hidden things are the LORD's, the revealed ours forever. When you return with all your heart among the nations where He drove you, He will return and gather you from the end of heaven, circumcise your heart, rejoice over you as He rejoiced over your fathers; the commandment is not in heaven nor beyond the sea but in your mouth and in your heart; life and death, the blessing and the curse — choose life. Moses at a hundred and twenty: Joshua crosses before you, be strong and of good courage; the law written and given to the priests and the elders, to be read every seventh year at the feast of booths before all Israel; the LORD at the Tent in the pillar of cloud: you will sleep with your fathers and this people will whore after other gods and I will hide My face; write this song as a witness; the book beside the ark; I know your rebellion and your stiff neck — heaven and earth called to witness."
OUT = f'{ROOT}/logic/oral_triage/deu_29_31_nitzavim_vayelech_{DATE}.md'
PATCHED = bool(os.environ.get('DEU29_PATCHED'))   # the tail's flag: after the manifest and the seat, the drafts carry operators and the store its overrides
db = sqlite3.connect(f'file:{ROOT}/Data/tanakh.sqlite?mode=ro', uri=True)
VC = dict(db.execute("SELECT chapter, COUNT(*) FROM verses WHERE book='Deut' GROUP BY chapter").fetchall())
NV = {c: VC[c] for c in CHS}
# ---- THE HELPERS (ch22_ink.py's, copied by content markers) ----
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
def he_cites(t): return [(b, hn(c), hn(v)) for b, c, v in re.findall(r'\(([א-ת]+(?: [א-ת])?) ([א-ת]{1,3}) ([א-ת]{1,3})\)', t)]
def has_points(s): return any(0x05B0 <= ord(c) <= 0x05BD for c in s)
def kinrows(f, pat): return len(re.findall(r'^- Onkelos ' + pat, LED[f], re.M))
def onk_ev(c, v):
    """an Onkelos row by the DB's verse — the export's row found through the map (chapter 5's 17-20 share the export's 17)"""
    e = DB2EXP[v] if c == 5 else v
    return clean(onk[c - 1][e - 1]), clean(onk_he[c - 1][e - 1])
# ---- THE INK'S HELPERS, THE DB AND THE STORE (ch22_ink.py's, the three chapters substituted) ----
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
def W29(v): return words('Deut', 29, v)
def W30(v): return words('Deut', 30, v)
def W31(v): return words('Deut', 31, v)
def W(c, v): return words('Deut', c, v)
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
for c, v, idx, hp, g in store.execute("SELECT v.chapter, v.verse, w.idx, w.he_plain, w.gloss FROM words w JOIN verses v ON w.verse_id=v.id WHERE v.book='Deut' AND v.chapter IN (29, 30, 31) ORDER BY v.id, w.idx"):
    SG.setdefault((c, v), []).append((idx, hp.replace('/', ''), g))
def sg(c, v, tok, nth=0):
    hit = [g for _, hp, g in SG[(c, v)] if hp == tok]
    if len(hit) <= nth: raise KeyError((c, v, tok, nth))
    return hit[nth]
def sidx(c, v, tok, nth=0):
    hit = [i for i, hp, _ in SG[(c, v)] if hp == tok]
    assert len(hit) > nth, (c, v, tok, nth, hit)
    return hit[nth]
STORE_MISMATCH = [(c, v, n, len(by[('Deut', c, v)])) for c, v, n in store.execute("SELECT v.chapter, v.verse, COUNT(*) FROM words w JOIN verses v ON w.verse_id=v.id WHERE v.book='Deut' AND v.chapter IN (29, 30, 31) GROUP BY v.chapter, v.verse").fetchall() if n != len(by[('Deut', c, v)])]
import difflib
def SH(a, b_): return sum(s for _, _, s in difflib.SequenceMatcher(a=words(*a), b=words(*b_)).get_matching_blocks())
DV = lambda c, v: ('Deut', c, v)
# THE KIN FOUND BY COMPUTATION (the measure's A section, recomputed here so the asserts read the same instrument): the shared distinct tokens outside the stop list, the top eight, the three closest re-scored in order — keyed by (chapter, verse)
STOP = set('את ואת אשר כל וכל על ועל אל ואל לא ולא כי אם יהוה אלהיך אלהיכם לך לכם בו שם שמה גם מן ממך עד הוא היא אתם אתה אנכי אני לו לה בכל כאשר כן הימים היום אלה האלה בארץ הארץ אשר ואם או פן ופן ואת זה וזה הם המה'.split())
ORD = {k: i for i, k in enumerate(by)}
TOK = {k: set(words(*k)) - STOP for k in by}
KINC = {}
for _c, _v in SPAN:
    _me = DV(_c, _v); _t = TOK[_me]
    _sc = sorted(((len(_t & TOK[k]), k) for k in by if k != _me and len(_t & TOK[k]) >= 2), key=lambda x: (-x[0], ORD[x[1]]))[:8]
    KINC[(_c, _v)] = [(f'{k[0]} {k[1]}:{k[2]}', n, SH(_me, k) if i < 3 else None) for i, (n, k) in enumerate(_sc)]
# ---- THE ASSERTS TYPED FROM THE PRINTS (block a: the dumps' and the split's — the shelf by position, the divisions, the citations; the outside rows' facts COMPUTED) ----
DT = ('Deut',)
def PL(s): return ''.join(c for c in s if c != '/' and not (0x0591 <= ord(c) <= 0x05C7))
def HB0(p, r): return PL(clean(sif_he[p - 1][r - 1]))
def ARM(c, v): return [PL(unicodedata.normalize('NFKC', x)).strip('.:()') for x in clean(onk_he[c - 1][v - 1]).rstrip(':').split()]
def SEATS(sub): return [(c + 1, v + 1) for c in range(34) for v in range(len(onk_he[c])) if sub in ' '.join(ARM(c + 1, v + 1))]
# THE SHELF BY POSITION — the spine ON chapter 31 alone: 304 on 31:14 and 305 HEADLESS; NO piska heads in 29 and 30 (the Sifrei runs 303 on 26:15 to 304 on 31:14); 306 on 32:1 after; the heads by chapter and the window 295-320 as the dumps printed them
assert NV == {29: 28, 30: 20, 31: 30} and VC[28] == 69 and VC[32] == 52 and len(sif) == 357 and len(sif_he) == 357 and sum(len(s) for s in sif) == 2357 and sum(len(s) for s in sif_he) == 2357
HC = Counter(h[0] for h in heads.values() if h)
assert (HC[29], HC[30], HC[31]) == (0, 0, 1) and sorted(HC.items()) == [(1, 24), (3, 4), (6, 6), (11, 21), (12, 20), (13, 14), (14, 14), (15, 16), (16, 19), (17, 16), (18, 16), (19, 10), (20, 14), (21, 17), (22, 22), (23, 22), (24, 16), (25, 10), (26, 4), (31, 1), (32, 36), (33, 14), (34, 1)], sorted(HC.items())
assert {p: heads[p] for p in range(295, 321)} == {295: None, 296: (25, 17), 297: (26, 1), 298: None, 299: None, 300: (26, 4), 301: (26, 5), 302: (26, 12), 303: None, 304: (31, 14), 305: None, 306: (32, 1), 307: (32, 4), 308: (32, 5), 309: (32, 6), 310: (32, 7), 311: (32, 8), 312: (32, 9), 313: (32, 10), 314: (32, 11), 315: (32, 12), 316: (32, 13), 317: (32, 14), 318: (32, 15), 319: (32, 18), 320: (32, 19)}, {p: heads[p] for p in range(295, 321)}
HV = {c: [heads[p][1] for p in PISKAOT_BY[c] if heads[p]] for c in CHS}
assert HV == {29: [], 30: [], 31: [14]}, HV
NOHEAD = {c: [v for v in range(1, NV[c] + 1) if v not in HV[c]] for c in CHS}
assert NOHEAD == {29: list(range(1, 29)), 30: list(range(1, 21)), 31: [v for v in range(1, 31) if v != 14]}, NOHEAD   # chapters 29 and 30 whole without a piska; 31:1-13 the charge, the reading and the ark HEADLESS; 31:15-30 inside 304-305 or uncited
assert {p: (len(sif_he[p - 1]), len(sif[p - 1])) for p in PISKAOT} == {p: (n, n) for p, n in SPINE_ROWS.items()} and [sum(SPINE_ROWS[p] for p in PISKAOT_BY[c]) for c in CHS] == [0, 0, 8] and sum(SPINE_ROWS.values()) == 8 and len(READ_ROWS) == 8 and len(PISKAOT) == 2 and READ_ROWS[0] == (304, 1) and READ_ROWS[-1] == (305, 6)
# THE TAILS AND THE EDGES (the split's print): 303's rows carry no word of 31:14; 303:20 cites 26:15; 304:1 opens with 31:14's citation; 305:1 opens with Numbers 27:18's; 305:6 ends with Joshua weeping; 306:1 opens with 32:1's
assert not any(w in HB0(303, r) for r in range(1, 21) for w in ('הן קרבו ימיך', 'קרבו ימיך למות')) and HB0(303, 20).startswith('(דברים כו טו) השקיפה ממעון קדשך') and HB0(304, 1).startswith('(דברים לא יד) ויאמר ה׳ אל משה הן קרבו ימיך למות') and HB0(305, 1).startswith('(במדבר כז יח) ויאמר ה׳ אל משה קח לך את יהושע בן נון') and HB0(305, 6).startswith('וכיון שמת משה היה יהושע בוכה') and HB0(306, 1).startswith('(דברים לב א) האזינו השמים ואדברה')
assert all(clean(sif[p - 1][0]).startswith('Pisqa’ %d' % p) for p in PISKAOT) and 'your days are dwindling' in clean(sif[303][0]) and 'Take for yourself Joshua' in clean(sif[304][0]) and 'Lend an ear, Heavens' in clean(sif[305][0])   # the English rows open with the translator's apparatus (H:293-294; JN2:289-290) before the text — the first pass read [:160] and fell on 305:1 (retyped from the print), (clean(sif[303][0])[:100], clean(sif[304][0])[:100])
# THE CITATIONS PARSED FROM THE THREE DUMPS' PRINTS (the instrument's own lists read back): the row-citations per file, the union, the outside sets; the divisions
import ast as _ast
_DUMP = {}; _HE = {}; _EN = {}
for _c in CHS:
    _t = open(os.path.join(os.path.dirname(os.path.abspath(__file__)), f'ch{_c}_dump0.out'), encoding='utf-8').read()
    _HE[_c] = _ast.literal_eval(re.search(r'^  HE rows citing Deut %d[^:]*: \d+ (\[.*\])$' % _c, _t, re.M).group(1)); _EN[_c] = _ast.literal_eval(re.search(r'^  EN rows citing Deut %d[^:]*: \d+ (\[.*\])$' % _c, _t, re.M).group(1))
    _un = int(re.search(r'^  the union of rows \(both files\): (\d+) \[', _t, re.M).group(1)); _out = _ast.literal_eval(re.search(r'^  the rows OUTSIDE the spine piskaot [^:]*: \d+ (\[.*?\]) \|', _t, re.M).group(1))
    _two = re.search(r'^  DB verses (\d+) \| export verses HE (\d+) EN (\d+) \| per-chapter export lengths vs DB, chapters 1-31: (\[.*\])$', _t, re.M); _cost = int(re.search(r'^  the alignment cost (\d+) \|', _t, re.M).group(1))
    _mis = _ast.literal_eval(re.search(r'verses whose store token count differs from the DB: (\[.*?\])$', _t, re.M).group(1))
    _DUMP[_c] = (len(_HE[_c]), len(_EN[_c]), _un, _out, tuple(int(x) for x in _two.groups()[:3]), _two.group(4), _cost, _mis)
assert {c: v[:3] for c, v in _DUMP.items()} == {29: (4, 4, 4), 30: (2, 4, 3), 31: (16, 23, 17)}, {c: v[:3] for c, v in _DUMP.items()}
assert {c: v[4] for c, v in _DUMP.items()} == {29: (28, 28, 28), 30: (20, 20, 20), 31: (30, 30, 30)} and {c: v[6] for c, v in _DUMP.items()} == {29: 19, 30: 18, 31: 30} and all(v[5] == '[(5, 30, 33)]' for v in _DUMP.values()), 'THE TWO DIVISIONS: the identity in all three; chapter 5 the book\'s one split'
assert {c: v[7] for c, v in _DUMP.items()} == {29: [(29, 22, 25, 24)], 30: [], 31: []}, 'THE STORE = THE DB except at 29:22 (the store one token more — Sodom and Gomorrah, Admah and Zeboiim)'
assert _DUMP[29][3] == [(43, 29), (48, 9), (148, 8), (345, 2)] and _DUMP[30][3] == [(53, 1), (306, 2), (306, 15)] and len(_DUMP[31][3]) == 16 and {(305, 2), (305, 6)} <= set(_DUMP[31][3])
# THE OUTSIDE ROWS' FACTS COMPUTED from the dumps' lists: the verses each row cites (the DB's numbering), the heads of their piskaot, the prior reads from the ledgers, the fresh rows
CITED = {}
for _c in CHS:
    for _p, _r, _e, _dbv in _HE[_c] + _EN[_c]:
        if (_p, _r) in OUTSIDE:
            for _d in _dbv: CITED.setdefault((_p, _r), set()).add((_c, _d))
CITED = {k: sorted(v) for k, v in sorted(CITED.items())}
assert sorted(CITED) == OUTSIDE, (sorted(set(OUTSIDE) - set(CITED)), sorted(set(CITED) - set(OUTSIDE)))
assert CITED[(48, 9)] == [(29, 9), (31, 21)] and CITED[(306, 15)] == [(30, 19), (31, 19), (31, 21)] and CITED[(43, 29)] == [(29, 27)] and CITED[(1, 1)] == [(31, 9), (31, 22)], (CITED[(48, 9)], CITED[(306, 15)], CITED[(1, 1)])
HEADS_ON = {p: heads[p] for p in sorted({p for p, _ in OUTSIDE})}
assert HEADS_ON[1] == (1, 1) and HEADS_ON[2] == (1, 2) and HEADS_ON[29] == (3, 26) and HEADS_ON[43] == (11, 15) and HEADS_ON[48] == (11, 22) and HEADS_ON[53] == (11, 26) and HEADS_ON[109] == (14, 28) and HEADS_ON[111] == (15, 1) and HEADS_ON[148] == (17, 2) and HEADS_ON[157] == (17, 15) and HEADS_ON[160] == (17, 18) and HEADS_ON[302] == (26, 12) and HEADS_ON[306] == (32, 1) and HEADS_ON[318] == (32, 15) and HEADS_ON[334] == (32, 44) and HEADS_ON[345] == (33, 4) and HEADS_ON[357] == (34, 1), HEADS_ON   # 334 heads on 32:44 (the song's close), not on 33 — the first pass guessed the chapter, the print corrected it
_TRI = f'{ROOT}/logic/oral_triage'
LED = {f: open(f'{_TRI}/{f}', encoding='utf-8').read() for f in os.listdir(_TRI) if f.endswith('.md') and os.path.isfile(f'{_TRI}/{f}') and f != os.path.basename(OUT)}
SPINE_PRIOR = sorted({(f, int(a), int(b)) for f, t in LED.items() for a, b in re.findall(r'Sifrei Devarim (\d+):(\d+)', t) if int(a) in PISKAOT})
PRIOR_READ = {}
for f, t in LED.items():
    for a, b in re.findall(r'Sifrei Devarim (\d+):(\d+)', t):
        if (int(a), int(b)) in OUTSIDE: PRIOR_READ.setdefault((int(a), int(b)), []).append(f)
PRIOR_READ = {k: sorted(set(v)) for k, v in sorted(PRIOR_READ.items())}
FRESH = [k for k in OUTSIDE if k not in PRIOR_READ]
assert SPINE_PRIOR == [], SPINE_PRIOR   # no spine row of 304-305 read before (the Sifrei's rows on Moses' death and Joshua's commission are new to the ledgers)
assert FRESH == [(306, 2), (306, 15), (334, 1), (345, 2), (357, 28)] and (318, 1) in PRIOR_READ, (FRESH, PRIOR_READ.get((318, 1)))   # FIVE fresh rows from Haazinu's and Vezot Habrachah's piskaot; 318:1 (on 32:15) READ BEFORE — the first pass counted it fresh, the ledgers corrected it
# ---- THE ASSERTS TYPED FROM THE MEASURE'S PRINT (block b: ch29_measure_lean.out — the kin, the twins, the formulas, Onkelos, the register, the parser, the prior reads) ----
# THE KIN BY COMPUTATION (the closest re-scored in order): 29:1's closest 5:1 (eight in order — 'and Moses called to all Israel and said to them'); 29:6 3:1 (Og's five); 29:12 9:5 (the fathers' oath, six); 29:19 and 29:26 each other's ('the curse written in this book'); 29:23's closest 1 KINGS 9:8 (seven of nine — 'why has the LORD done thus to this land', the Prophets' seat cited never read); 30:9 28:11 (the fruit of womb, beast and ground, six of eight); 30:12 and 30:13 each other's (six of nine); 30:18 4:26 (six of seven); 30:20 1:8 and 6:10 (the oath to the three fathers); 31:1 Numbers 14:39 (four of seven); 31:6 and 31:8 each other's; 31:7 JOSHUA 1:6 (six of eleven — cited, not read) and Numbers 20:12; 31:9 and 31:22 (the writing); 31:15 Numbers 12:5 (the pillar of cloud at the Tent); 31:16 Exodus 32:9; 31:23 Numbers 32:28; 31:30 32:44; 30:5 NO KIN AT ALL by shared tokens
assert KINC[(29, 1)][0] == ('Deut 5:1', 5, 8) and KINC[(29, 6)][0] == ('Deut 3:1', 5, 5) and KINC[(29, 12)][0] == ('Deut 9:5', 6, 6) and KINC[(29, 19)][0] == ('Deut 29:26', 5, 7) and KINC[(29, 26)][0] == ('Deut 29:19', 5, 7) and KINC[(29, 23)][0] == ('1Kgs 9:8', 7, 9) and KINC[(29, 28)][0] == ('Deut 6:25', 4, 5), (KINC[(29, 1)][0], KINC[(29, 23)][0])
assert KINC[(30, 9)][0] == ('Deut 28:11', 6, 8) and KINC[(30, 12)][0] == ('Deut 30:13', 6, 9) and KINC[(30, 13)][0] == ('Deut 30:12', 6, 9) and KINC[(30, 18)][0] == ('Deut 4:26', 6, 7) and KINC[(30, 20)][0] == ('Deut 1:8', 6, 9) and KINC[(30, 5)] == [], (KINC[(30, 9)][0], KINC[(30, 5)])
assert KINC[(31, 1)][0] == ('Num 14:39', 4, 7) and KINC[(31, 6)][0] == ('Deut 31:8', 4, 7) and KINC[(31, 7)][0] == ('Josh 1:6', 6, 11) and KINC[(31, 9)][0] == ('Deut 31:22', 5, 6) and KINC[(31, 15)][0] == ('Num 12:5', 5, 6) and KINC[(31, 16)][0] == ('Exod 32:9', 5, 7) and KINC[(31, 23)][0] == ('Num 32:28', 6, 6) and KINC[(31, 30)][0] == ('Deut 32:44', 6, 5), (KINC[(31, 7)][0], KINC[(31, 16)][0])
# THE TWINS DIFFED (shared / the longest run): the calls of 29:1 and 5:1 seven in order; 29:23 and 1 Kings 9:8 seven; 29:28, 28:58 and 31:12 'to do all the words of this law' six; 30:2 and 4:30 six ('and return to the LORD your God and hearken to His voice'); 30:6 and 6:5 seven (all your heart and all your soul); 30:9 and 28:11 six (the three fruits), 30:9 and 28:63 'as He rejoiced' two; 30:12 and 30:13 five ('bring it to us that we may hear it and do it'); 30:18 and 30:19 against 4:26 seven ('I call heaven and earth to witness against you this day'); 31:1 and 32:45 five; 31:2 and 34:7 four (a hundred and twenty), 31:2 and 3:27 five ('you shall not cross this Jordan'); 31:6 and 31:8 five ('He will not fail you nor forsake you'); 31:7 and 31:23 ten shared; 31:9 and 10:8 four (the ark of the covenant); 31:10 and 15:1 three (at the end of seven years) but 16:13 NOTHING (the feast's spelling); 31:11 and 16:16 seven (before the LORD at the place He chooses); 31:15 and Numbers 12:5 three; 31:16 and 31:20 three ('and break My covenant'); 31:21 and 31:17 three (many evils and troubles); 31:23 and 1:38 three (Joshua son of Nun)
assert SHARED(('Deut', 29, 1), ('Deut', 5, 1)) == ['ויקרא', 'משה', 'אל', 'כל', 'ישראל', 'ויאמר', 'אלהם'] and SHN(('Deut', 29, 23), ('1Kgs', 9, 8)) == 9 and len(SHARED(('Deut', 29, 23), ('1Kgs', 9, 8))) == 7 and SHARED(('Deut', 29, 28), ('Deut', 28, 58)) == ['לעשות', 'את', 'כל', 'דברי', 'התורה', 'הזאת'] == SHARED(('Deut', 29, 28), ('Deut', 31, 12))
assert SHARED(('Deut', 30, 2), ('Deut', 4, 30)) == ['ושבת', 'עד', 'יהוה', 'אלהיך', 'ושמעת', 'בקלו'] and len(SHARED(('Deut', 30, 6), ('Deut', 6, 5))) == 7 and SHARED(('Deut', 30, 9), ('Deut', 28, 11)) == ['בפרי', 'בטנך', 'ובפרי', 'בהמתך', 'ובפרי', 'אדמתך'] and SHARED(('Deut', 30, 9), ('Deut', 28, 63)) == ['כאשר', 'שש'] and SHN(('Deut', 30, 12), ('Deut', 30, 13)) == 9 and SHARED(('Deut', 30, 19), ('Deut', 4, 26)) == ['העידתי', 'בכם', 'היום', 'את', 'השמים', 'ואת', 'הארץ']
assert SHARED(('Deut', 31, 2), ('Deut', 34, 7)) == ['בן', 'מאה', 'ועשרים', 'שנה'] and SHARED(('Deut', 31, 2), ('Deut', 3, 27)) == ['לא', 'תעבר', 'את', 'הירדן', 'הזה'] and SHARED(('Deut', 31, 6), ('Deut', 31, 8)) == ['עמך', 'לא', 'ירפך', 'ולא', 'יעזבך'] and SHN(('Deut', 31, 7), ('Deut', 31, 23)) == 10 and SHARED(('Deut', 31, 9), ('Deut', 10, 8)) == ['את', 'ארון', 'ברית', 'יהוה'] and SHARED(('Deut', 31, 10), ('Deut', 15, 1)) == ['מקץ', 'שבע', 'שנים'] and SHN(('Deut', 31, 10), ('Deut', 16, 13)) == 0 and len(SHARED(('Deut', 31, 11), ('Deut', 16, 16))) == 7 and SHARED(('Deut', 31, 16), ('Deut', 31, 20)) == ['והפר', 'את', 'בריתי'] and SHARED(('Deut', 31, 21), ('Deut', 31, 17)) == ['רעות', 'רבות', 'וצרות'] and SHARED(('Deut', 31, 23), ('Deut', 1, 38)) == ['יהושע', 'בן', 'נון']
# THE FORMULAS (phrase seats by consonants over the Torah and the Bible)
assert P('כאשר', 'נשבע', 'לאבתיך', books=T) == ['Deut 13:18', 'Deut 19:8'] and 'Deut 29:12' in P('לאברהם', 'ליצחק', 'וליעקב', books=T) and 'Deut 30:20' in P('לאברהם', 'ליצחק', 'וליעקב', books=T) and len(P('לאברהם', 'ליצחק', 'וליעקב', books=T)) == 11   # 29:12's and 30:20's oath formulas carry a prefix or the Name between — the bare phrase misses them (sitting 18's lesson 3)
assert P('הברכה', 'והקללה', books=T) == ['Deut 30:1', 'Deut 30:19'] and P('הברכה', 'והקללה', books=None) == ['Deut 30:1', 'Deut 30:19', 'Josh 8:34'] and P('העידתי', 'בכם', 'היום', books=T) == ['Deut 30:19', 'Deut 4:26'] and P('החיים', 'והמות', books=None) == ['Deut 30:19'] and len(P('את', 'השמים', 'ואת', 'הארץ', books=T)) == 6
assert len(P('דברי', 'התורה', 'הזאת', books=None)) == 9 and P('בספר', 'הזה', books=T) == ['Deut 28:58', 'Deut 29:19', 'Deut 29:26'] and P('ספר', 'התורה', 'הזה', books=None) == ['Deut 31:26', 'Josh 1:8'] and len(P('אלהים', 'אחרים', books=T)) == 19 and len(P('בכל', 'לבבך', 'ובכל', 'נפשך', books=None)) == 7 and P('והסתרתי', 'פני', books=None) == ['Deut 31:17']
assert P('חזק', 'ואמץ', books=T) == ['Deut 31:23', 'Deut 31:7'] and len(P('חזק', 'ואמץ', books=None)) == 9 and P('חזקו', 'ואמצו', books=T) == ['Deut 31:6'] and P('מאה', 'ועשרים', 'שנה', books=None) == ['Deut 31:2', 'Deut 34:7', 'Gen 6:3'] and P('מקץ', 'שבע', 'שנים', books=None) == ['Deut 15:1', 'Deut 31:10', 'Jer 34:14'] and P('בחג', 'הסכות', books=None) == ['Deut 31:10']
assert P('ארון', 'ברית', 'יהוה', books=T) == ['Deut 10:8', 'Deut 31:25', 'Deut 31:26', 'Deut 31:9'] and len(P('ארון', 'ברית', 'יהוה', books=None)) == 24 and P('בעמוד', 'ענן', books=T) == ['Deut 31:15', 'Exod 13:21', 'Num 12:5'] and P('ערפך', 'הקשה', books=None) == ['Deut 31:27'] and P('קשה', 'ערף', books=None) == ['Deut 9:13', 'Deut 9:6', 'Exod 32:9', 'Exod 33:3', 'Exod 33:5', 'Exod 34:9']   # 31:27's stiff neck in the reversed order — the six calf seats of the phrase stand (the chapter 9 runner's assert holds; the word scan will meet 31:27 at the compile)
assert 'Deut 31:20' in P('זבת', 'חלב', 'ודבש', books=T) and len(P('זבת', 'חלב', 'ודבש', books=T)) == 15 and P('סדם', 'ועמרה', books=T) == ['Deut 29:22', 'Gen 14:10', 'Gen 14:11', 'Gen 18:20', 'Gen 19:28'] and P('אדמה', 'וצבים', books=None) == [] and 'וצביים' in W(29, 22)   # Zeboiim is spelled with two yods in the DB (the ketiv) — the search with one yod misses; the store one token more at 29:22 (the qere beside)
assert P('עץ', 'ואבן', books=T) == ['Deut 28:36', 'Deut 28:64', 'Deut 29:16', 'Deut 4:28'] and P('בקצה', 'השמים', books=None) == ['Deut 30:4', 'Neh 1:9'] and P('לא', 'בשמים', 'הוא', books=None) == ['Deut 30:12'] and P('בפיך', 'ובלבבך', books=None) == ['Deut 30:14'] and P('שכב', 'עם', 'אבתיך', books=None) == ['Deut 31:16'] and P('הנסתרת', books=None) == ['Deut 29:28'] and P('ראש', 'ולענה', books=None) == ['Deut 29:17'] and P('גפרית', 'ומלח', books=None) == ['Deut 29:22'] and P('כאשר', 'שש', 'על', 'אבתיך', books=None) == ['Deut 30:9']
assert len(P('השירה', 'הזאת', books=T)) == 7 and P('השירה', 'הזאת', books=None)[:1] == ['2Sam 22:1'] and len(P('השירה', 'הזאת', books=None)) == 9 and P('לעד', 'בבני', 'ישראל', books=None) == ['Deut 31:19']
assert [(c, v) for c, v in SPAN for x in W(c, v) if x in ('ברית', 'הברית', 'בברית', 'בריתי', 'בריתו')] == [(29, 8), (29, 11), (29, 13), (29, 20), (29, 24), (31, 9), (31, 16), (31, 20), (31, 25), (31, 26)] and [(c, v, x) for c, v in SPAN for x in W(c, v) if x.startswith(('ושב', 'ישוב', 'תשוב', 'והשבת', 'ושבת')) and not x.startswith('ושבע')] == [(30, 1, 'והשבת'), (30, 2, 'ושבת'), (30, 3, 'ושב'), (30, 3, 'ושב'), (30, 8, 'תשוב'), (30, 9, 'ישוב'), (30, 10, 'תשוב')]   # the covenant ten times in 29 and 31, never in 30; the return SEVEN times in chapter 30 alone (its root; 31:20's 'sated' the seven's other homograph)
assert {c: sum(1 for v in range(1, NV[c] + 1) for x in W(c, v) if x in ('לא', 'ולא')) for c in CHS} == {29: 12, 30: 6, 31: 10} and [(c, v) for c, v in SPAN if 'אם' in W(c, v) or 'ואם' in W(c, v)] == [(30, 4), (30, 17)] and [(c, v) for c, v in SPAN if 'פן' in W(c, v) or 'ופן' in W(c, v)] == [(29, 17)] and [f'{c}:{v}' for c, v in SPAN if 'לאמר' in W(c, v)] == ['29:18', '30:12', '30:13', '31:10', '31:25']
# ONKELOS OVER THE BOOK (the export's rows through NFKC): the oath 'momata' at 29:11, 13, 18 alone in Deuteronomy; the hidden face RENDERED 'I will remove My Shekhinah' at 31:17, 31:18 and 32:20; the song 'tushbachta'; the release 'shemitta' at 15:1-9 and 31:10; the booths 'metaliya'; the stiff neck 'kedal' at 9:6, 9:13, 10:16 and 31:27; the hidden 'mitamran' at 29:28 and 33:19; the heart's foreskin rendered 'the folly of your heart' at 30:6 (ARM 20 against HE 18); 29:17 two tokens more ('a man thinking sins or rebellion')
assert SEATS('מומת') == [(29, 11), (29, 13), (29, 18)] and SEATS('אסלק') == [(31, 17), (31, 18), (32, 20)] and SEATS('תושבח') == [(31, 22), (31, 30)] and SEATS('שמטת') == [(15, 1), (15, 2), (15, 9), (31, 10)] and SEATS('מטלי') == [(14, 24), (16, 13), (16, 16), (31, 10)] and SEATS('קדל') == [(9, 6), (9, 13), (10, 16), (31, 27)] and SEATS('מטמר') == [(29, 28), (33, 19)] and SEATS('ארונ') == [(10, 1), (10, 2), (10, 3), (10, 5), (31, 26)] and SEATS('עמודא דעננא') == [(1, 33), (31, 15)] and len(SEATS('טעות')) == 32 and len(SEATS('קימ')) == 73
assert 'טפשות לבך' in ' '.join(ARM(30, 6)) and (len(W(30, 6)), len(ARM(30, 6))) == (18, 20) and (len(W(29, 17)), len(ARM(29, 17))) == (30, 32) and 'מהרהר חטאין' in ' '.join(ARM(29, 17)) and (len(W(31, 9)), len(ARM(31, 9))) == (19, 17) and 'שכנתי' in ' '.join(ARM(31, 17)) and 'בחיי' in ' '.join(ARM(30, 19)) and 'בר מאה ועשרין שנין' in ' '.join(ARM(31, 2))
# THE FRAMES, THE REGISTER AND THE PARSER: the imperatives (30:15 see; 31:6 be strong plural; 31:7 and 31:23 singular; 31:12 gather; 31:14 call, present yourselves; 31:19 write, teach, put; 31:28 assemble); "the LORD your God" paired at ELEVEN verses of chapter 30 (its refrain), at 29:11 alone in 29, at 31:3, 6, 11; NO REGISTER SEAT in the three chapters (no receipt, header or footer — the register file untouched at the compile); THE PARSER: 29:4 forty, 29:7 the half (starred %), 30:9 SIX the false hit ('rejoiced' — 28:63's twin), 31:2 a hundred and twenty, 31:10 seven (years starred), 31:20 'sated' starred with no number; 'swore' (nishba) at 29:12, 30:20, 31:7 not counted
MO = {(c, v): [(x, m) for x, m in by[('Deut', c, v)]] for c, v in SPAN}
assert [(c, v, x) for c, v in SPAN for x, m in MO[(c, v)] if m and re.search(r'V[a-zA-Z]v', m)] == [(30, 15, 'ראה'), (31, 6, 'חזקו'), (31, 6, 'ואמצו'), (31, 7, 'חזק'), (31, 7, 'ואמץ'), (31, 12, 'הקהל'), (31, 14, 'קרא'), (31, 14, 'והתיצבו'), (31, 19, 'כתבו'), (31, 19, 'ולמדה'), (31, 19, 'שימה'), (31, 23, 'חזק'), (31, 23, 'ואמץ'), (31, 28, 'הקהילו')]
assert {c: [v for v in range(1, NV[c] + 1) if any(a == 'יהוה' and b == 'אלהיך' for a, b in zip(W(c, v), W(c, v)[1:]))] for c in CHS} == {29: [11], 30: [1, 2, 3, 4, 5, 6, 7, 9, 10, 16, 20], 31: [3, 6, 11]} and {c: sum(1 for v in range(1, NV[c] + 1) for x in W(c, v) if x == 'יהוה') for c in CHS} == {29: 18, 30: 18, 31: 17}
_MP = open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'ch29_measure_lean.out'), encoding='utf-8').read()
assert "the register on Deut 29-31 — receipts: [] | footers: [] | headers: []" in _MP, 'the register: no seat in the three chapters'
assert "the parser's hits: {(29, 4): ([40], [], []), (29, 7): ([Fraction(1, 2)], [], ['ולחצי%']), (30, 9): ([6], [], []), (31, 2): ([120], [], []), (31, 10): ([7], [], ['שנים*']), (31, 20): ([], [], ['ושבע*'])}" in _MP and "29:12 \"swore\": ['וכאשר', 'נשבע']" in _MP, 'the parser as printed'
# THE STORE AND THE PRIOR READS: the store = the DB except 29:22 (one token more — Zeboiim's ketiv and qere); eight '?' glosses, all the pronoun I (29:5 ani; 29:13, 30:2, 30:8, 30:11, 30:16, 31:2, 31:27 anokhi) — a display patch at the tail; FOURTEEN of the nineteen outside rows READ BEFORE (chapters 1-3, 8, 11, 14-15, 17, 26, 32:15's 318:1), FIVE fresh (Haazinu's 306:2, 306:15, 334:1; Vezot Habrachah's 345:2, 357:28); no Onkelos of 29-34 or the Prophets in any ledger
assert STORE_MISMATCH == [(29, 22, 25, 24)] and [(cc, v, hp) for (cc, v) in SG for _, hp, g in SG[(cc, v)] if g == '?'] == [(29, 5, 'אני'), (29, 13, 'אנכי'), (30, 2, 'אנכי'), (30, 8, 'אנכי'), (30, 11, 'אנכי'), (30, 16, 'אנכי'), (31, 2, 'אנכי'), (31, 27, 'אנכי')] and {c: sum(len(W(c, v)) for v in range(1, NV[c] + 1)) for c in CHS} == {29: 439, 30: 326, 31: 553}
assert len(PRIOR_READ) == 14 and len(FRESH) == 5 and PRIOR_READ[(1, 1)] == ['deu_01_03_devarim_2026-09-15.md'] and PRIOR_READ[(43, 7)] == ['deu_08_ekev_2026-09-18.md', 'deu_11_ekev_reeh_2026-09-20.md'] and not [f for f, t in LED.items() if re.search(r'^- Onkelos (?:Deut (?:29|3\d)|Josh|Judg|1Sam|2Sam|1Kgs|2Kgs|Isa|Jer|Ezek):', t, re.M)], (len(PRIOR_READ), FRESH)

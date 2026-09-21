import os as _os
_ROOT = _os.path.normpath(_os.path.join(_os.path.dirname(_os.path.abspath(__file__)), '..', '..', '..'))   # THE PORTABLE REPO (2026-09-15): the repo root from this file's own place
#!/usr/bin/env python3
# THE DEUTERONOMY WALK, sitting 10 — CHAPTER 12, Deuteronomy 12:1-31 (2026-09-20; the owner: "Monitor how long each step takes and report when the chapter is
# done"; ONE RUN + ITS TAIL under THE COST RULES A-B-C — the rereads, the measurements, the ink, the design, the rows, the ledger, the seat, the chain LAUNCHED,
# the tail): THE INK of the chapter, computed from the Tanakh DB, the snapshot store and the shelf's own bytes — never typed. Sitting 9's form (ch11_ink.py): the
# generic helpers copied by derive_ch12_ink.py from that file by content markers, the constants and every assert chapter 12's own, typed FROM THE PRINTS
# (ch12_dump0.out, ch12_measure1.out). THE TWO DIVISIONS AGREE (31 = 31; the alignment the identity, cost 26) — THE CHAPTER IS THIRTY-ONE VERSES IN THE DB'S
# NUMBERING (the English's 12:32 is the Hebrew's 13:1; chapter 11's ink measured it). THE SPINE IS ON THE CHAPTER — TWENTY-THREE piskaot (59-81) with 159 rows:
# twenty heads computed in chapter 12 (59 on 12:1 … 81 on 12:30) and THREE PISKAOT WITHOUT A HEAD CITATION (68 opening with 12:11's "your burnt offerings", 73
# with 12:17's "your herd and your flock", 74 with 12:17's "your vows" — chapter 11's lesson 2, the membership decided on the consonants); SEVEN rows elsewhere
# cite it by the union of both files (2:2 the rest of 12:9 at the book's head, 106:5 and 147:2 the tithe's "you may not eat" at 14:23 and 17:1, 138:1 the
# rejoicing at 16:11, 145:3 the Asherah at 16:21, 179:2 the dwelling at 19:1, 286:16 the blood at 25:1), NONE excluded (the English's "(Dt.13:29)" at 179:2 a
# wrong chapter for 12:29 — the Hebrew right). The parser MEASURED on every verse — ONE NUMBER VERSE (12:14 "in one of your tribes" [1]) and ONE STARRED TOKEN
# (12:17's "tithe", the ten-word's homograph). THE STORE = THE DB at every verse (no written/read pair; 520 tokens, 2,051 letters; the four "?" glosses the
# store's "I"). The hand's facts as asserts, run all at once by assert_driver.py.
import json, os, re, html, sqlite3, sys, io, contextlib, unicodedata, subprocess
from collections import Counter
ROOT = _ROOT
sys.path.insert(0, f'{ROOT}/World/step9')
DATE = '2026-09-20'
CH = 12
UIDS = ['deu_12_place_name']
SPANS = {'deu_12_place_name': (12, 1, 31)}
PREFIX = {'deu_12_place_name': 'DV12'}
PISKAOT = list(range(59, 82))   # THE SPINE ON THE CHAPTER: twenty-three piskaot 59-81 — twenty heads computed in chapter 12 (the A print) and the three headless piskaot 68, 73, 74 whose first rows open with 12:11's and 12:17's own words; 58 on 11:32 before, 82 on 13:1 after
HEADLESS = [68, 73, 74]
SPINE_ROWS = {59: 5, 60: 4, 61: 8, 62: 4, 63: 11, 64: 5, 65: 6, 66: 2, 67: 4, 68: 6, 69: 4, 70: 6, 71: 14, 72: 11, 73: 1, 74: 9, 75: 15, 76: 9, 77: 9, 78: 10, 79: 5, 80: 5, 81: 6}   # rows per piska, both files (the I print and the splitter's) — 159
EXP2DB = {e: [e] for e in range(1, 32)}   # the identity — 31 = 31 (chapter 5 the book's one split)
DB2EXP = {d: e for e, ds in EXP2DB.items() for d in ds}
# the Hebrew's book-named citations of chapter 12 OUTSIDE the spine (the regex reads "(דברים יב ט)" etc.); 138:1's Hebrew cites 27:7 alone, its English adds (Dt.12:7)
OUTSIDE_HE = [(2, 2, (12, 9)), (106, 5, (12, 17)), (145, 3, (12, 3)), (147, 2, (12, 17)), (179, 2, (12, 29)), (286, 16, (12, 23))]
OUTSIDE = [(2, 2), (106, 5), (138, 1), (145, 3), (147, 2), (179, 2), (286, 16)]   # the SEVEN rows READ WHOLE: the union of both files beyond piskaot 59-81
EXCLUDED = []   # every outside citation genuine (179:2's English writes '(Dt.13:29)' for 12:29 — a wrong chapter in the English, the Hebrew's citation right; the row stays)
INTERPOLATION = []
CITED = {(2, 2): [9], (106, 5): [17], (138, 1): [7], (145, 3): [3], (147, 2): [17], (179, 2): [29], (286, 16): [23]}
CITED_DB = {k: v[0] for k, v in CITED.items()}
PRIOR_READ = {(2, 2): 'deu_01_03_devarim_2026-09-15.md'}   # one read before at sitting 1 (the eleven days) — REREAD WHOLE here
HEADS_ON = {2: (1, 2), 106: (14, 23), 138: (16, 11), 145: (16, 21), 147: (17, 1), 179: (19, 1), 286: (25, 1)}
FRESH = OUTSIDE[:]
CREDITED = {}   # under THE WHOLE-ROW RULE no spine row is credited: the five reads of four rows before (61:7 at chapter 7, 80:4-5 at chapter 11, 75:2 at two Genesis sittings) are REREAD WHOLE here and marked so
TITLE = "Chapter 12 — These are the statutes and the judgments for the land; destroy, you shall destroy all the places where the nations served their gods — the altars torn down, the pillars broken, the Asherim burned, the images cut down, the name destroyed from that place; not so to the LORD your God: the place which the LORD will choose from all your tribes to put His name there — His dwelling you shall seek, there you shall bring the burnt offerings, the sacrifices, the tithes, the heave offering, the vows, the freewill offerings, the firstlings, and eat before Him and rejoice, you and your households; not as we do here today, every man what is right in his eyes, for you have not yet come to the rest and the inheritance; across the Jordan, with rest from every enemy, the place chosen and the Levite in your gates with no portion; take heed lest you offer in every place you see — only in the place, in one of your tribes; only, with all the desire of your soul you may slaughter and eat flesh in all your gates, the unclean and the clean alike, as the gazelle and the hart — only the blood you shall not eat, on the earth you shall pour it like water; the tithe and the firstlings and the vows not in your gates but before the LORD in the place, with your household and the Levite — take heed lest you forsake him; when the border is enlarged as He spoke and the place is far, slaughter of your herd and flock as I have commanded you and eat in your gates; only be steadfast not to eat the blood, for the blood is the life; your holy things and your vows carried to the place, the flesh and the blood on the altar, the blood poured, the flesh eaten; observe and hear all these words that it may go well with you and your children forever; when the nations are cut off, take heed lest you be ensnared to inquire after their gods — every abomination of the LORD which He hates they did for their gods, even their sons and their daughters they burn in the fire"
OUT = f'{ROOT}/logic/oral_triage/deu_12_reeh_{DATE}.md'
db = sqlite3.connect(f'file:{ROOT}/Data/tanakh.sqlite?mode=ro', uri=True)
# ---- THE HELPERS (ch11_ink.py's, copied by content markers) ----
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
# ---- THE INK'S HELPERS, THE DB AND THE STORE (ch11_ink.py's, the chapter substituted) ----
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
def W12(v): return words('Deut', 12, v)
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
for c, v, idx, hp, g in store.execute("SELECT v.chapter, v.verse, w.idx, w.he_plain, w.gloss FROM words w JOIN verses v ON w.verse_id=v.id WHERE v.book='Deut' AND v.chapter = 12 ORDER BY v.id, w.idx"):
    SG.setdefault((c, v), []).append((idx, hp.replace('/', ''), g))
def sg(c, v, tok, nth=0):
    hit = [g for _, hp, g in SG[(c, v)] if hp == tok]
    if len(hit) <= nth: raise KeyError((c, v, tok, nth))
    return hit[nth]
def sidx(c, v, tok, nth=0):
    hit = [i for i, hp, _ in SG[(c, v)] if hp == tok]
    assert len(hit) > nth, (c, v, tok, nth, hit)
    return hit[nth]
STORE_MISMATCH = [(c, v, n, len(by[('Deut', c, v)])) for c, v, n in store.execute("SELECT v.chapter, v.verse, COUNT(*) FROM words w JOIN verses v ON w.verse_id=v.id WHERE v.book='Deut' AND v.chapter=12 GROUP BY v.chapter, v.verse").fetchall() if n != len(by[('Deut', c, v)])]
import difflib
def SH(a, b_): return sum(s for _, _, s in difflib.SequenceMatcher(a=words(*a), b=words(*b_)).get_matching_blocks())
D12 = lambda v: ('Deut', 12, v)
# ---- THE SHELF BY POSITION — the spine ON the chapter: twenty-three piskaot (59-81) — twenty heads in chapter 12 and three headless (68, 73, 74) whose first rows open with the chapter's own words; 58 on 11:32 before, 82 on 13:1 after; the two files' grains ----
assert len(sif) == 357 and len(sif_he) == 357 and sum(len(s) for s in sif) == 2357 and sum(len(s) for s in sif_he) == 2357
HC = Counter(h[0] for h in heads.values() if h)
assert [p for p, h in heads.items() if h and h[0] == 12] == [p for p in PISKAOT if p not in HEADLESS] and HC[12] == 20 and sorted(HC.items())[:12] == [(1, 24), (3, 4), (6, 6), (11, 21), (12, 20), (13, 14), (14, 14), (15, 16), (16, 19), (17, 16), (18, 16), (19, 10)], sorted(HC.items())[:12]
assert {p: heads[p] for p in range(58, 83)} == {58: (11, 32), 59: (12, 1), 60: (12, 2), 61: (12, 3), 62: (12, 5), 63: (12, 5), 64: (12, 7), 65: (12, 8), 66: (12, 9), 67: (12, 10), 68: None, 69: (12, 12), 70: (12, 13), 71: (12, 15), 72: (12, 17), 73: None, 74: None, 75: (12, 20), 76: (12, 23), 77: (12, 26), 78: (12, 27), 79: (12, 28), 80: (12, 29), 81: (12, 30), 82: (13, 1)}, {p: heads[p] for p in range(58, 83)}
# THE THREE HEADLESS PISKAOT: their first rows open with the chapter's own words (12:11's, 12:17's, 12:17's) — the spine's, not outside rows (chapter 11's lesson 2 at 45)
assert HB0(68, 1).startswith('עולתיכם') and '(Dt.12:11)' in E(68, 1) and he_cites(Hb(68, 1)) == [] and HB0(73, 1).startswith('בקרך וצאנך') and '(Dt.12:17)' in E(73, 1) and HB0(74, 1).startswith('נדריך') and '(Dt.12:17)' in E(74, 1) and he_cites(Hb(74, 2)) == [('דברים', 12, 18)] and he_cites(Hb(74, 6)) == [('דברים', 12, 19)]
assert 'עולתיכם' in W12(11) and 'בקרך' in W12(17) and 'וצאנך' in W12(17) and 'נדריך' in W12(17) and 'עלתיכם' in W12(6)   # 12:11's plene "your burnt offerings" (68:1's word) against 12:6's defective
assert {p: (len(sif_he[p - 1]), len(sif[p - 1])) for p in PISKAOT} == {p: (n, n) for p, n in SPINE_ROWS.items()} and sum(SPINE_ROWS.values()) == 159 and len(PISKAOT) == 23
CIT_HE = [(p, r, (12, c[2])) for p in range(1, 358) for r in range(1, len(sif_he[p - 1]) + 1) for c in he_cites(Hb(p, r)) if c[0] == 'דברים' and c[1] == 12]
CIT_EN = [(p, r, (12, int(m.group(2)))) for p in range(1, 358) for r in range(1, len(sif[p - 1]) + 1) for m in re.finditer(r'\((?:Deut(?:eronomy)?\.?|Dt\.?|Devarim) ?(12):(\d+)', E(p, r))]
assert len(CIT_HE) == 42 and len(CIT_EN) == 195, (len(CIT_HE), len(CIT_EN))
assert [(p, r, v) for p, r, v in CIT_HE if p not in PISKAOT] == OUTSIDE_HE
SPINE_CITES_HE = [(p, r, v) for p, r, v in CIT_HE if p in PISKAOT]
assert len(SPINE_CITES_HE) == 36 and SPINE_CITES_HE[:6] == [(59, 1, (12, 1)), (59, 5, (12, 2)), (60, 1, (12, 2)), (61, 1, (12, 3)), (62, 1, (12, 5)), (62, 2, (12, 14))] and (70, 4, (12, 14)) in SPINE_CITES_HE and (70, 4, (12, 5)) in SPINE_CITES_HE and (71, 5, (12, 26)) in SPINE_CITES_HE and (78, 9, (12, 26)) in SPINE_CITES_HE and SPINE_CITES_HE[-1] == (81, 5, (12, 31))   # every head piska's first row cites its verse by name but the three headless; 62:2 and 70:4 cite 12:14 and 12:5 together (one verse says, another verse says); 71:5 and 78:9 reach forward to 12:26
UNION = sorted({(p, r) for p, r, _ in CIT_HE} | {(p, r) for p, r, _ in CIT_EN})
assert len(UNION) == 144 and sorted(set(UNION) - {(p, r) for p, r in UNION if p in PISKAOT}) == sorted(OUTSIDE + EXCLUDED) and len(OUTSIDE) == 7 and len([(p, r) for p, r in UNION if p in PISKAOT]) == 137
assert all(1 <= v <= 31 for _, _, (_, v) in CIT_HE + CIT_EN)   # no cited verse beyond the chapter's thirty-one
assert [(p, r) for p in range(1, 358) for r in range(1, len(sif[p - 1]) + 1) if re.search(r'\((?:Ibid|ibid)\.? ?12:\d+\)', E(p, r))] == []
assert {p: heads[p] for p, _ in OUTSIDE} == HEADS_ON and all(heads[p] == HEADS_ON[p] for p, _ in OUTSIDE), {p: heads[p] for p, _ in OUTSIDE}
assert all(has_points(Hb(p, r)) for p, r in OUTSIDE) and all(has_points(Hb(p, r)) for p in PISKAOT for r in range(1, SPINE_ROWS[p] + 1))
NOCITE = [(p, r) for p in PISKAOT for r in range(1, SPINE_ROWS[p] + 1) if not he_cites(Hb(p, r)) and not re.findall(r'\([A-Z][a-z]+\.? ?\d+:\d+', E(p, r))]
assert NOCITE == [(63, 10), (65, 6), (72, 8), (72, 9), (75, 4), (76, 2), (76, 3), (76, 6), (77, 2), (77, 5), (79, 2)] and len(NOCITE) == 11, NOCITE
# THE ENGLISH'S WRONG CHAPTER at 179:2 (on 19:1): "(Dt.13:29)" for 12:29's "and you shall dwell in their land" — the Hebrew cites (דברים יב כט) rightly; 138:1's Hebrew cites 27:7 alone and the English adds (Dt.12:7); 2:2's range citation "(שמות יג ד-ה)" invisible to the regex (chapter 8's lesson)
assert 'Dt.13:29)' in E(179, 2) and '(Dt.13:29)' not in E(179, 2) and '(Dt.12:29)' not in E(179, 2) and he_cites(Hb(179, 2)) == [('דברים', 12, 29)] and 'וישבת בארצם' in HB0(179, 2)
assert he_cites(Hb(138, 1)) == [('דברים', 16, 11), ('דברים', 27, 7)] and '(Dt.12:7' in E(138, 1) and 'נאמרה כאן שמחה' in HB0(138, 1)
assert ('דברים', 12, 9) in he_cites(Hb(2, 2)) and ('במדבר', 14, 34) in he_cites(Hb(2, 2)) and ('במדבר', 10, 33) in he_cites(Hb(2, 2)) and '(שמות יג ד-ה)' in Hb(2, 2) and 'ואין מנוחה אלא ארץ ישראל' in HB0(2, 2)
assert 'לא תוכל לאכל בשעריך' in HB0(106, 5) and 'מקיש בכור למעשר שני' in HB0(106, 5) and 'קל וחומר שלא יטע' in HB0(145, 3) and ('דברים', 12, 3) in he_cites(Hb(145, 3)) and 'ואין מקדים קדשים זה לזה עובר בלא תעשה' in HB0(147, 2) and 'גזל ועריות' in HB0(286, 16) and ('דברים', 12, 23) in he_cites(Hb(286, 16))
# THE PRIOR READS, computed from the ledgers (never typed): five reads of four spine rows (61:7 at chapter 7 — the renaming; 80:4-5 at chapter 11 — the sages at the border; 75:2 at two Genesis sittings — the Kenite's land) and one outside row (2:2 at sitting 1)
TRI = f'{ROOT}/logic/oral_triage'
LED = {f: open(f'{TRI}/{f}', encoding='utf-8').read() for f in os.listdir(TRI) if f.endswith('.md') and os.path.isfile(f'{TRI}/{f}') and f'{TRI}/{f}' != OUT}
PRIOR = sorted({(f, int(a), int(b)) for f, t in LED.items() for a, b in re.findall(r'Sifrei Devarim (\d+):(\d+)', t)})
SPINE_PRIOR = [(f, p, r) for f, p, r in PRIOR if p in PISKAOT]
assert SPINE_PRIOR == [('deu_07_vaetchanan_ekev_2026-09-17.md', 61, 7), ('deu_11_ekev_reeh_2026-09-20.md', 80, 4), ('deu_11_ekev_reeh_2026-09-20.md', 80, 5), ('gen_27_the_call_2026-08-25.md', 75, 2), ('gen_31_covenant_pieces_2026-08-25.md', 75, 2)] and len(PRIOR) == 501, (SPINE_PRIOR, len(PRIOR))
assert [(f, p, r) for f, p, r in PRIOR if (p, r) in OUTSIDE] == [('deu_01_03_devarim_2026-09-15.md', 2, 2)] and sorted(PRIOR_READ) == [(2, 2)]
assert sorted(f for f, t in LED.items() if re.search(r'^- Onkelos Deut 12:', t, re.M)) == []
NAMING = sorted(f for f, t in LED.items() if re.search(r'Deut(?:eronomy)? 12:\d+', t))
assert len(NAMING) == 28 and NAMING[:4] == ['deu_01_03_devarim_exam_2026-09-15.md', 'deu_07_vaetchanan_ekev_2026-09-17.md', 'deu_11_ekev_reeh_exam_2026-09-20.md', 'erection_docket_2026-09-06.md'] and NAMING[-3:] == ['priesthood_topic_docket_2026-09-06.md', 'sanctions_topic_docket_2026-09-05.md', 'shemini_day_run_docket_2026-09-06.md'], NAMING
assert 'Deut 12:3' in LED['deu_07_vaetchanan_ekev_2026-09-17.md'] and 'Deut 12:23' in LED['lev_21_priests_2026-09-05.md'] and 'Deut 12:5' in LED['num_06_priest_blessing_2026-09-09.md'] and 'Deuteronomy 12:9' in LED['num_33_journeys_exam_2026-09-12.md']
# THE KIN'S READS: the slaughter at the tent and the blood at Leviticus 17, the dues at Numbers 18, the shrines and the idols' silver at chapter 7, Molech at Leviticus 18 and 20, the dispossession at Numbers 33, the angel's clauses at Exodus 23; THE ALTAR IN EVERY PLACE (Exodus 20:21) through the Mekhilta alone (no ledger holds an Onkelos row of Exodus 20:21 or of Genesis 9:4 or of Exodus 34:13, 24); NEVER READ AHEAD — no ledger holds an Onkelos row of Deuteronomy 13-16
assert kinrows('lev_17_18_blood_arayot_2026-09-05.md', r'Lev 17:(?:[1-9]|1[0-6])\b') == 16 and kinrows('num_18_priest_levite_dues_2026-09-10.md', r'Num 18:(?:[89]|[12]\d|3[0-2])\b') == 25 and kinrows('deu_07_vaetchanan_ekev_2026-09-17.md', r'Deut 7:(?:5|25|26)\b') == 3 and kinrows('lev_20_sanctions_2026-09-05.md', r'Lev (?:18:21|20:[2-5])\b') == 4 and kinrows('lev_17_18_blood_arayot_2026-09-05.md', r'Lev (?:18:21|20:[2-5])\b') == 1 and kinrows('num_33_journeys_2026-09-12.md', r'Num 33:52\b') == 1 and kinrows('exo_23_escort_land_2026-09-01.md', r'Exod 23:(?:24|33)\b') == 1
assert [f for f in LED if kinrows(f, r'Exod 20:21\b')] == [] and [(f, len(re.findall(r'Mekhilta[^\n]{0,60}(?:20:2[01]|Bachodesh 11)', t))) for f, t in LED.items() if re.search(r'Mekhilta[^\n]{0,60}(?:20:2[01]|Bachodesh 11)', t)] == [('compiler_code_hunt_2026-09-02.md', 2)] and [f for f in LED if kinrows(f, r'Gen 9:4\b')] == [] and [f for f in LED if kinrows(f, r'Exod 34:(?:13|24)\b')] == [] and [f for f in LED if kinrows(f, r'Deut 1[3-6]:')] == []
ONK_LEN = {c: len(onk[c - 1]) for c in (3, 4, 5, 6, 7, 8, 9, 10, 11, 12)}
assert len(onk) == 34 and len(onk_he) == 34 and ONK_LEN == {3: 29, 4: 49, 5: 30, 6: 25, 7: 26, 8: 20, 9: 29, 10: 22, 11: 32, 12: 31} and sum(len(c) for c in onk_he) == 956
shelf_deut = sorted(d for d in os.listdir(f'{ROOT}/Data/sefaria_export') if re.search(r'Deuteronomy|Devarim', d))
outside = [d for d in shelf_deut if d not in ('Sifrei_Devarim', 'Onkelos_Deuteronomy')]
assert len(shelf_deut) == 28 and len(outside) == 26, len(outside)
# ---- THE DRAFT'S SPAN, COMPUTED ----
VC = dict(db.execute("SELECT chapter, COUNT(*) FROM verses WHERE book='Deut' GROUP BY chapter").fetchall())
assert VC[5] == 33 and VC[11] == 32 and VC[12] == 31 and sum(VC.values()) == 959 and len(VC) == 34
assert [(c, len(onk_he[c - 1]), VC[c]) for c in range(1, 35) if len(onk_he[c - 1]) != VC[c]] == [(5, 30, 33)]
# THE ALIGNMENT RECOMPUTED (ch12_dump0's A0): the export's thirty-one rows against the DB's thirty-one verses over token and negation counts — the identity, cost 26
by12 = {v: [plain(he) for he, in db.execute("SELECT w.he FROM words w JOIN verses v ON w.verse_id=v.id WHERE v.book='Deut' AND v.chapter=12 AND v.verse=? ORDER BY w.idx", (v,))] for v in range(1, 32)}
NEG = ('לא', 'ולא')
D_ = [(len(by12[v]), sum(1 for x in by12[v] if x in NEG)) for v in range(1, 32)]
E_ = [(len(plain(clean(r)).split()), sum(1 for x in plain(clean(r)).split() if x.strip('.:') in NEG)) for r in onk_he[11]]
def _cost(e, ds): return abs(e[0] - sum(d[0] for d in ds)) + 3 * abs(e[1] - sum(d[1] for d in ds))
INF = 10 ** 9; best = {(0, 0): (0, None)}
for i in range(1, 32):
    for j in range(i, 32):
        cands = [(best[(i - 1, k)][0] + _cost(E_[i - 1], D_[k:j]), k) for k in range(i - 1, j) if (i - 1, k) in best and j - k <= 4]
        best[(i, j)] = min(cands) if cands else (INF, None)
i, j, ALIGN = 31, 31, {}
while i > 0:
    k = best[(i, j)][1]; ALIGN[i] = list(range(k + 1, j + 1)); i, j = i - 1, k
assert ALIGN == EXP2DB and best[(31, 31)][0] == 26 and Counter(ds[0] - e for e, ds in EXP2DB.items()) == Counter({0: 31}) and len(onk_he[11]) == 31 == VC[12], (best[(31, 31)][0], ALIGN)
def unit_text(uid): return open(f'{ROOT}/logic/units/{uid}.yaml', encoding='utf-8').read()
def steps(uid): return sorted({(int(a), int(b)) for a, b in re.findall(r'STEP_Dt_(\d+)_(\d+)', unit_text(uid))})
FIRST = not os.path.exists(OUT)
for uid, (c, lo, hi) in SPANS.items():
    t = unit_text(uid)
    assert steps(uid) == [(c, v) for v in range(lo, hi + 1)] and re.search(rf'refs: "?{c}:{lo}-{hi}"?', t) and '\nbinary_trees:' in t, uid
    if FIRST: assert 'status: draft' in t and 'operators:' not in t and '- step: E' not in t, uid
    assert t.count(f'  - id: STEP_Dt_{c}_{lo}\n') == 1 and t.count(f'  - id: STEP_Dt_{c}_{hi}\n') == 1, uid
UT12 = unit_text('deu_12_place_name')
assert UT12.count('\n    comment:') + UT12.count('\n      comment:') == 35 and UT12.count('\n  - id: S') == 38   # typed from ch12_dump0's G print (the draft's comment lines and scenarios)
assert 'deu_11_bless_curse_set' in UT12 and 'lev_17_blood_center' in UT12 and 'status: frozen' in unit_text('deu_11_bless_curse_set') and 'status: frozen' in unit_text('lev_17_blood_center') and re.search(r'title_en: "[^"\n]*the place He chooses[^"\n]*"', UT12)   # THE DRAFT'S OWN DEPENDENCY on Leviticus 17 — the slaughter's kin named by the tree-derived draft before any reading
assert sorted(f for f in os.listdir(TRI) if f.startswith('deu_') and f != os.path.basename(OUT)) == ['deu_01_03_devarim_2026-09-15.md', 'deu_01_03_devarim_exam_2026-09-15.md', 'deu_04_vaetchanan_2026-09-16.md', 'deu_04_vaetchanan_exam_2026-09-16.md', 'deu_05_vaetchanan_2026-09-16.md', 'deu_05_vaetchanan_exam_2026-09-16.md', 'deu_06_vaetchanan_2026-09-17.md', 'deu_06_vaetchanan_exam_2026-09-17.md', 'deu_07_vaetchanan_ekev_2026-09-17.md', 'deu_07_vaetchanan_ekev_exam_2026-09-18.md', 'deu_08_ekev_2026-09-18.md', 'deu_08_ekev_exam_2026-09-19.md', 'deu_09_ekev_2026-09-19.md', 'deu_09_ekev_exam_2026-09-19.md', 'deu_10_ekev_2026-09-19.md', 'deu_10_ekev_exam_2026-09-20.md', 'deu_11_ekev_reeh_2026-09-20.md', 'deu_11_ekev_reeh_exam_2026-09-20.md']
ALLTXT = ''.join(open(f'{ROOT}/logic/units/{f}', encoding='utf-8').read() for f in os.listdir(f'{ROOT}/logic/units') if f.endswith('.yaml') and f[:-5] not in UIDS) + ''.join(open(f'{ROOT}/logic/oral_audit/manifests/{f}', encoding='utf-8').read() for f in os.listdir(f'{ROOT}/logic/oral_audit/manifests') if f.endswith('.json'))
assert all(f'"{p}-' not in ALLTXT and f'[claim {p}-' not in ALLTXT for p in PREFIX.values())
SPAN = [(12, v) for v in range(1, VC[12] + 1)]
NV = 31
assert len(SPAN) == NV
# ---- THE INK, computed from the Tanakh DB and the snapshot store ----
# THE STORE = THE DB at EVERY verse — no written/read pair in the chapter (wtype None at all 520 tokens); 2,051 letters; the four "?" glosses the store's "I" (אנכי at 11, 14, 28; אני at 30)
assert STORE_MISMATCH == [] and sum(len(SG[(12, v)]) for v in range(1, 32)) == 520 == sum(len(W12(v)) for v in range(1, 32)) and sum(len(x) for v in range(1, 32) for x in W12(v)) == 2051
assert [(v, x, m, wt) for v in range(1, 32) for (x, m), wt in zip(by[('Deut', 12, v)], byw[('Deut', 12, v)]) if wt] == [] and Counter(wt for v in range(1, 32) for wt in byw[('Deut', 12, v)]) == Counter({None: 520})
assert [(v, i, hp, g) for (c, v), L in sorted(SG.items()) for i, hp, g in L if g == '?'] == [(11, 15, 'אנכי', '?'), (14, 15, 'אנכי', '?'), (28, 7, 'אנכי', '?'), (30, 21, 'אני', '?')]
assert {v: len(W12(v)) for v in range(1, 32)} == {1: 21, 2: 24, 3: 18, 4: 5, 5: 18, 6: 14, 7: 15, 8: 12, 9: 14, 10: 17, 11: 29, 12: 18, 13: 9, 14: 17, 15: 20, 16: 8, 17: 18, 18: 27, 19: 10, 20: 22, 21: 25, 22: 13, 23: 14, 24: 6, 25: 12, 26: 13, 27: 17, 28: 23, 29: 17, 30: 22, 31: 22}
# THE ENGINE'S PARSER on every verse — MEASURED before the compile is asked: ONE NUMBER VERSE (12:14 "in one of your tribes" [1]) and ONE STARRED TOKEN (12:17 "tithe" — the ten-word's homograph, starred at every tithe seat of the book: 12:17, 14:23, 14:28, 26:12); the kin's numbers — the third year's [3] (14:28), Exodus 34:24's three times [3]
with contextlib.redirect_stdout(io.StringIO()):
    import cold_run_sequence as CS
PARSE = {v: (CS.ink_numbers(CS.verse_words('Deut', 12, v)), CS.ink_ordinals(CS.verse_words('Deut', 12, v)), [t for t in CS.verse_words('Deut', 12, v) if t[-1] in '#~^%@|*']) for v in range(1, 32)}
assert {v: p for v, p in PARSE.items() if any(p)} == {14: ([1], [], []), 17: ([], [], ['מעשר*'])}, {v: p for v, p in PARSE.items() if any(p)}
assert sorted({(c, v) for (b, c, v) in by if b == 'Deut' for t in CS.verse_words(b, c, v) if t.startswith('מעשר') and t.endswith('*')}) == [(12, 17), (14, 23), (14, 28), (26, 12)] and [(v, x) for v in range(1, 32) for x in W12(v) if x in ('אחד', 'באחד', 'אחת')] == [(14, 'באחד')]
KINNUM = {k: CS.ink_numbers(CS.verse_words(*k)) for k in [('Num', 18, 26), ('Deut', 14, 22), ('Deut', 14, 28), ('Lev', 27, 30), ('Lev', 27, 32), ('Deut', 15, 22), ('Lev', 17, 3), ('Lev', 17, 11), ('Gen', 9, 4), ('Exod', 20, 21), ('Deut', 7, 5), ('Num', 33, 52), ('Deut', 14, 23), ('Deut', 16, 2), ('Deut', 26, 12), ('Judg', 17, 6), ('Deut', 19, 8), ('Exod', 34, 24), ('Num', 18, 21), ('Deut', 12, 14)]}
assert KINNUM == {('Num', 18, 26): [], ('Deut', 14, 22): [], ('Deut', 14, 28): [3], ('Lev', 27, 30): [], ('Lev', 27, 32): [], ('Deut', 15, 22): [], ('Lev', 17, 3): [], ('Lev', 17, 11): [], ('Gen', 9, 4): [], ('Exod', 20, 21): [], ('Deut', 7, 5): [], ('Num', 33, 52): [], ('Deut', 14, 23): [], ('Deut', 16, 2): [], ('Deut', 26, 12): [], ('Judg', 17, 6): [], ('Deut', 19, 8): [], ('Exod', 34, 24): [3], ('Num', 18, 21): [], ('Deut', 12, 14): [1]}, KINNUM
# THE REGISTER, computed on the morphology: THE CHAPTER SWITCHES NUMBER AT ITS MIDDLE — the second person PLURAL ONLY in eight verses (2-4, 6, 8, 10-12), BOTH in five (1, 5, 7, 9, 16 — the singular inside the plural verse; 12:16's "you (pl.) shall not eat" the one plural in the singular half), SINGULAR ONLY in eighteen (13-15, 17-31), NEITHER in none; THE FIRST PERSON: Moses' "I" three (11, 14, 28) and "I have commanded you" (21), the eater's "let me eat" (20), the seeker's "and I will do so, I too" (30); "we" once (8); the imperatives FIVE (13, 19, 30 "take heed" — the niphal; 23 "be steadfast"; 28 "observe"); the infinitive absolute ONE (2 "destroy, you shall destroy"); THE CONSECUTIVE PERFECTS TWENTY-THREE in fifteen verses — the law's form; NO wayyiqtol — no narrative verb in the chapter; the prohibitions EIGHT (4, 8, 16, 17, 23, 24, 25, 31; 12:9's "not" a perfect); "saying" once (30 — the seeker's speech), no divine frame
NUM = {v: (sum(1 for _, m in wm('Deut', 12, v) if m and '2mp' in m), sum(1 for _, m in wm('Deut', 12, v) if m and '2ms' in m)) for v in range(1, 32)}
assert NUM == {1: (2, 2), 2: (2, 0), 3: (5, 0), 4: (2, 0), 5: (3, 1), 6: (9, 0), 7: (6, 2), 8: (1, 0), 9: (1, 1), 10: (7, 0), 11: (9, 0), 12: (9, 0), 13: (0, 5), 14: (0, 5), 15: (0, 6), 16: (1, 1), 17: (0, 11), 18: (0, 12), 19: (0, 5), 20: (0, 6), 21: (0, 10), 22: (0, 1), 23: (0, 2), 24: (0, 2), 25: (0, 5), 26: (0, 5), 27: (0, 6), 28: (0, 8), 29: (0, 5), 30: (0, 5), 31: (0, 2)}
assert [v for v, (p, s) in NUM.items() if s and not p] == [13, 14, 15, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31] and [v for v, (p, s) in NUM.items() if p and s] == [1, 5, 7, 9, 16] and [v for v, (p, s) in NUM.items() if not p and not s] == [] and [v for v, (p, s) in NUM.items() if p and not s] == [2, 3, 4, 6, 8, 10, 11, 12]
assert [(x, m) for x, m in wm('Deut', 12, 16) if m and '2mp' in m] == [('תאכלו', 'HVqi2mp')] and [(x, m) for x, m in wm('Deut', 12, 1) if m and '2ms' in m] == [('אבתיך', 'HNcmpc/Sp2ms'), ('לך', 'HR/Sp2ms')] and [(x, m) for x, m in wm('Deut', 12, 5) if m and '2ms' in m] == [('ובאת', 'HC/Vqq2ms')] and [(x, m) for x, m in wm('Deut', 12, 9) if m and '2ms' in m] == [('אלהיך', 'HNcmpc/Sp2ms')]
assert {v: [(x, m) for x, m in wm('Deut', 12, v) if m and '1cs' in m] for v in range(1, 32) if any(m and '1cs' in m for _, m in wm('Deut', 12, v))} == {11: [('אנכי', 'HPp1cs')], 14: [('אנכי', 'HPp1cs')], 20: [('אכלה', 'HVqh1cs')], 21: [('צויתך', 'HVpp1cs/Sp2ms')], 28: [('אנכי', 'HPp1cs')], 30: [('ואעשה', 'HC/Vqi1cs'), ('אני', 'HPp1cs')]} and {v: [(x, m) for x, m in wm('Deut', 12, v) if m and '1cp' in m] for v in range(1, 32) if any(m and '1cp' in m for _, m in wm('Deut', 12, v))} == {8: [('אנחנו', 'HPp1cp')]}
assert {v: [(x, m) for x, m in wm('Deut', 12, v) if m and re.match(r'^HV.?.?v', m)] for v in range(1, 32) if any(m and re.match(r'^HV.?.?v', m) for _, m in wm('Deut', 12, v))} == {13: [('השמר', 'HVNv2ms')], 19: [('השמר', 'HVNv2ms')], 23: [('חזק', 'HVqv2ms')], 28: [('שמר', 'HVqv2ms')], 30: [('השמר', 'HVNv2ms')]}
assert {v: [(x, m) for x, m in wm('Deut', 12, v) if m and re.match(r'^H(?:C/)?V.a$', m)] for v in range(1, 32) if any(m and re.match(r'^H(?:C/)?V.a$', m) for _, m in wm('Deut', 12, v))} == {2: [('אבד', 'HVpa')]}
WEQ = {v: [x for x, m in wm('Deut', 12, v) if m and re.search(r'^HC/V.q', m)] for v in range(1, 32) if any(m and re.search(r'^HC/V.q', m) for _, m in wm('Deut', 12, v))}
assert WEQ == {3: ['ונתצתם', 'ושברתם', 'ואבדתם'], 5: ['ובאת'], 6: ['והבאתם'], 7: ['ואכלתם', 'ושמחתם'], 10: ['ועברתם', 'וישבתם', 'והניח', 'וישבתם'], 11: ['והיה'], 12: ['ושמחתם'], 15: ['ואכלת'], 18: ['ושמחת'], 20: ['ואמרת'], 21: ['וזבחת', 'ואכלת'], 26: ['ובאת'], 27: ['ועשית'], 28: ['ושמעת'], 29: ['וירשת', 'וישבת']} and sum(len(x) for x in WEQ.values()) == 23 and len(WEQ) == 15
assert {v: [x for x, m in wm('Deut', 12, v) if m and re.search(r'^HC/V.w', m)] for v in range(1, 32) if any(m and re.search(r'^HC/V.w', m) for _, m in wm('Deut', 12, v))} == {}
PTC = {v: [(x, m) for x, m in wm('Deut', 12, v) if m and re.search(r'^H(?:C/|R/|Td/|C/R/)?V.r', m)] for v in range(1, 32) if any(m and re.search(r'^H(?:C/|R/|Td/|C/R/)?V.r', m) for _, m in wm('Deut', 12, v))}
assert sum(len(x) for x in PTC.values()) == 10 and len(PTC) == 8 and PTC[2] == [('ירשים', 'HVqrmpa'), ('הרמים', 'HTd/Vqrmpa')] and PTC[10] == [('מנחיל', 'HVhrmsa'), ('איביכם', 'HVqrmpc/Sp2mp')] and PTC[9] == [('נתן', 'HVqrmsa')] and PTC[29] == [('בא', 'HVqrmsa')]
I2 = {v: [(x, m) for x, m in wm('Deut', 12, v) if m and re.search(r'^H(?:Ti/)?V.i2', m)] for v in range(1, 32) if any(m and re.search(r'^H(?:Ti/)?V.i2', m) for _, m in wm('Deut', 12, v))}
assert sum(len(x) for x in I2.values()) == 33 and len(I2) == 24 and I2[3] == [('תשרפון', 'HVqi2mp/Sn'), ('תגדעון', 'HVpi2mp/Sn')] and I2[17] == [('תוכל', 'HVqi2ms'), ('תדר', 'HVqi2ms')] and I2[30] == [('תנקש', 'HVNi2ms'), ('תדרש', 'HVqi2ms')]
assert [x for v in range(1, 32) for x, m in wm('Deut', 12, v) if m and m.endswith('/Sn')] == ['תשמרון', 'תאבדון', 'תשרפון', 'תגדעון', 'תעשון', 'תעשון']   # THE PARAGOGIC NUN six times, all in the plural half (1-8)
PROH = {v: [(x, m) for i, (x, m) in enumerate(wm('Deut', 12, v)) if i and wm('Deut', 12, v)[i - 1][0] in NEG and m and re.search(r'^HV.i2', m)] for v in range(1, 32)}
assert {v: x for v, x in PROH.items() if x} == {4: [('תעשון', 'HVqi2mp/Sn')], 8: [('תעשון', 'HVqi2mp/Sn')], 16: [('תאכלו', 'HVqi2mp')], 17: [('תוכל', 'HVqi2ms')], 23: [('תאכל', 'HVqi2ms')], 24: [('תאכלנו', 'HVqi2ms/Sp3ms')], 25: [('תאכלנו', 'HVqi2ms/Sp3ms')], 31: [('תעשה', 'HVqi2ms')]} and {v: [x for x in W12(v) if x in NEG] for v in range(1, 32) if any(x in NEG for x in W12(v))} == {4: ['לא'], 8: ['לא'], 9: ['לא'], 16: ['לא'], 17: ['לא'], 23: ['ולא'], 24: ['לא'], 25: ['לא'], 31: ['לא']}
assert {f'12:{v}': [x for x in W12(v) if x in ('כי', 'אם', 'ואם', 'או', 'פן', 'ופן')] for v in range(1, 32) if any(x in ('כי', 'אם', 'ואם', 'או', 'פן', 'ופן') for x in W12(v))} == {'12:5': ['כי', 'אם'], '12:9': ['כי'], '12:12': ['כי'], '12:13': ['פן'], '12:14': ['כי', 'אם'], '12:18': ['כי', 'אם'], '12:19': ['פן'], '12:20': ['כי', 'כי'], '12:21': ['כי'], '12:23': ['כי'], '12:25': ['כי'], '12:28': ['כי'], '12:29': ['כי'], '12:30': ['פן', 'ופן'], '12:31': ['כי', 'כי']}
assert [v for v in range(1, 32) if 'לאמר' in W12(v)] == [30] and [v for v in range(1, 32) if any(W12(v)[i] in ('ויאמר', 'וידבר') and W12(v)[i + 1] == 'יהוה' for i in range(len(W12(v)) - 1))] == []
assert {v: [x for x in W12(v) if x in ('למען', 'ולמען')] for v in range(1, 32) if any(x in ('למען', 'ולמען') for x in W12(v))} == {25: ['למען'], 28: ['למען']} and len(U('למען', 'ולמען', books=('Deut',))) == 43
assert sum(1 for v in range(1, 32) for x in W12(v) if x == 'יהוה') == 23 and [v for v in range(1, 32) if any(W12(v)[i:i + 2] == ['יהוה', 'אלהיך'] for i in range(len(W12(v)) - 1))] == [7, 9, 15, 18, 20, 21, 27, 28, 29] and [v for v in range(1, 32) if any(W12(v)[i:i + 2] == ['יהוה', 'אלהיכם'] for i in range(len(W12(v)) - 1))] == [5, 7, 10, 11, 12] and [v for v in range(1, 32) if 'ליהוה' in W12(v)] == [4, 11, 31]
assert [v for v in range(1, 32) for x in W12(v) if x in ('ישראל', 'מצרים', 'מצרימה', 'משה')] == [] and [v for v in range(1, 32) for x in W12(v) if x == 'היום'] == [8] and [v for v in range(1, 32) for x in W12(v) if x == 'הירדן'] == [10]
assert Counter(int(s.split()[1].split(':')[0]) for s in U('משה', 'למשה', 'ומשה', books=('Deut',))) == Counter({31: 10, 34: 6, 4: 4, 1: 3, 27: 3, 32: 3, 33: 2, 15: 1, 28: 1, 29: 1, 5: 1})   # MOSES UNNAMED FROM CHAPTER 6 TO 14 (chapter 10's find, held)
assert {v: [x for x in W12(v) if x in ('שם', 'שמה', 'ושם')] for v in range(1, 32) if any(x in ('שם', 'שמה', 'ושם') for x in W12(v))} == {2: ['שם'], 5: ['שם', 'שמה'], 6: ['שמה'], 7: ['שם'], 11: ['שם', 'שמה'], 14: ['שם', 'ושם'], 21: ['שם'], 29: ['שמה']}   # "there" eleven times — the chapter's word for the place
assert {v: [x for x in W12(v) if x in ('אלהיהם', 'לאלהיהם')] for v in range(1, 32) if any(x in ('אלהיהם', 'לאלהיהם') for x in W12(v))} == {2: ['אלהיהם'], 3: ['אלהיהם'], 30: ['לאלהיהם', 'אלהיהם'], 31: ['לאלהיהם', 'לאלהיהם']}
OWN = {lab: [s for s, _, _ in LEMT(lem, books=('Deut',)) if s.startswith('Deut 12:')] for lab, lem in (('place', '4725'), ('gate', '8179'), ('eat', '398'), ('flesh', '1320'), ('blood', '1818'), ('soul', '5315'), ('burnt', '5930 a'), ('sacrifice-n', '2077'), ('sacrifice-v', '2076'), ('tithe', '4643'), ('vow-n', '5088'), ('vow-v', '5087'), ('freewill', '5071'), ('heave', '8641'), ('firstling', '1062'), ('rejoice', '8055'), ('nations', '1471 a'), ('choose', '977'), ('seek', '1875'), ('levite', '3881'))}
assert {k: len(v) for k, v in OWN.items()} == {'place': 9, 'gate': 5, 'eat': 18, 'flesh': 7, 'blood': 5, 'soul': 6, 'burnt': 5, 'sacrifice-n': 3, 'sacrifice-v': 2, 'tithe': 3, 'vow-n': 4, 'vow-v': 2, 'freewill': 2, 'heave': 3, 'firstling': 2, 'rejoice': 3, 'nations': 3, 'choose': 6, 'seek': 2, 'levite': 3}, {k: len(v) for k, v in OWN.items()}
assert OWN['eat'][:3] == ['Deut 12:7', 'Deut 12:15', 'Deut 12:15'] and OWN['blood'] == ['Deut 12:16', 'Deut 12:23', 'Deut 12:23', 'Deut 12:27', 'Deut 12:27'] and OWN['choose'] == ['Deut 12:5', 'Deut 12:11', 'Deut 12:14', 'Deut 12:18', 'Deut 12:21', 'Deut 12:26'] and OWN['seek'] == ['Deut 12:5', 'Deut 12:30'] and len(LEMT('977', books=('Deut',))) == 31 and len(LEMT('3881', books=('Deut',))) == 19 and len(LEMT('7535', books=('Deut',))) == 20 and len(LEMT('8441', books=('Deut',))) == 17
# ---- THE PHRASES, censused over the whole DB (the measure's B print) ----
DT = ('Deut',)
assert P('אלה', 'החקים', 'והמשפטים') == ['Deut 12:1', 'Lev 26:46'] and P('החקים', 'והמשפטים') == ['Deut 12:1', 'Deut 6:1', 'Lev 26:46']   # THE HEADER'S TWIN IS THE FOLD'S FOOTER — "these are the statutes and the judgments" stands at 12:1 and at Leviticus 26:46 alone
assert U('תשמרון') == ['2Kgs 17:37', 'Deut 11:22', 'Deut 12:1', 'Deut 6:17', 'Deut 8:1'] and P('יהוה', 'אלהי', 'אבתיך') == ['Deut 12:1', 'Deut 1:21', 'Deut 27:3', 'Deut 6:3'] and P('כל', 'הימים', 'אשר', 'אתם', 'חיים', 'על', 'האדמה') == ['Deut 12:1', 'Deut 31:13'] and len(P('על', 'האדמה', books=DT)) == 13
assert P('אבד', 'תאבדון') == ['Deut 12:2', 'Deut 30:18', 'Deut 4:26', 'Deut 8:19'] and [(s, x, m) for s, x, m in LEMT('6', books=DT) if s.startswith('Deut 12:')] == [('Deut 12:2', 'אבד', 'HVpa'), ('Deut 12:2', 'תאבדון', 'HVpi2mp/Sn'), ('Deut 12:3', 'ואבדתם', 'HC/Vpq2mp')]   # THE VERB OF ISRAEL'S PERISHING TURNED ON THE SHRINES — the doubled "perish, you shall perish" of 4:26, 8:19, 30:18 said here as "destroy, you shall destroy" (the piel)
assert P('כל', 'המקמות') == ['Deut 12:2', 'Jer 45:5'] and P('אשר', 'עבדו', 'שם', 'הגוים') == ['Deut 12:2'] and P('על', 'ההרים', 'הרמים') == ['Deut 12:2'] and P('תחת', 'כל', 'עץ', 'רענן') == ['Isa 57:5', 'Jer 3:13', 'Jer 3:6'] and len(P('כל', 'עץ', 'רענן')) == 10 and len(U('רענן')) == 17 and P('כל', 'עץ', 'רענן')[:5] == ['1Kgs 14:23', '2Chr 28:4', '2Kgs 16:4', '2Kgs 17:10', 'Deut 12:2']   # THE KINGS' FORMULA — "under every leafy tree" the prophets' and the Kings' phrase for the high places, its Torah seat this one
assert [(s, x) for s, x, _ in LEMT('5422', books=T)] == [('Deut 7:5', 'תתצו'), ('Deut 12:3', 'ונתצתם'), ('Exod 34:13', 'תתצון'), ('Lev 11:35', 'יתץ'), ('Lev 14:45', 'ונתץ')] and U('תשרפון') == ['Deut 12:3', 'Deut 7:25', 'Deut 7:5'] and len(LEMT('1438')) == 22 and [(s, x) for s, x, _ in LEMT('1438', books=T)] == [('Deut 7:5', 'תגדעון'), ('Deut 12:3', 'תגדעון')] and P('ואבדתם', 'את', 'שמם') == ['Deut 12:3'] and P('מן', 'המקום', 'ההוא') == ['Deut 12:3', 'Deut 17:10'] and len(P('המקום', 'ההוא')) == 13
assert SH(D12(3), ('Exod', 34, 13)) == 3 and SH(D12(3), ('Deut', 7, 5)) == 2 and SH(D12(2), ('Deut', 7, 5)) == 0 and SH(D12(2), ('Num', 33, 52)) == 4 and SH(D12(2), ('2Kgs', 17, 10)) == 5   # THE DEMOLITION SAID IN NEW WORDS — 12:3 shares two tokens in order with 7:5 (the burning), three with Exodus 34:13; 12:2 none with 7:5
assert P('לא', 'תעשון', 'כן', 'ליהוה', 'אלהיכם') == ['Deut 12:4'] and P('לא', 'תעשה', 'כן') == ['Deut 12:31'] and SH(D12(4), ('Deut', 12, 31)) == 3   # THE PAIR'S TWO SEATS — plural at the shrines (12:4), singular at the abomination (12:31)
assert P('המקום', 'אשר', 'יבחר', 'יהוה') == ['Deut 12:11', 'Deut 12:21', 'Deut 12:26', 'Deut 12:5', 'Deut 14:24', 'Deut 14:25', 'Deut 16:6', 'Deut 17:8', 'Deut 18:6', 'Deut 26:2'] and P('במקום', 'אשר', 'יבחר', 'יהוה') == ['Deut 12:14', 'Deut 12:18', 'Deut 15:20', 'Deut 16:11', 'Deut 16:15', 'Deut 16:2', 'Deut 16:7'] and len(U('יבחר', books=DT)) == 23   # THE PLACE WHICH THE LORD WILL CHOOSE — six of the chapter's verses, twenty-three seats of "will choose" in the book, none before chapter 12
assert P('מכל', 'שבטיכם') == ['Deut 12:5'] and P('באחד', 'שבטיך') == ['Deut 12:14'] and P('לשום', 'את', 'שמו', 'שם') == ['1Kgs 14:21', '2Chr 12:13', 'Deut 12:5'] and P('לשום', 'שמו', 'שם') == ['Deut 12:21', 'Deut 14:24'] and P('לשכן', 'שמו', 'שם') == ['Deut 12:11', 'Deut 14:23', 'Deut 16:11', 'Deut 16:2', 'Deut 16:6', 'Deut 26:2'] and U('לשכנו') == ['Deut 12:5']   # "to put His name there" the chapter's form (12:5, 21), "to make His name dwell" its other (12:11) — Kings quotes the first; "His dwelling" ONE seat in the Bible
assert U('תדרשו') == ['Amos 5:5', 'Deut 12:5', 'Ezra 9:12'] and [(s, x, m) for s, x, m in LEMT('1875', books=DT) if s.startswith('Deut 12:')] == [('Deut 12:5', 'תדרשו', 'HVqi2mp'), ('Deut 12:30', 'תדרש', 'HVqi2ms')] and P('ובאת', 'שמה') == ['2Kgs 9:2', 'Deut 12:5']   # ONE VERB FOR TWO SEEKINGS — "seek" His dwelling (12:5) and "inquire" after their gods (12:30)
assert P('עלתיכם', 'וזבחיכם') == ['Deut 12:6'] and U('מעשרתיכם') == ['Amos 4:4', 'Deut 12:11', 'Deut 12:6', 'Num 18:28'] and P('תרומת', 'ידכם') == ['Deut 12:6'] and P('ותרומת', 'ידך') == ['Deut 12:17'] and P('ונדריכם', 'ונדבתיכם') == ['Deut 12:6'] and P('ובכרת', 'בקרכם', 'וצאנכם') == ['Deut 12:6'] and P('ובכרת', 'בקרך', 'וצאנך') == ['Deut 12:17', 'Deut 14:23'] and P('מבחר', 'נדריכם') == ['Deut 12:11'] and P('מעשר', 'דגנך', 'ותירשך', 'ויצהרך') == ['Deut 12:17'] and P('דגנך', 'ותירשך', 'ויצהרך') == ['Deut 11:14', 'Deut 12:17', 'Deut 7:13']
assert P('ואכלתם', 'שם', 'לפני', 'יהוה', 'אלהיכם') == ['Deut 12:7'] and U('ושמחתם', 'ושמחת', books=DT) == ['Deut 12:12', 'Deut 12:18', 'Deut 12:7', 'Deut 14:26', 'Deut 16:11', 'Deut 16:14', 'Deut 26:11', 'Deut 27:7'] and len(LEMT('8055', books=DT)) == 10 and P('משלח', 'ידכם') == ['Deut 12:7'] and P('משלח', 'ידך') == ['Deut 12:18', 'Deut 15:10', 'Deut 23:21', 'Deut 28:20', 'Deut 28:8'] and P('אתם', 'ובתיכם') == ['Deut 12:7'] and P('אשר', 'ברכך', 'יהוה', 'אלהיך') == ['Deut 12:7', 'Deut 15:14']
assert P('איש', 'כל', 'הישר', 'בעיניו') == ['Deut 12:8'] and P('הישר', 'בעיניו', 'יעשה') == ['Judg 17:6', 'Judg 21:25'] and P('פה', 'היום') == ['Deut 12:8', 'Deut 5:3'] and U('אנחנו', books=DT) == ['Deut 12:8', 'Deut 1:28', 'Deut 1:41', 'Deut 5:25', 'Deut 5:3'] and SH(D12(8), ('Judg', 17, 6)) == 3   # "EVERY MAN WHAT IS RIGHT IN HIS EYES" — the chapter's phrase is Judges' refrain (17:6, 21:25 "in those days there was no king"); "we" the book's five
assert P('המנוחה', 'ואל', 'הנחלה') == ['Deut 12:9'] and [(s, x) for s, x, _ in LEMT('4496', books=T)] == [('Deut 12:9', 'המנוחה'), ('Gen 49:15', 'מנחה'), ('Num 10:33', 'מנוחה')] and len(LEMT('4496')) == 22 and P('עד', 'עתה', books=DT) == ['Deut 12:9']   # "the rest" — Numbers 10:33's ark seeking a resting place (2:2's row), Issachar's (Genesis 49:15)
assert P('והניח', 'לכם', 'מכל', 'איביכם', 'מסביב') == ['Deut 12:10'] and P('מכל', 'איביך', 'מסביב') == ['Deut 25:19'] and P('וישבתם', 'בטח') == ['Deut 12:10'] and U('בטח', 'לבטח', books=T) == ['Deut 12:10', 'Deut 28:52', 'Deut 33:12', 'Deut 33:28', 'Gen 34:25', 'Lev 25:18', 'Lev 25:19', 'Lev 26:5'] and SH(D12(10), ('Josh', 23, 1)) == 4 and SH(D12(10), ('2Sam', 7, 1)) == 1
assert P('והלוי', 'אשר', 'בשעריכם') == ['Deut 12:12'] and P('והלוי', 'אשר', 'בשעריך') == ['Deut 12:18', 'Deut 14:27', 'Deut 16:11'] and P('אין', 'לו', 'חלק', 'ונחלה') == ['Deut 12:12', 'Deut 14:27', 'Deut 14:29'] and P('חלק', 'ונחלה') == ['Deut 10:9', 'Deut 12:12', 'Deut 14:27', 'Deut 14:29', 'Deut 18:1', 'Gen 31:14'] and P('ובניכם', 'ובנתיכם', 'ועבדיכם', 'ואמהתיכם') == ['Deut 12:12'] and P('אתה', 'ובנך', 'ובתך', 'ועבדך', 'ואמתך') == ['Deut 12:18', 'Deut 16:11', 'Deut 16:14', 'Deut 5:14']   # THE SABBATH'S LIST at the eating (12:18) — 5:14's household said again at the place, at the feasts
assert P('השמר', 'לך', 'פן') == ['Deut 12:13', 'Deut 12:19', 'Deut 12:30', 'Deut 15:9', 'Deut 6:12', 'Deut 8:11', 'Exod 34:12', 'Gen 24:6', 'Gen 31:24'] and P('השמרו', 'לכם', 'פן') == ['Deut 11:16', 'Deut 4:23'] and len(U('השמר', books=DT)) == 8 and P('בכל', 'מקום', 'אשר', 'תראה') == ['Deut 12:13'] and P('שם', 'תעלה', 'עלתיך') == ['Deut 12:14'] and P('כל', 'אשר', 'אנכי', 'מצוך', books=DT) == ['Deut 12:14']   # "take heed to yourself lest" THREE TIMES in one chapter (13, 19, 30) — nine in the Bible
assert [s for s, _, _ in LEMT('7535', books=DT) if s.startswith('Deut 12:')] == ['Deut 12:15', 'Deut 12:16', 'Deut 12:23', 'Deut 12:26'] and [s for s, _, _ in LEMT('389', books=DT) if s.startswith('Deut 12:')] == ['Deut 12:22'] and P('בכל', 'אות', 'נפשך') == ['Deut 12:15', 'Deut 12:20', 'Deut 12:21'] and [(s, x) for s, x, _ in LEMT('185')] == [('1Sam 23:20', 'אות'), ('Deut 12:15', 'אות'), ('Deut 12:20', 'אות'), ('Deut 12:21', 'אות'), ('Deut 18:6', 'אות'), ('Hos 10:10', 'באותי'), ('Jer 2:24', 'באות')] and [(s, x) for s, x, _ in LEMT('183', books=T)] == [('Deut 5:21', 'תתאוה'), ('Deut 12:20', 'תאוה'), ('Deut 14:26', 'תאוה'), ('Num 11:4', 'התאוו'), ('Num 11:34', 'המתאוים')]   # "only" FOUR times (15, 16, 23, 26) and "but" once (22) — the restrictive clauses the shelf reads; "the desire of your soul" the chapter's three of the noun's four Torah seats; the craving's verb the quails' (Numbers 11:4, 34) and the tenth word's (5:21)
assert P('תזבח', 'ואכלת', 'בשר') == ['Deut 12:15'] and P('כברכת', 'יהוה', 'אלהיך', 'אשר', 'נתן', 'לך') == ['Deut 12:15', 'Deut 16:17'] and len(P('בכל', 'שעריך', books=DT)) == 4 and P('הטמא', 'והטהור') == ['Deut 12:15', 'Deut 12:22', 'Deut 15:22'] and P('כצבי', 'וכאיל') == ['Deut 12:15', 'Deut 15:22'] and P('הצבי', 'ואת', 'האיל') == ['Deut 12:22'] and len(LEMT('6643 b')) == 14 and [(s, x) for s, x, _ in LEMT('6643 b') if s.startswith('Deut')] == [('Deut 12:15', 'כצבי'), ('Deut 12:22', 'הצבי'), ('Deut 14:5', 'וצבי'), ('Deut 15:22', 'כצבי')] and ('2Sam 1:19', 'הצבי') in [(s, x) for s, x, _ in LEMT('6643 a')]   # THE GAZELLE'S HOMOGRAPH — the same consonants are "the beauty" (2 Samuel 1:19, Isaiah 13:19, Daniel 8:9): the DB's lemma 6643 b the animal, 6643 a the glory; the store glossed the animal "splendor"
assert SH(D12(15), ('Lev', 17, 3)) == 1 and SH(D12(15), ('Lev', 17, 4)) == 1 and SH(D12(15), ('Lev', 17, 5)) == 1 and SH(D12(15), ('Deut', 15, 22)) == 4 and SH(D12(21), ('Lev', 17, 3)) == 2   # THE SLAUGHTER LAW SAID IN NEW WORDS — Leviticus 17:3-5 (every slaughter at the tent's door) shares one token in order with 12:15; the release from it named nowhere by Leviticus's words
assert P('רק', 'הדם', 'לא', 'תאכלו') == ['Deut 12:16'] and P('דם', 'לא', 'תאכלו') == ['Lev 3:17', 'Lev 7:26'] and P('כל', 'דם', 'לא', 'תאכלו') == [] and P('על', 'הארץ', 'תשפכנו', 'כמים') == ['Deut 12:16', 'Deut 12:24', 'Deut 15:23'] and U('כמים', books=T) == ['Deut 12:16', 'Deut 12:24', 'Deut 15:23', 'Gen 49:4'] and SH(D12(16), ('Deut', 15, 23)) == 6 and SH(D12(16), ('Lev', 17, 13)) == 0   # "on the earth you shall pour it like water" the book's three (12:16, 12:24, 15:23) — Leviticus 17:13 covers the blood with dust, Deuteronomy pours it like water: no token shared
assert P('לא', 'תוכל', 'לאכל', 'בשעריך') == ['Deut 12:17'] and P('לא', 'תוכל', books=DT) == ['Deut 12:17', 'Deut 14:24', 'Deut 16:5', 'Deut 17:15', 'Deut 22:3', 'Deut 28:27', 'Deut 28:35', 'Deut 7:22'] and P('נדריך', 'אשר', 'תדר') == ['Deut 12:17'] and SH(D12(17), ('Deut', 14, 23)) == 6
assert P('כי', 'אם', 'לפני', 'יהוה', 'אלהיך', 'תאכלנו') == ['Deut 12:18'] and U('תאכלנו', books=DT) == ['Deut 12:18', 'Deut 12:22', 'Deut 12:24', 'Deut 12:25', 'Deut 15:20', 'Deut 15:22', 'Deut 28:39', 'Deut 5:25'] and P('במקום', 'אשר', 'יבחר', 'יהוה', 'אלהיך', 'בו') == ['Deut 12:18', 'Deut 16:7'] and SH(D12(18), ('Deut', 16, 11)) == 13 and SH(D12(18), ('Deut', 5, 14)) == 8   # 12:18 and the Feast of Weeks' verse (16:11) share thirteen tokens in order — the chapter's closest kin in the book
assert P('פן', 'תעזב', 'את', 'הלוי') == ['Deut 12:19'] and P('כל', 'ימיך', 'על', 'אדמתך') == ['Deut 12:19']   # THE LEVITE'S VERSE ALONE (KINC[19] asserted empty below, after the computation) — no verse of the Bible shares two non-stop tokens with 12:19
assert P('כי', 'ירחיב', 'יהוה', 'אלהיך', 'את', 'גבולך') == ['Deut 12:20'] and [(s, x, m) for s, x, m in LEMT('7337', books=T) if m and 'Vh' in m] == [('Deut 12:20', 'ירחיב', 'HVhi3ms'), ('Deut 19:8', 'ירחיב', 'HVhi3ms'), ('Deut 33:20', 'מרחיב', 'HVhrmsc'), ('Exod 34:24', 'והרחבתי', 'HC/Vhq1cs'), ('Gen 26:22', 'הרחיב', 'HVhp3ms')] and 'גבלך' in words('Deut', 19, 8) and 'גבולך' in W12(20)   # the border's two spellings — plene here, defective at 19:8
assert P('כאשר', 'דבר', 'לך', books=DT) == ['Deut 12:20', 'Deut 15:6', 'Deut 26:18', 'Deut 29:12'] and len(P('כאשר', 'דבר', books=DT)) == 16 and P('אכלה', 'בשר') == ['Deut 12:20'] and P('כי', 'תאוה', 'נפשך', 'לאכל', 'בשר') == ['Deut 12:20'] and sum(1 for v in range(1, 32) for x in W12(v) if x in ('בשר', 'הבשר', 'והבשר')) == 7   # "AS HE HAS SPOKEN TO YOU" (12:20) — the AS_WHEN form, four seats in the book (11:25's is "as He spoke to YOU (pl.)"); "flesh" seven times, four of them in 12:20
assert P('כי', 'ירחק', 'ממך', 'המקום') == ['Deut 12:21', 'Deut 14:24'] and P('כאשר', 'צויתך') == ['Deut 12:21', 'Exod 23:15'] and len(P('כאשר', 'צויתי')) == 6 and len(P('כאשר', 'צוה', books=DT)) == 3 and P('ואכלת', 'בשעריך') == ['Deut 12:21'] and SH(D12(21), ('Deut', 14, 24)) == 12   # THE RECEIPT WITHOUT THE NAME — "as I have commanded you" (12:21) has ONE kin in the Bible, Exodus 23:15's unleavened bread; the finder's forms carry the Name and list no seat here (measured below)
assert P('כאשר', 'יאכל', 'את', 'הצבי', 'ואת', 'האיל') == ['Deut 12:22'] and U('יחדו', books=DT) == ['Deut 12:22', 'Deut 15:22', 'Deut 22:10', 'Deut 22:11', 'Deut 25:11', 'Deut 25:5', 'Deut 33:17']
assert P('רק', 'חזק', 'לבלתי', 'אכל', 'הדם') == ['Deut 12:23'] and [(s, x, m) for s, x, m in LEMT('2388', books=DT) if m and m.endswith('v2ms')] == [('Deut 1:38', 'חזק', 'HVpv2ms'), ('Deut 12:23', 'חזק', 'HVqv2ms'), ('Deut 31:7', 'חזק', 'HVqv2ms'), ('Deut 31:23', 'חזק', 'HVqv2ms')] and P('כי', 'הדם', 'הוא', 'הנפש') == ['Deut 12:23'] and P('ולא', 'תאכל', 'הנפש', 'עם', 'הבשר') == ['Deut 12:23'] and SH(D12(23), ('Lev', 17, 11)) == 3 and SH(D12(23), ('Gen', 9, 4)) == 0   # "BE STRONG" said to a man about the blood — the word said to Joshua (1:38, 31:7, 23); "the blood is the life" Leviticus 17:11's clause turned (there "the life of the flesh is in the blood"), Genesis 9:4's shares nothing
assert P('לא', 'תאכלנו') == ['Deut 12:24', 'Deut 12:25'] and P('למען', 'ייטב', 'לך', 'ולבניך', 'אחריך') == ['Deut 12:25', 'Deut 12:28'] and P('כי', 'תעשה', 'הישר', 'בעיני', 'יהוה') == ['Deut 12:25', 'Deut 21:9'] and P('הטוב', 'והישר') == ['2Chr 14:1', '2Chr 31:20', '2Kgs 10:3', 'Deut 12:28'] and len(P('הישר', 'בעיני', 'יהוה')) == 21 and SH(D12(25), ('Deut', 12, 28)) == 9 and SH(D12(28), ('Deut', 4, 40)) == 10   # "that it may go well with you and your children after you" — 12:25 and 12:28 alone (4:40's "after you" the kin); "the good and the right" 6:18's pair, Kings' measure of a king
assert P('רק', 'קדשיך', 'אשר', 'יהיו', 'לך', 'ונדריך') == ['Deut 12:26'] and U('קדשיך') == ['Deut 12:26'] and P('תשא', 'ובאת', 'אל', 'המקום') == ['Deut 12:26'] and P('ועשית', 'עלתיך', 'הבשר', 'והדם') == ['Deut 12:27'] and P('ודם', 'זבחיך', 'ישפך', 'על', 'מזבח') == ['Deut 12:27'] and U('ישפך', books=T) == ['Deut 12:27', 'Deut 19:10', 'Gen 9:6', 'Lev 4:18', 'Lev 4:25', 'Lev 4:30', 'Lev 4:34', 'Lev 4:7'] and P('מזבח', 'יהוה', 'אלהיך') == ['Deut 12:27', 'Deut 16:21', 'Deut 26:4', 'Deut 27:6'] and P('והבשר', 'תאכל') == ['Deut 12:27'] and SH(D12(27), ('Lev', 4, 7)) == 5 and SH(D12(27), ('Lev', 17, 6)) == 3   # "shall be poured" — the sin offering's verb (Leviticus 4:7, 18, 25, 30, 34: the rest of the blood at the altar's base) said of the sacrifices' blood
assert P('שמר', 'ושמעת', 'את', 'כל', 'הדברים', 'האלה') == ['Deut 12:28'] and len(P('כל', 'הדברים', 'האלה', books=DT)) == 4 and P('עד', 'עולם', books=DT) == ['Deut 12:28', 'Deut 23:4', 'Deut 28:46', 'Deut 29:28'] and words('Deut', 13, 1) == ['את', 'כל', 'הדבר', 'אשר', 'אנכי', 'מצוה', 'אתכם', 'אתו', 'תשמרו', 'לעשות', 'לא', 'תסף', 'עליו', 'ולא', 'תגרע', 'ממנו']   # THE DB'S 13:1 IS THE ENGLISH'S 12:32 — "you shall not add to it nor take from it" opens the next chapter in the Hebrew numbering: chapter 13's reading
assert P('כי', 'יכרית', 'יהוה', 'אלהיך', 'את', 'הגוים') == ['Deut 12:29', 'Deut 19:1'] and P('אשר', 'אתה', 'בא', 'שמה', 'לרשת', 'אותם') == ['Deut 12:29'] and P('וירשת', 'אתם', 'וישבת', 'בארצם') == ['Deut 12:29'] and SH(D12(29), ('Deut', 19, 1)) == 8 and SH(D12(29), ('Deut', 7, 1)) == 8 and words('Deut', 19, 1)[-3:] == ['וישבת', 'בעריהם', 'ובבתיהם']
assert P('פן', 'תנקש', 'אחריהם') == ['Deut 12:30'] and [(s, x, m) for s, x, m in LEMT('5367')] == [('1Sam 28:9', 'מתנקש', 'HVtrmsa'), ('Deut 12:30', 'תנקש', 'HVNi2ms'), ('Ps 9:17', 'נוקש', 'HVqrmsa'), ('Ps 38:13', 'וינקשו', 'HC/Vpw3mp'), ('Ps 109:11', 'ינקש', 'HVpi3ms')] and [(s, x, m) for s, x, m in LEMT('3369', books=T)] == [('Deut 7:25', 'תוקש', 'HVNi2ms')] and P('אחרי', 'השמדם', 'מפניך') == ['Deut 12:30'] and P('ופן', 'תדרש', 'לאלהיהם') == ['Deut 12:30'] and U('איכה', books=T) == ['Deut 12:30', 'Deut 18:21', 'Deut 1:12', 'Deut 32:30', 'Deut 7:17', 'Gen 3:9'] and P('ואעשה', 'כן', 'גם', 'אני') == ['Deut 12:30']   # "lest you be ENSNARED" — the snare's root here (נקש) is not 7:25's (יקש): the Torah's one seat of each niphal
assert P('כל', 'תועבת', 'יהוה', 'אשר', 'שנא') == ['Deut 12:31'] and len(P('תועבת', 'יהוה')) == 19 and [s for s in P('תועבת', 'יהוה') if s.startswith('Deut')] == ['Deut 12:31', 'Deut 17:1', 'Deut 18:12', 'Deut 22:5', 'Deut 23:19', 'Deut 25:16', 'Deut 27:15', 'Deut 7:25'] and P('אשר', 'שנא') == ['Deut 12:31', 'Deut 16:22'] and P('כי', 'גם', 'את', 'בניהם', 'ואת', 'בנתיהם', 'ישרפו', 'באש', 'לאלהיהם') == ['Deut 12:31'] and P('בניהם', 'ואת', 'בנתיהם') == ['Deut 12:31', 'Jer 7:31'] and P('לשרף', 'את', 'בניהם') == ['Jer 19:5', 'Jer 7:31'] and P('מעביר', 'בנו', 'ובתו', 'באש') == ['Deut 18:10'] and SH(D12(31), ('Jer', 7, 31)) == 6 and SH(D12(31), ('2Kgs', 17, 31)) == 4 and SH(D12(31), ('Lev', 18, 21)) == 3
assert 'Lev 18:21' in U('למלך') and 'Lev 20:2' in U('למלך') and 'Lev 20:3' in U('למלך') and len(U('למלך')) > 150   # THE KING-WORD'S HOMOGRAPH — Molech's consonants are "to the king" (the census's slip at 7:8 and 11:3); 12:31 names no Molech: "to their gods"
# ---- THE KIN FOUND BY COMPUTATION (the measure's A print, recomputed): the closest verses of the Bible by shared distinct tokens ----
STOP = set('את ואת אשר כל וכל על ועל אל ואל לא ולא כי אם יהוה אלהיך אלהיכם לך לכם בו שם שמה גם מן ממך עד הוא היא אתם אתה אנכי אני לו לה בכל כאשר כן הימים היום אלה האלה בארץ הארץ אשר ואם או פן ופן'.split())
ORD = {k: i for i, k in enumerate(by)}
TOK = {k: set(words(*k)) - STOP for k in by}
KINC = {}
for v in range(1, 32):
    me = D12(v); t = TOK[me]
    sc = sorted(((len(t & TOK[k]), k) for k in by if k != me and len(t & TOK[k]) >= 2), key=lambda x: (-x[0], ORD[x[1]]))[:8]
    KINC[v] = [(f'{k[0]} {k[1]}:{k[2]}', n, SH(me, k) if i < 3 else None) for i, (n, k) in enumerate(sc)]
assert KINC[18][0] == ('Deut 16:11', 10, 13) and KINC[17][0] == ('Deut 14:23', 6, 6) and KINC[21][0] == ('Deut 14:24', 5, 12) and KINC[28][:2] == [('Deut 12:25', 6, 9), ('Deut 4:40', 4, 10)] and KINC[2][:3] == [('2Chr 28:4', 4, 6), ('2Kgs 16:4', 4, 6), ('Ezek 6:13', 4, 6)] and KINC[8][3:5] == [('Judg 17:6', 3, None), ('Judg 21:25', 3, None)] and KINC[31][:2] == [('2Kgs 17:31', 3, 4), ('Deut 20:18', 3, 4)] and KINC[12][0] == ('Deut 14:27', 4, 7) and KINC[29][:3] == [('Deut 9:5', 4, 5), ('Deut 9:4', 3, 5), ('Deut 19:1', 3, 8)] and KINC[19] == []
# ---- ONKELOS — the renderings' seats over the book (the E print) ----
assert aramaic(12, 5) == ['אלהן', 'לאתרא', 'די', 'יתרעי', 'יי', 'אלהכון', 'מכל', 'שבטיכון', 'לאשראה', 'שכנתיה', 'תמן', 'לבית', 'שכנתיה', 'תתבעון', 'ותיתון', 'לתמן'] and len(onk_seats('שכנת')) == 23 and [(c, v) for c, v in onk_seats('שכנת') if c == 12] == [(12, 5), (12, 11), (12, 21)] and onk_seats('בית שכנת') == [(12, 5), (32, 40)]   # THE SHEKHINAH FOR THE NAME — "to put His name there, His dwelling" made "to make His Shekhinah dwell there, the house of His Shekhinah" (12:5 the Aramaic's one "house of His Shekhinah" in the book beside 32:40)
assert len(onk_tok('יתרעי')) == 26 and [(c, v) for c, v in onk_tok('יתרעי') if c == 12] == [(12, 5), (12, 11), (12, 14), (12, 18), (12, 21), (12, 26)] and onk_seats('רעות נפש') == [(12, 15), (12, 20), (12, 21), (18, 6)]
assert len(onk_seats('טעות')) == 32 and [(c, v) for c, v in onk_seats('טעות') if c == 12] == [(12, 2), (12, 3), (12, 30), (12, 31)] and [(c, v) for c, v in onk_seats('קדם יי') if c == 12] == [(12, 4), (12, 7), (12, 11), (12, 12), (12, 18), (12, 25), (12, 28), (12, 31)] and aramaic(12, 4) == ['לא', 'תעבדון', 'כן', 'קדם', 'יי', 'אלהכון'] and aramaic(12, 11)[-4:] == ['די', 'תדרון', 'קדם', 'יי']   # "their ERRORS" for their gods (four seats); "to the LORD" made "BEFORE the LORD" at 12:4, 12:11, 12:31 — the Aramaic's reverence
assert onk_seats('נכסת קודש') == [(12, 6), (12, 11), (12, 27), (16, 2), (27, 7), (33, 19)] and onk_seats('אפרשות יד') == [(12, 6), (12, 11), (12, 17)] and aramaic(12, 26)[:3] == ['לחוד', 'מעשר', 'קודשיך'] and onk_tok('מעשר') == [(12, 17), (12, 26), (14, 23), (14, 28), (26, 12)] and 'מעשר' not in W12(26)   # THE TITHE SUPPLIED at 12:26 — "your holy things" made "the tithe of your holy things": the Aramaic names the second tithe where the Hebrew has none (the shelf's 77:1 reads the verse of holy things from abroad)
assert onk_seats('מרחק') == [(7, 25), (7, 26), (12, 31), (14, 3), (17, 1), (18, 12), (22, 5), (23, 19), (24, 4), (25, 16), (27, 15)] and aramaic(12, 15)[-5:] == ['ודכיא', 'יכלניה', 'כבשר', 'טביא', 'ואילא'] and aramaic(12, 22)[:7] == ['ברם', 'כמא', 'די', 'מתאכל', 'בשר', 'טביא', 'ואילא'] and 'ואנש' in aramaic(12, 7) and aramaic(12, 9)[5:7] == ['לבית', 'ניחא']   # "distanced before the LORD" for abomination; "the FLESH of the gazelle" supplied twice; "the MEN of your houses" supplied at 12:7 (the shelf's 64:4 reads the house as the wife); "the house of rest" at 12:9
assert onk_tok('לרחצן') == [(12, 10), (33, 12), (33, 28)] and onk_seats('מסאבא ודכיא') == [(12, 15), (12, 22), (15, 22)] and onk_seats('תכוס') == [(12, 15), (12, 21), (16, 2), (16, 4), (16, 6), (17, 1), (27, 7)] and aramaic(12, 17)[:5] == ['לית', 'לך', 'רשו', 'למיכל', 'בקרויך'] and len(onk_seats('רשו')) == 13 and onk_seats('כשר') == [(6, 18), (12, 8), (12, 25), (12, 28), (13, 19), (21, 9), (33, 10)]   # "YOU HAVE NO PERMISSION" for "you are not able" (12:17 — the shelf's 72:1 reads it the same); "what is FIT before Him" for "right in His eyes" at three seats of the chapter
assert onk_seats('מליל לך') == [(12, 20), (15, 6), (26, 18), (29, 12)] and onk_tok('פקדתך') == [(12, 21)] and aramaic(12, 30)[-5:] == ['טעותהון', 'ואעבד', 'כן', 'אף', 'אנא'] and aramaic(12, 30)[3] == 'תתקל' and [(c, v) for c, v in onk_seats('מימר') if c == 12] == [(12, 30)] and 'למימר' in aramaic(12, 30) and 'מימרא' not in aramaic(12, 30) and [(12, v + 1) for v in range(len(onk_he[11])) if '(' in clean(onk_he[11][v])] == []   # "as He SPOKE to you" the Aramaic's four = the Hebrew's four; "as I commanded you" the one; NO MEMRA in the chapter (12:30's hit is "saying", the substring)
assert aramaic(12, 23) == ['לחוד', 'תקף', 'בדיל', 'דלא', 'למיכל', 'דמא', 'ארי', 'דמא', 'הוא', 'נפשא', 'ולא', 'תיכול', 'נפשא', 'עם', 'בשרא'] and aramaic(12, 2)[:2] == ['אבדא', 'תאבדון'] and aramaic(12, 3)[:3] == ['ותתרעון', 'ית', 'אגוריהון'] and len(onk_seats('וקד')) == 11
# ---- THE ENGLISH'S BRACKETS (the F print) ----
BR = {v: re.findall(r'\[([^\]]+)\]', clean(onk[11][v - 1])) for v in range(1, 32)}
assert sum(len(b) for b in BR.values()) == 25 and {v: len(b) for v, b in BR.items() if b} == {2: 1, 3: 1, 4: 1, 5: 2, 6: 1, 7: 1, 8: 1, 9: 1, 11: 2, 15: 1, 21: 1, 22: 1, 23: 1, 25: 1, 26: 1, 27: 1, 28: 2, 30: 1, 31: 4} and BR[5] == ['have His Shechinah dwell', 'at the abode of His Shechinah'] and BR[26] == ['tithes'] and BR[31] == ['before', 'distanced before', 'idols', 'idols'] and [v for v in range(1, 32) if '(' in clean(onk[11][v - 1])] == []
# ---- THE STORE'S GLOSSES (the display layer, never the draft): a selection read back per verse; the families censused over the whole store (the G print) ----
assert sg(12, 5, 'יבחר') == 'try' and sg(12, 15, 'רק') == 'leanness' and sg(12, 16, 'הדם') == 'the-blood--of-man' and sg(12, 7, 'ושמחתם') == 'and-brighten-up' and sg(12, 12, 'חלק') == 'smoothness' and sg(12, 15, 'כצבי') == 'like-splendor' and sg(12, 22, 'הצבי') == 'the-splendor' and sg(12, 17, 'תוכל') == 'be-able' and sg(12, 5, 'תדרשו') == 'tread' and sg(12, 21, 'ירחק') == 'widen' and sg(12, 20, 'גבולך') == 'cord-you/your'
assert sg(12, 10, 'בטח') == 'place-of-refuge' and sg(12, 9, 'המנוחה') == 'the-repose' and sg(12, 30, 'תנקש') == 'entrap' and sg(12, 19, 'תעזב') == 'loosen' and sg(12, 23, 'חזק') == 'fasten-upon' and sg(12, 2, 'רענן') == 'verdant' and sg(12, 2, 'הרמים') == 'the-be-high-actively' and sg(12, 11, 'מבחר') == 'select' and sg(12, 7, 'משלח') == 'sending-out' and sg(12, 6, 'תרומת') == 'present' and sg(12, 6, 'ונדבתיכם') == 'and-spontaneity-you/your (pl)' and sg(12, 22, 'יחדו') == 'unit' and sg(12, 22, 'אך') == 'particle-of-affirmation'
assert sg(12, 3, 'מצבתם') == 'something-stationed-them/their' and sg(12, 14, 'שבטיך') == 'scion-you/your' and sg(12, 1, 'החקים') == 'the-enactment' and sg(12, 31, 'תועבת') == 'something-disgusting' and sg(12, 5, 'כי') == 'very-widely-used-as-a-relati' and sg(12, 5, 'אם') == 'as-demonstrative' and sg(12, 11, 'אנכי') == '?' and sg(12, 30, 'אני') == '?' and sg(12, 6, 'ובכרת') == 'and-firstling-of-man' and sg(12, 27, 'ודם') == 'and-blood--of-man' and sg(12, 2, 'תאבדון') == 'wander-away-suffix' and sg(12, 3, 'ואבדתם') == 'and-wander-away'
GLOSS_FAMILY = {'and-brighten-up': [('ושמחת', 6), ('ושמחתם', 3), ('ושמח', 2)], "and-'Asherah-them/their": [('ואשירהם', 1), ('ואשריהם', 1)], 'and-blood--of-man': [('ודם', 3)], 'and-the-blood--of-man': [('והדם', 1)], 'and-firstling-of-man': [('ובכרת', 3)], 'and-spontaneity-you/your': [('ונדבתיך', 1)], 'and-spontaneity-you/your (pl)': [('ונדבתיכם', 2)], 'cord-you/your': [('גבולך', 6), ('גבלך', 5)], 'entrap': [('תנקש', 1)], 'from-circle': [('מסביב', 4)], 'from-herd-you/your': [('מבקרך', 1)], 'gate-you/your': [('שעריך', 11)], 'in-gate-you/your (pl)': [('בשעריכם', 1)],
                'like-benediction': [('כברכת', 2)], 'like-splendor': [('כצבי', 2)], 'the-splendor': [('הצבי', 1)], 'the-stag': [('האיל', 1)], 'and-like-stag': [('וכאיל', 2)], 'longing': [('אות', 4), ('תאוה', 2)], 'particle-of-affirmation': [('אך', 41)], 'place-of-refuge': [('בטח', 3)], 'the-repose': [('המנוחה', 1)], 'sending-out': [('משלח', 6)], 'select': [('מבחר', 1)], 'something-stationed-them/their': [('מצבתם', 2), ('מצבתיהם', 1)], 'tenth-you/your (pl)': [('מעשרתיכם', 3)], 'the-foul-in-a-religious-sense': [('הטמא', 10), ('הטמאה', 2), ('הטמאים', 1)], 'the-be-high-actively': [('הרמים', 1)], 'unit': [('יחדו', 14), ('יחד', 1)],
                'promise-you/your': [('נדריך', 1)], 'promise-you/your (pl)': [('נדריכם', 2)], 'and-promise-you/your': [('ונדריך', 1)], 'and-promise-you/your (pl)': [('ונדריכם', 1)], 'scion-you/your': [('שבטיך', 2)], 'burnt-offering-you/your (pl)': [('עלתיכם', 2), ('עולתיכם', 1)], 'sacrifice-you/your': [('זבחיך', 1)], 'and-sacrifice-you/your (pl)': [('וזבחיכם', 2)], 'herd-you/your': [('בקרך', 3)], 'herd-you/your (pl)': [('בקרכם', 2)], 'and-flock-you/your': [('וצאנך', 4)], 'and-flock-you/your (pl)': [('וצאנכם', 1)], 'and-from-flock-you/your': [('ומצאנך', 1)],
                'God-them/their': [('אלהיהם', 13), ('אלהיהן', 3), ('אלהימו', 1)], 'to-God-them/their': [('לאלהיהם', 7), ('לאלהיהן', 1)], 'daughter-them/their': [('בנתם', 1), ('בנתיהם', 1)], 'son-them/their': [('בניהם', 2)], 'and-daughter-you/your (pl)': [('ובנתיכם', 2)], 'and-son-you/your (pl)': [('ובניכם', 4)], 'and-servant-you/your (pl)': [('ועבדיכם', 1)], 'and-maidservant-you/your (pl)': [('ואמהתיכם', 1)], 'ground-you/your': [('אדמתך', 12)], 'from-face-you/your': [('מפניך', 20)], 'to-residence-him/its': [('לשכנו', 1)], 'to-reside': [('לשכן', 8)], 'to-put/set': [('לשום', 5)],
                'in-eye-him/its': [('בעיניו', 10), ('בעינו', 1)], 'and-the-straight': [('והישר', 2)], 'and-the-pure': [('והטהור', 3)], 'in-one': [('באחד', 16), ('באחת', 3)], 'like-all': [('ככל', 35)], 'like-waters': [('כמים', 4)], 'with-you/your (pl)': [('אתכם', 22), ('עמכם', 22)], 'verdant': [('רענן', 1)], 'the-these': [('האלה', 80), ('האל', 8)], 'and-to-son-you/your': [('ולבניך', 9)], 'from-you/your': [('ממך', 22)], 'God-you/your': [('אלהיך', 252)], 'God-you/your (pl)': [('אלהיכם', 85)], 'in-place': [('במקום', 36), ('במקם', 1)]}
GT = {g: store.execute("SELECT REPLACE(w.he_plain,'/',''), COUNT(*) FROM words w WHERE w.gloss=? GROUP BY 1 ORDER BY 2 DESC, 1", (g,)).fetchall() for g in GLOSS_FAMILY}
assert all(sorted(GT[g]) == sorted(v) for g, v in GLOSS_FAMILY.items()), [(g, GT[g]) for g, v in GLOSS_FAMILY.items() if sorted(GT[g]) != sorted(v)]
# BY GLOSS — every token of the gloss the one word (or one family read the same at every seat): the rewrite covers the whole store (SIXTY-NINE)
OVERRIDE_GLOSS = [('and-brighten-up', 'and-rejoice'), ("and-'Asherah-them/their", 'and-their-Asherim'), ('and-blood--of-man', 'and-the-blood-of'), ('and-the-blood--of-man', 'and-the-blood'), ('and-firstling-of-man', 'and-the-firstlings-of'), ('and-spontaneity-you/your', 'and-your-freewill-offerings'), ('and-spontaneity-you/your (pl)', 'and-your-freewill-offerings'), ('cord-you/your', 'your-border'), ('entrap', 'be-ensnared'), ('from-circle', 'round-about'), ('from-herd-you/your', 'from-your-herd'), ('gate-you/your', 'your-gates'), ('in-gate-you/your (pl)', 'within-your-gates'),
                  ('like-benediction', 'according-to-the-blessing-of'), ('like-splendor', 'as-the-gazelle'), ('the-splendor', 'the-gazelle'), ('the-stag', 'the-hart'), ('and-like-stag', 'and-as-the-hart'), ('longing', 'desire'), ('particle-of-affirmation', 'only'), ('place-of-refuge', 'in-safety'), ('the-repose', 'the-rest'), ('sending-out', 'the-undertaking-of'), ('select', 'the-choice-of'), ('something-stationed-them/their', 'their-pillars'), ('tenth-you/your (pl)', 'your-tithes'), ('the-foul-in-a-religious-sense', 'the-unclean'), ('the-be-high-actively', 'the-high'), ('unit', 'together'),
                  ('promise-you/your', 'your-vows'), ('promise-you/your (pl)', 'your-vows'), ('and-promise-you/your', 'and-your-vows'), ('and-promise-you/your (pl)', 'and-your-vows'), ('scion-you/your', 'your-tribes'), ('burnt-offering-you/your (pl)', 'your-burnt-offerings'), ('sacrifice-you/your', 'your-sacrifices'), ('and-sacrifice-you/your (pl)', 'and-your-sacrifices'), ('herd-you/your', 'your-herd'), ('herd-you/your (pl)', 'your-herd'), ('and-flock-you/your', 'and-your-flock'), ('and-flock-you/your (pl)', 'and-your-flock'), ('and-from-flock-you/your', 'and-from-your-flock'),
                  ('God-them/their', 'their-gods'), ('to-God-them/their', 'to-their-gods'), ('daughter-them/their', 'their-daughters'), ('son-them/their', 'their-sons'), ('and-daughter-you/your (pl)', 'and-your-daughters'), ('and-son-you/your (pl)', 'and-your-sons'), ('and-servant-you/your (pl)', 'and-your-menservants'), ('and-maidservant-you/your (pl)', 'and-your-maidservants'), ('ground-you/your', 'your-land'), ('from-face-you/your', 'from-before-you'), ('to-residence-him/its', 'to-his-dwelling'), ('to-reside', 'to-make-dwell'), ('to-put/set', 'to-put'),
                  ('in-eye-him/its', 'in-his-eyes'), ('and-the-straight', 'and-the-right'), ('and-the-pure', 'and-the-clean'), ('in-one', 'in-one-of'), ('like-all', 'according-to-all'), ('like-waters', 'like-water'), ('with-you/your (pl)', 'with-you'), ('verdant', 'leafy'), ('the-these', 'these'), ('and-to-son-you/your', 'and-to-your-children'), ('from-you/your', 'from-you'), ('God-you/your', 'your-God'), ('God-you/your (pl)', 'your-God'), ('in-place', 'in-the-place')]
# BY REFERENCE — the family mixed (a homograph, a verb read two ways, a noun singular and plural, Moses' "I" beside the store's "?"): the seat named (ONE HUNDRED AND TWENTY-FOUR)
OVERRIDE_REF_SPEC = [(1, 'אלהי', 'the-God-of', 0), (1, 'נתן', 'has-given', 0), (1, 'הימים', 'the-days', 0), (1, 'חיים', 'live', 0), (1, 'בארץ', 'in-the-land', 0), (1, 'תשמרון', 'you-shall-keep', 0), (1, 'לעשות', 'to-do', 0), (2, 'אבד', 'utterly', 0), (2, 'תאבדון', 'you-shall-destroy', 0), (2, 'עבדו', 'served', 0), (2, 'הגוים', 'the-nations', 0), (2, 'ירשים', 'are-dispossessing', 0), (2, 'ההרים', 'the-mountains', 0), (2, 'הגבעות', 'the-hills', 0),
                     (3, 'ונתצתם', 'and-you-shall-tear-down', 0), (3, 'ושברתם', 'and-you-shall-break', 0), (3, 'ופסילי', 'and-the-images-of', 0), (3, 'ואבדתם', 'and-you-shall-destroy', 0), (4, 'תעשון', 'you-shall-do', 0), (5, 'כי', 'but', 0), (5, 'אם', 'only', 0), (5, 'שמו', 'his-name', 0), (5, 'תדרשו', 'you-shall-seek', 0), (5, 'ובאת', 'and-you-shall-come', 0), (6, 'והבאתם', 'and-you-shall-bring', 0), (6, 'תרומת', 'the-heave-offering-of', 0), (6, 'ידכם', 'your-hand', 0),
                     (7, 'לפני', 'before', 0), (7, 'ידכם', 'your-hand', 0), (7, 'ובתיכם', 'and-your-households', 0), (7, 'ברכך', 'has-blessed-you', 0), (8, 'תעשון', 'you-shall-do', 0), (8, 'עשים', 'are-doing', 0), (9, 'באתם', 'you-have-come', 0), (9, 'נתן', 'is-giving', 0), (10, 'ועברתם', 'and-you-shall-cross', 0), (10, 'וישבתם', 'and-you-shall-dwell', 0), (10, 'בארץ', 'in-the-land', 0), (10, 'והניח', 'and-He-gives-rest', 0), (10, 'וישבתם', 'and-you-shall-dwell', 1),
                     (11, 'והיה', 'and-it-shall-be', 0), (11, 'שמו', 'his-name', 0), (11, 'תביאו', 'you-shall-bring', 0), (11, 'אנכי', 'I', 0), (11, 'ותרמת', 'and-the-heave-offering-of', 0), (11, 'ידכם', 'your-hand', 0), (11, 'תדרו', 'you-vow', 0), (12, 'לפני', 'before', 0), (12, 'חלק', 'portion', 0), (13, 'השמר', 'take-heed', 0), (13, 'תעלה', 'you-offer-up', 0), (13, 'עלתיך', 'your-burnt-offerings', 0), (14, 'כי', 'but', 0), (14, 'אם', 'only', 0), (14, 'תעלה', 'you-shall-offer-up', 0), (14, 'עלתיך', 'your-burnt-offerings', 0), (14, 'תעשה', 'you-shall-do', 0), (14, 'אנכי', 'I', 0),
                     (15, 'תזבח', 'you-may-slaughter', 0), (15, 'נתן', 'has-given', 0), (15, 'יאכלנו', 'may-eat-it', 0), (16, 'תשפכנו', 'you-shall-pour-it', 0), (17, 'תוכל', 'you-may', 0), (17, 'מעשר', 'the-tithe-of', 0), (17, 'תדר', 'you-vow', 0), (17, 'ותרומת', 'and-the-heave-offering-of', 0), (18, 'כי', 'but', 0), (18, 'אם', 'only', 0), (18, 'לפני', 'before', 0), (18, 'תאכלנו', 'you-shall-eat-it', 0), (18, 'ובנך', 'and-your-son', 0), (18, 'ובתך', 'and-your-daughter', 0), (18, 'ועבדך', 'and-your-manservant', 0), (18, 'לפני', 'before', 1),
                     (19, 'השמר', 'take-heed', 0), (19, 'תעזב', 'you-forsake', 0), (20, 'ירחיב', 'enlarges', 0), (20, 'דבר', 'He-has-spoken', 0), (20, 'ואמרת', 'and-you-say', 0), (20, 'אכלה', 'let-me-eat', 0), (20, 'תאוה', 'craves', 0), (21, 'ירחק', 'is-too-far', 0), (21, 'שמו', 'his-name', 0), (21, 'וזבחת', 'and-you-shall-slaughter', 0), (21, 'נתן', 'has-given', 0), (21, 'צויתך', 'I-have-commanded-you', 0), (22, 'יאכל', 'is-eaten', 0), (22, 'תאכלנו', 'you-shall-eat-it', 0), (22, 'יאכלנו', 'may-eat-it', 0),
                     (23, 'חזק', 'be-steadfast', 0), (23, 'הוא', 'is', 0), (23, 'הנפש', 'the-life', 0), (23, 'הנפש', 'the-life', 1), (24, 'תאכלנו', 'you-shall-eat-it', 0), (24, 'תשפכנו', 'you-shall-pour-it', 0), (25, 'תאכלנו', 'you-shall-eat-it', 0), (25, 'תעשה', 'you-do', 0), (25, 'בעיני', 'in-the-eyes-of', 0), (26, 'קדשיך', 'your-holy-things', 0), (26, 'תשא', 'you-shall-take-up', 0), (26, 'ובאת', 'and-you-shall-go', 0), (27, 'ועשית', 'and-you-shall-offer', 0), (27, 'עלתיך', 'your-burnt-offerings', 0), (27, 'ישפך', 'shall-be-poured-out', 0),
                     (28, 'שמר', 'observe', 0), (28, 'ושמעת', 'and-hear', 0), (28, 'הדברים', 'the-words', 0), (28, 'אנכי', 'I', 0), (28, 'תעשה', 'you-do', 0), (28, 'בעיני', 'in-the-eyes-of', 0), (29, 'יכרית', 'cuts-off', 0), (29, 'הגוים', 'the-nations', 0), (29, 'בא', 'are-going', 0), (29, 'וירשת', 'and-you-dispossess', 0), (29, 'וישבת', 'and-dwell', 0), (30, 'השמר', 'take-heed', 0), (30, 'הגוים', 'the-nations', 0), (30, 'יעבדו', 'serve', 0), (30, 'ואעשה', 'and-I-will-do', 0), (30, 'אני', 'I', 0), (31, 'תעשה', 'you-shall-do', 0), (31, 'שנא', 'He-hates', 0), (31, 'עשו', 'they-did', 0), (31, 'ישרפו', 'they-burn', 0)]
OVERRIDE_REF3 = [(f'Deut.12.{v}:{sidx(12, v, tok, nth)}', new, tok) for v, tok, new, nth in OVERRIDE_REF_SPEC]
OVERRIDE_REF = [(k, v) for k, v, _ in OVERRIDE_REF3]
assert len(OVERRIDE_REF) == len({k for k, _ in OVERRIDE_REF}) == len(OVERRIDE_REF_SPEC) == 124 and len(OVERRIDE_GLOSS) == 69 and len({k for k, _ in OVERRIDE_GLOSS}) == 69, (len(OVERRIDE_REF), len(OVERRIDE_GLOSS))
assert all(g in GLOSS_FAMILY for g, _ in OVERRIDE_GLOSS) and all(sg(12, v, tok, nth) is not None for v, tok, _, nth in OVERRIDE_REF_SPEC)
ALREADY = {'?': '', 'altar-them/their': 'their-altars', 'and-maidservant-you/your': 'and-your-maidservant', 'and-must-you/your': 'and-your-wine', 'and-oil-you/your': 'and-your-oil', 'and-the-judgment': 'and-the-judgments', 'be--make-well': 'do-well', 'be--on-fire-suffix': 'you-shall-burn', 'day-you/your': 'your-days', 'desolate-them/their': 'destroyed-them', 'fell-a-tree-suffix': 'you-shall-cut-down', 'hating-you/your (pl)': 'your-enemies', 'hind-part': 'after', 'hind-part-them/their': 'after-them', 'hind-part-you/your': 'after-you', 'in-gate-you/your': 'within-your-gates', 'increase-you/your': 'your-grain', 'inherit--mode-of-descent)': 'inherit', 'keep/guard-suffix': 'keep', 'leanness': 'only', 'like-as/which': 'as', 'living-being-you/your': 'your-soul', 'scion-you/your (pl)': 'your-tribes', 'something-disgusting': 'abomination', 'spill-forth': 'shed', 'the-blood--of-man': 'the-blood', 'the-enactment': 'the-statutes', 'the-he/it': 'that', 'the-straight': 'the-right', 'there-suffix': 'thither', 'this-place': 'here', 'to-failure-of': 'so-as-not', 'to-possess/inherit-her/its': 'to-possess-it', 'try': 'choose', 'wander-away': 'perish', 'wander-away-suffix': 'you-shall-perish'}
assert len(ALREADY) == 36
OV = open(f'{ROOT}/logic/glosses/word_gloss_overrides.yaml', encoding='utf-8').read()
PATCHED = 'THE DEUTERONOMY WALK sitting 10 (2026-09-20, Deuteronomy 12)' in OV
assert all(f'"{k}": "{v}"' in OV for k, v in ALREADY.items()) and all(f'"{k}": ' not in OV for k, _ in OVERRIDE_GLOSS if not PATCHED) and (PATCHED or '"Deut.12.' not in OV), [k for k, _ in OVERRIDE_GLOSS if f'"{k}": ' in OV]
if PATCHED: assert all(f'"{k}": "{v}"' in OV for k, v in OVERRIDE_REF) and all(f'"{k}": "{v}"' in OV for k, v in OVERRIDE_GLOSS), [k for k, v in OVERRIDE_REF + OVERRIDE_GLOSS if f'"{k}": "{v}"' not in OV][:6]
assert OV.count('  "Deut.11.32:11": "today"') == 1 and 'THE DEUTERONOMY WALK sitting 9 (2026-09-20, Deuteronomy 11)' in OV
# ---- THE REGISTER'S FINDER on the chapter (the H print): the header at 12:1 declared EMPTY on the register index; no receipt with the Name — 12:21's "as I have commanded you" invisible to the finder's two forms
with contextlib.redirect_stdout(io.StringIO()):
    import register_census as RC
    _ink = RC.read_ink()
assert [k for k in RC.receipts(_ink) if k[0] == 'Deut' and k[1] == 12] == [] and [x for x in RC.footers(_ink) if x[0][0] == 'Deut' and x[0][1] == 12] == [(('Deut', 12, 1), {'noun': 'statutes', 'kind': 'HEADER', 'stamp': 'none'})] and [x for x in RC.register_headers(_ink) if x[0][0] == 'Deut' and x[0][1] == 12] == [] and [k for k in RC.receipts(_ink) if k[0] == 'Deut' and k[1] <= 12] == [('Deut', 1, 3), ('Deut', 1, 19), ('Deut', 1, 41), ('Deut', 4, 5), ('Deut', 5, 12), ('Deut', 5, 16), ('Deut', 5, 32), ('Deut', 10, 5)]
RD = open(f'{ROOT}/World/step9/register_dispositions.yaml', encoding='utf-8').read() if os.path.exists(f'{ROOT}/World/step9/register_dispositions.yaml') else ''
FAIL_ALL = list(FAIL)

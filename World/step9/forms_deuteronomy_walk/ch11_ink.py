import os as _os
_ROOT = _os.path.normpath(_os.path.join(_os.path.dirname(_os.path.abspath(__file__)), '..', '..', '..'))   # THE PORTABLE REPO (2026-09-15): the repo root from this file's own place
#!/usr/bin/env python3
# THE DEUTERONOMY WALK, sitting 9 — CHAPTER 11, Deuteronomy 11:1-32 (2026-09-20; the owner: "Go" after the reread that followed 8b's compaction; ONE RUN under
# THE TWO-RUN RULE — the rereads, the measurements, the ink, the design, the rows, the ledger, the seat, the gates, the records): THE INK of the chapter, computed
# from the Tanakh DB, the snapshot store and the shelf's own bytes — never typed. Sitting 8's form (ch10_ink.py): the generic helpers copied by derive_ch11_ink.py
# from that file by content markers, the constants and every assert chapter 11's own, typed FROM THE PRINTS (ch11_dump0.out, ch11_measure1.out). THE TWO DIVISIONS
# AGREE (32 = 32; the alignment the identity, cost 18). THE SPINE IS ON THE CHAPTER for the first time since chapter 6 — TWENTY-TWO piskaot (37-58) with 171 rows,
# the heads on 11:10, 10, 11, 12, 13, 14, 15, 18, (45 without a citation — its words 11:18's), 19, 21, 22, 22, 23, 24, 25, 26, 26, 29, 30, 31, 32; SEVEN rows
# elsewhere cite it by the union of both files (the frontlets' spellings at 35:4, the doorposts' second plural at 36:3, the sages weeping at the border at 80:4-5,
# the shut heavens in the Ha'azinu parables at 306:4, 306:6, 306:9), ONE excluded (234:6 — the English's "(Dt.11:12)" for 22:12's garment). The parser MEASURED on
# every verse — NO NUMBER VERSE in the chapter (the book's first such chapter since the walk began), "swore" twice no number, "be satisfied" starred at 11:15.
# THE STORE = THE DB at every verse (no written/read pair; 508 tokens, 1,992 letters; the seven "?" glosses the store's "I"). The hand's facts as asserts, run
# all at once by assert_driver.py.
import json, os, re, html, sqlite3, sys, io, contextlib, unicodedata, subprocess
from collections import Counter
ROOT = _ROOT
sys.path.insert(0, f'{ROOT}/World/step9')
DATE = '2026-09-20'
CH = 11
UIDS = ['deu_11_bless_curse_set']
SPANS = {'deu_11_bless_curse_set': (11, 1, 32)}
PREFIX = {'deu_11_bless_curse_set': 'DV11'}
PISKAOT = list(range(37, 59))   # THE SPINE ON THE CHAPTER: twenty-two piskaot 37-58 — twenty-one heads computed in chapter 11 (the A print) and piska 45, whose one row opens with 11:18's own words and carries no citation (the head regex finds none); 36 on 6:9 before, 59 on 12:1 after
SPINE_ROWS = {37: 16, 38: 11, 39: 11, 40: 14, 41: 20, 42: 10, 43: 35, 44: 1, 45: 1, 46: 1, 47: 9, 48: 12, 49: 3, 50: 4, 51: 3, 52: 4, 53: 2, 54: 4, 55: 2, 56: 4, 57: 3, 58: 1}   # rows per piska, both files (the I print) — 171
EXP2DB = {e: [e] for e in range(1, 33)}   # the identity — 32 = 32 (chapter 5 the book's one split)
DB2EXP = {d: e for e, ds in EXP2DB.items() for d in ds}
# the Hebrew's book-named citations of chapter 11 OUTSIDE the spine (the regex reads "(דברים יא כ)" etc.); 306:4 and 306:9 cite by "(שם יא יז)" — the ibid. form the regex misses, the English's (Dt.11:17) catches; 35:4's Hebrew cites Exodus 13:9 alone, the English adds (Dt.11:18)
OUTSIDE_HE = [(36, 3, (11, 20)), (80, 4, (11, 31)), (80, 5, (11, 31)), (306, 6, (11, 17))]
OUTSIDE = [(35, 4), (36, 3), (80, 4), (80, 5), (306, 4), (306, 6), (306, 9)]   # the SEVEN rows READ WHOLE: the union of both files beyond piskaot 37-58, less the excluded slip
EXCLUDED = [(234, 6)]   # the English export cites '(Dt.11:12)' for "of your garment" — the row is on 22:12 (the tassels' garment); the Hebrew cites nothing; a wrong chapter (chapter 6's lesson was a wrong book)
INTERPOLATION = []   # no translator's own citation of chapter 11 marked as such
CITED = {(35, 4): [18], (36, 3): [20], (80, 4): [31], (80, 5): [31], (306, 4): [17], (306, 6): [17], (306, 9): [17]}
CITED_DB = {k: v[0] for k, v in CITED.items()}
PRIOR_READ = {(35, 4): 'deu_06_vaetchanan_2026-09-17.md', (36, 3): 'deu_06_vaetchanan_2026-09-17.md'}   # two read before at sitting 4 (the frontlets, the doorposts) — REREAD WHOLE here
HEADS_ON = {35: (6, 8), 36: (6, 9), 80: (12, 29), 306: (32, 1), 234: (22, 12)}
FRESH = OUTSIDE[:]   # every one of the seven read whole this sitting
CREDITED = {}   # under THE WHOLE-ROW RULE no spine row is credited: the forty-one read before (twenty-three at the Deuteronomy sittings, eighteen at Genesis sittings) are REREAD WHOLE here and marked so
TITLE = "Chapter 11 — Love the LORD and keep His charge; the discipline your children have not seen — Egypt, the sea, the wilderness, Dathan and Abiram; keep all the commandment, go in and possess, prolong days on the land of milk and honey; a land not like Egypt's garden of herbs but of hills and valleys drinking the rain of heaven, a land the LORD seeks, His eyes on it from the year's beginning to its end; if you hearken — the rain in its season, the early and the late, grain, wine and oil, grass for the cattle; take heed lest the heart be deceived — the anger, the heaven shut, no rain, no produce, perishing quickly from the good land; these My words on the heart, bound on the hand, frontlets between the eyes, taught to the children, written on the doorposts and the gates — days as the days of heaven above the earth; keep, love, walk, cleave — the nations dispossessed, every place the sole treads, the wilderness to Lebanon, the river to the western sea, no man standing, dread and fear as He spoke; see, a blessing and a curse set today — the blessing on Mount Gerizim and the curse on Mount Ebal beyond the Jordan opposite Gilgal beside the terebinths of Moreh; cross, possess, dwell, and keep to do the statutes and the judgments set before you today"
OUT = f'{ROOT}/logic/oral_triage/deu_11_ekev_reeh_{DATE}.md'
db = sqlite3.connect(f'file:{ROOT}/Data/tanakh.sqlite?mode=ro', uri=True)
# ---- THE HELPERS (ch10_ink.py's, copied by content markers) ----
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
# ---- THE INK'S HELPERS, THE DB AND THE STORE (ch10_ink.py's, the chapter substituted) ----
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
def W11(v): return words('Deut', 11, v)
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
for c, v, idx, hp, g in store.execute("SELECT v.chapter, v.verse, w.idx, w.he_plain, w.gloss FROM words w JOIN verses v ON w.verse_id=v.id WHERE v.book='Deut' AND v.chapter = 11 ORDER BY v.id, w.idx"):
    SG.setdefault((c, v), []).append((idx, hp.replace('/', ''), g))
def sg(c, v, tok, nth=0):
    hit = [g for _, hp, g in SG[(c, v)] if hp == tok]
    if len(hit) <= nth: raise KeyError((c, v, tok, nth))
    return hit[nth]
def sidx(c, v, tok, nth=0):
    hit = [i for i, hp, _ in SG[(c, v)] if hp == tok]
    assert len(hit) > nth, (c, v, tok, nth, hit)
    return hit[nth]
STORE_MISMATCH = [(c, v, n, len(by[('Deut', c, v)])) for c, v, n in store.execute("SELECT v.chapter, v.verse, COUNT(*) FROM words w JOIN verses v ON w.verse_id=v.id WHERE v.book='Deut' AND v.chapter=11 GROUP BY v.chapter, v.verse").fetchall() if n != len(by[('Deut', c, v)])]
# ---- THE SHELF BY POSITION — the spine ON the chapter: twenty-two piskaot (37-58) head in chapter 11; 36 on 6:9 before, 59 on 12:1 after; the two files' grains ----
assert len(sif) == 357 and len(sif_he) == 357 and sum(len(s) for s in sif) == 2357 and sum(len(s) for s in sif_he) == 2357
HC = Counter(h[0] for h in heads.values() if h)
assert [p for p, h in heads.items() if h and h[0] == 11] == [p for p in PISKAOT if p != 45] and HC[11] == 21 and HC[10] == 0 and HC[7] == 0 and sorted(HC.items())[:11] == [(1, 24), (3, 4), (6, 6), (11, 21), (12, 20), (13, 14), (14, 14), (15, 16), (16, 19), (17, 16), (18, 16)], sorted(HC.items())[:11]
assert {p: heads[p] for p in range(36, 60)} == {36: (6, 9), 37: (11, 10), 38: (11, 10), 39: (11, 11), 40: (11, 12), 41: (11, 13), 42: (11, 14), 43: (11, 15), 44: (11, 18), 45: None, 46: (11, 19), 47: (11, 21), 48: (11, 22), 49: (11, 22), 50: (11, 23), 51: (11, 24), 52: (11, 25), 53: (11, 26), 54: (11, 26), 55: (11, 29), 56: (11, 30), 57: (11, 31), 58: (11, 32), 59: (12, 1)}, {p: heads[p] for p in range(36, 60)}
assert HB0(45, 1).startswith('ושמתם את דברי אלה על לבבכם') and 'סם חיים' in HB0(45, 1) and '(Dt.11:18)' in E(45, 1) and he_cites(Hb(45, 1)) == [('בראשית', 4, 7), ('בראשית', 8, 21)] and '(משלי כה כא-כב)' in Hb(45, 1)   # piska 45's one row: no head citation — its first words 11:18's own (the life-giving potion; the compulsion to evil); the spine's, not an outside row
assert {p: (len(sif_he[p - 1]), len(sif[p - 1])) for p in PISKAOT} == {p: (n, n) for p, n in SPINE_ROWS.items()} and sum(SPINE_ROWS.values()) == 171 and len(PISKAOT) == 22
CIT_HE = [(p, r, (11, c[2])) for p in range(1, 358) for r in range(1, len(sif_he[p - 1]) + 1) for c in he_cites(Hb(p, r)) if c[0] == 'דברים' and c[1] == 11]
CIT_EN = [(p, r, (11, int(m.group(2)))) for p in range(1, 358) for r in range(1, len(sif[p - 1]) + 1) for m in re.finditer(r'\((?:Deut(?:eronomy)?\.?|Dt\.?|Devarim) ?(11):(\d+)', E(p, r))]
assert len(CIT_HE) == 33 and len(CIT_EN) == 196, (len(CIT_HE), len(CIT_EN))
assert [(p, r, v) for p, r, v in CIT_HE if p not in PISKAOT] == OUTSIDE_HE
SPINE_CITES_HE = [(37, 1, (11, 10)), (37, 16, (11, 9)), (38, 1, (11, 10)), (39, 1, (11, 11)), (40, 1, (11, 12)), (40, 12, (11, 17)), (41, 1, (11, 13)), (41, 20, (11, 14)), (42, 1, (11, 14)), (43, 1, (11, 15)), (43, 23, (11, 17)), (44, 1, (11, 18)), (46, 1, (11, 19)), (46, 1, (11, 21)), (47, 1, (11, 21)), (48, 1, (11, 22)), (48, 1, (11, 13)), (49, 1, (11, 22)), (49, 3, (11, 23)), (50, 1, (11, 23)), (51, 1, (11, 24)), (51, 1, (11, 23)), (52, 1, (11, 25)), (53, 1, (11, 26)), (54, 2, (11, 28)), (55, 1, (11, 29)), (56, 1, (11, 30)), (57, 1, (11, 31)), (58, 1, (11, 32))]
assert [(p, r, v) for p, r, v in CIT_HE if p in PISKAOT] == SPINE_CITES_HE and len(SPINE_CITES_HE) == 29   # every piska's head row cites its verse by name, but 45's; 40:12, 43:23 cite 11:17 inside; 46:1 and 48:1 cite two verses; 37:16 cites 11:9 (the milk and honey)
UNION = sorted({(p, r) for p, r, _ in CIT_HE} | {(p, r) for p, r, _ in CIT_EN})
assert len(UNION) == 112 and sorted(set(UNION) - {(p, r) for p, r in UNION if p in PISKAOT}) == sorted(OUTSIDE + EXCLUDED) and len(OUTSIDE) == 7 and len([(p, r) for p, r in UNION if p in PISKAOT]) == 104
assert all(1 <= v <= 32 for _, _, (_, v) in CIT_HE + CIT_EN)   # no cited verse beyond the chapter's length (chapter 6's slip form absent)
assert [(p, r) for p in range(1, 358) for r in range(1, len(sif[p - 1]) + 1) if re.search(r'\((?:Ibid|ibid)\.? ?11:\d+\)', E(p, r))] == []
assert {p: heads[p] for p, _ in OUTSIDE + EXCLUDED} == {35: (6, 8), 36: (6, 9), 80: (12, 29), 306: (32, 1), 234: (22, 12)} and all(heads[p] == HEADS_ON[p] for p, _ in OUTSIDE + EXCLUDED), {p: heads[p] for p, _ in OUTSIDE + EXCLUDED}
assert all(has_points(Hb(p, r)) for p, r in OUTSIDE) and all(has_points(Hb(p, r)) for p in PISKAOT for r in range(1, SPINE_ROWS[p] + 1))
# THE EXCLUDED SLIP: 234:6 (on 22:12, the tassels' garment) — the English cites '(Dt.11:12)' for "of your garment"; 11:12 is the land the LORD seeks; the Hebrew cites nothing
assert he_cites(Hb(234, 6)) == [] and '(Dt.11:12)' in E(234, 6) and 'כסותך' in HB0(234, 6) and '(22:12)' in E(234, 6) and 'garment' in E(234, 6)
# THE HEBREW'S 'IBID.' at 306:4 and 306:9 — "(שם יא יז)" after "(דברים כח יב)" / "(דברים יז ז)": the book-name regex misses them; the English's (Dt.11:17) catches them (chapter 6's 355:27 form)
assert '(שם יא יז)' in Hb(306, 4) and '(דברים כח יב)' in Hb(306, 4) and '(Dt.11:17)' in E(306, 4) and '(שם יא יז)' in Hb(306, 9) and '(דברים יז ז)' in Hb(306, 9) and E(306, 9).count('(Dt.11:17)') == 2
assert '(דברים יא יז)' in Hb(306, 6) and '(דברים כח יב)' in Hb(306, 6) and 'ואין עצירה אלא לשון הדחק' in HB0(306, 6) and '(בראשית כ יח)' in Hb(306, 6) and 'ואין פתיחה אלא לשון הרוחה' in HB0(306, 6)
# THE TWO FILES DIVIDE PISKA 37 DIFFERENTLY: the English's row 3 carries a paragraph of piska 39 (the mountain's thin soil, on 11:11 — 39:6's opening), and its row 4 begins with the Hebrew's row 3 (the two banquet halls); the English's 39:6 carries 39:6-10's paragraphs whole and 39:7-10 repeat them (chapter 8's lesson, a third time)
assert HB0(37, 3).startswith('ואם תאמר: לא מי שבנה את זו') and E(37, 3).startswith('6. Insofar as') and '(Dt.11:11)' in E(37, 3) and 'Zech.10:1' in E(37, 3) and E(37, 4).startswith('3. An analogy') and E(39, 6).startswith(E(37, 3).strip()[:120])
assert E(39, 7).strip()[:80] in E(39, 6) and E(39, 8).strip()[:60] in E(39, 6) and E(39, 10).strip()[:60] in E(39, 6) and HB0(39, 7).startswith('או לפי שארץ ישראל מכפלת בהרים')
# THE OUTSIDE ROWS' CONTENT (the consonants of the shelf's bytes)
assert [c for c in he_cites(Hb(35, 4)) if c[0] == 'דברים'] == [] and he_cites(Hb(35, 4)) == [('שמות', 13, 9)] and '(Dt.11:18)' in E(35, 4) and '(Dt.6:8)' in E(35, 4) and 'הרי ארבע טוטפות אמורות' in HB0(35, 4) and 'טוטפת טוטפות' in HB0(35, 4) and 'כיס אחד של ארבע טוטפות' in HB0(35, 4) and 'four inscriptions' in E(35, 4)   # THE FRONTLETS' COUNT — the shelf reads the spellings to four
assert '(דברים יא כ)' in Hb(36, 3) and 'רבוי אחר רבוי' in HB0(36, 3) and 'למעט' in HB0(36, 3) and 'דברי רבי ישמעאל' in HB0(36, 3) and '(Dt.11:20)' in E(36, 3) and 'single doorpost' in E(36, 3)   # "doorposts" twice plural — an inclusion after an inclusion restricts: ONE doorpost
assert '(דברים יא לא)' in Hb(80, 4) and 'ישיבת ארץ ישראל שקולה כנגד כל המצוות שבתורה' in HB0(80, 4) and 'רבי יהודה בן בתירה' in HB0(80, 4) and 'וקרעו בגדיהם' in HB0(80, 4) and '(Dt.11:31-32)' in E(80, 4) and 'outweighs all the commandments' in E(80, 4)
assert '(דברים יא לא)' in Hb(80, 5) and 'לנציבים' in HB0(80, 5) and 'רבי אלעזר בן שמוע ורבי יוחנן הסנדלר' in HB0(80, 5) and 'חזרו ובאו להם לארץ ישראל' in HB0(80, 5) and '(Dt.11:31-32)' in E(80, 5)
assert 'שני אפוטרופים' in HB0(306, 4) and 'ועצר את השמים ולא יהיה מטר והאדמה לא תתן את יבולה' in HB0(306, 4) and 'רבי יהודה אומר' in HB0(306, 4)
assert 'רבי בניה' in HB0(306, 9) and 'יד העדים תהיה בו בראשונה' in HB0(306, 9) and 'ואבדתם מהרה' in HB0(306, 9) and '(הושע ב כג)' in Hb(306, 9)
NOCITE = [(p, r) for p in PISKAOT for r in range(1, SPINE_ROWS[p] + 1) if not he_cites(Hb(p, r)) and not re.findall(r'\([A-Z][a-z]+\.? ?\d+:\d+', E(p, r))]
assert NOCITE == [(37, 8), (37, 13), (37, 15), (38, 2), (38, 3), (38, 4), (41, 11), (43, 12), (43, 20), (43, 21), (51, 3)], NOCITE
# THE PRIOR READS — the strict row form over every ledger: TWO of the seven outside rows read before (35:4, 36:3 at sitting 4); FORTY-ONE spine rows read before (twenty-three at the Deuteronomy sittings, eighteen at Genesis sittings) — every one REREAD WHOLE here; no Onkelos row of chapter 11 anywhere
TRI = f'{ROOT}/logic/oral_triage'
LED = {f: open(f'{TRI}/{f}', encoding='utf-8').read() for f in os.listdir(TRI) if f.endswith('.md') and os.path.isfile(f'{TRI}/{f}') and f'{TRI}/{f}' != OUT}
PRIOR = sorted({(f, int(a), int(b)) for f, t in LED.items() for a, b in re.findall(r'Sifrei Devarim (\d+):(\d+)', t)})
assert [(f, p, r) for f, p, r in PRIOR if (p, r) in OUTSIDE + EXCLUDED] == [('deu_06_vaetchanan_2026-09-17.md', 35, 4), ('deu_06_vaetchanan_2026-09-17.md', 36, 3)] and len(PRIOR) == 323, (len(PRIOR), [(f, p, r) for f, p, r in PRIOR if (p, r) in OUTSIDE])
SPINE_PRIOR = [(f, p, r) for f, p, r in PRIOR if p in PISKAOT]
assert len(SPINE_PRIOR) == 41 and sum(1 for f, _, _ in SPINE_PRIOR if f.startswith('deu_')) == 23 and sum(1 for f, _, _ in SPINE_PRIOR if f.startswith('gen_')) == 18 and ('deu_08_ekev_2026-09-18.md', 39, 4) in SPINE_PRIOR and ('deu_07_vaetchanan_ekev_2026-09-17.md', 37, 1) in SPINE_PRIOR and ('gen_27_the_call_2026-08-25.md', 56, 3) in SPINE_PRIOR and ('gen_12_cain_abel_2026-08-26.md', 45, 1) in SPINE_PRIOR, len(SPINE_PRIOR)
assert sorted(f for f, t in LED.items() if re.search(r'^- Onkelos Deut 11:', t, re.M)) == []
NAMING = sorted(f for f, t in LED.items() if re.search(r'Deut(?:eronomy)? 11:\d+', t))
assert NAMING == ['deu_01_03_devarim_exam_2026-09-15.md', 'deu_06_vaetchanan_2026-09-17.md', 'deu_07_vaetchanan_ekev_2026-09-17.md', 'exodus_block_matza_2026-09-04.md', 'gen_27_the_call_2026-08-25.md', 'gen_29_separation_promise_2026-08-25.md', 'num_16_korach_2026-09-10.md', 'num_26_second_census_2026-09-11.md', 'num_26_second_census_exam_2026-09-11.md', 'num_33_journeys_2026-09-12.md', 'num_34_borders_2026-09-12.md', 'num_35_refuge_cities_2026-09-13.md', 'num_36_heiresses_2026-09-09.md'], NAMING
assert 'Deut 11:18' in LED['deu_06_vaetchanan_2026-09-17.md'] and 'Deut 11:18' in LED['exodus_block_matza_2026-09-04.md'] and 'Deuteronomy 11:6' in LED['num_16_korach_2026-09-10.md'] and 'Deuteronomy 11:24' in LED['num_34_borders_2026-09-12.md'] and 'Deuteronomy 11:31' in LED['num_33_journeys_2026-09-12.md']
# THE KIN'S READS: Dathan and Abiram at the Korah sitting (Onkelos Numbers 16 whole), the Shema's first paragraph at sitting 4, the good land at sitting 6, the dread and the borders at the Exodus 23 sitting, the fold's blessing and curse at Leviticus 26; THE SEA AND THE FRONTLETS through the Mekhilta at the Exodus block (no ledger holds an Onkelos row of Exodus 13-15)
assert kinrows('num_16_korach_2026-09-10.md', r'Num 16:(?:[1-9]|[12]\d|3[0-5])\b') == 35 and kinrows('deu_06_vaetchanan_2026-09-17.md', r'Deut 6:[4-9]\b') == 6 and kinrows('deu_08_ekev_2026-09-18.md', r'Deut 8:(?:[7-9]|10)\b') == 4 and kinrows('exo_23_escort_land_2026-09-01.md', r'Exod 23:(?:2[7-9]|3[01])\b') == 3 and kinrows('lev_26_blessings_curses_2026-09-05.md', r'Lev 26:(?:[3-5]|19|20)\b') == 5
assert sorted(f for f, t in LED.items() if re.search(r'^- Onkelos Exod 1[345]:', t, re.M)) == [] and sum(len(re.findall(r'Mekhilta[^\n]{0,40}(?:14|23):\d+', t)) for t in LED.values()) == 38 and sorted(f for f in LED if f.startswith('exo_1')) == []
assert [(f, len(re.findall(r'Gen(?:esis)? 15:18', t))) for f, t in sorted(LED.items()) if re.search(r'Gen(?:esis)? 15:18', t)] == [('deu_01_03_devarim_2026-09-15.md', 2), ('num_34_borders_2026-09-12.md', 3), ('talmud_triage_gen_2026-09-01.md', 1)]
ONK_LEN = {c: len(onk[c - 1]) for c in (3, 4, 5, 6, 7, 8, 9, 10, 11)}
assert len(onk) == 34 and len(onk_he) == 34 and ONK_LEN == {3: 29, 4: 49, 5: 30, 6: 25, 7: 26, 8: 20, 9: 29, 10: 22, 11: 32} and sum(len(c) for c in onk_he) == 956
shelf_deut = sorted(d for d in os.listdir(f'{ROOT}/Data/sefaria_export') if re.search(r'Deuteronomy|Devarim', d))
outside = [d for d in shelf_deut if d not in ('Sifrei_Devarim', 'Onkelos_Deuteronomy')]
assert len(shelf_deut) == 28 and len(outside) == 26, len(outside)
# ---- THE DRAFT'S SPAN, COMPUTED ----
VC = dict(db.execute("SELECT chapter, COUNT(*) FROM verses WHERE book='Deut' GROUP BY chapter").fetchall())
assert VC[5] == 33 and VC[10] == 22 and VC[11] == 32 and VC[12] == 31 and sum(VC.values()) == 959 and len(VC) == 34
assert [(c, len(onk_he[c - 1]), VC[c]) for c in range(1, 35) if len(onk_he[c - 1]) != VC[c]] == [(5, 30, 33)]
# THE ALIGNMENT RECOMPUTED (ch11_dump0's A0): the export's thirty-two rows against the DB's thirty-two verses over token and negation counts — the identity, cost 18
by11 = {v: [plain(he) for he, in db.execute("SELECT w.he FROM words w JOIN verses v ON w.verse_id=v.id WHERE v.book='Deut' AND v.chapter=11 AND v.verse=? ORDER BY w.idx", (v,))] for v in range(1, 33)}
NEG = ('לא', 'ולא')
D_ = [(len(by11[v]), sum(1 for x in by11[v] if x in NEG)) for v in range(1, 33)]
E_ = [(len(plain(clean(r)).split()), sum(1 for x in plain(clean(r)).split() if x.strip('.:') in NEG)) for r in onk_he[10]]
def _cost(e, ds): return abs(e[0] - sum(d[0] for d in ds)) + 3 * abs(e[1] - sum(d[1] for d in ds))
INF = 10 ** 9; best = {(0, 0): (0, None)}
for i in range(1, 33):
    for j in range(i, 33):
        cands = [(best[(i - 1, k)][0] + _cost(E_[i - 1], D_[k:j]), k) for k in range(i - 1, j) if (i - 1, k) in best and j - k <= 4]
        best[(i, j)] = min(cands) if cands else (INF, None)
i, j, ALIGN = 32, 32, {}
while i > 0:
    k = best[(i, j)][1]; ALIGN[i] = list(range(k + 1, j + 1)); i, j = i - 1, k
assert ALIGN == EXP2DB and best[(32, 32)][0] == 18 and Counter(ds[0] - e for e, ds in EXP2DB.items()) == Counter({0: 32}) and len(onk_he[10]) == 32 == VC[11], (best[(32, 32)][0], ALIGN)
def unit_text(uid): return open(f'{ROOT}/logic/units/{uid}.yaml', encoding='utf-8').read()
def steps(uid): return sorted({(int(a), int(b)) for a, b in re.findall(r'STEP_Dt_(\d+)_(\d+)', unit_text(uid))})
FIRST = not os.path.exists(OUT)
for uid, (c, lo, hi) in SPANS.items():
    t = unit_text(uid)
    assert steps(uid) == [(c, v) for v in range(lo, hi + 1)] and re.search(rf'refs: "?{c}:{lo}-{hi}"?', t) and '\nbinary_trees:' in t, uid
    if FIRST: assert 'status: draft' in t and 'operators:' not in t and '- step: E' not in t, uid
    assert t.count(f'  - id: STEP_Dt_{c}_{lo}\n') == 1 and t.count(f'  - id: STEP_Dt_{c}_{hi}\n') == 1, uid
UT11 = unit_text('deu_11_bless_curse_set')
assert UT11.count('\n    comment:') + UT11.count('\n      comment:') == 36 and UT11.count('\n  - id: S') == 39   # typed from ch11_dump0's G print (the draft's comment lines and scenarios)
assert 'deu_10_second_tablets' in UT11 and 'status: frozen' in unit_text('deu_10_second_tablets') and 'title_en: "Love and keep; rain; bless/curse set on mountains (11:1–32)"' in UT11
assert sorted(f for f in os.listdir(TRI) if f.startswith('deu_') and f != os.path.basename(OUT)) == ['deu_01_03_devarim_2026-09-15.md', 'deu_01_03_devarim_exam_2026-09-15.md', 'deu_04_vaetchanan_2026-09-16.md', 'deu_04_vaetchanan_exam_2026-09-16.md', 'deu_05_vaetchanan_2026-09-16.md', 'deu_05_vaetchanan_exam_2026-09-16.md', 'deu_06_vaetchanan_2026-09-17.md', 'deu_06_vaetchanan_exam_2026-09-17.md', 'deu_07_vaetchanan_ekev_2026-09-17.md', 'deu_07_vaetchanan_ekev_exam_2026-09-18.md', 'deu_08_ekev_2026-09-18.md', 'deu_08_ekev_exam_2026-09-19.md', 'deu_09_ekev_2026-09-19.md', 'deu_09_ekev_exam_2026-09-19.md', 'deu_10_ekev_2026-09-19.md', 'deu_10_ekev_exam_2026-09-20.md']
ALLTXT = ''.join(open(f'{ROOT}/logic/units/{f}', encoding='utf-8').read() for f in os.listdir(f'{ROOT}/logic/units') if f.endswith('.yaml') and f[:-5] not in UIDS) + ''.join(open(f'{ROOT}/logic/oral_audit/manifests/{f}', encoding='utf-8').read() for f in os.listdir(f'{ROOT}/logic/oral_audit/manifests') if f.endswith('.json'))
assert all(f'"{p}-' not in ALLTXT and f'[claim {p}-' not in ALLTXT for p in PREFIX.values())
SPAN = [(11, v) for v in range(1, VC[11] + 1)]
NV = 32
assert len(SPAN) == NV
# ---- THE INK, computed from the Tanakh DB and the snapshot store ----
# THE STORE = THE DB at EVERY verse — no written/read pair in the chapter (wtype None at all 508 tokens); 1,992 letters; the seven "?" glosses the store's "I" (אנכי at 8, 13, 22, 26, 27, 28, 32)
assert STORE_MISMATCH == [] and sum(len(SG[(11, v)]) for v in range(1, 33)) == 508 == sum(len(W11(v)) for v in range(1, 33)) and sum(len(x) for v in range(1, 33) for x in W11(v)) == 1992
assert [(v, x, m, wt) for v in range(1, 33) for (x, m), wt in zip(by[('Deut', 11, v)], byw[('Deut', 11, v)]) if wt] == [] and Counter(wt for v in range(1, 33) for wt in byw[('Deut', 11, v)]) == Counter({None: 508})
assert [(v, i, hp, g) for (c, v), L in sorted(SG.items()) for i, hp, g in L if '?' in g] == [(8, 5, 'אנכי', '?'), (13, 7, 'אנכי', '?'), (22, 9, 'אנכי', '?'), (26, 1, 'אנכי', '?'), (27, 9, 'אנכי', '?'), (28, 12, 'אנכי', '?'), (32, 8, 'אנכי', '?')]
assert {v: len(W11(v)) for v in range(1, 33)} == {1: 11, 2: 23, 3: 13, 4: 21, 5: 9, 6: 26, 7: 10, 8: 19, 9: 16, 10: 22, 11: 13, 12: 16, 13: 20, 14: 10, 15: 6, 16: 11, 17: 24, 18: 17, 19: 12, 20: 5, 21: 17, 22: 22, 23: 12, 24: 21, 25: 19, 26: 7, 27: 13, 28: 23, 29: 23, 30: 17, 31: 18, 32: 12}
# THE ENGINE'S PARSER on every verse — MEASURED before the compile is asked: NO NUMBER VERSE IN THE CHAPTER (chapter 10 had five); "swore" (11:9, 11:21) the seven-stem homograph no number; "be satisfied" starred at 11:15 (chapter 8's lesson); the kin's numbers — Korah's two hundred and fifty (Numbers 16:2, 17, 35; 26:10), the plague's 14,700 (17:14), the six hundred chariots (Exodus 14:7), the six hundred thousand (12:37), the creed's [1] (6:4), the seven nations [7] (7:1)
with contextlib.redirect_stdout(io.StringIO()):
    import cold_run_sequence as CS
PARSE = {v: (CS.ink_numbers(CS.verse_words('Deut', 11, v)), CS.ink_ordinals(CS.verse_words('Deut', 11, v)), [t for t in CS.verse_words('Deut', 11, v) if t[-1] in '#~^%@|*']) for v in range(1, 33)}
assert all(n == [] and o == [] for n, o, _ in PARSE.values()) and {v: m for v, (_, _, m) in PARSE.items() if m} == {15: ['ושבעת*']}, {v: p for v, p in PARSE.items() if any(p)}
assert [s for s, x, _ in LEMT('7650') if s.startswith('Deut 11:')] == ['Deut 11:9', 'Deut 11:21'] and 'נשבע' in W11(9) and 'נשבע' in W11(21)
KINNUM = {k: CS.ink_numbers(CS.verse_words(*k)) for k in [('Num', 16, 2), ('Num', 16, 17), ('Num', 16, 35), ('Num', 17, 14), ('Num', 26, 10), ('Exod', 14, 7), ('Exod', 12, 37), ('Deut', 6, 4), ('Deut', 7, 1), ('Num', 26, 9), ('Exod', 13, 16), ('Deut', 6, 8), ('Gen', 15, 18), ('Josh', 1, 3), ('Josh', 1, 4), ('Deut', 27, 12), ('Deut', 27, 13), ('Gen', 12, 6), ('Josh', 8, 33)]}
assert KINNUM == {('Num', 16, 2): [250], ('Num', 16, 17): [250], ('Num', 16, 35): [250], ('Num', 17, 14): [14700], ('Num', 26, 10): [250], ('Exod', 14, 7): [600], ('Exod', 12, 37): [600000], ('Deut', 6, 4): [1], ('Deut', 7, 1): [7], ('Num', 26, 9): [], ('Exod', 13, 16): [], ('Deut', 6, 8): [], ('Gen', 15, 18): [], ('Josh', 1, 3): [], ('Josh', 1, 4): [], ('Deut', 27, 12): [], ('Deut', 27, 13): [], ('Gen', 12, 6): [], ('Josh', 8, 33): []}, KINNUM
# THE REGISTER, computed on the morphology: the second person PLURAL in nineteen verses, SINGULAR in five (1, 12, 15, 20, 29), BOTH in five (8, 10, 14, 19, 26 — "See" the singular imperative over "before you" plural), NEITHER in three (3, 6, 30); GOD'S FIRST PERSON INSIDE MOSES' SPEECH — "My commandments" (13), "and I will give" (14, 15), "My words" (18) — beside Moses' seven "I"; the imperatives TWO (16 "take heed", 26 "See"); the infinitive absolutes TWO (13 "hearken diligently", 22 "keep diligently"); THE CONSECUTIVE PERFECTS THIRTY-TWO in seventeen verses — the law's form; the wayyiqtol TWO (4 "and He destroyed them", 6 "and swallowed them") — the retelling's two narrative verbs; NO prohibition on Israel (every "not" a condition or a consequence); no "saying", no divine frame
NUM = {v: (sum(1 for _, m in wm('Deut', 11, v) if m and '2mp' in m), sum(1 for _, m in wm('Deut', 11, v) if m and '2ms' in m)) for v in range(1, 33)}
assert NUM == {1: (0, 3), 2: (3, 0), 3: (0, 0), 4: (1, 0), 5: (2, 0), 6: (0, 0), 7: (1, 0), 8: (5, 1), 9: (2, 0), 10: (1, 5), 11: (1, 0), 12: (0, 2), 13: (5, 0), 14: (1, 4), 15: (0, 4), 16: (6, 0), 17: (3, 0), 18: (6, 0), 19: (2, 5), 20: (0, 3), 21: (3, 0), 22: (3, 0), 23: (3, 0), 24: (3, 0), 25: (6, 0), 26: (1, 1), 27: (3, 0), 28: (5, 0), 29: (0, 4), 30: (0, 0), 31: (5, 0), 32: (2, 0)}
assert [v for v, (p, s) in NUM.items() if s and not p] == [1, 12, 15, 20, 29] and [v for v, (p, s) in NUM.items() if p and s] == [8, 10, 14, 19, 26] and [v for v, (p, s) in NUM.items() if not p and not s] == [3, 6, 30] and len([v for v, (p, s) in NUM.items() if p and not s]) == 19
assert {v: [(x, m) for x, m in wm('Deut', 11, v) if m and '1cs' in m] for v in range(1, 33) if any(m and '1cs' in m for _, m in wm('Deut', 11, v))} == {8: [('אנכי', 'HPp1cs')], 13: [('מצותי', 'HNcfpc/Sp1cs'), ('אנכי', 'HPp1cs')], 14: [('ונתתי', 'HC/Vqq1cs')], 15: [('ונתתי', 'HC/Vqq1cs')], 18: [('דברי', 'HNcmpc/Sp1cs')], 22: [('אנכי', 'HPp1cs')], 26: [('אנכי', 'HPp1cs')], 27: [('אנכי', 'HPp1cs')], 28: [('אנכי', 'HPp1cs')], 32: [('אנכי', 'HPp1cs')]}
assert {v: [(x, m) for x, m in wm('Deut', 11, v) if m and re.match(r'^HV.?.?v', m)] for v in range(1, 33) if any(m and re.match(r'^HV.?.?v', m) for _, m in wm('Deut', 11, v))} == {16: [('השמרו', 'HVNv2mp')], 26: [('ראה', 'HVqv2ms')]}
assert {v: [(x, m) for x, m in wm('Deut', 11, v) if m and re.match(r'^H(?:C/)?V.a$', m)] for v in range(1, 33) if any(m and re.match(r'^H(?:C/)?V.a$', m) for _, m in wm('Deut', 11, v))} == {13: [('שמע', 'HVqa')], 22: [('שמר', 'HVqa')]}
WEQ = {v: [x for x, m in wm('Deut', 11, v) if m and re.search(r'^HC/V.q', m)] for v in range(1, 33) if any(m and re.search(r'^HC/V.q', m) for _, m in wm('Deut', 11, v))}
assert WEQ == {1: ['ואהבת', 'ושמרת'], 2: ['וידעתם'], 8: ['ושמרתם', 'ובאתם', 'וירשתם'], 10: ['והשקית'], 13: ['והיה'], 14: ['ונתתי', 'ואספת'], 15: ['ונתתי', 'ואכלת', 'ושבעת'], 16: ['וסרתם', 'ועבדתם', 'והשתחויתם'], 17: ['וחרה', 'ועצר', 'ואבדתם'], 18: ['ושמתם', 'וקשרתם', 'והיו'], 19: ['ולמדתם'], 20: ['וכתבתם'], 23: ['והוריש', 'וירשתם'], 28: ['וסרתם'], 29: ['והיה', 'ונתתה'], 31: ['וירשתם', 'וישבתם'], 32: ['ושמרתם']} and sum(len(x) for x in WEQ.values()) == 32 and len(WEQ) == 17
assert {v: [x for x, m in wm('Deut', 11, v) if m and re.search(r'^HC/V.w', m)] for v in range(1, 33) if any(m and re.search(r'^HC/V.w', m) for _, m in wm('Deut', 11, v))} == {4: ['ויאבדם'], 6: ['ותבלעם']}
PTC = {v: [(x, m) for x, m in wm('Deut', 11, v) if m and re.search(r'^H(?:C/|R/|Td/|C/R/)?V.r', m)] for v in range(1, 33) if any(m and re.search(r'^H(?:C/|R/|Td/|C/R/)?V.r', m) for _, m in wm('Deut', 11, v))}
assert sum(len(x) for x in PTC.values()) == 18 and len(PTC) == 16 and PTC[12] == [('דרש', 'HVqrmsa')] and PTC[7] == [('הראת', 'HTd/Vqrfpa')] and PTC[30] == [('הישב', 'HTd/Vqrmsa')] and PTC[9] == [('זבת', 'HVqrfsc')]
assert {v: [(x, m) for x, m in wm('Deut', 11, v) if m and re.search(r'^H(?:Ti/)?V.i2', m)] for v in range(1, 33) if any(m and re.search(r'^H(?:Ti/)?V.i2', m) for _, m in wm('Deut', 11, v))} == {8: [('תחזקו', 'HVqi2mp')], 9: [('תאריכו', 'HVhi2mp')], 10: [('תזרע', 'HVqi2ms')], 13: [('תשמעו', 'HVqi2mp')], 22: [('תשמרון', 'HVqi2mp/Sn')], 25: [('תדרכו', 'HVqi2mp')], 27: [('תשמעו', 'HVqi2mp')], 28: [('תשמעו', 'HVqi2mp')]}
assert {v: [x for x in W11(v) if x in NEG] for v in range(1, 33) if any(x in NEG for x in W11(v))} == {2: ['לא', 'לא', 'לא'], 10: ['לא'], 17: ['ולא', 'לא'], 25: ['לא'], 28: ['לא', 'לא']}   # no "not" before a second-person imperfect: no prohibition on Israel in the chapter
assert {f'11:{v}': [x for x in W11(v) if x in ('כי', 'אם', 'ואם', 'או', 'פן')] for v in range(1, 33) if any(x in ('כי', 'אם', 'ואם', 'או', 'פן') for x in W11(v))} == {'11:2': ['כי'], '11:7': ['כי'], '11:10': ['כי'], '11:13': ['אם'], '11:16': ['פן'], '11:22': ['כי', 'אם'], '11:28': ['אם'], '11:29': ['כי'], '11:31': ['כי']}
assert [v for v in range(1, 33) if 'לאמר' in W11(v)] == [] and [v for v in range(1, 33) if any(W11(v)[i] in ('ויאמר', 'וידבר') and W11(v)[i + 1] == 'יהוה' for i in range(len(W11(v)) - 1))] == []
assert {v: [x for x in W11(v) if x in ('למען', 'ולמען')] for v in range(1, 33) if any(x in ('למען', 'ולמען') for x in W11(v))} == {8: ['למען'], 9: ['ולמען'], 21: ['למען']} and len(U('למען', 'ולמען', books=('Deut',))) == 43
assert sum(1 for v in range(1, 33) for x in W11(v) if x == 'יהוה') == 18 and [v for v in range(1, 33) if any(W11(v)[i:i + 2] == ['יהוה', 'אלהיך'] for i in range(len(W11(v)) - 1))] == [1, 12, 29] and [v for v in range(1, 33) if any(W11(v)[i:i + 2] == ['יהוה', 'אלהיכם'] for i in range(len(W11(v)) - 1))] == [2, 13, 22, 25, 27, 28, 31]
assert [v for v in range(1, 33) for x in W11(v) if x == 'ישראל'] == [6] and [v for v in range(1, 33) for x in W11(v) if x in ('מצרים', 'מצרימה')] == [3, 3, 4, 10] and [v for v in range(1, 33) for x in W11(v) if x == 'משה'] == [] and sum(1 for v in range(1, 33) for x in W11(v) if x == 'היום') == 8
assert Counter(int(s.split()[1].split(':')[0]) for s in U('משה', 'למשה', 'ומשה', books=('Deut',))) == Counter({31: 10, 34: 6, 4: 4, 1: 3, 27: 3, 32: 3, 33: 2, 15: 1, 28: 1, 29: 1, 5: 1})   # MOSES UNNAMED FROM CHAPTER 6 TO 14 (chapter 10's find extended: no "Moses" token in 6-14)
# THE KIN DIFFED (computed token by token, the shared tokens counted in order — the measure's A print)
import difflib
def SH(a, b_): return sum(s for _, _, s in difflib.SequenceMatcher(a=words(*a), b=words(*b_)).get_matching_blocks())
D11 = lambda v: ('Deut', 11, v)
assert SH(D11(1), ('Deut', 30, 16)) == 5 and SH(D11(1), ('Deut', 6, 5)) == 4 and SH(D11(1), ('Gen', 26, 5)) == 0 and SH(D11(1), ('1Kgs', 2, 3)) == 5
assert SH(D11(2), ('Deut', 31, 13)) == 7 and SH(D11(2), ('Deut', 8, 5)) == 3 and SH(D11(3), ('Deut', 29, 1)) == 6 and SH(D11(3), ('Deut', 34, 11)) == 5
assert SH(D11(4), ('Deut', 34, 6)) == 4 and SH(D11(4), ('Josh', 24, 6)) == 3 and max((SH(D11(4), ('Exod', 14, v)), v) for v in range(1, 32)) == (3, 31) and max(SH(D11(4), ('Exod', 15, v)) for v in range(1, 22)) == 2   # THE SEA TOLD IN NEW WORDS: no verse of Exodus 14-15 shares more than three tokens (14:31's 'which the LORD did against Egypt' the three)
assert SH(D11(5), ('Deut', 9, 7)) == 6 and SH(D11(5), ('Deut', 1, 31)) == 5
assert SH(D11(6), ('Num', 16, 32)) == 8 and SH(D11(6), ('Num', 16, 30)) == 5 and SH(D11(6), ('Gen', 7, 4)) == 5 and SH(D11(6), ('Gen', 7, 23)) == 4 and SH(D11(6), ('Num', 26, 10)) == 4 and SH(D11(6), ('Ps', 106, 17)) == 0
assert SH(D11(7), ('Judg', 2, 7)) == 6 and SH(D11(7), ('Josh', 24, 31)) == 6 and SH(D11(7), ('Deut', 3, 21)) == 5 and SH(D11(7), ('Deut', 4, 3)) == 5   # JOSHUA'S AND JUDGES' EPILOGUE read the elders' generation from this verse
assert SH(D11(8), ('Deut', 8, 1)) == 12 and SH(D11(8), ('Deut', 4, 1)) == 8 and SH(D11(9), ('Deut', 11, 21)) == 8 and SH(D11(9), ('Josh', 5, 6)) == 8 and SH(D11(9), ('Num', 16, 13)) == 3 and SH(D11(9), ('Num', 16, 14)) == 4
assert SH(D11(10), ('Deut', 11, 29)) == 8 and SH(D11(10), ('Deut', 7, 1)) == 7 and SH(D11(10), ('Gen', 13, 10)) == 3 and SH(D11(11), ('Deut', 8, 7)) == 2 and SH(D11(12), ('Ps', 34, 16)) == 2 and SH(D11(12), ('Zech', 4, 10)) == 2
assert SH(D11(13), ('Josh', 22, 5)) == 11 and SH(D11(13), ('Deut', 11, 22)) == 10 and SH(D11(13), ('Deut', 13, 4)) == 9 and SH(D11(13), ('Deut', 28, 1)) == 6 and SH(D11(13), ('Deut', 6, 5)) == 4
assert SH(D11(14), ('Deut', 7, 13)) == 3 and SH(D11(14), ('Lev', 26, 4)) == 1 and SH(D11(15), ('Deut', 6, 11)) == 2 and SH(D11(15), ('Deut', 8, 10)) == 2
assert SH(D11(16), ('Josh', 23, 16)) == 5 and SH(D11(16), ('1Kgs', 9, 6)) == 5 and SH(D11(17), ('Josh', 23, 16)) == 11 and SH(D11(17), ('Deut', 4, 26)) == 6 and SH(D11(17), ('Lev', 26, 20)) == 5 and SH(D11(17), ('2Chr', 6, 26)) == 5   # JOSHUA'S FAREWELL (23:16) reads 11:16-17 back — five and eleven tokens
assert SH(D11(18), ('Deut', 6, 8)) == 5 and SH(D11(18), ('Exod', 13, 9)) == 3 and SH(D11(18), ('Exod', 13, 16)) == 3 and SH(D11(19), ('Deut', 6, 7)) == 7 and SH(D11(20), ('Deut', 6, 9)) == 4 and SH(D11(21), ('Deut', 11, 9)) == 8 and SH(D11(21), ('Deut', 30, 20)) == 7
assert SH(D11(22), ('Josh', 22, 5)) == 12 and SH(D11(22), ('Deut', 19, 9)) == 10 and SH(D11(22), ('Deut', 11, 13)) == 10 and SH(D11(23), ('Deut', 31, 3)) == 5 and SH(D11(23), ('Josh', 23, 13)) == 5
assert SH(D11(24), ('Josh', 1, 3)) == 7 and SH(D11(24), ('Josh', 1, 4)) == 7 and SH(D11(24), ('Deut', 1, 7)) == 5 and SH(D11(24), ('Gen', 15, 18)) == 3 and SH(D11(24), ('Exod', 23, 31)) == 1   # JOSHUA 1:3-4 reads the borders from this verse, seven and seven
assert SH(D11(25), ('Josh', 1, 5)) == 5 and SH(D11(25), ('Deut', 7, 24)) == 3 and SH(D11(25), ('Deut', 2, 25)) == 4 and SH(D11(26), ('Deut', 4, 8)) == 4 and SH(D11(26), ('Deut', 11, 32)) == 4 and SH(D11(26), ('Deut', 30, 15)) == 2
assert SH(D11(27), ('Deut', 11, 28)) == 10 and SH(D11(28), ('Deut', 28, 14)) == 9 and SH(D11(28), ('Deut', 13, 3)) == 7 and SH(D11(29), ('Deut', 7, 1)) == 11 and SH(D11(29), ('Deut', 6, 10)) == 8 and SH(D11(29), ('Josh', 8, 33)) == 6
assert SH(D11(30), ('Deut', 1, 1)) == 4 and SH(D11(30), ('Gen', 12, 6)) == 1 and SH(D11(31), ('Josh', 1, 11)) == 13 and SH(D11(31), ('Deut', 12, 10)) == 7 and SH(D11(32), ('Deut', 5, 1)) == 7 and SH(D11(32), ('Deut', 7, 11)) == 7   # JOSHUA 1:11 repeats 11:31 — thirteen of eighteen tokens
# THE PHRASE CENSUSES (the B print) — 11:1-7 THE DISCIPLINE SEEN
assert P('ואהבת', 'את', 'יהוה', 'אלהיך') == ['Deut 11:1', 'Deut 6:5'] and U('ואהבת', books=T) == ['Deut 11:1', 'Deut 6:5', 'Lev 19:18', 'Lev 19:34'] and U('לאהבה', 'ולאהבה', books=('Deut',)) == ['Deut 10:12', 'Deut 10:15', 'Deut 11:13', 'Deut 11:22', 'Deut 19:9', 'Deut 30:16', 'Deut 30:20', 'Deut 30:6'] and len(LEMT('157', books=('Deut',))) == 22
assert P('ושמרת', 'משמרתו') == ['Deut 11:1'] and [(s, x) for s, x, _ in LEMT('4931', books=T) if x == 'משמרתו'] == [('Deut 11:1', 'משמרתו'), ('Num 3:7', 'משמרתו')] and P('משמרתי', 'מצותי', 'חקותי', 'ותורתי') == ['Gen 26:5'] and P('וחקתיו', 'ומשפטיו', 'ומצותיו') == ['Deut 11:1'] and len(P('כל', 'הימים', books=('Deut',))) == 12
assert [(s, x) for s, x, _ in LEMT('4148', books=T)] == [('Deut 11:2', 'מוסר')] and len(LEMT('4148')) == 50 and P('מוסר', 'יהוה') == ['Deut 11:2', 'Prov 3:11'] and [(s, x) for s, x, _ in LEMT('3256', books=('Deut',))] == [('Deut 4:36', 'ליסרך'), ('Deut 8:5', 'ייסר'), ('Deut 8:5', 'מיסרך'), ('Deut 21:18', 'ויסרו'), ('Deut 22:18', 'ויסרו')]   # "DISCIPLINE" THE NOUN — the Torah's ONE seat; "the discipline of the LORD" here and Proverbs 3:11
assert P('ידו', 'החזקה', 'וזרעו', 'הנטויה') == ['Deut 11:2'] and P('ביד', 'חזקה', 'ובזרע', 'נטויה') == ['Deut 26:8', 'Deut 5:15'] and [s for s in U('גדלו') if s.startswith('Deut')] == ['Deut 11:2', 'Deut 5:24'] and 'Deut 3:24' in U('גדלך') and P('אשר', 'לא', 'ידעו', 'ואשר', 'לא', 'ראו') == ['Deut 11:2']
assert P('אתתיו', 'ואת', 'מעשיו') == ['Deut 11:3'] and P('בתוך', 'מצרים') == ['Deut 11:3', 'Exod 11:4'] and P('לפרעה', 'מלך', 'מצרים', 'ולכל', 'ארצו') == ['Deut 11:3'] and P('ולכל', 'ארצו') == ['Deut 11:3', 'Deut 29:1', 'Deut 34:11']
assert P('לחיל', 'מצרים') == ['Deut 11:4'] and P('לסוסיו', 'ולרכבו') == ['Deut 11:4'] and [(s, x, m) for s, x, m in LEMT('6687')] == [('2Kgs 6:6', 'ויצף', 'HC/Vhw3ms'), ('Deut 11:4', 'הציף', 'HVhp3ms'), ('Lam 3:54', 'צפו', 'HVqp3cp')] and P('ים', 'סוף', books=('Deut',)) == ['Deut 11:4', 'Deut 1:40', 'Deut 2:1'] and len(P('ים', 'סוף', books=T)) == 7   # "MADE FLOW" — the hiphil's one seat in the Bible (the axe-head floated, the waters flowed over Lamentations' head)
assert P('מי', 'ים', 'סוף') == ['Deut 11:4', 'Josh 2:10'] and P('ברדפם', 'אחריכם') == ['Deut 11:4'] and 'Num 16:33' in U('ויאבדם', 'ויאבדו', 'ואבדם') and len(P('עד', 'היום', 'הזה', books=('Deut',))) == 6 and len(P('עד', 'היום', 'הזה', books=T)) == 12   # RAHAB reads "the waters of the Red Sea" from this verse (Joshua 2:10 the phrase's other seat)
assert P('עד', 'באכם', 'עד', 'המקום', 'הזה') == ['Deut 11:5', 'Deut 1:31', 'Deut 9:7'] and len(U('במדבר', books=('Deut',))) == 9
assert U('דתן', 'לדתן', 'ודתן') == U('אבירם', 'ולאבירם', 'ואבירם') == ['Deut 11:6', 'Num 16:1', 'Num 16:12', 'Num 16:24', 'Num 16:25', 'Num 16:27', 'Num 26:9', 'Ps 106:17'] and P('בני', 'אליאב') == ['Deut 11:6', 'Num 16:1', 'Num 16:12']   # DATHAN AND ABIRAM never apart — eight seats, always the pair
assert P('פצתה', 'הארץ', 'את', 'פיה') == ['Deut 11:6'] and P('ופצתה', 'האדמה', 'את', 'פיה') == ['Num 16:30'] and P('ותפתח', 'הארץ', 'את', 'פיה') == ['Num 16:32', 'Num 26:10'] and P('ותבלע', 'אתם') == ['Num 16:32', 'Num 26:10'] and 'Exod 15:12' in U('ותבלעם', 'תבלעמו', 'ותבלע', 'ויבלעם')
assert P('ואת', 'בתיהם') == ['Deut 11:6', 'Num 16:32'] and P('ואת', 'אהליהם') == ['Deut 11:6'] and [(s, x) for s, x, _ in LEMT('3351')] == [('Deut 11:6', 'היקום'), ('Gen 7:4', 'היקום'), ('Gen 7:23', 'היקום')] and P('בקרב', 'כל', 'ישראל') == ['Deut 11:6'] and P('אשר', 'ברגליהם') == ['2Kgs 3:9', 'Deut 11:6']   # "EVERY LIVING THING" — THE FLOOD'S WORD, the Bible's three seats: Genesis 7:4, 7:23 and the swallowing
assert P('עיניכם', 'הראת') == ['Deut 11:7', 'Deut 4:3'] and P('עיניך', 'הראת') == ['Deut 3:21'] and P('מעשה', 'יהוה', 'הגדל') == ['Deut 11:7'] and P('כל', 'מעשה', 'יהוה') == ['Deut 11:7', 'Josh 24:31', 'Judg 2:7']
# 11:8-12 THE LAND NOT LIKE EGYPT
assert P('את', 'כל', 'המצוה', books=('Deut',)) == ['Deut 11:22', 'Deut 11:8', 'Deut 15:5', 'Deut 19:9', 'Deut 27:1', 'Deut 5:31', 'Deut 6:25'] and P('למען', 'תחזקו') == ['Deut 11:8', 'Ezra 9:12'] and P('ובאתם', 'וירשתם', 'את', 'הארץ') == ['Deut 11:8', 'Deut 4:1', 'Deut 8:1'] and len(U('לרשתה', books=('Deut',))) == 25 and [s for s in U('לרשתה') if s.startswith('Deut 11:')] == ['Deut 11:10', 'Deut 11:11', 'Deut 11:29', 'Deut 11:8']   # EZRA 9:12 reads "that you may be strong" from this verse
assert P('אשר', 'אתם', 'עברים', 'שמה', 'לרשתה') == ['Deut 11:11', 'Deut 11:8', 'Deut 4:14', 'Deut 6:1'] and len(LEMT('748', books=('Deut',))) == 11 and [(s, x) for s, x, _ in LEMT('748', books=('Deut',)) if s.startswith('Deut 11:')] == [('Deut 11:9', 'תאריכו')]
assert P('על', 'האדמה', 'אשר', 'נשבע', 'יהוה', 'לאבתיכם') == ['Deut 11:21', 'Deut 11:9'] and len(U('לאבתיכם')) == 10 and len(U('לאבתיך', books=('Deut',))) == 11 and len(P('ארץ', 'זבת', 'חלב', 'ודבש')) == 14 and 'Num 16:14' in P('ארץ', 'זבת', 'חלב', 'ודבש') and len(P('זבת', 'חלב', 'ודבש')) == 20 and len(P('זבת', 'חלב', 'ודבש', books=T)) == 15
assert words('Num', 16, 13)[3:7] == ['מארץ', 'זבת', 'חלב', 'ודבש'] and words('Num', 16, 14)[3:7] == ['ארץ', 'זבת', 'חלב', 'ודבש']   # DATHAN AND ABIRAM'S OWN WORDS: the land of milk and honey said of EGYPT (16:13) and denied of Canaan (16:14) — the chapter names them (11:6) and promises it (11:9)
assert P('לא', 'כארץ', 'מצרים') == ['Deut 11:10'] and P('כארץ', 'מצרים') == ['Deut 11:10', 'Gen 13:10'] and P('כגן', 'יהוה', 'כארץ', 'מצרים') == ['Gen 13:10'] and P('כגן', 'הירק') == ['Deut 11:10'] and 'Deut 11:10' in U('הירק', 'ירק', 'וירק', 'כירק') and '1Kgs 21:2' in U('הירק', 'ירק', 'וירק', 'כירק')   # "LIKE THE LAND OF EGYPT" twice in the Bible: Lot's plain "like the garden of the LORD, like the land of Egypt" and this "not like the land of Egypt … like a garden of herbs" (Naboth's vineyard the herb garden's kin)
assert [(s, x) for s, x, _ in LEMT('1588', books=T)][0] == ('Deut 11:10', 'כגן') and len(LEMT('1588', books=T)) == 15 and all(s.startswith('Gen ') for s, _, _ in LEMT('1588', books=T)[1:]) and P('והשקית', 'ברגלך') == ['Deut 11:10'] and P('תזרע', 'את', 'זרעך') == ['Deut 11:10'] and P('אשר', 'יצאתם', 'משם') == ['Deut 11:10']   # "garden" in the Torah: Eden's thirteen, Lot's one, and this — the only garden outside Genesis
assert P('ארץ', 'הרים', 'ובקעת') == ['Deut 11:11'] and P('בבקעה', 'ובהר') == ['Deut 8:7'] and P('למטר', 'השמים', 'תשתה', 'מים') == ['Deut 11:11'] and [(s, x) for s, x, _ in LEMT('4306', books=T)] == [('Deut 11:11', 'למטר'), ('Deut 11:14', 'מטר'), ('Deut 11:17', 'מטר'), ('Deut 28:12', 'מטר'), ('Deut 28:24', 'מטר'), ('Deut 32:2', 'כמטר'), ('Exod 9:33', 'ומטר'), ('Exod 9:34', 'המטר')] and [(s, x) for s, x, _ in LEMT('1653', books=T)] == [('Gen 7:12', 'הגשם'), ('Gen 8:2', 'הגשם'), ('Lev 26:4', 'גשמיכם')]   # THE TWO WORDS FOR RAIN: the flood's and Leviticus's גשם ("rain") three seats; Deuteronomy's מטר ("rain") — six in the book, three in this chapter, Exodus's hail-rain the other two
assert P('תשתה', 'מים') == ['1Kgs 13:9', 'Deut 11:11'] and [(s, x, m) for s, x, m in LEMT('1875', books=('Deut',)) if m == 'HVqrmsa'] == [('Deut 11:12', 'דרש', 'HVqrmsa')] and P('עיני', 'יהוה') == ['Deut 11:12', 'Prov 15:3', 'Prov 22:12', 'Prov 5:21', 'Ps 34:16', 'Zech 4:10'] and U('תמיד', books=('Deut',)) == ['Deut 11:12']   # "ALWAYS" — the book's one seat; "the eyes of the LORD" the Torah's one
assert P('מרשית', 'השנה', 'ועד', 'אחרית', 'שנה') == ['Deut 11:12'] and U('מרשית') == ['Deut 11:12'] and Counter(x for _, x, _ in LEMT('7225'))['ראשית'] == 28 and Counter(x for _, x, _ in LEMT('7225'))['מראשית'] == 4 and PT('Deut', 11, 12, 'מרשית') == ['מֵֽרֵשִׁית'] and P('אחרית', 'שנה') == ['Deut 11:12'] and len(LEMT('319', books=T)) == 10   # מרשית ("from the beginning of") WITHOUT THE ALEPH — the spelling's one seat in the Bible (the shelf's reading at 40:8)
# 11:13-21 THE SECOND PARAGRAPH OF THE SHEMA
assert P('והיה', 'אם', 'שמע', 'תשמעו') == ['Deut 11:13'] and P('והיה', 'אם', 'שמוע', 'תשמע') == ['Deut 28:1'] and P('אם', 'שמוע', 'תשמע') == ['Deut 15:5', 'Deut 28:1', 'Exod 15:26'] and P('אם', 'שמע', 'תשמע') == ['Exod 23:22'] and P('שמוע', 'תשמעו') == ['Exod 19:5']   # the doubled hearing: plural and defective here alone
assert P('אל', 'מצותי') == ['Deut 11:13'] and U('מצותי', books=('Deut',)) == ['Deut 11:13', 'Deut 5:29'] and len(U('מצותי', books=T)) == 9 and P('אשר', 'אנכי', 'מצוה', 'אתכם', 'היום') == ['Deut 11:13', 'Deut 11:27', 'Deut 11:28', 'Deut 27:1', 'Deut 27:4', 'Deut 28:14'] and len(P('אשר', 'אנכי', 'מצוך', 'היום')) == 19   # "MY COMMANDMENTS" in the book: 5:29 inside God's quoted word, 11:13 INSIDE MOSES' OWN SPEECH
assert P('לאהבה', 'את', 'יהוה', 'אלהיכם', 'ולעבדו') == ['Deut 11:13'] and P('בכל', 'לבבכם', 'ובכל', 'נפשכם') == ['Deut 11:13', 'Deut 13:4', 'Josh 22:5', 'Josh 23:14'] and len(P('בכל', 'לבבך', 'ובכל', 'נפשך', books=('Deut',))) == 7
assert P('ונתתי', 'מטר', 'ארצכם', 'בעתו') == ['Deut 11:14'] and U('ונתתי', books=('Deut',)) == ['Deut 11:14', 'Deut 11:15', 'Deut 18:18'] and P('יורה', 'ומלקוש') == ['Deut 11:14'] and len(U('ומלקוש', 'מלקוש', 'למלקוש', 'כמלקוש')) == 8 and P('דגנך', 'ותירשך', 'ויצהרך') == ['Deut 11:14', 'Deut 12:17', 'Deut 7:13'] and P('ואספת', 'דגנך') == ['Deut 11:14'] and P('ונתתי', 'גשמיכם', 'בעתם') == ['Lev 26:4']   # "AND I WILL GIVE" — God's weqatal in the book three times, twice here and once in His quoted word (18:18): the speaker's "I" is God's for two verses
assert P('ונתתי', 'עשב') == ['Deut 11:15'] and len(LEMT('6212', books=T)) == 15 and P('ואכלת', 'ושבעת') == ['Deut 11:15', 'Deut 6:11', 'Deut 8:10'] and P('ואכלו', 'ושבעו') == ['Deut 14:29'] and P('ואכל', 'ושבע') == ['Deut 31:20']
assert P('השמרו', 'לכם') == ['Deut 11:16', 'Deut 4:23', 'Exod 19:12'] and len(P('השמר', 'לך')) == 12 and P('פן', 'יפתה', 'לבבכם') == ['Deut 11:16'] and P('וסרתם', 'ועבדתם', 'אלהים', 'אחרים', 'והשתחויתם', 'להם') == ['Deut 11:16'] and len(P('אלהים', 'אחרים', books=('Deut',))) == 17 and P('והשתחויתם', 'להם') == ['1Kgs 9:6', '2Chr 7:19', 'Deut 11:16', 'Josh 23:16']   # "take heed to yourselves" plural — 4:23's and Sinai's (Exodus 19:12); "and bow down to them" — Solomon's warning and Joshua's farewell the other seats
assert P('וחרה', 'אף', 'יהוה', 'בכם') == ['Deut 11:17', 'Deut 7:4', 'Josh 23:16'] and P('ועצר', 'את', 'השמים') == ['Deut 11:17'] and [(s, x) for s, x, _ in LEMT('6113', books=T)] == [('Deut 11:17', 'ועצר'), ('Deut 32:36', 'עצור'), ('Gen 16:2', 'עצרני'), ('Gen 20:18', 'עצר'), ('Gen 20:18', 'עצר'), ('Num 17:13', 'ותעצר'), ('Num 17:15', 'נעצרה'), ('Num 25:8', 'ותעצר')] and P('ולא', 'יהיה', 'מטר') == ['1Kgs 8:35', '2Chr 6:26', '2Chr 7:13', 'Deut 11:17']   # THE SHUTTING — Abimelech's wombs (Genesis 20:18, the shelf's proof at 306:6), the plagues stayed (Numbers 17, 25); "that there be no rain" SOLOMON'S PRAYER reads back (1 Kings 8:35)
assert P('והאדמה', 'לא', 'תתן', 'את', 'יבולה') == ['Deut 11:17'] and P('ונתנה', 'הארץ', 'יבולה') == ['Lev 26:4'] and P('ולא', 'תתן', 'ארצכם', 'את', 'יבולה') == ['Lev 26:20'] and len(LEMT('2981')) == 13 and P('ואבדתם', 'מהרה', 'מעל', 'הארץ', 'הטבה') == ['Deut 11:17'] and P('ואבדתם', 'מהרה', 'מעל', 'הארץ', 'הטובה') == ['Josh 23:16'] and P('אבד', 'תאבדון', 'מהר') == ['Deut 4:26'] and U('מהרה', books=('Deut',)) == ['Deut 11:17'] and P('אשר', 'יהוה', 'נתן', 'לכם', books=('Deut',)) == ['Deut 11:17']
assert P('ושמתם', 'את', 'דברי', 'אלה') == ['Deut 11:18'] and P('על', 'לבבכם', 'ועל', 'נפשכם') == ['Deut 11:18'] and P('והיו', 'הדברים', 'האלה') == ['Deut 6:6'] and P('וקשרתם', 'אתם', 'לאות', 'על', 'ידכם') == ['Deut 11:18'] and P('וקשרתם', 'לאות', 'על', 'ידך') == ['Deut 6:8'] and P('לאות', 'על', 'ידך') == ['Deut 6:8', 'Exod 13:9'] and P('לאות', 'על', 'ידכה') == ['Exod 13:16'] and U('ידכה') == ['Exod 13:16']
assert [(s, x) for s, x, _ in LEMT('2903')] == [('Deut 6:8', 'לטטפת'), ('Deut 11:18', 'לטוטפת'), ('Exod 13:16', 'ולטוטפת')] and PT('Deut', 11, 18, 'לטוטפת') == ['לְטוֹטָפֹת'] and PT('Deut', 6, 8, 'לטטפת') == ['לְטֹטָפֹת'] and PT('Exod', 13, 16, 'ולטוטפת') == ['וּלְטוֹטָפֹת']   # THE FRONTLETS' THREE SEATS AND THEIR SPELLINGS: 6:8 defective, 11:18 and Exodus 13:16 with the first vav — the shelf's count of four (35:4; Sanhedrin 4b, Menachot 34b) the compile's open row (4b's)
assert P('בין', 'עיניכם') == ['Deut 11:18', 'Deut 14:1'] and P('בין', 'עיניך') == ['Deut 6:8', 'Exod 13:16', 'Exod 13:9']   # "between your eyes" plural: the frontlets here and the baldness of mourning at 14:1
assert P('ולמדתם', 'אתם', 'את', 'בניכם') == ['Deut 11:19'] and P('ושננתם', 'לבניך') == ['Deut 6:7'] and [(s, x, m) for s, x, m in LEMT('3925', books=('Deut',)) if x == 'ולמדתם'] == [('Deut 5:1', 'ולמדתם', 'HC/Vqq2mp'), ('Deut 11:19', 'ולמדתם', 'HC/Vpq2mp')] and P('לדבר', 'בם') == ['Deut 11:19'] and P('ודברת', 'בם') == ['Deut 6:7'] and P('בשבתך', 'בביתך', 'ובלכתך', 'בדרך', 'ובשכבך', 'ובקומך') == ['Deut 11:19', 'Deut 6:7']   # THE SAME CONSONANTS, TWO STEMS: 5:1's "and you shall LEARN them" (qal) and 11:19's "and you shall TEACH them" (piel) — the DB's morphology divides the homograph; 6:7's "repeat" the other verb
assert P('וכתבתם', 'על', 'מזוזות', 'ביתך', 'ובשעריך') == ['Deut 11:20'] and P('וכתבתם', 'על', 'מזוזת', 'ביתך', 'ובשעריך') == ['Deut 6:9'] and [(s, x) for s, x, _ in LEMT('4201', books=('Deut',))] == [('Deut 6:9', 'מזוזת'), ('Deut 11:20', 'מזוזות')] and PT('Deut', 11, 20, 'מזוזות') == ['מְזוּזוֹת'] and len(LEMT('4201')) == 19   # THE DOORPOSTS: 6:9 with one vav, 11:20 with two — the shelf's inclusion after inclusion (36:3) on the pair
assert P('למען', 'ירבו', 'ימיכם') == ['Deut 11:21'] and P('כימי', 'השמים', 'על', 'הארץ') == ['Deut 11:21'] and P('כימי', 'שמים') == ['Ps 89:30'] and P('אשר', 'נשבע', 'יהוה', 'לאבתיכם', 'לתת', 'להם') == ['Deut 11:21', 'Deut 11:9'] and P('נשבע', 'יהוה', 'לאבתיכם') == ['Deut 11:21', 'Deut 11:9', 'Deut 1:8', 'Deut 8:1']
# 11:22-25 THE BORDERS AND THE DREAD
assert P('כי', 'אם', 'שמר', 'תשמרון') == ['Deut 11:22'] and P('שמור', 'תשמרון') == ['Deut 6:17'] and U('תשמרון', books=('Deut',)) == ['Deut 11:22', 'Deut 12:1', 'Deut 6:17', 'Deut 8:1'] and P('את', 'כל', 'המצוה', 'הזאת') == ['Deut 11:22', 'Deut 15:5', 'Deut 19:9', 'Deut 6:25'] and P('ללכת', 'בכל', 'דרכיו') == ['1Kgs 8:58', 'Deut 10:12', 'Deut 11:22'] and P('ולדבקה', 'בו') + P('לדבקה', 'בו') == ['Deut 11:22', 'Deut 30:20', 'Josh 22:5'] and len(LEMT('1692', books=('Deut',))) == 7 and U('לעשתה', books=('Deut',)) == ['Deut 11:22', 'Deut 19:9']
assert P('והוריש', 'יהוה', 'את', 'כל', 'הגוים', 'האלה', 'מלפניכם') == ['Deut 11:23'] and [(s, x) for s, x, m in LEMT('3423', books=('Deut',)) if m and 'Vh' in m] == [('Deut 4:38', 'להוריש'), ('Deut 7:17', 'להורישם'), ('Deut 9:3', 'והורשתם'), ('Deut 9:4', 'מורישם'), ('Deut 9:5', 'מורישם'), ('Deut 11:23', 'והוריש'), ('Deut 18:12', 'מוריש')] and P('גוים', 'גדלים', 'ועצמים', 'מכם') == ['Deut 11:23'] and P('גוים', 'גדלים', 'ועצמים', 'ממך') == ['Deut 4:38', 'Deut 9:1'] and P('רבים', 'ועצומים', 'ממך') == ['Deut 7:1']   # "greater and mightier THAN YOU" — plural here, singular at 4:38 and 9:1 (chapter 7's find on the number)
assert P('כל', 'המקום', 'אשר', 'תדרך', 'כף', 'רגלכם', 'בו') == ['Deut 11:24'] and P('כל', 'מקום', 'אשר', 'תדרך', 'כף', 'רגלכם', 'בו') == ['Josh 1:3'] and words('Josh', 1, 3)[7:] == ['לכם', 'נתתיו', 'כאשר', 'דברתי', 'אל', 'משה'] and P('מן', 'המדבר', 'והלבנון') == ['Deut 11:24'] and P('מהמדבר', 'והלבנון') == ['Josh 1:4']   # JOSHUA 1:3 quotes the verse with the article dropped and ends "AS I SPOKE TO MOSES" — the run's receipt of this verse
assert P('הנהר', 'נהר', 'פרת') == ['Deut 11:24'] and P('הנהר', 'הגדל', 'נהר', 'פרת') == ['Deut 1:7', 'Gen 15:18'] and P('הנהר', 'הגדול', 'נהר', 'פרת') == ['Josh 1:4'] and len(P('נהר', 'פרת')) == 9 and P('הים', 'האחרון') == ['Deut 11:24', 'Deut 34:2', 'Joel 2:20', 'Zech 14:8'] and U('גבלכם', 'גבולכם') == ['Deut 11:24', 'Josh 1:4'] and P('ושתי', 'את', 'גבלך') == ['Exod 23:31']
assert P('לא', 'יתיצב', 'איש', 'בפניכם') == ['Deut 11:25'] and P('לא', 'יתיצב', 'איש', 'בפניך') == ['Deut 7:24'] and P('לא', 'יתיצב', 'איש', 'לפניך') == ['Josh 1:5'] and len(U('יתיצב')) == 8 and P('פחדכם', 'ומוראכם') == ['Deut 11:25'] and P('פחדך', 'ויראתך') == ['Deut 2:25'] and len(P('על', 'פני', 'כל', 'הארץ')) == 11
assert P('כאשר', 'דבר', 'לכם') == ['Deut 11:25', 'Deut 1:11', 'Josh 23:10'] and P('כאשר', 'דבר', 'לך', books=('Deut',)) == ['Deut 12:20', 'Deut 15:6', 'Deut 26:18', 'Deut 29:12'] and len(P('כאשר', 'דבר', books=('Deut',))) == 16 and len(P('כאשר', 'צוה', books=('Deut',))) == 3 and len(P('כאשר', 'צוך', books=('Deut',))) == 3 and len(P('כאשר', 'צוני', books=('Deut',))) == 2   # THE RECEIPT BY "SPOKE": sixteen in the book against eight by "commanded" — the finder's third form (4b's owed item) weighs twice the first two
# 11:26-32 THE BLESSING AND THE CURSE
assert P('ראה', 'אנכי', 'נתן', 'לפניכם', 'היום') == ['Deut 11:26'] and P('ראה', 'נתתי', 'לפניך', 'היום') == ['Deut 30:15'] and P('ברכה', 'וקללה') == ['Deut 11:26'] and P('הברכה', 'והקללה') == ['Deut 30:1', 'Deut 30:19', 'Josh 8:34'] and P('קללה', 'ולא', 'ברכה') == ['Gen 27:12'] and len(LEMT('1293', books=('Deut',))) == 12 and len(LEMT('7045', books=('Deut',))) == 11
assert [(s, x) for s, x, m in LEMT('7200', books=('Deut',)) if m == 'HVqv2ms'] == [('Deut 1:8', 'ראה'), ('Deut 1:21', 'ראה'), ('Deut 2:24', 'ראה'), ('Deut 2:31', 'ראה'), ('Deut 4:5', 'ראה'), ('Deut 11:26', 'ראה'), ('Deut 30:15', 'ראה')] and P('אנכי', 'נתן', 'לפניכם', 'היום') == ['Deut 11:26', 'Deut 11:32', 'Deut 4:8']   # "SEE" the singular imperative seven in the book — at 1:8 and 11:26 over a plural "before you"; the frame "which I set before you today" 4:8, 11:26, 11:32
assert P('את', 'הברכה', 'אשר', 'תשמעו') == ['Deut 11:27'] and P('והקללה', 'אם', 'לא', 'תשמעו') == ['Deut 11:28'] and P('אל', 'מצות', 'יהוה', 'אלהיכם') == ['Deut 11:27', 'Deut 11:28'] and P('וסרתם', 'מן', 'הדרך') == ['Deut 11:28', 'Deut 31:29'] and P('סרו', 'מהר', 'מן', 'הדרך', 'אשר', 'צויתם') == ['Deut 9:12', 'Exod 32:8'] and P('מן', 'הדרך', books=('Deut',)) == ['Deut 11:28', 'Deut 13:6', 'Deut 31:29', 'Deut 9:12', 'Deut 9:16']   # THE CALF'S FORMULA "turned aside from the way" (Exodus 32:8, 9:12, 9:16) said of the curse
assert P('ללכת', 'אחרי', 'אלהים', 'אחרים') == ['Deut 11:28', 'Deut 28:14', 'Judg 2:19'] and P('אלהים', 'אחרים', 'אשר', 'לא', 'ידעתם') == ['Deut 11:28', 'Deut 13:14', 'Deut 13:3', 'Jer 7:9'] and P('אשר', 'לא', 'ידעת', books=('Deut',)) == ['Deut 13:7', 'Deut 28:33', 'Deut 28:36', 'Deut 28:64', 'Deut 8:3'] and P('אשר', 'לא', 'ידעום') == ['Deut 29:25', 'Jer 19:4', 'Jer 44:3', 'Zech 7:14']
assert P('והיה', 'כי', 'יביאך', 'יהוה', 'אלהיך', 'אל', 'הארץ') == ['Deut 11:29', 'Deut 6:10'] and P('כי', 'יביאך', 'יהוה', 'אלהיך') == ['Deut 11:29', 'Deut 6:10', 'Deut 7:1'] and len(P('אשר', 'אתה', 'בא', 'שמה', 'לרשתה')) == 7 and P('ונתתה', 'את', 'הברכה', 'על', 'הר', 'גרזים') == ['Deut 11:29']
assert U('גרזים') == ['Deut 11:29', 'Deut 27:12', 'Josh 8:33', 'Judg 9:7'] and U('עיבל', 'ועיבל') == ['1Chr 1:22', '1Chr 1:40', 'Deut 11:29', 'Deut 27:13', 'Deut 27:4', 'Gen 36:23', 'Josh 8:30', 'Josh 8:33'] and P('הר', 'עיבל') == ['Deut 11:29', 'Josh 8:33'] and P('בהר', 'עיבל') == ['Deut 27:13', 'Deut 27:4', 'Josh 8:30'] and words('Deut', 27, 12)[:3] == ['אלה', 'יעמדו', 'לברך'] and words('Josh', 8, 33)[-10:-6] == ['כאשר', 'צוה', 'משה', 'עבד']   # GERIZIM four seats, EBAL eight — three of them a man (Genesis 36:23's Ebal, the Chronicler's): the homograph for the census; JOSHUA 8:33 "as Moses the servant of the LORD commanded" the run's receipt
assert len(P('בעבר', 'הירדן', books=('Deut',))) == 9 and P('אחרי', 'דרך', 'מבוא', 'השמש') == ['Deut 11:30'] and P('מבוא', 'השמש') == ['Deut 11:30', 'Josh 1:4', 'Josh 23:4', 'Zech 8:7'] and U('מבוא', 'ומבוא', 'למבוא', books=T) == ['Deut 11:30', 'Gen 24:62'] and P('הכנעני', 'הישב', 'בערבה') == ['Deut 11:30'] and U('בערבה', books=('Deut',)) == ['Deut 11:30', 'Deut 1:1', 'Deut 1:7']
assert [s for s in U('הגלגל', 'גלגל', 'הגלגלה', 'בגלגל', 'מהגלגל', 'גלגלה') if s.startswith(('Gen', 'Exod', 'Lev', 'Num', 'Deut'))] == ['Deut 11:30'] and len(U('הגלגל', 'גלגל', 'הגלגלה', 'בגלגל', 'מהגלגל', 'גלגלה')) == 41   # GILGAL — the Torah's ONE seat (forty in the Prophets and Writings)
assert P('אצל', 'אלוני', 'מרה') == ['Deut 11:30'] and P('אלון', 'מורה') == ['Gen 12:6'] and [(s, x) for s, x, _ in LEMT('436')] == [('1Sam 10:3', 'אלון'), ('Deut 11:30', 'אלוני'), ('Gen 12:6', 'אלון'), ('Gen 13:18', 'באלני'), ('Gen 14:13', 'באלני'), ('Gen 18:1', 'באלני'), ('Judg 4:11', 'אלון'), ('Judg 9:6', 'אלון'), ('Judg 9:37', 'אלון')] and lemma_of('Deut', 11, 30, 'מרה') == ['4176'] and lemma_of('Exod', 15, 23, 'מרה') == ['4785'] and 'Exod 15:23' in U('מרה') and len(U('מרה')) == 11   # "THE TEREBINTHS OF MOREH" plural and defective (Genesis 12:6 singular, plene); מרה THE HOMOGRAPH — Moreh here, MARAH the bitter station at Exodus 15:23, "bitter" elsewhere: the DB divides them by lemma
assert P('כי', 'אתם', 'עברים', 'את', 'הירדן') == ['Deut 11:31', 'Num 33:51', 'Num 35:10'] and len(P('אתם', 'עברים', 'את', 'הירדן')) == 7 and P('לבא', 'לרשת', 'את', 'הארץ') == ['Deut 11:31', 'Judg 18:9'] and P('וירשתם', 'אתה', 'וישבתם', 'בה') == ['Deut 11:31'] and P('והורשתם', 'את', 'הארץ', 'וישבתם', 'בה') == ['Num 33:53'] and len(P('אשר', 'יהוה', 'אלהיכם', 'נתן', 'לכם', books=('Deut',))) == 1
assert P('ושמרתם', 'לעשות', 'את', 'כל', 'החקים', 'ואת', 'המשפטים') == ['Deut 11:32'] and P('החקים', 'ואת', 'המשפטים') == ['1Chr 22:13', '2Kgs 17:37', 'Deut 11:32', 'Deut 5:1', 'Deut 7:11', 'Neh 1:7'] and P('החקים', 'והמשפטים') == ['Deut 12:1', 'Deut 6:1', 'Lev 26:46'] and P('ושמרתם', 'לעשות', books=('Deut',)) == ['Deut 11:32', 'Deut 5:32'] and words('Deut', 12, 1)[:6] == ['אלה', 'החקים', 'והמשפטים', 'אשר', 'תשמרון', 'לעשות']   # the chapter's last verse is the next chapter's head — "keep to do the statutes and the judgments" / "these are the statutes and the judgments which you shall keep to do"
# ONKELOS OVER THE BOOK (the E print; the export's verse numbers)
assert aramaic(11, 1) == ['ותרחם', 'ית', 'יי', 'אלהך', 'ותטר', 'מטרת', 'מימריה', 'וקימוהי', 'ודינוהי', 'ופקודוהי', 'כל', 'יומיא'] and (11, 1) in onk_seats('מימר') and len(onk_seats('מימר')) == 91 and [s for s in onk_seats('מימר') if s[0] == 10] == []   # THE MEMRA RETURNS — "the charge of His Word" at 11:1 (chapter 10 had none); ninety-one rows of the book carry the Word
assert onk_seats('אלפנ') == [(11, 2), (31, 22), (32, 2), (32, 10)] and (11, 4) in onk_seats('משרי') and len(onk_seats('משרי')) == 10 and onk_seats('אנש בתי') == [(11, 6), (12, 7)]
assert '(כל)' in aramaic(11, 8) and 'ותעלון' in aramaic(11, 8) and Counter(c + 1 for c in range(34) for v in range(len(onk_he[c])) if '(' in clean(onk_he[c][v])) == Counter({33: 2, 6: 1, 11: 1, 18: 1, 20: 1, 22: 1, 25: 1, 29: 1, 32: 1})   # THE EXPORT'S PARENTHESIS at 11:8 — "(all) the commandment" a marked variant, one of ten rows so marked in the book; "go up" for "come in"
assert len(onk_tok('קיים')) == 22 and (11, 9) in onk_tok('קיים') and (11, 21) in onk_tok('קיים') and onk_seats('עבדא חלב') == [(6, 3), (11, 9), (26, 9), (26, 15), (27, 3), (31, 20)] and len(onk_tok('עלל')) == 10 and (11, 10) in onk_tok('עלל') and (11, 29) in onk_tok('עלל')
assert 'ומשקת ליה' in arm(11, 10) and 'כגנתא ירקא' in arm(11, 10) and onk_tok('ובקען') == [(11, 11)] and onk_tok('תבע') == [(10, 12), (11, 12)] and onk_tok('תדירא') == [(11, 12)] and onk_seats('דשתא') == [(11, 12)] and 'מרישא דשתא ועד סופא דשתא' in arm(11, 12)
assert onk_tok('קבלא') == [(11, 13), (15, 5), (28, 1)] and onk_tok('תקבלון') == [(7, 12), (11, 13), (11, 27), (11, 28), (13, 5), (18, 15)] and len(onk_tok('קדמוהי')) == 26 and (11, 13) in onk_tok('קדמוהי') and (11, 22) in onk_tok('קדמוהי')
assert onk_tok('בכיר') == [(11, 14)] and onk_tok('ולקיש') == [(11, 14)] and onk_tok('עבורך') == [(7, 13), (11, 14), (12, 17), (14, 23), (18, 4)] and onk_tok('יטעון') == [(11, 16)] and len(onk_seats('טעות עממיא')) == 18 and (11, 16) in onk_seats('טעות עממיא') and (11, 28) in onk_seats('טעות עממיא')
assert onk_tok('רגזא') == [(6, 15), (7, 4), (9, 19), (11, 17), (29, 19), (29, 23), (29, 26), (32, 27)] and onk_tok('ויחוד') == [(11, 17)] and onk_tok('בפריע') == [(4, 26), (7, 4), (7, 22), (9, 3), (9, 12), (9, 16), (11, 17), (28, 20)]
assert onk_seats('תפלין') == [(6, 8), (11, 18)] and aramaic(6, 8) == ['ותקטרנון', 'לאת', 'על', 'ידך', 'ויהון', 'לתפלין', 'בין', 'עיניך'] and aramaic(11, 19)[0] == 'ותלפון' and aramaic(6, 7)[0] == 'ותתננון' and aramaic(11, 19)[5:] == aramaic(6, 7)[3:] == ['בהון', 'במתבך', 'בביתך', 'ובמהכך', 'בארחא', 'ובמשכבך', 'ובמקימך']
assert aramaic(11, 20) == ['ותכתבנון', 'על', 'מזוזין', 'ותקבענון', 'בספי', 'ביתך', 'ובתרעך'] and aramaic(6, 9) == ['ותכתבנון', 'על', 'מזוזין', 'ותקבענון', 'בספי', 'ביתך', 'ובתרעיך'] and onk_tok('מזוזין') == [(6, 9), (11, 20)] and onk_tok('ותקבענון') == [(6, 9), (11, 20)]   # ONKELOS AT BOTH SEATS: "write them on MEZUZOT and FIX THEM on the DOORPOSTS" — two nouns and a supplied verb, the scroll and the post (one letter apart: "your gate" / "your gates")
assert onk_seats('דתקנן') == [(8, 6), (10, 12), (11, 22), (19, 9), (26, 17), (28, 9), (30, 16)] and onk_tok('לדחלתיה') == [(4, 20), (11, 22), (30, 20)] and onk_seats('אתקרב') == [(11, 22), (30, 20)] and len(onk_seats('תרך')) == 11 and (11, 23) in onk_seats('תרך')
assert onk_tok('פרסת') == [(2, 5), (11, 24), (28, 56)] and onk_seats('ימא מערבא') == [(11, 24), (34, 2)] and onk_tok('תחומכון') == [(11, 24)] and onk_tok('יתעתד') == [(7, 24), (11, 25)] and onk_tok('דחלתכון') == [(11, 25)] and onk_seats('מליל לכון') == [(1, 11), (11, 25)]
assert aramaic(11, 26) == ['חזי', 'די', 'אנא', 'יהב', 'קדמיכון', 'יומא', 'דין', 'ברכן', 'ולוטין'] and onk_tok('ברכן') == [(11, 26), (11, 27), (30, 1), (30, 19), (33, 23)] and onk_tok('ולוטין') == [(11, 26), (30, 1), (30, 19)] and onk_tok('ולוטיא') == [(11, 28)] and onk_tok('לוטיא') == [(27, 13), (28, 15), (28, 45), (29, 19), (29, 26), (30, 7)]   # BLESSINGS AND CURSES — the Aramaic pluralizes the singular pair (the same at 30:1, 30:19)
assert onk_tok('מברכיא') == [(11, 29)] and onk_tok('מלטטיא') == [(11, 29)] and 'מברכיא על טורא דגרזין' in arm(11, 29) and 'מלטטיא על טורא דעיבל' in arm(11, 29) and aramaic(27, 12)[:3] == ['אלין', 'יקומון', 'לברכא'] and aramaic(27, 13)[:5] == ['ואלין', 'יקומון', 'על', 'לוטיא', 'בטורא']   # THE BLESSERS AND THE CURSERS — the persons for the words at 11:29 alone (27:12-13's tribes "to bless" / "on the curses")
assert 'מישרי מרה' in arm(11, 30) and 'במישרא' in aramaic(11, 30) and 'מעלני שמשא' in arm(11, 30) and len(onk_seats('מישר')) == 16 and aramaic(11, 32)[4] == 'קימיא' and aramaic(11, 32)[6] == 'דיניא'
og = json.load(open(f'{ROOT}/Data/sefaria_export/Onkelos_Genesis/he.json', encoding='utf-8'))['text']; ox = json.load(open(f'{ROOT}/Data/sefaria_export/Onkelos_Exodus/he.json', encoding='utf-8'))['text']
assert 'מישר מורה' in plain(clean(og[11][5])) and 'כגינתא דיי כארעא דמצרים' in plain(clean(og[12][9])) and 'ולתפלין בין עיניך' in plain(clean(ox[12][15])) and 'ולדכרנא בין עיניך' in plain(clean(ox[12][8]))   # Onkelos Genesis 12:6 "the PLAIN of Moreh" (the trees a plain there too), 13:10 "like the garden of the LORD, like the land of Egypt"; Exodus 13:16 "tefillin", 13:9 "a reminder"
# THE ENGLISH'S BRACKETS — eighteen supplements in fifteen verses
BR = {v: re.findall(r'\[([^\]]+)\]', clean(onk[10][v - 1])) for v in range(1, 33)}
assert sum(len(b) for b in BR.values()) == 18 and {v: len(b) for v, b in BR.items() if b} == {1: 1, 4: 1, 6: 2, 8: 1, 9: 1, 10: 1, 13: 1, 16: 2, 18: 1, 20: 1, 22: 2, 24: 1, 27: 1, 28: 1, 30: 1} and BR[18] == ['tefillin'] and BR[20] == ['and affix them to the lintels'] and BR[22] == ['that are correct before Him', 'come near to the fear of Him'] and BR[16] == ['mistaken', 'idols of the nations'] and [v for v in range(1, 33) if '(' in clean(onk[10][v - 1])] == []
# THE STORE'S GLOSSES (the display layer, never the draft): a selection read back per verse; the families censused over the whole store (the G print)
assert sg(11, 1, 'משמרתו') == 'watch-him/its' and sg(11, 2, 'מוסר') == 'chastisement' and sg(11, 2, 'גדלו') == 'magnitude-him/its' and sg(11, 2, 'הנטויה') == 'the-stretch' and sg(11, 3, 'אתתיו') == 'signs-him/its' and sg(11, 4, 'לחיל') == 'to-force' and sg(11, 4, 'הציף') == 'overflow' and sg(11, 4, 'סוף') == 'reed' and sg(11, 4, 'ברדפם') == 'in-run-after--gone-by)-them/their' and sg(11, 4, 'ויאבדם') == 'and-wander-away-them/their'
assert sg(11, 6, 'פצתה') == 'rend' and sg(11, 6, 'ותבלעם') == 'and-make-away-with-them/their' and sg(11, 6, 'היקום') == 'the-standing' and sg(11, 6, 'בקרב') == 'in-nearest-part' and sg(11, 7, 'הראת') == 'the-see' and sg(11, 8, 'אנכי') == '?' and sg(11, 8, 'תחזקו') == 'fasten-upon' and sg(11, 9, 'תאריכו') == 'be--long' and sg(11, 9, 'זבת') == 'flow-freely'
assert sg(11, 10, 'כארץ') == 'like-earth' and sg(11, 10, 'תזרע') == 'yield-seed' and sg(11, 10, 'והשקית') == 'and-quaff' and sg(11, 10, 'כגן') == 'like-garden' and sg(11, 10, 'הירק') == 'the-green' and sg(11, 11, 'ובקעת') == 'and-split' and sg(11, 11, 'למטר') == 'to-rain' and sg(11, 11, 'תשתה') == 'imbibe' and sg(11, 12, 'דרש') == 'tread' and sg(11, 12, 'תמיד') == 'continuance' and sg(11, 12, 'מרשית') == 'from-beginning' and sg(11, 12, 'אחרית') == 'last'
assert sg(11, 13, 'מצותי') == 'commandment-me/my' and sg(11, 13, 'ולעבדו') == 'and-to-work/serve-him/its' and sg(11, 14, 'יורה') == 'sprinkling' and sg(11, 14, 'ומלקוש') == 'and-spring-rain' and sg(11, 14, 'ואספת') == 'and-gather-for-any-purpose' and sg(11, 14, 'ותירשך') == 'and-must-you/your' and sg(11, 15, 'עשב') == 'herb' and sg(11, 15, 'ושבעת') == 'and-sate'
assert sg(11, 16, 'יפתה') == 'open' and sg(11, 16, 'אחרים') == 'hinder' and sg(11, 16, 'והשתחויתם') == 'and-depress' and sg(11, 17, 'וחרה') == 'and-glow' and sg(11, 17, 'אף') == 'nose' and sg(11, 17, 'ועצר') == 'and-inclose' and sg(11, 17, 'יבולה') == 'produce-her/its' and sg(11, 17, 'ואבדתם') == 'and-wander-away' and sg(11, 17, 'מהרה') == 'hurry'
assert sg(11, 18, 'וקשרתם') == 'and-tie' and sg(11, 18, 'לאות') == 'to-signs' and sg(11, 18, 'לטוטפת') == 'to-fillet-for-the-forehead' and sg(11, 19, 'ולמדתם') == 'and-goad' and sg(11, 20, 'וכתבתם') == 'and-grave-them/their' and sg(11, 20, 'מזוזות') == 'door-post' and sg(11, 22, 'כי') == 'very-widely-used-as-a-relati' and sg(11, 22, 'אם') == 'as-demonstrative' and sg(11, 22, 'ולדבקה') == 'and-to-impinge'
assert sg(11, 23, 'מלפניכם') == 'from-to-face-you/your (pl)' and sg(11, 23, 'ועצמים') == 'and-powerful' and sg(11, 24, 'כף') == 'palm-of-hand' and sg(11, 24, 'הנהר') == 'the-stream' and sg(11, 24, 'נהר') == 'stream' and sg(11, 24, 'האחרון') == 'the-hinder' and sg(11, 24, 'גבלכם') == 'cord-you/your (pl)' and sg(11, 25, 'יתיצב') == 'place' and sg(11, 25, 'פחדכם') == 'alarm-you/your (pl)' and sg(11, 25, 'ומוראכם') == 'and-fear-you/your (pl)'
assert sg(11, 26, 'ברכה') == 'benediction' and sg(11, 26, 'וקללה') == 'and-vilification' and sg(11, 28, 'והקללה') == 'and-the-vilification' and sg(11, 29, 'הקללה') == 'the-vilification' and sg(11, 30, 'הלא') == 'the-not' and sg(11, 30, 'בעבר') == 'in-region-across' and sg(11, 30, 'מבוא') == 'entrance' and sg(11, 30, 'הכנעני') == 'the-Kenaanite' and sg(11, 30, 'בערבה') == 'in-desert' and sg(11, 30, 'מול') == 'abrupt' and sg(11, 30, 'אצל') == 'side' and sg(11, 30, 'אלוני') == 'oak' and sg(11, 32, 'החקים') == 'the-enactment'
GLOSS_FAMILY = {'watch-him/its': [('משמרתו', 2)], 'chastisement': [('מוסר', 1)], 'and-arm-him/its': [('וזרעו', 1)], 'signs-him/its': [('אתתיו', 1)], 'deed/work-him/its': [('מעשיו', 1)], 'to-force': [('לחיל', 1)], 'to-horse-him/its': [('לסוסיו', 1)], 'and-to-vehicle-him/its': [('ולרכבו', 1)], 'in-run-after--gone-by)-them/their': [('ברדפם', 1)], 'and-make-away-with-them/their': [('ותבלעם', 1)], 'the-standing': [('היקום', 3)], 'in-foot-them/their': [('ברגליהם', 1)],
                'like-garden': [('כגן', 2), ('כגנת', 1)], 'to-rain': [('למטר', 1)], 'continuance': [('תמיד', 18)], 'from-beginning': [('מראשית', 2), ('מרשית', 1)], 'last': [('אחרית', 1)], 'sprinkling': [('יורה', 1)], 'and-spring-rain': [('ומלקוש', 1)], 'and-oil-you/your': [('ויצהרך', 5)], 'herb': [('עשב', 14)], 'and-glow': [('ויחר', 19), ('וחרה', 4)], 'and-inclose': [('ותעצר', 2), ('ועצר', 1)], 'produce-her/its': [('יבולה', 3)], 'and-to-impinge': [('ולדבקה', 2)],
                'from-to-face-you/your (pl)': [('מלפניכם', 1)], 'cord-you/your (pl)': [('גבלכם', 1)], 'alarm-you/your (pl)': [('פחדכם', 1)], 'and-fear-you/your (pl)': [('ומוראכם', 2)], 'and-vilification': [('וקללה', 1)], 'and-the-vilification': [('והקללה', 3)], 'entrance': [('מבוא', 1)], 'the-Kenaanite': [('הכנעני', 18), ('הכנענית', 2)], 'day-you/your (pl)': [('ימיכם', 1)], 'son-you/your (pl)': [('בניכם', 9)], 'to-make-her/its': [('לעשתה', 2)], 'to-face-you/your (pl)': [('לפניכם', 17)], 'to-father-you/your (pl)': [('לאבתיכם', 6)],
                'seed-you/your': [('זרעך', 21)], 'in-field-you/your': [('בשדך', 2)], 'to-livestock-you/your': [('לבהמתך', 1)], 'house-them/their': [('בתיהם', 2)], 'tent-them/their': [('אהליהם', 2)], 'earth-you/your (pl)': [('ארצכם', 8)], 'earth-him/its': [('ארצו', 14)], 'mouth-her/its': [('פיה', 6)], 'eye-you/your (pl)': [('עיניכם', 7)], 'heart-you/your (pl)': [('לבבכם', 8), ('לבכם', 1)], 'in-time-him/its': [('בעתו', 2)], 'the-strong': [('החזקה', 4), ('החזק', 1)], 'like-earth': [('כארץ', 2)],
                'and-statute-him/its': [('וחקתיו', 6)], 'and-judgment-him/its': [('ומשפטיו', 5)], 'and-commandment-him/its': [('ומצותיו', 3)], 'and-to-seed-them/their': [('ולזרעם', 2)], 'the-Gilgal': [('הגלגל', 1)], 'and-in-gate-you/your': [('ובשעריך', 2)], 'and-in-go-you/your': [('ובלכתך', 2)], 'in-house-you/your': [('בביתך', 9)], 'in-face-you/your (pl)': [('בפניכם', 1)], 'in-midst': [('בתוך', 51)], 'and-to-work/serve-him/its': [('ולעבדו', 1)], 'word/thing-me/my': [('דברי', 7)], 'hind-part-you/your (pl)': [('אחריכם', 4)]}
GT = {g: store.execute("SELECT REPLACE(w.he_plain,'/',''), COUNT(*) FROM words w WHERE w.gloss=? GROUP BY 1 ORDER BY 2 DESC, 1", (g,)).fetchall() for g in GLOSS_FAMILY}
assert all(sorted(GT[g]) == sorted(v) for g, v in GLOSS_FAMILY.items()), [g for g, v in GLOSS_FAMILY.items() if sorted(GT[g]) != sorted(v)]
# BY GLOSS — every token of the gloss the one word (or one family read the same at every seat): the rewrite covers the whole store (SIXTY-FOUR)
OVERRIDE_GLOSS = [('watch-him/its', 'his-charge'), ('chastisement', 'the-discipline-of'), ('and-arm-him/its', 'and-his-arm'), ('signs-him/its', 'his-signs'), ('deed/work-him/its', 'his-deeds'), ('to-force', 'to-the-army-of'), ('to-horse-him/its', 'to-its-horses'), ('and-to-vehicle-him/its', 'and-to-its-chariots'), ('in-run-after--gone-by)-them/their', 'when-they-pursued'), ('and-make-away-with-them/their', 'and-swallowed-them'), ('the-standing', 'the-living-thing'), ('in-foot-them/their', 'at-their-feet'),
                  ('like-garden', 'like-a-garden-of'), ('to-rain', 'by-the-rain-of'), ('continuance', 'always'), ('from-beginning', 'from-the-beginning-of'), ('last', 'the-end-of'), ('sprinkling', 'the-early-rain'), ('and-spring-rain', 'and-the-late-rain'), ('and-oil-you/your', 'and-your-oil'), ('herb', 'grass'), ('and-glow', 'and-be-kindled'), ('and-inclose', 'and-shut-up'), ('produce-her/its', 'its-produce'), ('and-to-impinge', 'and-to-cleave'),
                  ('from-to-face-you/your (pl)', 'from-before-you'), ('cord-you/your (pl)', 'your-border'), ('alarm-you/your (pl)', 'the-dread-of-you'), ('and-fear-you/your (pl)', 'and-the-fear-of-you'), ('and-vilification', 'and-a-curse'), ('and-the-vilification', 'and-the-curse'), ('entrance', 'the-going-down-of'), ('the-Kenaanite', 'the-Canaanite'), ('day-you/your (pl)', 'your-days'), ('son-you/your (pl)', 'your-children'), ('to-make-her/its', 'to-do-it'), ('to-face-you/your (pl)', 'before-you'), ('to-father-you/your (pl)', 'to-your-fathers'),
                  ('seed-you/your', 'your-seed'), ('in-field-you/your', 'in-your-field'), ('to-livestock-you/your', 'for-your-cattle'), ('house-them/their', 'their-houses'), ('tent-them/their', 'their-tents'), ('earth-you/your (pl)', 'your-land'), ('earth-him/its', 'his-land'), ('mouth-her/its', 'its-mouth'), ('eye-you/your (pl)', 'your-eyes'), ('heart-you/your (pl)', 'your-heart'), ('in-time-him/its', 'in-its-season'), ('the-strong', 'the-mighty'), ('like-earth', 'like-the-land-of'),
                  ('and-statute-him/its', 'and-his-statutes'), ('and-judgment-him/its', 'and-his-judgments'), ('and-commandment-him/its', 'and-his-commandments'), ('and-to-seed-them/their', 'and-to-their-seed'), ('the-Gilgal', 'Gilgal'), ('and-in-gate-you/your', 'and-on-your-gates'), ('and-in-go-you/your', 'and-when-you-walk'), ('in-house-you/your', 'in-your-house'), ('in-face-you/your (pl)', 'before-you'), ('in-midst', 'in-the-midst-of'), ('and-to-work/serve-him/its', 'and-to-serve-Him'), ('word/thing-me/my', 'my-words'), ('hind-part-you/your (pl)', 'after-you')]
# BY REFERENCE — the family mixed (a homograph, a verb read two ways, a noun singular and plural, God's "I" beside the store's "?"): the seat named (ONE HUNDRED AND FIFTY-EIGHT)
OVERRIDE_REF_SPEC = [(1, 'ושמרת', 'and-you-shall-keep', 0), (2, 'וידעתם', 'and-you-shall-know', 0), (2, 'היום', 'today', 0), (2, 'ידעו', 'known', 0), (2, 'ראו', 'seen', 0), (3, 'עשה', 'did', 0), (4, 'עשה', 'did', 0), (4, 'הציף', 'made-flow', 0), (4, 'מי', 'the-waters-of', 0), (4, 'ים', 'the-Sea-of', 0), (4, 'סוף', 'Reeds', 0), (4, 'ויאבדם', 'and-He-destroyed-them', 0), (4, 'היום', 'today', 0), (5, 'עשה', 'did', 0), (5, 'באכם', 'you-came', 0),
                     (6, 'עשה', 'did', 0), (6, 'פצתה', 'opened', 0), (7, 'הראת', 'that-have-seen', 0), (7, 'עשה', 'did', 0), (8, 'ושמרתם', 'and-you-shall-keep', 0), (8, 'אנכי', 'I', 0), (8, 'היום', 'today', 0), (8, 'תחזקו', 'you-may-be-strong', 0), (8, 'ובאתם', 'and-you-shall-go-in', 0), (8, 'וירשתם', 'and-you-shall-possess', 0), (8, 'הארץ', 'the-land', 0), (8, 'עברים', 'are-crossing', 0), (9, 'תאריכו', 'you-may-prolong', 0), (9, 'ימים', 'days', 0), (9, 'ארץ', 'a-land', 0),
                     (10, 'הארץ', 'the-land', 0), (10, 'בא', 'are-going-in', 0), (10, 'יצאתם', 'you-came-out', 0), (10, 'תזרע', 'you-sow', 0), (10, 'והשקית', 'and-you-watered', 0), (10, 'הירק', 'herbs', 0), (11, 'עברים', 'are-crossing', 0), (11, 'ארץ', 'a-land', 0), (11, 'הרים', 'hills', 0), (11, 'ובקעת', 'and-valleys', 0), (11, 'מים', 'water', 0), (12, 'ארץ', 'a-land', 0), (12, 'דרש', 'seeks-out', 0), (12, 'אתה', 'it', 0), (12, 'בה', 'on-it', 0), (12, 'השנה', 'the-year', 0), (12, 'שנה', 'the-year', 0),
                     (13, 'והיה', 'and-it-shall-be', 0), (13, 'שמע', 'hearken', 0), (13, 'תשמעו', 'you-hearken', 0), (13, 'אנכי', 'I', 0), (13, 'היום', 'today', 0), (13, 'נפשכם', 'your-soul', 0), (14, 'ונתתי', 'and-I-will-give', 0), (14, 'ואספת', 'and-you-shall-gather', 0), (15, 'ונתתי', 'and-I-will-give', 0), (15, 'ואכלת', 'and-you-shall-eat', 0), (16, 'השמרו', 'take-heed', 0), (16, 'יפתה', 'be-deceived', 0), (16, 'וסרתם', 'and-you-turn-aside', 0), (16, 'ועבדתם', 'and-serve', 0), (16, 'אלהים', 'gods', 0),
                     (17, 'אף', 'the-anger-of', 0), (17, 'בכם', 'against-you', 0), (17, 'יהיה', 'there-be', 0), (17, 'ואבדתם', 'and-you-shall-perish', 0), (17, 'מהרה', 'quickly', 0), (17, 'הארץ', 'the-land', 0), (17, 'נתן', 'gives', 0), (18, 'ושמתם', 'and-you-shall-put', 0), (18, 'נפשכם', 'your-soul', 0), (18, 'וקשרתם', 'and-bind', 0), (18, 'אתם', 'them', 0), (18, 'לאות', 'for-a-sign', 0), (18, 'ידכם', 'your-hand', 0), (18, 'והיו', 'and-they-shall-be', 0), (19, 'ולמדתם', 'and-teach', 0), (19, 'אתם', 'them', 0), (19, 'בם', 'of-them', 0), (19, 'בדרך', 'by-the-way', 0),
                     (20, 'ביתך', 'your-house', 0), (21, 'ירבו', 'may-be-multiplied', 0), (21, 'וימי', 'and-the-days-of', 0), (21, 'כימי', 'as-the-days-of', 0), (21, 'הארץ', 'the-land', 0), (22, 'כי', 'for', 0), (22, 'אם', 'if', 0), (22, 'שמר', 'diligently', 0), (22, 'אנכי', 'I', 0), (22, 'בו', 'to-Him', 0), (23, 'והוריש', 'and-He-will-dispossess', 0), (23, 'הגוים', 'the-nations', 0), (23, 'וירשתם', 'and-you-shall-possess', 0), (23, 'גוים', 'nations', 0), (23, 'גדלים', 'greater', 0), (23, 'מכם', 'than-you', 0),
                     (24, 'כף', 'the-sole-of', 0), (24, 'רגלכם', 'your-foot', 0), (24, 'בו', 'on-it', 0), (24, 'יהיה', 'shall-be', 0), (24, 'הנהר', 'the-river', 0), (24, 'נהר', 'the-river', 0), (24, 'האחרון', 'the-western', 0), (24, 'יהיה', 'shall-be', 1), (25, 'יתיצב', 'shall-stand', 0), (25, 'יתן', 'shall-put', 0), (25, 'פני', 'the-face-of', 0), (25, 'הארץ', 'the-land', 0), (25, 'תדרכו', 'you-tread', 0), (25, 'בה', 'on-it', 0), (25, 'דבר', 'He-spoke', 0), (26, 'ראה', 'See', 0), (26, 'אנכי', 'I', 0), (26, 'היום', 'today', 0), (26, 'ברכה', 'a-blessing', 0),
                     (27, 'הברכה', 'the-blessing', 0), (27, 'תשמעו', 'you-hearken', 0), (27, 'מצות', 'the-commandments-of', 0), (27, 'אנכי', 'I', 0), (27, 'היום', 'today', 0), (28, 'תשמעו', 'you-hearken', 0), (28, 'מצות', 'the-commandments-of', 0), (28, 'וסרתם', 'and-you-turn-aside', 0), (28, 'הדרך', 'the-way', 0), (28, 'אנכי', 'I', 0), (28, 'היום', 'today', 0), (28, 'אלהים', 'gods', 0), (28, 'ידעתם', 'known', 0), (29, 'והיה', 'and-it-shall-be', 0), (29, 'כי', 'when', 0), (29, 'יביאך', 'brings-you', 0), (29, 'הארץ', 'the-land', 0), (29, 'בא', 'are-going-in', 0), (29, 'ונתתה', 'and-you-shall-set', 0), (29, 'הברכה', 'the-blessing', 0), (29, 'הר', 'Mount', 0), (29, 'הקללה', 'the-curse', 0), (29, 'הר', 'Mount', 1),
                     (30, 'דרך', 'the-way-of', 0), (30, 'בארץ', 'in-the-land-of', 0), (30, 'הישב', 'who-dwells', 0), (30, 'בערבה', 'in-the-Arabah', 0), (30, 'אצל', 'beside', 0), (30, 'אלוני', 'the-terebinths-of', 0), (31, 'כי', 'for', 0), (31, 'עברים', 'are-crossing', 0), (31, 'לבא', 'to-go-in', 0), (31, 'לרשת', 'to-possess', 0), (31, 'הארץ', 'the-land', 0), (31, 'נתן', 'gives', 0), (31, 'וירשתם', 'and-you-shall-possess', 0), (31, 'אתה', 'it', 0), (31, 'וישבתם', 'and-you-shall-dwell', 0), (31, 'בה', 'in-it', 0), (32, 'ושמרתם', 'and-you-shall-keep', 0), (32, 'המשפטים', 'the-judgments', 0), (32, 'אנכי', 'I', 0), (32, 'היום', 'today', 0)]
OVERRIDE_REF3 = [(f'Deut.11.{v}:{sidx(11, v, tok, nth)}', new, tok) for v, tok, new, nth in OVERRIDE_REF_SPEC]
OVERRIDE_REF = [(k, v) for k, v, _ in OVERRIDE_REF3]
assert len(OVERRIDE_REF) == len({k for k, _ in OVERRIDE_REF}) == len(OVERRIDE_REF_SPEC) and len(OVERRIDE_GLOSS) == 64 and len({k for k, _ in OVERRIDE_GLOSS}) == 64, (len(OVERRIDE_REF), len(OVERRIDE_GLOSS))
assert all(g in GLOSS_FAMILY for g, _ in OVERRIDE_GLOSS) and all(sg(11, v, tok, nth) is not None for v, tok, _, nth in OVERRIDE_REF_SPEC)
ALREADY = {'?': '', 'abrupt': 'opposite', 'and-depress': 'and-bow-down', 'and-grave-them/their': 'and-write-them', 'and-have-affection-for': 'and-love', 'and-in-arise-you/your': 'and-when-you-rise', 'and-in-lie-down-you/your': 'and-when-you-lie-down', 'and-must-you/your': 'and-your-wine', 'and-powerful': 'and-mighty', 'and-sate': 'and-be-satisfied', 'commandment-me/my': 'my-commandments', 'door-post': 'doorposts', 'flow-freely': 'flowing', 'from-over': 'from-upon', 'hind-part': 'after', 'hinder': 'other', 'imbibe': 'drink', 'in-dwell/sit-you/your': 'when-you-sit', 'in-nearest-part': 'in-the-midst-of', 'in-pasture': 'in-the-wilderness', 'in-region-across': 'beyond', 'increase-you/your': 'your-grain', 'keep/guard-suffix': 'keep', 'like-as/which': 'as', 'magnitude-him/its': 'his-greatness', 'the-enactment': 'the-statutes', 'the-not': 'is-it-not', 'the-pasture': 'the-wilderness', 'the-seas': 'the-sea', 'the-stretch': 'the-outstretched', 'there-suffix': 'thither', 'to-fillet-for-the-forehead': 'for-frontlets', 'to-go': 'to-walk', 'to-have-affection-for': 'to-love', 'to-possess/inherit-her/its': 'to-possess-it', 'to-set': 'to-give'}
assert len(ALREADY) == 36
OV = open(f'{ROOT}/logic/glosses/word_gloss_overrides.yaml', encoding='utf-8').read()
PATCHED = 'THE DEUTERONOMY WALK sitting 9 (2026-09-20, Deuteronomy 11)' in OV
assert all(f'"{k}": "{v}"' in OV for k, v in ALREADY.items()) and all(f'"{k}": ' not in OV for k, _ in OVERRIDE_GLOSS if not PATCHED) and (PATCHED or '"Deut.11.' not in OV), [k for k, _ in OVERRIDE_GLOSS if f'"{k}": ' in OV]
if PATCHED: assert all(f'"{k}": "{v}"' in OV for k, v in OVERRIDE_REF) and all(f'"{k}": "{v}"' in OV for k, v in OVERRIDE_GLOSS), [k for k, v in OVERRIDE_REF + OVERRIDE_GLOSS if f'"{k}": "{v}"' not in OV][:6]
assert OV.count('  "Deut.10.22:6": "has-made-you"') == 1 and 'THE DEUTERONOMY WALK sitting 8 (2026-09-19, Deuteronomy 10)' in OV

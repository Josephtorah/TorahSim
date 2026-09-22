import os as _os
_ROOT = _os.path.normpath(_os.path.join(_os.path.dirname(_os.path.abspath(__file__)), '..', '..', '..'))   # THE PORTABLE REPO (2026-09-15): the repo root from this file's own place
#!/usr/bin/env python3
# THE DEUTERONOMY WALK, sitting 12 — CHAPTER 14, Deuteronomy 14:1-29 (2026-09-21; the owner: "Go" after 11b's tail; ONE RUN + ITS TAIL under THE COST RULES
# A-B-C — the rereads, the measurements, the ink, the design, the rows, the ledger, the clean point, the tail): THE INK of the chapter, computed from the Tanakh
# DB, the snapshot store and the shelf's own bytes — never typed. Sitting 11's form (ch13_ink.py): the generic helpers copied by derive_ch14_ink.py from that
# file by content markers, the constants and every assert chapter 14's own, typed FROM THE PRINTS (ch14_dump0.out, ch14_measure1.out). THE TWO DIVISIONS AGREE
# (29 = 29; the alignment the identity, cost 17) — THE CHAPTER IS TWENTY-NINE VERSES in both numberings. THE SPINE IS ON THE CHAPTER — FOURTEEN piskaot (97-110)
# with 107 rows, every head computed in chapter 14 (97 on 14:2 … 110 on 14:29; the heads NOT in verse order — 98 on 14:6 before 99 on 14:3), AND PISKA 96's TAIL
# (rows 9-12 on 14:1 — sitting 11 left them: 96:9 opens with 14:1's citation, 96:10 with its clause and Amos 9:6 alone, folded by the consonants; 96:11-12 by
# their citations), so ONE HUNDRED AND ELEVEN spine rows are read here; THREE rows elsewhere cite the chapter by the union of both files (76:7 flesh in milk at
# 12:23 — READ BEFORE at chapter 12's sitting, REREAD WHOLE; 228:5 the bird's nest at 22:7; 312:1 the LORD's portion at 32:9), NONE excluded. The parser
# MEASURED on every verse — TWO NUMBER VERSES (14:6 "two hoofs" [2], 14:28 "three years" [3]) and the STARRED TITHE TOKENS (14:22, 14:23, 14:28 — the number word
# "ten" inside "tithe", marked, no number read). THE STORE = THE DB at every verse (351 = 351; NO KETIV this chapter). The hand's facts as asserts, run all at
# once by assert_driver.py.
import json, os, re, html, sqlite3, sys, io, contextlib, unicodedata, subprocess
from collections import Counter
ROOT = _ROOT
sys.path.insert(0, f'{ROOT}/World/step9')
DATE = '2026-09-21'
CH = 14
UIDS = ['deu_14_food_tithe']
SPANS = {'deu_14_food_tithe': (14, 1, 29)}
PREFIX = {'deu_14_food_tithe': 'DV14'}
SPAN = [(14, v) for v in range(1, 30)]
PISKAOT = list(range(96, 111))   # THE SPINE ON THE CHAPTER: piska 96's tail (rows 9-12 on 14:1) and the fourteen piskaot 97-110 whose heads are in chapter 14 (the A print); 96 heads on 13:17, 111 on 15:1 after
HEADLESS = []
TAIL_PISKA = 96
SPINE_ROWS = {96: 12, 97: 5, 98: 6, 99: 2, 100: 3, 101: 10, 102: 1, 103: 10, 104: 10, 105: 19, 106: 6, 107: 16, 108: 2, 109: 12, 110: 5}   # rows per piska, both files (the I print and the splitter's) — 119, of which 96's first eight are chapter 13's
PREV_CHAPTER_ROWS = [(96, r) for r in range(1, 9)]   # piska 96's rows on 13:17-19 — read at chapter 13's sitting (deu_13_reeh_2026-09-21.md; asserted from the ledgers)
READ_ROWS = [(p, r) for p in PISKAOT for r in range(1, SPINE_ROWS[p] + 1) if (p, r) not in PREV_CHAPTER_ROWS]   # 111 — this ledger's spine rows
EXP2DB = {e: [e] for e in range(1, 30)}   # the identity — 29 = 29 (chapter 5 the book's one split)
DB2EXP = {d: e for e, ds in EXP2DB.items() for d in ds}
# the Hebrew's book-named citations of chapter 14 OUTSIDE the spine (the regex reads "(דברים יד ב)" etc.); 76:7 and 228:5 cite it in the English only
OUTSIDE_HE = [(312, 1, (14, 2))]
OUTSIDE = [(76, 7), (228, 5), (312, 1)]   # the THREE rows READ WHOLE: the union of both files beyond piska 96's tail and piskaot 97-110
EXCLUDED = []   # every outside citation genuine
INTERPOLATION = []
CITED = {(76, 7): [21], (228, 5): [11], (312, 1): [2]}
CITED_DB = {k: v[0] for k, v in CITED.items()}
PRIOR_READ = {(76, 7): ['deu_12_reeh_2026-09-20.md']}   # the one outside row read before (chapter 12's sitting, on 12:23 — "to include flesh in milk"; computed from the ledgers, asserted) — REREAD WHOLE here
HEADS_ON = {76: (12, 23), 228: (22, 7), 312: (32, 9)}
FRESH = [(228, 5), (312, 1)]
CREDITED = {}   # under THE WHOLE-ROW RULE no spine row is credited: the two reads before (104:8 at chapter 6's sitting — the kid in its mother's milk said three times; 106:5 at chapter 12's — the firstling whose year passed) are REREAD WHOLE here and marked so
TITLE = "Chapter 14 — You are children of the LORD your God: you shall not cut yourselves nor make a baldness between your eyes for the dead, for you are a holy people to the LORD your God, and the LORD has chosen you to be His treasured people from all the peoples on the face of the earth. You shall not eat any abomination. These are the beasts you may eat: the ox, the sheep, the goat, the hart, the gazelle, the roebuck, the wild goat, the pygarg, the antelope and the mountain-sheep — every beast that parts the hoof, cleft into two hoofs, and chews the cud; but not the camel, the hare and the rock-badger, which chew the cud but part not the hoof, nor the swine, which parts the hoof but chews not the cud — of their flesh you shall not eat and their carcass you shall not touch. Of all in the waters, what has fins and scales you may eat; what has not, you shall not. Every clean bird you may eat; these you shall not: the eagle, the ossifrage, the osprey, the glede, the kite, the vulture after its kind, every raven, the ostrich, the night-hawk, the sea-mew, the hawk, the little owl, the great owl, the horned owl, the pelican, the carrion-vulture, the cormorant, the stork, the heron, the hoopoe and the bat; every swarming thing that flies is unclean, it shall not be eaten; every clean fowl you may eat. You shall not eat any carcass: give it to the sojourner within your gates, or sell it to a foreigner, for you are a holy people to the LORD your God. You shall not boil a kid in its mother's milk. Tithe, you shall tithe all the yield of your seed year by year, and eat before the LORD your God in the place He shall choose the tithe of your grain, wine and oil and the firstlings of your herd and flock, that you may learn to fear the LORD all the days; and if the way is too long, because the place is too far, turn it into money, bind the money in your hand, go to the place and spend it on whatever your soul desires — oxen, sheep, wine, strong drink — and eat there before the LORD and rejoice, you and your household; and the Levite within your gates you shall not forsake, for he has no portion nor inheritance with you. At the end of three years bring out all the tithe of your produce of that year and lay it up within your gates, and the Levite, the sojourner, the fatherless and the widow shall come and eat and be satisfied, that the LORD your God may bless you in all the work of your hand"
OUT = f'{ROOT}/logic/oral_triage/deu_14_reeh_{DATE}.md'
db = sqlite3.connect(f'file:{ROOT}/Data/tanakh.sqlite?mode=ro', uri=True)
VC = dict(db.execute("SELECT chapter, COUNT(*) FROM verses WHERE book='Deut' GROUP BY chapter").fetchall())
NV = VC[CH]
# ---- THE HELPERS (ch13_ink.py's, copied by content markers) ----
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
# ---- THE INK'S HELPERS, THE DB AND THE STORE (ch13_ink.py's, the chapter substituted) ----
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
def W14(v): return words('Deut', 14, v)
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
for c, v, idx, hp, g in store.execute("SELECT v.chapter, v.verse, w.idx, w.he_plain, w.gloss FROM words w JOIN verses v ON w.verse_id=v.id WHERE v.book='Deut' AND v.chapter = 14 ORDER BY v.id, w.idx"):
    SG.setdefault((c, v), []).append((idx, hp.replace('/', ''), g))
def sg(c, v, tok, nth=0):
    hit = [g for _, hp, g in SG[(c, v)] if hp == tok]
    if len(hit) <= nth: raise KeyError((c, v, tok, nth))
    return hit[nth]
def sidx(c, v, tok, nth=0):
    hit = [i for i, hp, _ in SG[(c, v)] if hp == tok]
    assert len(hit) > nth, (c, v, tok, nth, hit)
    return hit[nth]
STORE_MISMATCH = [(c, v, n, len(by[('Deut', c, v)])) for c, v, n in store.execute("SELECT v.chapter, v.verse, COUNT(*) FROM words w JOIN verses v ON w.verse_id=v.id WHERE v.book='Deut' AND v.chapter=14 GROUP BY v.chapter, v.verse").fetchall() if n != len(by[('Deut', c, v)])]
import difflib
def SH(a, b_): return sum(s for _, _, s in difflib.SequenceMatcher(a=words(*a), b=words(*b_)).get_matching_blocks())
D14 = lambda v: ('Deut', 14, v)
# THE KIN FOUND BY COMPUTATION (the measure's A section, recomputed here so the asserts read the same instrument): the shared distinct tokens outside the stop list, the top eight, the three closest re-scored in order
STOP = set('את ואת אשר כל וכל על ועל אל ואל לא ולא כי אם יהוה אלהיך אלהיכם לך לכם בו שם שמה גם מן ממך עד הוא היא אתם אתה אנכי אני לו לה בכל כאשר כן הימים היום אלה האלה בארץ הארץ אשר ואם או פן ופן ואת זה וזה הם המה'.split())
ORD = {k: i for i, k in enumerate(by)}
TOK = {k: set(words(*k)) - STOP for k in by}
KINC = {}
for _v in range(1, NV + 1):
    _me = D14(_v); _t = TOK[_me]
    _sc = sorted(((len(_t & TOK[k]), k) for k in by if k != _me and len(_t & TOK[k]) >= 2), key=lambda x: (-x[0], ORD[x[1]]))[:8]
    KINC[_v] = [(f'{k[0]} {k[1]}:{k[2]}', n, SH(_me, k) if i < 3 else None) for i, (n, k) in enumerate(_sc)]
DT = ('Deut',)   # the measure's name for the book alone (the ink's helpers carry T, the Torah)
# ---- THE SHELF BY POSITION — the spine ON the chapter: fourteen piskaot 97-110 (every head in chapter 14, NOT in verse order) and piska 96's TAIL (rows 9-12 on 14:1); 96 heads on 13:17 before, 111 on 15:1 after; the two files' grains ----
assert NV == 29 and VC[13] == 19 and VC[5] == 33 and len(sif) == 357 and len(sif_he) == 357 and sum(len(s) for s in sif) == 2357 and sum(len(s) for s in sif_he) == 2357
HC = Counter(h[0] for h in heads.values() if h)
assert [p for p, h in heads.items() if h and h[0] == 14] == list(range(97, 111)) and HC[14] == 14 and sorted(HC.items())[:14] == [(1, 24), (3, 4), (6, 6), (11, 21), (12, 20), (13, 14), (14, 14), (15, 16), (16, 19), (17, 16), (18, 16), (19, 10), (20, 14), (21, 17)], sorted(HC.items())[:14]
assert {p: heads[p] for p in range(96, 112)} == {96: (13, 17), 97: (14, 2), 98: (14, 6), 99: (14, 3), 100: (14, 4), 101: (14, 6), 102: (14, 6), 103: (14, 11), 104: (14, 21), 105: (14, 22), 106: (14, 23), 107: (14, 24), 108: (14, 27), 109: (14, 28), 110: (14, 29), 111: (15, 1)}, {p: heads[p] for p in range(96, 112)}
assert [heads[p][1] for p in range(97, 111)] == [2, 6, 3, 4, 6, 6, 11, 21, 22, 23, 24, 27, 28, 29] and sorted({heads[p][1] for p in range(97, 111)}) == [2, 3, 4, 6, 11, 21, 22, 23, 24, 27, 28, 29]   # THE HEADS NOT IN VERSE ORDER — 98 on 14:6 sits before 99 on 14:3 and 100 on 14:4; three piskaot head on 14:6
# PISKA 96's TAIL IS THIS CHAPTER'S: its ninth row opens with the citation of 14:1, its tenth with 14:1's clause and Amos 9:6 alone (folded by the consonants), its eleventh and twelfth by their citations; rows 1-8 on 13:17-19 read at sitting 11
assert he_cites(Hb(96, 9))[:1] == [('דברים', 14, 1)] and HB0(96, 9).startswith('(דברים יד א) בנים אתם') and HB0(96, 10).startswith('לא תתגדדו') and HB0(96, 11).startswith('דבר אחר: לא תתגדדו') and HB0(96, 12).startswith('ולא תשימו קרחה') and '(Dt.14:1)' in E(96, 9) and '(Dt.14:1)' in E(96, 11) and '(Dt.14:1)' in E(96, 12) and re.findall(r'\(([A-Z][a-z]+\.? ?\d+:\d+(?:-\d+)?)\)', E(96, 10)) == ['Am.9:6']
assert HB0(96, 8).startswith('לעשות הישר בעיני') and he_cites(Hb(96, 1)) == [('דברים', 13, 17)] and len(READ_ROWS) == 111 and sum(SPINE_ROWS.values()) == 119 and len(PISKAOT) == 15 and READ_ROWS[:5] == [(96, 9), (96, 10), (96, 11), (96, 12), (97, 1)]
assert {p: (len(sif_he[p - 1]), len(sif[p - 1])) for p in PISKAOT} == {p: (n, n) for p, n in SPINE_ROWS.items()}
assert W14(1) == ['בנים', 'אתם', 'ליהוה', 'אלהיכם', 'לא', 'תתגדדו', 'ולא', 'תשימו', 'קרחה', 'בין', 'עיניכם', 'למת'] and 'לא תתגדדו' in HB0(96, 10) and 'אגדות' in HB0(96, 10)   # the consonant rule — 96:10 opens with 14:1's own words
CIT_HE = [(p, r, (14, c[2])) for p in range(1, 358) for r in range(1, len(sif_he[p - 1]) + 1) for c in he_cites(Hb(p, r)) if c[0] == 'דברים' and c[1] == 14]
CIT_EN = [(p, r, (14, int(m.group(2)))) for p in range(1, 358) for r in range(1, len(sif[p - 1]) + 1) for m in re.finditer(r'\((?:Deut(?:eronomy)?\.?|Dt\.?|Devarim) ?(14):(\d+)', E(p, r))]
assert len(CIT_HE) == 25 and len(CIT_EN) == 135, (len(CIT_HE), len(CIT_EN))
assert [(p, r, v) for p, r, v in CIT_HE if p not in PISKAOT] == OUTSIDE_HE and (96, 9, (14, 1)) in CIT_HE
SPINE_CITES_HE = [(p, r, v) for p, r, v in CIT_HE if p in PISKAOT]
assert len(SPINE_CITES_HE) == 24 and SPINE_CITES_HE[:4] == [(96, 9, (14, 1)), (97, 1, (14, 2)), (98, 1, (14, 6)), (98, 3, (14, 11))] and (103, 10, (14, 19)) in SPINE_CITES_HE and (103, 9, (14, 20)) in SPINE_CITES_HE and SPINE_CITES_HE[-3:] == [(109, 1, (14, 28)), (109, 10, (14, 29)), (110, 1, (14, 29))]   # 103's rows cite 14:20 before 14:19
UNION = sorted({(p, r) for p, r, _ in CIT_HE} | {(p, r) for p, r, _ in CIT_EN})
assert len(UNION) == 100 and sorted(set(UNION) - {(p, r) for p, r in UNION if p in range(97, 111)} - {(96, 9), (96, 11), (96, 12)}) == sorted(OUTSIDE + EXCLUDED) and len(OUTSIDE) == 3 and len([(p, r) for p, r in UNION if p in range(97, 111)]) == 94 and (96, 10) not in UNION
assert all(1 <= v <= 29 for _, _, (_, v) in CIT_HE + CIT_EN)   # no cited verse beyond the chapter's twenty-nine
assert [(p, r) for p in range(1, 358) for r in range(1, len(sif[p - 1]) + 1) if re.search(r'\((?:Ibid|ibid)\.? ?14:\d+\)', E(p, r))] == []   # no "ibid."
assert {p: heads[p] for p, _ in OUTSIDE} == HEADS_ON and all(heads[p] == HEADS_ON[p] for p, _ in OUTSIDE), {p: heads[p] for p, _ in OUTSIDE}
assert all(has_points(Hb(p, r)) for p, r in OUTSIDE) and all(has_points(Hb(p, r)) for p, r in READ_ROWS)
NOCITE = [(p, r) for p in range(97, 111) for r in range(1, SPINE_ROWS[p] + 1) if not he_cites(Hb(p, r)) and not re.findall(r'\([A-Z][a-z]+\.? ?\d+:\d+', E(p, r))]
assert NOCITE == [(98, 4), (100, 3), (104, 6), (105, 2), (110, 5)] and len(NOCITE) == 5, NOCITE
# THE THREE OUTSIDE ROWS: 76:7 (on 12:23 — "you shall not eat it" to include flesh in milk; the English cites 14:21) READ BEFORE at chapter 12; 228:5 (on 22:7 — the bird's nest, "send away the clean"; the English cites 14:11); 312:1 (on 32:9 — the LORD's portion is His people; the Hebrew cites 14:2)
assert he_cites(Hb(76, 7)) == [] and '(Dt.14:21)' in E(76, 7) and HB0(76, 7).startswith('לא תאכלנו') and 'בשר בחלב' in HB0(76, 7)
assert he_cites(Hb(228, 5)) == [('דברים', 22, 7)] and '(Dt.14:11)' in E(228, 5) and 'שלח תשלח' in HB0(228, 5)
assert he_cites(Hb(312, 1))[:1] == [('דברים', 32, 9)] and ('דברים', 14, 2) in he_cites(Hb(312, 1)) and '(Dt.14:2)' in E(312, 1) and HB0(312, 1).startswith('(דברים לב ט) כי חלק')
# THE PRIOR READS, computed from the ledgers (never typed): two reads of two spine rows (104:8 at chapter 6's sitting — the kid in its mother's milk said three times; 106:5 at chapter 12's — the firstling whose year passed), one of the outside rows (76:7 at chapter 12's); 96's first eight rows chapter 13's
TRI = f'{ROOT}/logic/oral_triage'
LED = {f: open(f'{TRI}/{f}', encoding='utf-8').read() for f in os.listdir(TRI) if f.endswith('.md') and os.path.isfile(f'{TRI}/{f}') and f'{TRI}/{f}' != OUT}
PRIOR = sorted({(f, int(a), int(b)) for f, t in LED.items() for a, b in re.findall(r'Sifrei Devarim (\d+):(\d+)', t)})
SPINE_PRIOR = [(f, p, r) for f, p, r in PRIOR if (p, r) in READ_ROWS]
assert SPINE_PRIOR == [('deu_06_vaetchanan_2026-09-17.md', 104, 8), ('deu_12_reeh_2026-09-20.md', 106, 5)] and len(PRIOR) == 770, (SPINE_PRIOR, len(PRIOR))
assert [(f, p, r) for f, p, r in PRIOR if (p, r) in PREV_CHAPTER_ROWS] == [('deu_13_reeh_2026-09-21.md', 96, r) for r in range(1, 9)] and [(f, p, r) for f, p, r in PRIOR if p == 96 and r >= 9] == []
assert [(f, p, r) for f, p, r in PRIOR if (p, r) in OUTSIDE] == [('deu_12_reeh_2026-09-20.md', 76, 7)] and PRIOR_READ == {(76, 7): ['deu_12_reeh_2026-09-20.md']}
assert sorted(f for f, t in LED.items() if re.search(r'^- Onkelos Deut 14:', t, re.M)) == []
NAMING = sorted(f for f, t in LED.items() if re.search(r'Deut(?:eronomy)? 14:\d+', t))
assert len(NAMING) == 16 and 'lev_11_animals_water_birds_2026-09-05.md' in NAMING and 'lev_21_priests_2026-09-05.md' in NAMING and 'num_30_vows_exam_2026-09-12.md' in NAMING, NAMING
assert sorted(f for f, t in LED.items() if re.search(r'^- Onkelos Deut (?:1[5-9]|2[0-6]):', t, re.M)) == [] and sorted(f for f, t in LED.items() if re.search(r'^- Onkelos (?:Josh|Judg|1Sam|2Sam|1Kgs|2Kgs) ', t, re.M)) == []   # NEVER READ AHEAD
# THE KIN'S READING (the counts computed from the ledgers): Leviticus 11 read at its sitting — 6 + 5 Onkelos rows in two ledgers; the cuts (Leviticus 19:27-28, 21:5), the holy people (7:6; Leviticus 20:26), the carcass and the torn (Leviticus 17:15, 22:8; Exodus 22:30), the kid (Exodus 23:19), the tithe (Leviticus 27; Numbers 18; chapter 12), the Levite's portion, the place formula
assert kinrows('lev_11_animals_water_birds_2026-09-05.md', r'Lev 11:[2-8]\b') == 2 and kinrows('lev_11_animals_water_birds_2026-09-05.md', r'Lev 11:1[3-9]\b') == 1 and kinrows('lev_11_carcass_swarm_close_2026-09-05.md', r'Lev 11:4[1-7]\b') == 1 and kinrows('lev_11_animals_water_birds_2026-09-05.md', r'Lev 11:(?:9|1[0-2])\b') == 1
assert kinrows('lev_19_kedoshim_2026-09-05.md', r'Lev (?:19:2[78]|21:5)\b') == 2 and kinrows('lev_21_priests_2026-09-05.md', r'Lev 21:5\b') == 1 and kinrows('deu_07_vaetchanan_ekev_2026-09-17.md', r'Deut 7:6\b') == 1 and kinrows('lev_20_sanctions_2026-09-05.md', r'Lev 20:26\b') == 1
assert kinrows('lev_17_18_blood_arayot_2026-09-05.md', r'Lev 17:15\b') == 1 and kinrows('lev_22_holy_food_offerings_2026-09-05.md', r'Lev 22:8\b') == 1 and kinrows('exo_22_property_social_2026-09-01.md', r'Exod 22:30\b') == 1 and kinrows('exo_23_justice_calendar_2026-09-01.md', r'Exod 23:19\b') == 1 and sum(kinrows(f, r'Exod 34:26\b') for f in LED) == 0   # 34:26 read through its spine before the Onkelos standing
assert kinrows('lev_27_valuations_2026-09-05.md', r'Lev 27:3[0-3]\b') == 4 and kinrows('num_18_priest_levite_dues_2026-09-10.md', r'Num 18:(?:2[1-9]|3[0-2])\b') == 12 and kinrows('deu_12_reeh_2026-09-20.md', r'Deut 12:(?:6|11|1[7-9])\b') == 5 and kinrows('deu_12_reeh_2026-09-20.md', r'Deut 12:(?:5|11|14|18|21|26)\b') == 6 and kinrows('deu_12_reeh_2026-09-20.md', r'Deut 12:(?:15|2[0-2])\b') == 4
assert kinrows('deu_10_ekev_2026-09-19.md', r'Deut 10:9\b') == 1 and kinrows('deu_12_reeh_2026-09-20.md', r'Deut 12:12\b') == 1 and kinrows('num_18_priest_levite_dues_2026-09-10.md', r'Num 18:(?:20|2[34])\b') == 3 and kinrows('deu_10_ekev_2026-09-19.md', r'Deut 10:18\b') == 1 and kinrows('lev_19_kedoshim_2026-09-05.md', r'Lev 19:10\b') == 1 and kinrows('lev_23_festivals_2026-09-05.md', r'Lev 23:22\b') == 1
assert sum(kinrows(f, r'Gen (?:28:22|14:20|7:[28])\b') for f in LED) == 0 and sum(kinrows(f, r'Exod 19:[56]\b') for f in LED) == 0 and sum(kinrows(f, r'Exod 23:1[01]\b') for f in LED) == 0   # Genesis and Exodus 19, 23:10-11 read through their spines before the Onkelos standing
# ---- THE TWO DIVISIONS AND THE VERSES ----
assert len(onk[13]) == 29 and len(onk_he[13]) == 29 and NV == 29 and [(c, len(onk_he[c - 1]), VC[c]) for c in range(1, 15) if len(onk_he[c - 1]) != VC[c]] == [(5, 30, 33)]
assert sum(len(W14(v)) for v in range(1, 30)) == 351 and {v: len(W14(v)) for v in (1, 2, 7, 21, 23, 24, 26, 29)} == {1: 12, 2: 19, 7: 26, 21: 23, 23: 25, 24: 23, 26: 22, 29: 24}
# ---- THE INK FACTS (the B print) — THE CHILDREN AND THE CUTS (14:1-2) ----
assert P('בנים', 'אתם', 'ליהוה') == ['Deut 14:1'] and P('בני', 'בכרי') == ['Exod 4:22'] and P('לא', 'תתגדדו') == ['Deut 14:1']   # "you are children of the LORD" ONE seat; "My son, My firstborn" Exodus 4:22
assert [s for s, x, m in LEMT('1413')] == ['1Kgs 18:28', 'Deut 14:1', 'Jer 5:7', 'Jer 16:6', 'Jer 41:5', 'Jer 47:5', 'Mic 4:14', 'Ps 94:21'] and [s for s, x, m in LEMT('1413') if m.startswith('HVr') or m.startswith('HC/Vrw')] == ['1Kgs 18:28', 'Deut 14:1', 'Jer 5:7', 'Jer 16:6', 'Jer 47:5', 'Mic 4:14']   # "cut yourselves" — the Torah's ONE seat; Baal's prophets at Carmel the run's case (1 Kings 18:28)
assert P('קרחה', 'בין', 'עיניכם') == ['Deut 14:1'] and len(LEMT('7144')) == 11 and [s for s, _, _ in LEMT('7144', books=T)] == ['Deut 14:1', 'Lev 21:5'] and P('בין', 'עיניכם') == ['Deut 11:18', 'Deut 14:1'] and P('בין', 'עיניך') == ['Deut 6:8', 'Exod 13:16', 'Exod 13:9'] and U('למת') == ['Deut 14:1', 'Deut 26:14', 'Jer 22:10']   # "baldness" the Torah's two (the priests' 21:5 and this); "between your eyes" THE FRONTLETS' PHRASE (6:8, 11:18; Exodus 13:9, 16) — its fifth seat here; "for the dead" the Torah's two (26:14 ahead)
assert P('ושרט', 'לנפש') == ['Lev 19:28'] and P('קרחה', 'בראשם') == ['Lev 21:5'] and [s for s, _, _ in LEMT('8295')] == ['Lev 21:5', 'Zech 12:3', 'Zech 12:3']   # Leviticus 19:28's cut "for a soul" and 21:5's priests — the kin by CALL
assert P('כי', 'עם', 'קדוש', 'אתה', 'ליהוה', 'אלהיך') == ['Deut 14:2', 'Deut 14:21', 'Deut 7:6'] and P('עם', 'קדוש') == ['Deut 14:2', 'Deut 14:21', 'Deut 7:6'] and P('ובך', 'בחר', 'יהוה') == ['Deut 14:2'] and P('להיות', 'לו', 'לעם', 'סגלה') == ['Deut 14:2', 'Deut 26:18', 'Deut 7:6'] and P('מכל', 'העמים', 'אשר', 'על', 'פני', 'האדמה') == ['Deut 14:2', 'Deut 7:6']   # "a holy people" THREE seats in the Bible — 7:6, 14:2, 14:21: the chapter holds two; 14:2 IS 7:6 with the Name's second "your God" dropped (18 of 19 tokens in order)
assert [s for s, _, _ in LEMT('5459')] == ['1Chr 29:3', 'Deut 7:6', 'Deut 14:2', 'Deut 26:18', 'Eccl 2:8', 'Exod 19:5', 'Mal 3:17', 'Ps 135:4'] and SH(D14(2), ('Deut', 7, 6)) == 18 and SH(D14(2), D14(21)) == 6 and SH(D14(21), ('Deut', 7, 6)) == 6   # "treasure" eight in the Bible, Exodus 19:5 the first; Psalm 135:4 the shelf's own citation at 97:3
# ---- THE ABOMINATION AND THE TEN BEASTS (14:3-5) ----
assert P('לא', 'תאכל', 'כל', 'תועבה') == ['Deut 14:3'] and [s for s, x in [(s, x) for s, x, _ in LEMT('8441', books=DT)] if s.startswith('Deut 14:')] == ['Deut 14:3'] and len(LEMT('8441', books=DT)) == 17 and P('תועבת', 'יהוה', 'אלהיך') == ['Deut 17:1', 'Deut 22:5', 'Deut 23:19', 'Deut 25:16', 'Deut 7:25']   # "abomination" the chapter's one of the book's seventeen; 17:1's blemished offering the twin the shelf reads (99:2)
assert [s for s, _, _ in LEMT('8262')] == ['Deut 7:26', 'Deut 7:26', 'Lev 11:11', 'Lev 11:13', 'Lev 11:43', 'Lev 20:25', 'Ps 22:25'] and len(LEMT('8263')) == 11 and [s for s, _, _ in LEMT('8263') if s.startswith('Lev 11:')] == ['Lev 11:10', 'Lev 11:11', 'Lev 11:12', 'Lev 11:13', 'Lev 11:20', 'Lev 11:23', 'Lev 11:41', 'Lev 11:42']   # Leviticus 11's word is "detestable" (eight seats), this chapter's "abomination" and "unclean" — THE TWIN CHAPTER'S VOCABULARY DIFFERS
assert P('זאת', 'הבהמה', 'אשר', 'תאכלו') == ['Deut 14:4'] and P('זאת', 'החיה', 'אשר', 'תאכלו') == ['Lev 11:2'] and [v for v in range(1, 30) if W14(v)[0] == 'זאת'] == [4] and [v for v in range(1, 30) if W14(v)[0] in ('אלה', 'ואלה', 'וזאת', 'זה', 'וזה')] == [12]   # "this is the beast" against Leviticus 11:2's "this is the living thing" — the list's header; "and this is what you shall not eat" at 14:12 the birds' header
assert P('שור', 'שה', 'כשבים', 'ושה', 'עזים') == ['Deut 14:4'] and P('איל', 'וצבי') == ['Deut 14:5'] and P('כצבי', 'וכאיל') == ['Deut 12:15', 'Deut 15:22'] and U('יחמור', 'ויחמור') == ['1Kgs 5:3', 'Deut 14:5'] and U('אקו', 'ואקו') == ['Deut 14:5'] and U('זמר', 'וזמר') == ['Deut 14:5'] and U('תאו', 'ותאו', 'תוא', 'כתוא') == ['Deut 14:5', 'Ezek 40:21', 'Ezek 40:29', 'Ezek 40:33', 'Ezek 40:36', 'Isa 51:20'] and 'Gen 36:21' in U('דישן', 'ודישן', 'דישון')   # THE SEVEN WILD: the roebuck at Solomon's table (1 Kings 5:3), the wild goat and the mountain-sheep hapax, the antelope Isaiah's net (its letters Ezekiel 40's cells — a homograph), the pygarg a Horite's name (Genesis 36) — THE TEN NAMED HERE AND NOT IN LEVITICUS 11
assert SH(D14(5), ('1Kgs', 5, 3)) == 2 and KINC[5] == [('1Kgs 5:3', 2, 2)] and KINC[4][0] == ('Lev 11:2', 3, 3) and KINC[2][0] == ('Deut 7:6', 11, 18) and KINC[3] == [] and KINC[11] == [] and KINC[17] == [] and KINC[18] == []   # THE KIN BY COMPUTATION: 14:5's one kin in the Bible is Solomon's daily provision; 14:3, 11, 17, 18 have none
# ---- THE TWO SIGNS AND THE FOUR EXCEPTIONS (14:6-8) — LEVITICUS 11 DIFFED ----
assert P('מפרסת', 'פרסה', 'ושסעת', 'שסע') == ['Deut 14:6', 'Lev 11:3'] and P('שתי', 'פרסות') == ['Deut 14:6'] and U('השסועה', 'שסועה') == ['Deut 14:7'] and P('מפרסת', 'פרסה') == ['Deut 14:6', 'Lev 11:26', 'Lev 11:3'] and P('מעלת', 'גרה') == ['Deut 14:6', 'Lev 11:3', 'Lev 11:6'] and P('ממעלי', 'הגרה') == ['Deut 14:7', 'Lev 11:4']   # "two hoofs" ONE seat (the number the parser reads); "the cleft one" ONE seat (14:7 — the shelf's creature, Chullin 60b at the exam)
assert SH(D14(6), ('Lev', 11, 3)) == 9 and SH(D14(7), ('Lev', 11, 4)) == 16 and SH(D14(8), ('Lev', 11, 7)) == 10 and SH(D14(9), ('Lev', 11, 9)) == 12 and SH(D14(15), ('Lev', 11, 16)) == 10 and W14(15) == words('Lev', 11, 16)   # THE TWIN CHAPTER: 14:6 is 11:3 with "two hoofs" for "hoofs"; 14:7 folds 11:4-6's three into one; 14:15 IS 11:16 to the letter
assert P('הגמל', 'ואת', 'הארנבת', 'ואת', 'השפן') == ['Deut 14:7'] and U('החזיר', 'חזיר') == ['Deut 14:8', 'Isa 65:4', 'Isa 66:17', 'Isa 66:3', 'Lev 11:7', 'Neh 10:21', 'Prov 11:22', 'Ps 80:14'] and P('טמא', 'הוא', 'לכם') == ['Deut 14:10', 'Deut 14:19', 'Deut 14:8', 'Lev 11:38', 'Lev 11:4', 'Lev 11:5', 'Lev 11:7'] and P('טמאים', 'הם', 'לכם') == ['Deut 14:7', 'Lev 11:26', 'Lev 11:27', 'Lev 11:8'] and P('מבשרם', 'לא', 'תאכלו', 'ובנבלתם', 'לא', 'תגעו') == ['Deut 14:8', 'Lev 11:8']   # the three chewers in one verse; the swine the Torah's two; "of their flesh … their carcass" 11:8's clause verbatim
# ---- THE WATER, THE BIRDS, THE SWARMING FOWL (14:9-20) ----
assert P('סנפיר', 'וקשקשת') == ['Deut 14:10', 'Deut 14:9', 'Lev 11:10', 'Lev 11:12', 'Lev 11:9'] and P('כל', 'צפור', 'טהרה', 'תאכלו') == ['Deut 14:11'] and P('כל', 'עוף', 'טהור', 'תאכלו') == ['Deut 14:20'] and P('וזה', 'אשר', 'לא', 'תאכלו', 'מהם') == ['Deut 14:12'] and P('ואת', 'אלה', 'תשקצו', 'מן', 'העוף') == ['Lev 11:13']   # the two frames of the birds' list — "every clean bird" before, "every clean fowl" after: THE PERMITTED BIRDS HAVE NO SIGN IN THE INK (the exam's four signs from the shelf)
assert U('והראה') == ['Deut 14:13', 'Eccl 2:24', 'Lev 13:49'] and U('והדאה', 'הדאה', 'דאה', 'דיה', 'והדיה', 'הדיה') == ['Deut 14:13', 'Lev 11:14'] and W14(13) == ['והראה', 'ואת', 'האיה', 'והדיה', 'למינה'] and words('Lev', 11, 14) == ['ואת', 'הדאה', 'ואת', 'האיה', 'למינה']   # THE RA'AH AND THE DA'AH — resh for dalet, one letter (the bird's letters are the verb "see" at Leviticus 13:49 and Ecclesiastes 2:24 — the shelf's own reading of the name, a homograph in the ink); 14:13's three names against 11:14's two: the dayyah added
assert sum(1 for v in range(12, 19) for x in W14(v) if x.startswith('למינ')) == 4 and sum(1 for v in range(13, 20) for x in words('Lev', 11, v) if x.startswith('למינ')) == 4 and W14(16) == ['את', 'הכוס', 'ואת', 'הינשוף', 'והתנשמת'] and words('Lev', 11, 17) == ['ואת', 'הכוס', 'ואת', 'השלך', 'ואת', 'הינשוף'] and W14(17) == ['והקאת', 'ואת', 'הרחמה', 'ואת', 'השלך']   # the order of the names differs at 14:16-17 (the shalach moved, the tinshemet moved, the racham spelled rachamah)
assert P('וכל', 'שרץ', 'העוף', 'טמא', 'הוא', 'לכם') == ['Deut 14:19'] and P('שרץ', 'העוף') == ['Deut 14:19', 'Lev 11:20', 'Lev 11:21', 'Lev 11:23'] and [(x, m) for x, m in by[('Deut', 14, 19)] if x == 'יאכלו'] == [('יאכלו', 'HVNi3mp')] and 'הארבה' in words('Lev', 11, 22) and not any('ארבה' in x for v in range(1, 30) for x in W14(v))   # "they shall not be eaten" the chapter's one third-person form; LEVITICUS 11:21-22'S LOCUSTS ARE NOT IN THIS CHAPTER (the exam's question — Chullin 65a)
assert SH(D14(11), D14(20)) == 2 and P('כל', 'אשר', 'לו', 'סנפיר', 'וקשקשת') == ['Deut 14:9', 'Lev 11:9'] and len([1 for v in range(1, 48) for x in words('Lev', 11, v) if x in ('שקץ', 'ושקץ')]) == 8
# ---- THE CARCASS, THE SOJOURNER AND THE KID (14:21) ----
assert P('לא', 'תאכלו', 'כל', 'נבלה') == ['Deut 14:21'] and [s for s, x in [(s, x) for s, x, _ in LEMT('5038', books=T)] if s.startswith('Deut')] == ['Deut 14:8', 'Deut 14:21', 'Deut 21:23', 'Deut 28:26'] and P('לגר', 'אשר', 'בשעריך', 'תתננה', 'ואכלה') == ['Deut 14:21'] and P('לגר', 'אשר', 'בשעריך') == ['Deut 14:21'] and P('הגר', 'אשר', 'בשעריך') == [] and U('לנכרי') == ['Deut 14:21', 'Deut 23:21']   # "to the sojourner within your gates" ONE seat; "to a foreigner" the Torah's two (23:21's interest ahead)
assert words('Lev', 17, 15)[:5] == ['וכל', 'נפש', 'אשר', 'תאכל', 'נבלה'] and words('Exod', 22, 30)[-4:] == ['תאכלו', 'לכלב', 'תשלכון', 'אתו'] and words('Lev', 22, 8)[:4] == ['נבלה', 'וטרפה', 'לא', 'יאכל'] and SH(D14(21), ('Lev', 17, 15)) == 1 and SH(D14(21), ('Exod', 22, 30)) == 2   # the carcass's three kin verses — none shares a clause with 14:21: THE CARCASS GIVEN, NOT CAST TO THE DOG
assert P('לא', 'תבשל', 'גדי', 'בחלב', 'אמו') == ['Deut 14:21', 'Exod 23:19', 'Exod 34:26'] and words('Exod', 23, 19) == words('Exod', 34, 26) and SH(D14(21), ('Exod', 23, 19)) == 6 and [s for s, _, _ in LEMT('1423', books=T)] == ['Deut 14:21', 'Exod 23:19', 'Exod 34:26', 'Gen 27:9', 'Gen 27:16', 'Gen 38:17', 'Gen 38:20', 'Gen 38:23'] and [v for v in range(1, 30) if 'קדוש' in W14(v)] == [2, 21]   # THE KID IN ITS MOTHER'S MILK — the third and last seat (Exodus 23:19 and 34:26 identical verses); "a holy people" twice in the chapter, the clause before it
assert [(v, x, m) for v in range(1, 30) for x, m in by[('Deut', 14, v)] if m and re.match(r'^H(?:C/)?V.a$', m)] == [(21, 'מכר', 'HVqa'), (22, 'עשר', 'HVpa')]   # THE INFINITIVE ABSOLUTES: "sell" at 14:21 (the tagger's reading of מכר) and "tithe" at 14:22
# ---- THE TITHE AND THE PLACE (14:22-23) ----
assert P('עשר', 'תעשר') == ['Deut 14:22'] and [(s, x) for s, x, _ in LEMT('6237')] == [('1Sam 8:15', 'יעשר'), ('1Sam 8:17', 'יעשר'), ('Deut 14:22', 'עשר'), ('Deut 14:22', 'תעשר'), ('Deut 26:12', 'לעשר'), ('Gen 28:22', 'עשר'), ('Gen 28:22', 'אעשרנו'), ('Neh 10:38', 'המעשרים'), ('Neh 10:39', 'בעשר')] and P('את', 'כל', 'תבואת', 'זרעך') == ['Deut 14:22'] and P('היצא', 'השדה', 'שנה', 'שנה') == ['Deut 14:22'] and P('שנה', 'שנה') == ['Deut 14:22']   # "TITHE, YOU SHALL TITHE" — the verb's doubling ONE seat, Jacob's vow (Genesis 28:22) the form's first seat and the king's tithe (1 Samuel 8) the run's; "year by year" ONE seat (the shelf: not from one year on another)
assert [(s, x) for s, x, _ in LEMT('4643', books=T)][:8] == [('Deut 12:6', 'מעשרתיכם'), ('Deut 12:11', 'מעשרתיכם'), ('Deut 12:17', 'מעשר'), ('Deut 14:23', 'מעשר'), ('Deut 14:28', 'מעשר'), ('Deut 26:12', 'מעשר'), ('Deut 26:12', 'המעשר'), ('Gen 14:20', 'מעשר')] and len(LEMT('4643', books=T)) == 17   # "the tithe" the Torah's seventeen tokens — Abraham's, Leviticus 27's, Numbers 18's, chapter 12's, this chapter's two, 26:12's two
assert P('במקום', 'אשר', 'יבחר', books=DT) == ['Deut 12:14', 'Deut 12:18', 'Deut 14:23', 'Deut 15:20', 'Deut 16:11', 'Deut 16:15', 'Deut 16:16', 'Deut 16:2', 'Deut 16:7', 'Deut 23:17', 'Deut 31:11'] and P('לשכן', 'שמו', 'שם') == ['Deut 12:11', 'Deut 14:23', 'Deut 16:11', 'Deut 16:2', 'Deut 16:6', 'Deut 26:2'] and P('לשום', 'שמו', 'שם') == ['Deut 12:21', 'Deut 14:24'] and P('ואכלת', 'לפני', 'יהוה', 'אלהיך') == ['Deut 14:23']   # THE PLACE FORMULA at its fourth and fifth seats (14:23 "to cause His name to dwell", 14:24 "to put His name") — chapter 12's two forms both reused
assert P('מעשר', 'דגנך', 'תירשך', 'ויצהרך') == ['Deut 14:23'] and P('דגנך', 'ותירשך', 'ויצהרך') == ['Deut 11:14', 'Deut 12:17', 'Deut 7:13'] and P('דגנך', 'תירשך', 'ויצהרך') == ['Deut 14:23', 'Deut 18:4'] and P('ובכרת', 'בקרך', 'וצאנך') == ['Deut 12:17', 'Deut 14:23'] and SH(D14(23), ('Deut', 12, 17)) == 6   # 12:17's list said again with the firstlings — the second tithe and the firstling eaten at the place
assert P('למען', 'תלמד', 'ליראה', 'את', 'יהוה', 'אלהיך') == ['Deut 14:23'] and P('ליראה', 'את', 'יהוה') == ['Deut 10:12', 'Deut 14:23', 'Deut 17:19', 'Deut 31:13', 'Deut 6:24'] and KINC[23][0] == ('Deut 12:17', 6, 6) and KINC[23][1] == ('Deut 16:11', 5, 9)   # "learn to fear" — 4:10's and 17:19's kin; the closest verse in order 16:11's rejoicing
# ---- THE WAY, THE MONEY AND THE REJOICING (14:24-26) ----
assert P('וכי', 'ירבה', 'ממך', 'הדרך') == ['Deut 14:24'] and P('ירבה', 'הדרך') == ['Deut 19:6'] and P('כי', 'ירחק', 'ממך', 'המקום') == ['Deut 12:21', 'Deut 14:24'] and P('כי', 'יברכך', 'יהוה', 'אלהיך') == ['Deut 14:24', 'Deut 16:15'] and [x for x in W14(24) if x in ('כי', 'וכי')] == ['וכי', 'כי', 'כי', 'כי'] and SH(D14(24), ('Deut', 12, 21)) == 12   # THE WAY TOO LONG — 19:6's refuge road the twin; "the place too far" 12:21's clause verbatim (twelve tokens in order): THE FAR PLACE RELEASES THE FLESH THERE AND THE MONEY HERE; four "when/for/because" in one verse
assert P('ונתתה', 'בכסף') == ['Deut 14:25'] and P('וצרת', 'הכסף', 'בידך') == ['Deut 14:25'] and 'Gen 42:35' in U('וצרת', 'צרור', 'ויצר', 'צררו', 'צרר', 'ויצרו') and '2Kgs 5:23' in U('וצרת', 'צרור', 'ויצר', 'צררו', 'צרר', 'ויצרו') and P('והלכת', 'אל', 'המקום', 'אשר', 'יבחר', 'יהוה', 'אלהיך', 'בו') == ['Deut 14:25']   # "bind up the money in your hand" ONE seat (the bundles of Genesis 42:35, Naaman's two talents); THE REDEMPTION INTO MONEY — the shelf's silver with a form (Mishnah Maaser Sheni at the exam)
assert P('בכל', 'אשר', 'תאוה', 'נפשך') == ['1Kgs 11:37', '2Sam 3:21', 'Deut 14:26'] and P('בכל', 'אות', 'נפשך') == ['Deut 12:15', 'Deut 12:20', 'Deut 12:21'] and P('בבקר', 'ובצאן', 'וביין', 'ובשכר') == ['Deut 14:26'] and [(s, x) for s, x, _ in LEMT('7941', books=T)] == [('Deut 14:26', 'ובשכר'), ('Deut 29:5', 'ושכר'), ('Lev 10:9', 'ושכר'), ('Num 6:3', 'ושכר'), ('Num 6:3', 'שכר'), ('Num 28:7', 'שכר')] and P('ובכל', 'אשר', 'תשאלך', 'נפשך') == ['Deut 14:26']   # "whatever your soul desires" — chapter 12's noun three times, this chapter's verb once (Jeroboam's and Abner's the Prophets' two); "strong drink" the Torah's six — the priests' bar, the Nazirite's, the libation's, and HERE PERMITTED
assert P('ושמחת', 'אתה', 'וביתך') == ['Deut 14:26'] and U('ושמחת', 'ושמחתם', books=DT) == ['Deut 12:12', 'Deut 12:18', 'Deut 12:7', 'Deut 14:26', 'Deut 16:11', 'Deut 16:14', 'Deut 26:11', 'Deut 27:7'] and P('ואכלת', 'שם', 'לפני', 'יהוה', 'אלהיך') == ['Deut 14:26'] and KINC[26][0] == ('Deut 27:7', 3, 5)   # "rejoice, you and your household" ONE seat — the book's eight rejoicings, 12:7's "you and your households" the first
# ---- THE LEVITE, THE THIRD YEAR AND THE FOUR (14:27-29) ----
assert P('והלוי', 'אשר', 'בשעריך', 'לא', 'תעזבנו') == ['Deut 14:27'] and P('הלוי', 'אשר', 'בשעריך') == [] and P('והלוי', 'אשר', 'בשעריך') == ['Deut 12:18', 'Deut 14:27', 'Deut 16:11'] and words('Deut', 12, 19) == ['השמר', 'לך', 'פן', 'תעזב', 'את', 'הלוי', 'כל', 'ימיך', 'על', 'אדמתך'] and SH(D14(27), ('Deut', 12, 19)) == 0 and SH(D14(27), ('Deut', 12, 12)) == 7   # 12:19's "lest you forsake the Levite" said again in a new form (no token in order); 12:12's "no portion nor inheritance" the clause reused
assert P('כי', 'אין', 'לו', 'חלק', 'ונחלה', 'עמך') == ['Deut 14:27', 'Deut 14:29'] and P('חלק', 'ונחלה') == ['Deut 10:9', 'Deut 12:12', 'Deut 14:27', 'Deut 14:29', 'Deut 18:1', 'Gen 31:14'] and P('אין', 'לו', 'חלק', 'ונחלה') == ['Deut 12:12', 'Deut 14:27', 'Deut 14:29']   # "portion and inheritance" the Bible's six — Rachel and Leah's the first (Genesis 31:14), the Levite's five (10:9, 12:12, 14:27, 14:29, 18:1)
assert P('מקצה', 'שלש', 'שנים') == ['2Kgs 18:10', 'Deut 14:28'] and U('מקצה', 'מקץ', books=DT) == ['Deut 13:8', 'Deut 14:28', 'Deut 15:1', 'Deut 28:49', 'Deut 28:64', 'Deut 31:10', 'Deut 9:11'] and P('מקץ', 'שבע', 'שנים') == ['Deut 15:1', 'Deut 31:10', 'Jer 34:14'] and P('מעשר', 'תבואתך') == ['Deut 14:28', 'Deut 26:12'] and P('בשנה', 'ההוא') == ['Deut 14:28', 'Gen 26:12', 'Gen 47:17'] and U('והנחת', 'והנחתו', books=DT) == ['Deut 14:28', 'Deut 26:10']   # "AT THE END OF THREE YEARS" — Samaria's fall (2 Kings 18:10) the phrase's one kin; 15:1's "at the end of seven" ahead; "the tithe of your produce" 26:12's clause — THE THIRD YEAR'S TITHE, 26:12 its confession
assert words('Deut', 26, 12) == ['כי', 'תכלה', 'לעשר', 'את', 'כל', 'מעשר', 'תבואתך', 'בשנה', 'השלישת', 'שנת', 'המעשר', 'ונתתה', 'ללוי', 'לגר', 'ליתום', 'ולאלמנה', 'ואכלו', 'בשעריך', 'ושבעו'] and SH(D14(28), ('Deut', 26, 12)) == 6 and KINC[28][0] == ('Deut 26:12', 4, 6)
assert P('והגר', 'והיתום', 'והאלמנה') == ['Deut 14:29', 'Deut 16:11', 'Deut 16:14'] and P('לגר', 'ליתום', 'ולאלמנה') == ['Deut 24:19', 'Deut 24:20', 'Deut 24:21', 'Deut 26:12'] and P('ואכלו', 'ושבעו') == ['Deut 14:29'] and P('ובא', 'הלוי') == ['Deut 14:29']   # THE FOUR AT THE GATE — the formula's first seat (16:11, 16:14 ahead; 24:19-21 and 26:12 the "to" form); "eat and be satisfied" ONE seat in this form
assert P('למען', 'יברכך', 'יהוה', 'אלהיך', 'בכל', 'מעשה', 'ידך') == ['Deut 14:29'] and P('בכל', 'מעשה', 'ידך', books=DT) == ['Deut 14:29', 'Deut 2:7', 'Deut 30:9'] and P('בכל', 'מעשה', 'ידיך', books=DT) == ['Deut 24:19'] and SH(D14(29), ('Deut', 24, 19)) == 7 and KINC[29][0] == ('Deut 14:27', 5, 6)   # "that the LORD may bless you in all the work of your hand" — 24:19's forgotten sheaf the twin (seven tokens in order); 2:7's the first
# ---- THE REGISTER (the D print) ----
NUM = {v: (sum(1 for _, m in by[('Deut', 14, v)] if m and '2mp' in m), sum(1 for _, m in by[('Deut', 14, v)] if m and '2ms' in m)) for v in range(1, 30)}
assert [v for v, (p, s) in NUM.items() if s and not p] == [2, 3, 22, 23, 24, 25, 26, 27, 28, 29] and [v for v, (p, s) in NUM.items() if p and not s] == [1, 4, 6, 7, 8, 9, 10, 11, 12, 19, 20] and [v for v, (p, s) in NUM.items() if p and s] == [21] and [v for v, (p, s) in NUM.items() if not p and not s] == [5, 13, 14, 15, 16, 17, 18]   # THE REGISTER SPLITS THE CHAPTER IN TWO — the food laws PLURAL (14:1, 4-20), the tithe SINGULAR (14:22-29), 14:2-3 singular and 14:21 both (the carcass plural, the sojourner and the kid singular)
assert NUM[1] == (5, 0) and NUM[21] == (1, 5) and NUM[23] == (0, 9) and NUM[26] == (0, 9)
assert [v for v in range(1, 30) if any(m and re.search(r'1c[sp]', m) and m.startswith('HV') for _, m in by[('Deut', 14, v)])] == [] and [v for v in range(1, 30) if any(m and re.search(r'^HV..v', m) for _, m in by[('Deut', 14, v)])] == [] and [v for v in range(1, 30) if any(m and re.search(r'V.w', m) for _, m in by[('Deut', 14, v)])] == [] and [v for v in range(1, 30) if 'לאמר' in W14(v)] == []   # no first person, no imperative, no narrative verb, no "saying", no divine frame — MOSES' VOICE ALONE, and Moses never named
assert {v: [x for x in W14(v) if x in ('כי', 'וכי', 'אם', 'ואם', 'או', 'פן', 'ופן')] for v in range(1, 30) if any(x in ('כי', 'וכי', 'אם', 'ואם', 'או', 'פן', 'ופן') for x in W14(v))} == {2: ['כי'], 7: ['כי'], 8: ['כי'], 21: ['או', 'כי'], 24: ['וכי', 'כי', 'כי', 'כי'], 27: ['כי'], 29: ['כי']} and [v for v in range(1, 30) if W14(v)[0] in ('כי', 'וכי')] == [2, 24]   # NO "IF" IN THE CHAPTER — the one case on "when" (14:24 the way too long); the eight כי the reasons ("for")
assert {v: sum(1 for x in W14(v) if x in ('לא', 'ולא')) for v in range(1, 30) if any(x in ('לא', 'ולא') for x in W14(v))} == {1: 2, 3: 1, 7: 2, 8: 3, 10: 1, 12: 1, 19: 1, 21: 2, 24: 1, 27: 1} and sum(1 for v in range(1, 30) for x in W14(v) if x in ('תאכלו', 'תאכל', 'ואכלת')) == 14   # fifteen negations in ten verses; "you shall eat" fourteen times
assert {v: [x for x in W14(v) if x in ('טמא', 'טמאים', 'הטמא')] for v in range(1, 30) if any(x in ('טמא', 'טמאים', 'הטמא') for x in W14(v))} == {7: ['טמאים'], 8: ['טמא'], 10: ['טמא'], 19: ['טמא']} and {v: [x for x in W14(v) if x in ('טהור', 'טהרה')] for v in range(1, 30) if any(x in ('טהור', 'טהרה') for x in W14(v))} == {11: ['טהרה'], 20: ['טהור']} and [v for v in range(1, 30) if 'בשעריך' in W14(v)] == [21, 27, 28, 29] and len(U('בשעריך', books=DT)) == 16
assert [v for v in range(1, 30) if 'ליהוה' in W14(v)] == [1, 2, 21] and sum(1 for v in range(1, 30) for x in W14(v) if x == 'יהוה') == 8 and [v for v in range(1, 30) if any(W14(v)[i:i + 2] == ['יהוה', 'אלהיך'] for i in range(len(W14(v)) - 1))] == [23, 24, 25, 26, 29] and [(v, x) for v in range(1, 30) for x in W14(v) if x in ('משה', 'ישראל', 'מצרים')] == []   # THE NAME eleven tokens; "the LORD your God" singular five times, plural never; Israel, Egypt, Moses never named
assert {v: [x for x, m in by[('Deut', 14, v)] if m and re.search(r'V.q', m)] for v in (23, 25, 26, 28, 29)} == {23: ['ואכלת'], 25: ['ונתתה', 'וצרת', 'והלכת'], 26: ['ונתתה', 'ואכלת', 'ושמחת'], 28: ['והנחת'], 29: ['ובא', 'ואכלו', 'ושבעו']} and [(x, m) for x, m in by[('Deut', 14, 22)] if x == 'היצא'] == [('היצא', 'HTd/Vqrmsa')]   # the law's consecutive perfects in the tithe's half alone; "that comes forth" the one article-participle
assert Counter(wt for v in range(1, 30) for wt in byw[('Deut', 14, v)]) == Counter({None: 351}) and STORE_MISMATCH == [] and len([x for x, m in by[('Deut', 14, 1)] if m and 'Np' in m]) == 1   # NO KETIV, the store = the DB at every verse; the tagger's "Np" the Name's tokens only
# ---- THE PARSER (the C print): TWO NUMBER VERSES — 14:6 "two hoofs" [2] and 14:28 "three years" [3]; THE STARRED TITHE TOKENS — the number word "ten" inside "tithe" marked at 14:22, 14:23, 14:28 (and 12:17, 26:12 in the book), no number read; the kin's numbers (15:1's and 31:10's seven, Exodus 23:10's six) ----
with contextlib.redirect_stdout(io.StringIO()):
    import cold_run_sequence as CS
PARSE = {v: (CS.ink_numbers(CS.verse_words('Deut', 14, v)), CS.ink_ordinals(CS.verse_words('Deut', 14, v)), [t for t in CS.verse_words('Deut', 14, v) if t[-1] in '#~^%@|*']) for v in range(1, 30)}
assert {v: p for v, p in PARSE.items() if p[0] or p[1] or p[2]} == {6: ([2], [], ['שתי^']), 22: ([], [], ['עשר*']), 23: ([], [], ['מעשר*']), 28: ([3], [], ['שנים*', 'מעשר*'])}, {v: p for v, p in PARSE.items() if p[0] or p[1] or p[2]}
assert CS.verse_words('Deut', 14, 22)[:2] == ['עשר*', 'תעשר'] and CS.verse_words('Deut', 14, 28)[:3] == ['מקצה', 'שלש', 'שנים*'] and sorted({(c, v, t) for (b, c, v) in by if b == 'Deut' for t in CS.verse_words(b, c, v) if (t.startswith('מעשר') or t.startswith('עשר') or t.startswith('תעשר')) and t[-1] in '#~^%@|*'}) == [(12, 17, 'מעשר*'), (14, 22, 'עשר*'), (14, 23, 'מעשר*'), (14, 28, 'מעשר*'), (26, 12, 'מעשר*')]
assert {k: CS.ink_numbers(CS.verse_words(*k)) for k in (('Deut', 15, 1), ('Deut', 31, 10), ('Exod', 23, 10), ('Lev', 11, 3), ('Lev', 27, 30), ('Num', 18, 21), ('Deut', 26, 12), ('Deut', 12, 17))} == {('Deut', 15, 1): [7], ('Deut', 31, 10): [7], ('Exod', 23, 10): [6], ('Lev', 11, 3): [], ('Lev', 27, 30): [], ('Num', 18, 21): [], ('Deut', 26, 12): [], ('Deut', 12, 17): []}
assert [(v, x) for v in range(1, 30) for x in W14(v) if x in ('שלש', 'שלשה', 'שתי', 'שנים', 'שני')] == [(6, 'שתי'), (28, 'שלש'), (28, 'שנים')]
# ---- ONKELOS (the E print; the export's chapter 14 = the DB's) ----
assert aramaic(14, 1) == ['בנין', 'אתון', 'קדם', 'יי', 'אלהכון', 'לא', 'תתחממון', 'ולא', 'תשוון', 'מרט', 'בין', 'עיניכון', 'על', 'מית'] and onk_seats('בנין אתון') == [(14, 1)] and (14, 1) in onk_seats('מית')   # "you shall not make incisions" (תתחממון) — the Aramaic's own root, the Hebrew's "cut yourselves" not carried; "children BEFORE the LORD" — the English's bracket "[before]" the Aramaic's word
assert aramaic(14, 2)[-7:] == ['לעם', 'חביב', 'מכל', 'עממיא', 'די', 'על', 'אפי', 'ארעא'][-7:] and onk_seats('חביב') == [(7, 6), (14, 2), (26, 18), (33, 3)] and onk_seats('עם קדיש') == [(7, 6), (14, 2), (14, 21), (26, 19), (28, 9)] and aramaic(7, 6)[7:11] == ['בך', 'אתרעי', 'יי', 'אלהך'] and aramaic(14, 2)[7:11] == ['ובך', 'אתרעי', 'יי', 'למהוי']   # "BELOVED" for "treasured" at its four seats; "a holy people" five; the dropped "your God" of 14:2 dropped in the Aramaic too
assert aramaic(14, 3) == ['לא', 'תיכול', 'כל', 'דמרחק'] and len(onk_seats('מרחק')) == 11 and (14, 3) in onk_seats('מרחק') and onk_seats('שקצ') == [(7, 26)]   # "abomination" rendered "what is removed/far" at the book's eleven seats; "detest" once at 7:26
assert aramaic(14, 4) == ['דין', 'בעירא', 'דתיכלון', 'תורין', 'אמרין', 'דרחלין', 'וגדין', 'דעזין'] and aramaic(14, 5) == ['אילא', 'וטביא', 'ויחמורא', 'ויעלא', 'ורימא', 'ותורבלא', 'ודיצא'] and onk_seats('יחמור') == [(14, 5)] and onk_seats('תורבל') == [(14, 5)] and onk_seats('דיצ') == [(14, 5), (27, 19)] and onk_seats('רימ') == [(14, 5)]   # THE SEVEN WILD IN ARAMAIC — the wild goat "ya'ala", the pygarg "rema", the antelope "turbala", the mountain-sheep "ditsa": names, not glosses (the Talmud's identifications the exam's, Chullin 80a)
assert aramaic(14, 6)[6:8] == ['תרתין', 'פרסתא'] and onk_seats('סדיק') == [(14, 6), (14, 7), (14, 8)] and onk_seats('פשר') == [(14, 6), (14, 7), (14, 8)] and onk_seats('טפזא') == [(14, 7)] and onk_seats('חזירא') == [(14, 8)] and aramaic(14, 8)[-2:] == ['לא', 'תקרבון']   # "two hoofs" TWO in the Aramaic too (the number carried); "their carcass you shall not touch" — "draw near"
assert onk_seats('ציצין') == [(14, 9), (14, 10)] and aramaic(14, 11) == ['כל', 'צפר', 'דכיא', 'תיכלון'] and aramaic(14, 20) == ['כל', 'עופא', 'דכי', 'תיכלון'] and aramaic(14, 13) == ['ובת', 'כנפא', 'וטרפיתא', 'ודיתא', 'לזנה'] and aramaic(14, 19)[-2:] == ['לא', 'יתאכלון']   # "fins and scales" — the Aramaic's own pair; THE RA'AH RENDERED "bat kanfa" (the daughter of the wing) — the export's own names for the birds
assert aramaic(14, 21)[-4:] == ['לא', 'תיכול', 'בשר', 'בחלב'] and onk_seats('בשר בחלב') == [(14, 21)] and aramaic(14, 21)[4:6] == ['לתותב', 'ערל'] and onk_seats('בר עממין') == [(14, 21), (15, 3), (23, 21), (29, 21)] and onk_seats('נביל') == [(14, 21)] and onk_seats('תותב') == [(14, 21), (28, 43)]   # "YOU SHALL NOT EAT FLESH WITH MILK" — Onkelos writes the law, not the verse (the kid and the mother gone; the English's bracket "[milk with meat]"); "to the UNCIRCUMCISED sojourner" — the resident alien supplied; "a foreigner" the book's four
assert aramaic(14, 22)[:2] == ['עשרא', 'תעשר'] and aramaic(14, 22)[-2:] == ['שתא', 'בשתא'] and aramaic(14, 23)[4:10] == ['באתרא', 'די', 'יתרעי', 'לאשראה', 'שכנתיה', 'תמן'] and onk_seats('לאשראה') == [(12, 5), (12, 11), (12, 21), (14, 23), (14, 24), (16, 2), (16, 6), (16, 11), (26, 2)] and [(c, v) for c, v in onk_seats('שכנת') if c == 14] == [(14, 23), (14, 24)] and (14, 23) in onk_seats('למדחל')   # "tithe, you shall tithe" doubled in the Aramaic; THE SHEKHINAH AT THE PLACE — the formula's rendering at nine seats, the chapter's two
assert aramaic(14, 26)[6:11] == ['בתורי', 'ובענא', 'ובחמר', 'חדת', 'ועתיק'] and onk_seats('עתיק') == [(14, 26), (29, 5)] and aramaic(14, 24)[:4] == ['וארי', 'יסגי', 'מנך', 'ארחא'] and aramaic(14, 25)[:5] == ['ותתן', 'בכספא', 'ותצור', 'כספא', 'בידך'] and [(c, v) for c, v in onk_seats('ותחדי') if c == 14] == [(14, 26)]   # "wine and strong drink" rendered "NEW WINE AND OLD" — the strong drink read as aged wine (the English's bracket); the money bound
assert aramaic(14, 27) == ['ולואה', 'די', 'בקרויך', 'לא', 'תשבקניה', 'ארי', 'לית', 'ליה', 'חלק', 'ואחסנא', 'עמך'] and onk_seats('חלק ואחסנא') == [(10, 9), (12, 12), (14, 27), (14, 29), (18, 1)] and aramaic(14, 28)[:3] == ['מסוף', 'תלת', 'שנין'] and aramaic(14, 29)[8:11] == ['וגיורא', 'ויתמא', 'וארמלא'] and onk_seats('וישבעון') == [(14, 29), (26, 12), (31, 20)]   # "portion and inheritance" at the Levite's five; "three years" carried; the four at the gate
assert [(c, v) for c, v in onk_seats('מימר') if c == 14] == [] and [(14, v + 1) for v in range(29) if '(' in clean(onk_he[13][v])] == []   # no Memra, no parenthesis in the Aramaic of the chapter
# ---- THE ENGLISH'S BRACKETS (the F print) ----
BR = {v: re.findall(r'\[([^\]]+)\]', clean(onk[13][v - 1])) for v in range(1, 30)}
assert {v: len(b) for v, b in BR.items() if b} == {1: 1, 6: 1, 7: 1, 8: 2, 21: 3, 23: 2, 24: 1, 26: 2} and sum(len(b) for b in BR.values()) == 13 and BR[21] == ['uncircumcised', 'foreigner', 'milk with meat'] and BR[23] == ['Shechinah', 'before'] and BR[26] == ['fresh and aged wine', 'the members of'] and [v for v in range(1, 30) if '(' in clean(onk[13][v - 1])] == []
# ---- THE STORE (the G print): 197 distinct glosses, 25 already rewritten; NO KETIV (351 = 351) — the display patch predicted at the tail (ch14_ink_body_c.py) ----
store = sqlite3.connect(f'file:{ROOT}/torah_grok.SNAPSHOT-main-51801ca.sqlite?mode=ro', uri=True)
SG = {}
for c_, v_, i_, hp, g in store.execute("SELECT v.chapter, v.verse, w.idx, w.he_plain, w.gloss FROM words w JOIN verses v ON w.verse_id=v.id WHERE v.book='Deut' AND v.chapter=? ORDER BY v.id, w.idx", (14,)):
    SG.setdefault((c_, v_), []).append((i_, hp.replace('/', ''), g))
CHG = sorted({g for k in SG for _, _, g in SG[k]})
import yaml
OVY = yaml.safe_load(open(f'{ROOT}/logic/glosses/word_gloss_overrides.yaml', encoding='utf-8'))
BG = OVY.get('by_gloss', OVY.get('gloss', {})) if isinstance(OVY, dict) else {}
MARK = 'THE DEUTERONOMY WALK sitting 12 (2026-09-21, Deuteronomy 14)'
PATCHED = MARK in open(f'{ROOT}/logic/glosses/word_gloss_overrides.yaml', encoding='utf-8').read()   # the display patch's own marker: once the patch has run, this sitting's forty-nine by-gloss rows join the store's "already" count (the fifth pass's lesson)
assert len(CHG) == 197 and len([g for g in CHG if g in BG]) == (25 + 49 if PATCHED else 25) and sum(len(SG[k]) for k in SG) == 351 and [v for v in range(1, 30) if len(SG.get((14, v), [])) != len(W14(v))] == [] and [(k[1], i_, hp) for k in sorted(SG) for i_, hp, g in SG[k] if g == '?'] == []
assert BG.get('try') == 'choose' and BG.get('wealth') == 'treasure' and BG.get('something-disgusting') == 'abomination' and BG.get('goad') == 'teach' and BG.get('and-sate') == 'and-be-satisfied' and BG.get('to-reside') == 'to-make-dwell'   # the chapter's glosses already turned by earlier sittings' by-gloss rows
# ---- THE REGISTER'S FINDER on the chapter (the H print): no receipt with the Name, no header, no footer, no count line — 14:4's "this is the beast" is a list's header, not a register's
with contextlib.redirect_stdout(io.StringIO()):
    import register_census as RC
    _ink = RC.read_ink()
assert [k for k in RC.receipts(_ink) if k[0] == 'Deut' and k[1] == 14] == [] and [x for x in RC.footers(_ink) if x[0][0] == 'Deut' and x[0][1] == 14] == [] and [x for x in RC.register_headers(_ink) if x[0][0] == 'Deut' and x[0][1] == 14] == [] and [k for k in RC.receipts(_ink) if k[0] == 'Deut' and k[1] <= 14] == [('Deut', 1, 3), ('Deut', 1, 19), ('Deut', 1, 41), ('Deut', 4, 5), ('Deut', 5, 12), ('Deut', 5, 16), ('Deut', 5, 32), ('Deut', 10, 5)]
FAIL_ALL = list(FAIL)
print('THE INK OF CHAPTER 14 — every assert above passed; the cuts\' misses:', FAIL_ALL)
# ---- THE DISPLAY PATCH PREDICTED (the G print — the store's gloss families over the whole store; sitting 11's form, ch13_ink_body_c.py): BY GLOSS where every token of the gloss is the one word (or one family read the same at every seat), BY REFERENCE where the family is mixed ----
GLOSS_FAMILY = {'and-claw': [('ופרסה', 4)], 'and-from-break-in-pieces': [('וממפריסי', 2)], 'from-go-up': [('ממעלי', 2)], 'and-gazelle': [('וזמר', 1)], 'and-splendor': [('וצבי', 1)], 'and-kind-of-deer': [('ויחמור', 1)], 'and-leaper': [('ודישן', 1)], 'and-slender': [('ואקו', 1)], 'and-species-of-antelope': [('ותאו', 1)], 'stag': [('איל', 1)],
                'and-in-flabby-thing-them/their': [('ובנבלתם', 2)], 'flabby-thing': [('נבלה', 4)], 'and-in-intoxicant': [('ובשכר', 1)], 'and-in-wine': [('וביין', 1)], 'claw': [('פרסה', 7), ('פרסת', 1), ('פרסות', 1)], 'foul-in-a-religious-sense': [('טמא', 33), ('טמאים', 8), ('טמאה', 7)], 'little-bird': [('צפור', 4), ('צפרים', 2)], 'flying-creature': [('עוף', 9)], 'the-flying-creature': [('העוף', 12)],
                'and-the-claw': [('והפרס', 1)], 'and-the-sea-eagle': [('והעזניה', 1)], 'and-the-bird-of-prey': [('והראה', 1)], 'the-screamer': [('האיה', 2)], 'and-the-falcon': [('והדיה', 1)], 'the-ostrich-(probably-from-its-a': [('היענה', 2)], 'the-species-of-unclean-bird': [('התחמס', 2)], 'the-gull': [('השחף', 2)], 'the-flower': [('הנץ', 2)], 'the-unclean--bird': [('הינשוף', 2)], 'and-the-hard-breather': [('והתנשמת', 2)], 'the-kind-of-vulture-suffix': [('הרחמה', 1)], 'the-bird-of-prey': [('השלך', 2)], 'and-the-kind--bird': [('והחסידה', 1)], 'and-the-unclean-bird': [('והאנפה', 1)],
                'to-kind-her/its': [('למינה', 10)], 'to-kind-him/its': [('למינהו', 14), ('למינו', 4)], 'to-sojourner': [('לגר', 6)], 'to-strange': [('לנכרי', 2)], 'income': [('תבואת', 5)], 'income-you/your': [('תבואתך', 3)], 'must-you/your': [('תירשך', 2)], 'the-way/road': [('הדרך', 20)], 'and-house-you/your': [('וביתך', 3)], 'and-the-bereaved-person': [('והיתום', 3)], 'the-species-of-rockrabbit': [('השפן', 2)], 'the-split': [('השסועה', 1)], 'the-hog': [('החזיר', 2)], 'from-flesh-them/their': [('מבשרם', 3)], 'swarming-creature': [('שרץ', 8)]}
GT = {g: store.execute("SELECT REPLACE(w.he_plain,'/',''), COUNT(*) FROM words w WHERE w.gloss=? GROUP BY 1 ORDER BY 2 DESC, 1", (g,)).fetchall() for g in GLOSS_FAMILY}
assert all(sorted(GT[g]) == sorted(v) for g, v in GLOSS_FAMILY.items()), [(g, GT[g]) for g, v in GLOSS_FAMILY.items() if sorted(GT[g]) != sorted(v)]
# BY GLOSS — the beasts' and the birds' names (each ONE word in the store), the hoof and the cud's chewers, the carcass, the wine and the strong drink, the fowl, the kinds, the sojourner and the foreigner, the yield and the produce, the way, the household, the fatherless, the unclean (forty-eight tokens, three forms of one word)
OVERRIDE_GLOSS = [('and-claw', 'and-hoof'), ('and-from-break-in-pieces', 'and-of-those-that-part'), ('from-go-up', 'of-those-that-chew'), ('and-gazelle', 'and-the-mountain-sheep'), ('and-splendor', 'and-the-gazelle'), ('and-kind-of-deer', 'and-the-roebuck'), ('and-leaper', 'and-the-pygarg'), ('and-slender', 'and-the-wild-goat'), ('and-species-of-antelope', 'and-the-antelope'), ('stag', 'the-hart'),
                  ('and-in-flabby-thing-them/their', 'and-their-carcass'), ('flabby-thing', 'carcass'), ('and-in-intoxicant', 'and-on-strong-drink'), ('and-in-wine', 'and-on-wine'), ('claw', 'hoof'), ('foul-in-a-religious-sense', 'unclean'), ('little-bird', 'bird'), ('flying-creature', 'fowl'), ('the-flying-creature', 'the-fowl'),
                  ('and-the-claw', 'and-the-ossifrage'), ('and-the-sea-eagle', 'and-the-osprey'), ('and-the-bird-of-prey', 'and-the-glede'), ('the-screamer', 'the-kite'), ('and-the-falcon', 'and-the-vulture'), ('the-ostrich-(probably-from-its-a', 'the-ostrich'), ('the-species-of-unclean-bird', 'the-night-hawk'), ('the-gull', 'the-sea-mew'), ('the-flower', 'the-hawk'), ('the-unclean--bird', 'the-great-owl'), ('and-the-hard-breather', 'and-the-horned-owl'), ('the-kind-of-vulture-suffix', 'the-carrion-vulture'), ('the-bird-of-prey', 'the-cormorant'), ('and-the-kind--bird', 'and-the-stork'), ('and-the-unclean-bird', 'and-the-heron'),
                  ('to-kind-her/its', 'after-its-kind'), ('to-kind-him/its', 'after-its-kind'), ('to-sojourner', 'to-the-sojourner'), ('to-strange', 'to-a-foreigner'), ('income', 'the-yield-of'), ('income-you/your', 'your-produce'), ('must-you/your', 'your-wine'), ('the-way/road', 'the-way'), ('and-house-you/your', 'and-your-household'), ('and-the-bereaved-person', 'and-the-fatherless'), ('the-species-of-rockrabbit', 'the-rock-badger'), ('the-split', 'the-cleft-one'), ('the-hog', 'the-swine'), ('from-flesh-them/their', 'of-their-flesh'), ('swarming-creature', 'swarming-thing')]
# BY REFERENCE — the family mixed (a homograph: "cup" for the little owl, "smoothness" for the portion, "morning" for the herd, "flower" kept for the hawk by gloss; "for" against "that" and "when"; a verb read two ways; a noun singular and plural): the seat named
OVERRIDE_REF_SPEC = [(1, 'בנים', 'children', 0), (1, 'תתגדדו', 'cut-yourselves', 0), (1, 'תשימו', 'you-shall-make', 0), (1, 'למת', 'for-the-dead', 0),
                     (2, 'כי', 'for', 0), (2, 'עם', 'a-people', 0), (2, 'קדוש', 'holy', 0), (2, 'ובך', 'and-you', 0), (2, 'לו', 'for-Himself', 0), (2, 'לעם', 'as-a-people', 0), (2, 'העמים', 'the-peoples', 0), (2, 'על', 'upon', 0), (2, 'פני', 'the-face-of', 0), (2, 'האדמה', 'the-earth', 0),
                     (3, 'תאכל', 'you-shall-eat', 0), (3, 'כל', 'any', 0),
                     (4, 'הבהמה', 'the-beast', 0), (4, 'תאכלו', 'you-shall-eat', 0), (4, 'שור', 'the-ox', 0), (4, 'שה', 'the-sheep-of', 0), (4, 'כשבים', 'lambs', 0), (4, 'ושה', 'and-the-sheep-of', 0), (4, 'עזים', 'goats', 0),
                     (6, 'וכל', 'and-every', 0), (6, 'בהמה', 'beast', 0), (6, 'מפרסת', 'that-parts', 0), (6, 'ושסעת', 'and-cleaves', 0), (6, 'שסע', 'the-cleft', 0), (6, 'מעלת', 'chewing', 0), (6, 'בבהמה', 'among-the-beasts', 0), (6, 'אתה', 'it', 0), (6, 'תאכלו', 'you-shall-eat', 0),
                     (7, 'אך', 'but', 0), (7, 'תאכלו', 'you-shall-eat', 0), (7, 'הפרסה', 'the-hoof', 0), (7, 'כי', 'for', 0), (7, 'מעלה', 'chew', 0), (7, 'הפריסו', 'they-part', 0), (7, 'לכם', 'to-you', 0),
                     (8, 'כי', 'for', 0), (8, 'מפריס', 'parts', 0), (8, 'הוא', 'it', 0), (8, 'הוא', 'it', 1), (8, 'לכם', 'to-you', 0), (8, 'תאכלו', 'you-shall-eat', 0), (8, 'תגעו', 'you-shall-touch', 0),
                     (9, 'תאכלו', 'you-shall-eat', 0), (9, 'תאכלו', 'you-shall-eat', 1), (9, 'במים', 'in-the-waters', 0), (9, 'לו', 'to-it', 0), (9, 'וקשקשת', 'and-scales', 0),
                     (10, 'וקשקשת', 'and-scales', 0), (10, 'תאכלו', 'you-shall-eat', 0), (10, 'הוא', 'it', 0), (10, 'לכם', 'to-you', 0), (10, 'לו', 'to-it', 0),
                     (11, 'כל', 'every', 0), (11, 'טהרה', 'clean', 0), (11, 'תאכלו', 'you-shall-eat', 0),
                     (12, 'תאכלו', 'you-shall-eat', 0), (12, 'מהם', 'of-them', 0),
                     (14, 'כל', 'every', 0), (15, 'בת', 'the-daughter-of', 0), (16, 'הכוס', 'the-little-owl', 0),
                     (19, 'וכל', 'and-every', 0), (19, 'הוא', 'it', 0), (19, 'לכם', 'to-you', 0), (19, 'יאכלו', 'they-shall-be-eaten', 0),
                     (20, 'כל', 'every', 0), (20, 'טהור', 'clean', 0), (20, 'תאכלו', 'you-shall-eat', 0),
                     (21, 'תאכלו', 'you-shall-eat', 0), (21, 'כל', 'any', 0), (21, 'תתננה', 'you-shall-give-it', 0), (21, 'ואכלה', 'that-he-may-eat-it', 0), (21, 'מכר', 'sell-it', 0), (21, 'כי', 'for', 0), (21, 'עם', 'a-people', 0), (21, 'קדוש', 'holy', 0), (21, 'תבשל', 'you-shall-boil', 0), (21, 'גדי', 'a-kid', 0), (21, 'בחלב', 'in-the-milk-of', 0), (21, 'אמו', 'its-mother', 0),
                     (22, 'תעשר', 'you-shall-tithe', 0), (22, 'היצא', 'that-comes-forth-from', 0), (22, 'שנה', 'year', 0), (22, 'שנה', 'by-year', 1),
                     (23, 'לפני', 'before', 0), (23, 'שמו', 'His-name', 0), (23, 'מעשר', 'the-tithe-of', 0), (23, 'הימים', 'the-days', 0),
                     (24, 'וכי', 'and-when', 0), (24, 'ירבה', 'is-too-long', 0), (24, 'תוכל', 'you-are-able', 0), (24, 'שאתו', 'to-carry-it', 0), (24, 'כי', 'because', 1), (24, 'ירחק', 'is-too-far', 0), (24, 'שמו', 'His-name', 0), (24, 'כי', 'because', 2), (24, 'יברכך', 'will-bless-you', 0),
                     (25, 'ונתתה', 'and-you-shall-turn-it', 0), (25, 'בכסף', 'into-money', 0), (25, 'וצרת', 'and-bind-up', 0), (25, 'הכסף', 'the-money', 0), (25, 'והלכת', 'and-go', 0), (25, 'בו', 'in-it', 0),
                     (26, 'ונתתה', 'and-you-shall-bestow', 0), (26, 'הכסף', 'the-money', 0), (26, 'בכל', 'on-whatever', 0), (26, 'תאוה', 'desires', 0), (26, 'בבקר', 'on-oxen', 0), (26, 'ובצאן', 'and-on-sheep', 0), (26, 'ובכל', 'and-on-whatever', 0), (26, 'לפני', 'before', 0),
                     (27, 'תעזבנו', 'you-shall-forsake-him', 0), (27, 'כי', 'for', 0), (27, 'חלק', 'portion', 0), (27, 'עמך', 'with-you', 0),
                     (28, 'מקצה', 'at-the-end-of', 0), (28, 'תוציא', 'you-shall-bring-out', 0), (28, 'מעשר', 'the-tithe-of', 0), (28, 'בשנה', 'in-the-year', 0), (28, 'והנחת', 'and-lay-it-up', 0),
                     (29, 'ובא', 'and-shall-come', 0), (29, 'כי', 'for', 0), (29, 'חלק', 'portion', 0), (29, 'עמך', 'with-you', 0), (29, 'יברכך', 'may-bless-you', 0), (29, 'מעשה', 'the-work-of', 0), (29, 'ידך', 'your-hand', 0), (29, 'תעשה', 'you-do', 0)]
OVERRIDE_REF3 = [(f'Deut.14.{v}:{sidx(14, v, tok, nth)}', new, tok) for v, tok, new, nth in OVERRIDE_REF_SPEC]
OVERRIDE_REF = [(k, v) for k, v, _ in OVERRIDE_REF3]
assert len(OVERRIDE_REF) == len({k for k, _ in OVERRIDE_REF}) == len(OVERRIDE_REF_SPEC) and len(OVERRIDE_GLOSS) == len({k for k, _ in OVERRIDE_GLOSS}) and all(g in GLOSS_FAMILY for g, _ in OVERRIDE_GLOSS) and all(sg(14, v, tok, nth) is not None for v, tok, _, nth in OVERRIDE_REF_SPEC)
assert all(sg(14, v, tok, nth) != new for v, tok, new, nth in OVERRIDE_REF_SPEC), [(v, tok) for v, tok, new, nth in OVERRIDE_REF_SPEC if sg(14, v, tok, nth) == new]   # no row rewrites a gloss to itself
print('THE DISPLAY PATCH PREDICTED — by gloss', len(OVERRIDE_GLOSS), 'by reference', len(OVERRIDE_REF))
# the chapter's glosses ALREADY rewritten by the by-gloss overrides (the G print's twenty-five)
ALREADY = {'God-you/your': 'your-God', 'God-you/your (pl)': 'your-God', 'and-brighten-up': 'and-rejoice', 'and-firstling-of-man': 'and-the-firstlings-of', 'and-flock-you/your': 'and-your-flock', 'and-oil-you/your': 'and-your-oil', 'and-sate': 'and-be-satisfied', 'eye-you/your (pl)': 'your-eyes', 'from-you/your': 'from-you', 'goad': 'teach', 'herd-you/your': 'your-herd', 'in-gate-you/your': 'within-your-gates', 'in-hand-you/your': 'in-your-hand', 'in-place': 'in-the-place', 'increase-you/your': 'your-grain', 'inquire-you/your': 'asks-you', 'living-being-you/your': 'your-soul', 'particle-of-affirmation': 'only', 'seed-you/your': 'your-seed', 'something-disgusting': 'abomination', 'the-he/it': 'that', 'to-put/set': 'to-put', 'to-reside': 'to-make-dwell', 'try': 'choose', 'wealth': 'treasure'}
assert len(ALREADY) == 25 and sorted(ALREADY) == sorted(g for g in CHG if g in BG and g not in dict(OVERRIDE_GLOSS)) and all(BG[g] == ALREADY[g] for g in ALREADY)
OV = open(f'{ROOT}/logic/glosses/word_gloss_overrides.yaml', encoding='utf-8').read()
MARK = 'THE DEUTERONOMY WALK sitting 12 (2026-09-21, Deuteronomy 14)'
PATCHED = MARK in OV
assert all(f'"{k}": "{v}"' in OV for k, v in ALREADY.items()) and all(f'"{k}": ' not in OV for k, _ in OVERRIDE_GLOSS if not PATCHED) and (PATCHED or '"Deut.14.' not in OV), [k for k, _ in OVERRIDE_GLOSS if f'"{k}": ' in OV]
if PATCHED: assert all(f'"{k}": "{v}"' in OV for k, v in OVERRIDE_REF) and all(f'"{k}": "{v}"' in OV for k, v in OVERRIDE_GLOSS), [k for k, v in OVERRIDE_REF + OVERRIDE_GLOSS if f'"{k}": "{v}"' not in OV][:6]
assert OV.count('  "Deut.13.19:15": "in-the-eyes-of"') == 1 and 'THE DEUTERONOMY WALK sitting 11 (2026-09-21, Deuteronomy 13)' in OV   # sitting 11's anchors, the patch's own
FAIL_ALL = list(FAIL)

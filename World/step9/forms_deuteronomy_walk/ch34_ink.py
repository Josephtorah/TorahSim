import os as _os
_ROOT = _os.path.normpath(_os.path.join(_os.path.dirname(_os.path.abspath(__file__)), '..', '..', '..'))   # THE PORTABLE REPO (2026-09-15): the repo root from this file's own place
#!/usr/bin/env python3
# THE DEUTERONOMY WALK, sitting 22 — CHAPTER 34, THE DEATH OF MOSES, Deuteronomy 34:1-12 IN THE LEAN FORM (2026-09-30; the owner: "Reread and go" after the compaction
# that followed sitting 21b's tail — the tree UNCOMMITTED with 21 and 21b since 472d2a3; THE LEAN PASS's seventeenth sitting, its ninth reading; THE SPINE IN FORCE: ONE
# piska, 357 on 34:1 — THE EXPORT'S LAST, forty-four rows, 42 KB in the split's file; DEUTERONOMY'S LAST CHAPTER): THE INK of the chapter, computed from the Tanakh DB,
# the snapshot store and the shelf's own bytes — never typed. Sitting 21's form (ch33_ink.py): the generic helpers copied by derive_ch34_ink.py from the forms' ch22_ink.py
# by content markers (the chapter substituted; the head regex comma-tolerant as sitting 21 left it), the constants and every assert the chapter's own, typed FROM THE PRINTS
# (ch34_dump0.out, ch34_split.out, ch34_measure_lean.out). THE TWO DIVISIONS AGREE (12 = 12, cost 5) — the identity. ONE DRAFT on file: deu_34_moses_death (34:1-12,
# twelve steps one per verse) — one unit, CHAPTER NUMBERS. TWO rows elsewhere cite the chapter, both READ BEFORE (305:5 at chapters 29-31 — the angel of death sent for
# Moses' soul; 341:1 at the song — "from afar you shall see the land"). THE PORTION EDGE: Vezot Habrachah is 33:1-34:12 — the chapter the portion's and the book's last;
# no piska after 357. The parser MEASURED on every verse — TWO NUMBERS COUNTED: 34:7's hundred and twenty (Moses' years at his death — 31:2's number, the marker's day)
# and 34:8's thirty (the days of weeping — a duration: the compile's matter). ONE ROW OF THE TESTING SHELF read whole at this sitting by 21b's leaving — Tosefta Sotah 4:4
# on 34:6 (the four mil on the Shekhinah's wings from Reuben's field to Gad's; the export Tosefta_Sotah, the Vilna paragraphs). The hand's facts as asserts, run all at
# once by assert_driver.py.
import json, os, re, html, sqlite3, sys, io, contextlib, unicodedata, subprocess
from collections import Counter
ROOT = _ROOT
DATE = '2026-09-30'
CHS = (34,)
UIDS = ['deu_34_moses_death']   # the draft's own id (the G print): one unit in the one chapter — the death 34:1-12
SPANS = {'deu_34_moses_death': (34, 1, 12)}
PREFIX = {'deu_34_moses_death': 'DV34'}
SPAN = [(34, v) for v in range(1, 13)]
PISKAOT = [357]   # THE SPINE ON CHAPTER 34: one piska, the export's last (the A prints and the split's); 356 on 33:27 before, NOTHING after
PISKAOT_BY = {34: PISKAOT}
HEADLESS = []   # none (the dump's heads table: 357's head is (34, 1))
SPINE_ROWS = {357: 44}   # rows per piska, both files (the heads table and the split's print) — 44
PREV_CHAPTER_ROWS = []   # no tail folded in (356's fourteen rows carry no word of 34:1 — the split's print; 356:14 ends on Joshua 10:24's necks; 357:1 opens with 34:1's ascent)
READ_ROWS = [(p, r) for p in PISKAOT for r in range(1, SPINE_ROWS[p] + 1)]   # 44 — this ledger's spine rows, read WHOLE in one slice (the split's plan: one slice, 42,152 bytes)
EXP2DB = {34: {e: [e] for e in range(1, 13)}}   # the identity (the offset 0 at every export verse — A0's print)
DB2EXP = {c: {d: e for e, ds in EXP2DB[c].items() for d in ds} for c in CHS}
OUTSIDE = [(305, 5), (341, 1)]   # the TWO rows READ WHOLE: the union of the two files beyond piska 357 (the dump's and the split's print) — both read before
EXCLUDED = []   # none known at the design — a translator's misprint is judged by the Hebrew at the whole read (sitting 18's lesson 4)
INTERPOLATION = []
CREDITED = {}   # under THE WHOLE-ROW RULE no spine row is credited: the four rows read before (357:27, 28, 40, 44 — the dump's list) are REREAD WHOLE here and marked so
TOSEFTA_ROWS = [('Sotah', 4, 4)]   # THE TESTING SHELF'S ONE ROW read whole at this reading by sitting 21b's leaving (found beside 355:6 on 34:6): the export Tosefta_Sotah
TITLE = "Chapter 34 — the death of Moses: and Moses went up from the plains of Moab to Mount Nebo, the top of Pisgah over against Jericho, and the LORD showed him all the land — Gilead as far as Dan, all Naphtali, the land of Ephraim and Manasseh, all the land of Judah as far as the hinder sea, the south and the plain of the valley of Jericho the city of palm trees as far as Zoar; and the LORD said to him: this is the land which I swore to Abraham, to Isaac and to Jacob, saying, to your seed I will give it — I have caused you to see it with your eyes, but you shall not cross over there. So Moses the servant of the LORD died there in the land of Moab by the mouth of the LORD, and He buried him in the valley in the land of Moab over against Beth-peor, and no man knows his grave to this day. Moses was a hundred and twenty years old when he died; his eye was not dim nor his natural force abated. The children of Israel wept for Moses in the plains of Moab thirty days, and the days of weeping in the mourning for Moses were ended. Joshua the son of Nun was full of the spirit of wisdom, for Moses had laid his hands upon him, and the children of Israel hearkened to him and did as the LORD commanded Moses. And there has not arisen a prophet since in Israel like Moses, whom the LORD knew face to face, in all the signs and the wonders which the LORD sent him to do in the land of Egypt to Pharaoh and to all his servants and to all his land, and in all the mighty hand and all the great terror which Moses wrought in the sight of all Israel."
OUT = f'{ROOT}/logic/oral_triage/deu_34_moses_death_{DATE}.md'
PATCHED = bool(os.environ.get('DEU34_PATCHED'))   # the tail's flag: after the manifest and the seat, the draft carries operators and the store its overrides
db = sqlite3.connect(f'file:{ROOT}/Data/tanakh.sqlite?mode=ro', uri=True)
VC = dict(db.execute("SELECT chapter, COUNT(*) FROM verses WHERE book='Deut' GROUP BY chapter").fetchall())
NV = {c: VC[c] for c in CHS}
# ---- THE HELPERS (ch22_ink.py's, copied by content markers; the head regex comma-tolerant) ----
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
    m = re.match(r'\(דברים ([א-ת]+),? ([א-ת]+)(?:-[א-ת]+)?\)', Hb(p, 1))
    heads[p] = (hn(m.group(1)), hn(m.group(2))) if m else None
def head(p): return heads[p]
def he_cites(t): return [(b, hn(c), hn(v)) for b, c, v in re.findall(r'\(([א-ת]+(?: [א-ת])?) ([א-ת]{1,3}) ([א-ת]{1,3})\)', t)]
def has_points(s): return any(0x05B0 <= ord(c) <= 0x05BD for c in s)
def kinrows(f, pat): return len(re.findall(r'^- Onkelos ' + pat, LED[f], re.M))
def onk_ev(c, v):
    """an Onkelos row by the DB's verse — the export's row found through the map (chapter 5's 17-20 share the export's 17)"""
    e = DB2EXP[v] if c == 5 else v
    return clean(onk[c - 1][e - 1]), clean(onk_he[c - 1][e - 1])
# ---- THE INK'S HELPERS, THE DB AND THE STORE (ch22_ink.py's, the chapter substituted) ----
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
def W34(v): return words('Deut', 34, v)
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
for c, v, idx, hp, g in store.execute("SELECT v.chapter, v.verse, w.idx, w.he_plain, w.gloss FROM words w JOIN verses v ON w.verse_id=v.id WHERE v.book='Deut' AND v.chapter IN (34) ORDER BY v.id, w.idx"):
    SG.setdefault((c, v), []).append((idx, hp.replace('/', ''), g))
def sg(c, v, tok, nth=0):
    hit = [g for _, hp, g in SG[(c, v)] if hp == tok]
    if len(hit) <= nth: raise KeyError((c, v, tok, nth))
    return hit[nth]
def sidx(c, v, tok, nth=0):
    hit = [i for i, hp, _ in SG[(c, v)] if hp == tok]
    assert len(hit) > nth, (c, v, tok, nth, hit)
    return hit[nth]
STORE_MISMATCH = [(c, v, n, len(by[('Deut', c, v)])) for c, v, n in store.execute("SELECT v.chapter, v.verse, COUNT(*) FROM words w JOIN verses v ON w.verse_id=v.id WHERE v.book='Deut' AND v.chapter IN (34) GROUP BY v.chapter, v.verse").fetchall() if n != len(by[('Deut', c, v)])]
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
# ---- THE ASSERTS TYPED FROM THE PRINTS (block a: the dump's and the split's — the shelf by position, the divisions, the citations; the outside rows' facts COMPUTED) ----
DT = ('Deut',)
def PL(s): return ''.join(c for c in s if c != '/' and not (0x0591 <= ord(c) <= 0x05C7))
def HB0(p, r): return PL(clean(sif_he[p - 1][r - 1]))
def ARM(c, v): return [PL(unicodedata.normalize('NFKC', x)).strip('.:()') for x in clean(onk_he[c - 1][v - 1]).rstrip(':').split()]
def SEATS(sub): return [(c + 1, v + 1) for c in range(34) for v in range(len(onk_he[c])) if sub in ' '.join(ARM(c + 1, v + 1))]
# THE SHELF BY POSITION — THE SPINE IN FORCE on chapter 34: ONE head, 357 on 34:1 (the dump's window 335-357, the export's end); 356 on 33:27 before, NOTHING after; the heads by chapter as sitting 21's table printed them
assert NV == {34: 12} and VC[33] == 29 and VC[32] == 52 and len(sif) == 357 and len(sif_he) == 357 and sum(len(s) for s in sif) == 2357 and sum(len(s) for s in sif_he) == 2357
HC = Counter(h[0] for h in heads.values() if h)
assert (HC[31], HC[32], HC[33], HC[34]) == (1, 36, 15, 1) and sorted(HC.items()) == [(1, 24), (3, 4), (6, 6), (11, 21), (12, 20), (13, 14), (14, 14), (15, 16), (16, 19), (17, 16), (18, 16), (19, 10), (20, 14), (21, 17), (22, 22), (23, 22), (24, 16), (25, 10), (26, 4), (31, 1), (32, 36), (33, 15), (34, 1)], sorted(HC.items())
WIN = {335: (32, 46), 336: (32, 47), 337: (32, 48), 338: (32, 49), 339: (32, 50), 340: (32, 51), 341: (32, 52), 342: (33, 1), 343: (33, 2), 344: (33, 3), 345: (33, 4), 346: (33, 5), 347: (33, 6), 348: (33, 7), 349: (33, 8), 350: (33, 9), 351: (33, 10), 352: (33, 11), 353: (33, 13), 354: (33, 18), 355: (33, 20), 356: (33, 27), 357: (34, 1)}
assert {p: heads[p] for p in range(335, 358)} == WIN, {p: heads[p] for p in range(335, 358) if heads[p] != WIN[p]}
assert heads[357] == (34, 1) and 358 not in heads and HB0(357, 1).startswith('(דברים לד א) ויעל משה מערבת מואב, עליה היא ואינה ירידה') and 'And Moses ascended' in clean(sif[356][0]), (heads[357], HB0(357, 1)[:60])   # 357:1 opens with 34:1's citation: "and Moses went up — an ascent and not a descent"
HV = {c: [heads[p][1] for p in PISKAOT_BY[c] if heads[p]] for c in CHS}
assert HV == {34: [1]}, HV
NOHEAD = {c: [v for v in range(1, NV[c] + 1) if v not in HV[c]] for c in CHS}
assert NOHEAD == {34: [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]}, NOHEAD   # eleven verses without a head of their own — every one inside 357 (the one piska carries the whole chapter: the land shown, the oath, the death, the burial, the years, the weeping, Joshua, the prophet, the signs)
assert {p: (len(sif_he[p - 1]), len(sif[p - 1])) for p in PISKAOT} == {p: (n, n) for p, n in SPINE_ROWS.items()} and sum(SPINE_ROWS.values()) == 44 and len(READ_ROWS) == 44 and len(PISKAOT) == 1 and READ_ROWS[0] == (357, 1) and READ_ROWS[-1] == (357, 44)
# THE TAILS AND THE EDGES (the split's print): 356's fourteen rows carry no word of 34:1 ("and Moses went up"); 356:14 ends on Joshua 10:24's necks; 357:1 opens with 34:1's ascent; 357:43 reads the mighty hand as the plague of the firstborn and the great terror as the splitting of the sea; 357:44 — THE EXPORT'S LAST ROW — ends on the tablets broken "in the sight of all Israel" (9:17 against 34:12); no piska after 357
assert not any('ויעל משה' in HB0(356, r) for r in range(1, 15)) and HB0(356, 14).startswith('ואתה על במותימו תדרוך') and '(יהושע י כד)' in HB0(356, 14) and HB0(357, 43) == 'ולכל היד החזקה, זו מכת בכורות. ולכל המורא הגדול, זו קריעת ים סוף.' and HB0(357, 44).startswith('רבי אלעזר אומר: לכל האתת והמופתים ומנין אף לפני הר סיני') and '(דברים ט יז)' in HB0(357, 44) and HB0(357, 44).endswith('אשר עשה משה לעיני כל ישראל.')
assert all(clean(sif[p - 1][0]).startswith('Pisqa’ %d' % p) for p in PISKAOT) and 'And Moses ascended' in clean(sif[356][0]) and 'The Primordial God is a refuge' in clean(sif[355][0])   # the English rows open with the translator's apparatus before the text (sitting 19's lesson)
# THE CITATIONS PARSED FROM THE DUMP'S PRINT (the instrument's own lists read back): the row-citations per file, the union, the outside set; the divisions; the store
import ast as _ast
_t = open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'ch34_dump0.out'), encoding='utf-8').read()
_HE = _ast.literal_eval(re.search(r'^  HE rows citing Deut 34[^:]*: \d+ (\[.*\])$', _t, re.M).group(1)); _EN = _ast.literal_eval(re.search(r'^  EN rows citing Deut 34[^:]*: \d+ (\[.*\])$', _t, re.M).group(1))
_un = int(re.search(r'^  the union of rows \(both files\): (\d+) \[', _t, re.M).group(1)); _out = _ast.literal_eval(re.search(r'^  the rows OUTSIDE the spine piskaot [^:]*: \d+ (\[.*?\]) \|', _t, re.M).group(1)); _insp = int(re.search(r'\| in-spine rows of the union: (\d+)$', _t, re.M).group(1))
_two = re.search(r'^  DB verses (\d+) \| export verses HE (\d+) EN (\d+) \| per-chapter export lengths vs DB, chapters 1-34: (\[.*\])$', _t, re.M); _cost = int(re.search(r'^  the alignment cost (\d+) \|', _t, re.M).group(1))
_mis = _ast.literal_eval(re.search(r'verses whose store token count differs from the DB: (\[.*?\])$', _t, re.M).group(1)); _tok = int(re.search(r'^  token count chapter 34 : (\d+)$', _t, re.M).group(1))
assert (len(_HE), len(_EN), _un, _insp) == (13, 66, 43, 41) and _out == OUTSIDE and len(_out) == 2, (len(_HE), len(_EN), _un, _insp, _out)   # 13 Hebrew and 66 English row-citations; the union 43 rows — 41 inside 357 (three of its rows cite nothing in the Hebrew and 34's verse in neither file: 357:14, 23, 25), 2 outside
assert tuple(int(x) for x in _two.groups()[:3]) == (12, 12, 12) and _two.group(4) == '[(5, 30, 33)]' and _cost == 5, 'THE TWO DIVISIONS: the identity; chapter 5 the book\'s one split'
assert _mis == [] and _tok == 176, (_mis, _tok)   # THE STORE = THE DB at every verse (no ketiv-qere doubling in the chapter); 176 tokens
_sp = open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'ch34_split.out'), encoding='utf-8').read()
assert re.search(r'^spine piskaot 357 - 357 1 \| rows per piska \{357: 44\} \| totals \{34: 44\} 44$', _sp, re.M) and re.search(r'^the run plan under 90000 bytes a slice: \[\(\(357, 357\), 1, 42152\)\] \| slices 1$', _sp, re.M) and 'after: NO PISKA — the export ends at 357' in _sp
_seat = _ast.literal_eval(re.search(r'^the rows of 357 citing a chapter-34 verse in the Hebrew \(the seat rule by row\): (\[.*\])$', _sp, re.M).group(1))
SEAT_ROWS = {r: vs[0] for r, vs in _seat}   # the citing rows of 357 and the verse each cites (the Hebrew marker) — the seat rule by row's anchors
assert SEAT_ROWS == {1: 1, 8: 2, 19: 3, 26: 4, 28: 5, 31: 6, 33: 7, 36: 8, 38: 9, 40: 10, 42: 11} and all(len(vs) == 1 for _, vs in _seat), SEAT_ROWS   # eleven citing rows, one per verse 34:1-11 in order; 34:12 cited by no Hebrew marker (its words quoted at 357:43-44 — the English cites it there)
# THE OUTSIDE ROWS' FACTS COMPUTED from the dump's lists: the verses each row cites (the DB's numbering), the heads of their piskaot, the prior reads from the ledgers, the fresh rows
CITED = {}
for _p, _r, _e, _dbv in _HE + _EN:
    if (_p, _r) in OUTSIDE:
        for _d in _dbv: CITED.setdefault((_p, _r), set()).add((34, _d))
CITED = {k: sorted(v) for k, v in sorted(CITED.items())}
assert sorted(CITED) == OUTSIDE, (sorted(set(OUTSIDE) - set(CITED)), sorted(set(CITED) - set(OUTSIDE)))
assert CITED == {(305, 5): [(34, 6)], (341, 1): [(34, 4)]}, CITED   # the angel of death sent for Moses' soul and the burial by the Holy One (305:5 on 34:6, from 31:14's piska, headless); "from afar you shall see the land" read against "you shall not cross over" (341:1 on 34:4, from 32:52's piska)
HEADS_ON = {p: heads[p] for p in sorted({p for p, _ in OUTSIDE})}
assert HEADS_ON == {305: None, 341: (32, 52)}, HEADS_ON   # 305's first row opens with no citation marker (headless to the instrument — the piska of 31:14 "behold, your days approach to die")
assert HB0(305, 5).startswith('באותה שעה אמר הקדוש ברוך הוא למלאך המות: לך והבא לי נשמתו של משה') and HB0(341, 1).startswith('(דברים לב נב) כי מנגד תראה את הארץ ושמה לא תבא, נאמר כאן ושמה לא תבא ונאמר להלן'), (HB0(305, 5)[:60], HB0(341, 1)[:60])
_TRI = f'{ROOT}/logic/oral_triage'
LED = {f: open(f'{_TRI}/{f}', encoding='utf-8').read() for f in os.listdir(_TRI) if f.endswith('.md') and os.path.isfile(f'{_TRI}/{f}') and f != os.path.basename(OUT)}
SPINE_PRIOR = sorted({(f, int(a), int(b)) for f, t in LED.items() for a, b in re.findall(r'Sifrei Devarim (\d+):(\d+)', t) if int(a) in PISKAOT})
PRIOR_READ = {}
for f, t in LED.items():
    for a, b in re.findall(r'Sifrei Devarim (\d+):(\d+)', t):
        if (int(a), int(b)) in OUTSIDE: PRIOR_READ.setdefault((int(a), int(b)), []).append(f)
PRIOR_READ = {k: sorted(set(v)) for k, v in sorted(PRIOR_READ.items())}
FRESH = [k for k in OUTSIDE if k not in PRIOR_READ]
assert SPINE_PRIOR == [('deu_05_vaetchanan_2026-09-16.md', 357, 40), ('deu_09_ekev_2026-09-19.md', 357, 44), ('deu_29_31_nitzavim_vayelech_2026-09-27.md', 357, 28), ('deu_32_haazinu_2026-09-27.md', 357, 27)], SPINE_PRIOR   # FOUR spine rows READ BEFORE over four ledgers (the dump's list): no prophet like Moses (357:40 at chapter 5), the tablets broken (357:44 at chapter 9), Moses died there (357:28 at 29-31), you shall not cross over (357:27 at the song) — REREAD WHOLE here under the whole-row rule and marked so
assert sorted(PRIOR_READ) == OUTSIDE and FRESH == [] and PRIOR_READ == {(305, 5): ['deu_29_31_nitzavim_vayelech_2026-09-27.md'], (341, 1): ['deu_32_haazinu_2026-09-27.md']}, (PRIOR_READ, FRESH)   # EVERY OUTSIDE ROW READ BEFORE — 305:5 at chapters 29-31, 341:1 at the song: none fresh (the walk's second reading without a fresh outside row)
# THE FRAMES AND THE NAMES (the dump's D section): ONE divine frame with "saying" — 34:4 "and the LORD said to him … saying" (the oath to the fathers); "for" (ki) at 34:9 alone; no "if", no "lest"; no imperative; ONE prohibition-form "you shall not cross over" (34:4); the first person at 34:4 alone (I swore, I will give it, I have caused you to see); the second person singular at 34:4 alone
assert [(c, v) for c, v in SPAN if 'לאמר' in W(c, v)] == [(34, 4)] and [(c, v) for c, v in SPAN for i, x in enumerate(W(c, v)[:-1]) if x == 'ויאמר' and W(c, v)[i + 1] == 'יהוה'] == [(34, 4)] and [(c, v) for c, v in SPAN if 'כי' in W(c, v)] == [(34, 9)] and [(c, v) for c, v in SPAN if 'אם' in W(c, v) or 'ואם' in W(c, v) or 'פן' in W(c, v)] == []
NARR = {v: [x for x, m in wm('Deut', 34, v) if m and re.search(r'V.w', m)] for _, v in SPAN if any(m and re.search(r'V.w', m) for _, m in wm('Deut', 34, v))}
assert NARR == {1: ['ויעל', 'ויראהו'], 4: ['ויאמר'], 5: ['וימת'], 6: ['ויקבר'], 8: ['ויבכו', 'ויתמו'], 9: ['וישמעו', 'ויעשו']}, NARR   # the narrative past: he went up, He showed him (34:1); He said (34:4); he died (34:5); He buried (34:6); they wept, they were ended (34:8); they hearkened, they did (34:9) — nine acts in six verses; 34:2-3, 7, 10-12 verbless or descriptive
assert [(v, x) for _, v in SPAN for x, m in wm('Deut', 34, v) if m and re.search(r'^HV..v', m)] == [] and [(v, x) for _, v in SPAN for x, m in wm('Deut', 34, v) if m and re.search(r'1c[sp]', m) and m.startswith('HV')] == [(4, 'נשבעתי'), (4, 'אתננה'), (4, 'הראיתיך')] and {v: sum(1 for _, m in wm('Deut', 34, v) if m and '2ms' in m) for _, v in SPAN if any(m and '2ms' in m for _, m in wm('Deut', 34, v))} == {4: 4}
assert 'לא' in W(34, 4) and W(34, 4)[W(34, 4).index('לא') + 1] == 'תעבר' and sum(1 for c, v in SPAN for x in W(c, v) if x in ('לא', 'ולא')) == 5 and [(c, v) for c, v in SPAN if any(x in ('לא', 'ולא') for x in W(c, v))] == [(34, 4), (34, 6), (34, 7), (34, 10)]   # "not" five times: you shall not cross over (34:4), no man knows (34:6), his eye not dim, his force not abated (34:7), no prophet arose (34:10)
assert 'משה' in W(34, 1) and 'נבו' in W(34, 1) and 'הפסגה' in W(34, 1) and 'ירחו' in W(34, 1) and 'הגלעד' in W(34, 1) and 'דן' in W(34, 1) and 'נפתלי' in W(34, 2) and 'אפרים' in W(34, 2) and 'ומנשה' in W(34, 2) and 'יהודה' in W(34, 2) and 'צער' in W(34, 3) and 'לאברהם' in W(34, 4) and 'ליצחק' in W(34, 4) and 'וליעקב' in W(34, 4) and 'פעור' in W(34, 6) and 'ויהושע' in W(34, 9) and 'נון' in W(34, 9) and 'מצרים' in W(34, 11) and 'לפרעה' in W(34, 11)
assert [(c, v) for c, v in SPAN if 'ישראל' in W(c, v)] == [(34, 8), (34, 9), (34, 12)] and 'בישראל' in W(34, 10) and 'כמשה' in W(34, 10) and [(c, v) for c, v in SPAN if 'מואב' in W(c, v)] == [(34, 1), (34, 5), (34, 6), (34, 8)] and 'מערבת' in W(34, 1) and 'בערבת' in W(34, 8)   # Israel at 34:8, 9, 12 and "in Israel" 34:10; Moab FOUR times — the plains of Moab at 34:1 and 34:8, the land of Moab at 34:5 and 34:6 (the first pass typed three from memory; the print says four)
assert 'מאה' in W(34, 7) and 'ועשרים' in W(34, 7) and 'שלשים' in W(34, 8) and W(34, 7)[:5] == ['ומשה', 'בן', 'מאה', 'ועשרים', 'שנה'] and W(34, 8)[7:9] == ['שלשים', 'יום']   # the two number seats: a hundred and twenty years (34:7 — 31:2's number), thirty days (34:8)
assert [(c, v, x) for c, v in SPAN for x in W(c, v) if x in ('יהוה', 'ליהוה', 'ביהוה', 'ויהוה')] == [(34, 1, 'יהוה'), (34, 4, 'יהוה'), (34, 5, 'יהוה'), (34, 5, 'יהוה'), (34, 9, 'יהוה'), (34, 10, 'יהוה'), (34, 11, 'יהוה')] and not any(x in ('אלהים', 'האלהים', 'אלהיך', 'אלהי', 'אלוה') for c, v in SPAN for x in W(c, v)) and [(c, v) for c, v in SPAN if 'אל' in W(c, v)] == [(34, 1), (34, 10)]   # the Name SEVEN times bare (34:1, 4, 5 twice — the servant of the LORD, by the mouth of the LORD — 9, 10, 11); no "God" in the chapter — the two-letter "el" at 34:1 ("to Mount Nebo") and 34:10 ("face to face") is the PREPOSITION, a homograph of God's name for the compile's scans (the first pass counted it as God)
# ---- THE ASSERTS TYPED FROM THE MEASURE'S PRINT (block b: ch34_measure_lean.out — the kin, the twins, the formulas, Onkelos, the frames, the register, the parser, the prior reads) ----
# THE KIN BY COMPUTATION: the ascent's kin is the command to ascend — 34:1 with 32:49 (eight shared, "that is over against Jericho" four in order); THE OATH IS EXODUS 33:1's — 34:4 with Exodus 33:1 ten shared, NINE IN ORDER ("the land which I swore to Abraham, to Isaac and to Jacob, saying: to your seed I will give it" — the one line of the chapter taken whole from an earlier book); the years' kin 31:2 (the marker's verse); the weeping's kin the plains of Moab of Numbers' own footer (26:63, 36:13); Joshua's kin the tabernacle's receipt formula (Exodus 12:28, 12:50 — "as the LORD commanded Moses, so they did"); the signs' kin 29:1 (Pharaoh, his servants, his land); 34:3, 34:5, 34:6 and 34:10 kin only to the Writings and the Prophets by the instrument (2 Chronicles 28:15's city of palms; 1 Chronicles 1:46; 1 Samuel 17:25; 1 Chronicles 19:10) — cited never read; no verse of the chapter shares no two tokens with any verse
assert [v for c, v in SPAN if not KINC[(c, v)]] == [], [v for c, v in SPAN if not KINC[(c, v)]]
assert KINC[(34, 1)][0] == ('Deut 32:49', 5, 8) and KINC[(34, 4)][0] == ('Exod 33:1', 7, 10) and KINC[(34, 7)][0] == ('Deut 31:2', 4, 5) and KINC[(34, 8)][0] == ('Num 26:63', 5, 4) and KINC[(34, 9)][0] == ('Exod 12:28', 5, 7) and KINC[(34, 11)][0] == ('Deut 29:1', 5, 9) and KINC[(34, 12)][0] == ('Deut 29:1', 4, 2), (KINC[(34, 1)][0], KINC[(34, 4)][0], KINC[(34, 7)][0], KINC[(34, 8)][0], KINC[(34, 9)][0], KINC[(34, 11)][0], KINC[(34, 12)][0])
assert KINC[(34, 3)][0] == ('2Chr 28:15', 3, 3) and KINC[(34, 2)][0] == ('1Chr 9:3', 3, 2) and KINC[(34, 5)][0] == ('1Chr 1:46', 2, 2) and KINC[(34, 6)][0] == ('1Sam 17:25', 3, 1) and KINC[(34, 10)][0] == ('1Chr 19:10', 2, 1), (KINC[(34, 3)][0], KINC[(34, 2)][0], KINC[(34, 5)][0], KINC[(34, 6)][0], KINC[(34, 10)][0])
# THE TWINS DIFFED (shared / the longest run): the oath 34:4 with Exodus 33:1 NINE IN ORDER and with 6:10 and 30:20 the three fathers; "you shall not cross over" 34:4 with 3:27's "you shall not cross this Jordan" (two in order); the ascent 34:1 with 32:49 four in order and with 3:27 "the top of Pisgah"; THE DEATH IS AARON'S — 34:5 with Numbers 33:38 "by the mouth of the LORD" (three), 34:7 with Numbers 33:39 "years … when he died" (the one other seat of "when he died"), 34:8 with Numbers 20:29 "thirty days" (Aaron's thirty; the one other seat), and 34:5 with 32:50 ("as Aaron your brother died") SHARES NO TOKEN — the twin by sense alone; "Moses the servant of the LORD" 34:5 with Joshua 1:1 three in order (the Prophets' first verse — cited never read); the years 34:7 with 31:2 four in order and with Genesis 6:3's hundred and twenty three; Joshua 34:9 with Numbers 27:23 "his hands upon him" (six shared) and 27:18, with 31:23 six shared, with Exodus 28:3 and Isaiah 11:2 "the spirit of wisdom"; "face to face" 34:10 with Exodus 33:11 (four shared), Genesis 32:31 (Jacob at Peniel), Judges 6:22 and Ezekiel 20:35 — and with Numbers 12:8's "mouth to mouth" ONE token ("and not"): the twin by sense; "a prophet" 34:10 with 18:15 and 18:18; the signs 34:11 with Exodus 7:3 and Jeremiah 32:20 "in the land of Egypt"; the mighty hand 34:12 with Exodus 14:31 "which … did" (the great hand at the sea — three shared) and with 4:34; 34:12 with 9:17 (the Sifrei's join at 357:44 — the tablets broken before your eyes) SHARES NOTHING: the Sifrei's link by sense, its own; 34:6 with 33:21 (the lawgiver's portion) SHARES NOTHING — Onkelos alone joined them at the blessing
assert SHARED(('Deut', 34, 4), ('Exod', 33, 1)) == ['הארץ', 'אשר', 'נשבעתי', 'לאברהם', 'ליצחק', 'וליעקב', 'לאמר', 'לזרעך', 'אתננה'] and SHN(('Deut', 34, 4), ('Exod', 33, 1)) == 10 and SHARED(('Deut', 34, 4), ('Deut', 6, 10)) == ['לאברהם', 'ליצחק', 'וליעקב'] and SHN(('Deut', 34, 4), ('Deut', 6, 10)) == 7 and SHARED(('Deut', 34, 4), ('Deut', 3, 27)) == ['לא', 'תעבר'] and SHARED(('Deut', 34, 4), ('Gen', 26, 3)) == ['אשר', 'נשבעתי', 'לאברהם']
assert SHARED(('Deut', 34, 1), ('Deut', 32, 49)) == ['אשר', 'על', 'פני', 'ירחו'] and SHN(('Deut', 34, 1), ('Deut', 32, 49)) == 8 and SHARED(('Deut', 34, 1), ('Deut', 3, 27)) == ['ראש', 'הפסגה'] and SHARED(('Deut', 34, 1), ('Num', 27, 12)) == ['אל', 'הר'] and SHN(('Deut', 34, 1), ('Num', 27, 12)) == 4
assert SHARED(('Deut', 34, 5), ('Num', 33, 38)) == ['על', 'פי', 'יהוה'] and SHN(('Deut', 34, 5), ('Deut', 32, 50)) == 0 and SHARED(('Deut', 34, 5), ('Josh', 1, 1)) == ['משה', 'עבד', 'יהוה'] and SHN(('Deut', 34, 5), ('Josh', 1, 1)) == 4 and SHARED(('Deut', 34, 5), ('Num', 20, 28)) == ['וימת']
assert SHARED(('Deut', 34, 6), ('Deut', 3, 29)) == ['מול', 'בית', 'פעור'] and SHARED(('Deut', 34, 6), ('Deut', 4, 46)) == ['מול', 'בית', 'פעור'] and SHN(('Deut', 34, 6), ('Deut', 33, 21)) == 0 and SHARED(('Deut', 34, 6), ('Gen', 50, 13)) == ['אתו']
assert SHARED(('Deut', 34, 7), ('Deut', 31, 2)) == ['בן', 'מאה', 'ועשרים', 'שנה'] and SHN(('Deut', 34, 7), ('Deut', 31, 2)) == 5 and SHARED(('Deut', 34, 7), ('Gen', 6, 3)) == ['מאה', 'ועשרים', 'שנה'] and SHARED(('Deut', 34, 7), ('Num', 33, 39)) == ['שנה', 'במתו'] and SHN(('Deut', 34, 7), ('Num', 33, 39)) == 4 and SHARED(('Deut', 34, 7), ('Exod', 7, 7)) == ['ומשה', 'בן'] and SHN(('Deut', 34, 7), ('Gen', 27, 1)) == 0
assert SHARED(('Deut', 34, 8), ('Num', 20, 29)) == ['שלשים', 'יום'] and SHN(('Deut', 34, 8), ('Num', 20, 29)) == 4 and SHARED(('Deut', 34, 8), ('Gen', 50, 3)) == ['ויבכו'] and SHARED(('Deut', 34, 8), ('Gen', 50, 10)) == ['אבל']
assert SHARED(('Deut', 34, 9), ('Num', 27, 23)) == ['את', 'ידיו', 'עליו'] and SHN(('Deut', 34, 9), ('Num', 27, 23)) == 6 and SHARED(('Deut', 34, 9), ('Num', 27, 18)) == ['בן', 'נון'] and SHN(('Deut', 34, 9), ('Num', 27, 18)) == 5 and SHN(('Deut', 34, 9), ('Deut', 31, 23)) == 6 and SHARED(('Deut', 34, 9), ('Exod', 28, 3)) == ['רוח', 'חכמה'] and SHARED(('Deut', 34, 9), ('Isa', 11, 2)) == ['רוח', 'חכמה'] and SHARED(('Deut', 34, 9), ('Num', 27, 20)) == ['בני', 'ישראל']
assert SHARED(('Deut', 34, 10), ('Exod', 33, 11)) == ['פנים', 'אל', 'פנים'] and SHN(('Deut', 34, 10), ('Exod', 33, 11)) == 4 and SHARED(('Deut', 34, 10), ('Gen', 32, 31)) == ['פנים', 'אל', 'פנים'] and SHARED(('Deut', 34, 10), ('Judg', 6, 22)) == ['יהוה', 'פנים', 'אל', 'פנים'] and SHARED(('Deut', 34, 10), ('Ezek', 20, 35)) == ['פנים', 'אל', 'פנים'] and SHARED(('Deut', 34, 10), ('Num', 12, 8)) == ['ולא'] and SHARED(('Deut', 34, 10), ('Deut', 18, 15)) == ['נביא'] and SHARED(('Deut', 34, 10), ('Deut', 18, 18)) == ['נביא']
assert SHARED(('Deut', 34, 11), ('Exod', 7, 3)) == ['בארץ', 'מצרים'] and SHARED(('Deut', 34, 11), ('Jer', 32, 20)) == ['בארץ', 'מצרים'] and SHN(('Deut', 34, 11), ('Jer', 32, 20)) == 3 and SHARED(('Deut', 34, 12), ('Exod', 14, 31)) == ['אשר', 'עשה'] and SHN(('Deut', 34, 12), ('Exod', 14, 31)) == 3 and SHARED(('Deut', 34, 12), ('Deut', 4, 34)) == ['אשר', 'עשה'] and SHN(('Deut', 34, 12), ('Deut', 9, 17)) == 0 and SHARED(('Deut', 34, 12), ('Deut', 7, 19)) == ['החזקה'] and SHARED(('Deut', 34, 12), ('Deut', 3, 24)) == ['החזקה']
assert SHARED(('Deut', 34, 2), ('Deut', 11, 24)) == ['הים', 'האחרון'] and SHARED(('Deut', 34, 3), ('2Chr', 28, 15)) == ['ירחו', 'עיר', 'התמרים'] and SHARED(('Deut', 34, 3), ('Judg', 3, 13)) == ['עיר', 'התמרים'] and SHARED(('Deut', 34, 3), ('Judg', 1, 16)) == ['התמרים']
# THE FORMULAS: TWENTY-THREE phrases of the chapter ONCE in the Bible over the measure's list — "from the plains of Moab", "and the LORD showed him", "all Naphtali", "the land of Ephraim and Manasseh", "all the land of Judah", "the valley of Jericho", "I have caused you to see", "you shall not cross over there", "and Moses died there", "no man knows", "his grave", "his eye was not dim", "nor his natural force abated", "and the children of Israel wept", "the days of weeping", "the mourning for Moses", "full of the spirit of wisdom", "laid his hands upon him", "there arose not a prophet", "like Moses", "whom the LORD knew", "the mighty hand" (with the article — the formula's other seats say "a mighty hand"), "the great terror"; THE PAIRS — "Mount Nebo" and "over against Jericho" 32:49 and 34:1 alone; "to your seed I will give it" Exodus 33:1 and 34:4 alone; "a hundred and twenty years old" 31:2 and 34:7 alone; "when he died" 34:7 and Numbers 33:39 (Aaron) alone; "thirty days" 34:8 and Numbers 20:29 (Aaron) alone; "to Pharaoh and to all his servants" 29:1 and 34:11 alone; "in the sight of all Israel" 31:7 and 34:12 in the Torah; "the servant of the LORD" ONCE IN THE TORAH and nineteen in the Bible (the book of Joshua's title for Moses — cited never read); "and Moses went up" five — Sinai's four ascents (Exodus 19:20, 24:9, 13, 15) and this last; "in the plains of Moab" eight — Numbers' own seats (26:3, 26:63, 33:48-50, 35:1, 36:13 the footer) and 34:8; "by the mouth of the LORD" eighteen in the Torah (Numbers 33:38 — Aaron's death — among them); "as the LORD commanded Moses" thirty-eight in the Torah (the tabernacle's receipts) and 34:9 the last; "face to face" three in the Torah; "the LORD your God" 192 seats in the Torah and NONE in the chapter — the death never says "the LORD your God", as the song and the blessing did not; the Name SEVEN times bare, no "God" (the two-letter "el" the preposition)
Q34 = [('מערבת', 'מואב'), ('ויראהו', 'יהוה'), ('ואת', 'כל', 'נפתלי'), ('ארץ', 'אפרים', 'ומנשה'), ('כל', 'ארץ', 'יהודה'), ('בקעת', 'ירחו'), ('הראיתיך',), ('ושמה', 'לא', 'תעבר'), ('וימת', 'שם', 'משה'), ('ולא', 'ידע', 'איש'), ('קברתו',), ('לא', 'כהתה', 'עינו'), ('ולא', 'נס', 'לחה'), ('ויבכו', 'בני', 'ישראל'), ('ימי', 'בכי'), ('אבל', 'משה'), ('מלא', 'רוח', 'חכמה'), ('סמך', 'משה', 'את', 'ידיו', 'עליו'), ('ולא', 'קם', 'נביא'), ('כמשה',), ('אשר', 'ידעו', 'יהוה'), ('היד', 'החזקה'), ('המורא', 'הגדול')]
ONCE = [seq for seq in Q34 if len(P(*seq, books=None)) == 1 and P(*seq, books=None)[0].startswith('Deut 34:')]
assert len(ONCE) == 23 and len(Q34) == 23, (len(ONCE), [s for s in Q34 if s not in ONCE])
assert P('הר', 'נבו', books=None) == ['Deut 32:49', 'Deut 34:1'] and P('על', 'פני', 'ירחו', books=None) == ['Deut 32:49', 'Deut 34:1'] and P('לזרעך', 'אתננה', books=None) == ['Deut 34:4', 'Exod 33:1'] and P('בן', 'מאה', 'ועשרים', 'שנה', books=None) == ['Deut 31:2', 'Deut 34:7'] and P('במתו', books=None) == ['Deut 34:7', 'Num 33:39'] and P('שלשים', 'יום', books=None) == ['Deut 34:8', 'Num 20:29'] and P('לפרעה', 'ולכל', 'עבדיו', books=None) == ['Deut 29:1', 'Deut 34:11'] and P('לעיני', 'כל', 'ישראל', books=T) == ['Deut 31:7', 'Deut 34:12']
assert len(P('עבד', 'יהוה', books=T)) == 1 and len(P('עבד', 'יהוה', books=None)) == 19 and P('ויעל', 'משה', books=None) == ['Deut 34:1', 'Exod 19:20', 'Exod 24:13', 'Exod 24:15', 'Exod 24:9'] and len(P('בערבת', 'מואב', books=None)) == 8 and 'Num 36:13' in P('בערבת', 'מואב', books=None) and len(P('על', 'פי', 'יהוה', books=T)) == 18 and 'Num 33:38' in P('על', 'פי', 'יהוה', books=T) and len(P('כאשר', 'צוה', 'יהוה', 'את', 'משה', books=T)) == 38 and len(P('פנים', 'אל', 'פנים', books=T)) == 3 and len(P('פנים', 'אל', 'פנים', books=None)) == 5
assert P('מול', 'בית', 'פעור', books=None) == ['Deut 34:6', 'Deut 3:29', 'Deut 4:46'] and P('רוח', 'חכמה', books=None) == ['Deut 34:9', 'Exod 28:3', 'Isa 11:2'] and P('ויקבר', 'אתו', books=None) == ['2Kgs 21:26', 'Deut 34:6'] and P('עד', 'צער', books=None) == ['Deut 34:3', 'Isa 15:5'] and P('עיר', 'התמרים', books=None) == ['2Chr 28:15', 'Deut 34:3', 'Judg 3:13'] and P('הים', 'האחרון', books=T) == ['Deut 11:24', 'Deut 34:2'] and P('עד', 'דן', books=T) == ['Deut 34:1', 'Gen 14:14'] and len(P('ראש', 'הפסגה', books=None)) == 4
assert len(P('יהוה', 'אלהיך', books=T)) == 192 and not [v for c, v in SPAN if any(a == 'יהוה' and b == 'אלהיך' for a, b in zip(W(c, v), W(c, v)[1:]))] and sum(1 for c, v in SPAN for x in W(c, v) if x == 'יהוה') == 7
# THE NAMES AND THE PARTICLES (the measure's C): Moses eight times (34:1, 5, 7, 8 twice, 9 twice, 12) and "like Moses" once (34:10); Israel at 34:8, 9, 12 and "in Israel" 34:10; Moab four; the tribes Naphtali, Ephraim, Manasseh, Judah (34:2) and Dan as a border (34:1); Nebo, Pisgah, Jericho (twice), Gilead, Zoar, Beth-peor, Egypt, Pharaoh; the three fathers; Joshua son of Nun; "there" (34:5) and "thither" (34:4); "all" nine times; "as far as" four
assert [(c, v) for c, v in SPAN for x in W(c, v) if x in ('משה', 'ומשה')] == [(34, 1), (34, 5), (34, 7), (34, 8), (34, 8), (34, 9), (34, 9), (34, 12)] and [(c, v, x) for c, v in SPAN for x in W(c, v) if x in ('שם', 'ושמה', 'שמה')] == [(34, 4, 'ושמה'), (34, 5, 'שם')] and sum(1 for c, v in SPAN for x in W(c, v) if x in ('כל', 'וכל', 'ולכל', 'לכל', 'בכל')) == 9 and sum(1 for c, v in SPAN for x in W(c, v) if x == 'עד') == 4
assert [(c, v, x) for c, v in SPAN for x in W(c, v) if x in ('אמר', 'ויאמר')] == [(34, 4, 'ויאמר')] and W(34, 11)[:3] == ['לכל', 'האתות', 'והמופתים'] and W(34, 12)[:6] == ['ולכל', 'היד', 'החזקה', 'ולכל', 'המורא', 'הגדול']   # the one "he said"; the signs plene (the measure's defective spelling found no seat — the instrument's, not the text's)
# ONKELOS WRITING THE MEANING (the measure's D): the Pisgah "the head of THE HEIGHT" (ramata — 3:27's word); the hinder sea "THE WESTERN sea" (34:2 — maarva's four seats 3:27, 11:24, 33:23, 34:2); the south daroma, the plain meishra (34:1, 3, 8 — sixteen seats in the book), "the city of PALMS" (dikelaya — one seat); THE OATH "which I SWORE (kayemit) … to your SONS I will give it" (34:4 — the seed rendered the sons); "THITHER you shall not cross" (le-tamman); "MOSES THE SERVANT OF THE LORD died there … BY THE MEMRA OF THE LORD" (34:5 — the mouth rendered the Word: the Memra's ninety-one seats in the book); the valley cheilta (34:6 — 3:29's and 4:46's word, three seats) and "his grave" kevurteih (four seats — 10:6 Aaron's among them); "his eyes were not dimmed AND THE SPLENDOR OF THE GLORY OF HIS FACE DID NOT CHANGE" (34:7 — the natural force rendered the shining face of Exodus 34:29; ziv's three seats 1:33, 33:17, 34:7; yekar's nine, 33:2 and 34:7 the last two; fifteen Aramaic words for twelve Hebrew); "thirty days" telatin (2:14's word, the thirty-eight years — two seats); "AND THE CHILDREN OF ISRAEL RECEIVED FROM HIM" (34:9 — "hearkened to him" rendered kabbalah's verb, the chain of transmission's (Avot 1:1 "received"); semakh — the hands laid — ONE seat in the book, 34:9; wisdom's two seats 4:6 and 34:9); "TO WHOM THE LORD WAS REVEALED face to face" (34:10 — apin be-apin; the prophet's eleven seats, 33:1's prophet of the LORD and 34:10 the last); the signs atin (twelve) and the wonders mofetin (nine — 34:11 the last of each); "THE GREAT VISION" for the great terror (34:12 — chezvana, fifteen seats: 4:34, 26:8 and 34:12 the sights of Egypt); the mighty hand yeda takifta (34:12 — twenty-two seats)
assert ARM(34, 1)[:9] == ['וסלק', 'משה', 'ממישרא', 'דמואב', 'לטורא', 'דנבו', 'ריש', 'רמתא', 'די'] and ARM(34, 2)[-2:] == ['ימא', 'מערבא'] and ARM(34, 3) == ['וית', 'דרומא', 'וית', 'מישרא', 'בקעתא', 'דירחו', 'קרתא', 'דדקליא', 'עד', 'צער'], (ARM(34, 1)[:9], ARM(34, 2)[-2:], ARM(34, 3))
assert ARM(34, 4) == ['ואמר', 'יי', 'ליה', 'דא', 'ארעא', 'די', 'קימית', 'לאברהם', 'ליצחק', 'וליעקב', 'למימר', 'לבניך', 'אתננה', 'אחזיתך', 'בעיניך', 'ולתמן', 'לא', 'תעבר'] and ARM(34, 5) == ['ומית', 'תמן', 'משה', 'עבדא', 'דיי', 'בארעא', 'דמואב', 'על', 'מימרא', 'דיי'], (ARM(34, 4), ARM(34, 5))
assert ARM(34, 6) == ['וקבר', 'יתיה', 'בחילתא', 'בארעא', 'דמואב', 'לקבל', 'בית', 'פעור', 'ולא', 'ידע', 'אנש', 'ית', 'קברתיה', 'עד', 'יומא', 'הדין'] and ARM(34, 7) == ['ומשה', 'בר', 'מאה', 'ועשרין', 'שנין', 'כד', 'מית', 'לא', 'כהת', 'עינוהי', 'ולא', 'שנא', 'זיו', 'יקרא', 'דאפוהי'] and len(ARM(34, 7)) == 15 and len(W(34, 7)) == 12, (ARM(34, 6), ARM(34, 7))
assert ARM(34, 8) == ['ובכו', 'בני', 'ישראל', 'ית', 'משה', 'במישריא', 'דמואב', 'תלתין', 'יומין', 'ושלימו', 'יומי', 'בכיתא', 'אבלא', 'דמשה'] and ARM(34, 9) == ['ויהושע', 'בר', 'נון', 'מלי', 'רוח', 'חכמתא', 'ארי', 'סמך', 'משה', 'ית', 'ידוהי', 'עלוהי', 'וקבילו', 'מניה', 'בני', 'ישראל', 'ועבדו', 'כמא', 'די', 'פקיד', 'יי', 'ית', 'משה'], (ARM(34, 8), ARM(34, 9))
assert ARM(34, 10) == ['ולא', 'קם', 'נביא', 'עוד', 'בישראל', 'כמשה', 'די', 'אתגלי', 'ליה', 'יי', 'אפין', 'באפין'] and ARM(34, 11) == ['לכל', 'אתיא', 'ומופתיא', 'די', 'שלחיה', 'יי', 'למעבד', 'בארעא', 'דמצרים', 'לפרעה', 'ולכל', 'עבדוהי', 'ולכל', 'ארעיה'] and ARM(34, 12) == ['ולכל', 'ידא', 'תקפתא', 'ולכל', 'חזונא', 'רבא', 'די', 'עבד', 'משה', 'לעיני', 'כל', 'ישראל'], (ARM(34, 10), ARM(34, 11), ARM(34, 12))
assert SEATS('מימר') and len(SEATS('מימר')) == 91 and (34, 4) in SEATS('מימר') and (34, 5) in SEATS('מימר') and SEATS('נבי') == [(13, 2), (13, 4), (13, 6), (14, 21), (18, 15), (18, 18), (18, 20), (18, 22), (23, 25), (33, 1), (34, 10)] and SEATS('קבר') == [(9, 22), (10, 6), (21, 23), (34, 6)] and SEATS('חילת') == [(3, 29), (4, 46), (34, 6)] and SEATS('פעור') == [(3, 29), (4, 3), (4, 46), (34, 6)]
assert SEATS('מערב') == [(3, 27), (11, 24), (33, 23), (34, 2)] and SEATS('דרומ') == [(1, 7), (3, 27), (33, 23), (34, 3)] and SEATS('צער') == [(34, 3)] and SEATS('דקל') == [(34, 3)] and len(SEATS('מישר')) == 16 and all(k in SEATS('מישר') for k in ((34, 1), (34, 3), (34, 8))) and SEATS('חכמ') == [(4, 6), (34, 9)] and SEATS('סמך') == [(34, 9)]
assert len(SEATS('אתי')) == 12 and SEATS('אתי')[-1] == (34, 11) and len(SEATS('מופת')) == 9 and SEATS('מופת')[-1] == (34, 11) and len(SEATS('תקיפ')) == 22 and len(SEATS('חזו')) == 15 and SEATS('חזו')[-1] == (34, 12) and (4, 34) in SEATS('חזו') and (26, 8) in SEATS('חזו') and SEATS('אבל') == [(8, 4), (26, 14), (34, 8)] and SEATS('תלתין') == [(2, 14), (34, 8)] and SEATS('זיו') == [(1, 33), (33, 17), (34, 7)] and len(SEATS('יקר')) == 9 and SEATS('יקר')[-2:] == [(33, 2), (34, 7)] and SEATS('פרעה')[-1] == (34, 11) and len(SEATS('פרעה')) == 7
assert len(SEATS('אורית')) == 25 and SEATS('אורית')[-3:] == [(33, 2), (33, 4), (33, 10)] and SEATS('עלמ') == [(32, 7), (32, 12), (32, 40), (33, 6), (33, 27)] and not any(k[0] == 34 for k in SEATS('אורית') + SEATS('עלמ'))   # the Torah's twenty-five Aramaic seats end at 33:10 (the twenty-fifth past the measure's cut of twenty-four — sitting 21's lesson met again: the first typed pass read the cut list's last as the last) and the world's five at 33:27 — neither word in the death's chapter
# THE FRAMES, THE REGISTER AND THE PARSER (the measure's E): no imperative, no jussive, no infinitive absolute; the one frame 34:4 (the narrative past with the Name); the death 34:5 "and he died" the narrative past; Joshua 34:9 "full" an adjective, "laid" the perfect; THE REGISTER — ONE RECEIPT at 34:9 ("as the LORD commanded Moses" — the census's receipts list; no footer, no header in the chapter), its disposition on file class NONE with the reason "Deuteronomy is not on the tape — the seat waits for its reading and compile": THE COMPILE'S MATTER (22b re-declares it — the book now read); THE PARSER — TWO NUMBERS COUNTED: 120 at 34:7 (31:2's number — the marker's verse counted the same) and 30 at 34:8 (Numbers 20:29's number for Aaron counted the same): a guard owed the compile (the years are the ink's own count on the marker's day, the thirty days a duration — the counter's matter)
_MP = open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'ch34_measure_lean.out'), encoding='utf-8').read()
assert re.search(r'^  imperatives: \[\] \| jussives / cohortatives \(the morph codes with j\): \[\] \| infinitive absolutes: \[\]$', _MP, re.M)
assert "the register on Deut 34 — receipts: [('Deut', 34, 9)] | footers: [] | headers: []" in _MP and "Deut 34:9: |     class: NONE |     why: Deuteronomy is not on the tape (the book not read) — the seat waits for its reading and compile" in _MP
assert "the parser's hits: {(34, 7): ([120], [], []), (34, 8): ([30], [], [])}" in _MP and '| 31:2 "a hundred and twenty years old this day": [120] | Numbers 20:29 "thirty days" for Aaron: [30]' in _MP
assert [(x, m) for x, m in wm('Deut', 34, 4)][:2] == [('ויאמר', 'HC/Vqw3ms'), ('יהוה', 'HNp')] and [(x, m) for x, m in wm('Deut', 34, 5)][0] == ('וימת', 'HC/Vqw3ms') and [(x, m) for x, m in wm('Deut', 34, 9)][3] == ('מלא', 'HAamsa') and [(x, m) for x, m in wm('Deut', 34, 9)][7] == ('סמך', 'HVqp3ms')
# THE PRIOR READS (the measure's F): the four spine rows over four ledgers, the two outside rows; the kin ledgers' Onkelos rows counted — 1:1-3:29's 29, 17-18's 22, 29-31's 30, the song's 52, the blessing's 29, Exodus 24's 10 and 33's 6, Numbers 11's 35, 12's 16, 20's 29, 27's 23, 33's 56, the erection docket's 1; the Genesis-era ledgers on the oath and the deaths by their lines (the coffin in Egypt's 29); EIGHTEEN LEDGERS NAME A VERSE OF THE CHAPTER — the pointers to be paid at the compile: 34:1 (Numbers 12, 22, 32 and its exam, 33, 34), 34:4 (Numbers 27, 32, 34), 34:5 (the exams of Numbers 19-21 and 33), 34:6 (chapter 11, Genesis 11, Numbers 6, 23, 24, 32), 34:7 (Numbers 21, 27, 33 and its exam), 34:8 (Genesis 73, Numbers 19, 20, 21, 33), 34:9 (Numbers 27); no ledger holds an Onkelos row of chapter 34 or of the Prophets; THE STORE = THE DB (no mismatch), 176 tokens, 120 distinct glosses, ONE "?" gloss (34:6's "house" of Beth-peor); the store's own words the display patch's candidates — "Daniel" for Dan the border (34:1), "from-desert" for the plains, "the-earth" for the land, "the-seas" and "the-hinder" for the western sea, "the-circle" for the plain, "split" for the valley, "the-palm-tree" for the palms
assert re.search(r"^  spine rows read before: 4 \[\(357, 27\), \(357, 28\), \(357, 40\), \(357, 44\)\] \| distinct rows 4 \| the ledgers: \['deu_05_vaetchanan_2026-09-16\.md', 'deu_09_ekev_2026-09-19\.md', 'deu_29_31_nitzavim_vayelech_2026-09-27\.md', 'deu_32_haazinu_2026-09-27\.md'\]$", _MP, re.M)
assert "outside rows read before: {(305, 5): ['deu_29_31_nitzavim_vayelech_2026-09-27.md'], (341, 1): ['deu_32_haazinu_2026-09-27.md']} | fresh: []" in _MP and 'ledgers with an Onkelos row of Deut 34 or the Prophets (never read ahead — expected none): []' in _MP
_KIN = dict(_ast.literal_eval(re.search(r"^  the kin ledgers' Onkelos row counts: (\[.*?\]) \| the Genesis-era", _MP, re.M).group(1)))
assert _KIN == {'deu_01_03_devarim_2026-09-15.md': 29, 'deu_17_18_shoftim_2026-09-24.md': 22, 'deu_29_31_nitzavim_vayelech_2026-09-27.md': 30, 'deu_32_haazinu_2026-09-27.md': 52, 'deu_33_ve_zot_2026-09-29.md': 29, 'erection_docket_2026-09-06.md': 1, 'exo_24_covenant_ascent_2026-09-01.md': 10, 'exo_33_presence_2026-09-01.md': 6, 'num_11_complaint_quail_2026-09-10.md': 35, 'num_12_miriam_2026-09-10.md': 16, 'num_20_meribah_edom_aaron_2026-09-11.md': 29, 'num_27_zelophehad_joshua_2026-09-09.md': 23, 'num_33_journeys_2026-09-12.md': 56}, _KIN
_PTR = _ast.literal_eval(re.search(r"^  the ledgers naming a verse of Deut 34 \(the pointers to be paid — the dump's F list\) and the verse each names: (\[.*\])$", _MP, re.M).group(1))
POINTERS = {}
for _f, _vs in _PTR:
    for _x in _vs: POINTERS.setdefault(int(_x.split(':')[1]), set()).add(_f)
POINTERS = {k: sorted(v) for k, v in sorted(POINTERS.items())}
assert len(_PTR) == 18 and sorted(POINTERS) == [1, 4, 5, 6, 7, 8, 9] and {k: len(v) for k, v in POINTERS.items()} == {1: 6, 4: 3, 5: 2, 6: 6, 7: 4, 8: 5, 9: 1}, {k: len(v) for k, v in POINTERS.items()}
assert STORE_MISMATCH == [] and sum(len(W(34, v)) for v in range(1, 13)) == 176 and len({g for (cc, v) in SG if cc == 34 for _, _, g in SG[(cc, v)]}) == 120 and [(cc, v, hp) for (cc, v) in SG for _, hp, g in SG[(cc, v)] if g == '?'] == [(34, 6, 'בית')]
assert [g for _, hp, g in SG[(34, 1)] if hp == 'דן'] == ['Daniel'] and [g for _, hp, g in SG[(34, 1)] if hp == 'מערבת'] == ['from-desert'] and [g for _, hp, g in SG[(34, 3)] if hp == 'הככר'] == ['the-circle'] and [g for _, hp, g in SG[(34, 3)] if hp == 'בקעת'] == ['split'] and [g for _, hp, g in SG[(34, 3)] if hp == 'התמרים'] == ['the-palm-tree'] and [g for _, hp, g in SG[(34, 2)] if hp in ('הים', 'האחרון')] == ['the-seas', 'the-hinder']

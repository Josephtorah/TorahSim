import os as _os
_ROOT = _os.path.normpath(_os.path.join(_os.path.dirname(_os.path.abspath(__file__)), '..', '..', '..'))   # THE PORTABLE REPO (2026-09-15): the repo root from this file's own place
#!/usr/bin/env python3
# THE DEUTERONOMY WALK, sitting 21 — CHAPTER 33, THE BLESSING, Deuteronomy 33:1-29 IN THE LEAN FORM (2026-09-29; the owner: "Reread and go" after the compaction that
# followed sitting 20b's push 472d2a3 — THE LEAN PASS's fifteenth sitting, its eighth reading; THE SPINE IN FORCE: fifteen piskaot 342-356 with 142 rows, 207 KB in the
# split's files — 355 on 33:20 the chapter's longest with thirty rows, 343 on 33:2 fifteen, 352 on 33:11 seventeen): THE INK of the chapter, computed from the Tanakh DB,
# the snapshot store and the shelf's own bytes — never typed. Sitting 20's form (ch32_ink.py): the generic helpers copied by derive_ch33_ink.py from the forms' ch22_ink.py
# by content markers (the chapter substituted; THE HEAD REGEX MADE COMMA-TOLERANT — 342's head "(Deuteronomy 33, 1)" is the export's one comma head, headless to sitting
# 20's instrument), the constants and every assert the chapter's own, typed FROM THE PRINTS (ch33_dump0.out, ch33_split.out, ch33_measure_lean.out). THE TWO DIVISIONS AGREE
# (29 = 29, cost 121) — the identity. ONE DRAFT on file: deu_33_ve_zot (33:1-29, twenty-nine steps one per verse) — one unit, CHAPTER NUMBERS. FIVE rows elsewhere cite the
# chapter, every one READ BEFORE (the split's print and the ledgers). THE PORTION EDGE: Vezot Habrachah is 33:1-34:12 — chapter 34 the next sitting; 357 on 34:1 its piska,
# cited by no row of this chapter. The parser MEASURED on every verse — ONE MARK: 33:23's "sated" (seva, the consonants of seven — the false six's and the false eight's
# precedent), no number counted anywhere in the chapter (the myriads of 33:2 and 33:17 are construct plurals the parser does not read). The hand's facts as asserts, run
# all at once by assert_driver.py.
import json, os, re, html, sqlite3, sys, io, contextlib, unicodedata, subprocess
from collections import Counter
ROOT = _ROOT
DATE = '2026-09-29'
CHS = (33,)
UIDS = ['deu_33_ve_zot']   # the draft's own id (the G print): one unit in the one chapter — the blessing 33:1-29
SPANS = {'deu_33_ve_zot': (33, 1, 29)}
PREFIX = {'deu_33_ve_zot': 'DV33'}
SPAN = [(33, v) for v in range(1, 30)]
PISKAOT = list(range(342, 357))   # THE SPINE ON CHAPTER 33: fifteen piskaot, every head present with the comma tolerated (the A prints and the split's); 341 on 32:52 before, 357 on 34:1 after
PISKAOT_BY = {33: PISKAOT}
HEADLESS = []   # none inside the chapter (the dump's heads table: 342-356 every head a chapter-33 citation — 342's with a comma)
SPINE_ROWS = {342: 7, 343: 15, 344: 7, 345: 3, 346: 2, 347: 5, 348: 9, 349: 5, 350: 3, 351: 4, 352: 17, 353: 13, 354: 8, 355: 30, 356: 14}   # rows per piska, both files (the heads table and the split's print) — 142
PREV_CHAPTER_ROWS = []   # no tail folded in (341's one row carries no word of 33:1 — the split's print; 341:1 reads 32:52 against 34:4; 342:1 opens with 33:1's citation and the hard words of 32:24-25)
READ_ROWS = [(p, r) for p in PISKAOT for r in range(1, SPINE_ROWS[p] + 1)]   # 142 — this ledger's spine rows, read WHOLE over the row runs by the split's byte plan
EXP2DB = {33: {e: [e] for e in range(1, 30)}}   # the identity (the offset 0 at every export verse — A0's print)
DB2EXP = {c: {d: e for e, ds in EXP2DB[c].items() for d in ds} for c in CHS}
OUTSIDE = [(31, 6), (42, 9), (48, 9), (314, 1), (329, 3)]   # the FIVE rows READ WHOLE: the union of the two files beyond piskaot 342-356 (the dump's and the split's print) — every one read before
EXCLUDED = []   # none known at the design — a translator's misprint is judged by the Hebrew at the whole read (sitting 18's lesson 4)
INTERPOLATION = []
CREDITED = {}   # under THE WHOLE-ROW RULE no spine row is credited: rows read before (the dump lists ten ledgers' seats among 342-356) are REREAD WHOLE here and marked so
TITLE = "Chapter 33 — the blessing: and this is the blessing with which Moses the man of God blessed the children of Israel before his death — the LORD came from Sinai, rose from Seir, shone from Mount Paran with myriads of holy ones, a fiery law at His right hand; He loves the peoples, all His holy ones are in Your hand; Moses commanded us a law, the inheritance of the congregation of Jacob; there was a king in Jeshurun when the heads of the people gathered, the tribes of Israel together. Let Reuben live and not die, though his men be few; hear, LORD, the voice of Judah, bring him to his people; of Levi — Your Thummim and Your Urim with Your godly one whom You tried at Massah and strove with at the waters of Meribah, who said of his father and mother I have not seen him, who kept Your word and guarded Your covenant — they shall teach Jacob Your ordinances, put incense before You and whole burnt offering on Your altar; bless, LORD, his substance, smite the loins of them that rise against him. Benjamin the beloved of the LORD dwells in safety, He covers him all the day and dwells between his shoulders. Joseph — blessed of the LORD is his land, the precious things of heaven, the dew and the deep that couches beneath, the sun and the moons, the ancient mountains and the everlasting hills, the earth and its fullness and the good will of Him that dwelt in the bush, on the head of Joseph and the crown of him that was separate from his brethren; his firstling bullock, the horns of the wild ox, the ten thousands of Ephraim and the thousands of Manasseh. Rejoice, Zebulun, in your going out, and Issachar in your tents — they call peoples to the mountain, offer sacrifices of righteousness, suck the abundance of the seas and the hidden treasures of the sand. Blessed be He that enlarges Gad — he dwells as a lioness, tears the arm and the crown of the head; he chose a first part for himself, the lawgiver's portion, he came with the heads of the people and executed the righteousness of the LORD. Dan a lion's whelp that leaps from Bashan; Naphtali satisfied with favor, full of the blessing of the LORD, possess the sea and the south; Asher blessed above sons, acceptable to his brethren, dipping his foot in oil, iron and brass your bars, as your days your strength. There is none like the God of Jeshurun who rides upon the heaven for your help; the eternal God is a dwelling place and underneath are the everlasting arms, He thrust out the enemy and said destroy; Israel dwells in safety, the fountain of Jacob alone in a land of corn and wine, his heavens drop down dew. Happy are you, O Israel, who is like you, a people saved by the LORD, the shield of your help and the sword of your excellency; your enemies shall dwindle before you and you shall tread upon their high places."
OUT = f'{ROOT}/logic/oral_triage/deu_33_ve_zot_{DATE}.md'
PATCHED = bool(os.environ.get('DEU33_PATCHED'))   # the tail's flag: after the manifest and the seat, the draft carries operators and the store its overrides
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
def W33(v): return words('Deut', 33, v)
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
for c, v, idx, hp, g in store.execute("SELECT v.chapter, v.verse, w.idx, w.he_plain, w.gloss FROM words w JOIN verses v ON w.verse_id=v.id WHERE v.book='Deut' AND v.chapter IN (33) ORDER BY v.id, w.idx"):
    SG.setdefault((c, v), []).append((idx, hp.replace('/', ''), g))
def sg(c, v, tok, nth=0):
    hit = [g for _, hp, g in SG[(c, v)] if hp == tok]
    if len(hit) <= nth: raise KeyError((c, v, tok, nth))
    return hit[nth]
def sidx(c, v, tok, nth=0):
    hit = [i for i, hp, _ in SG[(c, v)] if hp == tok]
    assert len(hit) > nth, (c, v, tok, nth, hit)
    return hit[nth]
STORE_MISMATCH = [(c, v, n, len(by[('Deut', c, v)])) for c, v, n in store.execute("SELECT v.chapter, v.verse, COUNT(*) FROM words w JOIN verses v ON w.verse_id=v.id WHERE v.book='Deut' AND v.chapter IN (33) GROUP BY v.chapter, v.verse").fetchall() if n != len(by[('Deut', c, v)])]
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
# THE SHELF BY POSITION — THE SPINE IN FORCE on chapter 33: fifteen heads 342-356 (the dump's window 335-357, the export's end); 341 on 32:52 before, 357 on 34:1 after; the heads by chapter as sitting 20's table printed them but for (33, 15) — 342's comma head now read (sitting 20's instrument: (33, 14), 342 headless)
assert NV == {33: 29} and VC[32] == 52 and VC[34] == 12 and len(sif) == 357 and len(sif_he) == 357 and sum(len(s) for s in sif) == 2357 and sum(len(s) for s in sif_he) == 2357
HC = Counter(h[0] for h in heads.values() if h)
assert (HC[31], HC[32], HC[33], HC[34]) == (1, 36, 15, 1) and sorted(HC.items()) == [(1, 24), (3, 4), (6, 6), (11, 21), (12, 20), (13, 14), (14, 14), (15, 16), (16, 19), (17, 16), (18, 16), (19, 10), (20, 14), (21, 17), (22, 22), (23, 22), (24, 16), (25, 10), (26, 4), (31, 1), (32, 36), (33, 15), (34, 1)], sorted(HC.items())
WIN = {335: (32, 46), 336: (32, 47), 337: (32, 48), 338: (32, 49), 339: (32, 50), 340: (32, 51), 341: (32, 52), 342: (33, 1), 343: (33, 2), 344: (33, 3), 345: (33, 4), 346: (33, 5), 347: (33, 6), 348: (33, 7), 349: (33, 8), 350: (33, 9), 351: (33, 10), 352: (33, 11), 353: (33, 13), 354: (33, 18), 355: (33, 20), 356: (33, 27), 357: (34, 1)}
assert {p: heads[p] for p in range(335, 358)} == WIN, {p: heads[p] for p in range(335, 358) if heads[p] != WIN[p]}
assert heads[342] == (33, 1) and HB0(342, 1).startswith('(דברים לג, א) וזאת הברכה אשר ברך משה') and 'And this is the blessing' in clean(sif[341][0]), (heads[342], HB0(342, 1)[:60])   # THE COMMA HEAD: 342's marker "(Deuteronomy 33, 1) and this is the blessing which Moses blessed" carries a comma between the chapter and the verse — the export's one; sitting 20's strict regex read it as headless
HV = {c: [heads[p][1] for p in PISKAOT_BY[c] if heads[p]] for c in CHS}
assert HV == {33: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 13, 18, 20, 27]}, HV
NOHEAD = {c: [v for v in range(1, NV[c] + 1) if v not in HV[c]] for c in CHS}
assert NOHEAD == {33: [12, 14, 15, 16, 17, 19, 21, 22, 23, 24, 25, 26, 28, 29]}, NOHEAD   # fourteen verses without a head of their own — 12 inside 352 (Benjamin in the piska of Levi's blessing), 14-17 inside 353 (Joseph), 19 inside 354 (Zebulun and Issachar), 21-26 inside 355 (Gad's piska carries Dan, Naphtali, Asher and the rider of the heavens), 28-29 inside 356
assert {p: (len(sif_he[p - 1]), len(sif[p - 1])) for p in PISKAOT} == {p: (n, n) for p, n in SPINE_ROWS.items()} and sum(SPINE_ROWS.values()) == 142 and len(READ_ROWS) == 142 and len(PISKAOT) == 15 and READ_ROWS[0] == (342, 1) and READ_ROWS[-1] == (356, 14) and SPINE_ROWS[355] == 30 and max(SPINE_ROWS.values()) == 30
# THE TAILS AND THE EDGES (the split's print): 341's one row carries no word of 33:1 ("and this is the blessing"); 342:1 opens with 33:1's citation and the hard words of 32:24-25; 356:14 ends on Joshua 10:24's necks ("and you shall tread on their high places"); 357:1 opens with 34:1's ascent; 357's rows carry no "happy are you, O Israel"
assert not any('וזאת הברכה' in HB0(341, r) for r in range(1, 2)) and HB0(341, 1).startswith('(דברים לב נב) כי מנגד תראה את הארץ') and HB0(342, 1).startswith('(דברים לג, א) וזאת הברכה אשר ברך משה, לפי שאמר משה לישראל דברים קשים תחלה (דברים לב כד-כה)') and HB0(356, 14).startswith('ואתה על במותימו תדרוך') and '(יהושע י כד)' in HB0(356, 14) and HB0(357, 1).startswith('(דברים לד א) ויעל משה מערבת מואב') and not any('אשריך ישראל' in HB0(357, r) for r in range(1, 45))
assert all(clean(sif[p - 1][0]).startswith('Pisqa’ %d' % p) for p in PISKAOT) and 'And this is the blessing' in clean(sif[341][0]) and 'The Primordial God is a refuge' in clean(sif[355][0]) and 'And Moses ascended' in clean(sif[356][0])   # the English rows open with the translator's apparatus before the text (sitting 19's lesson)
# THE CITATIONS PARSED FROM THE DUMP'S PRINT (the instrument's own lists read back): the row-citations per file, the union, the outside set; the divisions; the store
import ast as _ast
_t = open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'ch33_dump0.out'), encoding='utf-8').read()
_HE = _ast.literal_eval(re.search(r'^  HE rows citing Deut 33[^:]*: \d+ (\[.*\])$', _t, re.M).group(1)); _EN = _ast.literal_eval(re.search(r'^  EN rows citing Deut 33[^:]*: \d+ (\[.*\])$', _t, re.M).group(1))
_un = int(re.search(r'^  the union of rows \(both files\): (\d+) \[', _t, re.M).group(1)); _out = _ast.literal_eval(re.search(r'^  the rows OUTSIDE the spine piskaot [^:]*: \d+ (\[.*?\]) \|', _t, re.M).group(1)); _insp = int(re.search(r'\| in-spine rows of the union: (\d+)$', _t, re.M).group(1))
_two = re.search(r'^  DB verses (\d+) \| export verses HE (\d+) EN (\d+) \| per-chapter export lengths vs DB, chapters 1-33: (\[.*\])$', _t, re.M); _cost = int(re.search(r'^  the alignment cost (\d+) \|', _t, re.M).group(1))
_mis = _ast.literal_eval(re.search(r'verses whose store token count differs from the DB: (\[.*?\])$', _t, re.M).group(1)); _tok = int(re.search(r'^  token count chapter 33 : (\d+)$', _t, re.M).group(1))
assert (len(_HE), len(_EN), _un, _insp) == (34, 203, 128, 123) and _out == OUTSIDE and len(_out) == 5, (len(_HE), len(_EN), _un, _insp, _out)
assert tuple(int(x) for x in _two.groups()[:3]) == (29, 29, 29) and _two.group(4) == '[(5, 30, 33)]' and _cost == 121, 'THE TWO DIVISIONS: the identity; chapter 5 the book\'s one split'
assert _mis == [(33, 2, 18, 16), (33, 9, 19, 18)] and _tok == 336, (_mis, _tok)   # THE STORE = THE DB except at 33:2 (the store two tokens more — the fiery law's ketiv one word, the qere two) and 33:9 (one more)
# THE OUTSIDE ROWS' FACTS COMPUTED from the dump's lists: the verses each row cites (the DB's numbering), the heads of their piskaot, the prior reads from the ledgers, the fresh rows
CITED = {}
for _p, _r, _e, _dbv in _HE + _EN:
    if (_p, _r) in OUTSIDE:
        for _d in _dbv: CITED.setdefault((_p, _r), set()).add((33, _d))
CITED = {k: sorted(v) for k, v in sorted(CITED.items())}
assert sorted(CITED) == OUTSIDE, (sorted(set(OUTSIDE) - set(CITED)), sorted(set(CITED) - set(OUTSIDE)))
assert CITED == {(31, 6): [(33, 6)], (42, 9): [(33, 25)], (48, 9): [(33, 4)], (314, 1): [(33, 2)], (329, 3): [(33, 6)]}, CITED   # Reuben's repentance (31:6 on 33:6), the lands' surplus (42:9 on 33:25), all equal in the Torah (48:9 on 33:4), the eagle and the four winds (314:1 on 33:2), death and life in one (329:3 on 33:6)
HEADS_ON = {p: heads[p] for p in sorted({p for p, _ in OUTSIDE})}
assert HEADS_ON == {31: (6, 4), 42: (11, 14), 48: (11, 22), 314: (32, 11), 329: (32, 39)}, HEADS_ON
_TRI = f'{ROOT}/logic/oral_triage'
LED = {f: open(f'{_TRI}/{f}', encoding='utf-8').read() for f in os.listdir(_TRI) if f.endswith('.md') and os.path.isfile(f'{_TRI}/{f}') and f != os.path.basename(OUT)}
SPINE_PRIOR = sorted({(f, int(a), int(b)) for f, t in LED.items() for a, b in re.findall(r'Sifrei Devarim (\d+):(\d+)', t) if int(a) in PISKAOT})
PRIOR_READ = {}
for f, t in LED.items():
    for a, b in re.findall(r'Sifrei Devarim (\d+):(\d+)', t):
        if (int(a), int(b)) in OUTSIDE: PRIOR_READ.setdefault((int(a), int(b)), []).append(f)
PRIOR_READ = {k: sorted(set(v)) for k, v in sorted(PRIOR_READ.items())}
FRESH = [k for k in OUTSIDE if k not in PRIOR_READ]
assert ('deu_09_ekev_2026-09-19.md', 342, 1) in SPINE_PRIOR and ('deu_32_haazinu_2026-09-27.md', 346, 2) in SPINE_PRIOR and ('gen_22_covenant_bow_2026-08-25.md', 343, 9) in SPINE_PRIOR and len(SPINE_PRIOR) >= 12, len(SPINE_PRIOR)   # spine rows READ BEFORE at earlier chapters (the dump's list) — REREAD WHOLE here under the whole-row rule and marked so
assert sorted(PRIOR_READ) == OUTSIDE and FRESH == [], (sorted(PRIOR_READ), FRESH)   # EVERY OUTSIDE ROW READ BEFORE — 31:6 at chapter 6, 42:9 and 48:9 at chapter 11 (48:9 again at 29-31), 314:1 and 329:3 at the song: none fresh
# THE FRAMES AND THE NAMES (the dump's D section): no 'saying' in the chapter; the one narrative frame 33:2 'and he said' with the Name its object (Moses speaking); Jeshurun at 33:5 (with the prefix) and 33:26; eleven tribes named, Simeon absent; 'for' (ki) at 33:9, 33:19, 33:21; no 'if', no 'lest'
assert [(c, v) for c, v in SPAN if 'לאמר' in W(c, v)] == [] and 'בישרון' in W(33, 5) and 'ישרון' in W(33, 26) and 'משה' in W(33, 1) and 'האלהים' in W(33, 1) and 'מותו' in W(33, 1)   # no "saying"; "in Jeshurun" 33:5; "Jeshurun" 33:26; "Moses", "God", "his death" at 33:1
assert 'ראובן' in W(33, 6) and 'יהודה' in W(33, 7) and 'וללוי' in W(33, 8) and 'לבנימן' in W(33, 12) and 'וליוסף' in W(33, 13) and 'אפרים' in W(33, 17) and 'מנשה' in W(33, 17) and 'ולזבולן' in W(33, 18) and 'ויששכר' in W(33, 18) and 'ולגד' in W(33, 20) and 'ולדן' in W(33, 22) and 'ולנפתלי' in W(33, 23) and 'ולאשר' in W(33, 24)   # Reuben, Judah, and-to-Levi, to-Benjamin, and-to-Joseph, Ephraim, Manasseh, and-to-Zebulun, and-Issachar, and-to-Gad, and-to-Dan, and-to-Naphtali, and-to-Asher
assert [(c, v) for c, v in SPAN if 'כי' in W(c, v)] == [(33, 9), (33, 19), (33, 21)] and [(c, v) for c, v in SPAN if 'אם' in W(c, v) or 'ואם' in W(c, v) or 'פן' in W(c, v)] == [] and not any('שמעון' in W(c, v) for c, v in SPAN)   # "for" thrice; no "if", no "lest"; Simeon named nowhere in the chapter
# ---- THE ASSERTS TYPED FROM THE MEASURE'S PRINT (block b: ch33_measure_lean.out — the kin, the twins, the formulas, Onkelos, the frames, the register, the parser, the prior reads) ----
# THE KIN BY COMPUTATION: the frame's kin 4:44 ("and this is the law which Moses set before the children of Israel" — five in order with 33:1's "and this is the blessing"); JOSEPH'S BLESSING IS JACOB'S — 33:16 five in order with Genesis 49:26 (the head of Joseph, the crown of him separate from his brethren), 33:13 with Genesis 49:25 (the deep that couches beneath); 33:15 with Habakkuk 3:6 (the everlasting hills — the Prophets' seat cited, never read); 33:22's lion's whelp Judah's (Genesis 49:9); two verses share no two tokens with any verse (33:11 the loins smitten, 33:14 the sun and the moons)
assert [v for c, v in SPAN if not KINC[(c, v)]] == [11, 14], [v for c, v in SPAN if not KINC[(c, v)]]
assert KINC[(33, 1)][0] == ('Deut 4:44', 5, 5) and KINC[(33, 16)][0] == ('Gen 49:26', 5, 5) and KINC[(33, 13)][0] == ('Gen 49:25', 3, 3) and KINC[(33, 15)][0] == ('Hab 3:6', 3, 3) and KINC[(33, 22)][0] == ('Gen 49:9', 2, 2) and KINC[(33, 5)][0] == ('Ezra 4:3', 4, 1) and KINC[(33, 21)][0] == ('1Chr 11:10', 3, 4) and KINC[(33, 28)][0] == ('2Kgs 18:32', 3, 4) and KINC[(33, 29)][0] == ('1Kgs 1:20', 3, 3) and KINC[(33, 4)][0] == ('Josh 17:4', 3, 2), (KINC[(33, 1)][0], KINC[(33, 16)][0], KINC[(33, 13)][0])
assert KINC[(33, 3)] == [('Deut 33:17', 2, 2), ('Ps 96:10', 2, 2)] and KINC[(33, 12)][0] == ('Deut 33:20', 2, 2) and KINC[(33, 18)] == [('Esth 5:14', 2, 2)] and KINC[(33, 2)][0] == ('1Chr 11:2', 2, 3), (KINC[(33, 3)], KINC[(33, 12)][0], KINC[(33, 18)])
# THE TWINS DIFFED (shared / the longest run): Joseph's crown 33:16 five in order with Genesis 49:26; the deep 33:13 with Genesis 49:25; the everlasting hills 33:15 with Habakkuk 3:6; Mount Paran 33:2 with Habakkuk 3:3; "Moses the man of God" 33:1 with Joshua 14:6 (the Prophets' seat cited, never read); the waters of Meribah 33:8 with Numbers 20:13; Levi's father and mother 33:9 with the high priest's (Leviticus 21:11); THE TWINS BY SENSE WITH NO SHARED TOKEN — Jeshurun 33:5 (prefixed) with 32:15, the dew 33:28 with 32:2, Benjamin 33:12 with Genesis 49:27, Reuben 33:6 with Genesis 49:4, Asher 33:24 with Genesis 49:20, the lawgiver's portion 33:21 with Numbers 32:33 and 34:6
assert SHARED(('Deut', 33, 16), ('Gen', 49, 26)) == ['לראש', 'יוסף', 'ולקדקד', 'נזיר', 'אחיו'] and SHN(('Deut', 33, 16), ('Gen', 49, 26)) == 5 and SHARED(('Deut', 33, 13), ('Gen', 49, 25)) == ['רבצת', 'תחת'] and SHN(('Deut', 33, 13), ('Gen', 49, 25)) == 3 and SHARED(('Deut', 33, 15), ('Hab', 3, 6)) == ['גבעות', 'עולם'] and SHN(('Deut', 33, 15), ('Hab', 3, 6)) == 3 and SHARED(('Deut', 33, 2), ('Hab', 3, 3)) == ['מהר', 'פארן']   # on the head of Joseph, the crown of him separate from his brethren; couches beneath; the everlasting hills; from Mount Paran
assert SHARED(('Deut', 33, 1), ('Josh', 14, 6)) == ['משה', 'איש', 'האלהים'] and SHN(('Deut', 33, 1), ('Josh', 14, 6)) == 4 and SHARED(('Deut', 33, 1), ('Gen', 49, 28)) == ['וזאת'] and SHN(('Deut', 33, 1), ('Gen', 49, 28)) == 3 and SHARED(('Deut', 33, 1), ('Deut', 4, 44)) == SHARED(('Deut', 33, 1), ('Deut', 4, 44)) and SHARED(('Deut', 33, 8), ('Num', 20, 13)) == ['מי', 'מריבה'] and SHARED(('Deut', 33, 8), ('Deut', 6, 16)) == ['במסה'] and SHARED(('Deut', 33, 9), ('Lev', 21, 11)) == ['לאביו', 'ולאמו', 'לא'] and SHN(('Deut', 33, 9), ('Lev', 21, 11)) == 3   # Moses the man of God; and this; the waters of Meribah; at Massah; to his father and to his mother not
assert SHARED(('Deut', 33, 22), ('Gen', 49, 9)) == ['גור', 'אריה'] and SHARED(('Deut', 33, 19), ('Ps', 4, 6)) == ['זבחי', 'צדק'] and SHARED(('Deut', 33, 17), ('Gen', 48, 20)) == ['אפרים'] and SHN(('Deut', 33, 17), ('Gen', 48, 20)) == 2 and SHARED(('Deut', 33, 29), ('Gen', 15, 1)) == ['מגן'] and SHN(('Deut', 33, 29), ('Gen', 15, 1)) == 2 and SHARED(('Deut', 33, 26), ('Deut', 32, 15)) == ['ישרון'] and SHARED(('Deut', 33, 28), ('Gen', 27, 28)) == ['דגן']   # a lion's whelp; sacrifices of righteousness; Ephraim; a shield; Jeshurun; corn
assert SHARED(('Deut', 33, 6), ('Gen', 49, 3)) == ['ראובן'] and SHARED(('Deut', 33, 7), ('Gen', 49, 8)) == ['יהודה'] and SHARED(('Deut', 33, 18), ('Gen', 49, 13)) == ['זבולן'] and SHARED(('Deut', 33, 20), ('Gen', 49, 19)) == ['גד'] and SHARED(('Deut', 33, 22), ('Gen', 49, 17)) == ['דן'] and SHARED(('Deut', 33, 23), ('Gen', 49, 21)) == ['נפתלי']   # Jacob's blessing shares each tribe's NAME alone — Reuben, Judah, Zebulun, Gad, Dan, Naphtali
assert SHN(('Deut', 33, 5), ('Deut', 32, 15)) == 0 and SHN(('Deut', 33, 28), ('Deut', 32, 2)) == 0 and SHN(('Deut', 33, 12), ('Gen', 49, 27)) == 0 and SHN(('Deut', 33, 6), ('Gen', 49, 4)) == 0 and SHN(('Deut', 33, 24), ('Gen', 49, 20)) == 0 and SHN(('Deut', 33, 21), ('Num', 32, 33)) == 0 and SHN(('Deut', 33, 21), ('Deut', 34, 6)) == 0 and SHN(('Deut', 33, 29), ('Deut', 32, 13)) == 1 and SHN(('Deut', 33, 17), ('Gen', 48, 19)) == 0 and SHN(('Deut', 33, 27), ('Ps', 90, 1)) == 0
# THE FORMULAS (phrase seats by consonants over the Torah and the Bible): THIRTY-EIGHT phrases of the blessing ONCE in the Bible (computed over the measure's list, the count read from its print); THE FIERY LAW'S KETIV IS ASHDOTH'S WORD (eshdat — the slopes of Pisgah at 3:17 and 4:49; the qere's two words nowhere); Jeshurun 32:15 and 33:26 (33:5 prefixed); "before his death" Isaac's and Jacob's (Genesis 27:10, 50:16); Massah 6:16; the waters of Meribah Numbers 20:13 (and two psalms); "separate from his brethren" Genesis 49:26 alone; "a lion's whelp" Judah's (Genesis 49:9); "as a lioness" Balaam's (Numbers 23:24); "the heads of the people" 33:5 and 33:21; "destroy" 4:26's word; Isaac's "corn and wine" defective, 33:28's full; THE CHAPTER NEVER SAYS "THE LORD YOUR GOD" (192 seats in the Torah, none here — as the song)
Q33 = [('וזאת', 'הברכה'), ('מסיני', 'בא'), ('מרבבת', 'קדש'), ('חבב', 'עמים'), ('קדשיו', 'בידך'), ('תורה', 'צוה', 'לנו', 'משה'), ('מורשה', 'קהלת', 'יעקב'), ('בישרון', 'מלך'), ('יחד', 'שבטי', 'ישראל'), ('יחי', 'ראובן', 'ואל', 'ימת'), ('תמיך', 'ואוריך'), ('שמרו', 'אמרתך'), ('יורו', 'משפטיך', 'ליעקב'), ('קטורה', 'באפך'), ('ידיד', 'יהוה'), ('ומתהום', 'רבצת', 'תחת'), ('הררי', 'קדם'), ('שכני', 'סנה'), ('רבבות', 'אפרים'), ('אלפי', 'מנשה'), ('שפע', 'ימים'), ('חלקת', 'מחקק'), ('צדקת', 'יהוה'), ('שבע', 'רצון'), ('ים', 'ודרום'), ('וטבל', 'בשמן', 'רגלו'), ('וכימיך',), ('אין', 'כאל', 'ישרון'), ('רכב', 'שמים'), ('אלהי', 'קדם'), ('זרעת', 'עולם'), ('עין', 'יעקב'), ('יערפו', 'טל'), ('אשריך', 'ישראל'), ('מי', 'כמוך'), ('עם', 'נושע', 'ביהוה'), ('מגן', 'עזרך'), ('חרב', 'גאותך'), ('על', 'במותימו', 'תדרך')]   # the measure's list (the names in its print): and this is the blessing … tread upon their high places — thirty-nine phrases, thirty-eight once in the Bible ("who is like you" four times)
ONCE = [seq for seq in Q33 if len(P(*seq, books=None)) == 1 and P(*seq, books=None)[0].startswith('Deut 33:')]
assert len(Q33) == 39 and len(ONCE) == 38 and [seq for seq in Q33 if seq not in ONCE] == [('מי', 'כמוך')] and P('מי', 'כמוך', books=None) == ['Deut 33:29', 'Ps 35:10', 'Ps 71:19', 'Ps 89:9'], (len(ONCE), [seq for seq in Q33 if seq not in ONCE])   # "who is like you" the one phrase of the list with psalm seats beside
assert P('אשדת', books=None) == ['Deut 33:2', 'Deut 3:17', 'Deut 4:49'] and P('אש', 'דת', books=None) == [] and 'אשדת' in W(33, 2) and P('ישרון', books=None) == ['Deut 32:15', 'Deut 33:26'] and P('לפני', 'מותו', books=T) == ['Deut 33:1', 'Gen 27:10', 'Gen 50:16'] and P('במסה', books=None) == ['Deut 33:8', 'Deut 6:16'] and P('מי', 'מריבה', books=T) == ['Deut 33:8', 'Num 20:13'] and len(P('מי', 'מריבה', books=None)) == 4   # the fiery law's ketiv = Ashdoth; Jeshurun; before his death; at Massah; the waters of Meribah
assert P('נזיר', 'אחיו', books=None) == ['Deut 33:16', 'Gen 49:26'] and P('גור', 'אריה', books=T) == ['Deut 33:22', 'Gen 49:9'] and len(P('גור', 'אריה', books=None)) == 3 and P('כלביא', books=T) == ['Deut 33:20', 'Num 23:24'] and P('ראשי', 'עם', books=T) == ['Deut 33:21', 'Deut 33:5'] and P('השמד', books=T) == ['Deut 33:27', 'Deut 4:26'] and P('דגן', 'ותירש', books=None) == ['Gen 27:28'] and 'ותירוש' in W(33, 28) and P('גבעות', 'עולם', books=None) == ['Deut 33:15', 'Hab 3:6'] and P('מהר', 'פארן', books=None) == ['Deut 33:2', 'Hab 3:3']   # separate from his brethren; a lion's whelp; as a lioness; the heads of the people; destroy; corn and wine; the everlasting hills; from Mount Paran
assert P('איש', 'האלהים', books=T) == ['Deut 33:1'] and len(P('איש', 'האלהים', books=None)) == 60 and len(P('הבשן', books=T)) == 12 and len(P('יהוה', 'אלהיך', books=T)) == 192 and len(P('יהוה', 'אלהיך', books=None)) == 236 and P('ישכן', 'לבטח', books=None) == ['Deut 33:12', 'Jer 23:6', 'Ps 16:9'] and P('זבחי', 'צדק', books=None) == ['Deut 33:19', 'Ps 4:6', 'Ps 51:21'] and P('ברזל', 'ונחשת', books=None) == ['2Chr 24:12', 'Deut 33:25'] and len(P('טל', books=None)) == 13 and P('טל', books=T) == ['Deut 33:28']   # the man of God (sixty in the Bible, once in the Torah); Bashan; the LORD your God; dwell in safety; sacrifices of righteousness; iron and brass; the dew bare once in the Torah
# THE WORDS: the Name SEVEN times bare (33:2, 7, 11, 12, 13, 21, 23) and once with bet (33:29 "saved by the LORD") — never "the LORD your God"; God at 33:1 (the man of God), 33:26 (none like God), 33:27 (the eternal God) — 33:28's "el" the preposition "unto"; eleven tribes named, Simeon absent, and THE PRECIOUS THINGS OF JOSEPH CARRY GAD'S LETTERS (meged at 33:13-16 — five false hits of the tribe scan, a homograph for the compile); the negation "not" thrice at 33:9 alone, the vetitive "let him not" at 33:6; "for" thrice; no "if", "lest" or "saying"; "he said" eleven — nine tribal frames, 33:2's theophany and 33:27's "destroy"
assert [(v, x) for c, v in SPAN for x in W(c, v) if x in ('יהוה', 'ליהוה', 'ביהוה', 'ויהוה')] == [(2, 'יהוה'), (7, 'יהוה'), (11, 'יהוה'), (12, 'יהוה'), (13, 'יהוה'), (21, 'יהוה'), (23, 'יהוה'), (29, 'ביהוה')] and [(v, x) for c, v in SPAN for x in W(c, v) if x in ('אל', 'כאל', 'אלוה', 'אלהים', 'האלהים', 'אלהי', 'אלהיו', 'אלהיהם', 'אלהיך')] == [(1, 'האלהים'), (26, 'כאל'), (27, 'אלהי'), (28, 'אל')]   # the Name; God — 33:28's "el" is "unto a land"
assert [(v, x) for c, v in SPAN for x in W(c, v) if any(x.endswith(n) for n in ('ראובן', 'יהודה', 'לוי', 'בנימן', 'יוסף', 'אפרים', 'מנשה', 'זבולן', 'יששכר', 'גד', 'דן', 'נפתלי', 'אשר', 'שמעון')) and x not in ('ואשר', 'אשר', 'כאשר', 'מגד')] == [(6, 'ראובן'), (7, 'ליהודה'), (7, 'יהודה'), (8, 'וללוי'), (12, 'לבנימן'), (13, 'וליוסף'), (13, 'ממגד'), (14, 'וממגד'), (14, 'וממגד'), (15, 'וממגד'), (16, 'וממגד'), (16, 'יוסף'), (17, 'אפרים'), (17, 'מנשה'), (18, 'ולזבולן'), (18, 'זבולן'), (18, 'ויששכר'), (20, 'ולגד'), (20, 'גד'), (22, 'ולדן'), (22, 'דן'), (23, 'ולנפתלי'), (23, 'נפתלי'), (24, 'ולאשר')]   # the tribe scan with its five false hits — "from the precious things" (meged) ends in Gad's letters
assert sum(1 for c, v in SPAN for x in W(c, v) if x in ('לא', 'ולא')) == 3 and [(c, v) for c, v in SPAN if any(x in ('לא', 'ולא') for x in W(c, v))] == [(33, 9)] and [(v, x) for c, v in SPAN for x in W(c, v) if x in ('אל', 'ואל')] == [(6, 'ואל'), (7, 'ואל'), (28, 'אל')] and sum(1 for c, v in SPAN for x in W(c, v) if x == 'כי') == 3   # not (lo) thrice at 33:9; al at 33:6 the vetitive, at 33:7 and 33:28 the preposition "unto"; for (ki) thrice
assert [(v, x) for c, v in SPAN for x in W(c, v) if x in ('אמר', 'ויאמר')] == [(2, 'ויאמר'), (7, 'ויאמר'), (8, 'אמר'), (12, 'אמר'), (13, 'אמר'), (18, 'אמר'), (20, 'אמר'), (22, 'אמר'), (23, 'אמר'), (24, 'אמר'), (27, 'ויאמר')]   # "he said" eleven: Judah, Levi, Benjamin, Joseph, Zebulun, Gad, Dan, Naphtali, Asher framed; Reuben unframed after the prologue; Issachar inside Zebulun's; 33:2 the theophany; 33:27 "destroy"
assert (len(W(33, 1)), len(W(33, 2)), len(W(33, 4)), len(W(33, 25)), len(W(33, 29))) == (12, 16, 7, 5, 19) and W(33, 4) == ['תורה', 'צוה', 'לנו', 'משה', 'מורשה', 'קהלת', 'יעקב'] and W(33, 25) == ['ברזל', 'ונחשת', 'מנעליך', 'וכימיך', 'דבאך'] and W(33, 6) == ['יחי', 'ראובן', 'ואל', 'ימת', 'ויהי', 'מתיו', 'מספר']   # a law Moses commanded us, an inheritance of the congregation of Jacob; iron and brass your bars, as your days your strength; let Reuben live and not die, and let his men be a number
# ONKELOS WRITING THE MEANING (the export's rows through NFKC): the man of God "the prophet of the LORD" (33:1); Sinai doubled sixteen to twenty-three with the Torah given "from the midst of fire" (33:2); the peoples "the tribes", led "under Your cloud by Your Memra" (33:3); Jeshurun ISRAEL again (33:5, 33:26 — 32:15's rule); REUBEN'S ETERNAL LIFE AND THE SECOND DEATH (33:6 — the world, alma, its fourth seat); Judah's prayer in war (33:7); the Urim "clothed" and Levi "found faithful" at the waters of strife (33:8 — Meribah's matzuta as 32:51); Levi "had no mercy on his father and mother when they sinned" and kept "the watch of Your Memra" (33:9); the incense of spices (33:10); "the offering of his hands" — korban's one seat in the book (33:11); BENJAMIN: "in his land the Shekhinah shall dwell" (33:12); the moons "month by month" (33:14); the everlasting hills "hills that cease not" (33:15); the bush "revealed to Moses" with a variant marked in the export's own row (33:16); Ephraim's myriads and Manasseh's thousands "of the house of" (33:17); ZEBULUN TO WAR, ISSACHAR TO THE FESTIVALS IN JERUSALEM (33:18); the mountain "the sanctuary house" and the peoples' wealth (33:19); Gad slays "rulers with kings" (33:20); THE LAWGIVER'S PORTION IS MOSES' GRAVE — "Moses the great scribe of Israel is buried" (33:21 — 34:6 read into the blessing, the death not yet on the tape); Dan drinks from the rivers of Matnan (33:22 — Bashan's name in Onkelos); Naphtali's sea Gennesar (33:23); Asher "the delicacies of kings" (33:24); "strong as iron" (33:25); "none like the God of Israel whose Shekhinah is in heaven" (33:26); THE EVERLASTING ARMS "by His Memra the world was made" (33:27); the fountain of Jacob "the blessing Jacob their father blessed them" (33:28); the high places "THE NECKS OF THEIR KINGS" (33:29 — Joshua 10:24, the spine's own last row)
assert (len(W(33, 2)), len(ARM(33, 2))) == (16, 23) and 'מגו אשתא אוריתא יהב לנא' in ' '.join(ARM(33, 2)) and (len(W(33, 3)), len(ARM(33, 3))) == (11, 17) and 'תחות עננך נטלין על מימרך' in ' '.join(ARM(33, 3)) and 'נביא דיי' in ' '.join(ARM(33, 1)) and (len(W(33, 1)), len(ARM(33, 1))) == (12, 12) and ' '.join(ARM(33, 5)).startswith('והוה בישראל מלכא') and (len(W(33, 5)), len(ARM(33, 5))) == (9, 9)   # from the midst of fire the Torah He gave us; under Your cloud journeying by Your Memra; the prophet of the LORD; and there was a king in Israel
assert (len(W(33, 6)), len(ARM(33, 6))) == (7, 12) and 'לחיי עלמא ומותא תנינא לא ימות' in ' '.join(ARM(33, 6)) and (len(W(33, 7)), len(ARM(33, 7))) == (16, 23) and 'קבל יי צלותיה דיהודה במפקיה לאגחא קרבא' in ' '.join(ARM(33, 7)) and (len(W(33, 8)), len(ARM(33, 8))) == (13, 20) and 'תמיא ואוריא אלבשתא' in ' '.join(ARM(33, 8)) and 'על מי מצותא ואשתכח מהימן' in ' '.join(ARM(33, 8))   # to eternal life, and the second death he shall not die; receive, LORD, Judah's prayer when he goes out to war; the Thummim and the Urim You clothed; at the waters of strife, and found faithful
assert (len(W(33, 9)), len(ARM(33, 9))) == (18, 22) and 'לא רחם כד חבו מן דינא' in ' '.join(ARM(33, 9)) and 'נטרו מטרת מימרך' in ' '.join(ARM(33, 9)) and 'קטורת בוסמין קדמך' in ' '.join(ARM(33, 10)) and 'וקרבן ידוהי תקבל ברעוא' in ' '.join(ARM(33, 11)) and (len(W(33, 12)), len(ARM(33, 12))) == (14, 15) and 'ובארעיה תשרי שכנתא' in ' '.join(ARM(33, 12))   # had no mercy when they sinned from the judgment; kept the watch of Your Memra; incense of spices before You; the offering of his hands receive with favor; in his land the Shekhinah shall dwell
assert (len(W(33, 13)), len(ARM(33, 13))) == (11, 19) and 'מריש ירח בירח' in ' '.join(ARM(33, 14)) and 'רמן דלא פסקן' in ' '.join(ARM(33, 15)) and (len(W(33, 16)), len(ARM(33, 16))) == (12, 21) and 'ועל משה אתגלי באסנא' in ' '.join(ARM(33, 16)) and 'ס"א' in ' '.join(ARM(33, 16)) and (len(W(33, 17)), len(ARM(33, 17))) == (19, 26) and 'רבותא דבית אפרים' in ' '.join(ARM(33, 17)) and 'אלפיא דבית מנשה' in ' '.join(ARM(33, 17))   # from the head of month to month; hills that cease not; revealed to Moses in the bush; the export's variant marker inside the row; the myriads of the house of Ephraim, the thousands of the house of Manasseh
assert (len(W(33, 18)), len(ARM(33, 18))) == (7, 16) and 'זמני מועדיא בירושלם' in ' '.join(ARM(33, 18)) and 'לאגחא קרבא על בעלי דבבך' in ' '.join(ARM(33, 18)) and (len(W(33, 19)), len(ARM(33, 19))) == (14, 20) and 'לטור בית מקדשא יתכנשון' in ' '.join(ARM(33, 19)) and (len(W(33, 20)), len(ARM(33, 20))) == (11, 11) and 'ויקטול שלטונין עם מלכין' in ' '.join(ARM(33, 20))   # the times of the festivals in Jerusalem; to wage war on your enemies; to the mountain of the sanctuary house they gather; slays rulers with kings
assert (len(W(33, 21)), len(ARM(33, 21))) == (17, 23) and 'משה ספרא רבא דישראל קביר' in ' '.join(ARM(33, 21)) and 'מן נחליא דנגדן מן מתנן' in ' '.join(ARM(33, 22)) and 'ים גנוסר ודרומא ירת' in ' '.join(ARM(33, 23)) and 'בתפנוקי מלכין' in ' '.join(ARM(33, 24)) and ' '.join(ARM(33, 25)).startswith('תקיף כפרזלא ונחשא') and ' '.join(ARM(33, 26)).startswith('לית אלה כאלהא דישראל דשכנתיה בשמיא')   # Moses the great scribe of Israel is buried; from the rivers that flow from Matnan; the sea of Gennesar and the south he inherits; the delicacies of kings; strong as iron and brass; there is no God like the God of Israel whose Shekhinah is in heaven
assert 'במימריה מתעבד עלמא' in ' '.join(ARM(33, 27)) and (len(W(33, 28)), len(ARM(33, 28))) == (14, 18) and 'כעין ברכתא דברכנון יעקב אבוהון' in ' '.join(ARM(33, 28)) and (len(W(33, 29)), len(ARM(33, 29))) == (19, 24) and 'על פריקת צוארי מלכיהון תדרך' in ' '.join(ARM(33, 29))   # by His Memra the world was made; as the blessing Jacob their father blessed them; you shall tread on the necks of their kings
assert SEATS('עלמ') == [(32, 7), (32, 12), (32, 40), (33, 6), (33, 27)] and SEATS('מצות') == [(32, 51), (33, 8)] and SEATS('סיני') == [(25, 9), (28, 23), (33, 2)] and SEATS('פארן') == [(1, 1), (33, 2)] and SEATS('קרבן') == [(33, 11)] and SEATS('מקדש') == [(3, 25), (23, 19), (33, 19)] and SEATS('צואר') == [(28, 48), (33, 29)] and len(SEATS('אורית')) == 25 and SEATS('אורית')[-3:] == [(33, 2), (33, 4), (33, 10)] and len(SEATS('מתנן')) == 14 and SEATS('מתנן')[-1] == (33, 22) and len(SEATS('מדבח')) == 6 and SEATS('מדבח')[-1] == (33, 10)   # the world; the strife; Sinai; Paran; the offering; the sanctuary; the necks; the Torah (its three seats in 33 — the fiery law, the inheritance, Your Torah to Israel; retyped from the second pass's print); Matnan; the altar
assert len(SEATS('שבט')) == 22 and SEATS('שבט')[-3:] == [(33, 3), (33, 5), (33, 19)] and len(SEATS('דבב')) == 22 and SEATS('דבב')[-3:] == [(33, 7), (33, 11), (33, 18)] and len(SEATS('נסי')) == 13 and SEATS('נסי')[-2:] == [(33, 8), (33, 9)] and len(SEATS('תקיפ')) == 22 and not [s for s in SEATS('תקיפ') if s[0] == 33] and {(33, 22), (33, 25), (33, 29)} <= set(SEATS('תקיף')) and {(32, 20), (33, 12), (33, 16), (33, 26)} <= set(SEATS('שכנת'))   # the tribes; the enemies; the trial; the Mighty One (takifa — none in 33; the adjective "strong" at Dan, the bars, the help); the Shekhinah's seats
# THE FRAMES, THE REGISTER AND THE PARSER: six imperatives (hear 33:7; bless, smite 33:11; rejoice 33:18; possess 33:23; destroy 33:27) and Reuben's three jussives (let him live, let him not die, let his men be — 33:6); THE CHAPTER NEVER SAYS "THE LORD YOUR GOD"; the register empty; THE PARSER'S ONE MARK — 33:23's "sated" carries seven's consonants and is MARKED, NOT COUNTED (no false number in the chapter; the myriads of 33:2 and 33:17 and the "number" of 33:6 unread — the parser's forms are the cardinal words)
MO = {(c, v): [(x, m) for x, m in by[('Deut', c, v)]] for c, v in SPAN}
assert [(v, x) for c, v in SPAN for x, m in MO[(c, v)] if m and re.search(r'V[a-zA-Z]v', m)] == [(7, 'שמע'), (11, 'ברך'), (11, 'מחץ'), (18, 'שמח'), (23, 'ירשה'), (27, 'השמד')] and [(v, x, m) for c, v in SPAN for x, m in MO[(c, v)] if m and re.search(r'V[a-zA-Z]j', m)] == [(6, 'יחי', 'HVqj3ms'), (6, 'ימת', 'HVqj3ms'), (6, 'ויהי', 'HC/Vqj3ms')] and MO[(33, 2)][0] == ('ויאמר', 'HC/Vqw3ms') and MO[(33, 6)][2] == ('ואל', 'HC/Tn')   # hear, bless, smite, rejoice, possess, destroy; let him live, let him not die, let there be; and he said; and-not (the vetitive particle)
assert [v for v in range(1, 30) if any(a == 'יהוה' and b == 'אלהיך' for a, b in zip(W(33, v), W(33, v)[1:]))] == [] and sum(1 for v in range(1, 30) for x in W(33, v) if x == 'יהוה') == 7 and sum(1 for v in range(1, 30) for x in W(33, v) if x == 'ליהוה') == 0 and sum(1 for v in range(1, 30) for x in W(33, v) if x == 'ביהוה') == 1
_MP = open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'ch33_measure_lean.out'), encoding='utf-8').read()
assert "the register on Deut 33 — receipts: [] | footers: [] | headers: []" in _MP, 'the register: no seat in the chapter'
assert "the parser's hits: {(33, 23): ([], [], ['שבע*'])}" in _MP and "33:23 \"sated with favor\" (the mark): ['ולנפתלי', 'אמר', 'נפתלי', 'שבע*', 'רצון', 'ומלא']" in _MP and "['והם', 'רבבות', 'אפרים', 'והם', 'אלפי', 'מנשה']" in _MP and "['ימת', 'ויהי', 'מתיו', 'מספר']" in _MP   # the one mark — sated (seva) as seven's homograph, marked with the star and counted as nothing; the myriads and the thousands and the number unread
# THE PRIOR READS (computed from the ledgers): eighteen seats of the spine's rows read before over eleven ledgers (fifteen distinct rows — 342:1 twice, 352:9 twice, 355:6 twice; the Genesis ledgers cite the theophany's piska on the bow and on Hagar's angel) — every one REREAD WHOLE here; ALL FIVE outside rows read before, NONE fresh
assert len(SPINE_PRIOR) == 18 and len({(p, r) for _, p, r in SPINE_PRIOR}) == 15 and len({f for f, _, _ in SPINE_PRIOR}) == 11 and {(342, 1), (343, 6), (343, 9), (345, 2), (346, 2), (347, 3), (351, 1), (352, 8), (352, 9), (352, 10), (352, 17), (355, 6), (355, 9), (355, 27), (356, 5)} == {(p, r) for _, p, r in SPINE_PRIOR}, (len(SPINE_PRIOR), sorted({(p, r) for _, p, r in SPINE_PRIOR}))
assert PRIOR_READ == {(31, 6): ['deu_06_vaetchanan_2026-09-17.md'], (42, 9): ['deu_11_ekev_reeh_2026-09-20.md'], (48, 9): ['deu_11_ekev_reeh_2026-09-20.md', 'deu_29_31_nitzavim_vayelech_2026-09-27.md'], (314, 1): ['deu_32_haazinu_2026-09-27.md'], (329, 3): ['deu_32_haazinu_2026-09-27.md']} and FRESH == [], (PRIOR_READ, FRESH)
assert STORE_MISMATCH == [(33, 2, 18, 16), (33, 9, 19, 18)] and sum(len(W(33, v)) for v in range(1, 30)) == 336 and len({g for (cc, v) in SG if cc == 33 for _, _, g in SG[(cc, v)]}) == 263 and [(v, hp) for (cc, v) in SG for _, hp, g in SG[(cc, v)] if g == '?'] == [] and [hp for _, hp, g in SG[(33, 2)]].count('אשדת') == 1 and 'אש' in [hp for _, hp, g in SG[(33, 2)]] and 'דת' in [hp for _, hp, g in SG[(33, 2)]] and 'בנו' in [hp for _, hp, g in SG[(33, 9)]] and 'בניו' in [hp for _, hp, g in SG[(33, 9)]]   # THE STORE'S TWO MISMATCHES ARE KETIV AND QERE BOTH KEPT: the fiery law one word and two (33:2), "his son" and "his sons" (33:9); no "?" gloss in the chapter (the song had seven)

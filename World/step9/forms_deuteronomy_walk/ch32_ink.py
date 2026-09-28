import os as _os
_ROOT = _os.path.normpath(_os.path.join(_os.path.dirname(_os.path.abspath(__file__)), '..', '..', '..'))   # THE PORTABLE REPO (2026-09-15): the repo root from this file's own place
#!/usr/bin/env python3
# THE DEUTERONOMY WALK, sitting 20 — CHAPTER 32, THE SONG, Deuteronomy 32:1-52 IN THE LEAN FORM (2026-09-27; the owner: "Continue" after sitting 19b's tail and the push
# c4b14ce, no compaction between, /context 332k at the open — THE LEAN PASS's thirteenth sitting, its seventh reading; THE SPINE IN FORCE: thirty-six piskaot 306-341 with
# 249 rows, 358 KB — the export's longest piska 306 on 32:1 with thirty-seven rows): THE INK of the chapter, computed from the Tanakh DB, the snapshot store and the shelf's
# own bytes — never typed. Sitting 19's form (ch29_ink.py): the generic helpers copied by derive_ch32_ink.py from the forms' ch22_ink.py by content markers (the chapter
# substituted), the constants and every assert the chapter's own, typed FROM THE PRINTS (ch32_dump0.out, ch32_split.out, ch32_measure_lean.out). THE TWO DIVISIONS AGREE
# (52 = 52, cost 141) — the identity. TWO DRAFTS on file: deu_32_haazinu (32:1-43, the song) and deu_32_song_aftermath (32:44-52, the frame and the summons to Nebo) — two
# units in one chapter, CHAPTER NUMBERS. ELEVEN rows elsewhere cite the chapter (the split's print). NO portion edge inside the chapter (Haazinu is 32:1-52 whole). The
# parser MEASURED on every verse — THE FALSE EIGHT at 32:15 ("you grew fat", shamanta, read as the number eight — the false six's precedent at 28:63 and 30:9) and the
# joined thousand at 32:30 ("one chase a thousand, and two put ten thousand to flight" read as [1, 1002] with 'one' marked); 328's head CITED AS 32:35 by the export while its
# text is 32:38's ("who ate the fat of their sacrifices") — a misprinted verse marker in the heads table (sitting 19's lesson 1). The hand's facts as asserts, run all at once by assert_driver.py.
import json, os, re, html, sqlite3, sys, io, contextlib, unicodedata, subprocess
from collections import Counter
ROOT = _ROOT
DATE = '2026-09-27'
CHS = (32,)
UIDS = ['deu_32_haazinu', 'deu_32_song_aftermath']   # the drafts' own ids (the G prints): two units in the one chapter — the song 32:1-43 and its frame 32:44-52
SPANS = {'deu_32_haazinu': (32, 1, 43), 'deu_32_song_aftermath': (32, 44, 52)}
PREFIX = {'deu_32_haazinu': 'DV32', 'deu_32_song_aftermath': 'DV32A'}
SPAN = [(32, v) for v in range(1, 53)]
PISKAOT = list(range(306, 342))   # THE SPINE ON CHAPTER 32: thirty-six piskaot, every head present (the A prints and the split's); 305 headless before (31:14-23's), 342 headless after (33:1's)
PISKAOT_BY = {32: PISKAOT}
HEADLESS = []   # none inside the chapter (the dump's heads table: 306-341 every head a chapter-32 citation)
SPINE_ROWS = {306: 37, 307: 15, 308: 4, 309: 7, 310: 8, 311: 5, 312: 2, 313: 16, 314: 6, 315: 6, 316: 4, 317: 7, 318: 16, 319: 6, 320: 13, 321: 14, 322: 12, 323: 13, 324: 3, 325: 4, 326: 7, 327: 2, 328: 4, 329: 4, 330: 2, 331: 4, 332: 6, 333: 5, 334: 3, 335: 2, 336: 2, 337: 1, 338: 3, 339: 3, 340: 2, 341: 1}   # rows per piska, both files (the heads table and the split's print) — 249
PREV_CHAPTER_ROWS = []   # no tail folded in (305's rows carry no word of 32:1 — the split's assert; 305:6 ends with Joshua weeping and 306:1 opens with 32:1's citation)
READ_ROWS = [(p, r) for p in PISKAOT for r in range(1, SPINE_ROWS[p] + 1)]   # 249 — this ledger's spine rows, read WHOLE over the row runs by the split's byte plan
EXP2DB = {32: {e: [e] for e in range(1, 53)}}   # the identity (the offset 0 at every export verse — A0's print)
DB2EXP = {c: {d: e for e, ds in EXP2DB[c].items() for d in ds} for c in CHS}
OUTSIDE = [(1, 1), (37, 11), (39, 11), (43, 24), (48, 2), (48, 10), (342, 1), (346, 2), (355, 6), (356, 5), (357, 27)]   # the ELEVEN rows READ WHOLE: the union of the two files beyond piskaot 306-341 (the dump's and the split's print)
EXCLUDED = []   # none known at the design — a translator's misprint is judged by the Hebrew at the whole read (sitting 18's lesson 4)
INTERPOLATION = []
CREDITED = {}   # under THE WHOLE-ROW RULE no spine row is credited: rows read before (the dump lists fourteen ledgers' seats among 306-341) are REREAD WHOLE here and marked so
TITLE = "Chapter 32 — the song: give ear, O heavens, and hear, O earth; the Rock whose work is perfect, a perverse and crooked generation; remember the days of old — the Most High divided the nations by the number of the children of Israel, the LORD's portion is His people; He found him in a desert land, as an eagle over her young, the LORD alone led him, honey from the rock, the blood of the grape; Jeshurun grew fat and kicked, forsook the God who made him, sacrificed to demons, to gods they knew not; the LORD saw and spurned, I will hide My face, a perverse generation, I will provoke them with a foolish nation, a fire kindled to the depths of Sheol, arrows spent, the teeth of beasts, the sword without and terror within; I would have said I will blot them out, but for the enemy's boast; a nation void of counsel — how should one chase a thousand unless their Rock had sold them; their vine of Sodom, their wine the venom of asps; vengeance is Mine and recompense, the LORD will judge His people when their power is gone — where are their gods who ate the fat of their sacrifices? See now that I, I am He, I kill and I make alive, I lift My hand to heaven, My glittering sword, vengeance on My adversaries, the blood of His servants — sing, O nations, of His people. Moses and Hoshea son of Nun spoke the song; set your heart to all these words, it is your life; and on that selfsame day: go up to Mount Nebo in the Abarim, see the land and die on the mountain as Aaron died on Hor, because you broke faith at the waters of Meribath-kadesh — you shall see the land from afar but not go there."
OUT = f'{ROOT}/logic/oral_triage/deu_32_haazinu_{DATE}.md'
PATCHED = bool(os.environ.get('DEU32_PATCHED'))   # the tail's flag: after the manifests and the seat, the drafts carry operators and the store its overrides
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
def W32(v): return words('Deut', 32, v)
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
for c, v, idx, hp, g in store.execute("SELECT v.chapter, v.verse, w.idx, w.he_plain, w.gloss FROM words w JOIN verses v ON w.verse_id=v.id WHERE v.book='Deut' AND v.chapter IN (32) ORDER BY v.id, w.idx"):
    SG.setdefault((c, v), []).append((idx, hp.replace('/', ''), g))
def sg(c, v, tok, nth=0):
    hit = [g for _, hp, g in SG[(c, v)] if hp == tok]
    if len(hit) <= nth: raise KeyError((c, v, tok, nth))
    return hit[nth]
def sidx(c, v, tok, nth=0):
    hit = [i for i, hp, _ in SG[(c, v)] if hp == tok]
    assert len(hit) > nth, (c, v, tok, nth, hit)
    return hit[nth]
STORE_MISMATCH = [(c, v, n, len(by[('Deut', c, v)])) for c, v, n in store.execute("SELECT v.chapter, v.verse, COUNT(*) FROM words w JOIN verses v ON w.verse_id=v.id WHERE v.book='Deut' AND v.chapter IN (32) GROUP BY v.chapter, v.verse").fetchall() if n != len(by[('Deut', c, v)])]
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
# THE SHELF BY POSITION — THE SPINE IN FORCE on chapter 32: thirty-six heads 306-341 (the dump's window 300-345); 305 headless before, 342 headless after; the heads by chapter as sitting 19's dumps printed them (the same table)
assert NV == {32: 52} and VC[31] == 30 and VC[33] == 29 and VC[34] == 12 and len(sif) == 357 and len(sif_he) == 357 and sum(len(s) for s in sif) == 2357 and sum(len(s) for s in sif_he) == 2357
HC = Counter(h[0] for h in heads.values() if h)
assert (HC[31], HC[32], HC[33], HC[34]) == (1, 36, 14, 1) and sorted(HC.items()) == [(1, 24), (3, 4), (6, 6), (11, 21), (12, 20), (13, 14), (14, 14), (15, 16), (16, 19), (17, 16), (18, 16), (19, 10), (20, 14), (21, 17), (22, 22), (23, 22), (24, 16), (25, 10), (26, 4), (31, 1), (32, 36), (33, 14), (34, 1)], sorted(HC.items())
WIN = {300: (26, 4), 301: (26, 5), 302: (26, 12), 303: None, 304: (31, 14), 305: None, 306: (32, 1), 307: (32, 4), 308: (32, 5), 309: (32, 6), 310: (32, 7), 311: (32, 8), 312: (32, 9), 313: (32, 10), 314: (32, 11), 315: (32, 12), 316: (32, 13), 317: (32, 14), 318: (32, 15), 319: (32, 18), 320: (32, 19), 321: (32, 23), 322: (32, 26), 323: (32, 29), 324: (32, 34), 325: (32, 35), 326: (32, 36), 327: (32, 37), 328: (32, 35), 329: (32, 39), 330: (32, 40), 331: (32, 41), 332: (32, 42), 333: (32, 43), 334: (32, 44), 335: (32, 46), 336: (32, 47), 337: (32, 48), 338: (32, 49), 339: (32, 50), 340: (32, 51), 341: (32, 52), 342: None, 343: (33, 2), 344: (33, 3), 345: (33, 4)}
assert {p: heads[p] for p in range(300, 346)} == WIN, {p: heads[p] for p in range(300, 346) if heads[p] != WIN[p]}
assert heads[328] == (32, 35) and 'Who ate the fat of their sacrificial' in clean(sif[327][0]) and HB0(328, 1).startswith('(דברים לב לה) אשר חלב זבחימו יאכלו'), (heads[328], clean(sif[327][0])[:80], HB0(328, 1)[:60])   # 328's HEAD MISPRINTED IN THE HEBREW ROW ITSELF: the row's own marker reads (Deuteronomy 32:35) before 32:38's words ("who ate the fat of their sacrifices") — the export's verse marker wrong, the head computed from it (sitting 19's lesson 1 in a head); retyped from the first pass's print
HV = {c: [heads[p][1] for p in PISKAOT_BY[c] if heads[p]] for c in CHS}
assert HV == {32: [1, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 18, 19, 23, 26, 29, 34, 35, 36, 37, 35, 39, 40, 41, 42, 43, 44, 46, 47, 48, 49, 50, 51, 52]}, HV
NOHEAD = {c: [v for v in range(1, NV[c] + 1) if v not in HV[c]] for c in CHS}
assert NOHEAD == {32: [2, 3, 16, 17, 20, 21, 22, 24, 25, 27, 28, 30, 31, 32, 33, 38, 45]}, NOHEAD   # seventeen verses without a head of their own — inside the piskaot before them (38 by 328's misprint)
assert {p: (len(sif_he[p - 1]), len(sif[p - 1])) for p in PISKAOT} == {p: (n, n) for p, n in SPINE_ROWS.items()} and sum(SPINE_ROWS.values()) == 249 and len(READ_ROWS) == 249 and len(PISKAOT) == 36 and READ_ROWS[0] == (306, 1) and READ_ROWS[-1] == (341, 1) and SPINE_ROWS[306] == 37 and max(SPINE_ROWS.values()) == 37
# THE TAILS AND THE EDGES (the split's print): 305's rows carry no word of 32:1; 305:6 ends with Joshua weeping; 306:1 opens with 32:1's citation and R. Meir; 341:1 opens with 32:52's; 342:1 opens with 33:1's and names 32:24-25
assert not any(w in HB0(305, r) for r in range(1, 7) for w in ('האזינו',)) and HB0(305, 6).startswith('וכיון שמת משה היה יהושע בוכה') and HB0(306, 1).startswith('(דברים לב א) האזינו השמים ואדברה, רבי מאיר אומר') and HB0(341, 1).startswith('(דברים לב נב) כי מנגד תראה את הארץ ושמה לא תבא') and HB0(342, 1).startswith('(דברים לג, א) וזאת הברכה אשר ברך משה') and '(דברים לב כד-כה)' in HB0(342, 1)
assert all(clean(sif[p - 1][0]).startswith('Pisqa’ %d' % p) for p in PISKAOT) and 'Lend an ear, Heavens' in clean(sif[305][0]) and 'For only from afar shall you see the Land' in clean(sif[340][0]) and 'And this is the blessing' in clean(sif[341][0])   # the English rows open with the translator's apparatus before the text (sitting 19's lesson)
# THE CITATIONS PARSED FROM THE DUMP'S PRINT (the instrument's own lists read back): the row-citations per file, the union, the outside set; the divisions; the store
import ast as _ast
_t = open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'ch32_dump0.out'), encoding='utf-8').read()
_HE = _ast.literal_eval(re.search(r'^  HE rows citing Deut 32[^:]*: \d+ (\[.*\])$', _t, re.M).group(1)); _EN = _ast.literal_eval(re.search(r'^  EN rows citing Deut 32[^:]*: \d+ (\[.*\])$', _t, re.M).group(1))
_un = int(re.search(r'^  the union of rows \(both files\): (\d+) \[', _t, re.M).group(1)); _out = _ast.literal_eval(re.search(r'^  the rows OUTSIDE the spine piskaot [^:]*: \d+ (\[.*?\]) \|', _t, re.M).group(1)); _insp = int(re.search(r'\| in-spine rows of the union: (\d+)$', _t, re.M).group(1))
_two = re.search(r'^  DB verses (\d+) \| export verses HE (\d+) EN (\d+) \| per-chapter export lengths vs DB, chapters 1-32: (\[.*\])$', _t, re.M); _cost = int(re.search(r'^  the alignment cost (\d+) \|', _t, re.M).group(1))
_mis = _ast.literal_eval(re.search(r'verses whose store token count differs from the DB: (\[.*?\])$', _t, re.M).group(1)); _tok = int(re.search(r'^  token count chapter 32 : (\d+)$', _t, re.M).group(1))
assert (len(_HE), len(_EN), _un, _insp) == (61, 368, 242, 231) and _out == OUTSIDE and len(_out) == 11, (len(_HE), len(_EN), _un, _insp, _out)
assert tuple(int(x) for x in _two.groups()[:3]) == (52, 52, 52) and _two.group(4) == '[(5, 30, 33)]' and _cost == 141, 'THE TWO DIVISIONS: the identity; chapter 5 the book\'s one split'
assert _mis == [(32, 13, 14, 13)] and _tok == 615, (_mis, _tok)   # THE STORE = THE DB except at 32:13 (the store one token more)
# THE OUTSIDE ROWS' FACTS COMPUTED from the dump's lists: the verses each row cites (the DB's numbering), the heads of their piskaot, the prior reads from the ledgers, the fresh rows
CITED = {}
for _p, _r, _e, _dbv in _HE + _EN:
    if (_p, _r) in OUTSIDE:
        for _d in _dbv: CITED.setdefault((_p, _r), set()).add((32, _d))
CITED = {k: sorted(v) for k, v in sorted(CITED.items())}
assert sorted(CITED) == OUTSIDE, (sorted(set(OUTSIDE) - set(CITED)), sorted(set(CITED) - set(OUTSIDE)))
assert CITED[(1, 1)] == [(32, 1), (32, 15)] and CITED[(37, 11)] == [(32, 49)] and CITED[(39, 11)] == [(32, 2)] and CITED[(43, 24)] == [(32, 23)] and CITED[(48, 2)] == [(32, 47)] and CITED[(48, 10)] == [(32, 47)], {k: CITED[k] for k in ((1, 1), (37, 11), (39, 11), (43, 24), (48, 2), (48, 10))}
HEADS_ON = {p: heads[p] for p in sorted({p for p, _ in OUTSIDE})}
assert HEADS_ON == {1: (1, 1), 37: (11, 10), 39: (11, 11), 43: (11, 15), 48: (11, 22), 342: None, 346: (33, 5), 355: (33, 20), 356: (33, 27), 357: (34, 1)}, HEADS_ON
_TRI = f'{ROOT}/logic/oral_triage'
LED = {f: open(f'{_TRI}/{f}', encoding='utf-8').read() for f in os.listdir(_TRI) if f.endswith('.md') and os.path.isfile(f'{_TRI}/{f}') and f != os.path.basename(OUT)}
SPINE_PRIOR = sorted({(f, int(a), int(b)) for f, t in LED.items() for a, b in re.findall(r'Sifrei Devarim (\d+):(\d+)', t) if int(a) in PISKAOT})
PRIOR_READ = {}
for f, t in LED.items():
    for a, b in re.findall(r'Sifrei Devarim (\d+):(\d+)', t):
        if (int(a), int(b)) in OUTSIDE: PRIOR_READ.setdefault((int(a), int(b)), []).append(f)
PRIOR_READ = {k: sorted(set(v)) for k, v in sorted(PRIOR_READ.items())}
FRESH = [k for k in OUTSIDE if k not in PRIOR_READ]
assert ('deu_04_vaetchanan_2026-09-16.md', 306, 1) in SPINE_PRIOR and ('deu_08_ekev_2026-09-18.md', 318, 1) in SPINE_PRIOR and len(SPINE_PRIOR) >= 12, len(SPINE_PRIOR)   # spine rows READ BEFORE at earlier chapters (the dump's list) — REREAD WHOLE here under the whole-row rule and marked so
assert (1, 1) in PRIOR_READ and (37, 11) in PRIOR_READ and (48, 2) in PRIOR_READ and (48, 10) in PRIOR_READ, sorted(PRIOR_READ)   # the dump's F list: 1:1 and 37:11 at chapters 1-3, 48:2 at chapter 4, 48:10 at chapter 8
# THE FRAMES AND THE NAMES (the dump's D section): the one divine frame and the one "saying" at 32:48; Hoshea's old name at 32:44; the case tokens
assert [(c, v) for c, v in SPAN if 'לאמר' in W(c, v)] == [(32, 48)] and 'והושע' in W(32, 44) and 'משה' in W(32, 44) and 'נון' in W(32, 44) and 'ישרון' in W(32, 15) and 'שאול' in W(32, 22)
assert [(c, v, x) for c, v in SPAN for x in W(c, v) if x in ('פן',)] == [(32, 27, 'פן'), (32, 27, 'פן')] and [(c, v) for c, v in SPAN if 'אם' in W(c, v)] == [(32, 30), (32, 41)] and [(c, v) for c, v in SPAN if 'לא' in W(c, v) and 'תבוא' in W(c, v)] == [(32, 52)]
# ---- THE ASSERTS TYPED FROM THE MEASURE'S PRINT (block b: ch32_measure_lean.out — the kin, the twins, the formulas, Onkelos, the frames, the register, the parser, the prior reads) ----
# THE KIN BY COMPUTATION: THE SONG'S VOCABULARY IS ITS OWN — eleven verses share no two tokens outside the stop list with any verse of the Bible (32:3, 5, 10, 16, 18, 26, 29, 31, 33, 34, 37); 32:36 quoted whole in Psalm 135:14 (seven in order); the frame's kin 31:30, 31:1, 31:12, 11:9, Numbers 27:12 and 27:14, 34:1, 34:4; 32:30's Joshua 23:10 (the Prophets' seat cited, never read)
assert [v for c, v in SPAN if not KINC[(c, v)]] == [3, 5, 10, 16, 18, 26, 29, 31, 33, 34, 37], [v for c, v in SPAN if not KINC[(c, v)]]
assert KINC[(32, 36)][0] == ('Ps 135:14', 4, 7) and KINC[(32, 44)][0] == ('Deut 31:30', 6, 5) and KINC[(32, 45)][0] == ('Deut 1:1', 3, 4) and KINC[(32, 46)][0] == ('Deut 17:19', 4, 7) and KINC[(32, 47)][0] == ('Josh 1:11', 5, 7) and KINC[(32, 48)][0] == ('Deut 27:9', 4, 4) and KINC[(32, 49)][0] == ('Num 27:12', 7, 10) and KINC[(32, 51)][0] == ('Num 20:1', 4, 4) and KINC[(32, 52)][0] == ('Deut 32:49', 3, 6) and KINC[(32, 30)][0] == ('Josh 23:10', 3, 3) and KINC[(32, 1)][1] == ('Deut 31:28', 2, 2) and KINC[(32, 17)][2] == ('Deut 29:25', 2, 3), (KINC[(32, 36)][0], KINC[(32, 49)][0], KINC[(32, 1)])
# THE TWINS DIFFED (shared / the longest run): the whole of 32:36 in Psalm 135:14; the summons to Nebo 32:49 against Numbers 27:12 ten shared, five in order; the frame 32:45 against 31:1, 32:46 against 31:12 six in order, 32:47 against 11:9 five; the selfsame day 32:48 against Genesis 7:13 and Exodus 12:17; 32:17's 'gods they knew not' 29:25's; 32:20's hidden face 31:17's; the song at 32:1 shares NOTHING with Isaiah 1:2's call to heaven and earth, 32:15 nothing with 31:20's satiety, 32:24 nothing with Leviticus 26:22's beasts — the kin is by sense, not by token
assert SHARED(('Deut', 32, 36), ('Ps', 135, 14)) == ['כי', 'ידין', 'יהוה', 'עמו', 'ועל', 'עבדיו', 'יתנחם'] and SHARED(('Deut', 32, 49), ('Num', 27, 12)) == ['עלה', 'אל', 'הר', 'העברים', 'הזה'] and SHN(('Deut', 32, 49), ('Num', 27, 12)) == 10 and SHARED(('Deut', 32, 45), ('Deut', 31, 1)) == ['הדברים', 'האלה', 'אל', 'כל', 'ישראל'] and SHARED(('Deut', 32, 46), ('Deut', 31, 12)) == ['לעשות', 'את', 'כל', 'דברי', 'התורה', 'הזאת'] and SHARED(('Deut', 32, 47), ('Deut', 11, 9)) == ['תאריכו', 'ימים', 'על', 'האדמה', 'אשר'] and SHARED(('Deut', 32, 48), ('Gen', 7, 13)) == ['בעצם', 'היום', 'הזה'] and SHARED(('Deut', 32, 48), ('Exod', 12, 17)) == ['בעצם', 'היום', 'הזה']
assert SHARED(('Deut', 32, 44), ('Deut', 31, 30)) == ['דברי', 'השירה', 'הזאת'] and SHARED(('Deut', 32, 44), ('Num', 13, 16)) == ['בן', 'נון'] and SHARED(('Deut', 32, 51), ('Num', 27, 14)) == ['מריבת', 'קדש', 'מדבר', 'צן'] and SHARED(('Deut', 32, 17), ('Deut', 29, 25)) == ['לא', 'ידעום'] and SHARED(('Deut', 32, 20), ('Deut', 31, 17)) == ['פני', 'מהם'] and SHARED(('Deut', 32, 27), ('Deut', 9, 28)) == ['פן', 'יאמרו'] and SHARED(('Deut', 32, 52), ('Deut', 34, 4)) == ['ושמה', 'לא'] and SHARED(('Deut', 32, 50), ('Num', 27, 13)) == ['אל', 'עמיך'] and SHN(('Deut', 32, 1), ('Isa', 1, 2)) == 0 and SHN(('Deut', 32, 15), ('Deut', 31, 20)) == 0 and SHN(('Deut', 32, 24), ('Lev', 26, 22)) == 0 and SHN(('Deut', 32, 8), ('Gen', 11, 8)) == 0 and SHN(('Deut', 32, 11), ('Exod', 19, 4)) == 1
# THE FORMULAS (phrase seats by consonants over the Torah and the Bible): twenty phrases of the song ONCE in the Bible; the Rock four in the Torah; 'as an eagle' once in the Torah, eleven in the Bible; 'the selfsame day' eleven in the Torah; the Abarim and Nebo twice each; Meribath-kadesh thrice (Ezekiel 48:28 beside); 'this song' seven; 'set your heart' Haggai's thrice beside; 'prolong days' 11:9 and 32:47
assert P('האזינו', 'השמים', books=None) == ['Deut 32:1'] and P('ותשמע', 'הארץ', books=None) == ['Deut 32:1'] and P('דור', 'עקש', 'ופתלתל', books=None) == ['Deut 32:5'] and P('כאישון', 'עינו', books=None) == ['Deut 32:10'] and P('דבש', 'מסלע', books=None) == ['Deut 32:13'] and P('ישרון', books=None) == ['Deut 32:15', 'Deut 33:26'] and P('אסתירה', 'פני', books=None) == ['Deut 32:20'] and P('נקם', 'ושלם', books=None) == ['Deut 32:35'] and P('לי', 'נקם', books=None) == ['Deut 32:35'] and P('אמית', 'ואחיה', books=None) == ['Deut 32:39'] and P('אשא', 'אל', 'שמים', 'ידי', books=None) == ['Deut 32:40'] and P('ואין', 'אלהים', 'עמדי', books=None) == ['Deut 32:39']
assert P('אלהים', 'לא', 'ידעום', books=None) == ['Deut 32:17'] and P('ימות', 'עולם', books=None) == ['Deut 32:7'] and P('הוא', 'חייכם', books=None) == ['Deut 32:47'] and P('למספר', 'בני', 'ישראל', books=None) == ['Deut 32:8'] and P('גוי', 'אבד', 'עצות', books=None) == ['Deut 32:28'] and P('ושמה', 'לא', 'תבוא', books=None) == ['Deut 32:52'] and P('והאסף', 'אל', 'עמיך', books=None) == ['Deut 32:50'] and P('כאשר', 'מת', 'אהרן', 'אחיך', books=None) == ['Deut 32:50'] and P('מחוץ', 'תשכל', 'חרב', books=None) == ['Deut 32:25']
assert P('הצור', books=T) == ['Deut 32:4', 'Exod 17:6', 'Exod 33:21', 'Exod 33:22'] and len(P('הצור', books=None)) == 8 and P('כנשר', books=T) == ['Deut 32:11'] and len(P('כנשר', books=None)) == 11 and len(P('בעצם', 'היום', 'הזה', books=T)) == 11 and len(P('בעצם', 'היום', 'הזה', books=None)) == 14 and P('הר', 'העברים', books=None) == ['Deut 32:49', 'Num 27:12'] and P('הר', 'נבו', books=None) == ['Deut 32:49', 'Deut 34:1'] and P('מריבת', 'קדש', books=None) == ['Deut 32:51', 'Ezek 48:28', 'Num 27:14'] and P('השירה', 'הזאת', books=T) == ['Deut 31:19', 'Deut 31:21', 'Deut 31:22', 'Deut 31:30', 'Deut 32:44', 'Exod 15:1', 'Num 21:17'] and len(P('השירה', 'הזאת', books=None)) == 9
assert P('שימו', 'לבבכם', books=None) == ['Deut 32:46', 'Hag 1:5', 'Hag 1:7', 'Hag 2:18'] and P('תאריכו', 'ימים', books=None) == ['Deut 11:9', 'Deut 32:47'] and P('עשהו', books=T) == ['Deut 32:15', 'Exod 18:18'] and P('באזני', 'העם', books=T) == ['Deut 32:44', 'Exod 11:2', 'Exod 24:7'] and len(P('עליון', books=T)) == 8 and len(P('עליון', books=None)) == 32 and len(P('ביד', 'משה', books=T)) == 16 and len(P('ביד', 'משה', books=None)) == 31 and P('ראש', 'פתנים', books=None) == ['Job 20:16'] and P('סדם', 'ועמרה', books=T) == ['Deut 29:22', 'Gen 14:10', 'Gen 14:11', 'Gen 18:20', 'Gen 19:28'] and P('דם', 'ענב', books=None) == []
# THE WORDS: eight 'rock' words (the Rock at 32:4 with the article; their Rock 32:30, 32:31 twice; the rock's honey 32:13); the Name seven bare, once with lamed (32:6), once with vav (32:30); the names Bashan, Jeshurun, Sheol, HOSHEA (32:44 — the old name), Nebo, Meribah; vengeance thrice (32:35, 41, 43); the Most High 32:8; Eloah 32:15; the negations twelve; 'for/when' nineteen; 'if' 32:30 and 32:41; 'lest' 32:27; 'saying' 32:48 alone
assert [(v, x) for c, v in SPAN for x in W(c, v) if x in ('צור', 'הצור', 'צורם', 'וצור', 'צורנו', 'כצורנו', 'צר')] == [(4, 'הצור'), (13, 'צור'), (15, 'צור'), (18, 'צור'), (30, 'צורם'), (31, 'כצורנו'), (31, 'צורם'), (37, 'צור')] and [(v, x) for c, v in SPAN for x in W(c, v) if x in ('יהוה', 'ליהוה', 'ויהוה')] == [(3, 'יהוה'), (6, 'ליהוה'), (9, 'יהוה'), (12, 'יהוה'), (19, 'יהוה'), (27, 'יהוה'), (30, 'ויהוה'), (36, 'יהוה'), (48, 'יהוה')]
assert [(v, x) for c, v in SPAN for x in W(c, v) if x in ('שאול', 'ישרון', 'בשן', 'והושע', 'הושע', 'נבו', 'מריבת')] == [(14, 'בשן'), (15, 'ישרון'), (22, 'שאול'), (44, 'והושע'), (49, 'נבו'), (51, 'מריבת')] and [(v, x) for c, v in SPAN for x in W(c, v) if x.startswith(('נקם', 'ונקם'))] == [(35, 'נקם'), (41, 'נקם'), (43, 'ונקם')] and [v for c, v in SPAN for x in W(c, v) if x == 'עליון'] == [8] and 'אלוה' in W(32, 15) and sum(1 for c, v in SPAN for x in W(c, v) if x in ('לא', 'ולא')) == 12 and sum(1 for c, v in SPAN for x in W(c, v) if x == 'כי') == 19
# ONKELOS WRITING THE MEANING (the export's rows through NFKC): the Rock RENDERED 'the Mighty One' (takifa) at 32:4, 13, 14, 15, 18, 27, 30, 37 — twenty-two in the book; 'I will remove My Shekhinah' at 31:17, 31:18, 32:20 (and 'the house of My Shekhinah in heaven' for the lifted hand at 32:40); THE WORLD TO COME at 32:12 ('the world that is to be renewed'); the desert at 32:10 the Torah's school ('He taught them the words of the Torah' — 32:10 doubled, eleven to twenty); the Torah into 32:6, 32:10, 32:46; 'the age' (alma) at 32:7, 12, 40, 33:6, 33:27; the curds and milk of 32:14 'the spoil of their kings'; Jeshurun 'Israel'; demons 'in whom there is no use'; the vine of Sodom 'the punishment of the people of Sodom'; 'vengeance is Mine' 'at the time they go into exile'; Meribah 'the waters of the strife of Rekem'; the selfsame day 'in the middle of this day'
assert len(SEATS('תקיפ')) == 22 and SEATS('תקיפ')[-8:] == [(32, 4), (32, 13), (32, 14), (32, 15), (32, 18), (32, 27), (32, 30), (32, 37)] and SEATS('אסלק') == [(31, 17), (31, 18), (32, 20)] and SEATS('עלמ') == [(32, 7), (32, 12), (32, 40), (33, 6), (33, 27)] and SEATS('מצות') == [(32, 51), (33, 8)] and SEATS('שאול') == [(32, 22)] and SEATS('נשר') == [(14, 12), (28, 49), (32, 11)] and {(32, 6), (32, 10), (32, 46)} <= set(SEATS('אורית')) and len(SEATS('אורית')) == 25 and SEATS('שכינת') == [(31, 17)] and (32, 38) in SEATS('תרב')
assert (len(W(32, 4)), len(ARM(32, 4))) == (14, 19) and ' '.join(ARM(32, 4)).startswith('תקיפא דשלמין עובדוהי') and (len(W(32, 10)), len(ARM(32, 10))) == (11, 20) and 'אלפנון פתגמי אוריתא' in ' '.join(ARM(32, 10)) and (len(W(32, 12)), len(ARM(32, 12))) == (7, 13) and 'בעלמא דהוא עתיד לאתחדתא' in ' '.join(ARM(32, 12)) and (len(W(32, 14)), len(ARM(32, 14))) == (19, 20) and 'בזת מלכיהון' in ' '.join(ARM(32, 14)) and ' '.join(ARM(32, 15)).startswith('ועתר ישראל') and 'לשדין דלית בהון צרוך' in ' '.join(ARM(32, 17))
assert 'אסלק שכנתי מנהון' in ' '.join(ARM(32, 20)) and 'עד שאול ארעית' in ' '.join(ARM(32, 22)) and 'חד אלפא ותרין' in ' '.join(ARM(32, 30)) and 'כפרענות עמא דסדום' in ' '.join(ARM(32, 32)) and 'לעדן דיגלון מארעהון' in ' '.join(ARM(32, 35)) and 'בית שכנתי' in ' '.join(ARM(32, 40)) and 'תשבחתא הדא' in ' '.join(ARM(32, 44)) and ' '.join(ARM(32, 48)) == 'ומליל יי עם משה בכרן יומא הדין למימר' and 'במי מצות רקם' in ' '.join(ARM(32, 51)) and 'בהור טורא' in ' '.join(ARM(32, 50)) and (len(W(32, 1)), len(ARM(32, 1))) == (7, 7)
# THE FRAMES, THE REGISTER AND THE PARSER: twelve imperatives (give ear 32:1; ascribe 32:3; remember, consider, ask 32:7; see 32:39; sing 32:43; set 32:46; go up, see 32:49; die, be gathered 32:50 — the dump's own scan printed empty, its regex the fault, the morph codes read here); THE SONG NEVER SAYS "THE LORD YOUR GOD"; the register empty; the parser's FALSE EIGHT at 32:15 and the joined thousand at 32:30
MO = {(c, v): [(x, m) for x, m in by[('Deut', c, v)]] for c, v in SPAN}
assert [(v, x) for c, v in SPAN for x, m in MO[(c, v)] if m and re.search(r'V[a-zA-Z]v', m)] == [(1, 'האזינו'), (3, 'הבו'), (7, 'זכר'), (7, 'בינו'), (7, 'שאל'), (39, 'ראו'), (43, 'הרנינו'), (46, 'שימו'), (49, 'עלה'), (49, 'וראה'), (50, 'ומת'), (50, 'והאסף')] and MO[(32, 1)][0] == ('האזינו', 'HVhv2mp') and MO[(32, 7)][0] == ('זכר', 'HVqv2ms')
assert [v for v in range(1, 53) if any(a == 'יהוה' and b == 'אלהיך' for a, b in zip(W(32, v), W(32, v)[1:]))] == [] and sum(1 for v in range(1, 53) for x in W(32, v) if x == 'יהוה') == 7 and sum(1 for v in range(1, 53) for x in W(32, v) if x == 'ליהוה') == 1
_MP = open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'ch32_measure_lean.out'), encoding='utf-8').read()
assert "the register on Deut 32 — receipts: [] | footers: [] | headers: []" in _MP, 'the register: no seat in the chapter'
assert "the parser's hits: {(32, 15): ([8], [], []), (32, 30): ([1, 1002], [], ['אחד|'])}" in _MP and "32:15 \"grew fat\" (the false eight): ['וישמן', 'ישרון', 'ויבעט', 'שמנת', 'עבית']" in _MP and "['איכה', 'ירדף', 'אחד|', 'אלף', 'ושנים', 'יניסו', 'רבבה']" in _MP and "32:8 \"the number\": ['למספר', 'בני', 'ישראל']" in _MP
# THE PRIOR READS (computed from the ledgers): thirty-seven seats of the spine's rows read before over twenty-four ledgers (thirty distinct rows — 306's twelve among them; the Genesis ledgers cite the song's piska on the creation and the flood) — every one REREAD WHOLE here; eight of the eleven outside rows read before, THREE fresh (346:2, 356:5, 357:27 — the blessing's and the death's piskaot ahead, read here as sitting 19 read 345:2 and 357:28)
assert len(SPINE_PRIOR) == 37 and len({(p, r) for _, p, r in SPINE_PRIOR}) == 30 and len({f for f, _, _ in SPINE_PRIOR}) == 24 and {(306, 1), (306, 37), (318, 1), (334, 1), (337, 1)} <= {(p, r) for _, p, r in SPINE_PRIOR} and len([1 for _, p, r in SPINE_PRIOR if p == 306]) >= 12, (len(SPINE_PRIOR), len({(p, r) for _, p, r in SPINE_PRIOR}))
assert FRESH == [(346, 2), (356, 5), (357, 27)] and sorted(PRIOR_READ) == [(1, 1), (37, 11), (39, 11), (43, 24), (48, 2), (48, 10), (342, 1), (355, 6)] and PRIOR_READ[(355, 6)] == ['gen_22_covenant_bow_2026-08-25.md'] and PRIOR_READ[(342, 1)] == ['deu_09_ekev_2026-09-19.md'], (FRESH, PRIOR_READ)
assert STORE_MISMATCH == [(32, 13, 14, 13)] and sum(len(W(32, v)) for v in range(1, 53)) == 615 and len({g for (cc, v) in SG if cc == 32 for _, _, g in SG[(cc, v)]}) == 420 and [(v, hp) for (cc, v) in SG for _, hp, g in SG[(cc, v)] if g == '?'] == [(39, 'אני'), (39, 'אני'), (39, 'אני'), (40, 'אנכי'), (46, 'אנכי'), (49, 'אני'), (52, 'אני')]   # seven "?" glosses, all the pronoun "I" (a display patch at the tail, sitting 19's precedent)

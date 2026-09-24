import os as _os
_ROOT = _os.path.normpath(_os.path.join(_os.path.dirname(_os.path.abspath(__file__)), '..', '..', '..'))   # THE PORTABLE REPO (2026-09-15): the repo root from this file's own place
#!/usr/bin/env python3
# THE DEUTERONOMY WALK, sitting 14 — CHAPTER 16, Deuteronomy 16:1-22 IN THE LEAN FORM (2026-09-23; the owner: "Reread and go" after the compaction at #208 —
# THE LEAN PASS's first sitting: ONE reading window (the ink, the shelf, the ledger, the freeze), one compile window, a short tail): THE INK of the chapter,
# computed from the Tanakh DB, the snapshot store and the shelf's own bytes — never typed. Sitting 13's form (ch15_ink.py): the generic helpers copied by
# derive_ch16_ink.py from the forms' ch15_ink.py by content markers, the constants and every assert chapter 16's own, typed FROM THE PRINTS (ch16_dump0.out,
# ch16_measure_lean.out). THE TWO DIVISIONS AGREE (22 = 22; the alignment the identity, cost 23) — THE CHAPTER IS TWENTY-TWO VERSES in both numberings.
# THE SPINE IS ON THE CHAPTER — TWENTY piskaot (127-146) with 111 rows: nineteen heads computed in chapter 16 (127 and 128 both on 16:1 … 146 on 16:22; THE
# HEADS IN VERSE ORDER) and ONE HEADLESS piska, 135 (its head row cites no verse — "on the seventh day", 16:8's; in the spine by position, between 134 on 16:7
# and 136 on 16:9); 126 on 15:21 before, 147 on 17:1 after; no tail folded in (146's one row stops before 17:1's words). THREE rows elsewhere cite the chapter
# by the union of both files (52:4 on 11:25 — READ BEFORE at chapter 11, REREAD WHOLE; 147:2 on 17:1 — READ BEFORE at chapter 12, REREAD WHOLE; 281:1 on 24:17
# fresh), NONE excluded. A PORTION EDGE INSIDE THE CHAPTER (Re'eh ends at 16:17, Shoftim opens at 16:18 — the chapter the unit, CHAPTER NUMBERS). The parser
# MEASURED on every verse — EIGHT NUMBER VERSES (16:3 [7], 16:4 [7], 16:5 [1], 16:8 [6], 16:9 [7, 7], 16:13 [7], 16:15 [7], 16:16 [3]), TWO ORDINALS (16:4 [1]
# "the first day", 16:8 [7] "the seventh day") and ONE STARRED token (16:9 "weeks" marked — the number word "seven" inside it). THE STORE = THE DB at every
# verse (334 = 334). The hand's facts as asserts, run all at once by assert_driver.py.
import json, os, re, html, sqlite3, sys, io, contextlib, unicodedata, subprocess
from collections import Counter
ROOT = _ROOT
sys.path.insert(0, f'{ROOT}/World/step9')
DATE = '2026-09-23'
CH = 16
UIDS = ['deu_16_festivals_judges']
SPANS = {'deu_16_festivals_judges': (16, 1, 22)}
PREFIX = {'deu_16_festivals_judges': 'DV16'}
SPAN = [(16, v) for v in range(1, 23)]
PISKAOT = list(range(127, 147))   # THE SPINE ON THE CHAPTER: the twenty piskaot 127-146 — nineteen heads in chapter 16 (the A print) + 135 headless (the split's print); 126 heads on 15:21, 147 on 17:1
HEADLESS = [135]   # the head row of 135 carries no citation in the Hebrew ("on the seventh day … a solemn assembly", 16:8's words) — in the spine by position
SPINE_ROWS = {127: 8, 128: 5, 129: 7, 130: 7, 131: 5, 132: 4, 133: 2, 134: 5, 135: 3, 136: 8, 137: 3, 138: 8, 139: 1, 140: 7, 141: 3, 142: 6, 143: 9, 144: 15, 145: 4, 146: 1}   # rows per piska, both files (the I print and the splitter's) — 111
PREV_CHAPTER_ROWS = []   # no tail folded in this chapter (126's rows chapter 15's — asserted at its sitting; 146's row stops before 17:1's words)
READ_ROWS = [(p, r) for p in PISKAOT for r in range(1, SPINE_ROWS[p] + 1)]   # 111 — this ledger's spine rows
EXP2DB = {e: [e] for e in range(1, 23)}   # the identity — 22 = 22 (chapter 5 the book's one split)
DB2EXP = {d: e for e, ds in EXP2DB.items() for d in ds}
# the Hebrew's book-named citations of chapter 16 OUTSIDE the spine (the regex reads "(דברים טז טז)" etc.); every outside row cites it in the Hebrew this chapter
OUTSIDE_HE = [(52, 4, (16, 16)), (147, 2, (16, 5)), (281, 1, (16, 19))]
OUTSIDE = [(52, 4), (147, 2), (281, 1)]   # the THREE rows READ WHOLE: the union of both files beyond piskaot 127-146 (135's three rows folded INTO the spine at the split)
EXCLUDED = []   # every outside citation genuine
INTERPOLATION = []
CITED = {(52, 4): [16], (147, 2): [5], (281, 1): [19]}
CITED_DB = {k: v[0] for k, v in CITED.items()}
PRIOR_READ = {(52, 4): ['deu_11_ekev_reeh_2026-09-20.md'], (147, 2): ['deu_12_reeh_2026-09-20.md']}   # the two outside rows read before (computed from the ledgers, asserted) — REREAD WHOLE here
HEADS_ON = {52: (11, 25), 147: (17, 1), 281: (24, 17)}
FRESH = [(281, 1)]
CREDITED = {}   # under THE WHOLE-ROW RULE no spine row is credited: the two reads before (138:1 and 145:3 at chapter 12's sitting — the rejoicing at the place, the asherah beside the altar) are REREAD WHOLE here and marked so
TITLE = "Chapter 16 — Observe the month of Aviv and keep the Passover to the LORD your God, for in the month of Aviv He brought you out of Egypt by night; sacrifice the Passover, flock and herd, in the place where He will make His name dwell; eat no leaven with it — seven days unleavened bread, the bread of affliction, for in haste you went out, that you may remember the day of your going out all the days of your life; no leaven seen in all your border seven days, none of the flesh left overnight; you may not sacrifice the Passover within any of your gates but only at the place, at evening, at the going down of the sun, the season of your going out; cook it and eat it there, and in the morning turn and go to your tents; six days unleavened bread and on the seventh a solemn assembly, no work. Count seven weeks from the sickle's first cut on the standing grain and keep the feast of weeks with the measure of your hand's freewill gift as the LORD has blessed you; rejoice before Him — you, your son and daughter, your manservant and maidservant, the Levite in your gates, the sojourner, the fatherless and the widow — at the place; remember you were a slave in Egypt and keep these statutes. Keep the feast of booths seven days when you gather in from your threshing floor and your winepress; rejoice in your feast with the same company; seven days keep the feast at the place, for the LORD will bless you in all your produce and all your work, and you shall be altogether joyful. Three times a year all your males shall appear before the LORD at the place — at the feast of unleavened bread, of weeks and of booths — and none shall appear empty: each man as his hand can give, according to the blessing given him. Judges and officers you shall set in all your gates, tribe by tribe, to judge the people with righteous judgment: wrest no judgment, respect no person, take no bribe — for a bribe blinds the eyes of the wise and perverts the words of the righteous; justice, justice you shall pursue, that you may live and inherit the land. Plant no asherah of any tree beside the altar of the LORD your God, and set up no pillar, which the LORD your God hates"
OUT = f'{ROOT}/logic/oral_triage/deu_16_reeh_shoftim_{DATE}.md'
PATCHED = bool(os.environ.get('DEU16_PATCHED'))   # the tail's flag: after the manifest and the seat, the draft carries operators and the store its overrides
db = sqlite3.connect(f'file:{ROOT}/Data/tanakh.sqlite?mode=ro', uri=True)
VC = dict(db.execute("SELECT chapter, COUNT(*) FROM verses WHERE book='Deut' GROUP BY chapter").fetchall())
NV = VC[CH]
# ---- THE HELPERS (ch15_ink.py's, copied by content markers) ----
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
# ---- THE INK'S HELPERS, THE DB AND THE STORE (ch15_ink.py's, the chapter substituted) ----
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
def W16(v): return words('Deut', 16, v)
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
for c, v, idx, hp, g in store.execute("SELECT v.chapter, v.verse, w.idx, w.he_plain, w.gloss FROM words w JOIN verses v ON w.verse_id=v.id WHERE v.book='Deut' AND v.chapter = 16 ORDER BY v.id, w.idx"):
    SG.setdefault((c, v), []).append((idx, hp.replace('/', ''), g))
def sg(c, v, tok, nth=0):
    hit = [g for _, hp, g in SG[(c, v)] if hp == tok]
    if len(hit) <= nth: raise KeyError((c, v, tok, nth))
    return hit[nth]
def sidx(c, v, tok, nth=0):
    hit = [i for i, hp, _ in SG[(c, v)] if hp == tok]
    assert len(hit) > nth, (c, v, tok, nth, hit)
    return hit[nth]
STORE_MISMATCH = [(c, v, n, len(by[('Deut', c, v)])) for c, v, n in store.execute("SELECT v.chapter, v.verse, COUNT(*) FROM words w JOIN verses v ON w.verse_id=v.id WHERE v.book='Deut' AND v.chapter=16 GROUP BY v.chapter, v.verse").fetchall() if n != len(by[('Deut', c, v)])]
import difflib
def SH(a, b_): return sum(s for _, _, s in difflib.SequenceMatcher(a=words(*a), b=words(*b_)).get_matching_blocks())
D16 = lambda v: ('Deut', 16, v)
# THE KIN FOUND BY COMPUTATION (the measure's A section, recomputed here so the asserts read the same instrument): the shared distinct tokens outside the stop list, the top eight, the three closest re-scored in order
STOP = set('את ואת אשר כל וכל על ועל אל ואל לא ולא כי אם יהוה אלהיך אלהיכם לך לכם בו שם שמה גם מן ממך עד הוא היא אתם אתה אנכי אני לו לה בכל כאשר כן הימים היום אלה האלה בארץ הארץ אשר ואם או פן ופן ואת זה וזה הם המה'.split())
ORD = {k: i for i, k in enumerate(by)}
TOK = {k: set(words(*k)) - STOP for k in by}
KINC = {}
for _v in range(1, NV + 1):
    _me = D16(_v); _t = TOK[_me]
    _sc = sorted(((len(_t & TOK[k]), k) for k in by if k != _me and len(_t & TOK[k]) >= 2), key=lambda x: (-x[0], ORD[x[1]]))[:8]
    KINC[_v] = [(f'{k[0]} {k[1]}:{k[2]}', n, SH(_me, k) if i < 3 else None) for i, (n, k) in enumerate(_sc)]
DT = ('Deut',)
# ---- THE SHELF BY POSITION — the spine ON the chapter: twenty piskaot 127-146 (nineteen heads in chapter 16, IN VERSE ORDER, and 135 HEADLESS); 126 heads on 15:21 before, 147 on 17:1 after; no tail folded in; the two files' grains ----
assert NV == 22 and VC[15] == 23 and VC[17] == 20 and len(sif) == 357 and len(sif_he) == 357 and sum(len(s) for s in sif) == 2357 and sum(len(s) for s in sif_he) == 2357
HC = Counter(h[0] for h in heads.values() if h)
assert [p for p, h in heads.items() if h and h[0] == 16] == [p for p in range(127, 147) if p != 135] and HC[16] == 19 and sorted(HC.items())[:16] == [(1, 24), (3, 4), (6, 6), (11, 21), (12, 20), (13, 14), (14, 14), (15, 16), (16, 19), (17, 16), (18, 16), (19, 10), (20, 14), (21, 17), (22, 22), (23, 22)], sorted(HC.items())[:16]
assert {p: heads[p] for p in range(126, 148)} == {126: (15, 21), 127: (16, 1), 128: (16, 1), 129: (16, 2), 130: (16, 3), 131: (16, 4), 132: (16, 5), 133: (16, 6), 134: (16, 7), 135: None, 136: (16, 9), 137: (16, 10), 138: (16, 11), 139: (16, 12), 140: (16, 13), 141: (16, 14), 142: (16, 15), 143: (16, 16), 144: (16, 18), 145: (16, 21), 146: (16, 22), 147: (17, 1)}, {p: heads[p] for p in range(126, 148)}
HV = [heads[p][1] for p in PISKAOT if p not in HEADLESS]
assert HV == [1, 1, 2, 3, 4, 5, 6, 7, 9, 10, 11, 12, 13, 14, 15, 16, 18, 21, 22] and HV == sorted(HV) and [v for v in range(1, 23) if v not in HV] == [8, 17, 19, 20], HV   # THE HEADS IN VERSE ORDER; two piskaot head on 16:1; four verses carry no head — 16:8 is headless 135's, 16:17 is 143:9's, 16:19-20 are 144's
assert {p: (len(sif_he[p - 1]), len(sif[p - 1])) for p in PISKAOT} == {p: (n, n) for p, n in SPINE_ROWS.items()} and sum(SPINE_ROWS.values()) == 111 and len(READ_ROWS) == 111 and len(PISKAOT) == 20 and READ_ROWS[:2] == [(127, 1), (127, 2)] and READ_ROWS[-1] == (146, 1)
# THE HEADLESS PISKA: 135's head row opens with 16:8's own words and cites no verse in the Hebrew; in the spine by position
assert not re.match(r'\(דברים', HB0(135, 1)) and he_cites(Hb(135, 1)) == [('במדבר', 29, 35)] and HB0(135, 1).startswith('וביום השביעי עצרת לה׳ אלהיך') and re.search(r'Dt\.16:8', E(135, 1)) and HEADLESS == [135]   # the row's one Hebrew citation is NUMBERS 29:35 — the other "solemn assembly" — not at its head (the first pass typed 'no citation' for 'no head'; retyped from the print)
# NO TAIL FOLDED IN: 146's one row does not carry 17:1's words; 147:1 opens with 17:1's citation; 127:1 opens with 16:1's; 126's rows chapter 15's (asserted there)
assert HB0(127, 1).startswith('(דברים טז א) שמור את חדש האביב') and HB0(147, 1).startswith('(דברים יז א) לא תזבח') and 'לא תזבח' not in HB0(146, 1) and 'שור ושה' not in HB0(146, 1) and HB0(146, 1).startswith('(דברים טז כב) ולא תקים לך מצבה') and he_cites(Hb(127, 1)) == [('דברים', 16, 1)]
CIT_HE = [(p, r, (16, c[2])) for p in range(1, 358) for r in range(1, len(sif_he[p - 1]) + 1) for c in he_cites(Hb(p, r)) if c[0] == 'דברים' and c[1] == 16]
CIT_EN = [(p, r, (16, int(m.group(2)))) for p in range(1, 358) for r in range(1, len(sif[p - 1]) + 1) for m in re.finditer(r'\((?:Deut(?:eronomy)?\.?|Dt\.?|Devarim) ?(16):(\d+)', E(p, r))]
assert len(CIT_HE) == 29 and len(CIT_EN) == 132, (len(CIT_HE), len(CIT_EN))
assert [(p, r, v) for p, r, v in CIT_HE if p not in PISKAOT] == OUTSIDE_HE, [(p, r, v) for p, r, v in CIT_HE if p not in PISKAOT]
SPINE_CITES_HE = [(p, r, v) for p, r, v in CIT_HE if p in PISKAOT]
assert len(SPINE_CITES_HE) == 26 and SPINE_CITES_HE[:3] == [(127, 1, (16, 1)), (128, 1, (16, 1)), (128, 2, (16, 2))] and (129, 2, (16, 1)) in SPINE_CITES_HE and (134, 5, (16, 8)) in SPINE_CITES_HE and (143, 9, (16, 17)) in SPINE_CITES_HE and SPINE_CITES_HE[-3:] == [(144, 12, (16, 20)), (145, 1, (16, 21)), (146, 1, (16, 22))], SPINE_CITES_HE   # 129:2 cites 16:1 inside 16:2's piska; 134:5 cites 16:8 (the headless verse) inside 16:7's; 143:9 carries 16:17; 144's rows carry 16:19-20
UNION = sorted({(p, r) for p, r, _ in CIT_HE} | {(p, r) for p, r, _ in CIT_EN})
assert len(UNION) == 93 and [(p, r) for p, r in UNION if p not in PISKAOT] == OUTSIDE and len(OUTSIDE) == 3 and len([(p, r) for p, r in UNION if p in PISKAOT]) == 90, (len(UNION), [(p, r) for p, r in UNION if p not in PISKAOT])
assert all(1 <= v <= 22 for _, _, (_, v) in CIT_HE + CIT_EN)   # no cited verse beyond the chapter's twenty-two
assert [(p, r) for p in range(1, 358) for r in range(1, len(sif[p - 1]) + 1) if re.search(r'\((?:Ibid|ibid)\.? ?16:\d+\)', E(p, r))] == []   # no "ibid."
assert {p: heads[p] for p, _ in OUTSIDE} == HEADS_ON, {p: heads[p] for p, _ in OUTSIDE}
assert all(has_points(Hb(p, r)) for p, r in OUTSIDE) and all(has_points(Hb(p, r)) for p, r in READ_ROWS)
NOCITE = [(p, r) for p in PISKAOT for r in range(1, SPINE_ROWS[p] + 1) if not he_cites(Hb(p, r)) and not re.findall(r'\([A-Z][a-z]+\.? ?\d+:\d+', E(p, r))]
assert NOCITE == [(127, 7), (127, 8), (129, 4), (130, 5), (132, 2), (133, 2), (136, 3), (136, 8), (138, 4), (138, 5), (138, 6), (138, 7), (138, 8), (140, 5), (140, 7), (143, 2), (145, 4)] and len(NOCITE) == 17, NOCITE
# THE THREE OUTSIDE ROWS: 52:4 (on 11:25 — "who will guard our land" while all go up; the Hebrew cites 16:16; READ BEFORE at chapter 11); 147:2 (on 17:1 — the offerings out of order no prohibition; the Hebrew cites 16:5; READ BEFORE at chapter 12); 281:1 (on 24:17 — the sojourner's judgment two prohibitions; the Hebrew cites 16:19; fresh)
CIT_OUT = {(p, r): sorted({v for q, s, (_, v) in CIT_HE + CIT_EN if (q, s) == (p, r)}) for p, r in OUTSIDE}
assert CIT_OUT == CITED, CIT_OUT
assert he_cites(Hb(52, 4))[:2] == [('דברים', 16, 16), ('שמות', 34, 24)] and HB0(52, 4).startswith('יתן ה׳ אלהיכם למה נאמר') and he_cites(Hb(147, 2)) == [('דברים', 12, 17), ('דברים', 16, 5)] and HB0(147, 2).startswith('יכול המקדים קדשים זה לזה') and he_cites(Hb(281, 1)) == [('דברים', 24, 17), ('דברים', 16, 19)] and HB0(281, 1).startswith('(דברים כד יז) לא תטה משפט גר')
# ---- THE PRIOR READS (computed from the ledgers): two spine rows at chapter 12 (138:1 the rejoicing, 145:3 the asherah beside the altar), two outside rows (52:4 at chapter 11, 147:2 at chapter 12); NEVER READ AHEAD ----
TRI = f'{ROOT}/logic/oral_triage'
LED = {f: open(f'{TRI}/{f}', encoding='utf-8').read() for f in os.listdir(TRI) if f.endswith('.md') and os.path.isfile(f'{TRI}/{f}') and f != os.path.basename(OUT)}   # this sitting's own ledger is not a prior read (the writer's second run found it)
SPINE_PRIOR = sorted({(f, int(a), int(b)) for f, t in LED.items() for a, b in re.findall(r'Sifrei Devarim (\d+):(\d+)', t) if int(a) in PISKAOT})
OUT_PRIOR = sorted({(f, int(a), int(b)) for f, t in LED.items() for a, b in re.findall(r'Sifrei Devarim (\d+):(\d+)', t) if (int(a), int(b)) in OUTSIDE})
assert SPINE_PRIOR == [('deu_12_reeh_2026-09-20.md', 138, 1), ('deu_12_reeh_2026-09-20.md', 145, 3)] and OUT_PRIOR == [('deu_11_ekev_reeh_2026-09-20.md', 52, 4), ('deu_12_reeh_2026-09-20.md', 147, 2)] and {(p, r): [f] for f, p, r in OUT_PRIOR} == PRIOR_READ, (SPINE_PRIOR, OUT_PRIOR)
assert sorted(f for f, t in LED.items() if re.search(r'^- Onkelos (?:Deut (?:1[6-9]|2\d|3\d)|Josh|Judg|1Sam|2Sam|1Kgs|2Kgs|Isa|Jer|Ezek):', t, re.M)) == [] and sorted(f for f, t in LED.items() if re.search(r'^- Onkelos Exod (?:12|13|18):', t, re.M)) == []   # never read ahead; Exodus 12-13's Passover and 18's judges were read through their spines in the law era, before the Onkelos standing
KINL = [(f, kinrows(f, pat)) for f, pat in [('lev_23_festivals_2026-09-05.md', r'Lev 23:'), ('num_28_pesach_shavuot_2026-09-11.md', r'Num 28:'), ('num_29_fall_festivals_2026-09-11.md', r'Num 29:'), ('num_09_pesach_cloud_2026-09-09.md', r'Num 9:'), ('exo_23_justice_calendar_2026-09-01.md', r'Exod 23:'), ('exo_34_second_tablets_2026-09-01.md', r'Exod 34:'), ('lev_19_kedoshim_2026-09-05.md', r'Lev 19:'), ('lev_26_blessings_curses_2026-09-05.md', r'Lev 26:'), ('deu_01_03_devarim_2026-09-15.md', r'Deut 1:'), ('deu_07_vaetchanan_ekev_2026-09-17.md', r'Deut 7:'), ('deu_12_reeh_2026-09-20.md', r'Deut 12:'), ('deu_05_vaetchanan_2026-09-16.md', r'Deut 5:'), ('deu_15_reeh_2026-09-22.md', r'Deut 15:')]]
assert KINL == [('lev_23_festivals_2026-09-05.md', 44), ('num_28_pesach_shavuot_2026-09-11.md', 16), ('num_29_fall_festivals_2026-09-11.md', 39), ('num_09_pesach_cloud_2026-09-09.md', 23), ('exo_23_justice_calendar_2026-09-01.md', 7), ('exo_34_second_tablets_2026-09-01.md', 7), ('lev_19_kedoshim_2026-09-05.md', 37), ('lev_26_blessings_curses_2026-09-05.md', 44), ('deu_01_03_devarim_2026-09-15.md', 46), ('deu_07_vaetchanan_ekev_2026-09-17.md', 26), ('deu_12_reeh_2026-09-20.md', 31), ('deu_05_vaetchanan_2026-09-16.md', 33), ('deu_15_reeh_2026-09-22.md', 23)], KINL
NAMING = sorted(f for f, t in LED.items() if re.search(r'Deut(?:eronomy)? 16:\d+', t)); assert len(NAMING) == 30 and 'num_28_29_musafim_exam_2026-09-11.md' in NAMING and 'lev_23_festivals_2026-09-05.md' in NAMING and not any(re.search(r'^- Onkelos Deut 16:', LED[f], re.M) for f in NAMING), len(NAMING)
# ---- THE DRAFT: one unit, 22 steps, no operators yet; the claim prefix DV16 unused anywhere ----
for uid in UIDS:
    t = open(f'{ROOT}/logic/units/{uid}.yaml', encoding='utf-8').read()
    st = sorted({(int(a), int(b)) for a, b in re.findall(r'id: STEP_Dt_(\d+)_(\d+)', t)})
    assert [b for a, b in st] == list(range(1, 23)) and re.search(r'refs: "16:1-22"', t) and 'depends_on:\n    - "deu_15_release_firstborn"\n    - "lev_23_spring_festivals"\n    - "lev_23_fall_festivals"\n' in t, (uid, st[:2], st[-1])
    if not PATCHED: assert 'status: draft' in t and 'operators:' not in t and '- step: E' not in t, uid
import glob
assert not any('DV16-' in open(f, encoding='utf-8').read() for f in glob.glob(f'{ROOT}/logic/oral_audit/manifests/*_claims.json') + glob.glob(f'{ROOT}/logic/units/*.yaml') if 'deu_16' not in f) and (PATCHED or not glob.glob(f'{ROOT}/logic/oral_audit/manifests/deu_16*'))
# ---- THE TWO DIVISIONS AND THE STORE: 22 = 22 (the identity); the store = the DB at every verse ----
assert len(onk[15]) == 22 and len(onk_he[15]) == 22 and NV == 22 and EXP2DB == {e: [e] for e in range(1, 23)} and STORE_MISMATCH == [] and sum(len(W16(v)) for v in range(1, 23)) == 334 and len({g for k in SG for _, _, g in SG[k]}) == 169 and [(c, v, hp) for (c, v) in SG for _, hp, g in SG[(c, v)] if g == '?'] == []
assert len(onk_he[4]) == 30 and VC[5] == 33   # chapter 5 the book's one split, asserted again
# ---- THE PARSER (measured on cold_run_sequence.ink_numbers / ink_ordinals BEFORE any claim was typed): eight number verses, two ordinals, one starred token ----
with contextlib.redirect_stdout(io.StringIO()):
    import cold_run_sequence as CS
PARSE = {v: (CS.ink_numbers(CS.verse_words('Deut', 16, v)), CS.ink_ordinals(CS.verse_words('Deut', 16, v)), [t for t in CS.verse_words('Deut', 16, v) if t[-1] in '#~^%@|*']) for v in range(1, 23)}
assert {v: p for v, p in PARSE.items() if p[0] or p[1] or p[2]} == {3: ([7], [], []), 4: ([7], [1], []), 5: ([1], [], []), 8: ([6], [7], []), 9: ([7, 7], [], ['שבעת*']), 13: ([7], [], []), 15: ([7], [], []), 16: ([3], [], [])}, {v: p for v, p in PARSE.items() if p[0] or p[1] or p[2]}
NUMV = [v for v in PARSE if PARSE[v][0]]; ORDV = [v for v in PARSE if PARSE[v][1]]; STARV = [v for v in PARSE if PARSE[v][2]]
assert NUMV == [3, 4, 5, 8, 9, 13, 15, 16] and ORDV == [4, 8] and STARV == [9]
# ---- THE FRAMES AND THE REGISTER (computed on the morphology): THE CHAPTER SINGULAR FROM END TO END; no divine frame, no "saying", no first person, no narrative form, no imperative; one infinitive absolute — "observe", the chapter's first word ----
MO = {v: [(x, m) for x, m in by[('Deut', 16, v)]] for v in range(1, 23)}
assert all(sum(1 for _, m in MO[v] if m and '2mp' in m) == 0 for v in range(1, 23)) and all(sum(1 for _, m in MO[v] if m and '2ms' in m) >= 1 for v in range(1, 23)) and sum(sum(1 for _, m in MO[v] if m and '2ms' in m) for v in range(1, 23)) == 95, sum(sum(1 for _, m in MO[v] if m and '2ms' in m) for v in range(1, 23))
assert [(v, x) for v in range(1, 23) for x, m in MO[v] if m and re.search(r'V[a-zA-Z]a$', m)] == [(1, 'שמור')] and [(v, x) for v in range(1, 23) for x, m in MO[v] if m and re.search(r'V[a-zA-Z]w', m)] == [] and [(v, x) for v in range(1, 23) for x, m in MO[v] if m and re.search(r'V[a-zA-Z]v', m)] == [] and [(v, x) for v in range(1, 23) for x, m in MO[v] if m and '1c' in m] == []
assert [(v, x) for v in range(1, 23) for x, m in MO[v] if m and re.search(r'V[a-zA-Z]r', m)] == [(5, 'נתן'), (18, 'שפטים'), (18, 'ושטרים'), (18, 'נתן'), (20, 'נתן')]   # "judges and officers" participles; "gives" thrice
NEG = {v: sum(1 for x in W16(v) if x in ('לא', 'ולא')) for v in range(1, 23) if any(x in ('לא', 'ולא') for x in W16(v))}
assert NEG == {3: 1, 4: 2, 5: 1, 8: 1, 16: 1, 19: 3, 21: 1, 22: 1} and sum(NEG.values()) == 11 and [v for v in range(1, 23) if W16(v)[0] in ('כי', 'וכי', 'אם')] == [6] and W16(6)[:2] == ['כי', 'אם'] and [v for v in range(1, 23) if 'לאמר' in W16(v)] == [] and [v for v in range(1, 23) if 'למען' in W16(v)] == [3, 20], NEG
NAME_BARE = sum(1 for v in range(1, 23) for x in W16(v) if x == 'יהוה'); NAME_L = sum(1 for v in range(1, 23) for x in W16(v) if x == 'ליהוה')
YOURGOD = [v for v in range(1, 23) if any(a == 'יהוה' and b == 'אלהיך' for a, b in zip(W16(v), W16(v)[1:]))]; NONAME = [v for v in range(1, 23) if not any('יהוה' in x for x in W16(v))]
assert NAME_BARE == 17 and NAME_L == 5 and YOURGOD == [1, 5, 6, 7, 10, 11, 15, 16, 17, 18, 20, 21, 22] and NONAME == [3, 4, 9, 12, 13, 14, 19], (NAME_BARE, NAME_L, YOURGOD, NONAME)
with contextlib.redirect_stdout(io.StringIO()):
    import register_census as RC
    _ink = RC.read_ink()
assert [k for k in RC.receipts(_ink) if k[0] == 'Deut' and k[1] == 16] == [] and [x for x in RC.footers(_ink) if x[0][0] == 'Deut' and x[0][1] == 16] == [] and [x for x in RC.register_headers(_ink) if x[0][0] == 'Deut' and x[0][1] == 16] == [] and [k for k in RC.receipts(_ink) if k[0] == 'Deut' and k[1] <= 16] == [('Deut', 1, 3), ('Deut', 1, 19), ('Deut', 1, 41), ('Deut', 4, 5), ('Deut', 5, 12), ('Deut', 5, 16), ('Deut', 5, 32), ('Deut', 10, 5)] and ([k for k in RC.count_lines(_ink) if k[0] == 'Deut' and k[1] == 16] if hasattr(RC, 'count_lines') else []) == []
# ---- THE KIN BY COMPUTATION (the closest three re-scored in order) and THE TWINS DIFFED ----
assert KINC[1][0] == ('Exod 34:18', 4, 7) and KINC[1][1] == ('Exod 23:15', 3, 5) and KINC[3][:3] == [('Exod 12:15', 5, 5), ('Exod 23:15', 5, 6), ('Exod 34:18', 5, 6)] and KINC[8][:2] == [('Exod 35:2', 7, 6), ('Lev 23:3', 7, 5)] and KINC[9] == [] and KINC[22] == [] and KINC[11][:2] == [('Deut 12:18', 10, 13), ('Deut 16:14', 10, 11)] and KINC[14][0] == ('Deut 16:11', 10, 11) and KINC[16][:3] == [('2Chr 8:13', 8, 9), ('Exod 23:17', 5, 7), ('Exod 34:23', 5, 8)] and KINC[19][0] == ('Exod 23:8', 5, 7) and KINC[12][0] == ('Deut 24:18', 4, 6) and KINC[5][:2] == [('Deut 15:7', 3, 7), ('Deut 17:2', 3, 7)], (KINC[1], KINC[9], KINC[16])
D = lambda v: ('Deut', 16, v)
assert SHN(D(1), ('Exod', 34, 18)) == 7 and SHARED(D(1), ('Exod', 34, 18)) == ['כי', 'בחדש', 'האביב'] and SHN(D(1), ('Exod', 23, 15)) == 5 and SHN(D(1), ('Exod', 13, 4)) == 2 and SHARED(D(1), ('Exod', 13, 4)) == ['בחדש', 'האביב']
assert SHN(D(4), ('Exod', 13, 7)) == 6 and SHARED(D(4), ('Exod', 13, 7)) == ['ולא', 'יראה', 'לך', 'שאר', 'בכל', 'גבלך'] and SHN(D(4), ('Exod', 34, 25)) == 3 and SHARED(D(4), ('Exod', 34, 25)) == ['ולא', 'ילין']   # "no leaven seen in all your border" Exodus 13:7's six words; "shall not remain overnight" 34:25's Passover clause
assert SHN(D(6), ('Exod', 12, 6)) == 0 and SHN(D(6), ('Lev', 23, 5)) == 0 and SHN(D(6), ('Num', 9, 3)) == 0 and 'בין' not in W16(6) and W16(6)[14:19] == ['בערב', 'כבוא', 'השמש', 'מועד', 'צאתך']   # "between the evenings" NOWHERE in the chapter: "at evening, at the going down of the sun, the season of your going out"
assert SHN(D(7), ('Exod', 12, 8)) == 0 and SHN(D(7), ('Exod', 12, 9)) == 0 and W16(7)[0] == 'ובשלת' and words('Exod', 12, 9)[3:7] == ['נא', 'ובשל', 'מבשל', 'במים'] and words('2Chr', 35, 13)[:3] == ['ויבשלו', 'הפסח', 'באש']   # "you shall boil" against "nor boiled in water" — the Chronicler's "they boiled the Passover with fire"
assert SHN(D(8), ('Exod', 13, 6)) == 5 and DIFF(D(8), ('Exod', 13, 6))[:2] == [('replace', ['ששת'], ['שבעת']), ('replace', ['מצות'], ['מצת'])] and SHN(D(8), ('Exod', 12, 16)) == 3 and SHN(D(8), ('Lev', 23, 8)) == 3   # SIX days here against SEVEN there — the shelf's question
assert SHN(D(9), ('Lev', 23, 15)) == 0 and SHN(D(9), ('Lev', 23, 16)) == 0 and W16(9)[:2] == ['שבעה', 'שבעת'] and W16(9)[-2:] == ['שבעה', 'שבעות'] and W16(9)[4:7] == ['מהחל', 'חרמש', 'בקמה']   # the count from the sickle, not from "the morrow of the sabbath"; "seven weeks" said twice, spelled two ways
assert SHN(D(11), ('Deut', 12, 18)) == 13 and SHARED(D(11), ('Deut', 12, 18)) == ['אתה', 'ובנך', 'ובתך', 'ועבדך', 'ואמתך', 'והלוי', 'אשר', 'בשעריך'] and SHN(D(11), D(14)) == 11 and SHN(D(11), ('Deut', 12, 12)) == 4 and [x for x in W16(11) if x in ('אתה', 'ובנך', 'ובתך', 'ועבדך', 'ואמתך', 'והלוי', 'והגר', 'והיתום', 'והאלמנה')] == [x for x in W16(14) if x in ('אתה', 'ובנך', 'ובתך', 'ועבדך', 'ואמתך', 'והלוי', 'והגר', 'והיתום', 'והאלמנה')] == ['אתה', 'ובנך', 'ובתך', 'ועבדך', 'ואמתך', 'והלוי', 'והגר', 'והיתום', 'והאלמנה']   # THE HOUSEHOLD LIST — nine members, identical at 16:11 and 16:14; 12:18's six (no sojourner, fatherless, widow); 12:12's plural
assert SHN(D(12), ('Deut', 24, 18)) == 6 and SHARED(D(12), ('Deut', 24, 18)) == ['וזכרת', 'כי', 'עבד', 'היית', 'במצרים'] and SHN(D(12), ('Deut', 5, 15)) == 5 and SHN(D(12), ('Deut', 15, 15)) == 5 and SHN(D(12), ('Deut', 24, 22)) == 5   # "remember that you were a slave" — the book's five seats (5:15, 15:15, 16:12, 24:18, 24:22), 24:18 the closest
assert SHN(D(16), ('Exod', 34, 23)) == 8 and SHARED(D(16), ('Exod', 34, 23)) == ['פעמים', 'בשנה', 'יראה', 'כל', 'זכורך', 'את', 'פני'] and SHN(D(16), ('Exod', 23, 17)) == 7 and DIFF(D(16), ('Exod', 34, 23))[0] == ('replace', ['שלוש'], ['שלש']) and SHN(D(16), ('Exod', 23, 14)) == 1 and words('Exod', 23, 14)[:2] == ['שלש', 'רגלים']   # "three times" spelled full here, defective in Exodus; "three feet" (regalim) Exodus 23:14's word
assert SHN(D(17), ('Deut', 12, 15)) == 6 and SHARED(D(17), ('Deut', 12, 15)) == ['כברכת', 'יהוה', 'אלהיך', 'אשר', 'נתן', 'לך'] and W16(17)[:3] == ['איש', 'כמתנת', 'ידו']
assert SHN(D(18), ('Deut', 1, 16)) == 2 and SHN(D(18), ('Exod', 18, 21)) == 1 and SHN(D(18), ('Exod', 18, 25)) == 1 and W16(18)[:2] == ['שפטים', 'ושטרים'] and W16(18)[-2:] == ['משפט', 'צדק']   # the judges' appointment shares nothing in order with Jethro's or Horeb's — a new command
assert SHN(D(19), ('Exod', 23, 8)) == 7 and SHARED(D(19), ('Exod', 23, 8)) == ['כי', 'השחד', 'יעור'] and [x for x in W16(19) if x in ('חכמים', 'פקחים')] == ['חכמים'] and [x for x in words('Exod', 23, 8) if x in ('חכמים', 'פקחים')] == ['פקחים'] and ('replace', ['צדיקם'], ['צדיקים']) in DIFF(D(19), ('Exod', 23, 8)) and SHN(D(19), ('Exod', 23, 6)) == 3 and SHARED(D(19), ('Exod', 23, 6)) == ['לא', 'תטה', 'משפט'] and SHN(D(19), ('Deut', 24, 17)) == 4 and SHN(D(19), ('Deut', 1, 17)) == 3   # "the eyes of THE WISE" here, "the OPEN-EYED" in Exodus; "the righteous" spelled defective here
assert SHN(D(20), ('Deut', 4, 1)) == 6 and SHN(D(20), ('Deut', 8, 1)) == 5 and W16(20)[:3] == ['צדק', 'צדק', 'תרדף'] and SHN(D(21), ('Deut', 7, 5)) == 0 and SHN(D(21), ('Deut', 12, 3)) == 0 and SHN(D(21), ('Exod', 34, 13)) == 0 and SHN(D(22), ('Deut', 12, 31)) == 2 and SHARED(D(22), ('Deut', 12, 31)) == ['אשר', 'שנא'] and SHN(D(22), ('Lev', 26, 1)) == 1
# ---- THE FORMULAS OVER THE TORAH AND THE BIBLE (by consonants) ----
assert P('חדש', 'האביב', books=None) == ['Deut 16:1', 'Exod 23:15', 'Exod 34:18'] and P('לחם', 'עני', books=None) == ['Deut 16:3'] and P('כבוא', 'השמש', books=None) == ['Deut 16:6'] and P('ששת', 'ימים', 'תאכל', books=None) == ['Deut 16:8'] and P('שבעה', 'שבעת', books=None) == ['Deut 16:9'] and P('חג', 'שבעות', books=None) == ['Deut 16:10', 'Ezek 45:21'] and P('שלוש', 'פעמים', 'בשנה', books=None) == ['2Chr 8:13', 'Deut 16:16'] and P('יראה', 'כל', 'זכורך', books=None) == ['Deut 16:16', 'Exod 23:17', 'Exod 34:23'] and P('פני', 'יהוה', 'ריקם', books=None) == ['Deut 16:16']
assert P('שפטים', 'ושטרים', books=None) == ['Deut 16:18'] and P('בכל', 'שעריך', books=None) == ['Deut 12:15', 'Deut 16:18', 'Deut 28:52', 'Deut 28:55'] and P('לא', 'תטה', 'משפט', books=None) == ['Deut 16:19', 'Deut 24:17', 'Exod 23:6'] and P('צדק', 'צדק', books=None) == ['Deut 16:20'] and P('למען', 'תחיה', 'וירשת', books=None) == ['Deut 16:20'] and P('אשר', 'שנא', 'יהוה', books=None) == ['Deut 16:22'] and P('לא', 'תכיר', 'פנים', books=None) == ['Deut 16:19'] and P('לא', 'תכירו', 'פנים', books=None) == ['Deut 1:17'] and P('השחד', 'יעור', books=None) == ['Deut 16:19', 'Exod 23:8'] and U('שחד', 'השחד', 'ושחד', books=T) == ['Deut 10:17', 'Deut 16:19', 'Deut 27:25', 'Exod 23:8']
PLACE = P('במקום', 'אשר', 'יבחר', books=None); assert PLACE == ['Deut 12:14', 'Deut 12:18', 'Deut 14:23', 'Deut 15:20', 'Deut 16:11', 'Deut 16:15', 'Deut 16:16', 'Deut 16:2', 'Deut 16:7', 'Deut 23:17', 'Deut 31:11'] and [(v, i) for v in range(1, 23) for i, x in enumerate(W16(v)) if x in ('במקום', 'המקום') and W16(v)[i + 1] == 'אשר' and W16(v)[i + 2] == 'יבחר'] == [(2, 6), (6, 3), (7, 2), (11, 17), (15, 5), (16, 10)] and P('לשכן', 'שמו', 'שם', books=None) == ['Deut 12:11', 'Deut 14:23', 'Deut 16:11', 'Deut 16:2', 'Deut 16:6', 'Deut 26:2']   # THE PLACE six times in the chapter (16:2, 6, 7, 11, 15, 16), "to make His name dwell there" three of its six
PESACH = U('פסח', 'הפסח', books=T); assert len(PESACH) == 23 and 'Deut 15:21' in PESACH and 'Lev 21:18' in PESACH and [s for s in PESACH if s.startswith('Deut 16')] == ['Deut 16:1', 'Deut 16:2', 'Deut 16:5', 'Deut 16:6'] and len(U('פסח', 'הפסח', books=None)) == 53 and lemma_of('Deut', 16, 1, 'פסח') == ['6453'] and lemma_of('Deut', 15, 21, 'פסח') == ['6455']   # THE HOMOGRAPH: "lame" (15:21, Leviticus 21:18) sits in the Passover's consonantal census — told apart by lemma (13b's lesson)
assert hits('בחפזון') == ['Deut 16:3', 'Exod 12:11', 'Isa 52:12'] and hits('עצרת', T) == ['Deut 16:8', 'Lev 23:36', 'Num 29:35'] and hits('חרמש') == ['Deut 16:9', 'Deut 23:26'] and U('אשרה', 'אשריו', 'אשרים', books=T) == ['Deut 16:21', 'Exod 34:13'] and 'ואשריהם' in words('Deut', 12, 3) and 'ואשירהם' in words('Deut', 7, 5) and U('מצבה', 'מצבת', 'מצבתם', 'מצבתיהם', books=T) == ['Deut 12:3', 'Deut 16:22', 'Exod 23:24', 'Exod 24:4', 'Exod 34:13', 'Gen 28:18', 'Gen 28:22', 'Gen 31:13', 'Gen 31:45', 'Gen 35:14', 'Gen 35:20'] and 'ומצבה' in words('Lev', 26, 1)   # "in haste" three in the Bible (the exodus, here, Isaiah's "not in haste"); "solemn assembly" the Torah's three; the sickle's two; the asherah bare here and at Exodus 34:13 (7:5 and 12:3 carry suffixes); the pillar's Torah seats — Jacob's six, Sinai's, the ban's
assert U('ושמחת', 'ושמחתם', books=DT) == ['Deut 12:12', 'Deut 12:18', 'Deut 12:7', 'Deut 14:26', 'Deut 16:11', 'Deut 16:14', 'Deut 26:11', 'Deut 27:7'] and [(v, x) for v in range(1, 23) for x in W16(v) if x.startswith('ושמח') or x == 'שמח'] == [(11, 'ושמחת'), (14, 'ושמחת'), (15, 'שמח')] and W16(15)[-3:] == ['והיית', 'אך', 'שמח']
assert P('חג', 'הסכת', books=None) == ['Deut 16:13'] and P('חג', 'הסכות', books=None) == ['Ezra 3:4', 'Lev 23:34', 'Zech 14:16', 'Zech 14:18', 'Zech 14:19'] and P('ובחג', 'הסכות', books=None) == ['2Chr 8:13', 'Deut 16:16'] and P('חג', 'המצות', books=None) == ['2Chr 30:13', '2Chr 30:21', '2Chr 35:17', 'Exod 23:15', 'Exod 34:18', 'Lev 23:6'] and P('בחג', 'המצות', books=None) == ['2Chr 8:13', 'Deut 16:16']   # "the feast of booths" spelled DEFECTIVE at 16:13 alone in the Bible (הסכת), full at 16:16; 2 Chronicles 8:13 the one verse that names all three feasts with 16:16's words
SEVEN = P('שבעת', 'ימים', books=T); assert [s for s in SEVEN if s.startswith('Deut')] == ['Deut 16:13', 'Deut 16:15', 'Deut 16:3', 'Deut 16:4'] and len(SEVEN) == 53 and {v: [x for x in W16(v) if x in ('שבעת', 'שבעה', 'שבעות', 'השבעות', 'שבע')] for v in range(1, 23) if any(x in ('שבעת', 'שבעה', 'שבעות', 'השבעות', 'שבע') for x in W16(v))} == {3: ['שבעת'], 4: ['שבעת'], 9: ['שבעה', 'שבעת', 'שבעה', 'שבעות'], 10: ['שבעות'], 13: ['שבעת'], 15: ['שבעת'], 16: ['השבעות']}   # "seven days" the book's only four seats all in this chapter; SEVEN at nine seats in seven verses
assert [(v, x) for v in range(1, 23) for x in W16(v) if x in ('תזכר', 'וזכרת')] == [(3, 'תזכר'), (12, 'וזכרת')] and [(v, x) for v in range(1, 23) for x in W16(v) if 'מצרים' in x] == [(1, 'ממצרים'), (3, 'מצרים'), (3, 'מצרים'), (6, 'ממצרים'), (12, 'במצרים')] and [(v, x) for v in range(1, 23) for x in W16(v) if 'שעריך' in x] == [(5, 'שעריך'), (11, 'בשעריך'), (14, 'בשעריך'), (18, 'שעריך')] and U('ובשלת', 'ובשל', 'מבשל', 'תבשל', books=T) == ['Deut 14:21', 'Deut 16:7', 'Exod 12:9', 'Exod 23:19', 'Exod 29:31', 'Exod 34:26', 'Lev 6:21']
# ---- ONKELOS OVER THE BOOK (the plain Aramaic through NFKC; EXPORT verse numbers): the additions and the renderings ----
def ARM(c, v): return [plain(unicodedata.normalize('NFKC', x)).strip('.:') for x in clean(onk_he[c - 1][v - 1]).rstrip(':').split()]
def SEATS(sub): return [(c + 1, v + 1) for c in range(34) for v in range(len(onk_he[c])) if sub in ' '.join(ARM(c + 1, v + 1))]
assert SEATS('ועבד לך נסין') == [(16, 1)] and SEATS('נסין') == [(4, 34), (7, 19), (16, 1)] and ARM(16, 1)[-4:] == ['ועבד', 'לך', 'נסין', 'בליליא']   # THE ADDITION: "and He did miracles for you at night" — the night's clause supplied a subject; "miracles" the Aramaic's word at 4:34 and 7:19 (the Hebrew's signs and wonders)
assert SEATS('נכסת קודשיא') == [(16, 2)] and ARM(16, 2)[5:12] == ['מן', 'בני', 'ענא', 'ונכסת', 'קודשיא', 'מן', 'תורי'] and SEATS('שכנתיה') == [(4, 39), (6, 15), (7, 21), (12, 5), (12, 11), (12, 21), (14, 23), (14, 24), (16, 2), (16, 6), (16, 11), (23, 15), (26, 2), (32, 10), (33, 16), (33, 26)]   # ONKELOS WRITES THE LAW: "the Passover from the sons of the flock, and the holy slaughterings from the oxen" — the festival offering (chagigah) read out of "flock and herd"; the Shekhinah's sixteen seats, three in the chapter
assert SEATS('לית לך רשו') == [(12, 17), (16, 5), (17, 15), (22, 3)] and SEATS('עומרא דארמותא') == [(16, 9)] and ARM(16, 9)[4:9] == ['מדשריות', 'מגלא', 'בחצד', 'עומרא', 'דארמותא'] and SEATS('כנש')[0] == (16, 8) and len(SEATS('כנש')) == 10 and SEATS('דינין ופרענין') == [(16, 18)] and SEATS('פתגמין תריצין') == [(16, 19)] and ARM(16, 20)[:4] == ['קשטא', 'קשטא', 'תהי', 'רדיף']   # "you have no permission" for "you may not" at its four seats; THE OMER OF THE WAVING supplied at 16:9 (Leviticus 23:15's words in the Aramaic of a verse that names only the sickle); "judges and officers" rendered "judges and punishers"; "truth, truth you shall be pursuing"
assert SEATS('קרויך') == [(12, 15), (12, 17), (12, 18), (12, 21), (13, 13), (14, 21), (14, 27), (14, 28), (14, 29), (15, 7), (15, 22), (16, 5), (16, 11), (16, 14), (16, 18), (17, 2), (17, 8), (18, 6), (23, 17), (24, 14), (26, 12), (28, 52), (28, 55), (28, 57)][:24] or len(SEATS('קרויך')) == 25
assert len(SEATS('קרויך')) == 25 and [s for s in SEATS('קרויך') if s[0] == 16] == [(16, 5), (16, 11), (16, 14), (16, 18)] and SEATS('אשרת') == [(16, 21)] and SEATS('חמיר') == [(16, 4)] and SEATS('כמעל שמשא') == [(16, 6), (23, 12), (24, 13)] and SEATS('מטליא') == [(16, 13), (16, 16), (31, 10)] and SEATS('ריקנון') == [(16, 16)] and (16, 22) in SEATS('קמא') and not any('מימר' in ' '.join(ARM(16, v)) for v in range(1, 23))   # "your cities" for "your gates" at the chapter's four; the huts at the three feasts of booths in the book; NO MEMRA in the chapter (chapter 15 had three)
FAIL_ALL = list(FAIL)
print('THE INK OF CHAPTER 16 (LEAN) — every assert above passed; the cuts\' misses:', FAIL_ALL)

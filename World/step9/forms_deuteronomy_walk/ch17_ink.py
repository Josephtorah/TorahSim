import os as _os
_ROOT = _os.path.normpath(_os.path.join(_os.path.dirname(_os.path.abspath(__file__)), '..', '..', '..'))   # THE PORTABLE REPO (2026-09-15): the repo root from this file's own place
#!/usr/bin/env python3
# THE DEUTERONOMY WALK, sitting 15 — CHAPTERS 17-18, Deuteronomy 17:1-18:22 IN THE LEAN FORM (2026-09-24; the owner: "Reread and go" after the compaction at
# #210 — THE LEAN PASS's third sitting, the first on TWO chapters: ONE reading window (the ink, the shelf, the ledger, the freeze), one compile window, a short
# tail): THE INK of the two chapters, computed from the Tanakh DB, the snapshot store and the shelf's own bytes — never typed. Sitting 14's form (ch16_ink.py):
# the generic helpers copied by derive_ch17_ink.py from the forms' ch16_ink.py by content markers (the chapter substituted for the pair), the constants and
# every assert the two chapters' own, typed FROM THE PRINTS (ch17_dump0.out, ch18_dump0.out, ch17_measure_lean.out). THE TWO DIVISIONS AGREE in both chapters
# (20 = 20, cost 20; 22 = 22, cost 14) — the identity. THE SPINE IS ON THE TWO CHAPTERS — THIRTY-TWO piskaot 147-178 with 181 rows (106 + 75): sixteen heads
# computed in chapter 17 (147 on 17:1 … 162 on 17:20) and sixteen in chapter 18 (163 on 18:1 … 178 on 18:20), ALL IN VERSE ORDER, NO HEADLESS PISKA; 146 on
# 16:22 before, 179 on 19:1 after; no tail folded in either way (162's rows stop before 18:1's words, 178's before 19:1's; 163:1 and 179:1 open with their
# verses' citations). ELEVEN rows elsewhere cite the two chapters by the union of both files (six READ BEFORE at chapters 11-14, REREAD WHOLE; five fresh),
# NONE excluded. NO portion edge inside either chapter (Shoftim 16:18-21:9 holds both whole; the chapters the units, CHAPTER NUMBERS). The parser MEASURED on
# every verse — TWO NUMBER VERSES (17:2 [1] "one of your gates", 17:6 [2, 3, 1] "two witnesses or three … one witness"), no ordinal, no starred token, and
# 18:6's "from one of your gates" NOT read (the number word behind its prefix). THE STORE = THE DB at every verse (368 = 368; 304 = 304); ONE "?" gloss (18:19
# "I"). The hand's facts as asserts, run all at once by assert_driver.py.
import json, os, re, html, sqlite3, sys, io, contextlib, unicodedata, subprocess
from collections import Counter
ROOT = _ROOT
sys.path.insert(0, f'{ROOT}/World/step9')
DATE = '2026-09-24'
CHS = (17, 18)
UIDS = ['deu_17_courts_king', 'deu_18_levi_prophet']
SPANS = {'deu_17_courts_king': (17, 1, 20), 'deu_18_levi_prophet': (18, 1, 22)}
PREFIX = {'deu_17_courts_king': 'DV17', 'deu_18_levi_prophet': 'DV18'}
SPAN = [(17, v) for v in range(1, 21)] + [(18, v) for v in range(1, 23)]
PISKAOT = list(range(147, 179))   # THE SPINE ON THE TWO CHAPTERS: 147-162 chapter 17's sixteen heads, 163-178 chapter 18's sixteen (the A prints); 146 heads on 16:22, 179 on 19:1
PISKAOT_BY = {17: list(range(147, 163)), 18: list(range(163, 179))}
HEADLESS = []   # every piska of the span heads on its verse in the Hebrew (the dumps' prints)
SPINE_ROWS = {147: 7, 148: 10, 149: 7, 150: 3, 151: 3, 152: 15, 153: 5, 154: 5, 155: 9, 156: 6, 157: 10, 158: 4, 159: 4, 160: 8, 161: 5, 162: 5, 163: 4, 164: 3, 165: 14, 166: 9, 167: 2, 168: 4, 169: 3, 170: 3, 171: 11, 172: 5, 173: 4, 174: 2, 175: 2, 176: 5, 177: 1, 178: 3}   # rows per piska, both files (the I prints and the splitter's) — 106 + 75 = 181
PREV_CHAPTER_ROWS = []   # no tail folded in (146's row chapter 16's — asserted there; 162's rows stop before 18:1's words, 178's before 19:1's)
READ_ROWS = [(p, r) for p in PISKAOT for r in range(1, SPINE_ROWS[p] + 1)]   # 181 — this ledger's spine rows
EXP2DB = {17: {e: [e] for e in range(1, 21)}, 18: {e: [e] for e in range(1, 23)}}   # the identity in both chapters (chapter 5 the book's one split)
DB2EXP = {c: {d: e for e, ds in EXP2DB[c].items() for d in ds} for c in CHS}
# the Hebrew's book-named citations of the two chapters OUTSIDE the spine (the regex reads "(דברים יז ח)" etc.); three rows cite only in the English (190:3, 261:2, 71:9)
OUTSIDE_HE = [(37, 16, (17, 8)), (93, 6, (17, 4)), (99, 2, (17, 1)), (190, 7, (17, 4)), (306, 9, (17, 7)), (317, 2, (17, 8)), (352, 9, (17, 8)), (208, 1, (18, 7))]
OUTSIDE = [(37, 16), (71, 9), (93, 6), (99, 2), (190, 3), (190, 7), (208, 1), (261, 2), (306, 9), (317, 2), (352, 9)]   # the ELEVEN rows READ WHOLE: the union of both files beyond piskaot 147-178, joined over the two dumps
EXCLUDED = []   # every outside citation genuine
INTERPOLATION = []
CITED = {(37, 16): [(17, 8)], (71, 9): [(18, 3)], (93, 6): [(17, 4)], (99, 2): [(17, 1)], (190, 3): [(17, 6)], (190, 7): [(17, 4)], (208, 1): [(18, 7)], (261, 2): [(17, 1)], (306, 9): [(17, 7)], (317, 2): [(17, 8)], (352, 9): [(17, 8)]}
PRIOR_READ = {(37, 16): ['deu_11_ekev_reeh_2026-09-20.md'], (71, 9): ['deu_12_reeh_2026-09-20.md'], (93, 6): ['deu_13_reeh_2026-09-21.md'], (99, 2): ['deu_14_reeh_2026-09-21.md'], (190, 7): ['deu_13_reeh_2026-09-21.md'], (306, 9): ['deu_11_ekev_reeh_2026-09-20.md']}   # the six outside rows read before (computed from the ledgers, asserted) — REREAD WHOLE here
HEADS_ON = {37: (11, 10), 71: (12, 15), 93: (13, 14), 99: (14, 3), 190: (19, 17), 208: (21, 5), 261: (23, 19), 306: (32, 1), 317: (32, 14), 352: (33, 11)}
FRESH = [(190, 3), (208, 1), (261, 2), (317, 2), (352, 9)]
CREDITED = {}   # under THE WHOLE-ROW RULE no spine row is credited: the seven rows read before (148:8 at chapter 4; 147:2 at chapters 12 and 16; 149:1-2 at chapter 13; 147:3-4 at chapter 15; 171:6 at Genesis 31) are REREAD WHOLE here and marked so
TITLE = "Chapters 17-18 — You shall not sacrifice to the LORD your God an ox or a sheep with a blemish, any evil thing, for it is an abomination to Him. When a man or a woman in one of your gates does what is evil in His eyes, transgressing His covenant — going and serving other gods, the sun or the moon or the host of heaven, which I have not commanded — and it is told you and you inquire well and the thing is true, bring them out to your gates and stone them; by the mouth of two witnesses or three shall the dead die, never by one; the witnesses' hand first and all the people's after, and you shall purge the evil from your midst. When a matter is too hard for you in judgment, between blood and blood, plea and plea, stroke and stroke, rise and go up to the place the LORD will choose, to the priests the Levites and the judge of those days; do according to the sentence they declare from that place, the law they teach and the judgment they say; turn not from their word right or left; the man who acts presumptuously, not hearkening to the priest who stands to minister there or to the judge, shall die — all the people shall hear and fear. When you come into the land and say 'I will set a king over me like all the nations', set the king the LORD chooses, from among your brothers, never a foreigner; he shall not multiply horses nor return the people to Egypt for horses, since the LORD said you shall not go back that way; nor multiply wives, lest his heart turn; nor silver and gold; when he sits on his throne he shall write himself a copy of this law before the priests the Levites, keep it with him and read it all his days, to learn to fear the LORD and keep all these words, his heart not lifted above his brothers, that he and his sons may reign long. The priests the Levites, all the tribe of Levi, have no portion or inheritance with Israel — the fire offerings of the LORD and His inheritance they eat, the LORD is their inheritance as He spoke; the priests' due from the people who sacrifice, ox or sheep: the shoulder, the two cheeks and the maw; the first of your grain, wine and oil and the first of the fleece — for the LORD chose him of all the tribes to stand and minister in His name, he and his sons forever. The Levite who comes from any of your gates with all his soul's desire to the place shall minister in the LORD's name like all his brothers who stand there, and eat portion as portion, besides what comes of the fathers' houses. When you come into the land, learn not the abominations of the nations: none among you who passes his son or daughter through the fire, a diviner, a soothsayer, an augur, a sorcerer, a charmer, one who consults a ghost or a familiar spirit, or a necromancer — for these abominations the LORD drives them out before you; be whole with the LORD your God, who has not given you such. A prophet from your midst, of your brothers, like me, the LORD will raise up for you — hear him — as you asked at Horeb on the day of the assembly: 'let me not hear the voice of the LORD again nor see this great fire, lest I die'; and the LORD said they had spoken well: 'a prophet like you I will raise up from their brothers, I will put My words in his mouth, and he shall speak all I command him; whoever hearkens not to My words spoken in My name, I will require it of him; but the prophet who presumes to speak in My name what I commanded him not, or who speaks in the name of other gods, shall die'. And if you say in your heart, how shall we know the word the LORD has not spoken — what the prophet speaks in the LORD's name and it does not come to pass, that is the word the LORD has not spoken; the prophet spoke it presumptuously; you shall not fear him"
OUT = f'{ROOT}/logic/oral_triage/deu_17_18_shoftim_{DATE}.md'
PATCHED = bool(os.environ.get('DEU17_PATCHED'))   # the tail's flag: after the manifest and the seat, the drafts carry operators and the store its overrides
db = sqlite3.connect(f'file:{ROOT}/Data/tanakh.sqlite?mode=ro', uri=True)
VC = dict(db.execute("SELECT chapter, COUNT(*) FROM verses WHERE book='Deut' GROUP BY chapter").fetchall())
NV = {c: VC[c] for c in CHS}
# ---- THE HELPERS (ch16_ink.py's, copied by content markers) ----
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
# ---- THE INK'S HELPERS, THE DB AND THE STORE (ch16_ink.py's, the pair of chapters substituted) ----
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
def W17(v): return words('Deut', 17, v)
def W18(v): return words('Deut', 18, v)
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
for c, v, idx, hp, g in store.execute("SELECT v.chapter, v.verse, w.idx, w.he_plain, w.gloss FROM words w JOIN verses v ON w.verse_id=v.id WHERE v.book='Deut' AND v.chapter IN (17, 18) ORDER BY v.id, w.idx"):
    SG.setdefault((c, v), []).append((idx, hp.replace('/', ''), g))
def sg(c, v, tok, nth=0):
    hit = [g for _, hp, g in SG[(c, v)] if hp == tok]
    if len(hit) <= nth: raise KeyError((c, v, tok, nth))
    return hit[nth]
def sidx(c, v, tok, nth=0):
    hit = [i for i, hp, _ in SG[(c, v)] if hp == tok]
    assert len(hit) > nth, (c, v, tok, nth, hit)
    return hit[nth]
STORE_MISMATCH = [(c, v, n, len(by[('Deut', c, v)])) for c, v, n in store.execute("SELECT v.chapter, v.verse, COUNT(*) FROM words w JOIN verses v ON w.verse_id=v.id WHERE v.book='Deut' AND v.chapter IN (17, 18) GROUP BY v.chapter, v.verse").fetchall() if n != len(by[('Deut', c, v)])]
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
DT = ('Deut',)
# ---- THE SHELF BY POSITION — the spine ON the two chapters: thirty-two piskaot 147-178 (sixteen heads in chapter 17 and sixteen in chapter 18, ALL IN VERSE ORDER, none headless); 146 heads on 16:22 before, 179 on 19:1 after; no tail folded in either way; the two files' grains ----
assert NV == {17: 20, 18: 22} and VC[16] == 22 and len(sif) == 357 and len(sif_he) == 357 and sum(len(s) for s in sif) == 2357 and sum(len(s) for s in sif_he) == 2357
HC = Counter(h[0] for h in heads.values() if h)
assert [p for p, h in heads.items() if h and h[0] == 17] == list(range(147, 163)) and [p for p, h in heads.items() if h and h[0] == 18] == list(range(163, 179)) and HC[17] == 16 and HC[18] == 16 and sorted(HC.items())[:18] == [(1, 24), (3, 4), (6, 6), (11, 21), (12, 20), (13, 14), (14, 14), (15, 16), (16, 19), (17, 16), (18, 16), (19, 10), (20, 14), (21, 17), (22, 22), (23, 22), (24, 16), (25, 10)], sorted(HC.items())[:18]
assert {p: heads[p] for p in range(146, 180)} == {146: (16, 22), 147: (17, 1), 148: (17, 2), 149: (17, 4), 150: (17, 6), 151: (17, 7), 152: (17, 8), 153: (17, 9), 154: (17, 10), 155: (17, 12), 156: (17, 14), 157: (17, 15), 158: (17, 16), 159: (17, 17), 160: (17, 18), 161: (17, 19), 162: (17, 20), 163: (18, 1), 164: (18, 2), 165: (18, 3), 166: (18, 4), 167: (18, 5), 168: (18, 6), 169: (18, 7), 170: (18, 9), 171: (18, 10), 172: (18, 11), 173: (18, 12), 174: (18, 14), 175: (18, 15), 176: (18, 16), 177: (18, 19), 178: (18, 20), 179: (19, 1)}, {p: heads[p] for p in range(146, 180)}
HV = {c: [heads[p][1] for p in PISKAOT_BY[c]] for c in CHS}
assert HV[17] == [1, 2, 4, 6, 7, 8, 9, 10, 12, 14, 15, 16, 17, 18, 19, 20] and HV[18] == [1, 2, 3, 4, 5, 6, 7, 9, 10, 11, 12, 14, 15, 16, 19, 20] and all(HV[c] == sorted(HV[c]) for c in CHS), HV   # THE HEADS IN VERSE ORDER in both chapters
NOHEAD = {c: [v for v in range(1, NV[c] + 1) if v not in HV[c]] for c in CHS}
assert NOHEAD == {17: [3, 5, 11, 13], 18: [8, 13, 17, 18, 21, 22]}, NOHEAD   # ten verses carry no head: 17:3 and 17:5 inside 148-149, 17:11 inside 154, 17:13 inside 155; 18:8 inside 169, 18:13 inside 173, 18:17-18 inside 176, 18:21-22 inside 178
assert {p: (len(sif_he[p - 1]), len(sif[p - 1])) for p in PISKAOT} == {p: (n, n) for p, n in SPINE_ROWS.items()} and sum(SPINE_ROWS[p] for p in PISKAOT_BY[17]) == 106 and sum(SPINE_ROWS[p] for p in PISKAOT_BY[18]) == 75 and sum(SPINE_ROWS.values()) == 181 and len(READ_ROWS) == 181 and len(PISKAOT) == 32 and READ_ROWS[:2] == [(147, 1), (147, 2)] and READ_ROWS[-1] == (178, 3) and HEADLESS == []
# NO TAIL FOLDED IN: 146's row stops before 17:1's words (chapter 16's own check); 162's rows carry no word of 18:1, 178's none of 19:1; 147:1, 163:1 and 179:1 open with their verses' citations
assert HB0(147, 1).startswith('(דברים יז א) לא תזבח') and HB0(163, 1).startswith('(דברים יח א) לא יהיה לכהנים') and HB0(179, 1).startswith('(דברים יט א) כי יכרית') and not any(w in HB0(162, r) for r in range(1, 6) for w in ('לא יהיה לכהנים', 'כל שבט לוי חלק')) and not any(w in HB0(178, r) for r in range(1, 4) for w in ('כי יכרית', 'יכרית יהוה')) and 'לא תזבח' not in HB0(146, 1) and he_cites(Hb(147, 1)) == [('דברים', 17, 1)] and he_cites(Hb(163, 1)) == [('דברים', 18, 1), ('דברים', 18, 7)]
CIT_HE = {c: [(p, r, (c, x[2])) for p in range(1, 358) for r in range(1, len(sif_he[p - 1]) + 1) for x in he_cites(Hb(p, r)) if x[0] == 'דברים' and x[1] == c] for c in CHS}
CIT_EN = {c: [(p, r, (c, int(m.group(2)))) for p in range(1, 358) for r in range(1, len(sif[p - 1]) + 1) for m in re.finditer(r'\((?:Deut(?:eronomy)?\.?|Dt\.?|Devarim) ?(%d):(\d+)' % c, E(p, r))] for c in CHS}
assert {c: len(CIT_HE[c]) for c in CHS} == {17: 32, 18: 26} and {c: len(CIT_EN[c]) for c in CHS} == {17: 136, 18: 96}, ({c: len(CIT_HE[c]) for c in CHS}, {c: len(CIT_EN[c]) for c in CHS})
assert sorted((p, r, v) for c in CHS for p, r, v in CIT_HE[c] if p not in PISKAOT) == sorted(OUTSIDE_HE), sorted((p, r, v) for c in CHS for p, r, v in CIT_HE[c] if p not in PISKAOT)
UNION = {c: sorted({(p, r) for p, r, _ in CIT_HE[c]} | {(p, r) for p, r, _ in CIT_EN[c]}) for c in CHS}
assert {c: len(UNION[c]) for c in CHS} == {17: 102, 18: 67} and [(p, r) for p, r in UNION[17] if p not in PISKAOT] == [(37, 16), (93, 6), (99, 2), (190, 3), (190, 7), (261, 2), (306, 9), (317, 2), (352, 9)] and [(p, r) for p, r in UNION[18] if p not in PISKAOT] == [(71, 9), (208, 1)] and not set(UNION[17]) & set(UNION[18]), ({c: len(UNION[c]) for c in CHS})
UNION_ALL = sorted(set(UNION[17]) | set(UNION[18]))
assert len(UNION_ALL) == 169 and [(p, r) for p, r in UNION_ALL if p not in PISKAOT] == OUTSIDE and len(OUTSIDE) == 11 and len([(p, r) for p, r in UNION_ALL if p in PISKAOT]) == 158, len(UNION_ALL)
assert all(1 <= v <= NV[c] for c in CHS for _, _, (_, v) in CIT_HE[c] + CIT_EN[c])   # no cited verse beyond either chapter's count
assert [(p, r) for c in CHS for p in range(1, 358) for r in range(1, len(sif[p - 1]) + 1) if re.search(r'\((?:Ibid|ibid)\.? ?%d:\d+\)' % c, E(p, r))] == []   # no "ibid."
assert {p: heads[p] for p, _ in OUTSIDE} == HEADS_ON, {p: heads[p] for p, _ in OUTSIDE}
assert all(has_points(Hb(p, r)) for p, r in OUTSIDE) and all(has_points(Hb(p, r)) for p, r in READ_ROWS)
NOCITE = [(p, r) for p in PISKAOT for r in range(1, SPINE_ROWS[p] + 1) if not he_cites(Hb(p, r)) and not re.findall(r'\([A-Z][a-z]+\.? ?\d+:\d+', E(p, r))]
assert NOCITE == [(152, 13), (155, 2), (158, 4), (159, 2), (161, 4), (161, 5), (165, 7), (165, 8), (171, 8), (171, 10), (171, 11), (172, 4)] and len(NOCITE) == 12, NOCITE
# THE MISHNAH CITED IN THE HEBREW ITSELF — the Hebrew's own bracketed tractate citations inside the spine: 152:13 (Sanhedrin 11:2 the three courts), 157:10 (Sotah 7:8 Agrippas), 161:1 and 161:4 (Sanhedrin 2:4 the king's copy, the king's road), 165:5 (Chullin 10:4 the proselyte's cow), 166:5-6 (Chullin 11:2 the fleece), 169:1 (Zevachim 2:1 the floor), 169:2 (Sukkah 5:7 the watches), 172:2 (Sanhedrin 7:7 the medium)
MISHNAH_HE = [(p, r, m) for p in PISKAOT for r in range(1, SPINE_ROWS[p] + 1) for m in re.findall(r'\((סנהדרין|סוטה|חולין|זבחים|סוכה)[^)]*\)', Hb(p, r))]
assert [(p, r) for p, r, _ in MISHNAH_HE] == [(152, 13), (157, 10), (161, 1), (161, 4), (165, 5), (166, 5), (169, 1), (169, 2), (172, 2)] and [m for _, _, m in MISHNAH_HE] == ['סנהדרין', 'סוטה', 'סנהדרין', 'סנהדרין', 'חולין', 'חולין', 'זבחים', 'סוכה', 'סנהדרין'] and '(שם)' in HB0(166, 6) and '(שם)' not in ''.join(HB0(p, r) for p in PISKAOT for r in range(1, SPINE_ROWS[p] + 1) if (p, r) != (166, 6)), MISHNAH_HE   # NINE by name (the first pass typed ten): 166:6 cites Chullin 11:2 as "(ibid.)" — the spine's ONE Hebrew "ibid.", retyped from the print
# THE OUTSIDE ROWS' own openings and citations (the consonants)
assert HB0(37, 16).startswith('מה צבי זה קל לאכל') and HB0(71, 9).startswith('יכול יהו חיבים במתנות') and HB0(93, 6).startswith('(דברים יג טו) ודרשת וחקרת') and HB0(99, 2).startswith('אחרים אומרים') and HB0(190, 3).startswith('יכול אף אשה תהא כשרה לעדות') and HB0(190, 7).startswith('(דברים יט יח) ודרשו השפטים היטב') and HB0(208, 1).startswith('(דברים כא ה) ונגשו הכהנים בני לוי') and HB0(261, 2).startswith('ומחיר כלב') and HB0(306, 9).startswith('דבר אחר האזינו השמים') and HB0(317, 2).startswith('דבר אחר: ירכיבהו על במתי ארץ') and HB0(352, 9).startswith('דבר אחר ובין כתפיו שכן')
CIT_OUT = {(p, r): sorted({(c, v) for cc in CHS for q, s, (c, v) in CIT_HE[cc] + CIT_EN[cc] if (q, s) == (p, r)}) for p, r in OUTSIDE}
assert CIT_OUT == CITED, CIT_OUT
# ---- THE PRIOR READS (computed from the ledgers): seven spine rows (148:8 at chapter 4; 147:2 at chapters 12 and 16; 149:1-2 at chapter 13; 147:3-4 at chapter 15; 171:6 at Genesis 31 — the covenant between the pieces), six outside rows at chapters 11-14; NEVER READ AHEAD ----
TRI = f'{ROOT}/logic/oral_triage'
LED = {f: open(f'{TRI}/{f}', encoding='utf-8').read() for f in os.listdir(TRI) if f.endswith('.md') and os.path.isfile(f'{TRI}/{f}') and f != os.path.basename(OUT)}   # this sitting's own ledger is not a prior read (sitting 14's lesson 3)
SPINE_PRIOR = sorted({(f, int(a), int(b)) for f, t in LED.items() for a, b in re.findall(r'Sifrei Devarim (\d+):(\d+)', t) if int(a) in PISKAOT})
OUT_PRIOR = sorted({(f, int(a), int(b)) for f, t in LED.items() for a, b in re.findall(r'Sifrei Devarim (\d+):(\d+)', t) if (int(a), int(b)) in OUTSIDE})
assert SPINE_PRIOR == [('deu_04_vaetchanan_2026-09-16.md', 148, 8), ('deu_12_reeh_2026-09-20.md', 147, 2), ('deu_13_reeh_2026-09-21.md', 149, 1), ('deu_13_reeh_2026-09-21.md', 149, 2), ('deu_15_reeh_2026-09-22.md', 147, 3), ('deu_15_reeh_2026-09-22.md', 147, 4), ('deu_16_reeh_shoftim_2026-09-23.md', 147, 2), ('gen_31_covenant_pieces_2026-08-25.md', 171, 6)], SPINE_PRIOR
assert OUT_PRIOR == [('deu_11_ekev_reeh_2026-09-20.md', 37, 16), ('deu_11_ekev_reeh_2026-09-20.md', 306, 9), ('deu_12_reeh_2026-09-20.md', 71, 9), ('deu_13_reeh_2026-09-21.md', 93, 6), ('deu_13_reeh_2026-09-21.md', 190, 7), ('deu_14_reeh_2026-09-21.md', 99, 2)] and {(p, r): [f] for f, p, r in OUT_PRIOR} == PRIOR_READ and sorted(FRESH) == sorted(k for k in OUTSIDE if k not in PRIOR_READ), OUT_PRIOR
assert sorted(f for f, t in LED.items() if re.search(r'^- Onkelos (?:Deut (?:1[7-9]|2\d|3\d)|Josh|Judg|1Sam|2Sam|1Kgs|2Kgs|Isa|Jer|Ezek):', t, re.M)) == [] and sorted(f for f, t in LED.items() if re.search(r'^- Onkelos Exod (?:18|20):', t, re.M)) == []   # never read ahead; Jethro's judges and the Decalogue's request read through their spines in the law era
KINL = [(f, kinrows(f, pat)) for f, pat in [('deu_01_03_devarim_2026-09-15.md', r'Deut 1:'), ('deu_04_vaetchanan_2026-09-16.md', r'Deut 4:'), ('deu_05_vaetchanan_2026-09-16.md', r'Deut 5:'), ('deu_10_ekev_2026-09-19.md', r'Deut 10:'), ('deu_12_reeh_2026-09-20.md', r'Deut 12:'), ('deu_13_reeh_2026-09-21.md', r'Deut 13:'), ('deu_14_reeh_2026-09-21.md', r'Deut 14:'), ('deu_15_reeh_2026-09-22.md', r'Deut 15:'), ('lev_22_holy_food_offerings_2026-09-05.md', r'Lev 22:'), ('num_35_refuge_cities_2026-09-13.md', r'Num 35:'), ('num_18_priest_levite_dues_2026-09-10.md', r'Num 18:'), ('lev_07_fat_blood_dues_2026-09-03.md', r'Lev 7:'), ('lev_07_shelamim_types_2026-09-03.md', r'Lev 7:'), ('lev_07_asham_procedure_2026-09-03.md', r'Lev 7:'), ('lev_19_kedoshim_2026-09-05.md', r'Lev 19:'), ('lev_20_sanctions_2026-09-05.md', r'Lev 20:'), ('exo_22_property_social_2026-09-01.md', r'Exod 22:'), ('num_22_balak_bilam_call_2026-09-11.md', r'Num 22:'), ('num_23_oracles_1_2_2026-09-11.md', r'Num 23:')]]
assert KINL == [('deu_01_03_devarim_2026-09-15.md', 46), ('deu_04_vaetchanan_2026-09-16.md', 49), ('deu_05_vaetchanan_2026-09-16.md', 33), ('deu_10_ekev_2026-09-19.md', 22), ('deu_12_reeh_2026-09-20.md', 31), ('deu_13_reeh_2026-09-21.md', 19), ('deu_14_reeh_2026-09-21.md', 29), ('deu_15_reeh_2026-09-22.md', 23), ('lev_22_holy_food_offerings_2026-09-05.md', 33), ('num_35_refuge_cities_2026-09-13.md', 34), ('num_18_priest_levite_dues_2026-09-10.md', 32), ('lev_07_fat_blood_dues_2026-09-03.md', 6), ('lev_07_shelamim_types_2026-09-03.md', 6), ('lev_07_asham_procedure_2026-09-03.md', 4), ('lev_19_kedoshim_2026-09-05.md', 37), ('lev_20_sanctions_2026-09-05.md', 27), ('exo_22_property_social_2026-09-01.md', 6), ('num_22_balak_bilam_call_2026-09-11.md', 41), ('num_23_oracles_1_2_2026-09-11.md', 30)], KINL
NAMING = {c: sorted(f for f, t in LED.items() if re.search(r'Deut(?:eronomy)? %d:\d+' % c, t)) for c in CHS}
assert {c: len(NAMING[c]) for c in CHS} == {17: 18, 18: 15} and not any(re.search(r'^- Onkelos Deut (?:17|18):', LED[f], re.M) for c in CHS for f in NAMING[c]), {c: len(NAMING[c]) for c in CHS}
# ---- THE STORE, THE PARSER, THE FRAMES (computed on the DB, the snapshot store and the engine) ----
assert STORE_MISMATCH == [] and {c: sum(len(W(c, v)) for v in range(1, NV[c] + 1)) for c in CHS} == {17: 368, 18: 304} and {c: len({g for (cc, v) in SG if cc == c for _, _, g in SG[(cc, v)]}) for c in CHS} == {17: 192, 18: 178} and [(c, v, hp) for (c, v) in SG for _, hp, g in SG[(c, v)] if g == '?'] == [(18, 19, 'אנכי')]   # ONE "?" gloss in the store — 18:19's "I" (the display patch's first row)
with contextlib.redirect_stdout(io.StringIO()):
    import cold_run_sequence as CS
PARSE = {}
for _c, _v in SPAN:
    _vw = CS.verse_words('Deut', _c, _v); _n, _o = CS.ink_numbers(_vw), CS.ink_ordinals(_vw); _mk = [t for t in _vw if t[-1] in '#~^%@|*']
    if _n or _o or _mk: PARSE[(_c, _v)] = (_n, _o, _mk)
assert PARSE == {(17, 2): ([1], [], []), (17, 6): ([2, 3, 1], [], [])}, PARSE   # TWO NUMBER VERSES, no ordinal, no starred token
assert CS.verse_words('Deut', 18, 6)[3] == 'מאחד' and CS.ink_numbers(CS.verse_words('Deut', 18, 6)) == [] and CS.verse_words('Deut', 17, 2)[3] == 'באחד'   # 18:6's "from one of your gates" NOT read as a number — the number word behind its "from" prefix; 17:2's "in one" read [1]
NUMV = {(c, v): [x for x in W(c, v) if x in ('אחד', 'שנים', 'שלשה') or x[1:] in ('אחד',)] for c, v in SPAN if any(x in ('אחד', 'שנים', 'שלשה') or x[1:] in ('אחד',) for x in W(c, v))}
assert NUMV == {(17, 2): ['באחד'], (17, 6): ['שנים', 'שלשה', 'אחד'], (18, 6): ['מאחד']}, NUMV
MO = {(c, v): [(x, m) for x, m in by[('Deut', c, v)]] for c, v in SPAN}
P2 = {(c, v): (sum(1 for _, m in MO[(c, v)] if m and '2mp' in m), sum(1 for _, m in MO[(c, v)] if m and '2ms' in m)) for c, v in SPAN}
assert [k for k, (mp, _) in P2.items() if mp] == [(17, 16), (18, 15)] and P2[(17, 16)] == (2, 0) and P2[(18, 15)] == (1, 4) and sum(ms for (c, _), (_, ms) in P2.items() if c == 17) == 48 and sum(ms for (c, _), (_, ms) in P2.items() if c == 18) == 30, P2   # THE PLURAL TWICE: 17:16 "the LORD said TO YOU (pl): you shall not go back" (the Exodus's word quoted); 18:15 "to him YOU (pl) shall hearken" — the rest singular
assert [(c, v, x) for c, v in SPAN for x, m in MO[(c, v)] if m and re.search(r'V[a-zA-Z]a$', m)] == [(17, 4, 'היטב'), (17, 15, 'שום')] and [(c, v, x) for c, v in SPAN for x, m in MO[(c, v)] if m and re.search(r'V[a-zA-Z]w', m)] == [(17, 3, 'וילך'), (17, 3, 'ויעבד'), (17, 3, 'וישתחו'), (18, 17, 'ויאמר')] and [(c, v, x) for c, v in SPAN for x, m in MO[(c, v)] if m and re.search(r'V[a-zA-Z]v', m)] == []   # two infinitive absolutes ("well", "set, you shall set"); the narrative form inside 17:3's case and at 18:17's one divine frame; no imperative
FIRST = [(c, v, x) for c, v in SPAN for x, m in MO[(c, v)] if m and '1c' in m and m.startswith('HV')]
assert FIRST == [(17, 3, 'צויתי'), (17, 14, 'אשימה'), (18, 16, 'אסף'), (18, 16, 'אראה'), (18, 16, 'אמות'), (18, 18, 'אקים'), (18, 18, 'אצונו'), (18, 19, 'אדרש'), (18, 20, 'צויתיו'), (18, 21, 'נדע')], FIRST   # THE FIRST PERSON TEN TIMES: the LORD's "I have not commanded" inside 17:3, the people's "I will set" at 17:14 and "let me not hear" at 18:16, the LORD's own five at 18:18-20, the people's "we" at 18:21
assert len([(c, v, x) for c, v in SPAN for x, m in MO[(c, v)] if m and re.search(r'V[a-zA-Z]r', m)]) == 26 and [x for x, m in MO[(18, 10)] if m and re.search(r'V[a-zA-Z]r', m)] == ['מעביר', 'קסם', 'מעונן', 'ומנחש', 'ומכשף'] and [x for x, m in MO[(18, 11)] if m and re.search(r'V[a-zA-Z]r', m)] == ['וחבר', 'ושאל', 'ודרש', 'המתים']   # the diviners' list is PARTICIPLES — nine agent nouns in two verses
NEG = {c: {v: sum(1 for x in W(c, v) if x in ('לא', 'ולא')) for v in range(1, NV[c] + 1) if any(x in ('לא', 'ולא') for x in W(c, v))} for c in CHS}
assert NEG == {17: {1: 1, 3: 1, 6: 1, 11: 1, 13: 1, 15: 2, 16: 3, 17: 3}, 18: {1: 1, 2: 1, 9: 1, 10: 1, 14: 1, 16: 3, 19: 1, 20: 1, 21: 1, 22: 4}} and sum(NEG[17].values()) == 13 and sum(NEG[18].values()) == 15, NEG
assert [f'{c}:{v}' for c, v in SPAN if 'לאמר' in W(c, v)] == ['18:16'] and [f'{c}:{v}' for c, v in SPAN if 'למען' in W(c, v)] == ['17:16', '17:19', '17:20'] and [f'{c}:{v}' for c, v in SPAN if any(x in ('לבלתי', 'ולבלתי') for x in W(c, v))] == ['17:12', '17:20'] and [f'{c}:{v}' for c, v in SPAN if W(c, v)[0] in ('כי', 'וכי', 'אם', 'רק', 'אך')] == ['17:2', '17:8', '17:14', '17:16', '18:5', '18:6', '18:9', '18:12', '18:14', '18:20', '18:21']
assert [f'{c}:{v}' for c, v in SPAN for i, (x, _) in enumerate(MO[(c, v)][:-1]) if x in ('ויאמר', 'וידבר') and MO[(c, v)][i + 1][0] == 'יהוה'] == ['18:17']   # ONE divine frame in the two chapters — "and the LORD said to me" inside Moses' retelling of Horeb
NAME = {c: (sum(1 for v in range(1, NV[c] + 1) for x in W(c, v) if x == 'יהוה'), sum(1 for v in range(1, NV[c] + 1) for x in W(c, v) if x == 'ליהוה'), [v for v in range(1, NV[c] + 1) if any(a == 'יהוה' and b == 'אלהיך' for a, b in zip(W(c, v), W(c, v)[1:]))], [v for v in range(1, NV[c] + 1) if not any('יהוה' in x for x in W(c, v))]) for c in CHS}
assert NAME == {17: (9, 1, [1, 2, 8, 12, 14, 15], [3, 4, 5, 6, 7, 9, 11, 13, 17, 18, 20]), 18: (19, 0, [5, 9, 12, 13, 14, 15, 16], [3, 4, 8, 10, 11, 18, 19, 20])} and [(c, v, x) for c, v in SPAN for x in W(c, v) if x in ('אלהיו', 'אלהי')] == [(17, 19, 'אלהיו'), (18, 7, 'אלהיו'), (18, 16, 'אלהי')], NAME
with contextlib.redirect_stdout(io.StringIO()):
    import register_census as RC
    _ink = RC.read_ink()
assert [k for k in RC.receipts(_ink) if k[0] == 'Deut' and k[1] in CHS] == [] and [x for x in RC.footers(_ink) if x[0][0] == 'Deut' and x[0][1] in CHS] == [] and [x for x in RC.register_headers(_ink) if x[0][0] == 'Deut' and x[0][1] in CHS] == [] and [k for k in RC.receipts(_ink) if k[0] == 'Deut' and k[1] <= 18] == [('Deut', 1, 3), ('Deut', 1, 19), ('Deut', 1, 41), ('Deut', 4, 5), ('Deut', 5, 12), ('Deut', 5, 16), ('Deut', 5, 32), ('Deut', 10, 5)]   # THE REGISTER on 17-18: no receipt, no footer, no header — the book's eight receipts unmoved
# ---- THE FORMULAS OVER THE TORAH AND THE BIBLE (the measure's C section, asserted) ----
assert P('ובערת', 'הרע', 'מקרבך', books=T) == ['Deut 13:6', 'Deut 17:7', 'Deut 19:19', 'Deut 21:21', 'Deut 22:21', 'Deut 22:24', 'Deut 24:7'] and P('ובערת', 'הרע', 'מישראל', books=T) == ['Deut 17:12', 'Deut 22:22'] and U('ובערת', 'תבערו', 'ובערתם', books=T) == ['Deut 13:6', 'Deut 17:12', 'Deut 17:7', 'Deut 19:13', 'Deut 19:19', 'Deut 21:21', 'Deut 22:21', 'Deut 22:22', 'Deut 22:24', 'Deut 24:7', 'Exod 35:3']   # THE PURGE FORMULA at its second and third seats of nine (17:7 "from your midst", 17:12 "from Israel" — the second form's two seats); the consonantal census carries Exodus 35:3's "you shall not KINDLE" — the store's gloss "and-kindle" the homograph
assert P('הכהנים', 'הלוים', books=T) == ['Deut 17:18', 'Deut 17:9', 'Deut 24:8'] and len(P('הכהנים', 'הלוים', books=None)) == 13 and P('הכהנים', 'בני', 'לוי', books=T) == ['Deut 21:5', 'Deut 31:9'] and P('בימים', 'ההם', books=T) == ['Deut 17:9', 'Deut 19:17', 'Deut 26:3', 'Exod 2:11', 'Gen 6:4']   # "the priests the Levites" the book's three (17:9, 17:18, 24:8) of the Bible's thirteen; "in those days" the judge's clause at 17:9, 19:17, 26:3
assert P('ימין', 'ושמאל', books=T) == ['Deut 17:11', 'Deut 5:32'] and P('ימין', 'ושמאול', books=T) == ['Deut 17:20', 'Deut 28:14', 'Deut 2:27', 'Num 20:17', 'Num 22:26'] and P('ימין', 'ושמאול', books=None) == ['1Sam 6:12', '2Chr 34:2', '2Kgs 22:2', 'Deut 17:20', 'Deut 28:14', 'Deut 2:27', 'Isa 54:3', 'Josh 1:7', 'Josh 23:6', 'Num 20:17', 'Num 22:26', 'Prov 4:27']   # "RIGHT OR LEFT" SPELLED TWO WAYS IN ONE CHAPTER — defective at 17:11 (the court's word; 5:32 its one twin) and full at 17:20 (the king's; 28:14's)
assert P('שנים', 'עדים', 'או', 'שלשה', books=None) == ['Deut 17:6'] and P('פי', 'שנים', 'עדים', books=None) == ['Deut 17:6'] and P('עד', 'אחד', books=T) == ['Deut 17:6', 'Deut 19:15', 'Exod 14:28', 'Exod 9:7'] and SHARED(('Deut', 17, 6), ('Deut', 19, 15)) == ['על', 'פי'] and SHN(('Deut', 17, 6), ('Deut', 19, 15)) == 6 and SHARED(('Deut', 17, 6), ('Num', 35, 30)) == ['עדים']   # "two witnesses or three" ONE seat (19:15 says "two witnesses" with the other spelling — 190:3's gezerah shavah (the analogy by a shared word) rides on the two spellings); "one witness" the Torah's four (two of them "not one was left" — Exodus's homograph)
assert P('ישמעו', 'ויראו', books=None) == ['Deut 17:13', 'Deut 19:20', 'Deut 21:21'] and P('המקום', 'אשר', 'יבחר', books=('Deut',)) == ['Deut 12:11', 'Deut 12:21', 'Deut 12:26', 'Deut 12:5', 'Deut 14:24', 'Deut 14:25', 'Deut 16:6', 'Deut 17:8', 'Deut 18:6', 'Deut 26:2'] and [(c, v, i) for c, v in SPAN for i, x in enumerate(W(c, v)) if x in ('במקום', 'המקום') and W(c, v)[i + 1] == 'אשר' and W(c, v)[i + 2] == 'יבחר'] == [(17, 8, 20), (18, 6, 16)]   # "hear and fear" three (the seducer's 13:12 spelled otherwise); THE PLACE at 17:8 (the high court) and 18:6 (the Levite) — the book's ten with the article
assert P('מלך', 'ככל', 'הגוים', books=None) == ['Deut 17:14'] and P('מקרב', 'אחיך', books=None) == ['Deut 17:15'] and P('משנה', 'התורה', books=None) == ['Deut 17:18'] and len(P('התורה', 'הזאת', books=None)) == 16 and P('כל', 'ימי', 'חייו', books=T) == ['Deut 17:19'] and len(P('כל', 'ימי', 'חייו', books=None)) == 10 and P('ליראה', 'את', 'יהוה', books=None) == ['Deut 10:12', 'Deut 14:23', 'Deut 17:19', 'Deut 31:13', 'Deut 6:24'] and P('יאריך', 'ימים', books=T) == ['Deut 17:20'] and P('רום', 'לבבו', books=None) == ['Deut 17:20']   # the king's clauses each ONE seat in the Bible — "a king like all the nations", "from among your brothers", "a copy of this law", "his heart lifted", "prolong days" (the Torah's one of the Bible's four); "this law" sixteen in the Torah, fifteen in the book
assert P('ירבה', 'לו', 'סוסים', books=None) == ['Deut 17:16'] and P('ירבה', 'לו', 'נשים', books=None) == ['Deut 17:17'] and P('וכסף', 'וזהב', 'לא', 'ירבה', books=None) == ['Deut 17:17'] and P('מלך', 'אשר', 'יבחר', 'יהוה', books=None) == ['Deut 17:15'] and P('איש', 'נכרי', 'אשר', 'לא', 'אחיך', books=None) == ['Deut 17:15'] and U('נכרי', 'הנכרי', 'לנכרי', books=T) == ['Deut 14:21', 'Deut 15:3', 'Deut 17:15', 'Deut 23:21', 'Exod 21:8'] and len(U('סוס', 'סוסים', 'סוסיו', 'וסוסים', 'סוסי', books=T)) == 9 and [(c, v, x) for c, v in SPAN for x in W(c, v) if x in ('מלך', 'המלך')] == [(17, 14, 'מלך'), (17, 15, 'מלך'), (17, 15, 'מלך')]   # the three "not multiply" each one seat; "king" three times in the two chapters and never "the king" — a king not yet on the tape
assert P('חלק', 'ונחלה', books=T) == ['Deut 10:9', 'Deut 12:12', 'Deut 14:27', 'Deut 14:29', 'Deut 18:1', 'Gen 31:14'] and P('אשי', 'יהוה', books=T) == ['Deut 18:1', 'Lev 21:21', 'Lev 21:6', 'Lev 4:35', 'Lev 5:12', 'Lev 7:30'] and P('יהוה', 'הוא', 'נחלתו', books=None) == ['Deut 10:9', 'Deut 18:2'] and P('ראשית', 'גז', books=None) == [] and P('דגנך', 'תירשך', 'ויצהרך', books=None) == ['Deut 14:23', 'Deut 18:4'] and P('לעמד', 'לשרת', 'בשם', books=None) == ['Deut 18:5'] and P('בכל', 'אות', 'נפשו', books=None) == ['Deut 18:6'] and P('בכל', 'אות', 'נפשך', books=None) == ['Deut 12:15', 'Deut 12:20', 'Deut 12:21'] and P('חלק', 'כחלק', books=None) == ['Deut 18:8']   # "portion and inheritance" the book's five and GENESIS 31:14 (Rachel and Leah's "is there yet any portion or inheritance for us" — the tape's own line); "the LORD is his inheritance" 10:9 and here; the fleece's phrase carries its vav ("and the first of the fleece" — the bare pair no seat); "with all the desire of HIS soul" the Levite's one seat, chapter 12's three "your soul"
assert P('כתועבת', 'הגוים', books=None) == ['2Kgs 21:2', 'Deut 18:9'] and P('תועבת', 'יהוה', books=T) == ['Deut 12:31', 'Deut 17:1', 'Deut 18:12', 'Deut 22:5', 'Deut 23:19', 'Deut 25:16', 'Deut 27:15', 'Deut 7:25'] and len(P('תועבת', 'יהוה', books=None)) == 19 and len(U('תועבת', 'תועבה', 'התועבה', 'התועבת', 'כתועבת', books=('Deut',))) == 14 and P('מעביר', 'בנו', 'ובתו', 'באש', books=None) == ['Deut 18:10'] and P('תמים', 'תהיה', books=None) == ['Deut 18:13']   # "an abomination of the LORD" the Torah's eight, all Deuteronomy's (17:1 and 18:12 two of them; the Proverbs' eleven the rest); "the abominations of the nations" here and Manasseh's (2 Kings 21:2 — the run's case)
assert U('קסם', 'קסמים', 'קוסם', books=None) == ['1Sam 15:23', '2Kgs 17:17', 'Deut 18:10', 'Deut 18:14', 'Ezek 21:26', 'Num 23:23', 'Prov 16:10'] and U('מעונן', 'מעננים', 'תעוננו', books=None) == ['Deut 18:10', 'Deut 18:14', 'Lev 19:26'] and U('ומנחש', 'מנחש', 'תנחשו', books=None) == ['Deut 18:10', 'Lev 19:26'] and U('ומכשף', 'מכשף', 'מכשפה', 'מכשפים', books=None) == ['Deut 18:10', 'Exod 22:17'] and U('וידעני', 'ידעני', 'ידענים', 'והידענים', books=None) == ['Deut 18:11', 'Lev 20:27'] and P('אל', 'המתים', books=None) == ['Deut 18:11', 'Eccl 9:3', 'Isa 8:19']   # THE DIVINERS' CENSUS: the augur's word at Balaam's "no augury in Israel" (Numbers 23:23); the soothsayer and the omen-reader Leviticus 19:26's pair; the sorcerer Exodus 22:17's sorceress; the familiar spirit Leviticus 20:27's
assert P('נביא', 'מקרבך', 'מאחיך', 'כמני', books=None) == ['Deut 18:15'] and P('נביא', 'אקים', books=None) == ['Deut 18:18'] and P('ביום', 'הקהל', books=None) == ['Deut 10:4', 'Deut 18:16', 'Deut 9:10'] and P('האש', 'הגדלה', 'הזאת', books=None) == ['Deut 18:16', 'Deut 5:25'] and P('דברי', 'בפיו', books=None) == ['Deut 18:18'] and P('דברי', 'בפיך', books=None) == ['Isa 51:16', 'Jer 1:9', 'Jer 5:14'] and P('ומת', 'הנביא', 'ההוא', books=None) == ['Deut 18:20'] and P('בשם', 'אלהים', 'אחרים', books=None) == ['Deut 18:20'] and P('לא', 'תגור', 'ממנו', books=None) == ['Deut 18:22'] and U('נביא', 'הנביא', 'נביאים', books=('Deut',)) == ['Deut 13:2', 'Deut 13:4', 'Deut 18:15', 'Deut 18:18', 'Deut 18:20', 'Deut 18:22', 'Deut 34:10']   # "My words in his mouth" one seat, "in YOUR mouth" the prophets' three (Jeremiah 1:9 the row's own cross-reference at 175:1); "prophet" in the book at 13:2-4, here five times, and 34:10's "no prophet like Moses"
assert P('מום', 'כל', 'דבר', 'רע', books=None) == ['Deut 17:1'] and P('ולשמש', 'או', 'לירח', books=None) == ['Deut 17:3'] and P('צבא', 'השמים', books=T) == ['Deut 17:3', 'Deut 4:19'] and len(P('צבא', 'השמים', books=None)) == 16 and P('אשר', 'לא', 'צויתי', books=None) == ['Deut 17:3', 'Jer 19:5', 'Jer 7:31'] and P('בין', 'דם', 'לדם', books=None) == ['2Chr 19:10', 'Deut 17:8'] and P('נגע', 'לנגע', books=None) == ['Deut 17:8'] and P('דברי', 'ריבת', books=None) == ['Deut 17:8'] and P('ודרשת', 'היטב', books=None) == ['Deut 17:4'] and P('ודרשת', 'וחקרת', 'ושאלת', 'היטב', books=None) == ['Deut 13:15'] and P('יד', 'העדים', 'תהיה', 'בו', 'בראשנה', books=None) == ['Deut 17:7'] and P('ידך', 'תהיה', 'בו', 'בראשונה', books=None) == ['Deut 13:10'] and P('וקרא', 'בו', books=None) == ['Deut 17:19']   # "which I have not commanded" — 17:3 and Jeremiah 19:5 and 7:31 (148:9's three words); "between blood and blood" here and Jehoshaphat's courts (2 Chronicles 19:10 — the run's case); the hand first: the witnesses' here, "your hand" the brother's at 13:10
assert U('בזדון', 'זדון', 'זדונו', books=None) == ['Deut 17:12', 'Deut 18:22', 'Jer 49:16', 'Jer 50:31', 'Jer 50:32', 'Obad 1:3', 'Prov 11:2', 'Prov 13:10', 'Prov 21:24'] and U('יזיד', 'יזידון', 'הזיד', 'זדו', 'ותזדו', books=None) == ['Deut 17:13', 'Deut 18:20', 'Deut 1:43', 'Exod 18:11'] and P('אדרש', 'מעמו', books=None) == ['Deut 18:19'] and U('השפט', 'השופט', books=('Deut',)) == ['Deut 17:12', 'Deut 17:9', 'Deut 25:2'] and U('הכהן', books=('Deut',)) == ['Deut 17:12', 'Deut 20:2', 'Deut 26:3', 'Deut 26:4']   # "PRESUMPTUOUSLY" (the noun) in the Torah only at 17:12 and 18:22 — the rebel against the court and the false prophet share the one word; the verb at 17:13, 18:20, and 1:43 (the people at Hormah) and Exodus 18:11 (Egypt's)
assert U('והקבה', 'הקבה', 'קבה', books=None) == ['Deut 18:3', 'Num 22:11', 'Num 22:17', 'Num 23:8', 'Num 25:8'] and U('והלחיים', 'הלחיים', 'לחיים', books=None) == ['2Sam 15:21', 'Deut 18:3', 'Isa 4:3', 'Prov 10:16', 'Prov 10:17', 'Prov 11:19', 'Prov 19:23'] and U('ראשית', 'וראשית', 'מראשית', books=('Deut',)) == ['Deut 18:4', 'Deut 21:17', 'Deut 26:10', 'Deut 26:2', 'Deut 33:21']   # THE MAW'S CONSONANTS carry Balaam's "curse" (Numbers 22:11, 22:17, 23:8) and Numbers 25:8's "her belly" — 165:14's own play (the maw for Kozbi's belly) sits in the consonantal census; "the cheeks" share their letters with "to life"
assert [(c, v, x) for c, v in SPAN for x in W(c, v) if 'שעריך' in x] == [(17, 2, 'שעריך'), (17, 5, 'שעריך'), (17, 8, 'בשעריך'), (18, 6, 'שעריך')] and [(c, v, x) for c, v in SPAN for x in W(c, v) if 'לוי' in x] == [(17, 9, 'הלוים'), (17, 18, 'הלוים'), (18, 1, 'הלוים'), (18, 1, 'לוי'), (18, 6, 'הלוי'), (18, 7, 'הלוים')] and [(c, v, x) for c, v in SPAN for x in W(c, v) if x == 'מצרימה' or 'מצרים' in x] == [(17, 16, 'מצרימה')] and [(c, v, x) for c, v in SPAN for x in W(c, v) if 'חרב' in x] == [(18, 16, 'בחרב')]
# ---- THE KIN BY COMPUTATION AND THE TWINS DIFFED (the measure's A and B sections, asserted) ----
assert KINC[(17, 1)][0] == ('Deut 15:21', 4, 6) and KINC[(17, 4)][0] == ('Deut 13:15', 9, 9) and KINC[(17, 5)][0] == ('Deut 22:24', 6, 5) and KINC[(17, 6)][0] == ('Deut 19:15', 4, 6) and KINC[(17, 7)][0] == ('Deut 13:10', 5, 7) and KINC[(17, 9)][0] == ('Deut 26:3', 4, 6) and KINC[(17, 10)][0] == ('Deut 17:11', 4, 6) and KINC[(17, 11)][0] == ('Deut 17:10', 4, 6) and KINC[(17, 14)][:3] == [('1Sam 8:5', 3, 3), ('2Chr 36:23', 3, 3), ('Deut 26:1', 3, 10)] and KINC[(17, 16)][0] == ('Deut 31:2', 4, 5) and KINC[(17, 17)][0] == ('Deut 8:13', 3, 3) and KINC[(17, 19)][:3] == [('Deut 27:3', 4, 5), ('Deut 28:58', 4, 5), ('Deut 31:12', 4, 8)] and KINC[(17, 20)][0] == ('Josh 23:6', 4, 4)
assert KINC[(18, 2)][0] == ('Deut 10:9', 4, 8) and KINC[(18, 8)] == [] and KINC[(18, 11)] == [] and KINC[(18, 15)] == [('2Chr 25:15', 2, 1)] and KINC[(18, 16)][0] == ('Deut 5:25', 6, 5) and KINC[(18, 17)][0] == ('Deut 5:28', 4, 5) and KINC[(18, 21)][0] == ('Deut 7:17', 3, 3) and KINC[(18, 22)][0] == ('Deut 18:20', 3, 4) and KINC[(18, 3)][0] == ('2Kgs 12:9', 3, 3) and KINC[(18, 1)][:2] == [('1Kgs 12:21', 3, 4), ('Deut 10:9', 3, 5)]   # TWO VERSES WITH NO KIN AT ALL — 18:8 (portion as portion) and 18:11 (the charmer, the ghost, the familiar spirit, the dead); 18:15's "a prophet like me" next to none (one Chronicles verse at two tokens)
assert SHN(('Deut', 17, 4), ('Deut', 13, 15)) == 9 and SHARED(('Deut', 17, 4), ('Deut', 13, 15)) == ['היטב', 'והנה', 'אמת', 'נכון', 'הדבר', 'נעשתה', 'התועבה', 'הזאת'] and SHN(('Deut', 17, 7), ('Deut', 13, 10)) == 7 and SHARED(('Deut', 17, 7), ('Deut', 13, 10)) == ['להמיתו', 'ויד', 'כל', 'העם', 'באחרנה'] and SHN(('Deut', 17, 14), ('Deut', 26, 1)) == 10 and SHN(('Deut', 17, 19), ('Deut', 31, 12)) == 8 and SHN(('Deut', 18, 2), ('Deut', 10, 9)) == 8 and SHARED(('Deut', 18, 2), ('Deut', 10, 9)) == ['אחיו', 'יהוה', 'הוא', 'נחלתו', 'כאשר', 'דבר'] and SHN(('Deut', 18, 16), ('Deut', 5, 25)) == 5 and SHARED(('Deut', 18, 16), ('Deut', 5, 25)) == ['לשמע', 'את', 'קול', 'יהוה'] and SHN(('Deut', 18, 5), ('Deut', 21, 5)) == 7
assert SHN(('Deut', 17, 8), ('Exod', 18, 22)) == 0 and SHN(('Deut', 17, 11), ('Deut', 5, 29)) == 0 and SHN(('Deut', 17, 20), ('Deut', 8, 14)) == 0 and SHN(('Deut', 18, 3), ('Exod', 29, 27)) == 0 and SHN(('Deut', 18, 4), ('Num', 18, 12)) == 0 and SHN(('Deut', 18, 10), ('Lev', 20, 2)) == 0 and SHN(('Deut', 18, 20), ('Deut', 13, 2)) == 0 and SHN(('Deut', 18, 22), ('Deut', 13, 2)) == 0 and SHN(('Deut', 18, 15), ('Deut', 18, 18)) == 1 and SHN(('Deut', 17, 16), ('1Kgs', 10, 26)) == 1 and SHARED(('Deut', 17, 17), ('1Kgs', 11, 3)) == ['לו', 'נשים'] and SHARED(('Deut', 17, 18), ('Josh', 8, 32)) == ['את', 'משנה']   # THE TWINS THAT SHARE NOTHING IN ORDER: the hard case against Jethro's (17:8 / Exodus 18:22), the priests' dues against Numbers 18:12 and the wave breast (18:3-4), the fire against Leviticus 20:2's Molech, the false prophet against 13:2 — the same laws in other words; Solomon's horses one token, his wives "to him wives", Joshua's copy "the copy"
assert words('Deut', 34, 10) == ['ולא', 'קם', 'נביא', 'עוד', 'בישראל', 'כמשה', 'אשר', 'ידעו', 'יהוה', 'פנים', 'אל', 'פנים'] and [x for x in W(18, 15) if x.startswith('כמ')] == ['כמני'] and [x for x in W(18, 18) if x.startswith('כמ')] == ['כמוך'] and words('1Sam', 8, 5)[-3:] == ['לשפטנו', 'ככל', 'הגוים']   # "like me" at 18:15, "like you" at 18:18, "like Moses" at 34:10 — the three seats of the comparison; Samuel's elders end with 17:14's own two words
# ---- ONKELOS OVER THE BOOK (the measure's D section, asserted on the plain Aramaic through NFKC; EXPORT verse numbers) ----
def ARM(c, v): return [plain(unicodedata.normalize('NFKC', x)).strip('.:()') for x in clean(onk_he[c - 1][v - 1]).rstrip(':').split()]
def SEATS(sub): return [(c + 1, v + 1) for c in range(34) for v in range(len(onk_he[c])) if sub in ' '.join(ARM(c + 1, v + 1))]
assert SEATS('לית לך רשו') == [(12, 17), (16, 5), (17, 15), (22, 3)] and SEATS('על מימר') == [(1, 26), (17, 6), (17, 10), (17, 11), (19, 15), (21, 5), (33, 3), (34, 5)] and len(SEATS('מימרא דיי')) == 24 and (18, 16) in SEATS('מימרא דיי') and len(SEATS('מימרי')) == 22 and (18, 19) in SEATS('מימרי') and len(SEATS('מימר')) == 91   # "you have no permission" the book's four (17:15 the king's); "BY THE MEMRA OF" — the witnesses' mouth, the court's word and its law (17:6, 10, 11) rendered "by the word of"; "the voice of the Memra of the LORD" at 18:16; "MY MEMRA will require it" at 18:19
assert SEATS('בית דינך') == [(17, 5)] and SEATS('דחיב קטול') == [(17, 6)] and SEATS('עבד דביש') == [(9, 18), (13, 6), (17, 7), (17, 12), (19, 19), (21, 21), (22, 21), (22, 22), (22, 24), (24, 7)] and SEATS('מכתש סגירו') == [(17, 8), (21, 5), (24, 8)] and SEATS('פתשגן') == [(17, 18)] and SEATS('נוכרי') == [(17, 15)] and len(SEATS('אוריתא')) == 24 and all(s in SEATS('אוריתא') for s in ((17, 11), (17, 18), (17, 19)))   # "the gate of YOUR COURT" (17:5 — the gate a court); "the one liable to death" for "the dead"; "THE DOER OF EVIL" at every purge seat but one (the nine seats and 9:18's "the evil you did") — Onkelos purges a man, never an abstraction; "the plague of confinement" for the stroke; "the copy" one seat
assert len(SEATS('טעות עממיא')) == 18 and all(s in SEATS('טעות עממיא') for s in ((17, 3), (18, 9), (18, 20))) and SEATS('מרחק') == [(7, 25), (7, 26), (12, 31), (14, 3), (17, 1), (18, 12), (22, 5), (23, 19), (24, 4), (25, 16), (27, 15)] and len(SEATS('קרויך')) == 25 and all(s in SEATS('קרויך') for s in ((17, 2), (17, 8), (18, 6)))   # "the idols of the nations" for "other gods" (eighteen seats — 17:3, 18:9, 18:20 among them); "DISTANCED" for "abomination" at the book's eleven; "your cities" for "your gates"
assert SEATS('קרבניא דיי') == [(18, 1)] and SEATS('מתנן דיהב ליה') == [(10, 9), (18, 2)] and SEATS('דחזי לכהניא') == [(18, 3)] and SEATS('ממטרתא') == [(18, 8)] and SEATS('אתקינו אבהתא') == [(18, 8)] and SEATS('בצלו') == [(18, 7)] and SEATS('בדחלתא דיי') == [(4, 4), (18, 13)] and SEATS('פתגמי נבואתי') == [(18, 18)] and SEATS('נבוא') == [(18, 18)] and SEATS('קבתא') == [(18, 3)] and SEATS('רטין') == [(18, 11)] and SEATS('זכורו') == [(18, 11)]   # THE ADDITIONS OF CHAPTER 18: "the gifts He gave him" for "the LORD is his inheritance" (10:9 and here); "what is fit for the priests" for "the priests' due"; "THE WATCH THAT COMES ON THE SABBATH, AS THE FATHERS ORDAINED" for "besides the sales of the fathers" (169:3's barter written into the verse); "(in prayer)" at 18:7 bracketed; "in the fear of the LORD" for "with"; "the words of MY PROPHECY" at 18:18 — "prophecy" once in the whole book
assert SEATS('ברשע') == [(15, 9), (17, 12), (18, 22)] and SEATS('ירשע') == [(18, 20)] and len(SEATS('תדחל')) == 15 and (18, 22) in SEATS('תדחל') and len(SEATS('תקבלון')) == 6 and (18, 15) in SEATS('תקבלון') and SEATS('סנהדרין') == [] and len(SEATS('דינא')) == 14 and all(s in SEATS('דינא') for s in ((17, 8), (17, 9), (17, 11), (17, 12))) and not any(s in SEATS('שכנתיה') for s in SPAN) and len(SEATS('שכנתיה')) == 16   # "in wickedness" for "presumptuously" (15:9's "Belial" the third seat); "you shall ACCEPT" for "hearken" at 18:15; NO SHEKHINAH in the two chapters (the place named twice without it)
assert ARM(17, 6)[:4] == ['על', 'מימר', 'תרין', 'סהדין'] and ARM(18, 8) == ['חלק', 'כחלק', 'ייכלון', 'בר', 'ממטרתא', 'דייתי', 'בשבתא', 'דכן', 'אתקינו', 'אבהתא'] and ARM(18, 13) == ['שלים', 'תהי', 'בדחלתא', 'דיי', 'אלהך'] and ARM(18, 19)[-3:] == ['מימרי', 'יתבע', 'מניה'] and ARM(18, 2)[6:10] == ['מתנן', 'דיהב', 'ליה', 'יי']

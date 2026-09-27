import os as _os
_ROOT = _os.path.normpath(_os.path.join(_os.path.dirname(_os.path.abspath(__file__)), '..', '..', '..'))   # THE PORTABLE REPO (2026-09-15): the repo root from this file's own place
#!/usr/bin/env python3
# THE DEUTERONOMY WALK, sitting 17 — CHAPTERS 22-25, Deuteronomy 22:1-25:19 IN THE LEAN FORM (2026-09-25; the owner: "Reread and go" after the compaction at #216 —
# THE LEAN PASS's seventh sitting, the first on FOUR chapters: the reading in runs under the 600k cap, one compile window, a short tail): THE INK of the four
# chapters, computed from the Tanakh DB, the snapshot store and the shelf's own bytes — never typed. Sitting 16's form (ch19_ink.py): the generic helpers copied
# by derive_ch22_ink.py from the forms' ch17_ink.py by content markers (the four chapters substituted for the pair), the constants and every assert the four
# chapters' own, typed FROM THE PRINTS (ch22_dump0.out … ch25_dump0.out, ch22_split.out, ch22_measure_lean.out). THE TWO DIVISIONS AGREE in all four chapters
# (29 = 29, cost 29; 26 = 26, cost 30; 22 = 22, cost 15; 19 = 19, cost 21) — the identity; the English's 22:30 is nowhere in the export. THE SPINE IS ON THE FOUR
# CHAPTERS — SEVENTY-FIVE piskaot 222-296 with 434 rows (157 + 99 + 99 + 79): TWENTY-FOUR in chapter 22 (222 HEADLESS on 22:1, opening on Exodus 23:5; 223 on
# 22:2 … 245 on 22:29; 236 HEADLESS inside 22:16-17; 232 AND 233 BOTH ON 22:11), TWENTY-TWO in chapter 23 (246 on 23:1 … 267 on 23:26 — contiguous, every head in
# verse order), EIGHTEEN in chapter 24 (268 on 24:1 … 285 on 24:21; 269 HEADLESS inside 24:1 with fourteen rows, 283 HEADLESS inside 24:19), ELEVEN in chapter 25
# (286 on 25:1 … 296 on 25:17; 295 HEADLESS inside 25:15); 221 on 21:22 before, 297 on 26:1 after; no tail folded (221's rows carry no word of 22:1; 296's stop
# before 26:1's words; 246:1, 268:1, 286:1 and 297:1 open with their verses' citations). FOURTEEN rows elsewhere cite the four chapters by the union of the four
# files (ten READ BEFORE at chapters 11-15, 17-18 and 19-21, REREAD WHOLE; four fresh — 336:2 on 22:7 and 352:8, 10, 17 whose English cites "Dt.23:12" from the
# Benjamin blessing: to be judged whole). NO portion edge inside 22-25 (Ki Teitzei 21:10-25:19 holds the four; Ki Tavo opens at 26:1, a chapter edge). The parser
# MEASURED on every verse — the number verses 22:12 [4] "four corners", 22:19 [100], 22:22 [2] and 22:24 [2] starred "the two of them", 22:29 [50], 23:17 [1]
# "in one of your gates", 23:19 [2] starred "both of them", 24:5 [1] "one year", 25:3 [40] "forty", 25:5 [1], 25:11 [1] starred "the one"; the ordinals 23:3 and
# 23:4 [10] "tenth generation", 23:9 [3] "third", 24:4 [1] "the first husband". THE STORE = THE DB at every verse of chapters 23-25 and at ELEVEN verses of
# chapter 22 it differs (22:15, 16, 20, 21, 23-29 — "the girl" written without its final letter, the store carrying the read form beside it); the tokens
# 437 / 339 / 327 / 260. The hand's facts as asserts, run all at once by assert_driver.py.
import json, os, re, html, sqlite3, sys, io, contextlib, unicodedata, subprocess
from collections import Counter
ROOT = _ROOT
sys.path.insert(0, f'{ROOT}/World/step9')
DATE = '2026-09-25'
CHS = (22, 23, 24, 25)
UIDS = ['deu_22_return_sex_laws', 'deu_23_qahal_purity_vows', 'deu_24_divorce_poor', 'deu_25_courts_yibbum']   # the drafts' own ids (the G prints): qahal = the assembly, yibbum = the levirate
SPANS = {'deu_22_return_sex_laws': (22, 1, 29), 'deu_23_qahal_purity_vows': (23, 1, 26), 'deu_24_divorce_poor': (24, 1, 22), 'deu_25_courts_yibbum': (25, 1, 19)}
PREFIX = {'deu_22_return_sex_laws': 'DV22', 'deu_23_qahal_purity_vows': 'DV23', 'deu_24_divorce_poor': 'DV24', 'deu_25_courts_yibbum': 'DV25'}
SPAN = [(22, v) for v in range(1, 30)] + [(23, v) for v in range(1, 27)] + [(24, v) for v in range(1, 23)] + [(25, v) for v in range(1, 20)]
PISKAOT = list(range(222, 297))   # THE SPINE ON THE FOUR CHAPTERS: 222-245 chapter 22's twenty-four (two headless), 246-267 chapter 23's twenty-two, 268-285 chapter 24's eighteen (two headless), 286-296 chapter 25's eleven (one headless) — the A prints and the split's; 221 heads on 21:22, 297 on 26:1
PISKAOT_BY = {22: list(range(222, 246)), 23: list(range(246, 268)), 24: list(range(268, 286)), 25: list(range(286, 297))}
HEADLESS = [222, 236, 269, 283, 295]   # the five piskaot with no book-named citation at their head (the dumps: "head None"; the split: 222:1 opens on Exodus 23:5 "when you see", 236:1 on 22:16-17's "to be his wife, and he hates her", 269:1 on 24:1's "if she finds no favor", 283:1 on 24:19's "and you forgot a sheaf", 295:1 on 25:15's "that your days be long") — read WHOLE from the export
SPINE_ROWS = {222: 8, 223: 4, 224: 7, 225: 6, 226: 3, 227: 11, 228: 8, 229: 10, 230: 13, 231: 3, 232: 5, 233: 5, 234: 7, 235: 11, 236: 4, 237: 3, 238: 10, 239: 3, 240: 5, 241: 7, 242: 10, 243: 4, 244: 3, 245: 7, 246: 1, 247: 5, 248: 5, 249: 4, 250: 5, 251: 3, 252: 3, 253: 3, 254: 4, 255: 5, 256: 2, 257: 6, 258: 4, 259: 8, 260: 2, 261: 6, 262: 3, 263: 4, 264: 7, 265: 9, 266: 6, 267: 4, 268: 3, 269: 14, 270: 13, 271: 6, 272: 2, 273: 9, 274: 6, 275: 3, 276: 3, 277: 5, 278: 5, 279: 4, 280: 3, 281: 3, 282: 4, 283: 6, 284: 6, 285: 4, 286: 17, 287: 3, 288: 6, 289: 11, 290: 4, 291: 9, 292: 5, 293: 2, 294: 9, 295: 4, 296: 9}   # rows per piska, both files (the I prints and the splitter's) — 157 + 99 + 99 + 79 = 434
PREV_CHAPTER_ROWS = []   # no tail folded in (221's rows carry no word of 22:1 — the split's assert; 296's rows stop before 26:1's words — the split's print)
READ_ROWS = [(p, r) for p in PISKAOT for r in range(1, SPINE_ROWS[p] + 1)]   # 434 — this ledger's spine rows
EXP2DB = {22: {e: [e] for e in range(1, 30)}, 23: {e: [e] for e in range(1, 27)}, 24: {e: [e] for e in range(1, 23)}, 25: {e: [e] for e in range(1, 20)}}   # the identity in all four chapters (chapter 5 the book's one split)
DB2EXP = {c: {d: e for e, ds in EXP2DB[c].items() for d in ds} for c in CHS}
# the Hebrew's book-named citations of the four chapters OUTSIDE the spine (the regex reads "(דברים כב ז)" — "Deuteronomy 22:7" — etc.); seven rows cite only in the English (41:3, 63:5, 155:9, 352:8, 352:9, 352:10, 352:17)
OUTSIDE_HE = [(336, 2, (22, 7)), (87, 3, (24, 16)), (94, 3, (24, 16)), (110, 1, (24, 17)), (117, 5, (24, 15)), (122, 1, (24, 1)), (190, 14, (25, 12))]
OUTSIDE = [(41, 3), (63, 5), (87, 3), (94, 3), (110, 1), (117, 5), (122, 1), (155, 9), (190, 14), (336, 2), (352, 8), (352, 9), (352, 10), (352, 17)]   # the FOURTEEN rows READ WHOLE: the union of the four files beyond piskaot 222-296, joined over the four dumps (the split's print)
EXCLUDED = [(352, 8), (352, 9), (352, 10), (352, 17)]   # JUDGED AT THE ROWS: the four rows of 352 cite "Dt.23:12" in the English alone for the blessing of Benjamin's "between his shoulders He dwells" (33:12) — the translator's misprint; the Hebrew cites nothing of chapter 23 — EXCLUDED from the coverage of the four chapters, read whole and kept
INTERPOLATION = []
CITED = {(41, 3): [(24, 19)], (63, 5): [(23, 22)], (87, 3): [(24, 16)], (94, 3): [(24, 16)], (110, 1): [(24, 17)], (117, 5): [(24, 15)], (122, 1): [(24, 1)], (155, 9): [(22, 1)], (190, 14): [(25, 12)], (336, 2): [(22, 7)], (352, 8): [(23, 12)], (352, 9): [(23, 12)], (352, 10): [(23, 12)], (352, 17): [(23, 12)]}
PRIOR_READ = {(41, 3): ['deu_11_ekev_reeh_2026-09-20.md', 'deu_15_reeh_2026-09-22.md'], (63, 5): ['deu_12_reeh_2026-09-20.md'], (87, 3): ['deu_13_reeh_2026-09-21.md'], (94, 3): ['deu_13_reeh_2026-09-21.md'], (110, 1): ['deu_14_reeh_2026-09-21.md'], (117, 5): ['deu_15_reeh_2026-09-22.md'], (122, 1): ['deu_15_reeh_2026-09-22.md'], (155, 9): ['deu_17_18_shoftim_2026-09-24.md'], (190, 14): ['deu_19_21_shoftim_ki_teitzei_2026-09-24.md'], (352, 9): ['deu_17_18_shoftim_2026-09-24.md']}   # the ten outside rows read before (computed from the ledgers, asserted) — REREAD WHOLE here
HEADS_ON = {41: (11, 13), 63: (12, 5), 87: (13, 7), 94: (13, 16), 110: (14, 29), 117: (15, 9), 122: (15, 17), 155: (17, 12), 190: (19, 17), 336: (32, 47), 352: (33, 11)}
FRESH = [(336, 2), (352, 8), (352, 10), (352, 17)]
CREDITED = {}   # under THE WHOLE-ROW RULE no spine row is credited: the rows read before (233:1 at chapter 5; 228:5 at chapter 14; 258:1 at chapter 6; 261:2 at chapters 17-18; 251:1, 259:5 and 293:2 at chapters 19-21; 279:4 at chapter 15; 281:1 at chapter 16; 286:16 at chapter 12; 286:1 and 292:1 at Genesis 29's ledger) are REREAD WHOLE here and marked so
TITLE = "Chapters 22-25 — You shall not see your brother's ox or sheep straying and hide yourself: return them; if he is not near or not known, gather it into your house until he seeks it — so his ass, his garment, every lost thing; you may not hide. Raise his fallen ass with him. No man's gear on a woman, no woman's garment on a man — an abomination. The bird's nest: let the mother go, take the young, that it be well with you and your days long. Build a parapet on your new house, that no blood fall from it. Sow no mixed seed in your vineyard, plow not with ox and ass together, wear not wool and linen mingled; make tassels on the four corners of your covering. When a man takes a wife and hates her and lays a charge of shame, saying he found no virginity — her father and mother bring the tokens to the elders at the gate; the elders take the man and chastise him and fine him a hundred of silver for her father, and she is his wife, he may never send her away; but if the charge is true, they bring her to her father's door and the men of her city stone her, for she committed folly in Israel — purge the evil. A man found lying with a married woman: both die — purge the evil. A betrothed virgin found in the city with a man: both stoned at the gate — she did not cry out, he humbled his neighbor's wife; in the field, the man alone dies — she cried and none saved her, as a man rises against his neighbor and murders him. A virgin not betrothed, seized and lain with: the man gives her father fifty of silver, she is his wife because he humbled her, he may never send her away. A man shall not take his father's wife nor uncover his father's skirt. None wounded or cut shall enter the LORD's assembly; no bastard, even to the tenth generation; no Ammonite or Moabite ever — they met you not with bread and water and hired Balaam to curse you, and the LORD turned the curse to blessing; seek not their peace. Abhor not the Edomite, your brother, nor the Egyptian, whose land you sojourned in: their third generation enters. In the camp against your enemies keep from every evil thing: the man unclean by a night's chance goes outside and returns at evening after washing; a place outside the camp, a spade among your gear, cover what comes from you — for the LORD walks in your camp: let it be holy, and let Him see nothing unseemly and turn from you. Hand not the escaped slave to his master: he dwells with you where he chooses; oppress him not. No harlot of Israel's daughters, no sodomite of her sons; bring not a harlot's hire or a dog's price into the LORD's house for any vow. Lend not on interest to your brother — silver, food, anything; to the foreigner you may; that the LORD bless you in the land. A vow: delay not to pay it, it is sin in you; to refrain is no sin; what your lips utter, keep, as you vowed freely. In your neighbor's vineyard eat grapes to your fill, but put none in your vessel; in his standing grain pluck ears with your hand, but swing no sickle. When a man takes a wife and she finds no favor because he found in her an unseemly thing, he writes her a bill of cutting-off and sends her from his house; she marries another who hates her and writes her a bill, or he dies: her first husband may not take her back after she was defiled — an abomination; sin not the land. A new husband is free one year for his house, to rejoice his wife. Take no millstone in pledge — it is a life. A man stealing a soul of his brothers and selling him dies — purge the evil. Keep the plague of leprosy as the priests teach — remember Miriam on the way from Egypt. Lend to your neighbor but enter not his house for the pledge; stand outside; a poor man's pledge you return by sunset, that he sleep in his garment and bless you — righteousness before the LORD. Oppress not a poor hireling, brother or sojourner: give his wage the same day before sunset, lest he cry to the LORD and it be sin in you. Fathers not put to death for sons nor sons for fathers: each for his own sin. Pervert not the sojourner's or orphan's justice; take no widow's garment in pledge — you were a slave in Egypt. The forgotten sheaf, the olive tree's second beating, the vineyard's second gleaning are the sojourner's, the orphan's and the widow's, that the LORD bless your work — remember Egypt. A dispute comes to judgment: they justify the righteous and condemn the wicked; if the wicked deserves stripes, the judge lays him down and beats him by his wickedness in number — forty, no more, lest your brother be degraded before your eyes. Muzzle not the threshing ox. Brothers dwell together and one dies without a son: his wife shall not marry outside; her husband's brother takes her, and the firstborn stands in the dead brother's name, that his name be not blotted from Israel; if he refuses, she goes up to the elders at the gate: 'he refuses to build his brother's house'; if he stands and says 'I do not desire her', she draws his shoe from his foot and spits in his face — 'so is done to the man who builds not his brother's house' — the house of the unshod. Men strive and the wife of one seizes the other's secrets to save her husband: cut off her hand, your eye shall not pity. No two weights or two measures in your bag or house, great and small: a whole and just weight and measure, that your days be long; all who do such are an abomination. Remember Amalek who met you on the way and cut off the stragglers, faint and weary, fearing not God: when the LORD gives you rest from your enemies in the land, blot out the memory of Amalek from under heaven — do not forget"
OUT = f'{ROOT}/logic/oral_triage/deu_22_25_ki_teitzei_{DATE}.md'
PATCHED = bool(os.environ.get('DEU22_PATCHED'))   # the tail's flag: after the manifest and the seat, the drafts carry operators and the store its overrides
db = sqlite3.connect(f'file:{ROOT}/Data/tanakh.sqlite?mode=ro', uri=True)
VC = dict(db.execute("SELECT chapter, COUNT(*) FROM verses WHERE book='Deut' GROUP BY chapter").fetchall())
NV = {c: VC[c] for c in CHS}
# ---- THE HELPERS (ch17_ink.py's, copied by content markers) ----
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
# ---- THE INK'S HELPERS, THE DB AND THE STORE (ch17_ink.py's, the four chapters substituted) ----
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
def W22(v): return words('Deut', 22, v)
def W23(v): return words('Deut', 23, v)
def W24(v): return words('Deut', 24, v)
def W25(v): return words('Deut', 25, v)
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
for c, v, idx, hp, g in store.execute("SELECT v.chapter, v.verse, w.idx, w.he_plain, w.gloss FROM words w JOIN verses v ON w.verse_id=v.id WHERE v.book='Deut' AND v.chapter IN (22, 23, 24, 25) ORDER BY v.id, w.idx"):
    SG.setdefault((c, v), []).append((idx, hp.replace('/', ''), g))
def sg(c, v, tok, nth=0):
    hit = [g for _, hp, g in SG[(c, v)] if hp == tok]
    if len(hit) <= nth: raise KeyError((c, v, tok, nth))
    return hit[nth]
def sidx(c, v, tok, nth=0):
    hit = [i for i, hp, _ in SG[(c, v)] if hp == tok]
    assert len(hit) > nth, (c, v, tok, nth, hit)
    return hit[nth]
STORE_MISMATCH = [(c, v, n, len(by[('Deut', c, v)])) for c, v, n in store.execute("SELECT v.chapter, v.verse, COUNT(*) FROM words w JOIN verses v ON w.verse_id=v.id WHERE v.book='Deut' AND v.chapter IN (22, 23, 24, 25) GROUP BY v.chapter, v.verse").fetchall() if n != len(by[('Deut', c, v)])]
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
def PL(s): return ''.join(c for c in s if c != '/' and not (0x0591 <= ord(c) <= 0x05C7))
def HB0(p, r): return PL(clean(sif_he[p - 1][r - 1]))
def ARM(c, v): return [PL(unicodedata.normalize('NFKC', x)).strip('.:()') for x in clean(onk_he[c - 1][v - 1]).rstrip(':').split()]
def SEATS(sub): return [(c + 1, v + 1) for c in range(34) for v in range(len(onk_he[c])) if sub in ' '.join(ARM(c + 1, v + 1))]
# ---- THE SHELF BY POSITION — the spine ON the four chapters: seventy-five piskaot 222-296 (twenty-four in chapter 22 with TWO HEADLESS and two heads on 22:11, twenty-two in chapter 23 contiguous, eighteen in chapter 24 with TWO HEADLESS, eleven in chapter 25 with ONE HEADLESS); 221 heads on 21:22 before, 297 on 26:1 after; the two files' grains ----
assert NV == {22: 29, 23: 26, 24: 22, 25: 19} and VC[21] == 23 and VC[26] == 19 and len(sif) == 357 and len(sif_he) == 357 and sum(len(s) for s in sif) == 2357 and sum(len(s) for s in sif_he) == 2357
HC = Counter(h[0] for h in heads.values() if h)
assert (HC[22], HC[23], HC[24], HC[25]) == (22, 22, 16, 10) and sorted(HC.items())[:25] == [(1, 24), (3, 4), (6, 6), (11, 21), (12, 20), (13, 14), (14, 14), (15, 16), (16, 19), (17, 16), (18, 16), (19, 10), (20, 14), (21, 17), (22, 22), (23, 22), (24, 16), (25, 10), (26, 4), (31, 1), (32, 36), (33, 14), (34, 1)], sorted(HC.items())[:25]
assert {p: heads[p] for p in range(220, 301)} == {220: (21, 21), 221: (21, 22), 222: None, 223: (22, 2), 224: (22, 3), 225: (22, 4), 226: (22, 5), 227: (22, 6), 228: (22, 7), 229: (22, 8), 230: (22, 9), 231: (22, 10), 232: (22, 11), 233: (22, 11), 234: (22, 12), 235: (22, 13), 236: None, 237: (22, 17), 238: (22, 18), 239: (22, 20), 240: (22, 21), 241: (22, 22), 242: (22, 23), 243: (22, 26), 244: (22, 28), 245: (22, 29), 246: (23, 1), 247: (23, 2), 248: (23, 3), 249: (23, 4), 250: (23, 5), 251: (23, 7), 252: (23, 8), 253: (23, 9), 254: (23, 10), 255: (23, 11), 256: (23, 12), 257: (23, 13), 258: (23, 15), 259: (23, 16), 260: (23, 18), 261: (23, 19), 262: (23, 20), 263: (23, 21), 264: (23, 22), 265: (23, 23), 266: (23, 25), 267: (23, 26), 268: (24, 1), 269: None, 270: (24, 2), 271: (24, 5), 272: (24, 6), 273: (24, 7), 274: (24, 8), 275: (24, 9), 276: (24, 10), 277: (24, 12), 278: (24, 14), 279: (24, 15), 280: (24, 16), 281: (24, 17), 282: (24, 19), 283: None, 284: (24, 20), 285: (24, 21), 286: (25, 1), 287: (25, 4), 288: (25, 5), 289: (25, 6), 290: (25, 8), 291: (25, 9), 292: (25, 11), 293: (25, 12), 294: (25, 13), 295: None, 296: (25, 17), 297: (26, 1), 298: None, 299: None, 300: (26, 4)}, {p: heads[p] for p in range(220, 301)}
HV = {c: [heads[p][1] for p in PISKAOT_BY[c] if heads[p]] for c in CHS}
assert HV[22] == [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 11, 12, 13, 17, 18, 20, 21, 22, 23, 26, 28, 29] and HV[23] == [1, 2, 3, 4, 5, 7, 8, 9, 10, 11, 12, 13, 15, 16, 18, 19, 20, 21, 22, 23, 25, 26] and HV[24] == [1, 2, 5, 6, 7, 8, 9, 10, 12, 14, 15, 16, 17, 19, 20, 21] and HV[25] == [1, 4, 5, 6, 8, 9, 11, 12, 13, 17] and all(HV[c] == sorted(HV[c]) for c in CHS) and [p for p in PISKAOT if heads[p] is None] == HEADLESS and HV[22].count(11) == 2, HV   # every head in verse order in all four chapters (no variant piska out of order this sitting); 232 AND 233 both head on 22:11 (the mingled stuff twice)
NOHEAD = {c: [v for v in range(1, NV[c] + 1) if v not in HV[c]] for c in CHS}
assert NOHEAD == {22: [1, 14, 15, 16, 19, 24, 25, 27], 23: [6, 14, 17, 24], 24: [3, 4, 11, 13, 18, 22], 25: [2, 3, 7, 10, 14, 15, 16, 18, 19]}, NOHEAD   # 22:1 is HEADLESS 222's (opening on Exodus 23:5), 22:14-16 inside 235-236, 24:3-4 inside 270, 25:14-16 inside 294-295, 25:18-19 inside 296
assert {p: (len(sif_he[p - 1]), len(sif[p - 1])) for p in PISKAOT} == {p: (n, n) for p, n in SPINE_ROWS.items()} and [sum(SPINE_ROWS[p] for p in PISKAOT_BY[c]) for c in CHS] == [157, 99, 99, 79] and sum(SPINE_ROWS.values()) == 434 and len(READ_ROWS) == 434 and len(PISKAOT) == 75 and READ_ROWS[:2] == [(222, 1), (222, 2)] and READ_ROWS[-1] == (296, 9) and [SPINE_ROWS[p] for p in HEADLESS] == [8, 4, 14, 6, 4] and max(SPINE_ROWS.values()) == 17 and SPINE_ROWS[286] == 17 and SPINE_ROWS[269] == 14
# THE TAILS AND THE EDGES (the split's print): 221's rows carry no word of 22:1; 222:1 opens on Exodus 23:5; the chapter edges 245|246, 267|268, 285|286 and the portion edge 296|297 clean — each first row opens with its verse's citation, each last row is the chapter's own
assert not any(w in HB0(221, r) for r in range(1, 11) for w in ('לא תראה את שור', 'שור אחיך או את שיו')) and HB0(222, 1).startswith('(שמות כג ה) ״כי תראה״') and HB0(246, 1).startswith('(דברים כג א) לא יקח איש את אשת אביו') and HB0(268, 1).startswith('(דברים כד א) כי יקח איש אשה ובעלה') and HB0(286, 1).startswith('(דברים כה א) כי יהיה ריב בין אנשים') and HB0(297, 1).startswith('(דברים כו א) והיה כי תבוא אל הארץ'), (HB0(222, 1)[:40], HB0(246, 1)[:40], HB0(268, 1)[:40], HB0(286, 1)[:40], HB0(297, 1)[:40])
assert HB0(245, 7).startswith('לא יוכל שלחה כל ימיו') and HB0(267, 4).startswith('וחרמש לא תניף') and HB0(285, 4).startswith('גר יתום') and HB0(296, 9).startswith('תמחה את זכר עמלק') and not any('לא יקח איש את אשת אביו' in HB0(245, r) for r in range(1, 8)) and not any('כי יקח איש אשה ובעלה' in HB0(267, r) for r in range(1, 5)) and not any('כי יהיה ריב בין אנשים' in HB0(285, r) for r in range(1, 5)) and not any('והיה כי תבוא אל הארץ' in HB0(296, r) for r in range(1, 10)), (HB0(245, 7)[:40], HB0(267, 4)[:40], HB0(285, 4)[:40], HB0(296, 9)[:40])
assert HB0(236, 1).startswith('לאשה וישנאה (דברים כב יז)') and HB0(269, 1).startswith('והיה אם לא תמצא חן בעיניו') and HB0(283, 1).startswith('ושכחת עמר') and HB0(295, 1).startswith('למען יאריכון ימיך'), (HB0(236, 1)[:40], HB0(269, 1)[:40], HB0(283, 1)[:40], HB0(295, 1)[:40])   # the four headless piskaot open inside their verses (the fifth, 222, on Exodus 23:5)
assert all(clean(sif[p - 1][0]).startswith('Pisqa’ %d' % p) for p in PISKAOT) and 'When you see' in clean(sif[221][0])[:100] and 'To be his wife, but now he hates her' in clean(sif[235][0])[:100] and 'In the event that she doesn’t please him' in clean(sif[268][0])[:100] and 'And you forgot a sheaf' in clean(sif[282][0])[:100] and 'So that you may extend your days' in clean(sif[294][0])[:100], (clean(sif[221][0])[:60], clean(sif[235][0])[:60], clean(sif[268][0])[:60], clean(sif[282][0])[:60], clean(sif[294][0])[:60])   # EVERY piska's English first row opens with the translator's "Pisqa’ NNN" prefix and its page numbers (the heads table strips it) — the first pass read the quote as the opening (sitting 16's lesson 4 again); the headless piskaot's English openings follow the prefix
# THE CITATIONS PARSED FROM THE FOUR DUMPS' PRINTS (the instrument's own lists read back): the row-citations per file, the distinct rows, the union, the outside sets before the headless join
import ast as _ast
_DUMP = {}
for _c in CHS:
    _t = open(f'{SP_DIR}/ch{_c}_dump0.out', encoding='utf-8').read() if 'SP_DIR' in dir() else open(os.path.join(os.path.dirname(os.path.abspath(__file__)), f'ch{_c}_dump0.out'), encoding='utf-8').read()
    _he = _ast.literal_eval(re.search(r'^  HE rows citing Deut %d[^:]*: \d+ (\[.*\])$' % _c, _t, re.M).group(1)); _en = _ast.literal_eval(re.search(r'^  EN rows citing Deut %d[^:]*: \d+ (\[.*\])$' % _c, _t, re.M).group(1))
    _out = _ast.literal_eval(re.search(r'^  the rows OUTSIDE the spine piskaot [^:]*: \d+ (\[.*?\]) \|', _t, re.M).group(1))
    _DUMP[_c] = (len(_he), len({(p, r) for p, r, _, _ in _he}), len(_en), len({(p, r) for p, r, _, _ in _en}), len({(p, r) for p, r, _, _ in _he} | {(p, r) for p, r, _, _ in _en}), _out)
assert {c: v[:5] for c, v in _DUMP.items()} == {22: (37, 35, 223, 138, 138), 23: (34, 31, 156, 96, 98), 24: (26, 26, 144, 97, 98), 25: (24, 21, 149, 76, 76)}, {c: v[:5] for c, v in _DUMP.items()}
assert [len(v[5]) for v in _DUMP.values()] == [11, 5, 21, 8] and sorted({k for v in _DUMP.values() for k in v[5] if k[0] not in PISKAOT}) == OUTSIDE and sorted({k for v in _DUMP.values() for k in v[5] if k[0] in PISKAOT}) == [(222, 3), (222, 4), (222, 5), (222, 6), (222, 7), (222, 8), (233, 3), (236, 1), (236, 3), (236, 4), (254, 4), (269, 1), (269, 2), (269, 3), (269, 4), (269, 5), (269, 6), (269, 7), (269, 13), (269, 14), (270, 8), (283, 1), (283, 2), (283, 3), (283, 4), (283, 5), (283, 6), (295, 1), (295, 2), (295, 3), (295, 4)], [len(v[5]) for v in _DUMP.values()]   # the headless piskaot's citing rows sat among the dumps' outside sets and joined the spine at the split, and three spine rows of other chapters citing chapter 25 (233:3 the mingled stuff's levirate, 254:4 the camp's, 270:8 the divorce's) with them; the fourteen true outside rows
assert len(OUTSIDE) == 14 and len(PRIOR_READ) == 10 and len(FRESH) == 4 and sorted(list(PRIOR_READ) + FRESH) == sorted(OUTSIDE) and all(CITED[k] for k in OUTSIDE) and {k[0] for k in OUTSIDE} == set(HEADS_ON) and [k for k in OUTSIDE if CITED[k] == [(23, 12)]] == [(352, 8), (352, 9), (352, 10), (352, 17)]
# THE PARSER on every verse (the I section of the four dumps and the measure's E): fifteen hits — eleven number verses and four ordinals
with contextlib.redirect_stdout(io.StringIO()):
    import cold_run_sequence as _CS
_PARSE = {}
for _c, _v in SPAN:
    _vw = _CS.verse_words('Deut', _c, _v); _n, _o = _CS.ink_numbers(_vw), _CS.ink_ordinals(_vw); _marked = [t for t in _vw if t[-1] in '#~^%@|*']
    if _n or _o or _marked: _PARSE[(_c, _v)] = (_n, _o, _marked)
assert _PARSE == {(22, 12): ([4], [], []), (22, 19): ([100], [], []), (22, 22): ([2], [], ['שני#']), (22, 24): ([2], [], ['שני#']), (22, 29): ([50], [], []), (23, 3): ([], [10], []), (23, 4): ([], [10], []), (23, 9): ([], [3], []), (23, 17): ([1], [], []), (23, 19): ([2], [], ['שני#']), (24, 4): ([], [1], []), (24, 5): ([1], [], []), (25, 3): ([40], [], []), (25, 5): ([1], [], []), (25, 11): ([1], [], ['האחד#'])}, _PARSE
assert _CS.verse_words('Deut', 22, 12)[4] == 'ארבע' and _CS.verse_words('Deut', 25, 3)[0] == 'ארבעים' and _CS.verse_words('Deut', 23, 3)[7] == 'עשירי' and _CS.verse_words('Deut', 24, 4)[3] == 'הראשון' and _CS.verse_words('Deut', 22, 22)[10] == 'שני#'
# THE STORE AND THE TOKENS: the store differs from the DB at ELEVEN verses of chapter 22 and nowhere else — every difference the count of "the girl" written without its final letter (the store carries the read form beside it); 22:19 alone writes her in full
assert STORE_MISMATCH == [(22, 15, 14, 12), (22, 16, 13, 12), (22, 20, 10, 9), (22, 21, 23, 22), (22, 23, 12, 11), (22, 24, 32, 31), (22, 25, 19, 18), (22, 26, 21, 19), (22, 27, 10, 9), (22, 28, 13, 12), (22, 29, 20, 19)] and all(s - d == sum(1 for x in W(c, v) if x in ('הנער', 'לנער', 'ולנער', 'נער')) for c, v, s, d in STORE_MISMATCH), [(c, v, s - d, [x for x in W(c, v) if 'נער' in x]) for c, v, s, d in STORE_MISMATCH]
assert [v for v in range(1, 30) if 'הנערה' in W22(v)] == [19] and [v for v in range(1, 30) if any(x in ('הנער', 'לנער', 'נער') for x in W22(v))] == [15, 16, 20, 21, 23, 24, 25, 26, 27, 28, 29] and [s for s in U('הנער', 'הנערה', 'לנער', 'לנערה', 'נער', 'נערה', books=T) if s.startswith('Deut')] == ['Deut 22:%d' % v for v in (15, 16, 19, 20, 21, 23, 24, 25, 26, 27, 28, 29)]
assert {c: sum(len(W(c, v)) for v in range(1, NV[c] + 1)) for c in CHS} == {22: 437, 23: 339, 24: 327, 25: 260} and {c: len({g for (cc, v) in SG if cc == c for _, _, g in SG[(cc, v)]}) for c in CHS} == {22: 222, 23: 191, 24: 194, 25: 168} and [(c, v, hp) for (c, v) in SG for _, hp, g in SG[(c, v)] if g == '?'] == [(23, 5, 'ארם'), (24, 18, 'אנכי'), (24, 22, 'אנכי')]
# THE KIN BY COMPUTATION (the measure's A): the closest verses of the Bible to each; five verses with no kin of two shared tokens
assert KINC[(24, 16)][0] == ('2Kgs 14:6', 6, 12) and KINC[(24, 18)][0] == ('Deut 15:15', 7, 14) and KINC[(24, 22)][0] == ('Deut 15:15', 7, 13) and KINC[(23, 3)][0] == ('Deut 23:4', 4, 11) and KINC[(22, 19)][0] == ('Deut 22:29', 7, 8) and KINC[(24, 1)][0] == ('Deut 24:3', 7, 8) and KINC[(25, 15)][:2] == [('Deut 5:16', 4, 8), ('Exod 20:12', 4, 9)] and KINC[(24, 9)][0] == ('Deut 25:17', 5, 7) and KINC[(23, 5)][0] == ('Neh 13:2', 4, 6) and KINC[(24, 2)][0] == ('Jer 3:1', 4, 4) and KINC[(22, 24)][0] == ('Deut 17:5', 6, 5), (KINC[(24, 16)][0], KINC[(24, 18)][0], KINC[(23, 3)][0], KINC[(22, 19)][0], KINC[(24, 1)][0])
assert [k for k in SPAN if KINC[k] == []] == [(22, 10), (23, 7), (24, 6), (24, 10), (25, 4)], [k for k in SPAN if KINC[k] == []]   # the ox and ass plowing, seek not their peace, the millstone, the loan, the muzzle — no verse of the Bible shares two of their words
# THE TWINS DIFFED (the measure's B): the verse Kings quotes whole, the twin refrains, the bill's clause verbatim, the abomination's run, the assembly's run, the gift formula, Amalek's memory, the seducer of Exodus
assert SHN(DV(24, 16), ('2Kgs', 14, 6)) == 12 and len(words('Deut', 24, 16)) == 13 and SHARED(DV(24, 16), ('2Kgs', 14, 6)) == ['לא', 'יומתו', 'אבות', 'על', 'בנים', 'ובנים', 'לא', 'יומתו', 'על', 'אבות'] and 'ככתוב' in words('2Kgs', 14, 6) and 'משה' in words('2Kgs', 14, 6), SHARED(DV(24, 16), ('2Kgs', 14, 6))   # Kings quotes 24:16 "as written in the book of the law of Moses" — ten words in a run
assert SHN(DV(24, 18), ('Deut', 15, 15)) == 14 and len(words('Deut', 24, 18)) == 17 == len(words('Deut', 15, 15)) and SHN(DV(24, 22), ('Deut', 15, 15)) == 13 and SHN(DV(24, 18), ('Deut', 24, 22)) == 12 and SHARED(DV(24, 18), ('Deut', 24, 22)) == ['על', 'כן', 'אנכי', 'מצוך', 'לעשות', 'את', 'הדבר', 'הזה'] and SHN(DV(24, 18), ('Deut', 5, 15)) == 11
assert SHN(DV(24, 1), ('Deut', 24, 3)) == 8 and SHARED(DV(24, 1), ('Deut', 24, 3)) == ['וכתב', 'לה', 'ספר', 'כריתת', 'ונתן', 'בידה', 'ושלחה', 'מביתו'] and SHN(DV(22, 5), ('Deut', 25, 16)) == 7 and SHARED(DV(22, 5), ('Deut', 25, 16)) == ['כי', 'תועבת', 'יהוה', 'אלהיך', 'כל', 'עשה', 'אלה'] and SHN(DV(23, 3), ('Deut', 23, 4)) == 11 and SHARED(DV(23, 3), ('Deut', 23, 4)) == ['בקהל', 'יהוה', 'גם', 'דור', 'עשירי', 'לא', 'יבא']
assert SHN(DV(24, 4), ('Deut', 21, 23)) == 10 and SHARED(DV(24, 4), ('Deut', 21, 23)) == ['אשר', 'יהוה', 'אלהיך', 'נתן', 'לך', 'נחלה'] and SHN(DV(25, 15), ('Deut', 5, 16)) == 8 and SHARED(DV(25, 15), ('Deut', 5, 16)) == ['על', 'האדמה', 'אשר', 'יהוה', 'אלהיך', 'נתן', 'לך'] and SHN(DV(25, 19), ('Exod', 17, 14)) == 6 and SHARED(DV(25, 19), ('Exod', 17, 14)) == ['את', 'זכר', 'עמלק', 'מתחת', 'השמים'] and SHN(DV(24, 9), ('Deut', 25, 17)) == 7 and SHARED(DV(24, 9), ('Deut', 25, 17)) == ['זכור', 'את', 'אשר', 'עשה']
assert SHN(DV(22, 28), ('Exod', 22, 15)) == 7 and SHARED(DV(22, 28), ('Exod', 22, 15)) == ['בתולה', 'אשר', 'לא', 'ארשה'] and SHN(DV(22, 29), ('Exod', 22, 16)) == 1 and SHN(DV(22, 19), ('Deut', 22, 29)) == 8 and SHARED(DV(22, 19), ('Deut', 22, 29)) == ['ולו', 'תהיה', 'לאשה'] and SHN(DV(22, 1), ('Deut', 22, 4)) == 7 and SHARED(DV(22, 1), ('Deut', 22, 4)) == ['לא', 'תראה', 'את'] and SHN(DV(22, 1), ('Exod', 23, 4)) == 3 and SHN(DV(22, 4), ('Exod', 23, 5)) == 3
assert SHN(DV(22, 22), ('Lev', 20, 10)) == 1 and SHN(DV(22, 22), ('Lev', 18, 20)) == 0 and SHN(DV(23, 2), ('Lev', 21, 20)) == 0 and SHN(DV(25, 3), ('Exod', 21, 20)) == 0 and SHN(DV(24, 9), ('Num', 12, 10)) == 0 and SHN(DV(24, 9), ('Num', 12, 15)) == 0 and SHN(DV(25, 5), ('Gen', 38, 8)) == 1 and SHN(DV(23, 15), ('Lev', 26, 12)) == 0 and SHN(DV(24, 2), ('Lev', 21, 7)) == 0   # the restatements that share no words with their kin: the adulterer, the crushed, the rod, Miriam, the levirate of Judah, the walking God, the divorced woman of the priests' law
assert SHN(DV(24, 17), ('Deut', 16, 19)) == 4 and SHARED(DV(24, 17), ('Deut', 16, 19)) == ['לא', 'תטה', 'משפט'] and SHARED(DV(24, 17), ('Exod', 23, 6)) == ['לא', 'תטה', 'משפט'] and SHN(DV(24, 15), ('Deut', 15, 9)) == 7 and SHARED(DV(24, 15), ('Deut', 15, 9)) == ['עליך', 'אל', 'יהוה', 'והיה', 'בך', 'חטא'] and SHN(DV(23, 22), ('Eccl', 5, 3)) == 5 and SHARED(DV(23, 22), ('Eccl', 5, 3)) == ['תאחר', 'לשלמו', 'כי'] and SHN(DV(24, 19), ('Deut', 14, 29)) == 7 and SHN(DV(22, 21), ('Deut', 21, 21)) == 5 and SHN(DV(22, 24), ('Deut', 17, 5)) == 5 and SHARED(DV(22, 24), ('Deut', 17, 5)) == ['באבנים', 'ומתו']
# THE FORMULAS (the measure's C): the abomination formula eight times, all in this book; the purge formula's last four seats (22:21, 22:22, 22:24, 24:7 — nine of "the evil" and 19:13's "innocent blood"); "sin in you" three times; the gift formula eight
assert P('תועבת', 'יהוה', books=T) == ['Deut 12:31', 'Deut 17:1', 'Deut 18:12', 'Deut 22:5', 'Deut 23:19', 'Deut 25:16', 'Deut 27:15', 'Deut 7:25'] and len(P('תועבת', 'יהוה', books=None)) == 19 and P('כל', 'עשה', 'אלה', books=T) == ['Deut 18:12', 'Deut 22:5', 'Deut 25:16'] and U('תועבה', 'תועבת', 'התועבת', 'תועבות', books=('Deut',)) == ['Deut 12:31', 'Deut 14:3', 'Deut 17:1', 'Deut 18:12', 'Deut 22:5', 'Deut 23:19', 'Deut 24:4', 'Deut 25:16', 'Deut 27:15', 'Deut 7:25', 'Deut 7:26']
assert P('ובערת', 'הרע', 'מקרבך', books=T) == ['Deut 13:6', 'Deut 17:7', 'Deut 19:19', 'Deut 21:21', 'Deut 22:21', 'Deut 22:24', 'Deut 24:7'] and P('ובערת', 'הרע', 'מישראל', books=T) == ['Deut 17:12', 'Deut 22:22'] and U('ובערת', 'תבערו', 'ובערתם', books=T) == ['Deut 13:6', 'Deut 17:12', 'Deut 17:7', 'Deut 19:13', 'Deut 19:19', 'Deut 21:21', 'Deut 22:21', 'Deut 22:22', 'Deut 22:24', 'Deut 24:7', 'Exod 35:3']   # Exodus 35:3 "you shall not kindle" the root's homograph; the formula's nine seats end at 24:7
assert P('בך', 'חטא', books=T) == ['Deut 15:9', 'Deut 23:22', 'Deut 23:23', 'Deut 24:15'] and P('והיה', 'בך', 'חטא', books=T) == ['Deut 15:9', 'Deut 23:22', 'Deut 24:15'] and P('נתן', 'לך', 'נחלה', books=T) == ['Deut 15:4', 'Deut 19:10', 'Deut 20:16', 'Deut 21:23', 'Deut 24:4', 'Deut 25:19', 'Deut 26:1', 'Deut 4:21'] and P('נחלה', 'לרשתה', books=T) == ['Deut 15:4', 'Deut 25:19'] and P('מתחת', 'השמים', books=T) == ['Deut 25:19', 'Deut 29:19', 'Deut 7:24', 'Deut 9:14', 'Exod 17:14', 'Gen 1:9', 'Gen 6:17'] and P('לא', 'תשכח', books=T) == ['Deut 25:19', 'Deut 31:21']
assert P('באחד', 'שעריך', books=T) == ['Deut 15:7', 'Deut 16:5', 'Deut 17:2', 'Deut 23:17'] and P('לא', 'תחוס', 'עינך', books=T) == ['Deut 19:13', 'Deut 25:12'] and P('לגר', 'ליתום', 'ולאלמנה', books=T) == ['Deut 24:19', 'Deut 24:20', 'Deut 24:21', 'Deut 26:12'] and P('בדרך', 'בצאתכם', 'ממצרים', books=T) == ['Deut 23:5', 'Deut 24:9', 'Deut 25:17'] and P('ערות', 'דבר', books=T) == ['Deut 23:15', 'Deut 24:1'] and P('ספר', 'כריתת', books=None) == ['Deut 24:1', 'Deut 24:3'] and P('לא', 'יומתו', 'אבות', 'על', 'בנים', books=None) == ['2Kgs 14:6', 'Deut 24:16']   # "on the way when you came out of Egypt" the three remembrances' one phrase (Balaam, Miriam, Amalek)
assert P('בעלת', 'בעל', books=T) == ['Deut 22:22', 'Gen 20:3'] and P('נבלה', 'בישראל', books=None) == ['Deut 22:21', 'Jer 29:23', 'Josh 7:15'] and P('בתולת', 'ישראל', books=None) == ['Amos 5:2', 'Deut 22:19', 'Jer 18:13', 'Jer 31:21', 'Jer 31:4'] and P('בקהל', 'יהוה', books=None) == ['Deut 23:2', 'Deut 23:3', 'Deut 23:4', 'Deut 23:9', 'Mic 2:5'] and P('ממזר', books=None) == ['Deut 23:3', 'Zech 9:6'] and P('אבן', 'ואבן', books=None) == ['Deut 25:13', 'Prov 20:10', 'Prov 20:23'] and P('אתנן', 'זונה', books=None) == ['Deut 23:19', 'Mic 1:7'] and len(P('עני', 'ואביון', books=None)) == 13 and P('עני', 'ואביון', books=T) == ['Deut 24:14']   # "married to a husband" is Sarah's phrase (Genesis 20:3)
assert P('עד', 'עולם', books=T) == ['Deut 12:28', 'Deut 23:4', 'Deut 28:46', 'Deut 29:28', 'Exod 12:24', 'Exod 14:13', 'Gen 13:15'] and len(P('עד', 'עולם', books=None)) == 57 and len(P('מחוץ', 'למחנה', books=T)) == 27 and P('כלאים', books=None) == ['Deut 22:9', 'Isa 42:22', 'Lev 19:19'] and P('שעטנז', books=None) == ['Deut 22:11', 'Lev 19:19'] and P('גדלים', books=T) == ['Deut 11:23', 'Deut 22:12', 'Deut 4:34', 'Deut 4:38', 'Deut 6:22', 'Deut 9:1', 'Exod 6:6', 'Exod 7:4', 'Gen 12:17'] and P('מעקה', books=None) == ['Deut 22:8'] and P('בית', 'חדש', books=None) == ['Deut 20:5', 'Deut 22:8'] and P('ויסרו', 'אתו', books=None) == ['Deut 21:18', 'Deut 22:18'] and P('גם', 'שניהם', books=T) == ['Deut 22:22', 'Deut 23:19']   # "tassels" (gedilim) is the consonants of "great" — eight seats of "great nations/plagues" beside 22:12
assert [(c, v, x) for c, v in SPAN for x in W(c, v) if x.startswith('אח') and 'אחר' not in x and x not in ('אחת', 'אחד', 'האחת', 'והאחת', 'האחד', 'אחרי')] == [(22, 1, 'אחיך'), (22, 2, 'אחיך'), (22, 2, 'אחיך'), (22, 3, 'אחיך'), (22, 4, 'אחיך'), (23, 8, 'אחיך'), (25, 3, 'אחיך'), (25, 5, 'אחים'), (25, 6, 'אחיו'), (25, 9, 'אחיו')] and [(c, v) for c, v in SPAN for x in W(c, v) if x in ('רעך', 'רעהו', 'לרעך', 'ברעהו')] == [(22, 24), (22, 26), (23, 25), (23, 26), (23, 26)] and [(c, v) for c, v in SPAN for x in W(c, v) if 'מצרים' in x or x == 'מצרי'] == [(23, 5), (23, 8), (24, 9), (24, 18), (24, 22), (25, 17)] and [(c, v) for c, v in SPAN for x in W(c, v) if 'ישראל' in x] == [(22, 19), (22, 21), (22, 22), (23, 18), (23, 18), (24, 7), (25, 6), (25, 7), (25, 10)]
assert [(c, v, x) for c, v in SPAN for x in W(c, v) if x in ('ומתו', 'ומת', 'מות', 'יומתו', 'יומת', 'המת', 'ומתה', 'תמות')] == [(22, 21, 'ומתה'), (22, 22, 'ומתו'), (22, 24, 'ומתו'), (22, 25, 'ומת'), (22, 26, 'מות'), (24, 7, 'ומת'), (24, 16, 'יומתו'), (24, 16, 'יומתו'), (24, 16, 'יומתו'), (25, 5, 'ומת'), (25, 5, 'המת'), (25, 6, 'המת')] and [(c, v) for c, v in SPAN for x in W(c, v) if 'סקל' in x] == [(22, 21), (22, 24)] and [(c, v) for c, v in SPAN for x in W(c, v) if x in ('ענה', 'עניתה', 'וענה')] == [(22, 24), (22, 29)] and [(c, v, x) for c, v in SPAN for x in W(c, v) if x in ('זכור', 'וזכרת', 'זכר')] == [(24, 9, 'זכור'), (24, 18, 'וזכרת'), (24, 22, 'וזכרת'), (25, 17, 'זכור'), (25, 19, 'זכר')]
assert [(c, v, x) for c, v in SPAN for x in W(c, v) if x.startswith(('שלח', 'לשלח', 'ושלח', 'תשלח'))] == [(22, 7, 'שלח'), (22, 7, 'תשלח'), (22, 19, 'לשלחה'), (22, 29, 'שלחה'), (24, 1, 'ושלחה'), (24, 3, 'ושלחה'), (24, 4, 'שלחה'), (25, 11, 'ושלחה')] and 'לשלחה' in W22(19) and 'שלחה' in W22(29) and 'לשלחה' not in W22(29)   # "send her away" with the lamed at 22:19 and without it at 22:29 — the two forms of the same clause (the spine reads the difference)
# THE FRAMES (the measure's E): the Name absent from chapter 22 but at 22:5; the plural "you" in five verses; seven infinitive absolutes; one imperative; one "saying"
assert [v for v in range(1, 30) if any('יהוה' in x for x in W22(v))] == [5] and sum(1 for v in range(1, 27) for x in W23(v) if x == 'יהוה') == 14 and sum(1 for v in range(1, 27) for x in W23(v) if x == 'ליהוה') == 2 and sum(1 for v in range(1, 23) for x in W24(v) if x == 'יהוה') == 7 and sum(1 for v in range(1, 20) for x in W25(v) if x == 'יהוה') == 4 and [(v, x) for v in range(1, 20) for x in W25(v) if x in ('אלהיו', 'אלהי', 'אלהים', 'אלהיכם')] == [(18, 'אלהים')] and [v for v in range(1, 27) if not any('יהוה' in x for x in W23(v))] == [1, 5, 7, 8, 10, 11, 12, 13, 14, 16, 17, 18, 20, 23, 25, 26] and [v for v in range(1, 23) if not any('יהוה' in x for x in W24(v))] == [1, 2, 3, 5, 6, 7, 8, 10, 11, 12, 14, 16, 17, 20, 21, 22] and [v for v in range(1, 20) if not any('יהוה' in x for x in W25(v))] == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 17, 18]
MO = {(c, v): [(x, m) for x, m in by[('Deut', c, v)]] for c, v in SPAN}
assert [k for k in SPAN if sum(1 for _, m in MO[k] if m and '2mp' in m)] == [(22, 24), (23, 5), (24, 8), (24, 9), (25, 17)] and [(c, v, x) for c, v in SPAN for x, m in MO[(c, v)] if m and re.search(r'V[a-zA-Z]a$', m)] == [(22, 1, 'השב'), (22, 4, 'הקם'), (22, 7, 'שלח'), (23, 22, 'דרש'), (24, 9, 'זכור'), (24, 13, 'השב'), (25, 17, 'זכור')] and [(c, v, x) for c, v in SPAN for x, m in MO[(c, v)] if m and re.search(r'V[a-zA-Z]w', m)] == [(22, 14, 'ואקרב'), (22, 16, 'וישנאה'), (23, 6, 'ויהפך'), (24, 18, 'ויפדך'), (25, 18, 'ויזנב')] and [(c, v, x) for c, v in SPAN for x, m in MO[(c, v)] if m and re.search(r'V[a-zA-Z]v', m)] == [(24, 8, 'השמר')]
assert [f'{c}:{v}' for c, v in SPAN if 'לאמר' in W(c, v)] == ['22:17'] and [f'{c}:{v}' for c, v in SPAN if 'למען' in W(c, v)] == ['22:7', '23:21', '24:19', '25:15'] and [f'{c}:{v}' for c, v in SPAN if any(x in ('פן', 'ופן') for x in W(c, v))] == ['22:9', '25:3'] and [(c, v, x) for c, v in SPAN for x, m in MO[(c, v)] if m and '1c' in m and m.startswith('HV')] == [(22, 14, 'לקחתי'), (22, 14, 'מצאתי'), (22, 16, 'נתתי'), (22, 17, 'מצאתי'), (24, 8, 'צויתם'), (25, 7, 'יבמי'), (25, 8, 'חפצתי')]
# THE REGISTER (the measure's E): no receipt, footer or header in the four chapters; nine receipts in the book so far, 20:17 the last
with contextlib.redirect_stdout(io.StringIO()):
    import register_census as _RC
    _ink = _RC.read_ink()
assert [k for k in _RC.receipts(_ink) if k[0] == 'Deut' and k[1] in CHS] == [] and [x for x in _RC.footers(_ink) if x[0][0] == 'Deut' and x[0][1] in CHS] == [] and [x for x in _RC.register_headers(_ink) if x[0][0] == 'Deut' and x[0][1] in CHS] == [] and [k for k in _RC.receipts(_ink) if k[0] == 'Deut' and k[1] <= 25] == [('Deut', 1, 3), ('Deut', 1, 19), ('Deut', 1, 41), ('Deut', 4, 5), ('Deut', 5, 12), ('Deut', 5, 16), ('Deut', 5, 32), ('Deut', 10, 5), ('Deut', 20, 17)]
# ONKELOS (the measure's D): the bill of divorce named "get piturin", the man's gear "weapons", the harlot and the sodomite "a slave man" and "a slave woman", the assembly's "shall not be fit", "transgression of a word" for the unseemly thing, the Shekhinah walking and the Memra turning, the export's two "another reading" marks
assert ARM(22, 5)[:5] == ['לא', 'יהי', 'תקון', 'זין', 'דגבר'] and ARM(22, 12)[0] == 'כרספדין' and 'סלעין' in ARM(22, 19) and ARM(22, 19)[-6:] == ['לית', 'ליה', 'רשו', 'למפטרה', 'כל', 'יומוהי'] and 'חובת' in ARM(22, 26) and 'דקטול' in ARM(22, 26) and ARM(22, 21)[-4:] == ['ותפלי', 'עבד', 'דביש', 'מבינך'], (ARM(22, 5)[:5], ARM(22, 19)[-6:], ARM(22, 21)[-4:])
assert ARM(23, 2)[:2] == ['לא', 'ידכי'] and ARM(23, 3)[:3] == ['לא', 'ידכי', 'ממזרא'] and SEATS('בקהלא דיי') == [(23, 2), (23, 3), (23, 4), (23, 9)] and ARM(23, 18) == ['לא', 'תהי', 'אתתא', 'מבנת', 'ישראל', 'לגבר', 'עבד', 'ולא', 'יסב', 'גברא', 'מבני', 'ישראל', 'אתתא', 'אמא'] and 'מקדשא' in ARM(23, 19) and ARM(23, 20).count('רבית') == 3 and 'שכנתיה' in ARM(23, 15) and 'מהלכא' in ARM(23, 15) and ARM(23, 15)[-4:] == ['ויתוב', 'מימריה', 'מלאוטבא', 'לך'], (ARM(23, 18), ARM(23, 15)[-4:])
assert SEATS('גט פטורין') == [(24, 1), (24, 3)] and SEATS('עברת פתגם') == [(23, 15), (24, 1)] and 'אחסנא' in ARM(24, 4) and 'מרחקא' in ARM(24, 4) and ARM(24, 8)[:3] == ['אסתמר', 'במכתש', 'סגירו'] and 'זכותא' in ARM(24, 13) and ARM(24, 15)[-3:] == ['בך', 'חובא'][-2:] + [] if False else ARM(24, 15)[-2:] == ['בך', 'חובא'] and SEATS('משכונ') == [(24, 6), (24, 10), (24, 11), (24, 12), (24, 13), (24, 17)] and SEATS('מרים') == [(24, 9)] and SEATS('סגירו') == [(17, 8), (21, 5), (24, 8)]
assert ARM(25, 1)[:3] == ['ארי', 'יהי', 'דין'] and 'לדינא' in ARM(25, 1) and ARM(25, 3)[:2] == ['ארבעין', 'ילקניה'] and 'סיניה' in ARM(25, 9) and 'ותרוק' in ARM(25, 9) and 'דאחוהי' == ARM(25, 9)[-1] and ARM(25, 12) == ['ותקוץ', 'ית', 'ידה', 'לא', 'תחוס', 'עינך'] and SEATS('עמלק') == [(25, 17), (25, 19)] and SEATS('מתקל') == [(25, 13), (25, 15)] and SEATS('מכיל') == [(25, 14), (25, 15)] and ARM(25, 18)[-5:] == ['ולא', 'דחיל', 'מן', 'קדם', 'יי']
assert {(22, 15), (25, 5)} <= set(SEATS('נ"א')) and 'נ"א' in ARM(22, 15) and ARM(22, 15)[1:4] == ['אבוהא', 'נ"א', 'אבוהי'] and 'נ"א' in ARM(25, 5) and ARM(25, 5)[16:19] == ['אוחרן', 'נ"א', 'חלוני'], (SEATS('נ"א'), ARM(22, 15)[:5], ARM(25, 5)[15:20])   # the export carries "another reading" (nusach acher) marks inside the Aramaic at 22:15 (the father's suffix) and 25:5 ("a strange man" / "an outsider")
assert SEATS('מרחק') == [(7, 25), (7, 26), (12, 31), (14, 3), (17, 1), (18, 12), (22, 5), (23, 19), (24, 4), (25, 16), (27, 15)] and SEATS('בתול') == [(22, 14), (22, 15), (22, 17), (22, 19), (22, 20)] and SEATS('סבי קרתא') == [(21, 3), (21, 4), (21, 6), (22, 15), (22, 17), (22, 18)] and SEATS('בלעם') == [(23, 5), (23, 6)] and len(SEATS('גיור')) == 17 and len(SEATS('שכנת')) == 23 and (23, 15) in SEATS('שכנת') and len(SEATS('מימריה')) == 18 and (23, 15) in SEATS('מימריה') and SEATS('בית דינא') == [(25, 7)] and SEATS('ירגמ') == [(21, 21), (22, 21)]   # "distanced" (merachak) renders every "abomination" in the book — eleven seats, the four chapters' four among them
# THE PRIOR READS (computed from the ledgers): twelve spine rows read before at ten ledgers (two at Genesis 29's — the strife of Abram's herdsmen cited by 286:1 and 292:1), ten outside rows read before
TRI = f'{ROOT}/logic/oral_triage'
LED = {f: open(f'{TRI}/{f}', encoding='utf-8').read() for f in os.listdir(TRI) if f.endswith('.md') and os.path.isfile(f'{TRI}/{f}') and f != os.path.basename(OUT)}
SPINE_PRIOR = sorted({(f, int(a), int(b)) for f, t in LED.items() for a, b in re.findall(r'Sifrei Devarim (\d+):(\d+)', t) if int(a) in PISKAOT})
OUT_PRIOR = sorted({(f, int(a), int(b)) for f, t in LED.items() for a, b in re.findall(r'Sifrei Devarim (\d+):(\d+)', t) if (int(a), int(b)) in OUTSIDE})
assert SPINE_PRIOR == [('deu_05_vaetchanan_2026-09-16.md', 233, 1), ('deu_06_vaetchanan_2026-09-17.md', 258, 1), ('deu_12_reeh_2026-09-20.md', 286, 16), ('deu_14_reeh_2026-09-21.md', 228, 5), ('deu_15_reeh_2026-09-22.md', 279, 4), ('deu_16_reeh_shoftim_2026-09-23.md', 281, 1), ('deu_17_18_shoftim_2026-09-24.md', 261, 2), ('deu_19_21_shoftim_ki_teitzei_2026-09-24.md', 251, 1), ('deu_19_21_shoftim_ki_teitzei_2026-09-24.md', 259, 5), ('deu_19_21_shoftim_ki_teitzei_2026-09-24.md', 293, 2), ('gen_29_separation_promise_2026-08-25.md', 286, 1), ('gen_29_separation_promise_2026-08-25.md', 292, 1)], SPINE_PRIOR
assert OUT_PRIOR == [('deu_11_ekev_reeh_2026-09-20.md', 41, 3), ('deu_12_reeh_2026-09-20.md', 63, 5), ('deu_13_reeh_2026-09-21.md', 87, 3), ('deu_13_reeh_2026-09-21.md', 94, 3), ('deu_14_reeh_2026-09-21.md', 110, 1), ('deu_15_reeh_2026-09-22.md', 41, 3), ('deu_15_reeh_2026-09-22.md', 117, 5), ('deu_15_reeh_2026-09-22.md', 122, 1), ('deu_17_18_shoftim_2026-09-24.md', 155, 9), ('deu_17_18_shoftim_2026-09-24.md', 352, 9), ('deu_19_21_shoftim_ki_teitzei_2026-09-24.md', 190, 14)] and {(p, r): sorted(f for f, a, b in OUT_PRIOR if (a, b) == (p, r)) for p, r in PRIOR_READ} == PRIOR_READ, OUT_PRIOR
assert sorted(f for f, t in LED.items() if re.search(r'^- Onkelos (?:Deut (?:2[2-9]|3\d)|Josh|Judg|1Sam|2Sam|1Kgs|2Kgs|Isa|Jer|Ezek):', t, re.M)) == []   # never read ahead

import os as _os
_ROOT = _os.path.normpath(_os.path.join(_os.path.dirname(_os.path.abspath(__file__)), '..', '..', '..'))   # THE PORTABLE REPO (2026-09-15): the repo root from this file's own place
#!/usr/bin/env python3
# THE DEUTERONOMY WALK, sitting 18 — CHAPTERS 26-28, Deuteronomy 26:1-28:69 IN THE LEAN FORM (2026-09-26; the owner: "Continue" after sitting 17b's tail, no
# compaction between — THE LEAN PASS's ninth sitting, its fifth reading, the first on chapters WITHOUT A SPINE PISKA): THE INK of the three chapters, computed from
# the Tanakh DB, the snapshot store and the shelf's own bytes — never typed. Sitting 17's form (ch22_ink.py): the generic helpers copied by derive_ch26_ink.py
# from the forms' ch22_ink.py by content markers (the three chapters substituted for the four), the constants and every assert the three chapters' own, typed FROM
# THE PRINTS (ch26_dump0.out … ch28_dump0.out, ch26_split.out, ch26_measure_lean.out). THE TWO DIVISIONS AGREE in all three (19 = 19, cost 21; 26 = 26, cost 12;
# 69 = 69, cost 37) — the identity; the Hebrew's 28:69 is the English's 29:1 and the Onkelos export follows the Hebrew. THE SPINE IS ON CHAPTER 26 ALONE — SEVEN
# piskaot 297-303 with 77 rows (297 on 26:1 ten rows; 298 HEADLESS inside 26:2 "and place it in a basket" three; 299 HEADLESS inside 26:3 "and you shall say to
# him" four; 300 on 26:4 two; 301 on 26:5 thirty-seven; 302 on 26:12 one; 303 HEADLESS inside 26:13-15 "and you shall give it to the Levite" twenty); 296 on
# 25:17 before, 304 on 31:14 after — THE SIFREI HAS NO PISKA ON 26:16-31:13: CHAPTERS 27 AND 28 CARRY NO SPINE, their shelf Onkelos whole and the rows elsewhere
# citing them. TWENTY-SIX rows elsewhere cite the three chapters by the union of the three files (twenty-five READ BEFORE at chapters 6, 8, 11-17 and 22-25,
# REREAD WHOLE; one fresh — 347:3 on 27:20 from the blessing of Reuben). NO portion edge inside 26-28 (Ki Tavo 26:1-29:8 holds the three; 29:1-8 is sitting 19's).
# The parser MEASURED on every verse — 28:7 and 28:25 [1, 7] "one way … seven ways", 28:55 [1] "to one of them", 28:63 [6] READ "shesh" REJOICED AS SIX (the
# number's homograph — the parser's false hit, asserted so), 26:12 the tithe's two starred tokens (the ten's homograph, starred by the store); "swore" (nishba) at
# 26:3, 28:9, 28:11 the seven's homograph, not counted. The hand's facts as asserts, run all at once by assert_driver.py.
import json, os, re, html, sqlite3, sys, io, contextlib, unicodedata, subprocess
from collections import Counter
ROOT = _ROOT
sys.path.insert(0, f'{ROOT}/World/step9')
DATE = '2026-09-26'
CHS = (26, 27, 28)
UIDS = ['deu_26_bikkurim_close', 'deu_27_ebal_curses', 'deu_28_blessings', 'deu_28_curses_a', 'deu_28_curses_b']   # the drafts' own ids (the G prints): bikkurim = the firstfruits; five units over three chapters — chapter 28 in three (the blessings, the curses in two halves)
SPANS = {'deu_26_bikkurim_close': (26, 1, 19), 'deu_27_ebal_curses': (27, 1, 26), 'deu_28_blessings': (28, 1, 14), 'deu_28_curses_a': (28, 15, 44), 'deu_28_curses_b': (28, 45, 69)}
PREFIX = {'deu_26_bikkurim_close': 'DV26', 'deu_27_ebal_curses': 'DV27', 'deu_28_blessings': 'DV28A', 'deu_28_curses_a': 'DV28B', 'deu_28_curses_b': 'DV28C'}
SPAN = [(26, v) for v in range(1, 20)] + [(27, v) for v in range(1, 27)] + [(28, v) for v in range(1, 70)]
PISKAOT = list(range(297, 304))   # THE SPINE ON CHAPTER 26: seven piskaot (three headless) — the A prints and the split's; 296 heads on 25:17, 304 on 31:14
PISKAOT_BY = {26: list(range(297, 304)), 27: [], 28: []}
HEADLESS = [298, 299, 303]   # no book-named citation at their head (the dumps: "head None"; the split: 298:1 opens "and place it in a basket", 299:1 "and you shall say to him", 303:1 "and you shall give it to the Levite, the stranger, the orphan and the widow") — read WHOLE from the export
SPINE_ROWS = {297: 10, 298: 3, 299: 4, 300: 2, 301: 37, 302: 1, 303: 20}   # rows per piska, both files (the heads table and the split's print) — 77
PREV_CHAPTER_ROWS = []   # no tail folded in (296's rows carry no word of 26:1 — the split's assert; 303's last row cites 26:15 and 304:1 opens with 31:14's citation)
READ_ROWS = [(p, r) for p in PISKAOT for r in range(1, SPINE_ROWS[p] + 1)]   # 77 — this ledger's spine rows
EXP2DB = {26: {e: [e] for e in range(1, 20)}, 27: {e: [e] for e in range(1, 27)}, 28: {e: [e] for e in range(1, 70)}}   # the identity in all three chapters (chapter 5 the book's one split)
DB2EXP = {c: {d: e for e, ds in EXP2DB[c].items() for d in ds} for c in CHS}
# the Hebrew's book-named citations of the three chapters OUTSIDE the spine; six rows cite only in the English (104:8, 109:3, 109:5, 291:5, 291:6, 291:7)
OUTSIDE_HE = [(63, 9, (26, 4)), (72, 5, (26, 14)), (109, 1, (26, 12)), (109, 4, (26, 12)), (36, 2, (27, 8)), (55, 2, (27, 12)), (64, 2, (27, 7)), (69, 1, (27, 7)), (107, 16, (27, 7)), (138, 1, (27, 7)), (347, 3, (27, 20)), (40, 10, (28, 8)), (40, 11, (28, 20)), (40, 12, (28, 12)), (42, 8, (28, 48)), (43, 28, (28, 23)), (116, 1, (28, 3)), (148, 7, (28, 14)), (306, 4, (28, 12)), (306, 6, (28, 12))]
OUTSIDE = [(36, 2), (40, 10), (40, 11), (40, 12), (42, 8), (43, 28), (55, 2), (63, 9), (64, 2), (69, 1), (72, 5), (104, 8), (107, 16), (109, 1), (109, 3), (109, 4), (109, 5), (116, 1), (138, 1), (148, 7), (291, 5), (291, 6), (291, 7), (306, 4), (306, 6), (347, 3)]   # the TWENTY-SIX rows READ WHOLE: the union of the three files beyond piskaot 297-303, joined over the three dumps (the split's print)
EXCLUDED = [(291, 6), (291, 7)]   # RUN 2's find at the whole read: the English's "Dt.27:9" on 291:6 and 291:7 is the translator's misprint for 25:9 (the Hebrew is 25:9's own words, "thus shall be done to the man who will not build his brother's house"; 27:9 is "be silent and hear") — read whole, KEPT OUT of chapter 27's coverage (sitting 17's 352 precedent); the design listed 291:5-7 as three rows on 27
INTERPOLATION = []
CITED = {(36, 2): [(27, 3), (27, 8)], (40, 10): [(28, 3), (28, 5), (28, 6), (28, 8)], (40, 11): [(28, 16), (28, 17), (28, 19), (28, 20)], (40, 12): [(28, 12)], (42, 8): [(28, 48)], (43, 28): [(28, 23)], (55, 2): [(27, 12)], (63, 9): [(26, 4)], (64, 2): [(27, 7)], (69, 1): [(27, 7)], (72, 5): [(26, 14)], (104, 8): [(28, 1), (28, 69)], (107, 16): [(27, 6), (27, 7)], (109, 1): [(26, 12)], (109, 3): [(26, 12)], (109, 4): [(26, 12)], (109, 5): [(26, 12)], (116, 1): [(28, 3)], (138, 1): [(27, 7)], (148, 7): [(28, 14)], (291, 5): [(27, 15)], (291, 6): [(27, 9)], (291, 7): [(27, 9)], (306, 4): [(28, 12)], (306, 6): [(28, 12)], (347, 3): [(27, 20)]}
PRIOR_READ = {(36, 2): ['deu_06_vaetchanan_2026-09-17.md'], (40, 10): ['deu_08_ekev_2026-09-18.md', 'deu_11_ekev_reeh_2026-09-20.md'], (40, 11): ['deu_11_ekev_reeh_2026-09-20.md'], (40, 12): ['deu_11_ekev_reeh_2026-09-20.md'], (42, 8): ['deu_11_ekev_reeh_2026-09-20.md'], (43, 28): ['deu_11_ekev_reeh_2026-09-20.md'], (55, 2): ['deu_11_ekev_reeh_2026-09-20.md'], (63, 9): ['deu_12_reeh_2026-09-20.md'], (64, 2): ['deu_12_reeh_2026-09-20.md'], (69, 1): ['deu_12_reeh_2026-09-20.md'], (72, 5): ['deu_12_reeh_2026-09-20.md'], (104, 8): ['deu_06_vaetchanan_2026-09-17.md', 'deu_14_reeh_2026-09-21.md'], (107, 16): ['deu_14_reeh_2026-09-21.md'], (109, 1): ['deu_14_reeh_2026-09-21.md'], (109, 3): ['deu_14_reeh_2026-09-21.md', 'deu_15_reeh_2026-09-22.md'], (109, 4): ['deu_14_reeh_2026-09-21.md'], (109, 5): ['deu_14_reeh_2026-09-21.md'], (116, 1): ['deu_15_reeh_2026-09-22.md'], (138, 1): ['deu_12_reeh_2026-09-20.md', 'deu_16_reeh_shoftim_2026-09-23.md'], (148, 7): ['deu_17_18_shoftim_2026-09-24.md'], (291, 5): ['deu_22_25_ki_teitzei_2026-09-25.md'], (291, 6): ['deu_22_25_ki_teitzei_2026-09-25.md'], (291, 7): ['deu_22_25_ki_teitzei_2026-09-25.md'], (306, 4): ['deu_11_ekev_reeh_2026-09-20.md'], (306, 6): ['deu_11_ekev_reeh_2026-09-20.md']}   # the twenty-five outside rows read before (computed from the ledgers at the dumps' F, asserted) — REREAD WHOLE here
HEADS_ON = {36: (6, 9), 40: (11, 12), 42: (11, 14), 43: (11, 15), 55: (11, 29), 63: (12, 5), 64: (12, 7), 69: (12, 12), 72: (12, 17), 104: (14, 21), 107: (14, 24), 109: (14, 28), 116: (15, 6), 138: (16, 11), 148: (17, 2), 291: (25, 9), 306: (32, 1), 347: (33, 6)}
FRESH = [(347, 3)]
CREDITED = {}   # under THE WHOLE-ROW RULE no spine row is credited: the rows read before (297:4 at chapter 8; 301:4 at chapter 10; 301:21 at chapter 4) are REREAD WHOLE here and marked so
TITLE = "Chapters 26-28 — When you come into the land and possess it, take the first of all the fruit of the ground in a basket to the place He chooses; say to the priest 'I declare this day that I have come into the land He swore to our fathers'; he sets the basket before the altar; and you recite: 'A wandering Aramean was my father; he went down to Egypt few in number and became a great, mighty and many nation; the Egyptians dealt ill with us and laid hard bondage on us; we cried to the LORD, He heard our voice and saw our affliction, our toil and our oppression; He brought us out with a mighty hand and an outstretched arm, with great terror, with signs and wonders, and gave us this land flowing with milk and honey; and now I have brought the first of the fruit of the ground'; set it down, bow, rejoice in all the good with the Levite and the stranger. When you finish tithing all your produce in the third year, the year of the tithe, give it to the Levite, the stranger, the orphan and the widow, that they eat within your gates and are satisfied; then say before the LORD: 'I have removed the holy from the house and given it to them by all Your commandment; I have not transgressed nor forgotten; I have not eaten of it in my mourning nor removed it in uncleanness nor given of it for the dead; I have hearkened, I have done all You commanded; look down from Your holy habitation and bless Your people Israel and the ground You gave us as You swore, a land flowing with milk and honey.' This day the LORD commands you to keep these statutes with all your heart and soul; you have declared Him your God, to walk in His ways and hearken; and He has declared you His treasured people, to keep His commandments, and to set you high above all nations for praise, name and glory, a holy people, as He spoke. Moses and the elders command the people: keep all the commandment; on the day you cross the Jordan set up great stones, plaster them with plaster and write on them all the words of this law; on Mount Ebal build an altar of whole stones on which no iron was lifted, offer burnt offerings and peace offerings, eat and rejoice, and write on the stones very plainly. Moses and the priests the Levites: 'Be silent and hear, Israel: this day you have become the people of the LORD your God; hearken and do His commandments.' Six tribes stand on Gerizim to bless and six on Ebal for the curse; the Levites answer with a loud voice: cursed is the man who makes an image in secret; who dishonors father or mother; who moves his neighbor's landmark; who misleads the blind; who perverts the judgment of the stranger, the orphan and the widow; who lies with his father's wife, with any beast, with his sister, with his mother-in-law; who smites his neighbor in secret; who takes a bribe to slay innocent blood; who does not uphold the words of this law — and all the people say Amen. If you diligently hearken, all these blessings overtake you: blessed in the city and the field, the fruit of your womb, ground and beast, your basket and your kneading trough, your coming in and going out; your enemies come one way and flee seven; the blessing in your storehouses; He establishes you a holy people; all peoples fear you; He opens the heavens' good treasure, rain in its season; you lend and do not borrow, the head and not the tail, if you turn not aside to the right or the left. But if you will not hearken, all these curses overtake you: cursed in the city and the field, the basket and the trough, the fruit of womb, ground and beast, coming in and going out; the curse, confusion and rebuke; pestilence, consumption, fever, inflammation, sword, blight and mildew; the heavens brass and the earth iron, the rain dust; smitten before your enemies, one way out and seven ways fleeing, a horror to all the kingdoms; your carcass food for the birds; the boil of Egypt, the hemorrhoids, the scab and the itch; madness, blindness and astonishment of heart; you betroth a wife and another lies with her, build a house and dwell not in it, plant a vineyard and use not its fruit; your ox slain before your eyes, your ass robbed, your flock given to enemies; your sons and daughters given to another people; a nation you know not eats the fruit of your ground; mad from what your eyes see; sore boils from sole to crown; carried with your king to a nation you have not known, to serve wood and stone; an astonishment, a proverb and a byword; the locust eats your seed, the worm your vines, your olives drop; your sons go into captivity; the stranger rises above you — he lends to you, he the head and you the tail; all these curses pursue you until you are destroyed, because you served not with joy; you serve your enemies in hunger, thirst, nakedness and want, an iron yoke on your neck; a nation from the end of the earth as the eagle flies, of a fierce countenance, eats the fruit of your beast and ground and besieges you in all your gates until your high and fortified walls fall; you eat the fruit of your own womb in the siege and the distress — the tender man and the delicate woman grudge their own children the flesh they eat. If you keep not all the words of this law written in this book, to fear this glorious and awesome Name, He makes your plagues wonderful, great and lasting, brings back all the diseases of Egypt, every sickness not written in this book, until you are left few in number who had been as the stars of heaven; as He rejoiced to do you good, so He rejoices to destroy you; scattered among all peoples from the end of the earth to the end, serving wood and stone; no rest for the sole of your foot, a trembling heart, failing eyes and a languishing soul; your life hangs in doubt, in the morning 'would it were evening', in the evening 'would it were morning'; and the LORD brings you back to Egypt in ships by the way of which He said 'you shall not see it again', to be sold as slaves and none buys. These are the words of the covenant the LORD commanded Moses to cut with the children of Israel in the land of Moab, besides the covenant cut with them at Horeb"
OUT = f'{ROOT}/logic/oral_triage/deu_26_28_ki_tavo_{DATE}.md'
PATCHED = bool(os.environ.get('DEU26_PATCHED'))   # the tail's flag: after the manifest and the seat, the drafts carry operators and the store its overrides
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
def W26(v): return words('Deut', 26, v)
def W27(v): return words('Deut', 27, v)
def W28(v): return words('Deut', 28, v)
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
for c, v, idx, hp, g in store.execute("SELECT v.chapter, v.verse, w.idx, w.he_plain, w.gloss FROM words w JOIN verses v ON w.verse_id=v.id WHERE v.book='Deut' AND v.chapter IN (26, 27, 28) ORDER BY v.id, w.idx"):
    SG.setdefault((c, v), []).append((idx, hp.replace('/', ''), g))
def sg(c, v, tok, nth=0):
    hit = [g for _, hp, g in SG[(c, v)] if hp == tok]
    if len(hit) <= nth: raise KeyError((c, v, tok, nth))
    return hit[nth]
def sidx(c, v, tok, nth=0):
    hit = [i for i, hp, _ in SG[(c, v)] if hp == tok]
    assert len(hit) > nth, (c, v, tok, nth, hit)
    return hit[nth]
STORE_MISMATCH = [(c, v, n, len(by[('Deut', c, v)])) for c, v, n in store.execute("SELECT v.chapter, v.verse, COUNT(*) FROM words w JOIN verses v ON w.verse_id=v.id WHERE v.book='Deut' AND v.chapter IN (26, 27, 28) GROUP BY v.chapter, v.verse").fetchall() if n != len(by[('Deut', c, v)])]
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
# ---- THE SHELF BY POSITION — the spine ON chapter 26 alone: seven piskaot 297-303 (three HEADLESS); NO piska heads in chapters 27 and 28 (the Sifrei runs 303 on 26:15 to 304 on 31:14); 296 heads on 25:17 before, 304 on 31:14 after; the heads by chapter and the window 290-310 as the dumps printed them
assert NV == {26: 19, 27: 26, 28: 69} and VC[25] == 19 and len(sif) == 357 and len(sif_he) == 357 and sum(len(s) for s in sif) == 2357 and sum(len(s) for s in sif_he) == 2357
HC = Counter(h[0] for h in heads.values() if h)
assert (HC[26], HC[27], HC[28]) == (4, 0, 0) and sorted(HC.items()) == [(1, 24), (3, 4), (6, 6), (11, 21), (12, 20), (13, 14), (14, 14), (15, 16), (16, 19), (17, 16), (18, 16), (19, 10), (20, 14), (21, 17), (22, 22), (23, 22), (24, 16), (25, 10), (26, 4), (31, 1), (32, 36), (33, 14), (34, 1)], sorted(HC.items())
assert {p: heads[p] for p in range(290, 311)} == {290: (25, 8), 291: (25, 9), 292: (25, 11), 293: (25, 12), 294: (25, 13), 295: None, 296: (25, 17), 297: (26, 1), 298: None, 299: None, 300: (26, 4), 301: (26, 5), 302: (26, 12), 303: None, 304: (31, 14), 305: None, 306: (32, 1), 307: (32, 4), 308: (32, 5), 309: (32, 6), 310: (32, 7)}, {p: heads[p] for p in range(290, 311)}
HV = {c: [heads[p][1] for p in PISKAOT_BY[c] if heads[p]] for c in CHS}
assert HV == {26: [1, 4, 5, 12], 27: [], 28: []}, HV
NOHEAD = {c: [v for v in range(1, NV[c] + 1) if v not in HV[c]] for c in CHS}
assert NOHEAD == {26: [2, 3, 6, 7, 8, 9, 10, 11, 13, 14, 15, 16, 17, 18, 19], 27: list(range(1, 27)), 28: list(range(1, 70))}, NOHEAD   # 26:2-3 inside 297-299 (298 and 299 headless), 26:6-11 inside 301 (thirty-seven rows), 26:13-15 inside 303 (headless), 26:16-19 NO ROW — the covenant formula uncited by the spine; chapters 27 and 28 whole without a piska
assert {p: (len(sif_he[p - 1]), len(sif[p - 1])) for p in PISKAOT} == {p: (n, n) for p, n in SPINE_ROWS.items()} and [sum(SPINE_ROWS[p] for p in PISKAOT_BY[c]) for c in CHS] == [77, 0, 0] and sum(SPINE_ROWS.values()) == 77 and len(READ_ROWS) == 77 and len(PISKAOT) == 7 and READ_ROWS[:2] == [(297, 1), (297, 2)] and READ_ROWS[-1] == (303, 20)
# THE TAILS AND THE EDGES (the split's print): 296's rows carry no word of 26:1; 297:1 opens with 26:1's citation; 303:20 cites 26:15 and 304:1 opens with 31:14's citation — the gap 26:16-31:13 has no piska; the three headless piskaot open inside their verses
assert not any(w in HB0(296, r) for r in range(1, 10) for w in ('והיה כי תבוא אל הארץ', 'כי תבוא אל הארץ אשר יהוה')) and HB0(297, 1).startswith('(דברים כו א) והיה כי תבוא אל הארץ') and HB0(303, 20).startswith('(דברים כו טו) השקיפה ממעון קדשך') and HB0(304, 1).startswith('(דברים לא יד) ויאמר ה׳ אל משה הן קרבו ימיך למות') and HB0(305, 1).startswith('(במדבר כז יח) ויאמר ה׳ אל משה קח לך את יהושע')
assert HB0(298, 1).startswith('ושמת בטנא') and HB0(299, 1).startswith('ואמרת אליו') and HB0(303, 1).startswith('ונתת ללוי לגר ליתום ולאלמנה') and HB0(302, 1).startswith('(דברים כו יב) כי תכלה לעשר') and HB0(300, 1).startswith('(דברים כו ד) ולקח הכהן הטנא מידך') and HB0(301, 1).startswith('(דברים כו ה) וענית ואמרת'), (HB0(298, 1)[:30], HB0(299, 1)[:30], HB0(303, 1)[:40])
assert all(clean(sif[p - 1][0]).startswith('Pisqa’ %d' % p) for p in PISKAOT) and 'Now it shall be, when you enter the Land' in clean(sif[296][0])[:120] and 'And place it in a basket' in clean(sif[297][0])[:80] and 'And you shall say to him' in clean(sif[298][0])[:80] and 'And you shall give it to the Levite' in clean(sif[302][0])[:100] and 'Then the Priest will take the basket' in clean(sif[299][0])[:100]
assert HB0(301, 8).startswith('[גדול ועצום') and HB0(301, 24).endswith('מכת בכורות].') and HB0(301, 25).startswith('רבי יהודה היה נותן בהם סימן'), (HB0(301, 8)[:20], HB0(301, 24)[-20:])   # 301:8-24 the bracketed Haggadah parallel in the export's own unpointed orthography ("poorly attested in copies of Sifre" — the translator's note at 301:4)
# THE CITATIONS PARSED FROM THE THREE DUMPS' PRINTS (the instrument's own lists read back): the row-citations per file, the union, the outside sets before the headless join
import ast as _ast
_DUMP = {}
for _c in CHS:
    _t = open(os.path.join(os.path.dirname(os.path.abspath(__file__)), f'ch{_c}_dump0.out'), encoding='utf-8').read()
    _he = _ast.literal_eval(re.search(r'^  HE rows citing Deut %d[^:]*: \d+ (\[.*\])$' % _c, _t, re.M).group(1)); _en = _ast.literal_eval(re.search(r'^  EN rows citing Deut %d[^:]*: \d+ (\[.*\])$' % _c, _t, re.M).group(1))
    _un = int(re.search(r'^  the union of rows \(both files\): (\d+) \[', _t, re.M).group(1)); _out = _ast.literal_eval(re.search(r'^  the rows OUTSIDE the spine piskaot [^:]*: \d+ (\[.*?\]) \|', _t, re.M).group(1))
    _two = re.search(r'^  DB verses (\d+) \| export verses HE (\d+) EN (\d+) \| per-chapter export lengths vs DB, chapters 1-28: (\[.*\])$', _t, re.M); _cost = int(re.search(r'^  the alignment cost (\d+) \|', _t, re.M).group(1))
    _DUMP[_c] = (len(_he), len(_en), _un, _out, tuple(int(x) for x in _two.groups()[:3]), _two.group(4), _cost)
assert {c: v[:3] for c, v in _DUMP.items()} == {26: (16, 94, 60), 27: (7, 14, 11), 28: (15, 17, 10)}, {c: v[:3] for c, v in _DUMP.items()}
assert {c: v[4:] for c, v in _DUMP.items()} == {26: ((19, 19, 19), '[(5, 30, 33)]', 21), 27: ((26, 26, 26), '[(5, 30, 33)]', 12), 28: ((69, 69, 69), '[(5, 30, 33)]', 37)}, {c: v[4:] for c, v in _DUMP.items()}   # THE TWO DIVISIONS the identity in all three (chapter 5 the book's one split); the Hebrew's 28:69 the export's own last verse
assert [len(v[3]) for v in _DUMP.values()] == [32, 11, 10] and sorted({k for v in _DUMP.values() for k in v[3] if k[0] not in PISKAOT}) == OUTSIDE and sorted({k for v in _DUMP.values() for k in v[3] if k[0] in PISKAOT}) == [(298, 1), (298, 2), (298, 3), (299, 1), (299, 2), (299, 3), (299, 4), (301, 1)] + [(303, r) for r in range(1, 21) if r != 3], sorted({k for v in _DUMP.values() for k in v[3] if k[0] in PISKAOT})   # the headless piskaot's citing rows fell among the outside sets (303:3 the Nevalta clan cites nothing); 301:1 fell into CHAPTER 27's outside set — it cites 27:14 from inside the spine (the split returned it to the spine; the first pass read the list without it — retyped from the print)
assert len(OUTSIDE) == 26 and len(PRIOR_READ) == 25 and FRESH == [(347, 3)] and sorted(list(PRIOR_READ) + FRESH) == sorted(OUTSIDE) and all(CITED[k] for k in OUTSIDE) and {k[0] for k in OUTSIDE} == set(HEADS_ON) and sorted(k for k in OUTSIDE if any(c == 26 for c, _ in CITED[k])) == [(63, 9), (72, 5), (109, 1), (109, 3), (109, 4), (109, 5)] and len([k for k in OUTSIDE if any(c == 27 for c, _ in CITED[k])]) == 10 and len([k for k in OUTSIDE if any(c == 28 for c, _ in CITED[k])]) == 10
# THE PARSER on every verse (the C section of the dumps and the measure's E): four number verses and one starred pair — and ONE FALSE HIT, 28:63's "shesh" REJOICED read as six
with contextlib.redirect_stdout(io.StringIO()):
    import cold_run_sequence as _CS
_PARSE = {}
for _c, _v in SPAN:
    _vw = _CS.verse_words('Deut', _c, _v); _n, _o = _CS.ink_numbers(_vw), _CS.ink_ordinals(_vw); _marked = [t for t in _vw if t[-1] in '#~^%@|*']
    if _n or _o or _marked: _PARSE[(_c, _v)] = (_n, _o, _marked)
assert _PARSE == {(26, 12): ([], [], ['לעשר*', 'מעשר*']), (28, 7): ([1, 7], [], []), (28, 25): ([1, 7], [], []), (28, 55): ([1], [], []), (28, 63): ([6], [], [])}, _PARSE
assert _CS.verse_words('Deut', 28, 63)[2] == 'שש' and _CS.verse_words('Deut', 28, 7)[9] == 'אחד' and _CS.verse_words('Deut', 28, 7)[12] == 'ובשבעה' and _CS.verse_words('Deut', 26, 3)[18] == 'נשבע' and _CS.verse_words('Deut', 28, 55)[1] == 'לאחד' and _CS.verse_words('Deut', 26, 12)[2] == 'לעשר*'   # "swore" (nishba) at 26:3 the seven's homograph, NOT counted; the tithe's two tokens starred by the store
# THE STORE = THE DB except at TWO verses of chapter 28 — the ketiv/qere seats 28:27 (the hemorrhoids) and 28:30 (lie with her): the store one token more at each; the tokens 319 / 326 / 994; seven "?" glosses, all 'anokhi' (I)
assert STORE_MISMATCH == [(28, 27, 12, 11), (28, 30, 15, 14)], STORE_MISMATCH
assert {c: sum(len(W(c, v)) for v in range(1, NV[c] + 1)) for c in CHS} == {26: 319, 27: 326, 28: 994} and [(cc, v, hp) for (cc, v) in SG for _, hp, g in SG[(cc, v)] if g in ('?', '', None)] == [(27, 1, 'אנכי'), (27, 4, 'אנכי'), (27, 10, 'אנכי'), (28, 1, 'אנכי'), (28, 13, 'אנכי'), (28, 14, 'אנכי'), (28, 15, 'אנכי')]
# THE FRAMES (the measure's E): the declaration's first person (26:3-14 — sixteen tokens over the three chapters), the narrative forms of the recital (26:5-9) and of Moses' commands (27:1, 9, 11), no imperative, five infinitive absolutes, "saying" thrice, "this day" thirteen; the register's ONE seat — the FOOTER at 28:69 (moab), no receipt, no header
MO = {(c, v): [(x, m) for x, m in by[('Deut', c, v)]] for c, v in SPAN}
assert [(c, v) for c, v in SPAN if any(m and '2mp' in m for _, m in MO[(c, v)])] == [(27, 1), (27, 2), (27, 4), (27, 12), (28, 14), (28, 62), (28, 63), (28, 68)] and [(c, v, x) for c, v in SPAN for x, m in MO[(c, v)] if m and re.search(r'V[a-zA-Z]a$', m)] == [(27, 1, 'שמר'), (27, 8, 'באר'), (27, 8, 'היטב'), (28, 1, 'שמוע'), (28, 20, 'מהר')]
assert len([(c, v, x) for c, v in SPAN for x, m in MO[(c, v)] if m and re.search(r'V[a-zA-Z]w', m)]) == 15 and [(c, v, x) for c, v in SPAN for x, m in MO[(c, v)] if m and re.search(r'V[a-zA-Z]w', m)][-3:] == [(27, 1, 'ויצו'), (27, 9, 'וידבר'), (27, 11, 'ויצו')] and [(c, v, x) for c, v in SPAN for x, m in MO[(c, v)] if m and re.search(r'^HV..v', m)] == [] and len([(c, v, x) for c, v in SPAN for x, m in MO[(c, v)] if m and re.search(r'1c[sp]', m) and m.startswith('HV')]) == 16
assert [f'{c}:{v}' for c, v in SPAN if 'לאמר' in W(c, v)] == ['27:1', '27:9', '27:11'] and [f'{c}:{v}' for c, v in SPAN if 'היום' in W(c, v)] == ['26:3', '26:16', '26:17', '26:18', '27:1', '27:4', '27:9', '27:10', '28:1', '28:13', '28:14', '28:15', '28:32'] and {c: sum(1 for v in range(1, NV[c] + 1) for x in W(c, v) if x in ('לא', 'ולא')) for c in CHS} == {26: 5, 27: 2, 28: 34} and [(c, v) for c, v in SPAN if 'אם' in W(c, v) or 'ואם' in W(c, v)] == [(28, 1), (28, 15), (28, 58)]
assert {c: (sum(1 for v in range(1, NV[c] + 1) for x in W(c, v) if x == 'יהוה'), sum(1 for v in range(1, NV[c] + 1) for x in W(c, v) if x == 'ליהוה')) for c in CHS} == {26: (17, 2), 27: (7, 3), 28: (41, 0)}
with contextlib.redirect_stdout(io.StringIO()):
    import register_census as _RC
    _rink = _RC.read_ink()
assert [k for k in _RC.receipts(_rink) if k[0] == 'Deut' and k[1] in CHS] == [] and [x for x in _RC.footers(_rink) if x[0][0] == 'Deut' and x[0][1] in CHS] == [(('Deut', 28, 69), {'noun': 'words', 'kind': 'FOOTER', 'stamp': 'moab'})] and [x for x in _RC.register_headers(_rink) if x[0][0] == 'Deut' and x[0][1] in CHS] == []
# THE FORMULAS (the measure's C): the seats over the Torah and the Bible by consonants
assert P('זבת', 'חלב', 'ודבש', books=T) == ['Deut 11:9', 'Deut 26:15', 'Deut 26:9', 'Deut 27:3', 'Deut 31:20', 'Deut 6:3', 'Exod 13:5', 'Exod 33:3', 'Exod 3:17', 'Exod 3:8', 'Lev 20:24', 'Num 13:27', 'Num 14:8', 'Num 16:13', 'Num 16:14'] and len(P('זבת', 'חלב', 'ודבש', books=None)) == 20
assert P('כל', 'דברי', 'התורה', 'הזאת', books=None) == ['Deut 17:19', 'Deut 27:3', 'Deut 27:8', 'Deut 28:58', 'Deut 29:28', 'Deut 31:12', 'Deut 32:46'] and P('ואמר', 'כל', 'העם', 'אמן', books=T) == ['Deut 27:%d' % v for v in range(16, 27)] and P('ואמר', 'כל', 'העם', 'אמן', books=None) == ['Deut 27:%d' % v for v in range(16, 27)] + ['Ps 106:48']
assert P('לעם', 'סגלה', books=None) == ['Deut 14:2', 'Deut 26:18', 'Deut 7:6'] and P('עליון', 'על', 'כל', books=T) == ['Deut 26:19', 'Deut 28:1'] and P('במתי', 'מעט', books=None) == ['Deut 26:5', 'Deut 28:62'] and P('ביד', 'חזקה', 'ובזרע', 'נטויה', books=None) == ['Deut 26:8', 'Deut 5:15'] and P('שמוע', 'תשמע', 'בקול', books=None) == ['Deut 15:5', 'Deut 28:1']
assert P('הר', 'גרזים', books=T) == ['Deut 11:29', 'Deut 27:12'] and P('הר', 'עיבל', books=T) == ['Deut 11:29'] and P('בהר', 'עיבל', books=T) == ['Deut 27:13', 'Deut 27:4'] and P('ראשית', 'כל', 'פרי', books=T) == [] and P('מראשית', 'כל', 'פרי', books=T) == ['Deut 26:2'] and P('ספר', 'התורה', 'הזאת', books=T) == [] and P('בספר', 'התורה', 'הזאת', books=T) == ['Deut 28:61']   # the consonantal phrases miss the prefixed forms — Ebal's two seats in 27 carry a bet, the first-fruits a mem, the book a bet
assert P('ימין', 'ושמאול', books=T) == ['Deut 17:20', 'Deut 28:14', 'Deut 2:27', 'Num 20:17', 'Num 22:26'] and P('במצור', 'ובמצוק', books=None) == ['Deut 28:53', 'Deut 28:55', 'Deut 28:57', 'Jer 19:9'] and P('עץ', 'ואבן', books=T) == ['Deut 28:36', 'Deut 28:64', 'Deut 29:16', 'Deut 4:28'] and P('דברי', 'הברית', books=T) == ['Deut 28:69', 'Deut 29:8', 'Exod 34:28'] and P('בארץ', 'מואב', books=None) == ['Deut 1:5', 'Deut 28:69', 'Deut 32:49', 'Deut 34:5', 'Deut 34:6']
assert P('פרי', 'בטנך', books=None) == ['Deut 28:18', 'Deut 28:4', 'Deut 28:53', 'Deut 7:13'] and P('טנאך', 'ומשארתך', books=None) == ['Deut 28:17', 'Deut 28:5'] and P('בדרך', 'אחד', books=None) == ['1Kgs 18:6', 'Deut 28:25', 'Deut 28:7'] and P('ככוכבי', 'השמים', 'לרב', books=None) == ['Deut 10:22', 'Deut 1:10', 'Deut 28:62'] and P('לראש', 'ולא', 'לזנב', books=None) == ['Deut 28:13'] and P('כנף', 'אביו', books=None) == ['Deut 23:1', 'Deut 27:20']
assert U('ארור', books=T) == ['Deut 27:%d' % v for v in range(15, 27)] + ['Deut 28:16', 'Deut 28:17', 'Deut 28:18', 'Deut 28:19', 'Gen 27:29', 'Gen 3:14', 'Gen 49:7', 'Gen 4:11', 'Gen 9:25', 'Num 24:9'] and U('שחד', 'ושחד', books=T) == ['Deut 10:17', 'Deut 16:19', 'Deut 27:25', 'Exod 23:8'] and U('בסתר', books=T) == P('בסתר', books=T)
# THE KIN BY COMPUTATION (the measure's A — the same instrument): the closest verses in order
assert KINC[(26, 1)][0] == ('Deut 17:14', 3, 10) and KINC[(26, 9)][:2] == [('Exod 13:5', 6, 5), ('Num 14:8', 6, 7)] and KINC[(26, 15)][0] == ('Josh 5:6', 6, 7) and KINC[(27, 3)][0] == ('Deut 6:3', 7, 8) and KINC[(27, 20)][0] == ('Deut 27:22', 7, 8) and KINC[(28, 1)][0] == ('Deut 28:15', 7, 16) and KINC[(28, 15)][0] == ('Deut 28:45', 8, 6) and KINC[(28, 4)][0] == ('Deut 28:18', 8, 8)
assert KINC[(28, 36)][0] == ('Deut 28:64', 7, 8) and KINC[(28, 26)][0] == ('Jer 7:33', 6, 7) and KINC[(28, 53)][:2] == [('Deut 28:55', 4, 7), ('Deut 28:57', 4, 7)] and KINC[(28, 69)][0] == ('1Kgs 8:9', 5, 4) and [k for k in SPAN if not KINC[k]] == [(28, 22), (28, 28), (28, 39), (28, 59)] and KINC[(26, 5)][0] == ('1Sam 7:10', 3, 1) and KINC[(28, 30)][:3] == [('Deut 20:5', 3, 2), ('Deut 20:6', 3, 2), ('Deut 20:7', 3, 3)]
# THE TWINS DIFFED (the measure's B): the blessings and the curses word for word, the recital's kin, the altar's DB seat
assert SHN(DV(28, 1), DV(28, 15)) == 16 and SHN(DV(28, 1), DV(15, 5)) == 14 and SHN(DV(28, 4), DV(28, 18)) == 8 and SHN(DV(28, 5), DV(28, 17)) == 2 and len(words(*DV(28, 5))) == 3 and SHARED(DV(26, 8), DV(5, 15)) == ['ביד', 'חזקה', 'ובזרע', 'נטויה'] and SHARED(DV(26, 9), ('Exod', 3, 8)) == ['ארץ', 'זבת', 'חלב', 'ודבש']
assert SHARED(DV(27, 22), ('Lev', 20, 17)) == ['אחתו', 'בת', 'אביו', 'או', 'בת', 'אמו'] and SHARED(DV(28, 53), DV(28, 55)) == ['במצור', 'ובמצוק', 'אשר', 'יציק', 'לך', 'איבך'] and SHN(DV(28, 36), DV(28, 64)) == 8 and SHARED(DV(28, 62), DV(26, 5)) == ['במתי', 'מעט'] and SHARED(DV(28, 63), DV(30, 9)) == ['כאשר', 'שש'] and SHN(DV(26, 5), ('Gen', 47, 4)) == 0 and SHARED(DV(27, 16), ('Exod', 21, 17)) == ['אביו', 'ואמו']
assert SHN(DV(27, 5), ('Exod', 20, 22)) == 0 and 'אבנים' in words('Exod', 20, 25) and 'גזית' in words('Exod', 20, 25) and SHN(DV(27, 5), ('Josh', 8, 31)) == 4 and SHARED(DV(27, 6), ('Josh', 8, 31)) == ['אבנים', 'שלמות'] and SHN(DV(27, 15), ('Exod', 20, 4)) == 1 and SHARED(DV(27, 19), DV(24, 17)) == ['משפט', 'גר', 'יתום']   # the altar of unhewn stones is Exodus 20:25 in the DB's numbering (20:22 the heavens' speech); Joshua 8:31 its twin — the Prophets' seat, not read ahead
# ONKELOS (the measure's D): the Aramean rendered LABAN who sought to destroy, the basket a sala, the Shekhinah made to dwell at the place, cursed = lit and blessed = berikh, Amen twelve times, the eagle, in ships; "hearken to the voice" = receive the Memra
assert SEATS('לבן ארמאה') == [(26, 5)] and SEATS('לאובדא') == [(26, 5), (28, 63)] and SEATS('סלא') == [(26, 2), (26, 4)] and SEATS('שכינת') == [(31, 17)] and ARM(26, 2)[-3:] == ['לאשראה', 'שכנתיה', 'תמן'] and ARM(26, 5)[:7] == ['ותתיב', 'ותימר', 'קדם', 'יי', 'אלהך', 'לבן', 'ארמאה'] and len(ARM(26, 5)) == 23 and len(W(26, 5)) == 20
assert SEATS('אמן') == [(27, v) for v in range(15, 27)] and SEATS('ליט') == [(3, 24), (4, 39), (10, 7)] + [(27, v) for v in range(15, 27)] + [(28, 16), (28, 17), (28, 18), (28, 19), (32, 13), (32, 14)] and SEATS('בריך') == [(7, 14), (28, 3), (28, 4), (28, 5), (28, 6), (33, 1), (33, 20), (33, 24)] and SEATS('בסתר') == [(13, 7), (27, 15), (27, 24), (28, 57)] and SEATS('נשר') == [(14, 12), (28, 49), (32, 11)] and SEATS('שעממו') == [(28, 28)] and SEATS('שוחד') == []
assert SEATS('חלב ודבש') == [(6, 3), (11, 9), (26, 9), (26, 15), (27, 3), (31, 20)] and ARM(27, 15)[:2] == ['ליט', 'גברא'] and ARM(27, 26)[-4:] == ['ויימר', 'כל', 'עמא', 'אמן'] and ARM(28, 68)[3:5] == ['בספינן', 'בארחא'] and ARM(28, 69)[:3] == ['אלין', 'פתגמי', 'קימא'] and 'למימרא' in ARM(26, 14) and 'למימרא' in ARM(28, 1) and ARM(26, 15)[0] == 'אסתכי' and ARM(28, 22)[:3] == ['ימחנך', 'יי', 'בשחפתא'] and ARM(28, 64)[-2:] == ['אעא', 'ואבנא']
# THE PRIOR READS (computed from the ledgers): three spine rows read before at three ledgers (297:4 at chapter 8, 301:4 at chapter 10, 301:21 at chapter 4); twenty-five outside rows read before; nothing of 26-34 or the Prophets read ahead
TRI = f'{ROOT}/logic/oral_triage'
LED = {f: open(f'{TRI}/{f}', encoding='utf-8').read() for f in os.listdir(TRI) if f.endswith('.md') and os.path.isfile(f'{TRI}/{f}') and f != os.path.basename(OUT)}
SPINE_PRIOR = sorted({(f, int(a), int(b)) for f, t in LED.items() for a, b in re.findall(r'Sifrei Devarim (\d+):(\d+)', t) if int(a) in PISKAOT})
OUT_PRIOR = sorted({(f, int(a), int(b)) for f, t in LED.items() for a, b in re.findall(r'Sifrei Devarim (\d+):(\d+)', t) if (int(a), int(b)) in OUTSIDE})
assert SPINE_PRIOR == [('deu_04_vaetchanan_2026-09-16.md', 301, 21), ('deu_08_ekev_2026-09-18.md', 297, 4), ('deu_10_ekev_2026-09-19.md', 301, 4)], SPINE_PRIOR
assert sorted({(p, r) for _, p, r in OUT_PRIOR}) == sorted(PRIOR_READ) and {(p, r): sorted({f for f, pp, rr in OUT_PRIOR if (pp, rr) == (p, r)}) for p, r in PRIOR_READ} == PRIOR_READ and len(OUT_PRIOR) == 29, (len(OUT_PRIOR), [k for k in PRIOR_READ if sorted({f for f, pp, rr in OUT_PRIOR if (pp, rr) == k}) != PRIOR_READ[k]])
assert sorted(f for f, t in LED.items() if re.search(r'^- Onkelos (?:Deut (?:2[6-9]|3\d)|Josh|Judg|1Sam|2Sam|1Kgs|2Kgs|Isa|Jer|Ezek):', t, re.M)) == []   # never read ahead

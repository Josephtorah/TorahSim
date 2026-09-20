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

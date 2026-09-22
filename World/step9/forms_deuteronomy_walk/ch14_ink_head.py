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

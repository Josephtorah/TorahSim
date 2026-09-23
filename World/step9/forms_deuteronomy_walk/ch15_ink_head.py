import os as _os
_ROOT = _os.path.normpath(_os.path.join(_os.path.dirname(_os.path.abspath(__file__)), '..', '..', '..'))   # THE PORTABLE REPO (2026-09-15): the repo root from this file's own place
#!/usr/bin/env python3
# THE DEUTERONOMY WALK, sitting 13 — CHAPTER 15, Deuteronomy 15:1-23 (2026-09-22; the owner: "Go" after the compaction at #205 addendum 5; TWO RUNS + THE
# TAIL under THE COST RULES A-B-C, the #204 NOTE — RUN A the rereads, the measurements, the ink, the design, the clean point; RUN B the rows in two halves with
# the clean point after the first half unconditionally and the ledger; THE TAIL): THE INK of the chapter, computed from the Tanakh DB, the snapshot store and
# the shelf's own bytes — never typed. Sitting 12's form (ch14_ink.py): the generic helpers copied by derive_ch15_ink.py from the forms' ch14_ink.py by
# content markers, the constants and every assert chapter 15's own, typed FROM THE PRINTS (ch15_dump0.out, ch15_measure1.out). THE TWO DIVISIONS AGREE
# (23 = 23; the alignment the identity, cost 20) — THE CHAPTER IS TWENTY-THREE VERSES in both numberings. THE SPINE IS ON THE CHAPTER — SIXTEEN piskaot
# (111-126) with 99 rows, every head computed in chapter 15 (111 on 15:1 … 126 on 15:21; THE HEADS IN VERSE ORDER this chapter; 110 on 14:29 before, 127 on
# 16:1 after; no tail folded in — piska 110's five rows were read whole at chapter 14, and 126's rows stop before 16:1's words); TEN rows elsewhere cite the
# chapter by the union of both files (41:3 on 11:13; 71:6-8 on 12:15; 106:5 on 14:23; 109:3 on 14:28 — SIX READ BEFORE at chapters 11, 12 and 14, REREAD WHOLE;
# 147:3-4 on 17:1, 279:4 on 24:15, 355:9 on 33:20 — FOUR fresh), NONE excluded. The parser MEASURED on every verse — FOUR NUMBER VERSES (15:1 "seven years" [7],
# 15:12 and 15:18 "six years" [6], 15:7 "one of your brothers … one of your gates" [1]), ONE ORDINAL (15:9 "the seventh" [7]) and the STARRED "years" tokens
# (the number word "two" inside "years" marked at 15:1, 12, 18 — the count before it read). THE STORE = THE DB at every verse (354 = 354; NO KETIV this
# chapter). The hand's facts as asserts, run all at once by assert_driver.py.
import json, os, re, html, sqlite3, sys, io, contextlib, unicodedata, subprocess
from collections import Counter
ROOT = _ROOT
sys.path.insert(0, f'{ROOT}/World/step9')
DATE = '2026-09-22'
CH = 15
UIDS = ['deu_15_release_firstborn']
SPANS = {'deu_15_release_firstborn': (15, 1, 23)}
PREFIX = {'deu_15_release_firstborn': 'DV15'}
SPAN = [(15, v) for v in range(1, 24)]
PISKAOT = list(range(111, 127))   # THE SPINE ON THE CHAPTER: the sixteen piskaot 111-126 whose heads are in chapter 15 (the A print); 110 heads on 14:29, 127 on 16:1
HEADLESS = []
SPINE_ROWS = {111: 11, 112: 11, 113: 3, 114: 3, 115: 2, 116: 18, 117: 8, 118: 7, 119: 5, 120: 2, 121: 4, 122: 9, 123: 3, 124: 6, 125: 1, 126: 6}   # rows per piska, both files (the I print and the splitter's) — 99
PREV_CHAPTER_ROWS = []   # no tail folded in this chapter (piska 110's rows all on 14:29, read at chapter 14's sitting — asserted from its ledger)
READ_ROWS = [(p, r) for p in PISKAOT for r in range(1, SPINE_ROWS[p] + 1)]   # 99 — this ledger's spine rows
EXP2DB = {e: [e] for e in range(1, 24)}   # the identity — 23 = 23 (chapter 5 the book's one split)
DB2EXP = {d: e for e, ds in EXP2DB.items() for d in ds}
# the Hebrew's book-named citations of chapter 15 OUTSIDE the spine (the regex reads "(דברים טו כב)" etc.); 41:3, 71:7-8, 109:3 and 147:3-4 cite it in the English only
OUTSIDE_HE = [(71, 6, (15, 22)), (106, 5, (15, 20)), (279, 4, (15, 9)), (355, 9, (15, 7))]
OUTSIDE = [(41, 3), (71, 6), (71, 7), (71, 8), (106, 5), (109, 3), (147, 3), (147, 4), (279, 4), (355, 9)]   # the TEN rows READ WHOLE: the union of both files beyond piskaot 111-126
EXCLUDED = []   # every outside citation genuine
INTERPOLATION = []
CITED = {(41, 3): [9], (71, 6): [22], (71, 7): [22], (71, 8): [22], (106, 5): [20], (109, 3): [1], (147, 3): [21], (147, 4): [21], (279, 4): [9], (355, 9): [7]}
CITED_DB = {k: v[0] for k, v in CITED.items()}
PRIOR_READ = {(41, 3): ['deu_11_ekev_reeh_2026-09-20.md'], (71, 6): ['deu_12_reeh_2026-09-20.md'], (71, 7): ['deu_12_reeh_2026-09-20.md'], (71, 8): ['deu_12_reeh_2026-09-20.md'], (106, 5): ['deu_12_reeh_2026-09-20.md', 'deu_14_reeh_2026-09-21.md'], (109, 3): ['deu_14_reeh_2026-09-21.md']}   # the six outside rows read before (computed from the ledgers, asserted) — REREAD WHOLE here
HEADS_ON = {41: (11, 13), 71: (12, 15), 106: (14, 23), 109: (14, 28), 147: (17, 1), 279: (24, 15), 355: (33, 20)}
FRESH = [(147, 3), (147, 4), (279, 4), (355, 9)]
CREDITED = {}   # under THE WHOLE-ROW RULE no spine row is credited: the two reads before (117:3 at chapter 13's sitting — "take care", 13:4's clause; 116:18 at the Genesis 2 sitting — "a helper", Genesis 2:18) are REREAD WHOLE here and marked so
TITLE = "Chapter 15 — At the end of seven years you shall make a release: every creditor shall release what he lent his neighbor; he shall not exact it of his neighbor and his brother, because the LORD's release has been proclaimed; the foreigner you may exact. There shall be no needy among you, for the LORD will surely bless you in the land, if only you hearken to His voice: you shall lend to many nations and not borrow, rule and not be ruled. If there be a needy man among you, one of your brothers, within one of your gates, you shall not harden your heart nor shut your hand, but surely open your hand and lend him sufficient for his need; beware lest a base thought say 'the seventh year, the year of release, is near' and your eye be evil against your brother and he cry to the LORD against you; give, and let your heart not grieve, for the needy will never cease from the land — open your hand to your poor and needy. If your brother, a Hebrew man or woman, be sold to you, he serves six years and in the seventh goes free; you shall not send him away empty but furnish him from your flock, your floor and your press, remembering that you were a slave in Egypt and the LORD redeemed you; and if he says 'I will not go out, for I love you and your house', take the awl and put it through his ear into the door and he is your servant for ever — and so to your maidservant; let it not be hard, for he has served you double a hireling's hire. Every firstling male of your herd and flock you shall sanctify to the LORD: not work the firstling of your ox nor shear the firstling of your flock; eat it before the LORD year by year in the place He will choose, you and your household; if it has a blemish, lame or blind, any ill blemish, you shall not sacrifice it — eat it within your gates, the unclean and the clean alike, as the gazelle and the hart; only its blood you shall not eat: pour it on the earth as water"
OUT = f'{ROOT}/logic/oral_triage/deu_15_reeh_{DATE}.md'
db = sqlite3.connect(f'file:{ROOT}/Data/tanakh.sqlite?mode=ro', uri=True)
VC = dict(db.execute("SELECT chapter, COUNT(*) FROM verses WHERE book='Deut' GROUP BY chapter").fetchall())
NV = VC[CH]

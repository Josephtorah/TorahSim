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

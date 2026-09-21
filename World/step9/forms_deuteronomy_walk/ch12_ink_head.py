import os as _os
_ROOT = _os.path.normpath(_os.path.join(_os.path.dirname(_os.path.abspath(__file__)), '..', '..', '..'))   # THE PORTABLE REPO (2026-09-15): the repo root from this file's own place
#!/usr/bin/env python3
# THE DEUTERONOMY WALK, sitting 10 — CHAPTER 12, Deuteronomy 12:1-31 (2026-09-20; the owner: "Monitor how long each step takes and report when the chapter is
# done"; ONE RUN + ITS TAIL under THE COST RULES A-B-C — the rereads, the measurements, the ink, the design, the rows, the ledger, the seat, the chain LAUNCHED,
# the tail): THE INK of the chapter, computed from the Tanakh DB, the snapshot store and the shelf's own bytes — never typed. Sitting 9's form (ch11_ink.py): the
# generic helpers copied by derive_ch12_ink.py from that file by content markers, the constants and every assert chapter 12's own, typed FROM THE PRINTS
# (ch12_dump0.out, ch12_measure1.out). THE TWO DIVISIONS AGREE (31 = 31; the alignment the identity, cost 26) — THE CHAPTER IS THIRTY-ONE VERSES IN THE DB'S
# NUMBERING (the English's 12:32 is the Hebrew's 13:1; chapter 11's ink measured it). THE SPINE IS ON THE CHAPTER — TWENTY-THREE piskaot (59-81) with 159 rows:
# twenty heads computed in chapter 12 (59 on 12:1 … 81 on 12:30) and THREE PISKAOT WITHOUT A HEAD CITATION (68 opening with 12:11's "your burnt offerings", 73
# with 12:17's "your herd and your flock", 74 with 12:17's "your vows" — chapter 11's lesson 2, the membership decided on the consonants); SEVEN rows elsewhere
# cite it by the union of both files (2:2 the rest of 12:9 at the book's head, 106:5 and 147:2 the tithe's "you may not eat" at 14:23 and 17:1, 138:1 the
# rejoicing at 16:11, 145:3 the Asherah at 16:21, 179:2 the dwelling at 19:1, 286:16 the blood at 25:1), NONE excluded (the English's "(Dt.13:29)" at 179:2 a
# wrong chapter for 12:29 — the Hebrew right). The parser MEASURED on every verse — ONE NUMBER VERSE (12:14 "in one of your tribes" [1]) and ONE STARRED TOKEN
# (12:17's "tithe", the ten-word's homograph). THE STORE = THE DB at every verse (no written/read pair; 520 tokens, 2,051 letters; the four "?" glosses the
# store's "I"). The hand's facts as asserts, run all at once by assert_driver.py.
import json, os, re, html, sqlite3, sys, io, contextlib, unicodedata, subprocess
from collections import Counter
ROOT = _ROOT
sys.path.insert(0, f'{ROOT}/World/step9')
DATE = '2026-09-20'
CH = 12
UIDS = ['deu_12_place_name']
SPANS = {'deu_12_place_name': (12, 1, 31)}
PREFIX = {'deu_12_place_name': 'DV12'}
PISKAOT = list(range(59, 82))   # THE SPINE ON THE CHAPTER: twenty-three piskaot 59-81 — twenty heads computed in chapter 12 (the A print) and the three headless piskaot 68, 73, 74 whose first rows open with 12:11's and 12:17's own words; 58 on 11:32 before, 82 on 13:1 after
HEADLESS = [68, 73, 74]
SPINE_ROWS = {59: 5, 60: 4, 61: 8, 62: 4, 63: 11, 64: 5, 65: 6, 66: 2, 67: 4, 68: 6, 69: 4, 70: 6, 71: 14, 72: 11, 73: 1, 74: 9, 75: 15, 76: 9, 77: 9, 78: 10, 79: 5, 80: 5, 81: 6}   # rows per piska, both files (the I print and the splitter's) — 159
EXP2DB = {e: [e] for e in range(1, 32)}   # the identity — 31 = 31 (chapter 5 the book's one split)
DB2EXP = {d: e for e, ds in EXP2DB.items() for d in ds}
# the Hebrew's book-named citations of chapter 12 OUTSIDE the spine (the regex reads "(דברים יב ט)" etc.); 138:1's Hebrew cites 27:7 alone, its English adds (Dt.12:7)
OUTSIDE_HE = [(2, 2, (12, 9)), (106, 5, (12, 17)), (145, 3, (12, 3)), (147, 2, (12, 17)), (179, 2, (12, 29)), (286, 16, (12, 23))]
OUTSIDE = [(2, 2), (106, 5), (138, 1), (145, 3), (147, 2), (179, 2), (286, 16)]   # the SEVEN rows READ WHOLE: the union of both files beyond piskaot 59-81
EXCLUDED = []   # every outside citation genuine (179:2's English writes '(Dt.13:29)' for 12:29 — a wrong chapter in the English, the Hebrew's citation right; the row stays)
INTERPOLATION = []
CITED = {(2, 2): [9], (106, 5): [17], (138, 1): [7], (145, 3): [3], (147, 2): [17], (179, 2): [29], (286, 16): [23]}
CITED_DB = {k: v[0] for k, v in CITED.items()}
PRIOR_READ = {(2, 2): 'deu_01_03_devarim_2026-09-15.md'}   # one read before at sitting 1 (the eleven days) — REREAD WHOLE here
HEADS_ON = {2: (1, 2), 106: (14, 23), 138: (16, 11), 145: (16, 21), 147: (17, 1), 179: (19, 1), 286: (25, 1)}
FRESH = OUTSIDE[:]
CREDITED = {}   # under THE WHOLE-ROW RULE no spine row is credited: the five reads of four rows before (61:7 at chapter 7, 80:4-5 at chapter 11, 75:2 at two Genesis sittings) are REREAD WHOLE here and marked so
TITLE = "Chapter 12 — These are the statutes and the judgments for the land; destroy, you shall destroy all the places where the nations served their gods — the altars torn down, the pillars broken, the Asherim burned, the images cut down, the name destroyed from that place; not so to the LORD your God: the place which the LORD will choose from all your tribes to put His name there — His dwelling you shall seek, there you shall bring the burnt offerings, the sacrifices, the tithes, the heave offering, the vows, the freewill offerings, the firstlings, and eat before Him and rejoice, you and your households; not as we do here today, every man what is right in his eyes, for you have not yet come to the rest and the inheritance; across the Jordan, with rest from every enemy, the place chosen and the Levite in your gates with no portion; take heed lest you offer in every place you see — only in the place, in one of your tribes; only, with all the desire of your soul you may slaughter and eat flesh in all your gates, the unclean and the clean alike, as the gazelle and the hart — only the blood you shall not eat, on the earth you shall pour it like water; the tithe and the firstlings and the vows not in your gates but before the LORD in the place, with your household and the Levite — take heed lest you forsake him; when the border is enlarged as He spoke and the place is far, slaughter of your herd and flock as I have commanded you and eat in your gates; only be steadfast not to eat the blood, for the blood is the life; your holy things and your vows carried to the place, the flesh and the blood on the altar, the blood poured, the flesh eaten; observe and hear all these words that it may go well with you and your children forever; when the nations are cut off, take heed lest you be ensnared to inquire after their gods — every abomination of the LORD which He hates they did for their gods, even their sons and their daughters they burn in the fire"
OUT = f'{ROOT}/logic/oral_triage/deu_12_reeh_{DATE}.md'
db = sqlite3.connect(f'file:{ROOT}/Data/tanakh.sqlite?mode=ro', uri=True)

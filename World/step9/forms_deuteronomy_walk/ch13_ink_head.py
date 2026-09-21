import os as _os
_ROOT = _os.path.normpath(_os.path.join(_os.path.dirname(_os.path.abspath(__file__)), '..', '..', '..'))   # THE PORTABLE REPO (2026-09-15): the repo root from this file's own place
#!/usr/bin/env python3
# THE DEUTERONOMY WALK, sitting 11 — CHAPTER 13, Deuteronomy 13:1-19 (2026-09-21; the owner: "Go" after the reread that followed 10b's compaction; ONE RUN +
# ITS TAIL under THE COST RULES A-B-C — the rereads, the measurements, the ink, the design, the rows, the ledger, the clean point, the tail): THE INK of the
# chapter, computed from the Tanakh DB, the snapshot store and the shelf's own bytes — never typed. Sitting 10's form (ch12_ink.py): the generic helpers copied
# by derive_ch13_ink.py from that file by content markers, the constants and every assert chapter 13's own, typed FROM THE PRINTS (ch13_dump0.out,
# ch13_measure1.out). THE TWO DIVISIONS AGREE (19 = 19; the alignment the identity, cost 10) — THE CHAPTER IS NINETEEN VERSES IN THE DB'S NUMBERING (the
# English's 12:32 is the Hebrew's 13:1; the Onkelos export and the Sifrei's English both count the Hebrew way — no row cites "12:32"). THE SPINE IS ON THE
# CHAPTER — FIFTEEN piskaot (82-96) with 101 rows: fourteen heads computed in chapter 13 (82 on 13:1 … 95 and 96 on 13:17) and ONE PISKA WITHOUT A HEAD
# CITATION (88, whose two rows open with 13:8's own words — chapter 11's lesson 2 a fifth time); PISKA 96's LAST FOUR ROWS ARE 14:1's (its ninth row opens
# with the citation of 14:1 — chapter 14's sitting reads them: NEVER READ AHEAD), so NINETY-SEVEN spine rows are read here; SIX rows elsewhere cite the chapter
# by the union of both files (117:3 Belial at 15:9, 149:1-2 the inquiry at 17:4, 189:1 the rebellion at 19:16, 190:7-8 the inquiry at 19:17), NONE excluded (the
# English's "(Dt.13:4)" at 117:3 a wrong verse for 13:14 — the Hebrew right). The parser MEASURED on every verse — ONE NUMBER VERSE (13:13 "in one of your
# cities" [1]) and NO STARRED TOKEN; 13:18's "swore" no number (the dump's bare check matched the seven inside the oath's root). THE STORE = THE DB at every
# verse but 13:16, WHERE THE STORE CARRIES THE WRITTEN AND THE READ FORM of "that city" (329 tokens against the DB's 328; the chapter's one ketiv); the two
# "?" glosses the store's "I" (13:1, 13:19). The hand's facts as asserts, run all at once by assert_driver.py.
import json, os, re, html, sqlite3, sys, io, contextlib, unicodedata, subprocess
from collections import Counter
ROOT = _ROOT
sys.path.insert(0, f'{ROOT}/World/step9')
DATE = '2026-09-21'
CH = 13
UIDS = ['deu_13_seducers']
SPANS = {'deu_13_seducers': (13, 1, 19)}
PREFIX = {'deu_13_seducers': 'DV13'}
SPAN = [(13, v) for v in range(1, 20)]
PISKAOT = list(range(82, 97))   # THE SPINE ON THE CHAPTER: fifteen piskaot 82-96 — fourteen heads computed in chapter 13 (the A print) and the one headless piska 88 whose rows open with 13:8's own words; 81 on 12:30 before, 97 on 14:2 after
HEADLESS = [88]
SPINE_ROWS = {82: 5, 83: 5, 84: 5, 85: 6, 86: 10, 87: 13, 88: 2, 89: 8, 90: 3, 91: 4, 92: 5, 93: 10, 94: 6, 95: 7, 96: 12}   # rows per piska, both files (the I print and the splitter's) — 101
NEXT_CHAPTER_ROWS = [(96, 9), (96, 10), (96, 11), (96, 12)]   # piska 96's tail on 14:1 ("you are children of the LORD your God; you shall not cut yourselves") — chapter 14's sitting reads them (never read ahead); asserted below on the rows' own bytes
READ_ROWS = [(p, r) for p in PISKAOT for r in range(1, SPINE_ROWS[p] + 1) if (p, r) not in NEXT_CHAPTER_ROWS]   # 97 — this ledger's spine rows
EXP2DB = {e: [e] for e in range(1, 20)}   # the identity — 19 = 19 (chapter 5 the book's one split)
DB2EXP = {d: e for e, ds in EXP2DB.items() for d in ds}
# the Hebrew's book-named citations of chapter 13 OUTSIDE the spine (the regex reads "(דברים יג יד)" etc.); 149:2 and 190:8 cite it in the English only (the two files divide 190's rows differently — chapter 8's lesson)
OUTSIDE_HE = [(117, 3, (13, 14)), (149, 1, (13, 15)), (189, 1, (13, 6)), (190, 7, (13, 15))]
OUTSIDE = [(117, 3), (149, 1), (149, 2), (189, 1), (190, 7), (190, 8)]   # the SIX rows READ WHOLE: the union of both files beyond piskaot 82-96
EXCLUDED = []   # every outside citation genuine (117:3's English writes '(Dt.13:4)' twice for 13:14 — a wrong verse in the English, the Hebrew's citation right; the row stays)
INTERPOLATION = []
CITED = {(117, 3): [14], (149, 1): [15], (149, 2): [15], (189, 1): [6], (190, 7): [15], (190, 8): [15]}
CITED_DB = {k: v[0] for k, v in CITED.items()}
PRIOR_READ = {}   # no outside row read before (computed from the ledgers, asserted)
HEADS_ON = {117: (15, 9), 149: (17, 4), 189: (19, 16), 190: (19, 17)}
FRESH = OUTSIDE[:]
CREDITED = {}   # under THE WHOLE-ROW RULE no spine row is credited: the two reads before (82:5 at sitting 1 — the eleven days' "a thousand times"; 83:4 at a Genesis sitting — the lights as signs) are REREAD WHOLE here and marked so
TITLE = "Chapter 13 — All the word that I command you, that you shall keep to do: you shall not add to it nor take from it. When a prophet arises among you, or a dreamer of a dream, and gives you a sign or a wonder, and the sign comes to pass, saying, let us go after other gods which you have not known and serve them — you shall not hearken: the LORD your God is testing you, to know whether you love Him with all your heart and soul; after the LORD you shall walk, Him fear, His commandments keep, His voice obey, Him serve, to Him cleave; that prophet shall be put to death, for he spoke rebellion against the LORD who brought you out of Egypt and redeemed you from the house of bondage, to thrust you from the way — and you shall purge the evil from your midst. When your brother, the son of your mother, or your son or your daughter or the wife of your bosom or your friend who is as your own soul entices you in secret, saying, let us go and serve other gods which you and your fathers have not known, of the gods of the peoples round about, near or far, from one end of the earth to the other — you shall not consent nor hearken, your eye shall not pity him, you shall not spare nor conceal him: kill, you shall kill him, your hand first upon him and the hand of all the people afterward, and stone him with stones that he die, for he sought to thrust you from the LORD; and all Israel shall hear and fear and not do again such an evil thing. When you hear in one of your cities that sons of Belial have gone out and drawn away its inhabitants, saying, let us go and serve other gods — you shall inquire and search and ask diligently, and if the thing is true and certain, that abomination done in your midst, smite, you shall smite that city with the edge of the sword, devoting it and all in it and its cattle; gather all its spoil into its street and burn the city and its spoil wholly to the LORD; a heap forever, not built again; and nothing of the devoted thing shall cleave to your hand, that the LORD may turn from the fierceness of His anger and give you mercy and multiply you as He swore to your fathers, when you hearken to His voice to keep all His commandments, to do the right in His eyes"
OUT = f'{ROOT}/logic/oral_triage/deu_13_reeh_{DATE}.md'
db = sqlite3.connect(f'file:{ROOT}/Data/tanakh.sqlite?mode=ro', uri=True)
VC = dict(db.execute("SELECT chapter, COUNT(*) FROM verses WHERE book='Deut' GROUP BY chapter").fetchall())
NV = VC[CH]

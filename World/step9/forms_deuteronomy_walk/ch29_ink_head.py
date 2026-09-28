import os as _os
_ROOT = _os.path.normpath(_os.path.join(_os.path.dirname(_os.path.abspath(__file__)), '..', '..', '..'))   # THE PORTABLE REPO (2026-09-15): the repo root from this file's own place
#!/usr/bin/env python3
# THE DEUTERONOMY WALK, sitting 19 — CHAPTERS 29-31, Deuteronomy 29:1-31:30 IN THE LEAN FORM (2026-09-27; the owner: "Continue" after sitting 18b's tail, no
# compaction between, /context 387k at the open — THE LEAN PASS's eleventh sitting, its sixth reading, the second on chapters WITHOUT A SPINE PISKA): THE INK of the
# three chapters, computed from the Tanakh DB, the snapshot store and the shelf's own bytes — never typed. Sitting 18's form (ch26_ink.py): the generic helpers copied
# by derive_ch29_ink.py from the forms' ch22_ink.py by content markers (the three chapters substituted), the constants and every assert the three chapters' own, typed
# FROM THE PRINTS (ch29_dump0.out … ch31_dump0.out, ch29_split.out, ch29_measure_lean.out). THE TWO DIVISIONS AGREE in all three (28 = 28, cost 19; 20 = 20, cost 18;
# 30 = 30, cost 30) — the identity; the Hebrew's 28:69 is the English's 29:1, so the English's chapter 29 runs one verse ahead. THE SPINE IS ON CHAPTER 31 ALONE —
# TWO piskaot 304-305 with 8 rows (304 on 31:14 "your days approach" two rows; 305 HEADLESS after it, "then the LORD said to Moses: take Joshua" six rows — Moses'
# death and Joshua's commission); 303 on 26:15 before, 306 on 32:1 after — THE SIFREI HAS NO PISKA ON 26:16-31:13: CHAPTERS 29 AND 30 CARRY NO SPINE, their shelf
# Onkelos whole and the rows elsewhere citing them. NINETEEN rows elsewhere cite the three chapters by the union of the three files (the split's print). THE PORTION
# EDGE at 29:8|29:9 INSIDE chapter 29 (Ki Tavo ends, Nitzavim opens); Nitzavim ends with chapter 30; Vayelech is chapter 31 whole — the chapter the unit, CHAPTER NUMBERS.
# The parser MEASURED on every verse — the bare number words 29:4 "forty", 31:2 "a hundred (and twenty)", 31:10 "seven years" (starred), and the homographs "swore"
# (nishba) at 29:12, 30:20, 31:7, "sated" (ve-sava, starred) at 31:20 — the seven's; "rejoiced" (shesh) at 30:9 — the six's (28:63's twin). The hand's facts as asserts, run all at once by assert_driver.py.
import json, os, re, html, sqlite3, sys, io, contextlib, unicodedata, subprocess
from collections import Counter
ROOT = _ROOT
DATE = '2026-09-27'
CHS = (29, 30, 31)
UIDS = ['deu_29_moab_covenant', 'deu_30_teshuvah_choice', 'deu_31_charge_torah']   # the drafts' own ids (the G prints): three units, one per chapter
SPANS = {'deu_29_moab_covenant': (29, 1, 28), 'deu_30_teshuvah_choice': (30, 1, 20), 'deu_31_charge_torah': (31, 1, 30)}
PREFIX = {'deu_29_moab_covenant': 'DV29', 'deu_30_teshuvah_choice': 'DV30', 'deu_31_charge_torah': 'DV31'}
SPAN = [(29, v) for v in range(1, 29)] + [(30, v) for v in range(1, 21)] + [(31, v) for v in range(1, 31)]
PISKAOT = [304, 305]   # THE SPINE ON CHAPTER 31: two piskaot (one headless) — the A prints and the split's; 303 heads on 26:15 (headless, inside 26:13-15), 306 on 32:1
PISKAOT_BY = {29: [], 30: [], 31: [304, 305]}
HEADLESS = [305]   # no book-named citation at its head (the dump: "head None"; the split: 305:1 opens "(Numbers 27:18) and the LORD said to Moses: take Joshua") — read WHOLE from the export
SPINE_ROWS = {304: 2, 305: 6}   # rows per piska, both files (the heads table and the split's print) — 8
PREV_CHAPTER_ROWS = []   # no tail folded in (303's rows carry no word of 31:14 — the split's assert; 303:20 cites 26:15 and 304:1 opens with 31:14's citation)
READ_ROWS = [(p, r) for p in PISKAOT for r in range(1, SPINE_ROWS[p] + 1)]   # 8 — this ledger's spine rows
EXP2DB = {29: {e: [e] for e in range(1, 29)}, 30: {e: [e] for e in range(1, 21)}, 31: {e: [e] for e in range(1, 31)}}   # the identity in all three chapters (chapter 5 the book's one split)
DB2EXP = {c: {d: e for e, ds in EXP2DB[c].items() for d in ds} for c in CHS}
OUTSIDE = [(1, 1), (2, 3), (29, 7), (43, 7), (43, 29), (48, 9), (53, 1), (109, 2), (111, 1), (148, 8), (157, 10), (160, 4), (302, 1), (306, 2), (306, 15), (318, 1), (334, 1), (345, 2), (357, 28)]   # the NINETEEN rows READ WHOLE: the union of the three files beyond piskaot 304-305, joined over the three dumps (the split's print)
EXCLUDED = []   # none known at the design — a translator's misprint is judged by the Hebrew at the whole read (sitting 18's lesson 4)
INTERPOLATION = []
CREDITED = {}   # under THE WHOLE-ROW RULE no spine row is credited: rows read before are REREAD WHOLE here and marked so
TITLE = "Chapters 29-31 — You have seen all the LORD did in Egypt; forty years your garments did not wear out; Sihon and Og taken; you stand this day, all of you, heads, elders, officers, children, wives and the stranger, the hewer of wood and the drawer of water, to enter the covenant and the oath, with those here and those not here; lest a root bear gall and wormwood and a man bless himself in his heart — the LORD will not pardon, the curses of this book will lie on him; the land brimstone and salt like Sodom and Gomorrah, Admah and Zeboiim; the nations will ask why, and be answered: they forsook the covenant and served other gods, and He cast them into another land; the hidden things are the LORD's, the revealed ours forever. When you return with all your heart among the nations where He drove you, He will return and gather you from the end of heaven, circumcise your heart, rejoice over you as He rejoiced over your fathers; the commandment is not in heaven nor beyond the sea but in your mouth and in your heart; life and death, the blessing and the curse — choose life. Moses at a hundred and twenty: Joshua crosses before you, be strong and of good courage; the law written and given to the priests and the elders, to be read every seventh year at the feast of booths before all Israel; the LORD at the Tent in the pillar of cloud: you will sleep with your fathers and this people will whore after other gods and I will hide My face; write this song as a witness; the book beside the ark; I know your rebellion and your stiff neck — heaven and earth called to witness."
OUT = f'{ROOT}/logic/oral_triage/deu_29_31_nitzavim_vayelech_{DATE}.md'
PATCHED = bool(os.environ.get('DEU29_PATCHED'))   # the tail's flag: after the manifest and the seat, the drafts carry operators and the store its overrides
db = sqlite3.connect(f'file:{ROOT}/Data/tanakh.sqlite?mode=ro', uri=True)
VC = dict(db.execute("SELECT chapter, COUNT(*) FROM verses WHERE book='Deut' GROUP BY chapter").fetchall())
NV = {c: VC[c] for c in CHS}

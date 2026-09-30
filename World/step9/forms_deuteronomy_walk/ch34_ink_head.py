import os as _os
_ROOT = _os.path.normpath(_os.path.join(_os.path.dirname(_os.path.abspath(__file__)), '..', '..', '..'))   # THE PORTABLE REPO (2026-09-15): the repo root from this file's own place
#!/usr/bin/env python3
# THE DEUTERONOMY WALK, sitting 22 — CHAPTER 34, THE DEATH OF MOSES, Deuteronomy 34:1-12 IN THE LEAN FORM (2026-09-30; the owner: "Reread and go" after the compaction
# that followed sitting 21b's tail — the tree UNCOMMITTED with 21 and 21b since 472d2a3; THE LEAN PASS's seventeenth sitting, its ninth reading; THE SPINE IN FORCE: ONE
# piska, 357 on 34:1 — THE EXPORT'S LAST, forty-four rows, 42 KB in the split's file; DEUTERONOMY'S LAST CHAPTER): THE INK of the chapter, computed from the Tanakh DB,
# the snapshot store and the shelf's own bytes — never typed. Sitting 21's form (ch33_ink.py): the generic helpers copied by derive_ch34_ink.py from the forms' ch22_ink.py
# by content markers (the chapter substituted; the head regex comma-tolerant as sitting 21 left it), the constants and every assert the chapter's own, typed FROM THE PRINTS
# (ch34_dump0.out, ch34_split.out, ch34_measure_lean.out). THE TWO DIVISIONS AGREE (12 = 12, cost 5) — the identity. ONE DRAFT on file: deu_34_moses_death (34:1-12,
# twelve steps one per verse) — one unit, CHAPTER NUMBERS. TWO rows elsewhere cite the chapter, both READ BEFORE (305:5 at chapters 29-31 — the angel of death sent for
# Moses' soul; 341:1 at the song — "from afar you shall see the land"). THE PORTION EDGE: Vezot Habrachah is 33:1-34:12 — the chapter the portion's and the book's last;
# no piska after 357. The parser MEASURED on every verse — TWO NUMBERS COUNTED: 34:7's hundred and twenty (Moses' years at his death — 31:2's number, the marker's day)
# and 34:8's thirty (the days of weeping — a duration: the compile's matter). ONE ROW OF THE TESTING SHELF read whole at this sitting by 21b's leaving — Tosefta Sotah 4:4
# on 34:6 (the four mil on the Shekhinah's wings from Reuben's field to Gad's; the export Tosefta_Sotah, the Vilna paragraphs). The hand's facts as asserts, run all at
# once by assert_driver.py.
import json, os, re, html, sqlite3, sys, io, contextlib, unicodedata, subprocess
from collections import Counter
ROOT = _ROOT
DATE = '2026-09-30'
CHS = (34,)
UIDS = ['deu_34_moses_death']   # the draft's own id (the G print): one unit in the one chapter — the death 34:1-12
SPANS = {'deu_34_moses_death': (34, 1, 12)}
PREFIX = {'deu_34_moses_death': 'DV34'}
SPAN = [(34, v) for v in range(1, 13)]
PISKAOT = [357]   # THE SPINE ON CHAPTER 34: one piska, the export's last (the A prints and the split's); 356 on 33:27 before, NOTHING after
PISKAOT_BY = {34: PISKAOT}
HEADLESS = []   # none (the dump's heads table: 357's head is (34, 1))
SPINE_ROWS = {357: 44}   # rows per piska, both files (the heads table and the split's print) — 44
PREV_CHAPTER_ROWS = []   # no tail folded in (356's fourteen rows carry no word of 34:1 — the split's print; 356:14 ends on Joshua 10:24's necks; 357:1 opens with 34:1's ascent)
READ_ROWS = [(p, r) for p in PISKAOT for r in range(1, SPINE_ROWS[p] + 1)]   # 44 — this ledger's spine rows, read WHOLE in one slice (the split's plan: one slice, 42,152 bytes)
EXP2DB = {34: {e: [e] for e in range(1, 13)}}   # the identity (the offset 0 at every export verse — A0's print)
DB2EXP = {c: {d: e for e, ds in EXP2DB[c].items() for d in ds} for c in CHS}
OUTSIDE = [(305, 5), (341, 1)]   # the TWO rows READ WHOLE: the union of the two files beyond piska 357 (the dump's and the split's print) — both read before
EXCLUDED = []   # none known at the design — a translator's misprint is judged by the Hebrew at the whole read (sitting 18's lesson 4)
INTERPOLATION = []
CREDITED = {}   # under THE WHOLE-ROW RULE no spine row is credited: the four rows read before (357:27, 28, 40, 44 — the dump's list) are REREAD WHOLE here and marked so
TOSEFTA_ROWS = [('Sotah', 4, 4)]   # THE TESTING SHELF'S ONE ROW read whole at this reading by sitting 21b's leaving (found beside 355:6 on 34:6): the export Tosefta_Sotah
TITLE = "Chapter 34 — the death of Moses: and Moses went up from the plains of Moab to Mount Nebo, the top of Pisgah over against Jericho, and the LORD showed him all the land — Gilead as far as Dan, all Naphtali, the land of Ephraim and Manasseh, all the land of Judah as far as the hinder sea, the south and the plain of the valley of Jericho the city of palm trees as far as Zoar; and the LORD said to him: this is the land which I swore to Abraham, to Isaac and to Jacob, saying, to your seed I will give it — I have caused you to see it with your eyes, but you shall not cross over there. So Moses the servant of the LORD died there in the land of Moab by the mouth of the LORD, and He buried him in the valley in the land of Moab over against Beth-peor, and no man knows his grave to this day. Moses was a hundred and twenty years old when he died; his eye was not dim nor his natural force abated. The children of Israel wept for Moses in the plains of Moab thirty days, and the days of weeping in the mourning for Moses were ended. Joshua the son of Nun was full of the spirit of wisdom, for Moses had laid his hands upon him, and the children of Israel hearkened to him and did as the LORD commanded Moses. And there has not arisen a prophet since in Israel like Moses, whom the LORD knew face to face, in all the signs and the wonders which the LORD sent him to do in the land of Egypt to Pharaoh and to all his servants and to all his land, and in all the mighty hand and all the great terror which Moses wrought in the sight of all Israel."
OUT = f'{ROOT}/logic/oral_triage/deu_34_moses_death_{DATE}.md'
PATCHED = bool(os.environ.get('DEU34_PATCHED'))   # the tail's flag: after the manifest and the seat, the draft carries operators and the store its overrides
db = sqlite3.connect(f'file:{ROOT}/Data/tanakh.sqlite?mode=ro', uri=True)
VC = dict(db.execute("SELECT chapter, COUNT(*) FROM verses WHERE book='Deut' GROUP BY chapter").fetchall())
NV = {c: VC[c] for c in CHS}

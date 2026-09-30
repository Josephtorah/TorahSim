import os as _os
_ROOT = _os.path.normpath(_os.path.join(_os.path.dirname(_os.path.abspath(__file__)), '..', '..', '..'))   # THE PORTABLE REPO (2026-09-15): the repo root from this file's own place
#!/usr/bin/env python3
# THE DEUTERONOMY WALK, sitting 21 — CHAPTER 33, THE BLESSING, Deuteronomy 33:1-29 IN THE LEAN FORM (2026-09-29; the owner: "Reread and go" after the compaction that
# followed sitting 20b's push 472d2a3 — THE LEAN PASS's fifteenth sitting, its eighth reading; THE SPINE IN FORCE: fifteen piskaot 342-356 with 142 rows, 207 KB in the
# split's files — 355 on 33:20 the chapter's longest with thirty rows, 343 on 33:2 fifteen, 352 on 33:11 seventeen): THE INK of the chapter, computed from the Tanakh DB,
# the snapshot store and the shelf's own bytes — never typed. Sitting 20's form (ch32_ink.py): the generic helpers copied by derive_ch33_ink.py from the forms' ch22_ink.py
# by content markers (the chapter substituted; THE HEAD REGEX MADE COMMA-TOLERANT — 342's head "(Deuteronomy 33, 1)" is the export's one comma head, headless to sitting
# 20's instrument), the constants and every assert the chapter's own, typed FROM THE PRINTS (ch33_dump0.out, ch33_split.out, ch33_measure_lean.out). THE TWO DIVISIONS AGREE
# (29 = 29, cost 121) — the identity. ONE DRAFT on file: deu_33_ve_zot (33:1-29, twenty-nine steps one per verse) — one unit, CHAPTER NUMBERS. FIVE rows elsewhere cite the
# chapter, every one READ BEFORE (the split's print and the ledgers). THE PORTION EDGE: Vezot Habrachah is 33:1-34:12 — chapter 34 the next sitting; 357 on 34:1 its piska,
# cited by no row of this chapter. The parser MEASURED on every verse — ONE MARK: 33:23's "sated" (seva, the consonants of seven — the false six's and the false eight's
# precedent), no number counted anywhere in the chapter (the myriads of 33:2 and 33:17 are construct plurals the parser does not read). The hand's facts as asserts, run
# all at once by assert_driver.py.
import json, os, re, html, sqlite3, sys, io, contextlib, unicodedata, subprocess
from collections import Counter
ROOT = _ROOT
DATE = '2026-09-29'
CHS = (33,)
UIDS = ['deu_33_ve_zot']   # the draft's own id (the G print): one unit in the one chapter — the blessing 33:1-29
SPANS = {'deu_33_ve_zot': (33, 1, 29)}
PREFIX = {'deu_33_ve_zot': 'DV33'}
SPAN = [(33, v) for v in range(1, 30)]
PISKAOT = list(range(342, 357))   # THE SPINE ON CHAPTER 33: fifteen piskaot, every head present with the comma tolerated (the A prints and the split's); 341 on 32:52 before, 357 on 34:1 after
PISKAOT_BY = {33: PISKAOT}
HEADLESS = []   # none inside the chapter (the dump's heads table: 342-356 every head a chapter-33 citation — 342's with a comma)
SPINE_ROWS = {342: 7, 343: 15, 344: 7, 345: 3, 346: 2, 347: 5, 348: 9, 349: 5, 350: 3, 351: 4, 352: 17, 353: 13, 354: 8, 355: 30, 356: 14}   # rows per piska, both files (the heads table and the split's print) — 142
PREV_CHAPTER_ROWS = []   # no tail folded in (341's one row carries no word of 33:1 — the split's print; 341:1 reads 32:52 against 34:4; 342:1 opens with 33:1's citation and the hard words of 32:24-25)
READ_ROWS = [(p, r) for p in PISKAOT for r in range(1, SPINE_ROWS[p] + 1)]   # 142 — this ledger's spine rows, read WHOLE over the row runs by the split's byte plan
EXP2DB = {33: {e: [e] for e in range(1, 30)}}   # the identity (the offset 0 at every export verse — A0's print)
DB2EXP = {c: {d: e for e, ds in EXP2DB[c].items() for d in ds} for c in CHS}
OUTSIDE = [(31, 6), (42, 9), (48, 9), (314, 1), (329, 3)]   # the FIVE rows READ WHOLE: the union of the two files beyond piskaot 342-356 (the dump's and the split's print) — every one read before
EXCLUDED = []   # none known at the design — a translator's misprint is judged by the Hebrew at the whole read (sitting 18's lesson 4)
INTERPOLATION = []
CREDITED = {}   # under THE WHOLE-ROW RULE no spine row is credited: rows read before (the dump lists ten ledgers' seats among 342-356) are REREAD WHOLE here and marked so
TITLE = "Chapter 33 — the blessing: and this is the blessing with which Moses the man of God blessed the children of Israel before his death — the LORD came from Sinai, rose from Seir, shone from Mount Paran with myriads of holy ones, a fiery law at His right hand; He loves the peoples, all His holy ones are in Your hand; Moses commanded us a law, the inheritance of the congregation of Jacob; there was a king in Jeshurun when the heads of the people gathered, the tribes of Israel together. Let Reuben live and not die, though his men be few; hear, LORD, the voice of Judah, bring him to his people; of Levi — Your Thummim and Your Urim with Your godly one whom You tried at Massah and strove with at the waters of Meribah, who said of his father and mother I have not seen him, who kept Your word and guarded Your covenant — they shall teach Jacob Your ordinances, put incense before You and whole burnt offering on Your altar; bless, LORD, his substance, smite the loins of them that rise against him. Benjamin the beloved of the LORD dwells in safety, He covers him all the day and dwells between his shoulders. Joseph — blessed of the LORD is his land, the precious things of heaven, the dew and the deep that couches beneath, the sun and the moons, the ancient mountains and the everlasting hills, the earth and its fullness and the good will of Him that dwelt in the bush, on the head of Joseph and the crown of him that was separate from his brethren; his firstling bullock, the horns of the wild ox, the ten thousands of Ephraim and the thousands of Manasseh. Rejoice, Zebulun, in your going out, and Issachar in your tents — they call peoples to the mountain, offer sacrifices of righteousness, suck the abundance of the seas and the hidden treasures of the sand. Blessed be He that enlarges Gad — he dwells as a lioness, tears the arm and the crown of the head; he chose a first part for himself, the lawgiver's portion, he came with the heads of the people and executed the righteousness of the LORD. Dan a lion's whelp that leaps from Bashan; Naphtali satisfied with favor, full of the blessing of the LORD, possess the sea and the south; Asher blessed above sons, acceptable to his brethren, dipping his foot in oil, iron and brass your bars, as your days your strength. There is none like the God of Jeshurun who rides upon the heaven for your help; the eternal God is a dwelling place and underneath are the everlasting arms, He thrust out the enemy and said destroy; Israel dwells in safety, the fountain of Jacob alone in a land of corn and wine, his heavens drop down dew. Happy are you, O Israel, who is like you, a people saved by the LORD, the shield of your help and the sword of your excellency; your enemies shall dwindle before you and you shall tread upon their high places."
OUT = f'{ROOT}/logic/oral_triage/deu_33_ve_zot_{DATE}.md'
PATCHED = bool(os.environ.get('DEU33_PATCHED'))   # the tail's flag: after the manifest and the seat, the draft carries operators and the store its overrides
db = sqlite3.connect(f'file:{ROOT}/Data/tanakh.sqlite?mode=ro', uri=True)
VC = dict(db.execute("SELECT chapter, COUNT(*) FROM verses WHERE book='Deut' GROUP BY chapter").fetchall())
NV = {c: VC[c] for c in CHS}

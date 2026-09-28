import os as _os
_ROOT = _os.path.normpath(_os.path.join(_os.path.dirname(_os.path.abspath(__file__)), '..', '..', '..'))   # THE PORTABLE REPO (2026-09-15): the repo root from this file's own place
#!/usr/bin/env python3
# THE DEUTERONOMY WALK, sitting 20 — CHAPTER 32, THE SONG, Deuteronomy 32:1-52 IN THE LEAN FORM (2026-09-27; the owner: "Continue" after sitting 19b's tail and the push
# c4b14ce, no compaction between, /context 332k at the open — THE LEAN PASS's thirteenth sitting, its seventh reading; THE SPINE IN FORCE: thirty-six piskaot 306-341 with
# 249 rows, 358 KB — the export's longest piska 306 on 32:1 with thirty-seven rows): THE INK of the chapter, computed from the Tanakh DB, the snapshot store and the shelf's
# own bytes — never typed. Sitting 19's form (ch29_ink.py): the generic helpers copied by derive_ch32_ink.py from the forms' ch22_ink.py by content markers (the chapter
# substituted), the constants and every assert the chapter's own, typed FROM THE PRINTS (ch32_dump0.out, ch32_split.out, ch32_measure_lean.out). THE TWO DIVISIONS AGREE
# (52 = 52, cost 141) — the identity. TWO DRAFTS on file: deu_32_haazinu (32:1-43, the song) and deu_32_song_aftermath (32:44-52, the frame and the summons to Nebo) — two
# units in one chapter, CHAPTER NUMBERS. ELEVEN rows elsewhere cite the chapter (the split's print). NO portion edge inside the chapter (Haazinu is 32:1-52 whole). The
# parser MEASURED on every verse — THE FALSE EIGHT at 32:15 ("you grew fat", shamanta, read as the number eight — the false six's precedent at 28:63 and 30:9) and the
# joined thousand at 32:30 ("one chase a thousand, and two put ten thousand to flight" read as [1, 1002] with 'one' marked); 328's head CITED AS 32:35 by the export while its
# text is 32:38's ("who ate the fat of their sacrifices") — a misprinted verse marker in the heads table (sitting 19's lesson 1). The hand's facts as asserts, run all at once by assert_driver.py.
import json, os, re, html, sqlite3, sys, io, contextlib, unicodedata, subprocess
from collections import Counter
ROOT = _ROOT
DATE = '2026-09-27'
CHS = (32,)
UIDS = ['deu_32_haazinu', 'deu_32_song_aftermath']   # the drafts' own ids (the G prints): two units in the one chapter — the song 32:1-43 and its frame 32:44-52
SPANS = {'deu_32_haazinu': (32, 1, 43), 'deu_32_song_aftermath': (32, 44, 52)}
PREFIX = {'deu_32_haazinu': 'DV32', 'deu_32_song_aftermath': 'DV32A'}
SPAN = [(32, v) for v in range(1, 53)]
PISKAOT = list(range(306, 342))   # THE SPINE ON CHAPTER 32: thirty-six piskaot, every head present (the A prints and the split's); 305 headless before (31:14-23's), 342 headless after (33:1's)
PISKAOT_BY = {32: PISKAOT}
HEADLESS = []   # none inside the chapter (the dump's heads table: 306-341 every head a chapter-32 citation)
SPINE_ROWS = {306: 37, 307: 15, 308: 4, 309: 7, 310: 8, 311: 5, 312: 2, 313: 16, 314: 6, 315: 6, 316: 4, 317: 7, 318: 16, 319: 6, 320: 13, 321: 14, 322: 12, 323: 13, 324: 3, 325: 4, 326: 7, 327: 2, 328: 4, 329: 4, 330: 2, 331: 4, 332: 6, 333: 5, 334: 3, 335: 2, 336: 2, 337: 1, 338: 3, 339: 3, 340: 2, 341: 1}   # rows per piska, both files (the heads table and the split's print) — 249
PREV_CHAPTER_ROWS = []   # no tail folded in (305's rows carry no word of 32:1 — the split's assert; 305:6 ends with Joshua weeping and 306:1 opens with 32:1's citation)
READ_ROWS = [(p, r) for p in PISKAOT for r in range(1, SPINE_ROWS[p] + 1)]   # 249 — this ledger's spine rows, read WHOLE over the row runs by the split's byte plan
EXP2DB = {32: {e: [e] for e in range(1, 53)}}   # the identity (the offset 0 at every export verse — A0's print)
DB2EXP = {c: {d: e for e, ds in EXP2DB[c].items() for d in ds} for c in CHS}
OUTSIDE = [(1, 1), (37, 11), (39, 11), (43, 24), (48, 2), (48, 10), (342, 1), (346, 2), (355, 6), (356, 5), (357, 27)]   # the ELEVEN rows READ WHOLE: the union of the two files beyond piskaot 306-341 (the dump's and the split's print)
EXCLUDED = []   # none known at the design — a translator's misprint is judged by the Hebrew at the whole read (sitting 18's lesson 4)
INTERPOLATION = []
CREDITED = {}   # under THE WHOLE-ROW RULE no spine row is credited: rows read before (the dump lists fourteen ledgers' seats among 306-341) are REREAD WHOLE here and marked so
TITLE = "Chapter 32 — the song: give ear, O heavens, and hear, O earth; the Rock whose work is perfect, a perverse and crooked generation; remember the days of old — the Most High divided the nations by the number of the children of Israel, the LORD's portion is His people; He found him in a desert land, as an eagle over her young, the LORD alone led him, honey from the rock, the blood of the grape; Jeshurun grew fat and kicked, forsook the God who made him, sacrificed to demons, to gods they knew not; the LORD saw and spurned, I will hide My face, a perverse generation, I will provoke them with a foolish nation, a fire kindled to the depths of Sheol, arrows spent, the teeth of beasts, the sword without and terror within; I would have said I will blot them out, but for the enemy's boast; a nation void of counsel — how should one chase a thousand unless their Rock had sold them; their vine of Sodom, their wine the venom of asps; vengeance is Mine and recompense, the LORD will judge His people when their power is gone — where are their gods who ate the fat of their sacrifices? See now that I, I am He, I kill and I make alive, I lift My hand to heaven, My glittering sword, vengeance on My adversaries, the blood of His servants — sing, O nations, of His people. Moses and Hoshea son of Nun spoke the song; set your heart to all these words, it is your life; and on that selfsame day: go up to Mount Nebo in the Abarim, see the land and die on the mountain as Aaron died on Hor, because you broke faith at the waters of Meribath-kadesh — you shall see the land from afar but not go there."
OUT = f'{ROOT}/logic/oral_triage/deu_32_haazinu_{DATE}.md'
PATCHED = bool(os.environ.get('DEU32_PATCHED'))   # the tail's flag: after the manifests and the seat, the drafts carry operators and the store its overrides
db = sqlite3.connect(f'file:{ROOT}/Data/tanakh.sqlite?mode=ro', uri=True)
VC = dict(db.execute("SELECT chapter, COUNT(*) FROM verses WHERE book='Deut' GROUP BY chapter").fetchall())
NV = {c: VC[c] for c in CHS}

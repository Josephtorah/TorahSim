import os as _os
_ROOT = _os.path.normpath(_os.path.join(_os.path.dirname(_os.path.abspath(__file__)), '..', '..', '..'))   # THE PORTABLE REPO (2026-09-15): the repo root from this file's own place
#!/usr/bin/env python3
# THE DEUTERONOMY WALK, sitting 15 — CHAPTERS 17-18, Deuteronomy 17:1-18:22 IN THE LEAN FORM (2026-09-24; the owner: "Reread and go" after the compaction at
# #210 — THE LEAN PASS's third sitting, the first on TWO chapters: ONE reading window (the ink, the shelf, the ledger, the freeze), one compile window, a short
# tail): THE INK of the two chapters, computed from the Tanakh DB, the snapshot store and the shelf's own bytes — never typed. Sitting 14's form (ch16_ink.py):
# the generic helpers copied by derive_ch17_ink.py from the forms' ch16_ink.py by content markers (the chapter substituted for the pair), the constants and
# every assert the two chapters' own, typed FROM THE PRINTS (ch17_dump0.out, ch18_dump0.out, ch17_measure_lean.out). THE TWO DIVISIONS AGREE in both chapters
# (20 = 20, cost 20; 22 = 22, cost 14) — the identity. THE SPINE IS ON THE TWO CHAPTERS — THIRTY-TWO piskaot 147-178 with 181 rows (106 + 75): sixteen heads
# computed in chapter 17 (147 on 17:1 … 162 on 17:20) and sixteen in chapter 18 (163 on 18:1 … 178 on 18:20), ALL IN VERSE ORDER, NO HEADLESS PISKA; 146 on
# 16:22 before, 179 on 19:1 after; no tail folded in either way (162's rows stop before 18:1's words, 178's before 19:1's; 163:1 and 179:1 open with their
# verses' citations). ELEVEN rows elsewhere cite the two chapters by the union of both files (six READ BEFORE at chapters 11-14, REREAD WHOLE; five fresh),
# NONE excluded. NO portion edge inside either chapter (Shoftim 16:18-21:9 holds both whole; the chapters the units, CHAPTER NUMBERS). The parser MEASURED on
# every verse — TWO NUMBER VERSES (17:2 [1] "one of your gates", 17:6 [2, 3, 1] "two witnesses or three … one witness"), no ordinal, no starred token, and
# 18:6's "from one of your gates" NOT read (the number word behind its prefix). THE STORE = THE DB at every verse (368 = 368; 304 = 304); ONE "?" gloss (18:19
# "I"). The hand's facts as asserts, run all at once by assert_driver.py.
import json, os, re, html, sqlite3, sys, io, contextlib, unicodedata, subprocess
from collections import Counter
ROOT = _ROOT
sys.path.insert(0, f'{ROOT}/World/step9')
DATE = '2026-09-24'
CHS = (17, 18)
UIDS = ['deu_17_courts_king', 'deu_18_levi_prophet']
SPANS = {'deu_17_courts_king': (17, 1, 20), 'deu_18_levi_prophet': (18, 1, 22)}
PREFIX = {'deu_17_courts_king': 'DV17', 'deu_18_levi_prophet': 'DV18'}
SPAN = [(17, v) for v in range(1, 21)] + [(18, v) for v in range(1, 23)]
PISKAOT = list(range(147, 179))   # THE SPINE ON THE TWO CHAPTERS: 147-162 chapter 17's sixteen heads, 163-178 chapter 18's sixteen (the A prints); 146 heads on 16:22, 179 on 19:1
PISKAOT_BY = {17: list(range(147, 163)), 18: list(range(163, 179))}
HEADLESS = []   # every piska of the span heads on its verse in the Hebrew (the dumps' prints)
SPINE_ROWS = {147: 7, 148: 10, 149: 7, 150: 3, 151: 3, 152: 15, 153: 5, 154: 5, 155: 9, 156: 6, 157: 10, 158: 4, 159: 4, 160: 8, 161: 5, 162: 5, 163: 4, 164: 3, 165: 14, 166: 9, 167: 2, 168: 4, 169: 3, 170: 3, 171: 11, 172: 5, 173: 4, 174: 2, 175: 2, 176: 5, 177: 1, 178: 3}   # rows per piska, both files (the I prints and the splitter's) — 106 + 75 = 181
PREV_CHAPTER_ROWS = []   # no tail folded in (146's row chapter 16's — asserted there; 162's rows stop before 18:1's words, 178's before 19:1's)
READ_ROWS = [(p, r) for p in PISKAOT for r in range(1, SPINE_ROWS[p] + 1)]   # 181 — this ledger's spine rows
EXP2DB = {17: {e: [e] for e in range(1, 21)}, 18: {e: [e] for e in range(1, 23)}}   # the identity in both chapters (chapter 5 the book's one split)
DB2EXP = {c: {d: e for e, ds in EXP2DB[c].items() for d in ds} for c in CHS}
# the Hebrew's book-named citations of the two chapters OUTSIDE the spine (the regex reads "(דברים יז ח)" etc.); three rows cite only in the English (190:3, 261:2, 71:9)
OUTSIDE_HE = [(37, 16, (17, 8)), (93, 6, (17, 4)), (99, 2, (17, 1)), (190, 7, (17, 4)), (306, 9, (17, 7)), (317, 2, (17, 8)), (352, 9, (17, 8)), (208, 1, (18, 7))]
OUTSIDE = [(37, 16), (71, 9), (93, 6), (99, 2), (190, 3), (190, 7), (208, 1), (261, 2), (306, 9), (317, 2), (352, 9)]   # the ELEVEN rows READ WHOLE: the union of both files beyond piskaot 147-178, joined over the two dumps
EXCLUDED = []   # every outside citation genuine
INTERPOLATION = []
CITED = {(37, 16): [(17, 8)], (71, 9): [(18, 3)], (93, 6): [(17, 4)], (99, 2): [(17, 1)], (190, 3): [(17, 6)], (190, 7): [(17, 4)], (208, 1): [(18, 7)], (261, 2): [(17, 1)], (306, 9): [(17, 7)], (317, 2): [(17, 8)], (352, 9): [(17, 8)]}
PRIOR_READ = {(37, 16): ['deu_11_ekev_reeh_2026-09-20.md'], (71, 9): ['deu_12_reeh_2026-09-20.md'], (93, 6): ['deu_13_reeh_2026-09-21.md'], (99, 2): ['deu_14_reeh_2026-09-21.md'], (190, 7): ['deu_13_reeh_2026-09-21.md'], (306, 9): ['deu_11_ekev_reeh_2026-09-20.md']}   # the six outside rows read before (computed from the ledgers, asserted) — REREAD WHOLE here
HEADS_ON = {37: (11, 10), 71: (12, 15), 93: (13, 14), 99: (14, 3), 190: (19, 17), 208: (21, 5), 261: (23, 19), 306: (32, 1), 317: (32, 14), 352: (33, 11)}
FRESH = [(190, 3), (208, 1), (261, 2), (317, 2), (352, 9)]
CREDITED = {}   # under THE WHOLE-ROW RULE no spine row is credited: the seven rows read before (148:8 at chapter 4; 147:2 at chapters 12 and 16; 149:1-2 at chapter 13; 147:3-4 at chapter 15; 171:6 at Genesis 31) are REREAD WHOLE here and marked so
TITLE = "Chapters 17-18 — You shall not sacrifice to the LORD your God an ox or a sheep with a blemish, any evil thing, for it is an abomination to Him. When a man or a woman in one of your gates does what is evil in His eyes, transgressing His covenant — going and serving other gods, the sun or the moon or the host of heaven, which I have not commanded — and it is told you and you inquire well and the thing is true, bring them out to your gates and stone them; by the mouth of two witnesses or three shall the dead die, never by one; the witnesses' hand first and all the people's after, and you shall purge the evil from your midst. When a matter is too hard for you in judgment, between blood and blood, plea and plea, stroke and stroke, rise and go up to the place the LORD will choose, to the priests the Levites and the judge of those days; do according to the sentence they declare from that place, the law they teach and the judgment they say; turn not from their word right or left; the man who acts presumptuously, not hearkening to the priest who stands to minister there or to the judge, shall die — all the people shall hear and fear. When you come into the land and say 'I will set a king over me like all the nations', set the king the LORD chooses, from among your brothers, never a foreigner; he shall not multiply horses nor return the people to Egypt for horses, since the LORD said you shall not go back that way; nor multiply wives, lest his heart turn; nor silver and gold; when he sits on his throne he shall write himself a copy of this law before the priests the Levites, keep it with him and read it all his days, to learn to fear the LORD and keep all these words, his heart not lifted above his brothers, that he and his sons may reign long. The priests the Levites, all the tribe of Levi, have no portion or inheritance with Israel — the fire offerings of the LORD and His inheritance they eat, the LORD is their inheritance as He spoke; the priests' due from the people who sacrifice, ox or sheep: the shoulder, the two cheeks and the maw; the first of your grain, wine and oil and the first of the fleece — for the LORD chose him of all the tribes to stand and minister in His name, he and his sons forever. The Levite who comes from any of your gates with all his soul's desire to the place shall minister in the LORD's name like all his brothers who stand there, and eat portion as portion, besides what comes of the fathers' houses. When you come into the land, learn not the abominations of the nations: none among you who passes his son or daughter through the fire, a diviner, a soothsayer, an augur, a sorcerer, a charmer, one who consults a ghost or a familiar spirit, or a necromancer — for these abominations the LORD drives them out before you; be whole with the LORD your God, who has not given you such. A prophet from your midst, of your brothers, like me, the LORD will raise up for you — hear him — as you asked at Horeb on the day of the assembly: 'let me not hear the voice of the LORD again nor see this great fire, lest I die'; and the LORD said they had spoken well: 'a prophet like you I will raise up from their brothers, I will put My words in his mouth, and he shall speak all I command him; whoever hearkens not to My words spoken in My name, I will require it of him; but the prophet who presumes to speak in My name what I commanded him not, or who speaks in the name of other gods, shall die'. And if you say in your heart, how shall we know the word the LORD has not spoken — what the prophet speaks in the LORD's name and it does not come to pass, that is the word the LORD has not spoken; the prophet spoke it presumptuously; you shall not fear him"
OUT = f'{ROOT}/logic/oral_triage/deu_17_18_shoftim_{DATE}.md'
PATCHED = bool(os.environ.get('DEU17_PATCHED'))   # the tail's flag: after the manifest and the seat, the drafts carry operators and the store its overrides
db = sqlite3.connect(f'file:{ROOT}/Data/tanakh.sqlite?mode=ro', uri=True)
VC = dict(db.execute("SELECT chapter, COUNT(*) FROM verses WHERE book='Deut' GROUP BY chapter").fetchall())
NV = {c: VC[c] for c in CHS}

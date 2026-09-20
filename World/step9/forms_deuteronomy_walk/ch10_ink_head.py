import os as _os
_ROOT = _os.path.normpath(_os.path.join(_os.path.dirname(_os.path.abspath(__file__)), '..', '..', '..'))   # THE PORTABLE REPO (2026-09-15): the repo root from this file's own place
#!/usr/bin/env python3
# THE DEUTERONOMY WALK, sitting 8 — CHAPTER 10, Deuteronomy 10:1-22 (2026-09-19; the owner: "Go"; ONE RUN under THE TWO-RUN RULE — the rereads, the
# measurements, the ink, the design, the rows, the ledger, the seat, the gates, the records): THE INK of the chapter, computed from the Tanakh DB, the
# snapshot store and the shelf's own bytes — never typed. Sitting 7's form (ch9_ink.py): the generic helpers copied by derive_ch10_ink.py from that file
# by content markers, the constants and every assert chapter 10's own, typed FROM THE PRINTS (ch10_dump0.out, ch10_measure1.out). THE TWO DIVISIONS AGREE
# (22 = 22; the alignment the identity, cost 14). THE SPINE IS SILENT ON THE CHAPTER (36 on 6:9, 37 on 11:10 — chapters 7 to 10 have none); THREE rows
# elsewhere cite it by the union of both files — act from love (10:20 at 32:1), the seventy who went down (10:22 at 301:4 and 311:5). The parser MEASURED on
# every verse — FIVE number verses (the two tablets [2] at 10:1 and [2, 2] at 10:3, the ten words [10] with the ordinal [1] at 10:4, the forty days [40, 40]
# at 10:10, the seventy [70] at 10:22), "swear" (10:20) no number; NO GAP. THE STORE = THE DB at every verse (no written/read pair; 324 tokens, 1,252
# letters; the four "?" glosses the store's split station name and its "I"). The hand's facts as asserts, run all at once by assert_driver.py.
import json, os, re, html, sqlite3, sys, io, contextlib, unicodedata, subprocess
from collections import Counter
ROOT = _ROOT
sys.path.insert(0, f'{ROOT}/World/step9')
DATE = '2026-09-19'
CH = 10
UIDS = ['deu_10_second_tablets']
SPANS = {'deu_10_second_tablets': (10, 1, 22)}
PREFIX = {'deu_10_second_tablets': 'DV10'}
PISKAOT = []   # NO piska head on the chapter (typed from ch10_dump0's A print: the heads by chapter (6, 6), (11, 21); the nearest 36 on 6:9, 37 on 11:10)
EXP2DB = {e: [e] for e in range(1, 23)}   # the identity — 22 = 22 (chapter 5 the book's one split)
DB2EXP = {d: e for e, ds in EXP2DB.items() for d in ds}
# the Hebrew's book-named citations of chapter 10 (the regex reads "(דברים י כ)" and "(דברים י כב)"); the English's "(Dt.10:n" — three rows, the same three
OUTSIDE_HE = [(32, 1, (10, 20)), (301, 4, (10, 22)), (311, 5, (10, 22))]
OUTSIDE_EN = [(32, 1, (10, 20)), (301, 4, (10, 22)), (311, 5, (10, 22))]
OUTSIDE = [(32, 1), (301, 4), (311, 5)]   # the THREE rows READ WHOLE: the union of both files
INTERPOLATION = []   # no translator's own citation of chapter 10
EXCLUDED = []   # no slip on chapter 10 (no cited verse beyond 22)
CITED = {(32, 1): [20], (301, 4): [22], (311, 5): [22]}
CITED_DB = {k: v[0] for k, v in CITED.items()}
PRIOR_READ = {(32, 1): 'deu_06_vaetchanan_2026-09-17.md', (311, 5): 'gen_25_babel_2026-08-25.md'}   # two read before (32:1 at sitting 4 on 6:5; 311:5 at a Genesis sitting by topic, credited at a second) — REREAD WHOLE here
HEADS_ON = {32: (6, 5), 301: (26, 5), 311: (32, 8)}   # every one of the three piskaot's first rows carries its head citation (asserted on the heads)
FRESH = OUTSIDE[:]   # every one of the three read whole this sitting
CREDITED = {}
TITLE = "Chapter 10 — The second tablets and the ark: hew two tablets like the first, make an ark of wood, the ten words written as the first writing, the tablets in the ark as the LORD commanded me; the stations and Aaron's death, Eleazar in his stead; the tribe of Levi separated to carry the ark and bless in His name, the LORD his inheritance; the third forty days, arise and go; what the LORD asks — to fear, walk, love, serve and keep; the heavens His, the fathers chosen, the foreskin of the heart; the God of gods who lifts no face and takes no bribe, the orphan, the widow and the stranger; fear, serve, cleave, swear; He is your praise — seventy souls to the stars of heaven"
OUT = f'{ROOT}/logic/oral_triage/deu_10_ekev_{DATE}.md'
db = sqlite3.connect(f'file:{ROOT}/Data/tanakh.sqlite?mode=ro', uri=True)

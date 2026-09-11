#!/usr/bin/env python3
# NUM 13:1-15:31 — SHELACH: THE SPIES, THE DECREE, THE LIBATIONS, THE STRANGER, THE CHALLAH, THE ERROR AND THE HIGH HAND (THE NUMBERS
# WALK sitting 4b, 2026-09-10; World/step9/NUMBERS_WALK.md "Sitting 4b"; 15:32-41 frozen at THE TENT sitting 3 and compiled by
# cold_run_mekoshesh). The fourth Numbers portion compiled after its walk, on the owner's ruling READ THEN COMPILE: the parser taught
# THE FRACTION before a measure noun, THE UNIT NOUN AS ONE (the tenth, the cubit by its points, the hin), THE DEFINITE ONE, the
# third-generation homograph, Sheshai and the tithe verb at this sitting (census_probes.py 109/109 after thirty-four rows failed first);
# the census set CALLED from Bamidbar, the idolatry column, the court's error and the karet class from the chatat engine, the olah's
# table from the offerings engine, the libation meal offering's adjuncts from the minchah engine; THE LIBATION TABLE computed from the
# ink's own numbers at every seat; the forty days and the thirty-eight years as TIMERS against Taanit 29a's day-stack. Five motions of
# the deliverable rule, the wrap the sixth; every cell cites its source; every token probed (zero-report law); effects on every cell (the
# effects law). Reading ledgers: the three logic/oral_triage/num_{13,14,15}_*_2026-09-10.md; the exam's docket:
# num_13_15_shelach_exam_2026-09-10.md (313 rows — 141 LAW, 45 DERIVATION, 31 DISPUTE, 96 CONTEXT).

# ---- THE HONEST-PAIRING GUARD ----------------------------------------------------------------------------
import os as _os, sys as _sys
_sys.path.insert(0, _os.path.dirname(_os.path.abspath(__file__)))
from compile_guards import check_honest_pairing as _chp
_P = _os.path.abspath(__file__)
GUARDED = _chp(_P, 'CASES', 2)
assert GUARDED == 172, ('the guard counted %d expectations, the tripwire holds 172' % GUARDED)   # the guard's own count on the first graded run
print('guard: %d expectations checked, every one a literal from the answer sheet [honest-pairing guard satisfied]' % GUARDED)
import sqlite3, sys, io, re, contextlib
from fractions import Fraction
import effects_layer as FX
import world_engine as WE
import cold_run_bamidbar as BM                   # THE EDGE: shelach -> bamidbar CALL, reference (14:29's census set)
import cold_run_chatat as CH                     # THE EDGE: shelach -> chatat CALL, reference (15:24-31's idolatry column, the court, the karet class)
import cold_run_offerings as OF                  # THE EDGE: shelach -> offerings CALL, reference (15:3, 15:8, 15:24's burnt offering)
import cold_run_minchah as MN                    # THE EDGE: shelach -> minchah CALL, reference (15:4's libation meal offering)
import cold_run_korach as KR                     # THE EDGE: shelach -> korach CALL, reference (15:20's 'as the terumah of the threshing floor' — Numbers 18's terumah: the OWED row of 4b PAID at 5b)

HERE = _os.path.dirname(_os.path.abspath(__file__))
# ONE copy of the numeral parser: the sequence runner's INK block executed here (the stitcher's way — no import edge)
_SRC = open(_os.path.join(HERE, 'cold_run_sequence.py'), encoding='utf-8').read()
_INK = {'re': re, 'sqlite3': sqlite3, 'os': _os, 'WE': WE}
exec(_SRC.split('# ==== INK BEGIN')[1].split('# ==== INK END ====')[0].split('\n', 1)[1], _INK)
ink_numbers, verse_words, ink_ordinals = _INK['ink_numbers'], _INK['verse_words'], _INK['ink_ordinals']

db = sqlite3.connect('<repo-old>/elijah_docket/tanakh.sqlite')

def strip(s):
    return ''.join(c for c in s if c != '/' and not (0x0591 <= ord(c) <= 0x05C7))

def verse_text(ch, vs, book='Num'):
    rows = db.execute("""SELECT w.he FROM words w JOIN verses v ON w.verse_id=v.id WHERE v.book=?
        AND v.chapter=? AND v.verse=? ORDER BY w.idx""", (book, ch, vs)).fetchall()
    return ' '.join(strip(h) for (h,) in rows)

def count_token(tok, books=None):
    n = 0
    for (he,) in db.execute("SELECT w.he FROM words w JOIN verses v ON w.verse_id=v.id" + (" WHERE v.book IN (%s)" % ','.join('?' * len(books)) if books else ""), tuple(books) if books else ()):
        if strip(he) == tok: n += 1
    return n

# ---- zero-report probes: the span's load-bearing tokens ---------------------------------------------------
PROBES = [
    ('ויתרו',    13, 2,  'that they may spy out — the ark\'s verb (10:33)'),
    ('לך',       13, 2,  'for yourself'),
    ('נשיא',     13, 2,  'a prince'),
    ('פארן',     13, 3,  'Paran'),
    ('הושע',     13, 8,  'Hoshea — before the renaming'),
    ('יהושע',    13, 16, 'Joshua — the new name given'),
    ('לתור',     13, 17, 'to spy out'),
    ('החזק',     13, 18, 'whether strong'),
    ('הרפה',     13, 18, 'or weak'),
    ('המעט',     13, 18, 'whether few'),
    ('הבמחנים',  13, 19, 'whether in camps'),
    ('במבצרים',  13, 19, 'or in fortresses'),
    ('השמנה',    13, 20, 'whether fat'),
    ('רזה',      13, 20, 'or lean'),
    ('בכורי',    13, 20, 'the first-ripe [grapes]'),
    ('צן',       13, 21, 'Zin'),
    ('ויבא',     13, 22, 'and HE came — the singular'),
    ('חברון',    13, 22, 'Hebron'),
    ('ששי',      13, 22, 'Sheshai — a name, not the ordinal'),
    ('צען',      13, 22, 'Zoan'),
    ('זמורה',    13, 23, 'a branch'),
    ('ואשכול',   13, 23, 'and a cluster — plene'),
    ('במוט',     13, 23, 'on a pole — the Kohathites\' bar'),
    ('בשנים',    13, 23, 'between two — the dual'),
    ('ארבעים',   13, 25, 'forty'),
    ('קדשה',     13, 26, 'to Kadesh'),
    ('זבת',      13, 27, 'flowing with'),
    ('עז',       13, 28, 'strong'),
    ('עמלק',     13, 29, 'Amalek'),
    ('ויהס',     13, 30, 'and he hushed'),
    ('ממנו',     13, 31, 'than us — or than Him'),
    ('דבת',      13, 32, 'an evil report — Joseph\'s word'),
    ('הנפילים',  13, 33, 'the Nephilim — plene'),
    ('כחגבים',   13, 33, 'as grasshoppers'),
    ('ויבכו',    14, 1,  'and they wept'),
    ('וילנו',    14, 2,  'and they murmured'),
    ('ראש',      14, 4,  'a head'),
    ('קרעו',     14, 6,  'they rent'),
    ('לחמנו',    14, 9,  'our bread'),
    ('לרגום',    14, 10, 'to stone'),
    ('ינאצני',   14, 11, 'will they scorn Me'),
    ('ואורשנו',  14, 12, 'and I will disinherit them'),
    ('יכלת',     14, 16, 'the ability — the feminine noun'),
    ('יגדל',     14, 17, 'let [the power] be great'),
    ('שלשים',    14, 18, 'the third generation — not thirty'),
    ('רבעים',    14, 18, 'the fourth generation'),
    ('סלחתי',    14, 20, 'I have pardoned — once in the Bible'),
    ('עשר',      14, 22, 'ten [times]'),
    ('עקב',      14, 24, 'because'),
    ('סוף',      14, 25, '[the Red] Sea'),
    ('נאם',      14, 28, 'says [the LORD]'),
    ('פגריכם',   14, 29, 'your carcasses'),
    ('לבז',      14, 31, 'a prey'),
    ('רעים',     14, 33, 'shepherds'),
    ('לשנה',     14, 34, 'for a year'),
    ('תנואתי',   14, 34, 'My alienation'),
    ('במגפה',    14, 37, 'by the plague'),
    ('חיו',      14, 38, 'lived'),
    ('ויתאבלו',  14, 39, 'and they mourned'),
    ('ויעפלו',   14, 44, 'and they presumed'),
    ('ויכתום',   14, 45, 'and beat them down'),
    ('החרמה',    14, 45, 'to Hormah — the name before its naming'),
    ('מושבתיכם', 15, 2,  'your dwellings'),
    ('לפלא',     15, 3,  'to fulfil [a vow]'),
    ('עשרון',    15, 4,  'a tenth — the unit noun'),
    ('ברבעית',   15, 4,  'with a quarter of — the fraction'),
    ('רביעית',   15, 5,  'a quarter of — the plene spelling'),
    ('האחד',     15, 5,  'the one [lamb] — the definite one'),
    ('שלשית',    15, 6,  'a third of'),
    ('חצי',      15, 9,  'half of'),
    ('ככה',      15, 11, 'so'),
    ('האזרח',    15, 13, 'the native-born'),
    ('הקהל',     15, 15, 'the assembly'),
    ('תורה',     15, 16, 'one Torah'),
    ('בבאכם',    15, 18, 'upon your coming — the varied formula'),
    ('ערסתכם',   15, 20, 'your dough'),
    ('חלה',      15, 20, 'a cake'),
    ('גרן',      15, 20, 'the threshing floor'),
    ('תשגו',     15, 22, 'you err'),
    ('מעיני',    15, 24, 'from the eyes of'),
    ('לחטת',     15, 24, 'for a sin offering — without the aleph'),
    ('ונסלח',    15, 25, 'and it shall be forgiven'),
    ('רמה',      15, 30, 'high [hand]'),
    ('מגדף',     15, 30, 'blasphemes — once in the Bible'),
    ('הכרת',     15, 31, 'cut off'),
    ('תכרת',     15, 31, 'shall be cut off'),
]
for tok, ch, vs, note in PROBES:
    if tok not in verse_text(ch, vs).split():
        sys.exit('ZERO-REPORT LAW: probe %r (%s) failed at Num %d:%d — refusing to run' % (tok, note, ch, vs))
print('probes: all %d token probes fired  [zero-report law satisfied]\n' % len(PROBES))

P = []  # the provenance trail of the case being run
def ink(ref, note):  P.append(('INK',  'Num %s — %s' % (ref, note)))
def move(src, note): P.append(('MOVE', '%s — %s' % (src, note)))
def dat(note):       P.append(('DATA', note))

def out(verdict, effects):
    """verdict + registry-validated effects (the engine contract)"""
    FX.validate([e for e in effects if e != FX.NONE])
    return verdict, effects, list(P)

# ---- THE NUMBERS, computed from the ink by the engine's parser (live; the probes' expectations are the ink's) ----
def N(book, ch, vs): return ink_numbers(verse_words(book, ch, vs))
ONE_ONE = N('Num', 13, 2); SEVEN = N('Num', 13, 22); POLE = N('Num', 13, 23); FORTY = N('Num', 13, 25); AS_ONE = N('Num', 14, 15)
GENERATIONS = N('Num', 14, 18); TEN = N('Num', 14, 22); TWENTY = N('Num', 14, 29); FORTY_YEARS = N('Num', 14, 33); DAY_YEAR = N('Num', 14, 34)
LAMB_A = N('Num', 15, 4); LAMB_B = N('Num', 15, 5); RAM_A = N('Num', 15, 6); RAM_B = N('Num', 15, 7); BULL_A = N('Num', 15, 9); BULL_B = N('Num', 15, 10)
ONE_OX_RAM = N('Num', 15, 11); MONTH_ROW = N('Num', 28, 14); TAMID_ROW = N('Exod', 29, 40); OMER_ROW = N('Lev', 23, 13); DAILY_ROW = N('Num', 28, 5) + N('Num', 28, 7)
SHESHAI = ink_ordinals(verse_words('Num', 13, 22))
assert ONE_ONE == [1, 1] and SEVEN == [7] and POLE == [1, 2] and FORTY == [40] and AS_ONE == [1] and GENERATIONS == [] and SHESHAI == [], (ONE_ONE, SEVEN, POLE, FORTY, AS_ONE, GENERATIONS, SHESHAI)
assert TEN == [10] and TWENTY == [20] and FORTY_YEARS == [40] and DAY_YEAR == [40, 40], (TEN, TWENTY, FORTY_YEARS, DAY_YEAR)
assert LAMB_A == [1, Fraction(1, 4)] and LAMB_B == [Fraction(1, 4), 1] and RAM_A == [2, Fraction(1, 3)] and RAM_B == [Fraction(1, 3)], (LAMB_A, LAMB_B, RAM_A, RAM_B)
assert BULL_A == [3, Fraction(1, 2)] and BULL_B == [Fraction(1, 2)] and ONE_OX_RAM == [1, 1], (BULL_A, BULL_B, ONE_OX_RAM)
# THE LIBATION TABLE — computed from the ink at 15:4-10 (flour in tenths, oil in hin, wine in hin), never typed
TABLE = {'lamb': (LAMB_A[0], LAMB_A[1], LAMB_B[0]), 'ram': (RAM_A[0], RAM_A[1], RAM_B[0]), 'bull': (BULL_A[0], BULL_A[1], BULL_B[0])}
assert MONTH_ROW == [TABLE['bull'][2], TABLE['ram'][2], TABLE['lamb'][2]], MONTH_ROW                  # 28:14's three rows in the ink's order: bull, ram, lamb
assert TAMID_ROW == [TABLE['lamb'][0], TABLE['lamb'][1], TABLE['lamb'][2], 1] and DAILY_ROW == [Fraction(1, 10), Fraction(1, 4), Fraction(1, 4), 1], (TAMID_ROW, DAILY_ROW)   # Exod 29:40 and Num 28:5-7: the lamb's row with the definite one; 28:5 the tenth as a FRACTION of the ephah
assert OMER_ROW == [2, Fraction(1, 4)], OMER_ROW                                                    # Lev 23:13: the omer's lamb — the flour DOUBLED, the wine the lamb's (Mishnah Menachot 9:4)
TRIBE_LINES = [v for v in range(4, 16) if 'למטה' in verse_text(13, v).split()[:3]]                    # 13:4 opens 'and these are their names, for the tribe of Reuben' — the tribe-word inside the first three (the first run read the head word alone)
SPY_TRIBES = [(lambda ws: ws[ws.index('למטה') + 1])(verse_text(13, v).split()) for v in TRIBE_LINES]
assert len(TRIBE_LINES) == 12 and 'לוי' not in SPY_TRIBES and SPY_TRIBES[7] == 'יוסף', (TRIBE_LINES, SPY_TRIBES)   # twelve lines, Levi absent, Joseph's name over Manasseh (13:11)
QUESTIONS = [w for v in (18, 19, 20) for w in verse_text(13, v).split() if w in ('החזק', 'הרפה', 'המעט', 'הטובה', 'הבמחנים', 'השמנה', 'היש')]
assert len(QUESTIONS) == 7, QUESTIONS                                                                # the seven interrogatives (sitting 4's count)
_ORDER = [('Exod', c, v) for c in range(1, 41) for v in range(1, 60)] + [('Lev', c, v) for c in range(1, 28) for v in range(1, 60)] + [('Num', c, v) for c in range(1, 37) for v in range(1, 90)]
JOSHUA_BEFORE = [(b, c, v) for (b, c, v) in _ORDER if (b, c, v) < ('Num', 13, 16) and db.execute("SELECT 1 FROM verses WHERE book=? AND chapter=? AND verse=?", (b, c, v)).fetchone() and any(w.lstrip('ו') == 'יהושע' for w in verse_text(c, v, b).split())]   # Exod 24:13's 'AND Joshua' carries the vav — the first run found seven
assert len(JOSHUA_BEFORE) == 8, JOSHUA_BEFORE                                                       # the new name at eight seats before the verse that gives it
assert any(w.lstrip('ו') == 'הושע' for w in verse_text(32, 44, 'Deut').split()), verse_text(32, 44, 'Deut')   # the old name again at the Torah's last song — 'AND Hoshea' with the vav (the first run read the bare form)
E34 = verse_text(34, 6, 'Exod').split() + verse_text(34, 7, 'Exod').split(); N18 = verse_text(14, 18).split()
def subsequence(a, b):
    i = 0
    for w in b:
        if i < len(a) and a[i] == w: i += 1
    return i == len(a)
DROPPED = [x for x in E34 if x not in N18]
assert subsequence(N18, E34) and [x for x in N18 if x not in E34] == [] and len(DROPPED) == 11 and (len(E34), len(N18)) == (37, 20), (DROPPED, len(E34), len(N18))   # the attributes ABRIDGED by pure deletion: eleven DISTINCT words dropped (seventeen tokens — the doubled name, 'upon', 'kindness', 'sons', 'iniquity' repeat), none added (sitting 4's measurement; the first run had typed the token difference)
THIS_WILDERNESS = [v for v in range(1, 46) if 'במדבר הזה' in verse_text(14, v)]
assert THIS_WILDERNESS == [2, 29, 32, 35], THIS_WILDERNESS                                          # measure for measure stated by the ink: 14:2 returned at 14:29, 14:32, 14:35
IN_ERROR = sum(verse_text(15, v).split().count('בשגגה') for v in (27, 28, 29))
ONCE = {tok: count_token(tok) for tok in ('לחטת', 'מגדף', 'סלחתי')}
assert IN_ERROR == 3 and ONCE == {'לחטת': 1, 'מגדף': 1, 'סלחתי': 1}, (IN_ERROR, ONCE)                # 'in error' thrice fenced; the aleph dropped once; 'blasphemes' once; 'I have pardoned' once
DOUGH = sorted({strip(he) for (he,) in db.execute("SELECT w.he FROM words w") if re.search('ערי?ס', strip(he))})   # Neh 10:38's plene form carries a yod — the first run's bare stem found three
assert len(DOUGH) == 4, DOUGH                                                                        # the dough-word four spellings in the Tanakh (Num 15:20, 15:21; Ezek 44:30; Neh 10:38)
HIN_LOGS = 12   # DATA: Mishnah Menachot 9:2 — the hin's twelve logs (the data channel's measure)
LOGS = {k: (int(HIN_LOGS * oil), int(HIN_LOGS * wine)) for k, (flour, oil, wine) in TABLE.items()}
assert LOGS == {'lamb': (3, 3), 'ram': (4, 4), 'bull': (6, 6)}, LOGS                                 # the answer sheet's logs (Mishnah Menachot 9:2-3) from the ink's fractions
RATIO = {k: Fraction(LOGS[k][0], TABLE[k][0]) for k in TABLE}                                       # oil logs per tenth of flour — the mixing rule's ground (Mishnah Menachot 9:4)
SUKKOT_SABBATH = 13 * TABLE['bull'][0] + 2 * TABLE['ram'][0] + 14 * TABLE['lamb'][0] + 2 * TABLE['lamb'][0] + 2 * TABLE['lamb'][0]
assert SUKKOT_SABBATH == 61, SUKKOT_SABBATH                                                          # Mishnah Menachot 12:4's sixty-one tenths from the table
_W0 = WE.World(era='shelach: the calendar', epoch='exodus')
SENDING = _W0.clock.day_in('exodus', 2, 3, 29); RETURN_DAY = _W0.clock.day_in('exodus', 2, 5, 9)
DUE_38 = _W0.clock.calendar.add(RETURN_DAY, 38, 'year'); _EX = _W0.clock.eras['exodus']
assert RETURN_DAY - SENDING == 39 and _EX.date(SENDING + 40) == (2, 5, 10) and _EX.date(DUE_38) == (40, 5, 9) and _EX.year(RETURN_DAY) == 2, (RETURN_DAY - SENDING, _EX.date(SENDING + 40), _EX.date(DUE_38))

# =====================================================================
# Motion 2 — THE DATA: the parameter rows (the tradition's own vocabulary; the running setting first)
# =====================================================================
DATA = {
    'hebron_visitor': {'value': 'Caleb alone', 'settings': {'Caleb alone': "Rava (Sotah 34b:7) — 'HE came to Hebron': Caleb separated from the counsel and prostrated himself on the graves of the forefathers", 'they came': "the plain plural of the verse's other verbs"}, 'source': "13:22 — the singular verb the ink's, the visitor the shelf's"},
    'hebron_before_zoan': {'value': 'seven times more fertile', 'settings': {'seven times more fertile': "Sotah 34b:11; Ketubot 112a:8 — 'built' cannot be literal: Canaan is Ham's youngest", 'seven years earlier': "the plain reading"}, 'source': "13:22 'built seven years before Zoan' — the parser's seven"},
    'cluster_bearers': {'value': 8, 'settings': {'8': "Sotah 34a:9 (the baraita continued) — the cluster on two poles, eight men; one the pomegranates, one the figs; Joshua and Caleb carried nothing", '4': "the first reading of 'on a pole between two' — two poles, four men (34a:9)"}, 'source': "13:23 — the parser's [1, 2]"},
    'cluster_weight': {'value': 480, 'settings': {'480': "Sotah 34a:9 — four hundred and eighty seah, from the bearers' count"}, 'source': "the shelf's arithmetic on the bearers"},
    'return_day': {'value': (2, 5, 9), 'settings': {'(2, 5, 9)': "Taanit 29a:5 — the baraita: sent on the twenty-ninth of Sivan, returned 'at the end of forty days' on the Ninth of Av; Mishnah Ta'anit 4:6 the decree's day; Sotah 35a:11 the eve; 29a:7 that night"}, 'source': "13:25 — the tape's reading-placed marker"},
    'tammuz_length': {'value': 29, 'settings': {'29': "the modeled alternation (calendar_parameters month_rounding) — the running setting: the forty-day timer fires at (2, 5, 10)", '30': "Abaye (Taanit 29a:6) — 'Tammuz of that year was made full', Lam 1:15: the fortieth day the ninth itself"}, 'source': "the calendar registry's row tammuz_length; CF2"},
    'the_ten_trials': {'value': 10, 'settings': {'10': "Arakhin 15a-b (R. Yehuda's list): two at the sea, two at the water, two at the manna, two at the quail, the calf, the spies; Pirkei Avot 5:4 the answer sheet"}, 'source': "14:22 'these ten times' — the parser's ten; the ledger's tested_the_lord count graded at CF6"},
    'congregation': {'value': 10, 'settings': {'10': "Mishnah Sanhedrin 1:6; Berakhot 21b:5; Megillah 23b:8; Sanhedrin 74b:3 — the twelve less Joshua and Caleb"}, 'source': "14:27 'this evil congregation'"},
    'deaths_ceased': {'value': (40, 5, 15), 'settings': {'(40, 5, 15)': "Bava Batra 121a:9 (Rav Nachman); Taanit 30b:12 (R. Yochanan) — the fifteenth of Av the day the dying in the wilderness ceased; Deut 2:16-17 the speech resumed"}, 'source': "the decree's timer due (40, 5, 9) six days before it"},
    'wilderness_share': {'value': 'no share', 'settings': {'no share': "R. Akiva (Mishnah Sanhedrin 10:3; Sanhedrin 110b:2) — 'in this wilderness they shall be consumed, and there they shall die'; Ps 95:11", 'a share': "R. Eliezer — Ps 50:5 'gather My pious to Me'; R. Yehoshua ben Korcha (Tosefta Sanhedrin 13:1)"}, 'source': "14:35"},
    'spies_share': {'value': 'no share', 'settings': {'no share': "Mishnah Sanhedrin 10:3; Sanhedrin 108a:2, 109b:10 — 'died' this world, 'by plague' the next"}, 'source': "14:37"},
    'spies_death_mode': {'value': 'the tongue to the navel', 'settings': {'the tongue to the navel': "R. Sheila of Kefar Temarta (Sotah 35a:13) — the tongue stretched to the navel, worms between", 'diphtheria': "Rav Nachman bar Yitzchak (35a:13)"}, 'source': "14:37 'by the plague before the LORD' — an unusual death (Reish Lakish)"},
    'count_from': {'value': 'the exodus', 'settings': {'the exodus': "Deut 2:14's thirty-eight from Kadesh-barnea to Zered — the forty includes the two years elapsed (40 − 38 = 2 = the era's year at the decree)", 'the decree': "the plain forty from 14:34's own day — (42, 5, 9)"}, 'source': "14:33-34 against Deut 2:14 (the retelling's ink)"},
    'hin_in_logs': {'value': 12, 'settings': {'12': "Mishnah Menachot 9:2 — the hin vessel twelve logs; the half six, the third four, the quarter three (R. Shimon: no hin vessel, the gradations)"}, 'source': "the table's fractions of the hin"},
    'libation_floors': {'value': [3, 4, 6], 'settings': {'[3, 4, 6]': "Mishnah Menachot 12:4, 13:5; Menachot 104a:10-11, 107a:11-12 — three, four, six logs and beyond, never one, two or five: the lamb's, the ram's, the bull's"}, 'source': "15:13 'all the home-born shall do these' with 28:14's 'shall be'"},
    'oil_donation': {'value': 'wine only', 'settings': {'wine only': "R. Akiva (Mishnah Menachot 12:5) — oil never comes alone with its obligation", 'oil too': "R. Tarfon; Rabbi three logs from 15:13 (Menachot 107a:17; Zevachim 91b:10), the Rabbis one log"}, 'source': "15:13"},
    'libations_from': {'value': 'the entry', 'settings': {'the entry': "Zevachim 111a:7 — 'when you come into the land': the libations began at the entry, on the great public altar; none in the wilderness", 'inheritance and settlement': "R. Yishmael (Kiddushin 37b:1) — where coming AND dwelling are written"}, 'source': "15:2 'when you come into the land of your dwellings' — the cell's own gate"},
    'altar_eras': {'value': 'wilderness forbidden; Gilgal permitted; Shiloh forbidden; Nov and Gibeon permitted; Jerusalem forbidden forever', 'settings': {'wilderness forbidden; Gilgal permitted; Shiloh forbidden; Nov and Gibeon permitted; Jerusalem forbidden forever': "Mishnah Zevachim 14:4-8 — the high places' eras; 14:10 the private altar's omissions"}, 'source': "the altar the libations are poured on (Zevachim 111a)"},
    'which_take_libations': {'value': 'all but the firstborn, the tithe, the Passover, the sin offering and the guilt offering; the leper\'s chatat and asham do', 'settings': {"all but the firstborn, the tithe, the Passover, the sin offering and the guilt offering; the leper's chatat and asham do": "Mishnah Menachot 9:6; Menachot 90b:6-91a:27 — the baraita on 15:3-5 (the vow, the gift, the festivals; the festival goats excluded at 15:8; the leper's three from 'the burnt offering or the sacrifice, for the one lamb')"}, 'source': "15:3-5, 15:8"},
    'lamb_and_ram_ages': {'value': 'lambs to a year; rams from thirteen months and a day', 'settings': {'lambs to a year; rams from thirteen months and a day': "Mishnah Parah 1:3 — day to day; the thirteen-month animal the palges, invalid as either; its libation a ram's (Chullin 23a:6)"}, 'source': "15:5-6, 15:11 'the one lamb', 'the one ram'"},
    'gentile_libations': {'value': 'the public pays', 'settings': {'the public pays': "Mishnah Shekalim 7:6 (R. Shimon's ordinance) — a gentile's olah from abroad without money for its libations: from the treasury; no independent libations for a gentile (Menachot 73b:14; Zevachim 45a:14; Temurah 3a:10)"}, 'source': "15:11, 15:13"},
    'convert_offering': {'value': 'a beast olah, or a bird pair both olot', 'settings': {'a beast olah, or a bird pair both olot': "Keritot 8b:18-9a:4 — as you entered the covenant (Exod 24:5); the bird burnt offering wholly for the LORD; Rabbi: circumcision, immersion, the sprinkling of blood; Mishnah Kinnim 1:1 vows all olot", 'a quarter-dinar today': "Keritot 9a:10 — set aside for the pair; R. Shimon annulled it"}, 'source': "15:14-16"},
    'convert_congregation': {'value': 'congregation', 'settings': {'congregation': "R. Yehuda (Kiddushin 73a:4) — 'as for the congregation, one statute for you and for the stranger'", 'not congregation': "R. Yosei — 'one statute' interrupts"}, 'source': "15:15"},
    'challah_measure': {'value': {'householder': Fraction(1, 24), 'baker': Fraction(1, 48)}, 'settings': {"{'householder': 1/24, 'baker': 1/48}": "Mishnah Challah 2:7 — one twenty-fourth for oneself or a banquet; one forty-eighth for the baker and the market; impure unwittingly 1/48, intentionally 1/24"}, 'source': "15:20 — no measure in the ink"},
    'challah_minimum': {'value': 'five quarters of a kav', 'settings': {'five quarters of a kav': "Mishnah Challah 2:6; Shabbat 15a:3; Tosefta Eduyot 1:1 — Shammai a kav, Hillel two, the Sages a kav and a half = the wilderness omer (Exod 16:36 'a tenth of the ephah'), recalculated five quarters (R. Yosei: and a bit more)"}, 'source': "15:20 'your dough' — the omer (Menachot 67a:6)"},
    'terumah_measure': {'value': {'generous': Fraction(1, 40), 'average': Fraction(1, 50), 'stingy': Fraction(1, 60)}, 'settings': {"{'generous': 1/40, 'average': 1/50, 'stingy': 1/60}": "Mishnah Terumot 4:3 (Beit Shammai 1/30) — the terumah's measure has no ink floor; 4:4 the messenger's average"}, 'source': "15:20 'as the terumah of the threshing floor' — Numbers 18's terumah: OWED to Korach's compile at 4b, PAID at 5b (2026-09-10) — the row's home is cold_run_korach.py's DATA, this copy the placeholder"},
    'outside_produce': {'value': 'in liable; out exempt', 'settings': {'in liable; out exempt': "Mishnah Challah 2:1 — R. Akiva: taken out exempt", 'in liable; out liable': "R. Eliezer"}, 'source': "15:18 'the land'"},
    'territories': {'value': 'the land to Chezib one; to the river and Amanah two; beyond two, the measures reversed', 'settings': {'the land to Chezib one; to the river and Amanah two; beyond two, the measures reversed': "Mishnah Challah 4:8 (Rabban Gamliel) — one for the fire, one for the priest; 4:7 Syria's two"}, 'source': "15:21 'throughout your generations' — outside the land by the rabbis' word"},
    'challah_today': {'value': 'rabbinic', 'settings': {'rabbinic': "Ketubot 25a:11; Niddah 47a:7 — 'when you come' = the coming of all of you; Ezra's return partial"}, 'source': "15:18-19"},
    'tribe_table': {'value': 'a bull and a goat (R. Meir)', 'settings': {'a bull and a goat (R. Meir)': "Mishnah Horayot 1:5 — the court's; carried in the chatat engine (court({'sin': 'idolatry'}))", 'twelve (R. Yehuda)': "each tribe a congregation — twelve bulls and twelve goats", 'thirteen (R. Shimon)': "the tribes and the court"}, 'source': "15:24 — the chatat engine's row by CALL"},
    'idolatry_principle': {'value': 'one sin offering', 'settings': {'one sin offering': "Mishnah Shabbat 7:1's analogue (Shabbat 68b-69a) — one who forgot the principle of idolatry brings one", 'prior knowledge required': "Munbaz (Shabbat 68b:6) — the unwitting juxtaposed to the intentional at 15:29-30"}, 'source': "15:22-31"},
    'karet_reading': {'value': 'this world and the next', 'settings': {'this world and the next': "R. Akiva (Sanhedrin 64b:21, 90b:18) — 'cut off' this world, 'shall be cut off' the World-to-Come", 'the language of men': "R. Yishmael (64b:22) — the doubling teaches nothing; 15:30's 'venikhreta' this world, 15:31's the next", 'before and after Yom Kippur': "Rabbi (Shevuot 13a:2) — the day does not atone for the high-handed"}, 'source': "15:31 'cut off, shall be cut off' — MIDDOT.md's governance row"},
    'despiser': {'value': 'who says the Torah is not from Heaven', 'settings': {'who says the Torah is not from Heaven': "Sanhedrin 99a:17 (the baraita)", 'the Epicurean': "99a:17 alternatively", 'who uncovers faces in the Torah': "Shevuot 13a:2 (Rabbi); Pirkei Avot 3:11 (R. Elazar of Modiin)", 'Manasseh': "Sanhedrin 99b:4 — the exemplar"}, 'source': "15:31 'despised the word of the LORD'"},
    'yoke': {'value': 'the yoke, the covenant, the faces', 'settings': {'the yoke, the covenant, the faces': "Shevuot 13a:2 — 'despised the word' = throws off the yoke, uncovers faces; 'breached His commandment' = circumcision; Pirkei Avot 3:11's five"}, 'source': "15:31"},
    'blasphemer_offering': {'value': 'none', 'settings': {'none': "the Rabbis (Mishnah Keritot 1:2; Keritot 2a:5, 7a:23) — 'one law for him who DOES': no act, no sin offering", 'an offering': "R. Akiva (Keritot 7b:1) — the karet written in the offering's passage"}, 'source': "15:29-30"},
    'blasphemer_identity': {'value': 'the curser of the Name', 'settings': {'the curser of the Name': "the Rabbis (Keritot 7b:6); Isi ben Yehuda (7b:4); Pesachim 93b:1 with Lev 24:15", 'the idolater': "R. Elazar ben Azarya (Keritot 7b:6); Sifrei 112:1"}, 'source': "15:30 'blasphemes the LORD'"},
    'owner_piggul': {'value': 'the performer only', 'settings': {'the performer only': "the mishna (Zevachim 47a)", 'the owner too': "R. Elazar son of R. Yosei (Zevachim 47a:3) — 'he who sacrifices shall sacrifice his offering'"}, 'source': "15:4"},
    'idolatry_goat_semikhah': {'value': 'no laying of hands', 'settings': {'no laying of hands': "Mishnah Menachot 9:7 — the communal offerings save the court's bull and the scapegoat", 'laying of hands': "R. Shimon (Menachot 92a:2) — the idolatry goat too"}, 'source': "15:24"},
    'anointed_idolatry_trigger': {'value': 'an erroneous ruling with an unwitting act', 'settings': {'an erroneous ruling with an unwitting act': "Mishnah Horayot 2:1-3 — the anointed like the court", 'an unwitting act alone': "Rabbi (Horayot 7b:19) — 'when he sins unwittingly'"}, 'source': "15:27-28"},
}
assert all('value' in r and 'settings' in r and 'source' in r for r in DATA.values()) and len(DATA) == 39, len(DATA)   # the first run counted the rows


# =====================================================================
# Motion 1 — THE FUNCTION, compiled from the ink (F1-F7)
# =====================================================================
# ===== F1: THE SPIES (Num 13:1-33) ==========================================================================
def spies(case, data):
    del P[:]
    ask = case['ask']
    if ask == 'send_for_yourself':
        ink('13:2', '"send FOR YOURSELF men" — the sending Moses\' own; Deut 1:22-23 the people\'s asking, "good in my eyes"'); move('Sotah 34b:3 (Reish Lakish)', 'at your discretion, not a divine command')
        return out("at Moses' discretion — 'for yourself' (Reish Lakish); the people's asking (Deut 1:22)", [FX.NONE])
    if ask == 'one_per_tribe':
        ink('13:2', '"one man, one man for his fathers\' tribe... every one a prince" — the parser\'s [1, 1] the distributive'); ink('13:4-15', 'twelve tribe-lines computed: %s; Levi absent' % SPY_TRIBES)
        return out('12 — one man per tribe, princes; Levi absent', [FX.NONE])
    if ask == 'fourth_order':
        ink('13:4-15', 'the tribes in the spies\' order: %s — a fourth order of the twelve (1:5-15, 2:3-31, 7:12-83 the others); Joseph named over Manasseh at 13:11' % SPY_TRIBES)
        return out('a fourth order of the twelve — Reuben, Simeon, Judah, Issachar, Ephraim, Benjamin, Zebulun, Manasseh under Joseph, Dan, Asher, Naphtali, Gad', [FX.NONE])
    if ask == 'joshua_name':
        ink('13:16', '"and Moses called Hoshea son of Nun Joshua" — the new name at %d seats BEFORE this verse (%s); Hoshea again at Deut 32:44' % (len(JOSHUA_BEFORE), ', '.join('%s %d:%d' % s for s in JOSHUA_BEFORE)))
        move('Sotah 34b:8', 'the name a prayer — the LORD will save you from the spies\' counsel'); move('Tosefta Berakhot 1:15', 'Hoshea again in his praise: the same man before and after')
        return out('Hoshea to Joshua at 13:16 — the new name at 8 seats before it, the old at Deut 32:44 (the same man)', [FX.NONE])
    if ask == 'questionnaire':
        ink('13:18-20', 'the seven interrogatives computed: %s — strong or weak, few or many, good or bad, camps or fortresses, fat or lean, trees or none' % QUESTIONS)
        return out('7 questions — strong or weak, few or many, good or bad, camps or fortresses, fat or lean, trees or none; and the fruit', [FX.NONE])
    if ask == 'report_answers':
        ink('13:27-29', 'the report answers the questionnaire: fat (milk and honey, the fruit), strong (the people fierce, the Anak), fortified (the cities great), the map (Amalek south; the Hittite, Jebusite, Amorite in the mountain; the Canaanite by the sea and the Jordan)')
        return out('the report answers: fat; strong; fortified; the Anak; the map — Amalek south, the mountain peoples, the Canaanite by the sea and the Jordan', [FX.NONE])
    if ask == 'hebron_visitor':
        ink('13:22', '"they went up by the south, and HE came to Hebron" — the singular verb between plurals'); dat('the row hebron_visitor = %s' % data['hebron_visitor']['value'])
        return out("Caleb alone at the graves (Rava, Sotah 34b:7) — the singular verb the ink's", [FX.NONE])
    if ask == 'hebron_zoan':
        ink('13:22', '"Hebron was built seven years before Zoan of Egypt" — the parser\'s %s' % SEVEN); dat('the row hebron_before_zoan = %s' % data['hebron_before_zoan']['value']); move('Sotah 34b:11; Ketubot 112a:8', 'Canaan Ham\'s youngest — seven times more fertile')
        return out('7 — built seven years before Zoan: sevenfold fertility (Sotah 34b:11; Ketubot 112a)', [FX.NONE])
    if ask == 'cluster':
        ink('13:23', '"they carried it on a pole between two" — the parser\'s %s (the dual)' % POLE); dat('the rows cluster_bearers = %s, cluster_weight = %s' % (data['cluster_bearers']['value'], data['cluster_weight']['value']))
        return out('on a pole between two — two poles, eight bearers (Sotah 34a); 480 seah', [FX.NONE])
    if ask == 'eshcol':
        ink('13:24', '"that place he called the wadi of Eshcol because of the cluster" — named after its use; Deut 1:24')
        return out('named after the cluster (13:24); Deut 1:24', [FX.NONE])
    if ask == 'forty_days':
        ink('13:25', '"at the end of forty days" — %s; 14:34 a day for a year' % FORTY)
        return out('40 days (13:25) — the timer; a day for a year (14:34)', [FX.NONE])
    if ask == 'going_like_coming':
        ink('13:25-26', '"and they went and came"'); move('Sotah 35a:1 (R. Shimon ben Yochai)', 'the going likened to the coming — with wicked counsel')
        return out('the going with wicked counsel like the coming (R. Shimon ben Yochai, Sotah 35a:1)', [FX.NONE])
    if ask == 'report_form':
        ink('13:27-28', 'the praise first ("flowing with milk and honey"), then "but the people are strong"'); move('Sotah 35a:2 (R. Meir)', 'a slander that does not begin with truth does not stand')
        return out('truth first, then the slander — a slander that does not begin with truth does not stand (R. Meir)', ['evil_report_spread'])
    if ask == 'caleb_hushed':
        ink('13:30', '"and Caleb hushed the people toward Moses" — "we shall surely go up", two doubled infinitives'); move('Sotah 35a:3-6 (Rabba)', 'persuaded them — the ruse: is this the only thing the son of Amram did to us?')
        return out('persuaded them (Rabba) — the ruse: is this the only thing the son of Amram did?', ['plea_made'])
    if ask == 'stronger_than':
        ink('13:31', '"for they are stronger than us" — the same letters read "than Him"'); move('Sotah 35a:7; Arakhin 15a:12 (R. Chanina bar Pappa)', 'the revocalization — heresy: the Owner cannot remove His vessels (M-16\'s class)')
        return out("stronger than us, read stronger than Him — heresy (R. Chanina bar Pappa; M-16's class)", [FX.NONE])
    if ask == 'punished_for':
        ink('14:37', '"those who brought out the evil report of the land died" — the report named, not the blasphemy'); move('Arakhin 15a:13 (Rabba / Reish Lakish)', 'punished for the evil report')
        return out('the evil report (14:37), not the blasphemy — Rabba / Reish Lakish', [FX.NONE])
    if ask == 'slander_sealed':
        ink('14:22', '"tried Me these ten times" — the sentence at the spies\' speech'); move('Arakhin 15a:6; Mishnah Arakhin 3:5', 'the sentence sealed by the malicious speech — speech severer than deeds')
        return out('the sentence sealed by the evil report — speech severer than deeds (Mishnah Arakhin 3:5)', ['evil_report_spread'])
    if ask == 'consumes_inhabitants':
        ink('13:32', '"a land that eats its inhabitants"'); move('Sotah 35a:8 (Rava)', 'the deaths for their own good — the mourning hid them; Job\'s eulogy (some say)')
        return out("the deaths for their good — the mourning that hid them (Rava); Job's eulogy (some say)", [FX.NONE])
    if ask == 'grasshoppers':
        ink('13:33', '"we were in our own eyes as grasshoppers, and so we were in their eyes"'); move('Sotah 35a:9 (Rav Mesharshiyya)', 'liars — in their eyes unknowable')
        return out('liars — "in their eyes" unknowable (Rav Mesharshiyya)', [FX.NONE])
    if ask == 'job':
        ink('13:20', '"whether there are trees (eitz) in it"'); move('Bava Batra 15a:14 (Rava)', 'Job (Utz) in the spies\' days')
        return out("Job in the spies' days — trees / Utz (Rava, Bava Batra 15a)", [FX.NONE])
    if ask == 'joshua_caleb_equal':
        ink('13:6, 13:8', 'Caleb named first (Judah), Joshua after (Ephraim) — the list\'s order'); move('Tosefta Keritot 4:7 (R. Shimon)', 'Joshua preceded Caleb everywhere but here — equal')
        return out('equal — Caleb first at 13:6, Joshua at 13:8 (Tosefta Keritot 4:7)', [FX.NONE])
    if ask == 'named_after_deeds':
        ink('13:13-14', 'Sethur son of Michael; Nahbi son of Vophsi'); move('Sotah 34b:5-6 (R. Yitzchak; R. Yochanan)', 'named after their deeds — hid, weakened; concealed, stomped')
        return out('Sethur son of Michael — hid the acts, weakened Him; Nahbi son of Vophsi (R. Yitzchak; R. Yochanan)', [FX.NONE])
    if ask == 'giants':
        ink('13:22', 'Ahiman, Sheshai and Talmai, the children of Anak — Sheshai a name, not the ordinal (the parser\'s %s)' % SHESHAI); move('Sotah 34b:9-10; Yoma 10a:6', 'the skilled, the pits, the furrows; the sun a necklace')
        return out('Ahiman the skilled, Sheshai the pits, Talmai the furrows; the sun a necklace (Sotah 34b:9-10; Yoma 10a)', [FX.NONE])
    raise KeyError(ask)


# ===== F2: THE DECREE (Num 14:1-45) =========================================================================
def decree(case, data):
    del P[:]
    ask = case['ask']
    if ask == 'that_night':
        ink('14:1', '"and the people wept that night"'); dat('the row return_day = %s' % (data['return_day']['value'],)); move('Taanit 29a:7; Sotah 35a:11; Sanhedrin 104b:4', 'the night of the Ninth of Av — a weeping for generations; Mishnah Ta\'anit 4:6 the decree\'s day')
        return out("the night of the Ninth of Av — a weeping for generations (Taanit 29a:7; Sotah 35a:11; Sanhedrin 104b:4); Mishnah Ta'anit 4:6", ['wept'])
    if ask == 'ten_trials':
        ink('14:22', '"tried Me these ten times" — the parser\'s %s' % TEN); dat('the row the_ten_trials = %s' % data['the_ten_trials']['value']); move('Arakhin 15a-b; Pirkei Avot 5:4', 'the ten trials — the spies the tenth')
        return out("10 — 'these ten times' (14:22; Pirkei Avot 5:4); the ledger's count graded at CF6", [FX.NONE])
    if ask == 'now_ten':
        ink('14:22', '"NOW ten times" — the extra word'); move('Arakhin 15a:10 (Reish Lakish)', 'sealed for THIS sin')
        return out('sealed for THIS sin — "now" (Reish Lakish, Arakhin 15a:10)', [FX.NONE])
    if ask == 'congregation':
        ink('14:27', '"this evil congregation" — twelve spies less Joshua and Caleb = %d' % (len(TRIBE_LINES) - 2)); dat('the row congregation = %s' % data['congregation']['value']); move('Mishnah Sanhedrin 1:6; Berakhot 21b:5; Megillah 23b:8; Sanhedrin 74b:3', 'a congregation is ten')
        return out('10 — the twelve less Joshua and Caleb (Mishnah Sanhedrin 1:6; Berakhot 21b; Megillah 23b; Sanhedrin 74b)', [FX.NONE])
    if ask == 'set':
        ink('14:29', '"all your counted by all your number, from twenty years old and upward" — the census formula (the parser\'s %s)' % TWENTY); move('Bava Batra 121b:8 (Rav Hamnuna)', 'Levi outside — counted from thirty'); dat('Bamidbar\'s total CALLED: census(total) -> %s' % BM.census({'ask': 'total'}, BM.DATA)[0])
        return out('%d — the census set by CALL: from twenty and upward, all your counted; Levi outside (Bava Batra 121b:8); not over sixty (121b:11)' % BM.TOTAL, ['sentence_pronounced'])
    if ask == 'set_edges':
        ink('14:29', '"and upward" — the valuations\' "and upward" (Lev 27:7)'); move('Bava Batra 121b:11 (Rav Acha bar Yaakov)', 'the verbal analogy: over sixty outside as under twenty — Yair son of Manasseh; 121b:8 Rav Hamnuna: Levi from thirty')
        return out('under twenty and over sixty outside — "and upward" / "and upward" with the valuations (Rav Acha bar Yaakov); Levi from thirty (Rav Hamnuna)', [FX.NONE])
    if ask == 'exceptions':
        ink('14:24, 14:30', '"save Caleb son of Jephunneh and Joshua son of Nun"'); ink('14:31', '"your little ones... I will bring in"')
        return out('Caleb and Joshua (14:24, 14:30); the children brought in (14:31)', ['exempt'])
    if ask == 'day_for_year':
        ink('14:34', '"forty days, a day for a year, a day for a year... forty years" — the parser\'s %s; Ezek 4:6 verbatim' % DAY_YEAR)
        return out('[40, 40] — forty days, a day for a year, a day for a year (14:34; Ezek 4:6 verbatim)', [FX.NONE])
    if ask == 'count_from':
        ink('14:33-34', 'forty years — %s; Deut 2:14 thirty-eight from Kadesh-barnea to Zered' % FORTY_YEARS); dat('the row count_from = %s' % data['count_from']['value']); ink('the Calendar', 'the era\'s year at the decree = %d; 40 − 38 = %d' % (_EX.year(RETURN_DAY), 40 - 38))
        return out("40 - 38 = 2 — the era's year at the decree: the forty from the exodus (Deut 2:14's thirty-eight from Kadesh)", [FX.NONE])
    if ask == 'due':
        ink('the Calendar', 'the decree\'s day (2, 5, 9) + 38 years = %s' % (_EX.date(DUE_38),)); dat('the row deaths_ceased = %s' % (data['deaths_ceased']['value'],))
        return out('(40, 5, 9) — the ninth of Av of the fortieth year, by the Calendar; PENDING on the tape (CF3)', ['carcasses_fall_in_the_wilderness'])
    if ask == 'deaths_ceased':
        dat('the row deaths_ceased = %s' % (data['deaths_ceased']['value'],)); move('Bava Batra 121a:9 (Rav Nachman); Taanit 30b:12 (R. Yochanan)', 'the fifteenth of Av — the dying ceased; Deut 2:16-17 the speech resumed')
        return out('the fifteenth of Av of the fortieth year — the dying ceased; the speech resumed (Bava Batra 121a:9; Taanit 30b:12; Deut 2:16-17)', [FX.NONE])
    if ask == 'wilderness_share':
        ink('14:35', '"in this wilderness they shall be consumed, and there they shall die" — the four seats of "this wilderness": %s' % THIS_WILDERNESS); dat('the row wilderness_share = %s' % data['wilderness_share']['value'])
        return out('no share (R. Akiva — "there they shall die"); a share (R. Eliezer — Ps 50:5)', [FX.NONE])
    if ask == 'spies_share':
        ink('14:37', '"died... by plague"'); dat('the row spies_share = %s' % data['spies_share']['value'])
        return out('no share — "died... by plague" (Mishnah Sanhedrin 10:3)', [FX.NONE])
    if ask == 'spies_death_mode':
        ink('14:37', '"died by the plague before the LORD" — an unusual death'); dat('the row spies_death_mode = %s' % data['spies_death_mode']['value'])
        return out('the tongue to the navel with worms (R. Sheila); diphtheria (Rav Nachman bar Yitzchak)', ['put_to_death'])
    if ask == 'spies_portions':
        ink('14:38', '"Joshua and Caleb LIVED of those men" — 26:65 already says they survived'); move('Bava Batra 118b:3 (Ulla)', 'lived IN the ten\'s portions of the land')
        return out("Joshua and Caleb lived in the ten's portions — 'lived' (Ulla, Bava Batra 118b)", [FX.NONE])
    if ask == 'pardon':
        ink('14:20', '"I have pardoned according to your word" — once in the Bible (%d)' % ONCE['סלחתי']); move('Berakhot 32a:29 (R. Yochanan; the school of R. Yishmael)', 'God conceded to Moses; according to your word — so it will be')
        return out('"I have pardoned according to your word" — God conceded (R. Yochanan); so it will be (the school of R. Yishmael)', ['pardoned'])
    if ask == 'plea':
        ink('14:17-18', '"as You have spoken, saying: the LORD, long of anger" — the attributes quoted back'); move('Sanhedrin 111b:1', 'long of anger even for the wicked — as You said')
        return out('the attributes quoted back — "as You have spoken": long of anger even for the wicked (Sanhedrin 111b:1)', [FX.NONE])
    if ask == 'attributes_deleted':
        ink('14:18 against Exod 34:6-7', 'a subsequence — %d tokens of %d kept, %d distinct words dropped (%s), none added; Onkelos restores "and sins" from its own Exod 34:7' % (len(N18), len(E34), len(DROPPED), ' '.join(DROPPED)))
        return out('a subsequence of Exod 34:6-7 — eleven words dropped, none added; Onkelos restores "and sins"', [FX.NONE])
    if ask == 'offer_second_seat':
        ink('14:12', '"I will make of you a greater nation" — Exod 32:10 the first seat, Deut 9:14 the retelling (M-23)')
        return out("the offer's second seat — Exod 32:10 / Num 14:12 / Deut 9:14 (M-23)", [FX.NONE])
    if ask == 'egypt_will_hear':
        ink('14:13', '"then Egypt will hear" — Exod 32:12 "why should Egypt say" at the calf')
        return out("Moses' Egypt argument at both intercessions (Exod 32:12; Num 14:13)", [FX.NONE])
    if ask == 'ability':
        ink('14:16', '"from lack of the ABILITY of the LORD" — the feminine noun'); move('Berakhot 32a:27', 'yekholet, not yakhol — the nations\' saying')
        return out('the ability — yekholet, the feminine noun (Berakhot 32a:27)', [FX.NONE])
    if ask == 'as_i_live':
        ink('14:21', '"as I live, and all the earth shall be filled with the glory of the LORD"'); move('Berakhot 32a:31 (Rava / Rav Yitzchak)', 'you have given Me life with your words')
        return out('"you have given Me life with your words" (Rava / Rav Yitzchak)', [FX.NONE])
    if ask == 'upon_children':
        ink('14:18', '"visiting the iniquity of the fathers upon the children"'); move('Berakhot 7a; Sanhedrin 27b', 'when they hold their fathers\' deeds')
        return out("when they hold their fathers' deeds (Berakhot 7a; Sanhedrin 27b)", [FX.NONE])
    if ask == 'caleb_entitlement':
        ink('14:24', '"him I will bring into the land where he went, and his seed shall possess it"'); ink('Josh 14:6-14', 'forty years, forty-five, eighty-five; "Moses swore that day" — the oath Numbers never wrote; Hebron given')
        return out('holding_owed — Hebron; PAID at Josh 14:13-14 (forty-five years; eighty-five; Moses swore that day)', ['holding_owed'])
    if ask == 'turn_back':
        ink('14:25', '"tomorrow turn and journey into the wilderness by the way of the Red Sea" — the run Num 21:4 by the same phrase; Deut 2:1')
        return out('tomorrow turn — by the way of the Red Sea: OPEN, its run Num 21:4 / Deut 2:1', ['commanded'])
    if ask == 'presumption':
        ink('14:44', '"they presumed to go up... the ark and Moses did not depart"'); move('Shabbat 97a:1 (R. Yehuda ben Beteira)', 'Zelophehad among them — the daughters\' father')
        return out('presumed — the ark and Moses stayed; Zelophehad among them (R. Yehuda ben Beteira, Shabbat 97a)', ['presumed_to_go_up'])
    if ask == 'hormah':
        ink('14:45', '"beat them down to Hormah" — the name at 21:3 ("and he called the name of the place Hormah"), six chapters later; Judg 1:17 the second naming')
        return out('Hormah — named at 21:3, used at 14:45: THE PROLEPTIC NAME (the registry row carries both); Judg 1:17', ['defeated'])
    if ask == 'fell_and_rent':
        ink('14:5-6', '"Moses and Aaron fell on their faces"; "Joshua and Caleb... rent their garments"'); move('Taanit 14b:13 (R. Elazar)', 'the worthy fall on their faces; their students rend')
        return out('Moses and Aaron fell on their faces; Joshua and Caleb rent garments (Taanit 14b)', [FX.NONE])
    if ask == 'stones_upward':
        ink('14:10', '"to stone them with stones; and the glory of the LORD appeared"'); move('Sotah 35a:12 (R. Chiyya bar Abba)', 'the stones thrown upward, as at God')
        return out('stones thrown upward, as at God (R. Chiyya bar Abba)', [FX.NONE])
    if ask == 'ninth_of_av_reading':
        ink('14:11 / 14:27', '"how long will this people provoke Me" / "this evil congregation"'); move('Megillah 31b:2', 'the Ninth of Av\'s Torah reading — R. Natan bar Yosef; Abaye: today Deut 4:25')
        return out('the Ninth of Av\'s Torah reading — "how long will this people provoke Me" (R. Natan bar Yosef); today Deut 4:25 (Abaye)', [FX.NONE])
    if ask == 'joshua_childless':
        ink('14:6', '"Joshua son of Nun" — 1 Chr 7:27 "Nun his son, Joshua his son", no children named'); move('Pesachim 119b:6', 'no son')
        return out('no son — "Joshua son of Nun" and 1 Chr 7:27 (Pesachim 119b)', [FX.NONE])
    raise KeyError(ask)

# ===== F3: THE LIBATIONS (Num 15:1-13) ======================================================================
NO_LIBATIONS = ('firstborn', 'tithe', 'pesach', 'chatat', 'asham', 'festival_goat', 'bird_olah', 'meal_offering')
def libations(case, data):
    del P[:]
    ask = case['ask']
    if ask == 'table':
        ink('15:4-10', 'the table computed from the ink: %s (flour in tenths, oil and wine in hin)' % {k: tuple(str(x) for x in v) for k, v in TABLE.items()})
        return out('lamb 1/10 + 1/4 + 1/4; ram 2/10 + 1/3 + 1/3; bull 3/10 + 1/2 + 1/2 — computed from 15:4-10', [FX.NONE])
    if ask == 'table_seats':
        ink('Exod 29:40; Lev 23:13; Num 28:5-7, 28:14', 'the same rows at every seat: the tamid %s, the daily %s, the new moon %s; the omer\'s lamb %s — its flour doubled' % (TAMID_ROW, DAILY_ROW, MONTH_ROW, OMER_ROW)); move('Mishnah Menachot 9:4', 'the omer\'s lamb: doubled flour, oil and wine not doubled')
        return out("the lamb's quarter-hin at Exod 29:40, Lev 23:13, Num 28:5-7; 28:14 the three rows; the omer's flour doubled (two tenths — Mishnah Menachot 9:4)", [FX.NONE])
    if ask == 'logs':
        dat('the row hin_in_logs = %s' % data['hin_in_logs']['value']); ink('15:4-10', 'the fractions in logs: %s' % LOGS)
        return out('lamb 3, ram 4, bull 6 — the hin twelve logs (Mishnah Menachot 9:2)', [FX.NONE])
    if ask == 'mixing':
        ink('15:4-10', 'oil logs per tenth of flour: %s' % {k: str(v) for k, v in RATIO.items()}); move('Mishnah Menachot 9:4', 'bulls\' with rams\' — the same ratio; lambs\' with lambs\'; not lambs\' with bulls\' or rams\'')
        a, b = case.get('pair', ('bull', 'ram'))
        return out('may mix — the same ratio' if RATIO[a] == RATIO[b] else 'may not mix — the ratios differ', ['accepted'] if RATIO[a] == RATIO[b] else ['disqualified'])
    if ask == 'sukkot_sabbath':
        ink('15:4-10 with 29:12-16, 28:3, 28:9', 'thirteen bulls at %d, two rams at %d, fourteen lambs at %d, the two daily and the two Sabbath lambs = %d' % (TABLE['bull'][0], TABLE['ram'][0], TABLE['lamb'][0], SUKKOT_SABBATH)); move('Mishnah Menachot 12:4', 'sixty-one tenths — the community\'s most in a day')
        return out('61 tenths — 13 bulls x 3 + 2 rams x 2 + 14 lambs + 2 daily + 2 Sabbath lambs (Mishnah Menachot 12:4)', [FX.NONE])
    if ask == 'which_offerings':
        ink('15:3', '"a burnt offering or a sacrifice, for a vow or a gift or at your festivals"'); ink('15:8', '"a young bull for a burnt offering" — the festival goats excluded'); ink('15:5', '"with the burnt offering or for the sacrifice, for the one lamb" — the leper\'s three'); dat('the row which_take_libations')
        return out("all but the firstborn, the tithe, the Passover, the sin offering, the guilt offering; the leper's chatat and asham do (Mishnah Menachot 9:6; 15:5)", [FX.NONE])
    if ask == 'takes':
        kind = case['offering']
        if case.get('where') == 'wilderness':
            ink('15:2', '"when you come into the land of your dwellings" — the cell\'s own gate'); dat('the row libations_from = %s' % data['libations_from']['value'])
            return out('not yet — before the entry (15:2)', ['exempt'])
        if kind in ('leper_chatat', 'leper_asham'):
            ink('15:5', '"or for the sacrifice" — the leper\'s sin offering and guilt offering included (Menachot 91a:27)')
            return out('libations — the leper\'s (15:5)', ['libation_owed'])
        if kind in NO_LIBATIONS:
            ink('15:3, 15:8', 'a burnt offering or a sacrifice of a vow or a gift — not the %s' % kind); move('Mishnah Menachot 9:6; Menachot 90b:6-10', 'the list')
            return out('no libations', ['exempt'])
        ink('15:3-10', 'the table applies — %s' % kind)
        return out('libations', ['libation_owed'])
    if ask == 'donated':
        dat('the row libation_floors = %s' % data['libation_floors']['value']); ink('15:13', '"all the home-born shall do these" — libations alone; 28:14 "shall be" adds'); move('Mishnah Menachot 12:4, 13:5; Menachot 104a:10-11', 'three, four, six logs and beyond; never one, two or five')
        n = case.get('logs')
        if n is None:
            return out("not less than three logs — the lamb's; 3, 4, 6 and beyond, never 1, 2, 5 (Mishnah Menachot 12:4, 13:5; Menachot 104a)", [FX.NONE])
        ok = n >= 3 and n != 5
        return out('a valid libation of %d logs' % n if ok else 'no such libation — %d logs' % n, ['accepted'] if ok else ['disqualified'])
    if ask == 'donated_oil':
        dat('the row oil_donation = %s' % data['oil_donation']['value'])
        return out('wine yes; oil — R. Akiva no, R. Tarfon yes; Rabbi three logs (Mishnah Menachot 12:5; 107a:17)', [FX.NONE])
    if ask == 'donated_wine_disposal':
        ink('15:10', '"half a hin of wine, an offering made by fire"'); move('Zevachim 91b:12 (Shmuel)', 'sprinkled on the altar\'s fire; partial extinguishing is no extinguishing')
        return out("on the altar's fire — an offering made by fire (Shmuel, Zevachim 91b)", ['accepted'])
    if ask == 'gentile':
        ink('15:13', '"the home-born" — a Jew brings libations alone'); ink('15:11', '"so shall it be done for the one bull" — every olah requires them'); dat('the row gentile_libations = %s' % data['gentile_libations']['value']); move('Menachot 73b:14; Zevachim 45a:14; Temurah 3a:10; Mishnah Shekalim 7:6', 'no independent libations for a gentile; his olah\'s required, the public pays')
        return out("no independent libations; his olah's required (15:11, 15:13); the public pays if he sent none (Mishnah Shekalim 7:6)", ['libation_owed'])
    if ask == 'found_animal':
        move('Mishnah Shekalim 7:5', 'the found animal\'s libations from public funds — the court\'s ordinance')
        return out('from public funds (Mishnah Shekalim 7:5)', ['libation_owed'])
    if ask == 'heir':
        move('Mishnah Menachot 9:7', 'the heir places hands and brings the libations')
        return out('the heir brings the libations (Mishnah Menachot 9:7)', ['libation_owed'])
    if ask == 'so':
        ink('15:11', '"SO shall it be done" — the exact measure'); move('Menachot 27a:7-8', 'the wine\'s minority prevents the majority; the log of oil likewise')
        return out('the exact measure indispensable — "so" (Menachot 27a)', ['disqualified'])
    if ask == 'calf':
        ink('15:11', '"for the ONE bull" — the definite one (the parser\'s %s)' % ONE_OX_RAM); move('Menachot 91b:20', 'one law for all bulls, the calf included')
        return out('as a bull — "for the one bull" (Menachot 91b:20)', ['libation_owed'])
    if ask == 'palges':
        ink('15:6', '"or for a ram"'); dat('the row lamb_and_ram_ages = %s' % data['lamb_and_ram_ages']['value']); move('Chullin 23a:6 (R. Yochanan); Mishnah Parah 1:3', 'the thirteen-month animal — a ram\'s libations, not counted')
        return out("the ram's libations, not counted — the thirteen-month animal (Mishnah Parah 1:3; Chullin 23a)", ['libation_owed'])
    if ask == 'ages':
        dat('the row lamb_and_ram_ages = %s' % data['lamb_and_ram_ages']['value'])
        return out('lambs to a year, rams from thirteen months and a day (Mishnah Parah 1:3)', [FX.NONE])
    if ask == 'the_one':
        ink('15:5, 15:11', '"for the one lamb", "for the one bull", "for the one ram" — THE DEFINITE ONE read by the parser (%s, %s)' % (LAMB_B, ONE_OX_RAM)); move('Menachot 91b:9 (R. Natan); 91b:20', 'the woman\'s olah; the tithe\'s eleventh; the calf')
        return out("the definite one read — the woman's olah, the tithe's eleventh (Menachot 91b:9); the calf (91b:20)", [FX.NONE])
    if ask == 'aarons_ram':
        ink('15:6-7', '"or for a ram" beside 28:12'); move('Menachot 91b:12 (Rav Sheshet)', 'the ram of Aaron included')
        return out('libations — "or for a ram" (Rav Sheshet)', ['libation_owed'])
    if ask == 'each_animal':
        ink('15:11-12', '"so shall be done for each... according to their number" — separate libations per animal'); move('Menachot 91a:18-24', 'even consecrated together')
        return out('separate libations per animal, even consecrated together (15:11-12)', ['libation_owed'])
    if ask == 'tenths_integral':
        ink('15:4-9', 'the tenth the unit noun — one, two, three tenths (the parser\'s %s, %s, %s)' % (LAMB_A[0], RAM_A[0], BULL_A[0])); move('Mishnah Menachot 12:3', 'no partial tenths')
        return out('no partial tenths — half a tenth brings a whole; a tenth and a half brings two (Mishnah Menachot 12:3)', [FX.NONE])
    if ask == 'with_price':
        move('Mishnah Menachot 13:8', 'the libations inside the vow\'s price')
        return out("the libations inside the vow's price — a bull 100 dinars, a calf 5 sela, a ram 2, a lamb 1 (Mishnah Menachot 13:8)", [FX.NONE])
    if ask == 'from_when':
        ink('15:2', '"when you come into the land of your dwellings"'); dat('the row libations_from = %s' % data['libations_from']['value'])
        return out('the entry (Zevachim 111a); after inheritance and settlement (R. Yishmael, Kiddushin 37b) — none in the wilderness on both', [FX.NONE])
    if ask == 'altar_eras':
        dat('the row altar_eras = %s' % data['altar_eras']['value'])
        return out('the wilderness / Gilgal / Shiloh / Nov and Gibeon / Jerusalem — forbidden, permitted, forbidden, permitted, forbidden forever (Mishnah Zevachim 14:4-8)', [FX.NONE])
    if ask == 'private_altar':
        move('Mishnah Zevachim 14:10; Zevachim 111a-b', 'the high place\'s omissions; the intents equal')
        return out('no laying of hands, no north, no blood around, no waving; the intents equal (Mishnah Zevachim 14:10)', [FX.NONE])
    if ask == 'ezekiel':
        ink('15:6, 15:9', 'the ram two tenths, the bull three — against Ezek 46:7\'s "an ephah for the bull and an ephah for the ram"'); move('Menachot 45a:21 (R. Shimon)', 'the ink\'s rows hold; Ezekiel\'s reconciled')
        return out("the bull's three tenths and the ram's two against Ezekiel 46:7's ephah each (R. Shimon, Menachot 45a)", [FX.NONE])
    if ask == 'or_against_and':
        ink('15:3', '"from the herd OR from the flock" — Lev 1:2 "from the herd AND from the flock"')
        return out('"from the herd OR from the flock" against Lev 1:2\'s AND (computed)', [FX.NONE])
    if ask == 'oil_only':
        v = MN.adjuncts('libation')['v']; ink('15:4', '"a meal offering... mixed with oil" — no frankincense named'); dat('the minchah engine CALLED: adjuncts(libation) -> %s' % v)
        return out('%s — the libation meal offering: oil, no frankincense (the minchah engine CALLED)' % v, [FX.NONE])
    if ask == 'olah_table':
        t = OF.dispatch('olah:herd'); ink('15:3, 15:8, 15:24', '"a burnt offering" — Lev 1\'s own table by name'); dat('the offerings engine CALLED: dispatch(olah) -> %s' % {k: c['v'] for k, c in t.items()})
        return out('%s; %s; %s; %s (the offerings engine CALLED)' % (t['place']['v'], t['applications']['v'], t['procedure']['v'], t['disposition']['v']), [FX.NONE])
    if ask == 'owner_piggul':
        ink('15:4', '"he who sacrifices shall sacrifice his offering" — the owner named a sacrificer'); dat('the row owner_piggul = %s' % data['owner_piggul']['value'])
        return out('the owner can render piggul — "he who sacrifices" (R. Elazar son of R. Yosei); the performer only (the mishna)', [FX.NONE])
    raise KeyError(ask)


# ===== F4: THE STRANGER (Num 15:14-16) ======================================================================
def stranger(case, data):
    del P[:]
    ask = case['ask']
    if ask == 'convert_offering':
        ink('15:14', '"as you do, so shall he do" — as at the covenant\'s entry (Exod 24:5)'); ink('15:14', '"an offering made by fire, a pleasing aroma" — wholly for the LORD: a bird olah'); dat('the row convert_offering = %s' % data['convert_offering']['value']); move('Keritot 8b:18-9a:3; Mishnah Kinnim 1:1', 'a beast olah, or a bird pair both olot')
        return out("an olah (a beast) or a bird pair, both olot — as at the covenant's entry (Keritot 8b-9a; Mishnah Kinnim 1:1)", ['accepted'])
    if ask == 'entry':
        ink('15:15', '"as you are, so shall the stranger be"'); move('Keritot 9a:4 (Rabbi)', 'as your fathers — circumcision, immersion, the sprinkling of blood')
        return out('circumcision, immersion, the sprinkling of blood — as your fathers (Rabbi, Keritot 9a:4)', [FX.NONE])
    if ask == 'no_temple':
        ink('15:14', '"throughout your generations"'); move('Keritot 9a:10 (Rav Acha bar Yaakov)', 'converts accepted without a Temple — the offering waits')
        return out('accepted — "throughout your generations" (Rav Acha bar Yaakov)', ['accepted'])
    if ask == 'court':
        ink('15:16', '"one JUDGMENT for you and for the stranger"'); move('Yevamot 46b:16 (R. Yochanan)', 'a court of three')
        return out('3 — "one judgment" (R. Yochanan, Yevamot 46b)', [FX.NONE])
    if ask == 'one_law':
        f = [w for v in (15, 16, 29) for w in verse_text(15, v).split() if w in ('אחת', 'אחד')]
        ink('15:15-16, 15:29', '"one statute", "one Torah", "one judgment", "one Torah" — the formulas computed: %d' % len(f))
        return out('one statute, one Torah, one judgment — the formulas computed (15:15-16, 15:29)', [FX.NONE])
    if ask == 'congregation':
        dat('the row convert_congregation = %s' % data['convert_congregation']['value'])
        return out('converts are congregation (R. Yehuda); not (R. Yosei) — Kiddushin 73a', [FX.NONE])
    if ask == 'meal_offering':
        ink('15:14', '"as you do" — offerings whose blood is sprinkled'); move('Keritot 9a:2', 'a meal offering does not discharge the convert')
        return out('a meal offering does not discharge — the blood sprinkled (Keritot 9a:2)', ['disqualified'])
    if ask == 'quarter_dinar':
        dat('the row convert_offering — the quarter-dinar arm'); move('Keritot 9a:10', 'set aside for the pair; R. Shimon annulled it')
        return out('a quarter-dinar set aside for the pair — R. Shimon annulled it (Keritot 9a)', [FX.NONE])
    raise KeyError(ask)


# ===== F5: THE CHALLAH (Num 15:17-21) =======================================================================
FIVE_SPECIES = ('wheat', 'barley', 'spelt', 'oats', 'rye')
def challah(case, data):
    del P[:]
    ask = case['ask']
    if ask == 'species':
        ink('15:19', '"the bread of the land"'); move('Menachot 70b:2 (Reish Lakish); Mishnah Challah 1:1', '"bread" / "bread" with matza — the five grains')
        grain = case.get('grain')
        if grain is None:
            return out('5 — wheat, barley, spelt, oats, rye (Mishnah Challah 1:1; "bread"/"bread", Menachot 70b)', [FX.NONE])
        return out('liable — one of the five' if grain in FIVE_SPECIES else 'exempt — not of the five (rice, millet, pulse)', ['accepted'] if grain in FIVE_SPECIES else ['exempt'])
    if ask == 'entry_gate':
        ink('15:18', '"UPON YOUR COMING to the land" — varied from "when you come" (M-23 exemplar 12)'); move('Sifrei Bamidbar 110:1 (R. Yishmael)', 'liable from the entry itself, unlike the land-laws that wait for settlement')
        return out('from the entry itself — "upon your coming" varied (Sifrei 110:1; R. Yishmael)', [FX.NONE])
    if ask == 'all_of_you':
        ink('15:18', '"upon your coming" — all of you'); dat('the row challah_today = %s' % data['challah_today']['value']); move('Ketubot 25a:11; Niddah 47a:7', 'not two or three spies; Ezra\'s return partial')
        return out('all of you, not two or three spies — challah today rabbinic (Ketubot 25a; Niddah 47a)', [FX.NONE])
    if ask == 'minimum':
        ink('15:20', '"your dough" — the wilderness measure (Menachot 67a:6): the omer, a tenth of the ephah (Exod 16:36 — the parser\'s fraction)'); dat('the row challah_minimum = %s' % data['challah_minimum']['value'])
        return out('five quarters of flour — the wilderness omer, a tenth of the ephah (Mishnah Challah 2:6; Shabbat 15a; Tosefta Eduyot 1:1; Exod 16:36)', [FX.NONE])
    if ask == 'measure':
        who = case.get('who', 'householder'); impure = case.get('impure')
        dat('the row challah_measure = %s' % data['challah_measure']['value']); ink('15:20', 'no measure in the ink — the data channel\'s')
        m = Fraction(1, 24) if (impure == 'intentional' or (who == 'householder' and impure is None)) else Fraction(1, 48)
        return out(str(m), ['due_to_priest'])
    if ask == 'as_terumah':
        ink('15:20', '"as the terumah of the threshing floor so shall you lift it" — Numbers 18\'s terumah'); dat('the row terumah_measure = %s (the placeholder copy; the row\'s home is cold_run_korach.py since 5b)' % data['terumah_measure']['value']); move('Mishnah Challah 1:9', 'the terumah\'s laws on the challah')
        _v, _e, _pr = KR.the_tithe({'ask': 'terumah_measure'}, KR.DATA)                                                     # THE CALL (THE NUMBERS WALK 5b, 2026-09-10): the pointer PAID
        P.append(('MOVE', 'CALLED cold_run_korach.the_tithe(terumah_measure) -> %s [IMPORT, live call] — 18:27 "reckoned as the grain of the threshing floor" pays 15:20\'s pointer' % _v))
        return out("the terumah's laws — death and a fifth, the priest's, 101 (Mishnah Challah 1:9); its measure 1/40, 1/50, 1/60 (Terumot 4:3) — PAID: cold_run_korach.the_tithe(terumah_measure) CALLED", ['due_to_priest'])
    if ask == 'owner':
        ink('15:20-21', '"your dough" twice'); move('Menachot 67a:6; Pesachim 38a:3', 'yours — not a gentile\'s, not consecrated')
        owner = case.get('owner', 'israelite')
        return out('yours — not a gentile\'s, not consecrated (Menachot 67a; Pesachim 38a)' if owner == 'israelite' else 'exempt — not your dough', ['accepted'] if owner == 'israelite' else ['exempt'])
    if ask == 'partners':
        ink('15:20', '"your dough" — the plural'); move('Chullin 135b:9 (R. Ilai concedes)', 'joint owners obligated')
        return out('liable — "your dough" plural (Chullin 135b)', ['accepted'])
    if ask == 'from_flour':
        ink('15:20', '"of your DOUGH"'); move('Kiddushin 46b:4; Mishnah Challah 2:5', 'from flour not challah; stolen in the priest\'s hand')
        return out("not challah — stolen in the priest's hand (Mishnah Challah 2:5)", ['disqualified'])
    if ask == 'outside_produce':
        dat('the row outside_produce = %s' % data['outside_produce']['value'])
        d = case.get('direction', 'in')
        return out('liable — brought into the land (Mishnah Challah 2:1)' if d == 'in' else 'R. Eliezer liable, R. Akiva exempt — taken out (Mishnah Challah 2:1)', ['accepted'] if d == 'in' else [FX.NONE])
    if ask == 'territories':
        ink('15:21', '"throughout your generations"'); dat('the row territories = %s' % data['territories']['value'])
        return out('three — to Chezib one; to the river two; beyond two, the measures reversed (Mishnah Challah 4:8)', [FX.NONE])
    if ask == 'sabbatical':
        ink('15:21', '"throughout your generations"'); move('Bekhorot 12b:11', 'sabbatical-year dough liable')
        return out('liable — throughout your generations (Bekhorot 12b)', ['accepted'])
    if ask == 'when_liable':
        move('Mishnah Challah 3:1-3', 'the rolling of wheat, the solid mass of barley; death by Heaven after')
        return out('the rolling (wheat) / the solid mass (barley); death by Heaven after (Mishnah Challah 3:1)', [FX.NONE])
    if ask == 'mixture':
        move('Mishnah Challah 3:7, 3:10; Zevachim 78a:7', 'wheat with rice — the taste of grain')
        return out('the taste of grain (Mishnah Challah 3:7, 3:10; Zevachim 78a)', [FX.NONE])
    if ask == 'joining':
        move('Mishnah Challah 2:4, 4:1-3', 'stuck together, one owner, one species; the basket (R. Eliezer)')
        return out('stuck together, one owner, one species; the basket (R. Eliezer) (Mishnah Challah 2:4, 4:1-3)', [FX.NONE])
    if ask == 'joining_species':
        move('Mishnah Challah 4:2', 'wheat with spelt only; barley with all but wheat')
        return out('wheat with spelt only; barley with all but wheat (Mishnah Challah 4:2)', [FX.NONE])
    if ask == 'gentile_dough':
        move('Mishnah Challah 3:5', 'a gentile\'s flour exempt; a gift before the rolling liable')
        return out("exempt — a gentile's; a gift before the rolling liable (Mishnah Challah 3:5)", ['exempt'])
    if ask == 'convert_dough':
        ink('15:14-16', 'one law for the stranger — at the dough'); move('Mishnah Challah 3:6', 'before conversion exempt, after liable, in doubt liable without the fifth')
        return out('before conversion exempt, after liable, in doubt liable without the fifth (Mishnah Challah 3:6)', [FX.NONE])
    if ask == 'dogs_dough':
        move('Mishnah Challah 1:8', 'if shepherds eat it')
        return out('liable if shepherds eat it (Mishnah Challah 1:8)', [FX.NONE])
    if ask == 'market':
        move('Mishnah Challah 1:6', 'the thanksgiving loaves for the market liable, for oneself exempt')
        return out('for the market liable, for oneself exempt — the thanksgiving loaves (Mishnah Challah 1:6)', [FX.NONE])
    if ask == 'liable_not_tithed':
        move('Mishnah Challah 1:3', 'gleanings, the forgotten sheaf, peah, ownerless, the first tithe, redeemed second tithe, the omer\'s remainder, grain under a third')
        return out("liable to challah, exempt from tithes — gleanings, the forgotten sheaf, peah, ownerless produce, the first tithe, redeemed second tithe, the omer's remainder (Mishnah Challah 1:3)", [FX.NONE])
    if ask == 'exempt_list':
        move('Mishnah Challah 1:4', 'rice, millet, poppy, sesame, pulse, under five quarters, sponge-cakes, honey-cakes, dumplings, a pan-cake, medumma')
        return out('exempt from challah — rice, millet, poppy, sesame, pulse, under five quarters, sponge-cakes, honey-cakes, dumplings, a pan-cake, medumma (Mishnah Challah 1:4)', ['exempt'])
    if ask == 'demai':
        move('Mishnah Challah 4:6', 'challah for demai from clean dough not near')
        return out('permitted from clean dough not near (Mishnah Challah 4:6)', [FX.NONE])
    if ask == 'clean_for_unclean':
        move('Mishnah Challah 2:8', 'R. Eliezer permits with the egg-size bridge; the sages forbid')
        return out('R. Eliezer permits (the egg bridge); the sages forbid (Mishnah Challah 2:8)', [FX.NONE])
    if ask == 'dough_word':
        ink('15:20-21', 'the dough-word twice here — %d spellings in the Tanakh: %s' % (len(DOUGH), DOUGH))
        return out('the dough-word four spellings in the Tanakh — two here, Ezekiel 44:30, Nehemiah 10:38 (computed)', [FX.NONE])
    raise KeyError(ask)


# ===== F6: THE ERROR (Num 15:22-29) =========================================================================
def error(case, data):
    del P[:]
    ask = case['ask']
    if ask == 'which_sin':
        ink('15:22', '"all these commandments" — the one commandment equal to them all'); move('Horayot 8a:20 (Rava / R. Yehoshua ben Levi); Sifrei Bamidbar 111:1', 'idolatry')
        return out('idolatry — "all these commandments" the one equal to all (Horayot 8a:20; Sifrei 111:1)', [FX.NONE])
    if ask == 'delta':
        d = (('העדה' in verse_text(15, 24), 'הקהל' in verse_text(4, 13, 'Lev')), ('לעלה' in verse_text(15, 24), 'לחטאת' in verse_text(4, 14, 'Lev')), ('ושעיר' in verse_text(15, 24), 'שעיר' not in verse_text(4, 14, 'Lev')))
        ink('15:24 against Lev 4:13-14', 'the three deltas on the ink: the congregation for the assembly %s; a burnt offering for the sin offering %s; a goat added %s' % d); move('Sifrei Bamidbar 111:1', 'the passage is idolatry\'s by the deltas')
        return out('three deltas against Lev 4:13-14 — the congregation for the assembly, a burnt offering for the sin offering, a goat added (computed on the ink)', [FX.NONE])
    if ask == 'communal':
        c = CH.court({'sin': 'idolatry'}); ink('15:24', '"one young bull for a burnt offering... one he-goat for a sin offering"'); dat('the chatat engine CALLED: court(idolatry) -> %s' % c['v'])
        return out('%s — a bull for a burnt offering and a goat for a sin offering (the chatat engine CALLED)' % c['v'], ['accepted'])
    if ask in ('individual', 'anointed', 'leader'):
        tier = {'individual': 'commoner', 'anointed': 'anointed', 'leader': 'leader'}[ask]
        c = CH.rank(tier, sin='idolatry'); ink('15:27', '"one soul... a she-goat of its first year"'); move('Mishnah Horayot 2:6; Horayot 7b:21, 8a:12', 'the individual, the king and the anointed all "one soul"'); dat('the chatat engine CALLED: rank(%s, idolatry) -> %s' % (tier, c['v']))
        return out('%s — "one soul" (Mishnah Horayot 2:6; the chatat engine CALLED)' % c['v'], ['accepted'])
    if ask == 'tribe_table':
        dat('the row tribe_table = %s' % data['tribe_table']['value']); move('Mishnah Horayot 1:5', 'R. Meir / R. Yehuda / R. Shimon — carried in the chatat engine')
        return out('R. Meir a bull and a goat; R. Yehuda twelve; R. Shimon thirteen (Mishnah Horayot 1:5 — the chatat engine carries the arms)', [FX.NONE])
    if ask == 'order':
        ink('15:24', '"for a sin offering" WITHOUT the aleph (%d in the Bible); "according to the ordinance"' % ONCE['לחטת']); move('Horayot 13a:4 (Rava bar Mari; Rava); Zevachim 90b:6 (Ravina)', 'the bull precedes the goat')
        return out('the bull then the goat — "for a sin offering" without its aleph; "according to the ordinance" (Horayot 13a; Zevachim 90b)', ['accepted'])
    if ask == 'aleph':
        ink('15:24', 'the aleph-less sin offering — once in the Bible (computed %d)' % ONCE['לחטת'])
        return out('once in the Bible — the sin offering without the aleph at 15:24 (computed)', [FX.NONE])
    if ask == 'goat_portions':
        ink('15:25', '"their sin offering... for their error"'); move('Zevachim 41a:8', 'the idolatry goats\' portions burned like the communal bull\'s')
        return out('burned like the communal bull\'s — "their sin offering... for their error" (Zevachim 41a)', ['accepted'])
    if ask == 'majority_manner':
        ink('15:26', '"for all the people it was unwitting"'); move('Horayot 2a:19 (Rava)', 'all unwitting in one manner')
        return out('all unwitting in one manner (Rava, Horayot 2a)', [FX.NONE])
    if ask == 'eyes':
        ink('15:24', '"from the eyes of the congregation" — the court'); move('Horayot 5a-8a; Taanit 24a:12', 'the leaders the eyes; "from the eyes" / "from the eyes" with Lev 4:13')
        return out('"from the eyes of the congregation" = the court; the leaders the eyes (Horayot; Taanit 24a)', [FX.NONE])
    if ask == 'partial':
        c = CH.court({'sin': 'idolatry', 'ruling': 'whole'}); move('Mishnah Horayot 1:3, 2:2', 'the whole essence abolished exempt; a part nullified liable — "one who bows without sacrificing is exempt"'); dat('the chatat engine CALLED: court(whole) -> %s' % c['v'])
        return out('%s — the whole essence abolished; a part nullified liable (Mishnah Horayot 1:3)' % c['v'], ['exempt'])
    if ask == 'reliance':
        c = CH.reliance({'knew_error': case.get('knew_error', False)}); move('Mishnah Horayot 1:1', 'the individual who relied on the court exempt; one who knew liable'); dat('the chatat engine CALLED: reliance -> %s' % c['v'])
        return out(c['v'], ['atoned_forgiven'] if c['v'] == 'liable' else ['exempt'])
    if ask == 'priest_own':
        ink('15:28', '"the priest shall atone for the soul that sins unwittingly"'); move('Menachot 74a:7, 109a:20 (Rav Nachman)', 'a priest atones through his own rite')
        return out('a priest atones through his own rite (Menachot 74a; 109a)', ['accepted'])
    if ask == 'idolatry_principle':
        dat('the row idolatry_principle = %s' % data['idolatry_principle']['value']); move('Mishnah Shabbat 7:1; Shabbat 68b-69a', 'the forgetter of the principle — one offering; Munbaz: prior knowledge')
        return out("one sin offering for the forgetter of the principle (Mishnah Shabbat 7:1's analogue); prior knowledge for both (Munbaz)", [FX.NONE])
    if ask == 'semikhah':
        dat('the row idolatry_goat_semikhah = %s' % data['idolatry_goat_semikhah']['value'])
        return out("the court's bull and the scapegoat; R. Shimon adds the idolatry goat (Mishnah Menachot 9:7)", [FX.NONE])
    if ask == 'class':
        c = CH.domain({'intent': 'intentional'}); ink('15:29-30', '"one Torah for the one who acts unwittingly... with a high hand... cut off"'); move('Horayot 8a:14 (R. Yehoshua ben Levi); Keritot 3a:20; Shabbat 69a:1', 'the whole Torah juxtaposed to idolatry — intentional karet, unwitting sin offering'); dat('the chatat engine CALLED: domain(intentional) -> %s' % c['v'])
        return out('%s — the whole Torah juxtaposed to idolatry: intentional karet, unwitting sin offering (Horayot 8a:14; Keritot 3a:20)' % c['v'], [FX.NONE])
    if ask == 'stranger_included':
        ink('15:26', '"and to the stranger who sojourns among them"')
        return out('the stranger forgiven with them (15:26)', ['atoned_forgiven'])
    if ask == 'thrice_unwitting':
        ink('15:27-29', '"in error" %d times — thrice fenced' % IN_ERROR)
        return out('"in error" thrice at 15:27-29 (computed)', [FX.NONE])
    raise KeyError(ask)


# ===== F7: THE HIGH HAND (Num 15:30-31) =====================================================================
def high_hand(case, data):
    del P[:]
    ask = case['ask']
    if ask == 'class':
        c = CH.domain({'intent': case.get('intent', 'intentional')}); ink('15:30', '"with a high hand... cut off"'); move('Horayot 8a:14; Keritot 3a:20; Mishnah Keritot 1:2', 'the karet class'); dat('the chatat engine CALLED: domain -> %s' % c['v'])
        return out(c['v'], ['karet_cut_off'] if c['v'] == 'karet_no_offering' else ['atoned_forgiven'])
    if ask == 'blasphemer_offering':
        ink('15:29', '"one law for him who DOES unwittingly" — no act, no offering'); dat('the row blasphemer_offering = %s' % data['blasphemer_offering']['value'])
        return out('none — no act (the Rabbis, Mishnah Keritot 1:2); an offering (R. Akiva, Keritot 7b)', ['exempt'])
    if ask == 'blasphemer_identity':
        ink('15:30', '"blasphemes the LORD" — %d in the Bible' % ONCE['מגדף']); dat('the row blasphemer_identity = %s' % data['blasphemer_identity']['value'])
        return out('the curser of the Name (the Rabbis); the idolater (R. Elazar ben Azarya)', [FX.NONE])
    if ask == 'blasphemes_once':
        ink('15:30', 'the participle once in the Bible (computed %d)' % ONCE['מגדף'])
        return out('once in the Bible — blasphemes (computed)', [FX.NONE])
    if ask == 'despiser':
        ink('15:31', '"despised the word of the LORD"'); dat('the row despiser = %s' % data['despiser']['value']); move('Sanhedrin 99a:17; 99b:4', 'not from Heaven; the Epicurean; Manasseh')
        return out('who says the Torah is not from Heaven; the Epicurean (Sanhedrin 99a); Manasseh the exemplar (99b)', [FX.NONE])
    if ask == 'karet_reading':
        ink('15:31', '"cut off, shall be cut off" — the doubled infinitive'); dat('the row karet_reading = %s' % data['karet_reading']['value']); move('Sanhedrin 64b:21-22; 90b:18', 'R. Akiva two worlds; R. Yishmael the language of men — THE FORK (MIDDOT.md)')
        return out('R. Akiva: this world and the next; R. Yishmael: the language of men (Sanhedrin 64b; 90b) — the fork', [FX.NONE])
    if ask == 'yoke':
        ink('15:31', '"despised the word... breached His commandment... cut off, shall be cut off"'); dat('the row yoke = %s' % data['yoke']['value']); move('Shevuot 13a:2 (Rabbi); Pirkei Avot 3:11', 'the yoke, the faces, the covenant; before and after Yom Kippur')
        return out('throws off the yoke / uncovers faces in the Torah; the covenant of circumcision; before and after Yom Kippur (Shevuot 13a; Pirkei Avot 3:11)', ['karet_cut_off'])
    if ask == 'iniquity_in_him':
        ink('15:31', '"his iniquity is in him"'); move('Sanhedrin 90b:16; Yoma 36b:5; Keritot 25b:16', 'after death — the World-to-Come; iniquities = intentional')
        return out('after death — the World-to-Come alluded (Sanhedrin 90b); intentional sins (Yoma 36b)', [FX.NONE])
    if ask == 'census':
        c = CH.karet_census(); dat('the chatat engine CALLED: karet_census -> %s' % c['v']); move('Mishnah Keritot 1:1', 'the thirty-six — the blasphemer and the idolater among them')
        return out('%d — the karet cases (Mishnah Keritot 1:1; the chatat engine CALLED)' % c['v'], [FX.NONE])
    if ask == 'high_hand_posture':
        ink('15:30', '"with a high hand" — Exod 14:8, Num 33:3 the exodus\'s posture'); move('Onkelos 15:30', '"with uncovered head"')
        return out('the exodus\'s posture — "with a high hand" (Exod 14:8; Num 33:3)', [FX.NONE])
    if ask == 'filthy_place':
        move('Berakhot 24b:20 (Rav Adda bar Ahava)', 'reciting in a filthy place — "despised the word"')
        return out('reciting in a filthy place — despised (Rav Adda bar Ahava)', [FX.NONE])
    if ask == 'own_body':
        move('Shabbat 153b:13 (Rava)', 'liable only for an act with his own body — the juxtaposition to idolatry')
        return out("liable only for an act with his own body — the Sabbath's application (Shabbat 153b)", [FX.NONE])
    raise KeyError(ask)


# ---- THE WRAP — the daemon, the scene, the narrative ------------------------------------------------------
def law_shelach(event, world):
    """Num 13:1-15:31 (cold_run_shelach.py F1-F7). installed_by boot — the laws spoken at their verses; the libations' and the challah's
    land gate is the cell's own (15:2, 15:18), not the daemon's, so the spies' lines dispatch in year 2."""
    k, src = event['kind'], event['case_source']
    E_ = lambda eff, s, cp=None, amount=None, due=None, law='', value=None: {'effect': eff, 'subject': s, 'counterparty': cp, 'amount': amount, 'due': due, 'value': value if value is not None else True, 'source_law': law, 'case_source': src}
    day = event.get('day', world.clock.day)      # THE SEQUENTIAL RUN: the event's own day
    if k == 'spies_commanded':
        return [E_('commanded', event['subject'], value='the_sending', law='F1 [INK 13:2 "send for yourself men that they may spy out the land" — the sending owed on Moses, at his discretion (Sotah 34b:3)]')]
    if k == 'spies_sent':
        world.close('moses', 'commanded', 'Num 13:3 — and Moses sent them from the wilderness of Paran by the mouth of the LORD', value='the_sending')
        return [E_('sent_to_spy', event['subject'], value='the twelve by tribe — a fourth order, Levi absent, Joseph over Manasseh; Hoshea renamed Joshua (13:16)', law='F1 [INK 13:3-16; Sotah 34b:5-8]'),
                E_('spied_forty_days', event['subject'], due=day + FORTY[0], value='forty days of spying — the return "at the end of forty days" (13:25) on the Ninth of Av (Taanit 29a:5); the fire the day after the marker (CF2)', law='F1 [INK 13:25; Taanit 29a:5-6]')]
    if k == 'spies_instructed':
        return [E_('commanded', event['subject'], value='the_questionnaire', law='F1 [INK 13:17-20 — the seven questions owed an answer: strong or weak, few or many, good or bad, camps or fortresses, fat or lean, trees or none; the fruit]')]
    if k == 'spies_went_up':
        return []                                  # the timer runs; the route and Hebron the line's values
    if k == 'spies_returned':
        return []                                  # the return is the tape's reading-placed marker (2, 5, 9); the timer fires the day after
    if k == 'report_given':
        if not src.startswith('Num 13:'):           # A SHARED KIND'S SECOND SEAT (3b's lesson, the sixth instance): 'report_given' is an earlier story's kind — this daemon writes only at its own seat (THE REST read one stray write on the first run)
            return []
        world.close(event['subject'], 'commanded', 'Num 13:27 — and they told him and said: we came to the land where you sent us', value='the_questionnaire')
        return [E_('report_given', event['subject'], value='fat (milk and honey, the fruit); strong (the people fierce, the Anak); fortified; the map — the questionnaire answered; truth first (Sotah 35a:2)', law='F1 [INK 13:27-29; the questionnaire\'s debit CLOSED]')]
    if k == 'caleb_hushed_the_people':
        return [E_('plea_made', 'caleb', cp='israel', value='we shall surely go up and possess it, for we can surely prevail — the ruse (Sotah 35a:3-6)', law='F1 [INK 13:30]')]
    if k == 'evil_report_spread':
        return [E_('evil_report_spread', event['subject'], value='stronger than us — or than Him; a land that eats its inhabitants; the Nephilim; grasshoppers (13:31-33)', law='F1 [INK 13:31-33; Arakhin 15a:12-13; Sotah 35a:7-9]')]
    if k == 'congregation_wept':
        return [E_('wept', event['subject'], value='that night — the Ninth of Av (Taanit 29a:7; Sotah 35a:11; Sanhedrin 104b:4)', law='F2 [INK 14:1]'),
                E_('tested_the_lord', event['subject'], value='the tenth trial — the spies (Arakhin 15a-b; 14:22 "these ten times"); "let us appoint a head and return to Egypt"', law='F2 [INK 14:2-4; Arakhin 15a:10 (Reish Lakish: sealed for this sin)]')]
    if k == 'joshua_and_caleb_pleaded':
        return [E_('plea_made', 'joshua', cp='israel', value='the garments rent; the land is very very good; their shadow has departed; fear them not (14:6-9)', law='F2 [INK 14:5-9; Taanit 14b:13]'),
                E_('plea_made', 'caleb', cp='israel', value='the garments rent; the land is very very good; fear them not (14:6-9)', law='F2 [INK 14:5-9]')]
    if k == 'glory_appeared_at_the_threat':
        return [E_('glory_appeared', 'the-tabernacle', cp='HEAVEN', value='at the stoning threat — the glory of the LORD appeared in the tent of meeting to all the children of Israel (14:10); the stones thrown upward (Sotah 35a:12)', law='F2 [INK 14:10; Lev 9:23 the first seat, Num 16:19, 17:7, 20:6 the rest]')]
    if k == 'moses_pleaded_on_the_attributes':
        return [E_('plea_made', 'moses', cp='HEAVEN', value='the offer refused a second time (14:12 = Exod 32:10); Egypt will hear (14:13); the attributes quoted back "as You have spoken" (14:17-18 — a subsequence of Exod 34:6-7); pardon, I pray (14:19)', law='F2 [INK 14:11-19; Berakhot 32a:27-31; Sanhedrin 111b:1]')]
    if k == 'pardoned_and_decreed':
        return [E_('pardoned', 'israel', cp='HEAVEN', value='I have pardoned according to your word (14:20 — once in the Bible); the rider: they shall not see the land (14:21-23)', law='F2 [INK 14:20-23; Berakhot 32a:29]'),
                E_('holding_owed', 'caleb', cp='HEAVEN', value='him I will bring into the land where he went, and his seed shall possess it (14:24) — Hebron: PAID at Josh 14:13-14; Moses\' oath there (Josh 14:9)', law='F2 [INK 14:24; Josh 14:6-14; Deut 1:36]'),
                E_('commanded', 'israel', value='the_turn_back', law='F2 [INK 14:25 "tomorrow turn and journey into the wilderness by the way of the Red Sea" — OPEN in this span: its run Num 21:4 (the same phrase), Deut 2:1]')]
    if k == 'decree_declared':
        return [E_('sentence_pronounced', 'israel', cp='HEAVEN', value='in this wilderness your carcasses shall fall — the census set %d (Bamidbar CALLED), from twenty and upward; Caleb and Joshua excepted; the children brought in; a day for a year (14:28-35)' % BM.TOTAL, law='F2 [INK 14:26-35; Mishnah Sanhedrin 1:6, 10:3; Bava Batra 121b:8-11]'),
                E_('carcasses_fall_in_the_wilderness', 'israel', cp='HEAVEN', due=world.clock.calendar.add(day, 38, 'year'), value='forty years, a day for a year (14:33-34) — thirty-eight from Kadesh to Zered by Deut 2:14\'s ink: due the ninth of Av of the fortieth year; the dying ceased on the fifteenth (Bava Batra 121a:9)', law='F2 [INK 14:33-34; Deut 2:14-16; Ezek 4:6]')]
    if k == 'ten_spies_died_by_plague':
        return [E_('put_to_death', event['subject'], cp='HEAVEN', value='died by the plague before the LORD (14:37) — the tongue to the navel (Sotah 35a:13); Joshua and Caleb lived (14:38)', law='F2 [INK 14:36-38; Arakhin 15a:13; Mishnah Sanhedrin 10:3]')]
    if k == 'presumed_to_go_up':
        return [E_('presumed_to_go_up', 'israel', value='mourned; rose early; the LORD is not among you; presumed to go up — the ark and Moses did not depart (14:39-44); Zelophehad among them (Shabbat 97a)', law='F2 [INK 14:39-44; Deut 1:41-43]')]
    if k == 'smitten_to_hormah':
        return [E_('defeated', 'israel', cp='amalek-and-the-canaanite', value='smitten and beaten down to Hormah (14:45) — the name used six chapters before its naming at 21:3', law='F2 [INK 14:45; Deut 1:44; Num 21:3; Judg 1:17]')]
    # ---- the exam's case kinds: each names LITERALLY every effect it can write (2b's form — an unnamed effect is a KeyError to read) ----
    if k == 'spies_case':
        v, e, _ = spies({'ask': event['ask']}, DATA); L = 'F1 [%s]' % v; s_ = event['person']
        W = {'accepted': E_('accepted', s_, value=v, law=L), 'disqualified': E_('disqualified', s_, value=v, law=L), 'plea_made': E_('plea_made', s_, value=v, law=L), 'evil_report_spread': E_('evil_report_spread', s_, value=v, law=L)}
        return [W[x] for x in e if x != FX.NONE]
    if k == 'decree_case':
        v, e, _ = decree({'ask': event['ask']}, DATA); L = 'F2 [%s]' % v; s_ = event['person']
        W = {'accepted': E_('accepted', s_, value=v, law=L), 'disqualified': E_('disqualified', s_, value=v, law=L), 'exempt': E_('exempt', s_, value=v, law=L), 'sentence_pronounced': E_('sentence_pronounced', s_, cp='HEAVEN', value=v, law=L),
             'put_to_death': E_('put_to_death', s_, cp='HEAVEN', value=v, law=L), 'holding_owed': E_('holding_owed', s_, value=v, law=L), 'wept': E_('wept', s_, value=v, law=L), 'pardoned': E_('pardoned', s_, value=v, law=L),
             'carcasses_fall_in_the_wilderness': E_('carcasses_fall_in_the_wilderness', s_, cp='HEAVEN', due=world.clock.calendar.add(day, 38, 'year'), value=v, law=L), 'commanded': E_('commanded', s_, value=v, law=L), 'presumed_to_go_up': E_('presumed_to_go_up', s_, value=v, law=L), 'defeated': E_('defeated', s_, value=v, law=L)}
        return [W[x] for x in e if x != FX.NONE]
    if k == 'libation_case':
        v, e, _ = libations({'ask': event['ask'], 'offering': event.get('offering'), 'where': event.get('where'), 'pair': event.get('pair', ('bull', 'ram')), 'logs': event.get('logs')}, DATA); L = 'F3 [%s]' % v; s_ = event['person']
        W = {'accepted': E_('accepted', s_, value=v, law=L), 'disqualified': E_('disqualified', s_, value=v, law=L), 'exempt': E_('exempt', s_, value=v, law=L), 'libation_owed': E_('libation_owed', s_, value=v, law=L)}
        return [W[x] for x in e if x != FX.NONE]
    if k == 'stranger_case':
        v, e, _ = stranger({'ask': event['ask']}, DATA); L = 'F4 [%s]' % v; s_ = event['person']
        W = {'accepted': E_('accepted', s_, value=v, law=L), 'disqualified': E_('disqualified', s_, value=v, law=L), 'exempt': E_('exempt', s_, value=v, law=L)}
        return [W[x] for x in e if x != FX.NONE]
    if k == 'challah_case':
        v, e, _ = challah({'ask': event['ask'], 'who': event.get('who', 'householder'), 'impure': event.get('impure'), 'grain': event.get('grain'), 'owner': event.get('owner', 'israelite'), 'direction': event.get('direction', 'in')}, DATA); L = 'F5 [%s]' % v; s_ = event['person']
        W = {'accepted': E_('accepted', s_, value=v, law=L), 'disqualified': E_('disqualified', s_, value=v, law=L), 'exempt': E_('exempt', s_, value=v, law=L), 'due_to_priest': E_('due_to_priest', s_, cp='the-priest', value=v, law=L)}
        return [W[x] for x in e if x != FX.NONE]
    if k == 'error_case':
        v, e, _ = error({'ask': event['ask'], 'knew_error': event.get('knew_error', False)}, DATA); L = 'F6 [%s]' % v; s_ = event['person']
        W = {'accepted': E_('accepted', s_, value=v, law=L), 'disqualified': E_('disqualified', s_, value=v, law=L), 'exempt': E_('exempt', s_, value=v, law=L), 'atoned_forgiven': E_('atoned_forgiven', s_, value=v, law=L)}
        return [W[x] for x in e if x != FX.NONE]
    if k == 'high_hand_case':
        v, e, _ = high_hand({'ask': event['ask'], 'intent': event.get('intent', 'intentional')}, DATA); L = 'F7 [%s]' % v; s_ = event['person']
        W = {'accepted': E_('accepted', s_, value=v, law=L), 'disqualified': E_('disqualified', s_, value=v, law=L), 'exempt': E_('exempt', s_, value=v, law=L), 'karet_cut_off': E_('karet_cut_off', s_, cp='HEAVEN', value=v, law=L), 'atoned_forgiven': E_('atoned_forgiven', s_, value=v, law=L)}
        return [W[x] for x in e if x != FX.NONE]
    return []


def scene():
    """THE SCENE — the exam's rows replayed on the world engine (the exodus epoch): the decree's set, the libation owed and refused, the
    convert's olah, the householder's twenty-fourth, the individual's she-goat, the high hand's karet."""
    with contextlib.redirect_stdout(io.StringIO()):
        w = WE.World(era='Num 13-15: Mishnah Sanhedrin 1, 10, Menachot 9, 12-13, Challah 1-4, Horayot 1-2, Keritot 1, Shekalim 7 and the Talmud\'s rows on the engine (the exodus epoch)', epoch='exodus')
        w.laws = [law_shelach]
        w.advance(w.clock.day_in('exodus', 2, 5, 9))
        w.submit({'kind': 'spies_case', 'subject': 'the-hushing-spy', 'person': 'the-hushing-spy', 'ask': 'caleb_hushed', 'case_source': 'Sotah 35a:3; Num 13:30 — persuaded them'})
        w.submit({'kind': 'decree_case', 'subject': 'the-generation-of-the-wilderness', 'person': 'the-generation-of-the-wilderness', 'ask': 'set', 'case_source': 'Bava Batra 121b:8; Num 14:29 — the census set (Bamidbar called)'})
        w.submit({'kind': 'decree_case', 'subject': 'the-spy-of-judah', 'person': 'the-spy-of-judah', 'ask': 'caleb_entitlement', 'case_source': 'Josh 14:13; Num 14:24 — Hebron owed'})
        w.submit({'kind': 'libation_case', 'subject': 'the-vowed-olah', 'person': 'the-vowed-olah', 'ask': 'takes', 'offering': 'olah', 'case_source': 'Mishnah Menachot 9:6; Num 15:3 — libations'})
        w.submit({'kind': 'libation_case', 'subject': 'the-firstborn-offering', 'person': 'the-firstborn-offering', 'ask': 'takes', 'offering': 'firstborn', 'case_source': 'Mishnah Menachot 9:6; Num 15:3 — no libations'})
        w.submit({'kind': 'libation_case', 'subject': 'the-five-log-pledge', 'person': 'the-five-log-pledge', 'ask': 'donated', 'logs': 5, 'case_source': 'Mishnah Menachot 12:4; Num 15:13 — no such libation'})
        w.submit({'kind': 'stranger_case', 'subject': 'the-convert', 'person': 'the-convert', 'ask': 'convert_offering', 'case_source': 'Keritot 8b:18; Num 15:14 — as you do'})
        w.submit({'kind': 'challah_case', 'subject': 'the-householder', 'person': 'the-householder', 'ask': 'measure', 'who': 'householder', 'case_source': 'Mishnah Challah 2:7; Num 15:20 — one twenty-fourth'})
        w.submit({'kind': 'error_case', 'subject': 'the-unwitting-idolater', 'person': 'the-unwitting-idolater', 'ask': 'individual', 'case_source': 'Mishnah Horayot 2:6; Num 15:27 — the she-goat (the chatat engine called)'})
        w.submit({'kind': 'high_hand_case', 'subject': 'the-high-handed', 'person': 'the-high-handed', 'ask': 'class', 'intent': 'intentional', 'case_source': 'Horayot 8a:14; Num 15:30 — karet (the chatat engine called)'})
    n = lambda eid, eff: len([e for e in w.entity(eid).ledger if e['effect'] == eff])
    return (n('the-hushing-spy', 'plea_made'), n('the-generation-of-the-wilderness', 'sentence_pronounced'), n('the-spy-of-judah', 'holding_owed'), n('the-vowed-olah', 'libation_owed'), n('the-firstborn-offering', 'exempt'),
            n('the-five-log-pledge', 'disqualified'), n('the-convert', 'accepted'), n('the-householder', 'due_to_priest'), n('the-unwitting-idolater', 'accepted'), n('the-high-handed', 'karet_cut_off'), len(w.entities)), w
SCENE, _W = scene()
SCENE_PREDICTED = (1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 10)   # PREDICTED from the design BEFORE the first run: one effect per row — the hushing spy's plea; the generation sentenced; Caleb's holding owed; the vowed olah's libation owed; the firstborn exempt; the five logs refused; the convert accepted; the householder's twenty-fourth due; the idolater's she-goat accepted; the high hand cut off; ten entities
assert SCENE == SCENE_PREDICTED, ('THE NUMBERS WALK: the Shelach scene moved from its prediction', SCENE, SCENE_PREDICTED)


def narrative():
    """THE NUMBERS WALK 4b (2026-09-10; NUMBERS_WALK.md "Sitting 4b"): the portion's own acts AS HISTORY — the seventeen lines of Num 13:1-14:45 in
    the text's order on a world with this runner's daemon, from the sending's day (2, 3, 29) (12:16's marker — Taanit 29a:5), the ONE
    reading-placed marker at 13:25 (2, 5, 9) the Ninth of Av, the forty days' timer firing the day after it (the inclusive count, CF2) on a
    closing walk, the thirty-eight years' timer left PENDING. Not a graded cell: the tuple below is a tripwire PREDICTED before the first run;
    the sequence world's RUN tuple grades the tape."""
    with contextlib.redirect_stdout(io.StringIO()):
        w = WE.World(era='Num 13-14: Shelach on the tape — the spies, the decree (the exodus epoch)', epoch='exodus')
        w.laws = [law_shelach]
        w.advance(w.clock.day_in('exodus', 2, 3, 29))
        w.submit({'kind': 'spies_commanded', 'subject': 'moses', 'one_per_tribe': True, 'princes': True, 'case_source': 'Num 13:1-2 — and the LORD spoke to Moses saying: send for yourself men that they may spy out the land of Canaan which I give to the children of Israel; one man, one man for his fathers\' tribe you shall send, every one a prince among them'})
        w.submit({'kind': 'spies_sent', 'subject': 'the-twelve-spies', 'names': SPY_TRIBES, 'renamed': 'Hoshea to Joshua', 'days': FORTY[0], 'case_source': 'Num 13:3-16 — and Moses sent them from the wilderness of Paran by the mouth of the LORD, all of them men, heads of the children of Israel... and Moses called Hoshea son of Nun Joshua'})
        w.submit({'kind': 'spies_instructed', 'subject': 'the-twelve-spies', 'questions': QUESTIONS, 'season': 'the days of the first-ripe grapes', 'case_source': 'Num 13:17-20 — and Moses sent them to spy out the land of Canaan and said to them: go up this way by the south and go up into the mountain; and see the land, what it is... and be strong and take of the fruit of the land; and the days were the days of the first-ripe grapes'})
        w.submit({'kind': 'spies_went_up', 'subject': 'the-twelve-spies', 'route': 'Zin to Rehob, the entrance of Hamath', 'hebron': DATA['hebron_visitor']['value'], 'giants': ['Ahiman', 'Sheshai', 'Talmai'], 'cluster': 'on a pole between two', 'eshcol': True, 'case_source': 'Num 13:21-24 — and they went up and spied out the land from the wilderness of Zin to Rehob, to the entrance of Hamath; and they went up by the south, and he came to Hebron... and they came to the wadi of Eshcol and cut from there a branch with one cluster of grapes, and they carried it on a pole between two'})
        w.marker('Num 13:25', w.clock.day_in('exodus', 2, 5, 9), value='and they returned from spying out the land at the end of forty days (13:25) — READING-PLACED by Taanit 29a:5 (the baraita: sent on the twenty-ninth of Sivan, returned on the Ninth of Av; "forty days minus one" — thirty-nine; Abaye: Tammuz full); Mishnah Ta\'anit 4:6 the decree\'s day', placement='reading_placed')
        w.submit({'kind': 'spies_returned', 'subject': 'the-twelve-spies', 'days': FORTY[0], 'to': 'Kadesh', 'case_source': 'Num 13:25-26 — and they returned from spying out the land at the end of forty days; and they went and came to Moses and to Aaron and to all the congregation of the children of Israel, to the wilderness of Paran, to Kadesh, and brought back word to them and to all the congregation, and showed them the fruit of the land'})
        w.submit({'kind': 'report_given', 'subject': 'the-twelve-spies', 'answers': 'fat; strong; fortified; the Anak; the map', 'case_source': 'Num 13:27-29 — and they told him and said: we came to the land where you sent us, and it also flows with milk and honey, and this is its fruit; but the people who dwell in the land are strong, and the cities are fortified, very great, and also the children of Anak we saw there; Amalek dwells in the land of the south...'})
        w.submit({'kind': 'caleb_hushed_the_people', 'subject': 'caleb', 'words': 'we shall surely go up and possess it, for we can surely prevail over it', 'case_source': 'Num 13:30 — and Caleb hushed the people toward Moses and said: we shall surely go up and possess it, for we can surely prevail over it'})
        w.submit({'kind': 'evil_report_spread', 'subject': 'the-ten-spies', 'slander': 'stronger than us; a land that eats its inhabitants', 'nephilim': True, 'case_source': 'Num 13:31-33 — but the men who went up with him said: we are not able to go up against the people, for they are stronger than us; and they brought out an evil report of the land which they had spied to the children of Israel... and there we saw the Nephilim... and we were in our own eyes as grasshoppers'})
        w.submit({'kind': 'congregation_wept', 'subject': 'israel', 'night': 'that night', 'murmur': 'would that we had died in Egypt or in this wilderness', 'head': 'let us appoint a head and return to Egypt', 'case_source': 'Num 14:1-4 — and all the congregation lifted up and gave their voice, and the people wept that night; and all the children of Israel murmured against Moses and against Aaron... and they said one to another: let us appoint a head and return to Egypt'})
        w.submit({'kind': 'joshua_and_caleb_pleaded', 'subject': 'joshua', 'fell': 'Moses and Aaron on their faces', 'rent': 'Joshua and Caleb their garments', 'words': 'the land is very very good; fear not the people of the land', 'case_source': 'Num 14:5-9 — and Moses and Aaron fell on their faces before all the assembly of the congregation of the children of Israel; and Joshua son of Nun and Caleb son of Jephunneh, of those who had spied out the land, rent their garments; and they said to all the congregation of the children of Israel: the land through which we passed to spy it out, the land is very very good'})
        w.submit({'kind': 'glory_appeared_at_the_threat', 'subject': 'the-tabernacle', 'threat': 'to stone them with stones', 'case_source': 'Num 14:10 — and all the congregation said to stone them with stones; and the glory of the LORD appeared in the tent of meeting to all the children of Israel'})
        w.submit({'kind': 'moses_pleaded_on_the_attributes', 'subject': 'moses', 'offer': 'I will make of you a greater nation', 'argument': 'Egypt will hear', 'attributes': ' '.join(N18), 'case_source': 'Num 14:11-19 — and the LORD said to Moses: how long will this people scorn Me... I will smite them with the pestilence and disinherit them, and make of you a greater and mightier nation than they; and Moses said to the LORD: then Egypt will hear... and now, I pray, let the power of my Lord be great, as You have spoken, saying: the LORD, long of anger and abundant in kindness... pardon, I pray, the iniquity of this people'})
        w.submit({'kind': 'pardoned_and_decreed', 'subject': 'israel', 'pardon': 'I have pardoned according to your word', 'ten_times': TEN[0], 'caleb': 'him I will bring into the land where he went', 'turn': 'tomorrow turn and journey by the way of the Red Sea', 'case_source': 'Num 14:20-25 — and the LORD said: I have pardoned according to your word; but as I live... all the men who have seen My glory... and have tried Me these ten times... shall not see the land... but My servant Caleb... him I will bring into the land where he went, and his seed shall possess it... tomorrow turn and journey into the wilderness by the way of the Red Sea'})
        w.submit({'kind': 'decree_declared', 'subject': 'israel', 'set': BM.TOTAL, 'exceptions': ['Caleb', 'Joshua'], 'years': FORTY_YEARS[0], 'day_for_year': DAY_YEAR, 'case_source': 'Num 14:26-35 — and the LORD spoke to Moses and to Aaron saying: how long shall I bear with this evil congregation... say to them: as I live, says the LORD, surely as you have spoken in My ears, so I will do to you: in this wilderness your carcasses shall fall, and all your counted by all your number, from twenty years old and upward... your sons shall be shepherds in the wilderness forty years... forty days, a day for a year, a day for a year'})
        w.submit({'kind': 'ten_spies_died_by_plague', 'subject': 'the-ten-spies', 'mode': DATA['spies_death_mode']['value'], 'survivors': ['Joshua', 'Caleb'], 'case_source': 'Num 14:36-38 — and the men whom Moses sent to spy out the land, who returned and made all the congregation murmur against him by bringing out an evil report of the land, those men who brought out the evil report of the land died by the plague before the LORD; but Joshua son of Nun and Caleb son of Jephunneh lived'})
        w.submit({'kind': 'presumed_to_go_up', 'subject': 'israel', 'mourned': True, 'warning': 'the LORD is not among you', 'ark_stayed': True, 'case_source': 'Num 14:39-44 — and Moses spoke these words to all the children of Israel, and the people mourned greatly; and they rose early in the morning and went up to the top of the mountain, saying: here we are, and we will go up to the place which the LORD said, for we have sinned; and Moses said: why do you transgress the mouth of the LORD?... and they presumed to go up to the top of the mountain, but the ark of the covenant of the LORD and Moses did not depart from the midst of the camp'})
        w.submit({'kind': 'smitten_to_hormah', 'subject': 'israel', 'by': 'the Amalekite and the Canaanite', 'to': 'Hormah', 'case_source': 'Num 14:45 — and the Amalekite and the Canaanite who dwelt in that mountain came down and smote them and beat them down to Hormah'})
        w.advance(w.clock.day_in('exodus', 2, 5, 15))     # a closing walk to the fifteenth of Av: the forty days' timer fires at (2, 5, 10); the thirty-eight years' stays pending
    n = lambda eid, eff: len([e for e in w.entity(eid).ledger if e['effect'] == eff])
    is_open = lambda eid, eff: [e.get('open') for e in w.entity(eid).ledger if e['effect'] == eff]
    L = lambda k: len([l for l in w.log if l[0] == k])
    ex = w.clock.eras['exodus']
    markers = [l for l in w.log if l[0] == 'MARKER']
    fires = [l for l in w.log if l[0] == 'TIMER-FIRE']
    return (n('moses', 'commanded'), is_open('moses', 'commanded'), n('moses', 'plea_made'),
            n('the-twelve-spies', 'sent_to_spy'), n('the-twelve-spies', 'spied_forty_days'), n('the-twelve-spies', 'commanded'), is_open('the-twelve-spies', 'commanded'), n('the-twelve-spies', 'report_given'),
            n('caleb', 'plea_made'), n('caleb', 'holding_owed'), is_open('caleb', 'holding_owed'), n('joshua', 'plea_made'),
            n('the-ten-spies', 'evil_report_spread'), n('the-ten-spies', 'put_to_death'),
            n('israel', 'wept'), n('israel', 'tested_the_lord'), n('israel', 'pardoned'), n('israel', 'commanded'), is_open('israel', 'commanded'), n('israel', 'sentence_pronounced'), n('israel', 'carcasses_fall_in_the_wilderness'), n('israel', 'presumed_to_go_up'), n('israel', 'defeated'),
            n('the-tabernacle', 'glory_appeared'),
            L('TIMER-SET'), L('TIMER-FIRE'), [ex.date(f[1]) for f in fires], len(markers), [m[2].get('retrograde') for m in markers], L('EVENT'), L('WRITE'), len(w.entities)), w


NARRATIVE, _WN = narrative()
NARRATIVE_PREDICTED = (1, [False], 1,
                       1, 1, 1, [False], 1,
                       2, 1, [True], 1,
                       1, 1,
                       1, 1, 1, 1, [True], 1, 0, 1, 1,
                       1,
                       2, 1, [(2, 5, 10)], 1, [False], 17, 20, 7)   # THE FIRST RUN'S READING (two slots retyped): a TIMER'S SETTING IS NOT A LEDGER WRITE and its entry lands at the FIRE — the pending thirty-eight years has no entry on Israel's ledger yet (0, not 1), and the writes are the nineteen non-timer effects plus the forty days' fire (20, not 22); every other slot as PREDICTED from the design BEFORE the first run (NUMBERS_WALK.md "Sitting 4b"): Moses' sending closed by 13:3 and his plea; the twelve sent, timed, questioned (closed by the report), reporting; Caleb's two pleas and his holding OPEN; Joshua's plea; the ten's report and death; Israel wept, tested the tenth time, pardoned, the turn back OPEN, sentenced, timed, presumed, defeated; the glory on the tent; TWO TIMERS set, ONE fired — the forty days at (2, 5, 10), the day after the return marker (the inclusive count, CF2); one forward marker; seventeen events; twenty-two writes (twenty-one at the lines + the fire's one); seven entities
assert NARRATIVE == NARRATIVE_PREDICTED, ('THE NUMBERS WALK: Shelach\'s narrative moved from its prediction', NARRATIVE, NARRATIVE_PREDICTED)


# =====================================================================
# Motion 2 — THE TEST DATA: the answer sheet's rows (the docket's LAW rows).
# =====================================================================
CASES = [
    # F1 — the spies
    ('Sotah 34b:3; Deut 1:22-23 — send for yourself', lambda: spies({'ask': 'send_for_yourself'}, DATA), "at Moses' discretion — 'for yourself' (Reish Lakish); the people's asking (Deut 1:22)"),
    ('Num 13:2-15 — one per tribe (computed)', lambda: spies({'ask': 'one_per_tribe'}, DATA), '12 — one man per tribe, princes; Levi absent'),
    ('Num 13:4-15 — the fourth order (computed)', lambda: spies({'ask': 'fourth_order'}, DATA), 'a fourth order of the twelve — Reuben, Simeon, Judah, Issachar, Ephraim, Benjamin, Zebulun, Manasseh under Joseph, Dan, Asher, Naphtali, Gad'),
    ('Sotah 34b:8; Tosefta Berakhot 1:15 — the name (computed)', lambda: spies({'ask': 'joshua_name'}, DATA), 'Hoshea to Joshua at 13:16 — the new name at 8 seats before it, the old at Deut 32:44 (the same man)'),
    ('Num 13:18-20 — the questionnaire (computed)', lambda: spies({'ask': 'questionnaire'}, DATA), '7 questions — strong or weak, few or many, good or bad, camps or fortresses, fat or lean, trees or none; and the fruit'),
    ('Num 13:27-29 — the answers', lambda: spies({'ask': 'report_answers'}, DATA), 'the report answers: fat; strong; fortified; the Anak; the map — Amalek south, the mountain peoples, the Canaanite by the sea and the Jordan'),
    ('Sotah 34b:7 — he came to Hebron', lambda: spies({'ask': 'hebron_visitor'}, DATA), "Caleb alone at the graves (Rava, Sotah 34b:7) — the singular verb the ink's"),
    ('Sotah 34b:11; Ketubot 112a:8 — Hebron before Zoan', lambda: spies({'ask': 'hebron_zoan'}, DATA), '7 — built seven years before Zoan: sevenfold fertility (Sotah 34b:11; Ketubot 112a)'),
    ('Sotah 34a:9 — the cluster', lambda: spies({'ask': 'cluster'}, DATA), 'on a pole between two — two poles, eight bearers (Sotah 34a); 480 seah'),
    ('Num 13:24; Deut 1:24 — Eshcol', lambda: spies({'ask': 'eshcol'}, DATA), 'named after the cluster (13:24); Deut 1:24'),
    ('Num 13:25 — forty days', lambda: spies({'ask': 'forty_days'}, DATA), '40 days (13:25) — the timer; a day for a year (14:34)'),
    ('Sotah 35a:1 — the going and the coming', lambda: spies({'ask': 'going_like_coming'}, DATA), 'the going with wicked counsel like the coming (R. Shimon ben Yochai, Sotah 35a:1)'),
    ('Sotah 35a:2 — the report\'s form', lambda: spies({'ask': 'report_form'}, DATA), 'truth first, then the slander — a slander that does not begin with truth does not stand (R. Meir)'),
    ('Sotah 35a:3-6 — Caleb hushed', lambda: spies({'ask': 'caleb_hushed'}, DATA), 'persuaded them (Rabba) — the ruse: is this the only thing the son of Amram did?'),
    ('Sotah 35a:7; Arakhin 15a:12; Menachot 53b:9 — stronger than', lambda: spies({'ask': 'stronger_than'}, DATA), "stronger than us, read stronger than Him — heresy (R. Chanina bar Pappa; M-16's class)"),
    ('Arakhin 15a:13 — punished for', lambda: spies({'ask': 'punished_for'}, DATA), 'the evil report (14:37), not the blasphemy — Rabba / Reish Lakish'),
    ('Arakhin 15a:6; Mishnah Arakhin 3:5 — the sentence sealed', lambda: spies({'ask': 'slander_sealed'}, DATA), 'the sentence sealed by the evil report — speech severer than deeds (Mishnah Arakhin 3:5)'),
    ('Sotah 35a:8 — a land that eats', lambda: spies({'ask': 'consumes_inhabitants'}, DATA), "the deaths for their good — the mourning that hid them (Rava); Job's eulogy (some say)"),
    ('Sotah 35a:9 — the grasshoppers', lambda: spies({'ask': 'grasshoppers'}, DATA), 'liars — "in their eyes" unknowable (Rav Mesharshiyya)'),
    ('Bava Batra 15a:14 — Job', lambda: spies({'ask': 'job'}, DATA), "Job in the spies' days — trees / Utz (Rava, Bava Batra 15a)"),
    ('Tosefta Keritot 4:7 — Joshua and Caleb equal', lambda: spies({'ask': 'joshua_caleb_equal'}, DATA), 'equal — Caleb first at 13:6, Joshua at 13:8 (Tosefta Keritot 4:7)'),
    ('Sotah 34b:5-6 — named after their deeds', lambda: spies({'ask': 'named_after_deeds'}, DATA), 'Sethur son of Michael — hid the acts, weakened Him; Nahbi son of Vophsi (R. Yitzchak; R. Yochanan)'),
    ('Sotah 34b:9-10; Yoma 10a:6 — the giants (Sheshai not the ordinal)', lambda: spies({'ask': 'giants'}, DATA), 'Ahiman the skilled, Sheshai the pits, Talmai the furrows; the sun a necklace (Sotah 34b:9-10; Yoma 10a)'),
    # F2 — the decree
    ('Taanit 29a:7; Sotah 35a:11; Sanhedrin 104b:4; Mishnah Ta\'anit 4:6 — that night', lambda: decree({'ask': 'that_night'}, DATA), "the night of the Ninth of Av — a weeping for generations (Taanit 29a:7; Sotah 35a:11; Sanhedrin 104b:4); Mishnah Ta'anit 4:6"),
    ('Pirkei Avot 5:4; Arakhin 15a-b — the ten trials (the parser\'s ten)', lambda: decree({'ask': 'ten_trials'}, DATA), "10 — 'these ten times' (14:22; Pirkei Avot 5:4); the ledger's count graded at CF6"),
    ('Arakhin 15a:10 — now', lambda: decree({'ask': 'now_ten'}, DATA), 'sealed for THIS sin — "now" (Reish Lakish, Arakhin 15a:10)'),
    ('Mishnah Sanhedrin 1:6; Berakhot 21b:5; Megillah 23b:8; Sanhedrin 2a:15, 74b:3 — the congregation (computed)', lambda: decree({'ask': 'congregation'}, DATA), '10 — the twelve less Joshua and Caleb (Mishnah Sanhedrin 1:6; Berakhot 21b; Megillah 23b; Sanhedrin 74b)'),
    ('Bava Batra 121b:8 — the set (Bamidbar CALLED)', lambda: decree({'ask': 'set'}, DATA), '603550 — the census set by CALL: from twenty and upward, all your counted; Levi outside (Bava Batra 121b:8); not over sixty (121b:11)'),
    ('Bava Batra 121b:11 — the edges', lambda: decree({'ask': 'set_edges'}, DATA), 'under twenty and over sixty outside — "and upward" / "and upward" with the valuations (Rav Acha bar Yaakov); Levi from thirty (Rav Hamnuna)'),
    ('Num 14:24, 14:30-31 — the exceptions', lambda: decree({'ask': 'exceptions'}, DATA), 'Caleb and Joshua (14:24, 14:30); the children brought in (14:31)'),
    ('Num 14:34; Ezek 4:6 — a day for a year (the parser)', lambda: decree({'ask': 'day_for_year'}, DATA), '[40, 40] — forty days, a day for a year, a day for a year (14:34; Ezek 4:6 verbatim)'),
    ('Deut 2:14 — the count-from (the Calendar)', lambda: decree({'ask': 'count_from'}, DATA), "40 - 38 = 2 — the era's year at the decree: the forty from the exodus (Deut 2:14's thirty-eight from Kadesh)"),
    ('the Calendar — the due', lambda: decree({'ask': 'due'}, DATA), '(40, 5, 9) — the ninth of Av of the fortieth year, by the Calendar; PENDING on the tape (CF3)'),
    ('Bava Batra 121a:9; Taanit 30b:12 — the deaths ceased', lambda: decree({'ask': 'deaths_ceased'}, DATA), 'the fifteenth of Av of the fortieth year — the dying ceased; the speech resumed (Bava Batra 121a:9; Taanit 30b:12; Deut 2:16-17)'),
    ('Mishnah Sanhedrin 10:3; Sanhedrin 108a:3, 110b:2; Tosefta Sanhedrin 13:1 — the wilderness generation\'s share', lambda: decree({'ask': 'wilderness_share'}, DATA), 'no share (R. Akiva — "there they shall die"); a share (R. Eliezer — Ps 50:5)'),
    ('Mishnah Sanhedrin 10:3; Sanhedrin 108a:2, 109b:10 — the spies\' share', lambda: decree({'ask': 'spies_share'}, DATA), 'no share — "died... by plague" (Mishnah Sanhedrin 10:3)'),
    ('Sotah 35a:13 — the ten\'s death', lambda: decree({'ask': 'spies_death_mode'}, DATA), 'the tongue to the navel with worms (R. Sheila); diphtheria (Rav Nachman bar Yitzchak)'),
    ('Bava Batra 118b:3 — the spies\' portions', lambda: decree({'ask': 'spies_portions'}, DATA), "Joshua and Caleb lived in the ten's portions — 'lived' (Ulla, Bava Batra 118b)"),
    ('Berakhot 32a:29 — the pardon (once in the Bible)', lambda: decree({'ask': 'pardon'}, DATA), '"I have pardoned according to your word" — God conceded (R. Yochanan); so it will be (the school of R. Yishmael)'),
    ('Sanhedrin 111b:1 — the plea', lambda: decree({'ask': 'plea'}, DATA), 'the attributes quoted back — "as You have spoken": long of anger even for the wicked (Sanhedrin 111b:1)'),
    ('Num 14:18 against Exod 34:6-7 — the attributes (computed)', lambda: decree({'ask': 'attributes_deleted'}, DATA), 'a subsequence of Exod 34:6-7 — eleven words dropped, none added; Onkelos restores "and sins"'),
    ('Num 14:12; Exod 32:10; Deut 9:14 — the offer (M-23)', lambda: decree({'ask': 'offer_second_seat'}, DATA), "the offer's second seat — Exod 32:10 / Num 14:12 / Deut 9:14 (M-23)"),
    ('Num 14:13; Exod 32:12 — Egypt will hear', lambda: decree({'ask': 'egypt_will_hear'}, DATA), "Moses' Egypt argument at both intercessions (Exod 32:12; Num 14:13)"),
    ('Berakhot 32a:27 — the ability', lambda: decree({'ask': 'ability'}, DATA), 'the ability — yekholet, the feminine noun (Berakhot 32a:27)'),
    ('Berakhot 32a:31 — as I live', lambda: decree({'ask': 'as_i_live'}, DATA), '"you have given Me life with your words" (Rava / Rav Yitzchak)'),
    ('Berakhot 7a; Sanhedrin 27b — upon the children', lambda: decree({'ask': 'upon_children'}, DATA), "when they hold their fathers' deeds (Berakhot 7a; Sanhedrin 27b)"),
    ('Josh 14:6-14 — Caleb\'s entitlement', lambda: decree({'ask': 'caleb_entitlement'}, DATA), 'holding_owed — Hebron; PAID at Josh 14:13-14 (forty-five years; eighty-five; Moses swore that day)'),
    ('Num 14:25; 21:4 — the turn back', lambda: decree({'ask': 'turn_back'}, DATA), 'tomorrow turn — by the way of the Red Sea: OPEN, its run Num 21:4 / Deut 2:1'),
    ('Shabbat 97a:1 — the presumption', lambda: decree({'ask': 'presumption'}, DATA), 'presumed — the ark and Moses stayed; Zelophehad among them (R. Yehuda ben Beteira, Shabbat 97a)'),
    ('Num 14:45; 21:3; Judg 1:17 — Hormah (the proleptic name)', lambda: decree({'ask': 'hormah'}, DATA), 'Hormah — named at 21:3, used at 14:45: THE PROLEPTIC NAME (the registry row carries both); Judg 1:17'),
    ('Taanit 14b:13 — fell and rent', lambda: decree({'ask': 'fell_and_rent'}, DATA), 'Moses and Aaron fell on their faces; Joshua and Caleb rent garments (Taanit 14b)'),
    ('Sotah 35a:12 — the stones', lambda: decree({'ask': 'stones_upward'}, DATA), 'stones thrown upward, as at God (R. Chiyya bar Abba)'),
    ('Megillah 31b:2 — the Ninth of Av\'s reading', lambda: decree({'ask': 'ninth_of_av_reading'}, DATA), 'the Ninth of Av\'s Torah reading — "how long will this people provoke Me" (R. Natan bar Yosef); today Deut 4:25 (Abaye)'),
    ('Pesachim 119b:6 — Joshua childless', lambda: decree({'ask': 'joshua_childless'}, DATA), 'no son — "Joshua son of Nun" and 1 Chr 7:27 (Pesachim 119b)'),
    # F3 — the libations
    ('Num 15:4-10 — the table (computed)', lambda: libations({'ask': 'table'}, DATA), 'lamb 1/10 + 1/4 + 1/4; ram 2/10 + 1/3 + 1/3; bull 3/10 + 1/2 + 1/2 — computed from 15:4-10'),
    ('Exod 29:40; Lev 23:13; Num 28:5-7, 28:14 — the seats (computed); Mishnah Menachot 9:4', lambda: libations({'ask': 'table_seats'}, DATA), "the lamb's quarter-hin at Exod 29:40, Lev 23:13, Num 28:5-7; 28:14 the three rows; the omer's flour doubled (two tenths — Mishnah Menachot 9:4)"),
    ('Mishnah Menachot 9:2-3 — the logs (computed)', lambda: libations({'ask': 'logs'}, DATA), 'lamb 3, ram 4, bull 6 — the hin twelve logs (Mishnah Menachot 9:2)'),
    ('Mishnah Menachot 9:4 — bulls with rams (computed)', lambda: libations({'ask': 'mixing', 'pair': ('bull', 'ram')}, DATA), 'may mix — the same ratio'),
    ('Mishnah Menachot 9:4 — lambs with bulls (computed)', lambda: libations({'ask': 'mixing', 'pair': ('lamb', 'bull')}, DATA), 'may not mix — the ratios differ'),
    ('Mishnah Menachot 9:4 — lambs with lambs (computed)', lambda: libations({'ask': 'mixing', 'pair': ('lamb', 'lamb')}, DATA), 'may mix — the same ratio'),
    ('Mishnah Menachot 12:4 — Sukkot on the Sabbath (computed)', lambda: libations({'ask': 'sukkot_sabbath'}, DATA), '61 tenths — 13 bulls x 3 + 2 rams x 2 + 14 lambs + 2 daily + 2 Sabbath lambs (Mishnah Menachot 12:4)'),
    ('Mishnah Menachot 9:6; Menachot 90b-91a — which offerings', lambda: libations({'ask': 'which_offerings'}, DATA), "all but the firstborn, the tithe, the Passover, the sin offering, the guilt offering; the leper's chatat and asham do (Mishnah Menachot 9:6; 15:5)"),
    ('Mishnah Menachot 9:6 — the olah', lambda: libations({'ask': 'takes', 'offering': 'olah'}, DATA), 'libations'),
    ('Mishnah Menachot 9:6 — the shelamim', lambda: libations({'ask': 'takes', 'offering': 'shelamim'}, DATA), 'libations'),
    ('Mishnah Menachot 9:6 — the firstborn', lambda: libations({'ask': 'takes', 'offering': 'firstborn'}, DATA), 'no libations'),
    ('Mishnah Menachot 9:6 — the Passover', lambda: libations({'ask': 'takes', 'offering': 'pesach'}, DATA), 'no libations'),
    ('Mishnah Menachot 9:6 — the sin offering', lambda: libations({'ask': 'takes', 'offering': 'chatat'}, DATA), 'no libations'),
    ('Menachot 90b:10 — the festival goats', lambda: libations({'ask': 'takes', 'offering': 'festival_goat'}, DATA), 'no libations'),
    ('Menachot 91a:27 — the leper\'s sin offering', lambda: libations({'ask': 'takes', 'offering': 'leper_chatat'}, DATA), "libations — the leper's (15:5)"),
    ('Num 15:3 — a bird olah', lambda: libations({'ask': 'takes', 'offering': 'bird_olah'}, DATA), 'no libations'),
    ('Zevachim 111a:7; Kiddushin 37b:1 — the wilderness (the cell\'s gate)', lambda: libations({'ask': 'takes', 'offering': 'olah', 'where': 'wilderness'}, DATA), 'not yet — before the entry (15:2)'),
    ('Mishnah Menachot 12:4, 13:5; Menachot 104a, 107a — donated', lambda: libations({'ask': 'donated'}, DATA), "not less than three logs — the lamb's; 3, 4, 6 and beyond, never 1, 2, 5 (Mishnah Menachot 12:4, 13:5; Menachot 104a)"),
    ('Mishnah Menachot 12:4 — three logs', lambda: libations({'ask': 'donated', 'logs': 3}, DATA), 'a valid libation of 3 logs'),
    ('Mishnah Menachot 12:4 — five logs', lambda: libations({'ask': 'donated', 'logs': 5}, DATA), 'no such libation — 5 logs'),
    ('Mishnah Menachot 12:4 — two logs', lambda: libations({'ask': 'donated', 'logs': 2}, DATA), 'no such libation — 2 logs'),
    ('Mishnah Menachot 12:4 — seven logs', lambda: libations({'ask': 'donated', 'logs': 7}, DATA), 'a valid libation of 7 logs'),
    ('Mishnah Menachot 12:5; Menachot 107a:17; Zevachim 91b:10 — oil donated', lambda: libations({'ask': 'donated_oil'}, DATA), 'wine yes; oil — R. Akiva no, R. Tarfon yes; Rabbi three logs (Mishnah Menachot 12:5; 107a:17)'),
    ('Zevachim 91b:12 — the donated wine\'s disposal', lambda: libations({'ask': 'donated_wine_disposal'}, DATA), "on the altar's fire — an offering made by fire (Shmuel, Zevachim 91b)"),
    ('Menachot 73b:14; Zevachim 45a:14; Temurah 3a:10; Mishnah Shekalim 7:6 — the gentile', lambda: libations({'ask': 'gentile'}, DATA), "no independent libations; his olah's required (15:11, 15:13); the public pays if he sent none (Mishnah Shekalim 7:6)"),
    ('Mishnah Shekalim 7:5 — the found animal', lambda: libations({'ask': 'found_animal'}, DATA), 'from public funds (Mishnah Shekalim 7:5)'),
    ('Mishnah Menachot 9:7 — the heir', lambda: libations({'ask': 'heir'}, DATA), 'the heir brings the libations (Mishnah Menachot 9:7)'),
    ('Menachot 27a:7-8 — so', lambda: libations({'ask': 'so'}, DATA), 'the exact measure indispensable — "so" (Menachot 27a)'),
    ('Menachot 91b:20 — the calf', lambda: libations({'ask': 'calf'}, DATA), 'as a bull — "for the one bull" (Menachot 91b:20)'),
    ('Chullin 23a:6; Mishnah Parah 1:3 — the palges', lambda: libations({'ask': 'palges'}, DATA), "the ram's libations, not counted — the thirteen-month animal (Mishnah Parah 1:3; Chullin 23a)"),
    ('Mishnah Parah 1:3 — the ages', lambda: libations({'ask': 'ages'}, DATA), 'lambs to a year, rams from thirteen months and a day (Mishnah Parah 1:3)'),
    ('Menachot 91b:9, 91b:20 — the definite one', lambda: libations({'ask': 'the_one'}, DATA), "the definite one read — the woman's olah, the tithe's eleventh (Menachot 91b:9); the calf (91b:20)"),
    ('Menachot 91b:12 — Aaron\'s ram', lambda: libations({'ask': 'aarons_ram'}, DATA), 'libations — "or for a ram" (Rav Sheshet)'),
    ('Menachot 91a:18-24 — each animal', lambda: libations({'ask': 'each_animal'}, DATA), 'separate libations per animal, even consecrated together (15:11-12)'),
    ('Mishnah Menachot 12:3 — whole tenths', lambda: libations({'ask': 'tenths_integral'}, DATA), 'no partial tenths — half a tenth brings a whole; a tenth and a half brings two (Mishnah Menachot 12:3)'),
    ('Mishnah Menachot 13:8 — with the price', lambda: libations({'ask': 'with_price'}, DATA), "the libations inside the vow's price — a bull 100 dinars, a calf 5 sela, a ram 2, a lamb 1 (Mishnah Menachot 13:8)"),
    ('Zevachim 111a:7; Kiddushin 37b:1 — from when', lambda: libations({'ask': 'from_when'}, DATA), 'the entry (Zevachim 111a); after inheritance and settlement (R. Yishmael, Kiddushin 37b) — none in the wilderness on both'),
    ('Mishnah Zevachim 14:4-8 — the altar eras', lambda: libations({'ask': 'altar_eras'}, DATA), 'the wilderness / Gilgal / Shiloh / Nov and Gibeon / Jerusalem — forbidden, permitted, forbidden, permitted, forbidden forever (Mishnah Zevachim 14:4-8)'),
    ('Mishnah Zevachim 14:10; Zevachim 111a-b — the private altar', lambda: libations({'ask': 'private_altar'}, DATA), 'no laying of hands, no north, no blood around, no waving; the intents equal (Mishnah Zevachim 14:10)'),
    ('Menachot 45a:21 — Ezekiel\'s ephah', lambda: libations({'ask': 'ezekiel'}, DATA), "the bull's three tenths and the ram's two against Ezekiel 46:7's ephah each (R. Shimon, Menachot 45a)"),
    ('Num 15:3 against Lev 1:2 — or against and (computed)', lambda: libations({'ask': 'or_against_and'}, DATA), '"from the herd OR from the flock" against Lev 1:2\'s AND (computed)'),
    ('Mishnah Menachot 5:3 — the oil (the minchah engine CALLED)', lambda: libations({'ask': 'oil_only'}, DATA), 'oil_only — the libation meal offering: oil, no frankincense (the minchah engine CALLED)'),
    ('Lev 1 — the olah\'s table (the offerings engine CALLED)', lambda: libations({'ask': 'olah_table'}, DATA), 'north; two_that_are_four; flay_and_cut; wholly_to_fires (the offerings engine CALLED)'),
    ('Zevachim 47a:3 — the owner\'s piggul', lambda: libations({'ask': 'owner_piggul'}, DATA), 'the owner can render piggul — "he who sacrifices" (R. Elazar son of R. Yosei); the performer only (the mishna)'),
    # F4 — the stranger
    ('Keritot 8b:18-21; Mishnah Kinnim 1:1 — the convert\'s offering', lambda: stranger({'ask': 'convert_offering'}, DATA), "an olah (a beast) or a bird pair, both olot — as at the covenant's entry (Keritot 8b-9a; Mishnah Kinnim 1:1)"),
    ('Keritot 9a:4 — the entry', lambda: stranger({'ask': 'entry'}, DATA), 'circumcision, immersion, the sprinkling of blood — as your fathers (Rabbi, Keritot 9a:4)'),
    ('Keritot 9a:10 — no Temple', lambda: stranger({'ask': 'no_temple'}, DATA), 'accepted — "throughout your generations" (Rav Acha bar Yaakov)'),
    ('Yevamot 46b:16 — the court', lambda: stranger({'ask': 'court'}, DATA), '3 — "one judgment" (R. Yochanan, Yevamot 46b)'),
    ('Num 15:15-16, 15:29 — the formulas (computed)', lambda: stranger({'ask': 'one_law'}, DATA), 'one statute, one Torah, one judgment — the formulas computed (15:15-16, 15:29)'),
    ('Kiddushin 73a:4 — the congregation', lambda: stranger({'ask': 'congregation'}, DATA), 'converts are congregation (R. Yehuda); not (R. Yosei) — Kiddushin 73a'),
    ('Keritot 9a:2 — a meal offering', lambda: stranger({'ask': 'meal_offering'}, DATA), 'a meal offering does not discharge — the blood sprinkled (Keritot 9a:2)'),
    ('Keritot 9a:10 — the quarter-dinar', lambda: stranger({'ask': 'quarter_dinar'}, DATA), 'a quarter-dinar set aside for the pair — R. Shimon annulled it (Keritot 9a)'),
    # F5 — the challah
    ('Mishnah Challah 1:1; Menachot 70b:2 — the species', lambda: challah({'ask': 'species'}, DATA), '5 — wheat, barley, spelt, oats, rye (Mishnah Challah 1:1; "bread"/"bread", Menachot 70b)'),
    ('Mishnah Challah 1:1 — wheat', lambda: challah({'ask': 'species', 'grain': 'wheat'}, DATA), 'liable — one of the five'),
    ('Mishnah Challah 1:4 — rice', lambda: challah({'ask': 'species', 'grain': 'rice'}, DATA), 'exempt — not of the five (rice, millet, pulse)'),
    ('Sifrei 110:1 — the entry gate (M-23 exemplar 12)', lambda: challah({'ask': 'entry_gate'}, DATA), 'from the entry itself — "upon your coming" varied (Sifrei 110:1; R. Yishmael)'),
    ('Ketubot 25a:11; Niddah 47a:7 — all of you', lambda: challah({'ask': 'all_of_you'}, DATA), 'all of you, not two or three spies — challah today rabbinic (Ketubot 25a; Niddah 47a)'),
    ('Mishnah Challah 2:6; Shabbat 15a:3; Tosefta Eduyot 1:1; Menachot 67a:6 — the minimum', lambda: challah({'ask': 'minimum'}, DATA), 'five quarters of flour — the wilderness omer, a tenth of the ephah (Mishnah Challah 2:6; Shabbat 15a; Tosefta Eduyot 1:1; Exod 16:36)'),
    ('Mishnah Challah 2:7 — the householder', lambda: challah({'ask': 'measure', 'who': 'householder'}, DATA), '1/24'),
    ('Mishnah Challah 2:7 — the baker', lambda: challah({'ask': 'measure', 'who': 'baker'}, DATA), '1/48'),
    ('Mishnah Challah 2:7 — impure unwittingly', lambda: challah({'ask': 'measure', 'who': 'householder', 'impure': 'unwitting'}, DATA), '1/48'),
    ('Mishnah Challah 2:7 — impure intentionally', lambda: challah({'ask': 'measure', 'who': 'baker', 'impure': 'intentional'}, DATA), '1/24'),
    ('Mishnah Challah 1:9; Terumot 4:3 — as the terumah (PAID at 5b: the Korach engine CALLED)', lambda: challah({'ask': 'as_terumah'}, DATA), "the terumah's laws — death and a fifth, the priest's, 101 (Mishnah Challah 1:9); its measure 1/40, 1/50, 1/60 (Terumot 4:3) — PAID: cold_run_korach.the_tithe(terumah_measure) CALLED"),
    ('Menachot 67a:6; Pesachim 38a:3 — the owner', lambda: challah({'ask': 'owner'}, DATA), "yours — not a gentile's, not consecrated (Menachot 67a; Pesachim 38a)"),
    ('Menachot 67a:6 — consecrated dough', lambda: challah({'ask': 'owner', 'owner': 'hekdesh'}, DATA), 'exempt — not your dough'),
    ('Chullin 135b:9 — partners', lambda: challah({'ask': 'partners'}, DATA), 'liable — "your dough" plural (Chullin 135b)'),
    ('Kiddushin 46b:4; Mishnah Challah 2:5 — from flour', lambda: challah({'ask': 'from_flour'}, DATA), "not challah — stolen in the priest's hand (Mishnah Challah 2:5)"),
    ('Mishnah Challah 2:1 — produce brought in', lambda: challah({'ask': 'outside_produce', 'direction': 'in'}, DATA), 'liable — brought into the land (Mishnah Challah 2:1)'),
    ('Mishnah Challah 2:1 — produce taken out', lambda: challah({'ask': 'outside_produce', 'direction': 'out'}, DATA), 'R. Eliezer liable, R. Akiva exempt — taken out (Mishnah Challah 2:1)'),
    ('Mishnah Challah 4:7-8 — the territories', lambda: challah({'ask': 'territories'}, DATA), 'three — to Chezib one; to the river two; beyond two, the measures reversed (Mishnah Challah 4:8)'),
    ('Bekhorot 12b:11 — the sabbatical year', lambda: challah({'ask': 'sabbatical'}, DATA), 'liable — throughout your generations (Bekhorot 12b)'),
    ('Mishnah Challah 3:1-3 — when liable', lambda: challah({'ask': 'when_liable'}, DATA), 'the rolling (wheat) / the solid mass (barley); death by Heaven after (Mishnah Challah 3:1)'),
    ('Mishnah Challah 3:7, 3:10; Zevachim 78a:7 — the mixture', lambda: challah({'ask': 'mixture'}, DATA), 'the taste of grain (Mishnah Challah 3:7, 3:10; Zevachim 78a)'),
    ('Mishnah Challah 2:4, 4:1-3 — the joining', lambda: challah({'ask': 'joining'}, DATA), 'stuck together, one owner, one species; the basket (R. Eliezer) (Mishnah Challah 2:4, 4:1-3)'),
    ('Mishnah Challah 4:2 — species with species', lambda: challah({'ask': 'joining_species'}, DATA), 'wheat with spelt only; barley with all but wheat (Mishnah Challah 4:2)'),
    ('Mishnah Challah 3:5 — a gentile\'s dough', lambda: challah({'ask': 'gentile_dough'}, DATA), "exempt — a gentile's; a gift before the rolling liable (Mishnah Challah 3:5)"),
    ('Mishnah Challah 3:6 — a convert\'s dough', lambda: challah({'ask': 'convert_dough'}, DATA), 'before conversion exempt, after liable, in doubt liable without the fifth (Mishnah Challah 3:6)'),
    ('Mishnah Challah 1:8 — dogs\' dough', lambda: challah({'ask': 'dogs_dough'}, DATA), 'liable if shepherds eat it (Mishnah Challah 1:8)'),
    ('Mishnah Challah 1:6 — the market', lambda: challah({'ask': 'market'}, DATA), 'for the market liable, for oneself exempt — the thanksgiving loaves (Mishnah Challah 1:6)'),
    ('Mishnah Challah 1:3 — liable, not tithed', lambda: challah({'ask': 'liable_not_tithed'}, DATA), "liable to challah, exempt from tithes — gleanings, the forgotten sheaf, peah, ownerless produce, the first tithe, redeemed second tithe, the omer's remainder (Mishnah Challah 1:3)"),
    ('Mishnah Challah 1:4 — the exempt list', lambda: challah({'ask': 'exempt_list'}, DATA), 'exempt from challah — rice, millet, poppy, sesame, pulse, under five quarters, sponge-cakes, honey-cakes, dumplings, a pan-cake, medumma (Mishnah Challah 1:4)'),
    ('Mishnah Challah 4:6 — demai', lambda: challah({'ask': 'demai'}, DATA), 'permitted from clean dough not near (Mishnah Challah 4:6)'),
    ('Mishnah Challah 2:8 — clean for unclean', lambda: challah({'ask': 'clean_for_unclean'}, DATA), 'R. Eliezer permits (the egg bridge); the sages forbid (Mishnah Challah 2:8)'),
    ('Num 15:20-21 — the dough-word (computed)', lambda: challah({'ask': 'dough_word'}, DATA), 'the dough-word four spellings in the Tanakh — two here, Ezekiel 44:30, Nehemiah 10:38 (computed)'),
    # F6 — the error
    ('Horayot 8a:20; Sifrei 111:1 — which sin', lambda: error({'ask': 'which_sin'}, DATA), 'idolatry — "all these commandments" the one equal to all (Horayot 8a:20; Sifrei 111:1)'),
    ('Sifrei 111:1 — the delta (computed)', lambda: error({'ask': 'delta'}, DATA), 'three deltas against Lev 4:13-14 — the congregation for the assembly, a burnt offering for the sin offering, a goat added (computed on the ink)'),
    ('Mishnah Horayot 1:5, 2:6 — the communal (the chatat engine CALLED)', lambda: error({'ask': 'communal'}, DATA), 'bull_and_goat — a bull for a burnt offering and a goat for a sin offering (the chatat engine CALLED)'),
    ('Mishnah Horayot 2:6; Horayot 7b:21 — the individual (the chatat engine CALLED)', lambda: error({'ask': 'individual'}, DATA), 'she_goat — "one soul" (Mishnah Horayot 2:6; the chatat engine CALLED)'),
    ('Mishnah Horayot 2:6 — the anointed (the chatat engine CALLED)', lambda: error({'ask': 'anointed'}, DATA), 'she_goat — "one soul" (Mishnah Horayot 2:6; the chatat engine CALLED)'),
    ('Mishnah Horayot 2:6 — the leader (the chatat engine CALLED)', lambda: error({'ask': 'leader'}, DATA), 'she_goat — "one soul" (Mishnah Horayot 2:6; the chatat engine CALLED)'),
    ('Mishnah Horayot 1:5; Horayot 4b:19 — the tribe table', lambda: error({'ask': 'tribe_table'}, DATA), 'R. Meir a bull and a goat; R. Yehuda twelve; R. Shimon thirteen (Mishnah Horayot 1:5 — the chatat engine carries the arms)'),
    ('Horayot 13a:4; Zevachim 90b:6 — the order (the aleph)', lambda: error({'ask': 'order'}, DATA), 'the bull then the goat — "for a sin offering" without its aleph; "according to the ordinance" (Horayot 13a; Zevachim 90b)'),
    ('Num 15:24 — the aleph (computed)', lambda: error({'ask': 'aleph'}, DATA), 'once in the Bible — the sin offering without the aleph at 15:24 (computed)'),
    ('Zevachim 41a:8 — the goat\'s portions', lambda: error({'ask': 'goat_portions'}, DATA), 'burned like the communal bull\'s — "their sin offering... for their error" (Zevachim 41a)'),
    ('Horayot 2a:19 — the majority\'s manner', lambda: error({'ask': 'majority_manner'}, DATA), 'all unwitting in one manner (Rava, Horayot 2a)'),
    ('Horayot 5a-8a; Taanit 24a:12 — the eyes', lambda: error({'ask': 'eyes'}, DATA), '"from the eyes of the congregation" = the court; the leaders the eyes (Horayot; Taanit 24a)'),
    ('Mishnah Horayot 1:3, 2:2 — the whole essence (the chatat engine CALLED)', lambda: error({'ask': 'partial'}, DATA), 'exempt — the whole essence abolished; a part nullified liable (Mishnah Horayot 1:3)'),
    ('Mishnah Horayot 1:1 — relied on the court (the chatat engine CALLED)', lambda: error({'ask': 'reliance'}, DATA), 'exempt_relied_on_court'),
    ('Mishnah Horayot 1:1 — a judge who knew (the chatat engine CALLED)', lambda: error({'ask': 'reliance', 'knew_error': True}, DATA), 'liable'),
    ('Menachot 74a:7, 109a:20 — the priest\'s own rite', lambda: error({'ask': 'priest_own'}, DATA), 'a priest atones through his own rite (Menachot 74a; 109a)'),
    ('Mishnah Shabbat 7:1; Shabbat 68b-69a — the principle', lambda: error({'ask': 'idolatry_principle'}, DATA), "one sin offering for the forgetter of the principle (Mishnah Shabbat 7:1's analogue); prior knowledge for both (Munbaz)"),
    ('Mishnah Menachot 9:7; Menachot 92a:2 — the laying of hands', lambda: error({'ask': 'semikhah'}, DATA), "the court's bull and the scapegoat; R. Shimon adds the idolatry goat (Mishnah Menachot 9:7)"),
    ('Horayot 8a:14; Keritot 3a:20; Shabbat 69a:1; Yevamot 9a:9 — the class (the chatat engine CALLED)', lambda: error({'ask': 'class'}, DATA), 'karet_no_offering — the whole Torah juxtaposed to idolatry: intentional karet, unwitting sin offering (Horayot 8a:14; Keritot 3a:20)'),
    ('Num 15:26 — the stranger included', lambda: error({'ask': 'stranger_included'}, DATA), 'the stranger forgiven with them (15:26)'),
    ('Num 15:27-29 — in error thrice (computed)', lambda: error({'ask': 'thrice_unwitting'}, DATA), '"in error" thrice at 15:27-29 (computed)'),
    # F7 — the high hand
    ('Horayot 8a:14; Mishnah Keritot 1:2 — intentional (the chatat engine CALLED)', lambda: high_hand({'ask': 'class', 'intent': 'intentional'}, DATA), 'karet_no_offering'),
    ('Mishnah Keritot 1:2 — unwitting (the chatat engine CALLED)', lambda: high_hand({'ask': 'class', 'intent': 'unwitting'}, DATA), 'sin_offering'),
    ('Mishnah Keritot 1:2; Keritot 2a:5, 7b:1 — the blasphemer\'s offering', lambda: high_hand({'ask': 'blasphemer_offering'}, DATA), 'none — no act (the Rabbis, Mishnah Keritot 1:2); an offering (R. Akiva, Keritot 7b)'),
    ('Keritot 7b:4-6; Pesachim 93b:1 — the blasphemer\'s identity', lambda: high_hand({'ask': 'blasphemer_identity'}, DATA), 'the curser of the Name (the Rabbis); the idolater (R. Elazar ben Azarya)'),
    ('Num 15:30 — blasphemes once (computed)', lambda: high_hand({'ask': 'blasphemes_once'}, DATA), 'once in the Bible — blasphemes (computed)'),
    ('Sanhedrin 99a:17, 99b:4 — the despiser', lambda: high_hand({'ask': 'despiser'}, DATA), 'who says the Torah is not from Heaven; the Epicurean (Sanhedrin 99a); Manasseh the exemplar (99b)'),
    ('Sanhedrin 64b:21-22, 90b:18 — the doubled infinitive (the fork)', lambda: high_hand({'ask': 'karet_reading'}, DATA), 'R. Akiva: this world and the next; R. Yishmael: the language of men (Sanhedrin 64b; 90b) — the fork'),
    ('Shevuot 13a:2; Pirkei Avot 3:11 — the yoke', lambda: high_hand({'ask': 'yoke'}, DATA), 'throws off the yoke / uncovers faces in the Torah; the covenant of circumcision; before and after Yom Kippur (Shevuot 13a; Pirkei Avot 3:11)'),
    ('Sanhedrin 90b:16; Yoma 36b:5; Keritot 25b:16 — his iniquity in him', lambda: high_hand({'ask': 'iniquity_in_him'}, DATA), 'after death — the World-to-Come alluded (Sanhedrin 90b); intentional sins (Yoma 36b)'),
    ('Mishnah Keritot 1:1 — the thirty-six (the chatat engine CALLED)', lambda: high_hand({'ask': 'census'}, DATA), '36 — the karet cases (Mishnah Keritot 1:1; the chatat engine CALLED)'),
    ('Exod 14:8; Num 33:3; Onkelos 15:30 — the posture', lambda: high_hand({'ask': 'high_hand_posture'}, DATA), 'the exodus\'s posture — "with a high hand" (Exod 14:8; Num 33:3)'),
    ('Berakhot 24b:20 — the filthy place', lambda: high_hand({'ask': 'filthy_place'}, DATA), 'reciting in a filthy place — despised (Rav Adda bar Ahava)'),
    ('Shabbat 153b:13 — his own body', lambda: high_hand({'ask': 'own_body'}, DATA), "liable only for an act with his own body — the Sabbath's application (Shabbat 153b)"),
]


if __name__ == '__main__':
    ok = 0
    for name, run, want in CASES:
        v, e, pr = run()
        hit = v == want
        ok += hit
        print('  %s  %s\n        -> %s  %s' % ('PASS' if hit else 'MISS', name, v, e))
        if not hit:
            print('        expected: %s' % want)
    print('\nSHELACH: %d/%d cells; the scene %s; the narrative %s' % (ok, len(CASES), SCENE, NARRATIVE))
    sys.exit(0 if ok == len(CASES) else 1)

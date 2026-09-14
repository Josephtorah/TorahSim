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
print('guard: %d expectations checked, every one a literal from the answer sheet [honest-pairing guard satisfied]' % GUARDED)
import sqlite3, sys, io, re, contextlib
from fractions import Fraction
import effects_layer as FX
import world_engine as WE
import cold_run_bamidbar as BM                   # THE EDGE: shelach -> bamidbar CALL, reference (14:29's census set)
import cold_run_chatat as CH                     # THE EDGE: shelach -> chatat CALL, reference (15:24-31's idolatry column, the court, the karet class)
import cold_run_offerings as OF                  # THE EDGE: shelach -> offerings CALL, reference (15:3, 15:8, 15:24's burnt offering)
import cold_run_minchah as MN                    # THE EDGE: shelach -> minchah CALL, reference (15:4's libation meal offering)

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
    q = "SELECT COUNT(*) FROM words w JOIN verses v ON w.verse_id=v.id WHERE w.he_plain=?" if False else None
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
TRIBE_LINES = [v for v in range(4, 16) if verse_text(13, v).split()[0] == 'למטה']
SPY_TRIBES = [verse_text(13, v).split()[1] for v in TRIBE_LINES]
assert len(TRIBE_LINES) == 12 and 'לוי' not in SPY_TRIBES and SPY_TRIBES[7] == 'יוסף', (TRIBE_LINES, SPY_TRIBES)   # twelve lines, Levi absent, Joseph's name over Manasseh (13:11)
QUESTIONS = [w for v in (18, 19, 20) for w in verse_text(13, v).split() if w in ('החזק', 'הרפה', 'המעט', 'הטובה', 'הבמחנים', 'השמנה', 'היש')]
assert len(QUESTIONS) == 7, QUESTIONS                                                                # the seven interrogatives (sitting 4's count)
_ORDER = [('Exod', c, v) for c in range(1, 41) for v in range(1, 60)] + [('Lev', c, v) for c in range(1, 28) for v in range(1, 60)] + [('Num', c, v) for c in range(1, 37) for v in range(1, 90)]
JOSHUA_BEFORE = [(b, c, v) for (b, c, v) in _ORDER if (b, c, v) < ('Num', 13, 16) and db.execute("SELECT 1 FROM verses WHERE book=? AND chapter=? AND verse=?", (b, c, v)).fetchone() and 'יהושע' in verse_text(c, v, b).split()]
assert len(JOSHUA_BEFORE) == 8 and 'הושע' in verse_text(44, 32 if False else 44, 'Deut').split() if False else len(JOSHUA_BEFORE) == 8, JOSHUA_BEFORE   # the new name at eight seats before the verse that gives it
assert 'הושע' in verse_text(32, 44, 'Deut').split(), verse_text(32, 44, 'Deut')                      # the old name again at the Torah's last song
E34 = verse_text(34, 6, 'Exod').split() + verse_text(34, 7, 'Exod').split(); N18 = verse_text(14, 18).split()
def subsequence(a, b):
    i = 0
    for w in b:
        if i < len(a) and a[i] == w: i += 1
    return i == len(a)
assert subsequence(N18, E34) and len(E34) - len(N18) == 11, (len(E34), len(N18))                   # the attributes ABRIDGED by pure deletion: eleven words dropped, none added (sitting 4)
THIS_WILDERNESS = [v for v in range(1, 46) if 'במדבר הזה' in verse_text(14, v)]
assert THIS_WILDERNESS == [2, 29, 32, 35], THIS_WILDERNESS                                          # measure for measure stated by the ink: 14:2 returned at 14:29, 14:32, 14:35
IN_ERROR = sum(verse_text(15, v).split().count('בשגגה') for v in (27, 28, 29))
ONCE = {tok: count_token(tok) for tok in ('לחטת', 'מגדף', 'סלחתי')}
assert IN_ERROR == 3 and ONCE == {'לחטת': 1, 'מגדף': 1, 'סלחתי': 1}, (IN_ERROR, ONCE)                # 'in error' thrice fenced; the aleph dropped once; 'blasphemes' once; 'I have pardoned' once
DOUGH = sorted({strip(he) for (he,) in db.execute("SELECT w.he FROM words w") if 'ערס' in strip(he)})
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

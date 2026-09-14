#!/usr/bin/env python3
# NUM 28:1-29:39 — THE OFFERINGS CALENDAR: THE MUSAFIM (THE NUMBERS WALK sitting 9b, 2026-09-11; World/step9/NUMBERS_WALK.md "Sitting 9b";
# the name the tradition's own word for the offering BESIDES the continual — Mishnah Menachot 4:4, Shekalim 4:1; the collision guard bars
# "offerings_calendar" beside cold_run_offerings and cold_run_calendar). ONE speech, 28:1 to 29:39 (the register's one verb), read as ONE
# TABLE: the tamid restated from Exodus 29 with its deltas (by CALL to the incense-shekel engine's fourteen tamid cells); the Sabbath's two
# lambs; the new moon's table two-one-seven with THE MASTER ROW of tenths and hin-fractions (by CALL to the Shelach engine's table, READ never
# re-declared) cited by pointer eight times; Pesach's seven days "as these"; the day of firstfruits with Numbers' set [2, 1, 7] against
# Leviticus 23:18's [7, 1, 2] (R. Akiva's two orders — the parser's); Tishri's stack on the first, the tenth's afflictions, the atonements'
# goat beside the inner one (by CALL to the Yoma engine's routing table); Sukkot's declining bulls thirteen to seven = seventy with the
# watches' division a function of the table, the water libation's three letters as a CHECKED ROW with its four sources a parameter, the
# eighth day's head without the conjunction; the closer "these you shall make in your appointed times, besides your vows" — and the
# THIRTEEN GOATS with their vav census (Shevuot 9b-10a's token fact computed off the ink). The daemon law_musafim sets EIGHT PERIOD TIMERS
# on the altar at the command's verse (the Calendar's keys by CALL to the moadim engine's dates) and READS the tamid's open debt, never
# rewriting it. Seven cells + the watches; every token probed (zero-report law); effects on every cell (the effects law); the parameters
# the ink leaves open recorded in DATA with their arms. Reading ledgers: logic/oral_triage/num_28_daily_shabbat_rosh_2026-09-11.md,
# num_28_pesach_shavuot_2026-09-11.md, num_29_fall_festivals_2026-09-11.md; the exam's docket: num_28_29_musafim_exam_2026-09-11.md.

# ---- THE HONEST-PAIRING GUARD ----------------------------------------------------------------------------
import os as _os, sys as _sys
_sys.path.insert(0, _os.path.dirname(_os.path.abspath(__file__)))
from compile_guards import check_honest_pairing as _chp
_P = _os.path.abspath(__file__)
GUARDED = _chp(_P, 'CASES', 2)
assert GUARDED == 110, ('the guard counted %d expectations, the tripwire holds 110' % GUARDED)   # the guard's own count on the first run (typed 118 from the design's estimate, read 110 off the guard's print)
print('guard: %d expectations checked, every one a literal from the answer sheet [honest-pairing guard satisfied]' % GUARDED)
import sqlite3, sys, io, re, contextlib, collections
from fractions import Fraction
import effects_layer as FX
import world_engine as WE
import cold_run_incense_shekel as IS             # THE EDGE: musafim -> incense_shekel CALL, reference (28:3-8 restates Exod 29:38-42; the tamid's fourteen cells; the Sabbath token homes law_sabbath there)
import cold_run_shelach as SH                    # THE EDGE: musafim -> shelach CALL, reference (28:12-14 restates 15:4-10 — the master row READ)
import cold_run_moadim as MO                     # THE EDGE: musafim -> moadim CALL, reference (Leviticus 23 at its second seat — the dates, the labor class, the omer, the two sets)
import cold_run_offerings as OFF                 # THE EDGE: musafim -> offerings CALL, reference (the burnt offerings' and sin offerings' rite)
import cold_run_yoma as YO                       # THE EDGE: musafim -> yoma CALL, reference (29:11 'besides the sin offering of the atonements' — the routing table)
import cold_run_minchah as MIN                   # THE EDGE: musafim -> minchah CALL, reference (28:26's new meal offering; the oil's grade; the salt)

HERE = _os.path.dirname(_os.path.abspath(__file__))
# ONE copy of the numeral parser: the sequence runner's INK block executed here (the stitcher's way — no import edge)
_SRC = open(_os.path.join(HERE, 'cold_run_sequence.py'), encoding='utf-8').read()
_INK = {'re': re, 'sqlite3': sqlite3, 'os': _os, 'WE': WE}
exec(_SRC.split('# ==== INK BEGIN')[1].split('# ==== INK END ====')[0].split('\n', 1)[1], _INK)
ink_numbers, verse_words = _INK['ink_numbers'], _INK['verse_words']

db = sqlite3.connect('<repo-old>/elijah_docket/tanakh.sqlite')

def strip(s):
    return ''.join(c for c in s if c != '/' and not (0x0591 <= ord(c) <= 0x05C7))

def verse_text(ch, vs, book='Num'):
    rows = db.execute("""SELECT w.he FROM words w JOIN verses v ON w.verse_id=v.id WHERE v.book=?
        AND v.chapter=? AND v.verse=? ORDER BY w.idx""", (book, ch, vs)).fetchall()
    return ' '.join(strip(h) for (h,) in rows)

def words(ch, vs, book='Num'):
    return verse_text(ch, vs, book).split()

# ---- zero-report probes: the span's load-bearing tokens (every one measured on the DB before it was typed) ----------------
PROBES = [
    ('וידבר',   28, 1,  'and He spoke — the register\'s ONE verb (30:1 the closer)'),
    ('צו',      28, 2,  'command — the imperative of the standing statute'),
    ('קרבני',   28, 2,  'My offering — the possessive'),
    ('לחמי',    28, 2,  'My bread — the altar\'s table'),
    ('במועדו',  28, 2,  'in its appointed time — the freed term (Pesachim 66a)'),
    ('תמימם',   28, 3,  'without blemish — added to Exod 29:38'),
    ('שנים',    28, 3,  'two [a day]'),
    ('תמיד',    28, 3,  'continual'),
    ('השני',    28, 4,  'the second [lamb]'),
    ('הערבים',  28, 4,  'the evenings — between them'),
    ('כתית',    28, 5,  'beaten [oil]'),
    ('העשיה',   28, 6,  'made — at Mount Sinai'),
    ('סיני',    28, 6,  'Sinai'),
    ('שכר',     28, 7,  'strong drink — the libation\'s word'),
    ('הסך',     28, 7,  'pour — the libation-root, R. Nathan\'s first'),
    ('נסך',     28, 7,  'a libation — the libation-root, R. Nathan\'s second'),
    ('כמנחת',   28, 8,  'as the meal offering of [the morning] — the pointer (Exod 29:41\'s)'),
    ('השבת',    28, 9,  'the Sabbath'),
    ('בשבתו',   28, 10, 'on its Sabbath'),
    ('התמיד',   28, 10, 'the continual — the first of fifteen'),
    ('חדשיכם',  28, 11, 'your new moons'),
    ('שבעה',    28, 11, 'seven [lambs]'),
    ('בחדשו',   28, 14, 'in its month'),
    ('לחטאת',   28, 15, 'for a sin offering — the only one with "to the LORD"'),
    ('ליהוה',   28, 15, 'to the LORD — the new moon\'s goat alone'),
    ('פסח',     28, 16, 'Passover'),
    ('מצות',    28, 17, 'unleavened bread'),
    ('עבדה',    28, 18, 'servile [work]'),
    ('ושבעה',   28, 19, 'and seven — the bare "one" before it (rule 25)'),
    ('מלבד',    28, 23, 'besides — the first of twelve'),
    ('כאלה',    28, 24, 'as these'),
    ('הבכורים', 28, 26, 'the firstfruits'),
    ('חדשה',    28, 26, 'new [meal offering]'),
    ('בשבעתיכם', 28, 26, 'in your weeks'),
    ('שעיר',    28, 30, 'a goat — WITHOUT the conjunction (Shevuot 10a:11)'),
    ('תרועה',   29, 1,  'blowing — a day of teruah'),
    ('כמשפטם',  29, 6,  'according to their ordinance — ben Beteira\'s third letter'),
    ('ובעשור',  29, 7,  'and on the tenth — the plene noun (rule 26); typed without its vav on the first run, read off the DB'),
    ('ועניתם',  29, 7,  'and you shall afflict'),
    ('הכפרים',  29, 11, 'the atonements — the inner goat named'),
    ('וחגתם',   29, 12, 'and you shall keep a feast'),
    ('עשר',     29, 13, 'ten — thirteen bulls, fourteen lambs'),
    ('ועשרון',  29, 15, 'and a tenth — the dotted tenth (Menachot 87b:5)'),
    ('במספרם',  29, 18, 'by their number'),
    ('כמשפט',   29, 18, 'according to the ordinance — the first of six'),
    ('ונסכיהם', 29, 19, 'and their libations — the mem'),
    ('עשתי',    29, 20, 'eleven — the eleven bulls'),
    ('ונסכיה',  29, 31, 'and its libations — the yod'),
    ('ביום',    29, 35, 'on the [eighth] day — WITHOUT the conjunction (Sukkah 47a:9)'),
    ('עצרת',    29, 35, 'an assembly'),
    ('אלה',     29, 39, 'these — the closer'),
    ('במועדיכם', 29, 39, 'in your appointed times'),
    ('לבד',     29, 39, 'besides — the closer\'s form'),
    ('ולשלמיכם', 29, 39, 'and your peace offerings'),
]
for tok, ch, vs, note in PROBES:
    if tok not in words(ch, vs):
        sys.exit('ZERO-REPORT LAW: probe %r (%s) failed at Num %d:%d — refusing to run' % (tok, note, ch, vs))
print('probes: all %d token probes fired  [zero-report law satisfied]\n' % len(PROBES))

P = []  # the provenance trail of the case being run
def ink(ref, note):  P.append(('INK',  'Num %s — %s' % (ref, note)))
def move(src, note): P.append(('MOVE', '%s — %s' % (src, note)))
def dat(note):       P.append(('DATA', note))
def hyp(note):       P.append(('HYP',  note))     # THE LINK REVIEW LAW: a hypothesis — no teacher; counted apart, never as compiled

def out(verdict, effects):
    """verdict + registry-validated effects (the engine contract)"""
    FX.validate([e for e in effects if e != FX.NONE])
    return verdict, effects, list(P)

# ---- THE NUMBERS, computed from the ink by the engine's parser (live; the probes' expectations are the ink's) ----
def N(ch, vs, book='Num'): return ink_numbers(verse_words(book, ch, vs))
T_MONTH, T_PESACH, T_SHAVUOT = N(28, 11), N(28, 19), N(28, 27)             # the new moon's, Pesach's, the firstfruits day's animals
T_RH, T_YK, T_EIGHTH = N(29, 2), N(29, 8), N(29, 36)                        # Tishri's three [1, 1, 7]
SUKKOT_VERSES = (13, 17, 20, 23, 26, 29, 32)
SUKKOT = [N(29, v) for v in SUKKOT_VERSES]                                   # the seven days [bulls, rams, lambs]
LEV_SET = N(23, 18, 'Lev')                                                   # Leviticus 23:18's [7, 1, 2]
TAMID_TWO, SAB_TWO = N(28, 3), N(28, 9)
assert T_MONTH == T_PESACH == T_SHAVUOT == [2, 1, 7] and T_RH == T_YK == T_EIGHTH == [1, 1, 7], (T_MONTH, T_PESACH, T_SHAVUOT, T_RH, T_YK, T_EIGHTH)
assert [s[0] for s in SUKKOT] == [13, 12, 11, 10, 9, 8, 7] and all(s[1:] == [2, 14] for s in SUKKOT), SUKKOT
assert LEV_SET == [7, 1, 2] and TAMID_TWO == [2] and SAB_TWO == [2, 2], (LEV_SET, TAMID_TWO, SAB_TWO)
BULLS_70 = sum(s[0] for s in SUKKOT); RAMS_14 = sum(s[1] for s in SUKKOT); LAMBS_98 = sum(s[2] for s in SUKKOT)
MONTH_ROW = N(28, 14)                                                        # the hin-fractions [1/2, 1/3, 1/4]
TENTHS_12 = N(28, 12)                                                        # [3, 2]
DATE_PESACH, DATE_MATZOT, DATE_RH, DATE_YK, DATE_SUKKOT = N(28, 16), N(28, 17), N(29, 1), N(29, 7), N(29, 12)
assert DATE_PESACH == [14] and DATE_MATZOT == [15, 7] and DATE_RH == [1] and DATE_YK == [10] and DATE_SUKKOT == [15, 7], (DATE_PESACH, DATE_MATZOT, DATE_RH, DATE_YK, DATE_SUKKOT)   # the month-ORDINALS ('the first', 'the seventh') are ink_ordinals', not cardinals — the diff's own [10] at 29:7
# THE TOKEN CENSUSES of the span (computed; the reading's counts the expectations)
SPAN = [(28, v) for v in range(1, 32)] + [(29, v) for v in range(1, 40)]
def seats(tok, exact=True):
    return [(c, v) for c, v in SPAN if (tok in words(c, v) if exact else any(w.endswith(tok) or w == tok for w in words(c, v)))]
BESIDES = seats('מלבד'); ORDINANCE = seats('כמשפט'); THEIR_ORDINANCE = seats('כמשפטם'); BY_NUMBER = seats('במספרם'); CONTINUAL = seats('התמיד')
BLEMISH = seats('תמימם'); TO_LORD = seats('ליהוה'); THEIR_LIB = seats('ונסכיהם'); ITS_LIB_F = seats('ונסכיה'); TO_ATONE = seats('לכפר'); THESE = seats('אלה')
assert (len(BESIDES), len(ORDINANCE), len(THEIR_ORDINANCE), len(BY_NUMBER), len(CONTINUAL), len(BLEMISH), len(TO_LORD), len(THEIR_LIB), len(ITS_LIB_F), len(TO_ATONE), len(THESE)) == (12, 6, 2, 7, 15, 15, 19, 11, 1, 3, 2), \
    (len(BESIDES), len(ORDINANCE), len(THEIR_ORDINANCE), len(BY_NUMBER), len(CONTINUAL), len(BLEMISH), len(TO_LORD), len(THEIR_LIB), len(ITS_LIB_F), len(TO_ATONE), len(THESE))
# THE GOAT LINES and their VAV (Shevuot 9b:2, 10a:8, 10a:11 — the token fact): every verse with the goat-word, the conjunction read off the word's first letter
GOATS = [(c, v, w) for c, v in SPAN for w in words(c, v) if w in ('שעיר', 'ושעיר')]
GOAT_VAV = [(c, v) for c, v, w in GOATS if w == 'ושעיר']; GOAT_BARE = [(c, v) for c, v, w in GOATS if w == 'שעיר']
assert len(GOATS) == 13 and GOAT_BARE == [(28, 30), (29, 11)], (len(GOATS), GOAT_BARE)
GOAT_TO_LORD = [(c, v) for c, v in SPAN if 'לחטאת' in words(c, v) and 'ליהוה' in words(c, v)]
assert GOAT_TO_LORD == [(28, 15)], GOAT_TO_LORD
# THE EIGHTH'S HEAD (Sukkah 47a:9): 29:35 'on the eighth day' against 29:17-32 'AND on the second day'
HEADS = [(v, words(29, v)[0]) for v in (17, 20, 23, 26, 29, 32, 35)]
assert [h for _, h in HEADS] == ['וביום'] * 6 + ['ביום'], HEADS
# THE WATER LIBATION'S THREE LETTERS (M-28; Taanit 2b:14; Shabbat 103b:12): the mem of 29:19, the yod of 29:31, the mem of 29:33 — against the pointer line's plain forms
LETTERS = (words(29, 19)[-1], words(29, 31)[-1], words(29, 33)[-1]); PLAIN = (words(29, 16)[-1], words(29, 22)[-1], words(29, 18)[-1])
assert LETTERS == ('ונסכיהם', 'ונסכיה', 'כמשפטם') and PLAIN == ('ונסכה', 'ונסכה', 'כמשפט'), (LETTERS, PLAIN)
MAYIM_RAW = LETTERS[0][-1] + LETTERS[1][-2] + LETTERS[2][-1]                 # the three surplus letters as WRITTEN: the final mem of 29:19, the yod of 29:31, the final mem of 29:33
assert MAYIM_RAW == 'םים', MAYIM_RAW                                          # the first run took the last letter of every word and read a he — the yod is the penultimate; a miss read off the print
MAYIM = MAYIM_RAW.replace('ם', 'מ', 1)                                       # THE SCRIBAL LICENSE (Shabbat 103b:12, 103b:16 — Rav Chisda: a closed letter rendered open is valid): the closed mem read open — "water"
assert MAYIM == 'מים', MAYIM
# BEN AZZAI'S CENSUS (Sifrei 143:2; Menachot 110a): the Name at every offering — the special Name against the other names, this span and Leviticus 1-7
def name_census(chapters, book):
    yh, oth = 0, []
    for ch, n in chapters:
        for v in range(1, n + 1):
            for w in words(ch, v, book):
                if w in ('יהוה', 'ליהוה'): yh += 1
                if w in ('אלהים', 'אלהיך', 'אלהיכם', 'אלהיו', 'שדי', 'צבאות', 'לאלהים'): oth.append((ch, v, w))
    return yh, oth
NAMES_SPAN = name_census(((28, 31), (29, 39)), 'Num'); NAMES_LEV = name_census(((1, 17), (2, 16), (3, 17), (4, 35), (5, 26), (6, 23), (7, 38)), 'Lev')
# the first run typed zero for Leviticus 1-7 and read TWO seats off the print: 2:13 'the salt of the covenant of YOUR GOD' (the covenant's, not an offering's addressee)
# and 4:22 'the commandments of the LORD HIS GOD' (the ruler's sin — the Name with its apposition): ben Azzai's dictum is about the offering's ADDRESSEE ('to the LORD'), the census says so
assert NAMES_SPAN[1] == [] and [(c, v) for c, v, _ in NAMES_LEV[1]] == [(2, 13), (4, 22)] and NAMES_SPAN[0] >= 19, (NAMES_SPAN, NAMES_LEV)
ADDRESSEE_OTHER = [(c, v, w) for c, v, w in NAMES_LEV[1] if w.startswith('ל')]   # an offering 'to God' — none: every 'to' is 'to the LORD'
assert ADDRESSEE_OTHER == [], ADDRESSEE_OTHER
# THE POINTERS of the span, computed: 'as the meal offering of the morning' (28:8), 'according to the ordinance' x6, 'according to their ordinance' x2 — all INTERNAL (the master row 28:12-14; the tamid 28:5)
POINTERS = [(28, 8, 'כמנחת')] + [(c, v, 'כמשפט') for c, v in ORDINANCE] + [(c, v, 'כמשפטם') for c, v in THEIR_ORDINANCE]
assert len(POINTERS) == 9, POINTERS

# ---- THE CALLEES (live import edges; the design's cells by name) ----
TAMID = {q: IS.tamid(q)['v'] for q in ('two_lambs', 'plural_minimum', 'ordinals', 'clocks', 'measures', 'beaten_oil', 'three_log', 'pointer', 'olat_tamid', 'sabbath_overrides', 'sheet_4_4', 'sheet_shekalim_4_1', 'doubled_morning_order', 'initiations')}
assert TAMID['plural_minimum'] == 2 and TAMID['three_log'] == 3 and TAMID['sabbath_overrides'] == words(28, 10)[:6] and 'Num 28:8' in TAMID['pointer'] and 'Num 28:6' in TAMID['olat_tamid'], TAMID
SH_TABLE, SH_LOGS, SH_RATIO, SH_MONTH_ROW, SH_61 = SH.TABLE, SH.LOGS, SH.RATIO, SH.MONTH_ROW, SH.SUKKOT_SABBATH   # THE CALL: the master row READ, never re-declared
assert SH_MONTH_ROW == MONTH_ROW and SH_61 == 61 and SH_LOGS == {'lamb': (3, 3), 'ram': (4, 4), 'bull': (6, 6)}, (SH_MONTH_ROW, MONTH_ROW, SH_61, SH_LOGS)
SH_TABLE_CELL = SH.libations({'ask': 'table'}, SH.DATA)[0]; SH_SEATS = SH.libations({'ask': 'table_seats'}, SH.DATA)[0]; SH_SUKSAB = SH.libations({'ask': 'sukkot_sabbath'}, SH.DATA)[0]
SH_TAKES_GOAT = SH.libations({'ask': 'takes', 'offering': 'chatat'}, SH.DATA)[0]; SH_HIN = SH.DATA['hin_in_logs']['value']
MO_PASS, MO_RH, MO_YK, MO_SUK, MO_SHAV, MO_LOAVES, MO_OMER = MO.passover(), MO.rosh_hashanah(), MO.yom_kippur(), MO.sukkot(), MO.shavuot_animals(), MO.two_loaves(), MO.omer()   # THE CALL
MO_WORK = {d: MO.work_class(d)['v'] for d in ('sabbath', 'passover_1', 'passover_7', 'atzeret', 'rosh_hashanah', 'yom_kippur', 'sukkot_1', 'shemini')}
assert MO_PASS['date']['v'] == '14th_of_1st' and MO_RH['date']['v'] == '1st_of_7th' and MO_RH['sound']['v'] == 'teruah' and MO_SUK['eighth']['v'] == 'atzeret' and MO_SHAV['two_sets']['v'] == 'for_the_bread_not_for_the_day' and MO_OMER['count_length']['v'] == 49, 'the moadim engine moved'
assert MO_WORK['sabbath'] == 'all_work' and MO_WORK['passover_1'] == 'servile_only' and MO_WORK['yom_kippur'] == 'all_work', MO_WORK
OLAH_HERD, OLAH_FLOCK, CHATAT_OUT, SHELAMIM = OFF.dispatch('olah:herd'), OFF.dispatch('olah:flock'), OFF.dispatch('outer_chatat'), OFF.dispatch('shelamim')   # THE CALL
ROUTE_NONE, ROUTE_END, ORDER = YO.route(), YO.route(known_end=True), YO.service_order()                                       # THE CALL
assert ROUTE_NONE['agent'] == 'festival_and_new_moon_goats' and ROUTE_END['agent'] == 'outer_goat_and_day' and len(ORDER) == 18, (ROUTE_NONE['agent'], ROUTE_END['agent'], len(ORDER))
OMER_SRC, OIL_GRADE, SALT = MIN.omer('source')['v'], MIN.oil_grade()['v'], MIN.salt('meal_offering')['v']                     # THE CALL
assert OMER_SRC == 'new_and_from_the_land' and TAMID['beaten_oil'] == OIL_GRADE and SALT == 'required', (OMER_SRC, OIL_GRADE, SALT)
# THE TABLES the daemon sets as the timers' values: (bulls, rams, lambs, goats) per Calendar key — read off the parser's lists
TABLES = {'sabbath': (0, 0, SAB_TWO[0], 0), 'month': tuple(T_MONTH) + (1,), 'passover_1': tuple(T_PESACH) + (1,), 'atzeret': tuple(T_SHAVUOT) + (1,),
          'rosh_hashanah': tuple(T_RH) + (1,), 'yom_kippur': tuple(T_YK) + (1,), 'sukkot_1': tuple(SUKKOT[0]) + (1,), 'shemini': tuple(T_EIGHTH) + (1,)}
# THE STACKS: Tishri's first (Arakhin 13a:10) and Shavuot on a Sabbath (Menachot 49b:5)
LAMBS_TISHRI_1 = TAMID_TWO[0] + T_RH[2] + T_MONTH[2]
LAMBS_THREE_DAYS = 3 * TAMID_TWO[0] + SAB_TWO[0] + T_RH[2] + T_MONTH[2]                # Menachot 49b:5's own composition: Shabbat and the two days of Rosh Hashanah — three days' temidim, the Sabbath's musaf, Rosh Hashanah's, the new moon's (the first run typed a 'Shavuot on a Sabbath' stack from memory = 20 and read the page)
assert LAMBS_TISHRI_1 == 16 and LAMBS_THREE_DAYS == 22, (LAMBS_TISHRI_1, LAMBS_THREE_DAYS)
# THE WATCHES' DIVISION (Mishnah Sukkah 5:6; Sukkah 55b:1-8): day d — (14 - d) + 2 + 1 offerings to as many watches; the fourteen sheep to the rest
WATCHES = 24
def watches_day(d):
    bulls, rams, goat = SUKKOT[d - 1][0], SUKKOT[d - 1][1], 1
    big = bulls + rams + goat; rest = WATCHES - big
    two = SUKKOT[d - 1][2] - rest                                                # watches with two sheep: 14 - rest
    one = rest - two
    assert 2 * two + one == SUKKOT[d - 1][2], (d, two, one)
    return big, rest, two, one
WD = [watches_day(d) for d in range(1, 8)]
assert WD[0] == (16, 8, 6, 2) and WD[1] == (15, 9, 5, 4) and WD[6] == (10, 14, 0, 14), WD
SEVENTY_SPLIT = (BULLS_70 // WATCHES, BULLS_70 % WATCHES)                        # 70 = 24 x 2 + 22: twenty-two watches thrice, two twice (55b:8)
assert SEVENTY_SPLIT == (2, 22)


# ===== THE DATA CHANNEL — the parameter rows the ink leaves open (motion 2's recorded settings) =========
DATA = {
    'water_libation_source': {'value': 'received', 'settings': {
        'received': "A HALAKHAH TO MOSES FROM SINAI (a received rule) — R. Yehoshua / R. Nechunya of Beit Chortan: the ten saplings, the willow, the water libation (Taanit 3a:6-7; Sukkah 34a:2, 44a:5; Zevachim 110b:6)",
        'ben_beteira_letters': "the three surplus letters mem, yod, mem of 29:19, 29:31, 29:33 = water (Sifrei 150:1; Taanit 2b:14; licensed by Rav Chisda's 'a closed letter rendered open is valid', Shabbat 103b:12/16)",
        'akiva_induction': "R. Akiva: the water on Sukkot from the seasons — 'that the year's rains be blessed' (Sifrei 150:1; Rosh Hashanah 16a:15)",
        'nathan_doubled_verb': "R. Nathan: 'pour a libation' (28:7) — the libation-root twice with varied prefixes: one of water, one of wine (Sifrei 143:2; Taanit 3a:2)"},
        'source': "the ink writes no water: 29:19, 29:31, 29:33 carry three letters the pointer line's plain forms lack (computed above); 28:7's root twice"},
    'water_libation_days': {'value': 7, 'settings': {7: "the mishna (Sukkah 42b): all seven days — the received arm's count", 1: "R. Yehoshua's letters alone would give one day (Taanit 3a:3)", 2: "R. Akiva's induction two (the sixth and seventh)", 6: "ben Beteira's letters six (from the second)", 8: "R. Yehuda: eight days, the eighth's included (Sukkah 48b)"},
                            'source': "Taanit 3a:3-5 — the day-counts each source yields, computed by the Gemara"},
    'water_libation_measure': {'value': 'three_log', 'settings': {'three_log': "Mishnah Sukkah 4:9 — a gold flask of three log", 'one_log': "R. Yehuda: one log all eight days (Sukkah 48b)", 'no_measure': "the ink's own silence"}, 'source': "no measure in the ink"},
    'rain_mention_day': {'value': 'eighth_last_prayer_leader', 'settings': {'eighth_last_prayer_leader': "R. Yehuda in R. Yehoshua's name (Taanit 2b:9)", 'second': "ben Beteira", 'sixth': "R. Akiva", 'first_from_the_lulav': "R. Eliezer (Taanit 2b:3-6)"}, 'source': "the prayer's calendar hung on the water libation's day"},
    'hin_vessel': {'value': 'twelve_log_by_zeh', 'settings': {'twelve_log_by_zeh': "the hin twelve log — 'THIS shall be for Me' (Exod 30:24-25) by numerical value (Menachot 89a:16); R. Elazar b. Azarya: the log measures a halakhah to Moses from Sinai (a received rule, 89a:7)", 'elazar_marks': "R. Elazar b. R. Tzadok: marks on the hin vessel for the bull, the ram, the lamb (Mishnah Menachot 9:2)", 'shimon_log_and_a_half': "R. Shimon: no hin, a log and a half measures the tamid's oil (Mishnah Menachot 9:2)"},
                   'source': "28:14 'half a hin, a third, a quarter' — the hin's size the shelf's (SH.DATA hin_in_logs by CALL = %s)" % SH_HIN},
    'morning_missed': {'value': 'offer_the_twilight_barred_priests', 'settings': {'offer_the_twilight_barred_priests': "Mishnah Menachot 4:4: the morning lamb not offered — the twilight one offered; R. Shimon: those priests who withheld are barred from the twilight's, others offer (Menachot 50a:2-4)"}, 'source': "28:4 'the one lamb in the morning and the second between the evenings' — no fallback in the ink; IS.tamid('sheet_4_4') by CALL = %s" % TAMID['sheet_4_4']},
    'ben_azzai_corners': {'value': 'NW_morning_NE_evening', 'settings': {'NW_morning_NE_evening': "Mishnah Tamid 4:1: the morning lamb at the northwest corner's second ring, the evening's at the northeast — opposite the sun (Yoma 62b:14)", 'sifrei_NE_SW': "the Sifrei 142:3's Hebrew row: northeast and southwest (the reading's defect row)"}, 'source': "28:4 names the times, not the corners"},
    'goats_atonement_tiers': {'value': 'yehuda_one_job', 'settings': {'yehuda_one_job': "R. Yehuda: the festivals' and new moons' goats atone for the Temple's defiling unknown at both ends (Mishnah Shevuot 1:4; the vav juxtaposes them — Shevuot 9b:2)", 'shimon_three_tiers': "R. Shimon: new moons — the pure eater of impure food (Lev 10:17 with the frontplate, Shevuot 9b:6); festivals — unknown at both ends; Yom Kippur's outer goat — known at the end (2b:3)", 'meir_flat': "R. Meir: all the musafim's goats one atonement, the inner goat excepted (2b:2; 10a:8, 10a:14)", 'shimon_cumulative': "R. Shimon b. Yehuda in R. Shimon's name: each tier includes the ones below (2b:5-6)"},
                              'source': "28:15 'to the LORD' at the new moon alone; 28:22, 28:30, 29:5 'to atone'; nine bare — three grammatical tiers, the jobs the shelf's"},
    'availability': {'value': 'ezekiel_ladder', 'settings': {'ezekiel_ladder': "Ezek 46:6-7's altered table read as the fallback: two bulls not found — one; seven lambs not found — six... down to one (Menachot 45a:6-8); R. Shimon: a lamb with its libations rather than seven without (45a:21-45b:1)", 'ink_literal': "28:11's two bulls, one ram, seven lambs as written — no fallback in the ink"}, 'source': "Chanina b. Chizkiya's reconciliation charter for Ezekiel (Menachot 45a:19)"},
    'vow_deadline': {'value': 'three_festivals_any_order', 'settings': {'three_festivals_any_order': "the first tanna: three festivals in any order (Beitzah 19b:9; Rosh Hashanah 4b)", 'three_in_order': "R. Shimon: Pesach, Shavuot, Sukkot in their order — 'the festival of Sukkot' written to make it last (19b:10, 19b:12)", 'by_sukkot': "R. Elazar b. R. Shimon: by Sukkot whenever vowed (19b:13)", 'one_festival': "R. Meir: one festival (Rosh Hashanah 4b)"}, 'source': "29:39 'besides your vows and your freewill offerings' — the vows named at the calendar's close; 'you shall not delay' (Deut 23:22) the clock"},
    'atzeret_stay': {'value': 'lodging_required', 'settings': {'lodging_required': "the overnight stay after the festival — Pesach's 'you shall turn in the morning' (Deut 16:7) carried to Sukkot by Deut 16:16's analogy (Chagigah 17a:9, 17b:1); the Sifrei 151:1's 'withheld' on 29:35"}, 'source': "29:35 'an assembly' — the word's sense open"},
    'eighth_day_status': {'value': 'own_festival_for_six_marks', 'settings': {'own_festival_for_six_marks': "a festival of its own for PZR KShB — the lottery, the time-blessing, the festival's name, the offering, the song, the blessing (Sukkah 48a:1; Rav Pappa's one bull, 47a:8); for the redress it is Sukkot's (Rosh Hashanah 4b:13; Chagigah 17a:7; Mishnah Chagigah 1:6)"}, 'source': "29:35-36: the head without the conjunction, the table [1, 1, 7] not [6, 2, 14]"},
    'sinai_olah': {'value': 'tamid_by_beit_hillel', 'settings': {'tamid_by_beit_hillel': "Beit Hillel, R. Akiva, R. Yosei HaGelili: the burnt offering of Exod 24:5 was the DAILY offering — 'never ceased' (Chagigah 6a:15-16, 6b:4)", 'appearance_olah': "Beit Shammai, R. Elazar: an appearance olah; R. Elazar on 28:6 — 'its details said at Sinai, itself not offered until the Tabernacle stood' (6b:3) — the tape's own timer (the tamid's debt opened at Exod 40:29) his arm"},
                   'source': "28:6 'the continual burnt offering MADE at Mount Sinai' — made = offered, or prescribed"},
    'tamid_surplus': {'value': 'redeemed_by_stipulation', 'settings': {'redeemed_by_stipulation': "the Rabbis (R. Yochanan by Ulla): the fiscal year's unneeded tamid lambs redeemed unblemished — the court's tacit stipulation (Shevuot 10b:7, 11a:8, 11b:11)", 'supplement_the_altar': "R. Shimon: not redeemed — offered as the altar's supplement, its 'dessert' (Shevuot 12a:7, 12b:1)"}, 'source': "28:3 fixes two a day; the stock the shelf's (Mishnah Arakhin 2:5 — six inspected lambs, three days' temidim)"},
    'teruah_count': {'value': 'two_torah_one_rabbinic', 'settings': {'two_torah_one_rabbinic': "Lev 23:24 and Lev 25:9 by the Torah, 29:1 'for its own statement' — the third terua rabbinic (Rosh Hashanah 34a:10)", 'one_torah_two_rabbinic': "R. Shmuel b. Nachmani in R. Yonatan's name: Lev 25:9 alone by the Torah (34a:11)"}, 'source': "29:1 'a day of teruah' — the count of blasts not in the ink"},
    'shofar_source': {'value': 'jubilee_seventh_month', 'settings': {'jubilee_seventh_month': "Lev 25:9's 'in the seventh month' — the Jubilee's shofar carried to Rosh Hashanah (Rosh Hashanah 33b:11-12; Sifra Section 11 6 — MO.rosh_hashanah('instrument') by CALL = %s)" % MO_RH['instrument']['v'], 'covered_moon': "Ps 81:4 'at the covered moon for our feast day' — the one festival at a new moon: a shofar and nothing else (34a:19)", 'wilderness_trumpets': "the Beha runner's 'terua'/'terua' (Num 10:5-7) — the shape, not the instrument (34a:8, 34a:18)"},
                      'source': "29:1 names the sound ('a day of teruah'), not the horn; Onkelos 'a day of wailing' (33b:10)"},
    'loaves_and_lambs': {'value': 'bread_blocks_lambs', 'settings': {'bread_blocks_lambs': "R. Akiva (Mishnah Menachot 4:3; MO.shavuot_animals('interdependence') by CALL = %s)" % MO_SHAV['interdependence']['v'], 'lambs_block_bread': "ben Nannas; R. Shimon rules as he for another reason (Menachot 45b:3-7)"}, 'source': "Lev 23:18 'with the bread' — Numbers' set silent on the loaves"},
    'shavuot_redress_days': {'value': 7, 'settings': {7: "R. Elazar in R. Oshaya's name: Shavuot likened to Pesach by Deut 16:16 — seven (Chagigah 17a:5; Menachot 65b); 'the count's unit is the sanctification's span' — a week (Rosh Hashanah 5a:4; Chagigah 17b:7-8)"}, 'source': "28:26's one day; the redress the shelf's"},
    'yom_kippur_rams': {'value': 'one_ram_two_seats', 'settings': {'one_ram_two_seats': "Rebbi: one ram — Lev 16:5's and 29:8's the same (Yoma 3a:4, 70b:9)", 'two_rams': "R. Elazar b. R. Shimon: two — the people's ram of Lev 16 and the musaf's (Yoma 3a:4)"}, 'source': "29:8 'one ram' beside Lev 16:5 'one ram for a burnt offering'"},
    'tamid_afternoon_hour': {'value': 'eight_and_a_half', 'settings': {'eight_and_a_half': "Mishnah Pesachim 5:1: slaughtered at eight and a half, offered at nine and a half", 'seven_and_a_half': "the eve of Pesach", 'six_and_a_half': "the eve of Pesach on a Friday (Pesachim 58a)"}, 'source': "28:4 'between the evenings' — the hour the shelf's (IS.tamid('clocks') by CALL = %s)" % TAMID['clocks']},
    'musaf_hour': {'value': 'all_day', 'settings': {'all_day': "the Rabbis: the additional prayer all day (Mishnah Berakhot 4:1 at 26a:12) — the offering's window the ground", 'seven_hours': "R. Yehuda: until seven hours"}, 'source': "no hour for the musaf in the ink; the tamid's 'between the evenings' the day's close"},
    'food_work_extension': {'value': 'since_permitted_for_food', 'settings': {'since_permitted_for_food': "Beit Hillel: since carrying out was permitted for food it was permitted not for food (Beitzah 12a:4)", 'food_only': "Beit Shammai: for food alone"}, 'source': "28:18 'no servile work' (MO.work_class('passover_1') by CALL = %s) — the class's edge the shelf's" % MO_WORK['passover_1']},
    'communal_consecration': {'value': 'genus_by_consecration_species_by_the_knife', 'settings': {'genus_by_consecration_species_by_the_knife': "Rav Yehuda in Shmuel's name: communal offerings' consecration fixes only the genus, the slaughter the species (Shevuot 12b:3); R. Shimon concedes the goats' interchange ring — festival, new moon, Yom Kippur, festival (12b:4)"}, 'source': "the tables' animals drawn from one stock; the ink names no consecration"},
    'lamb_stock_floor': {'value': 6, 'settings': {6: "Mishnah Arakhin 2:5: no fewer than six inspected lambs in the Chamber of the Lambs — three days' temidim (Arakhin 13a:11), the 'Shabbat and two festival days' a mnemonic"}, 'source': "28:3 two a day; the floor the shelf's"},
}


# ===== F1: THE TAMID (Num 28:1-8) ============================================================================
def the_tamid(case, data):
    del P[:]
    ask = case['ask']
    if ask == 'frame':
        ink('28:1-2', '"and the LORD spoke to Moses, saying: command the children of Israel and say to them" — the register\'s ONE verb for seventy verses; 30:1 the closer; "command" the imperative of a standing statute (Sifrei 142:1: for the generations)')
        return out('one speech, 28:1-29:39 — a standing statute commanded', ['commanded'])
    if ask == 'possessives':
        ink('28:2', '"MY offering, MY bread for MY fire offerings, MY pleasing odor" — four possessives; the altar\'s table (Beitzah 20b:8 "your Master\'s table")')
        move('Sifrei 142:2', 'My offering — the blood; My bread — the limbs; My fire offerings — the fistfuls; My pleasing odor — the bowls (the reading\'s row)')
        return out('four possessives — the altar\'s bread', ['accepted'])
    if ask == 'appointed_time':
        ink('28:2', '"you shall keep to bring near to Me IN ITS APPOINTED TIME" — the freed term at three seats (9:2, 9:3 the Pesach; 28:2 the tamid)')
        move('Pesachim 66a:3-12 (Hillel; the Sifrei 142:3\'s identity)', '"its appointed time" at the Pesach and "its appointed time" at the tamid — even on the Sabbath, even in impurity: the verbal analogy the link review law\'s own seat')
        move('Pesachim 81b:3 (Rava)', 'the identity\'s second yield: the impurity of the deep permitted for the tamid as for the Pesach')
        return out('in its appointed time — even the Sabbath, even impurity (the Pesach\'s analogy)', ['tamid_owed'])
    if ask == 'two_per_day':
        ink('28:3', '"yearling lambs without blemish, TWO a day, a continual burnt offering" — %s by the parser; "without blemish" ADDED to Exod 29:38' % TAMID_TWO)
        move('CALLED cold_run_incense_shekel.tamid(two_lambs) -> %s; (plural_minimum) -> %s [IMPORT, live]' % (TAMID['two_lambs'], TAMID['plural_minimum']), 'the tamid\'s own engine: the phrase at Exod 29:38 alone, the plural\'s minimum two (Yoma 62b:11-12)')
        dat('the row ben_azzai_corners = %s' % data['ben_azzai_corners']['value'])
        return out('two a day — Exod 29:38 restated with "without blemish" added', ['tamid_owed'])
    if ask == 'the_one_lamb':
        ink('28:4', '"THE one lamb you shall make in the morning, and THE SECOND lamb you shall make between the evenings" — the article on "the lamb" (Exod 29:39 "the ONE lamb")')
        move('CALLED cold_run_incense_shekel.tamid(ordinals) -> %s; (clocks) -> %s [IMPORT, live]' % (TAMID['ordinals'], TAMID['clocks']), 'Menachot 50a:6 — the second and not the first between the evenings; the tamid and the incense share the clock')
        dat('the row tamid_afternoon_hour = %s' % data['tamid_afternoon_hour']['value'])
        return out('the one in the morning, the second between the evenings', ['tamid_owed'])
    if ask == 'the_tenth':
        ink('28:5', '"a tenth of the ephah of fine flour for a meal offering, mingled with BEATEN oil, a quarter of the hin" — Onkelos three seahs; "beaten" at Exod 29:40 and here (I3)')
        move('CALLED cold_run_incense_shekel.tamid(measures) -> %s; (three_log) -> %s; (beaten_oil) -> %s; cold_run_minchah.oil_grade() -> %s; salt(meal_offering) -> %s [IMPORT, live]' % (TAMID['measures'], TAMID['three_log'], TAMID['beaten_oil'], OIL_GRADE, SALT), 'the quarter-hin is three log (the hin twelve); pure beaten not required for meal offerings (Menachot 86b); the salt of Lev 2:13')
        return out('a tenth with a quarter-hin of beaten oil — three log; salted', ['libation_owed'])
    if ask == 'made_at_sinai':
        ink('28:6', '"a continual burnt offering, MADE at Mount Sinai, for a pleasing odor" — the one-word participle; "a continual burnt offering" at Exod 29:42, here and Ezra 3:5 (computed by the callee)')
        move('CALLED cold_run_incense_shekel.tamid(olat_tamid) -> %s [IMPORT, live]' % TAMID['olat_tamid'], 'the phrase\'s three seats — the return\'s altar resuming it')
        move('Chagigah 6a:15-16, 6b:3-4', 'Beit Hillel: the Sinai olah WAS the tamid (R. Akiva: never ceased; Amos 5:25 answered by Levi\'s funds); R. Elazar: its details at Sinai, itself first at the Tabernacle — the tape\'s own timer (the debt opened at Exod 40:29) his arm')
        dat('the row sinai_olah = %s' % data['sinai_olah']['value'])
        return out('made at Sinai — the tamid by one house, its prescription by the other', ['accepted'])
    if ask == 'strong_drink':
        ink('28:7', '"and its libation a quarter of the hin for the one lamb; in the holy place POUR A LIBATION of STRONG DRINK to the LORD" — the libation-root twice (%s, %s); "strong drink" for Exod 29:40\'s "wine"' % (words(28, 7)[6], words(28, 7)[7]))
        move('Sukkah 49b:5 (Rav Pappa)', 'shekhar — an expression of drinking, satiation, intoxication: the space between the ramp and the altar filled with wine (the reading\'s row)')
        move('Menachot 87a:7', 'wine of the second year — valid after the fact (Rebbi); the parameter wine_age')
        move('Sifrei 143:2 (R. Nathan); Taanit 3a:2', 'the doubled root with varied prefixes: one of water, one of wine — the water libation\'s third source')
        return out('strong drink — wine that intoxicates; the doubled root R. Nathan\'s water', ['libation_owed'])
    if ask == 'the_second_lamb':
        ink('28:8', '"and the second lamb you shall make between the evenings; AS THE MEAL OFFERING OF THE MORNING and as its libation you shall make" — the pointer to 28:5-7 (INTERNAL); Exod 29:41 the same pointer')
        move('CALLED cold_run_incense_shekel.tamid(pointer) -> %s; (sheet_4_4) -> %s [IMPORT, live]' % (TAMID['pointer'], TAMID['sheet_4_4']), 'the LIKE_OFFERING form at two seats; Mishnah Menachot 4:4 — the tamids and the additionals do not hold each other up')
        return out('as the morning\'s — the pointer internal; the second not held up by the first', ['tamid_owed'])
    if ask == 'the_name':
        ink('28:3-8', '"to the LORD" %d times in the span, the special Name at every offering; the other names %s (computed); Leviticus 1-7: the Name %d, the other names %s — the covenant\'s "your God" (2:13) and the apposition "the LORD his God" (4:22), no offering addressed "to God" (%s)' % (NAMES_SPAN[0], NAMES_SPAN[1], NAMES_LEV[0], NAMES_LEV[1], ADDRESSEE_OTHER))
        move('Sifrei 143:2 (ben Azzai); Menachot 110a', '"come and see: in all the offerings of the Torah not God, not your God, not Shaddai, not Hosts — the special Name alone": the census computed on the ink — the addressee always the Name')
        return out('the special Name the addressee of every offering — no offering to God (computed)', ['accepted'])
    if ask == 'tamid_read':
        ink('28:1-8', 'the tamid RESTATED — Exod 29:38-42 with its deltas ("without blemish", "made at Mount Sinai", "strong drink", "in the holy place"); the debt on the altar since the erection')
        move('CALLED cold_run_incense_shekel.tamid(initiations) -> %s; (sheet_shekalim_4_1) -> %s [IMPORT, live]' % (TAMID['initiations']['olah_altar'], TAMID['sheet_shekalim_4_1']), 'the olah altar initiated at Exod 40:29 — the tape\'s tamid_owed opened there; bought from the terumah')
        return out('the tamid read from the erection\'s debt — never rewritten here', ['accepted'])
    if ask == 'morning_missed':
        move('Mishnah Menachot 4:4; Menachot 50a:2-4', 'the morning lamb not offered — offer the twilight one; the priests who withheld barred (R. Shimon), others offer')
        dat('the row morning_missed = %s' % data['morning_missed']['value'])
        return out('the twilight lamb offered; the withholding priests barred', ['disqualified'])
    if ask == 'impurity_of_the_deep':
        move('Pesachim 80b:5; 81a:14-15; 81b:3', 'a concealed grave under the priest — the frontplate appeases for the Pesach (the answer sheet); the tamid by "its appointed time" (Rava) or by Rabba\'s a fortiori from the communal override')
        return out('the deep\'s impurity permitted for the tamid — the Pesach\'s analogy', ['accepted'])
    if ask == 'surplus_lambs':
        move('Shevuot 10b:7, 11a:8, 11b:11, 12a:7', 'the fiscal year\'s unneeded lambs: redeemed unblemished by the court\'s stipulation (the Rabbis) / the altar\'s supplement (R. Shimon)')
        dat('the row tamid_surplus = %s' % data['tamid_surplus']['value'])
        return out('redeemed unblemished — the court\'s tacit stipulation', ['exempt'])
    if ask == 'lamb_stock':
        move('Mishnah Arakhin 2:5; Arakhin 13a:9-11', 'six inspected lambs — three days\' temidim (2 x 3), the "Shabbat and two festival days" a mnemonic; one day of Rosh Hashanah alone needs sixteen')
        dat('the row lamb_stock_floor = %s; the tamid\'s two by the parser %s' % (data['lamb_stock_floor']['value'], TAMID_TWO))
        return out('six lambs — three days of the tamid', ['tamid_owed'])
    if ask == 'sinai_olah':
        move('Chagigah 6a:16 (Abaye\'s census)', 'Beit Hillel, R. Akiva, R. Yosei HaGelili — the tamid; Beit Shammai, R. Elazar — an appearance olah; R. Yishmael deleted from the list (6b:11)')
        dat('the row sinai_olah = %s' % data['sinai_olah']['value'])
        return out('the Sinai olah the tamid — Beit Hillel\'s list', ['accepted'])
    return out('no verdict in span', [FX.NONE])


# ===== F2: THE SABBATH (Num 28:9-10) ==========================================================================
def the_sabbath(case, data):
    del P[:]
    ask = case['ask']
    if ask == 'two_lambs':
        ink('28:9', '"and on the Sabbath day TWO yearling lambs without blemish, and TWO tenths of fine flour" — %s by the parser: the Sabbath\'s first offering in the Torah; the table (0, 0, 2, 0)' % SAB_TWO)
        return out('two lambs and two tenths — the Sabbath\'s first offering', ['musaf_owed'])
    if ask == 'on_its_sabbath':
        ink('28:10', '"the burnt offering of the Sabbath ON ITS SABBATH, beside the continual burnt offering and its libation" — the phrase a hapax; the timer\'s period the week')
        move('Sifrei 144:1', '"on its Sabbath" — not the Sabbath\'s offering on another Sabbath: the musaf lapses with its day (Berakhot 26a:17 "its day passed, its sacrifice is invalid")')
        return out('on its Sabbath — the debt lapses with the day', ['musaf_owed'])
    if ask == 'overrides':
        ink('28:10', '"beside the continual burnt offering" — the tamid written FOR THE SABBATH by name: %s' % TAMID['sabbath_overrides'])
        move('CALLED cold_run_incense_shekel.tamid(sabbath_overrides) -> %s [IMPORT, live]' % TAMID['sabbath_overrides'], 'the fixed-time offerings override the Sabbath (Shabbat 132b:1\'s premise; Pesachim 66a\'s Hillel)')
        return out('the tamid on the Sabbath by name — the override the verse\'s own', ['labor_barred'])
    if ask == 'between_the_temidim':
        move('Mishnah Tamid 7:3 (credited); Mishnah Zevachim 10:1', 'the musaf between the morning tamid and the twilight\'s — the frequent precedes; the song of the Sabbath')
        dat('the row musaf_hour = %s' % data['musaf_hour']['value'])
        return out('between the temidim — the frequent first', ['rest_required'])
    if ask == 'licensed_slaughter':
        move('Mishnah Beitzah 2:4 (19a:11); Beitzah 20b:4', 'Beit Shammai: no burnt offering on a festival "apart from the daily and additional offerings of the day"; Beit Hillel\'s a fortiori FROM the Sabbath\'s musaf — where the commoner\'s slaughter is barred the Most High\'s is permitted')
        return out('the temidim and musafim the festival\'s licensed slaughter — both houses', ['accepted'])
    if ask == 'hillel_two_hundred':
        move('Pesachim 66a:3', 'Hillel to the sons of Beteira: "have we but one Pesach a year that overrides the Sabbath? MORE THAN TWO HUNDRED" — the year\'s Sabbath offerings: 52 x (2 tamid + 2 musaf) = %d lambs, the tables\' own arithmetic' % (52 * (TAMID_TWO[0] + SAB_TWO[0])))
        return out('more than two hundred a year — computable from the tables', ['accepted'])
    if ask == 'work_class':
        move('CALLED cold_run_moadim.work_class(sabbath) -> %s [IMPORT, live]' % MO_WORK['sabbath'], 'the Sabbath\'s class all work — the moadim engine\'s; the Sabbath token of 28:9 homes the pre-Sinai span, the tabernacle\'s clause law_sabbath in the incense-shekel file')
        return out('all work barred — the moadim engine\'s class by call', ['exempt'])
    return out('no verdict in span', [FX.NONE])


# ===== F3: THE NEW MOON (Num 28:11-15) ========================================================================
def the_new_moon(case, data):
    del P[:]
    ask = case['ask']
    if ask == 'the_table':
        ink('28:11', '"and at the heads of your months you shall bring near a burnt offering to the LORD: two young bulls, one ram, seven yearling lambs without blemish" — %s by the parser; the goat at 28:15' % T_MONTH)
        return out('two bulls, one ram, seven lambs — the table [2, 1, 7]', ['musaf_owed'])
    if ask == 'master_row':
        ink('28:12-14', '"three tenths for the bull, two tenths for the ram, a tenth for the lamb; their libations half a hin for the bull, a third for the ram, a quarter for the lamb" — %s and %s by the parser: 15:4-10 RESTATED, the row every pointer cites' % (TENTHS_12, [str(x) for x in MONTH_ROW]))
        move('CALLED cold_run_shelach.TABLE = %s; LOGS = %s; MONTH_ROW = %s; libations(table) -> %s [IMPORT, live] — the row READ, never re-declared' % ({k: tuple(str(x) for x in v) for k, v in SH_TABLE.items()}, SH_LOGS, [str(x) for x in SH_MONTH_ROW], SH_TABLE_CELL), 'the Shelach engine\'s table at its second seat')
        dat('the row hin_vessel = %s' % data['hin_vessel']['value'])
        return out('the master row = 15:4-10 by call — lamb 1/10 + 1/4, ram 2/10 + 1/3, bull 3/10 + 1/2', ['musaf_owed'])
    if ask == 'in_its_month':
        ink('28:14', '"this is the burnt offering of the month IN ITS MONTH for the months of the year" — the period the month; the new moon\'s only register in the Torah')
        move('Sifrei 145:2', '"in its month" — not this month\'s on another (the Sabbath\'s form); the reading\'s row')
        return out('in its month — the timer keyed to the month', ['sanctify_day'])
    if ask == 'the_goat_to_the_lord':
        ink('28:15', '"and one goat of the goats for a sin offering TO THE LORD" — the only goat so named (computed: %s of thirteen); "to the LORD" %d seats in the span' % (GOAT_TO_LORD, len(TO_LORD)))
        move('Shevuot 9a:7-9 (Reish Lakish); Sifrei 145:3', '"an atonement for My diminishing the moon" AND "a sin the LORD alone knows" — both from the one preposition; the scope by the fixed-time analogy to Yom Kippur\'s goat (9a:10)')
        move('CALLED cold_run_yoma.route() -> %s [IMPORT, live]' % ROUTE_NONE['agent'], 'no knowledge at either end — the festival and new-moon goats (the recorded three-way dispute)')
        dat('the row goats_atonement_tiers = %s' % data['goats_atonement_tiers']['value'])
        return out('to the LORD — the sin the LORD alone knows; the routing table\'s festival-and-new-moon agent', ['atoned_forgiven'])
    if ask == 'absent_from_lev23':
        ink('28:11-15 against Lev 23', 'the new moon has NO seat in Leviticus 23\'s appointed times — the offerings calendar\'s own day')
        move('Shevuot 10a:13 (Abaye)', 'the new moon called a "festival" — Tammuz of thirty days (Lam 1:15; the Shelach runner\'s tammuz_length)')
        return out('the new moon absent from Leviticus 23 — this calendar\'s own day', ['accepted'])
    if ask == 'availability':
        move('Menachot 45a:6-8 (Ezek 46:6-7)', '"a young bull" against two, "six lambs" against seven, "as his means suffice" — the ladder: two not found, one; seven not found, six... to one')
        dat('the row availability = %s' % data['availability']['value'])
        return out('the ladder from Ezekiel — fewer when not found', ['accepted'])
    if ask == 'month_sanctified':
        move('Rosh Hashanah 5a:4; Chagigah 17b:7 (Rabba b. Shmuel)', 'count thirty days and SANCTIFY THE MONTH WITH OFFERINGS — the count\'s unit is the sanctification\'s span: the month a day, Shavuot a week')
        return out('the month sanctified by its offerings — one day', ['sanctify_day'])
    if ask == 'labor_permitted':
        ink('28:11-15', 'no rest token, no convocation at the new moon (the register\'s own count)')
        move('Chagigah 18a:6', 'the new moon has a musaf and labor is permitted — the a fortiori\'s refutation; the musaf a sanctity marker, not the ban')
        return out('a musaf without a ban — labor permitted', ['exempt'])
    return out('no verdict in span', [FX.NONE])


# ===== F4: PESACH AND THE DAY OF FIRSTFRUITS (Num 28:16-31) ====================================================
def pesach_shavuot(case, data):
    del P[:]
    ask = case['ask']
    if ask == 'the_dates':
        ink('28:16-17', '"in the first month, on the fourteenth day of the month, a Passover to the LORD; and on the fifteenth day a feast, seven days unleavened bread" — %s, %s by the parser' % (DATE_PESACH, DATE_MATZOT))
        move('CALLED cold_run_moadim.passover() -> date %s, matzot_days %s [IMPORT, live]' % (MO_PASS['date']['v'], MO_PASS['matzot_days']['v']), 'Leviticus 23:5-6 at its second seat; the Passover\'s procedure through the moadim engine (PS by its call)')
        return out('the fourteenth and the fifteenth — Leviticus 23 by call', ['musaf_owed'])
    if ask == 'food_work':
        ink('28:18, 28:25, 28:26', '"a holy convocation; no SERVILE work" — three seats')
        move('CALLED cold_run_moadim.work_class(passover_1) -> %s [IMPORT, live]' % MO_WORK['passover_1'], 'the lighter class — food work permitted')
        move('Beitzah 12a:4', 'Beit Hillel: since permitted for food, permitted not for food; Beit Shammai: food alone')
        dat('the row food_work_extension = %s' % data['food_work_extension']['value'])
        return out('servile work barred — the lighter class; food work permitted', ['labor_barred'])
    if ask == 'the_table':
        ink('28:19', '"two young bulls, one ram, and seven yearling lambs" — %s by the parser (rule 25: the bare "one" before "and seven" under the pause)' % T_PESACH)
        return out('two bulls, one ram, seven lambs — the new moon\'s table', ['musaf_owed'])
    if ask == 'as_these':
        ink('28:23-24', '"besides the burnt offering of the morning which is for the continual burnt offering you shall make THESE; AS THESE you shall make daily seven days" — "these" %d seats, "as these" one' % len(THESE))
        move('Sifrei 147:2', '"as these" — the seven days alike, no decline (Sukkot\'s the contrast)')
        return out('as these daily seven days — one table seven times', ['musaf_owed'])
    if ask == 'the_seventh':
        ink('28:25', '"and on the seventh day a holy convocation" — the ordinal; MO.work_class(passover_7) -> %s' % MO_WORK['passover_7'])
        return out('the seventh a convocation — the same class', ['labor_barred'])
    if ask == 'firstfruits_day':
        ink('28:26', '"and on the DAY OF THE FIRSTFRUITS, when you bring near a NEW meal offering to the LORD, in your weeks" — the day named by its offering; Onkelos ATZERET')
        move('CALLED cold_run_moadim.omer() -> count %s, morrow %s; two_loaves() -> %s loaves of %s; cold_run_minchah.omer(source) -> %s [IMPORT, live]' % (MO_OMER['count_length']['v'], MO_OMER['morrow_reading']['v'], MO_LOAVES['count']['v'], MO_LOAVES['flour']['v'], OMER_SRC), 'the fiftieth day; the new meal offering the two loaves; the omer the minchah engine\'s')
        return out('the day of firstfruits — the fiftieth, the two loaves the new meal offering', ['commanded'])
    if ask == 'the_second_set':
        ink('28:27 against Lev 23:18', '"two young bulls, one ram, seven yearling lambs" %s against Leviticus\'s "seven lambs, one bull, two rams" %s — the numbers AND the order differ (the parser at both seats)' % (T_SHAVUOT, LEV_SET))
        move('CALLED cold_run_moadim.shavuot_animals() -> olah_kinds %s, two_sets %s [IMPORT, live]' % (MO_SHAV['olah_kinds']['v'], MO_SHAV['two_sets']['v']), 'the Sifra: those for the day, these for the bread')
        move('Menachot 45b:10, 45b:13 (R. Akiva)', 'ONE bull and TWO rams against TWO bulls and ONE ram; Leviticus writes sheep, bull, rams — Numbers bulls, ram, sheep: two sets')
        return out('two sets — [2, 1, 7] for the day, [7, 1, 2] for the bread', ['musaf_owed'])
    if ask == 'wilderness_set':
        move('Menachot 45b:6, 45b:11 (R. Shimon)', 'NUMBERS\' set ran in the wilderness, Leviticus\'s not until the land (R. Tarfon 45b:9: "with the bread" — the land)')
        return out('Numbers\' set in the wilderness — the tape\'s own claim', ['accepted'])
    if ask == 'libations_likened':
        ink('28:28-29, 28:31', '"their meal offering... three tenths for the bull, two for the ram, a tenth for the lamb" — the master row restated; "besides the continual burnt offering and its meal offering you shall make, without blemish, and their libations"')
        move('Sifrei 148:2', '"without blemish shall they be to you, and their libations" — the libations likened to the animals: unblemished wine (Menachot 87a)')
        return out('the libations likened — unblemished as the animals', ['disqualified'])
    if ask == 'loaves_and_lambs':
        move('Mishnah Menachot 4:3; Menachot 45b:3-7', 'the loaves block the lambs (R. Akiva) / the lambs the loaves (ben Nannas)')
        dat('the row loaves_and_lambs = %s' % data['loaves_and_lambs']['value'])
        return out('the bread blocks the lambs — R. Akiva', ['accepted'])
    if ask == 'redress_days':
        move('Chagigah 17a:5 (R. Elazar in R. Oshaya\'s name); Rosh Hashanah 4b:15', 'Shavuot likened to Pesach by Deut 16:16 — seven days of redress; "grasped many, grasped nothing"')
        dat('the row shavuot_redress_days = %s' % data['shavuot_redress_days']['value'])
        return out('seven days of redress — Pesach\'s analogy', ['commanded'])
    if ask == 'day_of_slaughter':
        move('Mishnah Chagigah 2:4 (17a:3-4)', 'Shavuot on a Friday: Beit Shammai the day of slaughter after Shabbat; the High Priest not in festive garments — against the Sadducees')
        return out('a day of slaughter after Shabbat — the festival\'s one-day tail', ['exempt'])
    if ask == 'loaves_baking':
        move('Beitzah 20b:11', 'the two loaves an obligation of the day, yet their baking overrides neither Shabbat nor the festival — "what need not be done on the festival is not done on it"')
        return out('the loaves baked before the day — no override', ['labor_barred'])
    if ask == 'availability_libations':
        move('Menachot 45a:21-45b:1 (R. Shimon)', 'a lamb with its libations rather than seven without — the libations\' priority on the ladder')
        return out('one with its libations before seven without', ['accepted'])
    return out('no verdict in span', [FX.NONE])


# ===== F5: TISHRI — THE DAY OF BLOWING AND THE TENTH (Num 29:1-11) ==========================================
def tishri(case, data):
    del P[:]
    ask = case['ask']
    if ask == 'day_of_blowing':
        ink('29:1', '"in the seventh month, on the first of the month... A DAY OF TERUAH shall it be to you" — %s by the parser; the sound named, not the horn' % DATE_RH)
        move('CALLED cold_run_moadim.rosh_hashanah() -> date %s, sound %s, instrument %s [IMPORT, live]' % (MO_RH['date']['v'], MO_RH['sound']['v'], MO_RH['instrument']['v']), 'Leviticus 23:24 at its second seat')
        move('Rosh Hashanah 33b:10 (Abaye)', '"and we TRANSLATE it: a day of yevava (wailing)" — Onkelos cited by name on this verse')
        dat('the row shofar_source = %s' % data['shofar_source']['value'])
        return out('a day of teruah — the sound the verse\'s, the shofar the Jubilee\'s', ['musaf_owed'])
    if ask == 'teruah_count':
        move('Rosh Hashanah 34a:10-11', 'three teruot — Lev 23:24 and 25:9 by the Torah, 29:1 "for its own statement" (the analogy\'s peg); R. Yonatan one')
        dat('the row teruah_count = %s' % data['teruah_count']['value'])
        return out('29:1 comes for its own statement — the third terua rabbinic', ['accepted'])
    if ask == 'by_day':
        ink('29:1', '"a DAY of teruah" — the word day')
        move('Rosh Hashanah 34a:12', 'by day and not at night — the blowing\'s slot from the verse\'s own word')
        return out('by day, not at night', ['rest_required'])
    if ask == 'the_tishri_table':
        ink('29:2', '"one young bull, one ram, seven yearling lambs" — %s by the parser; the goat at 29:5' % T_RH)
        return out('one bull, one ram, seven lambs — the table [1, 1, 7]', ['musaf_owed'])
    if ask == 'the_stack':
        ink('29:6', '"BESIDES the burnt offering of the month and its meal offering, and the continual burnt offering and its meal offering and their libations ACCORDING TO THEIR ORDINANCE" — three offerings stacked on one day: the tamid, the new moon\'s, the day\'s')
        move('Arakhin 13a:10', 'one day of Rosh Hashanah needs SIXTEEN lambs — %d + %d + %d = %d (computed)' % (TAMID_TWO[0], T_RH[2], T_MONTH[2], LAMBS_TISHRI_1))
        return out('the stack — sixteen lambs on the first of Tishri', ['musaf_owed'])
    if ask == 'the_tenth':
        ink('29:7', '"on THE TENTH of this seventh month a holy convocation; you shall AFFLICT your souls; NO WORK" — %s by the parser (rule 26: the plene noun); all work, not servile' % DATE_YK)
        move('CALLED cold_run_moadim.yom_kippur() -> affliction %s, list %s; work_class(yom_kippur) -> %s [IMPORT, live]' % (MO_YK['affliction']['v'], MO_YK['affliction_list']['v'], MO_WORK['yom_kippur']), 'Leviticus 23:27-32 at its second seat')
        move('Yoma 76a:11 (Rav Chisda)', 'the five afflictions from the five mentions — 29:7 among them')
        return out('the tenth — afflict, all work barred; the five afflictions', ['labor_barred'])
    if ask == 'atonements_goat':
        ink('29:11', '"one goat of the goats a sin offering, BESIDES THE SIN OFFERING OF THE ATONEMENTS" — the inner goat named beside the musaf\'s outer one; "the atonements" at Exod 30:10 and here alone; the goat-word WITHOUT the conjunction here (computed)')
        move('CALLED cold_run_yoma.route(known_end=True) -> %s; service_order() -> %d steps [IMPORT, live]' % (ROUTE_END['agent'], len(ORDER)), 'the outer goat and the day — knowledge at the end alone (Mishnah Shevuot 1:3); the Day\'s order the Yoma engine\'s')
        move('Shevuot 10a:21', '"once" written of the inner goat — the bridge to the outer is THIS clause')
        return out('the outer goat beside the inner — the routing table\'s outer-goat-and-day', ['atoned_forgiven'])
    if ask == 'yk_rams':
        ink('29:8', '"one young bull, one ram, seven lambs" — %s; Lev 16:5 "one ram for a burnt offering"' % T_YK)
        move('Yoma 3a:4, 70b:9', 'one ram (Rebbi — the same at both seats) or two (R. Elazar b. R. Shimon)')
        dat('the row yom_kippur_rams = %s' % data['yom_kippur_rams']['value'])
        return out('one ram — Lev 16:5\'s and 29:8\'s the same (Rebbi)', ['accepted'])
    if ask == 'musaf_order':
        move('Yoma 70a-70b', 'the Day\'s musaf offered with the morning tamid (R. Eliezer) / the bull and seven lambs with the morning, the goat and the ram with the twilight (R. Akiva)')
        return out('the Day\'s musaf order — a recorded dispute', ['accepted'])
    if ask == 'convocation':
        ink('29:1, 29:7', '"a holy convocation" at both days; "no servile work" at the first, "no work" at the tenth — the two classes on one page')
        move('CALLED cold_run_moadim.work_class(rosh_hashanah) -> %s; (yom_kippur) -> %s [IMPORT, live]' % (MO_WORK['rosh_hashanah'], MO_WORK['yom_kippur']), 'the classes by the verse that names the day')
        return out('servile at the first, all work at the tenth — the classes by call', ['rest_required'])
    if ask == 'shofar_on_sabbath':
        move('Mishnah Rosh Hashanah 4:8 (32b:23); 4:7 (32b:18)', 'the shofar\'s facilitators barred on the Sabbath; the second prayer leader sounds it — the prayer modeled on the musaf')
        return out('the blowing at the musaf; its facilitators barred', ['exempt'])
    return out('no verdict in span', [FX.NONE])


# ===== F6: SUKKOT AND THE EIGHTH DAY (Num 29:12-38) ==========================================================
def sukkot(case, data):
    del P[:]
    ask = case['ask']
    if ask.startswith('watches_'):
        return the_watches(case, data)
    if ask == 'the_dates':
        ink('29:12', '"on the fifteenth day of the seventh month a holy convocation... you shall keep a feast to the LORD seven days" — %s by the parser' % DATE_SUKKOT)
        move('CALLED cold_run_moadim.sukkot() -> date %s, length %s, eighth %s [IMPORT, live]' % (MO_SUK['date']['v'], MO_SUK['length']['v'], MO_SUK['eighth']['v']), 'Leviticus 23:34-36 at its second seat')
        return out('the fifteenth, seven days, the eighth an assembly — Leviticus 23 by call', ['musaf_owed'])
    if ask == 'the_declining_bulls':
        ink('29:13-32', 'the bulls %s — thirteen to seven, one fewer each day; rams %s, lambs %s each day (the parser at the seven heads)' % ([s[0] for s in SUKKOT], [s[1] for s in SUKKOT], [s[2] for s in SUKKOT]))
        ink('29:13-32', 'the sums: %d bulls, %d rams, %d lambs (computed)' % (BULLS_70, RAMS_14, LAMBS_98))
        move('Sukkah 55b:9 (R. Elazar)', 'the seventy bulls for the seventy nations; the eighth\'s one for the one nation')
        return out('seventy bulls — thirteen down to seven', ['musaf_owed'])
    if ask == 'the_multiplied_table':
        ink('29:14-15', '"three tenths for each bull OF THE THIRTEEN BULLS, two tenths for each ram OF THE TWO RAMS, a tenth for each lamb OF THE FOURTEEN LAMBS" — the master row multiplied, the multipliers named on the first day alone')
        move('CALLED cold_run_shelach.libations(table_seats) -> %s [IMPORT, live]' % SH_SEATS, 'the same rows at every seat')
        return out('the master row multiplied — the multipliers written once', ['musaf_owed'])
    if ask == 'the_pointer_line':
        ink('29:18-37', '"their meal offering and their libations for the bulls, for the rams and for the lambs BY THEIR NUMBER ACCORDING TO THE ORDINANCE" — %d seats of "by their number", %d of "according to the ordinance", %d of "their ordinance" (computed): the pointer INTERNAL to 28:12-14' % (len(BY_NUMBER), len(ORDINANCE), len(THEIR_ORDINANCE)))
        return out('by their number according to the ordinance — the pointer line six times, internal', ['accepted'])
    if ask == 'the_water_libation':
        ink('29:19, 29:31, 29:33', 'the pointer line\'s three deviations: %s against the plain %s — the surplus letters %s = "water" (computed off the ink; M-28)' % (LETTERS, PLAIN, MAYIM))
        move('Sifrei 150:1 (ben Beteira); Taanit 2b:14; Shabbat 103b:12, 103b:16', 'mem, yod, mem = MAYIM (water): the water libation from the letters; a closed letter rendered open valid — the scribal license')
        dat('the row water_libation_source = %s (the arms: %s)' % (data['water_libation_source']['value'], ', '.join(data['water_libation_source']['settings'])))
        return out('the three letters spell water — the libation\'s four sources a parameter', ['libation_owed'])
    if ask == 'water_days':
        move('Taanit 3a:3-7; Sukkah 34a:2, 44a:5; Zevachim 110b:6', 'all seven days — a halakhah to Moses from Sinai (a received rule); the sources\' day-counts 1 / 2 / 6 / 8 computed by the Gemara')
        dat('the row water_libation_days = %s; water_libation_measure = %s' % (data['water_libation_days']['value'], data['water_libation_measure']['value']))
        return out('seven days, three log — the received rule', ['libation_owed'])
    if ask == 'rain_mention':
        move('Taanit 2b:3-9', 'the rain\'s mention hung on the water libation\'s day — the second (ben Beteira), the sixth (R. Akiva), the eighth\'s last prayer leader')
        dat('the row rain_mention_day = %s' % data['rain_mention_day']['value'])
        return out('the rain mentioned from the eighth\'s last prayer', ['accepted'])
    if ask == 'the_eighth':
        ink('29:35-36', '"ON THE EIGHTH DAY an assembly shall be to you... one bull, one ram, seven lambs" — %s by the parser: not the decline\'s six' % T_EIGHTH)
        move('Sukkah 47a:8 (Rav Pappa); 47a:12; 48a:1', 'a festival of its own — one bull where the decline would give six; the rams and sheep halved; PZR KShB the six marks')
        dat('the row eighth_day_status = %s' % data['eighth_day_status']['value'])
        return out('the eighth its own festival — one bull, [1, 1, 7]', ['musaf_owed'])
    if ask == 'eighth_head':
        ink('29:17-35', 'the day-heads %s — six with the conjunction, the eighth WITHOUT (computed)' % HEADS)
        move('Sukkah 47a:9 (Rav Nachman b. Yitzchak)', '"on the eighth day" against "AND on the second day" — the eighth not continued from the seventh')
        return out('the eighth\'s head without the vav — its own festival', ['accepted'])
    if ask == 'sukkot_sabbath':
        move('CALLED cold_run_shelach.libations(sukkot_sabbath) -> %s; SUKKOT_SABBATH = %d [IMPORT, live]' % (SH_SUKSAB, SH_61), 'sixty-one tenths on a Sukkot Sabbath (Mishnah Menachot 12:4) — the table\'s arithmetic on the shelf')
        return out('sixty-one tenths on a Sukkot Sabbath — by call', ['musaf_owed'])
    if ask == 'stay':
        ink('29:35', '"an assembly (atzeret)" — the word\'s Torah seats: Lev 23:36, here, Deut 16:8 (Pesach\'s seventh)')
        move('Sifrei 151:1; Chagigah 17a:9, 17b:1; Pesachim 95b:6-8', '"withheld" — the overnight stay after the festival: Pesach\'s "you shall turn in the morning" carried to Sukkot by Deut 16:16; Chagigah 18a:9 "atzeret = pause" at Deut 16:8')
        dat('the row atzeret_stay = %s' % data['atzeret_stay']['value'])
        return out('an assembly — withheld overnight after the festival', ['exempt'])
    if ask == 'dotted_tenth':
        ink('29:15', '"and a tenth, a tenth for each lamb" — the first tenth-word DOTTED in the scrolls (the reading\'s row; the store\'s puncta not on this DB)')
        move('Menachot 87b:5', 'the dotted tenth — the ten dotted seats of the Torah; the reading\'s parameter tenth_vessels')
        return out('the dotted tenth at 29:15 — a mark to check on the store', ['accepted'])
    if ask == 'seventy_nations':
        move('Sukkah 55b:9; 55b:8', 'the seventy bulls — the seventy nations; a simple calculation: seventy over twenty-four watches = %s (computed)' % (SEVENTY_SPLIT,))
        return out('seventy for the seventy nations — twenty-two watches thrice, two twice', ['smoked_to_the_lord'])
    if ask == 'the_rite':
        move('CALLED cold_run_offerings.dispatch(olah:herd) -> place %s, disposition %s; (outer_chatat) -> eater %s [IMPORT, live]' % (OLAH_HERD['place']['v'], OLAH_HERD['disposition']['v'], CHATAT_OUT['eater']['v']), 'the bulls\' rite Leviticus 1\'s, the goats\' Leviticus 4\'s')
        return out('the bulls wholly to the fire; the goat eaten by the male priests — by call', ['smoked_to_the_lord'])
    return out('no verdict in span', [FX.NONE])


def the_watches(case, data):
    """Mishnah Sukkah 5:6 (Sukkah 55b:1-8): the twenty-four watches divide the day's offerings — a FUNCTION of the declining table."""
    del P[:]
    ask = case['ask']
    if ask == 'watches_division':
        ink('29:13-32', 'day d: (14 - d) bulls + 2 rams + 1 goat to as many watches, the fourteen lambs to the rest — %s (big, rest, two-lamb watches, one-lamb watches) computed' % WD)
        move('Mishnah Sukkah 5:6; Sukkah 55b:1-2', 'the first day sixteen offerings to sixteen watches, six of the remaining eight two lambs, two one; the second fifteen, five and four')
        return out('the watches\' shares a function of the table — (16, 8, 6, 2) then (15, 9, 5, 4)', ['musaf_owed'])
    if ask == 'watches_seventh':
        move('Sukkah 55b:4', 'the seventh all equal — %d + %d + 1 + %d = %d = the watches (computed)' % (SUKKOT[6][0], SUKKOT[6][1], SUKKOT[6][2], sum(SUKKOT[6]) + 1))
        return out('the seventh day every watch one offering', ['accepted'])
    if ask == 'watches_eighth':
        move('Sukkah 55b:5', 'the eighth\'s bull — a lottery from the beginning (Rebbi) or one of the two watches that offered only two bulls (the Rabbis)')
        return out('the eighth\'s bull by lot or to a twice-watch — a recorded dispute', ['accepted'])
    if ask == 'watches_institution':
        move('Mishnah Taanit 4:2 (the link row); Taanit 27a:3', '"command... My offering... you shall keep" (28:2) — a communal obligation on every Israelite: the prophets instituted the watches standing by')
        return out('the watches instituted on "you shall keep" — the people stand by their offering', ['accepted'])
    return out('no verdict in span', [FX.NONE])


# ===== F7: THE CALENDAR AS ONE TABLE (Num 29:39 and the span whole) =========================================
def the_calendar(case, data):
    del P[:]
    ask = case['ask']
    if ask == 'these_you_shall_do':
        ink('29:39', '"THESE you shall make to the LORD IN YOUR APPOINTED TIMES, besides your vows and your freewill offerings, for your burnt offerings, your meal offerings, your libations and your peace offerings" — the closer names the whole; "these" at 28:23 and here')
        move('Sifrei 152:1', '"in your appointed times" — the fixed and the vowed apart; the vows brought on the festival (Beitzah 19a-20b the dispute)')
        return out('these in your appointed times — the fixed table; the vows besides', ['commanded'])
    if ask == 'the_thirteen_goats':
        ink('28:15-29:38', 'thirteen goats (computed: %d); ONE "to the LORD" (%s), THREE "to atone" (%s), NINE bare' % (len(GOATS), GOAT_TO_LORD, TO_ATONE))
        move('Mishnah Shevuot 1:4-5 (2a:8-2b:7); Shevuot 10a:14-16', 'R. Yehuda one job, R. Shimon three tiers, R. Meir flat with the inner goat excepted')
        dat('the row goats_atonement_tiers = %s' % data['goats_atonement_tiers']['value'])
        return out('thirteen goats — one, three, nine by the grammar; the jobs the tannaim\'s', ['musaf_owed'])
    if ask == 'goat_vav':
        ink('28:15-29:38', 'the goat-word with the conjunction at %d lines, WITHOUT at %s (computed): Shavuot\'s and Yom Kippur\'s' % (len(GOAT_VAV), GOAT_BARE))
        move('Shevuot 9b:2, 10a:8, 10a:11 (R. Chama b. R. Chanina)', '"AND a goat" juxtaposes each festival\'s goat to the new moon\'s at the passage\'s head; Shavuot\'s and Yom Kippur\'s carry no vav — the Talmud\'s token fact matches the ink')
        move('Shevuot 10a:9 (R. Yochanan)', 'no juxtaposition from a juxtaposition in consecrated matters — every goat runs directly to the first')
        return out('eleven with the vav, two without — Shavuot\'s and Yom Kippur\'s, as the Talmud says', ['accepted'])
    if ask == 'interchange':
        move('Shevuot 2b:4, 11b:10, 12b:4', 'a goat consecrated for one day offered on another — R. Shimon: yes, one genus; the ring festival, new moon, Yom Kippur, festival')
        dat('the row communal_consecration = %s' % data['communal_consecration']['value'])
        return out('the goats interchange — one genus, the species by the knife', ['accepted'])
    if ask == 'besides_twelve':
        ink('28:23-29:38', '"besides" (mil-vad) %d seats (computed) — every musaf written BESIDE the continual; 29:39 "besides" (le-vad) the closer\'s form' % len(BESIDES))
        move('Sifrei 147:1', '"besides the burnt offering of the morning" — the tamid first, then the musaf (Mishnah Zevachim 10:1 the frequent precedes)')
        return out('besides twelve times — the tamid first, the musaf beside it', ['musaf_owed'])
    if ask == 'the_sums':
        ink('the span', 'the year\'s lambs: the tamid %d x 354; the Sabbath\'s %d x ~50; the tables\' — Tishri\'s first %d, Shabbat with the two days of Rosh Hashanah %d, Sukkot\'s %d; the bulls %d; the goats %d (computed)' % (TAMID_TWO[0], SAB_TWO[0], LAMBS_TISHRI_1, LAMBS_THREE_DAYS, LAMBS_98, BULLS_70, len(GOATS)))
        move('Menachot 49b:5; Arakhin 13a:10; Sukkah 55b:8', 'twenty-two lambs for Shabbat and the two days of Rosh Hashanah = 6 + 2 + 7 + 7; sixteen on Tishri\'s first; seventy over twenty-four watches')
        return out('the sums — 16, 22, 70, 13: the tables\' arithmetic', ['accepted'])
    if ask == 'ben_azzai_census':
        ink('the span; Lev 1-7', 'the special Name %d / the other names %s in the span; %d / %s in Leviticus 1-7 (computed): the two other seats are the covenant\'s and an apposition, neither an offering\'s addressee' % (NAMES_SPAN[0], NAMES_SPAN[1], NAMES_LEV[0], [(c, v) for c, v, _ in NAMES_LEV[1]]))
        move('Sifrei 143:2 (ben Azzai); Menachot 110a', 'not God, not Shaddai, not Hosts — the special Name at every offering, "so as not to give the heretics a foothold"')
        return out('the special Name only as the addressee — zero in the span, two non-addressee seats in Leviticus 1-7', ['accepted'])
    if ask == 'timers':
        dat('the daemon\'s eight PERIOD TIMERS: %s — the Calendar\'s keys by CALL (the moadim engine\'s dates); the tables the values' % ', '.join('%s %s' % (k, v) for k, v in TABLES.items()))
        move('Rosh Hashanah 5a:4; Chagigah 17b:7', 'the count\'s unit is the sanctification\'s span — the month\'s timer a day, the week\'s a Sabbath')
        return out('eight period timers — sabbath, month, passover_1, atzeret, rosh_hashanah, yom_kippur, sukkot_1, shemini', ['musaf_owed'])
    if ask == 'its_day_passed':
        move('Berakhot 26a:17', '"its day passed, its sacrifice is invalid" — the offering\'s due cannot be paid late: the musaf_owed debit lapses at the day\'s end, the timer\'s miss a miss')
        return out('a missed day is not a carried debt — the debit lapses', ['exempt'])
    if ask == 'sanctity_marker':
        move('Chagigah 18a:6', 'the weekdays no musaf; the new moon a musaf and labor permitted; the intermediate days a holy convocation — the musaf grades the days')
        return out('the musaf a sanctity marker — the tradition\'s own scale', ['accepted'])
    if ask == 'run_in_writings':
        move('Menachot 110a:9 (2 Chr 2:3); Sukkah 51a:12-13 (2 Chr 29:27, 5:13)', 'Solomon\'s four tiers — morning and evening, the Sabbaths, the new moons, the festivals; the song with the burnt offering; the trumpets over THE TEMIDIM AND THE MUSAFIM')
        return out('the calendar RUN in Chronicles — four tiers, the song, the trumpets', ['accepted'])
    if ask == 'vow_deadline':
        move('Beitzah 19b:8-13', '"you shall not delay" measured in festivals — three any order / in order / by Sukkot')
        dat('the row vow_deadline = %s' % data['vow_deadline']['value'])
        return out('three festivals in any order — the first tanna', ['commanded'])
    if ask == 'pointers':
        ink('28:8; 29:18-37', 'the span\'s pointers computed: %s — every one INTERNAL (the tamid 28:5-7; the master row 28:12-14)' % POINTERS)
        return out('nine pointers, all internal — the master row and the tamid', ['accepted'])
    if ask == 'the_register_gate':
        ink('28:1-29:39', 'the register: one verb (28:1), no count-noun, no receipt, no register header — no seat of 28-29 in the register gate\'s four censuses (the gate\'s own print at the gates step)')
        return out('no register seat in 28-29 — the gate\'s print the check', ['accepted'])
    if ask == 'peace_offerings':
        ink('29:39', '"and for your peace offerings" — the vowed peace offerings named at the close')
        move('CALLED cold_run_offerings.dispatch(shelamim) -> window %s [IMPORT, live]' % SHELAMIM['window']['v'], 'Leviticus 7\'s window for the vowed peace offering')
        return out('the vowed peace offerings — two days and a night by call', ['accepted'])
    return out('no verdict in span', [FX.NONE])


# ---- THE WRAP — the daemon, the scene, the narrative ------------------------------------------------------
KEYS = ('sabbath', 'month', 'passover_1', 'atzeret', 'rosh_hashanah', 'yom_kippur', 'sukkot_1', 'shemini')
def law_musafim(event, world):
    """Num 28:1-29:39 (cold_run_musafim.py F1-F7 + the watches). installed_by called_from_the_tent — a standing statute (law_moadim's form):
    the ONE tape line sets EIGHT PERIOD TIMERS of musaf_owed on the altar, keyed to the Calendar; the tamid's open debt is READ, never rewritten."""
    k, src = event['kind'], event['case_source']
    E_ = lambda eff, s, cp=None, amount=None, due=None, law='', value=None, period=None: dict({'effect': eff, 'subject': s, 'counterparty': cp, 'amount': amount, 'due': due, 'value': value if value is not None else True, 'source_law': law, 'case_source': src}, **({'period': period} if period else {}))
    if k == 'offerings_calendar_commanded':
        tamid = [e for e in world.entity('the-altar').ledger if e['effect'] == 'tamid_owed']
        read = ('READ — open since %s' % tamid[0].get('case_source', '')[:24]) if tamid else 'NOT FOUND on this world (the erection not on it)'
        out_ = []
        for key in KEYS:                                                        # the eight keys in the ink's own order (the Sabbath, the month, Pesach, the firstfruits, Tishri's first and tenth, Sukkot, the eighth)
            table = event['tables'][key]
            out_.append(E_('musaf_owed', 'the-altar', cp='HEAVEN', value=[key] + list(table), due=world.clock.next(key), period=key,
                           law='F7 [INK 28:10 "the burnt offering of the Sabbath on its Sabbath, beside the continual"; 28:14 "in its month"; 29:39 "in your appointed times" — the PERIOD TIMER on the Calendar\'s key %s, the table %s the value; the tamid\'s debt %s]' % (key, table, read)))
        return out_
    # ---- the exam's case kinds: each names LITERALLY every effect it can write (2b's form) ----
    if k == 'tamid_case':
        v, e, _ = the_tamid({'ask': event['ask']}, DATA); L = 'F1 [%s]' % v; s_ = event['person']
        W = {'accepted': E_('accepted', s_, value=v, law=L), 'commanded': E_('commanded', s_, value=v, law=L), 'tamid_owed': E_('tamid_owed', s_, cp='HEAVEN', value=v, law=L), 'libation_owed': E_('libation_owed', s_, cp='HEAVEN', value=v, law=L), 'disqualified': E_('disqualified', s_, value=v, law=L), 'exempt': E_('exempt', s_, value=v, law=L)}
        return [W[x] for x in e if x != FX.NONE]
    if k == 'sabbath_musaf_case':
        v, e, _ = the_sabbath({'ask': event['ask']}, DATA); L = 'F2 [%s]' % v; s_ = event['person']
        W = {'accepted': E_('accepted', s_, value=v, law=L), 'musaf_owed': E_('musaf_owed', s_, cp='HEAVEN', value=v, law=L), 'labor_barred': E_('labor_barred', s_, value=v, law=L), 'rest_required': E_('rest_required', s_, value=v, law=L), 'exempt': E_('exempt', s_, value=v, law=L)}
        return [W[x] for x in e if x != FX.NONE]
    if k == 'new_moon_case':
        v, e, _ = the_new_moon({'ask': event['ask']}, DATA); L = 'F3 [%s]' % v; s_ = event['person']
        W = {'accepted': E_('accepted', s_, value=v, law=L), 'musaf_owed': E_('musaf_owed', s_, cp='HEAVEN', value=v, law=L), 'atoned_forgiven': E_('atoned_forgiven', s_, cp='HEAVEN', value=v, law=L), 'sanctify_day': E_('sanctify_day', s_, cp='HEAVEN', value=v, law=L), 'exempt': E_('exempt', s_, value=v, law=L)}
        return [W[x] for x in e if x != FX.NONE]
    if k == 'pesach_shavuot_case':
        v, e, _ = pesach_shavuot({'ask': event['ask']}, DATA); L = 'F4 [%s]' % v; s_ = event['person']
        W = {'accepted': E_('accepted', s_, value=v, law=L), 'musaf_owed': E_('musaf_owed', s_, cp='HEAVEN', value=v, law=L), 'labor_barred': E_('labor_barred', s_, value=v, law=L), 'commanded': E_('commanded', s_, value=v, law=L), 'disqualified': E_('disqualified', s_, value=v, law=L), 'exempt': E_('exempt', s_, value=v, law=L)}
        return [W[x] for x in e if x != FX.NONE]
    if k == 'tishri_case':
        v, e, _ = tishri({'ask': event['ask']}, DATA); L = 'F5 [%s]' % v; s_ = event['person']
        W = {'accepted': E_('accepted', s_, value=v, law=L), 'musaf_owed': E_('musaf_owed', s_, cp='HEAVEN', value=v, law=L), 'labor_barred': E_('labor_barred', s_, value=v, law=L), 'rest_required': E_('rest_required', s_, value=v, law=L), 'atoned_forgiven': E_('atoned_forgiven', s_, cp='HEAVEN', value=v, law=L), 'exempt': E_('exempt', s_, value=v, law=L)}
        return [W[x] for x in e if x != FX.NONE]
    if k == 'sukkot_case':
        v, e, _ = sukkot({'ask': event['ask']}, DATA); L = 'F6 [%s]' % v; s_ = event['person']
        W = {'accepted': E_('accepted', s_, value=v, law=L), 'musaf_owed': E_('musaf_owed', s_, cp='HEAVEN', value=v, law=L), 'libation_owed': E_('libation_owed', s_, cp='HEAVEN', value=v, law=L), 'smoked_to_the_lord': E_('smoked_to_the_lord', s_, value=v, law=L), 'exempt': E_('exempt', s_, value=v, law=L)}
        return [W[x] for x in e if x != FX.NONE]
    if k == 'calendar_case':
        v, e, _ = the_calendar({'ask': event['ask']}, DATA); L = 'F7 [%s]' % v; s_ = event['person']
        W = {'accepted': E_('accepted', s_, value=v, law=L), 'musaf_owed': E_('musaf_owed', s_, cp='HEAVEN', value=v, law=L), 'commanded': E_('commanded', s_, value=v, law=L), 'exempt': E_('exempt', s_, value=v, law=L)}
        return [W[x] for x in e if x != FX.NONE]
    return []


LINE = 'Num 28:1-29:39 — and the LORD spoke to Moses, saying: command the children of Israel and say to them: My offering, My bread for My fire offerings, My pleasing odor, you shall keep to bring near to Me in its appointed time; and you shall say to them: this is the fire offering that you shall bring near to the LORD: yearling lambs without blemish, two a day, a continual burnt offering... these you shall make to the LORD in your appointed times, besides your vows and your freewill offerings'
CLOSE = 'none — each timer\'s fire opens the day\'s debt and the offering brought closes it; no offering line in the span'


def scene():
    """THE SCENE — the exam's rows replayed on the world engine (the exodus epoch): the seven case kinds on the exam's persons."""
    with contextlib.redirect_stdout(io.StringIO()):
        w = WE.World(era='Num 28:1-29:39: Menachot 4-5, 9, 12; Shevuot 1; Sukkah 4-5; Rosh Hashanah 4; Tamid 4, 7; Arakhin 2; Beitzah 2; Chagigah 1-2 on the engine (the exodus epoch)', epoch='exodus')
        w.laws = [law_musafim]
        w.advance(w.clock.day_in('exodus', 40, 6, 1))
        # LITERAL submits (the daemon gate parses no loop — 5b's, 7b's and 8b's lesson): twenty-one of the exam's persons through the seven case kinds
        w.submit({'kind': 'tamid_case', 'subject': 'the-appointed-time', 'person': 'the-appointed-time', 'ask': 'appointed_time', 'case_source': 'Num 28:2 — the exam\'s row appointed_time (Pesachim 66a; the Sifrei 142:3)'})
        w.submit({'kind': 'tamid_case', 'subject': 'the-two-lambs', 'person': 'the-two-lambs', 'ask': 'two_per_day', 'case_source': 'Num 28:3 — the exam\'s row two_per_day (Exod 29:38 by CALL)'})
        w.submit({'kind': 'tamid_case', 'subject': 'the-tenth-of-flour', 'person': 'the-tenth-of-flour', 'ask': 'the_tenth', 'case_source': 'Num 28:5 — the exam\'s row the_tenth (three log by CALL)'})
        w.submit({'kind': 'tamid_case', 'subject': 'the-withholding-priest', 'person': 'the-withholding-priest', 'ask': 'morning_missed', 'case_source': 'Mishnah Menachot 4:4 — the exam\'s row morning_missed'})
        w.submit({'kind': 'tamid_case', 'subject': 'the-surplus-lamb', 'person': 'the-surplus-lamb', 'ask': 'surplus_lambs', 'case_source': 'Shevuot 10b:7 — the exam\'s row surplus_lambs'})
        w.submit({'kind': 'sabbath_musaf_case', 'subject': 'the-sabbath-lambs', 'person': 'the-sabbath-lambs', 'ask': 'two_lambs', 'case_source': 'Num 28:9 — the exam\'s row two_lambs'})
        w.submit({'kind': 'sabbath_musaf_case', 'subject': 'the-sabbath-override', 'person': 'the-sabbath-override', 'ask': 'overrides', 'case_source': 'Num 28:10 — the exam\'s row overrides (Shabbat 132b:1)'})
        w.submit({'kind': 'sabbath_musaf_case', 'subject': 'the-sabbath-song', 'person': 'the-sabbath-song', 'ask': 'between_the_temidim', 'case_source': 'Mishnah Tamid 7:3 — the exam\'s row between_the_temidim'})
        w.submit({'kind': 'new_moon_case', 'subject': 'the-new-moon-table', 'person': 'the-new-moon-table', 'ask': 'the_table', 'case_source': 'Num 28:11 — the exam\'s row the_table'})
        w.submit({'kind': 'new_moon_case', 'subject': 'the-goat-to-the-lord', 'person': 'the-goat-to-the-lord', 'ask': 'the_goat_to_the_lord', 'case_source': 'Num 28:15 — the exam\'s row the_goat_to_the_lord (Shevuot 9a:7-10)'})
        w.submit({'kind': 'new_moon_case', 'subject': 'the-month-sanctified', 'person': 'the-month-sanctified', 'ask': 'month_sanctified', 'case_source': 'Rosh Hashanah 5a:4 — the exam\'s row month_sanctified'})
        w.submit({'kind': 'new_moon_case', 'subject': 'the-new-moon-worker', 'person': 'the-new-moon-worker', 'ask': 'labor_permitted', 'case_source': 'Chagigah 18a:6 — the exam\'s row labor_permitted'})
        w.submit({'kind': 'pesach_shavuot_case', 'subject': 'the-festival-worker', 'person': 'the-festival-worker', 'ask': 'food_work', 'case_source': 'Num 28:18 — the exam\'s row food_work (Beitzah 12a:4)'})
        w.submit({'kind': 'pesach_shavuot_case', 'subject': 'the-second-set', 'person': 'the-second-set', 'ask': 'the_second_set', 'case_source': 'Num 28:27 — the exam\'s row the_second_set (Menachot 45b:10-13)'})
        w.submit({'kind': 'pesach_shavuot_case', 'subject': 'the-blemished-wine', 'person': 'the-blemished-wine', 'ask': 'libations_likened', 'case_source': 'Num 28:31 — the exam\'s row libations_likened (Sifrei 148:2)'})
        w.submit({'kind': 'tishri_case', 'subject': 'the-day-of-blowing', 'person': 'the-day-of-blowing', 'ask': 'day_of_blowing', 'case_source': 'Num 29:1 — the exam\'s row day_of_blowing (Rosh Hashanah 33b-34a)'})
        w.submit({'kind': 'tishri_case', 'subject': 'the-tenth-day', 'person': 'the-tenth-day', 'ask': 'the_tenth', 'case_source': 'Num 29:7 — the exam\'s row the_tenth (Yoma 76a:11)'})
        w.submit({'kind': 'tishri_case', 'subject': 'the-outer-goat', 'person': 'the-outer-goat', 'ask': 'atonements_goat', 'case_source': 'Num 29:11 — the exam\'s row atonements_goat (Mishnah Shevuot 1:3; the Yoma engine by CALL)'})
        w.submit({'kind': 'sukkot_case', 'subject': 'the-seventy-bulls', 'person': 'the-seventy-bulls', 'ask': 'the_declining_bulls', 'case_source': 'Num 29:13-32 — the exam\'s row the_declining_bulls (Sukkah 55b:9)'})
        w.submit({'kind': 'sukkot_case', 'subject': 'the-water-libation', 'person': 'the-water-libation', 'ask': 'the_water_libation', 'case_source': 'Num 29:19, 29:31, 29:33 — the exam\'s row the_water_libation (Taanit 2b:14)'})
        w.submit({'kind': 'sukkot_case', 'subject': 'the-eighth-day', 'person': 'the-eighth-day', 'ask': 'the_eighth', 'case_source': 'Num 29:35-36 — the exam\'s row the_eighth (Sukkah 47a:8)'})
        w.submit({'kind': 'sukkot_case', 'subject': 'the-lodger', 'person': 'the-lodger', 'ask': 'stay', 'case_source': 'Num 29:35 — the exam\'s row stay (Chagigah 17a:9)'})
        w.submit({'kind': 'sukkot_case', 'subject': 'the-watches', 'person': 'the-watches', 'ask': 'watches_division', 'case_source': 'Mishnah Sukkah 5:6 — the exam\'s row watches_division'})
        w.submit({'kind': 'calendar_case', 'subject': 'the-thirteen-goats', 'person': 'the-thirteen-goats', 'ask': 'the_thirteen_goats', 'case_source': 'Num 28:15-29:38 — the exam\'s row the_thirteen_goats (Mishnah Shevuot 1:4-5)'})
        w.submit({'kind': 'calendar_case', 'subject': 'the-vower', 'person': 'the-vower', 'ask': 'vow_deadline', 'case_source': 'Num 29:39 — the exam\'s row vow_deadline (Beitzah 19b:8-13)'})
        w.submit({'kind': 'calendar_case', 'subject': 'the-late-musaf', 'person': 'the-late-musaf', 'ask': 'its_day_passed', 'case_source': 'Berakhot 26a:17 — the exam\'s row its_day_passed'})
    n = lambda eid, eff: len([e for e in w.entity(eid).ledger if e['effect'] == eff])
    return (n('the-appointed-time', 'tamid_owed'), n('the-two-lambs', 'tamid_owed'), n('the-tenth-of-flour', 'libation_owed'), n('the-withholding-priest', 'disqualified'), n('the-surplus-lamb', 'exempt'),
            n('the-sabbath-lambs', 'musaf_owed'), n('the-sabbath-override', 'labor_barred'), n('the-sabbath-song', 'rest_required'),
            n('the-new-moon-table', 'musaf_owed'), n('the-goat-to-the-lord', 'atoned_forgiven'), n('the-month-sanctified', 'sanctify_day'), n('the-new-moon-worker', 'exempt'),
            n('the-festival-worker', 'labor_barred'), n('the-second-set', 'musaf_owed'), n('the-blemished-wine', 'disqualified'),
            n('the-day-of-blowing', 'musaf_owed'), n('the-tenth-day', 'labor_barred'), n('the-outer-goat', 'atoned_forgiven'),
            n('the-seventy-bulls', 'musaf_owed'), n('the-water-libation', 'libation_owed'), n('the-eighth-day', 'musaf_owed'), n('the-lodger', 'exempt'), n('the-watches', 'musaf_owed'),
            n('the-thirteen-goats', 'musaf_owed'), n('the-vower', 'commanded'), n('the-late-musaf', 'exempt'), len(w.entities), len(w.timers)), w
SCENE, _W = scene()


def narrative():
    """THE NUMBERS WALK 9b (2026-09-11): the portion's own act AS HISTORY — the ONE line of 28:1-29:39 at the counter's day (40, 6, 1), page-order
    after the daughters' output (27:6-11), on a world with this runner's daemon: EIGHT PERIOD TIMERS set, none fired, no marker, no entity but
    the altar. Recorded by the sequential run's recorder and stitched onto the tape. Not a graded cell: the tuple below is a tripwire typed from
    the first run's print; the sequence world's RUN tuple and CT1-CT9 grade the tape."""
    with contextlib.redirect_stdout(io.StringIO()):
        w = WE.World(era='Num 28:1-29:39: the offerings calendar on the tape — one speech, eight period timers on the altar (the exodus epoch)', epoch='exodus')
        w.laws = [law_musafim]
        w.advance(w.clock.day_in('exodus', 40, 6, 1))
        # THE DAEMON GATE READS LITERAL SUBMITS ONLY (7b's and 8b's lesson) — the one line typed out
        w.submit({'kind': 'offerings_calendar_commanded', 'subject': 'israel', 'tables': dict(TABLES), 'close': CLOSE, 'case_source': LINE})
    tset = [l for l in w.log if l[0] == 'TIMER-SET']; fired = [l for l in w.log if l[0] == 'TIMER-FIRE']
    dues = [w.clock.eras['exodus'].date(t[0])[1:] for t in w.timers]
    keys = [t[1].get('period') for t in w.timers]
    read = [t[1]['source_law'].split('the tamid\'s debt ')[1].rstrip(']')[:9] for t in w.timers][:1]   # the first run read the LEDGER and found nothing: a pending timer is not a ledger entry until it fires — the note sits on the timer
    return (len(tset), len(fired), len(w.timers), keys, dues, read, len(w.entities), w.clock.eras['exodus'].date(w.clock.day)[1:]), w


NARRATIVE, _WN = narrative()
NARRATIVE_PREDICTED = (8, 0, 8, ['sabbath', 'month', 'passover_1', 'atzeret', 'rosh_hashanah', 'yom_kippur', 'sukkot_1', 'shemini'],
                       [(6, 8), (7, 1), (1, 15), (3, 6), (7, 1), (7, 10), (7, 15), (7, 22)], ['NOT FOUND'], 1, (6, 1))   # NUMBERS_WALK.md "Sitting 9b": eight timers set, none fired, eight pending in the keys' order; the dues from (40, 6, 1) — the Sabbath the 8th of the sixth month, the month and Tishri's first (7, 1), Pesach's first and Shavuot in the next year (1, 15), (3, 6), the tenth, Sukkot, the eighth; the tamid's debt NOT FOUND on the narrative world (the erection is not on it — READ on the tape); one entity (the altar); the date (6, 1) of the fortieth year
assert NARRATIVE == NARRATIVE_PREDICTED, ('THE NUMBERS WALK: the offerings calendar\'s narrative moved from its prediction', NARRATIVE, NARRATIVE_PREDICTED)


# =====================================================================
# Motion 2 — THE TEST DATA: the answer sheet's rows (the docket's LAW rows).
# =====================================================================
CASES = [
    # F1 — the tamid
    ('Num 28:1-2 / Sifrei 142:1 — one speech, a standing statute', lambda: the_tamid({'ask': 'frame'}, DATA), 'one speech, 28:1-29:39 — a standing statute commanded'),
    ('Num 28:2 / Sifrei 142:2 — the four possessives', lambda: the_tamid({'ask': 'possessives'}, DATA), 'four possessives — the altar\'s bread'),
    ('Num 28:2 / Pesachim 66a, 81b:3 — in its appointed time (the freed term)', lambda: the_tamid({'ask': 'appointed_time'}, DATA), 'in its appointed time — even the Sabbath, even impurity (the Pesach\'s analogy)'),
    ('Num 28:3 / Exod 29:38 by CALL — two a day, without blemish added', lambda: the_tamid({'ask': 'two_per_day'}, DATA), 'two a day — Exod 29:38 restated with "without blemish" added'),
    ('Num 28:4 / Menachot 50a:6 by CALL — the one and the second', lambda: the_tamid({'ask': 'the_one_lamb'}, DATA), 'the one in the morning, the second between the evenings'),
    ('Num 28:5 / Menachot 51a, 86b by CALL — the tenth, the quarter-hin, the salt', lambda: the_tamid({'ask': 'the_tenth'}, DATA), 'a tenth with a quarter-hin of beaten oil — three log; salted'),
    ('Num 28:6 / Chagigah 6a:15-6b:4 — made at Mount Sinai', lambda: the_tamid({'ask': 'made_at_sinai'}, DATA), 'made at Sinai — the tamid by one house, its prescription by the other'),
    ('Num 28:7 / Sukkah 49b:5; Sifrei 143:2 — strong drink; the doubled root', lambda: the_tamid({'ask': 'strong_drink'}, DATA), 'strong drink — wine that intoxicates; the doubled root R. Nathan\'s water'),
    ('Num 28:8 / Exod 29:41 by CALL — the pointer internal; Mishnah Menachot 4:4', lambda: the_tamid({'ask': 'the_second_lamb'}, DATA), 'as the morning\'s — the pointer internal; the second not held up by the first'),
    ('Sifrei 143:2 (ben Azzai) — the special Name at every offering (computed)', lambda: the_tamid({'ask': 'the_name'}, DATA), 'the special Name the addressee of every offering — no offering to God (computed)'),
    ('Exod 40:29 by CALL — the tamid read from the erection\'s debt', lambda: the_tamid({'ask': 'tamid_read'}, DATA), 'the tamid read from the erection\'s debt — never rewritten here'),
    ('Mishnah Menachot 4:4; Menachot 50a:2-4 — the morning missed', lambda: the_tamid({'ask': 'morning_missed'}, DATA), 'the twilight lamb offered; the withholding priests barred'),
    ('Pesachim 80b:5, 81a:14-15 — the impurity of the deep for the tamid', lambda: the_tamid({'ask': 'impurity_of_the_deep'}, DATA), 'the deep\'s impurity permitted for the tamid — the Pesach\'s analogy'),
    ('Shevuot 10b:7, 11a:8 — the surplus lambs redeemed', lambda: the_tamid({'ask': 'surplus_lambs'}, DATA), 'redeemed unblemished — the court\'s tacit stipulation'),
    ('Mishnah Arakhin 2:5; Arakhin 13a:11 — the six-lamb floor', lambda: the_tamid({'ask': 'lamb_stock'}, DATA), 'six lambs — three days of the tamid'),
    ('Chagigah 6a:16 — Abaye\'s census of the Sinai olah', lambda: the_tamid({'ask': 'sinai_olah'}, DATA), 'the Sinai olah the tamid — Beit Hillel\'s list'),
    # F2 — the Sabbath
    ('Num 28:9 — two lambs and two tenths', lambda: the_sabbath({'ask': 'two_lambs'}, DATA), 'two lambs and two tenths — the Sabbath\'s first offering'),
    ('Num 28:10 / Sifrei 144:1 — on its Sabbath', lambda: the_sabbath({'ask': 'on_its_sabbath'}, DATA), 'on its Sabbath — the debt lapses with the day'),
    ('Num 28:10 / Shabbat 132b:1 by CALL — the tamid on the Sabbath by name', lambda: the_sabbath({'ask': 'overrides'}, DATA), 'the tamid on the Sabbath by name — the override the verse\'s own'),
    ('Mishnah Tamid 7:3; Zevachim 10:1 — between the temidim', lambda: the_sabbath({'ask': 'between_the_temidim'}, DATA), 'between the temidim — the frequent first'),
    ('Mishnah Beitzah 2:4; Beitzah 20b:4 — the festival\'s licensed slaughter', lambda: the_sabbath({'ask': 'licensed_slaughter'}, DATA), 'the temidim and musafim the festival\'s licensed slaughter — both houses'),
    ('Pesachim 66a:3 — Hillel\'s more than two hundred', lambda: the_sabbath({'ask': 'hillel_two_hundred'}, DATA), 'more than two hundred a year — computable from the tables'),
    ('Lev 23:3 by CALL — the Sabbath\'s class', lambda: the_sabbath({'ask': 'work_class'}, DATA), 'all work barred — the moadim engine\'s class by call'),
    # F3 — the new moon
    ('Num 28:11 — the table [2, 1, 7]', lambda: the_new_moon({'ask': 'the_table'}, DATA), 'two bulls, one ram, seven lambs — the table [2, 1, 7]'),
    ('Num 28:12-14 / Num 15:4-10 by CALL — the master row read', lambda: the_new_moon({'ask': 'master_row'}, DATA), 'the master row = 15:4-10 by call — lamb 1/10 + 1/4, ram 2/10 + 1/3, bull 3/10 + 1/2'),
    ('Num 28:14 / Sifrei 145:2 — in its month', lambda: the_new_moon({'ask': 'in_its_month'}, DATA), 'in its month — the timer keyed to the month'),
    ('Num 28:15 / Shevuot 9a:7-10; Sifrei 145:3 — the goat to the LORD (the Yoma engine by CALL)', lambda: the_new_moon({'ask': 'the_goat_to_the_lord'}, DATA), 'to the LORD — the sin the LORD alone knows; the routing table\'s festival-and-new-moon agent'),
    ('Num 28:11-15 against Lev 23 — absent from Leviticus 23', lambda: the_new_moon({'ask': 'absent_from_lev23'}, DATA), 'the new moon absent from Leviticus 23 — this calendar\'s own day'),
    ('Menachot 45a:6-8 (Ezek 46:6-7) — the availability ladder', lambda: the_new_moon({'ask': 'availability'}, DATA), 'the ladder from Ezekiel — fewer when not found'),
    ('Rosh Hashanah 5a:4; Chagigah 17b:7 — the month sanctified by its offerings', lambda: the_new_moon({'ask': 'month_sanctified'}, DATA), 'the month sanctified by its offerings — one day'),
    ('Chagigah 18a:6 — a musaf without a ban', lambda: the_new_moon({'ask': 'labor_permitted'}, DATA), 'a musaf without a ban — labor permitted'),
    # F4 — Pesach and the firstfruits day
    ('Num 28:16-17 / Lev 23:5-6 by CALL — the dates', lambda: pesach_shavuot({'ask': 'the_dates'}, DATA), 'the fourteenth and the fifteenth — Leviticus 23 by call'),
    ('Num 28:18 / Beitzah 12a:4 — servile work; the food-work extension', lambda: pesach_shavuot({'ask': 'food_work'}, DATA), 'servile work barred — the lighter class; food work permitted'),
    ('Num 28:19 — the table [2, 1, 7] (rule 25)', lambda: pesach_shavuot({'ask': 'the_table'}, DATA), 'two bulls, one ram, seven lambs — the new moon\'s table'),
    ('Num 28:23-24 / Sifrei 147:2 — as these, seven days', lambda: pesach_shavuot({'ask': 'as_these'}, DATA), 'as these daily seven days — one table seven times'),
    ('Num 28:25 — the seventh a convocation', lambda: pesach_shavuot({'ask': 'the_seventh'}, DATA), 'the seventh a convocation — the same class'),
    ('Num 28:26 / Lev 23:16-17 by CALL — the day of firstfruits', lambda: pesach_shavuot({'ask': 'firstfruits_day'}, DATA), 'the day of firstfruits — the fiftieth, the two loaves the new meal offering'),
    ('Num 28:27 against Lev 23:18 / Menachot 45b:10-13 — R. Akiva\'s two orders', lambda: pesach_shavuot({'ask': 'the_second_set'}, DATA), 'two sets — [2, 1, 7] for the day, [7, 1, 2] for the bread'),
    ('Menachot 45b:6, 45b:11 — Numbers\' set in the wilderness', lambda: pesach_shavuot({'ask': 'wilderness_set'}, DATA), 'Numbers\' set in the wilderness — the tape\'s own claim'),
    ('Num 28:31 / Sifrei 148:2 — the libations likened', lambda: pesach_shavuot({'ask': 'libations_likened'}, DATA), 'the libations likened — unblemished as the animals'),
    ('Mishnah Menachot 4:3; Menachot 45b:3-7 — the loaves and the lambs', lambda: pesach_shavuot({'ask': 'loaves_and_lambs'}, DATA), 'the bread blocks the lambs — R. Akiva'),
    ('Chagigah 17a:5; Rosh Hashanah 4b:15 — seven days of redress', lambda: pesach_shavuot({'ask': 'redress_days'}, DATA), 'seven days of redress — Pesach\'s analogy'),
    ('Mishnah Chagigah 2:4 (17a:3) — the day of slaughter', lambda: pesach_shavuot({'ask': 'day_of_slaughter'}, DATA), 'a day of slaughter after Shabbat — the festival\'s one-day tail'),
    ('Beitzah 20b:11 — the loaves\' baking overrides neither', lambda: pesach_shavuot({'ask': 'loaves_baking'}, DATA), 'the loaves baked before the day — no override'),
    ('Menachot 45a:21-45b:1 — R. Shimon: one with its libations', lambda: pesach_shavuot({'ask': 'availability_libations'}, DATA), 'one with its libations before seven without'),
    # F5 — Tishri
    ('Num 29:1 / Rosh Hashanah 33b:10-11; Lev 23:24 by CALL — a day of teruah', lambda: tishri({'ask': 'day_of_blowing'}, DATA), 'a day of teruah — the sound the verse\'s, the shofar the Jubilee\'s'),
    ('Rosh Hashanah 34a:10-11 — 29:1 in the shofar\'s count', lambda: tishri({'ask': 'teruah_count'}, DATA), '29:1 comes for its own statement — the third terua rabbinic'),
    ('Rosh Hashanah 34a:12 — by day, not at night', lambda: tishri({'ask': 'by_day'}, DATA), 'by day, not at night'),
    ('Num 29:2 — the table [1, 1, 7]', lambda: tishri({'ask': 'the_tishri_table'}, DATA), 'one bull, one ram, seven lambs — the table [1, 1, 7]'),
    ('Num 29:6 / Arakhin 13a:10 — the stack: sixteen lambs', lambda: tishri({'ask': 'the_stack'}, DATA), 'the stack — sixteen lambs on the first of Tishri'),
    ('Num 29:7 / Yoma 76a:11; Lev 23:27-32 by CALL — the tenth', lambda: tishri({'ask': 'the_tenth'}, DATA), 'the tenth — afflict, all work barred; the five afflictions'),
    ('Num 29:11 / Mishnah Shevuot 1:3; Shevuot 10a:21 — the outer goat beside the inner (the Yoma engine by CALL)', lambda: tishri({'ask': 'atonements_goat'}, DATA), 'the outer goat beside the inner — the routing table\'s outer-goat-and-day'),
    ('Num 29:8 / Yoma 3a:4, 70b:9 — the rams one or two', lambda: tishri({'ask': 'yk_rams'}, DATA), 'one ram — Lev 16:5\'s and 29:8\'s the same (Rebbi)'),
    ('Yoma 70a-70b — the Day\'s musaf order', lambda: tishri({'ask': 'musaf_order'}, DATA), 'the Day\'s musaf order — a recorded dispute'),
    ('Num 29:1, 29:7 / Lev 23 by CALL — the two classes', lambda: tishri({'ask': 'convocation'}, DATA), 'servile at the first, all work at the tenth — the classes by call'),
    ('Mishnah Rosh Hashanah 4:7-8 — the blowing at the musaf; its facilitators barred', lambda: tishri({'ask': 'shofar_on_sabbath'}, DATA), 'the blowing at the musaf; its facilitators barred'),
    # F6 — Sukkot and the eighth
    ('Num 29:12 / Lev 23:34-36 by CALL — the dates', lambda: sukkot({'ask': 'the_dates'}, DATA), 'the fifteenth, seven days, the eighth an assembly — Leviticus 23 by call'),
    ('Num 29:13-32 / Sukkah 55b:9 — seventy bulls', lambda: sukkot({'ask': 'the_declining_bulls'}, DATA), 'seventy bulls — thirteen down to seven'),
    ('Num 29:14-15 / Num 15 by CALL — the master row multiplied', lambda: sukkot({'ask': 'the_multiplied_table'}, DATA), 'the master row multiplied — the multipliers written once'),
    ('Num 29:18-37 — the pointer line (computed)', lambda: sukkot({'ask': 'the_pointer_line'}, DATA), 'by their number according to the ordinance — the pointer line six times, internal'),
    ('Num 29:19, 29:31, 29:33 / Taanit 2b:14; Shabbat 103b:12 — the three letters (M-28)', lambda: sukkot({'ask': 'the_water_libation'}, DATA), 'the three letters spell water — the libation\'s four sources a parameter'),
    ('Taanit 3a:3-7; Sukkah 34a:2 — seven days, three log', lambda: sukkot({'ask': 'water_days'}, DATA), 'seven days, three log — the received rule'),
    ('Taanit 2b:3-9 — the rain\'s mention', lambda: sukkot({'ask': 'rain_mention'}, DATA), 'the rain mentioned from the eighth\'s last prayer'),
    ('Num 29:35-36 / Sukkah 47a:8, 48a:1 — the eighth its own festival', lambda: sukkot({'ask': 'the_eighth'}, DATA), 'the eighth its own festival — one bull, [1, 1, 7]'),
    ('Num 29:35 / Sukkah 47a:9 — the head without the vav (computed)', lambda: sukkot({'ask': 'eighth_head'}, DATA), 'the eighth\'s head without the vav — its own festival'),
    ('Mishnah Menachot 12:4 by CALL — sixty-one tenths', lambda: sukkot({'ask': 'sukkot_sabbath'}, DATA), 'sixty-one tenths on a Sukkot Sabbath — by call'),
    ('Num 29:35 / Sifrei 151:1; Chagigah 17a:9 — the stay', lambda: sukkot({'ask': 'stay'}, DATA), 'an assembly — withheld overnight after the festival'),
    ('Num 29:15 / Menachot 87b:5 — the dotted tenth', lambda: sukkot({'ask': 'dotted_tenth'}, DATA), 'the dotted tenth at 29:15 — a mark to check on the store'),
    ('Sukkah 55b:8-9 — seventy nations; seventy over twenty-four', lambda: sukkot({'ask': 'seventy_nations'}, DATA), 'seventy for the seventy nations — twenty-two watches thrice, two twice'),
    ('Lev 1 and Lev 4 by CALL — the rite', lambda: sukkot({'ask': 'the_rite'}, DATA), 'the bulls wholly to the fire; the goat eaten by the male priests — by call'),
    ('Mishnah Sukkah 5:6; Sukkah 55b:1-2 — the watches\' division (computed)', lambda: sukkot({'ask': 'watches_division'}, DATA), 'the watches\' shares a function of the table — (16, 8, 6, 2) then (15, 9, 5, 4)'),
    ('Sukkah 55b:4 — the seventh all equal', lambda: sukkot({'ask': 'watches_seventh'}, DATA), 'the seventh day every watch one offering'),
    ('Sukkah 55b:5 — the eighth\'s bull', lambda: sukkot({'ask': 'watches_eighth'}, DATA), 'the eighth\'s bull by lot or to a twice-watch — a recorded dispute'),
    ('Mishnah Taanit 4:2; Taanit 27a:3 — the watches instituted on 28:2', lambda: sukkot({'ask': 'watches_institution'}, DATA), 'the watches instituted on "you shall keep" — the people stand by their offering'),
    # F7 — the calendar as one table
    ('Num 29:39 / Sifrei 152:1 — these in your appointed times', lambda: the_calendar({'ask': 'these_you_shall_do'}, DATA), 'these in your appointed times — the fixed table; the vows besides'),
    ('Num 28:15-29:38 / Mishnah Shevuot 1:4-5 — the thirteen goats (computed)', lambda: the_calendar({'ask': 'the_thirteen_goats'}, DATA), 'thirteen goats — one, three, nine by the grammar; the jobs the tannaim\'s'),
    ('Shevuot 9b:2, 10a:8, 10a:11 — the vav of "and a goat" (computed)', lambda: the_calendar({'ask': 'goat_vav'}, DATA), 'eleven with the vav, two without — Shavuot\'s and Yom Kippur\'s, as the Talmud says'),
    ('Shevuot 2b:4, 12b:3-4 — the interchange ring', lambda: the_calendar({'ask': 'interchange'}, DATA), 'the goats interchange — one genus, the species by the knife'),
    ('Num 28:23-29:38 / Sifrei 147:1 — besides twelve times (computed)', lambda: the_calendar({'ask': 'besides_twelve'}, DATA), 'besides twelve times — the tamid first, the musaf beside it'),
    ('Menachot 49b:5; Arakhin 13a:10; Sukkah 55b:8 — the sums', lambda: the_calendar({'ask': 'the_sums'}, DATA), 'the sums — 16, 22, 70, 13: the tables\' arithmetic'),
    ('Sifrei 143:2; Menachot 110a — ben Azzai\'s census (computed)', lambda: the_calendar({'ask': 'ben_azzai_census'}, DATA), 'the special Name only as the addressee — zero in the span, two non-addressee seats in Leviticus 1-7'),
    ('Rosh Hashanah 5a:4 — the eight period timers', lambda: the_calendar({'ask': 'timers'}, DATA), 'eight period timers — sabbath, month, passover_1, atzeret, rosh_hashanah, yom_kippur, sukkot_1, shemini'),
    ('Berakhot 26a:17 — its day passed, its sacrifice is invalid', lambda: the_calendar({'ask': 'its_day_passed'}, DATA), 'a missed day is not a carried debt — the debit lapses'),
    ('Chagigah 18a:6 — the musaf a sanctity marker', lambda: the_calendar({'ask': 'sanctity_marker'}, DATA), 'the musaf a sanctity marker — the tradition\'s own scale'),
    ('Menachot 110a:9; Sukkah 51a:12-13 — the run in Chronicles', lambda: the_calendar({'ask': 'run_in_writings'}, DATA), 'the calendar RUN in Chronicles — four tiers, the song, the trumpets'),
    ('Beitzah 19b:8-13 — the vow deadline', lambda: the_calendar({'ask': 'vow_deadline'}, DATA), 'three festivals in any order — the first tanna'),
    ('Num 28:8, 29:18-37 — the nine pointers, all internal (computed)', lambda: the_calendar({'ask': 'pointers'}, DATA), 'nine pointers, all internal — the master row and the tamid'),
    ('THE REGISTER GATE — no seat in 28-29', lambda: the_calendar({'ask': 'the_register_gate'}, DATA), 'no register seat in 28-29 — the gate\'s print the check'),
    ('Num 29:39 / Lev 7 by CALL — the vowed peace offerings', lambda: the_calendar({'ask': 'peace_offerings'}, DATA), 'the vowed peace offerings — two days and a night by call'),
    # THE NUMBERS from the ink (the parser at every seat; the tables' arithmetic)
    ('THE PARSER — the three [2, 1, 7] tables and the three [1, 1, 7]', lambda: ((T_MONTH, T_PESACH, T_SHAVUOT, T_RH, T_YK, T_EIGHTH), [FX.NONE], [('INK', 'Num 28:11, 28:19, 28:27, 29:2, 29:8, 29:36 — the parser')]), ([2, 1, 7], [2, 1, 7], [2, 1, 7], [1, 1, 7], [1, 1, 7], [1, 1, 7])),
    ('THE PARSER — Sukkot\'s seven days', lambda: (SUKKOT, [FX.NONE], [('INK', 'Num 29:13-32 — the parser at the seven heads')]), [[13, 2, 14], [12, 2, 14], [11, 2, 14], [10, 2, 14], [9, 2, 14], [8, 2, 14], [7, 2, 14]]),   # the first graded run typed a tuple for the parser's list — the one miss of 109/110, retyped from the print
    ('THE SUMS — seventy bulls, fourteen rams, ninety-eight lambs; thirteen goats', lambda: ((BULLS_70, RAMS_14, LAMBS_98, len(GOATS)), [FX.NONE], [('INK', 'Num 29:13-32; 28:15-29:38 — computed')]), (70, 14, 98, 13)),
    ('THE STACKS — sixteen on Tishri\'s first (Arakhin 13a:10), twenty-two for Shabbat and the two days of Rosh Hashanah (Menachot 49b:5)', lambda: ((LAMBS_TISHRI_1, LAMBS_THREE_DAYS), [FX.NONE], [('INK', 'Num 28:3, 28:9, 28:11, 29:2 — computed')]), (16, 22)),
    ('THE PARSER — Leviticus 23:18 against 28:27', lambda: ((LEV_SET, T_SHAVUOT), [FX.NONE], [('INK', 'Lev 23:18; Num 28:27 — the parser at both seats')]), ([7, 1, 2], [2, 1, 7])),
    ('THE PARSER — the dates (the month-ordinals apart)', lambda: ((DATE_PESACH, DATE_MATZOT, DATE_RH, DATE_YK, DATE_SUKKOT), [FX.NONE], [('INK', 'Num 28:16, 28:17, 29:1, 29:7, 29:12 — the parser (rule 26 at 29:7)')]), ([14], [15, 7], [1], [10], [15, 7])),
    ('THE TOKEN CENSUS — besides, ordinance, their ordinance, by their number, the continual, without blemish', lambda: ((len(BESIDES), len(ORDINANCE), len(THEIR_ORDINANCE), len(BY_NUMBER), len(CONTINUAL), len(BLEMISH)), [FX.NONE], [('INK', 'Num 28-29 — computed')]), (12, 6, 2, 7, 15, 15)),
    ('THE TOKEN CENSUS — to the LORD, their libations, its libations, to atone, these', lambda: ((len(TO_LORD), len(THEIR_LIB), len(ITS_LIB_F), len(TO_ATONE), len(THESE)), [FX.NONE], [('INK', 'Num 28-29 — computed')]), (19, 11, 1, 3, 2)),
    ('THE GOATS\' VAV — two bare, at Shavuot and Yom Kippur (Shevuot 10a:11)', lambda: ((len(GOAT_VAV), GOAT_BARE, GOAT_TO_LORD), [FX.NONE], [('INK', 'Num 28:15-29:38 — computed')]), (11, [(28, 30), (29, 11)], [(28, 15)])),
    ('THE EIGHTH\'S HEAD — six with the vav, the eighth without (Sukkah 47a:9)', lambda: ([h for _, h in HEADS], [FX.NONE], [('INK', 'Num 29:17-35 — computed')]), ['וביום', 'וביום', 'וביום', 'וביום', 'וביום', 'וביום', 'ביום']),
    ('THE THREE LETTERS — mem, yod, mem = water (M-28)', lambda: ((LETTERS, PLAIN, MAYIM), [FX.NONE], [('INK', 'Num 29:19, 29:31, 29:33 against 29:16, 29:22, 29:18 — computed')]), (('ונסכיהם', 'ונסכיה', 'כמשפטם'), ('ונסכה', 'ונסכה', 'כמשפט'), 'מים')),
    ('BEN AZZAI\'S CENSUS — the other names: none in the span, two non-addressee seats in Leviticus 1-7, no offering "to God" (read off the first run\'s print)', lambda: ((NAMES_SPAN[1], [(c, v) for c, v, _ in NAMES_LEV[1]], ADDRESSEE_OTHER), [FX.NONE], [('INK', 'Num 28-29; Lev 1-7 — computed')]), ([], [(2, 13), (4, 22)], [])),
    ('THE WATCHES\' DIVISION — days one, two and seven; seventy over twenty-four', lambda: ((WD[0], WD[1], WD[6], SEVENTY_SPLIT), [FX.NONE], [('INK', 'Num 29:13-32 — the function computed')]), ((16, 8, 6, 2), (15, 9, 5, 4), (10, 14, 0, 14), (2, 22))),
    ('THE SHELACH RUNNER\'s master row — the logs and sixty-one (by CALL)', lambda: ((SH_LOGS, SH_61, SH_MONTH_ROW == MONTH_ROW), [FX.NONE], [('MOVE', 'CALLED cold_run_shelach')]), ({'lamb': (3, 3), 'ram': (4, 4), 'bull': (6, 6)}, 61, True)),
    ('THE INCENSE-SHEKEL RUNNER\'s tamid — the minimum, the log, the Sabbath tokens (by CALL)', lambda: ((TAMID['plural_minimum'], TAMID['three_log'], TAMID['sabbath_overrides'] == words(28, 10)[:6]), [FX.NONE], [('MOVE', 'CALLED cold_run_incense_shekel.tamid')]), (2, 3, True)),
    ('THE MOADIM RUNNER\'s dates and classes (by CALL)', lambda: ((MO_PASS['date']['v'], MO_RH['date']['v'], MO_SUK['date']['v'], MO_SUK['eighth']['v'], MO_WORK['passover_1'], MO_WORK['yom_kippur']), [FX.NONE], [('MOVE', 'CALLED cold_run_moadim')]), ('14th_of_1st', '1st_of_7th', '15th_of_7th', 'atzeret', 'servile_only', 'all_work')),
    ('THE YOMA RUNNER\'s routing table (by CALL)', lambda: ((ROUTE_NONE['agent'], ROUTE_END['agent'], len(ORDER)), [FX.NONE], [('MOVE', 'CALLED cold_run_yoma.route')]), ('festival_and_new_moon_goats', 'outer_goat_and_day', 18)),
    ('THE MINCHAH RUNNER\'s omer, oil and salt (by CALL)', lambda: ((OMER_SRC, OIL_GRADE, SALT), [FX.NONE], [('MOVE', 'CALLED cold_run_minchah')]), ('new_and_from_the_land', 'not_required_pure_beaten', 'required')),
    ('THE TABLES the daemon sets — eight keys', lambda: (TABLES, [FX.NONE], [('INK', 'Num 28:9, 28:11, 28:19, 28:27, 29:2, 29:8, 29:13, 29:36 — the parser')]),
     {'sabbath': (0, 0, 2, 0), 'month': (2, 1, 7, 1), 'passover_1': (2, 1, 7, 1), 'atzeret': (2, 1, 7, 1), 'rosh_hashanah': (1, 1, 7, 1), 'yom_kippur': (1, 1, 7, 1), 'sukkot_1': (13, 2, 14, 1), 'shemini': (1, 1, 7, 1)}),
    # THE WRAP: the scene on the world engine
    ('THE SCENE on the world engine — the wrap: twenty-six of the exam\'s persons through the seven case kinds; no timer on the bench (no command line submitted there)',
     lambda: (SCENE, [FX.NONE], [('INK', 'Num 28:1-29:39 — the recorded rows replayed')]),
     (1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 26, 0)),
    ('THE NARRATIVE on the world engine — the one line; EIGHT PERIOD TIMERS set, none fired (the tripwire typed from the first run)',
     lambda: (NARRATIVE, [FX.NONE], [('INK', 'Num 28:1-29:39 — the one line')]),
     (8, 0, 8, ['sabbath', 'month', 'passover_1', 'atzeret', 'rosh_hashanah', 'yom_kippur', 'sukkot_1', 'shemini'], [(6, 8), (7, 1), (1, 15), (3, 6), (7, 1), (7, 10), (7, 15), (7, 22)], ['NOT FOUND'], 1, (6, 1))),
]

if __name__ == '__main__':
    ok = 0
    frac = {'INK': 0, 'MOVE': 0, 'DATA': 0, 'HYP': 0}
    used_effects = []
    print()
    for label, fn, want in CASES:
        got, effects, prov = fn()
        hit = got == want
        ok += hit
        kinds = [k for k, _ in prov]
        cls = 'HYP' if 'HYP' in kinds else ('INK' if all(k == 'INK' for k in kinds) else ('MOVE' if 'MOVE' in kinds else 'DATA'))
        frac[cls] += 1
        print('%s  [%s]  %s' % ('PASS' if hit else 'MISS', cls, label))
        if not hit:
            print('      expected: %s' % (want,))
            print('      got     : %s' % (got,))
        used_effects += effects
        for line in FX.render(effects):
            print('        ->%s' % line)
    print()
    print('WATCH COVERAGE (the wrap):')
    _W.print_coverage()
    print('MATRIX: %d/%d cells match the answer sheet' % (ok, len(CASES)))
    tot = len(CASES)
    print('FRACTIONS: pure ink %d/%d (%.0f%%) · named moves %d/%d (%.0f%%) · data %d/%d (%.0f%%) · hypotheses %d/%d (the H class, counted apart — never as compiled)' %
          (frac['INK'], tot, 100.0 * frac['INK'] / tot, frac['MOVE'], tot, 100.0 * frac['MOVE'] / tot, frac['DATA'], tot, 100.0 * frac['DATA'] / tot, frac['HYP'], tot))
    ops = FX.summarize(used_effects)
    print('LEDGER OPS this span writes:', ', '.join('%s x%d' % kv for kv in sorted(ops.items())))
    print('THE TABLES from the ink: %s; Sukkot %s; the sums %d bulls, %d rams, %d lambs, %d goats; the stacks %d and %d; the master row %s (tenths %s)' %
          (TABLES, SUKKOT, BULLS_70, RAMS_14, LAMBS_98, len(GOATS), LAMBS_TISHRI_1, LAMBS_THREE_DAYS, [str(x) for x in MONTH_ROW], TENTHS_12))
    print('THE TOKEN CENSUSES: besides %d, ordinance %d + %d, by their number %d, the continual %d, without blemish %d, to the LORD %d, their libations %d, its libations %d, to atone %d, these %d; the goats\' vav %d / bare %s; the heads %s; the letters %s = %s; the Names %s / Lev 1-7 %s' %
          (len(BESIDES), len(ORDINANCE), len(THEIR_ORDINANCE), len(BY_NUMBER), len(CONTINUAL), len(BLEMISH), len(TO_LORD), len(THEIR_LIB), len(ITS_LIB_F), len(TO_ATONE), len(THESE), len(GOAT_VAV), GOAT_BARE, [h for _, h in HEADS], LETTERS, MAYIM, NAMES_SPAN, NAMES_LEV))
    print('THE TIMERS on the narrative world: %d set, %d pending — %s' % (NARRATIVE[0], NARRATIVE[2], list(zip(NARRATIVE[3], NARRATIVE[4]))))
    print('THE PARAMETER ROWS: ' + '; '.join('%s = %s' % (k, DATA[k]['value']) for k in DATA) + ' (the other settings recorded in DATA)')
    if ok == len(CASES):
        print('\nTHE OFFERINGS CALENDAR COMPILES — one speech as one table: the tamid by call, the master row by call, the tables by the parser, the thirteen goats with their vav, the three letters as a checked row, the watches as a function, eight period timers on the altar.')

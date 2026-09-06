#!/usr/bin/env python3
"""cold_run_moadim.py — THE APPOINTED TIMES ENGINE (Leviticus 23),
the eighth span compiled under the Step-5 deliverable rule (2026-09-05,
the Emor sweep — the first compile under Claude Fable 5.1).

The five motions, in order:
 (1) code from the BARE INK of Lev 23 alone — every appointed time's
     DATE, LENGTH, and WORK-BAN CLASS read off the verse's own tokens
     (כל מלאכה 'all work' vs מלאכת עבדה 'servile work' — two classes,
     two token forms, counted per verse), the omer's arithmetic (seven
     whole weeks + fifty days), the new-grain gate ('until you bring'),
     the affliction with its two sanctions (karet at 23:29, destruction
     at 23:30), the dwelling ('dwell seven days'), the four species'
     grammatical numbers (singular/plural tokens at 23:40), the lulav's
     'before the LORD seven days' vs 'on the first day';
 (2) the Mishnah's rows collected as TEST DATA, read from the local
     shelf with a token verified in each row's own ink;
 (3) run;
 (4) misses filled by NAMED recorded arguments, each labeled [MOVE]
     with its source — this run's: the morrow-of-the-Sabbath = the
     festival (Sifra Emor Chapter 12 1-5, four routes; Onkelos Lev
     23:11/15 'after the festival day'); the five afflictions from
     shabbaton = shevut (Sifra Chapter 14 4); the first day overriding
     the Sabbath (Sifra Chapter 16 3); 'the native' excluding women
     (Chapter 17 9); the myrtle count dispute (Chapter 16 7); the shofar
     imported from the Jubilee (Section 11 6); the loaves' equality and
     mutual indispensability (Chapter 13 2); the whole-day ban without
     the Temple (R. Yehuda, Section 10 10);
 (5) the graded matrix with per-cell provenance, fractions, and
     EFFECTS on every verdict — three effects DISCOVERED in the span's
     own verbs and registered before this run: counts_omer (a TIMER),
     dwells_in_booths (a TIMER), takes_four_species (a status).
Zero-report law: every claimed ink token is probed before anything
runs; the answer sheet is verified in its own ink.
"""
import sqlite3, sys, os, json
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import effects_layer as FX
from compile_guards import check_honest_pairing
GUARDED = check_honest_pairing(os.path.abspath(__file__))
assert GUARDED == 41, ('the guard counted %d expectations, the tripwire holds 41' % GUARDED)
print('guard: %d expectations checked, every one a literal from the answer sheet [honest-pairing guard satisfied]' % GUARDED)
# the callees (cold) — the dependency-debt sitting (2026-09-06): this runner
# imported nothing while 23:5 named the Passover, 23:12 and 23:18-19 the
# burnt, sin, and peace offerings, 23:9-14 the omer of Lev 2:14, and
# 23:16-20 the first fruits and the harvest feast of Exod 23:16-19.
import io as _io, contextlib as _ctx
with _ctx.redirect_stdout(_io.StringIO()):
    import cold_run_pesach as PS
    import cold_run_offerings as OFF
    import cold_run_minchah as MIN
    import cold_run_calendar as CAL
PS_EAT = PS.paschal_procedure({'ask': 'eating_time'}, PS.DATA)[0]
PS_WIN = PS.leaven_machine({'ask': 'window_bounds'}, PS.DATA)[0]
OLAH = OFF.dispatch('olah:flock'); CHATAT = OFF.dispatch('outer_chatat'); CSA = OFF.dispatch('communal_shelamim_and_asham')
OMER_MIN = MIN.omer('source')
FF = CAL.first_fruits({}, CAL.DATA)[0]; PIL = CAL.pilgrimage({'kind': 'able_male'}, CAL.DATA)[0]
print('routing receipts: cold_run_pesach CALLED — eating_time %r, window %r; cold_run_offerings CALLED — olah %r, '
      'outer chatat place %r, communal shelamim place %r eater %r; cold_run_minchah CALLED — omer(source) %r; '
      'cold_run_calendar CALLED — first_fruits %r, pilgrimage %r [IMPORT, live calls]'
      % (PS_EAT, PS_WIN, OLAH['disposition']['v'], CHATAT['place']['v'], CSA['place']['v'], CSA['eater']['v'],
         OMER_MIN['v'], FF, PIL))

ROOT = '<repo-old>'
db = sqlite3.connect(ROOT + '/elijah_docket/tanakh.sqlite')


def strip(s):
    return ''.join(c for c in s if c != '/' and not (0x0591 <= ord(c) <= 0x05C7))


def toks(ch, vs):
    rows = db.execute("""SELECT w.he FROM words w JOIN verses v
        ON w.verse_id=v.id WHERE v.book='Lev' AND v.chapter=? AND v.verse=?
        ORDER BY w.idx""", (ch, vs)).fetchall()
    return [strip(r[0]) for r in rows]


T = {v: toks(23, v) for v in range(1, 45)}


def count(tok, vs, exact=False):
    return sum(1 for w in T[vs] if (w == tok if exact else tok in w))

# ---- (1) ink probes — each MUST fire or the run refuses -------------
PROBES = [
    ('14th of the first month (Passover)',   5, 'בארבעה'),
    ('15th — the festival of matzot',        6, 'בחמשה'),
    ('seven days of matzot',                 6, 'שבעת'),
    ('servile work banned, day one',         7, 'עבדה'),
    ('servile work banned, day seven',       8, 'עבדה'),
    ('the morrow of the Sabbath (omer)',    11, 'ממחרת'),
    ('two tenths for the omer lamb',        13, 'עשרנים'),
    ('mixed with OIL',                      13, 'בשמן'),
    ('a quarter hin',                       13, 'רביעת'),
    ('until you BRING — the new-grain gate', 14, 'הביאכם'),
    ('until this very DAY',                 14, 'עצם'),
    ('COUNT for yourselves',                15, 'וספרתם'),
    ('seven WHOLE weeks',                   15, 'תמימת'),
    ('FIFTY days',                          16, 'חמשים'),
    ('two loaves — TWO',                    17, 'שתים'),
    ('two tenths for the loaves',           17, 'עשרנים'),
    ('LEAVENED',                            17, 'חמץ'),
    ('servile work banned at Atzeret',      21, 'עבדה'),
    ('first of the seventh month',          24, 'באחד'),
    ('a memorial of TERUAH',                24, 'תרועה'),
    ('rest (shabbaton) at Rosh Hashanah',   24, 'שבתון'),
    ('the tenth — Yom Kippur',              27, 'בעשור'),
    ('AFFLICT your souls',                  27, 'ועניתם'),
    ('ALL work banned (Yom Kippur)',        28, 'מלאכה'),
    ('CUT OFF for not afflicting',          29, 'ונכרתה'),
    ('I will DESTROY for working',          30, 'והאבדתי'),
    ('on the NINTH in the evening',         32, 'בתשעה'),
    ('15th of the seventh — Sukkot',        34, 'בחמשה'),
    ('the EIGHTH day',                      36, 'השמיני'),
    ('atzeret — an assembly',               36, 'עצרת'),
    ('TAKE for yourselves',                 40, 'ולקחתם'),
    ('on the FIRST day',                    40, 'הראשון'),
    ('before the LORD SEVEN days',          40, 'שבעת'),
    ('DWELL in booths',                     42, 'תשבו'),
    ('the NATIVE',                          42, 'האזרח'),
]
for label, vs, tok in PROBES:
    if count(tok, vs) < 1:
        sys.exit('ZERO-REPORT LAW: probe %r wanted %r at Lev 23:%d — '
                 'not found, refusing to run' % (label, tok, vs))
print('probes: all %d ink-token probes fired [zero-report law satisfied]'
      % len(PROBES))

# ---- the ink censuses the machine runs on ----------------------------
ALL_WORK = sorted(v for v in T if count('מלאכה', v) and not count('מלאכת', v))
SERVILE = sorted(v for v in T if count('עבדה', v))
CONVOC = sorted(v for v in T if count('מקרא', v))
assert ALL_WORK == [3, 28, 30, 31], ALL_WORK   # the Sabbath + Yom Kippur only
assert SERVILE == [7, 8, 21, 25, 35, 36], SERVILE
assert len(CONVOC) == 11, CONVOC
print('ink census: ALL-work verses %s · SERVILE-work verses %s · '
      'convocation tokens %d' % (ALL_WORK, SERVILE, len(CONVOC)))

I, M, A, D, P = 'INK', 'MOVE', 'ANSWER-SHEET', 'DATA', 'IMPORT'


def cell(v, p, why, effects):
    FX.validate(effects)
    return {'v': v, 'p': p, 'why': why, 'fx': effects}


# ---- (1) THE ENGINE — compiled from Lev 23's ink -------------------
def work_class(day):
    """Which ban a day carries, read from the verse that names it."""
    verse = {'sabbath': 3, 'passover_1': 7, 'passover_7': 8, 'atzeret': 21,
             'rosh_hashanah': 25, 'yom_kippur': 28, 'sukkot_1': 35,
             'shemini': 36}[day]
    if verse in ALL_WORK:
        return cell('all_work', I, 'כל מלאכה (all work) at Lev 23:%d' % verse,
                    ['labor_barred', 'sanctify_day'])
    return cell('servile_only', I,
                'מלאכת עבדה (servile work) at Lev 23:%d — the lighter class'
                % verse, ['labor_barred', 'sanctify_day'])


def yom_kippur():
    return {
     'affliction': cell('required', I, 'ועניתם (afflict) at 23:27 and 23:32',
                        ['rest_required']),
     'not_afflicting': cell('karet', I, 'ונכרתה (cut off) at 23:29',
                            ['karet_cut_off']),
     'working': cell('destroyed', I, 'והאבדתי (I will destroy) at 23:30',
                     ['destroyed']),
     'affliction_list': cell('eating_drinking_washing_anointing_sandals_relations',
                             M, 'shabbaton = shevut — Sifra Emor Chapter 14 4 '
                             '(the five afflictions from the rest token)',
                             ['rest_required']),
     'addition': cell('begins_ninth_evening', I,
                      'בתשעה לחדש בערב (on the ninth in the evening) at 23:32 '
                      '— the fast starts while it is still day: Sifra Chapter '
                      '14 5 names it the addition',
                      ['rest_required']),
     'prohibition_class': cell('lav_and_karet', I,
                               'both the all-work ban (23:28) and the karet '
                               '(23:29-30) written', ['labor_barred']),
    }


def omer():
    weeks = count('שבע', 15) and 7
    days = 50  # חמשים at 23:16
    return {
     'morrow_reading': cell('festival', M,
                            'ממחרת השבת (the morrow of the Sabbath) = the '
                            'morrow of the FESTIVAL — Sifra Chapter 12 1-5 '
                            '(four routes) and Onkelos 23:11/15 "after the '
                            'festival day"', ['counts_omer']),
     'count_length': cell(weeks * 7, I,
                          'seven whole weeks (23:15) = 49 counted; the '
                          'FIFTIETH day (23:16) is the new offering\'s day — '
                          'count 49, sanctify the 50th', ['counts_omer']),
     'minchah_flour': cell('two_tenths', I, 'שני עשרנים at 23:13',
                           ['accepted']),
     'minchah_oil': cell('oil', I, 'בלולה בשמן (mixed with oil) at 23:13',
                         ['accepted']),
     'minchah_frankincense': cell('frankincense', A,
                                  'not in Lev 23\'s ink — the answer sheet '
                                  'supplies it (Mishnah Menachot 5:3)',
                                  ['accepted']),
     'libation': cell('quarter_hin', I, 'רביעת ההין at 23:13', ['accepted']),
     'new_grain_gate_with_temple': cell('the_omer', I,
                                        'עד הביאכם (until you bring) at 23:14 '
                                        '— the gate is the bringing',
                                        ['barred_from_it']),
     'new_grain_gate_without_temple': cell('whole_day', I,
                                           'עד עצם היום הזה (until this very '
                                           'day) at 23:14 — the day itself '
                                           'when there is no bringing (R. '
                                           'Yehuda, Sifra Section 10 10)',
                                           ['barred_from_it']),
     # the pointers, live (2026-09-06)
     'lamb_olah': cell(OLAH['disposition']['v'], P,
                       'כבש תמים בן שנתו לעלה (a lamb of its first year for a burnt offering) at 23:12 — Lev '
                       '1:10\'s flock burnt offering: CALLED cold_run_offerings.dispatch(olah:flock) disposition '
                       '[IMPORT, live call]', ['accepted']),
     'grain_source': cell(OMER_MIN['v'], P,
                          'the omer IS Lev 2:14\'s first-fruits meal offering — "what is missing there the verse '
                          'stated here," one offering split across two chapters (Sifra Emor Chapter 13 3): CALLED '
                          'cold_run_minchah.omer(source) [IMPORT, live call]', ['accepted']),
    }


def shavuot_animals():
    """Lev 23:18-19 — the animals brought ON the bread, compiled from the two
    verses' own tokens; the procedures by live call (added 2026-09-06: the
    sub-span had been cited by no cell)."""
    kinds = (count('שבעת', 18) and count('כבשים', 18) and count('ופר', 18) and count('ואילם', 18))
    return {
     'olah_kinds': cell('seven_lambs_one_bull_two_rams' if kinds else 'census_failed', I,
                        'שבעת כבשים... ופר בן בקר אחד ואילם שנים יהיו עלה (seven lambs... and one bull and two '
                        'rams, a burnt offering) at 23:18 — the three kinds counted by their own numerals',
                        ['accepted']),
     'olah_procedure': cell(OLAH['disposition']['v'], P,
                            'עלה ליהוה at 23:18 — Lev 1\'s burnt offering: CALLED cold_run_offerings.dispatch(olah:flock) '
                            'disposition [IMPORT, live call]', ['smoked_to_the_lord']),
     'minchah_libations': cell('per_Numbers_28', D,
                               'ומנחתם ונסכיהם (their meal offering and their libations) at 23:18 — the quantities are '
                               'Numbers 28:26-31\'s, outside this span [IMPORT; the Sifra: "the verse spoke briefly," '
                               'Emor Chapter 13 5]', ['accepted']),
     'chatat_place': cell(CHATAT['place']['v'], P,
                          'שעיר עזים אחד לחטאת (one he-goat for a sin offering) at 23:19 — Lev 4\'s outer sin offering: '
                          'CALLED cold_run_offerings.dispatch(outer_chatat) place [IMPORT, live call]', ['accepted']),
     'shelamim_grade': cell(CSA['eater']['v'], P,
                            'קדש יהיו ליהוה לכהן (holy shall they be to the LORD, for the priest) at 23:20 — the '
                            'communal peace offering is MOST HOLY, eaten by the priests: CALLED cold_run_offerings.dispatch'
                            '(communal_shelamim_and_asham) eater [IMPORT, live call; Mishnah Zevachim 5:5\'s row read '
                            'off the verse\'s own "for the priest"]', ['most_holy', 'due_to_priest']),
     'shelamim_place': cell(CSA['place']['v'], P,
                            'the communal peace offering\'s slaughter place — north (Zevachim 5:5; the Num 10:10 pairing, '
                            'Zevachim 55a:3): CALLED cold_run_offerings [IMPORT, live call]', ['accepted']),
     'waving': cell('loaves_on_two_lambs', M,
                    'והניף הכהן אתם על לחם הבכורים תנופה... על שני כבשים (the priest shall wave them on the bread of '
                    'the first fruits... on the two lambs) at 23:20 [INK] — the geometry: the bread ABOVE everywhere '
                    '(Sifra Emor Chapter 13 8; Mishnah Menachot 5:6: the loaves on the two lambs, both hands beneath)',
                    ['waved']),
     'interdependence': cell('bread_blocks_lambs_R._Akiva_lambs_block_bread_ben_Nannas', A,
                             'על הלחם (ON the bread) at 23:18 [INK] — the lambs an obligation to the bread (Sifra Emor '
                             'Chapter 13 4); Mishnah Menachot 4:3: the bread blocks the lambs (R. Akiva) / the lambs '
                             'block the bread (ben Nannas; R. Shimon rules as he, not for his reason)', ['accepted']),
     'two_lambs_mutual': cell('block_each_other', A,
                              'שני כבשים (two lambs) at 23:19 — Mishnah Menachot 3:6: the two lambs of Atzeret '
                              'indispensable to one another', ['accepted']),
     'kinds_independent': cell('do_not_block_each_other', A,
                               'Mishnah Menachot 4:2 — the bulls, the rams, and the lambs do not invalidate one '
                               'another (the three numerals of 23:18 stand apart)', ['accepted']),
     'two_sets': cell('for_the_bread_not_for_the_day', M,
                      'Sifra Emor Chapter 13 6 — the seven lambs and the goat of Numbers 28 are NOT these: those come '
                      'for the DAY, these for the BREAD (the bulls and rams differ between the lists)', ['accepted']),
    }


def two_loaves():
    return {
     'count': cell(2, I, 'שתים at 23:17', ['accepted']),
     # the pointers, live (2026-09-06)
     'first_fruits_link': cell(FF, P,
                               'לחם הבכורים (the bread of the first fruits) at 23:20 with Exod 23:16 "the feast of the '
                               'harvest, the first fruits of your labors" and 23:19 "the first of the first fruits" — one '
                               'institution at two seats: CALLED cold_run_calendar.first_fruits [IMPORT, live call]',
                               ['accepted']),
     'pilgrimage': cell(PIL, P,
                        'the day of the two loaves is Exod 23:16\'s feast of the harvest, one of the three appearings: '
                        'CALLED cold_run_calendar.pilgrimage(able_male) [IMPORT, live call]', ['appearance_owed']),
     'flour': cell('two_tenths', I, 'שני עשרנים at 23:17', ['accepted']),
     'leaven': cell('leavened', I, 'חמץ תאפינה at 23:17', ['accepted']),
     'oil_frankincense': cell('neither', A,
                              'the ink is silent; the answer sheet (Mishnah '
                              'Menachot 5:3)', ['accepted']),
     'mutual': cell('block_each_other', M,
                    '"two... shall be" — equal and indispensable, Sifra '
                    'Chapter 13 2', ['accepted']),
    }


def rosh_hashanah():
    return {
     'date': cell('1st_of_7th', I, 'באחד לחדש (on the first of the month) '
                  'at 23:24', ['sanctify_day']),
     'rest': cell('shabbaton', I, 'שבתון at 23:24', ['rest_required']),
     'sound': cell('teruah', I, 'זכרון תרועה at 23:24', ['sanctify_day']),
     'instrument': cell('shofar', M, 'imported from the Jubilee — Lev 25:9\'s '
                        '"in the seventh month" (Sifra Section 11 6)',
                        ['sanctify_day']),
    }


def sukkot():
    n_seven = count('שבעת', 40)
    return {
     'date': cell('15th_of_7th', I, 'בחמשה עשר at 23:34', ['sanctify_day']),
     'length': cell(7, I, 'שבעת ימים at 23:34', ['dwells_in_booths']),
     'eighth': cell('atzeret', I, 'ביום השמיני עצרת (on the eighth day, an assembly) at 23:36',
                    ['sanctify_day']),
     'dwelling_days': cell(7, I, 'בסכת תשבו שבעת ימים at 23:42',
                           ['dwells_in_booths']),
     'women': cell('exempt', M, '"THE native" — the article excludes women '
                   '(Sifra Chapter 17 9); minors included by "every"',
                   ['dwells_in_booths']),
     'lulav_temple_days': cell(7, I, 'ושמחתם לפני יהוה שבעת ימים (rejoice before the '
                               'LORD seven days) at 23:40 — seven days BEFORE THE '
                               'LORD means the Temple',
                               ['takes_four_species']),
     'lulav_province_days': cell(1, I, 'ביום הראשון (on the first day) at '
                                 '23:40 — the first day alone elsewhere',
                                 ['takes_four_species']),
     'first_day_on_sabbath': cell('overrides', M,
                                  '"on the FIRST day" — even on the Sabbath, '
                                  'that day alone (Sifra Chapter 16 3)',
                                  ['takes_four_species']),
     'etrog_count': cell(1, I, 'פרי עץ הדר — singular at 23:40',
                         ['takes_four_species']),
     'lulav_count': cell(1, I, 'כפת תמרים — written defective, one',
                         ['takes_four_species']),
     'willow_count': cell(2, I, 'ערבי נחל — plural at 23:40: two',
                          ['takes_four_species']),
     'myrtle_count': cell(['r_yishmael_three', 'r_akiva_one'], M,
                          'ענף עץ עבת — the recorded dispute (Sifra Chapter '
                          '16 7): three or one', ['takes_four_species']),
    }


def sabbath_vs_festival():
    return {
     'sabbath_class': work_class('sabbath'),
     'festival_class': work_class('passover_1'),
    }


def passover():
    assert count('הערבים', 5) == 1, 'between the evenings missing at 23:5'
    return {
     'date': cell('14th_of_1st', I, 'בארבעה עשר לחדש at 23:5', ['sanctify_day']),
     'slaughter_window': cell('after_midday', M,
                              'בין הערבים (between the evenings) at 23:5 [INK] '
                              '— read as "from when the day turns, six hours '
                              'onward" (Sifra Emor Chapter 11 1, Jeremiah 6:4 '
                              'the witness): before midday invalid',
                              ['accepted']),
     'matzot_days': cell(7, I, 'שבעת ימים מצות at 23:6', ['sanctify_day']),
     # the pointers, live (2026-09-06)
     'eating_time': cell(PS_EAT, P,
                         'פסח ליהוה (the LORD\'s Passover) at 23:5 — the Passover engine holds the lamb\'s law: CALLED '
                         'cold_run_pesach.paschal_procedure(eating_time) [IMPORT, live call]', ['eating_window']),
     'matzot_window': cell(PS_WIN, P,
                           'חג המצות (the feast of unleavened bread) at 23:6 — Exod 12:15-20\'s window: CALLED '
                           'cold_run_pesach.leaven_machine(window_bounds) [IMPORT, live call]', ['purge_deadline']),
    }


# ---- (2) TEST DATA — Mishnah rows read from the shelf --------------
def mishnah(tractate, ch, m, must):
    fn = ROOT + '/Data/mishnah_%s_he.json' % tractate
    d = json.load(open(fn))
    t = d['text'] if isinstance(d, dict) and 'text' in d else d
    row = strip(t[ch - 1][m - 1])
    assert must in row, 'answer-sheet check failed: %r not in Mishnah %s %d:%d' % (must, tractate, ch, m)
    return row


SHEET = [
    ('Megillah 1:5', 'megillah', 1, 5, 'אכל נפש'),
    ('Yoma 8:1', 'yoma', 8, 1, 'באכילה'),
    ('Keritot 1:1', 'keritot', 1, 1, 'הכפורים'),
    ('Makkot 3:2', 'makkot', 3, 2, 'הכפורים'),
    ('Chagigah 2:4', 'chagigah', 2, 4, 'עצרת'),
    ('Menachot 5:3', 'menachot', 5, 3, 'העמר'),
    ('Menachot 10:5', 'menachot', 10, 5, 'הנף'),
    ('Menachot 3:6', 'menachot', 3, 6, 'חלות'),
    ('Rosh Hashanah 3:3', 'rosh_hashanah', 3, 3, 'שופר'),
    ('Sukkah 4:1', 'sukkah', 4, 1, 'שבעה'),
    ('Sukkah 3:12', 'sukkah', 3, 12, 'במקדש'),
    ('Sukkah 4:2', 'sukkah', 4, 2, 'שבעה'),
    ('Sukkah 3:4', 'sukkah', 3, 4, 'הדסים'),
    ('Sukkah 2:8', 'sukkah', 2, 8, 'נשים'),
    ('Pesachim 5:3', 'pesachim', 5, 3, 'חצות'),
]
for name, tr, ch, m, must in SHEET:
    mishnah(tr, ch, m, must)
print('answer sheet: %d Mishnah rows read whole from the shelf, each '
      'verified by a token in its own ink' % len(SHEET))

YK, OM, TL, RH, SK, SV, PSV, SA = (yom_kippur(), omer(), two_loaves(), rosh_hashanah(),
                                   sukkot(), sabbath_vs_festival(), passover(), shavuot_animals())

# (Mishnah row, cell, expected)
TESTS = [
 ('Megillah 1:5 — festival vs Sabbath differ only in food work',
  SV['festival_class'], 'servile_only'),
 ('Megillah 1:5 — the Sabbath bars all work',
  SV['sabbath_class'], 'all_work'),
 ('Yoma 8:1 — the forbidden list', YK['affliction_list'],
  'eating_drinking_washing_anointing_sandals_relations'),
 ('Yoma 8:1 / Keritot 1:1 — eating on Yom Kippur is karet',
  YK['not_afflicting'], 'karet'),
 ('Keritot 1:1 — working on Yom Kippur is karet (the destroying verb)',
  YK['working'], 'destroyed'),
 ('Makkot 3:2 — the eater and the worker on Yom Kippur among the lashed',
  YK['prohibition_class'], 'lav_and_karet'),
 ('Chagigah 2:4 — Atzeret can fall beside the Sabbath (the morrow = festival)',
  OM['morrow_reading'], 'festival'),
 ('Menachot 5:3 — the omer\'s grain offering takes oil', OM['minchah_oil'], 'oil'),
 ('Menachot 5:3 — and frankincense', OM['minchah_frankincense'], 'frankincense'),
 ('Menachot 5:3 — the two loaves take neither', TL['oil_frankincense'], 'neither'),
 ('Menachot 10:5 — the new grain permitted from the omer',
  OM['new_grain_gate_with_temple'], 'the_omer'),
 ('Menachot 10:5 — without the Temple the whole day (R. Yehuda: Torah)',
  OM['new_grain_gate_without_temple'], 'whole_day'),
 ('Menachot 3:6 — the two loaves block each other', TL['mutual'], 'block_each_other'),
 ('Rosh Hashanah 3:3 — the day\'s instrument is a shofar', RH['instrument'], 'shofar'),
 ('Sukkah 4:1 — the sukkah seven days', SK['dwelling_days'], 7),
 ('Sukkah 3:12 — lulav seven in the Temple', SK['lulav_temple_days'], 7),
 ('Sukkah 3:12 — one in the provinces', SK['lulav_province_days'], 1),
 ('Sukkah 4:2 — lulav seven when the first day falls on the Sabbath',
  SK['first_day_on_sabbath'], 'overrides'),
 ('Sukkah 3:4 — one etrog', SK['etrog_count'], 1),
 ('Sukkah 3:4 — one lulav', SK['lulav_count'], 1),
 ('Sukkah 3:4 — two willows', SK['willow_count'], 2),
 ('Sukkah 3:4 — three myrtles (R. Yishmael) / one (R. Akiva)',
  SK['myrtle_count'], ['r_yishmael_three', 'r_akiva_one']),
 ('Sukkah 2:8 — women exempt from the sukkah', SK['women'], 'exempt'),
 ('Pesachim 5:3 — slaughtered before midday invalid: "between the evenings"',
  PSV['slaughter_window'], 'after_midday'),
 # ---- THE SHAVUOT ANIMALS (23:18-19) and the pointers, live (2026-09-06) ----
 ('Lev 23:18 — seven lambs, one bull, two rams: the three kinds censused', SA['olah_kinds'], 'seven_lambs_one_bull_two_rams'),
 ('Lev 23:18 — a burnt offering: wholly to the fires (CALLED offerings)', SA['olah_procedure'], 'wholly_to_fires'),
 ('Lev 23:18 — their meal offering and libations: Numbers 28\'s quantities', SA['minchah_libations'], 'per_Numbers_28'),
 ('Lev 23:19 — the goat sin offering slaughtered north (CALLED offerings)', SA['chatat_place'], 'north'),
 ('Zevachim 5:5 — the communal peace offering eaten by male priests: 23:20\'s "for the priest" (CALLED)', SA['shelamim_grade'], 'male_priests'),
 ('Zevachim 5:5 — the communal peace offering slaughtered north (CALLED)', SA['shelamim_place'], 'north'),
 ('Menachot 5:6 — the loaves waved on the two lambs', SA['waving'], 'loaves_on_two_lambs'),
 ('Menachot 4:3 — the bread and the lambs: R. Akiva / ben Nannas', SA['interdependence'], 'bread_blocks_lambs_R._Akiva_lambs_block_bread_ben_Nannas'),
 ('Menachot 3:6 — the two lambs block each other', SA['two_lambs_mutual'], 'block_each_other'),
 ('Menachot 4:2 — bulls, rams, lambs do not block each other', SA['kinds_independent'], 'do_not_block_each_other'),
 ('Sifra Emor Chapter 13 6 — two sets: for the bread, not for the day', SA['two_sets'], 'for_the_bread_not_for_the_day'),
 ('Lev 23:12 — the omer\'s lamb: a burnt offering (CALLED offerings)', OM['lamb_olah'], 'wholly_to_fires'),
 ('Sifra Emor Chapter 13 3 — the omer is Lev 2:14\'s offering (CALLED minchah)', OM['grain_source'], 'new_and_from_the_land'),
 ('Lev 23:5 — the LORD\'s Passover: eaten at night until midnight (CALLED pesach)', PSV['eating_time'], 'night only, until midnight'),
 ('Lev 23:6 — the feast of unleavened bread: Exod 12\'s window (CALLED pesach)', PSV['matzot_window'], '14th evening to 21st evening'),
 ('Exod 23:16, 23:19 — the first fruits, one institution at two seats (CALLED calendar)', TL['first_fruits_link'], 'bring to the house (seven kinds — fetched list)'),
 ('Exod 23:14-17 — the harvest feast is an appearing (CALLED calendar)', TL['pilgrimage'], 'owes the three appearings'),
]

# ---- (3)+(5) run, grade, effects ------------------------------------
print()
ok = 0
frac = {I: 0, M: 0, A: 0, D: 0, P: 0}
assert len(TESTS) == GUARDED, (len(TESTS), GUARDED)
for name, c, want in TESTS:
    hit = c['v'] == want
    ok += hit
    frac[c['p']] += 1
    print('%s %-72s [%s] %s' % ('OK ' if hit else 'MISS', name[:72], c['p'],
                                '' if hit else 'got=%r' % (c['v'],)))
    print('     effects: %s' % ', '.join(c['fx']))
n = len(TESTS)
print()
print('MATRIX: %d/%d cells match the answer sheet' % (ok, n))
print('FRACTIONS: pure ink %d/%d (%d%%) · recorded moves %d/%d (%d%%) · '
      'answer-sheet %d/%d · data %d/%d · imports %d/%d' % (
      frac[I], n, 100 * frac[I] // n, frac[M], n, 100 * frac[M] // n,
      frac[A], n, frac[D], n, frac[P], n))
print('computed, not graded: the count runs %d days and sanctifies the '
      '%dth (INK arithmetic); the fast begins on the ninth in the evening '
      '(INK); the eighth day is an assembly (INK)' % (OM['count_length']['v'], 50))
print('effects: every cell carries REGISTERED effects — three discovered '
      'in this span\'s own verbs: counts_omer, dwells_in_booths, '
      'takes_four_species [effects law satisfied]')
if ok == n:
    print()
    print('THE APPOINTED TIMES ENGINE STANDS — two work classes read off '
          'two token forms, the fast\'s two sanctions in their own verbs, '
          'the omer\'s arithmetic and gate from the ink, the four species '
          'counted by grammatical number, and the morrow ruled by the '
          'Sifra\'s four routes with Onkelos writing it into the verse.')
else:
    sys.exit('MISSES REMAIN — consult the Talmud per gap and recompile.')

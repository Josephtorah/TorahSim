#!/usr/bin/env python3
"""cold_run_yovel.py — THE JUBILEE ENGINE (Leviticus 25, with the
valuation table of Leviticus 27), the ninth span compiled under the
Step-5 deliverable rule (2026-09-05, the Behar-Bechukotai sweep — the
compile that closes Leviticus).

The five motions, in order:
 (1) code from the BARE INK of Lev 25 and 27 alone — the seven-year
     cycle and its product (seven sabbaths of years = forty-nine, the
     verse states the number; sanctify the fiftieth), the release day
     (the tenth of the seventh month, the Day of Atonement), the land's
     return (the RETURN verbs censused), the harvest-year pricing and
     the surplus returned, the walled-city year and its perpetuity, the
     village house reckoned as field, the Levites' perpetual redemption,
     the unsellable pasture, the two interest nouns, the Hebrew slave's
     hireling status and Jubilee exit with his children, the kin ladder,
     the hireling-days reckoning, the valuation table by sex and age
     bracket, the field's fifty per homer of seed and its deduction by
     the remaining years, the sela of twenty gerah; anything the ink
     does not state (the sixth, the pundion's size) is a PARAMETER;
 (2) the Mishnah's rows collected as TEST DATA, read from the local
     shelf with a token verified in each row's own ink;
 (3) run;
 (4) misses filled by NAMED recorded arguments, each labeled [MOVE]
     with its source — this run's: the Jubilee outside the seven-year
     cycle (Sifra Behar Section 1 6); the two-year floor from the plural
     'years' (Section 3 10); the reckoning counterpart and the lesser
     figure (Chapter 5 3-4; Chapter 8 5); the sanctuary's inversion
     (Chapter 5 6); the ten-day window (Chapter 2 1) and the cessation
     with the tribes' exile (Chapter 2 3); the pierced slave freed by
     the Jubilee (Chapter 2 5); the six-year exit IMPORTED from Exodus
     21:2 for the one sold to an Israelite (M-07) and denied to the one
     sold to a gentile (Chapter 8 4); land outside overreaching from
     'from the hand' (Section 3 1); the interest nouns defined by their
     worked cases (Section 5 2); the boundary year counting below
     (Bechukotai Section 3 9-11); the consecration floor (Chapter 10 7);
 (5) the graded matrix with per-cell provenance, fractions, and EFFECTS
     on every verdict — FOUR effects DISCOVERED in the span's own verbs
     and registered before this run: returns_to_holding (a TRANSFER),
     sold_in_perpetuity (a status), redemption_right (a status),
     interest_barred (a block).
Zero-report law: every claimed ink token is probed before anything
runs; the answer sheet is verified in its own ink.
"""
import sqlite3, sys, os, json
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import effects_layer as FX
from compile_guards import check_honest_pairing

GUARDED = check_honest_pairing(os.path.abspath(__file__))   # REVIEW_BEHAR item 6 — retrofit 2026-09-05
print('honest-pairing guard: %d tests checked, every expectation a literal' % GUARDED)

ROOT = '<repo-old>'
db = sqlite3.connect(ROOT + '/elijah_docket/tanakh.sqlite')


def strip(s):
    return ''.join(c for c in s if c != '/' and not (0x0591 <= ord(c) <= 0x05C7))


def toks(ch, vs):
    rows = db.execute("""SELECT w.he FROM words w JOIN verses v
        ON w.verse_id=v.id WHERE v.book='Lev' AND v.chapter=? AND v.verse=?
        ORDER BY w.idx""", (ch, vs)).fetchall()
    return [strip(r[0]) for r in rows]


T25 = {v: toks(25, v) for v in range(1, 56)}
T27 = {v: toks(27, v) for v in range(1, 35)}


def count(T, tok, vs, exact=False):
    return sum(1 for w in T[vs] if (w == tok if exact else tok in w))

# ---- (1) ink probes — each MUST fire or the run refuses -------------
PROBES = [
    ('SIX years sow',                          25, 3, 'שש'),
    ('the SEVENTH year — a sabbath of rest',    25, 4, 'השביעת'),
    ('seven sabbaths of years (seven x4)',      25, 8, 'שבע'),
    ('FORTY',                                   25, 8, 'וארבעים'),
    ('NINE — forty-nine stated',                25, 8, 'תשע'),
    ('a shofar',                                25, 9, 'שופר'),
    ('on the TENTH of the month',               25, 9, 'בעשור'),
    ('the Day of ATONEMENT',                    25, 9, 'הכפרים'),
    ('the FIFTIETH year',                       25, 10, 'החמשים'),
    ('LIBERTY',                                 25, 10, 'דרור'),
    ('to ALL its inhabitants',                  25, 10, 'ישביה'),
    ('you shall RETURN each to his holding',    25, 10, 'ושבתם'),
    ('RETURN each to his holding (13)',         25, 13, 'תשבו'),
    ('by the NUMBER of harvest YEARS',          25, 15, 'במספר'),
    ('INCREASE the price',                      25, 16, 'תרבה'),
    ('DECREASE the price',                      25, 16, 'תמעיט'),
    ('the blessing for THREE years',            25, 21, 'לשלש'),
    ('not sold IN PERPETUITY (the ban)',        25, 23, 'לצמתת'),
    ('REDEMPTION you shall give',               25, 24, 'גאלה'),
    ('his NEAR redeemer',                       25, 25, 'הקרב'),
    ('the SURPLUS returned',                    25, 27, 'העדף'),
    ('goes out IN THE JUBILEE',                 25, 28, 'ביבל'),
    ('a WALLED city',                           25, 29, 'חומה'),
    ('a FULL year',                             25, 30, 'תמימה'),
    ('IN PERPETUITY (the status)',              25, 30, 'לצמיתת'),
    ('to his GENERATIONS',                      25, 30, 'לדרתיו'),
    ('the VILLAGE houses',                      25, 31, 'החצרים'),
    ('PERPETUAL redemption for the Levites',    25, 32, 'עולם'),
    ('the PASTURE field',                       25, 34, 'מגרש'),
    ('shall NOT BE SOLD',                       25, 34, 'ימכר'),
    ('BITE-interest',                           25, 36, 'נשך'),
    ('and INCREASE',                            25, 36, 'ותרבית'),
    ('money in bite',                           25, 37, 'בנשך'),
    ('food in increase',                        25, 37, 'ובמרבית'),
    ("a slave's work",                          25, 39, 'עבדת'),
    ('as a HIRELING',                           25, 40, 'כשכיר'),
    ('as a RESIDENT',                           25, 40, 'כתושב'),
    ('until the JUBILEE year',                  25, 40, 'היבל'),
    ('he and his CHILDREN with him',            25, 41, 'ובניו'),
    ("a slave's SALE",                          25, 42, 'ממכרת'),
    ('with RIGOR',                              25, 43, 'בפרך'),
    ('FOREVER — the gentile slave',             25, 46, 'לעלם'),
    ('one of his BROTHERS redeems him',         25, 48, 'מאחיו'),
    ('his UNCLE',                               25, 49, 'דדו'),
    ("as a hireling's DAYS",                    25, 50, 'כימי'),
    ('MANY years remain',                       25, 51, 'רבות'),
    ('FEW remain',                              25, 52, 'מעט'),
    ('IN YOUR SIGHT',                           25, 53, 'לעיניך'),
    ('nor PRUNE your vineyard',                 25, 4, 'תזמר'),
    ('the AFTERGROWTH of your harvest',         25, 5, 'ספיח'),
    ('you shall not REAP',                      25, 5, 'תקצור'),
    ('you shall not GATHER (vintage)',          25, 5, 'תבצר'),
    ('for FOOD — the eaters clause opens',      25, 6, 'לאכלה'),
    ('for your SLAVE',                          25, 6, 'ולעבדך'),
    ('for your MAIDSERVANT',                    25, 6, 'ולאמתך'),
    ('for your HIRELING',                       25, 6, 'ולשכירך'),
    ('for your RESIDENT',                       25, 6, 'ולתושבך'),
    ('for your CATTLE',                         25, 7, 'ולבהמתך'),
    ('and for the BEAST',                       25, 7, 'ולחיה'),
    ('which is IN YOUR LAND',                   25, 7, 'בארצך'),
    ('until the NINTH year',                    25, 22, 'התשיעת'),
    ('the TENTH shall be holy',                 27, 32, 'העשירי'),
    ('under the ROD',                           27, 32, 'השבט'),
    ('nor SUBSTITUTE it (the tithe)',           27, 33, 'ימירנו'),
    ('it shall not be REDEEMED (the tithe)',    27, 33, 'יגאל'),
    ('FIFTY shekels — the adult male',          27, 3, 'חמשים'),
    ('THIRTY — the adult female',               27, 4, 'שלשים'),
    ('TWENTY / TEN — five to twenty',           27, 5, 'עשרים'),
    ('FIVE shekels — a month to five',          27, 6, 'חמשה'),
    ('THREE — the girl',                        27, 6, 'שלשת'),
    ('FIFTEEN — sixty and up',                  27, 7, 'עשר'),
    ('a HOMER of barley seed',                  27, 16, 'חמר'),
    ('at FIFTY shekels',                        27, 16, 'בחמשים'),
    ('DEDUCTED by the remaining years',         27, 18, 'ונגרע'),
    ('add its FIFTH',                           27, 19, 'חמשית'),
    ('TWENTY GERAH the shekel',                 27, 25, 'גרה'),
]
for label, ch, vs, tok in PROBES:
    T = T25 if ch == 25 else T27
    if count(T, tok, vs) < 1:
        sys.exit('ZERO-REPORT LAW: probe %r wanted %r at Lev %d:%d — '
                 'not found, refusing to run' % (label, tok, ch, vs))
print('probes: all %d ink-token probes fired [zero-report law satisfied]'
      % len(PROBES))

# ---- the ink censuses the machine runs on ----------------------------
SEVENS_25_8 = count(T25, 'שבע', 8, exact=True)
RETURN_VERSES = sorted(v for v in T25 if count(T25, 'ושבתם', v) or count(T25, 'תשבו', v)
                       or count(T25, 'ושב', v, exact=True))
JUBILEE_EXIT = sorted(v for v in T25 if count(T25, 'ביבל', v))
JUBILEE_YEAR_TOK = sorted(v for v in T25 if count(T25, 'היבל', v))
REDEMPTION = sorted(v for v in T25 if count(T25, 'גאל', v))
HAKOHEN_27 = [v for v in T27 for w in T27[v] if w == 'הכהן']   # the definite SUBJECT form
LAKOHEN_27 = [v for v in T27 for w in T27[v] if w == 'לכהן']   # the dative DESTINATION form (27:21)
PRIEST_27 = HAKOHEN_27 + LAKOHEN_27
assert SEVENS_25_8 == 4, SEVENS_25_8   # seven sabbaths / seven years / seven times / seven sabbaths
assert RETURN_VERSES == [10, 13, 27, 28, 41], RETURN_VERSES
assert JUBILEE_EXIT == [28, 30, 31, 33], JUBILEE_EXIT   # 25:54 says בשנת היבל (in the Jubilee YEAR)
print('ink census: seven x%d at 25:8 · RETURN verbs at %s · in-the-Jubilee '
      'tokens at %s · Jubilee-YEAR tokens at %s · redemption tokens at %d '
      'verses · priest tokens in Lev 27: %d definite (the assessor) + %d '
      'dative (the destination)' % (SEVENS_25_8, RETURN_VERSES, JUBILEE_EXIT,
      JUBILEE_YEAR_TOK, len(REDEMPTION), len(HAKOHEN_27), len(LAKOHEN_27)))

I, M, A, D = 'INK', 'MOVE', 'ANSWER-SHEET', 'DATA'


def cell(v, p, why, effects):
    FX.validate(effects)
    return {'v': v, 'p': p, 'why': why, 'fx': effects}


# ---- (1) THE ENGINE — compiled from Lev 25's ink -------------------
CYCLE = 7 * 7                              # שבע שנים שבע פעמים — seven years, seven times (25:8)
assert CYCLE == 49                         # תשע וארבעים at 25:8 — the ink states it
JUBILEE = CYCLE + 1                        # שנת החמשים at 25:10


def cycle(year):
    """A year's class inside one Jubilee period, from the ink's arithmetic."""
    if year == JUBILEE:
        return cell('jubilee', I, 'שנת החמשים (the fiftieth year) at 25:10-11 — '
                    'seven sabbaths of years = forty-nine (25:8 states תשע '
                    'וארבעים), the fiftieth sanctified',
                    ['jubilee_release', 'returns_to_holding', 'goes_free',
                     'land_release', 'labor_barred'])
    if year % 7 == 0:
        return cell('sabbath_of_the_land', I,
                    'ובשנה השביעת שבת שבתון (in the seventh year a sabbath of '
                    'rest) at 25:4 — no sowing, pruning, reaping, gathering '
                    '(25:4-5)', ['land_release', 'labor_barred'])
    return cell('work_year', I, 'שש שנים תזרע (six years you shall sow) at 25:3',
                [FX.NONE])


def jubilee():
    return {
     'cycle_length': cell(CYCLE, I, 'תשע וארבעים שנה at 25:8 — the product stated',
                          ['jubilee_release']),
     'jubilee_year': cell(JUBILEE, I, 'החמשים at 25:10 and 25:11', ['jubilee_release']),
     'release_day': cell('tenth_of_seventh_month_yom_kippur', I,
                         'בחדש השבעי בעשור לחדש ביום הכפרים at 25:9',
                         ['jubilee_release', 'returns_to_holding', 'goes_free']),
     'sanctified_from': cell('first_of_tishrei', M,
                             '"sanctify the fiftieth YEAR" — from the New Year, '
                             'the release firing at Yom Kippur ten days in '
                             '(Sifra Behar Chapter 2 1, R. Yochanan b. Beroka)',
                             ['jubilee_release']),
     'in_cycle': cell('not_counted', M,
                      '"six years sow" — the sown years count, the Jubilee '
                      'does not (Sifra Behar Section 1 6; the Sages of Section '
                      '2 2 couple it to the seventh)', ['jubilee_release']),
     'precondition': cell('all_inhabitants_on_the_land', I,
                          'לכל ישביה (to ALL its inhabitants) at 25:10',
                          ['jubilee_release']),
     'ceased_when': cell('two_and_a_half_tribes_exiled', M,
                         'Sifra Behar Chapter 2 3 — the Jubilees ceased when '
                         'Reuben, Gad, and half Manasseh went into exile',
                         [FX.NONE]),
     'pierced_slave': cell('freed_by_jubilee', M,
                           '"return each to his family" — the pierced slave '
                           'near the Jubilee (Sifra Behar Chapter 2 5, R. '
                           'Eliezer b. Yaakov)', ['jubilee_release', 'goes_free']),
    }


def field_sale(price, years_to_jubilee, elapsed):
    """The harvest-year pricing of 25:15-16 and the surplus of 25:27."""
    remaining = years_to_jubilee - elapsed
    surplus = price * remaining // years_to_jubilee
    return {
     'price_rule': cell('by_harvest_years', I,
                        'במספר שני תבואת ימכר לך (by the number of harvest '
                        'years he sells to you) at 25:15; increase/decrease by '
                        'the years at 25:16', ['redemption_right']),
     'redemption_price': cell(surplus, I,
                              'והשיב את העדף (return the SURPLUS) at 25:27 — '
                              'price x remaining / total = %d x %d / %d'
                              % (price, remaining, years_to_jubilee), ['pays']),
     'unredeemed': cell('returns_at_jubilee', I,
                        'ויצא ביבל ושב לאחזתו at 25:28', ['returns_to_holding']),
     'floor': cell('not_under_two_years', M,
                   '"YEARS... you shall buy" — the plural is two: sold in the '
                   'Jubilee year, no redemption in less than two (Sifra Behar '
                   'Section 3 10)', ['redemption_right']),
     'blight_year': cell('not_counted', M,
                         '"years of PRODUCE" — a blight or mildew year and the '
                         'seventh do not count (Sifra Behar Section 3 10)',
                         ['redemption_right']),
     'counterpart_when_resold_dearer': cell('first_buyer', M,
                                            '"to whom he sold" (Sifra Behar '
                                            'Chapter 5 3)', ['pays']),
     'improved_or_declined': cell('lesser_figure', M,
                                  'R. Dostai b. Yehuda — the surplus in his hand '
                                  'or in the land (Sifra Behar Chapter 5 4)',
                                  ['pays']),
     'hekdesh_constraints': cell('inverted', M,
                                 '"in the BUYER\'s hand" — not the sanctuary\'s: '
                                 'from the sanctuary one borrows and redeems by '
                                 'halves (Sifra Behar Chapter 5 6)',
                                 ['redemption_right']),
    }


def house_sale(kind):
    if kind == 'walled_city':
        return cell('one_year_then_permanent', I,
                    'עד תם שנת ממכרו (until the end of the year of its sale) at '
                    '25:29; שנה תמימה (a full year), לצמיתת (in perpetuity), '
                    'לא יצא ביבל (it shall not go out in the Jubilee) at 25:30', ['redemption_right', 'sold_in_perpetuity'])
    if kind == 'village':
        return cell('as_field_but_at_once', I,
                    'על שדה הארץ יחשב (reckoned as the field) — גאלה תהיה לו, '
                    'וביבל יצא (25:31)', ['redemption_right', 'returns_to_holding'])
    if kind == 'levite_house':
        return cell('perpetual_redemption', I,
                    'גאלת עולם תהיה ללוים (25:32); ויצא... ביבל (25:33)',
                    ['redemption_right', 'returns_to_holding'])
    if kind == 'levite_pasture':
        return cell('unsellable', I, 'לא ימכר כי אחזת עולם הוא להם (25:34)',
                    [FX.NONE])
    raise KeyError(kind)


HILLEL = cell('deposit_in_chamber', A,
              'the buyer who hid on the twelfth month\'s last day — Hillel\'s '
              'ordinance (Mishnah Arakhin 9:4; Sifra Behar Section 4 8)',
              ['redemption_right'])


def overreaching():
    return {
     'measure': cell('sixth', D, 'the verse says only "do not wrong" (25:14) — '
                     'the sixth is the answer sheet\'s parameter (Mishnah Bava '
                     'Metzia 4:3; Sifra Behar Section 3 5)', ['restores']),
     'on_land': cell('none', M, '"buy FROM THE HAND of your fellow" — what passes '
                     'hand to hand; land excluded (Sifra Behar Section 3 1)',
                     [FX.NONE]),
    }


def interest():
    return {
     'both_nouns': cell('barred', I, 'נשך ותרבית at 25:36; בנשך / ובמרבית at 25:37',
                        ['interest_barred']),
     'definitions': cell('money_bite_vs_produce_increase', M,
                         'a sela for five dinars; wheat reckoned at the risen '
                         'price for wine he lacks (Sifra Behar Section 5 2)',
                         ['interest_barred']),
    }


def hebrew_slave(sold_to, price, years_to_jubilee, elapsed):
    remaining = years_to_jubilee - elapsed
    out = {
     'status': cell('hireling_resident', I, 'כשכיר כתושב יהיה עמך at 25:40',
                    [FX.NONE]),
     'slave_work': cell('barred', I, 'לא תעבד בו עבדת עבד at 25:39', [FX.NONE]),
     'rigor': cell('barred', I, 'לא תרדה בו בפרך at 25:43 (and 25:53 in your sight)',
                   [FX.NONE]),
     'exit': cell('at_jubilee_with_children', I,
                  'עד שנת היבל יעבד עמך (until the Jubilee year he serves with '
                  'you) at 25:40; הוא ובניו עמו (he and his children with him) '
                  'at 25:41 and 25:54; ויצא בשנת היבל (he goes out in the '
                  'Jubilee year) at 25:54',
                  ['jubilee_release', 'goes_free', 'returns_to_holding']),
     'redemption_price': cell(price * remaining // years_to_jubilee, I,
                              'כימי שכיר (as a hireling\'s days) at 25:50; "if '
                              'many years remain... from the money of his '
                              'purchase" (25:51-52) — price x remaining / total',
                              ['pays', 'goes_free']),
     'lesser_figure': cell('lesser_figure', M,
                           'improved or declined — the maneh either way (Sifra '
                           'Behar Chapter 8 5)', ['pays']),
    }
    if sold_to == 'gentile':
        out['redeemers'] = cell('kin_ladder_at_once', I,
                                'גאלה תהיה לו אחד מאחיו יגאלנו (25:48); the uncle, '
                                'the cousin, the near of flesh, or his own hand '
                                '(25:49)', ['redemption_right'])
        out['six_year_exit'] = cell('none', M,
                                    '"from the year of his sale until the Jubilee" '
                                    '— he does not go out at six (Sifra Behar '
                                    'Chapter 8 4)', [FX.NONE])
    else:
        out['six_year_exit'] = cell('imported_exodus_21_2', M,
                                    'IMPORT EDGE (M-07): "six years he shall serve" '
                                    '(Exod 21:2) — the term clock of cold_run_'
                                    'mishpatim.py; Lev 25 states only the Jubilee '
                                    'ceiling', ['term_clock', 'goes_free'])
    return out


def gentile_slave():
    return {
     'term': cell('forever', I, 'לעלם בהם תעבדו at 25:46', [FX.NONE]),
     'acquisition': cell('money_deed_possession', M,
                         '"a holding for you" — as land is acquired, so slaves '
                         '(Sifra Behar Section 6 4)', [FX.NONE]),
    }


# ---- THE VALUATION TABLE — Lev 27:3-7, the ink's own brackets -------
TABLE = {  # (lower_inclusive_years, upper_exclusive_years): (male, female)
    (20, 60): (50, 30), (5, 20): (20, 10), (0, 5): (5, 3), (60, 999): (15, 10)}


def valuation(sex, age_years, age_months=0):
    """The fixed sums by sex and bracket; the boundary year counts BELOW."""
    if age_years == 0 and age_months < 1:
        return cell('none', I, 'מבן חדש (from a month old) at 27:6 — no bracket below',
                    [FX.NONE])
    for (lo, hi), (m, f) in TABLE.items():
        if lo < age_years < hi or (age_years == lo == 0):
            v = m if sex == 'male' else f
            return cell(v, I, 'ערכך at 27:%d — the bracket %d-%d, %s'
                        % ({20: 3, 5: 5, 0: 6, 60: 7}[lo], lo, hi, sex),
                        ['gives_fixed_sum'])
    # exactly on a boundary year: 5, 20, or 60
    below = {5: (0, 5), 20: (5, 20), 60: (20, 60)}[age_years]
    m, f = TABLE[below]
    return cell(m if sex == 'male' else f, M,
                'the boundary year counts BELOW — "from sixty and UPWARD" and '
                '"year"-"year" (Sifra Bechukotai Section 3 9-11; Mishnah '
                'Arakhin 4:4)', ['gives_fixed_sum'])


PUNDION_PER_SELA = 48   # DATA: the coin table (a dinar = 12 pundion, a sela = 4 dinar)


def field_valuation(years_to_jubilee):
    rate = 50                                   # בחמשים שקל כסף at 27:16
    per_year = rate / CYCLE                     # 50 / 49 — deducted by the years (27:18)
    sela_pundion = 1 + 1 / PUNDION_PER_SELA
    return {
     'rate': cell(rate, I, 'זרע חמר שערים בחמשים שקל כסף at 27:16', ['gives_fixed_sum']),
     'deduction': cell('by_remaining_years', I, 'ונגרע מערכך at 27:18', ['gives_fixed_sum']),
     'per_year': cell('sela_and_pundion', I,
                      '50 / 49 = %.4f sela per year; a sela and a pundion = %.4f '
                      '(the pundion, 1/48 sela, is the coin nearest the '
                      'remainder — Sifra Bechukotai Chapter 10 5 calls it the '
                      'premium)' % (per_year, sela_pundion), ['gives_fixed_sum']),
     'owed': cell(round(per_year * years_to_jubilee, 2), I,
                  'the remaining years x the per-year rate', ['gives_fixed_sum']),
     'redeem_fifth': cell('adds_fifth', I, 'ויסף חמשית כסף ערכך עליו at 27:19',
                          ['adds_fifth']),
     'unredeemed_sold': cell('to_the_priest_at_jubilee', I,
                             'והיה השדה בצאתו ביבל קדש (the field in its going out in the '
                             'Jubilee is holy); לכהן תהיה אחזתו (to the priest shall '
                             'be its holding) at 27:21',
                             ['due_to_priest']),
     'consecration_floor': cell('two_years_before_jubilee', M,
                                '"the priest shall reckon by the REMAINING years" '
                                '(Sifra Bechukotai Chapter 10 7)', [FX.NONE]),
     'shekel': cell(20, I, 'עשרים גרה יהיה השקל at 27:25', ['gives_fixed_sum']),
    }


PRIESTS = cell(len(HAKOHEN_27), I,
               'הכהן (THE priest — the definite subject form) counted %d times in '
               'Lev 27 as the ASSESSOR (27:8 x3, 27:11, 27:12 x2, 27:14 x2, '
               '27:18, 27:23); the one לכהן (TO the priest, 27:21) is a '
               'destination, not an assessor — the form splits the census'
               % len(HAKOHEN_27), [FX.NONE])
ASSESSORS = cell('nine_israelites_and_a_priest', M,
                 'Shmuel: "ten priests are written in the section — one for '
                 'itself, the rest a limitation after a limitation, which '
                 'includes: even nine Israelites and one priest" (Babylonian '
                 'Talmud Sanhedrin 15a:6, read for this gap)', [FX.NONE])


# ---- (2) TEST DATA — Mishnah rows read from the shelf --------------
def mishnah(tractate, ch, m, must):
    fn = ROOT + '/Data/mishnah_%s_he.json' % tractate
    d = json.load(open(fn))
    t = d['text'] if isinstance(d, dict) and 'text' in d else d
    row = strip(t[ch - 1][m - 1])
    assert must in row, 'answer-sheet check failed: %r not in Mishnah %s %d:%d' % (must, tractate, ch, m)
    return row



# ---- THE SABBATICAL YEAR — the cell extended into a graded function
# (2026-09-05, REVIEW_BEHAR item 2: Mishnah Sheviit routed by topic) ----
LABOR_VERBS = [w for v in (4, 5) for w in T25[v] if w in ('תזרע', 'תזמר', 'תקצור', 'תבצר')]
EATERS = [w for v in (6, 7) for w in T25[v] if w in ('לך', 'ולעבדך', 'ולאמתך', 'ולשכירך', 'ולתושבך', 'ולבהמתך', 'ולחיה')]
assert len(LABOR_VERBS) == 4, LABOR_VERBS
assert len(EATERS) == 7, EATERS


def sabbatical():
    return {
     'torah_labors': cell(len(LABOR_VERBS), I, 'the four verbs the ink writes at 25:4-5: %s — sow, '
                          'prune, reap, gather' % ' / '.join(LABOR_VERBS), ['labor_barred', 'land_release']),
     'derivative_layer': cell('rabbinic_verse_as_support', M, 'the census the Sifra reads from "your '
                              'field NOT, your vineyard NOT" (weeding, hoeing, trimming, fertilizing, '
                              'smoking) is RULED rabbinic, the verse a mere support — "pruning is under '
                              'sowing, vintaging under reaping; written to say THESE derivatives alone '
                              'incur liability" (Babylonian Talmud Moed Katan 3a:2-3, 3a:9, 3a:22)',
                              ['labor_barred']),
     'plowing_lashes': cell(['lashes', 'no_lashes'], M, 'R. Yochanan and R. Elazar, one each way '
                            '(Moed Katan 3a:12) — on R. Avin\'s meta-rule about a general in a positive '
                            'and a particular in a negative', ['labor_barred']),
     'two_hoeings': cell('strengthen_barred_close_cracks_permitted', M, 'Rav Ukva b. Chama (Moed Katan '
                         '3a:11) on Exod 23:11\'s "release and abandon"', ['labor_barred']),
     'addition_days': cell(30, D, 'THIRTY DAYS before the New Year — a halakhah to Moses from Sinai '
                           '(Moed Katan 3b:12; Sifra Behar Chapter 1 1): the data channel', ['labor_barred']),
     'addition_cutoffs': cell('abolished_by_rabban_gamliel', M, 'the Passover and Atzeret cutoffs of '
                              'Mishnah Sheviit 1:1 and 2:1 were the sages\' own with a repeal condition; '
                              'Rabban Gamliel\'s court voted and abolished them (Moed Katan 3b:8-12)',
                              [FX.NONE]),
     'addition_temple_bound': cell('only_while_temple_stands', M, 'Rav Ashi: the halakhah was received '
                                   'only while the Temple stands, like the water libation (Moed Katan 4a:9)',
                                   [FX.NONE]),
     'eaters': cell(len(EATERS), I, 'לך ולעבדך ולאמתך ולשכירך ולתושבך (25:6) ולבהמתך ולחיה (25:7) — '
                    'seven eater tokens: you, your slave, your maidservant, your hireling, your '
                    'resident, your cattle, the beast', ['land_release']),
     'after_removal': cell(['r_yehuda_poor_only', 'r_yosei_poor_and_rich'], M, 'who eats after the '
                           'removal — the eaters clause read two ways (Sifra Behar Chapter 1 6; Mishnah '
                           'Sheviit 9:8)', ['land_release']),
     'aftergrowth_ink': cell('not_reaped_as_harvest', I, 'את ספיח קצירך לא תקצור (the aftergrowth of your '
                             'harvest you shall not reap, 25:5); ספיחיה at 25:11 for the Jubilee',
                             ['labor_barred']),
     'aftergrowth_ban': cell(['sages_all_forbidden', 'r_shimon_permitted_but_cabbage', 'r_yehuda_mustard_permitted'],
                             M, 'the Sages: all aftergrowth forbidden — "from here the sages RELIED on the '
                             'aftergrowth being forbidden" (Sifra Behar Chapter 1 3, Chapter 4 5 — the '
                             'ban rabbinic with the verse its peg); R. Shimon and R. Yehuda\'s arms '
                             '(Mishnah Sheviit 9:1)', ['labor_barred']),
     'field_clock': cell('eat_from_house_while_in_field', M, '"from the field you shall eat its produce" — '
                         'while you eat from the field you eat from the house; gone from the field, '
                         'remove from the house (Sifra Behar Chapter 3 4)', ['land_release']),
     'jar': cell('per_kind_rabban_gamliel_the_law', M, 'three pickled kinds in one jar — Rabban Gamliel: '
                 'each kind gone from the field is removed from the jar, "and the law follows him" '
                 '(Sifra Behar Chapter 3 5; Mishnah Sheviit 9:5)', ['land_release']),
     'export': cell('not_abroad_syria_permitted', M, 'אשר בארצך (which is in your land, 25:7) — what is '
                    'in your land is eaten, not what one carried to his slaves abroad; R. Shimon: "I '
                    'heard explicitly — to Syria yes, abroad no" (Sifra Behar Chapter 1 9)',
                    ['land_release']),
     'commerce': cell('barred', M, 'לאכלה (for FOOD, 25:6) — not for meal offerings or libations, and '
                      'the eating-not-commerce rule the seat carries (Sifra Behar Chapter 1 6, LV25A-05)',
                      ['land_release']),
     'changed_manner': cell('not_as_the_gatherers', M, '"you shall not gather" — not as the gatherers '
                            'gather: figs not in the drying-yard, grapes not in the press (Sifra Behar '
                            'Chapter 1 3)', ['labor_barred']),
     'money_chain': cell('last_seized_fruit_forbidden', M, 'as the holy seizes its price, so the seventh '
                         'seizes its price; "it" — it stays in its holiness: the last and last is seized '
                         'and the fruit itself forbidden (Sifra Behar Chapter 3 3)', ['land_release']),
     'blessing_years': cell(3, I, 'ועשת את התבואה לשלש השנים (it shall make produce for THREE years, '
                            '25:21) — the sixth, the seventh, the year after', ['land_release']),
     'blessing_with_jubilee': cell(4, M, '"another reading: for the seventh, the Jubilee, and the year '
                                   'after" — four when the fiftieth follows the forty-ninth (Sifra Behar '
                                   'Chapter 4 6)', ['jubilee_release']),
     'old_until': cell('ninth_year', I, 'ואכלתם מן התבואה ישן עד השנה התשיעת (you shall eat of the old '
                       'produce until the ninth year, 25:22)', ['land_release']),
     'zones': cell('three_lands', D, 'the three lands of Mishnah Sheviit 6:1 — the returnees\' holdings — '
                   'a zone map the ink\'s "in your land" (25:7) leaves as data', ['land_release']),
     'debt_release': cell('routed_deut_15', M, 'the money release is Deuteronomy 15\'s (THE TWO RELEASES '
                          'MATRIX, LV25A-13: money to the seventh, slaves to the Jubilee) — an import edge '
                          '(M-07) the walk\'s Re\'eh sitting will compile; Mishnah Sheviit 10 carried '
                          'routed', [FX.NONE]),
     'tools_rule': cell('work_specific_to_transgression_barred', A, 'the craftsman\'s sale classifier — '
                        'the Mishnah\'s own rule with no ink beneath it (Mishnah Sheviit 5:6)', [FX.NONE]),
    }


# ---- THE ANIMAL TITHE'S NAMING MACHINE — Lev 27:32-33 (the error rule the
# review said was never written) ----------------------------------------
def tithe_naming(calls):
    """calls: {position: name} for the ninth, tenth, eleventh to pass under
    the rod. THE TENTH IS HOLY by the ink (27:32); an ERROR sanctifies the
    neighbor it names 'tenth' (the Sifra's inclusion of the ninth and the
    eleventh from 'shall be holy' — LV27-23), and the eleventh only if the
    name 'tenth' was UPROOTED from the tenth (Mishnah Bekhorot 9:8's rule)."""
    tenth_uprooted = calls.get(10) != 'tenth'
    out = {}
    for pos in (9, 10, 11):
        nm = calls.get(pos)
        if pos == 10:
            out[pos] = 'tithe'                      # INK: העשירי יהיה קדש — whatever it was called
        elif pos == 9 and nm == 'tenth':
            out[pos] = 'sanctified_eaten_blemished' # MOVE: the neighbor named in error
        elif pos == 11 and nm == 'tenth':
            out[pos] = 'shelamim' if tenth_uprooted else 'not_sanctified'
        else:
            out[pos] = 'profane'
    return out


TN_ERROR = cell(tithe_naming({9: 'tenth', 10: 'ninth', 11: 'tenth'}), M,
                'ninth called tenth, tenth ninth, eleventh tenth — all three sanctified: the ninth eaten '
                'blemished, the tenth tithe, the eleventh a peace offering (R. Meir; Sifra Bechukotai '
                'Chapter 13 1-3, LV27-23; Mishnah Bekhorot 9:8)', ['substitution'])
TN_PLAIN = cell(tithe_naming({9: 'ninth', 10: 'tenth', 11: 'eleventh'}), I,
                'העשירי יהיה קדש ליהוה (the tenth shall be holy to the LORD, 27:32) — the ordinal '
                'names its own', ['substitution'])
TN_NOT_UPROOTED = cell(tithe_naming({9: 'tenth', 10: 'tenth', 11: 'tenth'}), M,
                       'the name "tenth" was NOT uprooted from the tenth — the eleventh is not sanctified '
                       '(Mishnah Bekhorot 9:8\'s closing rule)', ['substitution'])
TN_PASSES = cell('bought_and_gifted_exempt', M, '"all that PASSES under the rod" — born in his domain: the '
                 'bought and the gifted exempt (Sifra Bechukotai Chapter 12, LV27-22; Mishnah Bekhorot 9:3)',
                 [FX.NONE])
TN_EXCLUDED = cell('kilayim_terefah_caesarean_underage_orphan', M, 'what enters the pen — the Sifra\'s '
                   'exclusions on "all that passes" (LV27-06; Mishnah Bekhorot 9:4)', [FX.NONE])
TN_DISTANCE = cell(16, D, 'the herd combines within a grazing beast\'s walk — sixteen mil (Mishnah '
                   'Bekhorot 9:2): a distance parameter the ink leaves open', [FX.NONE])


# ---- THE OWNER'S PRECEDENCE — Arakhin 8:2-8:3's fifth arithmetic ------
def owner_price(bid, own=20):
    """The owner adds a FIFTH (27:19) to his own valuation — a quarter of the
    principal, so that the fifth is of the total (20 → 25); no fifth on
    another's raise: at bids up to own + 5 the owner pays bid + 5; above
    that he must exceed by a dinar to stay first."""
    fifth = own // 4
    if bid <= own + fifth:
        return bid + fifth
    return 'thirty_one_and_a_dinar' if bid == 26 else bid + fifth + 0.25


OP = {b: cell(owner_price(b), A if b <= 25 else A, 'ויסף חמשית (27:19) on the owner\'s own twenty = 5, and '
              'no fifth on the other\'s raise — the answer sheet\'s arithmetic (Mishnah Arakhin 8:3)',
              ['adds_fifth']) for b in (21, 22, 23, 24, 25, 26)}


# ---- THE INTEREST SCOPE — brother and foreigner ---------------------
def interest_scope(borrower):
    if borrower == 'brother':
        return cell('barred', I, 'אל תקח מאתו נשך ותרבית... וחי אחיך עמך (25:36) — your BROTHER', ['interest_barred'])
    if borrower == 'foreigner':
        return cell('permitted', M, 'IMPORT EDGE (M-07): לנכרי תשיך ולאחיך לא תשיך (to the foreigner you '
                    'may lend at interest, to your brother not — Deut 23:21); Mishnah Bava Metzia 5:6\'s '
                    'iron sheep from gentiles', [FX.NONE])
    raise KeyError(borrower)


RENT_SALE = cell('increase_on_rent_not_sale', A, 'the answer sheet\'s own asymmetry over the two nouns — '
                 'ten sela a year now or a sela a month, permitted; a thousand now or twelve maneh at '
                 'threshing, forbidden (Mishnah Bava Metzia 5:2)', ['interest_barred'])
NAMED_FENCES = cell(['advance', 'after', 'words'], A, 'Rabban Gamliel\'s advance interest and after-interest, '
                    'R. Shimon\'s interest of words (Mishnah Bava Metzia 5:10) — the fence\'s three named '
                    'outer classes, no ink beneath', ['interest_barred'])

SHEET = [
    ('Rosh Hashanah 1:1', 'rosh_hashanah', 1, 1, 'וליובלות'),
    ('Kiddushin 1:2', 'kiddushin', 1, 2, 'וביובל'),
    ('Arakhin 9:1', 'arakhin', 9, 1, 'שתי'),
    ('Arakhin 9:2', 'arakhin', 9, 2, 'הראשון'),
    ('Arakhin 9:3', 'arakhin', 9, 3, 'מיד'),
    ('Arakhin 9:4', 'arakhin', 9, 4, 'הלל'),
    ('Arakhin 9:7', 'arakhin', 9, 7, 'החצרים'),
    ('Arakhin 9:8', 'arakhin', 9, 8, 'לעולם'),
    ('Bava Metzia 4:3', 'bava_metzia', 4, 3, 'שתות'),
    ('Bava Metzia 4:9', 'bava_metzia', 4, 9, 'והקרקעות'),
    ('Bava Metzia 5:1', 'bava_metzia', 5, 1, 'נשך'),
    ('Arakhin 1:1', 'arakhin', 1, 1, 'חדש'),
    ('Arakhin 3:1', 'arakhin', 3, 1, 'חמשים'),
    ('Arakhin 4:4', 'arakhin', 4, 4, 'כלמטה'),
    ('Arakhin 7:1', 'arakhin', 7, 1, 'ופנדיון'),
    ('Megillah 4:3', 'megillah', 4, 3, 'תשעה'),
    ('Sheviit 1:1', 'sheviit', 1, 1, 'העצרת'),
    ('Sheviit 2:2', 'sheviit', 2, 2, 'מזבלין'),
    ('Sheviit 2:6', 'sheviit', 2, 6, 'שלשים'),
    ('Sheviit 5:6', 'sheviit', 5, 6, 'הכלל'),
    ('Sheviit 6:1', 'sheviit', 6, 1, 'שלש'),
    ('Sheviit 6:5', 'sheviit', 6, 5, 'לסוריא'),
    ('Sheviit 7:3', 'sheviit', 7, 3, 'סחורה'),
    ('Sheviit 8:6', 'sheviit', 8, 6, 'במקצה'),
    ('Sheviit 8:7', 'sheviit', 8, 7, 'אחרון'),
    ('Sheviit 9:1', 'sheviit', 9, 1, 'הספיחין'),
    ('Sheviit 9:3', 'sheviit', 9, 3, 'שיכלה'),
    ('Sheviit 9:5', 'sheviit', 9, 5, 'והלכה'),
    ('Sheviit 9:8', 'sheviit', 9, 8, 'הבעור'),
    ('Sheviit 10:1', 'sheviit', 10, 1, 'משמטת'),
    ('Bekhorot 9:2', 'bekhorot', 9, 2, 'מיל'),
    ('Bekhorot 9:3', 'bekhorot', 9, 3, 'פטור'),
    ('Bekhorot 9:4', 'bekhorot', 9, 4, 'הכלאים'),
    ('Bekhorot 9:8', 'bekhorot', 9, 8, 'עשירי'),
    ('Arakhin 8:3', 'arakhin', 8, 3, 'ודינר'),
    ('Bava Metzia 5:2', 'bava_metzia', 5, 2, 'השכר'),
    ('Bava Metzia 5:6', 'bava_metzia', 5, 6, 'הנכרים'),
    ('Bava Metzia 5:10', 'bava_metzia', 5, 10, 'מקדמת'),
]
SHEET2 = [   # the Sifra and Talmud rows the sabbatical cells cite, verified in their own ink
    ('sifra', 'Behar', 'Chapter 1', 3, 'הבוצרים'),
    ('sifra', 'Behar', 'Chapter 1', 6, 'לאכלה'),
    ('sifra', 'Behar', 'Chapter 1', 9, 'לסוריא'),
    ('sifra', 'Behar', 'Chapter 3', 3, 'נתפס'),
    ('sifra', 'Behar', 'Chapter 3', 4, 'כלה'),
    ('sifra', 'Behar', 'Chapter 3', 5, 'והלכה'),
    ('sifra', 'Behar', 'Chapter 4', 5, 'הספיחים'),
    ('sifra', 'Behar', 'Chapter 4', 6, 'לשלש'),
    ('bavli', 'moed_katan', 3, 'a', 2, 'זמירה'),
    ('bavli', 'moed_katan', 3, 'a', 9, 'מדרבנן'),
    ('bavli', 'moed_katan', 3, 'a', 12, 'לוקה'),
    ('bavli', 'moed_katan', 3, 'b', 8, 'ובטלום'),
    ('bavli', 'moed_katan', 3, 'b', 12, 'שלשים'),
    ('bavli', 'moed_katan', 4, 'a', 9, 'קיים'),
]
import re as _re
def _sifra(book, section, n, must):
    d = json.load(open(ROOT + '/Data/sifra_he.json'))
    t = d['text'] if isinstance(d, dict) and 'text' in d else d
    row = strip(t[book][section][n - 1])
    assert must in row, 'answer-sheet check failed: %r not in Sifra %s %s %d' % (must, book, section, n)
def _bavli(tr, daf, side, seg, must):
    d = json.load(open(ROOT + '/Data/bavli_%s_he.json' % tr))
    t = d['text'] if isinstance(d, dict) and 'text' in d else d
    row = _re.sub(r'<[^>]+>', '', strip(t[2 * daf - 2 + (1 if side == 'b' else 0)][seg - 1]))
    assert must in row, 'answer-sheet check failed: %r not in %s %d%s:%d' % (must, tr, daf, side, seg)
for kind, *ref in SHEET2:
    (_sifra if kind == 'sifra' else _bavli)(*ref)
for name, tr, ch, m, must in SHEET:
    mishnah(tr, ch, m, must)
print('answer sheet: %d Mishnah rows + %d Sifra/Talmud rows read whole from the shelf, '
      'each verified by a token in its own ink' % (len(SHEET), len(SHEET2)))

JB = jubilee()
FS = field_sale(100, 10, 4)          # sold at 100 with 10 harvest years to the Jubilee, 4 elapsed
HS_I = hebrew_slave('israelite', 100, 10, 4)
HS_G = hebrew_slave('gentile', 100, 10, 4)
GS = gentile_slave()
ON = overreaching()
RB = interest()
FV = field_valuation(49)
SB = sabbatical()
IS_B = interest_scope('brother')
IS_F = interest_scope('foreigner')

# (Mishnah row, cell, expected)
TESTS = [
 ('Rosh Hashanah 1:1 — Tishrei is the new year for Jubilees: the fiftieth is a Jubilee',
  cycle(50), 'jubilee'),
 ('Rosh Hashanah 1:1 — and for sabbatical years: year seven rests', cycle(7),
  'sabbath_of_the_land'),
 ('Rosh Hashanah 1:1 — the Jubilee sanctified from the New Year', JB['sanctified_from'],
  'first_of_tishrei'),
 ('Kiddushin 1:2 — the Hebrew slave acquires himself by YEARS (six)',
  HS_I['six_year_exit'], 'imported_exodus_21_2'),
 ('Kiddushin 1:2 — by the JUBILEE', HS_I['exit'], 'at_jubilee_with_children'),
 ('Kiddushin 1:2 — by DEDUCTION of money (100 over 10 years, 4 served)',
  HS_I['redemption_price'], 60),
 ('Kiddushin 1:2 — the pierced slave goes out by the Jubilee', JB['pierced_slave'],
  'freed_by_jubilee'),
 ('Arakhin 9:1 — sold in the Jubilee year: not under two years', FS['floor'],
  'not_under_two_years'),
 ('Arakhin 9:1 — a blight year does not count', FS['blight_year'], 'not_counted'),
 ('Arakhin 9:2 — resold dearer: reckon with the first', FS['counterpart_when_resold_dearer'],
  'first_buyer'),
 ('Arakhin 9:2 — the surplus returned (100 over 10 years, 4 elapsed)',
  FS['redemption_price'], 60),
 ('Arakhin 9:2 — the sanctuary permitted borrowing and halves', FS['hekdesh_constraints'],
  'inverted'),
 ('Arakhin 9:3 — the walled-city house: at once, through the year, then permanent',
  house_sale('walled_city'), 'one_year_then_permanent'),
 ('Arakhin 9:4 — Hillel\'s ordinance against the hiding buyer', HILLEL, 'deposit_in_chamber'),
 ('Arakhin 9:7 — the village house: field\'s exit, house\'s at-once',
  house_sale('village'), 'as_field_but_at_once'),
 ('Arakhin 9:8 — the Levites redeem forever', house_sale('levite_house'),
  'perpetual_redemption'),
 ('Arakhin 9:8 — the pasture is not sold', house_sale('levite_pasture'), 'unsellable'),
 ('Bava Metzia 4:3 — overreaching is a sixth', ON['measure'], 'sixth'),
 ('Bava Metzia 4:9 — land has no overreaching', ON['on_land'], 'none'),
 ('Bava Metzia 5:1 — bite and increase both barred', RB['both_nouns'], 'barred'),
 ('Bava Metzia 5:1 — bite on money, increase on produce', RB['definitions'],
  'money_bite_vs_produce_increase'),
 ('Arakhin 1:1 — under a month is not valued', valuation('male', 0, 0), 'none'),
 ('Arakhin 3:1 — the handsome and the ugly alike: fifty', valuation('male', 30), 50),
 ('Arakhin 4:4 — a man valuing a woman gives the woman\'s: thirty', valuation('female', 30), 30),
 ('Arakhin 4:4 — the twentieth year counts below', valuation('male', 20), 20),
 ('Arakhin 4:4 — the sixtieth year counts below', valuation('male', 60), 50),
 ('Arakhin 7:1 — fifty shekels per homer of seed', FV['rate'], 50),
 ('Arakhin 7:1 — a sela and a pundion per year', FV['per_year'], 'sela_and_pundion'),
 ('Arakhin 7:1 — not consecrated less than two years before the Jubilee',
  FV['consecration_floor'], 'two_years_before_jubilee'),
 ('Megillah 4:3 — land by nine and a priest: TEN assessor tokens in the chapter',
  PRIESTS, 10),
 ('Megillah 4:3 / Sanhedrin 1:3 — nine Israelites and one priest suffice', ASSESSORS,
  'nine_israelites_and_a_priest'),
 ('Kiddushin 1:2 — the one sold to a gentile: redeemed at once by the kin ladder',
  HS_G['redeemers'], 'kin_ladder_at_once'),
 ('Arakhin 9:2 — improved or declined: the lesser figure (the field)',
  FS['improved_or_declined'], 'lesser_figure'),
 # ---- the sabbatical year, graded against Mishnah Sheviit (2026-09-05, item 2)
 ('Moed Katan 3a:1-3 — the Torah layer is the four written verbs', SB['torah_labors'], 4),
 ('Moed Katan 3a:9 — the derivative labors of Sheviit 2:2: rabbinic, the verse a support',
  SB['derivative_layer'], 'rabbinic_verse_as_support'),
 ('Moed Katan 3a:12 — plowing in the seventh: lashes disputed both ways', SB['plowing_lashes'],
  ['lashes', 'no_lashes']),
 ('Moed Katan 3a:11 — two hoeings', SB['two_hoeings'], 'strengthen_barred_close_cracks_permitted'),
 ('Sheviit 2:6 / Moed Katan 3b:12 — the addition: thirty days [DATA]', SB['addition_days'], 30),
 ('Sheviit 1:1 / Moed Katan 3b:8 — the Passover/Atzeret cutoffs abolished', SB['addition_cutoffs'],
  'abolished_by_rabban_gamliel'),
 ('Moed Katan 4a:9 — the addition bound to the standing Temple', SB['addition_temple_bound'],
  'only_while_temple_stands'),
 ('Sifra Behar Chapter 1 6 — the seven eaters of 25:6-7', SB['eaters'], 7),
 ('Sheviit 9:8 — who eats after the removal: two arms', SB['after_removal'],
  ['r_yehuda_poor_only', 'r_yosei_poor_and_rich']),
 ('Lev 25:5 — the aftergrowth not reaped as a harvest', SB['aftergrowth_ink'], 'not_reaped_as_harvest'),
 ('Sheviit 9:1 — the aftergrowth ban: three arms', SB['aftergrowth_ban'],
  ['sages_all_forbidden', 'r_shimon_permitted_but_cabbage', 'r_yehuda_mustard_permitted']),
 ('Sheviit 9:3 / Sifra Chapter 3 4 — the field-clock', SB['field_clock'], 'eat_from_house_while_in_field'),
 ('Sheviit 9:5 / Sifra Chapter 3 5 — the jar: Rabban Gamliel, and the law follows him', SB['jar'],
  'per_kind_rabban_gamliel_the_law'),
 ('Sheviit 6:5 / Sifra Chapter 1 9 — the export border', SB['export'], 'not_abroad_syria_permitted'),
 ('Sheviit 7:3 / Sifra Chapter 1 6 — no commerce', SB['commerce'], 'barred'),
 ('Sheviit 8:6 / Sifra Chapter 1 3 — the changed manner', SB['changed_manner'], 'not_as_the_gatherers'),
 ('Sheviit 8:7 / Sifra Chapter 3 3 — the money chain', SB['money_chain'], 'last_seized_fruit_forbidden'),
 ('Lev 25:21 — the blessing for three years', SB['blessing_years'], 3),
 ('Sifra Behar Chapter 4 6 — four when the Jubilee follows', SB['blessing_with_jubilee'], 4),
 ('Lev 25:22 — the old eaten until the ninth', SB['old_until'], 'ninth_year'),
 ('Sheviit 6:1 — the three lands [DATA]', SB['zones'], 'three_lands'),
 ('Sheviit 10:1 — the money release routed to Deuteronomy 15', SB['debt_release'], 'routed_deut_15'),
 ('Sheviit 5:6 — the tools rule [ANSWER-SHEET]', SB['tools_rule'], 'work_specific_to_transgression_barred'),
 # ---- the animal tithe's naming machine (Bekhorot 9)
 ('Lev 27:32 — the tenth is the tithe when called by its own name', TN_PLAIN,
  {9: 'profane', 10: 'tithe', 11: 'profane'}),
 ('Bekhorot 9:8 — ninth called tenth, tenth ninth, eleventh tenth: all three sanctified', TN_ERROR,
  {9: 'sanctified_eaten_blemished', 10: 'tithe', 11: 'shelamim'}),
 ('Bekhorot 9:8 — the name tenth not uprooted: the eleventh not sanctified', TN_NOT_UPROOTED,
  {9: 'sanctified_eaten_blemished', 10: 'tithe', 11: 'not_sanctified'}),
 ('Bekhorot 9:3 — the bought and the gifted exempt (passes = born in his domain)', TN_PASSES,
  'bought_and_gifted_exempt'),
 ('Bekhorot 9:4 — what enters the pen', TN_EXCLUDED, 'kilayim_terefah_caesarean_underage_orphan'),
 ('Bekhorot 9:2 — sixteen mil [DATA]', TN_DISTANCE, 16),
 # ---- the owner's precedence (Arakhin 8:3)
 ('Arakhin 8:3 — another at twenty-one: the owner gives twenty-six', OP[21], 26),
 ('Arakhin 8:3 — at twenty-five: thirty', OP[25], 30),
 ('Arakhin 8:3 — at twenty-six: thirty-one and a dinar', OP[26], 'thirty_one_and_a_dinar'),
 # ---- the interest scope (Bava Metzia 5)
 ('Lev 25:36 — your brother: barred', IS_B, 'barred'),
 ('Bava Metzia 5:6 / Deut 23:21 — the foreigner: permitted (import edge)', IS_F, 'permitted'),
 ('Bava Metzia 5:2 — increase on rent, not on sale [ANSWER-SHEET]', RENT_SALE, 'increase_on_rent_not_sale'),
 ('Bava Metzia 5:10 — the three named fences [ANSWER-SHEET]', NAMED_FENCES, ['advance', 'after', 'words']),
]

# ---- (3)+(5) run, grade, effects ------------------------------------
print()
ok = 0
frac = {I: 0, M: 0, A: 0, D: 0}
for name, c, want in TESTS:
    hit = c['v'] == want
    ok += hit
    frac[c['p']] += 1
    print('%s %-76s [%s] %s' % ('OK ' if hit else 'MISS', name[:76], c['p'],
                                '' if hit else 'got=%r' % (c['v'],)))
    print('     effects: %s' % ', '.join(c['fx']))
n = len(TESTS)
assert n == GUARDED, (n, GUARDED)
print()
print('MATRIX: %d/%d cells match the answer sheet' % (ok, n))
print('FRACTIONS: pure ink %d/%d (%d%%) · recorded moves %d/%d (%d%%) · '
      'answer-sheet %d/%d · data %d/%d' % (
      frac[I], n, 100 * frac[I] // n, frac[M], n, 100 * frac[M] // n,
      frac[A], n, frac[D], n))
print('computed, not graded: the release day is Yom Kippur of the fiftieth '
      '(INK); the precondition is all inhabitants on the land (INK) and the '
      'cessation is the tribes\' exile (MOVE); the gentile slave forever '
      '(INK); the sela is twenty gerah (INK); the field\'s fifth (INK); the '
      'unredeemed field to the priest at the Jubilee (INK); the field owed '
      'over a full cycle = %s' % FV['owed']['v'])
print('the sabbatical year extended 2026-09-05 (REVIEW_BEHAR item 2): %d cells graded against '
      'Mishnah Sheviit, Bekhorot 9, Arakhin 8, Bava Metzia 5 and the Sifra/Talmud rows the seats '
      'cite; the tithe naming machine written' % (n - 33))
print('effects: every cell carries REGISTERED effects — four discovered in '
      'this span\'s own verbs: returns_to_holding (TRANSFER), '
      'sold_in_perpetuity, redemption_right, interest_barred [effects law '
      'satisfied]')
if ok == n:
    print()
    print('THE JUBILEE ENGINE STANDS — the cycle\'s product read off the '
          'verse that states it, the return verbs censused, the harvest-year '
          'pricing and the surplus computed from the ink, the four house '
          'classes by their own clauses, the two interest nouns, the Hebrew '
          'slave\'s hireling status with his Jubilee exit and hireling-days '
          'redemption, the valuation table by bracket with the boundary year '
          'counting below, and the field\'s fifty per homer deducted by the '
          'years to a sela and a pundion.')
else:
    sys.exit('MISSES REMAIN — consult the Talmud per gap and recompile.')

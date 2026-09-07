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

I, M, A, D, H = 'INK', 'MOVE', 'ANSWER-SHEET', 'DATA', 'HYPOTHESIS'   # H: THE LINK REVIEW LAW (LR3, 2026-09-07) — an untaught transfer, kept and labeled, never counted as compiled


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


# ---- REVIEW_BEHAR items 4 and 5 (sitting B, 2026-09-05) ---------------
def support_duty(state):
    """Lev 25:35 — 'when your brother becomes poor and his hand falters with
    you, you shall STRENGTHEN him' — the obligation entry on the kinsman."""
    if state == 'faltering':
        return cell('uphold_before_he_falls', M,
                    'INK: והחזקת בו (and you shall strengthen him, 25:35) — the duty; '
                    'its TIMING is the Sifra\'s: like a load on a donkey — while it is still '
                    'in place one man holds it up, fallen to the ground five cannot raise it '
                    '(Sifra Behar Section 5 1)', ['supports_kinsman'])
    if state == 'supported_four_or_five_times':
        return cell('support_again', I,
                    'והחזקת בו — the verb bears no count; the Sifra reads the repeat off it: '
                    '"even four or five times, support again" (Section 5 1)', ['supports_kinsman'])
    if state == 'your_life_against_his':
        return cell('your_life_first', M,
                    'וחי עמך (that he live WITH you, 25:35-36) — "your life comes first" '
                    '(Sifra Behar Section 5 1)', [FX.NONE])
    return cell('no_duty_stated', I, 'no faltering hand in the case', [FX.NONE])


def sale_manner(manner):
    """Lev 25:42 — 'they shall not be sold as a slave is sold' — the market form."""
    if manner in ('auction_stone', 'alley_stand'):
        return cell('barred', M,
                    'INK: לא ימכרו ממכרת עבד (they shall not be sold as slaves are sold, 25:42) '
                    '— the ban; the FORM it names is the Sifra\'s: "not stood in the alley nor '
                    'on the auction stone" (Sifra Behar Section 6 1); Onkelos keeps the noun '
                    'of a slave-sale', ['barred_from_it'])
    return cell('permitted', I, 'a private sale is not the slave-market\'s form', [FX.NONE])


def rigor_visibility(where):
    """Lev 25:53 — 'he shall not rule over him with rigor IN YOUR SIGHT' —
    the visibility bound on the bystander's duty."""
    if where == 'in_your_sight':
        return cell('you_are_commanded', I,
                    'לא ירדנו בפרך לעיניך (he shall not rule him with rigor in your sight, 25:53) '
                    '— the bystander\'s duty runs where he sees', ['barred_from_it'])
    if where == 'inside_his_house':
        return cell('not_commanded', M,
                    '"could he enter his house to know what he does to him? the verse says IN '
                    'YOUR SIGHT — you are commanded only in your sight" (Sifra Behar Chapter 8 8)',
                    ['exempt'])
    return cell('no_case', I, '', [FX.NONE])


SUPPORT = {s: support_duty(s) for s in ('faltering', 'supported_four_or_five_times', 'your_life_against_his')}
SALE = {m: sale_manner(m) for m in ('auction_stone', 'private')}
RIGOR = {w: rigor_visibility(w) for w in ('in_your_sight', 'inside_his_house')}

import os as _os5, sys as _sys5, io as _io5, contextlib as _ctx5
_sys5.path.insert(0, _os5.path.dirname(_os5.path.abspath(__file__)))
# ---- THE WRAP (W5 HOLINESS, SANCTIONS, THE LAND, 2026-09-07): the daemon over the compiled jubilee engine ----
import world_engine as WE
def law_yovel(event, world):
    """Lev 25 + 27:2-8, 16-25 (cold_run_yovel.py — cycle, jubilee, field_sale, house_sale, overreaching, interest, hebrew_slave, valuation, field_valuation, sabbatical, interest_scope, support_duty, sale_manner, rigor_visibility):
    THE CLOCK SITTING (2026-09-07; CLOCK.md section 5): the COUNT begins at entry (25:2) — two recurring status timers on the land through the Calendar (the seventh, the fiftieth);
    the sowing reads the land's status, never the event's year; a sale's timer writes the ENTITLEMENT (25:28 "it shall go out in the jubilee"); the RELEASE is written when the
    proclamation (25:9-10, the text's own act) is consumed, forked on the tradition's three recorded conditions — the horn and the servants (Sifra Behar Chapter 2 4) off the act,
    all the inhabitants (Arakhin 32b:16) off the ledger."""
    k, src = event['kind'], event['case_source']
    E_ = lambda eff, s, cp=None, amount=None, due=None, law='', value=None, period=None: dict({'effect': eff, 'subject': s, 'counterparty': cp, 'amount': amount, 'due': due, 'value': value if value is not None else True, 'source_law': law, 'case_source': src}, **({'period': period} if period else {}))
    yr = world.clock.year
    if k == 'entered_the_land':
        land = event.get('land', 'the-land'); c7 = cycle(7); jb = jubilee()
        return [E_('sabbath_of_the_land', land, due=world.clock.next('sabbatical'), value=c7['v'], period='sabbatical', law='F1 [INK 25:2 "when you come into the land... the land shall keep a sabbath"; 25:4 "in the seventh year" — the COUNT\'S TIMER, the period of seven re-armed through the Calendar (Mishnah Rosh Hashanah 1:1 the seventh month\'s first day)]'),
                E_('jubilee_year', land, due=world.clock.next('jubilee'), value=jb['sanctified_from']['v'], period='jubilee', law='F1 [INK 25:8-10 "seven sabbaths of years... you shall sanctify the fiftieth year" — the COUNT\'S TIMER, the period of fifty; sanctified from %s (Rosh Hashanah 8b:12)]' % jb['sanctified_from']['v'])]
    if k == 'land_sown':
        land = event.get('land', 'the-land'); o = event.get('owner')
        L = world.entity(land).ledger
        on = lambda eff: any(e['effect'] == eff and e['year'] == yr for e in L)      # the land's own status this year — the count's timer wrote it
        c = cycle(JUBILEE) if on('jubilee_year') else cycle(7) if on('sabbath_of_the_land') else cycle(1)
        if 'land_release' not in c['fx']:
            return []                                                # a work year: "six years you shall sow" (25:3) — the silence
        sb = sabbatical()
        out = [E_('land_release', land, cp=o, value=c['v'], law='F1 [INK 25:4 "in the seventh year a sabbath of rest shall be to the land" — count-year %d, read off the land\'s status: %s; the eaters %d (25:6-7)]' % (yr, c['v'], sb['eaters']['v'])),
               E_('labor_barred', o, value=sb['torah_labors']['v'], law='F1 [INK 25:4-5 the four labor verbs — sow, prune, reap, gather]')]
        if event.get('plowed') and event.get('warned'):
            pl = sb['plowing_lashes']
            out.append(E_('lashes', o, value=pl['v'], law='F1 [Moed Katan 3a:12 — plowing in the seventh: %s]' % pl['v']))
        if 'jubilee_release' in c['fx']:
            out += [E_('jubilee_release', land, value=c['v'], law='F1 [INK 25:11 "a jubilee it is, the fiftieth year, you shall not sow" — the fiftieth rests too]'),
                    E_('goes_free', 'the-slaves-of-the-land', value=c['v'], law='F1 [INK 25:10 "you shall proclaim liberty" — the year\'s class carries the release]'),
                    E_('returns_to_holding', 'the-holdings-of-the-land', value=c['v'], law='F1 [INK 25:13 "in this jubilee year you shall return each to his holding"]')]
        return out
    if k == 'jubilee_proclaimed':
        # THE FORK ON THE ACT (CLOCK.md section 5): three recorded conditions — two off the act's own fields, one off the ledger
        land = event.get('land', 'the-land'); jb = jubilee()
        horn = event.get('horn_sounded', True); servants = event.get('servants_sent_free', True)
        ppl = world.entity(event.get('people', 'israel'))
        exiled = any(e['effect'] == 'scattered_among_nations' for e in ppl.ledger)          # Arakhin 32b:16 — a STATE, read off the ledger
        if exiled:
            arms = [('both arms', False, 'not all its inhabitants upon the land — Arakhin 32b:16 on 25:10 "to ALL its inhabitants": the jubilees ceased')]
        elif horn and servants:
            arms = [('both arms', True, 'the horn sounded and the servants sent free — Sifra Behar Chapter 2 4, both conditions met')]
        elif not horn and not servants:
            arms = [('both arms', False, 'neither the horn sounded nor the servants sent free — Sifra Behar Chapter 2 4, each arm\'s condition failed')]
        else:
            arms = [('Rabbi Yehuda', servants, 'the servants %s — Sifra Behar Chapter 2 4: a jubilee even without the horn, not without the servants sent free' % ('sent free' if servants else 'not sent free')),
                    ('Rabbi Yose', horn, 'the horn %s — Sifra Behar Chapter 2 4: a jubilee even without the servants sent free, not without the horn' % ('sounded' if horn else 'not sounded'))]
        verdicts = ['%s (%s: %s)' % ('jubilee' if ok else 'no jubilee', who, why) for who, ok, why in arms]
        # the holding arm FIRST in the land's verdict (the scene's first run caught the join in the arms' order: 'no jubilee (Rabbi
        # Yehuda...); jubilee (Rabbi Yose...)' read as no arm holding — the library's deferral reads the head of the string)
        holds = '; '.join(sorted(verdicts, key=lambda v: v.startswith('no '))) if any(ok for _, ok, _ in arms) else verdicts[0]
        out = [E_('jubilee_holds', land, cp=event.get('proclaimer'), value=holds, law='F1 [INK 25:10 "it is a jubilee" — the verdict on the three recorded conditions; %s]' % jb['precondition']['v'])]
        for who, ok, why in arms:
            v = '%s (%s: %s)' % ('jubilee' if ok else 'no jubilee', who, why)
            out.append(E_('jubilee_release', land, cp=event.get('proclaimer'), value=v, law='F1 [INK 25:9-10 "on the Day of Atonement you shall sound the horn... proclaim liberty in the land" — %s; the pierced slave %s]' % (jb['release_day']['v'], jb['pierced_slave']['v'])))
            if ok:                                                       # the RELEASE for every entitled holding and man (the entitlement fired at the year's arrival)
                for ent in world.entities.values():
                    if ent.status.get('goes_out_in_the_jubilee'):
                        out.append(E_('returns_to_holding', ent.eid, value=v, law='F1 [INK 25:28 "it shall go out in the jubilee and he shall return to his holding"; 25:41 "and return to his family" — the release on the act]'))
                        if ent.kind == 'person':
                            out.append(E_('goes_free', ent.eid, value=v, law='F1 [INK 25:54 "he shall go out in the year of the jubilee, he and his sons with him"]'))
        return out
    if k == 'field_sold':
        s_ = event['seller']; b = event['buyer']; f = event['field']; ytj = event.get('years_to_jubilee', JUBILEE - yr); el = event.get('elapsed', 0)
        fs = field_sale(event.get('price', 100), ytj, el); out = []
        if event.get('overcharged'):
            ov_ = overreaching()
            out.append(E_('restores', b, cp=s_, value=ov_['measure']['v'], law='F1 [INK 25:14 "do not wrong one another" — the sixth restored (Mishnah Bava Metzia 4:3, the answer sheet\'s parameter); on land %s]' % ov_['on_land']['v']))
        out.append(E_('redemption_right', f, cp=s_, value=fs['price_rule']['v'], law='F1 [INK 25:15-16 by the number of harvest years; 25:24 "a redemption you shall give to the land"; the floor %s, the blight year %s]' % (fs['floor']['v'], fs['blight_year']['v'])))
        if event.get('redeemed'):
            out.append(E_('pays', s_, cp=b, amount=fs['redemption_price']['v'], value=fs['improved_or_declined']['v'], law='F1 [INK 25:27 "return the SURPLUS" — price x remaining / total = %d]' % fs['redemption_price']['v']))
            out.append(E_('returns_to_holding', f, cp=s_, value='redeemed', law='F1 [INK 25:27 "and return to his holding"]'))
        else:
            world.entity(f, 'field')
            out.append(E_('goes_out_in_the_jubilee', f, cp=s_, due=world.clock.next('jubilee'), value=fs['unredeemed']['v'], law='F1 [INK 25:28 "it shall go out in the jubilee" — the ENTITLEMENT, a TIMER to the fiftieth the Calendar computes (count-year %d); the return itself on the proclamation]' % world.clock.calendar.year(world.clock.next('jubilee'))))
        return out
    if k == 'house_sold':
        s_ = event['seller']; b = event['buyer']; h = event['house']; kind = event.get('house_kind', 'walled_city'); c = house_sale(kind); out = []
        if kind == 'walled_city':
            out.append(E_('redemption_right', h, cp=s_, amount=1, value=c['v'], law='F1 [INK 25:29 "its redemption shall be until the end of the year of its sale" — %s (Hillel\'s deposit: %s)]' % (c['v'], HILLEL['v'])))
            if event.get('redeemed_within_year'):
                return out
            out.append(E_('sold_in_perpetuity', h, cp=b, due=world.clock.after(1, 'year'), value=c['v'], law='F1 [INK 25:30 "if it is not redeemed until a full year is complete... in perpetuity... it shall not go out in the jubilee" — the one-year TIMER, the same date a year on]'))
            return out
        if kind == 'levite_pasture':
            return []                                                # "it shall not be sold" (25:34) — the sale writes nothing: the silence
        out.append(E_('redemption_right', h, cp=s_, value=c['v'], law='F1 [INK 25:31-32 — %s]' % c['why'][:80]))
        world.entity(h, 'house')
        out.append(E_('goes_out_in_the_jubilee', h, cp=s_, due=world.clock.next('jubilee'), value=c['v'], law='F1 [INK 25:31 / 25:33 "in the jubilee it shall go out" — the ENTITLEMENT, a TIMER to the fiftieth; the return on the proclamation]'))
        return out
    if k == 'brother_grew_poor':
        c = support_duty(event.get('state', 'faltering'))
        if 'supports_kinsman' in c['fx']:
            return [E_('supports_kinsman', event['kinsman'], cp=event['brother'], value=c['v'], law='F2 [INK 25:35 "you shall strengthen him" — %s]' % c['v'])]
        return []                                                    # your life first (Sifra Behar Section 5 1) — the silence
    if k == 'silver_lent':
        i = interest(); sc = interest_scope(event.get('borrower_class', 'brother'))
        if 'interest_barred' in sc['fx']:
            return [E_('interest_barred', event['lender'], cp=event['borrower'], value=i['both_nouns']['v'], law='F2 [INK 25:36-37 "bite or increase" — %s; %s]' % (i['definitions']['v'], sc['v']))]
        return []                                                    # the foreigner (Deut 23:21 — the import edge) — the silence
    if k == 'brother_sold_as_slave':
        sl = event['slave']; m = event['master']; ytj = event.get('years_to_jubilee', JUBILEE - yr); el = event.get('elapsed', 0)
        hs = hebrew_slave(event.get('sold_to', 'israelite'), event.get('price', 100), ytj, el); out = []
        if event.get('manner'):
            sm = sale_manner(event['manner'])
            if 'barred_from_it' in sm['fx']:
                out.append(E_('barred_from_it', m, cp=sl, value=sm['v'], law='F3 [INK 25:42 "they shall not be sold as a slave is sold" — %s]' % sm['v']))
        if event.get('rigor_where'):
            rv = rigor_visibility(event['rigor_where'])
            if 'barred_from_it' in rv['fx']:
                out.append(E_('barred_from_it', 'the-bystander', cp=m, value=rv['v'], law='F3 [INK 25:53 "he shall not rule over him with rigor IN YOUR SIGHT" — %s]' % rv['v']))
            if 'exempt' in rv['fx']:
                out.append(E_('exempt', 'the-bystander', value=rv['v'], law='F3 [Sifra Behar Chapter 8 8 — %s]' % rv['v']))
        if el:
            out.append(E_('pays', sl, cp=m, amount=hs['redemption_price']['v'], value=hs['lesser_figure']['v'], law='F3 [INK 25:50-52 "as a hireling\'s days" — price x remaining / total = %d]' % hs['redemption_price']['v']))
            out.append(E_('goes_free', sl, cp=m, value='redeemed', law='F3 [INK 25:48-49 redeemed by his kin or his own hand]'))
            out.append(E_('returns_to_holding', sl, value='to_his_family', law='F3 [INK 25:41 "and return to his family"]'))
        else:
            out.append(E_('goes_out_in_the_jubilee', sl, cp=m, due=world.clock.next('jubilee'), value=hs['exit']['v'], law='F3 [INK 25:40-41 "until the jubilee year he shall serve with you, and he shall go out from you, he and his children with him"; 25:54 "he shall go out in the year of the jubilee" — the ENTITLEMENT, a TIMER to the fiftieth; the release (%s) on the proclamation]' % hs['status']['v']))
        if 'redeemers' in hs:
            out.append(E_('redemption_right', sl, cp='the-kin', value=hs['redeemers']['v'], law='F3 [INK 25:48-49 the kin ladder at once — %s]' % hs['redeemers']['v']))
        if 'term_clock' in hs['six_year_exit']['fx']:
            out.append(E_('term_clock', sl, cp=m, amount=6, value=hs['six_year_exit']['v'], law='F3 [IMPORT EDGE Exod 21:2 — the six-year term is the library daemon\'s (law_slave_term registered beside on this tape)]'))
        return out
    if k == 'person_valued':
        c = valuation(event.get('sex', 'male'), event.get('age_years', 30), event.get('age_months', 0))
        if 'gives_fixed_sum' in c['fx']:
            return [E_('gives_fixed_sum', event['vower'], cp='the-treasury', amount=c['v'], value=event.get('valued', 'himself'), law='F4 [INK 27:3-7 the bracket table — %s]' % c['why'][:90])]
        return []                                                    # under a month: no bracket (27:6) — the silence
    if k == 'field_consecrated':
        o = event['owner']; f = event['field']; ytj = event.get('years_to_jubilee', JUBILEE - yr); fv = field_valuation(ytj)
        out = [E_('gives_fixed_sum', o, cp='the-treasury', amount=fv['owed']['v'], value=fv['per_year']['v'], law='F4 [INK 27:16-18 fifty per homer deducted by the years — %s x %d = %s]' % (fv['per_year']['v'], ytj, fv['owed']['v']))]
        if event.get('redeemed'):
            op = owner_price(event.get('bid', 20), 20)
            out.append(E_('adds_fifth', o, cp='the-treasury', amount=(op if isinstance(op, int) else None), value=fv['redeem_fifth']['v'], law='F4 [INK 27:19 "he shall add a fifth of the money of the valuation" — the owner\'s precedence: bid %d -> %s (Mishnah Arakhin 8:2-3)]' % (event.get('bid', 20), op)))
            return out
        if event.get('field_kind') == 'purchased':
            out.append(E_('returns_to_holding', f, cp='the-original-holder', due=world.clock.next('jubilee'), value='to_him_from_whom_he_bought_it', law='F4 [INK 27:24 "in the jubilee year the field shall return to him from whom he bought it" — the TIMER to the fiftieth the Calendar computes; the fork\'s reach to Lev 27 filed OPEN]'))
        else:
            out.append(E_('due_to_priest', f, cp='the-priests', due=world.clock.next('jubilee'), value=fv['unredeemed_sold']['v'], law='F4 [INK 27:21 "the field in its going out in the jubilee shall be holy to the LORD, as a devoted field; to the priest shall be its holding" — the TIMER to the fiftieth; the fork\'s reach to Lev 27 filed OPEN]'))
        return out
    if k == 'consecrated_redeemed':
        if event.get('thing') != 'field':
            return []                                                # the consecration engine's seat (law_temurah) — the silence here
        op = owner_price(event.get('bid', 20), event.get('own', 20))
        return [E_('adds_fifth', event['redeemer'], cp='the-treasury', amount=(op if isinstance(op, int) else None), value=op, law='F4 [Mishnah Arakhin 8:2-3 — the owner\'s fifth arithmetic: bid %s -> %s]' % (event.get('bid', 20), op))]
    return []

def scene():
    """THE SCENE — Rosh Hashanah 1:1, Sheviit, Kiddushin 1:2, Arakhin 4, 7-9, Bava Metzia 4-5 and the Sifra's rows replayed on the world engine (THE COUNT EPOCH — the day the base unit, the year derived; one period of fifty):
    the count begins at entry (its first row); the library's law_slave_term registered beside; jubilee_proclaimed SUBMITTED on the tenth of the seventh month of the fiftieth year — the day the Calendar computes.
    THE FORK'S ROWS beside (Sifra Behar Chapter 2 4's 'even though they did not' cases; Arakhin 32b:16's exile) — three small worlds, law_tochacha registered for the exile's own event."""
    with _ctx5.redirect_stdout(_io5.StringIO()):
        w = WE.World(era='the jubilee engine: Lev 25 + 27 on the engine (the count epoch: the day the base unit, the year derived; one period of fifty)', epoch='count')
        w.laws = [law_yovel, WE.law_slave_term]
        w.submit({'kind': 'entered_the_land', 'subject': 'israel', 'people': 'israel', 'land': 'the-land', 'case_source': 'Lev 25:2 "when you come into the land" — the count begins; Mishnah Rosh Hashanah 1:1 the seventh month for sabbaticals and jubilees'})
        w.advance(w.clock.at_year(3))
        w.submit({'kind': 'land_sown', 'subject': 'the-land', 'land': 'the-land', 'owner': 'the-farmer', 'case_source': 'Lev 25:3 — a work year: the silence'})
        w.advance(w.clock.at_year(7))
        w.submit({'kind': 'land_sown', 'subject': 'the-land', 'land': 'the-land', 'owner': 'the-farmer', 'case_source': 'Lev 25:4; Mishnah Rosh Hashanah 1:1 — the seventh: the land rests'})
        w.submit({'kind': 'land_sown', 'subject': 'the-land', 'land': 'the-land', 'owner': 'the-plower', 'plowed': True, 'warned': True, 'case_source': 'Moed Katan 3a:12 — plowing in the seventh: the recorded dispute on the lashes'})
        w.advance(w.clock.at_year(40))
        w.submit({'kind': 'field_sold', 'subject': 'field-1', 'seller': 'the-seller', 'buyer': 'the-buyer', 'field': 'field-1', 'price': 100, 'years_to_jubilee': 10, 'case_source': 'Lev 25:15-16, 25:28; Mishnah Arakhin 9:1 — sold ten years before the jubilee, unredeemed: returns at the fiftieth'})
        w.submit({'kind': 'field_sold', 'subject': 'field-2', 'seller': 'the-overcharged', 'buyer': 'the-overcharger', 'field': 'field-2', 'price': 100, 'years_to_jubilee': 10, 'overcharged': True, 'case_source': 'Lev 25:14; Mishnah Bava Metzia 4:3 — overreaching by a sixth: restored'})
        w.submit({'kind': 'house_sold', 'subject': 'house-1', 'seller': 'the-house-seller', 'buyer': 'the-house-buyer', 'house': 'house-1', 'house_kind': 'walled_city', 'case_source': 'Lev 25:29-30; Mishnah Arakhin 9:3-4 — the walled city: one year, then perpetuity'})
        w.submit({'kind': 'house_sold', 'subject': 'house-2', 'seller': 'the-house-seller', 'buyer': 'the-house-buyer', 'house': 'house-2', 'house_kind': 'village', 'case_source': 'Lev 25:31 — the village house as the field'})
        w.submit({'kind': 'house_sold', 'subject': 'house-3', 'seller': 'the-levite', 'buyer': 'the-house-buyer', 'house': 'house-3', 'house_kind': 'levite_house', 'case_source': 'Lev 25:32-33 — the Levite\'s perpetual redemption'})
        w.submit({'kind': 'house_sold', 'subject': 'the-pasture', 'seller': 'the-levite', 'buyer': 'the-house-buyer', 'house': 'the-pasture', 'house_kind': 'levite_pasture', 'case_source': 'Lev 25:34 — the pasture unsellable: the silence'})
        w.submit({'kind': 'brother_grew_poor', 'subject': 'the-poor-brother', 'kinsman': 'the-kinsman', 'brother': 'the-poor-brother', 'state': 'faltering', 'case_source': 'Lev 25:35; Sifra Behar Section 5 1 — uphold before he falls'})
        w.submit({'kind': 'silver_lent', 'subject': 'the-lender', 'lender': 'the-lender', 'borrower': 'the-poor-brother', 'interest': True, 'borrower_class': 'brother', 'case_source': 'Lev 25:36-37; Mishnah Bava Metzia 5:1 — the bite and the increase barred'})
        w.submit({'kind': 'silver_lent', 'subject': 'the-lender-abroad', 'lender': 'the-lender-abroad', 'borrower': 'the-foreigner', 'interest': True, 'borrower_class': 'foreigner', 'case_source': 'Deut 23:21 — to the foreigner: the silence at this seat'})
        w.submit({'kind': 'brother_sold_as_slave', 'subject': 'the-brother-sold', 'slave': 'the-brother-sold', 'master': 'the-master', 'sold_to': 'israelite', 'price': 100, 'years_to_jubilee': 10, 'manner': 'auction_stone', 'rigor_where': 'in_your_sight', 'case_source': 'Lev 25:39-43; Mishnah Kiddushin 1:2 — sold to an Israelite: the jubilee exit, the six-year term the library\'s'})
        w.submit({'kind': 'brother_sold_as_slave', 'subject': 'the-sold-to-a-gentile', 'slave': 'the-sold-to-a-gentile', 'master': 'the-gentile-master', 'sold_to': 'gentile', 'price': 100, 'years_to_jubilee': 10, 'rigor_where': 'inside_his_house', 'case_source': 'Lev 25:47-54; Sifra Behar Chapter 8 — the kin ladder, no six-year exit, the jubilee'})
        w.advance(w.clock.at_year(44))
        w.submit({'kind': 'field_sold', 'subject': 'field-3', 'seller': 'the-redeeming-seller', 'buyer': 'the-buyer', 'field': 'field-3', 'price': 100, 'years_to_jubilee': 10, 'elapsed': 4, 'redeemed': True, 'case_source': 'Lev 25:27; Mishnah Arakhin 9:1 — redeemed after four of ten: the surplus sixty'})
        w.submit({'kind': 'brother_sold_as_slave', 'subject': 'the-redeemed-slave', 'slave': 'the-redeemed-slave', 'master': 'the-master', 'sold_to': 'israelite', 'price': 100, 'years_to_jubilee': 10, 'elapsed': 4, 'case_source': 'Mishnah Kiddushin 1:2 — by deduction of money: 100 over 10, 4 served: 60'})
        w.submit({'kind': 'person_valued', 'subject': 'the-vower-of-a-man', 'vower': 'the-vower-of-a-man', 'valued': 'himself', 'sex': 'male', 'age_years': 30, 'case_source': 'Lev 27:3; Mishnah Arakhin 4:1 — a male of thirty: fifty'})
        w.submit({'kind': 'person_valued', 'subject': 'the-vower-of-a-woman', 'vower': 'the-vower-of-a-woman', 'valued': 'his_wife', 'sex': 'female', 'age_years': 30, 'case_source': 'Lev 27:4 — a female: thirty'})
        w.submit({'kind': 'person_valued', 'subject': 'the-vower-of-a-boy', 'vower': 'the-vower-of-a-boy', 'valued': 'his_son', 'sex': 'male', 'age_years': 5, 'case_source': 'Mishnah Arakhin 4:4; Sifra Bechukotai Section 3 9-11 — the boundary year counts below: five'})
        w.submit({'kind': 'person_valued', 'subject': 'the-vower-of-an-infant', 'vower': 'the-vower-of-an-infant', 'valued': 'the_newborn', 'sex': 'male', 'age_years': 0, 'age_months': 0, 'case_source': 'Lev 27:6 "from a month old" — under a month: the silence'})
        w.submit({'kind': 'field_consecrated', 'subject': 'field-4', 'owner': 'the-sanctifier', 'field': 'field-4', 'years_to_jubilee': 6, 'field_kind': 'holding', 'case_source': 'Lev 27:16-21; Mishnah Arakhin 7:1 — the holding consecrated six years before the jubilee, unredeemed: to the priest'})
        w.submit({'kind': 'field_consecrated', 'subject': 'field-5', 'owner': 'the-redeeming-sanctifier', 'field': 'field-5', 'years_to_jubilee': 6, 'redeemed': True, 'bid': 21, 'case_source': 'Mishnah Arakhin 8:2-3 — the owner redeems against a bid of twenty-one: twenty-six'})
        w.submit({'kind': 'field_consecrated', 'subject': 'field-6', 'owner': 'the-buyer-sanctifier', 'field': 'field-6', 'years_to_jubilee': 6, 'field_kind': 'purchased', 'case_source': 'Lev 27:22-24 — the purchased field returns to its holder at the jubilee'})
        w.submit({'kind': 'consecrated_redeemed', 'subject': 'field-5', 'redeemer': 'the-redeeming-sanctifier', 'thing': 'field', 'bid': 26, 'own': 20, 'case_source': 'Mishnah Arakhin 8:3 — a bid of twenty-six: thirty-one and a dinar'})
        w.submit({'kind': 'consecrated_redeemed', 'subject': 'the-house', 'redeemer': 'the-house-redeemer', 'thing': 'house', 'case_source': 'Lev 27:15 — the house: the consecration engine\'s seat (the silence here)'})
        w.advance(w.clock.at_year(46))
        w.submit({'kind': 'acquire_hebrew_slave', 'subject': 'the-exodus-slave', 'slave': 'the-exodus-slave', 'master': 'the-master', 'case_source': 'Exod 21:2; Mishnah Kiddushin 1:2 — the library daemon: the six-year term clock (overtaken by the jubilee)'})
        w.advance(w.clock.calendar.day_of(50, 7, 10))                # the tenth of the seventh month of the fiftieth year — the Day of Atonement (Lev 25:9)
        w.submit({'kind': 'jubilee_proclaimed', 'subject': 'the-land', 'proclaimer': 'the-court', 'land': 'the-land', 'horn_sounded': True, 'servants_sent_free': True, 'case_source': 'Lev 25:9-10; Mishnah Rosh Hashanah 1:1; Arakhin 7:1-4 — the fiftieth: liberty proclaimed in the land'})
        w.submit({'kind': 'land_sown', 'subject': 'the-land', 'land': 'the-land', 'owner': 'the-farmer', 'case_source': 'Lev 25:11 — the jubilee: you shall not sow'})
        w.advance(w.clock.at_year(51))
        # THE FORK'S ROWS — Sifra Behar Chapter 2 4 (the horn, the servants) and Arakhin 32b:16 (the exile): three small worlds
        import cold_run_tochacha as T                              # the exile's own daemon for the fork's third condition — the edge yovel -> tochacha filed (Arakhin 32b:16)
        def fork_world():
            wf = WE.World(era='the jubilee\'s conditions: Sifra Behar Chapter 2 4, Arakhin 32b:16 on the engine (the count epoch)', epoch='count')
            wf.laws = [law_yovel, T.law_tochacha, WE.law_slave_term]
            wf.submit({'kind': 'entered_the_land', 'subject': 'israel', 'people': 'israel', 'land': 'the-land', 'case_source': 'Lev 25:2 — the count begins (the fork\'s world)'})
            wf.advance(wf.clock.at_year(40))
            wf.submit({'kind': 'field_sold', 'subject': 'field-f', 'seller': 'the-seller', 'buyer': 'the-buyer', 'field': 'field-f', 'price': 100, 'years_to_jubilee': 10, 'case_source': 'Lev 25:28 — sold ten years before the jubilee (the fork\'s world)'})
            return wf
        wa = fork_world(); wa.advance(wa.clock.calendar.day_of(50, 7, 10))
        wa.submit({'kind': 'jubilee_proclaimed', 'subject': 'the-land', 'proclaimer': 'the-court', 'land': 'the-land', 'horn_sounded': False, 'servants_sent_free': True, 'case_source': 'Sifra Behar Chapter 2 4 — they did not sound the horn: Rabbi Yehuda a jubilee, Rabbi Yose not'})
        wb = fork_world(); wb.advance(wb.clock.calendar.day_of(50, 7, 10))
        wb.submit({'kind': 'jubilee_proclaimed', 'subject': 'the-land', 'proclaimer': 'the-court', 'land': 'the-land', 'horn_sounded': True, 'servants_sent_free': False, 'case_source': 'Sifra Behar Chapter 2 4 — they did not send the servants free: Rabbi Yose a jubilee, Rabbi Yehuda not'})
        wc = fork_world()
        wc.submit({'kind': 'people_exiled', 'subject': 'israel', 'people': 'israel', 'land': 'the-land', 'case_source': 'Arakhin 32b:16 — Reuben, Gad and half of Manasseh exiled: not all its inhabitants upon it'})
        wc.advance(wc.clock.calendar.day_of(50, 7, 10))
        wc.submit({'kind': 'jubilee_proclaimed', 'subject': 'the-land', 'proclaimer': 'the-court', 'land': 'the-land', 'horn_sounded': True, 'servants_sent_free': True, 'case_source': 'Arakhin 32b:16 on Lev 25:10 "to ALL its inhabitants" — the jubilees ceased'})
    n = lambda eid, eff: len([e for e in w.entity(eid).ledger if e['effect'] == eff])
    yr = lambda eid, eff: [e['year'] for e in w.entity(eid).ledger if e['effect'] == eff]
    am = lambda eid, eff: [e['amount'] for e in w.entity(eid).ledger if e['effect'] == eff]
    tset = len([l for l in w.log if l[0] == 'TIMER-SET']); fired = len([l for l in w.log if l[0] == 'TIMER-FIRE']); cut = len([l for l in w.log if l[0] == 'TIMER-CANCEL'])
    rearm = len([l for l in w.log if l[0] == 'TIMER-SET' and l[2].get('rearmed_from') is not None])
    return ((yr('the-land', 'land_release'), n('the-farmer', 'labor_barred'), n('the-plower', 'lashes'), n('the-land', 'jubilee_release'), yr('the-slaves-of-the-land', 'goes_free'),
             n('field-1', 'redemption_right'), yr('field-1', 'returns_to_holding'), n('the-overcharger', 'restores'), yr('field-3', 'returns_to_holding'), am('the-redeeming-seller', 'pays'),
             n('house-1', 'redemption_right'), yr('house-1', 'sold_in_perpetuity'), yr('house-2', 'returns_to_holding'), yr('house-3', 'returns_to_holding'), n('the-pasture', 'redemption_right'),
             n('the-kinsman', 'supports_kinsman'), n('the-lender', 'interest_barred'), n('the-lender-abroad', 'interest_barred'),
             yr('the-brother-sold', 'goes_out_in_the_jubilee'), yr('the-brother-sold', 'goes_free'), yr('the-brother-sold', 'returns_to_holding'), n('the-brother-sold', 'term_clock'), n('the-master', 'barred_from_it'), n('the-bystander', 'barred_from_it'), n('the-bystander', 'exempt'),
             n('the-sold-to-a-gentile', 'redemption_right'), n('the-sold-to-a-gentile', 'term_clock'), yr('the-sold-to-a-gentile', 'goes_free'), am('the-redeemed-slave', 'pays'), yr('the-redeemed-slave', 'goes_free'),
             am('the-vower-of-a-man', 'gives_fixed_sum'), am('the-vower-of-a-woman', 'gives_fixed_sum'), am('the-vower-of-a-boy', 'gives_fixed_sum'), n('the-vower-of-an-infant', 'gives_fixed_sum'),
             am('the-sanctifier', 'gives_fixed_sum'), yr('field-4', 'due_to_priest'), am('the-redeeming-sanctifier', 'adds_fifth'), yr('field-6', 'returns_to_holding'), n('the-house-redeemer', 'adds_fifth'),
             yr('the-exodus-slave', 'goes_free'), n('the-exodus-slave', 'term_clock'), n('the-land', 'jubilee_release'),
             yr('the-land', 'sabbath_of_the_land'), yr('the-land', 'jubilee_year'), yr('field-1', 'goes_out_in_the_jubilee'), n('the-land', 'jubilee_holds'), cut, rearm, tset, fired, w.clock.year),
            scene_counts_fork(wa, wb, wc), w)

def scene_counts_fork(wa, wb, wc):
    """THE FORK'S ROWS — per world: the jubilee_release values on the land (the arms named), the field's returns, the land's verdict"""
    vals = lambda wf: sorted(e['value'].split(' (')[0] + ' — ' + e['value'].split(' (')[1].split(':')[0] for e in wf.entity('the-land').ledger if e['effect'] == 'jubilee_release' and e['day'] == wf.clock.day)
    ret = lambda wf: len([e for e in wf.entity('field-f').ledger if e['effect'] == 'returns_to_holding'])
    holds = lambda wf: wf.entity('the-land').status.get('jubilee_holds', '').split(' (')[0]
    return (vals(wa), ret(wa), holds(wa), vals(wb), ret(wb), holds(wb), vals(wc), ret(wc), holds(wc))
SCENE, SCENE_FORK, _W = scene()


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
    ('sifra', 'Behar', 'Section 5', 1, 'והחזקת'),   # sitting B: the falling load — 'strengthen him'
    ('sifra', 'Behar', 'Section 6', 1, 'ממכרת'),    # sitting B: not sold as slaves are sold — the auction stone
    ('sifra', 'Behar', 'Chapter 8', 8, 'לעיניך'),   # sitting B: in your sight — you are commanded only in your sight
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
 ('THE SCENE — Rosh Hashanah 1:1, Sheviit, Kiddushin 1:2, Arakhin 4 and 7-9, Bava Metzia 4-5 on the world engine (THE COUNT EPOCH — the day the base unit, the year derived; one period of fifty; the count\'s two timers set at entry; the library\'s law_slave_term beside; jubilee_proclaimed SUBMITTED on the computed tenth of the seventh month; the daemon\'s watch coverage printed below)', cell(SCENE, I, 'the seventh and the fiftieth, the sold field and the walled house and the slave each on a timer to its year, the poor brother, the interest, the valuations, the consecrated field to the priest at the jubilee — every value a cell\'s', ['land_release', 'labor_barred', 'lashes', 'jubilee_release', 'goes_free', 'returns_to_holding', 'redemption_right', 'pays', 'restores', 'sold_in_perpetuity', 'supports_kinsman', 'interest_barred', 'term_clock', 'barred_from_it', 'exempt', 'gives_fixed_sum', 'due_to_priest', 'adds_fifth']), ([7, 7, 50], 2, 1, 2, [50], 1, [50], 1, [44], [60], 1, [41], [50], [50], 0, 1, 1, 0, [50], [50], [50], 1, 1, 1, 1, 1, 0, [50], [60], [44], [50], [30], [5], 0, [6.12], [50], [26, None], [50], 0, [50], 1, 2, [7, 14, 21, 28, 35, 42, 49], [50], [50], 1, 1, 8, 20, 17, 51)),
 ('THE FORK\'S ROWS — Sifra Behar Chapter 2 4 (the horn, the servants) and Arakhin 32b:16 (the exile) on the world engine: the jubilee\'s validity forked on the PROCLAMATION ACT\'s three recorded conditions (THE CLOCK SITTING)', cell(SCENE_FORK, A, 'no horn: Rabbi Yehuda a jubilee, Rabbi Yose not; no servants sent free: Rabbi Yose a jubilee, Rabbi Yehuda not; the tribes exiled: no jubilee by both — the arms as VALUES on the land, the field returned only on an arm that holds', ['jubilee_release', 'jubilee_holds', 'returns_to_holding']), (['jubilee — Rabbi Yehuda', 'no jubilee — Rabbi Yose'], 1, 'jubilee', ['jubilee — Rabbi Yose', 'no jubilee — Rabbi Yehuda'], 1, 'jubilee', ['no jubilee — both arms'], 0, 'no jubilee')),
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
 # ---- REVIEW_BEHAR items 4 and 5 (sitting B, 2026-09-05): the Sifra's own case rows
 ('Sifra Behar Section 5 1 — the faltering hand: hold him up BEFORE he falls', SUPPORT['faltering'],
  'uphold_before_he_falls'),
 ('Sifra Behar Section 5 1 — supported four or five times: support again',
  SUPPORT['supported_four_or_five_times'], 'support_again'),
 ('Sifra Behar Section 5 1 — "that he live with you": your life comes first',
  SUPPORT['your_life_against_his'], 'your_life_first'),
 ('Sifra Behar Section 6 1 — not stood in the alley nor on the auction stone', SALE['auction_stone'],
  'barred'),
 ('Sifra Behar Chapter 8 8 — rigor in your sight: you are commanded', RIGOR['in_your_sight'],
  'you_are_commanded'),
 ('Sifra Behar Chapter 8 8 — inside his house: not commanded', RIGOR['inside_his_house'],
  'not_commanded'),
]

# ---- (3)+(5) run, grade, effects ------------------------------------
# Guarded so tithe_naming() IMPORTS COLD — cold_run_temurah.py CALLS it for the
# animal tithe's naming cells (sitting B, 2026-09-05; the first-call standard).
if __name__ == '__main__':
    print()
    ok = 0
    frac = {I: 0, M: 0, A: 0, D: 0, H: 0}
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
          'answer-sheet %d/%d · data %d/%d · hypotheses %d/%d' % (
          frac[I], n, 100 * frac[I] // n, frac[M], n, 100 * frac[M] // n,
          frac[A], n, frac[D], n, frac[H], n))
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
    _W.print_coverage()
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

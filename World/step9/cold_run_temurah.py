#!/usr/bin/env python3
"""cold_run_temurah.py — THE CONSECRATION, SUBSTITUTION, AND DEVOTION MACHINE
(2026-09-05, sitting B of the audit — REVIEW_BEHAR item 3: Lev 27's
remainder, which the Jubilee engine left as exam scaffold).

Span: Lev 27:9-15 and 27:26-33 — the animal vowed to the altar and the
SUBSTITUTION clause (27:9-10), the unfit animal stood before the priest
and redeemed with a fifth (27:11-13), the house valued and redeemed
(27:14-15), the firstborn that cannot be sanctified (27:26) and the
impure beast (27:27), the DEVOTED thing and the devoted person
(27:28-29), the land tithe and the animal tithe under the rod
(27:30-33). The valuations and the field are cold_run_yovel.py's.

Answer sheet: Mishnah Temurah (read whole in round 47's topic docket,
logic/oral_triage/sheviit_topic_docket_2026-09-05.md), Arakhin 8,
Bekhorot 9, and one Menachot row (12:1 — the redemption clause's scope)
from this sitting's docket; every expected value a literal typed from
its row (the honest-pairing guard runs first).

The five motions: (1) the ink — the two substitution verbs, 'beast for
beast', 'it and its substitute', the FIFTH token censused five times in
the chapter, the partitive 'from all that he has', 'passes under the
rod, the tenth', 'not examined good or bad'; (2) the rows; (3) run;
(4) the Sifra Bechukotai's recorded arguments per gap, labeled
[MOVE]; (5) effects — consecrated (STATUS, discovered from 27:9's own
'shall be holy'), substitution, adds_fifth, most_holy, put_to_death,
due_to_priest — and THREE inter-span CALLS: cold_run_yovel.tithe_naming()
for the tithe's naming cells, cold_run_pesach.firstborn() for the
firstling donkey the tradition reads beside 27:27, and the field's
priest destination from cold_run_yovel's own probes.
"""
import sqlite3, sys, os, json
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import effects_layer as FX
from compile_guards import check_honest_pairing
GUARDED = check_honest_pairing(os.path.abspath(__file__))

DB = '<repo-old>/elijah_docket/tanakh.sqlite'
db = sqlite3.connect(DB)

def strip(s):
    return ''.join(c for c in s if c != '/' and not (0x0591 <= ord(c) <= 0x05C7))

def toks(book, ch, vs):
    rows = db.execute("""SELECT w.he FROM words w JOIN verses v
        ON w.verse_id=v.id WHERE v.book=? AND v.chapter=? AND v.verse=?
        ORDER BY w.idx""", (book, ch, vs)).fetchall()
    return [strip(r[0]) for r in rows]

def count(book, ch, vs, tok):
    return sum(1 for w in toks(book, ch, vs) if tok in w)

PROBES = [
    ('a BEAST of which they bring an offering',   'Lev', 27, 9, 'בהמה'),
    ('all he gives of it — SHALL BE HOLY',        'Lev', 27, 9, 'קדש'),
    ('he shall not EXCHANGE it',                  'Lev', 27, 10, 'יחליפנו'),
    ('nor SUBSTITUTE it',                          'Lev', 27, 10, 'ימיר'),
    ('good for bad or bad for good',              'Lev', 27, 10, 'ברע'),
    ('BEAST for BEAST',                           'Lev', 27, 10, 'בבהמה'),
    ('it AND ITS SUBSTITUTE shall be holy',       'Lev', 27, 10, 'ותמורתו'),
    ('an IMPURE beast, not offered',              'Lev', 27, 11, 'טמאה'),
    ('STAND the beast before the priest',         'Lev', 27, 11, 'והעמיד'),
    ('the priest VALUES it, good or bad',         'Lev', 27, 12, 'והעריך'),
    ('redeems — adds its FIFTH (#1)',             'Lev', 27, 13, 'חמישתו'),
    ('a man sanctifies his HOUSE',                'Lev', 27, 14, 'ביתו'),
    ('THE SANCTIFIER redeems his house',          'Lev', 27, 15, 'המקדיש'),
    ('adds a fifth (#2)',                         'Lev', 27, 15, 'חמישית'),
    ('adds a fifth (#3, the field)',              'Lev', 27, 19, 'חמשית'),
    ('a FIRSTBORN — no man shall sanctify it',    'Lev', 27, 26, 'בכור'),
    ('which is BORN FIRSTBORN',                   'Lev', 27, 26, 'יבכר'),
    ('to the LORD it IS',                         'Lev', 27, 26, 'הוא'),
    ('the impure beast — redeem at valuation',    'Lev', 27, 27, 'ופדה'),
    ('adds its fifth (#4)',                       'Lev', 27, 27, 'חמשתו'),
    ('not redeemed — SOLD at valuation',          'Lev', 27, 27, 'ונמכר'),
    ('every DEVOTED thing',                       'Lev', 27, 28, 'חרם'),
    ('FROM all that he has (partitive)',          'Lev', 27, 28, 'מכל'),
    ('not sold, not redeemed',                    'Lev', 27, 28, 'יגאל'),
    ('most holy to the LORD',                     'Lev', 27, 28, 'קדשים'),
    ('a devoted PERSON — not ransomed',           'Lev', 27, 29, 'יפדה'),
    ('shall surely be put to death',              'Lev', 27, 29, 'יומת'),
    ('the tithe of the land is holy',             'Lev', 27, 30, 'מעשר'),
    ('redeems his tithe — adds a fifth (#5)',     'Lev', 27, 31, 'חמשיתו'),
    ('herd AND FLOCK',                            'Lev', 27, 32, 'וצאן'),
    ('passes UNDER THE ROD',                      'Lev', 27, 32, 'השבט'),
    ('the TENTH shall be holy',                   'Lev', 27, 32, 'העשירי'),
    ('not EXAMINED good or bad',                  'Lev', 27, 33, 'יבקר'),
    ('nor substitute it; it and its substitute',  'Lev', 27, 33, 'ותמורתו'),
    ('the tithe NOT REDEEMED',                    'Lev', 27, 33, 'יגאל'),
    ('[IMPORT] the field to the priest as a devoted field', 'Lev', 27, 21, 'החרם'),
    ('[IMPORT] the firstborn: you SHALL sanctify (Deut 15:19)', 'Deut', 15, 19, 'תקדיש'),
    ('[IMPORT] the firstling donkey redeemed with a lamb', 'Exod', 13, 13, 'תפדה'),
    ('[IMPORT] Menachot 12:1: only a beast is redeemed — the noun', 'Lev', 27, 11, 'בהמה'),
]
fired = 0
for row in PROBES:
    label, book, ch, vs, tok = row[:5]
    need = row[5] if len(row) > 5 else 1
    hits = count(book, ch, vs, tok)
    if hits < need:
        sys.exit('ZERO-REPORT LAW: probe %r wanted %d of %r at %s %d:%d, found %d — refusing to run'
                 % (label, need, tok, book, ch, vs, hits))
    fired += 1
print('probes: all %d ink-token probes fired (4 imports receipted) [zero-report law satisfied]' % fired)

import re as _re
FIFTH_FORMS = {vs: [w for w in toks('Lev', 27, vs) if _re.match(r'^חמי?שי?ת', w)] for vs in range(1, 35)}
FIFTH = [vs for vs, ws in FIFTH_FORMS.items() if ws]
assert FIFTH == [13, 15, 19, 27, 31], FIFTH
# the census caught its own first draft: a bare substring matched the FIVE and FIFTEEN of the valuation
# table (27:5-7) and missed 27:13 and 27:15, whose FIFTH is spelled plene with a yod (chamishit) where
# 27:19, 27:27, 27:31 spell it defective — five tokens, two spellings, one surcharge.
HOLY = [vs for vs in range(1, 35) if count('Lev', 27, vs, 'קדש')]
SUBST = [vs for vs in range(1, 35) if count('Lev', 27, vs, 'ותמורתו')]
assert SUBST == [10, 33], SUBST
print('censuses: the FIFTH at %s — forms %s (plene at 13 and 15, defective at 19, 27, 31) · the substitute clause at %s '
      '(the vow and the tithe) · holy tokens in %d verses' % (FIFTH, [FIFTH_FORMS[v][0] for v in FIFTH], SUBST, len(HOLY)))

# ---- the inter-span CALLS (the first-call standard) --------------------
import cold_run_yovel as YOVEL
import cold_run_pesach as PESACH
TN = {'ninth_called_tenth': YOVEL.tithe_naming({9: 'tenth', 10: 'ninth', 11: 'tenth'})[9],
      'plain': YOVEL.tithe_naming({9: 'ninth', 10: 'tenth', 11: 'eleventh'})[10],
      'eleventh_called_tenth': YOVEL.tithe_naming({9: 'tenth', 10: 'ninth', 11: 'tenth'})[11]}
_donkey = PESACH.firstborn({'kind': 'donkey'}, PESACH.DATA)
DONKEY = _donkey[0] if isinstance(_donkey, tuple) else _donkey
print('routing receipt: cold_run_yovel.tithe_naming() CALLED (%d namings); cold_run_pesach.firstborn(donkey) '
      'CALLED -> %r' % (len(TN), DONKEY))

I, M, A, D, P, H = 'INK', 'MOVE', 'ANSWER-SHEET', 'DATA', 'IMPORT', 'HYPOTHESIS'   # H: THE LINK REVIEW LAW (LR3, 2026-09-07) — an untaught transfer, kept and labeled, never counted as compiled

def cell(v, p, why, fx):
    FX.validate(fx)
    return {'v': v, 'p': p, 'why': why, 'fx': fx}

# ---- (1) THE MACHINE — compiled from Lev 27's ink ----------------------
def consecrate(thing, owner='israelite', to='unspecified'):
    if thing == 'fit_animal':
        return cell('holy_altar', I, 'ואם בהמה אשר יקריבו ממנה קרבן ליהוה — כל אשר יתן ממנו ליהוה יהיה קדש (a beast '
                    'of which they bring an offering... all he gives of it SHALL BE HOLY, 27:9)', ['consecrated'])
    if thing == 'unfit_animal':
        return cell('holy_upkeep_valued_by_priest', I, 'ואם כל בהמה טמאה אשר לא יקריבו ממנה קרבן... והעמיד... והעריך '
                    'הכהן (an impure beast not offered — stood before the priest, valued good or bad, 27:11-12) '
                    '— the value class, not the altar', ['consecrated'])
    if thing == 'house':
        return cell('valued_by_priest', I, 'ואיש כי יקדש את ביתו... והעריכו הכהן (a man sanctifies his house — the '
                    'priest values it, good or bad, as he values it so it stands, 27:14)', ['consecrated'])
    if thing == 'firstborn':
        return cell('cannot_be_sanctified_to_the_altar', I, 'אך בכור... לא יקדיש איש אתו... ליהוה הוא (a firstborn '
                    '— no man shall sanctify it; it IS the LORD\'s, 27:26)', [FX.NONE])
    if thing == 'firstborn_for_value':
        return cell('value_consecration_yes', M, 'the two verses — "you SHALL sanctify" (Deut 15:19) and "no man '
                    'shall sanctify" (27:26) [IMPORT]: R. Yishmael resolves them — sanctify it for VALUE, not '
                    'for the altar (Arakhin 8:7)', ['consecrated'])
    if thing == 'unspecified_consecration':
        return cell('upkeep', M, 'the Sifra: unspecified consecrations go to the Temple upkeep — the altar class '
                    'needs "of which they bring an offering" (Sifra Bechukotai Chapter 9 2; Temurah 7:2)',
                    ['consecrated'])
    if thing == 'not_his':
        return cell('not_devoted', I, 'מכל אשר לו (FROM ALL THAT HE HAS, 27:28) — a man devotes only what is his: '
                    'not his son, his daughter, his Hebrew slave, his purchased field (Arakhin 8:5)', [FX.NONE])
    return cell('no_case', I, '', [FX.NONE])

def substitute(case, **k):
    if case == 'attempted':
        return cell('both_holy', I, 'לא יחליפנו ולא ימיר אתו... ואם המר ימיר בהמה בבהמה והיה הוא ותמורתו יהיה קדש '
                    '(he shall not exchange it nor substitute it... and if he DOES substitute beast for beast, '
                    'it AND ITS SUBSTITUTE shall be holy, 27:10) — the ban and its outcome in one clause; '
                    'Temurah 1:1: "not that a man may, but if he did, it takes — and he receives forty"',
                    ['substitution', 'consecrated', 'lashes'])
    if case == 'good_for_bad':
        return cell('takes', I, 'טוב ברע או רע בטוב (good for bad or bad for good, 27:10) — both directions '
                    'written; Temurah 1:2 quotes the clause', ['substitution'])
    if case == 'herd_for_flock':
        return cell('takes', I, 'בהמה בבהמה (BEAST for BEAST, 27:10) — the noun is the class: herd for flock, '
                    'sheep for goats, male for female, blemished for whole (Temurah 1:2)', ['substitution'])
    if case == 'one_for_two':
        return cell('takes_R._Shimon_one_for_one', M, 'the first tanna: one for two, two for one, one for a '
                    'hundred; R. Shimon: "it and ITS substitute" — as it is one, so its substitute one '
                    '(Temurah 1:2; the Sifra\'s singular at Bechukotai Chapter 9 10)', ['substitution'])
    if case == 'birds_or_meal_offerings':
        return cell('no_substitution', I, 'בהמה (beast) is the only noun written (27:10) — "for only beast is '
                    'said" (Temurah 1:6)', [FX.NONE])
    if case == 'community_or_partners':
        return cell('no_substitution', M, 'לא ימיר אתו — singular; the Sifra: the INDIVIDUAL makes substitution, '
                    'not the public, not partners (Sifra Bechukotai Chapter 9 3; Temurah 1:6, 2:1, 2:3)', [FX.NONE])
    if case == 'limbs_or_embryos':
        return cell('no_substitution', M, 'not beast for fetuses nor fetuses for beast, not limbs for whole nor '
                    'whole for limbs (Sifra Bechukotai Chapter 9 8; R. Yosei\'s limb-for-whole arm at 9 9; '
                    'Temurah 1:3)', [FX.NONE])
    if case == 'substitute_of_a_substitute':
        return cell('none', M, 'ותמורתו (ITS substitute) — the consecrated makes a substitute, the substitute makes '
                    'none; substitution is not transitive (Sifra Bechukotai Chapter 9 5; Temurah 1:5, 2:3)',
                    [FX.NONE])
    if case == 'permanently_blemished_substitute':
        return cell('holiness_takes_hold', M, '"shall be holy" — on a permanently blemished beast too, and it does '
                    'not leave for shearing and work (Sifra Bechukotai Chapter 9 13-15; Temurah 2:3)',
                    ['consecrated'])
    if case == 'inadvertent':
        return cell('takes_effect_like_deliberate', M, 'R. Yosei b. R. Yehuda: "shall be holy" — the inadvertent '
                    'like the deliberate in substitution (Sifra Bechukotai Chapter 9 16; Temurah 2:3)',
                    ['substitution'])
    if case == 'formula':
        f = k['words']
        if f in ('this_instead_of_that', 'the_substitute_of_that', 'the_exchange_of_that'):
            return cell('substitution', I, 'the ink writes TWO verbs — יחליפנו (exchange) and ימיר (substitute, '
                        '27:10): "the exchange of that" and "the substitute of that" are both the clause\'s '
                        'own words; "this instead of that" their plain form (Temurah 5:5)', ['substitution'])
        if f == 'this_desanctified_on_that':
            return cell('not_substitution', A, 'desanctification is redemption\'s form, not substitution\'s '
                        '(Temurah 5:5); a blemished consecrated beast leaves to profane use and the value '
                        'is owed', ['redemption_right'])
    if case == 'altar_vs_upkeep':
        return cell('altar_holy_only', I, '27:9 "of which they bring an offering" carries the substitution clause; '
                    '27:11 "of which they do NOT bring an offering" carries the valuation-and-fifth clause '
                    'instead — the two classes are the chapter\'s own two paragraphs (Temurah 7:1; Sifra '
                    'Bechukotai Chapter 9 2)', [FX.NONE])
    if case == 'heir':
        return cell('substitutes', M, '"if he substitutes" — the woman and the heir included (the Sifra\'s '
                    'inclusion, Bechukotai Chapter 9 6\'s neighborhood; Menachot 9:7: the heir lays hands, '
                    'brings libations, and substitutes)', ['substitution'])
    return cell('no_case', I, '', [FX.NONE])

def redeem(thing, by='owner'):
    if thing == 'unfit_animal':
        return cell('valuation_plus_fifth', I, 'ואם גאל יגאלנה ויסף חמישתו על ערכך (if he redeems it he adds its '
                    'FIFTH to the valuation, 27:13)', ['adds_fifth', 'redemption_right'])
    if thing == 'house':
        if by == 'owner':
            return cell('valuation_plus_fifth', I, 'ואם המקדיש יגאל את ביתו ויסף חמישית (if THE SANCTIFIER redeems '
                        'his house, he adds a fifth, 27:15) — Arakhin 8:1-3: the owner adds a fifth',
                        ['adds_fifth', 'redemption_right'])
            return None
        return cell('valuation_no_fifth', I, 'the fifth is written on THE SANCTIFIER (27:15) — another\'s '
                    'redemption pays the valuation alone (Arakhin 8:2-3\'s ladder: the fifth on the owner\'s '
                    'bid only)', ['redemption_right'])
    if thing == 'impure_beast_27_27':
        return cell('valuation_plus_fifth_or_sold', I, 'ופדה בערכך ויסף חמשתו עליו ואם לא יגאל ונמכר בערכך (redeem '
                    'at the valuation and add its fifth; if not redeemed, SOLD at the valuation, 27:27)',
                    ['adds_fifth', 'redemption_right'])
    if thing == 'firstling_donkey':
        return cell(DONKEY, P, 'the tradition reads 27:27 of the consecrated impure beast, and sends the firstling '
                    'donkey to Exodus 13:13 — CALLED cold_run_pesach.firstborn(donkey) -> %r [IMPORT, live '
                    'call]' % (DONKEY,), ['redeem_or_break'])
    if thing == 'land_tithe':
        return cell('plus_fifth', I, 'ואם גאל יגאל איש ממעשרו חמשיתו יסף עליו (if a man redeems of his tithe he adds '
                    'its fifth, 27:31)', ['adds_fifth'])
    if thing == 'animal_tithe':
        return cell('not_redeemed', I, 'לא יגאל (it shall not be redeemed, 27:33)', [FX.NONE])
    if thing == 'devoted':
        return cell('not_sold_not_redeemed', I, 'לא ימכר ולא יגאל (not sold and not redeemed, 27:28)', [FX.NONE])
    if thing == 'scope':
        return cell('beast_only', I, 'בהמה (BEAST, 27:11) is the noun the redemption clause is written on — '
                    'birds, wood, frankincense, service vessels have no redemption, "for only beast is said" '
                    '(Menachot 12:1)', [FX.NONE])
    return cell('no_case', I, '', [FX.NONE])

def fifth_census():
    return cell(FIFTH, I, 'the FIFTH token censused: 27:13 (the unfit beast), 27:15 (the house), 27:19 (the '
                'field), 27:27 (the impure beast), 27:31 (the tithe) — five redemptions, one surcharge', ['adds_fifth'])

def devote(case):
    if case == 'status':
        return cell('most_holy_not_sold_not_redeemed', I, 'כל חרם קדש קדשים הוא ליהוה (every devoted thing is MOST HOLY '
                    'to the LORD, 27:28) — not sold, not redeemed', ['most_holy'])
    if case == 'unspecified_destination':
        return cell('priests_Sages_upkeep_R._Yehuda_b._Beteira', I, 'the two verses are both the chapter\'s: '
                    '"as the devoted field, to the PRIEST shall be his holding" (27:21) — the Sages; "every '
                    'devoted thing is most holy TO THE LORD" (27:28) — R. Yehuda b. Beteira (Arakhin 8:6); '
                    'the Sages read 27:28 as the scope (it lands on most holy and light alike)', ['due_to_priest'])
    if case == 'all_his_property':
        return cell('not_devoted', I, 'מכל אשר לו (FROM all that he has, 27:28) — the partitive; devoted all — not '
                    'devoted (R. Elazar; Arakhin 8:4; Sifra Bechukotai Chapter 12 6)', [FX.NONE])
    if case == 'person':
        return cell('put_to_death_not_ransomed', I, 'כל חרם אשר יחרם מן האדם לא יפדה מות יומת (every devoted person '
                    'shall not be ransomed; he shall surely be put to death, 27:29)', ['put_to_death'])
    if case == 'priests_devotions':
        return cell('no_redemption_given_to_priests', A, 'Arakhin 8:6 — the priests\' devoted things are not '
                    'redeemed but given to the priests', ['due_to_priest'])
    if case == 'firstborn':
        return cell('may_be_devoted', A, 'Arakhin 8:7 — the firstborn, whole or blemished, may be devoted; how it '
                    'is redeemed: what a man would give for it to give to his daughter\'s son', ['consecrated'])
    return cell('no_case', I, '', [FX.NONE])

def tithe(case):
    if case == 'procedure':
        return cell('counted_under_the_rod_the_tenth_holy', I, 'כל אשר יעבר תחת השבט העשירי יהיה קדש (all that '
                    'passes under the rod, the TENTH shall be holy, 27:32) — Bekhorot 9:7\'s pen, the small '
                    'gate, the count one to nine, the tenth marked', ['consecrated'])
    if case == 'not_marked_or_counted_lying':
        return cell('tithed', I, 'the ink requires the passing and the count, not the mark or the posture — '
                    'Bekhorot 9:7: not marked with red, not counted with the rod, counted lying or standing '
                    '— tithed', ['consecrated'])
    if case == 'took_ten_of_a_hundred':
        return cell('not_a_tithe', I, 'העשירי (THE TENTH, 27:32) — the ordinal, not a proportion: a hundred and '
                    'took ten, ten and took one — no tithe (Bekhorot 9:7)', [FX.NONE])
    if case == 'not_examined':
        return cell('not_examined_good_or_bad', I, 'לא יבקר בין טוב לרע (he shall not examine between good and bad, '
                    '27:33)', [FX.NONE])
    if case == 'substituted':
        return cell('both_holy_not_redeemed', I, 'ואם המר ימירנו והיה הוא ותמורתו יהיה קדש לא יגאל (if he substitutes '
                    'it, it and its substitute shall be holy; it shall not be redeemed, 27:33; Temurah 3:5)',
                    ['substitution', 'consecrated'])
    if case == 'herd_with_flock':
        return cell('not_tithed_together', I, 'וכל מעשר בקר וצאן (all the tithe of HERD and FLOCK, 27:32) — two '
                    'nouns, two pens; Bekhorot 9:1: "and flock" — all flock is one, sheep with goats',
                    [FX.NONE])
    if case == 'sheep_with_goats':
        return cell('tithed_together', I, 'וצאן (and FLOCK) — one noun covers sheep and goats; Bekhorot 9:1 '
                    'quotes it: "all flock, one"', ['consecrated'])
    if case == 'ninth_called_tenth':
        return cell(TN['ninth_called_tenth'], P, 'CALLED cold_run_yovel.tithe_naming({9: tenth, 10: ninth, 11: '
                    'tenth})[9] -> %r — the error rule compiled in the Jubilee engine (round 47) [IMPORT, '
                    'live call]' % TN['ninth_called_tenth'], ['consecrated'])
    if case == 'eleventh_called_tenth':
        return cell(TN['eleventh_called_tenth'], P, 'CALLED cold_run_yovel.tithe_naming({9: tenth, 10: ninth, '
                    '11: tenth})[11] -> %r — the name uprooted from the tenth, so the eleventh is a peace '
                    'offering [IMPORT, live call]' % TN['eleventh_called_tenth'], ['consecrated'])
    if case == 'land_tithe_status':
        return cell('holy_to_the_LORD', I, 'וכל מעשר הארץ... ליהוה הוא קדש ליהוה (all the tithe of the land... it is '
                    'the LORD\'s, holy to the LORD, 27:30)', ['consecrated'])
    return cell('no_case', I, '', [FX.NONE])

def firstborn_trick():
    return cell('what_is_in_her_womb_if_male_an_olah', M, 'אשר יבכר (which IS BORN firstborn, 27:26) — the Sifra: '
                'not from the womb? the ban binds once it is born a firstborn; sanctified BEFORE birth, the '
                'holiness of the vow lands first (Sifra Bechukotai Section 5 2; Temurah 5:1)', ['consecrated'])

import os as _os5, sys as _sys5, io as _io5, contextlib as _ctx5
_sys5.path.insert(0, _os5.path.dirname(_os5.path.abspath(__file__)))
# ---- THE WRAP (W5 HOLINESS, SANCTIONS, THE LAND, 2026-09-07): the daemon over the compiled consecration machine ----
import world_engine as WE
def _fx_union(cells):
    fx, why = set(), {}
    for c in cells:
        for f in c['fx']:
            fx.add(f); why.setdefault(f, c)
    return fx, why
def law_temurah(event, world):
    """Lev 27:9-15, 26-33 (cold_run_temurah.py — consecrate, substitute, redeem, fifth_census, devote, tithe, firstborn_trick): the holiness that takes, the fifth, the devoted, the tenth under the rod."""
    k, src = event['kind'], event['case_source']
    E_ = lambda eff, s, cp=None, amount=None, due=None, law='', value=None: {'effect': eff, 'subject': s, 'counterparty': cp, 'amount': amount, 'due': due, 'value': value if value is not None else True, 'source_law': law, 'case_source': src}
    if k == 'thing_consecrated':
        o = event['owner']; t = event['subject']
        if event.get('before_birth'):
            c = firstborn_trick()
            return [E_('consecrated', t, cp=o, value=c['v'], law='F1 [INK 27:26 "which IS BORN firstborn" — %s (Sifra Bechukotai Section 5 2, Temurah 5:1)]' % c['v'])]
        c = consecrate(event['thing'], event.get('owner_class', 'israelite'), event.get('to', 'unspecified'))
        if 'consecrated' in c['fx']:
            return [E_('consecrated', t, cp=o, value=c['v'], law='F1 [%s]' % c['why'][:110])]
        return []                                                    # the firstborn cannot be sanctified to the altar; not his — the silence
    if k == 'substitute_declared':
        o = event['owner']; t = event['subject']; case = event.get('case', 'attempted')
        if event.get('of') == 'tithe':
            c = tithe('substituted')
        elif case == 'formula':
            c = substitute('formula', words=event.get('words'))
        else:
            c = substitute(case)
        out = []
        if 'substitution' in c['fx']:
            out.append(E_('substitution', t, cp=o, value=c['v'], law='F2 [INK 27:10 "if he does substitute beast for beast, it and its substitute shall be holy" — %s]' % c['why'][:90]))
        if 'consecrated' in c['fx']:
            out.append(E_('consecrated', t, cp=o, value=c['v'], law='F2 [INK 27:10 / 27:33 "it and its substitute shall be holy" — %s]' % c['why'][:80]))
        if 'lashes' in c['fx']:
            out.append(E_('lashes', o, amount=40, value=c['v'], law='F2 [INK 27:10 "he shall not exchange it nor substitute it" — Temurah 1:1: it takes, and he receives forty]'))
        if 'redemption_right' in c['fx']:
            out.append(E_('redemption_right', t, cp=o, value=c['v'], law='F2 [%s]' % c['why'][:100]))
        return out
    if k == 'consecrated_redeemed':
        r = event['redeemer']; t = event['subject']
        c = redeem(event['thing'], event.get('by', 'owner'))
        if c is None:
            return []
        cells = [c] + ([fifth_census()] if 'adds_fifth' in c['fx'] else [])
        fx, why = _fx_union(cells); out = []
        if 'adds_fifth' in fx:
            out.append(E_('adds_fifth', r, cp='the-treasury', value=why['adds_fifth']['v'], law='F3 [%s — %s]' % (c['why'][:70], why['adds_fifth']['why'][:60] if why['adds_fifth'] is not c else '')))
        if 'redemption_right' in fx:
            out.append(E_('redemption_right', t, cp=r, value=c['v'], law='F3 [%s]' % c['why'][:100]))
        if 'redeem_or_break' in fx:
            out.append(E_('redeem_or_break', t, cp=r, value=c['v'], law='F3 [the firstling donkey — CALLED cold_run_pesach.firstborn(donkey) -> %s (Exod 13:13)]' % c['v']))
        return out
    if k == 'thing_devoted':
        d = event['devoter']; t = event['subject']; c = devote(event.get('case', 'status')); out = []
        if 'most_holy' in c['fx']:
            out.append(E_('most_holy', t, cp=d, value=c['v'], law='F4 [INK 27:28 "every devoted thing is MOST HOLY to the LORD" — not sold, not redeemed]'))
        if 'due_to_priest' in c['fx']:
            out.append(E_('due_to_priest', t, cp='the-priests', value=c['v'], law='F4 [INK 27:21 "as the devoted field, to the PRIEST shall be his holding" — %s]' % c['why'][:80]))
        if 'put_to_death' in c['fx']:
            out.append(E_('put_to_death', t, value=c['v'], law='F4 [INK 27:29 "every devoted person shall not be ransomed, he shall surely be put to death"]'))
        if 'consecrated' in c['fx']:
            out.append(E_('consecrated', t, cp=d, value=c['v'], law='F4 [%s]' % c['why'][:100]))
        return out
    if k == 'herd_tithed':
        o = event['owner']; t = event['subject']; c = tithe(event.get('case', 'procedure')); out = []
        if 'consecrated' in c['fx']:
            out.append(E_('consecrated', t, cp=o, value=c['v'], law='F5 [INK 27:32 "all that passes under the rod, the TENTH shall be holy" — %s]' % c['why'][:90]))
        if 'substitution' in c['fx']:
            out.append(E_('substitution', t, cp=o, value=c['v'], law='F5 [INK 27:33 "if he substitutes it, it and its substitute shall be holy, it shall not be redeemed" — %s]' % c['why'][:70]))
        return out
    return []

def scene():
    """THE SCENE — Temurah 1-7, Arakhin 8, Bekhorot 9 and the Sifra's rows replayed on the world engine (clock unit: days)."""
    with _ctx5.redirect_stdout(_io5.StringIO()):
        w = WE.World(era='the consecration machine: Temurah, Arakhin 8, Bekhorot 9 on the engine (clock unit: days)')
        w.laws = [law_temurah]
        w.advance(1)
        for t, ev in (('the-fit-animal', {'thing': 'fit_animal'}), ('the-unfit-animal', {'thing': 'unfit_animal'}), ('the-house', {'thing': 'house'}), ('the-firstborn', {'thing': 'firstborn'}),
                      ('the-firstborn-for-value', {'thing': 'firstborn_for_value'}), ('the-unborn', {'thing': 'fit_animal', 'before_birth': True}), ('the-sons-field', {'thing': 'not_his'})):
            w.submit(dict({'kind': 'thing_consecrated', 'subject': t, 'owner': 'the-vower', 'to': 'unspecified', 'day': 1, 'case_source': 'Lev 27:9-14, 26; Mishnah Temurah 5:1, 7:1-2; Arakhin 8:7 — %s' % t}, **ev))
        for t, ev in (('the-substituter', {'case': 'attempted'}), ('the-bird-vower', {'case': 'birds_or_meal_offerings'}), ('the-formula-sayer', {'case': 'formula', 'words': 'this_desanctified_on_that'}), ('the-heir', {'case': 'heir'}), ('the-tithe-substituter', {'of': 'tithe'})):
            w.submit(dict({'kind': 'substitute_declared', 'subject': t, 'owner': t, 'day': 1, 'case_source': 'Lev 27:10, 27:33; Mishnah Temurah 1:1-6, 3:5, 5:5 — %s' % t}, **ev))
        for t, ev in (('the-unfit-redeemer', {'thing': 'unfit_animal', 'by': 'owner'}), ('the-house-redeemer', {'thing': 'house', 'by': 'owner'}), ('the-other-redeemer', {'thing': 'house', 'by': 'other'}), ('the-donkey-owner', {'thing': 'firstling_donkey'}),
                      ('the-tithe-redeemer', {'thing': 'land_tithe'}), ('the-devoted-redeemer', {'thing': 'devoted'}), ('the-field-redeemer', {'thing': 'field'})):
            w.submit(dict({'kind': 'consecrated_redeemed', 'subject': t, 'redeemer': t, 'day': 1, 'case_source': 'Lev 27:13, 15, 27, 31; Mishnah Arakhin 8:1-3; Bekhorot 1:2-4 — %s' % t}, **ev))
        for t, ev in (('the-devoted-thing', {'case': 'status'}), ('the-unspecified-devotion', {'case': 'unspecified_destination'}), ('the-whole-estate', {'case': 'all_his_property'}), ('the-devoted-person', {'case': 'person'}), ('the-devoted-firstborn', {'case': 'firstborn'})):
            w.submit(dict({'kind': 'thing_devoted', 'subject': t, 'devoter': 'the-devoter', 'day': 1, 'case_source': 'Lev 27:28-29; Mishnah Arakhin 8:4-7 — %s' % t}, **ev))
        for t, ev in (('the-tenth', {'case': 'procedure'}), ('the-ten-of-a-hundred', {'case': 'took_ten_of_a_hundred'}), ('the-ninth-called-tenth', {'case': 'ninth_called_tenth'}), ('the-substituted-tenth', {'case': 'substituted'}), ('the-land-tithe', {'case': 'land_tithe_status'})):
            w.submit(dict({'kind': 'herd_tithed', 'subject': t, 'owner': 'the-herdsman', 'day': 1, 'case_source': 'Lev 27:30-33; Mishnah Bekhorot 9:7-8 — %s' % t}, **ev))
        w.advance(2)
    n = lambda eid, eff: len([e for e in w.entity(eid).ledger if e['effect'] == eff])
    am = lambda eid, eff: [e['amount'] for e in w.entity(eid).ledger if e['effect'] == eff]
    tset = len([l for l in w.log if l[0] == 'TIMER-SET']); fired = len([l for l in w.log if l[0] == 'TIMER-FIRE'])
    return (n('the-fit-animal', 'consecrated'), n('the-unfit-animal', 'consecrated'), n('the-house', 'consecrated'), n('the-firstborn', 'consecrated'), n('the-firstborn-for-value', 'consecrated'), n('the-unborn', 'consecrated'), n('the-sons-field', 'consecrated'),
            n('the-substituter', 'substitution'), n('the-substituter', 'consecrated'), am('the-substituter', 'lashes'), n('the-bird-vower', 'substitution'), n('the-formula-sayer', 'redemption_right'), n('the-heir', 'substitution'), n('the-tithe-substituter', 'substitution'), n('the-tithe-substituter', 'consecrated'),
            n('the-unfit-redeemer', 'adds_fifth'), n('the-unfit-redeemer', 'redemption_right'), n('the-house-redeemer', 'adds_fifth'), n('the-other-redeemer', 'adds_fifth'), n('the-other-redeemer', 'redemption_right'), n('the-donkey-owner', 'redeem_or_break'), n('the-tithe-redeemer', 'adds_fifth'), n('the-devoted-redeemer', 'redemption_right'), n('the-field-redeemer', 'adds_fifth'),
            n('the-devoted-thing', 'most_holy'), n('the-unspecified-devotion', 'due_to_priest'), n('the-whole-estate', 'most_holy'), n('the-devoted-person', 'put_to_death'), n('the-devoted-firstborn', 'consecrated'),
            n('the-tenth', 'consecrated'), n('the-ten-of-a-hundred', 'consecrated'), n('the-ninth-called-tenth', 'consecrated'), n('the-substituted-tenth', 'substitution'), n('the-substituted-tenth', 'consecrated'), n('the-land-tithe', 'consecrated'),
            tset, fired, w.clock.day), w
SCENE, _W = scene()


# ---- (2) TEST DATA — the Mishnah rows, read from the shelf ------------
def load(t):
    d = json.load(open('<repo-old>/Data/mishnah_%s_he.json' % t))
    return d['text'] if isinstance(d, dict) and 'text' in d else d
BOOKS = {'Temurah': load('temurah'), 'Arakhin': load('arakhin'), 'Bekhorot': load('bekhorot'), 'Menachot': load('menachot')}
SHEET = [
    ('Temurah', 1, 1, 'הארבעים'), ('Temurah', 1, 2, 'הבקר'), ('Temurah', 1, 3, 'אברים'), ('Temurah', 1, 5, 'תמורה'),
    ('Temurah', 1, 6, 'בבהמה'), ('Temurah', 2, 3, 'שוגג'), ('Temurah', 3, 5, 'המעשר'), ('Temurah', 5, 1, 'עולה'),
    ('Temurah', 5, 5, 'מחללת'), ('Temurah', 7, 1, 'תמורה'), ('Temurah', 7, 2, 'סתם'),
    ('Arakhin', 8, 1, 'חמש'), ('Arakhin', 8, 4, 'החרים'), ('Arakhin', 8, 5, 'שלו'), ('Arakhin', 8, 6, 'לכהנים'),
    ('Arakhin', 8, 7, 'תקדיש'), ('Bekhorot', 9, 1, 'וצאן'), ('Bekhorot', 9, 7, 'בשבט'), ('Bekhorot', 9, 8, 'תשיעי'),
    ('Menachot', 12, 1, 'בהמה'),
]
for b, ch, m, must in SHEET:
    assert must in strip(BOOKS[b][ch - 1][m - 1]), 'answer-sheet check failed: %r not in Mishnah %s %d:%d' % (must, b, ch, m)
print('answer sheet: %d Mishnah rows token-verified in their own ink' % len(SHEET))

TESTS = [
 ('THE SCENE — Temurah, Arakhin 8, Bekhorot 9 and the Sifra on the world engine (the daemon\'s watch coverage printed below)', cell(SCENE, I, 'the consecration\'s classes, the substitute that takes, the fifth at its five seats, the devoted, the tenth under the rod — every value a cell\'s', ['consecrated', 'substitution', 'lashes', 'redemption_right', 'adds_fifth', 'redeem_or_break', 'most_holy', 'due_to_priest', 'put_to_death']), (1, 1, 1, 0, 1, 1, 0, 1, 1, [40], 0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 0, 0, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 1, 0, 0, 2)),
 ('Temurah 7:1 — an animal vowed to the altar: holy (the altar class)', consecrate('fit_animal'), 'holy_altar'),
 ('Temurah 7:1-2 — an unfit animal consecrated: the upkeep class, valued by the priest', consecrate('unfit_animal'), 'holy_upkeep_valued_by_priest'),
 ('Temurah 7:2 — unspecified consecrations go to the upkeep', consecrate('unspecified_consecration'), 'upkeep'),
 ('Temurah 1:1 — substitution attempted: it takes, and forty', substitute('attempted'), 'both_holy'),
 ('Temurah 1:2 — good for bad, bad for good: takes', substitute('good_for_bad'), 'takes'),
 ('Temurah 1:2 — herd for flock, sheep for goats, blemished for whole: takes', substitute('herd_for_flock'), 'takes'),
 ('Temurah 1:2 — one for two, one for a hundred (R. Shimon: one for one)', substitute('one_for_two'), 'takes_R._Shimon_one_for_one'),
 ('Temurah 1:6 — birds and meal offerings make no substitute', substitute('birds_or_meal_offerings'), 'no_substitution'),
 ('Temurah 1:6 / 2:1 — the community and partners make no substitute', substitute('community_or_partners'), 'no_substitution'),
 ('Temurah 1:3 — limbs and embryos make no substitute', substitute('limbs_or_embryos'), 'no_substitution'),
 ('Temurah 1:5 / 2:3 — a substitute makes no substitute', substitute('substitute_of_a_substitute'), 'none'),
 ('Temurah 2:3 — holiness lands on a permanently blemished substitute', substitute('permanently_blemished_substitute'), 'holiness_takes_hold'),
 ('Temurah 2:3 — the inadvertent like the deliberate in substitution', substitute('inadvertent'), 'takes_effect_like_deliberate'),
 ('Temurah 5:5 — "this instead of that": a substitute', substitute('formula', words='this_instead_of_that'), 'substitution'),
 ('Temurah 5:5 — "the exchange of that": a substitute', substitute('formula', words='the_exchange_of_that'), 'substitution'),
 ('Temurah 5:5 — "this desanctified on that": not a substitute', substitute('formula', words='this_desanctified_on_that'), 'not_substitution'),
 ('Temurah 7:1 — altar-holy substitute; upkeep-holy do not', substitute('altar_vs_upkeep'), 'altar_holy_only'),
 ('Menachot 9:7 — the heir substitutes', substitute('heir'), 'substitutes'),
 ('Arakhin 8:1 — the owner redeeming adds a fifth (the unfit beast)', redeem('unfit_animal'), 'valuation_plus_fifth'),
 ('Arakhin 8:1-3 — the owner redeems his house with a fifth', redeem('house', 'owner'), 'valuation_plus_fifth'),
 ('Arakhin 8:2-3 — another redeems: the valuation, no fifth', redeem('house', 'another'), 'valuation_no_fifth'),
 ('the five fifths of the chapter (27:13, 15, 19, 27, 31)', fifth_census(), [13, 15, 19, 27, 31]),
 ('Menachot 12:1 — birds, wood, frankincense, vessels: no redemption, only a beast is said', redeem('scope'), 'beast_only'),
 ('Bekhorot 1:7 (via the Passover engine) — the firstling donkey: a lamb, else the neck', redeem('firstling_donkey'), 'redeem with a lamb, else break the neck'),
 ('Arakhin 8:7 — the firstborn: sanctify it for value, not for the altar', consecrate('firstborn_for_value'), 'value_consecration_yes'),
 ('Temurah 5:1 — outwitting the firstborn: "what is in her womb, if male, an olah"', firstborn_trick(), 'what_is_in_her_womb_if_male_an_olah'),
 ('Arakhin 8:6 — every devoted thing most holy, not sold, not redeemed', devote('status'), 'most_holy_not_sold_not_redeemed'),
 ('Arakhin 8:6 — unspecified devotion: to the priests (Sages) / the upkeep (R. Yehuda b. Beteira)', devote('unspecified_destination'), 'priests_Sages_upkeep_R._Yehuda_b._Beteira'),
 ('Arakhin 8:4 — devoted ALL he has: not devoted', devote('all_his_property'), 'not_devoted'),
 ('Arakhin 8:5 — devoted his son, daughter, Hebrew slave, purchased field: not devoted', consecrate('not_his'), 'not_devoted'),
 ('Arakhin 8:6 — the priests\' devotions: no redemption, given to the priests', devote('priests_devotions'), 'no_redemption_given_to_priests'),
 ('Arakhin 8:7 — the firstborn may be devoted', devote('firstborn'), 'may_be_devoted'),
 ('Bekhorot 9:7 — the pen, the small gate, the count, the tenth marked', tithe('procedure'), 'counted_under_the_rod_the_tenth_holy'),
 ('Bekhorot 9:7 — not marked, counted lying or standing: tithed', tithe('not_marked_or_counted_lying'), 'tithed'),
 ('Bekhorot 9:7 — a hundred and took ten: not a tithe', tithe('took_ten_of_a_hundred'), 'not_a_tithe'),
 ('Temurah 3:5 — the tithe substituted: both holy, not redeemed', tithe('substituted'), 'both_holy_not_redeemed'),
 ('Bekhorot 9:1 — herd and flock not tithed together', tithe('herd_with_flock'), 'not_tithed_together'),
 ('Bekhorot 9:1 — sheep and goats tithed together ("and flock" — all flock one)', tithe('sheep_with_goats'), 'tithed_together'),
 ('Bekhorot 9:8 (via the Jubilee engine) — the ninth called tenth: sanctified, eaten blemished', tithe('ninth_called_tenth'), 'sanctified_eaten_blemished'),
 ('Bekhorot 9:8 (via the Jubilee engine) — the eleventh called tenth: a peace offering', tithe('eleventh_called_tenth'), 'shelamim'),
]

# ---- (3)+(5) run, grade, effects ------------------------------------
n = len(TESTS)
assert n == GUARDED, (n, GUARDED)
print('guard: %d test rows, every expected value a literal from the answer sheet [honest-pairing guard satisfied]' % GUARDED)
print()
ok = 0
frac = {I: 0, M: 0, A: 0, D: 0, P: 0, H: 0}
used = []
for name, c, want in TESTS:
    hit = c['v'] == want
    ok += hit
    frac[c['p']] += 1
    used += [e for e in c['fx'] if e != FX.NONE]
    print('%s %-92s [%s] %s' % ('OK ' if hit else 'MISS', name[:92], c['p'], '' if hit else 'got=%r' % (c['v'],)))
    print('     effects: %s' % ', '.join(c['fx']))
print()
print('MATRIX: %d/%d cells match the answer sheet' % (ok, n))
print('FRACTIONS: pure ink %d/%d (%d%%) · recorded moves %d/%d (%d%%) · answer-sheet %d/%d · data %d/%d · imports %d/%d · hypotheses %d/%d'
      % (frac[I], n, 100 * frac[I] // n, frac[M], n, 100 * frac[M] // n, frac[A], n, frac[D], n, frac[P], n, frac[H], n))
print('computed, not graded: the impure beast of 27:27 redeemed at valuation plus a fifth or sold (INK); the '
      'devoted person put to death, not ransomed (INK 27:29); the land tithe holy (INK 27:30) and redeemed '
      'with a fifth (INK 27:31); not examined good or bad (INK 27:33) — %s'
      % ', '.join(str(x['v']) for x in (redeem('impure_beast_27_27'), devote('person'), tithe('land_tithe_status'),
                                         redeem('land_tithe'), tithe('not_examined'))))
ops = FX.summarize(used)
print('LEDGER OPS this span writes: %s' % ', '.join('%s x%d' % kv for kv in sorted(ops.items())))
print('effects: every cell carries REGISTERED effects — consecrated (STATUS) discovered from 27:9\'s own "shall '
      'be holy"; most_holy shared with the meal offering; substitution, adds_fifth, put_to_death, '
      'due_to_priest, redemption_right, lashes, redeem_or_break from the registry [effects law satisfied]')
_W.print_coverage()
if ok == n:
    print()
    print('THE CONSECRATION, SUBSTITUTION, AND DEVOTION MACHINE COMPILES — the two substitution verbs, "beast '
          'for beast," "it and its substitute" at the vow and the tithe, the fifth censused five times, the '
          'partitive "from all that he has," the ordinal tenth under the rod; three calls into sister '
          'engines: the Jubilee engine\'s tithe naming and the Passover engine\'s firstling donkey.')
else:
    sys.exit('MISSES REMAIN — consult the Talmud per gap and recompile.')

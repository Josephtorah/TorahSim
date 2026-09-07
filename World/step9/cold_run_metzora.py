#!/usr/bin/env python3
"""cold_run_metzora.py — THE LEPER'S CLEANSING (Lev 14:1-32)
(2026-09-06, the dependency-debt sitting — the owner: "can we fix all of the
overlooked sections, then make sure we code properly going forward").

The dependency audit (World/step9/REPORT_DEPENDENCIES.md) found this sub-span
UNCOMPILED behind the Lev 13-14 check mark: the affliction runner holds the
six-track state machine and the ten houses, and cites 14:37-45 alone. Here
the cleansing itself is compiled from the ink: the day and the priest, the
kit of four (two live pure birds, cedar, scarlet, hyssop), the slaughter
over living water in an earthen vessel, the dip and the seven sprinklings,
the sending over the open field, the first shave and the week outside his
tent, the seventh day's second shave and the three purities, the eighth day
— two lambs and a ewe with three tenths and a log, the guilt offering waved
alive with its log, its blood and then the oil on the right ear-ridge,
thumb, and toe, the remainder on the head, the sin offering, the burnt
offering, the meal offering — and the poor man's scale with its sampling
point. The offering PROCEDURES are fetched by LIVE CALL: the offerings
dispatcher (the north, the communal row's eater), the Tzav engine's guilt
offering law (compiled the same sitting), the sin-offering engine (the
commoner's animal), the meal-offering engine (the bird burnt offering's
place), the Lev 5 engine (the bird pair's order).

Answer sheet ROUTED BY TOPIC under the union rule: Mishnah Negaim 14 whole,
the link rows (Keritot 2, Menachot 3:6, 5:6-7, 9:3, Zevachim 5:5, 10:5, Nazir
6-8, Sotah 1:5, Arakhin 4:2, Moed Katan 3:1, Megillah 1:7, 2:5, Avodah Zarah
5:9) — the ledger logic/oral_triage/dependency_debt_docket_2026-09-06.md,
coverage computed, written before any cell; the Sifra Metzora rows (the
unit's own spine, read 2026-09-05) are the labeled moves.

The five motions: (1) the ink — every number, member, and verb probed and
censused; the quantities the ink leaves open (the quarter-log, the cedar's
size, Nicanor's gate, the tenth's measure) are DATA; (2) the rows as literal
test data (the honest-pairing guard first); (3) run; (4) misses per gap;
(5) fractions and EFFECTS on every cell — eight registered from this
chapter's own verbs at this sitting.
"""
import sqlite3, sys, os, io, contextlib
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import effects_layer as FX
from compile_guards import check_honest_pairing
GUARDED = check_honest_pairing(os.path.abspath(__file__))
assert GUARDED == 78, ('the guard counted %d expectations, the tripwire holds 78' % GUARDED)   # W4: +1, the scene row

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

def phrase(book, ch, vs, words):
    t = toks(book, ch, vs); n = len(words)
    return sum(1 for i in range(len(t) - n + 1) if t[i:i + n] == words)

# ---- (1) ink probes — each MUST fire or the run refuses -------------
PROBES = [
    ('this is the LAW of the leper',               'Lev', 14, 2, 'תורת'),
    ('on the DAY of his cleansing',                'Lev', 14, 2, 'ביום'),
    ('brought to the PRIEST',                      'Lev', 14, 2, 'הכהן'),
    ('the priest goes OUT of the camp',            'Lev', 14, 3, 'ויצא'),
    ('HEALED',                                     'Lev', 14, 3, 'נרפא'),
    ('two LIVE birds',                             'Lev', 14, 4, 'חיות'),
    ('PURE birds',                                 'Lev', 14, 4, 'טהרות'),
    ('cedar wood',                                 'Lev', 14, 4, 'ארז'),
    ('scarlet',                                    'Lev', 14, 4, 'תולעת'),
    ('hyssop',                                     'Lev', 14, 4, 'ואזב'),
    ('an EARTHEN vessel',                          'Lev', 14, 5, 'חרש'),
    ('LIVING water',                               'Lev', 14, 5, 'חיים'),
    ('DIP them',                                   'Lev', 14, 6, 'וטבל'),
    ('SEVEN times',                                'Lev', 14, 7, 'שבע'),
    ('and he shall PURIFY him',                    'Lev', 14, 7, 'וטהרו'),
    ('SEND the living bird',                       'Lev', 14, 7, 'ושלח'),
    ('over the face of the FIELD',                 'Lev', 14, 7, 'השדה'),
    ('SHAVE all his hair',                         'Lev', 14, 8, 'וגלח'),
    ('outside his TENT',                           'Lev', 14, 8, 'לאהלו'),
    ('the SEVENTH day',                            'Lev', 14, 9, 'השביעי'),
    ('his EYEBROWS',                               'Lev', 14, 9, 'גבת'),
    ('the EIGHTH day',                             'Lev', 14, 10, 'השמיני'),
    ('two LAMBS',                                  'Lev', 14, 10, 'כבשים'),
    ('one EWE of its first year',                  'Lev', 14, 10, 'וכבשה'),
    ('three TENTHS',                               'Lev', 14, 10, 'עשרנים'),
    ('one LOG of oil',                             'Lev', 14, 10, 'לג'),
    ('the guilt offering WAVED',                   'Lev', 14, 12, 'והניף'),
    ('as the sin offering so the guilt offering',  'Lev', 14, 13, 'כחטאת'),
    ('the RIGHT ear',                              'Lev', 14, 14, 'הימנית'),
    ('the ear\'s RIDGE',                           'Lev', 14, 14, 'תנוך'),
    ('the priest\'s LEFT palm',                    'Lev', 14, 15, 'השמאלית'),
    ('on the BLOOD of the guilt offering',         'Lev', 14, 17, 'דם'),
    ('the REMAINDER on the head',                  'Lev', 14, 18, 'והנותר'),
    ('and AFTERWARD the burnt offering',           'Lev', 14, 19, 'ואחר'),
    ('if he is POOR',                              'Lev', 14, 21, 'דל'),
    ('his hand does not REACH',                    'Lev', 14, 21, 'משגת'),
    ('two turtledoves',                            'Lev', 14, 22, 'תרים'),
    ('on the PLACE of the blood',                  'Lev', 14, 28, 'מקום'),
    ('the closing torah',                          'Lev', 14, 32, 'תורת'),
]
fired = 0
for name, b, ch, vs, tok in PROBES:
    if count(b, ch, vs, tok) == 0:
        sys.exit('PROBE FAILED: %s — %r not in %s %d:%d' % (name, tok, b, ch, vs))
    fired += 1
print('probes: all %d ink-token probes fired [zero-report law satisfied]' % fired)

# ---- the censuses (asserted: tripwires, not recitals) ----------------
V = list(range(1, 33))
c_pure = [v for v in V if count('Lev', 14, v, 'וטהר')]                      # the purity verb's seats
c_seven = [v for v in V if any(w == 'שבע' for w in toks('Lev', 14, v))]    # the seven-count (exact: 14:8's "seven DAYS" is the tent week, not a sprinkling)
c_right = {v: count('Lev', 14, v, 'הימנית') for v in V if count('Lev', 14, v, 'הימנית')}
c_log = [v for v in V if any(w in ('לג', 'ולג', 'מלג') for w in toks('Lev', 14, v))]   # 14:15 "FROM the log" carries the prefix
c_asham = [v for v in V if count('Lev', 14, v, 'אשם')]
c_reach = [v for v in V if count('Lev', 14, v, 'תשיג')]
c_on_blood = (phrase('Lev', 14, 17, ['על', 'דם', 'האשם']), phrase('Lev', 14, 28, ['על', 'מקום', 'דם', 'האשם']))
c_all_hair = count('Lev', 14, 9, 'שערו')
c_kit = [count('Lev', 14, 4, t) for t in ('צפרים', 'ארז', 'תולעת', 'ואזב')]
c_wave = [v for v in V if count('Lev', 14, v, 'תנופה')]
c_tent = count('Lev', 14, 8, 'לאהלו')
c_lambs = (count('Lev', 14, 10, 'כבשים'), count('Lev', 14, 10, 'וכבשה'), count('Lev', 14, 21, 'כבש'))
assert c_pure == [7, 8, 9, 20], c_pure
assert c_seven == [7, 16, 27], c_seven
assert c_right == {14: 3, 16: 1, 17: 3, 25: 3, 27: 1, 28: 3}, c_right   # x3 = the three members; x1 = the priest's RIGHT finger (16, 27)
assert c_log == [10, 12, 15, 21, 24], c_log
assert c_asham == [12, 13, 14, 17, 21, 24, 25, 28], c_asham
assert c_reach == [22, 30, 31, 32], c_reach
assert c_on_blood == (1, 1) and c_all_hair == 2 and c_kit == [1, 1, 1, 1] and c_wave == [12, 21, 24] and c_tent == 1, \
    (c_on_blood, c_all_hair, c_kit, c_wave, c_tent)
assert c_lambs == (1, 1, 1), c_lambs
print('censuses: the purity verb at 14:%s (four gates) · seven at 14:%s · "the right" x3 at 14:%s · the log at 14:%s · '
      'the guilt offering at 14:%s · "his hand reaches" at 14:%s · "on the blood" (17) vs "on the PLACE of the blood" (28) '
      '%s · "all his hair" x%d at 14:9 · the kit of four at 14:4 %s · the waving at 14:%s · the tent once · lambs %s'
      % (c_pure, c_seven, sorted(c_right), c_log, c_asham, c_reach, c_on_blood, c_all_hair, c_kit, c_wave, c_lambs))

# ---- the callees (cold) --------------------------------------------
_buf = io.StringIO()
with contextlib.redirect_stdout(_buf):
    import cold_run_offerings as OFF
    import cold_run_minchah as MIN
    import cold_run_tzav as TZ
    import cold_run_chatat as CH
    import cold_run_vayikra5 as V5
CSA = OFF.dispatch('communal_shelamim_and_asham')
CHATAT_ROW = OFF.dispatch('outer_chatat')
OLAH_ROW = OFF.dispatch('olah:flock')
BIRD_PLACE = MIN.bird('place')['v']
ASHAM_GRADE = TZ.asham_law({'ask': 'grade'}, TZ.PARAMS)[0]
ASHAM_LEPER = TZ.asham_law({'ask': 'leper_blood'}, TZ.PARAMS)[0]
ASHAM_PREC = TZ.asham_law({'ask': 'precedence'}, TZ.PARAMS)[0]
ASHAM_AGE = TZ.asham_law({'ask': 'age_and_price'}, TZ.PARAMS)[0]
COMMONER = CH.rank('commoner')['v']
_r = V5.graded_offering({'trigger': 'utterance_oath', 'act_is_his_option': True, 'oath_forgotten': True,
                         'means': 'reaches_birds'}, V5.DATA)
BIRD_ORDER = _r[0] if isinstance(_r, tuple) else _r
print('routing receipts: cold_run_offerings CALLED — asham/communal row place %r eater %r; outer chatat place %r; olah %r; '
      'cold_run_minchah CALLED — bird place %r; cold_run_tzav CALLED — asham_law grade %r, leper_blood %r, precedence %r; '
      'cold_run_chatat CALLED — rank(commoner) %r; cold_run_vayikra5 CALLED — birds tier %r [IMPORT, live calls]'
      % (CSA['place']['v'], CSA['eater']['v'], CHATAT_ROW['place']['v'], OLAH_ROW['disposition']['v'], BIRD_PLACE,
         ASHAM_GRADE, ASHAM_LEPER, ASHAM_PREC, COMMONER, BIRD_ORDER))

I, M, A, D, P = 'INK', 'MOVE', 'ANSWER-SHEET', 'DATA', 'IMPORT'
def cell(v, p, why, fx):
    FX.validate(fx)
    return {'v': v, 'p': p, 'why': why, 'fx': fx}
SM = 'Sifra, Metzora, '

# =====================================================================
# THE CODE — from the ink of Leviticus 14:1-32 alone. Mishnah/Talmud
# appear ONLY on [MOVE]/[ANSWER-SHEET] lines and as DATA.
# =====================================================================

# ---- F1: THE DAY AND THE PRIEST (14:2-3) -----------------------------
def frame(q):
    if q == 'one_law':
        return cell('one_law_for_all_lepers', I, '14:2 "this shall be the LAW of the leper" — one law; ' + SM +
                    'Section 1 1 (one offering for all marks; Mishnah Keritot 2:3: afflicted many times, one offering)',
                    ['declared_pure'])
    if q == 'day':
        return cell('by_day_no_delay', M, '14:2 "on the DAY of his cleansing" [INK] — ' + SM + 'Section 1 2: the acts '
                    'BY DAY (Mishnah Megillah 2:5: the leper\'s purification all the day) and no delay', ['declared_pure'])
    if q == 'who':
        return cell('priest_goes_outside_the_camp', I, '14:3 "the PRIEST shall go OUT of the camp" — the leper is not '
                    'brought in; the priest goes to him (' + SM + 'Section 1 4: any priest who could enter)', [FX.NONE])
    if q == 'healed':
        return cell('mark_gone_even_partly', M, '14:3 "behold, the mark of leprosy is HEALED" [INK] — ' + SM +
                    'Section 1 5: healed = the mark, the white hair, the raw flesh gone — even partly', ['declared_pure'])
    if q == 'which_leper':
        return cell('decided_not_quarantined', A, 'Mishnah Megillah 1:7 — between the one pure from quarantine and the '
                    'one pure from decision only the shaving and the birds: this rite runs for the DECIDED leper',
                    [FX.NONE])
    return cell('unknown', I, '', [FX.NONE])

# ---- F2: THE KIT AND THE BIRDS (14:4-7) ------------------------------
def birds(q):
    if q == 'kit':
        return cell('two_live_pure_birds+cedar+scarlet+hyssop', I, '14:4 "two LIVE PURE birds, cedar wood, scarlet, '
                    'and hyssop" — four tokens at one verse (%s)' % c_kit, [FX.NONE])
    if q == 'four_indispensable':
        return cell('block_each_other', A, 'Mishnah Menachot 3:6 — the four of the leper indispensable to one another',
                    [FX.NONE])
    if q == 'equal':
        return cell('valid_unequal', M, '14:4 "two birds" — the doubled noun [INK]; ' + SM + 'Section 1 10: equal in '
                    'look, size, and price is the command, valid unequal (Mishnah Negaim 14:5)', [FX.NONE])
    if q == 'species':
        return cell('free_bird_dror', M, '"pure" and "live" [INK]; ' + SM + 'Chapter 5 14 (R. Yosei HaGelili): one that '
                    'lives outside the city — the free sparrow; Mishnah Negaim 14:1 "two free birds"', [FX.NONE])
    if q == 'slaughter':
        return cell('one_bird_over_earthen_vessel_on_living_water', I, '14:5 "slaughter the ONE bird into an EARTHEN '
                    'vessel over LIVING water" — slaughtered, not pinched (' + SM + 'Chapter 1 7)', ['birds_die'])
    if q == 'who_slaughters':
        return cell('anyone_R._Yehuda_b._R._Yosei_priest_Rabbi', M, SM + 'Chapter 1 1 — the recorded dispute kept',
                    [FX.NONE])
    if q == 'water_quantity':
        return cell('quarter_log', D, 'the ink states living water, no measure; the sages measured a QUARTER-LOG — the '
                    'blood must stay recognizable in it (' + SM + 'Chapter 1 5; Mishnah Negaim 14:1; Menachot 9:3)',
                    [FX.NONE])
    if q == 'dip':
        return cell('live_bird_cedar_scarlet_hyssop_in_the_blood_over_the_water', I, '14:6 "the living bird he shall '
                    'take, and the cedar, the scarlet, and the hyssop, and DIP them and the living bird in the blood of '
                    'the slaughtered bird over the living water"', [FX.NONE])
    if q == 'sprinkle_count':
        return cell(7, I, '14:7 "sprinkle on the one being cleansed SEVEN times" — the seven at 14:%s' % c_seven,
                    ['sprinkled_seven'])
    if q == 'sprinkle_where':
        return cell('back_of_the_hand_or_forehead', A, 'Mishnah Negaim 14:1 — on the back of the leper\'s hand, some '
                    'say the forehead (' + SM + 'Section 2 1)', ['sprinkled_seven'])
    if q == 'purify':
        return cell('purified_by_the_body_acts', M, '14:7 "and he shall PURIFY him" [INK] — ' + SM + 'Section 2 4: '
                    'none of send, shave, wash, bathe singly withholds', ['declared_pure'])
    if q == 'send':
        return cell('over_the_open_field_not_sea_city_desert', M, '14:7 "SEND the living bird over the face of the FIELD" '
                    '[INK] — ' + SM + 'Section 2 5: not standing in Jaffa seaward, not in Gabbath desert-ward, not '
                    'outside the city sending at it (Mishnah Negaim 14:2)', ['sent_over_the_field'])
    if q == 'sent_bird':
        return cell('permitted', M, SM + 'Section 2 5 — the returned bird is permitted to eat', [FX.NONE])
    if q == 'slaughtered_bird':
        return cell('forbidden_in_any_amount', A, 'Mishnah Avodah Zarah 5:9 — the leper\'s birds among those that '
                    'forbid in any amount (the slaughtered one)', ['barred_from_it'])
    if q == 'coupled_fates':
        return cell('blood_spilled_bird_dies_bird_died_blood_poured', M, SM + 'Chapter 1 6 — the two birds\' fates '
                    'coupled (Mishnah Negaim 14:5)', ['birds_die'])
    if q == 'cedar':
        return cell('cubit_long_quarter_of_a_bed_leg', D, '14:4 names the cedar, no measure; the size is R. Yehuda\'s '
                    'sandal story (' + SM + 'Section 1 12; Mishnah Negaim 14:6)', [FX.NONE])
    if q == 'hyssop':
        return cell('plain_hyssop_no_accompanying_name', M, '14:4 "hyssop" [INK] — ' + SM + 'Section 1 15: not Greek, '
                    'blue, Roman, or desert hyssop (Mishnah Negaim 14:6)', [FX.NONE])
    return cell('unknown', I, '', [FX.NONE])

# ---- F3: THE FIRST SHAVE AND THE WEEK (14:8) -------------------------
def week(q):
    if q == 'first_shave':
        return cell('all_visible_hair', M, '14:8 "shave ALL his hair" [INK] — ' + SM + 'Section 2 7: all visible hair, '
                    'the hidden excluded', ['shaved_whole'])
    if q == 'wash_bathe':
        return cell('wash_garments_bathe_then_enter_the_camp', I, '14:8 "wash his garments... bathe in water, and be '
                    'pure, and AFTERWARD come into the camp"', ['washes_and_bathes', 'immersed'])
    if q == 'what_gates_entry':
        return cell('the_bathing_not_the_birds', M, SM + 'Section 2 10 — bathing gates camp-entry; the birds do not',
                    ['declared_pure'])
    if q == 'status':
        return cell('pure_from_defiling_by_entry_defiles_as_a_creeping_thing', A, 'Mishnah Negaim 14:2 — the first '
                    'purity: no longer defiles by entry; defiles as a creeping thing', ['declared_pure'])
    if q == 'tent_days':
        return cell(7, I, '14:8 "dwell OUTSIDE HIS TENT seven days" — the counting week inside the camp',
                    ['outside_his_tent'])
    if q == 'tent_meaning':
        return cell('his_wife_the_bed_barred', M, '"his TENT" [INK] — ' + SM + 'Section 2 11: tent = his wife '
                    '("return to your tents"); Mishnah Negaim 14:2: barred from the bed; Jotham conceived in Uzziah\'s '
                    'decided days', ['outside_his_tent'])
    if q == 'mikveh':
        return cell('even_a_mikveh', M, '14:8 "bathe in WATER" — not living water [INK]; ' + SM + 'Section 2 9: the '
                    'leper needs no living water for his body', ['immersed'])
    return cell('unknown', I, '', [FX.NONE])

# ---- F4: THE SECOND SHAVE (14:9) -------------------------------------
def shave(q):
    if q == 'sites':
        return cell('head_beard_eyebrows_all_hair', I, '14:9 "his HEAD and his BEARD and his EYEBROWS — all his hair '
                    'he shall shave" ("all his hair" x%d in the verse)' % c_all_hair, ['shaved_whole'])
    if q == 'instrument':
        return cell('razor_only_two_hairs_left_is_nothing', A, 'Mishnah Negaim 14:4 — not by a razor, or two hairs '
                    'left: did nothing (' + SM + 'Chapter 2 6)', ['shaved_whole'])
    if q == 'three_shavers':
        return cell('nazirite_leper_levites', A, 'Mishnah Negaim 14:4 — the three who shave by command', [FX.NONE])
    if q == 'status':
        return cell('tevul_yom_eats_tithe_sunset_terumah_atonement_holies', A, 'Mishnah Negaim 14:3 — the three '
                    'purities: after the second shave a tevul yom eating tithe; sunset, terumah; the atonement, holies '
                    '(Keritot 2:1: the leper lacks atonement)', ['declared_pure', 'barred_from_holies'])
    if q == 'day_gap':
        return cell('shave_seventh_offer_eighth_sunset_between', M, '14:9 "on the SEVENTH day" / 14:10 "on the EIGHTH '
                    'day" [INK] — ' + SM + 'Chapter 2 7: shaved on the eighth, not the same day (R. Akiva: sunset must '
                    'interpose; Mishnah Nazir 6:6 R. Tarfon\'s challenge: the leper\'s purity hangs on his shaving)',
                    ['declared_pure'])
    if q == 'late':
        return cell('valid_8th_9th_10th', M, SM + 'Chapter 2 5 — late shaving valid', ['shaved_whole'])
    if q == 'festival':
        return cell('shaves_on_the_festival', A, 'Mishnah Moed Katan 3:1 — the leper rising from impurity to purity '
                    'shaves on the festival (the commanded shave is not delayed)', ['shaved_whole'])
    if q == 'nazirite':
        return cell('commanded_shave_overrides', A, 'Mishnah Nazir 6:5 — shaving was permitted from its rule by the '
                    'shaving of mitzvah', ['shaved_whole'])
    return cell('unknown', I, '', [FX.NONE])

# ---- F5: THE EIGHTH DAY — THE RICH SCALE (14:10-20) ------------------
def eighth(q):
    if q == 'animals':
        return cell('two_lambs_one_ewe_of_its_first_year', I, '14:10 "two LAMBS without blemish and one EWE of its '
                    'first year without blemish" (%s)' % (c_lambs[:2],), ['accepted'])
    if q == 'minchah':
        return cell('three_tenths_mixed_with_oil', I, '14:10 "three TENTHS of fine flour, a meal offering mixed with '
                    'oil" — the tenth\'s measure is data', ['accepted'])
    if q == 'tenths_per_beast':
        return cell('one_tenth_per_beast', M, SM + 'Section 3 1 (R. Yehuda b. Beteira: the poor\'s one-tenth-per-beast '
                    'fixes the rich at three for three); Chapter 2 9-10: the three tenths belong to the beasts',
                    ['accepted'])
    if q == 'log':
        return cell('one_log', I, ('14:10 "and ONE log of oil" — one, not three (' + SM + 'Section 3 2); the log at '
                    '14:%s') % c_log, ['accepted'])
    if q == 'log_per':
        return cell('one_log_per_offering_R._Eliezer_b._Yaakov_vs_per_tenth_sages', A, 'Mishnah Menachot 9:3 — R. '
                    'Eliezer b. Yaakov: even sixty tenths one log, "for a meal offering and one log" (14:21); the '
                    'sages per tenth (' + SM + 'Section 4 5)', [FX.NONE])
    if q == 'station':
        return cell('before_the_LORD_at_the_tent_door_Nicanors_gate', D, '14:11 "the priest shall set the man being '
                    'cleansed and them BEFORE THE LORD at the door of the tent of meeting" [INK]; the gate is data '
                    'geography — Nicanor\'s gate, backs east, faces west (' + SM + 'Section 3 6; Mishnah Sotah 1:5, '
                    'Negaim 14:8)', ['presented'])
    if q == 'all_stand':
        return cell('the_man_and_the_offerings_stand_the_man_not_waved', M, SM + 'Section 3 3-5 — all stand; the '
                    'asham is waved, not the person', [FX.NONE])
    if q == 'asham_waved':
        return cell('asham_and_log_waved_together_alive', I, '14:12 "the priest shall take the one lamb and offer it '
                    'for a GUILT offering, and the log of oil, and WAVE them as a waving" — together, alive (' + SM +
                    'Section 3 7; Mishnah Menachot 5:6-7: waved not presented; hand-laying and waving alive)', ['waved'])
    if q == 'asham_place':
        return cell(CSA['place']['v'], P, '14:13 "slaughter the lamb in the place where the sin offering and the burnt '
                    'offering are slaughtered, in the holy place" — CALLED cold_run_offerings.dispatch'
                    '(communal_shelamim_and_asham) place [IMPORT, live call; ' + SM + 'Section 3 8-10: the whole north '
                    'side, the chatat there too]', ['accepted'])
    if q == 'asham_grade':
        return cell(ASHAM_GRADE, P, '14:13 "for AS the sin offering, so the guilt offering is the priest\'s; it is MOST '
                    'HOLY" — CALLED cold_run_tzav.asham_law(grade) [IMPORT, live call — the law compiled this sitting]',
                    ['most_holy', 'due_to_priest'])
    if q == 'asham_blood_altar':
        return cell(ASHAM_LEPER, P, '14:14 "the priest shall take of the blood of the guilt offering" — its altar-blood '
                    'BELOW like every asham, the 14:13 comparison defeated for placement by 7:1\'s "the law": CALLED '
                    'cold_run_tzav.asham_law(leper_blood) [IMPORT, live call]', ['accepted'])
    if q == 'altar_before_members':
        return cell('altar_first', M, SM + 'Chapter 3 2 — "what qualified him for the priest? the altar" — the altar '
                    'before the thumbs; two priests receive: one in a vessel to the altar, one in the hand to the leper '
                    '(Chapter 3 4; Mishnah Negaim 14:8)', ['accepted'])
    if q == 'members':
        return cell('right_ear_ridge_right_thumb_right_toe', I, '14:14 "on the RIDGE of the RIGHT ear of the one being '
                    'cleansed, on the thumb of his RIGHT hand, on the big toe of his RIGHT foot" — "the right" x%d at '
                    '14:14, 17, 25, 28 (the three members) and x1 at 14:16, 27 (the priest\'s right FINGER)' % c_right[14],
                    ['oil_on_the_blood'])
    if q == 'missing_member':
        return cell('no_purity_ever_R._Eliezer_its_place_R._Shimon_the_left', A, 'Mishnah Negaim 14:9 — no thumb, toe, '
                    'or right ear: no purity ever; the two dissents (' + SM + 'Chapter 3 11)', ['barred_from_holies'])
    if q == 'oil_pour':
        return cell('into_the_priests_left_palm_the_fellows_or_his_own', M, '14:15 "pour on the priest\'s LEFT palm" '
                    '[INK]; ' + SM + 'Chapter 3 7: the fellow-priest\'s palm, his own valid (Mishnah Negaim 14:10)',
                    [FX.NONE])
    if q == 'oil_sprinkle':
        return cell(7, I, '14:16 "dip his RIGHT finger in the oil on his left palm and sprinkle of the oil with his '
                    'finger SEVEN times before the LORD" — toward the Holy of Holies, a dip per sprinkling (Mishnah '
                    'Negaim 14:10)', ['sprinkled_seven'])
    if q == 'oil_on_blood':
        return cell('on_the_place_of_the_blood', M, ('14:17 "ON THE BLOOD of the guilt offering" against 14:28 "on the '
                    'PLACE of the blood" (%s) [INK] — ' + SM + 'Chapter 3 10: the place causes, not the blood — blood '
                    'wiped away, the spot still serves (Mishnah Negaim 14:10 quotes 14:28)') % (c_on_blood,),
                    ['oil_on_the_blood'])
    if q == 'head_oil':
        return cell('R._Akiva_withholds_R._Yochanan_b._Nuri_leftover_of_the_mitzvah', A, '14:18 "the REMAINDER of the '
                    'oil on the head of the one being cleansed, and the priest shall atone for him" [INK]; Mishnah '
                    'Negaim 14:10: not given — no atonement (R. Akiva) / atones either way (R. Yochanan b. Nuri)',
                    ['atoned_forgiven'])
    if q == 'log_deficit':
        return cell('before_pouring_fill_after_pouring_new_log_R._Akiva_R._Shimon_at_the_giving', A, 'Mishnah Negaim '
                    '14:10 — the deficit fork (' + SM + 'Chapter 3 6)', [FX.NONE])
    if q == 'chatat_then_olah':
        return cell('chatat_atones_then_olah', I, '14:19 "the priest shall make the SIN offering and atone for the one '
                    'being cleansed from his impurity, and AFTERWARD slaughter the burnt offering" — the order in the '
                    'ink (' + SM + 'Chapter 3 13-14: atonement by the chatat; the olah after)', ['atoned_forgiven'])
    if q == 'chatat_place':
        return cell(CHATAT_ROW['place']['v'], P, '14:19 the sin offering — the commoner\'s ewe of Lev 4:32: CALLED '
                    'cold_run_offerings.dispatch(outer_chatat) place [IMPORT, live call]', ['accepted'])
    if q == 'chatat_animal':
        return cell(COMMONER, P, '14:10 "one ewe of its first year" — the sin-offering engine\'s commoner animal: CALLED '
                    'cold_run_chatat.rank(commoner) [IMPORT, live call]', ['accepted'])
    if q == 'olah':
        return cell(OLAH_ROW['disposition']['v'], P, '14:20 "the priest shall offer up the burnt offering and the meal '
                    'offering on the altar" — CALLED cold_run_offerings.dispatch(olah:flock) disposition [IMPORT, live '
                    'call]', ['smoked_to_the_lord'])
    if q == 'atonement_gate':
        return cell('holies_after_the_atonement', A, 'Mishnah Keritot 2:1 — the leper lacks atonement until the offering; '
                    '14:20 "and he shall be PURE" — the purity verb\'s fourth seat (14:%s)' % c_pure, ['declared_pure'])
    if q == 'precedence':
        return cell(ASHAM_PREC, P, '14:12 the guilt offering BEFORE 14:19 the sin offering — the ink\'s order; CALLED '
                    'cold_run_tzav.asham_law(precedence) [IMPORT, live call; Mishnah Zevachim 10:5]', [FX.NONE])
    if q == 'age_and_price':
        return cell(ASHAM_AGE, P, '14:10 "lambs" beside "a ewe of its FIRST YEAR", no "silver shekels" in 14:10-12 — '
                    'CALLED cold_run_tzav.asham_law(age_and_price) [IMPORT, live call; Mishnah Zevachim 10:5]',
                    [FX.NONE])
    return cell('unknown', I, '', [FX.NONE])

# ---- F6: THE POOR SCALE (14:21-32) -----------------------------------
def poor(q):
    if q == 'animals':
        return cell('one_lamb_asham_one_tenth_one_log_two_birds', I, '14:21-22 "if he is POOR and his hand does not '
                    'reach: ONE lamb for a guilt offering to be waved, ONE tenth of fine flour mixed with oil, a log '
                    'of oil, and two turtledoves or two young pigeons"', ['accepted'])
    if q == 'both_clauses':
        return cell('poor_AND_hand_not_reaching', M, '"poor" AND "his hand does not reach" [INK] — ' + SM + 'Section 4 1: '
                    'each clause alone would miss a case ("until two verses say it, we have not heard")', [FX.NONE])
    if q == 'asham_never_scaled':
        return cell('the_lamb_asham_in_both_scales', I, '14:21 "one LAMB for a guilt offering" — the same asham lamb as '
                    '14:12; only the sin and burnt offerings scale to birds (' + SM + 'Section 4 4: the asham is never '
                    'scaled)', ['accepted'])
    if q == 'birds':
        return cell('one_chatat_one_olah', I, '14:22 "the one a sin offering and the one a burnt offering" — the pair '
                    'formula of 12:8, 15:15, 15:30', ['pair_owed'])
    if q == 'bird_order':
        return cell('chatat_first', P, ('14:22 writes the sin offering first [INK]; the pair\'s order is the Lev 5 engine\'s: '
                    'CALLED cold_run_vayikra5.graded_offering(birds) -> %r [IMPORT, live call; ' + SM +
                    'Section 4 14: the meal precedes the bird sin offering]') % BIRD_ORDER, ['accepted'])
    if q == 'bird_olah_place':
        return cell(BIRD_PLACE, P, '14:22 the bird burnt offering — Lev 1:14-17\'s rite: CALLED cold_run_minchah.bird(place) '
                    '[IMPORT, live call]', ['accepted'])
    if q == 'sampling_point':
        return cell('at_the_asham_R._Yehuda_Sifra_vs_the_chatat_R._Shimon', A, 'Mishnah Negaim 14:11 — poor and grew '
                    'rich, rich and grew poor: all follows the sin offering (R. Shimon) / the guilt offering (R. Yehuda); '
                    + SM + 'Section 4 13 records the asham as its own verdict: status SAMPLED at the asham',
                    ['accepted'])
    if q == 'swap':
        return cell('poor_brought_rich_valid_rich_brought_poor_not', A, 'Mishnah Negaim 14:12 (' + SM + 'Section 4 16)',
                    ['accepted', 'disqualified'])
    if q == 'vower':
        return cell('the_lepers_status_not_the_vowers', A, 'Mishnah Arakhin 4:2 — "this leper\'s offering is upon me": '
                    'a poor leper, the poor offering; 14:21 "if HE is poor" (' + SM + 'Section 4 2)', ['accepted'])
    if q == 'father':
        return cell('son_daughter_slave_maidservant_not_wife_R._Yehuda_wife_rich', A, 'Mishnah Negaim 14:12 — a man '
                    'brings the poor offering for his son, daughter, slave, maidservant; R. Yehuda: for his wife the '
                    'rich (the marriage-contract lien, ' + SM + 'Section 4 16)', ['accepted'])
    if q == 'mixed':
        return cell('writes_his_property_to_another_brings_the_poor_offering', A, 'Mishnah Negaim 14:13 — R. Yehoshua\'s '
                    'answer to the men of Alexandria', ['accepted'])
    if q == 'reach_forms':
        return cell(c_reach, I, '"his hand reaches" at 14:%s — the three reach-forms the Sifra enumerates (Section 4 11: '
                    'verses 22, 30, 31) with the closing torah\'s (32)' % c_reach, [FX.NONE])
    if q == 'closing':
        return cell('the_law_for_the_one_whose_hand_does_not_reach', I, '14:32 "this is the law for the one in whom is a '
                    'mark of leprosy, whose hand does not reach in his cleansing" — the closing torah names the poor '
                    'scale alone', [FX.NONE])
    if q == 'many_marks':
        return cell('one_offering_birds_do_not_count_until_the_chatat_R._Yehuda_asham', A, 'Mishnah Keritot 2:3 — '
                    'afflicted many times: one offering; brought his birds and was afflicted again — they do not count '
                    'until the sin offering (R. Yehuda: the guilt offering)', ['accepted'])
    return cell('unknown', I, '', [FX.NONE])

# ---- THE WRAP (W4 THE PURITY CLOCKS, 2026-09-07): the daemon over the compiled cleansing ----
import world_engine as WE
def law_metzora(event, world):
    """Lev 14:1-32 (cold_run_metzora.py — frame, birds, week, shave, eighth, poor): the leper's week as a TIMER, the purity verb's four gates."""
    k, src = event['kind'], event['case_source']
    E_ = lambda eff, s, cp=None, amount=None, due=None, law='', value=None: {'effect': eff, 'subject': s, 'counterparty': cp, 'amount': amount, 'due': due, 'value': value if value is not None else True, 'source_law': law, 'case_source': src}
    day = event.get('day', world.clock.year)
    if k == 'leper_cleansing_begun':
        l = event['leper']
        if event.get('which_leper') == 'quarantined':
            return []                                                # frame('which_leper'): the rite runs for the DECIDED leper (Mishnah Megillah 1:7) — the quarantined one's silence
        h = frame('healed'); sl = birds('slaughter'); sp = birds('sprinkle_count'); sd = birds('send'); td = week('tent_days')
        return [E_('declared_pure', l, value=h['v'], law='F1 [INK 14:2-3 "the law of the leper on the DAY of his cleansing... behold, HEALED" — %s; %s]' % (frame('one_law')['v'], frame('day')['v'])),
                E_('birds_die', 'the-slaughtered-bird', cp=l, amount=1, value=sl['v'], law='F2 [INK 14:5 "slaughter the ONE bird into an earthen vessel over living water" — the water\'s measure data: %s]' % birds('water_quantity')['v']),
                E_('barred_from_it', 'the-slaughtered-bird', value=birds('slaughtered_bird')['v'], law='F2 [Mishnah Avodah Zarah 5:9 — forbidden in any amount; the sent bird %s]' % birds('sent_bird')['v']),
                E_('sprinkled_seven', l, amount=sp['v'], value=birds('sprinkle_where')['v'], law='F2 [INK 14:7 "sprinkle on the one being cleansed SEVEN times"]'),
                E_('sent_over_the_field', 'the-living-bird', cp=l, value=sd['v'], law='F2 [INK 14:7 "SEND the living bird over the face of the FIELD" — from %s]' % event.get('send_place', 'the open field')),
                E_('declared_pure', l, value=birds('purify')['v'], law='F2 [INK 14:7 "and he shall PURIFY him" — the purity verb\'s first gate (14:%s)]' % c_pure),
                E_('shaved_whole', l, value=week('first_shave')['v'], law='F3 [INK 14:8 "shave ALL his hair" — the first shave]'),
                E_('washes_and_bathes', l, value=week('wash_bathe')['v'], law='F3 [INK 14:8 "wash his garments... bathe in water"]'),
                E_('immersed', l, value=week('mikveh')['v'], law='F3 [INK 14:8 "bathe in WATER" — not living water: even a mikveh]'),
                E_('declared_pure', l, value=week('status')['v'], law='F3 [INK 14:8 "and be pure, and AFTERWARD come into the camp" — the first purity, gated by %s]' % week('what_gates_entry')['v']),
                E_('outside_his_tent', l, amount=td['v'], due=day + td['v'] - 1, value=week('tent_meaning')['v'], law='F3 [INK 14:8 "dwell OUTSIDE HIS TENT seven days" — the TIMER to the seventh day]')]
    if k == 'leper_shaved_seventh':
        l = event['leper']; ins = shave('instrument')
        if event.get('instrument', 'razor') != 'razor' or event.get('hairs_left', 0) >= 2:
            return []                                                # 'razor_only_two_hairs_left_is_nothing' (Mishnah Negaim 14:4) — did nothing: the silence
        st = shave('status')
        return [E_('shaved_whole', l, value=shave('sites')['v'], law='F4 [INK 14:9 "his HEAD and his BEARD and his EYEBROWS — all his hair" — %s; late valid: %s]' % (ins['v'], shave('late')['v'])),
                E_('declared_pure', l, value=st['v'], law='F4 [INK 14:9 "and he shall be pure" — the second purity: %s]' % st['v']),
                E_('barred_from_holies', l, value=shave('day_gap')['v'], law='F4 [Mishnah Keritot 2:1 — the leper lacks atonement until the eighth day; the sunset between the shave and the offering]')]
    if k == 'leper_offering_brought':
        l = event['leper']; scale = event.get('scale', 'rich'); brought = event.get('brought', scale)
        if event.get('missing_member'):
            mm = eighth('missing_member')
            return [E_('barred_from_holies', l, value=mm['v'], law='F5 [Mishnah Negaim 14:9 — no thumb, toe, or right ear: no purity ever (the two dissents kept)]')]
        sw = poor('swap')
        if scale == 'rich' and brought == 'poor':
            return [E_('disqualified', l, value=sw['v'], law='F6 [Mishnah Negaim 14:12 — rich brought poor: not valid; the status sampled %s]' % poor('sampling_point')['v'])]
        out = []
        if brought == 'rich':
            an = eighth('animals')
            out.append(E_('accepted', l, cp='HEAVEN', value=an['v'], law='F5 [INK 14:10 "two lambs and one ewe of its first year, three tenths, one log" — %s; %s; the asham slaughtered %s (CALLED offerings)]' % (eighth('minchah')['v'], eighth('log')['v'], eighth('asham_place')['v'])))
        else:
            an = poor('animals')
            out.append(E_('accepted', l, cp='HEAVEN', value=an['v'], law='F6 [INK 14:21-22 "if he is POOR and his hand does not reach" — %s; the asham never scaled: %s%s]' % (poor('both_clauses')['v'], poor('asham_never_scaled')['v'], '; poor brought rich: valid (%s)' % sw['v'] if brought != scale else '')))
            out.append(E_('pair_owed', l, cp='HEAVEN', amount=1, value=poor('birds')['v'], law='F6 [INK 14:22 "the one a sin offering and the one a burnt offering" — the pair formula; the order CALLED vayikra5: %s; the bird burnt offering\'s place CALLED minchah: %s]' % (poor('bird_order')['v'], poor('bird_olah_place')['v'])))
        out += [E_('presented', l, value=eighth('station')['v'], law='F5 [INK 14:11 "set the man being cleansed and them BEFORE THE LORD at the door of the tent of meeting" — %s]' % eighth('all_stand')['v']),
                E_('waved', 'the-guilt-offering', cp=l, value=eighth('asham_waved')['v'], law='F5 [INK 14:12 "wave them as a waving before the LORD" — the asham and the log together, alive]'),
                E_('most_holy', 'the-guilt-offering', value=eighth('asham_grade')['v'], law='F5 [INK 14:13 "as the sin offering, so the guilt offering... it is MOST HOLY" — CALLED cold_run_tzav.asham_law(grade)]'),
                E_('due_to_priest', 'the-priests', cp=l, value=eighth('asham_grade')['v'], law='F5 [INK 14:13 "so the guilt offering is the priest\'s"; the precedence CALLED tzav: %s]' % eighth('precedence')['v']),
                E_('accepted', 'the-guilt-offering', cp='HEAVEN', value=eighth('asham_blood_altar')['v'], law='F5 [INK 14:14 "the priest shall take of the blood of the guilt offering" — its altar-blood below (CALLED tzav.asham_law(leper_blood)); the altar before the members: %s]' % eighth('altar_before_members')['v']),
                E_('oil_on_the_blood', l, value=eighth('members')['v'], law='F5 [INK 14:14, 14:17 the RIGHT ear-ridge, thumb, toe; the oil %s (14:28 against 14:17)]' % eighth('oil_on_blood')['v']),
                E_('sprinkled_seven', 'the-priest', amount=eighth('oil_sprinkle')['v'], value='the_oil_before_the_LORD', law='F5 [INK 14:16 "dip his RIGHT finger in the oil on his left palm and sprinkle SEVEN times before the LORD" — the pour: %s]' % eighth('oil_pour')['v']),
                E_('atoned_forgiven', l, cp='HEAVEN', value=eighth('chatat_then_olah')['v'], law='F5 [INK 14:18-19 "the remainder of the oil on his head, and the priest shall atone for him... the SIN offering and atone" — the head-oil %s; the ewe CALLED chatat.rank(commoner): %s; its place CALLED offerings: %s]' % (eighth('head_oil')['v'], eighth('chatat_animal')['v'], eighth('chatat_place')['v'])),
                E_('smoked_to_the_lord', 'the-burnt-offering', value=eighth('olah')['v'], law='F5 [INK 14:19-20 "and AFTERWARD slaughter the burnt offering... on the altar" — CALLED cold_run_offerings.dispatch(olah:flock)]'),
                E_('declared_pure', l, value=eighth('atonement_gate')['v'], law='F5 [INK 14:20 "and he shall be PURE" — the purity verb\'s fourth gate; Mishnah Keritot 2:1 the holies after the atonement; many marks one offering: %s]' % frame('one_law')['v'])]
        return out
    return []

def scene():
    """THE SCENE — Negaim 14's recorded rows replayed on the world engine (clock unit: days): the week outside his tent as a TIMER."""
    with contextlib.redirect_stdout(io.StringIO()):
        w = WE.World(era='the leper\'s cleansing: Negaim 14, Keritot 2, Megillah 1:7 on the engine (clock unit: days)')
        w.laws = [law_metzora]
        w.advance(1)
        w.submit({'kind': 'leper_cleansing_begun', 'subject': 'the-leper', 'leper': 'the-leper', 'day': 1, 'which_leper': 'decided', 'case_source': 'Lev 14:2-8; Mishnah Negaim 14:1-2 — the day, the birds, the first shave, the week outside his tent'})
        w.submit({'kind': 'leper_cleansing_begun', 'subject': 'the-quarantined', 'leper': 'the-quarantined', 'day': 1, 'which_leper': 'quarantined', 'case_source': 'Mishnah Megillah 1:7 — the one pure from quarantine: no birds, no shaving (the silence)'})
        w.submit({'kind': 'leper_cleansing_begun', 'subject': 'the-poor-leper', 'leper': 'the-poor-leper', 'day': 1, 'which_leper': 'decided', 'send_place': 'the open field', 'case_source': 'Lev 14:2-8 — the poor leper\'s week (the same rite)'})
        w.advance(7)                                                 # the seventh day: the tent week's TIMER fires
        w.submit({'kind': 'leper_shaved_seventh', 'subject': 'the-leper', 'leper': 'the-leper', 'day': 7, 'instrument': 'razor', 'hairs_left': 0, 'case_source': 'Lev 14:9; Mishnah Negaim 14:3-4 — the second shave, the three purities'})
        w.submit({'kind': 'leper_shaved_seventh', 'subject': 'the-poor-leper', 'leper': 'the-poor-leper', 'day': 7, 'instrument': 'razor', 'hairs_left': 0, 'case_source': 'Lev 14:9'})
        w.submit({'kind': 'leper_shaved_seventh', 'subject': 'the-scissors-user', 'leper': 'the-scissors-user', 'day': 7, 'instrument': 'scissors', 'hairs_left': 0, 'case_source': 'Mishnah Negaim 14:4 — not by a razor: did nothing (the silence)'})
        w.advance(8)                                                 # the eighth day
        w.submit({'kind': 'leper_offering_brought', 'subject': 'the-leper', 'leper': 'the-leper', 'day': 8, 'scale': 'rich', 'brought': 'rich', 'case_source': 'Lev 14:10-20; Mishnah Negaim 14:7-10 — the rich scale'})
        w.submit({'kind': 'leper_offering_brought', 'subject': 'the-poor-leper', 'leper': 'the-poor-leper', 'day': 8, 'scale': 'poor', 'brought': 'poor', 'case_source': 'Lev 14:21-32; Mishnah Negaim 14:7 — the poor scale'})
        w.submit({'kind': 'leper_offering_brought', 'subject': 'the-rich-who-brought-poor', 'leper': 'the-rich-who-brought-poor', 'day': 8, 'scale': 'rich', 'brought': 'poor', 'case_source': 'Mishnah Negaim 14:12 — rich brought poor: not valid'})
        w.submit({'kind': 'leper_offering_brought', 'subject': 'the-poor-who-brought-rich', 'leper': 'the-poor-who-brought-rich', 'day': 8, 'scale': 'poor', 'brought': 'rich', 'case_source': 'Mishnah Negaim 14:12 — poor brought rich: valid'})
        w.submit({'kind': 'leper_offering_brought', 'subject': 'the-maimed', 'leper': 'the-maimed', 'day': 8, 'scale': 'rich', 'brought': 'rich', 'missing_member': True, 'case_source': 'Mishnah Negaim 14:9 — no thumb: no purity ever'})
        w.advance(9)
    n = lambda eid, eff: len([e for e in w.entity(eid).ledger if e['effect'] == eff])
    tset = len([l for l in w.log if l[0] == 'TIMER-SET']); fired = len([l for l in w.log if l[0] == 'TIMER-FIRE'])
    yr = lambda eid, eff: [e['year'] for e in w.entity(eid).ledger if e['effect'] == eff]
    return (n('the-leper', 'declared_pure'), n('the-slaughtered-bird', 'birds_die'), n('the-slaughtered-bird', 'barred_from_it'), n('the-leper', 'sprinkled_seven'), n('the-living-bird', 'sent_over_the_field'),
            n('the-leper', 'shaved_whole'), n('the-leper', 'washes_and_bathes'), n('the-leper', 'immersed'), yr('the-leper', 'outside_his_tent'), n('the-quarantined', 'declared_pure'),
            n('the-leper', 'barred_from_holies'), n('the-scissors-user', 'shaved_whole'), n('the-leper', 'accepted'), n('the-leper', 'presented'), n('the-guilt-offering', 'waved'), n('the-guilt-offering', 'most_holy'),
            n('the-priests', 'due_to_priest'), n('the-guilt-offering', 'accepted'), n('the-leper', 'oil_on_the_blood'), n('the-priest', 'sprinkled_seven'), n('the-leper', 'atoned_forgiven'), n('the-burnt-offering', 'smoked_to_the_lord'),
            n('the-poor-leper', 'accepted'), n('the-poor-leper', 'pair_owed'), n('the-rich-who-brought-poor', 'disqualified'), n('the-poor-who-brought-rich', 'accepted'), n('the-maimed', 'barred_from_holies'), n('the-maimed', 'accepted'),
            tset, fired, w.clock.year), w
SCENE, _W = scene()

# ---- (2) TEST DATA — the rows, each expected value a literal ----------
TESTS = [
 # F1 the day and the priest
 ('Lev 14:2 / Keritot 2:3 — one law for all lepers', frame('one_law'), 'one_law_for_all_lepers'),
 ('Megillah 2:5 — by day, no delay', frame('day'), 'by_day_no_delay'),
 ('Lev 14:3 — the priest goes out of the camp', frame('who'), 'priest_goes_outside_the_camp'),
 ('Sifra Section 1 5 — healed: the mark gone, even partly', frame('healed'), 'mark_gone_even_partly'),
 ('Megillah 1:7 — the rite runs for the decided leper', frame('which_leper'), 'decided_not_quarantined'),
 # F2 the kit and the birds
 ('Lev 14:4 — the kit of four', birds('kit'), 'two_live_pure_birds+cedar+scarlet+hyssop'),
 ('Menachot 3:6 — the four indispensable', birds('four_indispensable'), 'block_each_other'),
 ('Negaim 14:5 — equal is the command, valid unequal', birds('equal'), 'valid_unequal'),
 ('Negaim 14:1 — free birds', birds('species'), 'free_bird_dror'),
 ('Lev 14:5 — one bird over the earthen vessel on living water', birds('slaughter'), 'one_bird_over_earthen_vessel_on_living_water'),
 ('Sifra Chapter 1 1 — who slaughters', birds('who_slaughters'), 'anyone_R._Yehuda_b._R._Yosei_priest_Rabbi'),
 ('Negaim 14:1 / Menachot 9:3 — a quarter-log of living water', birds('water_quantity'), 'quarter_log'),
 ('Lev 14:6 — the dip', birds('dip'), 'live_bird_cedar_scarlet_hyssop_in_the_blood_over_the_water'),
 ('Lev 14:7 — seven sprinklings', birds('sprinkle_count'), 7),
 ('Negaim 14:1 — on the back of the hand, some say the forehead', birds('sprinkle_where'), 'back_of_the_hand_or_forehead'),
 ('Sifra Section 2 4 — purified by the body-acts', birds('purify'), 'purified_by_the_body_acts'),
 ('Negaim 14:2 — the sending geography', birds('send'), 'over_the_open_field_not_sea_city_desert'),
 ('Sifra Section 2 5 — the sent bird permitted', birds('sent_bird'), 'permitted'),
 ('Avodah Zarah 5:9 — the slaughtered bird forbidden in any amount', birds('slaughtered_bird'), 'forbidden_in_any_amount'),
 ('Negaim 14:5 — the coupled fates', birds('coupled_fates'), 'blood_spilled_bird_dies_bird_died_blood_poured'),
 ('Negaim 14:6 — the cedar\'s size (data)', birds('cedar'), 'cubit_long_quarter_of_a_bed_leg'),
 ('Negaim 14:6 — plain hyssop', birds('hyssop'), 'plain_hyssop_no_accompanying_name'),
 # F3 the first shave and the week
 ('Sifra Section 2 7 — all visible hair', week('first_shave'), 'all_visible_hair'),
 ('Lev 14:8 — wash, bathe, then the camp', week('wash_bathe'), 'wash_garments_bathe_then_enter_the_camp'),
 ('Sifra Section 2 10 — bathing gates entry, not the birds', week('what_gates_entry'), 'the_bathing_not_the_birds'),
 ('Negaim 14:2 — the first purity', week('status'), 'pure_from_defiling_by_entry_defiles_as_a_creeping_thing'),
 ('Lev 14:8 — seven days outside his tent', week('tent_days'), 7),
 ('Negaim 14:2 — the tent is his wife', week('tent_meaning'), 'his_wife_the_bed_barred'),
 ('Sifra Section 2 9 — even a mikveh', week('mikveh'), 'even_a_mikveh'),
 # F4 the second shave
 ('Lev 14:9 — head, beard, eyebrows, all hair', shave('sites'), 'head_beard_eyebrows_all_hair'),
 ('Negaim 14:4 — razor only; two hairs left, nothing', shave('instrument'), 'razor_only_two_hairs_left_is_nothing'),
 ('Negaim 14:4 — the three commanded shavers', shave('three_shavers'), 'nazirite_leper_levites'),
 ('Negaim 14:3 — the three purities', shave('status'), 'tevul_yom_eats_tithe_sunset_terumah_atonement_holies'),
 ('Nazir 6:6 — shave the seventh, offer the eighth, sunset between', shave('day_gap'), 'shave_seventh_offer_eighth_sunset_between'),
 ('Sifra Chapter 2 5 — late shaving valid', shave('late'), 'valid_8th_9th_10th'),
 ('Moed Katan 3:1 — shaves on the festival', shave('festival'), 'shaves_on_the_festival'),
 ('Nazir 6:5 — the commanded shave overrides the nazirite\'s ban', shave('nazirite'), 'commanded_shave_overrides'),
 # F5 the eighth day, rich
 ('Lev 14:10 / Negaim 14:7 — two lambs and a ewe', eighth('animals'), 'two_lambs_one_ewe_of_its_first_year'),
 ('Lev 14:10 — three tenths mixed with oil', eighth('minchah'), 'three_tenths_mixed_with_oil'),
 ('Sifra Section 3 1 — a tenth per beast', eighth('tenths_per_beast'), 'one_tenth_per_beast'),
 ('Lev 14:10 — one log', eighth('log'), 'one_log'),
 ('Menachot 9:3 — the log per offering (R. Eliezer b. Yaakov) or per tenth', eighth('log_per'), 'one_log_per_offering_R._Eliezer_b._Yaakov_vs_per_tenth_sages'),
 ('Sotah 1:5 / Negaim 14:8 — the station: Nicanor\'s gate (data)', eighth('station'), 'before_the_LORD_at_the_tent_door_Nicanors_gate'),
 ('Sifra Section 3 3-5 — all stand; the man not waved', eighth('all_stand'), 'the_man_and_the_offerings_stand_the_man_not_waved'),
 ('Menachot 5:6-7 — the asham and the log waved together, alive', eighth('asham_waved'), 'asham_and_log_waved_together_alive'),
 ('Zevachim 5:5 — the asham slaughtered north (CALLED offerings)', eighth('asham_place'), 'north'),
 ('Lev 14:13 — most holy as the chatat (CALLED tzav)', eighth('asham_grade'), 'most holy'),
 ('Sifra Tzav Section 5 1-2 — the leper\'s asham blood below (CALLED tzav)', eighth('asham_blood_altar'), 'blood below the red line, the leper\'s included'),
 ('Negaim 14:8 — the altar before the thumbs; two receivers', eighth('altar_before_members'), 'altar_first'),
 ('Lev 14:14 — the three right members', eighth('members'), 'right_ear_ridge_right_thumb_right_toe'),
 ('Negaim 14:9 — no thumb, toe, or right ear: no purity ever', eighth('missing_member'), 'no_purity_ever_R._Eliezer_its_place_R._Shimon_the_left'),
 ('Negaim 14:10 — the log into the fellow\'s left palm', eighth('oil_pour'), 'into_the_priests_left_palm_the_fellows_or_his_own'),
 ('Lev 14:16 — seven sprinklings of oil', eighth('oil_sprinkle'), 7),
 ('Negaim 14:10 — on the PLACE of the blood', eighth('oil_on_blood'), 'on_the_place_of_the_blood'),
 ('Negaim 14:10 — the head-oil: R. Akiva / R. Yochanan b. Nuri', eighth('head_oil'), 'R._Akiva_withholds_R._Yochanan_b._Nuri_leftover_of_the_mitzvah'),
 ('Negaim 14:10 — the log deficit fork', eighth('log_deficit'), 'before_pouring_fill_after_pouring_new_log_R._Akiva_R._Shimon_at_the_giving'),
 ('Lev 14:19-20 — the sin offering atones, then the burnt offering', eighth('chatat_then_olah'), 'chatat_atones_then_olah'),
 ('Zevachim 5:3 — the sin offering north (CALLED offerings)', eighth('chatat_place'), 'north'),
 ('Lev 4:32 — the ewe is the commoner\'s animal (CALLED chatat)', eighth('chatat_animal'), 'she_goat_or_ewe_lamb'),
 ('Lev 14:20 — the burnt offering wholly to the fires (CALLED offerings)', eighth('olah'), 'wholly_to_fires'),
 ('Keritot 2:1 — holies after the atonement: the fourth purity seat', eighth('atonement_gate'), 'holies_after_the_atonement'),
 ('Zevachim 10:5 — the leper\'s asham precedes its chatat (CALLED tzav)', eighth('precedence'), 'chatat first, except the leper\'s asham'),
 ('Zevachim 10:5 — a year old, no shekel floor (CALLED tzav)', eighth('age_and_price'), 'two-year-old in silver shekels, except the nazirite\'s and the leper\'s'),
 # F6 the poor scale
 ('Lev 14:21-22 / Negaim 14:7 — the poor man\'s offerings', poor('animals'), 'one_lamb_asham_one_tenth_one_log_two_birds'),
 ('Sifra Section 4 1 — both clauses needed', poor('both_clauses'), 'poor_AND_hand_not_reaching'),
 ('Sifra Section 4 4 — the asham never scaled', poor('asham_never_scaled'), 'the_lamb_asham_in_both_scales'),
 ('Lev 14:22 — one sin offering, one burnt offering', poor('birds'), 'one_chatat_one_olah'),
 ('Lev 5:8 — the sin offering first (CALLED vayikra5)', poor('bird_order'), 'chatat_first'),
 ('Zevachim 6:5 — the bird burnt offering\'s place (CALLED minchah)', poor('bird_olah_place'), 'above_the_red_line_south_east_corner'),
 ('Negaim 14:11 — status sampled at the asham (R. Yehuda, the Sifra) or the chatat (R. Shimon)', poor('sampling_point'), 'at_the_asham_R._Yehuda_Sifra_vs_the_chatat_R._Shimon'),
 ('Negaim 14:12 — poor brought rich, valid; rich brought poor, not', poor('swap'), 'poor_brought_rich_valid_rich_brought_poor_not'),
 ('Arakhin 4:2 — the leper\'s status, not the vower\'s', poor('vower'), 'the_lepers_status_not_the_vowers'),
 ('Negaim 14:12 — the father brings the poor offering, not for his wife', poor('father'), 'son_daughter_slave_maidservant_not_wife_R._Yehuda_wife_rich'),
 ('Negaim 14:13 — the mixed offerings: R. Yehoshua\'s answer', poor('mixed'), 'writes_his_property_to_another_brings_the_poor_offering'),
 ('Sifra Section 4 11 — the reach-forms censused', poor('reach_forms'), [22, 30, 31, 32]),
 ('Lev 14:32 — the closing torah', poor('closing'), 'the_law_for_the_one_whose_hand_does_not_reach'),
 ('Keritot 2:3 — many marks, one offering; the birds do not count until the chatat', poor('many_marks'), 'one_offering_birds_do_not_count_until_the_chatat_R._Yehuda_asham'),
 # ---- THE SCENE (W4, 2026-09-07): the leper\'s week as a TIMER on the world engine ----
 ('THE SCENE — Negaim 14 on the engine: the decided leper\'s birds, first shave and week outside his tent (fired on day 7), the seventh day\'s shave, the eighth day rich and poor, the swap both ways, the maimed, the quarantined and the scissors-user silent (set, fired, the clock)',
  cell(SCENE, I, 'the purity verb\'s four gates written at 14:7, 14:8, 14:9 and 14:20 by the daemon; the guilt offering waved, most holy, the priests\' due, its blood below and the oil on the place of the blood; the poor scale\'s pair; every value the engine\'s',
       ['declared_pure', 'birds_die', 'barred_from_it', 'sprinkled_seven', 'sent_over_the_field', 'shaved_whole', 'washes_and_bathes', 'immersed', 'outside_his_tent', 'barred_from_holies', 'accepted', 'presented', 'waved', 'most_holy', 'due_to_priest', 'oil_on_the_blood', 'atoned_forgiven', 'smoked_to_the_lord', 'pair_owed', 'disqualified']),
  (5, 2, 2, 1, 2, 2, 1, 1, [7], 0, 1, 0, 1, 1, 3, 3, 3, 3, 1, 3, 1, 3, 1, 1, 1, 1, 1, 0, 2, 2, 9)),
]

# ---- (3)+(5) run, grade, effects ------------------------------------
n = len(TESTS)
assert n == GUARDED, (n, GUARDED)
print('guard: %d test rows, every expected value a literal from the answer sheet [honest-pairing guard satisfied]' % GUARDED)
print()
ok = 0
frac = {I: 0, M: 0, A: 0, D: 0, P: 0}
used = []
misses = []
for name, c, want in TESTS:
    hit = c['v'] == want
    ok += hit
    frac[c['p']] += 1
    used += [e for e in c['fx'] if e != FX.NONE]
    if not hit: misses.append((name, c['v']))
    print('%s %-96s [%s] %s' % ('OK ' if hit else 'MISS', name[:96], c['p'], '' if hit else 'got=%r' % (c['v'],)))
    print('     effects: %s' % ', '.join(c['fx']))
print()
print('MATRIX: %d/%d cells match the answer sheet' % (ok, n))
print('FRACTIONS: pure ink %d/%d (%d%%) · recorded moves %d/%d (%d%%) · answer-sheet %d/%d · data %d/%d · imports %d/%d'
      % (frac[I], n, 100 * frac[I] // n, frac[M], n, 100 * frac[M] // n, frac[A], n, frac[D], n, frac[P], n))
ops = FX.summarize(used)
print('LEDGER OPS this span writes: %s' % ', '.join('%s x%d' % kv for kv in sorted(ops.items())))
print('effects: every cell carries REGISTERED effects — seven discovered in this chapter\'s own verbs: sprinkled_seven, '
      'sent_over_the_field, shaved_whole (BODY), outside_his_tent (TIMER), declared_pure (STATUS), oil_on_the_blood (BODY), '
      'waved (STATUS) [effects law satisfied]')
_W.print_coverage()                                                  # W4: every daemon prints its watch coverage
if ok == n:
    print('THE LEPER\'S CLEANSING COMPILES — the kit of four, the slaughter over living water, the seven sprinklings, the '
          'sending over the field, the two shaves and the week outside his tent, the three purities, the eighth day\'s '
          'guilt offering waved alive with its log, the blood and the oil on the right ear-ridge, thumb, and toe, the '
          'sin offering then the burnt offering, the poor scale sampled at the asham; the offerings, Tzav, sin-offering, '
          'meal-offering, and Lev 5 engines CALLED.')
else:
    print('MISSES (%d):' % len(misses))
    for m_ in misses: print('  -', m_[0][:80], '->', m_[1])
    sys.exit('MISSES REMAIN — consult the Talmud per gap and recompile.')

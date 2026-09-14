#!/usr/bin/env python3
# NUM 4:21-7:89 — NASO: THE WORK-COUNT, THE CAMP'S PURITY, THE THEFT AND THE GIFTS, THE SUSPECTED WIFE, THE NAZIRITE, THE BLESSING,
# THE WAGONS, THE DEDICATION, THE VOICE (THE NUMBERS WALK sitting 2b, 2026-09-10; World/step9/NUMBERS_WALK.md "Sitting 2b"). The
# second Numbers portion compiled after its walk: the four work-counts by the ENGINE'S PARSER (taught the construct "two of", "eleven"
# and M-26's accent cut at this sitting — census_probes.py 34/34, every marker re-verified), the three camps CALLED from Bamidbar, the
# theft's payment algebra CALLED from Lev 5's cell, the sotah's meal-offering CALLED from the meal-offering engine, the nazirite's
# breast and thigh from Tzav's cell, the blemish list from the priesthood's, the leper's shaving from the metzora's, the sanctuary
# shekel and the anointing from the incense engine, the offerings' kinds from the offering engine, the zav and the leper from the
# purity engines; the dedication's twelve days as A SCHEDULE — twelve dues from the anointing day, retro-writes inside the stretch.
# Five motions of the deliverable rule, the wrap the sixth; every cell cites its source; every token probed (zero-report law);
# effects on every cell (the effects law). Reading ledgers: the seven logic/oral_triage/num_0{4,5,6,7}_*_2026-09-09.md; the exam's
# docket: num_04_07_naso_exam_2026-09-10.md (638 rows).

# ---- THE HONEST-PAIRING GUARD ----------------------------------------------------------------------------
import os as _os, sys as _sys
_sys.path.insert(0, _os.path.dirname(_os.path.abspath(__file__)))
from compile_guards import check_honest_pairing as _chp
_P = _os.path.abspath(__file__)
GUARDED = _chp(_P, 'CASES', 2)
assert GUARDED == 186, ('the guard counted %d expectations, the tripwire holds 186' % GUARDED)   # the guard's own count on the first run (the hand had said "about 150")
print('guard: %d expectations checked, every one a literal from the answer sheet [honest-pairing guard satisfied]' % GUARDED)
import sqlite3, sys, io, re, contextlib
import effects_layer as FX
import world_engine as WE
import cold_run_bamidbar as BM                   # THE EDGE: naso -> bamidbar CALL, reference (the three camps; the thirty days; the fitness; the houses)
import cold_run_vayikra5 as V5                   # THE EDGE: naso -> vayikra5 CALL, reference (5:6-8 = Lev 5:20-26's guilt and fifth)
import cold_run_minchah as MN                    # THE EDGE: naso -> minchah CALL, reference (5:15's no oil no frankincense; 5:26's fistful)
import cold_run_tzav as TZ                       # THE EDGE: naso -> tzav CALL, reference (6:20's breast and thigh)
import cold_run_priesthood as PR                 # THE EDGE: naso -> priesthood CALL, reference (the blemished priest and the blessing)
import cold_run_metzora as MZ                    # THE EDGE: naso -> metzora CALL, reference (the nazirite-leper shaves)
import cold_run_incense_shekel as IS             # THE EDGE: naso -> incense_shekel CALL, reference (7:13's sanctuary shekel; 7:1's anointing)
import cold_run_offerings as OF                  # THE EDGE: naso -> offerings CALL, reference (the nazirite's and the princes' animals)
import cold_run_clocks as CL                     # THE EDGE: naso -> clocks CALL, reference (5:2's zav)
import cold_run_negaim as NG                     # THE EDGE: naso -> negaim CALL, reference (5:2's leper)

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

def raw_words(ch, vs, book='Num'):
    return [h for (h,) in db.execute("""SELECT w.he FROM words w JOIN verses v ON w.verse_id=v.id WHERE v.book=?
        AND v.chapter=? AND v.verse=? ORDER BY w.idx""", (book, ch, vs)).fetchall()]

# ---- zero-report probes: the span's load-bearing tokens ---------------------------------------------------
PROBES = [
    ('נשא',      4, 22, 'lift [the head] — Gershon too'),
    ('עבדה',     4, 23, 'the work — the service of service'),
    ('ובשמת',    4, 32, 'and by names — the vessels appointed'),
    ('ויפקד',    4, 34, 'and he counted — the run'),
    ('ושמנים',   4, 48, 'and eighty — the total 8,580'),
    ('צרוע',     5, 2,  'leper — the first class'),
    ('תשלחום',   5, 3,  'you shall send them — outside the camp'),
    ('והתודו',   5, 7,  'and they shall confess'),
    ('וחמישתו',  5, 7,  'and its fifth'),
    ('גאל',      5, 8,  'kinsman — the proselyte clause'),
    ('קדשיו',    5, 10, 'his hallowed things'),
    ('תשטה',     5, 12, 'goes aside — the sin-dot the teacher re-reads'),
    ('ונסתרה',   5, 13, 'and she was secreted'),
    ('שערים',    5, 15, 'barley — the meal-offering'),
    ('קדשים',    5, 17, 'holy [water]'),
    ('ופרע',     5, 18, 'and he shall uncover'),
    ('הנקי',     5, 19, 'be free — written without the yod'),
    ('אמן',      5, 22, 'amen [amen]'),
    ('ומחה',     5, 23, 'and he shall blot out'),
    ('וקמץ',     5, 26, 'and he shall take a fistful'),
    ('ונזרעה',   5, 28, 'and she shall be sown'),
    ('ונקה',     5, 31, 'and [the man] shall be clear'),
    ('יפלא',     6, 2,  'shall clearly utter'),
    ('מיין',     6, 3,  'from wine'),
    ('מחרצנים',  6, 4,  'from kernels'),
    ('תער',      6, 5,  'a razor'),
    ('פרע',      6, 5,  'the locks'),
    ('נזר',      6, 7,  'the crown [of his God]'),
    ('בפתע',     6, 9,  'suddenly'),
    ('תרים',     6, 10, 'turtledoves'),
    ('יפלו',     6, 12, 'shall fall — the former days'),
    ('מלאת',     6, 13, 'the fulfilling — the term'),
    ('וסל',      6, 15, 'and a basket'),
    ('הזרע',     6, 19, 'the foreleg'),
    ('כפי',      6, 19, 'the palms of'),
    ('תברכו',    6, 23, 'you shall bless'),
    ('ואברכם',   6, 27, 'and I will bless them'),
    ('כלות',     7, 1,  'finishing — the day Moses finished'),
    ('צב',       7, 3,  'covered [wagons]'),
    ('בכתף',     7, 9,  'on the shoulder'),
    ('חנכת',     7, 10, 'the dedication of'),
    ('קערת',     7, 13, 'a dish of'),
    ('מלאה',     7, 14, 'full [of incense]'),
    ('עשתי',     7, 72, 'eleven[th] — the bound form'),
    ('מדבר',     7, 89, 'speaking itself — the reflexive'),
    ('הכרבים',   7, 89, 'the cherubim'),
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
WORK = {'kohath': N('Num', 4, 36)[0], 'gershon': N('Num', 4, 40)[0], 'merari': N('Num', 4, 44)[0]}
WORK_TOTAL = N('Num', 4, 48)[0]
HOUSES = dict(BM.HOUSES)                                                                                        # THE CALL: chapter 3's counts
SHARE = {k: round(100 * WORK[k] / HOUSES[k]) for k in WORK}
WAGONS = N('Num', 7, 3); DIST_G = N('Num', 7, 7); DIST_M = N('Num', 7, 8)
DISH = N('Num', 7, 13); PAN = N('Num', 7, 14); BLOCK17 = N('Num', 7, 17)
TOTALS = {v: N('Num', 7, v) for v in (84, 85, 86, 87, 88)}
DAY_TOKENS = {v: verse_text(7, v).split().count('יום') for v in (12, 72, 78)}
BLESS_WORDS = [len(verse_text(6, v).split()) for v in (24, 25, 26)]
BLESS_LETTERS = [len(verse_text(6, v).replace(' ', '')) for v in (24, 25, 26)]
NAMES = ['נחשון', 'נתנאל', 'אליאב', 'אליצור', 'שלמיאל', 'אליסף', 'אלישמע', 'גמליאל', 'אבידן', 'אחיעזר', 'פגעיאל', 'אחירע']
def prince_of(ch, vs):
    ws = verse_text(ch, vs).split(); hit = [n for n in NAMES if n in ws]; return hit[0] if hit else None
ORDER_7 = [prince_of(7, v) for v in range(12, 84, 6)]
ORDER_2 = [prince_of(2, v) for v in (3, 5, 7, 10, 12, 14, 18, 20, 22, 25, 27, 29)]
HINNAKI_DEFECTIVE = 'הנקי' in verse_text(5, 19).split() and 'הנקיי' not in verse_text(5, 19)
TISTEH_SIN = any('ׂ' in w for w in raw_words(5, 12) if strip(w) == 'תשטה')
TO_MOSES_AND_AARON = sum(1 for (b, c, v) in db.execute("SELECT DISTINCT v.book, v.chapter, v.verse FROM verses v WHERE v.book IN ('Exod','Lev','Num')").fetchall()
                         if 'אל משה ואל אהרן' in verse_text(c, v, b))
assert sum(WORK.values()) == WORK_TOTAL == 8580 and SHARE == {'kohath': 32, 'gershon': 35, 'merari': 52}, (WORK, WORK_TOTAL, SHARE)
assert WAGONS == [6, 12, 2, 1] and DIST_G == [2, 4] and DIST_M == [4, 8] and WAGONS[0] == DIST_G[0] + DIST_M[0] and WAGONS[1] == DIST_G[1] + DIST_M[1], (WAGONS, DIST_G, DIST_M)
assert DISH == [1, 130, 1, 70] and PAN == [1, 10] and BLOCK17 == [2, 5, 5, 5], (DISH, PAN, BLOCK17)
assert TOTALS[84] == [12, 12, 12] and TOTALS[85] == [130, 70, 2400] and TOTALS[86] == [12, 10, 120] and TOTALS[87] == [12, 12, 12, 12] and TOTALS[88] == [24, 60, 60, 60], TOTALS
assert 12 * (DISH[1] + DISH[3]) == TOTALS[85][2] and 12 * PAN[1] == TOTALS[86][2] and [12 * x for x in BLOCK17] == TOTALS[88], (DISH, PAN, TOTALS)
assert ORDER_7 == ORDER_2 == NAMES and DAY_TOKENS == {12: 1, 72: 2, 78: 2}, (ORDER_7, ORDER_2, DAY_TOKENS)
assert BLESS_WORDS == [3, 5, 7] and BLESS_LETTERS == [15, 20, 25] and HINNAKI_DEFECTIVE and TISTEH_SIN, (BLESS_WORDS, BLESS_LETTERS, HINNAKI_DEFECTIVE, TISTEH_SIN)
SHEKEL_SEATS = IS.shekel('twenty_gerah')['v']                                                                    # THE CALL: the sanctuary shekel's seats
assert 'Exod 30:13' in SHEKEL_SEATS, SHEKEL_SEATS
ADJ_SINNER = MN.adjuncts('sinner')['v']                                                                          # THE CALL: the sinner's meal-offering — neither oil nor frankincense
assert ADJ_SINNER == 'neither', ADJ_SINNER


# ===== THE DATA CHANNEL — the parameter rows the ink leaves open (motion 2's recorded settings) =========
DATA = {
    'fifth_base': {'value': 'a_quarter_added', 'settings': {'a_quarter_added': "the fifth is a fifth OF THE WHOLE — a quarter added to the principal (Bava Metzia 54a; Sifrei 3:1's dispute; Lev 5's cell computes it so)", 'a_fifth_of_the_principal': "a fifth of the principal itself (the other arm, Sifrei 3:1)"},
                   'source': "5:7 'and its fifth he shall add to it' — the base of 'its' the shelf's dispute"},
    'secreting_minimum': {'value': 'the_returning_of_a_palm', 'settings': {'the_returning_of_a_palm': "R. Eliezer: the time of a palm's returning (Sotah 4a; Tosefta 1:2)", 'a_cup_of_wine': "R. Yehoshua: the time to mix a cup", 'to_drink_it': "ben Azzai", 'to_roast_an_egg': "R. Akiva", 'to_swallow_it': "R. Yehuda b. Beteira", 'three_eggs': "R. Elazar b. Yirmiya (the Sifrei 7:3's six settings)"},
                          'source': "5:13 'and she was defiled SECRETLY' — the measure of seclusion = the time for defilement (Sotah 2b:21); the number the shelf's"},
    'merit_suspends': {'value': 'twelve_months', 'settings': {'three_months': "Abba Yosei b. Chanan (Sotah 20b; Sifrei 8:1)", 'nine_months': "R. Elazar b. Yitzchak", 'twelve_months': "R. Yishmael (Sifrei 8:1)", 'one_to_three_years': "Mishnah Sotah 3:4", 'none': "R. Shimon b. Yochai: merit does not suspend (Mishnah 3:5); Rebbi: suspends but she wastes"},
                       'source': "5:28 'she shall be cleared and sown with seed' — the delay the shelf's; the ink writes the two outcomes"},
    'sotah_order': {'value': 'drink_then_offer', 'settings': {'drink_then_offer': "the Rabbis (Mishnah Sotah 3:2; Sotah 19a)", 'offer_then_drink': "R. Shimon from 5:26 'AFTERWARD he shall make the woman drink'; either valid after the fact"},
                    'source': "the ink writes the drinking at 5:24 and again at 5:26-27 — the order the shelf's dispute (the reading's NS05B-08)"},
    'waters_abolished': {'value': 'running', 'settings': {'running': "the tape's world runs the rite (the ink's)", 'abolished': "Rabban Yochanan ben Zakkai abolished it when adulterers multiplied — Hosea 4:14 (Mishnah Sotah 9:9; Sotah 47b)"},
                         'source': "5:31 'the man shall be clear of iniquity' — the abolition the tradition's own setting, recorded"},
    'nazir_default_days': {'value': 30, 'settings': {30: "an unspecified naziriteship is THIRTY days (Mishnah Nazir 1:3, 6:3) — Rav Mattana: 6:5 'he shall BE [yihye] holy' counts thirty by its letters (Nazir 5a; Sifrei 25:1 'thirty from the letters'; Sanhedrin 22b; Taanit 17a; Moed Katan 19b) — a gematria, the data channel labeled"},
                           'source': "the ink writes no term at 6:2-8 — the number is the data channel's"},
    'nazir_wine_pair': {'value': 'wine_and_strong_drink', 'settings': {'wine_and_strong_drink': "6:3 'yayin and shekhar' — two tongues (the Sifrei 23:1's first)", 'diluted_and_undiluted': "the Sifrei's second", 'new_and_old': "Onkelos' third (the reading's crown)", 'shekhar_is_wine': "the Talmud's: shekhar = strong wine (Keritot 13b; Shevuot 23a; Yoma 76b)"},
                        'source': "one pair of words, four recorded readings"},
    'face_lifted': {'value': 'when_they_do_his_will', 'settings': {'when_they_do_his_will': "the Sifrei 42:2: 6:26 'lift His face' when Israel do His will, Deut 10:17 'lifts no face' when not", 'beyond_the_letter': "Berakhot 20b: Israel go beyond the letter (blessing after an olive's bulk) — so favor", 'before_the_sentence': "Niddah 70b: before the sentence He shows favor, after it not"},
                    'source': "6:26 against Deut 10:17 — one contradiction, three recorded reconciliations"},
    'blessing_name_by_place': {'value': 'the_name_in_the_temple', 'settings': {'the_name_in_the_temple': "in the Temple the Name as written; in the province the substitute (Mishnah Sotah 7:6; Tamid 7:2; Sotah 38a:9 'MY name')"},
                               'source': "6:27 'they shall put MY NAME' — the place rule the shelf's"},
    'princes_order': {'value': 'the_camps_order', 'settings': {'the_camps_order': "by the journeying (2:3-31 = 7:12-83, computed at import), not by birth (Sifrei 47:1; Reuben's protest)"},
                      'source': "the ink names the twelve by day; the order's reason the shelf's"},
    'wagons_distribution': {'value': '2/4 gershon, 4/8 merari, kohath none', 'settings': {'2/4 gershon, 4/8 merari, kohath none': "7:7-9's own numbers — as Moses saw fit (Sifrei 46:1); Kohath on the shoulder"},
                            'source': "the ink's numbers; 'as he saw fit' the shelf's"},
    'prince_exceptions': {'value': 'the_four', 'settings': {'the_four': "the Sabbath overridden (Moed Katan 9a — 'on the day of the eleventh day'), an individual's incense (the pan), a sin-offering not for a sin (the goat — the grave of the depths), one of each kind (Sifrei 51:1; Menachot 50a)"},
                          'source': "the ink writes the offerings and the days; the exceptions the shelf's"},
    'nazir_recount_day': {'value': 'the_eighth', 'settings': {'the_eighth': "Rebbi: 'he shall sanctify his head THAT DAY' (6:11) = the offerings' day (Keritot 2b; Nazir 18a)", 'the_seventh': "R. Yosei b. R. Yehuda: the shaving's day"},
                          'source': "6:11's 'that day' the shelf's dispute"},
    'sotah_witness_counts': {'value': 'two_two_one', 'settings': {'two_two_one': "R. Yehoshua: two for the warning, two for the seclusion, one for the defilement (Mishnah Sotah 1:1, 6:3; Sotah 2b:10)", 'two_one_one': "R. Eliezer: two for the warning, one (or himself) for the seclusion"},
                             'source': "5:13 'no witness [ed] against her [bah]' — the counts the shelf's"},
    'nazir_leaves': {'value': 'permitted', 'settings': {'permitted': "the Rabbis by general-and-detail: fruit and fruit-waste only (Nazir 34b:7; Sifrei 24:1)", 'forbidden': "R. Elazar by amplification-and-restriction (Nazir 34b:5) — THE METHOD FORK"},
                     'source': "6:4 'anything made of the vine, from kernels to skin' — two inference engines on one verse"},
    'general_prohibition_lashes': {'value': 'one_set', 'settings': {'one_set': "Rava (Nazir 38b:4): no lashes for a general prohibition — a seed one set", 'two_sets': "Abaye (Nazir 38b:4) — the seed's ban and 'anything of the vine': two; ATTRIBUTED TO RAVA at Pesachim 41b:5 (the tradition's own variance, recorded)"},
                                   'source': "6:4's general clause beside its details"},
    'husband_died_ketubah': {'value': 'no_drink_no_ketubah', 'settings': {'no_drink_no_ketubah': "Beit Hillel: since they cannot drink (5:15 'the MAN shall bring'), they do not collect (Mishnah Sotah 4:2; Ketubot 81a; Yevamot 38b)", 'collect': "Beit Shammai: they collect and do not drink"},
                             'source': "5:15 — a dead husband cannot bring her; the contract the shelf's institution"},
    'dust_order': {'value': 'water_then_dust', 'settings': {'water_then_dust': "5:17 'put [the dust] INTO THE WATER' — the water first; reversed unfit (Temurah 12b)", 'either': "R. Shimon: fit reversed"},
                   'source': "the ink's order; its indispensability the shelf's"},
    'vessel_joining': {'value': 'torah_law', 'settings': {'torah_law': "R. Chanin: 7:14 'one pan... full of incense' treats the contents as one (Chagigah 23b)", 'rabbinic': "R. Yochanan (Pesachim 19a)"},
                       'source': "7:14's 'full' — the joining's status the shelf's"},
    'nazir_permitted_after': {'value': 'one_offering', 'settings': {'one_offering': "the Rabbis / R. Shimon: after one offering's blood (Mishnah Nazir 6:9; Nazir 46a)", 'all': "R. Eliezer: after all the actions"},
                              'source': "6:20 'and after that the nazirite may drink wine' — which 'after' the shelf's"},
    'nazir_vow_scope': {'value': 'one_suffices', 'settings': {'one_suffices': "the Rabbis from 6:3: a vow naming one prohibition makes a full nazirite (Mishnah Nazir 1:2; Nazir 3b)", 'all_required': "R. Shimon from 6:4 'anything of the vine'"},
                        'source': "6:3 and 6:4 read against each other"},
    'anointing_scope': {'value': 'liquid_in_and_out_dry_inside', 'settings': {'liquid_in_and_out_dry_inside': "R. Yoshiya on 7:1 'them' (Menachot 57b)", 'dry_non_sacred_liquid_inside': "R. Yonatan"},
                        'source': "7:1 'and he anointed THEM' — the measures' anointing the shelf's; the incense engine's oil the object"},
}


# ===== F1: THE WORK-COUNT (Num 4:21-49) ======================================================================
def work_count(case, data):
    del P[:]
    ask = case['ask']
    if ask == 'counts':
        ink('4:36, 4:40, 4:44, 4:48', 'Kohath %d, Gershon %d, Merari %d — all %d, each from its own numerals by the engine\'s parser' % (WORK['kohath'], WORK['gershon'], WORK['merari'], WORK_TOTAL))
        return out('%d + %d + %d = %d' % (WORK['kohath'], WORK['gershon'], WORK['merari'], WORK_TOTAL), ['work_counted'])
    if ask == 'shares':
        move('CALLED cold_run_bamidbar.HOUSES -> %s [IMPORT, live]' % HOUSES, 'chapter 3\'s houses from a month old; the work-counts from thirty to fifty')
        return out('kohath 32, gershon 35, merari 52 of a hundred — the frame-carriers the largest share', ['work_counted'])
    if ask == 'ages':
        ink('4:23, 4:30, 4:35, 4:39, 4:43, 4:47', '"from thirty years old and upward until fifty years old" — the window written seven times in the chapter')
        v, e, _ = BM.charges({'ask': 'ages'}, BM.DATA)                                                             # THE CALL
        move('CALLED cold_run_bamidbar.charges(ages) -> %s [IMPORT, live]' % v, 'the ages table compiled at Bamidbar (Chullin 24a; Sifrei 62:1)')
        return out('thirty to fifty — ' + v, ['appointed_to_serve'])
    if ask == 'fitness':
        v, e, _ = BM.charges({'ask': 'fitness', 'who': case['who'], 'age': case.get('age', 40), 'carrying': case.get('carrying', True), 'blemished': case.get('blemished', False)}, BM.DATA)   # THE CALL
        move('CALLED cold_run_bamidbar.charges(fitness) -> %s [IMPORT, live]' % v, '4:47 "the work of service and the work of bearing" — the years only while carrying (Chullin 24a:11)')
        return out(v, e)
    if ask == 'song':
        ink('4:47', '"everyone who enters to do the WORK OF SERVICE and the work of bearing" — the doubled cognate (the reading\'s NS04A-04)')
        move('Arakhin 11a:17 (R. Yochanan)', 'a work performed with another service — the SONG; Arakhin 11a:19: 7:9\'s "they carry" read as "they lift up [the voice]"')
        return out('the service of service is the song (Arakhin 11a)', ['appointed_to_serve'])
    if ask == 'loads':
        ink('4:25-26', 'Gershon: the curtains, the tent, its covering, the screens, the cords — the SOFT'); ink('4:31-32', 'Merari: the frames, the bars, the pillars, the sockets, the pegs, the cords — the HARD, appointed by names'); ink('4:15; 7:9', 'Kohath: the holy — on the shoulder')
        return out('gershon the soft, merari the hard; kohath the holy (on the shoulder)', ['charge_kept'])
    if ask == 'under':
        ink('4:28, 4:33', '"in the hand of Ithamar son of Aaron the priest" — the chapter\'s two Ithamars (computed at the reading)'); ink('4:16', 'Eleazar over Kohath\'s charge')
        return out('Gershon and Merari under Ithamar; Kohath under Eleazar', ['charge_kept'])
    if ask == 'formula':
        ink('4:37, 4:45, 4:49', '"by the mouth of the LORD by the hand of Moses"'); ink('4:41', '"by the mouth of the LORD" alone — the one variant (the reading\'s NS04A-03)')
        return out('by the mouth of the LORD by the hand of Moses at 4:37, 4:45, 4:49; by the mouth of the LORD at 4:41', ['work_counted'])
    if ask == 'princes':
        ink('4:34, 4:46', '"and Moses and Aaron and the princes of the congregation counted" — the princes join the counters (the reading\'s NS04A-05)')
        return out('the princes counted with Moses and Aaron (4:34, 4:46)', ['work_counted'])
    return out('no verdict in span', [FX.NONE])


# ===== F2: THE CAMP'S PURITY (Num 5:1-4) =====================================================================
def camp_purity(case, data):
    del P[:]
    ask = case['ask']
    if ask == 'classes':
        ink('5:2', '"every leper and everyone with an issue and everyone unclean by a corpse" — three classes named')
        return out('the leper, the zav, the corpse-unclean — three classes', ['sent_outside_the_camp'])
    if ask == 'ladder':
        who = case['who']
        ink('5:2-3', '"the camp", "outside the camp", "their camps" — three camp-words (computed at the reading); "their CAMPS" plural')
        move('Pesachim 67a:11-12 (R. Yehuda from the plural; R. Shimon from the unnecessary zav); Sifrei 1:3-1:4; Zevachim 117a', 'a camp for this one and a camp for that: the leper out of three, the zav out of two, the corpse-unclean out of one')
        if who == 'leper':
            move('CALLED cold_run_negaim.standing_verdict(skin) -> %s [IMPORT, live]' % NG.standing_verdict('skin'), 'the confirmed leper — Lev 13:46 "alone, outside the camp" (Mishnah Kelim 1:5\'s confirmed / confined fork)')
            return out('out of all three camps (Israel, Levi, the Presence)', ['sent_outside_the_camp'])
        if who == 'zav':
            z = CL.zav('tier', sightings=case.get('sightings', 2))                                                  # THE CALL
            move('CALLED cold_run_clocks.zav(tier, sightings=%d) -> %s [IMPORT, live]' % (case.get('sightings', 2), z.get('v')), 'the zav of two sightings defiles bedding; of three brings an offering (Mishnah Kelim 1:5)')
            return out('out of two (Levi and the Presence)', ['sent_outside_the_camp'])
        if who == 'corpse_unclean':
            move('the heifer OWED FORWARD (Num 19 — with 8:7\'s water)', 'the corpse-unclean\'s purification the heifer\'s water; his sending the Presence\'s camp alone')
            return out('out of one (the Presence)', ['sent_outside_the_camp'])
        return out('no verdict in span', [FX.NONE])
    if ask == 'three_camps':
        v, e, _ = BM.camp({'ask': 'three_camps'}, BM.DATA)                                                         # THE CALL
        move('CALLED cold_run_bamidbar.camp(three_camps) -> %s [IMPORT, live]' % v, 'Zevachim 116b\'s mapping; Mishnah Kelim 1:7-8 the walled city, the Temple Mount, the courtyard')
        return out(v, e)
    if ask == 'who_is_sent':
        what = case['what']
        ink('5:3', '"male and female alike you shall send out"')
        if what == 'purifiable':
            return out('sent — has a purification (Eruvin 104b)', ['sent_outside_the_camp'])
        if what == 'creeping_carcass':
            move('Eruvin 104b:10 (Shmuel)', 'the send-out applies to what has a purification in a ritual bath — the carcass has none: exempt')
            return out('not sent — no purification (Eruvin 104b)', ['exempt'])
        if what == 'tumtum':
            move('Niddah 28b:1 (Rav)', '"male and female" — a definite male or female; the tumtum and the hermaphrodite not liable')
            return out('not liable — male and female (Niddah 28b)', ['exempt'])
        return out('no verdict in span', [FX.NONE])
    if ask == 'entered_impure':
        ink('5:3', '"that they not defile their camps" — THE PROHIBITION'); move('Num 19:13 [IMPORT]; Makkot 14b:6; Mishnah Makkot 3:2', 'the punishment (karet) there, the prohibition here — the impure who entered the Temple is flogged')
        return out('lashes (5:3 the prohibition, 19:13 the punishment)', ['lashes'])
    if ask == 'leper_entered':
        move('Pesachim 67a:7 (Rav Chisda) / 67a:11 (R. Yehuda\'s tanna)', 'the leper beyond his boundary: exempt from lashes by Lev 13:46 "alone" — or liable (the dispute)')
        return out('a dispute: exempt (Rav Chisda) / liable (R. Yehuda\'s tanna)', ['lashes'])
    if ask == 'impure_pesach':
        move('Pesachim 67b:8, 95b:14 (R. Eliezer); Menachot 95b:1', 'zavim and lepers are liable to karet only when the corpse-unclean are sent; the Passover in impurity — not')
        return out('zavim and lepers not liable to karet (R. Eliezer)' if case.get('majority_impure') else 'liable to karet (the corpse-unclean sent)', ['exempt'] if case.get('majority_impure') else ['karet_cut_off'])
    if ask == 'tevul_yom_pesach':
        move('Pesachim 92a:15', 'the send-out (a positive command without karet) is overridden by the Passover\'s (with karet): one who immersed that day may enter')
        return out('may enter — the Passover\'s karet overrides (Pesachim 92a)', ['exempt'])
    if ask == 'tent_rolled_up':
        move('Taanit 21b:5', 'when the curtain was rolled up for travel, zavim and lepers could enter its place — the sanctity the Presence\'s, not the ground\'s')
        v, e, _ = BM.camp({'ask': 'tent_on_the_march'}, BM.DATA)                                                   # THE CALL
        move('CALLED cold_run_bamidbar.camp(tent_on_the_march) -> %s [IMPORT, live]' % v, 'the tent on the march still the tent — the two rows together: the tent moves with the Presence, the place stays behind')
        return out('the place unsacred — the Presence, not the ground (Taanit 21b)', ['exempt'])
    if ask == 'warning':
        move('Sifrei 1:1', 'Num 19:20 gives the punishment (karet) for defiling the sanctuary and no warning — 5:2-3 is the warning')
        return out('the warning for 19:20\'s punishment (Sifrei 1:1)', ['sent_outside_the_camp'])
    if ask == 'day':
        move('Gittin 60a:17 (R. Levi)', 'eight sections said on the day the tabernacle was erected — the sending away of the impure among them: a READING-PLACED date, the tape\'s retrograde marker at 5:1')
        return out('the first of Nisan — R. Levi\'s eight sections (Gittin 60a:17): reading-placed', ['sent_outside_the_camp'])
    if ask == 'run_doubled':
        ink('5:4', '"and the children of Israel did so... as the LORD spoke to Moses, so did the children of Israel" — the report doubled')
        move('Sifrei 1:8 (R. Yossi HaGelili)', 'before the calf there were no zavim and lepers; the doubling read')
        return out('before the calf no zavim; after — the doubling (Sifrei 1:8)', ['sent_outside_the_camp'])
    return out('no verdict in span', [FX.NONE])


# ===== F3: THE THEFT'S RESTITUTION AND THE GIFTS (Num 5:5-10) ================================================
def restitution(case, data):
    del P[:]
    ask = case['ask']
    if ask == 'confession':
        ink('5:7', '"and they shall confess their sin which they did"'); move('Mishnah Sanhedrin 6:2', 'all the executed confess (Achan\'s "I have sinned"); Sifrei 2:1 the confession here')
        return out('confess (the executed confess — Sanhedrin 6:2)', ['guilt_acknowledged'])
    if ask == 'principal':
        ink('5:7', '"and he shall return his guilt AT ITS HEAD" — the principal'); move('Bava Kamma 110a:12-17', '"guilt" = the principal, "restitution" = the fifth — not the double payment')
        return out('at its head — the principal, not the double', ['pays'])
    if ask == 'fifth':
        s = data['fifth_base']['value']; dat('the row fifth_base = %s: %s' % (s, data['fifth_base']['settings'][s]))
        return out('a quarter added = a fifth of the whole (Bava Metzia 54a)' if s == 'a_quarter_added' else 'a fifth of the principal', ['adds_fifth'])
    if ask == 'algebra':
        claim = {'claim_kind': 'robbery', 'swore_falsely': True, 'value': case.get('value', 100), 'swore_on_fifth': case.get('swore_on_fifth', False)}
        v, pr = V5.deposit_restitution(claim, V5.DATA)                                                            # THE CALL
        move('CALLED cold_run_vayikra5.deposit_restitution(robbery, swore, %s) -> %r [IMPORT, live]' % (claim['value'], v), 'the section repeats Lev 5:20-26 for the proselyte (Sifrei 2:1 the rule of repetition) — the algebra is Lev 5\'s')
        return out(v, ['pays', 'adds_fifth'])
    if ask == 'order':
        ink('5:8', '"the restitution... to the priest; BESIDES the ram of atonement"'); move('Bava Kamma 111a:11-14 (Rava); Mishnah Bava Kamma 9:12', 'the money first, then the ram; the ram first does not discharge')
        return out('the money first, then the ram (Bava Kamma 111a; Mishnah 9:12)', ['pays'])
    if ask == 'proselyte_dead':
        ink('5:8', '"if the man has no kinsman to whom the guilt may be restored, the guilt restored is the LORD\'s, to the priest"')
        move('Bava Kamma 109a:5 (Tosefta 10:16); Sifrei 4:1 (R. Yishmael); Mishnah Bava Kamma 9:11', 'is there a Jew without kinsmen? — the proselyte who died without heirs'); move('Arakhin 28b:1-2; Bava Kamma 109b:6', 'to the priests OF THE WATCH — as the ram goes to the priest on duty')
        return out('to the priests of the watch (5:8; Arakhin 28b)', ['due_to_priest'])
    if ask == 'robber_died_before':
        move('Mishnah Bava Kamma 9:11', 'died on the way — the money to his children; the ram grazes till blemished, sold for communal gifts')
        return out('the money to his children; the ram grazes, sold for communal gifts (Mishnah 9:11)', ['exempt'])
    if ask == 'given_then_died':
        ink('5:10', '"what a man gives the priest, his it shall be"'); move('Mishnah Bava Kamma 9:12; Bava Kamma 110a:9', 'the heirs cannot reclaim from the watch')
        return out('the heirs cannot reclaim — 5:10 (Mishnah 9:12)', ['due_to_priest'])
    if ask == 'fifth_not_precluding':
        move('Mishnah Bava Kamma 9:12', 'gave the principal but not the fifth — the offering not precluded')
        return out('the fifth missing does not preclude the ram (Mishnah 9:12)', ['pays'])
    if ask == 'woman_equals_man':
        ink('5:6', '"when a man or WOMAN shall commit any of the sins of a person"'); move('Bava Kamma 15a:4; Kiddushin 35a; Pesachim 43a; Sukkah 28a; Temurah 2b; Yevamot 84b (Rav; the school of R. Yishmael)', 'THE EQUATING RULE')
        return out('a woman equals a man for all punishments (5:6 — Bava Kamma 15a)', ['pays'])
    if ask == 'priest_thief':
        move('Sifrei 4:2', 'a priest who robbed the proselyte does not keep what is in his hand — the a-fortiori refused by the verse')
        return out('the priest-thief does not keep it (Sifrei 4:2)', ['due_to_priest'])
    if ask == 'to_whom':
        ink('5:7', '"and give it to the one against whom he was guilty"'); move('Mishnah Bava Kamma 9:5', 'to the victim himself, even to Media; not to his son or agent; to the court\'s agent; if he died, to the heirs'); move('R. Natan (Bava Kamma 40b; Gittin 37a; Ketubot 19a, 82a; Kiddushin 15a; Pesachim 31a)', 'the creditor\'s creditor paid directly — the courts engine\'s reference')
        return out('to the victim himself, even to Media; not his son or agent (Mishnah 9:5)', ['pays'])
    if ask == 'remainder':
        move('Mishnah Bava Kamma 9:6', 'the principal paid, the fifth not — need not pursue; the fifth paid, the principal not — must pursue; a perutah the floor')
        return out('pursue for the principal, not for the fifth; a perutah the floor (Mishnah 9:6)', ['pays'])
    if ask == 'robbed_father':
        ink('5:7', '"their sin which THEY did" — his own (Sifrei 3:1)'); move('Mishnah Bava Kamma 9:9', 'robbed his father, swore, the father died, admitted — pays the father\'s sons or brothers, forfeits his share, brings the ram')
        return out('to the father\'s sons or brothers; forfeits his share; the ram (Mishnah 9:9)', ['pays', 'adds_fifth'])
    if ask == 'confessed_after_oath':
        move('Bava Kamma 106a:16 (Rava)', 'one who admits a false oath on a deposit pays the principal and the fifth even where the oath would have exempted')
        return out('principal and fifth even where the oath would exempt (Bava Kamma 106a)', ['pays', 'adds_fifth'])
    if ask == 'proselyte_female':
        move('Bava Kamma 109b:3 (Ravina)', '5:8\'s "the MAN has no kinsman" — a female proselyte: an open dilemma')
        return out('an open dilemma (Bava Kamma 109b:3)', [FX.NONE])
    # ---- the gifts (5:9-10) ----
    if ask == 'owners_choice':
        ink('5:9-10', '"every heave-offering... which they bring to the priest, his shall be; and every man\'s hallowed things shall be his; what a man gives the priest, his it shall be"'); move('Sifrei 5:1-6:1; Arakhin 34a:6', 'the owner gives to the priest he chooses; the priest who offers his own keeps its portions')
        return out('the owner\'s choice of priest; the priest\'s own offering his', ['due_to_priest'])
    if ask == 'terumah_measure':
        move('Mishnah Terumot 4:5', 'R. Eliezer up to a tenth; R. Yishmael half; R. Tarfon and R. Akiva as long as some remains non-sacred')
        return out('the owner\'s measure, with a floor: some must remain non-sacred (Mishnah Terumot 4:5)', ['due_to_priest'])
    if ask == 'blemished_priests_offering':
        move('Bava Kamma 109b:16', 'a blemished priest gives his offering to a priest of his own watch to sacrifice; the flesh and the hide his (5:10)')
        return out('flesh and hide his (Bava Kamma 109b:16)', ['due_to_priest'])
    if ask == 'firstborn_thirty':
        v, e, _ = BM.levites({'ask': 'age', 'age_days': case.get('age_days', 31)}, BM.DATA)                          # THE CALL
        move('CALLED cold_run_bamidbar.levites(age, %d) -> %s [IMPORT, live]' % (case.get('age_days', 31), v), 'the Sifrei 6:1 reads the firstborn\'s redemption among the gifts of 5:9; the thirty days Bamidbar\'s cell (Bekhorot 49a)')
        return out(v, e)
    if ask == 'tithe_inserted':
        move('Onkelos 5:10 (the reading\'s crown)', '"THE TITHE of his holy things" — the translation\'s insertion; the Sifrei\'s reading beside it')
        return out('the tithe Onkelos inserts at 5:10', ['due_to_priest'])
    return out('no verdict in span', [FX.NONE])

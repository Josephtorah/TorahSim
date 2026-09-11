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
assert GUARDED == 274, ('the guard counted %d expectations, the tripwire holds 274' % GUARDED)   # the guard's own count on the first run (the hand had typed 186 before the rows were written)
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
import cold_run_chukat as CK                     # THE EDGE: naso -> chukat CALL, reference (5:2's corpse-unclean — his purification Num 19:12, 19:19; PAID at THE NUMBERS WALK 6b, 2026-09-11)

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
    ('אברכם',    6, 27, 'I will bless them — after "and I" (ואני), two words on the ink'),
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
assert DISH == [1, 130, 1, 70, 2] and PAN == [1, 10] and BLOCK17 == [2, 5, 5, 5], (DISH, PAN, BLOCK17)   # THE NUMBERS WALK 3b (2026-09-10): the fifth number is 7:13's 'BOTH OF THEM full of fine flour' (שניהם — the suffixed numeral the parser now reads); the dish and the bowl stay DISH[1] and DISH[3]
assert TOTALS[84] == [12, 12, 12] and TOTALS[85] == [130, 1, 70, 1, 2400] and TOTALS[86] == [12, 10, 120] and TOTALS[87] == [12, 12, 12, 12] and TOTALS[88] == [24, 60, 60, 60], TOTALS   # THE NUMBERS WALK 4b (2026-09-10): THE DEFINITE ONE — 7:85 'a hundred and thirty THE ONE dish... seventy THE ONE bowl' now reads its two ones (retyped from the reading; was [130, 70, 2400])
assert 12 * (DISH[1] + DISH[3]) == TOTALS[85][4] and 12 * PAN[1] == TOTALS[86][2] and [12 * x for x in BLOCK17] == TOTALS[88], (DISH, PAN, TOTALS)
assert ORDER_7 == ORDER_2 == NAMES and DAY_TOKENS == {12: 0, 72: 1, 78: 1}, (ORDER_7, ORDER_2, DAY_TOKENS)   # the BARE word יום (day) — absent from the first ten day-heads (only ביום 'on the day'), present once at 7:72 and 7:78: 'on the eleventh day, DAY' — the doubled day the Sifrei reads (the first run measured 0/1/1 against the hand's 1/2/2, which had counted the prefixed word)
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
            c = CK.corpse_tumah({'ask': 'purification'}, CK.DATA)                                                   # THE CALL (was: the heifer OWED FORWARD — paid at THE NUMBERS WALK 6b, 2026-09-11)
            move('CALLED cold_run_chukat.corpse_tumah(purification) -> %s [IMPORT, live]' % c[0], 'the corpse-unclean\'s purification the heifer\'s water (Num 19:12, 19:19); his sending the Presence\'s camp alone')
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


# ===== F4: THE SUSPECTED WIFE (Num 5:11-31) =================================================================
def sotah(case, data):
    del P[:]
    ask = case['ask']
    if ask == 'conditions':
        ink('5:13', '"a man lay with her... hidden from her husband\'s eyes, and she was secreted and defiled, and there is no witness against her, and she was not seized" — six clauses (the reading\'s NS05B-02)')
        return out('six: lain with, hidden, secreted, defiled, no witness, not seized', ['forbidden_to_her_husband'])
    if ask == 'witnesses':
        what = case['what']
        ink('5:13', '"and there is no witness [ed] against her [bah]" — the singular: not two witnesses, one (Sotah 2a:12)')
        if what == 'defilement':
            return out('one witness suffices (5:13)', ['forbidden_to_her_husband'])
        s = data['sotah_witness_counts']['value']; dat('the row sotah_witness_counts = %s: %s' % (s, data['sotah_witness_counts']['settings'][s]))
        if what == 'warning':
            return out('two (R. Yehoshua; the mishnah)', ['forbidden_to_her_husband'])
        if what == 'seclusion':
            return out('two (R. Yehoshua) — R. Eliezer one' if s == 'two_two_one' else 'one or himself (R. Eliezer)', ['forbidden_to_her_husband'])
        return out('no verdict in span', [FX.NONE])
    if ask == 'secluded':
        s = data['secreting_minimum']['value']; dat('the row secreting_minimum = %s: %s' % (s, data['secreting_minimum']['settings'][s]))
        ink('5:13', '"and she was defiled SECRETLY" — the measure of seclusion = the time for defilement (Sotah 2b:21, 4a:9)')
        return out('the time for the first stage of intercourse — the returning of a palm (R. Eliezer)', ['forbidden_to_her_husband'])
    if ask == 'status':
        who = case['who']
        if who in ('betrothed', 'awaiting_levir'):
            ink('5:29', '"when a wife, UNDER HER HUSBAND, goes aside"'); move('Mishnah Sotah 4:1; Kiddushin 27b:7; Sotah 24a:11-12', 'the betrothed and the widow awaiting the levir neither drink nor collect — not yet under her husband (R. Yoshiya: the widow drinks — recorded)')
            return out('neither drinks nor collects (5:29 under her husband)', ['exempt', 'ketubah_forfeited'])
        if who == 'forbidden_marriage':
            move('Mishnah Sotah 4:1', 'a widow to a High Priest, a divorcee to a priest, a mamzeret to an Israelite — the rite applies to permitted marriages')
            return out('neither drinks nor collects (a forbidden marriage)', ['exempt', 'ketubah_forfeited'])
        if who == 'ailonit':
            ink('5:28', '"she shall be cleared and sown with seed" — whose way is to bear'); move('Sotah 25b-26a; Mishnah 4:3', 'the sexually undeveloped woman neither drinks nor collects (R. Elazar: drinks — recorded)')
            return out('neither (the Rabbis; R. Elazar: drinks)', ['exempt', 'ketubah_forfeited'])
        if who == 'convert':
            ink('5:12', '"and SAY TO THEM" — the amplification'); move('Sotah 26a:11; Mishnah Eduyot 5:6', 'the proselyte woman drinks (the Sages; Akavya: not — Karkemit)')
            return out('drinks (the Sages; Akavya recorded)', ['tested_by_the_waters'])
        if who == 'priests_wife':
            move('Mishnah Sotah 4:4; Sotah 26a:12; Yevamot 56b', 'the priest\'s wife drinks; cleared she is permitted (raped she would be forbidden — "she")')
            return out('drinks; cleared she is permitted', ['tested_by_the_waters'])
        if who == 'eunuchs_wife':
            move('Mishnah Sotah 4:4; Sotah 26a:15', 'the eunuch\'s wife drinks — "besides your husband" does not exclude him')
            return out('drinks', ['tested_by_the_waters'])
        if who == 'pregnant_or_nursing':
            move('Mishnah Sotah 4:3', 'R. Meir: neither; the Rabbis: he separates and remarries — drinks')
            return out('the Rabbis: drinks; R. Meir: neither', ['tested_by_the_waters'])
        if who == 'married':
            return out('drinks or forfeits her contract (Mishnah 4:3)', ['tested_by_the_waters'])
        return out('no verdict in span', [FX.NONE])
    if ask == 'husband_clean':
        ink('5:31', '"and the man shall be clear from iniquity, and that woman shall bear her iniquity"')
        move('Kiddushin 27b:9; Shevuot 5a:10; Sotah 28a:1, 47b; Yevamot 58a:12; Sifrei 21:3', 'when the man is clear the water tests his wife; not clear — it does not (the reading\'s NS05B-11)')
        return out('tested' if case.get('clean', True) else 'the waters do not test — the man not clear of iniquity (5:31)', ['tested_by_the_waters'] if case.get('clean', True) else ['exempt'])
    if ask == 'husband_first':
        ink('5:20', '"some man has lain with you BESIDES your husband"'); move('Sotah 24b:2; Yevamot 58a:14 (R. Acha bar Chanina)', 'only when the husband\'s cohabitation preceded the paramour\'s')
        return out('only when the husband\'s cohabitation preceded (5:20)', ['tested_by_the_waters'])
    if ask == 'husband_dead':
        s = data['husband_died_ketubah']['value']; dat('the row husband_died_ketubah = %s: %s' % (s, data['husband_died_ketubah']['settings'][s]))
        return out('Beit Hillel: no drink, no ketubah' if s == 'no_drink_no_ketubah' else 'Beit Shammai: collect, no drink', ['exempt', 'ketubah_forfeited'] if s == 'no_drink_no_ketubah' else ['exempt'])
    if ask == 'warned_about':
        who = case['who']
        if who in ('relative', 'gentile', 'shachuf'):
            move('Mishnah Sotah 4:4; Sotah 26b:1-6 (Shmuel; Rav Hamnuna)', 'a warning about a forbidden relative, a gentile, a shachuf — valid (the two "defiled"s do not exclude)')
            return out('valid', ['forbidden_to_her_husband'])
        if who in ('minor', 'beast'):
            ink('5:13', '"and a MAN lay with her"'); move('Mishnah Sotah 4:4; Sotah 26b:2', 'not a minor, not one who is not a man')
            return out('no warning', ['exempt'])
        return out('no verdict in span', [FX.NONE])
    if ask == 'warning_scope':
        ink('5:12', '"and say to them"'); move('Sotah 24a:10', 'the betrothed and the widow awaiting the levir are included in the WARNING (forbidden by it), not the drinking')
        return out('the betrothed and the shomeret yavam can be warned, not tested', ['forbidden_to_her_husband'])
    if ask == 'court_warns':
        ink('5:12', '"the wife of ANY man"'); move('Mishnah Sotah 4:5; Sotah 27a:7-9', 'the court warns the deaf-mute\'s, the imbecile\'s, the prisoner\'s wife — to disqualify the ketubah (the Sages); R. Yosei: to drink when he returns')
        return out('to disqualify the ketubah (the Sages); R. Yosei: to drink too', ['ketubah_forfeited'])
    if ask == 'witnesses_overseas':
        move('Sotah 6a:10 (Rav Sheshet)', '"no witness against her" — witnesses overseas exist: the water does not test her')
        return out('not tested — witnesses exist overseas', ['exempt'])
    if ask == 'witnesses_conspiring':
        move('Keritot 24a:9 (R. Elazar)', 'the witnesses to her seclusion found conspiring — her meal-offering non-sacred')
        return out('her minchah non-sacred', ['exempt'])
    if ask == 'rumor':
        move('Mishnah Sotah 6:1', 'warned and secluded on a bird\'s word — R. Eliezer: divorces her with the ketubah; R. Yehoshua: not until the spinners by moonlight')
        return out('R. Eliezer: divorce with the ketubah; R. Yehoshua: not until the spinners', ['forbidden_to_her_husband'])
    if ask == 'witness_of_defilement':
        who = case['who']
        move('Mishnah Sotah 6:2', 'one witness of defilement — she does not drink; a slave or maidservant believed to bar the ketubah; her mother-in-law and the four believed only to bar the drinking')
        return out('believed — bars the ketubah' if who in ('slave', 'maidservant', 'any') else 'believed only to bar the drinking', ['ketubah_forfeited'] if who in ('slave', 'maidservant', 'any') else ['exempt'])
    if ask == 'contradicting':
        f, a = case['for'], case['against']
        move('Mishnah Sotah 6:4', 'one against one, one against two — she drinks; two against one — does not drink, divorced')
        return out('does not drink, divorced' if (f == 2 and a == 1) else 'drinks', ['exempt'] if (f == 2 and a == 1) else ['tested_by_the_waters'])
    if ask == 'escort':
        ink('5:15', '"the MAN shall bring his wife to the priest"'); move('Sotah 7a:10; Mishnah 1:3', 'by Torah law he alone; the Sages: two scholars accompany (R. Yehuda: trusted)')
        return out('two scholars (rabbinic; R. Yehuda: trusted)', ['tested_by_the_waters'])
    if ask == 'court':
        ink('5:30', '"all this LAW"'); move('Sotah 7b:3 (torah/torah with Deut 17:11); Mishnah 1:4', 'the Great Sanhedrin of seventy-one')
        return out('the Sanhedrin of seventy-one (torah/torah)', ['tested_by_the_waters'])
    if ask == 'admonition':
        move('Mishnah Sotah 1:4', 'threatened as capital witnesses: wine, levity, immaturity, bad neighbors; act for the great Name, that it not be erased')
        return out('wine, levity, immaturity, bad neighbors; act for the great Name', ['tested_by_the_waters'])
    if ask == 'confesses':
        move('Mishnah Sotah 1:5', '"I am defiled" — she writes a receipt for her contract and is divorced')
        return out('a receipt for the ketubah; divorced', ['ketubah_forfeited', 'forbidden_to_her_husband'])
    if ask == 'place':
        ink('5:18', '"the priest shall stand the woman BEFORE THE LORD"'); move('Sotah 8a:2; Mishnah 1:5', 'the Eastern Gate — Nicanor\'s, opposite the Sanctuary')
        return out('the Nicanor gate — before the LORD', ['tested_by_the_waters'])
    if ask == 'uncovering':
        ink('5:18', '"and uncover the woman\'s head"'); move('Sotah 8a:10; Mishnah 1:5-6', 'the head, the body, the hair unbraided; black garments; the adornments removed; the Egyptian rope; watchers except her slaves (R. Yehuda: unless attractive)')
        return out('the head, the body, the hair unbraided; black garments; the Egyptian rope; the adornments removed', ['tested_by_the_waters'])
    if ask == 'minchah_form':
        ink('5:15', '"a tenth of an ephah of BARLEY meal; he shall pour no oil on it nor put frankincense on it"'); move('Mishnah Sotah 2:1; Menachot 59a:5; Mishnah Menachot 5:3', 'barley, unsifted; in a basket then a service vessel; neither oil nor frankincense')
        move('CALLED cold_run_minchah.adjuncts(sinner) -> %s [IMPORT, live]' % ADJ_SINNER, 'the sinner\'s meal-offering (Lev 5:11) the parallel — neither (the Sifrei 8:1\'s reading)')
        return out('barley, unsifted; no oil, no frankincense — as the sinner\'s: ' + ADJ_SINNER, ['accepted'])
    if ask == 'ephah':
        move('Onkelos 5:15 (the reading\'s crown)', '"a tenth of THREE SE\'AH" — the conversion layer on a dry measure')
        return out('a tenth of an ephah = a tenth of three se\'ah (Onkelos)', ['accepted'])
    if ask == 'fistful':
        f = MN.fistful('overflowing_or_fingertips')['v']                                                          # THE CALL
        ink('5:26', '"the priest shall take a fistful of the meal-offering, its memorial, and burn it on the altar"')
        move('CALLED cold_run_minchah.fistful(overflowing_or_fingertips) -> %s [IMPORT, live]' % f, 'the scoop\'s measure the meal-offering engine\'s: level, three fingers over the palm')
        return out('the scoop level — the meal-offering engine: overflowing or fingertips ' + f, ['accepted'])
    if ask == 'waving':
        ink('5:25', '"the priest shall take the meal-offering from the woman\'s HAND and wave it"'); move('Kiddushin 36b:4-5; Sotah 19a:9-10; Mishnah 3:1', 'hand/hand with Lev 7:30 — by her hand and the priest\'s together')
        return out('by her hand and the priest\'s together (hand/hand with Lev 7:30)', ['accepted'])
    if ask == 'bringing_near':
        ink('5:25', '"and draw it near to the altar"'); move('Menachot 60b:6, 61a:8; Mishnah Menachot 5:6', 'the sotah\'s minchah requires both bringing near and waving')
        return out('required (5:25 draw it near)', ['accepted'])
    if ask == 'minchah_not_for_its_name':
        ink('5:15', '"a reminder of iniquity" / Lev 10:17 "to bear the iniquity"'); move('Menachot 4a:8-16', 'like a sin-offering: not for its name disqualified; the surplus to communal gifts')
        return out('disqualified; the surplus to communal gifts', ['disqualified'])
    if ask == 'water_and_dust':
        ink('5:17', '"holy water in an earthen vessel; and of the dust on the floor of the tabernacle... into the water"')
        s = data['dust_order']['value']; dat('the row dust_order = %s' % s)
        move('Mishnah Sotah 2:2; Sotah 15b; Menachot 88b:3; Temurah 12b:6', 'half a log from the laver (R. Yehuda a quarter); the cubit-square tablet, the ring, the dust visible; water first')
        return out('half a log from the laver (R. Yehuda a quarter); the dust from the Sanctuary floor, visible on the water; water first (R. Shimon: either)', ['accepted'])
    if ask == 'vessel':
        move('Sotah 15b:4 (R. Yishmael: vessel/vessel with the leper\'s); 15b:9 (Rabba)', 'a NEW earthenware vessel')
        return out('a new earthenware vessel (R. Yishmael)', ['accepted'])
    if ask == 'bitter_added':
        ink('5:23', '"into the water of BITTERNESS" — bitter before the erasure'); move('Sotah 20a:4 (Shmuel\'s father)', 'a bitter substance is put in')
        return out('a bitter substance in the water', ['accepted'])
    if ask == 'scroll_text':
        move('Mishnah Sotah 2:3; Sotah 17a; Berakhot 15b:24', 'the Rabbis: 5:19 through 5:22\'s curses, without 5:21\'s frame and the amens; R. Yosei the whole; R. Yehuda the curses alone')
        return out('from 5:19 through 5:22\'s curses, without the frame and the amens (the Rabbis); R. Yosei whole; R. Yehuda curses alone', ['accepted'])
    if ask == 'scroll_material':
        ink('5:23', '"the priest shall write these curses IN A SCROLL and blot them out into the water"'); move('Mishnah Sotah 2:4; Sotah 17b:1-2; Eruvin 13a:10', 'parchment; ink that can be blotted out — no iron sulfate')
        return out('a scroll (parchment); erasable ink; no iron sulfate', ['accepted'])
    if ask == 'scroll_time':
        move('Sotah 17b:3 (Rava; torah/torah)', 'written at night — unfit'); return out('by day', ['accepted'])
    if ask == 'scroll_order':
        move('Sotah 17b:4', '"THESE curses" — as written in the Torah'); return out('the Torah\'s order', ['accepted'])
    if ask == 'scroll_before_oath':
        ink('5:21, 5:23', 'the oath, then the writing'); move('Sotah 17b:5', 'written before the oath — unfit'); return out('unfit', ['disqualified'])
    if ask == 'scroll_erasure':
        move('Sotah 18a:2', '"all this law" — written whole, erased at once'); return out('written whole, erased at once', ['accepted'])
    if ask == 'for_her_name':
        ink('5:30', '"and the priest shall PERFORM with her all this law"'); move('Eruvin 13b:2; Sotah 20b:6', 'the erasure for her name; the writing need not be')
        return out('the erasure for her name; the writing not', ['accepted'])
    if ask == 'language':
        ink('5:21', '"and the priest shall SAY to the woman"'); move('Sotah 32b:2; Mishnah 7:1', 'in any language')
        return out('any language', ['accepted'])
    if ask == 'oath_order':
        ink('5:19-20', 'the innocent clause first, then "but if you have gone aside"'); move('Sanhedrin 32b:18 (Rebbi; Abaye and Rava)', 'the priest states the innocent scenario first')
        return out('the innocent clause first', ['accepted'])
    if ask == 'oaths_count':
        ink('5:19, 5:21', '"the priest shall cause her to swear" — twice'); move('Sotah 18a:8 (R. Zeira, Rav)', 'one before the erasure, one after')
        return out('two: before and after the erasure', ['accepted'])
    if ask == 'amen_amen':
        ink('5:22', '"and the woman shall say: amen, amen" — the bare double at Num 5:22 and Neh 8:6 alone (the reading)'); move('Mishnah Sotah 2:5; Kiddushin 27b:6', 'on the curse and the oath; this man and another; betrothed, married, awaiting the levir, married to the levir')
        return out('on the curse and the oath; this man and another; betrothed, married, awaiting the levir, married to the levir', ['accepted'])
    if ask == 'amen_is_oath':
        move('Shevuot 29b:9 (Shmuel)', 'one who answers amen is as one who swore'); return out('amen = her oath (Shmuel)', ['accepted'])
    if ask == 'oath_form':
        ink('5:21', '"the oath of the curse" — Lev 5:1\'s "curse" by the identity (Sifrei 14:1)'); move('Shevuot 35b:23-36a:10', 'an oath is a curse, administered in the Name; amen the oath')
        return out('a curse, in the Name', ['accepted'])
    if ask == 'oath_scope':
        move('Mishnah Sotah 2:6', 'not before betrothal nor after divorce — only acts that would forbid her'); return out('only acts that would forbid her', ['accepted'])
    if ask == 'several_warnings':
        ink('5:29', '"this is the law of JEALOUSIES" — plural'); move('Keritot 9b:10', 'one meal-offering for several warnings'); return out('one meal-offering (jealousies)', ['accepted'])
    if ask == 'order':
        s = data['sotah_order']['value']; dat('the row sotah_order = %s: %s' % (s, data['sotah_order']['settings'][s]))
        return out('drink then offer (the Rabbis); R. Shimon offer then drink; either valid after the fact', ['tested_by_the_waters'])
    if ask == 'preconditions':
        ink('5:26', '"AFTERWARD he shall make the woman drink"'); move('Sotah 19b:2 (R. Shimon)', 'three preclude: the fistful offered, the scroll erased, the oath accepted')
        return out('R. Shimon: the fistful offered, the scroll erased, the oath accepted', ['tested_by_the_waters'])
    if ask == 'refuses':
        when = case['when']
        move('Mishnah Sotah 3:3; Sotah 19b:1 (R. Akiva)', 'before the erasure: the scroll sequestered, the minchah burned; after: forced; confessed after: the water poured out')
        if when == 'before_erasure':
            return out('the scroll sequestered, the minchah burned; not forced', ['exempt'])
        if when == 'after_erasure':
            return out('forced to drink', ['tested_by_the_waters'])
        if when == 'confesses_after_erasure':
            return out('the water poured out, the minchah scattered', ['ketubah_forfeited'])
        return out('no verdict in span', [FX.NONE])
    if ask == 'time':
        move('Mishnah Megillah 2:5; Megillah 20b:9, 20b:17; Sotah 17b:3', 'by day, the whole day'); return out('by day, the whole day', ['tested_by_the_waters'])
    if ask == 'two_at_once':
        ink('5:16, 5:27', '"bring HER near"; "make HER drink" — her alone'); move('Sotah 8a:4; Nedarim 73a:7 (R. Yehuda)', 'not two together'); return out('not together', ['tested_by_the_waters'])
    if ask == 'outcome':
        if case.get('guilty'):
            if case.get('merit'):
                s = data['merit_suspends']['value']; dat('the row merit_suspends = %s: %s' % (s, data['merit_suspends']['settings'][s]))
                return out('suspended (three, nine, twelve months — the Sifrei; one to three years — the mishnah; R. Shimon none)', ['tested_by_the_waters'])
            ink('5:27', '"her belly shall swell and her thigh fall, and the woman shall be a curse"'); move('Mishnah Sotah 3:4, 1:7; Sotah 9b, 28a:14', 'her face greens, her eyes bulge — the thigh first (measure for measure); the paramour too')
            return out('her face greens, her belly swells, her thigh falls — she dies; the paramour too', ['tested_by_the_waters', 'put_to_death'])
        ink('5:28', '"and if the woman was not defiled but is clean, she shall be cleared and sown with seed"'); move('Sotah 26a:7-8 (R. Akiva / R. Yishmael)', 'the barren conceives; or pain to ease, females to males')
        return out('cleared and sown with seed (the barren conceives — R. Akiva; R. Yishmael: ease)', ['tested_by_the_waters', 'accepted'])
    if ask == 'paramour_tested':
        ink('5:24, 5:27', '"the water shall enter her" twice'); move('Mishnah Sotah 5:1; Sotah 27b:3, 28a:9-10', 'the water tests him as her')
        return out('tested too (5:24, 5:27)', ['tested_by_the_waters'])
    if ask == 'defiled_consequences':
        ink('5:14, 5:27, 5:29', '"defiled" thrice; 5:29\'s "AND is defiled" the vav'); move('Sotah 28a:19, 29a:2 (R. Akiva); Mishnah 5:1', 'forbidden to her husband, to her paramour, to the priesthood, from terumah')
        return out('forbidden to her husband, her paramour, the priesthood and terumah (R. Akiva)', ['forbidden_to_her_husband'])
    if ask == 'doubt_forbids':
        ink('5:14', '"and she was defiled... or she was not defiled" — the doubtful case'); move('Sotah 28a:21; Mishnah 1:2', 'forbidden to her husband until clarified')
        return out('forbidden to her husband until clarified', ['forbidden_to_her_husband'])
    if ask == 'levirate':
        move('Yevamot 11a:10; Mishnah Sotah 1:2', '"defiled" with Lev 18:24\'s — as a forbidden relative: she and her rival exempt from levirate and chalitzah')
        return out('exempt from levirate and chalitzah (Yevamot 11a)', ['exempt'])
    if ask == 'minchah_disposition':
        c = case['case']
        move('Mishnah Sotah 3:6-7', 'impure before the vessel — redeemed; after — burned; the confessed, the witnessed, the refusing, the husband\'s refusal or cohabitation — burned; every priest\'s wife\'s burned; a priest\'s daughter married to an Israelite — eaten')
        if c == 'priests_daughter_to_israelite':
            return out('eaten', ['accepted'])
        return out('burned (once in a service vessel; redeemed if before)', ['disqualified'])
    if ask == 'disabled':
        ink('5:13, 5:18, 5:22', '"hidden from the EYES"; "STAND the woman... in her HANDS"; "the woman shall SAY"'); move('Sotah 27a:10-27b:1 (Rav Sheshet, Rav Ashi, Mar bar Rav Ashi)', 'blind, lame, handless, mute — neither side')
        return out('neither side drinks or gives to drink', ['exempt'])
    if ask == 'intercourse':
        ink('5:13', '"and SHE was not seized" — raped, permitted; "she" adds cases')
        if case.get('who') == 'priests_wife':
            move('Yevamot 56b:7', 'the priest\'s wife forbidden even when seized'); return out('forbidden (the priest\'s wife)', ['forbidden_to_her_husband'])
        move('Ketubot 51b:13 (Rava); 74a:13; Yevamot 100b', 'raped permitted; begun under duress ended willingly permitted; the mistaken betrothal permitted')
        return out('permitted to her husband', ['accepted'])
    if ask == 'drinks_twice':
        ink('5:29', '"this is the law of jealousy"'); move('Sotah 18b:15', 'she drinks and drinks again for a second warning'); return out('drinks again for a second warning', ['tested_by_the_waters'])
    if ask == 'abolished':
        s = data['waters_abolished']['value']; dat('the row waters_abolished = %s: %s' % (s, data['waters_abolished']['settings'][s]))
        return out('the rite runs (the ink); abolished by Rabban Yochanan ben Zakkai — Hosea 4:14 (the tradition\'s setting)', ['tested_by_the_waters'])
    if ask == 'warning_permitted':
        ink('5:14', '"and he warned his wife"'); move('Sotah 3a:17 (R. Eliezer b. Yaakov); 3a:10', 'permitted against "you shall not hate"; optional (R. Yishmael) or obligatory (R. Akiva)')
        return out('permitted (R. Eliezer b. Yaakov); optional or obligatory disputed', ['forbidden_to_her_husband'])
    if ask == 'spelling':
        ink('5:19', '"hinnaki" written WITHOUT the yod — measured on the DB: %s' % HINNAKI_DEFECTIVE); ink('5:12', '"tisteh" with the sin-dot — measured: %s' % TISTEH_SIN)
        move('Kiddushin 62a:2 (R. Tanchum); Sotah 3a:4 (Reish Lakish)', 'read also chinnaki (you shall choke); read tishteh (folly) — M-16\'s shape on the sotah\'s own verses')
        return out('hinnaki without the yod read also as chinnaki; tisteh read as folly — the ink measured', ['forbidden_to_her_husband'])
    return out('no verdict in span', [FX.NONE])


# ===== F5: THE NAZIRITE (Num 6:1-21) =========================================================================
def nazirite(case, data):
    del P[:]
    ask = case['ask']
    if ask == 'vow_form':
        form = case['form']
        ink('6:2', '"when a man or woman shall clearly utter a vow, the vow of a nazirite [nazir], to separate [lehazir]"')
        if form in ('substitute', 'intimation'):
            move('Nedarim 3a:5; Mishnah Nedarim 1:1, Nazir 1:1', 'nazir lehazir — substitutes and intimations bind'); return out('binds (nazir lehazir)', ['nazirite_vow_bound'])
        if form == 'partial':
            s = data['nazir_vow_scope']['value']; dat('the row nazir_vow_scope = %s' % s); move('Mishnah Nazir 1:2; Nazir 3b:11, 4a:3', 'one prohibition named — a full nazirite (R. Shimon: all required)')
            return out('a full nazirite', ['nazirite_vow_bound'])
        if form == 'birds':
            move('Mishnah Nazir 1:1; Nazir 2a:3, 3b:2', 'R. Meir: a nazirite (the impure nazirite\'s birds); the Sages: not'); return out('the Sages: not (R. Meir: a nazirite)', ['exempt'])
        if form == 'from_the_cup':
            move('Mishnah Nazir 2:3', 'a cup poured — a full nazirite; the intoxicated woman\'s a konam on the cup'); return out('a nazirite; the drunk woman\'s a konam', ['nazirite_vow_bound'])
        if form == 'conditioned_on_wine':
            move('Mishnah Nazir 2:4', 'on condition to drink and become impure — a full nazirite'); return out('a full nazirite', ['nazirite_vow_bound'])
        if form == 'mistaken_no_wine':
            move('Mishnah Nazir 2:4', 'did not know wine is forbidden — bound (R. Shimon: free)'); return out('bound (R. Shimon free)', ['nazirite_vow_bound'])
        if form == 'mistaken_sages_permit':
            move('Mishnah Nazir 2:4', 'thought the Sages would permit — free (R. Shimon: bound)'); return out('free (R. Shimon bound)', ['exempt'])
        if form == 'figs':
            move('Mishnah Nazir 2:1; Nazir 9a:2', 'Beit Shammai: a nazirite; Beit Hillel: not'); return out('Beit Hillel: not (Shammai: a nazirite)', ['exempt'])
        if form == 'samson':
            move('Mishnah Nazir 1:2', 'a Samson-nazirite never shaves and brings no impurity offering'); return out('a Samson-nazirite: never shaves, no impurity offering', ['nazirite_vow_bound'])
        if form == 'permanent':
            move('Mishnah Nazir 1:2', 'the permanent nazirite lightens with a razor and brings three'); return out('lightens with a razor every thirty, brings three', ['nazirite_vow_bound'])
        if form == 'ambiguous_intimation':
            move('Nedarim 5b:5', 'Abaye valid, Rava not'); return out('Rava: not', ['exempt'])
        if form == 'uncertain':
            move('Mishnah Nazir 5:5; Nazir 34a:1', 'Shammai all; Hillel whose statement failed; R. Tarfon none (explicitness)'); return out('Hillel: whose statement failed; R. Tarfon none', ['nazirite_vow_bound'])
        return out('no verdict in span', [FX.NONE])
    if ask == 'who_vows':
        who, age = case['who'], case.get('age')
        ink('6:2', '"speak to the children of Israel... a man or woman"')
        if who == 'gentile':
            move('Nazir 61a:7-12; Mishnah 9:1; Menachot 73b', '"the children of Israel" — not the gentiles'); return out('no naziriteship', ['exempt'])
        if who == 'woman':
            move('Mishnah Nazir 9:1', 'women yes (the husband nullifies, cannot force)'); return out('yes', ['nazirite_vow_bound'])
        if who == 'slave':
            move('Nazir 61a:7; Mishnah 9:1', '"a man or woman" includes slaves (the master forces)'); return out('yes (the master forces)', ['nazirite_vow_bound'])
        if who == 'boy':
            move('Niddah 46a:2; Mishnah Niddah 5:6', 'thirteen and a day — valid; the twelfth year examined')
            return out('valid (thirteen and a day)' if age >= 13 else ('examined (the twelfth year)' if age == 12 else 'invalid'), ['nazirite_vow_bound'] if age >= 13 else ['exempt'])
        if who == 'girl':
            move('Mishnah Niddah 5:6', 'twelve and a day — valid; the eleventh year examined')
            return out('valid (twelve and a day)' if age >= 12 else ('examined (the eleventh year)' if age == 11 else 'invalid'), ['nazirite_vow_bound'] if age >= 12 else ['exempt'])
        return out('no verdict in span', [FX.NONE])
    if ask == 'term':
        form = case['form']; d = data['nazir_default_days']['value']
        dat('the row nazir_default_days = %d: %s' % (d, data['nazir_default_days']['settings'][d]))
        if form in ('unspecified', 'long', 'short', 'till_the_end_of_the_world'):
            move('Mishnah Nazir 1:3', 'unspecified, long, short, till the end of the world — thirty'); return out('%d days' % d, ['nazirite_vow_bound'])
        if form == 'and_a_day':
            move('Mishnah Nazir 1:3', '"and a day", "and an hour", "one and a half" — two terms'); return out('%d days (two terms)' % (2 * d), ['nazirite_vow_bound'])
        if form == 'thirty_and_an_hour':
            move('Mishnah Nazir 1:3', 'no naziriteship for hours — thirty-one'); return out('31 days', ['nazirite_vow_bound'])
        if form == 'like_the_hairs':
            move('Mishnah Nazir 1:4', 'forever, shaving every thirty (Rebbi: one long term)'); return out('forever, shaving every thirty (Rebbi: one term)', ['nazirite_vow_bound'])
        if form == 'capacity':
            move('Mishnah Nazir 1:5', 'asked his intent: one long term — thirty; unspecified — mustard seeds, a life'); return out('a life (mustard seeds) or thirty by his intent', ['nazirite_vow_bound'])
        if form == 'distance':
            move('Mishnah Nazir 1:6', 'the days of the walk; under thirty — thirty'); return out('%d days' % max(d, case.get('days', 0)), ['nazirite_vow_bound'])
        if form == 'solar_year':
            move('Mishnah Nazir 1:7', '365 consecutive terms'); return out('365 terms', ['nazirite_vow_bound'])
        if form == 'hundred_days':
            return out('100 days', ['nazirite_vow_bound'])
        return out('no verdict in span', [FX.NONE])
    if ask == 'shaving_day':
        form = case['form']
        move('Mishnah Nazir 3:1-2', 'unspecified — the thirty-first (the thirtieth fulfilled); "thirty days" — the thirty-first only; two terms — 31 and 61 (30 and 60; 59 fulfilled)')
        if form == 'unspecified':
            return out('the thirty-first (the thirtieth fulfilled)', ['nazirite_term_fulfilled'])
        if form == 'stated_thirty':
            return out('the thirty-first only', ['nazirite_term_fulfilled'])
        if form == 'two_terms':
            return out('31 and 61 (30 and 60; 59 fulfilled)', ['nazirite_term_fulfilled'])
        return out('no verdict in span', [FX.NONE])
    if ask == 'ate':
        product, amount = case['product'], case.get('amount', 'olive')
        ink('6:3-4', '"from wine and strong drink he shall separate; vinegar... anything soaked... fresh or dried... anything made of the vine, from kernels to skin"')
        if product == 'leaves':
            s = data['nazir_leaves']['value']; dat('the row nazir_leaves = %s: %s' % (s, data['nazir_leaves']['settings'][s]))
            return out('permitted (the Rabbis; R. Elazar forbids)', ['exempt'])
        if product == 'wine' and amount == 'less_than_a_quarter_log':
            move('Mishnah Nazir 6:1; Nazir 38b:1', 'a quarter-log for drinking (R. Akiva: an olive\'s bulk with bread)'); return out('exempt (R. Akiva: an olive\'s bulk with bread)', ['exempt'])
        if product == 'mixture':
            move('Nazir 35b:12, 38a:2; Pesachim 43b (R. Yochanan; R. Elazar)', '"soaked" — permitted combines with forbidden for the nazirite alone'); return out('combines — liable (soaked)', ['lashes'])
        if product == 'seed':
            s = data['general_prohibition_lashes']['value']; dat('the row general_prohibition_lashes = %s' % s)
            return out('lashes (Rava one set; Abaye two)', ['lashes'])
        if product == 'two_seeds_one_skin':
            move('Mishnah Nazir 6:2 (R. Elazar b. Azarya)', 'liable only for two chartzannim and a zag — 6:4\'s plural and singular'); return out('R. Elazar b. Azarya\'s measure — liable', ['lashes'])
        move('Mishnah Nazir 6:1-2; Nazir 38b:2; 34b:11', 'wine, grapes, kernels, skins, vinegar each by itself — an olive\'s bulk; each kind called by two names liable for each')
        return out('lashes', ['lashes'])
    if ask == 'mitzvah_wine':
        move('Nazir 4a:3, 44a:9; Sifrei 23:1', '"wine AND strong drink" — obligatory wine like optional'); return out('forbidden like optional', ['lashes'])
    if ask == 'benefit_from_wine':
        ink('6:4', '"all the days of HIS naziriteship"'); move('Pesachim 23a:5 (Mar Zutra)', 'the nazirite may own and benefit from wine'); return out('permitted (his naziriteship)', ['exempt'])
    if ask == 'shaving_means':
        means = case['means']
        ink('6:5', '"a razor shall not come upon his head... he shall be holy, let the locks grow"')
        if means in ('razor', 'scissors'):
            move('Mishnah Nazir 6:3', 'scissors or a razor — liable'); return out('liable', ['lashes'])
        if means == 'plucked_any':
            move('Nazir 39b:5-6 (R. Yoshiya / R. Yonatan); Mishnah 6:3', 'plucked any amount — liable (R. Yoshiya; R. Yonatan exempt)'); return out('R. Yoshiya liable (R. Yonatan exempt)', ['lashes'])
        if means == 'shampoo':
            move('Mishnah Nazir 6:3', 'may shampoo and separate by hand; not comb (R. Yishmael: not with earth)'); return out('permitted; combing not', ['exempt'])
        return out('no verdict in span', [FX.NONE])
    if ask == 'shaved_by_another':
        ink('6:5', '"a razor shall not COME upon his head" — passive'); move('Nazir 44a:17', 'he and another — both liable'); return out('both liable', ['lashes'])
    if ask == 'shaving_amount':
        ink('6:9', '"on the seventh day he shall shave IT"'); move('Nazir 42a:3', 'not fulfilled until all is removed'); return out('all the hair', ['accepted'])
    if ask == 'final_shaving_tool':
        move('Nazir 40a:2-10 (Rebbi); Mishnah 6:3\'s rider', 'the final shaving by razor; the Levites\' razor 8:7 (Beha\'alotcha\'s)'); return out('a razor', ['accepted'])
    if ask == 'impurity_kinds':
        source, mode = case['source'], case.get('mode', 'contact')
        ink('6:6-7, 6:9', '"he shall not come upon a dead body... when they die"; "if any man DIE suddenly beside him"')
        if source in ('corpse', 'olive_of_corpse', 'ladle_of_dust', 'spine', 'skull', 'limb', 'half_kav_bones', 'half_log_blood'):
            move('Mishnah Nazir 7:2', 'shaves — by contact, carrying and tent'); return out('shaves', ['count_voided'])
        if source == 'barley_grain_bone':
            move('Mishnah Nazir 7:2', 'by contact and carrying, not by tent'); return out('shaves' if mode != 'tent' else 'not — the barley-grain bone does not defile by tent', ['count_voided'] if mode != 'tent' else ['exempt'])
        if source == 'quarter_log_blood':
            move('Mishnah Nazir 7:3-4', 'R. Akiva\'s a-fortiori refused: a halakhah to Moses from Sinai'); return out('not (a halakhah to Moses from Sinai — R. Akiva\'s a-fortiori refused)', ['exempt'])
        if source in ('boughs', 'beit_haperas', 'land_of_nations', 'grave_cover', 'tent_only', 'quarter_kav_bones', 'vessels_touching'):
            move('Mishnah Nazir 7:3', 'sprinkled but no negation and no offering'); return out('not — sprinkled, no negation', ['exempt'])
        if source in ('leprosy', 'ziva'):
            move('Nazir 48a:1 (Rebbi); Mishnah 7:3', '"when they die" — not their leprosy or ziva; the leper\'s and zav\'s days count'); return out('not corpse impurity — no negation; the days count', ['exempt'])
        if source == 'creeping':
            move('Pesachim 80b:15', 'only corpse impurity interrupts'); return out('not — only the corpse', ['exempt'])
        return out('no verdict in span', [FX.NONE])
    if ask == 'impurity_for':
        who = case['who']
        ink('6:7', '"for his father, or his mother, for his brother, or his sister he shall not become impure when they die"')
        if who == 'relative':
            move('Zevachim 100a:6; Sanhedrin 35a:13', 'not — even on the way to the Passover or the circumcision'); return out('not — even on the way to the Passover', ['exempt'])
        if who == 'met_mitzvah':
            move('Nazir 44a:8, 48a-48b; Yevamot 7a:3; Megillah 3b:8; Berakhot 19b:15; Mishnah 7:1', 'becomes impure — even on the way to the Passover'); return out('becomes impure — even on the way to the Passover', ['count_voided'])
        return out('no verdict in span', [FX.NONE])
    if ask == 'met_mitzvah_with_high_priest':
        move('Mishnah Nazir 7:1', 'R. Eliezer: the priest (no offering); the Rabbis: the nazirite (his holiness not permanent)'); return out('the nazirite becomes impure (the Rabbis); R. Eliezer the priest', ['count_voided'])
    if ask == 'impurity_lashes':
        move('Nazir 42b:1 (Rabba, Rav Huna)', 'contact, carrying, tent — one ban; entering an enclosure — another; impure again — one set'); return out('a set per distinct ban (the corpse and the enclosure); repeated impurity one set', ['lashes'])
    if ask == 'lashes_count':
        n = case.get('warnings', 0)
        move('Mishnah Makkot 3:7-8; Mishnah Nazir 6:4', 'all day — one set; per warning followed by the act — each'); return out('%d set(s) — one, or one per warning' % max(1, n), ['lashes'])
    if ask == 'what_negates':
        act = case['act']
        ink('6:12', '"the former days shall fall, for his separation was defiled"')
        if act == 'impurity':
            day, term = case.get('day', 15), case.get('term', 30)
            if day <= 2:
                move('Nazir 19b:2-5 (Abaye; Rava)', '"the first days" plural — no negation until two days'); return out('nothing — no first days (two)', ['exempt'])
            if term == 30 and day == 30:
                move('Mishnah Nazir 3:3', 'impure on the thirtieth — negates all (R. Eliezer seven)'); return out('all (R. Eliezer seven)', ['count_voided'])
            if term == 100 and day == 100:
                move('Mishnah Nazir 3:4', 'the hundredth — all (R. Eliezer thirty)'); return out('all (R. Eliezer thirty)', ['count_voided'])
            if term == 100 and day == 101:
                move('Mishnah Nazir 3:4', 'the 101st before the offerings — thirty (R. Eliezer seven)'); return out('thirty (R. Eliezer seven)', ['count_voided'])
            move('Mishnah Nazir 6:5, 7:2; Nazir 44a:13', 'impurity negates all — recount after purification and offerings'); return out('all — recount after purification and offerings', ['count_voided'])
        if act == 'shaving':
            move('Mishnah Nazir 6:3, 6:5; Nazir 44a:13', 'shaving negates thirty'); return out('thirty', ['count_voided'])
        if act == 'wine':
            move('Nazir 44a:11', 'wine negates nothing'); return out('nothing', ['lashes'])
        if act == 'unknown_impurity':
            ink('6:9', '"BESIDE him" — known'); move('Nazir 63a:4; Pesachim 81b:4; Mishnah 9:2', 'the grave of the depths does not negate'); return out('nothing (the depths)', ['exempt'])
        return out('no verdict in span', [FX.NONE])
    if ask == 'vowed_in_cemetery':
        move('Mishnah Nazir 3:5; Nazir 18a:2', 'the days there do not count; no shaving, no birds; left and re-entered — counts and brings (R. Eliezer: not the same day)'); return out('the days do not count; no shaving, no birds; re-entered: counts and brings', ['exempt'])
    if ask == 'defiled':
        ink('6:9-12', '"he shall shave his head on the day of his cleansing, on the seventh day; on the eighth day two turtledoves or two young pigeons... a lamb of its first year for a guilt-offering; the former days shall fall"')
        s = data['nazir_recount_day']['value']; dat('the row nazir_recount_day = %s' % s)
        move('Mishnah Nazir 6:6; Keritot 2b:5; Mishnah Keritot 2:2; Nazir 18a-18b', 'sprinkled the third and seventh, shaves the seventh, brings the eighth; intentional as unwitting; the recount from the eighth (Rebbi)')
        return out('sprinkled the third and seventh, shaves the seventh, brings the eighth (a lamb asham, two birds); intentional as unwitting; the recount from the eighth', ['count_voided'])
    if ask == 'birds':
        move('Mishnah Kinnim 1:1, 2:5; Sifrei 29:2', 'one sin-offering, one burnt-offering; a turtledove not paired with a pigeon'); return out('one chatat, one olah; not mixed', ['accepted'])
    if ask == 'completion':
        ink('6:13-18', '"he shall bring himself to the door... one he-lamb for a burnt-offering, one ewe-lamb for a sin-offering, one ram for peace-offerings, and a basket of unleavened bread... and the nazirite shall shave his consecrated head at the door of the tent of meeting"')
        move('Mishnah Nazir 6:7-8; Nazir 45a', 'three animals; shaves after the peace-offering (R. Yehuda; R. Elazar the sin); any one suffices; unspecified animals sorted by fitness')
        d = OF.dispatch('todah_and_nazir_ram')                                                                    # THE CALL
        move('CALLED cold_run_offerings.dispatch(todah_and_nazir_ram) -> %s [IMPORT, live]' % sorted(d), 'the ram\'s procedure the offering engine\'s')
        return out('three animals — the sin, the burnt, the peace; shaves after the peace-offering (R. Yehuda; R. Elazar the sin); any one suffices', ['nazirite_term_fulfilled'])
    if ask == 'where_shaves':
        ink('6:18', '"at the door of the tent of meeting... on the fire under the sacrifice of the peace-offering"'); move('Nazir 45a:13 (R. Yitzchak); Sifrei 34:1; Yoma 16a:2; 45a:14 (Abba Chanan)', 'where the peace-offering is cooked — the Chamber of the Nazirites; Abba Chanan: while the entrance is open')
        return out('where the peace-offering is cooked — the Chamber of the Nazirites (Abba Chanan: while the entrance is open)', ['nazirite_term_fulfilled'])
    if ask == 'hair_under_pot':
        where, which = case.get('where', 'temple'), case.get('which', 'purity')
        move('Mishnah Nazir 6:8; Menachot 91b:1; Temurah 34a:4', 'the purity shaving in the Temple: under the peace-offering\'s pot (the sin or guilt fulfill); the province: not thrown; the impurity shaving: not thrown, the hair buried')
        if which == 'impurity':
            return out('not thrown; the hair buried (the pure\'s burned)', ['count_voided'])
        if where == 'province':
            return out('not thrown', ['nazirite_term_fulfilled'])
        return out('under the peace-offering\'s pot (the others fulfill)', ['nazirite_term_fulfilled'])
    if ask == 'hair':
        ink('6:5', '"he shall be HOLY, let the locks grow" — the hair holy'); move('Kiddushin 57b:6; Avodah Zarah 74a:3; Temurah 28a:11; Mishnah AZ 5:9', 'forbidden for benefit in any amount; burned')
        return out('holy — forbidden for benefit in any amount; burned', ['disqualified'])
    if ask == 'loaves':
        ink('6:15', '"a basket of unleavened bread, loaves mingled with oil and wafers spread with oil, and their meal-offering and their libations"'); move('Mishnah Menachot 7:2, 3:6; Menachot 46b, 78a, 91a-b', 'loaves and wafers, ten kav; both indispensable; sanctified by the ram\'s slaughter; libations for the burnt- and peace-offerings')
        return out('loaves and wafers (no poached), ten kav; both indispensable; sanctified by the ram\'s slaughter; with libations for the burnt- and peace-offerings', ['accepted'])
    if ask == 'foreleg':
        v, e, _ = TZ.dues_machine({'ask': 'breast_thigh'}, TZ.PARAMS)                                                # THE CALL
        ink('6:19-20', '"the cooked foreleg of the ram, one loaf, one wafer on the palms of the nazirite... waved... holy to the priest beside the breast of waving and the thigh of lifting"')
        move('CALLED cold_run_tzav.dues_machine(breast_thigh) -> %s [IMPORT, live]' % v, 'I11 stated on 6:20 (Sifrei 37:1): the breast and thigh kept out of the shoulder-law; the nazirite woman waves too (Kiddushin 36b:7)')
        return out('the cooked foreleg, a loaf and a wafer on his palms, waved (the woman too); beside the ' + v, ['due_to_priest'])
    if ask == 'foreleg_bounds':
        move('Mishnah Chullin 10:4', 'from the lower knee joint to the thigh bone\'s protrusion'); return out('the lower knee joint to the thigh bone\'s protrusion (Mishnah Chullin 10:4)', ['due_to_priest'])
    if ask == 'ram_eaten_by':
        move('Zevachim 55a:6', 'the foreleg the priest\'s; the rest the owner\'s'); return out('the owner; the foreleg the priest\'s', ['accepted'])
    if ask == 'asham':
        d = OF.dispatch('communal_shelamim_and_asham')                                                            # THE CALL
        move('CALLED cold_run_offerings.dispatch(communal_shelamim_and_asham) -> %s [IMPORT, live]' % sorted(d), 'Mishnah Zevachim 5:5: the nazirite\'s guilt-offering — north, two-that-are-four, male priests, a day and a night; eaten by the priests (Menachot 73a)')
        return out('north; two placements that are four; male priests within the curtains, a day and a night (Mishnah Zevachim 5:5)', ['due_to_priest'])
    if ask == 'permitted_after':
        s = data['nazir_permitted_after']['value']; dat('the row nazir_permitted_after = %s' % s); ink('6:20', '"and AFTER THAT the nazirite may drink wine"')
        return out('after one offering (the Rabbis; R. Shimon); R. Eliezer after all', ['nazirite_term_fulfilled'])
    if ask == 'after_term_before_offerings':
        ink('6:6', '"ALL the days"'); move('Nazir 14b:9-15a:1 (the baraita)', 'flogged for impurity, shaving and wine alike'); return out('lashes for impurity, shaving and wine alike (the baraita)', ['lashes'])
    if ask == 'waving_indispensable':
        move('Nazir 46b:1 (Tosefta 1:5) / Menachot 19a:12 (Rav)', 'with or without palms — not indispensable; Rav: yes'); return out('not (the Tosefta: with or without palms); Rav: yes', ['accepted'])
    if ask == 'vow_on_vow':
        move('Nedarim 18a:3; Nazir 5a:19', 'nazir lehazzir — naziriteship on a prior naziriteship'); return out('takes effect (two terms)', ['nazirite_vow_bound'])
    if ask == 'chained_vows':
        move('Mishnah Nazir 4:1', '"and I", "and I" — all; the first dissolved, all; the last, he alone'); return out('all dissolved' if case.get('which_dissolved') == 'first' else 'the last alone', ['exempt'])
    if ask == 'spouse_and_i':
        move('Mishnah Nazir 4:1-2', 'his vow then hers — he nullifies hers; hers then his — he cannot (his own would fall)'); return out('he nullifies hers, his stands' if case.get('who_first') == 'husband' else 'he cannot nullify (his own would fall)', ['nazirite_vow_bound'])
    if ask == 'husband_annuls_after':
        stage = case['stage']
        move('Mishnah Nazir 4:5', 'after the blood of one offering — cannot (R. Akiva: after any slaughter); at the impurity shaving — can (a downcast wife); R. Meir even at purity')
        return out('cannot (R. Akiva: after any slaughter)' if stage == 'blood_sprinkled_purity' else 'can — a downcast wife', ['nazirite_vow_bound'] if stage == 'blood_sprinkled_purity' else ['exempt'])
    if ask == 'nullified_unknown':
        move('Mishnah Nazir 4:3', 'no lashes (R. Yehuda: lashes of rebellion)'); return out('no lashes (R. Yehuda: lashes of rebellion)', ['exempt'])
    if ask in ('nullified_after_separation', 'died_with_funds'):
        whose, allocated = case.get('whose', 'hers'), case.get('allocated')
        move('Mishnah Nazir 4:4; Mishnah Meilah 3:2; Meilah 11a:7', 'his animal grazes; hers: the sin dies, the burnt offered, the peace eaten a day without loaves; unallocated funds — gifts; allocated — the sin\'s to the Dead Sea, the burnt\'s an olah (misuse), the peace\'s a shelamim a day without loaves')
        if whose == 'his':
            return out('grazes', ['exempt'])
        if allocated is None:
            return out('the sin-offering dies, the burnt offered, the peace eaten a day without loaves', ['accepted'])
        return out('the sin\'s to the Dead Sea, the burnt\'s an olah (misuse), the peace\'s a shelamim a day without loaves' if allocated else 'communal gifts', ['accepted'])
    if ask == 'father_vows_son':
        move('Mishnah Nazir 4:6; Mishnah Sotah 3:8', 'a father may (not a mother); the son\'s or relatives\' objection cancels'); return out('a father may (not a mother); the son\'s or relatives\' objection cancels', ['nazirite_vow_bound'])
    if ask == 'shaves_on_fathers_funds':
        move('Mishnah Nazir 4:7', 'only a son who was a nazirite in his father\'s lifetime (R. Yosei: vowed after — gifts)'); return out('may (vowed in his father\'s lifetime)' if case.get('when_vowed') == 'in_lifetime' else 'communal gifts (R. Yosei)', ['accepted'])
    if ask == 'designated_by_others':
        ink('6:21', '"beside that for which his means suffice"'); move('Temurah 10a:5', 'designation by others effective'); return out('effective (6:21 his means)', ['accepted'])
    if ask == 'dissolved_by_sage':
        move('Mishnah Nazir 5:3', 'released — the animal grazes; not — counts from the vow'); return out('the animal grazes' if case.get('released') else 'counts from the vow', ['exempt'] if case.get('released') else ['nazirite_vow_bound'])
    if ask == 'vow_in_error':
        move('Mishnah Nazir 5:4', 'vowed then stolen — a nazirite; stolen then vowed — not (Nachum the Mede\'s error)'); return out('a nazirite (the event after the vow)' if case.get('event_before') is False else 'not — an error from the outset (Nachum the Mede)', ['nazirite_vow_bound'] if case.get('event_before') is False else ['exempt'])
    if ask == 'conditioned_on_birth':
        form, born = case['form'], case['born']
        move('Mishnah Nazir 2:7-8', '"a son" — a daughter or tumtum not; "a child" — any; a miscarriage not (R. Shimon\'s condition)')
        if born == 'miscarriage':
            return out('not (R. Shimon\'s condition)', ['exempt'])
        return out('a nazirite' if (form == 'child' or born == 'son') else 'not', ['nazirite_vow_bound'] if (form == 'child' or born == 'son') else ['exempt'])
    if ask == 'two_terms_order':
        move('Mishnah Nazir 2:9-10', 'his own first then the son\'s; reversed — the son\'s interrupts; a hundred days: born within seventy — nothing lost, after — the seventy negated'); return out('born within seventy days — nothing lost; after — the seventy negated' if case.get('born_on_day', 0) > 70 else 'born within seventy days — nothing lost', ['nazirite_vow_bound'])
    if ask == 'doubtful_vow':
        c = case.get('case', 'turned_back')
        move('Mishnah Nazir 5:6-7; Mishnah Tahorot 4:7, 4:12', 'the man turned back — none (lenient; R. Shimon\'s condition); the koy — all bound')
        return out('all bound (the koy)' if c == 'koy' else 'none (lenient; R. Shimon\'s condition)', ['nazirite_vow_bound'] if c == 'koy' else ['exempt'])
    if ask == 'two_doubtful':
        move('Mishnah Nazir 8:1', 'ben Zoma\'s procedure (the Rabbis agreed)'); return out('ben Zoma\'s procedure (the Rabbis)', ['accepted'])
    if ask == 'doubtful_leper':
        move('Mishnah Nazir 8:2; Nazir 60a:6', 'sixty days to sacred food, a hundred and twenty to wine and the dead'); return out('sixty days to sacred food, a hundred and twenty to wine and the dead', ['nazirite_vow_bound'])
    if ask == 'leper_nazirite_shaves':
        z = MZ.shave('nazirite')['v']                                                                              # THE CALL
        move('CALLED cold_run_metzora.shave(nazirite) -> %s [IMPORT, live]' % z, 'Lev 14:9 "his head" — the leper\'s positive command overrides 6:5\'s razor (Nazir 41a, 58a; Yevamot 5a)')
        return out('shaves with a razor — the leper\'s command overrides (metzora: %s)' % z, ['accepted'])
    if ask == 'oath_on_seed':
        move('Shevuot 22b:8 (Rav Ashi)', 'any amount or an olive\'s bulk — an open dilemma'); return out('an open dilemma (Rav Ashi)', [FX.NONE])
    if ask == 'sinner':
        ink('6:11', '"and atone for him for sinning by the soul"'); move('Bava Kamma 91b; Nazir 19a; Taanit 11a; Nedarim 10a', 'HaKappar: a sinner; R. Elazar: holy'); return out('a sinner (HaKappar) / holy (R. Elazar) — a dispute', ['accepted'])
    if ask == 'exemptions':
        move('Mishnah Nazir 6:5', 'the vine none; impurity and shaving: the met mitzvah, the leper\'s shaving'); return out('the vine none; impurity and shaving: the met mitzvah, the leper\'s shaving', ['accepted'])
    if ask == 'impure_after_first_blood':
        move('Mishnah Nazir 6:11', 'R. Eliezer negates all; the Rabbis: brings the rest (Miriam of Tarmod)'); return out('brings the rest and is pure (the Rabbis); R. Eliezer negates all', ['accepted'])
    if ask == 'shaved_on_invalid':
        move('Mishnah Nazir 6:10', 'the offering invalid — the shaving invalid; R. Shimon: that one alone fails; all three with one valid — the shaving valid'); return out('the shaving invalid (R. Shimon: that one alone fails); one of three valid — valid', ['disqualified'])
    if ask == 'vowed_abroad':
        move('Mishnah Nazir 3:6', 'Shammai thirty more; Hillel all again (Queen Helene)'); return out('Hillel: all again (Shammai: thirty)', ['nazirite_vow_bound'])
    return out('no verdict in span', [FX.NONE])


# ===== F6: THE PRIESTS' BLESSING (Num 6:22-27) ==============================================================
def blessing(case, data):
    del P[:]
    ask = case['ask']
    if ask == 'form':
        place = case['place']
        ink('6:23', '"THUS shall you bless the children of Israel; SAY to them"')
        move('Mishnah Sotah 7:6; Mishnah Tamid 7:2; Sotah 38a; Sifrei 39:1', 'in the Temple one blessing, the Name as written, the hands above the head (the High Priest not above the frontplate; R. Yehuda even he); in the province three with amen, the substitute, the hands at the shoulders')
        if place == 'temple':
            return out('one blessing; the Name as written; the hands above the head (the High Priest not above the frontplate)', ['blessed_by_the_priests'])
        return out('three blessings with amen; the substitute name; the hands at the shoulders', ['blessed_by_the_priests'])
    if ask == 'language':
        move('Sotah 33b:3 (R. Yehuda: "so"); 38a:2 (bless/bless with Deut 27:12)', 'the holy tongue'); return out('the holy tongue (so/so)', ['blessed_by_the_priests'])
    if ask == 'who_blesses':
        who = case['who']
        if who == 'priest':
            return out('blesses', ['blessed_by_the_priests'])
        if who == 'blemished_hands':
            b = PR.blemish('blemish_tokens')['v']                                                                     # THE CALL
            move('CALLED cold_run_priesthood.blemish(blemish_tokens) -> %s [IMPORT, live]' % b, 'the priesthood\'s blemish file; Mishnah Megillah 4:7: blemished hands — the people would look')
            return out('does not lift his hands (Megillah 4:7)', ['disqualified'])
        if who == 'drunk':
            move('Taanit 26b:16 (bar Kappara)', 'the blessing juxtaposed to the nazirite — a drunk priest may not bless'); return out('may not (the nazirite\'s juxtaposition)', ['disqualified'])
        if who in ('minor', 'exposed'):
            move('Mishnah Megillah 4:6', 'a minor does not lift his hands; the exposed not'); return out('not', ['disqualified'])
        if who == 'non_priest':
            return out('not — the priests bless', ['exempt'])
        return out('no verdict in span', [FX.NONE])
    if ask == 'quorum':
        move('Mishnah Megillah 4:3', 'not with fewer than ten'); return out('ten', ['blessed_by_the_priests'])
    if ask == 'who_is_blessed':
        ink('6:23', '"say to them"'); move('Sotah 38a:12', 'converts, women, freed slaves included'); return out('all Israel — converts, women, freed slaves', ['blessed_by_the_priests'])
    if ask == 'translated':
        move('Mishnah Megillah 4:10; Megillah 25a-b', 'read, not translated — lest "lift His face" be heard as favoritism'); return out('read, not translated', ['blessed_by_the_priests'])
    if ask == 'three_commands':
        move('Sotah 38b:4; Menachot 44a:18', 'a priest who does not ascend violates three'); return out('so you shall bless; say to them; put My name', ['blessed_by_the_priests'])
    if ask == 'priests_blessed':
        ink('6:27', '"and I will bless THEM"'); move('Chullin 49a:16 (R. Yishmael)', 'the priests bless Israel, the Holy One blesses the priests'); return out('by Heaven (I will bless them)', ['blessed_by_the_priests'])
    if ask == 'face_lifted':
        s = data['face_lifted']['value']; dat('the row face_lifted = %s: %s' % (s, data['face_lifted']['settings'][s]))
        return out('when they do His will (the Sifrei) / beyond the letter (Berakhot 20b) / before the sentence (Niddah 70b) — three reconciliations', ['blessed_by_the_priests'])
    if ask == 'counts':
        ink('6:24-26', 'words %s, letters %s — computed on the ink; the Name thrice' % (BLESS_WORDS, BLESS_LETTERS))
        return out('3, 5, 7 words; 15, 20, 25 letters; the Name thrice', ['blessed_by_the_priests'])
    if ask == 'name':
        s = data['blessing_name_by_place']['value']; dat('the row blessing_name_by_place = %s' % s); ink('6:27', '"they shall put MY NAME"')
        return out('the Name in the Temple, the substitute in the province', ['blessed_by_the_priests'])
    if ask == 'four_times':
        move('Taanit 26b', 'the four daily times of the blessing'); return out('the four daily times (Taanit 26b)', ['blessed_by_the_priests'])
    return out('no verdict in span', [FX.NONE])


# ===== F7: THE WAGONS (Num 7:1-9) ===========================================================================
def wagons(case, data):
    del P[:]
    ask = case['ask']
    if ask == 'day':
        ink('7:1', '"on the day Moses finished setting up the tabernacle" — Exod 40:33\'s finishing; the erection\'s day'); move('Sifrei 44:1; Shabbat 87b; Zevachim 101b:6', 'the day-stack of the first of Nisan — RETROGRADE after 1:1')
        return out('the erection\'s day — the day-stack (Sifrei 44:1; Shabbat 87b): RETROGRADE', ['wagons_brought'])
    if ask == 'numbers':
        ink('7:3', '"six covered wagons and twelve oxen, a wagon for two princes and an ox for one" — the parser: %s' % WAGONS)
        return out('6 wagons, 12 oxen; a wagon for two princes, an ox for one (the parser: [6, 12, 2, 1])', ['wagons_brought'])
    if ask == 'covered':
        move('Sifrei 45:1 (Rebbi); Onkelos 7:3', '"covered" — the translation\'s word'); return out('covered (Rebbi — Onkelos)', ['wagons_brought'])
    if ask == 'accepted':
        ink('7:4-5', '"take from them"'); move('Sifrei 45:1', 'not accepted until told'); return out('not accepted until told (7:4-5)', ['commanded'])
    if ask == 'distribution':
        ink('7:7-9', 'Gershon %s, Merari %s, Kohath none' % (DIST_G, DIST_M)); s = data['wagons_distribution']['value']; dat('the row wagons_distribution = %s' % s)
        return out('as Moses saw fit: Gershon 2 and 4, Merari 4 and 8, Kohath none — on the shoulder', ['wagons_assigned'])
    if ask == 'shoulder':
        ink('7:9', '"the service of the holy is upon them — on the shoulder they carry"'); move('Sifrei 46:2; Sotah 35a:22; Arakhin 11a:19', 'David\'s error and return; "they carry" as song')
        return out('David\'s error and return (the flow reversed); the song from "they carry"', ['wagons_assigned'])
    if ask == 'anointing':
        o = IS.oil('holy_anointing_oil')['v']                                                                       # THE CALL
        s = data['anointing_scope']['value']; dat('the row anointing_scope = %s: %s' % (s, data['anointing_scope']['settings'][s]))
        ink('7:1', '"he anointed it and sanctified it and all its vessels, the altar and all its vessels; he anointed THEM and sanctified them"')
        move('CALLED cold_run_incense_shekel.oil(holy_anointing_oil) -> %r [IMPORT, live]' % (o,), 'Exod 30:22-33\'s oil; "them" — Moses\' vessels by anointing, the generations\' by service (Sanhedrin 16b; Shevuot 15a); Horayot 12a: anointed, not poured')
        return out('Moses\' vessels by anointing (the liquid measures in and out, the dry inside — R. Yoshiya); the generations\' by service', ['wagons_brought'])
    return out('no verdict in span', [FX.NONE])


# ===== F8: THE DEDICATION (Num 7:10-88) =====================================================================
def dedication(case, data):
    del P[:]
    ask = case['ask']
    if ask == 'first_day':
        ink('7:10', '"on the day it was anointed"'); move('Zevachim 101b:6', 'three goats on one day — Nahshon\'s, the eighth day\'s, the New Moon\'s: the first of Nisan'); return out('the anointing day = the erection = 1 Nisan: three goats on one day (Zevachim 101b)', ['dedication_brought'])
    if ask == 'order':
        ink('7:12-83', 'the twelve by day: %s = the camp\'s 2:3-31 (computed)' % ORDER_7); s = data['princes_order']['value']; dat('the row princes_order = %s' % s); move('Sifrei 47:1, 52:1', 'by the journeying, not by birth; Reuben\'s protest, Moses\' rebuke')
        return out('by the journeying = the camp\'s order (computed = 2:3-31), not by birth; Reuben\'s protest', ['dedication_offered'])
    if ask == 'per_day':
        ink('7:11', '"one prince per day, one prince per day"'); ink('7:72, 7:78', '"on the DAY of the eleventh DAY" — the doubled day: %s' % DAY_TOKENS); move('Moed Katan 9a:11-12', 'one continuous period — the Sabbath overridden')
        return out('one prince per day — twelve dues from the anointing day, the Sabbath overridden (Moed Katan 9a)', ['dedication_offered'])
    if ask == 'same_day':
        ink('7:84, 7:88', '"on the day of its anointing" / "after it was anointed"'); move('Sifrei 53:1', 'the same day'); return out('7:84 = 7:88 — on the day of its anointing / after: the same day (Sifrei 53:1)', ['dedication_offered'])
    if ask == 'one_text':
        move('the reading (NS07A-05, computed)', 'the twelve blocks one text but the opening verb, the name, one spelling'); return out('the twelve blocks one text (computed at the reading)', ['dedication_offered'])
    if ask == 'dish':
        ink('7:13', '"one silver dish, a hundred and thirty its weight; one silver bowl, seventy shekels, by the shekel of the sanctuary" — %s' % DISH)
        move('CALLED cold_run_incense_shekel.shekel(twenty_gerah) -> %s [IMPORT, live]' % SHEKEL_SEATS, 'the sanctuary shekel = Exod 30:13\'s twenty gerah — the sela (Onkelos; Sifrei 49:1, 54:1)')
        return out('130 and 70 by the sanctuary shekel (Exod 30:13\'s twenty gerah — the sela)', ['accepted'])
    if ask == 'pan':
        ink('7:14', '"one pan, ten of gold, full of incense" — %s (M-26: the tevir on "one")' % PAN); ink('7:86', '"all the gold of the pans, a hundred and twenty" = 12 x 10 — %s' % TOTALS[86]); move('Sifrei 49:1, 55:1', 'gold weighed in silver shekels — the total decides')
        return out('ten of gold weighed in silver — 120 = 12 x 10 decides (M-26)', ['accepted'])
    if ask == 'full':
        ink('7:13', '"both of them FULL of fine flour"'); move('Menachot 8a:13; 88a:8', 'a full tenth sanctifies (R. Yosei: unless meant to add)'); return out('a full tenth sanctifies (R. Yosei: unless meant to add)', ['accepted'])
    if ask == 'bowls_sanctify_dry':
        move('Menachot 8b:5, 19b:6; Zevachim 88a:6 (Shmuel)', 'the bowls sanctify dry goods'); return out('yes (Shmuel)', ['accepted'])
    if ask == 'vessel_joins':
        s = data['vessel_joining']['value']; dat('the row vessel_joining = %s' % s); ink('7:14', '"full of incense"'); return out('Torah law (R. Chanin); R. Yochanan rabbinic', ['accepted'])
    if ask == 'animals':
        ink('7:15-17', '"one bull, one ram, one lamb of its first year for a burnt-offering; one goat for a sin-offering; two oxen, five rams, five he-goats, five lambs for peace-offerings" — %s' % BLOCK17); move('Sifrei 50:1-51:1', 'none like it in its herd; its own year')
        d = OF.dispatch('olah')                                                                                   # THE CALL
        move('CALLED cold_run_offerings.dispatch(olah) -> %s [IMPORT, live]' % sorted(d), 'the burnt-offering\'s procedure the offering engine\'s')
        return out('one bull, one ram, one lamb (burnt); one goat (sin); two oxen, five, five, five (peace) — none like it; its own year', ['accepted'])
    if ask == 'animal_age':
        m = case['months']; move('Mishnah Parah 1:3', 'lambs to a year, rams to two — day to day; thirteen months neither (a palgas)')
        return out('a lamb' if m <= 12 else ('neither (a palgas)' if m == 13 else 'a ram'), ['accepted'] if m != 13 else ['disqualified'])
    if ask == 'goat':
        ink('7:16', '"one he-goat for a sin-offering"'); move('Sifrei 51:1; Horayot 6a; Menachot 92b:7', 'for the grave of the depths; leaning — R. Yehuda yes, R. Shimon the idolatry goats'); return out('for the grave of the depths; leaning — R. Yehuda yes (R. Shimon the idolatry goats)', ['accepted'])
    if ask == 'exceptions':
        s = data['prince_exceptions']['value']; dat('the row prince_exceptions = %s: %s' % (s, data['prince_exceptions']['settings'][s]))
        return out('the Sabbath overridden; an individual\'s incense; a sin-offering not for a sin; one of each', ['accepted'])
    if ask == 'sabbath':
        move('Moed Katan 9a:11-12', 'the twelve days continuous — the Sabbath overridden'); return out('overridden — the days continuous (Moed Katan 9a)', ['accepted'])
    if ask == 'totals':
        ink('7:84-88', '%s' % TOTALS); return out('2400 = 12 x (130 + 70); 120 = 12 x 10; 12/12/12/12; 24/60/60/60 — computed', ['accepted'])
    if ask == 'credited':
        move('Sifrei 55:1-57:1', 'each credited with all twelve'); return out('each credited with all twelve (Sifrei 55:1-57:1)', ['accepted'])
    if ask == 'weights':
        move('Sifrei 54:1', 'Temple vessels weigh the same singly and together'); return out('Temple vessels weigh the same singly and together (54:1)', ['accepted'])
    return out('no verdict in span', [FX.NONE])


# ===== F9: THE VOICE (Num 7:89) =============================================================================
def voice(case, data):
    del P[:]
    ask = case['ask']
    if ask == 'reflexive':
        ink('7:89', '"he heard the Voice SPEAKING ITSELF [middabber] to him" — the hitpael by the points (the reading\'s NS07B-04); Onkelos both verbs reflexive')
        return out('the Voice speaking ITSELF (the hitpael by the points); Onkelos both verbs', ['spoken_to_from_the_ark'])
    if ask == 'third_verse':
        move('Sifrei 58:1 (I13 stated here)', 'Lev 1:1 "from the tent" against Exod 25:22 "from above the ark-cover" — 7:89 the third'); return out('Lev 1:1 against Exod 25:22 reconciled by 7:89 (I13)', ['spoken_to_from_the_ark'])
    if ask == 'exclusions':
        move('Sifrei 58:1', 'thirteen utterances to Moses and Aaron, thirteen exclusions of Aaron'); ink('the frame census', '"to Moses and to Aaron" at %d verses of Exodus-Numbers (computed)' % TO_MOSES_AND_AARON)
        return out('thirteen utterances to Moses and Aaron, thirteen exclusions — the frame census %d' % TO_MOSES_AND_AARON, ['spoken_to_from_the_ark'])
    if ask == 'who_heard':
        ink('7:89', '"speaking UNTO HIM"'); move('Yoma 4b:8', 'Moses alone at the Tent; at Sinai all heard'); return out('Moses alone at the Tent (Yoma 4b); all at Sinai', ['spoken_to_from_the_ark'])
    if ask == 'great_voice':
        move('Sifrei 58:2', 'THE voice — not low: Deut 5:19\'s great voice'); return out('not a low voice — the great voice of Sinai (58:2)', ['spoken_to_from_the_ark'])
    if ask == 'door':
        move('Yoma 4b; Sukkah 5a', 'the Voice at the door of the tent'); return out('the Voice at the door (Yoma 4b; Sukkah 5a)', ['spoken_to_from_the_ark'])
    return out('no verdict in span', [FX.NONE])


# ---- THE WRAP — the daemon, the scene, the narrative ------------------------------------------------------
PRINCE_TOKENS = ['nahshon-ben-amminadab', 'nethanel-ben-zuar', 'eliab-ben-helon', 'elizur-ben-shedeur', 'shelumiel-ben-zurishaddai', 'eliasaph-ben-deuel',
                 'elishama-ben-ammihud', 'gamaliel-ben-pedahzur', 'abidan-ben-gideoni', 'ahiezer-ben-ammishaddai', 'pagiel-ben-ochran', 'ahira-ben-enan']

def law_naso(event, world):
    """Num 4:21-7:89 (cold_run_naso.py F1-F9). installed_by boot — the standing setting for a law spoken at its verse."""
    k, src = event['kind'], event['case_source']
    E_ = lambda eff, s, cp=None, amount=None, due=None, law='', value=None: {'effect': eff, 'subject': s, 'counterparty': cp, 'amount': amount, 'due': due, 'value': value if value is not None else True, 'source_law': law, 'case_source': src}
    if k == 'gershon_service_commanded':
        return [E_('commanded', event['subject'], value='the_gershonites_count', law='F1 [INK 4:22-28 "lift the head of the sons of Gershon, them also" — the count and the soft load owed]')]
    if k == 'merari_service_commanded':
        return [E_('commanded', event['subject'], value='the_merarites_count', law='F1 [INK 4:29-33 "the sons of Merari... you shall count them" — the count and the hard load owed]')]
    if k == 'levites_work_counted':
        for val, note in (('the_kohathites_service', 'Num 4:34-37 — the sons of Kohath counted, by the mouth of the LORD by the hand of Moses'), ('the_gershonites_count', 'Num 4:38-41 — the sons of Gershon counted'), ('the_merarites_count', 'Num 4:42-45 — the sons of Merari counted')):
            world.close(event['subject'], 'commanded', note, value=val)
        return [E_('work_counted', event['subject'], value=event.get('total', WORK_TOTAL), law='F1 [INK 4:36, 4:40, 4:44, 4:48 — %s = %d; the three debits closed]' % (WORK, WORK_TOTAL))]
    if k == 'send_out_commanded':
        return [E_('commanded', event['subject'], value='the_send_out', law='F2 [INK 5:2-3 "send out of the camp every leper and every zav and everyone unclean by a corpse" — the send-out owed]')]
    if k == 'unclean_sent_out':
        world.close('israel', 'commanded', 'Num 5:4 — and the children of Israel did so, and sent them outside the camp', value='the_send_out')
        return [E_('sent_outside_the_camp', event['subject'], value='leper: all three camps; zav: two; corpse-unclean: one', law='F2 [INK 5:4; the ladder — Pesachim 67a; Sifrei 1:3-4]')]
    if k == 'wagons_brought':
        return [E_('wagons_brought', event['subject'], value='%d wagons, %d oxen' % (WAGONS[0], WAGONS[1]), law='F7 [INK 7:2-3 — six covered wagons and twelve oxen before the tabernacle]')]
    if k == 'wagons_accepted_commanded':
        return [E_('commanded', event['subject'], value='the_wagons_distribution', law='F7 [INK 7:4-5 "take from them... give them to the Levites" — the distribution owed]')]
    if k == 'wagons_assigned':
        world.close('moses', 'commanded', 'Num 7:6 — and Moses took the wagons and the oxen and gave them to the Levites', value='the_wagons_distribution')
        return [E_('wagons_assigned', event['subject'], cp='moses', value='gershon 2/4, merari 4/8, kohath none', law='F7 [INK 7:6-9 — as Moses saw fit; Kohath on the shoulder]')]
    if k == 'dedication_brought':
        return [E_('dedication_brought', event['subject'], value='the_dedication', law='F8 [INK 7:10 "the princes brought near the dedication of the altar on the day it was anointed" — to be offered by days]')]
    if k == 'dedication_order_commanded':
        day = event.get('day', world.clock.day)      # THE SEQUENTIAL RUN: the event's own day (the text's date inside the retrograde stretch — the anointing day)
        return [E_('dedication_offered', tok, due=day + n, value='day %d: %s — the dish %d, the bowl %d, the pan %d of gold; the animals %s' % (n + 1, NAMES[n], DISH[1], DISH[3], PAN[1], BLOCK17),
                   law='F8 [INK 7:11 "one prince per day"; 7:%d — the %s day; the due the anointing day + %d (Moed Katan 9a: continuous)]' % (12 + 6 * n, ['first', 'second', 'third', 'fourth', 'fifth', 'sixth', 'seventh', 'eighth', 'ninth', 'tenth', 'eleventh', 'twelfth'][n], n))
                for n, tok in enumerate(PRINCE_TOKENS)]
    if k == 'voice_heard_from_the_ark':
        return [E_('spoken_to_from_the_ark', event['subject'], value='the Voice speaking itself, from between the two cherubim', law='F9 [INK 7:89 — the reflexive by the points; Yoma 4b: Moses alone]')]
    # ---- the exam's case kinds: each names LITERALLY every effect it can write (the daemon gate parses the names; an effect a cell
    #      returns that the daemon did not name is a KeyError — a miss to read, never a silent write) ----
    if k == 'send_out_case':
        v, e, _ = camp_purity({'ask': 'ladder', 'who': event['who']} if event.get('camp_entered') is None else {'ask': 'entered_impure'}, DATA)
        L = 'F2 [%s]' % v
        W = {'sent_outside_the_camp': E_('sent_outside_the_camp', event['person'], value=v, law=L), 'exempt': E_('exempt', event['person'], value=v, law=L), 'lashes': E_('lashes', event['person'], value=v, law=L)}
        return [W[x] for x in e if x != FX.NONE]
    if k == 'theft_confessed_case':
        v, e, _ = restitution({'ask': event['ask'], 'value': event.get('value', 100), 'swore_on_fifth': event.get('swore_on_fifth', False)}, DATA)
        cp = 'the-priest' if event['ask'] == 'proselyte_dead' else event.get('victim'); L = 'F3 [%s]' % v
        W = {'guilt_acknowledged': E_('guilt_acknowledged', event['person'], cp=cp, value=v, law=L), 'pays': E_('pays', event['person'], cp=cp, amount=event.get('value'), value=v, law=L),
             'adds_fifth': E_('adds_fifth', event['person'], cp=cp, value=v, law=L), 'due_to_priest': E_('due_to_priest', event['person'], cp=cp, value=v, law=L), 'exempt': E_('exempt', event['person'], cp=cp, value=v, law=L)}
        return [W[x] for x in e if x != FX.NONE]
    if k == 'gifts_case':
        v, e, _ = restitution({'ask': event['ask'], 'age_days': event.get('age_days', 31)}, DATA)
        L = 'F3 [%s]' % v
        W = {'due_to_priest': E_('due_to_priest', event['person'], cp='the-priest', value=v, law=L), 'exempt': E_('exempt', event['person'], cp='the-priest', value=v, law=L),
             'pays': E_('pays', event['person'], cp='the-priest', amount=BM.RATE, value=v, law=L)}   # the firstborn's five shekels after thirty days (Bamidbar's RATE) — the literal form's first catch: the first run raised KeyError 'pays'
        return [W[x] for x in e if x != FX.NONE]
    if k == 'sotah_case':
        v, e, _ = sotah({'ask': event['ask'], 'who': event.get('who'), 'what': event.get('what'), 'clean': event.get('clean', True), 'guilty': event.get('guilty'), 'merit': event.get('merit'), 'when': event.get('when'), 'for': event.get('for'), 'against': event.get('against'), 'case': event.get('case')}, DATA)
        L = 'F4 [%s]' % v; s_ = event['person']
        W = {'tested_by_the_waters': E_('tested_by_the_waters', s_, value=v, law=L), 'forbidden_to_her_husband': E_('forbidden_to_her_husband', s_, value=v, law=L), 'ketubah_forfeited': E_('ketubah_forfeited', s_, value=v, law=L),
             'exempt': E_('exempt', s_, value=v, law=L), 'disqualified': E_('disqualified', s_, value=v, law=L), 'accepted': E_('accepted', s_, value=v, law=L), 'put_to_death': E_('put_to_death', s_, cp='HEAVEN', value=v, law=L)}
        return [W[x] for x in e if x != FX.NONE]
    if k == 'nazirite_case':
        a = event['ask']
        if a == 'vow':
            term = event.get('term', DATA['nazir_default_days']['value'])
            day = event.get('day', world.clock.day)
            return [E_('nazirite_vow_bound', event['person'], value='term %d days' % term, law='F5 [INK 6:2-8; the row nazir_default_days]'),
                    E_('nazirite_term_fulfilled', event['person'], due=day + term, value='the days of his separation fulfilled', law='F5 [INK 6:13 — the term\'s due: the timer]')]
        if a == 'defiled':
            world.cancel_timers(event['person'], 'nazirite_term_fulfilled', 'Num 6:9-12 — a corpse beside him: the former days fall')
            v, e, _ = nazirite({'ask': 'defiled'}, DATA)
            day = event.get('day', world.clock.day); term = event.get('term', DATA['nazir_default_days']['value'])
            return [E_('count_voided', event['person'], value=v, law='F5 [%s]' % v),
                    E_('nazirite_term_fulfilled', event['person'], due=day + 8 + term, value='the recount from the eighth day (the row nazir_recount_day)', law='F5 [INK 6:11-12 — sanctify his head that day; the former days fall: the timer re-set]')]
        v, e, _ = nazirite({'ask': a, 'form': event.get('form'), 'who': event.get('who'), 'age': event.get('age'), 'product': event.get('product'), 'amount': event.get('amount'), 'means': event.get('means'), 'source': event.get('source'), 'mode': event.get('mode'), 'act': event.get('act'), 'day': event.get('day_of_term'), 'term': event.get('term'), 'warnings': event.get('warnings', 0), 'which': event.get('which'), 'where': event.get('where'), 'stage': event.get('stage'), 'case': event.get('case')}, DATA)
        L = 'F5 [%s]' % v; s_ = event['person']
        W = {'count_voided': E_('count_voided', s_, value=v, law=L), 'lashes': E_('lashes', s_, value=v, law=L), 'exempt': E_('exempt', s_, value=v, law=L), 'disqualified': E_('disqualified', s_, value=v, law=L),
             'accepted': E_('accepted', s_, value=v, law=L), 'due_to_priest': E_('due_to_priest', s_, cp='the-priest', value=v, law=L), 'released': E_('released', s_, value=v, law=L)}
        return [W[x] for x in e if x != FX.NONE]
    if k == 'blessing_case':
        v, e, _ = blessing({'ask': event['ask'], 'who': event.get('who'), 'place': event.get('place')}, DATA)
        L = 'F6 [%s]' % v; s_ = event['person']
        W = {'blessed_by_the_priests': E_('blessed_by_the_priests', s_, value=v, law=L), 'exempt': E_('exempt', s_, value=v, law=L), 'disqualified': E_('disqualified', s_, value=v, law=L)}
        return [W[x] for x in e if x != FX.NONE]
    if k == 'dedication_case':
        v, e, _ = dedication({'ask': event['ask'], 'months': event.get('age_months', 12)}, DATA)
        L = 'F8 [%s]' % v; s_ = event['person']
        W = {'accepted': E_('accepted', s_, value=v, law=L), 'disqualified': E_('disqualified', s_, value=v, law=L)}
        return [W[x] for x in e if x != FX.NONE]
    if k == 'work_count_case':
        v, e, _ = work_count({'ask': event['ask'], 'who': event.get('who', 'levite'), 'age': event.get('age', 40), 'carrying': event.get('carrying', True)}, DATA)
        L = 'F1 [%s]' % v; s_ = event['person']
        W = {'appointed_to_serve': E_('appointed_to_serve', s_, value=v, law=L), 'exempt': E_('exempt', s_, value=v, law=L), 'charge_kept': E_('charge_kept', s_, value=v, law=L)}
        return [W[x] for x in e if x != FX.NONE]
    return []


def scene():
    """THE SCENE — the exam's rows replayed on the world engine (the exodus epoch): the nazirite's term as a TIMER (set, cancelled by a
    defilement, re-set from the eighth day), the sotah's outcomes, the send-out's ladder, the theft's algebra, the blessing's who, the
    dedication's exceptions, the work-count's ages."""
    with contextlib.redirect_stdout(io.StringIO()):
        w = WE.World(era='Num 4:21-7:89: Mishnah Sotah, Nazir, Bava Kamma 9, Megillah 4, Kelim 1, Makkot 3 and the Talmud\'s rows on the engine (the exodus epoch)', epoch='exodus')
        w.laws = [law_naso]
        w.advance(w.clock.day_in('exodus', 2, 2, 1))
        w.submit({'kind': 'send_out_case', 'subject': 'the-leper-at-the-gate', 'person': 'the-leper-at-the-gate', 'who': 'leper', 'case_source': 'Num 5:2; Pesachim 67a:11 — the leper out of all three camps'})
        w.submit({'kind': 'send_out_case', 'subject': 'the-zav-at-the-mount', 'person': 'the-zav-at-the-mount', 'who': 'zav', 'case_source': 'Num 5:2; Pesachim 67a:12 — the zav out of two'})
        w.submit({'kind': 'send_out_case', 'subject': 'the-mourner-at-the-court', 'person': 'the-mourner-at-the-court', 'who': 'corpse_unclean', 'case_source': 'Num 5:2; Zevachim 117a — the corpse-unclean out of one'})
        w.submit({'kind': 'send_out_case', 'subject': 'the-impure-who-entered', 'person': 'the-impure-who-entered', 'who': 'zav', 'camp_entered': 'the_courtyard', 'case_source': 'Num 5:3; Makkot 14b:6; Mishnah Makkot 3:2 — the impure who entered the Temple'})
        w.submit({'kind': 'theft_confessed_case', 'subject': 'the-robber-of-the-proselyte', 'person': 'the-robber-of-the-proselyte', 'ask': 'proselyte_dead', 'value': 100, 'case_source': 'Num 5:8; Mishnah Bava Kamma 9:11 — the proselyte dead without heirs'})
        w.submit({'kind': 'theft_confessed_case', 'subject': 'the-robber-who-swore', 'person': 'the-robber-who-swore', 'ask': 'algebra', 'value': 100, 'victim': 'the-victim', 'case_source': 'Num 5:7; Lev 5:24 — the principal and the fifth (Lev 5\'s cell called)'})
        w.submit({'kind': 'theft_confessed_case', 'subject': 'the-son-who-robbed-his-father', 'person': 'the-son-who-robbed-his-father', 'ask': 'robbed_father', 'value': 100, 'victim': 'the-heirs', 'case_source': 'Num 5:7; Mishnah Bava Kamma 9:9 — robbed his father'})
        w.submit({'kind': 'gifts_case', 'subject': 'the-father-of-a-firstborn', 'person': 'the-father-of-a-firstborn', 'ask': 'firstborn_thirty', 'age_days': 31, 'case_source': 'Num 5:9-10; Sifrei 6:1; Bekhorot 49a — the firstborn\'s thirty days (Bamidbar called)'})
        w.submit({'kind': 'sotah_case', 'subject': 'the-guilty-wife', 'person': 'the-guilty-wife', 'ask': 'outcome', 'guilty': True, 'case_source': 'Num 5:27; Mishnah Sotah 3:4 — the guilty one drinks'})
        w.submit({'kind': 'sotah_case', 'subject': 'the-innocent-wife', 'person': 'the-innocent-wife', 'ask': 'outcome', 'guilty': False, 'case_source': 'Num 5:28 — cleared and sown with seed'})
        w.submit({'kind': 'sotah_case', 'subject': 'the-betrothed-warned', 'person': 'the-betrothed-warned', 'ask': 'status', 'who': 'betrothed', 'case_source': 'Num 5:29; Mishnah Sotah 4:1 — the betrothed neither drinks nor collects'})
        w.submit({'kind': 'sotah_case', 'subject': 'the-wife-with-witnesses-overseas', 'person': 'the-wife-with-witnesses-overseas', 'ask': 'witnesses_overseas', 'case_source': 'Num 5:13; Sotah 6a:10 — witnesses overseas'})
        w.submit({'kind': 'sotah_case', 'subject': 'the-wife-who-refused-late', 'person': 'the-wife-who-refused-late', 'ask': 'refuses', 'when': 'after_erasure', 'case_source': 'Num 5:27; Mishnah Sotah 3:3 — forced after the erasure'})
        w.submit({'kind': 'sotah_case', 'subject': 'the-wife-of-an-unclean-husband', 'person': 'the-wife-of-an-unclean-husband', 'ask': 'husband_clean', 'clean': False, 'case_source': 'Num 5:31; Kiddushin 27b:9 — the man not clear of iniquity'})
        d0 = w.clock.day
        w.submit({'kind': 'nazirite_case', 'subject': 'the-thirty-day-nazirite', 'person': 'the-thirty-day-nazirite', 'ask': 'vow', 'term': 30, 'case_source': 'Num 6:2; Mishnah Nazir 1:3, 3:1 — an unspecified naziriteship: thirty days'})
        w.submit({'kind': 'nazirite_case', 'subject': 'the-nazirite-defiled', 'person': 'the-nazirite-defiled', 'ask': 'vow', 'term': 30, 'case_source': 'Num 6:2 — a second nazirite, to be defiled on his twentieth day'})
        w.submit({'kind': 'nazirite_case', 'subject': 'the-nazirite-who-drank', 'person': 'the-nazirite-who-drank', 'ask': 'ate', 'product': 'wine', 'amount': 'quarter_log', 'case_source': 'Num 6:3; Mishnah Nazir 6:1 — a quarter-log of wine'})
        w.submit({'kind': 'nazirite_case', 'subject': 'the-nazirite-at-the-unburied', 'person': 'the-nazirite-at-the-unburied', 'ask': 'impurity_for', 'who': 'met_mitzvah', 'case_source': 'Num 6:7; Nazir 48a — the met mitzvah'})
        w.submit({'kind': 'nazirite_case', 'subject': 'the-leper-nazirite', 'person': 'the-leper-nazirite', 'ask': 'leper_nazirite_shaves', 'case_source': 'Num 6:5; Lev 14:9; Nazir 41a — the leper-nazirite shaves (the metzora engine called)'})
        w.submit({'kind': 'nazirite_case', 'subject': 'the-nazirite-completing', 'person': 'the-nazirite-completing', 'ask': 'foreleg', 'case_source': 'Num 6:19-20; Mishnah Nazir 6:9 — the foreleg on his palms (Tzav\'s cell called)'})
        w.advance(d0 + 20)
        w.submit({'kind': 'nazirite_case', 'subject': 'the-nazirite-defiled', 'person': 'the-nazirite-defiled', 'ask': 'defiled', 'term': 30, 'case_source': 'Num 6:9-12; Mishnah Nazir 6:6 — defiled on the twentieth day: the former days fall; the recount from the eighth'})
        w.advance(d0 + 31)
        fired_first = len([l for l in w.log if l[0] == 'TIMER-FIRE'])
        w.advance(d0 + 20 + 8 + 30)
        w.submit({'kind': 'blessing_case', 'subject': 'the-priest-with-blemished-hands', 'person': 'the-priest-with-blemished-hands', 'ask': 'who_blesses', 'who': 'blemished_hands', 'case_source': 'Num 6:23; Mishnah Megillah 4:7 — blemished hands (the priesthood\'s cell called)'})
        w.submit({'kind': 'blessing_case', 'subject': 'the-drunk-priest', 'person': 'the-drunk-priest', 'ask': 'who_blesses', 'who': 'drunk', 'case_source': 'Num 6:23; Taanit 26b:16 — the drunk priest'})
        w.submit({'kind': 'blessing_case', 'subject': 'the-priests-in-the-province', 'person': 'the-priests-in-the-province', 'ask': 'form', 'place': 'province', 'case_source': 'Num 6:23-27; Mishnah Sotah 7:6 — the blessing in the province'})
        w.submit({'kind': 'dedication_case', 'subject': 'the-princes-sabbath', 'person': 'the-princes-sabbath', 'ask': 'sabbath', 'case_source': 'Num 7:72, 7:78; Moed Katan 9a — the Sabbath overridden'})
        w.submit({'kind': 'dedication_case', 'subject': 'the-palgas-offered', 'person': 'the-palgas-offered', 'ask': 'animal_age', 'age_months': 13, 'case_source': 'Num 7:15; Mishnah Parah 1:3 — thirteen months: neither'})
        w.submit({'kind': 'work_count_case', 'subject': 'the-apprentice-levite', 'person': 'the-apprentice-levite', 'ask': 'fitness', 'who': 'levite', 'age': 27, 'carrying': True, 'case_source': 'Num 4:47; Chullin 24a:12 — twenty-seven: an apprentice (Bamidbar called)'})
        w.submit({'kind': 'work_count_case', 'subject': 'the-old-levite-at-shiloh', 'person': 'the-old-levite-at-shiloh', 'ask': 'fitness', 'who': 'levite', 'age': 55, 'carrying': False, 'case_source': 'Num 4:47; Chullin 24a:11 — not carrying: fit (Bamidbar called)'})
    n = lambda eid, eff: len([e for e in w.entity(eid).ledger if e['effect'] == eff])
    val = lambda eid, eff: [e.get('value') for e in w.entity(eid).ledger if e['effect'] == eff]
    L = lambda k: len([l for l in w.log if l[0] == k])
    return (val('the-leper-at-the-gate', 'sent_outside_the_camp'), val('the-zav-at-the-mount', 'sent_outside_the_camp'), val('the-mourner-at-the-court', 'sent_outside_the_camp'), n('the-impure-who-entered', 'lashes'),
            n('the-robber-of-the-proselyte', 'due_to_priest'), val('the-robber-who-swore', 'pays'), n('the-son-who-robbed-his-father', 'adds_fifth'), val('the-father-of-a-firstborn', 'pays'),
            n('the-guilty-wife', 'put_to_death'), n('the-innocent-wife', 'accepted'), n('the-betrothed-warned', 'ketubah_forfeited'), n('the-wife-with-witnesses-overseas', 'exempt'), n('the-wife-who-refused-late', 'tested_by_the_waters'), n('the-wife-of-an-unclean-husband', 'exempt'),
            n('the-thirty-day-nazirite', 'nazirite_term_fulfilled'), n('the-nazirite-defiled', 'count_voided'), n('the-nazirite-defiled', 'nazirite_term_fulfilled'), fired_first, L('TIMER-SET'), L('TIMER-CANCEL'), L('TIMER-FIRE'),
            n('the-nazirite-who-drank', 'lashes'), n('the-nazirite-at-the-unburied', 'count_voided'), n('the-leper-nazirite', 'accepted'), n('the-nazirite-completing', 'due_to_priest'),
            n('the-priest-with-blemished-hands', 'disqualified'), n('the-drunk-priest', 'disqualified'), n('the-priests-in-the-province', 'blessed_by_the_priests'), n('the-princes-sabbath', 'accepted'), n('the-palgas-offered', 'disqualified'),
            n('the-apprentice-levite', 'exempt'), n('the-old-levite-at-shiloh', 'appointed_to_serve'), len(w.entities)), w
SCENE, _W = scene()
SCENE_PREDICTED = (['out of all three camps (Israel, Levi, the Presence)'], ['out of two (Levi and the Presence)'], ['out of one (the Presence)'], 1,
                   1, ['pay its value; add the fifth (25.00); ram at the valuation floor'], 1, ['after thirty days'],
                   1, 1, 1, 1, 1, 1,
                   1, 1, 1, 1, 3, 1, 2,
                   1, 1, 1, 1,
                   1, 1, 1, 1, 1,
                   1, 1, 27)   # NUMBERS_WALK.md "Sitting 2b" + THE FIRST RUN'S PRINT: the ladder 3/2/1; the impure entrant's lashes; the proselyte's debt to the priest; the algebra; the son's fifth; the firstborn after thirty; the six sotah rows one effect each; THE TIMER — the thirty-day term fulfilled (fired at day 31: fired_first 1), the defiled one's count voided and its term re-fulfilled from the eighth (TIMER-SET 3 = two vows + the re-set, CANCEL 1, FIRE 2); the drinker's lashes, the met mitzvah's voiding, the leper-nazirite's shave accepted, the completing one's foreleg due; the two disqualified priests, the province blessed; the Sabbath's dedication accepted, the palgas disqualified; the apprentice exempt, the old Levite appointed; 27 entities
assert SCENE == SCENE_PREDICTED, ('THE NUMBERS WALK: Naso\'s scene moved from its prediction', SCENE, SCENE_PREDICTED)


def narrative():
    """THE NUMBERS WALK 2b (2026-09-10; NUMBERS_WALK.md "Sitting 2b"): the portion's own acts AS HISTORY — the eleven lines of Num 4:21-7:89 in
    the text's order on a world with this runner's daemon after Bamidbar's forward marker at 1:1 (2, 2, 1): the two counts commanded and the
    work-count (three closes — the third Bamidbar's Kohathite debit, absent on this bare world), the send-out commanded and run under the
    reading-placed retrograde marker at 5:1, the wagons and the dedication under 7:1's retrograde marker, THE SCHEDULE of 7:11 as twelve
    RETRO-WRITES, the Voice; recorded by the sequential run's recorder and stitched onto the tape (the fourteen markers the stitcher's rows).
    Not a graded cell: the tuple below is a tripwire typed from the first run's print; the sequence world's RUN tuple grades the tape."""
    with contextlib.redirect_stdout(io.StringIO()):
        w = WE.World(era='Num 4:21-7:89: Naso on the tape — the work-count, the send-out, the wagons, the dedication, the Voice (the exodus epoch)', epoch='exodus')
        w.laws = [law_naso]
        w.marker('Num 1:1', w.clock.day_in('exodus', 2, 2, 1), value='the census commanded (1:1) — Bamidbar\'s FORWARD marker, the context of every Naso date')
        w.submit({'kind': 'gershon_service_commanded', 'subject': 'the-levites', 'house': 'gershon', 'ages': [30, 50], 'burden': 'the soft: the curtains, the tent, its covering, the screens, the cords', 'under': 'ithamar', 'case_source': 'Num 4:21-28 — and the LORD spoke to Moses saying: lift the head of the sons of Gershon, them also... from thirty years old and upward until fifty... this is the service of the families of the Gershonites... in the hand of Ithamar'})
        w.submit({'kind': 'merari_service_commanded', 'subject': 'the-levites', 'house': 'merari', 'ages': [30, 50], 'burden': 'the hard: the frames, the bars, the pillars, the sockets, the pegs, the cords', 'by_names': True, 'under': 'ithamar', 'case_source': 'Num 4:29-33 — the sons of Merari by their families... you shall count them... and by names you shall appoint the vessels of the charge of their burden... in the hand of Ithamar'})
        w.submit({'kind': 'levites_work_counted', 'subject': 'the-levites', 'counts': dict(WORK), 'total': WORK_TOTAL, 'princes_joined': True, 'case_source': 'Num 4:34-49 — and Moses and Aaron and the princes of the congregation counted the sons of the Kohathite... their counted two thousand seven hundred and fifty... Gershon two thousand six hundred and thirty... Merari three thousand two hundred... all the counted eight thousand five hundred and eighty; by the mouth of the LORD by the hand of Moses'})
        w.marker('Num 5:1', w.clock.day_in('exodus', 2, 1, 1), value='the sending away of the impure — READING-PLACED on the day the tabernacle was erected (R. Levi, Gittin 60a:17): RETROGRADE', placement='reading_placed')
        w.submit({'kind': 'send_out_commanded', 'subject': 'israel', 'classes': ['leper', 'zav', 'corpse_unclean'], 'camps': 3, 'male_and_female': True, 'spoken_day': 'the first of Nisan (R. Levi)', 'case_source': 'Num 5:1-3 — and the LORD spoke to Moses saying: command the children of Israel that they send out of the camp every leper and everyone with an issue and everyone unclean by a corpse; male and female alike you shall send out, outside the camp, that they not defile their camps in whose midst I dwell'})
        w.submit({'kind': 'unclean_sent_out', 'subject': 'the-unclean-of-the-camp', 'classes': ['leper', 'zav', 'corpse_unclean'], 'as_spoken': True, 'case_source': 'Num 5:4 — and the children of Israel did so, and sent them out, outside the camp; as the LORD spoke to Moses, so did the children of Israel'})
        w.marker('Num 7:1', w.clock.day_in('exodus', 2, 1, 1), value='on the day Moses finished setting up the tabernacle (7:1) — the erection\'s day: RETROGRADE after 1:1')
        w.submit({'kind': 'wagons_brought', 'subject': 'the-princes-of-israel', 'wagons': WAGONS[0], 'oxen': WAGONS[1], 'per_prince': 'a wagon for two, an ox for one', 'day': 'the day Moses finished', 'case_source': 'Num 7:2-3 — and the princes of Israel, the heads of their fathers\' houses, they who stood over the counted, brought near; and they brought their offering before the LORD: six covered wagons and twelve oxen, a wagon for two princes and an ox for one, and they brought them before the tabernacle'})
        w.submit({'kind': 'wagons_accepted_commanded', 'subject': 'moses', 'from': 'the-princes-of-israel', 'to': 'the-levites', 'by_service': True, 'case_source': 'Num 7:4-5 — and the LORD said to Moses: take from them, and they shall be for the service of the tent of meeting, and give them to the Levites, each according to his service'})
        w.submit({'kind': 'wagons_assigned', 'subject': 'the-levites', 'gershon': DIST_G, 'merari': DIST_M, 'kohath': [0, 0], 'under': 'ithamar', 'case_source': 'Num 7:6-9 — and Moses took the wagons and the oxen and gave them to the Levites: two wagons and four oxen to the sons of Gershon, four wagons and eight oxen to the sons of Merari, in the hand of Ithamar; and to the sons of Kohath he gave none, for the service of the holy is upon them: on the shoulder they carry'})
        w.submit({'kind': 'dedication_brought', 'subject': 'the-princes-of-israel', 'day': 'the day it was anointed', 'before': 'the altar', 'case_source': 'Num 7:10 — and the princes brought near the dedication of the altar on the day it was anointed, and the princes brought near their offering before the altar'})
        w.submit({'kind': 'dedication_order_commanded', 'subject': 'the-princes-of-israel', 'per_day': 1, 'order': 'the camp\'s (2:3-31)', 'days': 12, 'case_source': 'Num 7:11 — and the LORD said to Moses: one prince per day, one prince per day, they shall bring near their offering for the dedication of the altar'})
        w.close('the-princes-of-israel', 'dedication_brought', 'Num 7:84-88 — this is the dedication of the altar on the day it was anointed: twelve dishes, twelve bowls, twelve pans... all the gold of the pans a hundred and twenty; the twelve days complete', value='the_dedication')
        w.submit({'kind': 'voice_heard_from_the_ark', 'subject': 'moses', 'reflexive': True, 'from': 'between the two cherubim', 'who_heard': 'moses alone', 'case_source': 'Num 7:89 — and when Moses came into the tent of meeting to speak with Him, he heard the Voice speaking itself to him from above the ark-cover that is upon the ark of the testimony, from between the two cherubim; and He spoke to him'})
    n = lambda eid, eff: len([e for e in w.entity(eid).ledger if e['effect'] == eff])
    is_open = lambda eid, eff: [e.get('open') for e in w.entity(eid).ledger if e['effect'] == eff]
    L = lambda k: len([l for l in w.log if l[0] == k])
    markers = [l for l in w.log if l[0] == 'MARKER']
    retro = [l for l in w.log if l[0] == 'RETRO-WRITE']
    return (n('the-levites', 'commanded'), is_open('the-levites', 'commanded'), n('the-levites', 'work_counted'), n('the-levites', 'wagons_assigned'),
            n('israel', 'commanded'), is_open('israel', 'commanded'), n('the-unclean-of-the-camp', 'sent_outside_the_camp'),
            n('moses', 'commanded'), is_open('moses', 'commanded'), n('moses', 'spoken_to_from_the_ark'),
            n('the-princes-of-israel', 'wagons_brought'), n('the-princes-of-israel', 'dedication_brought'), is_open('the-princes-of-israel', 'dedication_brought'),
            sum(n(t, 'dedication_offered') for t in PRINCE_TOKENS), L('RETRO-WRITE'), sorted(set(r[2].get('due') - w.clock.day_in('exodus', 2, 1, 1) for r in retro)),
            len(markers), [m[2].get('retrograde') for m in markers], L('EVENT'), L('WRITE'), len(w.entities)), w


NARRATIVE, _WN = narrative()
NARRATIVE_PREDICTED = (2, [False, False], 1, 1,
                       1, [False], 1,
                       1, [False], 1,
                       1, 1, [False],
                       12, 12, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11],
                       3, [False, True, True], 11, 10, 17)   # typed from the design's arithmetic BEFORE the first run: two count debits (closed by the work-count), the send-out's (closed), the wagons' (closed), the dedication's (closed by the scene's 7:84 line); twelve retro-writes at the anointing day + 0..11; three markers (1:1 forward, 5:1 and 7:1 retrograde); eleven events; ten WRITEs (the twelve dedication entries are RETRO-WRITEs); entities: the-levites, israel, the-unclean-of-the-camp, moses, the-princes-of-israel, the twelve = 17
assert NARRATIVE == NARRATIVE_PREDICTED, ('THE NUMBERS WALK: Naso\'s narrative moved from its prediction', NARRATIVE, NARRATIVE_PREDICTED)


# =====================================================================
# Motion 2 — THE TEST DATA: the answer sheet's rows (the docket's LAW rows).
# =====================================================================
CASES = [
    # F1 — the work-count
    ('Num 4:36-48 — the four work-counts summed (the parser on the ink)', lambda: work_count({'ask': 'counts'}, DATA), '2750 + 2630 + 3200 = 8580'),
    ('Num 4:36-48 against 3:22-34 — the shares (Bamidbar\'s houses CALLED)', lambda: work_count({'ask': 'shares'}, DATA), 'kohath 32, gershon 35, merari 52 of a hundred — the frame-carriers the largest share'),
    ('Num 4:47; Chullin 24a:12 — the ages (Bamidbar\'s table CALLED)', lambda: work_count({'ask': 'ages'}, DATA), 'thirty to fifty — 25 learn, 30 serve, 50 return'),
    ('Chullin 24a:12 — the apprentice of twenty-seven (Bamidbar\'s fitness CALLED)', lambda: work_count({'ask': 'fitness', 'who': 'levite', 'age': 27}, DATA), 'unfit — under thirty (twenty-five to apprentice)'),
    ('Chullin 24a:11 — fifty-five at Shiloh, not carrying', lambda: work_count({'ask': 'fitness', 'who': 'levite', 'age': 55, 'carrying': False}, DATA), 'fit — years disqualify only while carrying'),
    ('Arakhin 11a:17 — 4:47 the service of service', lambda: work_count({'ask': 'song'}, DATA), 'the service of service is the song (Arakhin 11a)'),
    ('Num 4:25-32; 7:9 — the three loads', lambda: work_count({'ask': 'loads'}, DATA), 'gershon the soft, merari the hard; kohath the holy (on the shoulder)'),
    ('Num 4:28, 4:33, 4:16 — under whose hand', lambda: work_count({'ask': 'under'}, DATA), 'Gershon and Merari under Ithamar; Kohath under Eleazar'),
    ('Num 4:37, 4:41, 4:45, 4:49 — the formula and its variant', lambda: work_count({'ask': 'formula'}, DATA), 'by the mouth of the LORD by the hand of Moses at 4:37, 4:45, 4:49; by the mouth of the LORD at 4:41'),
    ('Num 4:34, 4:46 — the princes among the counters', lambda: work_count({'ask': 'princes'}, DATA), 'the princes counted with Moses and Aaron (4:34, 4:46)'),
    # F2 — the camp's purity
    ('Num 5:2 — the three classes', lambda: camp_purity({'ask': 'classes'}, DATA), 'the leper, the zav, the corpse-unclean — three classes'),
    ('Pesachim 67a:11; Mishnah Kelim 1:7 — the leper (the negaim engine CALLED)', lambda: camp_purity({'ask': 'ladder', 'who': 'leper'}, DATA), 'out of all three camps (Israel, Levi, the Presence)'),
    ('Pesachim 67a:12; Mishnah Kelim 1:8 — the zav (the clocks engine CALLED)', lambda: camp_purity({'ask': 'ladder', 'who': 'zav'}, DATA), 'out of two (Levi and the Presence)'),
    ('Zevachim 117a:1 — the corpse-unclean (the chukat engine CALLED — the edge paid at 6b)', lambda: camp_purity({'ask': 'ladder', 'who': 'corpse_unclean'}, DATA), 'out of one (the Presence)'),
    ('Zevachim 116b; Mishnah Kelim 1:7-8 — the three camps (Bamidbar CALLED)', lambda: camp_purity({'ask': 'three_camps'}, DATA), 'israel: the walls to the mount; levites: the mount to nicanor; presence: the courtyard'),
    ('Eruvin 104b:10 — the purifiable is sent', lambda: camp_purity({'ask': 'who_is_sent', 'what': 'purifiable'}, DATA), 'sent — has a purification (Eruvin 104b)'),
    ('Eruvin 104b:10 — a creeping thing\'s carcass', lambda: camp_purity({'ask': 'who_is_sent', 'what': 'creeping_carcass'}, DATA), 'not sent — no purification (Eruvin 104b)'),
    ('Niddah 28b:1 — the tumtum', lambda: camp_purity({'ask': 'who_is_sent', 'what': 'tumtum'}, DATA), 'not liable — male and female (Niddah 28b)'),
    ('Makkot 14b:6; Mishnah Makkot 3:2 — the impure who entered', lambda: camp_purity({'ask': 'entered_impure'}, DATA), 'lashes (5:3 the prohibition, 19:13 the punishment)'),
    ('Pesachim 67a:7 / 67a:11 — the leper beyond his boundary', lambda: camp_purity({'ask': 'leper_entered'}, DATA), 'a dispute: exempt (Rav Chisda) / liable (R. Yehuda\'s tanna)'),
    ('Pesachim 67b:8, 95b:14 — the Passover in impurity', lambda: camp_purity({'ask': 'impure_pesach', 'majority_impure': True}, DATA), 'zavim and lepers not liable to karet (R. Eliezer)'),
    ('Pesachim 67b:8 — the majority pure', lambda: camp_purity({'ask': 'impure_pesach', 'majority_impure': False}, DATA), 'liable to karet (the corpse-unclean sent)'),
    ('Pesachim 92a:15 — the tevul yom and the Passover', lambda: camp_purity({'ask': 'tevul_yom_pesach'}, DATA), 'may enter — the Passover\'s karet overrides (Pesachim 92a)'),
    ('Taanit 21b:5 — the tent rolled up (Bamidbar\'s tent CALLED)', lambda: camp_purity({'ask': 'tent_rolled_up'}, DATA), 'the place unsacred — the Presence, not the ground (Taanit 21b)'),
    ('Sifrei 1:1 — the warning for 19:20', lambda: camp_purity({'ask': 'warning'}, DATA), 'the warning for 19:20\'s punishment (Sifrei 1:1)'),
    ('Gittin 60a:17 — the day the section was said', lambda: camp_purity({'ask': 'day'}, DATA), 'the first of Nisan — R. Levi\'s eight sections (Gittin 60a:17): reading-placed'),
    ('Sifrei 1:8 — the run doubled', lambda: camp_purity({'ask': 'run_doubled'}, DATA), 'before the calf no zavim; after — the doubling (Sifrei 1:8)'),
    # F3 — the theft's restitution and the gifts
    ('Num 5:7; Mishnah Sanhedrin 6:2 — the confession', lambda: restitution({'ask': 'confession'}, DATA), 'confess (the executed confess — Sanhedrin 6:2)'),
    ('Bava Kamma 110a:12-17 — the principal', lambda: restitution({'ask': 'principal'}, DATA), 'at its head — the principal, not the double'),
    ('Bava Metzia 54a; Sifrei 3:1 — the fifth\'s base (the running setting)', lambda: restitution({'ask': 'fifth'}, DATA), 'a quarter added = a fifth of the whole (Bava Metzia 54a)'),
    ('Lev 5:24 CALLED — the algebra for a hundred', lambda: restitution({'ask': 'algebra', 'value': 100}, DATA), 'pay its value; add the fifth (25.00); ram at the valuation floor'),
    ('Mishnah Bava Kamma 9:7 — the fifth on the fifth (Lev 5\'s cell CALLED)', lambda: restitution({'ask': 'algebra', 'value': 100, 'swore_on_fifth': True}, DATA), 'pay its value; add the fifth (25.00); fifth on the fifth, to the perutah floor; ram at the valuation floor'),
    ('Bava Kamma 111a:11; Mishnah 9:12 — the order', lambda: restitution({'ask': 'order'}, DATA), 'the money first, then the ram (Bava Kamma 111a; Mishnah 9:12)'),
    ('Bava Kamma 109a:5; Arakhin 28b:1; Mishnah 9:11 — the proselyte dead', lambda: restitution({'ask': 'proselyte_dead'}, DATA), 'to the priests of the watch (5:8; Arakhin 28b)'),
    ('Mishnah Bava Kamma 9:11 — the robber died on the way', lambda: restitution({'ask': 'robber_died_before'}, DATA), 'the money to his children; the ram grazes, sold for communal gifts (Mishnah 9:11)'),
    ('Mishnah Bava Kamma 9:12 — given to the watch then died', lambda: restitution({'ask': 'given_then_died'}, DATA), 'the heirs cannot reclaim — 5:10 (Mishnah 9:12)'),
    ('Mishnah Bava Kamma 9:12 — the fifth missing', lambda: restitution({'ask': 'fifth_not_precluding'}, DATA), 'the fifth missing does not preclude the ram (Mishnah 9:12)'),
    ('Bava Kamma 15a:4 — the equating rule', lambda: restitution({'ask': 'woman_equals_man'}, DATA), 'a woman equals a man for all punishments (5:6 — Bava Kamma 15a)'),
    ('Sifrei 4:2 — the priest-thief', lambda: restitution({'ask': 'priest_thief'}, DATA), 'the priest-thief does not keep it (Sifrei 4:2)'),
    ('Mishnah Bava Kamma 9:5 — to whom', lambda: restitution({'ask': 'to_whom'}, DATA), 'to the victim himself, even to Media; not his son or agent (Mishnah 9:5)'),
    ('Mishnah Bava Kamma 9:6 — the remainder', lambda: restitution({'ask': 'remainder'}, DATA), 'pursue for the principal, not for the fifth; a perutah the floor (Mishnah 9:6)'),
    ('Mishnah Bava Kamma 9:9 — robbed his father', lambda: restitution({'ask': 'robbed_father'}, DATA), 'to the father\'s sons or brothers; forfeits his share; the ram (Mishnah 9:9)'),
    ('Bava Kamma 106a:16 — confessed after the oath', lambda: restitution({'ask': 'confessed_after_oath'}, DATA), 'principal and fifth even where the oath would exempt (Bava Kamma 106a)'),
    ('Bava Kamma 109b:3 — the female proselyte', lambda: restitution({'ask': 'proselyte_female'}, DATA), 'an open dilemma (Bava Kamma 109b:3)'),
    ('Num 5:9-10; Arakhin 34a:6 — the owner\'s choice', lambda: restitution({'ask': 'owners_choice'}, DATA), 'the owner\'s choice of priest; the priest\'s own offering his'),
    ('Mishnah Terumot 4:5 — the terumah\'s measure', lambda: restitution({'ask': 'terumah_measure'}, DATA), 'the owner\'s measure, with a floor: some must remain non-sacred (Mishnah Terumot 4:5)'),
    ('Bava Kamma 109b:16 — the blemished priest\'s own offering', lambda: restitution({'ask': 'blemished_priests_offering'}, DATA), 'flesh and hide his (Bava Kamma 109b:16)'),
    ('Sifrei 6:1; Bekhorot 49a — the firstborn after thirty days (Bamidbar CALLED)', lambda: restitution({'ask': 'firstborn_thirty', 'age_days': 31}, DATA), 'after thirty days'),
    ('Bekhorot 49a — before thirty days (Bamidbar CALLED)', lambda: restitution({'ask': 'firstborn_thirty', 'age_days': 20}, DATA), 'not yet — before thirty days'),
    ('Onkelos 5:10 — the tithe inserted', lambda: restitution({'ask': 'tithe_inserted'}, DATA), 'the tithe Onkelos inserts at 5:10'),
    # F4 — the suspected wife
    ('Num 5:13 — the six conditions', lambda: sotah({'ask': 'conditions'}, DATA), 'six: lain with, hidden, secreted, defiled, no witness, not seized'),
    ('Sotah 2a:12; Mishnah 6:3 — one witness for defilement', lambda: sotah({'ask': 'witnesses', 'what': 'defilement'}, DATA), 'one witness suffices (5:13)'),
    ('Mishnah Sotah 1:1 — two for the warning', lambda: sotah({'ask': 'witnesses', 'what': 'warning'}, DATA), 'two (R. Yehoshua; the mishnah)'),
    ('Sotah 2b:10 — the seclusion (the running setting)', lambda: sotah({'ask': 'witnesses', 'what': 'seclusion'}, DATA), 'two (R. Yehoshua) — R. Eliezer one'),
    ('Sotah 4a:9 — the measure of seclusion (the running setting)', lambda: sotah({'ask': 'secluded'}, DATA), 'the time for the first stage of intercourse — the returning of a palm (R. Eliezer)'),
    ('Mishnah Sotah 4:1; Kiddushin 27b:7 — the betrothed', lambda: sotah({'ask': 'status', 'who': 'betrothed'}, DATA), 'neither drinks nor collects (5:29 under her husband)'),
    ('Mishnah Sotah 4:1 — the widow awaiting the levir', lambda: sotah({'ask': 'status', 'who': 'awaiting_levir'}, DATA), 'neither drinks nor collects (5:29 under her husband)'),
    ('Mishnah Sotah 4:1 — a forbidden marriage', lambda: sotah({'ask': 'status', 'who': 'forbidden_marriage'}, DATA), 'neither drinks nor collects (a forbidden marriage)'),
    ('Sotah 25b:3; Mishnah 4:3 — the ailonit', lambda: sotah({'ask': 'status', 'who': 'ailonit'}, DATA), 'neither (the Rabbis; R. Elazar: drinks)'),
    ('Sotah 26a:11; Mishnah Eduyot 5:6 — the convert', lambda: sotah({'ask': 'status', 'who': 'convert'}, DATA), 'drinks (the Sages; Akavya recorded)'),
    ('Mishnah Sotah 4:4; Sotah 26a:12 — the priest\'s wife', lambda: sotah({'ask': 'status', 'who': 'priests_wife'}, DATA), 'drinks; cleared she is permitted'),
    ('Mishnah Sotah 4:4; Sotah 26a:15 — the eunuch\'s wife', lambda: sotah({'ask': 'status', 'who': 'eunuchs_wife'}, DATA), 'drinks'),
    ('Mishnah Sotah 4:3 — pregnant or nursing', lambda: sotah({'ask': 'status', 'who': 'pregnant_or_nursing'}, DATA), 'the Rabbis: drinks; R. Meir: neither'),
    ('Kiddushin 27b:9; Sotah 28a:1 — the husband not clean', lambda: sotah({'ask': 'husband_clean', 'clean': False}, DATA), 'the waters do not test — the man not clear of iniquity (5:31)'),
    ('Sotah 24b:2; Yevamot 58a:14 — the husband first', lambda: sotah({'ask': 'husband_first'}, DATA), 'only when the husband\'s cohabitation preceded (5:20)'),
    ('Ketubot 81a:6; Mishnah 4:2 — the husband died (the running setting)', lambda: sotah({'ask': 'husband_dead'}, DATA), 'Beit Hillel: no drink, no ketubah'),
    ('Mishnah Sotah 4:4; Sotah 26b:1 — warned about a relative', lambda: sotah({'ask': 'warned_about', 'who': 'relative'}, DATA), 'valid'),
    ('Sotah 26b:6 — warned about a gentile', lambda: sotah({'ask': 'warned_about', 'who': 'gentile'}, DATA), 'valid'),
    ('Sotah 26b:2 — warned about a minor', lambda: sotah({'ask': 'warned_about', 'who': 'minor'}, DATA), 'no warning'),
    ('Sotah 24a:10 — the warning\'s scope', lambda: sotah({'ask': 'warning_scope'}, DATA), 'the betrothed and the shomeret yavam can be warned, not tested'),
    ('Mishnah Sotah 4:5; Sotah 27a:7 — the court warns', lambda: sotah({'ask': 'court_warns'}, DATA), 'to disqualify the ketubah (the Sages); R. Yosei: to drink too'),
    ('Sotah 6a:10 — witnesses overseas', lambda: sotah({'ask': 'witnesses_overseas'}, DATA), 'not tested — witnesses exist overseas'),
    ('Keritot 24a:9 — conspiring witnesses', lambda: sotah({'ask': 'witnesses_conspiring'}, DATA), 'her minchah non-sacred'),
    ('Mishnah Sotah 6:1 — the rumor', lambda: sotah({'ask': 'rumor'}, DATA), 'R. Eliezer: divorce with the ketubah; R. Yehoshua: not until the spinners'),
    ('Mishnah Sotah 6:2 — a slave\'s testimony', lambda: sotah({'ask': 'witness_of_defilement', 'who': 'slave'}, DATA), 'believed — bars the ketubah'),
    ('Mishnah Sotah 6:2 — the mother-in-law\'s', lambda: sotah({'ask': 'witness_of_defilement', 'who': 'mother_in_law'}, DATA), 'believed only to bar the drinking'),
    ('Mishnah Sotah 6:4 — one against one', lambda: sotah({'ask': 'contradicting', 'for': 1, 'against': 1}, DATA), 'drinks'),
    ('Mishnah Sotah 6:4 — two against one', lambda: sotah({'ask': 'contradicting', 'for': 2, 'against': 1}, DATA), 'does not drink, divorced'),
    ('Sotah 7a:10; Mishnah 1:3 — the escort', lambda: sotah({'ask': 'escort'}, DATA), 'two scholars (rabbinic; R. Yehuda: trusted)'),
    ('Sotah 7b:3; Mishnah 1:4 — the court', lambda: sotah({'ask': 'court'}, DATA), 'the Sanhedrin of seventy-one (torah/torah)'),
    ('Mishnah Sotah 1:4 — the admonition', lambda: sotah({'ask': 'admonition'}, DATA), 'wine, levity, immaturity, bad neighbors; act for the great Name'),
    ('Mishnah Sotah 1:5 — she confesses', lambda: sotah({'ask': 'confesses'}, DATA), 'a receipt for the ketubah; divorced'),
    ('Sotah 8a:2; Mishnah 1:5 — the place', lambda: sotah({'ask': 'place'}, DATA), 'the Nicanor gate — before the LORD'),
    ('Sotah 8a:10; Mishnah 1:5-6 — the uncovering', lambda: sotah({'ask': 'uncovering'}, DATA), 'the head, the body, the hair unbraided; black garments; the Egyptian rope; the adornments removed'),
    ('Mishnah Sotah 2:1; Menachot 59a:5 — the minchah\'s form (the minchah engine CALLED)', lambda: sotah({'ask': 'minchah_form'}, DATA), 'barley, unsifted; no oil, no frankincense — as the sinner\'s: neither'),
    ('Onkelos 5:15 — the ephah as three se\'ah', lambda: sotah({'ask': 'ephah'}, DATA), 'a tenth of an ephah = a tenth of three se\'ah (Onkelos)'),
    ('Num 5:26 — the fistful (the minchah engine CALLED)', lambda: sotah({'ask': 'fistful'}, DATA), 'the scoop level — the meal-offering engine: overflowing or fingertips invalid'),
    ('Kiddushin 36b:4; Mishnah 3:1 — the waving', lambda: sotah({'ask': 'waving'}, DATA), 'by her hand and the priest\'s together (hand/hand with Lev 7:30)'),
    ('Menachot 60b:6; Mishnah Menachot 5:6 — bringing near', lambda: sotah({'ask': 'bringing_near'}, DATA), 'required (5:25 draw it near)'),
    ('Menachot 4a:8 — not for its name', lambda: sotah({'ask': 'minchah_not_for_its_name'}, DATA), 'disqualified; the surplus to communal gifts'),
    ('Mishnah Sotah 2:2; Temurah 12b:6 — the water and the dust', lambda: sotah({'ask': 'water_and_dust'}, DATA), 'half a log from the laver (R. Yehuda a quarter); the dust from the Sanctuary floor, visible on the water; water first (R. Shimon: either)'),
    ('Sotah 15b:4 — the vessel', lambda: sotah({'ask': 'vessel'}, DATA), 'a new earthenware vessel (R. Yishmael)'),
    ('Sotah 20a:4 — the bitter substance', lambda: sotah({'ask': 'bitter_added'}, DATA), 'a bitter substance in the water'),
    ('Mishnah Sotah 2:3 — the scroll\'s text', lambda: sotah({'ask': 'scroll_text'}, DATA), 'from 5:19 through 5:22\'s curses, without the frame and the amens (the Rabbis); R. Yosei whole; R. Yehuda curses alone'),
    ('Mishnah Sotah 2:4; Eruvin 13a:10 — the scroll\'s material and ink', lambda: sotah({'ask': 'scroll_material'}, DATA), 'a scroll (parchment); erasable ink; no iron sulfate'),
    ('Sotah 17b:3 — by day', lambda: sotah({'ask': 'scroll_time'}, DATA), 'by day'),
    ('Sotah 17b:4 — the order', lambda: sotah({'ask': 'scroll_order'}, DATA), 'the Torah\'s order'),
    ('Sotah 17b:5 — before the oath', lambda: sotah({'ask': 'scroll_before_oath'}, DATA), 'unfit'),
    ('Sotah 18a:2 — the erasure', lambda: sotah({'ask': 'scroll_erasure'}, DATA), 'written whole, erased at once'),
    ('Eruvin 13b:2; Sotah 20b:6 — for her name', lambda: sotah({'ask': 'for_her_name'}, DATA), 'the erasure for her name; the writing not'),
    ('Sotah 32b:2; Mishnah 7:1 — the language', lambda: sotah({'ask': 'language'}, DATA), 'any language'),
    ('Sanhedrin 32b:18 — the oath\'s order', lambda: sotah({'ask': 'oath_order'}, DATA), 'the innocent clause first'),
    ('Sotah 18a:8 — two oaths', lambda: sotah({'ask': 'oaths_count'}, DATA), 'two: before and after the erasure'),
    ('Mishnah Sotah 2:5; Kiddushin 27b:6 — amen, amen', lambda: sotah({'ask': 'amen_amen'}, DATA), 'on the curse and the oath; this man and another; betrothed, married, awaiting the levir, married to the levir'),
    ('Shevuot 29b:9 — amen is an oath', lambda: sotah({'ask': 'amen_is_oath'}, DATA), 'amen = her oath (Shmuel)'),
    ('Shevuot 35b:23 — the oath\'s form', lambda: sotah({'ask': 'oath_form'}, DATA), 'a curse, in the Name'),
    ('Mishnah Sotah 2:6 — the oath\'s scope', lambda: sotah({'ask': 'oath_scope'}, DATA), 'only acts that would forbid her'),
    ('Keritot 9b:10 — several warnings', lambda: sotah({'ask': 'several_warnings'}, DATA), 'one meal-offering (jealousies)'),
    ('Mishnah Sotah 3:2; Sotah 19a — the order of drinking and offering (the running setting)', lambda: sotah({'ask': 'order'}, DATA), 'drink then offer (the Rabbis); R. Shimon offer then drink; either valid after the fact'),
    ('Sotah 19b:2 — R. Shimon\'s three preconditions', lambda: sotah({'ask': 'preconditions'}, DATA), 'R. Shimon: the fistful offered, the scroll erased, the oath accepted'),
    ('Mishnah Sotah 3:3 — refuses before the erasure', lambda: sotah({'ask': 'refuses', 'when': 'before_erasure'}, DATA), 'the scroll sequestered, the minchah burned; not forced'),
    ('Mishnah Sotah 3:3; Sotah 19b:1 — refuses after the erasure', lambda: sotah({'ask': 'refuses', 'when': 'after_erasure'}, DATA), 'forced to drink'),
    ('Mishnah Sotah 3:3 — confesses after the erasure', lambda: sotah({'ask': 'refuses', 'when': 'confesses_after_erasure'}, DATA), 'the water poured out, the minchah scattered'),
    ('Mishnah Megillah 2:5 — the time', lambda: sotah({'ask': 'time'}, DATA), 'by day, the whole day'),
    ('Sotah 8a:4; Nedarim 73a:7 — two at once', lambda: sotah({'ask': 'two_at_once'}, DATA), 'not together'),
    ('Mishnah Sotah 3:4, 1:7 — the guilty outcome', lambda: sotah({'ask': 'outcome', 'guilty': True}, DATA), 'her face greens, her belly swells, her thigh falls — she dies; the paramour too'),
    ('Mishnah Sotah 3:4; Sotah 20b:14 — merit suspends (the running setting)', lambda: sotah({'ask': 'outcome', 'guilty': True, 'merit': True}, DATA), 'suspended (three, nine, twelve months — the Sifrei; one to three years — the mishnah; R. Shimon none)'),
    ('Num 5:28; Sotah 26a:7-8 — the innocent outcome', lambda: sotah({'ask': 'outcome', 'guilty': False}, DATA), 'cleared and sown with seed (the barren conceives — R. Akiva; R. Yishmael: ease)'),
    ('Mishnah Sotah 5:1 — the paramour tested', lambda: sotah({'ask': 'paramour_tested'}, DATA), 'tested too (5:24, 5:27)'),
    ('Sotah 28a:19, 29a:2 — the consequences', lambda: sotah({'ask': 'defiled_consequences'}, DATA), 'forbidden to her husband, her paramour, the priesthood and terumah (R. Akiva)'),
    ('Sotah 28a:21; Mishnah 1:2 — the doubt forbids', lambda: sotah({'ask': 'doubt_forbids'}, DATA), 'forbidden to her husband until clarified'),
    ('Yevamot 11a:10 — the levirate', lambda: sotah({'ask': 'levirate'}, DATA), 'exempt from levirate and chalitzah (Yevamot 11a)'),
    ('Mishnah Sotah 3:6 — the confessed one\'s minchah', lambda: sotah({'ask': 'minchah_disposition', 'case': 'confessed'}, DATA), 'burned (once in a service vessel; redeemed if before)'),
    ('Mishnah Sotah 3:7 — a priest\'s daughter married to an Israelite', lambda: sotah({'ask': 'minchah_disposition', 'case': 'priests_daughter_to_israelite'}, DATA), 'eaten'),
    ('Sotah 27a:10-27b:1 — the blind, the lame, the mute', lambda: sotah({'ask': 'disabled', 'who': 'blind'}, DATA), 'neither side drinks or gives to drink'),
    ('Ketubot 51b:13 — raped', lambda: sotah({'ask': 'intercourse', 'consent': 'raped'}, DATA), 'permitted to her husband'),
    ('Yevamot 56b:7 — the priest\'s wife raped', lambda: sotah({'ask': 'intercourse', 'consent': 'raped', 'who': 'priests_wife'}, DATA), 'forbidden (the priest\'s wife)'),
    ('Sotah 18b:15 — drinks twice', lambda: sotah({'ask': 'drinks_twice'}, DATA), 'drinks again for a second warning'),
    ('Mishnah Sotah 9:9; Sotah 47b — the abolition (the tape runs the rite)', lambda: sotah({'ask': 'abolished'}, DATA), 'the rite runs (the ink); abolished by Rabban Yochanan ben Zakkai — Hosea 4:14 (the tradition\'s setting)'),
    ('Sotah 3a:17 — the warning permitted', lambda: sotah({'ask': 'warning_permitted'}, DATA), 'permitted (R. Eliezer b. Yaakov); optional or obligatory disputed'),
    ('Kiddushin 62a:2; Sotah 3a:4 — the spellings the teacher re-reads (measured)', lambda: sotah({'ask': 'spelling'}, DATA), 'hinnaki without the yod read also as chinnaki; tisteh read as folly — the ink measured'),
    # F5 — the nazirite
    ('Nedarim 3a:5; Mishnah Nazir 1:1 — a substitute', lambda: nazirite({'ask': 'vow_form', 'form': 'substitute'}, DATA), 'binds (nazir lehazir)'),
    ('Mishnah Nazir 1:2 — a partial vow', lambda: nazirite({'ask': 'vow_form', 'form': 'partial'}, DATA), 'a full nazirite'),
    ('Mishnah Nazir 1:1 — "birds"', lambda: nazirite({'ask': 'vow_form', 'form': 'birds'}, DATA), 'the Sages: not (R. Meir: a nazirite)'),
    ('Mishnah Nazir 2:3 — the cup', lambda: nazirite({'ask': 'vow_form', 'form': 'from_the_cup'}, DATA), 'a nazirite; the drunk woman\'s a konam'),
    ('Mishnah Nazir 2:4 — on condition to drink', lambda: nazirite({'ask': 'vow_form', 'form': 'conditioned_on_wine'}, DATA), 'a full nazirite'),
    ('Mishnah Nazir 2:4 — thought the Sages would permit', lambda: nazirite({'ask': 'vow_form', 'form': 'mistaken_sages_permit'}, DATA), 'free (R. Shimon bound)'),
    ('Mishnah Nazir 2:1; Nazir 9a:2 — from figs', lambda: nazirite({'ask': 'vow_form', 'form': 'figs'}, DATA), 'Beit Hillel: not (Shammai: a nazirite)'),
    ('Mishnah Nazir 1:2 — like Samson', lambda: nazirite({'ask': 'vow_form', 'form': 'samson'}, DATA), 'a Samson-nazirite: never shaves, no impurity offering'),
    ('Nedarim 5b:5 — an ambiguous intimation', lambda: nazirite({'ask': 'vow_form', 'form': 'ambiguous_intimation'}, DATA), 'Rava: not'),
    ('Mishnah Nazir 5:5; Nazir 34a:1 — the uncertain vow', lambda: nazirite({'ask': 'vow_form', 'form': 'uncertain'}, DATA), 'Hillel: whose statement failed; R. Tarfon none'),
    ('Nazir 61a:7; Mishnah 9:1 — a gentile', lambda: nazirite({'ask': 'who_vows', 'who': 'gentile'}, DATA), 'no naziriteship'),
    ('Mishnah Nazir 9:1 — a slave', lambda: nazirite({'ask': 'who_vows', 'who': 'slave'}, DATA), 'yes (the master forces)'),
    ('Niddah 46a:2; Mishnah Niddah 5:6 — a boy of thirteen and a day', lambda: nazirite({'ask': 'who_vows', 'who': 'boy', 'age': 13}, DATA), 'valid (thirteen and a day)'),
    ('Mishnah Niddah 5:6 — a boy of twelve', lambda: nazirite({'ask': 'who_vows', 'who': 'boy', 'age': 12}, DATA), 'examined (the twelfth year)'),
    ('Mishnah Nazir 1:3; Nazir 5a:16 — the unspecified term (the data row)', lambda: nazirite({'ask': 'term', 'form': 'unspecified'}, DATA), '30 days'),
    ('Mishnah Nazir 1:3 — "and a day"', lambda: nazirite({'ask': 'term', 'form': 'and_a_day'}, DATA), '60 days (two terms)'),
    ('Mishnah Nazir 1:3 — thirty days and an hour', lambda: nazirite({'ask': 'term', 'form': 'thirty_and_an_hour'}, DATA), '31 days'),
    ('Mishnah Nazir 1:4 — like the hairs of my head', lambda: nazirite({'ask': 'term', 'form': 'like_the_hairs'}, DATA), 'forever, shaving every thirty (Rebbi: one term)'),
    ('Mishnah Nazir 1:6 — from here to a place forty days off', lambda: nazirite({'ask': 'term', 'form': 'distance', 'days': 40}, DATA), '40 days'),
    ('Mishnah Nazir 1:7 — the solar year', lambda: nazirite({'ask': 'term', 'form': 'solar_year'}, DATA), '365 terms'),
    ('Mishnah Nazir 3:1 — the shaving day', lambda: nazirite({'ask': 'shaving_day', 'form': 'unspecified'}, DATA), 'the thirty-first (the thirtieth fulfilled)'),
    ('Mishnah Nazir 3:2 — two terms', lambda: nazirite({'ask': 'shaving_day', 'form': 'two_terms'}, DATA), '31 and 61 (30 and 60; 59 fulfilled)'),
    ('Mishnah Nazir 6:1 — a quarter-log of wine', lambda: nazirite({'ask': 'ate', 'product': 'wine', 'amount': 'quarter_log'}, DATA), 'lashes'),
    ('Mishnah Nazir 6:1; Nazir 38b:1 — less than a quarter-log', lambda: nazirite({'ask': 'ate', 'product': 'wine', 'amount': 'less_than_a_quarter_log'}, DATA), 'exempt (R. Akiva: an olive\'s bulk with bread)'),
    ('Nazir 34b:7 — leaves (the running setting)', lambda: nazirite({'ask': 'ate', 'product': 'leaves'}, DATA), 'permitted (the Rabbis; R. Elazar forbids)'),
    ('Nazir 35b:12 — a permitted mixture', lambda: nazirite({'ask': 'ate', 'product': 'mixture'}, DATA), 'combines — liable (soaked)'),
    ('Nazir 38b:4 / Pesachim 41b:5 — a seed', lambda: nazirite({'ask': 'ate', 'product': 'seed'}, DATA), 'lashes (Rava one set; Abaye two)'),
    ('Mishnah Nazir 6:2 — R. Elazar b. Azarya\'s measure', lambda: nazirite({'ask': 'ate', 'product': 'two_seeds_one_skin'}, DATA), 'R. Elazar b. Azarya\'s measure — liable'),
    ('Nazir 4a:3, 44a:9 — mitzvah wine', lambda: nazirite({'ask': 'mitzvah_wine'}, DATA), 'forbidden like optional'),
    ('Pesachim 23a:5 — benefit from wine', lambda: nazirite({'ask': 'benefit_from_wine'}, DATA), 'permitted (his naziriteship)'),
    ('Mishnah Nazir 6:3 — scissors', lambda: nazirite({'ask': 'shaving_means', 'means': 'scissors'}, DATA), 'liable'),
    ('Nazir 39b:5-6 — plucked any amount', lambda: nazirite({'ask': 'shaving_means', 'means': 'plucked_any'}, DATA), 'R. Yoshiya liable (R. Yonatan exempt)'),
    ('Mishnah Nazir 6:3 — shampooing', lambda: nazirite({'ask': 'shaving_means', 'means': 'shampoo'}, DATA), 'permitted; combing not'),
    ('Nazir 44a:17 — shaved by another', lambda: nazirite({'ask': 'shaved_by_another'}, DATA), 'both liable'),
    ('Nazir 42a:3 — the shaving\'s amount', lambda: nazirite({'ask': 'shaving_amount'}, DATA), 'all the hair'),
    ('Nazir 40a — the final shaving\'s tool', lambda: nazirite({'ask': 'final_shaving_tool'}, DATA), 'a razor'),
    ('Mishnah Nazir 7:2 — a half-log of blood', lambda: nazirite({'ask': 'impurity_kinds', 'source': 'half_log_blood'}, DATA), 'shaves'),
    ('Mishnah Nazir 7:2 — a barley-grain bone by tent', lambda: nazirite({'ask': 'impurity_kinds', 'source': 'barley_grain_bone', 'mode': 'tent'}, DATA), 'not — the barley-grain bone does not defile by tent'),
    ('Mishnah Nazir 7:3-4 — a quarter-log of blood (the halakhah from Sinai)', lambda: nazirite({'ask': 'impurity_kinds', 'source': 'quarter_log_blood'}, DATA), 'not (a halakhah to Moses from Sinai — R. Akiva\'s a-fortiori refused)'),
    ('Mishnah Nazir 7:3 — the land of the nations', lambda: nazirite({'ask': 'impurity_kinds', 'source': 'land_of_nations'}, DATA), 'not — sprinkled, no negation'),
    ('Nazir 48a:1 — their leprosy', lambda: nazirite({'ask': 'impurity_kinds', 'source': 'leprosy'}, DATA), 'not corpse impurity — no negation; the days count'),
    ('Pesachim 80b:15 — a creeping thing', lambda: nazirite({'ask': 'impurity_kinds', 'source': 'creeping'}, DATA), 'not — only the corpse'),
    ('Zevachim 100a:6 — a relative on the way to the Passover', lambda: nazirite({'ask': 'impurity_for', 'who': 'relative'}, DATA), 'not — even on the way to the Passover'),
    ('Nazir 48a; Yevamot 7a:3 — the met mitzvah', lambda: nazirite({'ask': 'impurity_for', 'who': 'met_mitzvah'}, DATA), 'becomes impure — even on the way to the Passover'),
    ('Mishnah Nazir 7:1 — with the High Priest', lambda: nazirite({'ask': 'met_mitzvah_with_high_priest'}, DATA), 'the nazirite becomes impure (the Rabbis); R. Eliezer the priest'),
    ('Nazir 42b:1 — the impurity\'s lashes', lambda: nazirite({'ask': 'impurity_lashes'}, DATA), 'a set per distinct ban (the corpse and the enclosure); repeated impurity one set'),
    ('Mishnah Makkot 3:7 — drinking all day', lambda: nazirite({'ask': 'lashes_count', 'warnings': 0}, DATA), '1 set(s) — one, or one per warning'),
    ('Mishnah Makkot 3:7 — three warnings', lambda: nazirite({'ask': 'lashes_count', 'warnings': 3}, DATA), '3 set(s) — one, or one per warning'),
    ('Mishnah Nazir 6:5, 7:2 — impurity negates', lambda: nazirite({'ask': 'what_negates', 'act': 'impurity', 'day': 15, 'term': 30}, DATA), 'all — recount after purification and offerings'),
    ('Mishnah Nazir 3:3 — impure on the thirtieth', lambda: nazirite({'ask': 'what_negates', 'act': 'impurity', 'day': 30, 'term': 30}, DATA), 'all (R. Eliezer seven)'),
    ('Mishnah Nazir 3:4 — the hundredth day', lambda: nazirite({'ask': 'what_negates', 'act': 'impurity', 'day': 100, 'term': 100}, DATA), 'all (R. Eliezer thirty)'),
    ('Mishnah Nazir 3:4 — the hundred and first', lambda: nazirite({'ask': 'what_negates', 'act': 'impurity', 'day': 101, 'term': 100}, DATA), 'thirty (R. Eliezer seven)'),
    ('Nazir 19b:2-5 — impure on the second day', lambda: nazirite({'ask': 'what_negates', 'act': 'impurity', 'day': 2, 'term': 30}, DATA), 'nothing — no first days (two)'),
    ('Mishnah Nazir 6:3, 6:5 — shaving negates', lambda: nazirite({'ask': 'what_negates', 'act': 'shaving'}, DATA), 'thirty'),
    ('Nazir 44a:11 — wine negates', lambda: nazirite({'ask': 'what_negates', 'act': 'wine'}, DATA), 'nothing'),
    ('Nazir 63a:4; Mishnah 9:2 — the depths', lambda: nazirite({'ask': 'what_negates', 'act': 'unknown_impurity'}, DATA), 'nothing (the depths)'),
    ('Mishnah Nazir 3:5; Nazir 18a:2 — vowed in a cemetery', lambda: nazirite({'ask': 'vowed_in_cemetery'}, DATA), 'the days do not count; no shaving, no birds; re-entered: counts and brings'),
    ('Mishnah Nazir 6:6; Keritot 2b:5 — the defiled nazirite\'s week (the running setting)', lambda: nazirite({'ask': 'defiled'}, DATA), 'sprinkled the third and seventh, shaves the seventh, brings the eighth (a lamb asham, two birds); intentional as unwitting; the recount from the eighth'),
    ('Mishnah Kinnim 1:1, 2:5 — the birds', lambda: nazirite({'ask': 'birds'}, DATA), 'one chatat, one olah; not mixed'),
    ('Mishnah Nazir 6:7-8 — the completion (the offering engine CALLED)', lambda: nazirite({'ask': 'completion'}, DATA), 'three animals — the sin, the burnt, the peace; shaves after the peace-offering (R. Yehuda; R. Elazar the sin); any one suffices'),
    ('Nazir 45a:13; Yoma 16a:2 — where he shaves', lambda: nazirite({'ask': 'where_shaves'}, DATA), 'where the peace-offering is cooked — the Chamber of the Nazirites (Abba Chanan: while the entrance is open)'),
    ('Mishnah Nazir 6:8; Menachot 91b:1 — the hair under the pot', lambda: nazirite({'ask': 'hair_under_pot'}, DATA), 'under the peace-offering\'s pot (the others fulfill)'),
    ('Temurah 34a:4 — the impure nazirite\'s hair', lambda: nazirite({'ask': 'hair_under_pot', 'which': 'impurity'}, DATA), 'not thrown; the hair buried (the pure\'s burned)'),
    ('Kiddushin 57b:6; Avodah Zarah 74a:3 — the hair', lambda: nazirite({'ask': 'hair'}, DATA), 'holy — forbidden for benefit in any amount; burned'),
    ('Mishnah Menachot 7:2, 3:6; Menachot 46b, 91a — the loaves', lambda: nazirite({'ask': 'loaves'}, DATA), 'loaves and wafers (no poached), ten kav; both indispensable; sanctified by the ram\'s slaughter; with libations for the burnt- and peace-offerings'),
    ('Num 6:19-20; Mishnah 6:9 — the foreleg (Tzav\'s cell CALLED)', lambda: nazirite({'ask': 'foreleg'}, DATA), 'the cooked foreleg, a loaf and a wafer on his palms, waved (the woman too); beside the breast and thigh to the priests after the smoking'),
    ('Mishnah Chullin 10:4 — the foreleg\'s bounds', lambda: nazirite({'ask': 'foreleg_bounds'}, DATA), 'the lower knee joint to the thigh bone\'s protrusion (Mishnah Chullin 10:4)'),
    ('Zevachim 55a:6 — who eats the ram', lambda: nazirite({'ask': 'ram_eaten_by'}, DATA), 'the owner; the foreleg the priest\'s'),
    ('Mishnah Zevachim 5:5 — the guilt-offering (the offering engine CALLED)', lambda: nazirite({'ask': 'asham'}, DATA), 'north; two placements that are four; male priests within the curtains, a day and a night (Mishnah Zevachim 5:5)'),
    ('Mishnah Nazir 6:9; Nazir 46a:2 — permitted after (the running setting)', lambda: nazirite({'ask': 'permitted_after'}, DATA), 'after one offering (the Rabbis; R. Shimon); R. Eliezer after all'),
    ('Nazir 14b-15a — after the term, before the offerings', lambda: nazirite({'ask': 'after_term_before_offerings'}, DATA), 'lashes for impurity, shaving and wine alike (the baraita)'),
    ('Nazir 46b:1 / Menachot 19a:12 — the waving', lambda: nazirite({'ask': 'waving_indispensable'}, DATA), 'not (the Tosefta: with or without palms); Rav: yes'),
    ('Nedarim 18a:3 — a vow on a vow', lambda: nazirite({'ask': 'vow_on_vow'}, DATA), 'takes effect (two terms)'),
    ('Mishnah Nazir 4:1 — the first dissolved', lambda: nazirite({'ask': 'chained_vows', 'which_dissolved': 'first'}, DATA), 'all dissolved'),
    ('Mishnah Nazir 4:1-2 — the wife\'s "and I"', lambda: nazirite({'ask': 'spouse_and_i', 'who_first': 'husband'}, DATA), 'he nullifies hers, his stands'),
    ('Mishnah Nazir 4:5 — after the blood', lambda: nazirite({'ask': 'husband_annuls_after', 'stage': 'blood_sprinkled_purity'}, DATA), 'cannot (R. Akiva: after any slaughter)'),
    ('Mishnah Nazir 4:5 — at the impurity shaving', lambda: nazirite({'ask': 'husband_annuls_after', 'stage': 'impurity_shaving'}, DATA), 'can — a downcast wife'),
    ('Mishnah Nazir 4:3 — nullified without her knowing', lambda: nazirite({'ask': 'nullified_unknown'}, DATA), 'no lashes (R. Yehuda: lashes of rebellion)'),
    ('Mishnah Nazir 4:4 — her animals after nullification', lambda: nazirite({'ask': 'nullified_after_separation', 'whose': 'hers'}, DATA), 'the sin-offering dies, the burnt offered, the peace eaten a day without loaves'),
    ('Mishnah Meilah 3:2 — died with allocated funds', lambda: nazirite({'ask': 'died_with_funds', 'whose': 'hers', 'allocated': True}, DATA), 'the sin\'s to the Dead Sea, the burnt\'s an olah (misuse), the peace\'s a shelamim a day without loaves'),
    ('Mishnah Meilah 3:2 — died with unallocated funds', lambda: nazirite({'ask': 'died_with_funds', 'whose': 'hers', 'allocated': False}, DATA), 'communal gifts'),
    ('Mishnah Nazir 4:6; Mishnah Sotah 3:8 — a father vows his son', lambda: nazirite({'ask': 'father_vows_son'}, DATA), 'a father may (not a mother); the son\'s or relatives\' objection cancels'),
    ('Mishnah Nazir 4:7 — the father\'s funds', lambda: nazirite({'ask': 'shaves_on_fathers_funds', 'when_vowed': 'in_lifetime'}, DATA), 'may (vowed in his father\'s lifetime)'),
    ('Temurah 10a:5 — designated by others', lambda: nazirite({'ask': 'designated_by_others'}, DATA), 'effective (6:21 his means)'),
    ('Mishnah Nazir 5:3 — released by a sage', lambda: nazirite({'ask': 'dissolved_by_sage', 'released': True}, DATA), 'the animal grazes'),
    ('Mishnah Nazir 5:4 — the animal stolen before the vow', lambda: nazirite({'ask': 'vow_in_error', 'event_before': True}, DATA), 'not — an error from the outset (Nachum the Mede)'),
    ('Mishnah Nazir 2:7 — "a son" and a daughter born', lambda: nazirite({'ask': 'conditioned_on_birth', 'form': 'son', 'born': 'daughter'}, DATA), 'not'),
    ('Mishnah Nazir 2:7 — "a child" and a daughter born', lambda: nazirite({'ask': 'conditioned_on_birth', 'form': 'child', 'born': 'daughter'}, DATA), 'a nazirite'),
    ('Mishnah Nazir 2:10 — born after seventy days', lambda: nazirite({'ask': 'two_terms_order', 'born_on_day': 80}, DATA), 'born within seventy days — nothing lost; after — the seventy negated'),
    ('Mishnah Nazir 5:6; Tahorot 4:12 — the doubtful vow', lambda: nazirite({'ask': 'doubtful_vow', 'case': 'turned_back'}, DATA), 'none (lenient; R. Shimon\'s condition)'),
    ('Mishnah Nazir 5:7 — the koy', lambda: nazirite({'ask': 'doubtful_vow', 'case': 'koy'}, DATA), 'all bound (the koy)'),
    ('Mishnah Nazir 8:1 — two doubtful nazirites', lambda: nazirite({'ask': 'two_doubtful'}, DATA), 'ben Zoma\'s procedure (the Rabbis)'),
    ('Mishnah Nazir 8:2; Nazir 60a:6 — the doubtful leper', lambda: nazirite({'ask': 'doubtful_leper'}, DATA), 'sixty days to sacred food, a hundred and twenty to wine and the dead'),
    ('Nazir 41a:3; Yevamot 5a:8 — the leper-nazirite shaves (the metzora engine CALLED)', lambda: nazirite({'ask': 'leper_nazirite_shaves'}, DATA), 'shaves with a razor — the leper\'s command overrides (metzora: commanded_shave_overrides)'),
    ('Shevuot 22b:8 — the oath on a seed', lambda: nazirite({'ask': 'oath_on_seed'}, DATA), 'an open dilemma (Rav Ashi)'),
    ('Bava Kamma 91b:12 / Taanit 11a:16 — a sinner or holy', lambda: nazirite({'ask': 'sinner'}, DATA), 'a sinner (HaKappar) / holy (R. Elazar) — a dispute'),
    ('Mishnah Nazir 6:5 — the exemptions', lambda: nazirite({'ask': 'exemptions'}, DATA), 'the vine none; impurity and shaving: the met mitzvah, the leper\'s shaving'),
    ('Mishnah Nazir 6:11 — impure after the first blood', lambda: nazirite({'ask': 'impure_after_first_blood'}, DATA), 'brings the rest and is pure (the Rabbis); R. Eliezer negates all'),
    ('Mishnah Nazir 6:10 — shaved on an invalid offering', lambda: nazirite({'ask': 'shaved_on_invalid'}, DATA), 'the shaving invalid (R. Shimon: that one alone fails); one of three valid — valid'),
    ('Mishnah Nazir 3:6 — vowed abroad', lambda: nazirite({'ask': 'vowed_abroad'}, DATA), 'Hillel: all again (Shammai: thirty)'),
    # F6 — the blessing
    ('Mishnah Sotah 7:6; Tamid 7:2 — in the Temple', lambda: blessing({'ask': 'form', 'place': 'temple'}, DATA), 'one blessing; the Name as written; the hands above the head (the High Priest not above the frontplate)'),
    ('Mishnah Sotah 7:6 — in the province', lambda: blessing({'ask': 'form', 'place': 'province'}, DATA), 'three blessings with amen; the substitute name; the hands at the shoulders'),
    ('Sotah 33b:3, 38a:2 — the language', lambda: blessing({'ask': 'language'}, DATA), 'the holy tongue (so/so)'),
    ('Mishnah Megillah 4:7 — blemished hands (the priesthood CALLED)', lambda: blessing({'ask': 'who_blesses', 'who': 'blemished_hands'}, DATA), 'does not lift his hands (Megillah 4:7)'),
    ('Taanit 26b:16 — the drunk priest', lambda: blessing({'ask': 'who_blesses', 'who': 'drunk'}, DATA), 'may not (the nazirite\'s juxtaposition)'),
    ('Mishnah Megillah 4:6 — a minor', lambda: blessing({'ask': 'who_blesses', 'who': 'minor'}, DATA), 'not'),
    ('Mishnah Megillah 4:3 — the quorum', lambda: blessing({'ask': 'quorum'}, DATA), 'ten'),
    ('Sotah 38a:12 — who is blessed', lambda: blessing({'ask': 'who_is_blessed'}, DATA), 'all Israel — converts, women, freed slaves'),
    ('Mishnah Megillah 4:10 — translated?', lambda: blessing({'ask': 'translated'}, DATA), 'read, not translated'),
    ('Sotah 38b:4; Menachot 44a:18 — the three commands', lambda: blessing({'ask': 'three_commands'}, DATA), 'so you shall bless; say to them; put My name'),
    ('Chullin 49a:16 — the priests blessed', lambda: blessing({'ask': 'priests_blessed'}, DATA), 'by Heaven (I will bless them)'),
    ('Sifrei 42:2; Berakhot 20b; Niddah 70b — the face lifted', lambda: blessing({'ask': 'face_lifted'}, DATA), 'when they do His will (the Sifrei) / beyond the letter (Berakhot 20b) / before the sentence (Niddah 70b) — three reconciliations'),
    ('Num 6:24-26 — the counts (computed)', lambda: blessing({'ask': 'counts'}, DATA), '3, 5, 7 words; 15, 20, 25 letters; the Name thrice'),
    ('Sotah 38a:9; Mishnah 7:6 — the Name by place', lambda: blessing({'ask': 'name'}, DATA), 'the Name in the Temple, the substitute in the province'),
    # F7 — the wagons
    ('Num 7:1; Sifrei 44:1 — the day', lambda: wagons({'ask': 'day'}, DATA), 'the erection\'s day — the day-stack (Sifrei 44:1; Shabbat 87b): RETROGRADE'),
    ('Num 7:3 — the numbers (the parser after the construct rule)', lambda: wagons({'ask': 'numbers'}, DATA), '6 wagons, 12 oxen; a wagon for two princes, an ox for one (the parser: [6, 12, 2, 1])'),
    ('Sifrei 45:1 — covered', lambda: wagons({'ask': 'covered'}, DATA), 'covered (Rebbi — Onkelos)'),
    ('Num 7:4-5; Sifrei 45:1 — accepted when told', lambda: wagons({'ask': 'accepted'}, DATA), 'not accepted until told (7:4-5)'),
    ('Num 7:6-9; Sifrei 46:1 — the distribution', lambda: wagons({'ask': 'distribution'}, DATA), 'as Moses saw fit: Gershon 2 and 4, Merari 4 and 8, Kohath none — on the shoulder'),
    ('Sifrei 46:2; Sotah 35a:22 — the shoulder', lambda: wagons({'ask': 'shoulder'}, DATA), 'David\'s error and return (the flow reversed); the song from "they carry"'),
    ('Num 7:1; Menachot 57b; Sanhedrin 16b — the anointing (the incense engine CALLED)', lambda: wagons({'ask': 'anointing'}, DATA), 'Moses\' vessels by anointing (the liquid measures in and out, the dry inside — R. Yoshiya); the generations\' by service'),
    # F8 — the dedication
    ('Zevachim 101b:6 — the first day', lambda: dedication({'ask': 'first_day'}, DATA), 'the anointing day = the erection = 1 Nisan: three goats on one day (Zevachim 101b)'),
    ('Sifrei 47:1 — the order (computed)', lambda: dedication({'ask': 'order'}, DATA), 'by the journeying = the camp\'s order (computed = 2:3-31), not by birth; Reuben\'s protest'),
    ('Num 7:11; Moed Katan 9a — one prince per day', lambda: dedication({'ask': 'per_day'}, DATA), 'one prince per day — twelve dues from the anointing day, the Sabbath overridden (Moed Katan 9a)'),
    ('Sifrei 53:1 — the same day', lambda: dedication({'ask': 'same_day'}, DATA), '7:84 = 7:88 — on the day of its anointing / after: the same day (Sifrei 53:1)'),
    ('Num 7:13; Sifrei 49:1 — the dish (the shekel CALLED)', lambda: dedication({'ask': 'dish'}, DATA), '130 and 70 by the sanctuary shekel (Exod 30:13\'s twenty gerah — the sela)'),
    ('Num 7:14, 7:86; Sifrei 55:1 — the pan (M-26)', lambda: dedication({'ask': 'pan'}, DATA), 'ten of gold weighed in silver — 120 = 12 x 10 decides (M-26)'),
    ('Menachot 8a:13 — full', lambda: dedication({'ask': 'full'}, DATA), 'a full tenth sanctifies (R. Yosei: unless meant to add)'),
    ('Menachot 8b:5; Zevachim 88a:6 — the bowls', lambda: dedication({'ask': 'bowls_sanctify_dry'}, DATA), 'yes (Shmuel)'),
    ('Chagigah 23b:7 / Pesachim 19a:8 — the pan joins', lambda: dedication({'ask': 'vessel_joins'}, DATA), 'Torah law (R. Chanin); R. Yochanan rabbinic'),
    ('Num 7:15-17; Sifrei 50:1 — the animals (the offering engine CALLED)', lambda: dedication({'ask': 'animals'}, DATA), 'one bull, one ram, one lamb (burnt); one goat (sin); two oxen, five, five, five (peace) — none like it; its own year'),
    ('Mishnah Parah 1:3 — thirteen months', lambda: dedication({'ask': 'animal_age', 'months': 13}, DATA), 'neither (a palgas)'),
    ('Sifrei 51:1; Menachot 92b:7 — the goat', lambda: dedication({'ask': 'goat'}, DATA), 'for the grave of the depths; leaning — R. Yehuda yes (R. Shimon the idolatry goats)'),
    ('Sifrei 51:1; Menachot 50a — the four exceptions', lambda: dedication({'ask': 'exceptions'}, DATA), 'the Sabbath overridden; an individual\'s incense; a sin-offering not for a sin; one of each'),
    ('Moed Katan 9a:11-12 — the Sabbath', lambda: dedication({'ask': 'sabbath'}, DATA), 'overridden — the days continuous (Moed Katan 9a)'),
    ('Num 7:84-88 — the totals (computed)', lambda: dedication({'ask': 'totals'}, DATA), '2400 = 12 x (130 + 70); 120 = 12 x 10; 12/12/12/12; 24/60/60/60 — computed'),
    ('Sifrei 55:1-57:1 — each credited', lambda: dedication({'ask': 'credited'}, DATA), 'each credited with all twelve (Sifrei 55:1-57:1)'),
    ('Sifrei 54:1 — the weights', lambda: dedication({'ask': 'weights'}, DATA), 'Temple vessels weigh the same singly and together (54:1)'),
    # F9 — the Voice
    ('Num 7:89 — the reflexive (the points)', lambda: voice({'ask': 'reflexive'}, DATA), 'the Voice speaking ITSELF (the hitpael by the points); Onkelos both verbs'),
    ('Sifrei 58:1 — the third verse (I13)', lambda: voice({'ask': 'third_verse'}, DATA), 'Lev 1:1 against Exod 25:22 reconciled by 7:89 (I13)'),
    ('Yoma 4b:8 — who heard', lambda: voice({'ask': 'who_heard'}, DATA), 'Moses alone at the Tent (Yoma 4b); all at Sinai'),
    ('Sifrei 58:2 — the great voice', lambda: voice({'ask': 'great_voice'}, DATA), 'not a low voice — the great voice of Sinai (58:2)'),
    ('Yoma 4b; Sukkah 5a — the door', lambda: voice({'ask': 'door'}, DATA), 'the Voice at the door (Yoma 4b; Sukkah 5a)'),
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
    print('\nNASO: %d/%d cells; the scene %s; the narrative %s' % (ok, len(CASES), SCENE, NARRATIVE))
    print('the exclusions census (to Moses and to Aaron, Exodus-Numbers): %d' % TO_MOSES_AND_AARON)
    sys.exit(0 if ok == len(CASES) else 1)

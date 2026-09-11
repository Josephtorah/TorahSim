#!/usr/bin/env python3
# NUM 16:1-18:32 — KORACH: THE REBELLION, THE PLAGUE AND THE STAFFS, THE PRIESTS' AND THE LEVITES' WATCH, GIFTS AND TITHE (THE NUMBERS
# WALK sitting 5b, 2026-09-10; World/step9/NUMBERS_WALK.md "Sitting 5b"). The fifth Numbers portion compiled after its walk, on the
# owner's ruling READ THEN COMPILE: the parser taught THE DEFINITE NUMERAL AT THE HEAD OF A COMPOUND (16:35's "THE fifty and two hundred"),
# the article on the hundreds-word, the plural unit noun and the definite one's accent gate at this sitting (census_probes.py 130/130
# after seven rows failed first); the firstborn's redemption CALLED from Bamidbar (with its row zar_who_served for the stranger's death),
# the shekel's seat from the incense engine, the ass from the Passover engine, the devotions from the temurah engine, the breast and thigh
# from the tzav engine, the terumah's measure from the naso engine, the hundred-and-one from the holiness engine, the exclusion by sin from
# the inheritance engine, the household's eaters from the priesthood engine, the peace offering's row from the offerings engine; the
# rebellion, the plague and the staffs on the tape with two one-day timers on an undated stretch. Five motions of the deliverable rule,
# the wrap the sixth; every cell cites its source; every token probed (zero-report law); effects on every cell (the effects law). Reading
# ledgers: the three logic/oral_triage/num_{16,17,18}_*_2026-09-10.md; the exam's docket: num_16_18_korach_exam_2026-09-10.md (316 rows —
# 195 LAW, 46 DERIVATION, 42 DISPUTE, 33 CONTEXT; 94 credited).

# ---- THE HONEST-PAIRING GUARD ----------------------------------------------------------------------------
import os as _os, sys as _sys
_sys.path.insert(0, _os.path.dirname(_os.path.abspath(__file__)))
from compile_guards import check_honest_pairing as _chp
_P = _os.path.abspath(__file__)
GUARDED = _chp(_P, 'CASES', 2)
assert GUARDED == 155, ('the guard counted %d expectations, the tripwire holds 155' % GUARDED)   # the guard's own count on the first graded run (155/155, the scene and the narrative matching their predictions first run)
print('guard: %d expectations checked, every one a literal from the answer sheet [honest-pairing guard satisfied]' % GUARDED)
import sqlite3, sys, io, re, contextlib
from fractions import Fraction
import effects_layer as FX
import world_engine as WE
import cold_run_bamidbar as BM                   # THE EDGE: korach -> bamidbar CALL, reference (18:15-16's redemption; 18:7's zar_who_served row; 18:5's no-more-wrath)
import cold_run_incense_shekel as IS             # THE EDGE: korach -> incense_shekel CALL, reference (18:16's twenty gerah — the unit's seat)
import cold_run_pesach as PS                     # THE EDGE: korach -> pesach CALL, reference (18:15's firstling of an ass)
import cold_run_temurah as TM                    # THE EDGE: korach -> temurah CALL, reference (18:14's devotions; 18:17's not-redeemed beside the tithe)
import cold_run_tzav as TZ                       # THE EDGE: korach -> tzav CALL, reference (18:18's breast and thigh; 18:1's Eli)
import cold_run_naso as NS                       # THE EDGE: korach -> naso CALL, reference (18:12's terumah measure — naso's row)
import cold_run_holiness_b as HB                 # THE EDGE: korach -> holiness_b CALL, reference (18:29's hundred and one)
import cold_run_zelophehad as ZL                 # THE EDGE: korach -> zelophehad CALL, reference (18:20-24's exclusion beside the exclusion by sin)
import cold_run_priesthood as PR                 # THE EDGE: korach -> priesthood CALL, reference (18:11, 18:13's household eaters)
import cold_run_offerings as OF                  # THE EDGE: korach -> offerings CALL, reference (18:18's peace offering row)
import cold_run_chatat as CH                     # THE EDGE: korach -> chatat CALL, reference (18:9's 'every sin offering of theirs' — the most-holy list; 16:26's 'their sins' the homograph)
import cold_run_minchah as MN                    # THE EDGE: korach -> minchah CALL, reference (18:9's 'every meal offering of theirs'; 16:15's 'their offering' Cain's word, the homograph)
import cold_run_moadim as MO                     # THE EDGE: korach -> moadim CALL, reference (18:13's first fruits — the two loaves' precedence, Menachot 84b)
import cold_run_vayikra5 as V5                   # THE EDGE: korach -> vayikra5 CALL, reference (18:9's 'every guilt offering of theirs')
import cold_run_yovel as YV                      # THE EDGE: korach -> yovel CALL, reference (18:16's 'by your valuation' — Lev 27:25's shekel at its second seat; the tithe VIA temurah)

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

def seats_of_stem(stem, books=('Num',)):
    out = []
    for b, c, v, he in db.execute("SELECT v.book, v.chapter, v.verse, w.he FROM words w JOIN verses v ON w.verse_id=v.id WHERE v.book IN (%s) ORDER BY v.id, w.idx" % ','.join('?' * len(books)), tuple(books)):
        if strip(he).endswith(stem): out.append('%s %d:%d' % (b, c, v))
    return out

def seats_of(tok, books=('Gen', 'Exod', 'Lev', 'Num', 'Deut')):
    out = []
    for b, c, v, he in db.execute("SELECT v.book, v.chapter, v.verse, w.he FROM words w JOIN verses v ON w.verse_id=v.id WHERE v.book IN (%s) ORDER BY v.id, w.idx" % ','.join('?' * len(books)), tuple(books)):
        if strip(he) == tok: out.append('%s %d:%d' % (b, c, v))
    return out

# ---- zero-report probes: the span's load-bearing tokens ---------------------------------------------------
PROBES = [
    ('ויקח',     16, 1,  'and he took — no object'), ('קרח', 16, 1, 'Korach'), ('חמשים', 16, 2, 'fifty'), ('ומאתים', 16, 2, 'and two hundred'),
    ('רב',       16, 3,  'too much'), ('לכם', 16, 3, 'for you'), ('בקר', 16, 5, 'in the morning'), ('מחתות', 16, 6, 'censers'), ('מחר', 16, 7, 'tomorrow'),
    ('המעט',     16, 9,  'is it too little'), ('נעלה', 16, 12, 'we will (not) go up'), ('תנקר', 16, 14, 'will you put out'), ('ויחר', 16, 15, 'it was hot'),
    ('חמור',     16, 15, 'an ass'), ('מחתתו', 16, 17, 'his censer'), ('הבדלו', 16, 21, 'separate yourselves'), ('כרגע', 16, 21, 'in a moment'),
    ('הרוחת',    16, 22, 'the spirits'), ('העלו', 16, 24, 'get up'), ('סורו', 16, 26, 'turn aside'), ('בריאה', 16, 30, 'a creation'),
    ('ותבקע',    16, 31, 'and it split'), ('ותפתח', 16, 32, 'and it opened'), ('לקרח', 16, 32, 'who belonged to Korach'), ('שאלה', 16, 33, 'to Sheol'),
    ('ואש',      16, 35, 'and fire'), ('החמשים', 16, 35, 'THE fifty'), ('מקריבי', 16, 35, 'who offered'),
    ('אלעזר',    17, 2,  'Eleazar'), ('רקעי', 17, 3, 'beaten'), ('פחים', 17, 3, 'plates'), ('זכרון', 17, 5, 'a memorial'), ('זר', 17, 5, 'a stranger'),
    ('המתם',     17, 6,  'you have killed'), ('הקצף', 17, 11, 'the wrath'), ('הנגף', 17, 11, 'the plague'), ('המחתה', 17, 11, 'the censer'),
    ('וירץ',     17, 12, 'and he ran'), ('ויכפר', 17, 12, 'and he atoned'), ('ותעצר', 17, 13, 'and it was stayed'), ('המגפה', 17, 13, 'the plague'),
    ('ארבעה',    17, 14, 'fourteen thousand (the head)'), ('מטה', 17, 17, 'a staff'), ('שנים', 17, 17, 'twelve (the head)'), ('אהרן', 17, 18, 'Aaron'),
    ('יפרח',     17, 20, 'shall bud'), ('והשכתי', 17, 20, 'and I will make abate'), ('וינח', 17, 22, 'and he laid'), ('ממחרת', 17, 23, 'on the morrow'),
    ('ויצץ',     17, 23, 'and it blossomed'), ('ציץ', 17, 23, 'a blossom — the frontplate\'s word'), ('שקדים', 17, 23, 'almonds'),
    ('למשמרת',   17, 25, 'for a keeping'), ('לאות', 17, 25, 'for a sign'), ('מרי', 17, 25, 'rebellion'), ('גוענו', 17, 27, 'we expire'), ('הקרב', 17, 28, 'who comes near'),
    ('עון',      18, 1,  'the iniquity'), ('המקדש', 18, 1, 'the sanctuary'), ('וילוו', 18, 2, 'and they shall be joined'), ('וישרתוך', 18, 2, 'and serve you'),
    ('אתם',      18, 3,  'you (both they and you)'), ('וזר', 18, 4, 'and a stranger'), ('קצף', 18, 5, 'wrath'), ('מתנה', 18, 6, 'a gift'),
    ('לפרכת',    18, 7,  'the veil'), ('והזר', 18, 7, 'and the stranger'), ('יומת', 18, 7, 'shall be put to death'), ('תרומתי', 18, 8, 'My terumot'),
    ('למשחה',    18, 8,  'for anointing'), ('הקדשים', 18, 9, 'the most holy'), ('האש', 18, 9, 'the fire'), ('ולבנתיך', 18, 11, 'and to your daughters'),
    ('יצהר',     18, 12, 'fresh oil — Izhar'), ('חרם', 18, 14, 'devoted'), ('פטר', 18, 15, 'opens'), ('פדה', 18, 15, 'redeem'), ('תפדה', 18, 15, 'you shall redeem'),
    ('מבן',      18, 16, 'from a son of'), ('חדש', 18, 16, 'a month'), ('חמשת', 18, 16, 'five'), ('שקלים', 18, 16, 'shekels'), ('עשרים', 18, 16, 'twenty'), ('גרה', 18, 16, 'gerah'),
    ('כחזה',     18, 18, 'as the breast'), ('מלח', 18, 19, 'salt'), ('תנחל', 18, 20, 'you shall inherit'), ('חלקך', 18, 20, 'your portion'),
    ('מעשר',     18, 21, 'tithe'), ('חלף', 18, 21, 'in exchange'), ('המעשר', 18, 26, 'the tithe'), ('ונחשב', 18, 27, 'and it shall be reckoned'),
    ('הגרן',     18, 27, 'the threshing floor'), ('היקב', 18, 27, 'the winepress'), ('חלבו', 18, 29, 'its best'), ('מקדשו', 18, 29, 'its hallowed part'),
    ('מקום',     18, 31, 'place'), ('שכר', 18, 31, 'wage'), ('תחללו', 18, 32, 'you shall (not) profane'), ('תמותו', 18, 32, 'you shall (not) die'),
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
C250 = [N('Num', 16, 2)[0], N('Num', 16, 17)[0], N('Num', 16, 35)[0]]
assert C250 == [250, 250, 250], ('the two hundred and fifty at three seats — 16:35 the definite numeral at the head of a compound', C250)
PLAGUE = N('Num', 17, 14)[0]; assert PLAGUE == 14700, PLAGUE
STAFFS = N('Num', 17, 17); STAFFS_21 = N('Num', 17, 21); assert STAFFS == [12] and STAFFS_21 == [1, 1, 12], (STAFFS, STAFFS_21)
REDEMPTION = N('Num', 18, 16); assert REDEMPTION == [5, 20], REDEMPTION
ONE_ONE = N('Num', 16, 15); assert ONE_ONE == [1, 1], ONE_ONE
TITHE_OF_TITHE = Fraction(1, 10) * Fraction(1, 10); assert TITHE_OF_TITHE == Fraction(1, 100)
# THE NO-MORE-WRATH CLAUSE: 18:5 against 1:53 — the token sets from 'and not' to 'Israel' (computed; sitting 5's crown, M-23 exemplar 15)
def clause(ch, vs, first, last):
    ws = verse_text(ch, vs).split(); return ws[ws.index(first):ws.index(last) + 1]
WRATH_153 = clause(1, 53, 'ולא', 'ישראל'); WRATH_185 = clause(18, 5, 'ולא', 'ישראל')
WRATH_ADDED = [w for w in WRATH_185 if w not in WRATH_153]; WRATH_DROPPED = [w for w in WRATH_153 if w not in WRATH_185]
assert WRATH_ADDED == ['עוד'], (WRATH_ADDED, WRATH_DROPPED)    # 'no MORE wrath' — the one token added; 'the congregation of' dropped
FLOOR_SEATS = seats_of_stem('גרן'); assert {'Num 15:20', 'Num 18:27', 'Num 18:30'} <= set(FLOOR_SEATS), FLOOR_SEATS   # 15:20's pointer and its payment on the floor-word — the STEM (15:20 'goren' bare in the construct, 18:27 'the goren', 18:30 'goren' again): the first run's bare-token census found 18:27 alone, the hand had typed the reading's three seats onto one form
TRIAD = [w for w in verse_text(18, 12).split() if w in ('יצהר', 'תירוש', 'ודגן')]; assert TRIAD == ['יצהר', 'תירוש', 'ודגן'], TRIAD   # oil, wine, grain — the triad reversed at this seat alone
_BYV = {}
for _b, _c, _v, _he in db.execute("SELECT v.book, v.chapter, v.verse, w.he FROM words w JOIN verses v ON w.verse_id=v.id ORDER BY v.id, w.idx"):
    _BYV.setdefault((_b, _c, _v), []).append(strip(_he))
COVENANT_OF_SALT = sorted('%s %d:%d' % k for k, ws in _BYV.items() if any(ws[i].endswith('ברית') and ws[i + 1] == 'מלח' for i in range(len(ws) - 1)))
assert COVENANT_OF_SALT == ['2Chr 13:5', 'Num 18:19'], COVENANT_OF_SALT   # the phrase's two seats in the Bible — Aaron's and David's (the first run's LIKE on the pointed bytes found none: the census runs on the stripped tokens)
SWALLOWED_NAMES = verse_text(16, 32).split(); assert 'לקרח' in SWALLOWED_NAMES and 'קרח' not in SWALLOWED_NAMES, SWALLOWED_NAMES   # 'who belonged TO Korach' — Korach not named among the swallowed
ADDS_KORACH = 'קרח' in verse_text(26, 10).split(); assert ADDS_KORACH   # 26:10 adds 'and Korach'

# ---- THE CALLEES, measured live at import (the edges) ----
BM_RATE = BM.levites({'ask': 'rate'}, BM.DATA)[0]; BM_AGE = BM.levites({'ask': 'age', 'age_days': 31}, BM.DATA)[0]; BM_MEANS = BM.levites({'ask': 'means', 'means': 'coins'}, BM.DATA)[0]
BM_OWNER = BM.levites({'ask': 'owner', 'owner': 'priest', 'animal': 'donkey'}, BM.DATA)[0]; BM_PARTNER = BM.levites({'ask': 'partner'}, BM.DATA)[0]; BM_ONE_LAMB = BM.levites({'ask': 'one_lamb'}, BM.DATA)[0]
ZAR = BM.DATA['zar_who_served']                                                   # THE ROW ON FILE SINCE 1b — read, never retyped
IS_SEATS = IS.shekel('twenty_gerah')['v']; assert 'Num 18:16' in IS_SEATS, IS_SEATS   # the unit's five seats, this portion's among them
PS_DONKEY = PS.firstborn({'kind': 'donkey'}, {})[0]; PS_CAESAREAN = PS.firstborn({'kind': 'caesarean_animal'}, {})[0]
TM_DEV = TM.devote('unspecified_destination')['v']; TM_DEV_STATUS = TM.devote('status')['v']; TM_DEV_FB = TM.devote('firstborn')['v']; TM_DEV_PRIESTS = TM.devote('priests_devotions')['v']; TM_TITHE = TM.redeem('animal_tithe')['v']
TZ_BT = TZ.dues_machine({'ask': 'breast_thigh'}, {})[0]; TZ_ELI = TZ.dues_machine({'ask': 'eli_violation'}, {})[0]
NS_TM = NS.restitution({'ask': 'terumah_measure'}, NS.DATA)[0]           # naso's CELL — the floor (Mishnah Terumot 4:5); the ROW terumah_measure is THIS runner's (below): the first run's KeyError read — Shelach carried the placeholder copy marked OWED, naso never held the row
HB_101 = HB.orlah('ratio')['v']['the_priestly_gifts']; assert HB_101 == 101, HB_101
ZL_EXCL = ZL.inheritance_order({'ask': 'excluded'}, ZL.DATA)[0]
PR_HOUSE = PR.holy_food('household', who='wife')['v']; PR_DAUGHTER = PR.holy_food('daughter_to_stranger')['v']; PR_STRANGER = PR.holy_food('stranger')['v']
OF_SHELAMIM = OF.dispatch('shelamim'); assert isinstance(OF_SHELAMIM, dict) and 'place' in OF_SHELAMIM, type(OF_SHELAMIM)
CH_SIN = CH.domain({'intent': 'unwitting'})['v']                                 # 18:9's sin offering — the chatat engine's own object (the unwitting arm)
MN_SINNER = MN.adjuncts('sinner')                                                 # 18:9's meal offering — the sinner's (no oil, no frankincense): the priests eat its remainder (Menachot 73a)
MO_LOAVES = MO.two_loaves(); MO_LOAVES = (MO_LOAVES['v'] if 'v' in MO_LOAVES else sorted(MO_LOAVES)) if isinstance(MO_LOAVES, dict) else MO_LOAVES   # 18:13's first fruits — the two loaves precede (Menachot 84b:6); the callee's cell is a dict of cells (the first run's KeyError read)
V5_ASHAM = V5.pointers('asham_procedure', V5.DATA); V5_ASHAM = V5_ASHAM['v'] if isinstance(V5_ASHAM, dict) else V5_ASHAM   # 18:9's guilt offering — the Lev 5 engine's own
YV_SHEKEL = YV.field_valuation(49)['shekel']['v']; assert YV_SHEKEL == 20, YV_SHEKEL   # 18:16 'by your valuation... twenty gerah' — Lev 27:25's definition at its second seat
_W0 = WE.World(era='the calendar', epoch='exodus'); DAY_480 = _W0.clock.day_in('exodus', 2, 5, 9); assert DAY_480 == 480 and _W0.clock.eras['exodus'].date(DAY_480 + 1) == (2, 5, 10)

# =====================================================================
# Motion 2 — THE DATA: the parameter rows (the tradition's own vocabulary; the running setting first)
# =====================================================================
DATA = {
    'korach_death_mode': {'value': 'open', 'settings': {'open': "the ink: 16:32 'every person who belonged to Korach' names the men who were his, not Korach; 26:10 adds 'and Korach' — the tape's put_to_death on Korach carries this row OPEN", 'plague': "R. Yochanan: neither swallowed nor burned — he died in the plague (Sanhedrin 110a:13)", 'burned_and_swallowed': "the baraita (the outside teaching): both — 26:10 'swallowed them with Korach', 16:35 the fire (Sanhedrin 110a:14)"}, 'source': 'Num 16:32, 16:35, 26:10; Sanhedrin 110a:13-14'},
    'korach_share': {'value': 'no_share_R._Akiva', 'settings': {'no_share_R._Akiva': "'the earth closed upon them' — this world; 'they perished from among the assembly' — the World-to-Come (Mishnah Sanhedrin 10:3)", 'has_share_R._Eliezer': "'the LORD kills and makes alive; He lowers to the grave and raises' (1 Sam 2:6)", 'lost_and_found_R._Yehuda_b._Beteira': "a lost item sought and found (Ps 119:176; Sanhedrin 109b:12; Tosefta Sanhedrin 13:9)"}, 'source': 'Mishnah Sanhedrin 10:3; Sanhedrin 108a, 109b-110a'},
    'earth_mouth': {'value': 'created_at_twilight', 'settings': {'created_at_twilight': 'the mouth of the earth the first of the ten things created on the Sabbath eve at twilight (Mishnah Avot 5:6; Pesachim 54a)', 'brought_near': "Rava: nothing new under the sun — Moses asked that Gehenna's opening be brought near (Sanhedrin 110a:16; Nedarim 39b:3)"}, 'source': 'Num 16:30; Mishnah Avot 5:6'},
    'sons_of_korach': {'value': 'did_not_die', 'settings': {'did_not_die': "'and the sons of Korach did not die' (26:11) — a place fortified for them (Sanhedrin 110a); the eleven Psalm headings"}, 'source': 'Num 26:11'},
    'dispute_not_for_heaven': {'value': 'korach', 'settings': {'korach': "a dispute not for Heaven's sake — Korach and all his congregation; for Heaven's sake — Hillel and Shammai (Mishnah Avot 5:17)"}, 'source': 'Mishnah Avot 5:17'},
    'maintaining_a_dispute': {'value': 'prohibition_Rav', 'settings': {'prohibition_Rav': "one who perpetuates a dispute violates a prohibition — 'he will not be like Korach' (17:5; Sanhedrin 110a:6)", 'leprosy_R._Ashi': 'R. Ashi: he is smitten with leprosy (Sanhedrin 110a)'}, 'source': 'Num 17:5; Sanhedrin 110a:6'},
    'wives': {'value': 'on_saved_by_his_wife', 'settings': {'on_saved_by_his_wife': "Rav: On's wife gave him wine and sat at the entrance — he was spared (Sanhedrin 109b:16); Korach's wife incited him (110a)"}, 'source': 'Sanhedrin 109b:15-16, 110a'},
    'incense_stays_plague': {'value': 'atones_for_slander', 'settings': {'atones_for_slander': 'incense atones — for malicious speech, the private for the private (Yoma 44a:5; Arakhin 16a:19; Zevachim 88b:10); the angel of death gave Moses the remedy (Shabbat 89a:2)'}, 'source': 'Num 17:12-13'},
    'staff_hidden_with': {'value': 'the_ark_the_jar_the_oil', 'settings': {'the_ark_the_jar_the_oil': "when the ark was sequestered, the anointing oil, the jar of manna, Aaron's staff with its almonds and blossoms and the Philistines' chest went with it (Horayot 12a:1; Keritot 5b:16; Yoma 52b:15 — Josiah)"}, 'source': 'Num 17:25; Exod 16:33-34'},
    'levite_at_another_work': {'value': 'death_by_heaven', 'settings': {'death_by_heaven': "a Levite at the priests' work or at another Levite's work is liable to death by Heaven; the song and the gates (Arakhin 11b)"}, 'source': 'Num 18:3; Arakhin 11b'},
    'zar_who_served': {'value': 'bamidbar_row_by_call', 'settings': {'bamidbar_row_by_call': "the row is Bamidbar's (1:51's clause) — read live: %s (%s)" % (ZAR['value'], '; '.join(ZAR['settings'].values())[:160])}, 'source': 'Num 18:7; Mishnah Sanhedrin 9:6; Sanhedrin 83b:4, 84a:13'},
    'genealogy_chamber': {'value': 'chamber_of_hewn_stone', 'settings': {'chamber_of_hewn_stone': "'within the veil' — the chamber where the great court judged the priesthood's genealogy: the disqualified in black, the fit in white (Mishnah Middot 5:4; Sifrei 116:2)"}, 'source': 'Num 18:7'},
    'the_twenty_four': {'value': {'sanctuary': ['the sin offering', 'the guilt offering', 'the communal peace offerings', 'the bird sin offering', 'the doubtful guilt offering', "the leper's log of oil", 'the two loaves', 'the showbread', 'the remainder of the meal offerings', "the omer's remainder", "the burnt offering's hide", 'the wave-breast and the thigh'],
                                  'borders': ['terumah', 'the terumah of the tithe', 'challah', 'the first fruits', 'the first shearing', 'the shoulder, the cheeks and the maw', 'the firstborn of man', 'the firstborn of a clean beast', 'the firstling of an ass', 'devotions', 'the field of holding', "the proselyte's theft"]},
                       'settings': {'twelve_and_twelve': "twenty-four gifts by a generalization, a detail and a covenant of salt (Chullin 133b:11; Bava Kamma 110b; Sifrei 119:1-2: twelve in the sanctuary, twelve in the borders)"}, 'source': 'Num 18:8-19'},
    'betrothed_eats': {'value': 'decree_not_until_the_canopy', 'settings': {'decree_not_until_the_canopy': "a court that convened after them said: not until she enters the canopy (Mishnah Ketubot 5:3; Ketubot 57b-58a: the cup and the simpon — the defect)", 'torah_eats': "'every clean one in your house' twice — the betrothed daughter of an Israelite eats (Sifrei 117:2, R. Yochanan b. Bag Bag's a-fortiori; Mishnah Ketubot 5:2 at the time arrived)"}, 'source': 'Num 18:11, 18:13; Sifrei 117:2 — R. Yehudah in Netzivim: the decree over the a-fortiori'},
    'terumah_measure': {'value': {'generous': Fraction(1, 40), 'average': Fraction(1, 50), 'stingy': Fraction(1, 60)}, 'settings': {'forty_fifty_sixty': "Mishnah Terumot 4:3 — the generous one-fortieth, the average one-fiftieth, the stingy one-sixtieth; the sixtieth valid, the sixty-first again; the floor: some must remain common (4:5 — naso's cell restitution(terumah_measure) CALLED: %s)" % NS_TM, 'beit_shammai_thirty': 'Beit Shammai: one-thirtieth (Mishnah Terumot 4:3)'}, 'source': "Num 18:12, 18:29 — NO MEASURE IN THE INK; 15:20's pointer: Shelach's challah cell carried a placeholder copy marked OWED to this compile — the row's home is here"},
    'devotion_default': {'value': 'temurah_row_by_call', 'settings': {'temurah_row_by_call': "temurah's arm read live: %s" % TM_DEV, 'four_authorities': 'R. Yossi HaGelili — the priests (18:14); R. Yehudah b. Beteira — Temple maintenance (27:28); R. Yehudah b. Bava — the priests; R. Shimon — Heaven: four authorities on one pair of verses (Sifrei 117:3; Mishnah Arakhin 8:6)'}, 'source': 'Num 18:14; Lev 27:21, 27:28'},
    'redemption_means': {'value': 'movable_not_writs', 'settings': {'movable_not_writs': 'general-particular-general on the redemption money: movable property, not bondsmen, writs or land (Sifrei 118:1; Mishnah Bekhorot 8:8)', 'rebbi_writs_only': 'Rebbi: writs only excluded (Sifrei 118:1; Bekhorot 51a:10)'}, 'source': 'Num 18:16'},
    'one_spilling': {'value': 'one_spilling_R._Yoshiyah', 'settings': {'one_spilling_R._Yoshiyah': "'they are consecrated' — the tithe and the paschal lamb take one spilling like the firstborn (Sifrei 118:1; Mishnah Zevachim 5:8)", 'the_fats_R._Yitzchak': 'R. Yitzchak: the fats are equated (Sifrei 118:1)'}, 'source': 'Num 18:17'},
    'exclusion_table': {'value': ['priests (18:20)', 'Levites (18:23)', 'bondsmen and proselytes (26:55)', 'the two of uncertain sex (26:54)'], 'settings': {'four_clauses': "the set carved from 26:53's apportionment by four clauses (Sifrei 119:1); R. Meir: priests and Levites do not confess, R. Yosei: the Levitical cities (Mishnah Ma'aser Sheni 5:14)"}, 'source': 'Num 18:20, 18:23; 26:53-55'},
    'tithe_recipient': {'value': 'levite', 'settings': {'levite': "'to the Levites you shall speak' (18:26) — R. Akiva; 'in every place' excludes the priest (Yevamot 86b:1-2)", 'priest_too': "R. Eliezer: the priests are called Levites in twenty-four places; Ezra's penalty gave the tithe to the priests (Yevamot 86a-b)"}, 'source': 'Num 18:21, 18:26, 18:31'},
    'tithe_thresholds': {'value': {'grain': 'the pile smoothed', 'wine': 'skimmed', 'oil': 'in the trough', 'olives_grapes': 'at the house or courtyard'}, 'settings': {'processed': "from what is processed — the pile evened, the wine skimmed, the oil dripped (Sifrei 121:1; Mishnah Ma'aserot 1:6-7); grain at the granary, olives and grapes at the house (Bava Metzia 88b)"}, 'source': 'Num 18:27, 18:30'},
    'one_in_a_hundred': {'value': 'holiness_row_by_call', 'settings': {'holiness_row_by_call': "the holiness engine's ratio read live: %d (Mishnah Orlah 2:1; Terumot 4:7 — R. Eliezer 101, R. Yehoshua a hundred and more, R. Yosei b. Meshullam a kav to a hundred seahs)" % HB_101}, 'source': 'Num 18:29; Sifrei 121:1'},
    'levite_wage_condition': {'value': 'if_he_serves_he_takes', 'settings': {'if_he_serves_he_takes': "'in exchange for their service' — if he serves he takes; a Levite who refused one service has no portion (Sifrei 119:5, 122:1)"}, 'source': 'Num 18:21, 18:31'},
    'every_place': {'value': 'even_a_cemetery', 'settings': {'even_a_cemetery': "'in every place' — even a cemetery, the a-fortiori from terumah refused (Sifrei 122:1; Yevamot 86b:2 R. Akiva)", 'any_city_R._Eliezer': 'R. Eliezer: any city, unlike the second tithe (Yevamot 86b:2)'}, 'source': 'Num 18:31'},
    'firstborn_threshold': {'value': 'bamidbar_row_by_call', 'settings': {'bamidbar_row_by_call': "the row threshold_edge is Bamidbar's (3:15's month): read live — %s" % BM_AGE}, 'source': 'Num 18:16; Bekhorot 49a:6'},
    'redeeming_lamb': {'value': 'any_lamb', 'settings': {'any_lamb': 'sheep or goat, any sex or age, blemished too; not a calf, a wild animal, a slaughtered one, a fatally wounded one, a hybrid or a koy (Mishnah Bekhorot 1:4-5)', 'hybrid_R._Eliezer': 'R. Eliezer permits the hybrid of a sheep and a goat (Mishnah Bekhorot 1:5)'}, 'source': 'Exod 13:13; Num 18:15'},
    'lamb_responsibility': {'value': 'not_liable_the_Rabbis', 'settings': {'not_liable_the_Rabbis': 'the designated lamb died — the owner not liable, as second-tithe money (Mishnah Bekhorot 1:6; R. Yehoshua and R. Tzadok testified)', 'liable_R._Eliezer': 'R. Eliezer: liable, as the five sela (Bekhorot 12b:18)'}, 'source': 'Num 18:15'},
    'donkey_timing': {'value': 'immediately_the_Rabbis', 'settings': {'immediately_the_Rabbis': 'the ass redeemed immediately (Bekhorot 12b:23, 13a:3 — the Rabbis; Sifrei 118:1)', 'thirty_days_R._Eliezer': 'R. Eliezer: after thirty days, compared to the son (Bekhorot 13a:3)'}, 'source': 'Num 18:15-16'},
    'raise_before_giving': {'value': {'small': 30, 'large': 50}, 'settings': {'thirty_fifty': 'the Israelite raises the firstborn thirty days (small) or fifty (large) before giving it (Mishnah Bekhorot 4:1; Bekhorot 26b:10 — Exod 22:29 juxtaposed to 18:16)', 'three_months_R._Yosei': 'R. Yosei: three months for the small animal (Mishnah Bekhorot 4:1)'}, 'source': 'Num 18:17-18'},
    'firstborn_eaters': {'value': 'priests_Beit_Shammai', 'settings': {'priests_Beit_Shammai': 'Beit Shammai: the firstborn like the breast and thigh — priests only; not menstruating women (Bekhorot 32b:11, 33a:7)', 'any_Beit_Hillel': 'Beit Hillel: the blemished firstborn to any, to menstruating women too (Bekhorot 33a:7)'}, 'source': 'Num 18:18'},
    'watch_places': {'value': {'priests': 3, 'levites': 21}, 'settings': {'three_and_twenty_one': 'the priests keep watch in three places, the Levites in twenty-one (Mishnah Middot 1:1; Tamid 1:1); the priests above, the Levites below (Middot 1:5; Tamid 26b)'}, 'source': 'Num 18:2-4'},
    'lots': {'value': 4, 'settings': {'four_lotteries': 'the ashes, the second of thirteen, the incense for new priests, the limbs (Mishnah Yoma 2:1-4); nine to twelve priests for the daily offering (2:5); the ram eleven, the bull twenty-four (2:6-7)'}, 'source': 'Num 18:7 — a service of gift; Sifrei 116:2: service by lot as the blood is by lot'},
    'three_crowns': {'value': 'torah_priesthood_kingdom', 'settings': {'torah_priesthood_kingdom': "three crowns — Torah, priesthood, kingdom; Aaron took the second, David the third, the first left for all (Sifrei 119:4); the crown of a good name above them (Mishnah Avot 4:13)"}, 'source': 'Num 18:19; 2 Sam 7:19'},
    'most_holy_portion_use': {'value': 'consumption_alone_R._Yosei', 'settings': {'consumption_alone_R._Yosei': "'from the fire' — as the fire's share, for consumption alone: a priest cannot betroth with it (Kiddushin 52b:16)", 'all_needs_R._Yehuda': "'yours' — for all your needs, betrothal too (Kiddushin 52b:16)"}, 'source': 'Num 18:9'},
    'doubtful_terumah_watch': {'value': 'pure_only_R._Yehoshua', 'settings': {'pure_only_R._Yehoshua': "'given YOU the charge' — only terumah fit for you is safeguarded (Bekhorot 34a:6)", 'doubtful_too_R._Eliezer': 'R. Eliezer: the doubtful too — Elijah may purify it (Bekhorot 34a:6)'}, 'source': 'Num 18:8'},
    'devotion_by_priests': {'value': 'priests_not_levites_may_R._Shimon', 'settings': {'priests_not_levites_may_R._Shimon': "R. Shimon: priests may not dedicate (dedications are theirs — 'shall be yours'), Levites may (Mishnah Arakhin 8:5; Arakhin 28a:12)", 'neither_R._Yehuda': 'R. Yehuda: neither priests nor Levites (Mishnah Arakhin 8:5); Rebbi: R. Yehuda on land, R. Shimon on movables'}, 'source': 'Num 18:14'},
}

# =====================================================================
# Motion 1 — THE FUNCTION, compiled from the ink (F1-F5)
# =====================================================================
# ===== F1: THE REBELLION (Num 16:1-35) =====================================================================
def rebellion(case, data):
    del P[:]
    ask = case['ask']
    if ask == 'took':
        ink('16:1', '"and Korach TOOK" — no object; the genealogy stops at Levi where 1 Chr 6:23 runs it to Israel'); move('Onkelos Num 16:1', 'divided himself'); move('Sanhedrin 109b:13 (Reish Lakish)', 'he took a bad acquisition for himself')
        return out('took — no object; Onkelos: divided himself; a bad acquisition (Sanhedrin 109b)', [FX.NONE])
    if ask == 'two_hundred_fifty':
        ink('16:2, 16:17, 16:35', 'the parser at three seats: %s — 16:35 "THE fifty and two hundred", the definite numeral at the head of a compound, taught at 5b' % C250)
        return out('250 — the parser at 16:2, 16:17 and 16:35 (the definite numeral at the head of a compound)', [FX.NONE])
    if ask == 'too_much_returned':
        ink('16:3', '"too much for you" (rav lakhem)'); ink('16:7', 'returned to the Levites — "too much for you, sons of Levi"'); move('Sotah 13b:13 (R. Levi)', 'proclaimed with "rav", so it was proclaimed to him with "rav" — Deut 3:26 "let it suffice for you"')
        return out('too much for you (16:3) returned at 16:7; proclaimed to Moses at Deut 3:26 (Sotah 13b)', [FX.NONE])
    if ask == 'congregation_ten':
        ink('16:21', '"separate yourselves from AMONG this congregation"'); move('Berakhot 21b:5; Megillah 23b:7; Sanhedrin 74b:3', '"among" / "among" with the sanctification of the Name; "congregation" / "congregation" with the spies (14:27): a congregation is ten')
        return out('10 — among / among with the sanctification of the Name; congregation / congregation with the spies (Berakhot 21b; Megillah 23b; Sanhedrin 74b)', [FX.NONE])
    if ask == 'summons_procedure':
        ink('16:12', '"and Moses sent to call Dathan and Abiram"'); ink('16:16', '"be you and all your congregation before the LORD, you and they and Aaron, tomorrow"'); ink('16:14', '"will you put out the eyes of these men" — the report'); move('Moed Katan 16a:3-5 (Rava)', "the court's agent; the defendant in person; before a great man; both parties named; a date set; the agent's report not slander")
        return out('the agent sent (16:12); in person (16:16); before a great man; both parties named; a date set — tomorrow; the report of disrespect permitted (Moed Katan 16a)', [FX.NONE])
    if ask == 'test':
        ink('16:5', '"in the morning the LORD will make known who is His and who is holy"'); ink('16:7, 16:16', '"tomorrow" twice — the one-day timer censers_test_awaited'); move('Sanhedrin 110a', 'as the boundary between morning and evening was fixed at creation, so Aaron')
        return out('in the morning the LORD will make known (16:5) — the boundary fixed at creation (Sanhedrin 110a); the censers tomorrow (16:7, 16:16) — the one-day timer', [FX.NONE])
    if ask == 'oath':
        ink('16:15', '"it was hot to Moses, very... do not turn to their offering; not ONE ass have I taken" — %s; the Cain echo (Gen 4:5 "it was hot to Cain, very"; "to Cain and his offering He did not turn")' % ONE_ONE); move('Nedarim 38a:11-13', "Rava: Samuel's greater — 'whose ox, whose ass' (1 Sam 12:3) even with consent"); move('Megillah 9b:1', "the translators' 'one item of value'")
        return out("not one ass (16:15) — Samuel's whose ox, whose ass (1 Sam 12:3; Nedarim 38a); the Cain echo (Gen 4:5)", [FX.NONE])
    if ask == 'oath_warning_formula':
        ink('16:26', '"turn aside, I pray, from the tents of these wicked men and touch nothing of theirs, lest you be swept away" — Sodom\'s verbs (Gen 19:2, 18:23)'); move('Shevuot 39a:7', 'the bystanders recite it when an oath is administered; the oath on the court\'s understanding (the oaths engine\'s seat)')
        return out('16:26 recited at the oath — depart from the tents of these wicked men (Shevuot 39a)', [FX.NONE])
    if ask == 'new_creation':
        ink('16:30', '"if the LORD creates a creation and the ground opens its mouth" — the noun\'s one seat'); dat('the row earth_mouth = %s' % data['earth_mouth']['value']); move('Mishnah Avot 5:6; Pesachim 54a', 'the mouth of the earth created at the twilight of the sixth day'); move('Sanhedrin 110a:16; Nedarim 39b:3 (Rava)', 'nothing new under the sun — the opening brought near')
        return out("the mouth of the earth created at the twilight of the sixth day (Avot 5:6); if not, create it now — Gehenna's opening brought near (Sanhedrin 110a:16; Nedarim 39b)", [FX.NONE])
    if ask == 'death_mode':
        ink('16:32', '"every person who belonged TO Korach" — Korach not named (computed: %s)' % ('לקרח' in SWALLOWED_NAMES)); ink('26:10', '"and swallowed them with Korach" — the retelling adds him (computed: %s)' % ADDS_KORACH); dat('the row korach_death_mode = %s: %s' % (data['korach_death_mode']['value'], data['korach_death_mode']['settings']['open'][:80]))
        move('Sanhedrin 110a:13 (R. Yochanan)', 'neither swallowed nor burned — he died in the plague'); move('Sanhedrin 110a:14 (the baraita, the outside teaching)', 'both burned and swallowed')
        return out('OPEN — 16:32 names the men who belonged to Korach, not Korach; 26:10 adds and Korach; R. Yochanan: the plague; the baraita: burned and swallowed (Sanhedrin 110a)', ['put_to_death'])
    if ask == 'share':
        ink('16:33', '"the earth covered them and they perished from among the assembly"'); dat('the row korach_share = %s' % data['korach_share']['value']); move('Mishnah Sanhedrin 10:3; Sanhedrin 108a:4, 109b:11', 'R. Akiva: no share, no rising; R. Eliezer: "the LORD kills and makes alive"'); move('Sanhedrin 109b:12; Tosefta Sanhedrin 13:9', 'R. Yehuda ben Beteira: a lost item sought and found')
        return out('R. Akiva: no share and no rising; R. Eliezer: the LORD kills and makes alive (Mishnah Sanhedrin 10:3); R. Yehuda ben Beteira: a lost item sought (Sanhedrin 109b)', [FX.NONE])
    if ask == 'sons_of_korach':
        ink('26:11', '"and the sons of Korach did not die"'); dat('the row sons_of_korach = %s' % data['sons_of_korach']['value']); move('Sanhedrin 110a', 'a place was fortified for them in Gehenna')
        return out('the sons of Korach did not die (26:11) — a place fortified for them (Sanhedrin 110a); the eleven Psalm headings', [FX.NONE])
    if ask == 'exclusion_by_sin':
        ink('16:32-33', 'the swallowed perished from among the assembly'); move('CALLED cold_run_zelophehad.inheritance_order(excluded) -> %r [IMPORT, live call]' % ZL_EXCL, "Bava Batra 118b: the spies, the protesters (Korach's two hundred fifty) and Korach's congregation took no portion")
        return out(ZL_EXCL, ['exempt'])
    if ask == 'not_for_heaven':
        dat('the row dispute_not_for_heaven = %s' % data['dispute_not_for_heaven']['value']); move('Mishnah Avot 5:17', "a dispute not for Heaven's sake will not endure — Korach and all his congregation")
        return out("a dispute not for Heaven's sake — Korach and all his congregation (Avot 5:17)", [FX.NONE])
    if ask == 'earth_mouth_cain':
        ink('16:30-32', '"the ground opens its mouth" / "the earth opened its mouth" — Cain\'s ground (Gen 4:11), Deut 11:6'); move('Sanhedrin 37b:11 (Rav Yehuda son of R. Chiyya)', "the earth's mouth opened for Abel's blood and again for Korach — for a deleterious purpose")
        return out('the ground opened its mouth for Abel\'s blood and for Korach — for a deleterious purpose (Sanhedrin 37b); Gen 4:11, Deut 11:6', [FX.NONE])
    if ask == 'swallowed':
        ink('16:31-33', '"the ground under them split... the earth opened its mouth and swallowed them and their houses... they went down alive to Sheol"'); ink('Deut 11:6; Ps 106:17', 'the retellings name Dathan and Abiram alone')
        return out('Dathan and Abiram and their households swallowed alive (16:31-33); Deut 11:6, Ps 106:17 name them alone', ['put_to_death'])
    if ask == 'fire':
        ink('16:35', '"fire went out from WITH the LORD and consumed the two hundred and fifty men" — %d; Leviticus\' "from before" (9:24, 10:2)' % C250[2]); move('Sanhedrin 52a:10-12', "the souls burned, the bodies intact — 'sinned against their souls' (17:3)")
        return out('fire from with the LORD consumed the 250 (16:35) — the souls burned, the bodies intact (Sanhedrin 52a); Lev 9:24, 10:2 from before', ['put_to_death'])
    if ask == 'wives':
        dat('the row wives = %s' % data['wives']['value']); move('Sanhedrin 109b:15-16 (Rav)', "On's wife: the wine, the tent's entrance — spared"); move('Sanhedrin 110a', "Korach's wife incited him")
        return out("On's wife saved him — the wine and the tent's entrance; Korach's wife incited (Sanhedrin 109b-110a)", [FX.NONE])
    if ask == 'names':
        ink('16:1, 18:12', 'Izhar = fresh oil — one pointed word (the reading\'s crown; the triad %s at 18:12)' % TRIAD); move('Sanhedrin 109b:13-15', 'the names expounded: a void, the afternoon heat, blunted teeth, an escort; Dathan the precepts, Abiram braced, On in mourning')
        return out("Korach a void; Izhar the afternoon heat; Dathan the precepts; Abiram braced; On in mourning (Sanhedrin 109b) — the names' lore; Izhar = fresh oil the ink's pointed word (18:12)", [FX.NONE])
    if ask == 'visiting_the_sick':
        ink('16:29', '"and the visitation of all men is visited on them"'); move('Nedarim 39b:2 (Reish Lakish; Rava)', 'visiting the sick alluded')
        return out('alluded from the visitation of all men (16:29 — Nedarim 39b)', [FX.NONE])
    if ask == 'elect':
        ink('16:2', '"princes of the congregation, called to the assembly, men of name" — 1:16\'s "called of the congregation" returning at 26:9'); move('Sanhedrin 110a:4', 'the elect who intercalate the years; men of renown')
        return out('the elect of the assembly = those who intercalate; men of renown (Sanhedrin 110a:4)', [FX.NONE])
    if ask == 'what_moses_heard':
        ink('16:4', '"and Moses heard and fell on his face" — alone on his face (singular); 16:22 and 17:10 the two'); move('Sanhedrin 110a:5', 'suspected of adultery — Ps 106:16; Exod 33:7')
        return out('suspected of adultery — Ps 106:16 (Sanhedrin 110a:5)', [FX.NONE])
    return out('no verdict in span', [FX.NONE])


# ===== F2: THE PLAGUE AND THE STAFFS (Num 17:1-28) =========================================================
def plague_and_staffs(case, data):
    del P[:]
    ask = case['ask']
    if ask == 'elevate_in_sanctity':
        ink('17:3-4', '"let them be made beaten plates, a covering for the altar, for they offered them before the LORD and they became holy" — the plate-word the gold thread\'s (Exod 39:3)'); move('Menachot 99a:11 (R. Acha bar Ya\'akov)', 'one elevates in sanctity — service vessels became the altar\'s own')
        return out("one elevates in sanctity — the censers, service vessels, became the altar's covering (Menachot 99a)", ['altar_plated'])
    if ask == 'burning_mode':
        ink('17:3', '"the censers of these sinners against their own souls"'); move('Sanhedrin 52a:10-12', 'burning / burning with Lev 21:9: the soul burned, the body intact')
        return out('the souls burned, the bodies intact (17:3 sinned against their souls; Sanhedrin 52a) — the capital burning\'s likeness', [FX.NONE])
    if ask == 'stranger_incense_ban':
        ink('17:5', '"a memorial... that no stranger who is not of Aaron\'s seed shall come near to burn incense before the LORD... as the LORD spoke by the hand of Moses TO HIM" — the output verse; the stranger defined "not of Aaron\'s seed" (Lev 21:21, 22:4 the seed)')
        return out("no stranger not of Aaron's seed to burn incense (17:5) — the output by the hand of Moses to him; rule installed on the priesthood", ['rule_installed'])
    if ask == 'maintaining_a_dispute':
        ink('16:25', '"and Moses rose and went to Dathan and Abiram"'); ink('17:5', '"that he be not as Korach and his congregation"'); dat('the row maintaining_a_dispute = %s' % data['maintaining_a_dispute']['value']); move('Sanhedrin 110a:6 (Reish Lakish; Rav)', 'one may not perpetuate a dispute — a prohibition; R. Ashi: leprosy')
        return out('one may not perpetuate a dispute — a prohibition from not to be as Korach (Rav; Reish Lakish on 16:25 — Sanhedrin 110a); R. Ashi: leprosy', [FX.NONE])
    if ask == 'incense_atones':
        ink('17:12', '"and he put the incense and atoned for the people" — atonement written of incense'); dat('the row incense_stays_plague = %s' % data['incense_stays_plague']['value']); move('Yoma 44a:5; Arakhin 16a:19; Zevachim 88b:10', 'incense atones — for slander: the private for the private')
        return out('incense atones — for slander: the private for the private (Yoma 44a; Arakhin 16a; Zevachim 88b)', ['atoned_forgiven'])
    if ask == 'angel_of_death':
        ink('17:13', '"and he stood between the dead and the living, and the plague was stayed"'); move('Shabbat 89a:2', 'the angel of death gave Moses the remedy — Ps 68:19')
        return out('the angel of death gave Moses the remedy (Shabbat 89a)', [FX.NONE])
    if ask == 'plague_count':
        ink('17:14', '"the dead in the plague were fourteen thousand and seven hundred, BESIDES the dead over the matter of Korach" — %d by the parser; the 250 and the households uncounted (Onkelos: the division of Korach)' % PLAGUE)
        return out("14,700 — besides the dead over the matter of Korach (17:14, the parser's)", ['plague_struck'])
    if ask == 'fire_from_the_altar':
        ink('17:11', '"put fire on it from OFF the altar and put incense" — the Day of Atonement\'s phrase (Lev 16:12) against Nadab\'s strange fire (Lev 10:1)')
        return out("from off the altar (17:11) — the Day of Atonement's phrase (Lev 16:12); against the strange fire (Lev 10:1)", [FX.NONE])
    if ask == 'staffs_count':
        ink('17:17-18', '"twelve staffs... Aaron\'s name on the staff of Levi" — %s' % STAFFS); ink('17:21', '"a staff for one prince, a staff for one prince... twelve staffs, and Aaron\'s staff among their staffs" — %s: Levi inside the twelve, Joseph one staff' % STAFFS_21)
        return out("12 — a staff for a father's house, Aaron's on Levi's, among their staffs (17:17-21 — the parser's [12], [1, 1, 12])", [FX.NONE])
    if ask == 'budded':
        ink('17:23', '"on the morrow... the staff of Aaron for the house of Levi had budded: it brought forth a bud and blossomed a BLOSSOM and ripened almonds" — the blossom the frontplate\'s word (Exod 28:36, 39:30, Lev 8:9); almonds once in the Bible; "ripened" Isaac weaned (Gen 21:8)')
        return out("a bud, a blossom (the frontplate's word), almonds (once; the menorah's cups) — on the morrow (17:23)", ['staff_budded'])
    if ask == 'staff_hidden':
        ink('17:25', '"return Aaron\'s staff before the testimony for a keeping, for a sign" — the manna jar\'s formula (Exod 16:34)'); dat('the row staff_hidden_with = %s' % data['staff_hidden_with']['value']); move('Horayot 12a:1-3; Keritot 5b:16-20; Yoma 52b:15', '"keepsake" / "keepsake" — sequestered with the ark, the jar and the oil')
        return out('hidden with the ark, the jar of manna and the anointing oil (Horayot 12a; Keritot 5b; Yoma 52b) — the keepsake / keepsake analogy', ['kept_for_a_sign'])
    if ask == 'three_deaths':
        ink('17:27', '"we expire, we perish, all of us perish" — the expire-verb Aaron\'s own at 20:29'); move('Onkelos Num 17:27', 'three deaths: the sword, the earth, the plague — cut from the shelf\'s bytes at the reading')
        return out('we expire, we perish, all of us perish (17:27) — Onkelos: the sword, the earth, the plague', [FX.NONE])
    if ask == 'levite_at_another_work':
        ink('18:3', '"only to the vessels of the holy and to the altar they shall not come near, that they die not, both they and you"'); dat('the row levite_at_another_work = %s' % data['levite_at_another_work']['value']); move('Arakhin 11b', "a Levite at the priests' work or another Levite's — death by Heaven")
        return out("a Levite at the priests' work or another Levite's — death by Heaven (Arakhin 11b)", ['death_by_heaven'])
    if ask == 'whoever_comes_near':
        ink('17:28', '"everyone who comes near, who comes near to the tabernacle of the LORD dies" — the doubled participle\'s one seat'); ink('18:7', '"the stranger who comes near shall be put to death"'); move('Sanhedrin 84a:13 (R. Yishmael)', '"shall die" / "shall be put to death" — death by Heaven')
        return out("whoever comes near dies (17:28) with 18:7's shall be put to death — R. Yishmael: death by Heaven (Sanhedrin 84a)", ['death_by_heaven'])
    return out('no verdict in span', [FX.NONE])

# ===== F3: THE WATCH (Num 18:1-7) ==========================================================================
def the_watch(case, data):
    del P[:]
    ask = case['ask']
    if ask == 'iniquity_of_the_sanctuary':
        ink('18:1', '"you and your sons and your father\'s house with you shall bear the iniquity of the sanctuary" — the LORD to Aaron alone (five Torah seats, three here)'); move('Sifrei Bamidbar 116:1 (R. Yoshiyah)', "the priests' mishandled offerings"); move('CALLED cold_run_tzav.dues_machine(eli_violation) -> %r [IMPORT, live call]' % TZ_ELI, "Eli's sons the recorded violation (1 Sam 2:15-17 — the Sifrei's own citation on 18:1)")
        return out("the priests' mishandled offerings (Sifrei 116:1 — R. Yoshiyah); Eli's sons the recorded violation (tzav CALLED)", [FX.NONE])
    if ask == 'iniquity_of_the_priesthood':
        ink('18:1', '"you and your sons with you shall bear the iniquity of your priesthood"'); move('Sifrei Bamidbar 116:1', 'keeping strangers out')
        return out('keeping strangers out (Sifrei 116:1)', [FX.NONE])
    if ask == 'song':
        ink('18:2-3', '"your brothers the tribe of Levi... joined to you and serve you" — Leah\'s verb at Levi\'s naming (Gen 29:34); "neither they nor you"'); move('Arakhin 11b:2 (R. Yonatan)', 'the Levites equated with the priests for a service pertaining to the altar — the song'); move('Sifrei Bamidbar 116:1', '"with you" = the Levites\' song')
        return out("the Levites' altar-service is the song — neither they nor you (Arakhin 11b; Sifrei 116:1)", ['watch_owed'])
    if ask == 'fence':
        ink('18:3', '"only to the vessels of the holy and to the altar they shall not come near, that they die not, BOTH THEY AND YOU"'); move('Sifrei Bamidbar 116:1', "the two-way fence — the priests inside, the Levites outside; treasurers and trustees"); move('Arakhin 11b', "the priests not the Levites' work, the Levites not the priests'")
        return out("both they and you — the priests not the Levites' work, the Levites not the priests' (18:3; Sifrei 116:1; Arakhin 11b)", ['watch_owed'])
    if ask == 'watch_stories':
        ink('18:2', '"that they may accompany you and serve you"'); ink('18:4', '"and keep the watch of the tent of meeting"'); move('Tamid 26b:3-4', 'the priests keep watch ABOVE, the Levites BELOW'); move('Mishnah Middot 1:5, 1:9', 'the Gate of the Sparks; the priest locks within while the Levite sleeps outside')
        return out('the priests above, the Levites below (Tamid 26b; Mishnah Middot 1:5); the priest locks within, the Levite sleeps outside (Middot 1:9)', ['watch_owed'])
    if ask == 'watch_places':
        ink('18:4-5', '"keep the watch of the tent of meeting... the watch of the holy and the watch of the altar" — the watch-word six times'); dat('the row watch_places = %s' % data['watch_places']['value']); move('Mishnah Middot 1:1-2; Mishnah Tamid 1:1', 'three and twenty-one; the sleeping watchman beaten, his clothes burned')
        return out('3 and 21 — the priests in three places, the Levites in twenty-one (Mishnah Middot 1:1; Tamid 1:1); the sleeping watchman beaten (Middot 1:2)', ['watch_owed'])
    if ask == 'stranger_warning':
        ink('18:4', '"and a stranger shall not come near to you" — the warning, one seat'); ink('1:51, 3:10, 3:38, 18:7', '"the stranger who comes near shall be put to death" — the punishment at four seats'); move('Zevachim 16a:5', 'the non-priest barred from the rites is derived from 18:4'); move('Sifrei Bamidbar 116:1', 'the warning and the punishment')
        return out('18:4 the warning — a stranger shall not come near to you (Zevachim 16a; Sifrei 116:1)', ['stranger_barred'])
    if ask == 'stranger_death':
        ink('18:7', '"and the stranger who comes near shall be put to death" — the formula\'s fourth seat'); dat('the row zar_who_served is BAMIDBAR\'S (1:51\'s clause), read by CALL: %s — %s' % (ZAR['value'], ZAR['source'][:90])); move('Mishnah Sanhedrin 9:6; Sanhedrin 83b:4, 84a:13', 'the Rabbis: death at the hand of Heaven; R. Akiva: strangulation; R. Yishmael\'s "shall die" / "shall be put to death"'); move('Sifrei Bamidbar 116:2', 'only for a service, even in purity — the fork on "shall be put to death"')
        return out("death by Heaven — the Rabbis; R. Akiva: strangulation (Mishnah Sanhedrin 9:6; Sanhedrin 83b, 84a) — Bamidbar's row zar_who_served by CALL: %s" % ZAR['value'], ['death_by_heaven'])
    if ask == 'stranger_death_scope':
        ink('18:7', '"for every matter of the altar and within the veil, and you shall serve; a service of GIFT"'); move('Yoma 24a:7 (Rav)', 'a service of giving, not removal; a complete service'); move('Yoma 24b:1', 'within the veil the giving services only; outside any service'); move('Yoma 27a:1', 'slaughter by a non-priest valid — Lev 1:5'); move('Sifrei Bamidbar 116:2', 'only for a service, even in purity')
        return out('a service of giving and complete — not removal, not slaughter; within the veil the giving services (Yoma 24a-b, 27a); only for a service, even in purity (Sifrei 116:2)', [FX.NONE])
    if ask == 'no_more_wrath':
        ink('18:5 / 1:53', 'the clause computed: 1:53 %s; 18:5 %s — added %s, dropped %s' % (' '.join(WRATH_153), ' '.join(WRATH_185), WRATH_ADDED, WRATH_DROPPED)); move('Sifrei Bamidbar 116:1', 'four "no more"s, each paid by a prior event — the calf, the murmur, the spies, Korach (M-23 exemplar 15)')
        return out("18:5 = 1:53's clause with one token added — no MORE wrath (computed); the four no-mores each paid by a prior event (Sifrei 116:1)", ['watch_owed'])
    if ask == 'given_to_the_lord':
        ink('18:6', '"to you a GIFT, given to the LORD" — the third form of the Levites given (3:9, 8:16)'); move('Sifrei Bamidbar 116:2', 'to the LORD, not to the priests')
        return out('a gift, given to the LORD (18:6) — to the LORD, not to the priests (Sifrei 116:2); the third form (3:9, 8:16)', [FX.NONE])
    if ask == 'service_of_gift':
        ink('18:7', '"a service of gift I give your priesthood"'); move('Pesachim 73a:1; Sifrei Bamidbar 116:2 (R. Tarfon)', 'the eating of terumah in the provinces made like the Temple\'s service'); move('Mishnah Yoma 2:1-2', 'the lots — service by lot as the blood is by lot (Sifrei 116:2)')
        return out('a service of gift — the lots (Mishnah Yoma 2:1-2: four lotteries); eating terumah in the provinces equated (Pesachim 73a; Sifrei 116:2)', [FX.NONE])
    if ask == 'lots':
        dat('the row lots = %s' % data['lots']['value']); move('Mishnah Yoma 2:1-7; Mishnah Tamid 1:2', 'the ashes, the thirteen, the incense, the limbs; nine to twelve priests; the ram eleven, the bull twenty-four')
        return out('four lotteries — the ashes, the thirteen, the incense, the limbs (Mishnah Yoma 2:1-4); nine to twelve priests (2:5); the ram eleven, the bull twenty-four (2:6-7)', [FX.NONE])
    if ask == 'genealogy_chamber':
        ink('18:7', '"and within the veil"'); dat('the row genealogy_chamber = %s' % data['genealogy_chamber']['value']); move('Sifrei Bamidbar 116:2; Mishnah Middot 5:4', 'the chamber where the priesthood\'s genealogy was judged — black and white')
        return out('within the veil — the chamber of hewn stone judges the priesthood: black and white (Mishnah Middot 5:4; Sifrei 116:2)', [FX.NONE])
    if ask == 'washing_hands':
        move('Sifrei Bamidbar 116:2', 'the washing of the hands scriptural — "and you shall serve"'); move('Chullin 106a-107a', 'the hands washed')
        return out('the washing of the hands scriptural (Sifrei 116:2; Chullin 106a)', [FX.NONE])
    if ask == 'why_reiterate':
        ink('18:1', 'the demarcation reiterated after 1:51, 3:10, 3:38'); move('Sifrei Bamidbar 116:1 (Rebbi)', 'because Korach came, Scripture reiterated the exhortation — the census of the demarcation verses')
        return out('because Korach came, Scripture reiterated the exhortation (Sifrei 116:1 — Rebbi)', [FX.NONE])
    return out('no verdict in span', [FX.NONE])


# ===== F4: THE GIFTS (Num 18:8-19) =========================================================================
def the_gifts(case, data):
    del P[:]
    ask = case['ask']
    if ask == 'with_joy':
        ink('18:8', '"and the LORD spoke to Aaron: and I, behold, I have given you" — the LORD to Aaron; 17:5\'s "to him" the frame through Moses'); move('Sifrei Bamidbar 117:1 (R. Yishmael; R. Nathan)', '"and I, behold" — with joy; "and I" willingly')
        return out("and I, behold — with joy (Sifrei 117:1); through Moses by 17:5's to him", [FX.NONE])
    if ask == 'covenant_reason':
        ink('18:8', 'the gifts written after the rebellion'); move('Sifrei Bamidbar 117:2', 'the covenant written, sealed and recorded because Korach contested — the king\'s retainer'); move('Sifrei Bamidbar 119:2 (R. Yishmael)', '"my cow\'s leg was broken for my good" — for Aaron\'s good did Korach come')
        return out("the covenant written because Korach contested — the king's retainer (Sifrei 117:2); for Aaron's good did Korach come (119:2)", [FX.NONE])
    if ask == 'eaten_in_greatness':
        ink('18:8', '"to you I have given them for ANOINTING"'); move('Onkelos Num 18:8', 'for GREATNESS — cut from the shelf\'s bytes at the reading'); move('Zevachim 91a:19', 'THE TALMUD CITES ONKELOS: eaten as kings eat, any manner'); move('Chullin 132b:14; Sotah 15a:5; Zevachim 28a:10', 'roasted with mustard; wine, oil and honey in the remainder; the tail\'s skin')
        return out('for anointing = for greatness — eaten as kings eat, roasted with mustard, any manner (Onkelos cited at Zevachim 91a; Chullin 132b; Sotah 15a)', ['due_to_priest'])
    if ask == 'twenty_four':
        L = data['the_twenty_four']['value']; n = len(L['sanctuary']) + len(L['borders']); assert n == 24, n
        ink('18:8-19', 'a generalization (18:8), the details (18:9-18), a covenant of salt (18:19)'); dat('the row the_twenty_four = twelve in the sanctuary + twelve in the borders = %d (computed on the list)' % n); move('Chullin 133b:11; Bava Kamma 110b; Sifrei Bamidbar 119:1-2', 'twenty-four gifts given to Aaron and his sons')
        return out('24 — twelve in the sanctuary, twelve in the borders (Sifrei 119:1-2; Chullin 133b; Bava Kamma 110b); a generalization, a detail and a covenant of salt', ['priestly_dues_granted'])
    if ask == 'most_holy_list':
        ink('18:9', '"every offering of theirs, every meal offering, every sin offering, every guilt offering" — the four "every"s (Sifrei 117:2\'s four lists)'); move('Menachot 73a:9; Zevachim 44b:4 (Levi\'s baraita, the outside teaching)', 'the omer\'s and the suspected wife\'s meal offerings, the bird olah\'s meat'); move('Menachot 58a:14', 'the leper\'s log included'); move('CALLED cold_run_chatat.domain(unwitting) -> %r; cold_run_minchah.adjuncts(sinner) -> %r; cold_run_vayikra5.pointers(asham_procedure) -> %r [IMPORT, live calls]' % (CH_SIN, MN_SINNER, str(V5_ASHAM)[:60]), 'the sin, meal and guilt offerings the engines\' own objects')
        return out("every offering, every meal offering, every sin offering, every guilt offering (18:9) — the four everys include the omer's, the suspected wife's, the bird olah's meat, the leper's log (Menachot 73a; Zevachim 44b)", ['due_to_priest'])
    if ask == 'from_the_fire':
        ink('18:9', '"this shall be yours of the most holy, from the fire"'); move('Sifrei Bamidbar 117:2', 'the most holy from the fire = the burnt offering\'s hide')
        return out("the olah's hide — the most holy from the fire (Sifrei 117:2)", ['due_to_priest'])
    if ask == 'returned':
        ink('18:9', '"which they RETURN to Me" — 5:8\'s restitution the pointer'); move('Sifrei Bamidbar 117:2; Bava Kamma 110a', 'the proselyte\'s theft')
        return out("which they return to Me — the proselyte's theft (5:8; Sifrei 117:2; Bava Kamma 110a)", ['due_to_priest'])
    if ask == 'most_holy_eating_place':
        ink('18:10', '"in the most holy place you shall eat it"'); move('Menachot 9a:1', 'the courtyard; inside the Sanctuary in certain instances'); move('Zevachim 63a:15 (R. Yochanan ben Beteira)', 'gentiles surrounding the courtyard — the priests eat inside')
        return out('in the most holy place — the courtyard; inside the Sanctuary when gentiles surround it (Zevachim 63a; Menachot 9a)', [FX.NONE])
    if ask == 'every_male':
        ink('18:10', '"every male shall eat it"'); move('Menachot 83a:2; Zevachim 97b:11', 'communal peace offerings eaten only by the priests\' males')
        return out("every male — communal peace offerings eaten by the priests' males (Menachot 83a; Zevachim 97b)", [FX.NONE])
    if ask == 'most_holy_portion_use':
        dat('the row most_holy_portion_use = %s' % data['most_holy_portion_use']['value']); move('Kiddushin 52b:16', 'R. Yehuda: betrothed with it; R. Yosei: consumption alone')
        return out('R. Yehuda: betrothed with it; R. Yosei: consumption alone (Kiddushin 52b)', [FX.NONE])
    if ask == 'impure_terumah_benefit':
        ink('18:8', '"the watch of My TERUMOT" — plural'); move('Shabbat 25a:2, 26a:5; Yevamot 74a:18 (Rav Nachman / Rabba bar Avuh)', 'two terumot — the impure burned with benefit beneath the dish, from the separation onward')
        return out('My terumot — two: the impure burned with benefit beneath the dish, from the separation onward (Shabbat 25a-26a; Yevamot 74a)', [FX.NONE])
    if ask == 'doubtful_terumah_watch':
        dat('the row doubtful_terumah_watch = %s' % data['doubtful_terumah_watch']['value']); move('Bekhorot 34a:6', 'R. Yehoshua: the pure only; R. Eliezer: the doubtful too')
        return out('R. Yehoshua: safeguard only the pure; R. Eliezer: the doubtful too (Bekhorot 34a)', [FX.NONE])
    if ask == 'breast_and_thigh':
        ink('18:11', '"the terumah of their gift, all the wave offerings of the children of Israel" — to your sons and daughters'); move('CALLED cold_run_tzav.dues_machine(breast_thigh) -> %r [IMPORT, live call]' % TZ_BT, 'Lev 7:30-34\'s breast and thigh')
        return out('breast and thigh to the priests after the smoking (tzav CALLED); the terumah of their gift, all the wave offerings (18:11)', ['due_to_priest'])
    if ask == 'household':
        ink('18:11, 18:13', '"every clean one in your house shall eat it" twice; "to your daughters"'); move('CALLED cold_run_priesthood.holy_food(household, who=wife) -> %r [IMPORT, live call]' % PR_HOUSE, 'Lev 22:11\'s household — the wife eats'); move('CALLED cold_run_priesthood.holy_food(daughter_to_stranger) -> %r' % PR_DAUGHTER, 'Lev 22:12-13\'s daughter')
        return out('every clean one in your house — the household (priesthood CALLED); to your daughters', ['terumah_fed'])
    if ask == 'betrothed_eats':
        ink('18:11, 18:13', '"every clean one in your house" TWICE — the betrothed daughter of an Israelite (Sifrei 117:2)'); dat('the row betrothed_eats = %s' % data['betrothed_eats']['value']); move('Sifrei Bamidbar 117:2 (R. Yochanan b. Bag Bag; R. Yehudah in Netzivim)', 'the a-fortiori: she eats; the Sages\' decree: not'); move('Mishnah Ketubot 5:2-3; Ketubot 57b-58a', 'the later court: not until she enters the canopy — the cup and the simpon')
        return out('the a-fortiori: she eats (R. Yochanan b. Bag Bag); THE DECREE: not until the canopy (Mishnah Ketubot 5:3 — the later court; Ketubot 57b-58a: the cup and the simpon) — the decree over the a-fortiori', ['stranger_barred'])
    if ask == 'the_best_triad':
        ink('18:12', '"all the best of the fresh oil, all the best of the wine and the grain, their first part" — the triad %s: oil, wine, grain — reversed against eleven grain-wine-oil seats; the first word Izhar\'s' % TRIAD); move('Bekhorot 53b:17, 54b:2; Temurah 5a:11', 'the best of this and of that separately — kind for kind; "their first part" each type its own')
        return out("the best of the oil, the wine and the grain (18:12) — Izhar's word; the triad reversed against eleven seats (computed); kind for kind: each type its first (Bekhorot 53b, 54b)", [FX.NONE])
    if ask == 'bikkurim':
        ink('18:13', '"the first fruits of all that is in their land, which they bring to the LORD, shall be yours; every clean one in your house shall eat it"'); move('Sifrei Bamidbar 117:2', 'holy while attached'); move('Chullin 136a:8; Menachot 84b:6, 84b:10', 'partners liable, outside the land exempt; roofs and ships; the household eats — the verse read as two'); move('CALLED cold_run_moadim.two_loaves() -> %r [IMPORT, live call]' % (str(MO_LOAVES)[:80],), 'the two loaves precede the first fruits (Menachot 84b:6)')
        return out('the first fruits of all — holy while attached (18:13; Sifrei 117:2); partners liable, outside the land exempt (Chullin 136a); roofs and ships (Menachot 84b); the household eats (84b:10)', ['due_to_priest'])
    if ask == 'devoted':
        ink('18:14', '"every devoted thing in Israel shall be yours" — one seat'); dat('the row devotion_default = %s; the four authorities: %s' % (data['devotion_default']['value'], data['devotion_default']['settings']['four_authorities'][:120])); move('CALLED cold_run_temurah.devote(unspecified_destination) -> %r [IMPORT, live call]' % TM_DEV, 'Lev 27:21 / 27:28 — the Sages / R. Yehuda b. Beteira'); move('Sifrei Bamidbar 117:3', 'gentiles\', women\'s and bondsmen\'s too; the four-way dispute')
        return out("every devoted thing in Israel — gentiles', women's, bondsmen's too (Sifrei 117:3); unspecified: %s (temurah CALLED) — the four-way dispute: R. Yossi HaGelili the priests, R. Yehudah b. Beteira Temple maintenance, R. Yehudah b. Bava the priests, R. Shimon Heaven" % TM_DEV, ['most_holy'])
    if ask == 'devoted_status':
        ink('18:14', '"shall be yours"'); move('CALLED cold_run_temurah.devote(priests_devotions) -> %r [IMPORT, live call]' % TM_DEV_PRIESTS, 'no redemption, given to the priests'); move('Arakhin 29a:1; Bekhorot 32a:25', 'in the owner\'s house consecrated (27:28); given to the priest common (18:14)'); move('Arakhin 28b:1', '"to the priest" / "to the priest" with 5:8 — the watch on duty')
        return out('in the owner\'s house consecrated; given to the priest common (Arakhin 29a; Bekhorot 32a); to the priest of the watch serving (Arakhin 28b)', ['due_to_priest'])
    if ask == 'devoted_to_whom':
        move('Arakhin 28b:1', 'a dedicated field to the priest of the watch serving — the verbal analogy "to the priest" (Lev 27:21) / "to the priest" (5:8, the proselyte\'s theft)')
        return out('to the priest of the watch serving in the Temple — to the priest / to the priest with 5:8 (Arakhin 28b)', ['due_to_priest'])
    if ask == 'devotion_by_priests':
        dat('the row devotion_by_priests = %s' % data['devotion_by_priests']['value']); move('Mishnah Arakhin 8:5; Arakhin 28a:12', 'R. Yehuda: neither; R. Shimon: priests not, Levites may')
        return out('R. Yehuda: priests and Levites may not; R. Shimon: priests not, Levites may (Mishnah Arakhin 8:5)', [FX.NONE])
    if ask == 'devote_firstborn':
        move('CALLED cold_run_temurah.devote(firstborn) -> %r [IMPORT, live call]' % TM_DEV_FB, 'Mishnah Arakhin 8:7: the firstborn, whole or blemished, may be devoted — assessed by the daughter\'s son; R. Yishmael\'s two verses')
        return out("the firstborn, whole or blemished, may be devoted — assessed by the daughter's son (Mishnah Arakhin 8:7; temurah CALLED: %s)" % TM_DEV_FB, [FX.NONE])
    if ask == 'opens_the_womb':
        ink('18:15', '"all that opens the womb of all flesh which they offer to the LORD, in man and in beast, shall be yours; yet redeem, you shall redeem the firstborn of man, and the firstborn of the unclean beast you shall redeem"'); move('Sifrei Bamidbar 118:1', '"which they offer" excludes the unclean animal, "and in beast" re-includes the blemished; what obtains with the man obtains with his beast — the Levites\' ass exempt'); move('Bekhorot 4a:6', 'the juxtaposition: the Levites\' donkeys exempt')
        return out("all that opens the womb — which they offer excludes the unclean animal, and in beast re-includes the blemished (Sifrei 118:1); the Levites' ass exempt", ['consecrated_firstborn'])
    if ask == 'redemption_rate':
        ink('18:16', '"by your valuation, five shekels of silver by the shekel of the sanctuary — it is twenty gerah" — %s' % REDEMPTION); move('CALLED cold_run_bamidbar.levites(rate) -> %r [IMPORT, live call]' % BM_RATE, '3:47\'s five, five shekels per skull — the same rate at the census')
        return out(BM_RATE, ['pays'])
    if ask == 'redemption_before_thirty':
        ink('18:16', '"from a month old you shall redeem"'); dat('the row firstborn_threshold is Bamidbar\'s threshold_edge, by CALL'); move('CALLED cold_run_bamidbar.levites(age, 31 days) -> %r [IMPORT, live call]' % BM_AGE, '"month" / "month" with 3:40 (Bekhorot 49a:6)'); move('Bava Kamma 11b:2-3; Menachot 37a:8', 'mauled within thirty days — no redemption ("yet")'); move('Mishnah Bekhorot 8:6; Shabbat 135b:13', 'the thirtieth day like the day before (R. Akiva: doubtful); a child alive thirty days no stillborn')
        return out('after thirty days — from a month old (18:16 / 3:40; Bekhorot 49a; Bamidbar CALLED: %s); mauled within thirty — no redemption (Bava Kamma 11b); the thirtieth day like the day before (Mishnah Bekhorot 8:6)' % BM_AGE, ['pays'])
    if ask == 'redemption_timing':
        dat('the row donkey_timing = %s' % data['donkey_timing']['value']); move('Bekhorot 12b:23, 13a:3; Sifrei Bamidbar 118:1', 'the son after thirty days; the ass immediately (the Rabbis) or after thirty (R. Eliezer)')
        return out('thirty days the son, at once the ass (Bekhorot 12b-13a; Sifrei 118:1 — immediately or after a month)', ['pays'])
    if ask == 'redemption_means':
        ink('18:16', '"by your valuation, five shekels of silver"'); dat('the row redemption_means = %s' % data['redemption_means']['value']); move('CALLED cold_run_bamidbar.levites(means, coins) -> %r [IMPORT, live call]' % BM_MEANS, 'Mishnah Bekhorot 8:8'); move('Sifrei Bamidbar 118:1; Bekhorot 51a:10; Shevuot 4b:6', 'general-particular-general: movable, not bondsmen, writs or land; Rebbi: writs only')
        return out('redeemed when in the priest\'s hand (Bamidbar CALLED); not with slaves, notes, land or consecrated items (Mishnah Bekhorot 8:8); movable, not writs (Sifrei 118:1 — Rebbi: writs only)', ['pays'])
    if ask == 'twenty_gerah_floor':
        ink('18:16', '"it is twenty gerah" — the seat among the shekel engine\'s five: %s' % IS_SEATS); move('CALLED cold_run_incense_shekel.shekel(twenty_gerah) -> %r [IMPORT, live call]' % IS_SEATS, 'the unit defined at Exod 30:13'); move('Bekhorot 50a:6; Sifrei Bamidbar 118:1', '"shall be" — may add (the Sages\' sixth); "the same is twenty" — never fewer'); move('CALLED cold_run_yovel.field_valuation(49)[shekel] -> %r [IMPORT, live call]' % YV_SHEKEL, 'Lev 27:25 "twenty gerah shall be the shekel" — "by your valuation" (18:16) the valuations\' word')
        return out('twenty gerah — more, not less (Sifrei 118:1; Bekhorot 50a); the seat among the shekel engine\'s five: Num 18:16', ['pays'])
    if ask == 'five_sela_coinage':
        move('Mishnah Bekhorot 8:7; Bekhorot 49b:10-11; Kiddushin 11b:7', 'the five sela in the Tyrian maneh; the sanctuary shekel twenty gera')
        return out('the five sela in the Tyrian maneh (Mishnah Bekhorot 8:7; Bekhorot 49b)', ['pays'])
    if ask == 'self_redemption':
        ink('18:15', '"REDEEM, YOU SHALL REDEEM" — the doubled infinitive\'s one seat'); move('Kiddushin 29a:15', 'the father redeems (Exod 34:20); if not, the son redeems himself'); move('Sifrei Bamidbar 118:1 (Kerem Beyavneh, R. Tarfon)', 'the doubled verb')
        return out('redeem, you shall redeem — the son redeems himself if the father did not (Kiddushin 29a; Sifrei 118:1 Kerem Beyavneh)', ['pays'])
    if ask == 'redemption_money_lost':
        ink('18:15', '"shall be yours" BEFORE "you shall redeem" — the verse order'); move('Mishnah Bekhorot 8:8; Bekhorot 51a:8, 51b:7-9', 'the father liable for the lost coins; redeemed only in the priest\'s hand')
        return out('the father liable — shall be yours before you shall redeem (Mishnah Bekhorot 8:8; Bekhorot 51a)', ['pays'])
    if ask == 'unclean_firstborn_scope':
        ink('18:15', '"the firstborn of the unclean beast you shall redeem"'); move('Sifrei Bamidbar 118:1; Bekhorot 5b:28 (R. Yosei HaGelili)', 'the ass alone — "the firstborn of a donkey" (Exod 13:13), not horses or camels; with a sheep'); move('CALLED cold_run_pesach.firstborn(donkey) -> %r [IMPORT, live call]' % PS_DONKEY, 'Exod 13:13\'s fork')
        return out('the ass alone (Sifrei 118:1; Bekhorot 5b) — redeem with a lamb, else break the neck (pesach CALLED)', ['redeem_or_break'])
    if ask == 'ass_redeem_or_break':
        move('CALLED cold_run_pesach.firstborn(donkey) -> %r [IMPORT, live call]' % PS_DONKEY, 'Mishnah Bekhorot 1:7: the redemption precedes the breaking')
        return out(PS_DONKEY, ['redeem_or_break'])
    if ask == 'levite_donkey':
        move('CALLED cold_run_bamidbar.levites(owner=priest, donkey) -> %r [IMPORT, live call]' % BM_OWNER, 'Mishnah Bekhorot 1:1\'s a-fortiori from 3:45; Bekhorot 4a:6\'s juxtaposition'); move('CALLED cold_run_bamidbar.levites(partner) -> %r' % BM_PARTNER, 'a gentile partner')
        return out(BM_OWNER, ['exempt'])
    if ask == 'donkey_doubt':
        move('Mishnah Bekhorot 1:3', 'the untried donkey bearing two males — one lamb; a male and a female — the burden of proof on the priest')
        return out('the burden of proof on the priest — a male and a female, the owner keeps the lamb; two males, one lamb (Mishnah Bekhorot 1:3)', [FX.NONE])
    if ask == 'redeeming_lamb':
        dat('the rows redeeming_lamb = %s; lamb_responsibility = %s' % (data['redeeming_lamb']['value'], data['lamb_responsibility']['value'])); move('Mishnah Bekhorot 1:4-6; Bekhorot 12b:18', 'any lamb; the exclusions; the designated lamb died')
        return out('any lamb — sheep or goat, any age, blemished; not a calf, a hybrid or a koy (Mishnah Bekhorot 1:4-5); the designated lamb died — R. Eliezer / the Rabbis (1:6)', [FX.NONE])
    if ask == 'clean_firstborn':
        ink('18:17', '"the firstborn of an ox, or the firstborn of a sheep, or the firstborn of a goat you shall not redeem — they are holy"'); move('Bekhorot 5b:10; Sifrei Bamidbar 118:1', 'an ox and its firstborn an ox; no hybrid'); move('CALLED cold_run_temurah.redeem(animal_tithe) -> %r [IMPORT, live call]' % TM_TITHE, 'Lev 27:33\'s "it shall not be redeemed" beside')
        return out('the firstborn of an ox, a sheep, a goat you shall not redeem — they are holy (18:17); an ox and its firstborn an ox (Bekhorot 5b); no hybrid (Sifrei 118:1)', ['consecrated'])
    if ask == 'firstborn_resembles':
        move('Bekhorot 7a:4, 12a:16, 6b:24; Bava Kamma 78a:6; Mishnah Bekhorot 1:2', 'the head and the majority of the body like the mother; resembling another species — no firstborn; the ass likewise')
        return out('the head and the majority of the body like the mother (Bekhorot 7a); resembling another species — no firstborn (Bekhorot 12a; Bava Kamma 78a)', [FX.NONE])
    if ask == 'firstborn_portions':
        ink('18:17', '"you shall sprinkle THEIR blood on the altar and make THEIR fat smoke"'); dat('the row one_spilling = %s' % data['one_spilling']['value']); move('Pesachim 64b:18; Zevachim 37a:8-9, 56b:12 (R. Yosei HaGelili / R. Yishmael)', 'the tithe and the Passover too — or from Deut 12:27'); move('Keritot 4a:12', 'the portions burned'); move('Sifrei Bamidbar 118:1', '"they are consecrated" — one spilling (Yoshiyah) / the fats (Yitzchak)')
        return out("their blood, their fat — the tithe and the Passover placed like the firstborn (R. Yosei HaGelili; Zevachim 37a, 56b; Pesachim 64b); R. Yishmael from Deut 12:27; the portions burned (Keritot 4a)", ['consecrated'])
    if ask == 'firstborn_blood_placement':
        move('Mishnah Zevachim 5:8; Zevachim 56b:12', 'lesser sanctity; slaughtered anywhere in the courtyard; the blood ONE PLACEMENT on the base')
        return out("one placement on the base — their blood, their fat: the tithe and the Passover too (R. Yosei HaGelili; Zevachim 56b; Mishnah Zevachim 5:8; Sifrei 118:1's one spilling)", ['consecrated'])
    if ask == 'firstborn_eating_window':
        ink('18:18', '"their flesh shall be yours, as the wave-breast and as the right thigh, it shall be yours" — "it shall be yours" twice'); move('CALLED cold_run_offerings.dispatch(shelamim) -> the peace offering\'s row (%s) [IMPORT, live call]' % ', '.join(sorted(OF_SHELAMIM)), 'the analogy\'s object'); move('Bekhorot 27b:7, 28a:2; Zevachim 57a:5-13; Temurah 21b:13; Mishnah Zevachim 5:8', 'two days and a night; the second "it shall be yours" the second day')
        return out('two days and a night — as the wave-breast and the right thigh (18:18; Bekhorot 27b; Zevachim 57a; Mishnah Zevachim 5:8) — the peace offering\'s row CALLED', ['due_to_priest'])
    if ask == 'firstborn_sale':
        move('Bava Kamma 13a:7; Bekhorot 31b:7, 32a:7; Temurah 5b:1, 8a:1; Zevachim 75b:8', '"you shall not redeem" — its sanctity never removed, yet sold: alive unblemished, blemished alive or slaughtered; the tithe neither')
        return out('not redeemed, but sold — alive unblemished, blemished alive or slaughtered; the tithe neither (Bava Kamma 13a; Bekhorot 31b; Temurah 5b, 8a)', [FX.NONE])
    if ask == 'firstborn_substitute':
        move('Temurah 21a:9; Zevachim 37b:3, 81b:7-8', '"THEY are holy" — they, not their substitutes')
        return out('they are holy — they, not their substitutes (Temurah 21a; Zevachim 37b)', [FX.NONE])
    if ask == 'firstborn_blood_mixed':
        move('Zevachim 81a:8; Temurah 5b:9', '"they are holy" — the blood mixed with others\' still sacrificed')
        return out("they are holy — the blood mixed with others' still sacrificed (Zevachim 81a; Temurah 5b)", [FX.NONE])
    if ask == 'firstborn_without_altar':
        move('Makkot 19a:9; Temurah 21a:22; Zevachim 60b:9', 'the flesh as the blood — eaten only while the altar stands; second tithe follows')
        return out('the flesh as the blood — eaten only while the altar stands (Makkot 19a; Temurah 21a; Zevachim 60b)', [FX.NONE])
    if ask == 'blemished_firstborn':
        move('Zevachim 37b:2', 'the blemished firstborn to the priest — "it shall be yours" repeated'); dat('the row raise_before_giving = %s' % data['raise_before_giving']['value']); move('Mishnah Bekhorot 4:1-5', 'raised thirty or fifty days; kept the year; the expert')
        return out('to the priest — it shall be yours repeated (Zevachim 37b); raised thirty or fifty days (Mishnah Bekhorot 4:1); kept the year (4:2); the expert (4:4-5)', ['due_to_priest'])
    if ask == 'blemished_keeping':
        move('Mishnah Bekhorot 4:2', 'a blemish within the year — the twelve months; after — thirty days')
        return out('a blemish within the year — kept the twelve months; after the year — thirty days (Mishnah Bekhorot 4:2)', [FX.NONE])
    if ask == 'blemish_expert':
        move('Mishnah Bekhorot 4:3-5', 'slaughtered then shown (R. Yehuda / R. Meir); a non-expert pays, the court\'s expert exempt (R. Tarfon\'s cow); a paid examiner disqualified unless like Ila')
        return out("the court's expert exempt, a non-expert pays (Mishnah Bekhorot 4:4); a paid examiner disqualified unless like Ila (4:5); shown after slaughter — R. Yehuda / R. Meir (4:3)", [FX.NONE])
    if ask == 'firstborn_eaters':
        dat('the row firstborn_eaters = %s' % data['firstborn_eaters']['value']); move('Bekhorot 32b:11, 33a:7', 'Beit Shammai / Beit Hillel')
        return out('Beit Shammai: priests only, not menstruating women; Beit Hillel: the blemished to any (Bekhorot 32b-33a)', [FX.NONE])
    if ask == 'raise_before_giving':
        dat('the row raise_before_giving = %s' % data['raise_before_giving']['value']); move('Mishnah Bekhorot 4:1; Bekhorot 26b:10', 'Exod 22:29 juxtaposed to 18:16\'s month')
        return out("30 days a small animal, 50 a large (Mishnah Bekhorot 4:1; Bekhorot 26b — Exod 22:29 juxtaposed to 18:16's month)", [FX.NONE])
    if ask == 'twins':
        move('Mishnah Bekhorot 8:3-5', 'twins — five sela after thirty days; one died — exempt; two wives — ten; the intermingled by certainty; the son redeems himself')
        return out('twins — five sela after thirty days; one died — exempt; two wives — ten; the intermingled by certainty (Mishnah Bekhorot 8:3-5)', ['pays'])
    if ask == 'firstborn_for_redemption':
        move('Mishnah Bekhorot 8:1-2', 'the four classes; R. Yosei HaGelili: opens a Jewish mother\'s womb; the caesarean — neither'); move('CALLED cold_run_pesach.firstborn(caesarean_animal) -> %r [IMPORT, live call]' % PS_CAESAREAN, 'the womb not opened')
        return out("opens a Jewish mother's womb (Mishnah Bekhorot 8:1); the caesarean — neither (8:2; pesach CALLED: %s)" % PS_CAESAREAN, [FX.NONE])
    if ask == 'suspect_firstborn':
        move('Mishnah Bekhorot 4:7, 4:10', 'no meat nor untanned hides from one suspect on firstborns; may neither judge nor testify on that matter')
        return out('no meat nor untanned hides from one suspect on firstborns (Mishnah Bekhorot 4:7); may neither judge nor testify on it (4:10)', [FX.NONE])
    if ask == 'suspect_principle':
        move('Mishnah Bekhorot 4:10', 'suspect on this not on that; suspect on either suspect on purities')
        return out('suspect on the sabbatical year not on tithes, nor the reverse; suspect on either — on purities; neither judge nor witness on that matter (Mishnah Bekhorot 4:10)', [FX.NONE])
    if ask == 'covenant_of_salt':
        ink('18:19', '"a covenant of salt forever it is before the LORD, for you and your seed with you" — the phrase\'s two seats in the Bible (computed): %s' % COVENANT_OF_SALT); move('Sifrei Bamidbar 119:5', 'Aaron\'s covenant greater than David\'s — for the wicked sons too'); move('Menachot 19b:14-20a:1; 21b:12', 'salting indispensable; from communal supplies'); move('Chullin 133b:11', 'the twenty-four eternal as salt')
        return out("a covenant of salt — Aaron's (18:19) and David's (2 Chr 13:5) alone; salting indispensable (Menachot 19b-20a); from communal supplies (Menachot 21b); Aaron's greater than David's (Sifrei 119:5)", ['covenant_of_salt'])
    if ask == 'salt_source':
        move('Menachot 21b:12', '"everlasting covenant" / "everlasting covenant" with the showbread (Lev 24:8) — from communal supplies')
        return out('the salt from communal supplies — everlasting covenant / everlasting covenant with the showbread (Menachot 21b)', [FX.NONE])
    if ask == 'gentile_consecrations':
        ink('18:8', '"of all the hallowed things of the CHILDREN OF ISRAEL"'); move('Temurah 3a:4', 'not gentiles\' — no misuse in their consecrations')
        return out("of all the hallowed things of the children of Israel — not gentiles': no misuse (Temurah 3a)", [FX.NONE])
    if ask == 'three_crowns':
        dat('the row three_crowns = %s' % data['three_crowns']['value']); move('Sifrei Bamidbar 119:4; Mishnah Avot 4:13', 'three crowns; the good name above them')
        return out('three crowns — Torah, priesthood, kingdom; the good name above them (Avot 4:13; Sifrei 119:4)', [FX.NONE])
    if ask == 'bikkurim_partners':
        move('Chullin 136a:8', '"in THEIR land" — partners liable; "your land" excludes outside')
        return out('first fruits from land in partnership — liable; outside the land exempt (Chullin 136a)', ['due_to_priest'])
    if ask == 'bikkurim_scope':
        move('Menachot 84b:6', '"the first fruits of ALL" — roofs, ruins, flowerpots, ships; the two loaves first')
        return out('the first fruits of all — roofs, ruins, flowerpots and ships; the two loaves precede (Menachot 84b)', ['due_to_priest'])
    if ask == 'bikkurim_eaters':
        move('Menachot 84b:9-10 (Rav Mesharshiyya)', 'the verse read as two: the meal offerings for males, the first fruits for the household')
        return out('the household eats the first fruits — the verse read as two (Menachot 84b:10)', ['terumah_fed'])
    return out('no verdict in span', [FX.NONE])

# ===== F5: THE TITHE (Num 18:20-32) ========================================================================
def the_tithe(case, data):
    del P[:]
    ask = case['ask']
    if ask == 'no_inheritance':
        ink('18:20', '"in their land you shall not inherit, and you shall have no portion among them; I am your portion and your inheritance"'); move('Onkelos Num 18:20', 'the gifts I have given you, they are your portion'); ink('18:23-24', '"among the children of Israel they shall inherit no inheritance" twice'); ink('Deut 10:9, 18:2; Josh 13:14; Ezek 44:28', 'the runs')
        return out('in their land you shall not inherit — I am your portion (18:20; Onkelos: the gifts I have given you); the Levites no inheritance (18:23-24); Deut 10:9, 18:2, Josh 13:14, Ezek 44:28', ['inheritance_barred'])
    if ask == 'exclusion_table':
        dat('the row exclusion_table = %s' % data['exclusion_table']['value']); move('Sifrei Bamidbar 119:1', 'the set carved from 26:53 by four clauses'); move('Mishnah Ma\'aser Sheni 5:14', 'R. Meir: priests and Levites do not confess; R. Yosei: the Levitical cities'); move('CALLED cold_run_zelophehad.inheritance_order(excluded) -> %r' % ZL_EXCL, 'the exclusion by sin beside')
        return out("priests (18:20), Levites (18:23), bondsmen and proselytes (26:55), the two of uncertain sex (26:54) — Sifrei 119:1; R. Meir: priests and Levites do not confess (Mishnah Ma'aser Sheni 5:14)", ['inheritance_barred'])
    if ask == 'tithe_to_levites':
        ink('18:21', '"all the tithe in Israel for an inheritance IN EXCHANGE for their service" — "in exchange" the Torah\'s two seats (18:21, 18:31)'); dat('the row levite_wage_condition = %s' % data['levite_wage_condition']['value']); move('Sifrei Bamidbar 119:5, 122:1', 'if he serves he takes; a Levite who refused one service has no portion')
        return out('all the tithe in Israel — in exchange for their service (18:21): the Levite serves, the Levite takes; a Levite who refused one service has no portion (Sifrei 119:5, 122:1)', ['tithe_granted'])
    if ask == 'tithe_recipient':
        dat('the row tithe_recipient = %s' % data['tithe_recipient']['value']); move('Yevamot 86b:1-2', 'R. Akiva: the Levites; R. Eliezer: the priests too'); move('Yevamot 86a-b', "Ezra's penalty")
        return out("the Levite (18:21, 18:26 — R. Akiva); the priest too — Ezra's penalty / the priests called Levites (R. Eliezer; Yevamot 86a-b)", ['tithe_granted'])
    if ask == 'third_year':
        move('Rosh Hashanah 12b:3', 'the first tithe juxtaposed to an inheritance — no interruption in the third year'); move('Sifrei Bamidbar 119:5', 'the tithe an inheritance — does not change its place')
        return out('the first tithe every year — juxtaposed to an inheritance (Rosh Hashanah 12b; Sifrei 119:5)', [FX.NONE])
    if ask == 'tithe_to_foreigners':
        move('Yevamot 86a:2', 'R. Meir: the tithe called terumah — forbidden to non-Levites; the Rabbis permit')
        return out('R. Meir: forbidden to non-Levites as terumah; the Rabbis permit (Yevamot 86a)', [FX.NONE])
    if ask == 'levite_he':
        ink('18:23', '"and the Levite, HE shall serve" — one seat'); move('Sifrei Bamidbar 119:5', 'perforce; in sabbatical and jubilee years; no priest in his stead — R. Nathan\'s a-fortiori refused')
        return out('the Levite — he: perforce, in sabbatical and jubilee years, no priest in his stead (Sifrei 119:5)', [FX.NONE])
    if ask == 'tithe_of_the_tithe':
        ink('18:26', '"you shall lift from it a terumah of the LORD, a tithe from the tithe" — one seat; Neh 10:39 the run'); dat('the arithmetic: %s x %s = %s' % (Fraction(1, 10), Fraction(1, 10), TITHE_OF_TITHE)); move('Menachot 54b:11; Beitzah 13b:3', 'one-tenth of the first tithe')
        return out('1/100 — a tenth of the tenth (18:26; Menachot 54b; Neh 10:39)', ['terumah_of_the_tithe_owed'])
    if ask == 'from_it':
        ink('18:26', '"from IT"'); move('Sifrei Bamidbar 120:1', 'kind for its kind, rooted for rooted, new for new, not across the border (Lev 27:30)'); move('Mishnah Terumot 1:5, 1:8-10; Mishnah Ma\'aser Sheni 5:11', 'the answer sheet\'s row — not the tithed tithe, not the exempt for the liable, not plucked for attached, not new for old, not the land\'s for outside')
        return out('from it — kind for its kind, rooted for rooted, new for new, not across the border (Sifrei 120:1; Mishnah Terumot 1:5); not the tithed tithe, not the exempt for the liable', [FX.NONE])
    if ask == 'mourner':
        move('Sifrei Bamidbar 120:1', '"from it" free (mufneh) for the mourner — the tithe and the paschal lamb'); move('Pesachim 36a; Yevamot 73b-74a; Mishnah Ma\'aser Sheni 5:12', '"not in my mourning"')
        return out("from it free for the mourner — the tithe and the paschal lamb (Sifrei 120:1; Pesachim 36a; Yevamot 73b); Mishnah Ma'aser Sheni 5:12", [FX.NONE])
    if ask == 'levite_preceded':
        ink('18:26', '"a tenth part of the tithe" — I said to you the tithe\'s terumah'); ink('18:29', '"from ALL that is given you" — the great terumah from the tithe too'); move('Berakhot 47a:15-47b:1; Beitzah 13b:6-7; Eruvin 31b:4-5; Pesachim 35b:6-7; Shabbat 127b:17-18 (R. Abbahu / Reish Lakish; Abaye to Rav Pappa)', 'on the stalks exempt from the great terumah; after the pile liable')
        return out("on the stalks — the tithe's terumah only; after the pile — the great terumah too (Berakhot 47a-b; Beitzah 13b; Eruvin 31b; Pesachim 35b; Shabbat 127b)", ['due_to_priest'])
    if ask == 'estimate':
        ink('18:27', '"and YOUR terumah shall be reckoned to you" — the plural'); move('Beitzah 13b:3; Bekhorot 58b:11, 59a:1; Menachot 54b:11 (Abba Elazar ben Gomel)', 'two terumot — by estimate and by thought; the tithes too (18:24\'s "terumah"), the animal tithe'); move('Sifrei Bamidbar 121:1', 'by estimate and by thought'); move('Mishnah Terumot 1:7, 4:6', 'never by measure; counting, measuring, weighing ranked')
        return out("by estimate and by thought — your terumah plural, two terumot (Abba Elazar ben Gomel: Beitzah 13b; Bekhorot 58b-59a; Sifrei 121:1); never by measure (Mishnah Terumot 1:7); the tithes too (18:24's terumah)", [FX.NONE])
    if ask == 'who_separates_tithe_terumah':
        move('Gittin 30b:13 (Abba Elazar ben Gamla)', 'the homeowner may separate the tithe\'s terumah from the Levite\'s tithe')
        return out('the Levite, and the owner too (Gittin 30b)', [FX.NONE])
    if ask == 'thresholds':
        ink('18:27, 18:30', '"as the grain of the threshing floor and as the fullness of the winepress" — the floor-word at %s' % [s for s in FLOOR_SEATS if s.startswith('Num')]); dat('the row tithe_thresholds = %s' % data['tithe_thresholds']['value']); move('Sifrei Bamidbar 121:1', 'from what is processed — the pile evened, the wine skimmed, the oil dripped'); move('Mishnah Ma\'aserot 1:5-8; Bava Metzia 88b:7; Mishnah Terumot 1:10', 'the answer sheet\'s thresholds; grain at the granary, olives and grapes at the house; the processed for the processed')
        return out("the pile evened, the wine skimmed, the oil dripped (Sifrei 121:1; Mishnah Ma'aserot 1:6-7); grain at the granary, olives and grapes at the house (Bava Metzia 88b); the processed for the processed (Terumot 1:10)", [FX.NONE])
    if ask == 'terumah_measure':
        ink('18:12, 18:29', '"the best of the oil..." / "from all its best" — NO MEASURE IN THE INK'); ink('15:20', '"as the terumah of the threshing floor" — the challah cell\'s pointer PAID at this cell'); dat('the row terumah_measure = %s (this runner\'s own; Shelach\'s copy the placeholder)' % data['terumah_measure']['value']); move('CALLED cold_run_naso.restitution(terumah_measure) -> %r [IMPORT, live call]' % NS_TM, 'the floor — Mishnah Terumot 4:5')
        return out('1/40, 1/50, 1/60 (Beit Shammai 1/30 — Mishnah Terumot 4:3); the floor: some must remain common (4:5 — naso\'s cell CALLED)', ['due_to_priest'])
    if ask == 'kind_for_kind':
        ink('18:12', '"the best of the oil, the best of the wine and the grain, THEIR first part"'); move('Mishnah Terumot 2:4; Bekhorot 53b:17, 54b:2; Temurah 5a:11', 'not one kind for another — not terumah; each type its own first')
        return out('not one kind for another — not terumah (Mishnah Terumot 2:4; Bekhorot 53b); the first part of them — each type its own (Bekhorot 54b; Temurah 5a)', [FX.NONE])
    if ask == 'the_best':
        ink('18:29-30, 18:32', '"from all its best, its hallowed part" / "when you lift its best" — Onkelos "its beauty"'); move('Sifrei Bamidbar 122:1', 'a warning to take only from the choicest'); move('Mishnah Terumot 2:4, 2:6', 'where a priest is, the best; where none, what lasts; the superior for the inferior, not the reverse')
        return out('from all its best (18:29-30, 18:32) — where a priest is, the best; where none, what lasts; the superior for the inferior, not the reverse (Mishnah Terumot 2:4, 2:6); a warning to take the choicest (Sifrei 122:1)', [FX.NONE])
    if ask == 'inferior_for_superior':
        ink('18:32', '"and you shall bear no sin by reason of it, when you lift its best from it" — a sin, so an effect'); move('Bava Batra 84b:2, 143a:6; Bava Metzia 56a:5; Kiddushin 46b:13; Temurah 5a:9 (R. Ilai)', 'valid terumah, a transgression that takes effect'); move('Yevamot 89b:2; Mishnah Terumot 2:2', 'the impure for the pure likewise — valid by Torah law, penalized')
        return out('valid terumah, a transgression that takes effect — you shall bear no sin (18:32; R. Ilai: Bava Batra 84b, 143a; Bava Metzia 56a; Kiddushin 46b; Temurah 5a); the impure for the pure likewise, penalized (Yevamot 89b; Terumot 2:2)', ['due_to_priest'])
    if ask == 'impure_for_pure':
        move('Mishnah Terumot 2:2; Yevamot 89b:2', 'not impure for pure — unwitting valid, intentional nothing; the Levite\'s unclean tithe likewise; R. Yehuda: if he knew, even in error nothing')
        return out('not impure for pure — unwitting valid, intentional nothing (Mishnah Terumot 2:2); terumah by Torah law, the Sages penalized (Yevamot 89b)', [FX.NONE])
    if ask == 'one_in_a_hundred':
        move('Sifrei Bamidbar 121:1', 'neutralized in a hundred and one — the last rendered clause before the translator stops'); move('CALLED cold_run_holiness_b.orlah(ratio)[the_priestly_gifts] -> %r [IMPORT, live call]' % HB_101, 'Mishnah Orlah 2:1'); move('Mishnah Terumot 4:7-13; Mishnah Challah 1:9', 'R. Eliezer 101; R. Yehoshua a hundred and more; the mixtures by kind')
        return out('neutralized in a hundred and one (Sifrei 121:1; Mishnah Terumot 4:7; Challah 1:9) — holiness_b CALLED: 101', [FX.NONE])
    if ask == 'what_remains_common':
        ink('18:30', '"it shall be reckoned to the Levites as the produce of the threshing floor and the produce of the winepress"'); move('Sifrei Bamidbar 122:1', 'what remains is common, as the floor\'s grain after terumah')
        return out("what remains is common, as the floor's grain after terumah (18:30; Sifrei 122:1)", [FX.NONE])
    if ask == 'every_place':
        ink('18:31', '"and you may eat it in EVERY PLACE" — Deut 12:13\'s ban the Torah twin'); dat('the row every_place = %s' % data['every_place']['value']); move('Sifrei Bamidbar 122:1', 'even a cemetery — the a-fortiori from terumah refused'); move('Yevamot 86b:2', 'R. Akiva: excludes the priest; R. Eliezer: any city')
        return out("in every place — even a cemetery (Sifrei 122:1; Yevamot 86b — R. Akiva: excludes the priest); Deut 12:13's ban the Torah twin", [FX.NONE])
    if ask == 'household_deputes':
        ink('18:31', '"you and your household"'); move('Yevamot 86a:9; Sifrei Bamidbar 122:1', 'the Israelite wife of a Levite may depute the separation')
        return out('you and your household — the Israelite wife of a Levite may depute the separation (18:31; Yevamot 86a; Sifrei 122:1)', [FX.NONE])
    if ask == 'wage':
        ink('18:31', '"for it is your WAGE in exchange for your service" — the wage-word\'s consonants the Nazirite\'s strong drink (6:3)'); move('Bekhorot 26b:18-19', 'terumah or tithe not given as wages to the assisting priests, Levites or poor — desecrated, "that you shall not die"')
        return out('it is your wage in exchange for your service (18:31); terumah or tithe not given as wages to the assisting priests, Levites or poor (Bekhorot 26b)', ['tithe_granted'])
    if ask == 'as_wages':
        move('Bekhorot 26b:18-19', 'forbidden, desecrated — the second verse adds the death')
        return out('forbidden, desecrated — that you shall not die (Bekhorot 26b)', [FX.NONE])
    if ask == 'agent':
        ink('18:28', '"so YOU ALSO shall lift the terumah of the LORD"'); move('Bava Metzia 22a:8; Kiddushin 41b:1; Mishnah Terumot 4:4', '"also" includes an agent, with the owner\'s knowledge; by the owner\'s mind, else 1/50'); move('Gittin 52a:3', '"you" — not partners, sharecroppers, stewards'); move('Bava Metzia 71b:10-12; Gittin 23b:4', 'members of the covenant — a gentile no')
        return out('you also — an agent, with the owner\'s knowledge; by the owner\'s mind, else 1/50; not partners, sharecroppers, stewards; a gentile no (Bava Metzia 22a, 71b; Kiddushin 41b; Gittin 23b, 52a; Mishnah Terumot 4:4)', [FX.NONE])
    if ask == 'agent_gentile':
        move('Bava Metzia 71b:10-12; Gittin 23b:4', 'as the appointers are members of the covenant so the agents')
        return out('a gentile cannot separate terumah even as an agent — members of the covenant (Bava Metzia 71b; Gittin 23b)', [FX.NONE])
    if ask == 'who_separates':
        move('Mishnah Terumot 1:1-3, 1:6', 'the five excluded; the five valid after the fact; the minor disputed')
        return out('not the deaf-mute, the imbecile, the minor, from what is not his, a gentile (Mishnah Terumot 1:1); the mute, the drunk, the naked, the blind — valid after the fact (1:6)', [FX.NONE])
    if ask == 'partners':
        ink('18:28', '"ALL YOUR tithes" — plural'); move('Chullin 136a:2', 'partners obligated; a gentile\'s partnership exempt')
        return out('partners liable — all your tithes (Chullin 136a); with a gentile exempt', [FX.NONE])
    if ask == 'gentile_tithe':
        ink('18:24, 18:26', '"the tithe of the children of Israel" / "from the children of Israel"'); move('Temurah 3a:9; Zevachim 45a:10', 'not gentiles\''); move('Bekhorot 11b:9 (R. Yehoshua ben Levi)', 'bought from a gentile in smoothed piles — exempt from the tithe\'s terumah')
        return out("the tithe of the children of Israel — not gentiles' (Temurah 3a; Zevachim 45a); bought from a gentile in piles — exempt from the tithe's terumah (Bekhorot 11b)", [FX.NONE])
    if ask == 'bought_from_gentile':
        move('Bekhorot 11b:9', '"from the children of Israel" — the gentile\'s piles exempt')
        return out("bought from a gentile in smoothed piles — exempt from the tithe's terumah (Bekhorot 11b)", [FX.NONE])
    if ask == 'wrong_order':
        ink('18:29', '"of all your tithes"'); move('Temurah 4b:3 (R. Avin)', 'tithed in the wrong order — rectified by the positive command, no lashes')
        return out('tithed in the wrong order — valid, rectified by the positive command, no lashes (Temurah 4b)', [FX.NONE])
    if ask == 'israelite_benefit_from_terumah':
        ink('18:27', '"YOUR terumah"'); move('Pesachim 23a:4 (Rav Pappa; Chizkiya)', 'an Israelite may benefit from terumah')
        return out('your terumah — an Israelite may benefit (Pesachim 23a)', [FX.NONE])
    if ask == 'tithe_terumah_betrothal':
        move('Kiddushin 53a:12', 'no "to the LORD" written of the tithe\'s terumah — betrothal with it valid')
        return out("betrothal with the tithe's terumah valid — no to the LORD written of it (Kiddushin 53a)", [FX.NONE])
    if ask == 'liable_produce':
        move('Mishnah Ma\'aserot 1:1-4', 'food, guarded, grown from the land; the ripening signs')
        return out("food, guarded, grown from the land (Mishnah Ma'aserot 1:1); the ripening signs (1:2-4)", [FX.NONE])
    if ask == 'removal':
        move('Mishnah Ma\'aser Sheni 5:6, 5:9', 'the removal on Passover eve of the fourth and seventh years — the first tithe to the Levite; Rabban Gamliel\'s ship')
        return out("the removal on Passover eve of the fourth and seventh years — the first tithe to the Levite (Mishnah Ma'aser Sheni 5:6); the recipients by office: Joshua the Levite, Elazar ben Azariah the priest (5:9)", [FX.NONE])
    if ask == 'recipients':
        move('Mishnah Ma\'aser Sheni 5:9', 'the tithe to Joshua the Levite; the poor\'s to Akiva; the tithe\'s terumah to Elazar ben Azariah the priest')
        return out("the Levite, the priest (the tithe's terumah), the poor — Rabban Gamliel's ship (Mishnah Ma'aser Sheni 5:9)", [FX.NONE])
    if ask == 'confession':
        move('Mishnah Ma\'aser Sheni 5:10-11', '"given to the Levite" = the first tithe; "also given" = terumah and the tithe\'s terumah; the exclusions on the confession\'s tongue')
        return out("given to the Levite = the first tithe; also given = terumah and the tithe's terumah (Mishnah Ma'aser Sheni 5:10-11); Deut 26's run", [FX.NONE])
    if ask == 'you_shall_not_die':
        ink('18:32', '"the holy things of the children of Israel you shall not profane, and you shall not die" — the priests\' words (Lev 8:35, 10:6-9; Joseph\'s Gen 42:20)'); move('Sifrei Bamidbar 122:1', 'the warning to Levites and Israelites both')
        return out("you shall not profane... and you shall not die (18:32) — the warning to Levites and Israelites both (Sifrei 122:1); the priests' words (Lev 8:35, 10:6-9)", [FX.NONE])
    if ask == 'so_you_too':
        ink('18:28', '"so YOU TOO shall lift"'); move('Sifrei Bamidbar 121:1', 'the priests separate too (or the Levites from their own — Yishmael\'s a-fortiori from challah); the three a-fortioris')
        return out('so you too — the priests separate too (Sifrei 121:1); the three a-fortioris', [FX.NONE])
    if ask == 'terumah_status':
        move('Mishnah Challah 1:9', 'challah and terumah alike — death and a fifth, forbidden to non-priests, the priest\'s property, nullified in a hundred and one, the hands, sunset, from the near and finished'); move('CALLED cold_run_priesthood.holy_food(stranger) -> %r [IMPORT, live call]' % PR_STRANGER, 'Lev 22:10\'s stranger')
        return out("death and a fifth, forbidden to non-priests, the priest's property, nullified in a hundred and one, the hands, sunset, from the near and finished (Mishnah Challah 1:9)", ['due_to_priest'])
    if ask == 'pointer_paid':
        ink('15:20 / 18:27, 18:30', 'the floor-word\'s seats %s — "as the terumah of the threshing floor" pointed forward at 15:20 and is paid at 18:27\'s "reckoned as the grain of the threshing floor" (computed)' % [s for s in FLOOR_SEATS if s.startswith('Num')])
        return out("15:20's as the terumah of the threshing floor is paid at 18:27's reckoned as the grain of the threshing floor (computed on the floor-word); the challah cell's as_terumah CALLS this cell", [FX.NONE])
    return out('no verdict in span', [FX.NONE])


# ---- THE WRAP — the daemon, the scene, the narrative ------------------------------------------------------
def law_korach(event, world):
    """Num 16:1-18:32 (cold_run_korach.py F1-F5). installed_by boot — the rebellion's lines are acts, the grants spoken at their verses to
    Aaron and the Levites; the stranger's ban at 17:5 an OUTPUT (rule_installed on the priesthood). Two one-day timers on an undated stretch."""
    k, src = event['kind'], event['case_source']
    E_ = lambda eff, s, cp=None, amount=None, due=None, law='', value=None: {'effect': eff, 'subject': s, 'counterparty': cp, 'amount': amount, 'due': due, 'value': value if value is not None else True, 'source_law': law, 'case_source': src}
    day = event.get('day', world.clock.day)      # THE SEQUENTIAL RUN: the event's own day
    if k == 'korach_gathered_against':
        return [E_('gathered_against', 'korach', cp='moses-and-aaron', value='and Korach took... two hundred and fifty princes; gathered against Moses and against Aaron: too much for you (16:1-3)', law='F1 [INK 16:1-3; Sanhedrin 109b:13]'),
                E_('gathered_against', 'dathan', cp='moses-and-aaron', value='sons of Eliab, of Reuben — with Korach (16:1)', law='F1 [INK 16:1]'),
                E_('gathered_against', 'abiram', cp='moses-and-aaron', value='sons of Eliab, of Reuben — with Korach (16:1)', law='F1 [INK 16:1]')]
    if k == 'moses_set_the_test':
        return [E_('commanded', 'korach', value='the_censers', law='F1 [INK 16:6-7 "take for yourselves censers... tomorrow" — the debit on Korach; CLOSED by 16:18]'),
                E_('censers_test_awaited', 'korach', due=day + 1, value="tomorrow (16:7, 16:16) — the court's date set (Moed Katan 16a:4); the undated stretch's morrow", law='F1 [INK 16:7; Moed Katan 16a:4]')]
    if k == 'levites_rebuked':
        return []                                  # the words are the line's value (16:8-11)
    if k == 'censers_commanded':
        return []                                  # the command restated (16:16-17)
    if k == 'separation_commanded':
        return []                                  # the threat the value (16:20-21)
    if k == 'dathan_and_abiram_refused':
        return [E_('refused', 'dathan', cp='moses', value='we will not go up (16:12, 16:14) — the summons refused, the report of disrespect (Moed Katan 16a:5)', law='F1 [INK 16:12-14]'),
                E_('refused', 'abiram', cp='moses', value='we will not go up (16:12, 16:14)', law='F1 [INK 16:12-14]')]
    if k == 'moses_swore':
        return [E_('plea_made', 'moses', cp='HEAVEN', value="do not turn to their offering; not one ass have I taken (16:15) — the Cain echo; Samuel's run (1 Sam 12:3)", law='F1 [INK 16:15; Nedarim 38a]')]
    if k == 'censers_offered_at_the_tent':
        world.close('korach', 'commanded', 'Num 16:18 — and they took each his censer and put fire on them and put incense on them', value='the_censers')
        return [E_('glory_appeared', 'the-tabernacle', cp='HEAVEN', value='the glory of the LORD appeared to all the congregation at the entrance of the tent of meeting (16:19) — the formula\'s third seat (Lev 9:23, Num 14:10)', law='F1 [INK 16:19]')]
    if k == 'moses_and_aaron_pleaded':
        return [E_('plea_made', 'moses', cp='HEAVEN', value='O God, God of the spirits of all flesh, shall one man sin and You be wroth with all the congregation (16:22)', law='F1 [INK 16:22; Num 27:16]'),
                E_('plea_made', 'aaron', cp='HEAVEN', value='shall one man sin (16:22) — the two on their faces', law='F1 [INK 16:22]')]
    if k == 'get_up_commanded':
        return [E_('commanded', 'israel', value='get_up_from_the_dwelling', law='F1 [INK 16:24 "get up from around the dwelling of Korach, Dathan and Abiram" — the debit on Israel; CLOSED by 16:27]')]
    if k == 'congregation_withdrew':
        world.close('israel', 'commanded', 'Num 16:27 — and they got up from around the dwelling of Korach, Dathan and Abiram', value='get_up_from_the_dwelling')
        return []
    if k == 'creation_test_declared':
        return [E_('test_set', 'israel', cp='moses', value='by this you shall know: if these die the common death — the LORD has not sent me; if the LORD creates a creation and the ground opens its mouth — these men have scorned the LORD (16:28-30)', law='F1 [INK 16:28-30; Sanhedrin 110a:16; Mishnah Avot 5:6]')]
    if k == 'earth_swallowed':
        return [E_('put_to_death', 'dathan', cp='HEAVEN', value='swallowed alive with his household — the ground split, the earth opened its mouth (16:31-33); Deut 11:6, Ps 106:17', law='F1 [INK 16:31-33]'),
                E_('put_to_death', 'abiram', cp='HEAVEN', value='swallowed alive with his household (16:31-33)', law='F1 [INK 16:31-33]'),
                E_('put_to_death', 'korach', cp='HEAVEN', value='OPEN — the row korach_death_mode: 16:32 names the men who belonged to Korach, 26:10 adds and Korach; R. Yochanan the plague, the baraita burned and swallowed (Sanhedrin 110a:13-14)', law='F1 [INK 16:32 against 26:10; the DATA row korach_death_mode]')]
    if k == 'fire_consumed_the_two_hundred_fifty':
        return [E_('put_to_death', 'the-two-hundred-fifty', cp='HEAVEN', amount=C250[2], value='fire from with the LORD consumed the two hundred and fifty who offered the incense (16:35) — the souls burned, the bodies intact (Sanhedrin 52a)', law='F1 [INK 16:35 — the definite numeral read 250]')]
    if k == 'censers_beaten_into_plates':
        return [E_('altar_plated', 'the-altar', value="the copper censers beaten into plates, a covering for the altar — for they became holy; a sign, a memorial (17:3-5); one elevates in sanctity (Menachot 99a)", law='F2 [INK 17:2-5; Menachot 99a:11]'),
                E_('rule_installed', 'the-priesthood', value='law_korach:stranger_incense', law='F2 [INK 17:5 "that no stranger who is not of Aaron\'s seed shall come near to burn incense... as the LORD spoke by the hand of Moses to him" — the OUTPUT installing the ban; Sanhedrin 110a:6 the ban on maintaining a dispute]')]
    if k == 'congregation_murmured_you_killed':
        return [E_('gathered_against', 'israel', cp='moses-and-aaron', value='you have killed the people of the LORD (17:6); gathered against Moses and against Aaron (17:7)', law='F2 [INK 17:6-7]'),
                E_('glory_appeared', 'the-tabernacle', cp='HEAVEN', value='the cloud covered it and the glory of the LORD appeared (17:7) — the formula\'s fourth seat', law='F2 [INK 17:7]')]
    if k == 'plague_begun_and_stayed':
        return [E_('plague_struck', 'israel', cp='HEAVEN', amount=PLAGUE, value='the wrath has gone out, the plague has begun (17:11) — the dead 14,700 besides the dead over the matter of Korach (17:14)', law='F2 [INK 17:11-14 — the parser\'s 14,700]'),
                E_('atoned_forgiven', 'israel', value='Aaron put the incense and atoned for the people (17:12) — incense atones for slander (Yoma 44a; Arakhin 16a)', law='F2 [INK 17:12; Yoma 44a:5]'),
                E_('plague_removed', 'israel', value='he stood between the dead and the living, and the plague was stayed (17:13, 17:15)', law='F2 [INK 17:13, 17:15; Shabbat 89a:2]')]
    if k == 'staffs_commanded':
        return [E_('commanded', 'moses', value='the_staffs', law='F2 [INK 17:16-20 "take from them a staff, a staff for a father\'s house... twelve staffs... lay them before the testimony" — the debit on Moses; CLOSED by 17:22]')]
    if k == 'staffs_laid_and_budded':
        world.close('moses', 'commanded', 'Num 17:22 — and Moses laid the staffs before the LORD in the tent of the testimony', value='the_staffs')
        return [E_('staff_budding_awaited', 'aarons-staff', due=day + 1, value='laid before the LORD (17:22); on the morrow (17:23) — the undated stretch\'s morrow', law='F2 [INK 17:22-23]'),
                E_('staff_budded', 'aarons-staff', value='the staff of Aaron for the house of Levi budded: a bud, a blossom (the frontplate\'s word), almonds (17:23); twelve staffs with Levi among them (17:21)', law='F2 [INK 17:21-24; Exod 28:36]')]
    if k == 'aarons_staff_kept':
        return [E_('kept_for_a_sign', 'aarons-staff', value="returned before the testimony for a keeping, for a sign to the sons of rebellion (17:25) — beside the manna jar (Exod 16:34); hidden with the ark, the jar and the oil (Horayot 12a; Keritot 5b; Yoma 52b)", law='F2 [INK 17:25-26; Keritot 5b:20]')]
    if k == 'congregation_despaired':
        return [E_('plea_made', 'israel', cp='moses', value='we expire, we perish, all of us perish; everyone who comes near dies (17:27-28) — Onkelos: the sword, the earth, the plague', law='F2 [INK 17:27-28]')]
    if k == 'watch_given_to_aaron':
        return [E_('watch_owed', 'aaron', value="the watch of the holy and the watch of the altar (18:5); the priests within, the Levites without — both they and you (18:3); the stranger who comes near shall be put to death (18:7 — the row zar_who_served by CALL: %s); no more wrath (18:5 = 1:53 + one token)" % ZAR['value'], law='F3 [INK 18:1-7; Sifrei 116:1-2]'),
                E_('watch_owed', 'the-levites', value='joined to you and keep the watch of the tent of meeting for all the service of the tent (18:2-4); not to the vessels of the holy nor to the altar (18:3); the song (Arakhin 11b); the priests above, the Levites below (Tamid 26b)', law='F3 [INK 18:2-4; Arakhin 11b:2]')]
    if k == 'gifts_granted':
        return [E_('priestly_dues_granted', 'aaron', value='the watch of My terumot — the twenty-four gifts, twelve in the sanctuary and twelve in the borders (18:8-18; Chullin 133b; Sifrei 119:1-2); for greatness (Onkelos)', law='F4 [INK 18:8-18; the DATA row the_twenty_four]'),
                E_('covenant_of_salt', 'aaron', value="a covenant of salt forever before the LORD, for you and your seed with you (18:19) — Aaron's and David's (2 Chr 13:5)", law='F4 [INK 18:19; Sifrei 119:5]')]
    if k == 'portion_declared':
        return [E_('inheritance_barred', 'aaron', value='in their land you shall not inherit, and you shall have no portion among them; I am your portion and your inheritance (18:20)', law='F5 [INK 18:20; Sifrei 119:1]'),
                E_('inheritance_barred', 'the-levites', value='among the children of Israel they shall inherit no inheritance (18:23-24)', law='F5 [INK 18:23-24]'),
                E_('tithe_granted', 'the-levites', value='all the tithe in Israel for an inheritance in exchange for their service (18:21, 18:24) — if he serves he takes (Sifrei 119:5)', law='F5 [INK 18:21; the DATA rows tithe_recipient, levite_wage_condition]')]
    if k == 'tithe_of_the_tithe_commanded':
        return [E_('terumah_of_the_tithe_owed', 'the-levites', cp='aaron', value='a terumah of the LORD from the tithe — a tenth of the tenth (18:26) = 1/100; from all its best (18:29); reckoned as the grain of the threshing floor (18:27 — 15:20\'s pointer paid); to Aaron the priest (18:28)', law='F5 [INK 18:25-32; Menachot 54b:11]')]
    # ---- the exam's case kinds: each names LITERALLY every effect it can write (2b's form — an unnamed effect is a KeyError to read) ----
    if k == 'korach_case':
        v, e, _ = rebellion({'ask': event['ask']}, DATA); L = 'F1 [%s]' % v; s_ = event['person']
        W = {'accepted': E_('accepted', s_, value=v, law=L), 'disqualified': E_('disqualified', s_, value=v, law=L), 'exempt': E_('exempt', s_, value=v, law=L), 'put_to_death': E_('put_to_death', s_, cp='HEAVEN', value=v, law=L), 'plea_made': E_('plea_made', s_, value=v, law=L)}
        return [W[x] for x in e if x != FX.NONE]
    if k == 'plague_staff_case':
        v, e, _ = plague_and_staffs({'ask': event['ask']}, DATA); L = 'F2 [%s]' % v; s_ = event['person']
        W = {'accepted': E_('accepted', s_, value=v, law=L), 'disqualified': E_('disqualified', s_, value=v, law=L), 'exempt': E_('exempt', s_, value=v, law=L), 'atoned_forgiven': E_('atoned_forgiven', s_, value=v, law=L), 'death_by_heaven': E_('death_by_heaven', s_, cp='HEAVEN', value=v, law=L),
             'altar_plated': E_('altar_plated', s_, value=v, law=L), 'rule_installed': E_('rule_installed', s_, value=v, law=L), 'plague_struck': E_('plague_struck', s_, cp='HEAVEN', value=v, law=L), 'staff_budded': E_('staff_budded', s_, value=v, law=L), 'kept_for_a_sign': E_('kept_for_a_sign', s_, value=v, law=L)}
        return [W[x] for x in e if x != FX.NONE]
    if k == 'watch_case':
        v, e, _ = the_watch({'ask': event['ask']}, DATA); L = 'F3 [%s]' % v; s_ = event['person']
        W = {'accepted': E_('accepted', s_, value=v, law=L), 'disqualified': E_('disqualified', s_, value=v, law=L), 'exempt': E_('exempt', s_, value=v, law=L), 'death_by_heaven': E_('death_by_heaven', s_, cp='HEAVEN', value=v, law=L), 'put_to_death': E_('put_to_death', s_, cp='HEAVEN', value=v, law=L),
             'watch_owed': E_('watch_owed', s_, value=v, law=L), 'stranger_barred': E_('stranger_barred', s_, value=v, law=L)}
        return [W[x] for x in e if x != FX.NONE]
    if k == 'stranger_service_case':
        v, e, _ = the_watch({'ask': event['ask']}, DATA); L = 'F3 [%s]' % v; s_ = event['person']
        W = {'accepted': E_('accepted', s_, value=v, law=L), 'disqualified': E_('disqualified', s_, value=v, law=L), 'exempt': E_('exempt', s_, value=v, law=L), 'death_by_heaven': E_('death_by_heaven', s_, cp='HEAVEN', value=v, law=L), 'put_to_death': E_('put_to_death', s_, cp='HEAVEN', value=v, law=L),
             'watch_owed': E_('watch_owed', s_, value=v, law=L), 'stranger_barred': E_('stranger_barred', s_, value=v, law=L)}
        return [W[x] for x in e if x != FX.NONE]
    if k == 'priestly_gifts_case':
        v, e, _ = the_gifts({'ask': event['ask']}, DATA); L = 'F4 [%s]' % v; s_ = event['person']
        W = {'accepted': E_('accepted', s_, value=v, law=L), 'disqualified': E_('disqualified', s_, value=v, law=L), 'exempt': E_('exempt', s_, value=v, law=L), 'due_to_priest': E_('due_to_priest', s_, cp='the-priest', value=v, law=L), 'consecrated_firstborn': E_('consecrated_firstborn', s_, value=v, law=L),
             'redeem_or_break': E_('redeem_or_break', s_, value=v, law=L), 'pays': E_('pays', s_, cp='the-priest', value=v, law=L), 'most_holy': E_('most_holy', s_, value=v, law=L), 'terumah_fed': E_('terumah_fed', s_, value=v, law=L), 'stranger_barred': E_('stranger_barred', s_, value=v, law=L),
             'consecrated': E_('consecrated', s_, value=v, law=L), 'priestly_dues_granted': E_('priestly_dues_granted', s_, value=v, law=L), 'covenant_of_salt': E_('covenant_of_salt', s_, value=v, law=L)}
        return [W[x] for x in e if x != FX.NONE]
    if k == 'tithe_case':
        v, e, _ = the_tithe({'ask': event['ask']}, DATA); L = 'F5 [%s]' % v; s_ = event['person']
        W = {'accepted': E_('accepted', s_, value=v, law=L), 'disqualified': E_('disqualified', s_, value=v, law=L), 'exempt': E_('exempt', s_, value=v, law=L), 'due_to_priest': E_('due_to_priest', s_, cp='the-priest', value=v, law=L), 'pays': E_('pays', s_, cp='the-priest', value=v, law=L),
             'inheritance_barred': E_('inheritance_barred', s_, value=v, law=L), 'tithe_granted': E_('tithe_granted', s_, value=v, law=L), 'terumah_of_the_tithe_owed': E_('terumah_of_the_tithe_owed', s_, cp='the-priest', value=v, law=L)}
        return [W[x] for x in e if x != FX.NONE]
    return []


def scene():
    """THE SCENE — the exam's rows replayed on the world engine (the exodus epoch): Korach's death-mode OPEN, the protesters' exclusion,
    the slanderer atoned by incense, the Levite at another's work, the stranger who served, the priest's watch, the firstborn son's
    thirty days, the betrothed daughter's decree, the devoted field, the Levite's tithe of the tithe, the inferior terumah."""
    with contextlib.redirect_stdout(io.StringIO()):
        w = WE.World(era='Num 16-18: Mishnah Sanhedrin 9-10, Bekhorot 1, 4, 8, Zevachim 5, Terumot 1-2, 4, Ma\'aserot 1, Ma\'aser Sheni 5, Middot 1, Yoma 2 and the Talmud\'s rows on the engine (the exodus epoch)', epoch='exodus')
        w.laws = [law_korach]
        w.advance(w.clock.day_in('exodus', 2, 5, 9))
        w.submit({'kind': 'korach_case', 'subject': 'the-rebel', 'person': 'the-rebel', 'ask': 'death_mode', 'case_source': 'Sanhedrin 110a:13-14; Num 16:32 — Korach not named among the swallowed'})
        w.submit({'kind': 'korach_case', 'subject': 'the-protester', 'person': 'the-protester', 'ask': 'exclusion_by_sin', 'case_source': 'Bava Batra 118b; Num 16:2 — no portion (the inheritance engine called)'})
        w.submit({'kind': 'plague_staff_case', 'subject': 'the-slanderer', 'person': 'the-slanderer', 'ask': 'incense_atones', 'case_source': 'Yoma 44a:5; Num 17:12 — incense atones'})
        w.submit({'kind': 'plague_staff_case', 'subject': 'the-levite-at-the-gate', 'person': 'the-levite-at-the-gate', 'ask': 'levite_at_another_work', 'case_source': 'Arakhin 11b; Num 18:3 — death by Heaven'})
        w.submit({'kind': 'stranger_service_case', 'subject': 'the-stranger-who-served', 'person': 'the-stranger-who-served', 'ask': 'stranger_death', 'case_source': 'Mishnah Sanhedrin 9:6; Num 18:7 — the Bamidbar row called'})
        w.submit({'kind': 'watch_case', 'subject': 'the-priest-of-the-watch', 'person': 'the-priest-of-the-watch', 'ask': 'fence', 'case_source': 'Sifrei Bamidbar 116:1; Num 18:3 — both they and you'})
        w.submit({'kind': 'priestly_gifts_case', 'subject': 'the-firstborn-son', 'person': 'the-firstborn-son', 'ask': 'redemption_before_thirty', 'case_source': 'Bekhorot 49a:6; Num 18:16 — from a month old (Bamidbar called)'})
        w.submit({'kind': 'priestly_gifts_case', 'subject': 'the-betrothed-daughter', 'person': 'the-betrothed-daughter', 'ask': 'betrothed_eats', 'case_source': 'Mishnah Ketubot 5:3; Num 18:11 — the decree over the a-fortiori'})
        w.submit({'kind': 'priestly_gifts_case', 'subject': 'the-devoted-field', 'person': 'the-devoted-field', 'ask': 'devoted_status', 'case_source': 'Arakhin 29a:1; Num 18:14 — given to the priest (the temurah engine called)'})
        w.submit({'kind': 'tithe_case', 'subject': 'the-levite-of-the-tithe', 'person': 'the-levite-of-the-tithe', 'ask': 'tithe_of_the_tithe', 'case_source': 'Menachot 54b:11; Num 18:26 — a tenth of the tenth'})
        w.submit({'kind': 'tithe_case', 'subject': 'the-inferior-terumah', 'person': 'the-inferior-terumah', 'ask': 'inferior_for_superior', 'case_source': 'Bava Batra 84b:2; Num 18:32 — valid, a sin'})
    n = lambda eid, eff: len([e for e in w.entity(eid).ledger if e['effect'] == eff])
    return (n('the-rebel', 'put_to_death'), n('the-protester', 'exempt'), n('the-slanderer', 'atoned_forgiven'), n('the-levite-at-the-gate', 'death_by_heaven'), n('the-stranger-who-served', 'death_by_heaven'),
            n('the-priest-of-the-watch', 'watch_owed'), n('the-firstborn-son', 'pays'), n('the-betrothed-daughter', 'stranger_barred'), n('the-devoted-field', 'due_to_priest'), n('the-levite-of-the-tithe', 'terumah_of_the_tithe_owed'),
            n('the-inferior-terumah', 'due_to_priest'), len(w.entities)), w
SCENE, _W = scene()
SCENE_PREDICTED = (1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 11)   # PREDICTED from the design BEFORE the first run: one effect per row — the rebel's death (the OPEN row), the protester excluded, the slanderer atoned, the Levite at the gate by Heaven, the stranger by Heaven (Bamidbar's row), the priest's watch, the son's five sela at thirty days, the betrothed barred by the decree, the devoted field the priest's, the Levite's tithe of the tithe, the inferior terumah valid; eleven entities
assert SCENE == SCENE_PREDICTED, ('THE NUMBERS WALK: the Korach scene moved from its prediction', SCENE, SCENE_PREDICTED)


def narrative():
    """THE NUMBERS WALK 5b (2026-09-10; NUMBERS_WALK.md "Sitting 5b"): the portion's own acts AS HISTORY — the twenty-five lines of Num 16:1-18:32 in
    the text's order on a world with this runner's daemon, page_order at (2, 5, 9) (no date in the ink, none on the shelf — the running clock's
    day), the two one-day timers ("tomorrow", "on the morrow") firing at (2, 5, 10) on a closing walk. Not a graded cell: the tuple below is a
    tripwire PREDICTED before the first run; the sequence world's RUN tuple grades the tape."""
    with contextlib.redirect_stdout(io.StringIO()):
        w = WE.World(era='Num 16-18: Korach on the tape — the rebellion, the plague, the staffs, the grants (the exodus epoch)', epoch='exodus')
        w.laws = [law_korach]
        w.advance(w.clock.day_in('exodus', 2, 5, 9))
        w.submit({'kind': 'korach_gathered_against', 'subject': 'korach', 'parties': ['korach', 'dathan', 'abiram', 'on'], 'count': C250[0], 'words': 'too much for you; all the congregation are holy', 'case_source': 'Num 16:1-3 — and Korach son of Izhar son of Kohath son of Levi took, and Dathan and Abiram sons of Eliab and On son of Peleth, sons of Reuben; and they rose before Moses with men of the children of Israel, two hundred and fifty princes of the congregation, called to the assembly, men of name; and they gathered against Moses and against Aaron and said to them: too much for you'})
        w.submit({'kind': 'moses_set_the_test', 'subject': 'moses', 'test': 'in the morning the LORD will make known who is His', 'when': 'tomorrow', 'case_source': 'Num 16:4-7 — and Moses heard and fell on his face; and he spoke to Korach and to all his congregation saying: in the morning the LORD will make known who is His and who is holy... take for yourselves censers... and put incense on them before the LORD tomorrow'})
        w.submit({'kind': 'levites_rebuked', 'subject': 'moses', 'words': 'is it too little; you seek the priesthood too; gathered against the LORD', 'case_source': 'Num 16:8-11 — and Moses said to Korach: hear now, sons of Levi: is it too little for you that the God of Israel has separated you... and you seek the priesthood too? therefore you and all your congregation are gathered against the LORD'})
        w.submit({'kind': 'dathan_and_abiram_refused', 'subject': 'dathan', 'words': 'we will not go up; will you put out the eyes of these men', 'case_source': 'Num 16:12-14 — and Moses sent to call Dathan and Abiram sons of Eliab, and they said: we will not go up... will you put out the eyes of these men? we will not go up'})
        w.submit({'kind': 'moses_swore', 'subject': 'moses', 'words': 'do not turn to their offering; not one ass have I taken from them', 'case_source': 'Num 16:15 — and it was hot to Moses, very, and he said to the LORD: do not turn to their offering; not one ass have I taken from them, nor have I wronged one of them'})
        w.submit({'kind': 'censers_commanded', 'subject': 'moses', 'count': C250[1], 'when': 'tomorrow', 'case_source': 'Num 16:16-17 — and Moses said to Korach: you and all your congregation, be before the LORD, you and they and Aaron, tomorrow; and take each his censer... two hundred and fifty censers'})
        w.submit({'kind': 'censers_offered_at_the_tent', 'subject': 'the-two-hundred-fifty', 'at': 'the entrance of the tent of meeting', 'case_source': 'Num 16:18-19 — and they took each his censer and put fire on them and put incense on them, and they stood at the entrance of the tent of meeting, with Moses and Aaron; and Korach gathered all the congregation against them... and the glory of the LORD appeared to all the congregation'})
        w.submit({'kind': 'separation_commanded', 'subject': 'moses', 'words': 'separate yourselves from among this congregation and I will consume them in a moment', 'case_source': 'Num 16:20-21 — and the LORD spoke to Moses and to Aaron saying: separate yourselves from among this congregation and I will consume them in a moment'})
        w.submit({'kind': 'moses_and_aaron_pleaded', 'subject': 'moses', 'words': 'God of the spirits of all flesh, shall one man sin', 'case_source': 'Num 16:22 — and they fell on their faces and said: O God, God of the spirits of all flesh, shall one man sin and You be wroth with all the congregation'})
        w.submit({'kind': 'get_up_commanded', 'subject': 'israel', 'words': 'get up from around the dwelling of Korach, Dathan and Abiram', 'case_source': 'Num 16:23-24 — and the LORD spoke to Moses saying: speak to the congregation saying: get up from around the dwelling of Korach, Dathan and Abiram'})
        w.submit({'kind': 'congregation_withdrew', 'subject': 'israel', 'went': 'Moses to Dathan and Abiram, the elders after him', 'words': 'turn aside from the tents of these wicked men', 'case_source': 'Num 16:25-27 — and Moses rose and went to Dathan and Abiram... turn aside, I pray, from the tents of these wicked men... and they got up from around the dwelling of Korach, Dathan and Abiram; and Dathan and Abiram came out standing at the entrance of their tents'})
        w.submit({'kind': 'creation_test_declared', 'subject': 'moses', 'arms': ['the common death — the LORD has not sent me', 'a new creation, the ground opens its mouth — these men have scorned the LORD'], 'case_source': 'Num 16:28-30 — and Moses said: by this you shall know that the LORD has sent me... if these die as all men die... but if the LORD creates a creation and the ground opens its mouth and swallows them... then you shall know that these men have scorned the LORD'})
        w.submit({'kind': 'earth_swallowed', 'subject': 'dathan', 'swallowed': ['dathan', 'abiram', 'their households', 'every person who belonged to Korach'], 'korach_named': False, 'households': True, 'case_source': 'Num 16:31-34 — and it was, as he finished speaking all these words, the ground under them split; and the earth opened its mouth and swallowed them and their houses and every person who belonged to Korach and all the property; and they and all that was theirs went down alive to Sheol'})
        w.submit({'kind': 'fire_consumed_the_two_hundred_fifty', 'subject': 'the-two-hundred-fifty', 'count': C250[2], 'mode': 'fire from with the LORD', 'case_source': 'Num 16:35 — and fire went out from with the LORD and consumed the two hundred and fifty men who offered the incense'})
        w.submit({'kind': 'censers_beaten_into_plates', 'subject': 'eleazar', 'by': 'eleazar', 'into': 'a covering for the altar', 'installs': 'law_korach:stranger_incense', 'case_source': "Num 17:1-5 — and the LORD spoke to Moses saying: say to Eleazar son of Aaron the priest that he lift the censers from among the burning... and let them be made beaten plates, a covering for the altar... a memorial to the children of Israel, that no stranger who is not of Aaron's seed shall come near to burn incense before the LORD"})
        w.submit({'kind': 'congregation_murmured_you_killed', 'subject': 'israel', 'words': 'you have killed the people of the LORD', 'case_source': 'Num 17:6-7 — and all the congregation of the children of Israel murmured on the morrow against Moses and against Aaron saying: you have killed the people of the LORD; and it was, when the congregation gathered against Moses and against Aaron, they turned to the tent of meeting, and behold the cloud covered it and the glory of the LORD appeared'})
        w.submit({'kind': 'plague_begun_and_stayed', 'subject': 'israel', 'dead': PLAGUE, 'besides': 'the dead over the matter of Korach', 'stayed_by': 'the incense between the dead and the living', 'case_source': 'Num 17:8-15 — and Moses and Aaron came before the tent of meeting... take the censer and put fire on it from off the altar and put incense... and Aaron took as Moses spoke and ran into the midst of the assembly, and behold the plague had begun among the people, and he put the incense and atoned for the people; and he stood between the dead and the living, and the plague was stayed; and the dead in the plague were fourteen thousand and seven hundred'})
        w.submit({'kind': 'staffs_commanded', 'subject': 'moses', 'count': STAFFS[0], 'levi_among': True, 'case_source': "Num 17:16-20 — and the LORD spoke to Moses saying: speak to the children of Israel and take from them a staff, a staff for a father's house... twelve staffs... and Aaron's name you shall write on the staff of Levi... and you shall lay them in the tent of meeting before the testimony"})
        w.submit({'kind': 'staffs_laid_and_budded', 'subject': 'aarons-staff', 'count': STAFFS_21[2], 'levi_among': True, 'budded': 'a bud, a blossom, almonds', 'case_source': "Num 17:21-24 — and Moses spoke to the children of Israel, and all their princes gave him a staff for one prince, a staff for one prince... twelve staffs, and Aaron's staff among their staffs; and Moses laid the staffs before the LORD in the tent of the testimony; and it was on the morrow, Moses came into the tent of the testimony, and behold, the staff of Aaron for the house of Levi had budded"})
        w.submit({'kind': 'aarons_staff_kept', 'subject': 'aarons-staff', 'where': 'before the testimony', 'beside': 'the jar of manna (Exod 16:34)', 'case_source': "Num 17:25-26 — and the LORD said to Moses: return Aaron's staff before the testimony for a keeping, for a sign to the sons of rebellion, and you shall end their murmurings from Me, that they die not; and Moses did as the LORD commanded him"})
        w.submit({'kind': 'congregation_despaired', 'subject': 'israel', 'words': 'we expire, we perish, all of us perish', 'case_source': 'Num 17:27-28 — and the children of Israel said to Moses saying: behold, we expire, we perish, all of us perish; everyone who comes near, who comes near to the tabernacle of the LORD, dies; have we finished expiring'})
        w.submit({'kind': 'watch_given_to_aaron', 'subject': 'aaron', 'fence': 'both they and you', 'stranger': 'the stranger who comes near shall be put to death', 'no_more_wrath': True, 'case_source': "Num 18:1-7 — and the LORD said to Aaron: you and your sons and your father's house with you shall bear the iniquity of the sanctuary... they shall keep your watch and the watch of all the tent... both they and you... and a stranger shall not come near to you; and you shall keep the watch of the holy and the watch of the altar, and there shall be no more wrath upon the children of Israel... a service of gift I give your priesthood; and the stranger who comes near shall be put to death"})
        w.submit({'kind': 'gifts_granted', 'subject': 'aaron', 'gifts': 24, 'salt': True, 'case_source': 'Num 18:8-19 — and the LORD spoke to Aaron: and I, behold, I have given you the watch of My terumot, of all the hallowed things of the children of Israel; to you I have given them for anointing and to your sons, an everlasting statute... a covenant of salt forever it is before the LORD, for you and your seed with you'})
        w.submit({'kind': 'portion_declared', 'subject': 'the-levites', 'portion': 'I am your portion and your inheritance', 'tithe': 'all the tithe in Israel', 'condition': 'in exchange for their service', 'case_source': 'Num 18:20-24 — and the LORD said to Aaron: in their land you shall not inherit, and you shall have no portion among them; I am your portion and your inheritance among the children of Israel; and to the sons of Levi, behold, I have given all the tithe in Israel for an inheritance in exchange for their service... among the children of Israel they shall inherit no inheritance'})
        w.submit({'kind': 'tithe_of_the_tithe_commanded', 'subject': 'the-levites', 'fraction': str(TITHE_OF_TITHE), 'reckoned_as': 'the grain from the threshing floor and the fullness of the winepress', 'the_best': True, 'case_source': 'Num 18:25-32 — and the LORD spoke to Moses saying: and to the Levites you shall speak and say to them: when you take from the children of Israel the tithe... you shall lift from it a terumah of the LORD, a tithe from the tithe; and your terumah shall be reckoned to you as the grain from the threshing floor... and you may eat it in every place, you and your household, for it is your wage... and you shall not die'})
        w.advance(w.clock.day_in('exodus', 2, 5, 15))     # a closing walk: the two one-day timers fire at (2, 5, 10)
    n = lambda eid, eff: len([e for e in w.entity(eid).ledger if e['effect'] == eff])
    is_open = lambda eid, eff: [e.get('open') for e in w.entity(eid).ledger if e['effect'] == eff]
    L = lambda k: len([l for l in w.log if l[0] == k])
    ex = w.clock.eras['exodus']
    markers = [l for l in w.log if l[0] == 'MARKER']
    fires = [l for l in w.log if l[0] == 'TIMER-FIRE']
    return (n('korach', 'gathered_against'), n('korach', 'commanded'), is_open('korach', 'commanded'), n('korach', 'put_to_death'),
            n('dathan', 'gathered_against'), n('dathan', 'refused'), n('dathan', 'put_to_death'), n('abiram', 'put_to_death'),
            n('the-two-hundred-fifty', 'put_to_death'),
            n('moses', 'plea_made'), n('moses', 'commanded'), is_open('moses', 'commanded'),
            n('aaron', 'plea_made'), n('aaron', 'watch_owed'), n('aaron', 'priestly_dues_granted'), n('aaron', 'covenant_of_salt'), n('aaron', 'inheritance_barred'),
            n('israel', 'commanded'), is_open('israel', 'commanded'), n('israel', 'test_set'), n('israel', 'gathered_against'), n('israel', 'plague_struck'), n('israel', 'atoned_forgiven'), n('israel', 'plague_removed'), n('israel', 'plea_made'),
            n('the-tabernacle', 'glory_appeared'), n('the-altar', 'altar_plated'), n('the-priesthood', 'rule_installed'),
            n('aarons-staff', 'staff_budding_awaited'), n('aarons-staff', 'staff_budded'), n('aarons-staff', 'kept_for_a_sign'),
            n('the-levites', 'watch_owed'), n('the-levites', 'inheritance_barred'), n('the-levites', 'tithe_granted'), n('the-levites', 'terumah_of_the_tithe_owed'),
            L('TIMER-SET'), L('TIMER-FIRE'), [ex.date(f[1]) for f in fires], len(markers), L('EVENT'), L('WRITE'), len(w.entities)), w


NARRATIVE, _WN = narrative()
NARRATIVE_PREDICTED = (1, 1, [False], 1,
                       1, 1, 1, 1,
                       1,
                       2, 1, [False],
                       1, 1, 1, 1, 1,
                       1, [False], 1, 1, 1, 1, 1, 1,
                       2, 1, 1,
                       1, 1, 1,
                       1, 1, 1, 1,
                       2, 2, [(2, 5, 10), (2, 5, 10)], 0, 25, 37, 12)   # PREDICTED from the design BEFORE the first run (NUMBERS_WALK.md "Sitting 5b"): Korach gathered, the censers' debit closed by 16:18, his death the OPEN row; Dathan and Abiram gathered, refused, swallowed; the 250 burned; Moses' two pleas and the staffs' debit closed by 17:22; Aaron's plea, his watch, his dues, his salt, his no-inheritance; Israel's get-up closed by 16:27, the test set, the murmur, the plague struck and stayed and atoned, the despair; the glory twice on the tent; the altar plated; the rule installed on the priesthood; Aaron's staff timed, budded, kept; the Levites' watch, no-inheritance, tithe, tithe of the tithe; two timers set and fired at (2, 5, 10); no marker; twenty-five events; thirty-seven writes (the thirty-five at the lines + the two fires — a timer's setting is not a write); twelve entities
assert NARRATIVE == NARRATIVE_PREDICTED, ('THE NUMBERS WALK: Korach\'s narrative moved from its prediction', NARRATIVE, NARRATIVE_PREDICTED)


# =====================================================================
# Motion 2 — THE TEST DATA: the answer sheet's rows (the docket's LAW rows).
# =====================================================================
CASES = [
    # F1 — the rebellion
    ('Num 16:1; Onkelos; Sanhedrin 109b:13 — took', lambda: rebellion({'ask': 'took'}, DATA), 'took — no object; Onkelos: divided himself; a bad acquisition (Sanhedrin 109b)'),
    ('Num 16:2, 16:17, 16:35 — the 250 (computed; the definite numeral)', lambda: rebellion({'ask': 'two_hundred_fifty'}, DATA), '250 — the parser at 16:2, 16:17 and 16:35 (the definite numeral at the head of a compound)'),
    ('Sotah 13b:13 — too much returned', lambda: rebellion({'ask': 'too_much_returned'}, DATA), 'too much for you (16:3) returned at 16:7; proclaimed to Moses at Deut 3:26 (Sotah 13b)'),
    ('Berakhot 21b:5; Megillah 23b:7; Sanhedrin 74b:3 — the congregation of ten', lambda: rebellion({'ask': 'congregation_ten'}, DATA), '10 — among / among with the sanctification of the Name; congregation / congregation with the spies (Berakhot 21b; Megillah 23b; Sanhedrin 74b)'),
    ('Moed Katan 16a:3-5 — the summons', lambda: rebellion({'ask': 'summons_procedure'}, DATA), 'the agent sent (16:12); in person (16:16); before a great man; both parties named; a date set — tomorrow; the report of disrespect permitted (Moed Katan 16a)'),
    ('Sanhedrin 110a; Num 16:5-7 — the test', lambda: rebellion({'ask': 'test'}, DATA), 'in the morning the LORD will make known (16:5) — the boundary fixed at creation (Sanhedrin 110a); the censers tomorrow (16:7, 16:16) — the one-day timer'),
    ('Nedarim 38a:13; Megillah 9b:1 — the oath', lambda: rebellion({'ask': 'oath'}, DATA), "not one ass (16:15) — Samuel's whose ox, whose ass (1 Sam 12:3; Nedarim 38a); the Cain echo (Gen 4:5)"),
    ('Shevuot 39a:7 — the oath\'s warning formula', lambda: rebellion({'ask': 'oath_warning_formula'}, DATA), '16:26 recited at the oath — depart from the tents of these wicked men (Shevuot 39a)'),
    ('Mishnah Avot 5:6; Sanhedrin 110a:16; Nedarim 39b:3 — the new creation', lambda: rebellion({'ask': 'new_creation'}, DATA), "the mouth of the earth created at the twilight of the sixth day (Avot 5:6); if not, create it now — Gehenna's opening brought near (Sanhedrin 110a:16; Nedarim 39b)"),
    ('Sanhedrin 110a:13-14; Num 16:32 / 26:10 — the death mode (the OPEN row)', lambda: rebellion({'ask': 'death_mode'}, DATA), 'OPEN — 16:32 names the men who belonged to Korach, not Korach; 26:10 adds and Korach; R. Yochanan: the plague; the baraita: burned and swallowed (Sanhedrin 110a)'),
    ('Mishnah Sanhedrin 10:3; Sanhedrin 108a, 109b:11-12 — the share', lambda: rebellion({'ask': 'share'}, DATA), 'R. Akiva: no share and no rising; R. Eliezer: the LORD kills and makes alive (Mishnah Sanhedrin 10:3); R. Yehuda ben Beteira: a lost item sought (Sanhedrin 109b)'),
    ('Num 26:11; Sanhedrin 110a — the sons of Korach', lambda: rebellion({'ask': 'sons_of_korach'}, DATA), 'the sons of Korach did not die (26:11) — a place fortified for them (Sanhedrin 110a); the eleven Psalm headings'),
    ('Bava Batra 118b — the exclusion by sin (the inheritance engine CALLED)', lambda: rebellion({'ask': 'exclusion_by_sin'}, DATA), "no portion — the spies, the protesters (Korach's two hundred fifty) and Korach's congregation"),
    ('Mishnah Avot 5:17 — not for Heaven\'s sake', lambda: rebellion({'ask': 'not_for_heaven'}, DATA), "a dispute not for Heaven's sake — Korach and all his congregation (Avot 5:17)"),
    ('Sanhedrin 37b:11 — the earth\'s mouth and Abel', lambda: rebellion({'ask': 'earth_mouth_cain'}, DATA), 'the ground opened its mouth for Abel\'s blood and for Korach — for a deleterious purpose (Sanhedrin 37b); Gen 4:11, Deut 11:6'),
    ('Num 16:31-33; Deut 11:6; Ps 106:17 — swallowed', lambda: rebellion({'ask': 'swallowed'}, DATA), 'Dathan and Abiram and their households swallowed alive (16:31-33); Deut 11:6, Ps 106:17 name them alone'),
    ('Num 16:35; Sanhedrin 52a:10-12 — the fire', lambda: rebellion({'ask': 'fire'}, DATA), 'fire from with the LORD consumed the 250 (16:35) — the souls burned, the bodies intact (Sanhedrin 52a); Lev 9:24, 10:2 from before'),
    ('Sanhedrin 109b:15-16 — the wives', lambda: rebellion({'ask': 'wives'}, DATA), "On's wife saved him — the wine and the tent's entrance; Korach's wife incited (Sanhedrin 109b-110a)"),
    ('Sanhedrin 109b:13-15 — the names', lambda: rebellion({'ask': 'names'}, DATA), "Korach a void; Izhar the afternoon heat; Dathan the precepts; Abiram braced; On in mourning (Sanhedrin 109b) — the names' lore; Izhar = fresh oil the ink's pointed word (18:12)"),
    ('Nedarim 39b:2 — visiting the sick', lambda: rebellion({'ask': 'visiting_the_sick'}, DATA), 'alluded from the visitation of all men (16:29 — Nedarim 39b)'),
    ('Sanhedrin 110a:4 — the elect', lambda: rebellion({'ask': 'elect'}, DATA), 'the elect of the assembly = those who intercalate; men of renown (Sanhedrin 110a:4)'),
    ('Sanhedrin 110a:5 — what Moses heard', lambda: rebellion({'ask': 'what_moses_heard'}, DATA), 'suspected of adultery — Ps 106:16 (Sanhedrin 110a:5)'),
    # F2 — the plague and the staffs
    ('Menachot 99a:11 — elevate in sanctity', lambda: plague_and_staffs({'ask': 'elevate_in_sanctity'}, DATA), "one elevates in sanctity — the censers, service vessels, became the altar's covering (Menachot 99a)"),
    ('Sanhedrin 52a:10-12 — the burning\'s mode', lambda: plague_and_staffs({'ask': 'burning_mode'}, DATA), 'the souls burned, the bodies intact (17:3 sinned against their souls; Sanhedrin 52a) — the capital burning\'s likeness'),
    ('Num 17:5 — the stranger\'s incense ban (the output)', lambda: plague_and_staffs({'ask': 'stranger_incense_ban'}, DATA), "no stranger not of Aaron's seed to burn incense (17:5) — the output by the hand of Moses to him; rule installed on the priesthood"),
    ('Sanhedrin 110a:6 — maintaining a dispute', lambda: plague_and_staffs({'ask': 'maintaining_a_dispute'}, DATA), 'one may not perpetuate a dispute — a prohibition from not to be as Korach (Rav; Reish Lakish on 16:25 — Sanhedrin 110a); R. Ashi: leprosy'),
    ('Yoma 44a:5; Arakhin 16a:19; Zevachim 88b:10 — incense atones', lambda: plague_and_staffs({'ask': 'incense_atones'}, DATA), 'incense atones — for slander: the private for the private (Yoma 44a; Arakhin 16a; Zevachim 88b)'),
    ('Shabbat 89a:2 — the angel of death', lambda: plague_and_staffs({'ask': 'angel_of_death'}, DATA), 'the angel of death gave Moses the remedy (Shabbat 89a)'),
    ('Num 17:14 — the plague\'s count (computed)', lambda: plague_and_staffs({'ask': 'plague_count'}, DATA), "14,700 — besides the dead over the matter of Korach (17:14, the parser's)"),
    ('Num 17:11; Lev 16:12 — fire from off the altar', lambda: plague_and_staffs({'ask': 'fire_from_the_altar'}, DATA), "from off the altar (17:11) — the Day of Atonement's phrase (Lev 16:12); against the strange fire (Lev 10:1)"),
    ('Num 17:17-21 — the staffs (computed)', lambda: plague_and_staffs({'ask': 'staffs_count'}, DATA), "12 — a staff for a father's house, Aaron's on Levi's, among their staffs (17:17-21 — the parser's [12], [1, 1, 12])"),
    ('Num 17:23; Exod 28:36 — budded', lambda: plague_and_staffs({'ask': 'budded'}, DATA), "a bud, a blossom (the frontplate's word), almonds (once; the menorah's cups) — on the morrow (17:23)"),
    ('Horayot 12a:1-3; Keritot 5b:16-20; Yoma 52b:15 — the staff hidden', lambda: plague_and_staffs({'ask': 'staff_hidden'}, DATA), 'hidden with the ark, the jar of manna and the anointing oil (Horayot 12a; Keritot 5b; Yoma 52b) — the keepsake / keepsake analogy'),
    ('Onkelos Num 17:27 — three deaths', lambda: plague_and_staffs({'ask': 'three_deaths'}, DATA), 'we expire, we perish, all of us perish (17:27) — Onkelos: the sword, the earth, the plague'),
    ('Arakhin 11b — the Levite at another\'s work', lambda: plague_and_staffs({'ask': 'levite_at_another_work'}, DATA), "a Levite at the priests' work or another Levite's — death by Heaven (Arakhin 11b)"),
    ('Sanhedrin 84a:13 — whoever comes near', lambda: plague_and_staffs({'ask': 'whoever_comes_near'}, DATA), "whoever comes near dies (17:28) with 18:7's shall be put to death — R. Yishmael: death by Heaven (Sanhedrin 84a)"),
    # F3 — the watch
    ('Sifrei 116:1 — the iniquity of the sanctuary (the tzav engine CALLED)', lambda: the_watch({'ask': 'iniquity_of_the_sanctuary'}, DATA), "the priests' mishandled offerings (Sifrei 116:1 — R. Yoshiyah); Eli's sons the recorded violation (tzav CALLED)"),
    ('Sifrei 116:1 — the iniquity of the priesthood', lambda: the_watch({'ask': 'iniquity_of_the_priesthood'}, DATA), 'keeping strangers out (Sifrei 116:1)'),
    ('Arakhin 11b:2 — the song', lambda: the_watch({'ask': 'song'}, DATA), "the Levites' altar-service is the song — neither they nor you (Arakhin 11b; Sifrei 116:1)"),
    ('Sifrei 116:1; Arakhin 11b — the two-way fence', lambda: the_watch({'ask': 'fence'}, DATA), "both they and you — the priests not the Levites' work, the Levites not the priests' (18:3; Sifrei 116:1; Arakhin 11b)"),
    ('Tamid 26b:3-4; Mishnah Middot 1:5, 1:9 — above and below', lambda: the_watch({'ask': 'watch_stories'}, DATA), 'the priests above, the Levites below (Tamid 26b; Mishnah Middot 1:5); the priest locks within, the Levite sleeps outside (Middot 1:9)'),
    ('Mishnah Middot 1:1-2; Tamid 1:1 — the watch places', lambda: the_watch({'ask': 'watch_places'}, DATA), '3 and 21 — the priests in three places, the Levites in twenty-one (Mishnah Middot 1:1; Tamid 1:1); the sleeping watchman beaten (Middot 1:2)'),
    ('Zevachim 16a:5; Sifrei 116:1 — the warning', lambda: the_watch({'ask': 'stranger_warning'}, DATA), '18:4 the warning — a stranger shall not come near to you (Zevachim 16a; Sifrei 116:1)'),
    ('Mishnah Sanhedrin 9:6; Sanhedrin 83b:4, 84a:13 — the stranger\'s death (Bamidbar\'s row CALLED)', lambda: the_watch({'ask': 'stranger_death'}, DATA), "death by Heaven — the Rabbis; R. Akiva: strangulation (Mishnah Sanhedrin 9:6; Sanhedrin 83b, 84a) — Bamidbar's row zar_who_served by CALL: death_by_heaven"),
    ('Yoma 24a:7, 24b:1, 27a:1; Sifrei 116:2 — the death\'s scope', lambda: the_watch({'ask': 'stranger_death_scope'}, DATA), 'a service of giving and complete — not removal, not slaughter; within the veil the giving services (Yoma 24a-b, 27a); only for a service, even in purity (Sifrei 116:2)'),
    ('Sifrei 116:1; Num 18:5 / 1:53 — no more wrath (computed)', lambda: the_watch({'ask': 'no_more_wrath'}, DATA), "18:5 = 1:53's clause with one token added — no MORE wrath (computed); the four no-mores each paid by a prior event (Sifrei 116:1)"),
    ('Sifrei 116:2 — given to the LORD', lambda: the_watch({'ask': 'given_to_the_lord'}, DATA), 'a gift, given to the LORD (18:6) — to the LORD, not to the priests (Sifrei 116:2); the third form (3:9, 8:16)'),
    ('Pesachim 73a:1; Sifrei 116:2 — a service of gift', lambda: the_watch({'ask': 'service_of_gift'}, DATA), 'a service of gift — the lots (Mishnah Yoma 2:1-2: four lotteries); eating terumah in the provinces equated (Pesachim 73a; Sifrei 116:2)'),
    ('Mishnah Yoma 2:1-7; Tamid 1:2 — the lots', lambda: the_watch({'ask': 'lots'}, DATA), 'four lotteries — the ashes, the thirteen, the incense, the limbs (Mishnah Yoma 2:1-4); nine to twelve priests (2:5); the ram eleven, the bull twenty-four (2:6-7)'),
    ('Mishnah Middot 5:4; Sifrei 116:2 — the genealogy chamber', lambda: the_watch({'ask': 'genealogy_chamber'}, DATA), 'within the veil — the chamber of hewn stone judges the priesthood: black and white (Mishnah Middot 5:4; Sifrei 116:2)'),
    ('Sifrei 116:2; Chullin 106a — the washing of the hands', lambda: the_watch({'ask': 'washing_hands'}, DATA), 'the washing of the hands scriptural (Sifrei 116:2; Chullin 106a)'),
    ('Sifrei 116:1 (Rebbi) — why reiterate', lambda: the_watch({'ask': 'why_reiterate'}, DATA), 'because Korach came, Scripture reiterated the exhortation (Sifrei 116:1 — Rebbi)'),
    # F4 — the gifts
    ('Sifrei 117:1 — with joy', lambda: the_gifts({'ask': 'with_joy'}, DATA), "and I, behold — with joy (Sifrei 117:1); through Moses by 17:5's to him"),
    ('Sifrei 117:2, 119:2 — the covenant\'s reason', lambda: the_gifts({'ask': 'covenant_reason'}, DATA), "the covenant written because Korach contested — the king's retainer (Sifrei 117:2); for Aaron's good did Korach come (119:2)"),
    ('Zevachim 91a:19; Chullin 132b:14; Sotah 15a:5 — eaten in greatness (Onkelos cited)', lambda: the_gifts({'ask': 'eaten_in_greatness'}, DATA), 'for anointing = for greatness — eaten as kings eat, roasted with mustard, any manner (Onkelos cited at Zevachim 91a; Chullin 132b; Sotah 15a)'),
    ('Chullin 133b:11; Sifrei 119:1-2 — the twenty-four (computed on the list)', lambda: the_gifts({'ask': 'twenty_four'}, DATA), '24 — twelve in the sanctuary, twelve in the borders (Sifrei 119:1-2; Chullin 133b; Bava Kamma 110b); a generalization, a detail and a covenant of salt'),
    ('Menachot 73a:9; Zevachim 44b:4 — the most holy list', lambda: the_gifts({'ask': 'most_holy_list'}, DATA), "every offering, every meal offering, every sin offering, every guilt offering (18:9) — the four everys include the omer's, the suspected wife's, the bird olah's meat, the leper's log (Menachot 73a; Zevachim 44b)"),
    ('Sifrei 117:2 — from the fire', lambda: the_gifts({'ask': 'from_the_fire'}, DATA), "the olah's hide — the most holy from the fire (Sifrei 117:2)"),
    ('Sifrei 117:2; Bava Kamma 110a — which they return', lambda: the_gifts({'ask': 'returned'}, DATA), "which they return to Me — the proselyte's theft (5:8; Sifrei 117:2; Bava Kamma 110a)"),
    ('Menachot 9a:1; Zevachim 63a:15 — the eating place', lambda: the_gifts({'ask': 'most_holy_eating_place'}, DATA), 'in the most holy place — the courtyard; inside the Sanctuary when gentiles surround it (Zevachim 63a; Menachot 9a)'),
    ('Menachot 83a:2; Zevachim 97b:11 — every male', lambda: the_gifts({'ask': 'every_male'}, DATA), "every male — communal peace offerings eaten by the priests' males (Menachot 83a; Zevachim 97b)"),
    ('Kiddushin 52b:16 — the portion\'s use', lambda: the_gifts({'ask': 'most_holy_portion_use'}, DATA), 'R. Yehuda: betrothed with it; R. Yosei: consumption alone (Kiddushin 52b)'),
    ('Shabbat 25a:2, 26a:5; Yevamot 74a:18 — impure terumah\'s benefit', lambda: the_gifts({'ask': 'impure_terumah_benefit'}, DATA), 'My terumot — two: the impure burned with benefit beneath the dish, from the separation onward (Shabbat 25a-26a; Yevamot 74a)'),
    ('Bekhorot 34a:6 — the doubtful terumah\'s watch', lambda: the_gifts({'ask': 'doubtful_terumah_watch'}, DATA), 'R. Yehoshua: safeguard only the pure; R. Eliezer: the doubtful too (Bekhorot 34a)'),
    ('Num 18:11; Lev 7:34 — the breast and thigh (the tzav engine CALLED)', lambda: the_gifts({'ask': 'breast_and_thigh'}, DATA), 'breast and thigh to the priests after the smoking (tzav CALLED); the terumah of their gift, all the wave offerings (18:11)'),
    ('Num 18:11, 18:13; Lev 22:11-13 — the household (the priesthood engine CALLED)', lambda: the_gifts({'ask': 'household'}, DATA), 'every clean one in your house — the household (priesthood CALLED); to your daughters'),
    ('Sifrei 117:2; Mishnah Ketubot 5:3 — the betrothed daughter (the decree over the a-fortiori)', lambda: the_gifts({'ask': 'betrothed_eats'}, DATA), 'the a-fortiori: she eats (R. Yochanan b. Bag Bag); THE DECREE: not until the canopy (Mishnah Ketubot 5:3 — the later court; Ketubot 57b-58a: the cup and the simpon) — the decree over the a-fortiori'),
    ('Num 18:12; Bekhorot 53b:17, 54b:2 — the best triad (computed)', lambda: the_gifts({'ask': 'the_best_triad'}, DATA), "the best of the oil, the wine and the grain (18:12) — Izhar's word; the triad reversed against eleven seats (computed); kind for kind: each type its first (Bekhorot 53b, 54b)"),
    ('Sifrei 117:2; Chullin 136a:8; Menachot 84b — the first fruits', lambda: the_gifts({'ask': 'bikkurim'}, DATA), 'the first fruits of all — holy while attached (18:13; Sifrei 117:2); partners liable, outside the land exempt (Chullin 136a); roofs and ships (Menachot 84b); the household eats (84b:10)'),
    ('Sifrei 117:3; Mishnah Arakhin 8:6 — the devotions (the temurah engine CALLED)', lambda: the_gifts({'ask': 'devoted'}, DATA), "every devoted thing in Israel — gentiles', women's, bondsmen's too (Sifrei 117:3); unspecified: priests_Sages_upkeep_R._Yehuda_b._Beteira (temurah CALLED) — the four-way dispute: R. Yossi HaGelili the priests, R. Yehudah b. Beteira Temple maintenance, R. Yehudah b. Bava the priests, R. Shimon Heaven"),
    ('Arakhin 29a:1, 28b:1; Bekhorot 32a:25 — the devoted\'s status', lambda: the_gifts({'ask': 'devoted_status'}, DATA), 'in the owner\'s house consecrated; given to the priest common (Arakhin 29a; Bekhorot 32a); to the priest of the watch serving (Arakhin 28b)'),
    ('Arakhin 28b:1 — devoted to whom', lambda: the_gifts({'ask': 'devoted_to_whom'}, DATA), 'to the priest of the watch serving in the Temple — to the priest / to the priest with 5:8 (Arakhin 28b)'),
    ('Mishnah Arakhin 8:5; Arakhin 28a:12 — devotion by priests', lambda: the_gifts({'ask': 'devotion_by_priests'}, DATA), 'R. Yehuda: priests and Levites may not; R. Shimon: priests not, Levites may (Mishnah Arakhin 8:5)'),
    ('Mishnah Arakhin 8:7 — devote the firstborn (the temurah engine CALLED)', lambda: the_gifts({'ask': 'devote_firstborn'}, DATA), "the firstborn, whole or blemished, may be devoted — assessed by the daughter's son (Mishnah Arakhin 8:7; temurah CALLED: may_be_devoted)"),
    ('Sifrei 118:1; Bekhorot 4a:6 — all that opens the womb', lambda: the_gifts({'ask': 'opens_the_womb'}, DATA), "all that opens the womb — which they offer excludes the unclean animal, and in beast re-includes the blemished (Sifrei 118:1); the Levites' ass exempt"),
    ('Num 18:16 / 3:47 — the rate (the Bamidbar engine CALLED)', lambda: the_gifts({'ask': 'redemption_rate'}, DATA), "five shekels per skull; twenty gerah the shekel (the sela of twenty ma'ah)"),
    ('Bekhorot 49a:6; Bava Kamma 11b:2; Mishnah Bekhorot 8:6 — thirty days (the Bamidbar engine CALLED)', lambda: the_gifts({'ask': 'redemption_before_thirty'}, DATA), 'after thirty days — from a month old (18:16 / 3:40; Bekhorot 49a; Bamidbar CALLED: after thirty days); mauled within thirty — no redemption (Bava Kamma 11b); the thirtieth day like the day before (Mishnah Bekhorot 8:6)'),
    ('Bekhorot 12b:23, 13a:3; Sifrei 118:1 — the timing', lambda: the_gifts({'ask': 'redemption_timing'}, DATA), 'thirty days the son, at once the ass (Bekhorot 12b-13a; Sifrei 118:1 — immediately or after a month)'),
    ('Mishnah Bekhorot 8:8; Sifrei 118:1; Bekhorot 51a:10 — the means (the Bamidbar engine CALLED)', lambda: the_gifts({'ask': 'redemption_means'}, DATA), 'redeemed when in the priest\'s hand (Bamidbar CALLED); not with slaves, notes, land or consecrated items (Mishnah Bekhorot 8:8); movable, not writs (Sifrei 118:1 — Rebbi: writs only)'),
    ('Bekhorot 50a:6; Sifrei 118:1 — twenty gerah (the shekel engine CALLED)', lambda: the_gifts({'ask': 'twenty_gerah_floor'}, DATA), 'twenty gerah — more, not less (Sifrei 118:1; Bekhorot 50a); the seat among the shekel engine\'s five: Num 18:16'),
    ('Mishnah Bekhorot 8:7; Bekhorot 49b:10-11; Kiddushin 11b:7 — the coinage', lambda: the_gifts({'ask': 'five_sela_coinage'}, DATA), 'the five sela in the Tyrian maneh (Mishnah Bekhorot 8:7; Bekhorot 49b)'),
    ('Kiddushin 29a:15; Sifrei 118:1 — redeem, you shall redeem', lambda: the_gifts({'ask': 'self_redemption'}, DATA), 'redeem, you shall redeem — the son redeems himself if the father did not (Kiddushin 29a; Sifrei 118:1 Kerem Beyavneh)'),
    ('Mishnah Bekhorot 8:8; Bekhorot 51a:8, 51b:7-9 — the money lost', lambda: the_gifts({'ask': 'redemption_money_lost'}, DATA), 'the father liable — shall be yours before you shall redeem (Mishnah Bekhorot 8:8; Bekhorot 51a)'),
    ('Sifrei 118:1; Bekhorot 5b:28 — the unclean firstborn (the Passover engine CALLED)', lambda: the_gifts({'ask': 'unclean_firstborn_scope'}, DATA), 'the ass alone (Sifrei 118:1; Bekhorot 5b) — redeem with a lamb, else break the neck (pesach CALLED)'),
    ('Mishnah Bekhorot 1:7 — redeem or break (the Passover engine CALLED)', lambda: the_gifts({'ask': 'ass_redeem_or_break'}, DATA), 'redeem with a lamb, else break the neck'),
    ('Mishnah Bekhorot 1:1; Bekhorot 4a:6 — the Levites\' donkey (the Bamidbar engine CALLED)', lambda: the_gifts({'ask': 'levite_donkey'}, DATA), 'exempt — a priest or a Levite (the son and the donkey)'),
    ('Mishnah Bekhorot 1:3 — the donkey\'s doubt', lambda: the_gifts({'ask': 'donkey_doubt'}, DATA), 'the burden of proof on the priest — a male and a female, the owner keeps the lamb; two males, one lamb (Mishnah Bekhorot 1:3)'),
    ('Mishnah Bekhorot 1:4-6; Bekhorot 12b:18 — the redeeming lamb', lambda: the_gifts({'ask': 'redeeming_lamb'}, DATA), 'any lamb — sheep or goat, any age, blemished; not a calf, a hybrid or a koy (Mishnah Bekhorot 1:4-5); the designated lamb died — R. Eliezer / the Rabbis (1:6)'),
    ('Num 18:17; Bekhorot 5b:10; Sifrei 118:1 — the clean firstborn', lambda: the_gifts({'ask': 'clean_firstborn'}, DATA), 'the firstborn of an ox, a sheep, a goat you shall not redeem — they are holy (18:17); an ox and its firstborn an ox (Bekhorot 5b); no hybrid (Sifrei 118:1)'),
    ('Bekhorot 7a:4, 12a:16; Bava Kamma 78a:6 — resembles', lambda: the_gifts({'ask': 'firstborn_resembles'}, DATA), 'the head and the majority of the body like the mother (Bekhorot 7a); resembling another species — no firstborn (Bekhorot 12a; Bava Kamma 78a)'),
    ('Pesachim 64b:18; Zevachim 37a:8-9, 56b:12; Keritot 4a:12 — their blood, their fat', lambda: the_gifts({'ask': 'firstborn_portions'}, DATA), "their blood, their fat — the tithe and the Passover placed like the firstborn (R. Yosei HaGelili; Zevachim 37a, 56b; Pesachim 64b); R. Yishmael from Deut 12:27; the portions burned (Keritot 4a)"),
    ('Mishnah Zevachim 5:8; Zevachim 56b:12 — one placement', lambda: the_gifts({'ask': 'firstborn_blood_placement'}, DATA), "one placement on the base — their blood, their fat: the tithe and the Passover too (R. Yosei HaGelili; Zevachim 56b; Mishnah Zevachim 5:8; Sifrei 118:1's one spilling)"),
    ('Bekhorot 27b:7, 28a:2; Zevachim 57a; Mishnah Zevachim 5:8 — two days and a night (the offerings engine CALLED)', lambda: the_gifts({'ask': 'firstborn_eating_window'}, DATA), 'two days and a night — as the wave-breast and the right thigh (18:18; Bekhorot 27b; Zevachim 57a; Mishnah Zevachim 5:8) — the peace offering\'s row CALLED'),
    ('Bava Kamma 13a:7; Bekhorot 31b:7, 32a:7; Temurah 5b:1, 8a:1; Zevachim 75b:8 — the sale', lambda: the_gifts({'ask': 'firstborn_sale'}, DATA), 'not redeemed, but sold — alive unblemished, blemished alive or slaughtered; the tithe neither (Bava Kamma 13a; Bekhorot 31b; Temurah 5b, 8a)'),
    ('Temurah 21a:9; Zevachim 37b:3 — the substitute', lambda: the_gifts({'ask': 'firstborn_substitute'}, DATA), 'they are holy — they, not their substitutes (Temurah 21a; Zevachim 37b)'),
    ('Zevachim 81a:8; Temurah 5b:9 — the blood mixed', lambda: the_gifts({'ask': 'firstborn_blood_mixed'}, DATA), "they are holy — the blood mixed with others' still sacrificed (Zevachim 81a; Temurah 5b)"),
    ('Makkot 19a:9; Temurah 21a:22; Zevachim 60b:9 — without the altar', lambda: the_gifts({'ask': 'firstborn_without_altar'}, DATA), 'the flesh as the blood — eaten only while the altar stands (Makkot 19a; Temurah 21a; Zevachim 60b)'),
    ('Zevachim 37b:2; Mishnah Bekhorot 4:1-5 — the blemished firstborn', lambda: the_gifts({'ask': 'blemished_firstborn'}, DATA), 'to the priest — it shall be yours repeated (Zevachim 37b); raised thirty or fifty days (Mishnah Bekhorot 4:1); kept the year (4:2); the expert (4:4-5)'),
    ('Mishnah Bekhorot 4:2 — the blemished kept', lambda: the_gifts({'ask': 'blemished_keeping'}, DATA), 'a blemish within the year — kept the twelve months; after the year — thirty days (Mishnah Bekhorot 4:2)'),
    ('Mishnah Bekhorot 4:3-5 — the expert', lambda: the_gifts({'ask': 'blemish_expert'}, DATA), "the court's expert exempt, a non-expert pays (Mishnah Bekhorot 4:4); a paid examiner disqualified unless like Ila (4:5); shown after slaughter — R. Yehuda / R. Meir (4:3)"),
    ('Bekhorot 32b:11, 33a:7 — the eaters', lambda: the_gifts({'ask': 'firstborn_eaters'}, DATA), 'Beit Shammai: priests only, not menstruating women; Beit Hillel: the blemished to any (Bekhorot 32b-33a)'),
    ('Mishnah Bekhorot 4:1; Bekhorot 26b:10 — raise before giving', lambda: the_gifts({'ask': 'raise_before_giving'}, DATA), "30 days a small animal, 50 a large (Mishnah Bekhorot 4:1; Bekhorot 26b — Exod 22:29 juxtaposed to 18:16's month)"),
    ('Mishnah Bekhorot 8:3-5 — twins', lambda: the_gifts({'ask': 'twins'}, DATA), 'twins — five sela after thirty days; one died — exempt; two wives — ten; the intermingled by certainty (Mishnah Bekhorot 8:3-5)'),
    ('Mishnah Bekhorot 8:1-2 — for redemption (the Passover engine CALLED)', lambda: the_gifts({'ask': 'firstborn_for_redemption'}, DATA), "opens a Jewish mother's womb (Mishnah Bekhorot 8:1); the caesarean — neither (8:2; pesach CALLED: not consecrated)"),
    ('Mishnah Bekhorot 4:7, 4:10 — the suspect', lambda: the_gifts({'ask': 'suspect_firstborn'}, DATA), 'no meat nor untanned hides from one suspect on firstborns (Mishnah Bekhorot 4:7); may neither judge nor testify on it (4:10)'),
    ('Mishnah Bekhorot 4:10 — the suspects\' principle', lambda: the_gifts({'ask': 'suspect_principle'}, DATA), 'suspect on the sabbatical year not on tithes, nor the reverse; suspect on either — on purities; neither judge nor witness on that matter (Mishnah Bekhorot 4:10)'),
    ('Num 18:19; 2 Chr 13:5; Sifrei 119:5; Menachot 19b-21b — the covenant of salt (computed)', lambda: the_gifts({'ask': 'covenant_of_salt'}, DATA), "a covenant of salt — Aaron's (18:19) and David's (2 Chr 13:5) alone; salting indispensable (Menachot 19b-20a); from communal supplies (Menachot 21b); Aaron's greater than David's (Sifrei 119:5)"),
    ('Menachot 21b:12 — the salt\'s source', lambda: the_gifts({'ask': 'salt_source'}, DATA), 'the salt from communal supplies — everlasting covenant / everlasting covenant with the showbread (Menachot 21b)'),
    ('Temurah 3a:4 — gentiles\' consecrations', lambda: the_gifts({'ask': 'gentile_consecrations'}, DATA), "of all the hallowed things of the children of Israel — not gentiles': no misuse (Temurah 3a)"),
    ('Mishnah Avot 4:13; Sifrei 119:4 — three crowns', lambda: the_gifts({'ask': 'three_crowns'}, DATA), 'three crowns — Torah, priesthood, kingdom; the good name above them (Avot 4:13; Sifrei 119:4)'),
    ('Chullin 136a:8 — first fruits of partners', lambda: the_gifts({'ask': 'bikkurim_partners'}, DATA), 'first fruits from land in partnership — liable; outside the land exempt (Chullin 136a)'),
    ('Menachot 84b:6 — first fruits of all', lambda: the_gifts({'ask': 'bikkurim_scope'}, DATA), 'the first fruits of all — roofs, ruins, flowerpots and ships; the two loaves precede (Menachot 84b)'),
    ('Menachot 84b:9-10 — the first fruits\' eaters', lambda: the_gifts({'ask': 'bikkurim_eaters'}, DATA), 'the household eats the first fruits — the verse read as two (Menachot 84b:10)'),
    # F5 — the tithe
    ('Num 18:20, 18:23-24; Onkelos — no inheritance', lambda: the_tithe({'ask': 'no_inheritance'}, DATA), 'in their land you shall not inherit — I am your portion (18:20; Onkelos: the gifts I have given you); the Levites no inheritance (18:23-24); Deut 10:9, 18:2, Josh 13:14, Ezek 44:28'),
    ('Sifrei 119:1; Mishnah Ma\'aser Sheni 5:14 — the exclusion table', lambda: the_tithe({'ask': 'exclusion_table'}, DATA), "priests (18:20), Levites (18:23), bondsmen and proselytes (26:55), the two of uncertain sex (26:54) — Sifrei 119:1; R. Meir: priests and Levites do not confess (Mishnah Ma'aser Sheni 5:14)"),
    ('Sifrei 119:5, 122:1 — the tithe to the Levites', lambda: the_tithe({'ask': 'tithe_to_levites'}, DATA), 'all the tithe in Israel — in exchange for their service (18:21): the Levite serves, the Levite takes; a Levite who refused one service has no portion (Sifrei 119:5, 122:1)'),
    ('Yevamot 86a-b — the recipient', lambda: the_tithe({'ask': 'tithe_recipient'}, DATA), "the Levite (18:21, 18:26 — R. Akiva); the priest too — Ezra's penalty / the priests called Levites (R. Eliezer; Yevamot 86a-b)"),
    ('Rosh Hashanah 12b:3; Sifrei 119:5 — the third year', lambda: the_tithe({'ask': 'third_year'}, DATA), 'the first tithe every year — juxtaposed to an inheritance (Rosh Hashanah 12b; Sifrei 119:5)'),
    ('Yevamot 86a:2 — to foreigners', lambda: the_tithe({'ask': 'tithe_to_foreigners'}, DATA), 'R. Meir: forbidden to non-Levites as terumah; the Rabbis permit (Yevamot 86a)'),
    ('Sifrei 119:5 — the Levite, he', lambda: the_tithe({'ask': 'levite_he'}, DATA), 'the Levite — he: perforce, in sabbatical and jubilee years, no priest in his stead (Sifrei 119:5)'),
    ('Menachot 54b:11; Neh 10:39 — the tithe of the tithe (computed)', lambda: the_tithe({'ask': 'tithe_of_the_tithe'}, DATA), '1/100 — a tenth of the tenth (18:26; Menachot 54b; Neh 10:39)'),
    ('Sifrei 120:1; Mishnah Terumot 1:5 — from it', lambda: the_tithe({'ask': 'from_it'}, DATA), 'from it — kind for its kind, rooted for rooted, new for new, not across the border (Sifrei 120:1; Mishnah Terumot 1:5); not the tithed tithe, not the exempt for the liable'),
    ('Sifrei 120:1; Pesachim 36a; Yevamot 73b — the mourner', lambda: the_tithe({'ask': 'mourner'}, DATA), "from it free for the mourner — the tithe and the paschal lamb (Sifrei 120:1; Pesachim 36a; Yevamot 73b); Mishnah Ma'aser Sheni 5:12"),
    ('Berakhot 47a-b; Beitzah 13b; Eruvin 31b; Pesachim 35b; Shabbat 127b — the Levite who preceded', lambda: the_tithe({'ask': 'levite_preceded'}, DATA), "on the stalks — the tithe's terumah only; after the pile — the great terumah too (Berakhot 47a-b; Beitzah 13b; Eruvin 31b; Pesachim 35b; Shabbat 127b)"),
    ('Beitzah 13b:3; Bekhorot 58b-59a; Sifrei 121:1; Mishnah Terumot 1:7 — by estimate', lambda: the_tithe({'ask': 'estimate'}, DATA), "by estimate and by thought — your terumah plural, two terumot (Abba Elazar ben Gomel: Beitzah 13b; Bekhorot 58b-59a; Sifrei 121:1); never by measure (Mishnah Terumot 1:7); the tithes too (18:24's terumah)"),
    ('Gittin 30b:13 — who separates the tithe\'s terumah', lambda: the_tithe({'ask': 'who_separates_tithe_terumah'}, DATA), 'the Levite, and the owner too (Gittin 30b)'),
    ('Sifrei 121:1; Mishnah Ma\'aserot 1:5-8; Bava Metzia 88b — the thresholds (computed on the floor-word)', lambda: the_tithe({'ask': 'thresholds'}, DATA), "the pile evened, the wine skimmed, the oil dripped (Sifrei 121:1; Mishnah Ma'aserot 1:6-7); grain at the granary, olives and grapes at the house (Bava Metzia 88b); the processed for the processed (Terumot 1:10)"),
    ('Mishnah Terumot 4:3-5 — the measure (the naso engine CALLED; 15:20\'s pointer PAID)', lambda: the_tithe({'ask': 'terumah_measure'}, DATA), '1/40, 1/50, 1/60 (Beit Shammai 1/30 — Mishnah Terumot 4:3); the floor: some must remain common (4:5 — naso\'s cell CALLED)'),
    ('Mishnah Terumot 2:4; Bekhorot 53b, 54b; Temurah 5a — kind for kind', lambda: the_tithe({'ask': 'kind_for_kind'}, DATA), 'not one kind for another — not terumah (Mishnah Terumot 2:4; Bekhorot 53b); the first part of them — each type its own (Bekhorot 54b; Temurah 5a)'),
    ('Sifrei 122:1; Mishnah Terumot 2:4, 2:6 — the best', lambda: the_tithe({'ask': 'the_best'}, DATA), 'from all its best (18:29-30, 18:32) — where a priest is, the best; where none, what lasts; the superior for the inferior, not the reverse (Mishnah Terumot 2:4, 2:6); a warning to take the choicest (Sifrei 122:1)'),
    ('Bava Batra 84b, 143a; Bava Metzia 56a; Kiddushin 46b; Temurah 5a; Yevamot 89b — the inferior for the superior', lambda: the_tithe({'ask': 'inferior_for_superior'}, DATA), 'valid terumah, a transgression that takes effect — you shall bear no sin (18:32; R. Ilai: Bava Batra 84b, 143a; Bava Metzia 56a; Kiddushin 46b; Temurah 5a); the impure for the pure likewise, penalized (Yevamot 89b; Terumot 2:2)'),
    ('Mishnah Terumot 2:2; Yevamot 89b:2 — the impure for the pure', lambda: the_tithe({'ask': 'impure_for_pure'}, DATA), 'not impure for pure — unwitting valid, intentional nothing (Mishnah Terumot 2:2); terumah by Torah law, the Sages penalized (Yevamot 89b)'),
    ('Sifrei 121:1; Mishnah Terumot 4:7; Challah 1:9 — the hundred and one (the holiness engine CALLED)', lambda: the_tithe({'ask': 'one_in_a_hundred'}, DATA), 'neutralized in a hundred and one (Sifrei 121:1; Mishnah Terumot 4:7; Challah 1:9) — holiness_b CALLED: 101'),
    ('Sifrei 122:1 — what remains', lambda: the_tithe({'ask': 'what_remains_common'}, DATA), "what remains is common, as the floor's grain after terumah (18:30; Sifrei 122:1)"),
    ('Sifrei 122:1; Yevamot 86b:2 — in every place', lambda: the_tithe({'ask': 'every_place'}, DATA), "in every place — even a cemetery (Sifrei 122:1; Yevamot 86b — R. Akiva: excludes the priest); Deut 12:13's ban the Torah twin"),
    ('Yevamot 86a:9; Sifrei 122:1 — the household deputes', lambda: the_tithe({'ask': 'household_deputes'}, DATA), 'you and your household — the Israelite wife of a Levite may depute the separation (18:31; Yevamot 86a; Sifrei 122:1)'),
    ('Num 18:31; Bekhorot 26b:18 — the wage', lambda: the_tithe({'ask': 'wage'}, DATA), 'it is your wage in exchange for your service (18:31); terumah or tithe not given as wages to the assisting priests, Levites or poor (Bekhorot 26b)'),
    ('Bekhorot 26b:18-19 — as wages', lambda: the_tithe({'ask': 'as_wages'}, DATA), 'forbidden, desecrated — that you shall not die (Bekhorot 26b)'),
    ('Bava Metzia 22a, 71b; Kiddushin 41b; Gittin 23b, 52a; Mishnah Terumot 4:4 — the agent', lambda: the_tithe({'ask': 'agent'}, DATA), 'you also — an agent, with the owner\'s knowledge; by the owner\'s mind, else 1/50; not partners, sharecroppers, stewards; a gentile no (Bava Metzia 22a, 71b; Kiddushin 41b; Gittin 23b, 52a; Mishnah Terumot 4:4)'),
    ('Bava Metzia 71b:10-12; Gittin 23b:4 — the gentile agent', lambda: the_tithe({'ask': 'agent_gentile'}, DATA), 'a gentile cannot separate terumah even as an agent — members of the covenant (Bava Metzia 71b; Gittin 23b)'),
    ('Mishnah Terumot 1:1-3, 1:6 — who separates', lambda: the_tithe({'ask': 'who_separates'}, DATA), 'not the deaf-mute, the imbecile, the minor, from what is not his, a gentile (Mishnah Terumot 1:1); the mute, the drunk, the naked, the blind — valid after the fact (1:6)'),
    ('Chullin 136a:2 — partners', lambda: the_tithe({'ask': 'partners'}, DATA), 'partners liable — all your tithes (Chullin 136a); with a gentile exempt'),
    ('Temurah 3a:9; Zevachim 45a:10; Bekhorot 11b:9 — gentiles\' tithe', lambda: the_tithe({'ask': 'gentile_tithe'}, DATA), "the tithe of the children of Israel — not gentiles' (Temurah 3a; Zevachim 45a); bought from a gentile in piles — exempt from the tithe's terumah (Bekhorot 11b)"),
    ('Bekhorot 11b:9 — bought from a gentile', lambda: the_tithe({'ask': 'bought_from_gentile'}, DATA), "bought from a gentile in smoothed piles — exempt from the tithe's terumah (Bekhorot 11b)"),
    ('Temurah 4b:3 — the wrong order', lambda: the_tithe({'ask': 'wrong_order'}, DATA), 'tithed in the wrong order — valid, rectified by the positive command, no lashes (Temurah 4b)'),
    ('Pesachim 23a:4 — an Israelite\'s benefit', lambda: the_tithe({'ask': 'israelite_benefit_from_terumah'}, DATA), 'your terumah — an Israelite may benefit (Pesachim 23a)'),
    ('Kiddushin 53a:12 — betrothal with the tithe\'s terumah', lambda: the_tithe({'ask': 'tithe_terumah_betrothal'}, DATA), "betrothal with the tithe's terumah valid — no to the LORD written of it (Kiddushin 53a)"),
    ('Mishnah Ma\'aserot 1:1-4 — liable produce', lambda: the_tithe({'ask': 'liable_produce'}, DATA), "food, guarded, grown from the land (Mishnah Ma'aserot 1:1); the ripening signs (1:2-4)"),
    ('Mishnah Ma\'aser Sheni 5:6, 5:9 — the removal', lambda: the_tithe({'ask': 'removal'}, DATA), "the removal on Passover eve of the fourth and seventh years — the first tithe to the Levite (Mishnah Ma'aser Sheni 5:6); the recipients by office: Joshua the Levite, Elazar ben Azariah the priest (5:9)"),
    ('Mishnah Ma\'aser Sheni 5:9 — the recipients', lambda: the_tithe({'ask': 'recipients'}, DATA), "the Levite, the priest (the tithe's terumah), the poor — Rabban Gamliel's ship (Mishnah Ma'aser Sheni 5:9)"),
    ('Mishnah Ma\'aser Sheni 5:10-11 — the confession', lambda: the_tithe({'ask': 'confession'}, DATA), "given to the Levite = the first tithe; also given = terumah and the tithe's terumah (Mishnah Ma'aser Sheni 5:10-11); Deut 26's run"),
    ('Sifrei 122:1; Lev 8:35, 10:6-9 — you shall not die', lambda: the_tithe({'ask': 'you_shall_not_die'}, DATA), "you shall not profane... and you shall not die (18:32) — the warning to Levites and Israelites both (Sifrei 122:1); the priests' words (Lev 8:35, 10:6-9)"),
    ('Sifrei 121:1 — so you too', lambda: the_tithe({'ask': 'so_you_too'}, DATA), 'so you too — the priests separate too (Sifrei 121:1); the three a-fortioris'),
    ('Mishnah Challah 1:9 — terumah\'s status (the priesthood engine CALLED)', lambda: the_tithe({'ask': 'terumah_status'}, DATA), "death and a fifth, forbidden to non-priests, the priest's property, nullified in a hundred and one, the hands, sunset, from the near and finished (Mishnah Challah 1:9)"),
    ('Num 15:20 / 18:27 — the pointer paid (computed on the floor-word)', lambda: the_tithe({'ask': 'pointer_paid'}, DATA), "15:20's as the terumah of the threshing floor is paid at 18:27's reckoned as the grain of the threshing floor (computed on the floor-word); the challah cell's as_terumah CALLS this cell"),
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
    print('\nKORACH: %d/%d cells; the scene %s; the narrative %s' % (ok, len(CASES), SCENE, NARRATIVE))
    sys.exit(0 if ok == len(CASES) else 1)

import os as _os
_ROOT = _os.path.normpath(_os.path.join(_os.path.dirname(_os.path.abspath(__file__)), '..', '..', '..'))   # THE PORTABLE REPO (2026-09-15): the repo root from this file's own place
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
_INK['_ROOT'] = _ROOT   # THE PORTABLE REPO (2026-09-15): the INK block reads the store through the root; the exec'd namespace must carry it
exec(_SRC.split('# ==== INK BEGIN')[1].split('# ==== INK END ====')[0].split('\n', 1)[1], _INK)
ink_numbers, verse_words, ink_ordinals = _INK['ink_numbers'], _INK['verse_words'], _INK['ink_ordinals']

db = sqlite3.connect((_ROOT + '/Data/tanakh.sqlite'))

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

#!/usr/bin/env python3
# NUM 19:1-21:35 — CHUKAT: THE RED HEIFER AND THE CORPSE'S LAW, MIRIAM'S DEATH AND THE WATERS OF MERIBAH, EDOM'S REFUSAL, AARON'S DEATH ON
# MOUNT HOR AND THE SUCCESSION, ARAD AND THE VOW, THE SERPENTS AND THE POLE, THE STATIONS AND THE WELL, SIHON AND OG (THE NUMBERS WALK
# sitting 6b, 2026-09-11; World/step9/NUMBERS_WALK.md "Sitting 6b"). The sixth Numbers portion compiled after its walk, on the owner's
# ruling READ THEN COMPILE: the parser taught THE DUAL "TWICE" (20:11's pa'amayim by the patach) and THE DEFINITE NUMERAL AFTER THE
# YEAR-CONSTRUCT AS AN ORDINAL YEAR (33:38's fortieth year — Aaron's death-date read whole) at this sitting (census_probes.py 149/149 after
# five rows failed first; the corpus diff's three unnamed seats read and typed); the leper's kit CALLED from the leper engine, the
# sin-bull's carcass and sevens from the sin-offering engine, me'ilah from the Lev 5 engine, the Day's finger from the Yom Kippur engine,
# the garments' succession from the vestments engine, the blemish and the office from the priesthood engine, the cherem from the temurah
# engine, the karet census from the sanctions engine, the grades from the clocks engine; THE TWO OWED EDGES of Naso (5:2) and
# Beha'alotcha (8:7) PAID by their live calls into this runner's corpse cell; the heifer's statute, Miriam's death, the strife and the
# strike, the sentence, Edom, Mount Hor, the succession, the mourning, Arad, the vow, the serpents, the well and the two kings on the
# tape with four markers in the fortieth year and two timers firing on one walk. Six motions of the deliverable rule, the wrap the sixth;
# every cell cites its source; every token probed (zero-report law); effects on every cell (the effects law). Reading ledgers: the three
# logic/oral_triage/num_{19,20,21}_*_2026-09-11.md; the exam's docket: num_19_21_chukat_exam_2026-09-11.md (480 rows — 322 LAW, 103
# DISPUTE, 38 CONTEXT, 17 DERIVATION; 60 credited).

# ---- THE HONEST-PAIRING GUARD ----------------------------------------------------------------------------
import os as _os, sys as _sys
_sys.path.insert(0, _os.path.dirname(_os.path.abspath(__file__)))
from compile_guards import check_honest_pairing as _chp
_P = _os.path.abspath(__file__)
GUARDED = _chp(_P, 'CASES', 2)
assert GUARDED == 159, ('the guard counted %d expectations, the tripwire holds 159' % GUARDED)   # the guard's own count, read off the first run (2026-09-11)
print('guard: %d expectations checked, every one a literal from the answer sheet [honest-pairing guard satisfied]' % GUARDED)
import sqlite3, sys, io, re, contextlib
from fractions import Fraction
import effects_layer as FX
import world_engine as WE
import cold_run_metzora as MZ                     # THE EDGE: chukat -> metzora CALL, reference (19:6's cedar, hyssop, scarlet — the leper's kit; 19:18's hyssop)
import cold_run_chatat as CH                     # THE EDGE: chukat -> chatat CALL, reference (19:9 'it is a sin offering'; 19:5's burn-list; 19:4's seven)
import cold_run_vayikra5 as V5                   # THE EDGE: chukat -> vayikra5 CALL, reference (19:9 — me'ilah on the heifer, Menachot 51b)
import cold_run_yoma as YM                       # THE EDGE: chukat -> yoma CALL, reference (19:4's finger and seven — Lev 16:14's seat)
import cold_run_vestments as VS                  # THE EDGE: chukat -> vestments CALL, reference (20:26-28's garments — Exod 29:29-30's spec)
import cold_run_priesthood as PR                 # THE EDGE: chukat -> priesthood CALL, reference (19:2's blemish; 20:28's office)
import cold_run_temurah as TM                    # THE EDGE: chukat -> temurah CALL, reference (21:2-3's cherem — Lev 27:28-29)
import cold_run_sanctions as SA                  # THE EDGE: chukat -> sanctions CALL, reference (19:13, 19:20's karet formula)
import cold_run_clocks as CL                     # THE EDGE: chukat -> clocks CALL, reference (19:7-8, 19:19, 19:21-22's grades)

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

_BYV = {}
for _b, _c, _v, _he in db.execute("SELECT v.book, v.chapter, v.verse, w.he FROM words w JOIN verses v ON w.verse_id=v.id ORDER BY v.id, w.idx"):
    _BYV.setdefault((_b, _c, _v), []).append(strip(_he))

def seats_of(tok, books=('Gen', 'Exod', 'Lev', 'Num', 'Deut')):
    return sorted(('%s %d:%d' % k for k, ws in _BYV.items() if k[0] in books and tok in ws), key=lambda s: (s.split()[0], int(s.split()[1].split(':')[0]), int(s.split(':')[1])))

# ---- zero-report probes: the span's load-bearing tokens ---------------------------------------------------
PROBES = [
    ('חקת', 19, 2, 'the statute'), ('פרה', 19, 2, 'a heifer'), ('אדמה', 19, 2, 'red'), ('תמימה', 19, 2, 'whole'), ('מום', 19, 2, 'a blemish'), ('על', 19, 2, 'a yoke'),
    ('אלעזר', 19, 3, 'Eleazar'), ('ושחט', 19, 3, 'and he shall slaughter'), ('לפניו', 19, 3, 'before him'), ('באצבעו', 19, 4, 'with his finger'), ('שבע', 19, 4, 'seven'), ('פעמים', 19, 4, 'times'),
    ('ושרף', 19, 5, 'and he shall burn'), ('ערה', 19, 5, 'its hide'), ('בשרה', 19, 5, 'its flesh'), ('דמה', 19, 5, 'its blood'), ('פרשה', 19, 5, 'its dung'),
    ('ארז', 19, 6, 'cedar'), ('ואזוב', 19, 6, 'and hyssop'), ('ושני', 19, 6, 'and scarlet (of)'), ('תולעת', 19, 6, 'worm — the crimson'), ('וכבס', 19, 7, 'and he shall wash'), ('ורחץ', 19, 7, 'and bathe'), ('הערב', 19, 7, 'the evening'),
    ('ואסף', 19, 9, 'and he shall gather'), ('למשמרת', 19, 9, 'for a keeping'), ('נדה', 19, 9, 'niddah'), ('חטאת', 19, 9, 'a sin offering'), ('הנגע', 19, 11, 'he who touches'), ('במת', 19, 11, 'the dead'), ('נפש', 19, 11, 'soul'), ('אדם', 19, 11, 'a human'), ('שבעת', 19, 11, 'seven'),
    ('השלישי', 19, 12, 'the third'), ('השביעי', 19, 12, 'the seventh'), ('יטהר', 19, 12, 'he shall be clean'), ('משכן', 19, 13, 'the tabernacle'), ('ונכרתה', 19, 13, 'and shall be cut off'), ('טמאתו', 19, 13, 'his uncleanness'),
    ('באהל', 19, 14, 'in a tent'), ('צמיד', 19, 15, 'a cord-bound'), ('פתיל', 19, 15, 'cover'), ('בחלל', 19, 16, 'one slain'), ('חרב', 19, 16, 'a sword'), ('בעצם', 19, 16, 'a bone'), ('בקבר', 19, 16, 'a grave'),
    ('מעפר', 19, 17, 'of the dust'), ('חיים', 19, 17, 'living'), ('אזוב', 19, 18, 'hyssop'), ('וטבל', 19, 18, 'and dip'), ('והזה', 19, 18, 'and sprinkle'), ('וחטאו', 19, 19, 'and purify him'), ('מקדש', 19, 20, 'the sanctuary'), ('הקהל', 19, 20, 'the assembly'), ('הנדה', 19, 21, 'the niddah'),
    ('צן', 20, 1, 'Zin'), ('הראשון', 20, 1, 'the first'), ('בקדש', 20, 1, 'at Kadesh'), ('ותמת', 20, 1, 'and she died'), ('מרים', 20, 1, 'Miriam'), ('ותקבר', 20, 1, 'and she was buried'), ('ויקהלו', 20, 2, 'and they assembled'), ('וירב', 20, 3, 'and they strove'), ('גוענו', 20, 3, 'we expired'),
    ('העליתנו', 20, 5, 'you brought us up'), ('כבוד', 20, 6, 'the glory'), ('המטה', 20, 8, 'the staff'), ('ודברתם', 20, 8, 'and speak'), ('הסלע', 20, 8, 'the rock'), ('מלפני', 20, 9, 'from before'), ('המרים', 20, 10, 'the rebels'),
    ('במטהו', 20, 11, 'with his staff'), ('פעמים', 20, 11, 'twice'), ('רבים', 20, 11, 'much'), ('האמנתם', 20, 12, 'you believed'), ('להקדישני', 20, 12, 'to sanctify Me'), ('מריבה', 20, 13, 'Meribah'), ('ויקדש', 20, 13, 'and He was sanctified'),
    ('מלאכים', 20, 14, 'messengers'), ('אדום', 20, 14, 'Edom'), ('אחיך', 20, 14, 'your brother'), ('ונצעק', 20, 16, 'and we cried'), ('מלאך', 20, 16, 'a messenger'), ('המלך', 20, 17, "the king's"), ('ימין', 20, 17, 'right'), ('ושמאול', 20, 17, 'and left'),
    ('בחרב', 20, 18, 'with the sword'), ('במסלה', 20, 19, 'by the highway'), ('חזקה', 20, 20, 'strong'), ('וימאן', 20, 21, 'and he refused'), ('ההר', 20, 22, 'Hor'), ('יאסף', 20, 24, 'shall be gathered'), ('מריתם', 20, 24, 'you rebelled'),
    ('והפשט', 20, 26, 'and strip'), ('והלבשתם', 20, 26, 'and clothe them'), ('וימת', 20, 28, 'and he died'), ('שלשים', 20, 29, 'thirty'), ('ויבכו', 20, 29, 'and they wept'),
    ('ערד', 21, 1, 'Arad'), ('האתרים', 21, 1, 'Atharim'), ('שבי', 21, 1, 'captive'), ('וידר', 21, 2, 'and he vowed'), ('נדר', 21, 2, 'a vow'), ('והחרמתי', 21, 2, 'and I will devote'), ('ויחרם', 21, 3, 'and he devoted'), ('חרמה', 21, 3, 'Hormah'),
    ('סוף', 21, 4, 'the Red (Sea)'), ('ותקצר', 21, 4, 'and was shortened'), ('הקלקל', 21, 5, 'the light'), ('השרפים', 21, 6, 'the fiery'), ('וינשכו', 21, 6, 'and they bit'), ('חטאנו', 21, 7, 'we have sinned'), ('ויתפלל', 21, 7, 'and he prayed'),
    ('שרף', 21, 8, 'a fiery one'), ('נס', 21, 8, 'a pole'), ('נחשת', 21, 9, 'copper'), ('והביט', 21, 9, 'and he looked'), ('וחי', 21, 9, 'and he lived'), ('זרד', 21, 12, 'Zered'), ('ארנון', 21, 13, 'Arnon'), ('מלחמת', 21, 14, 'the wars of'),
    ('בארה', 21, 16, 'to Beer'), ('ואתנה', 21, 16, 'and I will give'), ('ישיר', 21, 17, 'sang'), ('עלי', 21, 17, 'rise up'), ('במחקק', 21, 18, 'with the lawgiver'), ('במשענתם', 21, 18, 'with their staffs'), ('מתנה', 21, 18, 'Mattanah'), ('הפסגה', 21, 20, 'Pisgah'),
    ('סיחן', 21, 21, 'Sihon'), ('יהצה', 21, 23, 'Jahaz'), ('יבק', 21, 24, 'Jabbok'), ('עמון', 21, 24, 'Ammon'), ('חשבון', 21, 26, 'Heshbon'), ('המשלים', 21, 27, 'the parable-tellers'), ('כמוש', 21, 29, 'Chemosh'), ('ונירם', 21, 30, 'and we shot them'),
    ('יעזר', 21, 32, 'Jazer'), ('עוג', 21, 33, 'Og'), ('אדרעי', 21, 33, 'Edrei'), ('תירא', 21, 34, 'you shall (not) fear'), ('שריד', 21, 35, 'a survivor'),
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
def O(book, ch, vs): return ink_ordinals(verse_words(book, ch, vs))
TWICE = N('Num', 20, 11); assert TWICE == [2], ('the dual "twice" at 20:11 — rule (19)', TWICE)
TWICE_KIN = [N('Gen', 27, 36), N('Gen', 41, 32), N('Gen', 43, 10)]; assert TWICE_KIN == [[2], [2], [2]], TWICE_KIN
SEVEN = N('Num', 19, 4); assert SEVEN == [7], SEVEN
SEVENS = [N('Num', 19, 11), N('Num', 19, 14), N('Num', 19, 16)]; assert SEVENS == [[7], [7], [7]], SEVENS
SCHEDULE = O('Num', 19, 12); assert SCHEDULE == [3, 7, 3, 7], SCHEDULE          # the third and the seventh, twice at 19:12
SCHEDULE_19 = O('Num', 19, 19); assert SCHEDULE_19 == [3, 7, 7], SCHEDULE_19
FIRST_MONTH = O('Num', 20, 1); assert FIRST_MONTH == [1], FIRST_MONTH
DAYS30 = N('Num', 20, 29); assert DAYS30 == [30], DAYS30
AARON_DATE = (O('Num', 33, 38)[0], O('Num', 33, 38)[1], N('Num', 33, 38)[0]); assert AARON_DATE == (40, 5, 1), AARON_DATE   # rule (20): the year read whole
AARON_AGE = N('Num', 33, 39); assert AARON_AGE == [123], AARON_AGE
THIRTY_EIGHT = N('Deut', 2, 14); assert THIRTY_EIGHT == [38], THIRTY_EIGHT
MOSES_MOURNED = N('Deut', 34, 8); assert MOSES_MOURNED == [30], MOSES_MOURNED
OG_BED = N('Deut', 3, 11); assert OG_BED == [9, 4], OG_BED
WAR_RUN = (O('Num', 31, 19), N('Num', 31, 19)); assert WAR_RUN == ([3, 7], [7]), WAR_RUN   # 31:19's run of the schedule, read already
# THE BURN-LIST: 19:5's four (hide, flesh, blood, dung) against the sin-bull's three seats — the blood-word present here alone (the reading's crown, computed)
BURN_19 = [w for w in verse_text(19, 5).split() if w in ('ערה', 'בשרה', 'דמה', 'פרשה')]; assert BURN_19 == ['ערה', 'בשרה', 'דמה', 'פרשה'], BURN_19
BLOOD_AT_SIN_BULL = [any(w.startswith('דמ') or w.endswith('דמו') for w in verse_text(c, v, b).split()) for b, c, v in (('Exod', 29, 14), ('Lev', 4, 11), ('Lev', 16, 27))]
assert BLOOD_AT_SIN_BULL == [False, False, True], BLOOD_AT_SIN_BULL            # READ OFF THE FIRST RUN (2026-09-11): 16:27 names the blood ONCE — "whose blood was BROUGHT IN to atone in the holy place" — the inside's blood, not the burning's: the verse's own contrast, measured on the next line
_W1627 = verse_text(16, 27, 'Lev').split()
assert _W1627[_W1627.index('דמם') - 2] == 'הובא' and not any(w.startswith('דמ') for w in _W1627[_W1627.index('ושרפו'):]), _W1627   # הוּבָא אֶת דָּמָם ("was brought in... their blood"); the burn-list after וְשָׂרְפוּ ("and they shall burn") — hide, flesh, dung — carries no blood-word
# THE KIT'S ORDER: 19:6 cedar, hyssop, scarlet = Lev 14:49's (the house's) order; Lev 14:4 (the person's) cedar, scarlet, hyssop
def kit_order(b, c, v):                                                        # every written form of the three at the six seats (bare, articled, prefixed)
    KITW = {'ארז': 'cedar', 'הארז': 'cedar', 'ואזוב': 'hyssop', 'ואזב': 'hyssop', 'האזב': 'hyssop', 'ובאזב': 'hyssop', 'ושני': 'scarlet', 'שני': 'scarlet', 'ובשני': 'scarlet'}
    return [KITW[w] for w in verse_text(c, v, b).split() if w in KITW]
KIT_19, KIT_14_4, KIT_14_6, KIT_14_49, KIT_14_51, KIT_14_52 = [kit_order(*s) for s in (('Num', 19, 6), ('Lev', 14, 4), ('Lev', 14, 6), ('Lev', 14, 49), ('Lev', 14, 51), ('Lev', 14, 52))]
assert KIT_19 == ['cedar', 'hyssop', 'scarlet'] and KIT_14_51 == KIT_14_52 == KIT_19 and KIT_14_4 == KIT_14_6 == KIT_14_49 == ['cedar', 'scarlet', 'hyssop'], (KIT_19, KIT_14_4, KIT_14_6, KIT_14_49, KIT_14_51, KIT_14_52)
# MEASURED AT SIX SEATS (2026-09-11, read off the assert driver): the heifer's order is the HOUSE'S DIPPING order (Lev 14:51-52), not any taking's (14:4, 14:6, 14:49 all cedar, scarlet, hyssop) — the design's "= 14:49's" was false on the ink
# THE TWO MESSAGES: the Edom letter's request (20:17) and Sihon's (21:22) — the shared tokens computed
MSG_20, MSG_21 = set(verse_text(20, 17).split()), set(verse_text(21, 22).split())
SHARED_MSG = sorted(MSG_20 & MSG_21); assert len(SHARED_MSG) == 13, SHARED_MSG
# THE FOUR SOURCES reordered between 19:16 and 19:18 (computed on the four stems)
def sources(v):
    return [w for w in verse_text(19, v).split() if w in ('בחלל', 'במת', 'בעצם', 'בקבר', 'בעצם', 'בחלל', 'במת', 'בקבר')]
SRC_16, SRC_18 = sources(16), sources(18); assert SRC_16 == ['בחלל', 'במת', 'בעצם', 'בקבר'] and SRC_18 == ['בעצם', 'בחלל', 'במת', 'בקבר'], (SRC_16, SRC_18)
MERIBAH_HOMOGRAPH = ['Gen 13:8']                                                # the common noun "strife" — "let there be no STRIFE between me and you" (Abram to Lot): named, never counted (the census's one homograph, read off the first measurement)
MERIBAH_SEATS = [s for s in seats_of('מריבה') + seats_of('ומריבה') + seats_of('מריבת') if s not in MERIBAH_HOMOGRAPH]; assert 'Num 20:13' in MERIBAH_SEATS and 'Exod 17:7' in MERIBAH_SEATS and len(MERIBAH_SEATS) == 6, MERIBAH_SEATS
FRAMES = [(c, v) for (b, c, v), ws in _BYV.items() if b == 'Num' and c in (19, 20, 21) and len(ws) > 2 and ws[0] in ('וידבר', 'ויאמר') and ws[1] == 'יהוה']
assert sorted(FRAMES) == [(19, 1), (20, 7), (20, 12), (20, 23), (21, 8), (21, 34)], sorted(FRAMES)
STATUTE_SEATS = sorted(k for k, ws in _BYV.items() if k[0] == 'Num' and any(ws[i] == 'זאת' and ws[i + 1] == 'חקת' and ws[i + 2] == 'התורה' for i in range(len(ws) - 2)))
assert STATUTE_SEATS == [('Num', 19, 2), ('Num', 31, 21)], STATUTE_SEATS       # "this is the statute of the Torah" — two seats

# ---- THE CALLEES, measured live at import (the edges) ----
MZ_KIT = MZ.birds('kit')['v']; assert 'cedar' in str(MZ_KIT) and 'hyssop' in str(MZ_KIT), MZ_KIT
MZ_HYSSOP = MZ.birds('hyssop')['v']
CH_CARCASS = CH.carcass('anointed')['v']; CH_SEVEN = CH.sprinklings('anointed')['v']; CH_BLOOD = CH.blood('anointed')['v']
assert CH_SEVEN == 7 and 'outside' in str(CH_CARCASS), (CH_SEVEN, CH_CARCASS)
V5_MEILAH = V5.sacrilege({'kind': 'meilah', 'unwitting': True, 'benefit': True, 'damage': True, 'value': 4}, V5.DATA)[0]
YM_ORDER = YM.service_order(); YM_1614 = [x for x in YM_ORDER if x[0] == '16:14'][0][1]; assert 'seven' in YM_1614, YM_1614
VS_SUBSTITUTE = VS.investiture('substitute')['v']; assert VS_SUBSTITUTE == 'another_priest_prepared', VS_SUBSTITUTE
PR_BEAST = PR.blemish('beast_unfits_in_man')['v']; PR_PASSED = PR.blemish('passed_blemish')['v']; PR_HOUR = PR.family('one_hour')['v']; PR_HP_DEAD = PR.family('high_priest_dead')['v']
assert PR_PASSED == 'fit' and PR_HOUR == 'office_attaches_at_the_pouring', (PR_PASSED, PR_HOUR)
TM_DEVOTE = TM.devote('status')['v']; TM_DEVOTE_DEST = TM.devote('unspecified_destination')['v']; TM_PERSON = TM.devote('person')['v']
SA_KARET = SA.c_karet; SA_KARET_MODE = SA.read_sanction(3)['karet']; assert len(SA_KARET) == 10 and SA_KARET_MODE is True, (SA_KARET, SA_KARET_MODE)   # Lev 17-20's ten karet seats (the sanctions engine's census) and Lev 20:3's karet read live by its reader — THE CALL (an attribute is no edge to the gate: 4b's lesson, read off the first gate run)
CL_GRADE = CL.touch('zav', 'bed', 'touch')['v']; assert CL_GRADE == 'washes_garments_bathes_until_evening', CL_GRADE
_W0 = WE.World(era='the calendar', epoch='exodus'); EX0 = _W0.clock.eras['exodus']
D_ZIN, D_HOR, D_AARON, D_DEPART = (_W0.clock.day_in('exodus', 40, 1, 1), _W0.clock.day_in('exodus', 40, 4, 1), _W0.clock.day_in('exodus', *AARON_DATE), None)
D_DEPART = D_AARON + DAYS30[0]; assert EX0.date(D_DEPART) == (40, 6, 1) and EX0.date(D_AARON) == (40, 5, 1), (EX0.date(D_DEPART), EX0.date(D_AARON))
D_DUE38 = _W0.clock.calendar.add(_W0.clock.day_in('exodus', 2, 5, 9), THIRTY_EIGHT[0], 'year'); assert EX0.date(D_DUE38) == (40, 5, 9), EX0.date(D_DUE38)

# =====================================================================
# Motion 2 — THE DATA: the parameter rows (the tradition's own vocabulary; the running setting first)
# =====================================================================
DATA = {
    'heifer_age': {'value': 'three_or_four_the_Sages', 'settings': {'three_or_four_the_Sages': 'the heifer may be two, the red cow three or four (Mishnah Parah 1:1)', 'two_R._Eliezer': 'R. Eliezer: the heifer one year, the cow two (Parah 1:1)', 'five_R._Meir': 'R. Meir: even five, though old — the black hairs feared (Parah 1:1)'}, 'source': 'Num 19:2 — NO AGE IN THE INK; Mishnah Parah 1:1'},
    'heifer_hairs': {'value': 'two_in_one_follicle', 'settings': {'two_in_one_follicle': 'two black or white hairs in one follicle invalidate (Mishnah Parah 2:5)', 'one_kos_R._Yehuda': 'R. Yehuda: within one kos, or two adjacent (Parah 2:5)', 'plucked_R._Akiva': 'R. Akiva: four or five dispersed may be plucked; R. Eliezer even fifty; R. Yehoshua b. Beteira: one on the head and one on the tail invalidate (Parah 2:5)'}, 'source': 'Num 19:2 "red" — Mishnah Parah 2:5'},
    'heifer_yoke': {'value': 'any_burden_placed', 'settings': {'any_burden_placed': "a bundle of sacks placed on it disqualifies — a yoke placed, not at work; other labor at work (Rav — Sotah 46a:11, 46a:16; Avodah Zarah 23a:6); for its own sake valid, for another's invalid (Mishnah Parah 2:3-4)", 'bit_no_burden': 'tied by its reins it stays fit (Shabbat 52a:7)', 'threshing_by_intent': 'threshing in a pen while walking valid unless brought in to thresh (Pesachim 26a:16)'}, 'source': 'Num 19:2 "upon which never came a yoke"; Deut 21:3'},
    'heifer_blemish': {'value': 'consecrated_animals_list_by_call', 'settings': {'consecrated_animals_list_by_call': "all blemishes that invalidate consecrated animals invalidate the heifer (Mishnah Parah 2:3) — the priesthood engine's beast rows by CALL: %s; a blemish that passed: %s" % (PR_BEAST, PR_PASSED), 'bah_excludes_the_eglah': "'wherein [bah] has no blemish' — the heifer alone, not the eglah arufah (Sotah 46a:2)", 'horns_hoofs': 'black horns or hoofs chopped off; the eyeball, teeth and tongue do not invalidate; the dwarf valid (Parah 2:2)'}, 'source': 'Num 19:2 "whole, in which there is no blemish"'},
    'heifer_pregnant': {'value': 'invalid_the_Sages', 'settings': {'invalid_the_Sages': 'a pregnant heifer invalid (Mishnah Parah 2:1)', 'valid_R._Eliezer': 'R. Eliezer: valid (Parah 2:1)'}, 'source': 'Mishnah Parah 2:1'},
    'heifer_from_gentile': {'value': 'valid_the_Sages', 'settings': {'valid_the_Sages': 'bought from gentiles valid (Mishnah Parah 2:1); the phrase "that they take" shared with Exod 25:2 (Avodah Zarah 23b-24a)', 'invalid_R._Eliezer': "R. Eliezer: Israel takes, gentiles do not (Sheila's baraita — Avodah Zarah 23a:9)"}, 'source': 'Num 19:2 "speak to the children of Israel that they take"'},
    'who_burns': {'value': 'first_by_eleazar_then_common_priest', 'settings': {'first_by_eleazar_then_common_priest': "'give IT to Eleazar' — the first by the deputy alone; in later generations even a common priest (some say — Yoma 42b:10; Rav's restrictive-after-restrictive at 43a:3)", 'high_priest_after': "some say: the high priest, from 'statute' / 'statute' with the Day (Yoma 42b:10-11); Mishnah Parah 4:1 'not by the high priest invalid' — R. Yehuda valid"}, 'source': 'Num 19:3 "you shall give it to Eleazar the priest"'},
    'who_slaughters': {'value': 'a_stranger_valid_Shmuel', 'settings': {'a_stranger_valid_Shmuel': "'he shall slaughter it BEFORE HIM' — a non-priest slaughters and Eleazar watches (Shmuel — Yoma 42a:10)", 'a_priest_Rav': "Rav: 'Eleazar the priest' and 'statute' — a non-priest's slaughter invalid (Yoma 42a:6; Menachot 6b:11; Zevachim 14b:6, 68b:5)"}, 'source': 'Num 19:3 "and he shall slaughter it before him"'},
    'work_invalidates': {'value': 'from_the_slaughter_to_the_ashes', 'settings': {'from_the_slaughter_to_the_ashes': 'all occupied from the beginning to the end invalidate it by other work, until it becomes ashes; the water until the ashes are in it (Mishnah Parah 4:4; 7:1-12 the filling and mixing; 8:1 the two guards)'}, 'source': 'Num 19:3-9; Mishnah Parah 4:4, 7:1-12'},
    'tvul_yom_fit': {'value': 'fit_the_burner_defiled_on_purpose', 'settings': {'fit_the_burner_defiled_on_purpose': "'the PURE one shall sprinkle' — pure only in relation to the impure: the tevul yom fit (Yoma 43b:3; Zevachim 17b:3; Yevamot 73a:1); the burning priest deliberately defiled and immersed against the Sadducees (Mishnah Parah 3:7)", 'sadducees_sunset': "the Sadducees: 'only those on whom the sun has set' (Parah 3:7 — the rejected arm, recorded)"}, 'source': 'Num 19:19 "the clean one"; 19:9 "a clean man"'},
    'sprinkle_toward': {'value': 'toward_the_entrance_each_dip_its_own', 'settings': {'toward_the_entrance_each_dip_its_own': "seven times toward the front of the tent of meeting — seven indispensable, each its own dip; not toward the entrance invalid; the seventh from the sixth then a seventh invalid, an eighth from the seventh valid (Mishnah Parah 3:9, 4:2; Menachot 27a-b; Zevachim 40a)", 'r_yehuda_precisely': "R. Yehuda: 'toward [el] the front' precisely (Menachot 27b:15)"}, 'source': 'Num 19:4 "toward the front of the tent of meeting seven times"'},
    'bundle': {'value': 'the_three_wrapped_and_cast', 'settings': {'the_three_wrapped_and_cast': "the cedar, hyssop and scarlet asked thrice each, wrapped with the strip's remainder and cast into the fire (Mishnah Parah 3:10-11); burned in the air before the mass valid, singed before it replaced (Yoma 41b:18); the strip's weight disputed (41b:16)"}, 'source': 'Num 19:6 "into the midst of the burning of the heifer"'},
    'ashes_thirds': {'value': ['the rampart', 'the Mount of Olives', 'the priestly watches'], 'settings': {'three_parts': 'divided into three parts (Mishnah Parah 3:11)'}, 'source': 'Num 19:9 "lay them outside the camp in a clean place"'},
    'nine_heifers': {'value': 'seven_after_Ezra_the_Sages', 'settings': {'seven_after_Ezra_the_Sages': "Moses the first, Ezra the second, seven from Ezra's time: Shimon the Just and Yochanan the high priest two each, Elihoenai, Hanamel the Egyptian, Ishmael b. Piabi one each (Mishnah Parah 3:5)", 'five_after_Ezra_R._Meir': 'R. Meir: five from the time of Ezra (Parah 3:5)'}, 'source': "Num 19:2 — the ink never narrates the first heifer's burning: the tape's debit OPEN; the shelf's run"},
    'meilah_on_the_heifer': {'value': 'applies_by_torah_law', 'settings': {'applies_by_torah_law': "'it is a sin offering' — treated as a sin offering, me'ilah applies (Menachot 51b:22; Mishnah Parah 4:4 'always subject to trespass'); the court's ordinance on the ashes (Shekalim 7:7); the Lev 5 engine's cell by CALL: %s" % V5_MEILAH}, 'source': 'Num 19:9 "it is a sin offering"'},
    'removes': {'value': {'toucher': 'seven days', 'toucher_of_toucher': 'until evening', 'vessels': 'three in a series', 'persons': 'two, four with a person in the middle'}, 'settings': {'oholot_1': 'two, three, four defiled through a corpse; the tent does not count (Mishnah Oholot 1:1-4); the corpse a father of fathers, the top of the ladder (Kelim 1:4)'}, 'source': 'Num 19:11 seven days; 19:22 until evening'},
    'tent_measure': {'value': {'block': 'a handbreadth square (an olive), four handbreadths (a corpse)', 'go_out': 'a handbreadth', 'beam': 'three round, four square for a handbreadth', 'pillar': 'twenty-four'}, 'settings': {'oholot_3': 'the handbreadth (Mishnah Oholot 3:6-7; 12:6-7); R. Yehuda: a tent not made by a person is no tent (3:7; Sukkah 21a)'}, 'source': 'Num 19:14 "in a tent"'},
    'tent_material': {'value': 'any_shelter_the_Rabbis', 'settings': {'any_shelter_the_Rabbis': "'tent, tent' repeated amplifies: any shelter (Sukkah 21a:1; Shabbat 28a:1)", 'linen_by_analogy': "'tent' / 'tent' with Exod 40:19: linen as the Tabernacle's (Shabbat 28a)", 'man_made_R._Yehuda': 'R. Yehuda: a tent made by a person (Sukkah 21a; Oholot 3:7)'}, 'source': 'Num 19:14; Exod 40:19'},
    'tent_gentile': {'value': 'no_tent_impurity', 'settings': {'no_tent_impurity': "'when a MAN dies in a tent' — gentiles' graves do not defile by tent (R. Shimon b. Yochai — Bava Metzia 114b:2; Yevamot 61a:1); touch and carrying remain (Yevamot 61a:5 — the Midian war)"}, 'source': 'Num 19:14 "a man"; Ezek 34:31'},
    'bone_measure': {'value': {'bone': 'a barley-grain', 'blood': 'a quarter-log', 'flesh': 'an olive', 'spine_or_skull': 'whole or deficient by Beit Shammai / Beit Hillel', 'bones': 'a quarter-kav of the majority; the majority by number 125'}, 'settings': {'oholot_2': 'the overshadowing sources and the contact-only ones (Mishnah Oholot 2:1-7; Nazir 53b-54a; Chullin 72a:8)', 'two_corpses_R._Akiva': 'from two corpses — R. Akiva unclean, the Sages clean (Oholot 2:6)'}, 'source': 'Num 19:16, 19:18 "a bone"; 19:13 "of the life"'},
    'field_phrase': {'value': 'grave_stones_R._Akiva', 'settings': {'grave_stones_R._Akiva': "'in the open field' includes the grave's cover and walls (R. Akiva — Chullin 72a:6; Oholot 2:4)", 'excludes_fetus_R._Yishmael': "R. Yishmael: excludes a dead fetus in the womb; R. Akiva has it from 'of the life' (Chullin 72a:6-7)"}, 'source': 'Num 19:16 "on the open field"'},
    'sword_like_slain': {'value': 'a_metal_vessel_takes_the_corpse_grade', 'settings': {'a_metal_vessel_takes_the_corpse_grade': "'one slain by a SWORD' — the sword like the slain: a metal vessel touching a corpse takes its grade (Pesachim 14b:1, 19b:11, 79a:15; Shabbat 101b:8 — iron, not a string)"}, 'source': 'Num 19:16 "one slain by the sword"'},
    'vessel_census': {'value': ['dung', 'stone', 'clay', 'earthenware', 'sodium carbonate', "a fish's bones or skin", "a sea animal's", 'always-clean wooden vessels'], 'settings': {'kelim_10_1': 'the vessels that protect with a tight cover; an earthenware vessel protects only foods, liquids and earthenware (Mishnah Kelim 10:1; Chullin 25a; Sifrei 126 by three verses)', 'beit_shammai_foods_only': "an earthenware vessel protects only food, drink and earthenware (Beit Shammai; Beit Hillel retracted — Eduyot 1:14; Oholot 5:3)"}, 'source': 'Num 19:15 "every open vessel"; Lev 11:33'},
    'tzamid_patil': {'value': ['lime', 'gypsum', 'pitch', 'wax', 'mud', 'excrement', 'crude clay', "potter's clay", 'any plastering'], 'settings': {'kelim_10_2': 'not tin or lead (a cover, not tight); not swollen fig-cakes or juice-dough, but if done it protects (Mishnah Kelim 10:2); the hatat water itself unprotected (Parah 11:1); Onkelos inserts OF EARTHENWARE'}, 'source': 'Num 19:15 "a cord-bound cover"'},
    'living_water': {'value': 'spring_water_drawn_into_a_vessel', 'settings': {'spring_water_drawn_into_a_vessel': "the spring's water flows straight into the vessel (Pesachim 34b:13); diverted into a vat unfit (Parah 6:5); the seas, the marsh rivers, the mixed rivers unfit (Parah 8:8-11; Sanhedrin 5b:7); the sixth degree of waters (Mikvaot 1:8); the leper engine's vessel: %s" % MZ_HYSSOP}, 'source': 'Num 19:17 "living water into a vessel"; Lev 14:5'},
    'mixing_order': {'value': 'ashes_upon_the_water', 'settings': {'ashes_upon_the_water': "the Torah called ashes DUST for the verbal analogy with the sotah's dust: as there the dust on the water, so here the ashes ON the water (R. Shimon — Sotah 16b:15; Temurah 12b:7; Chullin 88b:8); by hand, intentionally (Parah 6:1; Sukkah 37b:1); naso's row dust_order (water then dust) the same order at the other rite"}, 'source': 'Num 19:17 "of the dust of the burning"; Num 5:17'},
    'third_day_fixed': {'value': 'third_then_seventh_a_four_day_interval', 'settings': {'third_then_seventh_a_four_day_interval': 'the third excludes the second, the seventh the sixth; the third and the EIGHTH invalid too — a fixed interval (Kiddushin 62a:6); both needed even for terumah (62a:7); Sifrei 125: the third fixed, the seventh counted from it'}, 'source': 'Num 19:12, 19:19'},
    'punishment_split': {'value': 'uncleanness_for_the_omission_karet_for_the_entry', 'settings': {'uncleanness_for_the_omission_karet_for_the_entry': "'he shall not be clean' for the omission; 'cut off' for the entry — 19:13 the tabernacle, 19:20 the sanctuary (Sifrei 125-126); the punishment here, the prohibition at 5:3 (Makkot 14b:6); the sanctions engine's karet census: %d seats in Lev 17-20, these two in Numbers" % len(SA_KARET), 'inside_R._Elazar': 'the second verse for one made impure INSIDE the courtyard who lingers (Shevuot 16b:1; Mishnah Shevuot 2:3)'}, 'source': 'Num 19:13, 19:20'},
    'minor_and_karet': {'value': 'impure_but_no_karet', 'settings': {'impure_but_no_karet': "'the persons that were there' — a minor becomes impure, a day old (Arakhin 3a:6; Niddah 44a:7); 'the man' excludes him from the karet (Arakhin 3a:7)"}, 'source': 'Num 19:18, 19:20'},
    'high_priest_exempt': {'value': 'exempt_R._Shimon', 'settings': {'exempt_R._Shimon': "'from the midst of the CONGREGATION' — the anointed high priest not liable for defiling the Temple (Horayot 9b:3; Parah 12:4 'a high priest is never liable for entering')"}, 'source': 'Num 19:20'},
    'gentile_no_tumah': {'value': 'excluded_from_the_assembly', 'settings': {'excluded_from_the_assembly': "'cut off from the midst of the assembly' — impurity applies to a member of the assembly; who cannot be purified cannot become impure (Nazir 61b:1-3)"}, 'source': 'Num 19:20'},
    'sprinkler_measure': {'value': 'enough_to_dip_the_buds_tips', 'settings': {'enough_to_dip_the_buds_tips': "how much water — enough to dip the tips of the buds and sprinkle (Mishnah Parah 12:5; Sifrei 129's elimination); under the measure a father by contact, above it by carrying (Kelim 1:1-2)", 'brass_hyssop_R._Yehuda': 'R. Yehuda: as though on a hyssop of brass (Parah 12:5)'}, 'source': 'Num 19:18 "dip it in the water"'},
    'sprinkler_or_carrier': {'value': 'the_sprinkler_clean_the_carrier_unclean', 'settings': {'the_sprinkler_clean_the_carrier_unclean': "'he who sprinkles' read as 'he who CARRIES' a sprinkling's worth: the sprinkler clean, the carrier's grade heavier than the toucher's (Yoma 14a:9; Niddah 9a:15; Parah 12:5; Sifrei 130)"}, 'source': 'Num 19:21'},
    'sprinkler_who': {'value': 'a_man_not_a_woman_the_Rabbis', 'settings': {'a_man_not_a_woman_the_Rabbis': "'a MAN who is pure' — a man, not a woman; 'pure' includes a minor (the Rabbis — Yoma 43a:13; 42b:3; Parah 12:10: not a tumtum, hermaphrodite, woman or witless child; a woman may assist)", 'an_adult_R._Yehuda': "R. Yehuda: an adult, not a minor; 'pure' includes a woman (Yoma 43a:13; Parah 5:4)"}, 'source': 'Num 19:18-19'},
    'who_sanctifies': {'value': 'as_the_gatherer', 'settings': {'as_the_gatherer': "'THEY shall take... HE shall put' — the disqualified for gathering disqualified for sanctifying; a woman gathers, so she sanctifies (Yevamot 72b:16; Yoma 43a:9); two take and one puts, valid (43a:12); the gatherer: a non-priest, a woman; not the deaf-mute, imbecile or minor (43a:7)"}, 'source': 'Num 19:9, 19:17'},
    'sprinkling_day': {'value': 'by_day_from_sunrise', 'settings': {'by_day_from_sunrise': "'on the seventh DAY' — by day, not at night; immersion likened (Megillah 20a:10); dipped by day and sprinkled at night invalid; from dawn valid (Parah 12:11)"}, 'source': 'Num 19:19'},
    'a_clean_man': {'value': 'the_woman_excluded_from_gathering_a_child_fit', 'settings': {'the_woman_excluded_from_gathering_a_child_fit': "Sifrei 124, 129's exclusions on 'a clean man'; the answer sheet widens the gathering to a woman (Yoma 43a:7) and narrows the sprinkling to a man (Parah 12:10)"}, 'source': 'Num 19:9, 19:18'},
    'madaf': {'value': 'the_unclean_has_madaf_the_clean_not_the_Sages', 'settings': {'the_unclean_has_madaf_the_clean_not_the_Sages': "the heifer-purity's stringency: what is susceptible to midras has madaf for the hatat, clean or unclean; what is susceptible to corpse uncleanness — the Sages: the unclean has it, the clean not (Mishnah Parah 10:1)", 'no_madaf_R._Eliezer': 'R. Eliezer: no madaf; R. Yehoshua: madaf (Parah 10:1)'}, 'source': 'Mishnah Parah 10:1-6'},
    'miriam_death_day': {'value': 'tenth_of_nisan', 'settings': {'tenth_of_nisan': "Miriam died on the tenth of Nisan (Seder Olam Rabbah 10:2 — R. Yosei b. R. Yehuda's tradition; Megillat Taanit)", 'first_of_nisan_the_arrival': "the arrival at Zin 'in the first month' = the new moon of Nisan of the fortieth year, the well removed (Seder Olam Rabbah 9:2) — the tape's marker at 20:1: the death's line on the arrival's day, the nine days the checkpoint CM5's DIVERGE"}, 'source': 'Num 20:1 "in the first month" — no day, no year in the ink; Taanit 9a:9 the well gone at her death'},
    'well_by_merit': {'value': 'miriams_gone_at_her_death_returned', 'settings': {'miriams_gone_at_her_death_returned': "three sustainers, three gifts — the well by Miriam's merit disappeared at her death ('and there was no water for the congregation') and returned by Moses' and Aaron's (R. Yosei b. R. Yehuda — Taanit 9a:9; Seder Olam 10:2; 9:2 'the well to which they returned' at Beer)"}, 'source': 'Num 20:1-2; 21:16'},
    'death_by_the_kiss': {'value': 'miriam_too_by_there_there', 'settings': {'miriam_too_by_there_there': "'and Miriam died THERE' / 'and Moses died THERE' — Miriam too by the kiss; 'by the mouth of the LORD' unwritten for a woman (R. Elazar — Bava Batra 17a:4); Moed Katan 28a: the righteous' death atones — the heifer's juxtaposition"}, 'source': 'Num 20:1; Deut 34:5'},
    'meribah_sin': {'value': 'struck_not_spoke', 'settings': {'struck_not_spoke': "the spec's verb SPEAK (20:8), the run's STRUCK TWICE (20:11 — the parser's [2]): 'because you did not believe in Me, to sanctify Me' (20:12); had you believed and spoken, your time had not come (Shabbat 55b:2; Yoma 87a:3)", 'the_words_rebels': "'hear now, you rebels' — the speech (Ps 106:33 'he spoke rashly with his lips'; one consonantal skin with Miriam and Marah — the reading's crown)", 'disgrace_written': "Moses asked that his disgrace be written (Yoma 86b:15)"}, 'source': 'Num 20:8-12; Ps 106:32-33; Deut 32:51'},
    'edom_passage': {'value': 'refused_and_turned_away', 'settings': {'refused_and_turned_away': "'you shall not pass through me' twice, 'and Israel turned away from him' (Num 20:18-21)", 'bought_and_passed_deut_2': "Deut 2:4-8, 2:28-29 'as the sons of Esau did for me': food and water bought, the passage by their border — the other arm (a DISPUTE row)"}, 'source': 'Num 20:14-21; Deut 2:4-8, 2:28-29'},
    'moserah': {'value': 'the_retreat_of_seven_stations', 'settings': {'the_retreat_of_seven_stations': "Deut 10:6 'there Aaron died' at Moserah — after the king of Arad came they retreated seven stations to Moserah, the mourning renewed there (Seder Olam Rabbah 9:2); Aaron died at Mount Hor (Num 20:28, 33:38)"}, 'source': 'Num 20:22-28; 33:30-38; Deut 10:6'},
    'succession_by': {'value': 'the_garments_the_ink', 'settings': {'the_garments_the_ink': "'strip Aaron of his garments and put them on Eleazar' (20:26, 20:28) — Exod 29:29-30's spec RUN: 'the holy garments of Aaron shall be his sons' after him... seven days shall the priest in his stead wear them'; the vestments engine's cell: %s; the priesthood engine: %s" % (VS_SUBSTITUTE, PR_HOUR), 'the_anointing_29_29': "'to be anointed in them' (Exod 29:29) — the many-garmented against the anointed (Horayot 12a; Yoma 12b; the priesthood engine's crown-of-the-oil row)"}, 'source': 'Num 20:26, 20:28; Exod 29:29-30'},
    'aaron_mourned_by_all': {'value': 'the_men_and_the_women', 'settings': {'the_men_and_the_women': "'all the house of Israel' — the men and the women (Aaron the peacemaker; Lev 10:6's mourners of his sons the same phrase); Moses' thirty at Deut 34:8 [%d]" % MOSES_MOURNED[0]}, 'source': 'Num 20:29'},
    'arad_heard': {'value': 'that_aaron_died_and_the_clouds_departed', 'settings': {'that_aaron_died_and_the_clouds_departed': "'the Canaanite king of Arad heard' — what? that Aaron had died and the clouds of glory withdrew; 'and all the congregation SAW that Aaron was dead' (Rosh Hashanah 3a:1; Taanit 9a:10; Seder Olam 9:2)", 'arad_is_amalek': "'Canaanite' — Amalek came in disguise (Rosh Hashanah 3a — the row)"}, 'source': 'Num 21:1; 20:29; 33:40'},
    'captive_count': {'value': 'one_maidservant', 'settings': {'one_maidservant': "'took some of them captive' — the shelf's one maidservant (the reading's row); Gittin 38a:4: a gentile acquires a Jew by conquest"}, 'source': 'Num 21:1'},
    'cherem_law': {'value': 'temurah_by_call', 'settings': {'temurah_by_call': "the devotion's law read live from the temurah engine — status: %s; unspecified destination: %s; a person devoted: %s (Lev 27:28-29)" % (TM_DEVOTE, TM_DEVOTE_DEST, TM_PERSON), 'vow_form': "'if You will indeed give this people into my hand' — the conditional vow of Jacob (Gen 28:20) and Jephthah (Judg 11:30); one who wishes to succeed sanctifies a portion (Eruvin 64b:3)"}, 'source': 'Num 21:2-3'},
    'manna_absorbed': {'value': 'light_absorbed_in_the_limbs', 'settings': {'light_absorbed_in_the_limbs': "'our soul loathes the light bread' — the manna absorbed in the limbs (Yoma 75a); Onkelos 'this manna whose food is light'; Moses called them ingrates (Avodah Zarah 5b:1)"}, 'source': 'Num 21:5'},
    'nehushtan': {'value': 'broken_by_hezekiah_the_sages_agreed', 'settings': {'broken_by_hezekiah_the_sages_agreed': "Hezekiah ground the copper serpent (2 Kgs 18:4 'Nehushtan') and the Sages agreed (Berakhot 10b:7; Pesachim 56a; Chullin 6b-7a); 'make YOU' — Moses' own, so the worshipped serpent was no idol by right (Avodah Zarah 44a:7)"}, 'source': 'Num 21:8-9; 2 Kgs 18:4'},
    'serpent_kills_or_heals': {'value': 'the_heart_subjected', 'settings': {'the_heart_subjected': 'does the serpent kill or give life? when Israel looked upward and subjected their hearts to their Father in heaven they were healed, else they rotted (Mishnah Rosh Hashanah 3:8; Rosh Hashanah 29a:7) — with Moses\' hands at Amalek (Exod 17:11)'}, 'source': 'Num 21:8-9'},
    'arnon_miracle': {'value': 'the_mountains_met', 'settings': {'the_mountains_met': "'Vaheb in Suphah and the brooks of Arnon' — the Emorites in the caves, the ark flattened the mountains, the blood flowed to the brooks; the two lepers Et and Hev saw it and Israel sang (Berakhot 54a:16, 54b:1); 'Vahev' love at the end (Kiddushin 30b:2); the book named (Bava Batra 14b)"}, 'source': 'Num 21:14-15'},
    'well_song_reading': {'value': 'the_torah_as_a_gift', 'settings': {'the_torah_as_a_gift': "Rava: who makes himself a wilderness receives the Torah as a GIFT (Mattanah); given, God bequeaths it (Nahaliel); he rises (Bamoth); arrogant, lowered to the valley and the wasteland's threshold (Nedarim 55a:9; Eruvin 54a:21; Avot 6:2); the well's mouth created at twilight (Avot 5:6); the Levites' Sabbath song (Rosh Hashanah 31a:11)"}, 'source': 'Num 21:16-20'},
    'parable_tellers': {'value': 'balaam_and_beor', 'settings': {'balaam_and_beor': "'the parable-tellers' — Balaam and Beor (Chullin 60b); Balaam's own word (23:7, 23:18, 24:3, 24:15, 24:20-23); the homily: those who rule over their inclination (Bava Batra 78b:12)"}, 'source': 'Num 21:27; Jer 48:45-46 quotes the song'},
    'sihon_purified': {'value': 'ammon_and_moab_purified_through_sihon', 'settings': {'ammon_and_moab_purified_through_sihon': "'Heshbon was the city of Sihon who had taken all his land from Moab' — Israel forbidden Moab's land (Deut 2:9): Sihon took it, Israel took it from Sihon — Rav Pappa (Chullin 60b:13; Gittin 38a); 'from his hand' = from his possession (Bava Metzia 56b:4-7)"}, 'source': 'Num 21:26; Deut 2:9, 2:19'},
    'ammon_border': {'value': 'strong_here_commanded_at_deut_2', 'settings': {'strong_here_commanded_at_deut_2': "'for the border of the sons of Ammon was STRONG' (21:24) — Deut 2:19, 2:37: Ammon's land COMMANDED off-limits (the reading's row)"}, 'source': 'Num 21:24; Deut 2:19, 2:37'},
    'og_lore': {'value': 'sihons_brother_of_the_rephaim', 'settings': {'sihons_brother_of_the_rephaim': "Sihon and Og brothers, sons of Ahijah son of Shamhazai (Niddah 61a:18); Og of the flood's generation (Zevachim 113b:12); the mountain (Berakhot 54b); the iron bed nine by four (Deut 3:11 — the parser's %s)" % OG_BED}, 'source': 'Num 21:33-35; Deut 3:11'},
    'spy_verb': {'value': 'ragal_calebs', 'settings': {'ragal_calebs': "'Moses sent to SPY OUT Jazer' (21:32) — the other spy-verb, Caleb's (Josh 14:7), against 13:2's 'tour' (the reading's row)"}, 'source': 'Num 21:32; Josh 14:7'},
    'deaths_ceased': {'value': (40, 5, 15), 'settings': {'(40, 5, 15)': "the fifteenth of Av the dying in the wilderness ceased (Bava Batra 121a:9; Taanit 30b:12) — Shelach's row; the decree's timer due (40, 5, 9) six days before it; the Zered crossed after the mourning (21:12 after 20:29): three placements, one stretch — CM3"}, 'source': "Deut 2:14-17; Num 20:29, 21:12"},
}

import os as _os
_ROOT = _os.path.normpath(_os.path.join(_os.path.dirname(_os.path.abspath(__file__)), '..', '..'))   # THE PORTABLE REPO (2026-09-15): the repo root from this file's own place
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

# =====================================================================
# Motion 1 — THE FUNCTION, compiled from the ink (F1-F6)
# =====================================================================
# ===== F1: THE HEIFER'S RITE (Num 19:1-10) ================================================================
def heifer_rite(case, data):
    """19:1-10 — the statute, the heifer's conditions as parameters, the procession, the slaughter, the seven sprinklings, the burning
    with the kit, the rite's contagion, the ashes for a keeping. Every quantity the ink leaves open is a DATA row."""
    del P[:]
    ask = case['ask']
    if ask == 'statute_indispensable':
        ink('19:2', '"this is the STATUTE of the Torah that the LORD commanded" — the statute-word on the section (its two seats %s)' % [('%s %d:%d' % k) for k in STATUTE_SEATS])
        move('Menachot 19a:10; 27a:18, 27a:29; Yoma 42a:6; Zevachim 14b:6, 68b:5', "where law and statute are stated, omission invalidates (Rav): the three of the kit, the seven sprinklings, the priest's slaughter each indispensable")
        return out('every detail indispensable — statute and law both written (19:2)', ['disqualified'])
    if ask == 'statute_seats':
        ink('19:2, 31:21', '"this is the statute of the Torah" at its two seats — the heifer and the Midian war\'s vessels (computed)')
        return out('two seats: Num 19:2, Num 31:21', [FX.NONE])
    if ask == 'frames':
        ink('19:1; 20:7, 20:12, 20:23; 21:8, 21:34', 'six frames in the portion (computed): three to Moses and Aaron together (19:1, 20:12, 20:23)')
        return out('six frames — 19:1, 20:7, 20:12, 20:23, 21:8, 21:34', [FX.NONE])
    if ask == 'yoke':
        ink('19:2', '"upon which never came a yoke" — the yoke clause (1 Sam 6:7 its other seat: the ark-cows)')
        dat('the row heifer_yoke: %s' % data['heifer_yoke']['value'])
        move('Avodah Zarah 23a:6; Sotah 46a:11, 46a:16; Shabbat 52a:7; Pesachim 26a:16; Mishnah Parah 2:3-4', 'any burden placed disqualifies (Rav); the bit no burden; threshing by intent; for its own sake valid, for another\'s invalid; a male mounted invalid')
        burden = case.get('burden', 'sacks')
        if burden in ('bit', 'rope', 'sandal', 'cloak_against_flies', 'bird'):
            return out('valid — for its own sake, no burden (Parah 2:3-4; Shabbat 52a)', ['accepted'])
        return out('disqualified — a burden came on it (19:2; Rav: a bundle of sacks)', ['disqualified'])
    if ask == 'blemish':
        ink('19:2', '"whole, in which there is no blemish" — the blemish clause; "wherein [bah]" excludes the eglah arufah (Sotah 46a:2)')
        move('CALLED cold_run_priesthood.blemish(beast_unfits_in_man) -> %s; blemish(passed_blemish) -> %s [IMPORT, live]' % (PR_BEAST, PR_PASSED), 'all blemishes that invalidate consecrated animals invalidate the heifer (Mishnah Parah 2:3); the passed blemish fit')
        dat('the row heifer_blemish: %s' % data['heifer_blemish']['value'])
        if case.get('passed'):
            return out('fit — the blemish passed (the priesthood engine\'s row)', ['accepted'])
        return out('disqualified by any consecrated-animal blemish (Parah 2:3; Sotah 46a:2)', ['disqualified'])
    if ask == 'age':
        ink('19:2', '"a red heifer" — NO AGE in the ink')
        dat('the row heifer_age: %s' % data['heifer_age']['value'])
        return out('three or four years (the Sages); R. Eliezer two; R. Meir even five — DATA', [FX.NONE])
    if ask == 'hairs':
        ink('19:2', '"red" — the color; NO count of hairs in the ink')
        dat('the row heifer_hairs: %s' % data['heifer_hairs']['value'])
        return out('two black or white hairs in one follicle invalidate (Parah 2:5) — DATA', ['disqualified'])
    if ask == 'pregnant':
        dat('the row heifer_pregnant: %s' % data['heifer_pregnant']['value'])
        return out('invalid (the Sages); R. Eliezer valid — DATA (Parah 2:1)', ['disqualified'])
    if ask == 'from_gentile':
        ink('19:2', '"speak to the children of Israel that they take to you" — the phrase Exod 25:2 shares')
        dat('the row heifer_from_gentile: %s' % data['heifer_from_gentile']['value'])
        return out('valid from gentiles (the Sages — Parah 2:1); R. Eliezer no (Avodah Zarah 23a-24a)', ['accepted'])
    if ask == 'who_burns':
        ink('19:3', '"you shall give IT to Eleazar the priest" — the deputy named for the first')
        dat('the row who_burns: %s' % data['who_burns']['value'])
        move('Yoma 42b:10-11, 43a:3; Mishnah Parah 4:1', "the first by Eleazar alone; after it even a common priest (some say) / the high priest (some say; Parah 4:1 — R. Yehuda valid otherwise)")
        return out('the first by Eleazar the deputy; later heifers by a common priest (some say) or the high priest — DATA', [FX.NONE])
    if ask == 'who_slaughters':
        ink('19:3', '"and he shall slaughter it BEFORE HIM" — Eleazar named, the slaughter watched')
        dat('the row who_slaughters: %s' % data['who_slaughters']['value'])
        move('Yoma 42a:6-11; Menachot 6b:11; Zevachim 14b:6, 68b:5', "Shmuel: a non-priest slaughters and Eleazar watches — valid; Rav: 'Eleazar the priest' and 'statute' — a priest, else invalid")
        return out('a stranger\'s slaughter valid with Eleazar watching (Shmuel); Rav: a priest — DISPUTE', [FX.NONE])
    if ask == 'slaughter_whole':
        ink('19:3, 19:5', '"he shall slaughter... he shall burn" — as the slaughter is whole so the burning is whole')
        move('Chullin 11a:15', 'the majority followed — not a tereifa (the principle of the unquantifiable majority from the heifer)')
        return out('burned whole as slaughtered whole — the majority followed (Chullin 11a)', ['accepted'])
    if ask == 'slaughter_not_neck':
        ink('19:2-3', '"the statute" with "he shall slaughter it" — slaughter fits, neck-breaking does not')
        move('Chullin 24a:1', 'with slaughter yes, with breaking the neck no')
        return out('slaughter only — neck-breaking invalid (Chullin 24a)', ['disqualified'])
    if ask == 'slaughter_alone':
        ink('19:3', '"he shall slaughter IT" — it, not it and another')
        move('Chullin 32a:2', 'slaughtered together with even a non-sacred animal the heifer is disqualified (Rava for R. Natan)')
        return out('disqualified with another animal in one act (Chullin 32a)', ['disqualified'])
    if ask == 'outside_the_camp':
        ink('19:3-4', '"outside the camp... toward the front of the tent of meeting" — three camps, east')
        move('Yoma 68a:9; Zevachim 105b:17, 113a:4-5; Yoma 2a:6; Mishnah Parah 3:6, 4:2', "burned outside three camps, east of Jerusalem opposite the entrance (R. Eliezer); slaughtered within the walls or not opposite the entrance — disqualified; the ramp to the Mount of Olives; its own pit")
        return out('outside three camps, east, opposite the entrance — the Mount of Olives by the ramp (Yoma 68a; Parah 3:6)', ['accepted'])
    if ask == 'sprinkling':
        ink('19:4', '"with his finger... toward the front of the tent of meeting seven times" — the parser\'s %s' % SEVEN)
        move('CALLED cold_run_chatat.sprinklings(anointed) -> %d; cold_run_yoma.service_order() 16:14 -> %r [IMPORT, live]' % (CH_SEVEN, YM_1614), "the sin-bull's seven and the Day's finger — the seat's kin")
        dat('the row sprinkle_toward: %s' % data['sprinkle_toward']['value'])
        move('Menachot 27a:14, 27a:29, 27b:2; Zevachim 40a:1; Mishnah Parah 3:9, 4:2; Menachot 27b:15', 'seven indispensable, each its own dip, for its name and toward the entrance; the seventh from the sixth invalid, an eighth from the seventh valid; R. Yehuda: precisely toward')
        return out('seven sprinklings toward the entrance, each its own dip, all indispensable (19:4 [7]; Parah 3:9, 4:2)', ['sprinkled_seven'])
    if ask == 'finger_wipe':
        ink('19:4-5', '"with his finger" (19:4); "its blood" burned (19:5)')
        move('Menachot 7b:20; Zevachim 93b:14; Mishnah Parah 3:9', 'after the sprinklings the hand wiped on the body; between them the finger on the bowl\'s lip (Abaye — Ezra 1:10\'s bowls)')
        return out('the hand wiped on the heifer after the seventh; the finger on the bowl\'s lip between (Zevachim 93b)', [FX.NONE])
    if ask == 'burn_list':
        ink('19:5', '"its hide, its flesh and its blood with its dung" — %s; the sin-bull\'s lists (Exod 29:14, Lev 4:11, 16:27) carry no blood-word: %s (computed)' % (BURN_19, BLOOD_AT_SIN_BULL))
        move('CALLED cold_run_chatat.carcass(anointed) -> %s; blood(anointed) -> %s [IMPORT, live]' % (CH_CARCASS, CH_BLOOD), "the sin-bull's carcass burned outside the camp; its blood brought INSIDE — the heifer's blood burned with the flesh instead (Menachot 7b:20; Zevachim 93b:14)")
        return out('the sin-bull\'s burn-list WITH THE BLOOD ADDED — burned whole with its blood (19:5; Zevachim 93b)', ['accepted'])
    if ask == 'kit':
        ink('19:6', '"cedar wood and hyssop and scarlet" cast into the burning — the order %s = the house\'s dipping at Lev 14:51-52 %s; the three takings 14:4 / 14:6 / 14:49 %s (measured at six seats)' % (KIT_19, KIT_14_51, KIT_14_49))
        move('CALLED cold_run_metzora.birds(kit) -> %s [IMPORT, live]' % MZ_KIT, "the leper's four (two birds, cedar, scarlet, hyssop) — the heifer's three")
        dat('the row bundle: %s' % data['bundle']['value'])
        move('Menachot 27a:13, 27a:18; Mishnah Menachot 3:6; Yoma 41b:18, 43a:4; Mishnah Parah 3:10-11', 'the three indispensable by "statute"; by a priest; burned in the air before the mass valid, singed before it replaced; asked thrice, wrapped, cast')
        return out('cedar, hyssop and scarlet — the three indispensable, cast into the burning by a priest (19:6; Menachot 27a)', ['accepted'])
    if ask == 'kit_order':
        ink('19:6; Lev 14:4, 14:6, 14:49, 14:51, 14:52', 'the kit\'s order at the six seats (computed): the heifer %s; the takings 14:4 %s, 14:6 %s, 14:49 %s; the house\'s dipping 14:51 %s, 14:52 %s' % (KIT_19, KIT_14_4, KIT_14_6, KIT_14_49, KIT_14_51, KIT_14_52))
        return out('the heifer\'s order is Lev 14:51-52\'s (cedar, hyssop, scarlet — the house\'s dipping); the takings 14:4, 14:6, 14:49 have cedar, scarlet, hyssop — computed at six seats', [FX.NONE])
    if ask == 'priest_in_garments':
        ink('19:7', '"the PRIEST shall wash his garments... and the priest shall be unclean until the evening" — the priest restated')
        move('Yoma 43a:5; Mishnah Parah 4:1', 'in his priestly state — the garments worn, in future generations too; prepared in WHITE garments; not in all the garments invalid')
        return out('by a priest in his garments — white garments (Parah 4:1; Yoma 43a)', ['accepted'])
    if ask == 'work_invalidates':
        ink('19:3-9', 'the rite\'s stages from the slaughter to the ashes')
        dat('the row work_invalidates: %s' % data['work_invalidates']['value'])
        move('Mishnah Parah 4:4, 7:1-12, 8:1', 'other work invalidates until it is ashes; the water\'s filling and mixing by the purpose test; the two guards')
        return out('other work invalidates from the slaughter until the ashes; the water until the ashes are in it (Parah 4:4, 7)', ['disqualified'])
    if ask == 'sequestering':
        ink('19:2', '"that the LORD commanded" — with Lev 8:34\'s "commanded"')
        move('Yoma 2a:10; Mishnah Parah 3:1', 'sequestered seven days before the heifer as before the inauguration; sprinkled all seven (R. Yose: the third and seventh)')
        return out('seven days\' sequestering in the Stone Chamber, sprinkled through them (Yoma 2a; Parah 3:1)', ['accepted'])
    if ask == 'procession':
        move('Mishnah Parah 3:2-3, 3:6-8', 'the children born over the hollow, the oxen with doors, the Shiloah\'s water, the ashes taken by a child; the ramp; the pile of cedar, pine, spruce and fig wood facing west; the immersion')
        return out('the children\'s water, the child\'s mixing, the ramp to the Mount of Olives, the pile facing west (Parah 3:2-8)', [FX.NONE])
    if ask == 'tvul_yom':
        ink('19:19, 19:9', '"the CLEAN one shall sprinkle on the unclean" — clean by inference from unclean; "a clean man" gathers')
        dat('the row tvul_yom_fit: %s' % data['tvul_yom_fit']['value'])
        move('Yoma 43b:3; Zevachim 17b:3; Yevamot 73a:1; Mishnah Parah 3:7', 'the tevul yom fit to sprinkle and to burn; the burning priest deliberately defiled and immersed against the Sadducees')
        return out('the tevul yom fit — the burner defiled on purpose against the Sadducees (Parah 3:7; Yoma 43b)', ['accepted'])
    if ask == 'gatherer':
        ink('19:9', '"a MAN who is PURE shall gather the ashes of the heifer and PLACE them" — three words')
        dat('the row who_sanctifies: %s; the row a_clean_man: %s' % (data['who_sanctifies']['value'], data['a_clean_man']['value']))
        move('Yoma 43a:7; Yevamot 72b:16', "'a man' a non-priest; 'pure' even a woman; 'place' excludes the deaf-mute, imbecile and minor; the sanctifier as the gatherer")
        return out('a non-priest and a woman gather; the deaf-mute, imbecile and minor do not (Yoma 43a:7)', ['ashes_kept_for_niddah_water'])
    if ask == 'ashes_thirds':
        ink('19:9', '"lay them outside the camp in a clean place... for a keeping, for waters of niddah" — "for a keeping" the manna jar\'s and Aaron\'s staff\'s word')
        dat('the row ashes_thirds: %s' % data['ashes_thirds']['value'])
        return out('three parts — the rampart, the Mount of Olives, the priestly watches (Parah 3:11); kept for waters of niddah', ['ashes_kept_for_niddah_water'])
    if ask == 'meilah':
        ink('19:9', '"it is a SIN OFFERING" — Exod 29:14\'s formula')
        dat('the row meilah_on_the_heifer: %s' % data['meilah_on_the_heifer']['value'])
        move('CALLED cold_run_vayikra5.sacrilege(meilah) -> %s [IMPORT, live]' % V5_MEILAH, "me'ilah applies to the heifer by Torah law (Menachot 51b:22); always subject to trespass (Parah 4:4)")
        return out('me\'ilah applies — a sin offering (19:9; Menachot 51b): the principal, the fifth, the ram', ['pays'])
    if ask == 'for_its_name':
        move('Mishnah Parah 4:1, 4:3', 'slaughtered, received or sprinkled not for its name invalid (R. Eliezer valid); the intention to eat its flesh harmless (R. Eliezer: no intention invalidates)')
        return out('not for its name invalid; the eating intention harmless (Parah 4:1, 4:3)', ['disqualified'])
    if ask == 'nine_heifers':
        ink('19:2', 'the heifer commanded — its first burning NEVER NARRATED in the ink: the tape\'s debit OPEN')
        dat('the row nine_heifers: %s' % data['nine_heifers']['value'])
        return out('nine heifers — Moses, Ezra, seven after (the Sages; R. Meir five): the shelf\'s run of the open debit (Parah 3:5)', [FX.NONE])
    if ask == 'day_and_priest':
        ink('19:2, 19:19', '"law" includes the rite\'s stages; "THIS is the statute" excludes the gathering, the filling and the sanctification; "on the third DAY"')
        move('Yoma 42b:3-4; Mishnah Parah 4:4', 'the slaughter, the blood, the sprinkling, the burning and the casting by a man by day; the ashes, the water and the mixing not so bound')
        return out('the rite\'s stages by a priest by day; the gathering, filling and mixing not so bound (Yoma 42b; Parah 4:4)', ['accepted'])
    if ask == 'attention':
        ink('19:3, 19:5, 19:9', '"before him" / "in his sight" / "it shall be kept" — the attention clauses')
        move('Yoma 42a:11, 42b:1', 'no diverting of attention from the slaughter to the completion, through the gathering; the casting of the kit excepted')
        return out('attention undiverted from the slaughter through the keeping; the kit\'s casting excepted (Yoma 42a-b)', ['accepted'])
    if ask == 'defiles_garments':
        ink('19:7-8, 19:10', '"the priest shall be unclean until the evening... he who burns it... he who gathers" — the rite\'s three made unclean (impure_until_evening each)')
        move('Mishnah Parah 4:4, 8:3; Yoma 14a', "everyone occupied from the slaughter to the ashes defiles his garments; the heifer itself does not — the paradox: 'that which defiled you did not defile me'")
        return out('the burner, the gatherer and the priest unclean until evening — the rite defiles its servants, the heifer does not (Parah 4:4, 8:3)', ['impure_until_evening'])
    if ask == 'wood':
        move('Mishnah Parah 3:8, 4:3', 'the pile of cedar, pine, spruce and fig wood; burned with any wood, straw or stubble valid; flayed and cut valid')
        return out('any wood, straw or stubble valid; the pile\'s four woods (Parah 3:8, 4:3)', ['accepted'])
    if ask == 'taken_out_alone':
        ink('19:3', '"he shall bring IT out" — it alone')
        move('Yoma 42b:12; Mishnah Parah 3:7', 'no black cow, no second red heifer taken out with it (Rebbi from "it"; the Sages lest people say)')
        return out('brought out alone — no black cow, no second red one (Parah 3:7; Yoma 42b)', ['accepted'])
    if ask == 'who_sprinkles_blood':
        ink('19:4', '"Eleazar the priest shall take of its blood with his finger" — Eleazar named again')
        move('Yoma 43a:3; Kiddushin 36b:2', "Shmuel: returned to Eleazar for the blood; Rav: a restrictive after a restrictive includes a common priest; women excluded a fortiori")
        return out('a priest sprinkles the blood — Eleazar (Shmuel) or any priest (Rav); not a woman (Kiddushin 36b)', ['accepted'])
    if ask == 'madaf':
        dat('the row madaf: %s' % data['madaf']['value'])
        move('Mishnah Parah 10:1-6', "the heifer-purity's stringency: the hatat-clean touching food with the hand unclean, with the foot clean; the flask over the oven disputed; the two flasks")
        return out('madaf — the unclean has it, the clean not (the Sages; Parah 10:1); the hand defiles, the foot not (10:2)', ['disqualified'])
    if ask == 'first_heifer_open':
        ink('19:1-22', 'the statute spoken; no verse of the Torah narrates the first heifer\'s burning')
        return out('the heifer\'s debit OPEN on the tape — the ink never narrates the first burning; Parah 3:5 the shelf\'s run', [FX.NONE])
    return out('no verdict in span', [FX.NONE])


# ===== F2: THE CORPSE'S UNCLEANNESS AND THE SPRINKLING (Num 19:11-22) ======================================
def corpse_tumah(case, data):
    """19:11-22 — the toucher's seven days, the third and the seventh as timers with the four failure states, the punishment split, the
    tent, the open vessel, the field's four sources, the water and the sprinkler; the removes and the geometry as data (Oholot)."""
    del P[:]
    ask = case['ask']
    day = case.get('day', 0)
    if ask == 'seven_days':
        ink('19:11', '"he who touches the dead of any human soul shall be unclean SEVEN days" — the parser\'s %s; "a human soul" the blasphemer\'s clause (Lev 24:17)' % SEVENS[0])
        return out('unclean seven days — the toucher (19:11)', ['corpse_unclean_seven_days'])
    if ask == 'schedule':
        ink('19:12, 19:19', '"he shall purify himself on the third day and on the seventh day" — the ordinal reader\'s %s and %s' % (SCHEDULE, SCHEDULE_19))
        dat('the row third_day_fixed: %s' % data['third_day_fixed']['value'])
        move('Kiddushin 62a:4-7; Shabbat 16b:3; Sifrei 125', 'the third excludes the second, the seventh the sixth; the third and the eighth invalid — a fixed interval; both needed even for terumah')
        third, seventh = case.get('third', True), case.get('seventh', True)
        if third and seventh:
            return out('sprinkled on the third and the seventh: clean in the evening of the seventh (19:12, 19:19)', ['sprinkling_due_third_day', 'sprinkling_due_seventh_day', 'declared_pure'])
        if third and not seventh:
            return out('the seventh omitted: not clean (19:12b)', ['sprinkling_due_third_day', 'not_purified'])
        if seventh and not third:
            return out('the third omitted: the seventh does not clean — the interval fixed (Kiddushin 62a)', ['sprinkling_due_seventh_day', 'not_purified'])
        return out('neither sprinkling: not clean — his uncleanness is yet on him (19:13)', ['not_purified'])
    if ask == 'purification':                                                  # THE PAID EDGE naso -> chukat: 5:2's corpse-unclean sent out of the Presence's camp — his purification here
        ink('19:12, 19:19', 'the corpse-unclean purified by the water of niddah on the third and the seventh day; sent out of the Presence\'s camp alone (5:2 — naso\'s ladder)')
        return out('the third and the seventh day\'s sprinkling with the water of niddah, then the wash, the bath and the evening (19:12, 19:19)', ['sprinkling_due_third_day', 'sprinkling_due_seventh_day', 'declared_pure'])
    if ask == 'sprinkling_water':                                              # THE PAID EDGE beha -> chukat: 8:7's water of purification on the Levites
        ink('19:9, 19:17-18', '"waters of niddah" — the ashes kept for it; living water into a vessel; a clean man dips hyssop and sprinkles')
        return out('the heifer\'s ashes on living water in a vessel, sprinkled with hyssop by a clean man (19:9, 19:17-18) — 8:7\'s water', ['declared_pure'])
    if ask == 'minor':
        dat('the row minor_and_karet: %s' % data['minor_and_karet']['value'])
        move('Arakhin 3a:6-7; Niddah 44a:7', "'the persons that were there' — a minor becomes impure, a day old; 'the man' excludes him from the karet")
        return out('a minor impure (even a day old), no karet for his entry (Arakhin 3a; Niddah 44a)', ['corpse_unclean_seven_days', 'exempt'])
    if ask == 'toucher_of_toucher':
        ink('19:22', '"whatever the unclean touches shall be unclean, and the soul that touches shall be unclean until the evening"')
        move('Avodah Zarah 37b:7, 37b:9; Mishnah Oholot 1:1', 'the toucher of the toucher impure by Torah law — until evening: the second grade')
        return out('the toucher of the toucher unclean until evening (19:22; Oholot 1:1)', ['impure_until_evening'])
    if ask == 'removes':
        dat('the row removes: %s' % data['removes']['value'])
        move('Mishnah Oholot 1:1-4; Kelim 1:4; Avodah Zarah 37b:9', 'two, three, four defiled through a corpse; the tent does not count; the corpse the top of the ladder')
        return out('the removes — the toucher seven days, the second until evening; vessels three in a series, persons two (Oholot 1:1-4)', ['corpse_unclean_seven_days', 'impure_until_evening'])
    if ask == 'karet_entry':
        ink('19:13, 19:20', '"he has defiled the TABERNACLE of the LORD, and that soul shall be cut off" / "the SANCTUARY of the LORD" — the Sifrei\'s pair; the punishment here, the prohibition at 5:3')
        dat('the row punishment_split: %s' % data['punishment_split']['value'])
        move('Makkot 14b:6, 14b:8, 8a:16, 8b:1; Zevachim 33b:5, 43b:8; Shevuot 7b:1, 2a:2; Nazir 45a:5; Mishnah Keritot 1:1-2; Mishnah Shevuot 1:1-2:5', "karet and lashes for the impure who entered; the met mitzvah's burier not exempt; any impurity; the body's impurity; the tevul yom and the lacking-atonement included; the unwitting's sliding-scale offering; the awareness grid as data")
        if case.get('intent') == 'unwitting':
            return out('unwitting entry — the sliding-scale offering by the awareness grid (Mishnah Shevuot 1:1-2:5; Keritot 1:2)', ['disqualified'])
        return out('cut off — the intentional entry of the impure into the sanctuary; lashes with it (19:13, 19:20; Makkot 14b)', ['karet_cut_off', 'lashes'])
    if ask == 'high_priest_exempt':
        dat('the row high_priest_exempt: %s' % data['high_priest_exempt']['value'])
        return out('the high priest exempt from the entry\'s karet (Horayot 9b; Parah 12:4)', ['exempt'])
    if ask == 'impure_inside':
        move('Shevuot 16b:1; Mishnah Shevuot 2:3', 'the second verse (19:20) for one made impure INSIDE the courtyard who bowed, tarried or left by the longer route: liable; the shortest way exempt')
        return out('made impure inside: liable unless he leaves by the shortest way (Shevuot 16b; Mishnah Shevuot 2:3)', ['disqualified'])
    if ask == 'metal_vessels_decree':
        move('Shabbat 16b:3', "the Sages' decree of previous impurity on metal vessels — a fence for the purification water's use")
        return out('metal vessels keep their impurity until the sprinkling — the Sages\' fence (Shabbat 16b)', ['disqualified'])
    if ask == 'tent':
        ink('19:14', '"this is the Torah: a man who dies in a tent — everyone who comes into the tent and everything in the tent shall be unclean seven days"')
        dat('the row tent_measure: %s; the row tent_material: %s' % (data['tent_measure']['value'], data['tent_material']['value']))
        move('Mishnah Oholot 3:6-7; Shabbat 17a:2; Sukkah 21a:1; Shabbat 28a:1', 'the handbreadth; any shelter (the Rabbis) / man-made (R. Yehuda); linen by the analogy, widened')
        return out('the tent\'s enterers and contents unclean seven days — by the handbreadth (19:14; Oholot 3:6-7)', ['tent_unclean', 'corpse_unclean_seven_days'])
    if ask == 'tent_gentile':
        dat('the row tent_gentile: %s' % data['tent_gentile']['value'])
        return out('gentiles\' graves defile by touch and carrying, not by tent (Bava Metzia 114b; Yevamot 61a)', ['exempt'])
    if ask == 'tent_limbs':
        move('Bekhorot 45a:20', "'when a person dies in a tent' — only what is equal for all people (the limbs found only in a woman do not defile in a tent)")
        return out('the tent\'s impurity from the limbs equal for all (Bekhorot 45a)', [FX.NONE])
    if ask == 'tent_material':
        dat('the row tent_material: %s' % data['tent_material']['value'])
        return out('any shelter (the Rabbis — "tent, tent" amplifies); R. Yehuda man-made (Sukkah 21a; Shabbat 28a)', [FX.NONE])
    if ask == 'tent_measure':
        dat('the row tent_measure: %s' % data['tent_measure']['value'])
        return out('a handbreadth square blocks and conveys; a corpse\'s opening four; the beam\'s circumference three round, four square (Oholot 3:6-7, 12:6-7)', [FX.NONE])
    if ask == 'overshadowing_table':
        move('Mishnah Oholot 4-15', "the cupboard, the oven, the hatch, the hive, the projection, the split house, the partitions — the tradition's tables of overshadowing as DATA: 'the manner of uncleanness is to go out and not to go in'; a cubic handbreadth the unit")
        return out('the overshadowing tables as DATA (Oholot 4-15) — the handbreadth the unit; out, not in', [FX.NONE])
    if ask == 'open_vessel':
        ink('19:15', '"and every open vessel that has no cord-bound cover upon it is unclean" — Onkelos inserts OF EARTHENWARE')
        dat('the row vessel_census: %s; the row tzamid_patil: %s' % (data['vessel_census']['value'], data['tzamid_patil']['value']))
        move('Chullin 25a:3, 25a:10, 71a:24; Chagigah 22a:19, 25a:5; Shabbat 84b:3; Mishnah Kelim 9:1-10:8; Oholot 5:3-7, 8:6; Eduyot 1:14; Parah 11:1', 'the earthenware\'s airspace; the tight cover protects (not holies; not the hatat water itself); the materials; Beit Shammai\'s foods-only arm, Beit Hillel retracted')
        if case.get('covered'):
            return out('protected — a cord-bound cover on it: earthenware protects foods, liquids and earthenware; the other vessels everything (19:15; Kelim 10:1)', ['exempt'])
        return out('unclean — an open vessel in the tent (19:15; Kelim 10:1)', ['open_vessel_unclean'])
    if ask == 'field_sources':
        ink('19:16, 19:18', '"one slain by the sword, or a dead body, or a human bone, or a grave" — the four; reordered at 19:18: %s -> %s (computed)' % (SRC_16, SRC_18))
        dat('the row field_phrase: %s; the row bone_measure: %s' % (data['field_phrase']['value'], data['bone_measure']['value']))
        move('Nazir 53b:10, 54a:1; Chullin 2b:14, 72a:6; Avodah Zarah 37b:5; Mishnah Oholot 2:1-7', 'the Sages\' four readings: the overlier, the limb from the living, the barley-grain bone, the sealed grave that breaks through; the tent\'s list as data')
        return out('the four sources — the slain, the dead, the bone (a barley-grain), the grave: unclean seven days (19:16; Nazir 54a; Oholot 2)', ['corpse_unclean_seven_days'])
    if ask == 'sword_like_slain':
        dat('the row sword_like_slain: %s' % data['sword_like_slain']['value'])
        return out('a sword is like the slain — the metal vessel takes the corpse\'s grade (Pesachim 14b, 79a; Shabbat 101b)', ['corpse_unclean_seven_days'])
    if ask == 'fetus_in_womb':
        dat('the row field_phrase: %s' % data['field_phrase']['value'])
        return out('the dead fetus in the womb — excluded (R. Yishmael) / impure from "of the life" (R. Akiva) — DISPUTE (Chullin 72a)', [FX.NONE])
    if ask == 'quarter_log_blood':
        ink('19:13', '"of the LIFE of a person that died" — a quarter-log of blood, the life (Deut 12:23)')
        dat('the row bone_measure: %s' % data['bone_measure']['value'])
        move('Chullin 72a:8; Mishnah Oholot 2:2, 3:2-5', 'a quarter-log defiles like the corpse; absorbed in the ground clean; mixed blood the arms')
        return out('a quarter-log of blood defiles as the corpse (Chullin 72a; Oholot 2:2)', ['corpse_unclean_seven_days'])
    if ask == 'living_water':
        ink('19:17', '"living water into a vessel" — Isaac\'s well\'s word (Gen 26:19)')
        dat('the row living_water: %s' % data['living_water']['value'])
        move('Pesachim 34b:13; Sanhedrin 5b:7; Mishnah Parah 6:4-5, 8:8-11; Mikvaot 1:8', 'the spring\'s water drawn into a vessel; the conduit\'s susceptibility; the seas, marsh and mixed rivers unfit; the sixth degree')
        return out('spring water drawn straight into a vessel; the seas and the marsh rivers unfit (Pesachim 34b; Parah 8:8-11)', ['accepted'])
    if ask == 'mixing_order':
        ink('19:17', '"of the DUST of the burning" — ashes called dust (19:9-10 ashes; 19:17 dust — the two words)')
        dat('the row mixing_order: %s' % data['mixing_order']['value'])
        move('Sotah 16b:15; Temurah 12b:7; Chullin 88b:8; Sukkah 37b:1; Mishnah Parah 6:1-3', 'the ashes ON the water (the sotah analogy); by hand, intentionally; the sponge')
        return out('the ashes upon the water, by hand and with intent — the dust-word for the sotah analogy (Sotah 16b; Parah 6:1)', ['accepted'])
    if ask == 'sprinkler_who':
        dat('the row sprinkler_who: %s' % data['sprinkler_who']['value'])
        return out('a man, not a woman (a minor by "pure"); R. Yehuda: an adult, a woman by "pure" — DISPUTE (Yoma 43a; Parah 12:10)', [FX.NONE])
    if ask == 'who_sanctifies':
        dat('the row who_sanctifies: %s' % data['who_sanctifies']['value'])
        return out('as the gatherer — a woman sanctifies; two take and one puts (Yevamot 72b; Yoma 43a)', ['accepted'])
    if ask == 'sprinkling_day':
        dat('the row sprinkling_day: %s' % data['sprinkling_day']['value'])
        return out('by day, from sunrise; dipped by day and sprinkled at night invalid (Megillah 20a; Parah 12:11)', ['disqualified'])
    if ask == 'sprinkling_on_pure':
        move('Yoma 14a:5; Mishnah Parah 12:3', "R. Akiva: sprinkled on the pure he becomes impure; the Rabbis: only on the susceptible counts; the intention grid")
        return out('sprinkling counts only on the susceptible (the Rabbis); R. Akiva: the pure sprinkled becomes impure — DISPUTE', [FX.NONE])
    if ask == 'sprinkler_carrier':
        ink('19:21', '"he who sprinkles the water of niddah shall wash his clothes, and he who touches shall be unclean until the evening"')
        dat('the row sprinkler_or_carrier: %s' % data['sprinkler_or_carrier']['value'])
        move('Yoma 14a:9; Niddah 9a:15; Mishnah Parah 12:5; Kelim 1:1-2', "'sprinkles' = carries a sprinkling's worth: the sprinkler clean, the carrier's grade heavier than the toucher's")
        return out('the sprinkler clean, the carrier washes his clothes, the toucher unclean until evening (19:21; Yoma 14a)', ['washes_and_bathes', 'impure_until_evening'])
    if ask == 'hyssop_dip':
        ink('19:18', '"a clean man shall take hyssop and dip it in the water and sprinkle" — the Passover\'s two verbs (Exod 12:22)')
        move('Sukkah 37a:8; Menachot 7b:9; Zevachim 93b:5; Gittin 86b:14; Mishnah Parah 12:1-2', 'lengthened by a string valid (taking by another object); enough water from the outset; the diminished water by the tips; the doubts invalid')
        return out('the hyssop dipped in the vessel\'s own water, lengthened if short; the doubts invalid (Sukkah 37a; Parah 12:1-2)', ['accepted'])
    if ask == 'hyssop_species':
        move('CALLED cold_run_metzora.birds(hyssop) -> %s [IMPORT, live]' % MZ_HYSSOP, "the leper's hyssop the same species")
        move('Mishnah Parah 11:7-9', 'plain hyssop — not lavender, blue, Roman or wild; three stalks with three buds; the leper\'s shared')
        return out('plain hyssop of three stalks — the leper\'s kind; the named kinds invalid (Parah 11:7-9)', ['accepted'])
    if ask == 'water_measure':
        dat('the row sprinkler_measure: %s' % data['sprinkler_measure']['value'])
        return out('enough to dip the tips of the buds and sprinkle (Parah 12:5; Sifrei 129); under it a father by contact, above by carrying (Kelim 1:1-2)', [FX.NONE])
    if ask == 'connection':
        move('Shabbat 48b:10, 58b:11; Mishnah Parah 12:8-10', 'parts that come apart are a connection for impurity, not for the sprinkling; the kettle\'s lid on a chain by the houses')
        return out('connected for impurity, not for the sprinkling — each part sprinkled (Shabbat 48b; Parah 12:9)', ['disqualified'])
    if ask == 'sprinkle_on_part':
        move('Kiddushin 25a:15', 'Rebbi: the sprinkling reaches any part of the body that can become impure')
        return out('on any part of the body that can become impure (Rebbi — Kiddushin 25a) — DISPUTE', [FX.NONE])
    if ask == 'gentile_no_tumah':
        dat('the row gentile_no_tumah: %s' % data['gentile_no_tumah']['value'])
        return out('the gentile has no corpse-impurity — no membership in the assembly (Nazir 61b)', ['exempt'])
    if ask == 'tevul_yom_hatat':
        move('Mishnah Parah 11:4-6', 'the Torah\'s immersers defile holies and terumah and may not enter; the scribes\' immersers no guilt for entering; all defile the hatat water and ashes')
        return out('the tevul yom by Torah law guilty for entering; by the scribes\' word not; both defile the hatat water (Parah 11:4-6)', ['disqualified'])
    if ask == 'invalid_water':
        move('Mishnah Parah 9:1-9; Gittin 86b:14', 'water or dew fallen in (R. Eliezer / the Sages); insects that burst, a beetle; the drinkers except the dove; the cow that drank; the kartzit harmless')
        return out('invalidated by water fallen in, bursting insects, a beast that drank; the kartzit harmless (Parah 9; Gittin 86b)', ['disqualified'])
    if ask == 'water_defiles':
        move('Mishnah Parah 8:2, 9:8-9, 11:2-3, 12:6-7', 'the sandal paradox; the two cleannesses; the terumah figs; the hyssop\'s and the hands\' chains to a hundred')
        return out('the hatat water defiles the terumah-clean by hands or body, the hatat-clean by hands (Parah 9:8; the chains 12:6-7)', ['disqualified'])
    if ask == 'water_transport':
        move('Mishnah Parah 9:6', 'not carried across a river by ship, floated or thrown; crossed with the water to the neck')
        return out('not carried across a river by ship (Parah 9:6)', ['disqualified'])
    if ask == 'vessel_for_water':
        move('Mishnah Parah 5:2-9', 'the vessel dried; a vessel required — not the walls, a jug\'s side, cupped hands; the trough in the rock no vessel; two troughs joined by a spout')
        return out('a vessel required for the filling, the mixing and the sprinkling; the trough in the rock is none (Parah 5:5-9)', ['disqualified'])
    if ask == 'all_trusted':
        ink('19:9', '"it shall be kept for the congregation" — R. Yehuda: all believed in guarding the water')
        move('Tosefta Chagigah 3:20; Mishnah Parah 5:1; Oholot 5:5', 'the am haaretz trusted for the hatat; the vessel\'s bringer; a vessel clean for purification protects with the tent\'s walls')
        return out('all are trusted for the heifer\'s water (Tosefta Chagigah 3:20; Parah 5:1)', ['accepted'])
    if ask == 'bet_peras':
        move('Mishnah Oholot 16:2-18:6', 'the mounds near a city; the graveyard\'s search; the plowed grave a hundred cubits; the three kinds; the purification by three handbreadths; the land of the gentiles')
        return out('a bet peras — the plowed grave\'s hundred cubits, the lost grave\'s field, the kokhin field: contact and carriage; purified by three handbreadths (Oholot 17-18)', ['corpse_unclean_seven_days'])
    if ask == 'gentile_dwellings':
        move('Mishnah Oholot 18:7-10', 'gentile dwellings unclean after forty days; the drains examined; ten places excepted')
        return out('gentile dwellings unclean after forty days; ten places excepted (Oholot 18:7-10)', ['corpse_unclean_seven_days'])
    if ask == 'grave_stones':
        move('Mishnah Oholot 2:4, 15:8-9; Chullin 72a:6', 'the covering and buttressing stones by contact and overshadowing (R. Akiva from "the open field"); the tomb\'s courtyard; the jar and the animal as covering stones')
        return out('the grave\'s covering and buttressing stones defile by contact and overshadowing, not carriage (Oholot 2:4)', ['corpse_unclean_seven_days'])
    if ask == 'limb':
        move('Mishnah Oholot 1:7-8, 3:3-4; Eduyot 6:2-3', 'a whole limb no minimum; 248 limbs; the teeth, hair and nails clean apart; human connections not connections; the limb from the living disputed')
        return out('a whole limb defiles at any size; 248 limbs; the teeth, hair and nails clean when severed (Oholot 1:7-8, 3:3)', ['corpse_unclean_seven_days'])
    if ask == 'bone_measure':
        dat('the row bone_measure: %s' % data['bone_measure']['value'])
        return out('a barley-grain of bone by contact and carriage; a quarter-kav or the majority by tent; deficient clean (Oholot 2:1-7)', [FX.NONE])
    if ask == 'death_moment':
        move('Mishnah Oholot 1:6', 'no corpse-defilement until death; cut up or dying he binds the levirate and feeds terumah; the convulsing beast unclean')
        return out('defiles from the death, not before — the dying binds and feeds still (Oholot 1:6)', [FX.NONE])
    if ask == 'dry_flesh':
        move('Niddah 55a:4', 'as a bone is dry, the corpse defiles even when dry (R. Yochanan from 19:16)')
        return out('the corpse defiles dry, as the bone (Niddah 55a)', ['corpse_unclean_seven_days'])
    if ask == 'birth_and_fetus':
        move('Mishnah Oholot 7:4-6', 'the woman in hard labor carried between houses; twins; the child cut up for her life, not after the greater part emerged')
        return out('the opened tomb; the mother\'s life before the fetus until the greater part emerges (Oholot 7:4-6)', [FX.NONE])
    if ask == 'ox_goad':
        move('Shabbat 17a:2; Mishnah Oholot 16:1-2', "R. Akiva's three measures: to the carrier at an ox-goad's thickness, to themselves at any, to others at a handbreadth")
        return out('movables convey to the carrier at an ox-goad\'s thickness, to themselves at any, to others at a handbreadth (Oholot 16:1)', ['corpse_unclean_seven_days'])
    if ask == 'window_measures':
        move('Mishnah Oholot 13:1-6', 'the light-hole by the drill; for use a square handbreadth; the reducers and the non-reducers: the clean reduces, the unclean does not')
        return out('the window\'s measures — the drill\'s hole for light, a square handbreadth for use; the clean reduces (Oholot 13)', [FX.NONE])
    if ask == 'madaf':
        dat('the row madaf: %s' % data['madaf']['value'])
        return out('madaf for the hatat — the unclean has it, the clean not (Parah 10:1)', [FX.NONE])
    if ask == 'mikveh_grades':
        move('Mishnah Mikvaot 1:1-8, 2:1-10', 'six degrees of waters — the pools, the unstopped flows, forty seahs, the small spring, the smitten waters, the living waters; the doubts; the three logs')
        return out('six degrees — the living waters the top: the zav, the leper and the hatat water (Mikvaot 1:8)', ['accepted'])
    if ask == 'camps':
        move('Mishnah Kelim 1:7-8', 'the corpse carried within the walled city but not brought back; the corpse-impure barred at the chel — naso\'s three camps by the paid CALL')
        return out('the corpse-impure barred at the chel; out of the Presence\'s camp alone (Kelim 1:8; Num 5:2)', ['sent_outside_the_camp'])
    if ask == 'torah_endures':
        move('Berakhot 63b:14; Gittin 57b:22; Shabbat 83b:10', 'Reish Lakish: "this is the Torah: when one dies in a tent" — Torah endures in one who kills himself over it (the homily\'s three seats)')
        return out('the homily — Torah endures in one who kills himself over it in its tent (Berakhot 63b)', [FX.NONE])
    return out('no verdict in span', [FX.NONE])

# ---- the retellings and the echoes, computed on the ink (F3-F6's crowns) ----
THEN_SANG = sorted(k for k, ws in _BYV.items() if any(ws[i] == 'אז' and ws[i + 1] == 'ישיר' for i in range(len(ws) - 1)))
assert THEN_SANG == [('Exod', 15, 1), ('Num', 21, 17)], THEN_SANG                 # "then sang" — the sea's and the well's
LAWGIVER = seats_of('מחקק') + seats_of('במחקק') + seats_of('ומחקק'); assert set(('Gen 49:10', 'Num 21:18', 'Deut 33:21')) <= set(LAWGIVER), LAWGIVER
SURVIVOR = sorted(('%s %d:%d' % k) for k, ws in _BYV.items() if any(ws[i] == 'בלתי' and ws[i + 1] == 'השאיר' for i in range(len(ws) - 1)))
assert set(('Num 21:35', 'Deut 3:3', 'Josh 8:22', 'Josh 10:33', '2Kgs 10:11')) <= set(SURVIVOR), SURVIVOR   # "until no survivor was left" — Joshua's refrain born here
def delta(a, b):
    A, B = verse_text(*a[1:], book=a[0]).split(), verse_text(*b[1:], book=b[0]).split()
    return [w for w in A if w not in B], [w for w in B if w not in A]
D33 = delta(('Num', 21, 33), ('Deut', 3, 1)); D34 = delta(('Num', 21, 34), ('Deut', 3, 2)); D35 = delta(('Num', 21, 35), ('Deut', 3, 3))
assert D33 == (['ויפנו', 'ויעלו', 'לקראתם'], ['ונפן', 'ונעל', 'לקראתנו']) and D34[0] == ['משה'] and D34[1] == ['אלי'], (D33, D34)   # Deut 3 = 21:33-35 with the pronouns shifted
JER = set(verse_text(48, 45, book='Jer').split()) & set(verse_text(21, 28).split()); assert JER == {'כי', 'אש', 'מחשבון', 'מואב'}, JER   # Jeremiah 48:45 quotes 21:28 with FOUR exact tokens ("for a fire", "from Heshbon", "Moab") — the rest shifted in spelling (read off the assert driver, 2026-09-11: the hand had typed >= 5, and had reversed chapter and verse in five calls)
MERIBAH_17 = set(verse_text(17, 2, book='Exod').split()) | set(verse_text(17, 3, book='Exod').split())
FIRST_MERIBAH_CLAUSES = [w for w in ('וירב', 'העליתנו', 'ממצרים') if w in verse_text(20, 3).split() + verse_text(20, 5).split() and w in MERIBAH_17]
assert FIRST_MERIBAH_CLAUSES == ['וירב', 'העליתנו', 'ממצרים'], FIRST_MERIBAH_CLAUSES   # the first Meribah's clauses at the second
FIRSTFRUITS = [w for w in ('ונצעק', 'וירעו') if w in verse_text(20, 15).split() + verse_text(20, 16).split()]
assert 'ונצעק' in FIRSTFRUITS and 'ונצעק' in verse_text(26, 7, book='Deut').split(), FIRSTFRUITS   # "and we cried" — Deut 26:7's clause in the Edom letter

# ===== F3: MIRIAM'S DEATH AND THE WATERS OF MERIBAH (Num 20:1-13) ==========================================
def meribah(case, data):
    del P[:]
    ask = case['ask']
    if ask == 'well_by_merit':
        ink('20:1-2', '"and Miriam died there... and there was no water for the congregation" — the two verses adjacent')
        dat('the row well_by_merit: %s' % data['well_by_merit']['value'])
        return out('the well gone at Miriam\'s death, returned by Moses\' and Aaron\'s merit (Taanit 9a; Seder Olam 10:2)', [FX.NONE])
    if ask == 'death_by_the_kiss':
        dat('the row death_by_the_kiss: %s' % data['death_by_the_kiss']['value'])
        return out('Miriam too by the kiss — "there" / "there" with Deut 34:5 (Bava Batra 17a)', [FX.NONE])
    if ask == 'burial_near_death':
        ink('20:1', '"and Miriam died there and was BURIED there" — Deborah\'s (Gen 35:8) and Rachel\'s (35:19) formula')
        move('Moed Katan 28a:2', 'buried near where she died; a woman\'s bier not set down in the street (R. Elazar)')
        return out('buried near the death — the woman\'s bier not set down in the street (Moed Katan 28a)', ['buried'])
    if ask == 'there_there':
        ink('20:1', '"died THERE" — with Deut 21:4\'s "there" (the eglah arufah)')
        move('Avodah Zarah 29b:12; Sanhedrin 47b:17', 'benefit from a corpse forbidden by the analogy; Abaye: by designation')
        return out('benefit from a corpse forbidden — "there" / "there" with the eglah arufah (Avodah Zarah 29b; Sanhedrin 47b)', [FX.NONE])
    if ask == 'astrologers':
        ink('20:13', '"THESE are the waters of Meribah"')
        move('Sanhedrin 101b:10; Sotah 12b:14', "the waters Pharaoh's astrologers saw and erred on — the savior stricken by water: Meribah, not the Nile")
        return out('the astrologers\' waters — Meribah, not the Nile (Sanhedrin 101b; Sotah 12b)', [FX.NONE])
    if ask == 'quarrel_with_teacher':
        ink('20:13', '"where the children of Israel strove WITH THE LORD" — the quarrel was with Moses')
        move('Sanhedrin 110a:9', 'who quarrels with his teacher quarrels with the Presence (R. Chama b. R. Chanina)')
        return out('a quarrel with the teacher is a quarrel with the Presence (Sanhedrin 110a)', [FX.NONE])
    if ask == 'cattle_water':
        ink('20:8', '"give drink to the congregation AND THEIR CATTLE"')
        move('Menachot 76b:13', 'the Torah spared Israel\'s money — the miracle even for the livestock (R. Elazar)')
        return out('the cattle included — the Torah spared Israel\'s money (Menachot 76b)', ['water_from_the_rock'])
    if ask == 'struck_twice':
        ink('20:11', '"and he struck the rock with his staff TWICE" — the dual read %s by the taught parser (rule 19; Gen 27:36, 41:32, 43:10 its kin %s)' % (TWICE, TWICE_KIN))
        return out('struck twice — [2] by the parser (20:11); much water came out', ['water_from_the_rock'])
    if ask == 'sin':
        ink('20:8, 20:11-12', 'SPEAK commanded (20:8); STRUCK twice done (20:11); "because you did not believe in Me, to sanctify Me" (20:12)')
        dat('the row meribah_sin: %s' % data['meribah_sin']['value'])
        move('Shabbat 55b:2; Yoma 86b:15, 87a:3; Ps 106:32-33', 'even Moses and Aaron died for their sin; Moses asked his disgrace written; "he spoke rashly with his lips"')
        return out('the spec\'s SPEAK, the run\'s STRUCK TWICE — the sin the ink\'s own delta; the rash speech the Psalm\'s (20:8-12; Ps 106:33)', [FX.NONE])
    if ask == 'died_for_sin':
        move('Shabbat 55b:2; Yoma 87a:3', 'R. Shimon b. Elazar: had you believed, your time had not yet come — even Moses and Aaron died for their sin')
        return out('died for their sin — had they believed, their time had not come (Shabbat 55b; Yoma 87a)', ['barred_from_the_land'])
    if ask == 'disgrace_written':
        move('Yoma 86b:15', 'Moses: let my disgrace be written (20:12); David: hidden (Ps 32:1)')
        return out('Moses\' disgrace written explicitly at 20:12 (Yoma 86b)', [FX.NONE])
    if ask == 'sentence':
        ink('20:12', '"therefore you shall not bring this assembly into the land which I have given them" — the frame to Moses AND Aaron; 20:24, 27:14, Deut 32:51 the run citations')
        return out('barred from the land — Moses and Aaron; Aaron\'s closed at 20:28, Moses\' at Deut 34 (20:12)', ['barred_from_the_land'])
    if ask == 'miriam_day':
        ink('20:1', '"in the first month" — the ordinal reader\'s %s; no day, no year in the ink' % FIRST_MONTH)
        dat('the row miriam_death_day: %s' % data['miriam_death_day']['value'])
        return out('the tenth of Nisan (Seder Olam 10:2); the arrival on the new moon (9:2) — the tape\'s marker on the first, the row\'s arm the tenth', [FX.NONE])
    if ask == 'meribah_seats':
        ink('20:13, 20:24, 27:14; Exod 17:7; Deut 32:51, 33:8; Ps 81:8, 95:8, 106:32; Ezek 47:19, 48:28', 'the Meribah-word\'s seats in the five books (computed): %s — Gen 13:8\'s "strife" the named homograph, not counted' % MERIBAH_SEATS)
        return out('Meribah at %d seats — Exod 17:7 the first, Num 20:13 the second (computed)' % len(MERIBAH_SEATS), [FX.NONE])
    if ask == 'first_meribah_clauses':
        ink('20:3, 20:5; Exod 17:2-3', 'the first Meribah\'s clauses at the second (computed): %s — "the people strove", "why did you bring us up from Egypt"' % FIRST_MERIBAH_CLAUSES)
        return out('Exod 17:2-3\'s clauses at Num 20:3-5 — strove, brought up, from Egypt (computed)', ['gathered_against'])
    if ask == 'rebels_skin':
        ink('20:10', '"hear now, you REBELS" — one consonantal skin with Miriam\'s name (20:1) and Marah\'s waters (Exod 15:23), told by the points (the reading\'s crown)')
        return out('the rebels, Miriam and the bitter waters — one consonantal skin, three words (20:10)', [FX.NONE])
    return out('no verdict in span', [FX.NONE])


# ===== F4: EDOM, MOUNT HOR, THE SUCCESSION AND THE MOURNING (Num 20:14-29) ================================
def edom_and_hor(case, data):
    del P[:]
    ask = case['ask']
    if ask == 'arad_heard':
        ink('20:29; 21:1; 33:40', '"and all the congregation SAW that Aaron was dead" — "the Canaanite king of Arad heard"')
        dat('the row arad_heard: %s' % data['arad_heard']['value'])
        return out('Arad heard that Aaron died and the clouds departed (Rosh Hashanah 3a; Taanit 9a) — the attack during the mourning', [FX.NONE])
    if ask == 'death_dates':
        ink('33:38-39', '"in the fortieth year, in the fifth month, on the first of the month" — read whole by the parser: %s; his age %s' % (AARON_DATE, AARON_AGE))
        dat('the rows miriam_death_day: %s; deaths_ceased: %s' % (data['miriam_death_day']['value'], data['deaths_ceased']['value']))
        move('Seder Olam Rabbah 10:2', 'Miriam the tenth of Nisan, Aaron the first of Av, Moses the seventh of Adar — one year, not one month (Zech 11:8)')
        return out('Aaron (40, 5, 1) by the ink, aged 123; Miriam the tenth of Nisan by the shelf; Moses the seventh of Adar (33:38-39; Seder Olam 10:2)', [FX.NONE])
    if ask == 'seder_olam_walk':
        dat('the row moserah: %s' % data['moserah']['value'])
        move('Seder Olam Rabbah 9:2', 'the new moon of Nisan at Zin; three months at Kadesh; Aaron at 123; the clouds departed, Arad came; the retreat of seven stations to Moserah; Gudgod, Beer, Oboth, Iye-abarim, Zered, beyond Arnon, Sihon, Og, Arvot Moab, the plague, the census, the daughters')
        return out('the fortieth year\'s walk: (40, 1, 1) the arrival, three months at Kadesh, Aaron\'s death, the retreat to Moserah, the daughters after the conquest (Seder Olam 9:2)', [FX.NONE])
    if ask == 'moserah':
        ink('20:28; Deut 10:6', '"Aaron died there on the top of the mountain" / "at Moserah there Aaron died" — the DIVERGE')
        dat('the row moserah: %s' % data['moserah']['value'])
        return out('Moserah — the retreat of seven stations after Arad\'s attack, the mourning renewed there (Seder Olam 9:2); the death at Mount Hor (20:28)', [FX.NONE])
    if ask == 'succession':
        ink('20:26, 20:28', '"strip Aaron of his garments and put them on Eleazar his son" — Exod 29:29-30\'s spec RUN')
        dat('the row succession_by: %s' % data['succession_by']['value'])
        move('CALLED cold_run_vestments.investiture(substitute) -> %s; cold_run_priesthood.family(one_hour) -> %s; family(high_priest_dead) -> %s [IMPORT, live]' % (VS_SUBSTITUTE, PR_HOUR, PR_HP_DEAD), "the garments transferable to the son after him; the office attaches at the pouring — here at the dressing; the high priest's mourning rows")
        return out('the garments to Eleazar and the office with them — Exod 29:29-30 run at Mount Hor (20:26-28)', ['garments_transferred', 'invested_office', 'gathered_to_his_people'])
    if ask == 'thirty_days':
        ink('20:29', '"they wept for Aaron thirty days, all the house of Israel" — the parser\'s %s; Moses\' %s at Deut 34:8' % (DAYS30, MOSES_MOURNED))
        dat('the row aaron_mourned_by_all: %s' % data['aaron_mourned_by_all']['value'])
        return out('thirty days\' weeping by all the house of Israel — a timer due (40, 6, 1) (20:29; Deut 34:8 Moses\' thirty)', [FX.NONE])
    if ask == 'edom_passage':
        ink('20:18, 20:20-21', '"you shall not pass through me" twice; "and Israel turned away from him"')
        dat('the row edom_passage: %s' % data['edom_passage']['value'])
        return out('Edom refused twice and Israel turned away (20:18-21); Deut 2:28-29\'s purchase the other arm — DISPUTE', ['refused'])
    if ask == 'two_messages':
        ink('20:17; 21:22', 'the Edom letter\'s request and Sihon\'s — %d shared tokens (computed): %s' % (len(SHARED_MSG), SHARED_MSG))
        return out('thirteen tokens shared between the Edom and Sihon messages (20:17; 21:22 — computed)', [FX.NONE])
    if ask == 'two_mount_hors':
        ink('20:22-27, 21:4, 33:37-41; 34:7-8', 'Mount Hor at the border of Edom (Aaron\'s) and Mount Hor of the northern border — two')
        return out('two Mount Hors — Aaron\'s at Edom\'s border, the northern border\'s (34:7-8)', [FX.NONE])
    if ask == 'aaron_age':
        ink('33:39', '"a hundred and twenty-three years" — %s by the parser' % AARON_AGE)
        return out('Aaron 123 at his death (33:39 — [123])', [FX.NONE])
    if ask == 'firstfruits_clauses':
        ink('20:15-16; Deut 26:6-7', '"the Egyptians did evil to us... and we CRIED to the LORD" — the firstfruits declaration\'s two clauses in the Edom letter (computed: %s; "and we cried" at Deut 26:7 too)' % FIRSTFRUITS)
        return out('the firstfruits declaration\'s clauses in the Edom letter — "and we cried to the LORD" at Num 20:16 and Deut 26:7 alone', ['plea_made'])
    if ask == 'messengers_word':
        ink('20:14, 20:16', '"messengers" (the men) and "a messenger" (the LORD\'s) — one noun; Onkelos ENVOYS for the men, the ANGEL kept')
        return out('one noun, two translations — envoys for Moses\' men, the angel for the LORD\'s (20:14, 20:16)', [FX.NONE])
    return out('no verdict in span', [FX.NONE])


# ===== F5: ARAD, THE VOW, THE SERPENTS AND THE POLE (Num 21:1-9) ==========================================
def arad_and_the_serpent(case, data):
    del P[:]
    ask = case['ask']
    if ask == 'captive_acquired':
        ink('21:1', '"and took some of them captive"')
        dat('the row captive_count: %s' % data['captive_count']['value'])
        move('Gittin 38a:4', 'a gentile acquires a Jew by conquest — an act of possession')
        return out('acquired by conquest — a gentile acquires a Jew by possession (Gittin 38a); the shelf\'s one maidservant', ['taken_captive'])
    if ask == 'vow_form':
        ink('21:2', '"if You will indeed give this people into my hand, I will devote their cities" — Jacob\'s (Gen 28:20) and Jephthah\'s (Judg 11:30) form')
        dat('the row cherem_law: %s' % data['cherem_law']['settings']['vow_form'])
        move('Eruvin 64b:3', 'one who wishes to succeed sanctifies a portion for Heaven')
        return out('the conditional vow — a portion sanctified for success (21:2; Eruvin 64b)', ['cherem_vowed'])
    if ask == 'cherem_law':
        ink('21:3', '"and he devoted them and their cities" — Onkelos DESTROYED')
        dat('the row cherem_law: %s' % data['cherem_law']['value'])
        move('CALLED cold_run_temurah.devote(status) -> %s; devote(person) -> %s [IMPORT, live]' % (TM_DEVOTE, TM_PERSON), "Lev 27:28-29's devotion: most holy, not sold, not redeemed; a person devoted put to death")
        return out('the cherem executed — the devoted not redeemed, the persons put to death (21:3; Lev 27:28-29 by the temurah engine)', ['destroyed'])
    if ask == 'hormah':
        ink('21:3; 14:45', '"and he called the name of the place Hormah" — the proleptic name\'s naming; 14:45\'s use six chapters before (CF9\'s row)')
        return out('Hormah named at 21:3 after its use at 14:45 — the proleptic name closed; Judg 1:17 the second naming', ['hormah_named'])
    if ask == 'turn_back':
        ink('21:4; 14:25', '"they journeyed from Mount Hor by the way of the Red Sea" — 14:25\'s "tomorrow turn and journey by the way of the Red Sea" RUN; Deut 2:1')
        return out('14:25\'s turn-back run at 21:4 — the open debit closed (CF8)', [FX.NONE])
    if ask == 'light_bread':
        ink('21:5', '"our soul loathes the light bread" — the manna (Onkelos: this manna whose food is light)')
        dat('the row manna_absorbed: %s' % data['manna_absorbed']['value'])
        return out('the manna called light — absorbed in the limbs (Yoma 75a); ingrates (Avodah Zarah 5b)', ['confessed'])
    if ask == 'spoke_against':
        ink('21:5', '"and the people spoke against God and against Moses"')
        move('Sanhedrin 110a:10', 'who suspects his teacher suspects the Presence — God and Moses likened (R. Abbahu)')
        return out('against God and against Moses likened — suspecting the teacher (Sanhedrin 110a)', ['confessed'])
    if ask == 'bite_and_burn':
        ink('21:6', '"the FIERY serpents... and they BIT the people" — the burn-word the heifer\'s (19:5); the bite usury\'s verb (Deut 23:20)')
        return out('the fiery serpents — the heifer\'s burn-word, usury\'s bite (21:6)', ['serpents_sent'])
    if ask == 'singular_serpent':
        ink('21:6-7, 21:9', '"the serpents" plural (21:6), "the serpent" singular (21:7, 21:9) — the reading\'s measurement')
        return out('the serpents sent, the serpent removed — plural then singular (21:6-9)', [FX.NONE])
    if ask == 'pole_word':
        ink('21:8-9; Exod 17:15; Num 26:10', '"a POLE" — YHWH-nissi\'s word and Korach\'s sign\'s; Onkelos one Aramaic word (את, "a sign"); Deut 34:7 / 4:42 the homographs "fled" / "to flee"')
        return out('the pole-word — the banner of Exod 17:15 and the sign of 26:10 (21:8-9)', [FX.NONE])
    if ask == 'serpent_property':
        ink('21:8', '"make YOU" — from Moses\' own property')
        dat('the row nehushtan: %s' % data['nehushtan']['value'])
        move('Avodah Zarah 44a:7', 'a person does not render forbidden what is not his — the worshipped serpent no idol by right')
        return out('Moses\' own serpent — not an idol by right, its worship notwithstanding (Avodah Zarah 44a)', ['set_on_the_pole'])
    if ask == 'serpent_heals':
        ink('21:8-9', '"everyone bitten who sees it shall live... he looked at the copper serpent and lived" — the look that killed Lot\'s wife (Gen 19:26)')
        dat('the row serpent_kills_or_heals: %s' % data['serpent_kills_or_heals']['value'])
        move('Mishnah Rosh Hashanah 3:8; Rosh Hashanah 29a:7', 'does the serpent kill or give life? the heart subjected to the Father in heaven — with Moses\' hands at Amalek')
        return out('the serpent neither kills nor heals — the heart subjected to Heaven heals (Mishnah Rosh Hashanah 3:8)', ['healed'])
    if ask == 'nehushtan':
        ink('21:9; 2 Kgs 18:4', 'the object\'s run ends at Hezekiah — "he broke in pieces the copper serpent that Moses had made... and he called it Nehushtan"')
        dat('the row nehushtan: %s' % data['nehushtan']['value'])
        return out('Nehushtan — broken by Hezekiah, the Sages agreed (2 Kgs 18:4; Berakhot 10b; Pesachim 56a)', [FX.NONE])
    return out('no verdict in span', [FX.NONE])


# ===== F6: THE STATIONS, THE WELL, SIHON AND OG (Num 21:10-35) ============================================
def well_and_kings(case, data):
    del P[:]
    ask = case['ask']
    if ask == 'zered_date':
        ink('21:12; Deut 2:14', '"and camped at the brook Zered" — Deut 2:14: "the days we walked from Kadesh-barnea until we crossed the brook Zered were THIRTY-EIGHT years" — the parser\'s %s; the decree\'s due (40, 5, 9) = %s' % (THIRTY_EIGHT, EX0.date(D_DUE38)))
        dat('the row deaths_ceased: %s' % (data['deaths_ceased']['value'],))
        return out('the Zered crossed after the thirty-eight years (Deut 2:14 — [38]); the timer due (40, 5, 9), the dying ceased the fifteenth of Av by the shelf, the crossing after the mourning by the text', [FX.NONE])
    if ask == 'book_of_wars':
        ink('21:14-15', '"therefore it is said in the Book of the Wars of the LORD: Vaheb in Suphah and the brooks of Arnon"')
        move('Bava Batra 14b; Kiddushin 30b:2; Moed Katan 25b:2', 'the book named; Vahev love at the end; the phrase in a eulogy')
        return out('the Book of the Wars of the LORD cited — the unnamed book\'s one citation (21:14)', [FX.NONE])
    if ask == 'arnon_miracle':
        dat('the row arnon_miracle: %s' % data['arnon_miracle']['value'])
        return out('the mountains met over the Emorites, the blood ran to the Arnon, the lepers saw and Israel sang (Berakhot 54a-b)', [FX.NONE])
    if ask == 'then_sang':
        ink('21:17; Exod 15:1', '"THEN SANG Israel this song" — the sea\'s formula at its second seat (computed: %s); "answer it" Miriam\'s verb (15:21)' % [('%s %d:%d' % k) for k in THEN_SANG])
        return out('"then sang" at two seats — the sea and the well (Exod 15:1; Num 21:17)', ['well_given'])
    if ask == 'lawgiver':
        ink('21:18; Gen 49:10; Deut 33:21', '"with the LAWGIVER, with their staffs" — Judah\'s word (Onkelos SCRIBES at both): %s' % LAWGIVER)
        return out('the lawgiver — Judah\'s word at Gen 49:10, the well\'s at 21:18, Gad\'s at Deut 33:21 (Onkelos: the scribes)', [FX.NONE])
    if ask == 'well_mouth':
        move('Mishnah Avot 5:6', 'the mouth of the well the second of the ten created at twilight')
        return out('the well\'s mouth created at twilight — the second of the ten (Avot 5:6)', [FX.NONE])
    if ask == 'mattanah_reading':
        ink('21:18-20', '"from the wilderness Mattanah, from Mattanah Nahaliel, from Nahaliel Bamoth, from Bamoth the valley... Pisgah" — Mattanah 18:6-7\'s gift-word')
        dat('the row well_song_reading: %s' % data['well_song_reading']['value'])
        return out('the stations as the Torah\'s ladder — the gift, the inheritance, the heights, the valley (Nedarim 55a; Eruvin 54a)', [FX.NONE])
    if ask == 'from_his_hand':
        ink('21:26', '"and taken all his land FROM HIS HAND as far as Arnon"')
        move('Bava Metzia 56b:4, 56b:7', "'his hand' here means his possession — the one seat where it cannot be the hand")
        return out('"from his hand" = from his possession (Bava Metzia 56b)', [FX.NONE])
    if ask == 'sihon_purified':
        ink('21:26', '"Heshbon was the city of Sihon who had fought against the former king of Moab and taken all his land" — the apparently needless verse')
        dat('the row sihon_purified: %s' % data['sihon_purified']['value'])
        return out('Ammon and Moab purified through Sihon — Israel\'s title by his conquest (Chullin 60b; Deut 2:9)', ['land_possessed'])
    if ask == 'parable_tellers':
        ink('21:27', '"therefore the PARABLE-TELLERS say" — Balaam\'s word (23:7 and after); the hapax')
        dat('the row parable_tellers: %s' % data['parable_tellers']['value'])
        return out('the parable-tellers — Balaam and Beor (Chullin 60b); the homily on the inclination (Bava Batra 78b)', [FX.NONE])
    if ask == 'jeremiah_quote':
        ink('21:28; Jer 48:45', 'Jeremiah quotes the song — the shared tokens (computed): %s' % sorted(JER))
        return out('Jeremiah 48:45-46 quotes 21:28-29 — the parable-tellers\' song in the prophet (computed)', [FX.NONE])
    if ask == 'ammon_border':
        ink('21:24', '"for the border of the sons of Ammon was STRONG"')
        dat('the row ammon_border: %s' % data['ammon_border']['value'])
        return out('Ammon\'s border strong here, commanded off-limits at Deut 2:19, 2:37', [FX.NONE])
    if ask == 'land_east':
        ink('21:24-25, 21:31-32, 21:35', '"and possessed his land from Arnon to Jabbok... Heshbon and its daughters... Jazer... and they possessed his land" — the land east of the Jordan')
        return out('the land east of the Jordan possessed — Sihon\'s from Arnon to Jabbok, Jazer, Og\'s Bashan (21:24-35); chapter 32\'s status', ['land_possessed', 'kings_smitten'])
    if ask == 'spy_verb':
        dat('the row spy_verb: %s' % data['spy_verb']['value'])
        return out('"to spy out Jazer" — Caleb\'s verb (Josh 14:7), not the spies\' "tour" (13:2)', [FX.NONE])
    if ask == 'og_lore':
        ink('21:33-35; Deut 3:11', '"Og king of Bashan came out against them" — his bed %s by the parser' % OG_BED)
        dat('the row og_lore: %s' % data['og_lore']['value'])
        return out('Og — Sihon\'s brother of the Rephaim, the flood\'s survivor by the lore; his bed nine by four (Deut 3:11)', ['fear_not_promised'])
    if ask == 'deut3_delta':
        ink('21:33-35; Deut 3:1-3', 'the retelling with the pronouns shifted (computed): %s / %s; one token at 3:2 (%s / %s)' % (D33[0], D33[1], D34[0], D34[1]))
        return out('Deuteronomy 3:1-3 = 21:33-35 with the pronouns shifted — we for they, "to me" for "to Moses" (computed)', [FX.NONE])
    if ask == 'joshua_refrain':
        ink('21:35', '"until no survivor was left to him" — the refrain\'s seats (computed): %s' % SURVIVOR)
        return out('"until no survivor was left" — born at 21:35, Joshua\'s refrain (8:22, 10:33), 2 Kgs 10:11', ['kings_smitten'])
    if ask == 'sihon_refused':
        ink('21:23', '"and Sihon did not let Israel pass through his border" — Deut 2:30\'s hardening; Judg 11:20\'s distrust')
        return out('Sihon refused the passage and came to Jahaz — hardened (Deut 2:30)', ['refused'])
    return out('no verdict in span', [FX.NONE])


# ---- THE WRAP — the daemon, the scene, the narrative ------------------------------------------------------
def law_chukat(event, world):
    """Num 19:1-21:35 (cold_run_chukat.py F1-F6). installed_by boot — the heifer's statute spoken at 19:1 with no installing act on the
    tape (the standing setting); the lines of chapters 20-21 are acts in the fortieth year. ONE timer: the thirty days' weeping (20:29,
    due the day + 30 = (40, 6, 1) on the tape). SIX closes, all the daemon's own (THE TENT sitting 1: a daemon's close is not a tape
    line): the rock's debit (20:11), the ascent's (20:27), Aaron's block (20:28), the cherem (21:3), the turn-back of 14:25 (21:4 —
    law_shelach's entry, closed here on the tape; on this runner's own world the close finds no entry and returns False), the pole's
    (21:9). The exam's six case kinds dispatch to the cells with LITERAL effects per kind (2b's form — an unnamed effect is a KeyError)."""
    k, src = event['kind'], event['case_source']
    E_ = lambda eff, s, cp=None, amount=None, due=None, law='', value=None: {'effect': eff, 'subject': s, 'counterparty': cp, 'amount': amount, 'due': due, 'value': value if value is not None else True, 'source_law': law, 'case_source': src}
    C_ = lambda ev: {f: ev[f] for f in ('ask', 'burden', 'passed', 'third', 'seventh', 'intent', 'covered') if f in ev}   # the case's own fields to the cell (no field named kind or day)
    day = event.get('day', world.clock.day)      # THE SEQUENTIAL RUN: the event's own day
    # ---- chapter 19: the statute (one line, page_order at the running counter) ----
    if k == 'heifer_statute_given':
        return [E_('commanded', 'israel', value='the_red_heifer', law='F1 [INK 19:1-10 "speak to the children of Israel that they take to you a red heifer, whole, in which there is no blemish, upon which never came a yoke; and you shall give it to Eleazar the priest" — the debit on Israel; OPEN on this tape: the ink never narrates the first burning (the row nine_heifers — Parah 3:5 the shelf\'s run)]')]
    # ---- chapter 20: Kadesh (the first marker), Meribah, Edom, Mount Hor ----
    if k == 'miriam_died_at_kadesh':
        return [E_('buried', 'miriam', value='and Miriam died there and was buried there (20:1) — Kadesh in the wilderness of Zin; the tenth of Nisan by the shelf (the row miriam_death_day), the arrival\'s day on the tape (CM5\'s nine days)', law='F3 [INK 20:1; Moed Katan 28a:2; Seder Olam 10:2]'),
                E_('encamped_at', 'israel', value='Kadesh, the wilderness of Zin — in the first month (20:1; the ordinal reader\'s [1]; Seder Olam 9:2: the new moon of Nisan of the fortieth year, the well removed)', law='F3 [INK 20:1; Seder Olam 9:2]')]
    if k == 'congregation_strove_for_water':
        return [E_('gathered_against', 'israel', cp='moses-and-aaron', value='there was no water for the congregation; they gathered against Moses and against Aaron; the people strove with Moses: would that we had expired... why have you brought us up from Egypt (20:2-5) — the first Meribah\'s clauses at the second (Exod 17:2-3, computed)', law='F3 [INK 20:2-5; Exod 17:2-3]')]
    if k == 'moses_and_aaron_fell_and_the_glory':
        return [E_('glory_appeared', 'the-tabernacle', cp='HEAVEN', value='Moses and Aaron came from before the assembly to the entrance of the tent of meeting and fell on their faces, and the glory of the LORD appeared to them (20:6) — the formula\'s fifth seat (Lev 9:23; Num 14:10, 16:19, 17:7)', law='F3 [INK 20:6]')]
    if k == 'rock_commanded':
        return [E_('commanded', 'moses', value='the_rock', law='F3 [INK 20:7-8 "take the staff and assemble the congregation, you and Aaron your brother, and SPEAK to the rock before their eyes, and it shall give its water" — the debit on Moses: the spec\'s verb SPEAK; CLOSED by 20:11\'s strike, the run\'s verb (CM6)]')]
    if k == 'staff_taken_from_before_the_lord':
        return []                                  # the object row read (20:9): "the staff from before the LORD" — Aaron's kept staff (17:25); the words are the line's value
    if k == 'rock_struck_twice':
        world.close('moses', 'commanded', 'Num 20:11 — and Moses lifted his hand and STRUCK the rock with his staff TWICE (the parser\'s [2]) — the run\'s verb against the spec\'s SPEAK (CM6)', value='the_rock')
        return [E_('water_from_the_rock', 'israel', amount=TWICE[0], value='hear now, you rebels: shall we bring you water out of this rock? (20:10); much water came out and the congregation drank, and their cattle (20:11) — struck twice', law='F3 [INK 20:10-11 — rule (19) the dual "twice"; Menachot 76b:13 the cattle]')]
    if k == 'sentence_at_meribah':
        return [E_('barred_from_the_land', 'moses', cp='HEAVEN', value='because you did not believe in Me, to sanctify Me before the eyes of the children of Israel, therefore you shall not bring this assembly into the land which I have given them (20:12) — OPEN: its close at Deut 34', law='F3 [INK 20:12-13; Shabbat 55b:2; Yoma 87a:3]'),
                E_('barred_from_the_land', 'aaron', cp='HEAVEN', value='the same sentence — the frame to Moses AND Aaron (20:12); restated at 20:24; CLOSED by 20:28', law='F3 [INK 20:12, 20:24]')]
    if k == 'messengers_sent_to_edom':
        return [E_('plea_made', 'israel', cp='edom', value='thus says your brother Israel: you know all the hardship... the Egyptians did evil to us and we cried to the LORD... let us pass through your land; we will not pass through field or vineyard nor drink well water; by the king\'s highway (20:14-17) — the firstfruits declaration\'s clauses (Deut 26:6-7, computed)', law='F4 [INK 20:14-17; Deut 26:6-7]')]
    if k == 'edom_refused':
        return [E_('refused', 'edom', cp='israel', value='you shall not pass through me, lest I come out against you with the sword (20:18)', law='F4 [INK 20:18]')]
    if k == 'israel_pleaded_the_highway':
        return [E_('plea_made', 'israel', cp='edom', value='we will go up by the highway; if we drink your water, I and my cattle, I will pay its price; only on foot, nothing more (20:19)', law='F4 [INK 20:19]')]
    if k == 'edom_came_out_against':
        return [E_('refused', 'edom', cp='israel', value='you shall not pass; and Edom came out against him with much people and with a strong hand; and Israel turned away from him (20:20-21) — the row edom_passage: Deut 2:28-29\'s purchase the other arm', law='F4 [INK 20:20-21; Deut 2:4-8, 2:28-29]')]
    if k == 'journeyed_to_mount_hor':
        return [E_('encamped_at', 'israel', value='Mount Hor, by the border of the land of Edom (20:22-23) — from Kadesh, all the congregation; three months at Kadesh by the shelf (Seder Olam 9:2 — the second marker)', law='F4 [INK 20:22; Seder Olam 9:2]')]
    if k == 'aarons_gathering_decreed':
        return [E_('commanded', 'moses', value='bring_aaron_up_mount_hor', law='F4 [INK 20:23-26 "Aaron shall be gathered to his people... because you rebelled against My word at the waters of Meribah; take Aaron and Eleazar his son and bring them up Mount Hor; strip Aaron of his garments and put them on Eleazar his son; and Aaron shall be gathered and die there" — the debit on Moses; CLOSED by 20:27]')]
    if k == 'aaron_brought_up_mount_hor':
        world.close('moses', 'commanded', 'Num 20:27 — and Moses did as the LORD commanded, and they went up Mount Hor before the eyes of all the congregation', value='bring_aaron_up_mount_hor')
        return []
    if k == 'garments_transferred_and_aaron_died':
        world.close('aaron', 'barred_from_the_land', 'Num 20:28 — and Aaron died there on the top of the mountain: the block run to its end (33:38 the date, 33:39 the age)')
        return [E_('garments_transferred', 'aaron', cp='eleazar', value='Moses stripped Aaron of his garments and put them on Eleazar his son (20:28) — Exod 29:29-30\'s spec RUN; the vestments engine\'s cell: %s' % VS_SUBSTITUTE, law='F4 [INK 20:26, 20:28; Exod 29:29-30]'),
                E_('invested_office', 'eleazar', value='the office with the garments (20:28) — the many-garmented priest (Horayot 12a); the priesthood engine\'s hour: %s' % PR_HOUR, law='F4 [INK 20:28; Exod 29:29-30; the priesthood engine\'s row one_hour]'),
                E_('gathered_to_his_people', 'aaron', cp='HEAVEN', value='and Aaron died there on the top of the mountain (20:28) — in the fortieth year, the fifth month, the first of the month, aged a hundred and twenty-three (33:38-39: the parser\'s %s, %s)' % (AARON_DATE, AARON_AGE), law='F4 [INK 20:28; 33:38-39; Seder Olam 10:2]')]
    if k == 'aaron_mourned_thirty_days':
        return [E_('mourned_thirty_days', 'israel', due=day + DAYS30[0], value='and all the congregation saw that Aaron had expired, and they wept for Aaron thirty days, all the house of Israel (20:29) — the men and the women; the TIMER due the thirtieth day: (40, 6, 1) on the tape (CM4)', law='F4 [INK 20:29 — the parser\'s [30]; Deut 34:8 Moses\' thirty]')]
    # ---- chapter 21: Arad during the mourning, the serpents, the stations, the well, the two kings ----
    if k == 'arad_fought_and_took_captives':
        return [E_('taken_captive', 'israel', cp='the-king-of-arad', value='the Canaanite king of Arad, who dwelt in the Negev, heard that Israel came by the way of Atharim; he fought against Israel and took some of them captive (21:1) — during the mourning (Rosh Hashanah 3a: he heard that Aaron died); the shelf\'s one maidservant (the row captive_count)', law='F5 [INK 21:1; 33:40; Rosh Hashanah 3a:1; Gittin 38a:4]')]
    if k == 'israel_vowed_the_cherem':
        return [E_('cherem_vowed', 'israel', cp='HEAVEN', value='if You will indeed give this people into my hand, I will devote their cities (21:2) — the conditional vow (Gen 28:20; Judg 11:30); CLOSED by 21:3', law='F5 [INK 21:2; Eruvin 64b:3]')]
    if k == 'canaanites_devoted_hormah_named':
        world.close('israel', 'cherem_vowed', 'Num 21:3 — and the LORD heard the voice of Israel and gave the Canaanite, and he devoted them and their cities')
        return [E_('destroyed', 'the-king-of-arad', cp='israel', value='he devoted them and their cities (21:3) — Onkelos DESTROYED; the temurah engine\'s devotion: %s' % TM_DEVOTE, law='F5 [INK 21:3; Lev 27:28-29]'),
                E_('hormah_named', 'hormah', value='and he called the name of the place Hormah (21:3) — the proleptic name of 14:45 closed (CF9); Judg 1:17 the second naming', law='F5 [INK 21:3; 14:45]')]
    if k == 'journeyed_by_the_red_sea_way':
        world.close('israel', 'commanded', 'Num 21:4 — and they journeyed from Mount Hor by the way of the Red Sea to go around the land of Edom: 14:25\'s "turn and journey by the way of the Red Sea" RUN (CF8)', value='the_turn_back')
        return [E_('encamped_at', 'israel', value='from Mount Hor by the way of the Red Sea, to go around the land of Edom; and the soul of the people was shortened on the way (21:4) — after the thirty days (the fourth marker: Aaron\'s death + 30)', law='F5 [INK 21:4; 14:25; Deut 2:1]')]
    if k == 'people_spoke_against_god_and_moses':
        return [E_('spoke_against_god_and_moses', 'israel', value='why have you brought us up from Egypt to die in the wilderness? there is no bread and no water, and our soul loathes the light bread (21:5) — the manna (the row manna_absorbed)', law='F5 [INK 21:5; Sanhedrin 110a:10; Yoma 75a]')]
    if k == 'fiery_serpents_sent':
        return [E_('serpents_sent', 'israel', cp='HEAVEN', value='the LORD sent among the people the fiery serpents, and they bit the people, and many people of Israel died (21:6) — the burn-word the heifer\'s (19:5), the bite usury\'s (Deut 23:20)', law='F5 [INK 21:6]')]
    if k == 'people_confessed_and_moses_prayed':
        return [E_('confessed', 'israel', value='we have sinned, for we spoke against the LORD and against you; pray to the LORD that He remove the serpent from us (21:7) — the serpent singular', law='F5 [INK 21:7]'),
                E_('plea_made', 'moses', cp='HEAVEN', value='and Moses prayed for the people (21:7)', law='F5 [INK 21:7]')]
    if k == 'pole_commanded':
        return [E_('commanded', 'moses', value='the_serpent_on_a_pole', law='F5 [INK 21:8 "make YOU a fiery one and set it on a pole; and everyone bitten who sees it shall live" — the debit on Moses; CLOSED by 21:9]')]
    if k == 'copper_serpent_made':
        world.close('moses', 'commanded', 'Num 21:9 — and Moses made a serpent of copper and set it on the pole', value='the_serpent_on_a_pole')
        return [E_('set_on_the_pole', 'the-copper-serpent', value='a serpent of copper on the pole (21:9) — from Moses\' own (Avodah Zarah 44a); its run ends at 2 Kgs 18:4, Nehushtan (the row nehushtan)', law='F5 [INK 21:9; 2 Kgs 18:4]'),
                E_('healed', 'israel', cp='HEAVEN', value='if the serpent bit a man and he looked at the copper serpent, he lived (21:9) — the heart subjected to Heaven (Mishnah Rosh Hashanah 3:8; the row serpent_kills_or_heals)', law='F5 [INK 21:9; Mishnah Rosh Hashanah 3:8]')]
    if k == 'journeyed_oboth_to_arnon':
        return [E_('encamped_at', 'israel', value='Oboth; Iye-abarim in the wilderness before Moab toward the sunrise; the brook Zered; beyond Arnon in the wilderness at the Amorite\'s border (21:10-13) — the Zered after the thirty-eight years (Deut 2:14 — [38])', law='F6 [INK 21:10-13; Deut 2:13-14]')]
    if k == 'book_of_the_wars_cited':
        return []                                  # the citation the value (21:14-15): "therefore it is said in the Book of the Wars of the LORD: Vaheb in Suphah and the brooks of Arnon"
    if k == 'well_given_at_beer':
        return [E_('well_given', 'israel', cp='HEAVEN', value='Beer — the well of which the LORD said to Moses: assemble the people and I will give them water; then sang Israel this song: rise up, O well (21:16-18) — the second "then sang" (Exod 15:1, computed); the lawgiver\'s word (Gen 49:10)', law='F6 [INK 21:16-18; Exod 15:1; Gen 49:10]')]
    if k == 'journeyed_to_pisgah':
        return [E_('encamped_at', 'israel', value='from the wilderness Mattanah, Nahaliel, Bamoth, the valley in the field of Moab, the top of Pisgah looking over the wasteland (21:18-20)', law='F6 [INK 21:19-20]')]
    if k == 'messengers_sent_to_sihon':
        return [E_('plea_made', 'israel', cp='sihon', value='let me pass through your land; we will not turn into field or vineyard, nor drink well water; by the king\'s highway until we pass your border (21:21-22) — thirteen tokens shared with the Edom letter (computed)', law='F6 [INK 21:21-22; 20:17]')]
    if k == 'sihon_came_out_and_fought':
        return [E_('refused', 'sihon', cp='israel', value='Sihon did not let Israel pass through his border; he gathered all his people and came out against Israel to the wilderness, to Jahaz, and fought against Israel (21:23) — hardened (Deut 2:30)', law='F6 [INK 21:23; Deut 2:30]')]
    if k == 'sihon_smitten_land_possessed':
        return [E_('kings_smitten', 'sihon', cp='israel', value='Israel smote him with the edge of the sword (21:24)', law='F6 [INK 21:24]'),
                E_('land_possessed', 'israel', value='his land from Arnon to Jabbok, as far as the sons of Ammon — for the border of the sons of Ammon was strong; all these cities, Heshbon and all its daughters (21:24-25)', law='F6 [INK 21:24-25; Deut 2:19, 2:37]')]
    if k == 'heshbon_and_the_parable':
        return []                                  # the history and the parable the value (21:26-30): Sihon's war on Moab's former king; the parable-tellers' song (Jer 48:45-46 quotes it)
    if k == 'israel_dwelt_and_jazer_taken':
        return [E_('land_possessed', 'israel', value='Israel dwelt in the land of the Amorite; Moses sent to spy out Jazer, and they took its daughters and dispossessed the Amorite there (21:31-32) — Caleb\'s spy-verb (Josh 14:7)', law='F6 [INK 21:31-32; Josh 14:7]')]
    if k == 'og_came_out_and_fear_not':
        return [E_('fear_not_promised', 'moses', cp='HEAVEN', value='do not fear him, for into your hand I have given him and all his people and his land; you shall do to him as you did to Sihon (21:34) — Og came out to Edrei (21:33)', law='F6 [INK 21:33-34; Deut 3:1-2]')]
    if k == 'og_smitten':
        return [E_('kings_smitten', 'og', cp='israel', value='they smote him and his sons and all his people until no survivor was left to him (21:35) — Joshua\'s refrain born (Josh 8:22, 10:33; computed)', law='F6 [INK 21:35; Deut 3:3]'),
                E_('land_possessed', 'israel', value='and they possessed his land (21:35) — Bashan; the land east of the Jordan whole: Sihon\'s, the Amorite\'s and Jazer, Og\'s (CM10)', law='F6 [INK 21:35; Deut 3:1-11]')]
    # ---- the exam's case kinds: each names LITERALLY every effect it can write (2b's form — an unnamed effect is a KeyError to read) ----
    if k == 'heifer_case':
        v, e, _ = heifer_rite(C_(event), DATA); L = 'F1 [%s]' % v; s_ = event['person']
        W = {'accepted': E_('accepted', s_, value=v, law=L), 'disqualified': E_('disqualified', s_, value=v, law=L), 'exempt': E_('exempt', s_, value=v, law=L), 'impure_until_evening': E_('impure_until_evening', s_, value=v, law=L),
             'ashes_kept_for_niddah_water': E_('ashes_kept_for_niddah_water', s_, value=v, law=L), 'sprinkled_seven': E_('sprinkled_seven', s_, amount=SEVEN[0], value=v, law=L), 'pays': E_('pays', s_, cp='the-priest', value=v, law=L)}
        return [W[x] for x in e if x != FX.NONE]
    if k == 'corpse_tumah_case':
        v, e, _ = corpse_tumah(C_(event), DATA); L = 'F2 [%s]' % v; s_ = event['person']
        W = {'accepted': E_('accepted', s_, value=v, law=L), 'disqualified': E_('disqualified', s_, value=v, law=L), 'exempt': E_('exempt', s_, value=v, law=L),
             'corpse_unclean_seven_days': E_('corpse_unclean_seven_days', s_, amount=SEVENS[0][0], due=day + SEVENS[0][0], value=v, law=L),               # the TIMERS: the machine counts the days that pass (3b's inclusive-count lesson recorded, never absorbed)
             'sprinkling_due_third_day': E_('sprinkling_due_third_day', s_, due=day + SCHEDULE[0], value=v, law=L), 'sprinkling_due_seventh_day': E_('sprinkling_due_seventh_day', s_, due=day + SCHEDULE[1], value=v, law=L),
             'not_purified': E_('not_purified', s_, value=v, law=L), 'declared_pure': E_('declared_pure', s_, value=v, law=L), 'impure_until_evening': E_('impure_until_evening', s_, value=v, law=L), 'tent_unclean': E_('tent_unclean', s_, value=v, law=L),
             'open_vessel_unclean': E_('open_vessel_unclean', s_, value=v, law=L), 'karet_cut_off': E_('karet_cut_off', s_, cp='HEAVEN', value=v, law=L), 'sent_outside_the_camp': E_('sent_outside_the_camp', s_, value=v, law=L),
             'washes_and_bathes': E_('washes_and_bathes', s_, value=v, law=L), 'lashes': E_('lashes', s_, value=v, law=L)}
        return [W[x] for x in e if x != FX.NONE]
    if k == 'meribah_case':
        v, e, _ = meribah(C_(event), DATA); L = 'F3 [%s]' % v; s_ = event['person']
        W = {'accepted': E_('accepted', s_, value=v, law=L), 'exempt': E_('exempt', s_, value=v, law=L), 'water_from_the_rock': E_('water_from_the_rock', s_, value=v, law=L), 'barred_from_the_land': E_('barred_from_the_land', s_, cp='HEAVEN', value=v, law=L),
             'buried': E_('buried', s_, value=v, law=L), 'gathered_against': E_('gathered_against', s_, cp='moses-and-aaron', value=v, law=L)}
        return [W[x] for x in e if x != FX.NONE]
    if k == 'edom_hor_case':
        v, e, _ = edom_and_hor(C_(event), DATA); L = 'F4 [%s]' % v; s_ = event['person']
        W = {'accepted': E_('accepted', s_, value=v, law=L), 'exempt': E_('exempt', s_, value=v, law=L), 'refused': E_('refused', s_, value=v, law=L), 'garments_transferred': E_('garments_transferred', s_, cp='eleazar', value=v, law=L),
             'invested_office': E_('invested_office', s_, value=v, law=L), 'gathered_to_his_people': E_('gathered_to_his_people', s_, cp='HEAVEN', value=v, law=L), 'plea_made': E_('plea_made', s_, value=v, law=L)}
        return [W[x] for x in e if x != FX.NONE]
    if k == 'arad_serpent_case':
        v, e, _ = arad_and_the_serpent(C_(event), DATA); L = 'F5 [%s]' % v; s_ = event['person']
        W = {'accepted': E_('accepted', s_, value=v, law=L), 'exempt': E_('exempt', s_, value=v, law=L), 'taken_captive': E_('taken_captive', s_, cp='the-king-of-arad', value=v, law=L), 'cherem_vowed': E_('cherem_vowed', s_, cp='HEAVEN', value=v, law=L),
             'destroyed': E_('destroyed', s_, value=v, law=L), 'hormah_named': E_('hormah_named', s_, value=v, law=L), 'serpents_sent': E_('serpents_sent', s_, cp='HEAVEN', value=v, law=L), 'healed': E_('healed', s_, cp='HEAVEN', value=v, law=L),
             'set_on_the_pole': E_('set_on_the_pole', s_, value=v, law=L), 'confessed': E_('confessed', s_, value=v, law=L)}
        return [W[x] for x in e if x != FX.NONE]
    if k == 'well_kings_case':
        v, e, _ = well_and_kings(C_(event), DATA); L = 'F6 [%s]' % v; s_ = event['person']
        W = {'accepted': E_('accepted', s_, value=v, law=L), 'exempt': E_('exempt', s_, value=v, law=L), 'well_given': E_('well_given', s_, cp='HEAVEN', value=v, law=L), 'land_possessed': E_('land_possessed', s_, value=v, law=L),
             'kings_smitten': E_('kings_smitten', s_, value=v, law=L), 'fear_not_promised': E_('fear_not_promised', s_, cp='HEAVEN', value=v, law=L), 'refused': E_('refused', s_, value=v, law=L)}
        return [W[x] for x in e if x != FX.NONE]
    return []


def scene():
    """THE SCENE — the exam's rows replayed on the world engine (the exodus epoch): the yoked heifer, the tevul yom who burns, the gatherer,
    the trespasser, the seven sprinklings, the burner's garments; the toucher's third and seventh as TIMERS and the omitter's failure, the
    intentional enterer's karet, the high priest, the tent, the open vessel, the gentile, the carrier, the camp; the cattle at the rock,
    the sentence, the bier; the succession, Edom; the captive, the vow, the cherem, the bitten, Hormah; the well's song, the land east,
    Og, Sihon. A closing walk of seven days fires the timers (a timer's setting is not a write — 4b's lesson)."""
    with contextlib.redirect_stdout(io.StringIO()):
        w = WE.World(era='Num 19-21: Mishnah Parah, Oholot, Kelim, Mikvaot, Shevuot, Rosh Hashanah 3:8 and the Talmud\'s rows on the engine (the exodus epoch)', epoch='exodus')
        w.laws = [law_chukat]
        w.advance(w.clock.day_in('exodus', 2, 5, 9))
        d0 = w.clock.day
        w.submit({'kind': 'heifer_case', 'subject': 'the-yoked-heifer', 'person': 'the-yoked-heifer', 'ask': 'yoke', 'burden': 'sacks', 'case_source': 'Sotah 46a:11; Avodah Zarah 23a:6; Num 19:2 — a bundle of sacks placed on it'})
        w.submit({'kind': 'heifer_case', 'subject': 'the-tevul-yom-burner', 'person': 'the-tevul-yom-burner', 'ask': 'tvul_yom', 'case_source': 'Mishnah Parah 3:7; Yoma 43b:3; Num 19:19 — the burner defiled on purpose'})
        w.submit({'kind': 'heifer_case', 'subject': 'the-gatherer', 'person': 'the-gatherer', 'ask': 'gatherer', 'case_source': 'Yoma 43a:7; Yevamot 72b:16; Num 19:9 — a man who is pure shall gather'})
        w.submit({'kind': 'heifer_case', 'subject': 'the-trespasser', 'person': 'the-trespasser', 'ask': 'meilah', 'case_source': 'Menachot 51b:22; Mishnah Parah 4:4; Num 19:9 — it is a sin offering (the Lev 5 engine called)'})
        w.submit({'kind': 'heifer_case', 'subject': 'the-sprinkling-priest', 'person': 'the-sprinkling-priest', 'ask': 'sprinkling', 'case_source': 'Mishnah Parah 3:9; Menachot 27a:14; Num 19:4 — seven times toward the entrance'})
        w.submit({'kind': 'heifer_case', 'subject': 'the-burner', 'person': 'the-burner', 'ask': 'defiles_garments', 'case_source': 'Mishnah Parah 4:4, 8:3; Num 19:7-8 — the rite defiles its servants'})
        w.submit({'kind': 'corpse_tumah_case', 'subject': 'the-toucher', 'person': 'the-toucher', 'ask': 'schedule', 'third': True, 'seventh': True, 'case_source': 'Kiddushin 62a:4; Num 19:12 — the third and the seventh (the timers)'})
        w.submit({'kind': 'corpse_tumah_case', 'subject': 'the-omitter', 'person': 'the-omitter', 'ask': 'schedule', 'third': True, 'seventh': False, 'case_source': 'Sifrei Bamidbar 125; Num 19:12b — the seventh omitted'})
        w.submit({'kind': 'corpse_tumah_case', 'subject': 'the-enterer', 'person': 'the-enterer', 'ask': 'karet_entry', 'intent': 'intentional', 'case_source': 'Makkot 14b:6; Mishnah Keritot 1:1; Num 19:13, 19:20 — the impure who entered'})
        w.submit({'kind': 'corpse_tumah_case', 'subject': 'the-high-priest', 'person': 'the-high-priest', 'ask': 'high_priest_exempt', 'case_source': 'Horayot 9b:3; Mishnah Parah 12:4; Num 19:20 — from the midst of the congregation'})
        w.submit({'kind': 'corpse_tumah_case', 'subject': 'the-tent-dweller', 'person': 'the-tent-dweller', 'ask': 'tent', 'case_source': 'Mishnah Oholot 3:6; Num 19:14 — everyone who comes into the tent'})
        w.submit({'kind': 'corpse_tumah_case', 'subject': 'the-open-vessel', 'person': 'the-open-vessel', 'ask': 'open_vessel', 'covered': False, 'case_source': 'Mishnah Kelim 10:1; Chullin 25a:3; Num 19:15 — no cord-bound cover'})
        w.submit({'kind': 'corpse_tumah_case', 'subject': 'the-gentile', 'person': 'the-gentile', 'ask': 'gentile_no_tumah', 'case_source': 'Nazir 61b:1; Num 19:20 — cut off from the midst of the assembly'})
        w.submit({'kind': 'corpse_tumah_case', 'subject': 'the-carrier', 'person': 'the-carrier', 'ask': 'sprinkler_carrier', 'case_source': 'Yoma 14a:9; Mishnah Parah 12:5; Num 19:21 — he who sprinkles read as he who carries'})
        w.submit({'kind': 'corpse_tumah_case', 'subject': 'the-unclean-at-the-camp', 'person': 'the-unclean-at-the-camp', 'ask': 'camps', 'case_source': 'Mishnah Kelim 1:8; Num 5:2 — the corpse-impure at the chel (naso\'s paid edge)'})
        w.submit({'kind': 'meribah_case', 'subject': 'the-cattle', 'person': 'the-cattle', 'ask': 'cattle_water', 'case_source': 'Menachot 76b:13; Num 20:8 — and their cattle'})
        w.submit({'kind': 'meribah_case', 'subject': 'the-sentenced', 'person': 'the-sentenced', 'ask': 'died_for_sin', 'case_source': 'Shabbat 55b:2; Yoma 87a:3; Num 20:12 — had you believed'})
        w.submit({'kind': 'meribah_case', 'subject': 'the-bier', 'person': 'the-bier', 'ask': 'burial_near_death', 'case_source': 'Moed Katan 28a:2; Num 20:1 — died there and was buried there'})
        w.submit({'kind': 'edom_hor_case', 'subject': 'the-successor', 'person': 'the-successor', 'ask': 'succession', 'case_source': 'Horayot 12a; Num 20:28 — the garments to Eleazar (the vestments engine called)'})
        w.submit({'kind': 'edom_hor_case', 'subject': 'the-refuser', 'person': 'the-refuser', 'ask': 'edom_passage', 'case_source': 'Onkelos Num 20:18-21; Deut 2:28-29 — you shall not pass (the DISPUTE row)'})
        w.submit({'kind': 'arad_serpent_case', 'subject': 'the-captive', 'person': 'the-captive', 'ask': 'captive_acquired', 'case_source': 'Gittin 38a:4; Num 21:1 — took some of them captive'})
        w.submit({'kind': 'arad_serpent_case', 'subject': 'the-vower', 'person': 'the-vower', 'ask': 'vow_form', 'case_source': 'Eruvin 64b:3; Num 21:2 — if You will indeed give'})
        w.submit({'kind': 'arad_serpent_case', 'subject': 'the-devoted', 'person': 'the-devoted', 'ask': 'cherem_law', 'case_source': 'Lev 27:28-29 by the temurah engine; Num 21:3 — he devoted them'})
        w.submit({'kind': 'arad_serpent_case', 'subject': 'the-bitten', 'person': 'the-bitten', 'ask': 'serpent_heals', 'case_source': 'Mishnah Rosh Hashanah 3:8; Num 21:9 — he looked and lived'})
        w.submit({'kind': 'arad_serpent_case', 'subject': 'the-place-hormah', 'person': 'the-place-hormah', 'ask': 'hormah', 'case_source': 'Judg 1:17; Num 21:3 against 14:45 — the proleptic name (CF9)'})
        w.submit({'kind': 'well_kings_case', 'subject': 'the-singer', 'person': 'the-singer', 'ask': 'then_sang', 'case_source': 'Rosh Hashanah 31a:11; Num 21:17 — then sang Israel'})
        w.submit({'kind': 'well_kings_case', 'subject': 'the-east-land', 'person': 'the-east-land', 'ask': 'land_east', 'case_source': 'Chullin 60b:13; Num 21:24-35 — from Arnon to Jabbok, Jazer, Bashan'})
        w.submit({'kind': 'well_kings_case', 'subject': 'the-king-og', 'person': 'the-king-og', 'ask': 'og_lore', 'case_source': 'Niddah 61a:18; Berakhot 54b; Num 21:34 — do not fear him'})
        w.submit({'kind': 'well_kings_case', 'subject': 'the-king-sihon', 'person': 'the-king-sihon', 'ask': 'sihon_refused', 'case_source': 'Deut 2:30; Judg 11:20; Num 21:23 — Sihon did not let Israel pass'})
        w.advance(d0 + SEVENS[0][0])                          # the closing walk: the third day, the seventh day and the seven days fire
    n = lambda eid, eff: len([e for e in w.entity(eid).ledger if e['effect'] == eff])
    L = lambda kk: len([l for l in w.log if l[0] == kk])
    return (n('the-yoked-heifer', 'disqualified'), n('the-tevul-yom-burner', 'accepted'), n('the-gatherer', 'ashes_kept_for_niddah_water'), n('the-trespasser', 'pays'), n('the-sprinkling-priest', 'sprinkled_seven'), n('the-burner', 'impure_until_evening'),
            n('the-toucher', 'sprinkling_due_third_day'), n('the-toucher', 'sprinkling_due_seventh_day'), n('the-toucher', 'declared_pure'), n('the-omitter', 'sprinkling_due_third_day'), n('the-omitter', 'not_purified'),
            n('the-enterer', 'karet_cut_off'), n('the-enterer', 'lashes'), n('the-high-priest', 'exempt'), n('the-tent-dweller', 'tent_unclean'), n('the-tent-dweller', 'corpse_unclean_seven_days'), n('the-open-vessel', 'open_vessel_unclean'),
            n('the-gentile', 'exempt'), n('the-carrier', 'washes_and_bathes'), n('the-carrier', 'impure_until_evening'), n('the-unclean-at-the-camp', 'sent_outside_the_camp'),
            n('the-cattle', 'water_from_the_rock'), n('the-sentenced', 'barred_from_the_land'), n('the-bier', 'buried'),
            n('the-successor', 'garments_transferred'), n('the-successor', 'invested_office'), n('the-successor', 'gathered_to_his_people'), n('the-refuser', 'refused'),
            n('the-captive', 'taken_captive'), n('the-vower', 'cherem_vowed'), n('the-devoted', 'destroyed'), n('the-bitten', 'healed'), n('the-place-hormah', 'hormah_named'),
            n('the-singer', 'well_given'), n('the-east-land', 'land_possessed'), n('the-east-land', 'kings_smitten'), n('the-king-og', 'fear_not_promised'), n('the-king-sihon', 'refused'),
            L('TIMER-SET'), L('TIMER-FIRE'), len(w.entities)), w
SCENE, _W = scene()
SCENE_PREDICTED = (1, 1, 1, 1, 1, 1,
                   1, 1, 1, 1, 1,
                   1, 1, 1, 1, 1, 1,
                   1, 1, 1, 1,
                   1, 1, 1,
                   1, 1, 1, 1,
                   1, 1, 1, 1, 1,
                   1, 1, 1, 1, 1,
                   4, 4, 29)   # PREDICTED from the design BEFORE the first run: one effect per declared row — thirty-eight ledger counts of one; FOUR timers set and fired on the closing walk (the toucher's third and seventh, the omitter's third, the tent-dweller's seven days — the settings not writes, the fires the entries); twenty-nine entities (the subjects; HEAVEN, the priest, Eleazar and the king of Arad counterparties, not entities until written on)
assert SCENE == SCENE_PREDICTED, ('THE NUMBERS WALK: the Chukat scene moved from its prediction', SCENE, SCENE_PREDICTED)


def narrative():
    """THE NUMBERS WALK 6b (2026-09-11; NUMBERS_WALK.md "Sitting 6b"): the portion's own acts AS HISTORY — the thirty-seven lines of Num
    19:1-21:35 in the text's order on a world with this runner's daemon: chapter 19's statute at the running (2, 5, 9) (Seder Olam 8:2 —
    the laws of 1:1-19:22 in the second year); then the fortieth year by its four dates — (40, 1, 1) the arrival at Zin (Seder Olam 9:2's
    new moon of Nisan), (40, 4, 1) Mount Hor (three months at Kadesh), (40, 5, 1) Aaron's death (33:38 read whole by the taught parser),
    (40, 6, 1) the departure (Aaron's death + 20:29's thirty days — the mourning's timer fires on that walk, at its due). On the tape these
    four days are the stitcher's marker rows; here they are advances. The daughters' marker (27:1, the zelophehad runner) moved to
    day_in(40, 6, 1) this sitting — its own literal, reading-placed unchanged (the changelog line). Not a graded cell: the tuple below is a
    tripwire PREDICTED before the first run; the sequence world's RUN tuple grades the tape."""
    with contextlib.redirect_stdout(io.StringIO()):
        w = WE.World(era='Num 19-21: Chukat on the tape — the statute, Kadesh, Meribah, Edom, Mount Hor, Arad, the serpents, the well, the two kings (the exodus epoch)', epoch='exodus')
        w.laws = [law_chukat]
        w.advance(w.clock.day_in('exodus', 2, 5, 9))
        w.submit({'kind': 'heifer_statute_given', 'subject': 'israel', 'heifer': 'red, whole, no blemish, no yoke', 'to': 'eleazar', 'kit': ['cedar', 'hyssop', 'scarlet'], 'case_source': 'Num 19:1-22 — and the LORD spoke to Moses and to Aaron saying: this is the statute of the Torah that the LORD commanded, saying: speak to the children of Israel that they take to you a red heifer, whole, in which there is no blemish, upon which never came a yoke; and you shall give it to Eleazar the priest, and he shall bring it outside the camp and slaughter it before him... and it shall be for the congregation of the children of Israel for a keeping, for waters of niddah; it is a sin offering'})
        w.advance(w.clock.day_in('exodus', 40, 1, 1))     # THE FIRST MARKER on the tape: the arrival at Zin, the new moon of Nisan of the fortieth year
        w.submit({'kind': 'miriam_died_at_kadesh', 'subject': 'miriam', 'at': 'Kadesh, the wilderness of Zin', 'month': FIRST_MONTH[0], 'case_source': 'Num 20:1 — and the children of Israel, the whole congregation, came to the wilderness of Zin in the first month, and the people dwelt at Kadesh; and Miriam died there and was buried there'})
        w.submit({'kind': 'congregation_strove_for_water', 'subject': 'israel', 'words': 'would that we had expired; why have you brought us up from Egypt', 'case_source': 'Num 20:2-5 — and there was no water for the congregation, and they gathered against Moses and against Aaron; and the people strove with Moses and said: would that we had expired when our brothers expired before the LORD; why have you brought the assembly of the LORD into this wilderness... why have you brought us up from Egypt to bring us to this evil place'})
        w.submit({'kind': 'moses_and_aaron_fell_and_the_glory', 'subject': 'moses', 'at': 'the entrance of the tent of meeting', 'case_source': 'Num 20:6 — and Moses and Aaron came from before the assembly to the entrance of the tent of meeting and fell on their faces, and the glory of the LORD appeared to them'})
        w.submit({'kind': 'rock_commanded', 'subject': 'moses', 'verb': 'speak', 'take': 'the staff', 'case_source': 'Num 20:7-8 — and the LORD spoke to Moses saying: take the staff and assemble the congregation, you and Aaron your brother, and speak to the rock before their eyes, and it shall give its water; and you shall bring them water out of the rock and give drink to the congregation and their cattle'})
        w.submit({'kind': 'staff_taken_from_before_the_lord', 'subject': 'moses', 'object': 'the staff from before the LORD', 'case_source': 'Num 20:9 — and Moses took the staff from before the LORD as He commanded him'})
        w.submit({'kind': 'rock_struck_twice', 'subject': 'moses', 'verb': 'struck', 'count': TWICE[0], 'words': 'hear now, you rebels', 'case_source': 'Num 20:10-11 — and Moses and Aaron assembled the assembly before the rock, and he said to them: hear now, you rebels, shall we bring you water out of this rock? and Moses lifted his hand and struck the rock with his staff twice, and much water came out, and the congregation drank, and their cattle'})
        w.submit({'kind': 'sentence_at_meribah', 'subject': 'moses', 'to': ['moses', 'aaron'], 'case_source': 'Num 20:12-13 — and the LORD said to Moses and to Aaron: because you did not believe in Me, to sanctify Me before the eyes of the children of Israel, therefore you shall not bring this assembly into the land which I have given them; these are the waters of Meribah, where the children of Israel strove with the LORD, and He was sanctified in them'})
        w.submit({'kind': 'messengers_sent_to_edom', 'subject': 'israel', 'to': 'the king of Edom', 'words': 'thus says your brother Israel', 'case_source': "Num 20:14-17 — and Moses sent messengers from Kadesh to the king of Edom: thus says your brother Israel: you know all the hardship that has found us; our fathers went down to Egypt... and the Egyptians did evil to us and to our fathers, and we cried to the LORD and He heard our voice and sent a messenger and brought us out of Egypt; and behold, we are at Kadesh, a city at the edge of your border; let us pass, we pray, through your land; we will not pass through field or vineyard, nor drink water of a well; by the king's highway we will go, we will not turn right or left until we pass your border"})
        w.submit({'kind': 'edom_refused', 'subject': 'edom', 'words': 'you shall not pass through me', 'case_source': 'Num 20:18 — and Edom said to him: you shall not pass through me, lest I come out against you with the sword'})
        w.submit({'kind': 'israel_pleaded_the_highway', 'subject': 'israel', 'words': 'by the highway; only on foot', 'case_source': 'Num 20:19 — and the children of Israel said to him: we will go up by the highway, and if we drink your water, I and my cattle, I will give its price; only, nothing more, let me pass on foot'})
        w.submit({'kind': 'edom_came_out_against', 'subject': 'edom', 'with': 'much people and a strong hand', 'case_source': 'Num 20:20-21 — and he said: you shall not pass; and Edom came out against him with much people and with a strong hand; and Edom refused to let Israel pass through his border, and Israel turned away from him'})
        w.advance(w.clock.day_in('exodus', 40, 4, 1))     # THE SECOND MARKER: three months at Kadesh (Seder Olam 9:2), the journey to Mount Hor
        w.submit({'kind': 'journeyed_to_mount_hor', 'subject': 'israel', 'to': 'Mount Hor, by the border of the land of Edom', 'case_source': 'Num 20:22 — and they journeyed from Kadesh, and the children of Israel, the whole congregation, came to Mount Hor'})
        w.submit({'kind': 'aarons_gathering_decreed', 'subject': 'moses', 'words': 'Aaron shall be gathered to his people; because you rebelled at the waters of Meribah', 'case_source': 'Num 20:23-24 — and the LORD said to Moses and to Aaron at Mount Hor, by the border of the land of Edom, saying: Aaron shall be gathered to his people, for he shall not come into the land which I have given to the children of Israel, because you rebelled against My word at the waters of Meribah; take Aaron and Eleazar his son and bring them up Mount Hor'})
        w.submit({'kind': 'aaron_brought_up_mount_hor', 'subject': 'moses', 'with': ['aaron', 'eleazar'], 'case_source': 'Num 20:25-27 — take Aaron and Eleazar his son and bring them up Mount Hor; and strip Aaron of his garments and put them on Eleazar his son, and Aaron shall be gathered and die there; and Moses did as the LORD commanded, and they went up Mount Hor before the eyes of all the congregation'})
        w.advance(w.clock.day_in('exodus', *AARON_DATE))  # THE THIRD MARKER: 33:38 read whole — the fortieth year, the fifth month, the first of the month
        w.submit({'kind': 'garments_transferred_and_aaron_died', 'subject': 'aaron', 'to': 'eleazar', 'age': AARON_AGE[0], 'date': AARON_DATE, 'case_source': 'Num 20:28 — and Moses stripped Aaron of his garments and put them on Eleazar his son; and Aaron died there on the top of the mountain; and Moses and Eleazar came down from the mountain'})
        w.submit({'kind': 'aaron_mourned_thirty_days', 'subject': 'israel', 'days': DAYS30[0], 'who': 'all the house of Israel', 'case_source': 'Num 20:29 — and all the congregation saw that Aaron had expired, and they wept for Aaron thirty days, all the house of Israel'})
        w.submit({'kind': 'arad_fought_and_took_captives', 'subject': 'the-king-of-arad', 'heard': 'that Israel came by the way of Atharim', 'case_source': 'Num 21:1 — and the Canaanite, the king of Arad, who dwelt in the Negev, heard that Israel came by the way of Atharim; and he fought against Israel and took some of them captive'})
        w.submit({'kind': 'israel_vowed_the_cherem', 'subject': 'israel', 'vow': 'if You will indeed give this people into my hand, I will devote their cities', 'case_source': 'Num 21:2 — and Israel vowed a vow to the LORD and said: if You will indeed give this people into my hand, I will devote their cities'})
        w.submit({'kind': 'canaanites_devoted_hormah_named', 'subject': 'israel', 'named': 'Hormah', 'case_source': 'Num 21:3 — and the LORD heard the voice of Israel and gave the Canaanite, and he devoted them and their cities; and he called the name of the place Hormah'})
        w.advance(w.clock.day_in('exodus', 40, 6, 1))     # THE FOURTH MARKER: Aaron's death + the thirty days (the mourning fires on this walk, at its due)
        w.submit({'kind': 'journeyed_by_the_red_sea_way', 'subject': 'israel', 'from': 'Mount Hor', 'by': 'the way of the Red Sea, around the land of Edom', 'case_source': 'Num 21:4 — and they journeyed from Mount Hor by the way of the Red Sea, to go around the land of Edom; and the soul of the people was shortened on the way'})
        w.submit({'kind': 'people_spoke_against_god_and_moses', 'subject': 'israel', 'words': 'why have you brought us up from Egypt to die in the wilderness; our soul loathes the light bread', 'case_source': 'Num 21:5 — and the people spoke against God and against Moses: why have you brought us up from Egypt to die in the wilderness? for there is no bread and no water, and our soul loathes the light bread'})
        w.submit({'kind': 'fiery_serpents_sent', 'subject': 'israel', 'by': 'HEAVEN', 'case_source': 'Num 21:6 — and the LORD sent among the people the fiery serpents, and they bit the people, and many people of Israel died'})
        w.submit({'kind': 'people_confessed_and_moses_prayed', 'subject': 'israel', 'words': 'we have sinned, for we spoke against the LORD and against you', 'case_source': 'Num 21:7 — and the people came to Moses and said: we have sinned, for we spoke against the LORD and against you; pray to the LORD that He remove the serpent from us; and Moses prayed for the people'})
        w.submit({'kind': 'pole_commanded', 'subject': 'moses', 'make': 'a fiery one on a pole', 'case_source': 'Num 21:8 — and the LORD said to Moses: make you a fiery one and set it on a pole; and it shall be, everyone bitten who sees it shall live'})
        w.submit({'kind': 'copper_serpent_made', 'subject': 'moses', 'of': 'copper', 'case_source': 'Num 21:9 — and Moses made a serpent of copper and set it on the pole; and it was, if the serpent bit a man, and he looked at the copper serpent, he lived'})
        w.submit({'kind': 'journeyed_oboth_to_arnon', 'subject': 'israel', 'stations': ['Oboth', 'Iye-abarim', 'the brook Zered', 'beyond Arnon'], 'case_source': "Num 21:10-13 — and the children of Israel journeyed and camped at Oboth; and they journeyed from Oboth and camped at Iye-abarim, in the wilderness before Moab toward the sunrise; from there they journeyed and camped at the brook Zered; from there they journeyed and camped beyond Arnon, in the wilderness that comes out of the Amorite's border, for Arnon is Moab's border, between Moab and the Amorite"})
        w.submit({'kind': 'book_of_the_wars_cited', 'subject': 'israel', 'book': 'the Book of the Wars of the LORD', 'case_source': 'Num 21:14-15 — therefore it is said in the Book of the Wars of the LORD: Vaheb in Suphah and the brooks of Arnon, and the slope of the brooks that turns to the seat of Ar and leans on the border of Moab'})
        w.submit({'kind': 'well_given_at_beer', 'subject': 'israel', 'song': 'rise up, O well', 'case_source': 'Num 21:16-18 — and from there to Beer: that is the well of which the LORD said to Moses: assemble the people and I will give them water; then sang Israel this song: rise up, O well, answer it; the well the princes dug, the nobles of the people delved it, with the lawgiver, with their staffs'})
        w.submit({'kind': 'journeyed_to_pisgah', 'subject': 'israel', 'stations': ['Mattanah', 'Nahaliel', 'Bamoth', 'the valley in the field of Moab', 'the top of Pisgah'], 'case_source': 'Num 21:18-20 — and from the wilderness Mattanah; and from Mattanah Nahaliel; and from Nahaliel Bamoth; and from Bamoth the valley that is in the field of Moab, the top of Pisgah, which looks over the wasteland'})
        w.submit({'kind': 'messengers_sent_to_sihon', 'subject': 'israel', 'to': 'Sihon king of the Amorite', 'case_source': "Num 21:21-22 — and Israel sent messengers to Sihon king of the Amorite saying: let me pass through your land; we will not turn into field or vineyard, we will not drink water of a well; by the king's highway we will go until we pass your border"})
        w.submit({'kind': 'sihon_came_out_and_fought', 'subject': 'sihon', 'at': 'Jahaz', 'case_source': 'Num 21:23 — and Sihon did not let Israel pass through his border; and Sihon gathered all his people and came out against Israel to the wilderness, and came to Jahaz and fought against Israel'})
        w.submit({'kind': 'sihon_smitten_land_possessed', 'subject': 'israel', 'from': 'Arnon', 'to': 'Jabbok', 'case_source': "Num 21:24-25 — and Israel smote him with the edge of the sword and possessed his land from Arnon to Jabbok, as far as the sons of Ammon, for the border of the sons of Ammon was strong; and Israel took all these cities, and Israel dwelt in all the cities of the Amorite, in Heshbon and in all its daughters"})
        w.submit({'kind': 'heshbon_and_the_parable', 'subject': 'israel', 'tellers': 'the parable-tellers', 'case_source': 'Num 21:26-30 — for Heshbon was the city of Sihon king of the Amorite, who had fought against the former king of Moab and taken all his land from his hand as far as Arnon; therefore the parable-tellers say: come to Heshbon... woe to you, Moab; you are lost, people of Chemosh... and we shot them; Heshbon is lost as far as Dibon'})
        w.submit({'kind': 'israel_dwelt_and_jazer_taken', 'subject': 'israel', 'spied': 'Jazer', 'case_source': 'Num 21:31-32 — and Israel dwelt in the land of the Amorite; and Moses sent to spy out Jazer, and they took its daughters and dispossessed the Amorite that was there'})
        w.submit({'kind': 'og_came_out_and_fear_not', 'subject': 'og', 'at': 'Edrei', 'words': 'do not fear him', 'case_source': 'Num 21:33-34 — and they turned and went up by the way of Bashan; and Og king of Bashan came out against them, he and all his people, to battle at Edrei; and the LORD said to Moses: do not fear him, for into your hand I have given him and all his people and his land, and you shall do to him as you did to Sihon king of the Amorite who dwelt at Heshbon'})
        w.submit({'kind': 'og_smitten', 'subject': 'israel', 'survivor': False, 'case_source': 'Num 21:35 — and they smote him and his sons and all his people until no survivor was left to him, and they possessed his land'})
    n = lambda eid, eff: len([e for e in w.entity(eid).ledger if e['effect'] == eff])
    is_open = lambda eid, eff: [e.get('open') for e in w.entity(eid).ledger if e['effect'] == eff]
    L = lambda kk: len([l for l in w.log if l[0] == kk])
    ex = w.clock.eras['exodus']
    markers = [l for l in w.log if l[0] == 'MARKER']
    fires = [l for l in w.log if l[0] == 'TIMER-FIRE']
    return (n('israel', 'commanded'), is_open('israel', 'commanded'),
            n('miriam', 'buried'), n('israel', 'encamped_at'), n('israel', 'gathered_against'), n('the-tabernacle', 'glory_appeared'),
            n('moses', 'commanded'), is_open('moses', 'commanded'), n('israel', 'water_from_the_rock'),
            n('moses', 'barred_from_the_land'), is_open('moses', 'barred_from_the_land'), n('aaron', 'barred_from_the_land'), is_open('aaron', 'barred_from_the_land'),
            n('israel', 'plea_made'), n('edom', 'refused'),
            n('aaron', 'garments_transferred'), n('eleazar', 'invested_office'), n('aaron', 'gathered_to_his_people'), n('israel', 'mourned_thirty_days'),
            n('israel', 'taken_captive'), n('israel', 'cherem_vowed'), is_open('israel', 'cherem_vowed'), n('the-king-of-arad', 'destroyed'), n('hormah', 'hormah_named'),
            n('israel', 'spoke_against_god_and_moses'), n('israel', 'serpents_sent'), n('israel', 'confessed'), n('moses', 'plea_made'), n('the-copper-serpent', 'set_on_the_pole'), n('israel', 'healed'),
            n('israel', 'well_given'), n('sihon', 'refused'), n('sihon', 'kings_smitten'), n('og', 'kings_smitten'), n('israel', 'land_possessed'), n('moses', 'fear_not_promised'),
            L('TIMER-SET'), L('TIMER-FIRE'), [ex.date(f[1]) for f in fires], len(markers), L('EVENT'), L('WRITE'), len(w.entities)), w


NARRATIVE, _WN = narrative()
NARRATIVE_PREDICTED = (1, [True],
                       1, 5, 1, 1,
                       3, [False, False, False], 1,
                       1, [True], 1, [False],
                       3, 2,
                       1, 1, 1, 1,
                       1, 1, [False], 1, 1,
                       1, 1, 1, 1, 1, 1,
                       1, 1, 1, 1, 3, 1,
                       1, 1, [(40, 6, 1)], 0, 37, 42, 12)   # PREDICTED from the design BEFORE the first run (NUMBERS_WALK.md "Sitting 6b"): the heifer's debit OPEN; Miriam buried; Israel encamped five times (Kadesh, Mount Hor, the Red Sea way, Oboth-to-Arnon, Pisgah), the strife, the glory's fifth seat; Moses' three debits (the rock, the ascent, the pole) all CLOSED, the water struck out; Moses barred OPEN, Aaron barred CLOSED by 20:28; Israel's three pleas (Edom twice, Sihon), Edom's two refusals; the garments, Eleazar's office, Aaron gathered, the mourning's fire; the captives, the cherem CLOSED by 21:3, Arad devoted, Hormah named; the speaking against, the serpents, the confession, Moses' prayer, the serpent on the pole, the healing; the well; Sihon's refusal and death, Og's death, the land possessed three times, the fear-not; ONE timer set and fired at (40, 6, 1); no marker (advances here, markers on the tape); thirty-seven events; forty-two writes (forty-one at the lines + the mourning's fire — a timer's setting is not a write; CF3's carcasses are the tape's, not this world's); twelve entities (israel, miriam, the tabernacle, moses, aaron, edom, eleazar, the king of Arad, hormah, the copper serpent, sihon, og)
assert NARRATIVE == NARRATIVE_PREDICTED, ('THE NUMBERS WALK: Chukat\'s narrative moved from its prediction', NARRATIVE, NARRATIVE_PREDICTED)


# =====================================================================
# Motion 2 — THE TEST DATA: the answer sheet's rows (the docket's LAW rows; the expected string = the cell's verdict, typed).
# =====================================================================
CASES = [
    # F1 — the heifer's rite
    ('Menachot 19a:10, 27a:18; Yoma 42a:6; Num 19:2 — the statute indispensable', lambda: heifer_rite({'ask': 'statute_indispensable'}, DATA), 'every detail indispensable — statute and law both written (19:2)'),
    ('Num 19:2, 31:21 — the statute\'s two seats (computed)', lambda: heifer_rite({'ask': 'statute_seats'}, DATA), 'two seats: Num 19:2, Num 31:21'),
    ('Num 19-21 — the six frames (computed)', lambda: heifer_rite({'ask': 'frames'}, DATA), 'six frames — 19:1, 20:7, 20:12, 20:23, 21:8, 21:34'),
    ('Sotah 46a:11; Avodah Zarah 23a:6; Mishnah Parah 2:3 — the yoke: sacks', lambda: heifer_rite({'ask': 'yoke', 'burden': 'sacks'}, DATA), 'disqualified — a burden came on it (19:2; Rav: a bundle of sacks)'),
    ('Shabbat 52a:7; Mishnah Parah 2:3-4 — the yoke: the bit', lambda: heifer_rite({'ask': 'yoke', 'burden': 'bit'}, DATA), 'valid — for its own sake, no burden (Parah 2:3-4; Shabbat 52a)'),
    ('Mishnah Parah 2:3; Sotah 46a:2 — the blemish (the priesthood engine CALLED)', lambda: heifer_rite({'ask': 'blemish'}, DATA), 'disqualified by any consecrated-animal blemish (Parah 2:3; Sotah 46a:2)'),
    ('the priesthood engine\'s passed_blemish row — the blemish that passed', lambda: heifer_rite({'ask': 'blemish', 'passed': True}, DATA), 'fit — the blemish passed (the priesthood engine\'s row)'),
    ('Mishnah Parah 1:1 — the age (DATA)', lambda: heifer_rite({'ask': 'age'}, DATA), 'three or four years (the Sages); R. Eliezer two; R. Meir even five — DATA'),
    ('Mishnah Parah 2:5 — the hairs (DATA)', lambda: heifer_rite({'ask': 'hairs'}, DATA), 'two black or white hairs in one follicle invalidate (Parah 2:5) — DATA'),
    ('Mishnah Parah 2:1 — pregnant (DATA)', lambda: heifer_rite({'ask': 'pregnant'}, DATA), 'invalid (the Sages); R. Eliezer valid — DATA (Parah 2:1)'),
    ('Mishnah Parah 2:1; Avodah Zarah 23a-24a — from gentiles', lambda: heifer_rite({'ask': 'from_gentile'}, DATA), 'valid from gentiles (the Sages — Parah 2:1); R. Eliezer no (Avodah Zarah 23a-24a)'),
    ('Yoma 42b:10-11, 43a:3; Mishnah Parah 4:1 — who burns', lambda: heifer_rite({'ask': 'who_burns'}, DATA), 'the first by Eleazar the deputy; later heifers by a common priest (some say) or the high priest — DATA'),
    ('Yoma 42a:6-11; Zevachim 14b:6 — who slaughters (DISPUTE)', lambda: heifer_rite({'ask': 'who_slaughters'}, DATA), 'a stranger\'s slaughter valid with Eleazar watching (Shmuel); Rav: a priest — DISPUTE'),
    ('Chullin 11a:15 — slaughtered whole, burned whole', lambda: heifer_rite({'ask': 'slaughter_whole'}, DATA), 'burned whole as slaughtered whole — the majority followed (Chullin 11a)'),
    ('Chullin 24a:1 — slaughter, not neck-breaking', lambda: heifer_rite({'ask': 'slaughter_not_neck'}, DATA), 'slaughter only — neck-breaking invalid (Chullin 24a)'),
    ('Chullin 32a:2 — slaughtered alone', lambda: heifer_rite({'ask': 'slaughter_alone'}, DATA), 'disqualified with another animal in one act (Chullin 32a)'),
    ('Yoma 68a:9; Zevachim 105b:17; Mishnah Parah 3:6 — outside the camp', lambda: heifer_rite({'ask': 'outside_the_camp'}, DATA), 'outside three camps, east, opposite the entrance — the Mount of Olives by the ramp (Yoma 68a; Parah 3:6)'),
    ('Menachot 27a:14; Mishnah Parah 3:9, 4:2; Num 19:4 — the seven sprinklings (the chatat and yoma engines CALLED)', lambda: heifer_rite({'ask': 'sprinkling'}, DATA), 'seven sprinklings toward the entrance, each its own dip, all indispensable (19:4 [7]; Parah 3:9, 4:2)'),
    ('Zevachim 93b:14; Menachot 7b:20 — the finger wiped', lambda: heifer_rite({'ask': 'finger_wipe'}, DATA), 'the hand wiped on the heifer after the seventh; the finger on the bowl\'s lip between (Zevachim 93b)'),
    ('Num 19:5 against Exod 29:14, Lev 4:11, 16:27 — the burn-list with the blood (computed; the chatat engine CALLED)', lambda: heifer_rite({'ask': 'burn_list'}, DATA), 'the sin-bull\'s burn-list WITH THE BLOOD ADDED — burned whole with its blood (19:5; Zevachim 93b)'),
    ('Menachot 27a:13; Mishnah Parah 3:10-11; Num 19:6 — the kit (the leper engine CALLED)', lambda: heifer_rite({'ask': 'kit'}, DATA), 'cedar, hyssop and scarlet — the three indispensable, cast into the burning by a priest (19:6; Menachot 27a)'),
    ('Num 19:6; Lev 14:4, 14:6, 14:49, 14:51, 14:52 — the kit\'s order (computed at six seats)', lambda: heifer_rite({'ask': 'kit_order'}, DATA), 'the heifer\'s order is Lev 14:51-52\'s (cedar, hyssop, scarlet — the house\'s dipping); the takings 14:4, 14:6, 14:49 have cedar, scarlet, hyssop — computed at six seats'),
    ('Yoma 43a:5; Mishnah Parah 4:1 — the priest in his garments', lambda: heifer_rite({'ask': 'priest_in_garments'}, DATA), 'by a priest in his garments — white garments (Parah 4:1; Yoma 43a)'),
    ('Mishnah Parah 4:4, 7:1-12 — other work invalidates', lambda: heifer_rite({'ask': 'work_invalidates'}, DATA), 'other work invalidates from the slaughter until the ashes; the water until the ashes are in it (Parah 4:4, 7)'),
    ('Yoma 2a:10; Mishnah Parah 3:1 — the sequestering', lambda: heifer_rite({'ask': 'sequestering'}, DATA), 'seven days\' sequestering in the Stone Chamber, sprinkled through them (Yoma 2a; Parah 3:1)'),
    ('Mishnah Parah 3:2-8 — the procession', lambda: heifer_rite({'ask': 'procession'}, DATA), 'the children\'s water, the child\'s mixing, the ramp to the Mount of Olives, the pile facing west (Parah 3:2-8)'),
    ('Yoma 43b:3; Zevachim 17b:3; Mishnah Parah 3:7 — the tevul yom', lambda: heifer_rite({'ask': 'tvul_yom'}, DATA), 'the tevul yom fit — the burner defiled on purpose against the Sadducees (Parah 3:7; Yoma 43b)'),
    ('Yoma 43a:7; Yevamot 72b:16; Num 19:9 — the gatherer', lambda: heifer_rite({'ask': 'gatherer'}, DATA), 'a non-priest and a woman gather; the deaf-mute, imbecile and minor do not (Yoma 43a:7)'),
    ('Mishnah Parah 3:11; Num 19:9 — the ashes in three', lambda: heifer_rite({'ask': 'ashes_thirds'}, DATA), 'three parts — the rampart, the Mount of Olives, the priestly watches (Parah 3:11); kept for waters of niddah'),
    ('Menachot 51b:22; Mishnah Parah 4:4; Num 19:9 — me\'ilah (the Lev 5 engine CALLED)', lambda: heifer_rite({'ask': 'meilah'}, DATA), 'me\'ilah applies — a sin offering (19:9; Menachot 51b): the principal, the fifth, the ram'),
    ('Mishnah Parah 4:1, 4:3 — for its name', lambda: heifer_rite({'ask': 'for_its_name'}, DATA), 'not for its name invalid; the eating intention harmless (Parah 4:1, 4:3)'),
    ('Mishnah Parah 3:5 — the nine heifers (the open debit\'s run)', lambda: heifer_rite({'ask': 'nine_heifers'}, DATA), 'nine heifers — Moses, Ezra, seven after (the Sages; R. Meir five): the shelf\'s run of the open debit (Parah 3:5)'),
    ('Yoma 42b:3-4; Mishnah Parah 4:4 — by a priest by day', lambda: heifer_rite({'ask': 'day_and_priest'}, DATA), 'the rite\'s stages by a priest by day; the gathering, filling and mixing not so bound (Yoma 42b; Parah 4:4)'),
    ('Yoma 42a:11, 42b:1 — the attention', lambda: heifer_rite({'ask': 'attention'}, DATA), 'attention undiverted from the slaughter through the keeping; the kit\'s casting excepted (Yoma 42a-b)'),
    ('Mishnah Parah 4:4, 8:3; Num 19:7-10 — the rite defiles its servants', lambda: heifer_rite({'ask': 'defiles_garments'}, DATA), 'the burner, the gatherer and the priest unclean until evening — the rite defiles its servants, the heifer does not (Parah 4:4, 8:3)'),
    ('Mishnah Parah 3:8, 4:3 — the wood', lambda: heifer_rite({'ask': 'wood'}, DATA), 'any wood, straw or stubble valid; the pile\'s four woods (Parah 3:8, 4:3)'),
    ('Yoma 42b:12; Mishnah Parah 3:7 — taken out alone', lambda: heifer_rite({'ask': 'taken_out_alone'}, DATA), 'brought out alone — no black cow, no second red one (Parah 3:7; Yoma 42b)'),
    ('Yoma 43a:3; Kiddushin 36b:2 — who sprinkles the blood', lambda: heifer_rite({'ask': 'who_sprinkles_blood'}, DATA), 'a priest sprinkles the blood — Eleazar (Shmuel) or any priest (Rav); not a woman (Kiddushin 36b)'),
    ('Mishnah Parah 10:1-6 — madaf (the heifer)', lambda: heifer_rite({'ask': 'madaf'}, DATA), 'madaf — the unclean has it, the clean not (the Sages; Parah 10:1); the hand defiles, the foot not (10:2)'),
    ('Num 19:1-22 — the first heifer never narrated (the tape\'s open debit)', lambda: heifer_rite({'ask': 'first_heifer_open'}, DATA), 'the heifer\'s debit OPEN on the tape — the ink never narrates the first burning; Parah 3:5 the shelf\'s run'),
    # F2 — the corpse's uncleanness and the sprinkling
    ('Num 19:11 — seven days (computed)', lambda: corpse_tumah({'ask': 'seven_days'}, DATA), 'unclean seven days — the toucher (19:11)'),
    ('Num 19:12, 19:19; Kiddushin 62a:4 — the schedule kept', lambda: corpse_tumah({'ask': 'schedule', 'third': True, 'seventh': True}, DATA), 'sprinkled on the third and the seventh: clean in the evening of the seventh (19:12, 19:19)'),
    ('Num 19:12b — the seventh omitted', lambda: corpse_tumah({'ask': 'schedule', 'third': True, 'seventh': False}, DATA), 'the seventh omitted: not clean (19:12b)'),
    ('Kiddushin 62a:6 — the third omitted', lambda: corpse_tumah({'ask': 'schedule', 'third': False, 'seventh': True}, DATA), 'the third omitted: the seventh does not clean — the interval fixed (Kiddushin 62a)'),
    ('Num 19:13 — neither sprinkling', lambda: corpse_tumah({'ask': 'schedule', 'third': False, 'seventh': False}, DATA), 'neither sprinkling: not clean — his uncleanness is yet on him (19:13)'),
    ('Num 5:2 -> 19:12, 19:19 — THE PAID EDGE naso -> chukat: the corpse-unclean\'s purification', lambda: corpse_tumah({'ask': 'purification'}, DATA), 'the third and the seventh day\'s sprinkling with the water of niddah, then the wash, the bath and the evening (19:12, 19:19)'),
    ('Num 8:7 -> 19:9, 19:17-18 — THE PAID EDGE beha -> chukat: the water of purification', lambda: corpse_tumah({'ask': 'sprinkling_water'}, DATA), 'the heifer\'s ashes on living water in a vessel, sprinkled with hyssop by a clean man (19:9, 19:17-18) — 8:7\'s water'),
    ('Arakhin 3a:6-7; Niddah 44a:7 — the minor', lambda: corpse_tumah({'ask': 'minor'}, DATA), 'a minor impure (even a day old), no karet for his entry (Arakhin 3a; Niddah 44a)'),
    ('Avodah Zarah 37b:7; Mishnah Oholot 1:1; Num 19:22 — the toucher of the toucher', lambda: corpse_tumah({'ask': 'toucher_of_toucher'}, DATA), 'the toucher of the toucher unclean until evening (19:22; Oholot 1:1)'),
    ('Mishnah Oholot 1:1-4; Kelim 1:4 — the removes (DATA)', lambda: corpse_tumah({'ask': 'removes'}, DATA), 'the removes — the toucher seven days, the second until evening; vessels three in a series, persons two (Oholot 1:1-4)'),
    ('Makkot 14b:6; Mishnah Keritot 1:1; Num 19:13, 19:20 — the entry: intentional', lambda: corpse_tumah({'ask': 'karet_entry'}, DATA), 'cut off — the intentional entry of the impure into the sanctuary; lashes with it (19:13, 19:20; Makkot 14b)'),
    ('Mishnah Shevuot 1:1-2:5; Keritot 1:2 — the entry: unwitting', lambda: corpse_tumah({'ask': 'karet_entry', 'intent': 'unwitting'}, DATA), 'unwitting entry — the sliding-scale offering by the awareness grid (Mishnah Shevuot 1:1-2:5; Keritot 1:2)'),
    ('Horayot 9b:3; Mishnah Parah 12:4 — the high priest exempt', lambda: corpse_tumah({'ask': 'high_priest_exempt'}, DATA), 'the high priest exempt from the entry\'s karet (Horayot 9b; Parah 12:4)'),
    ('Shevuot 16b:1; Mishnah Shevuot 2:3 — made impure inside', lambda: corpse_tumah({'ask': 'impure_inside'}, DATA), 'made impure inside: liable unless he leaves by the shortest way (Shevuot 16b; Mishnah Shevuot 2:3)'),
    ('Shabbat 16b:3 — the metal vessels\' decree', lambda: corpse_tumah({'ask': 'metal_vessels_decree'}, DATA), 'metal vessels keep their impurity until the sprinkling — the Sages\' fence (Shabbat 16b)'),
    ('Mishnah Oholot 3:6-7; Num 19:14 — the tent', lambda: corpse_tumah({'ask': 'tent'}, DATA), 'the tent\'s enterers and contents unclean seven days — by the handbreadth (19:14; Oholot 3:6-7)'),
    ('Bava Metzia 114b:2; Yevamot 61a:1 — gentiles\' graves', lambda: corpse_tumah({'ask': 'tent_gentile'}, DATA), 'gentiles\' graves defile by touch and carrying, not by tent (Bava Metzia 114b; Yevamot 61a)'),
    ('Bekhorot 45a:20 — the limbs equal for all', lambda: corpse_tumah({'ask': 'tent_limbs'}, DATA), 'the tent\'s impurity from the limbs equal for all (Bekhorot 45a)'),
    ('Sukkah 21a:1; Shabbat 28a:1 — the tent\'s material', lambda: corpse_tumah({'ask': 'tent_material'}, DATA), 'any shelter (the Rabbis — "tent, tent" amplifies); R. Yehuda man-made (Sukkah 21a; Shabbat 28a)'),
    ('Mishnah Oholot 3:6-7, 12:6-7 — the tent\'s measures (DATA)', lambda: corpse_tumah({'ask': 'tent_measure'}, DATA), 'a handbreadth square blocks and conveys; a corpse\'s opening four; the beam\'s circumference three round, four square (Oholot 3:6-7, 12:6-7)'),
    ('Mishnah Oholot 4-15 — the overshadowing tables (DATA)', lambda: corpse_tumah({'ask': 'overshadowing_table'}, DATA), 'the overshadowing tables as DATA (Oholot 4-15) — the handbreadth the unit; out, not in'),
    ('Mishnah Kelim 10:1; Chullin 25a:3; Num 19:15 — the open vessel', lambda: corpse_tumah({'ask': 'open_vessel'}, DATA), 'unclean — an open vessel in the tent (19:15; Kelim 10:1)'),
    ('Mishnah Kelim 10:1-2 — the cord-bound cover', lambda: corpse_tumah({'ask': 'open_vessel', 'covered': True}, DATA), 'protected — a cord-bound cover on it: earthenware protects foods, liquids and earthenware; the other vessels everything (19:15; Kelim 10:1)'),
    ('Nazir 53b:10, 54a:1; Mishnah Oholot 2; Num 19:16, 19:18 — the four sources (computed)', lambda: corpse_tumah({'ask': 'field_sources'}, DATA), 'the four sources — the slain, the dead, the bone (a barley-grain), the grave: unclean seven days (19:16; Nazir 54a; Oholot 2)'),
    ('Pesachim 14b:1, 79a:15; Shabbat 101b:8 — a sword like the slain', lambda: corpse_tumah({'ask': 'sword_like_slain'}, DATA), 'a sword is like the slain — the metal vessel takes the corpse\'s grade (Pesachim 14b, 79a; Shabbat 101b)'),
    ('Chullin 72a:6-7 — the fetus in the womb (DISPUTE)', lambda: corpse_tumah({'ask': 'fetus_in_womb'}, DATA), 'the dead fetus in the womb — excluded (R. Yishmael) / impure from "of the life" (R. Akiva) — DISPUTE (Chullin 72a)'),
    ('Chullin 72a:8; Mishnah Oholot 2:2; Num 19:13 — a quarter-log of blood', lambda: corpse_tumah({'ask': 'quarter_log_blood'}, DATA), 'a quarter-log of blood defiles as the corpse (Chullin 72a; Oholot 2:2)'),
    ('Pesachim 34b:13; Mishnah Parah 8:8-11; Num 19:17 — living water', lambda: corpse_tumah({'ask': 'living_water'}, DATA), 'spring water drawn straight into a vessel; the seas and the marsh rivers unfit (Pesachim 34b; Parah 8:8-11)'),
    ('Sotah 16b:15; Mishnah Parah 6:1; Num 19:17 — the mixing order', lambda: corpse_tumah({'ask': 'mixing_order'}, DATA), 'the ashes upon the water, by hand and with intent — the dust-word for the sotah analogy (Sotah 16b; Parah 6:1)'),
    ('Yoma 43a:13; Mishnah Parah 12:10 — who sprinkles (DISPUTE)', lambda: corpse_tumah({'ask': 'sprinkler_who'}, DATA), 'a man, not a woman (a minor by "pure"); R. Yehuda: an adult, a woman by "pure" — DISPUTE (Yoma 43a; Parah 12:10)'),
    ('Yevamot 72b:16; Yoma 43a:9-12 — who sanctifies', lambda: corpse_tumah({'ask': 'who_sanctifies'}, DATA), 'as the gatherer — a woman sanctifies; two take and one puts (Yevamot 72b; Yoma 43a)'),
    ('Megillah 20a:10; Mishnah Parah 12:11 — the sprinkling by day', lambda: corpse_tumah({'ask': 'sprinkling_day'}, DATA), 'by day, from sunrise; dipped by day and sprinkled at night invalid (Megillah 20a; Parah 12:11)'),
    ('Yoma 14a:5; Mishnah Parah 12:3 — sprinkling on the pure (DISPUTE)', lambda: corpse_tumah({'ask': 'sprinkling_on_pure'}, DATA), 'sprinkling counts only on the susceptible (the Rabbis); R. Akiva: the pure sprinkled becomes impure — DISPUTE'),
    ('Yoma 14a:9; Niddah 9a:15; Num 19:21 — the sprinkler and the carrier', lambda: corpse_tumah({'ask': 'sprinkler_carrier'}, DATA), 'the sprinkler clean, the carrier washes his clothes, the toucher unclean until evening (19:21; Yoma 14a)'),
    ('Sukkah 37a:8; Mishnah Parah 12:1-2; Num 19:18 — the hyssop dipped', lambda: corpse_tumah({'ask': 'hyssop_dip'}, DATA), 'the hyssop dipped in the vessel\'s own water, lengthened if short; the doubts invalid (Sukkah 37a; Parah 12:1-2)'),
    ('Mishnah Parah 11:7-9 — the hyssop\'s species (the leper engine CALLED)', lambda: corpse_tumah({'ask': 'hyssop_species'}, DATA), 'plain hyssop of three stalks — the leper\'s kind; the named kinds invalid (Parah 11:7-9)'),
    ('Mishnah Parah 12:5; Sifrei 129 — the water\'s measure (DATA)', lambda: corpse_tumah({'ask': 'water_measure'}, DATA), 'enough to dip the tips of the buds and sprinkle (Parah 12:5; Sifrei 129); under it a father by contact, above by carrying (Kelim 1:1-2)'),
    ('Shabbat 48b:10; Mishnah Parah 12:8-10 — the connection', lambda: corpse_tumah({'ask': 'connection'}, DATA), 'connected for impurity, not for the sprinkling — each part sprinkled (Shabbat 48b; Parah 12:9)'),
    ('Kiddushin 25a:15 — sprinkled on a part (DISPUTE)', lambda: corpse_tumah({'ask': 'sprinkle_on_part'}, DATA), 'on any part of the body that can become impure (Rebbi — Kiddushin 25a) — DISPUTE'),
    ('Nazir 61b:1-3; Num 19:20 — the gentile', lambda: corpse_tumah({'ask': 'gentile_no_tumah'}, DATA), 'the gentile has no corpse-impurity — no membership in the assembly (Nazir 61b)'),
    ('Mishnah Parah 11:4-6 — the tevul yom and the hatat', lambda: corpse_tumah({'ask': 'tevul_yom_hatat'}, DATA), 'the tevul yom by Torah law guilty for entering; by the scribes\' word not; both defile the hatat water (Parah 11:4-6)'),
    ('Mishnah Parah 9:1-9; Gittin 86b:14 — the invalidated water', lambda: corpse_tumah({'ask': 'invalid_water'}, DATA), 'invalidated by water fallen in, bursting insects, a beast that drank; the kartzit harmless (Parah 9; Gittin 86b)'),
    ('Mishnah Parah 9:8, 12:6-7 — the water defiles', lambda: corpse_tumah({'ask': 'water_defiles'}, DATA), 'the hatat water defiles the terumah-clean by hands or body, the hatat-clean by hands (Parah 9:8; the chains 12:6-7)'),
    ('Mishnah Parah 9:6 — the water\'s transport', lambda: corpse_tumah({'ask': 'water_transport'}, DATA), 'not carried across a river by ship (Parah 9:6)'),
    ('Mishnah Parah 5:2-9 — the vessel for the water', lambda: corpse_tumah({'ask': 'vessel_for_water'}, DATA), 'a vessel required for the filling, the mixing and the sprinkling; the trough in the rock is none (Parah 5:5-9)'),
    ('Tosefta Chagigah 3:20; Mishnah Parah 5:1; Num 19:9 — all trusted', lambda: corpse_tumah({'ask': 'all_trusted'}, DATA), 'all are trusted for the heifer\'s water (Tosefta Chagigah 3:20; Parah 5:1)'),
    ('Mishnah Oholot 16:2-18:6 — a bet peras', lambda: corpse_tumah({'ask': 'bet_peras'}, DATA), 'a bet peras — the plowed grave\'s hundred cubits, the lost grave\'s field, the kokhin field: contact and carriage; purified by three handbreadths (Oholot 17-18)'),
    ('Mishnah Oholot 18:7-10 — gentile dwellings', lambda: corpse_tumah({'ask': 'gentile_dwellings'}, DATA), 'gentile dwellings unclean after forty days; ten places excepted (Oholot 18:7-10)'),
    ('Mishnah Oholot 2:4, 15:8-9; Chullin 72a:6 — the grave\'s stones', lambda: corpse_tumah({'ask': 'grave_stones'}, DATA), 'the grave\'s covering and buttressing stones defile by contact and overshadowing, not carriage (Oholot 2:4)'),
    ('Mishnah Oholot 1:7-8, 3:3-4 — the limb', lambda: corpse_tumah({'ask': 'limb'}, DATA), 'a whole limb defiles at any size; 248 limbs; the teeth, hair and nails clean when severed (Oholot 1:7-8, 3:3)'),
    ('Mishnah Oholot 2:1-7 — the bone\'s measure (DATA)', lambda: corpse_tumah({'ask': 'bone_measure'}, DATA), 'a barley-grain of bone by contact and carriage; a quarter-kav or the majority by tent; deficient clean (Oholot 2:1-7)'),
    ('Mishnah Oholot 1:6 — the moment of death', lambda: corpse_tumah({'ask': 'death_moment'}, DATA), 'defiles from the death, not before — the dying binds and feeds still (Oholot 1:6)'),
    ('Niddah 55a:4; Num 19:16 — the dry corpse', lambda: corpse_tumah({'ask': 'dry_flesh'}, DATA), 'the corpse defiles dry, as the bone (Niddah 55a)'),
    ('Mishnah Oholot 7:4-6 — the birth and the fetus', lambda: corpse_tumah({'ask': 'birth_and_fetus'}, DATA), 'the opened tomb; the mother\'s life before the fetus until the greater part emerges (Oholot 7:4-6)'),
    ('Shabbat 17a:2; Mishnah Oholot 16:1 — the ox-goad', lambda: corpse_tumah({'ask': 'ox_goad'}, DATA), 'movables convey to the carrier at an ox-goad\'s thickness, to themselves at any, to others at a handbreadth (Oholot 16:1)'),
    ('Mishnah Oholot 13:1-6 — the window\'s measures', lambda: corpse_tumah({'ask': 'window_measures'}, DATA), 'the window\'s measures — the drill\'s hole for light, a square handbreadth for use; the clean reduces (Oholot 13)'),
    ('Mishnah Parah 10:1 — madaf (the hatat)', lambda: corpse_tumah({'ask': 'madaf'}, DATA), 'madaf for the hatat — the unclean has it, the clean not (Parah 10:1)'),
    ('Mishnah Mikvaot 1:1-8 — the six degrees', lambda: corpse_tumah({'ask': 'mikveh_grades'}, DATA), 'six degrees — the living waters the top: the zav, the leper and the hatat water (Mikvaot 1:8)'),
    ('Mishnah Kelim 1:7-8; Num 5:2 — the camps (the paid edge\'s floor)', lambda: corpse_tumah({'ask': 'camps'}, DATA), 'the corpse-impure barred at the chel; out of the Presence\'s camp alone (Kelim 1:8; Num 5:2)'),
    ('Berakhot 63b:14; Gittin 57b:22; Shabbat 83b:10 — the homily on the tent', lambda: corpse_tumah({'ask': 'torah_endures'}, DATA), 'the homily — Torah endures in one who kills himself over it in its tent (Berakhot 63b)'),
    # F3 — Miriam's death and the waters of Meribah
    ('Taanit 9a:9; Seder Olam Rabbah 10:2; Num 20:1-2 — the well by merit', lambda: meribah({'ask': 'well_by_merit'}, DATA), 'the well gone at Miriam\'s death, returned by Moses\' and Aaron\'s merit (Taanit 9a; Seder Olam 10:2)'),
    ('Bava Batra 17a:4 — death by the kiss', lambda: meribah({'ask': 'death_by_the_kiss'}, DATA), 'Miriam too by the kiss — "there" / "there" with Deut 34:5 (Bava Batra 17a)'),
    ('Moed Katan 28a:2; Num 20:1 — buried near the death', lambda: meribah({'ask': 'burial_near_death'}, DATA), 'buried near the death — the woman\'s bier not set down in the street (Moed Katan 28a)'),
    ('Avodah Zarah 29b:12; Sanhedrin 47b:17 — there / there', lambda: meribah({'ask': 'there_there'}, DATA), 'benefit from a corpse forbidden — "there" / "there" with the eglah arufah (Avodah Zarah 29b; Sanhedrin 47b)'),
    ('Sanhedrin 101b:10; Sotah 12b:14; Num 20:13 — the astrologers\' waters', lambda: meribah({'ask': 'astrologers'}, DATA), 'the astrologers\' waters — Meribah, not the Nile (Sanhedrin 101b; Sotah 12b)'),
    ('Sanhedrin 110a:9; Num 20:13 — the quarrel with the teacher', lambda: meribah({'ask': 'quarrel_with_teacher'}, DATA), 'a quarrel with the teacher is a quarrel with the Presence (Sanhedrin 110a)'),
    ('Menachot 76b:13; Num 20:8 — the cattle', lambda: meribah({'ask': 'cattle_water'}, DATA), 'the cattle included — the Torah spared Israel\'s money (Menachot 76b)'),
    ('Num 20:11 — struck twice (computed; rule 19)', lambda: meribah({'ask': 'struck_twice'}, DATA), 'struck twice — [2] by the parser (20:11); much water came out'),
    ('Num 20:8, 20:11-12; Ps 106:32-33 — the sin (the spec / run delta)', lambda: meribah({'ask': 'sin'}, DATA), 'the spec\'s SPEAK, the run\'s STRUCK TWICE — the sin the ink\'s own delta; the rash speech the Psalm\'s (20:8-12; Ps 106:33)'),
    ('Shabbat 55b:2; Yoma 87a:3 — died for their sin', lambda: meribah({'ask': 'died_for_sin'}, DATA), 'died for their sin — had they believed, their time had not come (Shabbat 55b; Yoma 87a)'),
    ('Yoma 86b:15 — the disgrace written', lambda: meribah({'ask': 'disgrace_written'}, DATA), 'Moses\' disgrace written explicitly at 20:12 (Yoma 86b)'),
    ('Num 20:12, 20:24; Deut 32:51 — the sentence', lambda: meribah({'ask': 'sentence'}, DATA), 'barred from the land — Moses and Aaron; Aaron\'s closed at 20:28, Moses\' at Deut 34 (20:12)'),
    ('Seder Olam Rabbah 9:2, 10:2; Num 20:1 — Miriam\'s day (the row; CM5)', lambda: meribah({'ask': 'miriam_day'}, DATA), 'the tenth of Nisan (Seder Olam 10:2); the arrival on the new moon (9:2) — the tape\'s marker on the first, the row\'s arm the tenth'),
    ('Exod 17:7; Num 20:13 — Meribah\'s seats (computed)', lambda: meribah({'ask': 'meribah_seats'}, DATA), 'Meribah at 6 seats — Exod 17:7 the first, Num 20:13 the second (computed)'),
    ('Exod 17:2-3; Num 20:3-5 — the first Meribah\'s clauses at the second (computed)', lambda: meribah({'ask': 'first_meribah_clauses'}, DATA), 'Exod 17:2-3\'s clauses at Num 20:3-5 — strove, brought up, from Egypt (computed)'),
    ('Num 20:10, 20:1; Exod 15:23 — the rebels\' skin (the reading\'s crown)', lambda: meribah({'ask': 'rebels_skin'}, DATA), 'the rebels, Miriam and the bitter waters — one consonantal skin, three words (20:10)'),
    # F4 — Edom, Mount Hor, the succession and the mourning
    ('Rosh Hashanah 3a:1; Taanit 9a:10; Num 20:29, 21:1 — what Arad heard', lambda: edom_and_hor({'ask': 'arad_heard'}, DATA), 'Arad heard that Aaron died and the clouds departed (Rosh Hashanah 3a; Taanit 9a) — the attack during the mourning'),
    ('Num 33:38-39; Seder Olam Rabbah 10:2 — the death dates (computed; rule 20)', lambda: edom_and_hor({'ask': 'death_dates'}, DATA), 'Aaron (40, 5, 1) by the ink, aged 123; Miriam the tenth of Nisan by the shelf; Moses the seventh of Adar (33:38-39; Seder Olam 10:2)'),
    ('Seder Olam Rabbah 9:2 — the fortieth year\'s walk', lambda: edom_and_hor({'ask': 'seder_olam_walk'}, DATA), 'the fortieth year\'s walk: (40, 1, 1) the arrival, three months at Kadesh, Aaron\'s death, the retreat to Moserah, the daughters after the conquest (Seder Olam 9:2)'),
    ('Deut 10:6 against Num 20:28; Seder Olam Rabbah 9:2 — Moserah', lambda: edom_and_hor({'ask': 'moserah'}, DATA), 'Moserah — the retreat of seven stations after Arad\'s attack, the mourning renewed there (Seder Olam 9:2); the death at Mount Hor (20:28)'),
    ('Exod 29:29-30 run at Num 20:26-28 — the succession (the vestments and priesthood engines CALLED)', lambda: edom_and_hor({'ask': 'succession'}, DATA), 'the garments to Eleazar and the office with them — Exod 29:29-30 run at Mount Hor (20:26-28)'),
    ('Num 20:29; Deut 34:8 — the thirty days (computed; the timer)', lambda: edom_and_hor({'ask': 'thirty_days'}, DATA), 'thirty days\' weeping by all the house of Israel — a timer due (40, 6, 1) (20:29; Deut 34:8 Moses\' thirty)'),
    ('Num 20:18-21; Deut 2:28-29 — Edom\'s passage (DISPUTE)', lambda: edom_and_hor({'ask': 'edom_passage'}, DATA), 'Edom refused twice and Israel turned away (20:18-21); Deut 2:28-29\'s purchase the other arm — DISPUTE'),
    ('Num 20:17; 21:22 — the two messages (computed)', lambda: edom_and_hor({'ask': 'two_messages'}, DATA), 'thirteen tokens shared between the Edom and Sihon messages (20:17; 21:22 — computed)'),
    ('Num 20:22, 34:7-8 — the two Mount Hors', lambda: edom_and_hor({'ask': 'two_mount_hors'}, DATA), 'two Mount Hors — Aaron\'s at Edom\'s border, the northern border\'s (34:7-8)'),
    ('Num 33:39 — Aaron\'s age (computed)', lambda: edom_and_hor({'ask': 'aaron_age'}, DATA), 'Aaron 123 at his death (33:39 — [123])'),
    ('Num 20:15-16; Deut 26:6-7 — the firstfruits clauses in the letter (computed)', lambda: edom_and_hor({'ask': 'firstfruits_clauses'}, DATA), 'the firstfruits declaration\'s clauses in the Edom letter — "and we cried to the LORD" at Num 20:16 and Deut 26:7 alone'),
    ('Onkelos Num 20:14, 20:16 — one noun, two translations', lambda: edom_and_hor({'ask': 'messengers_word'}, DATA), 'one noun, two translations — envoys for Moses\' men, the angel for the LORD\'s (20:14, 20:16)'),
    # F5 — Arad, the vow, the serpents and the pole
    ('Gittin 38a:4; Num 21:1 — the captive acquired', lambda: arad_and_the_serpent({'ask': 'captive_acquired'}, DATA), 'acquired by conquest — a gentile acquires a Jew by possession (Gittin 38a); the shelf\'s one maidservant'),
    ('Eruvin 64b:3; Num 21:2 — the vow\'s form', lambda: arad_and_the_serpent({'ask': 'vow_form'}, DATA), 'the conditional vow — a portion sanctified for success (21:2; Eruvin 64b)'),
    ('Lev 27:28-29 at Num 21:3 — the cherem (the temurah engine CALLED)', lambda: arad_and_the_serpent({'ask': 'cherem_law'}, DATA), 'the cherem executed — the devoted not redeemed, the persons put to death (21:3; Lev 27:28-29 by the temurah engine)'),
    ('Num 21:3 against 14:45; Judg 1:17 — Hormah (CF9)', lambda: arad_and_the_serpent({'ask': 'hormah'}, DATA), 'Hormah named at 21:3 after its use at 14:45 — the proleptic name closed; Judg 1:17 the second naming'),
    ('Num 21:4 against 14:25; Deut 2:1 — the turn-back run (CF8)', lambda: arad_and_the_serpent({'ask': 'turn_back'}, DATA), '14:25\'s turn-back run at 21:4 — the open debit closed (CF8)'),
    ('Yoma 75a; Avodah Zarah 5b:1; Num 21:5 — the light bread', lambda: arad_and_the_serpent({'ask': 'light_bread'}, DATA), 'the manna called light — absorbed in the limbs (Yoma 75a); ingrates (Avodah Zarah 5b)'),
    ('Sanhedrin 110a:10; Num 21:5 — against God and against Moses', lambda: arad_and_the_serpent({'ask': 'spoke_against'}, DATA), 'against God and against Moses likened — suspecting the teacher (Sanhedrin 110a)'),
    ('Num 21:6; 19:5; Deut 23:20 — the bite and the burn (the reading\'s crown)', lambda: arad_and_the_serpent({'ask': 'bite_and_burn'}, DATA), 'the fiery serpents — the heifer\'s burn-word, usury\'s bite (21:6)'),
    ('Num 21:6-9 — plural then singular (the reading\'s measurement)', lambda: arad_and_the_serpent({'ask': 'singular_serpent'}, DATA), 'the serpents sent, the serpent removed — plural then singular (21:6-9)'),
    ('Num 21:8-9; Exod 17:15; Num 26:10 — the pole-word', lambda: arad_and_the_serpent({'ask': 'pole_word'}, DATA), 'the pole-word — the banner of Exod 17:15 and the sign of 26:10 (21:8-9)'),
    ('Avodah Zarah 44a:7; Num 21:8 — Moses\' own serpent', lambda: arad_and_the_serpent({'ask': 'serpent_property'}, DATA), 'Moses\' own serpent — not an idol by right, its worship notwithstanding (Avodah Zarah 44a)'),
    ('Mishnah Rosh Hashanah 3:8; Num 21:8-9 — does the serpent heal', lambda: arad_and_the_serpent({'ask': 'serpent_heals'}, DATA), 'the serpent neither kills nor heals — the heart subjected to Heaven heals (Mishnah Rosh Hashanah 3:8)'),
    ('2 Kgs 18:4; Berakhot 10b:7; Pesachim 56a — Nehushtan', lambda: arad_and_the_serpent({'ask': 'nehushtan'}, DATA), 'Nehushtan — broken by Hezekiah, the Sages agreed (2 Kgs 18:4; Berakhot 10b; Pesachim 56a)'),
    # F6 — the stations, the well, Sihon and Og
    ('Deut 2:14 at Num 21:12 — the Zered\'s date (computed; CM3)', lambda: well_and_kings({'ask': 'zered_date'}, DATA), 'the Zered crossed after the thirty-eight years (Deut 2:14 — [38]); the timer due (40, 5, 9), the dying ceased the fifteenth of Av by the shelf, the crossing after the mourning by the text'),
    ('Bava Batra 14b; Num 21:14-15 — the Book of the Wars', lambda: well_and_kings({'ask': 'book_of_wars'}, DATA), 'the Book of the Wars of the LORD cited — the unnamed book\'s one citation (21:14)'),
    ('Berakhot 54a:16, 54b:1 — the Arnon miracle', lambda: well_and_kings({'ask': 'arnon_miracle'}, DATA), 'the mountains met over the Emorites, the blood ran to the Arnon, the lepers saw and Israel sang (Berakhot 54a-b)'),
    ('Exod 15:1; Num 21:17 — then sang (computed)', lambda: well_and_kings({'ask': 'then_sang'}, DATA), '"then sang" at two seats — the sea and the well (Exod 15:1; Num 21:17)'),
    ('Gen 49:10; Num 21:18; Deut 33:21 — the lawgiver (computed)', lambda: well_and_kings({'ask': 'lawgiver'}, DATA), 'the lawgiver — Judah\'s word at Gen 49:10, the well\'s at 21:18, Gad\'s at Deut 33:21 (Onkelos: the scribes)'),
    ('Mishnah Avot 5:6 — the well\'s mouth', lambda: well_and_kings({'ask': 'well_mouth'}, DATA), 'the well\'s mouth created at twilight — the second of the ten (Avot 5:6)'),
    ('Nedarim 55a:9; Eruvin 54a:21; Num 21:18-20 — the stations as the ladder', lambda: well_and_kings({'ask': 'mattanah_reading'}, DATA), 'the stations as the Torah\'s ladder — the gift, the inheritance, the heights, the valley (Nedarim 55a; Eruvin 54a)'),
    ('Bava Metzia 56b:4-7; Num 21:26 — from his hand', lambda: well_and_kings({'ask': 'from_his_hand'}, DATA), '"from his hand" = from his possession (Bava Metzia 56b)'),
    ('Chullin 60b:13; Gittin 38a; Num 21:26; Deut 2:9 — purified through Sihon', lambda: well_and_kings({'ask': 'sihon_purified'}, DATA), 'Ammon and Moab purified through Sihon — Israel\'s title by his conquest (Chullin 60b; Deut 2:9)'),
    ('Chullin 60b; Bava Batra 78b:12; Num 21:27 — the parable-tellers', lambda: well_and_kings({'ask': 'parable_tellers'}, DATA), 'the parable-tellers — Balaam and Beor (Chullin 60b); the homily on the inclination (Bava Batra 78b)'),
    ('Jer 48:45-46 quoting Num 21:28-29 (computed)', lambda: well_and_kings({'ask': 'jeremiah_quote'}, DATA), 'Jeremiah 48:45-46 quotes 21:28-29 — the parable-tellers\' song in the prophet (computed)'),
    ('Num 21:24; Deut 2:19, 2:37 — Ammon\'s border', lambda: well_and_kings({'ask': 'ammon_border'}, DATA), 'Ammon\'s border strong here, commanded off-limits at Deut 2:19, 2:37'),
    ('Num 21:24-35 — the land east of the Jordan (CM10)', lambda: well_and_kings({'ask': 'land_east'}, DATA), 'the land east of the Jordan possessed — Sihon\'s from Arnon to Jabbok, Jazer, Og\'s Bashan (21:24-35); chapter 32\'s status'),
    ('Num 21:32; Josh 14:7; 13:2 — the spy-verb', lambda: well_and_kings({'ask': 'spy_verb'}, DATA), '"to spy out Jazer" — Caleb\'s verb (Josh 14:7), not the spies\' "tour" (13:2)'),
    ('Niddah 61a:18; Zevachim 113b:12; Deut 3:11 — Og\'s lore (the bed computed)', lambda: well_and_kings({'ask': 'og_lore'}, DATA), 'Og — Sihon\'s brother of the Rephaim, the flood\'s survivor by the lore; his bed nine by four (Deut 3:11)'),
    ('Deut 3:1-3 against Num 21:33-35 — the retelling\'s delta (computed)', lambda: well_and_kings({'ask': 'deut3_delta'}, DATA), 'Deuteronomy 3:1-3 = 21:33-35 with the pronouns shifted — we for they, "to me" for "to Moses" (computed)'),
    ('Num 21:35; Josh 8:22, 10:33; 2 Kgs 10:11 — Joshua\'s refrain (computed)', lambda: well_and_kings({'ask': 'joshua_refrain'}, DATA), '"until no survivor was left" — born at 21:35, Joshua\'s refrain (8:22, 10:33), 2 Kgs 10:11'),
    ('Deut 2:30; Judg 11:20; Num 21:23 — Sihon refused', lambda: well_and_kings({'ask': 'sihon_refused'}, DATA), 'Sihon refused the passage and came to Jahaz — hardened (Deut 2:30)'),
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
    print('\nCHUKAT: %d/%d cells; the scene %s; the narrative %s' % (ok, len(CASES), SCENE, NARRATIVE))
    sys.exit(0 if ok == len(CASES) else 1)

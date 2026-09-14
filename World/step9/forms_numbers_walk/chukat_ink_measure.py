import os as _os, sys as _sys
_sys.path.insert(0, '<repo-old>/World/step9')
import sqlite3, sys, io, re, contextlib
from fractions import Fraction
import effects_layer as FX
import world_engine as WE

HERE = '<repo-old>/World/step9'
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
JER = set(verse_text(48, 45, book='Jer').split()) & set(verse_text(21, 28).split()); assert len(JER) >= 5, JER   # Jeremiah 48:45 quotes 21:28 (the hand had reversed chapter and verse in five calls — read off the assert driver, 2026-09-11)
MERIBAH_17 = set(verse_text(17, 2, book='Exod').split()) | set(verse_text(17, 3, book='Exod').split())
FIRST_MERIBAH_CLAUSES = [w for w in ('וירב', 'העליתנו', 'ממצרים') if w in verse_text(20, 3).split() + verse_text(20, 5).split() and w in MERIBAH_17]
assert FIRST_MERIBAH_CLAUSES == ['וירב', 'העליתנו', 'ממצרים'], FIRST_MERIBAH_CLAUSES   # the first Meribah's clauses at the second
FIRSTFRUITS = [w for w in ('ונצעק', 'וירעו') if w in verse_text(20, 15).split() + verse_text(20, 16).split()]
assert 'ונצעק' in FIRSTFRUITS and 'ונצעק' in verse_text(26, 7, book='Deut').split(), FIRSTFRUITS   # "and we cried" — Deut 26:7's clause in the Edom letter

print("MERIBAH", len(MERIBAH_SEATS), MERIBAH_SEATS)
print("JER", len(JER), sorted(JER))
print("FMC", FIRST_MERIBAH_CLAUSES, "FF", FIRSTFRUITS, "LAW", LAWGIVER)

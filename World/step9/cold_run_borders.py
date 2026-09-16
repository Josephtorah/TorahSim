import os as _os
_ROOT = _os.path.normpath(_os.path.join(_os.path.dirname(_os.path.abspath(__file__)), '..', '..'))   # THE PORTABLE REPO (2026-09-15): the repo root from this file's own place
#!/usr/bin/env python3
# NUM 34:1-29 — THE BORDERS (THE NUMBERS WALK sitting 14b, 2026-09-13; World/step9/NUMBERS_WALK.md "Sitting 14b"; the state doc's #156).
# THE LAND'S EXTENT AS ONE STATUS ON THE LAND: the spec of the four sides (34:1-12 — south, west, north, east in the ink's order, the Salt Sea at
# both ends of the loop, "by its borders" the inclusio) written as borders_declared on the land of Canaan (the standing place entity), its value
# THE FOUR SIDES — a DATA row built from the DB at import (the named points by side with their seats: Joshua 15:1-4 Judah's run of the south,
# Ezekiel 47 the kin), the second Mount Hor the chukat runner's row; nothing on the people ("shall fall TO YOU" is the lot's debit of 26:52-56,
# open, cited by CALL). MOSES' RESTATEMENT (34:13-15) WRITES NOTHING — the nine and a half a RUN CITATION of the Gad runner's grant on the tape
# (32:33's three transfers, 110,580 by CALL), Joshua 14:2's receipt outside the Torah; its form "and Moses commanded the children of Israel"
# 36:5's (the installing act command_relayed — the second pass's D2 question). THE DIVIDERS NAMED (34:16-29) — the party 32:28 charged as a body
# gets its roster: dividers_named (a status valued the twelve) and commanded (a debit to divide, OPEN BY DESIGN to Joshua 14:1, 19:51) on the
# dividers of the land, AND TWELVE NAMED ROWS in the population table (the register gate's Num 34 seat PAID — the first register reached since the
# table was built at 26). Five cells; every token probed (zero-report law); effects on every cell (the effects law); the parameters the ink
# leaves open recorded in DATA with their arms. Reading ledger: logic/oral_triage/num_34_borders_2026-09-12.md; the exam's docket:
# logic/oral_triage/num_34_borders_exam_2026-09-13.md (171 rows: LAW 3 / DERIVATION 23 / DISPUTE 16 / CONTEXT 129).

# ---- THE HONEST-PAIRING GUARD ----------------------------------------------------------------------------
import os as _os, sys as _sys
_sys.path.insert(0, _os.path.dirname(_os.path.abspath(__file__)))
from compile_guards import check_honest_pairing as _chp
_P = _os.path.abspath(__file__)
GUARDED = _chp(_P, 'CASES', 2)
assert GUARDED == 56, ("the guard counted %d expectations, the tripwire holds 56" % GUARDED)   # the design's estimate — retyped from the guard's print after the first run
print('guard: %d expectations checked, every one a literal from the answer sheet [honest-pairing guard satisfied]' % GUARDED)
import sqlite3, sys, io, re, contextlib, collections, unicodedata, yaml
import effects_layer as FX
import world_engine as WE
import cold_run_second_census as C2              # THE EDGE: borders -> second_census CALL, reference (34:2's "shall fall as an inheritance" and 34:13's "inherit by lot" — 26:52-56's own words; the lot's debit cited; "only" excludes the two dividers' portions)
import cold_run_gad_reuben as GR                 # THE EDGE: borders -> gad_reuben CALL, reference (34:14-15's "have taken their inheritance" — 32:33's grant on the tape; 34:17's triad — 32:28's charge)
import cold_run_shelach as SL                    # THE EDGE: borders -> shelach CALL, reference (Caleb's five words 13:6; the spies' range 13:21; the doubling 13:2; the two survivors)
import cold_run_chukat as CK                     # THE EDGE: borders -> chukat CALL, reference (the second Mount Hor — the runner's row names 34:7-8)
import cold_run_bamidbar as CB                   # THE EDGE: borders -> bamidbar CALL, reference (the roll's form and order; no prince of chapter 1; Ammihud)
import cold_run_naso as NS                       # THE EDGE: borders -> naso CALL, reference (7:11's doubling; the twelve princes' names; the sotah's 5:23 blot — a homograph by sense, FALSE for its rule)
import cold_run_korach as KR                     # THE EDGE: borders -> korach CALL, reference (17:21's rods by prince and tribe)
import cold_run_zelophehad as ZL                 # THE EDGE: borders -> zelophehad CALL, reference (Eleazar and Joshua the court that owes the daughters' holding; 27:19-22)
import cold_run_journeys as JO                   # THE EDGE: borders -> journeys CALL, reference (33:51's entry clause; 33:54's lot restated)

HERE = _os.path.dirname(_os.path.abspath(__file__))
# ONE copy of the numeral parser: the sequence runner's INK block executed here (the stitcher's way — no import edge)
_SRC = open(_os.path.join(HERE, 'cold_run_sequence.py'), encoding='utf-8').read()
_INK = {'re': re, 'sqlite3': sqlite3, 'os': _os, 'WE': WE}
_INK['_ROOT'] = _ROOT   # THE PORTABLE REPO (2026-09-15): the INK block reads the store through the root; the exec'd namespace must carry it
exec(_SRC.split('# ==== INK BEGIN')[1].split('# ==== INK END ====')[0].split('\n', 1)[1], _INK)
ink_numbers, ink_ordinals, verse_words = _INK['ink_numbers'], _INK['ink_ordinals'], _INK['verse_words']
from fractions import Fraction   # THE DEUTERONOMY WALK 1b (2026-09-15): the half read by rule (30) is a Fraction in the tripwire

db = sqlite3.connect((_ROOT + '/Data/tanakh.sqlite'))

def strip(s):
    return ''.join(c for c in s if c != '/' and not (0x0591 <= ord(c) <= 0x05C7))
NF = lambda s: unicodedata.normalize('NFC', s)                                                   # THE MARKS' ORDER: every pointed comparison on NFC both sides (sitting 14's lesson)

def verse_text(ch, vs, book='Num'):
    rows = db.execute("""SELECT w.he FROM words w JOIN verses v ON w.verse_id=v.id WHERE v.book=?
        AND v.chapter=? AND v.verse=? ORDER BY w.idx""", (book, ch, vs)).fetchall()
    return ' '.join(strip(h) for (h,) in rows)

def words(ch, vs, book='Num'):
    return verse_text(ch, vs, book).split()

# ---- zero-report probes: the span's load-bearing tokens (every one measured on the DB before it was typed — bor_runner_measure.out, 2026-09-13) ----
PROBES = [
    ('וידבר',     34, 1,  'and [the LORD] spoke — the first frame (34:16 the second, the same five words)'),
    ('לאמר',      34, 1,  'saying'),
    ('צו',        34, 2,  'command — the five Torah seats; the Sifrei 1:2\'s one without expense'),
    ('באים',      34, 2,  '[you are] coming — the participle'),
    ('כנען',      34, 2,  'Canaan — the article on the land, none on the name'),
    ('זאת',       34, 2,  'this [is the land] — 34:13 and Deuteronomy 34:4'),
    ('תפל',       34, 2,  'shall fall — the lot\'s verb; Onkelos "be divided"'),
    ('בנחלה',     34, 2,  'as an inheritance — three Torah seats'),
    ('לגבלתיה',   34, 2,  'by its borders — the inclusio (34:12)'),
    ('פאת',       34, 3,  'side — the tabernacle\'s word'),
    ('נגב',       34, 3,  'south'),
    ('ממדבר',     34, 3,  'from the wilderness of [Zin] — 13:21'),
    ('צן',        34, 3,  'Zin'),
    ('אדום',      34, 3,  'Edom — on the hands of Edom'),
    ('גבול',      34, 3,  'border — sixteen in the chapter'),
    ('המלח',      34, 3,  'the Salt [Sea] — the loop\'s two ends'),
    ('קדמה',      34, 3,  'eastward'),
    ('ונסב',      34, 4,  'and it shall turn'),
    ('עקרבים',    34, 4,  'Akrabbim — Joshua 15:3, Judges 1:36'),
    ('צנה',       34, 4,  'to Zin — the directional ending'),
    ('והיה',      34, 4,  'and it shall be — THE WRITTEN SINGULAR read plural (unpointed in the DB)'),
    ('תוצאתיו',   34, 4,  'its goings-out — the Torah\'s five seats all here'),
    ('ברנע',      34, 4,  '[Kadesh-]barnea — Onkelos "Rekem Geah"'),
    ('ויצא',      34, 4,  'and it shall go out'),
    ('חצר',       34, 4,  'Hazar[-addar] — split into Hezron and Addar at Joshua 15:3'),
    ('אדר',       34, 4,  '[Hazar-]addar'),
    ('עצמנה',     34, 4,  'to Azmon — defective; Joshua 15:4 plene'),
    ('מעצמון',    34, 5,  'from Azmon'),
    ('נחלה',      34, 5,  'the brook of [Egypt] — the inheritance\'s consonants'),
    ('מצרים',     34, 5,  'Egypt'),
    ('הימה',      34, 5,  'at the sea — the south\'s goings-out'),
    ('וגבול',     34, 6,  'and the border — Gittin 8a:7\'s word'),
    ('ים',        34, 6,  'the sea / the west — one token, seven times'),
    ('הים',       34, 6,  'the sea — the great sea'),
    ('הגדול',     34, 6,  'the great — plene; 34:7 defective'),
    ('הגדל',      34, 7,  'the great — defective'),
    ('צפון',      34, 7,  'north — the store\'s "hidden"'),
    ('תתאו',      34, 7,  'you shall mark out — three Bible seats all here; Proverbs\' "desire" the homograph'),
    ('הר',        34, 7,  'Mount [Hor] — the second Mount Hor'),
    ('ההר',       34, 7,  'Hor'),
    ('מהר',       34, 8,  'from Mount [Hor]'),
    ('לבא',       34, 8,  'Lebo[-hamath] — defective, 13:21\'s'),
    ('חמת',       34, 8,  'Hamath'),
    ('תוצאת',     34, 8,  'the goings-out of — the bare form'),
    ('הגבל',      34, 8,  'the border — defective'),
    ('צדדה',      34, 8,  'to Zedad — Ezekiel 47:15'),
    ('זפרנה',     34, 9,  'to Ziphron — one seat'),
    ('עינן',      34, 9,  '[Hazar-]enan — Ezekiel 48:1'),
    ('והתאויתם',  34, 10, 'and you shall mark out for yourselves — the Hitpael, one seat'),
    ('לגבול',     34, 10, 'for the border'),
    ('מחצר',      34, 10, 'from Hazar[-enan]'),
    ('שפמה',      34, 10, 'to Shepham'),
    ('וירד',      34, 11, 'and it shall go down'),
    ('משפם',      34, 11, 'from Shepham'),
    ('הרבלה',     34, 11, 'the Riblah — with the article, one seat'),
    ('מקדם',      34, 11, 'east of'),
    ('לעין',      34, 11, 'Ain'),
    ('ומחה',      34, 11, 'and it shall reach — the blotting verb (5:23)'),
    ('כתף',       34, 11, 'the shoulder of — the ephod\'s word'),
    ('כנרת',      34, 11, 'Chinnereth — Onkelos "Gennesar"'),
    ('הירדנה',    34, 12, 'to the Jordan — with the article and the ending'),
    ('סביב',      34, 12, 'round about'),
    ('ויצו',      34, 13, 'and [Moses] commanded — the relay; 36:5 the other seat of the phrase'),
    ('תתנחלו',    34, 13, 'you shall inherit — the reflexive stem'),
    ('בגורל',     34, 13, 'by lot — 26:55\'s'),
    ('לתשעת',     34, 13, 'to the nine of — the construct; Joshua 13:7, 14:2'),
    ('המטות',     34, 13, 'the tribes — the staff-word, the chapter\'s one tribe-noun'),
    ('וחצי',      34, 13, 'and the half'),
    ('לקחו',      34, 14, 'have taken — "took their inheritance", four Bible seats'),
    ('הראובני',   34, 14, 'the Reubenite'),
    ('הגדי',      34, 14, 'the Gadite — Genesis 38:23\'s "kid" the homograph'),
    ('מנשה',      34, 14, 'Manasseh'),
    ('נחלתם',     34, 14, 'their inheritance'),
    ('שני',       34, 15, 'the two of — the construct (the caret)'),
    ('מעבר',      34, 15, 'beyond — from beyond'),
    ('ירחו',      34, 15, 'Jericho — 22:1\'s phrase; Bekhorot 55a:14\'s hinge'),
    ('מזרחה',     34, 15, 'toward the sunrise — the court\'s east side'),
    ('אלה',       34, 17, 'these are — the rosters\' heading'),
    ('שמות',      34, 17, 'the names of'),
    ('האנשים',    34, 17, 'the men'),
    ('ינחלו',     34, 17, 'who shall divide — the plain stem'),
    ('אלעזר',     34, 17, 'Eleazar'),
    ('הכהן',      34, 17, 'the priest'),
    ('ויהושע',    34, 17, 'and Joshua'),
    ('נון',       34, 17, 'Nun'),
    ('ונשיא',     34, 18, 'and a prince — one prince, one prince: the distributive doubling'),
    ('אחד',       34, 18, 'one — [1, 1]'),
    ('ממטה',      34, 18, 'from a tribe'),
    ('תקחו',      34, 18, 'you shall take — Kiddushin 42a\'s verse'),
    ('לנחל',      34, 18, 'to divide — the plain infinitive (34:29 the intensive\'s, one skin)'),
    ('ואלה',      34, 19, 'and these are'),
    ('יהודה',     34, 19, 'Judah — first'),
    ('כלב',       34, 19, 'Caleb — 13:6\'s five words'),
    ('יפנה',      34, 19, 'Jephunneh'),
    ('שמעון',     34, 20, 'Simeon'),
    ('שמואל',     34, 20, 'Shemuel — the prophet\'s name\'s first seat'),
    ('עמיהוד',    34, 20, 'Ammihud — three tribes\' fathers\' name'),
    ('בנימן',     34, 21, 'Benjamin'),
    ('אלידד',     34, 21, 'Elidad — one seat'),
    ('כסלון',     34, 21, 'Chislon — Joshua 15:10\'s Chesalon'),
    ('דן',        34, 22, 'Dan'),
    ('נשיא',      34, 22, 'a prince — the title at seven rows'),
    ('בקי',       34, 22, 'Bukki'),
    ('יגלי',      34, 22, 'Jogli — one seat'),
    ('יוסף',      34, 23, 'Joseph — the heading over Manasseh'),
    ('חניאל',     34, 23, 'Hanniel'),
    ('אפד',       34, 23, 'Ephod — the vestment\'s consonants'),
    ('אפרים',     34, 24, 'Ephraim — after Manasseh'),
    ('קמואל',     34, 24, 'Kemuel — Nahor\'s son\'s name'),
    ('שפטן',      34, 24, 'Shiphtan — one seat'),
    ('זבולן',     34, 25, 'Zebulun — before Issachar'),
    ('אליצפן',    34, 25, 'Elizaphan — the Kohathite prince\'s name'),
    ('פרנך',      34, 25, 'Parnach — one seat'),
    ('יששכר',     34, 26, 'Issachar'),
    ('פלטיאל',    34, 26, 'Paltiel — Michal\'s husband\'s name'),
    ('עזן',       34, 26, 'Azzan — one seat'),
    ('אשר',       34, 27, 'Asher'),
    ('אחיהוד',    34, 27, 'Ahihud — one seat'),
    ('שלמי',      34, 27, 'Shelomi — "my peace-offerings" the homograph'),
    ('נפתלי',     34, 28, 'Naphtali — last'),
    ('פדהאל',     34, 28, 'Pedahel — one seat'),
    ('צוה',       34, 29, '[whom the LORD] commanded — the closer'),
    ('בארץ',      34, 29, 'in the land of [Canaan]'),
]
for tok_, ch, vs, note in PROBES:
    if tok_ not in words(ch, vs):
        sys.exit('ZERO-REPORT LAW: probe %r (%s) failed at Num %d:%d — refusing to run' % (tok_, note, ch, vs))
print('probes: all %d token probes fired  [zero-report law satisfied]\n' % len(PROBES))

P = []  # the provenance trail of the case being run

def ink(ref, note):  P.append(('INK',  'Num %s — %s' % (ref, note)))
def move(src, note): P.append(('MOVE', '%s — %s' % (src, note)))
def dat(note):       P.append(('DATA', note))
def hyp(note):       P.append(('HYP',  note))     # THE LINK REVIEW LAW: a hypothesis — no teacher; counted apart, never as compiled

def out(verdict, effects):
    """verdict + registry-validated effects (the engine contract)"""
    FX.validate([e for e in effects if e != FX.NONE])
    return verdict, effects, list(P)

# ---- THE INK, computed (the parser and the tokens; the reading's facts the expectations) ----
SPAN = [(34, v) for v in range(1, 30)]
NUMBERS = {v: ink_numbers(verse_words('Num', 34, v)) for _, v in SPAN}
ORDINALS = {v: ink_ordinals(verse_words('Num', 34, v)) for _, v in SPAN}
STARRED = [(v, t) for _, v in SPAN for t in verse_words('Num', 34, v) if t.endswith('*')]
CARET = [(v, t) for _, v in SPAN for t in verse_words('Num', 34, v) if t.endswith('^')]
INTS = {v: n for v, n in NUMBERS.items() if n}; ORDS = {v: o for v, o in ORDINALS.items() if o}
assert INTS == {13: [9, Fraction(1, 2)], 14: [Fraction(1, 2)], 15: [2, Fraction(1, 2)], 18: [1, 1]} and ORDS == {} and STARRED == [] and CARET == [(15, 'שני^')], (INTS, ORDS, STARRED, CARET)   # THE DEUTERONOMY WALK 1b (2026-09-15): rule (30) THE HALF OF A NAMED WHOLE reads the half tribe at 34:13, 34:14, 34:15 — nine and a half, two and a half; before it THREE number verses in twenty-nine — every one read; the construct "two of" by its points; THE DISTRIBUTIVE DOUBLING as two ones; no rule owed
NINE, TWO, ONE_ONE = INTS[13][0], INTS[15][0], INTS[18]
assert ink_numbers(verse_words('Num', 35, 1)) == [] and ink_ordinals(verse_words('Num', 35, 1)) == [], 'the next chapter opens without a number'
FRAME_VERBS = [(v, words(34, v)[0], words(34, v)[1]) for _, v in SPAN if words(34, v)[0] in ('וידבר', 'ויאמר', 'ויאמרו', 'ויענו', 'ויצו')]
assert FRAME_VERBS == [(1, 'וידבר', 'יהוה'), (13, 'ויצו', 'משה'), (16, 'וידבר', 'יהוה')], FRAME_VERBS                               # TWO divine frames with MOSES' OWN COMMAND between them
assert words(34, 1) == words(34, 16) == ['וידבר', 'יהוה', 'אל', 'משה', 'לאמר'] and words(35, 1) == ['וידבר', 'יהוה', 'אל', 'משה', 'בערבת', 'מואב', 'על', 'ירדן', 'ירחו', 'לאמר'], (words(34, 1), words(34, 16), words(35, 1))   # the same five words at both; 35:1 adds the plains of Moab
# the whole-DB phrase census (the seats typed from the measurement print of 2026-09-13 — bor_runner_measure.out)
_V = collections.OrderedDict(); _L = collections.OrderedDict(); _M = collections.OrderedDict(); _PT = collections.OrderedDict()
for b, c, v, he, lm, mo in db.execute("SELECT v.book, v.chapter, v.verse, w.he, w.lemma, w.morph FROM words w JOIN verses v ON w.verse_id=v.id ORDER BY v.id, w.idx"):
    _V.setdefault((b, c, v), []).append(strip(he)); _L.setdefault((b, c, v), []).append((lm.split('/')[-1].split(' ')[0] if lm else '').rstrip('+')); _M.setdefault((b, c, v), []).append(mo or ''); _PT.setdefault((b, c, v), []).append(NF(he.replace('/', '')))
def seats(phrase, books=None):
    p = phrase.split(); n = len(p)
    return ['%s %d:%d' % k for k, ws in _V.items() if (books is None or k[0] in books) and any(ws[i:i + n] == p for i in range(len(ws) - n + 1))]
def rx(pattern, books=None):
    r = re.compile(pattern)
    return ['%s %d:%d' % k for k, ws in _V.items() if (books is None or k[0] in books) and r.search(' ' + ' '.join(ws) + ' ')]
def tok(t, books=None):
    return ['%s %d:%d' % k for k, ws in _V.items() if (books is None or k[0] in books) and t in ws]
def lemma_seats(lm, books=None):
    return ['%s %d:%d' % k for k, ls in _L.items() if (books is None or k[0] in books) and lm in ls]
TORAH = ('Gen', 'Exod', 'Lev', 'Num', 'Deut')
# ---- F1's facts: the land and its fall ----
COMMAND = seats('צו את בני ישראל'); THIS_LAND = seats('זאת הארץ'); FALL_TO_YOU = seats('אשר תפל לכם'); FALL = seats('תפל'); FALL_T = seats('תפל', TORAH)
assert COMMAND == ['Lev 24:2', 'Num 5:2', 'Num 28:2', 'Num 34:2', 'Num 35:2'], COMMAND                                                # THE FIVE "command the children of Israel" — the Sifrei 1:2's five, this the one without expense
assert THIS_LAND == ['Deut 34:4', 'Ezek 48:29', 'Josh 13:2', 'Num 34:2', 'Num 34:13'] and FALL_TO_YOU == ['Num 34:2'], (THIS_LAND, FALL_TO_YOU)
assert len(FALL) == 14 and FALL_T == ['Deut 1:1', 'Exod 15:16', 'Num 34:2'], (len(FALL), FALL_T)                                     # "shall fall" with the inheritance one Torah seat (Deuteronomy 1:1's Tophel a place, Exodus 15:16's "fall upon them")
INHERITANCE_T = seats('בנחלה', TORAH); BY_ITS_BORDERS = seats('לגבלתיה'); BY_ITS_BORDERS_JOSH = seats('לגבולתיה'); LAND_CANAAN_ART = seats('הארץ כנען'); LAND_CANAAN_T = seats('ארץ כנען', TORAH)
assert INHERITANCE_T == ['Num 26:53', 'Num 34:2', 'Num 36:2'] and BY_ITS_BORDERS == ['Num 34:2', 'Num 34:12'] and BY_ITS_BORDERS_JOSH == ['Josh 18:20', 'Josh 19:49'], (INHERITANCE_T, BY_ITS_BORDERS, BY_ITS_BORDERS_JOSH)   # THE INCLUSIO and Joshua's two closers
assert LAND_CANAAN_ART == ['Num 34:2'] and len(LAND_CANAAN_T) == 13 and {'Num 13:2', 'Num 33:51', 'Num 34:2', 'Gen 17:8'} <= set(LAND_CANAAN_T), (LAND_CANAAN_ART, LAND_CANAAN_T)   # "THE LAND Canaan" — the article on the land, none on the name: ONE Bible seat (the first run read: the bare pair's thirteen Torah seats are another census)
assert words(34, 2)[9:12] == ['אל', 'הארץ', 'כנען'] and words(34, 2)[12:14] == ['זאת', 'הארץ'], words(34, 2)
def _stem_border(t):
    t2 = t
    for pfx in ('ו', 'ל', 'ה'):
        if t2.startswith(pfx) and len(t2) > 3: t2 = t2[1:]
    if t2.startswith('ה') and len(t2) > 3: t2 = t2[1:]
    return t2.startswith('גבל') or t2.startswith('גבול')
BORDER_TOKENS = [(v, t) for _, v in SPAN for t in words(34, v) if _stem_border(t)]
assert len(BORDER_TOKENS) == 16 and BORDER_TOKENS[0] == (2, 'לגבלתיה') and BORDER_TOKENS[-1] == (12, 'לגבלתיה'), BORDER_TOKENS       # THE BORDER-WORD SIXTEEN TIMES in the chapter (the reading: half of Numbers' thirty-two)
BORDER_NUM = sum(1 for (b, c, v), ws in _V.items() if b == 'Num' for t in ws if _stem_border(t))
SHALL_BE = [(v, t) for v in range(2, 13) for t in words(34, v) if t in ('והיה', 'והיו', 'וירד', 'ונסב', 'ועבר', 'ויצא', 'ואמרת', 'והתאויתם', 'ומחה')]
assert len(SHALL_BE) == 20, SHALL_BE                                                                                                    # THE BORDER RUNS ON TWENTY "and it shall" verbs (34:2-12)
TO_YOU = [(v, i) for _, v in SPAN for i, t in enumerate(words(34, v)) if t == 'לכם']
assert len(TO_YOU) == 12 and 'לכם' in words(15, 4, 'Josh'), TO_YOU                                                                     # "to you" twelve times; JOSHUA 15:4 KEEPS ONE "to you" inside Judah's border
# ---- F2's facts: the four sides ----
SOUTH_SIDE = seats('פאת נגב'); WILD_ZIN = seats('ממדבר צן'); HANDS_EDOM = seats('על ידי אדום'); END_SALT = seats('מקצה ים המלח'); SALT_SEA = seats('ים המלח')
assert SOUTH_SIDE == ['Ezek 48:28', 'Num 34:3', 'Num 35:5'] and WILD_ZIN == ['Num 13:21', 'Num 34:3'] and HANDS_EDOM == ['Num 34:3'], (SOUTH_SIDE, WILD_ZIN, HANDS_EDOM)   # "from the wilderness of Zin" with that prefix: 13:21 and here — THE SPIES WALKED THE BORDER'S LENGTH
assert END_SALT == ['Josh 15:2', 'Num 34:3'] and SALT_SEA == ['Deut 3:17', 'Gen 14:3', 'Josh 3:16', 'Josh 12:3', 'Josh 15:2', 'Josh 15:5', 'Josh 18:19', 'Num 34:3', 'Num 34:12'], (END_SALT, SALT_SEA)   # THE LOOP: the Salt Sea at 34:3 and 34:12; Genesis 14:3's identity clause
EASTWARD = seats('קדמה'); EASTWARD_34 = [s for s in EASTWARD if s.startswith('Num 34:')]
assert len(EASTWARD) == 27 and EASTWARD_34 == ['Num 34:3', 'Num 34:10', 'Num 34:11', 'Num 34:15'], (len(EASTWARD), EASTWARD_34)
AKRABBIM = seats('למעלה עקרבים'); KADESH_BARNEA_BARE = seats('קדש ברנע'); BARNEA_LEMMA = lemma_seats('6947'); HAZAR_ADDAR = seats('חצר אדר'); AZMON = seats('עצמנה'); AZMON_JOSH = seats('עצמונה'); AZMON_LEMMA = lemma_seats('6111')
assert AKRABBIM == ['Josh 15:3', 'Num 34:4'] and KADESH_BARNEA_BARE == ['Deut 1:2', 'Deut 1:19'] and BARNEA_LEMMA == ['Deut 1:2', 'Deut 1:19', 'Deut 2:14', 'Deut 9:23', 'Josh 10:41', 'Josh 14:6', 'Josh 14:7', 'Josh 15:3', 'Num 32:8', 'Num 34:4'], (AKRABBIM, KADESH_BARNEA_BARE, BARNEA_LEMMA)   # Kadesh-barnea ten seats by lemma
assert HAZAR_ADDAR == ['Num 34:4'] and 'חצרון' in words(15, 3, 'Josh') and 'אדרה' in words(15, 3, 'Josh'), (HAZAR_ADDAR, words(15, 3, 'Josh'))   # JOSHUA SPLITS HAZAR-ADDAR into Hezron and Addar
assert AZMON == ['Num 34:4'] and AZMON_JOSH == ['Josh 15:4'] and AZMON_LEMMA == ['Josh 15:4', 'Num 34:4', 'Num 34:5'], (AZMON, AZMON_JOSH, AZMON_LEMMA)   # Azmon defective here, plene in Joshua
BROOK = seats('נחלה מצרים'); BROOK_KINGS = seats('נחל מצרים'); GOINGS = seats('תוצאתיו'); GOINGS_BARE = seats('תוצאת'); AT_THE_SEA = seats('הימה')
assert BROOK == ['Num 34:5'] and BROOK_KINGS == ['1Kgs 8:65', '2Chr 7:8', 'Isa 27:12', 'Josh 15:4', 'Josh 15:47'], (BROOK, BROOK_KINGS)   # "the brook of Egypt" — 1 Kings 8:65 "from Lebo-hamath to the brook of Egypt" the kingdom's measure by the chapter's two ends
assert GOINGS == ['Num 34:4', 'Num 34:5', 'Num 34:9', 'Num 34:12'] and 'Num 34:8' in GOINGS_BARE and len(AT_THE_SEA) == 9 and {'Num 34:5', 'Josh 15:12'} <= set(AT_THE_SEA), (GOINGS, GOINGS_BARE, AT_THE_SEA)   # THE GOINGS-OUT: four suffixed + the bare at 34:8 = the Torah's five, all here
GOINGS_JOSH = rx(r' ת[ו]?צא[ו]?ת', ('Josh',))
assert words(34, 4)[8] == 'והיה' and _PT[('Num', 34, 4)][8] == 'והיה', (words(34, 4)[8], _PT[('Num', 34, 4)][8])                          # THE ONE WRITTEN SINGULAR READ PLURAL — the DB writes the written form UNPOINTED
assert words(34, 5)[3:5] == ['נחלה', 'מצרים'] and words(34, 2)[17] == 'בנחלה', (words(34, 5), words(34, 2))                                # the brook's consonants the inheritance's
WEST_BORDER = seats('גבול ים'); GREAT_SEA = seats('הים הגדול'); GREAT_SEA_DEF = seats('הים הגדל'); AND_ITS_BORDER = seats('וגבול'); NORTH_BORDER = seats('גבול צפון')
assert WEST_BORDER == ['Num 34:6'] and GREAT_SEA == ['Ezek 47:10', 'Ezek 47:15', 'Ezek 47:19', 'Ezek 47:20', 'Ezek 48:28', 'Josh 1:4', 'Josh 9:1', 'Num 34:6'] and GREAT_SEA_DEF == ['Num 34:7'], (WEST_BORDER, GREAT_SEA, GREAT_SEA_DEF)   # THE GREAT SEA plene at 34:6, defective at 34:7
assert len(AND_ITS_BORDER) == 12 and {'Num 34:6', 'Josh 15:12', 'Ezek 47:17'} <= set(AND_ITS_BORDER) and NORTH_BORDER == ['Num 34:7', 'Num 34:9'], (AND_ITS_BORDER, NORTH_BORDER)
SEA_TOKENS = [(v, t) for _, v in SPAN for t in words(34, v) if t in ('ים', 'הים')]
assert len(SEA_TOKENS) == 7, SEA_TOKENS                                                                                                 # THE SEA AS THE WEST — one token seven times (Onkelos splits)
MARK = seats('תתאו'); MARK_HIT = seats('והתאויתם'); HOR = seats('הר ההר'); HOR_LEMMA = lemma_seats('2023'); LEBO = seats('לבא חמת'); ZEDAD = seats('צדדה'); ZIPHRON = seats('זפרנה'); HAZAR_ENAN = seats('חצר עינן'); HAZAR_ENON = seats('חצר עינון'); ENAN_LEMMA = lemma_seats('2704')
assert MARK == ['Num 34:7', 'Num 34:8', 'Prov 23:3', 'Prov 23:6', 'Prov 24:1'] and MARK_HIT == ['Num 34:10'], (MARK, MARK_HIT)          # "you shall mark out" — three Bible seats all here; Proverbs' "do not desire" the homograph by the points
assert HOR == ['Num 20:22', 'Num 20:25', 'Num 20:27', 'Num 33:38', 'Num 34:7'] and HOR_LEMMA == ['Deut 32:50', 'Num 20:22', 'Num 20:23', 'Num 20:25', 'Num 20:27', 'Num 21:4', 'Num 33:37', 'Num 33:38', 'Num 33:39', 'Num 33:41', 'Num 34:7', 'Num 34:8'], (HOR, HOR_LEMMA)   # MOUNT HOR twelve Torah seats — ten Aaron's, TWO the north border's
HOR_AARON = [s for s in HOR_LEMMA if not s.startswith('Num 34:')]; HOR_BORDER = [s for s in HOR_LEMMA if s.startswith('Num 34:')]
assert len(HOR_AARON) == 10 and HOR_BORDER == ['Num 34:7', 'Num 34:8'], (HOR_AARON, HOR_BORDER)
assert LEBO == ['Num 13:21', 'Num 34:8'] and ZEDAD == ['Ezek 47:15', 'Num 34:8'] and ZIPHRON == ['Num 34:9'] and HAZAR_ENAN == ['Ezek 48:1', 'Num 34:9'] and HAZAR_ENON == ['Ezek 47:17'] and ENAN_LEMMA == ['Ezek 48:1', 'Num 34:9', 'Num 34:10'], (LEBO, ZEDAD, ZIPHRON, HAZAR_ENAN, HAZAR_ENON, ENAN_LEMMA)   # defective "Lebo-hamath" at 13:21 and here alone
EAST_BORDER = seats('לגבול קדמה'); SHEPHAM = seats('שפמה'); SHEPHAM_LEMMA = lemma_seats('8221'); RIBLAH = seats('הרבלה'); RIBLAH_LEMMA = lemma_seats('7247'); AIN = seats('לעין'); AIN_LEMMA = lemma_seats('5871')
assert EAST_BORDER == ['Num 34:10'] and SHEPHAM == ['Num 34:10'] and SHEPHAM_LEMMA == ['Num 34:10', 'Num 34:11'] and RIBLAH == ['Num 34:11'] and len(RIBLAH_LEMMA) == 11 and RIBLAH_LEMMA[-1] == 'Num 34:11', (EAST_BORDER, SHEPHAM, SHEPHAM_LEMMA, RIBLAH, RIBLAH_LEMMA)   # "the Riblah" with the article one seat; the exile's Riblah ten without it
assert AIN == ['Ezek 12:12', 'Num 34:11'] and AIN_LEMMA == ['1Chr 4:32', 'Josh 15:32', 'Josh 19:7', 'Josh 21:16', 'Num 34:11'], (AIN, AIN_LEMMA)   # Ain the place: Ezekiel 12:12's "to the eye" a homograph by token; the lemma's four Joshua and Chronicles seats
SHOULDER_CHIN = seats('כתף ים כנרת'); SEA_CHIN = seats('ים כנרת'); CHIN_LEMMA = lemma_seats('3672'); REACH = seats('ומחה'); TO_JORDAN = seats('הירדנה'); ROUND_NUM = seats('סביב', ('Num',))
assert SHOULDER_CHIN == ['Num 34:11'] and SEA_CHIN == ['Josh 13:27', 'Num 34:11'] and CHIN_LEMMA == ['1Kgs 15:20', 'Deut 3:17', 'Josh 11:2', 'Josh 12:3', 'Josh 13:27', 'Josh 19:35', 'Num 34:11'], (SHOULDER_CHIN, SEA_CHIN, CHIN_LEMMA)   # the sea of Chinnereth two seats; the name seven; Joshua 19:35's Chinnereth in Naphtali
assert REACH == ['Deut 29:19', 'Isa 25:8', 'Num 5:23', 'Num 34:11'], REACH                                                              # "and it shall REACH" IS THE BLOTTING VERB — one pointing at four Bible seats (the sotah's scroll, a name, tears, this border)
assert TO_JORDAN == ['2Kgs 2:6', '2Kgs 6:4', 'Judg 8:4', 'Num 34:12'] and ROUND_NUM == ['Num 1:53', 'Num 2:2', 'Num 3:26', 'Num 3:37', 'Num 4:26', 'Num 4:32', 'Num 32:33', 'Num 34:12', 'Num 35:4'], (TO_JORDAN, ROUND_NUM)
SIDE_T = seats('פאת', TORAH); SIDE_L_T = seats('לפאת', TORAH); SUNRISE = seats('קדמה מזרחה')
assert SIDE_T == ['Lev 19:9', 'Lev 19:27', 'Lev 23:22', 'Num 34:3', 'Num 35:5'] and {'Exod 27:9', 'Exod 27:13'} <= set(SIDE_L_T) and SUNRISE == ['Exod 27:13', 'Exod 38:13', 'Josh 19:13', 'Num 2:3', 'Num 34:15'], (SIDE_T, SIDE_L_T, SUNRISE)   # the bare side-word five Torah seats — the field's corner (Leviticus 19:9, 23:22) and the beard's (19:27) HOMOGRAPHS BY SENSE beside 34:3 and 35:5 (the first run read: the reading's eighteen was the word's family); the court's sides with the prefix (Exodus 27:9, 27:13); "eastward toward the sunrise" the court's east side = 34:15's phrase
assert words(27, 9, 'Exod')[4:7] == ['לפאת', 'נגב', 'תימנה'] and words(27, 13, 'Exod')[2:5] == ['לפאת', 'קדמה', 'מזרחה'], (words(27, 9, 'Exod'), words(27, 13, 'Exod'))
JUDAH_S = [w for v in range(1, 5) for w in words(15, v, 'Josh')]; NUM_S = [w for v in range(3, 6) for w in words(34, v)]
SHARED_S = [w for w in NUM_S if w in JUDAH_S]
assert len(NUM_S) == 43 and len(JUDAH_S) == 56 and len(SHARED_S) == 29, (len(NUM_S), len(JUDAH_S), len(SHARED_S))                          # JUDAH'S SOUTH BORDER IS THE LAND'S — twenty-nine of the forty-three tokens of 34:3-5 stand in Joshua 15:1-4 (with repeats)
EZEK_TOKS = [w for v in range(13, 21) for w in words(47, v, 'Ezek')]; NUM_ALL = [w for _, v in SPAN for w in words(34, v)]
EZEK_SHARED = sorted(set(w for w in NUM_ALL if w in EZEK_TOKS))
assert len(EZEK_SHARED) == 29 and {'תתנחלו', 'בנחלה', 'צדדה', 'חמת', 'הגדול', 'פאת', 'גבול'} <= set(EZEK_SHARED), EZEK_SHARED             # Ezekiel 47:13-20 shares twenty-nine distinct tokens; opens with 34:13's "you shall inherit"
EZEK_SIDES = [(15, 'צפונה'), (18, 'קדים'), (19, 'נגב'), (20, 'ים')]
assert all(t in words(47, v, 'Ezek') for v, t in EZEK_SIDES), 'EZEKIEL\'S ORDER: north (47:15), east (47:18), south (47:19), west (47:20) — against the chapter\'s south, west, north, east'
NUM_POINTS = [(v, w, l) for v in range(3, 13) for w, l, m in zip(_V[('Num', 34, v)], _L[('Num', 34, v)], _M[('Num', 34, v)]) if 'Np' in m]
assert len(NUM_POINTS) == 27 and NUM_POINTS[0][1] == 'צן' and NUM_POINTS[-1][1] == 'הירדנה', (len(NUM_POINTS), NUM_POINTS[:3], NUM_POINTS[-1])   # TWENTY-SEVEN proper-name tokens on the four sides (the print's rows)
def _side(v): return 'south' if 3 <= v <= 5 else 'west' if v == 6 else 'north' if 7 <= v <= 9 else 'east'
SIDES = collections.OrderedDict((s, {'verses': [v for v in range(3, 13) if _side(v) == s], 'points': [(v, w, l, [x for x in lemma_seats(l) if not x.startswith('Num 34:')][:12]) for v, w, l in NUM_POINTS if _side(v) == s]}) for s in ('south', 'west', 'north', 'east'))
SIDES['south']['common'] = ['the Salt Sea (34:3)', 'the brook of Egypt (34:5)', 'the sea (34:5)']; SIDES['west']['common'] = ['the great sea (34:6)']; SIDES['north']['common'] = ['the great sea (34:7)']; SIDES['east']['common'] = ['the sea of Chinnereth (34:11)', 'the Jordan (34:12)', 'the Salt Sea (34:12)']
assert [len(SIDES[s]['points']) for s in SIDES] == [11, 0, 8, 8] and SIDES['west']['verses'] == [6], [len(SIDES[s]['points']) for s in SIDES]   # the west side names no proper name — the great sea alone
SIDES_EN = 'four sides — south (34:3-5): from the wilderness of Zin on the hands of Edom, the end of the Salt Sea eastward, the ascent of Akrabbim, Zin, Kadesh-barnea, Hazar-addar, Azmon, the brook of Egypt, the sea; west (34:6): the great sea and its border; north (34:7-9): from the great sea, Mount Hor, Lebo-hamath, Zedad, Ziphron, Hazar-enan; east (34:10-12): from Hazar-enan, Shepham, Riblah east of Ain, the shoulder of the sea of Chinnereth eastward, the Jordan, the Salt Sea — by its borders round about'
# ---- F3's facts: Moses' restatement ----
RELAY = seats('ויצו משה את בני ישראל'); NINE_HALF = seats('לתשעת המטות וחצי המטה'); NINE_HALF_OTHER = seats('לתשעת השבטים וחצי השבט'); NINE_CONSTRUCT = seats('לתשעת'); TWO_HALF = seats('שני המטות וחצי המטה')
assert RELAY == ['Num 34:13', 'Num 36:5'], RELAY                                                                                        # THE RELAY'S FORM — two Torah seats; 36:5's the installing act command_relayed (THE TENT sitting 4)
assert NINE_HALF == ['Josh 14:2', 'Num 34:13'] and NINE_HALF_OTHER == ['Josh 13:7'] and NINE_CONSTRUCT == ['Josh 13:7', 'Josh 14:2', 'Num 34:13'] and TWO_HALF == ['Josh 14:3', 'Num 34:15'], (NINE_HALF, NINE_HALF_OTHER, NINE_CONSTRUCT, TWO_HALF)   # "nine" in the construct three Bible seats, every one the nine tribes
assert words(34, 13)[16:20] == words(14, 2, 'Josh')[-4:] == ['לתשעת', 'המטות', 'וחצי', 'המטה'], (words(34, 13), words(14, 2, 'Josh'))          # JOSHUA 14:2 QUOTES 34:13's words under "as the LORD commanded by the hand of Moses"
RECEIPT_HAND = seats('כאשר צוה יהוה ביד משה'); RECEIPT_NUM = seats('כאשר צוה יהוה את משה', ('Num',)); BY_HAND = seats('ביד משה')
assert RECEIPT_HAND == ['Josh 14:2', 'Josh 21:8'] and len(RECEIPT_NUM) == 13 and not any(s.startswith('Num 34:') for s in RECEIPT_NUM) and len(BY_HAND) == 31, (RECEIPT_HAND, RECEIPT_NUM, len(BY_HAND))   # NO receipt in the chapter — the run's receipt Joshua 14:2's, outside the Torah
MATTEH = [(v, t) for _, v in SPAN for t, l in zip(_V[('Num', 34, v)], _L[('Num', 34, v)]) if l == '4294']; SHEVET = [(v, t) for _, v in SPAN for t, l in zip(_V[('Num', 34, v)], _L[('Num', 34, v)]) if l == '7626']
assert len(MATTEH) == 18 and SHEVET == [] and [l for t, l in zip(_V[('Num', 32, 33)], _L[('Num', 32, 33)]) if l in ('4294', '7626')] == ['7626'], (len(MATTEH), SHEVET)   # ONE TRIBE-NOUN — the staff-word eighteen times, the other never; 32:33's the neighbour
TOOK = seats('לקחו נחלתם'); REUBENITE = seats('הראובני'); GADITE = seats('הגדי'); HALF_MAN_MATTEH = seats('חצי מטה מנשה'); HALF_MAN_SHEVET = seats('חצי שבט מנשה'); BEYOND = seats('מעבר לירדן ירחו'); BY_LOT_T = seats('בגורל', TORAH); INHERIT_HIT = seats('תתנחלו')
assert TOOK == ['Josh 13:8', 'Josh 18:7', 'Num 34:14', 'Num 34:15'], TOOK                                                               # "took their inheritance" four Bible seats — always the two and a half
assert REUBENITE == ['1Chr 11:42', '1Chr 12:38', '1Chr 26:32', 'Josh 13:8', 'Num 26:7', 'Num 34:14'] and GADITE == ['1Chr 12:9', '2Kgs 10:33', '2Sam 23:36', 'Gen 38:23', 'Judg 14:6', 'Num 34:14'], (REUBENITE, GADITE)   # the Gadite's token is also "the kid" (Genesis 38:23, Judges 14:6) — a homograph by token
assert HALF_MAN_MATTEH == ['1Chr 6:56'] and words(34, 14)[12:15] == ['וחצי', 'מטה', 'מנשה'] and HALF_MAN_SHEVET == ['1Chr 5:23', 'Josh 22:13', 'Josh 22:15'], (HALF_MAN_MATTEH, HALF_MAN_SHEVET)
assert BEYOND == ['Num 22:1', 'Num 34:15'] and BY_LOT_T == ['Num 26:55', 'Num 33:54', 'Num 34:13', 'Num 36:2'] and INHERIT_HIT == ['Ezek 47:13', 'Num 33:54', 'Num 34:13'], (BEYOND, BY_LOT_T, INHERIT_HIT)
# ---- F4's facts: the dividers ----
NAMES_MEN = seats('אלה שמות האנשים'); TRIAD = seats('אלעזר הכהן ויהושע בן נון'); INHERIT_QAL = seats('ינחלו'); TO_DIVIDE = seats('לנחל'); TO_DIVIDE_LAND = seats('לנחל את הארץ')
assert NAMES_MEN == ['Num 13:16', 'Num 34:17'] and words(34, 19)[:3] == ['ואלה', 'שמות', 'האנשים'], (NAMES_MEN, words(34, 19))          # "these are the names of the men" — the spies' roster and this (34:19 with the conjunction)
assert TRIAD == ['Josh 14:1', 'Josh 19:51', 'Num 34:17'], TRIAD                                                                         # ELEAZAR THE PRIEST AND JOSHUA SON OF NUN as one phrase — three Bible seats: this and Joshua's two runs
assert INHERIT_QAL == ['Num 18:23', 'Num 18:24', 'Num 26:55', 'Num 34:17', 'Num 35:8', 'Prov 3:35', 'Prov 28:10'] and TO_DIVIDE_LAND == ['Josh 19:49', 'Num 34:18'], (INHERIT_QAL, TO_DIVIDE_LAND)
assert TO_DIVIDE == ['2Chr 29:16', '2Chr 30:14', 'Jer 47:2', 'Josh 15:7', 'Josh 17:9', 'Josh 19:49', 'Num 34:18', 'Num 34:29'], TO_DIVIDE   # one skin: "to the brook" (five seats), the plain "to divide" (34:18; Joshua 19:49), the intensive (34:29) — THE POINTS DECIDE
assert _PT[('Num', 34, 18)][6] == NF('לִנְחֹ֥ל') and _PT[('Num', 34, 29)][4] == NF('לְנַחֵ֥ל'), (_PT[('Num', 34, 18)][6], _PT[('Num', 34, 29)][4])   # the plain infinitive at 34:18, the intensive's at 34:29 (NFC both sides)
PIEL_RUNS = seats('נחלו'); PIEL_MOSES = seats('נחל משה')
assert {'Josh 14:1', 'Josh 19:51'} <= set(PIEL_RUNS) and 'Josh 13:32' in PIEL_MOSES, (PIEL_RUNS, PIEL_MOSES)                                # the intensive stem's other three seats Joshua's runs (13:32 Moses'; 14:1 and 19:51 Eleazar and Joshua's)
assert words(34, 17)[4:8] == ['ינחלו', 'לכם', 'את', 'הארץ'] and words(34, 29)[4:8] == ['לנחל', 'את', 'בני', 'ישראל'], (words(34, 17), words(34, 29))   # THE OBJECT SWITCHES WITH THE STEM — the land at 34:17-18, the people at 34:29
DOUBLING = words(34, 18)[:5]; ONE_PRINCE_PAIR = seats('נשיא אחד נשיא אחד'); ONE_MAN_PAIR = seats('איש אחד איש אחד')
assert DOUBLING == ['ונשיא', 'אחד', 'נשיא', 'אחד', 'ממטה'] and ONE_PRINCE_PAIR == ['Josh 22:14'] and ONE_MAN_PAIR == ['Josh 3:12', 'Josh 4:2', 'Josh 4:4', 'Num 13:2'], (DOUBLING, ONE_PRINCE_PAIR, ONE_MAN_PAIR)   # THE DISTRIBUTIVE DOUBLING — the spies, Joshua's stones and embassy
KIN = {k: ink_numbers(verse_words(*k)) for k in (('Num', 13, 2), ('Num', 7, 11), ('Num', 17, 21), ('Josh', 3, 12), ('Josh', 4, 2), ('Josh', 4, 4), ('Josh', 22, 14), ('Josh', 14, 2), ('Josh', 13, 7), ('Josh', 14, 3), ('Josh', 14, 4), ('Ezek', 47, 13), ('1Kgs', 8, 65))}
assert KIN == {('Num', 13, 2): [1, 1], ('Num', 7, 11): [1, 1], ('Num', 17, 21): [1, 1, 12], ('Josh', 3, 12): [12, 1, 1], ('Josh', 4, 2): [12, 1, 1], ('Josh', 4, 4): [2, 1, 1], ('Josh', 22, 14): [10, 1, 1], ('Josh', 14, 2): [9, Fraction(1, 2)], ('Josh', 13, 7): [9, Fraction(1, 2)], ('Josh', 14, 3): [2, Fraction(1, 2)], ('Josh', 14, 4): [2], ('Ezek', 47, 13): [12], ('1Kgs', 8, 65): [7, 7, 14]}, KIN   # the parser at the kin — the doubling read [1, 1] everywhere; the nine and the two at Joshua's runs
# ---- F5's facts: the roster ----
CALEB_FIVE = seats('למטה יהודה כלב בן יפנה'); CALEB_JEPH = seats('כלב בן יפנה'); PRINCE_NUM = seats('נשיא', ('Num',)); PRINCE_34 = [s for s in PRINCE_NUM if s.startswith('Num 34:')]
assert CALEB_FIVE == ['Num 13:6', 'Num 34:19'] and words(13, 6) == words(34, 19)[3:8] == ['למטה', 'יהודה', 'כלב', 'בן', 'יפנה'], (CALEB_FIVE, words(13, 6), words(34, 19))   # CALEB'S FIVE WORDS — the spy's line at the dividers'
assert CALEB_JEPH == ['1Chr 4:15', 'Deut 1:36', 'Josh 14:6', 'Num 13:6', 'Num 14:30', 'Num 26:65', 'Num 32:12', 'Num 34:19'], CALEB_JEPH
assert len(PRINCE_NUM) == 23 and PRINCE_34 == ['Num 34:18', 'Num 34:22', 'Num 34:23', 'Num 34:24', 'Num 34:25', 'Num 34:26', 'Num 34:27', 'Num 34:28'], (len(PRINCE_NUM), PRINCE_34)   # THE TITLE at seven roster rows — dropped at Judah's, Simeon's, Benjamin's
TRIBE = {'3063': 'judah', '8095': 'simeon', '1144': 'benjamin', '1835': 'dan', '4519': 'manasseh', '669': 'ephraim', '2074': 'zebulun', '3485': 'issachar', '836': 'asher', '5321': 'naphtali', '7205': 'reuben', '1410': 'gad', '3878': 'levi', '3130': 'joseph'}
def _tribe_of(book, ch, vs):
    ts = [TRIBE[l] for l in _L[(book, ch, vs)] if l in TRIBE]
    return ts[-1] if ts else None                                                                          # the LAST tribe lemma of the verse (34:23 names Joseph then Manasseh)
ROSTER = []
for v in range(19, 29):
    ws, ls, ms = _V[('Num', 34, v)], _L[('Num', 34, v)], _M[('Num', 34, v)]
    nps = [(w, l) for w, l, m in zip(ws, ls, ms) if 'Np' in m and l not in TRIBE]
    assert len(nps) == 2, (v, nps)                                                                                                     # every roster row names a prince and his father
    ROSTER.append({'verse': v, 'tribe': _tribe_of('Num', 34, v), 'prince': nps[0][0], 'prince_lemma': nps[0][1], 'father': nps[1][0], 'father_lemma': nps[1][1], 'title': 'נשיא' in ws, 'sons_of': 'בני' in ws, 'conjunction': ws[0].startswith('ו')})
assert [r['tribe'] for r in ROSTER] == ['judah', 'simeon', 'benjamin', 'dan', 'manasseh', 'ephraim', 'zebulun', 'issachar', 'asher', 'naphtali'], [r['tribe'] for r in ROSTER]
assert [r['prince'] for r in ROSTER] == ['כלב', 'שמואל', 'אלידד', 'בקי', 'חניאל', 'קמואל', 'אליצפן', 'פלטיאל', 'אחיהוד', 'פדהאל'] and [r['father'] for r in ROSTER] == ['יפנה', 'עמיהוד', 'כסלון', 'יגלי', 'אפד', 'שפטן', 'פרנך', 'עזן', 'שלמי', 'עמיהוד'], ROSTER
assert [r['title'] for r in ROSTER] == [False, False, False, True, True, True, True, True, True, True] and [r['sons_of'] for r in ROSTER] == [False, True, False, True, True, True, True, True, True, True] and [r['conjunction'] for r in ROSTER] == [True, True, False, True, False, True, True, True, True, True], ROSTER   # the title dropped for three; "the children of" absent at Judah's and Benjamin's; the conjunction absent at Benjamin's and at Joseph's heading
PRINCE_SEATS = {r['prince']: lemma_seats(r['prince_lemma']) for r in ROSTER}; FATHER_SEATS = {r['father']: lemma_seats(r['father_lemma']) for r in ROSTER}
ONLY_HERE_LEMMA = [n for n, s in list(PRINCE_SEATS.items()) + list(FATHER_SEATS.items()) if s == ['Num 34:%d' % v for v in range(19, 29) if n in words(34, v)]]
ONLY_HERE_TOKEN = [n for n in [r['prince'] for r in ROSTER] + [r['father'] for r in ROSTER] if all(s.startswith('Num 34:') for s in tok(n))]
assert ONLY_HERE_TOKEN == ['אלידד', 'חניאל', 'אחיהוד', 'פדהאל', 'יגלי', 'שפטן', 'פרנך', 'עזן'] and len(ONLY_HERE_TOKEN) == 8, ONLY_HERE_TOKEN   # EIGHT names nowhere else BY TOKEN — Hanniel among them (1 Chronicles 7:39 spells his namesake otherwise), Ephod not (the vestment's token at Exodus 28:15, 39:8): the third run read
assert set(ONLY_HERE_LEMMA) == (set(ONLY_HERE_TOKEN) - {'חניאל'}) | {'אפד', 'כסלון', 'שלמי'} and len(ONLY_HERE_LEMMA) == 10, ONLY_HERE_LEMMA   # TEN BY LEMMA — Ephod the person (641), Chislon (Joshua 15:10's Chesalon another lemma), Shelomi ("my peace-offerings" another) in; Hanniel out (his lemma at 1 Chronicles 7:39): the reading's "eight" (Ephod in, Hanniel out) was a MIXED measure — filed at the compile
assert PRINCE_SEATS['שמואל'] and len(PRINCE_SEATS['שמואל']) == 120 and PRINCE_SEATS['שמואל'][0] != 'Num 34:20' and 'Num 34:20' in PRINCE_SEATS['שמואל'], (len(PRINCE_SEATS['שמואל']), PRINCE_SEATS['שמואל'][:3])   # SHEMUEL — the prophet's name (one hundred twenty verses by lemma), its first seat here
assert len(PRINCE_SEATS['כלב']) == 35 and FATHER_SEATS['עמיהוד'] == ['1Chr 7:26', '1Chr 9:4', 'Num 1:10', 'Num 2:18', 'Num 7:48', 'Num 7:53', 'Num 10:22', 'Num 34:20', 'Num 34:28'], (len(PRINCE_SEATS['כלב']), FATHER_SEATS['עמיהוד'])   # AMMIHUD — three tribes' fathers' name (Ephraim's Elishama 1:10; Simeon's; Naphtali's)
assert FATHER_SEATS['אפד'] == ['Num 34:23'] and tok('אפד') == ['Exod 28:15', 'Exod 39:8', 'Num 34:23'] and tok('כסלון') == ['Josh 15:10', 'Num 34:21'] and PRINCE_SEATS['קמואל'] == ['1Chr 27:17', 'Gen 22:21', 'Num 34:24'], (FATHER_SEATS['אפד'], tok('אפד'), tok('כסלון'), PRINCE_SEATS['קמואל'])   # Ephod the vestment's consonants; Chislon Judah's north-border Chesalon; Kemuel Nahor's son's name
assert PRINCE_SEATS['אליצפן'] == ['1Chr 15:8', '2Chr 29:13', 'Exod 6:22', 'Lev 10:4', 'Num 3:30', 'Num 34:25'] and tok('אליצפן') == ['1Chr 15:8', '2Chr 29:13', 'Num 3:30', 'Num 34:25'] and PRINCE_SEATS['פלטיאל'] == ['2Sam 3:15', 'Num 34:26'] and PRINCE_SEATS['בקי'] == ['1Chr 5:31', '1Chr 6:36', 'Ezra 7:4', 'Num 34:22'] and len(PRINCE_SEATS['חניאל']) == 2, (PRINCE_SEATS['אליצפן'], PRINCE_SEATS['פלטיאל'], PRINCE_SEATS['בקי'], PRINCE_SEATS['חניאל'])   # Elizaphan SIX by lemma (Exodus 6:22's and Leviticus 10:4's Elzaphan the same Kohathite), four by token — the fourth run read: a token list typed against a lemma census
GOD_NAMES = [r['prince'] for r in ROSTER if r['prince'].startswith('אל') or r['prince'].endswith('אל')]; GOD_FATHERS = [r['father'] for r in ROSTER if r['father'].startswith('אל') or r['father'].endswith('אל')]
assert GOD_NAMES == ['שמואל', 'אלידד', 'חניאל', 'קמואל', 'אליצפן', 'פלטיאל', 'פדהאל'] and GOD_FATHERS == [], (GOD_NAMES, GOD_FATHERS)   # SEVEN of the ten carry God's name, none of the fathers
JOSHUA_TRIBE = _tribe_of('Num', 13, 8)
assert JOSHUA_TRIBE == 'ephraim' and words(13, 8)[:2] == ['למטה', 'אפרים'], (JOSHUA_TRIBE, words(13, 8))                                  # Joshua's tribe from 13:8's line (the spies' roster) — the row's column computed
def _order(rng):
    o = []
    for k in rng:
        if k not in _V: continue
        for l in _L[k]:
            if l in TRIBE and TRIBE[l] not in o: o.append(TRIBE[l])
    return o
LISTS = collections.OrderedDict([('Gen 29-30', [('Gen', 29, v) for v in range(31, 36)] + [('Gen', 30, v) for v in range(1, 25)]), ('Gen 35:23-26', [('Gen', 35, v) for v in range(23, 27)]), ('Gen 46:8-25', [('Gen', 46, v) for v in range(8, 26)]), ('Gen 49', [('Gen', 49, v) for v in range(3, 28)]), ('Exod 1:2-4', [('Exod', 1, v) for v in range(2, 5)]), ('Num 1:5-15', [('Num', 1, v) for v in range(5, 16)]), ('Num 1:20-43', [('Num', 1, v) for v in range(20, 44)]), ('Num 2', [('Num', 2, v) for v in range(3, 32)]), ('Num 7:12-83', [('Num', 7, v) for v in range(12, 84)]), ('Num 10:14-27', [('Num', 10, v) for v in range(14, 28)]), ('Num 13:4-15', [('Num', 13, v) for v in range(4, 16)]), ('Num 26:5-50', [('Num', 26, v) for v in range(5, 51)]), ('Deut 27:12-13', [('Deut', 27, v) for v in (12, 13)]), ('Deut 33', [('Deut', 33, v) for v in range(6, 25)]), ('Josh 13-19', [('Josh', c, v) for c in range(13, 20) for v in range(1, 60)]), ('Ezek 48:1-7, 23-27', [('Ezek', 48, v) for v in list(range(1, 8)) + list(range(23, 28))])])
ORDERS = collections.OrderedDict((n, _order(rng)) for n, rng in LISTS.items())
ROSTER_ORDER = [r['tribe'] for r in ROSTER]
def _restrict(o): return [t for t in o if t in ROSTER_ORDER]
MATCHES = [n for n, o in ORDERS.items() if _restrict(o) == ROSTER_ORDER]
assert MATCHES == [] and len(ORDERS) == 16, (MATCHES, ORDERS)                                                                          # THE ORDER MATCHES NO OTHER ROSTER (sixteen lists, restricted to the roster's ten)
MAN_BEFORE_EPH = [n for n, o in ORDERS.items() if 'manasseh' in o and 'ephraim' in o and o.index('manasseh') < o.index('ephraim')]
ZEB_BEFORE_ISS = [n for n, o in ORDERS.items() if 'zebulun' in o and 'issachar' in o and o.index('zebulun') < o.index('issachar')]
assert MAN_BEFORE_EPH == ['Gen 46:8-25', 'Num 26:5-50', 'Josh 13-19', 'Ezek 48:1-7, 23-27'] and ZEB_BEFORE_ISS == ['Gen 49', 'Deut 33'], (MAN_BEFORE_EPH, ZEB_BEFORE_ISS)   # Manasseh before Ephraim as the second census and Genesis 46 in the Torah (Joshua's east half and Ezekiel's north outside it); Zebulun before Issachar as the two blessings alone
LOTS_19 = [_tribe_of('Josh', 19, v) for v in (10, 17, 24, 32)]
assert LOTS_19 == ['zebulun', 'issachar', 'asher', 'naphtali'] == ROSTER_ORDER[-4:], (LOTS_19, ROSTER_ORDER)                             # THE FOUR NORTHERN TRIBES in the order Joshua's lots fall (19:10, 17, 24, 32)
CLOSER = seats('אלה אשר צוה יהוה'); SPOKE_NUM = seats('וידבר יהוה אל משה לאמר', ('Num',))
assert CLOSER == ['Num 34:29'] and len(SPOKE_NUM) == 32 and {'Num 34:1', 'Num 34:16'} <= set(SPOKE_NUM), (CLOSER, len(SPOKE_NUM))         # the closer's form without a noun — one seat; no receipt
# ---- THE CALLEES (live import edges; the design's cells by name; every value typed from bor_compile_measure.out) ----
C2_LOT = C2.the_land({'ask': 'by_lot'}, C2.DATA); C2_ONLY = C2.the_land({'ask': 'only_excludes'}, C2.DATA); C2_MOUTH = C2.the_land({'ask': 'lots_mouth'}, C2.DATA); C2_THIRTEEN = C2.the_land({'ask': 'thirteen_tribes'}, C2.DATA); C2_HELD = C2.the_land({'ask': 'possession_before_assignment'}, C2.DATA)
assert C2_LOT[0] == 'the place by lot — Joshua 14-19 the run' and C2_LOT[1] == ['commanded'] and C2_ONLY[0] == "Joshua and Caleb excluded from the lot — 26:65's two" and C2_ONLY[1] == ['exempt'], (C2_LOT, C2_ONLY)   # THE CALL: the lot's cell — 34:2 and 34:13 cite it; "only" excludes the two dividers' portions
assert C2_MOUTH[0] == "the lot's mouth is the oracle's — two receptacles before Eleazar" and C2_THIRTEEN[0] == 'twelve now, thirteen to come' and C2_HELD[0] == 'in possession before assignment — the rows are holdings before the lot' and C2.DATA['division_by']['value'] == 'tribes', (C2_MOUTH, C2_THIRTEEN, C2_HELD)
GR_COMM = GR.the_acceptance_and_the_charge({'ask': 'the_commission'}, GR.DATA); GR_THREE = GR.the_grant({'ask': 'three_parties'}, GR.DATA); GR_COUNT = GR.the_grant({'ask': 'the_count'}, GR.DATA); GR_NOTLOT = GR.the_grant({'ask': 'not_by_lot'}, GR.DATA); GR_HELD = GR.the_grant({'ask': 'land_held'}, GR.DATA)
assert GR_COMM[0].startswith('Eleazar the priest, Joshua son of Nun and the heads of the fathers of the tribes (32:28)') and GR_COMM[1] == ['commanded'] and GR.TRIAD_32 == ['Num 32:28'] and GR.TRIAD_JOSH == ['Josh 14:1'], (GR_COMM, GR.TRIAD_32, GR.TRIAD_JOSH)   # THE CALL: the commission's charge — the same triad
assert GR_THREE[0].startswith('to the sons of Gad, to the sons of Reuben and to half the tribe of Manasseh (32:33) — three transfers') and GR_THREE[1] == ['holding_given'] and GR_COUNT[0].startswith("the two and a half's count — 43,730 + 40,500 + 52,700 ÷ 2 = 110,580"), (GR_THREE, GR_COUNT)   # THE CALL: the grant's three transfers and the count
assert GR_NOTLOT[0].startswith("the east by Moses' word, not by lot") and GR_HELD[0].startswith('in possession before assignment'), (GR_NOTLOT, GR_HELD)
COUNT_TWO_HALF = 43730 + 40500 + 52700 // 2
assert COUNT_TWO_HALF == 110580 and '110,580' in GR_COUNT[0], COUNT_TWO_HALF
SL_ONE = SL.spies({'ask': 'one_per_tribe'}, SL.DATA); SL_EQUAL = SL.spies({'ask': 'joshua_caleb_equal'}, SL.DATA); SL_FOURTH = SL.spies({'ask': 'fourth_order'}, SL.DATA); SL_EXC = SL.decree({'ask': 'exceptions'}, SL.DATA); SL_CALEB = SL.decree({'ask': 'caleb_entitlement'}, SL.DATA); SL_PORTIONS = SL.decree({'ask': 'spies_portions'}, SL.DATA)
assert SL_ONE[0] == '12 — one man per tribe, princes; Levi absent' and SL_EQUAL[0] == 'equal — Caleb first at 13:6, Joshua at 13:8 (Tosefta Keritot 4:7)' and SL_FOURTH[0].startswith('a fourth order of the twelve'), (SL_ONE, SL_EQUAL, SL_FOURTH)   # THE CALL: the spies' doubling and roster
assert SL_EXC[0] == 'Caleb and Joshua (14:24, 14:30); the children brought in (14:31)' and SL_EXC[1] == ['exempt'] and SL_CALEB[0].startswith('holding_owed — Hebron; PAID at Josh 14:13-14') and SL_PORTIONS[0].startswith("Joshua and Caleb lived in the ten's portions"), (SL_EXC, SL_CALEB, SL_PORTIONS)
assert SL.SPY_TRIBES == ['ראובן', 'שמעון', 'יהודה', 'יששכר', 'אפרים', 'בנימן', 'זבולן', 'יוסף', 'דן', 'אשר', 'נפתלי', 'גד'], SL.SPY_TRIBES
CK_TWO = CK.edom_and_hor({'ask': 'two_mount_hors'}, CK.DATA)
assert CK_TWO[0] == "two Mount Hors — Aaron's at Edom's border, the northern border's (34:7-8)", CK_TWO                                # THE CALL: the chukat runner's row NAMES THIS CHAPTER
CB_ORDERS = CB.census({'ask': 'orders'}, CB.DATA)
assert CB_ORDERS[0] == 'three orders in the portion; Gad moves from eleventh to third' and CB.TRIBES == ['reuben', 'simeon', 'gad', 'judah', 'issachar', 'zebulun', 'ephraim', 'manasseh', 'benjamin', 'dan', 'asher', 'naphtali'], (CB_ORDERS, CB.TRIBES)   # THE CALL: the roll's three orders
NS_PER_DAY = NS.dedication({'ask': 'per_day'}, NS.DATA); NS_ERASURE = NS.sotah({'ask': 'scroll_erasure'}, NS.DATA)
assert NS_PER_DAY[0].startswith('one prince per day') and NS.NAMES == ['נחשון', 'נתנאל', 'אליאב', 'אליצור', 'שלמיאל', 'אליסף', 'אלישמע', 'גמליאל', 'אבידן', 'אחיעזר', 'פגעיאל', 'אחירע'] and NS_ERASURE[0] == 'written whole, erased at once', (NS_PER_DAY, NS.NAMES, NS_ERASURE)   # THE CALL: 7:11's doubling; the twelve of chapter 1; the sotah's blot (the other sense of 34:11's token)
assert not set(NS.NAMES) & {r['prince'] for r in ROSTER}, 'NO PRINCE OF CHAPTER 1 among the ten'
KR_STAFFS = KR.plague_and_staffs({'ask': 'staffs_count'}, KR.DATA)
assert KR_STAFFS[0].startswith("12 — a staff for a father's house") and KR.STAFFS_21 == [1, 1, 12] and KR.ONE_ONE == [1, 1], (KR_STAFFS, KR.STAFFS_21, KR.ONE_ONE)   # THE CALL: 17:21's rods by prince and tribe
ZL_RUN = ZL.the_daughters({'ask': 'the_run'}, ZL.DATA); ZL_REACH = ZL.the_daughters({'ask': 'reach'}, ZL.DATA); ZL_TEN = ZL.inheritance_order({'ask': 'ten_parts'}, ZL.DATA)
assert ZL_RUN[0].startswith('given in the sixth book by the mouth of the LORD') and ZL_RUN[1] == ['holding_owed'] and ZL_REACH[0] == 'this generation — the one that divided the land' and ZL_TEN[0].startswith("ten — six fathers' houses"), (ZL_RUN, ZL_REACH, ZL_TEN)   # THE CALL: the daughters' holding paid before Eleazar and Joshua (Joshua 17:4)
JO_LOT = JO.the_command({'ask': 'the_lot_restated'}, JO.DATA); JO_PASS = JO.the_command({'ask': 'when_you_pass'}, JO.DATA); JO_DWELL = JO.the_command({'ask': 'possess_and_dwell'}, JO.DATA)
assert JO_LOT[0].startswith('the lot restated to the people (33:54)') and JO_PASS[0].startswith('when you pass over the Jordan into the land of Canaan (33:51)') and JO_DWELL[0].startswith('possess the land and dwell in it'), (JO_LOT, JO_PASS, JO_DWELL)   # THE CALL: 33:51's entry clause, 33:54's restatement
# ===== THE DATA CHANNEL — the parameter rows the ink leaves open (motion 2's recorded settings) =========
DATA = {
    'the_four_sides': {'value': SIDES, 'settings': {'one_status_on_the_land': "THE FOUR SIDES AS A DATA ROW AND ONE STATUS ON THE LAND (the design's decision on the measurements): the border is the land's property — 'the land of Canaan BY ITS BORDERS' (34:2), 'this shall be your land by its borders round about' (34:12) — so the speech writes borders_declared on the land of Canaan (the standing place entity), its value the sides in the ink's order with their named points; nothing on the people, whose lot's debit (26:52-56) stands open and is cited", 'a_line_per_side': 'four acts for one speech — REFUSED: one speech, one status'},
                       'source': "34:3-12 — the proper-name tokens by verse and side on the DB (twenty-seven), each with its lemma's seats outside the chapter (Joshua 15:1-4 the south's run; Ezekiel 47:15-20 and 48:1, 28 the kin); the common-noun points named in the design"},
    'the_two_mount_hors': {'value': CK.DATA['two_mount_hors']['value'] if 'two_mount_hors' in CK.DATA else CK_TWO[0], 'settings': {'read_from_chukat': "the chukat runner's row: Aaron's Mount Hor at Edom's border (20:22-28; 33:37-41) and the north border's (34:7-8) — twelve Torah seats of the name, ten Aaron's, two the border's; Onkelos spells the two differently in adjacent verses (34:7 without the vav, 34:8 with it)"},
                           'source': "34:7-8 against 20:22 — CK.edom_and_hor('two_mount_hors') by CALL; HOR_LEMMA computed"},
    'the_promised_extents': {'value': ['Gen 15:18', 'Exod 23:31', 'Deut 1:7', 'Deut 11:24', 'Josh 1:4'], 'settings': {'no_verdict': "the covenant's 'from the river of Egypt to the great river, the river Euphrates' (Genesis 15:18), 'from the Red Sea to the sea of the Philistines and from the wilderness to the river' (Exodus 23:31), 'to the great river, the river Euphrates' (Deuteronomy 1:7), 'from the river … to the western sea' (11:24), 'from the wilderness and this Lebanon to the great river' (Joshua 1:4): NO river, Euphrates, Lebanon or western sea stands in the chapter — the four sides are another description; OBSERVED, no link (the reading's finding)"},
                             'source': '34:3-12 against the five verses on the tokens (the reading measured the absence; the runner asserts it on the chapter\'s tokens)'},
    'ezekiels_order': {'value': 'north_east_south_west', 'settings': {'north_east_south_west': "Ezekiel 47:15 'the north side', 47:18 'the east side', 47:19 'the south side', 47:20 'the west side' — the prophet's four sides from the north, against the chapter's south (34:3), west (34:6), north (34:7), east (34:10); twenty-nine tokens shared; Ezekiel 47:13 opens with 34:13's 'you shall inherit' and 47:14 with 34:2's 'shall fall to you as an inheritance': OBSERVED, no link"},
                       'source': 'Ezekiel 47:13-20 on the tokens (EZEK_SHARED, EZEK_SIDES computed)'},
    'the_sea_as_border': {'value': 'the_islands_by_the_string', 'settings': {'the_islands_by_the_string': "the Rabbis (Gittin 8a:4, 8a:6; the Tosefta Terumot 2:12): a string pulled taut from Turei Amnon in the north to the River of Egypt in the south — the islands inward are the land, outward not; 34:6's 'and its border' teaches the islands (8a:7): THE WEST DRAWN AS A LINE BETWEEN THE INK'S TWO CORNERS", 'the_sea_itself': "Rabbi Yehuda (Gittin 8a:5): every place directly across from the land, the sea itself included, is the land — from 34:6 'and its border'; no verse needed for the islands (8a:7)"},
                          'source': "34:6 — the shelf's two readings of one word (Gittin 8a:4-7); Onkelos's possessive on 34:6's second 'border' the reading's find; the value the Rabbis' (the majority) — a DATA row, no verdict on the tape"},
    'the_jordan_as_border': {'value': 'one_border_round_about', 'settings': {'one_border_round_about': "Bekhorot 55a:10 from 34:12 'this shall be your land by its borders round about' — all the land one border, the tribes' demarcations inside it not borders (the animal tithe joins across the Jordan)", 'the_jordan_canaans': "Rabbi Shimon ben Yochai (Bekhorot 55a:14) from 34:15 'beyond the Jordan AT JERICHO': as Jericho is Canaan's, the Jordan is Canaan's"},
                             'source': "34:12 and 34:15 — the loop's closer and the 'at Jericho' pair (22:1, 34:15) read as rules on the shelf; a DATA row, no verdict on the tape"},
    'the_three_lands': {'value': 'babylon_egypt_beyond', 'settings': {'babylon_egypt_beyond': "Mishnah Sheviit 6:1: what those who came up from Babylon held (to Chezib) — not eaten, not worked; what those who came up from Egypt held (Chezib to the river and to Amanah) — eaten, not worked; from the river and Amanah inward — eaten and worked; 9:2: Judea, Transjordan, Galilee for the removal; the Tosefta 4:4: from the river north of Achziv to Ammon and Moab and the land of Egypt, 'two lands'; Mishnah Gittin 1:2 for the bills: from REKEM eastward overseas (Rekem the translation's Kadesh-barnea of 34:4), from Ashkelon southward, from Akko northward"},
                        'source': "the shelf's own border lines inside 34's one border — OBSERVED (no cell computes a holding's line); the translation's 'Rekem Geah' at 34:4 the reading's find"},
    'the_land_bound_rule': {'value': 'body_everywhere_land_inside', 'settings': {'body_everywhere_land_inside': "Mishnah Kiddushin 1:9 (36b:8): a commandment dependent on the land applies only in the land, one not dependent everywhere; Rav Yehuda (37a:3): an obligation of the body everywhere, an obligation of the land — the earth and its growths — inside only; the exceptions orlah and diverse kinds (37a:1); the new crop disputed (37a:7-15); the classing taught from Deuteronomy 12:1-2's adjacent verses (37a:4-6)"},
                            'source': "THE BORDERS' LEGAL REACH — the rule the chapter's border serves; added at the docket (the design's fifteenth row); no cell classes the commandments — Deuteronomy's, the readback's"},
    'the_nine_and_a_half': {'value': {'nine': NINE, 'two': TWO, 'halves': 2, 'sum': NINE + TWO + 1, 'count_two_and_a_half': COUNT_TWO_HALF}, 'settings': {'a_run_citation': "34:14-15's 'have taken their inheritance' is the ledger's own three holding_given transfers (32:33 — the sons of Gad, the sons of Reuben, the half tribe of Manasseh) read back: the line WRITES NOTHING; the count 110,580 GR.the_grant('the_count') by CALL; Joshua 14:2's receipt 'as the LORD commanded by the hand of Moses, to the nine tribes and the half tribe' quotes 34:13's words OUTSIDE THE TORAH — the readback's"},
                            'source': "34:13-15 — the parser's [9] and [2] with the two halves = twelve; 'took their inheritance' four Bible seats (TOOK); the grant's transfers on the running world (CW4)"},
    'the_relay_form': {'value': 'moses_commanded_the_children_of_israel', 'settings': {'moses_commanded_the_children_of_israel': "'and Moses commanded the children of Israel, saying' — the phrase's TWO Torah seats, 34:13 and 36:5 (RELAY); 36:5's is the installing act command_relayed of THE TENT sitting 4 (the second output on the daughters' case); here the relay of 34:1-12 to the people; law_borders installed_by BOOT with the class named — whether a relay in this form INSTALLS is the second pass's D2 question"},
                       'source': "34:13 against 36:5 on the tokens (RELAY computed); the installation registry's command_relayed row (installation_parameters.yaml)"},
    'the_distributive_doubling': {'value': [1, 1], 'settings': {'two_ones': "'one prince, one prince from a tribe' (34:18) read [1, 1] by the parser — the idiom's sense 'each': 13:2's spies, 7:11's dedication ('one prince per day, one prince per day'), 17:21's rods ([1, 1, 12]); Joshua 3:12 and 4:2 [12, 1, 1], 4:4 [2, 1, 1], 22:14 [10, 1, 1] the runs — a class named, not a gap (no rule owed)"},
                                  'source': '34:18 and the seven kin verses by the same parser (KIN computed)'},
    'the_princes_as_agents': {'value': 'the_steward_for_orphans', 'settings': {'the_steward_for_orphans': "Rava bar Rav Huna, Rav Giddel, Rav (Kiddushin 42a:8): from 34:18 'you shall take one prince from each tribe' — the court appoints a steward for orphans who come to divide, 'to their disadvantage and to their benefit': the verse's teaching kept", 'agency_refused': "Rav Giddel (42a:6): the law of agency from 34:18 — the prince the tribe's agent; REFUSED, since minors have no agency and the princes divided for them"},
                              'source': "34:18 — the shelf's two readings (Kiddushin 42a:6-8); the dividers a court acting for those who cannot act — the class the daughters' holding_owed carries (its counterparty the court)"},
    'the_seventy_one': {'value': 'refused_the_lots_the_urim_all_israel', 'settings': {'refused_the_lots_the_urim_all_israel': "Sanhedrin 16a:3: the first division needed the lots, the Urim and all Israel present — a later border dispute needs none, so Ulla's likeness (16a:2 — two tribes' border dispute before the seventy-one, as the first division by seventy-one elders) is refused; the dividers of 34:17-18 the ink's twelve", 'ulla_seventy_one': "Ulla, Rabbi Elazar (Sanhedrin 16a:2): the initial division was performed by seventy-one elders of the congregation — a tribes' border dispute before the Great Sanhedrin"},
                        'source': "Sanhedrin 16a:2-3 — the first division's instruments on the shelf (the lot 26:55, the Urim 26:56, the people: Bava Batra 122a:4); no verdict on the tape"},
    'the_roster': {'value': ROSTER, 'settings': {'the_twelve': "Eleazar the priest, Joshua son of Nun, and the ten princes by tribe (34:17-28) — the columns tribe, prince, father, the title, 'the children of', the conjunction, computed per row; the title at seven rows (dropped at Judah's, Simeon's, Benjamin's); 'the children of' absent at Judah's and Benjamin's; the conjunction absent at Benjamin's and at Joseph's heading (1:10's form); seven of the ten carry God's name, none of the fathers; Caleb's five words 13:6's; Ammihud three tribes' fathers' name; Shemuel the prophet's name's first seat; EIGHT names nowhere else by token (Hanniel among them), TEN by lemma (Ephod, Chislon, Shelomi in by lemma, homographs by token; Hanniel out by lemma) — the reading's 'eight' a mixed measure, filed"},
                   'source': '34:17-28 on the DB (ROSTER, PRINCE_SEATS, FATHER_SEATS computed); the twelve enter the population table as named rows (grain named, as_of Num 34:17-29)'},
    'the_roster_order': {'value': ROSTER_ORDER, 'settings': {'matching_none': "Judah, Simeon, Benjamin, Dan, (Joseph:) Manasseh, Ephraim, Zebulun, Issachar, Asher, Naphtali — against SIXTEEN lists computed by lemma (Genesis 29-30, 35, 46, 49; Exodus 1; Numbers 1 twice, 2, 7, 10, 13, 26; Deuteronomy 27, 33; Joshua 13-19; Ezekiel 48): matching NONE; Manasseh before Ephraim as the second census and Genesis 46 (and Joshua's east half named first); Zebulun before Issachar as Jacob's and Moses' blessings alone; the four northern tribes in the order Joshua's lots fall (19:10, 17, 24, 32) — the cause unnamed, the declared shelf silent"},
                         'source': '34:19-28 against the sixteen lists (ORDERS, MATCHES, MAN_BEFORE_EPH, ZEB_BEFORE_ISS, LOTS_19 computed)'},
}


# ===== F1: THE LAND AND ITS FALL (Num 34:1-2) ===========================================================
def the_land_and_its_fall(case, data):
    del P[:]
    ask = case['ask']
    if ask == 'the_command':
        ink('34:2', '"command the children of Israel" — %s: THE FIVE TORAH SEATS' % COMMAND)
        move('Sifrei Bamidbar 1:2 (credited)', "Rabbi Shimon ben Yochai: everywhere 'command' entails expense except this one — 'impel them to the division of the land' (the reading: the census meets the row, the five seats the row's five)")
        return out("command the children of Israel (34:2) — five Torah seats, the Sifrei's five; the one command without expense (Sifrei 1:2)", ['accepted'])
    if ask == 'when_you_come':
        ink('34:2', '"when you are coming into the land Canaan" — %s: the article on the land, none on Canaan — %s, ONE Bible seat; the bare pair "the land of Canaan" %d Torah seats; 33:51\'s "when you pass over the Jordan into the land of Canaan" the entry clause' % (words(34, 2)[6:12], LAND_CANAAN_ART, len(LAND_CANAAN_T)))
        move('cold_run_journeys (CALL) — JO.the_command(when_you_pass) = %s' % JO_PASS[0], "33:51's trigger clause")
        return out("when you are coming into the land Canaan (34:2) — the article on the land, none on the name; 33:51's entry clause by CALL", ['accepted'])
    if ask == 'the_land_canaan':
        ink('34:2', '"the land Canaan" — the name in the deed; Genesis 9:25\'s canaan_cursed on the ledger since the curse')
        move('Sanhedrin 91a:6', "the people of Afrikiya claim the land from 34:2 'the land of Canaan' — Canaan their forefather; Geviha ben Pesisa's answer Genesis 9:25 (a slave's acquisitions are his master's)")
        return out("the land of Canaan (34:2) read as a title claim (Sanhedrin 91a:6) — the tape's answer canaan's status since Genesis 9:25", ['accepted'])
    if ask == 'this_is_the_land':
        ink('34:2, 13', '"this is the land" — %s: 34:2, 34:13, Deuteronomy 34:4 (from Nebo), Joshua 13:2, Ezekiel 48:29' % THIS_LAND)
        return out("this is the land — 34:2 and 34:13, Deuteronomy 34:4 from Nebo, Joshua 13:2, Ezekiel 48:29", ['accepted'])
    if ask == 'shall_fall':
        ink('34:2', '"that shall FALL to you as an inheritance" — %s (one seat); "shall fall" in the Torah %s; Onkelos "be DIVIDED" — one Aramaic verb for 34:2\'s fall and 26:53-56\'s divide' % (FALL_TO_YOU, FALL_T))
        move('cold_run_second_census (CALL) — C2.the_land(by_lot) = %s' % C2_LOT[0], "the lot's cell: the OPEN divide_the_land debit on Israel (26:52-56) — CITED, not rewritten (CW3)")
        return out("that shall fall to you as an inheritance (34:2) — the lot's verb at its one Torah seat with the inheritance; Onkelos 'be divided'; the lot's debit by CALL, cited", ['accepted'])
    if ask == 'as_an_inheritance':
        ink('34:2', '"as an inheritance" — %s: three Torah seats, all the land\'s' % INHERITANCE_T)
        return out("as an inheritance (34:2) — three Torah seats: 26:53, 34:2, 36:2, all the land's", ['accepted'])
    if ask == 'by_its_borders':
        ink('34:2, 12', '"by its borders" — %s: THE INCLUSIO; Joshua\'s two closers %s (with the vav); the border-word %d times in the chapter, %d in Numbers' % (BY_ITS_BORDERS, BY_ITS_BORDERS_JOSH, len(BORDER_TOKENS), BORDER_NUM))
        move('Bekhorot 55a:10', "'this shall be your land by its borders round about' — all the land one border, the tribes' demarcations inside it")
        dat('the row the_four_sides: %s' % data['the_four_sides']['settings']['one_status_on_the_land'][:80])
        return out("by its borders (34:2, 34:12) — the inclusio; Joshua 18:20 and 19:49 the closers; the border-word sixteen times: ONE STATUS ON THE LAND", ['borders_declared'])
    if ask == 'the_frame':
        ink('34:1, 16', 'the frames %s — two divine frames with Moses\' own command between them (34:13); 35:1 adds the plains of Moab' % FRAME_VERBS)
        dat('installed_by BOOT with the class named — a law in the divine voice relayed at 34:13 in 36:5\'s form; the second pass (D2) decides')
        return out("and the LORD spoke to Moses, saying (34:1, 34:16) — two divine frames with Moses' command between them; 35:1 adds the plains of Moab", ['accepted'])
    if ask == 'the_land_bound_rule':
        move('Mishnah Kiddushin 1:9 (36b:8); Kiddushin 37a:3-6', "a commandment dependent on the land applies inside the border only, an obligation of the body everywhere — the classing from Deuteronomy 12:1-2's adjacent verses")
        dat('the row the_land_bound_rule: %s — the borders\' legal reach; no cell classes the commandments' % data['the_land_bound_rule']['value'])
        return out("the borders' legal reach — an obligation of the land inside the border, of the body everywhere (Mishnah Kiddushin 1:9; 37a:3-6): a data row, the classing Deuteronomy's", ['accepted'])
    return out('no verdict in span', [FX.NONE])


# ===== F2: THE FOUR SIDES (Num 34:3-12) — the data row; the second Mount Hor; the sea; the Jordan ===========
def the_four_sides(case, data):
    del P[:]
    ask = case['ask']
    if ask == 'the_south':
        ink('34:3-5', 'the south side — %s; "the south side" %s; "from the wilderness of Zin" %s (13:21 the other seat); "on the hands of Edom" %s (one seat, Onkelos "on the borders of"); "the end of the Salt Sea" %s; the ascent of Akrabbim %s; Kadesh-barnea ten seats by lemma (Onkelos "Rekem Geah"); Hazar-addar %s (Joshua splits it — Hezron and Addar); Azmon %s / %s; "the brook of Egypt" %s (the Kings\' form %s)' % ([p[1] for p in SIDES['south']['points']], SOUTH_SIDE, WILD_ZIN, HANDS_EDOM, END_SALT, AKRABBIM, HAZAR_ADDAR, AZMON, AZMON_JOSH, BROOK, BROOK_KINGS))
        return out("the south side (34:3-5) — from the wilderness of Zin on the hands of Edom to the brook of Egypt and the sea; eleven proper-name tokens; Joshua 15:1-4 Judah's run of it", ['borders_declared'])
    if ask == 'the_west':
        ink('34:6', '"and the west border: you shall have the great sea and its border" — "the west border" %s (one seat); "the great sea" %s (plene); "and its border" %s (twelve seats)' % (WEST_BORDER, GREAT_SEA, len(AND_ITS_BORDER)))
        move('Gittin 8a:5-7', "Rabbi Yehuda: the sea itself within the land from 'and its border'; the Rabbis: the word teaches the islands")
        dat('the row the_sea_as_border: %s (the Rabbis\' string from Turei Amnon to the River of Egypt); Rabbi Yehuda\'s arm recorded' % data['the_sea_as_border']['value'])
        return out("the west border (34:6) — the great sea and its border: one word read two ways on the shelf (the sea itself, or the islands by the string — Gittin 8a:4-7)", ['borders_declared'])
    if ask == 'the_north':
        ink('34:7-9', 'the north side — %s; "the north border" %s; "you shall mark out" %s (three Bible seats here; Proverbs\' "desire" the homograph); "Lebo-hamath" %s (13:21 the other); Zedad %s, Ziphron %s, Hazar-enan %s (Ezekiel\'s spelling %s)' % ([p[1] for p in SIDES['north']['points']], NORTH_BORDER, MARK, LEBO, ZEDAD, ZIPHRON, HAZAR_ENAN, HAZAR_ENON))
        return out("the north side (34:7-9) — from the great sea by Mount Hor and Lebo-hamath to Zedad, Ziphron and Hazar-enan; the border's own verb three Bible seats all here", ['borders_declared'])
    if ask == 'the_east':
        ink('34:10-12', 'the east side — %s; "the east border" %s (one seat; the Hitpael "mark out for yourselves" %s); Shepham %s; "the Riblah" with the article %s (the exile\'s ten without it); Ain %s; "the shoulder of the sea of Chinnereth" %s; "to the Jordan" %s; the Salt Sea again — THE LOOP' % ([p[1] for p in SIDES['east']['points']], EAST_BORDER, MARK_HIT, SHEPHAM, RIBLAH, AIN, SHOULDER_CHIN, TO_JORDAN))
        return out("the east side (34:10-12) — from Hazar-enan by Shepham, Riblah east of Ain, the shoulder of the sea of Chinnereth and the Jordan to the Salt Sea: the loop closes", ['borders_declared'])
    if ask == 'the_loop':
        ink('34:3, 12', 'the Salt Sea at both ends — %s; "by its borders round about" the inclusio (%s); "round about" in Numbers %s' % (SALT_SEA, BY_ITS_BORDERS, ROUND_NUM))
        move('Bekhorot 55a:10', "one border round about — the demarcations within not borders")
        dat('the row the_jordan_as_border: %s' % data['the_jordan_as_border']['value'])
        return out("the loop (34:3, 34:12) — the Salt Sea at both ends, 'by its borders round about' the inclusio: all the land one border (Bekhorot 55a:10)", ['borders_declared'])
    if ask == 'the_points':
        ink('34:3-12', '%d proper-name tokens on the four sides (south %d, west %d, north %d, east %d) — each with its lemma\'s seats outside the chapter in the DATA row' % (len(NUM_POINTS), *[len(SIDES[s]['points']) for s in SIDES]))
        dat('the row the_four_sides: the list itself — a DATA row, one status on the land; the refused alternative a line per side')
        return out("the points (34:3-12) — twenty-seven proper-name tokens: south eleven, west none (the great sea alone), north eight, east eight; the data row the status's value", ['borders_declared'])
    if ask == 'judahs_border':
        ink('34:3-5 / Joshua 15:1-4', '%d of the %d tokens of 34:3-5 stand in Judah\'s south border (with repeats); Hazar-addar split into Hezron and Addar (Joshua 15:3); Azmon plene there (%s); Joshua 15:4 keeps one "to you" — the spec\'s pronoun in the run; "the end of the Salt Sea" %s' % (len(SHARED_S), len(NUM_S), AZMON_JOSH, END_SALT))
        return out("Judah's south border is the land's (Joshua 15:1-4) — twenty-nine of the forty-three tokens of 34:3-5 stand there; Hazar-addar split in two; Azmon plene; one 'to you' kept in the run", ['accepted'])
    if ask == 'the_goings_out':
        ink('34:4, 5, 8, 9, 12', '"its goings-out" %s + the bare form at 34:8 = THE TORAH\'S FIVE, all here; Joshua\'s borders %d verses with the word' % (GOINGS, len(GOINGS_JOSH)))
        return out("its goings-out — the outlet-word's five Torah seats all in this chapter (34:4, 5, 8, 9, 12); Joshua's borders say it again and again", ['accepted'])
    if ask == 'the_written_singular':
        ink('34:4', '"and it shall be" — the written singular %r, UNPOINTED in the DB (the written form); the clause\'s four other seats written plural (34:5, 8, 9, 12); Joshua 15:4 the same clause with the written singular' % _PT[('Num', 34, 4)][8])
        return out("the written singular read plural (34:4) — the chapter's one written-and-read pair; the DB writes the written form unpointed; Joshua 15:4 the same clause", ['accepted'])
    if ask == 'the_marking_verb':
        ink('34:7, 8, 10', '"you shall mark out" %s — three Bible seats all here (34:7, 8 Piel; 34:10 Hitpael %s); Proverbs 23:3, 23:6, 24:1 "do not DESIRE" its consonants, told apart by the points and the stem; Joshua marks with another verb; Onkelos "direct yourselves"' % (MARK, MARK_HIT))
        return out("you shall mark out (34:7, 8, 10) — the border's own verb, three Bible seats all here; Proverbs' 'desire' the homograph by the points", ['accepted'])
    if ask == 'the_second_mount_hor':
        ink('34:7-8', 'Mount Hor %s (the exact pair; 34:8 "from Mount Hor"); the name\'s twelve Torah seats %s — ten Aaron\'s, two the border\'s %s' % (HOR, HOR_LEMMA, HOR_BORDER))
        move('cold_run_chukat (CALL) — CK.edom_and_hor(two_mount_hors) = %s' % CK_TWO[0], "the chukat runner's row NAMES this chapter's Mount Hor")
        dat('the row the_two_mount_hors: %s' % data['the_two_mount_hors']['value'])
        return out("the second Mount Hor (34:7-8) — the name's twelve Torah seats, ten Aaron's and two the north border's; the chukat runner's row by CALL; Onkelos spells the two differently", ['accepted'])
    if ask == 'the_great_sea':
        ink('34:6-7', '"the great sea" plene %s and DEFECTIVE %s in adjacent verses — the defective phrase\'s one seat' % (GREAT_SEA, GREAT_SEA_DEF))
        return out("the great sea plene at 34:6 and defective at 34:7 — the defective phrase's one seat", ['accepted'])
    if ask == 'the_sea_as_west':
        ink('34:3-12', 'the sea-token %d times — the west twice, the great sea twice, the Salt Sea twice, Chinnereth once: %s; ONKELOS splits "the west" from "the sea"' % (len(SEA_TOKENS), SEA_TOKENS))
        return out("the sea as the west — one token seven times in the sides (the west, the great sea, the Salt Sea, Chinnereth); Onkelos splits it", ['accepted'])
    if ask == 'the_side_word':
        ink('34:3 / Exodus 27:9, 13', '"side" — the bare token %s (the field\'s corner and the beard\'s the homographs by sense); with the prefix %d Torah seats, Exodus 27:9 %s the court\'s south side, 27:13 %s the east side — "eastward toward the sunrise" %s = 34:15\'s phrase; Numbers gives the south alone the side-word' % (SIDE_T, len(SIDE_L_T), words(27, 9, 'Exod')[4:7], words(27, 13, 'Exod')[2:5], SUNRISE))
        return out("the side-word is the tabernacle's (34:3) — the court's south side Exodus 27:9 and its east side 27:13 carry it with the prefix; the bare token's five Torah seats include Leviticus's field-corner and beard-corner, homographs by sense; 'eastward toward the sunrise' (34:15) the court's east side", ['accepted'])
    if ask == 'the_blotting_verb':
        ink('34:11', '"and it shall REACH the shoulder of the sea of Chinnereth" — the token %s: the sotah\'s scroll blotted into the water (5:23), a name blotted out (Deuteronomy 29:19), tears wiped away (Isaiah 25:8), and this border — one pointing at all four; Onkelos "reach" here, "blot" at 5:23' % REACH)
        move('cold_run_naso (CALL) — NS.sotah(scroll_erasure) = %s' % NS_ERASURE[0], "the blotting's own cell (5:23) READ for the other sense — FALSE for the sotah's rule: a homograph by sense")
        return out("and it shall reach (34:11) — the blotting verb's token (5:23; Deuteronomy 29:19; Isaiah 25:8): the border reaches, the priest blots — a homograph by sense, the sotah's cell by CALL", ['accepted'])
    if ask == 'chinnereth':
        ink('34:11', '"the shoulder of the sea of Chinnereth" %s; "the sea of Chinnereth" %s; the name %s — Joshua 19:35\'s Chinnereth in Naphtali; Onkelos "the sea of Gennesar" (its one seat)' % (SHOULDER_CHIN, SEA_CHIN, CHIN_LEMMA))
        move('Bava Batra 122a:6 (credited)', "'Naphtali emerges, and with it the boundary of GINNOSAR' — the lottery names Naphtali's boundary by the translation's word for this sea")
        return out("the sea of Chinnereth (34:11) — two seats of the phrase, seven of the name; Onkelos 'Gennesar' — the shelf's lottery names Naphtali's boundary by that word (Bava Batra 122a:6)", ['accepted'])
    if ask == 'the_spies_walked_it':
        ink('34:3, 8 / 13:21', '"from the wilderness of Zin" %s and defective "Lebo-hamath" %s — each at exactly two seats: 13:21 and this chapter; the spies\' range the border\'s length' % (WILD_ZIN, LEBO))
        move('cold_run_shelach (CALL) — SL.spies(one_per_tribe) = %s' % SL_ONE[0], "the spies' roster and range")
        return out("the spies walked the border's length — 'from the wilderness of Zin' and 'Lebo-hamath' each at two seats: 13:21 and 34:3, 34:8", ['accepted'])
    if ask == 'ezekiels_order':
        ink('Ezekiel 47:13-20', 'the prophet\'s sides north (47:15), east (47:18), south (47:19), west (47:20) — against the chapter\'s south, west, north, east; %d tokens shared; 47:13 opens with "you shall inherit" (34:13\'s), 47:14 with "shall fall to you as an inheritance" (34:2\'s)' % len(EZEK_SHARED))
        dat('the row ezekiels_order: %s — OBSERVED, no link' % data['ezekiels_order']['value'])
        return out("Ezekiel's order — north, east, south, west against the chapter's south, west, north, east; twenty-nine tokens shared; observed, no link", ['accepted'])
    if ask == 'the_promised_extents':
        ink('34:3-12', 'no river, Euphrates, Lebanon or western sea in the chapter — the covenant\'s "river of Egypt" (Genesis 15:18) another word than "the brook of Egypt" (34:5)')
        dat('the row the_promised_extents: %s — OBSERVED, no verdict' % data['the_promised_extents']['value'])
        return out("the four promised extents (Genesis 15:18, Exodus 23:31, Deuteronomy 1:7, 11:24; Joshua 1:4) — no river, Euphrates, Lebanon or western sea in the chapter: another description, observed", ['accepted'])
    if ask == 'the_sea_as_border':
        move('Gittin 8a:4, 8a:6 (the Tosefta Terumot 2:12)', "the Rabbis: a string from Turei Amnon in the north to the River of Egypt in the south — the islands inward the land")
        move('Gittin 8a:5', "Rabbi Yehuda: the sea itself directly across from the land is the land — from 34:6")
        dat('the row the_sea_as_border: %s' % data['the_sea_as_border']['value'])
        return out("the sea as a border, two ways (Gittin 8a:4-7 on 34:6) — the Rabbis' string over the islands between the ink's two corners, or Rabbi Yehuda's sea itself: a data row", ['accepted'])
    if ask == 'the_jordan_as_border':
        move('Bekhorot 55a:14', "Rabbi Shimon ben Yochai: 'beyond the Jordan at Jericho' (34:15) — as Jericho is Canaan's, the Jordan is Canaan's")
        move('Bekhorot 55a:10', "'by its borders round about' (34:12) — one border")
        dat('the row the_jordan_as_border: %s' % data['the_jordan_as_border']['value'])
        return out("the Jordan as a border, two ways (Bekhorot 55a:10 on 34:12; 55a:14 on 34:15) — one border round about, or the river Canaan's from 'at Jericho': a data row", ['accepted'])
    if ask == 'the_three_lands':
        move('Mishnah Sheviit 6:1, 9:2; Tosefta Sheviit 4:4; Mishnah Gittin 1:2', "the shelf's own border lines — two holdings' lines for the sabbatical law; Rekem, Ashkelon, Akko for the bills")
        ink('34:4', 'Onkelos "Rekem Geah" for Kadesh-barnea — the Mishnah\'s east point (Gittin 1:2) is the translation\'s name of the chapter\'s south-east corner')
        dat('the row the_three_lands: %s' % data['the_three_lands']['value'])
        return out("the shelf's own border points — the three lands of Sheviit 6:1 inside 34's one border; the bills' Rekem the translation's Kadesh-barnea of 34:4 (Mishnah Gittin 1:2): a data row", ['accepted'])
    return out('no verdict in span', [FX.NONE])
# ===== F3: MOSES' RESTATEMENT (Num 34:13-15) — the relay; the nine and a half a run citation; no write ==========
def moses_restatement(case, data):
    del P[:]
    ask = case['ask']
    if ask == 'the_relay':
        ink('34:13', '"and Moses commanded the children of Israel, saying" — %s: the phrase\'s TWO Torah seats; 36:5\'s is the installing act command_relayed (THE TENT sitting 4)' % RELAY)
        dat('the row the_relay_form: %s — law_borders installed_by BOOT with the class named; whether a relay in this form installs is the second pass\'s D2 question' % data['the_relay_form']['value'])
        return out("and Moses commanded the children of Israel (34:13) — the relay of 34:1-12 in the form 36:5's installing act took: the D2 question of the second pass, the class named", ['accepted'])
    if ask == 'the_nine_and_a_half':
        ink('34:13, 15', 'the parser [%d] at 34:13 and [%d] at 34:15 (the construct "two of", the caret) with the two halves = %d; "to the nine tribes and the half tribe" %s (Joshua 14:2 the other seat); "nine" in the construct %s — every one the nine tribes; "the two tribes and the half tribe" %s' % (NINE, TWO, NINE + TWO + 1, NINE_HALF, NINE_CONSTRUCT, TWO_HALF))
        dat('the row the_nine_and_a_half: %s' % data['the_nine_and_a_half']['value'])
        return out("the nine tribes and the half tribe, the two tribes and the half tribe (34:13, 34:15) — [9] and [2] with the two halves = twelve; 'nine' in the construct three Bible seats, all the nine tribes", ['accepted'])
    if ask == 'one_tribe_noun':
        ink('34:13-28', 'the staff-word %d times in the chapter, the other tribe-word NEVER; 32:33 gave "the half tribe of Manasseh" with the other word (the neighbour); Joshua 13:7 says the nine with the other word %s' % (len(MATTEH), NINE_HALF_OTHER))
        return out("one tribe-noun — the staff-word eighteen times in the chapter and the other never; 32:33's the neighbour; Joshua 13:7 says the nine with the other word", ['accepted'])
    if ask == 'the_grant_read':
        ink('34:14-15', '"the two tribes and the half tribe HAVE TAKEN THEIR INHERITANCE beyond the Jordan at Jericho" — "took their inheritance" %s (always the two and a half); "beyond the Jordan at Jericho" %s' % (TOOK, BEYOND))
        move('cold_run_gad_reuben (CALL) — GR.the_grant(three_parties) = %s' % GR_THREE[0][:90], "32:33's three transfers on the tape (holding_given on the sons of Gad, the sons of Reuben, the half tribe of Manasseh) — A RUN CITATION: the line writes nothing (CW4 reads the ledger)")
        move('cold_run_gad_reuben (CALL) — GR.the_grant(not_by_lot) = %s' % GR_NOTLOT[0][:70], "the east by Moses' word, not by the lot of 26:55")
        return out("the two and a half have taken their inheritance (34:14-15) — a run citation of 32:33's three transfers on the tape; the line writes nothing", ['accepted'])
    if ask == 'the_count':
        move('cold_run_gad_reuben (CALL) — GR.the_grant(the_count) = %s' % GR_COUNT[0][:80], "43,730 + 40,500 + 52,700 ÷ 2 = 110,580 from the second census")
        ink('34:14', '43730 + 40500 + 52700 // 2 = %d' % COUNT_TWO_HALF)
        dat('the row the_nine_and_a_half: count_two_and_a_half = %d' % data['the_nine_and_a_half']['value']['count_two_and_a_half'])
        return out("the two and a half's count — 110,580 by CALL (43,730 + 40,500 + 52,700 ÷ 2 from the second census)", ['accepted'])
    if ask == 'the_pair':
        ink('34:14', '"the tribe of the sons of the Reubenite … the tribe of the sons of the Gadite" — the gentilics %s / %s: THE PAIR\'S FIRST SEAT; the Gadite\'s token also "the kid" (Genesis 38:23, Judges 14:6) — a homograph by token' % (REUBENITE, GADITE))
        return out("the Reubenite and the Gadite (34:14) — the pair's first seat; the Gadite's token is also 'the kid' at Genesis 38:23 and Judges 14:6", ['accepted'])
    if ask == 'joshuas_receipt':
        ink('34:13 / Joshua 14:2', 'Joshua 14:2 %s quotes 34:13\'s %s under "as the LORD commanded by the hand of Moses" %s (Joshua 21:8 the form\'s other seat); NO receipt in the chapter — "as the LORD commanded Moses" in Numbers %d seats, none in 34' % (words(14, 2, 'Josh')[-4:], words(34, 13)[16:20], RECEIPT_HAND, len(RECEIPT_NUM)))
        return out("Joshua 14:2's receipt — 'as the LORD commanded by the hand of Moses, to the nine tribes and the half tribe' quotes 34:13 outside the Torah; no receipt in the chapter", ['accepted'])
    if ask == 'the_lot_by_call':
        ink('34:13', '"this is the land which you shall INHERIT BY LOT" — "by lot" in the Torah %s; the reflexive stem %s (Ezekiel 47:13 the same)' % (BY_LOT_T, INHERIT_HIT))
        move('cold_run_second_census (CALL) — C2.the_land(by_lot) = %s; C2.DATA[division_by] = %s' % (C2_LOT[0], C2.DATA['division_by']['value']), "the OPEN divide_the_land debit (26:52-56) CITED, not rewritten — VIA second_census as at 32:18 and 33:54")
        move('cold_run_journeys (CALL) — JO.the_command(the_lot_restated) = %s' % JO_LOT[0][:80], "33:54's restatement the same way")
        return out("you shall inherit by lot (34:13) — 26:52-56's lot by CALL, the open debit cited a third time (32:18, 33:54, here), not rewritten", ['accepted'])
    return out('no verdict in span', [FX.NONE])


# ===== F4: THE DIVIDERS (Num 34:16-18) — the standing party named; the doubling; the court that owes ===========
def the_dividers(case, data):
    del P[:]
    ask = case['ask']
    if ask == 'the_names_form':
        ink('34:17, 19', '"these are the names of the men" — %s: the spies\' roster (13:16) and this; 34:19 with the conjunction %s' % (NAMES_MEN, words(34, 19)[:3]))
        return out("these are the names of the men (34:17, 34:19) — the rosters' heading, 13:16's and this", ['dividers_named'])
    if ask == 'the_triad':
        ink('34:17', '"Eleazar the priest and Joshua son of Nun" as one phrase — %s: this and Joshua\'s two runs (14:1, 19:51)' % TRIAD)
        move('cold_run_gad_reuben (CALL) — GR.the_acceptance_and_the_charge(the_commission) = %s' % GR_COMM[0][:90], "32:28's charge to the same triad — the dividers of the land written on already (the Gilead charge OPEN)")
        move('Bava Batra 122a:4-6 (credited)', "the lottery's picture — Eleazar with the Urim, Joshua and all Israel before him, two receptacles: THE DIVIDERS AT WORK")
        return out("Eleazar the priest and Joshua son of Nun (34:17) — the triad's three Bible seats: this and Joshua 14:1, 19:51; 32:28's charge by CALL; the lottery's picture on the shelf", ['dividers_named'])
    if ask == 'the_three_stems':
        ink('34:13, 17-18, 29', 'the one root in three stems — the reflexive 34:13 (%s), the plain 34:17-18 (%s; "to divide the land" %s), the INTENSIVE 34:29 (its other three seats Joshua\'s runs %s, %s); one skin "to divide" / "to the brook" %s — the points decide; THE OBJECT SWITCHES: the land at 34:17 %s, the people at 34:29 %s' % (INHERIT_HIT, INHERIT_QAL, TO_DIVIDE_LAND, PIEL_MOSES, PIEL_RUNS, TO_DIVIDE, words(34, 17)[4:8], words(34, 29)[4:8]))
        return out("the one root in three stems — the reflexive (34:13), the plain (34:17-18), the intensive (34:29) whose other three seats are Joshua's runs; the object switching from the land to the people", ['accepted'])
    if ask == 'the_distributive':
        ink('34:18', '"one prince, one prince from a tribe" %s — the parser [%d, %d]; the pair\'s bare form %s; "one man, one man" %s; the kin by the same parser %s' % (DOUBLING, ONE_ONE[0], ONE_ONE[1], ONE_PRINCE_PAIR, ONE_MAN_PAIR, {('%s %d:%d' % k): v for k, v in KIN.items()}))
        move('cold_run_shelach (CALL) — SL.spies(one_per_tribe) = %s' % SL_ONE[0], "13:2's doubling")
        move('cold_run_naso (CALL) — NS.dedication(per_day) = %s' % NS_PER_DAY[0][:60], "7:11's doubling")
        move('cold_run_korach (CALL) — KR.plague_and_staffs(staffs_count) = %s' % KR_STAFFS[0][:70], "17:21's doubling with the twelve")
        dat('the row the_distributive_doubling: %s' % data['the_distributive_doubling']['value'])
        return out("one prince, one prince from a tribe (34:18) — the distributive doubling read [1, 1]: the spies, the dedication and the rods by CALL; Joshua's stones and embassy the runs", ['dividers_named'])
    if ask == 'the_court_that_owes':
        move('cold_run_zelophehad (CALL) — ZL.the_daughters(the_run) = %s' % ZL_RUN[0][:80], "the daughters' holding owed at 27:7 paid at Joshua 17:4 'before Eleazar the priest and before Joshua' — the dividers the court that owes it (the zelophehad runner's token table reads 34:17 so)")
        move('cold_run_shelach (CALL) — SL.decree(caleb_entitlement) = %s' % SL_CALEB[0][:70], "Caleb's Hebron paid at Joshua 14:13 before the same court")
        ink('34:17', 'Caleb\'s holding_owed OPEN on the tape since 14:24 and the daughters\' since 27:4 — both paid before the dividers outside the Torah (CW7)')
        return out("the court that owes — the daughters' holding (paid at Joshua 17:4 before Eleazar and Joshua) and Caleb's Hebron (Joshua 14:13): the dividers the payers, by CALL", ['accepted'])
    if ask == 'only_excludes':
        move('cold_run_second_census (CALL) — C2.the_land(only_excludes) = %s' % C2_ONLY[0], "'only by lot' excludes Joshua and Caleb — not by the lot they administer (Bava Batra 122a:12)")
        return out("'only' excludes Joshua and Caleb (Bava Batra 122a:12) — the two dividers' own portions not by the lot they administer: by CALL", ['exempt'])
    if ask == 'the_princes_as_agents':
        move('Kiddushin 42a:6', "Rav Giddel: the law of agency from 34:18 — refused, since minors have no agency and the princes divided for them")
        move('Kiddushin 42a:8', "Rava bar Rav Huna: the court appoints a steward for orphans who come to divide, to their disadvantage and to their benefit — from 34:18")
        dat('the row the_princes_as_agents: %s' % data['the_princes_as_agents']['value'])
        return out("the princes as agents or stewards (Kiddushin 42a:6-8 on 34:18) — agency asked and refused, the court's steward for orphans the verse's teaching: a data row", ['accepted'])
    if ask == 'the_seventy_one':
        move('Sanhedrin 16a:2', "Ulla: the first division by seventy-one elders — a tribes' border dispute before the Great Sanhedrin")
        move('Sanhedrin 16a:3', "refused: the first division needed the lots, the Urim and all Israel")
        dat('the row the_seventy_one: %s' % data['the_seventy_one']['value'])
        return out("the seventy-one at the first division (Sanhedrin 16a:2-3) — Ulla's likeness refused: the lots, the Urim and all Israel; the ink's dividers twelve by name: a data row", ['accepted'])
    if ask == 'the_debit':
        ink('34:29', '"these are they whom the LORD commanded to divide to the children of Israel in the land of Canaan" — the closer %s; the debit on the dividers OPEN BY DESIGN to Joshua 14:1 and 19:51' % CLOSER)
        return out("the dividers commanded (34:29) — a debit to divide the inheritance to the children of Israel in Canaan, OPEN BY DESIGN to Joshua 14:1 and 19:51", ['commanded'])
    return out('no verdict in span', [FX.NONE])


# ===== F5: THE ROSTER (Num 34:19-29) — the twelve as rows; the order matching none ==========================
def the_roster(case, data):
    del P[:]
    ask = case['ask']
    if ask == 'the_roster':
        ink('34:19-28', 'the ten by tribe — %s; the fathers %s; the title at %s; "the children of" absent at %s; the conjunction absent at %s' % ([r['tribe'] for r in ROSTER], [r['father'] for r in ROSTER], [r['tribe'] for r in ROSTER if r['title']], [r['tribe'] for r in ROSTER if not r['sons_of']], [r['tribe'] for r in ROSTER if not r['conjunction']]))
        dat('the row the_roster: the twelve — Eleazar, Joshua and the ten; the population table\'s named rows (as_of Num 34:17-29)')
        return out("the roster (34:19-28) — ten princes by tribe with their fathers; the title at seven rows, dropped at Judah's, Simeon's and Benjamin's; the twelve enter the population table", ['dividers_named'])
    if ask == 'calebs_five_words':
        ink('34:19 / 13:6', '34:19\'s five %s = 13:6\'s %s — the spy\'s line at the dividers\'; "Caleb son of Jephunneh" %s' % (words(34, 19)[3:8], words(13, 6), CALEB_JEPH))
        move('cold_run_shelach (CALL) — SL.spies(joshua_caleb_equal) = %s' % SL_EQUAL[0], "Caleb first at 13:6")
        return out("Caleb's five words (34:19 = 13:6) — the spy's line repeated at the dividers'; Caleb son of Jephunneh eight Torah seats", ['accepted'])
    if ask == 'the_survivors':
        move('cold_run_shelach (CALL) — SL.decree(exceptions) = %s; SL.decree(spies_portions) = %s' % (SL_EXC[0], SL_PORTIONS[0][:60]), "the two survivors of the spies' roster")
        ink('34:17, 19', 'Joshua son of Nun (34:17; 13:8 "Hoshea son of Nun") and Caleb — the ONLY persons of chapter 13\'s roster here; the spies\' tribes %s' % SL.SPY_TRIBES)
        return out("the two survivors — Joshua and Caleb the only persons of the spies' roster among the dividers; the exceptions of 14:24, 14:30 by CALL", ['accepted'])
    if ask == 'no_prince_of_chapter_one':
        move('cold_run_naso (CALL) — NS.NAMES = %s' % NS.NAMES, "the twelve princes of 1:5-15 (the dedication's twelve)")
        move('cold_run_bamidbar (CALL) — CB.census(orders) = %s' % CB_ORDERS[0], "the roll's orders")
        ink('34:19-28', 'NONE of the twelve among the ten; one father\'s name shared — Ammihud %s (Ephraim\'s Elishama 1:10; Simeon\'s Shemuel; Naphtali\'s Pedahel)' % FATHER_SEATS['עמיהוד'])
        return out("no prince of chapter 1 among the ten (by CALL); Ammihud the one father's name shared — three tribes' fathers' name (1:10; 34:20; 34:28)", ['accepted'])
    if ask == 'only_here':
        ink('34:19-28', 'nowhere else BY TOKEN %s (eight — Hanniel among them, his namesake at 1 Chronicles 7:39 spelled otherwise); BY LEMMA %s (ten — Ephod the vestment\'s consonants at Exodus 28:15, 39:8; Chislon Joshua 15:10\'s Chesalon; Shelomi "my peace-offerings"; Hanniel out); Shemuel %d verses by lemma, this the first; Kemuel %s; Elizaphan %s; Paltiel %s; Bukki %s' % (ONLY_HERE_TOKEN, ONLY_HERE_LEMMA, len(PRINCE_SEATS['שמואל']), PRINCE_SEATS['קמואל'], PRINCE_SEATS['אליצפן'], PRINCE_SEATS['פלטיאל'], PRINCE_SEATS['בקי']))
        dat('the reading\'s "eight names only here" was a MIXED measure — filed at the compile (the ledger\'s CORRECTIONS block)')
        return out("the names nowhere else — eight by token (Hanniel among them), ten by lemma (Ephod, Chislon, Shelomi homographs by token; Hanniel's lemma shared); Shemuel the prophet's name's first seat; seven of the ten carry God's name, none of the fathers", ['accepted'])
    if ask == 'the_order':
        ink('34:19-28', 'the order %s against sixteen lists — matching %s; Manasseh before Ephraim in %s; Zebulun before Issachar in %s; the four northern in Joshua\'s lot order %s' % (ROSTER_ORDER, MATCHES or 'none', MAN_BEFORE_EPH, ZEB_BEFORE_ISS, LOTS_19))
        dat('the row the_roster_order: matching none — the cause unnamed, the declared shelf silent')
        return out("the order matches no other roster (sixteen lists) — Manasseh before Ephraim as the second census and Genesis 46 in the Torah, Zebulun before Issachar as the two blessings, the four northern in Joshua's lot order", ['accepted'])
    if ask == 'the_closer':
        ink('34:29', '"these are they whom the LORD commanded" %s — the closer without a noun, one seat; no receipt "as the LORD commanded Moses" in the chapter (Numbers\' %d seats); the receipt Joshua 14:2\'s' % (CLOSER, len(RECEIPT_NUM)))
        return out("the closer (34:29) — 'these are they whom the LORD commanded to divide', one seat; no receipt in the chapter — Joshua 14:2's is outside the Torah", ['commanded'])
    if ask == 'the_rows':
        ink('34:17-28', 'TWELVE NAMED ROWS — Eleazar (levi, "the priest"), Joshua (ephraim by 13:8, "son of Nun"), and the ten by tribe with their fathers and the title\'s clause; as_of Num 34:17-29 — the register gate\'s Num 34 seat PAID')
        dat('the population table\'s named grain (8b): the persons the roll names enter the table — the first register reached since the table was built')
        return out("the twelve named rows — the roll's persons enter the population table (grain named, as of Num 34:17-29): the register gate's seat paid", ['dividers_named'])
    return out('no verdict in span', [FX.NONE])


# ---- THE WRAP — the daemon, the scene, the narrative ------------------------------------------------------
PRINCE_TOKENS = {'כלב': 'caleb', 'שמואל': 'shemuel-ben-ammihud', 'אלידד': 'elidad-ben-chislon', 'בקי': 'bukki-ben-jogli', 'חניאל': 'hanniel-ben-ephod', 'קמואל': 'kemuel-ben-shiphtan', 'אליצפן': 'elizaphan-ben-parnach', 'פלטיאל': 'paltiel-ben-azzan', 'אחיהוד': 'ahihud-ben-shelomi', 'פדהאל': 'pedahel-ben-ammihud'}   # the rows' subjects — the registry's id where one exists (caleb; eleazar and joshua through the map), the naso runner's name-ben-father form for the rest
NAMED_ROWS = [('eleazar', 'אלעזר', 'levi', None, 'the priest (34:17)', 17), ('joshua', 'יהושע', JOSHUA_TRIBE, 'נון', 'son of Nun (34:17; the tribe by 13:8)', 17)] + \
             [(PRINCE_TOKENS[r['prince']], r['prince'], r['tribe'], r['father'], ('prince (34:%d)' % r['verse']) if r['title'] else ('named without the title (34:%d)' % r['verse']), r['verse']) for r in ROSTER]
assert len(NAMED_ROWS) == 12 and NAMED_ROWS[2][0] == 'caleb' and NAMED_ROWS[1][2] == 'ephraim', NAMED_ROWS[:3]

def law_borders(event, world):
    """Num 34:1-29 (cold_run_borders.py F1-F5). given_at Num 34:1; installed_by boot — A LAW IN THE DIVINE VOICE relayed at 34:13 in 36:5's
    form (the class named in the registry, the second pass decides). THREE TAPE LINES: the borders commanded (34:1-12) — ONE status on the
    land of Canaan valued the four sides; Moses' restatement (34:13-15) — NO write (the grant read, the lot cited); the dividers named
    (34:16-29) — a status and a debit on the dividers of the land (the party 32:28 charged) and TWELVE named rows in the population table.
    The exam's two case kinds dispatch to the cells with LITERAL effects per kind (2b's form — an unnamed effect is a KeyError)."""
    k, src = event['kind'], event['case_source']
    E_ = lambda eff, s, cp=None, amount=None, due=None, law='', value=None: {'effect': eff, 'subject': s, 'counterparty': cp, 'amount': amount, 'due': due, 'value': value if value is not None else True, 'source_law': law, 'case_source': src}
    day = event.get('day', world.clock.day)      # THE SEQUENTIAL RUN: the event's own day
    # ---- the three lines (page_order at the counter's day, no marker in the chapter) ----
    if k == 'borders_commanded':
        return [E_('borders_declared', 'the-land-of-canaan', value=SIDES_EN, law='F2 [INK 34:2 "this is the land that shall fall to you as an inheritance, the land of Canaan BY ITS BORDERS" … 34:12 "this shall be your land by its borders round about" — ONE STATUS ON THE LAND: the four sides in the ink\'s order with their named points (the DATA row the_four_sides, twenty-seven proper-name tokens; Joshua 15:1-4 Judah\'s run of the south; Ezekiel 47 the kin in another order; the second Mount Hor the chukat runner\'s row); nothing on the people — the lot\'s debit of 26:52-56 OPEN, cited (CW3); the shelf: the sea within the border or the islands by the string (Gittin 8a:4-7), one border round about (Bekhorot 55a:10), the Jordan Canaan\'s (55a:14)]')]
    if k == 'moses_commanded_the_nine_and_a_half':
        return []                                                                                        # THE EMPTY WATCH: the relay writes nothing — the grant's three transfers and the lot's open debit are read at the checkpoints (CW3, CW4); Joshua 14:2's receipt outside the Torah
    if k == 'dividers_named':
        for subj, person, tribe, father, status, v in NAMED_ROWS:
            world.row('population', {'grain': 'named', 'as_of': 'Num 34:17-29', 'subject': subj, 'person': person, 'tribe': tribe, 'father': father, 'status': status, 'source': src, 'note': 'Num 34:%d' % v})   # the father column always present (None for Eleazar — 34:17 names no father; the second census runner's rows carry the column the same way): the tape's first run read a KeyError on the view                                                                # THE ROLL'S PERSONS ENTER THE TABLE (8b's law) — the register gate's Num 34 seat PAID
        return [E_('dividers_named', 'the-dividers-of-the-land', value='Eleazar the priest, Joshua son of Nun, and one prince from a tribe — Judah Caleb son of Jephunneh, Simeon Shemuel son of Ammihud, Benjamin Elidad son of Chislon, Dan Bukki son of Jogli, Manasseh Hanniel son of Ephod, Ephraim Kemuel son of Shiphtan, Zebulun Elizaphan son of Parnach, Issachar Paltiel son of Azzan, Asher Ahihud son of Shelomi, Naphtali Pedahel son of Ammihud (34:17-28)', law='F4 [INK 34:17 "these are the names of the men who shall divide the land for you: Eleazar the priest and Joshua son of Nun" — the party 32:28 charged as a body (its Gilead charge OPEN beside this write) gets its roster; 34:18 "one prince, one prince from a tribe" the distributive doubling; the triad\'s three Bible seats (34:17; Joshua 14:1, 19:51); the twelve rows in the population table (grain named, as_of Num 34:17-29)]'),
                E_('commanded', 'the-dividers-of-the-land', value='divide_the_inheritance_to_the_children_of_israel_in_canaan', law='F4 [INK 34:29 "these are they whom the LORD commanded to divide to the children of Israel in the land of Canaan" — the DEBIT on the dividers OPEN BY DESIGN: its runs Joshua 14:1 ("which Eleazar the priest and Joshua son of Nun … divided"), 17:14 (Joseph\'s claim answered), 19:51 (the lot before the LORD at Shiloh) — outside the Torah, THE READBACK\'s; the intensive stem\'s other three seats those runs; "only" excludes the two dividers\' own portions (Bava Batra 122a:12)]')]
    # ---- the exam's case kinds: each names LITERALLY every effect it can write (2b's form) ----
    if k == 'borders_case':
        fn = {'heading': the_land_and_its_fall}.get(event.get('cell'), the_four_sides)
        v, e, _ = fn(dict(event, ask=event['ask']), DATA); L = '%s [%s]' % ({'heading': 'F1'}.get(event.get('cell'), 'F2'), v); s_ = event['person']
        W = {'borders_declared': E_('borders_declared', s_, value=v, law=L), 'accepted': E_('accepted', s_, value=v, law=L), 'exempt': E_('exempt', s_, value=v, law=L)}
        return [W[x] for x in e if x != FX.NONE]
    if k == 'dividers_case':
        fn = {'restatement': moses_restatement, 'dividers': the_dividers}.get(event.get('cell'), the_roster)
        v, e, _ = fn(dict(event, ask=event['ask']), DATA); L = '%s [%s]' % ({'restatement': 'F3', 'dividers': 'F4'}.get(event.get('cell'), 'F5'), v); s_ = event['person']
        W = {'commanded': E_('commanded', s_, value=v, law=L), 'dividers_named': E_('dividers_named', s_, value=v, law=L), 'accepted': E_('accepted', s_, value=v, law=L), 'exempt': E_('exempt', s_, value=v, law=L)}
        return [W[x] for x in e if x != FX.NONE]
    return []


LINES = [
    ('Num 34:1-12 — and the LORD spoke to Moses, saying: command the children of Israel and say to them: when you are coming into the land Canaan, this is the land that shall fall to you as an inheritance, the land of Canaan by its borders; and your south side shall be from the wilderness of Zin on the hands of Edom, and your south border shall be from the end of the Salt Sea eastward; and the border shall turn for you south of the ascent of Akrabbim and pass to Zin, and its goings-out shall be south of Kadesh-barnea, and it shall go out to Hazar-addar and pass to Azmon; and the border shall turn from Azmon to the brook of Egypt, and its goings-out shall be at the sea; and the west border: you shall have the great sea and its border, this shall be your west border; and this shall be your north border: from the great sea you shall mark out for yourselves Mount Hor; from Mount Hor you shall mark out to Lebo-hamath, and the goings-out of the border shall be to Zedad; and the border shall go out to Ziphron, and its goings-out shall be Hazar-enan, this shall be your north border; and you shall mark out for yourselves the east border from Hazar-enan to Shepham; and the border shall go down from Shepham to Riblah east of Ain, and the border shall go down and reach the shoulder of the sea of Chinnereth eastward; and the border shall go down to the Jordan, and its goings-out shall be the Salt Sea; this shall be your land by its borders round about', 'israel'),
    ('Num 34:13-15 — and Moses commanded the children of Israel, saying: this is the land which you shall inherit by lot, which the LORD commanded to give to the nine tribes and the half tribe; for the tribe of the sons of the Reubenite by their fathers\' house and the tribe of the sons of the Gadite by their fathers\' house and the half tribe of Manasseh have taken their inheritance; the two tribes and the half tribe have taken their inheritance beyond the Jordan at Jericho, eastward toward the sunrise', 'moses'),
    ('Num 34:16-29 — and the LORD spoke to Moses, saying: these are the names of the men who shall divide the land for you: Eleazar the priest and Joshua son of Nun; and one prince, one prince from a tribe you shall take to divide the land; and these are the names of the men: for the tribe of Judah, Caleb son of Jephunneh; and for the tribe of the sons of Simeon, Shemuel son of Ammihud; for the tribe of Benjamin, Elidad son of Chislon; and for the tribe of the sons of Dan a prince, Bukki son of Jogli; for the sons of Joseph: for the tribe of the sons of Manasseh a prince, Hanniel son of Ephod; and for the tribe of the sons of Ephraim a prince, Kemuel son of Shiphtan; and for the tribe of the sons of Zebulun a prince, Elizaphan son of Parnach; and for the tribe of the sons of Issachar a prince, Paltiel son of Azzan; and for the tribe of the sons of Asher a prince, Ahihud son of Shelomi; and for the tribe of the sons of Naphtali a prince, Pedahel son of Ammihud; these are they whom the LORD commanded to divide to the children of Israel in the land of Canaan', 'israel'),
]
CLOSES = 'none — Caleb\'s holding_owed (14:24) and the daughters\' (27:4) are paid before the dividers OUTSIDE THE TORAH (Joshua 14:13, 17:4); the lot\'s debit (26:52-56) stays open, cited; the dividers\' Gilead charge (32:28-30) stays open beside the new debit'


def scene():
    """THE SCENE — the exam's rows replayed on the world engine (the exodus epoch): the exam's persons through the two case kinds."""
    with contextlib.redirect_stdout(io.StringIO()):
        w = WE.World(era='Num 34:1-29: the borders on the shelf — Gittin, Bekhorot, Kiddushin, Sanhedrin, Bava Batra, Sheviit on the engine (the exodus epoch)', epoch='exodus')
        w.laws = [law_borders]
        w.advance(w.clock.day_in('exodus', 40, 6, 1))
        # ---- the exam's persons through the two case kinds (LITERAL submits — the daemon gate parses no loop) ----
        w.submit({'kind': 'borders_case', 'subject': 'the-title-claim', 'person': 'the-title-claim', 'cell': 'heading', 'ask': 'the_land_canaan', 'case_source': 'Sanhedrin 91a:6 — the exam\'s row the_land_canaan'})
        w.submit({'kind': 'borders_case', 'subject': 'the-land-bound-rule', 'person': 'the-land-bound-rule', 'cell': 'heading', 'ask': 'the_land_bound_rule', 'case_source': 'Mishnah Kiddushin 1:9 (36b:8) — the exam\'s row the_land_bound_rule'})
        w.submit({'kind': 'borders_case', 'subject': 'the-one-border', 'person': 'the-one-border', 'cell': 'heading', 'ask': 'by_its_borders', 'case_source': 'Bekhorot 55a:10 — the exam\'s row by_its_borders'})
        w.submit({'kind': 'borders_case', 'subject': 'the-sea-within', 'person': 'the-sea-within', 'cell': 'sides', 'ask': 'the_sea_as_border', 'case_source': 'Gittin 8a:5 — the exam\'s row the_sea_as_border'})
        w.submit({'kind': 'borders_case', 'subject': 'the-islands', 'person': 'the-islands', 'cell': 'sides', 'ask': 'the_west', 'case_source': 'Gittin 8a:4-7 — the exam\'s row the_west'})
        w.submit({'kind': 'borders_case', 'subject': 'the-jordan-canaans', 'person': 'the-jordan-canaans', 'cell': 'sides', 'ask': 'the_jordan_as_border', 'case_source': 'Bekhorot 55a:14 — the exam\'s row the_jordan_as_border'})
        w.submit({'kind': 'borders_case', 'subject': 'the-three-lands', 'person': 'the-three-lands', 'cell': 'sides', 'ask': 'the_three_lands', 'case_source': 'Mishnah Sheviit 6:1; Gittin 1:2 — the exam\'s row the_three_lands'})
        w.submit({'kind': 'borders_case', 'subject': 'the-ginnosar', 'person': 'the-ginnosar', 'cell': 'sides', 'ask': 'chinnereth', 'case_source': 'Bava Batra 122a:6 — the exam\'s row chinnereth'})
        w.submit({'kind': 'dividers_case', 'subject': 'the-nine-and-a-half', 'person': 'the-nine-and-a-half', 'cell': 'restatement', 'ask': 'the_grant_read', 'case_source': 'Bekhorot 55a:14 — the exam\'s row the_grant_read'})
        w.submit({'kind': 'dividers_case', 'subject': 'the-relay', 'person': 'the-relay', 'cell': 'restatement', 'ask': 'the_relay', 'case_source': 'Num 36:5 (command_relayed) — the exam\'s row the_relay'})
        w.submit({'kind': 'dividers_case', 'subject': 'the-agent', 'person': 'the-agent', 'cell': 'dividers', 'ask': 'the_princes_as_agents', 'case_source': 'Kiddushin 42a:6 — the exam\'s row the_princes_as_agents'})
        w.submit({'kind': 'dividers_case', 'subject': 'the-lottery', 'person': 'the-lottery', 'cell': 'dividers', 'ask': 'the_triad', 'case_source': 'Bava Batra 122a:4 — the exam\'s row the_triad'})
        w.submit({'kind': 'dividers_case', 'subject': 'the-only-excludes', 'person': 'the-only-excludes', 'cell': 'dividers', 'ask': 'only_excludes', 'case_source': 'Bava Batra 122a:12 — the exam\'s row only_excludes'})
        w.submit({'kind': 'dividers_case', 'subject': 'the-seventy-one', 'person': 'the-seventy-one', 'cell': 'dividers', 'ask': 'the_seventy_one', 'case_source': 'Sanhedrin 16a:2 — the exam\'s row the_seventy_one'})
        w.submit({'kind': 'dividers_case', 'subject': 'the-court-that-owes', 'person': 'the-court-that-owes', 'cell': 'dividers', 'ask': 'the_court_that_owes', 'case_source': 'Bava Batra 118b:8 — the exam\'s row the_court_that_owes'})
        w.submit({'kind': 'dividers_case', 'subject': 'the-debit', 'person': 'the-debit', 'cell': 'dividers', 'ask': 'the_debit', 'case_source': 'Num 34:29 — the exam\'s row the_debit'})
        w.submit({'kind': 'dividers_case', 'subject': 'the-survivors', 'person': 'the-survivors', 'cell': 'roster', 'ask': 'the_survivors', 'case_source': 'Bava Batra 117b:2 — the exam\'s row the_survivors'})
        w.submit({'kind': 'dividers_case', 'subject': 'the-order', 'person': 'the-order', 'cell': 'roster', 'ask': 'the_order', 'case_source': 'Num 34:19-28 — the exam\'s row the_order'})
    n = lambda eid, eff: len([e for e in w.entity(eid).ledger if e['effect'] == eff])
    tset = len([l for l in w.log if l[0] == 'TIMER-SET']); tfire = len([l for l in w.log if l[0] == 'TIMER-FIRE']); tcan = len([l for l in w.log if l[0] == 'TIMER-CANCEL'])
    return ((n('the-title-claim', 'accepted'), n('the-land-bound-rule', 'accepted'), n('the-one-border', 'borders_declared'), n('the-sea-within', 'accepted'), n('the-islands', 'borders_declared'), n('the-jordan-canaans', 'accepted'), n('the-three-lands', 'accepted'), n('the-ginnosar', 'accepted'),
             n('the-nine-and-a-half', 'accepted'), n('the-relay', 'accepted'), n('the-agent', 'accepted'), n('the-lottery', 'dividers_named'), n('the-only-excludes', 'exempt'), n('the-seventy-one', 'accepted'), n('the-court-that-owes', 'accepted'), n('the-debit', 'commanded'), n('the-survivors', 'accepted'), n('the-order', 'accepted')),
            (tset, tfire, tcan, len(w.timers)),
            len(w.entities)), w
SCENE, _W = scene()
# THE PREDICTION (typed before the first run, NUMBERS_WALK.md "Sitting 14b"): every exam person written once — eighteen ones; no timer in the
# chapter (set 0, fired 0, cancelled 0, pending 0). ENTITIES: the exam's 18 persons alone (an entity is a written-on party; no counterparty written on).
SCENE_PREDICTED = ((1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1), (0, 0, 0, 0), 18)
assert SCENE == SCENE_PREDICTED, ('THE NUMBERS WALK: the scene moved from its prediction', SCENE, SCENE_PREDICTED)


def narrative():
    """THE NUMBERS WALK 14b (2026-09-13): the chapter's own acts AS HISTORY — the THREE lines of 34:1-29 at the counter's day (40, 6, 1),
    page-order after the journeys' three (33:1-56), on a world with this runner's daemon: 3 writes, no timer, no marker, two entities
    (the land of Canaan and the dividers of the land — moses and israel subjects with no write), no close, TWELVE population rows.
    Recorded by the sequential run's recorder and stitched onto the tape. Not a graded cell: the tuple below is a tripwire typed from the
    design; the sequence world's RUN tuple and CW1-CW9 grade the tape."""
    with contextlib.redirect_stdout(io.StringIO()):
        w = WE.World(era='Num 34:1-29: the borders on the tape — the four sides on the land, the relay, the dividers named (the exodus epoch)', epoch='exodus')
        w.laws = [law_borders]
        w.advance(w.clock.day_in('exodus', 40, 6, 1))
        # THE DAEMON GATE READS LITERAL SUBMITS ONLY — the three lines typed out
        w.submit({'kind': 'borders_commanded', 'subject': 'israel', 'sides': ['south', 'west', 'north', 'east'], 'points': 27, 'first': 'the wilderness of Zin', 'last': 'the Salt Sea', 'by_its_borders': True, 'case_source': LINES[0][0]})
        w.submit({'kind': 'moses_commanded_the_nine_and_a_half', 'subject': 'moses', 'to': 'israel', 'nine': 9, 'two': 2, 'halves': 2, 'by_lot': True, 'case_source': LINES[1][0]})
        w.submit({'kind': 'dividers_named', 'subject': 'israel', 'dividers': ['eleazar', 'joshua', 'caleb', 'shemuel-ben-ammihud', 'elidad-ben-chislon', 'bukki-ben-jogli', 'hanniel-ben-ephod', 'kemuel-ben-shiphtan', 'elizaphan-ben-parnach', 'paltiel-ben-azzan', 'ahihud-ben-shelomi', 'pedahel-ben-ammihud'], 'per_tribe': 1, 'case_source': LINES[2][0]})
    writes = len([l for l in w.log if l[0] == 'WRITE'])
    closes = len([e for ent in w.entities.values() for e in ent.ledger if e.get('closed_by')])
    rows = len([l for l in w.log if l[0] == 'ROW'])
    return (writes, len([l for l in w.log if l[0] == 'TIMER-SET']), len(w.entities), w.clock.eras['exodus'].date(w.clock.day)[1:], closes, rows, len(w.tables['population'])), w


NARRATIVE, _WN = narrative()
NARRATIVE_PREDICTED = (3, 0, 2, (6, 1), 0, 12, 12)   # NUMBERS_WALK.md "Sitting 14b": 3 writes (L1 1, L2 0, L3 2), no timer, TWO entities (the land of Canaan, the dividers of the land — the written-on parties; moses and israel subjects with no write), the counter's day (6, 1), no close, TWELVE rows = twelve ROW lines
assert NARRATIVE == NARRATIVE_PREDICTED, ('THE NUMBERS WALK: the borders\' narrative moved from its prediction', NARRATIVE, NARRATIVE_PREDICTED)
assert all(r['written_by'] == 'law_borders' and r['grain'] == 'named' and r['as_of'] == 'Num 34:17-29' for r in _WN.tables['population']) and [r['subject'] for r in _WN.tables['population']][:3] == ['eleazar', 'joshua', 'caleb'], _WN.tables['population'][:3]


# =====================================================================
# Motion 2 — THE TEST DATA: the answer sheet's rows (the docket's LAW rows).
# =====================================================================
CASES = [
    # F1 — the land and its fall
    ('Num 34:2 / Sifrei 1:2 — the command', lambda: the_land_and_its_fall({'ask': 'the_command'}, DATA), "command the children of Israel (34:2) — five Torah seats, the Sifrei's five; the one command without expense (Sifrei 1:2)"),
    ('Num 34:2 / 33:51 by CALL — when you come', lambda: the_land_and_its_fall({'ask': 'when_you_come'}, DATA), "when you are coming into the land Canaan (34:2) — the article on the land, none on the name; 33:51's entry clause by CALL"),
    ('Num 34:2 / Sanhedrin 91a:6 — the title claim', lambda: the_land_and_its_fall({'ask': 'the_land_canaan'}, DATA), "the land of Canaan (34:2) read as a title claim (Sanhedrin 91a:6) — the tape's answer canaan's status since Genesis 9:25"),
    ('Num 34:2, 13 / Deut 34:4 — this is the land', lambda: the_land_and_its_fall({'ask': 'this_is_the_land'}, DATA), "this is the land — 34:2 and 34:13, Deuteronomy 34:4 from Nebo, Joshua 13:2, Ezekiel 48:29"),
    ('Num 34:2 / 26:52-56 by CALL — shall fall', lambda: the_land_and_its_fall({'ask': 'shall_fall'}, DATA), "that shall fall to you as an inheritance (34:2) — the lot's verb at its one Torah seat with the inheritance; Onkelos 'be divided'; the lot's debit by CALL, cited"),
    ('Num 34:2 — as an inheritance', lambda: the_land_and_its_fall({'ask': 'as_an_inheritance'}, DATA), "as an inheritance (34:2) — three Torah seats: 26:53, 34:2, 36:2, all the land's"),
    ('Num 34:2, 12 / Josh 18:20, 19:49; Bekhorot 55a:10 — by its borders', lambda: the_land_and_its_fall({'ask': 'by_its_borders'}, DATA), "by its borders (34:2, 34:12) — the inclusio; Joshua 18:20 and 19:49 the closers; the border-word sixteen times: ONE STATUS ON THE LAND"),
    ('Num 34:1, 16 / 35:1 — the frames', lambda: the_land_and_its_fall({'ask': 'the_frame'}, DATA), "and the LORD spoke to Moses, saying (34:1, 34:16) — two divine frames with Moses' command between them; 35:1 adds the plains of Moab"),
    ('Mishnah Kiddushin 1:9; 37a:3-6 — the land-bound rule', lambda: the_land_and_its_fall({'ask': 'the_land_bound_rule'}, DATA), "the borders' legal reach — an obligation of the land inside the border, of the body everywhere (Mishnah Kiddushin 1:9; 37a:3-6): a data row, the classing Deuteronomy's"),
    # F2 — the four sides
    ('Num 34:3-5 — the south side', lambda: the_four_sides({'ask': 'the_south'}, DATA), "the south side (34:3-5) — from the wilderness of Zin on the hands of Edom to the brook of Egypt and the sea; eleven proper-name tokens; Joshua 15:1-4 Judah's run of it"),
    ('Num 34:6 / Gittin 8a:4-7 — the west border', lambda: the_four_sides({'ask': 'the_west'}, DATA), "the west border (34:6) — the great sea and its border: one word read two ways on the shelf (the sea itself, or the islands by the string — Gittin 8a:4-7)"),
    ('Num 34:7-9 — the north side', lambda: the_four_sides({'ask': 'the_north'}, DATA), "the north side (34:7-9) — from the great sea by Mount Hor and Lebo-hamath to Zedad, Ziphron and Hazar-enan; the border's own verb three Bible seats all here"),
    ('Num 34:10-12 — the east side', lambda: the_four_sides({'ask': 'the_east'}, DATA), "the east side (34:10-12) — from Hazar-enan by Shepham, Riblah east of Ain, the shoulder of the sea of Chinnereth and the Jordan to the Salt Sea: the loop closes"),
    ('Num 34:3, 12 / Bekhorot 55a:10 — the loop', lambda: the_four_sides({'ask': 'the_loop'}, DATA), "the loop (34:3, 34:12) — the Salt Sea at both ends, 'by its borders round about' the inclusio: all the land one border (Bekhorot 55a:10)"),
    ('Num 34:3-12 — the points (the data row)', lambda: the_four_sides({'ask': 'the_points'}, DATA), "the points (34:3-12) — twenty-seven proper-name tokens: south eleven, west none (the great sea alone), north eight, east eight; the data row the status's value"),
    ('Num 34:3-5 / Josh 15:1-4 — Judah\'s border', lambda: the_four_sides({'ask': 'judahs_border'}, DATA), "Judah's south border is the land's (Joshua 15:1-4) — twenty-nine of the forty-three tokens of 34:3-5 stand there; Hazar-addar split in two; Azmon plene; one 'to you' kept in the run"),
    ('Num 34:4, 5, 8, 9, 12 — the goings-out', lambda: the_four_sides({'ask': 'the_goings_out'}, DATA), "its goings-out — the outlet-word's five Torah seats all in this chapter (34:4, 5, 8, 9, 12); Joshua's borders say it again and again"),
    ('Num 34:4 / Josh 15:4 — the written singular', lambda: the_four_sides({'ask': 'the_written_singular'}, DATA), "the written singular read plural (34:4) — the chapter's one written-and-read pair; the DB writes the written form unpointed; Joshua 15:4 the same clause"),
    ('Num 34:7, 8, 10 / Prov 23:3 — the marking verb', lambda: the_four_sides({'ask': 'the_marking_verb'}, DATA), "you shall mark out (34:7, 8, 10) — the border's own verb, three Bible seats all here; Proverbs' 'desire' the homograph by the points"),
    ('Num 34:7-8 / 20:22 by CALL — the second Mount Hor', lambda: the_four_sides({'ask': 'the_second_mount_hor'}, DATA), "the second Mount Hor (34:7-8) — the name's twelve Torah seats, ten Aaron's and two the north border's; the chukat runner's row by CALL; Onkelos spells the two differently"),
    ('Num 34:6-7 — the great sea plene and defective', lambda: the_four_sides({'ask': 'the_great_sea'}, DATA), "the great sea plene at 34:6 and defective at 34:7 — the defective phrase's one seat"),
    ('Num 34:3-12 — the sea as the west', lambda: the_four_sides({'ask': 'the_sea_as_west'}, DATA), "the sea as the west — one token seven times in the sides (the west, the great sea, the Salt Sea, Chinnereth); Onkelos splits it"),
    ('Num 34:3 / Exod 27:9, 13 — the side-word', lambda: the_four_sides({'ask': 'the_side_word'}, DATA), "the side-word is the tabernacle's (34:3) — the court's south side Exodus 27:9 and its east side 27:13 carry it with the prefix; the bare token's five Torah seats include Leviticus's field-corner and beard-corner, homographs by sense; 'eastward toward the sunrise' (34:15) the court's east side"),
    ('Num 34:11 / 5:23 by CALL — the blotting verb', lambda: the_four_sides({'ask': 'the_blotting_verb'}, DATA), "and it shall reach (34:11) — the blotting verb's token (5:23; Deuteronomy 29:19; Isaiah 25:8): the border reaches, the priest blots — a homograph by sense, the sotah's cell by CALL"),
    ('Num 34:11 / Josh 13:27, 19:35; Bava Batra 122a:6 — Chinnereth', lambda: the_four_sides({'ask': 'chinnereth'}, DATA), "the sea of Chinnereth (34:11) — two seats of the phrase, seven of the name; Onkelos 'Gennesar' — the shelf's lottery names Naphtali's boundary by that word (Bava Batra 122a:6)"),
    ('Num 34:3, 8 / 13:21 by CALL — the spies walked it', lambda: the_four_sides({'ask': 'the_spies_walked_it'}, DATA), "the spies walked the border's length — 'from the wilderness of Zin' and 'Lebo-hamath' each at two seats: 13:21 and 34:3, 34:8"),
    ('Ezek 47:13-20 — the order', lambda: the_four_sides({'ask': 'ezekiels_order'}, DATA), "Ezekiel's order — north, east, south, west against the chapter's south, west, north, east; twenty-nine tokens shared; observed, no link"),
    ('Gen 15:18; Exod 23:31; Deut 1:7, 11:24; Josh 1:4 — the promised extents', lambda: the_four_sides({'ask': 'the_promised_extents'}, DATA), "the four promised extents (Genesis 15:18, Exodus 23:31, Deuteronomy 1:7, 11:24; Joshua 1:4) — no river, Euphrates, Lebanon or western sea in the chapter: another description, observed"),
    ('Gittin 8a:4-7 — the sea as a border', lambda: the_four_sides({'ask': 'the_sea_as_border'}, DATA), "the sea as a border, two ways (Gittin 8a:4-7 on 34:6) — the Rabbis' string over the islands between the ink's two corners, or Rabbi Yehuda's sea itself: a data row"),
    ('Bekhorot 55a:10, 14 — the Jordan as a border', lambda: the_four_sides({'ask': 'the_jordan_as_border'}, DATA), "the Jordan as a border, two ways (Bekhorot 55a:10 on 34:12; 55a:14 on 34:15) — one border round about, or the river Canaan's from 'at Jericho': a data row"),
    ('Mishnah Sheviit 6:1; Gittin 1:2 — the three lands', lambda: the_four_sides({'ask': 'the_three_lands'}, DATA), "the shelf's own border points — the three lands of Sheviit 6:1 inside 34's one border; the bills' Rekem the translation's Kadesh-barnea of 34:4 (Mishnah Gittin 1:2): a data row"),
    # F3 — Moses' restatement
    ('Num 34:13 / 36:5 — the relay', lambda: moses_restatement({'ask': 'the_relay'}, DATA), "and Moses commanded the children of Israel (34:13) — the relay of 34:1-12 in the form 36:5's installing act took: the D2 question of the second pass, the class named"),
    ('Num 34:13, 15 / Josh 13:7, 14:2 — the nine and a half', lambda: moses_restatement({'ask': 'the_nine_and_a_half'}, DATA), "the nine tribes and the half tribe, the two tribes and the half tribe (34:13, 34:15) — [9] and [2] with the two halves = twelve; 'nine' in the construct three Bible seats, all the nine tribes"),
    ('Num 34:13-28 / 32:33 — one tribe-noun', lambda: moses_restatement({'ask': 'one_tribe_noun'}, DATA), "one tribe-noun — the staff-word eighteen times in the chapter and the other never; 32:33's the neighbour; Joshua 13:7 says the nine with the other word"),
    ('Num 34:14-15 / 32:33 by CALL — the grant read', lambda: moses_restatement({'ask': 'the_grant_read'}, DATA), "the two and a half have taken their inheritance (34:14-15) — a run citation of 32:33's three transfers on the tape; the line writes nothing"),
    ('Num 26 by CALL — the count', lambda: moses_restatement({'ask': 'the_count'}, DATA), "the two and a half's count — 110,580 by CALL (43,730 + 40,500 + 52,700 ÷ 2 from the second census)"),
    ('Num 34:14 / Gen 38:23 — the pair', lambda: moses_restatement({'ask': 'the_pair'}, DATA), "the Reubenite and the Gadite (34:14) — the pair's first seat; the Gadite's token is also 'the kid' at Genesis 38:23 and Judges 14:6"),
    ('Num 34:13 / Josh 14:2, 21:8 — Joshua\'s receipt', lambda: moses_restatement({'ask': 'joshuas_receipt'}, DATA), "Joshua 14:2's receipt — 'as the LORD commanded by the hand of Moses, to the nine tribes and the half tribe' quotes 34:13 outside the Torah; no receipt in the chapter"),
    ('Num 34:13 / 26:52-56, 33:54 by CALL — the lot', lambda: moses_restatement({'ask': 'the_lot_by_call'}, DATA), "you shall inherit by lot (34:13) — 26:52-56's lot by CALL, the open debit cited a third time (32:18, 33:54, here), not rewritten"),
    # F4 — the dividers
    ('Num 34:17, 19 / 13:16 — the names form', lambda: the_dividers({'ask': 'the_names_form'}, DATA), "these are the names of the men (34:17, 34:19) — the rosters' heading, 13:16's and this"),
    ('Num 34:17 / 32:28 by CALL; Josh 14:1, 19:51 — the triad', lambda: the_dividers({'ask': 'the_triad'}, DATA), "Eleazar the priest and Joshua son of Nun (34:17) — the triad's three Bible seats: this and Joshua 14:1, 19:51; 32:28's charge by CALL; the lottery's picture on the shelf"),
    ('Num 34:13, 17-18, 29 / Josh 13:32 — the three stems', lambda: the_dividers({'ask': 'the_three_stems'}, DATA), "the one root in three stems — the reflexive (34:13), the plain (34:17-18), the intensive (34:29) whose other three seats are Joshua's runs; the object switching from the land to the people"),
    ('Num 34:18 / 13:2, 7:11, 17:21 by CALL — the distributive', lambda: the_dividers({'ask': 'the_distributive'}, DATA), "one prince, one prince from a tribe (34:18) — the distributive doubling read [1, 1]: the spies, the dedication and the rods by CALL; Joshua's stones and embassy the runs"),
    ('Josh 17:4, 14:13 by CALL — the court that owes', lambda: the_dividers({'ask': 'the_court_that_owes'}, DATA), "the court that owes — the daughters' holding (paid at Joshua 17:4 before Eleazar and Joshua) and Caleb's Hebron (Joshua 14:13): the dividers the payers, by CALL"),
    ('Bava Batra 122a:12 by CALL — only excludes', lambda: the_dividers({'ask': 'only_excludes'}, DATA), "'only' excludes Joshua and Caleb (Bava Batra 122a:12) — the two dividers' own portions not by the lot they administer: by CALL"),
    ('Kiddushin 42a:6-8 — the princes as agents', lambda: the_dividers({'ask': 'the_princes_as_agents'}, DATA), "the princes as agents or stewards (Kiddushin 42a:6-8 on 34:18) — agency asked and refused, the court's steward for orphans the verse's teaching: a data row"),
    ('Sanhedrin 16a:2-3 — the seventy-one', lambda: the_dividers({'ask': 'the_seventy_one'}, DATA), "the seventy-one at the first division (Sanhedrin 16a:2-3) — Ulla's likeness refused: the lots, the Urim and all Israel; the ink's dividers twelve by name: a data row"),
    ('Num 34:29 / Josh 14:1, 19:51 — the debit', lambda: the_dividers({'ask': 'the_debit'}, DATA), "the dividers commanded (34:29) — a debit to divide the inheritance to the children of Israel in Canaan, OPEN BY DESIGN to Joshua 14:1 and 19:51"),
    # F5 — the roster
    ('Num 34:19-28 — the roster', lambda: the_roster({'ask': 'the_roster'}, DATA), "the roster (34:19-28) — ten princes by tribe with their fathers; the title at seven rows, dropped at Judah's, Simeon's and Benjamin's; the twelve enter the population table"),
    ('Num 34:19 / 13:6 by CALL — Caleb\'s five words', lambda: the_roster({'ask': 'calebs_five_words'}, DATA), "Caleb's five words (34:19 = 13:6) — the spy's line repeated at the dividers'; Caleb son of Jephunneh eight Torah seats"),
    ('Num 14:24, 30 by CALL — the survivors', lambda: the_roster({'ask': 'the_survivors'}, DATA), "the two survivors — Joshua and Caleb the only persons of the spies' roster among the dividers; the exceptions of 14:24, 14:30 by CALL"),
    ('Num 1:5-15 by CALL — no prince of chapter 1', lambda: the_roster({'ask': 'no_prince_of_chapter_one'}, DATA), "no prince of chapter 1 among the ten (by CALL); Ammihud the one father's name shared — three tribes' fathers' name (1:10; 34:20; 34:28)"),
    ('Num 34:19-28 — the names nowhere else', lambda: the_roster({'ask': 'only_here'}, DATA), "the names nowhere else — eight by token (Hanniel among them), ten by lemma (Ephod, Chislon, Shelomi homographs by token; Hanniel's lemma shared); Shemuel the prophet's name's first seat; seven of the ten carry God's name, none of the fathers"),
    ('Num 34:19-28 against sixteen lists — the order', lambda: the_roster({'ask': 'the_order'}, DATA), "the order matches no other roster (sixteen lists) — Manasseh before Ephraim as the second census and Genesis 46 in the Torah, Zebulun before Issachar as the two blessings, the four northern in Joshua's lot order"),
    ('Num 34:29 — the closer', lambda: the_roster({'ask': 'the_closer'}, DATA), "the closer (34:29) — 'these are they whom the LORD commanded to divide', one seat; no receipt in the chapter — Joshua 14:2's is outside the Torah"),
    ('Num 34:17-28 — the twelve rows', lambda: the_roster({'ask': 'the_rows'}, DATA), "the twelve named rows — the roll's persons enter the population table (grain named, as of Num 34:17-29): the register gate's seat paid"),
]


if __name__ == '__main__':
    ok = 0
    frac = {'INK': 0, 'MOVE': 0, 'DATA': 0, 'HYP': 0}
    used_effects = []
    print()
    for label, fn, want in CASES:
        got, effects, prov = fn()
        hit = got == want
        ok += hit
        kinds = [k for k, _ in prov]
        cls = 'HYP' if 'HYP' in kinds else ('INK' if all(k == 'INK' for k in kinds) else ('MOVE' if 'MOVE' in kinds else 'DATA'))
        frac[cls] += 1
        print('%s  [%s]  %s' % ('PASS' if hit else 'MISS', cls, label))
        if not hit:
            print('      expected: %s' % (want,))
            print('      got     : %s' % (got,))
        used_effects += effects
        for line in FX.render(effects):
            print('        ->%s' % line)
    print()
    print('WATCH COVERAGE (the wrap):')
    _W.print_coverage()
    print('MATRIX: %d/%d cells match the answer sheet' % (ok, len(CASES)))
    tot = len(CASES)
    print('FRACTIONS: pure ink %d/%d (%.0f%%) · named moves %d/%d (%.0f%%) · data %d/%d (%.0f%%) · hypotheses %d/%d (the H class, counted apart — never as compiled)' %
          (frac['INK'], tot, 100.0 * frac['INK'] / tot, frac['MOVE'], tot, 100.0 * frac['MOVE'] / tot, frac['DATA'], tot, 100.0 * frac['DATA'] / tot, frac['HYP'], tot))
    ops = FX.summarize(used_effects)
    print('LEDGER OPS this span writes:', ', '.join('%s x%d' % kv for kv in sorted(ops.items())))
    print('THE INK: integers %s; the caret %s; starred none; the frame verbs %s (two divine frames, Moses\' command between)' % (sorted(INTS.items()), CARET, FRAME_VERBS))
    print('THE SIDES: %d proper-name tokens (%s); the border-word %d in the chapter, %d in Numbers; %d "and it shall" verbs; "to you" %d; Judah\'s border shares %d of %d; Ezekiel shares %d tokens' % (len(NUM_POINTS), [len(SIDES[s]['points']) for s in SIDES], len(BORDER_TOKENS), BORDER_NUM, len(SHALL_BE), len(TO_YOU), len(SHARED_S), len(NUM_S), len(EZEK_SHARED)))
    print('THE ROSTER: %s; only here by token %d, by lemma %d; the order matches %s; Joshua\'s tribe %s' % ([(r['tribe'], r['prince'], r['father'], r['title']) for r in ROSTER], len(ONLY_HERE_TOKEN), len(ONLY_HERE_LEMMA), MATCHES or 'none', JOSHUA_TRIBE))
    print('THE SCENE on the bench: %s; the timers (set, fired, cancelled, pending) %s; entities %d' % SCENE)
    print('THE NARRATIVE: %s' % (NARRATIVE,))
    print('THE PARAMETER ROWS: ' + '; '.join('%s = %s' % (k, (DATA[k]['value'] if k not in ('the_four_sides', 'the_roster') else '%d rows (a data list)' % len(DATA[k]['value']))) for k in DATA) + ' (the other settings recorded in DATA)')
    if ok == len(CASES):
        print('\nTHE COMPILE OF THE BORDERS: the answer sheet REPRODUCED — %d/%d' % (ok, len(CASES)))
    sys.exit(0 if ok == len(CASES) else 1)

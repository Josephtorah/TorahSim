import os as _os
_ROOT = _os.path.normpath(_os.path.join(_os.path.dirname(_os.path.abspath(__file__)), '..', '..', '..'))   # THE PORTABLE REPO (2026-09-15): the repo root from this file's own place
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
assert INTS == {13: [9], 15: [2], 18: [1, 1]} and ORDS == {} and STARRED == [] and CARET == [(15, 'שני^')], (INTS, ORDS, STARRED, CARET)   # THREE number verses in twenty-nine — every one read; the construct "two of" by its points; THE DISTRIBUTIVE DOUBLING as two ones; no rule owed
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

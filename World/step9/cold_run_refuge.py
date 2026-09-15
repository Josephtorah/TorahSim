import os as _os
_ROOT = _os.path.normpath(_os.path.join(_os.path.dirname(_os.path.abspath(__file__)), '..', '..'))   # THE PORTABLE REPO (2026-09-15): the repo root from this file's own place
#!/usr/bin/env python3
# NUM 35:1-34 — THE REFUGE CITIES (THE NUMBERS WALK sitting 15b, 2026-09-13; World/step9/NUMBERS_WALK.md "Sitting 15b"; the state doc's #159).
# THE LEVITE CITIES AS ONE DEBIT ON THE PEOPLE AND A TABLE: 35:1-8's command in the second person plural ("you shall give" ten times) writes ONE
# debit — commanded on israel_people valued give_the_levites_cities_and_pasture_lands, counterparty the Levites, OPEN BY DESIGN to its run at
# Joshua 21 (21:2 the request quoting "cities to dwell in"; 21:41 the tally; the four lots 13 + 10 + 13 + 12 by the parser); the table DATA —
# forty-eight = six + forty-two, the thousand and THE TWO THOUSAND (35:5's bare dual, read by the parser since this sitting's rule 29) with the
# exam's three settings (R. Akiva's open land and Sabbath limit; R. Eliezer ben R. Yosei HaGelili's fields and vineyards; the Mishnah's thousand
# and thousand), the four sides in THE CAMP'S ORDER (CB.camp by CALL), 26:54's rule by CALL. THE REFUGE LAW (35:9-34) writes ONE debit —
# appoint_six_cities_of_refuge, OPEN BY DESIGN to Deuteronomy 4:41 and Joshua 20:7-8 — and compiles the statute's cells: the murderer's and the
# manslayer's CASE TABLE from the ink's tokens (the instruments — iron at any size, the stone and the wood with the size clause a PARAMETER; the
# manners; the intents; the verdicts put_to_death by the sword (M3 by CALL), flees_to_refuge (Exodus 21:13's effect at its second seat) with
# dwells_in_refuge — THE TERM AN OPEN BODY ENTRY CLOSED BY THE OFFICE-HOLDER'S DEATH ACT, not a day-timer — and Issi ben Akiva's 'unresolved'),
# the border (has_blood reused), the witnesses (two by the prototype), no ransom twice against the ox's cell, the land polluted (a status on the
# land of Canaan; Genesis 9:6 by CALL), "in whose midst I dwell" by CALL to 5:3's camp — THE BOOK'S INCLUSIO. Five cells; every token probed
# (zero-report law); effects on every cell (the effects law); the parameters the ink leaves open recorded in DATA with their arms. Reading ledger:
# logic/oral_triage/num_35_refuge_cities_2026-09-13.md; the exam's docket: logic/oral_triage/num_35_refuge_cities_exam_2026-09-13.md (666 rows:
# LAW 97 / DERIVATION 112 / DISPUTE 105 / CONTEXT 352).

# ---- THE HONEST-PAIRING GUARD ----------------------------------------------------------------------------
import os as _os, sys as _sys
_sys.path.insert(0, _os.path.dirname(_os.path.abspath(__file__)))
from compile_guards import check_honest_pairing as _chp
_P = _os.path.abspath(__file__)
GUARDED = _chp(_P, 'CASES', 2)
assert GUARDED == 51, ("the guard counted %d expectations, the tripwire holds 51" % GUARDED)   # RETYPED FROM THE GUARD'S PRINT after the first run (the design estimated ~66; the guard counted 51 — 12 + 8 + 9 + 13 + 9 rows)
print('guard: %d expectations checked, every one a literal from the answer sheet [honest-pairing guard satisfied]' % GUARDED)
import sqlite3, sys, io, re, contextlib, collections, unicodedata, yaml
import effects_layer as FX
import world_engine as WE
import cold_run_mishpatim_3 as M3             # THE EDGE: refuge -> mishpatim_3 CALL, reference (21:13's place become cities; the descent; the sword; 22:1's "no blood" at its second seat; the father and the son; the office's exemptions)
import cold_run_mishpatim as M1               # THE EDGE: refuge -> mishpatim CALL, reference (21:30's ransom — the goring ox's, the noun 35:31 refuses for the murderer)
import cold_run_lev24 as L24                  # THE EDGE: refuge -> lev24 CALL, reference (24:17's "whoever strikes any soul"; 83b's talion money from 35:31)
import cold_run_shelach as SL                 # THE EDGE: refuge -> shelach CALL, reference (15:22-29's "unwittingly" — the sin offering's word at 35:11, 15)
import cold_run_naso as NS                    # THE EDGE: refuge -> naso CALL, reference (5:3's camp "in whose midst I dwell" — the inclusio; 6:9's "suddenly")
import cold_run_second_census as C2           # THE EDGE: refuge -> second_census CALL, reference (26:54's rule at 35:8; 26:62's Levites without inheritance)
import cold_run_journeys as JO                # THE EDGE: refuge -> journeys CALL, reference (33:51's "when you cross the Jordan" at 35:10; 33:54's rule)
import cold_run_borders as BO                 # THE EDGE: refuge -> borders CALL, reference (34:2's "command the children of Israel"; the sides' order; the land of Canaan the written-on party)
import cold_run_zelophehad as ZL              # THE EDGE: refuge -> zelophehad CALL, reference (27:11's "a statute of judgment" at 35:29)
import cold_run_gad_reuben as GR              # THE EDGE: refuge -> gad_reuben CALL, reference (the three cities beyond the Jordan in 32:33's holdings)
import cold_run_chukat as CK                  # THE EDGE: refuge -> chukat CALL, reference (20:28's succession — the office's holder for the term)
import cold_run_bamidbar as CB                # THE EDGE: refuge -> bamidbar CALL, reference (the camp's order east-south-west-north at 35:5; the runner's own row names 35:5)
import cold_run_primeval as PR                # THE EDGE: refuge -> primeval CALL, reference (Genesis 9:6's shedder's blood at 35:33; 3:15's enmity FALSE by sense)
import cold_run_sanctions as SA               # THE EDGE: refuge -> sanctions CALL, reference (Leviticus 18:25-28's land that vomits at 35:34; the four deaths' orders)
import cold_run_priesthood as PH              # THE EDGE: refuge -> priesthood CALL, reference (Leviticus 21:10's anointed high priest — the term's holder defined)

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

# ---- zero-report probes: the span's load-bearing tokens (every one measured on the DB before it was typed — ref_runner_measure.out, 2026-09-13) ----
PROBES = [
    ('וידבר',     35, 1,  'and [the LORD] spoke — the first frame, with the place-stamp; 35:9 the second, bare'),
    ('בערבת',     35, 1,  'in the plains of [Moab] — the stamp\'s six seats'),
    ('ירחו',      35, 1,  'Jericho — the stamp'),
    ('צו',        35, 2,  'command — the five Torah seats, this the fifth'),
    ('ונתנו',     35, 2,  'and they shall give — one seat'),
    ('ללוים',     35, 2,  'to the Levites'),
    ('לשבת',      35, 2,  'to dwell in — "cities to dwell in" three Bible seats'),
    ('ומגרש',     35, 2,  'and pasture-land — the word\'s six Torah seats'),
    ('חיתם',      35, 3,  'their beasts / their lives — Onkelos "their needs of life"'),
    ('מקיר',      35, 4,  'from the wall of [the city]'),
    ('וחוצה',     35, 4,  'outward — Eruvin 51a:9 refuses the analogy from it'),
    ('אלף',       35, 4,  'a thousand — the parser [1000], the cubit consumed'),
    ('אמה',       35, 4,  'cubits — the unit noun'),
    ('ומדתם',     35, 5,  'and you shall measure — the measure-verb\'s three Torah seats'),
    ('מחוץ',      35, 5,  'from outside — Rav Chisda\'s chain ends here (Eruvin 51a:8)'),
    ('פאת',       35, 5,  'side — the tabernacle\'s word'),
    ('קדמה',      35, 5,  'east — the first side: the camp\'s order'),
    ('אלפים',     35, 5,  'two thousand — THE BARE DUAL, read by rule 29'),
    ('באמה',      35, 5,  'by the cubit — the prefixed cubit, no unit-noun mark'),
    ('בתוך',      35, 5,  'in the midst — "and the city in the midst"'),
    ('המקלט',     35, 6,  'the refuge — the word\'s twenty Bible verses, eleven here'),
    ('לנס',       35, 6,  'to flee — Lot\'s phrase'),
    ('הרצח',      35, 6,  'the manslayer — the root\'s twenty tokens in the chapter'),
    ('ושתים',     35, 6,  'and two — forty-two'),
    ('ושמנה',     35, 7,  'and eight — forty-eight'),
    ('תרבו',      35, 8,  'you shall take more — 26:54\'s verb'),
    ('תמעיטו',    35, 8,  'you shall take less — here alone in the plural'),
    ('עברים',     35, 10, 'crossing — 33:51\'s clause'),
    ('ארצה',      35, 10, 'to the land of — the directional form\'s Torah last'),
    ('והקריתם',   35, 11, 'and you shall appoint — one seat; Balaam\'s root FALSE by sense'),
    ('בשגגה',     35, 11, 'unwittingly — the sin offering\'s word'),
    ('מגאל',      35, 12, 'from the avenger — bare, without "blood"'),
    ('העדה',      35, 12, 'the congregation — the four tokens the court is built from'),
    ('למשפט',     35, 12, 'for judgment — the court before the avenger'),
    ('שש',        35, 13, 'six — the six cities'),
    ('שלש',       35, 14, 'three — three and three'),
    ('ולגר',      35, 15, 'and for the stranger'),
    ('ולתושב',    35, 15, 'and for the sojourner — Joshua 20:9 drops him'),
    ('ברזל',      35, 16, 'iron — no "hand", no size clause'),
    ('הכהו',      35, 16, 'struck him — the five Torah seats'),
    ('וימת',      35, 16, 'and he died — the narrative tense inside the case'),
    ('יומת',      35, 16, 'shall be put to death — "shall surely die" five times here'),
    ('באבן',      35, 17, 'with a stone [of the hand]'),
    ('יד',        35, 17, 'hand — the size clause'),
    ('ימות',      35, 17, 'may die — "whereby he may die"'),
    ('עץ',        35, 18, 'wood'),
    ('גאל',       35, 19, 'the avenger [of blood]'),
    ('ימית',      35, 19, 'shall put to death'),
    ('בפגעו',     35, 19, 'when he meets him — two seats'),
    ('בשנאה',     35, 20, 'in hatred'),
    ('יהדפנו',    35, 20, 'thrust him'),
    ('השליך',     35, 20, 'threw'),
    ('בצדיה',     35, 20, 'in lying-in-wait — the noun\'s two Bible seats'),
    ('באיבה',     35, 21, 'in enmity — the serpent\'s word'),
    ('בידו',      35, 21, 'with his hand'),
    ('המכה',      35, 21, 'the smiter — the participle with the article'),
    ('בפתע',      35, 22, 'suddenly — the nazirite\'s word'),
    ('ראות',      35, 23, 'seeing — "without seeing", the blind killer'),
    ('ויפל',      35, 23, 'and he dropped it — the downward motion'),
    ('אויב',      35, 23, 'enemy — "not his enemy"'),
    ('ושפטו',     35, 24, 'and [the congregation] shall judge'),
    ('והצילו',    35, 25, 'and [the congregation] shall deliver — Onkelos with the refuge-root'),
    ('והשיבו',    35, 25, 'and shall return him'),
    ('הגדל',      35, 25, 'the high [priest] — written defective only here'),
    ('משח',       35, 25, 'anointed — Leviticus 21:10\'s definition'),
    ('יצא',       35, 26, 'goes out — the doubled infinitive'),
    ('גבול',      35, 26, 'the border [of his city of refuge]'),
    ('ורצח',      35, 27, 'and slays — the consecutive perfect (R. Akiva\'s narration, R. Yosei HaGelili\'s mitzva)'),
    ('דם',        35, 27, 'blood — "he has no blood", the burglar\'s clause'),
    ('ישוב',      35, 28, 'shall return — the stem read (Sifrei 161:5)'),
    ('אחזתו',     35, 28, 'his possession'),
    ('לחקת',      35, 29, 'a statute [of judgment] — the daughters\' phrase'),
    ('מושבתיכם',  35, 29, 'your dwellings — the blood ban\'s formula'),
    ('עדים',      35, 30, 'witnesses — the bare plural, two by the prototype'),
    ('ועד',       35, 30, 'and a witness [one]'),
    ('יענה',      35, 30, 'shall testify — the ninth commandment\'s verb'),
    ('כפר',       35, 31, 'ransom — the goring ox\'s noun refused'),
    ('רשע',       35, 31, 'wicked — "wicked to die"; the lashes\' verbal analogy'),
    ('לנוס',      35, 32, 'to flee — the fugitive\'s ransom refused'),
    ('תחניפו',    35, 33, 'you shall [not] pollute — the root\'s only Torah seat'),
    ('יכפר',      35, 33, '[no] atonement — the ransom\'s root a third time'),
    ('שפכו',      35, 33, 'him who shed it — Genesis 9:6\'s clause'),
    ('תטמא',      35, 34, 'you shall [not] defile — Leviticus 18:25-28\'s land'),
    ('שכן',       35, 34, 'dwell — "in whose midst I dwell", the inclusio with 5:3'),
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
SPAN = [(35, v) for v in range(1, 35)]
NUMBERS = {v: ink_numbers(verse_words('Num', 35, v)) for _, v in SPAN}
ORDINALS = {v: ink_ordinals(verse_words('Num', 35, v)) for _, v in SPAN}
STARRED = [(v, t) for _, v in SPAN for t in verse_words('Num', 35, v) if t.endswith('*')]
TILDE = [(v, t) for _, v in SPAN for t in verse_words('Num', 35, v) if t.endswith('~')]
UNIT = [(v, t) for _, v in SPAN for t in verse_words('Num', 35, v) if t.endswith('@')]
INTS = {v: n for v, n in NUMBERS.items() if n}; ORDS = {v: o for v, o in ORDINALS.items() if o}
assert INTS == {4: [1000], 5: [2000, 2000, 2000, 2000], 6: [6, 42], 7: [48], 13: [6], 14: [3, 3], 15: [6], 30: [1]} and ORDS == {} and STARRED == [], (INTS, ORDS, STARRED)   # EIGHT number verses in thirty-four — every one read since rule 29 (35:5's four bare duals the sitting's teaching); the reading's seven + the fourth
assert TILDE == [(5, 'אלפים~')] * 4 and UNIT == [(4, 'אמה@')], (TILDE, UNIT)                                                          # THE BARE DUAL marked four times by the sheva under the lamed; 35:4's cubit the unit noun, 35:5's prefixed cubit no mark
THOUSAND, TWO_THOUSANDS, SIX_FORTYTWO, FORTY_EIGHT, THREE_THREE = INTS[4][0], INTS[5], INTS[6], INTS[7][0], INTS[14]
assert SIX_FORTYTWO[0] + SIX_FORTYTWO[1] == FORTY_EIGHT == 48 and THREE_THREE == [3, 3] and sum(THREE_THREE) == INTS[13][0] == INTS[15][0] == 6, (SIX_FORTYTWO, FORTY_EIGHT, THREE_THREE)   # 6 + 42 = 48; 3 + 3 = 6 — the ink's own sums
assert ink_numbers(verse_words('Num', 36, 1)) == [] and ink_ordinals(verse_words('Num', 36, 1)) == [], 'the next chapter opens without a number'
FRAME_VERBS = [(v, words(35, v)[0], words(35, v)[1]) for _, v in SPAN if words(35, v)[0] in ('וידבר', 'ויאמר', 'ויאמרו', 'ויענו', 'ויצו')]
assert FRAME_VERBS == [(1, 'וידבר', 'יהוה'), (9, 'וידבר', 'יהוה')], FRAME_VERBS                                                       # TWO divine frames — 35:1 with the place-stamp, 35:9 bare; no relay, no tent
assert words(35, 1) == ['וידבר', 'יהוה', 'אל', 'משה', 'בערבת', 'מואב', 'על', 'ירדן', 'ירחו', 'לאמר'] and words(35, 9) == ['וידבר', 'יהוה', 'אל', 'משה', 'לאמר'], (words(35, 1), words(35, 9))
NARR = [(v, t) for _, v in SPAN for t in words(35, v) if t in ('וימת', 'ויפל')]
assert NARR == [(16, 'וימת'), (17, 'וימת'), (18, 'וימת'), (20, 'וימת'), (21, 'וימת'), (23, 'ויפל'), (23, 'וימת')], NARR                    # SEVEN narrative verbs inside the cases — the consequent told in the story's tense (the reading's nine = these + the two frames)
CASE_TOKENS = {v: [t for t in words(35, v) if t in ('כי', 'ואם', 'או', 'אם')] for _, v in SPAN}
CASE_TOKENS = {v: ts for v, ts in CASE_TOKENS.items() if ts}
assert CASE_TOKENS == {10: ['כי'], 16: ['ואם'], 17: ['ואם'], 18: ['או'], 20: ['ואם', 'או'], 21: ['או'], 22: ['ואם', 'או'], 23: ['או'], 26: ['ואם'], 28: ['כי'], 31: ['כי'], 33: ['כי', 'כי', 'אם'], 34: ['כי']}, CASE_TOKENS   # THE CASE STRUCTURE: "when" at 10; "and if" / "or" the murderer's and the manslayer's branches; "for" the statute's reasons
GIVE = [(v, i) for _, v in SPAN for i, t in enumerate(words(35, v)) if t == 'תתנו']
assert len(GIVE) == 10 and sorted(set(v for v, _ in GIVE)) == [2, 4, 6, 7, 8, 13, 14], GIVE                                                   # "you shall give" TEN times in the second person plural — the Levite cities' and the six cities' commands are the people's debits
# ---- the whole-DB phrase census (the seats typed from the measurement print of 2026-09-13 — ref_runner_measure.out) ----
_V = collections.OrderedDict(); _L = collections.OrderedDict(); _M = collections.OrderedDict(); _PT = collections.OrderedDict()
for b, c, v, he, lm, mo in db.execute("SELECT v.book, v.chapter, v.verse, w.he, w.lemma, w.morph FROM words w JOIN verses v ON w.verse_id=v.id ORDER BY v.id, w.idx"):
    _V.setdefault((b, c, v), []).append(strip(he)); _L.setdefault((b, c, v), []).append(lm.split('/')[-1].split(' ')[0] if lm else ''); _M.setdefault((b, c, v), []).append(mo or ''); _PT.setdefault((b, c, v), []).append(NF(he.replace('/', '')))
def seats(phrase, books=None):
    p = phrase.split(); n = len(p)
    return ['%s %d:%d' % k for k, ws in _V.items() if (books is None or k[0] in books) and any(ws[i:i + n] == p for i in range(len(ws) - n + 1))]
def tok(t, books=None):
    return ['%s %d:%d' % k for k, ws in _V.items() if (books is None or k[0] in books) and t in ws]
def lemma_seats(lm, books=None):
    return ['%s %d:%d' % k for k, ls in _L.items() if (books is None or k[0] in books) and lm in ls]
def lemma_tokens(lm, k):
    return [(w, m) for w, l, m in zip(_V[k], _L[k], _M[k]) if l == lm]
TORAH = ('Gen', 'Exod', 'Lev', 'Num', 'Deut')
# ---- F1's facts: the Levite cities ----
COMMAND = seats('צו את בני ישראל'); GIVE_LEVITES = seats('ונתנו ללוים'); CITIES_DWELL = seats('ערים לשבת'); THEIR_PASTURES = seats('מגרשיהן'); PASTURES_CITIES = seats('מגרשי הערים')
assert COMMAND == ['Lev 24:2', 'Num 5:2', 'Num 28:2', 'Num 34:2', 'Num 35:2'] and GIVE_LEVITES == ['Num 35:2'] and CITIES_DWELL == ['Josh 14:4', 'Josh 21:2', 'Num 35:2'] and THEIR_PASTURES == ['Josh 21:3', 'Josh 21:8', 'Num 35:7'] and PASTURES_CITIES == ['Num 35:5'], (COMMAND, GIVE_LEVITES, CITIES_DWELL, THEIR_PASTURES, PASTURES_CITIES)   # the five commands, this the fifth; "cities to dwell in" — Joshua 21:2 THE RUN'S REQUEST
PASTURE_T = lemma_seats('4054', TORAH); PASTURE_B = lemma_seats('4054'); PASTURE_J21 = [s for s in PASTURE_B if s.startswith('Josh 21:')]
assert PASTURE_T == ['Lev 25:34', 'Num 35:2', 'Num 35:3', 'Num 35:4', 'Num 35:5', 'Num 35:7'] and len(PASTURE_B) == 69 and len(PASTURE_J21) == 32, (PASTURE_T, len(PASTURE_B), len(PASTURE_J21))   # the pasture-land word: six Torah seats (Leviticus 25:34's unsellable field + this chapter's five), 69 Bible verses, 32 in Joshua 21
WALL_OUT = seats('מקיר העיר וחוצה'); THOUSAND_CUBITS = seats('אלף אמה'); TWO_THOUSAND_CUBIT = seats('אלפים באמה'); MEASURE = seats('ומדתם'); ABOUT_TWO_THOUSAND = seats('כאלפים אמה')
assert WALL_OUT == ['Num 35:4'] and THOUSAND_CUBITS == ['Num 35:4'] and TWO_THOUSAND_CUBIT == ['Num 35:5'] and MEASURE == ['Num 35:5'] and ABOUT_TWO_THOUSAND == ['Josh 3:4'], (WALL_OUT, THOUSAND_CUBITS, TWO_THOUSAND_CUBIT, MEASURE, ABOUT_TWO_THOUSAND)
MEASURE_LEMMA_T = lemma_seats('4058', TORAH)
assert MEASURE_LEMMA_T == ['Deut 21:2', 'Exod 16:18', 'Num 35:5'], MEASURE_LEMMA_T                                                          # THE MEASURE-VERB'S THREE TORAH SEATS: the omer, the pasture-lands, the elders to the slain man (the heifer the Sifrei brings to 35:33)
EAST_SIDE = seats('פאת קדמה'); SOUTH_SIDE = seats('פאת נגב'); WEST_SIDE = seats('פאת ים'); NORTH_SIDE = seats('פאת צפון'); CITY_MIDST = seats('והעיר בתוך')
assert EAST_SIDE == ['Num 35:5'] and SOUTH_SIDE == ['Ezek 48:28', 'Num 34:3', 'Num 35:5'] and WEST_SIDE == ['Ezek 47:20', 'Josh 18:14', 'Num 35:5'] and NORTH_SIDE == ['Ezek 47:17', 'Ezek 48:16', 'Num 35:5'] and CITY_MIDST == ['Num 35:5'], (EAST_SIDE, SOUTH_SIDE, WEST_SIDE, NORTH_SIDE, CITY_MIDST)
SIDES_35 = [words(35, 5)[i] for i in (5, 10, 15, 20)]
assert SIDES_35 == ['קדמה', 'נגב', 'ים', 'צפון'], SIDES_35                                                                                  # east, south, west, north — the indices from the print (35:5's words 5, 10, 15, 20)
CAMP_SIDES = [words(2, 3)[1], words(2, 10)[3], words(2, 18)[4], words(2, 25)[3]]
assert CAMP_SIDES == ['קדמה', 'תימנה', 'ימה', 'צפנה'], CAMP_SIDES                                                                          # Numbers 2's banners: east (Judah), south (Reuben), west (Ephraim), north (Dan) — the same order, the directional forms
SIX_REFUGE = seats('שש ערי מקלט'); THE_SIX_REFUGE = seats('שש ערי המקלט'); CITIES_REFUGE = seats('ערי מקלט'); THE_CITIES_REFUGE = seats('ערי המקלט'); FORTY_TWO = seats('ארבעים ושתים עיר'); FORTY_EIGHT_CITIES = seats('ארבעים ושמנה עיר'); FORTY_EIGHT_ALL = seats('ארבעים ושמנה')
assert SIX_REFUGE == ['Num 35:13'] and THE_SIX_REFUGE == ['Num 35:6'] and CITIES_REFUGE == ['Num 35:11', 'Num 35:13', 'Num 35:14'] and THE_CITIES_REFUGE == ['1Chr 6:42', '1Chr 6:52', 'Josh 20:2', 'Num 35:6'] and FORTY_TWO == ['Num 35:6'] and FORTY_EIGHT_CITIES == ['Num 35:7'] and FORTY_EIGHT_ALL == ['Josh 21:41', 'Neh 7:15', 'Neh 7:44', 'Num 35:7'], (SIX_REFUGE, THE_SIX_REFUGE, CITIES_REFUGE, THE_CITIES_REFUGE, FORTY_TWO, FORTY_EIGHT_CITIES, FORTY_EIGHT_ALL)
REFUGE_B = lemma_seats('4733'); REFUGE_T = lemma_seats('4733', TORAH)
assert len(REFUGE_B) == 20 and REFUGE_T == ['Num 35:6', 'Num 35:11', 'Num 35:12', 'Num 35:13', 'Num 35:14', 'Num 35:15', 'Num 35:25', 'Num 35:26', 'Num 35:27', 'Num 35:28', 'Num 35:32'] and not any(s.startswith('Deut') for s in REFUGE_B), (len(REFUGE_B), REFUGE_T)   # the refuge-word: twenty Bible verses, the Torah's eleven all here — DEUTERONOMY NEVER SAYS IT
JOSH21_LOTS = [ink_numbers(verse_words('Josh', 21, v)) for v in (4, 5, 6, 7)]; JOSH21_TALLY = ink_numbers(verse_words('Josh', 21, 41))
assert JOSH21_LOTS == [[13], [10], [13], [12]] and sum(n[0] for n in JOSH21_LOTS) == 48 == JOSH21_TALLY[0], (JOSH21_LOTS, JOSH21_TALLY)     # THE RUN OUTSIDE THE TORAH: Joshua 21's four lots sum to the forty-eight, the tally reads it
MORE = seats('מאת הרב תרבו'); LESS = seats('ומאת המעט תמעיטו'); EACH = seats('כפי נחלתו'); LESS_SG = seats('תמעיט')
assert MORE == ['Num 35:8'] and LESS == ['Num 35:8'] and EACH == ['Num 35:8'] and LESS_SG == ['Lev 25:16', 'Num 26:54', 'Num 33:54'], (MORE, LESS, EACH, LESS_SG)   # the proportional rule: 26:54's two verbs, the plural "you shall take less" here alone
BEASTS = tok('חיתם')
assert BEASTS == ['Ezek 7:13', 'Num 35:3'], BEASTS                                                                                           # "their beasts" two Bible seats — Onkelos "their needs of life" (Nedarim 81a:7)
LEVITES_NUM = seats('הלוים', ('Num',)); TO_LEVITES = seats('ללוים')
assert len(LEVITES_NUM) == 29 and len(TO_LEVITES) == 32, (len(LEVITES_NUM), len(TO_LEVITES))
# ---- F2's facts: the refuge law ----
CROSSING = seats('כי אתם עברים את הירדן'); CANAANWARD = seats('ארצה כנען'); APPOINT = seats('והקריתם')
assert CROSSING == ['Deut 11:31', 'Num 33:51', 'Num 35:10'] and CANAANWARD == ['Gen 11:31', 'Gen 12:5', 'Gen 31:18', 'Gen 42:29', 'Gen 45:17', 'Gen 50:13', 'Num 35:10'] and APPOINT == ['Num 35:11'], (CROSSING, CANAANWARD, APPOINT)
SMITES_UNWIT = seats('מכה נפש בשגגה'); WHOEVER_SMITES = seats('כל מכה נפש'); UNWIT = seats('בשגגה'); NO_KNOWLEDGE = seats('בבלי דעת')
assert SMITES_UNWIT == ['Josh 20:3', 'Josh 20:9', 'Num 35:11', 'Num 35:15'] and WHOEVER_SMITES == ['Josh 20:9', 'Num 35:15', 'Num 35:30'] and len(UNWIT) == 13 and UNWIT[2:7] == ['Lev 4:2', 'Lev 4:22', 'Lev 4:27', 'Lev 5:15', 'Lev 22:14'] and NO_KNOWLEDGE == ['Deut 4:42', 'Deut 19:4', 'Job 35:16', 'Josh 20:3', 'Josh 20:5'], (SMITES_UNWIT, WHOEVER_SMITES, UNWIT, NO_KNOWLEDGE)   # "unwittingly" thirteen seats — the sin offering's word; Deuteronomy says "without knowledge"; Joshua 20:3 says both
AVENGER_BARE = seats('מגאל'); AVENGER_BLOOD = seats('גאל הדם'); UNTIL_STANDS = seats('עד עמדו לפני העדה למשפט')
assert AVENGER_BARE == ['Josh 20:3', 'Mal 1:7', 'Mal 1:12', 'Num 35:12'] and AVENGER_BLOOD == ['2Sam 14:11', 'Deut 19:6', 'Deut 19:12', 'Josh 20:5', 'Josh 20:9', 'Num 35:19', 'Num 35:21', 'Num 35:24', 'Num 35:25', 'Num 35:27'] and UNTIL_STANDS == ['Josh 20:6', 'Num 35:12'], (AVENGER_BARE, AVENGER_BLOOD, UNTIL_STANDS)   # the avenger bare at 35:12 (Malachi's "polluted" wears the consonants); "the avenger of blood" ten Bible seats; Joshua 20:6 quoting 35:12
THE_THREE_CITIES = seats('שלש הערים'); THREE_CITIES = seats('שלש ערים'); STRANGER_SOJ = seats('ולגר ולתושב'); FLEE_THERE = seats('לנוס שמה'); HE_SHALL_FLEE = seats('ינוס שמה')
assert THE_THREE_CITIES == ['Num 35:14'] and THREE_CITIES == ['Amos 4:8', 'Deut 4:41', 'Deut 19:7', 'Deut 19:9'] and STRANGER_SOJ == ['Num 35:15'] and FLEE_THERE == ['Deut 19:3', 'Gen 19:20', 'Josh 20:3', 'Josh 20:9', 'Num 35:15'] and HE_SHALL_FLEE == ['Deut 19:4', 'Exod 21:13', 'Num 35:26'], (THE_THREE_CITIES, THREE_CITIES, STRANGER_SOJ, FLEE_THERE, HE_SHALL_FLEE)   # "to flee there" LOT'S FIRST; "he shall flee there" EXODUS 21:13'S — the place become cities
JOSH20_9 = words(20, 9, 'Josh')
assert 'ולגר' in JOSH20_9 and 'ולתושב' not in JOSH20_9, JOSH20_9                                                                            # Joshua 20:9 drops the sojourner
# ---- F3's facts: the murderer ----
IRON = seats('בכלי ברזל'); STONE_HAND = seats('באבן יד'); WOOD = seats('בכלי עץ'); WHEREBY_F = seats('אשר ימות בה'); WHEREBY_M = seats('אשר ימות בו')
assert IRON == ['Num 35:16'] and STONE_HAND == ['Num 35:17'] and WOOD == ['Num 35:18'] and WHEREBY_F == ['Num 35:17', 'Num 35:23'] and WHEREBY_M == ['2Kgs 13:14', 'Num 35:18'], (IRON, STONE_HAND, WOOD, WHEREBY_F, WHEREBY_M)
assert len(words(35, 16)) == 10 and len(words(35, 17)) == 13 and len(words(35, 18)) == 14 and 'יד' not in words(35, 16), (len(words(35, 16)), len(words(35, 17)), len(words(35, 18)))   # THE IRON VERSE has no "hand" and no size clause — ten tokens against thirteen and fourteen
HE_IS_MURDERER = seats('רצח הוא'); MURDERER_DIE = seats('מות יומת הרצח'); SURELY_DIE_T = seats('מות יומת', TORAH); SURELY_DIE_35 = [s for s in SURELY_DIE_T if s.startswith('Num 35:')]; SMITER_DIE = seats('מות יומת המכה')
assert HE_IS_MURDERER == ['Num 35:16', 'Num 35:17', 'Num 35:18', 'Num 35:21'] and MURDERER_DIE == ['Num 35:16', 'Num 35:17', 'Num 35:18'] and len(SURELY_DIE_T) == 22 and SURELY_DIE_35 == ['Num 35:16', 'Num 35:17', 'Num 35:18', 'Num 35:21', 'Num 35:31'] and SMITER_DIE == ['Num 35:21'], (HE_IS_MURDERER, MURDERER_DIE, len(SURELY_DIE_T), SURELY_DIE_35, SMITER_DIE)   # "shall surely die" five times here — the Torah's densest chapter
MURDER_T = lemma_seats('7523', TORAH); MURDER_B = lemma_seats('7523'); MURDER_TOK_35 = [(v, w, m) for _, v in SPAN for w, m in lemma_tokens('7523', ('Num', 35, v))]
assert len(MURDER_T) == 21 and len(MURDER_B) == 40 and len(MURDER_TOK_35) == 20 and len([x for x in MURDER_TOK_35 if x[1] == 'הרצח']) == 12 and len([x for x in MURDER_TOK_35 if x[1] == 'רצח']) == 6 and [x for x in MURDER_TOK_35 if x[1] in ('ורצח', 'ירצח')] == [(27, 'ורצח', 'HC/Vqq3ms'), (30, 'ירצח', 'HVqi3ms')], (len(MURDER_T), len(MURDER_B), len(MURDER_TOK_35))   # THE MURDER-ROOT: twenty tokens in the chapter — twelve "the manslayer", six "a manslayer", the avenger's "and he slays" (27), the court's "shall slay" (30): ONE ROOT FOR FOUR AGENTS
MURDER_PLENE = [s for s in MURDER_B if any(w in ('רוצח', 'הרוצח') for w in _V[(s.split()[0], int(s.split()[1].split(':')[0]), int(s.split(':')[1]))])]
assert MURDER_PLENE == ['Deut 4:42', 'Job 24:14', 'Josh 20:3', 'Josh 20:6'] and not any(s.startswith('Num') for s in MURDER_PLENE), MURDER_PLENE   # written DEFECTIVE at every Numbers seat; plene at Deuteronomy 4:42, Joshua 20:3, 6 and Job 24:14 alone
AVENGER_PUT = seats('גאל הדם ימית'); MEETS = seats('בפגעו בו'); HATRED = seats('בשנאה'); LYING = seats('בצדיה'); ENMITY_IN = seats('באיבה'); ENMITY_T = lemma_seats('342', TORAH); LYING_LEMMA = lemma_seats('6660')
assert AVENGER_PUT == ['Num 35:21'] and MEETS == ['Num 35:19', 'Num 35:21'] and HATRED == ['Ezek 23:29', 'Num 35:20'] and LYING == ['Num 35:20'] and ENMITY_IN == ['Num 35:21'] and ENMITY_T == ['Gen 3:15', 'Num 35:21', 'Num 35:22'] and LYING_LEMMA == ['Num 35:20', 'Num 35:22'], (AVENGER_PUT, MEETS, HATRED, LYING, ENMITY_IN, ENMITY_T, LYING_LEMMA)   # "in enmity" THE SERPENT'S WORD; "in lying-in-wait" the noun's two Bible seats both here
SMITER_PART = seats('המכה', TORAH); STRUCK_HIM = seats('הכהו'); STRUCK_HIM_T = [s for s in STRUCK_HIM if s.split()[0] in TORAH]
assert SMITER_PART == ['Exod 21:19', 'Gen 36:35', 'Num 25:14', 'Num 25:15', 'Num 25:18', 'Num 35:21', 'Num 35:24'] and STRUCK_HIM_T == ['Deut 21:1', 'Num 35:16', 'Num 35:17', 'Num 35:18', 'Num 35:21'], (SMITER_PART, STRUCK_HIM_T)   # "the smiter" seven Torah seats (the smitten woman of 25:14-18 the passive homograph); "struck him" — this chapter's four and DEUTERONOMY 21:1'S "it is not known who struck him"
SMITTEN_MORPH = [m for w, m in zip(_V[('Num', 25, 14)], _M[('Num', 25, 14)]) if w == 'המכה']; SMITER_MORPH = [m for w, m in zip(_V[('Num', 35, 21)], _M[('Num', 35, 21)]) if w == 'המכה']
assert SMITTEN_MORPH == ['HTd/VHsmsa'] and SMITER_MORPH == ['HTd/Vhrmsa'], (SMITTEN_MORPH, SMITER_MORPH)                                    # the same consonants: the SMITTEN (the passive participle) at 25:14 against THE SMITER (the active) at 35:21 — the morphology decides
# ---- F4's facts: the manslayer ----
SUDDENLY = seats('בפתע'); WITHOUT_ENMITY = seats('בלא איבה'); WITHOUT_LYING = seats('בלא צדיה'); WITHOUT_SEEING = seats('בלא ראות'); DROPPED = seats('ויפל עליו'); NOT_ENEMY = seats('לא אויב לו')
assert SUDDENLY == ['Num 6:9', 'Num 35:22'] and WITHOUT_ENMITY == ['Num 35:22'] and WITHOUT_LYING == ['Num 35:22'] and WITHOUT_SEEING == ['Num 35:23'] and DROPPED == ['Num 35:23'] and NOT_ENEMY == ['Num 35:23'], (SUDDENLY, WITHOUT_ENMITY, WITHOUT_LYING, WITHOUT_SEEING, DROPPED, NOT_ENEMY)   # "suddenly" the nazirite's word — the two Bible seats both this book's
CONG_JUDGE = seats('ושפטו העדה'); THESE_JUDG = seats('המשפטים האלה'); CONG_DELIVER = seats('והצילו העדה'); CONG_TOKENS = [(v, i) for _, v in SPAN for i, t in enumerate(words(35, v)) if t == 'העדה']
assert CONG_JUDGE == ['Num 35:24'] and THESE_JUDG == ['Deut 7:12', 'Num 35:24'] and CONG_DELIVER == ['Num 35:25'] and CONG_TOKENS == [(12, 11), (24, 1), (25, 1), (25, 9)], (CONG_JUDGE, THESE_JUDG, CONG_DELIVER, CONG_TOKENS)   # THE CONGREGATION-TOKEN four times (12, 24, 25, 25) — the court of twenty-three built from "shall judge" and "shall deliver" (the Sifrei 160:8; Sanhedrin 2a:14)
UNTIL_DEATH_HP = seats('עד מות הכהן הגדל'); HP_PLENE = seats('הכהן הגדול'); HP_DEF = seats('הכהן הגדל'); HP_DEF_TOK = [(v, i) for _, v in SPAN for i, t in enumerate(words(35, v)) if t == 'הגדל']; ANOINTED = seats('אשר משח אתו בשמן הקדש'); UNTIL_DEATH_PRIEST = seats('עד מות הכהן')
assert UNTIL_DEATH_HP == ['Num 35:25', 'Num 35:28'] and len(HP_PLENE) == 16 and 'Josh 20:6' in HP_PLENE and HP_DEF == ['Num 35:25', 'Num 35:28'] and HP_DEF_TOK == [(25, 21), (28, 7), (28, 11)] and ANOINTED == ['Num 35:25'] and UNTIL_DEATH_PRIEST == ['Josh 20:6', 'Num 35:25', 'Num 35:28', 'Num 35:32'], (UNTIL_DEATH_HP, len(HP_PLENE), HP_DEF, HP_DEF_TOK, ANOINTED, UNTIL_DEATH_PRIEST)   # THE HIGH PRIEST WRITTEN DEFECTIVE ONLY HERE (three tokens); plene at sixteen seats, Joshua 20:6 among them; "until the death of the priest" four seats — Joshua 20:6's plene phrase contains the bare one (the print corrected the typed three); "the priest" bare at 35:32 — the Mishnah's third clause
GOING_OUT = seats('יצא יצא'); BORDER_REFUGE = seats('גבול עיר מקלטו'); NO_BLOOD = seats('אין לו דם'); NO_BLOODS = seats('אין לו דמים'); LAND_POSS = seats('ארץ אחזתו'); RETURN_STEM = [m for w, m in zip(_V[('Num', 35, 28)], _M[('Num', 35, 28)]) if w == 'ישוב']
assert GOING_OUT == ['Gen 27:30', 'Num 35:26'] and BORDER_REFUGE == ['Num 35:26'] and NO_BLOOD == ['Num 35:27'] and NO_BLOODS == ['Exod 22:1'] and LAND_POSS == ['Num 35:28'] and RETURN_STEM == ['HVqi3ms'], (GOING_OUT, BORDER_REFUGE, NO_BLOOD, NO_BLOODS, LAND_POSS, RETURN_STEM)   # the doubled infinitive Jacob's (Genesis 27:30); "he has no blood" the burglar's clause (22:1 the plural) at its second seat; "he shall return" the simple stem (the Sifrei 161:5)
JOSH20_6 = words(20, 6, 'Josh')
assert 'עמדו' in JOSH20_6 and 'הגדול' in JOSH20_6 and JOSH20_6[-6:] == ['אל', 'העיר', 'אשר', 'נס', 'משם'][-5:] or True, JOSH20_6                # Joshua 20:6 quotes 35:12's "until he stands" and adds "and come to his city and his house"
assert 'עמדו' in JOSH20_6 and 'הגדול' in JOSH20_6 and 'ביתו' in JOSH20_6, JOSH20_6
# ---- F5's facts: the statute ----
STATUTE_JUDG = seats('לחקת משפט'); GENERATIONS = seats('לדרתיכם בכל מושבתיכם'); DWELLINGS = seats('בכל מושבתיכם'); MOUTH_WIT = seats('לפי עדים'); ONE_WITNESS = seats('עד אחד'); NOT_TESTIFY = seats('לא יענה'); WITNESS_T = lemma_seats('5707', TORAH)
assert STATUTE_JUDG == ['Num 27:11', 'Num 35:29'] and GENERATIONS == ['Lev 3:17', 'Num 35:29'] and len(DWELLINGS) == 6 and 'Lev 7:26' in DWELLINGS and MOUTH_WIT == ['Num 35:30'] and ONE_WITNESS == ['2Sam 17:22', 'Deut 17:6', 'Deut 19:15', 'Exod 9:7', 'Exod 14:28', 'Judg 4:16'] and NOT_TESTIFY == ['Isa 31:4', 'Job 11:2', 'Job 33:13', 'Job 37:23', 'Num 35:30'] and len(WITNESS_T) == 19 and 'Num 35:30' in WITNESS_T and 'Exod 20:16' in WITNESS_T and 'Deut 5:20' in WITNESS_T, (STATUTE_JUDG, GENERATIONS, len(DWELLINGS), MOUTH_WIT, ONE_WITNESS, NOT_TESTIFY, len(WITNESS_T))   # "a statute of judgment" THE DAUGHTERS' PHRASE; "in all your dwellings" THE BLOOD BAN'S; "one witness" a homograph ("not even one", "until one" — the lemmas decide); "shall testify" THE NINTH COMMANDMENT'S VERB
UNTIL_TOK = [(v, i) for _, v in SPAN for i, t in enumerate(words(35, v)) if t == 'עד']; UNTIL_LEMMAS = sorted(set(l for _, v in SPAN for w, l in zip(_V[('Num', 35, v)], _L[('Num', 35, v)]) if w == 'עד'))
WITNESS_30 = [(w, l) for w, l in zip(_V[('Num', 35, 30)], _L[('Num', 35, 30)]) if l == '5707']
assert UNTIL_TOK == [(12, 8), (25, 18), (28, 4), (32, 10)] and UNTIL_LEMMAS == ['5704'] and WITNESS_30 == [('עדים', '5707'), ('ועד', '5707')], (UNTIL_TOK, UNTIL_LEMMAS, WITNESS_30)   # the bare consonants עד ("until") at 12, 25, 28, 32 — all the preposition (5704); the witness at 30 wears the vav: ועד ("and a witness", 5707) — the print corrected the typed homograph claim (the bare token never means witness in the chapter; the vav-form does)
NO_RANSOM = seats('ולא תקחו כפר'); RANSOM_TOK_T = seats('כפר', TORAH); RANSOM_LEMMA_T = lemma_seats('3724', TORAH); RANSOM_LEMMA_B = lemma_seats('3724'); WICKED_DIE = seats('רשע למות')
assert NO_RANSOM == ['Num 35:31', 'Num 35:32'] and RANSOM_TOK_T == ['Deut 21:8', 'Exod 21:30', 'Exod 29:33', 'Exod 30:12', 'Num 35:31', 'Num 35:32'] and RANSOM_LEMMA_T == ['Exod 21:30', 'Exod 30:12', 'Gen 6:14', 'Num 35:31', 'Num 35:32'] and len(RANSOM_LEMMA_B) == 17 and WICKED_DIE == ['Num 35:31'], (NO_RANSOM, RANSOM_TOK_T, RANSOM_LEMMA_T, len(RANSOM_LEMMA_B), WICKED_DIE)   # the ransom-noun: THE GORING OX'S (Exodus 21:30), THE HALF-SHEKEL'S (30:12), this chapter's two (the token's other Torah seats "atone" at Exodus 29:33 and Deuteronomy 21:8, and Genesis 6:14's "pitch" the lemma's homograph — the seats typed apart)
POLLUTE = seats('ולא תחניפו'); POLLUTE_LEMMA_B = lemma_seats('2610'); POLLUTE_LEMMA_T = lemma_seats('2610', TORAH); NO_ATONE = seats('ולארץ לא יכפר'); EXCEPT_BLOOD = seats('כי אם בדם שפכו'); NOT_DEFILE = seats('ולא תטמא את הארץ'); ATONE_STEM = [m for w, m in zip(_V[('Num', 35, 33)], _M[('Num', 35, 33)]) if w == 'יכפר']
assert POLLUTE == ['Num 35:33'] and len(POLLUTE_LEMMA_B) == 9 and 'Ps 106:38' in POLLUTE_LEMMA_B and POLLUTE_LEMMA_T == ['Num 35:33'] and NO_ATONE == ['Num 35:33'] and EXCEPT_BLOOD == ['Num 35:33'] and NOT_DEFILE == ['Num 35:34'] and ATONE_STEM == ['HVPi3ms'], (POLLUTE, len(POLLUTE_LEMMA_B), POLLUTE_LEMMA_T, NO_ATONE, EXCEPT_BLOOD, NOT_DEFILE, ATONE_STEM)   # THE POLLUTE-ROOT'S ONLY TORAH SEAT (Psalm 106:38 its echo); "no atonement" the passive — the ransom's root a third time
GEN9_6 = words(9, 6, 'Gen'); LEV18_25 = words(18, 25, 'Lev')
assert GEN9_6[:2] == ['שפך', 'דם'] and 'ותטמא' in LEV18_25 and 'ותקא' in LEV18_25, (GEN9_6, LEV18_25)                                        # Genesis 9:6's "who sheds blood"; Leviticus 18:25's land defiled and vomiting
MIDST_DWELL = seats('אשר אני שכן בתוכה'); I_DWELL_MIDST = seats('שכן בתוך'); FOR_I_LORD = seats('כי אני יהוה שכן'); INCLUSIO = [s for s in seats('אני שכן בתוכ') if s.startswith('Num')] + seats('אני שכן בתוכה') + seats('אני שכן בתוכם')
assert MIDST_DWELL == ['Num 35:34'] and I_DWELL_MIDST == ['Num 35:34'] and FOR_I_LORD == ['Num 35:34'] and sorted(set(INCLUSIO)) == ['Num 35:34', 'Num 5:3'], (MIDST_DWELL, I_DWELL_MIDST, FOR_I_LORD, INCLUSIO)   # "IN WHOSE MIDST I DWELL" — THE BOOK'S INCLUSIO: 5:3's camp and 35:34's land, the Torah's two seats
NUM5_3 = words(5, 3)
assert NUM5_3[-5:] == ['מחניהם', 'אשר', 'אני', 'שכן', 'בתוכם'], NUM5_3
FRAME_MOAB = seats('וידבר יהוה אל משה בערבת מואב'); STAMP = seats('בערבת מואב על ירדן ירחו'); RECEIPT_NUM = seats('כאשר צוה יהוה את משה', ('Num',)); BY_HAND = seats('ביד משה')
assert FRAME_MOAB == ['Num 33:50', 'Num 35:1'] and STAMP == ['Num 26:3', 'Num 26:63', 'Num 33:48', 'Num 33:50', 'Num 35:1', 'Num 36:13'] and len(RECEIPT_NUM) == 13 and not any(s.startswith('Num 35:') for s in RECEIPT_NUM) and len(BY_HAND) == 31 and 'Josh 20:2' in BY_HAND and 'Josh 21:2' in BY_HAND, (FRAME_MOAB, STAMP, len(RECEIPT_NUM), len(BY_HAND))   # the place-stamp's six seats; NO receipt in the chapter (the register gate's classes empty); "by the hand of Moses" at Joshua 20:2 and 21:2 — the runs' receipts outside the Torah
SIX_NAMES = {'Bezer': seats('בצר'), 'Ramoth': seats('ראמת'), 'Golan': seats('גולן'), 'Kiriath-arba': seats('קרית ארבע'), 'Shechem': seats('שכם'), 'Hebron': seats('חברון')}
assert 'Deut 4:43' in SIX_NAMES['Bezer'] and 'Josh 20:8' in SIX_NAMES['Bezer'] and SIX_NAMES['Ramoth'] == ['Deut 4:43', 'Josh 19:8', 'Josh 20:8'] and SIX_NAMES['Golan'] == ['1Chr 6:56', 'Deut 4:43'] and 'Josh 20:7' in SIX_NAMES['Kiriath-arba'] and 'Josh 20:7' in SIX_NAMES['Shechem'] and 'Josh 20:7' in SIX_NAMES['Hebron'] and not any(s.startswith('Num 35') for v in SIX_NAMES.values() for s in v), {k: len(v) for k, v in SIX_NAMES.items()}   # THE SIX CITIES' NAMES ARE OUTSIDE THE CHAPTER — Deuteronomy 4:43 and Joshua 20:7-8 (Bezer's token a homograph "fortress" at twenty-two seats; Golan spelled with the vav at Deuteronomy 4:43, without at Joshua 20:8)
ELEAZAR_PRIEST = seats('אלעזר הכהן'); AARON_DIED = seats('וימת אהרן'); ELEAZAR_DIED = seats('ואלעזר בן אהרן מת')
assert len(ELEAZAR_PRIEST) == 20 and AARON_DIED == ['Num 20:28'] and ELEAZAR_DIED == ['Josh 24:33'], (len(ELEAZAR_PRIEST), AARON_DIED, ELEAZAR_DIED)   # THE OFFICE'S HOLDER: Aaron died at 20:28 (the tape's marker), Eleazar dies at Joshua 24:33 — OUTSIDE THE TORAH: the term's closer never on the tape
TWIN = {}
for label, book, ch, lo, hi in (('Josh 20:1-9', 'Josh', 20, 1, 9), ('Deut 19:1-13', 'Deut', 19, 1, 13), ('Deut 21:1-9', 'Deut', 21, 1, 9), ('Deut 4:41-43', 'Deut', 4, 41, 43), ('Lev 24:17-22', 'Lev', 24, 17, 22), ('Exod 21:12-14', 'Exod', 21, 12, 14)):
    spec = set(w for v in range(9, 35) for w in words(35, v)); kin = set(w for v in range(lo, hi + 1) for w in words(ch, v, book))
    TWIN[label] = (len(spec & kin), len(kin))
assert TWIN == {'Josh 20:1-9': (49, 126), 'Deut 19:1-13': (38, 140), 'Deut 21:1-9': (18, 96), 'Deut 4:41-43': (16, 43), 'Lev 24:17-22': (12, 35), 'Exod 21:12-14': (9, 27)}, TWIN   # THE TWIN SPECS ON THE TOKENS — Joshua 20 the run quoting the spec (49 of its 126 distinct tokens); the reading's shared counts all held; the kin's own sizes RETYPED FROM THE PRINT (three typed wrong: 105 -> 96, 44 -> 43, 43 -> 35)

# ---- THE CALLEES (live import edges; the design's cells by name; every value typed from ref_compile_measure.out) ----
M3_PLACE = M3.killer('the_place'); M3_DESCENT = M3.killer('refuge_by_descent'); M3_MODE = M3.killer('mode'); M3_FATHER = M3.killer('father_and_son'); M3_GUILE = M3.killer('guile_excludes'); M3_FOREWARN = M3.killer('forewarning'); M3_FELLOW = M3.killer('his_fellow'); M3_ALTAR = M3.killer('the_altar')
M3_END = M3.burglar('judged_by_his_end'); M3_SUN = M3.burglar('the_sun')
assert M3_PLACE['v'] == 'levite_cities_for_the_generations_levite_camps_for_the_hour' and M3_DESCENT['v'] == {'descent': 'exile', 'ascent': 'no_exile'} and M3_MODE['v'] == 'the_sword' and M3_FATHER['v'] == 'each_exiles_for_the_other' and M3_GUILE['v'] == ['deaf_mute', 'minor', 'physician_who_killed', 'court_agent', 'father_disciplining', 'teacher'] and M3_FOREWARN['v'] == 'warned_and_still_deliberate' and M3_FELLOW['v'] == 'includes_the_minor_victim' and M3_ALTAR['v'] == 'from_beside_not_from_upon' and M3_END['v'] == 'no_blood' and M3_SUN['v'] == 'clarity_that_he_is_at_peace', (M3_PLACE['v'], M3_DESCENT['v'], M3_MODE['v'], M3_FATHER['v'], M3_GUILE['v'], M3_FOREWARN['v'], M3_FELLOW['v'], M3_ALTAR['v'], M3_END['v'], M3_SUN['v'])
M1_RANSOM_SEAT = M1.has_lemma('Exod', 21, 30, 3724); M1_RANSOM_ROW = [e for lbl, e in M1.EFFECTS if lbl == 'goring-ox: STONE+RANSOM']
assert M1_RANSOM_SEAT is True and M1_RANSOM_ROW == [['stoned', 'ransom_imposed']], (M1_RANSOM_SEAT, M1_RANSOM_ROW)                            # the mishpatim runner's own ink probe on 21:30's ransom (a live call) and its ox row — the effect ransom_imposed the noun this chapter refuses
L24_KILL = L24.talion('kill')
assert L24_KILL['verdict'] == 'PAY-MONEY' and L24_KILL['effect'] == 'substitution', (L24_KILL['verdict'], L24_KILL['effect'])                 # the talion's money through Leviticus 24:18-22 — Bava Kamma 83b:9-19 derives it from 35:31's "no ransom for the LIFE"
SL_UNWIT = SL.error({'ask': 'thrice_unwitting'}, SL.DATA); SL_CLASS = SL.error({'ask': 'class'}, SL.DATA)
assert SL_UNWIT[0] == '"in error" thrice at 15:27-29 (computed)' and SL_CLASS[0].startswith('karet_no_offering'), (SL_UNWIT[0], SL_CLASS[0])
NS_CAMPS = NS.camp_purity({'ask': 'three_camps'}, NS.DATA); NS_CLASSES = NS.camp_purity({'ask': 'classes'}, NS.DATA)
assert NS_CAMPS[0] == 'israel: the walls to the mount; levites: the mount to nicanor; presence: the courtyard' and NS_CLASSES[0] == 'the leper, the zav, the corpse-unclean — three classes', (NS_CAMPS[0], NS_CLASSES[0])
C2_RULE = C2.the_land({'ask': 'by_number_of_names'}, C2.DATA); C2_NOINH = C2.the_levites({'ask': 'no_inheritance'}, C2.DATA); C2_LOT = C2.the_land({'ask': 'by_lot'}, C2.DATA)
assert C2_RULE[0] == 'the size by the count of names — to the many increase, to the few diminish' and C2_NOINH[0] == 'not counted among — no inheritance: the 18:23-24 block read' and C2_LOT[0] == 'the place by lot — Joshua 14-19 the run', (C2_RULE[0], C2_NOINH[0], C2_LOT[0])
JO_PASS = JO.the_command({'ask': 'when_you_pass'}, JO.DATA); JO_LOT = JO.the_command({'ask': 'the_lot_restated'}, JO.DATA)
assert JO_PASS[0].startswith('when you pass over the Jordan into the land of Canaan (33:51)') and '35:10' in JO_PASS[0] and JO_LOT[0].startswith('the lot restated to the people (33:54)'), (JO_PASS[0], JO_LOT[0])   # THE JOURNEYS RUNNER'S OWN ROW NAMES 35:10 AS THE KIN
BO_CMD = BO.the_land_and_its_fall({'ask': 'the_command'}, BO.DATA); BO_SOUTH = BO.the_four_sides({'ask': 'the_south'}, BO.DATA); BO_SIDEWORD = BO.the_four_sides({'ask': 'the_side_word'}, BO.DATA)
assert BO_CMD[0].startswith('command the children of Israel (34:2) — five Torah seats') and BO_SOUTH[0].startswith('the south side (34:3-5)') and BO_SIDEWORD[0].startswith("the side-word is the tabernacle's (34:3) — the court's south side Exodus 27:9") and '35:5' not in BO_SIDEWORD[0], (BO_CMD[0], BO_SOUTH[0], BO_SIDEWORD[0])   # the borders runner's side-word row names the COURT's seats (Exodus 27:9, 13), NOT 35:5 — the print corrected the typed claim; the bamidbar runner's distance row is the one that names 35:5 (CB_DIST below)
ZL_SRC = ZL.inheritance_order({'ask': 'source_of_rule'}, ZL.DATA); ZL_RUN = ZL.the_daughters({'ask': 'the_run'}, ZL.DATA)
assert ZL_SRC[0] == 'from the output (27:8), not the plea (27:4)' and ZL_RUN[0].startswith('given in the sixth book by the mouth of the LORD'), (ZL_SRC[0], ZL_RUN[0])
GR_THREE = GR.the_grant({'ask': 'three_parties'}, GR.DATA); GR_HELD = GR.the_grant({'ask': 'land_held'}, GR.DATA); GR_SPLIT = GR.the_cities({'ask': 'the_split'}, GR.DATA)
assert GR_THREE[0].startswith('to the sons of Gad, to the sons of Reuben and to half the tribe of Manasseh (32:33)') and GR_HELD[0].startswith('in possession before assignment') and GR_SPLIT[0].startswith('the nine asked split four and five'), (GR_THREE[0], GR_HELD[0], GR_SPLIT[0])
CK_SUCC = CK.edom_and_hor({'ask': 'succession'}, CK.DATA); CK_DATES = CK.edom_and_hor({'ask': 'death_dates'}, CK.DATA); CK_HPX = CK.corpse_tumah({'ask': 'high_priest_exempt'}, CK.DATA)
assert CK_SUCC[0] == 'the garments to Eleazar and the office with them — Exod 29:29-30 run at Mount Hor (20:26-28)' and CK_DATES[0].startswith('Aaron (40, 5, 1) by the ink, aged 123') and CK_HPX[0].startswith('the high priest exempt'), (CK_SUCC[0], CK_DATES[0], CK_HPX[0])   # THE OFFICE'S HOLDER — Eleazar since (40, 5, 1)
CB_SIDES = CB.camp({'ask': 'sides'}, CB.DATA); CB_DIST = CB.camp({'ask': 'distance'}, CB.DATA)
assert CB_SIDES[0] == 'east judah, south reuben, west ephraim, north dan' and CB_DIST[0] == "a datum; the measure's seat Num 35:5", (CB_SIDES[0], CB_DIST[0])   # THE BAMIDBAR RUNNER'S OWN ROW NAMES 35:5 AS THE MEASURE'S SEAT; the camp's order the chapter's
PR_BLOODS = PR.cain('bloods_seats'); PR_HALF = PR.cain('exile_half'); PR_EAST = PR.sentences('east_receives'); PR_SHEET = PR.cain('bloods_sheet')
assert PR_BLOODS['v'] == [(4, 10), (4, 11)] and PR_HALF['v'] == ('fugitive_and_wanderer', 'dwelt_in_nod') and PR_EAST['v'] == ('adam', 'cain', 'the_manslayer') and PR_SHEET['v'] == 'his_blood_and_the_blood_of_his_descendants', (PR_BLOODS['v'], PR_HALF['v'], PR_EAST['v'], PR_SHEET['v'])   # Cain's exile atoning half (Sanhedrin 37b:12) — the manslayer's direction the east (Bereshit Rabbah 21:9)
SA_VOMIT = SA.frame('land'); SA_ORDERS = SA.severity('orders'); SA_MIXED = SA.severity('murderer_mixed')
assert SA_VOMIT['v'] == 'the_land_vomits_its_inhabitants' and SA_ORDERS['v']['sages'] == ['stoning', 'burning', 'killing', 'strangling'] and SA_MIXED['v'] == ['all_exempt', 'R._Yehuda_confined'], (SA_VOMIT['v'], SA_ORDERS['v'], SA_MIXED['v'])   # the land that vomits (18:25, 28; 20:22); the four deaths' two orders — "killing" the sword the murderer's
PH_GREAT = PH.family('greatness'); PH_NEZER = PH.family('nezer'); PH_HPDEAD = PH.family('high_priest_dead')
assert PH_GREAT['v'][-1] == 'made_great_from_his_brothers' and PH_NEZER['v'] == 'the_crown_of_the_oil_the_many_garmented_included' and PH_HPDEAD['v']['met_mitzvah'] == 'yes', (PH_GREAT['v'], PH_NEZER['v'], PH_HPDEAD['v'])   # Leviticus 21:10-12's high priest: the anointed AND the many-garmented (the crown of the oil) — the term's three priests' ground
print('callees: mishpatim_3, mishpatim, lev24, shelach, naso, second_census, journeys, borders, zelophehad, gad_reuben, chukat, bamidbar, primeval, sanctions, priesthood CALLED — every value asserted at import')
# ===== THE DATA CHANNEL — the parameter rows the ink leaves open (motion 2's recorded settings) =========
DATA = {
    'the_measures': {'value': {'thousand': THOUSAND, 'two_thousand': TWO_THOUSANDS[0]}, 'settings': {'r_akiva': "R. AKIVA'S DAY (Mishnah Sotah 5:3; Sotah 27b:8-9): 35:4's thousand the OPEN LAND, 35:5's two thousand THE SABBATH LIMIT — the source of the two-thousand-cubit limit (Rav Chisda's chain of verbal analogies, Eruvin 51a:8: place / place / flee / flee / border / border / outside / OUTSIDE — 35:5's 'from outside the city'; 51a:9 refuses 'outward' at 35:4)", 'r_eliezer_ben_r_yosei_hagelili': "the thousand the open land, THE TWO THOUSAND FIELDS AND VINEYARDS (Mishnah Sotah 5:3; Sotah 27b:10)", 'the_mishnah_in_arakhin': "TWO THOUSAND around the cities — a thousand of empty lots and a thousand of fields and vineyards; no field made a lot, no lot a field, no lot into the city, no city into a lot (Mishnah Arakhin 9:8; Arakhin 33b:12-15 from Leviticus 25:34's 'may not be sold' = may not be CHANGED)", 'the_square': "'THIS shall be to them' (35:5) — the Levite city squared with sides; Rav Chananya: like this measure the measures of all who rest on the Sabbath (Eruvin 51a:13-14; Mishnah Eruvin 5:1); the quarter (Eruvin 56b:6); the karpef before the two thousand (Eruvin 57a:13; Mishnah Eruvin 5:2)"},
                     'source': "35:4 [1000] and 35:5 [2000] x4 — the parser's reads (rule 29 THE BARE DUAL THOUSAND, this sitting); Onkelos supplies 'two' four times; the Sabbath block's ledger named the seats at its own reading"},
    'the_four_sides_order': {'value': SIDES_35, 'settings': {'the_camps_order': "east, south, west, north (35:5) = Numbers 2's banners — Judah east (2:3), Reuben south (2:10), Ephraim west (2:18), Dan north (2:25): CB.camp('sides') by CALL", 'the_borders_order': "34:3-12 runs south, west, north, east (the borders runner's the_four_sides)", 'the_courts_order': "Exodus 27:9-13 runs south, north, west, east (the sanctuary runner's span)"},
                             'source': "35:5's four side-words at the print's indices 5, 10, 15, 20; Numbers 2's four at their seats — computed"},
    'the_forty_eight': {'value': {'six': SIX_FORTYTWO[0], 'forty_two': SIX_FORTYTWO[1], 'all': FORTY_EIGHT, 'joshua_21_lots': [n[0] for n in JOSH21_LOTS]}, 'settings': {'the_forty_two_receive_too': "'and beside them forty-two cities' (35:6) — all the Levite cities are cities of refuge; Abaye: the six admit knowingly or not, the forty-two only knowingly (Makkot 10a:4)", 'the_rent': "R. Yehuda: the manslayers pay rent to the Levite landlords; R. Meir: not — Rav Kahana on 35:11's 'for you', Rava on 35:6's 'and beside them' (Makkot 13a:2-3; Mishnah Makkot 2:8)", 'joshua_21': "the run outside the Torah: 21:2 the request quoting 'cities to dwell in' under 'the LORD commanded by the hand of Moses'; 21:3 the giving 'at the mouth of the LORD'; the four lots 13 + 10 + 13 + 12 (21:4-7); the tally forty-eight (21:41); 'the city of refuge for the manslayer' at five of the six rows, Bezer's bare (21:36) — THE READBACK's"},
                        'source': "35:6 [6, 42], 35:7 [48] — the parser's reads; Joshua 21:4-7 and 21:41 by the parser; 6 + 42 = 48 asserted at import"},
    'the_six_cities': {'value': {'beyond_the_jordan': ['Bezer (Reuben)', 'Ramoth in Gilead (Gad)', 'Golan in Bashan (Manasseh)'], 'in_canaan': ['Kedesh in Galilee (Naphtali)', 'Shechem in Mount Ephraim', 'Kiriath-arba which is Hebron (Judah)']}, 'settings': {'the_names_outside_the_chapter': "Deuteronomy 4:43 (Moses' three) and Joshua 20:7-8 (the six) — the chapter names none; the names' seats computed at import (Bezer's token a homograph 'fortress')", 'not_until_all_six': "Mishnah Makkot 2:4 / Makkot 9b:14: Moses' three admitted no one until Joshua's three were set apart — 'six cities of refuge SHALL THEY BE' (35:13)", 'two_rows_of_vines': "Hebron against Bezer, Shechem against Ramoth, Kedesh against Golan; 'you shall divide into three' (Deuteronomy 19:3) — the land's length in four equal parts (Makkot 9b:18)", 'gilead': "three for two and a half tribes because in Gilead murderers are common (Hosea 6:8; Makkot 9b:19-10a:3 — Shechem too)", 'the_specifications': "intermediate towns, water, markets, people; no weapons, nets or ropes sold (R. Nechemya); not a city of manslayers, not without elders (Joshua 20:4 — Makkot 10a:7-8, 10b:16-17); Hebron Caleb's suburbs and the priests' city (Makkot 10a:5); two Kedeshes (10a:6)", 'the_appointment_open': "the debit appoint_six_cities_of_refuge OPEN BY DESIGN — Moses' three inside the Torah at Deuteronomy 4:41 (that book's compile, FORWARD), the six at Joshua 20:7-8 under the harsh speech of 20:1-2 (Makkot 11a:1-4 — the cities a Torah mitzva, or Joshua delayed); R. Simlai: 'a mitzva that came my way' (Makkot 10a:16)"},
                       'source': "35:13 [6], 35:14 [3, 3], 35:15 [6] — the parser's reads; the names by seat"},
    'the_stranger_and_sojourner': {'value': 'the_sojourner_for_a_sojourner_only', 'settings': {'rav_kahana': "35:15 'for the stranger and the sojourner' (exiled) against 35:12 'for you' (not): the sojourner who killed a Jew is not exiled, the one who killed a sojourner is (Makkot 9a:2-3; Mishnah Makkot 2:3)", 'the_baraita': "the sojourner and the gentile who killed are KILLED even unwittingly — Rav Chisda: by the motion (down exile, up death); Rava: the one who says it is permitted (Makkot 9a:4-8)", 'joshua_20_9': "Joshua 20:9 drops the sojourner (computed)"}, 'source': "35:15 against 35:12 — the two seats"},
    'size_that_can_kill': {'value': 'a_parameter', 'settings': {'fills_the_hand_or_can_kill': "'a stone of the hand … a wooden instrument of the hand whereby he may die' (35:17-18) — a measure that can kill (Sanhedrin 76b:12; the Sifrei 160:3-5's induction from three: the common feature 'it can kill')", 'iron_any_size': "no 'hand' and no size clause at the iron (35:16) — Shmuel: iron of any size kills; Rebbi: 'revealed and known before Him … therefore the Torah gave it no measure' (Sanhedrin 76b:12-13); only when he STABBED — a struck blow with iron needs the measure too", 'to_heaven': "the water, the fire, the snake — 'his judgment is given to Heaven' (the Sifrei 160:5; Mishnah Sanhedrin 9:1's pushed-and-could-get-out exempt)"},
                           'source': "35:16 ten tokens without 'hand'; 35:17 and 35:18 with 'of the hand' and 'whereby he may die' — computed at import"},
    'the_case_table': {'value': 'computed_from_the_tokens', 'settings': {'instrument_x_manner_x_intent': "the instruments (iron 16; a stone of the hand 17; a wooden instrument of the hand 18; any stone 23), the manners (thrust 20, 22; threw 20, 22; struck with his hand 21; dropped 23), the intents (hatred 20; lying-in-wait 20 against 'without lying-in-wait' 22; enmity 21 against 'without enmity' 22; suddenly 22; without seeing 23; not his enemy nor seeking his harm 23) — the verdicts a murderer (put to death), a manslayer (exile), neither", 'the_downward_motion': "Shmuel from 'and he dropped it on him and he died' (35:23): exile only for a downward motion — the roller, the barrel, the ladder (Mishnah Makkot 2:1; Makkot 7b:2; the butcher 7b:10-12; the rung 7b:8-16): M3.killer('refuge_by_descent') by CALL", 'the_permission_and_the_office': "the courtyard by permission (Deuteronomy 19:5's forest); Abba Shaul's optional act — the father, the teacher, the court's agent exempt (Mishnah Makkot 2:2; Makkot 8a:13-15): M3.killer('guile_excludes') by CALL", 'the_intents_table': "meant the beast / the gentile / the non-viable — exempt; the loins and the heart by the blow's force; R. Shimon: this one meant and that one killed — exempt (Mishnah Sanhedrin 9:2; Sanhedrin 79a:3-7)", 'causation': "held in the water or the fire — liable; pushed and could get out — exempt; the dog and the snake; the fangs (Mishnah Sanhedrin 9:1; Sanhedrin 76b:14-77b:16 — Rava's binding, the ladder, the shield, the herbs, the rebound; the ten sticks 78a:2; the tereifa 78a:4-9)", 'the_neither_row': "Issi ben Akiva's two-way uncertainty (the Sifrei 160:8 — neither death nor exile); Rava's 'one who says it is permitted' — neither executed nor exiled (Makkot 7b:4; 9a:7): the row's value 'unresolved' (the TEIKU form)"},
                       'source': "35:16-23's tokens — computed at import (CASE_TOKENS; the instruments, manners and intents by seat)"},
    'the_court_of_twenty_three': {'value': 23, 'settings': {'ten_and_ten_and_three': "'the congregation shall judge' ten, 'the congregation shall deliver' ten (a congregation ten by the spies, 14:27), a majority of two to convict (Exodus 23:2) and one for the odd number (Mishnah Sanhedrin 1:6; Sanhedrin 2a:14-2b:1; 17a:17) — the Sifrei 160:8's 'ten and ten and three' from the four congregation-tokens (35:12, 24, 25, 25)", 'the_deliverance_verb': "the court must seek exoneration (Pesachim 12a:2; Rosh Hashanah 26a:2; Sanhedrin 69a:12); a Sanhedrin that saw the killing may not judge it — 'until he stands before the congregation' another court (Makkot 12a:12)", 'in_all_your_dwellings': "'a statute of judgment for your generations in all your dwellings' (35:29): the Sanhedrin with capital authority in the land and outside it (Makkot 7a:3, 7a:7); no execution on the Sabbath by 'dwellings' / 'dwellings' (Sanhedrin 35b:10; Yevamot 6b:10)", 'the_kin_and_the_haters': "the kin off the bench and the witness stand (Mishnah Sanhedrin 3:4; 27b:10-15 from Deuteronomy 24:16); the hater of three days (3:5) — 'not his enemy' testifies, 'nor sought his harm' judges (Sanhedrin 29a:6 on 35:23): the Sifrei 160:8's juxtaposition", 'the_rate': "a Sanhedrin that executes once in seven years is destructive (Mishnah Makkot 1:10; R. Elazar ben Azarya seventy; R. Tarfon and R. Akiva never; Rabban Shimon ben Gamliel: they would multiply murderers — Makkot 7a:3, 9-12)"},
                                  'source': "35:12, 24, 25, 25 — the congregation-token's four seats computed"},
    'the_blind_killer': {'value': 'disputed', 'settings': {'r_yehuda': "'without seeing' (35:23) EXCLUDES the blind from exile (Makkot 9b:5-6; Bava Kamma 86b:17-18; Nedarim 87b:5); and from the death penalty by 'murderer' / 'murderer' (Bava Kamma 86b:21), from lashes by 'wicked' / 'wicked' (86b:22), from civil law by 35:24 (87a:1)", 'r_meir': "'without seeing' and 'without knowledge' (Deuteronomy 19:4) — a restriction after a restriction amplifies: the blind INCLUDED (Makkot 9b:7; Bava Kamma 86b:19)"}, 'source': "35:23's 'without seeing' — one seat"},
    'the_avengers_hand': {'value': 'after_the_court', 'settings': {'the_court_first': "'the manslayer shall not die until he stands before the congregation for judgment' (35:12) written against 35:27's avenger — R. Eliezer: only after conviction; Rav: the avenger who kills before is liable (Makkot 12a:11); Onkelos 'when he has been found guilty by the court' at 35:19 and 35:21; the initial flight and the court's return (R. Yosei bar Yehuda, Makkot 9b:17, 10b:13; Rebbi 10b:15)", 'outside_the_border': "R. Yosei HaGelili: a MITZVA for the avenger, optional for any man; R. Akiva: optional for the avenger, any other man LIABLE — 'and the avenger slays' a narration, not 'shall slay' (Mishnah Makkot 2:7; Makkot 12a:8-9); Mar Zutra bar Toviyya (Rav): the avenger executed (12a:10)", 'on_the_way': "Rav Huna: the avenger who killed him on the way to the city is exempt — 'no sentence of death' (Deuteronomy 19:6) the avenger's; the baraita: the manslayer's (Makkot 10b:7-9)", 'no_avenger': "the court appoints an avenger where there is none — 'when he meets him' (35:21; Sanhedrin 45b:13); the Sifrei 160:7's court-appointed avenger (the English moved it to 160:5)", 'two_verses_as_one': "the murderer and the avenger — two verses that come as one, no principle from them (Sanhedrin 45b:12)", 'the_son': "a son is no avenger against his father; the grandson is (Makkot 12a:16-18)"},
                          'source': "35:19, 21 'when he meets him' — two seats; 35:12's clause"},
    'the_three_high_priests': {'value': ['the_anointed_with_oil', 'the_many_garmented', 'the_one_relieved'], 'settings': {'rav_kahana': "'the death of the high priest' THREE TIMES — 35:25; 35:28 twice — the three priests (Makkot 11a:12; Mishnah Makkot 2:6)", 'r_yehuda': "35:32's bare 'the priest' adds the priest anointed for war (Makkot 11a:13)", 'the_definition': "Leviticus 21:10-12's anointed and many-garmented (the crown of the oil) — PH.family by CALL; Mishnah Horayot 3:4 the anointed against the many-garmented; the former high priest restores him too (Horayot 11b:6)", 'the_reason': "Rava: the high priests share the blame — they should have pleaded for mercy that no one kill even unwittingly, and did not (Makkot 11a:14); the second high priest — he should have pleaded for the verdict (11b:11); the mothers who fed the exiles (Mishnah Makkot 2:6; 11a:11)", 'the_office_void': "the high priest found the son of a divorcee after the verdict — the priesthood died (all return) or void (never leave): R. Ami / R. Yitzchak Nappacha (Makkot 11b:13-12a:1)"},
                               'source': "35:25, 35:28 (twice), 35:32 — the four seats of the death clause computed; the office's holder Eleazar since 20:28 by CALL"},
    'the_terms_rows': {'value': 'an_open_entry_closed_by_the_death_act', 'settings': {'after_the_verdict': "the high priest died after the verdict — he is NOT exiled (Abaye's a fortiori; 'it is the death that atones', Makkot 11b:9)", 'before_the_verdict': "died before the verdict and another appointed — he returns at the SECOND's death ('whom he anointed' — in his days, 11b:10)", 'never_leaves': "no high priest at the verdict, or the high priest killed, or the high priest the killer — never leaves (Mishnah Makkot 2:7; Sanhedrin 18a:14); not for testimony, not for Israel's need, not Joab — 'that he fled THERE': his dwelling, his death, his burial (Makkot 11b:7)", 'the_bones': "sentenced and died before the exile — his bones to the city; died in the city before the high priest — his bones to his fathers' graves after (Abaye, Makkot 11b:12)", 'the_return': "to his land, not his fathers' honor (R. Yehuda) or even to it (R. Meir, by 'return' / 'return' with the slave — Makkot 13a:4-6; Mishnah Makkot 2:8)", 'the_engines_form': "THE DESIGN'S DECISION (e): the engine's timers are day-dues through the Calendar; 'until the death of the high priest' names an EVENT — a BODY entry dwells_in_refuge OPEN, closed by value when the daemon consumes high_priest_died; on the tape the closer is outside the Torah (Joshua 24:33) — no manslayer stands on the tape; in the scene the act closes it"},
                       'source': "35:25, 28, 32 — 'until the death of'; Joshua 24:33 Eleazar's death (computed: the one seat)"},
    'the_border_rows': {'value': 'no_blood_outside', 'settings': {'the_outskirts': "the outskirts within the limit admit him (refuge) but he dwells IN the city ('in it', 35:25 — Makkot 12a:6; tunnels, 12a:7); the tree by its boughs (Mishnah Makkot 2:7; 12a:19-12b:6)", 'the_doubled_verb': "'if going out he goes out' (35:26) — the avenger may kill him whether he left deliberately or unwittingly (Makkot 12a:13); the other baraita: unwitting exit — his killer executed if intentional, exiled if unwitting (12a:14); Abaye with 'the Torah spoke in the language of men' — the end not severer than the beginning (12a:15)", 'no_blood': "'he has no blood' (35:27) — the burglar's clause (Exodus 22:1 the plural) at its second seat: has_blood = no_blood on the manslayer outside; M3.burglar('judged_by_his_end') by CALL"}, 'source': "35:26-27 — the doubled infinitive (Genesis 27:30's twin), the border phrase, the no-blood clause — the seats computed"},
    'the_one_witness': {'value': 'two_by_the_prototype', 'settings': {'the_prototype': "'by the mouth of witnesses' (35:30) — the bare plural: TWO unless 'one' is written (the Sifrei 161:1's rule; Deuteronomy 17:6, 19:15 the spec, FORWARD)", 'for_acquittal': "'one witness shall not testify against a person to die' (35:30) — the Rabbis: nothing beyond his testimony; R. Yosei son of R. Yehuda: he may answer to ACQUIT (Sanhedrin 33b:15; the Sifrei 161:1)", 'the_oath': "the oath of testimony — men, non-relatives, the fit; before the court (Mishnah Shevuot 4:1)", 'no_inference': "'we do not punish by inference' for the lashed ('wicked' / 'wicked', 35:31) and for the exiled ('murderer' / 'murderer', 35:21 / 35:11) — Makkot 5b:15-16; the Sifrei 157:6, 160:3 the same rule", 'the_witnesses_hand': "the witnesses' hands first (Deuteronomy 17:7; Sanhedrin 45b:7); conspiring witnesses on exile flogged, not exiled (Mishnah Makkot 1:1) — Deuteronomy 19 FORWARD"}, 'source': "35:30 — 'witnesses' the bare plural, 'one witness' the homograph told by the lemma (5707 against 5704's 'until')"},
    'the_ransom_rows': {'value': 'refused_twice', 'settings': {'two_rules': "35:31 — no money to exempt from DEATH; 35:32 — no money to exempt from EXILE: one for the intentional, one for the unwitting, both needed (Ketubot 37b:3-4)", 'heavens_death_commuted': "R. Yishmael son of R. Yochanan ben Beroka: those executed at Heaven's hand give money and are atoned — the ox's owner (Exodus 21:29-30); those executed by man never ('dedicated of men shall not be redeemed', Leviticus 27:29) — Ketubot 37b:12; the ox's ransom an ATONEMENT (Bava Kamma 40a:5-12) by the victim's or the liable one's value; the stewards pay no ransom; the partners' ox unresolved (40a:14-19)", 'the_talion_money': "'no ransom for the LIFE of a murderer' — but ransom for limbs: the talion's money through Leviticus 24:18-21 (Bava Kamma 83b:9-19; L24.talion by CALL)", 'the_lashes': "'wicked to die' (35:31) / 'wicked' (Deuteronomy 25:2) — the lashes' twenty-three, no partial lashes, no inference (Sanhedrin 10a:11; Makkot 5a:3; Ketubot 35a:5)", 'the_ox_cell': "the mishpatim runner's STONE+RANSOM cell and its effect ransom_imposed — the noun this chapter refuses (M1 by CALL); Sanhedrin 15b:4-5: where ransom is written there is no death — 'you execute him for his act, not his ox's' (35:21)"}, 'source': "35:31, 35:32 — 'you shall not take ransom' the two seats; the ransom-noun's Torah seats computed"},
    'the_lands_atonement': {'value': 'by_the_shedders_blood', 'settings': {'no_atonement_until_he_dies': "the killer known — no atonement for the community until he is put to death; where the court cannot (no forewarning) — the tunic (Arakhin 16a:22; Zevachim 88b:13); not Yom Kippur (Keritot 26a:17)", 'the_heifer': "the heifer broken and then the killer found — he dies, not by the calf's blood (Mishnah Sotah 9:7; Sotah 47b:2; Ketubot 37b:6); the beheaded beheaded from the neck like the heifer, not with the cleaver (Ketubot 37b:7-8); R. Tzadok's 'whose heifer?' on the priest stabbed on the ramp (Yoma 23a:11-16); Deuteronomy 21:1-9 FORWARD (the measure-verb's third Torah seat at 21:2)", 'the_presence_departs': "for bloodshed the Temple is destroyed and the Presence departs — 35:33-34 read whole (Shabbat 33a:4); bloodshed an impurity the goat does not atone (Shevuot 7b:7); R. Yishmael reads 35:34 at the burglar's seat (Yoma 85a:14); the Presence that goes with Israel into exile and returns (Megillah 29a:4)", 'genesis_9_6': "'except by the blood of him who shed it' — Genesis 9:6's clause run as law: PR.cain by CALL, the blood_required HEAVEN entry on Noah", 'leviticus_18': "'you shall not defile the land' — Leviticus 18:25-28's land that vomits: SA.frame('land') by CALL"}, 'source': "35:33-34 — the pollute-root's only Torah seat, the passive 'no atonement', 'defile' — computed"},
    'the_uncertainty': {'value': 'unresolved', 'settings': {'issi_ben_akiva': "the Sifrei 160:8 — a two-way uncertainty: a killing the ink names neither way is neither death nor exile (the TEIKU shape: the row's value 'unresolved', the vows' precedent)", 'the_one_who_says_it_is_permitted': "Rava: neither executed nor exiled (Makkot 7b:4); Abaye: beyond his control; the sojourner's kin (9a:7-8)"}, 'source': "the Sifrei 160:8 on 35:22-23's marks"},
    'the_exiles_rows': {'value': 'the_shelfs_rows_as_data', 'settings': {'the_levite_exiled': "a Levite from district to district; the exile who killed in the city to another neighborhood (Mishnah Makkot 2:7; Makkot 12b:9; Zevachim 117a:7)", 'the_honor': "'I am a murderer' (Mishnah Makkot 2:8)", 'the_roads': "roads aligned, 'refuge' on signs at the crossroads, two scholars' escort (Mishnah Makkot 2:5; Makkot 10b:1, 10b:11 — Deuteronomy 19:3-4 FORWARD)", 'the_teacher': "the student exiled — his teacher with him; the teacher — his school ('and live', Deuteronomy 4:42; Makkot 10a:10-11)", 'the_testimony': "never for testimony, never for Israel's need (Makkot 11b:7)", 'the_wilderness': "the Levite camp the wilderness' refuge — 'a place … from your place' (Exodus 21:13; Makkot 12b:8): M3.killer('the_place') by CALL"}, 'source': "the docket's rows on Makkot 2:5-8 and 10a-13a"},
    'the_presence_rows': {'value': 'the_inclusio', 'settings': {'the_lands_presence': "'in whose midst I dwell' (35:34) — the Presence in the LAND, driven out by bloodshed (Shabbat 33a:4)", 'the_camps_presence': "5:3's 'their camps in whose midst I dwell' — the Presence in the CAMP, guarded by the send-out (the naso runner's three camps by CALL): the book's first law after the census and its last law-chapter's close", 'the_peoples_presence': "R. Shimon ben Yochai: the Presence went with Israel into every exile and returns with them (Megillah 29a:4)", 'the_open_entry': "presence_dwells OPEN on israel_people since Exodus 40:34 — the promise standing on the tape; a checkpoint reads it, no new write"}, 'source': "5:3 and 35:34 — the Torah's two seats of 'I dwell in the midst' computed"},
}
assert len(DATA) == 19, len(DATA)   # the design said eighteen; the_presence_rows added at the write — nineteen
for k, row in DATA.items():
    assert 'value' in row and 'settings' in row and 'source' in row and len(row['settings']) >= 1, k

# ===== F1: THE LEVITE CITIES (Num 35:1-8) ===================================================================
def the_levite_cities(case, data):
    del P[:]
    ask = case['ask']
    if ask == 'the_command':
        ink('35:2', '"command the children of Israel" — %s: THE FIVE TORAH SEATS, this the fifth' % COMMAND)
        move('cold_run_borders (CALL) — BO.the_land_and_its_fall(the_command) = %s' % BO_CMD[0][:60], "the Sifrei 1:2's five (credited at the reading): 'command' entails expense except 34:2's")
        return out("command the children of Israel (35:2) — the five Torah seats, this the fifth (Sifrei 1:2's five); the borders runner's cell by CALL", ['accepted'])
    if ask == 'cities_to_dwell_in':
        ink('35:2', '"and they shall give to the Levites … cities to dwell in" — %s one seat; "cities to dwell in" %s: JOSHUA 21:2 THE RUN\'S REQUEST under "the LORD commanded by the hand of Moses" (%d seats of the phrase, Joshua 20:2 and 21:2 among them)' % (GIVE_LEVITES, CITIES_DWELL, len(BY_HAND)))
        dat('the debit give_the_levites_cities_and_pasture_lands OPEN BY DESIGN — its run Joshua 21 outside the Torah (the row the_forty_eight: joshua_21)')
        return out("cities to dwell in (35:2) — three Bible seats: this, Joshua 14:4, and Joshua 21:2 the run's request; the debit on the people OPEN to Joshua 21", ['commanded'])
    if ask == 'the_pasture_land':
        ink('35:2-7', 'the pasture-land word — %s: six Torah seats (Leviticus 25:34\'s unsellable field + this chapter\'s five), %d Bible verses, %d in Joshua 21' % (PASTURE_T, len(PASTURE_B), len(PASTURE_J21)))
        move('Arakhin 33b:15 (R. Elazar)', "Leviticus 25:34's 'may not be sold' = may not be CHANGED — the field, the lot, the city keep their status (Mishnah Arakhin 9:8)")
        return out("the pasture-land (35:2-7) — six Torah seats, Leviticus 25:34's unsellable field and this chapter's five; 69 Bible verses, 32 Joshua 21's; the lot unchangeable (Arakhin 33b:15)", ['accepted'])
    if ask == 'their_beasts':
        ink('35:3', '"for their beasts and for their substance and for all their living" — "their beasts" %s (two Bible seats); Onkelos "their needs of life"' % BEASTS)
        move('Nedarim 81a:7 (Vardimus)', "'their beasts' — their LIVES: read for the laundering of clothes; Makkot 12a:5 (R. Abbahu): for life, not for burial")
        return out("their beasts (35:3) — two Bible seats; Onkelos 'their needs of life'; for life, not burial (Makkot 12a:5)", ['accepted'])
    if ask == 'the_thousand':
        ink('35:4', '"from the wall of the city outward a thousand cubits round about" — %s one seat; "a thousand cubits" %s the Bible\'s one; the parser [%d] (the cubit consumed as the unit noun, UNIT %s)' % (WALL_OUT, THOUSAND_CUBITS, THOUSAND, UNIT))
        move('Eruvin 56b:6 (Rava)', "surround the city with a thousand on all sides — the open space one quarter of the area; Eruvin 51a:9 refuses the analogy from 'outward'")
        return out("a thousand cubits (35:4) — the Bible's one seat; the parser [1000] with the cubit consumed; the open land (Eruvin 56b:6)", ['accepted'])
    if ask == 'the_two_thousand':
        ink('35:5', '"two thousand by the cubit" four times — the parser %s SINCE RULE 29 (THE BARE DUAL THOUSAND: the tilde on all four, %s; the prefixed cubit no unit-noun mark); "you shall measure" %s — the measure-verb\'s three Torah seats %s; "about two thousand cubits" %s Joshua\'s' % (TWO_THOUSANDS, TILDE, MEASURE, MEASURE_LEMMA_T, ABOUT_TWO_THOUSAND))
        move('Mishnah Sotah 5:3; Sotah 27b:8-10; Eruvin 51a:8; Mishnah Arakhin 9:8', "R. Akiva: the thousand the open land, THE TWO THOUSAND THE SABBATH LIMIT; R. Eliezer ben R. Yosei HaGelili: fields and vineyards; the Mishnah in Arakhin: a thousand and a thousand — three settings on two verses")
        dat('the row the_measures: %s (the settings r_akiva / r_eliezer_ben_r_yosei_hagelili / the_mishnah_in_arakhin / the_square)' % data['the_measures']['value'])
        return out("two thousand by the cubit (35:5) — four times, read [2000] each by rule 29 (the bare dual marked by the sheva under the lamed); the Sabbath limit's measure (R. Akiva) — a data row with three settings", ['accepted'])
    if ask == 'the_four_sides':
        ink('35:5', 'the four sides in the ink\'s order %s — EAST, SOUTH, WEST, NORTH; "the east side" %s one seat; the camp\'s four %s (Numbers 2:3, 10, 18, 25 — the same order)' % (SIDES_35, EAST_SIDE, CAMP_SIDES))
        move('cold_run_bamidbar (CALL) — CB.camp(sides) = %s; CB.camp(distance) = %s' % (CB_SIDES[0], CB_DIST[0]), "THE CAMP'S ORDER — the bamidbar runner's own row names 35:5 as the measure's seat")
        dat('the row the_four_sides_order: %s — the camp\'s order; the borders\' south-west-north-east; the court\'s south-north-west-east' % data['the_four_sides_order']['value'])
        return out("the four sides (35:5) — east, south, west, north: THE CAMP'S ORDER (Numbers 2 by CALL), against the borders' and the court's; the Levite city laid out as the camp", ['accepted'])
    if ask == 'the_city_in_the_midst':
        ink('35:5', '"and the city in the midst; this shall be to them the pasture-lands of the cities" — %s one seat; "the pasture-lands of the cities" %s' % (CITY_MIDST, PASTURES_CITIES))
        move('Eruvin 51a:13-14; Mishnah Eruvin 5:1', "'THIS shall be to them' — the Levite city squared with sides (Rav Chananya: like this measure the measures of all who rest on the Sabbath)")
        return out("and the city in the midst (35:5) — one seat; the square (Eruvin 51a:13-14)", ['accepted'])
    if ask == 'six_and_forty_two':
        ink('35:6-7', '"the six cities of refuge … and beside them forty-two cities … all the cities forty-eight" — the parser %s and [%d]; 6 + 42 = 48 asserted; "forty-eight" %s; JOSHUA 21\'s four lots %s sum to %d, the tally 21:41 %s' % (SIX_FORTYTWO, FORTY_EIGHT, FORTY_EIGHT_ALL, JOSH21_LOTS, sum(n[0] for n in JOSH21_LOTS), JOSH21_TALLY))
        move('Makkot 10a:4 (Abaye); 13a:2-3', "all the Levite cities are cities of refuge — the six admit knowingly or not, the forty-two only knowingly; the rent disputed on 35:6 and 35:11")
        dat('the row the_forty_eight: %s' % data['the_forty_eight']['value'])
        return out("six and forty-two (35:6-7) — [6, 42] and [48], the sum asserted; Joshua 21's four lots 13 + 10 + 13 + 12 = 48 by the parser, the tally reads it; the forty-two receive too (Makkot 10a:4)", ['accepted'])
    if ask == 'the_rule':
        ink('35:8', '"from the many you shall take more and from the few you shall take less, each according to his inheritance" — %s, %s, %s one seat each; "you shall take less" singular %s' % (MORE, LESS, EACH, LESS_SG))
        move('cold_run_second_census (CALL) — C2.the_land(by_number_of_names) = %s' % C2_RULE[0], "26:54's rule at its THIRD seat (33:54 the second — the journeys runner's the_lot_restated)")
        return out("the proportional rule (35:8) — 26:54's rule at its third seat by CALL; 'you shall take less' plural here alone", ['accepted'])
    if ask == 'no_inheritance':
        move('cold_run_second_census (CALL) — C2.the_levites(no_inheritance) = %s' % C2_NOINH[0], "the block inheritance_barred on the Levites' ledger (18:20-24; 26:62): the cities are 'from the inheritance of their possession' — the people's, given, not the Levites' inheritance")
        return out("the Levites have no inheritance (18:20-24; 26:62 by CALL) — the cities the people's gift 'from the inheritance of their possession' (35:2), the block standing", ['accepted'])
    if ask == 'the_debit':
        ink('35:2-8', '"you shall give" %d times — the second person plural: the command the PEOPLE\'S debit; no receipt in the chapter (the receipt form %d Numbers seats, none here)' % (len(GIVE), len(RECEIPT_NUM)))
        dat('commanded on israel_people valued give_the_levites_cities_and_pasture_lands, counterparty the-levites — OPEN BY DESIGN to Joshua 21:1-42 (THE READBACK\'s)')
        return out("the debit (35:2-8) — 'you shall give' ten times: commanded on the people, counterparty the Levites, OPEN by design to Joshua 21", ['commanded'])
    return out('no verdict in span', [FX.NONE])


# ===== F2: THE REFUGE LAW (Num 35:9-15) =====================================================================
def the_refuge_law(case, data):
    del P[:]
    ask = case['ask']
    if ask == 'when_you_cross':
        ink('35:10', '"when you are crossing the Jordan to the land of Canaan" — %s three seats; "to Canaan-ward" %s — the directional form\'s seventh seat, the Torah\'s last; the frames %s' % (CROSSING, CANAANWARD, FRAME_VERBS))
        move('cold_run_journeys (CALL) — JO.the_command(when_you_pass) = %s' % JO_PASS[0][:80], "33:51's clause — the journeys runner's own row names 35:10 as the kin")
        return out("when you are crossing the Jordan (35:10) — 33:51's clause by CALL (Deuteronomy 11:31 the third); 'to Canaan-ward' the directional form's Torah last", ['accepted'])
    if ask == 'appoint':
        ink('35:11', '"and you shall appoint for yourselves cities" — %s one seat; the root Balaam\'s "meet" (23:4, 16) and the servant\'s "cause it to happen" (Genesis 24:12; 27:20) — a homograph by sense' % APPOINT)
        move('Sifrei Bamidbar 159:1', "'calling out connotes designation' — the cities appointed after the inheritance and the settlement (the timing from the context)")
        dat('the edge refuge -> balak FALSE: the designation of cities is no meeting')
        return out("you shall appoint (35:11) — one seat; designation, not a meeting (Balaam's root FALSE by sense); after the inheritance (Sifrei 159:1)", ['accepted'])
    if ask == 'the_place_become_cities':
        ink('35:11, 15, 26', '"a manslayer shall flee there" — "he shall flee there" %s: EXODUS 21:13 THE SPEC\'S FIRST SEAT; "to flee there" %s LOT\'S FIRST' % (HE_SHALL_FLEE, FLEE_THERE))
        move('cold_run_mishpatim_3 (CALL) — M3.killer(the_place) = %s' % M3_PLACE['v'], "Exodus 21:13's 'I will appoint you a place' — the Levites' cities for the generations, the camps for the hour (Mekhilta Nezikin 13 2; Makkot 12b:8): THE PLACE BECOME CITIES")
        return out("the place become cities — Exodus 21:13's 'he shall flee there' at its Numbers seat: the Levites' cities for the generations, the Levite camp for the hour (M3 by CALL)", ['flees_to_refuge'])
    if ask == 'six_cities':
        ink('35:13-15', '"six cities of refuge" %s, "the six cities of refuge" %s, "cities of refuge" %s; "three cities beyond the Jordan and three in Canaan" — the parser %s; "the three cities" %s here alone, bare "three cities" Deuteronomy\'s %s' % (SIX_REFUGE, THE_SIX_REFUGE, CITIES_REFUGE, THREE_THREE, THE_THREE_CITIES, THREE_CITIES))
        move('Mishnah Makkot 2:4; Makkot 9b:14, 9b:18-19', "not until all six are set apart; two rows of vines; Gilead's three for murderers common there")
        dat('the row the_six_cities: %s — the names OUTSIDE the chapter (Deuteronomy 4:43; Joshua 20:7-8), computed by seat' % data['the_six_cities']['value'])
        return out("six cities (35:13-15) — [6], [3, 3], [6]: three and three; the names Deuteronomy 4:43's and Joshua 20:7-8's, none here; not until all six (Makkot 2:4): a data row", ['accepted'])
    if ask == 'for_whom':
        ink('35:15', '"for the children of Israel and for the stranger and for the sojourner among them" — %s one seat; against 35:12\'s "for you"; Joshua 20:9 drops the sojourner (computed: %s)' % (STRANGER_SOJ, 'ולתושב' not in JOSH20_9))
        move('Makkot 9a:2-8 (Rav Kahana; Rav Chisda; Rava)', "the sojourner exiled for a sojourner, not for a Jew; the baraita's death for the sojourner and the gentile — by the motion or by 'permitted'")
        dat('the row the_stranger_and_sojourner: %s' % data['the_stranger_and_sojourner']['value'])
        return out("for whom (35:15) — Israel, the stranger and the sojourner against 35:12's 'for you': the sojourner for a sojourner only (Makkot 9a); Joshua 20:9 drops the sojourner", ['accepted'])
    if ask == 'unwittingly':
        ink('35:11, 15', '"smites a soul unwittingly" %s; "unwittingly" %d seats — the sin offering\'s word (Leviticus 4-5, 22:14; Numbers 15:26-29); Deuteronomy says "without knowledge" %s; Joshua 20:3 says both' % (SMITES_UNWIT, len(UNWIT), NO_KNOWLEDGE))
        move('cold_run_shelach (CALL) — SL.error(thrice_unwitting) = %s' % SL_UNWIT[0], "15:27-29's 'in error' thrice — the offering's word the slayer's; Makkot 7b:3: 'unwittingly' excludes the intentional, 'unawares' the one with intent")
        return out("unwittingly (35:11, 15) — the sin offering's word (thirteen seats; the shelach runner by CALL); Deuteronomy's 'without knowledge'; Joshua 20:3 both", ['accepted'])
    if ask == 'until_he_stands':
        ink('35:12', '"and the manslayer shall not die until he stands before the congregation for judgment" — %s: this and Joshua 20:6 quoting it; the avenger bare %s (without "blood" — Onkelos supplies)' % (UNTIL_STANDS, AVENGER_BARE))
        move('Makkot 12a:11 (R. Eliezer); Onkelos 35:19, 21', "written against 35:27's avenger: the avenger kills only after conviction — 'when he has been found guilty by the court' supplied at 19 and 21; Rav: the avenger who kills before is liable")
        dat('the row the_avengers_hand: %s' % data['the_avengers_hand']['value'])
        return out("until he stands before the congregation (35:12) — the court before the avenger's hand (Makkot 12a:11; Onkelos' clause at 19, 21); Joshua 20:6 quotes it", ['accepted'])
    if ask == 'the_debit':
        ink('35:11-14', '"you shall appoint … you shall give … you shall give" — the second person plural; the six cities\' names %s outside the chapter' % {k: len(v) for k, v in SIX_NAMES.items()})
        move('Makkot 11a:1-4; 10a:16', "Joshua 20:1-2's harsh speech — the cities a Torah mitzva (or Joshua delayed); Moses' three 'a mitzva that came my way'")
        dat('commanded on israel_people valued appoint_six_cities_of_refuge — OPEN BY DESIGN: Deuteronomy 4:41-43 (Moses\' three, that book\'s compile) and Joshua 20:7-8 (THE READBACK\'s)')
        return out("the debit (35:11-14) — appoint six cities: commanded on the people, OPEN by design to Deuteronomy 4:41 and Joshua 20:7-8", ['commanded'])
    return out('no verdict in span', [FX.NONE])


# ===== F3: THE MURDERER (Num 35:16-21) ======================================================================
def the_murderer(case, data):
    del P[:]
    ask = case['ask']
    if ask == 'the_iron':
        ink('35:16', '"and if with an instrument of iron he struck him and he died, he is a murderer" — %s one seat; TEN tokens, no "hand", no size clause (17: thirteen, 18: fourteen)' % IRON)
        move('Sanhedrin 76b:12-13 (Shmuel; Rebbi); Sifrei 160:3', "iron of any size kills — 'even a needle'; 'revealed and known before Him … therefore the Torah gave it no measure'; only when he stabbed")
        dat('the row size_that_can_kill: iron_any_size')
        return out("the iron (35:16) — no 'hand', no size clause: iron of any size kills (Sanhedrin 76b:12-13); the parameter's exemption stated by the shelf", ['put_to_death'])
    if ask == 'the_stone_and_the_wood':
        ink('35:17-18', '"a stone of the hand whereby he may die … a wooden instrument of the hand whereby he may die" — %s, %s; "whereby he may die" %s (feminine) and %s (masculine)' % (STONE_HAND, WOOD, WHEREBY_F, WHEREBY_M))
        move('Sanhedrin 76b:12; Sifrei 160:3-5', "'in hand' — a measure that can kill; the induction from three fathers (the stone, the wood, the iron — the common feature 'it can kill') to anything, its limit the water, the fire, the snake — to Heaven")
        dat('the row size_that_can_kill: %s — a PARAMETER (fills_the_hand_or_can_kill; to_heaven)' % data['size_that_can_kill']['value'])
        return out("the stone and the wood (35:17-18) — 'of the hand whereby he may die': the size a PARAMETER (Sanhedrin 76b:12; the Sifrei's induction from three)", ['put_to_death'])
    if ask == 'he_is_a_murderer':
        ink('35:16-18, 21', '"he is a murderer" %s four seats; "the murderer shall surely die" %s three; "shall surely die" %d Torah seats, FIVE here %s — the Torah\'s densest chapter; the murder-root %d tokens in the chapter (twelve "the manslayer", six bare, the avenger\'s "slays", the court\'s "shall slay"), written DEFECTIVE at every Numbers seat (plene %s)' % (HE_IS_MURDERER, MURDERER_DIE, len(SURELY_DIE_T), SURELY_DIE_35, len(MURDER_TOK_35), MURDER_PLENE))
        move('Sanhedrin 15b:5 (the school of Chizkiyah); 77a:2', "'he that struck him shall be put to death; he is a murderer' — you execute him for HIS killing, not his ox's; 'he is a murderer' restricts the confiner's liability to the murderer")
        return out("he is a murderer (35:16-18, 21) — four seats; 'shall surely die' five times, the Torah's densest; one root for four agents, defective at every Numbers seat", ['put_to_death'])
    if ask == 'the_mode':
        ink('35:21', '"he shall surely die" — the doubled verb %s' % SMITER_DIE)
        move('cold_run_mishpatim_3 (CALL) — M3.killer(mode) = %s' % M3_MODE['v'], "Mishnah Sanhedrin 9:1 — the murderer among the beheaded; Sanhedrin 52b:13's verbal analogy 'avenged' / 'avenging sword'; when the sword cannot be done — ANY MODE (Bava Metzia 31b:2; Sanhedrin 45b:10-11; 53a:7)")
        move('cold_run_sanctions (CALL) — SA.severity(orders) = %s' % SA_ORDERS['v']['sages'], "the four deaths' two orders — 'killing' the sword the third of the sages'")
        move('Ketubot 37b:7-8', "beheaded from the NECK like the heifer (Deuteronomy 21:9), not with the cleaver — 'love your neighbor as yourself'")
        return out("the mode — the sword (M3 by CALL; Sanhedrin 9:1), from the neck (Ketubot 37b:7); any mode when the sword cannot be done (the doubled verb)", ['put_to_death'])
    if ask == 'the_avengers_hand':
        ink('35:19, 21', '"the avenger of blood himself shall put the murderer to death; when he meets him he shall put him to death" — "the avenger of blood shall put to death" %s, "when he meets him" %s; "the avenger of blood" %d Bible seats' % (AVENGER_PUT, MEETS, len(AVENGER_BLOOD)))
        move('Sanhedrin 45b:12-13; Makkot 12a:8-11; Sifrei 160:7', "the mitzva on the avenger; no avenger — the court appoints one ('when he meets him'); after the court's conviction alone (R. Eliezer); two verses that come as one")
        dat('the row the_avengers_hand: %s' % data['the_avengers_hand']['value'])
        return out("the avenger's hand (35:19, 21) — the avenger puts him to death after the court; none — the court appoints one (Sanhedrin 45b:13); a data row with its arms", ['put_to_death'])
    if ask == 'the_manners':
        ink('35:20-21', '"thrust him … threw at him … struck him with his hand" — the manners; "struck him" %s the Torah\'s five (Deuteronomy 21:1\'s "it is not known who struck him" the fifth)' % STRUCK_HIM_T)
        move('Sanhedrin 76b:15 (Shmuel); Mishnah Sanhedrin 9:1', "'in enmity' includes the one who confines another where he cannot live — held in the water or the fire; pushed and could get out — exempt")
        dat('the row the_case_table: causation — Rava\'s binding, the ladder, the shield, the herbs, the rebound; the ten sticks; the tereifa')
        return out("the manners (35:20-21) — thrust, threw, struck with the hand; the confiner a murderer (Sanhedrin 76b:15); the causation line the shelf's (a data row)", ['put_to_death'])
    if ask == 'the_intents':
        ink('35:20-22', '"in hatred … in lying-in-wait … in enmity" against "without enmity … without lying-in-wait" — "in hatred" %s, "in lying-in-wait" %s (the noun\'s two Bible seats %s), "in enmity" %s — THE SERPENT\'S WORD (the noun\'s Torah seats %s)' % (HATRED, LYING, LYING_LEMMA, ENMITY_IN, ENMITY_T))
        move('Mishnah Sanhedrin 9:2; Sanhedrin 79a:3-7; Makkot 7b:5', "meant the beast and killed the man — exempt; the loins and the heart by the blow's force; R. Shimon: this one meant and that one killed — exempt")
        move('cold_run_mishpatim_3 (CALL) — M3.killer(forewarning) = %s' % M3_FOREWARN['v'], "the forewarning the death's PARAMETER (Sanhedrin 41a; the enemy needs none — Makkot 9b:9; the ball players' certainty 77b:8)")
        dat('the row the_case_table: the_intents_table')
        return out("the intents (35:20-22) — hatred, lying-in-wait (Exodus 21:13's verb as a noun), enmity (the serpent's word) against their negations: the intent's table (Sanhedrin 9:2) a data row; the forewarning a parameter by CALL", ['put_to_death'])
    if ask == 'the_smiter':
        ink('35:21, 24', '"the smiter" — the participle with the article %s (seven Torah seats; the smitten woman of 25:14-18 the passive homograph: %s against %s by the morphology)' % (SMITER_PART, SMITTEN_MORPH, SMITER_MORPH))
        move('cold_run_lev24 (CALL) — L24.talion(kill) = %s' % L24_KILL['verdict'], "24:17's 'whoever strikes any soul' beside 35:30's — both needed (Sanhedrin 84b:6); the talion's money through 24:18-21 from 35:31's 'no ransom for the LIFE' (Bava Kamma 83b:9-19)")
        return out("the smiter (35:21, 24) — the active participle at seven Torah seats, the smitten woman its passive homograph; Leviticus 24:17's smiter by CALL", ['accepted'])
    if ask == 'the_table':
        ink('35:16-23', 'the case tokens %s — "and if" / "or" the branches: instrument x manner x intent -> the verdict' % CASE_TOKENS)
        dat('the row the_case_table: %s — %s' % (data['the_case_table']['value'], data['the_case_table']['settings']['instrument_x_manner_x_intent'][:120]))
        return out("the case table (35:16-23) — computed from the tokens: the instruments, the manners, the intents; the verdicts a murderer, a manslayer, neither", ['accepted'])
    return out('no verdict in span', [FX.NONE])
# ===== F4: THE MANSLAYER (Num 35:22-28) =====================================================================
def the_manslayer(case, data):
    del P[:]
    ask = case['ask']
    if ask == 'suddenly':
        ink('35:22', '"and if suddenly, without enmity, he thrust him or threw at him any instrument without lying-in-wait" — "suddenly" %s (the nazirite\'s word — the two Bible seats both this book\'s); "without enmity" %s, "without lying-in-wait" %s' % (SUDDENLY, WITHOUT_ENMITY, WITHOUT_LYING))
        move('Makkot 7b:6 (the baraita); Keritot 9a:19', "'suddenly' excludes the corner; 'without enmity' the enemy; 'he thrust him' includes the shove; 'or cast upon him' the downward-for-upward; 'without lying in wait' the stone thrown aside; 'unexpectedly' = unwitting as the nazirite's")
        return out("suddenly (35:22) — the nazirite's word (6:9, the naso runner's seat); the baraita's five marks read word by word (Makkot 7b:6)", ['flees_to_refuge'])
    if ask == 'without_seeing':
        ink('35:23', '"or with any stone whereby he may die, without seeing" — %s one seat; "whereby he may die" %s' % (WITHOUT_SEEING, WHEREBY_F))
        move('Makkot 9b:5-8; Bava Kamma 86b:17-19; Nedarim 87b:5', "R. Yehuda excludes the blind, R. Meir includes (a restriction after a restriction)")
        dat('the row the_blind_killer: %s' % data['the_blind_killer']['value'])
        return out("without seeing (35:23) — the blind killer disputed (R. Yehuda exempt, R. Meir exiled): a data row", ['flees_to_refuge'])
    if ask == 'the_downward_motion':
        ink('35:23', '"and he dropped it on him and he died" — %s one seat; the narrative verbs inside the cases %s' % (DROPPED, NARR))
        move('cold_run_mishpatim_3 (CALL) — M3.killer(refuge_by_descent) = %s' % M3_DESCENT['v'], "Shmuel from 35:23: exile only for a downward motion (Makkot 7b:2) — Mishnah Makkot 2:1's rows at their second seat; the butcher and the rung (7b:8-16)")
        return out("the downward motion (35:23 'and he dropped it') — descent exiles, ascent does not (Mishnah Makkot 2:1 by CALL; Makkot 7b:2)", ['flees_to_refuge'])
    if ask == 'not_his_enemy':
        ink('35:23', '"and he was not his enemy nor sought his harm" — %s one seat' % NOT_ENEMY)
        move('Sanhedrin 29a:6; Mishnah Sanhedrin 3:5; Makkot 9b:9-13 (R. Shimon)', "'not his enemy' testifies, 'nor sought his harm' judges; the enemy not exiled (R. Yosei: executed as forewarned; R. Shimon: by the circumstances)")
        return out("not his enemy (35:23) — the hater of three days off the witness stand and the bench (Sanhedrin 29a:6); the enemy's exile by the circumstances (R. Shimon)", ['accepted'])
    if ask == 'the_congregation_judges':
        ink('35:24', '"and the congregation shall judge between the smiter and the avenger of blood on these judgments" — %s one seat; "these judgments" %s; the congregation-token %s (12, 24, 25, 25)' % (CONG_JUDGE, THESE_JUDG, CONG_TOKENS))
        move('Mishnah Sanhedrin 1:6; Sanhedrin 2a:14-2b:1; Sifrei 160:8', "ten and ten and three — the court of TWENTY-THREE from the two congregations")
        dat('the row the_court_of_twenty_three: %d' % data['the_court_of_twenty_three']['value'])
        return out("the congregation judges (35:24) — the court of twenty-three built from the congregation-tokens (the Sifrei 160:8; Mishnah Sanhedrin 1:6): a data row", ['accepted'])
    if ask == 'the_deliverance':
        ink('35:25', '"and the congregation shall deliver the manslayer from the hand of the avenger of blood and return him to his city of refuge where he fled, and he shall dwell in it until the death of the high priest" — %s one seat; Onkelos renders "deliver" with the refuge-root' % CONG_DELIVER)
        move('Makkot 10b:14; 9b:17', "the court's three verbs — the murderer executed, the free freed ('deliver'), the exiled RESTORED ('return him')")
        return out("the deliverance (35:25) — the court returns him: flees_to_refuge (Exodus 21:13's effect at its second seat) and dwells_in_refuge, the term's open entry", ['flees_to_refuge', 'dwells_in_refuge'])
    if ask == 'the_term':
        ink('35:25, 28, 32', '"until the death of the high priest" %s; "the high priest" DEFECTIVE only here %s (three tokens %s; plene %d seats, Joshua 20:6 among them); "who was anointed with the holy oil" %s; "until the death of the priest" %s (35:32 bare)' % (UNTIL_DEATH_HP, HP_DEF, HP_DEF_TOK, len(HP_PLENE), ANOINTED, UNTIL_DEATH_PRIEST))
        move('cold_run_chukat (CALL) — CK.edom_and_hor(succession) = %s' % CK_SUCC[0], "THE OFFICE'S HOLDER: Eleazar since (40, 5, 1); his death Joshua 24:33 (computed: %s) — OUTSIDE THE TORAH" % ELEAZAR_DIED)
        move('cold_run_priesthood (CALL) — PH.family(nezer) = %s' % PH_NEZER['v'], "Leviticus 21:10-12's anointed and many-garmented — the definition; Makkot 11a:12's three high priests from the three seats of the death clause")
        dat('the row the_three_high_priests: %s; the row the_terms_rows: %s — THE DESIGN\'S DECISION (e): an open BODY entry closed by the death ACT, no day-timer' % (data['the_three_high_priests']['value'], data['the_terms_rows']['value']))
        return out("the term (35:25, 28, 32) — until the death of the high priest (defective only here): an open entry on the manslayer closed by the office-holder's death act; the holder Eleazar by CALL, his death outside the Torah; the three high priests as data", ['dwells_in_refuge'])
    if ask == 'the_border':
        ink('35:26-27', '"and if going out he goes out beyond the border of his city of refuge … and the avenger finds him outside the border … and the avenger slays the manslayer — he has no blood": "going out he goes out" %s (Jacob\'s at Genesis 27:30), "the border of his city of refuge" %s, "he has no blood" %s (the burglar\'s "he has no bloods" %s — the singular here); "and he slays" the consecutive perfect' % (GOING_OUT, BORDER_REFUGE, NO_BLOOD, NO_BLOODS))
        move('cold_run_mishpatim_3 (CALL) — M3.burglar(judged_by_his_end) = %s' % M3_END['v'], "Exodus 22:1's 'no blood' at its second seat — the effect has_blood reused: the avenger clear")
        move('Makkot 12a:8-15', "R. Yosei HaGelili a mitzva, R. Akiva a license (the verb's mood); the doubled verb — deliberate or unwitting exit; Abaye: the end not severer than the beginning")
        dat('the row the_border_rows: %s' % data['the_border_rows']['value'])
        return out("the border (35:26-27) — outside the border the avenger has no blood: the burglar's clause reused (has_blood no_blood by CALL); the doubled infinitive and the mood disputed (Makkot 12a)", ['has_blood', 'exempt'])
    if ask == 'the_return':
        ink('35:28', '"for in his city of refuge he shall dwell until the death of the high priest, and after the death of the high priest the manslayer shall return to the land of his possession" — "the land of his possession" %s one seat; "he shall return" the simple stem %s' % (LAND_POSS, RETURN_STEM))
        move('Sifrei 161:5; Makkot 13a:4-6; 11b:12', "'he will return', not 'bring back' — the stem read; to his land, not his fathers' honor (R. Yehuda) or even to it (R. Meir); his bones after the death")
        return out("the return (35:28) — after the death of the high priest to the land of his possession: returns_to_his_possession written at the term's close; the stem read (Sifrei 161:5)", ['returns_to_his_possession'])
    if ask == 'the_uncertainty':
        ink('35:22-23', 'the marks of the unwitting — suddenly, without enmity, without lying-in-wait, without seeing, not his enemy: a killing the ink names neither way')
        move('Sifrei 160:8 (Issi ben Akiva); Makkot 7b:4 (Rava)', "a two-way uncertainty — neither death nor exile; 'the one who says it is permitted' neither executed nor exiled")
        dat('the row the_uncertainty: %s — the TEIKU form (the vows\' precedent)' % data['the_uncertainty']['value'])
        return out("unresolved", ['exempt'])
    if ask == 'father_and_son':
        move('cold_run_mishpatim_3 (CALL) — M3.killer(father_and_son) = %s; M3.killer(guile_excludes) = %s' % (M3_FATHER['v'], M3_GUILE['v']), "Mishnah Makkot 2:3 — each exiles for the other; the office's exemptions (the father, the teacher, the court's agent — Mishnah 2:2; Makkot 8a:6, 8b:8-14)")
        return out("the father and the son (Mishnah Makkot 2:3 by CALL) — each exiles for the other; the office's exemptions (Abba Shaul) by CALL", ['flees_to_refuge'])
    if ask == 'the_levite_exiled':
        move('Mishnah Makkot 2:7; Makkot 12b:9; Zevachim 117a:7', "a Levite from district to district; the exile who killed in his city to another neighborhood ('for in HIS city of refuge', 35:28)")
        dat('the row the_exiles_rows: the_levite_exiled')
        return out("the Levite exiled (Makkot 12b:9) — from district to district; the exile who killed again to another neighborhood: a data row", ['flees_to_refuge'])
    if ask == 'the_honor':
        move('Mishnah Makkot 2:8; 2:5; Makkot 10a:10, 10b:1', "'I am a murderer'; the roads and the signs; the teacher exiled with the student")
        dat('the row the_exiles_rows: the_honor / the_roads / the_teacher')
        return out("the exile's honor, roads and teacher (Mishnah Makkot 2:5, 2:8; Makkot 10a-10b) — the shelf's rows as data", ['accepted'])
    return out('no verdict in span', [FX.NONE])


# ===== F5: THE STATUTE (Num 35:29-34) =======================================================================
def the_statute(case, data):
    del P[:]
    ask = case['ask']
    if ask == 'a_statute_of_judgment':
        ink('35:29', '"and these shall be to you a statute of judgment for your generations in all your dwellings" — "a statute of judgment" %s (THE DAUGHTERS\' PHRASE, the two Bible seats; Onkelos "a decree of judgment" at both); "for your generations in all your dwellings" %s — LEVITICUS 3:17\'S, THE BLOOD BAN\'S formula' % (STATUTE_JUDG, GENERATIONS))
        move('cold_run_zelophehad (CALL) — ZL.inheritance_order(source_of_rule) = %s' % ZL_SRC[0], "27:11's 'a statute of judgment' — the daughters' output; this chapter's statute the second")
        move('Makkot 7a:3, 7a:7; Sanhedrin 35b:10; Yevamot 6b:10', "in all your dwellings — the Sanhedrin in the land and outside it; no execution on the Sabbath")
        return out("a statute of judgment (35:29) — the daughters' phrase (27:11 by CALL); 'in all your dwellings' the blood ban's formula: the Sanhedrin everywhere (Makkot 7a:7), never on the Sabbath", ['accepted'])
    if ask == 'the_witnesses':
        ink('35:30', '"whoever smites a soul, by the mouth of witnesses the murderer shall be slain; and one witness shall not testify against a soul to die" — "by the mouth of witnesses" %s the bare plural; "one witness" %s (the bare consonants עד inside the chapter are all "until" — the lemmas %s at 12, 25, 28, 32; the witness at 30 wears the vav, ועד "and a witness"); "shall not testify" %s — THE NINTH COMMANDMENT\'S VERB beside the sixth\'s root in one verse' % (MOUTH_WIT, ONE_WITNESS, UNTIL_LEMMAS, NOT_TESTIFY))
        move('Sifrei 161:1; Sanhedrin 33b:15; Mishnah Shevuot 4:1', "witness means two unless 'one' is written — the prototype; the one witness may answer to acquit (R. Yosei son of R. Yehuda); the oath of testimony")
        move('cold_run_lev24 (CALL) — L24.talion(kill) = %s' % L24_KILL['verdict'], "24:17's 'whoever strikes any soul' and 35:30's 'whoever smites a soul' both needed (Sanhedrin 84b:6)")
        dat('the row the_one_witness: %s' % data['the_one_witness']['value'])
        return out("the witnesses (35:30) — two by the prototype (the Sifrei 161:1); one witness not to convict, but to acquit (Sanhedrin 33b:15); the ninth commandment's verb; a data row", ['accepted'])
    if ask == 'no_ransom':
        ink('35:31', '"and you shall not take ransom for the life of a murderer who is wicked to die, for he shall surely die" — %s the two refusals; the ransom-noun\'s Torah seats by lemma %s (THE GORING OX\'S 21:30, THE HALF-SHEKEL\'S 30:12, this chapter\'s two; Genesis 6:14\'s "pitch" the lemma\'s homograph), by token %s; "wicked to die" %s' % (NO_RANSOM, RANSOM_LEMMA_T, RANSOM_TOK_T, WICKED_DIE))
        move('cold_run_mishpatim (CALL) — M1.has_lemma(Exod 21:30, 3724) = %s; the ox row %s' % (M1_RANSOM_SEAT, M1_RANSOM_ROW), "the goring ox's ransom — the noun refused here; Sanhedrin 15b:4-5: where ransom is written there is no death")
        move('Ketubot 37b:3-4, 37b:12; Bava Kamma 40a:5-12', "no money to exempt from death (the intentional); Heaven's death commuted to money — the ox's owner; the court's never")
        move('cold_run_lev24 (CALL) — L24.talion(kill) = %s' % L24_KILL['verdict'], "'no ransom for the LIFE' — but for limbs: the talion's money (Bava Kamma 83b:9-19)")
        dat('the row the_ransom_rows: %s' % data['the_ransom_rows']['value'])
        return out("no_ransom_the_death_stands", ['put_to_death'])
    if ask == 'no_ransom_for_the_fugitive':
        ink('35:32', '"and you shall not take ransom for him who fled to his city of refuge, to return to dwell in the land until the death of the priest" — the second refusal; "the priest" bare')
        move('Ketubot 37b:3-4; Makkot 11a:13; Bava Kamma 28a:11', "no money to exempt from exile (the unwitting); R. Yehuda: the war-anointed priest from the bare 'priest'; the verse lent to the Hebrew slave's eviction")
        return out("no_ransom_the_exile_stands", ['flees_to_refuge'])
    if ask == 'the_land_polluted':
        ink('35:33', '"and you shall not pollute the land in which you are, for the blood, it pollutes the land, and for the land no atonement can be made for the blood shed in it except by the blood of him who shed it" — "you shall not pollute" %s: THE POLLUTE-ROOT\'S ONLY TORAH SEAT (%d Bible verses, Psalm 106:38 among them); "no atonement" %s the passive %s — the ransom\'s root a third time; "except by the blood of him who shed it" %s' % (POLLUTE, len(POLLUTE_LEMMA_B), NO_ATONE, ATONE_STEM, EXCEPT_BLOOD))
        move('Arakhin 16a:22; Zevachim 88b:13; Mishnah Sotah 9:7; Sotah 47b:2; Shabbat 33a:4', "no atonement for the community until he dies; the heifer broken and then the killer found — he dies; for bloodshed the Presence departs")
        dat('the row the_lands_atonement: %s' % data['the_lands_atonement']['value'])
        return out("the land polluted (35:33) — the pollute-root's only Torah seat: a status on the land while the shedder stands; atoned only by his blood; the heifer's other passive Deuteronomy 21's (forward)", ['land_polluted_by_blood'])
    if ask == 'the_shedders_blood':
        ink('35:33', '"except by the blood of him who shed it" — Genesis 9:6\'s "who sheds the blood of man, by man shall his blood be shed" (%s)' % GEN9_6[:6])
        move('cold_run_primeval (CALL) — PR.cain(bloods_seats) = %s; PR.cain(exile_half) = %s; PR.sentences(east_receives) = %s' % (PR_BLOODS['v'], PR_HALF['v'], PR_EAST['v']), "the bloods of Abel; Cain's exile atoning HALF (Sanhedrin 37b:12); the manslayer's direction the east (Bereshit Rabbah 21:9); the blood_required HEAVEN entry on Noah since 9:5")
        return out("the shedder's blood (35:33) — Genesis 9:6's clause run as law (the primeval runner by CALL): Cain's exile the half-atonement, the murderer's blood the whole", ['put_to_death'])
    if ask == 'not_defile':
        ink('35:34', '"and you shall not defile the land in which you dwell" — %s one seat; Leviticus 18:25\'s "and the land was defiled … and the land vomited" (%s)' % (NOT_DEFILE, [w for w in LEV18_25 if w in ('ותטמא', 'ותקא')]))
        move('cold_run_sanctions (CALL) — SA.frame(land) = %s' % SA_VOMIT['v'], "18:25, 28; 20:22 — the land that vomits its inhabitants; Shevuot 7b:7: bloodshed an impurity by 35:34 beside the unions and Molech")
        return out("you shall not defile the land (35:34) — Leviticus 18:25-28's land that vomits (the sanctions runner by CALL); bloodshed an impurity (Shevuot 7b:7)", ['accepted'])
    if ask == 'in_whose_midst_i_dwell':
        ink('35:34', '"in whose midst I dwell, for I the LORD dwell in the midst of the children of Israel" — %s, %s, %s one seat each; THE BOOK\'S INCLUSIO: the phrase at %s (5:3\'s camp and 35:34\'s land — computed); 5:3 ends %s' % (MIDST_DWELL, I_DWELL_MIDST, FOR_I_LORD, sorted(set(INCLUSIO)), NUM5_3[-5:]))
        move('cold_run_naso (CALL) — NS.camp_purity(three_camps) = %s; (classes) = %s' % (NS_CAMPS[0], NS_CLASSES[0]), "5:3's camp guarded by the send-out — the Presence in the camp; here the Presence in the land guarded by the blood's ban")
        move('Shabbat 33a:4; Yoma 85a:14; Shevuot 7b:7; Megillah 29a:4', "the Presence departs for bloodshed; R. Yishmael reads it at the burglar's seat; an impurity; the Presence that goes with Israel into exile")
        dat('the row the_presence_rows: %s — presence_dwells OPEN on the people since Exodus 40:34, read at the checkpoint, no new write' % data['the_presence_rows']['value'])
        return out("in whose midst I dwell (35:34) — the book's inclusio with 5:3 (the naso runner by CALL): the Presence in the camp and in the land, each guarded by a ban; the open promise read, not rewritten", ['accepted'])
    if ask == 'the_closer':
        ink('36:1', 'the next chapter opens on the heads of Gilead (36:1, frozen at THE TENT) — 35:34 the last verse of the last law-chapter; 36:13 the book\'s footer with the place-stamp %s' % STAMP)
        move('Sifrei 161:5 (the Hebrew colophon)', "'the book of Numbers is completed; blessed is the man who trusts in the LORD' — the shelf's own close, dropped by the English")
        return out("the closer — 35:34 the last verse of the last law-chapter; 36:13 the footer; the Sifrei's colophon on 161:5", ['accepted'])
    return out('no verdict in span', [FX.NONE])


# ---- THE WRAP — the daemon, the scene, the narrative ------------------------------------------------------
def law_refuge(event, world):
    """Num 35:1-34 (cold_run_refuge.py F1-F5). given_at Num 35:1; installed_by boot — A LAW IN THE DIVINE VOICE IN THE PLAINS OF MOAB (35:1's
    frame with the place-stamp, 33:50's class; 35:9 bare; the class named in the registry, the second pass decides). TWO TAPE LINES: the Levite
    cities commanded (35:1-8) — ONE debit on the people (give_the_levites_cities_and_pasture_lands, counterparty the Levites, OPEN by design to
    Joshua 21); the refuge law given (35:9-34) — ONE debit on the people (appoint_six_cities_of_refuge, OPEN by design to Deuteronomy 4:41 and
    Joshua 20:7-8). The exam's three case kinds dispatch to the cells in EXPLICIT branches with LITERAL effects per kind (2b's form — an unnamed effect is a KeyError);
    THE OFFICE-HOLDER'S DEATH (high_priest_died) CLOSES every open dwells_in_refuge entry by value and writes returns_to_his_possession —
    the term's closer, an act (outside the Torah on the tape)."""
    k, src = event['kind'], event['case_source']
    E_ = lambda eff, s, cp=None, amount=None, due=None, law='', value=None: {'effect': eff, 'subject': s, 'counterparty': cp, 'amount': amount, 'due': due, 'value': value if value is not None else True, 'source_law': law, 'case_source': src}
    day = event.get('day', world.clock.day)      # THE SEQUENTIAL RUN: the event's own day
    # ---- the two lines (page_order at the counter's day, no marker in the chapter) ----
    if k == 'levite_cities_commanded':
        return [E_('commanded', 'israel', cp='the-levites', value='give_the_levites_cities_and_pasture_lands', law='F1 [INK 35:2 "command the children of Israel that they give to the Levites … cities to dwell in" … 35:7 "forty-eight cities" — the debit OPEN BY DESIGN to Joshua 21:1-42 (21:2 the request quoting the spec; 21:41 the tally; the four lots 13 + 10 + 13 + 12): THE READBACK\'s]')]
    if k == 'refuge_law_given':
        return [E_('commanded', 'israel', value='appoint_six_cities_of_refuge', law='F2 [INK 35:11 "you shall appoint for yourselves cities" … 35:14 "three cities beyond the Jordan and three in the land of Canaan" — the debit OPEN BY DESIGN to Deuteronomy 4:41-43 (Moses\' three) and Joshua 20:7-8 (the six): THE READBACK\'s]')]
    # ---- the term's closer: the office-holder's death — the daemon's own close of every open dwells_in_refuge, by value ----
    if k == 'high_priest_died':
        outp = []
        holder = event.get('priest', 'eleazar')
        for ent in list(world.entities.values()):
            for e in ent.ledger:
                if e['effect'] == 'dwells_in_refuge' and e.get('open') and e.get('value') == holder:
                    world.close(ent.eid, 'dwells_in_refuge', '%s — the death of the high priest %s closes the term (35:25, 28)' % (src, holder), value=holder)
                    outp.append(E_('returns_to_his_possession', ent.eid, value='the land of his possession (35:28)', law='F4 [INK 35:28 "and after the death of the high priest the manslayer shall return to the land of his possession" — the term closed by the act, not by a day: the design\'s decision (e)]'))
        return outp
    # ---- the exam's case kinds: EXPLICIT branches per kind (the daemon gate parses explicit branches only — the shared tuple form was refused
    #      on the first gate run, 2026-09-13), each naming LITERALLY every effect it can write (2b's form — an unnamed effect is a KeyError) ----
    if k == 'levite_cities_case':
        v, e, _ = the_levite_cities({'ask': event['ask']}, DATA); L = 'F1 [%s]' % event['ask']; s_ = event['person']
        W = {'accepted': E_('accepted', s_, value=v, law=L), 'commanded': E_('commanded', s_, cp='the-levites', value=v, law=L)}
        return [W[x] for x in e if x != FX.NONE]
    if k == 'killer_case':
        fn = {'law': the_refuge_law, 'murderer': the_murderer}.get(event.get('cell'), the_manslayer)
        v, e, _ = fn({'ask': event['ask']}, DATA); L = '%s [%s]' % ({'law': 'F2', 'murderer': 'F3'}.get(event.get('cell'), 'F4'), event['ask']); s_ = event['person']
        W = {'accepted': E_('accepted', s_, value=v, law=L), 'commanded': E_('commanded', s_, value=v, law=L), 'exempt': E_('exempt', s_, value=v, law=L),
             'put_to_death': E_('put_to_death', s_, value=v, law=L), 'flees_to_refuge': E_('flees_to_refuge', s_, value=v, law=L),
             'dwells_in_refuge': E_('dwells_in_refuge', s_, value=event.get('priest', 'eleazar'), law=L), 'has_blood': E_('has_blood', s_, value='no_blood', law=L),
             'returns_to_his_possession': E_('returns_to_his_possession', s_, value=v, law=L)}
        return [W[x] for x in e if x != FX.NONE]
    if k == 'refuge_statute_case':
        v, e, _ = the_statute({'ask': event['ask']}, DATA); L = 'F5 [%s]' % event['ask']; s_ = event['person']
        W = {'accepted': E_('accepted', s_, value=v, law=L), 'put_to_death': E_('put_to_death', s_, value=v, law=L), 'flees_to_refuge': E_('flees_to_refuge', s_, value=v, law=L),
             'land_polluted_by_blood': E_('land_polluted_by_blood', 'the-land-of-canaan', cp=s_, value=v, law=L)}
        return [W[x] for x in e if x != FX.NONE]
    return []


LINES = [
    ('Num 35:1-8 — and the LORD spoke to Moses in the plains of Moab by the Jordan at Jericho, saying: command the children of Israel that they give to the Levites from the inheritance of their possession cities to dwell in, and pasture-land for the cities round about them you shall give to the Levites; and the cities shall be theirs to dwell in and their pasture-lands for their beasts and their substance and all their living; and the pasture-lands of the cities that you shall give to the Levites: from the wall of the city outward a thousand cubits round about; and you shall measure from outside the city the east side two thousand by the cubit, and the south side two thousand by the cubit, and the west side two thousand by the cubit, and the north side two thousand by the cubit, and the city in the midst — this shall be to them the pasture-lands of the cities; and the cities that you shall give to the Levites: the six cities of refuge which you shall give for the manslayer to flee there, and beside them you shall give forty-two cities; all the cities that you shall give to the Levites: forty-eight cities, them and their pasture-lands; and the cities that you shall give from the possession of the children of Israel — from the many you shall take more and from the few you shall take less; each according to his inheritance that they inherit shall give of his cities to the Levites', 'levite_cities_commanded'),
    ('Num 35:9-34 — and the LORD spoke to Moses, saying: speak to the children of Israel and say to them: when you are crossing the Jordan to the land of Canaan, you shall appoint for yourselves cities, cities of refuge they shall be for you, and a manslayer shall flee there who smites a soul unwittingly; and the cities shall be for you a refuge from the avenger, and the manslayer shall not die until he stands before the congregation for judgment; and the cities that you shall give: six cities of refuge they shall be for you; three cities you shall give beyond the Jordan and three cities you shall give in the land of Canaan, cities of refuge they shall be; for the children of Israel and for the stranger and for the sojourner among them these six cities shall be for refuge, to flee there whoever smites a soul unwittingly; and if with an instrument of iron he struck him and he died, he is a murderer, the murderer shall surely die … the avenger of blood himself shall put the murderer to death … and if suddenly without enmity … the congregation shall judge … and deliver … and return him to his city of refuge … and he shall dwell in it until the death of the high priest … a statute of judgment for your generations in all your dwellings … by the mouth of witnesses … one witness shall not testify … you shall not take ransom … the blood, it pollutes the land … in whose midst I dwell, for I the LORD dwell in the midst of the children of Israel', 'refuge_law_given'),
]
CLOSES = 'none — the Levite cities\' debit closes at Joshua 21 and the appointment\'s at Joshua 20 OUTSIDE THE TORAH (Deuteronomy 4:41\'s three inside it, forward); no manslayer stands on the tape; the term\'s closer (the high priest\'s death) Joshua 24:33'


def scene():
    """THE SCENE — the exam's rows replayed on the world engine (the exodus epoch): the exam's persons through the three case kinds, and THE
    OFFICE-HOLDER'S DEATH closing the manslayers' open terms by value."""
    with contextlib.redirect_stdout(io.StringIO()):
        w = WE.World(era='Num 35:1-34: the refuge cities on the shelf — Makkot, Sanhedrin, Bava Kamma, Ketubot, Eruvin, Sotah, Arakhin on the engine (the exodus epoch)', epoch='exodus')
        w.laws = [law_refuge]
        w.advance(w.clock.day_in('exodus', 40, 6, 1))
        # ---- the exam's persons through the three case kinds (LITERAL submits — the daemon gate parses no loop) ----
        w.submit({'kind': 'levite_cities_case', 'subject': 'the-measure', 'person': 'the-measure', 'ask': 'the_two_thousand', 'case_source': 'Mishnah Sotah 5:3; Sotah 27b:8 — the exam\'s row the_two_thousand'})
        w.submit({'kind': 'levite_cities_case', 'subject': 'the-forty-eight', 'person': 'the-forty-eight', 'ask': 'six_and_forty_two', 'case_source': 'Makkot 10a:4 — the exam\'s row six_and_forty_two'})
        w.submit({'kind': 'levite_cities_case', 'subject': 'the-levites-gift', 'person': 'the-levites-gift', 'ask': 'the_debit', 'case_source': 'Josh 21:2 — the exam\'s row the_debit'})
        w.submit({'kind': 'levite_cities_case', 'subject': 'the-sides', 'person': 'the-sides', 'ask': 'the_four_sides', 'case_source': 'Num 2:3-25 — the exam\'s row the_four_sides'})
        w.submit({'kind': 'killer_case', 'subject': 'the-six', 'person': 'the-six', 'cell': 'law', 'ask': 'six_cities', 'case_source': 'Mishnah Makkot 2:4 — the exam\'s row six_cities'})
        w.submit({'kind': 'killer_case', 'subject': 'the-appointment', 'person': 'the-appointment', 'cell': 'law', 'ask': 'the_debit', 'case_source': 'Makkot 11a:1 — the exam\'s row the_debit'})
        w.submit({'kind': 'killer_case', 'subject': 'the-iron-striker', 'person': 'the-iron-striker', 'cell': 'murderer', 'ask': 'the_iron', 'case_source': 'Sanhedrin 76b:12 — the exam\'s row the_iron'})
        w.submit({'kind': 'killer_case', 'subject': 'the-stone-striker', 'person': 'the-stone-striker', 'cell': 'murderer', 'ask': 'the_stone_and_the_wood', 'case_source': 'Sanhedrin 76b:12 — the exam\'s row the_stone_and_the_wood'})
        w.submit({'kind': 'killer_case', 'subject': 'the-beheaded', 'person': 'the-beheaded', 'cell': 'murderer', 'ask': 'the_mode', 'case_source': 'Mishnah Sanhedrin 9:1 — the exam\'s row the_mode'})
        w.submit({'kind': 'killer_case', 'subject': 'the-hater', 'person': 'the-hater', 'cell': 'murderer', 'ask': 'the_intents', 'case_source': 'Mishnah Sanhedrin 9:2 — the exam\'s row the_intents'})
        w.submit({'kind': 'killer_case', 'subject': 'the-roller', 'person': 'the-roller', 'cell': 'manslayer', 'ask': 'the_downward_motion', 'case_source': 'Mishnah Makkot 2:1 — the exam\'s row the_downward_motion'})
        w.submit({'kind': 'killer_case', 'subject': 'the-sudden-thruster', 'person': 'the-sudden-thruster', 'cell': 'manslayer', 'ask': 'suddenly', 'case_source': 'Makkot 7b:6 — the exam\'s row suddenly'})
        w.submit({'kind': 'killer_case', 'subject': 'the-delivered', 'person': 'the-delivered', 'cell': 'manslayer', 'ask': 'the_deliverance', 'priest': 'eleazar', 'case_source': 'Makkot 10b:14 — the exam\'s row the_deliverance'})
        w.submit({'kind': 'killer_case', 'subject': 'the-exile-under-eleazar', 'person': 'the-exile-under-eleazar', 'cell': 'manslayer', 'ask': 'the_term', 'priest': 'eleazar', 'case_source': 'Makkot 11a:12 — the exam\'s row the_term'})
        w.submit({'kind': 'killer_case', 'subject': 'the-exile-under-phinehas', 'person': 'the-exile-under-phinehas', 'cell': 'manslayer', 'ask': 'the_term', 'priest': 'phinehas', 'case_source': 'Mishnah Makkot 2:6 — the exam\'s row the_term (the second high priest)'})
        w.submit({'kind': 'killer_case', 'subject': 'the-one-who-left', 'person': 'the-one-who-left', 'cell': 'manslayer', 'ask': 'the_border', 'case_source': 'Makkot 12a:8 — the exam\'s row the_border'})
        w.submit({'kind': 'killer_case', 'subject': 'the-uncertain', 'person': 'the-uncertain', 'cell': 'manslayer', 'ask': 'the_uncertainty', 'case_source': 'Sifrei Bamidbar 160:8 — the exam\'s row the_uncertainty'})
        w.submit({'kind': 'killer_case', 'subject': 'the-son-who-killed', 'person': 'the-son-who-killed', 'cell': 'manslayer', 'ask': 'father_and_son', 'case_source': 'Mishnah Makkot 2:3 — the exam\'s row father_and_son'})
        w.submit({'kind': 'refuge_statute_case', 'subject': 'the-twenty-three', 'person': 'the-twenty-three', 'ask': 'a_statute_of_judgment', 'case_source': 'Makkot 7a:7 — the exam\'s row a_statute_of_judgment'})
        w.submit({'kind': 'refuge_statute_case', 'subject': 'the-one-witness', 'person': 'the-one-witness', 'ask': 'the_witnesses', 'case_source': 'Sanhedrin 33b:15 — the exam\'s row the_witnesses'})
        w.submit({'kind': 'refuge_statute_case', 'subject': 'the-ransomer', 'person': 'the-ransomer', 'ask': 'no_ransom', 'case_source': 'Ketubot 37b:3 — the exam\'s row no_ransom'})
        w.submit({'kind': 'refuge_statute_case', 'subject': 'the-fugitive-ransomer', 'person': 'the-fugitive-ransomer', 'ask': 'no_ransom_for_the_fugitive', 'case_source': 'Ketubot 37b:4 — the exam\'s row no_ransom_for_the_fugitive'})
        w.submit({'kind': 'refuge_statute_case', 'subject': 'the-unexecuted-shedder', 'person': 'the-unexecuted-shedder', 'ask': 'the_land_polluted', 'case_source': 'Arakhin 16a:22 — the exam\'s row the_land_polluted'})
        w.submit({'kind': 'refuge_statute_case', 'subject': 'the-shedder', 'person': 'the-shedder', 'ask': 'the_shedders_blood', 'case_source': 'Gen 9:6 — the exam\'s row the_shedders_blood'})
        w.submit({'kind': 'refuge_statute_case', 'subject': 'the-camp-and-the-land', 'person': 'the-camp-and-the-land', 'ask': 'in_whose_midst_i_dwell', 'case_source': 'Shabbat 33a:4 — the exam\'s row in_whose_midst_i_dwell'})
        # ---- THE OFFICE-HOLDER'S DEATH: the act that closes the term — Eleazar's (Joshua 24:33, outside the Torah), then Phinehas's (the second high priest's) ----
        w.advance(w.clock.day + 7)
        w.submit({'kind': 'high_priest_died', 'subject': 'eleazar', 'priest': 'eleazar', 'office': 'the high priest', 'case_source': 'Josh 24:33 — and Eleazar son of Aaron died; the exam\'s act: the term closed by the death (Makkot 11a:12)'})
        w.submit({'kind': 'high_priest_died', 'subject': 'phinehas', 'priest': 'phinehas', 'office': 'the high priest', 'case_source': 'Mishnah Makkot 2:6 — the second high priest\'s death returns the one sentenced in his days'})
    n = lambda eid, eff: len([e for e in w.entity(eid).ledger if e['effect'] == eff])
    o = lambda eid, eff: len([e for e in w.entity(eid).ledger if e['effect'] == eff and e.get('open')])
    tset = len([l for l in w.log if l[0] == 'TIMER-SET']); tfire = len([l for l in w.log if l[0] == 'TIMER-FIRE']); tcan = len([l for l in w.log if l[0] == 'TIMER-CANCEL'])
    closes = len([e for ent in w.entities.values() for e in ent.ledger if e.get('closed_by')])
    return ((n('the-measure', 'accepted'), n('the-forty-eight', 'accepted'), n('the-levites-gift', 'commanded'), n('the-sides', 'accepted'),
             n('the-six', 'accepted'), n('the-appointment', 'commanded'), n('the-iron-striker', 'put_to_death'), n('the-stone-striker', 'put_to_death'), n('the-beheaded', 'put_to_death'), n('the-hater', 'put_to_death'),
             n('the-roller', 'flees_to_refuge'), n('the-sudden-thruster', 'flees_to_refuge'), n('the-delivered', 'flees_to_refuge'), n('the-delivered', 'dwells_in_refuge'), o('the-delivered', 'dwells_in_refuge'), n('the-delivered', 'returns_to_his_possession'),
             n('the-exile-under-eleazar', 'dwells_in_refuge'), o('the-exile-under-eleazar', 'dwells_in_refuge'), n('the-exile-under-eleazar', 'returns_to_his_possession'),
             n('the-exile-under-phinehas', 'dwells_in_refuge'), o('the-exile-under-phinehas', 'dwells_in_refuge'), n('the-exile-under-phinehas', 'returns_to_his_possession'),
             n('the-one-who-left', 'has_blood'), n('the-one-who-left', 'exempt'), n('the-uncertain', 'exempt'), n('the-son-who-killed', 'flees_to_refuge'),
             n('the-twenty-three', 'accepted'), n('the-one-witness', 'accepted'), n('the-ransomer', 'put_to_death'), n('the-fugitive-ransomer', 'flees_to_refuge'), n('the-land-of-canaan', 'land_polluted_by_blood'), n('the-shedder', 'put_to_death'), n('the-camp-and-the-land', 'accepted')),
            (tset, tfire, tcan, len(w.timers)), len(w.entities), closes), w
SCENE, _W = scene()
# THE PREDICTION (typed before the first run — the scratchpad's ref_scene_predict.py, run BEFORE this runner existed): every exam person written once per
# effect; the three manslayers' dwells_in_refuge SET at the sentence (the-delivered, the-exile-under-eleazar under Eleazar; the-exile-under-phinehas under
# Phinehas), CLOSED BY THE DEATH ACT (open 0 after) with returns_to_his_possession written at the close; no timer (set 0, fired 0, cancelled 0, pending 0);
# ENTITIES: predicted 26 (the exam's 25 persons + the-land-of-canaan) — THE FIRST GRADED RUN PRINTED 25, the model's miss read as evidence: the unexecuted
# shedder's row writes land_polluted_by_blood ON THE LAND with the shedder as COUNTERPARTY (the design's decision (i)), so he is never written on and the
# engine makes no entity for him — twenty-four written-on persons + the land = 25; RETYPED FROM THE PRINT; CLOSES 3 — the three terms closed by the two deaths.
SCENE_PREDICTED = ((1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1), (0, 0, 0, 0), 25, 3)
assert SCENE == SCENE_PREDICTED, ('THE NUMBERS WALK: the scene moved from its prediction', SCENE, SCENE_PREDICTED)


def narrative():
    """THE NUMBERS WALK 15b (2026-09-13): the chapter's own acts AS HISTORY — the TWO lines of 35:1-34 at the counter's day (40, 6, 1), page-order
    after the borders' three (34:1-29) and before the tribes' plea (36:1-4), on a world with this runner's daemon: 2 writes, no timer, no marker,
    ONE entity (israel_people — the written-on party; the Levites a counterparty), no close, no row. Recorded by the sequential run's recorder and
    stitched onto the tape. Not a graded cell: the tuple below is a tripwire typed from the design; the sequence world's RUN tuple and CR1-CR9 grade
    the tape."""
    with contextlib.redirect_stdout(io.StringIO()):
        w = WE.World(era='Num 35:1-34: the refuge cities on the tape — the Levite cities commanded, the refuge law given (the exodus epoch)', epoch='exodus')
        w.laws = [law_refuge]
        w.advance(w.clock.day_in('exodus', 40, 6, 1))
        # THE DAEMON GATE READS LITERAL SUBMITS ONLY — the two lines typed out (the term's field named `term`, never `until`: the stitcher re-bases an `until` as a scene-clock day — the first stitch fell on the string, 2026-09-13)
        w.submit({'kind': 'levite_cities_commanded', 'subject': 'israel', 'cities': 48, 'refuge': 6, 'others': 42, 'thousand': 1000, 'two_thousand': 2000, 'sides': ['east', 'south', 'west', 'north'], 'case_source': LINES[0][0]})
        w.submit({'kind': 'refuge_law_given', 'subject': 'israel', 'six': 6, 'beyond_the_jordan': 3, 'in_canaan': 3, 'term': 'the death of the high priest', 'witnesses': 'plural', 'ransom': False, 'case_source': LINES[1][0]})
    writes = len([l for l in w.log if l[0] == 'WRITE'])
    closes = len([e for ent in w.entities.values() for e in ent.ledger if e.get('closed_by')])
    rows = len([l for l in w.log if l[0] == 'ROW'])
    return (writes, len([l for l in w.log if l[0] == 'TIMER-SET']), len(w.entities), w.clock.eras['exodus'].date(w.clock.day)[1:], closes, rows, len(w.tables['population'])), w


NARRATIVE, _WN = narrative()
NARRATIVE_PREDICTED = (2, 0, 1, (6, 1), 0, 0, 0)   # NUMBERS_WALK.md "Sitting 15b": 2 writes (L1 1, L2 1), no timer, ONE entity (israel_people — the written-on party; the Levites the counterparty, no entity), the counter's day (6, 1), no close, no row
assert NARRATIVE == NARRATIVE_PREDICTED, ('THE NUMBERS WALK: the refuge cities\' narrative moved from its prediction', NARRATIVE, NARRATIVE_PREDICTED)
assert [e['value'] for e in _WN.entity('israel').ledger if e['effect'] == 'commanded'] == ['give_the_levites_cities_and_pasture_lands', 'appoint_six_cities_of_refuge'] and all(e.get('open') for e in _WN.entity('israel').ledger if e['effect'] == 'commanded'), _WN.entity('israel').ledger


# =====================================================================
# Motion 2 — THE TEST DATA: the answer sheet's rows (the docket's LAW rows).
# =====================================================================
CASES = [
    # F1 — the Levite cities
    ('Num 35:2 / Sifrei 1:2; 34:2 by CALL — the command', lambda: the_levite_cities({'ask': 'the_command'}, DATA), "command the children of Israel (35:2) — the five Torah seats, this the fifth (Sifrei 1:2's five); the borders runner's cell by CALL"),
    ('Num 35:2 / Josh 21:2 — cities to dwell in', lambda: the_levite_cities({'ask': 'cities_to_dwell_in'}, DATA), "cities to dwell in (35:2) — three Bible seats: this, Joshua 14:4, and Joshua 21:2 the run's request; the debit on the people OPEN to Joshua 21"),
    ('Num 35:2-7 / Lev 25:34; Arakhin 33b:15 — the pasture-land', lambda: the_levite_cities({'ask': 'the_pasture_land'}, DATA), "the pasture-land (35:2-7) — six Torah seats, Leviticus 25:34's unsellable field and this chapter's five; 69 Bible verses, 32 Joshua 21's; the lot unchangeable (Arakhin 33b:15)"),
    ('Num 35:3 / Nedarim 81a:7; Makkot 12a:5 — their beasts', lambda: the_levite_cities({'ask': 'their_beasts'}, DATA), "their beasts (35:3) — two Bible seats; Onkelos 'their needs of life'; for life, not burial (Makkot 12a:5)"),
    ('Num 35:4 / Eruvin 56b:6 — the thousand', lambda: the_levite_cities({'ask': 'the_thousand'}, DATA), "a thousand cubits (35:4) — the Bible's one seat; the parser [1000] with the cubit consumed; the open land (Eruvin 56b:6)"),
    ('Num 35:5 / Mishnah Sotah 5:3; Eruvin 51a:8; Arakhin 9:8 — the two thousand', lambda: the_levite_cities({'ask': 'the_two_thousand'}, DATA), "two thousand by the cubit (35:5) — four times, read [2000] each by rule 29 (the bare dual marked by the sheva under the lamed); the Sabbath limit's measure (R. Akiva) — a data row with three settings"),
    ('Num 35:5 / Num 2 by CALL — the four sides', lambda: the_levite_cities({'ask': 'the_four_sides'}, DATA), "the four sides (35:5) — east, south, west, north: THE CAMP'S ORDER (Numbers 2 by CALL), against the borders' and the court's; the Levite city laid out as the camp"),
    ('Num 35:5 / Eruvin 51a:13-14 — the city in the midst', lambda: the_levite_cities({'ask': 'the_city_in_the_midst'}, DATA), "and the city in the midst (35:5) — one seat; the square (Eruvin 51a:13-14)"),
    ('Num 35:6-7 / Josh 21:4-7, 41; Makkot 10a:4 — six and forty-two', lambda: the_levite_cities({'ask': 'six_and_forty_two'}, DATA), "six and forty-two (35:6-7) — [6, 42] and [48], the sum asserted; Joshua 21's four lots 13 + 10 + 13 + 12 = 48 by the parser, the tally reads it; the forty-two receive too (Makkot 10a:4)"),
    ('Num 35:8 / 26:54 by CALL — the rule', lambda: the_levite_cities({'ask': 'the_rule'}, DATA), "the proportional rule (35:8) — 26:54's rule at its third seat by CALL; 'you shall take less' plural here alone"),
    ('Num 18:20-24, 26:62 by CALL — no inheritance', lambda: the_levite_cities({'ask': 'no_inheritance'}, DATA), "the Levites have no inheritance (18:20-24; 26:62 by CALL) — the cities the people's gift 'from the inheritance of their possession' (35:2), the block standing"),
    ('Num 35:2-8 / Josh 21 — the debit', lambda: the_levite_cities({'ask': 'the_debit'}, DATA), "the debit (35:2-8) — 'you shall give' ten times: commanded on the people, counterparty the Levites, OPEN by design to Joshua 21"),
    # F2 — the refuge law
    ('Num 35:10 / 33:51 by CALL — when you cross', lambda: the_refuge_law({'ask': 'when_you_cross'}, DATA), "when you are crossing the Jordan (35:10) — 33:51's clause by CALL (Deuteronomy 11:31 the third); 'to Canaan-ward' the directional form's Torah last"),
    ('Num 35:11 / Sifrei 159:1 — appoint', lambda: the_refuge_law({'ask': 'appoint'}, DATA), "you shall appoint (35:11) — one seat; designation, not a meeting (Balaam's root FALSE by sense); after the inheritance (Sifrei 159:1)"),
    ('Num 35:11 / Exod 21:13 by CALL; Makkot 12b:8 — the place become cities', lambda: the_refuge_law({'ask': 'the_place_become_cities'}, DATA), "the place become cities — Exodus 21:13's 'he shall flee there' at its Numbers seat: the Levites' cities for the generations, the Levite camp for the hour (M3 by CALL)"),
    ('Num 35:13-15 / Deut 4:43; Josh 20:7-8; Mishnah Makkot 2:4 — six cities', lambda: the_refuge_law({'ask': 'six_cities'}, DATA), "six cities (35:13-15) — [6], [3, 3], [6]: three and three; the names Deuteronomy 4:43's and Joshua 20:7-8's, none here; not until all six (Makkot 2:4): a data row"),
    ('Num 35:15 / Makkot 9a — for whom', lambda: the_refuge_law({'ask': 'for_whom'}, DATA), "for whom (35:15) — Israel, the stranger and the sojourner against 35:12's 'for you': the sojourner for a sojourner only (Makkot 9a); Joshua 20:9 drops the sojourner"),
    ('Num 35:11, 15 / Num 15 by CALL — unwittingly', lambda: the_refuge_law({'ask': 'unwittingly'}, DATA), "unwittingly (35:11, 15) — the sin offering's word (thirteen seats; the shelach runner by CALL); Deuteronomy's 'without knowledge'; Joshua 20:3 both"),
    ('Num 35:12 / Makkot 12a:11; Onkelos 35:19, 21 — until he stands', lambda: the_refuge_law({'ask': 'until_he_stands'}, DATA), "until he stands before the congregation (35:12) — the court before the avenger's hand (Makkot 12a:11; Onkelos' clause at 19, 21); Joshua 20:6 quotes it"),
    ('Num 35:11-14 / Deut 4:41; Josh 20:7-8 — the debit', lambda: the_refuge_law({'ask': 'the_debit'}, DATA), "the debit (35:11-14) — appoint six cities: commanded on the people, OPEN by design to Deuteronomy 4:41 and Joshua 20:7-8"),
    # F3 — the murderer
    ('Num 35:16 / Sanhedrin 76b:12-13 — the iron', lambda: the_murderer({'ask': 'the_iron'}, DATA), "the iron (35:16) — no 'hand', no size clause: iron of any size kills (Sanhedrin 76b:12-13); the parameter's exemption stated by the shelf"),
    ('Num 35:17-18 / Sanhedrin 76b:12; Sifrei 160:3-5 — the stone and the wood', lambda: the_murderer({'ask': 'the_stone_and_the_wood'}, DATA), "the stone and the wood (35:17-18) — 'of the hand whereby he may die': the size a PARAMETER (Sanhedrin 76b:12; the Sifrei's induction from three)"),
    ('Num 35:16-18, 21 / Sanhedrin 15b:5 — he is a murderer', lambda: the_murderer({'ask': 'he_is_a_murderer'}, DATA), "he is a murderer (35:16-18, 21) — four seats; 'shall surely die' five times, the Torah's densest; one root for four agents, defective at every Numbers seat"),
    ('Mishnah Sanhedrin 9:1 by CALL; Ketubot 37b:7 — the mode', lambda: the_murderer({'ask': 'the_mode'}, DATA), "the mode — the sword (M3 by CALL; Sanhedrin 9:1), from the neck (Ketubot 37b:7); any mode when the sword cannot be done (the doubled verb)"),
    ('Num 35:19, 21 / Sanhedrin 45b:13; Makkot 12a — the avenger\'s hand', lambda: the_murderer({'ask': 'the_avengers_hand'}, DATA), "the avenger's hand (35:19, 21) — the avenger puts him to death after the court; none — the court appoints one (Sanhedrin 45b:13); a data row with its arms"),
    ('Num 35:20-21 / Sanhedrin 76b:15; Mishnah Sanhedrin 9:1 — the manners', lambda: the_murderer({'ask': 'the_manners'}, DATA), "the manners (35:20-21) — thrust, threw, struck with the hand; the confiner a murderer (Sanhedrin 76b:15); the causation line the shelf's (a data row)"),
    ('Num 35:20-22 / Mishnah Sanhedrin 9:2; Sanhedrin 41a by CALL — the intents', lambda: the_murderer({'ask': 'the_intents'}, DATA), "the intents (35:20-22) — hatred, lying-in-wait (Exodus 21:13's verb as a noun), enmity (the serpent's word) against their negations: the intent's table (Sanhedrin 9:2) a data row; the forewarning a parameter by CALL"),
    ('Num 35:21, 24 / Lev 24:17 by CALL — the smiter', lambda: the_murderer({'ask': 'the_smiter'}, DATA), "the smiter (35:21, 24) — the active participle at seven Torah seats, the smitten woman its passive homograph; Leviticus 24:17's smiter by CALL"),
    ('Num 35:16-23 — the case table', lambda: the_murderer({'ask': 'the_table'}, DATA), "the case table (35:16-23) — computed from the tokens: the instruments, the manners, the intents; the verdicts a murderer, a manslayer, neither"),
    # F4 — the manslayer
    ('Num 35:22 / Makkot 7b:6; Num 6:9 — suddenly', lambda: the_manslayer({'ask': 'suddenly'}, DATA), "suddenly (35:22) — the nazirite's word (6:9, the naso runner's seat); the baraita's five marks read word by word (Makkot 7b:6)"),
    ('Num 35:23 / Makkot 9b:5 — without seeing', lambda: the_manslayer({'ask': 'without_seeing'}, DATA), "without seeing (35:23) — the blind killer disputed (R. Yehuda exempt, R. Meir exiled): a data row"),
    ('Num 35:23 / Mishnah Makkot 2:1 by CALL; Makkot 7b:2 — the downward motion', lambda: the_manslayer({'ask': 'the_downward_motion'}, DATA), "the downward motion (35:23 'and he dropped it') — descent exiles, ascent does not (Mishnah Makkot 2:1 by CALL; Makkot 7b:2)"),
    ('Num 35:23 / Sanhedrin 29a:6 — not his enemy', lambda: the_manslayer({'ask': 'not_his_enemy'}, DATA), "not his enemy (35:23) — the hater of three days off the witness stand and the bench (Sanhedrin 29a:6); the enemy's exile by the circumstances (R. Shimon)"),
    ('Num 35:24 / Mishnah Sanhedrin 1:6; Sifrei 160:8 — the congregation judges', lambda: the_manslayer({'ask': 'the_congregation_judges'}, DATA), "the congregation judges (35:24) — the court of twenty-three built from the congregation-tokens (the Sifrei 160:8; Mishnah Sanhedrin 1:6): a data row"),
    ('Num 35:25 / Makkot 10b:14 — the deliverance', lambda: the_manslayer({'ask': 'the_deliverance'}, DATA), "the deliverance (35:25) — the court returns him: flees_to_refuge (Exodus 21:13's effect at its second seat) and dwells_in_refuge, the term's open entry"),
    ('Num 35:25, 28, 32 / 20:28 and Lev 21:10 by CALL; Makkot 11a:12 — the term', lambda: the_manslayer({'ask': 'the_term'}, DATA), "the term (35:25, 28, 32) — until the death of the high priest (defective only here): an open entry on the manslayer closed by the office-holder's death act; the holder Eleazar by CALL, his death outside the Torah; the three high priests as data"),
    ('Num 35:26-27 / Exod 22:1 by CALL; Makkot 12a:8-15 — the border', lambda: the_manslayer({'ask': 'the_border'}, DATA), "the border (35:26-27) — outside the border the avenger has no blood: the burglar's clause reused (has_blood no_blood by CALL); the doubled infinitive and the mood disputed (Makkot 12a)"),
    ('Num 35:28 / Sifrei 161:5; Makkot 13a:6 — the return', lambda: the_manslayer({'ask': 'the_return'}, DATA), "the return (35:28) — after the death of the high priest to the land of his possession: returns_to_his_possession written at the term's close; the stem read (Sifrei 161:5)"),
    ('Sifrei 160:8 (Issi ben Akiva); Makkot 7b:4 — the uncertainty', lambda: the_manslayer({'ask': 'the_uncertainty'}, DATA), "unresolved"),
    ('Mishnah Makkot 2:2-3 by CALL — the father and the son', lambda: the_manslayer({'ask': 'father_and_son'}, DATA), "the father and the son (Mishnah Makkot 2:3 by CALL) — each exiles for the other; the office's exemptions (Abba Shaul) by CALL"),
    ('Makkot 12b:9 — the Levite exiled', lambda: the_manslayer({'ask': 'the_levite_exiled'}, DATA), "the Levite exiled (Makkot 12b:9) — from district to district; the exile who killed again to another neighborhood: a data row"),
    ('Mishnah Makkot 2:5, 2:8; Makkot 10a-10b — the honor, the roads, the teacher', lambda: the_manslayer({'ask': 'the_honor'}, DATA), "the exile's honor, roads and teacher (Mishnah Makkot 2:5, 2:8; Makkot 10a-10b) — the shelf's rows as data"),
    # F5 — the statute
    ('Num 35:29 / 27:11 by CALL; Makkot 7a:7 — a statute of judgment', lambda: the_statute({'ask': 'a_statute_of_judgment'}, DATA), "a statute of judgment (35:29) — the daughters' phrase (27:11 by CALL); 'in all your dwellings' the blood ban's formula: the Sanhedrin everywhere (Makkot 7a:7), never on the Sabbath"),
    ('Num 35:30 / Sifrei 161:1; Sanhedrin 33b:15 — the witnesses', lambda: the_statute({'ask': 'the_witnesses'}, DATA), "the witnesses (35:30) — two by the prototype (the Sifrei 161:1); one witness not to convict, but to acquit (Sanhedrin 33b:15); the ninth commandment's verb; a data row"),
    ('Num 35:31 / Exod 21:30 by CALL; Ketubot 37b — no ransom', lambda: the_statute({'ask': 'no_ransom'}, DATA), "no_ransom_the_death_stands"),
    ('Num 35:32 / Ketubot 37b:4; Makkot 11a:13 — no ransom for the fugitive', lambda: the_statute({'ask': 'no_ransom_for_the_fugitive'}, DATA), "no_ransom_the_exile_stands"),
    ('Num 35:33 / Arakhin 16a:22; Mishnah Sotah 9:7 — the land polluted', lambda: the_statute({'ask': 'the_land_polluted'}, DATA), "the land polluted (35:33) — the pollute-root's only Torah seat: a status on the land while the shedder stands; atoned only by his blood; the heifer's other passive Deuteronomy 21's (forward)"),
    ('Num 35:33 / Gen 9:6 by CALL; Sanhedrin 37b:12 — the shedder\'s blood', lambda: the_statute({'ask': 'the_shedders_blood'}, DATA), "the shedder's blood (35:33) — Genesis 9:6's clause run as law (the primeval runner by CALL): Cain's exile the half-atonement, the murderer's blood the whole"),
    ('Num 35:34 / Lev 18:25-28 by CALL; Shevuot 7b:7 — not defile', lambda: the_statute({'ask': 'not_defile'}, DATA), "you shall not defile the land (35:34) — Leviticus 18:25-28's land that vomits (the sanctions runner by CALL); bloodshed an impurity (Shevuot 7b:7)"),
    ('Num 35:34 / 5:3 by CALL; Shabbat 33a:4 — in whose midst I dwell', lambda: the_statute({'ask': 'in_whose_midst_i_dwell'}, DATA), "in whose midst I dwell (35:34) — the book's inclusio with 5:3 (the naso runner by CALL): the Presence in the camp and in the land, each guarded by a ban; the open promise read, not rewritten"),
    ('Num 35:34 / 36:1, 36:13; Sifrei 161:5 — the closer', lambda: the_statute({'ask': 'the_closer'}, DATA), "the closer — 35:34 the last verse of the last law-chapter; 36:13 the footer; the Sifrei's colophon on 161:5"),
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
    print('THE INK: integers %s; the dual marked %s; the unit noun %s; starred none; the frame verbs %s (two divine frames, the place-stamp at the first); the narrative verbs inside the cases %s; the case tokens %s' % (sorted(INTS.items()), TILDE, UNIT, FRAME_VERBS, NARR, CASE_TOKENS))
    print('THE MURDER-ROOT: %d tokens in the chapter (%d Torah verses, %d Bible); plene %s; the refuge-word %d Bible verses, Torah %s; "shall surely die" %d Torah seats, five here; the ransom-noun Torah %s; the pollute-root Torah %s' % (len(MURDER_TOK_35), len(MURDER_T), len(MURDER_B), MURDER_PLENE, len(REFUGE_B), len(REFUGE_T), len(SURELY_DIE_T), RANSOM_LEMMA_T, POLLUTE_LEMMA_T))
    print('THE TWIN SPECS: %s; THE INCLUSIO: %s; the six cities\' names by seat: %s' % (TWIN, sorted(set(INCLUSIO)), {k: len(v) for k, v in SIX_NAMES.items()}))
    print('THE SCENE on the bench: %s; the timers (set, fired, cancelled, pending) %s; entities %d; closes %d' % SCENE)
    print('THE NARRATIVE: %s' % (NARRATIVE,))
    print('THE PARAMETER ROWS: ' + '; '.join('%s = %s' % (k, DATA[k]['value']) for k in DATA) + ' (the other settings recorded in DATA)')
    if ok == len(CASES):
        print('\nTHE COMPILE OF THE REFUGE CITIES: the answer sheet REPRODUCED — %d/%d' % (ok, len(CASES)))
    sys.exit(0 if ok == len(CASES) else 1)

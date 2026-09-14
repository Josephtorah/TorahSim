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
exec(_SRC.split('# ==== INK BEGIN')[1].split('# ==== INK END ====')[0].split('\n', 1)[1], _INK)
ink_numbers, ink_ordinals, verse_words = _INK['ink_numbers'], _INK['ink_ordinals'], _INK['verse_words']

db = sqlite3.connect('<repo-old>/elijah_docket/tanakh.sqlite')

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

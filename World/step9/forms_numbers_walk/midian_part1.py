import os as _os
_ROOT = _os.path.normpath(_os.path.join(_os.path.dirname(_os.path.abspath(__file__)), '..', '..', '..'))   # THE PORTABLE REPO (2026-09-15): the repo root from this file's own place
#!/usr/bin/env python3
# NUM 31:1-54 — MIDIAN (THE NUMBERS WALK sitting 11b, 2026-09-12; World/step9/NUMBERS_WALK.md "Sitting 11b"; the state doc's #146-#147).
# THE WAR AS A RUN OF THREE OPEN DEBITS, THE DIVISION AS A CHECKED TABLE: the command "avenge the vengeance of the children of Israel from
# the Midianites" (31:2) opens a debit on Moses beside the Balak runner's harass_the_midianites (25:17 — the command and its run share the
# word), and the receipt "as the LORD commanded Moses" (31:7) closes both BY VALUE; the trumpets of 10:2 close at 31:6 in Phinehas's hand
# (a run by carrying — no sounding narrated); the five kings and Balaam slain (31:8 — the Balak runner's row by CALL); the captives, the
# spoil, the cities burned; Moses' wrath (31:14 — anger begets error, the statute in Eleazar's mouth at 31:21) and THE SENTENCE on the
# captives a COMMAND with no narrated run (OPEN forever); the warriors' purification as chukat's three timers by CALL on the men and on the
# captives (31:19 — the gentile's corpse by touch and carrying); the four materials of 31:20 against Leviticus 11:32's four ON THE DB (the
# edge shemini a TRANSFER taught — Shabbat 64a:7-8, 64a:15; Bava Kamma 25b:6); Eleazar's statute of the vessels (31:21-23 — the six metals,
# fire then the water of sprinkling, water for the rest; the Mishnah's modes and the immersion as DATA); THE DIVISION (31:25-47) as three
# debits opened by one speech and closed by three receipts, THE RATES "one of five hundred" and "one of fifty" the parser's new fraction
# class, the sixteen written numbers as counted statuses on four thing parties and the arithmetic CHECKED (the totals halved, the tribute
# at 1/500 = 840 heads, the Levites' 8,400 COMPUTED and UNWRITTEN); the officers' gold (31:48-54) as the ransom of Exodus 30 run at a
# count — IS.shekel by CALL — the memorial in the tent. Seven cells; every token probed (zero-report law); effects on every cell (the
# effects law); the parameters the ink leaves open recorded in DATA with their arms. Reading ledger: logic/oral_triage/num_31_midian_2026-09-12.md;
# the exam's docket: logic/oral_triage/num_31_midian_exam_2026-09-12.md (451 rows: LAW 86 / DERIVATION 70 / DISPUTE 12 / CONTEXT 282 / OUTSIDE 1).

# ---- THE HONEST-PAIRING GUARD ----------------------------------------------------------------------------
import os as _os, sys as _sys
_sys.path.insert(0, _os.path.dirname(_os.path.abspath(__file__)))
from compile_guards import check_honest_pairing as _chp
_P = _os.path.abspath(__file__)
GUARDED = _chp(_P, 'CASES', 2)
assert GUARDED == 99, ("the guard counted %d expectations, the tripwire holds 99" % GUARDED)   # the design's estimate — retyped from the guard's print after the first run
print('guard: %d expectations checked, every one a literal from the answer sheet [honest-pairing guard satisfied]' % GUARDED)
import sqlite3, sys, io, re, contextlib, collections, yaml
from fractions import Fraction
import effects_layer as FX
import world_engine as WE
import cold_run_balak as BK                      # THE EDGE: midian -> balak CALL, reference (25:17's "the Midianites" with the article — the debit's own verse; Balaam's and Zur's rows READ)
import cold_run_beha as BH                       # THE EDGE: midian -> beha CALL, reference (10:9's war clause; the trumpets' debit closed at 31:6)
import cold_run_chukat as CK                     # THE EDGE: midian -> chukat CALL, reference (the water of sprinkling, the third and the seventh day, the slain by the sword — the shared tokens of 19 and 31)
import cold_run_shemini as SH                    # THE EDGE: midian -> shemini CALL, TRANSFER taught (Shabbat 64a:7-8, 64a:15; Bava Kamma 25b:6; Sifrei 157:8 — Lev 11:32's four materials against 31:20's)
import cold_run_incense_shekel as IS             # THE EDGE: midian -> incense_shekel CALL, reference ("lift the head", "to atone for our souls", "a memorial before the LORD" — Exod 30:12-16's own words)
import cold_run_bamidbar as BM                   # THE EDGE: midian -> bamidbar CALL, reference (1:53's "keep the charge of the tabernacle" — 31:30's and 31:47's Levites)

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

def verse_text(ch, vs, book='Num'):
    rows = db.execute("""SELECT w.he FROM words w JOIN verses v ON w.verse_id=v.id WHERE v.book=?
        AND v.chapter=? AND v.verse=? ORDER BY w.idx""", (book, ch, vs)).fetchall()
    return ' '.join(strip(h) for (h,) in rows)

def words(ch, vs, book='Num'):
    return verse_text(ch, vs, book).split()

# ---- zero-report probes: the span's load-bearing tokens (every one measured on the DB before it was typed — the print of 2026-09-12) ----
PROBES = [
    ('נקם',      31, 2,  'avenge — the doubled verb "avenge the vengeance"'),
    ('נקמת',     31, 2,  'the vengeance of [the children of Israel]'),
    ('המדינים',  31, 2,  'the Midianites WITH THE ARTICLE — 25:17 and here alone: the command and its run share the word'),
    ('תאסף',     31, 2,  'you shall be gathered [to your people] — the sequence clause'),
    ('החלצו',    31, 3,  'arm [men from among you] — the muster verb'),
    ('לצבא',     31, 3,  'for the army'),
    ('אלף',      31, 4,  'a thousand [to a tribe] — the distributive pair'),
    ('למטה',     31, 4,  'to a tribe'),
    ('וימסרו',   31, 5,  'and there were delivered — the deliver-root, Sifrei 157:4'),
    ('חלוצי',    31, 5,  'armed for [the army]'),
    ('פינחס',    31, 6,  'Phinehas — the priest anointed for war (Sotah 43a:1)'),
    ('הקדש',     31, 6,  'the holy [vessels]'),
    ('וחצצרות',  31, 6,  'and the trumpets — 10:2\'s pair in his hand'),
    ('התרועה',   31, 6,  'of the alarm — 10:9\'s war clause'),
    ('ויצבאו',   31, 7,  'and they warred — a hapax, the chapter\'s own kind'),
    ('כאשר',     31, 7,  'as [the LORD commanded Moses] — THE RECEIPT'),
    ('ויהרגו',   31, 7,  'and they killed [every male] — Shechem\'s phrase'),
    ('מלכי',     31, 8,  'the kings of [Midian]'),
    ('חלליהם',   31, 8,  'their slain'),
    ('צור',      31, 8,  'Zur — Cozbi\'s father (25:15)'),
    ('חמשת',     31, 8,  'five [kings] — the parser\'s [5]'),
    ('בלעם',     31, 8,  'Balaam [son of Beor]'),
    ('בחרב',     31, 8,  'with the sword'),
    ('וישבו',    31, 9,  'and they took captive'),
    ('בזזו',     31, 9,  'they took as spoil'),
    ('טירתם',    31, 10, 'their castles — Onkelos\' houses of worship'),
    ('שרפו',     31, 10, 'they burned [with fire]'),
    ('השלל',     31, 11, 'the spoil'),
    ('המלקוח',   31, 11, 'the prey — the thing party\'s noun (four seats)'),
    ('השבי',     31, 12, 'the captives'),
    ('ערבת',     31, 12, 'the plains of [Moab] — the line\'s field'),
    ('לקראתם',   31, 13, 'to meet them — outside the camp'),
    ('ויקצף',    31, 14, 'and [Moses] was wroth — the wrath-verb, Moses its subject at three Torah seats'),
    ('פקודי',    31, 14, 'the officers of [the host]'),
    ('החיל',     31, 14, 'the host'),
    ('החייתם',   31, 15, 'have you kept alive — the midwives\' verb'),
    ('נקבה',     31, 15, 'every female'),
    ('בדבר',     31, 16, 'by the word of [Balaam] — Onkelos "by the counsel"'),
    ('מעל',      31, 16, 'treachery [against the LORD] — the sotah\'s phrase (5:6)'),
    ('פעור',     31, 16, 'Peor'),
    ('המגפה',    31, 16, 'the plague — 25:9\'s'),
    ('בטף',      31, 17, 'among the little ones'),
    ('למשכב',    31, 17, 'by lying with [a male]'),
    ('הטף',      31, 18, 'the little ones [among the women]'),
    ('החיו',     31, 18, 'keep alive [for yourselves]'),
    ('חנו',      31, 19, 'encamp [outside the camp]'),
    ('שבעת',     31, 19, 'seven [days]'),
    ('בחלל',     31, 19, 'the slain — the sword like the slain (Sifrei 158:3)'),
    ('תתחטאו',   31, 19, 'purify yourselves — the purify-verb'),
    ('השלישי',   31, 19, 'the third [day]'),
    ('השביעי',   31, 19, 'the seventh [day]'),
    ('ושביכם',   31, 19, 'and your captives — the gentile\'s corpse by touch'),
    ('בגד',      31, 20, 'garment — Lev 11:32\'s first shared material'),
    ('עור',      31, 20, 'skin'),
    ('עזים',     31, 20, 'goats — [work of] goats: the spun and woven'),
    ('עץ',       31, 20, 'wood'),
    ('אלעזר',    31, 21, 'Eleazar — the statute in the priest\'s voice'),
    ('חקת',      31, 21, 'the statute of [the Torah] — 19:2\'s head'),
    ('הזהב',     31, 22, 'the gold'),
    ('הכסף',     31, 22, 'the silver'),
    ('הנחשת',    31, 22, 'the bronze'),
    ('הברזל',    31, 22, 'the iron'),
    ('הבדיל',    31, 22, 'the tin — one Torah seat as a metal'),
    ('העפרת',    31, 22, 'the lead'),
    ('באש',      31, 23, 'into the fire'),
    ('תעבירו',   31, 23, 'you shall pass [through the fire]'),
    ('נדה',      31, 23, 'the water of sprinkling — the heifer\'s phrase'),
    ('יתחטא',    31, 23, 'it shall be purified'),
    ('במים',     31, 23, 'through water — the second branch'),
    ('וכבסתם',   31, 24, 'and you shall wash [your garments]'),
    ('וטהרתם',   31, 24, 'and be clean'),
    ('שא',       31, 26, 'lift [the head] — the census idiom, Exod 30:12'),
    ('מלקוח',    31, 26, 'the prey [of the captives]'),
    ('וחצית',    31, 27, 'and halve [the prey]'),
    ('תפשי',     31, 27, 'those who took [the war]'),
    ('והרמת',    31, 28, 'and you shall levy [a tribute]'),
    ('מכס',      31, 28, 'a tribute — the tribute-word\'s Torah seats both here'),
    ('אחד',      31, 28, 'one [soul of five hundred] — THE RATE'),
    ('מחמש',     31, 28, 'of five [hundred] — the from-prefix on the numeral, starred'),
    ('המאות',    31, 28, 'the hundreds — the article-bearing chain, starred'),
    ('תרומת',    31, 29, 'the heave-offering of [the LORD] — the half-shekel\'s phrase'),
    ('וממחצת',   31, 30, 'and from the half of [the children of Israel]'),
    ('אחז',      31, 30, 'held — one HELD of fifty'),
    ('החמשים',   31, 30, 'the fifty — the denominator, starred'),
    ('ללוים',    31, 30, 'to the Levites'),
    ('משמרת',    31, 30, 'the charge of [the tabernacle] — 1:53\'s'),
    ('ויעש',     31, 31, 'and [Moses and Eleazar] did — the second receipt'),
    ('יתר',      31, 32, 'the rest of [the plunder]'),
    ('צאן',      31, 32, 'sheep — 675,000'),
    ('ובקר',     31, 33, 'and cattle — 72,000'),
    ('וחמרים',   31, 34, 'and donkeys — 61,000'),
    ('ונפש',     31, 35, 'and persons — 32,000'),
    ('המחצה',    31, 36, 'the half — the warriors\' portion'),
    ('חלק',      31, 36, 'the portion of [those who went out to the army]'),
    ('המכס',     31, 37, 'the tribute [to the LORD] — 675'),
    ('ומכסם',    31, 38, 'and their tribute'),
    ('ויתן',     31, 41, 'and [Moses] gave — the third receipt\'s act'),
    ('חצה',      31, 42, 'halved'),
    ('מחצת',     31, 43, 'the half of [the congregation]'),
    ('האחז',     31, 47, 'the held one [of fifty] — the run'),
    ('ויקרבו',   31, 48, 'and [the officers] came near'),
    ('הפקדים',   31, 48, 'the officers [of the thousands of the army]'),
    ('נשאו',     31, 49, 'have lifted [the head] — the count'),
    ('נפקד',     31, 49, 'is missing — not one man'),
    ('קרבן',     31, 50, 'the offering of [the LORD] — the tent\'s phrase (Temurah 13a:14)'),
    ('אצעדה',    31, 50, 'the armlet'),
    ('וכומז',    31, 50, 'and the kumaz — the womb-mold (Shabbat 64a:20)'),
    ('לכפר',     31, 50, 'to atone [for our souls] — Exod 30:15-16\'s words'),
    ('התרומה',   31, 52, 'the heave-offering [of gold] — 16,750'),
    ('שקל',      31, 52, 'shekel'),
    ('בזזו',     31, 53, 'had taken spoil [every man for himself] — outside the count'),
    ('זכרון',    31, 54, 'a memorial [for the children of Israel before the LORD] — Exod 30:16\'s six words'),
]
for tok, ch, vs, note in PROBES:
    if tok not in words(ch, vs):
        sys.exit('ZERO-REPORT LAW: probe %r (%s) failed at Num %d:%d — refusing to run' % (tok, note, ch, vs))
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
SPAN = [(31, v) for v in range(1, 55)]
NUMBERS = {v: ink_numbers(verse_words('Num', 31, v)) for _, v in SPAN}
ORDINALS = {v: ink_ordinals(verse_words('Num', 31, v)) for _, v in SPAN}
STARRED = [(v, t) for _, v in SPAN for t in verse_words('Num', 31, v) if t.endswith('*')]
MARKED = [(v, t) for _, v in SPAN for t in verse_words('Num', 31, v) if '%' in t]
COUNTS = {v: n for v, n in NUMBERS.items() if n}
RATES = {v: [(x.numerator, x.denominator) for x in n] for v, n in COUNTS.items() if any(isinstance(x, Fraction) for x in n)}
INTS = {v: n for v, n in COUNTS.items() if v not in RATES}
assert INTS == {4: [1000, 1000], 5: [1000, 12000], 6: [1000], 8: [5], 19: [7], 32: [675000], 33: [72000], 34: [61000], 35: [32000], 36: [337500], 37: [675],
                38: [36000, 72], 39: [30500, 61], 40: [16000, 32], 43: [337500], 44: [36000], 45: [30500], 46: [16000], 52: [16750]}, INTS
assert RATES == {28: [(1, 500)], 30: [(1, 50)], 47: [(1, 50)]}, RATES                                                  # THE RATIO CLASS "one of the N" — rule (28), taught this sitting
assert {v: o for v, o in ORDINALS.items() if o} == {19: [3, 7], 24: [7]}, ORDINALS
assert STARRED == [(28, 'מחמש*'), (28, 'המאות*'), (30, 'החמשים*'), (47, 'החמשים*')], STARRED                          # the denominators starred — never counted
assert MARKED == [(28, 'אחד/500%'), (30, 'אחד/50%'), (47, 'אחד/50%')], MARKED                                          # the one carries the fraction mark
TRIBUTE_RATE, LEVITE_RATE = Fraction(*RATES[28][0]), Fraction(*RATES[30][0])
# THE ARITHMETIC AS CHECKS (the design's CX7): the totals halved, the tribute at the rate, the Levites' share computed
TOTALS = (INTS[32][0], INTS[33][0], INTS[34][0], INTS[35][0])          # sheep, cattle, donkeys, persons — 31:32-35
WARRIORS = (INTS[36][0], INTS[38][0], INTS[39][0], INTS[40][0])        # the warriors' portion — 31:36, 31:38-40
TRIBUTE = (INTS[37][0], INTS[38][1], INTS[39][1], INTS[40][1])         # the tribute — 31:37-40
CONGREGATION = (INTS[43][0], INTS[44][0], INTS[45][0], INTS[46][0])    # the congregation's half — 31:43-46
LEVITES = tuple(int(c * LEVITE_RATE) for c in CONGREGATION)            # COMPUTED, UNWRITTEN — 31:30's rate on 31:43-46
assert tuple(t // 2 for t in TOTALS) == WARRIORS == CONGREGATION, (TOTALS, WARRIORS, CONGREGATION)
assert tuple(int(w * TRIBUTE_RATE) for w in WARRIORS) == TRIBUTE and sum(TRIBUTE) == 840, (WARRIORS, TRIBUTE)
assert LEVITES == (6750, 720, 610, 320) and sum(LEVITES) == 8400 and all(t % 1000 == 0 for t in TOTALS), LEVITES
MUSTER = INTS[4][0] * 12
assert MUSTER == INTS[5][1] == 12000, (INTS[4], INTS[5])                                                                 # 1,000 x 12 the ink's own product
GOLD = INTS[52][0]
FIRST = {v: words(31, v)[0] for _, v in SPAN}
FRAME_VERBS = [(v, FIRST[v], words(31, v)[1]) for _, v in SPAN if FIRST[v] in ('וידבר', 'ויאמר', 'ויאמרו')]
assert FRAME_VERBS == [(1, 'וידבר', 'יהוה'), (3, 'וידבר', 'משה'), (15, 'ויאמר', 'אליהם'), (21, 'ויאמר', 'אלעזר'), (25, 'ויאמר', 'יהוה'), (49, 'ויאמרו', 'אל')], FRAME_VERBS
# the whole-DB phrase census (the seats typed from the measurement print of 2026-09-12)
_V = collections.OrderedDict()
for b, c, v, he in db.execute("SELECT v.book, v.chapter, v.verse, w.he FROM words w JOIN verses v ON w.verse_id=v.id ORDER BY v.id, w.idx"):
    _V.setdefault((b, c, v), []).append(strip(he))
def seats(phrase):
    p = phrase.split(); n = len(p)
    return ['%s %d:%d' % k for k, ws in _V.items() if any(ws[i:i + n] == p for i in range(len(ws) - n + 1))]
TORAH = ('Gen', 'Exod', 'Lev', 'Num', 'Deut')
def torah_seats(phrase):
    return [s for s in seats(phrase) if s.split()[0] in TORAH]
MIDIANITES_ART = seats('המדינים'); AVENGE = seats('נקם נקמת'); VENGEANCE_OF_THE_LORD = seats('נקמת יהוה'); GATHERED = seats('אחר תאסף')
THOUSAND_PER_TRIBE = seats('אלף למטה'); TRUMPETS_OF_ALARM = seats('וחצצרות התרועה'); WARRED = seats('ויצבאו'); RECEIPT = torah_seats('כאשר צוה יהוה את משה')
KILLED_EVERY_MALE = seats('ויהרגו כל זכר'); KINGS_OF_MIDIAN = seats('מלכי מדין'); FIVE_KINGS = seats('חמשת מלכי מדין'); BALAAM_SON_OF_BEOR = seats('בלעם בן בעור')
WORD_OF_BALAAM = seats('בדבר בלעם'); TREACHERY = seats('מעל ביהוה'); MATTER_OF_PEOR = seats('דבר פעור'); MOSES_WROTH = seats('ויקצף משה'); OFFICERS_OF_THE_HOST = seats('פקודי החיל')
LYING_WITH_A_MALE = seats('למשכב זכר'); KEEP_ALIVE = seats('החיו לכם'); OUTSIDE_SEVEN = seats('מחוץ למחנה שבעת ימים'); THIRD_AND_SEVENTH = seats('ביום השלישי וביום השביעי')
YOU_AND_YOUR_CAPTIVES = seats('אתם ושביכם'); STATUTE_HEAD = seats('זאת חקת התורה'); WATER_OF_SPRINKLING = seats('במי נדה'); PASS_THROUGH_FIRE = seats('תעבירו באש')
LIFT_THE_HEAD = seats('שא את ראש'); WHEN_YOU_LIFT = seats('כי תשא את ראש'); ONE_OF_FIVE_HUNDRED = seats('אחד נפש מחמש המאות'); ONE_HELD_OF_FIFTY = seats('אחד אחז מן החמשים')
HEAVE_OFFERING = seats('תרומת יהוה'); KEEP_THE_CHARGE = seats('שמרי משמרת משכן יהוה'); TRIBUTE_TOKENS = torah_seats('מכס'); PREY_TOKENS = torah_seats('המלקוח')
HALF_OF_THE_CONGREGATION = seats('מחצת העדה'); LIFTED_THE_HEAD = seats('נשאו את ראש'); NONE_MISSING = seats('ולא נפקד ממנו איש'); ATONE_OUR_SOULS = seats('לכפר על נפשתינו')
ATONE_YOUR_SOULS = seats('לכפר על נפשתיכם'); MEMORIAL = seats('זכרון לבני ישראל לפני יהוה'); MEMORIAL_EXOD = seats('לזכרון לפני יהוה'); OFFERING_OF_THE_LORD = seats('קרבן יהוה')
GOLD_PHRASE = seats('ששה עשר אלף שבע מאות וחמשים'); TIN = torah_seats('הבדיל'); LEAD = seats('העפרת'); WROTH_TOKENS = torah_seats('ויקצף'); PURIFY_2 = seats('תתחטאו'); PURIFY_3 = seats('יתחטא')
assert MIDIANITES_ART == ['Num 25:17', 'Num 31:2'] and AVENGE == ['Num 31:2'] and GATHERED == ['Num 31:2'], (MIDIANITES_ART, AVENGE, GATHERED)
assert VENGEANCE_OF_THE_LORD == ['Jer 50:15', 'Jer 50:28', 'Jer 51:11', 'Num 31:3'] and THOUSAND_PER_TRIBE == ['Num 31:4', 'Num 31:5', 'Num 31:6'], (VENGEANCE_OF_THE_LORD, THOUSAND_PER_TRIBE)
assert TRUMPETS_OF_ALARM == ['2Chr 13:12', 'Num 31:6'] and WARRED == ['Num 31:7'] and KILLED_EVERY_MALE == ['Gen 34:25', 'Num 31:7'], (TRUMPETS_OF_ALARM, WARRED, KILLED_EVERY_MALE)
assert RECEIPT == ['Num 1:19', 'Num 2:33', 'Num 3:51', 'Num 8:3', 'Num 8:22', 'Num 15:36', 'Num 26:4', 'Num 27:11', 'Num 31:7', 'Num 31:31', 'Num 31:41', 'Num 31:47', 'Num 36:10'], RECEIPT
assert KINGS_OF_MIDIAN == ['Judg 8:5', 'Judg 8:12', 'Judg 8:26', 'Num 31:8'] and FIVE_KINGS == ['Num 31:8'], (KINGS_OF_MIDIAN, FIVE_KINGS)
assert BALAAM_SON_OF_BEOR == ['Deut 23:5', 'Josh 13:22', 'Mic 6:5', 'Num 22:5', 'Num 31:8'] and WORD_OF_BALAAM == ['Num 31:16'], (BALAAM_SON_OF_BEOR, WORD_OF_BALAAM)
assert TREACHERY == ['1Chr 10:13', '2Chr 28:19', 'Lev 5:21', 'Num 5:6', 'Num 31:16'] and MATTER_OF_PEOR == ['Num 25:18', 'Num 31:16'], (TREACHERY, MATTER_OF_PEOR)
assert MOSES_WROTH == ['Num 31:14'] and OFFICERS_OF_THE_HOST == ['2Chr 23:14', 'Num 31:14'] and WROTH_TOKENS == ['Deut 1:34', 'Exod 16:20', 'Gen 40:2', 'Lev 10:16', 'Num 31:14'], (MOSES_WROTH, OFFICERS_OF_THE_HOST, WROTH_TOKENS)
assert LYING_WITH_A_MALE == ['Judg 21:12', 'Num 31:17'] and KEEP_ALIVE == ['Num 31:18'], (LYING_WITH_A_MALE, KEEP_ALIVE)
assert OUTSIDE_SEVEN == ['Num 12:15', 'Num 31:19'] and THIRD_AND_SEVENTH == ['Num 19:12', 'Num 19:19', 'Num 31:19'] and YOU_AND_YOUR_CAPTIVES == ['Num 31:19'], (OUTSIDE_SEVEN, THIRD_AND_SEVENTH, YOU_AND_YOUR_CAPTIVES)
assert PURIFY_2 == ['Num 31:19', 'Num 31:20'] and PURIFY_3 == ['Num 19:12', 'Num 19:13', 'Num 19:20', 'Num 31:23'], (PURIFY_2, PURIFY_3)
assert STATUTE_HEAD == ['Num 19:2', 'Num 31:21'] and WATER_OF_SPRINKLING == ['Num 31:23'] and PASS_THROUGH_FIRE == ['Num 31:23'], (STATUTE_HEAD, WATER_OF_SPRINKLING, PASS_THROUGH_FIRE)
assert TIN == ['Deut 10:8', 'Num 16:9', 'Num 31:22'] and LEAD == ['Num 31:22', 'Zech 5:8'], (TIN, LEAD)
assert LIFT_THE_HEAD == ['Num 31:26'] and WHEN_YOU_LIFT == ['Exod 30:12'] and LIFTED_THE_HEAD == ['Num 31:49'] and NONE_MISSING == ['Num 31:49'], (LIFT_THE_HEAD, WHEN_YOU_LIFT, LIFTED_THE_HEAD, NONE_MISSING)
assert ONE_OF_FIVE_HUNDRED == ['Num 31:28'] and ONE_HELD_OF_FIFTY == ['Num 31:30'] and TRIBUTE_TOKENS == ['Num 31:28', 'Num 31:41'], (ONE_OF_FIVE_HUNDRED, ONE_HELD_OF_FIFTY, TRIBUTE_TOKENS)
assert len(HEAVE_OFFERING) == 11 and HEAVE_OFFERING[-2:] == ['Num 31:29', 'Num 31:41'] and KEEP_THE_CHARGE == ['Num 31:30', 'Num 31:47'], (HEAVE_OFFERING, KEEP_THE_CHARGE)
assert PREY_TOKENS == ['Num 31:11', 'Num 31:12', 'Num 31:27', 'Num 31:32'] and HALF_OF_THE_CONGREGATION == ['Num 31:43'], (PREY_TOKENS, HALF_OF_THE_CONGREGATION)
assert ATONE_OUR_SOULS == ['Num 31:50'] and ATONE_YOUR_SOULS == ['Exod 30:15', 'Exod 30:16', 'Lev 17:11'], (ATONE_OUR_SOULS, ATONE_YOUR_SOULS)
assert MEMORIAL == ['Num 31:54'] and MEMORIAL_EXOD == ['Exod 30:16'] and OFFERING_OF_THE_LORD == ['Num 9:7', 'Num 9:13', 'Num 31:50'] and GOLD_PHRASE == ['Num 31:52'], (MEMORIAL, MEMORIAL_EXOD, OFFERING_OF_THE_LORD, GOLD_PHRASE)
# THE SIX METALS (31:22) and THE FOUR MATERIALS (31:20 against Lev 11:32 — ON THE DB)
METALS = [w for w in words(31, 22) if w not in ('אך', 'את', 'ואת')]
assert METALS == ['הזהב', 'הכסף', 'הנחשת', 'הברזל', 'הבדיל', 'העפרת'], METALS
NUM_MATERIALS = [w for w in words(31, 20) if w in ('בגד', 'עור', 'עזים', 'עץ')]
LEV_MATERIALS = [w for w in words(11, 32, 'Lev') if w in ('עץ', 'בגד', 'עור', 'שק')]
SHARED_MATERIALS = sorted(set(NUM_MATERIALS) & set(LEV_MATERIALS))
assert NUM_MATERIALS == ['בגד', 'עור', 'עזים', 'עץ'] and LEV_MATERIALS == ['עץ', 'בגד', 'עור', 'שק'] and SHARED_MATERIALS == ['בגד', 'עור', 'עץ'], (NUM_MATERIALS, LEV_MATERIALS)
KINGS_NAMES = [words(31, 8)[i + 1] for i, w in enumerate(words(31, 8)) if w in ('את', 'ואת')][1:6]                       # after 'the kings of', before 'Balaam'
assert KINGS_NAMES == ['אוי', 'רקם', 'צור', 'חור', 'רבע'], KINGS_NAMES                                                    # the five names in the ink's order
ORNAMENTS = words(31, 50)[9:14]
assert ORNAMENTS == ['אצעדה', 'וצמיד', 'טבעת', 'עגיל', 'וכומז'], ORNAMENTS                                                # the five ornaments in the ink's order

# ---- THE CALLEES (live import edges; the design's cells by name) ----
BK_MOAB = BK.phinehas_and_midian({'ask': 'midian_not_moab'}, BK.DATA)                                                    # THE CALL: the debit's scope — Midian, never Moab
BK_BALAAM = BK.phinehas_and_midian({'ask': 'balaam_death'}, BK.DATA)                                                     # THE CALL: Balaam's death row READ
BK_ZUR = BK.phinehas_and_midian({'ask': 'cozbi_and_zur'}, BK.DATA)                                                       # THE CALL: Zur among the five
assert BK_MOAB[0].startswith('Midian harassed, Moab spared') and BK_MOAB[1] == ['commanded'], BK_MOAB
assert BK_BALAAM[0].startswith('Balaam killed by the sword at Midian (31:8)') and BK_ZUR[0].startswith('Cozbi daughter of Zur'), (BK_BALAAM[0], BK_ZUR[0])
assert BK.DATA['balaam_death']['value'] == 'by_the_sword_at_midian' and sorted(BK.DATA['balaam_death']['settings']) == ['by_the_sword_at_midian', 'four_modes'], BK.DATA['balaam_death']
assert BK.DATA['cozbi_and_zur']['value'] == 'zur_of_the_five_kings' and BK.DATA['midian_command_run']['value'] == ('31:2', '31:7'), (BK.DATA['cozbi_and_zur'], BK.DATA['midian_command_run'])
BH_WAR = BH.trumpets({'ask': 'oppression', 'kind': 'war'}, BH.DATA); BH_COUNT = BH.trumpets({'ask': 'count'}, BH.DATA)      # THE CALL: 10:9's war clause; the pair
assert BH_WAR[0] == 'the alarm — war itself (10:9)' and BH_WAR[1] == ['sanctify_day'] and BH_COUNT[0].startswith('2 — the wilderness pair') and BH.TRUMPETS == [2], (BH_WAR, BH_COUNT)
assert BH.DATA['oppression_scope']['value'] == 'any oppression', BH.DATA['oppression_scope']
CK_SCHEDULE = CK.corpse_tumah({'ask': 'schedule', 'third': True, 'seventh': True}, CK.DATA); CK_SEVEN = CK.corpse_tumah({'ask': 'seven_days'}, CK.DATA)   # THE CALL: the timers' dues
CK_SWORD = CK.corpse_tumah({'ask': 'sword_like_slain'}, CK.DATA); CK_CAMPS = CK.corpse_tumah({'ask': 'camps'}, CK.DATA)
CK_TENT = CK.corpse_tumah({'ask': 'tent_gentile'}, CK.DATA); CK_METAL = CK.corpse_tumah({'ask': 'metal_vessels_decree'}, CK.DATA); CK_REMOVES = CK.corpse_tumah({'ask': 'removes'}, CK.DATA)
assert CK_SCHEDULE[1] == ['sprinkling_due_third_day', 'sprinkling_due_seventh_day', 'declared_pure'] and CK_SEVEN[1] == ['corpse_unclean_seven_days'], (CK_SCHEDULE, CK_SEVEN)
assert CK_SWORD[0].startswith('a sword is like the slain') and CK_CAMPS[1] == ['sent_outside_the_camp'] and CK_TENT[0].startswith("gentiles' graves defile by touch and carrying"), (CK_SWORD[0], CK_CAMPS, CK_TENT[0])
assert CK_METAL[1] == ['disqualified'] and CK_REMOVES[1] == ['corpse_unclean_seven_days', 'impure_until_evening'], (CK_METAL, CK_REMOVES)
assert CK.SCHEDULE == [3, 7, 3, 7] and CK.SEVENS == [[7], [7], [7]], (CK.SCHEDULE, CK.SEVENS)
assert CK.DATA['sword_like_slain']['value'] == 'a_metal_vessel_takes_the_corpse_grade' and CK.DATA['tent_gentile']['value'] == 'no_tent_impurity', CK.DATA['tent_gentile']
THIRD_DUE, SEVENTH_DUE, SEVEN = CK.SCHEDULE[0], CK.SCHEDULE[1], CK.SEVENS[0][0]                                          # chukat's own dues — day + 3, day + 7, seven days
SH_TOUCH = SH.touch_effect('touch_carcass'); SH_CARRY = SH.touch_effect('carry_carcass')                                 # THE CALL: the carcass grade (Lev 11:24-25)
assert SH_TOUCH[0] == 'impure_until_evening' and SH_CARRY[0] == 'wash_and_evening' and SH_TOUCH[2].startswith('Lev 11:24'), (SH_TOUCH, SH_CARRY)
IS_LIFT = IS.shekel('lift_head')['v']; IS_ATONE = IS.shekel('atone_souls')['v']; IS_PLAGUE = IS.shekel('plague_clause'); IS_SILVER = IS.shekel('silver_of_atonements')['v']   # THE CALL: Exod 30:12-16
assert IS_LIFT == ['Exod 30:12'] and IS_ATONE == ['Exod 30:15', 'Exod 30:16', 'Lev 17:11'] and IS_PLAGUE['v'] == ['Exod 30:12'] and IS_PLAGUE['fx'] == ['no_plague_at_counting'], (IS_LIFT, IS_ATONE, IS_PLAGUE)
assert IS_SILVER == ['Exod 30:16'] and IS.shekel('trigger_parameter')['v'] == {'ink': 'census', 'descendant': 'yearly'}, IS_SILVER
BM_CHARGES = BM.charges({'ask': 'houses_charges'}, BM.DATA)                                                              # THE CALL: 1:53's charge on the Levites
assert BM_CHARGES[0] == 'gershon the woven, kohath the holy, merari the frame' and BM_CHARGES[1] == ['charge_kept'], BM_CHARGES

import os as _os
_ROOT = _os.path.normpath(_os.path.join(_os.path.dirname(_os.path.abspath(__file__)), '..', '..'))   # THE PORTABLE REPO (2026-09-15): the repo root from this file's own place
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
assert RATES == {28: [(1, 500)], 30: [(1, 50)], 42: [(1, 2)], 47: [(1, 50)]}, RATES                                    # THE RATIO CLASS "one of the N" — rule (28), taught this sitting; 42: [(1, 2)] since THE DEUTERONOMY WALK 1b (2026-09-15) — rule (30) THE HALF OF A NAMED WHOLE reads "the half-part of the children of Israel" (31:42) as the half
assert {v: o for v, o in ORDINALS.items() if o} == {19: [3, 7], 24: [7]}, ORDINALS
assert STARRED == [(28, 'מחמש*'), (28, 'המאות*'), (30, 'החמשים*'), (47, 'החמשים*')], STARRED                          # the denominators starred — never counted
assert MARKED == [(28, 'אחד/500%'), (30, 'אחד/50%'), (42, 'וממחצית%'), (47, 'אחד/50%')], MARKED                                          # the one carries the fraction mark
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
THOUSAND_PER_TRIBE = seats('אלף למטה'); TRUMPETS_OF_ALARM = seats('וחצצרות התרועה'); WARRED = seats('ויצבאו'); RECEIPT = [s for s in seats('כאשר צוה יהוה את משה') if s.startswith('Num ')]   # the formula's Numbers seats (thirteen of the Torah's thirty-eight)
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


# ===== THE DATA CHANNEL — the parameter rows the ink leaves open (motion 2's recorded settings) =========
DATA = {
    'muster_count': {'value': 12000, 'settings': {12000: "R. Akiva — the ink's own product: 'a thousand to a tribe, a thousand to a tribe' (31:4) is the distributive pair, 31:5's 'twelve thousand armed for the army' the sum (Sifrei 157:3)", 24000: "R. Yishmael — the doubling read twice: 'a thousand to a tribe' for the war and 'a thousand to a tribe' for the guard of the vessels — twenty-four thousand, twelve thousand delivered (Sifrei 157:3)"},
                     'source': "31:4-5 — the parser's [1000, 1000] and [1000, 12000]: 1,000 x 12 = 12,000 a CHECK; the doubled clause the shelf's question"},
    'levi_in_the_muster': {'value': 'included', 'settings': {'included': "'to ALL the tribes of Israel' (31:4) — Levi INCLUDED (Sifrei 157:3's Hebrew: the phrase brings Levi in)", 'excluded': "the export's English of the same piska reads 'to EXCLUDE the tribe of Levi' — the reversed arm, the export's defect class (RESEARCH_LOG)"},
                           'source': "31:4 'to all the tribes of Israel' — the ink names all; the Sifrei's Hebrew and its translation disagree (measured at the reading)"},
    'delivered_how': {'value': 'against_their_will', 'settings': {'against_their_will': "'and there were DELIVERED' (31:5) — against their will: they had heard that Moses' death hung on the war (31:2 'afterward you shall be gathered') and would not go (Sifrei 157:4's first reading)", 'counted_by_lot': "delivered by count — the tribes' own choosing, the second reading (Sifrei 157:4)", 'righteous_men': "'were delivered' — men handed over as fit, the righteous of each tribe (Sifrei 157:4's third reading)"},
                      'source': "31:5 וימסרו ('and they were delivered') — the deliver-root's two Torah seats both in this verse-pair; the passive leaves the deliverer unnamed"},
    'holy_vessels': {'value': 'the_ark_and_the_frontplate', 'settings': {'the_ark_and_the_frontplate': "the Sifrei 157:4: the holy vessels — the ark and the frontplate (the Urim by which they ask)", 'the_ark_and_the_tablets': "Sotah 43a:1 read word by word — 'them': the Sanhedrin; 'Phinehas': THE PRIEST ANOINTED FOR WAR; 'the holy vessels': the ark and the tablets in it; 'the trumpets of the alarm': the shofarot"},
                     'source': "31:6 'the holy vessels and the trumpets of the alarm in his hand' — the ink names no vessel; the trumpets 10:2's pair (BH.TRUMPETS by CALL)"},
    'phinehas_lineage': {'value': 'joseph_and_jethro_both', 'settings': {'joseph_and_jethro_both': "Sotah 43a:2-3: Phinehas went to exact the judgment of his mother's father JOSEPH — 'and the Midianites sold him' (Genesis 37:36); the tribes' taunt 'this son of Puti' — Jethro who fattened calves; 'from the DAUGHTERS of Putiel' (Exodus 6:25) — TWO: from Joseph AND from Jethro", 'joseph': "the Sifrei 157:4's Hebrew — Joseph alone (the reading's finding: Genesis 37:36 names the MEDANITES)", 'jethro': "the export's English inserts Jethro — the reading's defect line"},
                         'source': "31:6 'Phinehas son of Eleazar the priest' — the ink names the father; the mother's line the shelf's"},
    'balaam_death': {'value': BK.DATA['balaam_death']['value'], 'settings': BK.DATA['balaam_death']['settings'],
                     'source': "31:8 'and Balaam son of Beor they killed with the sword' — the Balak runner's row READ by CALL (by_the_sword_at_midian; the four court modes recorded — Sanhedrin 106a:16, 106b:1)"},
    'cozbi_and_zur': {'value': BK.DATA['cozbi_and_zur']['value'], 'settings': {BK.DATA['cozbi_and_zur']['value']: BK.DATA['cozbi_and_zur']['source']},   # the Balak row carries value + source, no settings: the one setting the row's own
                      'source': "31:8 'Zur' among the five kings — Cozbi's father (25:15, 25:18): the Balak runner's row READ by CALL"},
    'castles_reading': {'value': 'castles', 'settings': {'castles': "the Hebrew's טירתם ('their castles', 31:10) — the encampments' towers", 'houses_of_worship': "Onkelos 31:10: 'the houses of their worship' — the castles read as the idols' houses (the reading's Onkelos line)"},
                        'source': "31:10 'all their cities in their dwellings and all their castles they burned with fire' — the word's sense open"},
    'known_a_man_test': {'value': 'fit_for_intercourse_at_three_years', 'settings': {'fit_for_intercourse_at_three_years': "Rav Huna: THE VERSE SPEAKS OF ONE FIT FOR INTERCOURSE — the line at three years, not at the act (Yevamot 60b:9-10); the Sifrei 157:6-7: 'every woman who has known a man' — fit for it, 'the little ones among the women who have not known' — the unfit kept alive", 'by_the_act': "the plain sense — killed for the deed, kept alive for its absence (Rav Huna's contradiction of the two verses, 60b:8 — refused at 60b:9)"},
                         'source': "31:17-18 'every woman who has known a man by lying with a male' / 'the little ones among the women who have not known a man' — the two case kinds read against each other"},
    'frontplate_test': {'value': 'passed_before_the_frontplate', 'settings': {'passed_before_the_frontplate': "Rav Huna bar Bizna in R. Shimon Chasida's name: they passed them before the FRONTPLATE — the face of one fit for intercourse turned sallow (Yevamot 60b:11); Jabesh-gilead's four hundred by the barrel of wine (60b:12 — Rav Kahana); the frontplate for Israel's acceptance, not calamity — for gentiles even calamity (60b:13)"},
                        'source': "no test in the ink — 31:35 names the outcome ('the women who had not known a man by lying with a male, 32,000 souls'); the instrument the shelf's"},
    'proselyte_age': {'value': 'under_three_fit_for_the_priesthood', 'settings': {'under_three_fit_for_the_priesthood': "R. Shimon ben Yochai: a female convert under three years and a day is fit for the priesthood — 'keep alive for yourselves' (31:18) with Phinehas among them (Yevamot 60b:6; Kiddushin 78a:19); THE HALAKHA as him (Yevamot 60b:14); the reason 'virgins of the seed of the house of Israel' (Ezekiel 44:22) — a hymen formed as a Jew (Kiddushin 78a:21)", 'as_slaves_and_maidservants': "the Rabbis: 'keep alive for yourselves' — as slaves and maidservants, not for marriage (Yevamot 60b:7)"},
                      'source': "31:18 'keep alive for yourselves' — the ink's 'for yourselves' the shelf's hook"},
    'punish_by_inference': {'value': 'refused', 'settings': {'refused': "we do not punish by inference — the second 'kill' of 31:17 written because the a-fortiori could not carry the death (Sifrei 157:6 — R. Yoshiyah; Makkot 5b:11-12 'you have taught us, our teacher'); no prohibition by inference either (5b:14), not lashes (5b:15), not exile (5b:16)", 'to_close_the_subject': "R. Yishmael: the second 'kill' 'to close the subject' — a structural reading, not the rule about rules (Sifrei 157:6)", 'abaye_rava_fork': "Sanhedrin 54a:17: whether one administers punishment on an a-fortiori — Abaye and Rava's dispute, one Sage yes, one no"},
                            'source': "31:17 'kill ... kill' — the verb doubled at the two case kinds (computed: הרגו twice in the verse)"},
    'goat_work_reading': {'value': 'spun_and_woven', 'settings': {'spun_and_woven': "'or sack' (Leviticus 11:32) — SPUN AND WOVEN, so everything spun and woven, not ropes and measuring cords (Shabbat 64a:3; the Sifrei 157:8); reins and the horse's belly band (64a:4), the horse's and the cow's tail (64a:9); horn and hoof in, birds' bones out (Chullin 25b:4)"},
                          'source': "31:20 'every work of goats' against Leviticus 11:32's 'sack' — the freed-word identity of Sifrei 157:8 run both ways (Shabbat 64a:7-8)"},
    'camp_entry_reading': {'value': 'seventh_day_wash_then_the_camp', 'settings': {'seventh_day_wash_then_the_camp': "31:24 'wash your garments on the seventh day and be clean; afterward you shall come into the camp' against 19:19's 'clean at evening' — Sifrei 158:3's two-way likening: the camp after the wash, the purity at evening", 'seven_days_floor': "Rava: 'wash your garments on the seventh day' — a Torah edict that what a corpse defiles stays impure no less than SEVEN DAYS (Bava Kamma 25b:13)"},
                           'source': "31:24 — the seventh day named for the wash and the entry; the evening 19:19's"},
    'kashering_modes': {'value': 'by_the_vessels_use', 'settings': {'by_the_vessels_use': "Mishnah Avodah Zarah 5:12 (= 75b:6): what is used by immersion he immerses; what by purging in boiling water he purges (pots); what by whitening in fire he whitens (the spit and the grill); the knife he polishes; the baraita's table (75b:17) — unused: immerse; used cold: rinse and immerse; used hot: purge and immerse; used with fire: whiten and immerse; the measures — until the outer layer sheds, a kettle in a kettle (76a:17); AS IT ABSORBS SO IT EMITS (76b:1; Pesachim 30b:6); the knife thrust ten times into hard earth (76b:2), white-hot for Passover (Pesachim 30b:5); earthenware never — 'the Torah testified: broken' (Pesachim 30b:8; Leviticus 6:21)", 'same_day_pot': "the Torah forbids only a pot used THAT SAME DAY by the gentile (Rav Chiyya son of Rav Huna, Avodah Zarah 75b:21-76a:1; Pesachim 44b:15); the rest a rabbinic fence (76a:2)", 'the_novelty': "the Rabbis: the purging of gentiles' vessels is itself a NOVELTY — a taste that taints forbidden here alone (Pesachim 44b:14, 44b:16); R. Akiva derives THE TASTE AS THE SUBSTANCE from these vessels (Nazir 37b:1; Pesachim 44b:13)"},
                        'source': "31:23 'everything that comes into the fire you shall pass through the fire ... and everything that does not come into the fire you shall pass through water' — the ink's TWO branches; the Mishnah's four modes its branches by use (the Sifrei 158:2's one list)"},
    'immersion_source': {'value': 'and_it_shall_be_pure', 'settings': {'and_it_shall_be_pure': "Rava: 'and it shall be pure' (31:23) ADDS an act to the fire — IMMERSION in forty se'ah; the purged and the whitened immersed too (Avodah Zarah 75b:7); Bar Kappara: 'NEVERTHELESS' excludes the third and seventh day's sprinkling, 'the water of niddah' the water a menstruant immerses in (75b:8-11)", 'a_fortiori_of_the_sifrei': "the Sifrei 158:2: if for the water of sprinkling ... an a-fortiori to the immersion (the reading's line)", 'scope': "metal utensils alone (75b:14); PURCHASED as the captured were, not borrowed (75b:13); even new (75b:12); glass as metal, the glazed by its final state (75b:15); meal utensils"},
                         'source': "31:23 'only with the water of sprinkling it shall be purified' — the phrase's four Torah seats all in 19 and 31; the shelf splits its sense here"},
    'sword_like_slain': {'value': CK.DATA['sword_like_slain']['value'], 'settings': CK.DATA['sword_like_slain']['settings'],
                         'source': "31:19 'whoever has touched any slain' with 31:22's metals — CK's row READ by CALL: the metal sword takes the corpse's grade (Nazir 53b:11; Pesachim 14b:1, 14b:5; Chullin 3a:1); the vessel's toucher until evening (Nazir 54b:6; Oholot 1:2-3)"},
    'tent_gentile': {'value': CK.DATA['tent_gentile']['value'], 'settings': CK.DATA['tent_gentile']['settings'],
                     'source': "31:19 'you and your captives' — CK's row READ by CALL: no tent (Yevamot 61a:1) but touch and carrying — the Midian war's purification the proof even per R. Shimon ben Yochai (61a:5)"},
    'levites_rate_reading': {'value': 'the_terumahs_average', 'settings': {'the_terumahs_average': "R. Levi: 'from the half of the children of Israel take one part in fifty' (31:30) — 'all you take elsewhere shall be like this': the average terumah ONE FIFTIETH from this verse (Jerusalem Talmud Terumot 4:3:2; Mishnah Terumot 4:3 — generous one fortieth, the House of Shammai one thirtieth, the average one fiftieth, stingy one sixtieth)", 'no_torah_measure': "the Torah's own measure of terumah: one in a hundred (R. Yonatan), one in a thousand (R. Yannai), NO MEASURE — 'the first of your grain', any amount (R. Mana; Jerusalem Talmud Terumot 4:3:8)"},
                             'source': "31:30 'one held of fifty' — the parser's Fraction(1, 50); a TRANSFER taught (Num 31:30 -> Mishnah Terumot 4:3's average)"},
    'tribute_rate_reading': {'value': 'one_time_instruction', 'settings': {'one_time_instruction': "Menachot 77b:20: the thanks-offering's teruma NOT derived from Midian's — its measure was not one of ten, and IT IS NOT PRACTICED FOR ALL GENERATIONS (the daemon's class witnessed: the rates instruct this spoil alone)", 'asked_as_a_measure': "R. Avin's dilemma: the ash removal's measure from the tithe's teruma (one in a hundred) or from Midian's (ONE IN FIVE HUNDRED)? — answered by the handful (Yoma 24a:5)"},
                             'source': "31:28 'one soul of five hundred' — the parser's Fraction(1, 500); the tribute-word's Torah seats both here"},
    'ornaments_reading': {'value': 'five_named_by_the_shelf', 'settings': {'five_named_by_the_shelf': "the armlet, the bracelet, the ring, the earring, the kumaz (31:50 — the ink's five in order); R. Elazar: agil a mold in the shape of the breasts, kumaz a mold in the shape of the womb (Shabbat 64a:20); the kumaz in Aramaic 'what leads to folly' — Rav Yosef; Rabba: an acronym (64a:21); vessels for impurity — 'all vessels with which labor is done' (31:51; Shabbat 60a:3, 63b:19); the bracelet impure beside 31:19 (63b:6)"},
                          'source': "31:50 — the five ornaments computed from the verse; their shapes the shelf's"},
    'atonement_reading': {'value': 'ransom_at_a_count', 'settings': {'ransom_at_a_count': "the ink: 'lift the head' (31:49 / Exodus 30:12), 'to atone for our souls before the LORD' (31:50 / 30:15-16), 'a memorial before the LORD' (31:54 / 30:16) — the ransom of Exodus 30 run at a count: no plague at the counting (IS.shekel by CALL)", 'the_eyes_thoughts': "Rav Nachman in Rabba bar Avuh's name: 'not one man of us is missing' — 'then why atonement?' — 'from the grasp of transgression we emerged, not from the grasp of its THOUGHTS' (Shabbat 64a:22); the school of R. Yishmael: they nourished their eyes from nakedness — the atonement for the EYES (64a:23-64b:2; Berakhot 24a:15)", 'moral_count': "R. Shimon ben Yochai: 'not one man of us is missing' — missing TO TRANSGRESSION (Yevamot 61a:4); the Rabbis: the casualty count, no Jew fell"},
                          'source': "31:49-50 — the ink's three phrases Exodus 30:12-16's own words (computed on the DB)"},
    'anger_seats': {'value': 'three_seats_of_moses_anger', 'settings': {'three_seats_of_moses_anger': "the Sifrei 157:9: at three places Moses grew angry and erred — the manna (Exodus 16:20), the goat (Leviticus 10:16), here (31:14); the wrath-verb with Moses as subject at exactly these three Torah seats (computed: ויקצף five Torah tokens, three Moses')", 'the_shelfs_three': "Pesachim 66b:6-9: the scholar's wisdom departs (Moses — 31:14 then 31:21), the prophet's prophecy (Elisha, 2 Kings 3:14-15), whoever is angry is lowered (Eliab, 1 Samuel 17:28 / 16:7); the haughty too (Hillel, 66b:6)"},
                    'source': "31:14 'and Moses was wroth with the officers of the host' — the verb's five Torah tokens computed"},
    'oppression_scope': {'value': BH.DATA['oppression_scope']['value'], 'settings': BH.DATA['oppression_scope']['settings'],
                         'source': "31:6 'the trumpets of the alarm in his hand' — BH's row READ by CALL: 10:9's war clause the reference; no sounding narrated"},
    'trigger_parameter': {'value': IS.shekel('trigger_parameter')['v'], 'settings': {'census': "the ink: the ransom at a count (Exodus 30:12 'when you lift the head') — this chapter's count the run", 'yearly': "the descendant: the yearly half-shekel (Mishnah Shekalim)"},
                          'source': "31:49-50 — the officers' count and their offering; IS's row READ by CALL"},
}


# ===== F1: THE VENGEANCE AND THE MUSTER (Num 31:1-6) =========================================================
def the_vengeance(case, data):
    del P[:]
    ask = case['ask']
    if ask == 'the_command':
        ink('31:1-2', '"avenge the vengeance of the children of Israel from THE MIDIANITES; afterward you shall be gathered to your people" — the Midianites with the article at %s alone (computed): THE COMMAND AND ITS RUN SHARE THE WORD; "avenge the vengeance" %s' % (MIDIANITES_ART, AVENGE))
        move('cold_run_balak (CALL) — BK.DATA[midian_command_run] = %s' % (BK.DATA['midian_command_run']['value'],), "the Balak compile named this chapter's two verses as the debit's run; the Midian debit OPEN to 31:7")
        return out('avenge the vengeance — the command and its run share the word: the Midianites with the article at 25:17 and 31:2 alone', ['commanded'])
    if ask == 'vengeance_of_the_lord':
        ink('31:3', '"to put the vengeance of the LORD upon Midian" — Moses relays "the vengeance of the children of Israel" as the LORD\'s; the phrase\'s seats %s' % VENGEANCE_OF_THE_LORD)
        move('Sifrei 157:2', "whoever stands against Israel stands against the Holy One — Moses' relay turns Israel's vengeance into the LORD's")
        return out("Moses relays the vengeance of the children of Israel as the vengeance of the LORD (31:3) — Sifrei 157:2", ['commanded'])
    if ask == 'gathered_after':
        ink('31:2', '"afterward you shall be gathered to your people" — %s, one seat: the SEQUENCE — Moses\' death after the war' % GATHERED)
        move('Sifrei 157:2; Nedarim 37b:8', "Moses' death hung on the war and he ran to it (the Sifrei); 'afterward' among the scribes' ornamentations (the shelf's lexical row)")
        return out("the sequence — Moses gathered to his people AFTER the war (31:2); the checkpoint waits at Deuteronomy 34", ['accepted'])
    if ask == 'muster':
        ink('31:4-5', '"a thousand to a tribe, a thousand to a tribe, to all the tribes of Israel" — the distributive pair %s; "twelve thousand armed for the army" — the parser\'s %s; 1,000 x 12 = %d THE INK\'S OWN PRODUCT' % (INTS[4], INTS[5], MUSTER))
        dat('the row muster_count: %s (the other setting %s recorded)' % (data['muster_count']['value'], [k for k in data['muster_count']['settings'] if k != data['muster_count']['value']]))
        return out("twelve thousand — a thousand to a tribe, the distributive pair; 1,000 x 12 the ink's own product (31:4-5)", ['counted'])
    if ask == 'muster_count':
        dat('the row muster_count: %s' % data['muster_count']['value']); move('Sifrei 157:3', "R. Yishmael's doubling read twice (24,000) against R. Akiva's twelve — the ink's product")
        return out("twelve thousand (R. Akiva; the ink's product) — R. Yishmael's twenty-four thousand recorded (Sifrei 157:3)", ['counted'])
    if ask == 'levi_in_the_muster':
        ink('31:4', '"to ALL the tribes of Israel" — the ink names all'); dat('the row levi_in_the_muster: %s (the export\'s reversed arm recorded)' % data['levi_in_the_muster']['value'])
        move('Sifrei 157:3', "'to all the tribes of Israel' — to include the tribe of Levi (the Hebrew); the export's English reads 'to exclude'")
        return out("Levi in — 'to all the tribes of Israel' includes Levi (Sifrei 157:3's Hebrew); the export's 'to exclude' the reversed arm", ['accepted'])
    if ask == 'delivered':
        ink('31:5', '"and there were delivered from the thousands of Israel" — the passive; the deliverer unnamed'); dat('the row delivered_how: %s (three readings recorded)' % data['delivered_how']['value'])
        move('Sifrei 157:4', "against their will — Moses' death hung on the war; the three readings")
        return out("'they were delivered' — against their will, the war brought Moses' death near (Sifrei 157:4); the three readings recorded", ['accepted'])
    if ask == 'holy_vessels':
        ink('31:6', '"the holy vessels and the trumpets of the alarm in his hand" — the ink names no vessel; the trumpets 10:2\'s pair (BH.TRUMPETS %s by CALL)' % BH.TRUMPETS)
        dat('the row holy_vessels: %s (Sotah 43a:1\'s arm recorded)' % data['holy_vessels']['value']); move('Sifrei 157:4; Sotah 43a:1', "the ark and the frontplate / the ark and the tablets; the trumpets the shofarot")
        return out("the ark and the frontplate (Sifrei 157:4) / the ark and the tablets (Sotah 43a:1) — the shelf assigns the vessels; the trumpets the shofarot", ['accepted'])
    if ask == 'phinehas_anointed_for_war':
        ink('31:6', '"Phinehas son of Eleazar the priest" sent with the twelve thousand — the priest, not Eleazar')
        move('Sotah 43a:1-3', "'them' the Sanhedrin; Phinehas THE PRIEST ANOINTED FOR WAR; the avenger of his mother's father Joseph — 'and the Midianites sold him' (Genesis 37:36)")
        dat('the row phinehas_lineage: %s' % data['phinehas_lineage']['value'])
        return out("Phinehas the priest anointed for war (Sotah 43a:1); 'them' the Sanhedrin; the avenger of Joseph — 'the Midianites sold him' (Sotah 43a:2-3; Sifrei 157:4)", ['accepted'])
    if ask == 'phinehas_lineage':
        dat('the row phinehas_lineage: %s' % data['phinehas_lineage']['value']); move('Sotah 43a:3', "'from the DAUGHTERS of Putiel' — two: Joseph and Jethro both")
        return out("from the daughters of Putiel — Joseph and Jethro both (Sotah 43a:3); the Sifrei's Hebrew Joseph alone, the export's English Jethro", ['accepted'])
    if ask == 'the_trumpets':
        ink('31:6', '"the trumpets of the alarm in his hand" — %s (2 Chronicles 13:12 Abijah\'s war, where the priests DO sound); the trumpets EXIST: 10:2\'s making implied by the run, never narrated' % TRUMPETS_OF_ALARM)
        move('cold_run_beha (CALL) — BH.trumpets(count) = %s' % BH_COUNT[0], "moses' commanded the_trumpets (10:2) CLOSED BY VALUE at 31:6 — A RUN BY CARRYING")
        return out("the trumpets in Phinehas's hand (31:6) — moses' debit the_trumpets closed BY VALUE: a run by carrying; no sounding narrated", ['accepted'])
    if ask == 'war_clause':
        move('cold_run_beha (CALL) — BH.trumpets(oppression, war) = %s' % BH_WAR[0], "10:9's war clause the REFERENCE — 'when you go to war in your land against the oppressor you shall sound an alarm'; the row oppression_scope = %s" % data['oppression_scope']['value'])
        ink('31:6-7', 'NO SOUNDING NARRATED — the trumpets carried (31:6), the war fought (31:7): nothing written for the alarm (the law\'s own silence)')
        return out("10:9's war clause by CALL — 'the alarm — war itself'; nothing written for the alarm: no sounding narrated (BH.trumpets)", ['accepted'])
    if ask == 'moab_spared':
        move('cold_run_balak (CALL) — BK.phinehas_and_midian(midian_not_moab) = %s' % BK_MOAB[0], "Ulla's consolation: Moses reasoned an a-fortiori from 'harass the Midianites' (25:17) to Moab — Deuteronomy 2:9 barred it (Bava Kamma 38a:16)")
        ink('31:2-3', '"from the Midianites" / "upon Midian" — Moab never named in the chapter (computed: no Moab-token but the plains of Moab, 31:12)')
        return out("Midian harassed, Moab spared — Deuteronomy 2:9 barred Moses' own a-fortiori (Bava Kamma 38a:16; BK by CALL)", ['commanded'])
    return out('no verdict in span', [FX.NONE])


# ===== F2: THE WAR (Num 31:7-12) ==============================================================================
def the_war(case, data):
    del P[:]
    ask = case['ask']
    if ask == 'receipt':
        ink('31:7', '"and they warred against Midian AS THE LORD COMMANDED MOSES" — the war-verb a hapax %s; the receipt formula\'s Numbers seats %s, this chapter four of them (31:7, 31:31, 31:41, 31:47)' % (WARRED, [s for s in RECEIPT if s.startswith('Num 31:')]))
        move('THE REGISTER GATE (register_census.receipts)', "the receipt closes israel_people's harass_the_midianites (the Balak runner's debit, 25:17) and moses' avenge_the_midianites (31:2) BY VALUE — the 7b lesson; 31:7 turns CLOSE")
        return out("as the LORD commanded Moses (31:7) — the receipt closes israel_people's harass_the_midianites and moses' avenge_the_midianites BY VALUE", ['accepted'])
    if ask == 'every_male':
        ink('31:7', '"and they killed every male" — %s: Shechem\'s phrase, Genesis 34:25 its only other seat' % KILLED_EVERY_MALE)
        return out("they killed every male — Shechem's phrase (Genesis 34:25 its only other seat)", ['slain'])
    if ask == 'five_kings':
        ink('31:8', '"Evi, Rekem, Zur, Hur, Reba — the five kings of Midian" — the names %s in the ink\'s order; the parser\'s %s; "the kings of Midian" %s' % (KINGS_NAMES, INTS[8], KINGS_OF_MIDIAN))
        move('Joshua 13:21 (RUN_CITATION)', "'the princes of Sihon, dwelling in the land' — the five retold with three deltas; ONE PARTY on the ledger (the registry's the_five_kings is Genesis 14's, chur Exodus 17's)")
        return out("five kings — Evi, Rekem, Zur, Hur, Reba (31:8; the parser's [5]); Joshua 13:21 retells them as the princes of Sihon: a RUN_CITATION; one party on the ledger", ['slain'])
    if ask == 'zur':
        move('cold_run_balak (CALL) — BK.phinehas_and_midian(cozbi_and_zur) = %s' % BK_ZUR[0], "Zur one of the five (BK.DATA[cozbi_and_zur] = %s)" % data['cozbi_and_zur']['value'])
        return out("Zur one of the five kings — Cozbi's father dies in the war her death opened (31:8; 25:15 — BK's row by CALL)", ['slain'])
    if ask == 'balaam':
        ink('31:8', '"and Balaam son of Beor they killed with the sword" — %s; the ass\'s sword clause (22:29) a CROWN in the reading\'s sense, no entry of its own' % BALAAM_SON_OF_BEOR)
        move('cold_run_balak (CALL) — BK.phinehas_and_midian(balaam_death) = %s' % BK_BALAAM[0], "the row balaam_death = %s (the settings %s)" % (data['balaam_death']['value'], sorted(data['balaam_death']['settings'])))
        return out("Balaam killed with the sword (31:8) — come for his wages (Sanhedrin 106a:16); the four court modes recorded (106b:1) — BK's row by CALL", ['slain'])
    if ask == 'captives':
        ink('31:9', '"and the children of Israel took captive the women of Midian and their little ones" — taken_captive on the captives, cp israel (Lot\'s effect, Genesis 14)')
        return out("the women of Midian and their little ones taken captive (31:9) — the captives of Midian one party, cp israel", ['taken_captive'])
    if ask == 'spoil':
        ink('31:9', '"all their cattle, all their flocks and all their goods they took as spoil" — spoil_taken on israel, cp the Midianites (Shechem\'s effect, Genesis 34)')
        return out("all their cattle, all their flocks, all their goods taken as spoil (31:9) — spoil_taken on israel, cp the Midianites", ['spoil_taken'])
    if ask == 'cities_burned':
        ink('31:10', '"all their cities in their dwellings and all their castles they burned with fire"'); dat('the row castles_reading: %s (Onkelos\' houses of worship recorded)' % data['castles_reading']['value'])
        return out("all their cities in their dwellings and all their castles burned with fire (31:10) — Onkelos' houses of worship the castles_reading row", ['burned_in_fire'])
    if ask == 'brought_to_moses':
        ink('31:11-12', '"they took all the spoil and all the prey, of man and of beast, and brought to Moses, to Eleazar the priest and to the congregation ... at the plains of Moab by the Jordan at Jericho" — the prey-noun %s (four seats, the thing party); the line\'s field' % PREY_TOKENS)
        return out("the captives, the prey and the spoil brought to Moses, Eleazar and the congregation at the plains of Moab by the Jordan at Jericho (31:12) — the line's field", ['accepted'])
    if ask == 'joshua_13':
        move('Joshua 13:21-22 (RUN_CITATION)', "the five as 'the princes of Sihon, dwelling in the land' and 'Balaam son of Beor the diviner' slain with the sword among their slain — three deltas from 31:8: princes for kings, Sihon's, the diviner")
        return out("Joshua 13:21-22 retells the five as the princes of Sihon and Balaam the diviner slain with the sword — a RUN_CITATION, three deltas", ['accepted'])
    return out('no verdict in span', [FX.NONE])


# ===== F3: THE SENTENCE (Num 31:13-18) ========================================================================
def the_sentence(case, data):
    del P[:]
    ask = case['ask']
    if ask == 'moses_wrath':
        ink('31:14', '"and Moses was wroth with the officers of the host" — %s; the wrath-verb\'s Torah tokens %s, Moses its subject at Exodus 16:20, Leviticus 10:16 and here' % (MOSES_WROTH, WROTH_TOKENS))
        move('Sifrei 157:9; Pesachim 66b:7', "ANGER BEGETS ERROR at three places — the law hidden from Moses by his anger: 'and Eleazar the priest said ... this is the statute' (31:21) — the error's evidence (Reish Lakish)")
        dat('the row anger_seats: %s' % data['anger_seats']['value'])
        return out("and Moses was wroth with the officers of the host (31:14) — anger begets error (Sifrei 157:9; Pesachim 66b:7): the law hidden, Eleazar speaks it at 31:21", ['mark_of_anger'])
    if ask == 'anger_seats':
        dat('the row anger_seats: %s (the shelf\'s three recorded)' % data['anger_seats']['value']); move('Pesachim 66b:6-9', "the scholar (Moses), the prophet (Elisha), whoever is angry is lowered (Eliab); the haughty (Hillel)")
        return out("Moses the scholar (31:14 / 31:21), Elisha the prophet (2 Kings 3:14-15), Eliab lowered (1 Samuel 17:28 / 16:7) — Pesachim 66b:6-9", ['accepted'])
    if ask == 'in_the_name_of_its_sayer':
        move('Sifrei 157:9; Megillah 15a:20', "'whoever reports a saying in the name of its sayer brings redemption to the world' — the Sifrei's closing rule at its Talmud seat (Esther 2:22); the export dropped R. Yoshiyah's name at that row (the reading's finding)")
        return out("whoever reports a saying in the name of its sayer brings redemption (Megillah 15a:20) — the Sifrei 157:9's closing rule; the export dropped R. Yoshiyah's name", ['accepted'])
    if ask == 'every_female_kept':
        ink('31:15-16', '"have you kept every female alive? behold, these were the cause, by the word of Balaam, of the children of Israel\'s treachery against the LORD in the matter of Peor" — "by the word of Balaam" %s (Onkelos "by the counsel"); "treachery against the LORD" %s (the sotah\'s 5:6 and the guilt offering\'s Lev 5:21); "in the matter of Peor" %s' % (WORD_OF_BALAAM, TREACHERY, MATTER_OF_PEOR))
        move('Sanhedrin 106a:4-16 (the Balak docket, CREDITED)', "Balaam's counsel — the daughters of Moab and Midian; the plague 25:9's twenty-four thousand (the Balak runner)")
        return out("'have you kept every female alive?' (31:15) — by the word of Balaam they were the cause of the treachery in the matter of Peor (31:16): the sotah's phrase", ['accepted'])
    if ask == 'the_sentence':
        ink('31:17-18', '"now kill every male among the little ones, and every woman who has known a man by lying with a male kill; and all the little ones among the women who have not known a man by lying with a male keep alive for yourselves" — "lying with a male" %s (Judges 21:12 the RUN_CITATION); "keep alive for yourselves" %s' % (LYING_WITH_A_MALE, KEEP_ALIVE))
        ink('31:35', '"the persons, of the women who had not known a man by lying with a male — 32,000 souls" (the parser\'s %s): THE OUTCOME DESCRIBED, the killing NEVER NARRATED — the command stays OPEN (the effects law: obligations computed, acts from the text)' % INTS[35])
        return out("every male among the little ones and every woman who has known a man killed, the little ones among the women who have not known a man kept alive (31:17-18) — a COMMAND with no narrated run: OPEN", ['commanded'])
    if ask == 'known_a_man_test':
        dat('the row known_a_man_test: %s' % data['known_a_man_test']['value']); move('Yevamot 60b:8-10; Sifrei 157:6-7', "Rav Huna's contradiction of the two verses resolved: THE VERSE SPEAKS OF ONE FIT FOR INTERCOURSE — the line at three years, not the act")
        return out("fit for intercourse — the line at three years, not the act (Yevamot 60b:9-10; Sifrei 157:6-7): the case kinds run by age", ['accepted'])
    if ask == 'frontplate_test':
        dat('the row frontplate_test: %s' % data['frontplate_test']['value']); move('Yevamot 60b:11-13', "passed before the frontplate — the sallow face; Jabesh-gilead by the barrel of wine; the frontplate for Israel's acceptance, not calamity")
        return out("passed before the frontplate — the face turned sallow (Yevamot 60b:11); Jabesh-gilead's four hundred by the barrel of wine (60b:12)", ['accepted'])
    if ask == 'proselyte_age':
        dat('the row proselyte_age: %s (the Rabbis\' arm recorded)' % data['proselyte_age']['value'])
        move('Yevamot 60b:6, 60b:7, 60b:14; Kiddushin 78a:19-21', "R. Shimon ben Yochai from 31:18 with Phinehas present; the halakha as him; the reason Ezekiel 44:22's 'virgins of the seed of the house of Israel'; the Rabbis: as slaves and maidservants")
        return out("the convert under three years and a day fit for the priesthood — R. Shimon ben Yochai from 31:18 with Phinehas present, the halakha as him (Yevamot 60b:6, 60b:14; Kiddushin 78a:19-21); the Rabbis: as slaves and maidservants", ['accepted'])
    if ask == 'punish_by_inference':
        ink('31:17', '"kill ... kill" — the verb doubled: %d tokens of הרגו ("kill") in the verse (computed)' % words(31, 17).count('הרגו'))
        dat('the row punish_by_inference: %s' % data['punish_by_inference']['value'])
        move('Sifrei 157:6; Makkot 5b:11-16; Sanhedrin 54a:17', "WE DO NOT PUNISH BY INFERENCE — the second 'kill' written because the a-fortiori could not carry the death; no prohibition, no lashes, no exile by inference; R. Yishmael's 'to close the subject'; Abaye and Rava's fork")
        return out("we do not punish by inference — the second 'kill' written (Sifrei 157:6; Makkot 5b:11-16); R. Yishmael's 'to close the subject' beside; the Abaye / Rava fork (Sanhedrin 54a:17)", ['accepted'])
    if ask == 'jabesh_gilead':
        move('Judges 21:10-12 (RUN_CITATION); Yevamot 60b:12', "twelve thousand sent, every male and every woman who knew a man devoted, four hundred virgins kept — the sentence run with its number and its phrase ('lying with a male' %s)" % LYING_WITH_A_MALE)
        return out("Judges 21:10-12 runs the sentence — twelve thousand sent, every male and every woman who knew a man devoted, four hundred virgins kept: a RUN_CITATION", ['accepted'])
    if ask == 'deuteronomy_20':
        move('Deuteronomy 20:13-14 (NOT COMPILED)', "the war law spares the women and the little ones — this chapter stricter on both (the sentence on the women who knew a man, on the male little ones); Deuteronomy 21:10-14's captive woman forward — OWED at their chapters (COMPILE_DEBT)")
        return out("Deuteronomy 20:13-14 spares the women and the little ones — this chapter stricter on both; NOT COMPILED, owed at its chapter", ['accepted'])
    return out('no verdict in span', [FX.NONE])


# ===== F4: THE PURIFICATION (Num 31:19-20 with 31:24) =========================================================
def the_purification(case, data):
    del P[:]
    ask = case['ask']
    if ask == 'outside_the_camp':
        ink('31:19', '"and you, encamp outside the camp seven days" — %s (Miriam\'s seven at 12:15 the other seat); the parser\'s %s' % (OUTSIDE_SEVEN, INTS[19]))
        move('cold_run_chukat (CALL) — CK.corpse_tumah(camps) = %s' % CK_CAMPS[0], "the corpse-impure out of the Presence's camp alone (Kelim 1:8; 5:2)")
        return out("encamp outside the camp seven days (31:19) — the corpse-impure out of the Presence's camp alone (CK.corpse_tumah camps by CALL)", ['sent_outside_the_camp'])
    if ask == 'schedule':
        ink('31:19', '"whoever has killed a soul and whoever has touched a slain one, purify yourselves on the third day and on the seventh day, you and your captives" — %s; "you and your captives" %s; the ordinal reader\'s %s' % (THIRD_AND_SEVENTH, YOU_AND_YOUR_CAPTIVES, ORDINALS[19]))
        move('cold_run_chukat (CALL) — CK.corpse_tumah(schedule) = %s' % CK_SCHEDULE[0], "THE THREE TIMERS on the men of war and on the captives: corpse_unclean_seven_days due day + %d, sprinkling_due_third_day day + %d, sprinkling_due_seventh_day day + %d — chukat's own dues (the machine counts the days that pass)" % (SEVEN, THIRD_DUE, SEVENTH_DUE))
        return out("purify yourselves on the third day and on the seventh day, you and your captives (31:19) — the three timers, chukat's dues (day + 3, day + 7)", ['corpse_unclean_seven_days', 'sprinkling_due_third_day', 'sprinkling_due_seventh_day'])
    if ask == 'seven_days_floor':
        ink('31:24', '"and you shall wash your garments on the seventh day" — the seventh named for the wash'); dat('the row camp_entry_reading: %s (the seven_days_floor arm)' % data['camp_entry_reading']['value'])
        move('Bava Kamma 25b:13; cold_run_chukat (CALL) — CK.corpse_tumah(seven_days) = %s' % CK_SEVEN[0], "Rava: a Torah edict that what a corpse defiles stays impure no less than SEVEN DAYS — the vessels' seven the men's")
        return out("wash your garments on the seventh day (31:24) — what a corpse defiles stays impure no less than seven days (Bava Kamma 25b:13); CK seven_days by CALL", ['corpse_unclean_seven_days'])
    if ask == 'sword_like_slain':
        ink('31:19, 31:22', '"whoever has touched a slain one" beside the six metals — the warriors\' metal the seat (19:16\'s "slain by the sword"; Sifrei 158:3)')
        dat('the row sword_like_slain: %s (CK\'s row READ)' % data['sword_like_slain']['value'])
        move('cold_run_chukat (CALL) — CK.corpse_tumah(sword_like_slain) = %s' % CK_SWORD[0], "Nazir 53b:11; Pesachim 14b:1, 14b:5 — metal the one substance where the corpse's and the creeping animal's impurity differ; Chullin 3a:1 the knife")
        return out("a sword is like the slain — the metal takes the corpse's grade (Nazir 53b:11; Pesachim 14b:1, 14b:5; Chullin 3a:1) — the warriors' metal the seat", ['corpse_unclean_seven_days'])
    if ask == 'captives_sprinkled':
        ink('31:19', '"you AND YOUR CAPTIVES" — the captives sprinkled: the gentile\'s corpse defiles them by touch and carrying')
        dat('the row tent_gentile: %s (CK\'s row READ — its note names the Midian war)' % data['tent_gentile']['value'])
        move('cold_run_chukat (CALL) — CK.corpse_tumah(tent_gentile) = %s' % CK_TENT[0], "Yevamot 61a:1 (no tent — 'you are men'), 61a:5 (Ravina: excluded from the tent, not from touch and carrying — hence the Midian war's purification even per R. Shimon ben Yochai)")
        return out("the captives sprinkled — gentile corpses defile by touch and carrying, not by tent (Yevamot 61a:1, 61a:5): the Midian war the proof", ['sprinkling_due_third_day', 'sprinkling_due_seventh_day'])
    if ask == 'four_materials':
        ink('31:20', '"every garment, every vessel of skin, every work of goats, every vessel of wood you shall purify" — %s against Leviticus 11:32\'s %s ON THE DB: shared %s, sack there against goat-work here' % (NUM_MATERIALS, LEV_MATERIALS, SHARED_MATERIALS))
        move('Sifrei 157:8', "the freed-word identity of the two lists — what is said here is said there: the spun and woven, the vessels of skin and wood")
        return out("garment, vessel of skin, goat-work, vessel of wood (31:20) against Leviticus 11:32's wood, garment, skin, sack — three shared, sack there against goat-work here (computed on the DB)", ['accepted'])
    if ask == 'goat_work_reading':
        dat('the row goat_work_reading: %s' % data['goat_work_reading']['value'])
        move('Shabbat 64a:2-4, 64a:9; Chullin 25b:4; Sifrei 157:8', "spun and woven — the sack; reins and the belly band; the tails; horn and hoof in, birds' bones out")
        return out("spun and woven — the sack (Shabbat 64a:3; Sifrei 157:8); reins and the belly band (64a:4), the tails (64a:9), horn and hoof in, birds' bones out (Chullin 25b:4)", ['accepted'])
    if ask == 'the_transfer':
        move('Shabbat 64a:7-8, 64a:15; Bava Kamma 25b:6', "THE VERBAL ANALOGY 'garment and leather' between Leviticus 11:32 and Numbers 31:20 run both ways — as there only the spun and woven, so here; as here all work of goats, so there: THE TEACHER of the edge midian -> shemini (link: transfer); the free-word condition argued (64a:16-19)")
        return out("the verbal analogy garment / leather between Leviticus 11:32 and Numbers 31:20 run both ways (Shabbat 64a:7-8, 64a:15; Bava Kamma 25b:6) — the edge midian to shemini a TRANSFER taught; the free-word condition argued (64a:16-19)", ['accepted'])
    if ask == 'carcass_grade':
        move('cold_run_shemini (CALL) — SH.touch_effect(touch_carcass) = %s, (carry_carcass) = %s' % (SH_TOUCH[0], SH_CARRY[0]), "the carcass grade at Leviticus 11:24-25; THE LEVITICUS 11 RUNNER HAS NO VESSELS CELL — 11:32's list compared on the DB here, the cell OWED (COMPILE_DEBT)")
        return out("the carcass grade by call — touch impure until evening, carry wash and evening (Lev 11:24-25); the vessels' cell in shemini OWED", ['accepted'])
    if ask == 'camp_entry_reading':
        ink('31:24', '"and you shall wash your garments on the seventh day and be clean; and afterward you shall come into the camp" against 19:19\'s "and he shall be clean at evening"')
        dat('the row camp_entry_reading: %s' % data['camp_entry_reading']['value']); move('Sifrei 158:3', "the two-way likening — the camp after the wash, the purity at evening")
        return out("wash on the seventh day, be clean, then come into the camp (31:24) against 19:19's evening — Sifrei 158:3's two-way likening", ['declared_pure'])
    if ask == 'removes':
        move('cold_run_chukat (CALL) — CK.corpse_tumah(removes) = %s' % CK_REMOVES[0], "the vessel's toucher until evening (Nazir 54b:6; Mishnah Oholot 1:2-3) — the remove after the vessel is the evening's")
        return out("the vessel's toucher until evening (Nazir 54b:6; Oholot 1:2-3) — the removes by call", ['accepted'])
    if ask == 'receptacles':
        move('Mishnah Kelim 15:1', "vessels of wood, leather, bone or glass: flat clean, receptacles susceptible; broken clean; the forty-se'ah vessels clean")
        return out("vessels of wood and skin as receptacles (Mishnah Kelim 15:1) — the flat ones outside", ['accepted'])
    return out('no verdict in span', [FX.NONE])


# ===== F5: THE VESSELS — ELEAZAR'S STATUTE (Num 31:21-23) =====================================================
def the_vessels(case, data):
    del P[:]
    ask = case['ask']
    if ask == 'statute_head':
        ink('31:21', '"and Eleazar the priest said to the men of war who had gone to the battle: this is the statute of the Torah which the LORD commanded Moses" — %s (19:2 the heifer\'s head); the frame verbs %s: the priest\'s voice citing Moses' % (STATUTE_HEAD, FRAME_VERBS[3]))
        return out("this is the statute of the Torah (31:21) — 19:2's head, Eleazar speaking it: the third relayed form", ['commanded'])
    if ask == 'eleazar_before_his_teacher':
        move('Eruvin 63a:24', "R. Eliezer: who rules before his teacher is lowered — Eleazar's 'this is the statute' spoken in Moses' presence, though he said 'commanded to my father's brother, not to me'; Pesachim 66b:7 the same pair from the anger's side")
        return out("Eleazar lowered for ruling before his teacher (Eruvin 63a:24) — the relay a fault on the shelf; the installed_by class's witness", ['accepted'])
    if ask == 'installed_by':
        ink('31:21', 'no divine frame on the statute — Eleazar cites "which the LORD commanded Moses"; the chapter\'s frames %s' % [f[:2] for f in FRAME_VERBS])
        move('THE LOOP step 3 (installation_parameters.yaml); Menachot 77b:20', "BOOT with the class named — THE THIRD RELAYED FORM (the priest's voice citing Moses; 30:2's relay in Moses' voice; 36:6's relayed output); the installing acts erect institutions and the priest's relay erects none; the division's rates 'not for all generations' — the second pass (D2) decides")
        return out("installed_by boot — the priest's voice citing the LORD's command to Moses: the third relayed form, the class named; the second pass decides", ['accepted'])
    if ask == 'six_metals':
        ink('31:22', '"the gold, the silver, the bronze, the iron, the tin and the lead" — %s, every one with its article; the tin %s, the lead %s' % (METALS, TIN, LEAD))
        move('Shabbat 16b:2; Mishnah Kelim 11:1', "metal vessels impure BY TORAH LAW from this list; recast they revert (the Sages' decree — CK.corpse_tumah(metal_vessels_decree) READ: %s)" % CK_METAL[0])
        return out("gold, silver, bronze, iron, tin, lead (31:22) — tin's one Torah seat, lead's two; metal vessels impure by Torah law (Shabbat 16b:2; Kelim 11:1)", ['accepted'])
    if ask == 'kashering':
        material, use = case.get('material', 'metal'), case.get('use', 'fire')
        ink('31:23', '"everything that comes into the fire you shall pass through the fire and it shall be clean, only with the water of sprinkling it shall be purified; and everything that does not come into the fire you shall pass through water" — %s / %s: the ink\'s TWO branches' % (PASS_THROUGH_FIRE, WATER_OF_SPRINKLING))
        if material == 'earthenware':
            move('Pesachim 30b:8, 30b:2', "Ameimar: earthenware NEVER leaves its defective state — 'the Torah testified: broken' (Leviticus 6:21); the six metals the rule's whole class")
            return out("earthenware never purged — the Torah testified: broken (Leviticus 6:21; Pesachim 30b:8); the six metals the rule's whole class", ['exempt'])
        if use == 'fire':
            dat('the row immersion_source: %s' % data['immersion_source']['value'])
            return out("what comes into the fire — through the fire, and with the water of sprinkling purified (31:23): the first branch; the immersion added by the shelf", ['declared_pure', 'immersed'])
        return out("what does not come into the fire — through water (31:23): the second branch", ['immersed'])
    if ask == 'kashering_modes':
        dat('the row kashering_modes: %s' % data['kashering_modes']['value'])
        move('Mishnah Avodah Zarah 5:12 (= 75b:6); Avodah Zarah 75b:17, 76a:17, 76b:1-2; Pesachim 30b:5-6', "whiten the spit and the grill, boil the pot and the kettle, polish the knife — and immerse all; the baraita's four uses; as it absorbs so it emits")
        return out("whiten the spit and the grill, boil the pot and the kettle, polish the knife — and immerse all (Mishnah Avodah Zarah 5:12; the baraita's four uses, 75b:17)", ['immersed'])
    if ask == 'immersion_source':
        dat('the row immersion_source: %s' % data['immersion_source']['value'])
        move('Avodah Zarah 75b:7-11; Sifrei 158:2', "Rava: 'and it shall be pure' adds immersion in forty se'ah; Bar Kappara: 'nevertheless' excludes the third and seventh day's sprinkling — the water of niddah the menstruant's; the Sifrei's a-fortiori beside")
        return out("'and it shall be pure' adds immersion in forty se'ah (Rava, Avodah Zarah 75b:7); 'nevertheless' excludes the third and seventh day's sprinkling (Bar Kappara, 75b:8); the Sifrei 158:2's a-fortiori beside", ['immersed'])
    if ask == 'water_of_sprinkling':
        ink('31:23', '"only with the water of sprinkling it shall be purified" — %s here; the purify-verb\'s seats %s, all in 19 and 31' % (WATER_OF_SPRINKLING, PURIFY_3))
        move('cold_run_chukat (CALL) — CK.corpse_tumah(metal_vessels_decree) = %s' % CK_METAL[0], "the heifer's water by call; the shelf splits the phrase's sense — the menstruant's immersion water (Avodah Zarah 75b:9)")
        return out("the water of niddah — four Torah seats all in 19 and 31; the heifer's water by call: metal vessels keep their impurity until the sprinkling (Shabbat 16b); the shelf splits its sense (75b:9)", ['accepted'])
    if ask == 'same_day_pot':
        dat('the row kashering_modes (the same_day_pot arm): %s' % data['kashering_modes']['settings']['same_day_pot'][:60])
        move('Avodah Zarah 75b:21-76a:2; Pesachim 44b:15', "the Torah forbids only a pot used that same day; the rest a rabbinic fence")
        return out("the Torah forbids only a pot used that same day (Avodah Zarah 75b:21; Pesachim 44b:15); the rest a fence", ['accepted'])
    if ask == 'taste_as_substance':
        move('Nazir 37b:1; Pesachim 44b:13-16; Avodah Zarah 67b:6', "R. Akiva derives THE TASTE AS THE SUBSTANCE from the vessels of Midian; the Rabbis: the purging a NOVELTY — a taste that taints forbidden here alone; R. Meir's detriment principle on the same verses")
        return out("the taste as the substance from the vessels of Midian (R. Akiva — Nazir 37b:1; Pesachim 44b:13); the Rabbis: the purging a NOVELTY (44b:14)", ['accepted'])
    if ask == 'immersion_scope':
        dat('the row immersion_source (the scope arm): %s' % data['immersion_source']['settings']['scope'])
        move('Avodah Zarah 75b:12-15', "metal utensils alone; purchased as the captured were, not borrowed; even new; glass as metal; meal utensils")
        return out("metal utensils (75b:14), purchased as the captured (75b:13), even new (75b:12), glass as metal (75b:15) — the immersion's scope the passage's own", ['immersed'])
    if ask == 'as_it_absorbs':
        move('Avodah Zarah 76a:17, 76b:1; Pesachim 30b:6', "AS IT ABSORBS SO IT EMITS — Rava on Rav Akavya's cauldron; the measures: until the outer layer sheds, a kettle in a kettle")
        return out("as it absorbs so it emits (Avodah Zarah 76b:1; Pesachim 30b:6); the measures — until the outer layer sheds, a kettle in a kettle (76a:17)", ['accepted'])
    if ask == 'the_line':
        ink('31:21-24', "ONE line on the tape for the statute — Eleazar's speech at the counter's day, no marker; commanded on the men of war")
        return out("commanded on the men of war valued the_statute_of_the_vessels — the walk's form for a statute line (10b's commanded on israel)", ['commanded'])
    return out('no verdict in span', [FX.NONE])


# ===== F6: THE DIVISION (Num 31:25-47) ========================================================================
def the_division(case, data):
    del P[:]
    ask = case['ask']
    if ask == 'lift_the_head':
        ink('31:26', '"take the sum of the prey of the captives, of man and of beast, you and Eleazar the priest and the heads of the fathers\' houses of the congregation" — %s the singular imperative, one seat; Exodus 30:12\'s %s' % (LIFT_THE_HEAD, WHEN_YOU_LIFT))
        move('cold_run_incense_shekel (CALL) — IS.shekel(lift_head) = %s' % IS_LIFT, "the census idiom's seats named there — a REFERENCE by the shared words")
        return out("take the sum of the prey (31:26) — 'lift the head', the census idiom (Exod 30:12 by call), the singular imperative one seat", ['accepted'])
    if ask == 'halve':
        ink('31:27', '"and halve the prey between those who took the war, who went out to the army, and all the congregation" — the equal halves; the halving computed: %s // 2 = %s' % (TOTALS, WARRIORS))
        move('1 Samuel 30:24-25; Joshua 22:8 (OBSERVED)', "David's statute at Ziklag — 'as his share who goes down to the battle, so his share who stays by the baggage'; Joshua's 'divide the spoil with your brothers' — NO ROW OF THE DECLARED SHELF LINKS them to 31:27 (the docket found none): observed, not linked (THE LINK REVIEW LAW)")
        return out("halve the prey between those who took the war and all the congregation (31:27) — the equal halves; David's statute (1 Samuel 30:24-25) OBSERVED, no link on the declared shelf", ['accepted'])
    if ask == 'tribute_rate':
        ink('31:28-29', '"and levy a tribute to the LORD from the men of war who went out to the army: one soul of five hundred, of the persons, the cattle, the donkeys and the flock; from their half you shall take it and give it to Eleazar the priest, the LORD\'s heave-offering" — %s; THE RATE %s the parser\'s read (the one marked, the denominator starred); the tribute-word %s; "the LORD\'s heave-offering" %d seats' % (ONE_OF_FIVE_HUNDRED, TRIBUTE_RATE, TRIBUTE_TOKENS, len(HEAVE_OFFERING)))
        dat('the row tribute_rate_reading: %s' % data['tribute_rate_reading']['value']); move('Menachot 77b:20; Yoma 24a:5', "not one of ten and not for all generations; asked as a measure for the ash removal")
        return out("one soul of five hundred (31:28) — the rate Fraction(1, 500), the parser's read; not one of ten and not for all generations (Menachot 77b:20); asked as a measure (Yoma 24a:5)", ['heave_offering_given'])
    if ask == 'levites_rate':
        ink('31:30', '"and from the half of the children of Israel you shall take one held of fifty, of the persons, the cattle, the donkeys and the flock, of all the beasts, and give them to the Levites who keep the charge of the tabernacle of the LORD" — %s; THE RATE %s' % (ONE_HELD_OF_FIFTY, LEVITE_RATE))
        dat('the row levites_rate_reading: %s' % data['levites_rate_reading']['value']); move('Jerusalem Talmud Terumot 4:3:2; Mishnah Terumot 4:3', "R. Levi: 'all you take elsewhere shall be like this' — the terumah's average fiftieth FROM THIS VERSE: a TRANSFER taught")
        return out("one held of fifty (31:30) — Fraction(1, 50); the terumah's average rate (Mishnah Terumot 4:3; Jerusalem Talmud Terumot 4:3:2 — R. Levi from this verse): a TRANSFER taught", ['levites_portion_given'])
    if ask == 'levites_charge':
        ink('31:30, 31:47', '"the Levites who keep the charge of the tabernacle of the LORD" — %s; 1:53\'s charge' % KEEP_THE_CHARGE)
        move('cold_run_bamidbar (CALL) — BM.charges(houses_charges) = %s' % BM_CHARGES[0], "1:50-53's charge_kept on the Levites' ledger (the census daemon's) — a REFERENCE by the shared words")
        return out("to the Levites who keep the charge of the tabernacle of the LORD (31:30, 31:47) — 1:53's charge (BM.charges by call: gershon the woven, kohath the holy, merari the frame)", ['accepted'])
    if ask == 'three_debits':
        ink('31:26-30 / 31:31, 31:41, 31:47', 'ONE speech, THREE commands — the count and the halving (31:26-27), the tribute to the priest (31:28-29), the Levites\' share (31:30); THREE RECEIPTS "as the LORD commanded Moses" at %s' % [s for s in RECEIPT if s in ('Num 31:31', 'Num 31:41', 'Num 31:47')])
        return out("three commands in one speech — divide the prey, the tribute to the priest, the Levites' share — closed by value at 31:31, 31:41, 31:47", ['commanded'])
    if ask == 'the_count':
        ink('31:32-35', '"the prey, the rest of the plunder which the people of the army took: sheep %d, cattle %d, donkeys %d, persons %d" — the parser\'s numbers; every total a multiple of a thousand' % TOTALS)
        return out("the prey: 675,000 sheep, 72,000 cattle, 61,000 donkeys, 32,000 persons (31:32-35) — the parser's numbers, every total a multiple of a thousand", ['counted'])
    if ask == 'the_halving_check':
        ink('31:36, 31:43', '"the half, the portion of those who went out to the army" %s = "the half of the congregation" %s (%s one seat) = the totals halved — CHECK' % (WARRIORS, CONGREGATION, HALF_OF_THE_CONGREGATION))
        return out("the totals halved = the warriors' portion = the congregation's half: 337,500 / 36,000 / 30,500 / 16,000 (31:36-46) — CHECK", ['counted'])
    if ask == 'the_tribute_check':
        ink('31:37-41', '"the tribute to the LORD" %s = the warriors\' portion x %s — %d heads; "and Moses gave the tribute, the LORD\'s heave-offering, to Eleazar the priest, as the LORD commanded Moses" (31:41)' % (TRIBUTE, TRIBUTE_RATE, sum(TRIBUTE)))
        return out("the warriors' portion at one of five hundred = the tribute: 675 / 72 / 61 / 32 = 840 heads (31:37-40) — CHECK; given to Eleazar (31:41)", ['counted', 'heave_offering_given'])
    if ask == 'the_levites_share':
        ink('31:42-47', 'THE SHARE STATED AS A RATE AND NEVER AS A NUMBER — the congregation\'s half %s x %s = %s = %d heads COMPUTED, UNWRITTEN; ten times the priest\'s %d; "and Moses took ... the held one of fifty, of man and of beast, and gave them to the Levites" (31:47)' % (CONGREGATION, LEVITE_RATE, LEVITES, sum(LEVITES), sum(TRIBUTE)))
        return out("the congregation's half at one of fifty = 6,750 / 720 / 610 / 320 = 8,400 heads — COMPUTED, UNWRITTEN; ten times the priest's; given to the Levites (31:47)", ['levites_portion_given'])
    if ask == 'thing_parties':
        ink('31:32, 31:36, 31:37, 31:43', 'the ink\'s own nouns for the four counted things — the prey (המלקוח, %d seats), the portion of those who went out (חלק היצאים בצבא), the tribute (המכס), the half of the congregation (מחצת העדה)' % len(PREY_TOKENS))
        move('world_engine._write (ent.status[effect] = value)', "a counted STATUS overwrites — the sixteen values go on four thing parties, never on israel_people (601,730) or the Levites (23,000)")
        return out("the sixteen counted statuses on four thing parties — the prey, the warriors' portion, the tribute, the congregation's half — never on israel_people or the Levites (the status overwrite)", ['counted'])
    if ask == 'private_plunder':
        ink('31:53', '"the men of the host had taken spoil, every man for himself" — outside the count (the prey "the rest of the plunder", 31:32)')
        return out("the men of the host had taken spoil every man for himself (31:53) — outside the count", ['accepted'])
    if ask == 'register_gate':
        move('THE REGISTER GATE (register_census.py --strict)', "the four count lines (31:35, 31:36, 31:40, 31:46) LEDGER by the counted statuses on the thing parties; the four receipts (31:7, 31:31, 31:41, 31:47) CLOSE by the notes; 31:28's rate a MEASURE (register_probes R7 — a Fraction leaves the count census); the footer Num 36:13 DAEMONS by law_midian's given_at")
        return out("the four count lines LEDGER by the counted statuses; the four receipts CLOSE; the rate a MEASURE (R7); the footer's block DAEMONS", ['accepted'])
    if ask == 'terumah_measure':
        dat('the row levites_rate_reading (the no_torah_measure arm): %s' % data['levites_rate_reading']['settings']['no_torah_measure'][:80]); move('Jerusalem Talmud Terumot 4:3:8', "R. Yonatan one in a hundred, R. Yannai one in a thousand, R. Mana no measure")
        return out("the Torah's own measure of terumah none (Jerusalem Talmud Terumot 4:3:8) — the rates the shelf's settings, the ink's fiftieth a one-time instruction", ['accepted'])
    return out('no verdict in span', [FX.NONE])


# ===== F7: THE OFFICERS' GOLD (Num 31:48-54) ==================================================================
def the_gold(case, data):
    del P[:]
    ask = case['ask']
    if ask == 'the_count':
        ink('31:48-49', '"the officers over the thousands of the army, the captains of thousands and the captains of hundreds, came near to Moses and said: your servants have lifted the head of the men of war under our hand, and not one man of us is missing" — %s; %s; Jethro\'s grades (Exodus 18:21, 25) the army\'s ranks' % (LIFTED_THE_HEAD, NONE_MISSING))
        move('cold_run_incense_shekel (CALL) — IS.shekel(plague_clause) = %s' % IS_PLAGUE['fx'], "the count taken with none missing — the shekel engine's clause: no plague at the counting")
        return out("the officers of thousands and of hundreds lifted the head of the men of war — not one man of us is missing (31:49): Jethro's grades the army's ranks; the count with none missing", ['no_plague_at_counting'])
    if ask == 'ransom_at_a_count':
        ink('31:49-50, 31:54', '"lift the head" %s / Exodus 30:12 %s; "to atone for our souls before the LORD" %s / "for your souls" %s; "a memorial ... before the LORD" %s / %s — EXODUS 30:12-16\'S OWN WORDS (computed)' % (LIFTED_THE_HEAD, WHEN_YOU_LIFT, ATONE_OUR_SOULS, ATONE_YOUR_SOULS, MEMORIAL, MEMORIAL_EXOD))
        move('cold_run_incense_shekel (CALL) — IS.shekel(lift_head) = %s, (atone_souls) = %s, (silver_of_atonements) = %s' % (IS_LIFT, IS_ATONE, IS_SILVER), "THE OFFICERS' GOLD RUNS THE RANSOM OF EXODUS 30 AT A COUNT — a REFERENCE by three shared phrases; the row trigger_parameter = %s" % data['trigger_parameter']['value'])
        return out("to atone for our souls before the LORD (31:50) — Exodus 30:12-16's own words (lift the head, atone for your souls, a memorial): the ransom of Exodus 30 run at a count; no plague at the counting", ['no_plague_at_counting', 'atoned_forgiven'])
    if ask == 'atonement_reading':
        dat('the row atonement_reading: %s (the eyes\' thoughts and the moral count recorded)' % data['atonement_reading']['value'])
        move('Shabbat 64a:22-64b:2; Yevamot 61a:4; Berakhot 24a:15', "'then why atonement?' — the thoughts of transgression; the eyes nourished from nakedness; R. Shimon: missing to transgression")
        return out("the ransom at a count (the ink) / the eyes' thoughts of transgression (Shabbat 64a:22-64b:2) — both arms; R. Shimon's moral count (Yevamot 61a:4)", ['atoned_forgiven'])
    if ask == 'ornaments':
        ink('31:50-51', '"every man what he found, vessels of gold: the armlet, the bracelet, the ring, the earring and the kumaz" — %s in the ink\'s order; "all vessels of workmanship" (31:51)' % ORNAMENTS)
        dat('the row ornaments_reading: %s' % data['ornaments_reading']['value']); move('Shabbat 64a:20-21, 60a:3, 63b:6, 63b:19', "agil the breast-mold, kumaz the womb-mold; the kumaz in Aramaic; vessels for impurity")
        return out("armlet, bracelet, ring, earring, kumaz (31:50) — agil the breast-mold, kumaz the womb-mold (Shabbat 64a:20-21); vessels for impurity (31:51 — Shabbat 60a:3, 63b:19)", ['accepted'])
    if ask == 'ornaments_impure':
        move('Shabbat 63b:6, 60a:3, 63b:19', "Rav Yosef: the bracelet impure — 31:50's ornaments beside 31:19's 'purify yourselves'; 'all vessels with which labor is done' (31:51) — a ring with a seal, a woven fabric of any size")
        return out("the bracelet impure — 31:50 beside 31:19 (Shabbat 63b:6); all vessels with which labor is done (31:51) the class's definition (60a:3, 63b:19)", ['accepted'])
    if ask == 'gold_weight':
        ink('31:52', '"all the gold of the heave-offering which they offered to the LORD was sixteen thousand seven hundred and fifty shekels, from the captains of thousands and from the captains of hundreds" — the parser\'s %d; %s one seat; the captains no number (census_probes G3); Onkelos\' selas' % (GOLD, GOLD_PHRASE))
        return out("sixteen thousand seven hundred and fifty shekels (31:52) — the parser's 16,750; the captains no number", ['memorial_before_the_lord'])
    if ask == 'memorial':
        ink('31:54', '"and Moses and Eleazar the priest took the gold from the captains of thousands and of hundreds and brought it into the tent of meeting, a memorial for the children of Israel before the LORD" — %s; Exodus 30:16\'s %s in another order; "the LORD\'s offering" (31:50) %s' % (MEMORIAL, MEMORIAL_EXOD, OFFERING_OF_THE_LORD))
        move('Temurah 13a:14', "'the LORD's offering', not 'an offering TO the LORD' — the tent, not the altar (the noun's form decides the destination)")
        return out("brought into the tent of meeting, a memorial for the children of Israel before the LORD (31:54) — Exodus 30:16's six words in another order; the LORD's offering, not an offering to the LORD: the tent, not the altar (Temurah 13a:14)", ['memorial_before_the_lord'])
    if ask == 'not_one_missing_reading':
        dat('the row atonement_reading (the moral_count arm): %s' % data['atonement_reading']['settings']['moral_count'][:70]); move('Yevamot 61a:4', "the Rabbis: the casualty count — no Jew fell, the corpses gentile; R. Shimon ben Yochai: missing to transgression")
        return out("the Rabbis: the casualty count — no Jew fell (the corpses gentile); R. Shimon ben Yochai: missing to transgression (Yevamot 61a:4)", ['accepted'])
    return out('no verdict in span', [FX.NONE])


# ---- THE WRAP — the daemon, the scene, the narrative ------------------------------------------------------
def law_midian(event, world):
    """Num 31:1-54 (cold_run_midian.py F1-F7). given_at Num 31:21; installed_by boot — THE THIRD RELAYED FORM (a statute in the PRIEST'S
    voice citing the LORD's command to Moses; the class named in the registry, the second pass decides). THIRTEEN TAPE LINES: the vengeance
    commanded (a DEBIT on Moses), the muster counted and the trumpets' debit CLOSED BY VALUE (a run by carrying), the war's receipt closing
    the two vengeance debits and writing NOTHING, the kings and Balaam slain, the captives / the spoil / the cities, Moses' wrath and THE
    SENTENCE (a debit OPEN forever — no narrated run), the purification's status and SIX TIMERS (chukat's dues on the men and on the
    captives), Eleazar's statute, the division's THREE DEBITS and their three receipts, the sixteen counted statuses on four thing parties,
    the two transfers, the officers' gold as the ransom at a count. The exam's six case kinds dispatch to the cells with LITERAL effects per
    kind (2b's form — an unnamed effect is a KeyError)."""
    k, src = event['kind'], event['case_source']
    E_ = lambda eff, s, cp=None, amount=None, due=None, law='', value=None: {'effect': eff, 'subject': s, 'counterparty': cp, 'amount': amount, 'due': due, 'value': value if value is not None else True, 'source_law': law, 'case_source': src}
    day = event.get('day', world.clock.day)      # THE SEQUENTIAL RUN: the event's own day
    # ---- the thirteen lines (page_order at the counter's day, no marker in the chapter) ----
    if k == 'midian_vengeance_commanded':
        return [E_('commanded', 'moses', value='avenge_the_midianites', law='F1 [INK 31:1-2 "avenge the vengeance of the children of Israel from THE MIDIANITES; afterward you shall be gathered to your people" — the debit on Moses beside the Balak runner\'s harass_the_midianites (25:17: the command and its run share the word); closed by value at 31:7\'s receipt]')]
    if k == 'midian_army_mustered':
        world.close('moses', 'commanded', 'Num 31:6 — the trumpets of the alarm in Phinehas\'s hand: 10:2\'s making implied by the run and never narrated — A RUN BY CARRYING; no sounding narrated, nothing written for the alarm (10:9\'s war clause the reference, BH.trumpets by CALL)', value='the_trumpets')
        return [E_('counted', 'the-men-of-war', value=MUSTER, law='F1 [INK 31:4-5 "a thousand to a tribe, a thousand to a tribe ... twelve thousand armed for the army" — 1,000 x 12 the ink\'s own product (the row muster_count: R. Yishmael\'s 24,000 recorded); Levi in (the row levi_in_the_muster); "delivered" (the row delivered_how); 31:6 Phinehas the priest anointed for war with the holy vessels (the row holy_vessels) and the trumpets]')]
    if k == 'midian_warred':
        world.close('israel', 'commanded', 'Num 31:7 — and they warred against Midian AS THE LORD COMMANDED MOSES: the receipt closes the Balak runner\'s harass_the_midianites (25:17) BY VALUE — the debit "OPEN to 31:7" in its own note', value='harass_the_midianites')
        world.close('moses', 'commanded', 'Num 31:7 — and they warred against Midian as the LORD commanded Moses: the receipt closes 31:2\'s avenge_the_midianites BY VALUE', value='avenge_the_midianites')
        return []                                                              # NO WRITE — the closes are the line's work (the register gate's 31:7 turns CLOSE)
    if k == 'kings_and_balaam_slain':
        return [E_('slain', 'the-kings-of-midian', cp='israel', value='%s — the five kings of Midian (31:8), Zur among them (Cozbi\'s father, 25:15; BK.DATA[cozbi_and_zur] = %s); Joshua 13:21 the RUN_CITATION' % (' '.join(KINGS_NAMES), DATA['cozbi_and_zur']['value']), law='F2 [INK 31:8 "and the kings of Midian they killed with their slain: Evi, Rekem, Zur, Hur and Reba, the five kings of Midian" — the parser\'s [5]; one party on the ledger]'),
                E_('slain', 'balaam', cp='israel', value=DATA['balaam_death']['value'], law='F2 [INK 31:8 "and Balaam son of Beor they killed with the sword" — BK.DATA[balaam_death] READ by CALL: come for his wages (Sanhedrin 106a:16), the four court modes recorded (106b:1); the ass\'s sword clause (22:29) a crown, no entry of its own]')]
    if k == 'captives_and_spoil_taken':
        return [E_('taken_captive', 'the-captives-of-midian', cp='israel', value='the women of Midian and their little ones (31:9)', law='F2 [INK 31:9 "and the children of Israel took captive the women of Midian and their little ones" — Lot\'s effect (Genesis 14); the sentence of 31:17-18 falls on this party]'),
                E_('spoil_taken', 'israel', cp='the-midianites', value='all their cattle, all their flocks and all their goods (31:9)', law='F2 [INK 31:9 "and all their cattle, and all their flocks, and all their goods they took as spoil" — Shechem\'s effect (Genesis 34); 31:11-12 the prey and the spoil brought to Moses at the plains of Moab]'),
                E_('burned_in_fire', 'the-midianites', value='all their cities in their dwellings and all their castles (31:10)', law='F2 [INK 31:10 "and all their cities in their dwellings and all their castles they burned with fire" — the row castles_reading (Onkelos\' houses of worship); the Midianites a counterparty until now, written on here]')]
    if k == 'moses_wroth_at_the_officers':
        return [E_('mark_of_anger', 'moses', cp='the-officers-of-the-host', value='and Moses was wroth with the officers of the host (31:14) — ANGER BEGETS ERROR: the statute in Eleazar\'s mouth at 31:21 (Sifrei 157:9; Pesachim 66b:7)', law='F3 [INK 31:14 — the wrath-verb with Moses as subject at three Torah seats (the row anger_seats); MOVE Sifrei 157:9 "in the name of its sayer" (Megillah 15a:20)]'),
                E_('commanded', 'the-officers-of-the-host', value='the_sentence_on_the_captives', law='F3 [INK 31:17-18 "now kill every male among the little ones, and every woman who has known a man by lying with a male kill; and all the little ones among the women who have not known a man by lying with a male keep alive for yourselves" — A COMMAND WITH NO NARRATED RUN: OPEN forever; 31:35 names the outcome ("the women who had not known a man", 32,000) and never the killing; the rows known_a_man_test, frontplate_test, proselyte_age, punish_by_inference]')]
    if k == 'warriors_purification_commanded':
        return [E_('sent_outside_the_camp', 'the-men-of-war', value='encamp outside the camp seven days (31:19) — the corpse-impure out of the Presence\'s camp alone (CK.corpse_tumah camps by CALL)', law='F4 [INK 31:19 "and you, encamp outside the camp seven days: whoever has killed a soul and whoever has touched a slain one" — Miriam\'s seven at 12:15 the phrase\'s other seat]'),
                E_('corpse_unclean_seven_days', 'the-men-of-war', amount=SEVEN, due=day + SEVEN, value='unclean seven days — whoever has killed a soul, whoever has touched a slain one (31:19); the sword like the slain (the row sword_like_slain)', law='F4 [INK 31:19; CK.corpse_tumah(seven_days) by CALL — the TIMER due day + 7, chukat\'s own due]'),
                E_('sprinkling_due_third_day', 'the-men-of-war', due=day + THIRD_DUE, value='purify yourselves on the third day (31:19)', law='F4 [INK 31:19 "on the third day and on the seventh day" — 19:12, 19:19\'s schedule; CK.corpse_tumah(schedule) by CALL — the TIMER due day + 3]'),
                E_('sprinkling_due_seventh_day', 'the-men-of-war', due=day + SEVENTH_DUE, value='purify yourselves on the seventh day; wash your garments on the seventh day and be clean, afterward come into the camp (31:19, 31:24)', law='F4 [INK 31:19, 31:24 — the row camp_entry_reading (Sifrei 158:3); CK.corpse_tumah(schedule) by CALL — the TIMER due day + 7]'),
                E_('corpse_unclean_seven_days', 'the-captives-of-midian', amount=SEVEN, due=day + SEVEN, value='you AND YOUR CAPTIVES (31:19) — the gentile\'s corpse defiles by touch and carrying, not by tent (the row tent_gentile; Yevamot 61a:5 the Midian war)', law='F4 [INK 31:19 "you and your captives" — CK.DATA[tent_gentile] READ by CALL; the TIMER due day + 7]'),
                E_('sprinkling_due_third_day', 'the-captives-of-midian', due=day + THIRD_DUE, value='the captives sprinkled on the third day (31:19)', law='F4 [INK 31:19 — CK.corpse_tumah(schedule) by CALL; the TIMER due day + 3]'),
                E_('sprinkling_due_seventh_day', 'the-captives-of-midian', due=day + SEVENTH_DUE, value='the captives sprinkled on the seventh day (31:19)', law='F4 [INK 31:19 — CK.corpse_tumah(schedule) by CALL; the TIMER due day + 7]')]
    if k == 'vessels_statute_spoken':
        return [E_('commanded', 'the-men-of-war', value='the_statute_of_the_vessels — Num 31:21-23', law='F5 [INK 31:21-23 "and Eleazar the priest said to the men of war who had gone to the battle: this is the statute of the Torah which the LORD commanded Moses — the gold, the silver, the bronze, the iron, the tin and the lead: everything that comes into the fire you shall pass through the fire and it shall be clean, only with the water of sprinkling it shall be purified; and everything that does not come into the fire you shall pass through water" — THE THIRD RELAYED FORM (installed_by boot, the class named); the rows kashering_modes, immersion_source; 31:20\'s four materials against Leviticus 11:32\'s (the edge shemini, a transfer taught)]')]
    if k == 'prey_division_commanded':
        return [E_('commanded', 'moses', value='divide_the_prey', law='F6 [INK 31:26-27 "take the sum of the prey of the captives, of man and of beast, you and Eleazar the priest and the heads of the fathers\' houses of the congregation; and halve the prey between those who took the war, who went out to the army, and all the congregation" — "lift the head" the census idiom (IS.shekel by CALL); the equal halves; closed by value at 31:31]'),
                E_('commanded', 'moses', value='the_tribute_to_the_priest', law='F6 [INK 31:28-29 "and levy a tribute to the LORD from the men of war who went out to the army: ONE SOUL OF FIVE HUNDRED, of the persons, the cattle, the donkeys and the flock; from their half you shall take it and give it to Eleazar the priest, the LORD\'s heave-offering" — THE RATE Fraction(1, 500), the parser\'s ratio class; the row tribute_rate_reading; closed by value at 31:41]'),
                E_('commanded', 'moses', value='the_levites_share', law='F6 [INK 31:30 "and from the half of the children of Israel you shall take ONE HELD OF FIFTY, of the persons, the cattle, the donkeys and the flock, of all the beasts, and give them to the Levites who keep the charge of the tabernacle of the LORD" — THE RATE Fraction(1, 50); 1:53\'s charge (BM.charges by CALL); the row levites_rate_reading (the terumah\'s average, a transfer taught); closed by value at 31:47]')]
    if k == 'prey_counted':
        world.close('moses', 'commanded', 'Num 31:31 — and Moses and Eleazar the priest did as the LORD commanded Moses: the count and the halving run (31:32-36)', value='divide_the_prey')
        return [E_('counted', 'the-prey', value=TOTALS[0], law='F6 [INK 31:32 "and the prey, the rest of the plunder which the people of the army took, was: sheep six hundred and seventy-five thousand" — the parser\'s 675,000; the thing party the ink\'s own noun (המלקוח "the prey", four seats)]'),
                E_('counted', 'the-prey', value=TOTALS[1], law='F6 [INK 31:33 "and cattle seventy-two thousand" — the parser\'s 72,000]'),
                E_('counted', 'the-prey', value=TOTALS[2], law='F6 [INK 31:34 "and donkeys sixty-one thousand" — the parser\'s 61,000]'),
                E_('counted', 'the-prey', value=TOTALS[3], law='F6 [INK 31:35 "and the persons, of the women who had not known a man by lying with a male, all the souls thirty-two thousand" — the parser\'s 32,000; the sentence\'s outcome described, its run never narrated; THE REGISTER GATE\'s count line 31:35 turns LEDGER by this status]')]
    if k == 'tribute_given':
        world.close('moses', 'commanded', 'Num 31:41 — and Moses gave the tribute, the LORD\'s heave-offering, to Eleazar the priest, as the LORD commanded Moses: the transfer run', value='the_tribute_to_the_priest')
        return [E_('counted', 'the-warriors-portion', value=WARRIORS[0], law='F6 [INK 31:36 "and the half, the portion of those who went out to the army, was: the number of the sheep three hundred and thirty-seven thousand five hundred" — the parser\'s 337,500 = 675,000 / 2 CHECK; the register gate\'s count line 31:36 LEDGER]'),
                E_('counted', 'the-warriors-portion', value=WARRIORS[1], law='F6 [INK 31:38 "and the cattle thirty-six thousand" — 72,000 / 2 CHECK]'),
                E_('counted', 'the-warriors-portion', value=WARRIORS[2], law='F6 [INK 31:39 "and the donkeys thirty thousand five hundred" — 61,000 / 2 CHECK]'),
                E_('counted', 'the-warriors-portion', value=WARRIORS[3], law='F6 [INK 31:40 "and the persons sixteen thousand" — 32,000 / 2 CHECK; the register gate\'s count line 31:40 LEDGER]'),
                E_('counted', 'the-tribute', value=TRIBUTE[0], law='F6 [INK 31:37 "and the tribute to the LORD of the sheep was six hundred and seventy-five" — 337,500 x 1/500 CHECK]'),
                E_('counted', 'the-tribute', value=TRIBUTE[1], law='F6 [INK 31:38 "and their tribute to the LORD seventy-two" — 36,000 x 1/500 CHECK]'),
                E_('counted', 'the-tribute', value=TRIBUTE[2], law='F6 [INK 31:39 "and their tribute to the LORD sixty-one" — 30,500 x 1/500 CHECK]'),
                E_('counted', 'the-tribute', value=TRIBUTE[3], law='F6 [INK 31:40 "and their tribute to the LORD thirty-two souls" — 16,000 x 1/500 CHECK; the tribute 840 heads in all]'),
                E_('heave_offering_given', 'eleazar', cp='the-tribute', amount=sum(TRIBUTE), value='the tribute, the LORD\'s heave-offering — 675 sheep, 72 cattle, 61 donkeys, 32 persons: 840 heads (31:37-41)', law='F6 [INK 31:41 "and Moses gave the tribute, the LORD\'s heave-offering, to Eleazar the priest, as the LORD commanded Moses" — the TRANSFER; "the LORD\'s heave-offering" the half-shekel\'s phrase (eleven seats); the row tribute_rate_reading (Menachot 77b:20: not for all generations)]')]
    if k == 'levites_portion_given':
        world.close('moses', 'commanded', 'Num 31:47 — and Moses took from the half of the children of Israel the held one of fifty, of man and of beast, and gave them to the Levites who keep the charge of the tabernacle of the LORD, as the LORD commanded Moses: the transfer run', value='the_levites_share')
        return [E_('counted', 'the-congregations-half', value=CONGREGATION[0], law='F6 [INK 31:43 "and the half of the congregation was: of the sheep three hundred and thirty-seven thousand five hundred" — = the warriors\' portion CHECK (מחצת העדה "the half of the congregation", one seat)]'),
                E_('counted', 'the-congregations-half', value=CONGREGATION[1], law='F6 [INK 31:44 "and cattle thirty-six thousand" — CHECK]'),
                E_('counted', 'the-congregations-half', value=CONGREGATION[2], law='F6 [INK 31:45 "and donkeys thirty thousand five hundred" — CHECK]'),
                E_('counted', 'the-congregations-half', value=CONGREGATION[3], law='F6 [INK 31:46 "and the persons sixteen thousand" — CHECK; the register gate\'s count line 31:46 LEDGER]'),
                E_('levites_portion_given', 'the-levites', cp='the-congregations-half', amount=sum(LEVITES), value='one held of fifty of the congregation\'s half — %d / %d / %d / %d = %d heads COMPUTED, UNWRITTEN (31:47); ten times the priest\'s 840' % (LEVITES + (sum(LEVITES),)), law='F6 [INK 31:47 "and Moses took from the half of the children of Israel the held one of fifty, of man and of beast, and gave them to the Levites who keep the charge of the tabernacle of the LORD, as the LORD commanded Moses" — the TRANSFER; THE SHARE STATED AS A RATE AND NEVER AS A NUMBER: the value the runner\'s arithmetic; the row levites_rate_reading (the terumah\'s average — Jerusalem Talmud Terumot 4:3:2)]')]
    if k == 'officers_gold_brought':
        return [E_('no_plague_at_counting', 'the-men-of-war', value='your servants have lifted the head of the men of war under our hand, and not one man of us is missing (31:49)', law='F7 [INK 31:48-49 — the officers of thousands and of hundreds (Jethro\'s grades, Exodus 18:21); "lift the head" Exodus 30:12\'s idiom; the shekel engine\'s clause (IS.shekel(plague_clause) by CALL); the row atonement_reading (the moral count, Yevamot 61a:4)]'),
                E_('atoned_forgiven', 'the-officers-of-the-host', cp='HEAVEN', value='we have brought the LORD\'s offering, every man what he found, vessels of gold — the armlet, the bracelet, the ring, the earring and the kumaz — to atone for our souls before the LORD (31:50): the ransom of Exodus 30 run at a count', law='F7 [INK 31:50 — "to atone for our souls" / Exodus 30:15-16\'s "to atone for your souls" (IS.shekel(atone_souls) by CALL); the rows ornaments_reading (Shabbat 64a:20-21) and atonement_reading (the eyes\' thoughts, Shabbat 64a:22-64b:2)]'),
                E_('memorial_before_the_lord', 'israel', value=GOLD, law='F7 [INK 31:52-54 "all the gold of the heave-offering which they offered to the LORD was sixteen thousand seven hundred and fifty shekels ... and Moses and Eleazar the priest took the gold ... and brought it into the tent of meeting, a memorial for the children of Israel before the LORD" — the parser\'s 16,750; Exodus 30:16\'s six words in another order; the LORD\'s offering to the tent, not the altar (Temurah 13a:14); 31:53 the private plunder outside the count]')]
    # ---- the exam's case kinds: each names LITERALLY every effect it can write (2b's form) ----
    if k == 'midian_war_case':
        fn = the_war if event.get('cell') == 'war' else the_vengeance
        v, e, _ = fn(dict(event, ask=event['ask']), DATA); L = '%s [%s]' % ('F2' if event.get('cell') == 'war' else 'F1', v); s_ = event['person']
        W = {'commanded': E_('commanded', s_, value=v, law=L), 'counted': E_('counted', s_, value=v, law=L), 'slain': E_('slain', s_, cp='israel', value=v, law=L), 'accepted': E_('accepted', s_, value=v, law=L), 'exempt': E_('exempt', s_, value=v, law=L)}
        return [W[x] for x in e if x != FX.NONE]
    if k == 'captive_sentence_case':
        v, e, _ = the_sentence(dict(event, ask=event['ask']), DATA); L = 'F3 [%s]' % v; s_ = event['person']
        W = {'commanded': E_('commanded', s_, value=v, law=L), 'mark_of_anger': E_('mark_of_anger', s_, cp='the-officers-of-the-host', value=v, law=L), 'accepted': E_('accepted', s_, value=v, law=L), 'exempt': E_('exempt', s_, value=v, law=L)}
        return [W[x] for x in e if x != FX.NONE]
    if k == 'warriors_purification_case':
        v, e, _ = the_purification(dict(event, ask=event['ask']), DATA); L = 'F4 [%s]' % v; s_ = event['person']
        W = {'sent_outside_the_camp': E_('sent_outside_the_camp', s_, value=v, law=L),
             'corpse_unclean_seven_days': E_('corpse_unclean_seven_days', s_, amount=SEVEN, due=day + SEVEN, value=v, law=L),               # the TIMERS: chukat's dues (the machine counts the days that pass)
             'sprinkling_due_third_day': E_('sprinkling_due_third_day', s_, due=day + THIRD_DUE, value=v, law=L), 'sprinkling_due_seventh_day': E_('sprinkling_due_seventh_day', s_, due=day + SEVENTH_DUE, value=v, law=L),
             'declared_pure': E_('declared_pure', s_, value=v, law=L), 'accepted': E_('accepted', s_, value=v, law=L), 'exempt': E_('exempt', s_, value=v, law=L)}
        return [W[x] for x in e if x != FX.NONE]
    if k == 'vessel_of_war_case':
        v, e, _ = the_vessels(dict(event, ask=event['ask']), DATA); L = 'F5 [%s]' % v; s_ = event['person']
        W = {'declared_pure': E_('declared_pure', s_, value=v, law=L), 'immersed': E_('immersed', s_, value=v, law=L), 'accepted': E_('accepted', s_, value=v, law=L), 'exempt': E_('exempt', s_, value=v, law=L)}
        return [W[x] for x in e if x != FX.NONE]
    if k == 'prey_division_case':
        v, e, _ = the_division(dict(event, ask=event['ask']), DATA); L = 'F6 [%s]' % v; s_ = event['person']
        W = {'counted': E_('counted', s_, value=v, law=L), 'heave_offering_given': E_('heave_offering_given', s_, cp='the-tribute', value=v, law=L), 'levites_portion_given': E_('levites_portion_given', s_, cp='the-congregations-half', value=v, law=L), 'accepted': E_('accepted', s_, value=v, law=L), 'exempt': E_('exempt', s_, value=v, law=L)}
        return [W[x] for x in e if x != FX.NONE]
    if k == 'officers_gold_case':
        v, e, _ = the_gold(dict(event, ask=event['ask']), DATA); L = 'F7 [%s]' % v; s_ = event['person']
        W = {'no_plague_at_counting': E_('no_plague_at_counting', s_, value=v, law=L), 'atoned_forgiven': E_('atoned_forgiven', s_, cp='HEAVEN', value=v, law=L), 'memorial_before_the_lord': E_('memorial_before_the_lord', s_, value=v, law=L), 'accepted': E_('accepted', s_, value=v, law=L), 'exempt': E_('exempt', s_, value=v, law=L)}
        return [W[x] for x in e if x != FX.NONE]
    return []


LINES = [
    ('Num 31:1-2 — and the LORD spoke to Moses, saying: avenge the vengeance of the children of Israel from the Midianites; afterward you shall be gathered to your people', 'moses'),
    ('Num 31:3-6 — and Moses spoke to the people: arm men from among you for the army ... a thousand to a tribe ... and there were delivered from the thousands of Israel a thousand to a tribe, twelve thousand armed for the army; and Moses sent them, and Phinehas son of Eleazar the priest, with the holy vessels and the trumpets of the alarm in his hand', 'israel'),
    ('Num 31:7 — and they warred against Midian as the LORD commanded Moses, and they killed every male', 'israel'),
    ('Num 31:8 — and the kings of Midian they killed with their slain: Evi, Rekem, Zur, Hur and Reba, the five kings of Midian; and Balaam son of Beor they killed with the sword', 'israel'),
    ('Num 31:9-12 — and the children of Israel took captive the women of Midian and their little ones, and all their cattle, and all their flocks, and all their goods they took as spoil; and all their cities in their dwellings and all their castles they burned with fire; and they brought the captives, the prey and the spoil to Moses and to Eleazar the priest and to the congregation, at the plains of Moab by the Jordan at Jericho', 'israel'),
    ('Num 31:13-18 — and Moses was wroth with the officers of the host ... have you kept every female alive? ... now kill every male among the little ones, and every woman who has known a man by lying with a male kill; and all the little ones among the women who have not known a man by lying with a male keep alive for yourselves', 'moses'),
    ('Num 31:19-20 — and you, encamp outside the camp seven days: whoever has killed a soul and whoever has touched a slain one, purify yourselves on the third day and on the seventh day, you and your captives; and every garment, every vessel of skin, every work of goats and every vessel of wood you shall purify', 'moses'),
    ('Num 31:21-24 — and Eleazar the priest said to the men of war who had gone to the battle: this is the statute of the Torah which the LORD commanded Moses: the gold, the silver, the bronze, the iron, the tin and the lead — everything that comes into the fire you shall pass through the fire and it shall be clean, only with the water of sprinkling it shall be purified; and everything that does not come into the fire you shall pass through water; and wash your garments on the seventh day and be clean, and afterward come into the camp', 'eleazar'),
    ('Num 31:25-30 — and the LORD spoke to Moses: take the sum of the prey of the captives ... and halve the prey between those who took the war and all the congregation; and levy a tribute to the LORD from the men of war: one soul of five hundred ... and give it to Eleazar the priest, the heave-offering of the LORD; and from the half of the children of Israel take one held of fifty ... and give them to the Levites who keep the charge of the tabernacle of the LORD', 'moses'),
    ('Num 31:31-35 — and Moses and Eleazar the priest did as the LORD commanded Moses; and the prey, the rest of the plunder, was: sheep six hundred and seventy-five thousand, cattle seventy-two thousand, donkeys sixty-one thousand, and the persons, of the women who had not known a man, thirty-two thousand', 'moses'),
    ('Num 31:36-41 — and the half, the portion of those who went out to the army, was: sheep three hundred and thirty-seven thousand five hundred, and the tribute to the LORD six hundred and seventy-five; cattle thirty-six thousand, their tribute seventy-two; donkeys thirty thousand five hundred, their tribute sixty-one; persons sixteen thousand, their tribute thirty-two souls; and Moses gave the tribute, the heave-offering of the LORD, to Eleazar the priest, as the LORD commanded Moses', 'moses'),
    ('Num 31:42-47 — and from the half of the children of Israel, which Moses halved from the men of the army: the half of the congregation was sheep three hundred and thirty-seven thousand five hundred, cattle thirty-six thousand, donkeys thirty thousand five hundred, persons sixteen thousand; and Moses took from the half of the children of Israel the held one of fifty, of man and of beast, and gave them to the Levites who keep the charge of the tabernacle of the LORD, as the LORD commanded Moses', 'moses'),
    ('Num 31:48-54 — and the officers over the thousands of the army came near to Moses: your servants have lifted the head of the men of war under our hand, and not one man of us is missing; and we have brought the offering of the LORD, every man what he found, vessels of gold — the armlet, the bracelet, the ring, the earring and the kumaz — to atone for our souls before the LORD; and all the gold of the heave-offering was sixteen thousand seven hundred and fifty shekels; the men of the host had taken spoil every man for himself; and Moses and Eleazar the priest took the gold and brought it into the tent of meeting, a memorial for the children of Israel before the LORD', 'the-officers-of-the-host'),
]
CLOSES = 'six — the trumpets (31:6, by carrying), the two vengeance debits (31:7), the division (31:31), the tribute (31:41), the Levites\' share (31:47); the sentence on the captives OPEN forever'


def scene():
    """THE SCENE — the exam's rows replayed on the world engine (the exodus epoch): the exam's persons through the six case kinds, the
    clock advanced seven days to fire the purification's timers."""
    with contextlib.redirect_stdout(io.StringIO()):
        w = WE.World(era='Num 31:1-54: Mishnah Avodah Zarah 5:12, Kelim 11:1, Terumot 4:3 and the sugyot on the engine (the exodus epoch)', epoch='exodus')
        w.laws = [law_midian]
        w.advance(w.clock.day_in('exodus', 40, 6, 1))
        # ---- the exam's persons through the six case kinds (LITERAL submits — the daemon gate parses no loop) ----
        w.submit({'kind': 'midian_war_case', 'subject': 'the-muster', 'person': 'the-muster', 'ask': 'muster', 'case_source': 'Num 31:4-5 — the exam\'s row muster'})
        w.submit({'kind': 'midian_war_case', 'subject': 'the-moab-question', 'person': 'the-moab-question', 'ask': 'moab_spared', 'case_source': 'Bava Kamma 38a:16 — the exam\'s row moab_spared'})
        w.submit({'kind': 'midian_war_case', 'subject': 'the-anointed-priest', 'person': 'the-anointed-priest', 'ask': 'phinehas_anointed_for_war', 'case_source': 'Sotah 43a:1 — the exam\'s row phinehas_anointed_for_war'})
        w.submit({'kind': 'midian_war_case', 'subject': 'the-five-kings-slain', 'person': 'the-five-kings-slain', 'cell': 'war', 'ask': 'five_kings', 'case_source': 'Num 31:8 — the exam\'s row five_kings'})
        w.submit({'kind': 'midian_war_case', 'subject': 'the-diviner', 'person': 'the-diviner', 'cell': 'war', 'ask': 'balaam', 'case_source': 'Sanhedrin 106a:16 — the exam\'s row balaam'})
        w.submit({'kind': 'captive_sentence_case', 'subject': 'the-wrath', 'person': 'the-wrath', 'ask': 'moses_wrath', 'case_source': 'Pesachim 66b:7 — the exam\'s row moses_wrath'})
        w.submit({'kind': 'captive_sentence_case', 'subject': 'the-sentence', 'person': 'the-sentence', 'ask': 'the_sentence', 'case_source': 'Num 31:17-18 — the exam\'s row the_sentence'})
        w.submit({'kind': 'captive_sentence_case', 'subject': 'the-convert-under-three', 'person': 'the-convert-under-three', 'ask': 'proselyte_age', 'case_source': 'Yevamot 60b:6 — the exam\'s row proselyte_age'})
        w.submit({'kind': 'captive_sentence_case', 'subject': 'the-inference', 'person': 'the-inference', 'ask': 'punish_by_inference', 'case_source': 'Makkot 5b:11 — the exam\'s row punish_by_inference'})
        w.submit({'kind': 'warriors_purification_case', 'subject': 'the-toucher', 'person': 'the-toucher', 'ask': 'schedule', 'case_source': 'Num 31:19 — the exam\'s row schedule'})
        w.submit({'kind': 'warriors_purification_case', 'subject': 'the-sworded', 'person': 'the-sworded', 'ask': 'sword_like_slain', 'case_source': 'Nazir 53b:11 — the exam\'s row sword_like_slain'})
        w.submit({'kind': 'warriors_purification_case', 'subject': 'the-captive-sprinkled', 'person': 'the-captive-sprinkled', 'ask': 'captives_sprinkled', 'case_source': 'Yevamot 61a:5 — the exam\'s row captives_sprinkled'})
        w.submit({'kind': 'warriors_purification_case', 'subject': 'the-four-materials', 'person': 'the-four-materials', 'ask': 'four_materials', 'case_source': 'Shabbat 64a:7 — the exam\'s row four_materials'})
        w.submit({'kind': 'warriors_purification_case', 'subject': 'the-camp-entrant', 'person': 'the-camp-entrant', 'ask': 'camp_entry_reading', 'case_source': 'Sifrei 158:3 — the exam\'s row camp_entry_reading'})
        w.submit({'kind': 'vessel_of_war_case', 'subject': 'the-spit', 'person': 'the-spit', 'ask': 'kashering', 'material': 'metal', 'use': 'fire', 'case_source': 'Mishnah Avodah Zarah 5:12 — the exam\'s row kashering (the spit)'})
        w.submit({'kind': 'vessel_of_war_case', 'subject': 'the-cup', 'person': 'the-cup', 'ask': 'kashering', 'material': 'metal', 'use': 'cold', 'case_source': 'Avodah Zarah 75b:17 — the exam\'s row kashering (the cup)'})
        w.submit({'kind': 'vessel_of_war_case', 'subject': 'the-earthen-pot', 'person': 'the-earthen-pot', 'ask': 'kashering', 'material': 'earthenware', 'case_source': 'Pesachim 30b:8 — the exam\'s row kashering (earthenware)'})
        w.submit({'kind': 'vessel_of_war_case', 'subject': 'the-immersion', 'person': 'the-immersion', 'ask': 'immersion_source', 'case_source': 'Avodah Zarah 75b:7 — the exam\'s row immersion_source'})
        w.submit({'kind': 'prey_division_case', 'subject': 'the-tribute-rate', 'person': 'the-tribute-rate', 'ask': 'tribute_rate', 'case_source': 'Num 31:28 — the exam\'s row tribute_rate'})
        w.submit({'kind': 'prey_division_case', 'subject': 'the-levites-rate', 'person': 'the-levites-rate', 'ask': 'levites_rate', 'case_source': 'Jerusalem Talmud Terumot 4:3:2 — the exam\'s row levites_rate'})
        w.submit({'kind': 'prey_division_case', 'subject': 'the-tribute-check', 'person': 'the-tribute-check', 'ask': 'the_tribute_check', 'case_source': 'Num 31:37-41 — the exam\'s row the_tribute_check'})
        w.submit({'kind': 'prey_division_case', 'subject': 'the-private-plunder', 'person': 'the-private-plunder', 'ask': 'private_plunder', 'case_source': 'Num 31:53 — the exam\'s row private_plunder'})
        w.submit({'kind': 'officers_gold_case', 'subject': 'the-count', 'person': 'the-count', 'ask': 'the_count', 'case_source': 'Num 31:49 — the exam\'s row the_count'})
        w.submit({'kind': 'officers_gold_case', 'subject': 'the-ransom', 'person': 'the-ransom', 'ask': 'ransom_at_a_count', 'case_source': 'Num 31:50 — the exam\'s row ransom_at_a_count'})
        w.submit({'kind': 'officers_gold_case', 'subject': 'the-memorial', 'person': 'the-memorial', 'ask': 'memorial', 'case_source': 'Temurah 13a:14 — the exam\'s row memorial'})
        w.submit({'kind': 'officers_gold_case', 'subject': 'the-ornaments', 'person': 'the-ornaments', 'ask': 'ornaments', 'case_source': 'Shabbat 64a:20 — the exam\'s row ornaments'})
        w.advance(w.clock.day + 7)                                             # THE SEVENTH DAY: the purification's timers fire (the third at + 3, the seventh at + 7)
    n = lambda eid, eff: len([e for e in w.entity(eid).ledger if e['effect'] == eff])
    is_open = lambda eid, eff: int(any(e['effect'] == eff and e.get('open') for e in w.entity(eid).ledger))
    tset = len([l for l in w.log if l[0] == 'TIMER-SET']); tfire = len([l for l in w.log if l[0] == 'TIMER-FIRE']); tcan = len([l for l in w.log if l[0] == 'TIMER-CANCEL'])
    return ((n('the-muster', 'counted'), n('the-moab-question', 'commanded'), n('the-anointed-priest', 'accepted'), n('the-five-kings-slain', 'slain'), n('the-diviner', 'slain'),
             n('the-wrath', 'mark_of_anger'), n('the-sentence', 'commanded'), is_open('the-sentence', 'commanded'), n('the-convert-under-three', 'accepted'), n('the-inference', 'accepted'),
             n('the-toucher', 'sprinkling_due_third_day'), n('the-toucher', 'sprinkling_due_seventh_day'), n('the-toucher', 'corpse_unclean_seven_days'), n('the-sworded', 'corpse_unclean_seven_days'), n('the-captive-sprinkled', 'sprinkling_due_seventh_day'), n('the-four-materials', 'accepted'), n('the-camp-entrant', 'declared_pure'),
             n('the-spit', 'declared_pure'), n('the-spit', 'immersed'), n('the-cup', 'immersed'), n('the-cup', 'declared_pure'), n('the-earthen-pot', 'exempt'), n('the-immersion', 'immersed'),
             n('the-tribute-rate', 'heave_offering_given'), n('the-levites-rate', 'levites_portion_given'), n('the-tribute-check', 'counted'), n('the-tribute-check', 'heave_offering_given'), n('the-private-plunder', 'accepted'),
             n('the-count', 'no_plague_at_counting'), n('the-ransom', 'no_plague_at_counting'), n('the-ransom', 'atoned_forgiven'), n('the-memorial', 'memorial_before_the_lord'), n('the-ornaments', 'accepted')),
            (tset, tfire, tcan, len(w.timers)),
            len(w.entities)), w
SCENE, _W = scene()
# THE PREDICTION (typed before the first run, NUMBERS_WALK.md "Sitting 11b"): every exam person written once per effect — the cup's 'declared_pure' the one zero (the
# second branch writes immersed alone); the sentence's debit OPEN; TIMERS: set 6 (the toucher's three, the sworded's one, the captive's two), fired 6 at the seventh day,
# cancelled 0, pending 0. ENTITIES: the exam's 26 persons.
SCENE_PREDICTED = ((1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1), (6, 6, 0, 0), 26)


def narrative():
    """THE NUMBERS WALK 11b (2026-09-12): the portion's own acts AS HISTORY — the THIRTEEN lines of 31:1-54 at the counter's day (40, 6, 1),
    page-order after the vows' line (30:2-17), on a world with this runner's daemon: 35 writes, six timers set (none fired — the tape ends
    at the counter's day), no marker, fourteen entities, four closes found on this world (the trumpets' and the Balak debit's entries live on
    the sequence world alone). Recorded by the sequential run's recorder and stitched onto the tape. Not a graded cell: the tuple below is
    a tripwire typed from the design; the sequence world's RUN tuple and CX1-CX9 grade the tape."""
    with contextlib.redirect_stdout(io.StringIO()):
        w = WE.World(era='Num 31:1-54: the war of Midian on the tape — the vengeance, the war, the sentence, the purification, the statute, the division, the gold (the exodus epoch)', epoch='exodus')
        w.laws = [law_midian]
        w.advance(w.clock.day_in('exodus', 40, 6, 1))
        # THE DAEMON GATE READS LITERAL SUBMITS ONLY — the thirteen lines typed out
        w.submit({'kind': 'midian_vengeance_commanded', 'subject': 'moses', 'to': 'moses', 'close': 'Num 31:7 — by value', 'case_source': LINES[0][0]})
        w.submit({'kind': 'midian_army_mustered', 'subject': 'israel', 'count': MUSTER, 'with': 'pinchas', 'close': 'the trumpets (10:2) closed by value — a run by carrying', 'case_source': LINES[1][0]})
        w.submit({'kind': 'midian_warred', 'subject': 'israel', 'against': 'the-midianites', 'close': 'harass_the_midianites (25:17) and avenge_the_midianites (31:2) closed by value — no write', 'case_source': LINES[2][0]})
        w.submit({'kind': 'kings_and_balaam_slain', 'subject': 'israel', 'kings': KINGS_NAMES, 'diviner': 'balaam', 'case_source': LINES[3][0]})
        w.submit({'kind': 'captives_and_spoil_taken', 'subject': 'israel', 'to': 'moses', 'at': 'the plains of Moab by the Jordan at Jericho', 'case_source': LINES[4][0]})
        w.submit({'kind': 'moses_wroth_at_the_officers', 'subject': 'moses', 'to': 'the-officers-of-the-host', 'close': 'the sentence OPEN forever — no narrated run', 'case_source': LINES[5][0]})
        w.submit({'kind': 'warriors_purification_commanded', 'subject': 'moses', 'to': 'the-men-of-war', 'captives': 'the-captives-of-midian', 'schedule': [THIRD_DUE, SEVENTH_DUE], 'case_source': LINES[6][0]})
        w.submit({'kind': 'vessels_statute_spoken', 'subject': 'eleazar', 'to': 'the-men-of-war', 'metals': METALS, 'case_source': LINES[7][0]})
        w.submit({'kind': 'prey_division_commanded', 'subject': 'moses', 'rates': [str(TRIBUTE_RATE), str(LEVITE_RATE)], 'close': '31:31, 31:41, 31:47 — by value', 'case_source': LINES[8][0]})
        w.submit({'kind': 'prey_counted', 'subject': 'moses', 'with': 'eleazar', 'totals': list(TOTALS), 'case_source': LINES[9][0]})
        w.submit({'kind': 'tribute_given', 'subject': 'moses', 'to': 'eleazar', 'portion': list(WARRIORS), 'tribute': list(TRIBUTE), 'case_source': LINES[10][0]})
        w.submit({'kind': 'levites_portion_given', 'subject': 'moses', 'to': 'the-levites', 'half': list(CONGREGATION), 'share': list(LEVITES), 'case_source': LINES[11][0]})
        w.submit({'kind': 'officers_gold_brought', 'subject': 'the-officers-of-the-host', 'to': 'moses', 'gold': GOLD, 'ornaments': ORNAMENTS, 'case_source': LINES[12][0]})
    writes = len([l for l in w.log if l[0] == 'WRITE'])
    closes = len([e for ent in w.entities.values() for e in ent.ledger if e.get('closed_by')])
    return (writes, len([l for l in w.log if l[0] == 'TIMER-SET']), len(w.entities), w.clock.eras['exodus'].date(w.clock.day)[1:], closes), w


NARRATIVE, _WN = narrative()
NARRATIVE_PREDICTED = (35, 6, 14, (6, 1), 4)   # NUMBERS_WALK.md "Sitting 11b": 35 writes (L1 1, L2 1, L3 0, L4 2, L5 3, L6 2, L7 1, L8 1, L9 3, L10 4, L11 9, L12 5, L13 3), six timers set, fourteen entities, the date (6, 1) of the fortieth year, four closes found on this world (avenge, divide, tribute, share — the trumpets' and the Balak entries live on the tape)
assert NARRATIVE == NARRATIVE_PREDICTED, ('THE NUMBERS WALK: the war of Midian\'s narrative moved from its prediction', NARRATIVE, NARRATIVE_PREDICTED)


# =====================================================================
# Motion 2 — THE TEST DATA: the answer sheet's rows (the docket's LAW rows).
# =====================================================================
CASES = [
    # F1 — the vengeance and the muster
    ('Num 31:1-2 / 25:17 — the command and its run share the word', lambda: the_vengeance({'ask': 'the_command'}, DATA), 'avenge the vengeance — the command and its run share the word: the Midianites with the article at 25:17 and 31:2 alone'),
    ('Num 31:3 / Sifrei 157:2 — the vengeance of the LORD', lambda: the_vengeance({'ask': 'vengeance_of_the_lord'}, DATA), "Moses relays the vengeance of the children of Israel as the vengeance of the LORD (31:3) — Sifrei 157:2"),
    ('Num 31:2 / Sifrei 157:2; Nedarim 37b:8 — afterward you shall be gathered', lambda: the_vengeance({'ask': 'gathered_after'}, DATA), "the sequence — Moses gathered to his people AFTER the war (31:2); the checkpoint waits at Deuteronomy 34"),
    ('Num 31:4-5 — the muster (computed: 1,000 x 12)', lambda: the_vengeance({'ask': 'muster'}, DATA), "twelve thousand — a thousand to a tribe, the distributive pair; 1,000 x 12 the ink's own product (31:4-5)"),
    ('Sifrei 157:3 — R. Yishmael\'s twenty-four thousand against R. Akiva\'s twelve', lambda: the_vengeance({'ask': 'muster_count'}, DATA), "twelve thousand (R. Akiva; the ink's product) — R. Yishmael's twenty-four thousand recorded (Sifrei 157:3)"),
    ('Sifrei 157:3 — Levi in the muster (the export\'s reversed arm)', lambda: the_vengeance({'ask': 'levi_in_the_muster'}, DATA), "Levi in — 'to all the tribes of Israel' includes Levi (Sifrei 157:3's Hebrew); the export's 'to exclude' the reversed arm"),
    ('Num 31:5 / Sifrei 157:4 — they were delivered', lambda: the_vengeance({'ask': 'delivered'}, DATA), "'they were delivered' — against their will, the war brought Moses' death near (Sifrei 157:4); the three readings recorded"),
    ('Num 31:6 / Sifrei 157:4; Sotah 43a:1 — the holy vessels', lambda: the_vengeance({'ask': 'holy_vessels'}, DATA), "the ark and the frontplate (Sifrei 157:4) / the ark and the tablets (Sotah 43a:1) — the shelf assigns the vessels; the trumpets the shofarot"),
    ('Sotah 43a:1-3 — Phinehas the priest anointed for war; the avenger of Joseph', lambda: the_vengeance({'ask': 'phinehas_anointed_for_war'}, DATA), "Phinehas the priest anointed for war (Sotah 43a:1); 'them' the Sanhedrin; the avenger of Joseph — 'the Midianites sold him' (Sotah 43a:2-3; Sifrei 157:4)"),
    ('Sotah 43a:3 — from the daughters of Putiel', lambda: the_vengeance({'ask': 'phinehas_lineage'}, DATA), "from the daughters of Putiel — Joseph and Jethro both (Sotah 43a:3); the Sifrei's Hebrew Joseph alone, the export's English Jethro"),
    ('Num 31:6 / Num 10:2 by CALL — the trumpets closed by carrying', lambda: the_vengeance({'ask': 'the_trumpets'}, DATA), "the trumpets in Phinehas's hand (31:6) — moses' debit the_trumpets closed BY VALUE: a run by carrying; no sounding narrated"),
    ('Num 10:9 by CALL — the war clause; nothing written for the alarm', lambda: the_vengeance({'ask': 'war_clause'}, DATA), "10:9's war clause by CALL — 'the alarm — war itself'; nothing written for the alarm: no sounding narrated (BH.trumpets)"),
    ('Bava Kamma 38a:16; BK by CALL — Moab spared', lambda: the_vengeance({'ask': 'moab_spared'}, DATA), "Midian harassed, Moab spared — Deuteronomy 2:9 barred Moses' own a-fortiori (Bava Kamma 38a:16; BK by CALL)"),
    # F2 — the war
    ('Num 31:7 / THE REGISTER GATE — the receipt closes two debits by value', lambda: the_war({'ask': 'receipt'}, DATA), "as the LORD commanded Moses (31:7) — the receipt closes israel_people's harass_the_midianites and moses' avenge_the_midianites BY VALUE"),
    ('Num 31:7 / Genesis 34:25 — they killed every male', lambda: the_war({'ask': 'every_male'}, DATA), "they killed every male — Shechem's phrase (Genesis 34:25 its only other seat)"),
    ('Num 31:8 / Joshua 13:21 — the five kings', lambda: the_war({'ask': 'five_kings'}, DATA), "five kings — Evi, Rekem, Zur, Hur, Reba (31:8; the parser's [5]); Joshua 13:21 retells them as the princes of Sihon: a RUN_CITATION; one party on the ledger"),
    ('Num 25:15, 31:8; BK by CALL — Zur among the five', lambda: the_war({'ask': 'zur'}, DATA), "Zur one of the five kings — Cozbi's father dies in the war her death opened (31:8; 25:15 — BK's row by CALL)"),
    ('Num 31:8 / Sanhedrin 106a:16, 106b:1; BK by CALL — Balaam with the sword', lambda: the_war({'ask': 'balaam'}, DATA), "Balaam killed with the sword (31:8) — come for his wages (Sanhedrin 106a:16); the four court modes recorded (106b:1) — BK's row by CALL"),
    ('Num 31:9 — the captives', lambda: the_war({'ask': 'captives'}, DATA), "the women of Midian and their little ones taken captive (31:9) — the captives of Midian one party, cp israel"),
    ('Num 31:9 — the spoil', lambda: the_war({'ask': 'spoil'}, DATA), "all their cattle, all their flocks, all their goods taken as spoil (31:9) — spoil_taken on israel, cp the Midianites"),
    ('Num 31:10 / Onkelos — the cities and the castles burned', lambda: the_war({'ask': 'cities_burned'}, DATA), "all their cities in their dwellings and all their castles burned with fire (31:10) — Onkelos' houses of worship the castles_reading row"),
    ('Num 31:11-12 — brought to Moses at the plains of Moab', lambda: the_war({'ask': 'brought_to_moses'}, DATA), "the captives, the prey and the spoil brought to Moses, Eleazar and the congregation at the plains of Moab by the Jordan at Jericho (31:12) — the line's field"),
    ('Joshua 13:21-22 — the RUN_CITATION', lambda: the_war({'ask': 'joshua_13'}, DATA), "Joshua 13:21-22 retells the five as the princes of Sihon and Balaam the diviner slain with the sword — a RUN_CITATION, three deltas"),
    # F3 — the sentence
    ('Num 31:14 / Sifrei 157:9; Pesachim 66b:7 — anger begets error', lambda: the_sentence({'ask': 'moses_wrath'}, DATA), "and Moses was wroth with the officers of the host (31:14) — anger begets error (Sifrei 157:9; Pesachim 66b:7): the law hidden, Eleazar speaks it at 31:21"),
    ('Pesachim 66b:6-9 — the anger seats', lambda: the_sentence({'ask': 'anger_seats'}, DATA), "Moses the scholar (31:14 / 31:21), Elisha the prophet (2 Kings 3:14-15), Eliab lowered (1 Samuel 17:28 / 16:7) — Pesachim 66b:6-9"),
    ('Sifrei 157:9; Megillah 15a:20 — in the name of its sayer', lambda: the_sentence({'ask': 'in_the_name_of_its_sayer'}, DATA), "whoever reports a saying in the name of its sayer brings redemption (Megillah 15a:20) — the Sifrei 157:9's closing rule; the export dropped R. Yoshiyah's name"),
    ('Num 31:15-16 — have you kept every female alive?', lambda: the_sentence({'ask': 'every_female_kept'}, DATA), "'have you kept every female alive?' (31:15) — by the word of Balaam they were the cause of the treachery in the matter of Peor (31:16): the sotah's phrase"),
    ('Num 31:17-18 / 31:35 — the sentence: a command with no narrated run', lambda: the_sentence({'ask': 'the_sentence'}, DATA), "every male among the little ones and every woman who has known a man killed, the little ones among the women who have not known a man kept alive (31:17-18) — a COMMAND with no narrated run: OPEN"),
    ('Yevamot 60b:8-10; Sifrei 157:6-7 — fit for intercourse', lambda: the_sentence({'ask': 'known_a_man_test'}, DATA), "fit for intercourse — the line at three years, not the act (Yevamot 60b:9-10; Sifrei 157:6-7): the case kinds run by age"),
    ('Yevamot 60b:11-13 — the frontplate test; Jabesh-gilead\'s barrel', lambda: the_sentence({'ask': 'frontplate_test'}, DATA), "passed before the frontplate — the face turned sallow (Yevamot 60b:11); Jabesh-gilead's four hundred by the barrel of wine (60b:12)"),
    ('Yevamot 60b:6, 60b:14; Kiddushin 78a:19-21 — the convert under three', lambda: the_sentence({'ask': 'proselyte_age'}, DATA), "the convert under three years and a day fit for the priesthood — R. Shimon ben Yochai from 31:18 with Phinehas present, the halakha as him (Yevamot 60b:6, 60b:14; Kiddushin 78a:19-21); the Rabbis: as slaves and maidservants"),
    ('Sifrei 157:6; Makkot 5b:11-16; Sanhedrin 54a:17 — we do not punish by inference', lambda: the_sentence({'ask': 'punish_by_inference'}, DATA), "we do not punish by inference — the second 'kill' written (Sifrei 157:6; Makkot 5b:11-16); R. Yishmael's 'to close the subject' beside; the Abaye / Rava fork (Sanhedrin 54a:17)"),
    ('Judges 21:10-12; Yevamot 60b:12 — Jabesh-gilead the RUN_CITATION', lambda: the_sentence({'ask': 'jabesh_gilead'}, DATA), "Judges 21:10-12 runs the sentence — twelve thousand sent, every male and every woman who knew a man devoted, four hundred virgins kept: a RUN_CITATION"),
    ('Deuteronomy 20:13-14 — the war law NOT COMPILED', lambda: the_sentence({'ask': 'deuteronomy_20'}, DATA), "Deuteronomy 20:13-14 spares the women and the little ones — this chapter stricter on both; NOT COMPILED, owed at its chapter"),
    # F4 — the purification
    ('Num 31:19 / Num 12:15; CK by CALL — outside the camp seven days', lambda: the_purification({'ask': 'outside_the_camp'}, DATA), "encamp outside the camp seven days (31:19) — the corpse-impure out of the Presence's camp alone (CK.corpse_tumah camps by CALL)"),
    ('Num 31:19 / 19:12, 19:19; CK by CALL — the schedule as timers', lambda: the_purification({'ask': 'schedule'}, DATA), "purify yourselves on the third day and on the seventh day, you and your captives (31:19) — the three timers, chukat's dues (day + 3, day + 7)"),
    ('Num 31:24 / Bava Kamma 25b:13 — the seven days a floor', lambda: the_purification({'ask': 'seven_days_floor'}, DATA), "wash your garments on the seventh day (31:24) — what a corpse defiles stays impure no less than seven days (Bava Kamma 25b:13); CK seven_days by CALL"),
    ('Nazir 53b:11; Pesachim 14b:1, 14b:5; Chullin 3a:1; CK\'s row READ — the sword like the slain', lambda: the_purification({'ask': 'sword_like_slain'}, DATA), "a sword is like the slain — the metal takes the corpse's grade (Nazir 53b:11; Pesachim 14b:1, 14b:5; Chullin 3a:1) — the warriors' metal the seat"),
    ('Yevamot 61a:1, 61a:5; CK\'s row READ — the captives sprinkled', lambda: the_purification({'ask': 'captives_sprinkled'}, DATA), "the captives sprinkled — gentile corpses defile by touch and carrying, not by tent (Yevamot 61a:1, 61a:5): the Midian war the proof"),
    ('Num 31:20 / Leviticus 11:32 — the four materials ON THE DB', lambda: the_purification({'ask': 'four_materials'}, DATA), "garment, vessel of skin, goat-work, vessel of wood (31:20) against Leviticus 11:32's wood, garment, skin, sack — three shared, sack there against goat-work here (computed on the DB)"),
    ('Shabbat 64a:2-4, 64a:9; Chullin 25b:4 — the goat-work\'s reach', lambda: the_purification({'ask': 'goat_work_reading'}, DATA), "spun and woven — the sack (Shabbat 64a:3; Sifrei 157:8); reins and the belly band (64a:4), the tails (64a:9), horn and hoof in, birds' bones out (Chullin 25b:4)"),
    ('Shabbat 64a:7-8, 64a:15; Bava Kamma 25b:6 — the two lists a TRANSFER taught', lambda: the_purification({'ask': 'the_transfer'}, DATA), "the verbal analogy garment / leather between Leviticus 11:32 and Numbers 31:20 run both ways (Shabbat 64a:7-8, 64a:15; Bava Kamma 25b:6) — the edge midian to shemini a TRANSFER taught; the free-word condition argued (64a:16-19)"),
    ('Leviticus 11:24-25 by CALL — the carcass grade; the vessels\' cell OWED', lambda: the_purification({'ask': 'carcass_grade'}, DATA), "the carcass grade by call — touch impure until evening, carry wash and evening (Lev 11:24-25); the vessels' cell in shemini OWED"),
    ('Num 31:24 / 19:19; Sifrei 158:3 — the camp entry', lambda: the_purification({'ask': 'camp_entry_reading'}, DATA), "wash on the seventh day, be clean, then come into the camp (31:24) against 19:19's evening — Sifrei 158:3's two-way likening"),
    ('Nazir 54b:6; Oholot 1:2-3; CK by CALL — the removes', lambda: the_purification({'ask': 'removes'}, DATA), "the vessel's toucher until evening (Nazir 54b:6; Oholot 1:2-3) — the removes by call"),
    ('Mishnah Kelim 15:1 — receptacles', lambda: the_purification({'ask': 'receptacles'}, DATA), "vessels of wood and skin as receptacles (Mishnah Kelim 15:1) — the flat ones outside"),
    # F5 — the vessels
    ('Num 31:21 / 19:2 — this is the statute of the Torah: the third relayed form', lambda: the_vessels({'ask': 'statute_head'}, DATA), "this is the statute of the Torah (31:21) — 19:2's head, Eleazar speaking it: the third relayed form"),
    ('Eruvin 63a:24 — Eleazar before his teacher', lambda: the_vessels({'ask': 'eleazar_before_his_teacher'}, DATA), "Eleazar lowered for ruling before his teacher (Eruvin 63a:24) — the relay a fault on the shelf; the installed_by class's witness"),
    ('THE LOOP step 3 — installed_by for a statute in the priest\'s voice', lambda: the_vessels({'ask': 'installed_by'}, DATA), "installed_by boot — the priest's voice citing the LORD's command to Moses: the third relayed form, the class named; the second pass decides"),
    ('Num 31:22 / Shabbat 16b:2; Kelim 11:1 — the six metals', lambda: the_vessels({'ask': 'six_metals'}, DATA), "gold, silver, bronze, iron, tin, lead (31:22) — tin's one Torah seat, lead's two; metal vessels impure by Torah law (Shabbat 16b:2; Kelim 11:1)"),
    ('Num 31:23 — what comes into the fire', lambda: the_vessels({'ask': 'kashering', 'material': 'metal', 'use': 'fire'}, DATA), "what comes into the fire — through the fire, and with the water of sprinkling purified (31:23): the first branch; the immersion added by the shelf"),
    ('Num 31:23 — what does not come into the fire', lambda: the_vessels({'ask': 'kashering', 'material': 'metal', 'use': 'cold'}, DATA), "what does not come into the fire — through water (31:23): the second branch"),
    ('Pesachim 30b:8 / Leviticus 6:21 — earthenware', lambda: the_vessels({'ask': 'kashering', 'material': 'earthenware'}, DATA), "earthenware never purged — the Torah testified: broken (Leviticus 6:21; Pesachim 30b:8); the six metals the rule's whole class"),
    ('Mishnah Avodah Zarah 5:12; Avodah Zarah 75b:17 — the modes by use', lambda: the_vessels({'ask': 'kashering_modes'}, DATA), "whiten the spit and the grill, boil the pot and the kettle, polish the knife — and immerse all (Mishnah Avodah Zarah 5:12; the baraita's four uses, 75b:17)"),
    ('Avodah Zarah 75b:7-11; Sifrei 158:2 — the immersion\'s source', lambda: the_vessels({'ask': 'immersion_source'}, DATA), "'and it shall be pure' adds immersion in forty se'ah (Rava, Avodah Zarah 75b:7); 'nevertheless' excludes the third and seventh day's sprinkling (Bar Kappara, 75b:8); the Sifrei 158:2's a-fortiori beside"),
    ('Num 31:23 / Shabbat 16b; Avodah Zarah 75b:9; CK by CALL — the water of niddah', lambda: the_vessels({'ask': 'water_of_sprinkling'}, DATA), "the water of niddah — four Torah seats all in 19 and 31; the heifer's water by call: metal vessels keep their impurity until the sprinkling (Shabbat 16b); the shelf splits its sense (75b:9)"),
    ('Avodah Zarah 75b:21; Pesachim 44b:15 — the same-day pot', lambda: the_vessels({'ask': 'same_day_pot'}, DATA), "the Torah forbids only a pot used that same day (Avodah Zarah 75b:21; Pesachim 44b:15); the rest a fence"),
    ('Nazir 37b:1; Pesachim 44b:13-14 — the taste as the substance; the novelty', lambda: the_vessels({'ask': 'taste_as_substance'}, DATA), "the taste as the substance from the vessels of Midian (R. Akiva — Nazir 37b:1; Pesachim 44b:13); the Rabbis: the purging a NOVELTY (44b:14)"),
    ('Avodah Zarah 75b:12-15 — the immersion\'s scope', lambda: the_vessels({'ask': 'immersion_scope'}, DATA), "metal utensils (75b:14), purchased as the captured (75b:13), even new (75b:12), glass as metal (75b:15) — the immersion's scope the passage's own"),
    ('Avodah Zarah 76a:17, 76b:1; Pesachim 30b:6 — as it absorbs so it emits', lambda: the_vessels({'ask': 'as_it_absorbs'}, DATA), "as it absorbs so it emits (Avodah Zarah 76b:1; Pesachim 30b:6); the measures — until the outer layer sheds, a kettle in a kettle (76a:17)"),
    ('Num 31:21-24 — the tape\'s statute line', lambda: the_vessels({'ask': 'the_line'}, DATA), "commanded on the men of war valued the_statute_of_the_vessels — the walk's form for a statute line (10b's commanded on israel)"),
    # F6 — the division
    ('Num 31:26 / Exodus 30:12 by CALL — lift the head', lambda: the_division({'ask': 'lift_the_head'}, DATA), "take the sum of the prey (31:26) — 'lift the head', the census idiom (Exod 30:12 by call), the singular imperative one seat"),
    ('Num 31:27 / 1 Samuel 30:24-25 OBSERVED — the halving', lambda: the_division({'ask': 'halve'}, DATA), "halve the prey between those who took the war and all the congregation (31:27) — the equal halves; David's statute (1 Samuel 30:24-25) OBSERVED, no link on the declared shelf"),
    ('Num 31:28 / Menachot 77b:20; Yoma 24a:5 — one of five hundred', lambda: the_division({'ask': 'tribute_rate'}, DATA), "one soul of five hundred (31:28) — the rate Fraction(1, 500), the parser's read; not one of ten and not for all generations (Menachot 77b:20); asked as a measure (Yoma 24a:5)"),
    ('Num 31:30 / Mishnah Terumot 4:3; Jerusalem Talmud Terumot 4:3:2 — one of fifty', lambda: the_division({'ask': 'levites_rate'}, DATA), "one held of fifty (31:30) — Fraction(1, 50); the terumah's average rate (Mishnah Terumot 4:3; Jerusalem Talmud Terumot 4:3:2 — R. Levi from this verse): a TRANSFER taught"),
    ('Num 31:30, 31:47 / 1:53 by CALL — the Levites\' charge', lambda: the_division({'ask': 'levites_charge'}, DATA), "to the Levites who keep the charge of the tabernacle of the LORD (31:30, 31:47) — 1:53's charge (BM.charges by call: gershon the woven, kohath the holy, merari the frame)"),
    ('Num 31:26-30 / 31:31, 31:41, 31:47 — three debits, three receipts', lambda: the_division({'ask': 'three_debits'}, DATA), "three commands in one speech — divide the prey, the tribute to the priest, the Levites' share — closed by value at 31:31, 31:41, 31:47"),
    ('Num 31:32-35 — the count (computed)', lambda: the_division({'ask': 'the_count'}, DATA), "the prey: 675,000 sheep, 72,000 cattle, 61,000 donkeys, 32,000 persons (31:32-35) — the parser's numbers, every total a multiple of a thousand"),
    ('Num 31:36-46 — the halving CHECK (computed)', lambda: the_division({'ask': 'the_halving_check'}, DATA), "the totals halved = the warriors' portion = the congregation's half: 337,500 / 36,000 / 30,500 / 16,000 (31:36-46) — CHECK"),
    ('Num 31:37-41 — the tribute CHECK (computed)', lambda: the_division({'ask': 'the_tribute_check'}, DATA), "the warriors' portion at one of five hundred = the tribute: 675 / 72 / 61 / 32 = 840 heads (31:37-40) — CHECK; given to Eleazar (31:41)"),
    ('Num 31:42-47 — the Levites\' share COMPUTED, UNWRITTEN', lambda: the_division({'ask': 'the_levites_share'}, DATA), "the congregation's half at one of fifty = 6,750 / 720 / 610 / 320 = 8,400 heads — COMPUTED, UNWRITTEN; ten times the priest's; given to the Levites (31:47)"),
    ('world_engine._write — the counted statuses on four thing parties', lambda: the_division({'ask': 'thing_parties'}, DATA), "the sixteen counted statuses on four thing parties — the prey, the warriors' portion, the tribute, the congregation's half — never on israel_people or the Levites (the status overwrite)"),
    ('Num 31:53 — the private plunder', lambda: the_division({'ask': 'private_plunder'}, DATA), "the men of the host had taken spoil every man for himself (31:53) — outside the count"),
    ('THE REGISTER GATE — the nine seats paid', lambda: the_division({'ask': 'register_gate'}, DATA), "the four count lines LEDGER by the counted statuses; the four receipts CLOSE; the rate a MEASURE (R7); the footer's block DAEMONS"),
    ('Jerusalem Talmud Terumot 4:3:8 — the Torah\'s own measure of terumah', lambda: the_division({'ask': 'terumah_measure'}, DATA), "the Torah's own measure of terumah none (Jerusalem Talmud Terumot 4:3:8) — the rates the shelf's settings, the ink's fiftieth a one-time instruction"),
    # F7 — the officers' gold
    ('Num 31:48-49 / Exodus 18:21; IS by CALL — the count with none missing', lambda: the_gold({'ask': 'the_count'}, DATA), "the officers of thousands and of hundreds lifted the head of the men of war — not one man of us is missing (31:49): Jethro's grades the army's ranks; the count with none missing"),
    ('Num 31:49-50, 31:54 / Exodus 30:12-16 by CALL — the ransom at a count', lambda: the_gold({'ask': 'ransom_at_a_count'}, DATA), "to atone for our souls before the LORD (31:50) — Exodus 30:12-16's own words (lift the head, atone for your souls, a memorial): the ransom of Exodus 30 run at a count; no plague at the counting"),
    ('Shabbat 64a:22-64b:2; Yevamot 61a:4 — the atonement\'s reading', lambda: the_gold({'ask': 'atonement_reading'}, DATA), "the ransom at a count (the ink) / the eyes' thoughts of transgression (Shabbat 64a:22-64b:2) — both arms; R. Shimon's moral count (Yevamot 61a:4)"),
    ('Num 31:50 / Shabbat 64a:20-21 — the five ornaments', lambda: the_gold({'ask': 'ornaments'}, DATA), "armlet, bracelet, ring, earring, kumaz (31:50) — agil the breast-mold, kumaz the womb-mold (Shabbat 64a:20-21); vessels for impurity (31:51 — Shabbat 60a:3, 63b:19)"),
    ('Shabbat 63b:6, 60a:3, 63b:19 — the ornaments as vessels', lambda: the_gold({'ask': 'ornaments_impure'}, DATA), "the bracelet impure — 31:50 beside 31:19 (Shabbat 63b:6); all vessels with which labor is done (31:51) the class's definition (60a:3, 63b:19)"),
    ('Num 31:52 — sixteen thousand seven hundred and fifty (computed)', lambda: the_gold({'ask': 'gold_weight'}, DATA), "sixteen thousand seven hundred and fifty shekels (31:52) — the parser's 16,750; the captains no number"),
    ('Num 31:54 / Exodus 30:16; Temurah 13a:14 — the memorial in the tent', lambda: the_gold({'ask': 'memorial'}, DATA), "brought into the tent of meeting, a memorial for the children of Israel before the LORD (31:54) — Exodus 30:16's six words in another order; the LORD's offering, not an offering to the LORD: the tent, not the altar (Temurah 13a:14)"),
    ('Yevamot 61a:4 — not one man of us is missing, two readings', lambda: the_gold({'ask': 'not_one_missing_reading'}, DATA), "the Rabbis: the casualty count — no Jew fell (the corpses gentile); R. Shimon ben Yochai: missing to transgression (Yevamot 61a:4)"),
    # THE INK, computed
    ('THE PARSER — the integers at nineteen verses', lambda: (sorted(INTS.items()), [FX.NONE], [('INK', 'Num 31:1-54 — the parser')]), [(4, [1000, 1000]), (5, [1000, 12000]), (6, [1000]), (8, [5]), (19, [7]), (32, [675000]), (33, [72000]), (34, [61000]), (35, [32000]), (36, [337500]), (37, [675]), (38, [36000, 72]), (39, [30500, 61]), (40, [16000, 32]), (43, [337500]), (44, [36000]), (45, [30500]), (46, [16000]), (52, [16750])]),
    ('THE PARSER — the rates (rule 28, the ratio class), the ordinals, the starred denominators, the marked ones', lambda: ((sorted(RATES.items()), sorted((v, o) for v, o in ORDINALS.items() if o), STARRED, MARKED), [FX.NONE], [('INK', 'Num 31:19, 31:24, 31:28, 31:30, 31:47')]), ([(28, [(1, 500)]), (30, [(1, 50)]), (42, [(1, 2)]), (47, [(1, 50)])], [(19, [3, 7]), (24, [7])], [(28, 'מחמש*'), (28, 'המאות*'), (30, 'החמשים*'), (47, 'החמשים*')], [(28, 'אחד/500%'), (30, 'אחד/50%'), (42, 'וממחצית%'), (47, 'אחד/50%')])),
    ('THE ARITHMETIC — the totals, the halves, the tribute, the Levites\' share, the muster, the gold (computed)', lambda: ((TOTALS, WARRIORS, TRIBUTE, CONGREGATION, LEVITES, sum(TRIBUTE), sum(LEVITES), MUSTER, GOLD), [FX.NONE], [('INK', 'Num 31:4-5, 31:32-52 — the checks')]), ((675000, 72000, 61000, 32000), (337500, 36000, 30500, 16000), (675, 72, 61, 32), (337500, 36000, 30500, 16000), (6750, 720, 610, 320), 840, 8400, 12000, 16750)),
    ('THE FRAMES — six frame verbs; the LORD twice, Moses once, Eleazar once, the officers once', lambda: (FRAME_VERBS, [FX.NONE], [('INK', 'Num 31 — the first words')]), [(1, 'וידבר', 'יהוה'), (3, 'וידבר', 'משה'), (15, 'ויאמר', 'אליהם'), (21, 'ויאמר', 'אלעזר'), (25, 'ויאמר', 'יהוה'), (49, 'ויאמרו', 'אל')]),
    ('THE PHRASE SEATS — the vengeance and the war (computed on the whole DB)', lambda: ((MIDIANITES_ART, AVENGE, VENGEANCE_OF_THE_LORD, GATHERED, THOUSAND_PER_TRIBE, TRUMPETS_OF_ALARM, WARRED, len(RECEIPT), KILLED_EVERY_MALE, KINGS_OF_MIDIAN, FIVE_KINGS, len(BALAAM_SON_OF_BEOR)), [FX.NONE], [('INK', 'the whole DB')]), (['Num 25:17', 'Num 31:2'], ['Num 31:2'], ['Jer 50:15', 'Jer 50:28', 'Jer 51:11', 'Num 31:3'], ['Num 31:2'], ['Num 31:4', 'Num 31:5', 'Num 31:6'], ['2Chr 13:12', 'Num 31:6'], ['Num 31:7'], 13, ['Gen 34:25', 'Num 31:7'], ['Judg 8:5', 'Judg 8:12', 'Judg 8:26', 'Num 31:8'], ['Num 31:8'], 5)),
    ('THE PHRASE SEATS — the sentence and the purification (computed on the whole DB)', lambda: ((WORD_OF_BALAAM, len(TREACHERY), MATTER_OF_PEOR, MOSES_WROTH, OFFICERS_OF_THE_HOST, LYING_WITH_A_MALE, KEEP_ALIVE, OUTSIDE_SEVEN, THIRD_AND_SEVENTH, YOU_AND_YOUR_CAPTIVES, STATUTE_HEAD, WATER_OF_SPRINKLING, PURIFY_2, PURIFY_3, TIN, LEAD), [FX.NONE], [('INK', 'the whole DB')]), (['Num 31:16'], 5, ['Num 25:18', 'Num 31:16'], ['Num 31:14'], ['2Chr 23:14', 'Num 31:14'], ['Judg 21:12', 'Num 31:17'], ['Num 31:18'], ['Num 12:15', 'Num 31:19'], ['Num 19:12', 'Num 19:19', 'Num 31:19'], ['Num 31:19'], ['Num 19:2', 'Num 31:21'], ['Num 31:23'], ['Num 31:19', 'Num 31:20'], ['Num 19:12', 'Num 19:13', 'Num 19:20', 'Num 31:23'], ['Deut 10:8', 'Num 16:9', 'Num 31:22'], ['Num 31:22', 'Zech 5:8'])),
    ('THE PHRASE SEATS — the division and the gold (computed on the whole DB)', lambda: ((LIFT_THE_HEAD, WHEN_YOU_LIFT, ONE_OF_FIVE_HUNDRED, ONE_HELD_OF_FIFTY, len(HEAVE_OFFERING), KEEP_THE_CHARGE, TRIBUTE_TOKENS, PREY_TOKENS, HALF_OF_THE_CONGREGATION, LIFTED_THE_HEAD, NONE_MISSING, ATONE_OUR_SOULS, ATONE_YOUR_SOULS, MEMORIAL, MEMORIAL_EXOD, OFFERING_OF_THE_LORD, GOLD_PHRASE), [FX.NONE], [('INK', 'the whole DB')]), (['Num 31:26'], ['Exod 30:12'], ['Num 31:28'], ['Num 31:30'], 11, ['Num 31:30', 'Num 31:47'], ['Num 31:28', 'Num 31:41'], ['Num 31:11', 'Num 31:12', 'Num 31:27', 'Num 31:32'], ['Num 31:43'], ['Num 31:49'], ['Num 31:49'], ['Num 31:50'], ['Exod 30:15', 'Exod 30:16', 'Lev 17:11'], ['Num 31:54'], ['Exod 30:16'], ['Num 9:7', 'Num 9:13', 'Num 31:50'], ['Num 31:52'])),
    ('THE METALS, THE MATERIALS, THE KINGS, THE ORNAMENTS (computed)', lambda: ((METALS, NUM_MATERIALS, LEV_MATERIALS, SHARED_MATERIALS, KINGS_NAMES, ORNAMENTS), [FX.NONE], [('INK', 'Num 31:8, 31:20, 31:22, 31:50; Lev 11:32')]), (['הזהב', 'הכסף', 'הנחשת', 'הברזל', 'הבדיל', 'העפרת'], ['בגד', 'עור', 'עזים', 'עץ'], ['עץ', 'בגד', 'עור', 'שק'], ['בגד', 'עור', 'עץ'], ['אוי', 'רקם', 'צור', 'חור', 'רבע'], ['אצעדה', 'וצמיד', 'טבעת', 'עגיל', 'וכומז'])),
    # THE CALLEES
    ('THE BALAK RUNNER — Moab spared, Balaam\'s death, Zur (by CALL; the rows READ)', lambda: ((BK_MOAB[0][:28], BK_BALAAM[0][:36], BK_ZUR[0][:21], BK.DATA['balaam_death']['value'], sorted(BK.DATA['balaam_death']['settings']), BK.DATA['cozbi_and_zur']['value'], BK.DATA['midian_command_run']['value']), [FX.NONE], [('MOVE', 'CALLED cold_run_balak')]), ('Midian harassed, Moab spared', 'Balaam killed by the sword at Midian', 'Cozbi daughter of Zur', 'by_the_sword_at_midian', ['by_the_sword_at_midian', 'four_modes'], 'zur_of_the_five_kings', ('31:2', '31:7'))),   # the first graded run: the three slices typed one character long (a trailing space) — retyped from the print, as at 10b
    ('THE BEHA RUNNER — the war clause, the pair (by CALL)', lambda: ((BH_WAR[0], BH_WAR[1], BH_COUNT[0][:23], BH.TRUMPETS, BH.DATA['oppression_scope']['value']), [FX.NONE], [('MOVE', 'CALLED cold_run_beha')]), ('the alarm — war itself (10:9)', ['sanctify_day'], '2 — the wilderness pair', [2], 'any oppression')),
    ('THE CHUKAT RUNNER — the schedule, the seven days, the sword, the camps, the tent, the decree, the removes (by CALL; the rows READ)', lambda: ((CK_SCHEDULE[1], CK_SEVEN[1], CK_SWORD[0][:25], CK_CAMPS[1], CK_TENT[1], CK_METAL[1], CK_REMOVES[1], CK.SCHEDULE, CK.SEVENS, CK.DATA['sword_like_slain']['value'], CK.DATA['tent_gentile']['value']), [FX.NONE], [('MOVE', 'CALLED cold_run_chukat')]), (['sprinkling_due_third_day', 'sprinkling_due_seventh_day', 'declared_pure'], ['corpse_unclean_seven_days'], 'a sword is like the slain', ['sent_outside_the_camp'], ['exempt'], ['disqualified'], ['corpse_unclean_seven_days', 'impure_until_evening'], [3, 7, 3, 7], [[7], [7], [7]], 'a_metal_vessel_takes_the_corpse_grade', 'no_tent_impurity')),
    ('THE SHEMINI RUNNER — the carcass grade (by CALL; the vessels\' cell OWED)', lambda: ((SH_TOUCH[0], SH_CARRY[0], SH_TOUCH[2][:9]), [FX.NONE], [('MOVE', 'CALLED cold_run_shemini')]), ('impure_until_evening', 'wash_and_evening', 'Lev 11:24')),
    ('THE INCENSE-SHEKEL RUNNER — lift the head, atone for your souls, the plague clause, the silver of atonements, the trigger (by CALL)', lambda: ((IS_LIFT, IS_ATONE, IS_PLAGUE['v'], IS_PLAGUE['fx'], IS_SILVER, IS.shekel('trigger_parameter')['v']['ink']), [FX.NONE], [('MOVE', 'CALLED cold_run_incense_shekel')]), (['Exod 30:12'], ['Exod 30:15', 'Exod 30:16', 'Lev 17:11'], ['Exod 30:12'], ['no_plague_at_counting'], ['Exod 30:16'], 'census')),
    ('THE BAMIDBAR RUNNER — the houses\' charges (by CALL)', lambda: ((BM_CHARGES[0], BM_CHARGES[1]), [FX.NONE], [('MOVE', 'CALLED cold_run_bamidbar')]), ('gershon the woven, kohath the holy, merari the frame', ['charge_kept'])),
    # THE WRAP: the scene on the world engine
    ('THE SCENE on the world engine — the exam\'s persons through the six case kinds; the purification\'s timers set and fired (predicted before the run)',
     lambda: (SCENE, [FX.NONE], [('INK', 'Num 31:1-54 — the recorded rows replayed')]),
     ((1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1), (6, 6, 0, 0), 26)),   # the literal typed from SCENE_PREDICTED (the guard reads literals only)
    ('THE NARRATIVE on the world engine — the thirteen lines; 35 writes, six timers, fourteen entities, four closes (predicted before the run)',
     lambda: (NARRATIVE, [FX.NONE], [('INK', 'Num 31:1-54 — the thirteen lines')]), (35, 6, 14, (6, 1), 4)),
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
    print('THE INK: integers %s; rates %s; ordinals %s; starred %s; marked %s' % (sorted(INTS.items()), sorted(RATES.items()), sorted((v, o) for v, o in ORDINALS.items() if o), STARRED, MARKED))
    print('THE ARITHMETIC: totals %s; the halves %s = %s; the tribute %s (%d heads); the Levites\' share %s (%d heads, UNWRITTEN); the muster %d; the gold %d' % (TOTALS, WARRIORS, CONGREGATION, TRIBUTE, sum(TRIBUTE), LEVITES, sum(LEVITES), MUSTER, GOLD))
    print('THE SCENE on the bench: %s; the timers (set, fired, cancelled, pending) %s; entities %d' % SCENE)
    print('THE NARRATIVE: %s' % (NARRATIVE,))
    print('THE PARAMETER ROWS: ' + '; '.join('%s = %s' % (k, DATA[k]['value']) for k in DATA) + ' (the other settings recorded in DATA)')
    if ok == len(CASES):
        print('\nTHE COMPILE OF MIDIAN: the answer sheet REPRODUCED — %d/%d' % (ok, len(CASES)))
    sys.exit(0 if ok == len(CASES) else 1)

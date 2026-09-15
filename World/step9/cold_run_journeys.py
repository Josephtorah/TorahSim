import os as _os
_ROOT = _os.path.normpath(_os.path.join(_os.path.dirname(_os.path.abspath(__file__)), '..', '..'))   # THE PORTABLE REPO (2026-09-15): the repo root from this file's own place
#!/usr/bin/env python3
# NUM 33:1-56 — THE JOURNEYS (THE NUMBERS WALK sitting 13b, 2026-09-12; World/step9/NUMBERS_WALK.md "Sitting 13b"; the state doc's #153-#154).
# THE ITINERARY AS A RECORD WRITTEN AT THE RUN'S END: Moses' writing (33:1-2) the chapter's own act, its value THE LIST — forty-two places
# built from the DB at import (Rameses and forty-one camps, forty-two "journeyed" and forty-two "camped"), each with its first telling outside
# the chapter and the tape's witness, EIGHTEEN named nowhere else; the departure retold with the tape's own date (33:3 = the exodus marker) and
# THE RUN OF EXODUS 12:12 recorded here alone (33:4 — the judgments on the gods, a status on Egypt forty years on; the firstborn's plague OPEN,
# a burial no removal); the stations against their first tellings on the tokens (33:6 = Exodus 13:20 + one word; 33:9 = 15:27's springs and
# palms; Etham for Shur; Rithmah for Paran; Moseroth seven camps before Mount Hor — the shelf's retreat of seven stations); Aaron's death
# retold with the date and the age the tape's 20:28 line already reads from this chapter (33:38-39 — (40, 5, 1) the marker; 123 = 83 + 40);
# Arad's hearing a run citation (33:40); THE COMMAND in the divine voice (33:50-56) — two DEBITS on Israel OPEN BY DESIGN (dispossess and
# possess; destroy the three objects), the lot's debit of 26:52-56 cited not rewritten (33:54 the restatement with the verb's number switching),
# the negative arm a DATA row (Joshua 23:13, Judges 2:3, Megillah 11a's Haman). Five cells; every token probed (zero-report law); effects on
# every cell (the effects law); the parameters the ink leaves open recorded in DATA with their arms. Reading ledger:
# logic/oral_triage/num_33_journeys_2026-09-12.md; the exam's docket: logic/oral_triage/num_33_journeys_exam_2026-09-12.md (196 rows: LAW 7 /
# DERIVATION 31 / DISPUTE 6 / CONTEXT 149 / OUTSIDE 3).

# ---- THE HONEST-PAIRING GUARD ----------------------------------------------------------------------------
import os as _os, sys as _sys
_sys.path.insert(0, _os.path.dirname(_os.path.abspath(__file__)))
from compile_guards import check_honest_pairing as _chp
_P = _os.path.abspath(__file__)
GUARDED = _chp(_P, 'CASES', 2)
assert GUARDED == 53, ("the guard counted %d expectations, the tripwire holds 53" % GUARDED)   # the design's estimate — retyped from the guard's print after the first run
print('guard: %d expectations checked, every one a literal from the answer sheet [honest-pairing guard satisfied]' % GUARDED)
import sqlite3, sys, io, re, contextlib, collections, yaml
import effects_layer as FX
import world_engine as WE
import cold_run_exodus_story as ES               # THE EDGE: journeys -> exodus_story CALL, reference (33:5-15's stations = Exodus 12:37-19:2's names; the ten plagues and the four removals; the new moon at Sinai)
import cold_run_pesach as PS                     # THE EDGE: journeys -> pesach CALL, reference (33:3's Passover, 33:4's firstborn; 12:12's spec inside its span with no cell on the gods)
import cold_run_beha as BH                       # THE EDGE: journeys -> beha CALL, reference (Kibroth-hattaavah's naming 11:34; Hazeroth and Paran's markers)
import cold_run_shelach as SL                    # THE EDGE: journeys -> shelach CALL, reference ("with a high hand" — the callee names 33:3; Rithmah = Paran's base)
import cold_run_chukat as CK                     # THE EDGE: journeys -> chukat CALL, reference (Kadesh, Mount Hor, the death's date and age, Arad's hearing, Moserah's row)
import cold_run_balak as BK                      # THE EDGE: journeys -> balak CALL, reference (the plains of Moab, Shittim)
import cold_run_second_census as C2              # THE EDGE: journeys -> second_census CALL, reference (33:54 restates 26:52-56 word for word)
import cold_run_gad_reuben as GR                 # THE EDGE: journeys -> gad_reuben CALL, reference (Dibon Gad — the Gad runner's own cell names 33:45-46)
import cold_run_erection as ER                   # THE EDGE: journeys -> erection CALL, reference (the molten image's ban Exodus 34:17; the calf's word 32:4; the other iconoclasm lists)
import cold_run_holiness as HL                   # THE EDGE: journeys -> holiness CALL, reference (Leviticus 19:4's molten gods)

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

# ---- zero-report probes: the span's load-bearing tokens (every one measured on the DB before it was typed — jou_runner_measure.out, 2026-09-12) ----
PROBES = [
    ('אלה',      33, 1,  'these are — the sixty-three verse-initial headings of the Torah'),
    ('מסעי',     33, 1,  'the journeys of — 10:28 the same four words'),
    ('לצבאתם',   33, 1,  'by their hosts — sixteen seats, all in Numbers'),
    ('ביד',      33, 1,  'by the hand of [Moses and Aaron] — Psalm 77:21 the other seat'),
    ('ואהרן',    33, 1,  'and Aaron'),
    ('ויכתב',    33, 2,  'and [Moses] wrote — the four Torah seats'),
    ('מוצאיהם',  33, 2,  'their goings out — Jeremiah 50:7 the other seat'),
    ('למסעיהם',  33, 2,  'by their journeys'),
    ('פי',       33, 2,  'the mouth of [the LORD] — 33:2 and 33:38'),
    ('ואלה',     33, 2,  'and these are — the chiasm'),
    ('ויסעו',    33, 3,  'and they journeyed — the first of forty-two'),
    ('מרעמסס',   33, 3,  'from Rameses — told twice (33:5)'),
    ('בחמשה',    33, 3,  'on the fifteenth — [15]'),
    ('הראשון',   33, 3,  'the first [month] — the ordinals [1, 1]'),
    ('ממחרת',    33, 3,  'on the morrow of — Joshua 5:11 the other seat'),
    ('הפסח',     33, 3,  'the Passover'),
    ('רמה',      33, 3,  'high [hand] — Exodus 14:8, Numbers 15:30'),
    ('לעיני',    33, 3,  'in the sight of [all Egypt]'),
    ('מקברים',   33, 4,  'was burying — the participle, Ezekiel 39:14 the other seat'),
    ('בכור',     33, 4,  'firstborn — every firstborn'),
    ('ובאלהיהם', 33, 4,  'and on their gods'),
    ('שפטים',    33, 4,  'judgments — THE RUN OF EXODUS 12:12'),
    ('ויחנו',    33, 5,  'and they camped — the first of forty-two'),
    ('בסכת',     33, 5,  'at Succoth — Exodus 12:37'),
    ('באתם',     33, 6,  'at Etham — Exodus 13:20'),
    ('החירת',    33, 7,  'Hahiroth — Pi-hahiroth, Exodus 14:2'),
    ('צפון',     33, 7,  '[Baal-]zephon'),
    ('מגדל',     33, 7,  'Migdol'),
    ('ויעברו',   33, 8,  'and they passed [through the midst of the sea]'),
    ('שלשת',     33, 8,  'three [days] — [3]'),
    ('אתם',      33, 8,  'Etham — the wilderness of Etham for Exodus 15:22\'s Shur'),
    ('במרה',     33, 8,  'at Marah'),
    ('אילמה',    33, 9,  'to Elim — the directional ending'),
    ('עינת',     33, 9,  'springs of [water] — twelve'),
    ('תמרים',    33, 9,  'palm trees — seventy'),
    ('סוף',      33, 10, '[the Red] Sea — the camp Exodus never names'),
    ('סין',      33, 11, 'Sin'),
    ('בדפקה',    33, 12, 'at Dophkah — named nowhere else'),
    ('באלוש',    33, 13, 'at Alush — named nowhere else'),
    ('ברפידם',   33, 14, 'at Rephidim'),
    ('לשתות',    33, 14, 'to drink — no water for the people'),
    ('סיני',     33, 15, 'Sinai'),
    ('התאוה',    33, 16, '[Kibroth-]hattaavah — the graves of lust (11:34)'),
    ('בחצרת',    33, 17, 'at Hazeroth'),
    ('ברתמה',    33, 18, 'at Rithmah — Paran under another name'),
    ('פרץ',      33, 19, '[Rimmon-]perez'),
    ('בלבנה',    33, 20, 'at Libnah — the Judah city\'s lemma'),
    ('ברסה',     33, 21, 'at Rissah'),
    ('בקהלתה',   33, 22, 'at Kehelathah'),
    ('שפר',      33, 23, '[Mount] Shepher'),
    ('בחרדה',    33, 24, 'at Haradah'),
    ('במקהלת',   33, 25, 'at Makheloth'),
    ('בתחת',     33, 26, 'at Tahath'),
    ('בתרח',     33, 27, 'at Terah'),
    ('במתקה',    33, 28, 'at Mithkah'),
    ('בחשמנה',   33, 29, 'at Hashmonah'),
    ('במסרות',   33, 30, 'at Moseroth — Deuteronomy 10:6; seven camps before Mount Hor'),
    ('יעקן',     33, 31, '[Bene-]jaakan'),
    ('הגדגד',    33, 32, '[Hor-]haggidgad'),
    ('ביטבתה',   33, 33, 'at Jotbathah — Deuteronomy 10:7'),
    ('בעברנה',   33, 34, 'at Abronah'),
    ('גבר',      33, 35, '[Ezion-]geber'),
    ('צן',       33, 36, 'Zin'),
    ('קדש',      33, 36, 'Kadesh — that is Kadesh'),
    ('ההר',      33, 37, '[Mount] Hor'),
    ('אדום',     33, 37, 'Edom — in the edge of the land of Edom'),
    ('ויעל',     33, 38, 'and [Aaron] went up'),
    ('וימת',     33, 38, 'and died'),
    ('הארבעים',  33, 38, 'the fortieth [year] — the ordinal reader\'s'),
    ('לצאת',     33, 38, 'of the going out — the era\'s stamp'),
    ('החמישי',   33, 38, 'the fifth [month]'),
    ('באחד',     33, 38, 'on the first [of the month] — [1]'),
    ('ועשרים',   33, 39, 'and twenty — a hundred and twenty-three'),
    ('במתו',     33, 39, 'at his death — Deuteronomy 34:7'),
    ('וישמע',    33, 40, 'and [the Canaanite] heard — 21:1'),
    ('ערד',      33, 40, 'Arad'),
    ('בנגב',     33, 40, 'in the Negev'),
    ('בצלמנה',   33, 41, 'at Zalmonah'),
    ('בפונן',    33, 42, 'at Punon'),
    ('באבת',     33, 43, 'at Oboth — 21:10'),
    ('העברים',   33, 44, '[Iye-]abarim'),
    ('מואב',     33, 44, 'Moab'),
    ('גד',       33, 45, 'Gad — Dibon Gad, 32:34\'s city'),
    ('דבלתימה',  33, 46, '[Almon-]diblathaim — the directional ending (Yevamot 13b:6)'),
    ('נבו',      33, 47, 'Nebo'),
    ('בערבת',    33, 48, 'in the plains of [Moab]'),
    ('ירחו',     33, 48, 'Jericho'),
    ('הישמת',    33, 49, '[Beth-]jeshimoth'),
    ('השטים',    33, 49, '[Abel-]shittim'),
    ('וידבר',    33, 50, 'and [the LORD] spoke — the chapter\'s one divine frame'),
    ('לאמר',     33, 50, 'saying'),
    ('עברים',    33, 51, 'pass over [the Jordan]'),
    ('והורשתם',  33, 52, 'and you shall drive out — the same verb at 33:53'),
    ('ישבי',     33, 52, 'the inhabitants of [the land]'),
    ('משכיתם',   33, 52, 'their figured stones — Leviticus 26:1\'s word'),
    ('מסכתם',    33, 52, 'their molten [images] — the calf\'s word'),
    ('במתם',     33, 52, 'their high places — the consonants of "at their death"'),
    ('תשמידו',   33, 52, 'you shall demolish — Leviticus 26:30\'s verb'),
    ('וישבתם',   33, 53, 'and you shall dwell'),
    ('נתתי',     33, 53, 'I have given — the fifth expression\'s gift'),
    ('והתנחלתם', 33, 54, 'and you shall inherit — the plural verb'),
    ('בגורל',    33, 54, 'by lot — 26:55\'s'),
    ('תרבו',     33, 54, 'you shall give more — the plural'),
    ('תמעיט',    33, 54, 'you shall give less — the singular'),
    ('הגורל',    33, 54, 'the lot'),
    ('תורישו',   33, 55, 'you drive out — the negative arm'),
    ('תותירו',   33, 55, 'you leave over — the Passover\'s verb'),
    ('לשכים',    33, 55, 'thorns'),
    ('ולצנינם',  33, 55, 'and pricks — reversed at Joshua 23:13'),
    ('וצררו',    33, 55, 'and they shall harass — 25:18\'s word'),
    ('דמיתי',    33, 56, 'I thought — Isaiah 14:24\'s phrase'),
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
SPAN = [(33, v) for v in range(1, 57)]
NUMBERS = {v: ink_numbers(verse_words('Num', 33, v)) for _, v in SPAN}
ORDINALS = {v: ink_ordinals(verse_words('Num', 33, v)) for _, v in SPAN}
STARRED = [(v, t) for _, v in SPAN for t in verse_words('Num', 33, v) if t.endswith('*')]
MARKED = [(v, t) for _, v in SPAN for t in verse_words('Num', 33, v) if '%' in t]
INTS = {v: n for v, n in NUMBERS.items() if n}; ORDS = {v: o for v, o in ORDINALS.items() if o}
assert INTS == {3: [15], 8: [3], 9: [12, 70], 38: [1], 39: [123]}, INTS                                             # FIVE number verses in fifty-six — every one read; no rule owed
assert ORDS == {3: [1, 1], 38: [40, 5]} and STARRED == [] and MARKED == [], (ORDS, STARRED, MARKED)                 # THE TWO DATE FORMS: 33:38's article-bearing year and month are the ordinal reader's
FIFTEEN, THREE, TWELVE, SEVENTY, DAY_ONE, AGE = INTS[3][0], INTS[8][0], INTS[9][0], INTS[9][1], INTS[38][0], INTS[39][0]
YEAR, MONTH = ORDS[38]
AARON_DATE = (YEAR, MONTH, DAY_ONE); DEPARTURE_DATE = (ORDS[3][0], ORDS[3][1], FIFTEEN)
assert AARON_DATE == (40, 5, 1) and DEPARTURE_DATE == (1, 1, 15), (AARON_DATE, DEPARTURE_DATE)
assert ink_numbers(verse_words('Num', 34, 1)) == [], 'the next chapter opens without a number'
FIRST = {v: words(33, v)[0] for _, v in SPAN}
FRAME_VERBS = [(v, FIRST[v], words(33, v)[1]) for _, v in SPAN if FIRST[v] in ('וידבר', 'ויאמר', 'ויאמרו', 'ויענו')]
assert FRAME_VERBS == [(50, 'וידבר', 'יהוה')], FRAME_VERBS                                                          # THE ONE DIVINE FRAME after forty-nine verses without one
JOURNEYED = [v for _, v in SPAN if 'ויסעו' in words(33, v)]; CAMPED = [v for _, v in SPAN if 'ויחנו' in words(33, v)]
assert JOURNEYED == [3] + list(range(5, 38)) + list(range(41, 49)) and len(JOURNEYED) == 42, JOURNEYED             # forty-two "journeyed"
assert CAMPED == list(range(5, 38)) + list(range(41, 50)) and len(CAMPED) == 42, CAMPED                              # forty-two "camped"
assert len(set(JOURNEYED) & set(CAMPED)) == 41 and set(JOURNEYED) - set(CAMPED) == {3} and set(CAMPED) - set(JOURNEYED) == {49}
# the whole-DB phrase census (the seats typed from the measurement print of 2026-09-12 — jou_runner_measure.out)
_V = collections.OrderedDict(); _L = collections.OrderedDict(); _M = collections.OrderedDict()
for b, c, v, he, lm, mo in db.execute("SELECT v.book, v.chapter, v.verse, w.he, w.lemma, w.morph FROM words w JOIN verses v ON w.verse_id=v.id ORDER BY v.id, w.idx"):
    _V.setdefault((b, c, v), []).append(strip(he)); _L.setdefault((b, c, v), []).append((lm.split('/')[-1].split(' ')[0] if lm else '').rstrip('+')); _M.setdefault((b, c, v), []).append(mo or '')
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
# ---- F1's facts: the heading and the writing ----
HEAD = seats('אלה מסעי בני ישראל'); HOSTS = seats('לצבאתם'); HAND = seats('ביד משה ואהרן'); WROTE = seats('ויכתב משה')
assert HEAD == ['Num 10:28', 'Num 33:1'] and len(HOSTS) == 16 and all(s.startswith('Num ') for s in HOSTS) and 'Num 33:1' in HOSTS, (HEAD, HOSTS)
assert HAND == ['Num 33:1', 'Ps 77:21'] and WROTE == ['Deut 31:9', 'Deut 31:22', 'Exod 24:4', 'Num 33:2'], (HAND, WROTE)                     # THE FOUR WRITINGS
MOUTH = seats('על פי יהוה'); MOUTH_T = seats('על פי יהוה', TORAH); MOUTH_N = seats('על פי יהוה', ('Num',))
assert len(MOUTH) == 21 and len(MOUTH_T) == 18 and len(MOUTH_N) == 15 and {'Num 33:2', 'Num 33:38', 'Deut 34:5', 'Josh 22:9'} <= set(MOUTH), (len(MOUTH), len(MOUTH_T), len(MOUTH_N))
GOINGS = seats('מוצאיהם'); JOURNEYS_L = seats('למסעיהם'); HEADINGS = [k for k, ws in _V.items() if k[0] in TORAH and ws and ws[0] == 'אלה']
assert GOINGS == ['Jer 50:7', 'Num 33:2'] and JOURNEYS_L == ['Exod 17:1', 'Num 10:6', 'Num 10:12', 'Num 33:2'] and len(HEADINGS) == 63, (GOINGS, JOURNEYS_L, len(HEADINGS))
assert words(33, 2)[3:5] == ['מוצאיהם', 'למסעיהם'] and words(33, 2)[9:11] == ['מסעיהם', 'למוצאיהם'], words(33, 2)                      # the chiasm
# ---- F2's facts: the departure ----
FIFTEENTH = seats('בחמשה עשר יום לחדש הראשון'); MORROW = seats('ממחרת הפסח'); HIGH_HAND = seats('ביד רמה'); SIGHT = seats('לעיני כל מצרים')
assert FIFTEENTH == ['Num 33:3'] and MORROW == ['Josh 5:11', 'Num 33:3'] and HIGH_HAND == ['Exod 14:8', 'Num 15:30', 'Num 33:3'] and SIGHT == ['Num 33:3'], (FIFTEENTH, MORROW, HIGH_HAND, SIGHT)
BURYING = seats('מקברים'); EVERY_FB = seats('כל בכור'); JUDG_PERF = seats('עשה יהוה שפטים'); JUDG_FUT = seats('אעשה שפטים'); JUDG_LEMMA = lemma_seats('8201')
assert BURYING == ['Ezek 39:14', 'Num 33:4'] and len(EVERY_FB) == 16 and {'Exod 12:12', 'Exod 12:29', 'Num 33:4'} <= set(EVERY_FB), (BURYING, EVERY_FB)
assert JUDG_PERF == ['Num 33:4'] and JUDG_FUT == ['Exod 12:12', 'Ezek 25:11'] and len(JUDG_LEMMA) == 16 and {'Exod 6:6', 'Exod 7:4', 'Exod 12:12', 'Num 33:4'} <= set(JUDG_LEMMA), (JUDG_PERF, JUDG_FUT, JUDG_LEMMA)   # THE RUN's one perfect
FROM_RAMESES = seats('מרעמסס'); PASSOVER_LEMMA = [s for s in lemma_seats('6453') if s.startswith('Num 33') or s.startswith('Josh 5')]
assert FROM_RAMESES == ['Exod 12:37', 'Num 33:3', 'Num 33:5'] and PASSOVER_LEMMA == ['Josh 5:10', 'Josh 5:11', 'Num 33:3'], (FROM_RAMESES, PASSOVER_LEMMA)
# ---- F3's facts: the stations ----
THREE_DAYS = seats('דרך שלשת ימים'); SPRINGS = seats('שתים עשרה עינת מים'); PALMS = seats('ושבעים תמרים'); SHUR = seats('מדבר שור'); ETHAM_HOMOGRAPH = seats('מדבר אתם')
assert THREE_DAYS == ['Exod 3:18', 'Exod 5:3', 'Exod 8:23', 'Gen 30:36', 'Num 10:33', 'Num 33:8'] and SPRINGS == ['Exod 15:27', 'Num 33:9'] and PALMS == ['Exod 15:27', 'Num 33:9'], (THREE_DAYS, SPRINGS, PALMS)
assert SHUR == ['Exod 15:22'] and ETHAM_HOMOGRAPH == ['Exod 34:33'] and words(33, 8)[11:13] == ['במדבר', 'אתם'], (SHUR, ETHAM_HOMOGRAPH, words(33, 8))   # 'the wilderness of Etham' with its prefix at 33:8 alone; the bare pair at Exodus 34:33 is "speaking with them" — A HOMOGRAPH (the measure's find)
assert words(33, 6) == ['ויסעו', 'מסכת', 'ויחנו', 'באתם', 'אשר', 'בקצה', 'המדבר'] and words(13, 20, 'Exod') == ['ויסעו', 'מסכת', 'ויחנו', 'באתם', 'בקצה', 'המדבר'], (words(33, 6), words(13, 20, 'Exod'))   # 33:6 IS Exodus 13:20 with one word added
RED_SEA_T = seats('ים סוף', TORAH); SINAI_T = seats('במדבר סיני', TORAH); RITHMAH = seats('ברתמה'); THAT_IS_KADESH = seats('הוא קדש')
assert RED_SEA_T == ['Deut 1:40', 'Deut 2:1', 'Deut 11:4', 'Exod 13:18', 'Num 14:25', 'Num 21:4', 'Num 33:10'] and len(SINAI_T) == 9 and 'Num 33:15' in SINAI_T and RITHMAH == ['Num 33:18'], (RED_SEA_T, SINAI_T, RITHMAH)
assert THAT_IS_KADESH == ['Exod 30:32', 'Gen 14:7', 'Lev 25:12', 'Lev 27:30', 'Num 33:36'], THAT_IS_KADESH   # the pair at five seats — Genesis 14:7 and 33:36 the PLACE; Exodus 30:32, Leviticus 25:12, 27:30 "it is HOLY": A HOMOGRAPH the reading's "five seats of the identity idiom" did not name (filed at this compile)
EDGE_EDOM = seats('בקצה ארץ אדום'); BORDER_EDOM = seats('גבול ארץ אדום'); HOR = seats('הר ההר'); HOR_LEMMA_T = lemma_seats('2023', TORAH)
assert EDGE_EDOM == ['Num 33:37'] and BORDER_EDOM == ['Num 20:23'] and HOR == ['Num 20:22', 'Num 20:25', 'Num 20:27', 'Num 33:38', 'Num 34:7'], (EDGE_EDOM, BORDER_EDOM, HOR)
ARAD = seats('הכנעני מלך ערד'); HEARD = seats('וישמע הכנעני'); ABARIM_PL = seats('בהרי העברים'); ABARIM_SG = seats('הר העברים'); JERICHO = seats('ירדן ירחו')
assert ARAD == ['Num 21:1', 'Num 33:40'] and HEARD == ['Num 21:1', 'Num 33:40'] and ABARIM_PL == ['Num 33:47'] and ABARIM_SG == ['Deut 32:49', 'Num 27:12'], (ARAD, HEARD, ABARIM_PL, ABARIM_SG)
assert JERICHO == ['Num 26:3', 'Num 26:63', 'Num 31:12', 'Num 33:48', 'Num 33:50', 'Num 35:1', 'Num 36:13'], JERICHO
BETH_J = seats('הישמת'); SHITTIM = seats('השטים'); DIBLATHAIMAH = tok('דבלתימה')
assert BETH_J == ['Num 33:49'] and SHITTIM == ['Ezek 27:26', 'Joel 4:18', 'Josh 2:1', 'Mic 6:5', 'Num 33:49'] and DIBLATHAIMAH == ['Num 33:46', 'Num 33:47'], (BETH_J, SHITTIM, DIBLATHAIMAH)
assert words(33, 45)[-2:] == ['בדיבן', 'גד'] and words(33, 46)[1:3] == ['מדיבן', 'גד'], (words(33, 45), words(33, 46))                    # Dibon Gad — 32:34's city under its tribe's name
assert words(10, 6, 'Deut')[3:6] == ['מבארת', 'בני', 'יעקן'] and words(10, 6, 'Deut')[6:9] == ['מוסרה', 'שם', 'מת'] and words(10, 7, 'Deut')[2] == 'הגדגדה' and words(10, 7, 'Deut')[5] == 'יטבתה', (words(10, 6, 'Deut'), words(10, 7, 'Deut'))   # THE DEUTERONOMY ORDER: Bene-jaakan then Moserah, "there Aaron died"
# ---- F4's facts: the death retold ----
FORTIETH = seats('בשנת הארבעים'); STAMPS = seats('לצאת בני ישראל מארץ מצרים'); FIFTH = seats('בחדש החמישי'); AT_DEATH = seats('במתו')
assert FORTIETH == ['1Chr 26:31', 'Num 33:38'] and STAMPS == ['1Kgs 6:1', 'Exod 19:1', 'Num 33:38'] and FIFTH == ['Ezra 7:8', 'Jer 1:3', 'Jer 28:1', 'Num 33:38'] and AT_DEATH == ['Deut 34:7', 'Num 33:39'], (FORTIETH, STAMPS, FIFTH, AT_DEATH)   # THE ERA'S THREE STAMPS; the Torah's one fifth month
RETOLD = {k: (ink_numbers(verse_words(*k)), ink_ordinals(verse_words(*k))) for k in (('Exod', 7, 7), ('Deut', 34, 7), ('Deut', 1, 3), ('Exod', 12, 37), ('Exod', 12, 41), ('Exod', 16, 1), ('Exod', 19, 1), ('Num', 10, 11), ('Num', 20, 29), ('Deut', 2, 14), ('Josh', 5, 10), ('1Kgs', 6, 1), ('Num', 14, 33))}
assert RETOLD == {('Exod', 7, 7): ([80, 83], []), ('Deut', 34, 7): ([120], []), ('Deut', 1, 3): ([40, 11, 1], []), ('Exod', 12, 37): ([600000], []), ('Exod', 12, 41): ([430], []), ('Exod', 16, 1): ([15], [2]), ('Exod', 19, 1): ([], [3]), ('Num', 10, 11): ([20], [2]), ('Num', 20, 29): ([30], []), ('Deut', 2, 14): ([38], []), ('Josh', 5, 10): ([14], []), ('1Kgs', 6, 1): ([480], [2]), ('Num', 14, 33): ([40], [])}, RETOLD
MOSES_80, AARON_83 = RETOLD[('Exod', 7, 7)][0]; MOSES_120 = RETOLD[('Deut', 34, 7)][0][0]; SHEVAT_DATE = tuple(RETOLD[('Deut', 1, 3)][0]); KINGS_480 = RETOLD[('1Kgs', 6, 1)][0][0]
assert AARON_83 + YEAR == AGE == 123 and MOSES_80 + YEAR == MOSES_120 == 120 and SHEVAT_DATE == (40, 11, 1), (AARON_83, YEAR, AGE, MOSES_80, MOSES_120, SHEVAT_DATE)   # THE INK'S CHECKSUM ON THE BROTHERS' AGES; the cardinal date the number reader's
# ---- F5's facts: the command ----
FRAME = seats('בערבת מואב על ירדן ירחו לאמר'); SPOKE_PLAINS = seats('וידבר יהוה אל משה בערבת מואב'); PASS_OVER = seats('עברים את הירדן'); INHAB_T = seats('ישבי הארץ', TORAH)
assert FRAME == ['Num 26:3', 'Num 33:50', 'Num 35:1'] and SPOKE_PLAINS == ['Num 33:50', 'Num 35:1'] and len(PASS_OVER) == 7 and {'Num 33:51', 'Num 35:10', 'Deut 11:31'} <= set(PASS_OVER), (FRAME, SPOKE_PLAINS, PASS_OVER)
assert INHAB_T == ['Exod 23:31', 'Gen 36:20', 'Num 32:17', 'Num 33:52', 'Num 33:55'] and seats('והורשתם את כל ישבי הארץ') == ['Num 33:52'], INHAB_T
FIGURED = seats('משכיתם'); FIG_LEV = seats('משכית'); FIG_LEMMA = lemma_seats('4906'); MOLTEN_IMG = seats('צלמי מסכתם'); MOLTEN_T = seats('מסכה', TORAH); MOLTEN_LEMMA_T = lemma_seats('4541', TORAH)
assert FIGURED == ['Num 33:52'] and FIG_LEV == ['Lev 26:1'] and FIG_LEMMA == ['Ezek 8:12', 'Lev 26:1', 'Num 33:52', 'Prov 18:11', 'Prov 25:11', 'Ps 73:7'], (FIGURED, FIG_LEV, FIG_LEMMA)   # THE FIGURED STONE — Leviticus 26:1's word, the ban's seat UNCOMPILED
assert MOLTEN_IMG == ['Num 33:52'] and MOLTEN_T == ['Deut 9:12', 'Deut 9:16', 'Exod 32:4', 'Exod 32:8', 'Exod 34:17', 'Lev 19:4'] and MOLTEN_LEMMA_T == ['Deut 9:12', 'Deut 9:16', 'Deut 27:15', 'Exod 32:4', 'Exod 32:8', 'Exod 34:17', 'Lev 19:4', 'Num 33:52'], (MOLTEN_IMG, MOLTEN_T, MOLTEN_LEMMA_T)
HIGH = seats('במתם'); HIGH_LEMMA_T = lemma_seats('1116', TORAH); YOUR_HIGH = seats('במתיכם'); DEMOLISH = seats('תשמידו'); I_DESTROY = seats('והשמדתי')
assert HIGH == ['Lev 11:31', 'Lev 11:32', 'Num 6:7', 'Num 33:52'] and HIGH_LEMMA_T == ['Deut 32:13', 'Deut 33:29', 'Lev 26:30', 'Num 21:28', 'Num 33:52'], (HIGH, HIGH_LEMMA_T)   # "their high places" the consonants of "at their death" — the morphology decides
assert YOUR_HIGH == ['Lev 26:30'] and DEMOLISH == ['Josh 7:12', 'Num 33:52'] and I_DESTROY == ['Amos 9:8', 'Hag 2:22', 'Lev 26:30', 'Mic 5:13'], (YOUR_HIGH, DEMOLISH, I_DESTROY)   # the spec/curse pair on one object, one verb
DISPOSSESS_DWELL = seats('והורשתם את הארץ וישבתם בה'); GIVEN = seats('לכם נתתי את הארץ'); BY_LOT_T = seats('בגורל', TORAH); MANY = seats('לרב תרבו'); LOT_OUT = seats('אל אשר יצא לו שמה הגורל'); TRIBES_FATHERS = seats('למטות אבתיכם')
assert DISPOSSESS_DWELL == ['Num 33:53'] and GIVEN == ['Num 33:53'] and BY_LOT_T == ['Num 26:55', 'Num 33:54', 'Num 34:13', 'Num 36:2'] and MANY == ['Num 33:54'] and LOT_OUT == ['Num 33:54'] and TRIBES_FATHERS == ['Num 33:54'], (DISPOSSESS_DWELL, GIVEN, BY_LOT_T, MANY, LOT_OUT, TRIBES_FATHERS)
MORPH_54 = [(w, m) for w, m in zip(_V[('Num', 33, 54)], _M[('Num', 33, 54)]) if 'V' in m]
assert MORPH_54 == [('והתנחלתם', 'HC/Vtq2mp'), ('תרבו', 'HVhi2mp'), ('תמעיט', 'HVhi2ms'), ('יצא', 'HVqi3ms'), ('יהיה', 'HVqi3ms'), ('תתנחלו', 'HVti2mp')], MORPH_54   # THE NUMBER SWITCHES INSIDE THE VERSE: "you (plural) shall give more", "you (singular) shall give less"
assert words(26, 54)[:2] == ['לרב', 'תרבה'] and words(33, 54)[5:7] == ['לרב', 'תרבו'] and words(26, 54)[3:5] == ['ולמעט', 'תמעיט'] and words(33, 54)[9:11] == ['ולמעט', 'תמעיט'], (words(26, 54), words(33, 54))   # 26:54's singular turned plural, the second left singular
THORNS = seats('לשכים בעיניכם'); PRICKS = seats('ולצנינם בצדיכם'); PRICKS_EYES = seats('ולצננים בעיניכם'); SIDES_JUDG = seats('לצדים'); LEAVE_OVER = seats('תותירו'); HARASS = seats('וצררו אתכם'); THOUGHT = seats('כאשר דמיתי')
assert THORNS == ['Num 33:55'] and PRICKS == ['Num 33:55'] and PRICKS_EYES == ['Josh 23:13'] and SIDES_JUDG == ['Judg 2:3'], (THORNS, PRICKS, PRICKS_EYES, SIDES_JUDG)   # the negative arm run back REVERSED at Joshua 23:13
assert LEAVE_OVER == ['Exod 12:10', 'Lev 22:30', 'Num 33:55'] and HARASS == ['Num 33:55'] and THOUGHT == ['Isa 14:24', 'Num 33:56'], (LEAVE_OVER, HARASS, THOUGHT)
assert 'מפניכם' in words(33, 52) and 'מפניכם' in words(33, 55) and 'מלפניכם' in words(23, 13, 'Josh') and 'מפניכם' in words(2, 3, 'Judg'), 'from before you — the arm at 33:52 and 33:55, Judges 2:3 the same token, Joshua 23:13 with the lamed (the print: the first typed pass had typed Joshua from memory)'

# ---- THE STATIONS, built from the DB (the design's DATA row): forty-two places = the forty-one departures' places (Rameses told twice) + the last camp ----
def _after(v, verb):
    ws = words(33, v); return ws[ws.index(verb) + 1:]
DEPARTURES = {}
for v in JOURNEYED:
    rest = _after(v, 'ויסעו'); j = next(i for i, t in enumerate(rest) if t.startswith('מ'))    # the from-token (33:5's subject "the children of Israel" skipped)
    place = []
    for t in rest[j:]:
        if t.startswith('וי') or (t.startswith('ב') and place): break                          # the next narrative verb; 33:3's "in the month"
        place.append(t)
    DEPARTURES[v] = place
assert DEPARTURES[3] == DEPARTURES[5] == ['מרעמסס'] and DEPARTURES[8] == ['מפני', 'החירת'] and DEPARTURES[11] == ['מים', 'סוף'] and DEPARTURES[41] == ['מהר', 'ההר'] and DEPARTURES[48] == ['מהרי', 'העברים'], DEPARTURES
LAST_CAMP = _after(48, 'ויחנו')[:2]
assert LAST_CAMP == ['בערבת', 'מואב'] and _after(49, 'ויחנו')[:7] == ['על', 'הירדן', 'מבית', 'הישמת', 'עד', 'אבל', 'השטים'], (LAST_CAMP, _after(49, 'ויחנו'))
def _bare(toks):
    return [toks[0][1:]] + toks[1:]                                                              # the leading preposition stripped (from / at)
PLACES_HE = [' '.join(_bare(DEPARTURES[v])) for v in JOURNEYED if v != 3] + [' '.join(_bare(LAST_CAMP))]
assert len(PLACES_HE) == 42 and len(set(PLACES_HE)) == 42, (len(PLACES_HE), PLACES_HE)          # THE FORTY-TWO on the ink's own count
PLACES_EN = ['Rameses', 'Succoth', 'Etham', 'Pi-hahiroth', 'Marah', 'Elim', 'the Red Sea', 'the wilderness of Sin', 'Dophkah', 'Alush', 'Rephidim', 'the wilderness of Sinai', 'Kibroth-hattaavah', 'Hazeroth', 'Rithmah', 'Rimmon-perez', 'Libnah', 'Rissah', 'Kehelathah', 'Mount Shepher', 'Haradah', 'Makheloth', 'Tahath', 'Terah', 'Mithkah', 'Hashmonah', 'Moseroth', 'Bene-jaakan', 'Hor-haggidgad', 'Jotbathah', 'Abronah', 'Ezion-geber', 'Kadesh', 'Mount Hor', 'Zalmonah', 'Punon', 'Oboth', 'Iye-abarim', 'Dibon-gad', 'Almon-diblathaim', 'the mountains of Abarim', 'the plains of Moab']
assert len(PLACES_EN) == 42
CAMP_VERSE = {i: v for i, v in enumerate([3] + CAMPED[:-1])}                                     # the place's own verse: Rameses 33:3; camp i at CAMPED[i-1] (the last camp 33:48)
CAMP_VERSE[41] = 48
def _lemmas(i):
    """the Np lemmas of a place in BOTH forms — the departure's (the next journeyed verse) and the camp's (its own verse)"""
    v_dep = JOURNEYED[i + 1] if i + 1 < len(JOURNEYED) else None; v_camp = CAMP_VERSE[i]
    out_ = set()
    for vv, toks in ((v_dep, DEPARTURES.get(v_dep, [])), (v_camp, _after(v_camp, 'ויחנו')[:len(PLACES_HE[i].split())] if v_camp in CAMPED else DEPARTURES[3])):
        if vv is None: continue
        ws, ls, ms = _V[('Num', 33, vv)], _L[('Num', 33, vv)], _M[('Num', 33, vv)]
        for t in toks:
            for w_, l_, m_ in zip(ws, ls, ms):
                if w_ == t and 'Np' in m_: out_.add(l_)
    return out_
ONLY_HERE = [PLACES_EN[i] for i in range(42) if _lemmas(i) and not any(not s.startswith('Num 33:') for l in _lemmas(i) for s in lemma_seats(l))]
NO_LEMMA = [PLACES_EN[i] for i in range(42) if not _lemmas(i)]
assert ONLY_HERE == ['Dophkah', 'Alush', 'Rithmah', 'Rimmon-perez', 'Rissah', 'Kehelathah', 'Mount Shepher', 'Haradah', 'Makheloth', 'Mithkah', 'Hashmonah', 'Bene-jaakan', 'Hor-haggidgad', 'Abronah', 'Zalmonah', 'Punon', 'Almon-diblathaim'] and len(ONLY_HERE) == 17, ONLY_HERE   # SEVENTEEN by lemma with no seat outside 33
assert NO_LEMMA == ['the Red Sea'], NO_LEMMA                                                     # the eighteenth — a common noun, no proper-name lemma: the camp Exodus never names
assert PLACES_EN.index('Moseroth') + 7 == PLACES_EN.index('Mount Hor') and PLACES_EN.index('Kadesh') + 1 == PLACES_EN.index('Mount Hor'), (PLACES_EN.index('Moseroth'), PLACES_EN.index('Mount Hor'))   # THE RETREAT OF SEVEN STATIONS (Seder Olam Rabbah 9:2) = the itinerary's own count
FIRST_TELLING = {'Rameses': 'Exod 12:37', 'Succoth': 'Exod 12:37', 'Etham': 'Exod 13:20', 'Pi-hahiroth': 'Exod 14:2', 'Marah': 'Exod 15:23', 'Elim': 'Exod 15:27', 'the Red Sea': None, 'the wilderness of Sin': 'Exod 16:1', 'Dophkah': None, 'Alush': None, 'Rephidim': 'Exod 17:1', 'the wilderness of Sinai': 'Exod 19:1', 'Kibroth-hattaavah': 'Num 11:34', 'Hazeroth': 'Num 11:35', 'Rithmah': None, 'Rimmon-perez': None, 'Libnah': None, 'Rissah': None, 'Kehelathah': None, 'Mount Shepher': None, 'Haradah': None, 'Makheloth': None, 'Tahath': None, 'Terah': None, 'Mithkah': None, 'Hashmonah': None, 'Moseroth': None, 'Bene-jaakan': None, 'Hor-haggidgad': None, 'Jotbathah': None, 'Abronah': None, 'Ezion-geber': None, 'Kadesh': 'Num 20:1', 'Mount Hor': 'Num 20:22', 'Zalmonah': None, 'Punon': None, 'Oboth': 'Num 21:10', 'Iye-abarim': 'Num 21:11', 'Dibon-gad': 'Num 32:34', 'Almon-diblathaim': None, 'the mountains of Abarim': 'Num 27:12', 'the plains of Moab': 'Num 22:1'}
# the tape's witness, typed from the running world's print (jou_compile_measure.out (2): the markers and the encamped_at statuses) — a marker (M), a status (S), another effect (E), none (-)
WITNESS = {'Rameses': 'M Exod 12:41 (1, 1, 15) + S Exod 12:37', 'Succoth': 'S Exod 12:37', 'Etham': 'S Exod 13:20', 'Pi-hahiroth': '-', 'Marah': 'S Exod 15:23', 'Elim': 'S Exod 15:27', 'the Red Sea': '-', 'the wilderness of Sin': 'M Exod 16:1 (1, 2, 15) + S', 'Dophkah': '-', 'Alush': '-', 'Rephidim': 'S Exod 17:1', 'the wilderness of Sinai': 'M Exod 19:1 (1, 3, 1) + S Exod 19:2', 'Kibroth-hattaavah': 'E buried Num 11:34', 'Hazeroth': 'M Num 11:35 (2, 3, 22)', 'Rithmah': 'M Num 12:16 (2, 3, 29) as Paran', 'Rimmon-perez': '-', 'Libnah': '-', 'Rissah': '-', 'Kehelathah': '-', 'Mount Shepher': '-', 'Haradah': '-', 'Makheloth': '-', 'Tahath': '-', 'Terah': '-', 'Mithkah': '-', 'Hashmonah': '-', 'Moseroth': '-', 'Bene-jaakan': '-', 'Hor-haggidgad': '-', 'Jotbathah': '-', 'Abronah': '-', 'Ezion-geber': '-', 'Kadesh': 'M Num 20:1 (40, 1, 1) + S', 'Mount Hor': 'M Num 20:22 (40, 4, 1) + S; M Num 20:28 (40, 5, 1) the death', 'Zalmonah': '-', 'Punon': '-', 'Oboth': 'S Num 21:10-13', 'Iye-abarim': 'S Num 21:10-13', 'Dibon-gad': 'E cities_built Num 32:34', 'Almon-diblathaim': '-', 'the mountains of Abarim': '-', 'the plains of Moab': 'S Num 22:1 (+ Shittim 25:1)'}
STATIONS = [{'index': i, 'he': PLACES_HE[i], 'en': PLACES_EN[i], 'verse': 'Num 33:%d' % CAMP_VERSE[i], 'first_telling': FIRST_TELLING[PLACES_EN[i]], 'witness': WITNESS[PLACES_EN[i]], 'only_here': PLACES_EN[i] in ONLY_HERE or PLACES_EN[i] in NO_LEMMA} for i in range(42)]
assert sum(1 for s in STATIONS if s['only_here']) == 18 and sum(1 for s in STATIONS if s['first_telling']) == 18 and sum(1 for s in STATIONS if s['witness'] != '-') == 17, (sum(1 for s in STATIONS if s['only_here']), sum(1 for s in STATIONS if s['first_telling']), sum(1 for s in STATIONS if s['witness'] != '-'))
TAPE_CAMPS_MATCHED = ['Succoth', 'Etham', 'Marah', 'Elim', 'the wilderness of Sin', 'Rephidim', 'the wilderness of Sinai', 'Kadesh', 'Mount Hor', 'Oboth', 'Iye-abarim', 'the plains of Moab']   # the encamped_at statuses on the tape that the list names (the design's eleven counted Oboth and Iye-abarim as one line: twelve names on eleven statuses)
TAPE_CAMPS_UNMATCHED = ['Goshen', 'the wilderness of Shur', 'the Red Sea way (21:4)', 'Mattanah to Pisgah (21:18-20)', 'Shittim (25:1)']   # the tape's statuses the list does not name (33:8 says Etham for Shur; 21:18-20's stations absent from the itinerary; Shittim = 33:49's extent)
assert all(c in PLACES_EN for c in TAPE_CAMPS_MATCHED) and not any(c in PLACES_EN for c in TAPE_CAMPS_UNMATCHED)

# ---- THE CALLEES (live import edges; the design's cells by name; every value typed from jou_runner_measure.out) ----
ES_ST = ES.night('stations'); ES_DAY = ES.night('by_day'); ES_TEN = ES.plagues('ten'); ES_REM = ES.plagues('removed')
assert ES_ST['v'] == 9 and ES_ST['fx'] == ['encamped_at'] and ES_DAY['v'] is True and ES_DAY['fx'] == ['brought_out'], (ES_ST, ES_DAY)           # THE CALL: the exodus story's nine stations (its why names Numbers 33's list)
assert ES_TEN['v'] == 10 and ES_REM['v'] == 4 and ES_REM['fx'] == ['plague_removed'] and ES.marah('three_days')['v'] == 3 and ES.sinai('new_moon')['v'] is True and ES.manna('forty_years')['v'] == 40, (ES_TEN, ES_REM)
assert ES.PLAGUES == ['blood', 'frogs', 'lice', 'swarms', 'pestilence', 'boils', 'hail', 'locusts', 'darkness', 'the_firstborn'] and sorted(ES.REMOVED) == ['frogs', 'hail', 'locusts', 'swarms'], (ES.PLAGUES, ES.REMOVED)   # the firstborn's plague has no removal
PS_FB = PS.firstborn({'kind': 'human'}, PS.DATA)
assert PS_FB[0].startswith('redeem (five sela') and PS_FB[1] == ['consecrated_firstborn', 'pays'], PS_FB                                          # THE CALL: the Passover's firstborn
BH_GRAVES = BH.taberah_and_quail({'ask': 'graves'}, BH.DATA); BH_STACK = BH.march({'ask': 'day_stack'}, BH.DATA); BH_YEAR = BH.march({'ask': 'year_turns'}, BH.DATA)
assert BH_GRAVES[0] == 'Kibroth-hattaavah — the graves of lust' and BH_GRAVES[1] == ['buried'] and BH_STACK[0].startswith('the march (2, 2, 20)') and 'Hazeroth on the twenty-second of Sivan; Paran on the twenty-ninth' in BH_STACK[0] and BH_YEAR[0] == 'not in Iyar — Nisan and Iyar in one year', (BH_GRAVES, BH_STACK, BH_YEAR)
SL_HIGH = SL.high_hand({'ask': 'high_hand_posture'}, SL.DATA); SL_FORTY = SL.spies({'ask': 'forty_days'}, SL.DATA); SL_COUNT = SL.decree({'ask': 'count_from'}, SL.DATA); SL_DEATHS = SL.decree({'ask': 'deaths_ceased'}, SL.DATA)
assert SL_HIGH[0] == 'the exodus\'s posture — "with a high hand" (Exod 14:8; Num 33:3)' and SL_FORTY[0].startswith('40 days (13:25)') and SL_COUNT[0].startswith('40 - 38 = 2') and SL_DEATHS[0].startswith('the fifteenth of Av of the fortieth year'), (SL_HIGH, SL_FORTY, SL_COUNT, SL_DEATHS)   # the callee names this chapter's verse
assert CK.AARON_DATE == AARON_DATE and CK.AARON_AGE == [AGE] and CK.DAYS30 == [30] and (CK.D_ZIN, CK.D_HOR, CK.D_AARON, CK.D_DEPART) == (14076, 14165, 14194, 14224), (CK.AARON_DATE, CK.AARON_AGE, CK.DAYS30)   # THE CALL: the chukat runner's date and age — this chapter's own numbers
CK_DATES = CK.edom_and_hor({'ask': 'death_dates'}, CK.DATA); CK_AGE = CK.edom_and_hor({'ask': 'aaron_age'}, CK.DATA); CK_ARAD = CK.edom_and_hor({'ask': 'arad_heard'}, CK.DATA); CK_MOSERAH = CK.edom_and_hor({'ask': 'moserah'}, CK.DATA)
CK_TWO = CK.edom_and_hor({'ask': 'two_mount_hors'}, CK.DATA); CK_THIRTY = CK.edom_and_hor({'ask': 'thirty_days'}, CK.DATA); CK_WALK = CK.edom_and_hor({'ask': 'seder_olam_walk'}, CK.DATA); CK_KISS = CK.meribah({'ask': 'death_by_the_kiss'}, CK.DATA)
assert CK_DATES[0].startswith('Aaron (40, 5, 1) by the ink, aged 123') and CK_AGE[0].startswith('Aaron 123 at his death (33:39 — [123])') and CK_ARAD[0].startswith('Arad heard that Aaron died and the clouds departed'), (CK_DATES, CK_AGE, CK_ARAD)
assert CK_MOSERAH[0].startswith('Moserah — the retreat of seven stations') and CK_TWO[0].startswith('two Mount Hors') and CK_THIRTY[0].startswith("thirty days' weeping") and CK_WALK[0].startswith("the fortieth year's walk: (40, 1, 1) the arrival, three months at Kadesh") and CK_KISS[0].startswith('Miriam too by the kiss'), (CK_MOSERAH, CK_TWO, CK_THIRTY, CK_WALK, CK_KISS)
assert CK.DATA['moserah']['value'] == 'the_retreat_of_seven_stations' and CK.DATA['arad_heard']['value'] == 'that_aaron_died_and_the_clouds_departed' and CK.DATA['death_by_the_kiss']['value'] == 'miriam_too_by_there_there' and CK.DATA['miriam_death_day']['value'] == 'tenth_of_nisan', CK.DATA['moserah']
BK_LAST = BK.the_call({'ask': 'last_camp'}, BK.DATA); BK_SHITTIM = BK.peor({'ask': 'shittim_name'}, BK.DATA)
assert BK_LAST[0].startswith('the plains of Moab — the last camp') and BK_LAST[1] == ['encamped_at'] and BK_SHITTIM[0].startswith("Shittim the place's name (R. Eliezer)") and BK.DATA['shittim_name']['value'] == 'the_place', (BK_LAST, BK_SHITTIM)
C2_LOT = C2.the_land({'ask': 'by_lot'}, C2.DATA); C2_MOUTH = C2.the_land({'ask': 'lots_mouth'}, C2.DATA); C2_NAMES = C2.the_land({'ask': 'by_number_of_names'}, C2.DATA); C2_AMONG = C2.the_land({'ask': 'land_divided_among'}, C2.DATA); C2_HELD = C2.the_land({'ask': 'possession_before_assignment'}, C2.DATA)
assert C2_LOT[0] == 'the place by lot — Joshua 14-19 the run' and C2_LOT[1] == ['commanded'] and C2_MOUTH[0].startswith("the lot's mouth is the oracle's") and C2_NAMES[0].startswith('the size by the count of names'), (C2_LOT, C2_MOUTH, C2_NAMES)   # THE CALL: the lot's cell — 33:54 restates it
assert C2_AMONG[0].startswith('left_egypt (the running setting)') and C2_HELD[0].startswith('in possession before assignment') and C2_HELD[1] == ['holding_owed'] and C2.DATA['division_by']['value'] == 'tribes', (C2_AMONG, C2_HELD)
GR_DIBON = GR.the_cities({'ask': 'dibon_gad'}, GR.DATA); GR_NOTLOT = GR.the_grant({'ask': 'not_by_lot'}, GR.DATA)
assert GR_DIBON[0].startswith("Dibon Gad (33:45-46) — the itinerary's own witness") and GR_NOTLOT[0].startswith("the east by Moses' word, not by lot") and GR.DATA['negative_arm_outcome']['value'] == 'canaan_only_or_gilead_shared', (GR_DIBON, GR_NOTLOT)   # THE CALL: the Gad runner names 33:45-46
ER_MOLTEN = ER.covenant('molten_two_seats'); ER_CALF = ER.calf('molten_calf'); ER_GROWS = ER.covenant('demolition_grows')
assert ER_MOLTEN['v'] == ([('Exod', 34, 17)], [('Lev', 19, 4)]) and ER_MOLTEN['fx'] == ['molten_image_barred'] and ER_CALF['v'] == 4 and ER_GROWS['v'] == [3, 4, 5] and ER_GROWS['fx'] == ['demolished'], (ER_MOLTEN, ER_CALF, ER_GROWS)   # THE CALL: the molten image's ban; the other iconoclasm lists grow 3, 4, 5
HL_MOLTEN = HL.frame('molten_warnings'); HL_LOOK = HL.frame('idols_look')
assert HL_MOLTEN['v'] == ['two_warnings', 'R._Yosei_three'] and HL_LOOK['v'] == 'not_even_to_look_R._Yehuda', (HL_MOLTEN, HL_LOOK)                 # THE CALL: Leviticus 19:4's molten gods
# ---- THE ERA'S YEAR on the engine's Calendar (Rosh Hashanah 2b:9, 3a:5 — the exodus era's new year in the first month) ----
with contextlib.redirect_stdout(io.StringIO()):
    _WC = WE.World(era='the exodus era on the Calendar (the journeys)', epoch='exodus')
_EX = _WC.clock.eras['exodus']
ERA_AV, ERA_SHEVAT, ERA_NISAN2, ERA_IYAR2 = (_EX.date(_WC.clock.day_in('exodus', *d)) for d in ((40, 5, 1), (40, 11, 1), (2, 1, 1), (2, 2, 20)))
assert ERA_AV == (40, 5, 1) and ERA_SHEVAT == (40, 11, 1) and ERA_AV[0] == ERA_SHEVAT[0] == 40 and _WC.clock.day_in('exodus', 40, 11, 1) > _WC.clock.day_in('exodus', 40, 5, 1), (ERA_AV, ERA_SHEVAT)   # Av and the following Shevat in ONE year — not Tishrei (33:38 with Deuteronomy 1:3)
assert ERA_NISAN2 == (2, 1, 1) and ERA_IYAR2 == (2, 2, 20) and ERA_NISAN2[0] == ERA_IYAR2[0] == 2, (ERA_NISAN2, ERA_IYAR2)                          # Nisan and Iyar of the second year in ONE year — not Iyar (Exodus 40:17 with Numbers 10:11)
assert _EX.date(_WC.clock.day_in('exodus', 1, 1, 15)) == DEPARTURE_DATE and _EX.date(_WC.clock.day_in('exodus', 1, 2, 16)) == (1, 2, 16), 'the departure and the manna\'s first day on the Calendar'


# ===== THE DATA CHANNEL — the parameter rows the ink leaves open (motion 2's recorded settings) =========
DATA = {
    'the_stations': {'value': STATIONS, 'settings': {'a_data_list': "THE FORTY-TWO AS A DATA ROW, NOT TAPE LINES (the design's decision on the measurements): a retelling never writes an act twice — sixteen camps stand on the ledger at their first tellings' own days; the chapter's lines land at (40, 6, 1) and a year-one camp cannot carry the record's day; the ink's own verb for the chapter is WROTE (33:2), whose value is the list", 'tape_lines': "the eighteen only-here stations as encamped_at statuses at (40, 6, 1) — REFUSED: false on the clock (no day of their own in the ink)"},
                     'source': "33:5-49 — the forty-two places cut from the verbs' after-tokens on the DB; each place's first telling by its lemma's seats; the tape's witness from the running world's markers and statuses (jou_compile_measure.out)"},
    'the_four_writings': {'value': ['Exod 24:4', 'Num 33:2', 'Deut 31:9', 'Deut 31:22'], 'settings': {'four': "'and Moses wrote' at four Torah seats — the covenant's words (Exodus 24:4), THE JOURNEYS (33:2), this Torah (Deuteronomy 31:9), this song (31:22); the tablets at Exodus 34:28 and Deuteronomy 10:4 the verb's other two seats (the LORD's writing)"},
                          'source': "33:2 'and Moses wrote' — the phrase's seats computed (WROTE)"},
    'the_morrow_of_the_passover': {'value': 'the_omer_then_the_produce', 'settings': {'the_omer_then_the_produce': "Joshua 5:11 'they ate of the produce of the land on the morrow of the Passover' — they brought the omer and only afterward ate (Kiddushin 37b:14-38a:1: the new crop's 'dwelling' is wherever you dwell)", 'the_manna_sufficed': "they did not need the new produce, for they still had manna (Kiddushin 38a:2) — the manna's end the morrow's meaning (38a:3-4: forty years less thirty days, the sixteenth of Iyar to the sixteenth of Nisan; Joshua 5:12 'the manna ceased on the morrow')"},
                                   'source': "33:3 'on the morrow of the Passover' and Joshua 5:11 — THE PHRASE'S TWO BIBLE SEATS (MORROW): the going out of Egypt and the land's bread on one date-word; Seder Olam Rabbah 10:2 the same reckoning"},
    'the_judgments_on_the_gods': {'value': 'recorded_at_33_4_alone', 'settings': {'recorded_at_33_4_alone': "Exodus 12:12 'on all the gods of Egypt I will execute judgments' THE SPEC (the future at 12:12 and Ezekiel 25:11 alone); Exodus narrates the firstborn struck (12:29) and never the gods; 'and on their gods the LORD executed judgments' (33:4) the perfect's ONE seat — the run recorded forty years on, in the itinerary; Onkelos 'on their idols'"},
                                  'source': "33:4 against Exodus 12:12 — the verb's forms computed (JUDG_PERF, JUDG_FUT, the noun's sixteen seats); NO entry on the tape before 33:4 carries the judgments (measured)"},
    'the_deuteronomy_order': {'value': 'the_retreat_of_seven_stations', 'settings': {'the_retreat_of_seven_stations': "Deuteronomy 10:6 'from Beeroth-bene-jaakan to Moserah; THERE Aaron died' against 33:30-31 (Moseroth then Bene-jaakan) and 33:37-38 (the death at Mount Hor): after Arad's attack they retreated seven stations to Moserah and the mourning was renewed there (Seder Olam Rabbah 9:2 — 'did Aaron die in Moserah? did he not die at Mount Hor? rather, from where Aaron died they retreated seven stations') — the chukat runner's row CK.DATA['moserah'] READ", 'the_ink_alone': "two orders in the ink, no rule between them — Deuteronomy's Beeroth-bene-jaakan and Gudgodah another lemma from 33:31-32's Bene-jaakan and Hor-haggidgad"},
                              'source': "33:30-38 against Deuteronomy 10:6-7 — MOSEROTH SEVEN CAMPS BEFORE MOUNT HOR BY INDEX (computed on the list): the shelf's seven = the ink's seven"},
    'arads_hearing': {'value': CK.DATA['arad_heard']['value'], 'settings': dict(CK.DATA['arad_heard']['settings'], **{'sihon_arad_canaan_one_person': "Rosh Hashanah 3a:3 — 'he is Sihon, he is Arad, he is Canaan': one person under three names (the foal, the kingdom, the real name Arad — or the wild ass, the kingdom, the real name Sihon): the hearer's identity DISPUTED; Taanit 9a's Amalek in disguise the registry row's other reading"}),
                      'source': "33:40 'and the Canaanite king of Arad heard' — 21:1's hearing without the war, the captives, the vow and Hormah, WITH 'in the land of Canaan'; CK's row READ by CALL (Rosh Hashanah 3a:1; Taanit 9a:10; Seder Olam Rabbah 9:2)"},
    'aarons_age': {'value': 123, 'settings': {'83_plus_40': "Aaron 83 at the speaking before Pharaoh (Exodus 7:7 — [80, 83]) + the era's fortieth year = 123 (33:39 — [123]); Moses 80 + 40 = 120 (Deuteronomy 34:7 — [120]): the brothers three years apart at both ends, THE INK'S OWN CHECKSUM; Kiddushin 38a:7 — 'a hundred and twenty years old THIS DAY': the years of the righteous completed to the day (Exodus 23:26)"},
                   'source': "33:39 by the same parser as Exodus 7:7 and Deuteronomy 34:7 (RETOLD); CK.AARON_AGE READ"},
    'the_death_date': {'value': AARON_DATE, 'settings': {'ordinal_reader': "33:38 'in the fortieth year … in the fifth month, on the first of the month' — the year and the month article-bearing ORDINALS [40, 5], the day [1]: THE TAPE'S OWN MARKER at 20:28 is built from this verse (cold_run_sequence.py); Deuteronomy 1:3's fortieth-year date is CARDINAL ([40, 11, 1] by the number reader): the two date forms have two readers", 'first_of_av_or_tammuz': "Seder Olam Rabbah 10:2 'Aaron on the first of Av' with the export's note of the French manuscripts' 'first of Tammuz' — a variant on the month the ink fixes as the fifth (OBSERVED, RESEARCH_LOG)"},
                       'source': "33:38 — the ordinals and the number computed (ORDS, INTS); CK.AARON_DATE READ; the marker at Num 20:28 on the tape (CZ5)"},
    'the_eras_stamps': {'value': ['Exod 19:1', 'Num 33:38', '1Kgs 6:1'], 'settings': {'three_stamps': "'of the going out of the children of Israel from the land of Egypt' at THREE Bible seats — Exodus 19:1 (the third month), Numbers 33:38 (the fortieth year), 1 Kings 6:1 (the 480th year — [480] with the ordinal [2] by the parser): the era's own dating form; Rosh Hashanah 2b:7-3a:13 reads the three in one chain to prove the New Year for the exodus count and the kings is Nisan (2b:9 — Av and the following Shevat both 'the fortieth year'; 2b:11 the verbal analogy 'the fortieth year' TAUGHT for Deuteronomy 1:3's bare date; 3a:5 Nisan and Iyar both 'the second year'; 3a:6 'the third month' without 'the second year')"},
                        'source': "33:38 — the phrase's three seats computed (STAMPS); the engine's Calendar with the exodus era's new year in the first month reproduces the chain (ERA_AV, ERA_SHEVAT, ERA_NISAN2, ERA_IYAR2)"},
    'the_camps_extent': {'value': 'three_parasangs', 'settings': {'three_parasangs': "'from Beth-jeshimoth to Abel-shittim' (33:49) — Rabba bar bar Chana in R. Yochanan's name: 'I saw that place, three parasangs by three' (twelve mil) — Eruvin 55b:15 (Rav Chisda's objection), Yoma 75b:14 (the baraita on relieving oneself behind the camp)"},
                         'source': "33:49 — the itinerary's ONE camp with two ends (Beth-jeshimoth one seat; Abel-shittim one seat of the full name); the shelf's measure a witness's"},
    'the_three_objects': {'value': ['figured_stones', 'molten_images', 'high_places'], 'settings': {'figured_stones': "Leviticus 26:1's word (the lemma's six Bible seats: Lev 26:1, Num 33:52, Ezek 8:12, Ps 73:7, Prov 18:11, 25:11) — the ban 'a figured stone you shall not install in your land to bow upon it': Ulla, bowing on a stone floor outside the Temple with outstretched arms and legs (Megillah 22b:11-13); THE CELL THAT COMPILES LEVITICUS 26:1 DOES NOT EXIST (measured) — journeys → tochacha OWED, the rows filed to the debt", 'molten_images': "the calf's word (Exodus 32:4, 32:8; Deuteronomy 9:12, 9:16) and the ban's — 'molten gods you shall not make for yourself' (Exodus 34:17; Leviticus 19:4 with the vav; Deuteronomy 27:15 the curse): ER.covenant('molten_two_seats') and HL.frame('molten_warnings') by CALL; aaron's molten_image_barred block on the tape (Exodus 32:4)", 'high_places': "Leviticus 26:30's curse in the same verb on the same object — 'I will DESTROY your high places' / 'their high places you shall DEMOLISH' (the verb's two Torah seats; the noun's five): the Canaanites' — ANOTHER SENSE than the private altar's eras (Mishnah Zevachim 14:4-8: Israel's own altars permitted and forbidden by era — the erection runner's high_places_banned block on the land); 'their high places' the consonants of 'at their death' (Leviticus 11:31-32, Numbers 6:7 — the morphology decides)"},
                          'source': "33:52 — the three objects' tokens and their seats computed; the other iconoclasm commands (Exodus 23:24, 34:13, Deuteronomy 7:5, 12:2-3) name altars, pillars, asherim and graven images — ER.covenant('demolition_grows') [3, 4, 5] by CALL: 33:52's three are its own list"},
    'the_lot_restated': {'value': 'plural_then_singular', 'settings': {'plural_then_singular': "33:54 restates 26:52-56 TO THE PEOPLE: 'you (plural) shall inherit … to the many you (PLURAL) shall give more … to the few you (SINGULAR) shall give less' — the number switches inside the verse (26:54 'to the many you shall give more' singular): computed on the morphology (MORPH_54); Onkelos makes both plural; C2.the_land('by_lot' / 'by_number_of_names') by CALL, C2.DATA['division_by'] = tribes READ; the OPEN divide_the_land debit (26:52-56) CITED, NOT REWRITTEN"},
                         'source': "33:54 against 26:52-56 — the shared clauses computed (BY_LOT_T, MANY, LOT_OUT, TRIBES_FATHERS); Bava Batra 117a:2-3, 117b:1 (left Egypt / entered / both), 122a:3 (the lot and the Urim) credited"},
    'negative_arm_outcome': {'value': 'thorns_in_your_eyes_and_pricks_in_your_sides', 'settings': {'thorns_in_your_eyes_and_pricks_in_your_sides': "33:55 'those you leave of them shall be thorns in your eyes and pricks in your sides, and they shall harass you on the land' — run back REVERSED by Joshua 23:13 ('a snare and a trap, a scourge in your sides and pricks in your eyes') and Judges 2:3 ('for sides, and their gods a snare'); 33:56 'as I thought to do to them, I will do to you' (Isaiah 14:24's phrase); Onkelos: bands taking up arms against you and camps surrounding you", 'sauls_amalek_and_haman': "Megillah 11a:13-14 — R. Levi and R. Chiyya open Esther from 33:55-56: Saul's failure to finish Amalek left Haman as the thorn; Purim's punishment 'as I thought to do to them' — the arm's runs on the shelf beyond Joshua and Judges", 'the_crossings_purpose': "Sotah 34a:5 — Joshua in the Jordan: 'know for what purpose you cross — to drive out the inhabitants (33:52); if not, the water will drown me and you': the debit's first run-reading with the negative arm as its condition"},
                             'source': "33:55-56 — the ink's three seats (THORNS, PRICKS, PRICKS_EYES, SIDES_JUDG, THOUGHT); NO verdict on the tape — the arm a DATA row; GR.DATA['negative_arm_outcome'] the chapter-32 arm beside it"},
}


# ===== F1: THE HEADING AND THE WRITING (Num 33:1-2) ===========================================================
def the_heading_and_the_writing(case, data):
    del P[:]
    ask = case['ask']
    if ask == 'heading':
        ink('33:1', '"these are the journeys of the children of Israel" — %s (10:28 the same four words: "these are the journeys of the children of Israel by their hosts, and they journeyed"); %d verse-initial "these" headings in the Torah' % (HEAD, len(HEADINGS)))
        return out("these are the journeys of the children of Israel (33:1) — 10:28's four words; sixty-three headings in the Torah", ['accepted'])
    if ask == 'by_their_hosts':
        ink('33:1', '"by their hosts" — %d seats, every one in Numbers (%s … %s)' % (len(HOSTS), HOSTS[0], HOSTS[-1]))
        return out("by their hosts (33:1) — sixteen seats, all in Numbers", ['accepted'])
    if ask == 'by_the_hand':
        ink('33:1', '"by the hand of Moses and Aaron" — %s: the phrase\'s two Bible seats; Psalm 77:21 "You led Your people like a flock by the hand of Moses and Aaron" OBSERVED, no link' % HAND)
        return out("by the hand of Moses and Aaron (33:1) — Psalm 77:21 the phrase's other seat, observed", ['accepted'])
    if ask == 'moses_wrote':
        ink('33:2', '"and Moses wrote" — %s: THE FOUR WRITINGS (the covenant\'s words, the journeys, this Torah, this song); the tablets Exodus 34:28 and Deuteronomy 10:4 the verb\'s other two' % WROTE)
        dat('the row the_four_writings: %s' % data['the_four_writings']['value'])
        return out("and Moses wrote (33:2) — the four writings: Exodus 24:4, Numbers 33:2, Deuteronomy 31:9, 31:22", ['journeys_recorded'])
    if ask == 'by_the_mouth':
        ink('33:2, 38', '"by the mouth of the LORD" — %d Bible seats, %d in the Torah, %d in Numbers; Moses WROTE by it (33:2) and Aaron WENT UP by it (33:38); Onkelos "by the WORD of the LORD" at both' % (len(MOUTH), len(MOUTH_T), len(MOUTH_N)))
        move('Bava Batra 17a:3', 'six over whom the Angel of Death had no sway — Moses, Aaron and Miriam died BY THE MOUTH OF THE LORD (33:38; Deuteronomy 34:5): the kiss')
        move('cold_run_chukat (CALL) — CK.meribah(death_by_the_kiss) = %s' % CK_KISS[0], "the chukat runner's row death_by_the_kiss READ")
        return out("by the mouth of the LORD — twenty-one Bible seats; Moses wrote by it (33:2), Aaron went up by it (33:38), and died by it on the shelf (Bava Batra 17a:3)", ['accepted'])
    if ask == 'the_chiasm':
        ink('33:2', '"their goings out by their journeys … their journeys by their goings out" — %s / %s; "their goings out" %s (Jeremiah 50:7 the other seat); "by their journeys" %s (the cloud\'s stages at Exodus 17:1, Numbers 10:6, 10:12)' % (words(33, 2)[3:5], words(33, 2)[9:11], GOINGS, JOURNEYS_L))
        return out("their goings out by their journeys, their journeys by their goings out (33:2) — the chiasm; 'their goings out' two Bible seats, 'by their journeys' four", ['accepted'])
    if ask == 'the_list':
        ink('33:2, 5-49', 'the writing\'s VALUE — %d places: %s … %s; %d named nowhere else; %d with a first telling outside the chapter; %d with a witness on the tape' % (len(STATIONS), STATIONS[0]['en'], STATIONS[-1]['en'], sum(1 for s in STATIONS if s['only_here']), sum(1 for s in STATIONS if s['first_telling']), sum(1 for s in STATIONS if s['witness'] != '-')))
        dat('the row the_stations: a DATA LIST, not tape lines — a retelling never writes a camp twice; the record\'s day the writing\'s')
        return out("the journeys recorded — forty-two places as the writing's value: Rameses and forty-one camps, eighteen named nowhere else, eighteen with a first telling, seventeen with a witness on the tape", ['journeys_recorded'])
    return out('no verdict in span', [FX.NONE])


# ===== F2: THE DEPARTURE (Num 33:3-4) — the tape's own date; the run of Exodus 12:12 recorded here alone ========
def the_departure(case, data):
    del P[:]
    ask = case['ask']
    if ask == 'the_date':
        ink('33:3', '"from Rameses in the first month, on the fifteenth day of the first month" — [%d] with the ordinals %s = %s; the full phrase %s (one seat); "from Rameses" %s' % (FIFTEEN, ORDS[3], DEPARTURE_DATE, FIFTEENTH, FROM_RAMESES))
        move('the Calendar (the exodus era registered at Exodus 12:2)', 'day_in(1, 1, 15) reads back %s — the tape\'s exodus marker at Exodus 12:29 and 12:41 (CZ3)' % (_EX.date(_WC.clock.day_in('exodus', 1, 1, 15)),))
        return out("the fifteenth day of the first month (33:3) = (1, 1, 15) — the tape's exodus marker; a retelling's date is a checkpoint, never a second marker", ['accepted'])
    if ask == 'the_morrow':
        ink('33:3', '"on the morrow of the Passover" — %s: the phrase\'s two Bible seats, the going out of Egypt and the land\'s bread (Joshua 5:11); the Passover\'s lemma at %s' % (MORROW, PASSOVER_LEMMA))
        move('Kiddushin 37b:14-38a:2', "the new crop's 'dwelling' wherever you dwell — they ate on the morrow after the omer (38a:1); or the manna sufficed (38a:2)")
        dat('the row the_morrow_of_the_passover: %s' % data['the_morrow_of_the_passover']['value'])
        return out("on the morrow of the Passover — 33:3 and Joshua 5:11 the phrase's two seats: the run's two ends on one date-word; the omer's arm and the manna's", ['accepted'])
    if ask == 'left_by_day':
        ink('33:3', '"on the morrow of the Passover the children of Israel went out with a high hand in the sight of all Egypt" — "in the sight of all Egypt" %s (one seat)' % SIGHT)
        move('Berakhot 9a:25', 'R. Abba: redeemed at evening (Deuteronomy 16:1), LEFT BY DAY — 33:3 the proof')
        move('cold_run_exodus_story (CALL) — ES.night(by_day) = %s' % ES_DAY['v'], "'on that very day' (12:51): they went out by day only (Mekhilta)")
        return out("left by day (33:3) — redeemed at evening, went out by day (Berakhot 9a:25); the exodus story's by_day by CALL", ['accepted'])
    if ask == 'high_hand':
        ink('33:3', '"with a high hand" — %s: three Torah seats (Exodus 14:8 the same going out; 15:30 the Sifrei 112:2\'s verse; here); Onkelos "with bared head" at 15:30 and 33:3 alone' % HIGH_HAND)
        move('cold_run_shelach (CALL) — SL.high_hand(high_hand_posture) = %s' % SL_HIGH[0], 'the callee names this chapter\'s verse')
        return out("with a high hand (33:3) — Exodus 14:8's posture at the same going out, 15:30's the high-hand sinner's; the shelach runner names 33:3", ['accepted'])
    if ask == 'the_burial':
        ink('33:4', '"and Egypt was burying those whom the LORD had struck among them, every firstborn" — "was burying" %s (the participle\'s two seats); "every firstborn" %d seats' % (BURYING, len(EVERY_FB)))
        move('cold_run_exodus_story (CALL) — ES.plagues(ten) = %d, (removed) = %d; ES.PLAGUES[-1] = %s; the removed %s' % (ES_TEN['v'], ES_REM['v'], ES.PLAGUES[-1], sorted(ES.REMOVED)), 'ten struck, four removed by a narrated removal — the firstborn\'s has none: A BURIAL IS NOT A REMOVAL, the entry stays OPEN (CZ4)')
        move('cold_run_pesach (CALL) — PS.firstborn(human) = %s' % PS_FB[0], "the Passover's firstborn cell live")
        return out("Egypt was burying every firstborn (33:4) — the plague's aftermath: the firstborn's plague_struck entry stays open, a burial is no removal (ten struck, four removed)", ['accepted'])
    if ask == 'the_gods_judged':
        ink('33:4', '"and on their gods the LORD executed judgments" — the perfect %s (ONE Bible seat); the future "I will execute judgments" %s (Exodus 12:12 THE SPEC, Ezekiel 25:11); the noun\'s %d seats' % (JUDG_PERF, JUDG_FUT, len(JUDG_LEMMA)))
        dat('the row the_judgments_on_the_gods: %s — Exodus narrates the firstborn and never the gods; NO entry on the tape before 33:4 carries the judgments (measured): the act\'s FIRST telling, forty years on' % data['the_judgments_on_the_gods']['value'])
        return out("on their gods the LORD executed judgments (33:4) — the run of Exodus 12:12 recorded here alone: a status on Egypt written forty years on, the act's first telling", ['judgments_executed_on_their_gods'])
    if ask == 'the_manna':
        move('Kiddushin 38a:3-4', 'the manna forty years less thirty days — from the sixteenth of Iyar of the first year to the sixteenth of Nisan of the fortieth; the cakes taken out on the fifteenth of Nisan tasted of manna thirty days')
        move('cold_run_exodus_story (CALL) — ES.manna(forty_years) = %d' % ES.manna('forty_years')['v'], "'until they came to an inhabited land' (Exodus 16:35) — the provision's span past the three books")
        ink('33:3', 'the Calendar: the manna\'s first morning %s = the tape\'s marker at Exodus 16:13; the cakes\' day %s = the exodus marker' % (_EX.date(_WC.clock.day_in('exodus', 1, 2, 16)), DEPARTURE_DATE))
        return out("the manna forty years less thirty days (Kiddushin 38a:3-4) — from (1, 2, 16), the tape's marker at Exodus 16:13, to the sixteenth of Nisan; the cakes of 33:3's fifteenth thirty days", ['accepted'])
    return out('no verdict in span', [FX.NONE])


# ===== F3: THE STATIONS (Num 33:5-37, 41-49) — the list against its first tellings, on the tokens ============
def the_stations(case, data):
    del P[:]
    ask = case['ask']
    if ask == 'forty_two':
        ink('33:3-49', '%d places = the forty-one departures\' places (Rameses told twice, 33:3 and 33:5) + the last camp; the departures\' from-tokens and the camps\' at-tokens the instrument' % len(PLACES_HE))
        return out("forty-two places (33:3-49) — Rameses and forty-one camps: the first departure and the last camp each told twice", ['accepted'])
    if ask == 'the_verbs':
        ink('33:3-49', '"journeyed" in %d verses (%s …), "camped" in %d (… %s); %d verses with both; 33:3 the journey alone (the date line), 33:49 the camp alone (the last camp\'s extent)' % (len(JOURNEYED), JOURNEYED[:3], len(CAMPED), CAMPED[-3:], len(set(JOURNEYED) & set(CAMPED))))
        return out("forty-two 'journeyed' and forty-two 'camped' — forty-one verses with both; 33:3 the journey alone, 33:49 the camp alone", ['accepted'])
    if ask == 'exodus_nine':
        move('cold_run_exodus_story (CALL) — ES.night(stations) = %d, its effects %s' % (ES_ST['v'], ES_ST['fx']), "the exodus story's nine encampments (Succoth, Etham, Pi-hahiroth, Shur, Marah, Elim, Sin, Rephidim, Sinai) — its why names Numbers 33's list as the run's citation")
        ink('33:5-15', 'the tape\'s witnesses among them: %s' % [(s['en'], s['witness']) for s in STATIONS[:12] if s['witness'] != '-'])
        return out("the exodus story's nine stations by CALL — Succoth to Sinai on the tape as statuses and markers; the itinerary's list their run citation", ['accepted'])
    if ask == 'etham_for_shur':
        ink('33:8', '"a way of three days in the wilderness of ETHAM" for Exodus 15:22\'s "wilderness of SHUR" — %s / %s (each one seat with its prefix); the bare pair "מדבר אתם" at %s is "speaking with them" — A HOMOGRAPH (the measure\'s find); "a way of three days" %s' % (words(33, 8)[11:13], SHUR, ETHAM_HOMOGRAPH, THREE_DAYS))
        move('cold_run_exodus_story (CALL) — ES.marah(three_days) = %d' % ES.marah('three_days')['v'], "the tape's marker at Shur (1, 1, 24)")
        return out("the wilderness of Etham (33:8) for Exodus 15:22's Shur — each one seat; 'a way of three days' six Torah seats; Exodus 34:33's 'speaking with them' a homograph", ['accepted'])
    if ask == 'one_word_added':
        ink('33:6', '33:6 %s IS Exodus 13:20 %s with ONE word added ("which")' % (words(33, 6), words(13, 20, 'Exod')))
        return out("33:6 is Exodus 13:20 with one word added — the itinerary retelling its first telling on the tokens", ['accepted'])
    if ask == 'elim':
        ink('33:9', '"twelve springs of water and seventy palm trees" — %s / %s: word for word with Exodus 15:27; the parser [%d, %d] at both' % (SPRINGS, PALMS, TWELVE, SEVENTY))
        return out("Elim's twelve springs and seventy palms (33:9) word for word with Exodus 15:27 — [12, 70] at both", ['accepted'])
    if ask == 'unnamed_in_exodus':
        ink('33:10-13', 'THE CAMP BY THE RED SEA (33:10 — "the Red Sea" %d Torah seats, the camp Exodus never names), DOPHKAH and ALUSH (33:12-13) — three stations between Elim and Rephidim that Exodus does not tell' % len(RED_SEA_T))
        return out("the Red Sea camp, Dophkah and Alush (33:10-13) — three stations Exodus never names", ['accepted'])
    if ask == 'kibroth_hazeroth':
        move('cold_run_beha (CALL) — BH.taberah_and_quail(graves) = %s; BH.march(day_stack) = %s' % (BH_GRAVES[0], BH_STACK[0]), "the naming 11:34 ('buried' on the tape); Hazeroth (2, 3, 22) and Paran (2, 3, 29) the tape's markers")
        ink('33:16-17', 'Kibroth-hattaavah and Hazeroth — 11:34-35\'s names; Onkelos "the graves of those who demanded" at all four seats')
        return out("Kibroth-hattaavah and Hazeroth (33:16-17) — chapter 11's graves and Hazeroth by CALL: the burial on the tape, the markers at (2, 3, 22) and (2, 3, 29)", ['accepted'])
    if ask == 'rithmah_paran':
        ink('33:18', '"Rithmah" %s — one seat: 12:16\'s "wilderness of Paran" under another name, the spies\' base (13:3 "from the wilderness of Paran", 13:26 "to Paran, to Kadesh"); Taberah no station' % RITHMAH)
        move('cold_run_shelach (CALL) — SL.spies(forty_days) = %s' % SL_FORTY[0], 'the forty days from the base; the tape\'s marker at 12:16 (2, 3, 29)')
        return out("Rithmah (33:18) — Paran under another name: the spies' base of 12:16, 13:3, 13:26; the tape's marker at (2, 3, 29)", ['accepted'])
    if ask == 'only_here':
        ink('33:10-46', '%d stations by lemma with no seat outside the chapter — %s; the eighteenth %s (a common noun, no proper-name lemma)' % (len(ONLY_HERE), ONLY_HERE, NO_LEMMA))
        return out("eighteen stations named nowhere else — seventeen by lemma (Dophkah to Almon-diblathaim) and the Red Sea camp", ['accepted'])
    if ask == 'common_word_names':
        ink('33:20, 26, 27', 'Libnah (the Judah city\'s lemma — Joshua 10:29 its first seat), Tahath (a Chronicles person\'s), Terah (Abraham\'s father\'s) — three names whose lemma\'s other seats are ANOTHER referent; Mount Shepher, Haradah, Tahath common words by consonants')
        return out("Libnah, Tahath, Terah (33:20, 26, 27) — three names whose lemma's other seats are another referent", ['accepted'])
    if ask == 'moseroth_seven':
        ink('33:30-38', 'Moseroth index %d, Mount Hor index %d — SEVEN CAMPS APART on the list; Deuteronomy 10:6 %s "there Aaron died", 10:7 %s' % (PLACES_EN.index('Moseroth'), PLACES_EN.index('Mount Hor'), words(10, 6, 'Deut')[3:9], words(10, 7, 'Deut')[:6]))
        move('Seder Olam Rabbah 9:2', "'did Aaron die in Moserah? did he not die at Mount Hor? rather, from where Aaron died they retreated seven stations until Moserah' — the shelf's seven = the ink's seven")
        move('cold_run_chukat (CALL) — CK.edom_and_hor(moserah) = %s; CK.DATA[moserah] = %s' % (CK_MOSERAH[0], CK.DATA['moserah']['value']), "the chukat runner's row READ")
        dat('the row the_deuteronomy_order: %s' % data['the_deuteronomy_order']['value'])
        return out("Moseroth seven camps before Mount Hor (33:30-37) — Deuteronomy 10:6's 'there Aaron died' at Moserah reconciled by the retreat of seven stations (Seder Olam Rabbah 9:2; the chukat runner's row)", ['accepted'])
    if ask == 'kadesh_hor':
        ink('33:36-37', '"in the wilderness of Zin, that is Kadesh" — the pair %s: Genesis 14:7 and here THE PLACE, Exodus 30:32, Leviticus 25:12, 27:30 "it is HOLY" — a homograph the reading\'s "five seats of the identity idiom" did not name (filed); "in the edge of the land of Edom" %s beside 20:23\'s "border" %s; "Mount Hor" bare at %s' % (THAT_IS_KADESH, EDGE_EDOM, BORDER_EDOM, HOR))
        move('cold_run_chukat (CALL) — CK.edom_and_hor(two_mount_hors) = %s' % CK_TWO[0], "Aaron's at Edom's border, the northern border's (34:7-8)")
        return out("Kadesh and Mount Hor (33:36-37) — 'that is Kadesh' with Genesis 14:7 (three of the pair's five seats read 'it is holy': a homograph); the edge of Edom one seat; two Mount Hors by CALL", ['accepted'])
    if ask == 'chapter_21':
        ink('33:41-47', 'Zalmonah and Punon named here alone (21:4 names no camp before Oboth); Oboth and Iye-abarim 21:10-11\'s; of 21:18-20\'s stations (Mattanah, Nahaliel, Bamoth, Pisgah) NOT ONE in the itinerary; Dibon-gad %s / %s; "the mountains of Abarim" %s beside 27:12\'s "the mountain of Abarim" %s' % (words(33, 45)[-2:], words(33, 46)[1:3], ABARIM_PL, ABARIM_SG))
        move('cold_run_gad_reuben (CALL) — GR.the_cities(dibon_gad) = %s' % GR_DIBON[0], "the Gad runner's own cell names 33:45-46")
        return out("the last stations against chapter 21 — Zalmonah and Punon only here; Oboth and Iye-abarim shared; 21:18-20's stations absent; Dibon Gad the Gad runner's own witness by CALL; the mountains of Abarim before Nebo", ['accepted'])
    if ask == 'the_last_camp':
        ink('33:48-49', '"the plains of Moab by the Jordan at Jericho" — "by the Jordan at Jericho" %s; "from Beth-jeshimoth to Abel-shittim" — Beth-jeshimoth %s, the full Abel-shittim one seat (%s the short name\'s)' % (JERICHO, BETH_J, SHITTIM))
        move('cold_run_balak (CALL) — BK.the_call(last_camp) = %s; BK.peor(shittim_name) = %s' % (BK_LAST[0], BK_SHITTIM[0]), "the last camp; Shittim's name")
        move('Eruvin 55b:15; Yoma 75b:14', "Rabba bar bar Chana: 'I saw that place — three parasangs by three'")
        dat('the row the_camps_extent: %s' % data['the_camps_extent']['value'])
        return out("the plains of Moab (33:48-49) — the last camp by CALL; from Beth-jeshimoth to Abel-shittim three parasangs on the shelf (Eruvin 55b:15; Yoma 75b:14)", ['accepted'])
    if ask == 'directional_ending':
        ink('33:46-47', '"Diblathaimah" %s — the directional ending on the station\'s name (Elimah at 33:9 the same form)' % DIBLATHAIMAH)
        move('Yevamot 13b:6', "R. Nechemya: a word needing a lamed at its head takes a heh at its end — 'Diblathaimah' among the examples")
        return out("Diblathaimah (33:46-47) — the directional ending on the station's name (Yevamot 13b:6's example)", ['accepted'])
    if ask == 'tape_matched':
        ink('33:5-49', 'the tape\'s camps the list names: %s; the tape\'s statuses the list does not name: %s' % (TAPE_CAMPS_MATCHED, TAPE_CAMPS_UNMATCHED))
        return out("the tape's camps against the list — twelve names matched (Succoth to the plains of Moab), five statuses not (Goshen, Shur, the Red Sea way, Mattanah to Pisgah, Shittim)", ['accepted'])
    return out('no verdict in span', [FX.NONE])


# ===== F4: AARON'S DEATH RETOLD (Num 33:38-40) — the tape's own marker; no write =============================
def aarons_death_retold(case, data):
    del P[:]
    ask = case['ask']
    if ask == 'the_date':
        ink('33:38', '"in the fortieth year of the going out … in the fifth month, on the first of the month" — the ordinals %s and the day [%d] = %s; "in the fortieth year" %s; "in the fifth month" %s (the Torah\'s one)' % (ORDS[38], DAY_ONE, AARON_DATE, FORTIETH, FIFTH))
        move('cold_run_chukat (CALL) — CK.AARON_DATE = %s; CK.edom_and_hor(death_dates) = %s' % (CK.AARON_DATE, CK_DATES[0]), "the tape's marker at 20:28 is built from this verse (CZ5)")
        dat('the row the_death_date: %s' % (data['the_death_date']['value'],))
        return out("Aaron died on (40, 5, 1) (33:38) — the tape's marker at 20:28, built from this verse; the ordinal reader's year and month", ['accepted'])
    if ask == 'the_age':
        ink('33:39', '"a hundred and twenty-three years at his death" — [%d]; Exodus 7:7 [%d, %d]: %d + %d = %d; Moses %d + %d = %d (Deuteronomy 34:7 [%d]); "at his death" %s' % (AGE, MOSES_80, AARON_83, AARON_83, YEAR, AGE, MOSES_80, YEAR, MOSES_120, MOSES_120, AT_DEATH))
        move('cold_run_chukat (CALL) — CK.AARON_AGE = %s; CK.edom_and_hor(aaron_age) = %s' % (CK.AARON_AGE, CK_AGE[0]), "the chukat runner's age READ")
        dat('the row aarons_age: %s' % data['aarons_age']['value'])
        return out("Aaron 123 at his death (33:39) = Exodus 7:7's 83 + 40; Moses 120 = 80 + 40 — the brothers three years apart at both ends, the ink's checksum", ['accepted'])
    if ask == 'the_eras_stamps':
        ink('33:38', '"of the going out of the children of Israel from the land of Egypt" — %s: THE ERA\'S THREE STAMPS; 1 Kings 6:1 by the parser [%d] with the ordinal %s' % (STAMPS, KINGS_480, RETOLD[('1Kgs', 6, 1)][1]))
        move('Rosh Hashanah 2b:7, 3a:11', "R. Yochanan: kings' years from Nisan — 1 Kings 6:1 juxtaposes Solomon's reign to the going out; the baraita's chain 1 Kings 6:1, Numbers 33:38, Deuteronomy 1:3")
        dat('the row the_eras_stamps: %s' % data['the_eras_stamps']['value'])
        return out("the era's three stamps — Exodus 19:1, Numbers 33:38, 1 Kings 6:1 (the 480th year): the shelf's own chain of proof (Rosh Hashanah 2b:7, 3a:11)", ['accepted'])
    if ask == 'the_era_new_year':
        ink('33:38 / Deuteronomy 1:3', 'the fortieth year in Av %s and in Shevat %s — ONE year on the Calendar; the second year in Nisan %s and Iyar %s — one year' % (ERA_AV, ERA_SHEVAT, ERA_NISAN2, ERA_IYAR2))
        move('Rosh Hashanah 2b:9, 3a:5-6', "Av and the following Shevat both 'the fortieth year' — the exodus count's New Year is not Tishrei; Nisan and Iyar both 'the second year' — not Iyar; 'the third month' without 'the second year' — not Sivan")
        move('cold_run_beha (CALL) — BH.march(year_turns) = %s' % BH_YEAR[0], "the beha runner's own row")
        return out("the era's new year from the chapter's date — (40, 5, 1) and (40, 11, 1) in one year, (2, 1, 1) and (2, 2, 20) in one year on the Calendar: not Tishrei, not Iyar (Rosh Hashanah 2b:9, 3a:5)", ['accepted'])
    if ask == 'verbal_analogy':
        ink('33:38 / Deuteronomy 1:3', 'the ordinal date %s (the article-bearing year and month) against the cardinal date %s (the number reader\'s) — THE TWO DATE FORMS HAVE TWO READERS' % (AARON_DATE, SHEVAT_DATE))
        move('Rosh Hashanah 2b:10-11', "33:38's epoch EXPLICIT ('of the going out from the land of Egypt'), Deuteronomy 1:3's bare — the verbal analogy 'the fortieth year' / 'the fortieth year' (Rav Pappa's form): a TRANSFER TAUGHT, the teacher named")
        return out("the fortieth year / the fortieth year — Deuteronomy 1:3's bare date counted from the exodus by the verbal analogy with 33:38 (Rosh Hashanah 2b:11, taught); the two date readers meet", ['accepted'])
    if ask == 'by_the_mouth_kiss':
        ink('33:38', '"Aaron the priest went up Mount Hor BY THE MOUTH OF THE LORD and died there" — the phrase\'s seat at the death')
        move('Bava Batra 17a:3', 'Moses, Aaron and Miriam died by the mouth of the LORD (33:38; Deuteronomy 34:5) — the kiss, not the Angel of Death')
        move('cold_run_chukat (CALL) — CK.DATA[death_by_the_kiss] = %s' % CK.DATA['death_by_the_kiss']['value'], "the chukat runner's row: Miriam too, by 'there' / 'there'")
        return out("by the mouth of the LORD at the death (33:38) — the kiss (Bava Batra 17a:3); the chukat runner's row death_by_the_kiss by CALL", ['accepted'])
    if ask == 'moses_seventh_adar':
        move('Kiddushin 38a:5-7; Seder Olam Rabbah 10:2', "Moses died on the seventh of Adar — the tenth of Nisan (Joshua 4:19) less thirty-three days (thirty of mourning, three of preparation); born the same day ('this day', Deuteronomy 31:2): the years of the righteous completed to the day")
        move('cold_run_chukat (CALL) — CK.edom_and_hor(death_dates) = %s' % CK_DATES[0], "Aaron by the ink, Miriam and Moses by the shelf")
        ink('33:38-39', 'the Torah\'s one full death-date is Aaron\'s; Moses\' date the shelf\'s, computed BACKWARD from a run\'s marker')
        return out("Moses' seventh of Adar — computed backward from the tenth of Nisan (Kiddushin 38a:5-6); born and died the same day, a hundred and twenty exact (38a:7): Aaron's date the ink's, Moses' the shelf's", ['accepted'])
    if ask == 'arad':
        ink('33:40', '"and the Canaanite king of Arad heard" — %s / %s: 21:1\'s hearing WITHOUT the war, the captives, the vow and Hormah, WITH "in the land of Canaan"; placed right after the death' % (ARAD, HEARD))
        move('cold_run_chukat (CALL) — CK.edom_and_hor(arad_heard) = %s' % CK_ARAD[0], "what he heard: that Aaron died and the clouds departed (Rosh Hashanah 3a:1; Taanit 9a:10; Seder Olam Rabbah 9:2)")
        move('Rosh Hashanah 3a:3', "'he is Sihon, he is Arad, he is Canaan' — the hearer's identity disputed on the shelf")
        dat('the row arads_hearing: %s' % data['arads_hearing']['value'])
        return out("the Canaanite king of Arad heard (33:40) — 21:1's hearing alone, a run citation of the tape's line at (40, 5, 1); what he heard by CALL: that Aaron died and the clouds departed", ['accepted'])
    if ask == 'the_order':
        move('Rosh Hashanah 2b:13, 3a:2', "'after he had slain Sihon' (Deuteronomy 1:4) — Sihon alive at Aaron's death: Av before Shevat")
        ink('33:38-40', 'the tape\'s own order: the death at (40, 5, 1), Arad\'s hearing at (40, 5, 1), the departure from Hor at (40, 6, 1) — CK.D_AARON %d < CK.D_DEPART %d; Sihon smitten after; Moses\' oration past the Torah' % (CK.D_AARON, CK.D_DEPART))
        return out("the fortieth year's order — Aaron's death, Arad, the departure, Sihon: the tape's days in the shelf's order (Rosh Hashanah 2b:13)", ['accepted'])
    if ask == 'no_write':
        ink('33:38-40', 'the death and the hearing stand on the tape at 20:28 (garments_transferred_and_aaron_died, date %s, age %d) and 21:1 (arad_fought_and_took_captives): A RETELLING NEVER WRITES AN ACT TWICE — no line for 33:38-40, the checkpoints CZ5 and CZ6 read the tape' % (list(AARON_DATE), AGE))
        return out("no write for 33:38-40 — the death and the hearing are the tape's 20:28 and 21:1 lines, checkpointed, not rewritten", [FX.NONE])
    return out('no verdict in span', [FX.NONE])


# ===== F5: THE COMMAND (Num 33:50-56) — the divine voice; two debits open by design; the lot cited; the negative arm as data ====
def the_command(case, data):
    del P[:]
    ask = case['ask']
    if ask == 'the_frame':
        ink('33:50', '"and the LORD spoke to Moses in the plains of Moab by the Jordan at Jericho, saying" — %s (35:1 the frame\'s second seat; 26:3 Moses and Eleazar\'s); THE ONE DIVINE FRAME of the chapter (FRAME_VERBS %s)' % (SPOKE_PLAINS, FRAME_VERBS))
        dat('installed_by BOOT with the class named — a law in the divine voice spoken in the plains of Moab; the second pass (D2) decides')
        return out("and the LORD spoke to Moses in the plains of Moab (33:50) — the chapter's one divine frame after forty-nine verses without one; 35:1 the second seat", ['accepted'])
    if ask == 'when_you_pass':
        ink('33:51', '"when you pass over the Jordan into the land of Canaan" — %d seats of the clause (33:51, 35:10, Deuteronomy 11:31 among them); "into the land of Canaan" Leviticus 14:34\'s form' % len(PASS_OVER))
        return out("when you pass over the Jordan into the land of Canaan (33:51) — the law's trigger; 35:10 and Deuteronomy 11:31 the clause's kin", ['accepted'])
    if ask == 'drive_out':
        ink('33:52-53', '"you shall drive out all the inhabitants of the land from before you" (one seat) … "and you shall dispossess the land and dwell in it" %s — the same root at both; "the inhabitants of the land" %s in the Torah (Exodus 23:31\'s promise "I will drive them out" the command\'s kin)' % (DISPOSSESS_DWELL, INHAB_T))
        move('Sotah 34a:5', "Joshua in the Jordan: 'know for what purpose you cross — to drive out the inhabitants (33:52); if not, the water will drown me and you' — the debit's first run-reading")
        return out("drive out all the inhabitants of the land (33:52-53) — a DEBIT on Israel OPEN BY DESIGN: its runs Joshua's; the crossing's purpose at the Jordan (Sotah 34a:5)", ['commanded'])
    if ask == 'figured_stones':
        ink('33:52', '"destroy all their figured stones" — %s; Leviticus 26:1\'s word %s; the lemma\'s seats %s' % (FIGURED, FIG_LEV, FIG_LEMMA))
        move('Megillah 22b:11-13', "the baraita on Leviticus 26:1 — bowing on a stone floor forbidden outside the Temple (Ulla), with outstretched arms and legs (22b:13)")
        dat('the row the_three_objects[figured_stones]: THE CELL THAT COMPILES LEVITICUS 26:1 DOES NOT EXIST — journeys → tochacha OWED; the rows filed to the debt')
        return out("their figured stones (33:52) — Leviticus 26:1's word at its ban's seat, uncompiled: the edge owed, Megillah 22b:11-13's rows filed to the debt", ['commanded'])
    if ask == 'molten_images':
        ink('33:52', '"all their molten images you shall destroy" — %s (one seat); the calf\'s word at %s in the Torah (the lemma at %d seats)' % (MOLTEN_IMG, MOLTEN_T, len(MOLTEN_LEMMA_T)))
        move('cold_run_erection (CALL) — ER.covenant(molten_two_seats) = %s; ER.calf(molten_calf) = %d seats' % (ER_MOLTEN['v'], ER_CALF['v']), "the ban on MAKING (Exodus 34:17; Leviticus 19:4) and the calf; aaron's molten_image_barred block on the tape")
        move('cold_run_holiness (CALL) — HL.frame(molten_warnings) = %s' % HL_MOLTEN['v'], "Leviticus 19:4's two warnings, R. Yosei's third")
        return out("their molten images (33:52) — the calf's word; the ban on making at Exodus 34:17 and Leviticus 19:4 by CALL (the erection and holiness runners)", ['commanded'])
    if ask == 'high_places':
        ink('33:52', '"all their high places you shall demolish" — "their high places" %s (the consonants of "at their death", Leviticus 11:31-32, Numbers 6:7 — the morphology decides); the noun\'s Torah seats %s; "demolish" %s; Leviticus 26:30 "I will destroy your high places" %s / %s' % (HIGH, HIGH_LEMMA_T, DEMOLISH, YOUR_HIGH, I_DESTROY))
        move('Mishnah Zevachim 14:4-8', "the private altars' eras — Israel's own altars permitted and forbidden by era (the erection runner's high_places_banned block on the land): ANOTHER SENSE than the Canaanites' high places to demolish")
        return out("their high places (33:52) — Leviticus 26:30's curse in the same verb on the same object: the spec/curse pair; the private altar's eras (Mishnah Zevachim 14:4-8) another sense", ['commanded'])
    if ask == 'three_objects_own':
        move('cold_run_erection (CALL) — ER.covenant(demolition_grows) = %s' % ER_GROWS['v'], "the other iconoclasm commands' lists grow — Exodus 34:13 three, Deuteronomy 7:5 four, 12:3 five: altars, pillars, asherim, graven images")
        ink('33:52', 'the figured stone, the molten image, the high place — none of them in Exodus 23:24, 34:13, Deuteronomy 7:5, 12:2-3\'s lists: 33:52\'s three are the chapter\'s own')
        dat('the row the_three_objects: %s' % data['the_three_objects']['value'])
        return out("the three objects (33:52) are the chapter's own — the other iconoclasm lists (three, four, five by CALL) name altars, pillars, asherim and graven images", ['accepted'])
    if ask == 'possess_and_dwell':
        ink('33:53', '"and you shall dispossess the land and dwell in it, for to you I have given the land to possess it" — %s / %s (each one seat); "dwell in it" Deuteronomy 11:31\'s, "to possess it" Leviticus 20:24\'s' % (DISPOSSESS_DWELL, GIVEN))
        move('cold_run_second_census (CALL) — C2.the_land(possession_before_assignment) = %s' % C2_HELD[0], "the land held before assignment (Bava Batra 119a:1, 119a:5); ZL's row 'held' — the fifth expression's 'heritage' (Exodus 6:8, OPEN on Israel) read in the perfect here")
        return out("possess the land and dwell in it, for to you I have given it (33:53) — the promise's gift read in the perfect; held before assignment by CALL; no second entry", ['accepted'])
    if ask == 'the_lot_restated':
        ink('33:54', '33:54 RESTATES 26:52-56 — "by lot" %s, "to the many you shall give more" %s, "to whom the lot goes out" %s, "by the tribes of your fathers" %s; THE NUMBER SWITCHES: %s (26:54 %s singular; 33:54 %s plural, %s singular)' % (BY_LOT_T, MANY, LOT_OUT, TRIBES_FATHERS, MORPH_54, words(26, 54)[:2], words(33, 54)[5:7], words(33, 54)[9:11]))
        move('cold_run_second_census (CALL) — C2.the_land(by_lot) = %s; (by_number_of_names) = %s; C2.DATA[division_by] = %s' % (C2_LOT[0], C2_NAMES[0], C2.DATA['division_by']['value']), "the lot's cell — its effect commanded the debit OPEN since 26:52-56: CITED, NOT REWRITTEN (CZ7)")
        dat('the row the_lot_restated: %s' % data['the_lot_restated']['value'])
        return out("the lot restated to the people (33:54) — 26:52-56 word for word with the verb's number switching inside the verse; the open debit cited by CALL, not rewritten", ['accepted'])
    if ask == 'negative_arm':
        ink('33:55-56', '"thorns in your eyes and pricks in your sides" %s / %s — run back REVERSED at Joshua 23:13 %s, Judges 2:3 %s; "leave over" the Passover\'s verb %s; "harass" %s (25:18\'s word); "as I thought" %s (Isaiah 14:24)' % (THORNS, PRICKS, PRICKS_EYES, SIDES_JUDG, LEAVE_OVER, HARASS, THOUGHT))
        move('Megillah 11a:13-14', "Saul's Amalek left Haman as the thorn; Purim's punishment 'as I thought to do to them'")
        dat('the row negative_arm_outcome: %s — NO verdict on the tape' % data['negative_arm_outcome']['value'])
        return out("the negative arm (33:55-56) — thorns in your eyes and pricks in your sides, run back reversed by Joshua 23:13 and Judges 2:3; Saul's Amalek and Haman on the shelf (Megillah 11a); a data row, no verdict on the tape", ['accepted'])
    if ask == 'the_lot_arms':
        move('cold_run_second_census (CALL) — C2.the_land(land_divided_among) = %s; (lots_mouth) = %s' % (C2_AMONG[0], C2_MOUTH[0]), "left Egypt / entered / both (Bava Batra 117a:2-3, 117b:1); the lot and the Urim (122a:3-4)")
        ink('33:54', '"by the tribes of your fathers you shall inherit" — 26:55\'s "by the names of the tribes of their fathers" restated: the arms are the second census\'s rows')
        return out("the lot's arms — divided among those who left Egypt (the running setting), those who entered, or both; by lot and by the Urim: the second census's rows by CALL", ['accepted'])
    if ask == 'private_altar_eras':
        move('Mishnah Zevachim 14:4-8', "until the tabernacle stood private altars were permitted; forbidden; Gilgal permitted; Shiloh forbidden; Nob and Gibeon permitted; Jerusalem forbidden forever")
        ink('33:52', '"their high places" the Canaanites\' — the eras\' high places Israel\'s own private altars: NOT this chapter\'s; the gemara 112b-119b cut at the docket as the erection runner\'s')
        return out("the private altar's eras (Mishnah Zevachim 14:4-8) — Israel's own altars by era, the erection runner's block: not this chapter's high places", ['exempt'])
    return out('no verdict in span', [FX.NONE])


# ---- THE WRAP — the daemon, the scene, the narrative ------------------------------------------------------
def law_journeys(event, world):
    """Num 33:1-56 (cold_run_journeys.py F1-F5). given_at Num 33:50; installed_by boot — A LAW IN THE DIVINE VOICE SPOKEN IN THE PLAINS
    OF MOAB (the class named in the registry, the second pass decides). THREE TAPE LINES: the writing (33:1-2) — journeys_recorded on the
    people, its value THE LIST of forty-two; the departure retold with the judgments on the gods (33:3-4) — a STATUS on Egypt, the run of
    Exodus 12:12's first telling (the firstborn's plague OPEN: a burial is no removal); the command (33:50-56) — TWO DEBITS on Israel OPEN BY
    DESIGN (dispossess and possess; destroy the three objects), the lot's debit of 26:52-56 cited, not rewritten. No line for the stations
    (the list) or for 33:38-40 (the tape's 20:28 and 21:1). The exam's two case kinds dispatch to the cells with LITERAL effects per kind
    (2b's form — an unnamed effect is a KeyError)."""
    k, src = event['kind'], event['case_source']
    E_ = lambda eff, s, cp=None, amount=None, due=None, law='', value=None: {'effect': eff, 'subject': s, 'counterparty': cp, 'amount': amount, 'due': due, 'value': value if value is not None else True, 'source_law': law, 'case_source': src}
    day = event.get('day', world.clock.day)      # THE SEQUENTIAL RUN: the event's own day
    # ---- the three lines (page_order at the counter's day, no marker in the chapter) ----
    if k == 'journeys_written':
        return [E_('journeys_recorded', 'israel', value='%d places — %s' % (len(PLACES_EN), ', '.join(PLACES_EN)), law='F1 [INK 33:2 "and Moses wrote their goings out by their journeys by the mouth of the LORD" — THE FOUR WRITINGS (Exodus 24:4, Numbers 33:2, Deuteronomy 31:9, 31:22); the value THE LIST: forty-two places built from the DB (Rameses and forty-one camps; forty-two "journeyed" and forty-two "camped"), eighteen named nowhere else, eighteen with a first telling outside the chapter, seventeen with a witness on the tape — a retelling never writes a camp twice; the DATA row the_stations]')]
    if k == 'gods_judged_at_the_departure':
        return [E_('judgments_executed_on_their_gods', 'egypt_people', value='and on their gods the LORD executed judgments (33:4) — THE RUN OF EXODUS 12:12 ("on all the gods of Egypt I will execute judgments") recorded here alone, forty years on; Egypt burying every firstborn — the plague\'s aftermath, the entry OPEN', law='F2 [INK 33:3-4 — the date (1, 1, 15) = the exodus marker (a retelling\'s date a checkpoint); "on the morrow of the Passover" 33:3 and Joshua 5:11; "with a high hand" Exodus 14:8\'s; the perfect "executed judgments" ONE Bible seat, the future Exodus 12:12 and Ezekiel 25:11: Exodus narrates the firstborn and never the gods — the act\'s FIRST telling; a burial is not a removal (ten struck, four removed by CALL)]')]
    if k == 'dispossession_commanded':
        return [E_('commanded', 'israel', value='dispossess_the_inhabitants_and_possess_the_land', law='F5 [INK 33:52-53 "you shall drive out all the inhabitants of the land from before you … and you shall dispossess the land and dwell in it, for to you I have given the land to possess it" — OPEN BY DESIGN: its runs Joshua\'s (Sotah 34a:5 the crossing\'s purpose); the negative arm 33:55-56 run back reversed by Joshua 23:13 and Judges 2:3 (the DATA row negative_arm_outcome; Megillah 11a:13-14 Saul\'s Amalek and Haman); the class of Caleb\'s Hebron, the captives\' sentence and the crossing\'s debit]'),
                E_('commanded', 'israel', value='destroy_their_images', law='F5 [INK 33:52 "destroy all their figured stones, and all their molten images you shall destroy, and all their high places you shall demolish" — THE THREE OBJECTS the value\'s fields (the figured stone Leviticus 26:1\'s word, its ban UNCOMPILED — journeys → tochacha OWED; the molten image the calf\'s word, Exodus 34:17 and Leviticus 19:4 by CALL; the high places Leviticus 26:30\'s curse in the same verb — the Canaanites\', another sense than the private altar\'s eras); OPEN BY DESIGN: its runs Joshua\'s and Judges\', 2 Kings 23\'s the last; the lot of 33:54 CITES 26:52-56\'s open debit — no third write]')]
    # ---- the exam's case kinds: each names LITERALLY every effect it can write (2b's form) ----
    if k == 'journeys_case':
        fn = {'writing': the_heading_and_the_writing, 'departure': the_departure, 'stations': the_stations}.get(event.get('cell'), aarons_death_retold)
        v, e, _ = fn(dict(event, ask=event['ask']), DATA); L = '%s [%s]' % ({'writing': 'F1', 'departure': 'F2', 'stations': 'F3'}.get(event.get('cell'), 'F4'), v); s_ = event['person']
        W = {'journeys_recorded': E_('journeys_recorded', s_, value=v, law=L), 'accepted': E_('accepted', s_, value=v, law=L), 'exempt': E_('exempt', s_, value=v, law=L)}
        return [W[x] for x in e if x != FX.NONE]
    if k == 'dispossession_case':
        v, e, _ = the_command(dict(event, ask=event['ask']), DATA); L = 'F5 [%s]' % v; s_ = event['person']
        W = {'commanded': E_('commanded', s_, value=v, law=L), 'accepted': E_('accepted', s_, value=v, law=L), 'exempt': E_('exempt', s_, value=v, law=L)}
        return [W[x] for x in e if x != FX.NONE]
    return []


LINES = [
    ('Num 33:1-2 — these are the journeys of the children of Israel who went out of the land of Egypt by their hosts by the hand of Moses and Aaron; and Moses wrote their goings out by their journeys by the mouth of the LORD, and these are their journeys by their goings out', 'moses'),
    ('Num 33:3-4 — and they journeyed from Rameses in the first month, on the fifteenth day of the first month; on the morrow of the Passover the children of Israel went out with a high hand in the sight of all Egypt; and Egypt was burying those whom the LORD had struck among them, every firstborn; and on their gods the LORD executed judgments', 'egypt_people'),
    ('Num 33:50-56 — and the LORD spoke to Moses in the plains of Moab by the Jordan at Jericho, saying: speak to the children of Israel and say to them: when you pass over the Jordan into the land of Canaan, you shall drive out all the inhabitants of the land from before you, and destroy all their figured stones, and all their molten images you shall destroy, and all their high places you shall demolish; and you shall dispossess the land and dwell in it, for to you I have given the land to possess it; and you shall inherit the land by lot by your families — to the many you shall give more inheritance and to the few less; to whom the lot goes out, his it shall be; by the tribes of your fathers you shall inherit; but if you do not drive out the inhabitants of the land from before you, then those you leave of them shall be thorns in your eyes and pricks in your sides, and they shall harass you on the land in which you dwell; and it shall be that as I thought to do to them, I will do to you', 'israel'),
]
CLOSES = 'none — the gods\' judgment had no entry to close; the firstborn\'s plague stays open (a burial is no removal); the lot\'s debit (26:52-56) stays open, cited by 33:54'


def scene():
    """THE SCENE — the exam's rows replayed on the world engine (the exodus epoch): the exam's persons through the two case kinds."""
    with contextlib.redirect_stdout(io.StringIO()):
        w = WE.World(era='Num 33:1-56: the journeys on the shelf — Rosh Hashanah, Kiddushin, Megillah, Bava Batra, Seder Olam on the engine (the exodus epoch)', epoch='exodus')
        w.laws = [law_journeys]
        w.advance(w.clock.day_in('exodus', 40, 6, 1))
        # ---- the exam's persons through the two case kinds (LITERAL submits — the daemon gate parses no loop) ----
        w.submit({'kind': 'journeys_case', 'subject': 'the-era-new-year', 'person': 'the-era-new-year', 'cell': 'death', 'ask': 'the_era_new_year', 'case_source': 'Rosh Hashanah 2b:9 — the exam\'s row the_era_new_year'})
        w.submit({'kind': 'journeys_case', 'subject': 'the-morrow', 'person': 'the-morrow', 'cell': 'departure', 'ask': 'the_morrow', 'case_source': 'Kiddushin 37b:14 — the exam\'s row the_morrow'})
        w.submit({'kind': 'journeys_case', 'subject': 'the-manna', 'person': 'the-manna', 'cell': 'departure', 'ask': 'the_manna', 'case_source': 'Kiddushin 38a:3-4 — the exam\'s row the_manna'})
        w.submit({'kind': 'journeys_case', 'subject': 'the-seventh-of-adar', 'person': 'the-seventh-of-adar', 'cell': 'death', 'ask': 'moses_seventh_adar', 'case_source': 'Kiddushin 38a:5 — the exam\'s row moses_seventh_adar'})
        w.submit({'kind': 'journeys_case', 'subject': 'the-kiss', 'person': 'the-kiss', 'cell': 'death', 'ask': 'by_the_mouth_kiss', 'case_source': 'Bava Batra 17a:3 — the exam\'s row by_the_mouth_kiss'})
        w.submit({'kind': 'journeys_case', 'subject': 'the-retreat', 'person': 'the-retreat', 'cell': 'stations', 'ask': 'moseroth_seven', 'case_source': 'Seder Olam Rabbah 9:2 — the exam\'s row moseroth_seven'})
        w.submit({'kind': 'journeys_case', 'subject': 'the-camps-extent', 'person': 'the-camps-extent', 'cell': 'stations', 'ask': 'the_last_camp', 'case_source': 'Eruvin 55b:15 — the exam\'s row the_last_camp'})
        w.submit({'kind': 'journeys_case', 'subject': 'the-directional-ending', 'person': 'the-directional-ending', 'cell': 'stations', 'ask': 'directional_ending', 'case_source': 'Yevamot 13b:6 — the exam\'s row directional_ending'})
        w.submit({'kind': 'journeys_case', 'subject': 'the-left-by-day', 'person': 'the-left-by-day', 'cell': 'departure', 'ask': 'left_by_day', 'case_source': 'Berakhot 9a:25 — the exam\'s row left_by_day'})
        w.submit({'kind': 'journeys_case', 'subject': 'the-arad-identity', 'person': 'the-arad-identity', 'cell': 'death', 'ask': 'arad', 'case_source': 'Rosh Hashanah 3a:3 — the exam\'s row arad'})
        w.submit({'kind': 'dispossession_case', 'subject': 'the-crossings-purpose', 'person': 'the-crossings-purpose', 'ask': 'drive_out', 'case_source': 'Sotah 34a:5 — the exam\'s row drive_out'})
        w.submit({'kind': 'dispossession_case', 'subject': 'the-thorns', 'person': 'the-thorns', 'ask': 'negative_arm', 'case_source': 'Megillah 11a:13 — the exam\'s row negative_arm'})
        w.submit({'kind': 'dispossession_case', 'subject': 'the-figured-stone', 'person': 'the-figured-stone', 'ask': 'figured_stones', 'case_source': 'Megillah 22b:11 — the exam\'s row figured_stones'})
        w.submit({'kind': 'dispossession_case', 'subject': 'the-private-altar', 'person': 'the-private-altar', 'ask': 'private_altar_eras', 'case_source': 'Mishnah Zevachim 14:4 — the exam\'s row private_altar_eras'})
        w.submit({'kind': 'dispossession_case', 'subject': 'the-lot-arms', 'person': 'the-lot-arms', 'ask': 'the_lot_arms', 'case_source': 'Bava Batra 117a:2 — the exam\'s row the_lot_arms'})
        w.submit({'kind': 'dispossession_case', 'subject': 'the-held-before', 'person': 'the-held-before', 'ask': 'possess_and_dwell', 'case_source': 'Bava Batra 119a:1 — the exam\'s row possess_and_dwell'})
        w.submit({'kind': 'dispossession_case', 'subject': 'the-lot-and-urim', 'person': 'the-lot-and-urim', 'ask': 'the_lot_restated', 'case_source': 'Bava Batra 122a:3 — the exam\'s row the_lot_restated'})
    n = lambda eid, eff: len([e for e in w.entity(eid).ledger if e['effect'] == eff])
    tset = len([l for l in w.log if l[0] == 'TIMER-SET']); tfire = len([l for l in w.log if l[0] == 'TIMER-FIRE']); tcan = len([l for l in w.log if l[0] == 'TIMER-CANCEL'])
    return ((n('the-era-new-year', 'accepted'), n('the-morrow', 'accepted'), n('the-manna', 'accepted'), n('the-seventh-of-adar', 'accepted'), n('the-kiss', 'accepted'), n('the-retreat', 'accepted'), n('the-camps-extent', 'accepted'), n('the-directional-ending', 'accepted'), n('the-left-by-day', 'accepted'), n('the-arad-identity', 'accepted'),
             n('the-crossings-purpose', 'commanded'), n('the-thorns', 'accepted'), n('the-figured-stone', 'commanded'), n('the-private-altar', 'exempt'), n('the-lot-arms', 'accepted'), n('the-held-before', 'accepted'), n('the-lot-and-urim', 'accepted')),
            (tset, tfire, tcan, len(w.timers)),
            len(w.entities)), w
SCENE, _W = scene()
# THE PREDICTION (typed before the first run, NUMBERS_WALK.md "Sitting 13b"): every exam person written once — seventeen ones; no timer in the
# chapter (set 0, fired 0, cancelled 0, pending 0). ENTITIES: the exam's 17 persons alone (an entity is a written-on party; no counterparty written on).
SCENE_PREDICTED = ((1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1), (0, 0, 0, 0), 17)
assert SCENE == SCENE_PREDICTED, ('THE NUMBERS WALK: the scene moved from its prediction', SCENE, SCENE_PREDICTED)


def narrative():
    """THE NUMBERS WALK 13b (2026-09-12): the chapter's own acts AS HISTORY — the THREE lines of 33:1-56 at the counter's day (40, 6, 1),
    page-order after Gad and Reuben's twelve (32:1-42), on a world with this runner's daemon: 4 writes, no timer, no marker, two entities
    (israel and egypt_people — moses a subject with no write), no close. Recorded by the sequential run's recorder and stitched onto the tape.
    Not a graded cell: the tuple below is a tripwire typed from the design; the sequence world's RUN tuple and CZ1-CZ9 grade the tape."""
    with contextlib.redirect_stdout(io.StringIO()):
        w = WE.World(era='Num 33:1-56: the journeys on the tape — the writing, the departure with the judgments on the gods, the command (the exodus epoch)', epoch='exodus')
        w.laws = [law_journeys]
        w.advance(w.clock.day_in('exodus', 40, 6, 1))
        # THE DAEMON GATE READS LITERAL SUBMITS ONLY — the three lines typed out
        w.submit({'kind': 'journeys_written', 'subject': 'moses', 'count': 42, 'by_the_mouth_of_the_lord': True, 'first': 'Rameses', 'case_source': LINES[0][0]})
        w.submit({'kind': 'gods_judged_at_the_departure', 'subject': 'egypt_people', 'date': [1, 1, 15], 'morrow_of_the_passover': True, 'high_hand': True, 'burying': 'the_firstborn', 'case_source': LINES[1][0]})
        w.submit({'kind': 'dispossession_commanded', 'subject': 'israel', 'objects': ['figured_stones', 'molten_images', 'high_places'], 'lot': True, 'negative_arm': True, 'frame': 'and the LORD spoke to Moses in the plains of Moab', 'case_source': LINES[2][0]})
    writes = len([l for l in w.log if l[0] == 'WRITE'])
    closes = len([e for ent in w.entities.values() for e in ent.ledger if e.get('closed_by')])
    return (writes, len([l for l in w.log if l[0] == 'TIMER-SET']), len(w.entities), w.clock.eras['exodus'].date(w.clock.day)[1:], closes), w


NARRATIVE, _WN = narrative()
NARRATIVE_PREDICTED = (4, 0, 2, (6, 1), 0)   # NUMBERS_WALK.md "Sitting 13b": 4 writes (L1 1, L2 1, L3 2), no timer, TWO entities (israel, egypt_people — the written-on parties; moses a subject with no write), the counter's day (6, 1), no close
assert NARRATIVE == NARRATIVE_PREDICTED, ('THE NUMBERS WALK: the journeys\' narrative moved from its prediction', NARRATIVE, NARRATIVE_PREDICTED)


# =====================================================================
# Motion 2 — THE TEST DATA: the answer sheet's rows (the docket's LAW rows).
# =====================================================================
CASES = [
    # F1 — the heading and the writing
    ('Num 33:1 / 10:28 — the heading', lambda: the_heading_and_the_writing({'ask': 'heading'}, DATA), "these are the journeys of the children of Israel (33:1) — 10:28's four words; sixty-three headings in the Torah"),
    ('Num 33:1 — by their hosts', lambda: the_heading_and_the_writing({'ask': 'by_their_hosts'}, DATA), "by their hosts (33:1) — sixteen seats, all in Numbers"),
    ('Num 33:1 / Ps 77:21 — by the hand of Moses and Aaron', lambda: the_heading_and_the_writing({'ask': 'by_the_hand'}, DATA), "by the hand of Moses and Aaron (33:1) — Psalm 77:21 the phrase's other seat, observed"),
    ('Num 33:2 — the four writings', lambda: the_heading_and_the_writing({'ask': 'moses_wrote'}, DATA), "and Moses wrote (33:2) — the four writings: Exodus 24:4, Numbers 33:2, Deuteronomy 31:9, 31:22"),
    ('Num 33:2, 38 / Bava Batra 17a:3 — by the mouth of the LORD', lambda: the_heading_and_the_writing({'ask': 'by_the_mouth'}, DATA), "by the mouth of the LORD — twenty-one Bible seats; Moses wrote by it (33:2), Aaron went up by it (33:38), and died by it on the shelf (Bava Batra 17a:3)"),
    ('Num 33:2 — the chiasm', lambda: the_heading_and_the_writing({'ask': 'the_chiasm'}, DATA), "their goings out by their journeys, their journeys by their goings out (33:2) — the chiasm; 'their goings out' two Bible seats, 'by their journeys' four"),
    ('Num 33:2, 5-49 — the list as the writing\'s value', lambda: the_heading_and_the_writing({'ask': 'the_list'}, DATA), "the journeys recorded — forty-two places as the writing's value: Rameses and forty-one camps, eighteen named nowhere else, eighteen with a first telling, seventeen with a witness on the tape"),
    # F2 — the departure
    ('Num 33:3 / Exod 12:41 — the date is the marker', lambda: the_departure({'ask': 'the_date'}, DATA), "the fifteenth day of the first month (33:3) = (1, 1, 15) — the tape's exodus marker; a retelling's date is a checkpoint, never a second marker"),
    ('Num 33:3 / Josh 5:11; Kiddushin 37b:14-38a:2 — the morrow of the Passover', lambda: the_departure({'ask': 'the_morrow'}, DATA), "on the morrow of the Passover — 33:3 and Joshua 5:11 the phrase's two seats: the run's two ends on one date-word; the omer's arm and the manna's"),
    ('Berakhot 9a:25 — left by day', lambda: the_departure({'ask': 'left_by_day'}, DATA), "left by day (33:3) — redeemed at evening, went out by day (Berakhot 9a:25); the exodus story's by_day by CALL"),
    ('Num 33:3 / Exod 14:8; 15:30 by CALL — with a high hand', lambda: the_departure({'ask': 'high_hand'}, DATA), "with a high hand (33:3) — Exodus 14:8's posture at the same going out, 15:30's the high-hand sinner's; the shelach runner names 33:3"),
    ('Num 33:4 / Exod 12:29 by CALL — the burial', lambda: the_departure({'ask': 'the_burial'}, DATA), "Egypt was burying every firstborn (33:4) — the plague's aftermath: the firstborn's plague_struck entry stays open, a burial is no removal (ten struck, four removed)"),
    ('Num 33:4 / Exod 12:12 — the run of the judgments', lambda: the_departure({'ask': 'the_gods_judged'}, DATA), "on their gods the LORD executed judgments (33:4) — the run of Exodus 12:12 recorded here alone: a status on Egypt written forty years on, the act's first telling"),
    ('Kiddushin 38a:3-4 / Exod 16:13 by CALL — the manna', lambda: the_departure({'ask': 'the_manna'}, DATA), "the manna forty years less thirty days (Kiddushin 38a:3-4) — from (1, 2, 16), the tape's marker at Exodus 16:13, to the sixteenth of Nisan; the cakes of 33:3's fifteenth thirty days"),
    # F3 — the stations
    ('Num 33:3-49 — forty-two places', lambda: the_stations({'ask': 'forty_two'}, DATA), "forty-two places (33:3-49) — Rameses and forty-one camps: the first departure and the last camp each told twice"),
    ('Num 33:3-49 — the verbs', lambda: the_stations({'ask': 'the_verbs'}, DATA), "forty-two 'journeyed' and forty-two 'camped' — forty-one verses with both; 33:3 the journey alone, 33:49 the camp alone"),
    ('Exod 12:37-19:2 by CALL — the nine', lambda: the_stations({'ask': 'exodus_nine'}, DATA), "the exodus story's nine stations by CALL — Succoth to Sinai on the tape as statuses and markers; the itinerary's list their run citation"),
    ('Num 33:8 / Exod 15:22; 34:33 — Etham for Shur', lambda: the_stations({'ask': 'etham_for_shur'}, DATA), "the wilderness of Etham (33:8) for Exodus 15:22's Shur — each one seat; 'a way of three days' six Torah seats; Exodus 34:33's 'speaking with them' a homograph"),
    ('Num 33:6 / Exod 13:20 — one word added', lambda: the_stations({'ask': 'one_word_added'}, DATA), "33:6 is Exodus 13:20 with one word added — the itinerary retelling its first telling on the tokens"),
    ('Num 33:9 / Exod 15:27 — Elim', lambda: the_stations({'ask': 'elim'}, DATA), "Elim's twelve springs and seventy palms (33:9) word for word with Exodus 15:27 — [12, 70] at both"),
    ('Num 33:10-13 — unnamed in Exodus', lambda: the_stations({'ask': 'unnamed_in_exodus'}, DATA), "the Red Sea camp, Dophkah and Alush (33:10-13) — three stations Exodus never names"),
    ('Num 33:16-17 / 11:34-35 by CALL — Kibroth-hattaavah and Hazeroth', lambda: the_stations({'ask': 'kibroth_hazeroth'}, DATA), "Kibroth-hattaavah and Hazeroth (33:16-17) — chapter 11's graves and Hazeroth by CALL: the burial on the tape, the markers at (2, 3, 22) and (2, 3, 29)"),
    ('Num 33:18 / 12:16; 13:3, 26 — Rithmah', lambda: the_stations({'ask': 'rithmah_paran'}, DATA), "Rithmah (33:18) — Paran under another name: the spies' base of 12:16, 13:3, 13:26; the tape's marker at (2, 3, 29)"),
    ('Num 33:10-46 — the eighteen only here', lambda: the_stations({'ask': 'only_here'}, DATA), "eighteen stations named nowhere else — seventeen by lemma (Dophkah to Almon-diblathaim) and the Red Sea camp"),
    ('Num 33:20, 26, 27 — the common-word names', lambda: the_stations({'ask': 'common_word_names'}, DATA), "Libnah, Tahath, Terah (33:20, 26, 27) — three names whose lemma's other seats are another referent"),
    ('Num 33:30-38 / Deut 10:6-7; Seder Olam 9:2 by CALL — Moseroth seven before Hor', lambda: the_stations({'ask': 'moseroth_seven'}, DATA), "Moseroth seven camps before Mount Hor (33:30-37) — Deuteronomy 10:6's 'there Aaron died' at Moserah reconciled by the retreat of seven stations (Seder Olam Rabbah 9:2; the chukat runner's row)"),
    ('Num 33:36-37 / Gen 14:7 — Kadesh and Mount Hor', lambda: the_stations({'ask': 'kadesh_hor'}, DATA), "Kadesh and Mount Hor (33:36-37) — 'that is Kadesh' with Genesis 14:7 (three of the pair's five seats read 'it is holy': a homograph); the edge of Edom one seat; two Mount Hors by CALL"),
    ('Num 33:41-47 / 21:4-20; 32:34 by CALL — the last stations', lambda: the_stations({'ask': 'chapter_21'}, DATA), "the last stations against chapter 21 — Zalmonah and Punon only here; Oboth and Iye-abarim shared; 21:18-20's stations absent; Dibon Gad the Gad runner's own witness by CALL; the mountains of Abarim before Nebo"),
    ('Num 33:48-49 / Eruvin 55b:15; Yoma 75b:14 — the last camp', lambda: the_stations({'ask': 'the_last_camp'}, DATA), "the plains of Moab (33:48-49) — the last camp by CALL; from Beth-jeshimoth to Abel-shittim three parasangs on the shelf (Eruvin 55b:15; Yoma 75b:14)"),
    ('Num 33:46-47 / Yevamot 13b:6 — the directional ending', lambda: the_stations({'ask': 'directional_ending'}, DATA), "Diblathaimah (33:46-47) — the directional ending on the station's name (Yevamot 13b:6's example)"),
    ('the tape\'s camps against the list', lambda: the_stations({'ask': 'tape_matched'}, DATA), "the tape's camps against the list — twelve names matched (Succoth to the plains of Moab), five statuses not (Goshen, Shur, the Red Sea way, Mattanah to Pisgah, Shittim)"),
    # F4 — Aaron's death retold
    ('Num 33:38 / 20:28 by CALL — the date', lambda: aarons_death_retold({'ask': 'the_date'}, DATA), "Aaron died on (40, 5, 1) (33:38) — the tape's marker at 20:28, built from this verse; the ordinal reader's year and month"),
    ('Num 33:39 / Exod 7:7; Deut 34:7 — the age', lambda: aarons_death_retold({'ask': 'the_age'}, DATA), "Aaron 123 at his death (33:39) = Exodus 7:7's 83 + 40; Moses 120 = 80 + 40 — the brothers three years apart at both ends, the ink's checksum"),
    ('Num 33:38 / Exod 19:1; 1 Kgs 6:1; Rosh Hashanah 2b:7 — the era\'s stamps', lambda: aarons_death_retold({'ask': 'the_eras_stamps'}, DATA), "the era's three stamps — Exodus 19:1, Numbers 33:38, 1 Kings 6:1 (the 480th year): the shelf's own chain of proof (Rosh Hashanah 2b:7, 3a:11)"),
    ('Rosh Hashanah 2b:9, 3a:5 — the era\'s new year', lambda: aarons_death_retold({'ask': 'the_era_new_year'}, DATA), "the era's new year from the chapter's date — (40, 5, 1) and (40, 11, 1) in one year, (2, 1, 1) and (2, 2, 20) in one year on the Calendar: not Tishrei, not Iyar (Rosh Hashanah 2b:9, 3a:5)"),
    ('Rosh Hashanah 2b:11 / Deut 1:3 — the verbal analogy', lambda: aarons_death_retold({'ask': 'verbal_analogy'}, DATA), "the fortieth year / the fortieth year — Deuteronomy 1:3's bare date counted from the exodus by the verbal analogy with 33:38 (Rosh Hashanah 2b:11, taught); the two date readers meet"),
    ('Bava Batra 17a:3 by CALL — the kiss', lambda: aarons_death_retold({'ask': 'by_the_mouth_kiss'}, DATA), "by the mouth of the LORD at the death (33:38) — the kiss (Bava Batra 17a:3); the chukat runner's row death_by_the_kiss by CALL"),
    ('Kiddushin 38a:5-7; Seder Olam 10:2 by CALL — Moses\' seventh of Adar', lambda: aarons_death_retold({'ask': 'moses_seventh_adar'}, DATA), "Moses' seventh of Adar — computed backward from the tenth of Nisan (Kiddushin 38a:5-6); born and died the same day, a hundred and twenty exact (38a:7): Aaron's date the ink's, Moses' the shelf's"),
    ('Num 33:40 / 21:1 by CALL; Rosh Hashanah 3a:1-3 — Arad', lambda: aarons_death_retold({'ask': 'arad'}, DATA), "the Canaanite king of Arad heard (33:40) — 21:1's hearing alone, a run citation of the tape's line at (40, 5, 1); what he heard by CALL: that Aaron died and the clouds departed"),
    ('Rosh Hashanah 2b:13 — the order', lambda: aarons_death_retold({'ask': 'the_order'}, DATA), "the fortieth year's order — Aaron's death, Arad, the departure, Sihon: the tape's days in the shelf's order (Rosh Hashanah 2b:13)"),
    ('Num 33:38-40 — no write', lambda: aarons_death_retold({'ask': 'no_write'}, DATA), "no write for 33:38-40 — the death and the hearing are the tape's 20:28 and 21:1 lines, checkpointed, not rewritten"),
    # F5 — the command
    ('Num 33:50 / 35:1 — the frame', lambda: the_command({'ask': 'the_frame'}, DATA), "and the LORD spoke to Moses in the plains of Moab (33:50) — the chapter's one divine frame after forty-nine verses without one; 35:1 the second seat"),
    ('Num 33:51 / 35:10; Deut 11:31 — when you pass over', lambda: the_command({'ask': 'when_you_pass'}, DATA), "when you pass over the Jordan into the land of Canaan (33:51) — the law's trigger; 35:10 and Deuteronomy 11:31 the clause's kin"),
    ('Num 33:52-53 / Sotah 34a:5 — drive out', lambda: the_command({'ask': 'drive_out'}, DATA), "drive out all the inhabitants of the land (33:52-53) — a DEBIT on Israel OPEN BY DESIGN: its runs Joshua's; the crossing's purpose at the Jordan (Sotah 34a:5)"),
    ('Num 33:52 / Lev 26:1; Megillah 22b:11-13 — the figured stones', lambda: the_command({'ask': 'figured_stones'}, DATA), "their figured stones (33:52) — Leviticus 26:1's word at its ban's seat, uncompiled: the edge owed, Megillah 22b:11-13's rows filed to the debt"),
    ('Num 33:52 / Exod 34:17; Lev 19:4 by CALL — the molten images', lambda: the_command({'ask': 'molten_images'}, DATA), "their molten images (33:52) — the calf's word; the ban on making at Exodus 34:17 and Leviticus 19:4 by CALL (the erection and holiness runners)"),
    ('Num 33:52 / Lev 26:30; Mishnah Zevachim 14:4-8 — the high places', lambda: the_command({'ask': 'high_places'}, DATA), "their high places (33:52) — Leviticus 26:30's curse in the same verb on the same object: the spec/curse pair; the private altar's eras (Mishnah Zevachim 14:4-8) another sense"),
    ('Exod 34:13; Deut 7:5, 12:3 by CALL — the three objects the chapter\'s own', lambda: the_command({'ask': 'three_objects_own'}, DATA), "the three objects (33:52) are the chapter's own — the other iconoclasm lists (three, four, five by CALL) name altars, pillars, asherim and graven images"),
    ('Num 33:53 / Bava Batra 119a:1 by CALL — possess and dwell', lambda: the_command({'ask': 'possess_and_dwell'}, DATA), "possess the land and dwell in it, for to you I have given it (33:53) — the promise's gift read in the perfect; held before assignment by CALL; no second entry"),
    ('Num 33:54 / 26:52-56 by CALL — the lot restated', lambda: the_command({'ask': 'the_lot_restated'}, DATA), "the lot restated to the people (33:54) — 26:52-56 word for word with the verb's number switching inside the verse; the open debit cited by CALL, not rewritten"),
    ('Num 33:55-56 / Josh 23:13; Judg 2:3; Megillah 11a — the negative arm', lambda: the_command({'ask': 'negative_arm'}, DATA), "the negative arm (33:55-56) — thorns in your eyes and pricks in your sides, run back reversed by Joshua 23:13 and Judges 2:3; Saul's Amalek and Haman on the shelf (Megillah 11a); a data row, no verdict on the tape"),
    ('Bava Batra 117a-122a by CALL — the lot\'s arms', lambda: the_command({'ask': 'the_lot_arms'}, DATA), "the lot's arms — divided among those who left Egypt (the running setting), those who entered, or both; by lot and by the Urim: the second census's rows by CALL"),
    ('Mishnah Zevachim 14:4-8 — the private altar\'s eras', lambda: the_command({'ask': 'private_altar_eras'}, DATA), "the private altar's eras (Mishnah Zevachim 14:4-8) — Israel's own altars by era, the erection runner's block: not this chapter's high places"),
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
    print('THE INK: integers %s; ordinals %s; starred none; marked none; the frame verbs %s (the one divine frame)' % (sorted(INTS.items()), sorted(ORDS.items()), FRAME_VERBS))
    print('THE STATIONS: %d places; %d journeyed, %d camped; only here %d (%s + the Red Sea); Moseroth %d camps before Mount Hor; the tape\'s camps matched %d, unmatched %d' % (len(STATIONS), len(JOURNEYED), len(CAMPED), sum(1 for s in STATIONS if s['only_here']), len(ONLY_HERE), PLACES_EN.index('Mount Hor') - PLACES_EN.index('Moseroth'), len(TAPE_CAMPS_MATCHED), len(TAPE_CAMPS_UNMATCHED)))
    print('THE DATES: the departure %s = the exodus marker; the death %s = the marker at 20:28; Aaron %d = %d + %d; Moses %d = %d + %d; the era\'s year at Av and Shevat %s / %s' % (DEPARTURE_DATE, AARON_DATE, AGE, AARON_83, YEAR, MOSES_120, MOSES_80, YEAR, ERA_AV, ERA_SHEVAT))
    print('THE SCENE on the bench: %s; the timers (set, fired, cancelled, pending) %s; entities %d' % SCENE)
    print('THE NARRATIVE: %s' % (NARRATIVE,))
    print('THE PARAMETER ROWS: ' + '; '.join('%s = %s' % (k, (DATA[k]['value'] if k != 'the_stations' else '%d places (a data list)' % len(DATA[k]['value']))) for k in DATA) + ' (the other settings recorded in DATA)')
    if ok == len(CASES):
        print('\nTHE COMPILE OF THE JOURNEYS: the answer sheet REPRODUCED — %d/%d' % (ok, len(CASES)))
    sys.exit(0 if ok == len(CASES) else 1)

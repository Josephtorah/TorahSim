import os as _os
_ROOT = _os.path.normpath(_os.path.join(_os.path.dirname(_os.path.abspath(__file__)), '..', '..', '..'))   # THE PORTABLE REPO (2026-09-15): the repo root from this file's own place
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

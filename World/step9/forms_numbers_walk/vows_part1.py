import os as _os
_ROOT = _os.path.normpath(_os.path.join(_os.path.dirname(_os.path.abspath(__file__)), '..', '..', '..'))   # THE PORTABLE REPO (2026-09-15): the repo root from this file's own place
#!/usr/bin/env python3
# NUM 30:1-17 — THE VOWS (THE NUMBERS WALK sitting 10b, 2026-09-12; World/step9/NUMBERS_WALK.md "Sitting 10b"; the state doc's "30b").
# A LAW IN MOSES' VOICE: no divine frame — "and Moses spoke to the heads of the tribes ... this is the thing which the LORD commanded" (30:2);
# two "when" cases (a man, 30:3; a woman in her youth in her father's house, 30:4) and seven "and if" branches; THE VOW AS A LEDGER ENTRY
# with its STATE MACHINE — vow_uttered writes the DEBIT vow_bound toward HEAVEN; vow_heard (the authority silent) sets the TIMER vow_confirmed
# due the hearing day + 1 (the calendar row vow_annulment_window: to nightfall; the pair's twenty-four hours recorded); vow_restrained on the
# day by the RIGHT authority cancels the timer, closes the debit and writes vow_annulled (HEAVEN forgives her); after the fire the vow stands
# and the annulling husband bears her iniquity (iniquity_borne); the wrong authority writes nothing. The callees by CALL: the nazirite's
# vow-identity and the suspected wife's "bear her iniquity" (naso), the utterance oath of Leviticus 5:4 (vayikra5), the priest's daughter's
# "a widow or a divorced woman ... as in her youth" (priesthood), the delay ban's vow_deadline row (musafim), the affliction-root at Leviticus
# 23:27 (moadim). Seven cells; every token probed (zero-report law); effects on every cell (the effects law); the parameters the ink leaves
# open recorded in DATA with their arms. Reading ledger: logic/oral_triage/num_30_vows_2026-09-12.md; the exam's docket:
# logic/oral_triage/num_30_vows_exam_2026-09-12.md (1,047 rows).

# ---- THE HONEST-PAIRING GUARD ----------------------------------------------------------------------------
import os as _os, sys as _sys
_sys.path.insert(0, _os.path.dirname(_os.path.abspath(__file__)))
from compile_guards import check_honest_pairing as _chp
_P = _os.path.abspath(__file__)
GUARDED = _chp(_P, 'CASES', 2)
assert GUARDED == 130, ('the guard counted %d expectations, the tripwire holds 130' % GUARDED)   # the design's estimate — retyped from the guard's print after the first run
print('guard: %d expectations checked, every one a literal from the answer sheet [honest-pairing guard satisfied]' % GUARDED)
import sqlite3, sys, io, re, contextlib, collections, yaml
import effects_layer as FX
import world_engine as WE
import cold_run_naso as NS                       # THE EDGE: vows -> naso CALL, reference (6:2's vow-identity for the age — Sifrei 153:3; 5:31's "bear her iniquity" — Sifrei 156:2)
import cold_run_vayikra5 as V5                   # THE EDGE: vows -> vayikra5 CALL, reference (30:7's "utterance" = Lev 5:4's oath — Sifrei 153:7)
import cold_run_priesthood as PR                 # THE EDGE: vows -> priesthood CALL, reference (30:10's "a widow or a divorced woman", 30:4's "in her youth" — Lev 22:13's pair of words)
import cold_run_musafim as MU                    # THE EDGE: vows -> musafim CALL, reference (29:39 "besides your vows" — the vow_deadline row READ)
import cold_run_moadim as MO                     # THE EDGE: vows -> moadim CALL, reference (30:14's affliction-root at Lev 23:27)

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
    ('ויאמר',   30, 1,  'and Moses SAID — the receipt that closes a speech (the first word)'),
    ('ככל',     30, 1,  'according to ALL that — the receipt formula\'s second form (the register gate\'s new seat)'),
    ('וידבר',   30, 2,  'and Moses SPOKE — the chapter\'s second and last narrative verb'),
    ('ראשי',    30, 2,  'the heads of [the tribes] — the addressees'),
    ('המטות',   30, 2,  'the tribes'),
    ('הדבר',    30, 2,  'the thing — "this is the thing" (the limiter of Sifrei 153:2)'),
    ('איש',     30, 3,  'a man — the minor excluded'),
    ('כי',      30, 3,  'when — the case head (the first word after "a man")'),
    ('ידר',     30, 3,  'vows'),
    ('נדר',     30, 3,  'a vow'),
    ('השבע',    30, 3,  'swear — the doubled verb\'s first'),
    ('שבעה',    30, 3,  'an oath — the seven-stem\'s homograph, STARRED by the parser'),
    ('לאסר',    30, 3,  'to bind'),
    ('אסר',     30, 3,  'a bond'),
    ('נפשו',    30, 3,  'his soul — the chapter\'s one masculine soul-token'),
    ('יחל',     30, 3,  'profane — "he shall not profane his word"'),
    ('דברו',    30, 3,  'his word'),
    ('היצא',    30, 3,  'that proceeds — "according to all that proceeds out of his mouth"'),
    ('מפיו',    30, 3,  'out of his mouth'),
    ('ואשה',    30, 4,  'and a woman — likened to the man'),
    ('בבית',    30, 4,  'in the house of [her father] — his domain'),
    ('בנעריה',  30, 4,  'in her youth — the first of two seats'),
    ('ושמע',    30, 5,  'and [her father] hears — the trigger'),
    ('והחריש',  30, 5,  'and is silent — the confirming silence'),
    ('וקמו',    30, 5,  'then [all her vows] shall stand'),
    ('הניא',    30, 6,  'restrain — the annulment\'s verb'),
    ('ביום',    30, 6,  'on the day [of his hearing] — the clock'),
    ('שמעו',    30, 6,  'his hearing'),
    ('יסלח',    30, 6,  'will forgive — "and the LORD will forgive her"'),
    ('היו',     30, 7,  'be — the doubled verb "be, she shall be"'),
    ('תהיה',    30, 7,  'she shall be'),
    ('מבטא',    30, 7,  'the utterance of [her lips] — the oath (Sifrei 153:7)'),
    ('יניא',    30, 9,  'he restrains — beside "and annuls" (the pair)'),
    ('והפר',    30, 9,  'and annuls'),
    ('אלמנה',   30, 10, 'a widow'),
    ('וגרושה',  30, 10, 'or a divorced woman'),
    ('בשבעה',   30, 11, 'by an oath — starred'),
    ('הפר',     30, 13, 'annul — the doubled verb'),
    ('יפר',     30, 13, 'he annuls'),
    ('מוצא',    30, 13, 'all that proceeds from [her lips]'),
    ('שבעת',    30, 14, 'the oath of — starred'),
    ('לענת',    30, 14, 'to afflict [a soul]'),
    ('יקימנו',  30, 14, 'shall confirm IT'),
    ('יפרנו',   30, 14, 'shall annul IT — R. Akiva\'s mem'),
    ('החרש',    30, 15, 'be silent — the doubled verb "silent, he is silent"'),
    ('יחריש',   30, 15, 'he is silent'),
    ('מיום',    30, 15, 'from day [to day]'),
    ('הקים',    30, 15, 'he has confirmed'),
    ('אחרי',    30, 16, 'after [his hearing] — after his confirming (Sifrei 156:2)'),
    ('ונשא',    30, 16, 'then he shall bear [her iniquity]'),
    ('עונה',    30, 16, 'her iniquity'),
    ('אלה',     30, 17, 'these are [the statutes] — the footer'),
    ('החקים',   30, 17, 'the statutes'),
    ('לאשתו',   30, 17, 'to his wife'),
    ('לבתו',    30, 17, 'to his daughter'),
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
SPAN = [(30, v) for v in range(1, 18)]
NUMBERS = {v: ink_numbers(verse_words('Num', 30, v)) for _, v in SPAN}
ORDINALS = {v: ink_ordinals(verse_words('Num', 30, v)) for _, v in SPAN}
STARRED = [(v, t) for _, v in SPAN for t in verse_words('Num', 30, v) if t.endswith('*')]
assert all(not n for n in NUMBERS.values()) and all(not o for o in ORDINALS.values()), (NUMBERS, ORDINALS)       # no cardinal, no ordinal in the chapter
assert STARRED == [(3, 'שבעה*'), (11, 'בשבעה*'), (14, 'שבעת*')], STARRED                                            # the three oath-tokens the seven-stem's refused homograph
FIRST = {v: words(30, v)[0] for _, v in SPAN}
WHEN = [v for _, v in SPAN if len(words(30, v)) > 1 and words(30, v)[1] == 'כי' and v in (3, 4)]                     # the two "when" cases at the second word ("a man, when"; "and a woman, when")
AND_IF = [v for _, v in SPAN if FIRST[v] == 'ואם']                                                                    # the seven "and if" branches at the first word
KI_SEATS = [(v, i) for _, v in SPAN for i, w in enumerate(words(30, v)) if w == 'כי']
assert WHEN == [3, 4] and AND_IF == [6, 7, 9, 11, 13, 15, 16] and KI_SEATS == [(3, 1), (4, 1), (6, 18), (15, 20)], (WHEN, AND_IF, KI_SEATS)
# the whole-DB phrase census (the seats typed from the measurement print of 2026-09-12)
_V = collections.OrderedDict()
for b, c, v, he in db.execute("SELECT v.book, v.chapter, v.verse, w.he FROM words w JOIN verses v ON w.verse_id=v.id ORDER BY v.id, w.idx"):
    _V.setdefault((b, c, v), []).append(strip(he))
def seats(phrase):
    p = phrase.split(); n = len(p)
    return ['%s %d:%d' % k for k, ws in _V.items() if any(ws[i:i + n] == p for i in range(len(ws) - n + 1))]
DAY_OF_HEARING = seats('ביום שמעו'); FORGIVE = seats('ויהוה יסלח לה'); DAY_TO_DAY = seats('מיום אל יום'); AFTER_HEARING = seats('אחרי שמעו')
HEADS = seats('ראשי המטות'); THIS_IS = seats('זה הדבר אשר צוה יהוה'); FOOTER = seats('אלה החקים'); RECEIPT2 = seats('ככל אשר צוה יהוה את משה')
ANNUL_ANNUL = seats('הפר יפר'); BE_BE = seats('היו תהיה'); SILENT_SILENT = seats('החרש יחריש'); SWEAR_OATH = seats('השבע שבעה')
WIDOW_DIVORCEE = seats('אלמנה וגרושה'); UTTERANCE = seats('מבטא שפתיה'); BEAR_HER = seats('ונשא את עונה'); IN_HER_YOUTH = seats('בנעריה')
BETWEEN_MAN = seats('בין איש לאשתו'); BETWEEN_FATHER = seats('בין אב לבתו'); AFFLICT = seats('לענת נפש'); HUSBANDS_HOUSE = seats('בית אישה')
assert DAY_OF_HEARING == ['Num 30:6', 'Num 30:8', 'Num 30:13', 'Num 30:15'] and FORGIVE == ['Num 30:6', 'Num 30:9', 'Num 30:13'], (DAY_OF_HEARING, FORGIVE)
assert DAY_TO_DAY == ['1Chr 16:23', 'Num 30:15'] and AFTER_HEARING == ['Num 30:16'], (DAY_TO_DAY, AFTER_HEARING)
assert HEADS == ['1Kgs 8:1', '2Chr 5:2', 'Num 30:2'] and len(THIS_IS) == 8 and THIS_IS[-2:] == ['Num 30:2', 'Num 36:6'], (HEADS, THIS_IS)
assert FOOTER == ['Deut 12:1', 'Lev 26:46', 'Num 30:17'] and len(RECEIPT2) == 7 and RECEIPT2[-1] == 'Num 30:1', (FOOTER, RECEIPT2)
assert ANNUL_ANNUL == ['Num 30:13', 'Num 30:16'] and BE_BE == ['Jer 15:18', 'Num 30:7'] and SILENT_SILENT == ['Num 30:15'] and SWEAR_OATH == ['Num 30:3'], (ANNUL_ANNUL, BE_BE, SILENT_SILENT, SWEAR_OATH)
assert WIDOW_DIVORCEE == ['Lev 21:14', 'Lev 22:13', 'Num 30:10'] and UTTERANCE == ['Num 30:7', 'Num 30:9'] and BEAR_HER == ['Num 30:16'], (WIDOW_DIVORCEE, UTTERANCE, BEAR_HER)
assert IN_HER_YOUTH == ['Num 30:4', 'Num 30:17'] and BETWEEN_MAN == ['Num 30:17'] and BETWEEN_FATHER == ['Num 30:17'] and AFFLICT == ['Num 30:14'] and HUSBANDS_HOUSE == ['Num 30:11', 'Ruth 1:9'], (IN_HER_YOUTH, BETWEEN_MAN, BETWEEN_FATHER, AFFLICT, HUSBANDS_HOUSE)
HUSBAND_TOKENS = sum(1 for _, v in SPAN for w in words(30, v) if w == 'אישה') + sum(1 for _, v in SPAN for w in words(30, v) if w == 'ואישה')   # 8 bare + 1 with the conjunction (30:14) = the reading's nine
FATHER_TOKENS = sum(1 for _, v in SPAN for w in words(30, v) if w == 'אביה')
assert HUSBAND_TOKENS == 9 and FATHER_TOKENS == 6, (HUSBAND_TOKENS, FATHER_TOKENS)
DOUBLED = [(3, 'השבע', 'שבעה'), (7, 'היו', 'תהיה'), (13, 'הפר', 'יפר'), (15, 'החרש', 'יחריש'), (16, 'הפר', 'יפר')]
for v, a, b in DOUBLED:
    ws = words(30, v); assert any(ws[i] == a and ws[i + 1] == b for i in range(len(ws) - 1)), (v, a, b)               # the five doubled verbs adjacent
RESTRAIN_ANNUL = [i for i, w in enumerate(words(30, 9)) if w == 'יניא' and words(30, 9)[i + 2] == 'והפר']             # 30:9 "he restrains her and annuls" — the pair's one seat
assert RESTRAIN_ANNUL == [4], RESTRAIN_ANNUL
FRAME_VERBS = [(v, FIRST[v]) for _, v in SPAN if FIRST[v] in ('ויאמר', 'וידבר')]
assert FRAME_VERBS == [(1, 'ויאמר'), (2, 'וידבר')] and 'יהוה' not in (words(30, 1)[1], words(30, 2)[1]), FRAME_VERBS   # both Moses' — no divine frame
CONFIRM_ANNUL_IT = (words(30, 14)[8], words(30, 14)[10])
assert CONFIRM_ANNUL_IT == ('יקימנו', 'יפרנו'), CONFIRM_ANNUL_IT                                                       # "confirm IT ... annul IT" — the two verbs with the one suffix (R. Akiva's mem)

# ---- THE CALLEES (live import edges; the design's cells by name) ----
NAZ_SUB = NS.nazirite({'ask': 'vow_form', 'form': 'substitute'}, NS.DATA); NAZ_PART = NS.nazirite({'ask': 'vow_form', 'form': 'partial'}, NS.DATA)          # THE CALL: the nazirite's vow-form
SOTAH_CLEAN = NS.sotah({'ask': 'husband_clean'}, NS.DATA); SOTAH_UNCLEAN = NS.sotah({'ask': 'husband_clean', 'clean': False}, NS.DATA)                     # THE CALL: 5:31's "bear her iniquity"
assert NAZ_SUB[0] == 'binds (nazir lehazir)' and NAZ_PART[0] == 'a full nazirite' and 'nazirite_vow_bound' in NAZ_SUB[1], (NAZ_SUB, NAZ_PART)
assert SOTAH_CLEAN[0] == 'tested' and SOTAH_UNCLEAN[0].startswith('the waters do not test'), (SOTAH_CLEAN, SOTAH_UNCLEAN)
OATH_OPTION = V5.graded_offering({'trigger': 'utterance_oath', 'act_is_his_option': True, 'oath_forgotten': True, 'means': 'reaches_lamb'}, V5.DATA)     # THE CALL: Lev 5:4's option template
OATH_NO_OPTION = V5.graded_offering({'trigger': 'utterance_oath', 'act_is_his_option': False}, V5.DATA)
assert OATH_OPTION[0].startswith('CONFESS') and OATH_NO_OPTION[0] == 'exempt', (OATH_OPTION[0], OATH_NO_OPTION[0])
PR_RETURN = PR.holy_food('return'); PR_TABLE = PR.holy_food('eating_table', husband='israelite', son_alive=False, after='fathers_house')                     # THE CALL: Lev 22:13's return
assert PR_RETURN['v']['widow_and_divorcee'] == 'both_written_both_need_no_seed' and PR_TABLE['v'] == 'terumah_returns', (PR_RETURN['v'], PR_TABLE['v'])
MU_DEADLINE = MU.the_calendar({'ask': 'vow_deadline'}, MU.DATA); MU_ROW = MU.DATA['vow_deadline']                                                              # THE CALL: the vow_deadline row READ
assert MU_DEADLINE[0] == 'three festivals in any order — the first tanna' and MU_ROW['value'] == 'three_festivals_any_order' and len(MU_ROW['settings']) == 4, (MU_DEADLINE[0], MU_ROW['value'])
MO_YK = MO.yom_kippur(); MO_AFFLICTION = MO_YK['affliction_list']['v']                                                                                        # THE CALL: the affliction-root's Yom Kippur seats
assert MO_AFFLICTION == 'eating_drinking_washing_anointing_sandals_relations', MO_AFFLICTION
# THE CALENDAR ROW (the third registry, read as DATA — the state machine's clock)
CAL_ROW = yaml.safe_load(open(_os.path.join(HERE, 'calendar_parameters.yaml'), encoding='utf-8'))['parameters']['vow_annulment_window']
WINDOW = CAL_ROW['value']
assert WINDOW == 'to_nightfall' and set(CAL_ROW['settings']) == {'to_nightfall', 'twenty_four_hours'}, CAL_ROW
def hearing_due(world):
    """the annulment window's end at the day grain: the hearing day + 1 on the engine's evening boundary (the row's running setting;
    the twenty-four-hour arm would land inside the next day — sub-day is out, the arm recorded and never run)"""
    return world.clock.day + 1

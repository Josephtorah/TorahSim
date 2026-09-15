import os as _os
_ROOT = _os.path.normpath(_os.path.join(_os.path.dirname(_os.path.abspath(__file__)), '..', '..'))   # THE PORTABLE REPO (2026-09-15): the repo root from this file's own place
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
assert GUARDED == 147, ("the guard counted %d expectations, the tripwire holds 147" % GUARDED)   # the design's estimate — retyped from the guard's print after the first run
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


# ===== THE DATA CHANNEL — the parameter rows the ink leaves open (motion 2's recorded settings) =========
DATA = {
    'vow_ages': {'value': 'girl_12_boy_13_examined_year_before', 'settings': {'girl_12_boy_13_examined_year_before': "Mishnah Niddah 5:6 (45b:2-4): the girl of eleven and a day EXAMINED (does she know in Whose name?), twelve and a day valid; the boy twelve and a day examined, thirteen and a day valid; before — no vow even saying 'we know'; after — a vow even saying 'we do not know' (45b:9); hairs during the year as before (46a:3, 46a:12); Rebbi's order", 'boys_first': "R. Shimon b. Elazar: the boy's development first — the periods reversed (Niddah 45b:10)"},
                 'source': "30:3 'a man' excludes the minor (Sifrei 153:3); the age by the identity with 6:2's 'clearly utter' (Niddah 46a:2 — NS.nazirite by CALL); the year's numbers the shelf's"},
    'sage_release': {'value': 'expert_alone_or_three_laymen', 'settings': {'expert_alone_or_three_laymen': "'the heads of the tribes' (30:2) — a single expert (Rav Chisda / R. Yochanan, Nedarim 78b:3; Bava Batra 121a:5); three laymen by the verbal analogy with Lev 17:2 or by ben Azzai (78a:3, 78b:2); standing, alone, at night, on the Sabbath, by relatives (77b:2); in the presence of the one vowed against (65a:1-4); only a vow in effect (90a:3, 90b:4); by an opening — the mistaken vow void, the new situation disputed (Mishnah Nedarim 9:1-10); with regret (Rabban Gamliel, 77b:3) or without (Rav Nachman)", 'flies_in_the_air': "Mishnah Chagigah 1:8 (10a:4): nothing to support it — the hints (R. Eliezer's 'clearly utter' twice; R. Yehoshua's 'I swore in My wrath'; R. Yitzchak's 'willing heart'; Chananya's 'I swore and fulfilled') each refuted; Shmuel's 'he shall not profane HIS word — others may' unrefuted (10a:9, 10a:13)"},
                     'source': "the ink of the chapter never names the sage: the husband ANNULS (six tokens), 'permits' never (computed at the reading) — the office the Sifrei 153:1's own addition on the FREED phrase 'to the heads of the tribes'; an answer-sheet row, never code"},
    'annul_by_messenger': {'value': 'husband_alone', 'settings': {'husband_alone': "R. Yoshiyah: 'her husband confirms, her husband annuls' (30:14) — the doubled 'her husband' a Torah edict; the steward told 'annul my wife's vows till I return' annuls nothing (Sifrei 153:6, 154:3; Nedarim 72b:8; Nazir 12b:3; Bava Metzia 96a:20)", 'agent_as_himself': "R. Yonatan: a man's agent is as himself everywhere (the principle's sources Kiddushin 41b:5, the Passover's 'the whole assembly shall slaughter it') — the steward annuls (72b:9)"},
                           'source': "30:6 'because her father restrained her', 30:13 'her husband has annulled them' — the act HIS; the steward the court's appointee from 'take one prince' (Num 34:18 — Kiddushin 42a:8, forward)"},
    'annul_in_advance': {'value': 'not_annulled', 'settings': {'not_annulled': "the Rabbis: 'her husband confirms IT, her husband annuls IT' (30:14) — what came to confirmation came to annulment; a vow not yet made reached neither (Mishnah Nedarim 10:7; Sifrei 153:10; Nedarim 75a:6, 76b:1)", 'annulled': "R. Eliezer's a-fortiori — he stipulates against his own future vows where he cannot annul them after; his wife's, which he annuls after, surely before (Sifrei 153:3, 153:10; Nedarim 75b:4; whether they take effect a moment or never — 75a:7-76a:3)"},
                         'source': "30:9 'and he annul her vow WHICH IS UPON HER' — the vows upon her, not the vows she will make (Sifrei 153:10)"},
    'partial_annulment': {'value': 'whole_only_yishmael', 'settings': {'whole_only_yishmael': "R. Yishmael (the Mishnah's arm, Nedarim 11:6 at 87a:9-10): 'figs and grapes are konam to me' — confirmed for the figs, ALL confirmed; annulled for the figs, NOT annulled until the grapes too; 'a fig and a grape' two vows (Sifrei 155:1)", 'part_annuls_whole_akiva': "R. Akiva: 'he shall confirm IT ... annul IT' (30:14) read yakim MIMMENNU — a part confirms the whole, so a part annuls the whole (87b:1; the Sifrei 155:1's second arm); the sage's partial release releases all (Mishnah Nedarim 9:6)", 'no_more_than_annulled_rabbis': "the Rabbis by R. Yochanan: what he annulled he annulled, what he confirmed he confirmed, no more (87b:2)"},
                          'source': "30:14 'her husband shall confirm IT, or her husband shall annul IT' — the two verbs with the one suffix (computed)"},
    'affliction_scope': {'value': 'rabbis_broad_shmuel', 'settings': {'rabbis_broad_shmuel': "the first tanna: 'if I bathe / if I do not bathe, if I adorn / do not adorn' are vows of affliction (Mishnah Nedarim 11:1); Shmuel by Levi: every affliction vow annulled except one wholly between her and another (82a:3); Shmuel rules as the Rabbis (82b:1)", 'yosei_narrow': "R. Yosei: those are not affliction; the produce of the WORLD is (he annuls), of this COUNTRY not (he brings from another), of this STOREKEEPER not, unless his sustenance is from him alone (11:2; the Sifrei 155:1's R. Yonatan case list); the whole eleventh chapter R. Yosei's (Rav Huna, 82a:2); by R. Yosei the bathe/adorn vows annulled as between him and her (Rav Adda b. Ahava, 81a:10; the baraita 81b:2-3) or not (Rav Huna, 81b:1)", 'leads_to_affliction_rava': "Rava: the vows' affliction is what LEADS to affliction (not bathing, felt later), Yom Kippur's what is felt now — one root, two senses (80b:6; MO.yom_kippur by CALL)"},
                         'source': "30:14 'every vow and every oath of binding TO AFFLICT A SOUL' restricts 30:9's 'the vow upon her' (Sifrei 155:1); 30:17 'between a man and his wife' adds the vows that touch him (Nedarim 79b:2)"},
    'fathers_scope': {'value': 'likened_to_the_husband', 'settings': {'likened_to_the_husband': "the Sifrei 155:1: 'I reasoned and reversed' — the induction from the husband refused, the reversal refuted by 'in her youth in her father's house', and 30:17's likening decides: the father as the husband (the affliction filter)", 'all_vows': "the reversed induction's arm — 'as the father annuls every vow' (the Sifrei's own refuted step; the docket found no Talmud row ruling the father broader: the arm recorded from the Sifrei alone)"},
                      'source': "30:17 'between a man and his wife, between a father and his daughter' — the likening BOTH WAYS in every rule stated (Sifrei 156:3)"},
    'betrothed_authority': {'value': 'joint', 'settings': {'joint': "the father AND the husband annul the betrothed maiden's vows together; one alone annuls nothing; one confirming blocks (Mishnah Nedarim 10:1; Rabba from 30:7-9, Nedarim 67a:5; R. Yishmael's school from 30:17, 68a:1; Sifrei 156:3); the annuller WEAKENS the vow, never severs (Beit Hillel, 69a:2, 71b:1); the father dies — no reversion to the betrothed; the betrothed dies — reversion to the father, if he had not confirmed nor died silent the next day (10:2; 70a:7-8; 68a:5-68b:3)", 'sustained_betrothed_eliezer': "R. Eliezer: the adult who waited twelve months (the widow thirty days) — the husband annuls alone, he owes her sustenance ('every woman vows on her husband's consent', 73b:5); the Rabbis: not until she enters his authority (10:5)"},
                            'source': "30:7 'and if she BE to a husband and her vows are upon her' — the betrothed (R. Yoshiyah; the Sifrei 153:7); the joint annulment the answer sheet's"},
    'annul_on_sabbath': {'value': 'permitted_even_not_for_the_sabbath', 'settings': {'permitted_even_not_for_the_sabbath': "by the whole-day arm of the deadline: he annuls on the Sabbath even not for its need, else a Sabbath vow could never be annulled (Nedarim 77a:4; Mishnah Shabbat 24:5 at 157a:5); the Sabbath's formula 'take and eat' with the heart's annulment (77b:6)", 'for_the_sabbaths_need_only': "by the twenty-four-hour arm — he may annul after the Sabbath (77a:4; Zutei's baraita 77a:2, Shabbat 157a:8)"},
                         'source': "the Sabbath rule hangs on the deadline's arm — the calendar row vow_annulment_window (Shabbat 157a:9-11)"},
    'measure_of_good_ratio': {'value': 500, 'settings': {500: "the measure of good exceeds the measure of punishment five hundredfold — 'to thousands' (Exod 20:6) against 'the third and fourth generation' (20:5): Sanhedrin 100a:17-18 (R. Meir: which attribute is greater?), Yoma 76a:7 (R. Elazar HaModai: the flood's windows against the manna's doors — there four)", 4: "Yoma 76a:8's own arithmetic on the flood and the manna: two doors of four windows each against two windows — four"},
                              'source': "the Sifrei 156:2's a-fortiori on 'he shall bear her iniquity': under the small measure he takes her place, under the great measure surely — the ratio the tradition's arithmetic, never the ink's"},
    'widows_vow_timing': {'value': 'at_the_vows_making', 'settings': {'at_the_vows_making': "the Mishnah (11:9; 89a:1): the widow's 'nazirite after thirty days' married within — the new husband cannot annul; vowed under the husband and annulled, widowed within — annulled; ONCE OUT ONE HOUR he annuls no more; R. Akiva (89a:2-4): the vow's BINDING at her widowhood", 'at_the_vows_taking_effect_yishmael': "R. Yishmael: 'shall stand against her' — the vow's application in widowhood; the vow hung on marriage follows its taking effect, hung on days its utterance (89a:2-5)"},
                          'source': "30:10 'the vow of a widow or of a divorced woman ... shall stand against her' — which moment the ink does not say"},
    'divorce_as': {'value': 'unresolved', 'settings': {'unresolved': "is a divorce after the hearing as SILENCE (he annuls on remarrying the same day) or as CONFIRMATION? the deaths baraita proves nothing (its clauses shaped by each other), 10:3 and 89a's mishna each answered — TEIKU (Nedarim 71b:2-72a:8): the machine writes nothing at a divorce; the vow stands until an act"},
                   'source': "no divorce in the chapter's ink — the shelf's own open question"},
    'hearing_required': {'value': 'unresolved_the_ink_names_the_hearing', 'settings': {'unresolved_the_ink_names_the_hearing': "may the husband annul WITHOUT hearing? the scholars' advance annulments and R. Eliezer's are read 'when I hear it' (Nedarim 72b:3-73a:1) — TEIKU; the deaf man cannot annul (73a:4 — 'and her husband hears it'); the machine's trigger is the hearing, the ink's own word (six tokens)"},
                         'source': "30:5, 30:8, 30:12 'and ... hears' — the hearing-infinitive six tokens in the chapter"},
    'annul_before_effect': {'value': 'rabbis_even_before', 'settings': {'rabbis_even_before': "the Rabbis: the husband annuls a conditional vow before it takes effect ('He annuls the thoughts of the crafty', Job 5:12 — Nedarim 90a:2; 89b:4-5 the fathers' benefit / 'removed from the Jews' if I engage with you)", 'natan_only_in_effect': "R. Natan: only once in effect ('the moon shall be confounded', Isa 24:23 heard as annulled — what exists); the sage's dissolution only of a vow in effect by all (90a:3, 90b:4)"},
                            'source': "30:9 'which is upon her' — the vow's existence; the conditional vow the shelf's question"},
    'annulment_reach': {'value': 'affliction_for_others_between_for_himself', 'settings': {'affliction_for_others_between_for_himself': "affliction vows annulled for himself AND for others (she marries another — still annulled); between-them vows for himself only (a second husband — the vow takes effect); 'I am removed from the Jews' — he annuls his part, she is forbidden to all if divorced (Nedarim 79b:5, 82a:1, 84a:2; Mishnah 11:12)", 'revive_at_divorce': "the Sages' first answer: between-them annulments lapse at the divorce (79b:3 — refuted by R. Yochanan b. Nuri's handiwork vow, 79b:4)"},
                        'source': "30:17 'between a man and his wife' — the class whose annulment is bounded by the marriage"},
    'yavam_annuls': {'value': 'never_akiva', 'settings': {'never_akiva': "R. Akiva: the widow awaiting the brother-in-law is not a full wife — no annulment, one brother or two; the bond not substantial (Mishnah Nedarim 10:6; 74a:4-5)", 'eliezer_annuls': "R. Eliezer: 'a woman acquired for him from Heaven' — he annuls (after levirate betrothal, Rav Ami 74a:6; or when he owes her sustenance, 74a:9)", 'yehoshua_one_brother': "R. Yehoshua: one brother yes, two no (74a:4, 74a:7)"},
                     'source': "no brother-in-law in the chapter — the widow's row extended by the shelf"},
    'vow_support_base': {'value': 'vowed_thing_only', 'settings': {'vowed_thing_only': "'when a man vows a vow' (30:3) — a vow takes effect by association with a thing forbidden BY A VOW (an offering, a konam), not by the Torah (carrion, the pig, Aaron's terumah — Mishnah Nedarim 2:1; 13a:2, 14a:5; Shevuot 20b:3); the firstborn excluded (13a:2) or included by Rebbi's 'you shall consecrate' (13a:6)", 'lord_includes_torah_forbidden': "'TO THE LORD' (30:3) includes association with a Torah-forbidden item (13a:3) — or the sin and guilt offerings (13a:4)"},
                         'source': "30:3 'vows a vow' — the doubled noun (Shevuot 20b:3); the Sifrei 153:3's 'like an offering'"},
    'substitutes_source': {'value': 'nations_words_yochanan', 'settings': {'nations_words_yochanan': "R. Yochanan: konam, konach, konas (for an offering), cherek (for a dedication), nazik (for a nazirite), shevuta (for an oath) are the nations' words — they bind (Mishnah Nedarim 1:2 at 10a:11-12); the second tier (mekanamna …) Beit Shammai / Beit Hillel (10b:3)", 'devised_by_the_sages_lakish': "Reish Lakish: words the Sages devised lest one say 'an offering TO THE LORD' and stop at the Name (10a:12-13)"},
                           'source': "30:3 'vows a vow' — lindor neder read for the intimations (Nedarim 3b:4); the substitutes the answer sheet's"},
    'oath_by_the_heart': {'value': 'lips_required', 'settings': {'lips_required': "Shmuel: the oath needs the LIPS — 'take an oath clearly WITH HIS LIPS' (Lev 5:4; Shevuot 26b:9); the Tabernacle's willing-hearted donation stands apart (Exod 35:22; 26b:15-16 — the erection engine's given_by_the_heart); Deut 23:24 'that which has gone out of your lips'", 'heart_binds_sifrei': "the Sifrei 153:4's 'on his soul' — the vow received inwardly counts; Rav Sheshet's 'meant wheat, said bread — bound' (26b:14); R. Yitzchak's 'willing heart' for the vow (Chagigah 10a:8, 10a:11)"},
                          'source': "30:3 'according to all that proceeds out of his mouth', 30:13 'all that proceeds from her lips' — the ink names the mouth and the lips"},
    'konam_measure': {'value': 'any_amount', 'settings': {'any_amount': "konamot forbid ANY AMOUNT — the item itself forbidden 'like an offering', no 'eating' named (Rav Pappa, Shevuot 22a:9; 22a:2); two konamot naming 'eating' combine to an olive-bulk (22a:11)", 'no_meilah_akiva': "R. Akiva: no misuse of consecrated property applies to a konam (22a:6); R. Meir / the Rabbis on 'this loaf is konam to me' — he liable for misuse, another not, or neither (22a:15-22b:2)"},
                      'source': "the vow forbids the OBJECT (the two stringencies, Nedarim 13b:4) — its measure the shelf's"},
    'hearing_of_the_law': {'value': 'day_he_learned', 'settings': {'day_he_learned': "'I knew there are vows but not that there are annullers' — he annuls on the day he LEARNED there are (Mishnah Nedarim 11:7 at 87b:4); 'I knew of annullers but not that this is a vow' — R. Meir no, the Rabbis yes (87b:4; 79a:8-9)"},
                           'source': "30:6 'on the day of his hearing' — the hearing of the vow; the hearing of the LAW a second trigger the shelf adds"},
    'confirmation_dissolved': {'value': 'confirmation_yes_annulment_no', 'settings': {'confirmation_yes_annulment_no': "R. Yochanan: a sage dissolves a husband's CONFIRMATION, not his ANNULMENT (Nedarim 69a:4, 79a:3); the second confirmation after the first's dissolution takes effect (69a:6); confirmed AND annulled at once — nothing (69b:3); confirmed on condition the annulment holds — annulled (69b:1-2)"},
                               'source': "30:5 'then all her vows shall stand' — the confirmation irreversible by the HUSBAND (Sifrei 153:5); the sage's route the shelf's"},
    'vower_a_sinner': {'value': 'called_a_sinner', 'settings': {'called_a_sinner': "whoever vows, even fulfilling it, is called a sinner — 'if you refrain from vowing there is no sin in you' (Deut 23:23; Nedarim 77b:4); 'better than both is one who does not vow' — R. Yehuda's 'vows and pays' emended to 'volunteers and pays' (10a:1-2); whoever fasts needlessly is a sinner (R. Elazar HaKappar, 10a:9)"},
                       'source': "30:3 binds the vower; the vow's standing the shelf's verdict"},
    'annulment_in_the_heart': {'value': 'act_required', 'settings': {'act_required': "annulled in his heart — NOT annulled; confirmed in his heart — confirmed (Nedarim 79a:1); Beit Shammai: on the Sabbath in the heart, on a weekday with the lips (77b:7)", 'heart_suffices_hillel': "Beit Hillel: the heart's annulment suffices on both (77b:7); R. Yochanan: the Sabbath's 'take and eat' needs the heart's annulment too (77b:6)"},
                               'source': "30:6 'her father RESTRAINED her', 30:13 'her husband has annulled them' — an act named; the heart the shelf's question"},
    'share_or_weaken': {'value': 'weakens_hillel', 'settings': {'weakens_hillel': "Beit Hillel: the betrothed's annulment WEAKENS the whole vow (the father then annuls the whole again; she is not flogged for the two olives) — the halakha (the ruling) as Beit Hillel (Nedarim 69a:2, 71b:1)", 'severs_shammai': "Beit Shammai: each annuls HALF — the father completes the husband's portion (69a:1; 71a:4-5)"},
                        'source': "the joint annulment's arithmetic — the shelf's"},
}


# ===== F1: THE MAN (Num 30:2-3) =============================================================================
def the_man(case, data):
    del P[:]
    ask = case['ask']
    if ask == 'frame':
        ink('30:2', '"and Moses SPOKE to the heads of the tribes of the children of Israel, saying: THIS IS THE THING which the LORD commanded" — no divine frame: the formula at %d Bible seats, its two Numbers seats %s the book\'s two law chapters without "the LORD spoke to Moses" (computed)' % (len(THIS_IS), THIS_IS[-2:]))
        move('Sifrei 153:2', 'Moses prophesied with "thus said the LORD" as the prophets and ADDED "this is the thing" — the relay\'s own mark')
        move('Bava Batra 120b:1', 'the vows\' law in ALL generations by the verbal analogy "this" / "this" with Lev 17:2 — against 36:6\'s "this generation": the relayed statute is not case-bound (the installed_by decision\'s witness)')
        return out('a law relayed in Moses\' voice — this is the thing which the LORD commanded, for all generations', ['commanded'])
    if ask == 'this_is_the_thing':
        ink('30:2', '"this is the thing" — the limiter: the husband\'s verb in the chapter is ANNUL (six tokens), "permit" never (computed at the reading)')
        move('Sifrei 153:2; Nedarim 77b:9-78a:1', 'two a-fortiori refused by the words — the sage DISSOLVES and does not annul, the husband ANNULS and does not dissolve')
        move('Nedarim 77b:8 (R. Yochanan)', 'a sage who said "annulled" or a husband who said "dissolved" HAS SAID NOTHING — each office its own verb')
        return out('two offices, two verbs — the husband annuls, the sage dissolves; the words crossed say nothing', ['accepted'])
    if ask == 'heads_of_the_tribes':
        ink('30:2', '"to the heads of the tribes" — %d Bible seats (Solomon\'s assembly the other two), "TO the heads" one (computed)' % len(HEADS))
        move('Sifrei 153:1 (R. Yonatan)', 'the frame freed by Exod 34:31-32 (the princes return first) — the FREED phrase teaches: the release of vows by experts alone')
        move('Nedarim 78b:3 (Rav Chisda / R. Yochanan); 78a:3; 78b:2 (ben Azzai)', 'a single expert from "the heads of the tribes"; three laymen by the verbal analogy with Lev 17:2, or by ben Azzai\'s "the vows\' portion needs no expert"')
        dat('the row sage_release = %s' % data['sage_release']['value'])
        return out('the sage\'s release — one expert or three laymen: the shelf\'s office on the freed phrase', ['accepted'])
    if ask == 'sage_release_flies':
        move('Mishnah Chagigah 1:8 (10a:4)', 'the dissolution of vows FLIES IN THE AIR — nothing to support it')
        move('Chagigah 10a:9, 10a:13 (Shmuel; Rava)', 'Shmuel\'s source has no refutation: "he shall not profane HIS word" — he cannot, others may; "one spicy pepper is better than a basket of squash"')
        return out('flies in the air — the one unrefuted ground the chapter\'s own clause 30:3', ['accepted'])
    if ask == 'sage_release_form':
        move('Nedarim 77b:2 (Rav Nachman); 77a:7 (Abaye)', 'dissolved standing, alone, at night, on the Sabbath, by relatives, even when one could have asked before — no court act')
        move('Nedarim 77b:3', 'Rabban Gamliel sat — an opening by REGRET needed; Rav Nachman: not needed')
        dat('the row sage_release = %s' % data['sage_release']['value'])
        return out('no session, no court — standing, alone, at night; the regret arm recorded', ['accepted'])
    if ask == 'sage_release_presence':
        move('Nedarim 65a:1 (Rav Nachman; Tosefta 2:12); 65a:4', 'a vow off a person is dissolved only IN HIS PRESENCE — "in MIDIAN ... go, return" (Exod 4:19); Zedekiah\'s oath and the Sanhedrin\'s error')
        return out('dissolved in the presence of the one vowed against', ['accepted'])
    if ask == 'sage_release_timing':
        move('Nedarim 90a:3; 90b:4', 'the sage dissolves only a vow IN EFFECT — "his word" must be his in force (R. Natan and the Rabbis agree; the second version refuted)')
        return out('only a vow in effect is dissolved', ['accepted'])
    if ask == 'openings':
        move('Mishnah Nedarim 9:1-10', 'the openings: the parents\' honor (disputed), the new situation (disputed), the Torah\'s prohibitions, the marriage contract, the Sabbaths and festivals, his own honor')
        return out('an opening on "had I known" — the answer sheet\'s method, never the ink\'s', ['accepted'])
    if ask == 'mistaken_vow':
        move('Mishnah Nedarim 9:10 (66a:12); 65a:6 (R. Yochanan)', '"ugly so-and-so" who is beautiful — permitted: a vow MISTAKEN FROM THE OUTSET never took effect; the dog already dead')
        return out('a mistaken vow — no vow', ['exempt'])
    if ask == 'age':
        age, sex, knows = case['age'], case['sex'], case.get('knows_to_whom', True)
        floor, top = (11, 12) if sex == 'girl' else (12, 13)
        ink('30:3', '"a MAN, when he vows" — the minor excluded (Sifrei 153:3); "and a woman ... in her youth" (30:4)')
        move('CALLED cold_run_naso.nazirite(vow_form) -> %s [IMPORT, live]' % NAZ_SUB[0], 'the age by the identity with 6:2 "when a man or woman shall clearly utter a vow" — Niddah 46a:2 (thirteen and a day without clear utterance)')
        move('Mishnah Niddah 5:6 (45b:2-4)', 'the girl eleven and a day EXAMINED, twelve and a day valid; the boy twelve / thirteen; before — no vow even saying "we know"; after — a vow even saying "we do not know"')
        dat('the row vow_ages = %s' % data['vow_ages']['value'])
        if age < floor:
            return out('a minor — no vow, no consecration (even saying "we know")', ['exempt'])
        if age < top:
            return out('the examined year — bound if she knows in Whose name' if knows else 'the examined year — she does not know in Whose name: no vow', ['vow_bound'] if knows else ['exempt'])
        return out('of age — the vow stands without examination', ['vow_bound'])
    if ask == 'vow_vs_oath':
        ink('30:3', '"vows a vow to the LORD, or swears an oath to bind a bond on his soul" — vows and oaths ADJACENT (Nedarim 2b:2); the oath by the seven-stem, starred by the parser at %s' % STARRED)
        move('Nedarim 13b:4; Shevuot 25a:11-12', 'THE TWO STRINGENCIES — vows take effect on a MITZVA, oaths not (no oath to neglect a mitzva — "HIS word he shall not profane", 16b:3); oaths take effect on the INTANGIBLE, vows only on substance')
        move('Sifrei 153:3', 'a vow is as by the king\'s life, an oath as by the King himself (2 Kings 2:2 the form)')
        return out('the vow binds the OBJECT (even a mitzva\'s), the oath binds the PERSON (even to nothing tangible)', ['accepted'])
    if ask == 'vow_support':
        base = case['base']
        ink('30:3', '"vows a VOW" — the doubled noun (Shevuot 20b:3); "to the LORD" (Nedarim 13a:3-4)')
        move('Nedarim 14a:5, 13a:2; Mishnah Nedarim 2:1 (13b:7)', 'a vow takes effect by association with a thing forbidden BY A VOW (an offering, a konam); by a Torah-forbidden thing (carrion, the pig, Aaron\'s terumah) it does not — the firstborn disputed')
        dat('the row vow_support_base = %s' % data['vow_support_base']['value'])
        return out('leans on a vowed thing — bound' if base == 'vowed' else 'leans on a Torah-forbidden thing — no vow', ['vow_bound'] if base == 'vowed' else ['exempt'])
    if ask == 'substitutes':
        move('Mishnah Nedarim 1:2 (10a:11); 10b:11', 'konam, konach, konas bind as "an offering"; nazik as "a nazirite"; shevuta as "an oath"; "by mohi" nothing, "by the oath Mohi said" binds')
        dat('the row substitutes_source = %s' % data['substitutes_source']['value'])
        return out('the substitutes bind — the nations\' words or the Sages\' devised ones', ['vow_bound'])
    if ask == 'not_non_sacred':
        move('Mishnah Nedarim 1:3 (10b:12); 11b:1, 11b:6', '"what I eat of yours shall be NOT non-sacred" — forbidden; "as non-sacred" — permitted; R. Meir infers no positive from a negative')
        return out('the negation of the common binds — "not non-sacred" is an offering', ['vow_bound'])
    if ask == 'on_a_limb':
        move('Mishnah Nedarim 1:4 (13b:3); Rav Yehuda 13b:5', '"konam my MOUTH speaking with you, my HAND working, my FOOT walking" — a vow on a limb, a thing of substance — forbidden; "what I speak" would be intangible')
        return out('a vow on the limb binds; on the act it would not', ['vow_bound'])
    if ask == 'bind_the_permitted':
        ink('30:3', '"to BIND a bond on his soul" — bind the permitted, not permit the forbidden (Sifrei 153:4)')
        move('Shevuot 27a:1-5; Nedarim 16b:3', 'an oath to eat carrion or to neglect a mitzva takes no effect — "sworn from Sinai"; the oath to harm himself binds (27a:6)')
        return out('no oath to permit the forbidden — the oath void', ['exempt'])
    if ask == 'not_profane':
        ink('30:3', '"he shall not PROFANE his word" — one Bible seat in this sense (computed)')
        move('Sifrei 153:4; Nedarim 81b:5, 90a:3', 'HE shall not profane it — the sage releases others, not himself; Rabban Gamliel: annul even a vow that does not take effect')
        move('Nedarim 15a:8, 81b:9', 'the custom of a place treated as forbidden — "he shall not profane his word" by rabbinic law (a quasi-vow)')
        return out('the vower bound to his word; the sage not for himself; the custom a quasi-vow', ['commanded'])
    if ask == 'two_transgressions':
        ink('30:3', '"he shall not profane his word; according to all that proceeds out of his mouth he shall do" — the two clauses')
        move('Sifrei 153:4; Nedarim 3a:7', 'TWO transgressions on the unpaid vow — "he shall not profane" and "you shall not delay" (Deut 23:22), on the nazirite\'s vow too')
        move('CALLED cold_run_musafim.the_calendar(vow_deadline) -> %s; DATA vow_deadline = %s (%d settings) [IMPORT, live]' % (MU_DEADLINE[0], MU_ROW['value'], len(MU_ROW['settings'])), 'the delay ban\'s clock in festivals — the musafim runner\'s row READ, never re-declared (the 9b debt (iv) paid); Deuteronomy 23 not compiled — OWED')
        return out('profane and delay — two transgressions; the delay counted in festivals by call', ['commanded'])
    if ask == 'delay_clocks':
        move('Rosh Hashanah 4a:13-14, 4b:2 (the five counts); 6a:16 (Rava); 6a:14 (Rava)', 'three festivals (the first tanna) / in order (R. Shimon) / one (R. Meir) / two (R. Eliezer b. Yaakov) / by Sukkot (R. Elazar b. R. Shimon); the POSITIVE mitzva at the first festival; CHARITY at once — the poor are everywhere')
        move('Rosh Hashanah 5b:11', 'the count RESTARTS at a replacement animal\'s consecration')
        return out('two dues — the positive at the first festival, the prohibition at the third; charity now', ['commanded'])
    if ask == 'sin_in_you':
        move('Rosh Hashanah 5b:5; 6a:3', '"and it would be sin IN YOU" — not in your offering (the late offering not disqualified), not in your wife (the delay\'s sin his alone)')
        return out('the delay\'s sin on the vower alone — the offering and the wife unmoved', ['accepted'])
    if ask == 'vow_vs_gift':
        move('Rosh Hashanah 6a:12; 6a:8', 'a VOW-offering ("upon me") — died or stolen, he pays again; a GIFT ("this one") — not liable; the bare vow and the designated animal both transgress by delay')
        return out('the vow\'s debit persists past its object; the gift\'s dies with it', ['vow_bound'])
    if ask == 'lips_or_heart':
        ink('30:3, 30:13', '"according to all that proceeds out of his MOUTH", "all that proceeds from her LIPS" — the ink names the mouth and the lips')
        move('Shevuot 26b:9 (Shmuel); 26b:15-16', 'the oath needs the lips — "clearly with his lips" (Lev 5:4); the Tabernacle\'s willing heart (Exod 35:22) stands apart')
        move('Sifrei 153:4; Chagigah 10a:8, 10a:11', '"on his soul" — the inward acceptance counts (the Sifrei); R. Yitzchak\'s "willing heart" for the vow')
        dat('the row oath_by_the_heart = %s' % data['oath_by_the_heart']['value'])
        return out('the lips required — the heart\'s vow the Sifrei\'s arm, recorded', ['accepted'])
    if ask == 'vower_a_sinner':
        move('Nedarim 77b:4 (Rav Dimi; Rav Zevid on Deut 23:23); 10a:9 (R. Elazar HaKappar)', 'whoever vows, even fulfilling it, is called a sinner; whoever fasts needlessly is a sinner')
        dat('the row vower_a_sinner = %s' % data['vower_a_sinner']['value'])
        return out('the vower called a sinner — the vow\'s standing on the shelf', ['accepted'])
    if ask == 'on_his_soul':
        ink('30:3', '"to bind a bond ON HIS SOUL" — the chapter\'s one masculine soul-token against ten "her soul" (computed)')
        move('Nazir 61a:8 (Rava)', 'one whose soul is in his own possession — the SLAVE excluded from vows (the nazirite\'s verse includes him there)')
        return out('the slave\'s soul not his — no vow', ['exempt'])
    if ask == 'konam_measure':
        move('Shevuot 22a:9 (Rav Pappa); 22a:2; 22a:6 (R. Akiva)', 'konamot forbid ANY AMOUNT — the item itself "like an offering"; no misuse of consecrated property applies to a konam (R. Akiva)')
        dat('the row konam_measure = %s' % data['konam_measure']['value'])
        return out('any amount — the vow forbids the object, not the act', ['vow_bound'])
    if ask == 'intimations':
        move('Nedarim 3b:4', 'the intimations ("handles" — a partial formula) from "lindor neder" or from "according to all that proceeds out of his mouth" — two sources')
        return out('the partial formula binds — two sources for one rule', ['vow_bound'])
    if ask == 'all_that_proceeds':
        ink('30:3', '"according to all that proceeds out of his mouth he shall do" — one seat, its echoes 32:24 (the next portion) and Judg 11:36')
        move('Rosh Hashanah 6a:5 (the baraita on Deut 23:24)', '"that which has gone out of your lips": a POSITIVE mitzva; "you shall keep": a PROHIBITION; "and do": the COURT\'S warrant to compel')
        return out('the vow\'s fulfilment — a positive duty, a prohibition, and the court\'s compulsion on one clause', ['commanded'])
    return out('no verdict in span', [FX.NONE])


# ===== F2: THE DAUGHTER (Num 30:4-6) ==========================================================================
def the_daughter(case, data):
    del P[:]
    ask = case['ask']
    if ask == 'in_her_youth':
        stage = case['stage']
        ink('30:4', '"and a woman, when she vows a vow to the LORD, and binds a bond IN HER FATHER\'S HOUSE IN HER YOUTH" — "in her youth" %s (computed)' % IN_HER_YOUTH)
        move('Sifrei 153:4', '"in her youth" — past minority, short of maturity: twelve years and a day; the mature daughter outside the father\'s power')
        move('Mishnah Nedarim 10:2, 11:10 (89b:2)', 'the father never annuls in her maturity; the Rabbis\' three whose vows stand — the mature, the orphan, the orphan in her father\'s lifetime')
        dat('the row vow_ages = %s' % data['vow_ages']['value'])
        if stage == 'minor':
            return out('a minor — no vow', ['exempt'])
        return out('in her youth — under her father' if stage == 'youth' else 'mature — her vow stands, no annuller', ['vow_bound'])
    if ask == 'fathers_domain':
        ink('30:4', '"in her father\'s house" — his DOMAIN')
        move('Sifrei 153:4; Nedarim 70a-70b', 'widowed or divorced from BETROTHAL she is still his; "in her youth in her father\'s house" — all her youth in his house: the widow of marriage excluded')
        return out('the father\'s domain — the betrothal\'s widow in, the marriage\'s out', ['accepted'])
    if ask == 'hearing_by_report':
        ink('30:5-6', '"and her father HEARS her vow" — "on the day of HIS HEARING" (30:6): the hearing by report counts (Sifrei 153:5)')
        move('Nedarim 72b:10', 'even R. Yoshiyah\'s steward never heard — hearing by report is no obstacle')
        return out('told by others — the hearing day opens', ['vow_confirmed'])
    if ask == 'the_deaf':
        ink('30:5', '"and her father hears" — the deaf excluded (Sifrei 153:5, 153:8)')
        move('Nedarim 73a:4 (Rava\'s baraita)', '"and her husband hears it" excludes the wife of a deaf man — the deaf cannot annul')
        dat('the row hearing_required = %s' % data['hearing_required']['value'])
        return out('the deaf hear nothing — no hearing day, no annulment', ['exempt'])
    if ask == 'intends_her':
        ink('30:5', '"and her father is silent TO HER" — the intended daughter (Sifrei 153:5: "I thought it was my wife\'s" — he may still annul)')
        move('Mishnah Nedarim 11:5 (86b:4-5); 87a:3-4', 'the wife\'s vow thought the daughter\'s, figs thought grapes — he must annul AGAIN; a specified wrong report voids the act')
        return out('the annulment void — the intended vow only; he annuls again', ['accepted'])
    if ask == 'confirmed_for_one_hour':
        ink('30:5', '"then all her vows SHALL STAND" — the stand-root twelve tokens in the chapter')
        move('Sifrei 153:5; Nedarim 79a:1', 'CONFIRMED FOR ONE HOUR, NEVER ANNULLED — silence confirms, silence does not annul; confirmed, he cannot annul')
        move('Nedarim 70a:4', 'the hour itself left open on the shelf ("and I" read as confirmed forever) — the day stands')
        return out('confirmed once, never annulled', ['vow_confirmed'])
    if ask == 'restraint_is_annulment':
        ink('30:6, 30:9', '"and if her father RESTRAIN her" — defined by the pair at 30:9 "he restrains her and ANNULS her vow" (the two verbs adjacent here alone, computed at index %s)' % RESTRAIN_ANNUL)
        move('Sifrei 153:6, 153:9; Nedarim 71b-72a', 'restraint is annulment; silence on the hearing day is as the vow\'s day')
        return out('restraint = annulment — the word defined by its pair', ['vow_annulled'])
    if ask == 'fathers_hearing_day':
        ink('30:6', '"on the day of his hearing" — the father\'s clock')
        move('Sifrei 153:6', 'the induction from the husband refused, the a-fortiori refused, and 30:17\'s LIKENING decides — "you are compelled to liken the father to the husband" (the hekkesh: the likening by juxtaposition)')
        return out('the father\'s day by the footer\'s likening', ['vow_annulled'])
    if ask == 'forgiveness':
        ink('30:6', '"and the LORD will forgive her, because her father restrained her" — the clause\'s %d seats all in this chapter (computed)' % len(FORGIVE))
        move('Sifrei 153:6; Kiddushin 81b:5; Nazir 23a:3', 'the woman who broke a vow her father annulled without her knowing — she needs forgiveness for the INTENT (the swine and the lamb); no lashes (Nedarim 83a:1)')
        return out('annulled unknown to her — forgiven for the intent, no lashes', ['vow_annulled'])
    if ask == 'caretaker':
        ink('30:6', '"BECAUSE HER FATHER RESTRAINED HER" — his act, not her assurance, not a caretaker\'s (Sifrei 153:6)')
        move('Bava Metzia 96a:20; Nazir 12b:3; Nedarim 72b:8-9', 'R. Yoshiyah: the husband alone (the doubled "her husband"); R. Yonatan: a man\'s agent is as himself')
        dat('the row annul_by_messenger = %s' % data['annul_by_messenger']['value'])
        return out('the act his own — the messenger a recorded dispute', ['accepted'])
    if ask == 'annulment_without_hearing':
        move('Nedarim 72b:3-73a:1', 'may he annul without hearing? every proof answered "when I hear it" — UNRESOLVED; the machine keeps the ink\'s trigger')
        dat('the row hearing_required = %s' % data['hearing_required']['value'])
        return out('unresolved on the shelf — the hearing the machine\'s trigger', ['accepted'])
    if ask == 'fathers_scope':
        move('Sifrei 155:1', '"I reasoned and reversed; the reversal fell and I merited the first reasoning" — and it too fails: 30:17 likens the father to the husband')
        dat('the row fathers_scope = %s' % data['fathers_scope']['value'])
        return out('the father as the husband by the likening — the reversed induction named', ['accepted'])
    if ask == 'fathers_rights':
        move('Ketubot 46b:6, 47a:6; Kiddushin 3b:7', '"in her youth, in her father\'s house" (30:17) — her gains and her betrothal money are her father\'s: the vows\' clause generalized (a taught transfer)')
        return out('the footer\'s clause carried to her gains — labeled', ['accepted'])
    if ask == 'heart_annuls':
        move('Nedarim 79a:1; 77b:7 (the houses)', 'annulled in his heart — NOT annulled; confirmed in his heart — confirmed; Beit Hillel: the heart suffices')
        dat('the row annulment_in_the_heart = %s' % data['annulment_in_the_heart']['value'])
        return out('the annulment an act — the heart\'s arm recorded', ['accepted'])
    return out('no verdict in span', [FX.NONE])


# ===== F3: THE BETROTHED (Num 30:7-9) =========================================================================
def the_betrothed(case, data):
    del P[:]
    ask = case['ask']
    if ask == 'joint_authority':
        by = set(case.get('by', []))
        ink('30:7-9', '"and if she be to a husband and her vows are upon her ... but if her husband disallow her on the day he hears" — the betrothed (R. Yoshiyah, Sifrei 153:7)')
        move('Mishnah Nedarim 10:1 (66b:10-67a:1); Rabba 67a:5; R. Yishmael\'s school 68a:1 from 30:17', 'her father AND her husband annul TOGETHER; one alone — not annulled; one confirming — needless to say')
        dat('the row betrothed_authority = %s' % data['betrothed_authority']['value'])
        return out('annulled — both together' if by == {'father', 'husband'} else 'not annulled — one alone', ['vow_annulled'] if by == {'father', 'husband'} else ['vow_bound'])
    if ask == 'be_she_shall_be':
        ink('30:7', '"and if she BE, SHE SHALL BE to a husband" — the doubled verb (its two Bible seats %s)' % BE_BE)
        move('Nedarim 67b:2; 70a:8 (Rabba); 70b:1', '"be" = betrothal; two beings = TWO BETROTHALS — the betrothed dies and the authority reverts to the father')
        return out('the doubled verb read as law — betrothal, and the second betrothal after the first\'s death', ['accepted'])
    if ask == 'fathers_death':
        move('Mishnah Nedarim 10:2; 70a:7 from 30:17', 'THE FATHER DIES — the authority does not pass to the betrothed: "in her youth, in her father\'s house" even after his death')
        return out('the father dead — the betrothed alone annuls nothing; the vow stands', ['vow_bound'])
    if ask == 'betrotheds_death':
        heard = case.get('husband', 'unheard')
        move('Mishnah Nedarim 10:2; 70a:8; the baraita 68a:5-68b:1', 'THE BETROTHED DIES — reversion to the father when he had not heard, or heard and was silent, or annulled and died THE SAME DAY; if he confirmed, or died silent THE NEXT DAY — the father cannot')
        if heard in ('unheard', 'silent_same_day', 'annulled_same_day'):
            return out('reverted to the father — he annuls alone', ['vow_annulled'])
        return out('confirmed before his death — the father cannot', ['vow_confirmed'])
    if ask == 'vows_carried':
        ink('30:7', '"and her vows are UPON HER" — the vows brought from the father\'s house (Sifrei 153:7); "upon her" superfluous (Nedarim 71a:3)')
        move('Nedarim 71a:2 (Shmuel); Mishnah Nedarim 10:3', 'the LAST betrothed annuls even vows disclosed to the first; betrothed a hundred times the same day — her father and her last husband annul')
        return out('the vows carried to the last betrothed — annulled with the father', ['vow_annulled'])
    if ask == 'share_or_weaken':
        move('Nedarim 69a:1-2, 71b:1', 'Beit Shammai: each severs HALF; Beit Hillel: the annulment WEAKENS the whole — the father annuls the whole again; the halakha (the ruling) as Beit Hillel')
        dat('the row share_or_weaken = %s' % data['share_or_weaken']['value'])
        return out('the joint annulment weakens, never severs', ['accepted'])
    if ask == 'fathers_confirmation':
        move('Nedarim 67b:4', 'the father\'s CONFIRMATION blocks — the betrothed can no longer annul')
        return out('one confirming — confirmed', ['vow_confirmed'])
    if ask == 'dissolved_confirmation':
        move('Nedarim 67a:4', 'one annulled, the other confirmed and had his confirmation dissolved by a sage — they must annul TOGETHER anew')
        return out('the dissolved confirmation does not revive the other\'s annulment', ['accepted'])
    if ask == 'utterance_is_oath':
        ink('30:7', '"or the UTTERANCE of her lips with which she bound her soul" — the noun\'s two seats %s (computed)' % UTTERANCE)
        move('CALLED cold_run_vayikra5.graded_offering(utterance_oath) -> %s / %s [IMPORT, live]' % (OATH_OPTION[0], OATH_NO_OPTION[0]), 'the utterance IS an oath — Lev 5:4 "to utter with the lips" (Sifrei 153:7; Shevuot 20a:4-9): the option template the oath\'s own')
        return out('the utterance of her lips = an oath — Leviticus 5:4 by call', ['accepted'])
    if ask == 'annul_in_advance':
        ink('30:9', '"and he annul her vow WHICH IS UPON HER" — the vows upon her, not those she will make (Sifrei 153:10)')
        move('Mishnah Nedarim 10:7 (75a:5); 75a:6', 'R. Eliezer: annulled in advance; the Rabbis: "confirm IT ... annul IT" — what came to confirmation came to annulment')
        dat('the row annul_in_advance = %s' % data['annul_in_advance']['value'])
        return out('"all vows you will vow are annulled" — nothing (the Rabbis)', ['vow_bound'])
    if ask == 'confirmation_and_annulment_reach':
        ink('30:14', '"her husband shall confirm IT, or her husband shall annul IT" — the two verbs with the one suffix %s (computed)' % (CONFIRM_ANNUL_IT,))
        move('Sifrei 153:10; Nedarim 75a:6, 76b:1', 'the parallel reach — what can come to confirmation can come to annulment, what cannot, cannot')
        return out('the two verbs one reach', ['accepted'])
    if ask == 'divorce_as':
        move('Nedarim 71b:2-72a:8', 'divorce after the hearing — as silence or as confirmation? every proof turned; UNRESOLVED')
        dat('the row divorce_as = %s' % data['divorce_as']['value'])
        return out('unresolved — the machine writes nothing at a divorce', ['accepted'])
    if ask == 'sustained_betrothed':
        move('Mishnah Nedarim 10:5 (73b:1); 73b:5 (Rav Pinchas in Rava\'s name)', 'the adult who waited twelve months — R. Eliezer: the husband annuls alone ("every woman vows on her husband\'s consent"); the Rabbis: not until she enters')
        dat('the row betrothed_authority = %s' % data['betrothed_authority']['value'])
        return out('the sustained betrothed — R. Eliezer\'s arm recorded; the Rabbis rule', ['accepted'])
    if ask == 'levirate_widow':
        move('Mishnah Nedarim 10:6 (74a:1-4); 74a:5-75a:3', 'R. Eliezer annuls; R. Yehoshua one brother; R. Akiva never — the bond not substantial, no stoning for her')
        dat('the row yavam_annuls = %s' % data['yavam_annuls']['value'])
        return out('the levirate widow — R. Akiva: no annulment', ['accepted'])
    if ask == 'two_wives':
        ink('30:9', '"he restrains HER" — the singular')
        move('Nedarim 73a:5-7 (R. Yehuda)', 'as "and he shall make HER drink" (5:27) is one woman, so "disallows HER" — not two wives at once (NS.sotah\'s two_at_once by reference)')
        return out('one wife at a time', ['accepted'])
    if ask == 'same_day_hundred':
        move('Mishnah Nedarim 10:3 (71a:1)', 'betrothed, vowed, divorced and betrothed again the same day, even to a hundred — her father and her LAST husband annul')
        return out('the last husband and the father annul', ['vow_annulled'])
    return out('no verdict in span', [FX.NONE])


# ===== F4: THE WIDOW AND THE DIVORCEE (Num 30:10) =============================================================
def the_widow(case, data):
    del P[:]
    ask = case['ask']
    if ask == 'from_marriage':
        ink('30:10', '"but the vow of a widow or of a divorced woman ... shall stand against her" — "a widow or a divorced woman" %s (computed)' % WIDOW_DIVORCEE)
        move('Sifrei 154:1; Ketubot 49a:2 (R. Yishmael\'s school)', 'from MARRIAGE, not from betrothal — as the mature daughter has wholly left the father\'s domain, so these: out of the father\'s and the husband\'s — who could annul?')
        return out('no annuller — the vow stands', ['vow_bound'])
    if ask == 'orphan_in_fathers_lifetime':
        move('Sifrei 154:1 (R. Akiva); Mishnah Nedarim 11:10; 89b:2 (Rav)', '"an orphan in her father\'s lifetime" — R. Yehuda\'s nine, the Rabbis\' THREE: the mature, the orphan, the orphan in her father\'s lifetime')
        return out('the orphan in her father\'s lifetime — her vows stand', ['vow_bound'])
    if ask == 'remarried':
        when = case['when']
        ink('30:11', '"and if in her husband\'s house she vowed" — in any event, even a forbidden marriage (Sifrei 154:1: the high priest\'s widow, the common priest\'s divorcee)')
        move('Mishnah Nedarim 11:9 (88b:7); 89a:1', 'the widow\'s "nazirite after thirty days" — married within, the new husband CANNOT annul; a vow made under him — he annuls')
        return out('vowed in widowhood — the new husband annuls nothing' if when == 'before' else 'vowed in his house — the husband annuls', ['vow_bound'] if when == 'before' else ['vow_annulled'])
    if ask == 'vow_timing':
        move('Nedarim 89a:2-5 (R. Yishmael / R. Akiva; Rav Chisda, Abaye)', 'the vow hung on MARRIAGE follows its taking effect (R. Yishmael), hung on DAYS its utterance; R. Akiva: the binding at widowhood')
        dat('the row widows_vow_timing = %s' % data['widows_vow_timing']['value'])
        return out('the authority at the vow\'s making — the marriage-hook the disputed arm', ['vow_bound'])
    if ask == 'once_out_one_hour':
        move('Mishnah Nedarim 11:9; Yevamot 87a:7', 'ONCE SHE LEFT TO HER OWN AUTHORITY ONE HOUR — vowed, divorced and taken back the same day: he cannot annul; handed to the husband\'s messengers and widowed on the way — out')
        return out('out one hour — the earlier vows beyond him', ['vow_bound'])
    if ask == 'priests_daughter_pair':
        ink('30:10, 30:4', '"a widow or a divorced woman" and "in her youth" — the priest\'s daughter\'s words at Lev 22:13 (the three Torah seats of the pair; computed)')
        move('CALLED cold_run_priesthood.holy_food(return) -> %s; (eating_table, after=fathers_house) -> %s [IMPORT, live]' % (PR_RETURN['v']['widow_and_divorcee'], PR_TABLE['v']), 'the priest\'s daughter returns to her father\'s bread; Yevamot 87a:6 — not to her father\'s POWER over vows (Rava, from 30:10)')
        return out('the pair of words shared — the return is for terumah, not for vows', ['accepted'])
    if ask == 'levirate':
        move('Mishnah Nedarim 10:6', 'the widow awaiting the brother-in-law — R. Akiva: he annuls nothing')
        dat('the row yavam_annuls = %s' % data['yavam_annuls']['value'])
        return out('awaiting the brother-in-law — her vow stands', ['vow_bound'])
    return out('no verdict in span', [FX.NONE])


# ===== F5: THE MARRIED WOMAN (Num 30:11-13) ====================================================================
def the_wife(case, data):
    del P[:]
    ask = case['ask']
    if ask == 'in_husbands_house':
        when = case['when']
        ink('30:11', '"and if in her husband\'s house she vowed" — "her husband\'s house" %s (computed); the married (30:7 having taken the betrothed — Sifrei 154:1)' % HUSBANDS_HOUSE)
        move('Nedarim 67b:1, 67b:6; Mishnah Nedarim 10:4', 'the husband annuls only vows made AFTER the marriage — not those before')
        return out('vowed before the marriage — beyond him' if when == 'before' else 'vowed in his house — he annuls', ['vow_bound'] if when == 'before' else ['vow_annulled'])
    if ask == 'scholars_practice':
        move('Mishnah Nedarim 10:4 (72b:1); 72b:4', 'the father before she leaves and the husband before she enters annul her vows in advance — "when I hear it": the practice prompts her to tell')
        return out('the advance annulment a conditional on the hearing', ['accepted'])
    if ask == 'two_silences':
        ink('30:12, 30:15', '"and was silent to her" (the single form at 30:5, 8, 12) against "silent, he is silent ... from day to day" (30:15 — %s)' % SILENT_SILENT)
        move('Sifrei 154:2, 156:1; Nedarim 79a:4-5, 79a:6', 'the silence to CONFIRM and the silence to VEX — both confirm ("superfluous verses are written about silence"); R. Chanina refuted')
        return out('both silences confirm at the day\'s end', ['vow_confirmed'])
    if ask == 'confirming_words':
        said = case['said']
        move('Nedarim 77b:5', '"you did well", "there is none like you", "had you not vowed I would have made you" — CONFIRMED; "I do not want you to vow", "this is no vow" — nothing')
        return out('confirmed by his words at once' if said == 'well_done' else 'nothing said — the day runs', ['vow_confirmed'] if said == 'well_done' else ['accepted'])
    if ask == 'all_the_day':
        move('Sifrei 154:2 (the Hebrew\'s close)', '"leave to annul all the day" — the married woman\'s verse')
        return out('leave to annul all the day', ['vow_annulled'])
    if ask == 'caretaker_excluded':
        ink('30:13', '"all that proceeds from her lips ... shall not stand" — to exclude the caretaker (Sifrei 154:3\'s lemma); "her husband has annulled them" — his act')
        dat('the row annul_by_messenger = %s' % data['annul_by_messenger']['value'])
        return out('the caretaker excluded — R. Yonatan\'s agent recorded', ['accepted'])
    if ask == 'sage_over_confirmation':
        move('Nedarim 69a:4, 79a:3 (R. Yochanan)', 'a sage dissolves a CONFIRMATION, not an ANNULMENT')
        dat('the row confirmation_dissolved = %s' % data['confirmation_dissolved']['value'])
        return out('the confirmation reopened by the sage; the annulment never', ['accepted'])
    if ask == 'confirmed_and_annulled':
        form = case['form']
        move('Nedarim 69b:3 (Rabba); 69b:1-2', '"confirmed and annulled" at once — nothing (what cannot be done in sequence is not done at once); "confirmed on condition the annulment holds" — annulled')
        return out('annulled — the condition carries it' if form == 'conditioned' else 'nothing — the two ops exclusive', ['vow_annulled'] if form == 'conditioned' else ['accepted'])
    if ask == 'mistaken_annulment':
        move('Mishnah Nedarim 11:5 (86b:4); 86b:5; 87a:3', 'the wife thought the daughter, the naziriteship thought an offering — he annuls AGAIN; a specified wrong report voids it')
        return out('the mistaken annulment void', ['accepted'])
    if ask == 'short_phrase':
        move('Nedarim 87a:5, 87a:8 (Rav Ashi; the halakha, the ruling)', 'within the time of a short phrase the act is open — except the blasphemer, the idolater, the betrother, the divorcer')
        return out('the retraction window of a short phrase — the vow and its annulment inside it', ['accepted'])
    if ask == 'her_and_i':
        who = case['who_first']
        move('CALLED cold_run_naso.nazirite(vow_form) -> %s [IMPORT, live]' % NAZ_SUB[0], 'the nazirite\'s vow annullable like a vow (Nedarim 3a:7)')
        move('Mishnah Nazir 4:1 (Nazir 20b:4)', 'he said "I am a nazirite" and she "and I" — he annuls hers, his stands; she first and he "and I" — he cannot (he would annul his own)')
        return out('her "and I" annulled' if who == 'husband' else 'his "and I" — he cannot annul hers', ['vow_annulled'] if who == 'husband' else ['vow_bound'])
    if ask == 'forgiveness_wife':
        ink('30:13', '"her husband has annulled them, and the LORD will forgive her" — the clause\'s third seat')
        move('Sifrei 154:3; Nazir 23a:3', 'as above — the woman who did not know')
        return out('forgiven — annulled unknown to her', ['vow_annulled'])
    if ask == 'annul_before_effect':
        move('Nedarim 89b:4-5 (R. Natan / the Rabbis); 90a:2', 'a conditional vow not yet in effect — R. Natan: he cannot annul; the Rabbis: he can ("He annuls the thoughts of the crafty")')
        dat('the row annul_before_effect = %s' % data['annul_before_effect']['value'])
        return out('annulled before it takes effect — the Rabbis', ['accepted'])
    if ask == 'consent_rationale':
        move('Nedarim 73b:5 (Rav Pinchas in Rava\'s name); 74a:9', 'EVERY WOMAN WHO VOWS, VOWS ON HER HUSBAND\'S CONSENT — he sustains her')
        return out('the husband\'s power explained by the sustenance', ['accepted'])
    if ask == 'divorce_except_vows':
        move('Gittin 85a:22; 73b:16', '"divorced except the annulment of your vows" — is the power intrinsic to marriage? a dilemma; the conditional bill keeps his power in the interval')
        return out('the power a marriage component — the severance question open', ['accepted'])
    return out('no verdict in span', [FX.NONE])


# ===== F6: THE AFFLICTION OATH AND THE DAY (Num 30:14-16) ===================================================
def the_affliction_oath(case, data):
    del P[:]
    ask = case['ask']
    if ask == 'the_filter':
        cls = case['content_class']
        ink('30:14, 30:17', '"every vow and every oath of binding TO AFFLICT A SOUL" (%s) restricts 30:9\'s "the vow upon her"; "between a man and his wife" (30:17, %s) adds the vows that touch him' % (AFFLICT, BETWEEN_MAN))
        move('Sifrei 155:1; Nedarim 79b:2; the baraita 81b:2', 'THE FOUR-CELL TABLE — affliction vows annulled whether between them or between her and others; non-affliction vows annulled only between him and her')
        move('Mishnah Nedarim 11:3-4', '"the property of people is konam to me" — not annulled; "I will not make for my father" — not; "for my father if I make for you" — annulled (11:11)')
        return out('annulled — affliction or between them' if cls in ('affliction', 'between') else 'not annulled — neither affliction nor between them', ['vow_annulled'] if cls in ('affliction', 'between') else ['vow_bound'])
    if ask == 'affliction_scope':
        what = case['what']
        move('Mishnah Nedarim 11:2 (79b:1); Sifrei 155:1 (R. Yonatan)', 'the produce of the WORLD — annulled; of this COUNTRY — not (he brings from another); of this STOREKEEPER — not, unless his sustenance is from him alone')
        move('Nedarim 82a:3, 82b:1 (Shmuel; Rav Huna)', 'the whole chapter R. Yosei\'s; Shmuel rules as the Rabbis — every affliction vow but one wholly between her and another')
        dat('the row affliction_scope = %s' % data['affliction_scope']['value'])
        return out('annulled' if what in ('world', 'sole_storekeeper') else 'not annulled — he supplies from elsewhere', ['vow_annulled'] if what in ('world', 'sole_storekeeper') else ['vow_bound'])
    if ask == 'bathing':
        move('Mishnah Nedarim 11:1; 81a:10 (Rav Adda b. Ahava / Rav Huna); 81b:2-3', '"if I bathe / do not bathe, adorn / do not adorn" — affliction (the Rabbis); not (R. Yosei) — annulled as between him and her (Rav Adda; the baraita: painting the eyes, rouge)')
        dat('the row affliction_scope = %s' % data['affliction_scope']['value'])
        return out('the bathe / adorn vows annulled — as affliction or as between them', ['vow_annulled'])
    if ask == 'two_afflictions':
        ink('30:14', '"to afflict a soul" — the infinitive\'s two Bible seats, Pharaoh\'s (Exod 10:3) and this (computed at the reading)')
        move('CALLED cold_run_moadim.yom_kippur() -> affliction_list %s [IMPORT, live]' % MO_AFFLICTION, 'Lev 23:27\'s afflictions — the five from the five mentions (Yoma 76a:11, 29:7 among them)')
        move('Nedarim 80b:6 (Rava)', 'Yom Kippur\'s affliction is felt NOW; the vows\' is what LEADS to affliction — one root, two senses read from each context')
        return out('one root, two senses — the vow\'s affliction is what leads to it', ['accepted'])
    if ask == 'annulment_reach':
        move('Nedarim 79b:5; 82a:1; 84a:2', 'affliction vows annulled for himself AND for others; between-them vows for himself only — "I am removed from the Jews": his part annulled, forbidden to all if divorced')
        dat('the row annulment_reach = %s' % data['annulment_reach']['value'])
        return out('two reaches — for others (affliction), for himself (between them)', ['accepted'])
    if ask == 'void_vow_owed_duty':
        move('Mishnah Nedarim 11:4 (85a:6); 81b:4', '"I will not make anything for YOU", "I will not make your bed" — no need to annul: it is VOID, she owes it')
        move('Mishnah Nedarim 11:4 (R. Akiva; R. Yochanan b. Nuri); Shmuel 85a:9; Rav Ashi 86b:1-2', 'annul it anyway — the excess (R. Akiva), lest he divorce her (b. Nuri — the halakha, the ruling); konamot break the lien')
        return out('no vow — she owes the work; annulled anyway for the excess or the divorce', ['exempt'])
    if ask == 'we_do_not_feed':
        move('Nedarim 81b:7-8 (Rav Kahana)', '"MY intercourse forbidden to you" — he compels her; "YOUR intercourse forbidden to me" — he must annul: we do not feed a person what is forbidden to him')
        return out('the self-prohibition annulled — the owed duty does not lift it', ['vow_annulled'])
    if ask == 'removed_from_the_jews':
        move('Mishnah Nedarim 11:12 (90b:5-6); 82a:1', '"I am removed from the Jews" — he annuls HIS PART; she is removed from all others if divorced — between him and her')
        return out('his part annulled — the between-them reach', ['vow_annulled'])
    if ask == 'fathers_reach':
        move('Sifrei 155:1', '"I reasoned and reversed" — the father likened to the husband by 30:17 (the third row ending on the footer)')
        dat('the row fathers_scope = %s' % data['fathers_scope']['value'])
        return out('the father\'s reach by the likening', ['accepted'])
    if ask == 'partial_annulment':
        act = case['act']
        ink('30:14', '"her husband shall confirm IT ... annul IT" — the two verbs with the one suffix %s (computed)' % (CONFIRM_ANNUL_IT,))
        move('Sifrei 155:1; Mishnah Nedarim 11:6 (87a:9); 87a:10; 87b:1-2', 'R. Yishmael: "figs and grapes" — confirmed for the figs, ALL confirmed; annulled for the figs, NOT till the grapes; R. Akiva: yakim MIMMENNU — a part annuls the whole; the Rabbis: no more than he annulled')
        dat('the row partial_annulment = %s' % data['partial_annulment']['value'])
        return out('confirmed for a part — all confirmed' if act == 'confirm_part' else 'annulled for a part — not annulled till the whole (R. Yishmael)', ['vow_confirmed'] if act == 'confirm_part' else ['vow_bound'])
    if ask == 'two_loaves':
        move('Nedarim 82b:2-3 (Shmuel / R. Yochanan)', 'one fine loaf (affliction) and one poor — Shmuel: both annulled; R. Yochanan: the afflicting one only')
        return out('the mixed vow — R. Yochanan: the afflicting loaf alone', ['accepted'])
    if ask == 'nazirite_whole':
        move('CALLED cold_run_naso.nazirite(vow_form, partial) -> %s [IMPORT, live]' % NAZ_PART[0], 'one prohibition named — a full nazirite')
        move('Nedarim 83a:3-6 (Rav Yosef; Abaye)', 'NAZIRITESHIP TAKES NO PARTIAL EFFECT — the annulment cancels the whole; a bird sin offering on the doubt')
        return out('her naziriteship annulled whole', ['vow_annulled'])
    if ask == 'the_deadline':
        ink('30:13, 30:15', '"on the day that he hears them" (%d seats, all here) against "from day to day" (%s)' % (len(DAY_OF_HEARING), DAY_TO_DAY))
        move('Sifrei 156:1; Nedarim 76b:4-8; Mishnah Nedarim 10:8', 'the whole day till dark (the first tanna) against the pair\'s twenty-four hours (R. Shimon ben Yochai in the Sifrei); each arm reads both clauses; R. Yehoshua b. Levi: the halakha (the ruling) is NOT as that pair')
        dat('the calendar row vow_annulment_window = %s (the other setting %s recorded)' % (WINDOW, [k for k in CAL_ROW['settings'] if k != WINDOW]))
        return out('to nightfall — the timer due the hearing day + 1; the twenty-four hours recorded', ['vow_confirmed'])
    if ask == 'day_leniency_stringency':
        move('Mishnah Nedarim 10:8 (76b:2-3)', 'vowed Friday night — annulled through the Sabbath till dark (the leniency); vowed near dark — till dark only (the stringency)')
        return out('the day ends at dark — a night and a day, or an hour', ['vow_confirmed'])
    if ask == 'silence_to_vex':
        move('Nedarim 78b:4-79a:9', 'R. Chanina: the vexing silence annuls ten days later — REFUTED three times (the deaths baraita; the near-dark vow; the day of learning)')
        return out('the vexing silence confirms at nightfall — the timer fires whatever the intent', ['vow_confirmed'])
    if ask == 'annul_on_sabbath':
        move('Mishnah Shabbat 24:5 (157a:5); Nedarim 77a:4; 77b:6', 'he annuls on the Sabbath even not for its need (by the whole-day arm); the formula "take and eat" with the heart\'s annulment')
        dat('the row annul_on_sabbath = %s' % data['annul_on_sabbath']['value'])
        return out('annulled on the Sabbath — "take and eat"', ['vow_annulled'])
    if ask == 'day_of_learning':
        move('Mishnah Nedarim 11:7 (87b:4)', '"I did not know there are annullers" — he annuls on the day he LEARNED; "I did not know this is a vow" — R. Meir no, the Rabbis yes')
        dat('the row hearing_of_the_law = %s' % data['hearing_of_the_law']['value'])
        return out('the day he learned — a second hearing day', ['vow_annulled'])
    if ask == 'after_his_hearing':
        ink('30:16', '"and if he annul, he annuls them AFTER HIS HEARING, then he shall bear her iniquity" — "after his hearing" %s; "annul, he annuls" %s (computed)' % (AFTER_HEARING, ANNUL_ANNUL))
        move('Sifrei 156:2', '"after his hearing" = after his CONFIRMING (freed by 30:15\'s neighbor) — he enters in her place for the sin')
        move('Nedarim 79a:4-5; Mishnah Nedarim 10:7', 'the husband who annuls a confirmed vow, so that she breaks it relying on him — he bears her iniquity')
        return out('annulled after the day — the vow stands, the husband bears her iniquity', ['iniquity_borne'])
    if ask == 'she_is_clear':
        ink('30:16, 5:31', '"he shall bear HER iniquity" — "her iniquity" five Torah seats, the suspected wife\'s among them (computed at the reading)')
        move('CALLED cold_run_naso.sotah(husband_clean) -> %s / %s [IMPORT, live]' % (SOTAH_CLEAN[0], SOTAH_UNCLEAN[0][:30]), '5:31 "the man shall be clear of iniquity and that woman shall bear her iniquity" — the phrase\'s first seat, the roles reversed here')
        move('Nedarim 83a:1', 'she who transgressed relying on his annulment incurs no lashes')
        return out('she is clear — the iniquity his', ['iniquity_borne'])
    if ask == 'measure_of_good':
        move('Sifrei 156:2; Sanhedrin 100a:17-18; Yoma 76a:7', 'if one who causes his fellow to stumble takes his place under the measure of PUNISHMENT, which is small, how much more under the measure of GOOD, which is great')
        dat('the row measure_of_good_ratio = %s' % data['measure_of_good_ratio']['value'])
        return out('the a-fortiori from the two measures — the ratio a recorded parameter', ['accepted'])
    if ask == 'oath_to_harm_himself':
        move('CALLED cold_run_vayikra5.graded_offering(utterance_oath, option) -> %s [IMPORT, live]' % OATH_OPTION[0], 'the option template "to do evil or to do good" — an oath to harm HIMSELF binds (Shevuot 27a:6); to harm others not (27a:7)')
        return out('the affliction oath the oath to harm oneself — bound', ['vow_bound'])
    if ask == 'vows_and_oaths_one_class':
        ink('30:14', '"EVERY VOW and EVERY OATH of binding" — the two words one class for the husband\'s power')
        move('Nedarim 80b:3-4 (Rav Yehuda; Rav Ashi)', '"these are the vows AND OATHS he annuls" — or oaths inside "vows" ("like the vows of the wicked" — a nazirite, an offering, an oath)')
        return out('vows and oaths one class for the annulment', ['accepted'])
    return out('no verdict in span', [FX.NONE])


# ===== F7: THE STATUTES (Num 30:17 and the chapter whole) ====================================================
def the_statutes(case, data):
    del P[:]
    ask = case['ask']
    if ask == 'likening_both_ways':
        ink('30:17', '"these are the statutes which the LORD commanded Moses, BETWEEN A MAN AND HIS WIFE, BETWEEN A FATHER AND HIS DAUGHTER" — %s, %s one seat each (computed)' % (BETWEEN_MAN, BETWEEN_FATHER))
        move('Sifrei 156:3; Nedarim 68a:1 (R. Yishmael\'s school)', 'the father likened to the husband and the husband to the father IN EVERY RULE STATED — the chapter\'s engine (four rows end on it); the betrothed\'s joint annulment from it')
        return out('the footer likens both ways — the engine of the chapter', ['accepted'])
    if ask == 'in_her_youth_her_fathers_house':
        ink('30:17', '"in her youth, her father\'s house" — "in her youth" %s (computed)' % IN_HER_YOUTH)
        move('Sifrei 156:3; Nedarim 70a:7', 'the father bounded to her youth in his house; the husband\'s power reaching past it; her father dead, she is still "in her father\'s house"')
        return out('the father\'s bound; the husband\'s reach', ['accepted'])
    if ask == 'fathers_gains':
        move('Ketubot 40b:4, 46b:6; Kiddushin 3b:7', 'the footer\'s clause for her gains and her betrothal money — a taught transfer')
        return out('the clause generalized — labeled', ['accepted'])
    if ask == 'the_receipt':
        ink('30:1', '"and Moses SAID to the children of Israel ACCORDING TO ALL that the LORD commanded Moses" — the formula\'s %d seats, this alone after a speech verb (computed); the register gate\'s finder read only "AS the LORD commanded" until this sitting' % len(RECEIPT2))
        move('THE REGISTER GATE (register_census.receipts, the second form)', 'the eleven seats of "according to ALL that the LORD commanded" joined the census; 30:1\'s class computed on the running world and declared from the print — the class of one (the 9b debt (v))')
        return out('the receipt that closes a speech — in the census by the finder\'s second form', ['accepted'])
    if ask == 'the_register_gate':
        ink('30:17', '"these are the statutes" — the footer (%s); its block (Lev 27:34, Num 30:17] holds the walk\'s daemons, law_vows the thirteenth' % FOOTER)
        return out('the footer DAEMONS — law_vows joined its block', ['accepted'])
    if ask == 'case_structure':
        ink('30:3-16', 'two "when" cases at %s and seven "and if" branches at %s; the chapter\'s other two "ki" are "because" (%s) — computed' % (WHEN, AND_IF, KI_SEATS[2:]))
        return out('two when, seven and-if — the draft\'s nine rows', ['accepted'])
    if ask == 'clock_words':
        ink('30:6-16', '"on the day of his hearing" %s; "from day to day" %s; "after his hearing" %s — computed' % (DAY_OF_HEARING, DAY_TO_DAY, AFTER_HEARING))
        return out('the clock the chapter\'s only number', ['accepted'])
    if ask == 'doubled_verbs':
        ink('30:3-16', 'five doubled verbs adjacent — %s; "annul, he annuls" %s, "be, she shall be" %s, "silent, he is silent" %s, "swear an oath" %s' % (DOUBLED, ANNUL_ANNUL, BE_BE, SILENT_SILENT, SWEAR_OATH))
        return out('five doubled verbs — every one read by the shelf as law', ['accepted'])
    if ask == 'the_line':
        ink('30:2-17', 'ONE line on the tape — Moses\' speech at the counter\'s day, no marker; the statutes commanded on israel')
        return out('the statutes of vows commanded — one write, no timer, no close', ['commanded'])
    if ask == 'installed_by':
        ink('30:2', 'no divine frame — the frame verbs %s both Moses\'' % FRAME_VERBS)
        move('THE LOOP step 3 (installation_parameters.yaml)', 'the installing acts erect institutions; Moses\' relay erects none and the chapter has no case (36:6\'s relay is a case-born output): BOOT with the class named — the second pass decides')
        return out('installed_by boot — a statute relayed in Moses\' voice, the class named', ['accepted'])
    if ask == 'all_generations':
        move('Bava Batra 120b:1 (Rav Ashi); Nedarim 78a:2', '"this is the thing" here and at Lev 17:2 — the vows\' law for all generations; the addressees Aaron, his sons and all Israel')
        return out('for all generations — the relay not case-bound', ['commanded'])
    if ask == 'placement_after_the_calendar':
        move('Nedarim 78a:9-11, 78b:2 (ben Azzai)', '"the festivals are stated, the vows\' portion not with them" — yet it stands NEXT to the festivals\' (28-29 then 30): the festivals need experts, the vows do not')
        return out('the chapter\'s placement read as law — next to the calendar, not of it', ['accepted'])
    if ask == 'two_kinds_of_ki':
        ink('30:3, 30:4, 30:6, 30:15', '"ki" as WHEN at the two case heads, as BECAUSE at 30:6 and 30:15 (computed: %s)' % KI_SEATS)
        return out('one particle, two jobs — the parse decides', ['accepted'])
    return out('no verdict in span', [FX.NONE])


# ---- THE WRAP — the daemon, the scene, the narrative ------------------------------------------------------
REQUIRED = {'man': set(), 'mature': set(), 'widow': set(), 'daughter': {'father'}, 'betrothed': {'father', 'husband'}, 'married': {'husband'}}   # the authority table (F2-F5): who annuls whom
def law_vows(event, world):
    """Num 30:1-17 (cold_run_vows.py F1-F7). installed_by boot — THE FORM FOR A LAW IN MOSES' VOICE (the class named in the registry):
    the ONE tape line writes the statutes commanded; THE STATE MACHINE on three case kinds — vow_uttered -> the DEBIT vow_bound toward
    HEAVEN; vow_heard -> the TIMER vow_confirmed due the hearing day + 1 (the calendar row's setting) or at once on the confirming words;
    vow_restrained on the day by the RIGHT authority -> the timer cancelled, the debit closed, HEAVEN forgives (vow_annulled); after the
    fire -> the vow stands and the annulling husband bears her iniquity; the wrong authority, the partial annulment (R. Yishmael's arm),
    the steward (R. Yoshiyah's arm) and the unheard vow write NOTHING — the vow stands."""
    k, src = event['kind'], event['case_source']
    E_ = lambda eff, s, cp=None, amount=None, due=None, law='', value=None: {'effect': eff, 'subject': s, 'counterparty': cp, 'amount': amount, 'due': due, 'value': value if value is not None else True, 'source_law': law, 'case_source': src}
    if k == 'vows_law_spoken':
        return [E_('commanded', 'israel', value='the statutes of vows — Num 30:2-17', law='F7 [INK 30:2 "this is the thing which the LORD commanded" ... 30:17 "these are the statutes which the LORD commanded Moses, between a man and his wife, between a father and his daughter" — Moses\' one speech to the heads of the tribes (%s), no divine frame; no timer, no close]' % event.get('to'))]
    if k == 'vow_uttered':
        vower, vow = event['vower'], event['vow']
        if event.get('age') is not None:
            v, e, _ = the_man({'ask': 'age', 'age': event['age'], 'sex': event.get('sex', 'girl'), 'knows_to_whom': event.get('knows_to_whom', True)}, DATA)
            if e == ['exempt']:
                return [E_('exempt', vower, value=v, law='F1 [%s]' % v)]
        if event.get('void'):
            return [E_('exempt', vower, value='a vow against an owed duty — void (Mishnah Nedarim 11:4)', law='F6 [INK 30:14 the vows he annuls — the owed work is not hers to forbid]')]
        return [E_('vow_bound', vower, cp='HEAVEN', value=vow, law='F1 [INK 30:3 "he shall not profane his word; according to all that proceeds out of his mouth he shall do" — the %s\'s %s (%s): the debit toward Heaven]' % (event.get('status', 'man'), event.get('vow_kind', 'vow'), event.get('content_class', 'other')))]
    if k == 'vow_heard':
        vower, vow = event['vower'], event['vow']
        if event.get('deaf'):
            return [E_('exempt', vower, value='the deaf cannot annul — the vow stands unheard', law='F2 [INK 30:5 "and her father hears" — the deaf excluded (Sifrei 153:5; Nedarim 73a:4)]')]
        if not event.get('intends_her', True):
            return []                                                          # "I thought it was my wife's" — no hearing of THIS vow: no clock (Sifrei 153:5; Mishnah Nedarim 11:5)
        if event.get('confirm_words'):
            return [E_('vow_confirmed', vower, value=vow, law='F5 [Nedarim 77b:5 "you did well" — confirmed by his words at once]')]
        return [E_('vow_confirmed', vower, value=vow, due=hearing_due(world), law='F6 [INK 30:5, 30:8 "and is silent to her, then all her vows shall stand" — THE TIMER: the hearing day + 1 (the calendar row vow_annulment_window = %s); the report counts (30:6 "on the day of his hearing")]' % WINDOW)]
    if k == 'vow_restrained':
        vower, vow, by = event['vower'], event['vow'], set(event.get('by', []))
        note = '%s — restrained by %s' % (src.split(' — ')[0], '+'.join(sorted(by)))
        ledger = world.entity(vower).ledger
        confirmed = any(e['effect'] == 'vow_confirmed' and e.get('value') == vow for e in ledger)
        pending = any(eff['effect'] == 'vow_confirmed' and eff.get('value') == vow and world._registry.get(eff['subject'], eff['subject']) == world._registry.get(vower, vower) for _, eff in world.timers)
        if confirmed:
            if 'husband' in by:
                return [E_('iniquity_borne', event.get('husband', vower + '-husband'), cp='HEAVEN', value=vow, law='F6 [INK 30:16 "and if he annul them after his hearing, then he shall bear her iniquity" — after the confirmation: the vow stands, the iniquity his (Sifrei 156:2)]')]
            return []                                                          # the father after the day: the ink names the husband alone — the vow stands, nothing written
        if not pending:
            return []                                                          # never heard: no clock to close — annulment without hearing UNRESOLVED (Nedarim 73a:1), the vow stands
        required = REQUIRED[event.get('status', 'man')]
        if not required or by != required:
            return []                                                          # the wrong authority (the father over the married; one of the two over the betrothed; any over the widow): the vow stands
        if event.get('status') == 'married' and event.get('content_class', 'other') not in ('affliction', 'between'):
            return []                                                          # THE FILTER (30:14 + 30:17): neither affliction nor between them — the vow stands
        if event.get('partial'):
            return []                                                          # R. Yishmael's arm (the Mishnah's): annulled for a part is not annulled until the whole
        if event.get('via_messenger'):
            return []                                                          # R. Yoshiyah's arm: the steward annuls nothing (the DATA row annul_by_messenger)
        world.cancel_timers(vower, 'vow_confirmed', note)
        world.close(vower, 'vow_bound', note, value=vow)
        return [E_('vow_annulled', vower, cp='HEAVEN', value=vow, law='F2 [INK 30:6 "and if her father restrain her on the day of his hearing ... and the LORD will forgive her" — the timer cancelled, the debit closed, Heaven forgives (30:9 restraint = annulment)]')]
    # ---- the exam's case kinds: each names LITERALLY every effect it can write (2b's form) ----
    if k == 'mans_vow_case':
        v, e, _ = the_man(dict(event, ask=event['ask']), DATA); L = 'F1 [%s]' % v; s_ = event['person']
        W = {'vow_bound': E_('vow_bound', s_, cp='HEAVEN', value=v, law=L), 'accepted': E_('accepted', s_, value=v, law=L), 'commanded': E_('commanded', s_, value=v, law=L), 'exempt': E_('exempt', s_, value=v, law=L)}
        return [W[x] for x in e if x != FX.NONE]
    if k == 'daughters_vow_case':
        v, e, _ = the_daughter(dict(event, ask=event['ask']), DATA); L = 'F2 [%s]' % v; s_ = event['person']
        W = {'vow_bound': E_('vow_bound', s_, cp='HEAVEN', value=v, law=L), 'vow_confirmed': E_('vow_confirmed', s_, value=v, law=L), 'vow_annulled': E_('vow_annulled', s_, cp='HEAVEN', value=v, law=L), 'accepted': E_('accepted', s_, value=v, law=L), 'exempt': E_('exempt', s_, value=v, law=L)}
        return [W[x] for x in e if x != FX.NONE]
    if k == 'betrothed_vow_case':
        v, e, _ = the_betrothed(dict(event, ask=event['ask']), DATA); L = 'F3 [%s]' % v; s_ = event['person']
        W = {'vow_bound': E_('vow_bound', s_, cp='HEAVEN', value=v, law=L), 'vow_confirmed': E_('vow_confirmed', s_, value=v, law=L), 'vow_annulled': E_('vow_annulled', s_, cp='HEAVEN', value=v, law=L), 'accepted': E_('accepted', s_, value=v, law=L), 'exempt': E_('exempt', s_, value=v, law=L)}
        return [W[x] for x in e if x != FX.NONE]
    if k == 'widows_vow_case':
        v, e, _ = the_widow(dict(event, ask=event['ask']), DATA); L = 'F4 [%s]' % v; s_ = event['person']
        W = {'vow_bound': E_('vow_bound', s_, cp='HEAVEN', value=v, law=L), 'accepted': E_('accepted', s_, value=v, law=L), 'exempt': E_('exempt', s_, value=v, law=L)}
        return [W[x] for x in e if x != FX.NONE]
    if k == 'wifes_vow_case':
        v, e, _ = the_wife(dict(event, ask=event['ask']), DATA); L = 'F5 [%s]' % v; s_ = event['person']
        W = {'vow_bound': E_('vow_bound', s_, cp='HEAVEN', value=v, law=L), 'vow_confirmed': E_('vow_confirmed', s_, value=v, law=L), 'vow_annulled': E_('vow_annulled', s_, cp='HEAVEN', value=v, law=L), 'accepted': E_('accepted', s_, value=v, law=L), 'exempt': E_('exempt', s_, value=v, law=L)}
        return [W[x] for x in e if x != FX.NONE]
    if k == 'affliction_oath_case':
        v, e, _ = the_affliction_oath(dict(event, ask=event['ask']), DATA); L = 'F6 [%s]' % v; s_ = event['person']
        W = {'vow_bound': E_('vow_bound', s_, cp='HEAVEN', value=v, law=L), 'vow_confirmed': E_('vow_confirmed', s_, value=v, law=L), 'vow_annulled': E_('vow_annulled', s_, cp='HEAVEN', value=v, law=L), 'iniquity_borne': E_('iniquity_borne', s_, cp='HEAVEN', value=v, law=L), 'accepted': E_('accepted', s_, value=v, law=L), 'exempt': E_('exempt', s_, value=v, law=L)}
        return [W[x] for x in e if x != FX.NONE]
    if k == 'statutes_case':
        v, e, _ = the_statutes(dict(event, ask=event['ask']), DATA); L = 'F7 [%s]' % v; s_ = event['person']
        W = {'accepted': E_('accepted', s_, value=v, law=L), 'commanded': E_('commanded', s_, value=v, law=L), 'exempt': E_('exempt', s_, value=v, law=L)}
        return [W[x] for x in e if x != FX.NONE]
    return []


LINE = 'Num 30:2-17 — and Moses spoke to the heads of the tribes of the children of Israel, saying: this is the thing which the LORD commanded: a man, when he vows a vow to the LORD, or swears an oath to bind a bond on his soul, he shall not profane his word ... these are the statutes which the LORD commanded Moses, between a man and his wife, between a father and his daughter, in her youth in her father\'s house'
CLOSE = 'none — the statutes commanded; the vows themselves are the bench\'s (no vow is uttered on the tape in this chapter)'


def scene():
    """THE SCENE — the exam's rows replayed on the world engine (the exodus epoch): THE STATE MACHINE's persons through vow_uttered /
    vow_heard / vow_restrained with the clock advanced one day to fire the pending confirmations, then the seven case kinds on the exam's persons."""
    with contextlib.redirect_stdout(io.StringIO()):
        w = WE.World(era='Num 30:1-17: Mishnah Nedarim 9-11, Niddah 5:6, Shabbat 24:5 on the engine (the exodus epoch)', epoch='exodus')
        w.laws = [law_vows]
        w.advance(w.clock.day_in('exodus', 40, 6, 1))
        # ---- THE STATE MACHINE (LITERAL submits — the daemon gate parses no loop) ----
        w.submit({'kind': 'vow_uttered', 'subject': 'the-man', 'vower': 'the-man', 'vow': 'the-man:olah-upon-me', 'status': 'man', 'vow_kind': 'vow', 'case_source': 'Num 30:3 — a man vows a burnt offering upon himself (Rosh Hashanah 6a:12)'})
        w.submit({'kind': 'vow_uttered', 'subject': 'the-minor', 'vower': 'the-minor', 'vow': 'the-minor:konam', 'status': 'daughter', 'age': 10, 'sex': 'girl', 'case_source': 'Mishnah Niddah 5:6 — a girl of ten vows: no vow'})
        w.submit({'kind': 'vow_uttered', 'subject': 'the-examined-girl', 'vower': 'the-examined-girl', 'vow': 'the-examined-girl:konam', 'status': 'daughter', 'age': 11, 'sex': 'girl', 'knows_to_whom': True, 'case_source': 'Mishnah Niddah 5:6 — a girl of eleven and a day who knows in Whose name: bound'})
        w.submit({'kind': 'vow_uttered', 'subject': 'the-examined-boy', 'vower': 'the-examined-boy', 'vow': 'the-examined-boy:konam', 'status': 'man', 'age': 12, 'sex': 'boy', 'knows_to_whom': False, 'case_source': 'Mishnah Niddah 5:6 — a boy of twelve and a day who does not know: no vow'})
        w.submit({'kind': 'vow_uttered', 'subject': 'the-daughter', 'vower': 'the-daughter', 'vow': 'the-daughter:konam-figs', 'status': 'daughter', 'content_class': 'other', 'case_source': 'Num 30:4 — a daughter in her youth in her father\'s house vows'})
        w.submit({'kind': 'vow_heard', 'subject': 'the-father', 'vower': 'the-daughter', 'vow': 'the-daughter:konam-figs', 'by': ['father'], 'silent': True, 'case_source': 'Num 30:5 — her father hears and is silent: the hearing day opens'})
        w.submit({'kind': 'vow_restrained', 'subject': 'the-father', 'vower': 'the-daughter', 'vow': 'the-daughter:konam-figs', 'by': ['father'], 'status': 'daughter', 'content_class': 'other', 'case_source': 'Num 30:6 — her father restrains her on the day of his hearing: annulled, the LORD forgives her'})
        w.submit({'kind': 'vow_uttered', 'subject': 'the-daughter-silent', 'vower': 'the-daughter-silent', 'vow': 'the-daughter-silent:konam', 'status': 'daughter', 'content_class': 'other', 'case_source': 'Num 30:4 — a second daughter vows'})
        w.submit({'kind': 'vow_heard', 'subject': 'the-father-silent', 'vower': 'the-daughter-silent', 'vow': 'the-daughter-silent:konam', 'by': ['father'], 'silent': True, 'case_source': 'Num 30:5 — her father hears and stays silent past the day'})
        w.submit({'kind': 'vow_uttered', 'subject': 'the-betrothed', 'vower': 'the-betrothed', 'vow': 'the-betrothed:konam', 'status': 'betrothed', 'content_class': 'other', 'case_source': 'Num 30:7 — a betrothed maiden vows (Mishnah Nedarim 10:1)'})
        w.submit({'kind': 'vow_heard', 'subject': 'the-betrothed-father', 'vower': 'the-betrothed', 'vow': 'the-betrothed:konam', 'by': ['father', 'husband'], 'silent': True, 'case_source': 'Num 30:8 — her father and her husband hear'})
        w.submit({'kind': 'vow_restrained', 'subject': 'the-betrothed-father', 'vower': 'the-betrothed', 'vow': 'the-betrothed:konam', 'by': ['father'], 'status': 'betrothed', 'content_class': 'other', 'case_source': 'Mishnah Nedarim 10:1 — the father annulled and not the husband: not annulled'})
        w.submit({'kind': 'vow_restrained', 'subject': 'the-betrothed-father', 'vower': 'the-betrothed', 'vow': 'the-betrothed:konam', 'by': ['father', 'husband'], 'status': 'betrothed', 'content_class': 'other', 'case_source': 'Mishnah Nedarim 10:1 — her father and her husband annul together: annulled'})
        w.submit({'kind': 'vow_uttered', 'subject': 'the-widow', 'vower': 'the-widow', 'vow': 'the-widow:nazirite-after-thirty', 'status': 'widow', 'content_class': 'affliction', 'case_source': 'Num 30:10 — a widow vows (Mishnah Nedarim 11:9)'})
        w.submit({'kind': 'vow_restrained', 'subject': 'the-new-husband', 'vower': 'the-widow', 'vow': 'the-widow:nazirite-after-thirty', 'by': ['husband'], 'status': 'widow', 'content_class': 'affliction', 'case_source': 'Mishnah Nedarim 11:9 — married within the thirty days, the new husband cannot annul'})
        w.submit({'kind': 'vow_uttered', 'subject': 'the-wife-affliction', 'vower': 'the-wife-affliction', 'vow': 'the-wife-affliction:konam-produce-of-the-world', 'status': 'married', 'content_class': 'affliction', 'case_source': 'Num 30:11, 30:14 — a married woman vows off the produce of the world (Mishnah Nedarim 11:2)'})
        w.submit({'kind': 'vow_heard', 'subject': 'the-husband-affliction', 'vower': 'the-wife-affliction', 'vow': 'the-wife-affliction:konam-produce-of-the-world', 'by': ['husband'], 'silent': True, 'case_source': 'Num 30:12 — her husband hears'})
        w.submit({'kind': 'vow_restrained', 'subject': 'the-husband-affliction', 'vower': 'the-wife-affliction', 'vow': 'the-wife-affliction:konam-produce-of-the-world', 'by': ['husband'], 'status': 'married', 'content_class': 'affliction', 'case_source': 'Num 30:13 — her husband annuls on the day: annulled, the LORD forgives her'})
        w.submit({'kind': 'vow_uttered', 'subject': 'the-wife-other', 'vower': 'the-wife-other', 'vow': 'the-wife-other:konam-my-fathers-work', 'status': 'married', 'content_class': 'other', 'case_source': 'Mishnah Nedarim 11:4 — "I will not make anything for my father" — neither affliction nor between them'})
        w.submit({'kind': 'vow_heard', 'subject': 'the-husband-other', 'vower': 'the-wife-other', 'vow': 'the-wife-other:konam-my-fathers-work', 'by': ['husband'], 'silent': True, 'case_source': 'Num 30:12 — her husband hears'})
        w.submit({'kind': 'vow_restrained', 'subject': 'the-husband-other', 'vower': 'the-wife-other', 'vow': 'the-wife-other:konam-my-fathers-work', 'by': ['husband'], 'status': 'married', 'content_class': 'other', 'case_source': 'Mishnah Nedarim 11:4 — he cannot annul: the filter of 30:14 and 30:17'})
        w.submit({'kind': 'vow_uttered', 'subject': 'the-wife-after', 'vower': 'the-wife-after', 'vow': 'the-wife-after:konam-bathing', 'status': 'married', 'content_class': 'affliction', 'case_source': 'Num 30:14 — an affliction oath (Mishnah Nedarim 11:1)'})
        w.submit({'kind': 'vow_heard', 'subject': 'the-husband-after', 'vower': 'the-wife-after', 'vow': 'the-wife-after:konam-bathing', 'by': ['husband'], 'silent': True, 'case_source': 'Num 30:15 — her husband is silent from day to day'})
        w.submit({'kind': 'vow_uttered', 'subject': 'the-deaf-wife', 'vower': 'the-deaf-wife', 'vow': 'the-deaf-wife:konam', 'status': 'married', 'content_class': 'affliction', 'case_source': 'Nedarim 73a:4 — the wife of a deaf man vows'})
        w.submit({'kind': 'vow_heard', 'subject': 'the-deaf-husband', 'vower': 'the-deaf-wife', 'vow': 'the-deaf-wife:konam', 'by': ['husband'], 'deaf': True, 'case_source': 'Nedarim 73a:4 — "and her husband hears it" excludes the deaf: no hearing'})
        w.submit({'kind': 'vow_uttered', 'subject': 'the-wife-well-done', 'vower': 'the-wife-well-done', 'vow': 'the-wife-well-done:konam', 'status': 'married', 'content_class': 'affliction', 'case_source': 'Nedarim 77b:5 — she vows'})
        w.submit({'kind': 'vow_heard', 'subject': 'the-husband-well-done', 'vower': 'the-wife-well-done', 'vow': 'the-wife-well-done:konam', 'by': ['husband'], 'confirm_words': True, 'case_source': 'Nedarim 77b:5 — "you did well": confirmed by his words'})
        w.submit({'kind': 'vow_restrained', 'subject': 'the-husband-well-done', 'vower': 'the-wife-well-done', 'vow': 'the-wife-well-done:konam', 'by': ['husband'], 'husband': 'the-husband-well-done', 'status': 'married', 'content_class': 'affliction', 'case_source': 'Num 30:16 — he annuls after confirming: he bears her iniquity'})
        w.submit({'kind': 'vow_uttered', 'subject': 'the-wife-mistaken', 'vower': 'the-wife-mistaken', 'vow': 'the-wife-mistaken:konam', 'status': 'married', 'content_class': 'affliction', 'case_source': 'Mishnah Nedarim 11:5 — the wife vows'})
        w.submit({'kind': 'vow_heard', 'subject': 'the-husband-mistaken', 'vower': 'the-wife-mistaken', 'vow': 'the-wife-mistaken:konam', 'by': ['husband'], 'silent': True, 'intends_her': False, 'case_source': 'Mishnah Nedarim 11:5 — he thought it was his daughter\'s: no hearing of this vow'})
        w.submit({'kind': 'vow_uttered', 'subject': 'the-wife-partial', 'vower': 'the-wife-partial', 'vow': 'the-wife-partial:konam-figs-and-grapes', 'status': 'married', 'content_class': 'affliction', 'case_source': 'Mishnah Nedarim 11:6 — "figs and grapes are konam to me"'})
        w.submit({'kind': 'vow_heard', 'subject': 'the-husband-partial', 'vower': 'the-wife-partial', 'vow': 'the-wife-partial:konam-figs-and-grapes', 'by': ['husband'], 'silent': True, 'case_source': 'Num 30:12 — her husband hears'})
        w.submit({'kind': 'vow_restrained', 'subject': 'the-husband-partial', 'vower': 'the-wife-partial', 'vow': 'the-wife-partial:konam-figs-and-grapes', 'by': ['husband'], 'status': 'married', 'content_class': 'affliction', 'partial': True, 'case_source': 'Mishnah Nedarim 11:6 — annulled for the figs alone: not annulled till the grapes (R. Yishmael)'})
        w.submit({'kind': 'vow_uttered', 'subject': 'the-wife-steward', 'vower': 'the-wife-steward', 'vow': 'the-wife-steward:konam', 'status': 'married', 'content_class': 'affliction', 'case_source': 'Nedarim 72b:8 — the wife vows while the husband is away'})
        w.submit({'kind': 'vow_heard', 'subject': 'the-steward', 'vower': 'the-wife-steward', 'vow': 'the-wife-steward:konam', 'by': ['husband'], 'silent': True, 'report': True, 'case_source': 'Nedarim 72b:10 — the report reaches the household'})
        w.submit({'kind': 'vow_restrained', 'subject': 'the-steward', 'vower': 'the-wife-steward', 'vow': 'the-wife-steward:konam', 'by': ['husband'], 'status': 'married', 'content_class': 'affliction', 'via_messenger': True, 'case_source': 'Nedarim 72b:8 — the steward annuls in his stead: nothing (R. Yoshiyah)'})
        w.submit({'kind': 'vow_uttered', 'subject': 'the-void-vow', 'vower': 'the-void-vow', 'vow': 'the-void-vow:konam-your-bed', 'status': 'married', 'content_class': 'between', 'void': True, 'case_source': 'Nedarim 81b:4 — "I will not make your bed": void, she owes it'})
        w.advance(w.clock.day + 1)                                             # THE HEARING DAY ENDS: the pending confirmations fire at the evening boundary
        w.submit({'kind': 'vow_restrained', 'subject': 'the-father-silent', 'vower': 'the-daughter-silent', 'vow': 'the-daughter-silent:konam', 'by': ['father'], 'status': 'daughter', 'content_class': 'other', 'case_source': 'Sifrei 153:5 — confirmed for one hour, never annulled: the father after the day annuls nothing'})
        w.submit({'kind': 'vow_restrained', 'subject': 'the-husband-after', 'vower': 'the-wife-after', 'vow': 'the-wife-after:konam-bathing', 'by': ['husband'], 'husband': 'the-husband-after', 'status': 'married', 'content_class': 'affliction', 'case_source': 'Num 30:16 — he annuls them after his hearing: he shall bear her iniquity'})
        # ---- the exam's persons through the seven case kinds ----
        w.submit({'kind': 'mans_vow_case', 'subject': 'the-frame', 'person': 'the-frame', 'ask': 'frame', 'case_source': 'Num 30:2 — the exam\'s row frame'})
        w.submit({'kind': 'mans_vow_case', 'subject': 'the-two-offices', 'person': 'the-two-offices', 'ask': 'this_is_the_thing', 'case_source': 'Nedarim 77b:8 — the exam\'s row this_is_the_thing'})
        w.submit({'kind': 'mans_vow_case', 'subject': 'the-expert', 'person': 'the-expert', 'ask': 'heads_of_the_tribes', 'case_source': 'Nedarim 78b:3 — the exam\'s row heads_of_the_tribes'})
        w.submit({'kind': 'mans_vow_case', 'subject': 'the-vower-of-carrion', 'person': 'the-vower-of-carrion', 'ask': 'vow_support', 'base': 'torah_forbidden', 'case_source': 'Mishnah Nedarim 2:1 — the exam\'s row vow_support (a Torah-forbidden base)'})
        w.submit({'kind': 'mans_vow_case', 'subject': 'the-delayer', 'person': 'the-delayer', 'ask': 'two_transgressions', 'case_source': 'Nedarim 3a:7 — the exam\'s row two_transgressions'})
        w.submit({'kind': 'mans_vow_case', 'subject': 'the-slave', 'person': 'the-slave', 'ask': 'on_his_soul', 'case_source': 'Nazir 61a:8 — the exam\'s row on_his_soul'})
        w.submit({'kind': 'daughters_vow_case', 'subject': 'the-mature-daughter', 'person': 'the-mature-daughter', 'ask': 'in_her_youth', 'stage': 'mature', 'case_source': 'Mishnah Nedarim 11:10 — the exam\'s row in_her_youth (mature)'})
        w.submit({'kind': 'daughters_vow_case', 'subject': 'the-deaf-father', 'person': 'the-deaf-father', 'ask': 'the_deaf', 'case_source': 'Nedarim 73a:4 — the exam\'s row the_deaf'})
        w.submit({'kind': 'daughters_vow_case', 'subject': 'the-forgiven-daughter', 'person': 'the-forgiven-daughter', 'ask': 'forgiveness', 'case_source': 'Kiddushin 81b:5 — the exam\'s row forgiveness'})
        w.submit({'kind': 'daughters_vow_case', 'subject': 'the-confirmed-hour', 'person': 'the-confirmed-hour', 'ask': 'confirmed_for_one_hour', 'case_source': 'Sifrei 153:5 — the exam\'s row confirmed_for_one_hour'})
        w.submit({'kind': 'betrothed_vow_case', 'subject': 'the-joint-annullers', 'person': 'the-joint-annullers', 'ask': 'joint_authority', 'by': ['father', 'husband'], 'case_source': 'Mishnah Nedarim 10:1 — the exam\'s row joint_authority'})
        w.submit({'kind': 'betrothed_vow_case', 'subject': 'the-orphaned-betrothed', 'person': 'the-orphaned-betrothed', 'ask': 'fathers_death', 'case_source': 'Mishnah Nedarim 10:2 — the exam\'s row fathers_death'})
        w.submit({'kind': 'betrothed_vow_case', 'subject': 'the-advance-annuller', 'person': 'the-advance-annuller', 'ask': 'annul_in_advance', 'case_source': 'Mishnah Nedarim 10:7 — the exam\'s row annul_in_advance'})
        w.submit({'kind': 'betrothed_vow_case', 'subject': 'the-utterer', 'person': 'the-utterer', 'ask': 'utterance_is_oath', 'case_source': 'Shevuot 20a:4 — the exam\'s row utterance_is_oath'})
        w.submit({'kind': 'widows_vow_case', 'subject': 'the-widow-of-marriage', 'person': 'the-widow-of-marriage', 'ask': 'from_marriage', 'case_source': 'Sifrei 154:1 — the exam\'s row from_marriage'})
        w.submit({'kind': 'widows_vow_case', 'subject': 'the-priests-daughter', 'person': 'the-priests-daughter', 'ask': 'priests_daughter_pair', 'case_source': 'Yevamot 87a:6 — the exam\'s row priests_daughter_pair'})
        w.submit({'kind': 'wifes_vow_case', 'subject': 'the-earlier-vow', 'person': 'the-earlier-vow', 'ask': 'in_husbands_house', 'when': 'before', 'case_source': 'Nedarim 67b:1 — the exam\'s row in_husbands_house (before)'})
        w.submit({'kind': 'wifes_vow_case', 'subject': 'the-two-silences', 'person': 'the-two-silences', 'ask': 'two_silences', 'case_source': 'Nedarim 79a:5 — the exam\'s row two_silences'})
        w.submit({'kind': 'wifes_vow_case', 'subject': 'the-nazirite-wife', 'person': 'the-nazirite-wife', 'ask': 'her_and_i', 'who_first': 'husband', 'case_source': 'Mishnah Nazir 4:1 — the exam\'s row her_and_i'})
        w.submit({'kind': 'affliction_oath_case', 'subject': 'the-storekeeper-vow', 'person': 'the-storekeeper-vow', 'ask': 'affliction_scope', 'what': 'storekeeper', 'case_source': 'Mishnah Nedarim 11:2 — the exam\'s row affliction_scope (this storekeeper)'})
        w.submit({'kind': 'affliction_oath_case', 'subject': 'the-deadline', 'person': 'the-deadline', 'ask': 'the_deadline', 'case_source': 'Nedarim 76b:4-8 — the exam\'s row the_deadline'})
        w.submit({'kind': 'affliction_oath_case', 'subject': 'the-late-annuller', 'person': 'the-late-annuller', 'ask': 'after_his_hearing', 'case_source': 'Nedarim 79a:4 — the exam\'s row after_his_hearing'})
        w.submit({'kind': 'affliction_oath_case', 'subject': 'the-sabbath-annuller', 'person': 'the-sabbath-annuller', 'ask': 'annul_on_sabbath', 'case_source': 'Mishnah Shabbat 24:5 — the exam\'s row annul_on_sabbath'})
        w.submit({'kind': 'affliction_oath_case', 'subject': 'the-bed-vow', 'person': 'the-bed-vow', 'ask': 'void_vow_owed_duty', 'case_source': 'Nedarim 81b:4 — the exam\'s row void_vow_owed_duty'})
        w.submit({'kind': 'statutes_case', 'subject': 'the-likening', 'person': 'the-likening', 'ask': 'likening_both_ways', 'case_source': 'Sifrei 156:3 — the exam\'s row likening_both_ways'})
        w.submit({'kind': 'statutes_case', 'subject': 'the-receipt', 'person': 'the-receipt', 'ask': 'the_receipt', 'case_source': 'Num 30:1 — the exam\'s row the_receipt'})
        w.submit({'kind': 'statutes_case', 'subject': 'the-generations', 'person': 'the-generations', 'ask': 'all_generations', 'case_source': 'Bava Batra 120b:1 — the exam\'s row all_generations'})
    n = lambda eid, eff: len([e for e in w.entity(eid).ledger if e['effect'] == eff])
    closed = lambda eid: len([e for e in w.entity(eid).ledger if e['effect'] == 'vow_bound' and not e.get('open')])
    tset = len([l for l in w.log if l[0] == 'TIMER-SET']); tfire = len([l for l in w.log if l[0] == 'TIMER-FIRE']); tcan = len([l for l in w.log if l[0] == 'TIMER-CANCEL'])
    return ((n('the-man', 'vow_bound'), n('the-minor', 'exempt'), n('the-examined-girl', 'vow_bound'), n('the-examined-boy', 'exempt'),
             n('the-daughter', 'vow_annulled'), closed('the-daughter'), n('the-daughter-silent', 'vow_confirmed'), n('the-daughter-silent', 'vow_annulled'), closed('the-daughter-silent'),
             n('the-betrothed', 'vow_annulled'), closed('the-betrothed'), n('the-widow', 'vow_annulled'), closed('the-widow'),
             n('the-wife-affliction', 'vow_annulled'), closed('the-wife-affliction'), n('the-wife-other', 'vow_annulled'), n('the-wife-other', 'vow_confirmed'),
             n('the-wife-after', 'vow_confirmed'), n('the-wife-after', 'vow_annulled'), n('the-husband-after', 'iniquity_borne'),
             n('the-deaf-wife', 'exempt'), n('the-deaf-wife', 'vow_confirmed'), n('the-wife-well-done', 'vow_confirmed'), n('the-husband-well-done', 'iniquity_borne'),
             n('the-wife-mistaken', 'vow_confirmed'), n('the-wife-partial', 'vow_confirmed'), n('the-wife-partial', 'vow_annulled'), n('the-wife-steward', 'vow_confirmed'), n('the-wife-steward', 'vow_annulled'),
             n('the-void-vow', 'exempt'), n('the-void-vow', 'vow_bound')),
            (tset, tfire, tcan, len(w.timers)),
            (n('the-frame', 'commanded'), n('the-two-offices', 'accepted'), n('the-expert', 'accepted'), n('the-vower-of-carrion', 'exempt'), n('the-delayer', 'commanded'), n('the-slave', 'exempt'),
             n('the-mature-daughter', 'vow_bound'), n('the-deaf-father', 'exempt'), n('the-forgiven-daughter', 'vow_annulled'), n('the-confirmed-hour', 'vow_confirmed'),
             n('the-joint-annullers', 'vow_annulled'), n('the-orphaned-betrothed', 'vow_bound'), n('the-advance-annuller', 'vow_bound'), n('the-utterer', 'accepted'),
             n('the-widow-of-marriage', 'vow_bound'), n('the-priests-daughter', 'accepted'), n('the-earlier-vow', 'vow_bound'), n('the-two-silences', 'vow_confirmed'), n('the-nazirite-wife', 'vow_annulled'),
             n('the-storekeeper-vow', 'vow_bound'), n('the-deadline', 'vow_confirmed'), n('the-late-annuller', 'iniquity_borne'), n('the-sabbath-annuller', 'vow_annulled'), n('the-bed-vow', 'exempt'),
             n('the-likening', 'accepted'), n('the-receipt', 'accepted'), n('the-generations', 'commanded')),
            len(w.entities)), w
SCENE, _W = scene()
# THE PREDICTION (typed before the first run, NUMBERS_WALK.md "Sitting 10b" — the state machine's arithmetic): the man bound, the minor and the unknowing boy exempt,
# the examined girl bound; the daughter annulled with her debit CLOSED; the silent daughter confirmed by the fire, never annulled, the debit open; the betrothed annulled by
# the pair (the father alone wrote nothing) with the debit closed; the widow untouched; the affliction wife annulled and closed; the other-class wife not annulled and confirmed
# by the fire; the wife-after confirmed by the fire, not annulled, her husband bears the iniquity; the deaf-wife exempt, no confirmation; the well-done wife confirmed at once,
# her husband bears; the mistaken hearing no confirmation; the partial and the steward's wives confirmed by the fire, not annulled; the void vow exempt, no debit.
# TIMERS: set 8 (the daughter, the silent daughter, the betrothed, the affliction wife, the other-class wife, the wife-after, the partial, the steward), fired 5 (the silent
# daughter, the other-class, the wife-after, the partial, the steward), cancelled 3 (the daughter, the betrothed, the affliction wife), pending 0. ENTITIES: the machine's
# 19 persons written on + the exam's 27 = 46.
SCENE_PREDICTED = ((1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 0, 1, 0, 1, 0), (8, 5, 3, 0),
                   (1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1), 46)


def narrative():
    """THE NUMBERS WALK 10b (2026-09-12): the portion's own act AS HISTORY — the ONE line of 30:2-17 at the counter's day (40, 6, 1), page-order
    after the calendar's line (28:1-29:39), on a world with this runner's daemon: ONE write (the statutes commanded on israel), no timer, no
    marker, no entity but israel. Recorded by the sequential run's recorder and stitched onto the tape. Not a graded cell: the tuple below is
    a tripwire typed from the design; the sequence world's RUN tuple and CV1-CV9 grade the tape."""
    with contextlib.redirect_stdout(io.StringIO()):
        w = WE.World(era='Num 30:2-17: the vows\' law on the tape — Moses\' one speech to the heads of the tribes (the exodus epoch)', epoch='exodus')
        w.laws = [law_vows]
        w.advance(w.clock.day_in('exodus', 40, 6, 1))
        # THE DAEMON GATE READS LITERAL SUBMITS ONLY — the one line typed out
        w.submit({'kind': 'vows_law_spoken', 'subject': 'moses', 'to': 'the-heads-of-the-tribes', 'heads': ['30:3 a man', '30:4 a daughter in her youth', '30:6 restrained', '30:7 the betrothed', '30:9 the husband on the day', '30:10 the widow', '30:11 the married', '30:13 annulled', '30:15 silent from day to day', '30:16 after his hearing'], 'close': CLOSE, 'case_source': LINE})
    writes = [e for e in w.entity('israel').ledger if e['effect'] == 'commanded']
    return (len(writes), len([l for l in w.log if l[0] == 'TIMER-SET']), len(w.entities), w.clock.eras['exodus'].date(w.clock.day)[1:]), w


NARRATIVE, _WN = narrative()
NARRATIVE_PREDICTED = (1, 0, 1, (6, 1))   # NUMBERS_WALK.md "Sitting 10b": one write (commanded on israel), no timer, one entity, the date (6, 1) of the fortieth year
assert NARRATIVE == NARRATIVE_PREDICTED, ('THE NUMBERS WALK: the vows\' narrative moved from its prediction', NARRATIVE, NARRATIVE_PREDICTED)


# =====================================================================
# Motion 2 — THE TEST DATA: the answer sheet's rows (the docket's LAW rows).
# =====================================================================
CASES = [
    # F1 — the man
    ('Num 30:2 / Sifrei 153:2; Bava Batra 120b:1 — the frame: Moses\' voice, for all generations', lambda: the_man({'ask': 'frame'}, DATA), 'a law relayed in Moses\' voice — this is the thing which the LORD commanded, for all generations'),
    ('Num 30:2 / Sifrei 153:2; Nedarim 77b:8-78a:1 — two offices, two verbs', lambda: the_man({'ask': 'this_is_the_thing'}, DATA), 'two offices, two verbs — the husband annuls, the sage dissolves; the words crossed say nothing'),
    ('Num 30:2 / Sifrei 153:1; Nedarim 78b:3 — the heads of the tribes', lambda: the_man({'ask': 'heads_of_the_tribes'}, DATA), 'the sage\'s release — one expert or three laymen: the shelf\'s office on the freed phrase'),
    ('Mishnah Chagigah 1:8; Chagigah 10a:13 — the release flies in the air; Shmuel\'s ground', lambda: the_man({'ask': 'sage_release_flies'}, DATA), 'flies in the air — the one unrefuted ground the chapter\'s own clause 30:3'),
    ('Nedarim 77b:2-3 — the sage standing, alone, at night', lambda: the_man({'ask': 'sage_release_form'}, DATA), 'no session, no court — standing, alone, at night; the regret arm recorded'),
    ('Nedarim 65a:1-4 — in the presence of the one vowed against', lambda: the_man({'ask': 'sage_release_presence'}, DATA), 'dissolved in the presence of the one vowed against'),
    ('Nedarim 90a:3, 90b:4 — only a vow in effect', lambda: the_man({'ask': 'sage_release_timing'}, DATA), 'only a vow in effect is dissolved'),
    ('Mishnah Nedarim 9:1-10 — the openings', lambda: the_man({'ask': 'openings'}, DATA), 'an opening on "had I known" — the answer sheet\'s method, never the ink\'s'),
    ('Mishnah Nedarim 9:10; Nedarim 65a:6 — the mistaken vow', lambda: the_man({'ask': 'mistaken_vow'}, DATA), 'a mistaken vow — no vow'),
    ('Mishnah Niddah 5:6 — a girl of ten', lambda: the_man({'ask': 'age', 'age': 10, 'sex': 'girl'}, DATA), 'a minor — no vow, no consecration (even saying "we know")'),
    ('Mishnah Niddah 5:6 — a girl of eleven and a day who knows', lambda: the_man({'ask': 'age', 'age': 11, 'sex': 'girl', 'knows_to_whom': True}, DATA), 'the examined year — bound if she knows in Whose name'),
    ('Mishnah Niddah 5:6 — a boy of twelve and a day who does not know', lambda: the_man({'ask': 'age', 'age': 12, 'sex': 'boy', 'knows_to_whom': False}, DATA), 'the examined year — she does not know in Whose name: no vow'),
    ('Mishnah Niddah 5:6; Niddah 46a:2 — a boy of thirteen and a day (NS by CALL)', lambda: the_man({'ask': 'age', 'age': 13, 'sex': 'boy'}, DATA), 'of age — the vow stands without examination'),
    ('Nedarim 13b:4; Shevuot 25a:11-12 — the two stringencies', lambda: the_man({'ask': 'vow_vs_oath'}, DATA), 'the vow binds the OBJECT (even a mitzva\'s), the oath binds the PERSON (even to nothing tangible)'),
    ('Nedarim 14a:5 — leaning on a vowed thing', lambda: the_man({'ask': 'vow_support', 'base': 'vowed'}, DATA), 'leans on a vowed thing — bound'),
    ('Mishnah Nedarim 2:1; Nedarim 13a:2 — leaning on carrion', lambda: the_man({'ask': 'vow_support', 'base': 'torah_forbidden'}, DATA), 'leans on a Torah-forbidden thing — no vow'),
    ('Mishnah Nedarim 1:2 — the substitutes', lambda: the_man({'ask': 'substitutes'}, DATA), 'the substitutes bind — the nations\' words or the Sages\' devised ones'),
    ('Mishnah Nedarim 1:3; Nedarim 11b:6 — not non-sacred', lambda: the_man({'ask': 'not_non_sacred'}, DATA), 'the negation of the common binds — "not non-sacred" is an offering'),
    ('Mishnah Nedarim 1:4; Nedarim 13b:5 — the vow on a limb', lambda: the_man({'ask': 'on_a_limb'}, DATA), 'a vow on the limb binds; on the act it would not'),
    ('Sifrei 153:4; Shevuot 27a:1-5; Nedarim 16b:3 — bind the permitted', lambda: the_man({'ask': 'bind_the_permitted'}, DATA), 'no oath to permit the forbidden — the oath void'),
    ('Num 30:3 / Sifrei 153:4; Nedarim 81b:5, 15a:8 — he shall not profane his word', lambda: the_man({'ask': 'not_profane'}, DATA), 'the vower bound to his word; the sage not for himself; the custom a quasi-vow'),
    ('Sifrei 153:4; Nedarim 3a:7; the musafim runner by CALL — the two transgressions', lambda: the_man({'ask': 'two_transgressions'}, DATA), 'profane and delay — two transgressions; the delay counted in festivals by call'),
    ('Rosh Hashanah 4a:13-4b:2, 6a:14, 6a:16 — the delay\'s clocks', lambda: the_man({'ask': 'delay_clocks'}, DATA), 'two dues — the positive at the first festival, the prohibition at the third; charity now'),
    ('Rosh Hashanah 5b:5, 6a:3 — the sin in you', lambda: the_man({'ask': 'sin_in_you'}, DATA), 'the delay\'s sin on the vower alone — the offering and the wife unmoved'),
    ('Rosh Hashanah 6a:12 — the vow and the gift', lambda: the_man({'ask': 'vow_vs_gift'}, DATA), 'the vow\'s debit persists past its object; the gift\'s dies with it'),
    ('Shevuot 26b:9, 26b:15-16; Sifrei 153:4 — the lips or the heart', lambda: the_man({'ask': 'lips_or_heart'}, DATA), 'the lips required — the heart\'s vow the Sifrei\'s arm, recorded'),
    ('Nedarim 77b:4, 10a:9 — the vower a sinner', lambda: the_man({'ask': 'vower_a_sinner'}, DATA), 'the vower called a sinner — the vow\'s standing on the shelf'),
    ('Nazir 61a:8 — on his soul: the slave', lambda: the_man({'ask': 'on_his_soul'}, DATA), 'the slave\'s soul not his — no vow'),
    ('Shevuot 22a:9, 22a:2 — the konam\'s measure', lambda: the_man({'ask': 'konam_measure'}, DATA), 'any amount — the vow forbids the object, not the act'),
    ('Nedarim 3b:4 — the intimations', lambda: the_man({'ask': 'intimations'}, DATA), 'the partial formula binds — two sources for one rule'),
    ('Num 30:3 / Rosh Hashanah 6a:5 — all that proceeds out of his mouth', lambda: the_man({'ask': 'all_that_proceeds'}, DATA), 'the vow\'s fulfilment — a positive duty, a prohibition, and the court\'s compulsion on one clause'),
    # F2 — the daughter
    ('Num 30:4 / Sifrei 153:4 — a minor', lambda: the_daughter({'ask': 'in_her_youth', 'stage': 'minor'}, DATA), 'a minor — no vow'),
    ('Num 30:4 / Sifrei 153:4 — in her youth', lambda: the_daughter({'ask': 'in_her_youth', 'stage': 'youth'}, DATA), 'in her youth — under her father'),
    ('Mishnah Nedarim 10:2, 11:10 — the mature daughter', lambda: the_daughter({'ask': 'in_her_youth', 'stage': 'mature'}, DATA), 'mature — her vow stands, no annuller'),
    ('Sifrei 153:4; Nedarim 70a-70b — the father\'s domain', lambda: the_daughter({'ask': 'fathers_domain'}, DATA), 'the father\'s domain — the betrothal\'s widow in, the marriage\'s out'),
    ('Sifrei 153:5; Nedarim 72b:10 — the hearing by report', lambda: the_daughter({'ask': 'hearing_by_report'}, DATA), 'told by others — the hearing day opens'),
    ('Sifrei 153:5; Nedarim 73a:4 — the deaf', lambda: the_daughter({'ask': 'the_deaf'}, DATA), 'the deaf hear nothing — no hearing day, no annulment'),
    ('Sifrei 153:5; Mishnah Nedarim 11:5; Nedarim 86b:5 — intending her', lambda: the_daughter({'ask': 'intends_her'}, DATA), 'the annulment void — the intended vow only; he annuls again'),
    ('Sifrei 153:5; Nedarim 79a:1 — confirmed for one hour', lambda: the_daughter({'ask': 'confirmed_for_one_hour'}, DATA), 'confirmed once, never annulled'),
    ('Num 30:9 / Sifrei 153:6, 153:9 — restraint is annulment', lambda: the_daughter({'ask': 'restraint_is_annulment'}, DATA), 'restraint = annulment — the word defined by its pair'),
    ('Sifrei 153:6 — the father\'s hearing day by the likening', lambda: the_daughter({'ask': 'fathers_hearing_day'}, DATA), 'the father\'s day by the footer\'s likening'),
    ('Sifrei 153:6; Kiddushin 81b:5; Nazir 23a:3; Nedarim 83a:1 — the forgiveness', lambda: the_daughter({'ask': 'forgiveness'}, DATA), 'annulled unknown to her — forgiven for the intent, no lashes'),
    ('Sifrei 153:6; Bava Metzia 96a:20; Nedarim 72b:8-9 — the caretaker and the messenger', lambda: the_daughter({'ask': 'caretaker'}, DATA), 'the act his own — the messenger a recorded dispute'),
    ('Nedarim 72b:3-73a:1 — annulment without hearing (unresolved)', lambda: the_daughter({'ask': 'annulment_without_hearing'}, DATA), 'unresolved on the shelf — the hearing the machine\'s trigger'),
    ('Sifrei 155:1 — the father\'s scope; I reasoned and reversed', lambda: the_daughter({'ask': 'fathers_scope'}, DATA), 'the father as the husband by the likening — the reversed induction named'),
    ('Ketubot 46b:6, 47a:6; Kiddushin 3b:7 — the father\'s rights from the footer', lambda: the_daughter({'ask': 'fathers_rights'}, DATA), 'the footer\'s clause carried to her gains — labeled'),
    ('Nedarim 79a:1; 77b:7 — the annulment in the heart', lambda: the_daughter({'ask': 'heart_annuls'}, DATA), 'the annulment an act — the heart\'s arm recorded'),
    # F3 — the betrothed
    ('Mishnah Nedarim 10:1; Nedarim 67a:5, 68a:1 — both together', lambda: the_betrothed({'ask': 'joint_authority', 'by': ['father', 'husband']}, DATA), 'annulled — both together'),
    ('Mishnah Nedarim 10:1 — the father alone', lambda: the_betrothed({'ask': 'joint_authority', 'by': ['father']}, DATA), 'not annulled — one alone'),
    ('Num 30:7 / Nedarim 67b:2, 70a:8, 70b:1 — be, she shall be', lambda: the_betrothed({'ask': 'be_she_shall_be'}, DATA), 'the doubled verb read as law — betrothal, and the second betrothal after the first\'s death'),
    ('Mishnah Nedarim 10:2; Nedarim 70a:7 — the father dies', lambda: the_betrothed({'ask': 'fathers_death'}, DATA), 'the father dead — the betrothed alone annuls nothing; the vow stands'),
    ('Mishnah Nedarim 10:2; Nedarim 68a:5 — the betrothed dies unheard', lambda: the_betrothed({'ask': 'betrotheds_death', 'husband': 'unheard'}, DATA), 'reverted to the father — he annuls alone'),
    ('Nedarim 68b:1 — the betrothed died silent the next day', lambda: the_betrothed({'ask': 'betrotheds_death', 'husband': 'silent_next_day'}, DATA), 'confirmed before his death — the father cannot'),
    ('Num 30:7 / Nedarim 71a:2-3; Mishnah Nedarim 10:3 — the vows carried', lambda: the_betrothed({'ask': 'vows_carried'}, DATA), 'the vows carried to the last betrothed — annulled with the father'),
    ('Nedarim 69a:2, 71b:1 — Beit Hillel: the annulment weakens', lambda: the_betrothed({'ask': 'share_or_weaken'}, DATA), 'the joint annulment weakens, never severs'),
    ('Nedarim 67b:4 — the father\'s confirmation blocks', lambda: the_betrothed({'ask': 'fathers_confirmation'}, DATA), 'one confirming — confirmed'),
    ('Nedarim 67a:4 — the dissolved confirmation', lambda: the_betrothed({'ask': 'dissolved_confirmation'}, DATA), 'the dissolved confirmation does not revive the other\'s annulment'),
    ('Num 30:7 / Sifrei 153:7; Shevuot 20a:4-9; Lev 5:4 by CALL — the utterance is an oath', lambda: the_betrothed({'ask': 'utterance_is_oath'}, DATA), 'the utterance of her lips = an oath — Leviticus 5:4 by call'),
    ('Mishnah Nedarim 10:7; Sifrei 153:10; Nedarim 75a:6 — annulling in advance', lambda: the_betrothed({'ask': 'annul_in_advance'}, DATA), '"all vows you will vow are annulled" — nothing (the Rabbis)'),
    ('Num 30:14 / Sifrei 153:10 — what came to confirmation came to annulment', lambda: the_betrothed({'ask': 'confirmation_and_annulment_reach'}, DATA), 'the two verbs one reach'),
    ('Nedarim 71b:2-72a:8 — divorce as silence or confirmation (unresolved)', lambda: the_betrothed({'ask': 'divorce_as'}, DATA), 'unresolved — the machine writes nothing at a divorce'),
    ('Mishnah Nedarim 10:5; Nedarim 73b:5 — the sustained betrothed', lambda: the_betrothed({'ask': 'sustained_betrothed'}, DATA), 'the sustained betrothed — R. Eliezer\'s arm recorded; the Rabbis rule'),
    ('Mishnah Nedarim 10:6; Nedarim 74a-75a — the levirate widow', lambda: the_betrothed({'ask': 'levirate_widow'}, DATA), 'the levirate widow — R. Akiva: no annulment'),
    ('Num 30:9 / Nedarim 73a:5-7 — two wives (NS.sotah by reference)', lambda: the_betrothed({'ask': 'two_wives'}, DATA), 'one wife at a time'),
    ('Mishnah Nedarim 10:3 — betrothed a hundred times the same day', lambda: the_betrothed({'ask': 'same_day_hundred'}, DATA), 'the last husband and the father annul'),
    # F4 — the widow and the divorcee
    ('Num 30:10 / Sifrei 154:1; Ketubot 49a:2 — from marriage', lambda: the_widow({'ask': 'from_marriage'}, DATA), 'no annuller — the vow stands'),
    ('Sifrei 154:1; Mishnah Nedarim 11:10; Nedarim 89b:2 — the orphan in her father\'s lifetime', lambda: the_widow({'ask': 'orphan_in_fathers_lifetime'}, DATA), 'the orphan in her father\'s lifetime — her vows stand'),
    ('Mishnah Nedarim 11:9 — vowed in widowhood, then married', lambda: the_widow({'ask': 'remarried', 'when': 'before'}, DATA), 'vowed in widowhood — the new husband annuls nothing'),
    ('Num 30:11 / Sifrei 154:1 — vowed in his house', lambda: the_widow({'ask': 'remarried', 'when': 'after'}, DATA), 'vowed in his house — the husband annuls'),
    ('Nedarim 89a:2-5 — the vow\'s timing (R. Yishmael / R. Akiva)', lambda: the_widow({'ask': 'vow_timing'}, DATA), 'the authority at the vow\'s making — the marriage-hook the disputed arm'),
    ('Mishnah Nedarim 11:9; Yevamot 87a:7 — once out one hour', lambda: the_widow({'ask': 'once_out_one_hour'}, DATA), 'out one hour — the earlier vows beyond him'),
    ('Lev 22:13 by CALL; Yevamot 87a:6 — the priest\'s daughter\'s pair of words', lambda: the_widow({'ask': 'priests_daughter_pair'}, DATA), 'the pair of words shared — the return is for terumah, not for vows'),
    ('Mishnah Nedarim 10:6 — awaiting the brother-in-law', lambda: the_widow({'ask': 'levirate'}, DATA), 'awaiting the brother-in-law — her vow stands'),
    # F5 — the married woman
    ('Num 30:11 / Nedarim 67b:1 — vowed before the marriage', lambda: the_wife({'ask': 'in_husbands_house', 'when': 'before'}, DATA), 'vowed before the marriage — beyond him'),
    ('Num 30:11 / Sifrei 154:1 — vowed in his house', lambda: the_wife({'ask': 'in_husbands_house', 'when': 'after'}, DATA), 'vowed in his house — he annuls'),
    ('Mishnah Nedarim 10:4; Nedarim 72b:4 — the scholars\' practice', lambda: the_wife({'ask': 'scholars_practice'}, DATA), 'the advance annulment a conditional on the hearing'),
    ('Num 30:12, 30:15 / Sifrei 154:2, 156:1; Nedarim 79a:5 — the two silences', lambda: the_wife({'ask': 'two_silences'}, DATA), 'both silences confirm at the day\'s end'),
    ('Nedarim 77b:5 — "you did well"', lambda: the_wife({'ask': 'confirming_words', 'said': 'well_done'}, DATA), 'confirmed by his words at once'),
    ('Nedarim 77b:5 — "I do not want you to vow"', lambda: the_wife({'ask': 'confirming_words', 'said': 'do_not_want'}, DATA), 'nothing said — the day runs'),
    ('Sifrei 154:2 — leave to annul all the day', lambda: the_wife({'ask': 'all_the_day'}, DATA), 'leave to annul all the day'),
    ('Num 30:13 / Sifrei 154:3 — the caretaker excluded', lambda: the_wife({'ask': 'caretaker_excluded'}, DATA), 'the caretaker excluded — R. Yonatan\'s agent recorded'),
    ('Nedarim 69a:4, 79a:3 — the sage over the confirmation', lambda: the_wife({'ask': 'sage_over_confirmation'}, DATA), 'the confirmation reopened by the sage; the annulment never'),
    ('Nedarim 69b:3 — confirmed and annulled at once', lambda: the_wife({'ask': 'confirmed_and_annulled', 'form': 'at_once'}, DATA), 'nothing — the two ops exclusive'),
    ('Nedarim 69b:1-2 — confirmed on condition the annulment holds', lambda: the_wife({'ask': 'confirmed_and_annulled', 'form': 'conditioned'}, DATA), 'annulled — the condition carries it'),
    ('Mishnah Nedarim 11:5; Nedarim 87a:3 — the mistaken annulment', lambda: the_wife({'ask': 'mistaken_annulment'}, DATA), 'the mistaken annulment void'),
    ('Nedarim 87a:5-8 — within the time of a short phrase', lambda: the_wife({'ask': 'short_phrase'}, DATA), 'the retraction window of a short phrase — the vow and its annulment inside it'),
    ('Mishnah Nazir 4:1; NS by CALL — her "and I" after his', lambda: the_wife({'ask': 'her_and_i', 'who_first': 'husband'}, DATA), 'her "and I" annulled'),
    ('Mishnah Nazir 4:1 — his "and I" after hers', lambda: the_wife({'ask': 'her_and_i', 'who_first': 'wife'}, DATA), 'his "and I" — he cannot annul hers'),
    ('Num 30:13 / Sifrei 154:3; Nazir 23a:3 — the forgiveness', lambda: the_wife({'ask': 'forgiveness_wife'}, DATA), 'forgiven — annulled unknown to her'),
    ('Nedarim 89b:4-5, 90a:2 — annulled before it takes effect', lambda: the_wife({'ask': 'annul_before_effect'}, DATA), 'annulled before it takes effect — the Rabbis'),
    ('Nedarim 73b:5 — every woman vows on her husband\'s consent', lambda: the_wife({'ask': 'consent_rationale'}, DATA), 'the husband\'s power explained by the sustenance'),
    ('Gittin 85a:22, 73b:16 — divorced except the vows', lambda: the_wife({'ask': 'divorce_except_vows'}, DATA), 'the power a marriage component — the severance question open'),
    # F6 — the affliction oath and the day
    ('Num 30:14, 30:17 / Sifrei 155:1; Nedarim 81b:2 — the filter: affliction', lambda: the_affliction_oath({'ask': 'the_filter', 'content_class': 'affliction'}, DATA), 'annulled — affliction or between them'),
    ('Nedarim 79b:2 — the filter: between him and her', lambda: the_affliction_oath({'ask': 'the_filter', 'content_class': 'between'}, DATA), 'annulled — affliction or between them'),
    ('Mishnah Nedarim 11:3-4 — the filter: neither', lambda: the_affliction_oath({'ask': 'the_filter', 'content_class': 'other'}, DATA), 'not annulled — neither affliction nor between them'),
    ('Mishnah Nedarim 11:2 — the produce of the world', lambda: the_affliction_oath({'ask': 'affliction_scope', 'what': 'world'}, DATA), 'annulled'),
    ('Mishnah Nedarim 11:2 — the produce of this country', lambda: the_affliction_oath({'ask': 'affliction_scope', 'what': 'country'}, DATA), 'not annulled — he supplies from elsewhere'),
    ('Mishnah Nedarim 11:2 — this storekeeper, his sole supplier', lambda: the_affliction_oath({'ask': 'affliction_scope', 'what': 'sole_storekeeper'}, DATA), 'annulled'),
    ('Mishnah Nedarim 11:1; Nedarim 81a:10, 81b:2-3 — the bathe / adorn vows', lambda: the_affliction_oath({'ask': 'bathing'}, DATA), 'the bathe / adorn vows annulled — as affliction or as between them'),
    ('Nedarim 80b:6; Lev 23:27 by CALL — Rava\'s two afflictions', lambda: the_affliction_oath({'ask': 'two_afflictions'}, DATA), 'one root, two senses — the vow\'s affliction is what leads to it'),
    ('Nedarim 79b:5, 82a:1 — the two reaches', lambda: the_affliction_oath({'ask': 'annulment_reach'}, DATA), 'two reaches — for others (affliction), for himself (between them)'),
    ('Mishnah Nedarim 11:4; Nedarim 81b:4, 85a:9 — the void vow on an owed duty', lambda: the_affliction_oath({'ask': 'void_vow_owed_duty'}, DATA), 'no vow — she owes the work; annulled anyway for the excess or the divorce'),
    ('Nedarim 81b:8 — we do not feed a person what is forbidden to him', lambda: the_affliction_oath({'ask': 'we_do_not_feed'}, DATA), 'the self-prohibition annulled — the owed duty does not lift it'),
    ('Mishnah Nedarim 11:12; Nedarim 82a:1 — removed from the Jews', lambda: the_affliction_oath({'ask': 'removed_from_the_jews'}, DATA), 'his part annulled — the between-them reach'),
    ('Sifrei 155:1 — the father\'s reach', lambda: the_affliction_oath({'ask': 'fathers_reach'}, DATA), 'the father\'s reach by the likening'),
    ('Mishnah Nedarim 11:6; Nedarim 87a:10 — confirmed for the figs', lambda: the_affliction_oath({'ask': 'partial_annulment', 'act': 'confirm_part'}, DATA), 'confirmed for a part — all confirmed'),
    ('Mishnah Nedarim 11:6; Nedarim 87b:1-2 — annulled for the figs', lambda: the_affliction_oath({'ask': 'partial_annulment', 'act': 'annul_part'}, DATA), 'annulled for a part — not annulled till the whole (R. Yishmael)'),
    ('Nedarim 82b:2-3 — the two loaves', lambda: the_affliction_oath({'ask': 'two_loaves'}, DATA), 'the mixed vow — R. Yochanan: the afflicting loaf alone'),
    ('Nedarim 83a:3-6; NS by CALL — the naziriteship annulled whole', lambda: the_affliction_oath({'ask': 'nazirite_whole'}, DATA), 'her naziriteship annulled whole'),
    ('Sifrei 156:1; Nedarim 76b:4-8; the calendar row — the deadline', lambda: the_affliction_oath({'ask': 'the_deadline'}, DATA), 'to nightfall — the timer due the hearing day + 1; the twenty-four hours recorded'),
    ('Mishnah Nedarim 10:8 — the leniency and the stringency', lambda: the_affliction_oath({'ask': 'day_leniency_stringency'}, DATA), 'the day ends at dark — a night and a day, or an hour'),
    ('Nedarim 78b:4-79a:9 — the silence to vex', lambda: the_affliction_oath({'ask': 'silence_to_vex'}, DATA), 'the vexing silence confirms at nightfall — the timer fires whatever the intent'),
    ('Mishnah Shabbat 24:5; Nedarim 77a:4, 77b:6 — the annulment on the Sabbath', lambda: the_affliction_oath({'ask': 'annul_on_sabbath'}, DATA), 'annulled on the Sabbath — "take and eat"'),
    ('Mishnah Nedarim 11:7 — the day he learned', lambda: the_affliction_oath({'ask': 'day_of_learning'}, DATA), 'the day he learned — a second hearing day'),
    ('Num 30:16 / Sifrei 156:2; Nedarim 79a:4 — after his hearing', lambda: the_affliction_oath({'ask': 'after_his_hearing'}, DATA), 'annulled after the day — the vow stands, the husband bears her iniquity'),
    ('Num 30:16, 5:31 by CALL; Nedarim 83a:1 — she is clear', lambda: the_affliction_oath({'ask': 'she_is_clear'}, DATA), 'she is clear — the iniquity his'),
    ('Sifrei 156:2; Sanhedrin 100a:18; Yoma 76a:7 — the measure of good', lambda: the_affliction_oath({'ask': 'measure_of_good'}, DATA), 'the a-fortiori from the two measures — the ratio a recorded parameter'),
    ('Shevuot 27a:6; Lev 5:4 by CALL — the oath to harm himself', lambda: the_affliction_oath({'ask': 'oath_to_harm_himself'}, DATA), 'the affliction oath the oath to harm oneself — bound'),
    ('Num 30:14 / Nedarim 80b:3-4 — vows and oaths one class', lambda: the_affliction_oath({'ask': 'vows_and_oaths_one_class'}, DATA), 'vows and oaths one class for the annulment'),
    # F7 — the statutes
    ('Num 30:17 / Sifrei 156:3; Nedarim 68a:1 — the likening both ways', lambda: the_statutes({'ask': 'likening_both_ways'}, DATA), 'the footer likens both ways — the engine of the chapter'),
    ('Num 30:17 / Sifrei 156:3; Nedarim 70a:7 — in her youth, her father\'s house', lambda: the_statutes({'ask': 'in_her_youth_her_fathers_house'}, DATA), 'the father\'s bound; the husband\'s reach'),
    ('Ketubot 40b:4; Kiddushin 3b:7 — the father\'s gains', lambda: the_statutes({'ask': 'fathers_gains'}, DATA), 'the clause generalized — labeled'),
    ('Num 30:1 / THE REGISTER GATE — the receipt\'s second form', lambda: the_statutes({'ask': 'the_receipt'}, DATA), 'the receipt that closes a speech — in the census by the finder\'s second form'),
    ('Num 30:17 / THE REGISTER GATE — the footer\'s block', lambda: the_statutes({'ask': 'the_register_gate'}, DATA), 'the footer DAEMONS — law_vows joined its block'),
    ('Num 30:3-16 — the case structure (computed)', lambda: the_statutes({'ask': 'case_structure'}, DATA), 'two when, seven and-if — the draft\'s nine rows'),
    ('Num 30:6-16 — the clock words (computed)', lambda: the_statutes({'ask': 'clock_words'}, DATA), 'the clock the chapter\'s only number'),
    ('Num 30:3-16 — the doubled verbs (computed)', lambda: the_statutes({'ask': 'doubled_verbs'}, DATA), 'five doubled verbs — every one read by the shelf as law'),
    ('Num 30:2-17 — the tape\'s one line', lambda: the_statutes({'ask': 'the_line'}, DATA), 'the statutes of vows commanded — one write, no timer, no close'),
    ('THE LOOP step 3 — installed_by for a law in Moses\' voice', lambda: the_statutes({'ask': 'installed_by'}, DATA), 'installed_by boot — a statute relayed in Moses\' voice, the class named'),
    ('Bava Batra 120b:1; Nedarim 78a:2 — for all generations', lambda: the_statutes({'ask': 'all_generations'}, DATA), 'for all generations — the relay not case-bound'),
    ('Nedarim 78a:9-78b:2 — the chapter\'s placement', lambda: the_statutes({'ask': 'placement_after_the_calendar'}, DATA), 'the chapter\'s placement read as law — next to the calendar, not of it'),
    ('Num 30:3, 30:4, 30:6, 30:15 — two kinds of ki (computed)', lambda: the_statutes({'ask': 'two_kinds_of_ki'}, DATA), 'one particle, two jobs — the parse decides'),
    # THE INK, computed
    ('THE PARSER — no cardinal, no ordinal; the three oath-tokens starred', lambda: (([n for n in NUMBERS.values() if n], [o for o in ORDINALS.values() if o], STARRED), [FX.NONE], [('INK', 'Num 30:1-17 — the parser')]), ([], [], [(3, 'שבעה*'), (11, 'בשבעה*'), (14, 'שבעת*')])),
    ('THE CASE STRUCTURE — two when, seven and-if, the two other ki (computed)', lambda: ((WHEN, AND_IF, KI_SEATS), [FX.NONE], [('INK', 'Num 30:3-16 — computed on the first words')]), ([3, 4], [6, 7, 9, 11, 13, 15, 16], [(3, 1), (4, 1), (6, 18), (15, 20)])),
    ('THE CLOCK WORDS — on the day of his hearing, from day to day, after his hearing (computed)', lambda: ((DAY_OF_HEARING, DAY_TO_DAY, AFTER_HEARING), [FX.NONE], [('INK', 'the whole DB')]), (['Num 30:6', 'Num 30:8', 'Num 30:13', 'Num 30:15'], ['1Chr 16:23', 'Num 30:15'], ['Num 30:16'])),
    ('THE FRAMES — this is the thing (8), the heads of the tribes (3), these are the statutes (3), the receipt\'s second form (7)', lambda: ((len(THIS_IS), THIS_IS[-2:], HEADS, FOOTER, len(RECEIPT2), RECEIPT2[-1]), [FX.NONE], [('INK', 'the whole DB')]), (8, ['Num 30:2', 'Num 36:6'], ['1Kgs 8:1', '2Chr 5:2', 'Num 30:2'], ['Deut 12:1', 'Lev 26:46', 'Num 30:17'], 7, 'Num 30:1')),
    ('THE DOUBLED VERBS — annul (2 seats), be (2), silent (1), swear (1)', lambda: ((ANNUL_ANNUL, BE_BE, SILENT_SILENT, SWEAR_OATH), [FX.NONE], [('INK', 'the whole DB')]), (['Num 30:13', 'Num 30:16'], ['Jer 15:18', 'Num 30:7'], ['Num 30:15'], ['Num 30:3'])),
    ('THE PERSONS AND THE PAIRS — her husband 9, her father 6; the widow\'s pair 3; the utterance 2; in her youth 2', lambda: ((HUSBAND_TOKENS, FATHER_TOKENS, WIDOW_DIVORCEE, UTTERANCE, IN_HER_YOUTH), [FX.NONE], [('INK', 'Num 30 and the whole DB')]), (9, 6, ['Lev 21:14', 'Lev 22:13', 'Num 30:10'], ['Num 30:7', 'Num 30:9'], ['Num 30:4', 'Num 30:17'])),
    ('THE FORGIVENESS AND THE INIQUITY — three seats; one seat; the frame verbs Moses\'', lambda: ((FORGIVE, BEAR_HER, FRAME_VERBS, CONFIRM_ANNUL_IT), [FX.NONE], [('INK', 'the whole DB')]), (['Num 30:6', 'Num 30:9', 'Num 30:13'], ['Num 30:16'], [(1, 'ויאמר'), (2, 'וידבר')], ('יקימנו', 'יפרנו'))),
    # THE CALLEES
    ('THE NASO RUNNER — the nazirite\'s vow-form and the sotah\'s 5:31 (by CALL)', lambda: ((NAZ_SUB[0], NAZ_PART[0], SOTAH_CLEAN[0], SOTAH_UNCLEAN[0][:19]), [FX.NONE], [('MOVE', 'CALLED cold_run_naso')]), ('binds (nazir lehazir)', 'a full nazirite', 'tested', 'the waters do not t')),   # the first graded run: the nineteen-character slice typed as eighteen — retyped from the print
    ('THE LEVITICUS 5 RUNNER — the utterance oath\'s option template (by CALL)', lambda: ((OATH_OPTION[0][:7], OATH_NO_OPTION[0]), [FX.NONE], [('MOVE', 'CALLED cold_run_vayikra5')]), ('CONFESS', 'exempt')),
    ('THE PRIESTHOOD RUNNER — the priest\'s daughter\'s return (by CALL)', lambda: ((PR_RETURN['v']['widow_and_divorcee'], PR_TABLE['v']), [FX.NONE], [('MOVE', 'CALLED cold_run_priesthood')]), ('both_written_both_need_no_seed', 'terumah_returns')),
    ('THE MUSAFIM RUNNER — the vow_deadline row (by CALL)', lambda: ((MU_DEADLINE[0], MU_ROW['value'], sorted(MU_ROW['settings'])), [FX.NONE], [('MOVE', 'CALLED cold_run_musafim')]), ('three festivals in any order — the first tanna', 'three_festivals_any_order', ['by_sukkot', 'one_festival', 'three_festivals_any_order', 'three_in_order'])),
    ('THE MOADIM RUNNER — the affliction list (by CALL)', lambda: (MO_AFFLICTION, [FX.NONE], [('MOVE', 'CALLED cold_run_moadim')]), 'eating_drinking_washing_anointing_sandals_relations'),
    ('THE CALENDAR ROW — vow_annulment_window (the third registry)', lambda: ((WINDOW, sorted(CAL_ROW['settings']), CAL_ROW['channel']), [FX.NONE], [('DATA', 'calendar_parameters.yaml')]), ('to_nightfall', ['to_nightfall', 'twenty_four_hours'], 'received')),
    # THE WRAP: the scene on the world engine
    ('THE SCENE on the world engine — THE STATE MACHINE\'s persons and the exam\'s through the ten case kinds; the timers set, fired and cancelled (predicted before the run)',
     lambda: (SCENE, [FX.NONE], [('INK', 'Num 30:1-17 — the recorded rows replayed')]),
     ((1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 0, 1, 0, 1, 0), (8, 5, 3, 0), (1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1), 46)),   # the literal typed from SCENE_PREDICTED (the guard reads literals only)
    ('THE NARRATIVE on the world engine — the one line; one write, no timer (predicted before the run)',
     lambda: (NARRATIVE, [FX.NONE], [('INK', 'Num 30:2-17 — the one line')]), (1, 0, 1, (6, 1))),
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
    print('THE INK: numbers %s; starred %s; when %s; and-if %s; the clock words %s / %s / %s; the doubled verbs %s' % ([n for n in NUMBERS.values() if n], STARRED, WHEN, AND_IF, DAY_OF_HEARING, DAY_TO_DAY, AFTER_HEARING, DOUBLED))
    print('THE STATE MACHINE on the bench: %s; the timers (set, fired, cancelled, pending) %s; the exam persons %s; entities %d' % SCENE)
    print('THE NARRATIVE: %s' % (NARRATIVE,))
    print('THE CALENDAR ROW: vow_annulment_window = %s (settings %s)' % (WINDOW, sorted(CAL_ROW['settings'])))
    print('THE PARAMETER ROWS: ' + '; '.join('%s = %s' % (k, DATA[k]['value']) for k in DATA) + ' (the other settings recorded in DATA)')
    if ok == len(CASES):
        print('\nTHE COMPILE OF THE VOWS: the answer sheet REPRODUCED — %d/%d' % (ok, len(CASES)))
    sys.exit(0 if ok == len(CASES) else 1)

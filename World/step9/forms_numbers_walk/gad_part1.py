#!/usr/bin/env python3
# NUM 32:1-42 — GAD AND REUBEN (THE NUMBERS WALK sitting 12b, 2026-09-12; World/step9/NUMBERS_WALK.md "Sitting 12b"; the state doc's #150-#151).
# THE STIPULATION AS A CONDITIONAL GRANT WITH BOTH ARMS ON THE LEDGER, ITS RELEASE A RUN OUTSIDE THE TORAH: the two tribes' request
# (32:1-5) a plea on the ink's compound party; Moses' rebuke retelling chapter 14's oath with the verb supplied (32:6-15 — read against the
# shelach runner's ledger, NO WRITE); the offer (32:16-19); THE DOUBLED CONDITION (32:20-24 — Mishnah Kiddushin 3:4's exemplar, the source of
# the whole law of conditions, Gittin 75a:11) as a DEBIT to cross armed before the LORD until the land is subdued, OPEN BY DESIGN to Joshua
# 22:1-9, beside the build command CLOSED at 32:34-38; THE UTTERANCE RULE'S SECOND SEAT (32:24 = 30:3) by CALL into the vows' runner, whose
# cell's own effect is the debit's; THE CLEARANCE (32:22 — Mishnah Shekalim 3:2's rule) a new status the exam writes; the acceptance and the
# commission charged with the second doubling (32:25-32 — the dividers of the land, Joshua 14:1's triad; their debit open); THE GRANT (32:33)
# as three transfers from Israel's possession by conquest (the chukat runner's land_possessed READ off the ledger), the two and a half's count
# from the second census's rows by CALL; the fourteen cities as statuses (32:34-38); Machir's sons, Jair and Nobah as the land possessed
# (32:39-42 — the Genesis 50:23 collective written on again; two new persons with their homograph traps). Eight cells; every token probed
# (zero-report law); effects on every cell (the effects law); the parameters the ink leaves open recorded in DATA with their arms. Reading
# ledger: logic/oral_triage/num_32_gad_reuben_2026-09-12.md; the exam's docket: logic/oral_triage/num_32_gad_reuben_exam_2026-09-12.md
# (319 rows: LAW 19 / DERIVATION 55 / DISPUTE 2 / CONTEXT 242 / OUTSIDE 1).

# ---- THE HONEST-PAIRING GUARD ----------------------------------------------------------------------------
import os as _os, sys as _sys
_sys.path.insert(0, _os.path.dirname(_os.path.abspath(__file__)))
from compile_guards import check_honest_pairing as _chp
_P = _os.path.abspath(__file__)
GUARDED = _chp(_P, 'CASES', 2)
assert GUARDED == 74, ("the guard counted %d expectations, the tripwire holds 74" % GUARDED)   # the design's estimate — retyped from the guard's print after the first run
print('guard: %d expectations checked, every one a literal from the answer sheet [honest-pairing guard satisfied]' % GUARDED)
import sqlite3, sys, io, re, contextlib, collections, yaml
import effects_layer as FX
import world_engine as WE
import cold_run_vows as VW                       # THE EDGE: gad_reuben -> vows CALL, reference (32:24's "that which has gone out of your mouth you shall do" = 30:3's phrase — the utterance rule's second seat; the hinder-root shared)
import cold_run_shelach as SL                    # THE EDGE: gad_reuben -> shelach CALL, reference (32:8-13 retells 13-14 in the oath's own words: the set, the exceptions, the forty years, Caleb's Hebron)
import cold_run_chukat as CK                     # THE EDGE: gad_reuben -> chukat CALL, reference (32:33's kingdoms of Sihon and Og = 21:21-35's conquests — the grant's source; Jazer; "its daughters"; "dispossessed the Amorite")
import cold_run_second_census as C2              # THE EDGE: gad_reuben -> second_census CALL, reference (26:7, 18, 34's counts — the two and a half; 26:2's formula; 26:29's Machir; the lot's division not this chapter's)
import cold_run_bamidbar as BM                   # THE EDGE: gad_reuben -> bamidbar CALL, reference (1:3's census formula at 32:11; Gad third in the camps)

HERE = _os.path.dirname(_os.path.abspath(__file__))
# ONE copy of the numeral parser: the sequence runner's INK block executed here (the stitcher's way — no import edge)
_SRC = open(_os.path.join(HERE, 'cold_run_sequence.py'), encoding='utf-8').read()
_INK = {'re': re, 'sqlite3': sqlite3, 'os': _os, 'WE': WE}
exec(_SRC.split('# ==== INK BEGIN')[1].split('# ==== INK END ====')[0].split('\n', 1)[1], _INK)
ink_numbers, ink_ordinals, verse_words = _INK['ink_numbers'], _INK['ink_ordinals'], _INK['verse_words']

db = sqlite3.connect('<repo-old>/elijah_docket/tanakh.sqlite')

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
    ('ומקנה',    32, 1,  'and much cattle — the chapter opens on the herds'),
    ('רב',       32, 1,  'much'),
    ('לבני',     32, 1,  'to the sons of [Reuben] — Reuben first here alone'),
    ('ראובן',    32, 1,  'Reuben'),
    ('גד',       32, 1,  'Gad'),
    ('יעזר',     32, 1,  'Jazer — 21:32\'s city'),
    ('גלעד',     32, 1,  'Gilead'),
    ('מקום',     32, 1,  'a place [for cattle]'),
    ('מקנה',     32, 1,  'cattle'),
    ('ויבאו',    32, 2,  'and they came'),
    ('בני',      32, 2,  'the sons of [Gad] — the compound party, Gad first'),
    ('ובני',     32, 2,  'and the sons of [Reuben]'),
    ('אלעזר',    32, 2,  'Eleazar [the priest] — 27:2\'s triad'),
    ('נשיאי',    32, 2,  'the princes of [the congregation]'),
    ('עטרות',    32, 3,  'Ataroth — the first of the nine'),
    ('ובען',     32, 3,  'and Beon — the last of the nine'),
    ('הכה',      32, 4,  'smote — the land which the LORD smote (the conquest\'s ledger)'),
    ('ולעבדיך',  32, 4,  'and your servants have [cattle]'),
    ('יתן',      32, 5,  'let [this land] be given'),
    ('לאחזה',    32, 5,  'for a possession — the holding word (Genesis 47:11)'),
    ('תעברנו',   32, 5,  'bring us over [the Jordan]'),
    ('הירדן',    32, 5,  'the Jordan'),
    ('האחיכם',   32, 6,  'shall your brothers'),
    ('למלחמה',   32, 6,  'to war'),
    ('תשבו',     32, 6,  'you sit [here]'),
    ('תנואון',   32, 7,  'you discourage — THE HINDER-ROOT, the vows\' verb (30:6-12); the store\'s written-and-read pair'),
    ('לב',       32, 7,  'the heart of'),
    ('אבתיכם',   32, 8,  'your fathers'),
    ('בשלחי',    32, 8,  'when I sent — Moses\' own first person'),
    ('ברנע',     32, 8,  'Kadesh-barnea'),
    ('לראות',    32, 8,  'to see [the land] — the spies\' verb at this telling'),
    ('אשכול',    32, 9,  'Eshcol'),
    ('ויניאו',   32, 9,  'and they discouraged'),
    ('ויחר',     32, 10, 'and [the anger of the LORD] burned'),
    ('וישבע',    32, 10, 'and he swore — THE VERB SUPPLIED (chapter 14: "as I live")'),
    ('העלים',    32, 11, 'who came up [from Egypt]'),
    ('עשרים',    32, 11, 'twenty — the census formula'),
    ('ומעלה',    32, 11, 'and upward'),
    ('נשבעתי',   32, 11, 'I swore [to Abraham, to Isaac and to Jacob]'),
    ('מלאו',     32, 11, 'they followed [Me] fully'),
    ('כלב',      32, 12, 'Caleb'),
    ('הקנזי',    32, 12, 'the Kenizzite — Genesis 15:19\'s nation as a gentilic'),
    ('ויהושע',   32, 12, 'and Joshua'),
    ('וינעם',    32, 13, 'and he made them wander — the causative\'s one Torah seat'),
    ('ארבעים',   32, 13, 'forty [years]'),
    ('תם',       32, 13, 'was consumed'),
    ('הדור',     32, 13, 'the generation'),
    ('הרע',      32, 13, 'the evil — the Kings\' formula at its first seat'),
    ('תרבות',    32, 14, 'a brood of — a hapax'),
    ('חטאים',    32, 14, 'sinful [men] — Sodom\'s word'),
    ('לספות',    32, 14, 'to add'),
    ('חרון',     32, 14, 'the fierce [anger]'),
    ('להניחו',   32, 15, 'to leave them [in the wilderness]'),
    ('ושחתם',    32, 15, 'and you will destroy'),
    ('גדרת',     32, 16, 'folds [for sheep] — the cattle first'),
    ('לטפנו',    32, 16, 'for our little ones'),
    ('נחלץ',     32, 17, 'we will arm ourselves — the arm-root'),
    ('חשים',     32, 17, 'hastening'),
    ('נשוב',     32, 18, 'we will [not] return'),
    ('התנחל',    32, 18, 'have inherited'),
    ('מזרחה',    32, 19, 'eastward'),
    ('תחלצו',    32, 20, 'you arm yourselves'),
    ('חלוץ',     32, 21, 'armed one — every armed one of you'),
    ('ועבר',     32, 21, 'and will pass over — the perfect read of the future (Sotah 3a:8)'),
    ('הורישו',   32, 21, 'he has dispossessed'),
    ('ונכבשה',   32, 22, 'and [the land] is subdued'),
    ('נקיים',    32, 22, 'clear — THE CLEARANCE (Shekalim 3:2)'),
    ('מיהוה',    32, 22, 'from the LORD'),
    ('ומישראל',  32, 22, 'and from Israel'),
    ('חטאתם',    32, 23, 'you have sinned — the negative arm'),
    ('תמצא',     32, 23, 'will find [you] — Judah\'s idiom'),
    ('בנו',      32, 24, 'build [for yourselves cities]'),
    ('לטפכם',    32, 24, 'for your little ones — Moses\' order: the children first'),
    ('והיצא',    32, 24, 'and that which has gone out [of your mouth] — THE UTTERANCE RULE (30:3)'),
    ('מפיכם',    32, 24, 'of your mouth'),
    ('תעשו',     32, 24, 'you shall do'),
    ('עבדיך',    32, 25, 'your servants [will do]'),
    ('אדני',     32, 25, 'my lord — for Moses'),
    ('טפנו',     32, 26, 'our little ones — the acceptance\'s order'),
    ('נשינו',    32, 26, 'our wives'),
    ('הגלעד',    32, 26, 'Gilead [the cities of]'),
    ('ויצו',     32, 28, 'and [Moses] commanded — the commission charged'),
    ('יהושע',    32, 28, 'Joshua [son of Nun]'),
    ('ראשי',     32, 28, 'the heads of [the fathers of the tribes] — Joshua 14:1\'s triad'),
    ('יעברו',    32, 29, 'they pass over — the second doubling\'s positive arm'),
    ('ונתתם',    32, 29, 'you shall give [them the land of Gilead]'),
    ('ונאחזו',   32, 30, 'they shall take possessions [among you] — the negative arm\'s outcome'),
    ('כנען',     32, 30, 'Canaan'),
    ('ויענו',    32, 31, 'and they answered'),
    ('דבר',      32, 31, 'has spoken — "that which the LORD has spoken to your servants"'),
    ('נחנו',     32, 32, 'we — the short form (three Bible seats)'),
    ('אחזת',     32, 32, 'the possession of [our inheritance] — 27:7\'s construct'),
    ('ויתן',     32, 33, 'and [Moses] gave — THE GRANT'),
    ('ולחצי',    32, 33, 'and to half [the tribe of Manasseh] — first named at the grant'),
    ('ממלכת',    32, 33, 'the kingdom of [Sihon]'),
    ('סיחן',     32, 33, 'Sihon'),
    ('עוג',      32, 33, 'Og'),
    ('ויבנו',    32, 34, 'and [the sons of Gad] built'),
    ('דיבן',     32, 34, 'Dibon — Dibon Gad (33:45)'),
    ('שופן',     32, 35, 'Atroth-shophan'),
    ('ויגבהה',   32, 35, 'and Jogbehah — with Nobah at Judges 8:11'),
    ('הרן',      32, 36, 'Beth-haran'),
    ('מבצר',     32, 36, 'fortified [cities]'),
    ('בנו',      32, 37, '[the sons of Reuben] built'),
    ('חשבון',    32, 37, 'Heshbon'),
    ('קריתים',   32, 37, 'Kiriathaim'),
    ('נבו',      32, 38, 'Nebo — Moses\' grave (Sotah 13b:20; Onkelos 32:3)'),
    ('מוסבת',    32, 38, 'being changed — their names, one seat'),
    ('שבמה',     32, 38, 'Sibmah'),
    ('מכיר',     32, 39, 'Machir — the sons of Machir son of Manasseh (Genesis 50:23)'),
    ('וילכדה',   32, 39, 'and took it'),
    ('ויורש',    32, 39, 'and dispossessed [the Amorite] — 21:32\'s verb'),
    ('למכיר',    32, 40, 'to Machir — Moses gave Gilead'),
    ('וישב',     32, 40, 'and he dwelt [in it]'),
    ('ויאיר',    32, 41, 'and Jair'),
    ('חותיהם',   32, 41, 'their villages'),
    ('חות',      32, 41, 'Havvoth-[jair]'),
    ('ונבח',     32, 42, 'and Nobah'),
    ('קנת',      32, 42, 'Kenath'),
    ('בנתיה',    32, 42, 'its daughters — the villages (21:25, 21:32)'),
    ('בשמו',     32, 42, 'after his own name'),
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
SPAN = [(32, v) for v in range(1, 43)]
NUMBERS = {v: ink_numbers(verse_words('Num', 32, v)) for _, v in SPAN}
ORDINALS = {v: ink_ordinals(verse_words('Num', 32, v)) for _, v in SPAN}
STARRED = [(v, t) for _, v in SPAN for t in verse_words('Num', 32, v) if t.endswith('*')]
MARKED = [(v, t) for _, v in SPAN for t in verse_words('Num', 32, v) if '%' in t]
INTS = {v: n for v, n in NUMBERS.items() if n}
assert INTS == {11: [20], 13: [40]}, INTS                                                                                # TWO numbers in forty-two verses — no gap, no rule owed
assert not any(o for o in ORDINALS.values()) and STARRED == [] and MARKED == [], (ORDINALS, STARRED, MARKED)
TWENTY, FORTY = INTS[11][0], INTS[13][0]
assert ink_numbers(verse_words('Num', 33, 1)) == [], 'the next chapter opens without a number'
FIRST = {v: words(32, v)[0] for _, v in SPAN}
FRAME_VERBS = [(v, FIRST[v], words(32, v)[1]) for _, v in SPAN if FIRST[v] in ('וידבר', 'ויאמר', 'ויאמרו', 'ויענו')]
assert FRAME_VERBS == [(5, 'ויאמרו', 'אם'), (6, 'ויאמר', 'משה'), (20, 'ויאמר', 'אליהם'), (25, 'ויאמר', 'בני'), (29, 'ויאמר', 'משה'), (31, 'ויענו', 'בני')], FRAME_VERBS
assert not any(w1 == 'יהוה' for _, _, w1 in FRAME_VERBS) and not any(w0 == 'וידבר' for _, w0, _ in FRAME_VERBS), 'NO DIVINE FRAME in the chapter'   # the reading's claim MT32A-01
# the whole-DB phrase census (the seats typed from the measurement print of 2026-09-12 — gad_runner_measure.out)
_V = collections.OrderedDict(); _L = collections.OrderedDict()
for b, c, v, he, lm in db.execute("SELECT v.book, v.chapter, v.verse, w.he, w.lemma FROM words w JOIN verses v ON w.verse_id=v.id ORDER BY v.id, w.idx"):
    _V.setdefault((b, c, v), []).append(strip(he)); _L.setdefault((b, c, v), []).append(lm.split('/')[-1].split(' ')[0] if lm else '')
def seats(phrase):
    p = phrase.split(); n = len(p)
    return ['%s %d:%d' % k for k, ws in _V.items() if any(ws[i:i + n] == p for i in range(len(ws) - n + 1))]
def rx(pattern):
    r = re.compile(pattern)
    return ['%s %d:%d' % k for k, ws in _V.items() if r.search(' ' + ' '.join(ws) + ' ')]
def tok(t, books=None):
    return ['%s %d:%d' % k for k, ws in _V.items() if (books is None or k[0] in books) and t in ws]
TORAH = ('Gen', 'Exod', 'Lev', 'Num', 'Deut')
COMPOUND = rx(r' ל?בני גד ול?בני ראובן ')
assert COMPOUND == ['Num 32:2', 'Num 32:6', 'Num 32:25', 'Num 32:29', 'Num 32:31', 'Num 32:33'], COMPOUND                # THE INK'S COMPOUND PARTY at six seats, Gad first
REUBEN_FIRST = seats('בני ראובן ובני גד')
assert len(REUBEN_FIRST) == 9 and all(s.startswith('Josh ') for s in REUBEN_FIRST) and words(32, 1)[3:6] == ['לבני', 'ראובן', 'ולבני'], (REUBEN_FIRST, words(32, 1))
MUCH_CATTLE = seats('מקנה רב'); PLACE_FOR_CATTLE = seats('מקום מקנה'); LAND_OF_JAZER = seats('ארץ יעזר'); LAND_OF_GILEAD_ART = seats('ארץ הגלעד')
assert MUCH_CATTLE == ['2Chr 26:10', 'Deut 3:19'] and words(32, 1)[:2] == ['ומקנה', 'רב'] and PLACE_FOR_CATTLE == ['Num 32:1'] and LAND_OF_JAZER == ['Num 32:1'], (MUCH_CATTLE, PLACE_FOR_CATTLE, LAND_OF_JAZER)
assert LAND_OF_GILEAD_ART == ['2Kgs 10:33', '2Sam 17:26', 'Josh 22:9', 'Josh 22:13', 'Josh 22:15', 'Num 32:29'], LAND_OF_GILEAD_ART
TRIAD_TO = seats('אל משה ואל אלעזר הכהן ואל נשיאי'); TRIAD_BEFORE = seats('לפני משה ולפני אלעזר הכהן ולפני הנשיאם')
assert TRIAD_TO == ['Num 32:2'] and TRIAD_BEFORE == ['Num 27:2'], (TRIAD_TO, TRIAD_BEFORE)                              # 27:2's triad addressed WITHOUT the halt
FOR_A_POSSESSION = seats('לאחזה'); POSSESSION_OF_OUR = seats('אחזת נחלתנו'); POSSESSION_OF = seats('אחזת נחלה')
assert FOR_A_POSSESSION == ['Deut 32:49', 'Ezek 45:5', 'Ezek 45:8', 'Lev 14:34', 'Lev 25:45', 'Num 32:5', 'Num 32:22', 'Num 32:29'], FOR_A_POSSESSION
assert POSSESSION_OF_OUR == ['Num 32:32'] and POSSESSION_OF == ['Num 27:7'], (POSSESSION_OF_OUR, POSSESSION_OF)
NINE = words(32, 3)
assert NINE == ['עטרות', 'ודיבן', 'ויעזר', 'ונמרה', 'וחשבון', 'ואלעלה', 'ושבם', 'ונבו', 'ובען'] and len(NINE) == 9, NINE
BROTHERS_TO_WAR = seats('האחיכם יבאו למלחמה'); DISCOURAGE = seats('ולמה תנואון')
assert BROTHERS_TO_WAR == ['Num 32:6'] and DISCOURAGE == ['Num 32:7'], (BROTHERS_TO_WAR, DISCOURAGE)
HINDER_SET = ('הניא', 'יניא', 'תנואון', 'ויניאו')                                                                        # THE TOKEN SET, never the letters (12's lesson)
HINDER_TOKENS = [(k, t) for k, ws in _V.items() if k[0] in TORAH for t in ws if t in HINDER_SET]
assert len(HINDER_TOKENS) == 6 and {k[1] for k, _ in HINDER_TOKENS} == {30, 32} and [k[2] for k, _ in HINDER_TOKENS] == [6, 6, 9, 12, 7, 9], HINDER_TOKENS   # six Torah tokens all in 30 and 32 (30:6 twice)
assert tok('תנואתי') == ['Num 14:34'] and tok('הניא') == ['Num 30:6', 'Num 30:12', 'Ps 33:10'], (tok('תנואתי'), tok('הניא'))
KADESH_BARNEA = seats('קדש ברנע'); ESHCOL = seats('נחל אשכול'); TO_SEE = seats('לראות את הארץ'); TO_SCOUT = seats('וירגלו'); TO_SEARCH = seats('ויחפרו'); TO_TOUR = [s for s in seats('לתור') if s.startswith('Num ')]
assert KADESH_BARNEA == ['Deut 1:2', 'Deut 1:19'] and 'ברנע' in words(32, 8) and ESHCOL == ['Num 13:24', 'Num 32:9'] and TO_SEE == ['Num 32:8'], (KADESH_BARNEA, ESHCOL, TO_SEE)
assert TO_SCOUT == ['Deut 1:24', 'Josh 7:2'] and len(TO_SEARCH) == 10 and 'Deut 1:22' in TO_SEARCH and TO_TOUR == ['Num 10:33', 'Num 13:16', 'Num 13:17', 'Num 13:32', 'Num 14:7', 'Num 14:36', 'Num 14:38'], (TO_SCOUT, TO_SEARCH, TO_TOUR)
ANGER_THAT_DAY = seats('ויחר אף יהוה ביום ההוא'); ANGER_AGAINST_ISRAEL = seats('ויחר אף יהוה בישראל'); SWORE_SAYING = seats('וישבע לאמר')
assert ANGER_THAT_DAY == ['Num 32:10'] and ANGER_AGAINST_ISRAEL == ['2Kgs 13:3', 'Judg 2:14', 'Judg 2:20', 'Judg 3:8', 'Judg 10:7', 'Num 25:3', 'Num 32:13'] and SWORE_SAYING == ['Deut 1:34', 'Num 32:10'], (ANGER_THAT_DAY, ANGER_AGAINST_ISRAEL, SWORE_SAYING)
TWENTY_AND_UP = seats('מבן עשרים שנה ומעלה'); SWORE_TO_ABRAHAM = seats('אשר נשבעתי לאברהם ליצחק וליעקב'); FOLLOWED_ME = seats('מלאו אחרי'); FOLLOWED_LORD = seats('מלאו אחרי יהוה')
assert len(TWENTY_AND_UP) == 23 and {'Exod 30:14', 'Num 1:3', 'Num 14:29', 'Num 32:11'} <= set(TWENTY_AND_UP), TWENTY_AND_UP                 # THE CENSUS FORMULA — twenty-three seats
assert SWORE_TO_ABRAHAM == ['Deut 34:4', 'Exod 33:1', 'Num 32:11'] and FOLLOWED_ME == ['Num 32:11', 'Num 32:12'] and FOLLOWED_LORD == ['Num 32:12'], (SWORE_TO_ABRAHAM, FOLLOWED_ME, FOLLOWED_LORD)
KENIZZITE = seats('הקנזי'); SON_OF_KENAZ = seats('בן קנז')
assert KENIZZITE == ['Gen 15:19', 'Josh 14:6', 'Josh 14:14', 'Num 32:12'] and SON_OF_KENAZ == ['Josh 15:17', 'Judg 1:13', 'Judg 3:9', 'Judg 3:11'], (KENIZZITE, SON_OF_KENAZ)
FORTY_YEARS_NUM = [s for s in seats('ארבעים שנה') if s.startswith('Num ')]; GENERATION_CONSUMED = seats('עד תם כל הדור'); EVIL_FORMULA = seats('הרע בעיני יהוה')
assert FORTY_YEARS_NUM == ['Num 14:33', 'Num 14:34', 'Num 32:13'] and GENERATION_CONSUMED == ['Deut 2:14', 'Num 32:13'], (FORTY_YEARS_NUM, GENERATION_CONSUMED)
assert len(EVIL_FORMULA) == 53 and 'Num 32:13' in EVIL_FORMULA and 'וינעם' in words(32, 13), (len(EVIL_FORMULA), words(32, 13))               # the Kings' formula's fifty-three seats; the causative's one Torah seat
BROOD = seats('תרבות'); SINFUL_MEN = seats('אנשים חטאים'); TO_ADD = seats('לספות'); FIERCE_ANGER = seats('חרון אף יהוה'); DESTROY = seats('ושחתם לכל העם הזה')
assert BROOD == ['Num 32:14'] and SINFUL_MEN == ['Num 32:14'] and TO_ADD == ['Num 32:14'] and DESTROY == ['Num 32:15'], (BROOD, SINFUL_MEN, TO_ADD, DESTROY)
assert FIERCE_ANGER == ['2Chr 28:11', 'Jer 4:8', 'Jer 25:37', 'Jer 30:24', 'Num 25:4', 'Num 32:14', 'Zeph 2:2'], FIERCE_ANGER
FOLDS = seats('גדרת צאן'); CITIES_OUR = seats('וערים לטפנו'); CITIES_YOUR = seats('ערים לטפכם'); NOT_RETURN = seats('לא נשוב אל בתינו'); GIVES_REST = seats('עד אשר יניח יהוה')
assert FOLDS == ['Num 32:16'] and CITIES_OUR == ['Num 32:16'] and CITIES_YOUR == ['Num 32:24'] and NOT_RETURN == ['Num 32:18'] and GIVES_REST == ['Deut 3:20', 'Josh 1:15'], (FOLDS, CITIES_OUR, CITIES_YOUR, NOT_RETURN, GIVES_REST)
ARM_SET = ('נחלץ', 'תחלצו', 'חלוץ', 'חלוצים')                                                                            # the final letter its own code point (11's lesson): the set typed whole
ARM_TOKENS = [(v, t) for _, v in SPAN for t in words(32, v) if t in ARM_SET]
assert ARM_TOKENS == [(17, 'נחלץ'), (20, 'תחלצו'), (21, 'חלוץ'), (27, 'חלוץ'), (29, 'חלוץ'), (30, 'חלוצים'), (32, 'חלוצים')] and len(ARM_TOKENS) == 7, ARM_TOKENS
assert 'חמשים' in words(1, 14, 'Josh') and 'חמשים' in words(4, 12, 'Josh') and 'חלוצי' in words(4, 13, 'Josh') and 'חלוצים' in words(3, 18, 'Deut'), 'Joshua\'s armed in the consonants of fifty'
BEFORE_THE_LORD_32 = [v for _, v in SPAN for i in range(len(words(32, v)) - 1) if words(32, v)[i:i + 2] == ['לפני', 'יהוה']]
assert BEFORE_THE_LORD_32 == [20, 21, 22, 22, 27, 29, 32] and len(BEFORE_THE_LORD_32) == 7, BEFORE_THE_LORD_32           # seven tokens in 32:20-32
BEFORE_LORD_FOR_WAR = seats('לפני יהוה למלחמה'); SUBDUED_BEFORE_LORD = seats('ונכבשה הארץ לפני יהוה'); SUBDUED_BEFORE_YOU = seats('ונכבשה הארץ לפניכם')
assert BEFORE_LORD_FOR_WAR == ['Josh 4:13', 'Num 32:20', 'Num 32:27'] and SUBDUED_BEFORE_LORD == ['1Chr 22:18', 'Num 32:22'] and SUBDUED_BEFORE_YOU == ['Num 32:29'], (BEFORE_LORD_FOR_WAR, SUBDUED_BEFORE_LORD, SUBDUED_BEFORE_YOU)
CLEAR = seats('נקיים מיהוה ומישראל'); SIN_FIND = seats('חטאתכם אשר תמצא אתכם'); FOUND_INIQUITY = seats('מצא את עון עבדיך')
assert CLEAR == ['Num 32:22'] and SIN_FIND == ['Num 32:23'] and FOUND_INIQUITY == ['Gen 44:16'], (CLEAR, SIN_FIND, FOUND_INIQUITY)
UTTERANCE_32 = seats('והיצא מפיכם תעשו'); UTTERANCE_30 = seats('ככל היצא מפיו יעשה')
LEMMA_PAIR = ['%s %d:%d' % k for k, ls in _L.items() if any(ls[i] == '3318' and ls[i + 1] == '6310' for i in range(len(ls) - 1))]
assert UTTERANCE_32 == ['Num 32:24'] and UTTERANCE_30 == ['Num 30:3'], (UTTERANCE_32, UTTERANCE_30)
assert LEMMA_PAIR == ['Esth 7:8', 'Isa 45:23', 'Isa 55:11', 'Jer 44:17', 'Job 15:13', 'Josh 6:10', 'Judg 11:36', 'Num 30:3', 'Num 32:24'], LEMMA_PAIR   # 'goes out' + 'mouth' adjacent: nine seats, the Torah's two, Jephthah's daughter among the seven
SERVANTS_WILL_DO = seats('עבדיך יעשו כאשר אדני מצוה'); MY_LORD_NUM = tok('אדני', ('Num',))
assert SERVANTS_WILL_DO == ['Num 32:25'] and MY_LORD_NUM == ['Num 11:28', 'Num 12:11', 'Num 14:17', 'Num 32:25', 'Num 32:27', 'Num 36:2'], (SERVANTS_WILL_DO, MY_LORD_NUM)
TRIAD_32 = seats('אלעזר הכהן ואת יהושע בן נון ואת ראשי אבות המטות'); TRIAD_JOSH = seats('אלעזר הכהן ויהושע בן נון וראשי אבות המטות'); TRIAD_JOSH21 = seats('אלעזר הכהן ואל יהושע בן נון ואל ראשי אבות המטות')
assert TRIAD_32 == ['Num 32:28'] and TRIAD_JOSH == ['Josh 14:1'] and 'Josh 21:1' in TRIAD_JOSH21, (TRIAD_32, TRIAD_JOSH, TRIAD_JOSH21)          # THE COMMISSION NAMED — Joshua 14:1's dividers word for word
TAKE_AMONG_YOU = seats('ונאחזו בתככם'); HAMOR = seats('והאחזו בה'); WE_SHORT = seats('נחנו')
assert TAKE_AMONG_YOU == ['Num 32:30'] and HAMOR == ['Gen 34:10'] and WE_SHORT == ['Gen 42:11', 'Lam 3:42', 'Num 32:32'], (TAKE_AMONG_YOU, HAMOR, WE_SHORT)
KINGDOM_SIHON = seats('ממלכת סיחן'); KINGDOM_OG = seats('ממלכת עוג'); HALF_MANASSEH = rx(r' \S*חצי (ה)?שבט (ה)?מנשה ')
assert KINGDOM_SIHON == ['Num 32:33'] and KINGDOM_OG == ['Deut 3:4', 'Deut 3:10', 'Deut 3:13', 'Num 32:33'] and len(HALF_MANASSEH) == 20 and HALF_MANASSEH[-1] == 'Num 32:33' and 'Josh 22:9' in HALF_MANASSEH, (KINGDOM_SIHON, KINGDOM_OG, HALF_MANASSEH)   # twenty seats with the tribe-noun shevet; 34:14-15 use the OTHER tribe-noun (matteh) — measured at the first run, the design's '34:14' retyped
GAD_BUILT = ' '.join(words(32, 34) + words(32, 35) + words(32, 36)); REUBEN_BUILT = ' '.join(words(32, 37) + words(32, 38))
assert GAD_BUILT == 'ויבנו בני גד את דיבן ואת עטרת ואת ערער ואת עטרת שופן ואת יעזר ויגבהה ואת בית נמרה ואת בית הרן ערי מבצר וגדרת צאן', GAD_BUILT
assert REUBEN_BUILT == 'ובני ראובן בנו את חשבון ואת אלעלא ואת קריתים ואת נבו ואת בעל מעון מוסבת שם ואת שבמה ויקראו בשמת את שמות הערים אשר בנו', REUBEN_BUILT
GAD_CITIES = ['דיבן', 'עטרת', 'ערער', 'עטרת שופן', 'יעזר', 'ויגבהה', 'בית נמרה', 'בית הרן']                              # EIGHT — the tokens between the object marks (the print's)
REUBEN_CITIES = ['חשבון', 'אלעלא', 'קריתים', 'נבו', 'בעל מעון', 'שבמה']                                                  # SIX
assert all(c in GAD_BUILT for c in GAD_CITIES) and all(c in REUBEN_BUILT for c in REUBEN_CITIES) and len(GAD_CITIES) == 8 and len(REUBEN_CITIES) == 6
NAMES_CHANGED = seats('מוסבת שם')
assert NAMES_CHANGED == ['Num 32:38'] and words(33, 45)[-2:] == ['בדיבן', 'גד'] and words(33, 46)[1:3] == ['מדיבן', 'גד'], (NAMES_CHANGED, words(33, 45), words(33, 46))   # Dibon Gad the itinerary's witness
assert {'חשבון', 'דיבון'} <= set(words(13, 17, 'Josh')) and 'ומחשבון' in words(13, 26, 'Josh') and 'ובית' in words(13, 20, 'Josh') and 'פעור' in words(13, 20, 'Josh'), 'the two crossed cities in Joshua 13; Beth-peor Reuben\'s'
SONS_OF_MACHIR = seats('בני מכיר בן מנשה'); MACHIR_SON = seats('מכיר בן מנשה'); HAVVOTH = seats('חות יאיר'); JAIR_SON = seats('יאיר בן מנשה')
assert SONS_OF_MACHIR == ['Gen 50:23', 'Num 32:39'] and MACHIR_SON == ['1Chr 7:17', 'Gen 50:23', 'Josh 13:31', 'Josh 17:3', 'Num 27:1', 'Num 32:39', 'Num 36:1'], (SONS_OF_MACHIR, MACHIR_SON)
assert HAVVOTH == ['1Chr 2:23', '1Kgs 4:13', 'Deut 3:14', 'Josh 13:30', 'Judg 10:4', 'Num 32:41'] and JAIR_SON == ['1Kgs 4:13', 'Deut 3:14'], (HAVVOTH, JAIR_SON)
DAUGHTERS_NUM = tok('בנתיה', ('Num',)); NOBAH = seats('נבח'); KENATH = seats('קנת'); WENT_AND_TOOK = seats('הלך וילכד'); AMORITE_IN_IT = seats('האמרי אשר בה')
assert DAUGHTERS_NUM == ['Num 21:25', 'Num 21:32', 'Num 32:42'] and NOBAH == ['Num 32:42'] and KENATH == ['1Chr 2:23', 'Num 32:42'] and AMORITE_IN_IT == ['Num 32:39'], (DAUGHTERS_NUM, NOBAH, KENATH, AMORITE_IN_IT)
assert 'Num 32:41' in WENT_AND_TOOK and 'Num 32:42' in WENT_AND_TOOK and 'ויגבהה' in words(32, 35) and 'ויגבהה' in words(8, 11, 'Judg') and 'לנבח' in words(8, 11, 'Judg'), (WENT_AND_TOOK, words(8, 11, 'Judg'))
# the retellings' numbers by the same parser (typed from the print)
RETOLD = {k: ink_numbers(verse_words(*k)) for k in (('Josh', 4, 13), ('1Chr', 5, 18), ('1Chr', 2, 21), ('1Chr', 2, 22), ('1Chr', 2, 23), ('1Kgs', 4, 13), ('Josh', 13, 30), ('Deut', 3, 4), ('Judg', 10, 4), ('Deut', 2, 14), ('Num', 14, 29), ('Num', 26, 7), ('Num', 26, 18), ('Num', 26, 34), ('Josh', 7, 5))}
assert RETOLD == {('Josh', 4, 13): [40000], ('1Chr', 5, 18): [44760], ('1Chr', 2, 21): [60], ('1Chr', 2, 22): [23], ('1Chr', 2, 23): [60], ('1Kgs', 4, 13): [60], ('Josh', 13, 30): [60], ('Deut', 3, 4): [60], ('Judg', 10, 4): [30, 30, 30], ('Deut', 2, 14): [38], ('Num', 14, 29): [20], ('Num', 26, 7): [43730], ('Num', 26, 18): [40500], ('Num', 26, 34): [52700], ('Josh', 7, 5): [36]}, RETOLD
FORTY_THOUSAND, CHRONICLES_COUNT, THIRTY_EIGHT, THIRTY_SIX = RETOLD[('Josh', 4, 13)][0], RETOLD[('1Chr', 5, 18)][0], RETOLD[('Deut', 2, 14)][0], RETOLD[('Josh', 7, 5)][0]

# ---- THE CALLEES (live import edges; the design's cells by name) ----
VW_UTTER = VW.the_man({'ask': 'all_that_proceeds'}, VW.DATA); VW_FRAME = VW.the_man({'ask': 'frame'}, VW.DATA)          # THE CALL: the utterance rule's own cell (30:3) — its effect the debit's
assert VW_UTTER[0].startswith("the vow's fulfilment") and VW_UTTER[1] == ['commanded'] and VW_FRAME[1] == ['commanded'], (VW_UTTER, VW_FRAME)
assert VW.DATA['vow_support_base']['value'] == 'vowed_thing_only', VW.DATA['vow_support_base']
SL_SET = SL.decree({'ask': 'set'}, SL.DATA); SL_EXC = SL.decree({'ask': 'exceptions'}, SL.DATA); SL_DUE = SL.decree({'ask': 'due'}, SL.DATA)   # THE CALL: the oath's set, its exceptions, its due
SL_COUNT_FROM = SL.decree({'ask': 'count_from'}, SL.DATA); SL_DAY_YEAR = SL.decree({'ask': 'day_for_year'}, SL.DATA); SL_CALEB = SL.decree({'ask': 'caleb_entitlement'}, SL.DATA)
SL_DEATHS = SL.decree({'ask': 'deaths_ceased'}, SL.DATA); SL_PARDON = SL.decree({'ask': 'pardon'}, SL.DATA); SL_EDGES = SL.decree({'ask': 'set_edges'}, SL.DATA); SL_CHILDLESS = SL.decree({'ask': 'joshua_childless'}, SL.DATA)
SL_NAME = SL.spies({'ask': 'joshua_name'}, SL.DATA); SL_EQUAL = SL.spies({'ask': 'joshua_caleb_equal'}, SL.DATA); SL_SEND = SL.spies({'ask': 'send_for_yourself'}, SL.DATA); SL_ESHCOL = SL.spies({'ask': 'eshcol'}, SL.DATA); SL_HEBRON = SL.spies({'ask': 'hebron_visitor'}, SL.DATA)
assert SL_SET[0].startswith('603550') and SL_SET[1] == ['sentence_pronounced'] and SL_EXC[0].startswith('Caleb and Joshua (14:24, 14:30)') and SL_EXC[1] == ['exempt'], (SL_SET, SL_EXC)
assert SL_DUE[0].startswith('(40, 5, 9)') and SL_DUE[1] == ['carcasses_fall_in_the_wilderness'] and SL_COUNT_FROM[0].startswith('40 - 38 = 2') and SL_DAY_YEAR[0].startswith('[40, 40]'), (SL_DUE, SL_COUNT_FROM, SL_DAY_YEAR)
assert SL_CALEB[0].startswith('holding_owed — Hebron; PAID at Josh 14:13-14') and SL_CALEB[1] == ['holding_owed'] and SL_DEATHS[0].startswith('the fifteenth of Av of the fortieth year') and SL_PARDON[1] == ['pardoned'], (SL_CALEB, SL_DEATHS, SL_PARDON)
assert SL_EDGES[0].startswith('under twenty and over sixty outside') and SL_CHILDLESS[0].startswith('no son') and SL_NAME[0].startswith('Hoshea to Joshua at 13:16') and SL_EQUAL[0].startswith('equal'), (SL_EDGES, SL_CHILDLESS, SL_NAME, SL_EQUAL)
assert SL_SEND[0].startswith("at Moses' discretion") and SL_ESHCOL[0].startswith('named after the cluster') and SL_HEBRON[0].startswith('Caleb alone at the graves'), (SL_SEND, SL_ESHCOL, SL_HEBRON)
assert SL.FORTY_YEARS == [FORTY] and SL.DATA['count_from']['value'] == 'the exodus' and SL.DATA['deaths_ceased']['value'] == (40, 5, 15) and SL.DATA['spies_share']['value'] == 'no share', (SL.FORTY_YEARS, SL.DATA['count_from'])
CK_EAST = CK.well_and_kings({'ask': 'land_east'}, CK.DATA); CK_DELTA = CK.well_and_kings({'ask': 'deut3_delta'}, CK.DATA); CK_OG = CK.well_and_kings({'ask': 'og_lore'}, CK.DATA)   # THE CALL: the grant's source
CK_SIHON = CK.well_and_kings({'ask': 'sihon_purified'}, CK.DATA); CK_SPY = CK.well_and_kings({'ask': 'spy_verb'}, CK.DATA)
assert CK_EAST[0].startswith('the land east of the Jordan possessed') and CK_EAST[1] == ['land_possessed', 'kings_smitten'] and CK_DELTA[0].startswith('Deuteronomy 3:1-3 = 21:33-35'), (CK_EAST, CK_DELTA)
assert CK_OG[1] == ['fear_not_promised'] and CK_SIHON[1] == ['land_possessed'] and CK_SPY[0].startswith('"to spy out Jazer"'), (CK_OG, CK_SIHON, CK_SPY)
assert CK.DATA['og_lore']['value'] == 'sihons_brother_of_the_rephaim' and CK.DATA['sihon_purified']['value'] == 'ammon_and_moab_purified_through_sihon', CK.DATA['og_lore']
C2_TOTAL = C2.the_roll({'ask': 'total'}, C2.DATA); C2_LOT = C2.the_land({'ask': 'by_lot'}, C2.DATA); C2_THIRTEEN = C2.the_land({'ask': 'thirteen_tribes'}, C2.DATA)   # THE CALL: the counts, the lot
C2_TEN = C2.the_land({'ask': 'ten_parts'}, C2.DATA); C2_MORASHA = C2.the_land({'ask': 'morasha'}, C2.DATA); C2_HELD = C2.the_land({'ask': 'possession_before_assignment'}, C2.DATA); C2_EXC = C2.the_rolls({'ask': 'except_caleb_joshua'}, C2.DATA)
assert C2_TOTAL[0].startswith('601730') and C2_TOTAL[1] == ['counted'] and C2_LOT[0].startswith('the place by lot') and C2_LOT[1] == ['commanded'], (C2_TOTAL, C2_LOT)
assert C2_THIRTEEN[0].startswith('twelve now, thirteen to come') and C2_TEN[1] == ['holding_owed'] and C2_MORASHA[0].startswith('morasha both ways') and C2_HELD[0].startswith('in possession before assignment') and C2_EXC[1] == ['exempt'], (C2_THIRTEEN, C2_TEN, C2_MORASHA, C2_HELD, C2_EXC)
assert (C2.C26['reuben'], C2.C26['gad'], C2.C26['manasseh']) == (RETOLD[('Num', 26, 7)][0], RETOLD[('Num', 26, 18)][0], RETOLD[('Num', 26, 34)][0]) and C2.FAMILIES['manasseh'][0] == 'Machir', (C2.C26, C2.FAMILIES['manasseh'])
assert C2.DATA['thirteen_tribes']['value'] == 'twelve_now_thirteen_to_come' and C2.DATA['division_by']['value'] == 'tribes', C2.DATA['division_by']
TWO_AND_A_HALF = C2.C26['reuben'] + C2.C26['gad'] + C2.C26['manasseh'] // 2
assert TWO_AND_A_HALF == 110580, TWO_AND_A_HALF                                                                          # 43,730 + 40,500 + 52,700 / 2 — the ink's own ratio against Joshua 4:13's forty thousand
BM_THRESH = BM.census({'ask': 'threshold'}, BM.DATA); BM_ORDERS = BM.census({'ask': 'orders'}, BM.DATA)                  # THE CALL: the census formula; Gad's place in the camps
assert BM_THRESH[0] == 'twenty years and upward, the host' and BM_THRESH[1] == ['commanded'] and BM_ORDERS[0].startswith('three orders in the portion; Gad moves from eleventh to third'), (BM_THRESH, BM_ORDERS)
assert (BM.TRIBES.index('reuben'), BM.TRIBES.index('gad'), BM.TRIBES.index('manasseh')) == (0, 2, 7), BM.TRIBES

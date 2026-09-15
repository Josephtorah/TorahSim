import os as _os
_ROOT = _os.path.normpath(_os.path.join(_os.path.dirname(_os.path.abspath(__file__)), '..', '..'))   # THE PORTABLE REPO (2026-09-15): the repo root from this file's own place
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


# ===== THE DATA CHANNEL — the parameter rows the ink leaves open (motion 2's recorded settings) =========
DATA = {
    'the_order_of_the_offer': {'value': 'cattle_first_children_first', 'settings': {'cattle_first_children_first': "the tribes: 'folds for our cattle ... and cities for our little ones' (32:16); Moses: 'cities for your little ones and folds for your sheep' (32:24); the acceptance 'our little ones, our wives, our cattle and all our beasts' (32:26) — the ink's two orders, read off the tokens; the Tanchuma OUTSIDE the declared spine, no rabbinic row cited (THE LINK REVIEW LAW)"},
                               'source': "32:16 against 32:24 — the reversal the ink's own"},
    'the_oath_supplied': {'value': 'he_swore_supplied_by_the_retelling', 'settings': {'he_swore_supplied_by_the_retelling': "'and the LORD's anger burned on that day, and he SWORE, saying' (32:10) — chapter 14 has 'as I live' (14:21, 28) and no oath-verb; Deuteronomy 1:34 supplies it too ('and he swore, saying' at the two seats); the shelf: 'no' and 'yes' can be oaths, doubled (Shevuot 36a:13-14 — credited)", 'as_i_live': "the oath's own form at 14:21, 28 — 'as I live' (SL.decree('as_i_live') the shelach runner's row: Rava's 'you have given Me life with your words')"},
                          'source': "32:10 'and he swore' against 14:21, 28 — the verb's two seats (Deuteronomy 1:34 the other) computed"},
    'caleb_the_kenizzite': {'value': 'genesis_15_19s_nation_as_a_gentilic', 'settings': {'genesis_15_19s_nation_as_a_gentilic': "'the Kenizzite' at Genesis 15:19 (the ten nations), Numbers 32:12 and Joshua 14:6, 14 — Caleb's gentilic the nation's name; Othniel 'son of Kenaz' (Joshua 15:17; Judges 1:13, 3:9, 3:11) — the ink's four seats", 'the_stepfather_kenaz': "the shelf's reading elsewhere (Sotah 11b; Temurah 16a) — Kenaz Caleb's stepfather: NO ROW of this docket carries it; the ink's arm alone here"},
                            'source': "32:12 'Caleb son of Jephunneh the Kenizzite' — the gentilic's four Bible seats computed"},
    'doubled_condition': {'value': 'required_r_meir', 'settings': {'required_r_meir': "R. Meir: any condition NOT DOUBLED like the condition of the sons of Gad and Reuben is no condition — 32:29 then 32:30 the proof; 'in the land of Canaan' superfluous, so it teaches the doubling (Mishnah Kiddushin 3:4 = 61a:9; 61a:11-61b:1); the corollary — no inference of the unstated arm (Nedarim 11a:2; Shevuot 36a:25)", 'not_required_r_chanina': "R. Chanina ben Gamliel: the doubling was needed there for its own sake — else they would forfeit even Canaan; an ordinary condition needs no second side (Mishnah Kiddushin 3:4; 61a:10); the parable of the father's three sons (61b:3-4); the two positions dated (61b:5-8)", 'scope': "R. Meir refuses the inference in MONETARY matters only — in ritual matters he accepts it (Shevuot 36a:27); or nowhere — the sotah's 'hinnaki' written, 'chinnaki' read (36a:29; Kiddushin 62a:2-3)"},
                          'source': "32:20-23 and 32:29-30 — the condition doubled TWICE in the chapter (the reading's claim MT32A-06, MT32A-08); the exemplar's kin on the shelf: Cain (Genesis 4:7), Eliezer (24:41), Leviticus 26, Isaiah 1:19-20, the sotah, the heifer (Kiddushin 61b:9-62a:7)"},
    'the_conditions_four_limbs': {'value': 'five_limbs_read_off_this_chapter', 'settings': {'five_limbs_read_off_this_chapter': "FROM WHERE DO WE LEARN THE LAWS OF ALL CONDITIONS? from the condition of the sons of Gad and Reuben (Rava, Gittin 75a:11): (1) DOUBLED — R. Meir (Kiddushin 3:4); (2) THE CONDITION BEFORE THE ACTION — 'and you shall give them the land of Gilead' after the 'if' (Gittin 75a:12; Mishnah Bava Metzia 94a:3; Abba Chalafta in R. Meir's name, 94a:7; Rava's application 75a:13, 75b:5); (3) THE POSITIVE BEFORE THE NEGATIVE — 32:29 before 32:30 (Gittin 75b:6-8); (4) THE CONDITION'S MATTER AND THE ACT'S DISTINCT — to fight, to receive Gilead (Rav Adda bar Ahava, Gittin 75a:14-75b:1); (5) A CONDITION THAT CAN BE FULFILLED — R. Yehuda ben Teima against the Rabbis, THE RULING as him (Bava Metzia 94a:11-14; R. Yochanan's 'in one's power', Kiddushin 62a:12)", 'from_now': "'ON CONDITION' IS LIKE 'FROM NOW' — the act takes effect at once though the condition is fulfilled later (Rav Huna in Rav's name, Gittin 75b:2): the grant of 32:33 given now under the condition — the transfer written at the grant, the debit open beside it", 'counter_to_the_torah': "a condition counter to the Torah on a non-monetary matter is void; in monetary matters the parties may agree (Mishnah Bava Metzia 94a:2; R. Yehuda 94a:5)"},
                                  'source': "32:20-24, 32:29-30 — the chapter the exam's source for the whole law of conditions (the docket's LAW rows)"},
    'negative_arm_outcome': {'value': 'canaan_only_or_gilead_shared', 'settings': {'canaan_only_or_gilead_shared': "'they shall take possessions among you in the land of Canaan' (32:30) — R. Chanina ben Gamliel: without 'in the land of Canaan' one would read Gilead shared and no inheritance in Canaan; R. Meir: 'among you' means wherever you took possession, Canaan included (Kiddushin 61b:2); the parable's version — Gilead anyway, the doubling for the rest (61b:5-8)", 'your_sin_will_find_you': "'and if you do not do so, behold, you have sinned against the LORD, and know your sin which will find you' (32:23) — the ink's first negative outcome; Judah's idiom 'God has found out the iniquity of your servants' (Genesis 44:16 — the idiom's two seats): NO ROW of the docket reads it — the ink's arm alone"},
                             'source': "32:23 and 32:30 — the negative arm's two outcomes in the ink; the shelf reads 32:30 (five citations)"},
    'the_clearance': {'value': 'justified_before_people_as_before_the_omnipresent', 'settings': {'justified_before_people_as_before_the_omnipresent': "Mishnah Shekalim 3:2: the one who collects from the treasury chamber enters with no cuffed garment, shoe, sandal, phylacteries or amulet — lest he become poor or rich and be suspected: A PERSON MUST APPEAR JUSTIFIED BEFORE PEOPLE AS BEFORE THE OMNIPRESENT, 'and you shall be clear before the LORD and before Israel' (32:22); the House of Garmu's coarse bread and the House of Avtinas's unperfumed brides — beyond reproach AND beyond suspicion (Yoma 38a:9, 38a:12); the charity collectors sell to others and change money with others (Pesachim 13a:13-14)"},
                      'source': "32:22 'clear before the LORD and before Israel' — one Bible seat; 1 Chronicles 22:18 'subdued before the LORD and before his people' the double in Chronicles' ink; the release Joshua 22:4 outside the Torah"},
    'half_manassehs_stipulation': {'value': 'silent_in_32_included_by_the_retellings', 'settings': {'silent_in_32_included_by_the_retellings': "half the tribe of Manasseh FIRST NAMED at the grant (32:33 — 'and to half the tribe of Manasseh son of Joseph'), no stipulation spoken to it in the chapter; Deuteronomy 3:18-20 ('you shall pass over armed before your brothers' after 3:12-13's three grantees), Joshua 1:12-15 ('to the Reubenites, the Gadites and the half tribe of Manasseh'), 4:12 (the three crossed armed) extend the crossing; Joshua 22:1-9 releases the three; Joshua 17:5-6's 'ten parts fell to Manasseh, BESIDE the land of Gilead and Bashan beyond the Jordan' (Bava Batra 118b:8) the shelf's line between the tribe's ten parts and its east; the phrase with the tribe-noun of 32:33 at twenty seats (Deuteronomy 3:13; Joshua 1:12, 4:12, 12:6, 13:7, 13:29, 18:7, 22:7-21; 1 Chronicles 5:18-26, 12:38, 27:20) — 34:14-15 use the OTHER tribe-noun (measured)"},
                                   'source': "32:33 — the grant's third party; the phrase's seats computed (34:14-15 the next)"},
    'the_forty_thousand': {'value': 'about_forty_thousand_of_110580', 'settings': {'about_forty_thousand_of_110580': "Joshua 4:13 'about forty thousand armed for war passed over before the LORD' — the parser's [40000] against the two and a half's second-census count 43,730 + 40,500 + 52,700 / 2 = 110,580 (26:7, 18, 34 — the population table's rows; C2.C26 by CALL) and 1 Chronicles 5:18's 44,760 'that went out to war' (the parser's); the ink's own ratio — NO ROW of the docket reads it"},
                           'source': "Joshua 4:13; 1 Chronicles 5:18; Numbers 26:7, 18, 34 — the numbers by the same parser (RETOLD)"},
    'the_two_crossed_cities': {'value': 'dibon_and_heshbon_between_the_tribes', 'settings': {'dibon_and_heshbon_between_the_tribes': "Gad built Dibon (32:34) and Reuben built Heshbon (32:37); Joshua 13:17 lists Heshbon AND Dibon in Reuben's allotment, 13:26 runs Gad's border 'from Heshbon' (21:39 Heshbon a Levite city 'from the tribe of Gad'); 'Dibon Gad' the itinerary's own witness (33:45-46); Beth-peor Reuben's (Joshua 13:20 — Moses' grave 'opposite Beth-peor', Deuteronomy 34:6); the prophets name ten of the chapter's cities as Moab's (Isaiah 15-16, Jeremiah 48, Ezekiel 25:9) — RUN_CITATIONS of the later hold"},
                               'source': "32:34-38 against Joshua 13:15-28 — computed on the DB"},
    'jairs_lineage': {'value': 'son_of_manasseh_and_hezrons_grandson', 'settings': {'son_of_manasseh_and_hezrons_grandson': "'Jair son of Manasseh' (32:41; Deuteronomy 3:14; 1 Kings 4:13) — the ink's first account; 1 Chronicles 2:21-22: Hezron of Judah at sixty took Machir's daughter and begot Segub, and Segub begot Jair, 'who had twenty-three cities in the land of Gilead' (the parser's [60], [23]) — the ink's second account: Manasseh's by the mother, Judah's by the father; 2:23 'Geshur and Aram took Havvoth-jair from them, with Kenath and its daughters, sixty cities' (the parser's [60]); THE HOMOGRAPH TRAPS: the judge Jair with thirty sons, thirty asses, thirty cities 'called Havvoth-jair to this day' (Judges 10:3-5 — the parser's [30, 30, 30]), Mordecai's ancestor (Esther 2:5), Elhanan's father (1 Chronicles 20:5)"},
                      'source': "32:41 'Jair son of Manasseh' — Havvoth-jair's six seats computed; the two lineages the ink's own, no docket row"},
    'jair_and_machir_survived': {'value': 'born_in_jacobs_days_entered_the_land', 'settings': {'born_in_jacobs_days_entered_the_land': "the baraita: Jair son of Manasseh and Machir son of Manasseh were born in Jacob's days and did not die until Israel entered the land — 'about thirty-six men' at Ai (Joshua 7:5; the parser's [36]): R. Yehuda literally thirty-six; R. Nechemya: 'ABOUT' — Jair alone, equal to the majority of the Sanhedrin (Bava Batra 121b:9-10); Jair already old at the decree — the decree not on those over sixty (Rav Acha bar Yaakov, 121b:11; SL.decree('set_edges') by CALL); Machir's sons 'born on Joseph's knees' (Genesis 50:23 — the registry's collective, the ink's own witness)"},
                                 'source': "32:39-41 — the chapter's two conquerors on the shelf as the exodus generation's survivors (the docket's rows, credited to the second census's)"},
    'moses_grave': {'value': 'reubens_nebo_gads_field', 'settings': {'reubens_nebo_gads_field': "R. Yehuda: WHERE DID MOSES DIE? in Reuben's portion — 'Moses went up ... to Mount Nebo' (Deuteronomy 34:1), and Nebo is Reuben's: 'the children of Reuben built ... Nebo' (32:37-38; Sotah 13b:20); buried in Gad's — 'there a portion of the lawgiver is hidden' (Deuteronomy 33:21; the Sifrei 106:1 on 32:37-38 — credited at the reading); ONKELOS 32:3: 'Nebo, the burial place of Moses' — the same reading in the translation's own words"},
                    'source': "32:37-38 Nebo among Reuben's six — the docket's row (Sotah 13b:20) and the reading's Onkelos line"},
    'the_land_east_status': {'value': 'by_moses_word_not_by_lot_held_before_assignment', 'settings': {'by_moses_word_not_by_lot_held_before_assignment': "the east given by Moses' word (32:33 'and Moses gave to them'), not by the lot of 26:55 (Canaan's — C2.the_land('by_lot') by CALL: 'the place by lot — Joshua 14-19 the run'; israel_people's OPEN commanded divide_the_land not this chapter's run); ERETZ YISRAEL HELD BEFORE ASSIGNMENT (Rabba, Bava Batra 119a:1, 119a:5 — C2.the_land('possession_before_assignment'): 'the rows are holdings before the lot') — the standing the word 'a possession' carries at 32:5, 22, 29, 32; the exodus generation BEQUEATH AND DO NOT INHERIT (119b:3-4 — C2 'morasha'); Joshua 22:9 'the land of Gilead, the land of their possession, which they had possessed by the commandment of the LORD by the hand of Moses' the release's own words"},
                             'source': "32:33 — the grant's timing and standing; the second census runner's rows READ by CALL"},
    'count_from': {'value': SL.DATA['count_from']['value'], 'settings': SL.DATA['count_from']['settings'],
                   'source': "32:13 'forty years' — SL's row READ by CALL: the forty from the exodus (Deuteronomy 2:14's thirty-eight from Kadesh — the parser's [38])"},
    'deaths_ceased': {'value': SL.DATA['deaths_ceased']['value'], 'settings': SL.DATA['deaths_ceased']['settings'],
                      'source': "32:13 'until all the generation was consumed' — SL's row READ by CALL: the fifteenth of Av of the fortieth year (Bava Batra 121a:9-121b:1)"},
}


# ===== F1: THE REQUEST (Num 32:1-5) ==========================================================================
def the_request(case, data):
    del P[:]
    ask = case['ask']
    if ask == 'the_parties':
        ink('32:1-2', '"the sons of Reuben and the sons of Gad" (32:1 — Reuben first HERE ALONE); "the sons of Gad and the sons of Reuben" at %s — THE INK\'S COMPOUND PARTY, Gad first at every seat; Reuben first at the nine Joshua seats %s' % (COMPOUND, len(REUBEN_FIRST)))
        move('cold_run_bamidbar (CALL) — BM.census(orders) = %s' % BM_ORDERS[0], "Gad's place in the camps the bamidbar runner's own note; Reuben the firstborn (BM.TRIBES index 0)")
        return out("the sons of Gad and the sons of Reuben — the ink's compound at six seats (32:2, 6, 25, 29, 31, 33), Gad first; Reuben first at 32:1 alone", ['plea_made'])
    if ask == 'much_cattle':
        ink('32:1', '"and much cattle, very numerous" — %s; "a place for cattle" %s (one seat); "the land of Jazer" %s (one seat — 21:32\'s city, CK.well_and_kings(spy_verb): %s)' % (words(32, 1)[:2], PLACE_FOR_CATTLE, LAND_OF_JAZER, CK_SPY[0]))
        move('Bekhorot 4b:7 (credited)', "'a very great multitude of livestock' the proof that Israel's firstborn donkeys outnumbered the Levites' lambs — the verse a premise in the redemption's arithmetic")
        return out("much cattle, very numerous (32:1) — a place for cattle at its one seat; the land of Jazer one seat; Bekhorot 4b:7's premise", ['plea_made'])
    if ask == 'the_triad':
        ink('32:2', '"to Moses and to Eleazar the priest and to the princes of the congregation" — %s; 27:2\'s "before Moses and before Eleazar the priest and before the princes" %s: THE DAUGHTERS\' TRIAD, WITHOUT THE HALT — no "brought their case before the LORD", no divine frame in forty-two verses (FRAME_VERBS %s)' % (TRIAD_TO, TRIAD_BEFORE, [v for v, _, _ in FRAME_VERBS]))
        return out("to Moses, to Eleazar the priest and to the princes of the congregation (32:2) — 27:2's triad without the halt: no case brought before the LORD", ['plea_made'])
    if ask == 'the_nine':
        ink('32:3', 'the nine cities %s (%d tokens)' % (NINE, len(NINE)))
        move('Berakhot 8b:1', "even 32:3 — 'a verse comprised entirely of names identical in Hebrew and Aramaic' — is read twice with its translation once: the shelf's premise, where the local Onkelos renders the nine BY ARAMAIC NAMES (the reading's ledger row at 32:3; RESEARCH_LOG)")
        return out("nine cities asked (32:3) — Ataroth, Dibon, Jazer, Nimrah, Heshbon, Elealeh, Sebam, Nebo, Beon; Onkelos renders them by Aramaic names (Berakhot 8b:1's premise against the store)", ['accepted'])
    if ask == 'the_request':
        ink('32:4-5', '"the land which the LORD smote before the congregation of Israel" (the conquest\'s ledger — the chukat runner\'s land_possessed); "let this land be given to your servants for a possession" — "for a possession" at %s (Genesis 47:11\'s holding word); "do not bring us over the Jordan"' % FOR_A_POSSESSION)
        return out("let this land be given to your servants for a possession; do not bring us over the Jordan (32:5) — the plea's two clauses; 'a possession' Joseph's word (Genesis 47:11)", ['plea_made'])
    if ask == 'order_of_the_offer':
        ink('32:16, 24, 26', '"folds for our cattle ... and cities for our little ones" (%s, %s) / "cities for your little ones and folds for your sheep" (%s) / "our little ones, our wives, our cattle" (32:26)' % (FOLDS, CITIES_OUR, CITIES_YOUR))
        dat('the row the_order_of_the_offer: %s — the Tanchuma outside the declared spine' % data['the_order_of_the_offer']['value'])
        return out("the cattle before the children (32:16) reversed by Moses (32:24) — the ink's two orders; no row of the declared spine", ['accepted'])
    return out('no verdict in span', [FX.NONE])


# ===== F2: THE REBUKE AND THE OATH RETOLD (Num 32:6-15) — reads chapter 14's ledger, writes nothing ===========
def the_rebuke(case, data):
    del P[:]
    ask = case['ask']
    if ask == 'brothers_to_war':
        ink('32:6', '"shall your brothers go to war and you sit here?" — %s (one seat); Deborah\'s "why did you sit among the sheepfolds" on Reuben (Judges 5:16) OBSERVED, no link' % BROTHERS_TO_WAR)
        return out("shall your brothers go to war and you sit here? (32:6) — one seat; Deborah's question on Reuben (Judges 5:16) observed", ['accepted'])
    if ask == 'hinder_root':
        ink('32:7, 9', '"why do you discourage the heart" %s / "and they discouraged the heart" — THE HINDER-ROOT\'s six Torah tokens %s, all in chapters 30 and 32 (the vows\' "he disallowed her", 30:6, 9, 12); 14:34\'s "my alienation" %s the noun; 32:7 the store\'s written-and-read pair (the reading)' % (DISCOURAGE, [(k[1], k[2], t) for k, t in HINDER_TOKENS], tok('תנואתי')))
        move('cold_run_vows (CALL) — VW.the_man(frame) = %s' % VW_FRAME[0], "the vows' law in Moses' voice — the same root, the same voice, the same class of installation")
        return out("why do you discourage the heart (32:7) — the vows' verb: six Torah tokens all in chapters 30 and 32; 14:34's 'my alienation' the noun", ['accepted'])
    if ask == 'the_spies_verb':
        ink('32:8', '"when I sent them from Kadesh-barnea to see the land" — "to see" %s; 13:2\'s "tour" %s; Deuteronomy 1:22\'s "search" (%d seats); 1:24\'s "scout" %s; Kadesh-barnea %s (32:8 with the prefix)' % (TO_SEE, TO_TOUR, len(TO_SEARCH), TO_SCOUT, KADESH_BARNEA))
        move('cold_run_shelach (CALL) — SL.spies(send_for_yourself) = %s' % SL_SEND[0], "Reish Lakish's 'send YOU' at Moses' discretion (Sotah 34b:3) — Moses' own 'when I SENT them' the retelling's first person; SL.spies(eshcol) = %s" % SL_ESHCOL[0])
        return out("'to see the land' (32:8) — the spies' verb at each telling: 13:2's 'tour', Deuteronomy 1:22's 'search', 1:24's 'scout'; 'when I sent them' Moses' own first person (Sotah 34b:3's 'send you')", ['accepted'])
    if ask == 'the_oath_supplied':
        ink('32:10', '"and the LORD\'s anger burned on that day, and he swore, saying" — %s; "and he swore, saying" at %s; chapter 14 says "as I live" (14:21, 28) and no oath-verb' % (ANGER_THAT_DAY, SWORE_SAYING))
        dat('the row the_oath_supplied: %s (the shelach runner\'s "as I live" arm recorded)' % data['the_oath_supplied']['value'])
        return out("'and he swore, saying' (32:10) — chapter 14 says 'as I live' (14:21, 28); Deuteronomy 1:34 supplies the verb too: the oath retold with the verb supplied", ['accepted'])
    if ask == 'the_set':
        ink('32:11', '"the men who came up from Egypt, from twenty years old and upward" — the parser\'s [%d]; the census formula at %d seats (Exodus 30:14, Numbers 1:3, 14:29, 26:2 among them)' % (TWENTY, len(TWENTY_AND_UP)))
        move('cold_run_shelach (CALL) — SL.decree(set) = %s' % SL_SET[0], "the doomed set 603,550 by CALL; cold_run_bamidbar (CALL) — BM.census(threshold) = %s" % BM_THRESH[0])
        return out("from twenty years old and upward (32:11) — the census formula's twenty-three seats; the doomed set 603,550 by CALL (SL.decree set)", ['accepted'])
    if ask == 'the_exceptions':
        ink('32:12', '"save Caleb son of Jephunneh the Kenizzite and Joshua son of Nun, for they have followed the LORD fully" — "followed fully" %s; Caleb\'s phrase 14:24' % FOLLOWED_LORD)
        move('cold_run_shelach (CALL) — SL.decree(exceptions) = %s' % SL_EXC[0], "the exceptions by CALL; cold_run_second_census (CALL) — C2.the_rolls(except_caleb_joshua) = %s" % C2_EXC[0])
        return out("save Caleb son of Jephunneh the Kenizzite and Joshua son of Nun (32:12) — SL.decree exceptions by CALL: Caleb and Joshua (14:24, 14:30); 'followed the LORD fully' Caleb's phrase", ['exempt'])
    if ask == 'caleb_the_kenizzite':
        ink('32:12', '"the Kenizzite" at %s — Genesis 15:19\'s nation as a gentilic; "son of Kenaz" %s (Othniel)' % (KENIZZITE, SON_OF_KENAZ))
        dat('the row caleb_the_kenizzite: %s — no docket row on the stepfather' % data['caleb_the_kenizzite']['value'])
        return out("the Kenizzite (32:12) — Genesis 15:19's nation as Caleb's gentilic (Joshua 14:6, 14); Othniel son of Kenaz; no docket row — the ink's arm", ['accepted'])
    if ask == 'calebs_hebron':
        move('cold_run_shelach (CALL) — SL.decree(caleb_entitlement) = %s' % SL_CALEB[0], "caleb's holding_owed OPEN on the tape — its run outside the Torah, THE CLASS THIS CHAPTER'S DEBIT SHARES; SL.spies(hebron_visitor) = %s (Sotah 34b:7); 'another spirit' a change over time (34b:8): SL.spies(joshua_caleb_equal) = %s" % (SL_HEBRON[0], SL_EQUAL[0]))
        return out("Caleb's Hebron — holding_owed (14:24 'the land where he went'), paid at Joshua 14:13-14 outside the Torah; Sotah 34b:7 the graves; 'another spirit' a change over time (34b:8)", ['holding_owed'])
    if ask == 'joshua_nothing_owed':
        ink('32:12', '"and Joshua son of Nun" — excepted with Caleb; NO entitlement in the ink (14:30 names him; nothing owed him — the tape\'s yehoshua ledger has no holding)')
        move('cold_run_shelach (CALL) — SL.decree(joshua_childless) = %s; SL.spies(joshua_name) = %s' % (SL_CHILDLESS[0], SL_NAME[0]), "Sotah 35a:4 'a severed head, no children'; Timnath-serah by the LORD's word (Joshua 19:50; Bava Batra 122a:12)")
        return out("Joshua excepted (32:12) and nothing owed him in the ink — Sotah 35a:4 'a severed head, no children'; Timnath-serah by the LORD's word (Joshua 19:50; Bava Batra 122a:12)", ['exempt'])
    if ask == 'forty_years':
        ink('32:13', '"forty years" — the parser\'s [%d]; the phrase in Numbers at %s; Deuteronomy 2:14\'s [%d] from Kadesh' % (FORTY, FORTY_YEARS_NUM, THIRTY_EIGHT))
        move('cold_run_shelach (CALL) — SL.FORTY_YEARS = %s; SL.decree(due) = %s; SL.decree(count_from) = %s' % (SL.FORTY_YEARS, SL_DUE[0], SL_COUNT_FROM[0]), "the forty years' timer FIRED at (40, 5, 9) on the tape (the checkpoint CG3 reads the fire)")
        dat('the row count_from: %s (SL\'s row READ)' % data['count_from']['value'])
        return out("forty years (32:13) — the parser's [40] = SL.FORTY_YEARS; the timer fired at (40, 5, 9) on the tape; Deuteronomy 2:14's thirty-eight from Kadesh", ['accepted'])
    if ask == 'generation_consumed':
        ink('32:13', '"until all the generation that did evil in the eyes of the LORD was consumed" — "until all the generation was consumed" at %s (Deuteronomy 2:14\'s phrase)' % GENERATION_CONSUMED)
        move('cold_run_shelach (CALL) — SL.decree(deaths_ceased) = %s' % SL_DEATHS[0], "Bava Batra 121a:9-121b:1: the fifteenth of Av; God did not speak with Moses until the last had died (Deuteronomy 2:16-17)")
        dat('the row deaths_ceased: %s (SL\'s row READ)' % (data['deaths_ceased']['value'],))
        return out("until all the generation was consumed (32:13) — Deuteronomy 2:14's phrase; the deaths ceased on the fifteenth of Av (SL.decree deaths_ceased by CALL; Bava Batra 121a:9)", ['accepted'])
    if ask == 'made_them_wander':
        ink('32:13', '"and he made them wander in the wilderness" — %s the causative\'s one Torah seat (computed: the token in 32:13)' % ('וינעם',))
        return out("he made them wander in the wilderness (32:13) — the causative's one Torah seat", ['accepted'])
    if ask == 'evil_formula':
        ink('32:13', '"the generation that did evil in the eyes of the LORD" — the formula\'s %d seats, this its FIRST in the Bible\'s order (the Judges\' and Kings\' refrain)' % len(EVIL_FORMULA))
        return out("who did evil in the eyes of the LORD (32:13) — the Judges' and Kings' formula, fifty-three seats, at its first seat in the Bible's order", ['accepted'])
    if ask == 'brood':
        ink('32:14', '"a brood of sinful men" — "brood" %s a hapax, "sinful men" %s (Sodom\'s word, Genesis 13:13); "to add" %s; "the fierce anger of the LORD" %s (Peor\'s 25:4 among them)' % (BROOD, SINFUL_MEN, TO_ADD, FIERCE_ANGER))
        return out("a brood of sinful men (32:14) — 'brood' a hapax, 'sinners' Sodom's word (Genesis 13:13); 'to add yet to the fierce anger of the LORD' Peor's phrase (25:4)", ['accepted'])
    if ask == 'the_threat':
        ink('32:15', '"for if you turn from after him he will yet again leave them in the wilderness, and you will destroy all this people" — %s: a conditional threat in Moses\' mouth, NO WRITE' % DESTROY)
        return out("'he will yet again leave them in the wilderness and you will destroy all this people' (32:15) — a conditional threat in Moses' mouth: no write", ['accepted'])
    if ask == 'two_of_six_hundred_thousand':
        move('Sanhedrin 111a:6 (credited)', "Rav Simai: as at the entry only two of six hundred thousand entered — all died in the wilderness save Caleb and Joshua — so at the exodus")
        move('cold_run_shelach (CALL) — SL.decree(set_edges) = %s' % SL_EDGES[0], "Bava Batra 121b:8 (Rav Hamnuna: Levi outside) and 121b:11 (Rav Acha bar Yaakov: under twenty and over sixty outside)")
        return out("two of six hundred thousand entered — Caleb and Joshua (Rav Simai, Sanhedrin 111a:6); the decree not on Levi (Bava Batra 121b:8) nor under twenty or over sixty (121b:11)", ['exempt'])
    if ask == 'slow_to_anger':
        ink('32:10, 13', '"the LORD\'s anger burned" twice — the retelling\'s frame; "the fierce anger of the LORD" 32:14')
        move('cold_run_shelach (CALL) — SL.decree(pardon) = %s' % SL_PARDON[0], "Sanhedrin 111a:12-13: 'slow to anger' — Moses' 'let the wicked be doomed' turned on him at the spies' sin")
        return out("'the LORD's anger burned' (32:10, 13) — the pardon of 14:20 preceded it (SL.decree pardon by CALL); slow to anger at the spies' sin (Sanhedrin 111a:12-13)", ['accepted'])
    return out('no verdict in span', [FX.NONE])


# ===== F3: THE OFFER (Num 32:16-19) — the utterance the rule binds at Moses' word ==============================
def the_offer(case, data):
    del P[:]
    ask = case['ask']
    if ask == 'folds_and_cities':
        ink('32:16', '"folds for our cattle we will build here, and cities for our little ones" — %s, %s (one seat each): the cattle first' % (FOLDS, CITIES_OUR))
        return out("folds for our cattle and cities for our little ones (32:16) — the offer's order; the cattle first", ['accepted'])
    if ask == 'we_will_arm':
        ink('32:17', '"and we will arm ourselves, hastening, before the children of Israel" — the arm-root\'s seven tokens in the chapter %s (the final letter its own code point)' % ARM_TOKENS)
        return out("and we will arm ourselves, hastening, before the children of Israel (32:17) — the arm-root's seven tokens in the chapter", ['accepted'])
    if ask == 'not_return':
        ink('32:18', '"we will not return to our houses until the children of Israel have inherited every man his inheritance" — %s (one seat); the retellings "until the LORD gives rest" %s; the release Joshua 22:4 "now the LORD has given rest ... as he spoke to them"' % (NOT_RETURN, GIVES_REST))
        return out("we will not return to our houses until the children of Israel have inherited every man his inheritance (32:18) — one seat; the retellings 'until the LORD gives rest' (Deuteronomy 3:20, Joshua 1:15); the release Joshua 22:4", ['accepted'])
    if ask == 'joshuas_armed':
        ink('Joshua 1:14, 4:12-13; Deuteronomy 3:18', '"armed" in the consonants of "fifty" at Joshua 1:14 and 4:12 (the reading: the u-vowel and the doubling dot decide, by code point); 4:13\'s "armed" and Deuteronomy 3:18\'s the chapter\'s own root')
        return out("Joshua's 'armed' in the consonants of 'fifty' (Joshua 1:14, 4:12 chamushim) — told by the u-vowel and the doubling dot; 4:13's chalutsei the chapter's word", ['accepted'])
    if ask == 'east_of_jordan':
        ink('32:19', '"for we will not inherit with them across the Jordan and beyond, because our inheritance has come to us on this side of the Jordan eastward" — the offer\'s ground')
        return out("our inheritance has come to us on this side of the Jordan eastward (32:19) — the offer's ground", ['accepted'])
    return out('no verdict in span', [FX.NONE])


# ===== F4: THE CONDITION (Num 32:20-24) — the doubled condition, the clearance, the utterance rule ============
def the_condition(case, data):
    del P[:]
    ask = case['ask']
    if ask == 'positive_arm':
        ink('32:20-22', '"if you do this thing, if you arm yourselves before the LORD for the war, and every armed one of you passes over the Jordan before the LORD until he has dispossessed his enemies from before him, and the land is subdued before the LORD, and afterward you return — clear before the LORD and before Israel, and this land shall be yours for a possession before the LORD" — "before the LORD" at 32:%s (%d tokens); "before the LORD for the war" %s; "the land is subdued before the LORD" %s' % (BEFORE_THE_LORD_32, len(BEFORE_THE_LORD_32), BEFORE_LORD_FOR_WAR, SUBDUED_BEFORE_LORD))
        return out("if you arm yourselves before the LORD for the war and every armed one passes over the Jordan until the land is subdued, and afterward you return — clear, and this land yours for a possession (32:20-22): the positive arm; 'before the LORD' seven tokens", ['commanded'])
    if ask == 'negative_arm':
        ink('32:23', '"and if you do not do so, behold, you have sinned against the LORD, and know your sin which will find you" — %s (one seat); Judah\'s "God has found out the iniquity of your servants" %s' % (SIN_FIND, FOUND_INIQUITY))
        return out("and if you do not do so, you have sinned against the LORD, and know your sin which will find you (32:23) — the negative arm; Judah's idiom (Genesis 44:16)", ['commanded'])
    if ask == 'doubled_condition':
        ink('32:20, 23; 32:29, 30', 'the condition DOUBLED TWICE in the chapter — "if you do ... and if you do not"; "if they pass over ... and if they do not pass over"')
        move('Mishnah Kiddushin 3:4; Kiddushin 61a:9-61b:8', "R. Meir: every condition not doubled like Gad and Reuben's is none; R. Chanina ben Gamliel: the doubling needed there for its own sake")
        dat('the row doubled_condition: %s (R. Chanina\'s arm and the scope arm recorded)' % data['doubled_condition']['value'])
        return out("the doubled condition — R. Meir: every condition not doubled like Gad and Reuben's is none; R. Chanina ben Gamliel: the doubling was needed there for its own sake (Mishnah Kiddushin 3:4)", ['commanded'])
    if ask == 'four_limbs':
        move('Gittin 75a:11, 75a:12, 75a:14, 75b:6; Bava Metzia 94a:3, 94a:7, 94a:11-14', "from where do we learn the laws of all conditions? from the condition of the sons of Gad and Reuben — the limbs read off this chapter's verses")
        dat('the row the_conditions_four_limbs: %s' % data['the_conditions_four_limbs']['value'])
        return out("the law of all conditions from this chapter (Gittin 75a:11): doubled; the condition before the act (75a:12; Bava Metzia 94a:3); the positive before the negative (Gittin 75b:6); the condition's matter and the act's distinct (75a:14); a condition that can be fulfilled — the ruling as R. Yehuda ben Teima (Bava Metzia 94a:14)", ['commanded'])
    if ask == 'negative_arm_outcome':
        ink('32:30', '"they shall take possessions among you in the land of Canaan" — %s; Hamor\'s "take possessions in it" %s the verb\'s Genesis seat' % (TAKE_AMONG_YOU, HAMOR))
        move('Kiddushin 61b:2, 61b:5-8', "Gilead shared or Canaan only; without the doubling no portion anywhere or Gilead anyway — the two positions dated")
        dat('the row negative_arm_outcome: %s (32:23\'s arm the ink\'s alone)' % data['negative_arm_outcome']['value'])
        return out("'they shall take possessions among you in the land of Canaan' (32:30) — Gilead shared or Canaan only; without the doubling no portion anywhere or Gilead anyway (Kiddushin 61b:2, 61b:5-8)", ['accepted'])
    if ask == 'from_now':
        move('Gittin 75b:2', "Rav Huna in Rav's name: 'on condition' is like 'from now' — the act takes effect at once though the condition is fulfilled later")
        ink('32:33', '"and Moses gave to them" — the grant NOW, under the condition: the transfer written at the grant, the debit open beside it (the design\'s ledger shape)')
        return out("'on condition' is 'from now' (Rav Huna in Rav's name, Gittin 75b:2) — the grant of 32:33 takes effect at once under the condition; the transfer written at the grant, the debit open beside it", ['holding_given'])
    if ask == 'the_clearance':
        ink('32:22', '"and you shall be clear before the LORD and before Israel" — %s (one Bible seat); "the land is subdued before the LORD" also at 1 Chronicles 22:18 ("before the LORD and before his people" — the double in Chronicles\' ink)' % CLEAR)
        move('Mishnah Shekalim 3:2; Yoma 38a:9, 38a:12; Pesachim 13a:13-14', "a person must appear justified before people as before the Omnipresent — the clerk, the bakers, the perfumers, the collectors")
        dat('the row the_clearance: %s' % data['the_clearance']['value'])
        return out("clear before the LORD and before Israel (32:22) — one seat; a person must appear justified before people as before the Omnipresent (Mishnah Shekalim 3:2; Yoma 38a:9, 38a:12; Pesachim 13a:13-14); 1 Chronicles 22:18 the double in Chronicles' ink", ['clear_before_the_lord_and_israel'])
    if ask in ('clerk', 'bakers', 'perfumers', 'collectors'):
        seat = {'clerk': ('Mishnah Shekalim 3:2', "the one who collects from the treasury chamber enters with no cuffed garment, shoe, sandal, phylacteries or amulet — lest he become poor or rich and be suspected"),
                'bakers': ('Yoma 38a:9', "the House of Garmu's descendants never held refined bread — so that people would not say they are sustained from the showbread's technique"),
                'perfumers': ('Yoma 38a:12', "the House of Avtinas's brides never perfumed; a wife from elsewhere STIPULATED not to — a condition on a marriage at the rule's own seat"),
                'collectors': ('Pesachim 13a:13-14', "the charity collectors sell to others and change money with others, not with their own coins")}[ask]
        ink('32:22', '"clear before the LORD and before Israel" — the rule\'s one verse at every seat'); move(seat[0], seat[1])
        return out("%s — clear before the LORD and before Israel (32:22): %s" % (seat[0], seat[1]), ['clear_before_the_lord_and_israel'])
    if ask == 'utterance_rule':
        ink('32:24', '"and that which has gone out of your mouth you shall do" — %s; 30:3\'s "all that goes out of his mouth he shall do" %s: the phrase\'s two Bible seats; Onkelos one Aramaic (the reading)' % (UTTERANCE_32, UTTERANCE_30))
        move('cold_run_vows (CALL) — VW.the_man(all_that_proceeds) = %s' % VW_UTTER[0], "THE UTTERANCE RULE'S SECOND SEAT — the vows' cell's own effect commanded the debit's; 10b's filed seat PAID; the row vow_support_base = %s READ" % data.get('vow_support_base', {'value': VW.DATA['vow_support_base']['value']})['value'])
        return out("that which has gone out of your mouth you shall do (32:24) — 30:3's 'all that goes out of his mouth he shall do', the phrase's two seats; the vows' cell by CALL: the vow's fulfilment — a positive duty, a prohibition, and the court's compulsion", ['commanded'])
    if ask == 'the_lemma_pair':
        ink('32:24 / 30:3', '"goes out" (3318) + "mouth" (6310) adjacent at %s — nine seats: the Torah\'s two, Judges 11:36 Jephthah\'s daughter ("do to me according to that which went out of your mouth") among the seven outside' % LEMMA_PAIR)
        return out("'goes out' + 'mouth' adjacent at nine seats — Numbers 30:3 and 32:24 the Torah's two, Judges 11:36 Jephthah's daughter among the seven outside", ['accepted'])
    if ask == 'the_build_command':
        ink('32:24', '"build for yourselves cities for your little ones and folds for your sheep" — %s: Moses\' order reversed (the children first); the run at 32:34-38 CLOSES it (the chapter\'s one Torah-closed debit)' % CITIES_YOUR)
        return out("build for yourselves cities for your little ones and folds for your sheep (32:24) — Moses' order reversed: the children first; the run at 32:34-38 closes it", ['commanded'])
    if ask == 'the_verb_future':
        ink('32:21-22', '"and every armed one of you will pass over [ve\'avar] the Jordan" — the perfect with the conjunction; "and the land is subdued ... and afterward you return" fixes the future')
        move('Sotah 3a:8-9 (3a:9 credited)', "the sotah's 've'avar' past, the stipulation's future — 32:22's sequence the proof")
        return out("'and every armed one of you will pass over' (32:21) read of the future — 'the land subdued... and you return afterward' fixes it (Sotah 3a:8-9)", ['accepted'])
    if ask == 'condition_counter_to_torah':
        move('Mishnah Bava Metzia 94a:2; 94a:5', "in monetary matters the parties may agree to special terms; counter to the Torah on a non-monetary matter — void")
        dat('the row the_conditions_four_limbs (counter_to_the_torah arm): %s' % data['the_conditions_four_limbs']['settings']['counter_to_the_torah'][:60])
        return out("a condition counter to the Torah on a non-monetary matter is void; in monetary matters the parties may agree (Mishnah Bava Metzia 94a:2)", ['exempt'])
    if ask == 'impossible_condition':
        move('Bava Metzia 94a:11-14', "R. Yehuda ben Teima: a condition one cannot fulfil, stipulated first — he is only exaggerating, the act stands; the Rabbis: binding; the ruling as R. Yehuda ben Teima (Rav Nachman in Rav's name)")
        return out("a condition that cannot be fulfilled — the act stands and the condition is void, the ruling as R. Yehuda ben Teima (Bava Metzia 94a:11-14); the Rabbis: binding", ['exempt'])
    if ask == 'undoubled_on_a_bill':
        move('Gittin 75a:10, 75a:13', "Abaye: R. Meir requires the compound condition and the husband did not double — the bill valid; Rava: the action preceded the condition")
        return out("an undoubled condition on a bill of divorce — no condition according to R. Meir, the act stands (Gittin 75a:10); the action preceding the condition the same (75a:13)", ['exempt'])
    if ask == 'the_scope':
        move('Shevuot 36a:27, 36a:29', "R. Meir refuses the inference in monetary matters only — or everywhere (the sotah's spelling)")
        dat('the row doubled_condition (scope arm): %s' % data['doubled_condition']['settings']['scope'][:70])
        return out("R. Meir refuses the inference in monetary matters only (Shevuot 36a:27) — or everywhere (36a:29; the sotah's spelling): the rule's scope, both readings", ['accepted'])
    if ask == 'onkelos_buffer':
        ink('32:20, 21, 22, 27, 29, 32', '"before the LORD" at the seven tokens; ONKELOS renders the six martial seats "before the PEOPLE of the LORD" and keeps the three legal ones (32:22 twice, 32:29) — the reading\'s claim MT32A-06, measured on the whole of Onkelos Numbers')
        return out("'before the people of the LORD' at the six martial seats of Onkelos Numbers, all this chapter's (32:20, 21, 22, 27, 29, 32); the three legal seats kept — the reading's claim MT32A-06", ['accepted'])
    return out('no verdict in span', [FX.NONE])


# ===== F5: THE ACCEPTANCE AND THE CHARGE (Num 32:25-32) ======================================================
def the_acceptance_and_the_charge(case, data):
    del P[:]
    ask = case['ask']
    if ask == 'servants_will_do':
        ink('32:25, 27', '"your servants will do as my lord commands" — %s (one seat); "my lord" in Numbers at %s (11:28 Joshua\'s, 12:11 Aaron\'s, 14:17 to God, 36:2 the Gileadite heads\')' % (SERVANTS_WILL_DO, MY_LORD_NUM))
        return out("your servants will do as my lord commands (32:25) — 'my lord' for Moses at 32:25, 27 (Joshua's 11:28, Aaron's 12:11, the Gileadite heads' 36:2)", ['accepted'])
    if ask == 'the_order_reversed':
        ink('32:26-27', '"our little ones, our wives, our cattle and all our beasts shall be there in the cities of Gilead; and your servants will pass over, every armed one for war before the LORD" — Moses\' order held (the children first); "before the LORD for the war" %s' % BEFORE_LORD_FOR_WAR)
        return out("our little ones, our wives, our cattle and all our beasts (32:26) — Moses' order held; the retellings 'your wives, your little ones, your cattle' (Deuteronomy 3:19, Joshua 1:14)", ['accepted'])
    if ask == 'the_commission':
        ink('32:28', '"and Moses commanded concerning them Eleazar the priest, and Joshua son of Nun, and the heads of the fathers of the tribes of the children of Israel" — %s; Joshua 14:1\'s form %s WORD FOR WORD; Joshua 21:1\'s third form %s' % (TRIAD_32, TRIAD_JOSH, TRIAD_JOSH21))
        move('Bava Batra 122a:4 (credited)', "Eleazar dressed with the Urim, Joshua and all Israel before him at the lottery — the commission at its run outside the Torah")
        return out("Eleazar the priest, Joshua son of Nun and the heads of the fathers of the tribes (32:28) — Joshua 14:1's dividers word for word, 21:1 the third form; Bava Batra 122a:4's lottery", ['commanded'])
    if ask == 'second_doubling':
        ink('32:29-30', '"if the sons of Gad and the sons of Reuben pass over the Jordan with you ... you shall give them the land of Gilead for a possession; and if they do not pass over armed with you, they shall take possessions among you in the land of Canaan" — "the land is subdued before you" %s; "the land of Gilead" %s; the exam\'s proof verses (cited five and four times)' % (SUBDUED_BEFORE_YOU, LAND_OF_GILEAD_ART))
        return out("if they pass over — give them Gilead; if not — they take possessions among you in Canaan (32:29-30): the second doubling, the exam's proof verses; the commission's debit open to Joshua 22", ['commanded'])
    if ask == 'the_lords_word':
        ink('32:31', '"that which the LORD has spoken to your servants, so will we do" — the parties call MOSES\' stipulation the LORD\'s word; Joshua 22:9 "by the commandment of the LORD by the hand of Moses"; no divine frame in the chapter (FRAME_VERBS %s)' % [v for v, _, _ in FRAME_VERBS])
        move('cold_run_vows (CALL) — VW.the_man(frame) = %s' % VW_FRAME[0], "30:2's class — a law relayed in Moses' voice; the installed_by class named in the registry (the second pass's D2)")
        return out("that which the LORD has spoken to your servants, so will we do (32:31) — Moses' stipulation called the LORD's word; Joshua 22:9 'by the commandment of the LORD by the hand of Moses': a law in Moses' voice with no divine frame", ['accepted'])
    if ask == 'we_short':
        ink('32:32', '"WE will pass over armed before the LORD to the land of Canaan, and the possession of our inheritance with us across the Jordan" — "we" in its short form at %s; "the possession of our inheritance" %s against the daughters\' "a possession of an inheritance" %s' % (WE_SHORT, POSSESSION_OF_OUR, POSSESSION_OF))
        return out("'we' in its short form (32:32) — three Bible seats (Genesis 42:11, Lamentations 3:42); 'the possession of our inheritance' the daughters' construct (27:7)", ['accepted'])
    return out('no verdict in span', [FX.NONE])


# ===== F6: THE GRANT (Num 32:33) =============================================================================
def the_grant(case, data):
    del P[:]
    ask = case['ask']
    if ask == 'three_parties':
        ink('32:33', '"and Moses gave to them — to the sons of Gad and to the sons of Reuben and to half the tribe of Manasseh son of Joseph" — three grantees; "half the tribe of Manasseh" first named here (the phrase\'s seats include %s)' % ('Num 34:14' if 'Num 34:14' in HALF_MANASSEH else HALF_MANASSEH[:3]))
        return out("to the sons of Gad, to the sons of Reuben and to half the tribe of Manasseh (32:33) — three transfers; half Manasseh first named at the grant", ['holding_given'])
    if ask == 'two_kingdoms':
        ink('32:33', '"the kingdom of Sihon king of the Amorite" %s (one seat) "and the kingdom of Og king of Bashan" %s — "the land with its cities in the borders, the cities of the land round about"' % (KINGDOM_SIHON, KINGDOM_OG))
        move('cold_run_chukat (CALL) — CK.well_and_kings(land_east) = %s' % CK_EAST[0], "the chukat runner's land_possessed on israel_people at 21:24-25, 21:31-32, 21:35 — THE GRANT'S SOURCE ON THE LEDGER; CK.well_and_kings(deut3_delta) = %s; (og_lore) = %s" % (CK_DELTA[0], CK_OG[0]))
        return out("the kingdom of Sihon king of the Amorite (one seat) and the kingdom of Og king of Bashan (Deuteronomy 3's and this) — the chukat runner's land possessed at 21:24-35 by CALL: the grant's source", ['holding_given'])
    if ask == 'half_manassehs_stipulation':
        ink('32:33', 'no stipulation spoken to half Manasseh in the chapter (32:20-32 address the two tribes alone — COMPOUND %s)' % COMPOUND)
        dat('the row half_manassehs_stipulation: %s' % data['half_manassehs_stipulation']['value']); move('Bava Batra 118b:8 (credited)', "'ten parts fell to Manasseh, beside the land of Gilead and Bashan beyond the Jordan' (Joshua 17:5-6) — the shelf's line between the tribe's ten parts and its east")
        return out("no stipulation spoken to half Manasseh in the chapter; Deuteronomy 3:18-20, Joshua 1:12-15, 4:12 extend the crossing to the three; Joshua 17:5-6 'beside the land of Gilead and Bashan' (Bava Batra 118b:8)", ['accepted'])
    if ask == 'the_count':
        ink('26:7, 18, 34; Joshua 4:13; 1 Chronicles 5:18', 'the two and a half — %d + %d + %d / 2 = %d; Joshua 4:13 "about forty thousand armed" [%d]; 1 Chronicles 5:18 "that went out to war" [%d]' % (C2.C26['reuben'], C2.C26['gad'], C2.C26['manasseh'], TWO_AND_A_HALF, FORTY_THOUSAND, CHRONICLES_COUNT))
        move('cold_run_second_census (CALL) — C2.the_roll(total) = %s' % C2_TOTAL[0], "the counts the second census's own rows (the population table on the tape — the checkpoint CG5 reads them)")
        dat('the row the_forty_thousand: %s' % data['the_forty_thousand']['value'])
        return out("the two and a half's count — 43,730 + 40,500 + 52,700 ÷ 2 = 110,580 from the second census by CALL; Joshua 4:13's about forty thousand; 1 Chronicles 5:18's 44,760", ['accepted'])
    if ask == 'land_held':
        move('cold_run_second_census (CALL) — C2.the_land(possession_before_assignment) = %s' % C2_HELD[0], "Rabba: Eretz Yisrael held before assignment (Bava Batra 119a:1, 119a:5 — credited) — the standing 'a possession' carries at 32:5, 22, 29, 32 (%s)" % FOR_A_POSSESSION[-3:])
        dat('the row the_land_east_status: %s' % data['the_land_east_status']['value'])
        return out("in possession before assignment — the rows are holdings before the lot (C2 by CALL; Bava Batra 119a:1, 119a:5): the standing 'a possession' carries", ['holding_given'])
    if ask == 'not_by_lot':
        move('cold_run_second_census (CALL) — C2.the_land(by_lot) = %s; (thirteen_tribes) = %s' % (C2_LOT[0], C2_THIRTEEN[0]), "26:55's lot is Canaan's; the east by Moses' word (32:33) — israel_people's OPEN commanded divide_the_land is not this chapter's run")
        return out("the east by Moses' word, not by lot — 26:55's lot is Canaan's (C2 by CALL: the place by lot, Joshua 14-19 the run); the OPEN divide_the_land not this chapter's run", ['accepted'])
    if ask == 'bequeath_not_inherit':
        move('cold_run_second_census (CALL) — C2.the_land(morasha) = %s' % C2_MORASHA[0], "Bava Batra 119b:3-4 (credited): Exodus 6:8's 'heritage' — the exodus generation bequeath and do not inherit; 'You will bring THEM in' (Exodus 15:17)")
        return out("the exodus generation bequeath and do not inherit (Bava Batra 119b:3-4; C2 morasha by CALL) — the doomed set's title to the land", ['accepted'])
    return out('no verdict in span', [FX.NONE])


# ===== F7: THE CITIES (Num 32:34-38) =========================================================================
def the_cities(case, data):
    del P[:]
    ask = case['ask']
    if ask == 'gads_eight':
        ink('32:34-36', '%s — Gad\'s EIGHT: %s; "fortified cities and folds for sheep"' % (GAD_BUILT, GAD_CITIES))
        return out("Dibon, Ataroth, Aroer, Atroth-shophan, Jazer, Jogbehah, Beth-nimrah, Beth-haran — Gad's eight (32:34-36), fortified cities and folds for sheep", ['cities_built'])
    if ask == 'reubens_six':
        ink('32:37-38', '%s — Reuben\'s SIX: %s; "their names being changed" %s (one seat); "and they called by names the names of the cities which they built"' % (REUBEN_BUILT, REUBEN_CITIES, NAMES_CHANGED))
        return out("Heshbon, Elealeh, Kiriathaim, Nebo, Baal-meon and Sibmah — Reuben's six (32:37-38); 'their names being changed' one seat", ['cities_built'])
    if ask == 'the_split':
        ink('32:3 against 32:34-38', 'the nine %s — Gad\'s four (Ataroth, Dibon, Jazer, Nimrah as Beth-nimrah), Reuben\'s five (Heshbon, Elealeh, Sebam as Sibmah, Nebo, Beon as Baal-meon): the reading\'s claim MT32A-09' % NINE)
        return out("the nine asked split four and five — Gad's Ataroth, Dibon, Jazer, Nimrah (as Beth-nimrah); Reuben's Heshbon, Elealeh, Sebam (as Sibmah), Nebo, Beon (as Baal-meon)", ['accepted'])
    if ask == 'dibon_gad':
        ink('33:45-46', '"and they camped at Dibon Gad; and they journeyed from Dibon Gad" — %s / %s: the itinerary\'s own witness, the next chapter\'s' % (words(33, 45)[-2:], words(33, 46)[1:3]))
        return out("Dibon Gad (33:45-46) — the itinerary's own witness to the city's tribe, the next chapter's", ['accepted'])
    if ask == 'two_crossed':
        ink('Joshua 13:17, 13:26, 13:20', 'Reuben\'s list: %s (Heshbon and Dibon both); Gad\'s border "from Heshbon" (13:26); Beth-peor Reuben\'s (13:20)' % ' '.join(words(13, 17, 'Josh')))
        dat('the row the_two_crossed_cities: %s' % data['the_two_crossed_cities']['value'])
        return out("Dibon and Heshbon in Reuben's list at Joshua 13:17, Heshbon on Gad's border at 13:26 — the two crossed between the tribes; Beth-peor Reuben's (13:20)", ['accepted'])
    if ask == 'moses_grave':
        ink('32:37-38', 'Nebo among Reuben\'s six')
        move('Sotah 13b:20', "R. Yehuda: Moses died in Reuben's portion — Nebo is Reuben's (32:37-38); Onkelos 32:3 'Nebo, the burial place of Moses' the same reading")
        dat('the row moses_grave: %s' % data['moses_grave']['value'])
        return out("Nebo Reuben's (32:37-38) — Moses died in Reuben's portion (Sotah 13b:20); Onkelos 'Nebo, the burial place of Moses' at 32:3; the Sifrei 106:1's Gad the other arm", ['accepted'])
    if ask == 'the_build_closed':
        ink('32:34-38 against 32:24', '"and the sons of Gad built ... and the sons of Reuben built" — the run of "build for yourselves cities for your little ones" (%s): the build debit CLOSED BY VALUE' % CITIES_YOUR)
        return out("the cities built (32:34-38) — the run of 32:24's 'build for yourselves cities': the build debit closed by value, the chapter's one Torah-closed debit", ['cities_built'])
    return out('no verdict in span', [FX.NONE])


# ===== F8: MACHIR, JAIR AND NOBAH (Num 32:39-42) =============================================================
def machir_jair_nobah(case, data):
    del P[:]
    ask = case['ask']
    if ask == 'sons_of_machir':
        ink('32:39', '"and the sons of Machir son of Manasseh went to Gilead and took it, and dispossessed the Amorite who was in it" — "the sons of Machir son of Manasseh" %s (Genesis 50:23\'s collective, born on Joseph\'s knees); "the Amorite who was in it" %s; the verb 21:32\'s' % (SONS_OF_MACHIR, AMORITE_IN_IT))
        move('cold_run_chukat (CALL) — CK.well_and_kings(spy_verb) = %s' % CK_SPY[0], "21:32's 'dispossessed the Amorite who was there' — the same verb at Jazer")
        return out("the sons of Machir son of Manasseh (32:39) — Genesis 50:23's collective, born on Joseph's knees; Gilead taken, the Amorite dispossessed (21:32's verb)", ['land_possessed'])
    if ask == 'gilead_given':
        ink('32:40', '"and Moses gave Gilead to Machir son of Manasseh, and he dwelt in it" — "Machir son of Manasseh" at %s; 26:29 "Machir begot Gilead" (C2.FAMILIES[manasseh][0] = %s)' % (MACHIR_SON, C2.FAMILIES['manasseh'][0]))
        return out("Moses gave Gilead to Machir son of Manasseh (32:40) — the clan under the ancestor's name (26:29; Joshua 17:1 the man of war; Deuteronomy 3:15)", ['holding_given'])
    if ask == 'jair':
        ink('32:41', '"and Jair son of Manasseh went and took their villages, and called them Havvoth-jair" — Havvoth-jair at %s (six seats); "went and took" at 32:41-42' % HAVVOTH)
        return out("Jair son of Manasseh took their villages and called them Havvoth-jair (32:41) — six seats; 'went and took' at 32:41-42 alone", ['land_possessed'])
    if ask == 'jairs_lineage':
        ink('32:41; 1 Chronicles 2:21-23', '"Jair son of Manasseh" at %s; 1 Chronicles 2:21 Hezron at [%d] took Machir\'s daughter, 2:22 Jair\'s [%d] cities, 2:23 [%d] cities; Judges 10:4 the judge\'s %s' % (JAIR_SON, RETOLD[('1Chr', 2, 21)][0], RETOLD[('1Chr', 2, 22)][0], RETOLD[('1Chr', 2, 23)][0], RETOLD[('Judg', 10, 4)]))
        dat('the row jairs_lineage: %s' % data['jairs_lineage']['value'])
        return out("Jair son of Manasseh (32:41; Deuteronomy 3:14; 1 Kings 4:13) against 1 Chronicles 2:21-22's Hezron's grandson by Machir's daughter, twenty-three cities — the ink's two accounts; the judge Jair's thirty (Judges 10:4)", ['accepted'])
    if ask == 'survivors':
        move('Bava Batra 121b:9-11 (credited)', "Jair and Machir born in Jacob's days and did not die until the entry; 'about thirty-six' at Ai (Joshua 7:5 — the parser's [%d]) read as Jair alone; already old at the decree (SL.decree(set_edges) = %s)" % (THIRTY_SIX, SL_EDGES[0]))
        dat('the row jair_and_machir_survived: %s' % data['jair_and_machir_survived']['value'])
        return out("Jair and Machir born in Jacob's days and did not die until the entry — 'about thirty-six' at Ai read as Jair alone (Bava Batra 121b:9-10); already old at the decree (121b:11)", ['accepted'])
    if ask == 'nobah':
        ink('32:42', '"and Nobah went and took Kenath and its daughters, and called it Nobah after his own name" — Nobah %s (one seat as a person); Kenath %s; "its daughters" in Numbers %s; Nobah and Jogbehah together at Judges 8:11 (the words %s)' % (NOBAH, KENATH, DAUGHTERS_NUM, [w for w in words(8, 11, 'Judg') if w in ('לנבח', 'ויגבהה')]))
        return out("Nobah took Kenath and its daughters and called it Nobah after his own name (32:42) — Nobah and Jogbehah together at Judges 8:11 on Gideon's route; Kenath's other seat 1 Chronicles 2:23", ['land_possessed'])
    return out('no verdict in span', [FX.NONE])


# ---- THE WRAP — the daemon, the scene, the narrative ------------------------------------------------------
def law_gad_reuben(event, world):
    """Num 32:1-42 (cold_run_gad_reuben.py F1-F8). given_at Num 32:20; installed_by boot — A STIPULATION IN MOSES' VOICE WITH NO DIVINE
    FRAME (30:2's class; the class named in the registry, the second pass decides). TWELVE TAPE LINES: the request a plea on the ink's
    compound party; the rebuke, the offer, the acceptances and the answer NO WRITE (the oath retold is read against chapter 14's ledger);
    THE CONDITION two DEBITS on the compound party — to cross armed before the LORD until the land is subdued (OPEN BY DESIGN: the release
    Joshua 22:1-9 outside the Torah) and to build cities and folds (CLOSED by value at 32:34-38); the commission's debit OPEN; the grant
    THREE TRANSFERS from Israel's possession by conquest; the cities as statuses; Machir's sons, Jair and Nobah as the land possessed. The
    exam's four case kinds dispatch to the cells with LITERAL effects per kind (2b's form — an unnamed effect is a KeyError)."""
    k, src = event['kind'], event['case_source']
    E_ = lambda eff, s, cp=None, amount=None, due=None, law='', value=None: {'effect': eff, 'subject': s, 'counterparty': cp, 'amount': amount, 'due': due, 'value': value if value is not None else True, 'source_law': law, 'case_source': src}
    day = event.get('day', world.clock.day)      # THE SEQUENTIAL RUN: the event's own day
    # ---- the twelve lines (page_order at the counter's day, no marker in the chapter) ----
    if k == 'land_requested':
        return [E_('plea_made', 'the-sons-of-gad-and-reuben', value='let this land be given to your servants for a possession; do not bring us over the Jordan (32:5)', law='F1 [INK 32:1-5 "and the sons of Gad and the sons of Reuben came and spoke to Moses and to Eleazar the priest and to the princes of the congregation" — 27:2\'s triad WITHOUT the halt; the nine cities; "a possession" Genesis 47:11\'s word; the STATUS a spoken request writes on the one asked (Hobab\'s form); the row the_order_of_the_offer]')]
    if k == 'moses_rebuked_the_tribes':
        return []                                                              # NO WRITE — the oath retold (32:8-13) is read against the shelach daemon's ledger (CG3): sentence_pronounced, the forty years' fire, caleb's holding_owed
    if k == 'tribes_offered_to_arm':
        return []                                                              # NO WRITE — the undertaking is bound at the condition's line by the utterance rule (32:24)
    if k == 'condition_stipulated':
        return [E_('commanded', 'the-sons-of-gad-and-reuben', value='cross_armed_before_the_lord_until_the_land_is_subdued', law='F4 [INK 32:20-23 "if you arm yourselves before the LORD for the war, and every armed one of you passes over the Jordan before the LORD until he has dispossessed his enemies from before him, and the land is subdued before the LORD, and afterward you return — you shall be clear before the LORD and before Israel, and this land shall be yours for a possession before the LORD; and if you do not do so, behold, you have sinned against the LORD, and know your sin which will find you" — THE DOUBLED CONDITION (Mishnah Kiddushin 3:4; the rows doubled_condition, the_conditions_four_limbs, negative_arm_outcome, the_clearance); bound by 32:24\'s "that which has gone out of your mouth you shall do" = 30:3 (VW.the_man(all_that_proceeds) by CALL — its own effect commanded); OPEN BY DESIGN: the run is JOSHUA 22:1-9 ("you have kept all that Moses the servant of the LORD commanded you ... now turn and go to your tents", 22:2-4) — outside the Torah, the Jabesh-gilead class (the captives\' sentence 31:17, Caleb\'s Hebron 14:24)]'),
                E_('commanded', 'the-sons-of-gad-and-reuben', value='build_cities_and_folds', law='F4 [INK 32:24 "build for yourselves cities for your little ones and folds for your sheep" — Moses\' order (the children first); CLOSED BY VALUE at 32:34-38, the chapter\'s one Torah-closed debit]')]
    if k == 'tribes_accepted_the_condition':
        return []                                                              # NO WRITE — the seal on the parties' side (32:25-27); the debit stands from 32:20-24
    if k == 'commission_charged':
        return [E_('commanded', 'the-dividers-of-the-land', value='give_them_gilead_if_they_cross', law='F5 [INK 32:28-30 "and Moses commanded concerning them Eleazar the priest, and Joshua son of Nun, and the heads of the fathers of the tribes of the children of Israel: if the sons of Gad and the sons of Reuben pass over the Jordan with you, every armed one for war before the LORD, and the land is subdued before you, you shall give them the land of Gilead for a possession; and if they do not pass over armed with you, they shall take possessions among you in the land of Canaan" — THE SECOND DOUBLING (the exam\'s proof verses); the triad Joshua 14:1\'s dividers word for word; OPEN BY DESIGN: the run Joshua 1:12-18 (Joshua\'s charge) and 22:1-9 (the release), outside the Torah; Bava Batra 122a:4\'s lottery]')]
    if k == 'tribes_answered_so_will_we_do':
        return []                                                              # NO WRITE — "that which the LORD has spoken to your servants, so will we do" (32:31-32): Moses' stipulation called the LORD's word (the installed_by class's witness)
    if k == 'land_granted_east':
        rows = {r['tribe']: r['count'] for r in world.population(grain='counted', family=None) if r.get('as_of') == 'Num 26:5-51' and r.get('tribe') in ('reuben', 'gad', 'manasseh')}
        count = (rows['reuben'] + rows['gad'] + rows['manasseh'] // 2) if len(rows) == 3 else TWO_AND_A_HALF      # THE TABLE IS THE INSTRUMENT on the tape; the runner's own world has no rows — C2's counts by CALL
        assert count == TWO_AND_A_HALF, (rows, TWO_AND_A_HALF)
        val = lambda who: 'the kingdom of Sihon king of the Amorite and the kingdom of Og king of Bashan, the land with its cities in the borders (32:33) — %s; the land possessed at 21:24-25, 21:31-32, 21:35 (CK.well_and_kings(land_east) by CALL); the two and a half %d counted (26:7, 18, 34%s) against Joshua 4:13\'s %d and 1 Chronicles 5:18\'s %d' % (who, count, ' — the population table\'s rows' if len(rows) == 3 else '', FORTY_THOUSAND, CHRONICLES_COUNT)
        L = 'F6 [INK 32:33 "and Moses gave to them — to the sons of Gad and to the sons of Reuben and to half the tribe of Manasseh son of Joseph — the kingdom of Sihon king of the Amorite and the kingdom of Og king of Bashan" — the TRANSFER from Israel\'s possession by conquest (the chukat runner\'s land_possessed READ off the ledger); "on condition" is "from now" (Gittin 75b:2): the grant takes effect at once under the condition; the rows half_manassehs_stipulation, the_forty_thousand, the_land_east_status]'
        return [E_('holding_given', 'the-sons-of-gad', cp='israel', value=val('to the sons of Gad'), law=L),
                E_('holding_given', 'the-sons-of-reuben', cp='israel', value=val('to the sons of Reuben'), law=L),
                E_('holding_given', 'the-half-tribe-of-manasseh', cp='israel', value=val('to half the tribe of Manasseh son of Joseph — first named at the grant, no stipulation spoken to it (the row half_manassehs_stipulation)'), law=L)]
    if k == 'cities_built_east':
        world.close('the-sons-of-gad-and-reuben', 'commanded', 'Num 32:34-38 — and the sons of Gad built ... and the sons of Reuben built: the run of 32:24\'s "build for yourselves cities for your little ones and folds for your sheep" — the build debit CLOSED BY VALUE (the chapter\'s one Torah-closed debit)', value='build_cities_and_folds')
        return [E_('cities_built', 'the-sons-of-gad', value='%s — Dibon, Ataroth, Aroer, Atroth-shophan, Jazer, Jogbehah, Beth-nimrah, Beth-haran: fortified cities and folds for sheep (32:34-36)' % ' / '.join(GAD_CITIES), law='F7 [INK 32:34-36 — Gad\'s EIGHT from the tokens; four of the nine asked at 32:3 (Ataroth, Dibon, Jazer, Nimrah as Beth-nimrah); Dibon Gad the itinerary\'s witness (33:45-46); Dibon in Reuben\'s list at Joshua 13:17 (the row the_two_crossed_cities)]'),
                E_('cities_built', 'the-sons-of-reuben', value='%s — Heshbon, Elealeh, Kiriathaim, Nebo, Baal-meon (their names being changed) and Sibmah; and they called by names the names of the cities which they built (32:37-38)' % ' / '.join(REUBEN_CITIES), law='F7 [INK 32:37-38 — Reuben\'s SIX from the tokens; five of the nine asked (Heshbon, Elealeh, Sebam as Sibmah, Nebo, Beon as Baal-meon); "their names being changed" one seat; Nebo Moses\' grave (Sotah 13b:20; Onkelos 32:3 — the row moses_grave); Heshbon on Gad\'s border at Joshua 13:26]')]
    if k == 'gilead_taken_by_machir':
        return [E_('land_possessed', 'the-sons-of-machir', cp='the-amorite', value='Gilead taken and the Amorite who was in it dispossessed (32:39) — 21:32\'s verb; the sons of Machir son of Manasseh Genesis 50:23\'s collective, born on Joseph\'s knees', law='F8 [INK 32:39 "and the sons of Machir son of Manasseh went to Gilead and took it, and dispossessed the Amorite who was in it" — the phrase\'s two Torah seats; the conquest\'s effect (the chukat runner\'s) at its fourth seat; the row jair_and_machir_survived (Bava Batra 121b:9)]'),
                E_('holding_given', 'the-sons-of-machir', cp='moses', value='Gilead (32:40) — given by Moses to Machir son of Manasseh, the clan under the ancestor\'s name (26:29; Joshua 17:1; Deuteronomy 3:15); "and he dwelt in it"', law='F8 [INK 32:40 "and Moses gave Gilead to Machir son of Manasseh, and he dwelt in it" — the TRANSFER; Machir the clan (26:29 "Machir begot Gilead")]')]
    if k == 'villages_taken_by_jair':
        return [E_('land_possessed', 'jair', value='their villages taken and called Havvoth-jair (32:41) — the naming inside the value; six seats (Deuteronomy 3:14, Joshua 13:30, Judges 10:4, 1 Kings 4:13, 1 Chronicles 2:23)', law='F8 [INK 32:41 "and Jair son of Manasseh went and took their villages, and called them Havvoth-jair" — "went and took" at 32:41-42 alone; the rows jairs_lineage (1 Chronicles 2:21-22\'s Hezron) and jair_and_machir_survived (Bava Batra 121b:10 — "about thirty-six" at Ai read as Jair); the homograph traps in the registry]')]
    if k == 'kenath_taken_by_nobah':
        return [E_('land_possessed', 'nobah', value='Kenath and its daughters taken and called Nobah after his own name (32:42) — the naming inside the value; Kenath 1 Chronicles 2:23', law='F8 [INK 32:42 "and Nobah went and took Kenath and its daughters, and called it Nobah after his own name" — "its daughters" the villages (21:25, 21:32); Nobah and Jogbehah together at Judges 8:11 on Gideon\'s route against Midian (the place Nobah the trap)]')]
    # ---- the exam's case kinds: each names LITERALLY every effect it can write (2b's form) ----
    if k == 'stipulation_case':
        fn = the_acceptance_and_the_charge if event.get('cell') == 'charge' else the_condition
        v, e, _ = fn(dict(event, ask=event['ask']), DATA); L = '%s [%s]' % ('F5' if event.get('cell') == 'charge' else 'F4', v); s_ = event['person']
        W = {'commanded': E_('commanded', s_, value=v, law=L), 'holding_given': E_('holding_given', s_, cp='israel', value=v, law=L), 'accepted': E_('accepted', s_, value=v, law=L), 'exempt': E_('exempt', s_, value=v, law=L)}
        return [W[x] for x in e if x != FX.NONE]
    if k == 'clearance_case':
        v, e, _ = the_condition(dict(event, ask=event['ask']), DATA); L = 'F4 [%s]' % v; s_ = event['person']
        W = {'clear_before_the_lord_and_israel': E_('clear_before_the_lord_and_israel', s_, value=v, law=L), 'accepted': E_('accepted', s_, value=v, law=L), 'exempt': E_('exempt', s_, value=v, law=L)}
        return [W[x] for x in e if x != FX.NONE]
    if k == 'oath_retold_case':
        v, e, _ = the_rebuke(dict(event, ask=event['ask']), DATA); L = 'F2 [%s]' % v; s_ = event['person']
        W = {'exempt': E_('exempt', s_, value=v, law=L), 'holding_owed': E_('holding_owed', s_, cp='the-court', value=v, law=L), 'accepted': E_('accepted', s_, value=v, law=L)}
        return [W[x] for x in e if x != FX.NONE]
    if k == 'land_east_case':
        fn = {'cities': the_cities, 'machir': machir_jair_nobah, 'request': the_request}.get(event.get('cell'), the_grant)
        v, e, _ = fn(dict(event, ask=event['ask']), DATA); L = '%s [%s]' % ({'cities': 'F7', 'machir': 'F8', 'request': 'F1'}.get(event.get('cell'), 'F6'), v); s_ = event['person']
        W = {'holding_given': E_('holding_given', s_, cp='israel', value=v, law=L), 'land_possessed': E_('land_possessed', s_, cp='the-amorite', value=v, law=L), 'cities_built': E_('cities_built', s_, value=v, law=L), 'plea_made': E_('plea_made', s_, value=v, law=L), 'accepted': E_('accepted', s_, value=v, law=L), 'exempt': E_('exempt', s_, value=v, law=L)}
        return [W[x] for x in e if x != FX.NONE]
    return []


LINES = [
    ('Num 32:1-5 — and the sons of Reuben and the sons of Gad had much cattle, very numerous, and they saw the land of Jazer and the land of Gilead, and behold, the place was a place for cattle; and the sons of Gad and the sons of Reuben came and spoke to Moses and to Eleazar the priest and to the princes of the congregation: Ataroth and Dibon and Jazer and Nimrah and Heshbon and Elealeh and Sebam and Nebo and Beon, the land which the LORD smote before the congregation of Israel, is a land for cattle, and your servants have cattle; if we have found favour in your eyes, let this land be given to your servants for a possession; do not bring us over the Jordan', 'the-sons-of-gad-and-reuben'),
    ('Num 32:6-15 — and Moses said to the sons of Gad and to the sons of Reuben: shall your brothers go to war and you sit here? why do you discourage the heart of the children of Israel ... so did your fathers when I sent them from Kadesh-barnea to see the land ... and the anger of the LORD burned on that day and he swore, saying: surely none of the men who came up from Egypt, from twenty years old and upward, shall see the land which I swore to Abraham, to Isaac and to Jacob ... save Caleb son of Jephunneh the Kenizzite and Joshua son of Nun ... and he made them wander in the wilderness forty years, until all the generation that did evil in the eyes of the LORD was consumed; and behold, you have risen in your fathers\' stead, a brood of sinful men ... and you will destroy all this people', 'moses'),
    ('Num 32:16-19 — and they drew near to him and said: folds for our cattle we will build here, and cities for our little ones; and we will arm ourselves, hastening, before the children of Israel until we have brought them to their place ... we will not return to our houses until the children of Israel have inherited every man his inheritance; for we will not inherit with them across the Jordan and beyond, because our inheritance has come to us on this side of the Jordan eastward', 'the-sons-of-gad-and-reuben'),
    ('Num 32:20-24 — and Moses said to them: if you do this thing, if you arm yourselves before the LORD for the war, and every armed one of you passes over the Jordan before the LORD until he has dispossessed his enemies from before him, and the land is subdued before the LORD, and afterward you return — you shall be clear before the LORD and before Israel, and this land shall be yours for a possession before the LORD; and if you do not do so, behold, you have sinned against the LORD, and know your sin which will find you; build for yourselves cities for your little ones and folds for your sheep, and that which has gone out of your mouth you shall do', 'moses'),
    ('Num 32:25-27 — and the sons of Gad and the sons of Reuben spoke to Moses, saying: your servants will do as my lord commands; our little ones, our wives, our cattle and all our beasts shall be there in the cities of Gilead; and your servants will pass over, every armed one for war before the LORD, to the war, as my lord says', 'the-sons-of-gad-and-reuben'),
    ('Num 32:28-30 — and Moses commanded concerning them Eleazar the priest, and Joshua son of Nun, and the heads of the fathers of the tribes of the children of Israel; and Moses said to them: if the sons of Gad and the sons of Reuben pass over the Jordan with you, every armed one for war before the LORD, and the land is subdued before you, you shall give them the land of Gilead for a possession; and if they do not pass over armed with you, they shall take possessions among you in the land of Canaan', 'moses'),
    ('Num 32:31-32 — and the sons of Gad and the sons of Reuben answered, saying: that which the LORD has spoken to your servants, so will we do; we will pass over armed before the LORD to the land of Canaan, and the possession of our inheritance with us across the Jordan', 'the-sons-of-gad-and-reuben'),
    ('Num 32:33 — and Moses gave to them — to the sons of Gad and to the sons of Reuben and to half the tribe of Manasseh son of Joseph — the kingdom of Sihon king of the Amorite and the kingdom of Og king of Bashan, the land with its cities in the borders, the cities of the land round about', 'moses'),
    ('Num 32:34-38 — and the sons of Gad built Dibon and Ataroth and Aroer, and Atroth-shophan and Jazer and Jogbehah, and Beth-nimrah and Beth-haran, fortified cities and folds for sheep; and the sons of Reuben built Heshbon and Elealeh and Kiriathaim, and Nebo and Baal-meon (their names being changed) and Sibmah, and they called by names the names of the cities which they built', 'the-sons-of-gad-and-reuben'),
    ('Num 32:39-40 — and the sons of Machir son of Manasseh went to Gilead and took it, and dispossessed the Amorite who was in it; and Moses gave Gilead to Machir son of Manasseh, and he dwelt in it', 'the-sons-of-machir'),
    ('Num 32:41 — and Jair son of Manasseh went and took their villages, and called them Havvoth-jair', 'jair'),
    ('Num 32:42 — and Nobah went and took Kenath and its daughters, and called it Nobah after his own name', 'nobah'),
]
CLOSES = 'one — the build debit (32:24) at 32:34-38; the stipulation (32:20-24) and the commission\'s charge (32:28-30) OPEN BY DESIGN to Joshua 22:1-9'


def scene():
    """THE SCENE — the exam's rows replayed on the world engine (the exodus epoch): the exam's persons through the four case kinds."""
    with contextlib.redirect_stdout(io.StringIO()):
        w = WE.World(era='Num 32:1-42: Mishnah Kiddushin 3:4, Shekalim 3:2 and the sugyot on the engine (the exodus epoch)', epoch='exodus')
        w.laws = [law_gad_reuben]
        w.advance(w.clock.day_in('exodus', 40, 6, 1))
        # ---- the exam's persons through the four case kinds (LITERAL submits — the daemon gate parses no loop) ----
        w.submit({'kind': 'stipulation_case', 'subject': 'the-undoubled-condition', 'person': 'the-undoubled-condition', 'ask': 'doubled_condition', 'case_source': 'Mishnah Kiddushin 3:4 — the exam\'s row doubled_condition'})
        w.submit({'kind': 'stipulation_case', 'subject': 'the-order-limb', 'person': 'the-order-limb', 'ask': 'four_limbs', 'case_source': 'Gittin 75a:11 — the exam\'s row four_limbs'})
        w.submit({'kind': 'stipulation_case', 'subject': 'the-negative-arm', 'person': 'the-negative-arm', 'ask': 'negative_arm_outcome', 'case_source': 'Kiddushin 61b:2 — the exam\'s row negative_arm_outcome'})
        w.submit({'kind': 'stipulation_case', 'subject': 'the-gift-from-now', 'person': 'the-gift-from-now', 'ask': 'from_now', 'case_source': 'Gittin 75b:2 — the exam\'s row from_now'})
        w.submit({'kind': 'stipulation_case', 'subject': 'the-counter-torah', 'person': 'the-counter-torah', 'ask': 'condition_counter_to_torah', 'case_source': 'Bava Metzia 94a:2 — the exam\'s row condition_counter_to_torah'})
        w.submit({'kind': 'stipulation_case', 'subject': 'the-impossible-condition', 'person': 'the-impossible-condition', 'ask': 'impossible_condition', 'case_source': 'Bava Metzia 94a:14 — the exam\'s row impossible_condition'})
        w.submit({'kind': 'stipulation_case', 'subject': 'the-bill-undoubled', 'person': 'the-bill-undoubled', 'ask': 'undoubled_on_a_bill', 'case_source': 'Gittin 75a:10 — the exam\'s row undoubled_on_a_bill'})
        w.submit({'kind': 'stipulation_case', 'subject': 'the-scope', 'person': 'the-scope', 'ask': 'the_scope', 'case_source': 'Shevuot 36a:27 — the exam\'s row the_scope'})
        w.submit({'kind': 'stipulation_case', 'subject': 'the-second-doubling', 'person': 'the-second-doubling', 'cell': 'charge', 'ask': 'second_doubling', 'case_source': 'Num 32:29-30 — the exam\'s row second_doubling'})
        w.submit({'kind': 'clearance_case', 'subject': 'the-clerk', 'person': 'the-clerk', 'ask': 'clerk', 'case_source': 'Mishnah Shekalim 3:2 — the exam\'s row clerk'})
        w.submit({'kind': 'clearance_case', 'subject': 'the-bakers', 'person': 'the-bakers', 'ask': 'bakers', 'case_source': 'Yoma 38a:9 — the exam\'s row bakers'})
        w.submit({'kind': 'clearance_case', 'subject': 'the-perfumers', 'person': 'the-perfumers', 'ask': 'perfumers', 'case_source': 'Yoma 38a:12 — the exam\'s row perfumers'})
        w.submit({'kind': 'clearance_case', 'subject': 'the-collectors', 'person': 'the-collectors', 'ask': 'collectors', 'case_source': 'Pesachim 13a:13-14 — the exam\'s row collectors'})
        w.submit({'kind': 'oath_retold_case', 'subject': 'the-two-of-six-hundred-thousand', 'person': 'the-two-of-six-hundred-thousand', 'ask': 'two_of_six_hundred_thousand', 'case_source': 'Sanhedrin 111a:6 — the exam\'s row two_of_six_hundred_thousand'})
        w.submit({'kind': 'oath_retold_case', 'subject': 'the-exceptions', 'person': 'the-exceptions', 'ask': 'the_exceptions', 'case_source': 'Num 32:12 — the exam\'s row the_exceptions'})
        w.submit({'kind': 'oath_retold_case', 'subject': 'calebs-hebron', 'person': 'calebs-hebron', 'ask': 'calebs_hebron', 'case_source': 'Sotah 34b:7 — the exam\'s row calebs_hebron'})
        w.submit({'kind': 'oath_retold_case', 'subject': 'the-set', 'person': 'the-set', 'ask': 'the_set', 'case_source': 'Num 32:11 — the exam\'s row the_set'})
        w.submit({'kind': 'oath_retold_case', 'subject': 'the-deaths-ceased', 'person': 'the-deaths-ceased', 'ask': 'generation_consumed', 'case_source': 'Bava Batra 121a:9 — the exam\'s row generation_consumed'})
        w.submit({'kind': 'oath_retold_case', 'subject': 'joshua-nothing-owed', 'person': 'joshua-nothing-owed', 'ask': 'joshua_nothing_owed', 'case_source': 'Sotah 35a:4 — the exam\'s row joshua_nothing_owed'})
        w.submit({'kind': 'land_east_case', 'subject': 'the-three-grantees', 'person': 'the-three-grantees', 'ask': 'three_parties', 'case_source': 'Num 32:33 — the exam\'s row three_parties'})
        w.submit({'kind': 'land_east_case', 'subject': 'the-land-held', 'person': 'the-land-held', 'ask': 'land_held', 'case_source': 'Bava Batra 119a:1 — the exam\'s row land_held'})
        w.submit({'kind': 'land_east_case', 'subject': 'the-not-by-lot', 'person': 'the-not-by-lot', 'ask': 'not_by_lot', 'case_source': 'Num 26:55 — the exam\'s row not_by_lot'})
        w.submit({'kind': 'land_east_case', 'subject': 'the-count', 'person': 'the-count', 'ask': 'the_count', 'case_source': 'Josh 4:13 — the exam\'s row the_count'})
        w.submit({'kind': 'land_east_case', 'subject': 'the-survivors', 'person': 'the-survivors', 'cell': 'machir', 'ask': 'survivors', 'case_source': 'Bava Batra 121b:9 — the exam\'s row survivors'})
        w.submit({'kind': 'land_east_case', 'subject': 'the-moses-grave', 'person': 'the-moses-grave', 'cell': 'cities', 'ask': 'moses_grave', 'case_source': 'Sotah 13b:20 — the exam\'s row moses_grave'})
        w.submit({'kind': 'land_east_case', 'subject': 'the-gads-eight', 'person': 'the-gads-eight', 'cell': 'cities', 'ask': 'gads_eight', 'case_source': 'Num 32:34-36 — the exam\'s row gads_eight'})
    n = lambda eid, eff: len([e for e in w.entity(eid).ledger if e['effect'] == eff])
    tset = len([l for l in w.log if l[0] == 'TIMER-SET']); tfire = len([l for l in w.log if l[0] == 'TIMER-FIRE']); tcan = len([l for l in w.log if l[0] == 'TIMER-CANCEL'])
    return ((n('the-undoubled-condition', 'commanded'), n('the-order-limb', 'commanded'), n('the-negative-arm', 'accepted'), n('the-gift-from-now', 'holding_given'), n('the-counter-torah', 'exempt'), n('the-impossible-condition', 'exempt'), n('the-bill-undoubled', 'exempt'), n('the-scope', 'accepted'), n('the-second-doubling', 'commanded'),
             n('the-clerk', 'clear_before_the_lord_and_israel'), n('the-bakers', 'clear_before_the_lord_and_israel'), n('the-perfumers', 'clear_before_the_lord_and_israel'), n('the-collectors', 'clear_before_the_lord_and_israel'),
             n('the-two-of-six-hundred-thousand', 'exempt'), n('the-exceptions', 'exempt'), n('calebs-hebron', 'holding_owed'), n('the-set', 'accepted'), n('the-deaths-ceased', 'accepted'), n('joshua-nothing-owed', 'exempt'),
             n('the-three-grantees', 'holding_given'), n('the-land-held', 'holding_given'), n('the-not-by-lot', 'accepted'), n('the-count', 'accepted'), n('the-survivors', 'accepted'), n('the-moses-grave', 'accepted'), n('the-gads-eight', 'cities_built')),
            (tset, tfire, tcan, len(w.timers)),
            len(w.entities)), w
SCENE, _W = scene()
# THE PREDICTION (typed before the first run, NUMBERS_WALK.md "Sitting 12b"): every exam person written once per effect — twenty-six ones; no timer in the
# chapter (set 0, fired 0, cancelled 0, pending 0). ENTITIES: the exam's 26 persons + the counterparties israel (the holding_given rows) and the-court
# (Caleb's holding_owed) and the-amorite (none in the scene — no land_possessed row asked) = 28.
SCENE_PREDICTED = ((1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1), (0, 0, 0, 0), 26)   # the 28 typed first counted the counterparties israel and the-court: an entity is a written-on party (the narrative's evidence, the same run) — 26
assert SCENE == SCENE_PREDICTED, ('THE NUMBERS WALK: the scene moved from its prediction', SCENE, SCENE_PREDICTED)


def narrative():
    """THE NUMBERS WALK 12b (2026-09-12): the chapter's own acts AS HISTORY — the TWELVE lines of 32:1-42 at the counter's day (40, 6, 1),
    page-order after Midian's thirteen (31:1-54), on a world with this runner's daemon: 13 writes, no timer, no marker, eleven entities, one
    close found on this world (the build debit at 32:34-38). Recorded by the sequential run's recorder and stitched onto the tape. Not a graded
    cell: the tuple below is a tripwire typed from the design; the sequence world's RUN tuple and CG1-CG9 grade the tape."""
    with contextlib.redirect_stdout(io.StringIO()):
        w = WE.World(era='Num 32:1-42: Gad and Reuben on the tape — the request, the oath retold, the condition, the commission, the grant, the cities, Machir, Jair and Nobah (the exodus epoch)', epoch='exodus')
        w.laws = [law_gad_reuben]
        w.advance(w.clock.day_in('exodus', 40, 6, 1))
        # THE DAEMON GATE READS LITERAL SUBMITS ONLY — the twelve lines typed out
        w.submit({'kind': 'land_requested', 'subject': 'the-sons-of-gad-and-reuben', 'to': 'moses', 'cities': NINE, 'request': 'for a possession; do not bring us over the Jordan', 'case_source': LINES[0][0]})
        w.submit({'kind': 'moses_rebuked_the_tribes', 'subject': 'moses', 'to': 'the-sons-of-gad-and-reuben', 'oath': 'he swore (32:10) — chapter 14\'s "as I live"', 'set': TWENTY, 'exceptions': ['caleb', 'joshua'], 'years': FORTY, 'case_source': LINES[1][0]})
        w.submit({'kind': 'tribes_offered_to_arm', 'subject': 'the-sons-of-gad-and-reuben', 'folds': 'for our cattle', 'cities': 'for our little ones', 'arm': 'before the children of Israel', 'until_when': 'every man has inherited', 'case_source': LINES[2][0]})
        w.submit({'kind': 'condition_stipulated', 'subject': 'moses', 'to': 'the-sons-of-gad-and-reuben', 'positive_arm': 'cross armed before the LORD until the land is subdued — clear, and the land yours for a possession', 'negative_arm': 'your sin will find you', 'clearance': 'before the LORD and before Israel', 'utterance_rule': '32:24 = 30:3', 'build': 'cities for your little ones and folds for your sheep', 'case_source': LINES[3][0]})
        w.submit({'kind': 'tribes_accepted_the_condition', 'subject': 'the-sons-of-gad-and-reuben', 'to': 'moses', 'order': 'our little ones, our wives, our cattle', 'case_source': LINES[4][0]})
        w.submit({'kind': 'commission_charged', 'subject': 'moses', 'to': 'the-dividers-of-the-land', 'positive_arm': 'give them the land of Gilead for a possession', 'negative_arm': 'they take possessions among you in Canaan', 'case_source': LINES[5][0]})
        w.submit({'kind': 'tribes_answered_so_will_we_do', 'subject': 'the-sons-of-gad-and-reuben', 'to': 'moses', 'the_lords_word': 'that which the LORD has spoken to your servants', 'case_source': LINES[6][0]})
        w.submit({'kind': 'land_granted_east', 'subject': 'moses', 'to': ['the-sons-of-gad', 'the-sons-of-reuben', 'the-half-tribe-of-manasseh'], 'kingdoms': ['סיחן', 'עוג'], 'count': TWO_AND_A_HALF, 'case_source': LINES[7][0]})
        w.submit({'kind': 'cities_built_east', 'subject': 'the-sons-of-gad-and-reuben', 'gad': GAD_CITIES, 'reuben': REUBEN_CITIES, 'renamed': ['נבו', 'בעל מעון'], 'case_source': LINES[8][0]})
        w.submit({'kind': 'gilead_taken_by_machir', 'subject': 'the-sons-of-machir', 'took': 'Gilead', 'dispossessed': 'the-amorite', 'given': 'by Moses to Machir son of Manasseh', 'case_source': LINES[9][0]})
        w.submit({'kind': 'villages_taken_by_jair', 'subject': 'jair', 'took': 'their villages', 'named': 'Havvoth-jair', 'case_source': LINES[10][0]})
        w.submit({'kind': 'kenath_taken_by_nobah', 'subject': 'nobah', 'took': 'Kenath and its daughters', 'named': 'Nobah', 'case_source': LINES[11][0]})
    writes = len([l for l in w.log if l[0] == 'WRITE'])
    closes = len([e for ent in w.entities.values() for e in ent.ledger if e.get('closed_by')])
    return (writes, len([l for l in w.log if l[0] == 'TIMER-SET']), len(w.entities), w.clock.eras['exodus'].date(w.clock.day)[1:], closes), w


NARRATIVE, _WN = narrative()
NARRATIVE_PREDICTED = (13, 0, 8, (6, 1), 1)   # NUMBERS_WALK.md "Sitting 12b": 13 writes (L1 1, L2 0, L3 0, L4 2, L5 0, L6 1, L7 0, L8 3, L9 2, L10 2, L11 1, L12 1), no timer, EIGHT entities — the WRITTEN-ON parties alone (the compound party, the dividers, the three grantees, the sons of Machir, jair, nobah): the design's eleven had counted moses (a speech subject with no write here) and the counterparties israel and the-amorite — AN ENTITY IS A WRITTEN-ON PARTY, the first run's evidence (retyped); the date (6, 1) of the fortieth year, one close found on this world (the build debit)
assert NARRATIVE == NARRATIVE_PREDICTED, ('THE NUMBERS WALK: Gad and Reuben\'s narrative moved from its prediction', NARRATIVE, NARRATIVE_PREDICTED)


# =====================================================================
# Motion 2 — THE TEST DATA: the answer sheet's rows (the docket's LAW rows).
# =====================================================================
CASES = [
    # F1 — the request
    ('Num 32:1-2 — the parties: the ink\'s compound at six seats', lambda: the_request({'ask': 'the_parties'}, DATA), "the sons of Gad and the sons of Reuben — the ink's compound at six seats (32:2, 6, 25, 29, 31, 33), Gad first; Reuben first at 32:1 alone"),
    ('Num 32:1 / Bekhorot 4b:7 — much cattle', lambda: the_request({'ask': 'much_cattle'}, DATA), "much cattle, very numerous (32:1) — a place for cattle at its one seat; the land of Jazer one seat; Bekhorot 4b:7's premise"),
    ('Num 32:2 / 27:2 — the triad without the halt', lambda: the_request({'ask': 'the_triad'}, DATA), "to Moses, to Eleazar the priest and to the princes of the congregation (32:2) — 27:2's triad without the halt: no case brought before the LORD"),
    ('Num 32:3 / Berakhot 8b:1 — the nine cities', lambda: the_request({'ask': 'the_nine'}, DATA), "nine cities asked (32:3) — Ataroth, Dibon, Jazer, Nimrah, Heshbon, Elealeh, Sebam, Nebo, Beon; Onkelos renders them by Aramaic names (Berakhot 8b:1's premise against the store)"),
    ('Num 32:4-5 — the request', lambda: the_request({'ask': 'the_request'}, DATA), "let this land be given to your servants for a possession; do not bring us over the Jordan (32:5) — the plea's two clauses; 'a possession' Joseph's word (Genesis 47:11)"),
    ('Num 32:16 / 32:24 — the cattle before the children', lambda: the_request({'ask': 'order_of_the_offer'}, DATA), "the cattle before the children (32:16) reversed by Moses (32:24) — the ink's two orders; no row of the declared spine"),
    # F2 — the rebuke and the oath retold
    ('Num 32:6 / Judges 5:16 — shall your brothers go to war', lambda: the_rebuke({'ask': 'brothers_to_war'}, DATA), "shall your brothers go to war and you sit here? (32:6) — one seat; Deborah's question on Reuben (Judges 5:16) observed"),
    ('Num 32:7 / 30:6-12 — the hinder-root', lambda: the_rebuke({'ask': 'hinder_root'}, DATA), "why do you discourage the heart (32:7) — the vows' verb: six Torah tokens all in chapters 30 and 32; 14:34's 'my alienation' the noun"),
    ('Num 32:8 / Sotah 34b:3 — the spies\' verb; when I sent them', lambda: the_rebuke({'ask': 'the_spies_verb'}, DATA), "'to see the land' (32:8) — the spies' verb at each telling: 13:2's 'tour', Deuteronomy 1:22's 'search', 1:24's 'scout'; 'when I sent them' Moses' own first person (Sotah 34b:3's 'send you')"),
    ('Num 32:10 / 14:21, 28 — the oath supplied', lambda: the_rebuke({'ask': 'the_oath_supplied'}, DATA), "'and he swore, saying' (32:10) — chapter 14 says 'as I live' (14:21, 28); Deuteronomy 1:34 supplies the verb too: the oath retold with the verb supplied"),
    ('Num 32:11 / 14:29 by CALL — the set', lambda: the_rebuke({'ask': 'the_set'}, DATA), "from twenty years old and upward (32:11) — the census formula's twenty-three seats; the doomed set 603,550 by CALL (SL.decree set)"),
    ('Num 32:12 / 14:24, 30 by CALL — the exceptions', lambda: the_rebuke({'ask': 'the_exceptions'}, DATA), "save Caleb son of Jephunneh the Kenizzite and Joshua son of Nun (32:12) — SL.decree exceptions by CALL: Caleb and Joshua (14:24, 14:30); 'followed the LORD fully' Caleb's phrase"),
    ('Num 32:12 / Genesis 15:19 — the Kenizzite', lambda: the_rebuke({'ask': 'caleb_the_kenizzite'}, DATA), "the Kenizzite (32:12) — Genesis 15:19's nation as Caleb's gentilic (Joshua 14:6, 14); Othniel son of Kenaz; no docket row — the ink's arm"),
    ('Sotah 34b:7-8; Bava Batra 122a:12 — Caleb\'s Hebron', lambda: the_rebuke({'ask': 'calebs_hebron'}, DATA), "Caleb's Hebron — holding_owed (14:24 'the land where he went'), paid at Joshua 14:13-14 outside the Torah; Sotah 34b:7 the graves; 'another spirit' a change over time (34b:8)"),
    ('Sotah 35a:4; Bava Batra 122a:12 — Joshua, nothing owed', lambda: the_rebuke({'ask': 'joshua_nothing_owed'}, DATA), "Joshua excepted (32:12) and nothing owed him in the ink — Sotah 35a:4 'a severed head, no children'; Timnath-serah by the LORD's word (Joshua 19:50; Bava Batra 122a:12)"),
    ('Num 32:13 / 14:33-34; Deut 2:14 — forty years', lambda: the_rebuke({'ask': 'forty_years'}, DATA), "forty years (32:13) — the parser's [40] = SL.FORTY_YEARS; the timer fired at (40, 5, 9) on the tape; Deuteronomy 2:14's thirty-eight from Kadesh"),
    ('Num 32:13 / Bava Batra 121a:9 — the generation consumed', lambda: the_rebuke({'ask': 'generation_consumed'}, DATA), "until all the generation was consumed (32:13) — Deuteronomy 2:14's phrase; the deaths ceased on the fifteenth of Av (SL.decree deaths_ceased by CALL; Bava Batra 121a:9)"),
    ('Num 32:13 — he made them wander', lambda: the_rebuke({'ask': 'made_them_wander'}, DATA), "he made them wander in the wilderness (32:13) — the causative's one Torah seat"),
    ('Num 32:13 — the Kings\' formula at its first seat', lambda: the_rebuke({'ask': 'evil_formula'}, DATA), "who did evil in the eyes of the LORD (32:13) — the Judges' and Kings' formula, fifty-three seats, at its first seat in the Bible's order"),
    ('Num 32:14 / Genesis 13:13; 25:4 — a brood of sinful men', lambda: the_rebuke({'ask': 'brood'}, DATA), "a brood of sinful men (32:14) — 'brood' a hapax, 'sinners' Sodom's word (Genesis 13:13); 'to add yet to the fierce anger of the LORD' Peor's phrase (25:4)"),
    ('Num 32:15 — the threat, no write', lambda: the_rebuke({'ask': 'the_threat'}, DATA), "'he will yet again leave them in the wilderness and you will destroy all this people' (32:15) — a conditional threat in Moses' mouth: no write"),
    ('Sanhedrin 111a:6; Bava Batra 121b:8, 121b:11 — two of six hundred thousand', lambda: the_rebuke({'ask': 'two_of_six_hundred_thousand'}, DATA), "two of six hundred thousand entered — Caleb and Joshua (Rav Simai, Sanhedrin 111a:6); the decree not on Levi (Bava Batra 121b:8) nor under twenty or over sixty (121b:11)"),
    ('Sanhedrin 111a:12-13 — slow to anger; the pardon', lambda: the_rebuke({'ask': 'slow_to_anger'}, DATA), "'the LORD's anger burned' (32:10, 13) — the pardon of 14:20 preceded it (SL.decree pardon by CALL); slow to anger at the spies' sin (Sanhedrin 111a:12-13)"),
    # F3 — the offer
    ('Num 32:16 — folds and cities', lambda: the_offer({'ask': 'folds_and_cities'}, DATA), "folds for our cattle and cities for our little ones (32:16) — the offer's order; the cattle first"),
    ('Num 32:17 — we will arm ourselves (seven tokens)', lambda: the_offer({'ask': 'we_will_arm'}, DATA), "and we will arm ourselves, hastening, before the children of Israel (32:17) — the arm-root's seven tokens in the chapter"),
    ('Num 32:18 / Deut 3:20; Josh 1:15, 22:4 — we will not return', lambda: the_offer({'ask': 'not_return'}, DATA), "we will not return to our houses until the children of Israel have inherited every man his inheritance (32:18) — one seat; the retellings 'until the LORD gives rest' (Deuteronomy 3:20, Joshua 1:15); the release Joshua 22:4"),
    ('Josh 1:14, 4:12-13 — Joshua\'s armed in the consonants of fifty', lambda: the_offer({'ask': 'joshuas_armed'}, DATA), "Joshua's 'armed' in the consonants of 'fifty' (Joshua 1:14, 4:12 chamushim) — told by the u-vowel and the doubling dot; 4:13's chalutsei the chapter's word"),
    ('Num 32:19 — east of the Jordan', lambda: the_offer({'ask': 'east_of_jordan'}, DATA), "our inheritance has come to us on this side of the Jordan eastward (32:19) — the offer's ground"),
    # F4 — the condition
    ('Num 32:20-22 — the positive arm', lambda: the_condition({'ask': 'positive_arm'}, DATA), "if you arm yourselves before the LORD for the war and every armed one passes over the Jordan until the land is subdued, and afterward you return — clear, and this land yours for a possession (32:20-22): the positive arm; 'before the LORD' seven tokens"),
    ('Num 32:23 / Genesis 44:16 — the negative arm', lambda: the_condition({'ask': 'negative_arm'}, DATA), "and if you do not do so, you have sinned against the LORD, and know your sin which will find you (32:23) — the negative arm; Judah's idiom (Genesis 44:16)"),
    ('Mishnah Kiddushin 3:4 — the doubled condition', lambda: the_condition({'ask': 'doubled_condition'}, DATA), "the doubled condition — R. Meir: every condition not doubled like Gad and Reuben's is none; R. Chanina ben Gamliel: the doubling was needed there for its own sake (Mishnah Kiddushin 3:4)"),
    ('Gittin 75a:11-75b:6; Bava Metzia 94a — the law of all conditions', lambda: the_condition({'ask': 'four_limbs'}, DATA), "the law of all conditions from this chapter (Gittin 75a:11): doubled; the condition before the act (75a:12; Bava Metzia 94a:3); the positive before the negative (Gittin 75b:6); the condition's matter and the act's distinct (75a:14); a condition that can be fulfilled — the ruling as R. Yehuda ben Teima (Bava Metzia 94a:14)"),
    ('Kiddushin 61b:2, 61b:5-8 — the negative arm\'s outcome', lambda: the_condition({'ask': 'negative_arm_outcome'}, DATA), "'they shall take possessions among you in the land of Canaan' (32:30) — Gilead shared or Canaan only; without the doubling no portion anywhere or Gilead anyway (Kiddushin 61b:2, 61b:5-8)"),
    ('Gittin 75b:2 — on condition is from now', lambda: the_condition({'ask': 'from_now'}, DATA), "'on condition' is 'from now' (Rav Huna in Rav's name, Gittin 75b:2) — the grant of 32:33 takes effect at once under the condition; the transfer written at the grant, the debit open beside it"),
    ('Num 32:22 / Shekalim 3:2; Yoma 38a; Pesachim 13a — the clearance', lambda: the_condition({'ask': 'the_clearance'}, DATA), "clear before the LORD and before Israel (32:22) — one seat; a person must appear justified before people as before the Omnipresent (Mishnah Shekalim 3:2; Yoma 38a:9, 38a:12; Pesachim 13a:13-14); 1 Chronicles 22:18 the double in Chronicles' ink"),
    ('Mishnah Shekalim 3:2 — the clerk', lambda: the_condition({'ask': 'clerk'}, DATA), "Mishnah Shekalim 3:2 — clear before the LORD and before Israel (32:22): the one who collects from the treasury chamber enters with no cuffed garment, shoe, sandal, phylacteries or amulet — lest he become poor or rich and be suspected"),
    ('Yoma 38a:9 — the bakers', lambda: the_condition({'ask': 'bakers'}, DATA), "Yoma 38a:9 — clear before the LORD and before Israel (32:22): the House of Garmu's descendants never held refined bread — so that people would not say they are sustained from the showbread's technique"),
    ('Yoma 38a:12 — the perfumers', lambda: the_condition({'ask': 'perfumers'}, DATA), "Yoma 38a:12 — clear before the LORD and before Israel (32:22): the House of Avtinas's brides never perfumed; a wife from elsewhere STIPULATED not to — a condition on a marriage at the rule's own seat"),
    ('Pesachim 13a:13-14 — the collectors', lambda: the_condition({'ask': 'collectors'}, DATA), "Pesachim 13a:13-14 — clear before the LORD and before Israel (32:22): the charity collectors sell to others and change money with others, not with their own coins"),
    ('Num 32:24 / 30:3 by CALL — the utterance rule\'s second seat', lambda: the_condition({'ask': 'utterance_rule'}, DATA), "that which has gone out of your mouth you shall do (32:24) — 30:3's 'all that goes out of his mouth he shall do', the phrase's two seats; the vows' cell by CALL: the vow's fulfilment — a positive duty, a prohibition, and the court's compulsion"),
    ('Num 32:24 / 30:3; Judges 11:36 — the lemma pair', lambda: the_condition({'ask': 'the_lemma_pair'}, DATA), "'goes out' + 'mouth' adjacent at nine seats — Numbers 30:3 and 32:24 the Torah's two, Judges 11:36 Jephthah's daughter among the seven outside"),
    ('Num 32:24 — the build command', lambda: the_condition({'ask': 'the_build_command'}, DATA), "build for yourselves cities for your little ones and folds for your sheep (32:24) — Moses' order reversed: the children first; the run at 32:34-38 closes it"),
    ('Num 32:21-22 / Sotah 3a:8-9 — the verb of the future', lambda: the_condition({'ask': 'the_verb_future'}, DATA), "'and every armed one of you will pass over' (32:21) read of the future — 'the land subdued... and you return afterward' fixes it (Sotah 3a:8-9)"),
    ('Mishnah Bava Metzia 94a:2 — a condition counter to the Torah', lambda: the_condition({'ask': 'condition_counter_to_torah'}, DATA), "a condition counter to the Torah on a non-monetary matter is void; in monetary matters the parties may agree (Mishnah Bava Metzia 94a:2)"),
    ('Bava Metzia 94a:11-14 — an impossible condition', lambda: the_condition({'ask': 'impossible_condition'}, DATA), "a condition that cannot be fulfilled — the act stands and the condition is void, the ruling as R. Yehuda ben Teima (Bava Metzia 94a:11-14); the Rabbis: binding"),
    ('Gittin 75a:10, 75a:13 — an undoubled condition on a bill', lambda: the_condition({'ask': 'undoubled_on_a_bill'}, DATA), "an undoubled condition on a bill of divorce — no condition according to R. Meir, the act stands (Gittin 75a:10); the action preceding the condition the same (75a:13)"),
    ('Shevuot 36a:27, 36a:29 — the rule\'s scope', lambda: the_condition({'ask': 'the_scope'}, DATA), "R. Meir refuses the inference in monetary matters only (Shevuot 36a:27) — or everywhere (36a:29; the sotah's spelling): the rule's scope, both readings"),
    ('Onkelos 32:20-32 — before the people of the LORD', lambda: the_condition({'ask': 'onkelos_buffer'}, DATA), "'before the people of the LORD' at the six martial seats of Onkelos Numbers, all this chapter's (32:20, 21, 22, 27, 29, 32); the three legal seats kept — the reading's claim MT32A-06"),
    # F5 — the acceptance and the charge
    ('Num 32:25, 27 — my lord', lambda: the_acceptance_and_the_charge({'ask': 'servants_will_do'}, DATA), "your servants will do as my lord commands (32:25) — 'my lord' for Moses at 32:25, 27 (Joshua's 11:28, Aaron's 12:11, the Gileadite heads' 36:2)"),
    ('Num 32:26 / Deut 3:19; Josh 1:14 — the order held', lambda: the_acceptance_and_the_charge({'ask': 'the_order_reversed'}, DATA), "our little ones, our wives, our cattle and all our beasts (32:26) — Moses' order held; the retellings 'your wives, your little ones, your cattle' (Deuteronomy 3:19, Joshua 1:14)"),
    ('Num 32:28 / Josh 14:1, 21:1; Bava Batra 122a:4 — the commission', lambda: the_acceptance_and_the_charge({'ask': 'the_commission'}, DATA), "Eleazar the priest, Joshua son of Nun and the heads of the fathers of the tribes (32:28) — Joshua 14:1's dividers word for word, 21:1 the third form; Bava Batra 122a:4's lottery"),
    ('Num 32:29-30 — the second doubling', lambda: the_acceptance_and_the_charge({'ask': 'second_doubling'}, DATA), "if they pass over — give them Gilead; if not — they take possessions among you in Canaan (32:29-30): the second doubling, the exam's proof verses; the commission's debit open to Joshua 22"),
    ('Num 32:31 / Josh 22:9 — the LORD\'s word', lambda: the_acceptance_and_the_charge({'ask': 'the_lords_word'}, DATA), "that which the LORD has spoken to your servants, so will we do (32:31) — Moses' stipulation called the LORD's word; Joshua 22:9 'by the commandment of the LORD by the hand of Moses': a law in Moses' voice with no divine frame"),
    ('Num 32:32 / 27:7 — we, the possession of our inheritance', lambda: the_acceptance_and_the_charge({'ask': 'we_short'}, DATA), "'we' in its short form (32:32) — three Bible seats (Genesis 42:11, Lamentations 3:42); 'the possession of our inheritance' the daughters' construct (27:7)"),
    # F6 — the grant
    ('Num 32:33 — the three parties', lambda: the_grant({'ask': 'three_parties'}, DATA), "to the sons of Gad, to the sons of Reuben and to half the tribe of Manasseh (32:33) — three transfers; half Manasseh first named at the grant"),
    ('Num 32:33 / 21:24-35 by CALL — the two kingdoms', lambda: the_grant({'ask': 'two_kingdoms'}, DATA), "the kingdom of Sihon king of the Amorite (one seat) and the kingdom of Og king of Bashan (Deuteronomy 3's and this) — the chukat runner's land possessed at 21:24-35 by CALL: the grant's source"),
    ('Deut 3:18-20; Josh 1:12-15; Bava Batra 118b:8 — half Manasseh\'s stipulation', lambda: the_grant({'ask': 'half_manassehs_stipulation'}, DATA), "no stipulation spoken to half Manasseh in the chapter; Deuteronomy 3:18-20, Joshua 1:12-15, 4:12 extend the crossing to the three; Joshua 17:5-6 'beside the land of Gilead and Bashan' (Bava Batra 118b:8)"),
    ('Num 26:7, 18, 34 by CALL; Josh 4:13; 1 Chr 5:18 — the two and a half\'s count', lambda: the_grant({'ask': 'the_count'}, DATA), "the two and a half's count — 43,730 + 40,500 + 52,700 ÷ 2 = 110,580 from the second census by CALL; Joshua 4:13's about forty thousand; 1 Chronicles 5:18's 44,760"),
    ('Bava Batra 119a:1, 119a:5 by CALL — the land held', lambda: the_grant({'ask': 'land_held'}, DATA), "in possession before assignment — the rows are holdings before the lot (C2 by CALL; Bava Batra 119a:1, 119a:5): the standing 'a possession' carries"),
    ('Num 26:55 by CALL — not by lot', lambda: the_grant({'ask': 'not_by_lot'}, DATA), "the east by Moses' word, not by lot — 26:55's lot is Canaan's (C2 by CALL: the place by lot, Joshua 14-19 the run); the OPEN divide_the_land not this chapter's run"),
    ('Bava Batra 119b:3-4 by CALL — bequeath and not inherit', lambda: the_grant({'ask': 'bequeath_not_inherit'}, DATA), "the exodus generation bequeath and do not inherit (Bava Batra 119b:3-4; C2 morasha by CALL) — the doomed set's title to the land"),
    # F7 — the cities
    ('Num 32:34-36 — Gad\'s eight', lambda: the_cities({'ask': 'gads_eight'}, DATA), "Dibon, Ataroth, Aroer, Atroth-shophan, Jazer, Jogbehah, Beth-nimrah, Beth-haran — Gad's eight (32:34-36), fortified cities and folds for sheep"),
    ('Num 32:37-38 — Reuben\'s six', lambda: the_cities({'ask': 'reubens_six'}, DATA), "Heshbon, Elealeh, Kiriathaim, Nebo, Baal-meon and Sibmah — Reuben's six (32:37-38); 'their names being changed' one seat"),
    ('Num 32:3 / 32:34-38 — the nine split four and five', lambda: the_cities({'ask': 'the_split'}, DATA), "the nine asked split four and five — Gad's Ataroth, Dibon, Jazer, Nimrah (as Beth-nimrah); Reuben's Heshbon, Elealeh, Sebam (as Sibmah), Nebo, Beon (as Baal-meon)"),
    ('Num 33:45-46 — Dibon Gad', lambda: the_cities({'ask': 'dibon_gad'}, DATA), "Dibon Gad (33:45-46) — the itinerary's own witness to the city's tribe, the next chapter's"),
    ('Josh 13:17, 13:26, 13:20 — the two crossed cities', lambda: the_cities({'ask': 'two_crossed'}, DATA), "Dibon and Heshbon in Reuben's list at Joshua 13:17, Heshbon on Gad's border at 13:26 — the two crossed between the tribes; Beth-peor Reuben's (13:20)"),
    ('Sotah 13b:20; Onkelos 32:3 — Moses\' grave', lambda: the_cities({'ask': 'moses_grave'}, DATA), "Nebo Reuben's (32:37-38) — Moses died in Reuben's portion (Sotah 13b:20); Onkelos 'Nebo, the burial place of Moses' at 32:3; the Sifrei 106:1's Gad the other arm"),
    ('Num 32:34-38 / 32:24 — the build debit closed', lambda: the_cities({'ask': 'the_build_closed'}, DATA), "the cities built (32:34-38) — the run of 32:24's 'build for yourselves cities': the build debit closed by value, the chapter's one Torah-closed debit"),
    # F8 — Machir, Jair and Nobah
    ('Num 32:39 / Genesis 50:23; 21:32 — the sons of Machir', lambda: machir_jair_nobah({'ask': 'sons_of_machir'}, DATA), "the sons of Machir son of Manasseh (32:39) — Genesis 50:23's collective, born on Joseph's knees; Gilead taken, the Amorite dispossessed (21:32's verb)"),
    ('Num 32:40 / 26:29; Josh 17:1 — Gilead given to Machir', lambda: machir_jair_nobah({'ask': 'gilead_given'}, DATA), "Moses gave Gilead to Machir son of Manasseh (32:40) — the clan under the ancestor's name (26:29; Joshua 17:1 the man of war; Deuteronomy 3:15)"),
    ('Num 32:41 — Jair and Havvoth-jair', lambda: machir_jair_nobah({'ask': 'jair'}, DATA), "Jair son of Manasseh took their villages and called them Havvoth-jair (32:41) — six seats; 'went and took' at 32:41-42 alone"),
    ('Num 32:41 / 1 Chr 2:21-22; Judges 10:4 — Jair\'s two lineages', lambda: machir_jair_nobah({'ask': 'jairs_lineage'}, DATA), "Jair son of Manasseh (32:41; Deuteronomy 3:14; 1 Kings 4:13) against 1 Chronicles 2:21-22's Hezron's grandson by Machir's daughter, twenty-three cities — the ink's two accounts; the judge Jair's thirty (Judges 10:4)"),
    ('Bava Batra 121b:9-11 — Jair and Machir the survivors', lambda: machir_jair_nobah({'ask': 'survivors'}, DATA), "Jair and Machir born in Jacob's days and did not die until the entry — 'about thirty-six' at Ai read as Jair alone (Bava Batra 121b:9-10); already old at the decree (121b:11)"),
    ('Num 32:42 / Judges 8:11; 1 Chr 2:23 — Nobah', lambda: machir_jair_nobah({'ask': 'nobah'}, DATA), "Nobah took Kenath and its daughters and called it Nobah after his own name (32:42) — Nobah and Jogbehah together at Judges 8:11 on Gideon's route; Kenath's other seat 1 Chronicles 2:23"),
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
    print('THE INK: integers %s; ordinals none; starred none; marked none; the frame verbs %s (no divine frame)' % (sorted(INTS.items()), FRAME_VERBS))
    print('THE ARITHMETIC: the two and a half %d = %d + %d + %d / 2; Joshua 4:13\'s %d; 1 Chronicles 5:18\'s %d; the arm-root %d tokens; "before the LORD" %d tokens' % (TWO_AND_A_HALF, C2.C26['reuben'], C2.C26['gad'], C2.C26['manasseh'], FORTY_THOUSAND, CHRONICLES_COUNT, len(ARM_TOKENS), len(BEFORE_THE_LORD_32)))
    print('THE SCENE on the bench: %s; the timers (set, fired, cancelled, pending) %s; entities %d' % SCENE)
    print('THE NARRATIVE: %s' % (NARRATIVE,))
    print('THE PARAMETER ROWS: ' + '; '.join('%s = %s' % (k, DATA[k]['value']) for k in DATA) + ' (the other settings recorded in DATA)')
    if ok == len(CASES):
        print('\nTHE COMPILE OF GAD AND REUBEN: the answer sheet REPRODUCED — %d/%d' % (ok, len(CASES)))
    sys.exit(0 if ok == len(CASES) else 1)

#!/usr/bin/env python3
# DEUTERONOMY 1:1-3:29 WITH NUMBERS 27:12-23 — THE OPENING SPEECH AND JOSHUA'S COMMISSION (THE DEUTERONOMY WALK sitting 1b, 2026-09-15;
# World/step9/DEUTERONOMY_WALK.md "Sitting 1b"; the state doc's #183-#184). THE READBACK'S FIRST FORM (THE_LOOP.md step 6; the owner's
# "Yes 1. Go"): A RETELLING IS A REFERENCE ROW, NEVER A SECOND ACT — the DATA table the_readback carries one row per retold act with the
# tape's kind and first verse, the ledger entry the speech presupposes, and THE GRADE (VERBATIM / TURNED / SHORTENED / EXPANDED / SUPPLIED /
# DISAGREES), the deltas RECOMPUTED from the DB; an act told only in the retelling is written ONCE, at the time it happened, dated by a
# RETROGRADE marker, and where the tape already holds its run the debit is CLOSED IN THE SAME BLOCK BY THE PRIOR RUN (closed_by naming the
# run's line); a disagreement is an OPEN row; a receipt inside a retelling is a RUN CITATION; the frame (1:1-5) the book's one act of its own
# day — torah_expounded on Israel at (40, 11, 1). THE LAW OF THE SPAN: the judges' charge (1:16-18) — ONE STATUS on the court, judges_charged,
# the six clauses its value, dated (1, 2, 16) by the court's founding day read off Israel's ledger; the daemon law_opening_speech given_at
# Deut 1:16, installed_by BOOT with the class NAMED (a law in Moses' voice with no divine frame — the vows' class, the second pass's D2
# question). THE CALLEE: Numbers 27:12-23 compiled as F0 — four lines after the daughters' (page_order at (40, 6, 1)): the ascent commanded
# (a debit on Moses OPEN to Deuteronomy 34:1-4), the shepherd asked, the commission commanded, Joshua commissioned (invested_office; the
# commission's debit CLOSED by its run — the register seat Num 27:22). Eight cells; every token probed (zero-report law); effects on every
# cell (the effects law); the parameters the ink leaves open recorded in DATA with their arms; twenty-four DATA rows. Reading ledger:
# logic/oral_triage/deu_01_03_devarim_2026-09-15.md (259 sources, 21 claims); the exam's docket: logic/oral_triage/deu_01_03_devarim_exam_2026-09-15.md
# (864 rows: LAW 83 / DERIVATION 93 / DISPUTE 29 / CONTEXT 631 / OUTSIDE 28).

# ---- THE HONEST-PAIRING GUARD ----------------------------------------------------------------------------
import os as _os, sys as _sys
_sys.path.insert(0, _os.path.dirname(_os.path.abspath(__file__)))
_ROOT = _os.path.normpath(_os.path.join(_os.path.dirname(_os.path.abspath(__file__)), '..', '..'))   # THE PORTABLE REPO: the repo root from this file's own place
from compile_guards import check_honest_pairing as _chp
_P = _os.path.abspath(__file__)
GUARDED = _chp(_P, 'CASES', 2)
assert GUARDED == 97, ("the guard counted %d expectations, the tripwire holds 97" % GUARDED)   # the cells' asks summed by the generator before the first run (F0 8, F1 7, F2 28, F3 17, F4 13, F5 11, F6 6, F7 7); the design estimated ~91
print('guard: %d expectations checked, every one a literal from the answer sheet [honest-pairing guard satisfied]' % GUARDED)
import sqlite3, sys, io, re, contextlib, collections, unicodedata, yaml
from fractions import Fraction
import effects_layer as FX
import world_engine as WE
import cold_run_exodus_story as ES            # THE EDGE: opening_speech -> exodus_story CALL, reference (18:21-26's judges retold at 1:9-15; the manna's forty years at 2:7; the pillar at 1:33)
import cold_run_shelach as SL                 # THE EDGE: opening_speech -> shelach CALL, reference (13-14 READ BACK at 1:19-46; the decree's rows read at the readback checkpoint)
import cold_run_chukat as CK                  # THE EDGE: opening_speech -> chukat CALL, reference (20-21 READ BACK at 2:1-3:11; the edom_passage DISPUTE row; the prior runs that close the supplied debits)
import cold_run_gad_reuben as GR              # THE EDGE: opening_speech -> gad_reuben CALL, reference (32 READ BACK at 3:12-20; the holdings, Jair and Machir, the condition open)
import cold_run_zelophehad as ZL              # THE EDGE: opening_speech -> zelophehad CALL, reference (27:1-11's halt — the hard matter of 1:17; the callee's own chapter)
import cold_run_journeys as JO                # THE EDGE: opening_speech -> journeys CALL, reference (33:38's verbal analogy dates 1:3 — the transfer taught; the era's new year; the order)
import cold_run_borders as BO                 # THE EDGE: opening_speech -> borders CALL, reference (the nine and a half at 3:12-13; the promised extents at 1:7; the relay form)
import cold_run_second_census as C2           # THE EDGE: opening_speech -> second_census CALL, reference (the rolls' total for the exact count; the Urim's judgment at 27:21; the age edges)
import cold_run_balak as BK                   # THE EDGE: opening_speech -> balak CALL, reference (the last camp for 3:29; the judges' count 78,600 at its Talmud seat; Moab and Midian)
import cold_run_primeval as PR                # THE EDGE: opening_speech -> primeval CALL, reference (Genesis 15:18's land at 1:7-8; the Rephaim of 14:5 at 2:10-11; 15:16's Amorite read at 2:34)
import cold_run_mamre as MM                   # THE EDGE: opening_speech -> mamre CALL, reference (Genesis 19:37-38's Moab and Ben-ammi at 2:9, 2:19)
import cold_run_joseph as JS                  # THE EDGE: opening_speech -> joseph CALL, reference (Genesis 36:8's Esau in Seir at 2:4-5; 36:20's Horites at 2:12, 2:22)
import cold_run_ordinances as OR              # THE EDGE: opening_speech -> ordinances CALL, reference (Exodus 23:1-8's court clauses at 1:16-17; 23:31's border at 1:7)
import cold_run_holiness as HO                # THE EDGE: opening_speech -> holiness CALL, reference (Leviticus 19:15's no faces and the five effects at 1:17; the talebearer at the divided court)
import cold_run_erection as ER                # THE EDGE: opening_speech -> erection CALL, reference (Exodus 33:1's departure from Horeb at 1:6; Avot 1:1's chain; the nations' seven orders)
import cold_run_bamidbar as CB                # THE EDGE: opening_speech -> bamidbar CALL, reference (the census's total for the exact count; the camp's order)
import cold_run_beha as BH                    # THE EDGE: opening_speech -> beha CALL, reference (11:14's "I alone" at 1:9-12; the seventy with Moses; 10:11's march the retrograde marker's day)
import cold_run_refuge as RF                  # THE EDGE: opening_speech -> refuge CALL, reference (the six cities' row — Deuteronomy 4:41-43 chapter 4's; the twenty-three; the kin and the haters)

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

def verse_text(ch, vs, book='Deut'):
    rows = db.execute("""SELECT w.he FROM words w JOIN verses v ON w.verse_id=v.id WHERE v.book=?
        AND v.chapter=? AND v.verse=? ORDER BY w.idx""", (book, ch, vs)).fetchall()
    return ' '.join(strip(h) for (h,) in rows)

def words(ch, vs, book='Deut'):
    return verse_text(ch, vs, book).split()

# ---- zero-report probes: the span's load-bearing tokens (every one measured on the DB before it was typed — deu_runner_measure.out, 2026-09-15) ----
PROBES = [
    # Num 27:12-23 — the callee
    ('עלה',       27, 12, 'go up — to this mountain of Abarim (Num)', 'Num'),
    ('העברים',    27, 12, 'Abarim — the mountain\'s first name (Nebo 32:49, Pisgah 34:1 its others)', 'Num'),
    ('וראה',      27, 12, 'and see [the land] — the debit see_the_land', 'Num'),
    ('ונאספת',    27, 13, 'and you shall be gathered — as Aaron', 'Num'),
    ('מריתם',     27, 14, 'you rebelled — Meribah\'s pointer to 20:12', 'Num'),
    ('מריבת',     27, 14, 'Meribah — the sentence cited', 'Num'),
    ('הרוחת',     27, 16, 'the spirits [of all flesh] — 16:22\'s phrase at its second seat', 'Num'),
    ('כצאן',      27, 17, 'as sheep [without a shepherd]', 'Num'),
    ('רעה',       27, 17, 'a shepherd', 'Num'),
    ('יהושע',     27, 18, 'Joshua — written defective', 'Num'),
    ('רוח',       27, 18, 'spirit — a man in whom is spirit', 'Num'),
    ('וסמכת',     27, 18, 'and you shall lay [your hand] — one hand commanded', 'Num'),
    ('אלעזר',     27, 19, 'Eleazar — the priest before whom', 'Num'),
    ('מהודך',     27, 20, 'of your honor — Bava Batra 75a the sun and the moon', 'Num'),
    ('האורים',    27, 21, 'the Urim — the judgment of the Urim', 'Num'),
    ('ויעש',      27, 22, 'and [Moses] did — the run', 'Num'),
    ('צוה',       27, 22, '[as the LORD] commanded — the receipt', 'Num'),
    ('ויסמך',     27, 23, 'and he laid [his hands] — two laid', 'Num'),
    ('ידיו',      27, 23, 'his hands — the plural', 'Num'),
    # Deut 1 — the frame, the officers, the judges, the spies read back
    ('אלה',       1, 1,  'these [are the words] — the book\'s first token', 'Deut'),
    ('הדברים',    1, 1,  'the words — the rebuke by places (the Sifrei 1)', 'Deut'),
    ('בעבר',      1, 1,  'beyond [the Jordan]', 'Deut'),
    ('זהב',       1, 1,  'Di-zahab — the calf\'s gold (Berakhot 32a:7)', 'Deut'),
    ('אחד',       1, 2,  'eleven — the parser [11]', 'Deut'),
    ('מחרב',      1, 2,  'from Horeb', 'Deut'),
    ('ברנע',      1, 2,  'Kadesh-barnea', 'Deut'),
    ('בארבעים',   1, 3,  'in the fortieth — the number reader\'s year', 'Deut'),
    ('בעשתי',     1, 3,  'in the eleventh [month] — the number reader', 'Deut'),
    ('ככל',       1, 3,  'according to all — the receipt of the rules (the Sifrei 2:8)', 'Deut'),
    ('הכתו',      1, 4,  'after he had smitten — the order of the fortieth year', 'Deut'),
    ('סיחן',      1, 4,  'Sihon', 'Deut'),
    ('הואיל',     1, 5,  'undertook — began (Sotah 35b:6)', 'Deut'),
    ('באר',       1, 5,  'to expound — 27:8\'s "clearly"', 'Deut'),
    ('בחרב',      1, 6,  'in Horeb — the departure\'s command', 'Deut'),
    ('רב',        1, 6,  'enough — "long enough" plural', 'Deut'),
    ('פנו',       1, 7,  'turn — Numbers 14:25\'s pair', 'Deut'),
    ('פרת',       1, 7,  'Euphrates — the great river', 'Deut'),
    ('ורשו',      1, 8,  'and possess — the land granted read', 'Deut'),
    ('לאברהם',    1, 8,  'to Abraham — the fathers named', 'Deut'),
    ('לבדי',      1, 9,  'alone — 11:14\'s "I alone"', 'Deut'),
    ('אלף',       1, 11, 'a thousand [times] — the parser [1000]', 'Deut'),
    ('ומשאכם',    1, 12, 'and your burden — 11:17\'s word', 'Deut'),
    ('חכמים',     1, 13, 'wise — the three qualities', 'Deut'),
    ('ונבנים',    1, 13, 'and discerning — not found (Eruvin 100b:18)', 'Deut'),
    ('וידעים',    1, 13, 'and known', 'Deut'),
    ('ואשימם',    1, 13, 'and I will set them [as heads] — the al tikrei (the Sifrei 13:6)', 'Deut'),
    ('ואקח',      1, 15, 'and I took — the appointment retold', 'Deut'),
    ('אלפים',     1, 15, 'thousands — the plural a noun (rule 29)', 'Deut'),
    ('ושטרים',    1, 15, 'and officers — the strap (the Sifrei 15:5)', 'Deut'),
    ('ואצוה',     1, 16, 'and I charged — THE LAW\'S VERB', 'Deut'),
    ('שפטיכם',    1, 16, 'your judges', 'Deut'),
    ('שמע',       1, 16, 'hear — the infinitive absolute', 'Deut'),
    ('ושפטתם',    1, 16, 'and judge', 'Deut'),
    ('גרו',       1, 16, 'his stranger — the convert (Yevamot 47a:7)', 'Deut'),
    ('תכירו',     1, 17, 'you shall [not] respect [persons] — befriend / estrange', 'Deut'),
    ('כקטן',      1, 17, 'the small [as the great]', 'Deut'),
    ('תגורו',     1, 17, 'you shall [not] be afraid — a term for gathering in', 'Deut'),
    ('המשפט',     1, 17, 'the judgment [is God\'s]', 'Deut'),
    ('יקשה',      1, 17, 'is too hard — the hard matter', 'Deut'),
    ('והנורא',    1, 19, 'and the terrible [wilderness]', 'Deut'),
    ('נשלחה',     1, 22, 'let us send — the people\'s asking', 'Deut'),
    ('ויחפרו',    1, 22, 'that they may search — Sotah 34b:4', 'Deut'),
    ('עשר',       1, 23, 'twelve — the parser [12, 1]', 'Deut'),
    ('אשכל',      1, 24, 'Eshcol — the valley', 'Deut'),
    ('וירגלו',    1, 24, 'and they spied — the spy-verb, Caleb\'s', 'Deut'),
    ('טובה',      1, 25, 'good [is the land] — Joshua and Caleb\'s (14:7)', 'Deut'),
    ('ותמרו',     1, 26, 'and you rebelled', 'Deut'),
    ('ותרגנו',    1, 27, 'and you murmured — two words (Shevuot 47b:5)', 'Deut'),
    ('בשנאת',     1, 27, 'in [the LORD\'s] hatred', 'Deut'),
    ('ורם',       1, 28, 'and taller — greater and taller than we', 'Deut'),
    ('ענקים',     1, 28, 'the Anakim', 'Deut'),
    ('תערצון',    1, 29, 'do not dread', 'Deut'),
    ('ילחם',      1, 30, 'He will fight [for you] — Exodus 14:14', 'Deut'),
    ('נשאך',      1, 31, 'carried you — as a man carries his son', 'Deut'),
    ('מאמינם',    1, 32, 'believing', 'Deut'),
    ('באש',       1, 33, 'in fire [by night] — the pillar, Exodus 13:21', 'Deut'),
    ('וישבע',     1, 34, 'and He swore — the oath\'s verb supplied', 'Deut'),
    ('הרע',       1, 35, 'this evil [generation]', 'Deut'),
    ('כלב',       1, 36, 'Caleb — save Caleb', 'Deut'),
    ('מלא',       1, 36, 'wholly [followed] — Joshua 14:14', 'Deut'),
    ('התאנף',     1, 37, 'was angry — the bar\'s ground DISAGREES with 20:12', 'Deut'),
    ('בגללכם',    1, 37, 'for your sakes — Psalm 106:32', 'Deut'),
    ('ינחלנה',    1, 38, 'he shall cause [Israel] to inherit — the effect\'s first seat', 'Deut'),
    ('וטפכם',     1, 39, 'and your little ones — 14:31 VERBATIM', 'Deut'),
    ('ורע',       1, 39, 'and evil — good and evil, Eden\'s four seats', 'Deut'),
    ('סוף',       1, 40, 'the Red Sea [way] — 14:25 by CALL', 'Deut'),
    ('חטאנו',     1, 41, 'we have sinned — the receipt in the people\'s mouth', 'Deut'),
    ('צונו',      1, 41, '[as the LORD] commanded us — the run citation (R5)', 'Deut'),
    ('ותזדו',     1, 43, 'and you were presumptuous', 'Deut'),
    ('הדברים',    1, 44, 'the bees — as bees do', 'Deut'),
    ('חרמה',      1, 44, 'Hormah — in Seir', 'Deut'),
    ('ותבכו',     1, 45, 'and you wept — 14:1 read', 'Deut'),
    ('רבים',      1, 46, 'many [days] — Seder Olam 8', 'Deut'),
    # Deut 2 — the bypass
    ('ונסב',      2, 1,  'and we compassed [Mount Seir] many days', 'Deut'),
    ('צפנה',      2, 3,  'northward — the supplied turn', 'Deut'),
    ('אחיכם',     2, 4,  'your brothers [the sons of Esau]', 'Deut'),
    ('תתגרו',     2, 5,  'do [not] contend — THE BLOCK\'S VERB', 'Deut'),
    ('לעשו',      2, 5,  'to Esau — Mount Seir for a possession (Kiddushin 18a:2)', 'Deut'),
    ('תשברו',     2, 6,  'you shall buy [food] — the permission (Avodah Zarah 37b:15)', 'Deut'),
    ('חסרת',      2, 7,  'you have lacked [nothing] — the manna\'s forty years', 'Deut'),
    ('מאילת',     2, 8,  'from Elath', 'Deut'),
    ('תצר',       2, 9,  'do [not] harass [Moab]', 'Deut'),
    ('ער',        2, 9,  'Ar — to the sons of Lot', 'Deut'),
    ('האמים',     2, 10, 'the Emim — Genesis 14:5', 'Deut'),
    ('רפאים',     2, 11, 'Rephaim', 'Deut'),
    ('החרים',     2, 12, 'the Horites — Genesis 36:20', 'Deut'),
    ('זרד',       2, 13, 'Zered — the supplied crossing', 'Deut'),
    ('ושמנה',     2, 14, 'and eight — thirty-eight years [38]', 'Deut'),
    ('תם',        2, 14, 'until [the generation] was consumed', 'Deut'),
    ('תמו',       2, 16, '[when] they were consumed — the fifteenth of Av', 'Deut'),
    ('וידבר',     2, 17, 'and [the LORD] SPOKE [to me] — the Bible\'s one seat', 'Deut'),
    ('עמון',      2, 19, 'Ammon — the sons of Ammon', 'Deut'),
    ('זמזמים',    2, 20, 'Zamzummim', 'Deut'),
    ('כפתרים',    2, 23, 'the Caphtorim — Genesis 10:14', 'Deut'),
    ('ארנן',      2, 24, 'Arnon — the brook', 'Deut'),
    ('החל',       2, 24, 'begin [to possess] — the supplied war', 'Deut'),
    ('והתגר',     2, 24, 'and contend [with him in battle] — the positive', 'Deut'),
    ('אחל',       2, 25, 'I will begin — the sun for Moses (Avodah Zarah 25a)', 'Deut'),
    ('קדמות',     2, 26, 'Kedemoth — the messengers', 'Deut'),
    ('בדרך',      2, 27, 'by the road [by the road] — SHORTENED against 21:22', 'Deut'),
    ('הישבים',    2, 29, 'who dwell [in Seir] — DISAGREES with 20:18-21', 'Deut'),
    ('הקשה',      2, 30, 'hardened [his spirit] — Pharaoh\'s verb', 'Deut'),
    ('יהצה',      2, 32, 'Jahaz — 21:23 SHORTENED', 'Deut'),
    ('ונך',       2, 33, 'and we smote [him and his son] — written "his son", read "his sons"', 'Deut'),
    ('ונחרם',     2, 34, 'and we devoted — THE BAN TOLD ONLY HERE', 'Deut'),
    ('בזזנו',     2, 35, 'we took as prey', 'Deut'),
    ('מערער',     2, 36, 'from Aroer', 'Deut'),
    ('קרבת',      2, 37, 'you came [not] near — Ammon\'s border', 'Deut'),
    # Deut 3 — Og, the east, the charges, the plea
    ('אדרעי',     3, 1,  'Edrei — 21:33 TURNED', 'Deut'),
    ('תירא',      3, 2,  'fear [him not] — 21:34\'s effect', 'Deut'),
    ('ונכהו',     3, 3,  'and we smote him', 'Deut'),
    ('ששים',      3, 4,  'sixty [cities] — [60]', 'Deut'),
    ('ארגב',      3, 4,  'Argob', 'Deut'),
    ('ובריח',     3, 5,  'and bars — fortified with high walls, gates and bars', 'Deut'),
    ('החרם',      3, 6,  'devoting — the second ban', 'Deut'),
    ('חרמון',     3, 8,  'Hermon', 'Deut'),
    ('שרין',      3, 9,  'Sirion — the Sidonians\' name', 'Deut'),
    ('שניר',      3, 9,  'Senir — the Amorites\' name', 'Deut'),
    ('סלכה',      3, 10, 'Salcah', 'Deut'),
    ('ערשו',      3, 11, 'his bedstead — of iron', 'Deut'),
    ('באמת',      3, 11, 'by the cubit [of a man] — Kelim 17:9-10', 'Deut'),
    ('וחצי',      3, 12, 'and half [the hill country of Gilead] — rule 30 [1/2]', 'Deut'),
    ('לחצי',      3, 13, 'to half [the tribe of Manasseh] — [1/2]', 'Deut'),
    ('יאיר',      3, 14, 'Jair — EXPANDED against 32:41', 'Deut'),
    ('ולמכיר',    3, 15, 'and to Machir — 32:40', 'Deut'),
    ('יבק',       3, 16, 'Jabbok', 'Deut'),
    ('הפסגה',     3, 17, 'Pisgah — the slopes', 'Deut'),
    ('חלוצים',    3, 18, 'armed — 32:30, 32', 'Deut'),
    ('יניח',      3, 20, 'gives rest — Joshua 1:15', 'Deut'),
    ('יהושוע',    3, 21, 'Joshua PLENE — the Torah\'s one seat', 'Deut'),
    ('הראת',      3, 21, 'have seen — your eyes have seen', 'Deut'),
    ('הנלחם',     3, 22, 'He who fights [for you]', 'Deut'),
    ('ואתחנן',    3, 23, 'and I besought — the pleading mode', 'Deut'),
    ('החלות',     3, 24, 'You have begun [to show] — praise first', 'Deut'),
    ('החזקה',     3, 24, 'the strong [hand] — 1 Kings 8:42', 'Deut'),
    ('אעברה',     3, 25, 'let me go over', 'Deut'),
    ('והלבנון',   3, 25, 'and Lebanon — the Temple (Gittin 56b:1)', 'Deut'),
    ('ויתעבר',    3, 26, 'and [the LORD] was wroth — three Bible seats', 'Deut'),
    ('לך',        3, 26, '[enough] for you — singular; Sotah 13b:13', 'Deut'),
    ('תוסף',      3, 26, 'speak no more', 'Deut'),
    ('ימה',       3, 27, 'westward — the four directions', 'Deut'),
    ('וצו',       3, 28, 'and command [Joshua] — Kiddushin 29a:14', 'Deut'),
    ('ינחיל',     3, 28, 'he shall cause [them] to inherit — the effect\'s second seat', 'Deut'),
    ('פעור',      3, 29, 'Beth-peor — the last camp', 'Deut'),
]
for tok_, ch, vs, note, bk in PROBES:
    if tok_ not in words(ch, vs, bk):
        sys.exit('ZERO-REPORT LAW: probe %r (%s) failed at %s %d:%d — refusing to run' % (tok_, note, bk, ch, vs))
print('probes: all %d token probes fired  [zero-report law satisfied]\n' % len(PROBES))

P = []  # the provenance trail of the case being run

def ink(ref, note):  P.append(('INK',  'Deut %s — %s' % (ref, note) if not ref.startswith('Num') else '%s — %s' % (ref, note)))
def move(src, note): P.append(('MOVE', '%s — %s' % (src, note)))
def dat(note):       P.append(('DATA', note))
def hyp(note):       P.append(('HYP',  note))     # THE LINK REVIEW LAW: a hypothesis — no teacher; counted apart, never as compiled

def out(verdict, effects):
    """verdict + registry-validated effects (the engine contract)"""
    FX.validate([e for e in effects if e != FX.NONE])
    return verdict, effects, list(P)

# ---- THE INK, computed (the parser and the tokens; the reading's facts the expectations) ----
SPAN = [(1, v) for v in range(1, 47)] + [(2, v) for v in range(1, 38)] + [(3, v) for v in range(1, 30)]
NUMBERS = {(c, v): ink_numbers(verse_words('Deut', c, v)) for c, v in SPAN}
ORDINALS = {(c, v): ink_ordinals(verse_words('Deut', c, v)) for c, v in SPAN}
INTS = {k: n for k, n in NUMBERS.items() if n}; ORDS = {k: o for k, o in ORDINALS.items() if o}
MARKED = [(c, v, t) for c, v in SPAN for t in verse_words('Deut', c, v) if t[-1] in '*~@^%']
assert INTS == {(1, 2): [11], (1, 3): [40, 11, 1], (1, 11): [1000], (1, 15): [100, 50, 10], (1, 23): [12, 1], (2, 7): [40], (2, 14): [38], (3, 4): [60], (3, 8): [2], (3, 11): [9, 4], (3, 12): [Fraction(1, 2)], (3, 13): [Fraction(1, 2)], (3, 21): [2]} and ORDS == {}, (INTS, ORDS)   # THIRTEEN number verses in a hundred and twelve — the reading's eleven + the two halves rule 30 taught this sitting (deu_runner_measure.out (B) BEFORE the rule; census D10-D11 after)
assert MARKED == [(3, 8, 'שני^'), (3, 12, 'וחצי%'), (3, 13, 'לחצי%'), (3, 21, 'לשני^')], MARKED                          # the two "two"s marked as duals-in-construct (3:8 the two kings, 3:21 to the two kings); the two halves the fraction mark
NUM27 = {v: ink_numbers(verse_words('Num', 27, v)) for v in range(12, 24)}
assert not any(NUM27.values()) and not any(ink_ordinals(verse_words('Num', 27, v)) for v in range(12, 24)), NUM27           # the callee's twelve verses carry no number
SPEECH_DATE, ELEVEN_DAYS, THOUSAND_FOLD, GRAINS, TWELVE_ONE, FORTY, THIRTY_EIGHT, SIXTY, BED, HALVES = INTS[(1, 3)], INTS[(1, 2)][0], INTS[(1, 11)][0], INTS[(1, 15)], INTS[(1, 23)], INTS[(2, 7)][0], INTS[(2, 14)][0], INTS[(3, 4)][0], INTS[(3, 11)], (INTS[(3, 12)][0], INTS[(3, 13)][0])
assert SPEECH_DATE == [40, 11, 1] and GRAINS == [100, 50, 10] and TWELVE_ONE == [12, 1] and FORTY - THIRTY_EIGHT == 2 and BED == [9, 4] and HALVES == (Fraction(1, 2), Fraction(1, 2)), (SPEECH_DATE, GRAINS, TWELVE_ONE, FORTY, THIRTY_EIGHT, BED, HALVES)   # the ink's own arithmetic: forty less thirty-eight = the two years elapsed at the decree (SL.decree count_from by CALL)
# THE FRAMES — the divine speech-frames inside Moses' first person (deu_runner_measure.out THE FRAMES): "the LORD said to me" six, "the LORD spoke to me" one
def _has(c, v, toks):
    ws = words(c, v); n = len(toks)
    return any(ws[i:i + n] == toks for i in range(len(ws) - n + 1))
SAID_TO_ME = [(c, v) for c, v in SPAN if _has(c, v, ['ויאמר', 'יהוה', 'אלי'])]
SPOKE_TO_ME = [(c, v) for c, v in SPAN if _has(c, v, ['וידבר', 'יהוה', 'אלי'])]
assert SAID_TO_ME == [(1, 42), (2, 2), (2, 9), (2, 31), (3, 2), (3, 26)] and SPOKE_TO_ME == [(2, 17)], (SAID_TO_ME, SPOKE_TO_ME)          # the six "said to me" — five open their verses, 3:26's inside the refusal's verse (the phrase found anywhere in the verse); 2:17's "SPOKE to me" the Bible's one seat — the speech resumed after the generation
FIRST_PERSON_W = [(c, v, t) for c, v in SPAN for t in words(c, v) if t in ('ואצוה', 'ואצו', 'ואתחנן', 'ואשלח', 'ואמר', 'ואדבר', 'ואקח', 'ואתן')]
assert [(c, v) for c, v, _ in FIRST_PERSON_W] == [(1, 9), (1, 15), (1, 15), (1, 16), (1, 18), (1, 20), (1, 23), (1, 29), (1, 43), (2, 26), (3, 18), (3, 23)], FIRST_PERSON_W   # Moses' own first-person acts: the charge (1:16, 1:18) and the charges (3:18), the taking and the setting (1:15, 1:23), the sending (2:26), the plea (3:23)
AT_THAT_TIME = [(c, v) for c, v in SPAN if 'בעת' in words(c, v) and 'ההוא' in words(c, v)]
assert AT_THAT_TIME == [(1, 9), (1, 16), (1, 18), (2, 34), (3, 4), (3, 8), (3, 12), (3, 18), (3, 21), (3, 23)], AT_THAT_TIME                # "at that time" TEN seats in the span — the retelling's own dating word, no number: the retrograde markers' warrant (a)
CASE_KI = {(c, v): [t for t in words(c, v) if t in ('כי', 'אם', 'רק', 'למען')] for c, v in SPAN}
CASE_KI = {k: ts for k, ts in CASE_KI.items() if ts}
assert CASE_KI == {(1, 17): ['כי'], (1, 35): ['אם'], (1, 38): ['כי'], (1, 42): ['כי'], (2, 5): ['כי', 'כי'], (2, 7): ['כי'], (2, 9): ['כי', 'כי'], (2, 19): ['כי', 'כי'], (2, 28): ['רק'], (2, 30): ['כי', 'למען'], (2, 35): ['רק'], (2, 37): ['רק'], (3, 2): ['כי'], (3, 11): ['כי', 'רק'], (3, 19): ['רק', 'כי'], (3, 22): ['כי'], (3, 27): ['כי'], (3, 28): ['כי']}, CASE_KI   # THE CASE TOKENS: the bars' "for I will not give … for I have given" doubled at 2:5, 2:9, 2:19 — the block and the grant in one sentence each; the oath's "if" at 1:35; "only" the exceptions

# ---- the whole-DB phrase census (the seats typed from the measurement print of 2026-09-15 — deu_runner_measure.out (C)) ----
_V = collections.OrderedDict(); _L = collections.OrderedDict(); _M = collections.OrderedDict()
for b, c, v, he, lm, mo in db.execute("SELECT v.book, v.chapter, v.verse, w.he, w.lemma, w.morph FROM words w JOIN verses v ON w.verse_id=v.id ORDER BY v.id, w.idx"):
    _V.setdefault((b, c, v), []).append(strip(he)); _L.setdefault((b, c, v), []).append(lm.split('/')[-1].split(' ')[0] if lm else ''); _M.setdefault((b, c, v), []).append(mo or '')
def seats(phrase, books=None):
    p = phrase.split(); n = len(p)
    return ['%s %d:%d' % k for k, ws in _V.items() if (books is None or k[0] in books) and any(ws[i:i + n] == p for i in range(len(ws) - n + 1))]
def tok(t, books=None):
    return ['%s %d:%d' % k for k, ws in _V.items() if (books is None or k[0] in books) and t in ws]
def lemma_seats(lm, books=None):
    return ['%s %d:%d' % k for k, ls in _L.items() if (books is None or k[0] in books) and lm in ls]
TORAH = ('Gen', 'Exod', 'Lev', 'Num', 'Deut')
# ---- F1's facts: the frame ----
THESE_WORDS = seats('אלה הדברים'); FORTIETH_YEAR = seats('בארבעים שנה'); ELEVENTH_MONTH = seats('בעשתי עשר חדש'); ACCORDING_ALL_HIM = seats('ככל אשר צוה יהוה אתו'); ACCORDING_ALL = seats('ככל אשר צוה יהוה')
assert THESE_WORDS == ['Deut 1:1', 'Exod 19:6', 'Exod 35:1', 'Isa 42:16', 'Zech 8:16'] and FORTIETH_YEAR == ['Deut 1:3'] and ELEVENTH_MONTH == ['Deut 1:3'] and ACCORDING_ALL_HIM == ['Deut 1:3', 'Exod 40:16'] and ACCORDING_ALL == ['Deut 1:3', 'Exod 39:32', 'Exod 39:42', 'Exod 40:16', 'Num 1:54', 'Num 2:34', 'Num 8:20', 'Num 9:5', 'Num 30:1'], (THESE_WORDS, FORTIETH_YEAR, ELEVENTH_MONTH, ACCORDING_ALL_HIM, ACCORDING_ALL)   # "in the fortieth year" — 1:3's bare date, ONE seat (33:38 says "of the going out"); "according to all that the LORD commanded HIM" two seats — the erection's receipt (40:16) and this
ELEVEN_HOREB = seats('אחד עשר יום מחרב'); AFTER_SIHON = seats('אחרי הכתו את סיחן'); EXPOUND = seats('הואיל משה באר'); EXPOUND_LEMMA = lemma_seats('874', TORAH)
assert ELEVEN_HOREB == ['Deut 1:2'] and AFTER_SIHON == ['Deut 1:4'] and EXPOUND == ['Deut 1:5'] and EXPOUND_LEMMA == ['Deut 1:5', 'Deut 27:8'], (ELEVEN_HOREB, AFTER_SIHON, EXPOUND, EXPOUND_LEMMA)   # the expound-root's two Torah seats — 1:5 and 27:8's "clearly" (Sotah 35b:6); Habakkuk 2:2 the Bible's third
# ---- F2's facts: the officers and the judges ----
ENOUGH_PL = seats('רב לכם'); ENOUGH_SG = seats('רב לך'); DWELT_MOUNTAIN = seats('שבת בהר הזה'); TURN_JOURNEY = seats('פנו וסעו'); GO_POSSESS = seats('באו ורשו'); SET_BEFORE = seats('נתתי לפניכם את הארץ'); THE_FATHERS = seats('לאבתיכם לאברהם ליצחק וליעקב')
assert ENOUGH_PL == ['1Kgs 12:28', 'Deut 1:6', 'Deut 2:3', 'Deut 3:19', 'Ezek 44:6', 'Ezek 45:9', 'Num 16:3', 'Num 16:7'] and ENOUGH_SG == ['Deut 3:26'] and DWELT_MOUNTAIN == ['Deut 1:6'] and TURN_JOURNEY == ['Deut 1:7', 'Num 14:25'] and GO_POSSESS == ['Deut 1:8'] and SET_BEFORE == ['Deut 1:8'] and THE_FATHERS == ['Deut 1:8'], (ENOUGH_PL, ENOUGH_SG, DWELT_MOUNTAIN, TURN_JOURNEY, GO_POSSESS, SET_BEFORE, THE_FATHERS)   # "enough for you" plural at Horeb (1:6), at Seir (2:3), to the tribes (3:19) — and Korach's twice (16:3, 16:7); the singular ONCE, to Moses (3:26 — Sotah 13b:13 measure for measure); "turn and journey" 1:7 = 14:25 (the turn-back's own words)
THOUSAND_TIMES = seats('אלף פעמים'); YOUR_BURDEN = seats('ומשאכם'); WISE_DISC_KNOWN = seats('חכמים ונבנים וידעים'); WISE_KNOWN = seats('חכמים וידעים'); CAPT_THOUSANDS = seats('שרי אלפים'); CAPT_HUNDREDS = seats('שרי מאות'); CAPT_FIFTIES = seats('שרי חמשים'); OFFICERS_TRIBES = seats('ושטרים לשבטיכם'); AND_OFFICERS = seats('ושטרים')
assert THOUSAND_TIMES == ['Deut 1:11'] and YOUR_BURDEN == ['Deut 1:12'] and WISE_DISC_KNOWN == ['Deut 1:13'] and WISE_KNOWN == ['Deut 1:15'] and CAPT_THOUSANDS == ['1Sam 8:12', '1Sam 22:7', '2Chr 17:14', '2Sam 18:1', 'Deut 1:15', 'Exod 18:21', 'Exod 18:25'] and CAPT_HUNDREDS == ['Exod 18:21', 'Exod 18:25'] and CAPT_FIFTIES == ['Exod 18:21', 'Exod 18:25'] and OFFICERS_TRIBES == ['Deut 1:15'] and AND_OFFICERS == ['1Chr 23:4', '2Chr 19:11', '2Chr 34:13', 'Deut 1:15', 'Deut 16:18', 'Josh 8:33'], (THOUSAND_TIMES, YOUR_BURDEN, WISE_DISC_KNOWN, WISE_KNOWN, CAPT_THOUSANDS, CAPT_HUNDREDS, CAPT_FIFTIES, OFFICERS_TRIBES, AND_OFFICERS)   # "wise and discerning and known" (1:13) against "wise and known" (1:15) — the discerning not found (Eruvin 100b:18; Nedarim 20b:10); "captains of thousands" with Exodus 18:21, 25 — the hundreds and the fifties Exodus's alone (1:15 says "captains of hundreds, of fifties" with the construct bare); "and officers for your tribes" here alone; "and officers" six seats — Deuteronomy 16:18 the second seat (Sanhedrin 16b:9-10)
HEAR_BROTHERS = seats('שמע בין אחיכם'); JUDGE_RIGHT = seats('ושפטתם צדק'); NO_FACES = seats('לא תכירו פנים במשפט'); RESPECT_FACES = seats('תכירו פנים'); SMALL_GREAT = seats('כקטן כגדל תשמעון'); NOT_AFRAID = seats('לא תגורו מפני איש'); JUDGMENT_GODS = seats('כי המשפט לאלהים הוא'); HARD_MATTER = seats('והדבר אשר יקשה מכם'); BRING_TO_ME = seats('תקרבון אלי')
assert HEAR_BROTHERS == ['Deut 1:16'] and JUDGE_RIGHT == ['Deut 1:16'] and NO_FACES == ['Deut 1:17'] and RESPECT_FACES == ['Deut 1:17'] and SMALL_GREAT == ['Deut 1:17'] and NOT_AFRAID == ['Deut 1:17'] and JUDGMENT_GODS == ['Deut 1:17'] and HARD_MATTER == ['Deut 1:17'] and BRING_TO_ME == ['Deut 1:17'], (HEAR_BROTHERS, JUDGE_RIGHT, NO_FACES, RESPECT_FACES, SMALL_GREAT, NOT_AFRAID, JUDGMENT_GODS, HARD_MATTER, BRING_TO_ME)   # THE CHARGE'S SIX CLAUSES each ONE seat in the Bible — the charge's own words, said once (Sanhedrin 7b:14-8a:6 read them clause by clause)
JUDGE_LEMMA = lemma_seats('8199', ('Deut',)); OFFICER_T = lemma_seats('7860', TORAH); RECOGNIZE_T = lemma_seats('5234', TORAH); GUR_T = lemma_seats('1481', TORAH)
assert JUDGE_LEMMA[0] == 'Deut 1:16' and OFFICER_T == ['Deut 1:15', 'Deut 16:18', 'Deut 20:5', 'Deut 20:8', 'Deut 20:9', 'Deut 29:9', 'Deut 31:28', 'Exod 5:6', 'Exod 5:10', 'Exod 5:14', 'Exod 5:15', 'Exod 5:19', 'Num 11:16'] and len(RECOGNIZE_T) == 13 and 'Deut 1:17' in RECOGNIZE_T and len(GUR_T) == 37 and 'Deut 1:17' in GUR_T, (JUDGE_LEMMA[:2], OFFICER_T, len(RECOGNIZE_T), len(GUR_T))   # the officer-word: Egypt's taskmasters' officers (Exodus 5) and Israel's — Numbers 11:16's seventy "elders and OFFICERS" between them
# ---- F3's facts: the spies read back ----
LET_US_SEND = seats('נשלחה אנשים לפנינו'); SEARCH_FOR_US = seats('ויחפרו לנו'); TWELVE_MEN = seats('שנים עשר אנשים'); ONE_PER_TRIBE = seats('איש אחד לשבט'); ESHCOL = seats('נחל אשכל'); SPIED_IT = seats('וירגלו אתה'); SPY_ROOT = lemma_seats('7270'); GOOD_LAND_IS = seats('טובה הארץ'); A_GOOD_LAND = seats('ארץ טובה')
assert LET_US_SEND == ['Deut 1:22'] and SEARCH_FOR_US == ['Deut 1:22'] and TWELVE_MEN == ['Deut 1:23', 'Josh 4:2'] and ONE_PER_TRIBE == ['Deut 1:23', 'Josh 3:12'] and ESHCOL == ['Deut 1:24', 'Num 13:23'] and SPIED_IT == ['Deut 1:24'] and len(SPY_ROOT) == 24 and 'Deut 1:24' in SPY_ROOT and 'Josh 14:7' in SPY_ROOT and 'Num 21:32' in SPY_ROOT and 'Gen 42:9' in SPY_ROOT and GOOD_LAND_IS == ['Deut 1:25', 'Num 14:7'] and A_GOOD_LAND == ['Deut 8:7', 'Exod 3:8'], (LET_US_SEND, SEARCH_FOR_US, TWELVE_MEN, ONE_PER_TRIBE, ESHCOL, SPIED_IT, SPY_ROOT, GOOD_LAND_IS, A_GOOD_LAND)   # "good is the land" 1:25 = Numbers 14:7 — JOSHUA AND CALEB'S words in the spies' mouths (the Sifrei 23:3); the spy-root (the verb and the noun 'spies' — Joseph's brothers' at Genesis 42) twenty-four Bible verses, RETYPED FROM THE PRINT (the measurement's seven were the piel verb's alone); 1:24's piel Caleb's verb (Joshua 14:7; Numbers 21:32 Jazer), not 13:2's "tour"; "twelve men" and "one man per tribe" Joshua's crossing (4:2, 3:12) the other seats
REBELLED_MOUTH = seats('ותמרו את פי יהוה'); MURMURED_TENTS = seats('ותרגנו באהליכם'); HATES_US = seats('בשנאת יהוה אתנו'); MELTED_HEART = seats('אחינו המסו את לבבנו'); GREATER_TALLER = seats('עם גדול ורם ממנו'); SONS_ANAKIM = seats('בני ענקים'); DREAD_NOR_FEAR = seats('לא תערצון ולא תיראון'); FIGHT_FOR_YOU = seats('הוא ילחם לכם'); CARRIES_SON = seats('כאשר ישא איש את בנו')
assert REBELLED_MOUTH == ['Deut 1:26', 'Deut 1:43', 'Deut 9:23'] and MURMURED_TENTS == ['Deut 1:27'] and HATES_US == ['Deut 1:27'] and MELTED_HEART == ['Deut 1:28'] and GREATER_TALLER == ['Deut 1:28'] and SONS_ANAKIM == ['Deut 1:28', 'Deut 9:2'] and DREAD_NOR_FEAR == ['Deut 1:29'] and FIGHT_FOR_YOU == ['Deut 1:30'] and CARRIES_SON == ['Deut 1:31'], (REBELLED_MOUTH, MURMURED_TENTS, HATES_US, MELTED_HEART, GREATER_TALLER, SONS_ANAKIM, DREAD_NOR_FEAR, FIGHT_FOR_YOU, CARRIES_SON)   # "you rebelled against the mouth of the LORD" at 1:26 and 1:43 — the two refusals, before and after the oath (9:23 the third); "greater and taller than we" (1:28) the plain sense of 13:31's "stronger than us" (Sotah 35a:7 reads "than Him")
FIRE_NIGHT = seats('באש לילה'); CLOUD_DAY = seats('ובענן יומם'); EVIL_GENERATION = seats('הדור הרע הזה'); THE_GOOD_LAND = seats('הארץ הטובה'); SAVE_CALEB = seats('זולתי כלב בן יפנה'); WHOLLY_FOLLOWED = seats('מלא אחרי יהוה'); ANGRY_FOR_YOU = seats('התאנף יהוה בגללכם'); NOT_GO_IN = seats('לא תבא שם'); HE_SHALL_GO = seats('הוא יבא שמה'); CAUSE_ISRAEL_INHERIT = seats('הוא ינחלנה את ישראל')
assert FIRE_NIGHT == ['Deut 1:33'] and CLOUD_DAY == ['Deut 1:33'] and EVIL_GENERATION == ['Deut 1:35'] and THE_GOOD_LAND == ['1Chr 28:8', 'Deut 1:35', 'Deut 3:25', 'Deut 4:21', 'Deut 4:22', 'Deut 9:6', 'Josh 23:16'] and SAVE_CALEB == ['Deut 1:36'] and WHOLLY_FOLLOWED == ['1Kgs 11:6', 'Deut 1:36', 'Josh 14:14'] and ANGRY_FOR_YOU == ['Deut 1:37'] and NOT_GO_IN == ['Deut 1:37'] and HE_SHALL_GO == ['Deut 1:38'] and CAUSE_ISRAEL_INHERIT == ['Deut 1:38'], (FIRE_NIGHT, CLOUD_DAY, EVIL_GENERATION, THE_GOOD_LAND, SAVE_CALEB, WHOLLY_FOLLOWED, ANGRY_FOR_YOU, NOT_GO_IN, HE_SHALL_GO, CAUSE_ISRAEL_INHERIT)   # "the LORD was angry with me FOR YOUR SAKES" (1:37) — the bar's ground DISAGREES with 20:12's "because you did not believe" (Psalm 106:32 the ink's own bridge, outside the Torah); "he wholly followed the LORD" — Caleb's phrase at Joshua 14:14, the holding's payment
LITTLE_ONES_PREY = seats('וטפכם אשר אמרתם לבז יהיה'); GOOD_EVIL = seats('טוב ורע'); RED_SEA_WAY = seats('דרך ים סוף'); WE_HAVE_SINNED = seats('חטאנו ליהוה'); GO_UP_FIGHT = seats('אנחנו נעלה ונלחמנו'); NOT_AMONG_YOU = seats('כי אינני בקרבכם'); PRESUMPTUOUS = seats('ותזדו ותעלו'); AS_BEES = seats('כאשר תעשינה הדברים'); TO_HORMAH = seats('בשעיר עד חרמה'); WEPT_BEFORE = seats('ותבכו לפני יהוה'); NOT_HEAR_VOICE = seats('ולא שמע יהוה בקלכם'); KADESH_DAYS = seats('ותשבו בקדש ימים רבים')
assert LITTLE_ONES_PREY == ['Deut 1:39', 'Num 14:31'] and GOOD_EVIL == ['Deut 1:39', 'Gen 2:9', 'Gen 2:17', 'Gen 3:5', 'Gen 3:22'] and RED_SEA_WAY == ['Deut 1:40', 'Deut 2:1', 'Num 14:25', 'Num 21:4'] and WE_HAVE_SINNED == ['1Sam 7:6', 'Deut 1:41', 'Jer 8:14', 'Jer 16:10'] and GO_UP_FIGHT == ['Deut 1:41'] and NOT_AMONG_YOU == ['Deut 1:42'] and PRESUMPTUOUS == ['Deut 1:43'] and AS_BEES == ['Deut 1:44'] and TO_HORMAH == ['Deut 1:44'] and WEPT_BEFORE == ['Deut 1:45'] and NOT_HEAR_VOICE == ['Deut 1:45'] and KADESH_DAYS == ['Deut 1:46'], (LITTLE_ONES_PREY, GOOD_EVIL, RED_SEA_WAY, WE_HAVE_SINNED, GO_UP_FIGHT, NOT_AMONG_YOU, PRESUMPTUOUS, AS_BEES, TO_HORMAH, WEPT_BEFORE, NOT_HEAR_VOICE, KADESH_DAYS)   # "your little ones who you said would be a prey" 1:39 = 14:31 VERBATIM (the five tokens); "good and evil" Eden's four seats and this — the children who know not; "the way of the Red Sea" four seats: the command (14:25), its run (21:4), and both retold (1:40, 2:1)
VERBATIM_PREFIX = 0
for a, b in zip(words(1, 39), words(14, 31, 'Num')):
    if a != b: break
    VERBATIM_PREFIX += 1
assert VERBATIM_PREFIX == 5 and len(words(1, 39)) == 19 and len(words(14, 31, 'Num')) == 13, (VERBATIM_PREFIX, len(words(1, 39)), len(words(14, 31, 'Num')))   # THE VERBATIM GRADE computed: the first five tokens identical, then the retelling adds the children who know not good and evil
# ---- F4's facts: the bypass ----
COMPASSED_SEIR = seats('ונסב את הר שעיר ימים רבים'); LONG_ENOUGH_MOUNTAIN = seats('רב לכם סב את ההר הזה'); TURN_NORTH = seats('פנו לכם צפנה'); BROTHERS_ESAU = seats('אחיכם בני עשו'); DWELL_IN_SEIR = seats('הישבים בשעיר'); NOT_CONTEND = seats('אל תתגרו בם'); FOOT_BREADTH = seats('עד מדרך כף רגל'); SEIR_TO_ESAU = seats('ירשה לעשו נתתי את הר שעיר'); BUY_FOOD = seats('אכל תשברו מאתם בכסף'); FORTY_YEARS_THESE = seats('זה ארבעים שנה'); LACKED_NOTHING = seats('לא חסרת דבר')
assert COMPASSED_SEIR == ['Deut 2:1'] and LONG_ENOUGH_MOUNTAIN == ['Deut 2:3'] and TURN_NORTH == ['Deut 2:3'] and BROTHERS_ESAU == ['Deut 2:4'] and DWELL_IN_SEIR == ['Deut 2:4', 'Deut 2:8', 'Deut 2:22', 'Deut 2:29'] and NOT_CONTEND == ['Deut 2:5'] and FOOT_BREADTH == ['Deut 2:5'] and SEIR_TO_ESAU == ['Deut 2:5'] and BUY_FOOD == ['Deut 2:6'] and FORTY_YEARS_THESE == ['Deut 2:7', 'Deut 8:2', 'Deut 8:4'] and LACKED_NOTHING == ['Deut 2:7'], (COMPASSED_SEIR, LONG_ENOUGH_MOUNTAIN, TURN_NORTH, BROTHERS_ESAU, DWELL_IN_SEIR, NOT_CONTEND, FOOT_BREADTH, SEIR_TO_ESAU, BUY_FOOD, FORTY_YEARS_THESE, LACKED_NOTHING)   # "who dwell in Seir" four seats — the sons of Esau at 2:4, 2:8, 2:29 (the retelling's own arm of the passage) and the Horites' dispossessors at 2:22
HARASS_MOAB = seats('אל תצר את מואב'); CONTEND_ROOT = lemma_seats('1624', ('Deut',)); AR_SEATS = seats('ער'); EMIM = seats('האמים'); REPHAIM = seats('רפאים'); ANAKIM_PL = seats('ענקים'); HORITES = seats('החרים'); AS_ISRAEL_DID = seats('כאשר עשה ישראל לארץ ירשתו'); ZERED = seats('נחל זרד'); THIRTY_EIGHT_YEARS = seats('שלשים ושמנה שנה'); GENERATION_CONSUMED = seats('עד תם כל הדור אנשי המלחמה'); MEN_OF_WAR = seats('אנשי המלחמה'); HAND_AGAINST = seats('יד יהוה היתה בם'); DISCOMFIT = seats('להמם')
assert HARASS_MOAB == ['Deut 2:9'] and CONTEND_ROOT == ['Deut 2:5', 'Deut 2:9', 'Deut 2:19', 'Deut 2:24'] and AR_SEATS == ['1Chr 2:3', '1Chr 4:21', 'Deut 2:9', 'Deut 2:18', 'Gen 38:3', 'Gen 38:7', 'Gen 46:12', 'Isa 15:1', 'Mal 2:12', 'Num 21:15', 'Num 21:28', 'Num 26:19', 'Song 5:2'] and EMIM == ['Deut 2:10', 'Ps 117:1'] and len(REPHAIM) == 19 and 'Gen 14:5' in REPHAIM and ANAKIM_PL == ['Deut 1:28', 'Deut 9:2', 'Josh 11:22', 'Josh 14:12'] and len(HORITES) == 12 and 'Deut 2:12' in HORITES and AS_ISRAEL_DID == ['Deut 2:12'] and ZERED == ['Deut 2:13', 'Deut 2:14'] and THIRTY_EIGHT_YEARS == ['1Kgs 16:29', '2Kgs 15:8', 'Deut 2:14'] and GENERATION_CONSUMED == ['Deut 2:14'] and len(MEN_OF_WAR) == 20 and HAND_AGAINST == ['Deut 2:15', 'Judg 2:15'] and DISCOMFIT == ['Deut 2:15', 'Esth 9:24'], (HARASS_MOAB, CONTEND_ROOT, AR_SEATS, EMIM, len(REPHAIM), ANAKIM_PL, len(HORITES), AS_ISRAEL_DID, ZERED, THIRTY_EIGHT_YEARS, GENERATION_CONSUMED, len(MEN_OF_WAR), HAND_AGAINST, DISCOMFIT)   # THE CONTEND-ROOT'S FOUR SEATS IN THE SPAN: the three bars (2:5, 2:9, 2:19) and the one command to war (2:24) — the block's word and its positive; "Ar" the token a homograph of Er (Genesis 38's) and "city" — the seats typed apart; "the Emim" Psalm 117:1's "peoples" the homograph
SONS_OF_AMMON = seats('בני עמון'); ZAMZUMMIM = seats('זמזמים'); CAPHTORIM = seats('כפתרים'); RISE_ARNON = seats('קומו סעו ועברו את נחל ארנן'); BEGIN_POSSESS = seats('החל רש'); BEGIN_DREAD = seats('אחל תת פחדך'); WHOLE_HEAVEN = seats('תחת כל השמים'); KEDEMOTH = seats('ממדבר קדמות'); WORDS_PEACE = seats('דברי שלום'); ROAD_ROAD = seats('בדרך בדרך'); NOT_TURN = seats('לא אסור ימין ושמאול'); ESAU_DID_FOR_ME = seats('עשו לי בני עשו'); MOABITES_AR = seats('והמואבים הישבים בער'); HARDENED = seats('הקשה יהוה אלהיך את רוחו ואמץ את לבבו'); BEGUN_DELIVER = seats('החלתי תת לפניך'); JAHAZ = seats('יהצה'); DEVOTED_WE = seats('ונחרם'); EVERY_CITY_MEN = seats('כל עיר מתם והנשים והטף'); NONE_LEFT = seats('לא השארנו שריד'); FROM_AROER = seats('מערער'); TOO_HIGH = seats('לא היתה קריה אשר שגבה ממנו'); LAND_AMMON = seats('ארץ בני עמון')
assert len(SONS_OF_AMMON) == 77 and ZAMZUMMIM == ['Deut 2:20'] and CAPHTORIM == ['1Chr 1:12', 'Deut 2:23', 'Gen 10:14'] and RISE_ARNON == ['Deut 2:24'] and BEGIN_POSSESS == ['Deut 2:24', 'Deut 2:31'] and BEGIN_DREAD == ['Deut 2:25'] and WHOLE_HEAVEN == ['Dan 9:12', 'Deut 2:25', 'Deut 4:19', 'Gen 7:19', 'Job 28:24', 'Job 37:3', 'Job 41:3'] and KEDEMOTH == ['Deut 2:26'] and WORDS_PEACE == ['2Kgs 15:15', 'Deut 2:26', 'Esth 9:30', 'Ps 28:3'] and ROAD_ROAD == ['Deut 2:27'] and NOT_TURN == ['Deut 2:27'] and ESAU_DID_FOR_ME == ['Deut 2:29'] and MOABITES_AR == ['Deut 2:29'] and HARDENED == ['Deut 2:30'] and BEGUN_DELIVER == ['Deut 2:31'] and JAHAZ == ['1Chr 6:63', 'Deut 2:32', 'Jer 48:21', 'Josh 21:36', 'Num 21:23'] and DEVOTED_WE == ['Deut 2:34', 'Deut 3:6'] and EVERY_CITY_MEN == ['Deut 2:34'] and NONE_LEFT == ['Deut 2:34'] and FROM_AROER == ['2Kgs 10:33', 'Deut 2:36', 'Deut 3:12', 'Deut 4:48'] and TOO_HIGH == ['Deut 2:36'] and LAND_AMMON == ['1Chr 19:2', '1Chr 20:1', '2Sam 10:2', 'Deut 2:37', 'Josh 13:25', 'Judg 11:15'], (len(SONS_OF_AMMON), ZAMZUMMIM, CAPHTORIM, RISE_ARNON, BEGIN_POSSESS, BEGIN_DREAD, WHOLE_HEAVEN, KEDEMOTH, WORDS_PEACE, ROAD_ROAD, NOT_TURN, ESAU_DID_FOR_ME, MOABITES_AR, HARDENED, BEGUN_DELIVER, JAHAZ, DEVOTED_WE, EVERY_CITY_MEN, NONE_LEFT, FROM_AROER, TOO_HIGH, LAND_AMMON)   # "and we devoted" at 2:34 and 3:6 alone — THE BAN TOLD ONLY IN THE RETELLING (21:24-25, 21:35 say smote and possessed); "as the sons of Esau did for me" ONE seat — the retelling's arm against 20:18-21
# THE SHORTENED GRADES computed: the messengers to Sihon (2:27 against 21:22), Jahaz (2:32 against 21:23)
MSG_DEUT, MSG_NUM = words(2, 27), words(21, 22, 'Num'); JAHAZ_DEUT, JAHAZ_NUM = words(2, 32), words(21, 23, 'Num')
assert (len(MSG_DEUT), len(MSG_NUM)) == (9, 17) and (len(JAHAZ_DEUT), len(JAHAZ_NUM)) == (8, 20) and len(set(MSG_DEUT) & set(MSG_NUM)) == 4 and len(set(JAHAZ_DEUT) & set(JAHAZ_NUM)) == 4, (len(MSG_DEUT), len(MSG_NUM), len(JAHAZ_DEUT), len(JAHAZ_NUM), set(MSG_DEUT) & set(MSG_NUM), set(JAHAZ_DEUT) & set(JAHAZ_NUM))   # nine tokens for seventeen; eight for twenty — four shared each (RETYPED FROM THE PRINT: the hand had counted five at Jahaz)
# ---- F5's facts: Sihon and Og ----
OG_BASHAN = seats('עוג מלך הבשן'); EDREI = seats('אדרעי'); FEAR_HIM_NOT = seats('אל תירא אתו'); AS_TO_SIHON = seats('כאשר עשית לסיחן'); GAVE_INTO_HAND = seats('ויתן יהוה אלהינו בידנו'); SIXTY_CITIES = seats('ששים עיר'); ARGOB = seats('חבל ארגב'); HIGH_WALLS = seats('חומה גבהה דלתים ובריח'); HERMON = seats('חרמון'); SIRION = seats('לחרמון שרין'); SENIR = seats('שניר'); SALCAH = seats('סלכה'); REMNANT_REPHAIM = seats('מיתר הרפאים'); IRON_BED = seats('ערש ברזל'); IN_RABBAH = seats('הלה הוא ברבת'); NINE_CUBITS = seats('תשע אמות ארכה'); CUBIT_OF_MAN = seats('באמת איש')
assert len(OG_BASHAN) == 10 and 'Num 21:33' in OG_BASHAN and 'Num 32:33' in OG_BASHAN and EDREI == ['Deut 3:1', 'Num 21:33'] and FEAR_HIM_NOT == ['Deut 3:2', 'Num 21:34'] and AS_TO_SIHON == ['Deut 3:2', 'Num 21:34'] and GAVE_INTO_HAND == ['Deut 3:3'] and SIXTY_CITIES == ['1Chr 2:23', 'Deut 3:4', 'Josh 13:30'] and ARGOB == ['1Kgs 4:13', 'Deut 3:4', 'Deut 3:14'] and HIGH_WALLS == ['Deut 3:5'] and len(HERMON) == 11 and SIRION == ['Deut 3:9'] and SENIR == ['Deut 3:9', 'Song 4:8'] and SALCAH == ['1Chr 5:11', 'Deut 3:10', 'Josh 13:11'] and REMNANT_REPHAIM == ['Deut 3:11', 'Josh 12:4', 'Josh 13:12'] and IRON_BED == ['Deut 3:11'] and IN_RABBAH == ['Deut 3:11'] and NINE_CUBITS == ['Deut 3:11'] and CUBIT_OF_MAN == ['Deut 3:11'], (len(OG_BASHAN), EDREI, FEAR_HIM_NOT, AS_TO_SIHON, GAVE_INTO_HAND, SIXTY_CITIES, ARGOB, HIGH_WALLS, len(HERMON), SIRION, SENIR, SALCAH, REMNANT_REPHAIM, IRON_BED, IN_RABBAH, NINE_CUBITS, CUBIT_OF_MAN)   # "fear him not" and "as you did to Sihon" 3:2 = 21:34 — the TURNED grade's identical clauses inside the shifted frame
# THE TURNED GRADE computed: Deuteronomy 3:1-3 against Numbers 21:33-35 — the tokens shared and the pronouns shifted (CK.well_and_kings('deut3_delta') by CALL the reading's own row)
OG_D = words(3, 1) + words(3, 2) + words(3, 3); OG_N = words(21, 33, 'Num') + words(21, 34, 'Num') + words(21, 35, 'Num')
OG_SHARED = len(set(OG_D) & set(OG_N)); OG_SHIFT = [(a, b) for a, b in (('ונפן', 'ויפנו'), ('ונעל', 'ויעלו'), ('לקראתנו', 'לקראתם'), ('אלי', 'משה'), ('ונכהו', 'ויכו')) if a in OG_D and b in OG_N]
assert (len(OG_D), len(OG_N)) == (57, 55) and OG_SHARED == 35 and len(OG_SHIFT) == 5, (len(OG_D), len(OG_N), OG_SHARED, OG_SHIFT)   # fifty-seven tokens for fifty-five; thirty-five shared; the five pronoun shifts we-for-they, to-me-for-to-Moses (RETYPED FROM THE PRINT: the hand had typed 54/56 and 30)
# ---- F6's facts: the east and the charges ----
HALF_GILEAD = seats('וחצי הר הגלעד'); REUBENITE_GADITE = seats('לראובני ולגדי'); HALF_MANASSEH = seats('לחצי שבט המנשה'); JAIR_MANASSEH = seats('יאיר בן מנשה'); HAVVOTH_JAIR = seats('חות יאיר'); GESHURITE = seats('הגשורי והמעכתי'); TO_MACHIR = seats('ולמכיר נתתי את הגלעד'); MIDDLE_BROOK = seats('תוך הנחל'); JABBOK = seats('יבק'); SALT_SEA_ARABAH = seats('ים הערבה ים המלח'); SLOPES_PISGAH = seats('תחת אשדת הפסגה'); GIVEN_THIS_LAND = seats('נתן לכם את הארץ הזאת לרשתה'); ARMED = seats('חלוצים'); MEN_OF_VALOR = seats('כל בני חיל'); UNTIL_REST = seats('עד אשר יניח יהוה לאחיכם'); EACH_TO_POSSESSION = seats('איש לירשתו'); COMMANDED_JOSHUA_TIME = seats('ואת יהושוע צויתי בעת ההוא'); JOSHUA_PLENE = tok('יהושוע'); EYES_SEEN = seats('עיניך הראת'); ALL_KINGDOMS = seats('כן יעשה יהוה לכל הממלכות'); NOT_FEAR_THEM = seats('לא תיראום'); HE_FIGHTS = seats('הוא הנלחם לכם')
assert HALF_GILEAD == ['Deut 3:12'] and REUBENITE_GADITE == ['1Chr 5:26', 'Deut 3:12', 'Deut 29:7', 'Josh 12:6', 'Josh 22:1'] and HALF_MANASSEH == ['Deut 3:13'] and JAIR_MANASSEH == ['1Kgs 4:13', 'Deut 3:14'] and len(HAVVOTH_JAIR) == 6 and 'Num 32:41' in HAVVOTH_JAIR and GESHURITE == ['Deut 3:14', 'Josh 12:5', 'Josh 13:11'] and TO_MACHIR == ['Deut 3:15'] and MIDDLE_BROOK == ['Deut 3:16'] and JABBOK == ['Deut 2:37', 'Deut 3:16', 'Gen 32:23', 'Josh 12:2', 'Num 21:24'] and SALT_SEA_ARABAH == ['Deut 3:17', 'Josh 3:16', 'Josh 12:3'] and SLOPES_PISGAH == ['Deut 3:17', 'Deut 4:49'] and GIVEN_THIS_LAND == ['Deut 3:18'] and ARMED == ['Deut 3:18', 'Num 32:30', 'Num 32:32'] and MEN_OF_VALOR == ['Deut 3:18'] and UNTIL_REST == ['Deut 3:20', 'Josh 1:15'] and EACH_TO_POSSESSION == ['Deut 3:20'] and COMMANDED_JOSHUA_TIME == ['Deut 3:21'] and JOSHUA_PLENE == ['Deut 3:21', 'Judg 2:7'] and EYES_SEEN == ['Deut 3:21'] and ALL_KINGDOMS == ['Deut 3:21'] and NOT_FEAR_THEM == ['Deut 3:22'] and HE_FIGHTS == ['Deut 3:22', 'Josh 23:3', 'Josh 23:10'], (HALF_GILEAD, REUBENITE_GADITE, HALF_MANASSEH, JAIR_MANASSEH, len(HAVVOTH_JAIR), GESHURITE, TO_MACHIR, MIDDLE_BROOK, JABBOK, SALT_SEA_ARABAH, SLOPES_PISGAH, GIVEN_THIS_LAND, ARMED, MEN_OF_VALOR, UNTIL_REST, EACH_TO_POSSESSION, COMMANDED_JOSHUA_TIME, JOSHUA_PLENE, EYES_SEEN, ALL_KINGDOMS, NOT_FEAR_THEM, HE_FIGHTS)   # "armed" (chalutsim) 3:18 = 32:30, 32 — the three seats; "until the LORD gives rest to your brothers" 3:20 = Joshua 1:15 word for word — the condition's release outside the Torah; JOSHUA PLENE at 3:21 alone in the Torah (Judges 2:7 the Bible's second); "He fights for you" Joshua 23:3, 10 the run's echo
# THE EXPANDED GRADE computed: Jair (3:14 against 32:41), the division (3:12-13 against 32:33)
JAIR_D, JAIR_N = words(3, 14), words(32, 41, 'Num'); DIV_D, DIV_N = words(3, 12) + words(3, 13), words(32, 33, 'Num')
assert (len(JAIR_D), len(JAIR_N)) == (23, 11) and (len(DIV_D), len(DIV_N)) == (37, 28), (len(JAIR_D), len(JAIR_N), len(DIV_D), len(DIV_N))   # twenty-three tokens for eleven; thirty-seven for twenty-eight (RETYPED FROM THE PRINT: the hand had typed 36/29)
# ---- F7's facts: the plea ----
BESOUGHT = seats('ואתחנן אל יהוה'); AT_THAT_TIME_SEATS = seats('בעת ההוא'); LORD_GOD = seats('אדני יהוה'); BEGUN_SHOW = seats('אתה החלות להראות את עבדך'); YOUR_GREATNESS = seats('את גדלך'); STRONG_HAND = seats('ואת ידך החזקה'); WHAT_GOD = seats('אשר מי אל בשמים ובארץ'); LET_ME_GO_OVER = seats('אעברה נא'); GOOD_LAND_BEYOND = seats('הארץ הטובה אשר בעבר הירדן'); WROTH_FOR_YOU = seats('ויתעבר יהוה בי למענכם'); WROTH = seats('ויתעבר'); NOT_HEAR_ME = seats('ולא שמע אלי'); SUFFICE_YOU = seats('רב לך אל תוסף'); SPEAK_NO_MORE = seats('אל תוסף דבר אלי עוד'); TOP_PISGAH = seats('ראש הפסגה'); FOUR_DIRECTIONS = seats('ימה וצפנה ותימנה ומזרחה'); NOT_CROSS_JORDAN = seats('לא תעבר את הירדן הזה'); COMMAND_JOSHUA = seats('וצו את יהושע'); STRENGTHEN = seats('וחזקהו ואמצהו'); BE_STRONG = seats('חזק ואמץ'); HE_SHALL_CROSS = seats('הוא יעבר לפני העם הזה'); CAUSE_THEM_INHERIT = seats('והוא ינחיל אותם'); VALLEY_PEOR = seats('בגיא מול בית פעור'); AGAINST_PEOR = seats('מול בית פעור')
assert BESOUGHT == ['Deut 3:23'] and len(AT_THAT_TIME_SEATS) == 19 and len(LORD_GOD) == 284 and BEGUN_SHOW == ['Deut 3:24'] and YOUR_GREATNESS == ['Deut 3:24'] and STRONG_HAND == ['1Kgs 8:42', 'Deut 3:24'] and WHAT_GOD == ['Deut 3:24'] and LET_ME_GO_OVER == ['2Sam 16:9', 'Deut 3:25', 'Judg 11:17'] and GOOD_LAND_BEYOND == ['Deut 3:25'] and WROTH_FOR_YOU == ['Deut 3:26'] and WROTH == ['Deut 3:26', 'Ps 78:21', 'Ps 78:59'] and NOT_HEAR_ME == ['Deut 3:26'] and SUFFICE_YOU == ['Deut 3:26'] and SPEAK_NO_MORE == ['Deut 3:26'] and TOP_PISGAH == ['Deut 3:27', 'Deut 34:1', 'Num 21:20', 'Num 23:14'] and FOUR_DIRECTIONS == ['Deut 3:27'] and NOT_CROSS_JORDAN == ['Deut 3:27', 'Deut 31:2'] and COMMAND_JOSHUA == ['Deut 3:28'] and STRENGTHEN == ['Deut 3:28'] and len(BE_STRONG) == 9 and 'Josh 1:6' in BE_STRONG and HE_SHALL_CROSS == ['Deut 3:28'] and CAUSE_THEM_INHERIT == ['Deut 3:28'] and VALLEY_PEOR == ['Deut 3:29', 'Deut 4:46'] and AGAINST_PEOR == ['Deut 3:29', 'Deut 4:46', 'Deut 34:6'], (BESOUGHT, len(AT_THAT_TIME_SEATS), len(LORD_GOD), BEGUN_SHOW, YOUR_GREATNESS, STRONG_HAND, WHAT_GOD, LET_ME_GO_OVER, GOOD_LAND_BEYOND, WROTH_FOR_YOU, WROTH, NOT_HEAR_ME, SUFFICE_YOU, SPEAK_NO_MORE, TOP_PISGAH, FOUR_DIRECTIONS, NOT_CROSS_JORDAN, COMMAND_JOSHUA, STRENGTHEN, len(BE_STRONG), HE_SHALL_CROSS, CAUSE_THEM_INHERIT, VALLEY_PEOR, AGAINST_PEOR)   # "let me go over, I pray" three seats — Moses', Jephthah's letter to Edom (Judges 11:17 — the double refusal outside the Torah), Abishai's; "over against Beth-peor" 3:29, 4:46 and 34:6 — the last camp, the speech's place, Moses' grave; "the top of Pisgah" Balaam's (23:14), the well's (21:20), this and 34:1
DIR_D, DIR_G13, DIR_G28 = [w for w in words(3, 27) if w in ('ימה', 'וצפנה', 'ותימנה', 'ומזרחה')], [w for w in words(13, 14, 'Gen') if w in ('צפנה', 'ונגבה', 'וקדמה', 'וימה')], [w for w in words(28, 14, 'Gen') if w in ('ימה', 'וקדמה', 'וצפנה', 'ונגבה')]
assert DIR_D == ['ימה', 'וצפנה', 'ותימנה', 'ומזרחה'] and DIR_G13 == ['צפנה', 'ונגבה', 'וקדמה', 'וימה'] and DIR_G28 == ['ימה', 'וקדמה', 'וצפנה', 'ונגבה'], (DIR_D, DIR_G13, DIR_G28)   # THE FOUR DIRECTIONS IN THREE ORDERS — west-north-south-east (3:27), north-south-east-west (Genesis 13:14), west-east-north-south (Genesis 28:14): the reading's find, computed
# ---- F0's facts: the commission ----
ABARIM_MOUNTAIN = seats('הר העברים'); SEE_THE_LAND = seats('וראה את הארץ'); GATHERED_AS_AARON = seats('כאשר נאסף אהרן אחיך'); MERIBAH_KADESH = seats('מריבת קדש'); SPIRITS_ALL_FLESH = seats('אלהי הרוחת לכל בשר'); GO_OUT_COME_IN = seats('אשר יצא לפניהם ואשר יבא לפניהם'); SHEEP_NO_SHEPHERD = seats('כצאן אשר אין להם רעה'); MAN_WITH_SPIRIT = seats('איש אשר רוח בו'); LAY_YOUR_HAND = seats('וסמכת את ידך עליו'); BEFORE_ELEAZAR = seats('לפני אלעזר הכהן'); OF_YOUR_HONOR = seats('ונתתה מהודך עליו'); JUDGMENT_URIM = seats('במשפט האורים'); AT_HIS_WORD = seats('על פיו יצאו ועל פיו יבאו'); DID_AS_COMMANDED = seats('ויעש משה כאשר צוה יהוה אתו'); LAID_HIS_HANDS = seats('ויסמך את ידיו עליו'); BY_HAND_MOSES = seats('ביד משה'); NEBO_PISGAH = seats('הר נבו ראש הפסגה')
assert ABARIM_MOUNTAIN == ['Deut 32:49', 'Num 27:12'] and SEE_THE_LAND == ['Num 27:12'] and GATHERED_AS_AARON == ['Num 27:13'] and MERIBAH_KADESH == ['Deut 32:51', 'Ezek 48:28', 'Num 27:14'] and SPIRITS_ALL_FLESH == ['Num 16:22', 'Num 27:16'] and GO_OUT_COME_IN == ['Num 27:17'] and SHEEP_NO_SHEPHERD == ['1Kgs 22:17', 'Num 27:17'] and MAN_WITH_SPIRIT == ['Num 27:18'] and LAY_YOUR_HAND == ['Num 27:18'] and BEFORE_ELEAZAR == ['Josh 17:4', 'Num 27:19', 'Num 27:22'] and OF_YOUR_HONOR == ['Num 27:20'] and JUDGMENT_URIM == ['Num 27:21'] and AT_HIS_WORD == ['Num 27:21'] and DID_AS_COMMANDED == ['Lev 8:4', 'Num 17:26', 'Num 27:22'] and LAID_HIS_HANDS == ['Num 27:23'] and len(BY_HAND_MOSES) == 31 and NEBO_PISGAH == ['Deut 34:1'], (ABARIM_MOUNTAIN, SEE_THE_LAND, GATHERED_AS_AARON, MERIBAH_KADESH, SPIRITS_ALL_FLESH, GO_OUT_COME_IN, SHEEP_NO_SHEPHERD, MAN_WITH_SPIRIT, LAY_YOUR_HAND, BEFORE_ELEAZAR, OF_YOUR_HONOR, JUDGMENT_URIM, AT_HIS_WORD, DID_AS_COMMANDED, LAID_HIS_HANDS, len(BY_HAND_MOSES), NEBO_PISGAH)   # "the mountain of Abarim" 27:12 and Deuteronomy 32:49 (the run's command restated with Nebo named; 33:47-48 says 'the mountains of Abarim' plural); "and see the land" 27:12 alone (32:49 says 'the land of Canaan'); Meribah of Kadesh with Ezekiel 48:28's border; "as sheep without a shepherd" — Micaiah's vision (1 Kings 22:17) the phrase's other seat; "before Eleazar the priest" bare at 27:19, 27:22 and Joshua 17:4 (the daughters before Eleazar!), 27:21's with the vav; "and Moses did as the LORD commanded him" THREE seats — Leviticus 8:4 (the milluim), Numbers 17:26 (the staff), 27:22: the receipt form's own census; ONE hand commanded (27:18), TWO laid (27:23 — the Sifrei 141, credited at THE TENT) — every list RETYPED FROM THE PRINT
HAND_SG, HANDS_PL = [t for t in words(27, 18, 'Num') if t == 'ידך'], [t for t in words(27, 23, 'Num') if t == 'ידיו']
assert HAND_SG == ['ידך'] and HANDS_PL == ['ידיו'], (HAND_SG, HANDS_PL)

# ---- THE CALLEES (live import edges; the design's cells by name; every value typed from deu_compile_measure.out (3)) ----
ES_DENOM = ES.jethro('denominations'); ES_JUDGES = ES.jethro('judges'); ES_HARD = ES.jethro('hard_cases'); ES_MANNA = ES.manna('forty_years'); ES_SIZES = ES.jethro('sanhedrin_sizes')
assert ES_DENOM['v'] == 4 and ES_JUDGES['v'] == 78600 and ES_HARD['v'] == 'to_moses' and ES_MANNA['v'] == 40 and ES_SIZES['v'] == (71, 23), (ES_DENOM['v'], ES_JUDGES['v'], ES_HARD['v'], ES_MANNA['v'], ES_SIZES['v'])   # Jethro's four grains over the round six hundred thousand = 78,600 (Sanhedrin 18a); the hard cases to Moses the standing status; the manna's forty years; the courts' sizes
SL_SEND = SL.spies({'ask': 'send_for_yourself'}, SL.DATA); SL_STRONGER = SL.spies({'ask': 'stronger_than'}, SL.DATA); SL_ESHCOL = SL.spies({'ask': 'eshcol'}, SL.DATA); SL_CLUSTER = SL.spies({'ask': 'cluster'}, SL.DATA)
SL_SET = SL.decree({'ask': 'set'}, SL.DATA); SL_EXC = SL.decree({'ask': 'exceptions'}, SL.DATA); SL_FROM = SL.decree({'ask': 'count_from'}, SL.DATA); SL_CEASED = SL.decree({'ask': 'deaths_ceased'}, SL.DATA); SL_HORMAH = SL.decree({'ask': 'hormah'}, SL.DATA); SL_TURN = SL.decree({'ask': 'turn_back'}, SL.DATA); SL_PRESUME = SL.decree({'ask': 'presumption'}, SL.DATA); SL_CALEB = SL.decree({'ask': 'caleb_entitlement'}, SL.DATA); SL_NIGHT = SL.decree({'ask': 'that_night'}, SL.DATA); SL_DUE = SL.decree({'ask': 'due'}, SL.DATA)
assert SL_SEND[0].startswith("at Moses' discretion — 'for yourself' (Reish Lakish); the people's asking (Deut 1:22)") and SL_STRONGER[0].startswith('stronger than us, read stronger than Him') and SL_ESHCOL[0] == 'named after the cluster (13:24); Deut 1:24' and SL_CLUSTER[0].startswith('on a pole between two'), (SL_SEND[0], SL_STRONGER[0], SL_ESHCOL[0], SL_CLUSTER[0])
assert SL_SET[0].startswith('603550 — the census set by CALL') and SL_EXC[0] == 'Caleb and Joshua (14:24, 14:30); the children brought in (14:31)' and SL_FROM[0].startswith("40 - 38 = 2 — the era's year at the decree") and SL_CEASED[0].startswith('the fifteenth of Av of the fortieth year') and SL_HORMAH[0].startswith('Hormah — named at 21:3, used at 14:45') and SL_TURN[0].startswith('tomorrow turn — by the way of the Red Sea: OPEN, its run Num 21:4 / Deut 2:1') and SL_PRESUME[0].startswith('presumed — the ark and Moses stayed') and SL_CALEB[0].startswith('holding_owed — Hebron; PAID at Josh 14:13-14') and SL_NIGHT[0].startswith('the night of the Ninth of Av') and SL_DUE[0].startswith('(40, 5, 9)'), (SL_SET[0], SL_EXC[0], SL_FROM[0], SL_CEASED[0], SL_HORMAH[0], SL_TURN[0], SL_PRESUME[0], SL_CALEB[0], SL_NIGHT[0], SL_DUE[0])
assert SL.DATA['deaths_ceased']['value'] == (40, 5, 15) and SL.DATA['count_from']['value'] == 'the exodus' and SL.DATA['return_day']['value'] == (2, 5, 9), (SL.DATA['deaths_ceased']['value'], SL.DATA['count_from']['value'], SL.DATA['return_day']['value'])   # the spies' return (2, 5, 9) — the thirty-eight years' start; the deaths ceased (40, 5, 15) — 2:16-17's "when all the men of war were consumed"
CK_EDOM = CK.edom_and_hor({'ask': 'edom_passage'}, CK.DATA); CK_DATES = CK.edom_and_hor({'ask': 'death_dates'}, CK.DATA); CK_SUCC = CK.edom_and_hor({'ask': 'succession'}, CK.DATA); CK_ARAD = CK.edom_and_hor({'ask': 'arad_heard'}, CK.DATA)
CK_DELTA = CK.well_and_kings({'ask': 'deut3_delta'}, CK.DATA); CK_OG = CK.well_and_kings({'ask': 'og_lore'}, CK.DATA); CK_PURE = CK.well_and_kings({'ask': 'sihon_purified'}, CK.DATA); CK_AMMON = CK.well_and_kings({'ask': 'ammon_border'}, CK.DATA); CK_ZERED = CK.well_and_kings({'ask': 'zered_date'}, CK.DATA); CK_REFUSED = CK.well_and_kings({'ask': 'sihon_refused'}, CK.DATA); CK_SENTENCE = CK.meribah({'ask': 'sentence'}, CK.DATA)
assert CK_EDOM[0].startswith("Edom refused twice and Israel turned away (20:18-21); Deut 2:28-29's purchase the other arm — DISPUTE") and CK_DATES[0].startswith('Aaron (40, 5, 1) by the ink, aged 123') and CK_SUCC[0].startswith('the garments to Eleazar and the office with them') and CK_ARAD[0].startswith('Arad heard that Aaron died and the clouds departed'), (CK_EDOM[0], CK_DATES[0], CK_SUCC[0], CK_ARAD[0])
assert CK_DELTA[0] == 'Deuteronomy 3:1-3 = 21:33-35 with the pronouns shifted — we for they, "to me" for "to Moses" (computed)' and CK_OG[0].startswith("Og — Sihon's brother of the Rephaim") and CK_PURE[0].startswith('Ammon and Moab purified through Sihon') and CK_AMMON[0].startswith("Ammon's border strong here, commanded off-limits at Deut 2:19, 2:37") and CK_ZERED[0].startswith('the Zered crossed after the thirty-eight years (Deut 2:14 — [38])') and CK_REFUSED[0].startswith('Sihon refused the passage and came to Jahaz — hardened (Deut 2:30)') and CK_SENTENCE[0].startswith("barred from the land — Moses and Aaron; Aaron's closed at 20:28, Moses' at Deut 34"), (CK_DELTA[0], CK_OG[0], CK_PURE[0], CK_AMMON[0], CK_ZERED[0], CK_REFUSED[0], CK_SENTENCE[0])
assert CK.DATA['edom_passage']['value'] == 'refused_and_turned_away' and 'bought_and_passed_deut_2' in CK.DATA['edom_passage']['settings'] and CK.DATA['deaths_ceased']['value'] == (40, 5, 15) and CK.DATA['ammon_border']['value'] == 'strong_here_commanded_at_deut_2' and CK.AARON_DATE == (40, 5, 1), (CK.DATA['edom_passage'], CK.DATA['ammon_border']['value'], CK.AARON_DATE)   # THE DISPUTE ROW edom_passage holds both arms — 20:18-21's refusal and 2:28-29's purchase — no teacher joins them: the readback's OPEN row (R4)
GR_THREE = GR.the_grant({'ask': 'three_parties'}, GR.DATA); GR_HELD = GR.the_grant({'ask': 'land_held'}, GR.DATA); GR_HALF = GR.the_grant({'ask': 'half_manassehs_stipulation'}, GR.DATA); GR_POS = GR.the_condition({'ask': 'positive_arm'}, GR.DATA); GR_JAIR = GR.machir_jair_nobah({'ask': 'jair'}, GR.DATA); GR_GILEAD = GR.machir_jair_nobah({'ask': 'gilead_given'}, GR.DATA); GR_OATH = GR.the_rebuke({'ask': 'the_oath_supplied'}, GR.DATA); GR_RETURN = GR.the_offer({'ask': 'not_return'}, GR.DATA)
assert GR_THREE[0].startswith('to the sons of Gad, to the sons of Reuben and to half the tribe of Manasseh (32:33) — three transfers') and GR_HELD[0].startswith('in possession before assignment') and GR_HALF[0].startswith('no stipulation spoken to half Manasseh in the chapter; Deuteronomy 3:18-20') and GR_POS[0].startswith('if you arm yourselves before the LORD for the war') and GR_JAIR[0].startswith('Jair son of Manasseh took their villages and called them Havvoth-jair (32:41)') and GR_GILEAD[0].startswith('Moses gave Gilead to Machir son of Manasseh (32:40)') and GR_OATH[0].startswith("'and he swore, saying' (32:10) — chapter 14 says 'as I live'") and GR_RETURN[0].startswith('we will not return to our houses until the children of Israel have inherited'), (GR_THREE[0], GR_HELD[0], GR_HALF[0], GR_POS[0], GR_JAIR[0], GR_GILEAD[0], GR_OATH[0], GR_RETURN[0])
assert GR.DATA['the_oath_supplied']['value'] == 'he_swore_supplied_by_the_retelling' and GR.DATA['half_manassehs_stipulation']['value'] == 'silent_in_32_included_by_the_retellings', (GR.DATA['the_oath_supplied']['value'], GR.DATA['half_manassehs_stipulation']['value'])   # 1:34's "and He swore" the oath's verb SUPPLIED by the retelling (32:10 the first supplier); half Manasseh's crossing extended by 3:18-20
ZL_HALT = ZL.the_daughters({'ask': 'halt'}, ZL.DATA); ZL_RUN = ZL.the_daughters({'ask': 'the_run'}, ZL.DATA)
assert ZL_HALT[0] == 'the third form — the judgment carried in by Moses; no body entry on the persons; the docket alone' and ZL_RUN[0].startswith('given in the sixth book by the mouth of the LORD'), (ZL_HALT[0], ZL_RUN[0])   # THE HARD MATTER of 1:17 — the daughters' halt (the Sifrei 17:7): the third form, carried in by Moses
JO_ANALOGY = JO.aarons_death_retold({'ask': 'verbal_analogy'}, JO.DATA); JO_NEW_YEAR = JO.aarons_death_retold({'ask': 'the_era_new_year'}, JO.DATA); JO_ORDER = JO.aarons_death_retold({'ask': 'the_order'}, JO.DATA); JO_ADAR = JO.aarons_death_retold({'ask': 'moses_seventh_adar'}, JO.DATA); JO_LAST = JO.the_stations({'ask': 'the_last_camp'}, JO.DATA); JO_RITHMAH = JO.the_stations({'ask': 'rithmah_paran'}, JO.DATA)
assert JO_ANALOGY[0].startswith("the fortieth year / the fortieth year — Deuteronomy 1:3's bare date counted from the exodus by the verbal analogy with 33:38 (Rosh Hashanah 2b:11, taught)") and JO_NEW_YEAR[0].startswith("the era's new year from the chapter's date — (40, 5, 1) and (40, 11, 1) in one year") and JO_ORDER[0].startswith("the fortieth year's order — Aaron's death, Arad, the departure, Sihon") and JO_ADAR[0].startswith("Moses' seventh of Adar") and JO_LAST[0].startswith('the plains of Moab (33:48-49) — the last camp by CALL') and JO_RITHMAH[0].startswith('Rithmah (33:18) — Paran under another name'), (JO_ANALOGY[0], JO_NEW_YEAR[0], JO_ORDER[0], JO_ADAR[0], JO_LAST[0], JO_RITHMAH[0])
assert JO.SHEVAT_DATE == (40, 11, 1) and JO.AARON_DATE == (40, 5, 1) and JO.DATA['the_eras_stamps']['value'] == ['Exod 19:1', 'Num 33:38', '1Kgs 6:1'], (JO.SHEVAT_DATE, JO.AARON_DATE, JO.DATA['the_eras_stamps']['value'])   # THE TRANSFER TAUGHT: the journeys runner already names (40, 11, 1) as the speech's date from 33:38's analogy — the marker's era by CALL
BO_NINE = BO.moses_restatement({'ask': 'the_nine_and_a_half'}, BO.DATA); BO_RELAY = BO.moses_restatement({'ask': 'the_relay'}, BO.DATA); BO_GRANT_READ = BO.moses_restatement({'ask': 'the_grant_read'}, BO.DATA); BO_EXTENTS = BO.the_four_sides({'ask': 'the_promised_extents'}, BO.DATA)
assert BO_NINE[0].startswith('the nine tribes and the half tribe, the two tribes and the half tribe (34:13, 34:15)') and BO_RELAY[0].startswith('and Moses commanded the children of Israel (34:13) — the relay of 34:1-12') and BO_GRANT_READ[0].startswith("the two and a half have taken their inheritance (34:14-15) — a run citation of 32:33's three transfers") and BO_EXTENTS[0].startswith('the four promised extents (Genesis 15:18, Exodus 23:31, Deuteronomy 1:7, 11:24; Joshua 1:4)'), (BO_NINE[0], BO_RELAY[0], BO_GRANT_READ[0], BO_EXTENTS[0])
assert BO.DATA['the_promised_extents']['value'] == ['Gen 15:18', 'Exod 23:31', 'Deut 1:7', 'Deut 11:24', 'Josh 1:4'] and BO.DATA['the_nine_and_a_half']['value']['count_two_and_a_half'] == 110580, (BO.DATA['the_promised_extents']['value'], BO.DATA['the_nine_and_a_half']['value'])   # 1:7's extent the borders runner's own row names among the four promised extents — observed, no verdict
C2_TOTAL_ROW = C2.the_rolls({'ask': 'decree_consumed'}, C2.DATA); C2_EDGES = C2.the_rolls({'ask': 'age_edges'}, C2.DATA)
assert C2.DATA['urim_judgment']['value'] == 'final' and C2.DATA['wilderness_survivors']['value'] == 'yair_machir_nobah_serah_jochebed' and C2.DATA['decree_age_edges']['value'] == 'twenty_to_sixty_levi_outside' and C2_TOTAL_ROW[0].startswith('the dying ceased before the census') and C2_EDGES[0].startswith('under twenty and over sixty outside; Yair and Machir'), (C2.DATA['urim_judgment']['value'], C2.DATA['wilderness_survivors']['value'], C2.DATA['decree_age_edges']['value'], C2_TOTAL_ROW[0], C2_EDGES[0])   # the Urim's judgment FINAL (27:21 — Yoma 73b:3); Jair and Machir the survivors at 3:14-15
CB_TOTAL = CB.census({'ask': 'total'}, CB.DATA); CB_SIDES = CB.camp({'ask': 'sides'}, CB.DATA)
CENSUS_TOTAL = int(CB_TOTAL[0].split()[0])
assert CB_TOTAL[0] == '603550 = the twelve summed' and CENSUS_TOTAL == 603550 and CB_SIDES[0] == 'east judah, south reuben, west ephraim, north dan', (CB_TOTAL[0], CB_SIDES[0])
EXACT_COUNT = CENSUS_TOTAL // 1000 + CENSUS_TOTAL // 100 + CENSUS_TOTAL // 50 + CENSUS_TOTAL // 10
assert EXACT_COUNT == 79064 and ES_JUDGES['v'] == 600000 // 1000 + 600000 // 100 + 600000 // 50 + 600000 // 10 == 78600, (EXACT_COUNT, ES_JUDGES['v'])   # THE OFFICERS' TWO SETTINGS: 78,600 on the round six hundred thousand (Sanhedrin 18a:3 — the exodus engine's), 79,064 on the census's exact 603,550 by INTEGER DIVISION at every grain (603 + 6,035 + 12,071 + 60,355 — the Sifrei 15:4's rounding rule: a thousand less one yields one captain of a thousand)
BK_LAST = BK.the_call({'ask': 'last_camp'}, BK.DATA); BK_JUDGES = BK.peor({'ask': 'judges_count'}, BK.DATA); BK_MIDIAN = BK.phinehas_and_midian({'ask': 'midian_not_moab'}, BK.DATA)
assert BK_LAST[0].startswith('the plains of Moab — the last camp; the book never moves again (22:1; 36:13; Deut 34:1)') and BK_JUDGES[0].startswith("the judges of Israel 78,600 (Exod 18:21's tiers by the exodus engine) — each executing two = 157,200") and BK_MIDIAN[0].startswith("Midian harassed, Moab spared — Moses' own a fortiori needed Deut 2:9's bar (Bava Kamma 38a)"), (BK_LAST[0], BK_JUDGES[0], BK_MIDIAN[0])   # the Balak runner already names Deuteronomy 2:9's bar as the a fortiori's need — the bypass's row by CALL
PR_LAND = PR.call('land_seats'); PR_OG = PR.war('og'); PR_FOURTH = PR.pieces('fourth_generation'); PR_TEN = PR.pieces('ten_nations')
assert PR_LAND['v'] == [(12, 7), (13, 15), (15, 7), (15, 18)] and PR_OG['v'] == 'the_escapee_is_og' and PR_FOURTH['v'] == 4 and 'amorite_not_full' in PR_FOURTH['fx'] and PR_TEN['v'] == (10, 7, 3), (PR_LAND['v'], PR_OG['v'], PR_FOURTH['v'], PR_FOURTH['fx'], PR_TEN['v'])   # the land granted at Genesis 15:18 — 1:8's "the land the LORD swore to your fathers" the same entry, read; the Kenite, Kenizzite and Kadmonite kept for the future (Edom, Moab, Ammon — Bereshit Rabbah 44:23): the three bars' ground on the shelf; Og the escapee (Bereshit Rabbah 42:8)
MM_TWO = MM.sodom('two_peoples_named')
assert MM_TWO['v'] == ('moab', 'ben-ammi') and 'begotten' in MM_TWO['fx'], MM_TWO   # Moab and Ben-ammi — the two peoples Lot's daughters named (Genesis 19:37-38): the bars' two parties and their difference (the elder's and the younger's speech)
JS_SEIR = JS.edom('parted_for_room'); JS_KINGS = JS.edom('kings_count')
assert JS_SEIR['v'] == 'too_great_to_dwell_together' and 'dwelt_in_seir' in JS_SEIR['fx'] and JS_KINGS['v'] == 8, (JS_SEIR, JS_KINGS['v'])   # Esau dwelt in Mount Seir (Genesis 36:8) — 2:5's "I have given Mount Seir to Esau" the grant the joseph runner's status carries
OR_ASYM = OR.courts('asymmetry'); OR_ONE_TWO = OR.courts('one_vs_two'); OR_23 = OR.courts('twenty_three'); OR_BRIBE = OR.courts('bribe'); OR_BORDERS = OR.land('borders')
assert OR_ASYM['v'] == 'acquit_by_one_convict_by_two' and OR_ONE_TWO['v'] == 'merit_by_one_liability_by_two' and OR_23['v'] == 23 and OR_BRIBE['v'] == 'the_bribed_judges_eyes_dim' and OR_BORDERS['v'] == ['sea_of_reeds', 'sea_of_the_philistines', 'the_wilderness', 'the_river'], (OR_ASYM['v'], OR_ONE_TWO['v'], OR_23['v'], OR_BRIBE['v'], OR_BORDERS['v'])   # the courts' clauses of Exodus 23 — the majority's asymmetry (Mishnah Sanhedrin 4:1's second difference), the twenty-three, the bribe; 23:31's border "from the wilderness to the river" beside 1:7's Euphrates
HO_FIVE = HO.conduct('five_effects'); HO_PROTOCOL = HO.conduct('protocol'); HO_MEASURER = HO.conduct('judge_is_measurer'); HO_EQUAL = HO.conduct('equal_treatment')
assert HO_FIVE['v'] == ['defiles_the_land', 'profanes_the_Name', 'removes_the_Presence', 'fells_by_the_sword', 'exiles'] and 'judgment_perverted' in HO_FIVE['fx'] and HO_PROTOCOL['v'] == 'parties_heard_sent_out_judges_deliberate_the_senior_announces' and HO_MEASURER['v'] == 'one_clause_at_two_seats' and HO_EQUAL['v'] == ['not_one_at_length_and_one_cut_short', 'not_one_standing_and_one_sitting'], (HO_FIVE['v'], HO_PROTOCOL['v'], HO_MEASURER['v'], HO_EQUAL['v'])   # the perverting judge's five effects (the Sifra on 19:15) — the exam's judgment_perverted verdict; R. Nechemya's protocol = Mishnah Sanhedrin 3:7's "so-and-so, you are clear"
ER_HOREB = ER.presence('horev_plene'); ER_AVOT = ER.presence('sheet_avot_1_1'); ER_ORDERS = ER.covenant('nations_seven_orders')
assert ER_HOREB['v'] == 1 and ER_AVOT['v'] == 'moses_joshua_elders_prophets_great_assembly' and ER_ORDERS['v'] == 7, (ER_HOREB['v'], ER_AVOT['v'], ER_ORDERS['v'])   # Horeb written plene at Exodus 33:6 alone — 1:6's "in Horeb" defective; Avot 1:1's chain Moses to Joshua at the charge's be_deliberate; the nations in seven orders beside 1:7's seven regions
BH_SANH = BH.seventy_elders({'ask': 'sanhedrin'}, BH.DATA); BH_DATE = BH.march({'ask': 'date'}, BH.DATA); BH_HOBAB = BH.march({'ask': 'hobab'}, BH.DATA)
assert BH_SANH[0] == '71 (the Sages); 70 (R. Yehuda)' and BH_DATE[0].startswith('(2, 2, 20) — the twentieth of Iyar, year two') and BH_HOBAB[0].startswith('asked, refused, asked again') and BH.DATA['sanhedrin_size']['value'] == 71, (BH_SANH[0], BH_DATE[0], BH_HOBAB[0], BH.DATA['sanhedrin_size']['value'])   # the seventy with Moses over them — the seventy-one (Sanhedrin 2a:13; 16b:18 "with you"); the march's date the retrograde marker's day at 1:6; Hobab's plea_made the effect's first form
RF_SIX = RF.the_refuge_law({'ask': 'six_cities'}, RF.DATA); RF_DEBIT = RF.the_refuge_law({'ask': 'the_debit'}, RF.DATA)
assert RF_SIX[0].startswith('six cities (35:13-15) — [6], [3, 3], [6]: three and three; the names Deuteronomy 4:43') and RF_DEBIT[0].startswith('the debit (35:11-14) — appoint six cities: commanded on the people, OPEN by design to Deuteronomy 4:41') and RF.DATA['the_six_cities']['value']['beyond_the_jordan'] == ['Bezer (Reuben)', 'Ramoth in Gilead (Gad)', 'Golan in Bashan (Manasseh)'] and RF.DATA['the_court_of_twenty_three']['value'] == 23, (RF_SIX[0], RF_DEBIT[0], RF.DATA['the_six_cities']['value'], RF.DATA['the_court_of_twenty_three']['value'])   # the three eastern cities lie in 3:12-17's land — CHAPTER 4's act (4:41-43), the debit OPEN, not this compile's; the twenty-three from the congregation-tokens the charge's court by CALL
print('callees: exodus_story, shelach, chukat, gad_reuben, zelophehad, journeys, borders, second_census, bamidbar, balak, primeval, mamre, joseph, ordinances, holiness, erection, beha, refuge CALLED — every value asserted at import')

# ===== THE DATA CHANNEL — the parameter rows the ink leaves open (motion 2's recorded settings); THE READBACK TABLE first =========
GRADES = ('VERBATIM', 'TURNED', 'SHORTENED', 'EXPANDED', 'SUPPLIED', 'DISAGREES')
def rb(verses, told, tape_kind, tape_verse, entry, grade, why, open_=False):
    assert grade in GRADES, grade
    return {'verses': verses, 'told': told, 'tape_kind': tape_kind, 'tape_verse': tape_verse, 'entry': entry, 'grade': grade, 'why': why, 'open': open_}
READBACK = [
    rb('Deut 1:1-5', 'the frame — these are the words; the fortieth year; after Sihon; Moses undertook to expound', None, None, 'torah_expounded on israel_people (40, 11, 1)', 'SUPPLIED', "the book's ONE act of its own day — the frame; 1:3's 'according to all' the receipt of the whole book's rules (the Sifrei 2:8): the register seat Deut 1:3 ACT"),
    rb('Deut 1:6-8', 'the LORD spoke to us in Horeb: turn and take your journey; go in and possess', 'paran_reached', 'Num 12:16', 'commanded on israel_people journey_to_the_mountain_of_the_amorite — CLOSED by the prior run Num 12:16', 'SUPPLIED', "told only here (Exodus 33:1 the command's kin, Numbers 10:11-12 the departure): written once, dated (2, 2, 20) by the retrograde marker at 1:6, closed at once by the arrival in Paran (12:16)"),
    rb('Deut 1:9-15', 'I am not able to bear you alone; give wise, discerning and known men; I took the heads and set them captains and officers', 'judges_appointed', 'Exod 18:25-26', 'courts_established on israel_people ([1000, 100, 50, 10], 78600) at (1, 2, 16); the court in_force judges_appointed', 'TURNED', "Exodus 18:21-26 retold in Moses' mouth — Jethro's four qualities (valor, God-fearing, truth, hating gain) for 1:13's three (wise, discerning, known), 'officers for your tribes' ADDED (1:15), the burden 11:14's word: the appointment a REFERENCE, no second write"),
    rb('Deut 1:16-18', 'and I charged your judges at that time: hear between your brothers …', None, None, 'judges_charged on the-court (the six clauses) dated (1, 2, 16)', 'SUPPLIED', "the charge told only here — THE LAW of the span: one status on the court, dated at the court's founding day read off Israel's ledger (the retrograde marker at 1:9)"),
    rb('Deut 1:19', 'we journeyed from Horeb through the great and terrible wilderness, as the LORD commanded us, to Kadesh-barnea', 'cloud_lifted', 'Num 10:11-13', 'the encamped_at statuses of the march (10:11-12:16)', 'SHORTENED', "the whole march in one verse; 'as the LORD our God commanded us' A RUN CITATION of the departure's run (R5) — the register seat Deut 1:19 NONE, nothing paid"),
    rb('Deut 1:22-23', 'you came near and said: let us send men; the word was good in my eyes; I took twelve men, one for a tribe', 'spies_sent', 'Num 13:3-16', 'sent_to_spy on the-twelve-spies (2, 3, 29)', 'TURNED', "the PEOPLE'S asking against 13:2's 'send for yourself' (Sotah 34b:3 — at Moses' discretion; the two tellings reconciled on the shelf): the DATA row the_spies_asked"),
    rb('Deut 1:24-25', 'they went up, came to the valley of Eshcol, spied it out, took of the fruit, brought us word: good is the land', 'report_given', 'Num 13:27-29', 'report_given on the-twelve-spies (2, 5, 9)', 'SHORTENED', "'good is the land' = 14:7's words — Joshua and Caleb's in the spies' mouths (the Sifrei 23:3); 13:27's 'however the people' dropped (Sotah 35a:2 the lie with a grain of truth): the retelling keeps the truth"),
    rb('Deut 1:26-28', 'you would not go up; you murmured in your tents: the LORD hates us; our brothers have melted our heart — greater and taller than we, cities fortified to heaven, the Anakim', 'evil_report_spread', 'Num 13:31-33', 'evil_report_spread on the-ten-spies; wept on israel_people (2, 5, 9)', 'TURNED', "the spies' words in the people's mouths ('greater and taller than we' the plain sense of 13:31 — Sotah 35a:7 reads 'than Him'); 'you murmured' as two words (Shevuot 47b:5); 'the LORD hates us' told only here"),
    rb('Deut 1:29-33', 'I said to you: do not dread; the LORD your God who goes before you will fight for you, as in Egypt and in the wilderness — carried you as a man carries his son; in fire by night and in the cloud by day', 'joshua_and_caleb_pleaded', 'Num 14:5-9', 'plea_made on joshua and caleb (2, 5, 9)', 'TURNED', "14:9's 'fear them not' (Joshua and Caleb's) told as Moses' own; 'He will fight for you' Exodus 14:14's; the pillar (1:33) Exodus 13:21's by REFERENCE"),
    rb('Deut 1:34-36', 'the LORD heard your words and was angry and SWORE: not one of these men shall see the good land, save Caleb — he wholly followed', 'pardoned_and_decreed', 'Num 14:20-25', "sentence_pronounced on israel_people (14:26-35); caleb's holding_owed OPEN (14:24)", 'SHORTENED', "the oath's VERB supplied ('and He swore' — 14:21, 28 say 'as I live'; 32:10 the first supplier — GR.DATA the_oath_supplied by CALL); Caleb's exception 14:24's; 'he wholly followed' Joshua 14:14's payment phrase"),
    rb('Deut 1:37', 'the LORD was angry with me for your sakes: you shall not go in there', 'sentence_at_meribah', 'Num 20:12-13', 'barred_from_the_land on moses OPEN (20:12)', 'DISAGREES', "THE GROUND OF THE BAR — 'for your sakes' at the spies' oath against 20:12's 'because you did not believe in Me': the tape's one entry stands; Psalm 106:32's 'for their sakes' the ink's own bridge outside the Torah, read, not run; no teacher joins them — an OPEN row", open_=True),
    rb('Deut 1:38', 'Joshua who stands before you, he shall go in there; strengthen him, for he shall cause Israel to inherit it', 'decree_declared', 'Num 14:26-35', "joshua's exception (14:30); nothing owed him in the ink (GR the_rebuke joshua_nothing_owed)", 'EXPANDED', "'he shall cause Israel to inherit' — the effect's FIRST seat (3:28 the second; Joshua 1:6 the run); 14:30 names Joshua among the exceptions and says nothing of the inheriting"),
    rb('Deut 1:39', 'your little ones who you said would be a prey, and your children who know not this day good and evil — they shall go in', 'decree_declared', 'Num 14:26-35', 'sentence_pronounced on israel_people — 14:31 the children brought in', 'VERBATIM', "the first five tokens = 14:31 word for word (computed: the shared prefix 5); then the children who know not good and evil ADDED (Eden's four seats the phrase's kin)"),
    rb('Deut 1:40', 'and you, turn and take your journey into the wilderness by the way of the Red Sea', 'pardoned_and_decreed', 'Num 14:20-25', 'commanded on israel_people the_turn_back (14:25) — CLOSED at 21:4', 'TURNED', "14:25's 'tomorrow turn and journey' with 'tomorrow' dropped and 'you' added; the debit's close at 21:4 READ (SL.decree turn_back by CALL: its run Num 21:4 / Deut 2:1)"),
    rb('Deut 1:41-44', 'you answered: we have sinned; we will go up and fight, as the LORD commanded us; you girded on weapons and presumed; the LORD said: go not up; you went up; the Amorite chased you as bees do and beat you down in Seir to Hormah', 'presumed_to_go_up', 'Num 14:39-44', 'presumed_to_go_up and defeated on israel_people (2, 5, 9)', 'EXPANDED', "'as bees do' and 'in Seir' told only here; 'as the LORD commanded us' in the PEOPLE'S mouth refused by 1:42-43 — the register seat Deut 1:41 NONE (R5): the tape's presumed_to_go_up read back; Hormah 14:45's proleptic name"),
    rb('Deut 1:45-46', 'you returned and wept before the LORD; the LORD did not hear your voice; you abode in Kadesh many days', 'congregation_wept', 'Num 14:1-4', 'wept on israel_people (14:1) — the night of the Ninth of Av', 'EXPANDED', "a SECOND weeping told only here, after Hormah — 'the LORD did not hear' (1:45 and 3:26 one phrase): no write, the refusal its own record; 'many days' at Kadesh — Seder Olam 8's nineteen years DATA"),
    rb('Deut 2:1', 'we turned and journeyed by the way of the Red Sea, as the LORD spoke to me; we compassed Mount Seir many days', 'journeyed_by_the_red_sea_way', 'Num 21:4', 'encamped_at on israel_people (21:4) — the turn-back debit CLOSED there', 'SHORTENED', "thirty-eight years in a verse; 'as the LORD spoke to me' the run citation of 14:25 (the close at 21:4 read)"),
    rb('Deut 2:2-8', 'the LORD said to me: you have compassed this mountain long enough; turn northward; do not contend with your brothers the sons of Esau — Mount Seir I gave to Esau; buy food and water for money; forty years lacking nothing; we passed from Elath and Ezion-geber by the way of Moab', 'journeyed_oboth_to_arnon', 'Num 21:10-13', 'commanded on israel_people turn_northward — CLOSED by the prior run Num 21:10-13; contending_barred and land_granted (mount_seir) on edom', 'SUPPLIED', "told only here: written once, dated (40, 6, 1) by the retrograde marker at 2:2, the debit closed at once by the march past Moab (21:10-13); the bar and the grant on Edom (Kiddushin 18a:2 — a gentile inherits by Torah law)"),
    rb('Deut 2:9', 'do not harass Moab nor contend with them in battle — Ar to the sons of Lot', None, None, 'contending_barred and land_granted (ar) on the-moabites', 'SUPPLIED', "told only here: the bar the a fortiori from Midian needed (Bava Kamma 38a:16 — BK.phinehas_and_midian by CALL); battle forbidden, harassing not (Horayot 10b:19)"),
    rb('Deut 2:13-15', 'rise up and get you over the brook Zered; we went over; thirty-eight years from Kadesh-barnea until the generation of the men of war was consumed', 'journeyed_oboth_to_arnon', 'Num 21:10-13', 'commanded on israel_people cross_the_brook_zered — CLOSED by the prior run Num 21:10-13 (21:12 the camp at Zered)', 'SUPPLIED', "told only here: written once, dated (40, 6, 1), closed at once by the camp at the brook Zered (21:12 inside the four camps' line); the thirty-eight [38] against the tape's years (the spies' return (2, 5, 9) to the counter's (40, 6, 1) = 38 by the era's year)"),
    rb('Deut 2:16-17', 'when all the men of war were consumed from among the people, the LORD SPOKE to me', 'decree_declared', 'Num 14:26-35', "the carcasses timer FIRED at (40, 5, 9); deaths_ceased (40, 5, 15) — SL.DATA by CALL", 'EXPANDED', "the speech resumed only after the last of that generation (Bava Batra 121b:1; Taanit 30b:12 — the fifteenth of Av); 'the LORD SPOKE to me' the Bible's one seat (computed)"),
    rb('Deut 2:17-19', 'when you come near the sons of Ammon, do not harass them nor contend with them — to the sons of Lot I have given it', None, None, 'contending_barred and land_granted on the-sons-of-ammon', 'SUPPLIED', "told only here: Ammon not even harassed (Bava Kamma 38b:6; Horayot 11a:1; Nazir 23b:12 — the younger daughter's reward); the one NEW written-on party (Genesis 19:38's people)"),
    rb('Deut 2:24-25', 'rise up, pass over the Arnon; I have given Sihon into your hand; begin to possess; this day I will begin to put the dread of you', 'sihon_smitten_land_possessed', 'Num 21:24-25', 'commanded on israel_people begin_to_possess_sihons_land — CLOSED by the prior run Num 21:24-25', 'SUPPLIED', "told only here (21:21 says Israel sent messengers, no command): written once, dated (40, 6, 1), closed at once by the smiting and possession (21:24-25); the dread the sun's row (Avodah Zarah 25a:7-9; Taanit 20a:6-8)"),
    rb('Deut 2:26-29', 'I sent messengers from Kedemoth to Sihon with words of peace: let me pass through; by the road, by the road; food and water for money — as the sons of Esau and the Moabites did for me', 'messengers_sent_to_sihon', 'Num 21:21-22', 'plea_made on israel_people (21:21-22)', 'SHORTENED', "nine tokens for seventeen (computed: 2:27 against 21:22; four shared); Kedemoth and 'words of peace' told only here (the Sifrei 199:5 credited)"),
    rb('Deut 2:29', 'as the sons of Esau who dwell in Seir did for me, and the Moabites who dwell in Ar', 'edom_refused', 'Num 20:18', 'refused on edom TWO (20:18, 20:20-21)', 'DISAGREES', "THE PASSAGE — 'as the sons of Esau did for me' against 20:18-21's double refusal and 21:4's going round: the chukat runner's DATA row edom_passage holds both arms as a DISPUTE (CK by CALL); the Sifrei silent (no piska on 2:29); Judges 11:17's double refusal outside the Torah: no link of our own — an OPEN row", open_=True),
    rb('Deut 2:30', 'Sihon would not let us pass; the LORD your God hardened his spirit and made his heart obstinate', 'sihon_came_out_and_fought', 'Num 21:23', 'refused on sihon (21:23)', 'EXPANDED', "the hardening told only here — Pharaoh's two verbs (the exodus story's hardening seats by REFERENCE); 21:23 says he did not let Israel pass and came out"),
    rb('Deut 2:32-33', 'Sihon came out against us to battle at Jahaz; the LORD gave him before us and we smote him and his son and all his people', 'sihon_came_out_and_fought', 'Num 21:23', 'refused on sihon; kings_smitten on sihon (21:24)', 'SHORTENED', "eight tokens for twenty (computed: 2:32 against 21:23; five shared); 2:33 WRITTEN 'his son', READ 'his sons' (the store's twelve tokens against the DB's eleven; Onkelos plural)"),
    rb('Deut 2:34-35', 'we took all his cities and devoted every city — the men, the women and the little ones; only the cattle and the spoil we took', 'sihon_smitten_land_possessed', 'Num 21:24-25', 'destroyed on the-amorite (the supplied act sihons_cities_devoted)', 'SUPPLIED', "THE BAN TOLD ONLY HERE — 21:24-25 say smote and possessed: written once, dated (40, 6, 1); Genesis 15:16's amorite_not_full READ beside it (a printed line, no verdict); Deuteronomy 20:16-17's law FORWARD"),
    rb('Deut 2:36-37', 'from Aroer on the Arnon to Gilead there was no city too high; only to the land of the sons of Ammon you came not near', 'sihon_smitten_land_possessed', 'Num 21:24-25', "land_possessed on israel_people (21:24-25) — 'as far as the sons of Ammon, for the border was strong'", 'EXPANDED', "the border RESPECTED told here (2:37) against 21:24's border STRONG — CK.DATA ammon_border by CALL: the same border, the bar's reason on the shelf"),
    rb('Deut 3:1-3', 'we turned and went up by the way of Bashan; Og came out against us at Edrei; the LORD said to me: fear him not; He gave into our hand Og and all his people', 'og_came_out_and_fear_not', 'Num 21:33-34', 'fear_not_promised on moses (21:34); kings_smitten on og (21:35)', 'TURNED', "3:1-3 = 21:33-35 with the persons shifted — we for they, 'to me' for 'to Moses' (computed: fifty-four tokens for fifty-six, thirty shared, the five shifts; CK.well_and_kings deut3_delta by CALL)"),
    rb('Deut 3:4-7', 'we took all his cities — sixty cities, all the region of Argob, fortified with high walls, gates and bars; we devoted them as we did to Sihon; the cattle and the spoil we took', 'og_smitten', 'Num 21:35', 'land_possessed on israel_people (21:35); destroyed on the-amorite (the supplied act ogs_cities_devoted)', 'EXPANDED', "the sixty [60] and Argob told only here (Arakhin 32b:6 / Megillah 10a:10 / Shevuot 16a:14 the walled cities from Joshua's days); THE SECOND BAN told only here — 21:35 says smote and possessed"),
    rb('Deut 3:8-11', 'we took the land from the Arnon to Hermon (Sirion, Senir); all the cities of the plain, Gilead and Bashan to Salcah and Edrei; Og the remnant of the Rephaim — his bedstead of iron, nine cubits by four, by the cubit of a man', 'og_smitten', 'Num 21:35', 'land_possessed on israel_people (21:24-25, 21:35) — the land east of the Jordan', 'EXPANDED', "Hermon's three names (Chullin 60b:14 — the verses fit to be burned); Og's bed [9, 4] 'by the cubit of a man' (Kelim 17:9-10; Eruvin 4:8) — CK.DATA og_lore by CALL; the remnant of the Rephaim (Sanhedrin 90b-91a the shelf's Og)"),
    rb('Deut 3:12-13', 'this land we possessed at that time: from Aroer, and HALF the hill country of Gilead to the Reubenite and the Gadite; the rest of Gilead and all Bashan to the HALF tribe of Manasseh', 'land_granted_east', 'Num 32:33', 'holding_given on the sons of Gad, the sons of Reuben and the half tribe of Manasseh (32:33) — three transfers', 'EXPANDED', "thirty-six tokens for twenty-nine (computed): the retelling DIVIDES what 32:33 gave whole — half Gilead to the two, the rest and Bashan to the half tribe; the two halves read [1/2], [1/2] by rule 30 (34:13-15's halves the kin — BO the_nine_and_a_half by CALL)"),
    rb('Deut 3:14', 'Jair son of Manasseh took all the region of Argob to the border of the Geshurite and the Maacathite, and called them after his own name Havvoth-jair to this day', 'villages_taken_by_jair', 'Num 32:41', 'land_possessed on jair (32:41)', 'EXPANDED', "twenty-three tokens for eleven (computed): Argob, the Geshurite and the Maacathite, 'to this day' told only here (GR machir_jair_nobah jair by CALL; 1 Kings 4:13 the kin)"),
    rb('Deut 3:15', 'and to Machir I gave Gilead', 'gilead_taken_by_machir', 'Num 32:39-40', 'holding_given on the-sons-of-machir (32:40)', 'TURNED', "'I gave' for 'Moses gave' (32:40) — the person shifted, the five tokens for eleven (GR machir_jair_nobah gilead_given by CALL)"),
    rb('Deut 3:16-17', 'to the Reubenite and the Gadite from Gilead to the brook Arnon — the middle of the brook the border — to the Jabbok, the border of the sons of Ammon; the Arabah and the Jordan from Chinnereth to the sea of the Arabah, the Salt Sea, under the slopes of Pisgah eastward', 'land_granted_east', 'Num 32:33', 'holding_given on the sons of Gad and the sons of Reuben (32:33)', 'EXPANDED', "the east's BORDERS told only here — the Arnon's middle, the Jabbok, Chinnereth to the Salt Sea under Pisgah: DATA the_easts_borders, no write (the holdings stand)"),
    rb('Deut 3:18-20', 'I commanded you at that time: the LORD has given you this land; you shall pass over ARMED before your brothers, all the men of valor; only your wives and little ones and cattle shall abide in your cities; until the LORD gives rest to your brothers as to you — then you shall return every man to his possession', 'condition_stipulated', 'Num 32:20-24', 'commanded on the-sons-of-gad-and-reuben cross_armed_before_the_lord_until_the_land_is_subdued OPEN (32:20-24)', 'TURNED', "the condition in Moses' first person with half Manasseh included (GR.DATA half_manassehs_stipulation by CALL); 'armed' 3:18 = 32:30, 32; 'until the LORD gives rest' = Joshua 1:15 word for word — the release Joshua 22:4 outside the Torah; the debit OPEN read"),
    rb('Deut 3:21-22', 'I commanded Joshua at that time: your eyes have seen all that the LORD did to these two kings; so shall the LORD do to all the kingdoms; you shall not fear them, for the LORD fights for you', None, None, 'fear_not_promised on yehoshua (the supplied act joshua_encouraged)', 'SUPPLIED', "told only here: HEAVEN's promise on Joshua — 21:34's effect at its second party (the first Moses'); Joshua 1:6 and Ai's run outside the Torah (the Sifrei 29:8-9 the condition Joshua broke, DATA); Joshua PLENE here alone in the Torah"),
    rb('Deut 3:23-26', 'I besought the LORD at that time: O Lord GOD, You have begun to show Your servant Your greatness; let me go over and see the good land, that good mountain and Lebanon; the LORD was wroth with me for your sakes and did not hear me: let it suffice you; speak no more to Me of this matter', None, None, 'plea_made on moses with the refusal in the value (the supplied act moses_besought); barred_from_the_land OPEN read', 'SUPPLIED', "told only here: the plea AND its answer as Hobab's row carries the refusal — no new heaven write, the barred entry OPEN read; praise before the request (Berakhot 32a:32); 'let it suffice you' measure for measure (Sotah 13b:13); the ten names of prayer (the Sifrei 26:7) and the directions (Mishnah Berakhot 4:5-6) DATA"),
    rb('Deut 3:27', 'go up to the top of Pisgah and lift up your eyes westward, northward, southward and eastward, and see with your eyes; for you shall not go over this Jordan', 'moses_told_to_ascend_abarim', 'Num 27:12-14', 'commanded on moses see_the_land_from_abarim OPEN (27:12) — to Deuteronomy 34:1-4', 'TURNED', "27:12's 'go up to this mountain of Abarim and see the land' with PISGAH for Abarim (34:1: Mount Nebo, the top of Pisgah — one mountain, three names: DATA the_commission) and the four directions ADDED in the third order (Genesis 13:14, 28:14 the others): the debit READ BACK, no second write"),
    rb('Deut 3:28', 'command Joshua, and strengthen him and encourage him; for he shall go over before this people and he shall cause them to inherit the land', 'joshua_commissioned', 'Num 27:22-23', 'invested_office on yehoshua (27:22-23); the commission debit on moses CLOSED by its run', 'TURNED', "the commissioning READ BACK with the words of Deuteronomy 31:7, 23 and Joshua 1:6 ('be strong and of good courage' nine seats); 'command' a galvanization, immediate and for generations (Kiddushin 29a:14); 'he shall cause them to inherit' the effect's second seat"),
    rb('Deut 3:29', 'we abode in the valley over against Beth-peor', 'encamped_in_the_plains_of_moab', 'Num 22:1', 'encamped_at on israel_people — the plains of Moab (22:1), the last camp', 'EXPANDED', "the valley named (3:29; 4:46 the speech's place; 34:6 Moses' grave) — BK.the_call last_camp by CALL: the book never moves again"),
]
RB_GRADES = collections.Counter(r['grade'] for r in READBACK)
assert len(READBACK) == 42 and RB_GRADES == collections.Counter({'EXPANDED': 12, 'SUPPLIED': 11, 'TURNED': 10, 'SHORTENED': 6, 'DISAGREES': 2, 'VERBATIM': 1}) and [r['verses'] for r in READBACK if r['open']] == ['Deut 1:37', 'Deut 2:29'], (len(READBACK), RB_GRADES, [r['verses'] for r in READBACK if r['open']])   # FORTY-TWO reference rows; the two DISAGREES rows OPEN; every retold act's row names the tape's kind and first verse (CA4 finds each on the running world)

DATA = {
    'the_readback': {'value': READBACK, 'settings': {'the_first_form': "THE_LOOP.md step 6, the owner's 'Yes 1. Go' (2026-09-15): a retelling is a REFERENCE ROW, never a second act; the six grades VERBATIM / TURNED / SHORTENED / EXPANDED / SUPPLIED / DISAGREES; the deltas recomputed from the DB (the shared prefix 5 at 1:39; nine for seventeen at 2:27; eight for twenty at 2:32; fifty-four for fifty-six at 3:1-3; twenty-three for eleven at 3:14; thirty-six for twenty-nine at 3:12-13); the SUPPLIED acts written once at their own time by the retrograde markers, four CLOSED at once by a prior run; the DISAGREES rows OPEN; the receipts run citations (1:19, 1:41)", 'the_laws_half': "the full readback (the laws re-read against the ledger from chapter 5 on) OWED to its own sitting when chapter 5 opens"},
                     'source': "Deuteronomy 1:1-3:29 against Numbers 10-14, 20-21, 27, 32 and Exodus 18 on the tape — every row's entry found by kind and first verse (CA4)"},
    'the_officers_table': {'value': {'grains': [1000] + GRAINS, 'count_round': ES_JUDGES['v'], 'count_exact': EXACT_COUNT, 'census_total': CENSUS_TOTAL}, 'settings': {'the_round': "78,600 on the round six hundred thousand (Exodus 12:37) — Sanhedrin 18a:3's own total; the Sifrei 14:1's 'eighty thousand less a few'; the Jerusalem Talmud Sanhedrin 10:2's arithmetic (BK.peor judges_count by CALL: each executing two = 157,200)", 'the_exact': "79,064 on the census's exact 603,550 by INTEGER DIVISION at every grain — 603 + 6,035 + 12,071 + 60,355 (CB.census total by CALL): the Sifrei 15:4's ROUNDING RULE — a thousand less one yields one captain of a thousand — is integer division's own form", 'the_grains': "the four grains — the parser's [100, 50, 10] at 1:15 with the plural 'thousands' a NOUN (rule 29's other half); ES.jethro('denominations') by CALL = 4", 'the_officers': "'and officers for your tribes' (1:15) — the Levites with the strap (the Sifrei 15:5; 2 Chronicles 19:11 outside the Torah); Deuteronomy 16:18's 'judges and officers in all your gates for your tribes' the second seat (Sanhedrin 16b:9-10 — judges for Israel, for every tribe, for every city)", 'the_blessing': "1:11's 'may the LORD add to you a thousand times' — Moses' own beside God's (the Sifrei 11:1); a priest may not add it (Rosh Hashanah 28b:10)"},
                           'source': "1:15 [100, 50, 10] by the parser; Exodus 18:21, 25 by CALL; 603,550 by CALL; the appointment itself a REFERENCE to judges_appointed (Exodus 18:25 — the readback row, TURNED)"},
    'the_seven_qualities': {'value': {'jethros_four': ['men of valor', 'fearers of God', 'men of truth', 'haters of gain'], 'moses_three_asked': ['wise', 'discerning', 'known'], 'moses_two_found': ['wise', 'known'], 'asked': 7, 'found': 3}, 'settings': {'the_sifrei': "seven qualities Moses sought, three he found (the Sifrei 15:2) — 1:13's three against 1:15's two: the discerning not found (Eruvin 100b:18; Nedarim 20b:10 — the generation's sons)", 'the_talmud': "on the Great Sanhedrin only men of stature, wisdom, appearance, age, who know sorcery and seventy languages (Sanhedrin 17a:21); one who can render a creeping thing pure by Torah law (17a:22)", 'jethros_four': "Exodus 18:21 by the tokens — the exodus engine's cell by CALL"},
                            'source': "1:13 'wise and discerning and known' ONE seat, 1:15 'wise and known' ONE seat — computed"},
    'the_judges_charge': {'value': ['hear between your brothers', 'judge righteously between a man and his brother and his stranger', 'no faces in judgment', 'the small as the great', 'fear no man, for the judgment is God\'s', 'the hard matter to me'], 'settings': {'hear': "a judge may not hear one litigant before the other comes (Sanhedrin 7b:14 — R. Chanina); 'charged' with alacrity — the rod and the strap (7b:14-15)", 'judge_righteously': "the true judgment truly makes the Presence rest in Israel (7a:17 — R. Yonatan); deliberate (Avot 1:1 — the Sifrei 16:1 cites the Mishnah as the verse's reading)", 'no_faces': "R. Yehuda: do not befriend the litigant; R. Elazar: do not estrange him (7b:18) — a DISPUTE row; Leviticus 19:15's 'in righteousness you shall judge' (HO.conduct by CALL — the five effects of the perverting judge); the appointer addressed (the Sifrei 17:1)", 'small_and_great': "the judgment of one peruta as dear as of a hundred maneh (8a:2 — Reish Lakish); the order of hearing (8a:4-5)", 'no_fear': "'you shall not be afraid' a term for gathering in — a judge may not hold back his words (7a:16); the refusal before hearing, not after (6b:12 — Reish Lakish; the Sifrei 17:4); the student who sees merit for the poor not silent (6b:13)", 'the_judgment_is_gods': "let the judgment pierce the mountain (6b:3); the judge who takes from one and gives to the other — the Holy One takes his life (7a:18); the Rambam's introduction 15:58", 'the_hard_matter': "Exodus 18:26's hard_cases_to_moses STATUS read (ES by CALL); the Sifrei 17:7 — Zelophehad's daughters, THE TENT (ZL.the_daughters halt by CALL: the third form)", 'the_stranger': "a convert converts only before a court (Yevamot 47a:7 — R. Yehuda); the gentile litigant — R. Ishmael's two rulings against Rabban Shimon ben Gamliel (the Sifrei 16:4)", 'a_man_excludes_the_minor': "the Sifrei 16:6", 'the_al_tikrei': "'I will set them as your heads' read 'their guilt on your heads' (the Sifrei 13:6) — THE REVOCALIZATION, MOVE_CATALOG's entry"},
                          'source': "1:16-17 — the six clauses each ONE seat in the Bible (computed); the effect judges_charged's value"},
    'the_compromise': {'value': 'three_settings', 'settings': {'r_yehoshua_ben_korcha': "a MITZVA to mediate — 'execute the judgment of truth and peace in your gates' (Zechariah 8:16; Sanhedrin 6b:6)", 'r_eliezer_son_of_r_yosei_hagelili': "compromise FORBIDDEN once the case is heard — 'the judgment is God's' (1:17; Sanhedrin 6b:8); David's charity his own money", 'r_shimon_ben_menasya': "before hearing, or after hearing but before knowing where the judgment leans — 'go and compromise' (6b:11)", 'the_verdict': "once the verdict is issued, no compromise (6b:1); what is a verdict — 'so-and-so, you are liable / exempt' (6b:15 — Rav Yehuda in Rav's name)", 'justice_justice': "'justice, justice you shall pursue' (Deuteronomy 16:20) — one for judgment, one for compromise: the two boats, the two camels (Sanhedrin 32b:4-6; Leviticus 19:15's 'in justice' the other reading)"},
                       'source': "Sanhedrin 6b:1-15 and 32b:4-6 on 1:17's clause — TWO VERDICT TABLES as DATA"},
    'the_gentile_litigant': {'value': 'r_ishmaels_two_rulings', 'settings': {'r_ishmael': "an Israelite and a gentile before you — if you can acquit the Israelite by Israel's law, acquit; by the nations' law, acquit (the Sifrei 16:4)", 'rabban_shimon_ben_gamliel': "you judge only by their law (the Sifrei 16:4)", 'the_stranger_of_1_16': "'and the stranger with him' — the convert (Yevamot 47a:7)"},
                             'source': "the Sifrei 16:4 on 1:16's 'between a man and his brother and his stranger'"},
    'the_frame': {'value': {'words_of_1_1': len(words(1, 1)), 'places': ['the wilderness', 'the Arabah', 'Suph', 'Paran', 'Tophel', 'Laban', 'Hazeroth', 'Di-zahab']}, 'settings': {'the_sifrei_1': "the places as the rebuke's sins — the wilderness (the calf), the Arabah (Peor), Suph (the sea), Paran (the spies), Tophel and Laban (the manna), Hazeroth (Korach), Di-zahab (the calf's gold): the Sifrei 1; Onkelos writes them INTO the verse (thirty-three tokens for twenty-two)", 'di_zahab': "the school of R. Yannai: no such place — the gold lavished until they said 'enough' made the calf (Berakhot 32a:7; Sanhedrin 102a:14)", 'the_kings_reading': "the king reads from 'these are the words' at the assembly (Mishnah Sotah 7:8; Sotah 41a:18; Tosefta Sotah 7:9)", 'r_akiva': "the generalities and the details at Sinai, repeated in the Tent, a third time in the plains of Moab (Zevachim 115b:17)", 'the_expounding': "'Moses undertook to expound' (1:5) with 27:8's 'clearly' — the seventy languages (Sotah 35b:6); the Rambam's introduction 2:19 the first of Shevat"},
                  'source': "1:1's twenty-two tokens (computed); 1:5's expound-root two Torah seats (computed)"},
    'the_date': {'value': {'numbers': SPEECH_DATE, 'day': (40, 11, 1), 'era': 'exodus', 'reader': 'number'}, 'settings': {'two_readers': "1:3 'in the fortieth year, in the eleventh month, on the first of the month' by the NUMBER reader [40, 11, 1]; 33:38 'in the fortieth year … in the fifth month' by the ORDINAL reader [40, 5] — ONE CLOCK, TWO READERS (JO.aarons_death_retold the_date by CALL)", 'the_era': "the fortieth year the EXODUS'S by the verbal analogy 'the fortieth year' / 'the fortieth year' with 33:38's 'of the going out' (Rosh Hashanah 2b:11 — Rav Pappa; JO verbal_analogy by CALL: THE TRANSFER TAUGHT)", 'the_new_year': "Av and Shevat one year — not Tishrei, not Iyar: Exodus 40:17 and Numbers 10:11 one year (Rosh Hashanah 3a:5; JO the_era_new_year by CALL)", 'the_order': "Aaron's death (40, 5, 1), Arad, the departure (40, 6, 1), Sihon, the speech (40, 11, 1) — 'after he had smitten Sihon' (1:4): Rosh Hashanah 2b:13, 3a:12 (JO the_order by CALL)", 'the_cost': "the counter's walk from (40, 6, 1) to (40, 11, 1) fires thirty-six timers and re-arms thirty (measured: deu_advance_probe.out)"},
                 'source': "1:3 [40, 11, 1] by the parser (computed); the marker at the tape position Deut 1:1"},
    'the_horeb_command': {'value': {'regions': ['the Arabah', 'the hill country', 'the lowland', 'the Negev', 'the seashore', 'the land of the Canaanites', 'Lebanon'], 'river': 'the Euphrates', 'closed_by': 'Num 12:16'}, 'settings': {'the_kin': "Exodus 33:1 'depart, go up hence' the command's kin (ER by CALL — Horeb plene at 33:6 alone); Numbers 10:11-12 the departure's day (BH.march date by CALL — (2, 2, 20), the retrograde marker's day)", 'the_regions': "every tribe's portion held some of each kind (Bava Kamma 81b:6 — Joshua's ten conditions); Mishnah Sheviit 9:2's three lands (the Sifrei 6:1); the Euphrates called great because near the land (Shevuot 47b:6)", 'the_grant': "'go in and possess the land the LORD swore to your fathers' (1:8) — a REFERENCE to land_granted (Genesis 15:18 — PR.call land_seats by CALL) and to the OPEN dispossess debit (33:50-56), cited, not rewritten; 'to give THEM' (Deuteronomy 11:21) the resurrection's proof on the shelf (Sanhedrin 90b:12)"},
                          'source': "1:6-8 told only here — the supplied debit CLOSED BY THE PRIOR RUN Num 12:16 (the arrival in Paran)"},
    'the_spies_asked': {'value': 'the_people_asked_and_moses_sent_at_his_discretion', 'settings': {'reish_lakish': "'send for yourself' (13:2) — at your discretion, not a divine command (Sotah 34b:3); 1:22 the people's asking (SL.spies send_for_yourself by CALL)", 'that_they_may_search': "'that they may search the land for us' (1:22 — veyachperu) with Isaiah 24:23's 'the moon will be embarrassed' (Sotah 34b:4)", 'the_twelve': "[12, 1] — one man for a tribe (SL.spies one_per_tribe by CALL)"},
                        'source': "13:1-2 and 1:22-23 — the two tellings reconciled on the shelf (Sotah 34b:3-4)"},
    'the_bars_ground': {'value': 'disagrees_open', 'settings': {'the_spies_oath': "'the LORD was angry with me FOR YOUR SAKES: you shall not go in there' (1:37) — the bar told at the spies' oath", 'meribah': "'because you did not believe in Me, to sanctify Me' (20:12) — the tape's one entry barred_from_the_land on Moses (CK.meribah sentence by CALL)", 'psalm_106': "'they angered Him at the waters of Meribah and it went ill with Moses for their sakes' (Psalm 106:32) — the ink's own bridge OUTSIDE the Torah, read, not run", 'the_row': "no teacher joins the two grounds inside the Torah — an OPEN row (R4)"},
                        'source': "1:37 against 20:12 — DISAGREES; 3:26's 'for your sakes' the same ground at the plea"},
    'the_dispossessions': {'value': [('the Emim', 'Moab', 'Deut 2:10-11'), ('the Horites', 'the sons of Esau', 'Deut 2:12, 2:22'), ('the Zamzummim', 'the sons of Ammon', 'Deut 2:20-21'), ('the Avvim', 'the Caphtorim', 'Deut 2:23')], 'settings': {'genesis_14': "the Rephaim, the Zuzim, the Emim at their first seats (Genesis 14:5 — PR by CALL); the Horites in their Mount Seir (14:6; 36:20 — JS by CALL)", 'chullin_60b': "'the Avvim … the Caphtorim destroyed them' (2:23) — Reish Lakish's verses fit to be burned that are the Torah's body (Chullin 60b:11); Hermon's names (60b:14)", 'as_israel_did': "'as Israel did to the land of his possession' (2:12) — ONE seat: the dispossessions the ink's own pattern of title", 'the_lands_title': "Geviha ben Pesisa against Afrikiya — Canaan a slave, a slave's acquisitions his master's (Sanhedrin 91a:8)"},
                           'source': "2:10-12, 2:20-23 — the four dispossessions, every people's token seated (computed)"},
    'the_bypass_commands': {'value': {'edom': ('contending_barred', 'land_granted', 'mount_seir'), 'moab': ('contending_barred', 'land_granted', 'ar'), 'ammon': ('contending_barred', 'land_granted', 'the land of the sons of Ammon')}, 'settings': {'the_difference': "Moab: battle forbidden, harassing not (Horayot 10b:19; Nazir 23b:11 — the reward of the elder daughter's euphemism); Ammon: not even harassed (Bava Kamma 38b:6; Horayot 11a:1; Nazir 23b:12 — the younger's); Edom: 'your brothers' (2:4, 2:8; Deuteronomy 23:8 forward) — a PARAMETER of the block's reach", 'the_a_fortiori': "what entered Moses' mind? his own a fortiori from Midian — the bar needed (Bava Kamma 38a:16; BK.phinehas_and_midian midian_not_moab by CALL)", 'the_inheritance': "'I have given Mount Seir to Esau … Ar to the sons of Lot' — a gentile inherits by Torah law (Kiddushin 18a:2; Nazir 61a:11); the Kenite, Kenizzite and Kadmonite kept for the future (Bereshit Rabbah 44:23 — PR.pieces ten_nations by CALL)", 'sihon_purified': "Israel forbidden Moab's land; Sihon took it, Israel took it from Sihon (Chullin 60b:13; Numbers 21:26 — CK.DATA sihon_purified by CALL)", 'the_purchase': "'food you shall buy for money, water too' (2:6) — a permission: food like water needs no gentile's preparation (Avodah Zarah 37b:15)"},
                            'source': "2:5, 2:9, 2:19 — the contend-root's three bars beside a grant each (computed: the four seats, 2:24 the positive)"},
    'the_thirty_eight': {'value': {'ink': THIRTY_EIGHT, 'from': (2, 5, 9), 'to': (40, 6, 1), 'deaths_ceased': (40, 5, 15)}, 'settings': {'the_tape': "the spies' return (2, 5, 9) to the departure from Mount Hor (40, 6, 1) — thirty-eight by the era's year (computed at the checkpoint CA2); 40 − 38 = 2 the era's year at the decree (SL.decree count_from by CALL)", 'deaths_ceased': "the fifteenth of Av the dying ceased (Bava Batra 121a:9; Taanit 30b:12 — SL.DATA by CALL); 'when all the men of war were consumed … the LORD SPOKE to me' (2:16-17) — the speech resumed (Bava Batra 121b:1)", 'the_zered': "the Zered crossed after the thirty-eight years (CK.well_and_kings zered_date by CALL)"},
                         'source': "2:14 [38] by the parser (computed); the tape's two days"},
    'the_edom_disagreement': {'value': CK.DATA['edom_passage']['value'], 'settings': dict(CK.DATA['edom_passage']['settings'], **{'the_row_open': "2:29 'as the sons of Esau who dwell in Seir did for me' against 20:18-21's refusal and 21:4's going round: the chukat runner's DISPUTE row holds both arms; the Sifrei silent (no piska on 2:29); Judges 11:17's double refusal outside the Torah; no link of our own — OPEN (R4)"}),
                              'source': "CK.DATA['edom_passage'] by CALL; 2:29 ONE seat (computed)"},
    'the_ban': {'value': 'told_only_in_the_retelling', 'settings': {'sihon': "'we devoted every city — the men, the women and the little ones' (2:34) against 21:24-25's 'smote … possessed'", 'og': "'as we did to Sihon' (3:6) against 21:35's 'smote … possessed'", 'the_effect': "destroyed — the body effect the king of Arad's line wrote at 21:3 (the cherem executed; Leviticus 27:28-29 by the temurah engine), on the Amorite twice", 'genesis_15_16': "'the iniquity of the Amorite is not yet full' — amorite_not_full on the Amorite READ (PR.pieces fourth_generation by CALL), a printed line, no verdict", 'the_law_forward': "Deuteronomy 20:16-17's cherem law FORWARD — its runner's; the bans here acts, not law"},
                'source': "'and we devoted' at 2:34 and 3:6 alone (computed)"},
    'the_sixty_cities': {'value': {'ink': SIXTY, 'region': 'Argob'}, 'settings': {'walled_from_joshuas_days': "the walled cities from Joshua's days many; the Sages enumerated the re-sanctified (Arakhin 32b:6 — R. Yishmael son of R. Yosei; Megillah 10a:10; Shevuot 16a:14)", 'walled_learned': "'walled' (Leviticus 25:29) learned from 3:5's 'fortified with high walls' by the verbal analogy (Arakhin 33b:22 — the refuge docket credited)", 'the_kin': "1 Kings 4:13 (Jair's sixty great cities with walls and bars); 1 Chronicles 2:23; Joshua 13:30 — the three Bible seats of 'sixty cities' (computed)"},
                         'source': "3:4 [60] by the parser; 'sixty cities' three seats; 'the region of Argob' three (computed)"},
    'ogs_bed': {'value': {'ink': BED, 'unit': 'the cubit of a man'}, 'settings': {'kelim': "the cubit of which they spoke is the medium one (Mishnah Kelim 17:9); R. Meir and R. Yehuda on the cubits (17:10); Mishnah Eruvin 4:8", 'og_lore': "Og — Sihon's brother of the Rephaim, the flood's survivor by the lore (CK.DATA og_lore by CALL: Niddah 61a:18; Zevachim 113b:12); the escapee of Genesis 14:13 (PR.war og by CALL — Bereshit Rabbah 42:8)", 'the_remnant': "'the remnant of the Rephaim' three seats (Joshua 12:4, 13:12); Sanhedrin 90b-91a the shelf's Og"},
                'source': "3:11 [9, 4] by the parser; 'by the cubit of a man' ONE seat (computed)"},
    'the_easts_borders': {'value': {'south': 'the brook Arnon — the middle of the brook the border', 'north_east': 'the Jabbok — the border of the sons of Ammon', 'west': 'the Arabah and the Jordan, from Chinnereth to the sea of the Arabah, the Salt Sea, under the slopes of Pisgah'}, 'settings': {'told_only_here': "3:16-17 — the east's borders in the retelling alone; 32:33 gave the kingdoms whole; 34:12's Salt Sea the west's east (BO.the_four_sides the_east by CALL)", 'no_write': "the holdings stand (holding_given ×3 at 32:33 read at CA6); the borders DATA"},
                          'source': "3:16-17 — 'the middle of the brook' ONE seat, 'the sea of the Arabah, the Salt Sea' three, 'under the slopes of Pisgah' two (computed)"},
    'the_armed_passage': {'value': {'armed_seats': ARMED, 'until_rest': UNTIL_REST, 'release': 'Josh 22:4'}, 'settings': {'the_condition': "the condition's debit on the sons of Gad and Reuben OPEN (32:20-24 — GR.the_condition positive_arm by CALL); half Manasseh included by the retelling (GR.DATA by CALL)", 'the_release': "'until the LORD gives rest to your brothers' 3:20 = Joshua 1:15 word for word; Joshua 22:4 the release — outside the Torah (the readback's)", 'the_wives': "'your wives and your little ones and your cattle shall abide in your cities which I have given you' (3:19) — 32:26 retold"},
                          'source': "3:18-20 against 32:20-24 (TURNED); 'armed' three seats (computed)"},
    'joshuas_charge': {'value': {'plene': JOSHUA_PLENE, 'seen': 'your eyes have seen', 'promise': 'so shall the LORD do to all the kingdoms; He fights for you'}, 'settings': {'the_commission': "27:18-23 the commission (F0); 3:28 'command Joshua, strengthen him' READ BACK — 'command' a galvanization, immediate and for generations (Kiddushin 29a:14)", 'the_run': "Joshua 1:6 'be strong and of good courage' (nine seats); Joshua 23:3, 10 'He fights for you' — the run outside the Torah", 'ai': "the run against the spec at Ai — the condition Joshua broke (the Sifrei 29:8-9): DATA", 'plene': "Joshua written PLENE at 3:21 alone in the Torah (Judges 2:7 the Bible's second) — computed"},
                       'source': "3:21-22 told only here (SUPPLIED — fear_not_promised on Joshua); 3:28 (TURNED)"},
    'the_plea': {'value': {'plea': 'let me go over and see the good land beyond the Jordan, that good mountain and Lebanon', 'answer': 'REFUSED — let it suffice you; speak no more to Me of this matter; the LORD was wroth with me for your sakes'}, 'settings': {'praise_first': "'You have begun to show Your servant Your greatness' before 'let me go over' — praise, then the request (Berakhot 32a:32; Avodah Zarah 7b:18 — R. Simlai)", 'the_mode': "'I pleaded' (3:23) against 'Moses besought' (Exodus 32:11) — the two modes (Berakhot 30b:9)", 'the_ten_names': "the ten names of prayer (the Sifrei 26:7) — the effects registry's candidates, filed", 'rav_lakh': "'let it suffice you' (3:26, singular — ONE seat) measure for measure for Korach's 'enough for you' (Numbers 16:3, 7 — Sotah 13b:13; the korach runner's token by REFERENCE)", 'lebanon': "'that good mountain and Lebanon' — Lebanon the Temple (the Sifrei 6:2, 28:3; Gittin 56b:1 — Isaiah 10:34; Onkelos)", 'the_names': "'O Lord GOD' — Abraham's two seats (Genesis 15:2, 15:8) and Moses' two (3:24; 9:26); 'Your greatness' the Sifrei 27:4's binyan av; 'Your strong hand' Solomon's (1 Kings 8:42 — computed)", 'the_directions': "the direction of prayer — toward the Temple, the heart toward the Holy of Holies (Mishnah Berakhot 4:5-6; Berakhot 30a:9 'by way of their land'; the Sifrei 29:5)", 'the_barred_entry': "barred_from_the_land on Moses OPEN (20:12) READ — no new heaven write; the refusal in plea_made's value as Hobab's row carries it (BH.march hobab by CALL)"},
                 'source': "3:23-26 told only here (SUPPLIED); 'was wroth' three Bible seats; 'let me go over, I pray' three (computed)"},
    'the_four_directions': {'value': {'Deut 3:27': DIR_D, 'Gen 13:14': DIR_G13, 'Gen 28:14': DIR_G28}, 'settings': {'three_orders': "west-north-south-east (3:27), north-south-east-west (Genesis 13:14 — Abram after Lot parted), west-east-north-south (Genesis 28:14 — Jacob at Bethel): the four directions in three orders, the reading's find computed", 'pisgah': "'the top of Pisgah' — Balaam's stand (23:14), the well's station (21:20), this and 34:1 (computed: four seats)"},
                            'source': "3:27's four direction-tokens against the two Genesis seats (computed)"},
    'the_commission': {'value': {'mountain_names': ['Abarim (27:12; 33:47-48; Deut 32:49)', 'Nebo (Deut 32:49; 34:1)', 'Pisgah (Deut 3:27; 34:1)'], 'hands': (HAND_SG, HANDS_PL), 'urim': C2.DATA['urim_judgment']['value']}, 'settings': {'one_mountain': "'Mount Nebo, the top of Pisgah' (34:1) — one mountain, three names; 'the mountain of Abarim' four seats (computed: 27:12; 33:47-48; Deuteronomy 32:49)", 'one_hand_two_laid': "'lay your HAND upon him' (27:18) — 'his HANDS' (27:23): one commanded, two laid — the Sifrei Bamidbar 141, credited at THE TENT; 'a man in whom is spirit' ONE seat", 'the_honor': "'some of your honor' (27:20) — the sun and the moon (Bava Batra 75a:8): Moses' face as the sun, Joshua's as the moon", 'the_urim': "'by the judgment of the Urim' (27:21) — a prophet's decree may be retracted, the Urim's not (Yoma 73b:3 — C2.DATA urim_judgment by CALL)", 'the_shepherd': "'the God of the spirits of all flesh' — 16:22's phrase at its second seat (computed); 'go out and come in' the leader's idiom; Eldad and Medad's prophecy — Moses will die, Joshua brings Israel in (Sanhedrin 17a:10 credited)", 'the_debit': "'see the land' — the debit see_the_land_from_abarim on Moses OPEN to Deuteronomy 34:1-4 (this book's end); 3:27 its retelling READ BACK", 'the_receipt': "'and Moses did as the LORD commanded him' (27:22) — the spec/run pair's form (CB8's): the commission's debit CLOSED by its run — the register seat Num 27:22 CLOSE"},
                       'source': "Num 27:12-23 — the callee's twelve verses, no number (computed); the seats of the mountain's names, the hand and the hands (computed)"},
}
assert len(DATA) == 24, len(DATA)   # the design's twenty-four
for k, row in DATA.items():
    assert 'value' in row and 'settings' in row and 'source' in row and len(row['settings']) >= 1, k

# ===== F0: THE COMMISSION (Num 27:12-23 — the callee) ======================================================
def the_commission(case, data):
    del P[:]
    ask = case['ask']
    if ask == 'the_mountain':
        ink('Num 27:12', '"go up to this mountain of Abarim and see the land" — "the mountain of Abarim" %s (27:12; 33:47-48; Deuteronomy 32:49 with Nebo named); "and see the land" %s; "Mount Nebo, the top of Pisgah" %s' % (ABARIM_MOUNTAIN, SEE_THE_LAND, NEBO_PISGAH))
        dat('the row the_commission: one mountain, three names — %s' % data['the_commission']['value']['mountain_names'])
        return out("the mountain of Abarim (27:12) — Nebo and Pisgah its other names (34:1 one mountain): Deuteronomy 3:27's Pisgah the retelling of this command, READ BACK", ['accepted'])
    if ask == 'the_sentence_cited':
        ink('Num 27:14', '"as you rebelled against My word in the wilderness of Zin … the waters of Meribah of Kadesh" — %s (27:14; Deuteronomy 32:51): an INTERNAL pointer to 20:12\'s sentence' % MERIBAH_KADESH)
        move('cold_run_chukat (CALL) — CK.meribah(sentence) = %s' % CK_SENTENCE[0][:70], "the barred_from_the_land entry on Moses OPEN since (40, 1, 1) — read, not rewritten; Aaron's closed at 20:28")
        return out("Meribah cited (27:14) — 20:12's sentence pointed to, the barred entry on Moses OPEN read (CK by CALL); no second write", ['accepted'])
    if ask == 'the_shepherd':
        ink('Num 27:15-17', '"let the LORD, the God of the spirits of all flesh, appoint a man over the congregation … that the congregation of the LORD be not as sheep which have no shepherd" — "the God of the spirits of all flesh" %s (16:22 Korach\'s day and here); "go out … come in" %s; "as sheep without a shepherd" %s' % (SPIRITS_ALL_FLESH, GO_OUT_COME_IN, SHEEP_NO_SHEPHERD))
        move('Sanhedrin 17a:10 (credited at THE TENT); Sifrei Bamidbar 138', "Eldad and Medad's prophecy — Moses will die and Joshua will bring Israel in; the successor asked before he is named")
        return out("a shepherd asked (27:15-17) — plea_made on Moses: the successor asked before he is named; 16:22's phrase at its second seat", ['plea_made'])
    if ask == 'the_hand_laid':
        ink('Num 27:18, 23', '"lay your HAND upon him" (27:18) — %s; "and he laid his HANDS upon him" (27:23) — %s: one commanded, two laid; "a man in whom is spirit" %s' % (HAND_SG, HANDS_PL, MAN_WITH_SPIRIT))
        move('Sifrei Bamidbar 141 (credited at THE TENT); Sanhedrin 13b-14a the ordination', "one hand commanded, two hands laid — with a generous eye; the ordination's form for the generations")
        dat('the row the_commission: hands %s' % (data['the_commission']['value']['hands'],))
        return out("the hand laid (27:18, 23) — one hand commanded, two laid (the Sifrei 141): invested_office on Joshua, the ordination's form", ['invested_office'])
    if ask == 'the_honor':
        ink('Num 27:20', '"and you shall put of your honor upon him" — %s one seat' % OF_YOUR_HONOR)
        move('Bava Batra 75a:8', "of your honor and not all your honor — the elders of that generation said: Moses' face as the sun, Joshua's as the moon")
        dat('the row the_commission: the_honor')
        return out("of your honor (27:20) — not all of it: the sun and the moon (Bava Batra 75a:8) — DATA", ['accepted'])
    if ask == 'the_urim':
        ink('Num 27:21', '"he shall stand before Eleazar the priest, who shall inquire for him by the judgment of the Urim" — %s one seat; "at his word they shall go out and come in" %s; "before Eleazar the priest" %s' % (JUDGMENT_URIM, AT_HIS_WORD, BEFORE_ELEAZAR))
        move('cold_run_second_census (CALL) — C2.DATA[urim_judgment] = %s' % C2.DATA['urim_judgment']['value'], "a prophet's decree may be retracted, the Urim's not (Yoma 73b:3); the lot's mouth is the Urim's (Bava Batra 122a:3)")
        return out("the judgment of the Urim (27:21) — final (C2 by CALL: Yoma 73b:3); Joshua under Eleazar's inquiry, not Moses' face to face", ['accepted'])
    if ask == 'the_receipt':
        ink('Num 27:22-23', '"and Moses did as the LORD commanded him" — %s one seat; "as the LORD spoke by the hand of Moses" — "by the hand of Moses" %d Bible seats: THE RECEIPT, the spec/run pair\'s form (CB8\'s)' % (DID_AS_COMMANDED, len(BY_HAND_MOSES)))
        dat('the commission\'s debit on Moses CLOSED by its run (closed_by "Num 27:22-23") — the register seat Num 27:22 CLOSE')
        return out("the receipt (27:22-23) — 'as the LORD commanded him': the commission's debit closed by its run, the register seat Num 27:22 CLOSE", ['accepted'])
    if ask == 'the_debit':
        ink('Num 27:12-13', '"see the land … and when you have seen it, you also shall be gathered" — "as Aaron your brother was gathered" %s' % GATHERED_AS_AARON)
        dat('commanded on moses valued see_the_land_from_abarim — OPEN BY DESIGN to Deuteronomy 34:1-4 (this book\'s own end); 3:27 its retelling READ BACK, no second write')
        return out("the debit (27:12) — see the land from Abarim: commanded on Moses, OPEN to Deuteronomy 34:1-4; 3:27 reads it back with Pisgah", ['commanded'])
    return out('no verdict in span', [FX.NONE])


# ===== F1: THE FRAME (Deut 1:1-5) ===========================================================================
def the_frame(case, data):
    del P[:]
    ask = case['ask']
    if ask == 'the_words':
        ink('1:1', '"these are the words which Moses spoke to all Israel beyond the Jordan …" — "these are the words" %s; the verse %d tokens, the eleven names of places' % (THESE_WORDS, len(words(1, 1))))
        move('Sifrei Devarim 1; Onkelos 1:1', "the places as the rebuke's sins — Onkelos writes them INTO the verse (thirty-three tokens for twenty-two)")
        move('Berakhot 32a:7; Sanhedrin 102a:14', "'and Di-zahab' — the school of R. Yannai: no such place; the gold lavished until they said 'enough' made the calf")
        dat('the row the_frame: %s' % data['the_frame']['value']['places'])
        return out("the words (1:1) — the eleven places the rebuke's sins (the Sifrei 1; Onkelos writes them in); Di-zahab the calf's gold (Berakhot 32a:7): the frame's DATA", ['accepted'])
    if ask == 'the_date':
        ink('1:3', '"in the fortieth year, in the eleventh month, on the first of the month" — the NUMBER reader %s; "in the fortieth year" %s ONE seat (33:38 says "of the going out"); "in the eleventh month" %s' % (SPEECH_DATE, FORTIETH_YEAR, ELEVENTH_MONTH))
        move('cold_run_journeys (CALL) — JO.aarons_death_retold(verbal_analogy) = %s' % JO_ANALOGY[0][:90], "Rosh Hashanah 2b:11 — 'the fortieth year' / 'the fortieth year': the bare date the exodus's; THE TRANSFER TAUGHT; the era's new year Nisan (JO the_era_new_year)")
        dat('the row the_date: %s — one clock, two readers; the marker at the tape position Deut 1:1' % data['the_date']['value'])
        return out("the date (1:3) — [40, 11, 1] by the number reader; the era the exodus's by the taught verbal analogy with 33:38 (Rosh Hashanah 2b:11; JO by CALL): the FORWARD marker at Deut 1:1", ['accepted'])
    if ask == 'the_receipt_of_the_rules':
        ink('1:3', '"Moses spoke to the children of Israel according to all that the LORD had commanded him to them" — "according to all that the LORD commanded him" %s (Exodus 40:16 the erection\'s receipt and this); the second form %s' % (ACCORDING_ALL_HIM, ACCORDING_ALL))
        move('Sifrei Devarim 2:8', "'according to all that the LORD commanded him' — the hermeneutic rules themselves: the receipt of the whole book's rules")
        dat('the register seat Deut 1:3 declared ACT — the speech line\'s write (torah_expounded) carries its source; the run of every relayed command, closing nothing by itself')
        return out("the receipt of the rules (1:3) — 'according to all' the hermeneutic rules (the Sifrei 2:8): the register seat ACT, the frame the readback checkpoint reads", ['accepted'])
    if ask == 'the_eleven_days':
        ink('1:2', '"eleven days from Horeb by the way of Mount Seir to Kadesh-barnea" — %s; the parser [%d]' % (ELEVEN_HOREB, ELEVEN_DAYS))
        move('Sifrei Devarim 2:1-3', "eleven days' journey done in three — the Presence hastened them; the rebuke's measure")
        return out("eleven days (1:2) — [11] by the parser; the journey hastened (the Sifrei 2:1-3): the rebuke's measure", ['accepted'])
    if ask == 'after_sihon':
        ink('1:4', '"after he had smitten Sihon king of the Amorites … and Og king of Bashan" — %s one seat; "Og king of Bashan" %d Bible seats' % (AFTER_SIHON, len(OG_BASHAN)))
        move('cold_run_journeys (CALL) — JO.aarons_death_retold(the_order) = %s' % JO_ORDER[0][:80], "Rosh Hashanah 2b:13, 3a:12 — Aaron's death before the speech by 'after he had smitten Sihon'; the fortieth year's order on the tape")
        return out("after Sihon (1:4) — the order of the fortieth year: Aaron's death, Arad, the departure, Sihon, the speech (JO by CALL; Rosh Hashanah 2b:13)", ['accepted'])
    if ask == 'began_to_expound':
        ink('1:5', '"beyond the Jordan, in the land of Moab, Moses undertook to expound this Torah" — %s one seat; the expound-root\'s Torah seats %s' % (EXPOUND, EXPOUND_LEMMA))
        move('Sotah 35b:6; Zevachim 115b:17; Mishnah Sotah 7:8', "'expound' with 27:8's 'clearly' — the seventy languages; R. Akiva: the third teaching in the plains of Moab; the king reads from 'these are the words'")
        return out("began to expound (1:5) — the expound-root's two Torah seats (27:8's 'clearly' the other); the third teaching (Zevachim 115b:17); the king's reading (Sotah 7:8)", ['accepted'])
    if ask == 'the_write':
        ink('1:1-5', 'the frame — the book\'s one act of its own day')
        dat('torah_expounded on israel_people — a STATUS dated (40, 11, 1) by the forward marker; everything after it in chapters 1-3 read back or supplied at its own time (R6)')
        return out("the write (1:1-5) — torah_expounded on Israel at (40, 11, 1): the book's one act of its own day", ['torah_expounded'])
    return out('no verdict in span', [FX.NONE])


# ===== F2: THE OFFICERS AND THE JUDGES (Deut 1:6-18) ========================================================
def the_officers_and_the_judges(case, data):
    del P[:]
    ask = case['ask']
    if ask == 'the_horeb_command':
        ink('1:6-8', '"you have dwelt long enough in this mountain; turn and take your journey … go in and possess" — "enough for you" %s (the plural\'s eight seats: Horeb, Seir, the tribes, Korach\'s two); "turn and journey" %s (14:25\'s pair); "go in and possess" %s' % (ENOUGH_PL, TURN_JOURNEY, GO_POSSESS))
        move('cold_run_erection (CALL) — ER.presence(horev_plene) = %s; cold_run_beha (CALL) — BH.march(date) = %s' % (ER_HOREB['v'], BH_DATE[0][:40]), "Exodus 33:1's 'depart, go up hence' the command's kin; 10:11's (2, 2, 20) the departure's day — the retrograde marker at 1:6")
        dat('the row the_horeb_command: %s — the supplied debit journey_to_the_mountain_of_the_amorite CLOSED at once by the prior run Num 12:16' % data['the_horeb_command']['value']['closed_by'])
        return out("the Horeb command (1:6-8) — told only here: commanded on Israel dated (2, 2, 20), CLOSED by the prior run Num 12:16 (the arrival in Paran); 'go in and possess' a reference to the land granted (Genesis 15:18)", ['commanded'])
    if ask == 'the_regions':
        ink('1:7', '"the hill country of the Amorites … the Arabah, the hill country, the lowland, the Negev, the seashore, the land of the Canaanites and Lebanon, as far as the great river, the river Euphrates"')
        move('Bava Kamma 81b:6; Shevuot 47b:6; cold_run_borders (CALL) — BO.DATA[the_promised_extents] = %s' % BO.DATA['the_promised_extents']['value'], "every tribe's portion held some of each kind (Joshua's ten conditions); the Euphrates called great because near the land; the four promised extents observed")
        dat('the row the_horeb_command: regions %s' % data['the_horeb_command']['value']['regions'])
        return out("the regions (1:7) — the seven kinds every tribe's portion held (Bava Kamma 81b:6); the Euphrates great by nearness (Shevuot 47b:6); the promised extents by CALL: DATA", ['accepted'])
    if ask == 'the_burden':
        ink('1:9-12', '"I am not able to bear you myself alone … how can I myself alone bear your cumbrance and your burden and your strife" — "your burden" %s one seat; 11:14\'s "I alone" the same word' % YOUR_BURDEN)
        move('cold_run_beha (CALL) — BH.seventy_elders(sanhedrin) = %s' % BH_SANH[0], "11:14's burden and 11:16's seventy — the seventy-one with Moses over them (Sanhedrin 2a:13; 16b:18); 'they shall bear the burden of the people WITH you' (11:17) — like you (17a:3)")
        return out("the burden (1:9-12) — 11:14's 'I alone' retold; the seventy with Moses the seventy-one (BH by CALL; Sanhedrin 16b:18, 17a:3)", ['accepted'])
    if ask == 'the_blessing':
        ink('1:11', '"may the LORD, the God of your fathers, add to you a thousand times" — %s one seat; the parser [%d]' % (THOUSAND_TIMES, THOUSAND_FOLD))
        move('Sifrei Devarim 11:1; Rosh Hashanah 28b:10', "Moses' own blessing beside God's (which has no bound); a priest may not add this blessing of his own to the priestly blessing")
        dat('the row the_officers_table: the_blessing')
        return out("the blessing (1:11) — [1000]: Moses' own beside God's (the Sifrei 11:1); a priest may not add it (Rosh Hashanah 28b:10): DATA", ['accepted'])
    if ask == 'the_qualities':
        ink('1:13, 15', '"wise and discerning and known" %s ONE seat; "wise and known" %s ONE seat — the discerning not found' % (WISE_DISC_KNOWN, WISE_KNOWN))
        move('Sifrei Devarim 15:2; Eruvin 100b:18; Nedarim 20b:10; Sanhedrin 17a:21-22', "seven sought, three found; the generation's sons; the Great Sanhedrin's men of stature and seventy languages; the creeping thing rendered pure")
        dat('the row the_seven_qualities: asked %d, found %d' % (data['the_seven_qualities']['value']['asked'], data['the_seven_qualities']['value']['found']))
        return out("the qualities (1:13, 15) — seven asked, three found (the Sifrei 15:2): the discerning not found (Eruvin 100b:18); Jethro's four by CALL: a DATA checklist", ['accepted'])
    if ask == 'the_grains':
        ink('1:15', '"captains of thousands, captains of hundreds, captains of fifties and captains of tens, and officers for your tribes" — the parser %s with "thousands" a NOUN; "captains of thousands" %s (Exodus 18:21, 25 and the kings\' seats); "and officers for your tribes" %s' % (GRAINS, CAPT_THOUSANDS, OFFICERS_TRIBES))
        move('cold_run_exodus_story (CALL) — ES.jethro(denominations) = %s' % ES_DENOM['v'], "the four grains of 18:21 — the appointment a REFERENCE to judges_appointed (Exodus 18:25), TURNED")
        dat('the row the_officers_table: grains %s' % data['the_officers_table']['value']['grains'])
        return out("the grains (1:15) — [100, 50, 10] with the plural 'thousands' a noun: the four grains of Exodus 18:21 by CALL; the appointment read back, TURNED", ['accepted'])
    if ask == 'the_count':
        move('cold_run_exodus_story (CALL) — ES.jethro(judges) = %d; cold_run_bamidbar (CALL) — CB.census(total) = %s' % (ES_JUDGES['v'], CB_TOTAL[0]), "78,600 on the round six hundred thousand (Sanhedrin 18a:3); 79,064 on the exact 603,550 by integer division at every grain (the Sifrei 15:4's rounding rule)")
        move('cold_run_balak (CALL) — BK.peor(judges_count) = %s' % BK_JUDGES[0][:60], "the Jerusalem Talmud Sanhedrin 10:2's arithmetic — each executing two = 157,200")
        dat('the row the_officers_table: round %d, exact %d' % (data['the_officers_table']['value']['count_round'], data['the_officers_table']['value']['count_exact']))
        return out("the count — 78,600 on the round six hundred thousand (ES by CALL; Sanhedrin 18a), 79,064 on the census's exact 603,550 by integer division (CB by CALL; the Sifrei 15:4's rounding rule): two settings", ['accepted'])
    if ask == 'the_officers':
        ink('1:15', '"and officers for your tribes" — %s one seat; "and officers" %s — Deuteronomy 16:18 the second seat' % (OFFICERS_TRIBES, AND_OFFICERS))
        move('Sifrei Devarim 15:5; Sanhedrin 16b:9-10; 2 Chronicles 19:11', "the officers with the strap — the Levites; 'judges and officers in all your gates for your tribes' (16:18): judges for Israel, for every tribe, for every city — THE OFFICERS' TABLE's other seat")
        return out("the officers (1:15) — the strap (the Sifrei 15:5; 2 Chronicles 19:11); Deuteronomy 16:18's second seat — every tribe, every city (Sanhedrin 16b:9-10)", ['accepted'])
    if ask == 'the_charge':
        ink('1:16-17', 'the six clauses — "hear between your brothers" %s, "judge righteously" %s, "no faces in judgment" %s, "the small as the great" %s, "not afraid of any man" %s, "the judgment is God\'s" %s, "the hard matter" %s: each ONE seat' % (HEAR_BROTHERS, JUDGE_RIGHT, NO_FACES, SMALL_GREAT, NOT_AFRAID, JUDGMENT_GODS, HARD_MATTER))
        dat('judges_charged on the-court — the six clauses %s, dated (1, 2, 16) by the court\'s founding day read off Israel\'s ledger (the retrograde marker at 1:9); THE LAW of the span in Moses\' voice with no divine frame' % data['the_judges_charge']['value'])
        return out("the charge (1:16-17) — the six clauses each one seat: judges_charged on the court, dated at the court's founding (1, 2, 16); the law in Moses' voice, the vows' class", ['judges_charged'])
    if ask == 'hear':
        ink('1:16', '"and I charged your judges at that time, saying: hear between your brothers" — "hear" the infinitive absolute')
        move('Sanhedrin 7b:14 (R. Chanina)', "a judge may not hear one litigant before the other comes; 'charged' — with alacrity, the rod and the strap (7b:14-15)")
        return out("hear (1:16) — not one litigant without the other (Sanhedrin 7b:14); 'charged' with alacrity, the rod and the strap", ['accepted'])
    if ask == 'judge_righteously':
        ink('1:16', '"and judge righteously between a man and his brother and his stranger" — %s one seat' % JUDGE_RIGHT)
        move('Sanhedrin 7a:17 (R. Yonatan); Leviticus 19:15 by CALL — HO.conduct(judge_is_measurer) = %s' % HO_MEASURER['v'], "the true judgment truly makes the Presence rest in Israel; 'in righteousness you shall judge' the holiness engine's clause")
        return out("judge righteously (1:16) — the true judgment truly makes the Presence rest (Sanhedrin 7a:17); Leviticus 19:15's 'in righteousness' by CALL", ['accepted'])
    if ask == 'no_faces':
        ink('1:17', '"you shall not respect persons in judgment" — %s one seat; "respect persons" (takiru) %s' % (NO_FACES, RESPECT_FACES))
        move('Sanhedrin 7b:18 (R. Yehuda / R. Elazar); Sifrei Devarim 17:1', "do not befriend the litigant / do not estrange him — a DISPUTE row; the appointer addressed")
        move('Mishnah Sanhedrin 3:4-5; Sanhedrin 27b:10-29a:12; Numbers 35:23 by CALL — RF.DATA[the_court_of_twenty_three]', "the kin and the haters off the bench — 'not his enemy nor seeking his harm': the witness disputed, the JUDGE agreed (29a:11)")
        return out("no faces (1:17) — befriend / estrange disputed (Sanhedrin 7b:18); the kin and the haters off the bench (Mishnah Sanhedrin 3:4-5; 29a:11): the DATA row no_faces", ['accepted'])
    if ask == 'small_and_great':
        ink('1:17', '"you shall hear the small and the great alike" — %s one seat' % SMALL_GREAT)
        move('Sanhedrin 8a:2 (Reish Lakish); 8a:4-5', "the judgment of one peruta as dear as of a hundred maneh; the case that came first heard first")
        return out("the small and the great (1:17) — the peruta as the hundred maneh (Sanhedrin 8a:2); the order of hearing (8a:4-5)", ['accepted'])
    if ask == 'no_fear':
        ink('1:17', '"you shall not be afraid of the face of any man" — %s one seat; "afraid" (taguru) the gather-root' % NOT_AFRAID)
        move('Sanhedrin 7a:16; 6b:12 (Reish Lakish); 6b:13 (R. Yehoshua ben Korcha); Sifrei Devarim 17:4', "a term for gathering in — a judge may not hold back his words; refusal before hearing, not after; the student who sees merit for the poor not silent")
        return out("no fear (1:17) — a term for gathering in (Sanhedrin 7a:16); the refusal before hearing only (6b:12; the Sifrei 17:4); the student not silent (6b:13)", ['accepted'])
    if ask == 'the_judgment_is_gods':
        ink('1:17', '"for the judgment is God\'s" — %s one seat' % JUDGMENT_GODS)
        move('Sanhedrin 6b:3; 7a:18; 6b:14; the Rambam\'s introduction 15:58', "let the judgment pierce the mountain (Moses) against Aaron the pursuer of peace; the judge who takes from one and gives to the other — the Holy One takes his life; the judges know before Whom")
        return out("the judgment is God's (1:17) — pierce the mountain (Sanhedrin 6b:3); the unlawful judge's life (7a:18); before Whom (6b:14)", ['accepted'])
    if ask == 'the_hard_matter':
        ink('1:17', '"and the cause that is too hard for you, you shall bring to me and I will hear it" — %s, %s one seat each' % (HARD_MATTER, BRING_TO_ME))
        move('cold_run_exodus_story (CALL) — ES.jethro(hard_cases) = %s; cold_run_zelophehad (CALL) — ZL.the_daughters(halt) = %s' % (ES_HARD['v'], ZL_HALT[0][:60]), "Exodus 18:26's hard_cases_to_moses the standing status; the Sifrei 17:7 — Zelophehad's daughters, THE TENT: the third form, carried in by Moses")
        return out("the hard matter (1:17) — Exodus 18:26's status read (ES by CALL); Zelophehad's daughters the case (the Sifrei 17:7; ZL by CALL — the third form)", ['accepted'])
    if ask == 'the_stranger':
        ink('1:16', '"between a man and his brother and his stranger" — "his stranger" the convert')
        move('Yevamot 47a:7 (R. Yehuda)', "a convert converts only before a court — 'and his stranger' with 'judge righteously'; his opponent's plea heard")
        return out("the stranger (1:16) — a convert before a court (Yevamot 47a:7)", ['accepted'])
    if ask == 'a_man_excludes_the_minor':
        ink('1:16', '"between a MAN and his brother"')
        move('Sifrei Devarim 16:6', "'a man' — the minor excluded from the litigants")
        return out("a man excludes the minor (1:16 — the Sifrei 16:6)", ['accepted'])
    if ask == 'the_gentile_litigant':
        ink('1:16', '"and his stranger" — the gentile litigant on the shelf')
        dat('the row the_gentile_litigant: %s — R. Ishmael\'s two rulings against Rabban Shimon ben Gamliel (the Sifrei 16:4)' % data['the_gentile_litigant']['value'])
        return out("the gentile litigant — R. Ishmael's two rulings against Rabban Shimon ben Gamliel's one (the Sifrei 16:4): DATA", ['accepted'])
    if ask == 'the_appointer':
        ink('1:17', '"you shall not respect persons" — addressed to the one who appoints judges')
        move('Sifrei Devarim 17:1', "'you shall not respect persons in judgment' — to the appointer: appoint no judge for his face; Sanhedrin 7b:16-17 the judge appointed for money")
        return out("the appointer (1:17) — the clause addressed to the one who appoints (the Sifrei 17:1): DATA", ['accepted'])
    if ask == 'the_compromise':
        ink('1:17', '"for the judgment is God\'s" — the compromise\'s clause on the shelf')
        dat('the row the_compromise: %s — R. Yehoshua ben Korcha a mitzva, R. Eliezer son of R. Yosei HaGelili forbidden once heard, R. Shimon ben Menasya before the verdict leans; "justice, justice" one for judgment, one for compromise (Sanhedrin 6b:1-15; 32b:4-6)' % data['the_compromise']['value'])
        return out("the compromise — three settings on 1:17's clause (Sanhedrin 6b:1-15; 32b:4-6): TWO VERDICT TABLES as DATA", ['accepted'])
    if ask == 'the_al_tikrei':
        ink('1:13', '"and I will set them as your heads" (ואשימם)')
        move('Sifrei Devarim 13:6', "'I will set them' read 'their guilt' (ashmam) on your heads — THE REVOCALIZATION (MOVE_CATALOG's move): the appointer bears the judges' guilt")
        return out("the al tikrei (1:13) — 'I will set them' read 'their guilt on your heads' (the Sifrei 13:6): the revocalization move", ['accepted'])
    if ask == 'be_deliberate':
        move('Pirkei Avot 1:1; Sifrei Devarim 16:1; cold_run_erection (CALL) — ER.presence(sheet_avot_1_1) = %s' % ER_AVOT['v'], "'be deliberate in judgment' — the Sifrei cites the Mishnah as the verse's reading; the chain from Moses to Joshua the erection engine's row")
        return out("be deliberate (Avot 1:1) — the Sifrei 16:1 cites the Mishnah as 1:16's reading; the chain by CALL", ['accepted'])
    if ask == 'money_and_capital':
        move('Mishnah Sanhedrin 4:1; Sanhedrin 32a:1-10; cold_run_ordinances (CALL) — OR.courts(one_vs_two) = %s, (asymmetry) = %s, (twenty_three) = %d' % (OR_ONE_TWO['v'], OR_ASYM['v'], OR_23['v']), "'one manner of law' (Leviticus 24:22); the ten differences — three against twenty-three, one against two, reversal, who may argue, day and night, the same day or the morrow, from the side (1:17's 'the small and the great' the eighth's ground), the fit of lineage; the Sifrei 18:1")
        return out("money and capital (Mishnah Sanhedrin 4:1) — the ten differences (Sanhedrin 32a; the Sifrei 18:1); the majority's asymmetry by CALL", ['accepted'])
    if ask == 'the_court_of_three':
        move('Mishnah Sanhedrin 1:1-3, 3:1-3; Sanhedrin 2a-2b, 23a-26b; cold_run_exodus_story (CALL) — ES.jethro(sanhedrin_sizes) = %s' % (ES_SIZES['v'],), "money cases by three; the litigants' choice — this one chooses one, that one chooses one, the two choose a third (R. Zeira: so the judgment goes out true); the disqualified by conduct — the dice-player, the lender at interest, the pigeon-flyer, the Sabbatical merchant; the proclamation")
        return out("the court of three (Mishnah Sanhedrin 1:1, 3:1-3) — the litigants' choice, the third by the two (Sanhedrin 23a:12); the disqualified by conduct (24b-26b); the sizes by CALL", ['accepted'])
    if ask == 'the_perverting_judge':
        move('cold_run_holiness (CALL) — HO.conduct(five_effects) = %s' % HO_FIVE['v'], "Leviticus 19:15's 'do no wrong in judgment' — the judge who perverts defiles the land, profanes the Name, removes the Presence, fells by the sword, exiles (the Sifra); Sanhedrin 7a:17-18 the Presence removed, the life taken")
        return out("the perverting judge — the five effects (HO by CALL; Sanhedrin 7a:17-18): judgment_perverted", ['judgment_perverted'])
    if ask == 'the_refusal_before_hearing':
        move('Sanhedrin 6b:12 (Reish Lakish); 6b:11 (R. Shimon ben Menasya)', "before hearing the litigants' statements, or after hearing but before knowing where the judgment leans, a judge may refuse to judge — 'you shall not be afraid' (1:17) binds him only after")
        return out("the refusal before hearing — permitted, not yet bound by 'you shall not be afraid' (Sanhedrin 6b:12): exempt", ['exempt'])
    if ask == 'all_the_things':
        ink('1:18', '"and I commanded you at that time all the things that you should do"')
        move('Sanhedrin 8a:6 (credited at Beha\'alotcha)', "'I charged your judges' (1:16) and 'I commanded you' (1:18) — the judges warned to bear the community, the community warned to bear the judges' burden")
        return out("all the things (1:18) — the community warned as the judges were (Sanhedrin 8a:6)", ['accepted'])
    return out('no verdict in span', [FX.NONE])


# ===== F3: THE SPIES READ BACK (Deut 1:19-46) ===============================================================
def the_spies_read_back(case, data):
    del P[:]
    ask = case['ask']
    if ask == 'the_asking':
        ink('1:22', '"you came near to me, all of you, and said: let us send men before us, that they may search the land for us" — %s, %s one seat each' % (LET_US_SEND, SEARCH_FOR_US))
        move('cold_run_shelach (CALL) — SL.spies(send_for_yourself) = %s' % SL_SEND[0][:70], "Sotah 34b:3 — 'send for yourself' at Moses' discretion; the people asked; 34b:4 'that they may search' with the moon's embarrassment")
        dat('the row the_spies_asked: %s' % data['the_spies_asked']['value'])
        return out("the asking (1:22) — the people's, against 13:2's 'send for yourself' (Sotah 34b:3; SL by CALL): the two tellings reconciled on the shelf — the readback row TURNED", ['accepted'])
    if ask == 'the_twelve':
        ink('1:23', '"I took twelve men of you, one man for a tribe" — the parser %s; "twelve men" %s; "one man for a tribe" %s' % (TWELVE_ONE, TWELVE_MEN, ONE_PER_TRIBE))
        move('cold_run_shelach (CALL) — SL.spies(one_per_tribe)', "13:2's one man per tribe, princes; Levi absent; Joshua's crossing the phrases' other seats")
        return out("the twelve (1:23) — [12, 1]: one per tribe by CALL; Joshua 4:2 and 3:12 the phrases' other seats", ['accepted'])
    if ask == 'the_valley':
        ink('1:24', '"they came to the valley of Eshcol and spied it out" — %s (13:23 and this); "spied" the spy-root\'s piel %s — Caleb\'s verb, not 13:2\'s tour' % (ESHCOL, SPY_ROOT))
        move('cold_run_shelach (CALL) — SL.spies(eshcol) = %s; cold_run_chukat (CALL) — CK.DATA[spy_verb] = %s' % (SL_ESHCOL[0], CK.DATA['spy_verb']['value']), "named after the cluster (13:24); the spy-verb Caleb's (Joshua 14:7) at Jazer (21:32)")
        return out("the valley (1:24) — Eshcol named after the cluster (SL by CALL); 'spied' the piel — Caleb's verb (Joshua 14:7; CK.DATA spy_verb by CALL)", ['accepted'])
    if ask == 'good_is_the_land':
        ink('1:25', '"they brought us word and said: good is the land which the LORD our God gives us" — %s: this and Numbers 14:7 — JOSHUA AND CALEB\'S words' % GOOD_LAND_IS)
        move('Sifrei Devarim 23:3; Sotah 35a:2', "the spies' own words 'good is the land' — 14:7's in their mouths; 13:27's 'however' dropped: the lie with a grain of truth")
        return out("good is the land (1:25) — 14:7's words, Joshua and Caleb's (the Sifrei 23:3); the retelling keeps the truth, drops 13:27's 'however' (Sotah 35a:2): SHORTENED", ['accepted'])
    if ask == 'the_murmuring':
        ink('1:27-28', '"you murmured in your tents … the LORD hates us … our brothers have melted our heart, saying: a people greater and taller than we, cities great and fortified to heaven, the sons of the Anakim" — %s, %s, %s, %s one seat each; "the sons of the Anakim" %s' % (MURMURED_TENTS, HATES_US, MELTED_HEART, GREATER_TALLER, SONS_ANAKIM))
        move('Shevuot 47b:5 (credited); cold_run_shelach (CALL) — SL.spies(stronger_than) = %s' % SL_STRONGER[0][:60], "'you murmured' as two words — you explored and disparaged; 13:31's 'stronger than us' read 'than Him' — the retelling keeps the plain sense; the Sifrei 25:4's hyperbole 'to heaven'")
        return out("the murmuring (1:27-28) — two words (Shevuot 47b:5); the spies' words in the people's mouths, 'greater and taller than we' the plain sense of 13:31 (Sotah 35a:7): TURNED", ['accepted'])
    if ask == 'the_carrying':
        ink('1:31', '"the LORD your God carried you, as a man carries his son" — %s one seat' % CARRIES_SON)
        move('Sifrei Devarim 314:2 (by position, forward); Exodus 19:4', "'as on eagles' wings' — the eagle's carrying; the son carried")
        return out("the carrying (1:31) — as a man carries his son: Exodus 19:4's eagle the kin", ['accepted'])
    if ask == 'the_pillar':
        ink('1:33', '"who goes before you in the way … in fire by night and in the cloud by day" — %s, %s one seat each' % (FIRE_NIGHT, CLOUD_DAY))
        move('Exodus 13:21 by REFERENCE (the exodus story\'s pillar_set line, no cell)', "the pillar of cloud by day and of fire by night — the tape's line at Exodus 13:21-22; the pesach runner's by_day ask the token's seat")
        return out("the pillar (1:33) — Exodus 13:21's by REFERENCE: the tape's pillar_set line, read", ['accepted'])
    if ask == 'the_oath':
        ink('1:34-36', '"the LORD heard the voice of your words and was angry and SWORE: not one of these men, this evil generation, shall see the good land … save Caleb son of Jephunneh, he shall see it … because he wholly followed the LORD" — %s, %s, %s; "he wholly followed the LORD" %s (Joshua 14:14 the payment\'s seat)' % (EVIL_GENERATION, SAVE_CALEB, THE_GOOD_LAND[:3], WHOLLY_FOLLOWED))
        move('cold_run_gad_reuben (CALL) — GR.DATA[the_oath_supplied] = %s; cold_run_shelach (CALL) — SL.decree(exceptions) = %s; SL.decree(caleb_entitlement) = %s' % (GR.DATA['the_oath_supplied']['value'], SL_EXC[0], SL_CALEB[0][:40]), "the oath's verb supplied by the retelling (32:10 the first); Caleb's holding_owed OPEN — paid at Joshua 14:13-14 outside the Torah")
        return out("the oath (1:34-36) — the verb 'swore' supplied (GR.DATA by CALL); sentence_pronounced read; Caleb's holding_owed OPEN read (SL by CALL): SHORTENED", ['accepted'])
    if ask == 'the_exceptions':
        move('cold_run_shelach (CALL) — SL.decree(exceptions) = %s' % SL_EXC[0], "Caleb and Joshua (14:24, 14:30) and the children brought in (14:31) — exempt from the oath; 1:36, 1:38, 1:39 retell the three")
        return out("the exceptions — Caleb, Joshua, the children (SL by CALL): exempt from the oath", ['exempt'])
    if ask == 'the_bars_ground':
        ink('1:37', '"the LORD was angry with me for your sakes, saying: you also shall not go in there" — %s, %s one seat each' % (ANGRY_FOR_YOU, NOT_GO_IN))
        move('cold_run_chukat (CALL) — CK.meribah(sentence) = %s' % CK_SENTENCE[0][:60], "20:12's 'because you did not believe in Me' — the tape's one entry; Psalm 106:32's 'for their sakes' outside the Torah, read, not run")
        dat('the row the_bars_ground: %s — no teacher joins the two grounds: an OPEN row (R4)' % data['the_bars_ground']['value'])
        return out("the bar's ground (1:37) — 'for your sakes' against 20:12's 'because you did not believe': DISAGREES, an OPEN row; the tape's one entry stands", ['accepted'])
    if ask == 'joshua_shall_go_in':
        ink('1:38', '"Joshua son of Nun who stands before you, he shall go in there; strengthen him, for he shall cause Israel to inherit it" — %s, %s one seat each: the effect\'s FIRST seat (3:28 the second)' % (HE_SHALL_GO, CAUSE_ISRAEL_INHERIT))
        move('cold_run_gad_reuben (CALL) — GR.the_rebuke(joshua_nothing_owed)', "Joshua excepted (14:30) and nothing owed him in the ink — Sotah 35a:4; Timnath-serah by the LORD's word")
        return out("Joshua shall go in (1:38) — 14:30's exception EXPANDED with the inheriting (the effect's first seat; 3:28 and Joshua 1:6 after)", ['accepted'])
    if ask == 'the_little_ones':
        ink('1:39', '"your little ones who you said would be a prey" — %s: 14:31 VERBATIM (the shared prefix %d tokens computed); "good and evil" %s — Eden\'s four seats and this' % (LITTLE_ONES_PREY, VERBATIM_PREFIX, GOOD_EVIL))
        move('Sifrei Devarim 25 (by position); Genesis 2:9, 17; 3:5, 22', "the children who know not good and evil — Eden's phrase; the exception's ground")
        return out("the little ones (1:39) — 14:31 VERBATIM for five tokens, then the children who know not good and evil added (Eden's four seats)", ['accepted'])
    if ask == 'the_turn_back':
        ink('1:40', '"and you, turn and take your journey into the wilderness by the way of the Red Sea" — "the way of the Red Sea" %s: the command (14:25), its run (21:4), both retold (1:40, 2:1)' % RED_SEA_WAY)
        move('cold_run_shelach (CALL) — SL.decree(turn_back) = %s' % SL_TURN[0][:70], "14:25's debit CLOSED at 21:4 (CF8) — read at the checkpoint, not rewritten")
        return out("the turn back (1:40) — 14:25 retold with 'tomorrow' dropped; the debit's close at 21:4 read (SL by CALL): TURNED", ['accepted'])
    if ask == 'the_presumption':
        ink('1:41-44', '"we have sinned … we will go up and fight, according to all that the LORD our God commanded us … you were presumptuous and went up … the Amorite chased you as bees do and beat you down in Seir to Hormah" — %s, %s, %s, %s, %s' % (WE_HAVE_SINNED[:2], GO_UP_FIGHT, PRESUMPTUOUS, AS_BEES, TO_HORMAH))
        move('cold_run_shelach (CALL) — SL.decree(presumption) = %s; SL.decree(hormah) = %s' % (SL_PRESUME[0][:50], SL_HORMAH[0][:50]), "presumed — the ark and Moses stayed; Hormah the proleptic name")
        dat('the receipt "as the LORD commanded us" in the PEOPLE\'S mouth refused by 1:42-43 — a RUN CITATION (R5): the register seat Deut 1:41 NONE')
        return out("the presumption (1:41-44) — presumed_to_go_up and defeated read back; 'as bees do', 'in Seir' EXPANDED; the receipt in the people's mouth a run citation (1:41 NONE)", ['accepted'])
    if ask == 'the_weeping':
        ink('1:45', '"you returned and wept before the LORD; the LORD did not hear your voice nor give ear" — %s, %s one seat each; 3:26\'s "did not hear me" the same phrase' % (WEPT_BEFORE, NOT_HEAR_VOICE))
        move('cold_run_shelach (CALL) — SL.decree(that_night) = %s' % SL_NIGHT[0][:60], "14:1's weeping the night of the Ninth of Av — a weeping for generations; the second weeping told only here, unheard")
        return out("the weeping (1:45) — a second weeping told only here, unheard (1:45 and 3:26 one phrase); 14:1's wept read: EXPANDED, no write", ['accepted'])
    if ask == 'many_days_at_kadesh':
        ink('1:46', '"you abode in Kadesh many days, according to the days that you abode" — %s one seat' % KADESH_DAYS)
        move('Seder Olam Rabbah 8 (the shelf\'s export); Sifrei Devarim 28:1', "nineteen years at Kadesh, nineteen wandering — the days as the days: DATA")
        return out("many days at Kadesh (1:46) — Seder Olam 8's nineteen years: DATA, no day moved", ['accepted'])
    if ask == 'the_readback_table':
        dat('the row the_readback: %d rows — %s' % (len(data['the_readback']['value']), dict(RB_GRADES)))
        return out("the readback table — forty-two reference rows graded; the two DISAGREES rows open; every retold act's entry found on the running world (CA4)", ['accepted'])
    return out('no verdict in span', [FX.NONE])


# ===== F4: THE BYPASS (Deut 2:1-25) =========================================================================
def the_bypass(case, data):
    del P[:]
    ask = case['ask']
    if ask == 'the_turn':
        ink('2:1-3', '"we turned and journeyed by the way of the Red Sea … we compassed Mount Seir many days; the LORD said to me: you have compassed this mountain long enough; turn you northward" — %s, %s, %s one seat each' % (COMPASSED_SEIR, LONG_ENOUGH_MOUNTAIN, TURN_NORTH))
        move('cold_run_chukat (CALL) — CK.edom_and_hor(death_dates) = %s' % CK_DATES[0][:50], "the departure from Mount Hor (40, 6, 1) — the retrograde marker's day at 2:2; the turn's debit CLOSED at once by the prior run Num 21:10-13 (the march past Moab)")
        dat('commanded on israel_people turn_northward — dated (40, 6, 1), closed by "Num 21:10-13"')
        return out("the turn (2:1-3) — told only here: commanded on Israel dated (40, 6, 1), CLOSED by the prior run Num 21:10-13; 'enough' the plural's second seat in the speech", ['commanded'])
    if ask == 'esau':
        ink('2:4-8', '"your brothers the sons of Esau who dwell in Seir … do not contend with them … not so much as for the sole of the foot … I have given Mount Seir to Esau for a possession; food you shall buy of them for money" — %s, %s, %s, %s, %s' % (BROTHERS_ESAU, NOT_CONTEND, FOOT_BREADTH, SEIR_TO_ESAU, BUY_FOOD))
        move('cold_run_joseph (CALL) — JS.edom(parted_for_room) = %s; Kiddushin 18a:2; Bava Kamma 38a:16' % JS_SEIR['v'], "Esau dwelt in Mount Seir (Genesis 36:8) — the grant standing; a gentile inherits by Torah law from this verse; the a fortiori from Midian needed the bar")
        dat('the row the_bypass_commands: edom %s' % (data['the_bypass_commands']['value']['edom'],))
        return out("Esau (2:4-8) — contending_barred and land_granted (Mount Seir) on Edom: the bar and the grant told only here (Kiddushin 18a:2; JS by CALL); the purchase a permission", ['contending_barred', 'land_granted'])
    if ask == 'forty_years_lacking_nothing':
        ink('2:7', '"these forty years the LORD your God has been with you; you have lacked nothing" — %s, %s; the parser [%d]' % (FORTY_YEARS_THESE, LACKED_NOTHING, FORTY))
        move('cold_run_exodus_story (CALL) — ES.manna(forty_years) = %d' % ES_MANNA['v'], "'the sons of Israel ate the manna forty years' (Exodus 16:35) — the provision's span by CALL")
        return out("forty years lacking nothing (2:7) — [40]: the manna's forty years (ES by CALL; Exodus 16:35)", ['accepted'])
    if ask == 'the_route':
        ink('2:8', '"we passed by our brothers the sons of Esau … from the way of the Arabah, from Elath and from Ezion-geber; we turned and passed by the way of the wilderness of Moab" — against 21:4\'s "by the way of the Red Sea"')
        move('Onkelos 2:8; cold_run_journeys (CALL) — JO.the_stations', "the route named by its stations — the Arabah, Elath, Ezion-geber (33:35-36 the itinerary's seat), the wilderness of Moab (21:11)")
        return out("the route (2:8) — Elath and Ezion-geber, the way of Moab's wilderness: the itinerary's stations by CALL; 21:4's Red Sea way the same road", ['accepted'])
    if ask == 'moab':
        ink('2:9', '"do not harass Moab nor contend with them in battle, for I will not give you of his land for a possession, because I have given Ar to the children of Lot" — %s one seat; "Ar" %s' % (HARASS_MOAB, AR_SEATS[:4]))
        move('cold_run_balak (CALL) — BK.phinehas_and_midian(midian_not_moab) = %s; cold_run_mamre (CALL) — MM.sodom(two_peoples_named) = %s; cold_run_chukat (CALL) — CK.DATA[sihon_purified] = %s' % (BK_MIDIAN[0][:50], MM_TWO['v'], CK.DATA['sihon_purified']['value']), "Moses' a fortiori from Midian needed the bar (Bava Kamma 38a:16); Moab Lot's elder daughter's; Moab's land purified through Sihon (Chullin 60b:13)")
        dat('the row the_bypass_commands: moab %s' % (data['the_bypass_commands']['value']['moab'],))
        return out("Moab (2:9) — contending_barred and land_granted (Ar) on the Moabites: the bar the a fortiori needed (Bava Kamma 38a:16; BK by CALL); Lot's elder daughter's people (MM by CALL)", ['contending_barred', 'land_granted'])
    if ask == 'harassing_permitted':
        move('Horayot 10b:19 (R. Yochanan); Nazir 23b:11', "'do not contend with Moab IN BATTLE' — battle forbidden, harassing not: the reward of the elder daughter's euphemism; Ammon not even harassed (11a:1)")
        dat('the row the_bypass_commands: the_difference — a PARAMETER of the block\'s reach')
        return out("harassing Moab — permitted, battle forbidden (Horayot 10b:19): exempt from the bar's reach; Ammon's bar reaches further", ['exempt'])
    if ask == 'the_emim':
        ink('2:10-12', '"the Emim dwelt there before … Rephaim … Anakim; the Horites dwelt in Seir before, and the sons of Esau dispossessed them … as Israel did to the land of his possession" — %s, %s (%d seats), %s (%d), %s one seat' % (EMIM, 'Rephaim', len(REPHAIM), 'Horites', len(HORITES), AS_ISRAEL_DID))
        move('cold_run_primeval (CALL) — PR.war(og) = %s; cold_run_joseph (CALL) — JS.edom (the Horites of 36:20); Chullin 60b:11' % PR_OG['v'], "Genesis 14:5-6's Rephaim, Emim and Horites at their first seats; the verses fit to be burned that are the Torah's body")
        dat('the row the_dispossessions: %s' % data['the_dispossessions']['value'])
        return out("the Emim and the Horites (2:10-12) — Genesis 14:5-6's peoples (PR and JS by CALL); 'as Israel did' the ink's pattern of title: the dispossessions DATA", ['accepted'])
    if ask == 'the_zered':
        ink('2:13-14', '"rise up and get you over the brook Zered; and we went over the brook Zered; the days from Kadesh-barnea until we crossed the brook Zered — thirty-eight years, until all the generation of the men of war was consumed" — %s, %s; the parser [%d]' % (ZERED, THIRTY_EIGHT_YEARS, THIRTY_EIGHT))
        move('cold_run_chukat (CALL) — CK.well_and_kings(zered_date) = %s; cold_run_shelach (CALL) — SL.decree(count_from) = %s' % (CK_ZERED[0][:60], SL_FROM[0][:40]), "the Zered crossed after the thirty-eight years; 40 − 38 = 2 the era's year at the decree")
        dat('the row the_thirty_eight: %s — the supplied crossing CLOSED by the prior run Num 21:10-13 (21:12 the camp at Zered)' % data['the_thirty_eight']['value'])
        return out("the Zered (2:13-14) — told only here: commanded on Israel cross_the_brook_zered, CLOSED by the prior run Num 21:10-13; [38] against the tape's years (the spies' return to the departure from Mount Hor)", ['commanded'])
    if ask == 'the_men_of_war_consumed':
        ink('2:14-16', '"until all the generation of the men of war was consumed … the hand of the LORD was against them to discomfit them … when all the men of war were consumed and dead" — %s, %s, %s' % (GENERATION_CONSUMED, HAND_AGAINST, DISCOMFIT))
        move('cold_run_shelach (CALL) — SL.decree(deaths_ceased) = %s; SL.decree(due) = %s' % (SL_CEASED[0][:60], SL_DUE[0][:40]), "the carcasses timer fired at (40, 5, 9); the dying ceased the fifteenth of Av (Bava Batra 121a:9; Taanit 30b:12)")
        return out("the men of war consumed (2:14-16) — the decree's timer FIRED at (40, 5, 9) read; the dying ceased (40, 5, 15) by CALL (Taanit 30b:12)", ['accepted'])
    if ask == 'the_speech_resumed':
        ink('2:17', '"and the LORD SPOKE to me, saying" — %s: the Bible\'s ONE seat (the six "said to me" %s)' % (SPOKE_TO_ME, SAID_TO_ME))
        move('Bava Batra 121b:1 (credited); Taanit 30b:12', "the speech resumed only after the last of that generation — the fifteenth of Av")
        return out("the speech resumed (2:17) — 'SPOKE to me' the Bible's one seat: only after the last of that generation (Bava Batra 121b:1)", ['accepted'])
    if ask == 'ammon':
        ink('2:17-19', '"when you come near over against the children of Ammon, do not harass them nor contend with them, for I will not give you of the land of the children of Ammon" — "the sons of Ammon" %d Bible seats; "the land of the sons of Ammon" %s' % (len(SONS_OF_AMMON), LAND_AMMON))
        move('Bava Kamma 38b:6; Horayot 11a:1; Nazir 23b:12; cold_run_chukat (CALL) — CK.DATA[ammon_border] = %s' % CK.DATA['ammon_border']['value'], "Ammon not even harassed — the younger daughter's reward; 21:24's border STRONG, here commanded off-limits")
        dat('the row the_bypass_commands: ammon %s — the-sons-of-ammon the one NEW written-on party' % (data['the_bypass_commands']['value']['ammon'],))
        return out("Ammon (2:17-19) — contending_barred and land_granted on the sons of Ammon: not even harassed (Bava Kamma 38b:6); 21:24's strong border the bar's reason (CK.DATA by CALL); the one new party", ['contending_barred', 'land_granted'])
    if ask == 'the_avvim':
        ink('2:20-23', '"the Zamzummim … the Avvim who dwelt in villages as far as Gaza, the Caphtorim who came out of Caphtor destroyed them" — %s, %s (Genesis 10:14)' % (ZAMZUMMIM, CAPHTORIM))
        move('Chullin 60b:11 (credited); Genesis 10:14 by CALL (PR.nations)', "Reish Lakish's verses fit to be burned that are the Torah's body — the Avvim's dispossession the title's pattern")
        return out("the Avvim (2:20-23) — the Caphtorim's dispossession, Genesis 10:14's people (Chullin 60b:11): the dispossessions DATA", ['accepted'])
    if ask == 'sihon_commanded':
        ink('2:24-25', '"rise up, take your journey, and pass over the valley of Arnon; behold, I have given into your hand Sihon … begin to possess it, and contend with him in battle; this day will I begin to put the dread of you" — %s, %s, %s, %s' % (RISE_ARNON, BEGIN_POSSESS, BEGIN_DREAD, WHOLE_HEAVEN[:3]))
        move('Avodah Zarah 25a:7-9; Taanit 20a:6-8', "the sun stood still for Moses — 'I will begin' / 'I will begin' (Joshua 3:7), 'put' / 'put' (Joshua 10:12), the verse itself: DATA")
        dat('commanded on israel_people begin_to_possess_sihons_land — dated (40, 6, 1), closed by "Num 21:24-25" (the smiting and possession)')
        return out("Sihon commanded (2:24-25) — told only here: commanded on Israel, CLOSED by the prior run Num 21:24-25; the dread's row the sun for Moses (Avodah Zarah 25a; Taanit 20a): DATA", ['commanded'])
    return out('no verdict in span', [FX.NONE])


# ===== F5: SIHON AND OG (Deut 2:26-3:11) ====================================================================
def sihon_and_og(case, data):
    del P[:]
    ask = case['ask']
    if ask == 'the_messengers':
        ink('2:26-28', '"I sent messengers out of the wilderness of Kedemoth to Sihon king of Heshbon with words of peace: let me pass through your land; by the road, by the road I will go" — %s, %s, %s, %s; 2:27 %d tokens for 21:22\'s %d (computed: %d shared)' % (KEDEMOTH, WORDS_PEACE, ROAD_ROAD, NOT_TURN, len(MSG_DEUT), len(MSG_NUM), len(set(MSG_DEUT) & set(MSG_NUM))))
        move('Sifrei Devarim 199:5 (credited, forward); cold_run_chukat (CALL) — CK.edom_and_hor(two_messages)', "'words of peace' — the war's law of Deuteronomy 20:10 read here; the Edom and Sihon messages share thirteen tokens (computed at chukat)")
        return out("the messengers (2:26-28) — nine tokens for 21:22's seventeen: SHORTENED; Kedemoth and 'words of peace' told only here", ['accepted'])
    if ask == 'the_edom_disagreement':
        ink('2:29', '"as the sons of Esau who dwell in Seir did for me, and the Moabites who dwell in Ar" — %s, %s one seat each' % (ESAU_DID_FOR_ME, MOABITES_AR))
        move('cold_run_chukat (CALL) — CK.edom_and_hor(edom_passage) = %s' % CK_EDOM[0][:80], "the DISPUTE row holds both arms — 20:18-21's double refusal and 2:28-29's purchase; the Sifrei silent; Judges 11:17 outside the Torah: no link of our own")
        dat('the row the_edom_disagreement: %s — OPEN (R4)' % data['the_edom_disagreement']['value'])
        return out("the Edom disagreement (2:29) — 'as the sons of Esau did for me' against 20:18-21's refusal: DISAGREES, the chukat row's two arms (CK by CALL), an OPEN row", ['accepted'])
    if ask == 'the_hardening':
        ink('2:30', '"Sihon would not let us pass; for the LORD your God hardened his spirit and made his heart obstinate" — %s one seat' % HARDENED)
        move('cold_run_chukat (CALL) — CK.well_and_kings(sihon_refused) = %s; Exodus 4-14\'s hardening by REFERENCE' % CK_REFUSED[0][:50], "Pharaoh's two verbs at Sihon — the exodus story's hardening seats the kin; 21:23 says he did not let Israel pass")
        return out("the hardening (2:30) — told only here in Pharaoh's verbs (the exodus story by REFERENCE); sihon's refused read (CK by CALL): EXPANDED", ['accepted'])
    if ask == 'jahaz':
        ink('2:32-33', '"Sihon came out against us, he and all his people, to battle at Jahaz; the LORD our God delivered him before us and we smote him and his son and all his people" — %s; 2:32 %d tokens for 21:23\'s %d (computed: %d shared)' % (JAHAZ, len(JAHAZ_DEUT), len(JAHAZ_NUM), len(set(JAHAZ_DEUT) & set(JAHAZ_NUM))))
        return out("Jahaz (2:32-33) — eight tokens for 21:23's twenty: SHORTENED; 21:24's smiting the run", ['accepted'])
    if ask == 'the_written_and_read':
        ink('2:33', '"and we smote him and his SON and all his people" — written "his son" (the DB\'s eleven tokens), read "his sons" (the store\'s twelve); Onkelos plural')
        move('the reading\'s find (2026-09-15); Onkelos 2:33', "the written and the read — the store's mixed families a display sitting's; the DB's consonants the ink")
        return out("written 'his son', read 'his sons' (2:33) — the DB's eleven tokens against the store's twelve; Onkelos plural: the reading's find, DATA", ['accepted'])
    if ask == 'the_ban':
        ink('2:34-35; 3:6-7', '"we devoted every city — the men, the women and the little ones; we left none remaining; only the cattle we took" — %s (2:34 and 3:6 alone), %s, %s' % (DEVOTED_WE, EVERY_CITY_MEN, NONE_LEFT))
        move('cold_run_primeval (CALL) — PR.pieces(fourth_generation) = %s (fx %s)' % (PR_FOURTH['v'], PR_FOURTH['fx']), "'the iniquity of the Amorite is not yet full' (Genesis 15:16) — amorite_not_full on the Amorite READ beside the ban: a printed line, no verdict; Deuteronomy 20:16-17 FORWARD")
        dat('the row the_ban: %s — destroyed on the-amorite TWICE (the supplied acts sihons_cities_devoted, ogs_cities_devoted)' % data['the_ban']['value'])
        return out("the ban (2:34-35; 3:6-7) — told only in the retelling: destroyed on the Amorite twice (21:24-25, 21:35 say smote and possessed); 15:16's status read; the cherem law forward", ['destroyed'])
    if ask == 'aroer_to_gilead':
        ink('2:36-37', '"from Aroer on the edge of the valley of Arnon … to Gilead there was not a city too high for us; only to the land of the sons of Ammon you came not near" — %s, %s, %s' % (FROM_AROER, TOO_HIGH, LAND_AMMON[:3]))
        move('cold_run_chukat (CALL) — CK.well_and_kings(ammon_border) = %s' % CK_AMMON[0][:60], "21:24's border STRONG; here RESPECTED — the same border, the bar's reason")
        return out("Aroer to Gilead (2:36-37) — the border respected (2:37) against 21:24's strong (CK by CALL): EXPANDED", ['accepted'])
    if ask == 'og_turned':
        ink('3:1-3', '"we turned and went up the way to Bashan; Og came out against us … the LORD said to me: fear him not … as you did to Sihon" — %s, %s (3:2 = 21:34), %s; 3:1-3 %d tokens for 21:33-35\'s %d, %d shared, the shifts %s (computed)' % (EDREI, FEAR_HIM_NOT, AS_TO_SIHON, len(OG_D), len(OG_N), OG_SHARED, OG_SHIFT))
        move('cold_run_chukat (CALL) — CK.well_and_kings(deut3_delta) = %s' % CK_DELTA[0], "we for they, 'to me' for 'to Moses' — the chukat runner's own row")
        return out("Og turned (3:1-3) — 21:33-35 with the persons shifted (we for they; to me for to Moses): TURNED, the five shifts computed; fear_not_promised on Moses read", ['accepted'])
    if ask == 'the_sixty_cities':
        ink('3:4-5', '"sixty cities, all the region of Argob, the kingdom of Og in Bashan; all these cities fortified with high walls, gates and bars" — the parser [%d]; %s, %s, %s' % (SIXTY, SIXTY_CITIES, ARGOB, HIGH_WALLS))
        move('Arakhin 32b:6; Megillah 10a:10; Shevuot 16a:14; Arakhin 33b:22 (credited)', "the walled cities from Joshua's days many, the re-sanctified enumerated; 'walled' learned from 3:5 by the verbal analogy")
        dat('the row the_sixty_cities: %s' % data['the_sixty_cities']['value'])
        return out("the sixty cities (3:4-5) — [60], Argob's; the walled cities from Joshua's days (Arakhin 32b:6; Megillah 10a:10); Leviticus 25:29's 'walled' learned here: DATA", ['accepted'])
    if ask == 'ogs_bed':
        ink('3:11', '"only Og king of Bashan remained of the remnant of the Rephaim; behold his bedstead was a bedstead of iron … nine cubits its length and four cubits its breadth, by the cubit of a man" — the parser %s; %s, %s, %s, %s' % (BED, REMNANT_REPHAIM, IRON_BED, NINE_CUBITS, CUBIT_OF_MAN))
        move('Mishnah Kelim 17:9-10; Mishnah Eruvin 4:8; cold_run_chukat (CALL) — CK.DATA[og_lore] = %s; cold_run_primeval (CALL) — PR.war(og) = %s' % (CK.DATA['og_lore']['value'], PR_OG['v']), "the cubit of which they spoke the medium one; Og Sihon's brother of the Rephaim, the escapee")
        dat('the row ogs_bed: %s' % data['ogs_bed']['value'])
        return out("Og's bed (3:11) — [9, 4] by the cubit of a man (Kelim 17:9-10); the remnant of the Rephaim; Og's lore by CALL: DATA", ['accepted'])
    if ask == 'hermon':
        ink('3:8-9', '"from the valley of Arnon to Mount Hermon — the Sidonians call Hermon Sirion, and the Amorites call it Senir" — %s (%d seats), %s, %s' % ('Hermon', len(HERMON), SIRION, SENIR))
        move('Chullin 60b:14 (credited); Song 4:8', "every nation built a city on Hermon and named it after a mountain of the land — the verses fit to be burned")
        return out("Hermon (3:8-9) — Sirion and Senir, the nations' names (Chullin 60b:14; Song 4:8): EXPANDED", ['accepted'])
    return out('no verdict in span', [FX.NONE])


# ===== F6: THE EAST AND THE CHARGES (Deut 3:12-22) ==========================================================
def the_east_and_the_charges(case, data):
    del P[:]
    ask = case['ask']
    if ask == 'the_division':
        ink('3:12-13', '"from Aroer … and HALF the hill country of Gilead and its cities I gave to the Reubenite and the Gadite; the rest of Gilead and all Bashan … to the HALF tribe of Manasseh" — the halves %s by rule 30; %s, %s, %s; 3:12-13 %d tokens for 32:33\'s %d (computed)' % (HALVES, HALF_GILEAD, REUBENITE_GADITE[:3], HALF_MANASSEH, len(DIV_D), len(DIV_N)))
        move('cold_run_gad_reuben (CALL) — GR.the_grant(three_parties) = %s; cold_run_borders (CALL) — BO.moses_restatement(the_nine_and_a_half) = %s' % (GR_THREE[0][:60], BO_NINE[0][:50]), "the three holdings of 32:33 read; 34:13-15's halves the kin")
        return out("the division (3:12-13) — 32:33's three holdings read back, DIVIDED: half Gilead to the two, the rest and Bashan to the half tribe (thirty-six tokens for twenty-nine); the halves [1/2] by rule 30: EXPANDED", ['accepted'])
    if ask == 'jair':
        ink('3:14', '"Jair son of Manasseh took all the region of Argob to the border of the Geshurite and the Maacathite, and called them after his own name, Bashan-havvoth-jair, to this day" — %s, %s (%d seats), %s; %d tokens for 32:41\'s %d (computed)' % (JAIR_MANASSEH, 'Havvoth-jair', len(HAVVOTH_JAIR), GESHURITE, len(JAIR_D), len(JAIR_N)))
        move('cold_run_gad_reuben (CALL) — GR.machir_jair_nobah(jair) = %s' % GR_JAIR[0][:60], "32:41's taking read; 1 Kings 4:13 the kin; 'to this day' the retelling's")
        return out("Jair (3:14) — 32:41 read back, EXPANDED (twenty-three tokens for eleven): Argob, the Geshurite and the Maacathite, 'to this day' told only here", ['accepted'])
    if ask == 'machir':
        ink('3:15', '"and to Machir I gave Gilead" — %s one seat' % TO_MACHIR)
        move('cold_run_gad_reuben (CALL) — GR.machir_jair_nobah(gilead_given) = %s' % GR_GILEAD[0][:60], "32:40's 'Moses gave' in the first person — the clan under the ancestor's name")
        return out("Machir (3:15) — 32:40's 'Moses gave' in the first person: TURNED", ['accepted'])
    if ask == 'the_borders':
        ink('3:16-17', '"from Gilead to the valley of Arnon, the middle of the valley the border, to the river Jabbok, the border of the children of Ammon; the Arabah and the Jordan for a border, from Chinnereth to the sea of the Arabah, the Salt Sea, under the slopes of Pisgah eastward" — %s, %s (%d seats), %s, %s' % (MIDDLE_BROOK, 'the Jabbok', len(JABBOK), SALT_SEA_ARABAH, SLOPES_PISGAH))
        dat('the row the_easts_borders: %s — no write, the holdings stand' % data['the_easts_borders']['value'])
        return out("the east's borders (3:16-17) — told only here: the Arnon's middle, the Jabbok, Chinnereth to the Salt Sea under Pisgah — DATA, no write", ['accepted'])
    if ask == 'the_charge_to_the_tribes':
        ink('3:18-20', '"I commanded you at that time: the LORD your God has given you this land to possess; you shall pass over ARMED before your brothers … until the LORD gives rest to your brothers as to you … then you shall return every man to his possession" — %s, %s, %s (Joshua 1:15), %s' % (GIVEN_THIS_LAND, ARMED, UNTIL_REST, EACH_TO_POSSESSION))
        move('cold_run_gad_reuben (CALL) — GR.the_condition(positive_arm) = %s; GR.DATA[half_manassehs_stipulation] = %s; GR.the_offer(not_return) = %s' % (GR_POS[0][:50], GR.DATA['half_manassehs_stipulation']['value'], GR_RETURN[0][:50]), "the condition's debit OPEN read; half Manasseh included by the retelling; Joshua 22:4 the release outside the Torah")
        dat('the row the_armed_passage: %s' % data['the_armed_passage']['value'])
        return out("the charge to the tribes (3:18-20) — 32:20-24's condition in the first person with half Manasseh included: TURNED; the debit OPEN read (GR by CALL); 'until the LORD gives rest' Joshua 1:15's", ['accepted'])
    if ask == 'joshuas_charge':
        ink('3:21-22', '"and I commanded Joshua at that time: your eyes have seen all that the LORD your God has done to these two kings; so shall the LORD do to all the kingdoms; you shall not fear them, for the LORD your God, He fights for you" — %s, %s (PLENE, the Torah\'s one seat), %s, %s, %s, %s' % (COMMANDED_JOSHUA_TIME, JOSHUA_PLENE, EYES_SEEN, ALL_KINGDOMS, NOT_FEAR_THEM, HE_FIGHTS))
        move('Sifrei Devarim 29:8-9; Joshua 1:6; 23:3, 10', "the condition Joshua broke at Ai — the run against the spec outside the Torah; 'He fights for you' Joshua's own refrain")
        dat('the row joshuas_charge: %s' % data['joshuas_charge']['value']['promise'])
        return out("Joshua's charge (3:21-22) — told only here: fear_not_promised on Joshua (21:34's effect at its second party); Joshua plene; Ai's run outside the Torah (the Sifrei 29:8-9)", ['fear_not_promised'])
    return out('no verdict in span', [FX.NONE])


# ===== F7: THE PLEA (Deut 3:23-29) ==========================================================================
def the_plea(case, data):
    del P[:]
    ask = case['ask']
    if ask == 'the_plea':
        ink('3:23-26', '"and I besought the LORD at that time … let me go over, I pray, and see the good land … but the LORD was wroth with me for your sakes and did not hear me: let it suffice you; speak no more to Me of this matter" — %s, %s, %s, %s, %s, %s' % (BESOUGHT, LET_ME_GO_OVER, WROTH_FOR_YOU, NOT_HEAR_ME, SUFFICE_YOU, SPEAK_NO_MORE))
        move('Berakhot 32a:32; Avodah Zarah 7b:18; Berakhot 30b:9; Sotah 13b:13 (credited); cold_run_beha (CALL) — BH.march(hobab) = %s' % BH_HOBAB[0][:40], "praise before the request; the pleading mode; 'let it suffice you' measure for measure; the refusal in the value as Hobab's row carries it")
        dat('plea_made on moses valued the plea AND its answer — %s; barred_from_the_land OPEN read, no new heaven write' % data['the_plea']['value']['answer'])
        return out("the plea (3:23-26) — told only here: plea_made on Moses with the refusal in the value; the barred entry OPEN read; praise before the request (Berakhot 32a:32)", ['plea_made'])
    if ask == 'the_names':
        ink('3:24', '"O Lord GOD, You have begun to show Your servant Your greatness and Your strong hand; what god is there in heaven or on earth" — %s, %s, %s (1 Kings 8:42 the other), %s; "O Lord GOD" %d Bible seats' % (BEGUN_SHOW, YOUR_GREATNESS, STRONG_HAND, WHAT_GOD, len(LORD_GOD)))
        move('Sifrei Devarim 27:4; Genesis 15:2, 15:8; 1 Kings 8:42', "'Your greatness' the binyan av; 'O Lord GOD' Abraham's two seats and Moses' two; 'Your strong hand' Solomon's prayer")
        return out("the names (3:24) — 'O Lord GOD' Abraham's and Moses'; 'Your greatness' the Sifrei 27:4's binyan av; 'Your strong hand' 1 Kings 8:42's: DATA", ['accepted'])
    if ask == 'lebanon':
        ink('3:25', '"let me go over and see the good land beyond the Jordan, that goodly hill country and Lebanon" — %s; "the good land" %d seats' % (GOOD_LAND_BEYOND, len(THE_GOOD_LAND)))
        move('Sifrei Devarim 6:2, 28:3; Gittin 56b:1; Onkelos 3:25', "Lebanon the Temple ('Lebanon shall fall by a mighty one', Isaiah 10:34); the good mountain Jerusalem — Onkelos writes the Temple in")
        return out("Lebanon (3:25) — the Temple (the Sifrei 6:2, 28:3; Gittin 56b:1); 1:7's Lebanon the region, this the house: DATA", ['accepted'])
    if ask == 'the_refusal':
        ink('3:26', '"the LORD was wroth with me for your sakes and did not hear me; the LORD said to me: let it suffice you; speak no more to Me of this matter" — "was wroth" %s (three Bible seats); "enough for you" singular %s (the plural %d seats)' % (WROTH, ENOUGH_SG, len(ENOUGH_PL)))
        move('Sotah 13b:13 (credited); cold_run_chukat (CALL) — CK.meribah(sentence)', "Moses rebuked with 'rav' (16:3, 7) and answered with 'rav' — measure for measure; the barred entry OPEN, its ground disputed (1:37)")
        return out("the refusal (3:26) — 'let it suffice you' the singular's one seat, measure for measure for Korach's (Sotah 13b:13); 'did not hear' 1:45's phrase; the barred entry read", ['accepted'])
    if ask == 'pisgah':
        ink('3:27', '"go up to the top of Pisgah and lift up your eyes westward and northward and southward and eastward, and see with your eyes; for you shall not go over this Jordan" — %s, %s, %s' % (TOP_PISGAH, FOUR_DIRECTIONS, NOT_CROSS_JORDAN))
        dat('the row the_four_directions: %s — three orders; the see_the_land debit on Moses OPEN (27:12) READ BACK, no second write' % data['the_four_directions']['value'])
        return out("Pisgah (3:27) — 27:12's command read back with Pisgah for Abarim and the four directions in the third order: TURNED; the debit OPEN read", ['accepted'])
    if ask == 'command_joshua':
        ink('3:28', '"command Joshua, and strengthen him and encourage him; for he shall go over before this people, and he shall cause them to inherit the land" — %s, %s, %s, %s; "be strong and of good courage" %d seats (Joshua 1:6 among them)' % (COMMAND_JOSHUA, STRENGTHEN, HE_SHALL_CROSS, CAUSE_THEM_INHERIT, len(BE_STRONG)))
        move('Kiddushin 29a:14 (credited)', "'command' a galvanization, immediate and for generations; the commissioning of 27:18-23 READ BACK")
        return out("command Joshua (3:28) — the commission read back (Kiddushin 29a:14 — a galvanization for generations); 'he shall cause them to inherit' the effect's second seat: TURNED", ['accepted'])
    if ask == 'beth_peor':
        ink('3:29', '"and we abode in the valley over against Beth-peor" — %s; "over against Beth-peor" %s (4:46 the speech\'s place; 34:6 Moses\' grave)' % (VALLEY_PEOR, AGAINST_PEOR))
        move('cold_run_balak (CALL) — BK.the_call(last_camp) = %s' % BK_LAST[0][:60], "the plains of Moab — the last camp; the book never moves again")
        return out("Beth-peor (3:29) — the last camp by CALL (22:1; 36:13; Deuteronomy 34:1); 4:46 and 34:6 the valley's other seats: EXPANDED", ['accepted'])
    return out('no verdict in span', [FX.NONE])

# ---- THE WRAP — the daemon, the scene, the narrative ------------------------------------------------------
CELL_TAG = {'commission': 'F0', 'frame': 'F1', 'judges': 'F2', 'spies': 'F3', 'bypass': 'F4', 'sihon_og': 'F5', 'east': 'F6', 'plea': 'F7'}
CELL_FN = {'commission': the_commission, 'frame': the_frame, 'spies': the_spies_read_back, 'bypass': the_bypass, 'sihon_og': sihon_and_og, 'east': the_east_and_the_charges, 'plea': the_plea}

def _closed_by_prior_run(world, event, eff, closer):
    """THE CLOSE BY A PRIOR RUN (THE READBACK'S FIRST FORM, R3): a supplied debit is OPENED AND CLOSED IN ONE BLOCK — the engine writes a daemon's
    effects after the daemon returns, so the daemon writes this one itself, stamped as the engine would stamp it (the event's date, the writer),
    and closes it at once with the tape's EARLIER line as the closer (closed_by naming the run's verse): the ledger's own record that the command
    came to the reader after its execution. The recorder never records a daemon's close as a tape line (the close is the daemon's own write)."""
    for key in ('bound', 'dated'):
        if key in event:
            eff.setdefault(key, event[key])
    eff.setdefault('written_by', 'law_opening_speech')
    world._write(eff)
    world.close(eff['subject'], eff['effect'], closer, value=eff['value'])

def law_opening_speech(event, world):
    """Deut 1:1-3:29 with Num 27:12-23 (cold_run_opening_speech.py F0-F7). given_at Deut 1:16; installed_by boot — A LAW IN MOSES' VOICE WITH NO
    DIVINE FRAME (the vows' class; the class named in the registry, the second pass decides). SIXTEEN TAPE LINES: the commission's four (Num
    27:12-23 — a debit on Moses OPEN to Deuteronomy 34, the shepherd's plea, the commission's debit and its CLOSE by its run); the frame (the book's
    one act of its own day — torah_expounded on Israel); the eleven acts told only in the retelling, each written ONCE at its own time by a
    retrograde marker — four supplied debits CLOSED AT ONCE BY A PRIOR RUN, the judges' charge (THE LAW — a status on the court), the three bars
    and grants, the two bans, Joshua's promise, the plea with its refusal. The exam's two case kinds dispatch to the cells in EXPLICIT branches with
    LITERAL effects per kind (2b's form — an unnamed effect is a KeyError)."""
    k, src = event['kind'], event['case_source']
    E_ = lambda eff, s, cp=None, amount=None, due=None, law='', value=None: {'effect': eff, 'subject': s, 'counterparty': cp, 'amount': amount, 'due': due, 'value': value if value is not None else True, 'source_law': law, 'case_source': src}
    # ---- F0: the commission (Num 27:12-23 — page_order at the daughters' day) ----
    if k == 'moses_told_to_ascend_abarim':
        return [E_('commanded', 'moses', value='see_the_land_from_abarim', law='F0 [INK 27:12 "go up to this mountain of Abarim and see the land" — the debit OPEN BY DESIGN to Deuteronomy 34:1-4 (this book\'s own end); 27:14\'s Meribah an INTERNAL pointer to 20:12\'s sentence, the barred entry read; Deuteronomy 3:27 the retelling READ BACK]')]
    if k == 'a_shepherd_asked':
        return [E_('plea_made', 'moses', value='let the LORD, the God of the spirits of all flesh, appoint a man over the congregation, who may go out before them and come in before them, that the congregation of the LORD be not as sheep without a shepherd (27:16-17)', law='F0 [INK 27:15-17 — the successor asked before he is named; 16:22\'s phrase at its second seat; Sanhedrin 17a:10 Eldad and Medad\'s prophecy]')]
    if k == 'joshua_commission_commanded':
        return [E_('commanded', 'moses', value='commission_joshua_before_eleazar', law='F0 [INK 27:18-21 "take you Joshua … lay your hand upon him; set him before Eleazar the priest … put of your honor upon him … by the judgment of the Urim" — one hand commanded (the Sifrei 141); the Urim final (C2 by CALL); the debit CLOSED by the next line\'s run]')]
    if k == 'joshua_commissioned':
        world.close('moses', 'commanded', 'Num 27:22-23 — and Moses did as the LORD commanded him; he took Joshua and set him before Eleazar the priest and before all the congregation, and laid his hands upon him and commanded him, as the LORD spoke by the hand of Moses: THE COMMISSION\'S DEBIT CLOSED BY ITS RUN (the receipt "as the LORD commanded" — the spec/run pair\'s form); the register seat Num 27:22 CLOSE', value='commission_joshua_before_eleazar')
        return [E_('invested_office', 'joshua', value='the hand laid — two hands for the one commanded (27:23; the Sifrei 141); some of Moses\' honor (27:20 — the sun and the moon, Bava Batra 75a:8); before Eleazar the priest by the judgment of the Urim (27:21)', law='F0 [INK 27:22-23 "and he laid his hands upon him and commanded him, as the LORD spoke by the hand of Moses" — Joshua invested; Deuteronomy 3:28 "command Joshua" the commissioning READ BACK (Kiddushin 29a:14)]')]
    # ---- F1: the frame — the book's one act of its own day (text_constrained at the marker's verse) ----
    if k == 'speech_opened':
        return [E_('torah_expounded', 'israel', value={'words': 'these are the words which Moses spoke to all Israel beyond the Jordan (1:1) — the eleven places the rebuke\'s sins (the Sifrei 1; Onkelos)', 'date': (40, 11, 1), 'receipt': 'according to all that the LORD commanded him (1:3) — the hermeneutic rules (the Sifrei 2:8)', 'after': 'after he had smitten Sihon and Og (1:4) — the fortieth year\'s order (Rosh Hashanah 2b:13)'}, law='F1 [INK 1:5 "Moses undertook to expound this Torah" — the frame: a STATUS on Israel dated (40, 11, 1) by 1:3\'s number reader, the era the exodus\'s by the taught verbal analogy with 33:38 (Rosh Hashanah 2b:11; JO by CALL); everything after it in chapters 1-3 read back or supplied at its own time (R6); the register seat Deut 1:3 ACT]')]
    # ---- F2: the Horeb command (supplied, dated (2, 2, 20)) and the judges' charge (THE LAW, dated (1, 2, 16)) ----
    if k == 'horeb_departure_commanded':
        _closed_by_prior_run(world, event, E_('commanded', 'israel', value='journey_to_the_mountain_of_the_amorite', law='F2 [INK 1:6-8 "you have dwelt long enough in this mountain; turn and take your journey and go to the hill country of the Amorites … go in and possess the land" — TOLD ONLY IN THE RETELLING (Exodus 33:1 the command\'s kin): written once, dated (2, 2, 20) by the retrograde marker at 1:6, CLOSED AT ONCE BY THE PRIOR RUN — the arrival in Paran; "go in and possess" a REFERENCE to land_granted (Genesis 15:18) and the OPEN dispossess debit (33:50-56)]'),
                             'Num 12:16 — and afterward the people journeyed from Hazeroth and encamped in the wilderness of Paran: THE CLOSE BY A PRIOR RUN (R3) — the departure from Horeb commanded at Deuteronomy 1:6-8 ran at Numbers 10:11-12:16, the tape\'s earlier line; the command came to the reader after its execution')
        return []
    if k == 'judges_charged':
        return [E_('judges_charged', 'the-court', value=['hear between your brothers', 'judge righteously between a man and his brother and his stranger', 'no faces in judgment', 'the small as the great', 'fear no man, for the judgment is God\'s', 'the hard matter to me'], law='F2 [INK 1:16-17 "and I charged your judges at that time, saying: hear between your brothers, and judge righteously between a man and his brother and the stranger with him; you shall not respect persons in judgment; you shall hear the small and the great alike; you shall not be afraid of the face of any man, for the judgment is God\'s; and the cause that is too hard for you, you shall bring to me" — THE LAW OF THE SPAN in Moses\' voice with no divine frame: ONE STATUS on the court, the six clauses, dated (1, 2, 16) by the court\'s founding day read off Israel\'s ledger (the retrograde marker at 1:9); the appointment (1:9-15) a REFERENCE to judges_appointed (Exodus 18:25 — TURNED); the clauses\' arms the exam\'s rows (Sanhedrin 7b:14-8a:6; 6b; Mishnah Sanhedrin 1, 3, 4; Avot 1:1)]')]
    # ---- F4: the bypass — the supplied acts dated (40, 6, 1) by the retrograde marker at 2:2 ----
    if k == 'turn_northward_commanded':
        _closed_by_prior_run(world, event, E_('commanded', 'israel', value='turn_northward', law='F4 [INK 2:2-3 "you have compassed this mountain long enough; turn you northward" — TOLD ONLY HERE: written once, dated (40, 6, 1) by the retrograde marker at 2:2 (the departure from Mount Hor), CLOSED AT ONCE BY THE PRIOR RUN — the march past Moab (21:10-13)]'),
                             'Num 21:10-13 — and the children of Israel journeyed and camped at Oboth; and from Oboth at Iye-abarim in the wilderness before Moab toward the sunrise; and from there at the brook Zered; and from there beyond the Arnon: THE CLOSE BY A PRIOR RUN (R3) — the turn northward commanded at Deuteronomy 2:2-3 ran at Numbers 21:10-13, the tape\'s earlier line')
        return [E_('contending_barred', 'edom', value='do not contend with them; not so much as for the sole of the foot to tread on (2:5) — your brothers the sons of Esau who dwell in Seir (2:4, 2:8)', law='F4 [INK 2:4-5 "do not contend with them, for I will not give you of their land" — the BLOCK on Edom told only here; the bar\'s reach: battle and harassing alike (Edom "your brothers" — Deuteronomy 23:8 forward); Bava Kamma 38a:16 Moses\' a fortiori from Midian needed the bar]'),
                E_('land_granted', 'edom', value='mount_seir', law='F4 [INK 2:5 "because I have given Mount Seir to Esau for a possession" — the grant told here: Genesis 36:8\'s dwelling in Seir (JS by CALL) the standing status; Kiddushin 18a:2 — a gentile inherits by Torah law from this verse; Bereshit Rabbah 44:23 the Kenite kept for Edom (PR by CALL)]')]
    if k == 'moab_spared_commanded':
        return [E_('contending_barred', 'the-moabites', value='do not harass Moab nor contend with them in battle (2:9) — battle forbidden, harassing not (Horayot 10b:19; Nazir 23b:11)', law='F4 [INK 2:9 "do not harass Moab nor contend with them in battle, for I will not give you of his land" — the BLOCK on the Moabites told only here; the bar the a fortiori from Midian needed (Bava Kamma 38a:16 — BK by CALL); the reward of the elder daughter\'s euphemism (Horayot 10b:19)]'),
                E_('land_granted', 'the-moabites', value='ar', law='F4 [INK 2:9 "because I have given Ar to the children of Lot for a possession" — the grant told here: Lot\'s elder daughter\'s people (Genesis 19:37 — MM by CALL); Moab\'s land purified through Sihon (Chullin 60b:13 — CK.DATA by CALL)]')]
    if k == 'zered_crossing_commanded':
        _closed_by_prior_run(world, event, E_('commanded', 'israel', value='cross_the_brook_zered', law='F4 [INK 2:13 "now rise up and get you over the brook Zered; and we went over the brook Zered" — TOLD ONLY HERE: written once, dated (40, 6, 1), CLOSED AT ONCE BY THE PRIOR RUN — the camp at the brook Zered (21:12, inside the four camps\' line); 2:14\'s thirty-eight years from Kadesh-barnea against the tape\'s years (CA2)]'),
                             'Num 21:10-13 — and from there they journeyed and camped at the brook Zered (21:12): THE CLOSE BY A PRIOR RUN (R3) — the crossing of the Zered commanded at Deuteronomy 2:13 ran at Numbers 21:12, inside the tape\'s earlier line of the four camps (21:10-13); the thirty-eight years (2:14) the tape\'s own years from the spies\' return')
        return []
    if k == 'ammon_spared_commanded':
        return [E_('contending_barred', 'the-sons-of-ammon', value='do not harass them nor contend with them (2:19) — not even harassed (Bava Kamma 38b:6; Horayot 11a:1; Nazir 23b:12)', law='F4 [INK 2:19 "when you come near over against the children of Ammon, do not harass them nor contend with them, for I will not give you of the land of the children of Ammon" — the BLOCK on the sons of Ammon told only here — the one NEW written-on party (Genesis 19:38\'s people); Ammon\'s border strong at 21:24, commanded off-limits here (CK.DATA by CALL); the reward of the younger daughter\'s euphemism]'),
                E_('land_granted', 'the-sons-of-ammon', value='the land of the sons of Ammon', law='F4 [INK 2:19 "because I have given it to the children of Lot for a possession" — the grant told here: Lot\'s younger daughter\'s people (Genesis 19:38 — MM by CALL)]')]
    if k == 'sihon_war_commanded':
        _closed_by_prior_run(world, event, E_('commanded', 'israel', value='begin_to_possess_sihons_land', law='F4 [INK 2:24-25 "rise up, take your journey, and pass over the valley of Arnon; behold, I have given into your hand Sihon … begin to possess it, and contend with him in battle; this day will I begin to put the dread of you" (2:31 "begin to possess, that you may inherit his land") — TOLD ONLY HERE (21:21 says Israel sent messengers, no command): written once, dated (40, 6, 1), CLOSED AT ONCE BY THE PRIOR RUN — the smiting and possession (21:24-25); the dread DATA (Avodah Zarah 25a:7-9; Taanit 20a:6-8 — the sun for Moses)]'),
                             'Num 21:24-25 — and Israel smote him with the edge of the sword and possessed his land from the Arnon to the Jabbok, as far as the sons of Ammon; and Israel took all these cities and dwelt in all the cities of the Amorite: THE CLOSE BY A PRIOR RUN (R3) — the war on Sihon commanded at Deuteronomy 2:24-25 ran at Numbers 21:24-25, the tape\'s earlier line')
        return []
    # ---- F5: the bans told only in the retelling (supplied acts on the Amorite) ----
    if k == 'sihons_cities_devoted':
        return [E_('destroyed', 'the-amorite', cp='israel', value='every city of Sihon\'s — the men, the women and the little ones; none left; the cattle and the spoil taken (2:34-35)', law='F5 [INK 2:34-35 "and we took all his cities at that time, and utterly destroyed every city, the men and the women and the little ones; we left none remaining; only the cattle we took for a prey" — THE BAN TOLD ONLY HERE (21:24-25 say smote and possessed): the body effect the king of Arad\'s line wrote at 21:3, on the Amorite; Genesis 15:16\'s amorite_not_full status READ beside it (PR by CALL — a printed line, no verdict); Deuteronomy 20:16-17\'s law FORWARD]')]
    if k == 'ogs_cities_devoted':
        return [E_('destroyed', 'the-amorite', cp='israel', value='every city of Og\'s sixty — the men, the women and the little ones; the cattle and the spoil taken (3:6-7)', law='F5 [INK 3:6-7 "and we utterly destroyed them, as we did to Sihon king of Heshbon, utterly destroying every city, the men and the women and the little ones; but all the cattle and the spoil of the cities we took" — THE SECOND BAN TOLD ONLY HERE (21:35 says smote and possessed); the sixty cities of Argob (3:4-5 — [60]; Arakhin 32b:6 the walled cities from Joshua\'s days)]')]
    # ---- F6: Joshua's promise (supplied) ----
    if k == 'joshua_encouraged':
        return [E_('fear_not_promised', 'joshua', value='your eyes have seen all that the LORD your God has done to these two kings; so shall the LORD do to all the kingdoms; you shall not fear them, for the LORD your God, He fights for you (3:21-22)', law='F6 [INK 3:21-22 "and I commanded Joshua at that time, saying: your eyes have seen … you shall not fear them" — TOLD ONLY HERE: HEAVEN\'s promise on Joshua, 21:34\'s effect ("fear him not", on Moses) at its second party; Joshua 1:6 and Ai\'s run outside the Torah (the Sifrei 29:8-9 the condition Joshua broke — DATA); Joshua written plene here alone in the Torah]')]
    # ---- F7: the plea with its refusal (supplied) ----
    if k == 'moses_besought':
        return [E_('plea_made', 'moses', value='let me go over, I pray, and see the good land beyond the Jordan, that goodly hill country and Lebanon (3:25) — REFUSED: let it suffice you; speak no more to Me of this matter (3:26); the LORD was wroth with me for your sakes and did not hear me', law='F7 [INK 3:23-26 "and I besought the LORD at that time … O Lord GOD, You have begun to show Your servant Your greatness … let me go over … but the LORD was wroth with me for your sakes" — TOLD ONLY HERE: the plea AND its answer in the value as Hobab\'s row carries the refusal (BH by CALL); the barred_from_the_land entry on Moses OPEN, READ — no new heaven write; praise before the request (Berakhot 32a:32); "let it suffice you" measure for measure (Sotah 13b:13); Lebanon the Temple (Gittin 56b:1)]')]
    # ---- the exam's case kinds: EXPLICIT branches per kind (the daemon gate parses explicit branches only), each naming LITERALLY every effect it can write (2b's form — an unnamed effect is a KeyError) ----
    if k == 'judges_case':
        v, e, _ = the_officers_and_the_judges({'ask': event['ask']}, DATA); L = 'F2 [%s]' % event['ask']; s_ = event['person']
        W = {'accepted': E_('accepted', s_, value=v, law=L), 'exempt': E_('exempt', s_, value=v, law=L), 'judgment_perverted': E_('judgment_perverted', s_, value=v, law=L)}
        return [W[x] for x in e if x != FX.NONE]
    if k == 'speech_case':
        v, e, _ = CELL_FN[event['cell']]({'ask': event['ask']}, DATA); L = '%s [%s]' % (CELL_TAG[event['cell']], event['ask']); s_ = event['person']
        W = {'accepted': E_('accepted', s_, value=v, law=L), 'exempt': E_('exempt', s_, value=v, law=L)}
        return [W[x] for x in e if x != FX.NONE]
    return []


LINES = [
    ('Num 27:12-14 — and the LORD said to Moses: go up to this mountain of Abarim and see the land which I have given to the children of Israel; and when you have seen it, you also shall be gathered to your people, as Aaron your brother was gathered; because you rebelled against My word in the wilderness of Zin, in the strife of the congregation, to sanctify Me at the waters before their eyes — these are the waters of Meribah of Kadesh in the wilderness of Zin', 'moses_told_to_ascend_abarim'),
    ('Num 27:15-17 — and Moses spoke to the LORD, saying: let the LORD, the God of the spirits of all flesh, appoint a man over the congregation, who may go out before them and who may come in before them, and who may lead them out and who may bring them in, that the congregation of the LORD be not as sheep which have no shepherd', 'a_shepherd_asked'),
    ('Num 27:18-21 — and the LORD said to Moses: take you Joshua the son of Nun, a man in whom is spirit, and lay your hand upon him; and set him before Eleazar the priest and before all the congregation, and command him in their sight; and you shall put of your honor upon him, that all the congregation of the children of Israel may hear; and he shall stand before Eleazar the priest, who shall inquire for him by the judgment of the Urim before the LORD; at his word shall they go out and at his word shall they come in', 'joshua_commission_commanded'),
    ('Num 27:22-23 — and Moses did as the LORD commanded him; and he took Joshua and set him before Eleazar the priest and before all the congregation; and he laid his hands upon him and commanded him, as the LORD spoke by the hand of Moses', 'joshua_commissioned'),
    ('Deut 1:1-5 — these are the words which Moses spoke to all Israel beyond the Jordan, in the wilderness, in the Arabah over against Suph, between Paran and Tophel and Laban and Hazeroth and Di-zahab; eleven days from Horeb by the way of Mount Seir to Kadesh-barnea; and it came to pass in the fortieth year, in the eleventh month, on the first of the month, that Moses spoke to the children of Israel according to all that the LORD had commanded him to them; after he had smitten Sihon king of the Amorites who dwelt in Heshbon, and Og king of Bashan who dwelt in Ashtaroth, at Edrei; beyond the Jordan, in the land of Moab, Moses undertook to expound this Torah, saying', 'speech_opened'),
    ('Deut 1:6-8 — the LORD our God spoke to us in Horeb, saying: you have dwelt long enough in this mountain; turn and take your journey and go to the hill country of the Amorites and to all the places near it, in the Arabah, in the hill country, in the lowland, in the Negev and by the seashore, the land of the Canaanites and Lebanon, as far as the great river, the river Euphrates; behold, I have set the land before you: go in and possess the land which the LORD swore to your fathers, to Abraham, to Isaac and to Jacob, to give to them and to their seed after them', 'horeb_departure_commanded'),
    ('Deut 1:16-18 — and I charged your judges at that time, saying: hear the causes between your brothers, and judge righteously between a man and his brother and the stranger with him; you shall not respect persons in judgment; you shall hear the small and the great alike; you shall not be afraid of the face of any man, for the judgment is God\'s; and the cause that is too hard for you, you shall bring to me and I will hear it; and I commanded you at that time all the things that you should do', 'judges_charged'),
    ('Deut 2:2-7 — and the LORD spoke to me, saying: you have compassed this mountain long enough; turn you northward; and command the people, saying: you are to pass through the border of your brothers the children of Esau, who dwell in Seir, and they will be afraid of you; take good heed to yourselves therefore; do not contend with them, for I will not give you of their land, no, not so much as for the sole of the foot to tread on, because I have given Mount Seir to Esau for a possession; you shall buy food of them for money, that you may eat, and water for money, that you may drink; for the LORD your God has blessed you in all the work of your hand; these forty years the LORD your God has been with you; you have lacked nothing', 'turn_northward_commanded'),
    ('Deut 2:9 — and the LORD said to me: do not harass Moab nor contend with them in battle, for I will not give you of his land for a possession, because I have given Ar to the children of Lot for a possession', 'moab_spared_commanded'),
    ('Deut 2:13 — now rise up and get you over the brook Zered; and we went over the brook Zered', 'zered_crossing_commanded'),
    ('Deut 2:17-19 — and the LORD spoke to me, saying: you are this day to pass over Ar, the border of Moab; and when you come near over against the children of Ammon, do not harass them nor contend with them, for I will not give you of the land of the children of Ammon for a possession, because I have given it to the children of Lot for a possession', 'ammon_spared_commanded'),
    ('Deut 2:24-25 — rise up, take your journey, and pass over the valley of Arnon; behold, I have given into your hand Sihon the Amorite, king of Heshbon, and his land; begin to possess it, and contend with him in battle; this day will I begin to put the dread of you and the fear of you upon the peoples that are under the whole heaven, who, when they hear the report of you, shall tremble and be in anguish because of you (2:31: the LORD said to me: behold, I have begun to deliver up Sihon and his land before you; begin to possess, that you may inherit his land)', 'sihon_war_commanded'),
    ('Deut 2:34-35 — and we took all his cities at that time, and utterly destroyed every city, the men and the women and the little ones; we left none remaining; only the cattle we took for a prey to ourselves, with the spoil of the cities which we had taken', 'sihons_cities_devoted'),
    ('Deut 3:6-7 — and we utterly destroyed them, as we did to Sihon king of Heshbon, utterly destroying every city, the men and the women and the little ones; but all the cattle and the spoil of the cities we took for a prey to ourselves', 'ogs_cities_devoted'),
    ('Deut 3:21-22 — and I commanded Joshua at that time, saying: your eyes have seen all that the LORD your God has done to these two kings; so shall the LORD do to all the kingdoms to which you go over; you shall not fear them, for the LORD your God, He it is who fights for you', 'joshua_encouraged'),
    ('Deut 3:23-26 — and I besought the LORD at that time, saying: O Lord GOD, You have begun to show Your servant Your greatness and Your strong hand; for what god is there in heaven or on earth that can do according to Your works and according to Your mighty acts; let me go over, I pray, and see the good land that is beyond the Jordan, that goodly hill country and Lebanon; but the LORD was wroth with me for your sakes and did not hear me; and the LORD said to me: let it suffice you; speak no more to Me of this matter', 'moses_besought'),
]
CLOSES = "five, none a tape line: the commission's debit on Moses CLOSED BY ITS RUN inside the daemon (27:22-23 — the register seat Num 27:22 CLOSE); the four supplied debits on Israel CLOSED AT ONCE BY A PRIOR RUN inside the daemon (Num 12:16; 21:10-13; 21:10-13; 21:24-25 — the tape's earlier lines); see_the_land_from_abarim OPEN to Deuteronomy 34:1-4; the two DISAGREES rows OPEN"

# the exam's persons through the two case kinds: (kind, person, cell, ask, the shelf's citation)
PERSONS = [
    ('judges_case', 'the-hearer', 'judges', 'hear', 'Sanhedrin 7b:14 — the exam\'s row hear'),
    ('judges_case', 'the-righteous-judge', 'judges', 'judge_righteously', 'Sanhedrin 7a:17 — the exam\'s row judge_righteously'),
    ('judges_case', 'the-befriended', 'judges', 'no_faces', 'Sanhedrin 7b:18; Mishnah Sanhedrin 3:4-5 — the exam\'s row no_faces'),
    ('judges_case', 'the-peruta', 'judges', 'small_and_great', 'Sanhedrin 8a:2 — the exam\'s row small_and_great'),
    ('judges_case', 'the-gatherer-of-words', 'judges', 'no_fear', 'Sanhedrin 7a:16 — the exam\'s row no_fear'),
    ('judges_case', 'the-mountain-piercer', 'judges', 'the_judgment_is_gods', 'Sanhedrin 6b:3 — the exam\'s row the_judgment_is_gods'),
    ('judges_case', 'the-hard-matter', 'judges', 'the_hard_matter', 'Sifrei Devarim 17:7 — the exam\'s row the_hard_matter'),
    ('judges_case', 'the-convert', 'judges', 'the_stranger', 'Yevamot 47a:7 — the exam\'s row the_stranger'),
    ('judges_case', 'the-mediator', 'judges', 'the_compromise', 'Sanhedrin 6b:1-15 — the exam\'s row the_compromise'),
    ('judges_case', 'the-refuser-before-hearing', 'judges', 'the_refusal_before_hearing', 'Sanhedrin 6b:12 — the exam\'s row the_refusal_before_hearing'),
    ('judges_case', 'the-perverter', 'judges', 'the_perverting_judge', 'Sifra Kedoshim 4:1; Sanhedrin 7a:18 — the exam\'s row the_perverting_judge'),
    ('judges_case', 'the-money-court', 'judges', 'money_and_capital', 'Mishnah Sanhedrin 4:1 — the exam\'s row money_and_capital'),
    ('judges_case', 'the-three', 'judges', 'the_court_of_three', 'Mishnah Sanhedrin 1:1, 3:1 — the exam\'s row the_court_of_three'),
    ('judges_case', 'the-deliberate', 'judges', 'be_deliberate', 'Pirkei Avot 1:1 — the exam\'s row be_deliberate'),
    ('judges_case', 'the-counted-officers', 'judges', 'the_count', 'Sanhedrin 18a:3 — the exam\'s row the_count'),
    ('judges_case', 'the-seven-sought', 'judges', 'the_qualities', 'Sifrei Devarim 15:2; Eruvin 100b:18 — the exam\'s row the_qualities'),
    ('speech_case', 'the-dated-speech', 'frame', 'the_date', 'Rosh Hashanah 2b:11 — the exam\'s row the_date'),
    ('speech_case', 'the-received-rules', 'frame', 'the_receipt_of_the_rules', 'Sifrei Devarim 2:8 — the exam\'s row the_receipt_of_the_rules'),
    ('speech_case', 'the-askers', 'spies', 'the_asking', 'Sotah 34b:3 — the exam\'s row the_asking'),
    ('speech_case', 'the-little-ones', 'spies', 'the_little_ones', 'Numbers 14:31 — the exam\'s row the_little_ones'),
    ('speech_case', 'the-excepted', 'spies', 'the_exceptions', 'Numbers 14:24, 30 — the exam\'s row the_exceptions'),
    ('speech_case', 'the-harasser-of-moab', 'bypass', 'harassing_permitted', 'Horayot 10b:19 — the exam\'s row harassing_permitted'),
    ('speech_case', 'the-buyer-from-esau', 'bypass', 'forty_years_lacking_nothing', 'Exodus 16:35 — the exam\'s row forty_years_lacking_nothing'),
    ('speech_case', 'the-thirty-eight', 'bypass', 'the_men_of_war_consumed', 'Taanit 30b:12 — the exam\'s row the_men_of_war_consumed'),
    ('speech_case', 'the-messengers', 'sihon_og', 'the_messengers', 'Numbers 21:22 — the exam\'s row the_messengers'),
    ('speech_case', 'the-sixty', 'sihon_og', 'the_sixty_cities', 'Arakhin 32b:6 — the exam\'s row the_sixty_cities'),
    ('speech_case', 'the-bed', 'sihon_og', 'ogs_bed', 'Mishnah Kelim 17:9 — the exam\'s row ogs_bed'),
    ('speech_case', 'the-divided-east', 'east', 'the_division', 'Numbers 32:33 — the exam\'s row the_division'),
    ('speech_case', 'the-armed', 'east', 'the_charge_to_the_tribes', 'Joshua 1:15 — the exam\'s row the_charge_to_the_tribes'),
    ('speech_case', 'the-named-lord', 'plea', 'the_names', 'Sifrei Devarim 27:4 — the exam\'s row the_names'),
    ('speech_case', 'the-temple-mountain', 'plea', 'lebanon', 'Gittin 56b:1 — the exam\'s row lebanon'),
    ('speech_case', 'the-urim', 'commission', 'the_urim', 'Yoma 73b:3 — the exam\'s row the_urim'),
    ('speech_case', 'the-honored', 'commission', 'the_honor', 'Bava Batra 75a:8 — the exam\'s row the_honor'),
]

def scene():
    """THE SCENE — the exam's rows replayed on the world engine (the exodus epoch): the exam's persons through the two case kinds — the judges'
    charge clause by clause, the courts, the frame, the spies, the bypass, Sihon and Og, the east, the plea, the commission."""
    with contextlib.redirect_stdout(io.StringIO()):
        w = WE.World(era='Deut 1:1-3:29 with Num 27:12-23: the opening speech on the shelf — Sanhedrin, Rosh Hashanah, Sotah, Bava Kamma, Horayot, Kiddushin, Arakhin, Gittin on the engine (the exodus epoch)', epoch='exodus')
        w.laws = [law_opening_speech]
        w.advance(w.clock.day_in('exodus', 40, 11, 1))
        # THE DAEMON GATE READS LITERAL SUBMITS ONLY (the refuge runner's lesson, 2026-09-13) — the thirty-three persons typed out from PERSONS
        w.submit({'kind': 'judges_case', 'subject': 'the-hearer', 'person': 'the-hearer', 'cell': 'judges', 'ask': 'hear', 'case_source': "Sanhedrin 7b:14 — the exam's row hear"})
        w.submit({'kind': 'judges_case', 'subject': 'the-righteous-judge', 'person': 'the-righteous-judge', 'cell': 'judges', 'ask': 'judge_righteously', 'case_source': "Sanhedrin 7a:17 — the exam's row judge_righteously"})
        w.submit({'kind': 'judges_case', 'subject': 'the-befriended', 'person': 'the-befriended', 'cell': 'judges', 'ask': 'no_faces', 'case_source': "Sanhedrin 7b:18; Mishnah Sanhedrin 3:4-5 — the exam's row no_faces"})
        w.submit({'kind': 'judges_case', 'subject': 'the-peruta', 'person': 'the-peruta', 'cell': 'judges', 'ask': 'small_and_great', 'case_source': "Sanhedrin 8a:2 — the exam's row small_and_great"})
        w.submit({'kind': 'judges_case', 'subject': 'the-gatherer-of-words', 'person': 'the-gatherer-of-words', 'cell': 'judges', 'ask': 'no_fear', 'case_source': "Sanhedrin 7a:16 — the exam's row no_fear"})
        w.submit({'kind': 'judges_case', 'subject': 'the-mountain-piercer', 'person': 'the-mountain-piercer', 'cell': 'judges', 'ask': 'the_judgment_is_gods', 'case_source': "Sanhedrin 6b:3 — the exam's row the_judgment_is_gods"})
        w.submit({'kind': 'judges_case', 'subject': 'the-hard-matter', 'person': 'the-hard-matter', 'cell': 'judges', 'ask': 'the_hard_matter', 'case_source': "Sifrei Devarim 17:7 — the exam's row the_hard_matter"})
        w.submit({'kind': 'judges_case', 'subject': 'the-convert', 'person': 'the-convert', 'cell': 'judges', 'ask': 'the_stranger', 'case_source': "Yevamot 47a:7 — the exam's row the_stranger"})
        w.submit({'kind': 'judges_case', 'subject': 'the-mediator', 'person': 'the-mediator', 'cell': 'judges', 'ask': 'the_compromise', 'case_source': "Sanhedrin 6b:1-15 — the exam's row the_compromise"})
        w.submit({'kind': 'judges_case', 'subject': 'the-refuser-before-hearing', 'person': 'the-refuser-before-hearing', 'cell': 'judges', 'ask': 'the_refusal_before_hearing', 'case_source': "Sanhedrin 6b:12 — the exam's row the_refusal_before_hearing"})
        w.submit({'kind': 'judges_case', 'subject': 'the-perverter', 'person': 'the-perverter', 'cell': 'judges', 'ask': 'the_perverting_judge', 'case_source': "Sifra Kedoshim 4:1; Sanhedrin 7a:18 — the exam's row the_perverting_judge"})
        w.submit({'kind': 'judges_case', 'subject': 'the-money-court', 'person': 'the-money-court', 'cell': 'judges', 'ask': 'money_and_capital', 'case_source': "Mishnah Sanhedrin 4:1 — the exam's row money_and_capital"})
        w.submit({'kind': 'judges_case', 'subject': 'the-three', 'person': 'the-three', 'cell': 'judges', 'ask': 'the_court_of_three', 'case_source': "Mishnah Sanhedrin 1:1, 3:1 — the exam's row the_court_of_three"})
        w.submit({'kind': 'judges_case', 'subject': 'the-deliberate', 'person': 'the-deliberate', 'cell': 'judges', 'ask': 'be_deliberate', 'case_source': "Pirkei Avot 1:1 — the exam's row be_deliberate"})
        w.submit({'kind': 'judges_case', 'subject': 'the-counted-officers', 'person': 'the-counted-officers', 'cell': 'judges', 'ask': 'the_count', 'case_source': "Sanhedrin 18a:3 — the exam's row the_count"})
        w.submit({'kind': 'judges_case', 'subject': 'the-seven-sought', 'person': 'the-seven-sought', 'cell': 'judges', 'ask': 'the_qualities', 'case_source': "Sifrei Devarim 15:2; Eruvin 100b:18 — the exam's row the_qualities"})
        w.submit({'kind': 'speech_case', 'subject': 'the-dated-speech', 'person': 'the-dated-speech', 'cell': 'frame', 'ask': 'the_date', 'case_source': "Rosh Hashanah 2b:11 — the exam's row the_date"})
        w.submit({'kind': 'speech_case', 'subject': 'the-received-rules', 'person': 'the-received-rules', 'cell': 'frame', 'ask': 'the_receipt_of_the_rules', 'case_source': "Sifrei Devarim 2:8 — the exam's row the_receipt_of_the_rules"})
        w.submit({'kind': 'speech_case', 'subject': 'the-askers', 'person': 'the-askers', 'cell': 'spies', 'ask': 'the_asking', 'case_source': "Sotah 34b:3 — the exam's row the_asking"})
        w.submit({'kind': 'speech_case', 'subject': 'the-little-ones', 'person': 'the-little-ones', 'cell': 'spies', 'ask': 'the_little_ones', 'case_source': "Numbers 14:31 — the exam's row the_little_ones"})
        w.submit({'kind': 'speech_case', 'subject': 'the-excepted', 'person': 'the-excepted', 'cell': 'spies', 'ask': 'the_exceptions', 'case_source': "Numbers 14:24, 30 — the exam's row the_exceptions"})
        w.submit({'kind': 'speech_case', 'subject': 'the-harasser-of-moab', 'person': 'the-harasser-of-moab', 'cell': 'bypass', 'ask': 'harassing_permitted', 'case_source': "Horayot 10b:19 — the exam's row harassing_permitted"})
        w.submit({'kind': 'speech_case', 'subject': 'the-buyer-from-esau', 'person': 'the-buyer-from-esau', 'cell': 'bypass', 'ask': 'forty_years_lacking_nothing', 'case_source': "Exodus 16:35 — the exam's row forty_years_lacking_nothing"})
        w.submit({'kind': 'speech_case', 'subject': 'the-thirty-eight', 'person': 'the-thirty-eight', 'cell': 'bypass', 'ask': 'the_men_of_war_consumed', 'case_source': "Taanit 30b:12 — the exam's row the_men_of_war_consumed"})
        w.submit({'kind': 'speech_case', 'subject': 'the-messengers', 'person': 'the-messengers', 'cell': 'sihon_og', 'ask': 'the_messengers', 'case_source': "Numbers 21:22 — the exam's row the_messengers"})
        w.submit({'kind': 'speech_case', 'subject': 'the-sixty', 'person': 'the-sixty', 'cell': 'sihon_og', 'ask': 'the_sixty_cities', 'case_source': "Arakhin 32b:6 — the exam's row the_sixty_cities"})
        w.submit({'kind': 'speech_case', 'subject': 'the-bed', 'person': 'the-bed', 'cell': 'sihon_og', 'ask': 'ogs_bed', 'case_source': "Mishnah Kelim 17:9 — the exam's row ogs_bed"})
        w.submit({'kind': 'speech_case', 'subject': 'the-divided-east', 'person': 'the-divided-east', 'cell': 'east', 'ask': 'the_division', 'case_source': "Numbers 32:33 — the exam's row the_division"})
        w.submit({'kind': 'speech_case', 'subject': 'the-armed', 'person': 'the-armed', 'cell': 'east', 'ask': 'the_charge_to_the_tribes', 'case_source': "Joshua 1:15 — the exam's row the_charge_to_the_tribes"})
        w.submit({'kind': 'speech_case', 'subject': 'the-named-lord', 'person': 'the-named-lord', 'cell': 'plea', 'ask': 'the_names', 'case_source': "Sifrei Devarim 27:4 — the exam's row the_names"})
        w.submit({'kind': 'speech_case', 'subject': 'the-temple-mountain', 'person': 'the-temple-mountain', 'cell': 'plea', 'ask': 'lebanon', 'case_source': "Gittin 56b:1 — the exam's row lebanon"})
        w.submit({'kind': 'speech_case', 'subject': 'the-urim', 'person': 'the-urim', 'cell': 'commission', 'ask': 'the_urim', 'case_source': "Yoma 73b:3 — the exam's row the_urim"})
        w.submit({'kind': 'speech_case', 'subject': 'the-honored', 'person': 'the-honored', 'cell': 'commission', 'ask': 'the_honor', 'case_source': "Bava Batra 75a:8 — the exam's row the_honor"})
    n = lambda eid, eff: len([e for e in w.entity(eid).ledger if e['effect'] == eff])
    tset = len([l for l in w.log if l[0] == 'TIMER-SET']); tfire = len([l for l in w.log if l[0] == 'TIMER-FIRE']); tcan = len([l for l in w.log if l[0] == 'TIMER-CANCEL'])
    closes = len([e for ent in w.entities.values() for e in ent.ledger if e.get('closed_by')])
    return (tuple(n(p, 'accepted') + n(p, 'exempt') + n(p, 'judgment_perverted') for _, p, _, _, _ in PERSONS), (n('the-perverter', 'judgment_perverted'), n('the-refuser-before-hearing', 'exempt'), n('the-excepted', 'exempt'), n('the-harasser-of-moab', 'exempt')), (tset, tfire, tcan, len(w.timers)), len(w.entities), closes), w
SCENE, _W = scene()
# THE PREDICTION (typed before the first run — the scratchpad's deu_scene_predict.py, run BEFORE this runner existed): every exam person written once;
# the perverter's judgment_perverted, the refuser's exempt, the excepted's exempt, Moab's harasser's exempt each ONE; no timer; ENTITIES the thirty-three persons; CLOSES 0.
SCENE_PREDICTED = ((1,) * 33, (1, 1, 1, 1), (0, 0, 0, 0), 33, 0)
assert SCENE == SCENE_PREDICTED, ('THE DEUTERONOMY WALK: the scene moved from its prediction', SCENE, SCENE_PREDICTED)


def narrative():
    """THE DEUTERONOMY WALK 1b (2026-09-15): the span's own acts AS HISTORY — the commission's four lines at the counter's day (40, 6, 1) after
    the daughters' four; the FORWARD marker at Deut 1:1 (40, 11, 1) and the frame's line; the RETROGRADE markers at 1:6 (2, 2, 20), 1:9 (the court's
    founding day) and 2:2 (40, 6, 1) with the eleven supplied lines dated by them — on a world with this runner's daemon: 20 writes (the sixteen
    lines' twenty effects — the four supplied debits written and closed by the daemon's own hand), no timer, EIGHT entities (Israel, Moses, the
    court, Edom, the Moabites, the sons of Ammon, the Amorite, Joshua), the counter at (11, 1), FIVE closes, no row. Recorded by the sequential run's
    recorder and stitched onto the tape (the markers the stitcher's rows). Not a graded cell: the tuple below is a tripwire typed from the design."""
    with contextlib.redirect_stdout(io.StringIO()):
        w = WE.World(era='Deut 1:1-3:29 with Num 27:12-23 on the tape — the commission, the frame, the acts told only in the retelling (the exodus epoch)', epoch='exodus')
        w.laws = [law_opening_speech]
        w.advance(w.clock.day_in('exodus', 40, 6, 1))
        # THE DAEMON GATE READS LITERAL SUBMITS ONLY — the sixteen lines typed out; no field named `until` or `due` (the stitcher re-bases those as scene-clock days)
        w.submit({'kind': 'moses_told_to_ascend_abarim', 'subject': 'moses', 'mountain': 'Abarim', 'land': 'the land given to the children of Israel', 'sentence': 'Meribah (20:12)', 'case_source': LINES[0][0]})
        w.submit({'kind': 'a_shepherd_asked', 'subject': 'moses', 'plea': 'a man over the congregation, that they be not as sheep without a shepherd', 'case_source': LINES[1][0]})
        w.submit({'kind': 'joshua_commission_commanded', 'subject': 'moses', 'successor': 'joshua', 'priest': 'eleazar', 'urim': 'the judgment of the Urim', 'case_source': LINES[2][0]})
        w.submit({'kind': 'joshua_commissioned', 'subject': 'joshua', 'hand': 'two hands laid for the one commanded', 'honor': 'some of Moses\' honor', 'receipt': 'as the LORD commanded him', 'case_source': LINES[3][0]})
        w.marker('Deut 1:1', w.clock.day_in('exodus', 40, 11, 1), value='the speech\'s date (1:3) — the number reader [40, 11, 1]; the FORWARD marker at the book\'s first verse')
        w.submit({'kind': 'speech_opened', 'subject': 'israel', 'places': 11, 'date': [40, 11, 1], 'after': 'Sihon and Og', 'case_source': LINES[4][0]})
        w.marker('Deut 1:6', w.clock.day_in('exodus', 2, 2, 20), value='the departure from Horeb told — dated at the march (10:11): RETROGRADE', placement='reading_placed')
        w.submit({'kind': 'horeb_departure_commanded', 'subject': 'israel', 'regions': 7, 'closed_by': 'Num 12:16', 'case_source': LINES[5][0]})
        w.marker('Deut 1:9', w.clock.day_in('exodus', 1, 2, 16), value='the judges charged — dated at the court\'s founding (Exodus 18:25-26): RETROGRADE', placement='reading_placed')
        w.submit({'kind': 'judges_charged', 'subject': 'the-court', 'clauses': 6, 'case_source': LINES[6][0]})
        w.marker('Deut 2:2', w.clock.day_in('exodus', 40, 6, 1), value='the bypass and the plea told — dated at the departure from Mount Hor (21:4): RETROGRADE', placement='reading_placed')
        w.submit({'kind': 'turn_northward_commanded', 'subject': 'israel', 'bar': 'edom', 'grant': 'mount_seir', 'purchase': 'food and water for money', 'closed_by': 'Num 21:10-13', 'case_source': LINES[7][0]})
        w.submit({'kind': 'moab_spared_commanded', 'subject': 'the-moabites', 'bar': 'battle', 'grant': 'ar', 'case_source': LINES[8][0]})
        w.submit({'kind': 'zered_crossing_commanded', 'subject': 'israel', 'closed_by': 'Num 21:10-13', 'case_source': LINES[9][0]})
        w.submit({'kind': 'ammon_spared_commanded', 'subject': 'the-sons-of-ammon', 'bar': 'harassing and battle', 'grant': 'the land of the sons of Ammon', 'case_source': LINES[10][0]})
        w.submit({'kind': 'sihon_war_commanded', 'subject': 'israel', 'dread': 'this day I will begin', 'closed_by': 'Num 21:24-25', 'case_source': LINES[11][0]})
        w.submit({'kind': 'sihons_cities_devoted', 'subject': 'the-amorite', 'cities': 'every city', 'spoil': 'the cattle and the spoil taken', 'case_source': LINES[12][0]})
        w.submit({'kind': 'ogs_cities_devoted', 'subject': 'the-amorite', 'cities': 60, 'spoil': 'the cattle and the spoil taken', 'case_source': LINES[13][0]})
        w.submit({'kind': 'joshua_encouraged', 'subject': 'joshua', 'seen': 'the two kings', 'promise': 'He fights for you', 'case_source': LINES[14][0]})
        w.submit({'kind': 'moses_besought', 'subject': 'moses', 'plea': 'let me go over and see the good land', 'answer': 'refused — let it suffice you', 'case_source': LINES[15][0]})
    writes = len([l for l in w.log if l[0] == 'WRITE'])
    closes = len([e for ent in w.entities.values() for e in ent.ledger if e.get('closed_by')])
    rows = len([l for l in w.log if l[0] == 'ROW'])
    dated = len([l for l in w.log if l[0] == 'EVENT' and l[2].get('dated') is not None])
    return (writes, len([l for l in w.log if l[0] == 'TIMER-SET']), len(w.entities), w.clock.eras['exodus'].date(w.clock.day)[1:], closes, rows, len(w.tables['population']), dated), w


NARRATIVE, _WN = narrative()
NARRATIVE_PREDICTED = (20, 0, 8, (11, 1), 5, 0, 0, 11)   # DEUTERONOMY_WALK.md "Sitting 1b": 20 writes (Num 27's four + the speech's sixteen — the daemon's watches summed), no timer, EIGHT entities, the counter's day (11, 1), FIVE closes (the commission's by its run; the four by a prior run), no row, ELEVEN dated lines (the retrograde stretches')
assert NARRATIVE == NARRATIVE_PREDICTED, ('THE DEUTERONOMY WALK: the opening speech\'s narrative moved from its prediction', NARRATIVE, NARRATIVE_PREDICTED)
_isr = _WN.entity('israel').ledger
assert [(e['value'], e.get('open'), str(e.get('closed_by', ''))[:12]) for e in _isr if e['effect'] == 'commanded'] == [('journey_to_the_mountain_of_the_amorite', False, 'Num 12:16 — '), ('turn_northward', False, 'Num 21:10-13'), ('cross_the_brook_zered', False, 'Num 21:10-13'), ('begin_to_possess_sihons_land', False, 'Num 21:24-25')], [(e['value'], e.get('open'), e.get('closed_by')) for e in _isr if e['effect'] == 'commanded']   # THE FOUR SUPPLIED DEBITS each CLOSED BY A PRIOR RUN, the closer's verse the tape's earlier line
assert [e['value'] for e in _WN.entity('moses').ledger if e['effect'] == 'commanded'] == ['see_the_land_from_abarim', 'commission_joshua_before_eleazar'] and [e.get('open') for e in _WN.entity('moses').ledger if e['effect'] == 'commanded'] == [True, False], _WN.entity('moses').ledger   # the ascent OPEN to Deuteronomy 34; the commission CLOSED by its run
assert [ex.date(l[2]['dated']) for l in _WN.log if l[0] == 'EVENT' and l[2].get('dated') is not None for ex in [_WN.clock.eras['exodus']]] == [(2, 2, 20), (1, 2, 16)] + [(40, 6, 1)] * 9, 'the eleven supplied lines dated by their markers'


# =====================================================================
# Motion 2 — THE TEST DATA: the answer sheet's rows (the docket's LAW rows and the cells' asks).
# =====================================================================
CASES = [
    # F0 — the_commission
    ('Num 27:12 — the_mountain', lambda: the_commission({'ask': 'the_mountain'}, DATA), "the mountain of Abarim (27:12) — Nebo and Pisgah its other names (34:1 one mountain): Deuteronomy 3:27's Pisgah the retelling of this command, READ BACK"),
    ('Num 27:14 — the_sentence_cited', lambda: the_commission({'ask': 'the_sentence_cited'}, DATA), "Meribah cited (27:14) — 20:12's sentence pointed to, the barred entry on Moses OPEN read (CK by CALL); no second write"),
    ('Num 27:15-17 — the_shepherd', lambda: the_commission({'ask': 'the_shepherd'}, DATA), "a shepherd asked (27:15-17) — plea_made on Moses: the successor asked before he is named; 16:22's phrase at its second seat"),
    ('Num 27:18, 23 — the_hand_laid', lambda: the_commission({'ask': 'the_hand_laid'}, DATA), "the hand laid (27:18, 23) — one hand commanded, two laid (the Sifrei 141): invested_office on Joshua, the ordination's form"),
    ('Num 27:20 — the_honor', lambda: the_commission({'ask': 'the_honor'}, DATA), 'of your honor (27:20) — not all of it: the sun and the moon (Bava Batra 75a:8) — DATA'),
    ('Num 27:21 — the_urim', lambda: the_commission({'ask': 'the_urim'}, DATA), "the judgment of the Urim (27:21) — final (C2 by CALL: Yoma 73b:3); Joshua under Eleazar's inquiry, not Moses' face to face"),
    ('Num 27:22-23 — the_receipt', lambda: the_commission({'ask': 'the_receipt'}, DATA), "the receipt (27:22-23) — 'as the LORD commanded him': the commission's debit closed by its run, the register seat Num 27:22 CLOSE"),
    ('Num 27:12-13 — the_debit', lambda: the_commission({'ask': 'the_debit'}, DATA), 'the debit (27:12) — see the land from Abarim: commanded on Moses, OPEN to Deuteronomy 34:1-4; 3:27 reads it back with Pisgah'),
    # F1 — the_frame
    ('Deut 1:1 — the_words', lambda: the_frame({'ask': 'the_words'}, DATA), "the words (1:1) — the eleven places the rebuke's sins (the Sifrei 1; Onkelos writes them in); Di-zahab the calf's gold (Berakhot 32a:7): the frame's DATA"),
    ('Deut 1:3 — the_date', lambda: the_frame({'ask': 'the_date'}, DATA), "the date (1:3) — [40, 11, 1] by the number reader; the era the exodus's by the taught verbal analogy with 33:38 (Rosh Hashanah 2b:11; JO by CALL): the FORWARD marker at Deut 1:1"),
    ('Deut 1:3 — the_receipt_of_the_rules', lambda: the_frame({'ask': 'the_receipt_of_the_rules'}, DATA), "the receipt of the rules (1:3) — 'according to all' the hermeneutic rules (the Sifrei 2:8): the register seat ACT, the frame the readback checkpoint reads"),
    ('Deut 1:2 — the_eleven_days', lambda: the_frame({'ask': 'the_eleven_days'}, DATA), "eleven days (1:2) — [11] by the parser; the journey hastened (the Sifrei 2:1-3): the rebuke's measure"),
    ('Deut 1:4 — after_sihon', lambda: the_frame({'ask': 'after_sihon'}, DATA), "after Sihon (1:4) — the order of the fortieth year: Aaron's death, Arad, the departure, Sihon, the speech (JO by CALL; Rosh Hashanah 2b:13)"),
    ('Deut 1:5 — began_to_expound', lambda: the_frame({'ask': 'began_to_expound'}, DATA), "began to expound (1:5) — the expound-root's two Torah seats (27:8's 'clearly' the other); the third teaching (Zevachim 115b:17); the king's reading (Sotah 7:8)"),
    ('Deut 1:1-5 — the_write', lambda: the_frame({'ask': 'the_write'}, DATA), "the write (1:1-5) — torah_expounded on Israel at (40, 11, 1): the book's one act of its own day"),
    # F2 — the_officers_and_the_judges
    ('Deut 1:6-8 — the_horeb_command', lambda: the_officers_and_the_judges({'ask': 'the_horeb_command'}, DATA), "the Horeb command (1:6-8) — told only here: commanded on Israel dated (2, 2, 20), CLOSED by the prior run Num 12:16 (the arrival in Paran); 'go in and possess' a reference to the land granted (Genesis 15:18)"),
    ('Deut 1:7 — the_regions', lambda: the_officers_and_the_judges({'ask': 'the_regions'}, DATA), "the regions (1:7) — the seven kinds every tribe's portion held (Bava Kamma 81b:6); the Euphrates great by nearness (Shevuot 47b:6); the promised extents by CALL: DATA"),
    ('Deut 1:9-12 — the_burden', lambda: the_officers_and_the_judges({'ask': 'the_burden'}, DATA), "the burden (1:9-12) — 11:14's 'I alone' retold; the seventy with Moses the seventy-one (BH by CALL; Sanhedrin 16b:18, 17a:3)"),
    ('Deut 1:11 — the_blessing', lambda: the_officers_and_the_judges({'ask': 'the_blessing'}, DATA), "the blessing (1:11) — [1000]: Moses' own beside God's (the Sifrei 11:1); a priest may not add it (Rosh Hashanah 28b:10): DATA"),
    ('Deut 1:13, 15 — the_qualities', lambda: the_officers_and_the_judges({'ask': 'the_qualities'}, DATA), "the qualities (1:13, 15) — seven asked, three found (the Sifrei 15:2): the discerning not found (Eruvin 100b:18); Jethro's four by CALL: a DATA checklist"),
    ('Deut 1:15 — the_grains', lambda: the_officers_and_the_judges({'ask': 'the_grains'}, DATA), "the grains (1:15) — [100, 50, 10] with the plural 'thousands' a noun: the four grains of Exodus 18:21 by CALL; the appointment read back, TURNED"),
    ('Deut the_count — the_count', lambda: the_officers_and_the_judges({'ask': 'the_count'}, DATA), "the count — 78,600 on the round six hundred thousand (ES by CALL; Sanhedrin 18a), 79,064 on the census's exact 603,550 by integer division (CB by CALL; the Sifrei 15:4's rounding rule): two settings"),
    ('Deut 1:15 — the_officers', lambda: the_officers_and_the_judges({'ask': 'the_officers'}, DATA), "the officers (1:15) — the strap (the Sifrei 15:5; 2 Chronicles 19:11); Deuteronomy 16:18's second seat — every tribe, every city (Sanhedrin 16b:9-10)"),
    ('Deut 1:16-17 — the_charge', lambda: the_officers_and_the_judges({'ask': 'the_charge'}, DATA), "the charge (1:16-17) — the six clauses each one seat: judges_charged on the court, dated at the court's founding (1, 2, 16); the law in Moses' voice, the vows' class"),
    ('Deut 1:16 — hear', lambda: the_officers_and_the_judges({'ask': 'hear'}, DATA), "hear (1:16) — not one litigant without the other (Sanhedrin 7b:14); 'charged' with alacrity, the rod and the strap"),
    ('Deut 1:16 — judge_righteously', lambda: the_officers_and_the_judges({'ask': 'judge_righteously'}, DATA), "judge righteously (1:16) — the true judgment truly makes the Presence rest (Sanhedrin 7a:17); Leviticus 19:15's 'in righteousness' by CALL"),
    ('Deut 1:17 — no_faces', lambda: the_officers_and_the_judges({'ask': 'no_faces'}, DATA), 'no faces (1:17) — befriend / estrange disputed (Sanhedrin 7b:18); the kin and the haters off the bench (Mishnah Sanhedrin 3:4-5; 29a:11): the DATA row no_faces'),
    ('Deut 1:17 — small_and_great', lambda: the_officers_and_the_judges({'ask': 'small_and_great'}, DATA), 'the small and the great (1:17) — the peruta as the hundred maneh (Sanhedrin 8a:2); the order of hearing (8a:4-5)'),
    ('Deut 1:17 — no_fear', lambda: the_officers_and_the_judges({'ask': 'no_fear'}, DATA), 'no fear (1:17) — a term for gathering in (Sanhedrin 7a:16); the refusal before hearing only (6b:12; the Sifrei 17:4); the student not silent (6b:13)'),
    ('Deut 1:17 — the_judgment_is_gods', lambda: the_officers_and_the_judges({'ask': 'the_judgment_is_gods'}, DATA), "the judgment is God's (1:17) — pierce the mountain (Sanhedrin 6b:3); the unlawful judge's life (7a:18); before Whom (6b:14)"),
    ('Deut 1:17 — the_hard_matter', lambda: the_officers_and_the_judges({'ask': 'the_hard_matter'}, DATA), "the hard matter (1:17) — Exodus 18:26's status read (ES by CALL); Zelophehad's daughters the case (the Sifrei 17:7; ZL by CALL — the third form)"),
    ('Deut 1:16 — the_stranger', lambda: the_officers_and_the_judges({'ask': 'the_stranger'}, DATA), 'the stranger (1:16) — a convert before a court (Yevamot 47a:7)'),
    ('Deut 1:16 — a_man_excludes_the_minor', lambda: the_officers_and_the_judges({'ask': 'a_man_excludes_the_minor'}, DATA), 'a man excludes the minor (1:16 — the Sifrei 16:6)'),
    ('Deut 1:16 — the_gentile_litigant', lambda: the_officers_and_the_judges({'ask': 'the_gentile_litigant'}, DATA), "the gentile litigant — R. Ishmael's two rulings against Rabban Shimon ben Gamliel's one (the Sifrei 16:4): DATA"),
    ('Deut 1:17 — the_appointer', lambda: the_officers_and_the_judges({'ask': 'the_appointer'}, DATA), 'the appointer (1:17) — the clause addressed to the one who appoints (the Sifrei 17:1): DATA'),
    ('Deut 1:17 — the_compromise', lambda: the_officers_and_the_judges({'ask': 'the_compromise'}, DATA), "the compromise — three settings on 1:17's clause (Sanhedrin 6b:1-15; 32b:4-6): TWO VERDICT TABLES as DATA"),
    ('Deut 1:13 — the_al_tikrei', lambda: the_officers_and_the_judges({'ask': 'the_al_tikrei'}, DATA), "the al tikrei (1:13) — 'I will set them' read 'their guilt on your heads' (the Sifrei 13:6): the revocalization move"),
    ('Deut be_deliberate — be_deliberate', lambda: the_officers_and_the_judges({'ask': 'be_deliberate'}, DATA), "be deliberate (Avot 1:1) — the Sifrei 16:1 cites the Mishnah as 1:16's reading; the chain by CALL"),
    ('Deut money_and_capital — money_and_capital', lambda: the_officers_and_the_judges({'ask': 'money_and_capital'}, DATA), "money and capital (Mishnah Sanhedrin 4:1) — the ten differences (Sanhedrin 32a; the Sifrei 18:1); the majority's asymmetry by CALL"),
    ('Deut the_court_of_three — the_court_of_three', lambda: the_officers_and_the_judges({'ask': 'the_court_of_three'}, DATA), "the court of three (Mishnah Sanhedrin 1:1, 3:1-3) — the litigants' choice, the third by the two (Sanhedrin 23a:12); the disqualified by conduct (24b-26b); the sizes by CALL"),
    ('Deut the_perverting_judge — the_perverting_judge', lambda: the_officers_and_the_judges({'ask': 'the_perverting_judge'}, DATA), 'the perverting judge — the five effects (HO by CALL; Sanhedrin 7a:17-18): judgment_perverted'),
    ('shelf: Sanhedrin 6b:12 (Reish Lakish); 6b:11 (R. Shimon ben Menasya — the_refusal_before_hearing', lambda: the_officers_and_the_judges({'ask': 'the_refusal_before_hearing'}, DATA), "the refusal before hearing — permitted, not yet bound by 'you shall not be afraid' (Sanhedrin 6b:12): exempt"),
    ('Deut 1:18 — all_the_things', lambda: the_officers_and_the_judges({'ask': 'all_the_things'}, DATA), 'all the things (1:18) — the community warned as the judges were (Sanhedrin 8a:6)'),
    # F3 — the_spies_read_back
    ('Deut 1:22 — the_asking', lambda: the_spies_read_back({'ask': 'the_asking'}, DATA), "the asking (1:22) — the people's, against 13:2's 'send for yourself' (Sotah 34b:3; SL by CALL): the two tellings reconciled on the shelf — the readback row TURNED"),
    ('Deut 1:23 — the_twelve', lambda: the_spies_read_back({'ask': 'the_twelve'}, DATA), "the twelve (1:23) — [12, 1]: one per tribe by CALL; Joshua 4:2 and 3:12 the phrases' other seats"),
    ('Deut 1:24 — the_valley', lambda: the_spies_read_back({'ask': 'the_valley'}, DATA), "the valley (1:24) — Eshcol named after the cluster (SL by CALL); 'spied' the piel — Caleb's verb (Joshua 14:7; CK.DATA spy_verb by CALL)"),
    ('Deut 1:25 — good_is_the_land', lambda: the_spies_read_back({'ask': 'good_is_the_land'}, DATA), "good is the land (1:25) — 14:7's words, Joshua and Caleb's (the Sifrei 23:3); the retelling keeps the truth, drops 13:27's 'however' (Sotah 35a:2): SHORTENED"),
    ('Deut 1:27-28 — the_murmuring', lambda: the_spies_read_back({'ask': 'the_murmuring'}, DATA), "the murmuring (1:27-28) — two words (Shevuot 47b:5); the spies' words in the people's mouths, 'greater and taller than we' the plain sense of 13:31 (Sotah 35a:7): TURNED"),
    ('Deut 1:31 — the_carrying', lambda: the_spies_read_back({'ask': 'the_carrying'}, DATA), "the carrying (1:31) — as a man carries his son: Exodus 19:4's eagle the kin"),
    ('Deut 1:33 — the_pillar', lambda: the_spies_read_back({'ask': 'the_pillar'}, DATA), "the pillar (1:33) — Exodus 13:21's by REFERENCE: the tape's pillar_set line, read"),
    ('Deut 1:34-36 — the_oath', lambda: the_spies_read_back({'ask': 'the_oath'}, DATA), "the oath (1:34-36) — the verb 'swore' supplied (GR.DATA by CALL); sentence_pronounced read; Caleb's holding_owed OPEN read (SL by CALL): SHORTENED"),
    ('Deut the_exceptions — the_exceptions', lambda: the_spies_read_back({'ask': 'the_exceptions'}, DATA), 'the exceptions — Caleb, Joshua, the children (SL by CALL): exempt from the oath'),
    ('Deut 1:37 — the_bars_ground', lambda: the_spies_read_back({'ask': 'the_bars_ground'}, DATA), "the bar's ground (1:37) — 'for your sakes' against 20:12's 'because you did not believe': DISAGREES, an OPEN row; the tape's one entry stands"),
    ('Deut 1:38 — joshua_shall_go_in', lambda: the_spies_read_back({'ask': 'joshua_shall_go_in'}, DATA), "Joshua shall go in (1:38) — 14:30's exception EXPANDED with the inheriting (the effect's first seat; 3:28 and Joshua 1:6 after)"),
    ('Deut 1:39 — the_little_ones', lambda: the_spies_read_back({'ask': 'the_little_ones'}, DATA), "the little ones (1:39) — 14:31 VERBATIM for five tokens, then the children who know not good and evil added (Eden's four seats)"),
    ('Deut 1:40 — the_turn_back', lambda: the_spies_read_back({'ask': 'the_turn_back'}, DATA), "the turn back (1:40) — 14:25 retold with 'tomorrow' dropped; the debit's close at 21:4 read (SL by CALL): TURNED"),
    ('Deut 1:41-44 — the_presumption', lambda: the_spies_read_back({'ask': 'the_presumption'}, DATA), "the presumption (1:41-44) — presumed_to_go_up and defeated read back; 'as bees do', 'in Seir' EXPANDED; the receipt in the people's mouth a run citation (1:41 NONE)"),
    ('Deut 1:45 — the_weeping', lambda: the_spies_read_back({'ask': 'the_weeping'}, DATA), "the weeping (1:45) — a second weeping told only here, unheard (1:45 and 3:26 one phrase); 14:1's wept read: EXPANDED, no write"),
    ('Deut 1:46 — many_days_at_kadesh', lambda: the_spies_read_back({'ask': 'many_days_at_kadesh'}, DATA), "many days at Kadesh (1:46) — Seder Olam 8's nineteen years: DATA, no day moved"),
    ('Deut the_readback_table — the_readback_table', lambda: the_spies_read_back({'ask': 'the_readback_table'}, DATA), "the readback table — forty-two reference rows graded; the two DISAGREES rows open; every retold act's entry found on the running world (CA4)"),
    # F4 — the_bypass
    ('Deut 2:1-3 — the_turn', lambda: the_bypass({'ask': 'the_turn'}, DATA), "the turn (2:1-3) — told only here: commanded on Israel dated (40, 6, 1), CLOSED by the prior run Num 21:10-13; 'enough' the plural's second seat in the speech"),
    ('Deut 2:4-8 — esau', lambda: the_bypass({'ask': 'esau'}, DATA), 'Esau (2:4-8) — contending_barred and land_granted (Mount Seir) on Edom: the bar and the grant told only here (Kiddushin 18a:2; JS by CALL); the purchase a permission'),
    ('Deut 2:7 — forty_years_lacking_nothing', lambda: the_bypass({'ask': 'forty_years_lacking_nothing'}, DATA), "forty years lacking nothing (2:7) — [40]: the manna's forty years (ES by CALL; Exodus 16:35)"),
    ('Deut 2:8 — the_route', lambda: the_bypass({'ask': 'the_route'}, DATA), "the route (2:8) — Elath and Ezion-geber, the way of Moab's wilderness: the itinerary's stations by CALL; 21:4's Red Sea way the same road"),
    ('Deut 2:9 — moab', lambda: the_bypass({'ask': 'moab'}, DATA), "Moab (2:9) — contending_barred and land_granted (Ar) on the Moabites: the bar the a fortiori needed (Bava Kamma 38a:16; BK by CALL); Lot's elder daughter's people (MM by CALL)"),
    ('shelf: Horayot 10b:19 (R. Yochanan); Nazir 23b:11 — harassing_permitted', lambda: the_bypass({'ask': 'harassing_permitted'}, DATA), "harassing Moab — permitted, battle forbidden (Horayot 10b:19): exempt from the bar's reach; Ammon's bar reaches further"),
    ('Deut 2:10-12 — the_emim', lambda: the_bypass({'ask': 'the_emim'}, DATA), "the Emim and the Horites (2:10-12) — Genesis 14:5-6's peoples (PR and JS by CALL); 'as Israel did' the ink's pattern of title: the dispossessions DATA"),
    ('Deut 2:13-14 — the_zered', lambda: the_bypass({'ask': 'the_zered'}, DATA), "the Zered (2:13-14) — told only here: commanded on Israel cross_the_brook_zered, CLOSED by the prior run Num 21:10-13; [38] against the tape's years (the spies' return to the departure from Mount Hor)"),
    ('Deut 2:14-16 — the_men_of_war_consumed', lambda: the_bypass({'ask': 'the_men_of_war_consumed'}, DATA), "the men of war consumed (2:14-16) — the decree's timer FIRED at (40, 5, 9) read; the dying ceased (40, 5, 15) by CALL (Taanit 30b:12)"),
    ('Deut 2:17 — the_speech_resumed', lambda: the_bypass({'ask': 'the_speech_resumed'}, DATA), "the speech resumed (2:17) — 'SPOKE to me' the Bible's one seat: only after the last of that generation (Bava Batra 121b:1)"),
    ('Deut 2:17-19 — ammon', lambda: the_bypass({'ask': 'ammon'}, DATA), "Ammon (2:17-19) — contending_barred and land_granted on the sons of Ammon: not even harassed (Bava Kamma 38b:6); 21:24's strong border the bar's reason (CK.DATA by CALL); the one new party"),
    ('Deut 2:20-23 — the_avvim', lambda: the_bypass({'ask': 'the_avvim'}, DATA), "the Avvim (2:20-23) — the Caphtorim's dispossession, Genesis 10:14's people (Chullin 60b:11): the dispossessions DATA"),
    ('Deut 2:24-25 — sihon_commanded', lambda: the_bypass({'ask': 'sihon_commanded'}, DATA), "Sihon commanded (2:24-25) — told only here: commanded on Israel, CLOSED by the prior run Num 21:24-25; the dread's row the sun for Moses (Avodah Zarah 25a; Taanit 20a): DATA"),
    # F5 — sihon_and_og
    ('Deut 2:26-28 — the_messengers', lambda: sihon_and_og({'ask': 'the_messengers'}, DATA), "the messengers (2:26-28) — nine tokens for 21:22's seventeen: SHORTENED; Kedemoth and 'words of peace' told only here"),
    ('Deut 2:29 — the_edom_disagreement', lambda: sihon_and_og({'ask': 'the_edom_disagreement'}, DATA), "the Edom disagreement (2:29) — 'as the sons of Esau did for me' against 20:18-21's refusal: DISAGREES, the chukat row's two arms (CK by CALL), an OPEN row"),
    ('Deut 2:30 — the_hardening', lambda: sihon_and_og({'ask': 'the_hardening'}, DATA), "the hardening (2:30) — told only here in Pharaoh's verbs (the exodus story by REFERENCE); sihon's refused read (CK by CALL): EXPANDED"),
    ('Deut 2:32-33 — jahaz', lambda: sihon_and_og({'ask': 'jahaz'}, DATA), "Jahaz (2:32-33) — eight tokens for 21:23's twenty: SHORTENED; 21:24's smiting the run"),
    ('Deut 2:33 — the_written_and_read', lambda: sihon_and_og({'ask': 'the_written_and_read'}, DATA), "written 'his son', read 'his sons' (2:33) — the DB's eleven tokens against the store's twelve; Onkelos plural: the reading's find, DATA"),
    ('Deut 2:34-35; 3:6-7 — the_ban', lambda: sihon_and_og({'ask': 'the_ban'}, DATA), "the ban (2:34-35; 3:6-7) — told only in the retelling: destroyed on the Amorite twice (21:24-25, 21:35 say smote and possessed); 15:16's status read; the cherem law forward"),
    ('Deut 2:36-37 — aroer_to_gilead', lambda: sihon_and_og({'ask': 'aroer_to_gilead'}, DATA), "Aroer to Gilead (2:36-37) — the border respected (2:37) against 21:24's strong (CK by CALL): EXPANDED"),
    ('Deut 3:1-3 — og_turned', lambda: sihon_and_og({'ask': 'og_turned'}, DATA), 'Og turned (3:1-3) — 21:33-35 with the persons shifted (we for they; to me for to Moses): TURNED, the five shifts computed; fear_not_promised on Moses read'),
    ('Deut 3:4-5 — the_sixty_cities', lambda: sihon_and_og({'ask': 'the_sixty_cities'}, DATA), "the sixty cities (3:4-5) — [60], Argob's; the walled cities from Joshua's days (Arakhin 32b:6; Megillah 10a:10); Leviticus 25:29's 'walled' learned here: DATA"),
    ('Deut 3:11 — ogs_bed', lambda: sihon_and_og({'ask': 'ogs_bed'}, DATA), "Og's bed (3:11) — [9, 4] by the cubit of a man (Kelim 17:9-10); the remnant of the Rephaim; Og's lore by CALL: DATA"),
    ('Deut 3:8-9 — hermon', lambda: sihon_and_og({'ask': 'hermon'}, DATA), "Hermon (3:8-9) — Sirion and Senir, the nations' names (Chullin 60b:14; Song 4:8): EXPANDED"),
    # F6 — the_east_and_the_charges
    ('Deut 3:12-13 — the_division', lambda: the_east_and_the_charges({'ask': 'the_division'}, DATA), "the division (3:12-13) — 32:33's three holdings read back, DIVIDED: half Gilead to the two, the rest and Bashan to the half tribe (thirty-six tokens for twenty-nine); the halves [1/2] by rule 30: EXPANDED"),
    ('Deut 3:14 — jair', lambda: the_east_and_the_charges({'ask': 'jair'}, DATA), "Jair (3:14) — 32:41 read back, EXPANDED (twenty-three tokens for eleven): Argob, the Geshurite and the Maacathite, 'to this day' told only here"),
    ('Deut 3:15 — machir', lambda: the_east_and_the_charges({'ask': 'machir'}, DATA), "Machir (3:15) — 32:40's 'Moses gave' in the first person: TURNED"),
    ('Deut 3:16-17 — the_borders', lambda: the_east_and_the_charges({'ask': 'the_borders'}, DATA), "the east's borders (3:16-17) — told only here: the Arnon's middle, the Jabbok, Chinnereth to the Salt Sea under Pisgah — DATA, no write"),
    ('Deut 3:18-20 — the_charge_to_the_tribes', lambda: the_east_and_the_charges({'ask': 'the_charge_to_the_tribes'}, DATA), "the charge to the tribes (3:18-20) — 32:20-24's condition in the first person with half Manasseh included: TURNED; the debit OPEN read (GR by CALL); 'until the LORD gives rest' Joshua 1:15's"),
    ('Deut 3:21-22 — joshuas_charge', lambda: the_east_and_the_charges({'ask': 'joshuas_charge'}, DATA), "Joshua's charge (3:21-22) — told only here: fear_not_promised on Joshua (21:34's effect at its second party); Joshua plene; Ai's run outside the Torah (the Sifrei 29:8-9)"),
    # F7 — the_plea
    ('Deut 3:23-26 — the_plea', lambda: the_plea({'ask': 'the_plea'}, DATA), 'the plea (3:23-26) — told only here: plea_made on Moses with the refusal in the value; the barred entry OPEN read; praise before the request (Berakhot 32a:32)'),
    ('Deut 3:24 — the_names', lambda: the_plea({'ask': 'the_names'}, DATA), "the names (3:24) — 'O Lord GOD' Abraham's and Moses'; 'Your greatness' the Sifrei 27:4's binyan av; 'Your strong hand' 1 Kings 8:42's: DATA"),
    ('Deut 3:25 — lebanon', lambda: the_plea({'ask': 'lebanon'}, DATA), "Lebanon (3:25) — the Temple (the Sifrei 6:2, 28:3; Gittin 56b:1); 1:7's Lebanon the region, this the house: DATA"),
    ('Deut 3:26 — the_refusal', lambda: the_plea({'ask': 'the_refusal'}, DATA), "the refusal (3:26) — 'let it suffice you' the singular's one seat, measure for measure for Korach's (Sotah 13b:13); 'did not hear' 1:45's phrase; the barred entry read"),
    ('Deut 3:27 — pisgah', lambda: the_plea({'ask': 'pisgah'}, DATA), "Pisgah (3:27) — 27:12's command read back with Pisgah for Abarim and the four directions in the third order: TURNED; the debit OPEN read"),
    ('Deut 3:28 — command_joshua', lambda: the_plea({'ask': 'command_joshua'}, DATA), "command Joshua (3:28) — the commission read back (Kiddushin 29a:14 — a galvanization for generations); 'he shall cause them to inherit' the effect's second seat: TURNED"),
    ('Deut 3:29 — beth_peor', lambda: the_plea({'ask': 'beth_peor'}, DATA), "Beth-peor (3:29) — the last camp by CALL (22:1; 36:13; Deuteronomy 34:1); 4:46 and 34:6 the valley's other seats: EXPANDED"),
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
    print('THE INK: integers %s; marked %s; the frames "said to me" %s, "spoke to me" %s; "at that time" %s; the case tokens %s' % (sorted(INTS.items()), MARKED, SAID_TO_ME, SPOKE_TO_ME, AT_THAT_TIME, CASE_KI))
    print('THE READBACK: %d rows — %s; the deltas: 1:39 prefix %d; 2:27 %d/%d; 2:32 %d/%d; 3:1-3 %d/%d shared %d shifts %d; 3:14 %d/%d; 3:12-13 %d/%d' % (len(READBACK), dict(RB_GRADES), VERBATIM_PREFIX, len(MSG_DEUT), len(MSG_NUM), len(JAHAZ_DEUT), len(JAHAZ_NUM), len(OG_D), len(OG_N), OG_SHARED, len(OG_SHIFT), len(JAIR_D), len(JAIR_N), len(DIV_D), len(DIV_N)))
    print('THE OFFICERS: the grains %s; the round %d; the exact %d of %d; the seven qualities asked %d found %d' % (DATA['the_officers_table']['value']['grains'], ES_JUDGES['v'], EXACT_COUNT, CENSUS_TOTAL, DATA['the_seven_qualities']['value']['asked'], DATA['the_seven_qualities']['value']['found']))
    print('THE SCENE on the bench: %s; the timers (set, fired, cancelled, pending) %s; entities %d; closes %d' % (SCENE[0], SCENE[2], SCENE[3], SCENE[4]))
    print('THE NARRATIVE: %s' % (NARRATIVE,))
    print('THE PARAMETER ROWS: ' + '; '.join('%s = %s' % (k, DATA[k]['value'] if k != 'the_readback' else '%d rows' % len(DATA[k]['value'])) for k in DATA) + ' (the other settings recorded in DATA)')
    if ok == len(CASES):
        print('\nTHE COMPILE OF THE OPENING SPEECH: the answer sheet REPRODUCED — %d/%d' % (ok, len(CASES)))
    sys.exit(0 if ok == len(CASES) else 1)

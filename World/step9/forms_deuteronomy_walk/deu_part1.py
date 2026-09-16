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

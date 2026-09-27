#!/usr/bin/env python3
# THE DEUTERONOMY WALK 17b: cold_run_persons_poor_court.py PART 1 derived — the head typed here; the generic helper block COPIED from the chapter 19-21 runner by content
# markers (HERE = … through def LEN — the parser exec, the DB, the phrase/lemma/diff helpers; W19/W20/W21 made W22, W23, W24, W25 and W); THE INK BLOCKS COPIED from the
# reading's own instrument ch22_ink.py by content markers — THREE blocks (the kin by computation over the four chapters; the kin re-scored, the twins diffed and the formulas
# over the Torah and the Bible; the frames), the store-, shelf- and Onkelos-bound lines DROPPED by name (10b's lesson 6 — the count read from the print); the counter's day,
# the one-database scans, and THE CALLEES' FACTS (typed in ch22_callees_facts.py from ch22_callees.out, ch22_callees2.out and ch22_callees3.out — read before any assert was
# typed). Asserted substitutions throughout. derive_ch19_part1.py's form over four chapters. RUN FROM THE REPO ROOT.
import subprocess, re, os, sys
ROOT = _ROOT
SP = os.path.dirname(os.path.abspath(__file__))
RWF = open(f'{ROOT}/World/step9/cold_run_refuge_war_family.py', encoding='utf-8').read()
INKB = open(f'{SP}/ch22_ink.py', encoding='utf-8').read()
FACTS = open(f'{SP}/ch22_callees_facts.py', encoding='utf-8').read()
assert FACTS.startswith('\n# ---- THE CALLEES\' FACTS'), 'the callees\' facts typed from the prints (ch22_callees_facts.py)'
HEAD = '''#!/usr/bin/env python3
# DEUTERONOMY 22:1-25:19 — THE LOST THING (your brother's ox or sheep straying, until your brother seeks it, you may not hide, his ass or his ox fallen), THE GARMENTS, THE
# NEST, THE PARAPET, THE MIXTURES AND THE TASSELS (a man's gear on a woman, the nest before you, the mother and the young, the parapet and the blood, the vineyard's two
# kinds, the ox and the ass, the mingled stuff, the tassels on the four corners), THE SLANDERED BRIDE (when a man takes a wife and hates her, the father and the mother and
# the elders, the hundred of silver, if the thing was true), THE ADULTERER, THE BETROTHED GIRL AND THE SEDUCER (a man found lying with a married woman, the betrothed girl
# in the city and in the field, the pursuer's law, the seducer of the unbetrothed, the fifty), THE FATHER'S WIFE AND THE ASSEMBLY (his father's wife and his father's skirt,
# the crushed and the cut, the mamzer, Ammon and Moab for ever, the curse turned to a blessing, Edom and Egypt the third generation), THE CAMP (when the camp goes out, the
# night's chance, toward evening he bathes, a place outside the camp and a spade, for the LORD walks in your camp), THE SLAVE, THE HIRE AND THE INTEREST (the slave who
# escapes to you, no cult harlot of the daughters of Israel, the harlot's hire and the dog's price, interest to your brother and to the foreigner), THE VOWS AND THE
# LABORER (when you vow a vow delay not, if you refrain from vowing, what goes out of your lips, when you come into your neighbor's vineyard, into your vessel you shall
# not put, the standing grain and the sickle), THE DIVORCE (when a man takes a wife and she finds no favor, the grounds, for her name, the bill in her hand, and she goes
# and becomes another man's, her first husband may not take her back), THE NEWLYWED, THE MILLSTONE, THE KIDNAPPER AND THE LEPROSY (a new wife and one year, the millstone
# and the upper stone, the kidnapper of a soul, take heed in the plague of leprosy, as the priests teach you, remember what the LORD did to Miriam), THE PLEDGE AND THE WAGE
# (when you lend your neighbor any loan, outside you shall stand, the poor man's pledge at sunset, righteousness before the LORD, you shall not oppress a hired man, on his
# day you shall give his wage), FATHERS AND SONS, THE STRANGER AND THE GLEANINGS (fathers shall not die for sons, each in his own sin, the stranger's and the orphan's
# justice, the widow's garment, remember that you were a slave, the forgotten sheaf, the olive and the vineyard), THE LASHES AND THE MUZZLE (when there is a dispute between
# men, if the wicked deserves beating, the one sanction, forty he shall strike him, and your brother be degraded before your eyes, you shall not muzzle an ox, in its
# treading), THE LEVIRATE (when brothers dwell together, the wife of the dead not outside, her husband's brother shall come upon her, the firstborn on the dead brother's
# name, if the man desires not to take her, the shoe and the spittle, the house of him whose shoe was drawn off), THE WRESTLERS AND THE WEIGHTS (when men strive together
# and the wife of one draws near, cut off her hand read twice, a stone and a stone an ephah and an ephah, a whole and just weight, the local custom and the inspector) and
# AMALEK (remember what Amalek did to you, how he met you, when the LORD gives you rest, blot out the memory of Amalek, you shall not forget); THE READBACK'S FORMS ON FILE,
# NO NEW FORM (THE DEUTERONOMY WALK sitting 17b — THE LEAN PASS, 2026-09-26; World/step9/DEUTERONOMY_WALK.md "Sitting 17b"; the state doc's #221). ONE RUNNER OVER FOUR
# CHAPTERS AND FOUR UNITS (the span four ranges); TWENTY own-day lines at the counter's day (40, 11, 1), NO marker: lost_thing_declared (22:1-4), garments_nest_parapet_declared
# (22:5-8), mixtures_tassels_declared (22:9-12), slandered_bride_declared (22:13-21), adultery_betrothed_seducer_declared (22:22-29), fathers_wife_assembly_declared (23:1-9),
# camp_holiness_declared (23:10-15), slave_hire_interest_declared (23:16-21), vows_law_declared (23:22-24), laborer_vineyard_grain_declared (23:25-26), divorce_declared
# (24:1-4), newlywed_millstone_kidnapper_declared (24:5-7), leprosy_miriam_declared (24:8-9), pledge_wage_declared (24:10-15), fathers_sons_stranger_gleanings_declared
# (24:16-22), lashes_declared (25:1-3), muzzle_declared (25:4), levirate_declared (25:5-10), wrestlers_weights_declared (25:11-16), amalek_remembrance_declared (25:17-19) —
# SEVENTY-NINE writes on Israel (thirty-four BLOCKS, forty-four STATUSES, one HEAVEN entry), every one its first entry. THE KIN'S CELLS BY CALL (thirty-two runners, every
# edge REFERENCE — the Exodus and Leviticus cells READ THESE CHAPTERS FORWARD at their own compiles: the lost thing, the pledge, the interest, the gleanings, the wage, the
# mixtures, the levirate's fifteen, the lashes); THE TAPE'S LINES BY KIND (Sarah's 'married to a husband', Dinah's folly, Judah's levirate and Tamar's pledge, Amalek's
# coming and the blotting sworn, Miriam's speech and stroke, Balak's hire and the parting, the camp's unclean sent out, the vows' law spoken, Moab spared, the abomination
# barred, the forgetting warned, the release, the hand opened, the Hebrew slave, the judges in every gate, the blemished sacrifice, the witnesses' law, the war's speech, the
# captive wife, the hanged man's burial). Sixteen cells and the table; every token probed (zero-report law); effects on every cell (the effects law); THE EXAM THE
# FORTY-FOUR MISHNAH ROWS THE LEDGER CITES AT LEAST TWICE (Bava Batra 5:10-11; Bava Kamma 8:1, 8:3; Bava Metzia 2:7-10, 5:10, 9:13; Berakhot 3:5; Chullin 12:2-3; Gittin
# 2:4, 3:1, 8:1, 9:10; Ketubot 3:1, 3:5, 4:3; Kiddushin 1:1; Makkot 3:10, 3:15; Peah 4:6, 6:6, 7:2; Rosh Hashanah 1:1; Sanhedrin 3:4, 11:1; Sotah 7:2, 8:4; Temurah
# 6:2-3; Yevamot 1:1, 2:1, 3:9, 4:13, 8:2-3, 10:1, 12:1, 12:3, 12:6; Zavim 2:3 — read whole; no docket, the lean form); the parameters the runner's DATA rows (no clock
# datum). The daemon law_persons_poor_court given_at Deut 22:1, installed_by boot (the Deuteronomy daemons' form). Reading ledger:
# logic/oral_triage/deu_22_25_ki_teitzei_2026-09-25.md; the lean exam: deu_22_25_ki_teitzei_exam_2026-09-26.md.

# ---- THE HONEST-PAIRING GUARD ----------------------------------------------------------------------------
import os as _os, sys as _sys
_sys.path.insert(0, _os.path.dirname(_os.path.abspath(__file__)))
_ROOT = _os.path.normpath(_os.path.join(_os.path.dirname(_os.path.abspath(__file__)), '..', '..'))   # THE PORTABLE REPO: the repo root from this file's own place
from compile_guards import check_honest_pairing as _chp
_P = _os.path.abspath(__file__)
GUARDED = _chp(_P, 'CASES', 2)
assert GUARDED == 0, ("the guard counted %d expectations, the tripwire holds 0" % GUARDED)   # RETYPED after the generator (the cells' asks summed)
print('guard: %d expectations checked, every one a literal from the answer sheet [honest-pairing guard satisfied]' % GUARDED)
import sqlite3, sys, io, re, contextlib, collections, unicodedata, yaml, inspect
from collections import Counter
import effects_layer as FX
import world_engine as WE
import cold_run_ordinances as OR                # THE EDGE: persons_poor_court -> ordinances CALL, reference (Exodus 23:4-5's lost ox and fallen ass, 22:24-26's pledge and interest, 22:20-21's stranger and widow — the Exodus cells READ 22:1-4, 23:21, 24:6, 24:11, 24:13 and 24:17 FORWARD)
import cold_run_mishpatim_2 as M2               # THE EDGE: persons_poor_court -> mishpatim_2 PARAMETER, reference, carries value — a DATA read (Exodus 22:15-16's seducer — the fifty a POINTER there to 22:29, the PROBES row read)
import cold_run_mishpatim as MI                 # THE EDGE: persons_poor_court -> mishpatim CALL, reference (Exodus 21:22's strivers and the humiliation's IMPORT of 25:11-12; 21:16's kidnapper by the verse)
import cold_run_holiness as HO                  # THE EDGE: persons_poor_court -> holiness CALL, reference (Leviticus 19:9-10's gifts — the forgotten sheaf and olive READ 24:19-20 FORWARD; 19:13's wage — 24:14 forward; 19:15's judgment; 19:35-36's balances)
import cold_run_holiness_b as HB                # THE EDGE: persons_poor_court -> holiness_b CALL, reference (Leviticus 19:19's mixtures ROUTED to 22:9-11 at their own compile; 19:20's lashing procedure — Makkot 3:14)
import cold_run_sanctions as SA                 # THE EDGE: persons_poor_court -> sanctions CALL, reference (Leviticus 18:8's father's wife; 20:10's adulterers and the strangled; the levirate's fifteen and the bonds — 25:5 READ FORWARD; the lashes' list and the excision's discharge — 25:2-3 forward)
import cold_run_priesthood as PR                # THE EDGE: persons_poor_court -> priesthood CALL, reference (Leviticus 21:7's harlot and the released widow; 22:24's crushed)
import cold_run_yovel as YV                     # THE EDGE: persons_poor_court -> yovel CALL, reference (Leviticus 25:36-37's interest — THE IMPORT EDGE M-07 naming 23:21, paid in reverse)
import cold_run_vows as VW                      # THE EDGE: persons_poor_court -> vows CALL, reference (Numbers 30's delay clocks, the sin on the vower, the lips, the vow and the gift, the levirate widow's vow)
import cold_run_musafim as MU                   # THE EDGE: persons_poor_court -> musafim PARAMETER, reference, carries value — a DATA read (Numbers 29:39's vows at the feasts — the deadline's data)
import cold_run_naso as NS                      # THE EDGE: persons_poor_court -> naso CALL, reference (Numbers 5:1-4's three camps and their ladder — the emitter NOT in its span: the night's chance this chapter's own law)
import cold_run_negaim as NG                    # THE EDGE: persons_poor_court -> negaim CALL, reference (Leviticus 13's tracks and their standing verdicts — 24:8's charge)
import cold_run_metzora as MT                   # THE EDGE: persons_poor_court -> metzora CALL, reference (Leviticus 14:14's right members — 25:9's right foot by the verbal analogy)
import cold_run_beha as BH                      # THE EDGE: persons_poor_court -> beha CALL, reference (Numbers 12's Miriam — the paradigm of evil speech, only a priest declares)
import cold_run_balak as BK                     # THE EDGE: persons_poor_court -> balak CALL, reference (Numbers 22-24's hire and the curse turned — the block never closed, 23:6 THE RUN)
import cold_run_exodus_story as ES              # THE EDGE: persons_poor_court -> exodus_story CALL, reference (Exodus 17:8-16's Amalek and the blotting sworn — a heaven entry open to 25:19)
import cold_run_family as FA                    # THE EDGE: persons_poor_court -> family CALL, reference (Genesis 38's levirate READ FORWARD to 25:5-10, the widow waiting, the cult harlot's Sinai seat 23:18, the mamzer's definition; Genesis 24's girl written as a boy — 22:15-16; THE OWED EDGE family -> deut_family PAID by this runner, REVERSE)
import cold_run_zelophehad as ZL                # THE EDGE: persons_poor_court -> zelophehad CALL, reference (Numbers 27:8's 'and he has no son' — ONE CLAUSE OPENS TWO INSTITUTIONS with 25:5; the name is the inheritance)
import cold_run_joseph as JO                    # THE EDGE: persons_poor_court -> joseph CALL, reference (Genesis 34:7's folly in Israel — 22:21; 34:12's bride-price and the FETCH-50 — 22:29)
import cold_run_primeval as PV                  # THE EDGE: persons_poor_court -> primeval CALL, reference (Genesis 16:6's humbling — 22:24, 22:29; 13:7's strife and the muzzled beasts — 25:1, 25:4, 25:11)
import cold_run_mekoshesh as MK                 # THE EDGE: persons_poor_court -> mekoshesh CALL, reference (Numbers 15:35-36's stoning rite — 22:21, 22:24)
import cold_run_seducers as SE                  # THE EDGE: persons_poor_court -> seducers CALL, reference (13:6's purge formula at its sixth to ninth seats — 22:21, 22:22, 22:24, 24:7; 13:10-11's hand first and the rite)
import cold_run_refuge_war_family as RW         # THE EDGE: persons_poor_court -> refuge_war_family CALL, reference (19:15-19's witnesses — 22:14-19, 24:16; 19:21's talion in 'be' — 25:12; 20:5-8's exemptions — 24:5; 21:14's release — 24:1; 20:1 and 20:10's enemies and peace)
import cold_run_courts_prophet as CP            # THE EDGE: persons_poor_court -> courts_prophet CALL, reference (17:1's harlot's hire and the abomination's nine — 23:19; 17:14's king — 25:19)
import cold_run_festivals_judges as FJ          # THE EDGE: persons_poor_court -> festivals_judges CALL, reference (16:18-20's courts, their three tiers and the judgment's wresting — 22:15-18, 24:17, 25:1, 25:7-9)
import cold_run_second_tablets as ST            # THE EDGE: persons_poor_court -> second_tablets CALL, reference (10:18-19's orphan, widow and stranger — 24:17-22)
import cold_run_release_firstborn as RF         # THE EDGE: persons_poor_court -> release_firstborn PARAMETER, reference, carries value — a DATA read (15:9's cry and sin — 23:22, 24:15; 15:15's slave refrain — 24:18, 24:22; 15:10, 15:18's blessing)
import cold_run_covenant_at_horeb as CH         # THE EDGE: persons_poor_court -> covenant_at_horeb CALL, reference (5:12-15's keep and remember, the ox and the ass, the exodus ground — 22:10-11, 24:18, 24:22; 5:16's reward clause — 22:7, 25:15)
import cold_run_seven_nations as SN             # THE EDGE: persons_poor_court -> seven_nations CALL, reference (7:25-26's abomination formula at its fifth to eighth seats — 22:5, 23:19, 24:4, 25:16)
import cold_run_place_name as PN                # THE EDGE: persons_poor_court -> place_name CALL, reference (12:30's inquiry barred and 12:23's blood — 25:3's a fortiori; 23:17's slave's gate NOT the place)
import cold_run_hear_o_israel as HI             # THE EDGE: persons_poor_court -> hear_o_israel CALL, reference (6:8-9's seven that surround a man — the fringes at 22:12; the Shema by the launderers' vat — 23:15)
import cold_run_lev24 as L24                    # THE EDGE: persons_poor_court -> lev24 CALL, reference (Leviticus 24:20's talion as money — 25:12's 'cut off her hand')
import cold_run_good_land as GL                 # THE EDGE: persons_poor_court -> good_land CALL, reference (the finder's own count: receipt_seats(22..25) -> [], [], [], [] — NO receipt in the four chapters, the register file untouched; the live edge filed from the gate's print, rule 9)

'''
# ---- the generic helper block from the chapter 19-21 runner, by content markers ----
a = RWF.index('HERE = _os.path.dirname(_os.path.abspath(__file__))'); b = RWF.index('def LEN(b, c, v): return len(words(b, c, v))'); b = RWF.index('\n', b) + 1
helpers = RWF[a:b]
OLDW = "def W19(v): return words('Deut', 19, v)\ndef W20(v): return words('Deut', 20, v)\ndef W21(v): return words('Deut', 21, v)\ndef W(c, v): return words('Deut', c, v)"
assert helpers.count(OLDW) == 1
helpers = helpers.replace(OLDW, "def W22(v): return words('Deut', 22, v)\ndef W23(v): return words('Deut', 23, v)\ndef W24(v): return words('Deut', 24, v)\ndef W25(v): return words('Deut', 25, v)\ndef W(c, v): return words('Deut', c, v)")
left = [l for l in helpers.split('\n') if re.search(r'(?<!\d)(19|20|21)(?!\d)', re.sub(r'2026-09-\d\d|0x05[0-9A-F]{2}', '', l))]
print('helper lines still naming 19, 20 or 21:', len(left), [l[:100] for l in left][:4]); assert not left, left[:3]
TAIL_A = '''def verse_text(ch, vs, book='Deut'): return ' '.join(words(book, ch, vs))
DV = lambda c, v: ('Deut', c, v)
NEG_T = ('לא', 'ולא')   # (not; and not)
NAME = ('יהוה', 'ליהוה', 'ויהוה', 'ביהוה', 'מיהוה')   # (the LORD; to the LORD; and the LORD; in the LORD; from the LORD)
import difflib
def SH(a, b_): return sum(s for _, _, s in difflib.SequenceMatcher(a=words(*a), b=words(*b_)).get_matching_blocks())   # the reading's shared-run measure
CHS = (22, 23, 24, 25)
NV = {c: len({v for (b, cc, v) in by if b == 'Deut' and cc == c}) for c in CHS}; assert NV == {22: 29, 23: 26, 24: 22, 25: 19}, NV   # twenty-nine, twenty-six, twenty-two and nineteen verses (the reading's divisions assert)
TOKN = {c: sum(len(W(c, v)) for v in range(1, NV[c] + 1)) for c in CHS}; assert TOKN == {22: 437, 23: 339, 24: 327, 25: 260}, TOKN   # the four chapters' tokens (the reading's store assert — the store the DB at every verse)
SPAN = [(22, v) for v in range(1, 30)] + [(23, v) for v in range(1, 27)] + [(24, v) for v in range(1, 23)] + [(25, v) for v in range(1, 20)]
assert len(SPAN) == 96

P_ = []   # the provenance trail of the case being run
def ink(ref, note):  P_.append(('INK',  'Deut %s — %s' % (ref, note) if not ref[:1].isupper() else '%s — %s' % (ref, note)))
def move(src, note): P_.append(('MOVE', '%s — %s' % (src, note)))
def dat(note):       P_.append(('DATA', note))
def hyp(note):       P_.append(('HYP',  note))     # THE LINK REVIEW LAW: a hypothesis — no teacher; counted apart, never as compiled
def out(verdict, effects):
    """verdict + registry-validated effects (the engine contract)"""
    FX.validate([e for e in effects if e != FX.NONE])
    return verdict, effects, list(P_)

# ---- THE INK, computed (the parser and the tokens; the reading's facts the expectations — every assert PROVEN at the reading, ch22_ink.py — COPIED from the reading's instrument by content markers in three blocks; the store-, shelf- and Onkelos-bound asserts left to the reading; the parser's facts typed from the ink's own asserts) ----
def MARKS(c, v): return [t for t in verse_words('Deut', c, v) if t[-1] in '#~^%@|*']
PARSE = {(c, v): (ink_numbers(verse_words('Deut', c, v)), ink_ordinals(verse_words('Deut', c, v)), MARKS(c, v)) for (c, v) in SPAN}
NUMV = [k for k in PARSE if PARSE[k][0]]; ORDV = [k for k in PARSE if PARSE[k][1]]; STARV = [k for k in PARSE if PARSE[k][2]]
print('THE INK (printed before it is asserted): PARSE %s, NUMV %s, ORDV %s, STARV %s, TOKN %s' % ({k: p for k, p in PARSE.items() if p[0] or p[1] or p[2]}, NUMV, ORDV, STARV, TOKN))
assert {k: p for k, p in PARSE.items() if p[0] or p[1] or p[2]} == {(22, 12): ([4], [], []), (22, 19): ([100], [], []), (22, 22): ([2], [], ['שני#']), (22, 24): ([2], [], ['שני#']), (22, 29): ([50], [], []), (23, 3): ([], [10], []), (23, 4): ([], [10], []), (23, 9): ([], [3], []), (23, 17): ([1], [], []), (23, 19): ([2], [], ['שני#']), (24, 4): ([], [1], []), (24, 5): ([1], [], []), (25, 3): ([40], [], []), (25, 5): ([1], [], []), (25, 11): ([1], [], ['האחד#'])}, {k: p for k, p in PARSE.items() if p[0] or p[1] or p[2]}   # (two; the one) FIFTEEN hits — eleven number verses (the four corners, the hundred, the two, the fifty, one of your gates, both of them, one year, forty, one of them, the one) and four ordinals (the tenth twice, the third, the first) — the reading's parser assert
assert NUMV == [(22, 12), (22, 19), (22, 22), (22, 24), (22, 29), (23, 17), (23, 19), (24, 5), (25, 3), (25, 5), (25, 11)] and ORDV == [(23, 3), (23, 4), (23, 9), (24, 4)] and STARV == [(22, 22), (22, 24), (23, 19), (25, 11)]
NEG = {(c, v): [x for x in W(c, v) if x in NEG_T] for (c, v) in SPAN if any(x in NEG_T for x in W(c, v))}
NAME_BARE = sum(1 for (c, v) in SPAN for x in W(c, v) if x == 'יהוה')   # (the LORD)
print('THE NEGATIONS AND THE NAME (printed before they are asserted):', NEG, NAME_BARE)
assert NAME_BARE == 1 + 14 + 7 + 4 and [v for v in range(1, 30) if (22, v) in NEG] == [1, 2, 3, 4, 5, 6, 8, 9, 10, 11, 14, 17, 19, 20, 24, 26, 28, 29], (NAME_BARE, [v for v in range(1, 30) if (22, v) in NEG])   # the Name once in chapter 22 (22:5), fourteen bare in 23, seven in 24, four in 25 (the reading's frames assert)
'''
# ---- THE INK BLOCKS from the reading's instrument, by content markers — three blocks ----
def block(start, end):
    i = INKB.index(start); j = INKB.index(end, i); assert i < j, (start[:40], end[:40]); return INKB[i:j]
ink_block = block("# THE KIN FOUND BY COMPUTATION (the measure's A section", "# ---- THE SHELF BY POSITION") + block("# THE KIN BY COMPUTATION (the measure's A): the closest verses", "# THE FRAMES (the measure's E)") + block("# THE FRAMES (the measure's E)", "# THE REGISTER (the measure's E)")
lines = ink_block.split('\n')
DROP_RX = re.compile(r"(?<![A-Za-z_0-9])(byw|SG|sg|STORE_MISMATCH|VC|LED|sif|sif_he|onk|onk_he|Hb|HB0|ARM|SEATS|clean|heads|SP_|aramaic|arm|arm_e|E|kinrows|CS|_CS|H|A|HP|AP|sidx|glob|UIDS|PATCHED|OUT|EXP2DB|store|FAIL|_DUMP)(?![A-Za-z_0-9])")
drop = [l for l in lines if not l.lstrip().startswith('#') and DROP_RX.search(l.split('   #')[0])]   # the code before its trailing comment
print('dropped (the store-, shelf- and Onkelos-bound lines):', len(drop), [d[:90] for d in drop])
N_DROP_EXPECTED = int(os.environ.get('N_DROP', '-1'))
if N_DROP_EXPECTED >= 0: assert len(drop) == N_DROP_EXPECTED, (len(drop), [d[:100] for d in drop])   # READ FROM THE PRINT at the first derive, typed into the shell's N_DROP at the second
lines = [l for l in lines if l not in drop]
STOP_OLD = "STOP = set('את ואת אשר כל וכל על ועל אל ואל לא ולא כי אם יהוה אלהיך אלהיכם לך לכם בו שם שמה גם מן ממך עד הוא היא אתם אתה אנכי אני לו לה בכל כאשר כן הימים היום אלה האלה בארץ הארץ אשר ואם או פן ופן ואת זה וזה הם המה'.split())"
STOP_NEW = ("STOP = set(('את ואת אשר כל וכל על ועל אל ואל '   # (the object marker, and-it, which, all, on, to — the particles)\n"
            "            'לא ולא כי אם יהוה אלהיך אלהיכם '   # (not, for, if; the LORD, your God)\n"
            "            'לך לכם בו שם שמה גם מן ממך עד '   # (to you, in it, there, also, from, until)\n"
            "            'הוא היא אתם אתה אנכי אני לו לה '   # (he, she, you, I, to him, to her)\n"
            "            'בכל כאשר כן הימים היום אלה האלה '   # (in all, as, so, the days, today, these)\n"
            "            'בארץ הארץ אשר ואם או פן ופן '   # (in the land, the land, which, and if, or, lest)\n"
            "            'ואת זה וזה הם המה').split())   # (and-it, this, and this, they, they) — the stopword set glossed piece by piece (the lint's ninety-character window)")
assert lines.count(STOP_OLD) == 1, lines.count(STOP_OLD)
lines[lines.index(STOP_OLD)] = STOP_NEW
ink_block = '\n'.join(lines)
n_as = ink_block.count('\nassert '); print('the ink block: %d lines, %d asserts' % (ink_block.count('\n'), n_as)); assert n_as >= 12, n_as
TAIL_B = '''
# ---- THE COUNTER'S DAY AND THE ONE DATABASE SCANNED (a bare world on the exodus epoch; no clock walk these chapters — no marker, no stretch, no clock datum: the sunset, the year, the thirty days and the twenty-four hours parameters, no timer at a line) ----
with contextlib.redirect_stdout(io.StringIO()):
    _WC = WE.World(era='the counter\\'s day — chapters 22-25 on a bare world (the exodus epoch)', epoch='exodus')
_EX = _WC.clock.eras['exodus']
def DAY(y, m, d): return _WC.clock.day_in('exodus', y, m, d)
def DATE(day): return _EX.date(day)
COUNTER = DAY(40, 11, 1)
CLOCK = {'counter': DATE(COUNTER), 'no_marker': True, 'no_clock_datum': True}
print('THE CLOCK (printed before it is asserted):', CLOCK)
assert CLOCK['counter'] == (40, 11, 1), CLOCK

# ---- THE ONE DATABASE SCANNED (the holes' ground — nothing names the seventy-nine on Israel before this sitting; the references' entities and counts as the recon read them — DK4) ----
_WDB = _os.path.join(_ROOT, 'World', 'journal', 'data', 'world.sqlite')
def ledger_scan(entity, pattern):
    """the effects on an entity in the one database whose name or value matches the pattern — None where the database is not built (a fresh clone before build_world)"""
    if not _os.path.exists(_WDB): return None
    c_ = sqlite3.connect('file:%s?mode=ro' % _WDB, uri=True)
    rx = re.compile(pattern, re.I)
    return sorted({e for e, v in c_.execute("SELECT DISTINCT effect, value FROM run_ledger WHERE entity=?", (entity,)).fetchall() if rx.search('%s %s' % (e, v if v is not None else ''))})
def effect_scan(effect):
    """the entities holding an effect in the one database — None where the database is not built"""
    if not _os.path.exists(_WDB): return None
    c_ = sqlite3.connect('file:%s?mode=ro' % _WDB, uri=True)
    return sorted({e for (e,) in c_.execute("SELECT DISTINCT entity FROM run_ledger WHERE effect=?", (effect,)).fetchall()})
def count_scan(effect):
    """the entries of an effect in ONE full run of the tape (DK4's counts — the running world's): the one database folds several runs' rows under their sources (the checkpoint sections' names); the largest source is a whole run — None where the database is not built"""
    if not _os.path.exists(_WDB): return None
    c_ = sqlite3.connect('file:%s?mode=ro' % _WDB, uri=True)
    src = c_.execute("SELECT source FROM run_ledger GROUP BY source ORDER BY COUNT(*) DESC, source LIMIT 1").fetchone()[0]
    return c_.execute("SELECT COUNT(*) FROM run_ledger WHERE effect=? AND source=?", (effect, src)).fetchone()[0]
OWN79 = ('lost_thing_return_commanded', 'hiding_from_lost_thing_barred', 'fallen_beast_raising_commanded', 'cross_dressing_barred', 'mother_bird_sending_commanded', 'parapet_commanded', 'house_bloodguilt_barred', 'vineyard_mixed_seed_barred', 'ox_ass_plowing_barred', 'wool_linen_barred', 'tassels_commanded', 'slander_fine_commanded', 'slanderer_divorce_barred', 'unchaste_bride_stoning_commanded', 'adulterers_death_commanded', 'betrothed_girl_city_field_declared', 'rapist_fifty_commanded', 'rapist_divorce_barred', 'fathers_wife_barred', 'crushed_barred_from_assembly', 'forbidden_union_offspring_barred', 'ammon_moab_barred_forever', 'ammon_moab_peace_barred', 'edom_egypt_third_generation_admitted', 'camp_evil_thing_guarded', 'nocturnal_unclean_exit_commanded', 'camp_latrine_commanded', 'camp_holiness_required', 'escaped_slave_return_barred', 'slave_oppression_barred', 'cult_prostitution_barred', 'harlots_hire_dogs_price_barred', 'interest_to_brother_barred', 'interest_to_foreigner_permitted', 'vow_delay_barred', 'vow_refraining_permitted', 'lips_utterance_binding', 'laborer_eating_permitted', 'laborer_vessel_barred', 'sickle_swinging_barred', 'bill_of_divorce_commanded', 'divorced_wife_remarriage_permitted', 'first_husband_retaking_barred', 'land_caused_to_sin_barred', 'newlywed_year_exemption_commanded', 'millstone_pledge_barred', 'kidnapper_death_commanded', 'leprosy_priests_teaching_commanded', 'miriam_remembrance_commanded', 'pledge_entry_barred', 'poor_mans_pledge_return_commanded', 'righteousness_before_the_lord', 'hireling_oppression_barred', 'hireling_wage_same_day_commanded', 'fathers_for_sons_death_barred', 'stranger_orphan_justice_commanded', 'widows_garment_pledge_barred', 'forgotten_sheaf_commanded', 'olive_second_beating_barred', 'vineyard_gleaning_barred', 'court_justification_commanded', 'lashes_by_number_commanded', 'lashes_forty_cap_declared', 'brother_degradation_barred', 'ox_muzzling_barred', 'widow_outsider_marriage_barred', 'levirate_marriage_commanded', 'firstborn_on_dead_name_commanded', 'refusal_at_gate_declared', 'shoe_loosening_rite_declared', 'house_of_unshod_named', 'wife_seizing_hand_cut_commanded', 'hand_cutting_pity_barred', 'diverse_weights_barred', 'diverse_measures_barred', 'whole_just_weight_commanded', 'amalek_remembrance_commanded', 'amalek_memory_blotting_commanded', 'amalek_forgetting_barred')
assert len(OWN79) == 79 and len(set(OWN79)) == 79
HOLE_WORDS = r"^(lost_thing\\w*|hiding_from\\w*|fallen_beast\\w*|cross_dressing\\w*|mother_bird\\w*|parapet\\w*|house_bloodguilt\\w*|vineyard_mixed\\w*|ox_ass\\w*|wool_linen\\w*|tassels\\w*|slander\\w*|unchaste_bride\\w*|adulterers_death\\w*|betrothed_girl\\w*|rapist\\w*|fathers_wife\\w*|crushed_barred\\w*|forbidden_union_offspring\\w*|ammon_moab\\w*|edom_egypt\\w*|camp_evil\\w*|nocturnal_unclean\\w*|camp_latrine\\w*|camp_holiness\\w*|escaped_slave\\w*|slave_oppression\\w*|cult_prostitution\\w*|harlots_hire\\w*|interest_to_\\w*|vow_delay\\w*|vow_refraining\\w*|lips_utterance\\w*|laborer_\\w*|sickle_swinging\\w*|bill_of_divorce\\w*|divorced_wife\\w*|first_husband\\w*|land_caused_to_sin\\w*|newlywed\\w*|millstone\\w*|kidnapper\\w*|leprosy_priests\\w*|miriam_remembrance\\w*|pledge_entry\\w*|poor_mans_pledge\\w*|righteousness_before\\w*|hireling_\\w*|fathers_for_sons\\w*|stranger_orphan\\w*|widows_garment\\w*|forgotten_sheaf\\w*|olive_second\\w*|vineyard_gleaning\\w*|court_justification\\w*|lashes_by_number\\w*|lashes_forty\\w*|brother_degradation\\w*|ox_muzzling\\w*|widow_outsider\\w*|levirate_marriage\\w*|firstborn_on_dead\\w*|refusal_at_gate\\w*|shoe_loosening\\w*|house_of_unshod\\w*|wife_seizing\\w*|hand_cutting\\w*|diverse_weights\\w*|diverse_measures\\w*|whole_just\\w*|amalek_remembrance\\w*|amalek_memory\\w*|amalek_forgetting\\w*)\\b"
_hs = ledger_scan('israel_people', HOLE_WORDS); HOLE_SCAN = None if _hs is None else [e for e in _hs if e not in OWN79]   # this sitting's own names excluded once the fold carries them
KIN42 = ('pity_barred', 'talion_pity_barred', 'put_to_death', 'stoned', 'lashes', 'pays', 'exempt', 'israel_hears_and_fears', 'hanged', 'buried', 'sent_outside_the_camp', 'firstborn_by_the_head', 'inheritance_stayed_in_tribe', 'blood_required', 'bribe_barred', 'judges_charged', 'courts_established', 'peace_call_commanded', 'innocent_blood_purge_commanded', 'evil_purged_from_the_midst', 'levirate_owed', 'waits_for_the_levir', 'amalek_to_be_blotted', 'amalek_weakened', 'justice_pursuit_commanded', 'judgment_wresting_barred', 'person_respecting_barred', 'forgetting_barred', 'stricken_with_leprosy', 'hand_opening_commanded', 'cry_heard', 'bears_sin', 'work_of_the_hand_blessed', 'blessings_for_hearing', 'evil_speech_spoken', 'cursing_barred', 'house_abomination_barred', 'interest_barred', 'pledge_returned_by_sunset', 'wage_due_by_morning', 'left_for_the_poor', 'mixture_barred')
KIN_EXPECTED = (2, 1, 7, 2, 0, 1, 1, 1, 1, 9, 2, 2, 1, 1, 1, 1, 1, 1, 1, 0, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 1, 2, 2, 2, 1, 1, 0, 0, 0, 0, 0)   # DK4 — the recon's counts on the running world (ch22_compile_recon.out, section G; the probe Q46's KIN tuple)
assert len(KIN42) == 42 == len(KIN_EXPECTED)
KIN_COUNTS = {k: count_scan(k) for k in KIN42}
SCANS = {k: effect_scan(k) for k in KIN42 + ('restores', 'unloading_owed', 'wife_taken', 'pledge_held', 'loathed', 'karet_cut_off', 'love_owed')}
del _hs   # 9b's lesson: the raw scans are the database's state at import — the derived lists are equal on the cached and the full load
_FXV = yaml.safe_load(open(_os.path.join(HERE, 'effect_vocabulary.yaml'), encoding='utf-8'))['effects']
print('THE SCANS (printed before they are asserted): holes %s; the kin counts %s; the entities %s' % (HOLE_SCAN, KIN_COUNTS, SCANS))
assert HOLE_SCAN in ([], None), HOLE_SCAN   # THE HOLES' GROUND — nothing on Israel named the seventy-nine before this sitting (DK4)
assert all(v is None for v in KIN_COUNTS.values()) or tuple(KIN_COUNTS.values()) == KIN_EXPECTED, [(k, KIN_COUNTS[k], e) for k, e in zip(KIN42, KIN_EXPECTED) if KIN_COUNTS[k] != e]   # the references' counts as the recon read them (DK4 — no second write)
SCANS_EXPECTED = _SCANS_EXPECTED_   # the entities per effect — typed from the first derive's print (the callees' way — printed before typed)
if SCANS_EXPECTED and any(v is not None for v in SCANS.values()): assert SCANS == SCANS_EXPECTED, [(k, SCANS[k], SCANS_EXPECTED.get(k)) for k in SCANS if SCANS[k] != SCANS_EXPECTED.get(k)]
assert all(k in _FXV for k in OWN79) and sum(1 for k in OWN79 if _FXV[k]['ledger_op'] == 'block') == 34 and sum(1 for k in OWN79 if _FXV[k]['ledger_op'] == 'status') == 44 and sum(1 for k in OWN79 if _FXV[k]['ledger_op'] == 'heaven') == 1, 'the seventy-nine on the registry (add_types_ch22_a.py)'
assert _FXV['put_to_death']['ledger_op'] == 'body' and _FXV['stoned']['ledger_op'] == 'body' and _FXV['evil_purged_from_the_midst']['ledger_op'] == 'body' and _FXV['lashes']['ledger_op'] == 'body' and _FXV['pays']['ledger_op'] == 'debit' and _FXV['exempt']['ledger_op'] == 'status' and _FXV['restores']['ledger_op'] == 'transfer' and _FXV['unloading_owed']['ledger_op'] == 'debit', 'the reused body effects as the recon read them'
# THE TWINS DIFFED on the DB (the reading's kin asserts read again here — DK4; the shared run SH)
TWIN = {'24:16 vs 2Kgs 14:6': SH(DV(24, 16), ('2Kgs', 14, 6)), '24:16 vs 2Chr 25:4': SH(DV(24, 16), ('2Chr', 25, 4)), '24:18 vs 15:15': SH(DV(24, 18), DV(15, 15)), '24:22 vs 15:15': SH(DV(24, 22), DV(15, 15)), '24:18 vs 24:22': SH(DV(24, 18), DV(24, 22)), '24:1 vs 24:3': SH(DV(24, 1), DV(24, 3)), '22:5 vs 25:16': SH(DV(22, 5), DV(25, 16)), '23:3 vs 23:4': SH(DV(23, 3), DV(23, 4)), '24:4 vs 21:23': SH(DV(24, 4), DV(21, 23)), '25:15 vs 5:16': SH(DV(25, 15), DV(5, 16)), '25:19 vs Exod 17:14': SH(DV(25, 19), ('Exod', 17, 14)), '24:9 vs 25:17': SH(DV(24, 9), DV(25, 17)), '23:5 vs 24:9': SH(DV(23, 5), DV(24, 9)), '22:28 vs Exod 22:15': SH(DV(22, 28), ('Exod', 22, 15)), '22:29 vs Exod 22:16': SH(DV(22, 29), ('Exod', 22, 16)), '22:19 vs 22:29': SH(DV(22, 19), DV(22, 29)), '22:1 vs 22:4': SH(DV(22, 1), DV(22, 4)), '22:1 vs Exod 23:4': SH(DV(22, 1), ('Exod', 23, 4)), '22:4 vs Exod 23:5': SH(DV(22, 4), ('Exod', 23, 5)), '22:22 vs Lev 20:10': SH(DV(22, 22), ('Lev', 20, 10)), '22:22 vs Gen 20:3': SH(DV(22, 22), ('Gen', 20, 3)), '22:21 vs Gen 34:7': SH(DV(22, 21), ('Gen', 34, 7)), '22:21 vs 21:21': SH(DV(22, 21), DV(21, 21)), '22:24 vs 17:5': SH(DV(22, 24), DV(17, 5)), '24:17 vs 16:19': SH(DV(24, 17), DV(16, 19)), '24:17 vs Exod 23:6': SH(DV(24, 17), ('Exod', 23, 6)), '24:15 vs 15:9': SH(DV(24, 15), DV(15, 9)), '23:22 vs 15:9': SH(DV(23, 22), DV(15, 9)), '23:22 vs Eccl 5:3': SH(DV(23, 22), ('Eccl', 5, 3)), '24:19 vs 14:29': SH(DV(24, 19), DV(14, 29)), '24:19 vs Lev 19:9': SH(DV(24, 19), ('Lev', 19, 9)), '24:21 vs Lev 19:10': SH(DV(24, 21), ('Lev', 19, 10)), '24:14 vs Lev 19:13': SH(DV(24, 14), ('Lev', 19, 13)), '25:5 vs Gen 38:8': SH(DV(25, 5), ('Gen', 38, 8)), '25:5 vs Num 27:8': SH(DV(25, 5), ('Num', 27, 8)), '25:6 vs Gen 48:6': SH(DV(25, 6), ('Gen', 48, 6)), '25:12 vs 19:21': SH(DV(25, 12), DV(19, 21)), '25:12 vs 19:13': SH(DV(25, 12), DV(19, 13)), '25:11 vs Exod 21:22': SH(DV(25, 11), ('Exod', 21, 22)), '23:20 vs Exod 22:24': SH(DV(23, 20), ('Exod', 22, 24)), '23:20 vs Lev 25:36': SH(DV(23, 20), ('Lev', 25, 36)), '23:21 vs Lev 25:37': SH(DV(23, 21), ('Lev', 25, 37)), '22:9 vs Lev 19:19': SH(DV(22, 9), ('Lev', 19, 19)), '22:11 vs Lev 19:19': SH(DV(22, 11), ('Lev', 19, 19)), '22:12 vs Num 15:38': SH(DV(22, 12), ('Num', 15, 38)), '23:1 vs Lev 18:8': SH(DV(23, 1), ('Lev', 18, 8)), '23:2 vs Lev 21:20': SH(DV(23, 2), ('Lev', 21, 20)), '23:2 vs Lev 22:24': SH(DV(23, 2), ('Lev', 22, 24)), '23:18 vs Gen 38:21': SH(DV(23, 18), ('Gen', 38, 21)), '23:19 vs 17:1': SH(DV(23, 19), DV(17, 1)), '23:11 vs Lev 15:16': SH(DV(23, 11), ('Lev', 15, 16)), '23:11 vs Num 5:2': SH(DV(23, 11), ('Num', 5, 2)), '23:17 vs Exod 22:20': SH(DV(23, 17), ('Exod', 22, 20)), '24:5 vs 20:7': SH(DV(24, 5), DV(20, 7)), '24:6 vs Exod 22:25': SH(DV(24, 6), ('Exod', 22, 25)), '24:13 vs Exod 22:25': SH(DV(24, 13), ('Exod', 22, 25)), '24:7 vs Exod 21:16': SH(DV(24, 7), ('Exod', 21, 16)), '24:8 vs Lev 13:2': SH(DV(24, 8), ('Lev', 13, 2)), '24:9 vs Num 12:10': SH(DV(24, 9), ('Num', 12, 10)), '25:3 vs Lev 19:20': SH(DV(25, 3), ('Lev', 19, 20)), '25:4 vs Gen 13:7': SH(DV(25, 4), ('Gen', 13, 7)), '25:13 vs Lev 19:35': SH(DV(25, 13), ('Lev', 19, 35)), '25:15 vs Lev 19:36': SH(DV(25, 15), ('Lev', 19, 36)), '25:17 vs Exod 17:8': SH(DV(25, 17), ('Exod', 17, 8)), '25:19 vs 8:11': SH(DV(25, 19), DV(8, 11)), '25:19 vs 25:6': SH(DV(25, 19), DV(25, 6)), '24:1 vs 21:14': SH(DV(24, 1), DV(21, 14)), '22:7 vs 5:16': SH(DV(22, 7), DV(5, 16)), '22:10 vs 5:14': SH(DV(22, 10), DV(5, 14)), '23:15 vs Lev 26:12': SH(DV(23, 15), ('Lev', 26, 12)), '23:7 vs 20:10': SH(DV(23, 7), DV(20, 10)), '23:4 vs 2:9': SH(DV(23, 4), DV(2, 9)), '22:14 vs 19:16': SH(DV(22, 14), DV(19, 16)), '25:1 vs 16:18': SH(DV(25, 1), DV(16, 18)), '25:7 vs Ruth 4:1': SH(DV(25, 7), ('Ruth', 4, 1)), '25:9 vs Ruth 4:7': SH(DV(25, 9), ('Ruth', 4, 7)), '25:6 vs Ruth 4:10': SH(DV(25, 6), ('Ruth', 4, 10)), '25:19 vs 1Sam 15:2': SH(DV(25, 19), ('1Sam', 15, 2)), '25:9 vs 27:15': SH(DV(25, 9), DV(27, 15))}
print('THE TWINS DIFFED (printed before they are asserted):', TWIN)
TWIN_EXPECTED = _TWIN_EXPECTED_
if TWIN_EXPECTED: assert TWIN == TWIN_EXPECTED, [(k, TWIN[k], TWIN_EXPECTED.get(k)) for k in TWIN if TWIN[k] != TWIN_EXPECTED.get(k)]   # typed from the first derive's print (the callees' way — printed before typed)
assert TWIN['24:16 vs 2Kgs 14:6'] >= 10 and TWIN['24:18 vs 15:15'] >= 12 and TWIN['24:1 vs 24:3'] >= 8, TWIN   # the reading's three largest twins (the shared runs the reading measured: Kings' quotation, the slave refrain, the bill's clause)
'''
TWIN_EXPECTED = open(f'{SP}/ch22_twin_expected.txt').read().strip() if os.path.exists(f'{SP}/ch22_twin_expected.txt') else 'None'; SCANS_EXPECTED = open(f'{SP}/ch22_scans_expected.txt').read().strip() if os.path.exists(f'{SP}/ch22_scans_expected.txt') else 'None'   # the first derive's prints, parsed by ast from the fast checker's output (ch22_fastcheck_run0.out) and written to the two files — never retyped
src = HEAD + helpers + TAIL_A + ink_block + TAIL_B.replace('_TWIN_EXPECTED_', TWIN_EXPECTED).replace('_SCANS_EXPECTED_', SCANS_EXPECTED) + FACTS
open(f'{SP}/ch22_part1.py', 'w', encoding='utf-8').write(src)
import py_compile; py_compile.compile(f'{SP}/ch22_part1.py', doraise=True)
print('part1 derived: %d bytes; helpers %d, ink block %d (asserts %d); dropped %d store-bound lines; the callees\' facts %d bytes; TWIN_EXPECTED %s; SCANS_EXPECTED %s' % (len(src), len(helpers), len(ink_block), n_as, len(drop), len(FACTS), TWIN_EXPECTED[:40], SCANS_EXPECTED[:40]))

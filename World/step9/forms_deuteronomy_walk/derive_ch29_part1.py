#!/usr/bin/env python3
# THE DEUTERONOMY WALK 19b: cold_run_covenant_return_charge.py PART 1 derived — the head typed here; the generic helper block COPIED from the chapter 26-28 runner by content
# markers (HERE = … through def LEN — the parser exec, the DB, the phrase/lemma/diff helpers; W26-W28 made W29, W30, W31 and W); THE INK BLOCKS COPIED from the reading's own
# instrument ch29_ink.py by content markers — FOUR blocks (the kin found by computation; the kin re-scored; the twins diffed; the formulas over the Torah and the Bible), the
# store-, shelf-, Onkelos- and register-bound lines DROPPED by name (10b's lesson 6 — the count read from the print); THE MARKER'S DAY and the counter's, the one-database scans,
# and THE CALLEES' FACTS (typed in ch29_callees_facts.py from ch29_callees_filtered.txt and ch29b_callees2.out — read before any assert was typed). Asserted substitutions
# throughout. derive_ch26_part1.py's form over three chapters with ONE MARKER. RUN FROM THE REPO ROOT with PYTHONPATH the scratchpad.
import subprocess, re, os, sys
ROOT = _ROOT
SP = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, SP)
import ch29b_spec as S
FEC = open(f'{ROOT}/World/step9/cold_run_firstfruits_ebal_curses.py', encoding='utf-8').read()
INKB = open(f'{SP}/ch29_ink.py', encoding='utf-8').read()
FACTS = open(f'{SP}/ch29_callees_facts.py', encoding='utf-8').read()
assert FACTS.startswith('\n# ---- THE CALLEES\' FACTS'), 'the callees\' facts typed from the prints (ch29_callees_facts.py)'
HEAD = '''#!/usr/bin/env python3
# DEUTERONOMY 29:1-31:30 — THE MOAB RECITAL (you have seen all the LORD did in Egypt, forty years your garments did not wear out, no bread, Sihon and Og and their land, keep the
# words of this covenant), THE COVENANT AND THE OATH (you stand this day all of you before the LORD, from the hewer of wood to the drawer of water, to enter the covenant and the
# oath, established this day as He swore to the fathers, with him who stands here and with him who is not here), THE INDIVIDUAL'S CURSE (lest a heart turn to the nations' gods,
# a root bearing gall and wormwood, he blesses himself in his heart in stubbornness, the LORD will not pardon, the curse written in this book lies on him, blotted out and separated
# for evil), THE LAND'S DESOLATION (the later generation and the foreigner see the plagues, brimstone and salt like Sodom and Gomorrah, the nations ask why, because they forsook the
# covenant and served other gods, uprooted and cast into another land as this day), THE HIDDEN AND THE REVEALED (the hidden the LORD's, the revealed ours to do all the words of this
# law), THE RETURN AND THE GATHERING (when all these things come and you take it to heart, return to the LORD and hearken, He returns your captivity, gathers you from all the peoples
# and from the end of heaven, brings you into the fathers' land and multiplies you above them), THE HEART CIRCUMCISED (the LORD circumcises your heart, the curses on your enemies,
# you return and hearken and do, abounding in the fruit of body, cattle and ground, rejoicing over you as He rejoiced over your fathers), THE COMMANDMENT NEAR (not too hard nor far,
# not in heaven nor beyond the sea, in your mouth and in your heart to do it), LIFE AND DEATH (see I set before you life and good, death and evil; if you love and walk and keep you
# live and multiply; if your heart turns you perish; heaven and earth called to witness; choose life, love, hearken and cleave, the length of days), THE CHARGE AND THE CROSSING
# (Moses went and spoke, a hundred and twenty years old this day, I can no more go out and come in, the LORD crosses before you and Joshua, as He did to Sihon and Og, be strong and of
# good courage; Moses called Joshua in the sight of all Israel), THE LAW WRITTEN AND THE HAKHEL (Moses wrote this law and gave it to the priests and the elders; at the end of seven
# years at the release year's set time at the feast of booths read this law before all Israel, assemble the men, the women, the children and the stranger, that they hear and learn and
# fear and do, their children who have not known), THE TENT AND THE COMMISSION (your days approach to die, call Joshua and present yourselves in the tent, the LORD appeared in the
# pillar of cloud at the tent door; He commissioned Joshua: you shall bring the children of Israel into the land I swore, I will be with you), THE APOSTASY FORETOLD (you shall sleep
# with your fathers, this people will rise and whore after the gods of the land, forsake Me and break My covenant, My anger kindled, I will forsake them and hide My face, many evils
# and troubles, is it not because our God is not among us, I will surely hide My face), THE SONG COMMANDED (write this song and teach it, put it in their mouths, a witness for Me,
# when they eat and are sated and grow fat and turn, the song testifies and is not forgotten, I know their inclination; Moses wrote this song that day and taught it) and THE BOOK
# BESIDE THE ARK AND THE ASSEMBLY (when Moses finished writing the words of this law to their end he commanded the Levites who carry the ark: take this book and put it beside the ark
# a witness against you, I know your rebellion and your stiff neck, how much more after my death; assemble to me all the elders of your tribes and your officers, heaven and earth to
# witness, after my death you will corrupt, Moses spoke the words of this song in the ears of all the assembly to their end); THE READBACK'S FORMS ON FILE, NO NEW FORM (THE
# DEUTERONOMY WALK sitting 19b — THE LEAN PASS, 2026-09-27; World/step9/DEUTERONOMY_WALK.md "Sitting 19b"; the state doc's #229). ONE RUNNER OVER THREE CHAPTERS AND THREE UNITS (the
# span three ranges); TWENTY own-day lines IN THREE FORMS — 13 STATUTES, 4 ACTS, 3 SPEECHES OF THE LORD: the 9 of chapters 29-30 at the counter's day (40, 11, 1), the 11 of chapter 31
# at MOSES' LAST DAY (40, 12, 7) after THE ONE MARKER at 31:1 (the number's verse 31:2 — the year the ink's, Exodus 7:7's eighty + forty; the month and the day the answer sheet's, the 7th
# of Adar — Tosefta Sotah 11:3): moab_recital_declared (29:1-8), covenant_oath_entered_declared (29:9-14), hidden_idolater_curse_declared (29:15-20), land_desolation_answer_declared
# (29:21-27), hidden_and_revealed_declared (29:28), return_and_gathering_declared (30:1-5), heart_circumcised_declared (30:6-10), commandment_near_declared (30:11-14),
# life_and_death_choice_declared (30:15-20), crossing_charge_declared (31:1-6), joshua_charged_before_israel (31:7-8, an act), law_written_given (31:9, an act), hakhel_reading_declared
# (31:10-13), tent_summons_cloud_appeared (31:14-15, an act), apostasy_and_hidden_face_foretold (31:16-18, a speech), song_witness_commanded (31:19-21, a speech), song_written_taught
# (31:22, an act), joshua_commissioned_at_tent (31:23, a speech), book_beside_the_ark_declared (31:24-27), assembly_and_song_spoken_declared (31:28-30) — SIXTY-EIGHT writes on FIVE
# ledgers (fifty-nine NEW: thirty-one STATUSES, two BLOCKS, twenty-six HEAVEN entries — Israel 53, Joshua 3 (the entity yehoshua), Moses 2, the Levites 1; NINE REUSES: entered_the_covenant
# 29:11, became_the_lords_people_this_day 29:12, heaven_and_earth_witness 30:19 and 31:28, blessing_and_curse_set 30:19, cleaving_commanded 30:20, fear_not_promised 31:6 on Israel and
# 31:8 on Joshua, glory_appeared 31:15 on the tent of meeting). THE KIN'S CELLS BY CALL (thirty-three runners, every edge REFERENCE — the kin read these chapters forward: the hakhel's
# end analogy FROM 31:10, the copy of the law's 31:9-13, the booths' 31:10-11, the heart's 30:6, the stiff neck's 31:27, the false six's 30:9, the witnesses' chain, the charge to
# Joshua); THE TAPE'S LINES BY KIND (the plagues, the manna, the pillar, the covenant's blood, the assembly at Horeb, the exile case and the witnesses, the creed, the calf retold, the
# pair set, the release, the booths, the king's copy, the war's speech, the curses, Joshua encouraged and commissioned, the kings smitten, the Sodom lines, Jacob's testament). Fifteen
# cells and the table; every token probed (zero-report law); effects on every cell (the effects law); THE EXAM THE SEVEN MISHNAH AND TOSEFTA ROWS THE LEDGER CITES (Sotah 7:8 — the king's
# reading at the hakhel; Berakhot 9:2; Avot 1:6; Tosefta Sotah 11:2, 11:3, 11:4; Tosefta Ketubot 5:8 — read whole; 11:7 read whole and excluded; no docket, the lean form); the
# parameters the runner's DATA rows and TWO clock data on the calendar's keys (the hakhel's time; Moses' death date — THE MARKER'S DAY). The daemon law_covenant_return_charge given_at
# Deut 29:1, installed_by boot (the Deuteronomy daemons' form). Reading ledger: logic/oral_triage/deu_29_31_nitzavim_vayelech_2026-09-27.md; the lean exam: deu_29_31_nitzavim_vayelech_exam_2026-09-27.md.

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
from fractions import Fraction
import effects_layer as FX
import world_engine as WE
import cold_run_opening_speech as OS             # THE EDGE: covenant_return_charge -> opening_speech CALL, reference (Numbers 27:12-23's commission — the shepherd, the hand laid, the Urim, the receipt, the debit OPEN to 34:1-4; 2:7's forty years; 2:26-3:17 Sihon and Og; 1:15's officers; 3:21-28 Joshua encouraged and the plea — 31:3's pointer)
import cold_run_gad_reuben as GR                 # THE EDGE: covenant_return_charge -> gad_reuben CALL, reference (Numbers 32:28-33's holding east — 29:7's Reubenite, Gadite and half tribe of Manasseh; Joshua among the dividers)
import cold_run_good_land as GL                  # THE EDGE: covenant_return_charge -> good_land CALL, reference (8:4's garment and foot — a STATE told again at 29:4; 8:1, 8:6 live and multiply, walk in His ways — 30:16; 8:19-20's testimony — 30:17-18; 8:12-14 satiety before rebellion — 31:20; the receipt finder [], [], [])
import cold_run_exodus_story as ES               # THE EDGE: covenant_return_charge -> exodus_story CALL, reference (Exodus 1-12's signs and wonders retold at 29:1-2; 7:7 Moses eighty — THE MARKER'S YEAR; 13:21 the pillar; 16 the manna; 3:12 'I will be with you' — 31:23)
import cold_run_covenant_at_horeb as CH          # THE EDGE: covenant_return_charge -> covenant_at_horeb CALL, reference (5:1's four verbs — 29:1 and 31:12; 5:3's 'not with our fathers' — 29:13-14's DATA note; 9:10's day of the assembly — the hakhel's model)
import cold_run_hear_o_israel as HI              # THE EDGE: covenant_return_charge -> hear_o_israel CALL, reference (6:5's heart and soul — 30:2, 30:6, 30:10; the two inclinations — 31:21; 6:10's oath of the land — 30:20; 6:7's teaching — 31:19)
import cold_run_seven_nations as SN              # THE EDGE: covenant_return_charge -> seven_nations CALL, reference (7:8's oath by kind — 29:12's pointer a run citation; 7:24's name from under heaven — 29:19; 7:15's diseases — 30:7; 7:1-2 the ban — 31:3, 31:5)
import cold_run_obey_horeb as OH                 # THE EDGE: covenant_return_charge -> obey_horeb CALL, reference (4:25-31's exile case — 30:1-10's return told fully, 31:29's corruption; 4:26's witnesses — the chain 30:19, 31:28; 4:19's host apportioned — 29:25; 4:28's wood and stone — 29:16)
import cold_run_second_tablets as ST             # THE EDGE: covenant_return_charge -> second_tablets CALL, reference (10:8's Levites carry the ark — 31:9, 31:25; the ark's contents two arms — 31:26; 10:11's charge forward — 31:7; 10:16's heart and stiffening — 30:6, 31:27; 10:20's cleaving — 30:20)
import cold_run_not_righteousness as NR          # THE EDGE: covenant_return_charge -> not_righteousness CALL, reference (the stiff neck's six seats — 31:27 the seventh in a new order; 9:7, 9:24 the rebellion; 9:5's oath to the fathers — 29:12; 9:12 turn aside — 31:29)
import cold_run_blessing_and_curse as BC         # THE EDGE: covenant_return_charge -> blessing_and_curse CALL, reference (11:26's 'see, I set before you' — 30:15's form, '30:15-20 the run forward'; the pair 30:1, 30:19 REUSED; 11:28's turn aside — 31:29)
import cold_run_seducers as SE                   # THE EDGE: covenant_return_charge -> seducers CALL, reference (13:7's inciter in secret — 29:17's individual; 13:18's 'as He swore to your fathers' the pointer row's form — 29:12; 13:5's cleaving)
import cold_run_food_tithe as FT                 # THE EDGE: covenant_return_charge -> food_tithe CALL, reference (14:28's removal by the end analogy FROM 31:10 — the Sifrei 109:1-3, I2 the spine's own; the import-time scan censused)
import cold_run_release_firstborn as RF          # THE EDGE: covenant_return_charge -> release_firstborn CALL, reference (15:1's release at the year's end — 31:10 THE SOURCE SEAT of the Sifrei 111:1's analogy; the release date by CALL, 'no count' on the bare world)
import cold_run_festivals_judges as FJ           # THE EDGE: covenant_return_charge -> festivals_judges CALL, reference (16:13-16's feast of booths and the appearing — 31:10-11; who appears and the exempt — the hakhel's wider assembly, 31:12)
import cold_run_courts_prophet as CP             # THE EDGE: covenant_return_charge -> courts_prophet CALL, reference (17:14-20's king the hakhel's reader, Agrippas — Sotah 7:8; the copy of the law — 31:11: THE POINTER ROW 15b OWED FOR 31:10 PAID; 17:8-11 the court on earth — 30:11-14)
import cold_run_firstfruits_ebal_curses as FE    # THE EDGE: covenant_return_charge -> firstfruits_ebal_curses CALL, reference (28:15-68's curses — 29:19, 30:7; 28:11's three fruits — 30:9; 28:63's false six — 30:9's twin; 28:64's scattering; 28:69's footer — 29:8; 28:58's 'all the words of this law' — 29:28, 31:12)
import cold_run_refuge_war_family as RW          # THE EDGE: covenant_return_charge -> refuge_war_family CALL, reference (20:3-4's fear not — 31:6's plural imperative; 20:16-18's ban — 31:5)
import cold_run_tochacha as TC                   # THE EDGE: covenant_return_charge -> tochacha CALL, reference (Leviticus 26:15 break My covenant — 31:16, 31:20; 26:32-33 desolate and scattered — 29:22, 29:27; 26:38 devoured — 31:17; 26:40-42 the recovery — 30:2)
import cold_run_yovel as YV                      # THE EDGE: covenant_return_charge -> yovel CALL, reference (Leviticus 25's cycle — yovel.cycle(7) the release year's class sabbath_of_the_land; 'no count' on the bare world)
import cold_run_calendar as CA                   # THE EDGE: covenant_return_charge -> calendar CALL, reference (Exodus 23:10-11's sabbatical — the release; 23:14-17's pilgrimages and the appearing — 31:11; appearance_owed ZERO on the world)
import cold_run_moadim as MD                     # THE EDGE: covenant_return_charge -> moadim CALL, reference (Leviticus 23:34-43's feast of booths — the fifteenth, seven days: the key sukkot_1 of the_hakhel_time)
import cold_run_musafim as MU                    # THE EDGE: covenant_return_charge -> musafim CALL, reference (Numbers 29:12-38's booths — the eighth its own festival; the hakhel the night after the FIRST day, Sotah 7:8)
import cold_run_mamre as MA                      # THE EDGE: covenant_return_charge -> mamre CALL, reference (Genesis 19:24-25's overthrow of Sodom — 29:22 'like the overthrow', a comparative; brimstone at 19:24 and here alone in the Torah)
import cold_run_primeval as PV                   # THE EDGE: covenant_return_charge -> primeval CALL, reference (Genesis 6:3's hundred and twenty — 31:2's number, reprieve_of_a_hundred_and_twenty UNMOVED; 6:5's inclination — 31:21)
import cold_run_family as FA                     # THE EDGE: covenant_return_charge -> family CALL, reference (Genesis 47:29-31 Jacob's testament — 31:16's 'sleep with your fathers')
import cold_run_erection as ER                   # THE EDGE: covenant_return_charge -> erection CALL, reference (Exodus 33:9-10's pillar at the door — 31:15; 32:9 stiff-necked; 32:33 blotted from the book — 29:19; 34:15 whoring after — 31:16)
import cold_run_beha as BH                       # THE EDGE: covenant_return_charge -> beha CALL, reference (Numbers 11:16's present yourselves — 31:14; 12:5's cloud at the door — 31:15)
import cold_run_chukat as CK                     # THE EDGE: covenant_return_charge -> chukat CALL, reference (Numbers 20:22-29 Aaron's death, the succession, the thirty days, the death dates — Moses the 7th of Adar THE MARKER'S DAY; 21:21-35 Sihon and Og, the refrain — 31:4)
import cold_run_journeys as JR                   # THE EDGE: covenant_return_charge -> journeys CALL, reference (Numbers 33:2's four writings — 31:9, 31:22; 33:38 Aaron's death date — the eras' stamps)
import cold_run_vestments as VE                  # THE EDGE: covenant_return_charge -> vestments CALL, reference (Exodus 28:30's Urim — the first commission's judgment; the second by the LORD's own mouth, 31:14, 31:23)
import cold_run_shelach as SHL                   # THE EDGE: covenant_return_charge -> shelach CALL, reference (Numbers 13:16 Hoshea to Joshua — 32:44's old name; 14:39 Moses spoke these words — 31:1; 14:42 'the LORD is not among you' — 31:17)
import cold_run_place_name as PN                 # THE EDGE: covenant_return_charge -> place_name CALL, reference (12:5's place — 31:11's hakhel at the place; the stations' six rows; the Name pronounced only there)

'''
# ---- the generic helper block from the chapter 26-28 runner, by content markers ----
a = FEC.index('HERE = _os.path.dirname(_os.path.abspath(__file__))'); b = FEC.index('def LEN(b, c, v): return len(words(b, c, v))'); b = FEC.index('\n', b) + 1
helpers = FEC[a:b]
OLDW = "def W26(v): return words('Deut', 26, v)\ndef W27(v): return words('Deut', 27, v)\ndef W28(v): return words('Deut', 28, v)\ndef W(c, v): return words('Deut', c, v)"
assert helpers.count(OLDW) == 1
helpers = helpers.replace(OLDW, "def W29(v): return words('Deut', 29, v)\ndef W30(v): return words('Deut', 30, v)\ndef W31(v): return words('Deut', 31, v)\ndef W(c, v): return words('Deut', c, v)")
left = [l for l in helpers.split('\n') if re.search(r'(?<!\d)(26|27|28)(?!\d)', re.sub(r'2026-09-\d\d|0x05[0-9A-F]{2}', '', l))]
print('helper lines still naming 26, 27 or 28:', len(left), [l[:100] for l in left][:4]); assert not left, left[:3]
TAIL_A = '''def verse_text(ch, vs, book='Deut'): return ' '.join(words(book, ch, vs))
def _G(s): return s.split(' (')[0]   # a Hebrew token typed WITH ITS GLOSS beside it — the token alone returned (the lint's ninety-character window; 18b's form for the copied ink asserts)
DV = lambda c, v: ('Deut', c, v)
NEG_T = ('לא', 'ולא')   # (not; and not)
NAME = ('יהוה', 'ליהוה', 'ויהוה', 'ביהוה', 'מיהוה')   # (the LORD; to the LORD; and the LORD; in the LORD; from the LORD)
import difflib
def SH(a, b_): return sum(s for _, _, s in difflib.SequenceMatcher(a=words(*a), b=words(*b_)).get_matching_blocks())   # the reading's shared-run measure
CHS = (29, 30, 31)
NV = {c: len({v for (b, cc, v) in by if b == 'Deut' and cc == c}) for c in CHS}; assert NV == {29: 28, 30: 20, 31: 30}, NV   # twenty-eight, twenty and thirty verses (the reading's divisions assert — the identity in all three)
TOKN = {c: sum(len(W(c, v)) for v in range(1, NV[c] + 1)) for c in CHS}
print('THE TOKENS (printed before they are asserted):', TOKN)
TOKN_EXPECTED = _TOKN_EXPECTED_   # typed from the first derive's print (the callees' way — printed before typed)
if TOKN_EXPECTED: assert TOKN == TOKN_EXPECTED, (TOKN, TOKN_EXPECTED)
SPAN = [(29, v) for v in range(1, 29)] + [(30, v) for v in range(1, 21)] + [(31, v) for v in range(1, 31)]
assert len(SPAN) == 78

P_ = []   # the provenance trail of the case being run
def ink(ref, note):  P_.append(('INK',  'Deut %s — %s' % (ref, note) if not ref[:1].isupper() else '%s — %s' % (ref, note)))
def move(src, note): P_.append(('MOVE', '%s — %s' % (src, note)))
def dat(note):       P_.append(('DATA', note))
def hyp(note):       P_.append(('HYP',  note))     # THE LINK REVIEW LAW: a hypothesis — no teacher; counted apart, never as compiled
def out(verdict, effects):
    """verdict + registry-validated effects (the engine contract)"""
    FX.validate([e for e in effects if e != FX.NONE])
    return verdict, effects, list(P_)

# ---- THE INK, computed (the parser and the tokens; the reading's facts the expectations — every assert PROVEN at the reading, ch29_ink.py — COPIED from the reading's instrument by content markers in four blocks; the store-, shelf-, Onkelos- and register-bound asserts left to the reading; the parser's facts typed from the ink's own asserts) ----
def MARKS(c, v): return [t for t in verse_words('Deut', c, v) if t[-1] in '#~^%@|*']
PARSE = {(c, v): (ink_numbers(verse_words('Deut', c, v)), ink_ordinals(verse_words('Deut', c, v)), MARKS(c, v)) for (c, v) in SPAN}
NUMV = [k for k in PARSE if PARSE[k][0]]; ORDV = [k for k in PARSE if PARSE[k][1]]; STARV = [k for k in PARSE if PARSE[k][2]]
print('THE INK (printed before it is asserted): PARSE %s, NUMV %s, ORDV %s, STARV %s, TOKN %s' % ({k: p for k, p in PARSE.items() if p[0] or p[1] or p[2]}, NUMV, ORDV, STARV, TOKN))
assert {k: p for k, p in PARSE.items() if p[0] or p[1] or p[2]} == {(29, 4): ([40], [], []), (29, 7): ([Fraction(1, 2)], [], ['ולחצי%']), (30, 9): ([6], [], []), (31, 2): ([120], [], []), (31, 10): ([7], [], ['שנים*']), (31, 20): ([], [], ['ושבע*'])}, {k: p for k, p in PARSE.items() if p[0] or p[1] or p[2]}   # the reading's parser assert (ch29_ink.py): 29:4 forty, 29:7 the half (and to the half tribe), 30:9 THE FALSE SIX (rejoiced), 31:2 a hundred and twenty, 31:10 seven years (starred), 31:20 sated (starred — the seven's homograph)
assert NUMV == [(29, 4), (29, 7), (30, 9), (31, 2), (31, 10)] and ORDV == [] and STARV == [(29, 7), (31, 10), (31, 20)]
FALSE_SIX = W(30, 9)[W(30, 9).index('שש')]; assert FALSE_SIX == 'שש' and W(30, 9)[W(30, 9).index('שש') - 1] == 'כאשר' and W(31, 2)[2:6] == ['בן', 'מאה', 'ועשרים', 'שנה'] and W(29, 4)[2] == 'ארבעים' and W(31, 10)[4:7] == ['מקץ', 'שבע', 'שנים']   # (rejoiced — the numeral's consonants at 30:9 after 'as'; a son of a hundred and twenty years; forty; at the end of seven years) — the guard on the parser's false hit and the marker's number
SEVENS_HOMOGRAPHS = [(c, v, x) for (c, v) in SPAN for x in W(c, v) if x in ('נשבע', 'ושבע')]   # (swore; and sated) — the seven's consonants at 29:12, 30:20, 31:7 and 31:20: no numeral (the reading's parser)
assert [(c, v) for c, v, _ in SEVENS_HOMOGRAPHS] == [(29, 12), (30, 20), (31, 7), (31, 20)], SEVENS_HOMOGRAPHS
NEG = {(c, v): [x for x in W(c, v) if x in NEG_T] for (c, v) in SPAN if any(x in NEG_T for x in W(c, v))}
NAME_BARE = sum(1 for (c, v) in SPAN for x in W(c, v) if x == 'יהוה')   # (the LORD)
print('THE NEGATIONS AND THE NAME (printed before they are asserted):', NEG, NAME_BARE)
NAME_BARE_EXPECTED = _NAME_BARE_EXPECTED_   # typed from the first derive's print
if NAME_BARE_EXPECTED: assert NAME_BARE == NAME_BARE_EXPECTED, (NAME_BARE, NAME_BARE_EXPECTED)
assert {c: sum(len(v) for k, v in NEG.items() if k[0] == c) for c in CHS} == {29: 12, 30: 6, 31: 10}, {c: sum(len(v) for k, v in NEG.items() if k[0] == c) for c in CHS}   # the negations twelve, six, ten (the reading's frames assert)
assert [f'{c}:{v}' for c, v in SPAN if 'לאמר' in W(c, v)] == ['29:18', '30:12', '30:13', '31:10', '31:25'] and [(c, v) for c, v in SPAN if 'אם' in W(c, v) or 'ואם' in W(c, v)] == [(30, 4), (30, 17)] and [(c, v) for c, v in SPAN if 'פן' in W(c, v) or 'ופן' in W(c, v)] == [(29, 17)]   # ("saying" — the self-blesser's, the two sayings of 'who will go up / cross for us', and chapter 31's two frames, the hakhel's and the Levites'; "if" — the end of heaven and the heart turning; "lest" — the root)
'''
def block(start, end):
    i = INKB.index(start); j = INKB.index(end, i); assert i < j, (start[:40], end[:40]); return INKB[i:j]
ink_block = (block("# THE KIN FOUND BY COMPUTATION (the measure's A section", "# ---- THE ASSERTS TYPED FROM THE PRINTS (block a")
             + block("# THE KIN BY COMPUTATION (the closest re-scored in order)", "# THE TWINS DIFFED (shared / the longest run)")
             + block("# THE TWINS DIFFED (shared / the longest run)", "# THE FORMULAS (phrase seats by consonants")
             + block("# THE FORMULAS (phrase seats by consonants", "# ONKELOS OVER THE BOOK"))
lines = ink_block.split('\n')
DROP_RX = re.compile(r"(?<![A-Za-z_0-9])(byw|SG|sg|STORE_MISMATCH|VC|LED|sif|sif_he|onk|onk_he|Hb|HB0|ARM|SEATS|clean|heads|SP_|aramaic|arm|arm_e|E|kinrows|CS|_CS|H|A|HP|AP|sidx|glob|UIDS|PATCHED|OUT|EXP2DB|store|FAIL|_DUMP|_RC|_rink|DT|_MP)(?![A-Za-z_0-9])")
drop = [l for l in lines if not l.lstrip().startswith('#') and DROP_RX.search(l.split('   #')[0])]
print('dropped (the store-, shelf-, Onkelos- and register-bound lines):', len(drop), [d[:90] for d in drop])
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
n_as = ink_block.count('\nassert '); print('the ink block: %d lines, %d asserts' % (ink_block.count('\n'), n_as)); assert n_as >= 8, n_as
KIN43 = tuple(S.KIN_UNMOVED); KIN_EXPECTED = tuple(S.KIN_UNMOVED[k] for k in KIN43); OWN59 = tuple(S.NEW_EFFECTS)
HOLE_WORDS = r"^(covenant_words_keeping\w*|standing_before\w*|covenant_oath\w*|covenant_with_those\w*|heart_turning\w*|stubborn_self\w*|hidden_idolater\w*|curses_of_the_book\w*|name_blotted\w*|separated_for_evil\w*|land_brimstone\w*|nations_question\w*|uprooted_and\w*|hidden_things\w*|revealed_things\w*|return_to_the_lord\w*|captivity_returned\w*|gathered_from\w*|brought_into_the_fathers\w*|multiplied_above\w*|heart_circumcised_by\w*|curses_put_on\w*|return_and_hearken\w*|abounding_in\w*|rejoiced_over\w*|commandment_not\w*|commandment_in_mouth\w*|life_and_death_set\w*|choose_life\w*|living_and_multiplying\w*|perishing_for\w*|length_of_days\w*|joshua_to_cross\w*|nations_dispossessed\w*|be_strong_and\w*|joshua_charged\w*|law_written_and_given\w*|hakhel_\w*|moses_days\w*|moses_to_sleep\w*|future_whoring\w*|covenant_breaking\w*|face_hidden\w*|evils_and_troubles\w*|song_writing\w*|song_taught\w*|song_a_witness\w*|song_written_and\w*|joshua_commissioned_to\w*|lord_with_joshua\w*|book_of_the_law_beside\w*|book_a_witness\w*|elders_and_officers\w*|corruption_after\w*|song_spoken\w*)$"
TAIL_B = '''
# ---- THE COUNTER'S DAY AND THE MARKER'S (a bare world on the exodus epoch; the clock walks thirty-six days from Shevat 1 to Adar 7 at THE ONE MARKER 31:1 — the number's verse 31:2; the hakhel's time and the death date CLOCK DATA on the calendar's keys) ----
with contextlib.redirect_stdout(io.StringIO()):
    _WC = WE.World(era='the counter\\'s day and Moses\\' last day — chapters 29-31 on a bare world (the exodus epoch)', epoch='exodus')
_EX = _WC.clock.eras['exodus']
def DAY(y, m, d): return _WC.clock.day_in('exodus', y, m, d)
def DATE(day): return _EX.date(day)
COUNTER = DAY(40, 11, 1); MOSES_120 = DAY(40, 12, 7)
CLOCK = {'counter': DATE(COUNTER), 'marker': DATE(MOSES_120), 'marker_verse': 'Deut 31:2', 'marker_at': 'Deut 31:1', 'days_walked': MOSES_120 - COUNTER, 'clock_data': ['the_hakhel_time', 'the_death_date_of_moses', 'the_release_date']}
print('THE CLOCK (printed before it is asserted):', CLOCK)
assert CLOCK['counter'] == (40, 11, 1) and CLOCK['marker'] == (40, 12, 7) and CLOCK['days_walked'] > 0, CLOCK
assert all(k in WE.CAL_PARAMS for k in CLOCK['clock_data']), [k for k in CLOCK['clock_data'] if k not in WE.CAL_PARAMS]   # the two calendar parameters on file (add_types_ch29_b.py) and the release's date (13b's) — the received channel
assert WE.CAL_PARAMS['the_death_date_of_moses']['exercised_by'] == ['covenant_return_charge'] and 'covenant_return_charge' in WE.CAL_PARAMS['the_release_date']['exercised_by']

# ---- THE ONE DATABASE SCANNED (the holes' ground — nothing names the fifty-nine on their ledgers before this sitting; the references' entities and counts as the recon read them — DM4) ----
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
    """the entries of an effect in ONE full run of the tape (DM4's counts — the running world's): the one database folds several runs' rows under their sources (the checkpoint sections' names); the largest source is a whole run — None where the database is not built"""
    if not _os.path.exists(_WDB): return None
    c_ = sqlite3.connect('file:%s?mode=ro' % _WDB, uri=True)
    src = c_.execute("SELECT source FROM run_ledger GROUP BY source ORDER BY COUNT(*) DESC, source LIMIT 1").fetchone()[0]
    return c_.execute("SELECT COUNT(*) FROM run_ledger WHERE effect=? AND source=?", (effect, src)).fetchone()[0]
OWN59 = %(OWN59)r
assert len(OWN59) == 59 and len(set(OWN59)) == 59
HOLE_WORDS = r"%(HOLE_WORDS)s"
_hs = {ent: ledger_scan(ent, HOLE_WORDS) for ent in ('israel_people', 'yehoshua', 'moses', 'the_levites')}; HOLE_SCAN = None if any(v is None for v in _hs.values()) else {ent: [e for e in v if e not in OWN59] for ent, v in _hs.items()}   # this sitting's own names excluded once the fold carries them
KIN43 = %(KIN43)r
KIN_EXPECTED = %(KIN_EXPECTED)r   # DM4 — the recon's counts on the running world (ch29b_recon.out, section H; the callees' near names; the probe Q48's KIN tuple)
assert len(KIN43) == 43 == len(KIN_EXPECTED)
KIN_COUNTS = {k: count_scan(k) for k in KIN43}
REUSE7 = ('entered_the_covenant', 'became_the_lords_people_this_day', 'heaven_and_earth_witness', 'blessing_and_curse_set', 'cleaving_commanded', 'fear_not_promised', 'glory_appeared')
REUSE_BEFORE = %(REUSE_BEFORE)r   # the reuses' counts BEFORE this sitting's lines (the recon) — after the fold carries the new entries the count is the after (the tape's second run reads it so)
REUSE_AFTER = %(REUSE_AFTER)r
REUSE_COUNTS = {k: count_scan(k) for k in REUSE7}
SCANS = {k: effect_scan(k) for k in KIN43[:8] + REUSE7 + ('barred_from_the_land', 'reprieve_of_a_hundred_and_twenty', 'invested_office', 'plea_made')}
del _hs   # 9b's lesson: the raw scans are the database's state at import — the derived lists are equal on the cached and the full load
_FXV = yaml.safe_load(open(_os.path.join(HERE, 'effect_vocabulary.yaml'), encoding='utf-8'))['effects']
print('THE SCANS (printed before they are asserted): holes %%s; the kin counts %%s; the reuses %%s; the entities %%s' %% (HOLE_SCAN, KIN_COUNTS, REUSE_COUNTS, SCANS))
assert HOLE_SCAN is None or all(v == [] for v in HOLE_SCAN.values()), HOLE_SCAN   # THE HOLES' GROUND — nothing on the four ledgers named the fifty-nine before this sitting (DM4)
assert all(v is None for v in KIN_COUNTS.values()) or tuple(KIN_COUNTS.values()) == KIN_EXPECTED, [(k, KIN_COUNTS[k], e) for k, e in zip(KIN43, KIN_EXPECTED) if KIN_COUNTS[k] != e]   # the references' counts as the recon read them (DM4 — no second write)
assert all(v is None for v in REUSE_COUNTS.values()) or all(REUSE_COUNTS[k] in (REUSE_BEFORE[k], REUSE_AFTER[k]) for k in REUSE7), REUSE_COUNTS   # the reuses' counts the before (the first run) or the after (the fold carrying this sitting's lines)
SCANS_EXPECTED = _SCANS_EXPECTED_   # the entities per effect — typed from the first derive's print (the callees' way — printed before typed)
if SCANS_EXPECTED and any(v is not None for v in SCANS.values()): assert SCANS == SCANS_EXPECTED, [(k, SCANS[k], SCANS_EXPECTED.get(k)) for k in SCANS if SCANS[k] != SCANS_EXPECTED.get(k)]
assert all(k in _FXV for k in OWN59) and sum(1 for k in OWN59 if _FXV[k]['ledger_op'] == 'block') == 2 and sum(1 for k in OWN59 if _FXV[k]['ledger_op'] == 'status') == 31 and sum(1 for k in OWN59 if _FXV[k]['ledger_op'] == 'heaven') == 26, 'the fifty-nine on the registry (add_types_ch29_a.py)'
assert _FXV['entered_the_covenant']['ledger_op'] == 'status' and _FXV['heaven_and_earth_witness']['ledger_op'] == 'status' and _FXV['fear_not_promised']['ledger_op'] == 'heaven' and _FXV['glory_appeared']['ledger_op'] == 'heaven' and _FXV['barred_from_the_land']['ledger_op'] == 'heaven' and _FXV['reprieve_of_a_hundred_and_twenty']['ledger_op'] == 'timer', 'the reused and referenced rows\\' ops'
# THE TWINS DIFFED on the DB (the reading's kin asserts read again here — DM4; the shared run SH)
TWIN = {'29:1 vs 5:1': SH(DV(29, 1), DV(5, 1)), '29:23 vs 1 Kings 9:8': SH(DV(29, 23), ('1Kgs', 9, 8)), '29:28 vs 28:58': SH(DV(29, 28), DV(28, 58)), '29:28 vs 31:12': SH(DV(29, 28), DV(31, 12)), '30:2 vs 4:30': SH(DV(30, 2), DV(4, 30)), '30:6 vs 6:5': SH(DV(30, 6), DV(6, 5)),
        '30:9 vs 28:11': SH(DV(30, 9), DV(28, 11)), '30:9 vs 28:63': SH(DV(30, 9), DV(28, 63)), '30:12 vs 30:13': SH(DV(30, 12), DV(30, 13)), '30:15 vs 11:26': SH(DV(30, 15), DV(11, 26)), '30:18 vs 4:26': SH(DV(30, 18), DV(4, 26)), '30:19 vs 4:26': SH(DV(30, 19), DV(4, 26)), '30:19 vs 31:28': SH(DV(30, 19), DV(31, 28)),
        '31:2 vs 34:7': SH(DV(31, 2), DV(34, 7)), '31:2 vs 3:27': SH(DV(31, 2), DV(3, 27)), '31:2 vs Gen 6:3': SH(DV(31, 2), ('Gen', 6, 3)), '31:6 vs 31:8': SH(DV(31, 6), DV(31, 8)), '31:7 vs 31:23': SH(DV(31, 7), DV(31, 23)), '31:7 vs 10:11': SH(DV(31, 7), DV(10, 11)), '31:7 vs Josh 1:6': SH(DV(31, 7), ('Josh', 1, 6)),
        '31:9 vs 31:22': SH(DV(31, 9), DV(31, 22)), '31:10 vs 15:1': SH(DV(31, 10), DV(15, 1)), '31:15 vs Num 12:5': SH(DV(31, 15), ('Num', 12, 5)), '31:15 vs Exod 33:9': SH(DV(31, 15), ('Exod', 33, 9)), '31:16 vs Gen 47:30': SH(DV(31, 16), ('Gen', 47, 30)), '31:23 vs Num 27:23': SH(DV(31, 23), ('Num', 27, 23)),
        '31:27 vs 9:13': SH(DV(31, 27), DV(9, 13)), '31:29 vs 4:25': SH(DV(31, 29), DV(4, 25)), '31:30 vs 32:44': SH(DV(31, 30), DV(32, 44)), '29:22 vs Gen 19:24': SH(DV(29, 22), ('Gen', 19, 24)), '29:4 vs 8:4': SH(DV(29, 4), DV(8, 4)), '29:1 vs 31:1': SH(DV(29, 1), DV(31, 1)), '31:1 vs Num 14:39': SH(DV(31, 1), ('Num', 14, 39))}
print('THE TWINS DIFFED (printed before they are asserted):', TWIN)
TWIN_EXPECTED = _TWIN_EXPECTED_
if TWIN_EXPECTED: assert TWIN == TWIN_EXPECTED, [(k, TWIN[k], TWIN_EXPECTED.get(k)) for k in TWIN if TWIN[k] != TWIN_EXPECTED.get(k)]   # typed from the first derive's print (the callees' way — printed before typed)
assert TWIN['29:1 vs 5:1'] >= 7 and TWIN['30:2 vs 4:30'] >= 6 and TWIN['31:7 vs 31:23'] >= 10 and TWIN['29:28 vs 28:58'] >= 6 and TWIN['30:19 vs 4:26'] >= 7, TWIN   # the reading's largest twins (the two calls seven in order, the return six, the two charges ten, all the words of this law six, the witnesses seven)
'''
for _k, _v in (('%(OWN59)r', repr(OWN59)), ('%(HOLE_WORDS)s', HOLE_WORDS), ('%(KIN43)r', repr(KIN43)), ('%(KIN_EXPECTED)r', repr(KIN_EXPECTED)), ('%(REUSE_BEFORE)r', repr(S.REUSE_BEFORE)), ('%(REUSE_AFTER)r', repr(S.REUSE_AFTER))): TAIL_B = TAIL_B.replace(_k, _v)
TAIL_B = TAIL_B.replace('%%', '%')   # the print's own %s escaped inside the template
def _read(name):
    p = f'{SP}/{name}'; return open(p).read().strip() if os.path.exists(p) else 'None'
TWIN_EXPECTED = _read('ch29_twin_expected.txt'); SCANS_EXPECTED = _read('ch29_scans_expected.txt'); TOKN_EXPECTED = _read('ch29_tokn_expected.txt'); NAME_BARE_EXPECTED = _read('ch29_name_bare_expected.txt')   # the first derive's prints, parsed by ast from the fast checker's output and written to the files — never typed by hand
GLOSS = {'את': 'the object marker', 'ואת': 'and-it', 'כל': 'all', 'וכל': 'and all', 'על': 'on', 'ועל': 'and on', 'אל': 'to', 'ואל': 'and to', 'לא': 'not', 'ולא': 'and not', 'כי': 'for', 'אם': 'if', 'ואם': 'and if', 'פן': 'lest', 'ופן': 'and lest', 'לאמר': 'saying',
         'יהוה': 'the LORD', 'ליהוה': 'to the LORD', 'ויהוה': 'and the LORD', 'ביהוה': 'in the LORD', 'מיהוה': 'from the LORD', 'אלהיך': 'your God', 'אלהינו': 'our God', 'אלהים': 'gods', 'אחרים': 'other',
         'ויקרא': 'and he called', 'משה': 'Moses', 'ישראל': 'Israel', 'ויאמר': 'and he said', 'אלהם': 'to them', 'לעשות': 'to do', 'דברי': 'the words of', 'התורה': 'the law', 'הזאת': 'this', 'הזה': 'this', 'בספר': 'in the book', 'ספר': 'the book of',
         'ושבת': 'and you shall return', 'עד': 'to', 'ושמעת': 'and you shall hearken', 'בקלו': 'to His voice', 'בפרי': 'in the fruit of', 'בטנך': 'your body', 'ובפרי': 'and in the fruit of', 'בהמתך': 'your cattle', 'אדמתך': 'your ground', 'כאשר': 'as', 'שש': 'rejoiced',
         'בן': 'a son of', 'מאה': 'a hundred', 'ועשרים': 'and twenty', 'שנה': 'years', 'תעבר': 'you shall cross', 'הירדן': 'the Jordan', 'עמך': 'with you', 'ירפך': 'He will fail you', 'יעזבך': 'He will forsake you',
         'נשבע': 'He swore', 'לאבתיך': 'to your fathers', 'לאברהם': 'to Abraham', 'ליצחק': 'to Isaac', 'וליעקב': 'and to Jacob', 'הברכה': 'the blessing', 'והקללה': 'and the curse', 'העידתי': 'I call to witness', 'בכם': 'against you', 'היום': 'this day',
         'החיים': 'the life', 'והמות': 'and the death', 'השמים': 'the heavens', 'הארץ': 'the earth', 'בכל': 'with all', 'לבבך': 'your heart', 'ובכל': 'and with all', 'נפשך': 'your soul', 'והסתרתי': 'and I will hide', 'פני': 'My face',
         'חזק': 'be strong', 'ואמץ': 'and of good courage', 'חזקו': 'be strong (plural)', 'ואמצו': 'and of good courage (plural)', 'מקץ': 'at the end of', 'שבע': 'seven', 'שנים': 'years', 'ארון': 'the ark of', 'ברית': 'the covenant of', 'בעמוד': 'in a pillar of', 'ענן': 'cloud',
         'ערפך': 'your neck', 'הקשה': 'the stiff', 'קשה': 'stiff', 'ערף': 'neck', 'זבת': 'flowing with', 'חלב': 'milk', 'ודבש': 'and honey', 'סדם': 'Sodom', 'ועמרה': 'and Gomorrah', 'אדמה': 'Admah', 'וצבים': 'and Zeboiim (the qere)', 'וצביים': 'and Zeboiim (the ketiv)',
         'עץ': 'wood', 'ואבן': 'and stone', 'בקצה': 'at the end of', 'בשמים': 'in heaven', 'הוא': 'it', 'בפיך': 'in your mouth', 'ובלבבך': 'and in your heart', 'שכב': 'sleep', 'עם': 'with', 'אבתיך': 'your fathers', 'השירה': 'the song', 'לעד': 'for a witness', 'בבני': 'against the children of',
         'הברית': 'the covenant', 'בברית': 'into the covenant of', 'בריתי': 'My covenant', 'בריתו': 'His covenant', 'ושב': 'and He will return', 'ישוב': 'He will again', 'תשוב': 'you shall return', 'והשבת': 'and you take to heart', 'ארבעים': 'forty', 'ולחצי': 'and to the half of',
         'בחג': 'at the feast of', 'גפרית': 'brimstone', 'הנסתרת': 'the hidden things', 'הסכות': 'booths', 'והפר': 'and break', 'ולענה': 'and wormwood', 'ומלח': 'and salt', 'וצרות': 'and troubles', 'יהושע': 'Joshua', 'נון': 'Nun', 'ראש': 'gall', 'רבות': 'many', 'רעות': 'evils',
         'ואנכי': 'and I', 'לעברך': 'to enter you', 'ובאלתו': 'and into His oath', 'ואלה': 'and these', 'האלה': 'these', 'הקהל': 'assemble', 'הקהילו': 'assemble (plural)', 'קהל': 'the assembly of', 'ולמדה': 'and teach it', 'שימה': 'put it', 'בפיהם': 'in their mouths', 'ושבע': 'and sated'}
MISSING = []
def glossify(text):
    def repl(m):
        tok = m.group(1); key = tok.rstrip('*%')
        if key not in GLOSS: MISSING.append(tok); return m.group(0)
        return "_G('%s (%s)')" % (tok, GLOSS[key])
    out_ = []
    for l in text.split('\n'):
        if l.lstrip().startswith('#') or 'STOP = set((' in l or l.lstrip().startswith("'") and '   # (' in l: out_.append(l); continue   # the comments and the glossed STOP set kept
        out_.append(re.sub(r"'([א-תװ-״]+[*%]?)'", repl, l))
    return '\n'.join(out_)
TAIL_A = glossify(TAIL_A); ink_block = glossify(ink_block)
assert not MISSING, ('a Hebrew token without a gloss in the table', sorted(set(MISSING)))
src = HEAD + helpers + TAIL_A.replace('_TOKN_EXPECTED_', TOKN_EXPECTED).replace('_NAME_BARE_EXPECTED_', NAME_BARE_EXPECTED) + ink_block + TAIL_B.replace('_TWIN_EXPECTED_', TWIN_EXPECTED).replace('_SCANS_EXPECTED_', SCANS_EXPECTED) + FACTS
open(f'{SP}/ch29_part1.py', 'w', encoding='utf-8').write(src)
import py_compile; py_compile.compile(f'{SP}/ch29_part1.py', doraise=True)
lint = subprocess.run([sys.executable, f'{ROOT}/logic/solo_tools/gloss_lint.py', f'{SP}/ch29_part1.py'], capture_output=True, text=True).stdout.strip().split('\n')[-1]; print('the lint on part 1:', lint); assert lint.endswith('0 flag(s)'), lint
print('part1 derived: %d bytes; helpers %d, ink block %d (asserts %d); dropped %d store-bound lines; the callees\' facts %d bytes; TWIN_EXPECTED %s; SCANS_EXPECTED %s; TOKN %s; NAME_BARE %s' % (len(src), len(helpers), len(ink_block), n_as, len(drop), len(FACTS), TWIN_EXPECTED[:40], SCANS_EXPECTED[:40], TOKN_EXPECTED, NAME_BARE_EXPECTED))

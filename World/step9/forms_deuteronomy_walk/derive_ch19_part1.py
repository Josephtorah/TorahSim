#!/usr/bin/env python3
# THE DEUTERONOMY WALK 16b: cold_run_refuge_war_family.py PART 1 derived — the head typed here; the generic helper block COPIED from the chapter 17-18 runner by content
# markers (HERE = … through def LEN — the parser exec, the DB, the phrase/lemma/diff helpers; W17/W18 made W19, W20, W21 and W); THE INK BLOCKS COPIED from the reading's
# own instrument ch19_ink.py by content markers — THREE blocks (the kin by computation over the three chapters; the formulas over the Torah and the Bible; the kin re-scored
# and the twins diffed), the store-, shelf- and Onkelos-bound lines DROPPED by name (10b's lesson 6 — the count read from the print); the counter's day, the one-database
# scans, and THE CALLEES' FACTS (typed in ch19_callees_facts.py from ch19_callees.out — read before any assert was typed). Asserted substitutions throughout.
# derive_ch17_part1.py's form over three chapters. RUN FROM THE REPO ROOT.
import subprocess, re, os, sys
ROOT = _ROOT
SP = os.path.dirname(os.path.abspath(__file__))
CPR = open(f'{ROOT}/World/step9/cold_run_courts_prophet.py', encoding='utf-8').read()
INKB = open(f'{SP}/ch19_ink.py', encoding='utf-8').read()
FACTS = open(f'{SP}/ch19_callees_facts.py', encoding='utf-8').read()
assert FACTS.startswith('\n# ---- THE CALLEES\' FACTS'), 'the callees\' facts typed from the print (ch19_callees_facts.py)'
HEAD = '''#!/usr/bin/env python3
# DEUTERONOMY 19:1-21:23 — THE CITIES OF REFUGE (when the LORD cuts off the nations, three cities in the midst, the way prepared and the border in three, this is
# the word of the manslayer, unknowingly and not hating from yesterday, the forest and the ax, the avenger's hot heart and the boundary, the three more conditioned,
# the hater who lies in wait), THE LANDMARK AND THE WITNESSES (the landmark of the first ones, one witness for any iniquity, by the mouth not by writing, the violent
# witness and the woman, the inquiry well at three verses, as he plotted, the rest hear and fear, the talion in "be"), THE PRIEST'S SPEECH AND THE OFFICERS' EXEMPTIONS
# (when you go out to war, the priest anointed for war, hear Israel the fourth, the four exemptions, the fearful and the faint of heart, the captains and the guards),
# THE SIEGE (call to it for peace, tribute and servitude both, the siege and the males, houses full of every good thing, the far cities and the seven, no breath left
# alive, that they teach you not, the trees of the siege), THE BROKEN-NECKED HEIFER (when murderers multiplied, slain on the ground in the field, the measuring court,
# the heifer never worked, the priests the sons of Levi, our hands have not shed, atone for your people), THE CAPTIVE (when you go out to war the second, a woman of
# beautiful form, the head the nails the garment, if you delight not in her), THE FIRSTBORN'S DOUBLE (two wives loved and hated, on the day he gives his sons
# inheritance, double of all that he has), THE STUBBORN AND REBELLIOUS SON (a son not a daughter, judged by his end, they chastise him and he hears not, his father and
# his mother seize him, a glutton and a drunkard, all the men of his city stone him) and THE HANGED (a sin worthy of death and you hang him, him and not two in one
# day, his corpse shall not stay the night, a curse of God is a hanged one, not defile your land); THE READBACK'S FORMS ON FILE, NO NEW FORM (THE DEUTERONOMY WALK
# sitting 16b — THE LEAN PASS, 2026-09-25; World/step9/DEUTERONOMY_WALK.md "Sitting 16b"; the state doc's #215). ONE RUNNER OVER THREE CHAPTERS AND THREE UNITS (the
# span three ranges); THIRTEEN own-day lines at the counter's day (40, 11, 1), NO marker: refuge_cities_declared (19:1-3, 7-10), manslayer_and_murderer_declared
# (19:4-6, 11-13), landmark_declared (19:14), witnesses_law_declared (19:15-21), war_speech_declared (20:1-9), siege_law_declared (20:10-15),
# seven_nations_herem_declared (20:16-18), siege_trees_declared (20:19-20), heifer_rite_declared (21:1-9), captive_wife_declared (21:10-14), firstborn_portion_declared
# (21:15-17), rebellious_son_declared (21:18-21), hanged_burial_declared (21:22-23) — FORTY-FIVE writes on Israel (thirty-four STATUSES, ten BLOCKS, one HEAVEN entry),
# every one its first entry. THE KIN'S CELLS BY CALL (twenty-three runners, every edge REFERENCE); THE TAPE'S LINES BY KIND (the nations cut off, the three cities set
# apart, the idolater's trial, the inciter's hear-and-fear, the seven nations devoted, the shema, Sihon's messengers, Midian's captives and spoil, the diviners, the
# heifer's statute, Lamech's two wives, Leah's womb, Joseph's portion, the testament, Zelophehad's statute, Peor's hanging, the blasphemer's sentence and stoning, the
# baker hanged, Noah's blood required). Nine cells and the table; every token probed (zero-report law); effects on every cell (the effects law); THE EXAM THE
# TWENTY-EIGHT MISHNAH ROWS THE LEDGER CITES AT LEAST TWICE (Makkot 1:4, 2:2, 2:4, 2:6, 2:7, 2:8; Sotah 8:1-3, 8:5-6, 9:1-2, 9:5-6, 9:9; Sanhedrin 6:3-5, 8:1-5;
# Bekhorot 8:1, 8:9; Bava Batra 8:5; Parah 1:1 — read whole; no docket, the lean form); the parameters the runner's DATA rows (no clock datum). The daemon
# law_refuge_war_family given_at Deut 19:1, installed_by boot (the Deuteronomy daemons' form). Reading ledger: logic/oral_triage/deu_19_21_shoftim_ki_teitzei_2026-09-24.md;
# the lean exam: deu_19_21_shoftim_ki_teitzei_exam_2026-09-25.md.

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
import cold_run_place_name as PN               # THE EDGE: refuge_war_family -> place_name CALL, reference (12:29's opening at 19:1; 12:25's "right in the eyes" at 21:9)
import cold_run_obey_horeb as OH               # THE EDGE: refuge_war_family -> obey_horeb CALL, reference (4:41-43's three cities and the manslayer defined — 19:2, 19:4)
import cold_run_refuge as RG                   # THE EDGE: refuge_war_family -> refuge CALL, reference (Numbers 35's six cities, the iron, the smiter, the mode, the intents, the manners, the border, the return; the one witness, the avenger's hand and the land's atonement DATA read)
import cold_run_ordinances as OR               # THE EDGE: refuge_war_family -> ordinances CALL, reference (Exodus 21:29's enemy-ox clock; Exodus 23:1's violent witness and false report)
import cold_run_courts_prophet as CP           # THE EDGE: refuge_war_family -> courts_prophet CALL, reference (17:6-7's one witness, the two for every death, the seven investigations, the witnesses' hand; 17:8's pairs and the three courts; 18:6's Levite who is a priest; 18:9's learning)
import cold_run_seducers as SE                 # THE EDGE: refuge_war_family -> seducers CALL, reference (13:15's seven interrogations, 13:10's stoning rite and the hand first, the purge formula's nine seats)
import cold_run_festivals_judges as FJ         # THE EDGE: refuge_war_family -> festivals_judges CALL, reference (16:18's court for all Israel and the three tiers)
import cold_run_lev24 as L24                   # THE EDGE: refuge_war_family -> lev24 CALL, reference (Leviticus 24:20's talion as money — 19:21's "eye in eye")
import cold_run_seven_nations as SN            # THE EDGE: refuge_war_family -> seven_nations CALL, reference (7:1-2's seven, the ban and its condition; 7:17-18's fear not; 7:25-26's abomination)
import cold_run_midian as MD                   # THE EDGE: refuge_war_family -> midian CALL, reference (Numbers 31:6's priest anointed for war and the trumpets; 31:7-18's every male, the captives, the females kept, the chapter's own ask deuteronomy_20; 31:28's tribute)
import cold_run_opening_speech as OP           # THE EDGE: refuge_war_family -> opening_speech CALL, reference (2:24-26's Sihon commanded and the speech resumed — 20:10's peace call)
import cold_run_chukat as CK                   # THE EDGE: refuge_war_family -> chukat CALL, reference (Numbers 19:2's yoke, blemish and age — 21:3's heifer)
import cold_run_incense_shekel as IS_          # THE EDGE: refuge_war_family -> incense_shekel CALL, reference (Exodus 30:15-16's atonement for souls — 21:8's ransom word)
import cold_run_primeval as PV                 # THE EDGE: refuge_war_family -> primeval CALL, reference (Genesis 16:6's humbling — 21:14's "since you have humbled her")
import cold_run_family as FA                   # THE EDGE: refuge_war_family -> family CALL, reference (Genesis 48:22's one portion and the birthright's run, the gift and its disputes, 49:3's first of my strength — 21:16-17)
import cold_run_zelophehad as ZL               # THE EDGE: refuge_war_family -> zelophehad CALL, reference (Numbers 27:8-11's source of the rule and the firstborn's double — 21:16)
import cold_run_mamre as MR                    # THE EDGE: refuge_war_family -> mamre CALL, reference (Genesis 25:31-34's birthright sold — 21:17's birthright's earliest seat)
import cold_run_release_firstborn as RF        # THE EDGE: refuge_war_family -> release_firstborn CALL, reference (15:19's consecrated from the womb — 21:15's firstborn for the priest)
import cold_run_mekoshesh as MK                # THE EDGE: refuge_war_family -> mekoshesh CALL, reference (Numbers 15:35-36's stoning, the stones and the stone, the hanging after — 21:21-22)
import cold_run_balak as BK                    # THE EDGE: refuge_war_family -> balak CALL, reference (Numbers 25:4's hanging before the sun — 21:22)
import cold_run_sanctions as SA                # THE EDGE: refuge_war_family -> sanctions CALL, reference (Leviticus 20:9's and 24:15-16's reviler by the Name — 21:23's curse)
import cold_run_pre_sinai as PS_               # THE EDGE: refuge_war_family -> pre_sinai CALL, reference (Genesis 9:6's blood shed by man — 21:23; blood_required on noach the reference)
import cold_run_good_land as GL                # THE EDGE: refuge_war_family -> good_land CALL, reference (the register's receipt seats — 20:17 the one seat in the three chapters)

'''
# ---- the generic helper block from the chapter 17-18 runner, by content markers ----
a = CPR.index('HERE = _os.path.dirname(_os.path.abspath(__file__))'); b = CPR.index('def LEN(b, c, v): return len(words(b, c, v))'); b = CPR.index('\n', b) + 1
helpers = CPR[a:b]
OLDW = "def W17(v): return words('Deut', 17, v)\ndef W18(v): return words('Deut', 18, v)\ndef W(c, v): return words('Deut', c, v)"
assert helpers.count(OLDW) == 1
helpers = helpers.replace(OLDW, "def W19(v): return words('Deut', 19, v)\ndef W20(v): return words('Deut', 20, v)\ndef W21(v): return words('Deut', 21, v)\ndef W(c, v): return words('Deut', c, v)")
left = [l for l in helpers.split('\n') if re.search(r'(?<!\d)(17|18)(?!\d)', re.sub(r'2026-09-\d\d|0x05[0-9A-F]{2}', '', l))]
print('helper lines still naming 17 or 18:', len(left), [l[:100] for l in left][:4]); assert not left, left[:3]
TAIL_A = '''def verse_text(ch, vs, book='Deut'): return ' '.join(words(book, ch, vs))
DV = lambda c, v: ('Deut', c, v)
NEG_T = ('לא', 'ולא')   # (not; and not)
NAME = ('יהוה', 'ליהוה', 'ויהוה', 'ביהוה', 'מיהוה')   # (the LORD; to the LORD; and the LORD; in the LORD; from the LORD)
import difflib
def SH(a, b_): return sum(s for _, _, s in difflib.SequenceMatcher(a=words(*a), b=words(*b_)).get_matching_blocks())   # the reading's shared-run measure
CHS = (19, 20, 21)
NV = {c: len({v for (b, cc, v) in by if b == 'Deut' and cc == c}) for c in CHS}; assert NV == {19: 21, 20: 20, 21: 23}, NV   # twenty-one, twenty and twenty-three verses (the reading's divisions assert)
TOKN = {c: sum(len(W(c, v)) for v in range(1, NV[c] + 1)) for c in CHS}; assert TOKN == {19: 332, 20: 316, 21: 354}, TOKN   # the three chapters' tokens (the reading's store assert — the store the DB at every verse)
SPAN = [(19, v) for v in range(1, 22)] + [(20, v) for v in range(1, 21)] + [(21, v) for v in range(1, 24)]

P_ = []   # the provenance trail of the case being run
def ink(ref, note):  P_.append(('INK',  'Deut %s — %s' % (ref, note) if not ref[:1].isupper() else '%s — %s' % (ref, note)))
def move(src, note): P_.append(('MOVE', '%s — %s' % (src, note)))
def dat(note):       P_.append(('DATA', note))
def hyp(note):       P_.append(('HYP',  note))     # THE LINK REVIEW LAW: a hypothesis — no teacher; counted apart, never as compiled
def out(verdict, effects):
    """verdict + registry-validated effects (the engine contract)"""
    FX.validate([e for e in effects if e != FX.NONE])
    return verdict, effects, list(P_)

# ---- THE INK, computed (the parser and the tokens; the reading's facts the expectations — every assert PROVEN at the reading, ch19_ink.py — COPIED from the reading's instrument by content markers in three blocks; the store-, shelf- and Onkelos-bound asserts left to the reading; the parser's facts typed from the ink's own asserts) ----
def MARKS(c, v): return [t for t in verse_words('Deut', c, v) if t[-1] in '#~^%@|*']
PARSE = {(c, v): (ink_numbers(verse_words('Deut', c, v)), ink_ordinals(verse_words('Deut', c, v)), MARKS(c, v)) for (c, v) in SPAN}
NUMV = [k for k in PARSE if PARSE[k][0]]; ORDV = [k for k in PARSE if PARSE[k][1]]; STARV = [k for k in PARSE if PARSE[k][2]]
print('THE INK (printed before it is asserted): PARSE %s, NUMV %s, ORDV %s, STARV %s, TOKN %s' % ({k: p for k, p in PARSE.items() if p[0] or p[1] or p[2]}, NUMV, ORDV, STARV, TOKN))
assert {k: p for k, p in PARSE.items() if p[0] or p[1] or p[2]} == {(19, 2): ([3], [], []), (19, 3): ([3], [], []), (19, 5): ([1], [], []), (19, 7): ([3], [], []), (19, 9): ([3], [], []), (19, 11): ([1], [], []), (19, 15): ([1, 2, 3], [], ['שני^']), (19, 17): ([2], [], ['שני^']), (21, 15): ([2, 1, 1], [], ['שתי^', 'האחת#', 'והאחת#']), (21, 17): ([2], [], [])}, {k: p for k, p in PARSE.items() if p[0] or p[1] or p[2]}   # (two; two, fem.; the one; and the one) TEN number verses, NONE in chapter 20; no ordinal; the starred tokens 19:15's and 19:17's "two" and 21:15's "two … the one … and the one" — the reading's parser assert
assert NUMV == [(19, 2), (19, 3), (19, 5), (19, 7), (19, 9), (19, 11), (19, 15), (19, 17), (21, 15), (21, 17)] and ORDV == [] and STARV == [(19, 15), (19, 17), (21, 15)]
NEG = {(c, v): [x for x in W(c, v) if x in NEG_T] for (c, v) in SPAN if any(x in NEG_T for x in W(c, v))}
NAME_BARE = sum(1 for (c, v) in SPAN for x in W(c, v) if x == 'יהוה')   # (the LORD)
print('THE NEGATIONS AND THE NAME (printed before they are asserted):', NEG, NAME_BARE)
'''
# ---- THE INK BLOCKS from the reading's instrument, by content markers — three blocks ----
def block(start, end):
    i = INKB.index(start); j = INKB.index(end, i); assert i < j, (start[:40], end[:40]); return INKB[i:j]
ink_block = block("# THE KIN FOUND BY COMPUTATION (the measure's A section", "# ---- THE SHELF BY POSITION") + block("# ---- THE FORMULAS OVER THE TORAH", "# ---- THE KIN BY COMPUTATION AND THE TWINS DIFFED") + block("# ---- THE KIN BY COMPUTATION AND THE TWINS DIFFED", "# ---- ONKELOS OVER THE BOOK")
lines = ink_block.split('\n')
DROP_RX = re.compile(r"(?<![A-Za-z_0-9])(byw|SG|sg|STORE_MISMATCH|VC|LED|sif|sif_he|onk|onk_he|Hb|HB0|SP_|aramaic|arm|arm_e|E|kinrows|heads|CS|H|A|HP|AP|sidx|glob|UIDS|PATCHED|OUT|EXP2DB|store|FAIL)(?![A-Za-z_0-9])")
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
n_as = ink_block.count('\nassert '); print('the ink block: %d lines, %d asserts' % (ink_block.count('\n'), n_as)); assert n_as >= 8, n_as
TAIL_B = '''
# ---- THE COUNTER'S DAY AND THE ONE DATABASE SCANNED (a bare world on the exodus epoch; no clock walk these chapters — no marker, no stretch, no clock datum: the captive's month a parameter, the executed man's day a clock word without a datum) ----
with contextlib.redirect_stdout(io.StringIO()):
    _WC = WE.World(era='the counter\\'s day — chapters 19-21 on a bare world (the exodus epoch)', epoch='exodus')
_EX = _WC.clock.eras['exodus']
def DAY(y, m, d): return _WC.clock.day_in('exodus', y, m, d)
def DATE(day): return _EX.date(day)
COUNTER = DAY(40, 11, 1)
CLOCK = {'counter': DATE(COUNTER), 'no_marker': True, 'no_clock_datum': True}
print('THE CLOCK (printed before it is asserted):', CLOCK)
assert CLOCK['counter'] == (40, 11, 1), CLOCK

# ---- THE ONE DATABASE SCANNED (the holes' ground — nothing names the forty-five on Israel before this sitting; the references' entities as the recon read them) ----
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
OWN45 = ('three_cities_separated_commanded', 'way_prepared_commanded', 'land_divided_in_three_commanded', 'three_more_cities_conditioned', 'manslayer_flight_permitted', 'murderer_extradition_commanded', 'murderer_pity_barred', 'innocent_blood_purge_commanded', 'landmark_removal_barred', 'two_or_three_witnesses_required', 'witnesses_inquiry_commanded', 'plotting_witness_talion_commanded', 'talion_pity_barred', 'war_fear_barred', 'priest_war_speech_commanded', 'officers_exemptions_commanded', 'fearful_exemption_commanded', 'captains_appointed_commanded', 'peace_call_commanded', 'tribute_service_commanded', 'siege_males_smitten_commanded', 'spoil_permitted', 'far_cities_scope_declared', 'nothing_alive_left_commanded', 'abominations_teaching_barred', 'fruit_tree_cutting_barred', 'siege_works_permitted', 'slain_found_measuring_commanded', 'heifer_neck_broken_commanded', 'priests_approach_commanded', 'elders_hands_washed_commanded', 'elders_declaration_commanded', 'innocent_blood_atoned', 'captive_wife_permitted', 'captive_mourning_month_commanded', 'captive_sale_barred', 'captive_release_commanded', 'firstborn_double_portion_commanded', 'firstborn_right_transfer_barred', 'rebellious_son_seized_commanded', 'rebellious_son_stoning_commanded', 'hanging_after_death_commanded', 'corpse_overnight_barred', 'same_day_burial_commanded', 'land_defilement_barred')
HOLE_WORDS = r"^(three_cities_separated\\w*|way_prepared\\w*|land_divided\\w*|three_more_cities\\w*|manslayer_flight\\w*|murderer_extradition\\w*|murderer_pity\\w*|innocent_blood_purge\\w*|landmark_removal\\w*|two_or_three_witnesses\\w*|witnesses_inquiry\\w*|plotting_witness\\w*|talion_pity\\w*|war_fear\\w*|priest_war_speech\\w*|officers_exemptions\\w*|fearful_exemption\\w*|captains_appointed\\w*|peace_call\\w*|tribute_service\\w*|siege_males\\w*|spoil_permitted|far_cities\\w*|nothing_alive\\w*|abominations_teaching\\w*|fruit_tree\\w*|siege_works\\w*|slain_found\\w*|heifer_neck\\w*|priests_approach\\w*|elders_hands\\w*|elders_declaration\\w*|innocent_blood_atoned|captive_wife\\w*|captive_mourning\\w*|captive_sale\\w*|captive_release\\w*|firstborn_double\\w*|firstborn_right\\w*|rebellious_son\\w*|hanging_after\\w*|corpse_overnight\\w*|same_day_burial\\w*|land_defilement\\w*)\\b"
_hs = ledger_scan('israel_people', HOLE_WORDS); HOLE_SCAN = None if _hs is None else [e for e in _hs if e not in OWN45]   # this sitting's own names excluded once the fold carries them
CITIES_SCAN = effect_scan('cities_set_apart'); PITY_SCAN = effect_scan('pity_barred'); HEARS_SCAN = effect_scan('israel_hears_and_fears'); ONEW_SCAN = effect_scan('one_witness_barred'); TWOW_SCAN = effect_scan('two_witnesses_required'); HANDF_SCAN = effect_scan('witnesses_hand_first_commanded'); ABOM_SCAN = effect_scan('abominations_learning_barred')
FEAR_SCAN = effect_scan('fear_not_promised'); CAPT_SCAN = effect_scan('taken_captive'); SPOIL_SCAN = effect_scan('spoil_taken'); BOUND_SCAN = effect_scan('boundary_witnessed'); HANGED_SCAN = effect_scan('hanged'); BURIED_SCAN = effect_scan('buried'); BLOOD_SCAN = effect_scan('blood_required'); ATONED_SCAN = effect_scan('atoned_forgiven')
FBH_SCAN = effect_scan('firstborn_by_the_head'); HATED_SCAN = effect_scan('hated'); STONED_SCAN = effect_scan('stoned'); PUT_SCAN = effect_scan('put_to_death'); PURGED_SCAN = effect_scan('evil_purged_from_the_midst'); FLEES_SCAN = effect_scan('flees_to_refuge'); DWELLS_SCAN = effect_scan('dwells_in_refuge'); LANDPOL_SCAN = effect_scan('land_polluted_by_blood'); CITYDEV_SCAN = effect_scan('city_devoted'); DRIVEN_SCAN = effect_scan('nations_driven_out'); LASHES_SCAN = effect_scan('lashes')
del _hs   # 9b's lesson: the raw scans are the database's state at import — the derived lists are equal on the cached and the full load
_FXV = yaml.safe_load(open(_os.path.join(HERE, 'effect_vocabulary.yaml'), encoding='utf-8'))['effects']
print('THE SCANS (printed before they are asserted): holes %s; cities %s; pity %s; hears %s; one witness %s; two witnesses %s; hand first %s; abominations %s; fear not %s; captive %s; spoil %s; boundary %s; hanged %s; buried %s; blood %s; atoned %s; firstborn by the head %s; hated %s; stoned %s; put to death %s; purged %s; flees %s; dwells %s; land polluted %s; city devoted %s; driven out %s; lashes %s' % (HOLE_SCAN, CITIES_SCAN, PITY_SCAN, HEARS_SCAN, ONEW_SCAN, TWOW_SCAN, HANDF_SCAN, ABOM_SCAN, FEAR_SCAN, CAPT_SCAN, SPOIL_SCAN, BOUND_SCAN, HANGED_SCAN, BURIED_SCAN, BLOOD_SCAN, ATONED_SCAN, FBH_SCAN, HATED_SCAN, STONED_SCAN, PUT_SCAN, PURGED_SCAN, FLEES_SCAN, DWELLS_SCAN, LANDPOL_SCAN, CITYDEV_SCAN, DRIVEN_SCAN, LASHES_SCAN))
assert HOLE_SCAN in ([], None), HOLE_SCAN   # THE HOLES' GROUND — nothing on Israel named the forty-five before this sitting (DJ4)
_I = ['israel_people']
assert CITIES_SCAN in (_I, None) and PITY_SCAN in (_I, None) and HEARS_SCAN in (_I, None) and ONEW_SCAN in (_I, None) and TWOW_SCAN in (_I, None) and HANDF_SCAN in (_I, None) and ABOM_SCAN in (_I, None) and FEAR_SCAN in (['isaac', 'jacob', 'moses', 'yehoshua'], None) and CAPT_SCAN in (['israel_people', 'lot', 'the_captives_of_midian'], None) and SPOIL_SCAN in (['israel_people', 'the-sons'], None) and BOUND_SCAN in (['the_heap_and_pillar'], None) and HANGED_SCAN in (['the_baker'], None) and BLOOD_SCAN in (['noach'], None) and FBH_SCAN in (['esau', 'perez'], None) and HATED_SCAN in (['the-sons'], None) and STONED_SCAN in (['the_blasphemer', 'the_wood_gatherer'], None) and (PUT_SCAN is None or len(PUT_SCAN) == 7) and PURGED_SCAN in ([], None) and FLEES_SCAN in ([], None) and DWELLS_SCAN in ([], None) and LANDPOL_SCAN in ([], None) and CITYDEV_SCAN in ([], None) and DRIVEN_SCAN in ([], None) and LASHES_SCAN in ([], None), (CITIES_SCAN, PITY_SCAN, HEARS_SCAN, ONEW_SCAN, TWOW_SCAN, HANDF_SCAN, ABOM_SCAN, FEAR_SCAN, CAPT_SCAN, SPOIL_SCAN, BOUND_SCAN, HANGED_SCAN, BLOOD_SCAN, FBH_SCAN, HATED_SCAN, STONED_SCAN, PUT_SCAN, PURGED_SCAN, FLEES_SCAN, DWELLS_SCAN, LANDPOL_SCAN, CITYDEV_SCAN, DRIVEN_SCAN, LASHES_SCAN)   # the references' entities as the recon read them from the snapshot (DJ4 — no second write)
SCANS_EXPECTED = _SCANS_EXPECTED_   # the buried and the atoned lists — typed from the first derive's print (the callees' way — printed before typed)
if SCANS_EXPECTED: assert (BURIED_SCAN, ATONED_SCAN) in ((SCANS_EXPECTED['buried'], SCANS_EXPECTED['atoned']), (None, None)), (BURIED_SCAN, ATONED_SCAN)
assert all(k in _FXV for k in OWN45) and sum(1 for k in OWN45 if _FXV[k]['ledger_op'] == 'block') == 10 and sum(1 for k in OWN45 if _FXV[k]['ledger_op'] == 'status') == 34 and sum(1 for k in OWN45 if _FXV[k]['ledger_op'] == 'heaven') == 1, 'the forty-five on the registry (add_types_ch19_a.py)'
# THE TWINS DIFFED on the DB (the reading's kin asserts read again here — DJ4; the shared run SH)
TWIN = {'19:1 vs 12:29': SH(DV(19, 1), DV(12, 29)), '19:4 vs 4:42': SH(DV(19, 4), DV(4, 42)), '19:4 vs Exod 21:13': SH(DV(19, 4), ('Exod', 21, 13)), '19:6 vs Josh 20:5': SH(DV(19, 6), ('Josh', 20, 5)), '19:8 vs 12:20': SH(DV(19, 8), DV(12, 20)), '19:9 vs 11:22': SH(DV(19, 9), DV(11, 22)), '19:13 vs 13:9': SH(DV(19, 13), DV(13, 9)), '19:15 vs 17:6': SH(DV(19, 15), DV(17, 6)), '19:15 vs Num 35:30': SH(DV(19, 15), ('Num', 35, 30)), '19:16 vs Exod 23:1': SH(DV(19, 16), ('Exod', 23, 1)), '19:17 vs 17:9': SH(DV(19, 17), DV(17, 9)), '19:19 vs 13:6': SH(DV(19, 19), DV(13, 6)), '19:20 vs 13:12': SH(DV(19, 20), DV(13, 12)), '19:21 vs Exod 21:24': SH(DV(19, 21), ('Exod', 21, 24)), '20:1 vs 7:18': SH(DV(20, 1), DV(7, 18)), '20:3 vs 6:4': SH(DV(20, 3), DV(6, 4)), '20:3 vs 31:6': SH(DV(20, 3), DV(31, 6)), '20:4 vs 1:30': SH(DV(20, 4), DV(1, 30)), '20:5 vs 20:6': SH(DV(20, 5), DV(20, 6)), '20:5 vs 20:7': SH(DV(20, 5), DV(20, 7)), '20:17 vs Josh 9:1': SH(DV(20, 17), ('Josh', 9, 1)), '21:1 vs 17:2': SH(DV(21, 1), DV(17, 2)), '21:3 vs Num 19:2': SH(DV(21, 3), ('Num', 19, 2)), '21:4 vs Exod 13:13': SH(DV(21, 4), ('Exod', 13, 13)), '21:5 vs 18:5': SH(DV(21, 5), DV(18, 5)), '21:6 vs 21:4': SH(DV(21, 6), DV(21, 4)), '21:9 vs 12:25': SH(DV(21, 9), DV(12, 25)), '21:10 vs 20:1': SH(DV(21, 10), DV(20, 1)), '21:11 vs Gen 29:17': SH(DV(21, 11), ('Gen', 29, 17)), '21:14 vs 24:1': SH(DV(21, 14), DV(24, 1)), '21:15 vs Gen 4:19': SH(DV(21, 15), ('Gen', 4, 19)), '21:17 vs Gen 49:3': SH(DV(21, 17), ('Gen', 49, 3)), '21:18 vs Jer 5:23': SH(DV(21, 18), ('Jer', 5, 23)), '21:21 vs 13:12': SH(DV(21, 21), DV(13, 12)), '21:21 vs 22:21': SH(DV(21, 21), DV(22, 21)), '21:23 vs Gen 9:6': SH(DV(21, 23), ('Gen', 9, 6))}
print('THE TWINS DIFFED (printed before they are asserted):', TWIN)
TWIN_EXPECTED = _TWIN_EXPECTED_
if TWIN_EXPECTED: assert TWIN == TWIN_EXPECTED, TWIN   # typed from the first derive's print (the callees' way — printed before typed)
'''
TWIN_EXPECTED = os.environ.get('TWIN_EXPECTED', 'None'); SCANS_EXPECTED = os.environ.get('SCANS_EXPECTED', 'None')
src = HEAD + helpers + TAIL_A + ink_block + TAIL_B.replace('_TWIN_EXPECTED_', TWIN_EXPECTED).replace('_SCANS_EXPECTED_', SCANS_EXPECTED) + FACTS
open(f'{SP}/ch19_part1.py', 'w', encoding='utf-8').write(src)
import py_compile; py_compile.compile(f'{SP}/ch19_part1.py', doraise=True)
print('part1 derived: %d bytes; helpers %d, ink block %d (asserts %d); dropped %d store-bound lines; the callees\' facts %d bytes; TWIN_EXPECTED %s; SCANS_EXPECTED %s' % (len(src), len(helpers), len(ink_block), n_as, len(drop), len(FACTS), TWIN_EXPECTED[:40], SCANS_EXPECTED[:40]))

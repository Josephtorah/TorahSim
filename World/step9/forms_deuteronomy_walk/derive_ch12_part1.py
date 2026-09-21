#!/usr/bin/env python3
# THE DEUTERONOMY WALK 10b: cold_run_place_name.py PART 1 derived — the head typed here; the generic helper block COPIED from the chapter-11 runner by content
# markers (HERE = … through def LEN — the parser exec, the DB, the phrase/lemma/diff helpers; W11 made W12); THE INK BLOCK COPIED from the reading's own
# instrument ch12_ink.py by content markers (the parser measured on every verse — ONE NUMBER VERSE 12:14 [1], ONE STARRED TOKEN 12:17 — through the kin found
# by computation: every assert PROVEN at sitting 10; the sequence module's names made the exec'd parser's; the store-bound asserts left to the reading); the
# counter's day, the two parameters, the one-database scans and THE CALLEES' FACTS (asserted from ch12_callees.out — read before any assert was typed) typed.
# Asserted substitutions throughout. derive_ch11_part1.py's form. RUN FROM THE REPO ROOT.
import subprocess, re, os
ROOT = _ROOT
SP = os.path.dirname(os.path.abspath(__file__))
BC = open(f'{ROOT}/World/step9/cold_run_blessing_and_curse.py', encoding='utf-8').read()
INKB = open(f'{ROOT}/World/step9/forms_deuteronomy_walk/ch12_ink.py', encoding='utf-8').read()
HEAD = '''#!/usr/bin/env python3
# DEUTERONOMY 12:1-31 — THE HEADER AND THE DEMOLITION, THE PLACE CHOSEN, THE BURNT OFFERINGS ONLY THERE, THE PROFANE SLAUGHTER, THE BLOOD AND THE GATES, THE
# BORDER ENLARGED AND THE ALTAR, THE NATIONS CUT OFF AND THE ABOMINATION — THE READBACK'S FORMS ON FILE, NO NEW FORM (THE DEUTERONOMY WALK sitting 10b,
# 2026-09-21; World/step9/DEUTERONOMY_WALK.md "Sitting 10b"; the state doc's #201). THE PLACE WHICH THE LORD WILL CHOOSE INSTALLED HERE with no seat before it
# (12:5 — 'will choose' none before the chapter; the Name pronounced only there, Sotah 38a; 'in one of your tribes' [1] the chapter's one number verse): THE
# ERAS TABLE'S OWN INK — high_places_banned REUSED (the erection's BLOCK on the-land, a second entry at the chapter's own day; the stations' six rows read by
# CALL from shemini_day, sanctions and journeys, unmoved). THE CODE'S FOUR HOLES compiled at the counter's day (40, 11, 1), FOUR own-day lines, NO marker: the
# Name's erasure (12:4 — name_erasure_barred), the place's law with the rejoicing (12:5-14 — place_chosen_required, rejoicing_before_the_lord_commanded, the
# reuse), THE SLAUGHTER LAW RELEASED IN NEW WORDS AS A LAW CHANGED BY A PLACE (12:15-28 — profane_slaughter_permitted conditional on the entry; the rite 'as I
# have commanded you' THE RECEIPT WITHOUT THE NAME, its referent the oral law: the_rite_of_slaughter and the_wilderness_flesh PARAMETERS; the gates' bar with
# THE LADDER OF A FORTIORI and the lashes; the Levite), the inquiry after the gods (12:29-31 — foreign_rite_inquiry_barred; no Molech named). The state row
# 12:9 SUPPLIED with no write (chapter 8's fifth form); the pointer at 12:20 to Exodus 34:24; the header's twin Leviticus 26:46; THE KIN FOUND BY COMPUTATION.
# Six cells and the table; every token probed (zero-report law); effects on every cell (the effects law); the DATA rows the docket added. The daemon
# law_place_name given_at Deut 12:1, installed_by boot (the Deuteronomy daemons' form). Reading ledger: logic/oral_triage/deu_12_reeh_2026-09-20.md (197
# sources, 6 claims); the exam's docket: deu_12_reeh_exam_2026-09-20.md (1,538 rows — 1,115 READ WHOLE in three runs, 423 carried with their ledgers' own
# verdicts: LAW 311 / DERIVATION 300 / DISPUTE 209 / CONTEXT 515 / OUTSIDE 203).

# ---- THE HONEST-PAIRING GUARD ----------------------------------------------------------------------------
import os as _os, sys as _sys
_sys.path.insert(0, _os.path.dirname(_os.path.abspath(__file__)))
_ROOT = _os.path.normpath(_os.path.join(_os.path.dirname(_os.path.abspath(__file__)), '..', '..'))   # THE PORTABLE REPO: the repo root from this file's own place
from compile_guards import check_honest_pairing as _chp
_P = _os.path.abspath(__file__)
GUARDED = _chp(_P, 'CASES', 2)
assert GUARDED == 0, ("the guard counted %d expectations, the tripwire holds 0" % GUARDED)   # RETYPED after the generator (the cells' asks summed)
print('guard: %d expectations checked, every one a literal from the answer sheet [honest-pairing guard satisfied]' % GUARDED)
import sqlite3, sys, io, re, contextlib, collections, unicodedata, yaml
from collections import Counter
import effects_layer as FX
import world_engine as WE
import cold_run_sanctions as SA               # THE EDGE: place_name -> sanctions CALL, reference (12:13-16, 20-25 Leviticus 17 released and restated — the outside slaughter, the blood, the covering; 12:31's children in the fire the Molech's kin; the platform's eras; the land)
import cold_run_korach as KR                  # THE EDGE: place_name -> korach CALL, reference (12:6, 11, 17's dues Numbers 18's; 18:31's 'in every place' the Levites' tithe eaten anywhere against the second tithe at the place — THE TWO TITHES; portion_declared 18:20 the Levite's reason at 12:12)
import cold_run_seven_nations as SN           # THE EDGE: place_name -> seven_nations CALL, reference (12:2-3's demolition 7:5's in new words — five verbs for four; 12:29-31's abomination and snare 7:25-26's; the ban's debit open, no second debit)
import cold_run_erection as ER                # THE EDGE: place_name -> erection CALL, reference (the demolition's verbs at Exodus 34:13, Deuteronomy 7:5 AND 12:3 in the cell's own assert; 34:24's 'I will enlarge your border' the pointer's target at 12:20; erected Exod 40:17 the tape's line)
import cold_run_ordinances as OR              # THE EDGE: place_name -> ordinances CALL, reference (12:26-27's altar Exodus 20:21-23's — 'in every place where I cause My name to be mentioned', the transposition's seat; 12:30's 'and I will do so too' 23:24's 'you shall not do after their deeds'; the pillars broken)
import cold_run_journeys as JO                # THE EDGE: place_name -> journeys CALL, reference (12:2-3's objects Numbers 33:52's three; 12:29's 'possess and dwell' 33:53's; the private altar's eras agreeing with the table; dispossession_commanded 33:50 the tape's line)
import cold_run_pre_sinai as PS               # THE EDGE: place_name -> pre_sinai CALL, reference (12:23's 'the blood is the life' Genesis 9:4's limb from the living — limb_barred on the tape; the blood ban and scope by CALL; 'shall be poured' the sin offering's verb at Leviticus 4)
import cold_run_calendar as CA                # THE EDGE: place_name -> calendar CALL, reference (Exodus 23:15's 'as I commanded you' THE RECEIPT'S ONE KIN WITH A WRITTEN CALLEE against 12:21's oral rite; flesh in milk from 12:25's redundant 'you shall not eat it' — the kid in milk's three seats)
import cold_run_shemini_day as SD             # THE EDGE: place_name -> shemini_day CALL, reference (THE ERAS TABLE — the six rows read, unmoved: high_places_banned REUSED; the karet matrix, the eleven differences, the ink of the ban 'Lev 17:4 and Deut 12:8')
import cold_run_tochacha as TC                # THE EDGE: place_name -> tochacha CALL, reference (12:1 Leviticus 26:46's twin — the header the fold's footer; 12:10's 'dwell in safety' 26:5's; the blessing's entry the cell's)
import cold_run_covenant_at_horeb as CH       # THE EDGE: place_name -> covenant_at_horeb CALL, reference (12:12 and 12:18's household list the fourth word's 5:14 — the servants' rest, without the ox and the ass, with the Levite)
import cold_run_hear_o_israel as HI           # THE EDGE: place_name -> hear_o_israel CALL, reference (12:25 and 12:28's 'the good and the right' 6:18's pair — Heaven's eyes and men's)
import cold_run_obey_horeb as OH              # THE EDGE: place_name -> obey_horeb CALL, reference (12:2's 'destroy, you shall destroy' 4:26's 'perish, you shall perish' in the piel — the doubled verb's kin)
import cold_run_good_land as GL               # THE EDGE: place_name -> good_land CALL, reference (8:19-20's perishing_testified the lemma's kin; 12:30's 'serve their gods' the second word's pair; 8:20's 'not hearken')
import cold_run_blessing_and_curse as BC      # THE EDGE: place_name -> blessing_and_curse CALL, reference (11:32's 'keep to do the statutes and the judgments' — 12:1 reopens the frame; 11:31's possess and dwell 12:10's and 12:29's; blessing_and_curse_set the tape's last Deuteronomy 11 line)
import cold_run_beha as BH                    # THE EDGE: place_name -> beha CALL, reference (12:9's rest the ark's seeking rest at Numbers 10:33 — the two nouns four ways; the state row's kin)
import cold_run_borders as BR                 # THE EDGE: place_name -> borders CALL, reference (12:1's 'in the land … on the earth' the land-bound rule — Mishnah Kiddushin 1:9 through the Sifrei 59:5)

'''
# ---- the generic helper block from the chapter-11 runner, by content markers ----
a = BC.index('HERE = _os.path.dirname(_os.path.abspath(__file__))'); b = BC.index('def LEN(b, c, v): return len(words(b, c, v))'); b = BC.index('\n', b) + 1
helpers = BC[a:b]
assert helpers.count("def W11(v): return words('Deut', 11, v)") == 1
helpers = helpers.replace("def W11(v): return words('Deut', 11, v)", "def W12(v): return words('Deut', 12, v)")
assert 'W11' not in helpers and '11' not in re.sub(r'0x0591|0x05C7|0x05AF', '', helpers), [l for l in helpers.split('\n') if '11' in l][:3]
TAIL_A = '''def verse_text(ch, vs, book='Deut'): return ' '.join(words(book, ch, vs))
D12 = lambda v: ('Deut', 12, v)
NEG = ('לא', 'ולא')   # (not; and not)
NAME = ('יהוה', 'ליהוה', 'ויהוה', 'ביהוה', 'מיהוה')   # (the LORD; to the LORD; and the LORD; in the LORD; from the LORD)
import difflib
def SH(a, b_): return sum(s for _, _, s in difflib.SequenceMatcher(a=words(*a), b=words(*b_)).get_matching_blocks())

P_ = []   # the provenance trail of the case being run
def ink(ref, note):  P_.append(('INK',  'Deut %s — %s' % (ref, note) if not ref[:1].isupper() else '%s — %s' % (ref, note)))
def move(src, note): P_.append(('MOVE', '%s — %s' % (src, note)))
def dat(note):       P_.append(('DATA', note))
def hyp(note):       P_.append(('HYP',  note))     # THE LINK REVIEW LAW: a hypothesis — no teacher; counted apart, never as compiled
def out(verdict, effects):
    """verdict + registry-validated effects (the engine contract)"""
    FX.validate([e for e in effects if e != FX.NONE])
    return verdict, effects, list(P_)

# ---- THE INK, computed (the parser and the tokens; the reading's facts the expectations — every assert PROVEN at the reading, ch12_ink.py — COPIED from the reading's instrument by content markers, the sequence module's names made the exec'd parser's; the store-bound asserts left to the reading) ----
SPAN = [(12, v) for v in range(1, 32)]
def MARKS(c, v): return [t for t in verse_words('Deut', c, v) if t[-1] in '#~^%@|*']
def N(b, c, v): return ink_numbers(verse_words(b, c, v))
NUMS = {v: ink_numbers(verse_words('Deut', 12, v)) for v in range(1, 32)}
ORDS = {v: ink_ordinals(verse_words('Deut', 12, v)) for v in range(1, 32)}
PARSED = {(12, v): n for v, n in NUMS.items() if n}
TOKN = sum(len(W12(v)) for v in range(1, 32)); LETN = sum(len(x) for v in range(1, 32) for x in W12(v))
assert PARSED == {(12, 14): [1]} and all(o == [] for o in ORDS.values()) and TOKN == 520 and LETN == 2051, (PARSED, ORDS, TOKN, LETN)   # ONE NUMBER VERSE (12:14 "in one of your tribes" [1]); 520 tokens, 2,051 letters (measured at the reading, the ink's header)
'''
# ---- THE INK BLOCK from the reading's instrument, by content markers ----
i = INKB.index("# ---- THE INK, computed from the Tanakh DB and the snapshot store ----")
j = INKB.index("# ---- ONKELOS — the renderings' seats")
ink_block = INKB[i:j]
lines = ink_block.split('\n')
drop = [l for l in lines if 'STORE_MISMATCH' in l or 'byw[' in l or 'SG.items()' in l or l.startswith('with contextlib.redirect_stdout(io.StringIO()):') or l.strip() == 'import cold_run_sequence as CS' or l.startswith('# ---- THE INK, computed from the Tanakh DB and the snapshot store') or l.startswith('# THE STORE = THE DB at EVERY verse')]
print('dropped (the store-bound lines):', len(drop), [d[:70] for d in drop])
assert len(drop) == 7, len(drop)   # READ FROM THE PRINT (the first derive dropped 6 and the fast checker found the seventh — the store's '?' glosses assert on SG.items(), a NameError at part 1 line 124)
lines = [l for l in lines if l not in drop]
STOP_OLD = "STOP = set('את ואת אשר כל וכל על ועל אל ואל לא ולא כי אם יהוה אלהיך אלהיכם לך לכם בו שם שמה גם מן ממך עד הוא היא אתם אתה אנכי אני לו לה בכל כאשר כן הימים היום אלה האלה בארץ הארץ אשר ואם או פן ופן'.split())"
STOP_NEW = ("STOP = set(('את ואת אשר כל וכל על ועל אל ואל '   # (the object marker, and-it, which, all, on, to — the particles)\n"
            "            'לא ולא כי אם יהוה אלהיך אלהיכם '   # (not, for, if; the LORD, your God)\n"
            "            'לך לכם בו שם שמה גם מן ממך עד '   # (to you, in it, there, also, from, until)\n"
            "            'הוא היא אתם אתה אנכי אני לו לה '   # (he, she, you, I, to him, to her)\n"
            "            'בכל כאשר כן הימים היום אלה האלה '   # (in all, as, so, the days, today, these)\n"
            "            'בארץ הארץ אשר ואם או פן ופן').split())   # (in the land, the land, which, and if, or, lest) — the stopword set glossed piece by piece (the lint's ninety-character window)")
assert lines.count(STOP_OLD) == 1, lines.count(STOP_OLD)
lines[lines.index(STOP_OLD)] = STOP_NEW
ink_block = '\n'.join(lines)
n_cs = ink_block.count('CS.'); assert n_cs >= 4, n_cs
ink_block = ink_block.replace('CS.ink_numbers', 'ink_numbers').replace('CS.verse_words', 'verse_words').replace('CS.ink_ordinals', 'ink_ordinals')
assert 'CS.' not in ink_block and 'SG[' not in ink_block and 'byw' not in ink_block and 'VC[' not in ink_block and 'STORE_' not in ink_block and 'sg(' not in ink_block, 'a store-bound name survived'
n_as = ink_block.count('\nassert '); print('the ink block: %d lines, %d asserts' % (ink_block.count('\n'), n_as)); assert n_as >= 60, n_as
TAIL_B = '''
# ---- THE COUNTER'S DAY AND THE TWO PARAMETERS (a bare world on the exodus epoch; no clock walk this chapter — no marker, no stretch) ----
with contextlib.redirect_stdout(io.StringIO()):
    _WC = WE.World(era='the counter\\'s day — chapter 12 on a bare world (the exodus epoch)', epoch='exodus')
_EX = _WC.clock.eras['exodus']
def DAY(y, m, d): return _WC.clock.day_in('exodus', y, m, d)
def DATE(day): return _EX.date(day)
COUNTER = DAY(40, 11, 1)
RITE = WE.CAL_PARAMS['the_rite_of_slaughter']['value']; WILDERNESS_FLESH = WE.CAL_PARAMS['the_wilderness_flesh']['value']   # THE TWO PARAMETERS read (exercised_by place_name) — never a constant in the code: the rite is ORAL, the written text holds none
CLOCK = {'counter': DATE(COUNTER), 'rite_keys': sorted(RITE), 'flesh_arms': sorted(WILDERNESS_FLESH), 'no_marker': True}
assert CLOCK == {'counter': (40, 11, 1), 'rite_keys': ['the_agent', 'the_bird', 'the_signs', 'the_uncertainty', 'the_wild_and_the_bird'], 'flesh_arms': ['r_akiva', 'r_yishmael', 'the_exile'], 'no_marker': True}, CLOCK
assert RITE['the_signs'].startswith('the gullet and the windpipe') and 'Chullin 28a:5' in RITE['the_signs'] and WILDERNESS_FLESH['r_yishmael'].startswith('the flesh of desire FORBIDDEN in the wilderness') and WILDERNESS_FLESH['r_akiva'].startswith('the flesh of desire NEVER forbidden') and WILDERNESS_FLESH['the_exile'].startswith('the release PERSISTS'), (RITE, WILDERNESS_FLESH)

# ---- THE ONE DATABASE SCANNED (the holes' ground — nothing names the place chosen, the rejoicing, the profane slaughter, the gates' bar, the Levite's forsaking, the Name's erasure or the inquiry on Israel before this sitting; high_places_banned on the-land alone) ----
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
OWN7 = ('name_erasure_barred', 'place_chosen_required', 'rejoicing_before_the_lord_commanded', 'profane_slaughter_permitted', 'holy_things_in_the_gates_barred', 'levite_forsaking_barred', 'foreign_rite_inquiry_barred')
PLACE_WORDS = r"\\b(place_chosen\\w*|rejoicing_before\\w*|profane_slaughter\\w*|holy_things_in_the_gates\\w*|levite_forsaking\\w*|name_erasure\\w*|foreign_rite\\w*|the place which the LORD (?:your God )?will choose|profane slaughter|forsake the Levite)\\b"
_ps = ledger_scan('israel_people', PLACE_WORDS); PLACE_SCAN = None if _ps is None else [e for e in _ps if e not in OWN7]   # this sitting's own seven excluded once the fold carries them
_hs = effect_scan('high_places_banned'); HPB_SCAN = None if _hs is None else sorted(set(_hs))
del _ps, _hs   # 9b's lesson: the raw scans are the database's state at import — the derived lists are equal on the cached and the full load
_FXV = yaml.safe_load(open(_os.path.join(HERE, 'effect_vocabulary.yaml'), encoding='utf-8'))['effects']
assert PLACE_SCAN in ([], None), PLACE_SCAN   # THE HOLES' GROUND — nothing on Israel named the seven before this sitting (DD4)
assert HPB_SCAN in (['the-land'], None), HPB_SCAN   # high_places_banned on the-land alone (the erection's write) before the reuse
assert all(k in _FXV for k in OWN7) and _FXV['high_places_banned']['ledger_op'] == 'block' and 'THE DEUTERONOMY WALK 10b' in _FXV['high_places_banned']['ink'], 'the seven on the registry; the reuse amended (add_types_ch12.py)'

# ---- THE CALLEES' FACTS (every edge live at the cells that consume them; the values asserted from the callees' own print — ch12_callees.out, read before any assert was typed; the older runners' cells take q and return a dict, the Deuteronomy runners' take (case, data) and return a tuple — the print settled each form) ----
SA_IND = SA.outside('individual'); SA_COMMON = SA.outside('for_commoner'); SA_BIRD = SA.outside('bird'); SA_AGENCY = SA.outside('agency'); SA_CROSS = SA.outside('cross_cases')
SA_BAN = SA.blood('ban'); SA_WHICH = SA.blood('which_blood'); SA_ATONES = SA.blood('atones'); SA_LASHES = SA.blood('lashes'); SA_KARET_OWN = SA.blood('karet_own_eating'); SA_EATER = SA.blood('eater_not_feeder')
SA_HUNTED = SA.covering('hunted_of_any_kind'); SA_CONSEC = SA.covering('consecrated'); SA_FOOT = SA.covering('not_with_the_foot')
SA_SEED = SA.molech('seed_scope'); SA_FAMILY = SA.molech('family'); SA_PRED = SA.molech('predicate'); SA_STRAY = SA.molech('all_who_stray')
SA_ERAS = SA.platform('eras'); SA_DIFF = SA.platform('differences'); SA_CLASSES = SA.platform('classes'); SA_SERVICE = SA.platform('service_by'); SA_NOKARET = SA.platform('no_karet_for_platform'); SA_LAND = SA.frame('land')
KR_BIK = KR.the_gifts({'ask': 'bikkurim'}, KR.DATA); KR_BLEM = KR.the_gifts({'ask': 'blemished_firstborn'}, KR.DATA); KR_BREAST = KR.the_gifts({'ask': 'breast_and_thigh'}, KR.DATA)
KR_EVERY = KR.the_tithe({'ask': 'every_place'}, KR.DATA); KR_EXCL = KR.the_tithe({'ask': 'exclusion_table'}, KR.DATA); KR_CONF = KR.the_tithe({'ask': 'confession'}, KR.DATA)
SN_SHADE = SN.the_seven_nations({'ask': 'the_asherah_shade'}, SN.DATA); SN_WOOD = SN.the_seven_nations({'ask': 'the_asherah_wood'}, SN.DATA); SN_BAN = SN.the_seven_nations({'ask': 'the_ban'}, SN.DATA); SN_NOCOV = SN.the_seven_nations({'ask': 'no_covenant'}, SN.DATA)
SN_BURN = SN.the_images_and_the_devoted({'ask': 'burn_the_images'}, SN.DATA); SN_SNARED = SN.the_images_and_the_devoted({'ask': 'lest_snared'}, SN.DATA); SN_ABOM = SN.the_images_and_the_devoted({'ask': 'abomination_to_the_lord'}, SN.DATA); SN_HOUSE = SN.the_images_and_the_devoted({'ask': 'into_your_house'}, SN.DATA); SN_COVET = SN.the_images_and_the_devoted({'ask': 'not_covet_silver_gold'}, SN.DATA)
ER_FIRST = ER.covenant('demolition_first_seat'); ER_GROWS = ER.covenant('demolition_grows'); ER_CUT4 = ER.covenant('cut_four'); ER_ASH = ER.covenant('asherav_homograph'); ER_ASC = ER.repeats('as_commanded_without_kaf')
OR_EARTH = OR.altar('earth_altar'); OR_EVERY = OR.altar('every_place'); OR_OLAH = OR.altar('olah_on_it'); OR_SHEL = OR.altar('shelamim_on_it'); OR_SWORD = OR.altar('sword_profanes'); OR_PILLARS = OR.land('break_pillars'); OR_SERVE = OR.land('serve_before'); OR_NOBOW = OR.land('no_bow')
JO_HIGH = JO.the_command({'ask': 'high_places'}, JO.DATA); JO_THREE = JO.the_command({'ask': 'three_objects_own'}, JO.DATA); JO_POSSESS = JO.the_command({'ask': 'possess_and_dwell'}, JO.DATA); JO_ERAS = JO.the_command({'ask': 'private_altar_eras'}, JO.DATA); JO_MOLTEN = JO.the_command({'ask': 'molten_images'}, JO.DATA)
PS_BAN = PS.noahide('blood_ban_by_call'); PS_SCOPE = PS.noahide('blood_scope_by_call'); PS_SHED = PS.noahide('shed_homograph')
CA_ASC = CA.matzah({'ask': 'as_commanded'}, CA.DATA); CA_KID = CA.kid_in_milk({'ask': 'eat'}, CA.DATA)
SD_TABLE = SD.eras('table'); SD_SWITCH = SD.eras('switch'); SD_MATRIX = SD.eras('karet_matrix'); SD_DIFF = SD.eras('differences'); SD_INK = SD.eras('ink_of_the_ban')
TC_COV = TC.covenant(True, True, True); TC_GATE = TC.cascade(0)
CH_FOURTH = CH.the_first_tablet({'ask': 'the_fourth_word'}, CH.DATA); CH_SERV = CH.the_first_tablet({'ask': 'the_servants_rest'}, CH.DATA); CH_OX = CH.the_first_tablet({'ask': 'the_ox_and_the_ass'}, CH.DATA)
HI_RIGHT = HI.the_test_and_the_right({'ask': 'the_right_and_the_good'}, HI.DATA)
OH_PERISH = OH.the_exile_case({'ask': 'perish_and_scatter'}, OH.DATA)
GL_OGSB = GL.the_testimony({'ask': 'other_gods_serve_bow'}, GL.DATA); GL_HEARK = GL.the_testimony({'ask': 'hearken_plural'}, GL.DATA)
BC_KEEP = BC.the_blessing_and_the_curse({'ask': 'keep_to_do'}, BC.DATA); BC_POSSESS = BC.the_blessing_and_the_curse({'ask': 'possess_and_dwell'}, BC.DATA)
BH_ARK = BH.march({'ask': 'ark_bearers'}, BH.DATA); BH_SANCT = BH.march({'ask': 'sanctuary_name'}, BH.DATA); BH_SHEK = BH.march({'ask': 'shekhinah_minimum'}, BH.DATA)
BR_BOUND = BR.the_land_and_its_fall({'ask': 'the_land_bound_rule'}, BR.DATA)
def FOUND(r):
    """a kin cell CALLED and answering — a tuple (verdict, effects, trail) whose verdict is in span, or a dict with its value"""
    if isinstance(r, dict): return 'v' in r
    return isinstance(r, tuple) and isinstance(r[0], str) and not r[0].startswith('no verdict')
# the values asserted from the callees' print (ch12_callees.out — read before any assert was typed)
assert SA_BAN['v'] == 'karet' and SA_WHICH['v'] == ['sages_lifeblood_only', 'R._Yehuda_any_blood'] and SA_HUNTED['v'] == 'bought_inherited_gifted_self_trapped_all_covered' and SA_CONSEC['v'] == 'no_covering' and SA_IND['v'] == 'individual_not_community_not_coerced_erring_misled' and SA_COMMON['v'] == 'exempt' and SA_BIRD['v'] == 'not_liable', (SA_BAN['v'], SA_WHICH['v'], SA_HUNTED['v'], SA_CONSEC['v'], SA_IND['v'], SA_COMMON['v'], SA_BIRD['v'])
assert SA_SEED['v'] == ['son', 'daughter', 'grandson', 'granddaughter', 'unfit_seed'] and SA_FAMILY['v'] == 'afflictions_not_karet' and SA_PRED['v'] == 'liable' and SA_LAND['v'] == 'the_land_vomits_its_inhabitants' and SA_SERVICE['v'] == ['firstborn_before', 'priests_after'], (SA_SEED['v'], SA_FAMILY['v'], SA_PRED['v'], SA_LAND['v'], SA_SERVICE['v'])
assert len(SA_ERAS['v']) == 6 and SA_ERAS['v'][:3] == [('before_the_Tabernacle', 'permitted'), ('the_Tabernacle', 'forbidden'), ('Gilgal', 'permitted')] and SD_TABLE['v'] == ['permitted', 'banned', 'permitted', 'banned', 'permitted', 'banned'] and SD_DIFF['v'] == 11 and SD_INK['v'] == 'Lev 17:4 and Deut 12:8' and SD_SWITCH['v'] == 'high_places_banned_service_by_priests', (SA_ERAS['v'], SD_TABLE['v'], SD_DIFF['v'], SD_INK['v'], SD_SWITCH['v'])
assert ER_GROWS['v'] == [3, 4, 5] and ER_FIRST['v'] == 'demolish_demolish_break_break' and ER_ASH['v'] == 4 and ER_ASC['v'] == (1, 1, False) and OR_PILLARS['v'] == 'demolish_demolish_break_break' and OR_SERVE['v'] == 'serve_before_the_LORD' and OR_EVERY['v'] == 'hapax_the_name_mentioned' and OR_OLAH['v'] == 'wholly_to_fires' and OR_SHEL['v'] == 'two_days_one_night', (ER_GROWS['v'], ER_FIRST['v'], ER_ASH['v'], ER_ASC['v'], OR_PILLARS['v'], OR_SERVE['v'], OR_EVERY['v'], OR_OLAH['v'], OR_SHEL['v'])
assert PS_BAN['v'] == ('karet', ['sages_lifeblood_only', 'R._Yehuda_any_blood'], 'convert_bound_as_the_citizen') and PS_SHED['v'] == ['Lev 4:7', 'Lev 4:18', 'Lev 4:25', 'Lev 4:30', 'Lev 4:34'] and TC_COV['v'] == 'blessing' and TC_GATE['stage']['v'] == 1, (PS_BAN['v'], PS_SHED['v'], TC_COV['v'], TC_GATE['stage']['v'])
assert all(FOUND(r) for r in (SA_AGENCY, SA_CROSS, SA_ATONES, SA_LASHES, SA_KARET_OWN, SA_EATER, SA_FOOT, SA_STRAY, SA_DIFF, SA_CLASSES, SA_NOKARET, KR_BIK, KR_BLEM, KR_BREAST, KR_EVERY, KR_EXCL, KR_CONF, SN_SHADE, SN_WOOD, SN_BAN, SN_NOCOV, SN_BURN, SN_SNARED, SN_ABOM, SN_HOUSE, SN_COVET, ER_CUT4, OR_EARTH, OR_SWORD, OR_NOBOW, JO_HIGH, JO_THREE, JO_POSSESS, JO_ERAS, JO_MOLTEN, PS_SCOPE, CA_ASC, CA_KID, SD_MATRIX, CH_FOURTH, CH_SERV, CH_OX, HI_RIGHT, OH_PERISH, GL_OGSB, GL_HEARK, BC_KEEP, BC_POSSESS, BH_ARK, BH_SANCT, BH_SHEK, BR_BOUND)), 'a kin cell answered out of span'
assert CA_ASC[0].startswith('seven days of unleavened bread') and CA_ASC[1] == ['purge_deadline'] and CA_KID[0] == 'barred' and KR_EVERY[0].startswith('in every place') and JO_ERAS[1] == ['exempt'] and 'Zevachim 14:4-8' in JO_ERAS[0] and JO_HIGH[1] == ['commanded'] and CH_FOURTH[1] == ['accepted'] and HI_RIGHT[0].startswith('the right and the good (6:18)') and SN_HOUSE[1] == ['accepted'] and BH_ARK[0] == 'four bearers (two plurals)' and BR_BOUND[0].startswith("the borders' legal reach") and SN_WOOD[1] == ['lashes'] and BC_KEEP[0].startswith('keep to do (11:32)') and OH_PERISH[0].startswith('perish and scatter (4:26-27)'), (CA_ASC[:2], CA_KID[0], KR_EVERY[0][:30], JO_ERAS[:2], JO_HIGH[1], CH_FOURTH[1], HI_RIGHT[0][:40], SN_HOUSE[1], BH_ARK[0], BR_BOUND[0][:30], SN_WOOD[1], BC_KEEP[0][:30], OH_PERISH[0][:30])
'''
src = HEAD + helpers + TAIL_A + ink_block + TAIL_B
open(f'{SP}/ch12_part1.py', 'w', encoding='utf-8').write(src)
import py_compile; py_compile.compile(f'{SP}/ch12_part1.py', doraise=True)
print('part1 derived: %d bytes; helpers %d, ink block %d (asserts %d); dropped %d store-bound lines' % (len(src), len(helpers), len(ink_block), n_as, len(drop)))

import os as _os
_ROOT = _os.path.normpath(_os.path.join(_os.path.dirname(_os.path.abspath(__file__)), '..', '..', '..'))   # THE PORTABLE REPO (2026-09-15): the repo root from this file's own place
#!/usr/bin/env python3
# THE DEUTERONOMY WALK 15b: cold_run_courts_prophet.py PART 1 derived — the head typed here; the generic helper block COPIED from the chapter-16 runner by content
# markers (HERE = … through def LEN — the parser exec, the DB, the phrase/lemma/diff helpers; W16 made W17, W18 and W); THE INK BLOCKS COPIED from the reading's own
# instrument ch17_ink.py by content markers — THREE blocks (the kin by computation over the two chapters; the formulas over the Torah and the Bible; the kin re-scored
# and the twins diffed), the store-, shelf- and Onkelos-bound lines DROPPED by name (10b's lesson 6 — the count read from the print); the counter's day, the one-database
# scans, and THE CALLEES' FACTS (typed in ch17_callees_facts.py from ch17_callees.out — read before any assert was typed). Asserted substitutions throughout.
# derive_ch16_part1.py's form over two chapters. RUN FROM THE REPO ROOT.
import subprocess, re, os, sys
ROOT = _ROOT
SP = os.path.dirname(os.path.abspath(__file__))
FJ = open(f'{ROOT}/World/step9/cold_run_festivals_judges.py', encoding='utf-8').read()
INKB = open(f'{SP}/ch17_ink.py', encoding='utf-8').read()
FACTS = open(f'{SP}/ch17_callees_facts.py', encoding='utf-8').read()
assert FACTS.startswith('\n# ---- THE CALLEES\' FACTS'), 'the callees\' facts typed from the print (ch17_callees_facts.py)'
HEAD = '''#!/usr/bin/env python3
# DEUTERONOMY 17:1-18:22 — THE BLEMISHED SACRIFICE (the south and the blemish, the three true prohibitions, born blemished and any evil thing, outside its time and
# place, the mounter and the harlot's hire, the sacrifice not the sacrificer), THE IDOLATER'S TRIAL (found means witnesses, the gate and the stoning, the three acts and
# the associator, the seven investigations, the three exclusions, two witnesses for every death, one witness and the disciple silent, the witnesses' hand first), THE
# HIGH COURT AT THE PLACE (the distinguished judge and the three grades, the pairs, rise at once in court, the three courts, Yavneh and the priests, the judge of those
# days, do and turn not right or left, the rebel elder), THE KING (the disgrace and the commandment, set you shall set, chosen by a prophet, from among your brothers and
# Agrippas, the awe of the king, the three limits for himself, the copy of the law, the circle of learning and the heart), THE PRIESTS' DUES (no portion no inheritance,
# the fire offerings and the boundary's holy things, the due exacted by judges, the claim at the slaughter and the proselyte's cow, in and outside the land, the three
# gifts named, the first fruits and the fleece, chosen to stand), THE LEVITE AT THE PLACE (the Levite who is a priest, all the desire of his soul, on the floor, portion as
# portion, the fathers' barter), THE DIVINERS (learn to understand not to do, the court warned and fire with Molech, the diviner and the augur, the Aramean woman, the
# soothsayer three ways, the sorcerer's deed, the charmer the ghost the spirit the dead, one of them and whole) and THE PROPHET (from your midst of your brothers, hear
# him even for the hour, Horeb's request the cause, My words in his mouth, the six deaths, the false prophet's kin, the test by the event, no fear in prosecuting); THE
# READBACK'S FORMS ON FILE, NO NEW FORM (THE DEUTERONOMY WALK sitting 15b — THE LEAN PASS, 2026-09-24; World/step9/DEUTERONOMY_WALK.md "Sitting 15b"; the state doc's
# #211). ONE RUNNER OVER TWO CHAPTERS AND TWO UNITS (the span two ranges); EIGHT own-day lines at the counter's day (40, 11, 1), NO marker: blemished_sacrifice_barred
# (17:1), idolater_trial_declared (17:2-7), high_court_declared (17:8-13), king_law_declared (17:14-20), priests_dues_declared (18:1-5), levite_at_the_place_declared
# (18:6-8), diviners_barred (18:9-14), prophet_law_declared (18:15-22) — THIRTY-SEVEN writes on Israel (fifteen STATUSES, twenty BLOCKS, two HEAVEN entries), every one
# its first entry. THE KIN'S CELLS BY CALL (twenty runners, every edge REFERENCE); THE TAPE'S LINES BY KIND (Horeb's request, the false prophet, the inciter's hear-and-
# fear, the Levites' portion, the kings promised, the courts). Eight cells and the table; every token probed (zero-report law); effects on every cell (the effects law);
# THE EXAM THE EIGHT MISHNAH ROWS THE SPINE CITES (Sanhedrin 11:2, Sotah 7:8, Sanhedrin 2:4, Chullin 10:4, Chullin 11:2, Zevachim 2:1, Sukkah 5:7, Sanhedrin 7:7 — read
# whole; no docket, the lean form); the parameters the runner's DATA rows (no clock datum). The daemon law_courts_prophet given_at Deut 17:1, installed_by boot (the
# Deuteronomy daemons' form). Reading ledger: logic/oral_triage/deu_17_18_shoftim_2026-09-24.md; the lean exam: deu_17_18_shoftim_exam_2026-09-24.md.

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
import cold_run_seducers as SE                 # THE EDGE: courts_prophet -> seducers CALL, reference (13's seven investigations, the witnesses' hand, the sword, the purge formula's nine seats; the prophet with the sign against the prophet with the word)
import cold_run_festivals_judges as FJ         # THE EDGE: courts_prophet -> festivals_judges CALL, reference (16:18's courts and the three tiers — the courts' first daemon)
import cold_run_opening_speech as OP           # THE EDGE: courts_prophet -> opening_speech CALL, reference (1:17's hard matter brought to Moses; the court of three; the judgment is God's)
import cold_run_exodus_story as ES             # THE EDGE: courts_prophet -> exodus_story CALL, reference (Exodus 18:21-25's courts — the sizes (71, 23), 78,600 judges)
import cold_run_ordinances as OR               # THE EDGE: courts_prophet -> ordinances CALL, reference (Exodus 23:2's one-and-two, the twenty-three; 22:17's sorceress — the punishment, this the warning)
import cold_run_sanctions as SA                # THE EDGE: courts_prophet -> sanctions CALL, reference (Leviticus 20:2-5's Molech by the shared word; 20:27's ghost and spirit stoned)
import cold_run_holiness_b as HB               # THE EDGE: courts_prophet -> holiness_b CALL, reference (Leviticus 19:31's warning — the consulter warned, the bearer stoned)
import cold_run_priesthood as PR               # THE EDGE: courts_prophet -> priesthood CALL, reference (Leviticus 22:20-25's blemish class — the sweep, the passing blemish)
import cold_run_release_firstborn as RF        # THE EDGE: courts_prophet -> release_firstborn CALL, reference (15:21's lame and blind — the particulars teach the class)
import cold_run_korach as KO                   # THE EDGE: courts_prophet -> korach CALL, reference (Numbers 18's twenty-four gifts, the no-inheritance, the watches' places and lots)
import cold_run_second_tablets as ST           # THE EDGE: courts_prophet -> second_tablets CALL, reference (10:8-9's stand-and-minister and no-portion — 18:2's receipt behind)
import cold_run_place_name as PN               # THE EDGE: courts_prophet -> place_name CALL, reference (the place formula at 17:8, 17:10, 18:6; 12:12's Levite; 12:17's gates; 12:30-31's inquiry and the fire)
import cold_run_seven_nations as SN            # THE EDGE: courts_prophet -> seven_nations CALL, reference (7:25-26's abomination to the LORD)
import cold_run_covenant_at_horeb as CH        # THE EDGE: courts_prophet -> covenant_at_horeb CALL, reference (5:24-28's request retold at 18:16-17; 5:9's bow-and-serve at 17:3)
import cold_run_obey_horeb as OH               # THE EDGE: courts_prophet -> obey_horeb CALL, reference (4:10's day of the assembly; 4:19's host apportioned; 4:2's sealing)
import cold_run_refuge as RG                   # THE EDGE: courts_prophet -> refuge CALL, reference (Numbers 35:30's witnesses — two by the prototype, the one witness)
import cold_run_mekoshesh as MK                # THE EDGE: courts_prophet -> mekoshesh CALL, reference (Numbers 15:35-36's stoning rite — the stones and the stone)
import cold_run_good_land as GL                # THE EDGE: courts_prophet -> good_land CALL, reference (8:13-14's silver and gold multiplied and the heart lifted — the king's twins)
import cold_run_balak as BK                    # THE EDGE: courts_prophet -> balak CALL, reference (Numbers 23:23's no divination; 23:5's word in the mouth — 18:18's kin)
import cold_run_pre_sinai as PS_               # THE EDGE: courts_prophet -> pre_sinai CALL, reference (Genesis 17:1's walk whole — 18:13's twin; the kings promised)

'''
# ---- the generic helper block from the chapter-16 runner, by content markers ----
a = FJ.index('HERE = _os.path.dirname(_os.path.abspath(__file__))'); b = FJ.index('def LEN(b, c, v): return len(words(b, c, v))'); b = FJ.index('\n', b) + 1
helpers = FJ[a:b]
assert helpers.count("def W16(v): return words('Deut', 16, v)") == 1
helpers = helpers.replace("def W16(v): return words('Deut', 16, v)", "def W17(v): return words('Deut', 17, v)\ndef W18(v): return words('Deut', 18, v)\ndef W(c, v): return words('Deut', c, v)")
assert 'W16' not in helpers and '16' not in re.sub(r'2026-09-1[56]|0x0591|0x05C7|0x05AF|0x05B0|0x05BD', '', helpers), [l for l in helpers.split('\n') if '16' in l][:3]
TAIL_A = '''def verse_text(ch, vs, book='Deut'): return ' '.join(words(book, ch, vs))
DV = lambda c, v: ('Deut', c, v)
NEG_T = ('לא', 'ולא')   # (not; and not)
NAME = ('יהוה', 'ליהוה', 'ויהוה', 'ביהוה', 'מיהוה')   # (the LORD; to the LORD; and the LORD; in the LORD; from the LORD)
import difflib
def SH(a, b_): return sum(s for _, _, s in difflib.SequenceMatcher(a=words(*a), b=words(*b_)).get_matching_blocks())   # the reading's shared-run measure
CHS = (17, 18)
NV = {c: len({v for (b, cc, v) in by if b == 'Deut' and cc == c}) for c in CHS}; assert NV == {17: 20, 18: 22}, NV   # twenty and twenty-two verses in both numberings (the identity — the reading's divisions assert)
TOKN = {c: sum(len(W(c, v)) for v in range(1, NV[c] + 1)) for c in CHS}; assert TOKN == {17: 368, 18: 304}, TOKN   # the two chapters' tokens (the reading's store assert — the store the DB at every verse)
SPAN = [(17, v) for v in range(1, 21)] + [(18, v) for v in range(1, 23)]

P_ = []   # the provenance trail of the case being run
def ink(ref, note):  P_.append(('INK',  'Deut %s — %s' % (ref, note) if not ref[:1].isupper() else '%s — %s' % (ref, note)))
def move(src, note): P_.append(('MOVE', '%s — %s' % (src, note)))
def dat(note):       P_.append(('DATA', note))
def hyp(note):       P_.append(('HYP',  note))     # THE LINK REVIEW LAW: a hypothesis — no teacher; counted apart, never as compiled
def out(verdict, effects):
    """verdict + registry-validated effects (the engine contract)"""
    FX.validate([e for e in effects if e != FX.NONE])
    return verdict, effects, list(P_)

# ---- THE INK, computed (the parser and the tokens; the reading's facts the expectations — every assert PROVEN at the reading, ch17_ink.py — COPIED from the reading's instrument by content markers in three blocks; the store-, shelf- and Onkelos-bound asserts left to the reading; the parser's facts typed from the ink's own asserts) ----
def MARKS(c, v): return [t for t in verse_words('Deut', c, v) if t[-1] in '#~^%@|*']
PARSE = {(c, v): (ink_numbers(verse_words('Deut', c, v)), ink_ordinals(verse_words('Deut', c, v)), MARKS(c, v)) for (c, v) in SPAN}
NUMV = [k for k in PARSE if PARSE[k][0]]; ORDV = [k for k in PARSE if PARSE[k][1]]; STARV = [k for k in PARSE if PARSE[k][2]]
print('THE INK (printed before it is asserted): PARSE %s, NUMV %s, ORDV %s, STARV %s, TOKN %s' % ({k: p for k, p in PARSE.items() if p[0] or p[1] or p[2]}, NUMV, ORDV, STARV, TOKN))
assert {k: p for k, p in PARSE.items() if p[0] or p[1] or p[2]} == {(17, 2): ([1], [], []), (17, 6): ([2, 3, 1], [], [])}, {k: p for k, p in PARSE.items() if p[0] or p[1] or p[2]}   # TWO NUMBER VERSES (17:2 one of your gates, 17:6 two witnesses or three, one witness), no ordinal, no starred token; 18:6's "from one of your gates" NOT read (the number word behind its prefix) — the reading's parser assert
assert NUMV == [(17, 2), (17, 6)] and ORDV == [] and STARV == []
NEG = {(c, v): [x for x in W(c, v) if x in NEG_T] for (c, v) in SPAN if any(x in NEG_T for x in W(c, v))}
NAME_BARE = sum(1 for (c, v) in SPAN for x in W(c, v) if x == 'יהוה')
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
# ---- THE COUNTER'S DAY AND THE ONE DATABASE SCANNED (a bare world on the exodus epoch; no clock walk these chapters — no marker, no stretch, no clock datum: the king's and the prophet's futures on the Prophets' tape) ----
with contextlib.redirect_stdout(io.StringIO()):
    _WC = WE.World(era='the counter\\'s day — chapters 17-18 on a bare world (the exodus epoch)', epoch='exodus')
_EX = _WC.clock.eras['exodus']
def DAY(y, m, d): return _WC.clock.day_in('exodus', y, m, d)
def DATE(day): return _EX.date(day)
COUNTER = DAY(40, 11, 1)
CLOCK = {'counter': DATE(COUNTER), 'no_marker': True, 'no_clock_datum': True}
print('THE CLOCK (printed before it is asserted):', CLOCK)
assert CLOCK['counter'] == (40, 11, 1), CLOCK

# ---- THE ONE DATABASE SCANNED (the holes' ground — nothing names the thirty-seven on Israel before this sitting; the references' entities as the recon read them) ----
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
OWN37 = ('blemished_offering_barred', 'idolater_inquiry_required', 'two_witnesses_required', 'one_witness_barred', 'witnesses_hand_first_commanded', 'high_court_at_the_place_commanded', 'sentence_binding_commanded', 'turning_from_the_word_barred', 'king_from_the_brothers_commanded', 'foreign_king_barred', 'horses_multiplying_barred', 'return_to_egypt_barred', 'wives_multiplying_barred', 'silver_and_gold_multiplying_barred', 'law_copy_commanded', 'heart_lifting_barred', 'shoulder_cheeks_maw_owed', 'first_fleece_owed', 'priests_standing_chosen', 'levite_service_at_the_place_permitted', 'equal_portions_commanded', 'abominations_learning_barred', 'passing_through_fire_barred', 'diviner_barred', 'soothsayer_barred', 'augur_barred', 'sorcerer_barred', 'charmer_barred', 'ghost_consulting_barred', 'familiar_spirit_barred', 'necromancer_barred', 'wholeness_commanded', 'prophet_like_moses_promised', 'prophet_hearkening_commanded', 'word_required_of_the_hearer', 'false_word_test_declared', 'false_prophet_fear_barred')
HOLE_WORDS = r"^(blemished_offering\\w*|idolater_inquiry\\w*|two_witnesses\\w*|one_witness\\w*|witnesses_hand\\w*|high_court\\w*|sentence_binding\\w*|turning_from\\w*|king_from\\w*|foreign_king\\w*|horses_multiply\\w*|return_to_egypt\\w*|wives_multiply\\w*|silver_and_gold_multiply\\w*|law_copy\\w*|heart_lifting\\w*|shoulder_cheeks\\w*|first_fleece\\w*|priests_standing\\w*|levite_service\\w*|equal_portions\\w*|abominations_learning\\w*|passing_through_fire\\w*|diviner_barred|soothsayer\\w*|augur_barred|sorcerer_barred|charmer_barred|ghost_consulting\\w*|familiar_spirit\\w*|necromancer\\w*|wholeness_commanded|prophet_hearkening\\w*|prophet_like_moses\\w*|word_required\\w*|false_word_test\\w*|false_prophet_fear\\w*)\\b"
_hs = ledger_scan('israel_people', HOLE_WORDS); HOLE_SCAN = None if _hs is None else [e for e in _hs if e not in OWN37]   # this sitting's own names excluded once the fold carries them
HEARS_SCAN = effect_scan('israel_hears_and_fears'); FALSEP_SCAN = effect_scan('false_prophet_hearing_barred'); INHERIT_SCAN = effect_scan('inheritance_barred'); KINGS_SCAN = effect_scan('kings_promised'); PROPHET_SCAN = effect_scan('prophet_declared'); WHOLE_SCAN = effect_scan('wholeness_owed')
COURTS_SCAN = effect_scan('courts_established'); JUDGES_SCAN = effect_scan('judges_charged'); BRIBE_SCAN = effect_scan('bribe_barred'); STONED_SCAN = effect_scan('stoned'); PUT_SCAN = effect_scan('put_to_death'); PURGED_SCAN = effect_scan('evil_purged_from_the_midst'); DUES_SCAN = effect_scan('priestly_dues_granted')
del _hs   # 9b's lesson: the raw scans are the database's state at import — the derived lists are equal on the cached and the full load
_FXV = yaml.safe_load(open(_os.path.join(HERE, 'effect_vocabulary.yaml'), encoding='utf-8'))['effects']
print('THE SCANS (printed before they are asserted): holes %s; hears %s; false prophet %s; inheritance %s; kings %s; prophet %s; wholeness %s; courts %s; judges %s; bribe %s; stoned %s; put to death %s; purged %s; dues %s' % (HOLE_SCAN, HEARS_SCAN, FALSEP_SCAN, INHERIT_SCAN, KINGS_SCAN, PROPHET_SCAN, WHOLE_SCAN, COURTS_SCAN, JUDGES_SCAN, BRIBE_SCAN, STONED_SCAN, PUT_SCAN, PURGED_SCAN, DUES_SCAN))
assert HOLE_SCAN in ([], None), HOLE_SCAN   # THE HOLES' GROUND — nothing on Israel named the thirty-seven before this sitting (DI4)
assert HEARS_SCAN in (['israel_people'], None) and FALSEP_SCAN in (['israel_people'], None) and INHERIT_SCAN in (['aaron', 'the_levites'], None) and KINGS_SCAN in (['jacob'], None) and PROPHET_SCAN in (['abraham'], None) and WHOLE_SCAN in (['abraham'], None) and COURTS_SCAN in (['israel_people'], None) and (JUDGES_SCAN is None or JUDGES_SCAN in (['the_court'], ['the-court'])) and BRIBE_SCAN in (['israel_people'], None) and STONED_SCAN in (['the_blasphemer', 'the_wood_gatherer'], None) and (PUT_SCAN is None or len(PUT_SCAN) == 7) and PURGED_SCAN in ([], None) and DUES_SCAN in (['aaron'], None), (HEARS_SCAN, FALSEP_SCAN, INHERIT_SCAN, KINGS_SCAN, PROPHET_SCAN, WHOLE_SCAN, COURTS_SCAN, JUDGES_SCAN, BRIBE_SCAN, STONED_SCAN, PUT_SCAN, PURGED_SCAN, DUES_SCAN)   # the references' entities as the recon read them from the snapshot (DI4 — no second write)
assert all(k in _FXV for k in OWN37) and sum(1 for k in OWN37 if _FXV[k]['ledger_op'] == 'block') == 20 and sum(1 for k in OWN37 if _FXV[k]['ledger_op'] == 'status') == 15 and sum(1 for k in OWN37 if _FXV[k]['ledger_op'] == 'heaven') == 2, 'the thirty-seven on the registry (add_types_ch17_a.py)'
# THE TWINS DIFFED on the DB (the reading's kin asserts read again here — DI4; the shared run SH)
TWIN = {'17:1 vs 15:21': SH(DV(17, 1), DV(15, 21)), '17:4 vs 13:15': SH(DV(17, 4), DV(13, 15)), '17:6 vs 19:15': SH(DV(17, 6), DV(19, 15)), '17:7 vs 13:10': SH(DV(17, 7), DV(13, 10)), '17:8 vs 1:17': SH(DV(17, 8), DV(1, 17)), '17:11 vs 17:20': SH(DV(17, 11), DV(17, 20)), '17:13 vs 13:12': SH(DV(17, 13), DV(13, 12)), '17:17 vs 8:13': SH(DV(17, 17), DV(8, 13)), '17:20 vs 8:14': SH(DV(17, 20), DV(8, 14)), '18:2 vs 10:9': SH(DV(18, 2), DV(10, 9)), '18:2 vs Num 18:20': SH(DV(18, 2), ('Num', 18, 20)), '18:5 vs 10:8': SH(DV(18, 5), DV(10, 8)), '18:10 vs Lev 20:2': SH(DV(18, 10), ('Lev', 20, 2)), '18:11 vs Lev 20:27': SH(DV(18, 11), ('Lev', 20, 27)), '18:13 vs Gen 17:1': SH(DV(18, 13), ('Gen', 17, 1)), '18:16 vs 5:25': SH(DV(18, 16), DV(5, 25)), '18:17 vs 5:28': SH(DV(18, 17), DV(5, 28)), '18:19 vs 13:4': SH(DV(18, 19), DV(13, 4)), '18:22 vs 13:2': SH(DV(18, 22), DV(13, 2))}
print('THE TWINS DIFFED (printed before they are asserted):', TWIN)
TWIN_EXPECTED = _TWIN_EXPECTED_
if TWIN_EXPECTED: assert TWIN == TWIN_EXPECTED, TWIN   # typed from the first derive's print (the callees' way — printed before typed)
'''
TWIN_EXPECTED = os.environ.get('TWIN_EXPECTED', 'None')
src = HEAD + helpers + TAIL_A + ink_block + TAIL_B.replace('_TWIN_EXPECTED_', TWIN_EXPECTED) + FACTS
open(f'{SP}/ch17_part1.py', 'w', encoding='utf-8').write(src)
import py_compile; py_compile.compile(f'{SP}/ch17_part1.py', doraise=True)
print('part1 derived: %d bytes; helpers %d, ink block %d (asserts %d); dropped %d store-bound lines; the callees\' facts %d bytes; TWIN_EXPECTED %s' % (len(src), len(helpers), len(ink_block), n_as, len(drop), len(FACTS), TWIN_EXPECTED[:40]))

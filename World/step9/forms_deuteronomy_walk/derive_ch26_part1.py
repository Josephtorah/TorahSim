#!/usr/bin/env python3
# THE DEUTERONOMY WALK 18b: cold_run_firstfruits_ebal_curses.py PART 1 derived — the head typed here; the generic helper block COPIED from the chapter 22-25 runner by content
# markers (HERE = … through def LEN — the parser exec, the DB, the phrase/lemma/diff helpers; W22-W25 made W26, W27, W28 and W); THE INK BLOCKS COPIED from the reading's own
# instrument ch26_ink.py by content markers — FOUR blocks (the kin found by computation; the formulas over the Torah and the Bible; the kin re-scored; the twins
# diffed), the store-, shelf-, Onkelos- and register-bound lines DROPPED by name (10b's lesson 6 — the count read from the print); the counter's day, the one-database scans, and
# THE CALLEES' FACTS (typed in ch26_callees_facts.py from ch26_callees_short.out, ch26_callees_short2.out and ch26b_callees2.out — read before any assert was typed).
# Asserted substitutions throughout. derive_ch22_part1.py's form over three chapters. RUN FROM THE REPO ROOT with PYTHONPATH the scratchpad.
import subprocess, re, os, sys
ROOT = _ROOT
SP = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, SP)
import ch26b_spec as S
PPC = open(f'{ROOT}/World/step9/cold_run_persons_poor_court.py', encoding='utf-8').read()
INKB = open(f'{SP}/ch26_ink.py', encoding='utf-8').read()
FACTS = open(f'{SP}/ch26_callees_facts.py', encoding='utf-8').read()
assert FACTS.startswith('\n# ---- THE CALLEES\' FACTS'), 'the callees\' facts typed from the prints (ch26_callees_facts.py)'
HEAD = '''#!/usr/bin/env python3
# DEUTERONOMY 26:1-28:69 — THE FIRST FRUITS (when you come into the land and dwell in it, the first of all the fruit in a basket to the place, I declare this day, the priest
# sets it before the altar, a wandering Aramean was my father, set it down and bow and rejoice with the Levite and the stranger), THE REMOVAL AND THE CONFESSION (when you have
# finished tithing in the third year, given to the Levite, the stranger, the orphan and the widow, I have removed the holy from the house, not in mourning, not in uncleanness,
# not for the dead, look down and bless), THE COVENANT FORMULA (this day the LORD commands you, the LORD you have declared, the LORD has declared you His treasured people, high
# above all nations a holy people), THE STONES AND THE ALTAR (Moses and the elders, great stones plastered on the day you cross, all the words of this law written, an altar of
# whole stones on Ebal with no iron, burnt and peace offerings, eat and rejoice, very plainly), THE PEOPLE THIS DAY (Moses and the priests the Levites: be silent and hear, this
# day you have become a people, hearken and do), THE SIX AND THE SIX (Moses commanded the people that day: these stand to bless on Gerizim, these for the curse on Ebal), THE
# TWELVE CURSES (the Levites answer with a loud voice, cursed the man twelve times, all the people say Amen), THE BLESSINGS (if you diligently hearken, blessed in the city and
# the field, the womb, the ground and the beast, the basket and the trough, coming in and going out, the enemies flee seven ways, the storehouses, a holy people and the
# peoples' fear, the heavens' good treasure, lend and not borrow, the head and not the tail, turn not aside), THE CURSES OF THE HOUSE AND THE FIELD (if you will not hearken,
# the four twins cursed, the curse, the confusion and the rebuke, the pestilence, the seven diseases, the brass heavens and the iron earth, the rain to dust, smitten before the
# enemies, the carcass, the boil of Egypt, the madness, a wife, a house, a vineyard another takes, the ox, the ass and the flock, the sons and daughters, the fruit eaten, sore
# boils, carried with the king to serve wood and stone, a byword, the seed, the vines and the olives lost, captivity, the stranger the head) and THE CURSES OF THE SIEGE AND THE
# EXILE (all these curses pursue you, because you served not with joy, an iron yoke, a nation from afar as the eagle flies, the siege in all the gates, the sons' flesh eaten,
# if you keep not all the words of this law, the plagues made wonderful, the diseases of Egypt returned, left few in number, as He rejoiced so He rejoices to destroy, scattered
# among all peoples to serve wood and stone, no rest and a trembling heart, the life hanging in doubt, back to Egypt in ships, sold and none buys, these are the words of the
# covenant in the land of Moab besides Horeb); THE READBACK'S FORMS ON FILE, NO NEW FORM (THE DEUTERONOMY WALK sitting 18b — THE LEAN PASS, 2026-09-26; World/step9/DEUTERONOMY_WALK.md
# "Sitting 18b"; the state doc's #225). ONE RUNNER OVER THREE CHAPTERS AND FIVE UNITS (the span three ranges); TWENTY-ONE own-day lines at the counter's day (40, 11, 1), NO
# marker (chapter 27's three narrative frames the lines' speaker): first_fruits_declared (26:1-11), tithe_confession_declared (26:12-15), covenant_formula_declared (26:16-19),
# stones_altar_declared (27:1-8), people_this_day_declared (27:9-10), gerizim_ebal_tribes_declared (27:11-13), twelve_curses_declared (27:14-26), blessings_condition_declared
# (28:1-6), enemies_storehouses_blessing_declared (28:7-8), holy_people_fear_declared (28:9-10), heavens_treasure_lending_declared (28:11-14), curses_condition_declared (28:15-19),
# curse_diseases_brass_declared (28:20-24), defeat_carcass_boil_madness_declared (28:25-29), wife_house_vineyard_king_taken_declared (28:30-37), harvests_failed_stranger_head_declared
# (28:38-44), curses_pursue_iron_yoke_declared (28:45-48), eagle_nation_siege_declared (28:49-52), sons_flesh_siege_declared (28:53-57), plagues_scattered_declared (28:58-64),
# trembling_ships_covenant_declared (28:65-69) — NINETY-SIX writes on Israel (ninety-one NEW: thirty-three STATUSES, five BLOCKS, fifty-three HEAVEN entries; FIVE REUSES: the
# rejoicing at 26:11 and 27:7, the poor tithe at 26:12, the blessings for hearing at 28:1, the rain at 28:12). THE KIN'S CELLS BY CALL (thirty-four runners, every edge REFERENCE —
# the kin read these chapters forward: the removal's date, the receipt's referent 28:3, Gerizim and Ebal's form, wood and stone, the blessing's list; the Sifrei's own analogies run
# FROM these chapters to the kin); THE TAPE'S LINES BY KIND (the offer at Sinai, the blessings for hearing, the second paragraph and the pair set, the release, the tithes, the
# place, the judges, the landmark, the war's speech, the father's wife, the stranger's justice, the king, the copy of the law, the testimony, the witnesses, the inciter, the
# hanged man, the bondage, the cry, the plagues, the going out, the covenant's blood, the seventy, the stars, the fathers' altars). Ten cells and the table; every token probed
# (zero-report law); effects on every cell (the effects law); THE EXAM THE TWENTY-SIX MISHNAH ROWS THE LEDGER CITES (Bikkurim 1:1-6, 1:8, 1:10, 2:4, 3:1, 3:4, 3:7, 3:8; Maaser
# Sheni 5:6, 5:10-14; Peah 1:1, 4:11, 8:5; Sotah 7:1, 7:2, 7:5; Terumot 11:3 — read whole; no docket, the lean form); the parameters the runner's DATA rows and TWO clock data on
# the calendar's keys (the first fruits' window, the confession's hour). The daemon law_firstfruits_ebal_curses given_at Deut 26:1, installed_by boot (the Deuteronomy daemons'
# form). Reading ledger: logic/oral_triage/deu_26_28_ki_tavo_2026-09-26.md; the lean exam: deu_26_28_ki_tavo_exam_2026-09-26.md.

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
import cold_run_food_tithe as FT                # THE EDGE: firstfruits_ebal_curses -> food_tithe CALL, reference (14:22-29's third year — the removal's date on file, the measures, the four in want; the cell READ 26:12 FORWARD; 26:11's rejoicing by I2 with 27:7; 26:14's dead; 28:43's sojourner)
import cold_run_release_firstborn as RF         # THE EDGE: firstfruits_ebal_curses -> release_firstborn CALL, reference (15:5's hearkening REUSED at 28:1; 15:6's lending and THE RECEIPT'S REFERENT 28:3 — the pointer PAID; 15:12's slave inverted at 28:68)
import cold_run_blessing_and_curse as BC        # THE EDGE: firstfruits_ebal_curses -> blessing_and_curse CALL, reference (11:29-30's Gerizim and Ebal — the form's seat 27:11-13 read forward; 11:13-17's rain state's two arms; 11:28's curse)
import cold_run_seven_nations as SN             # THE EDGE: firstfruits_ebal_curses -> seven_nations CALL, reference (7:6's holy people and the oath; 7:12-15's blessing list, no barren, the diseases turned — 28:4, 11, 18, 51, 60 forward; 7:25's abomination)
import cold_run_place_name as PN                # THE EDGE: firstfruits_ebal_curses -> place_name CALL, reference (12:5-7's place, the eras, eat there and rejoice — the first entry; 12:17's impure tithe's warning grounded by 26:14)
import cold_run_festivals_judges as FJ          # THE EDGE: firstfruits_ebal_curses -> festivals_judges CALL, reference (16:11 and 16:14's rejoicing; 16:16-17's appearing without measure; 16:19's bribe and wresting — 27:19, 27:25)
import cold_run_persons_poor_court as PP        # THE EDGE: firstfruits_ebal_curses -> persons_poor_court CALL, reference (24:17's triad — 27:19; 23:1's father's wife and skirt — 27:20; 25:9's tongue lent by I2; 22:1-4's ox inverted at 28:31)
import cold_run_refuge_war_family as RW         # THE EDGE: firstfruits_ebal_curses -> refuge_war_family CALL, reference (19:14's landmark — 27:17; 20:5-7's exemptions INVERTED at 28:30; 19:10's innocent blood; 21:23's burial; 20:19-20's siege turned)
import cold_run_sanctions as SA                 # THE EDGE: firstfruits_ebal_curses -> sanctions CALL, reference (Leviticus 18 and 20's four unions graded — 27:20-23; the curser's mode and either parent — 27:16)
import cold_run_mishpatim_3 as M3               # THE EDGE: firstfruits_ebal_curses -> mishpatim_3 CALL, reference (Exodus 21:17's parent curser at its first seat — 27:16; 21:12's killer — 27:24)
import cold_run_holiness as HO                  # THE EDGE: firstfruits_ebal_curses -> holiness CALL, reference (Leviticus 19:14's stumbling block before the blind — 27:18; 19:15's judgment)
import cold_run_second_tablets as ST            # THE EDGE: firstfruits_ebal_curses -> second_tablets CALL, reference (10:18's orphan and widow — 27:19; 10:22's seventy — 26:5, 28:62; Exodus 34:28's covenant words — 28:69)
import cold_run_courts_prophet as CP            # THE EDGE: firstfruits_ebal_curses -> courts_prophet CALL, reference (17:14-20's king exiled at 28:36, THE RETURN TO EGYPT 28:68's run citation of 17:16, the copy of the law — 27:3, 27:26, 28:58; right or left)
import cold_run_obey_horeb as OH                # THE EDGE: firstfruits_ebal_curses -> obey_horeb CALL, reference (4:26-28's perish, scatter, serve wood and stone — '28:36 and 28:64 forward'; 4:16-18's image list — 27:15; 4:10's covenant)
import cold_run_good_land as GL                 # THE EDGE: firstfruits_ebal_curses -> good_land CALL, reference (8:19-20's testimony — 'not hearken to the voice' 28:15, 45, 62; 8:10's eating; the receipt finder's own count receipt_seats(26..28) -> [], [], [])
import cold_run_covenant_at_horeb as CH         # THE EDGE: firstfruits_ebal_curses -> covenant_at_horeb CALL, reference (5:16's fifth word — 27:16; 5:8's image; 5:1's four verbs — 27:10; 5:15's hand and arm — 26:8; 5:2's Horeb — 28:69)
import cold_run_hear_o_israel as HI             # THE EDGE: firstfruits_ebal_curses -> hear_o_israel CALL, reference (6:3's 'as He spoke to you' — 27:3's run citation; 6:5's heart and soul — 26:16; 6:9's doorposts — the stones refused, the Sifrei 36:2)
import cold_run_decalogue as DC                 # THE EDGE: firstfruits_ebal_curses -> decalogue CALL, reference (Exodus 20:24-25's altar of stones and the hewn ban — 27:5-6; WRAPPED by law_ordinances; 20:4's image — 27:15)
import cold_run_ordinances as OR                # THE EDGE: firstfruits_ebal_curses -> ordinances CALL, reference (Exodus 23:25-26's bread and water blessed, no barren — 28:3-6; 23:4-5's beasts inverted at 28:31; 23:8's bribe)
import cold_run_exodus_story as ES              # THE EDGE: firstfruits_ebal_curses -> exodus_story CALL, reference (Exodus 1:11-14's bondage, 2:23's cry, 12:51's going out — the recital's retelling; 19:5-6's treasure — 26:18; 9:9's boil — 28:27, 35; 15:26's healer — 28:60)
import cold_run_korach as KO                    # THE EDGE: firstfruits_ebal_curses -> korach CALL, reference (Numbers 18:13's first fruits to the priest and the best triad — 26:2, 26:10; 18:21-32's tithe, the confession's clauses and the order — 26:13)
import cold_run_calendar as CA                  # THE EDGE: firstfruits_ebal_curses -> calendar CALL, reference (Exodus 23:19's first fruits' first-ness — the species fetched, Bikkurim 1:3; the two calendar parameters on the calendar's keys)
import cold_run_chukat as CK                    # THE EDGE: firstfruits_ebal_curses -> chukat CALL, reference (Numbers 20:15-16's recital clauses in the Edom letter — 26:7's 'and we cried' at the two seats alone)
import cold_run_tochacha as TC                  # THE EDGE: firstfruits_ebal_curses -> tochacha CALL, reference (Leviticus 26 whole — the covenant's three predicates, the five-gate cascade, the measures; the twin diffed at every inversion of 28:15-68)
import cold_run_naso as NS                      # THE EDGE: firstfruits_ebal_curses -> naso CALL, reference (Numbers 6:22-27's priests' blessing in the holy tongue by bless/bless with 27:12 — Sotah 33b; the Name)
import cold_run_joseph as JO                    # THE EDGE: firstfruits_ebal_curses -> joseph CALL, reference (Genesis 46:27's seventy — 26:5's 'few in number' and 28:62's echo; 47:4's sojourn)
import cold_run_primeval as PV                  # THE EDGE: firstfruits_ebal_curses -> primeval CALL, reference (Genesis 12:6's oaks of Moreh — Sotah 7:5's own analogy with 11:30 for 27:12; 15:5's stars — 28:62)
import cold_run_seducers as SE                  # THE EDGE: firstfruits_ebal_curses -> seducers CALL, reference (13:7's 'in secret' — the curses' KEY at 27:15, 27:24; 13:18's oath form; 13:7's 'wife of your bosom' — 28:54)
import cold_run_borders as BR                   # THE EDGE: firstfruits_ebal_curses -> borders CALL, reference (Numbers 34's roster — the tribes' orders compared with 27:12-13's two lists, a DATA row)
import cold_run_priesthood as PR                # THE EDGE: firstfruits_ebal_curses -> priesthood CALL, reference (Leviticus 22's holy food — 26:13's 'the holy' removed from the house; the priest of 26:3-4)
import cold_run_chatat as CT                    # THE EDGE: firstfruits_ebal_curses -> chatat CALL, reference (Leviticus 10:19's mourner — 26:14's 'not eaten in my mourning', the a fortiori for the holy of the generations)
import cold_run_opening_speech as OS            # THE EDGE: firstfruits_ebal_curses -> opening_speech CALL, reference (1:5's 'explain' — 27:8's 'very plainly', the root's two seats in the book)
import cold_run_journeys as JR                  # THE EDGE: firstfruits_ebal_curses -> journeys CALL, reference (Numbers 33:52's images destroyed at the entry — 27:15's graven and molten image)
import cold_run_sanctuary_build as SB           # THE EDGE: firstfruits_ebal_curses -> sanctuary_build CALL, reference (Exodus 27:1-8's bronze altar — the contrast with 27:5-6's field altar of whole stones)

'''
# ---- the generic helper block from the chapter 22-25 runner, by content markers ----
a = PPC.index('HERE = _os.path.dirname(_os.path.abspath(__file__))'); b = PPC.index('def LEN(b, c, v): return len(words(b, c, v))'); b = PPC.index('\n', b) + 1
helpers = PPC[a:b]
OLDW = "def W22(v): return words('Deut', 22, v)\ndef W23(v): return words('Deut', 23, v)\ndef W24(v): return words('Deut', 24, v)\ndef W25(v): return words('Deut', 25, v)\ndef W(c, v): return words('Deut', c, v)"
assert helpers.count(OLDW) == 1
helpers = helpers.replace(OLDW, "def W26(v): return words('Deut', 26, v)\ndef W27(v): return words('Deut', 27, v)\ndef W28(v): return words('Deut', 28, v)\ndef W(c, v): return words('Deut', c, v)")
left = [l for l in helpers.split('\n') if re.search(r'(?<!\d)(22|23|24|25)(?!\d)', re.sub(r'2026-09-\d\d|0x05[0-9A-F]{2}', '', l))]
print('helper lines still naming 22, 23, 24 or 25:', len(left), [l[:100] for l in left][:4]); assert not left, left[:3]
TAIL_A = '''def verse_text(ch, vs, book='Deut'): return ' '.join(words(book, ch, vs))
def _G(s): return s.split(' (')[0]   # a Hebrew token typed WITH ITS GLOSS beside it — the token alone returned (the lint's ninety-character window; 18b's form for the copied ink asserts)
DV = lambda c, v: ('Deut', c, v)
NEG_T = ('לא', 'ולא')   # (not; and not)
NAME = ('יהוה', 'ליהוה', 'ויהוה', 'ביהוה', 'מיהוה')   # (the LORD; to the LORD; and the LORD; in the LORD; from the LORD)
import difflib
def SH(a, b_): return sum(s for _, _, s in difflib.SequenceMatcher(a=words(*a), b=words(*b_)).get_matching_blocks())   # the reading's shared-run measure
CHS = (26, 27, 28)
NV = {c: len({v for (b, cc, v) in by if b == 'Deut' and cc == c}) for c in CHS}; assert NV == {26: 19, 27: 26, 28: 69}, NV   # nineteen, twenty-six and sixty-nine verses (the reading's divisions assert — the Hebrew's 28:69 the English's 29:1)
TOKN = {c: sum(len(W(c, v)) for v in range(1, NV[c] + 1)) for c in CHS}; assert TOKN == {26: 319, 27: 326, 28: 994}, TOKN   # the three chapters' tokens (the reading's store assert — the store the DB but at the two ketiv/qere seats 28:27 and 28:30)
SPAN = [(26, v) for v in range(1, 20)] + [(27, v) for v in range(1, 27)] + [(28, v) for v in range(1, 70)]
assert len(SPAN) == 114

P_ = []   # the provenance trail of the case being run
def ink(ref, note):  P_.append(('INK',  'Deut %s — %s' % (ref, note) if not ref[:1].isupper() else '%s — %s' % (ref, note)))
def move(src, note): P_.append(('MOVE', '%s — %s' % (src, note)))
def dat(note):       P_.append(('DATA', note))
def hyp(note):       P_.append(('HYP',  note))     # THE LINK REVIEW LAW: a hypothesis — no teacher; counted apart, never as compiled
def out(verdict, effects):
    """verdict + registry-validated effects (the engine contract)"""
    FX.validate([e for e in effects if e != FX.NONE])
    return verdict, effects, list(P_)

# ---- THE INK, computed (the parser and the tokens; the reading's facts the expectations — every assert PROVEN at the reading, ch26_ink.py — COPIED from the reading's instrument by content markers in five blocks; the store-, shelf-, Onkelos- and register-bound asserts left to the reading; the parser's facts typed from the ink's own asserts) ----
def MARKS(c, v): return [t for t in verse_words('Deut', c, v) if t[-1] in '#~^%@|*']
PARSE = {(c, v): (ink_numbers(verse_words('Deut', c, v)), ink_ordinals(verse_words('Deut', c, v)), MARKS(c, v)) for (c, v) in SPAN}
NUMV = [k for k in PARSE if PARSE[k][0]]; ORDV = [k for k in PARSE if PARSE[k][1]]; STARV = [k for k in PARSE if PARSE[k][2]]
print('THE INK (printed before it is asserted): PARSE %s, NUMV %s, ORDV %s, STARV %s, TOKN %s' % ({k: p for k, p in PARSE.items() if p[0] or p[1] or p[2]}, NUMV, ORDV, STARV, TOKN))
assert {k: p for k, p in PARSE.items() if p[0] or p[1] or p[2]} == {(26, 12): ([], [], ['לעשר*', 'מעשר*']), (28, 7): ([1, 7], [], []), (28, 25): ([1, 7], [], []), (28, 55): ([1], [], []), (28, 63): ([6], [], [])}, {k: p for k, p in PARSE.items() if p[0] or p[1] or p[2]}   # (to tithe*, the tithe* — the ten's homograph starred by the store); 28:7 and 28:25 one way and seven ways; 28:55 one of them a distributive; 28:63 THE FALSE SIX — "rejoiced" read as six (the reading's find; the Aramaic's "rejoiced" settles it)
assert NUMV == [(28, 7), (28, 25), (28, 55), (28, 63)] and ORDV == [] and STARV == [(26, 12)]
FALSE_SIX = verse_words('Deut', 28, 63)[2]; assert FALSE_SIX == 'שש' and verse_words('Deut', 28, 7)[9] == 'אחד' and verse_words('Deut', 28, 7)[12] == 'ובשבעה' and verse_words('Deut', 28, 55)[1] == 'לאחד'   # (rejoiced — the numeral's consonants; one; and by seven; to one of them) — the guard on the parser's false hit
NEG = {(c, v): [x for x in W(c, v) if x in NEG_T] for (c, v) in SPAN if any(x in NEG_T for x in W(c, v))}
NAME_BARE = sum(1 for (c, v) in SPAN for x in W(c, v) if x == 'יהוה')   # (the LORD)
print('THE NEGATIONS AND THE NAME (printed before they are asserted):', NEG, NAME_BARE)
assert NAME_BARE == 17 + 7 + 41 and {c: sum(len(v) for k, v in NEG.items() if k[0] == c) for c in CHS} == {26: 5, 27: 2, 28: 34}, (NAME_BARE, {c: sum(len(v) for k, v in NEG.items() if k[0] == c) for c in CHS})   # the Name bare seventeen in 26, seven in 27, forty-one in 28; the negations five, two, thirty-four (the reading's frames assert)
assert [f'{c}:{v}' for c, v in SPAN if 'לאמר' in W(c, v)] == ['27:1', '27:9', '27:11'] and [(c, v) for c, v in SPAN if 'אם' in W(c, v) or 'ואם' in W(c, v)] == [(28, 1), (28, 15), (28, 58)]   # ("saying" — the three frames of chapter 27; "if" — the two arms of the state row and the plagues' condition)
'''
def block(start, end):
    i = INKB.index(start); j = INKB.index(end, i); assert i < j, (start[:40], end[:40]); return INKB[i:j]
ink_block = (block("# THE KIN FOUND BY COMPUTATION (the measure's A section", "# ---- THE SHELF BY POSITION")
             + block("# THE FORMULAS (the measure's C)", "# THE KIN BY COMPUTATION (the measure's A")
             + block("# THE KIN BY COMPUTATION (the measure's A", "# THE TWINS DIFFED (the measure's B)")
             + block("# THE TWINS DIFFED (the measure's B)", "# ONKELOS (the measure's D)"))
lines = ink_block.split('\n')
DROP_RX = re.compile(r"(?<![A-Za-z_0-9])(byw|SG|sg|STORE_MISMATCH|VC|LED|sif|sif_he|onk|onk_he|Hb|HB0|ARM|SEATS|clean|heads|SP_|aramaic|arm|arm_e|E|kinrows|CS|_CS|H|A|HP|AP|sidx|glob|UIDS|PATCHED|OUT|EXP2DB|store|FAIL|_DUMP|_RC|_rink|DT)(?![A-Za-z_0-9])")
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
n_as = ink_block.count('\nassert '); print('the ink block: %d lines, %d asserts' % (ink_block.count('\n'), n_as)); assert n_as >= 10, n_as
KIN40 = tuple(S.KIN_UNMOVED); KIN_EXPECTED = tuple(S.KIN_UNMOVED[k] for k in KIN40); OWN91 = tuple(S.NEW_EFFECTS)
HOLE_WORDS = r"^(first_fruits\w*|tithe_remov\w*|tithe_confess\w*|tithe_in_\w*|tithe_for_the_dead\w*|statutes_this_day\w*|israel_declared\w*|lord_declared\w*|high_above\w*|holy_people_promised|great_stones\w*|stones_plastered\w*|whole_stones\w*|iron_on_altar\w*|ebal_offerings\w*|law_written\w*|became_the_lords\w*|hearken_and_do\w*|six_tribes\w*|levites_loud\w*|\w+_cursed|amen_answered\w*|blessed_\w*|enemies_flee\w*|storehouses_blessed|established_holy\w*|peoples_fear\w*|heavens_good\w*|lend_not_borrow|head_not_tail|turning_aside\w*|curses_for\w*|cursed_\w*|curse_confusion\w*|pestilence_cleaving|consumption_\w*|sword_blight\w*|heavens_brass\w*|rain_turned\w*|smitten_before\w*|carcass_food\w*|boil_of_egypt\w*|madness_\w*|wife_house\w*|ox_ass_flock\w*|sons_daughters\w*|fruit_eaten\w*|sore_boils\w*|exiled_with\w*|astonishment_\w*|seed_vines\w*|stranger_head\w*|curses_pursue\w*|iron_yoke\w*|enemies_served\w*|eagle_nation\w*|siege_in_all\w*|sons_flesh\w*|plagues_made\w*|diseases_of_egypt\w*|few_in_number\w*|scattered_among_all\w*|serving_wood\w*|trembling_heart\w*|life_hanging\w*|returned_to_egypt\w*|sold_and_none\w*|covenant_words\w*)$"
TAIL_B = '''
# ---- THE COUNTER'S DAY AND THE ONE DATABASE SCANNED (a bare world on the exodus epoch; no clock walk these chapters — no marker, no stretch; the first fruits' window and the confession's hour CLOCK DATA on the calendar's keys, no timer at a line) ----
with contextlib.redirect_stdout(io.StringIO()):
    _WC = WE.World(era='the counter\\'s day — chapters 26-28 on a bare world (the exodus epoch)', epoch='exodus')
_EX = _WC.clock.eras['exodus']
def DAY(y, m, d): return _WC.clock.day_in('exodus', y, m, d)
def DATE(day): return _EX.date(day)
COUNTER = DAY(40, 11, 1)
CLOCK = {'counter': DATE(COUNTER), 'no_marker': True, 'clock_data': ['the_first_fruits_window', 'the_confessions_hour', 'the_removal_date']}
print('THE CLOCK (printed before it is asserted):', CLOCK)
assert CLOCK['counter'] == (40, 11, 1), CLOCK
assert all(k in WE.CAL_PARAMS for k in CLOCK['clock_data']), [k for k in CLOCK['clock_data'] if k not in WE.CAL_PARAMS]   # the two calendar parameters on file (add_types_ch26_b.py) and the removal's date (12b's) — the received channel

# ---- THE ONE DATABASE SCANNED (the holes' ground — nothing names the ninety-one on Israel before this sitting; the references' entities and counts as the recon read them — DL4) ----
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
    """the entries of an effect in ONE full run of the tape (DL4's counts — the running world's): the one database folds several runs' rows under their sources (the checkpoint sections' names); the largest source is a whole run — None where the database is not built"""
    if not _os.path.exists(_WDB): return None
    c_ = sqlite3.connect('file:%s?mode=ro' % _WDB, uri=True)
    src = c_.execute("SELECT source FROM run_ledger GROUP BY source ORDER BY COUNT(*) DESC, source LIMIT 1").fetchone()[0]
    return c_.execute("SELECT COUNT(*) FROM run_ledger WHERE effect=? AND source=?", (effect, src)).fetchone()[0]
OWN91 = %(OWN91)r
assert len(OWN91) == 91 and len(set(OWN91)) == 91
HOLE_WORDS = r"%(HOLE_WORDS)s"
_hs = ledger_scan('israel_people', HOLE_WORDS); HOLE_SCAN = None if _hs is None else [e for e in _hs if e not in OWN91]   # this sitting's own names excluded once the fold carries them
KIN40 = %(KIN40)r
KIN_EXPECTED = %(KIN_EXPECTED)r   # DL4 — the recon's counts on the running world (ch26_compile_recon.out, section H; the callees' near names; the probe Q47's KIN tuple)
assert len(KIN40) == 40 == len(KIN_EXPECTED)
KIN_COUNTS = {k: count_scan(k) for k in KIN40}
REUSE4 = ('rejoicing_before_the_lord_commanded', 'poor_tithe_owed', 'blessings_for_hearing', 'rain_in_its_season')
REUSE_BEFORE = %(REUSE_BEFORE)r   # the reuses' counts BEFORE this sitting's lines (the recon) — after the fold carries the new entries the count is the after (the tape's second run reads it so)
REUSE_AFTER = %(REUSE_AFTER)r
REUSE_COUNTS = {k: count_scan(k) for k in REUSE4}
SCANS = {k: effect_scan(k) for k in KIN40[:8] + REUSE4 + ('gerizim_ebal_ceremony_owed', 'covenant_offered', 'other_gods_barred')}
del _hs   # 9b's lesson: the raw scans are the database's state at import — the derived lists are equal on the cached and the full load
_FXV = yaml.safe_load(open(_os.path.join(HERE, 'effect_vocabulary.yaml'), encoding='utf-8'))['effects']
print('THE SCANS (printed before they are asserted): holes %%s; the kin counts %%s; the reuses %%s; the entities %%s' %% (HOLE_SCAN, KIN_COUNTS, REUSE_COUNTS, SCANS))
assert HOLE_SCAN in ([], None), HOLE_SCAN   # THE HOLES' GROUND — nothing on Israel named the ninety-one before this sitting (DL4)
assert all(v is None for v in KIN_COUNTS.values()) or tuple(KIN_COUNTS.values()) == KIN_EXPECTED, [(k, KIN_COUNTS[k], e) for k, e in zip(KIN40, KIN_EXPECTED) if KIN_COUNTS[k] != e]   # the references' counts as the recon read them (DL4 — no second write)
assert all(v is None for v in REUSE_COUNTS.values()) or all(REUSE_COUNTS[k] in (REUSE_BEFORE[k], REUSE_AFTER[k]) for k in REUSE4), REUSE_COUNTS   # the reuses' counts the before (the first run) or the after (the fold carrying this sitting's lines)
SCANS_EXPECTED = _SCANS_EXPECTED_   # the entities per effect — typed from the first derive's print (the callees' way — printed before typed)
if SCANS_EXPECTED and any(v is not None for v in SCANS.values()): assert SCANS == SCANS_EXPECTED, [(k, SCANS[k], SCANS_EXPECTED.get(k)) for k in SCANS if SCANS[k] != SCANS_EXPECTED.get(k)]
assert all(k in _FXV for k in OWN91) and sum(1 for k in OWN91 if _FXV[k]['ledger_op'] == 'block') == 5 and sum(1 for k in OWN91 if _FXV[k]['ledger_op'] == 'status') == 33 and sum(1 for k in OWN91 if _FXV[k]['ledger_op'] == 'heaven') == 53, 'the ninety-one on the registry (add_types_ch26_a.py)'
assert _FXV['rejoicing_before_the_lord_commanded']['ledger_op'] == 'status' and _FXV['poor_tithe_owed']['ledger_op'] == 'status' and _FXV['blessings_for_hearing']['ledger_op'] == 'heaven' and _FXV['rain_in_its_season']['ledger_op'] == 'heaven' and _FXV['gerizim_ebal_ceremony_owed']['ledger_op'] == 'debit' and _FXV['treasured_people']['ledger_op'] == 'heaven', 'the reused and referenced rows\\' ops'
# THE TWINS DIFFED on the DB (the reading's kin asserts read again here — DL4; the shared run SH)
TWIN = {'28:1 vs 28:15': SH(DV(28, 1), DV(28, 15)), '28:1 vs 15:5': SH(DV(28, 1), DV(15, 5)), '28:3 vs 28:16': SH(DV(28, 3), DV(28, 16)), '28:4 vs 28:18': SH(DV(28, 4), DV(28, 18)), '28:5 vs 28:17': SH(DV(28, 5), DV(28, 17)), '28:6 vs 28:19': SH(DV(28, 6), DV(28, 19)), '28:7 vs 28:25': SH(DV(28, 7), DV(28, 25)),
        '28:36 vs 28:64': SH(DV(28, 36), DV(28, 64)), '26:8 vs 5:15': SH(DV(26, 8), DV(5, 15)), '26:9 vs Exod 3:8': SH(DV(26, 9), ('Exod', 3, 8)), '27:3 vs 6:3': SH(DV(27, 3), DV(6, 3)), '27:22 vs Lev 20:17': SH(DV(27, 22), ('Lev', 20, 17)), '27:16 vs Exod 21:17': SH(DV(27, 16), ('Exod', 21, 17)),
        '27:19 vs 24:17': SH(DV(27, 19), DV(24, 17)), '27:20 vs 23:1': SH(DV(27, 20), DV(23, 1)), '27:17 vs 19:14': SH(DV(27, 17), DV(19, 14)), '28:53 vs 28:55': SH(DV(28, 53), DV(28, 55)), '28:62 vs 26:5': SH(DV(28, 62), DV(26, 5)), '28:63 vs 30:9': SH(DV(28, 63), DV(30, 9)), '28:12 vs 15:6': SH(DV(28, 12), DV(15, 6)),
        '28:30 vs 20:5': SH(DV(28, 30), DV(20, 5)), '28:30 vs 20:6': SH(DV(28, 30), DV(20, 6)), '28:30 vs 20:7': SH(DV(28, 30), DV(20, 7)), '27:6 vs Josh 8:31': SH(DV(27, 6), ('Josh', 8, 31)), '27:5 vs Exod 20:25': SH(DV(27, 5), ('Exod', 20, 25)), '28:26 vs Jer 7:33': SH(DV(28, 26), ('Jer', 7, 33)), '26:19 vs 28:1': SH(DV(26, 19), DV(28, 1)), '28:69 vs Exod 34:28': SH(DV(28, 69), ('Exod', 34, 28)), '28:22 vs Lev 26:16': SH(DV(28, 22), ('Lev', 26, 16)), '28:23 vs Lev 26:19': SH(DV(28, 23), ('Lev', 26, 19))}
print('THE TWINS DIFFED (printed before they are asserted):', TWIN)
TWIN_EXPECTED = _TWIN_EXPECTED_
if TWIN_EXPECTED: assert TWIN == TWIN_EXPECTED, [(k, TWIN[k], TWIN_EXPECTED.get(k)) for k in TWIN if TWIN[k] != TWIN_EXPECTED.get(k)]   # typed from the first derive's print (the callees' way — printed before typed)
assert TWIN['28:1 vs 28:15'] >= 16 and TWIN['28:1 vs 15:5'] >= 14 and TWIN['28:36 vs 28:64'] >= 8 and TWIN['28:3 vs 28:16'] >= 4, TWIN   # the reading's largest twins (the condition and its negation sixteen, the hearkening fourteen, wood and stone eight, the city and the field)
'''
for _k, _v in (('%(OWN91)r', repr(OWN91)), ('%(HOLE_WORDS)s', HOLE_WORDS), ('%(KIN40)r', repr(KIN40)), ('%(KIN_EXPECTED)r', repr(KIN_EXPECTED)), ('%(REUSE_BEFORE)r', repr(S.REUSE_BEFORE)), ('%(REUSE_AFTER)r', repr(S.REUSE_AFTER))): TAIL_B = TAIL_B.replace(_k, _v)
TAIL_B = TAIL_B.replace('%%', '%')   # the print's own %s escaped inside the template
TWIN_EXPECTED = open(f'{SP}/ch26_twin_expected.txt').read().strip() if os.path.exists(f'{SP}/ch26_twin_expected.txt') else 'None'; SCANS_EXPECTED = open(f'{SP}/ch26_scans_expected.txt').read().strip() if os.path.exists(f'{SP}/ch26_scans_expected.txt') else 'None'   # the first derive's prints, parsed by ast from the fast checker's output and written to the two files — never typed by hand
GLOSS = {'זבת': 'flowing with', 'חלב': 'milk', 'ודבש': 'and honey', 'כל': 'all', 'דברי': 'the words of', 'התורה': 'the law', 'הזאת': 'this', 'ואמר': 'and shall say', 'העם': 'the people', 'אמן': 'Amen', 'לעם': 'a people', 'סגלה': 'treasured', 'עליון': 'high', 'על': 'above', 'במתי': 'few in', 'מעט': 'number',
         'ביד': 'with a hand', 'חזקה': 'mighty', 'ובזרע': 'and with an arm', 'נטויה': 'outstretched', 'שמוע': 'diligently', 'תשמע': 'you shall hearken', 'בקול': 'to the voice', 'הר': 'Mount', 'גרזים': 'Gerizim', 'עיבל': 'Ebal', 'בהר': 'in Mount', 'ראשית': 'the first of', 'פרי': 'fruit', 'מראשית': 'of the first of', 'ספר': 'the book of',
         'בספר': 'in the book of', 'ימין': 'right', 'ושמאול': 'and left', 'במצור': 'in the siege', 'ובמצוק': 'and in the distress', 'עץ': 'wood', 'ואבן': 'and stone', 'הברית': 'the covenant', 'בארץ': 'in the land of', 'מואב': 'Moab', 'בטנך': 'your womb', 'טנאך': 'your basket', 'ומשארתך': 'and your kneading trough', 'בדרך': 'by way',
         'אחד': 'one', 'ככוכבי': 'as the stars of', 'השמים': 'the heavens', 'לרב': 'for multitude', 'לראש': 'the head', 'ולא': 'and not', 'לזנב': 'the tail', 'כנף': 'the skirt of', 'אביו': 'his father', 'ארור': 'cursed', 'שחד': 'a bribe', 'ושחד': 'and a bribe', 'בסתר': 'in secret', 'ארץ': 'a land', 'אחתו': 'his sister', 'בת': 'the daughter of',
         'או': 'or', 'אמו': 'his mother', 'אשר': 'which', 'יציק': 'distresses', 'לך': 'you', 'איבך': 'your enemy', 'כאשר': 'as', 'שש': 'rejoiced', 'ואמו': 'and his mother', 'אבנים': 'stones', 'גזית': 'hewn', 'שלמות': 'whole', 'משפט': 'the judgment of', 'גר': 'the stranger', 'יתום': 'the orphan', 'לא': 'not', 'יהוה': 'the LORD',
         'ליהוה': 'to the LORD', 'ויהוה': 'and the LORD', 'ביהוה': 'in the LORD', 'מיהוה': 'from the LORD', 'לעשר': 'to tithe', 'מעשר': 'the tithe', 'ובשבעה': 'and by seven', 'לאחד': 'to one', 'לאמר': 'saying', 'אם': 'if', 'ואם': 'and if', 'ואת': 'and-it', 'את': 'the object marker', 'וכל': 'and all', 'ועל': 'and on', 'אל': 'to', 'ואל': 'and to', 'כי': 'for'}
MISSING = []
def glossify(text):
    def repl(m):
        tok = m.group(1); key = tok.rstrip('*')
        if key not in GLOSS: MISSING.append(tok); return m.group(0)
        return "_G('%s (%s)')" % (tok, GLOSS[key])
    out_ = []
    for l in text.split('\n'):
        if l.lstrip().startswith('#') or 'STOP = set((' in l or l.lstrip().startswith("'") and '   # (' in l: out_.append(l); continue   # the comments and the glossed STOP set kept
        out_.append(re.sub(r"'([\u05D0-\u05EA\u05F0-\u05F4]+\*?)'", repl, l))
    return '\n'.join(out_)
TAIL_A = glossify(TAIL_A); ink_block = glossify(ink_block)
assert not MISSING, ('a Hebrew token without a gloss in the table', sorted(set(MISSING)))
src = HEAD + helpers + TAIL_A + ink_block + TAIL_B.replace('_TWIN_EXPECTED_', TWIN_EXPECTED).replace('_SCANS_EXPECTED_', SCANS_EXPECTED) + FACTS
open(f'{SP}/ch26_part1.py', 'w', encoding='utf-8').write(src)
import py_compile; py_compile.compile(f'{SP}/ch26_part1.py', doraise=True)
lint = subprocess.run([sys.executable, f'{ROOT}/logic/solo_tools/gloss_lint.py', f'{SP}/ch26_part1.py'], capture_output=True, text=True).stdout.strip().split('\n')[-1]; print('the lint on part 1:', lint); assert lint.endswith('0 flag(s)'), lint
print('part1 derived: %d bytes; helpers %d, ink block %d (asserts %d); dropped %d store-bound lines; the callees\' facts %d bytes; TWIN_EXPECTED %s; SCANS_EXPECTED %s' % (len(src), len(helpers), len(ink_block), n_as, len(drop), len(FACTS), TWIN_EXPECTED[:40], SCANS_EXPECTED[:40]))

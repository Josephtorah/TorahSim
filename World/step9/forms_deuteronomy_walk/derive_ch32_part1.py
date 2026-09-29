#!/usr/bin/env python3
# THE DEUTERONOMY WALK 20b: cold_run_song_charge_nebo.py PART 1 derived — the head typed here; the generic helper block COPIED from the chapter 29-31 runner by content
# markers (HERE = … through def LEN — the parser exec, the DB, the phrase/lemma/diff helpers; W29-W31 made W32 and W); THE INK BLOCKS COPIED from the reading's own
# instrument ch32_ink.py by content markers — SIX blocks (the kin found by computation and the frames; the kin re-scored; the twins diffed; the formulas over the Torah and the
# Bible; the words; the frames, the register and the parser), the store-, shelf-, Onkelos- and register-bound lines DROPPED by name (10b's lesson 6 — the count read from the
# print); every Hebrew token GLOSSED from the store's own print (ch32_store_glosses.txt) with a small table for the tokens of other verses; THE COUNTER'S DAY (Moses' last day —
# NO MARKER), the one-database scans, and THE CALLEES' FACTS (ch32_callees_facts.py — printed at the first pass, asserted from the print at the second). Asserted substitutions
# throughout. derive_ch29_part1.py's form over one chapter with NO MARKER. RUN FROM THE REPO ROOT with PYTHONPATH the scratchpad.
import subprocess, re, os, sys, ast
ROOT = _ROOT
SP = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, SP)
import ch32b_spec as S
CRC = open(f'{ROOT}/World/step9/cold_run_covenant_return_charge.py', encoding='utf-8').read()
INKB = open(f'{SP}/ch32_ink.py', encoding='utf-8').read()
FACTS = open(f'{SP}/ch32_callees_facts.py', encoding='utf-8').read()
assert FACTS.startswith('\n# ---- THE CALLEES\' FACTS'), 'the callees\' facts (ch32_callees_facts.py)'
FA_ASSERTS = open(f'{SP}/ch32_fact_asserts.py', encoding='utf-8').read() if os.path.exists(f'{SP}/ch32_fact_asserts.py') else "# (the facts' asserts — written from the first pass's print at the second derive)\n"
FACTS = FACTS.replace('_FACT_ASSERTS_', FA_ASSERTS)
HEAD = '''#!/usr/bin/env python3
# DEUTERONOMY 32:1-52 — THE SONG (give ear, O heavens, and hear, O earth; the doctrine as rain; the Name proclaimed and the Rock whose work is perfect; the crooked generation and
# the Father who acquired you; remember the days of old — the nations divided by the number of the children of Israel, the LORD's portion His people; found in the desert, kept as
# the apple of His eye, borne as an eagle, the LORD alone; the heights of the land, honey from the rock, the feast of curd and milk and fat and wine; Jeshurun grew fat and kicked,
# demons and new gods, the Rock that begot you forgotten; the LORD saw and spurned — I will hide My face, jealousy by a no-people, a fire to the lowest Sheol; the evils heaped,
# hunger and beasts and serpents, the sword without and terror within; the blotting out stayed by the enemy's boast, a nation void of counsel; one chasing a thousand — their Rock
# sold them, the vine of Sodom; the cup in store, vengeance is Mine, the LORD judges His people, where are their gods; see now that I, I am He — I kill and I make alive, the hand
# lifted to heaven, the sword whetted, sing, O nations — the land atones) AND ITS FRAME (Moses came and spoke the song, he and Hoshea son of Nun; set your heart — it is your
# life and no empty matter; the LORD spoke that selfsame day: go up to Nebo, see the land, die in the mountain as Aaron died in Hor; because you trespassed at Meribath-kadesh,
# you shall see the land but not go there); THE READBACK'S FORMS ON FILE, NO NEW FORM (THE DEUTERONOMY WALK sitting 20b — THE LEAN PASS, 2026-09-28; World/step9/DEUTERONOMY_WALK.md
# "Sitting 20b"; the state doc's #235). ONE RUNNER OVER ONE CHAPTER AND TWO UNITS (deu_32_haazinu — the song 32:1-43; deu_32_song_aftermath — the frame 32:44-52; the span one
# range); SIXTEEN own-day lines IN THREE FORMS — 14 SPEECHES (the song's twelve stanzas, Moses' witness-song with the LORD's own words inside it from 32:20; the LORD's two to Moses
# at 32:48 and 32:51), 1 ACT (32:44), 1 STATUTE (32:46): EVERY LINE AT MOSES' LAST DAY (40, 12, 7) after 19b's ONE MARKER at 31:1 — NO MARKER HERE (32:48's selfsame day THAT day;
# the Sifrei 337:1): song_witnesses_called_declared (32:1-4), song_crooked_generation_declared (32:5-6), song_nations_divided_lords_portion_declared (32:7-9),
# song_found_in_the_desert_declared (32:10-12), song_heights_honey_rock_declared (32:13-14), song_jeshurun_fat_kicked_declared (32:15-18), song_face_hidden_foolish_nation_declared
# (32:19-22), song_evils_heaped_declared (32:23-25), song_enemys_boast_declared (32:26-28), song_one_chasing_a_thousand_declared (32:29-33), song_vengeance_in_store_declared
# (32:34-38), song_i_am_he_declared (32:39-43), song_spoken_by_moses_and_hoshea (32:44-45, an act), set_your_heart_no_empty_matter_declared (32:46-47, a statute),
# nebo_summons_die_as_aaron (32:48-50, a speech), meribah_trespass_not_go_there_declared (32:51-52, a speech) — FORTY-FIVE writes on THREE ledgers (forty-two NEW: thirty-two
# STATUSES, ten HEAVEN entries, no block — Israel 36, Moses 5, Joshua 1 (the entity yehoshua); THREE REUSES: heaven_and_earth_witness 32:1 the chain's fifth seat, face_hidden_and_forsaken_foretold
# 32:20 the third time, length_of_days_on_the_land_promised 32:47). THE PARSER'S TWO GUARDS as DATA rows (THE FALSE EIGHT at 32:15 — 'you grew fat' a verb; THE JOINED THOUSAND at
# 32:30 — [1, 1002] a proverb), no count in the world. THE KIN'S CELLS BY CALL (forty-two runners, every edge REFERENCE — the kin read this chapter forward: the witnesses' chain's fifth
# seat, the song ahead, the commission's mountain and its debit OPEN to 34:1-4, Meribah's sentence, Hoshea's old name, Aaron's death the receipt); THE TAPE'S LINES BY KIND (the manna,
# the water from the rock, the cloud and the well, Sinai's eagle, the plagues, Babel's division, the flood's boarding, the exodus's day, Sodom's overthrow, Aaron's death, the sentence
# at Meribah, the song commanded and spoken, the hidden face). Sixteen cells and the table; every token probed (zero-report law); effects on every cell (the effects law); THE EXAM THE
# TWENTY-SIX MISHNAH AND TOSEFTA ROWS THE LEDGER CITES (Berakhot 1:1, 2:2, 7:1, 8:8; Sanhedrin 3:5, 5:2, 9:1; Sotah 1:7, 9:9; Chagigah 1:8; Peah 1:1, 3:2; Kilayim 3:2; Nedarim 1:2;
# Shevuot 7:5; Avodah Zarah 3:4; Avot 3:6, 5:1, 5:6, 6:9, 6:10; Tosefta Arakhin 1:4, Avodah Zarah 9:4, Peah 1:1-3 — read whole; Mishnah Peah 1:3 read whole and excluded; no docket, the
# lean form); the parameters the runner's DATA rows, NO clock datum (19b's death date THE DAY). The daemon law_song_charge_nebo given_at Deut 32:1, installed_by boot (the Deuteronomy
# daemons' form). Reading ledger: logic/oral_triage/deu_32_haazinu_2026-09-27.md; the lean exam: deu_32_haazinu_exam_2026-09-28.md.

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
import cold_run_obey_horeb as OH                 # THE EDGE: song_charge_nebo -> obey_horeb CALL, reference (4:26's witnesses — THE CHAIN'S FIFTH SEAT at 32:1; 4:19's host apportioned — 32:8; 4:24's fire — 32:22; 4:35's 'none else' — 32:39)
import cold_run_covenant_return_charge as CR    # THE EDGE: song_charge_nebo -> covenant_return_charge CALL, reference (31:19-30's song commanded, written and spoken — the song ahead named forward; 31:17-18's hidden face — 32:20 REUSED; 31:20's satiety — 32:15's twin taught; 30:20's length of days — 32:47 REUSED; the marker's day (40, 12, 7); the three gifts owed at 34:5)
import cold_run_good_land as GL                  # THE EDGE: song_charge_nebo -> good_land CALL, reference (8:15-16's wilderness, flint and manna — 32:10, 32:13; 8:11-19's forgetting — 32:15-18; 'in your end' — 32:20, 32:29; the receipt finder [] over 32)
import cold_run_exodus_story as ES               # THE EDGE: song_charge_nebo -> exodus_story CALL, reference (Exodus 16-19's desert and eagle — 32:10-11, 19:4's twin taught at 314:3; 15:16's 'acquired' — 32:6; 12:41's selfsame day — 32:48; the plagues and the healing)
import cold_run_refuge_war_family as RW          # THE EDGE: song_charge_nebo -> refuge_war_family CALL, reference (19:15's one witness barred — the court law at 32:1; the heifer's verb — 32:2's homograph; 21:8's innocent blood — 32:43)
import cold_run_persons_poor_court as PP         # THE EDGE: song_charge_nebo -> persons_poor_court CALL, reference (22:9's vineyard — Kilayim 3:2 at 32:14; 22:7's nest — Peah 1:1's list at 32:47)
import cold_run_courts_prophet as CP             # THE EDGE: song_charge_nebo -> courts_prophet CALL, reference (17:6's two witnesses and the seven investigations — the court law read into 32:1's witnesses, Sanhedrin 5:2; 17:3's acts — 32:17)
import cold_run_refuge as RF                     # THE EDGE: song_charge_nebo -> refuge CALL, reference (Numbers 35:23's enemy neither witness nor judge — 32:31, Sanhedrin 3:5; 35:33's land's atonement — 32:43; 35:31's no ransom — 32:39; 35:30's one witness)
import cold_run_ordinances as OR                 # THE EDGE: song_charge_nebo -> ordinances CALL, reference (Exodus 21:22's judges — 32:31's pelilim, a homograph by word; 21:30's ransom — 329:4's soul beyond ransom)
import cold_run_chukat as CK                     # THE EDGE: song_charge_nebo -> chukat CALL, reference (Numbers 20:22-29 Aaron's death — 32:50 THE RECEIPT, the pointer a run citation; 20:12-13 the sentence at Meribah — 32:51; 21:6's serpents — 32:24; 19:14's tent — 339:1)
import cold_run_opening_speech as OS             # THE EDGE: song_charge_nebo -> opening_speech CALL, reference (Numbers 27:12-14's commission retold — 32:49's mountain, the sentence cited, the debit OPEN to 34:1-4, the receipt; 3:1-14's Bashan — 32:14; 3:27's Pisgah — 32:52)
import cold_run_journeys as JR                   # THE EDGE: song_charge_nebo -> journeys CALL, reference (Numbers 33:38-40 Aaron's death retold — 32:50, a retelling never writes an act twice; the four writings; the death date (40, 5, 1), the age 123)
import cold_run_second_tablets as ST             # THE EDGE: song_charge_nebo -> second_tablets CALL, reference (10:6's Moserah against Mount Hor — 32:50's OPEN row; 10:16's heart — 32:18)
import cold_run_primeval as PV                   # THE EDGE: song_charge_nebo -> primeval CALL, reference (Genesis 10:25 and 11's division — 32:8 by the ink's words, the twin a hypothesis; 7:13's selfsame day — 32:48; 6:5's inclination)
import cold_run_pre_sinai as PS                  # THE EDGE: song_charge_nebo -> pre_sinai CALL, reference (Genesis 9's sons of Noah — 32:28's seven commandments, Tosefta Avodah Zarah 9:4; 17:23, 26's selfsame day — 32:48)
import cold_run_mamre as MA                      # THE EDGE: song_charge_nebo -> mamre CALL, reference (Genesis 19:24-25 Sodom's overthrow — 32:32's vine; 14:19's possessor — 32:6's acquired; 14:22's lifted hand — 32:40)
import cold_run_family as FA                     # THE EDGE: song_charge_nebo -> family CALL, reference (Genesis 46:27's seventy souls — 32:8's number; 49:33's gathering — 32:50's form)
import cold_run_balak as BK                      # THE EDGE: song_charge_nebo -> balak CALL, reference (Numbers 23:9's 'a people that dwells alone' — 32:12's alone; the Sifrei 356:5)
import cold_run_beha as BH                       # THE EDGE: song_charge_nebo -> beha CALL, reference (Numbers 11's manna and the three gifts — the well, the cloud, the manna at 32:10; Taanit 9a)
import cold_run_shelach as SHL                   # THE EDGE: song_charge_nebo -> shelach CALL, reference (Numbers 13:16 Hoshea to Joshua — 32:44's old name; 14:16's 'lest they say' — 32:27)
import cold_run_not_righteousness as NR          # THE EDGE: song_charge_nebo -> not_righteousness CALL, reference (9:28's 'lest the land say' — 32:27's kin; 9:22-24's ten trials)
import cold_run_seven_nations as SN              # THE EDGE: song_charge_nebo -> seven_nations CALL, reference (7:6's holy people, 26:18's treasure — 32:9's portion beside them, UNMOVED; 7:8's oath by kind — 32:40)
import cold_run_hear_o_israel as HI              # THE EDGE: song_charge_nebo -> hear_o_israel CALL, reference (6:4's unity — 32:39's creed; 6:7's teaching — 32:46; the recitation times — Berakhot 1:1 at 333:4)
import cold_run_blessing_and_curse as BC         # THE EDGE: song_charge_nebo -> blessing_and_curse CALL, reference (11:14's early and latter rain — 32:2's four rains; 11:9's length of days — 32:47 REUSED)
import cold_run_firstfruits_ebal_curses as FE    # THE EDGE: song_charge_nebo -> firstfruits_ebal_curses CALL, reference (28:49's eagle nation — 32:21; 28:53-61's siege and plagues — 32:23-25; 28:7 and 28:25 — 32:30's two arms; 26:2's first fruits and the things without measure — 32:47)
import cold_run_tochacha as TC                   # THE EDGE: song_charge_nebo -> tochacha CALL, reference (Leviticus 26:22's beasts and 26:25's sword — 32:24-25 by the ink's shared words, the twin a hypothesis; 26:8's five chase a hundred — 32:30)
import cold_run_seducers as SE                   # THE EDGE: song_charge_nebo -> seducers CALL, reference (13:7's 'gods you have not known' — 32:17's 'gods they knew not')
import cold_run_decalogue as DC                  # THE EDGE: song_charge_nebo -> decalogue CALL, reference (5:11's vain Name — 328:4's Name profaned punished at once)
import cold_run_covenant_at_horeb as CH          # THE EDGE: song_charge_nebo -> covenant_at_horeb CALL, reference (5:1's assembly and Exodus 24:7's 'in the ears of the people' — 32:44)
import cold_run_naso as NS                       # THE EDGE: song_charge_nebo -> naso CALL, reference (Sotah 1:7's measure for measure — 32:5, 32:15 at the Sifrei 308:4, 318:8)
import cold_run_incense_shekel as IS             # THE EDGE: song_charge_nebo -> incense_shekel CALL, reference (Exodus 30:12's ransom of the soul — 329:4's no ransom at 32:39)
import cold_run_festivals_judges as FJ           # THE EDGE: song_charge_nebo -> festivals_judges CALL, reference (16:16's appearing, not empty, the gift of the hand — Peah 1:1's things without measure at 32:47; Chagigah 1:8's festival offerings)
import cold_run_holiness as HL                   # THE EDGE: song_charge_nebo -> holiness CALL, reference (Leviticus 19:9-10's corner — Peah 3:2 at 32:14, Peah 1:1 and Tosefta Peah 1:3 at 32:47, 32:34)
import cold_run_vows as VW                       # THE EDGE: song_charge_nebo -> vows CALL, reference (Nedarim 1:2's substitutes — 32:3's Name at 306:36; the sage's release — Chagigah 1:8 at 32:46)
import cold_run_food_tithe as FT                 # THE EDGE: song_charge_nebo -> food_tithe CALL, reference (14:1's sonship — 32:5's 'His children')
import cold_run_gad_reuben as GR                 # THE EDGE: song_charge_nebo -> gad_reuben CALL, reference (Numbers 32:38's Nebo — 32:49; Moses' grave: Reuben's Nebo, Gad's field, Sotah 13b)
import cold_run_borders as BR                    # THE EDGE: song_charge_nebo -> borders CALL, reference (Numbers 34:2's land of Canaan — 32:49)
import cold_run_erection as ER                   # THE EDGE: song_charge_nebo -> erection CALL, reference (Exodus 32:12's argument at the calf — 32:27; the shown face — 32:20's hidden face)
import cold_run_sanctions as SA                  # THE EDGE: song_charge_nebo -> sanctions CALL, reference (Sanhedrin 9:1's burned and beheaded — 32:4's 'all His ways are justice' at 307:14)
import cold_run_vayikra5 as V5                   # THE EDGE: song_charge_nebo -> vayikra5 CALL, reference (Leviticus 5:15's sacrilege — Chagigah 1:8's mountains by a hair at 32:46)
import cold_run_moadim as MD                     # THE EDGE: song_charge_nebo -> moadim CALL, reference (Leviticus 23's feasts — Chagigah 1:8's festival offerings at 32:46)
import cold_run_mekoshesh as MK                  # THE EDGE: song_charge_nebo -> mekoshesh CALL, reference (Numbers 15:32's gatherer — Chagigah 1:8's Sabbath laws by a hair at 32:46)

'''
# ---- the generic helper block from the chapter 29-31 runner, by content markers ----
a = CRC.index('HERE = _os.path.dirname(_os.path.abspath(__file__))'); b = CRC.index('def LEN(b, c, v): return len(words(b, c, v))'); b = CRC.index('\n', b) + 1
helpers = CRC[a:b]
OLDW = "def W29(v): return words('Deut', 29, v)\ndef W30(v): return words('Deut', 30, v)\ndef W31(v): return words('Deut', 31, v)\ndef W(c, v): return words('Deut', c, v)"
assert helpers.count(OLDW) == 1
helpers = helpers.replace(OLDW, "def W32(v): return words('Deut', 32, v)\ndef W(c, v): return words('Deut', c, v)")
left = [l for l in helpers.split('\n') if re.search(r'(?<!\d)(29|30|31)(?!\d)', re.sub(r'2026-09-\d\d|0x05[0-9A-F]{2}', '', l))]
print('helper lines still naming 29, 30 or 31:', len(left), [l[:100] for l in left][:4]); assert not left, left[:3]
TAIL_A = '''def verse_text(ch, vs, book='Deut'): return ' '.join(words(book, ch, vs))
def _G(s): return s.split(' (')[0]   # a Hebrew token typed WITH ITS GLOSS beside it — the token alone returned (the lint's ninety-character window; 18b's form for the copied ink asserts)
DV = lambda c, v: ('Deut', c, v)
NEG_T = ('לא', 'ולא')   # (not; and not)
NAME = ('יהוה', 'ליהוה', 'ויהוה', 'ביהוה', 'מיהוה')   # (the LORD; to the LORD; and the LORD; in the LORD; from the LORD)
import difflib
def SH(a, b_): return sum(s for _, _, s in difflib.SequenceMatcher(a=words(*a), b=words(*b_)).get_matching_blocks())   # the reading's shared-run measure
CHS = (32,)
NV = {c: len({v for (b, cc, v) in by if b == 'Deut' and cc == c}) for c in CHS}; assert NV == {32: 52}, NV   # fifty-two verses (the reading's divisions assert — the identity)
TOKN = {c: sum(len(W(c, v)) for v in range(1, NV[c] + 1)) for c in CHS}
print('THE TOKENS (printed before they are asserted):', TOKN)
TOKN_EXPECTED = _TOKN_EXPECTED_   # typed from the first derive's print (the callees' way — printed before typed)
if TOKN_EXPECTED: assert TOKN == TOKN_EXPECTED, (TOKN, TOKN_EXPECTED)
SPAN = [(32, v) for v in range(1, 53)]
assert len(SPAN) == 52

P_ = []   # the provenance trail of the case being run
def ink(ref, note):  P_.append(('INK',  'Deut %s — %s' % (ref, note) if not ref[:1].isupper() else '%s — %s' % (ref, note)))
def move(src, note): P_.append(('MOVE', '%s — %s' % (src, note)))
def dat(note):       P_.append(('DATA', note))
def hyp(note):       P_.append(('HYP',  note))     # THE LINK REVIEW LAW: a hypothesis — no teacher; counted apart, never as compiled
def out(verdict, effects):
    """verdict + registry-validated effects (the engine contract)"""
    FX.validate([e for e in effects if e != FX.NONE])
    return verdict, effects, list(P_)

# ---- THE INK, computed (the parser and the tokens; the reading's facts the expectations — every assert PROVEN at the reading, ch32_ink.py — COPIED from the reading's instrument by content markers in six blocks; the store-, shelf-, Onkelos- and register-bound asserts left to the reading; the parser's facts typed from the measure's print as the ink instrument asserted them) ----
def MARKS(c, v): return [t for t in verse_words('Deut', c, v) if t[-1] in '#~^%@|*']
PARSE = {(c, v): (ink_numbers(verse_words('Deut', c, v)), ink_ordinals(verse_words('Deut', c, v)), MARKS(c, v)) for (c, v) in SPAN}
NUMV = [k for k in PARSE if PARSE[k][0]]; ORDV = [k for k in PARSE if PARSE[k][1]]; STARV = [k for k in PARSE if PARSE[k][2]]
print('THE INK (printed before it is asserted): PARSE %s, NUMV %s, ORDV %s, STARV %s, TOKN %s' % ({k: p for k, p in PARSE.items() if p[0] or p[1] or p[2]}, NUMV, ORDV, STARV, TOKN))
assert {k: p for k, p in PARSE.items() if p[0] or p[1] or p[2]} == {(32, 15): ([8], [], []), (32, 30): ([1, 1002], [], ['אחד|'])}, {k: p for k, p in PARSE.items() if p[0] or p[1] or p[2]}   # the reading's parser assert (ch32_ink.py from ch32_measure_lean.out): 32:15 THE FALSE EIGHT (you grew fat), 32:30 THE JOINED THOUSAND (one chase a thousand, and two — [1, 1002] with 'one' marked)
assert NUMV == [(32, 15), (32, 30)] and ORDV == [] and STARV == [(32, 30)]
FALSE_EIGHT = W(32, 15)[3]; assert FALSE_EIGHT == 'שמנת' and W(32, 15)[0:3] == ['וישמן', 'ישרון', 'ויבעט'] and W(32, 15)[4:6] == ['עבית', 'כשית']   # (you grew fat — the eight's consonants, a verb: and Jeshurun grew fat and kicked; you grew thick, you became gross) — the guard on the parser's false hit
JOINED = W(32, 30)[1:7]; assert JOINED == ['ירדף', 'אחד', 'אלף', 'ושנים', 'יניסו', 'רבבה']   # (chase; one; a thousand; and two; put to flight; ten thousand) — the four numbers the Sifrei 322:10 reads aloud, the parser's [1, 1002] a proverb, no count
NEG = {(c, v): [x for x in W(c, v) if x in NEG_T] for (c, v) in SPAN if any(x in NEG_T for x in W(c, v))}
NAME_BARE = sum(1 for (c, v) in SPAN for x in W(c, v) if x == 'יהוה')   # (the LORD)
print('THE NEGATIONS AND THE NAME (printed before they are asserted):', NEG, NAME_BARE)
NAME_BARE_EXPECTED = _NAME_BARE_EXPECTED_   # typed from the first derive's print
if NAME_BARE_EXPECTED: assert NAME_BARE == NAME_BARE_EXPECTED, (NAME_BARE, NAME_BARE_EXPECTED)
NEG_EXPECTED = _NEG_EXPECTED_   # the negations per verse, typed from the first derive's print
if NEG_EXPECTED: assert {'%d:%d' % k: len(v) for k, v in NEG.items()} == NEG_EXPECTED, {'%d:%d' % k: len(v) for k, v in NEG.items()}
assert [f'{c}:{v}' for c, v in SPAN if 'לאמר' in W(c, v)] == ['32:48'] and [(c, v) for c, v in SPAN if 'אם' in W(c, v)] == [(32, 30), (32, 41)] and [(c, v, x) for c, v in SPAN for x in W(c, v) if x == 'פן'] == [(32, 27, 'פן'), (32, 27, 'פן')] and [(c, v) for c, v in SPAN if 'לא' in W(c, v) and 'תבוא' in W(c, v)] == [(32, 52)]   # ("saying" — the one divine frame at 32:48; "if" — the joined thousand's and the sword's; "lest" — the enemy's boast twice; "you shall not go" — the chapter's close) — the reading's frames assert
'''
def block(start, end):
    i = INKB.index(start); j = INKB.index(end, i); assert i < j, (start[:40], end[:40]); return INKB[i:j]
ink_block = (block("# THE KIN FOUND BY COMPUTATION (the measure's A section", "# ---- THE ASSERTS TYPED FROM THE PRINTS (block a")
             + block("# THE KIN BY COMPUTATION: THE SONG'S VOCABULARY IS ITS OWN", "# THE TWINS DIFFED (shared / the longest run)")
             + block("# THE TWINS DIFFED (shared / the longest run)", "# THE FORMULAS (phrase seats by consonants")
             + block("# THE FORMULAS (phrase seats by consonants", "# THE WORDS: eight 'rock' words")
             + block("# THE WORDS: eight 'rock' words", "# ONKELOS WRITING THE MEANING")
             + block("# THE FRAMES, THE REGISTER AND THE PARSER", "# THE PRIOR READS"))
lines = ink_block.split('\n')
DROP_RX = re.compile(r"(?<![A-Za-z_0-9])(byw|SG|sg|STORE_MISMATCH|VC|LED|sif|sif_he|onk|onk_he|Hb|HB0|ARM|SEATS|clean|heads|SP_|aramaic|arm|arm_e|E|kinrows|CS|_CS|H|A|HP|AP|sidx|glob|UIDS|PATCHED|OUT|EXP2DB|store|FAIL|_DUMP|_RC|_rink|DT|_MP|SPINE_PRIOR|FRESH|PRIOR_READ)(?![A-Za-z_0-9])")
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
KIN62 = tuple(S.KIN_UNMOVED); KIN_EXPECTED = tuple(S.KIN_UNMOVED[k] for k in KIN62); OWN42 = tuple(S.NEW_EFFECTS)
HOLE_WORDS = r"^(" + '|'.join(sorted({'_'.join(n.split('_')[:3]) + r'\w*' for n in OWN42})) + r")$"
TAIL_B = '''
# ---- THE COUNTER'S DAY (a bare world on the exodus epoch; Moses' last day (40, 12, 7) — 19b's ONE MARKER at 31:1 stands, NO MARKER here; 32:48's selfsame day THAT day; the death date 19b's clock datum on the calendar's keys, read here) ----
with contextlib.redirect_stdout(io.StringIO()):
    _WC = WE.World(era='Moses\\' last day — chapter 32 on a bare world (the exodus epoch)', epoch='exodus')
_EX = _WC.clock.eras['exodus']
def DAY(y, m, d): return _WC.clock.day_in('exodus', y, m, d)
def DATE(day): return _EX.date(day)
MOSES_120 = DAY(40, 12, 7); COUNTER = MOSES_120
CLOCK = {'counter': DATE(COUNTER), 'marker': None, 'marker_verse': None, 'marker_at': None, 'days_walked': 0, 'the_day_by': "19b's marker at Deut 31:1 (the number's verse 31:2) — the_death_date_of_moses on the calendar's keys", 'clock_data': ['the_death_date_of_moses']}
print('THE CLOCK (printed before it is asserted):', CLOCK)
assert CLOCK['counter'] == (40, 12, 7) and CLOCK['marker'] is None and CLOCK['days_walked'] == 0, CLOCK
assert all(k in WE.CAL_PARAMS for k in CLOCK['clock_data']), [k for k in CLOCK['clock_data'] if k not in WE.CAL_PARAMS]   # 19b's calendar parameter on file — the received channel
assert WE.CAL_PARAMS['the_death_date_of_moses']['exercised_by'] == ['covenant_return_charge'], WE.CAL_PARAMS['the_death_date_of_moses']['exercised_by']   # 19b's row UNTOUCHED (add_types_ch32_b.py — the calendar untouched)

# ---- THE ONE DATABASE SCANNED (the holes' ground — nothing names the forty-two on their ledgers before this sitting; the references' entities and counts as the recon read them — DN4) ----
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
    """the entries of an effect in ONE full run of the tape (DN4's counts — the running world's): the one database folds several runs' rows under their sources (the checkpoint sections' names); the largest source is a whole run — None where the database is not built"""
    if not _os.path.exists(_WDB): return None
    c_ = sqlite3.connect('file:%s?mode=ro' % _WDB, uri=True)
    src = c_.execute("SELECT source FROM run_ledger GROUP BY source ORDER BY COUNT(*) DESC, source LIMIT 1").fetchone()[0]
    return c_.execute("SELECT COUNT(*) FROM run_ledger WHERE effect=? AND source=?", (effect, src)).fetchone()[0]
OWN42 = %(OWN42)r
assert len(OWN42) == 42 and len(set(OWN42)) == 42
HOLE_WORDS = r"%(HOLE_WORDS)s"
_hs = {ent: ledger_scan(ent, HOLE_WORDS) for ent in ('israel_people', 'yehoshua', 'moses')}; HOLE_SCAN = None if any(v is None for v in _hs.values()) else {ent: [e for e in v if e not in OWN42] for ent, v in _hs.items()}   # this sitting's own names excluded once the fold carries them
KIN62 = %(KIN62)r
KIN_EXPECTED = %(KIN_EXPECTED)r   # DN4 — the recon's and the callees' counts on the running world (ch32b_recon.out section H; ch32_callees.out THE NEAR NAMES; the probe Q49's KIN tuple)
assert len(KIN62) == 62 == len(KIN_EXPECTED)
KIN_COUNTS = {k: count_scan(k) for k in KIN62}
REUSE3 = ('heaven_and_earth_witness', 'face_hidden_and_forsaken_foretold', 'length_of_days_on_the_land_promised')
REUSE_BEFORE = %(REUSE_BEFORE)r   # the reuses' counts BEFORE this sitting's lines (the recon) — after the fold carries the new entries the count is the after (the tape's second run reads it so)
REUSE_AFTER = %(REUSE_AFTER)r
REUSE_COUNTS = {k: count_scan(k) for k in REUSE3}
SCANS = {k: effect_scan(k) for k in KIN62[:8] + REUSE3 + ('garments_transferred_and_aaron_died', 'invested_office', 'song_spoken_to_the_assembly_to_its_end', 'treasured_people')}
del _hs   # 9b's lesson: the raw scans are the database's state at import — the derived lists are equal on the cached and the full load
_FXV = yaml.safe_load(open(_os.path.join(HERE, 'effect_vocabulary.yaml'), encoding='utf-8'))['effects']
print('THE SCANS (printed before they are asserted): holes %%s; the kin counts %%s; the reuses %%s; the entities %%s' %% (HOLE_SCAN, KIN_COUNTS, REUSE_COUNTS, SCANS))
assert HOLE_SCAN is None or all(v == [] for v in HOLE_SCAN.values()), HOLE_SCAN   # THE HOLES' GROUND — nothing on the three ledgers named the forty-two before this sitting (DN4)
assert all(v is None for v in KIN_COUNTS.values()) or tuple(KIN_COUNTS.values()) == KIN_EXPECTED, [(k, KIN_COUNTS[k], e) for k, e in zip(KIN62, KIN_EXPECTED) if KIN_COUNTS[k] != e]   # the references' counts as the recon read them (DN4 — no second write)
assert all(v is None for v in REUSE_COUNTS.values()) or all(REUSE_COUNTS[k] in (REUSE_BEFORE[k], REUSE_AFTER[k]) for k in REUSE3), REUSE_COUNTS   # the reuses' counts the before (the first run) or the after (the fold carrying this sitting's lines)
SCANS_EXPECTED = _SCANS_EXPECTED_   # the entities per effect — typed from the first derive's print (the callees' way — printed before typed)
if SCANS_EXPECTED and any(v is not None for v in SCANS.values()): assert SCANS == SCANS_EXPECTED, [(k, SCANS[k], SCANS_EXPECTED.get(k)) for k in SCANS if SCANS[k] != SCANS_EXPECTED.get(k)]
assert all(k in _FXV for k in OWN42) and sum(1 for k in OWN42 if _FXV[k]['ledger_op'] == 'block') == 0 and sum(1 for k in OWN42 if _FXV[k]['ledger_op'] == 'status') == 32 and sum(1 for k in OWN42 if _FXV[k]['ledger_op'] == 'heaven') == 10, 'the forty-two on the registry (add_types_ch32_a.py)'
assert _FXV['heaven_and_earth_witness']['ledger_op'] == 'status' and _FXV['face_hidden_and_forsaken_foretold']['ledger_op'] == 'heaven' and _FXV['length_of_days_on_the_land_promised']['ledger_op'] == 'heaven' and _FXV['barred_from_the_land']['ledger_op'] == 'heaven' and _FXV['gathered_to_his_people']['ledger_op'] == 'status' and _FXV['treasured_people']['ledger_op'] == 'heaven' and _FXV['other_gods_barred']['ledger_op'] == 'block', 'the reused and referenced rows\\' ops (read from the registry\\'s print at the types)'
# THE TWINS DIFFED on the DB (the reading's kin asserts read again here — DN4; the shared run SH)
TWIN = {'32:36 vs Ps 135:14': SH(DV(32, 36), ('Ps', 135, 14)), '32:49 vs Num 27:12': SH(DV(32, 49), ('Num', 27, 12)), '32:45 vs 31:1': SH(DV(32, 45), DV(31, 1)), '32:46 vs 31:12': SH(DV(32, 46), DV(31, 12)), '32:47 vs 11:9': SH(DV(32, 47), DV(11, 9)),
        '32:48 vs Gen 7:13': SH(DV(32, 48), ('Gen', 7, 13)), '32:48 vs Exod 12:41': SH(DV(32, 48), ('Exod', 12, 41)), '32:44 vs 31:30': SH(DV(32, 44), DV(31, 30)), '32:44 vs Num 13:16': SH(DV(32, 44), ('Num', 13, 16)), '32:51 vs Num 27:14': SH(DV(32, 51), ('Num', 27, 14)),
        '32:51 vs Num 20:12': SH(DV(32, 51), ('Num', 20, 12)), '32:50 vs Num 20:28': SH(DV(32, 50), ('Num', 20, 28)), '32:1 vs 31:28': SH(DV(32, 1), DV(31, 28)), '32:1 vs 4:26': SH(DV(32, 1), DV(4, 26)), '32:1 vs Isa 1:2': SH(DV(32, 1), ('Isa', 1, 2)), '32:11 vs Exod 19:4': SH(DV(32, 11), ('Exod', 19, 4)),
        '32:15 vs 31:20': SH(DV(32, 15), DV(31, 20)), '32:20 vs 31:17': SH(DV(32, 20), DV(31, 17)), '32:17 vs 29:25': SH(DV(32, 17), DV(29, 25)), '32:8 vs Gen 11:8': SH(DV(32, 8), ('Gen', 11, 8)), '32:24 vs Lev 26:22': SH(DV(32, 24), ('Lev', 26, 22)), '32:30 vs Lev 26:8': SH(DV(32, 30), ('Lev', 26, 8)),
        '32:30 vs Josh 23:10': SH(DV(32, 30), ('Josh', 23, 10)), '32:32 vs 29:22': SH(DV(32, 32), DV(29, 22)), '32:39 vs 6:4': SH(DV(32, 39), DV(6, 4)), '32:43 vs Num 35:33': SH(DV(32, 43), ('Num', 35, 33)), '32:52 vs 34:4': SH(DV(32, 52), DV(34, 4)), '32:49 vs 3:27': SH(DV(32, 49), DV(3, 27)), '32:13 vs 8:15': SH(DV(32, 13), DV(8, 15)),
        '32:21 vs 28:49': SH(DV(32, 21), DV(28, 49)), '32:27 vs 9:28': SH(DV(32, 27), DV(9, 28)), '32:12 vs Num 23:9': SH(DV(32, 12), ('Num', 23, 9)), '32:6 vs Exod 15:16': SH(DV(32, 6), ('Exod', 15, 16))}
print('THE TWINS DIFFED (printed before they are asserted):', TWIN)
TWIN_EXPECTED = _TWIN_EXPECTED_
if TWIN_EXPECTED: assert TWIN == TWIN_EXPECTED, [(k, TWIN[k], TWIN_EXPECTED.get(k)) for k in TWIN if TWIN[k] != TWIN_EXPECTED.get(k)]   # typed from the first derive's print (the callees' way — printed before typed)
assert TWIN['32:36 vs Ps 135:14'] >= 7 and TWIN['32:49 vs Num 27:12'] >= 5 and TWIN['32:46 vs 31:12'] >= 6 and TWIN['32:47 vs 11:9'] >= 5, TWIN   # the reading's largest twins (Psalm 135:14 seven in order, the summons five, the charge six, the length of days five)
'''
for _k, _v in (('%(OWN42)r', repr(OWN42)), ('%(HOLE_WORDS)s', HOLE_WORDS), ('%(KIN62)r', repr(KIN62)), ('%(KIN_EXPECTED)r', repr(KIN_EXPECTED)), ('%(REUSE_BEFORE)r', repr(S.REUSE_BEFORE)), ('%(REUSE_AFTER)r', repr(S.REUSE_AFTER))): TAIL_B = TAIL_B.replace(_k, _v)
TAIL_B = TAIL_B.replace('%%', '%')   # the print's own %s escaped inside the template
def _read(name):
    p = f'{SP}/{name}'; return open(p).read().strip() if os.path.exists(p) else 'None'
TWIN_EXPECTED = _read('ch32_twin_expected.txt'); SCANS_EXPECTED = _read('ch32_scans_expected.txt'); TOKN_EXPECTED = _read('ch32_tokn_expected.txt'); NAME_BARE_EXPECTED = _read('ch32_name_bare_expected.txt'); NEG_EXPECTED = _read('ch32_neg_expected.txt')   # the first derive's prints, parsed by ast from the fast checker's output and written to the files — never typed by hand
# THE GLOSS TABLE — the store's own glosses for the chapter's tokens (ch32_store_glosses.txt, the reading's print), a small table for the tokens of other verses the copied asserts name
GLOSS = {}
for _l in open(f'{SP}/ch32_store_glosses.txt', encoding='utf-8'):
    for _i, _tok, _g in ast.literal_eval(_l.split(': ', 1)[1]):
        GLOSS.setdefault(_tok, _g.replace('-', ' ').replace('/', ' or ').replace("'", '').replace('"', ''))   # the store's apostrophes dropped (a quoted gloss inside a quoted token)
GLOSS.update({'וצור': 'and a rock', 'צורנו': 'our rock', 'צר': 'a foe', 'הושע': 'Hoshea', 'ונקם': 'and vengeance', 'נקם': 'vengeance', 'לאמר': 'saying', 'ידעום': 'they knew them', 'הדברים': 'the words',
              'את': 'the object marker', 'ואת': 'and-it', 'כל': 'all', 'על': 'on', 'אל': 'to', 'לא': 'not', 'ולא': 'and not', 'כי': 'for', 'אם': 'if', 'פן': 'lest', 'יהוה': 'the LORD', 'ליהוה': 'to the LORD', 'ויהוה': 'and the LORD', 'ביהוה': 'in the LORD', 'מיהוה': 'from the LORD',
              'אלהיך': 'your God', 'תבוא': 'you shall go', 'אחד': 'one', 'שמנת': 'you grew fat', 'ירדף': 'chase', 'אלף': 'a thousand', 'ושנים': 'and two', 'יניסו': 'put to flight', 'רבבה': 'ten thousand', 'וישמן': 'and grew fat', 'ישרון': 'Jeshurun', 'ויבעט': 'and kicked', 'עבית': 'you grew thick', 'כשית': 'you became gross', 'ביד': 'by the hand of', 'ועמרה': 'and Gomorrah', 'ראש': 'gall, the head', 'שאול': 'Sheol'})
MISSING = []
def glossify(text):
    def repl(m):
        tok = m.group(1); key = tok.rstrip('*%|')
        if key not in GLOSS: MISSING.append(tok); return m.group(0)
        return "_G('%s (%s)')" % (tok, GLOSS[key])
    out_ = []
    for l in text.split('\n'):
        if l.lstrip().startswith('#') or 'STOP = set((' in l or l.lstrip().startswith("'") and '   # (' in l: out_.append(l); continue   # the comments and the glossed STOP set kept
        out_.append(re.sub(r"'([א-תװ-״]+[*%|]?)'", repl, l))
    return '\n'.join(out_)
TAIL_A = glossify(TAIL_A); ink_block = glossify(ink_block)
assert not MISSING, ('a Hebrew token without a gloss in the table', sorted(set(MISSING)))
src = HEAD + helpers + TAIL_A.replace('_TOKN_EXPECTED_', TOKN_EXPECTED).replace('_NAME_BARE_EXPECTED_', NAME_BARE_EXPECTED).replace('_NEG_EXPECTED_', NEG_EXPECTED) + ink_block + TAIL_B.replace('_TWIN_EXPECTED_', TWIN_EXPECTED).replace('_SCANS_EXPECTED_', SCANS_EXPECTED) + FACTS
open(f'{SP}/ch32_part1.py', 'w', encoding='utf-8').write(src)
import py_compile; py_compile.compile(f'{SP}/ch32_part1.py', doraise=True)
lint = subprocess.run([sys.executable, f'{ROOT}/logic/solo_tools/gloss_lint.py', f'{SP}/ch32_part1.py'], capture_output=True, text=True).stdout.strip().split('\n')[-1]; print('the lint on part 1:', lint); assert lint.endswith('0 flag(s)'), lint
print('part1 derived: %d bytes; helpers %d, ink block %d (asserts %d); dropped %d store-bound lines; the callees\' facts %d bytes; TWIN_EXPECTED %s; SCANS_EXPECTED %s; TOKN %s; NAME_BARE %s; NEG %s' % (len(src), len(helpers), len(ink_block), n_as, len(drop), len(FACTS), TWIN_EXPECTED[:40], SCANS_EXPECTED[:40], TOKN_EXPECTED, NAME_BARE_EXPECTED, NEG_EXPECTED[:40]))

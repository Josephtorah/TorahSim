#!/usr/bin/env python3
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

HERE = _os.path.dirname(_os.path.abspath(__file__))
# ONE copy of the numeral parser: the sequence runner's INK block executed here (the stitcher's way — no import edge)
_SRC = open(_os.path.join(HERE, 'cold_run_sequence.py'), encoding='utf-8').read()
_INK = {'re': re, 'sqlite3': sqlite3, 'os': _os, 'WE': WE}
_INK['_ROOT'] = _ROOT   # THE PORTABLE REPO (2026-09-15): the INK block reads the store through the root; the exec'd namespace must carry it
exec(_SRC.split('# ==== INK BEGIN')[1].split('# ==== INK END ====')[0].split('\n', 1)[1], _INK)
ink_numbers, ink_ordinals, verse_words = _INK['ink_numbers'], _INK['ink_ordinals'], _INK['verse_words']

db = sqlite3.connect((_ROOT + '/Data/tanakh.sqlite'))
def plain(w): return ''.join(c for c in w if c != '/' and not (0x0591 <= ord(c) <= 0x05C7))
def pointed(w): return ''.join(c for c in w if c != '/' and not (0x0591 <= ord(c) <= 0x05AF))
def NF(s): return unicodedata.normalize('NFC', s)
_rows = db.execute("SELECT v.book, v.chapter, v.verse, w.he, w.morph, w.lemma, w.wtype FROM words w JOIN verses v ON w.verse_id=v.id ORDER BY v.id, w.idx").fetchall()
by, byp, byl, byw, byraw = {}, {}, {}, {}, {}
for _b, _c, _v, _he, _m, _lem, _wt in _rows:
    by.setdefault((_b, _c, _v), []).append((plain(_he), _m)); byp.setdefault((_b, _c, _v), []).append(pointed(_he)); byl.setdefault((_b, _c, _v), []).append((_lem or '').split('/')[-1].strip()); byw.setdefault((_b, _c, _v), []).append(_wt); byraw.setdefault((_b, _c, _v), []).append(_lem or '')
T = ('Gen', 'Exod', 'Lev', 'Num', 'Deut')
def words(b, c, v): return [x for x, _ in by[(b, c, v)]]
def morphs(b, c, v): return [m for _, m in by[(b, c, v)]]
def wm(b, c, v): return list(zip(words(b, c, v), morphs(b, c, v)))
def hits(sub, books=None, exact=False): return sorted({f'{b} {c}:{v}' for (b, c, v), ws in by.items() if (books is None or b in books) and any((x == sub) if exact else (sub in x) for x, _ in ws)})
def phrase(seq, books=T):
    out_ = []
    for (b, c, v), ws in by.items():
        if books is not None and b not in books: continue
        w = [x for x, _ in ws]
        if any(w[i:i + len(seq)] == list(seq) for i in range(len(w) - len(seq) + 1)): out_.append(f'{b} {c}:{v}')
    return sorted(out_)
def P(*seq, books=None): return phrase(list(seq), books)
def S_(*x): return sorted(x)
def U(*toks, books=None): return sorted(set(s for t in toks for s in hits(t, books, True)))
def LEMT(lem, books=None): return [(f'{b} {c}:{v}', x, m) for (b, c, v), ws in by.items() if (books is None or b in books) for (x, m), l in zip(ws, byl[(b, c, v)]) if l == lem]
def LEMV(lem, books=None): return sorted({s for s, _, _ in LEMT(lem, books)})
def lemma_of(b, c, v, tok): return [l for (x, m), l in zip(by[(b, c, v)], byl[(b, c, v)]) if x == tok]
def W32(v): return words('Deut', 32, v)
def W(c, v): return words('Deut', c, v)
def PT(b, c, v, tok): return [NF(x) for x in byp[(b, c, v)] if plain(x) == tok]
def SEAT(s): b, cv = s.split(); c, v = map(int, cv.split(':')); return (b, c, v)
def DIFF(a, b_):
    import difflib
    A, B = words(*a), words(*b_)
    return [(op, A[i1:i2], B[j1:j2]) for op, i1, i2, j1, j2 in difflib.SequenceMatcher(None, A, B).get_opcodes() if op != 'equal']
def SHARED(a, b_):
    import difflib
    A, B = words(*a), words(*b_)
    m = difflib.SequenceMatcher(None, A, B).find_longest_match(0, len(A), 0, len(B))
    return A[m.a:m.a + m.size]
def SHN(a, b_):
    import difflib
    A, B = words(*a), words(*b_)
    return sum(i2 - i1 for op, i1, i2, j1, j2 in difflib.SequenceMatcher(None, A, B).get_opcodes() if op == 'equal')
def LEN(b, c, v): return len(words(b, c, v))
def verse_text(ch, vs, book='Deut'): return ' '.join(words(book, ch, vs))
def _G(s): return s.split(' (')[0]   # a Hebrew token typed WITH ITS GLOSS beside it — the token alone returned (the lint's ninety-character window; 18b's form for the copied ink asserts)
DV = lambda c, v: ('Deut', c, v)
NEG_T = (_G('לא (not)'), _G('ולא (and not)'))   # (not; and not)
NAME = (_G('יהוה (the LORD)'), _G('ליהוה (to the LORD)'), _G('ויהוה (and the LORD)'), _G('ביהוה (in the LORD)'), _G('מיהוה (from the LORD)'))   # (the LORD; to the LORD; and the LORD; in the LORD; from the LORD)
import difflib
def SH(a, b_): return sum(s for _, _, s in difflib.SequenceMatcher(a=words(*a), b=words(*b_)).get_matching_blocks())   # the reading's shared-run measure
CHS = (32,)
NV = {c: len({v for (b, cc, v) in by if b == 'Deut' and cc == c}) for c in CHS}; assert NV == {32: 52}, NV   # fifty-two verses (the reading's divisions assert — the identity)
TOKN = {c: sum(len(W(c, v)) for v in range(1, NV[c] + 1)) for c in CHS}
print('THE TOKENS (printed before they are asserted):', TOKN)
TOKN_EXPECTED = {32: 615}   # typed from the first derive's print (the callees' way — printed before typed)
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
assert {k: p for k, p in PARSE.items() if p[0] or p[1] or p[2]} == {(32, 15): ([8], [], []), (32, 30): ([1, 1002], [], [_G('אחד| (one)')])}, {k: p for k, p in PARSE.items() if p[0] or p[1] or p[2]}   # the reading's parser assert (ch32_ink.py from ch32_measure_lean.out): 32:15 THE FALSE EIGHT (you grew fat), 32:30 THE JOINED THOUSAND (one chase a thousand, and two — [1, 1002] with 'one' marked)
assert NUMV == [(32, 15), (32, 30)] and ORDV == [] and STARV == [(32, 30)]
FALSE_EIGHT = W(32, 15)[3]; assert FALSE_EIGHT == _G('שמנת (you grew fat)') and W(32, 15)[0:3] == [_G('וישמן (and grew fat)'), _G('ישרון (Jeshurun)'), _G('ויבעט (and kicked)')] and W(32, 15)[4:6] == [_G('עבית (you grew thick)'), _G('כשית (you became gross)')]   # (you grew fat — the eight's consonants, a verb: and Jeshurun grew fat and kicked; you grew thick, you became gross) — the guard on the parser's false hit
JOINED = W(32, 30)[1:7]; assert JOINED == [_G('ירדף (chase)'), _G('אחד (one)'), _G('אלף (a thousand)'), _G('ושנים (and two)'), _G('יניסו (put to flight)'), _G('רבבה (ten thousand)')]   # (chase; one; a thousand; and two; put to flight; ten thousand) — the four numbers the Sifrei 322:10 reads aloud, the parser's [1, 1002] a proverb, no count
NEG = {(c, v): [x for x in W(c, v) if x in NEG_T] for (c, v) in SPAN if any(x in NEG_T for x in W(c, v))}
NAME_BARE = sum(1 for (c, v) in SPAN for x in W(c, v) if x == _G('יהוה (the LORD)'))   # (the LORD)
print('THE NEGATIONS AND THE NAME (printed before they are asserted):', NEG, NAME_BARE)
NAME_BARE_EXPECTED = 7   # typed from the first derive's print
if NAME_BARE_EXPECTED: assert NAME_BARE == NAME_BARE_EXPECTED, (NAME_BARE, NAME_BARE_EXPECTED)
NEG_EXPECTED = {'32:5': 1, '32:6': 1, '32:17': 3, '32:20': 1, '32:27': 1, '32:30': 1, '32:31': 1, '32:47': 1, '32:51': 1, '32:52': 1}   # the negations per verse, typed from the first derive's print
if NEG_EXPECTED: assert {'%d:%d' % k: len(v) for k, v in NEG.items()} == NEG_EXPECTED, {'%d:%d' % k: len(v) for k, v in NEG.items()}
assert [f'{c}:{v}' for c, v in SPAN if _G('לאמר (saying)') in W(c, v)] == ['32:48'] and [(c, v) for c, v in SPAN if _G('אם (if)') in W(c, v)] == [(32, 30), (32, 41)] and [(c, v, x) for c, v in SPAN for x in W(c, v) if x == _G('פן (lest)')] == [(32, 27, _G('פן (lest)')), (32, 27, _G('פן (lest)'))] and [(c, v) for c, v in SPAN if _G('לא (not)') in W(c, v) and _G('תבוא (you shall go)') in W(c, v)] == [(32, 52)]   # ("saying" — the one divine frame at 32:48; "if" — the joined thousand's and the sword's; "lest" — the enemy's boast twice; "you shall not go" — the chapter's close) — the reading's frames assert
# THE KIN FOUND BY COMPUTATION (the measure's A section, recomputed here so the asserts read the same instrument): the shared distinct tokens outside the stop list, the top eight, the three closest re-scored in order — keyed by (chapter, verse)
STOP = set(('את ואת אשר כל וכל על ועל אל ואל '   # (the object marker, and-it, which, all, on, to — the particles)
            'לא ולא כי אם יהוה אלהיך אלהיכם '   # (not, for, if; the LORD, your God)
            'לך לכם בו שם שמה גם מן ממך עד '   # (to you, in it, there, also, from, until)
            'הוא היא אתם אתה אנכי אני לו לה '   # (he, she, you, I, to him, to her)
            'בכל כאשר כן הימים היום אלה האלה '   # (in all, as, so, the days, today, these)
            'בארץ הארץ אשר ואם או פן ופן '   # (in the land, the land, which, and if, or, lest)
            'ואת זה וזה הם המה').split())   # (and-it, this, and this, they, they) — the stopword set glossed piece by piece (the lint's ninety-character window)
ORD = {k: i for i, k in enumerate(by)}
TOK = {k: set(words(*k)) - STOP for k in by}
KINC = {}
for _c, _v in SPAN:
    _me = DV(_c, _v); _t = TOK[_me]
    _sc = sorted(((len(_t & TOK[k]), k) for k in by if k != _me and len(_t & TOK[k]) >= 2), key=lambda x: (-x[0], ORD[x[1]]))[:8]
    KINC[(_c, _v)] = [(f'{k[0]} {k[1]}:{k[2]}', n, SH(_me, k) if i < 3 else None) for i, (n, k) in enumerate(_sc)]
# THE KIN BY COMPUTATION: THE SONG'S VOCABULARY IS ITS OWN — eleven verses share no two tokens outside the stop list with any verse of the Bible (32:3, 5, 10, 16, 18, 26, 29, 31, 33, 34, 37); 32:36 quoted whole in Psalm 135:14 (seven in order); the frame's kin 31:30, 31:1, 31:12, 11:9, Numbers 27:12 and 27:14, 34:1, 34:4; 32:30's Joshua 23:10 (the Prophets' seat cited, never read)
assert [v for c, v in SPAN if not KINC[(c, v)]] == [3, 5, 10, 16, 18, 26, 29, 31, 33, 34, 37], [v for c, v in SPAN if not KINC[(c, v)]]
assert KINC[(32, 36)][0] == ('Ps 135:14', 4, 7) and KINC[(32, 44)][0] == ('Deut 31:30', 6, 5) and KINC[(32, 45)][0] == ('Deut 1:1', 3, 4) and KINC[(32, 46)][0] == ('Deut 17:19', 4, 7) and KINC[(32, 47)][0] == ('Josh 1:11', 5, 7) and KINC[(32, 48)][0] == ('Deut 27:9', 4, 4) and KINC[(32, 49)][0] == ('Num 27:12', 7, 10) and KINC[(32, 51)][0] == ('Num 20:1', 4, 4) and KINC[(32, 52)][0] == ('Deut 32:49', 3, 6) and KINC[(32, 30)][0] == ('Josh 23:10', 3, 3) and KINC[(32, 1)][1] == ('Deut 31:28', 2, 2) and KINC[(32, 17)][2] == ('Deut 29:25', 2, 3), (KINC[(32, 36)][0], KINC[(32, 49)][0], KINC[(32, 1)])
# THE TWINS DIFFED (shared / the longest run): the whole of 32:36 in Psalm 135:14; the summons to Nebo 32:49 against Numbers 27:12 ten shared, five in order; the frame 32:45 against 31:1, 32:46 against 31:12 six in order, 32:47 against 11:9 five; the selfsame day 32:48 against Genesis 7:13 and Exodus 12:17; 32:17's 'gods they knew not' 29:25's; 32:20's hidden face 31:17's; the song at 32:1 shares NOTHING with Isaiah 1:2's call to heaven and earth, 32:15 nothing with 31:20's satiety, 32:24 nothing with Leviticus 26:22's beasts — the kin is by sense, not by token
assert SHARED(('Deut', 32, 36), ('Ps', 135, 14)) == [_G('כי (for)'), _G('ידין (straight course)'), _G('יהוה (the LORD)'), _G('עמו (people him or its)'), _G('ועל (and over)'), _G('עבדיו (servant him or its)'), _G('יתנחם (sigh)')] and SHARED(('Deut', 32, 49), ('Num', 27, 12)) == [_G('עלה (go up)'), _G('אל (to)'), _G('הר (mountain)'), _G('העברים (the Abarim)'), _G('הזה (the this)')] and SHN(('Deut', 32, 49), ('Num', 27, 12)) == 10 and SHARED(('Deut', 32, 45), ('Deut', 31, 1)) == [_G('הדברים (the words)'), _G('האלה (the these)'), _G('אל (to)'), _G('כל (all)'), _G('ישראל (Israel)')] and SHARED(('Deut', 32, 46), ('Deut', 31, 12)) == [_G('לעשות (to make)'), _G('את (the object marker)'), _G('כל (all)'), _G('דברי (word or thing)'), _G('התורה (the precept)'), _G('הזאת (the this)')] and SHARED(('Deut', 32, 47), ('Deut', 11, 9)) == [_G('תאריכו (be  long)'), _G('ימים (day)'), _G('על (on)'), _G('האדמה (the ground)'), _G('אשר (which)')] and SHARED(('Deut', 32, 48), ('Gen', 7, 13)) == [_G('בעצם (in bone)'), _G('היום (the day)'), _G('הזה (the this)')] and SHARED(('Deut', 32, 48), ('Exod', 12, 17)) == [_G('בעצם (in bone)'), _G('היום (the day)'), _G('הזה (the this)')]
assert SHARED(('Deut', 32, 44), ('Deut', 31, 30)) == [_G('דברי (word or thing)'), _G('השירה (the song)'), _G('הזאת (the this)')] and SHARED(('Deut', 32, 44), ('Num', 13, 16)) == [_G('בן (son)'), _G('נון (Non)')] and SHARED(('Deut', 32, 51), ('Num', 27, 14)) == [_G('מריבת (quarrel)'), _G('קדש (Kadesh)'), _G('מדבר (pasture)'), _G('צן (Zin)')] and SHARED(('Deut', 32, 17), ('Deut', 29, 25)) == [_G('לא (not)'), _G('ידעום (they knew them)')] and SHARED(('Deut', 32, 20), ('Deut', 31, 17)) == [_G('פני (face me or my)'), _G('מהם (from them or their)')] and SHARED(('Deut', 32, 27), ('Deut', 9, 28)) == [_G('פן (lest)'), _G('יאמרו (say)')] and SHARED(('Deut', 32, 52), ('Deut', 34, 4)) == [_G('ושמה (and there suffix)'), _G('לא (not)')] and SHARED(('Deut', 32, 50), ('Num', 27, 13)) == [_G('אל (to)'), _G('עמיך (people you or your)')] and SHN(('Deut', 32, 1), ('Isa', 1, 2)) == 0 and SHN(('Deut', 32, 15), ('Deut', 31, 20)) == 0 and SHN(('Deut', 32, 24), ('Lev', 26, 22)) == 0 and SHN(('Deut', 32, 8), ('Gen', 11, 8)) == 0 and SHN(('Deut', 32, 11), ('Exod', 19, 4)) == 1
# THE FORMULAS (phrase seats by consonants over the Torah and the Bible): twenty phrases of the song ONCE in the Bible; the Rock four in the Torah; 'as an eagle' once in the Torah, eleven in the Bible; 'the selfsame day' eleven in the Torah; the Abarim and Nebo twice each; Meribath-kadesh thrice (Ezekiel 48:28 beside); 'this song' seven; 'set your heart' Haggai's thrice beside; 'prolong days' 11:9 and 32:47
assert P(_G('האזינו (broaden out the ear)'), _G('השמים (the heavens)'), books=None) == ['Deut 32:1'] and P(_G('ותשמע (and hear)'), _G('הארץ (the earth)'), books=None) == ['Deut 32:1'] and P(_G('דור (generation)'), _G('עקש (distorted)'), _G('ופתלתל (and tortuous)'), books=None) == ['Deut 32:5'] and P(_G('כאישון (like little man of the eye)'), _G('עינו (eye him or its)'), books=None) == ['Deut 32:10'] and P(_G('דבש (honey)'), _G('מסלע (from craggy rock)'), books=None) == ['Deut 32:13'] and P(_G('ישרון (Jeshurun)'), books=None) == ['Deut 32:15', 'Deut 33:26'] and P(_G('אסתירה (hide)'), _G('פני (face me or my)'), books=None) == ['Deut 32:20'] and P(_G('נקם (vengeance)'), _G('ושלם (and requital)'), books=None) == ['Deut 32:35'] and P(_G('לי (to me or my)'), _G('נקם (vengeance)'), books=None) == ['Deut 32:35'] and P(_G('אמית (die)'), _G('ואחיה (and live)'), books=None) == ['Deut 32:39'] and P(_G('אשא (lift or carry)'), _G('אל (to)'), _G('שמים (heavens)'), _G('ידי (hand me or my)'), books=None) == ['Deut 32:40'] and P(_G('ואין (and there is not)'), _G('אלהים (God)'), _G('עמדי (along with me or my)'), books=None) == ['Deut 32:39']
assert P(_G('אלהים (God)'), _G('לא (not)'), _G('ידעום (they knew them)'), books=None) == ['Deut 32:17'] and P(_G('ימות (day)'), _G('עולם (forever)'), books=None) == ['Deut 32:7'] and P(_G('הוא (he or it)'), _G('חייכם (alive you or your (pl))'), books=None) == ['Deut 32:47'] and P(_G('למספר (to number)'), _G('בני (son)'), _G('ישראל (Israel)'), books=None) == ['Deut 32:8'] and P(_G('גוי (nation)'), _G('אבד (wander away)'), _G('עצות (advice)'), books=None) == ['Deut 32:28'] and P(_G('ושמה (and there suffix)'), _G('לא (not)'), _G('תבוא (you shall go)'), books=None) == ['Deut 32:52'] and P(_G('והאסף (and gather for any purpose)'), _G('אל (to)'), _G('עמיך (people you or your)'), books=None) == ['Deut 32:50'] and P(_G('כאשר (like as or which)'), _G('מת (die)'), _G('אהרן (Aaron)'), _G('אחיך (brother you or your)'), books=None) == ['Deut 32:50'] and P(_G('מחוץ (from outside)'), _G('תשכל (miscarry)'), _G('חרב (drought)'), books=None) == ['Deut 32:25']
assert P(_G('הצור (the cliff)'), books=T) == ['Deut 32:4', 'Exod 17:6', 'Exod 33:21', 'Exod 33:22'] and len(P(_G('הצור (the cliff)'), books=None)) == 8 and P(_G('כנשר (like eagle)'), books=T) == ['Deut 32:11'] and len(P(_G('כנשר (like eagle)'), books=None)) == 11 and len(P(_G('בעצם (in bone)'), _G('היום (the day)'), _G('הזה (the this)'), books=T)) == 11 and len(P(_G('בעצם (in bone)'), _G('היום (the day)'), _G('הזה (the this)'), books=None)) == 14 and P(_G('הר (mountain)'), _G('העברים (the Abarim)'), books=None) == ['Deut 32:49', 'Num 27:12'] and P(_G('הר (mountain)'), _G('נבו (Nebo)'), books=None) == ['Deut 32:49', 'Deut 34:1'] and P(_G('מריבת (quarrel)'), _G('קדש (Kadesh)'), books=None) == ['Deut 32:51', 'Ezek 48:28', 'Num 27:14'] and P(_G('השירה (the song)'), _G('הזאת (the this)'), books=T) == ['Deut 31:19', 'Deut 31:21', 'Deut 31:22', 'Deut 31:30', 'Deut 32:44', 'Exod 15:1', 'Num 21:17'] and len(P(_G('השירה (the song)'), _G('הזאת (the this)'), books=None)) == 9
assert P(_G('שימו (put or set)'), _G('לבבכם (heart you or your (pl))'), books=None) == ['Deut 32:46', 'Hag 1:5', 'Hag 1:7', 'Hag 2:18'] and P(_G('תאריכו (be  long)'), _G('ימים (day)'), books=None) == ['Deut 11:9', 'Deut 32:47'] and P(_G('עשהו (make him or its)'), books=T) == ['Deut 32:15', 'Exod 18:18'] and P(_G('באזני (in broadness. i.e.  the ear)'), _G('העם (the people)'), books=T) == ['Deut 32:44', 'Exod 11:2', 'Exod 24:7'] and len(P(_G('עליון (elevation)'), books=T)) == 8 and len(P(_G('עליון (elevation)'), books=None)) == 32 and len(P(_G('ביד (by the hand of)'), _G('משה (Moses)'), books=T)) == 16 and len(P(_G('ביד (by the hand of)'), _G('משה (Moses)'), books=None)) == 31 and P(_G('ראש (gall, the head)'), _G('פתנים (asp)'), books=None) == ['Job 20:16'] and P(_G('סדם (Sodom)'), _G('ועמרה (and Gomorrah)'), books=T) == ['Deut 29:22', 'Gen 14:10', 'Gen 14:11', 'Gen 18:20', 'Gen 19:28'] and P(_G('דם (blood  of man)'), _G('ענב (grape)'), books=None) == []
# THE WORDS: eight 'rock' words (the Rock at 32:4 with the article; their Rock 32:30, 32:31 twice; the rock's honey 32:13); the Name seven bare, once with lamed (32:6), once with vav (32:30); the names Bashan, Jeshurun, Sheol, HOSHEA (32:44 — the old name), Nebo, Meribah; vengeance thrice (32:35, 41, 43); the Most High 32:8; Eloah 32:15; the negations twelve; 'for/when' nineteen; 'if' 32:30 and 32:41; 'lest' 32:27; 'saying' 32:48 alone
assert [(v, x) for c, v in SPAN for x in W(c, v) if x in (_G('צור (cliff)'), _G('הצור (the cliff)'), _G('צורם (cliff them or their)'), _G('וצור (and a rock)'), _G('צורנו (our rock)'), _G('כצורנו (like cliff us or our)'), _G('צר (a foe)'))] == [(4, _G('הצור (the cliff)')), (13, _G('צור (cliff)')), (15, _G('צור (cliff)')), (18, _G('צור (cliff)')), (30, _G('צורם (cliff them or their)')), (31, _G('כצורנו (like cliff us or our)')), (31, _G('צורם (cliff them or their)')), (37, _G('צור (cliff)'))] and [(v, x) for c, v in SPAN for x in W(c, v) if x in (_G('יהוה (the LORD)'), _G('ליהוה (to the LORD)'), _G('ויהוה (and the LORD)'))] == [(3, _G('יהוה (the LORD)')), (6, _G('ליהוה (to the LORD)')), (9, _G('יהוה (the LORD)')), (12, _G('יהוה (the LORD)')), (19, _G('יהוה (the LORD)')), (27, _G('יהוה (the LORD)')), (30, _G('ויהוה (and the LORD)')), (36, _G('יהוה (the LORD)')), (48, _G('יהוה (the LORD)'))]
assert [(v, x) for c, v in SPAN for x in W(c, v) if x in (_G('שאול (Sheol)'), _G('ישרון (Jeshurun)'), _G('בשן (Bashan)'), _G('והושע (and Hosea)'), _G('הושע (Hoshea)'), _G('נבו (Nebo)'), _G('מריבת (quarrel)'))] == [(14, _G('בשן (Bashan)')), (15, _G('ישרון (Jeshurun)')), (22, _G('שאול (Sheol)')), (44, _G('והושע (and Hosea)')), (49, _G('נבו (Nebo)')), (51, _G('מריבת (quarrel)'))] and [(v, x) for c, v in SPAN for x in W(c, v) if x.startswith((_G('נקם (vengeance)'), _G('ונקם (and vengeance)')))] == [(35, _G('נקם (vengeance)')), (41, _G('נקם (vengeance)')), (43, _G('ונקם (and vengeance)'))] and [v for c, v in SPAN for x in W(c, v) if x == _G('עליון (elevation)')] == [8] and _G('אלוה (deity)') in W(32, 15) and sum(1 for c, v in SPAN for x in W(c, v) if x in (_G('לא (not)'), _G('ולא (and not)'))) == 12 and sum(1 for c, v in SPAN for x in W(c, v) if x == _G('כי (for)')) == 19
# THE FRAMES, THE REGISTER AND THE PARSER: twelve imperatives (give ear 32:1; ascribe 32:3; remember, consider, ask 32:7; see 32:39; sing 32:43; set 32:46; go up, see 32:49; die, be gathered 32:50 — the dump's own scan printed empty, its regex the fault, the morph codes read here); THE SONG NEVER SAYS "THE LORD YOUR GOD"; the register empty; the parser's FALSE EIGHT at 32:15 and the joined thousand at 32:30
MO = {(c, v): [(x, m) for x, m in by[('Deut', c, v)]] for c, v in SPAN}
assert [(v, x) for c, v in SPAN for x, m in MO[(c, v)] if m and re.search(r'V[a-zA-Z]v', m)] == [(1, _G('האזינו (broaden out the ear)')), (3, _G('הבו (give)')), (7, _G('זכר (mark)')), (7, _G('בינו (separate mentally)')), (7, _G('שאל (inquire)')), (39, _G('ראו (see)')), (43, _G('הרנינו (creak)')), (46, _G('שימו (put or set)')), (49, _G('עלה (go up)')), (49, _G('וראה (and see)')), (50, _G('ומת (and die)')), (50, _G('והאסף (and gather for any purpose)'))] and MO[(32, 1)][0] == (_G('האזינו (broaden out the ear)'), 'HVhv2mp') and MO[(32, 7)][0] == (_G('זכר (mark)'), 'HVqv2ms')
assert [v for v in range(1, 53) if any(a == _G('יהוה (the LORD)') and b == _G('אלהיך (your God)') for a, b in zip(W(32, v), W(32, v)[1:]))] == [] and sum(1 for v in range(1, 53) for x in W(32, v) if x == _G('יהוה (the LORD)')) == 7 and sum(1 for v in range(1, 53) for x in W(32, v) if x == _G('ליהוה (to the LORD)')) == 1

# ---- THE COUNTER'S DAY (a bare world on the exodus epoch; Moses' last day (40, 12, 7) — 19b's ONE MARKER at 31:1 stands, NO MARKER here; 32:48's selfsame day THAT day; the death date 19b's clock datum on the calendar's keys, read here) ----
with contextlib.redirect_stdout(io.StringIO()):
    _WC = WE.World(era='Moses\' last day — chapter 32 on a bare world (the exodus epoch)', epoch='exodus')
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
OWN42 = ('doctrine_as_rain_and_dew_likened', 'name_of_the_lord_proclaimed_greatness_ascribed', 'the_rock_perfect_and_just_declared', 'generation_crooked_not_his_children', 'father_who_acquired_you_requited', 'days_of_old_remember_commanded', 'nations_bounds_set_by_number_of_israel', 'lords_portion_his_people_jacob', 'found_in_the_desert_encircled_and_kept', 'apple_of_his_eye_kept', 'as_an_eagle_stirring_its_nest_borne', 'the_lord_alone_led_no_foreign_god', 'heights_of_the_land_ridden_honey_from_the_rock', 'feast_of_curd_milk_fat_and_wine_given', 'jeshurun_fat_kicked_forsook_god', 'demons_and_new_gods_sacrificed', 'rock_that_begot_you_forgotten', 'jealousy_by_no_people_foolish_nation', 'fire_kindled_to_the_lowest_sheol', 'evils_heaped_arrows_spent', 'hunger_beasts_serpents_sword_terror_sent', 'blotting_out_stayed_by_the_enemys_boast', 'nation_void_of_counsel', 'one_chasing_a_thousand_rock_sold_them', 'vine_of_sodom_gall_grapes', 'vengeance_laid_up_in_store_sealed', 'lord_judges_his_people_repents_himself', 'where_are_their_gods_asked', 'i_i_am_he_no_god_beside_me', 'i_kill_and_make_alive_none_delivers', 'hand_lifted_to_heaven_live_forever_sworn', 'sword_whetted_vengeance_rendered', 'nations_sing_with_his_people_land_atones', 'song_spoken_in_the_ears_of_the_people', 'hoshea_speaks_the_song_beside_moses', 'set_your_heart_to_these_words_commanded', 'it_is_your_life_no_empty_matter', 'go_up_to_nebo_see_the_land_commanded', 'die_in_the_mountain_gathered_to_your_people_commanded', 'as_aaron_died_in_hor_and_was_gathered', 'trespassed_at_meribath_kadesh_not_sanctified', 'see_the_land_from_afar_not_go_there')
assert len(OWN42) == 42 and len(set(OWN42)) == 42
HOLE_WORDS = r"^(apple_of_his\w*|as_aaron_died\w*|as_an_eagle\w*|blotting_out_stayed\w*|days_of_old\w*|demons_and_new\w*|die_in_the\w*|doctrine_as_rain\w*|evils_heaped_arrows\w*|father_who_acquired\w*|feast_of_curd\w*|fire_kindled_to\w*|found_in_the\w*|generation_crooked_not\w*|go_up_to\w*|hand_lifted_to\w*|heights_of_the\w*|hoshea_speaks_the\w*|hunger_beasts_serpents\w*|i_i_am\w*|i_kill_and\w*|it_is_your\w*|jealousy_by_no\w*|jeshurun_fat_kicked\w*|lord_judges_his\w*|lords_portion_his\w*|name_of_the\w*|nation_void_of\w*|nations_bounds_set\w*|nations_sing_with\w*|one_chasing_a\w*|rock_that_begot\w*|see_the_land\w*|set_your_heart\w*|song_spoken_in\w*|sword_whetted_vengeance\w*|the_lord_alone\w*|the_rock_perfect\w*|trespassed_at_meribath\w*|vengeance_laid_up\w*|vine_of_sodom\w*|where_are_their\w*)$"
_hs = {ent: ledger_scan(ent, HOLE_WORDS) for ent in ('israel_people', 'yehoshua', 'moses')}; HOLE_SCAN = None if any(v is None for v in _hs.values()) else {ent: [e for e in v if e not in OWN42] for ent, v in _hs.items()}   # this sitting's own names excluded once the fold carries them
KIN62 = ('barred_from_the_land', 'gathered_to_his_people', 'became_the_lords_people_this_day', 'lord_declared_israel_treasure_people', 'treasured_people', 'other_gods_barred', 'manna_provided', 'water_from_the_rock', 'eagle_nation_devours', 'few_in_number_left', 'scattered_among_all_peoples', 'serving_wood_and_stone_among_nations', 'sold_and_none_buys', 'sons_flesh_eaten_in_siege', 'pestilence_cleaving', 'sword_blight_mildew_sent', 'trembling_heart_no_rest', 'plagues_made_wonderful', 'innocent_blood_atoned', 'two_witnesses_required', 'two_or_three_witnesses_required', 'one_witness_barred', 'witnesses_inquiry_commanded', 'plotting_witness_talion_commanded', 'song_sung', 'song_writing_commanded', 'song_taught_and_put_in_mouths_commanded', 'song_a_witness_against_israel', 'song_written_and_taught_by_moses', 'song_spoken_to_the_assembly_to_its_end', 'book_a_witness_against_israel', 'future_whoring_after_foreign_gods_foretold', 'covenant_breaking_foretold', 'evils_and_troubles_befall_foretold', 'corruption_after_moses_death_foretold', 'moses_to_sleep_with_the_fathers', 'moses_days_approach_to_die', 'joshua_commissioned_to_bring_israel_in', 'land_brimstone_salt_like_sodom', 'hidden_things_the_lords', 'shema_commanded', 'hakhel_children_hear_and_learn_commanded', 'serpents_sent', 'healed', 'atoned_forgiven', 'sevenfold_vengeance', 'blood_required', 'scattered', 'building_ceased', 'no_share_in_the_world_to_come', 'only_noah_remained', 'famine', 'rain_in_its_season', 'heavens_good_treasure_opened', 'curses_of_the_book_on_the_idolater', 'hidden_idolater_unpardoned', 'heart_turning_to_other_gods_barred', 'enemies_flee_seven_ways', 'smitten_before_enemies_seven_ways', 'nations_dispossessed_as_sihon_and_og_promised', 'holy_people_promised', 'established_holy_people')
KIN_EXPECTED = (2, 5, 2, 1, 1, 1, 1, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 7, 1, 1, 1, 1, 3, 1, 3, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1)   # DN4 — the recon's and the callees' counts on the running world (ch32b_recon.out section H; ch32_callees.out THE NEAR NAMES; the probe Q49's KIN tuple)
assert len(KIN62) == 62 == len(KIN_EXPECTED)
KIN_COUNTS = {k: count_scan(k) for k in KIN62}
REUSE3 = ('heaven_and_earth_witness', 'face_hidden_and_forsaken_foretold', 'length_of_days_on_the_land_promised')
REUSE_BEFORE = {'heaven_and_earth_witness': 4, 'face_hidden_and_forsaken_foretold': 1, 'length_of_days_on_the_land_promised': 1}   # the reuses' counts BEFORE this sitting's lines (the recon) — after the fold carries the new entries the count is the after (the tape's second run reads it so)
REUSE_AFTER = {'heaven_and_earth_witness': 5, 'face_hidden_and_forsaken_foretold': 2, 'length_of_days_on_the_land_promised': 2}
REUSE_COUNTS = {k: count_scan(k) for k in REUSE3}
SCANS = {k: effect_scan(k) for k in KIN62[:8] + REUSE3 + ('garments_transferred_and_aaron_died', 'invested_office', 'song_spoken_to_the_assembly_to_its_end', 'treasured_people')}
del _hs   # 9b's lesson: the raw scans are the database's state at import — the derived lists are equal on the cached and the full load
_FXV = yaml.safe_load(open(_os.path.join(HERE, 'effect_vocabulary.yaml'), encoding='utf-8'))['effects']
print('THE SCANS (printed before they are asserted): holes %s; the kin counts %s; the reuses %s; the entities %s' % (HOLE_SCAN, KIN_COUNTS, REUSE_COUNTS, SCANS))
assert HOLE_SCAN is None or all(v == [] for v in HOLE_SCAN.values()), HOLE_SCAN   # THE HOLES' GROUND — nothing on the three ledgers named the forty-two before this sitting (DN4)
assert all(v is None for v in KIN_COUNTS.values()) or tuple(KIN_COUNTS.values()) == KIN_EXPECTED, [(k, KIN_COUNTS[k], e) for k, e in zip(KIN62, KIN_EXPECTED) if KIN_COUNTS[k] != e]   # the references' counts as the recon read them (DN4 — no second write)
assert all(v is None for v in REUSE_COUNTS.values()) or all(REUSE_COUNTS[k] in (REUSE_BEFORE[k], REUSE_AFTER[k]) for k in REUSE3), REUSE_COUNTS   # the reuses' counts the before (the first run) or the after (the fold carrying this sitting's lines)
SCANS_EXPECTED = {'barred_from_the_land': ['aaron', 'moses'], 'gathered_to_his_people': ['aaron', 'abraham', 'isaac', 'ishmael', 'jacob'], 'became_the_lords_people_this_day': ['israel_people'], 'lord_declared_israel_treasure_people': ['israel_people'], 'treasured_people': ['israel_people'], 'other_gods_barred': ['israel_people'], 'manna_provided': ['israel_people'], 'water_from_the_rock': ['israel_people'], 'heaven_and_earth_witness': ['israel_people'], 'face_hidden_and_forsaken_foretold': ['israel_people'], 'length_of_days_on_the_land_promised': ['israel_people'], 'garments_transferred_and_aaron_died': [], 'invested_office': ['aaron-and-sons', 'eleazar_son_of_aaron', 'pinchas', 'the-firstborn', 'the_levites', 'yehoshua'], 'song_spoken_to_the_assembly_to_its_end': ['israel_people']}   # the entities per effect — typed from the first derive's print (the callees' way — printed before typed)
if SCANS_EXPECTED and any(v is not None for v in SCANS.values()): assert SCANS == SCANS_EXPECTED, [(k, SCANS[k], SCANS_EXPECTED.get(k)) for k in SCANS if SCANS[k] != SCANS_EXPECTED.get(k)]
assert all(k in _FXV for k in OWN42) and sum(1 for k in OWN42 if _FXV[k]['ledger_op'] == 'block') == 0 and sum(1 for k in OWN42 if _FXV[k]['ledger_op'] == 'status') == 32 and sum(1 for k in OWN42 if _FXV[k]['ledger_op'] == 'heaven') == 10, 'the forty-two on the registry (add_types_ch32_a.py)'
assert _FXV['heaven_and_earth_witness']['ledger_op'] == 'status' and _FXV['face_hidden_and_forsaken_foretold']['ledger_op'] == 'heaven' and _FXV['length_of_days_on_the_land_promised']['ledger_op'] == 'heaven' and _FXV['barred_from_the_land']['ledger_op'] == 'heaven' and _FXV['gathered_to_his_people']['ledger_op'] == 'status' and _FXV['treasured_people']['ledger_op'] == 'heaven' and _FXV['other_gods_barred']['ledger_op'] == 'block', 'the reused and referenced rows\' ops (read from the registry\'s print at the types)'
# THE TWINS DIFFED on the DB (the reading's kin asserts read again here — DN4; the shared run SH)
TWIN = {'32:36 vs Ps 135:14': SH(DV(32, 36), ('Ps', 135, 14)), '32:49 vs Num 27:12': SH(DV(32, 49), ('Num', 27, 12)), '32:45 vs 31:1': SH(DV(32, 45), DV(31, 1)), '32:46 vs 31:12': SH(DV(32, 46), DV(31, 12)), '32:47 vs 11:9': SH(DV(32, 47), DV(11, 9)),
        '32:48 vs Gen 7:13': SH(DV(32, 48), ('Gen', 7, 13)), '32:48 vs Exod 12:41': SH(DV(32, 48), ('Exod', 12, 41)), '32:44 vs 31:30': SH(DV(32, 44), DV(31, 30)), '32:44 vs Num 13:16': SH(DV(32, 44), ('Num', 13, 16)), '32:51 vs Num 27:14': SH(DV(32, 51), ('Num', 27, 14)),
        '32:51 vs Num 20:12': SH(DV(32, 51), ('Num', 20, 12)), '32:50 vs Num 20:28': SH(DV(32, 50), ('Num', 20, 28)), '32:1 vs 31:28': SH(DV(32, 1), DV(31, 28)), '32:1 vs 4:26': SH(DV(32, 1), DV(4, 26)), '32:1 vs Isa 1:2': SH(DV(32, 1), ('Isa', 1, 2)), '32:11 vs Exod 19:4': SH(DV(32, 11), ('Exod', 19, 4)),
        '32:15 vs 31:20': SH(DV(32, 15), DV(31, 20)), '32:20 vs 31:17': SH(DV(32, 20), DV(31, 17)), '32:17 vs 29:25': SH(DV(32, 17), DV(29, 25)), '32:8 vs Gen 11:8': SH(DV(32, 8), ('Gen', 11, 8)), '32:24 vs Lev 26:22': SH(DV(32, 24), ('Lev', 26, 22)), '32:30 vs Lev 26:8': SH(DV(32, 30), ('Lev', 26, 8)),
        '32:30 vs Josh 23:10': SH(DV(32, 30), ('Josh', 23, 10)), '32:32 vs 29:22': SH(DV(32, 32), DV(29, 22)), '32:39 vs 6:4': SH(DV(32, 39), DV(6, 4)), '32:43 vs Num 35:33': SH(DV(32, 43), ('Num', 35, 33)), '32:52 vs 34:4': SH(DV(32, 52), DV(34, 4)), '32:49 vs 3:27': SH(DV(32, 49), DV(3, 27)), '32:13 vs 8:15': SH(DV(32, 13), DV(8, 15)),
        '32:21 vs 28:49': SH(DV(32, 21), DV(28, 49)), '32:27 vs 9:28': SH(DV(32, 27), DV(9, 28)), '32:12 vs Num 23:9': SH(DV(32, 12), ('Num', 23, 9)), '32:6 vs Exod 15:16': SH(DV(32, 6), ('Exod', 15, 16))}
print('THE TWINS DIFFED (printed before they are asserted):', TWIN)
TWIN_EXPECTED = {'32:36 vs Ps 135:14': 7, '32:49 vs Num 27:12': 10, '32:45 vs 31:1': 7, '32:46 vs 31:12': 8, '32:47 vs 11:9': 5, '32:48 vs Gen 7:13': 3, '32:48 vs Exod 12:41': 3, '32:44 vs 31:30': 5, '32:44 vs Num 13:16': 4, '32:51 vs Num 27:14': 4, '32:51 vs Num 20:12': 4, '32:50 vs Num 20:28': 2, '32:1 vs 31:28': 2, '32:1 vs 4:26': 2, '32:1 vs Isa 1:2': 0, '32:11 vs Exod 19:4': 1, '32:15 vs 31:20': 0, '32:20 vs 31:17': 3, '32:17 vs 29:25': 3, '32:8 vs Gen 11:8': 0, '32:24 vs Lev 26:22': 0, '32:30 vs Lev 26:8': 1, '32:30 vs Josh 23:10': 3, '32:32 vs 29:22': 1, '32:39 vs 6:4': 0, '32:43 vs Num 35:33': 1, '32:52 vs 34:4': 3, '32:49 vs 3:27': 2, '32:13 vs 8:15': 0, '32:21 vs 28:49': 0, '32:27 vs 9:28': 3, '32:12 vs Num 23:9': 0, '32:6 vs Exod 15:16': 1}
if TWIN_EXPECTED: assert TWIN == TWIN_EXPECTED, [(k, TWIN[k], TWIN_EXPECTED.get(k)) for k in TWIN if TWIN[k] != TWIN_EXPECTED.get(k)]   # typed from the first derive's print (the callees' way — printed before typed)
assert TWIN['32:36 vs Ps 135:14'] >= 7 and TWIN['32:49 vs Num 27:12'] >= 5 and TWIN['32:46 vs 31:12'] >= 6 and TWIN['32:47 vs 11:9'] >= 5, TWIN   # the reading's largest twins (Psalm 135:14 seven in order, the summons five, the charge six, the length of days five)

# ---- THE CALLEES' FACTS (every edge live at the cells that consume them; the values PRINTED at the first pass and ASSERTED from that print at the second — 10b's lesson 2, the callees' way; the q-style cells called with their keys, an absent key printed, never guessed silently) ----
def V(x): return x[0] if isinstance(x, tuple) else x
def Q(c): return (c.get('v'), c.get('p'), c.get('fx'), str(c.get('why', ''))) if isinstance(c, dict) else tuple(c)   # the (v, p, fx, why) cells — the dict's four keys as a tuple
def DD(m): return getattr(m, 'DATA', {})
def ASKS(m, cell): return re.findall(r"if ask == '([a-z_0-9]+)':", inspect.getsource(getattr(m, cell)))
def A(m, cell, ask):
    """an ask-style cell called with its data — (verdict, effects, provenance); a q-style cell called with the key; the ask checked against the cell's own source first"""
    fn = getattr(m, cell); asks = ASKS(m, cell)
    if asks:
        assert ask in asks, ('THE ASK IS NOT THE CELL\'S OWN', m.__name__, cell, ask, asks[:6])
        return fn({'ask': ask}, DD(m))
    return fn(ask)
def DK(m, key):
    d = DD(m); assert key in d, ('THE DATA KEY IS NOT THE CALLEE\'S OWN', m.__name__, key, sorted(d)[:12]); return d[key]
FACTS_PRINT = []
def F(name, val):
    globals()[name] = val; FACTS_PRINT.append((name, (V(val) if not isinstance(val, dict) else val.get('v', val.get('value'))) if val is not None else None)); return val   # a DATA row's value printed (the first pass printed None for the dicts)
# obey_horeb — THE WITNESSES' CHAIN (4:26, 30:19, 31:28, 32:1 — the fifth seat this chapter's), the host apportioned (4:19 — 32:8's kin), the exile case
F('OH_CHAIN', DK(OH, 'the_witnesses_chain')); F('OH_HOST', A(OH, 'no_image', 'the_host_apportioned')); F('OH_WIT', A(OH, 'the_exile_case', 'the_case_head'))
# covenant_return_charge — the song commanded, written and spoken (31:19-30 — the song ahead named forward), the hidden face (31:17), the marker's day, the three gifts
F('CR_SATED', A(CR, 'the_song_commanded', 'when_they_eat_and_are_sated_and_grow_fat_and_turn')); F('CR_HIDE', A(CR, 'the_apostasy_foretold', 'my_anger_kindled_i_will_forsake_them_and_hide_my_face'))
F('CR_SPOKE', A(CR, 'the_book_beside_the_ark_and_the_assembly', 'moses_spoke_the_words_of_this_song_in_the_ears_of_all_the_assembly_to_their_end')); F('CR_LIFE', A(CR, 'life_and_death', 'choose_life_love_hearken_and_cleave_the_length_of_days'))
F('CR_AHEAD', DK(CR, 'the_song_ahead')); F('CR_GIFTS', DK(CR, 'the_three_gifts_and_their_merits')); F('CR_DEATH', DK(CR, 'the_death_date_of_moses')); F('CR_STATE', DK(CR, 'the_life_and_death_state')); F('CR_WITS', DK(CR, 'the_witnesses_of_the_chapter'))
# good_land — the wilderness, the rock of flint (THE TWO ROCKS), the manna 'in your end', the testimony's forgetting; NO receipt in the chapter
F('GL_WILD', A(GL, 'the_chain_and_the_covenant', 'the_wilderness')); F('GL_FLINT', A(GL, 'the_chain_and_the_covenant', 'the_rock_of_flint')); F('GL_MANNA', A(GL, 'the_chain_and_the_covenant', 'the_manna_to_do_you_good')); F('GL_FORGET', A(GL, 'the_testimony', 'if_you_forget'))
F('GL_ROCKS', DK(GL, 'the_two_rocks')); F('GL_HONEY', DK(GL, 'honey_without_milk')); GL_R = GL.receipt_seats(32); F('GL_R', GL_R)
# exodus_story — the treasure's seats (19:5 — 32:9's kin), the ten plagues (the tape's lines by kind), Moses' birthday (12, 7)
F('ES_TREASURE', ES.sinai('treasure_seats')); F('ES_TEN', ES.plagues('ten')); F('ES_BIRTH', ES.birth('birthday'))
# refuge_war_family — one witness for any iniquity (19:15 — the court law read into 32:1's witnesses)
F('RW_ONE', A(RW, 'the_landmark_and_the_witnesses', 'one_witness_for_any_iniquity'))
# persons_poor_court — the nest's sending (22:7 — Peah 1:1's list at 336:2), the vineyard's mixture (22:9 — Kilayim 3:2's kin)
F('PP_NEST', DK(PP, 'the_nests_sending')); F('PP_VINE', DK(PP, 'the_vineyards_mixture'))
# courts_prophet — two witnesses for every death (17:6), the seven investigations (Sanhedrin 5:2), the three acts (17:3 — 32:17's demons)
F('CP_TWO', A(CP, 'the_idolaters_trial', 'two_witnesses_for_every_death')); F('CP_SEVEN', A(CP, 'the_idolaters_trial', 'the_seven_investigations')); F('CP_ACTS', A(CP, 'the_idolaters_trial', 'the_three_acts_and_the_associator'))
# refuge — the one witness (35:30), the land's atonement (35:33 — 32:43's kin), the case table (35:23 — the enemy neither witness nor judge), the ransom rows (35:31)
F('RF_ONE', DK(RF, 'the_one_witness')); F('RF_ATONE', DK(RF, 'the_lands_atonement')); F('RF_TABLE', DK(RF, 'the_case_table')); F('RF_RANSOM', DK(RF, 'the_ransom_rows'))
# ordinances — the courts (Exodus 21:22's judges; 21:30's ransom — 329:4's kin)
OR_COURTS = OR.courts; F('OR_KEYS', sorted(DD(OR))[:8])
# chukat — Aaron's death (20:22-29 — THE RECEIPT at 32:50), the sentence at Meribah (20:12 — 32:51's reason), the seats, the kiss
F('CK_DATES', A(CK, 'edom_and_hor', 'death_dates')); F('CK_SUCC', A(CK, 'edom_and_hor', 'succession')); F('CK_AGE', A(CK, 'edom_and_hor', 'aaron_age'))
F('CK_SENT', A(CK, 'meribah', 'sentence')); F('CK_SEATS', A(CK, 'meribah', 'meribah_seats')); F('CK_KISS', A(CK, 'meribah', 'death_by_the_kiss')); F('CK_DIED', A(CK, 'meribah', 'died_for_sin'))
# opening_speech — THE COMMISSION (Numbers 27:12-23 — the mountain, the sentence cited, the receipt, the debit OPEN to 34:1-4), Bashan
F('OS_MTN', A(OS, 'the_commission', 'the_mountain')); F('OS_SENT', A(OS, 'the_commission', 'the_sentence_cited')); F('OS_RECEIPT', A(OS, 'the_commission', 'the_receipt')); F('OS_DEBIT', A(OS, 'the_commission', 'the_debit')); F('OS_OG', A(OS, 'sihon_and_og', 'og_turned'))
# journeys — Aaron's death RETOLD (33:38-40 — a retelling never writes an act twice), the four writings, the death date (40, 5, 1), the age 123
F('JR_DATE', A(JR, 'aarons_death_retold', 'the_date')); F('JR_AGE', A(JR, 'aarons_death_retold', 'the_age')); F('JR_NOWRITE', A(JR, 'aarons_death_retold', 'no_write')); F('JR_ADAR', A(JR, 'aarons_death_retold', 'moses_seventh_adar')); F('JR_KISS', A(JR, 'aarons_death_retold', 'by_the_mouth_kiss'))
F('JR_FOUR', DK(JR, 'the_four_writings')); F('JR_DD', DK(JR, 'the_death_date')); F('JR_AARON', DK(JR, 'aarons_age'))
# second_tablets — Aaron died there (10:6 — Moserah against Mount Hor, the OPEN row)
F('ST_THERE', A(ST, 'the_stations_and_the_death', 'aaron_died_there')); F('ST_PLACE', A(ST, 'the_stations_and_the_death', 'the_place_of_the_death'))
# primeval — Babel's division (Genesis 11 — 32:8's kin by the ink's words), the flood's boarding (7:13 — the selfsame day), the prologue (the inclination)
PV_BABEL, PV_NATIONS, PV_FLOOD, PV_PROLOGUE = PV.babel, PV.nations, PV.flood, PV.prologue; F('PV_KEYS', sorted(DD(PV))[:8])
# pre_sinai — the sons of Noah (Genesis 9 — the seven commandments, Tosefta Avodah Zarah 9:4's case), the circumcision (17:23, 26 — the selfsame day)
PS_NOAHIDE, PS_CIRC = PS.noahide, PS.circumcision; F('PS_KEYS', sorted(DD(PS))[:8])
# mamre — Sodom's overthrow (Genesis 19:24-25 — 32:32's vine), the possessor of heaven and earth (14:19 — 32:6's acquired)
MA_SODOM, MA_SCENE = MA.sodom, MA.scene; F('MA_KEYS', sorted(DD(MA))[:8])
# family — Jacob's seventy souls (Genesis 46:27 — 32:8's number), the testament (49:33 — the gathering)
FA_MROW, FA_TESTAMENT = FA.mrow, FA.testament; F('FA_KEYS', sorted(DD(FA))[:8])
# balak — a people that dwells alone (Numbers 23:9 — 32:12's 'alone')
BK_STANDS = BK.the_stands; F('BK_KEYS', sorted(DD(BK))[:8])
# beha — the three gifts (the well, the cloud, the manna — Taanit 9a), the manna's taste and form
F('BH_GIFTS', A(BH, 'taberah_and_quail', 'three_gifts')); F('BH_TASTE', A(BH, 'taberah_and_quail', 'manna_taste')); F('BH_FORM', A(BH, 'taberah_and_quail', 'manna_form'))
# shelach — Hoshea to Joshua (Numbers 13:16 — 32:44's old name), the decree (14:16's 'lest they say')
F('SH_NAME', A(SHL, 'spies', 'joshua_name')); SH_DECREE = SHL.decree   # the alias SHL — SH is the shared-run helper (the first pass's two errors)
# not_righteousness — lest the land say (9:28 — 32:27's kin), the ten trials
F('NR_LAND', A(NR, 'the_intercession', 'lest_the_land_say')); F('NR_TRIALS', A(NR, 'the_four_provocations', 'the_ten_trials'))
# seven_nations — the holy people (7:6 — 32:9's portion beside it), chose you, the fewest, the oath (32:40's oath by kind)
F('SN_HOLY', A(SN, 'the_holy_people', 'holy_people')); F('SN_CHOSE', A(SN, 'the_holy_people', 'chose_you')); F('SN_FEW', A(SN, 'the_holy_people', 'the_fewest')); F('SN_OATH', A(SN, 'the_holy_people', 'the_oath'))
# hear_o_israel — the LORD is one (6:4 — 32:39's creed), teach your sons (6:7 — 32:46), the recitation times (Berakhot 1:1 — 333:4's case)
F('HI_ONE', A(HI, 'the_creed', 'the_lord_is_one')); F('HI_TEACH', A(HI, 'the_four_duties', 'teach_your_sons')); F('HI_TIMES', DK(HI, 'the_recitation_times'))
# blessing_and_curse — the rains' dates (11:14 — 32:2's four rains), the land watered by heaven
F('BC_RAIN', DK(BC, 'rain_dates')); BC_WATER = BC.the_land_watered_by_heaven; F('BC_ASKS', ASKS(BC, 'the_land_watered_by_heaven')[:6])
# firstfruits_ebal_curses — the eagle nation (28:49 — 32:21's foolish nation), the first fruits, the things without measure (18b's own row), the false six
F('FE_EAGLE', A(FE, 'the_curses_of_the_siege_and_the_exile', 'a_nation_from_the_end_of_the_earth_as_the_eagle_flies')); F('FE_MEASURE', DK(FE, 'the_things_without_measure')); F('FE_SIX', DK(FE, 'the_false_six')); F('FE_FIRST_ASKS', ASKS(FE, 'the_first_fruits')[:6])
# tochacha — the cascade (Leviticus 26:22's beasts, 26:25's sword — the arms), the measures (26:8's five chase a hundred)
TC_CASCADE, TC_MEASURES, TC_COVENANT = TC.cascade, TC.measures, TC.covenant; F('TC_KEYS', sorted(DD(TC))[:8])
# seducers — the inciter (13:7 — 32:17's 'gods they knew not')
SE_INCITER = SE.the_inciter; F('SE_ASKS', ASKS(SE, 'the_inciter')[:6])
# decalogue — the vain Name (5:11 — 328:4's Name profaned punished at once)
DC_VAIN = DC.vain_name; F('DC_KEYS', sorted(DD(DC))[:8])
# covenant_at_horeb — the assembly called (5:1 — 32:44's 'in the ears of the people')
F('CH_FOUR', A(CH, 'the_assembly_called', 'hear_learn_keep_do'))
# naso — the sota's order (Sotah 1:7 — the measure for measure at 308:4 and 318:8)
F('NS_ORDER', DK(NS, 'sotah_order'))
# incense_shekel — the ransom of the soul (Exodus 30:12 — 329:4's no ransom)
IS_SHEKEL = IS.shekel; F('IS_KEYS', sorted(DD(IS))[:8])
# festivals_judges — who appears, not empty, the gift of the hand (16:16 — the appearing among Peah 1:1's things without measure)
F('FJ_WHO', A(FJ, 'the_three_pilgrimages', 'who_appears')); F('FJ_EMPTY', A(FJ, 'the_three_pilgrimages', 'not_empty')); F('FJ_HAND', A(FJ, 'the_three_pilgrimages', 'the_gift_of_the_hand'))
# holiness — the gifts of the field (Leviticus 19:9-10 — the corner: Peah 3:2, Tosefta Peah 1:3)
HL_GIFTS = HL.gifts; F('HL_ASKS', ASKS(HL, 'gifts')[:6])
# vows — the substitutes' source (Nedarim 1:2 — 306:36), the konam measure, the sage's release (Chagigah 1:8's flying dissolution)
F('VW_SUBS', DK(VW, 'substitutes_source')); F('VW_KONAM', DK(VW, 'konam_measure')); F('VW_SAGE', DK(VW, 'sage_release'))
# food_tithe — the sonship's two arms (14:1 — 32:5's 'His children')
F('FT_SONS', DK(FT, 'the_sonships_arms'))
# gad_reuben — Moses' grave (Reuben's Nebo, Gad's field — Sotah 13b; the Sifrei 355:6)
F('GR_GRAVE', DK(GR, 'moses_grave'))
# borders — the land of Canaan by its border (Numbers 34:2 — 32:49's land of Canaan)
F('BR_LAND', A(BR, 'the_land_and_its_fall', 'the_land_canaan'))
# erection — the calf's argument (Exodus 32:12 — 32:27's 'lest they say'), the presence (the shown face against the hidden)
ER_CALF, ER_PRESENCE = ER.calf, ER.presence; F('ER_KEYS', sorted(DD(ER))[:8])
# sanctions — the burning's scope (Sanhedrin 9:1 — 307:14's burned and beheaded)
SA_BURN = SA.burning_scope; F('SA_ASKS', ASKS(SA, 'burning_scope')[:6])
# vayikra5 — the sacrilege (Leviticus 5:15 — Chagigah 1:8's mountains by a hair)
V5_SAC = V5.sacrilege; F('V5_KEYS', sorted(DD(V5))[:8])
# moadim — the feasts (Leviticus 23 — Chagigah 1:8's festival offerings)
MD_SUK = MD.sukkot; F('MD_KEYS', sorted(DD(MD))[:8])
# mekoshesh — the gatherer's labor (Numbers 15:32 — Chagigah 1:8's Sabbath laws by a hair)
F('MK_LABOR', DK(MK, 'gatherers_labor'))
# THE LIVE CALLS — one cell of every callee CALLED by its literal name (the dependency gate reads `alias.name(` in the runner's source — 19b's lesson: a DATA read is not a live edge; the gate's first print demanded twenty-four)
F('FA_TESTAMENT', FA.testament('couch_seats')); F('OR_WITNESS', OR.courts('witness_of_violence')); F('PP_NEST_ASK', PP.the_garments_nest_parapet_and_mixtures({'ask': 'the_nest_before_you'}, DD(PP))); F('RF_WITNESSES', RF.the_statute({'ask': 'the_witnesses'}, DD(RF)))
F('PV_ONE_LANGUAGE', PV.babel('one_language')); F('PV_PELEG', PV.nations('peleg_prophet')); F('PV_FLOOD_150', PV.flood('hundred_fifty')); F('PV_READING_ROW', PV.prologue('reading_row'))
F('PS_SEVEN', PS.noahide('seven_from_root')); F('MA_LOT', MA.sodom('lot_learned_where')); F('MA_THREE', MA.mamre('three_men')); F('BK_MOST_HIGH', BK.the_stands({'ask': 'most_high_knowledge'}, DD(BK)))
F('SH_DECREE_TRIALS', SHL.decree({'ask': 'ten_trials'}, DD(SHL))); F('BC_WATER_ASK', BC.the_land_watered_by_heaven({'ask': BC_ASKS[3]}, DD(BC))); F('TC_MEAS', TC.measures()); F('SE_INCITER_KIN', SE.the_inciter({'ask': 'the_inciters_kin'}, DD(SE)))
F('DC_VAIN_OATH', DC.vain_name({'ask': 'vain_oath'}, DD(DC))); F('NS_SOTAH_CONDITIONS', NS.sotah({'ask': 'conditions'}, DD(NS))); F('IS_RANSOM', IS.shekel('ransom')); F('HL_KINDS', HL.gifts('kinds'))
F('VW_MAN', VW.the_man({'ask': 'frame'}, DD(VW))); F('FT_SONS_ASK', FT.the_sons_and_the_cuttings({'ask': 'the_sonships_arms'}, DD(FT))); F('GR_CHARGE', GR.the_acceptance_and_the_charge({'ask': 'the_order_reversed'}, DD(GR)))
F('ER_MOLTEN', ER.calf('molten_calf')); F('ER_TWELVE_MIL', ER.presence('twelve_mil')); F('SA_BURNED', SA.burning_scope()); F('V5_MEILAH', V5.sacrilege({'ask': 'meilah'}, DD(V5))); F('MD_SUKKOT', MD.sukkot()); F('MK_LABOR_ASK', MK.the_gatherer({'ask': 'labor'}, DD(MK)))
print('THE CALLEES\' FACTS (printed before they are asserted — %d):' % len(FACTS_PRINT))
for _n, _v in FACTS_PRINT: print('  FACT %s = %s' % (_n, repr(_v)[:150]))
# ---- THE FACTS ASSERTED FROM THE FIRST PASS'S PRINT (parse_ch32_fastcheck.py wrote these from ch32_fastcheck_run0.out — the repr's first sixty characters; a moved callee fails here, not in a cell) ----
_FV = dict(FACTS_PRINT)
assert repr(_FV['OH_CHAIN'])[:60] == "{'this_chapter': 'Deut 4:26', 'the_chain': ['Deut 4:26', 'De", ('OH_CHAIN', repr(_FV['OH_CHAIN'])[:100])
assert repr(_FV['OH_HOST'])[:60] == '"the host apportioned (4:19) — with 29:25 by the Sifrei 148:', ('OH_HOST', repr(_FV['OH_HOST'])[:100])
assert repr(_FV['OH_WIT'])[:60] == '"the case head (4:25) — THE CHAPTER\'S ONE CASE: \'when\' with ', ('OH_WIT', repr(_FV['OH_WIT'])[:100])
assert repr(_FV['CR_SATED'])[:60] == '"when they eat and are sated and grow fat and turn (31:20) —', ('CR_SATED', repr(_FV['CR_SATED'])[:100])
assert repr(_FV['CR_HIDE'])[:60] == '"My anger kindled, I will forsake them and hide My face (31:', ('CR_HIDE', repr(_FV['CR_HIDE'])[:100])
assert repr(_FV['CR_SPOKE'])[:60] == '"Moses spoke the words of this song in the ears of all the a', ('CR_SPOKE', repr(_FV['CR_SPOKE'])[:100])
assert repr(_FV['CR_LIFE'])[:60] == '"choose life, love, hearken and cleave — the length of days ', ('CR_LIFE', repr(_FV['CR_LIFE'])[:100])
assert repr(_FV['CR_AHEAD'])[:60] == '{\'the_text\': "Deut 32:1-43 — sitting 20\'s reading and its co', ('CR_AHEAD', repr(_FV['CR_AHEAD'])[:100])
assert repr(_FV['CR_GIFTS'])[:60] == '"THREE GIFTS BY THREE MERITS — the well by Miriam\'s, the pil', ('CR_GIFTS', repr(_FV['CR_GIFTS'])[:100])
assert repr(_FV['CR_DEATH'])[:60] == '"THE SEVENTH OF ADAR OF THE FORTIETH YEAR — the year the ink', ('CR_DEATH', repr(_FV['CR_DEATH'])[:100])
assert repr(_FV['CR_STATE'])[:60] == "{'the_settings_of_one_state': ['Deut 11:26-28 (a blessing an", ('CR_STATE', repr(_FV['CR_STATE'])[:100])
assert repr(_FV['CR_WITS'])[:60] == "{'heaven_and_earth': ['Deut 4:26', 'Deut 30:19', 'Deut 31:28", ('CR_WITS', repr(_FV['CR_WITS'])[:100])
assert repr(_FV['GL_WILD'])[:60] == '"the great and terrible wilderness (8:15) — 1:19\'s phrase (t', ('GL_WILD', repr(_FV['GL_WILD'])[:100])
assert repr(_FV['GL_FLINT'])[:60] == '"the rock of flint (8:15) — \'who brought you water out of th', ('GL_FLINT', repr(_FV['GL_FLINT'])[:100])
assert repr(_FV['GL_MANNA'])[:60] == '"the manna to do you good (8:16) — \'who fed you manna … to h', ('GL_MANNA', repr(_FV['GL_MANNA'])[:100])
assert repr(_FV['GL_FORGET'])[:60] == '"if you surely forget (8:19) — the infinitive absolute, the ', ('GL_FORGET', repr(_FV['GL_FORGET'])[:100])
assert repr(_FV['GL_ROCKS'])[:60] == '{\'exodus\': "Exodus 17:6 \'you shall strike THE ROCK (tzur)\' —', ('GL_ROCKS', repr(_FV['GL_ROCKS'])[:100])
assert repr(_FV['GL_HONEY'])[:60] == '{\'the_verse\': "\'a land of olive oil and honey\' (8:8) — \'flow', ('GL_HONEY', repr(_FV['GL_HONEY'])[:100])
assert repr(_FV['GL_R'])[:60] == '[]', ('GL_R', repr(_FV['GL_R'])[:100])
assert repr(_FV['ES_TREASURE'])[:60] == '4', ('ES_TREASURE', repr(_FV['ES_TREASURE'])[:100])
assert repr(_FV['ES_TEN'])[:60] == '10', ('ES_TEN', repr(_FV['ES_TEN'])[:100])
assert repr(_FV['ES_BIRTH'])[:60] == '(12, 7)', ('ES_BIRTH', repr(_FV['ES_BIRTH'])[:100])
assert repr(_FV['RW_ONE'])[:60] == '"one witness for any iniquity (19:15) — the general rule fro', ('RW_ONE', repr(_FV['RW_ONE'])[:100])
assert repr(_FV['PP_NEST'])[:60] == "'the hovering mother, even one fledgling, the return even fi", ('PP_NEST', repr(_FV['PP_NEST'])[:100])
assert repr(_FV['PP_VINE'])[:60] == '"routed here from Leviticus 19:19\'s cell — the institution\'s', ('PP_VINE', repr(_FV['PP_VINE'])[:100])
assert repr(_FV['CP_TWO'])[:60] == '"two witnesses for every death (17:6) — \'shall the dead die\'', ('CP_TWO', repr(_FV['CP_TWO'])[:100])
assert repr(_FV['CP_SEVEN'])[:60] == '"the seven investigations (17:4) — \'well\' \'well\' the analogy', ('CP_SEVEN', repr(_FV['CP_SEVEN'])[:100])
assert repr(_FV['CP_ACTS'])[:60] == '"the three acts and the associator (17:3) — the goer, the se', ('CP_ACTS', repr(_FV['CP_ACTS'])[:100])
assert repr(_FV['RF_ONE'])[:60] == "'two_by_the_prototype'", ('RF_ONE', repr(_FV['RF_ONE'])[:100])
assert repr(_FV['RF_ATONE'])[:60] == "'by_the_shedders_blood'", ('RF_ATONE', repr(_FV['RF_ATONE'])[:100])
assert repr(_FV['RF_TABLE'])[:60] == "'computed_from_the_tokens'", ('RF_TABLE', repr(_FV['RF_TABLE'])[:100])
assert repr(_FV['RF_RANSOM'])[:60] == "'refused_twice'", ('RF_RANSOM', repr(_FV['RF_RANSOM'])[:100])
assert repr(_FV['OR_KEYS'])[:60] == '[]', ('OR_KEYS', repr(_FV['OR_KEYS'])[:100])
assert repr(_FV['CK_DATES'])[:60] == "'Aaron (40, 5, 1) by the ink, aged 123; Miriam the tenth of ", ('CK_DATES', repr(_FV['CK_DATES'])[:100])
assert repr(_FV['CK_SUCC'])[:60] == "'the garments to Eleazar and the office with them — Exod 29:", ('CK_SUCC', repr(_FV['CK_SUCC'])[:100])
assert repr(_FV['CK_AGE'])[:60] == "'Aaron 123 at his death (33:39 — [123])'", ('CK_AGE', repr(_FV['CK_AGE'])[:100])
assert repr(_FV['CK_SENT'])[:60] == '"barred from the land — Moses and Aaron; Aaron\'s closed at 2', ('CK_SENT', repr(_FV['CK_SENT'])[:100])
assert repr(_FV['CK_SEATS'])[:60] == "'Meribah at 6 seats — Exod 17:7 the first, Num 20:13 the sec", ('CK_SEATS', repr(_FV['CK_SEATS'])[:100])
assert repr(_FV['CK_KISS'])[:60] == '\'Miriam too by the kiss — "there" / "there" with Deut 34:5 (', ('CK_KISS', repr(_FV['CK_KISS'])[:100])
assert repr(_FV['CK_DIED'])[:60] == "'died for their sin — had they believed, their time had not ", ('CK_DIED', repr(_FV['CK_DIED'])[:100])
assert repr(_FV['OS_MTN'])[:60] == '"the mountain of Abarim (27:12) — Nebo and Pisgah its other ', ('OS_MTN', repr(_FV['OS_MTN'])[:100])
assert repr(_FV['OS_SENT'])[:60] == '"Meribah cited (27:14) — 20:12\'s sentence pointed to, the ba', ('OS_SENT', repr(_FV['OS_SENT'])[:100])
assert repr(_FV['OS_RECEIPT'])[:60] == '"the receipt (27:22-23) — \'as the LORD commanded him\': the c', ('OS_RECEIPT', repr(_FV['OS_RECEIPT'])[:100])
assert repr(_FV['OS_DEBIT'])[:60] == "'the debit (27:12) — see the land from Abarim: commanded on ", ('OS_DEBIT', repr(_FV['OS_DEBIT'])[:100])
assert repr(_FV['OS_OG'])[:60] == "'Og turned (3:1-3) — 21:33-35 with the persons shifted (we f", ('OS_OG', repr(_FV['OS_OG'])[:100])
assert repr(_FV['JR_DATE'])[:60] == '"Aaron died on (40, 5, 1) (33:38) — the tape\'s marker at 20:', ('JR_DATE', repr(_FV['JR_DATE'])[:100])
assert repr(_FV['JR_AGE'])[:60] == '"Aaron 123 at his death (33:39) = Exodus 7:7\'s 83 + 40; Mose', ('JR_AGE', repr(_FV['JR_AGE'])[:100])
assert repr(_FV['JR_NOWRITE'])[:60] == '"no write for 33:38-40 — the death and the hearing are the t', ('JR_NOWRITE', repr(_FV['JR_NOWRITE'])[:100])
assert repr(_FV['JR_ADAR'])[:60] == '"Moses\' seventh of Adar — computed backward from the tenth o', ('JR_ADAR', repr(_FV['JR_ADAR'])[:100])
assert repr(_FV['JR_KISS'])[:60] == '"by the mouth of the LORD at the death (33:38) — the kiss (B', ('JR_KISS', repr(_FV['JR_KISS'])[:100])
assert repr(_FV['JR_FOUR'])[:60] == "['Exod 24:4', 'Num 33:2', 'Deut 31:9', 'Deut 31:22']", ('JR_FOUR', repr(_FV['JR_FOUR'])[:100])
assert repr(_FV['JR_DD'])[:60] == '(40, 5, 1)', ('JR_DD', repr(_FV['JR_DD'])[:100])
assert repr(_FV['JR_AARON'])[:60] == '123', ('JR_AARON', repr(_FV['JR_AARON'])[:100])
assert repr(_FV['ST_THERE'])[:60] == '"there Aaron died (10:6) — the tape\'s garments_transferred_a', ('ST_THERE', repr(_FV['ST_THERE'])[:100])
assert repr(_FV['ST_PLACE'])[:60] == '"the place of the death — Moserah in the retelling (10:6), M', ('ST_PLACE', repr(_FV['ST_PLACE'])[:100])
assert repr(_FV['PV_KEYS'])[:60] == '[]', ('PV_KEYS', repr(_FV['PV_KEYS'])[:100])
assert repr(_FV['PS_KEYS'])[:60] == '[]', ('PS_KEYS', repr(_FV['PS_KEYS'])[:100])
assert repr(_FV['MA_KEYS'])[:60] == '[]', ('MA_KEYS', repr(_FV['MA_KEYS'])[:100])
assert repr(_FV['FA_KEYS'])[:60] == '[]', ('FA_KEYS', repr(_FV['FA_KEYS'])[:100])
assert repr(_FV['BK_KEYS'])[:60] == "['altars_total', 'aramean_woman', 'atone_tense', 'balaam_and", ('BK_KEYS', repr(_FV['BK_KEYS'])[:100])
assert repr(_FV['BH_GIFTS'])[:60] == "'the well, the cloud, the manna — three gifts by three sheph", ('BH_GIFTS', repr(_FV['BH_GIFTS'])[:100])
assert repr(_FV['BH_TASTE'])[:60] == "'by age — bread, oil, honey'", ('BH_TASTE', repr(_FV['BH_TASTE'])[:100])
assert repr(_FV['BH_FORM'])[:60] == "'by rank — baked, cakes, raw'", ('BH_FORM', repr(_FV['BH_FORM'])[:100])
assert repr(_FV['SH_NAME'])[:60] == "'Hoshea to Joshua at 13:16 — the new name at 8 seats before ", ('SH_NAME', repr(_FV['SH_NAME'])[:100])
assert repr(_FV['NR_LAND'])[:60] == '"lest the land say (9:28) — THE TAUNT\'S FOUR FORMS (Exod 32:', ('NR_LAND', repr(_FV['NR_LAND'])[:100])
assert repr(_FV['NR_TRIALS'])[:60] == "'the ten trials (Avot 5:4; Arakhin 15a:14; ES.trials by CALL", ('NR_TRIALS', repr(_FV['NR_TRIALS'])[:100])
assert repr(_FV['SN_HOLY'])[:60] == '"a holy people (7:6) — 19:5-6\'s treasure and holy nation rea', ('SN_HOLY', repr(_FV['SN_HOLY'])[:100])
assert repr(_FV['SN_CHOSE'])[:60] == '"chose you (7:6-7) — the choice of the people after 4:37\'s c', ('SN_CHOSE', repr(_FV['SN_CHOSE'])[:100])
assert repr(_FV['SN_FEW'])[:60] == '"the fewest (7:7) — \'not because you were more\': the humbles', ('SN_FEW', repr(_FV['SN_FEW'])[:100])
assert repr(_FV['SN_OATH'])[:60] == "'the oath (7:8) — the noun starred by the parser, the sweari", ('SN_OATH', repr(_FV['SN_OATH'])[:100])
assert repr(_FV['HI_ONE'])[:60] == '"the LORD is one (6:4) — the two seats of the pair (6:4, Zec', ('HI_ONE', repr(_FV['HI_ONE'])[:100])
assert repr(_FV['HI_TEACH'])[:60] == '"teach your sons (6:7) — the father\'s duty to teach Torah, t', ('HI_TEACH', repr(_FV['HI_TEACH'])[:100])
assert repr(_FV['HI_TIMES'])[:60] == "{'evening_from': 'when the priests enter to eat their teruma", ('HI_TIMES', repr(_FV['HI_TIMES'])[:100])
assert repr(_FV['BC_RAIN'])[:60] == '{\'mention_from\': "the last festival day of Sukkot — the eigh', ('BC_RAIN', repr(_FV['BC_RAIN'])[:100])
assert repr(_FV['BC_ASKS'])[:60] == "['all_the_commandment', 'the_oath_to_the_fathers', 'not_like", ('BC_ASKS', repr(_FV['BC_ASKS'])[:100])
assert repr(_FV['FE_EAGLE'])[:60] == '"a nation from the end of the earth as the eagle flies (28:4', ('FE_EAGLE', repr(_FV['FE_EAGLE'])[:100])
assert repr(_FV['FE_MEASURE'])[:60] == "'the corner, the first fruits, the appearing, the acts of ki", ('FE_MEASURE', repr(_FV['FE_MEASURE'])[:100])
assert repr(_FV['FE_SIX'])[:60] == '{\'28:63\': "the parser\'s [6] is the verb \'rejoiced\' — the num', ('FE_SIX', repr(_FV['FE_SIX'])[:100])
assert repr(_FV['FE_FIRST_ASKS'])[:60] == "['when_you_come_into_the_land_and_dwell_in_it', 'the_first_o", ('FE_FIRST_ASKS', repr(_FV['FE_FIRST_ASKS'])[:100])
assert repr(_FV['TC_KEYS'])[:60] == '[]', ('TC_KEYS', repr(_FV['TC_KEYS'])[:100])
assert repr(_FV['SE_ASKS'])[:60] == "['the_inciters_kin', 'entice_two_senses', 'the_entrapment', ", ('SE_ASKS', repr(_FV['SE_ASKS'])[:100])
assert repr(_FV['DC_KEYS'])[:60] == '[]', ('DC_KEYS', repr(_FV['DC_KEYS'])[:100])
assert repr(_FV['CH_FOUR'])[:60] == '"hear, learn, keep, do (5:1) — the second speech opened: Mos', ('CH_FOUR', repr(_FV['CH_FOUR'])[:100])
assert repr(_FV['NS_ORDER'])[:60] == "'drink_then_offer'", ('NS_ORDER', repr(_FV['NS_ORDER'])[:100])
assert repr(_FV['IS_KEYS'])[:60] == '[]', ('IS_KEYS', repr(_FV['IS_KEYS'])[:100])
assert repr(_FV['FJ_WHO'])[:60] == '"who appears (16:16) — all obligated except the twelve exemp', ('FJ_WHO', repr(_FV['FJ_WHO'])[:100])
assert repr(_FV['FJ_EMPTY'])[:60] == '"not empty (16:16) — the appearance offering owed at the app', ('FJ_EMPTY', repr(_FV['FJ_EMPTY'])[:100])
assert repr(_FV['FJ_HAND'])[:60] == "'the gift of the hand (16:17) — many eaters and little prope", ('FJ_HAND', repr(_FV['FJ_HAND'])[:100])
assert repr(_FV['HL_ASKS'])[:60] == '[]', ('HL_ASKS', repr(_FV['HL_ASKS'])[:100])
assert repr(_FV['VW_SUBS'])[:60] == "'nations_words_yochanan'", ('VW_SUBS', repr(_FV['VW_SUBS'])[:100])
assert repr(_FV['VW_KONAM'])[:60] == "'any_amount'", ('VW_KONAM', repr(_FV['VW_KONAM'])[:100])
assert repr(_FV['VW_SAGE'])[:60] == "'expert_alone_or_three_laymen'", ('VW_SAGE', repr(_FV['VW_SAGE'])[:100])
assert repr(_FV['FT_SONS'])[:60] == "{'r_yehuda': 'sons when you act as sons (the Sifrei 96:9; Ki", ('FT_SONS', repr(_FV['FT_SONS'])[:100])
assert repr(_FV['GR_GRAVE'])[:60] == "'reubens_nebo_gads_field'", ('GR_GRAVE', repr(_FV['GR_GRAVE'])[:100])
assert repr(_FV['BR_LAND'])[:60] == '"the land of Canaan (34:2) read as a title claim (Sanhedrin ', ('BR_LAND', repr(_FV['BR_LAND'])[:100])
assert repr(_FV['ER_KEYS'])[:60] == '[]', ('ER_KEYS', repr(_FV['ER_KEYS'])[:100])
assert repr(_FV['SA_ASKS'])[:60] == '[]', ('SA_ASKS', repr(_FV['SA_ASKS'])[:100])
assert repr(_FV['V5_KEYS'])[:60] == "['claim_forms', 'ram_floor']", ('V5_KEYS', repr(_FV['V5_KEYS'])[:100])
assert repr(_FV['MD_KEYS'])[:60] == '[]', ('MD_KEYS', repr(_FV['MD_KEYS'])[:100])
assert repr(_FV['MK_LABOR'])[:60] == "'detaching'", ('MK_LABOR', repr(_FV['MK_LABOR'])[:100])
assert repr(_FV['FA_TESTAMENT'])[:60] == '5', ('FA_TESTAMENT', repr(_FV['FA_TESTAMENT'])[:100])
assert repr(_FV['OR_WITNESS'])[:60] == "'robbers_disqualified'", ('OR_WITNESS', repr(_FV['OR_WITNESS'])[:100])
assert repr(_FV['PP_NEST_ASK'])[:60] == '"the nest before you (22:6-7) — the chance nest, not the pre', ('PP_NEST_ASK', repr(_FV['PP_NEST_ASK'])[:100])
assert repr(_FV['RF_WITNESSES'])[:60] == '"the witnesses (35:30) — two by the prototype (the Sifrei 16', ('RF_WITNESSES', repr(_FV['RF_WITNESSES'])[:100])
assert repr(_FV['PV_ONE_LANGUAGE'])[:60] == '1', ('PV_ONE_LANGUAGE', repr(_FV['PV_ONE_LANGUAGE'])[:100])
assert repr(_FV['PV_PELEG'])[:60] == "'eber_a_great_prophet'", ('PV_PELEG', repr(_FV['PV_PELEG'])[:100])
assert repr(_FV['PV_FLOOD_150'])[:60] == '150', ('PV_FLOOD_150', repr(_FV['PV_FLOOD_150'])[:100])
assert repr(_FV['PV_READING_ROW'])[:60] == "'reprieve'", ('PV_READING_ROW', repr(_FV['PV_READING_ROW'])[:100])
assert repr(_FV['PS_SEVEN'])[:60] == "{'commanded': 'courts', 'the_LORD': 'blasphemy', 'God': 'ido", ('PS_SEVEN', repr(_FV['PS_SEVEN'])[:100])
assert repr(_FV['MA_LOT'])[:60] == "'abrahams_house'", ('MA_LOT', repr(_FV['MA_LOT'])[:100])
assert repr(_FV['MA_THREE'])[:60] == '3', ('MA_THREE', repr(_FV['MA_THREE'])[:100])
assert repr(_FV['BK_MOST_HIGH'])[:60] == '"\'knows the knowledge of the Most High\' = fixes the moment o', ('BK_MOST_HIGH', repr(_FV['BK_MOST_HIGH'])[:100])
assert repr(_FV['SH_DECREE_TRIALS'])[:60] == '"10 — \'these ten times\' (14:22; Pirkei Avot 5:4); the ledger', ('SH_DECREE_TRIALS', repr(_FV['SH_DECREE_TRIALS'])[:100])
assert repr(_FV['BC_WATER_ASK'])[:60] == '"drinks by the rain of heaven (11:11) — the one seat; THE SO', ('BC_WATER_ASK', repr(_FV['BC_WATER_ASK'])[:100])
assert repr(_FV['TC_MEAS'])[:60] == 'None', ('TC_MEAS', repr(_FV['TC_MEAS'])[:100])
assert repr(_FV['SE_INCITER_KIN'])[:60] == '"the inciter\'s kin (13:7) — the brother by the father, the m', ('SE_INCITER_KIN', repr(_FV['SE_INCITER_KIN'])[:100])
assert repr(_FV['DC_VAIN_OATH'])[:60] == "'lashes'", ('DC_VAIN_OATH', repr(_FV['DC_VAIN_OATH'])[:100])
assert repr(_FV['NS_SOTAH_CONDITIONS'])[:60] == "'six: lain with, hidden, secreted, defiled, no witness, not ", ('NS_SOTAH_CONDITIONS', repr(_FV['NS_SOTAH_CONDITIONS'])[:100])
assert repr(_FV['IS_RANSOM'])[:60] == "['Deut 21:8', 'Exod 21:30', 'Exod 29:33', 'Exod 30:12', 'Num", ('IS_RANSOM', repr(_FV['IS_RANSOM'])[:100])
assert repr(_FV['HL_KINDS'])[:60] == "['corner', 'fallen_grapes', 'gleanings', 'small_clusters']", ('HL_KINDS', repr(_FV['HL_KINDS'])[:100])
assert repr(_FV['VW_MAN'])[:60] == '"a law relayed in Moses\' voice — this is the thing which the', ('VW_MAN', repr(_FV['VW_MAN'])[:100])
assert repr(_FV['FT_SONS_ASK'])[:60] == '"the sonship\'s arms (14:1) — R. Yehuda: sons when you act as', ('FT_SONS_ASK', repr(_FV['FT_SONS_ASK'])[:100])
assert repr(_FV['GR_CHARGE'])[:60] == '"our little ones, our wives, our cattle and all our beasts (', ('GR_CHARGE', repr(_FV['GR_CHARGE'])[:100])
assert repr(_FV['ER_MOLTEN'])[:60] == '4', ('ER_MOLTEN', repr(_FV['ER_MOLTEN'])[:100])
assert repr(_FV['ER_TWELVE_MIL'])[:60] == "'students_travel_a_fortiori'", ('ER_TWELVE_MIL', repr(_FV['ER_TWELVE_MIL'])[:100])
assert repr(_FV['SA_BURNED'])[:60] == "['R._Yishmael_him_and_one', 'R._Akiva_both', 'Onkelos_plural", ('SA_BURNED', repr(_FV['SA_BURNED'])[:100])
assert repr(_FV['V5_MEILAH'])[:60] == "'no offering'", ('V5_MEILAH', repr(_FV['V5_MEILAH'])[:100])
assert repr(_FV['MD_SUKKOT'])[:60] == 'None', ('MD_SUKKOT', repr(_FV['MD_SUKKOT'])[:100])
assert repr(_FV['MK_LABOR_ASK'])[:60] == '"detaching (the baraita; the Sifrei\'s own word) — capital"', ('MK_LABOR_ASK', repr(_FV['MK_LABOR_ASK'])[:100])


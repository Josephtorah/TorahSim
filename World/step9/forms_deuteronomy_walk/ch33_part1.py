#!/usr/bin/env python3
# DEUTERONOMY 33:1-29 — THE BLESSING (and this is the blessing which Moses the man of God blessed the children of Israel before his death; the LORD came from Sinai, rose from Seir,
# shone from mount Paran, a fiery law at His right hand; He loves the peoples, all His holy ones in Your hand; Moses commanded us a law, the inheritance of the congregation of Jacob;
# a king in Jeshurun when the heads of the people gathered. Let Reuben live and not die; hear, LORD, the voice of Judah; Levi's Thummim and Urim, proved at Massah, the father and
# mother unseen, the covenant kept, the teaching, the incense and the whole offering, the substance blessed and the risers smitten; Benjamin the beloved between His shoulders; Joseph's
# land blessed with the precious things, the bush dweller's favor on the crown of him separate from his brethren, the firstling ox's horns with Ephraim's myriads and Manasseh's
# thousands; Zebulun in his going out and Issachar in his tents, the peoples called to the mountain; Gad enlarged, the lioness, the first part and the lawgiver's portion, the heads of
# the people; Dan the lion's whelp, Naphtali sated with favor, Asher's foot in oil, the bars of iron and brass; none like the God of Jeshurun, the rider of the heaven, the everlasting
# arms, the enemy driven out; Israel dwells in safety alone, the fountain of Jacob; happy are you, O Israel — the shield and the sword, the high places trodden); THE READBACK'S FORMS
# ON FILE, NO NEW FORM (THE DEUTERONOMY WALK sitting 21b — THE LEAN PASS, 2026-09-29; World/step9/DEUTERONOMY_WALK.md "Sitting 21b"; the state doc's #241). ONE RUNNER OVER ONE
# CHAPTER AND ONE UNIT (deu_33_ve_zot — the blessing 33:1-29; the span one range); ELEVEN own-day lines IN TWO FORMS — 1 ACT (the frame 33:1-2) and 10 SPEECHES (the prologue 33:3-5,
# the ten blessings at the reading's seats, the coda's two): EVERY LINE AT MOSES' LAST DAY (40, 12, 7) after 19b's ONE MARKER at 31:1 — NO MARKER HERE ('before his death' THAT day;
# the Sifrei 342:1 — the hard words first, the blessing after): moses_blessed_israel_before_his_death (33:1-2), blessing_prologue_law_and_king_declared (33:3-5),
# blessing_reuben_and_judah_declared (33:6-7), blessing_levi_declared (33:8-11), blessing_benjamin_declared (33:12), blessing_joseph_declared (33:13-17),
# blessing_zebulun_and_issachar_declared (33:18-19), blessing_gad_declared (33:20-21), blessing_dan_naphtali_asher_declared (33:22-25), blessing_rider_of_the_heaven_declared (33:26-27),
# blessing_israel_dwells_alone_declared (33:28-29) — TWENTY-EIGHT writes on TWELVE ledgers (twenty-eight NEW, all STATUSES, no block, no heaven entry — Israel 10 and THE TRIBES' OWN:
# reuben 1, judah 1, levi 4, benjamin 1, joseph 3, zebulun 1, issachar 1, gad 2, dan_son 1, naphtali 1, asher 2 — the sons' entities Genesis 49's testament wrote on; Simeon named
# nowhere, no write; NO REUSE). THE PARSER'S FALSE SEVEN as a DATA row (33:23's 'sated' — seven's consonants, MARKED and counted as nothing), no guard, no count in the world. THE
# KIN'S CELLS BY CALL (thirty-nine runners, every edge REFERENCE — the kin read this chapter forward: the death 34:5 ahead, Moses' grave in Gad's field, the six Meribah seats, the
# commission's debit OPEN to 34:1-4); THE TAPE'S LINES BY KIND (Sinai's descent, Massah and Meribah, the calf's sword, the bush, the crossed hands, Isaac's dew and corn, the
# testament, the law written and delivered); MOSES' GRAVE at 33:21 FORWARD to 34:6 (the death's sitting's — READ THEN COMPILE PER PORTION); THE TWO POINTER ROWS 33:5 and 33:28
# (20b's owed pointers PAID, grade R). Eleven cells and the table; every token probed (zero-report law); effects on every cell (the effects law); THE EXAM THE FIFTEEN MISHNAH AND
# TOSEFTA ROWS THE LEDGER CITES (Avot 1:1, 3:6, 5:6; Bava Kamma 4:3; Berakhot 4:3; Eduyot 8:6; Keritot 2:1; Menachot 8:3; Rosh Hashanah 2:8, 2:9; Sanhedrin 10:1; Shekalim 1:1;
# Sotah 7:5; Tosefta Avodah Zarah 9:4, Tosefta Eduyot 1:1 — read whole; four rows the regex misread, read whole and excluded; no docket, the lean form); the parameters the runner's
# DATA rows (sixteen — the sanctuary's tribe an OPEN parameter), NO clock datum (19b's death date THE DAY). The daemon law_blessing_of_moses given_at Deut 33:1, installed_by boot
# (the Deuteronomy daemons' form). Reading ledger: logic/oral_triage/deu_33_ve_zot_2026-09-29.md; the lean exam: deu_33_ve_zot_exam_2026-09-29.md.

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
import cold_run_song_charge_nebo as SC            # THE EDGE: blessing_of_moses -> song_charge_nebo CALL, reference (32:50's death commanded — 33:1's 'before his death', the event 34:5 AHEAD; the_readback's form; 32:15's Jeshurun — 33:5, 33:26; 32:13's high places — 33:29 by sense)
import cold_run_covenant_return_charge as CR    # THE EDGE: blessing_of_moses -> covenant_return_charge CALL, reference (31:9's law written and delivered — 33:4's handing-over; 31:14's days approach to die; the marker's day (40, 12, 7); the three gifts owed at 34:5)
import cold_run_gad_reuben as GR                 # THE EDGE: blessing_of_moses -> gad_reuben CALL, reference (Numbers 32:38's Nebo — MOSES' GRAVE in Gad's field, Sotah 13b: the pointer 33:21 FORWARD to 34:6; 32:33's land east — 33:20's enlarged Gad)
import cold_run_joseph as JO                     # THE EDGE: blessing_of_moses -> joseph CALL, reference (Genesis 49:25-26 five in order and 49:26's line whole — 33:13-16; 48:19's crossed hands — 33:17's Ephraim before Manasseh; the sons' ledgers the testament wrote on)
import cold_run_family as FA                     # THE EDGE: blessing_of_moses -> family CALL, reference (Genesis 27:10's 'before his death' — 33:1; 27:28's dew and corn THE KIN ONKELOS NAMES at 33:28; 35:22 Bilhah and 38:26 Tamar — 347:1, 348:1; 35:20 Rachel's grave — 352:16)
import cold_run_chukat as CK                     # THE EDGE: blessing_of_moses -> chukat CALL, reference (Numbers 20:12-13 the sentence at Meribah — 33:8's waters of Meribah, the six seats; 20:22-29 Aaron's death and the succession)
import cold_run_exodus_story as ES               # THE EDGE: blessing_of_moses -> exodus_story CALL, reference (Exodus 19:18-20 the descent — 33:2's Sinai; 17:7 Massah — 33:8; 3:2-4 the bush — 33:16; the seventh of Adar Moses' birthday)
import cold_run_erection as ER                   # THE EDGE: blessing_of_moses -> erection CALL, reference (Exodus 32:26-29 the calf's sword on the maternal kin — 33:9's father and mother unseen; 349:1's Levi repaid at the calf)
import cold_run_second_tablets as ST             # THE EDGE: blessing_of_moses -> second_tablets CALL, reference (10:6 Aaron died there and was buried there — Levi's tribe; Sotah 14a's burying the dead the callee's row on 34:6, cited never read)
import cold_run_incense_shekel as IS             # THE EDGE: blessing_of_moses -> incense_shekel CALL, reference (Exodus 30:7-8 the continual incense — 33:10's incense before You; 30:13 the half-shekel — Shekalim 1:1 at 352:14)
import cold_run_balak as BK                      # THE EDGE: blessing_of_moses -> balak CALL, reference (Numbers 23:22, 24:8's wild ox — 33:17's horns; 23:9's 'a people that dwells alone' — 33:28, the Sifrei 356:5; 23:24's lioness — 33:20; 25's Zimri — 349:1)
import cold_run_opening_speech as OS             # THE EDGE: blessing_of_moses -> opening_speech CALL, reference (2:8's Seir — 33:2's stations; Numbers 27:20's splendor — 33:17's majesty; the commission's debit OPEN to 34:1-4)
import cold_run_refuge_war_family as RW          # THE EDGE: blessing_of_moses -> refuge_war_family CALL, reference (21:5's 'by their word shall every controversy be' — 33:10's teaching; 351:1 every ruling from the Levites' mouth)
import cold_run_courts_prophet as CP             # THE EDGE: blessing_of_moses -> courts_prophet CALL, reference (17:8-11's high court at the place — 33:10's teaching; 352:6's sanctuary higher than the world with 17:8 at 33:12)
import cold_run_festivals_judges as FJ           # THE EDGE: blessing_of_moses -> festivals_judges CALL, reference (16:16's three times — 33:18's Issachar 'to make the times of the festivals in Jerusalem' (Onkelos); Rosh Hashanah 2:8-9 the cases)
import cold_run_good_land as GL                  # THE EDGE: blessing_of_moses -> good_land CALL, reference (8:8's olive oil — 33:24's foot in oil; 8:9's hills of brass — 33:25's iron and brass; the receipt finder [] over 33)
import cold_run_blessing_and_curse as BC         # THE EDGE: blessing_of_moses -> blessing_and_curse CALL, reference (11:14's rain in its season — 33:28's dew and 33:13's dew of heaven; 356:8's dew with 32:2's four rains)
import cold_run_release_firstborn as RL          # THE EDGE: blessing_of_moses -> release_firstborn CALL, reference (15:7's poor law — MOSES' RIGHTEOUSNESS at 33:21, the Sifrei 355:9: hand_opening_commanded on Israel)
import cold_run_persons_poor_court as PP         # THE EDGE: blessing_of_moses -> persons_poor_court CALL, reference (the compiled poor and court laws of 22-25 — 33:21's ordinances with Israel; 355:9-10's righteousness under the throne)
import cold_run_bamidbar as BM                   # THE EDGE: blessing_of_moses -> bamidbar CALL, reference (Numbers 1's census — 33:6's 'let his men be a number', counted 22 on the world; 33:17's myriads; the Levites' strip — 352:10)
import cold_run_naso as NS                       # THE EDGE: blessing_of_moses -> naso CALL, reference (Numbers 6's nazirite — 33:16's 'separate' THE HOMOGRAPH named at 353:8, FALSE for the nazirite's law)
import cold_run_korach as KO                     # THE EDGE: blessing_of_moses -> korach CALL, reference (Numbers 16's Korah the riser — 33:11's loins smitten, 352:1-4; 18's gifts and tithe — the Levites' portion unmoved)
import cold_run_vestments as VE                  # THE EDGE: blessing_of_moses -> vestments CALL, reference (Exodus 28:30's breastplate of judgment with the Urim and the Thummim — 33:8's one Torah seat of wearing)
import cold_run_priesthood as PR                 # THE EDGE: blessing_of_moses -> priesthood CALL, reference (Leviticus 21:11's high priest 'to his father and to his mother' — 33:9's one phrase; the priests' altar service — 33:10)
import cold_run_zelophehad as ZE                 # THE EDGE: blessing_of_moses -> zelophehad CALL, reference (Numbers 27:20's 'put of your splendor upon him' — 33:17's majesty, 353:9; Moses to Joshua the handing — Avot 1:1 at 33:4)
import cold_run_second_census as SC2             # THE EDGE: blessing_of_moses -> second_census CALL, reference (Numbers 26's second count — Reuben's number at 33:6; no number line here)
import cold_run_borders as BR                    # THE EDGE: blessing_of_moses -> borders CALL, reference (Numbers 34's borders — 33:23's sea and south, 33:19's seas; Onkelos's Gennesar 355:14-17)
import cold_run_place_name as PN                 # THE EDGE: blessing_of_moses -> place_name CALL, reference (12:5's place chosen 'in one of your tribes' — 33:12's sanctuary between Benjamin's shoulders: the strip, Zevachim 118b, 352:10's dispute the OPEN parameter; 12:2's high places — 33:29 FALSE)
import cold_run_obey_horeb as OH                 # THE EDGE: blessing_of_moses -> obey_horeb CALL, reference (4:44's frame 'and this is the law' — 33:1's frame five in order; 4:35, 4:39's creed — 33:26's 'none like'; 4:26's 'destroy' — 33:27)
import cold_run_seven_nations as SN              # THE EDGE: blessing_of_moses -> seven_nations CALL, reference (7:1-2's seven nations destroyed — 33:27's enemy driven out, 356:3's two fates; 7:6-7's chose you — 33:3's love)
import cold_run_hear_o_israel as HI              # THE EDGE: blessing_of_moses -> hear_o_israel CALL, reference (6:16's Massah inside the book — 33:8; 6:4's creed — 33:26's 'none like the God of Jeshurun')
import cold_run_moadim as MD                     # THE EDGE: blessing_of_moses -> moadim CALL, reference (Leviticus 23's appointed seasons — 33:18's festivals' times, Onkelos's; the registry's festival_dates unmoved)
import cold_run_offerings as OF                  # THE EDGE: blessing_of_moses -> offerings CALL, reference (Leviticus 1's burnt offering — 33:10's whole offering, 351:3-4's limbs; the peace offerings — 33:19's sacrifices of righteousness)
import cold_run_firstfruits_ebal_curses as FE    # THE EDGE: blessing_of_moses -> firstfruits_ebal_curses CALL, reference (27's stones on Ebal in seventy tongues — Sotah 7:5 the case at 343:5; six_tribes_on_gerizim_to_bless, six_tribes_on_ebal_for_the_curse unmoved)
import cold_run_shelach as SHL                   # THE EDGE: blessing_of_moses -> shelach CALL, reference (Numbers 13-14 the spies — 350:3's covenant kept 'at the spies'; 14:17's pointer on the chapter's words the recon found)
import cold_run_journeys as JR                   # THE EDGE: blessing_of_moses -> journeys CALL, reference (Numbers 33's stations — 33:2's Seir and Paran; 33:38-40 Aaron's death the retelling that never writes)
import cold_run_midian as MI                     # THE EDGE: blessing_of_moses -> midian CALL, reference (Numbers 25 and 31 — 349:1's Simeon borrowed again at Zimri: Simeon under Judah the DATA row, no write on simeon)
import cold_run_mamre as MA                      # THE EDGE: blessing_of_moses -> mamre CALL, reference (Genesis 15:1's 'I am your shield' — 33:29's shield of your help, shield_promised on abraham; 22:14's house seen — 352:9)
import cold_run_pre_sinai as PS                  # THE EDGE: blessing_of_moses -> pre_sinai CALL, reference (Genesis 9's sons of Noah — the seven commandments the nations refused, 343:6; Tosefta Avodah Zarah 9:4 the case)

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
def W33(v): return words('Deut', 33, v)
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
NAME = (_G('יהוה (the LORD)'), _G('ליהוה (to the LORD)'), _G('ויהוה (and the LORD)'), _G('ביהוה (in YHWH)'), _G('מיהוה (from the LORD)'))   # (the LORD; to the LORD; and the LORD; in the LORD; from the LORD)
import difflib
def SH(a, b_): return sum(s for _, _, s in difflib.SequenceMatcher(a=words(*a), b=words(*b_)).get_matching_blocks())   # the reading's shared-run measure
CHS = (33,)
NV = {c: len({v for (b, cc, v) in by if b == 'Deut' and cc == c}) for c in CHS}; assert NV == {33: 29}, NV   # twenty-nine verses (the reading's divisions assert — the identity)
TOKN = {c: sum(len(W(c, v)) for v in range(1, NV[c] + 1)) for c in CHS}
print('THE TOKENS (printed before they are asserted):', TOKN)
TOKN_EXPECTED = {33: 336}   # typed from the first derive's print (the callees' way — printed before typed)
if TOKN_EXPECTED: assert TOKN == TOKN_EXPECTED, (TOKN, TOKN_EXPECTED)
SPAN = [(33, v) for v in range(1, 30)]
assert len(SPAN) == 29

P_ = []   # the provenance trail of the case being run
def ink(ref, note):  P_.append(('INK',  'Deut %s — %s' % (ref, note) if not ref[:1].isupper() else '%s — %s' % (ref, note)))
def move(src, note): P_.append(('MOVE', '%s — %s' % (src, note)))
def dat(note):       P_.append(('DATA', note))
def hyp(note):       P_.append(('HYP',  note))     # THE LINK REVIEW LAW: a hypothesis — no teacher; counted apart, never as compiled
def out(verdict, effects):
    """verdict + registry-validated effects (the engine contract)"""
    FX.validate([e for e in effects if e != FX.NONE])
    return verdict, effects, list(P_)

# ---- THE INK, computed (the parser and the tokens; the reading's facts the expectations — every assert PROVEN at the reading, ch33_ink.py — COPIED from the reading's instrument by content markers in six blocks; the store-, shelf-, Onkelos- and register-bound asserts left to the reading; the parser's facts typed from the measure's print as the ink instrument asserted them) ----
def MARKS(c, v): return [t for t in verse_words('Deut', c, v) if t[-1] in '#~^%@|*']
PARSE = {(c, v): (ink_numbers(verse_words('Deut', c, v)), ink_ordinals(verse_words('Deut', c, v)), MARKS(c, v)) for (c, v) in SPAN}
NUMV = [k for k in PARSE if PARSE[k][0]]; ORDV = [k for k in PARSE if PARSE[k][1]]; STARV = [k for k in PARSE if PARSE[k][2]]
print('THE INK (printed before it is asserted): PARSE %s, NUMV %s, ORDV %s, STARV %s, TOKN %s' % ({k: p for k, p in PARSE.items() if p[0] or p[1] or p[2]}, NUMV, ORDV, STARV, TOKN))
assert {k: p for k, p in PARSE.items() if p[0] or p[1] or p[2]} == {(33, 23): ([], [], [_G('שבע* (sated, the consonants of seven)')])}, {k: p for k, p in PARSE.items() if p[0] or p[1] or p[2]}   # the reading's parser assert (ch33_ink.py from ch33_measure_lean.out): 33:23 THE FALSE SEVEN (sated with favor) MARKED, NOT COUNTED — no number in the chapter
assert NUMV == [] and ORDV == [] and STARV == [(33, 23)]
FALSE_SEVEN = W(33, 23)[3]; assert FALSE_SEVEN == _G('שבע (sated, the consonants of seven)') and W(33, 23)[0:3] == [_G('ולנפתלי (and to Naphtali)'), _G('אמר (he said)'), _G('נפתלי (Naphtali)')] and W(33, 23)[4:6] == [_G('רצון (delight)'), _G('ומלא (and full)')]   # (sated — seven's consonants, an adjective: of Naphtali he said, Naphtali sated with favor and full) — the parser's one mark, a DATA row
NEG = {(c, v): [x for x in W(c, v) if x in NEG_T] for (c, v) in SPAN if any(x in NEG_T for x in W(c, v))}
NAME_BARE = sum(1 for (c, v) in SPAN for x in W(c, v) if x == _G('יהוה (the LORD)'))   # (the LORD)
print('THE NEGATIONS AND THE NAME (printed before they are asserted):', NEG, NAME_BARE)
NAME_BARE_EXPECTED = 7   # typed from the first derive's print
if NAME_BARE_EXPECTED: assert NAME_BARE == NAME_BARE_EXPECTED, (NAME_BARE, NAME_BARE_EXPECTED)
NEG_EXPECTED = {'33:9': 3}   # the negations per verse, typed from the first derive's print
if NEG_EXPECTED: assert {'%d:%d' % k: len(v) for k, v in NEG.items()} == NEG_EXPECTED, {'%d:%d' % k: len(v) for k, v in NEG.items()}
assert [f'{c}:{v}' for c, v in SPAN if _G('לאמר (saying)') in W(c, v)] == [] and [(c, v) for c, v in SPAN if _G('אם (if)') in W(c, v)] == [] and [(c, v, x) for c, v in SPAN for x in W(c, v) if x == _G('פן (lest)')] == [] and [(c, v) for c, v in SPAN if _G('לא (not)') in W(c, v)] == [(33, 9)]   # ("saying" — none; "if" — none; "lest" — none; "not" — 33:9 alone, thrice) — the reading's frames assert
assert [(v, x) for c, v in SPAN for x in W(c, v) if x in (_G('אמר (he said)'), _G('ויאמר (and he said)'))] == [(2, _G('ויאמר (and he said)')), (7, _G('ויאמר (and he said)')), (8, _G('אמר (he said)')), (12, _G('אמר (he said)')), (13, _G('אמר (he said)')), (18, _G('אמר (he said)')), (20, _G('אמר (he said)')), (22, _G('אמר (he said)')), (23, _G('אמר (he said)')), (24, _G('אמר (he said)')), (27, _G('ויאמר (and he said)'))]   # ("he said" eleven — nine tribal frames, 33:2's theophany and 33:27's "destroy"; Reuben unframed)
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
# THE KIN BY COMPUTATION: the frame's kin 4:44 ("and this is the law which Moses set before the children of Israel" — five in order with 33:1's "and this is the blessing"); JOSEPH'S BLESSING IS JACOB'S — 33:16 five in order with Genesis 49:26 (the head of Joseph, the crown of him separate from his brethren), 33:13 with Genesis 49:25 (the deep that couches beneath); 33:15 with Habakkuk 3:6 (the everlasting hills — the Prophets' seat cited, never read); 33:22's lion's whelp Judah's (Genesis 49:9); two verses share no two tokens with any verse (33:11 the loins smitten, 33:14 the sun and the moons)
assert [v for c, v in SPAN if not KINC[(c, v)]] == [11, 14], [v for c, v in SPAN if not KINC[(c, v)]]
assert KINC[(33, 1)][0] == ('Deut 4:44', 5, 5) and KINC[(33, 16)][0] == ('Gen 49:26', 5, 5) and KINC[(33, 13)][0] == ('Gen 49:25', 3, 3) and KINC[(33, 15)][0] == ('Hab 3:6', 3, 3) and KINC[(33, 22)][0] == ('Gen 49:9', 2, 2) and KINC[(33, 5)][0] == ('Ezra 4:3', 4, 1) and KINC[(33, 21)][0] == ('1Chr 11:10', 3, 4) and KINC[(33, 28)][0] == ('2Kgs 18:32', 3, 4) and KINC[(33, 29)][0] == ('1Kgs 1:20', 3, 3) and KINC[(33, 4)][0] == ('Josh 17:4', 3, 2), (KINC[(33, 1)][0], KINC[(33, 16)][0], KINC[(33, 13)][0])
assert KINC[(33, 3)] == [('Deut 33:17', 2, 2), ('Ps 96:10', 2, 2)] and KINC[(33, 12)][0] == ('Deut 33:20', 2, 2) and KINC[(33, 18)] == [('Esth 5:14', 2, 2)] and KINC[(33, 2)][0] == ('1Chr 11:2', 2, 3), (KINC[(33, 3)], KINC[(33, 12)][0], KINC[(33, 18)])
# THE TWINS DIFFED (shared / the longest run): Joseph's crown 33:16 five in order with Genesis 49:26; the deep 33:13 with Genesis 49:25; the everlasting hills 33:15 with Habakkuk 3:6; Mount Paran 33:2 with Habakkuk 3:3; "Moses the man of God" 33:1 with Joshua 14:6 (the Prophets' seat cited, never read); the waters of Meribah 33:8 with Numbers 20:13; Levi's father and mother 33:9 with the high priest's (Leviticus 21:11); THE TWINS BY SENSE WITH NO SHARED TOKEN — Jeshurun 33:5 (prefixed) with 32:15, the dew 33:28 with 32:2, Benjamin 33:12 with Genesis 49:27, Reuben 33:6 with Genesis 49:4, Asher 33:24 with Genesis 49:20, the lawgiver's portion 33:21 with Numbers 32:33 and 34:6
assert SHARED(('Deut', 33, 16), ('Gen', 49, 26)) == [_G('לראש (to head)'), _G('יוסף (Joseph)'), _G('ולקדקד (and to crown of the head)'), _G('נזיר (separate)'), _G('אחיו (his brethren)')] and SHN(('Deut', 33, 16), ('Gen', 49, 26)) == 5 and SHARED(('Deut', 33, 13), ('Gen', 49, 25)) == [_G('רבצת (crouch)'), _G('תחת (under)')] and SHN(('Deut', 33, 13), ('Gen', 49, 25)) == 3 and SHARED(('Deut', 33, 15), ('Hab', 3, 6)) == [_G('גבעות (hillock)'), _G('עולם (forever)')] and SHN(('Deut', 33, 15), ('Hab', 3, 6)) == 3 and SHARED(('Deut', 33, 2), ('Hab', 3, 3)) == [_G('מהר (from mountain)'), _G('פארן (Paran)')]   # on the head of Joseph, the crown of him separate from his brethren; couches beneath; the everlasting hills; from Mount Paran
assert SHARED(('Deut', 33, 1), ('Josh', 14, 6)) == [_G('משה (Moses)'), _G('איש (man)'), _G('האלהים (God)')] and SHN(('Deut', 33, 1), ('Josh', 14, 6)) == 4 and SHARED(('Deut', 33, 1), ('Gen', 49, 28)) == [_G('וזאת (and this)')] and SHN(('Deut', 33, 1), ('Gen', 49, 28)) == 3 and SHARED(('Deut', 33, 1), ('Deut', 4, 44)) == SHARED(('Deut', 33, 1), ('Deut', 4, 44)) and SHARED(('Deut', 33, 8), ('Num', 20, 13)) == [_G('מי (who)'), _G('מריבה (Meribah)')] and SHARED(('Deut', 33, 8), ('Deut', 6, 16)) == [_G('במסה (at Massah)')] and SHARED(('Deut', 33, 9), ('Lev', 21, 11)) == [_G('לאביו (to father him or its)'), _G('ולאמו (and to mother him or its)'), _G('לא (not)')] and SHN(('Deut', 33, 9), ('Lev', 21, 11)) == 3   # Moses the man of God; and this; the waters of Meribah; at Massah; to his father and to his mother not
assert SHARED(('Deut', 33, 22), ('Gen', 49, 9)) == [_G('גור (whelp)'), _G('אריה (lion)')] and SHARED(('Deut', 33, 19), ('Ps', 4, 6)) == [_G('זבחי (sacrifices of)'), _G('צדק (righteousness)')] and SHARED(('Deut', 33, 17), ('Gen', 48, 20)) == [_G('אפרים (Ephraim)')] and SHN(('Deut', 33, 17), ('Gen', 48, 20)) == 2 and SHARED(('Deut', 33, 29), ('Gen', 15, 1)) == [_G('מגן (shield)')] and SHN(('Deut', 33, 29), ('Gen', 15, 1)) == 2 and SHARED(('Deut', 33, 26), ('Deut', 32, 15)) == [_G('ישרון (Jeshurun)')] and SHARED(('Deut', 33, 28), ('Gen', 27, 28)) == [_G('דגן (increase)')]   # a lion's whelp; sacrifices of righteousness; Ephraim; a shield; Jeshurun; corn
assert SHARED(('Deut', 33, 6), ('Gen', 49, 3)) == [_G('ראובן (Reuben)')] and SHARED(('Deut', 33, 7), ('Gen', 49, 8)) == [_G('יהודה (Judah)')] and SHARED(('Deut', 33, 18), ('Gen', 49, 13)) == [_G('זבולן (Zebulun)')] and SHARED(('Deut', 33, 20), ('Gen', 49, 19)) == [_G('גד (Gad)')] and SHARED(('Deut', 33, 22), ('Gen', 49, 17)) == [_G('דן (Daniel)')] and SHARED(('Deut', 33, 23), ('Gen', 49, 21)) == [_G('נפתלי (Naphtali)')]   # Jacob's blessing shares each tribe's NAME alone — Reuben, Judah, Zebulun, Gad, Dan, Naphtali
assert SHN(('Deut', 33, 5), ('Deut', 32, 15)) == 0 and SHN(('Deut', 33, 28), ('Deut', 32, 2)) == 0 and SHN(('Deut', 33, 12), ('Gen', 49, 27)) == 0 and SHN(('Deut', 33, 6), ('Gen', 49, 4)) == 0 and SHN(('Deut', 33, 24), ('Gen', 49, 20)) == 0 and SHN(('Deut', 33, 21), ('Num', 32, 33)) == 0 and SHN(('Deut', 33, 21), ('Deut', 34, 6)) == 0 and SHN(('Deut', 33, 29), ('Deut', 32, 13)) == 1 and SHN(('Deut', 33, 17), ('Gen', 48, 19)) == 0 and SHN(('Deut', 33, 27), ('Ps', 90, 1)) == 0
# THE FORMULAS (phrase seats by consonants over the Torah and the Bible): THIRTY-EIGHT phrases of the blessing ONCE in the Bible (computed over the measure's list, the count read from its print); THE FIERY LAW'S KETIV IS ASHDOTH'S WORD (eshdat — the slopes of Pisgah at 3:17 and 4:49; the qere's two words nowhere); Jeshurun 32:15 and 33:26 (33:5 prefixed); "before his death" Isaac's and Jacob's (Genesis 27:10, 50:16); Massah 6:16; the waters of Meribah Numbers 20:13 (and two psalms); "separate from his brethren" Genesis 49:26 alone; "a lion's whelp" Judah's (Genesis 49:9); "as a lioness" Balaam's (Numbers 23:24); "the heads of the people" 33:5 and 33:21; "destroy" 4:26's word; Isaac's "corn and wine" defective, 33:28's full; THE CHAPTER NEVER SAYS "THE LORD YOUR GOD" (192 seats in the Torah, none here — as the song)
Q33 = [(_G('וזאת (and this)'), _G('הברכה (the benediction)')), (_G('מסיני (from Sinai)'), _G('בא (come or bring)')), (_G('מרבבת (from abundance)'), _G('קדש (holiness)')), (_G('חבב (hide)'), _G('עמים (people)')), (_G('קדשיו (sacred him or its)'), _G('בידך (in hand you or your)')), (_G('תורה (precept)'), _G('צוה (command)'), _G('לנו (to us or our)'), _G('משה (Moses)')), (_G('מורשה (possession)'), _G('קהלת (assemblage)'), _G('יעקב (Jacob)')), (_G('בישרון (in Jeshurun)'), _G('מלך (king)')), (_G('יחד (unit)'), _G('שבטי (scion)'), _G('ישראל (Israel)')), (_G('יחי (live)'), _G('ראובן (Reuben)'), _G('ואל (and not)'), _G('ימת (die)')), (_G('תמיך (perfections you or your)'), _G('ואוריך (and Urim you or your)')), (_G('שמרו (keep or guard)'), _G('אמרתך (something said you or your)')), (_G('יורו (flow as water)'), _G('משפטיך (judgment you or your)'), _G('ליעקב (to Jacob)')), (_G('קטורה (perfume)'), _G('באפך (in nose you or your)')), (_G('ידיד (loved)'), _G('יהוה (the LORD)')), (_G('ומתהום (and from deep)'), _G('רבצת (crouch)'), _G('תחת (under)')), (_G('הררי (mountain)'), _G('קדם (front)')), (_G('שכני (reside)'), _G('סנה (bramble)')), (_G('רבבות (abundance)'), _G('אפרים (Ephraim)')), (_G('אלפי (thousand)'), _G('מנשה (Manasseh)')), (_G('שפע (resources)'), _G('ימים (seas)')), (_G('חלקת (smoothness)'), _G('מחקק (hack)')), (_G('צדקת (rightness)'), _G('יהוה (the LORD)')), (_G('שבע (sated, the consonants of seven)'), _G('רצון (delight)')), (_G('ים (seas)'), _G('ודרום (and south)')), (_G('וטבל (and dip)'), _G('בשמן (in oil)'), _G('רגלו (foot him or its)')), (_G('וכימיך (and like day you or your)'),), (_G('אין (there is not)'), _G('כאל (like God)'), _G('ישרון (Jeshurun)')), (_G('רכב (ride)'), _G('שמים (heavens)')), (_G('אלהי (the God of)'), _G('קדם (front)')), (_G('זרעת (arm)'), _G('עולם (forever)')), (_G('עין (eye)'), _G('יעקב (Jacob)')), (_G('יערפו (droop)'), _G('טל (dew)')), (_G('אשריך (happiness you or your)'), _G('ישראל (Israel)')), (_G('מי (who)'), _G('כמוך (like you)')), (_G('עם (the people)'), _G('נושע (be open)'), _G('ביהוה (in YHWH)')), (_G('מגן (shield)'), _G('עזרך (aid you or your)')), (_G('חרב (drought)'), _G('גאותך (arrogance you or your)')), (_G('על (on)'), _G('במותימו (elevation them or their)'), _G('תדרך (tread)'))]   # the measure's list (the names in its print): and this is the blessing … tread upon their high places — thirty-nine phrases, thirty-eight once in the Bible ("who is like you" four times)
ONCE = [seq for seq in Q33 if len(P(*seq, books=None)) == 1 and P(*seq, books=None)[0].startswith('Deut 33:')]
assert len(Q33) == 39 and len(ONCE) == 38 and [seq for seq in Q33 if seq not in ONCE] == [(_G('מי (who)'), _G('כמוך (like you)'))] and P(_G('מי (who)'), _G('כמוך (like you)'), books=None) == ['Deut 33:29', 'Ps 35:10', 'Ps 71:19', 'Ps 89:9'], (len(ONCE), [seq for seq in Q33 if seq not in ONCE])   # "who is like you" the one phrase of the list with psalm seats beside
assert P(_G('אשדת (fire law)'), books=None) == ['Deut 33:2', 'Deut 3:17', 'Deut 4:49'] and P(_G('אש (fire)'), _G('דת (law)'), books=None) == [] and _G('אשדת (fire law)') in W(33, 2) and P(_G('ישרון (Jeshurun)'), books=None) == ['Deut 32:15', 'Deut 33:26'] and P(_G('לפני (before)'), _G('מותו (his death)'), books=T) == ['Deut 33:1', 'Gen 27:10', 'Gen 50:16'] and P(_G('במסה (at Massah)'), books=None) == ['Deut 33:8', 'Deut 6:16'] and P(_G('מי (who)'), _G('מריבה (Meribah)'), books=T) == ['Deut 33:8', 'Num 20:13'] and len(P(_G('מי (who)'), _G('מריבה (Meribah)'), books=None)) == 4   # the fiery law's ketiv = Ashdoth; Jeshurun; before his death; at Massah; the waters of Meribah
assert P(_G('נזיר (separate)'), _G('אחיו (his brethren)'), books=None) == ['Deut 33:16', 'Gen 49:26'] and P(_G('גור (whelp)'), _G('אריה (lion)'), books=T) == ['Deut 33:22', 'Gen 49:9'] and len(P(_G('גור (whelp)'), _G('אריה (lion)'), books=None)) == 3 and P(_G('כלביא (as a lioness)'), books=T) == ['Deut 33:20', 'Num 23:24'] and P(_G('ראשי (the heads of)'), _G('עם (the people)'), books=T) == ['Deut 33:21', 'Deut 33:5'] and P(_G('השמד (destroy)'), books=T) == ['Deut 33:27', 'Deut 4:26'] and P(_G('דגן (increase)'), _G('ותירש (and wine, the defective spelling of Genesis 27:28)'), books=None) == ['Gen 27:28'] and _G('ותירוש (and must)') in W(33, 28) and P(_G('גבעות (hillock)'), _G('עולם (forever)'), books=None) == ['Deut 33:15', 'Hab 3:6'] and P(_G('מהר (from mountain)'), _G('פארן (Paran)'), books=None) == ['Deut 33:2', 'Hab 3:3']   # separate from his brethren; a lion's whelp; as a lioness; the heads of the people; destroy; corn and wine; the everlasting hills; from Mount Paran
assert P(_G('איש (man)'), _G('האלהים (God)'), books=T) == ['Deut 33:1'] and len(P(_G('איש (man)'), _G('האלהים (God)'), books=None)) == 60 and len(P(_G('הבשן (Bashan)'), books=T)) == 12 and len(P(_G('יהוה (the LORD)'), _G('אלהיך (your God)'), books=T)) == 192 and len(P(_G('יהוה (the LORD)'), _G('אלהיך (your God)'), books=None)) == 236 and P(_G('ישכן (shall dwell)'), _G('לבטח (in safety)'), books=None) == ['Deut 33:12', 'Jer 23:6', 'Ps 16:9'] and P(_G('זבחי (sacrifices of)'), _G('צדק (righteousness)'), books=None) == ['Deut 33:19', 'Ps 4:6', 'Ps 51:21'] and P(_G('ברזל (iron)'), _G('ונחשת (and copper)'), books=None) == ['2Chr 24:12', 'Deut 33:25'] and len(P(_G('טל (dew)'), books=None)) == 13 and P(_G('טל (dew)'), books=T) == ['Deut 33:28']   # the man of God (sixty in the Bible, once in the Torah); Bashan; the LORD your God; dwell in safety; sacrifices of righteousness; iron and brass; the dew bare once in the Torah
# THE WORDS: the Name SEVEN times bare (33:2, 7, 11, 12, 13, 21, 23) and once with bet (33:29 "saved by the LORD") — never "the LORD your God"; God at 33:1 (the man of God), 33:26 (none like God), 33:27 (the eternal God) — 33:28's "el" the preposition "unto"; eleven tribes named, Simeon absent, and THE PRECIOUS THINGS OF JOSEPH CARRY GAD'S LETTERS (meged at 33:13-16 — five false hits of the tribe scan, a homograph for the compile); the negation "not" thrice at 33:9 alone, the vetitive "let him not" at 33:6; "for" thrice; no "if", "lest" or "saying"; "he said" eleven — nine tribal frames, 33:2's theophany and 33:27's "destroy"
assert [(v, x) for c, v in SPAN for x in W(c, v) if x in (_G('יהוה (the LORD)'), _G('ליהוה (to the LORD)'), _G('ביהוה (in YHWH)'), _G('ויהוה (and the LORD)'))] == [(2, _G('יהוה (the LORD)')), (7, _G('יהוה (the LORD)')), (11, _G('יהוה (the LORD)')), (12, _G('יהוה (the LORD)')), (13, _G('יהוה (the LORD)')), (21, _G('יהוה (the LORD)')), (23, _G('יהוה (the LORD)')), (29, _G('ביהוה (in YHWH)'))] and [(v, x) for c, v in SPAN for x in W(c, v) if x in (_G('אל (to)'), _G('כאל (like God)'), _G('אלוה (God)'), _G('אלהים (God)'), _G('האלהים (God)'), _G('אלהי (the God of)'), _G('אלהיו (his God)'), _G('אלהיהם (their God)'), _G('אלהיך (your God)'))] == [(1, _G('האלהים (God)')), (26, _G('כאל (like God)')), (27, _G('אלהי (the God of)')), (28, _G('אל (to)'))]   # the Name; God — 33:28's "el" is "unto a land"
assert [(v, x) for c, v in SPAN for x in W(c, v) if any(x.endswith(n) for n in (_G('ראובן (Reuben)'), _G('יהודה (Judah)'), _G('לוי (Levi)'), _G('בנימן (Benjamin)'), _G('יוסף (Joseph)'), _G('אפרים (Ephraim)'), _G('מנשה (Manasseh)'), _G('זבולן (Zebulun)'), _G('יששכר (Issachar)'), _G('גד (Gad)'), _G('דן (Daniel)'), _G('נפתלי (Naphtali)'), _G('אשר (which)'), _G('שמעון (Simeon)'))) and x not in (_G('ואשר (and which)'), _G('אשר (which)'), _G('כאשר (as)'), _G('מגד (precious thing, the letters of Gad)'))] == [(6, _G('ראובן (Reuben)')), (7, _G('ליהודה (to Judah)')), (7, _G('יהודה (Judah)')), (8, _G('וללוי (and to Levi)')), (12, _G('לבנימן (to Benjamin)')), (13, _G('וליוסף (and to Joseph)')), (13, _G('ממגד (from distinguished thing)')), (14, _G('וממגד (and from distinguished thing)')), (14, _G('וממגד (and from distinguished thing)')), (15, _G('וממגד (and from distinguished thing)')), (16, _G('וממגד (and from distinguished thing)')), (16, _G('יוסף (Joseph)')), (17, _G('אפרים (Ephraim)')), (17, _G('מנשה (Manasseh)')), (18, _G('ולזבולן (and to Zebulun)')), (18, _G('זבולן (Zebulun)')), (18, _G('ויששכר (and Issachar)')), (20, _G('ולגד (and to Gad)')), (20, _G('גד (Gad)')), (22, _G('ולדן (and to Daniel)')), (22, _G('דן (Daniel)')), (23, _G('ולנפתלי (and to Naphtali)')), (23, _G('נפתלי (Naphtali)')), (24, _G('ולאשר (and to Asher)'))]   # the tribe scan with its five false hits — "from the precious things" (meged) ends in Gad's letters
assert sum(1 for c, v in SPAN for x in W(c, v) if x in (_G('לא (not)'), _G('ולא (and not)'))) == 3 and [(c, v) for c, v in SPAN if any(x in (_G('לא (not)'), _G('ולא (and not)')) for x in W(c, v))] == [(33, 9)] and [(v, x) for c, v in SPAN for x in W(c, v) if x in (_G('אל (to)'), _G('ואל (and not)'))] == [(6, _G('ואל (and not)')), (7, _G('ואל (and not)')), (28, _G('אל (to)'))] and sum(1 for c, v in SPAN for x in W(c, v) if x == _G('כי (for)')) == 3   # not (lo) thrice at 33:9; al at 33:6 the vetitive, at 33:7 and 33:28 the preposition "unto"; for (ki) thrice
assert [(v, x) for c, v in SPAN for x in W(c, v) if x in (_G('אמר (he said)'), _G('ויאמר (and he said)'))] == [(2, _G('ויאמר (and he said)')), (7, _G('ויאמר (and he said)')), (8, _G('אמר (he said)')), (12, _G('אמר (he said)')), (13, _G('אמר (he said)')), (18, _G('אמר (he said)')), (20, _G('אמר (he said)')), (22, _G('אמר (he said)')), (23, _G('אמר (he said)')), (24, _G('אמר (he said)')), (27, _G('ויאמר (and he said)'))]   # "he said" eleven: Judah, Levi, Benjamin, Joseph, Zebulun, Gad, Dan, Naphtali, Asher framed; Reuben unframed after the prologue; Issachar inside Zebulun's; 33:2 the theophany; 33:27 "destroy"
assert (len(W(33, 1)), len(W(33, 2)), len(W(33, 4)), len(W(33, 25)), len(W(33, 29))) == (12, 16, 7, 5, 19) and W(33, 4) == [_G('תורה (precept)'), _G('צוה (command)'), _G('לנו (to us or our)'), _G('משה (Moses)'), _G('מורשה (possession)'), _G('קהלת (assemblage)'), _G('יעקב (Jacob)')] and W(33, 25) == [_G('ברזל (iron)'), _G('ונחשת (and copper)'), _G('מנעליך (bolt you or your)'), _G('וכימיך (and like day you or your)'), _G('דבאך (quiet you or your)')] and W(33, 6) == [_G('יחי (live)'), _G('ראובן (Reuben)'), _G('ואל (and not)'), _G('ימת (die)'), _G('ויהי (and be)'), _G('מתיו (adult him or its)'), _G('מספר (number)')]   # a law Moses commanded us, an inheritance of the congregation of Jacob; iron and brass your bars, as your days your strength; let Reuben live and not die, and let his men be a number
# THE FRAMES, THE REGISTER AND THE PARSER: six imperatives (hear 33:7; bless, smite 33:11; rejoice 33:18; possess 33:23; destroy 33:27) and Reuben's three jussives (let him live, let him not die, let his men be — 33:6); THE CHAPTER NEVER SAYS "THE LORD YOUR GOD"; the register empty; THE PARSER'S ONE MARK — 33:23's "sated" carries seven's consonants and is MARKED, NOT COUNTED (no false number in the chapter; the myriads of 33:2 and 33:17 and the "number" of 33:6 unread — the parser's forms are the cardinal words)
MO = {(c, v): [(x, m) for x, m in by[('Deut', c, v)]] for c, v in SPAN}
assert [(v, x) for c, v in SPAN for x, m in MO[(c, v)] if m and re.search(r'V[a-zA-Z]v', m)] == [(7, _G('שמע (hear)')), (11, _G('ברך (bless)')), (11, _G('מחץ (dash asunder)')), (18, _G('שמח (brighten up)')), (23, _G('ירשה (possess or inherit suffix)')), (27, _G('השמד (destroy)'))] and [(v, x, m) for c, v in SPAN for x, m in MO[(c, v)] if m and re.search(r'V[a-zA-Z]j', m)] == [(6, _G('יחי (live)'), 'HVqj3ms'), (6, _G('ימת (die)'), 'HVqj3ms'), (6, _G('ויהי (and be)'), 'HC/Vqj3ms')] and MO[(33, 2)][0] == (_G('ויאמר (and he said)'), 'HC/Vqw3ms') and MO[(33, 6)][2] == (_G('ואל (and not)'), 'HC/Tn')   # hear, bless, smite, rejoice, possess, destroy; let him live, let him not die, let there be; and he said; and-not (the vetitive particle)
assert [v for v in range(1, 30) if any(a == _G('יהוה (the LORD)') and b == _G('אלהיך (your God)') for a, b in zip(W(33, v), W(33, v)[1:]))] == [] and sum(1 for v in range(1, 30) for x in W(33, v) if x == _G('יהוה (the LORD)')) == 7 and sum(1 for v in range(1, 30) for x in W(33, v) if x == _G('ליהוה (to the LORD)')) == 0 and sum(1 for v in range(1, 30) for x in W(33, v) if x == _G('ביהוה (in YHWH)')) == 1

# ---- THE COUNTER'S DAY (a bare world on the exodus epoch; Moses' last day (40, 12, 7) — 19b's ONE MARKER at 31:1 stands, NO MARKER here; 33:1's 'before his death' THAT day; the death date 19b's clock datum on the calendar's keys, read here) ----
with contextlib.redirect_stdout(io.StringIO()):
    _WC = WE.World(era='Moses\' last day — chapter 33 on a bare world (the exodus epoch)', epoch='exodus')
_EX = _WC.clock.eras['exodus']
def DAY(y, m, d): return _WC.clock.day_in('exodus', y, m, d)
def DATE(day): return _EX.date(day)
MOSES_120 = DAY(40, 12, 7); COUNTER = MOSES_120
CLOCK = {'counter': DATE(COUNTER), 'marker': None, 'marker_verse': None, 'marker_at': None, 'days_walked': 0, 'the_day_by': "19b's marker at Deut 31:1 (the number's verse 31:2) — the_death_date_of_moses on the calendar's keys", 'clock_data': ['the_death_date_of_moses']}
print('THE CLOCK (printed before it is asserted):', CLOCK)
assert CLOCK['counter'] == (40, 12, 7) and CLOCK['marker'] is None and CLOCK['days_walked'] == 0, CLOCK
assert all(k in WE.CAL_PARAMS for k in CLOCK['clock_data']), [k for k in CLOCK['clock_data'] if k not in WE.CAL_PARAMS]   # 19b's calendar parameter on file — the received channel
assert WE.CAL_PARAMS['the_death_date_of_moses']['exercised_by'] == ['covenant_return_charge'], WE.CAL_PARAMS['the_death_date_of_moses']['exercised_by']   # 19b's row UNTOUCHED (add_types_ch33_b.py — the calendar untouched)

# ---- THE ONE DATABASE SCANNED (the holes' ground — nothing names the twenty-eight on their twelve ledgers before this sitting; the references' entities and counts as the recon read them — DO4) ----
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
    """the entries of an effect in ONE full run of the tape (DO4's counts — the running world's): the one database folds several runs' rows under their sources (the checkpoint sections' names); the largest source is a whole run — None where the database is not built"""
    if not _os.path.exists(_WDB): return None
    c_ = sqlite3.connect('file:%s?mode=ro' % _WDB, uri=True)
    src = c_.execute("SELECT source FROM run_ledger GROUP BY source ORDER BY COUNT(*) DESC, source LIMIT 1").fetchone()[0]
    return c_.execute("SELECT COUNT(*) FROM run_ledger WHERE effect=? AND source=?", (effect, src)).fetchone()[0]
OWN28 = ('blessing_given_before_moses_death', 'the_lord_came_from_sinai_seir_paran_declared', 'fiery_law_from_his_right_hand_declared', 'lover_of_the_peoples_holy_ones_in_his_hand_declared', 'law_commanded_the_inheritance_of_jacob_declared', 'king_in_jeshurun_when_the_heads_gathered_declared', 'reuben_to_live_and_not_die_blessed', 'judahs_voice_heard_brought_to_his_people_blessed', 'levi_thummim_and_urim_proved_at_massah_blessed', 'levi_father_and_mother_unseen_covenant_kept', 'levi_teaches_jacob_incense_and_whole_offering', 'levi_substance_blessed_loins_of_his_foes_smitten', 'benjamin_beloved_dwells_in_safety_between_his_shoulders_blessed', 'joseph_land_blessed_with_the_precious_things', 'joseph_the_bush_dweller_favor_on_the_crown_separate_from_his_brethren', 'joseph_firstling_ox_horns_ephraim_myriads_manasseh_thousands', 'zebulun_going_out_issachar_in_tents_blessed', 'peoples_called_to_the_mountain_sacrifices_of_righteousness', 'gad_enlarged_lioness_first_part_lawgivers_portion_blessed', 'gad_came_with_the_heads_righteousness_of_the_lord_executed', 'dan_lions_whelp_leaps_from_bashan_blessed', 'naphtali_sated_with_favor_sea_and_south_blessed', 'asher_blessed_above_sons_foot_dipped_in_oil', 'iron_and_brass_bars_strength_as_your_days_blessed', 'none_like_the_god_of_jeshurun_rider_of_the_heaven_declared', 'eternal_god_dwelling_everlasting_arms_enemy_driven_out_declared', 'israel_dwells_in_safety_alone_fountain_of_jacob_declared', 'happy_are_you_israel_shield_and_sword_high_places_trodden_declared')
assert len(OWN28) == 28 and len(set(OWN28)) == 28
LEDGERS12 = ('israel_people', 'reuben', 'judah', 'levi', 'benjamin', 'joseph', 'zebulun', 'issachar', 'gad', 'dan_son', 'naphtali', 'asher')
HOLE_WORDS = r"^(asher_blessed_above\w*|benjamin_beloved_dwells\w*|blessing_given_before\w*|dan_lions_whelp\w*|eternal_god_dwelling\w*|fiery_law_from\w*|gad_came_with\w*|gad_enlarged_lioness\w*|happy_are_you\w*|iron_and_brass\w*|israel_dwells_in\w*|joseph_firstling_ox\w*|joseph_land_blessed\w*|joseph_the_bush\w*|judahs_voice_heard\w*|king_in_jeshurun\w*|law_commanded_the\w*|levi_father_and\w*|levi_substance_blessed\w*|levi_teaches_jacob\w*|levi_thummim_and\w*|lover_of_the\w*|naphtali_sated_with\w*|none_like_the\w*|peoples_called_to\w*|reuben_to_live\w*|the_lord_came\w*|zebulun_going_out\w*)$"
_hs = {ent: ledger_scan(ent, HOLE_WORDS) for ent in LEDGERS12}; HOLE_SCAN = None if any(v is None for v in _hs.values()) else {ent: [e for e in v if e not in OWN28] for ent, v in _hs.items()}   # this sitting's own names excluded once the fold carries them
KIN47 = ('barred_from_the_land', 'gathered_to_his_people', 'go_up_to_nebo_see_the_land_commanded', 'die_in_the_mountain_gathered_to_your_people_commanded', 'as_aaron_died_in_hor_and_was_gathered', 'see_the_land_from_afar_not_go_there', 'heaven_and_earth_witness', 'blessing_and_curse_set', 'blessings_for_hearing', 'blessed_with_dew_and_fat', 'blessed_the_people', 'counted', 'hand_opening_commanded', 'equal_portions_commanded', 'levites_portion_given', 'inheritance_barred', 'book_of_the_law_beside_the_ark_commanded', 'descended_on_the_mountain', 'doctrine_as_rain_and_dew_likened', 'heavens_good_treasure_opened', 'high_court_at_the_place_commanded', 'high_places_banned', 'incense_continual', 'kings_smitten', 'land_possessed', 'lords_portion_his_people_jacob', 'nations_dispossessed_as_sihon_and_og_promised', 'oral_law_unwritten', 'presence_dwells', 'shield_promised', 'six_tribes_on_ebal_for_the_curse', 'six_tribes_on_gerizim_to_bless', 'substituted_for_the_firstborn', 'torah_through_moses', 'work_of_the_hand_blessed', 'storehouses_blessed', 'firstling_sanctification_commanded', 'grave_marked', 'judah_sent_ahead', 'portion_added', 'levite_forsaking_barred', 'levites_loud_voice_commanded', 'the_lord_alone_led_no_foreign_god', 'song_sung', 'no_share_in_the_world_to_come', 'slain_by_sword', 'priestly_dues_granted')
KIN_EXPECTED = (2, 5, 1, 1, 1, 1, 5, 2, 3, 1, 2, 22, 1, 1, 1, 2, 1, 1, 1, 1, 1, 3, 2, 3, 6, 1, 1, 3, 1, 1, 1, 1, 1, 1, 2, 1, 1, 1, 1, 1, 2, 1, 1, 1, 3, 2, 1)   # DO4 — the recon's and the callees' counts on the running world (ch33b_recon.out section H; ch33_callees.out THE NEAR NAMES; the probe Q50's KIN tuple)
assert len(KIN47) == 47 == len(KIN_EXPECTED)
KIN_COUNTS = {k: count_scan(k) for k in KIN47}
REUSE3 = ()   # NO REUSE this sitting — no effect's own forward seat lies in the chapter (20b had three)
REUSE_BEFORE = {}
REUSE_AFTER = {}
REUSE_COUNTS = {}
SCANS = {k: effect_scan(k) for k in KIN47[:8] + ('garments_transferred_and_aaron_died', 'invested_office', 'demoted', 'scepter_held', 'birthright_transferred', 'scattered_in_israel', 'younger_set_first', 'concubine_lain_with')}
del _hs   # 9b's lesson: the raw scans are the database's state at import — the derived lists are equal on the cached and the full load
_FXV = yaml.safe_load(open(_os.path.join(HERE, 'effect_vocabulary.yaml'), encoding='utf-8'))['effects']
print('THE SCANS (printed before they are asserted): holes %s; the kin counts %s; the reuses %s; the entities %s' % (HOLE_SCAN, KIN_COUNTS, REUSE_COUNTS, SCANS))
assert HOLE_SCAN is None or all(v == [] for v in HOLE_SCAN.values()), HOLE_SCAN   # THE HOLES' GROUND — nothing on the twelve ledgers named the twenty-eight before this sitting (DO4)
assert all(v is None for v in KIN_COUNTS.values()) or tuple(KIN_COUNTS.values()) == KIN_EXPECTED, [(k, KIN_COUNTS[k], e) for k, e in zip(KIN47, KIN_EXPECTED) if KIN_COUNTS[k] != e]   # the references' counts as the recon read them (DO4 — no second write)
SCANS_EXPECTED = {'barred_from_the_land': ['aaron', 'moses'], 'gathered_to_his_people': ['aaron', 'abraham', 'isaac', 'ishmael', 'jacob'], 'go_up_to_nebo_see_the_land_commanded': ['moses'], 'die_in_the_mountain_gathered_to_your_people_commanded': ['moses'], 'as_aaron_died_in_hor_and_was_gathered': ['moses'], 'see_the_land_from_afar_not_go_there': ['moses'], 'heaven_and_earth_witness': ['israel_people'], 'blessing_and_curse_set': ['israel_people'], 'garments_transferred_and_aaron_died': [], 'invested_office': ['aaron-and-sons', 'eleazar_son_of_aaron', 'pinchas', 'the-firstborn', 'the_levites', 'yehoshua'], 'demoted': ['reuben'], 'scepter_held': ['judah'], 'birthright_transferred': ['jacob', 'joseph'], 'scattered_in_israel': ['levi', 'simeon'], 'younger_set_first': ['ephraim'], 'concubine_lain_with': ['reuben']}   # the entities per effect — typed from the first derive's print (the callees' way — printed before typed)
if SCANS_EXPECTED and any(v is not None for v in SCANS.values()): assert SCANS == SCANS_EXPECTED, [(k, SCANS[k], SCANS_EXPECTED.get(k)) for k in SCANS if SCANS[k] != SCANS_EXPECTED.get(k)]
assert all(k in _FXV for k in OWN28) and sum(1 for k in OWN28 if _FXV[k]['ledger_op'] == 'block') == 0 and sum(1 for k in OWN28 if _FXV[k]['ledger_op'] == 'status') == 28 and sum(1 for k in OWN28 if _FXV[k]['ledger_op'] == 'heaven') == 0, 'the twenty-eight on the registry (add_types_ch33_a.py)'
assert _FXV['barred_from_the_land']['ledger_op'] == 'heaven' and _FXV['gathered_to_his_people']['ledger_op'] == 'status' and _FXV['shield_promised']['ledger_op'] in ('status', 'heaven') and _FXV['blessed_with_dew_and_fat']['ledger_op'] in ('status', 'heaven'), 'the referenced rows\' ops (read from the registry\'s print at the types)'
# THE TWINS DIFFED on the DB (the reading's kin asserts read again here — DO4; the shared run SH)
TWIN = {'33:16 vs Gen 49:26': SH(DV(33, 16), ('Gen', 49, 26)), '33:13 vs Gen 49:25': SH(DV(33, 13), ('Gen', 49, 25)), '33:15 vs Hab 3:6': SH(DV(33, 15), ('Hab', 3, 6)), '33:2 vs Hab 3:3': SH(DV(33, 2), ('Hab', 3, 3)), '33:1 vs Josh 14:6': SH(DV(33, 1), ('Josh', 14, 6)), '33:1 vs 4:44': SH(DV(33, 1), DV(4, 44)),
        '33:1 vs Gen 27:10': SH(DV(33, 1), ('Gen', 27, 10)), '33:8 vs Num 20:13': SH(DV(33, 8), ('Num', 20, 13)), '33:8 vs Exod 17:7': SH(DV(33, 8), ('Exod', 17, 7)), '33:9 vs Lev 21:11': SH(DV(33, 9), ('Lev', 21, 11)), '33:5 vs 32:15': SH(DV(33, 5), DV(32, 15)), '33:28 vs 32:2': SH(DV(33, 28), DV(32, 2)),
        '33:12 vs Gen 49:27': SH(DV(33, 12), ('Gen', 49, 27)), '33:6 vs Gen 49:4': SH(DV(33, 6), ('Gen', 49, 4)), '33:6 vs Gen 49:3': SH(DV(33, 6), ('Gen', 49, 3)), '33:7 vs Gen 49:8': SH(DV(33, 7), ('Gen', 49, 8)), '33:24 vs Gen 49:20': SH(DV(33, 24), ('Gen', 49, 20)), '33:21 vs Num 32:33': SH(DV(33, 21), ('Num', 32, 33)),
        '33:22 vs Gen 49:9': SH(DV(33, 22), ('Gen', 49, 9)), '33:17 vs Gen 48:20': SH(DV(33, 17), ('Gen', 48, 20)), '33:17 vs Num 27:20': SH(DV(33, 17), ('Num', 27, 20)), '33:29 vs Gen 15:1': SH(DV(33, 29), ('Gen', 15, 1)), '33:28 vs Num 23:9': SH(DV(33, 28), ('Num', 23, 9)), '33:28 vs Gen 27:28': SH(DV(33, 28), ('Gen', 27, 28)),
        '33:26 vs 4:35': SH(DV(33, 26), DV(4, 35)), '33:29 vs 32:13': SH(DV(33, 29), DV(32, 13)), '33:19 vs Ps 4:6': SH(DV(33, 19), ('Ps', 4, 6)), '33:4 vs 31:9': SH(DV(33, 4), DV(31, 9)), '33:16 vs Exod 3:2': SH(DV(33, 16), ('Exod', 3, 2)), '33:27 vs 7:2': SH(DV(33, 27), DV(7, 2)),
        '33:23 vs Gen 49:21': SH(DV(33, 23), ('Gen', 49, 21)), '33:20 vs Gen 49:19': SH(DV(33, 20), ('Gen', 49, 19)), '33:18 vs Gen 49:13': SH(DV(33, 18), ('Gen', 49, 13)), '33:10 vs 21:5': SH(DV(33, 10), DV(21, 5)), '33:10 vs 17:8': SH(DV(33, 10), DV(17, 8)), '33:8 vs Exod 28:30': SH(DV(33, 8), ('Exod', 28, 30)),
        '33:8 vs 6:16': SH(DV(33, 8), DV(6, 16)), '33:12 vs 12:5': SH(DV(33, 12), DV(12, 5)), '33:21 vs 15:7': SH(DV(33, 21), DV(15, 7)), '33:24 vs 8:8': SH(DV(33, 24), DV(8, 8)), '33:25 vs 8:9': SH(DV(33, 25), DV(8, 9)), '33:27 vs Exod 24:5': SH(DV(33, 27), ('Exod', 24, 5)), '33:27 vs Exod 24:11': SH(DV(33, 27), ('Exod', 24, 11))}
print('THE TWINS DIFFED (printed before they are asserted):', TWIN)
TWIN_EXPECTED = {'33:16 vs Gen 49:26': 5, '33:13 vs Gen 49:25': 3, '33:15 vs Hab 3:6': 3, '33:2 vs Hab 3:3': 2, '33:1 vs Josh 14:6': 4, '33:1 vs 4:44': 5, '33:1 vs Gen 27:10': 3, '33:8 vs Num 20:13': 2, '33:8 vs Exod 17:7': 1, '33:9 vs Lev 21:11': 3, '33:5 vs 32:15': 0, '33:28 vs 32:2': 0, '33:12 vs Gen 49:27': 0, '33:6 vs Gen 49:4': 0, '33:6 vs Gen 49:3': 1, '33:7 vs Gen 49:8': 1, '33:24 vs Gen 49:20': 0, '33:21 vs Num 32:33': 0, '33:22 vs Gen 49:9': 2, '33:17 vs Gen 48:20': 2, '33:17 vs Num 27:20': 0, '33:29 vs Gen 15:1': 2, '33:28 vs Num 23:9': 0, '33:28 vs Gen 27:28': 1, '33:26 vs 4:35': 1, '33:29 vs 32:13': 1, '33:19 vs Ps 4:6': 2, '33:4 vs 31:9': 1, '33:16 vs Exod 3:2': 0, '33:27 vs 7:2': 0, '33:23 vs Gen 49:21': 1, '33:20 vs Gen 49:19': 1, '33:18 vs Gen 49:13': 1, '33:10 vs 21:5': 0, '33:10 vs 17:8': 0, '33:8 vs Exod 28:30': 1, '33:8 vs 6:16': 1, '33:12 vs 12:5': 1, '33:21 vs 15:7': 2, '33:24 vs 8:8': 0, '33:25 vs 8:9': 1, '33:27 vs Exod 24:5': 0, '33:27 vs Exod 24:11': 0}
if TWIN_EXPECTED: assert TWIN == TWIN_EXPECTED, [(k, TWIN[k], TWIN_EXPECTED.get(k)) for k in TWIN if TWIN[k] != TWIN_EXPECTED.get(k)]   # typed from the first derive's print (the callees' way — printed before typed)
assert TWIN['33:16 vs Gen 49:26'] >= 5 and TWIN['33:1 vs 4:44'] >= 5 and TWIN['33:13 vs Gen 49:25'] >= 3 and TWIN['33:1 vs Josh 14:6'] >= 3 and TWIN['33:22 vs Gen 49:9'] >= 2, TWIN   # the reading's largest twins (Joseph's crown five in order, the frame five, the deep three, the man of God three, the lion's whelp two)

# ---- THE CALLEES' FACTS (every edge live at the cells that consume them; the values PRINTED at the first pass and ASSERTED from that print at the second — 10b's lesson 2, the callees' way; the q-style cells called with their keys, an absent key printed, never guessed silently; EVERY CALLEE CALLED BY ITS LITERAL NAME `alias.name(` — the dependency gate reads the source, a DATA read is not a live edge (19b's lesson); the bindings ASSIGNMENTS, never a helper writing globals() — 20b's tail lesson, the cache's skip cannot see a globals() write) ----
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
    FACTS_PRINT.append((name, (V(val) if not isinstance(val, dict) else val.get('v', val.get('value'))) if val is not None else None)); return val   # a DATA row's value printed (the first pass printed None for the dicts); F records the fact alone
# song_charge_nebo — the death 32:50 COMMANDED (a STATUS on moses), the event 34:5 AHEAD; the_readback's fifty-two rows the form; Aaron's death the receipt; the summons cell
SC_DEATH = DK(SC, 'moses_death_ahead'); F('SC_DEATH', SC_DEATH); SC_RB = DK(SC, 'the_readback'); F('SC_RB', SC_RB); SC_AARON = DK(SC, 'aarons_death_the_receipt'); F('SC_AARON', SC_AARON)
SC_NEBO = SC.the_summons_to_nebo({'ask': 'die_in_the_mount_where_you_go_up_and_be_gathered_to_your_people'}, DD(SC)); F('SC_NEBO', SC_NEBO); SC_TABLE = SC.the_readback({'ask': 'the_table'}, DD(SC)); F('SC_TABLE', SC_TABLE)
# covenant_return_charge — the song ahead (31:19-30), the death date (19b's marker's day), the three gifts, the song spoken to its end; 31:9's law written and delivered the tape's kind law_written_given (the readback row 33:4)
CR_SONG = CR.the_song_commanded({'ask': 'when_they_eat_and_are_sated_and_grow_fat_and_turn'}, DD(CR)); F('CR_SONG', CR_SONG); CR_SPOKE = CR.the_book_beside_the_ark_and_the_assembly({'ask': 'moses_spoke_the_words_of_this_song_in_the_ears_of_all_the_assembly_to_their_end'}, DD(CR)); F('CR_SPOKE', CR_SPOKE)
CR_AHEAD = DK(CR, 'the_song_ahead'); F('CR_AHEAD', CR_AHEAD); CR_DEATH = DK(CR, 'the_death_date_of_moses'); F('CR_DEATH', CR_DEATH); CR_GIFTS = DK(CR, 'the_three_gifts_and_their_merits'); F('CR_GIFTS', CR_GIFTS)
# gad_reuben — MOSES' GRAVE (Reuben's Nebo, Gad's field — Sotah 13b; the pointer 33:21 -> 34:6), the land east, the deaths ceased, the doubled condition, the charge
GR_GRAVE = DK(GR, 'moses_grave'); F('GR_GRAVE', GR_GRAVE); GR_EAST = DK(GR, 'the_land_east_status'); F('GR_EAST', GR_EAST); GR_CEASED = DK(GR, 'deaths_ceased'); F('GR_CEASED', GR_CEASED)
GR_DOUBLED = GR.the_condition({'ask': 'doubled_condition'}, DD(GR)); F('GR_DOUBLED', GR_DOUBLED); GR_CHARGE = GR.the_acceptance_and_the_charge({'ask': 'the_order_reversed'}, DD(GR)); F('GR_CHARGE', GR_CHARGE)
# joseph — the seventy souls (46:27; the sons' ledgers Genesis 48-49 ride the tape as entries — birthright_transferred, younger_set_first: the kin BY THE LEDGERS), the callee's keys
JO_SEVENTY = JO.seventy('seventy'); F('JO_SEVENTY', JO_SEVENTY); JO_SIXTY_SIX = JO.seventy('sixty_six'); F('JO_SIXTY_SIX', JO_SIXTY_SIX); JO_KEYS = sorted(DD(JO))[:8]; F('JO_KEYS', JO_KEYS)
# family — the testament (49:3-4 Reuben's firstborn and his strength; the couch — Bilhah's seat; the alignment), Isaac's blessing (27:28 the dew and the corn — 33:28's kin Onkelos names)
FA_FIRSTBORN = FA.testament('firstborn_my_strength'); F('FA_FIRSTBORN', FA_FIRSTBORN); FA_COUCH = FA.testament('couch_seats'); F('FA_COUCH', FA_COUCH); FA_ALIGN = FA.testament('firstborn_alignment'); F('FA_ALIGN', FA_ALIGN)
# chukat — the sentence at Meribah (barred_from_the_land on Moses and Aaron — read, not rewritten), the six Meribah seats (33:8 among them), the kiss, the death dates, the succession (ask-style cells — the first pass's print corrected the q-style guess)
CK_SENT = CK.meribah({'ask': 'sentence'}, DD(CK)); F('CK_SENT', CK_SENT); CK_SEATS = CK.meribah({'ask': 'meribah_seats'}, DD(CK)); F('CK_SEATS', CK_SEATS); CK_KISS = CK.meribah({'ask': 'death_by_the_kiss'}, DD(CK)); F('CK_KISS', CK_KISS)
CK_DATES = CK.edom_and_hor({'ask': 'death_dates'}, DD(CK)); F('CK_DATES', CK_DATES); CK_SUCC = CK.edom_and_hor({'ask': 'succession'}, DD(CK)); F('CK_SUCC', CK_SUCC)
# exodus_story — Sinai (the new moon; the treasure's seats), the trials (Massah among them), the birth (the seventh of Adar — Moses' birthday and death day)
ES_SINAI = ES.sinai('new_moon'); F('ES_SINAI', ES_SINAI); ES_TREASURE = ES.sinai('treasure_seats'); F('ES_TREASURE', ES_TREASURE); ES_TRIALS = ES.trials('count_by_exodus'); F('ES_TRIALS', ES_TRIALS); ES_BIRTH = ES.birth('birthday'); F('ES_BIRTH', ES_BIRTH)
# erection — the calf (the molten calf; the sword on the maternal kin — 33:9's RUN CITATION), the presence (the camp's twelve mil)
ER_CALF = ER.calf('molten_calf'); F('ER_CALF', ER_CALF); ER_MIL = ER.presence('twelve_mil'); F('ER_MIL', ER_MIL)
# second_tablets — Aaron died there and was buried there (10:6 — the burial SUPPLIED), walk after His attributes (Sotah 14a's burying the dead — 34:6's row on the callee, cited never read), the place of the death
ST_THERE = ST.the_stations_and_the_death({'ask': 'aaron_died_there'}, DD(ST)); F('ST_THERE', ST_THERE); ST_BURIED = ST.the_stations_and_the_death({'ask': 'and_he_was_buried_there'}, DD(ST)); F('ST_BURIED', ST_BURIED)
ST_WALK = ST.the_stations_and_the_death({'ask': 'walk_after_his_attributes'}, DD(ST)); F('ST_WALK', ST_WALK); ST_PLACE = DK(ST, 'the_place_of_the_death'); F('ST_PLACE', ST_PLACE)
# incense_shekel — the incense (the four named spices — 33:10's incense before You), the shekel (the lifting of the head; the ransom — Shekalim 1:1's proclamation the case at 352:14)
IS_INCENSE = IS.incense('four_named'); F('IS_INCENSE', IS_INCENSE); IS_SHEKEL = IS.shekel('lift_head'); F('IS_SHEKEL', IS_SHEKEL); IS_RANSOM = IS.shekel('ransom'); F('IS_RANSOM', IS_RANSOM)
# balak — the stands (the Most High's knowledge; 23:9's 'a people that dwells alone' — 356:5's three alones; 23:22's wild ox — 33:17's horns; 23:24's lioness — 33:20's), the star
BK_MOST_HIGH = BK.the_stands({'ask': 'most_high_knowledge'}, DD(BK)); F('BK_MOST_HIGH', BK_MOST_HIGH); BK_STAR = DK(BK, 'star_reading'); F('BK_STAR', BK_STAR)
# opening_speech — THE COMMISSION (the mountain, the debit OPEN to 34:1-4, the hand laid, the honor — 33:17's majesty by Numbers 27:20), the bypass (Seir's route — 33:2's stations), the frame
OS_MTN = OS.the_commission({'ask': 'the_mountain'}, DD(OS)); F('OS_MTN', OS_MTN); OS_DEBIT = OS.the_commission({'ask': 'the_debit'}, DD(OS)); F('OS_DEBIT', OS_DEBIT); OS_HAND = OS.the_commission({'ask': 'the_hand_laid'}, DD(OS)); F('OS_HAND', OS_HAND)
OS_HONOR = OS.the_commission({'ask': 'the_honor'}, DD(OS)); F('OS_HONOR', OS_HONOR); OS_ROUTE = OS.the_bypass({'ask': 'the_route'}, DD(OS)); F('OS_ROUTE', OS_ROUTE); OS_FRAME = DK(OS, 'the_frame'); F('OS_FRAME', OS_FRAME)
# refuge_war_family — one witness for any iniquity (19:15), the priests' saying (21:5 — every controversy by their word: 351:1's every ruling from the Levites' mouth)
RW_ONE = RW.the_landmark_and_the_witnesses({'ask': 'one_witness_for_any_iniquity'}, DD(RW)); F('RW_ONE', RW_ONE); RW_SAYING = DK(RW, 'the_priests_saying'); F('RW_SAYING', RW_SAYING)
# courts_prophet — the high court (17:8-11 — the distinguished judge and the three grades; the court at Yavneh and the priests a duty not a condition; the judge of those days)
CP_GRADES = CP.the_high_court({'ask': 'the_distinguished_judge_and_the_three_grades'}, DD(CP)); F('CP_GRADES', CP_GRADES); CP_YAVNEH = CP.the_high_court({'ask': 'the_court_at_yavneh_and_the_priests'}, DD(CP)); F('CP_YAVNEH', CP_YAVNEH)
CP_JUDGE = CP.the_high_court({'ask': 'the_judge_of_those_days'}, DD(CP)); F('CP_JUDGE', CP_JUDGE)
# festivals_judges — the three pilgrimages (16:16 — the three times, who appears), the intercalation (33:18's festivals' times Onkelos's; Rosh Hashanah 2:8-9 the cases)
FJ_TIMES = FJ.the_three_pilgrimages({'ask': 'the_three_times'}, DD(FJ)); F('FJ_TIMES', FJ_TIMES); FJ_WHO = FJ.the_three_pilgrimages({'ask': 'who_appears'}, DD(FJ)); F('FJ_WHO', FJ_WHO); FJ_INTERCAL = DK(FJ, 'the_intercalation'); F('FJ_INTERCAL', FJ_INTERCAL)
# good_land — the growth's list (8:12-13), the seven species' seat (8:8 — 33:24's oil), NO receipt in the chapter (the finder over 33)
GL_GROWTH = GL.take_heed_lest_you_forget({'ask': 'the_growth_list'}, DD(GL)); F('GL_GROWTH', GL_GROWTH); GL_SPECIES = DK(GL, 'the_seven_species_seat'); F('GL_SPECIES', GL_SPECIES); GL_R = GL.receipt_seats(33); F('GL_R', GL_R)
# blessing_and_curse — the land watered by heaven (11:11), the rains' dates (11:14 — 33:28's dew, 33:13's dew of heaven)
BC_DRINKS = BC.the_land_watered_by_heaven({'ask': 'drinks_by_the_rain_of_heaven'}, DD(BC)); F('BC_DRINKS', BC_DRINKS); BC_RAIN = DK(BC, 'rain_dates'); F('BC_RAIN', BC_RAIN)
# release_firstborn — THE POOR LAW of 15:7 (355:9 — Moses' righteousness at 33:21): the needy condition, lend not borrow, the blessing in the land; the hand opened cell by its first ask
RL_NEEDY = DK(RL, 'the_needy_condition'); F('RL_NEEDY', RL_NEEDY); RL_LEND = DK(RL, 'lend_not_borrow'); F('RL_LEND', RL_LEND); RL_BLESS = DK(RL, 'the_blessing_in_the_land'); F('RL_BLESS', RL_BLESS)
RL_HAND = RL.the_hand_opened({'ask': ASKS(RL, 'the_hand_opened')[0]}, DD(RL)); F('RL_HAND', RL_HAND)
# persons_poor_court — the readback of chapters 22-25 (the compiled poor and court laws — 33:21's ordinances with Israel by reference), the olives' forgetting
PP_RB = PP.the_readback({'ask': ASKS(PP, 'the_readback')[0]}, DD(PP)); F('PP_RB', PP_RB); PP_OLIVES = DK(PP, 'the_olives_forgetting'); F('PP_OLIVES', PP_OLIVES)
# bamidbar — the census (the total; counted 22 on the world — 33:6's 'number'), the Levites (the houses — the strip), Aaron not counted
BM_TOTAL = BM.census({'ask': 'total'}, DD(BM)); F('BM_TOTAL', BM_TOTAL); BM_HOUSES = BM.levites({'ask': 'houses'}, DD(BM)); F('BM_HOUSES', BM_HOUSES); BM_AARON = DK(BM, 'aaron_not_counted'); F('BM_AARON', BM_AARON)
# naso — the sotah's conditions (the nazirite's homograph at 33:16 named FALSE), the face lifted (the priestly blessing)
NS_COND = NS.sotah({'ask': 'conditions'}, DD(NS)); F('NS_COND', NS_COND); NS_FACE = DK(NS, 'face_lifted'); F('NS_FACE', NS_FACE)
# korach — the gifts (the Levite's donkey by CALL to bamidbar; the twenty-four gifts), the tithe's recipient (352:1-4's priests rich; the Levites' portion the tape's)
KO_DONKEY = KO.the_gifts({'ask': 'levite_donkey'}, DD(KO)); F('KO_DONKEY', KO_DONKEY); KO_24 = KO.the_gifts({'ask': 'twenty_four'}, DD(KO)); F('KO_24', KO_24); KO_TITHE = DK(KO, 'tithe_recipient'); F('KO_TITHE', KO_TITHE)
# vestments — the breastplate (28:30's Urim's one Torah seat of wearing — 33:8), the ephod's shoulders (33:12's shoulders the ox's, not the ephod's — the ink)
VE_NAME = VE.breastplate('name'); F('VE_NAME', VE_NAME); VE_SHOULDERS = VE.ephod('shoulders'); F('VE_SHOULDERS', VE_SHOULDERS)
# priesthood — the addressees (Leviticus 21 — 21:11's high priest 'to his father and to his mother' one phrase with 33:9), the blemish ladder
PR_ADDR = PR.family('addressees'); F('PR_ADDR', PR_ADDR); PR_AGE = PR.blemish('age_ladder'); F('PR_AGE', PR_AGE)
# zelophehad — the daughters' plea, the inheritance ladder, the tribe transfer's reach (Numbers 27:20's splendor — 33:17's majesty; Avot 1:1's Moses to Joshua at 33:4)
ZE_PLEA = ZE.the_daughters({'ask': 'plea'}, DD(ZE)); F('ZE_PLEA', ZE_PLEA); ZE_COUNSEL = ZE.the_daughters({'ask': 'counsel'}, DD(ZE)); F('ZE_COUNSEL', ZE_COUNSEL); ZE_REACH = DK(ZE, 'tribe_transfer_reach'); F('ZE_REACH', ZE_REACH)
# second_census — the twelve counts (Reuben's second number — 33:6), the land by lot, the thirteen tribes
S2_COUNTS = SC2.the_roll({'ask': 'twelve_counts'}, DD(SC2)); F('S2_COUNTS', S2_COUNTS); S2_LOT = SC2.the_land({'ask': 'by_lot'}, DD(SC2)); F('S2_LOT', S2_LOT); S2_13 = DK(SC2, 'thirteen_tribes'); F('S2_13', S2_13)
# borders — the land of Canaan (34:2), the four sides (33:23's sea and south — Gennesar by Onkelos)
BR_LAND = BR.the_land_and_its_fall({'ask': 'the_land_canaan'}, DD(BR)); F('BR_LAND', BR_LAND); BR_SIDES = DK(BR, 'the_four_sides'); F('BR_SIDES', BR_SIDES)
# place_name — the place chosen (12:5 — in one of your tribes: BENJAMIN'S STRIP the callee's row, Zevachim 118b; the Name pronounced only there), the three commandments of the entry
PN_TRIBES = PN.the_place_chosen({'ask': 'in_one_of_your_tribes'}, DD(PN)); F('PN_TRIBES', PN_TRIBES); PN_NAME = PN.the_place_chosen({'ask': 'the_name_pronounced_only_there'}, DD(PN)); F('PN_NAME', PN_NAME); PN_ENTRY = DK(PN, 'the_three_commandments_of_the_entry'); F('PN_ENTRY', PN_ENTRY)
# obey_horeb — know this day (4:39 — the creed's second seat), no form seen, THE CREED (4:35, 4:39 — 33:26's 'none like'), the witnesses' chain, the second frame (4:44 — 33:1's frame five in order)
OH_KNOW = OH.the_one_god({'ask': 'know_this_day'}, DD(OH)); F('OH_KNOW', OH_KNOW); OH_FORM = OH.no_image({'ask': 'no_form_seen'}, DD(OH)); F('OH_FORM', OH_FORM)
OH_CREED = DK(OH, 'the_creed'); F('OH_CREED', OH_CREED); OH_CHAIN = DK(OH, 'the_witnesses_chain'); F('OH_CHAIN', OH_CHAIN); OH_FRAME = DK(OH, 'the_second_frame'); F('OH_FRAME', OH_FRAME)
# seven_nations — chose you (7:6-7 — 33:3's love of the peoples), the fewest; 7:1-2's seven nations destroyed (33:27's enemy driven out — 356:3's two fates)
SN_CHOSE = SN.the_holy_people({'ask': 'chose_you'}, DD(SN)); F('SN_CHOSE', SN_CHOSE); SN_FEW = SN.the_holy_people({'ask': 'the_fewest'}, DD(SN)); F('SN_FEW', SN_FEW)
# hear_o_israel — the creed (6:4 — hear, O Israel; the LORD is one: 33:26's 'none like the God of Jeshurun'), the creed's terms; 6:16's Massah inside the book
HI_HEAR = HI.the_creed({'ask': 'hear_o_israel'}, DD(HI)); F('HI_HEAR', HI_HEAR); HI_ONE = HI.the_creed({'ask': 'the_lord_is_one'}, DD(HI)); F('HI_ONE', HI_ONE); HI_TERMS = DK(HI, 'the_creed_terms'); F('HI_TERMS', HI_TERMS)
# moadim — the feasts (Leviticus 23 — 33:18's festivals' times in Jerusalem, Onkelos's; the registry's festival_dates unmoved)
MD_SUK = MD.sukkot(); F('MD_SUK', MD_SUK); MD_RH = MD.rosh_hashanah(); F('MD_RH', MD_RH)
# offerings — the peace offering's place (33:19's sacrifices of righteousness), the fat ban (33:10's whole offering the burnt offering's limbs — 351:3-4)
OF_PLACE = OF.dispatch('shelamim')['place']; F('OF_PLACE', OF_PLACE); OF_FAT = OF.fat_inventory('ban'); F('OF_FAT', OF_FAT)
# firstfruits_ebal_curses — the eagle nation (28:49), the things without measure (18b's row), the false six, the first fruits' first ask (26:2 — the stones on Ebal 27:1-8 the same runner: Sotah 7:5's seventy tongues at 343:5)
FE_EAGLE = FE.the_curses_of_the_siege_and_the_exile({'ask': 'a_nation_from_the_end_of_the_earth_as_the_eagle_flies'}, DD(FE)); F('FE_EAGLE', FE_EAGLE); FE_MEASURE = DK(FE, 'the_things_without_measure'); F('FE_MEASURE', FE_MEASURE)
FE_SIX = DK(FE, 'the_false_six'); F('FE_SIX', FE_SIX); FE_FIRST = FE.the_first_fruits({'ask': ASKS(FE, 'the_first_fruits')[0]}, DD(FE)); F('FE_FIRST', FE_FIRST)
# shelach — Hoshea to Joshua (13:16); the spies' going (350:3's covenant kept 'at the spies')
SH_NAME = SHL.spies({'ask': 'joshua_name'}, DD(SHL)); F('SH_NAME', SH_NAME)
# journeys — Aaron's death RETOLD (33:38-40 — a retelling never writes an act twice; the date), 33:2's stations
JR_DATE = JR.aarons_death_retold({'ask': 'the_date'}, DD(JR)); F('JR_DATE', JR_DATE); JR_NOWRITE = JR.aarons_death_retold({'ask': 'no_write'}, DD(JR)); F('JR_NOWRITE', JR_NOWRITE)
# midian — the war (the five kings; Balaam slain — 349:1's Simeon at Zimri: Numbers 25 and 31 on the tape), Phinehas's lineage
MI_KINGS = MI.the_war({'ask': 'five_kings'}, DD(MI)); F('MI_KINGS', MI_KINGS); MI_BALAAM = MI.the_war({'ask': 'balaam'}, DD(MI)); F('MI_BALAAM', MI_BALAAM); MI_LINEAGE = DK(MI, 'phinehas_lineage'); F('MI_LINEAGE', MI_LINEAGE)
# mamre — the three men (18:2 — Abraham seeing the house at 352:9), Sodom (Lot); Genesis 15:1's shield (shield_promised on abraham — 33:29's shield by the ink's word)
MA_THREE = MA.mamre('three_men'); F('MA_THREE', MA_THREE); MA_LOT = MA.sodom('lot_learned_where'); F('MA_LOT', MA_LOT)
# pre_sinai — the sons of Noah (Genesis 9 — the seven commandments: Tosefta Avodah Zarah 9:4 the case at 343:6, the Torah offered to the nations and refused)
PS_SEVEN = PS.noahide('seven_from_root'); F('PS_SEVEN', PS_SEVEN); PS_LIST = PS.noahide('seven_list'); F('PS_LIST', PS_LIST)
print('THE CALLEES\' FACTS (printed before they are asserted — %d):' % len(FACTS_PRINT))
for _n, _v in FACTS_PRINT: print('  FACT %s = %s' % (_n, repr(_v)[:150]))
# ---- THE FACTS ASSERTED FROM THE FIRST PASS'S PRINT (parse_ch33_fastcheck.py wrote these from ch33_fastcheck_run0.out — the repr's first sixty characters; a moved callee fails here, not in a cell) ----
_FV = dict(FACTS_PRINT)
assert repr(_FV['SC_DEATH'])[:60] == "{'the_command': 'Deut 32:50 — die in the mount and be gather", ('SC_DEATH', repr(_FV['SC_DEATH'])[:100])
assert repr(_FV['SC_RB'])[:60] == "[{'verses': 'Deut 32:1', 'told': 'give ear, O heavens, and I", ('SC_RB', repr(_FV['SC_RB'])[:100])
assert repr(_FV['SC_AARON'])[:60] == "{'the_tape': 'Numbers 20:28 — garments_transferred_and_aaron", ('SC_AARON', repr(_FV['SC_AARON'])[:100])
assert repr(_FV['SC_NEBO'])[:60] == '"die in the mount where you go up, and be gathered to your p', ('SC_NEBO', repr(_FV['SC_NEBO'])[:100])
assert repr(_FV['SC_TABLE'])[:60] == "'the readback table (32:1-52) — 52 rows one per verse, SHORT", ('SC_TABLE', repr(_FV['SC_TABLE'])[:100])
assert repr(_FV['CR_SONG'])[:60] == '"when they eat and are sated and grow fat and turn (31:20) —', ('CR_SONG', repr(_FV['CR_SONG'])[:100])
assert repr(_FV['CR_SPOKE'])[:60] == '"Moses spoke the words of this song in the ears of all the a', ('CR_SPOKE', repr(_FV['CR_SPOKE'])[:100])
assert repr(_FV['CR_AHEAD'])[:60] == '{\'the_text\': "Deut 32:1-43 — sitting 20\'s reading and its co', ('CR_AHEAD', repr(_FV['CR_AHEAD'])[:100])
assert repr(_FV['CR_DEATH'])[:60] == '"THE SEVENTH OF ADAR OF THE FORTIETH YEAR — the year the ink', ('CR_DEATH', repr(_FV['CR_DEATH'])[:100])
assert repr(_FV['CR_GIFTS'])[:60] == '"THREE GIFTS BY THREE MERITS — the well by Miriam\'s, the pil', ('CR_GIFTS', repr(_FV['CR_GIFTS'])[:100])
assert repr(_FV['GR_GRAVE'])[:60] == "'reubens_nebo_gads_field'", ('GR_GRAVE', repr(_FV['GR_GRAVE'])[:100])
assert repr(_FV['GR_EAST'])[:60] == "'by_moses_word_not_by_lot_held_before_assignment'", ('GR_EAST', repr(_FV['GR_EAST'])[:100])
assert repr(_FV['GR_CEASED'])[:60] == '(40, 5, 15)', ('GR_CEASED', repr(_FV['GR_CEASED'])[:100])
assert repr(_FV['GR_DOUBLED'])[:60] == '"the doubled condition — R. Meir: every condition not double', ('GR_DOUBLED', repr(_FV['GR_DOUBLED'])[:100])
assert repr(_FV['GR_CHARGE'])[:60] == '"our little ones, our wives, our cattle and all our beasts (', ('GR_CHARGE', repr(_FV['GR_CHARGE'])[:100])
assert repr(_FV['JO_SEVENTY'])[:60] == '70', ('JO_SEVENTY', repr(_FV['JO_SEVENTY'])[:100])
assert repr(_FV['JO_SIXTY_SIX'])[:60] == '66', ('JO_SIXTY_SIX', repr(_FV['JO_SIXTY_SIX'])[:100])
assert repr(_FV['JO_KEYS'])[:60] == '[]', ('JO_KEYS', repr(_FV['JO_KEYS'])[:100])
assert repr(_FV['FA_FIRSTBORN'])[:60] == "['Gen 49:3', 'Deut 21:17']", ('FA_FIRSTBORN', repr(_FV['FA_FIRSTBORN'])[:100])
assert repr(_FV['FA_COUCH'])[:60] == '5', ('FA_COUCH', repr(_FV['FA_COUCH'])[:100])
assert repr(_FV['FA_ALIGN'])[:60] == '(20, 9)', ('FA_ALIGN', repr(_FV['FA_ALIGN'])[:100])
assert repr(_FV['CK_SENT'])[:60] == '"barred from the land — Moses and Aaron; Aaron\'s closed at 2', ('CK_SENT', repr(_FV['CK_SENT'])[:100])
assert repr(_FV['CK_SEATS'])[:60] == "'Meribah at 6 seats — Exod 17:7 the first, Num 20:13 the sec", ('CK_SEATS', repr(_FV['CK_SEATS'])[:100])
assert repr(_FV['CK_KISS'])[:60] == '\'Miriam too by the kiss — "there" / "there" with Deut 34:5 (', ('CK_KISS', repr(_FV['CK_KISS'])[:100])
assert repr(_FV['CK_DATES'])[:60] == "'Aaron (40, 5, 1) by the ink, aged 123; Miriam the tenth of ", ('CK_DATES', repr(_FV['CK_DATES'])[:100])
assert repr(_FV['CK_SUCC'])[:60] == "'the garments to Eleazar and the office with them — Exod 29:", ('CK_SUCC', repr(_FV['CK_SUCC'])[:100])
assert repr(_FV['ES_SINAI'])[:60] == 'True', ('ES_SINAI', repr(_FV['ES_SINAI'])[:100])
assert repr(_FV['ES_TREASURE'])[:60] == '4', ('ES_TREASURE', repr(_FV['ES_TREASURE'])[:100])
assert repr(_FV['ES_TRIALS'])[:60] == '6', ('ES_TRIALS', repr(_FV['ES_TRIALS'])[:100])
assert repr(_FV['ES_BIRTH'])[:60] == '(12, 7)', ('ES_BIRTH', repr(_FV['ES_BIRTH'])[:100])
assert repr(_FV['ER_CALF'])[:60] == '4', ('ER_CALF', repr(_FV['ER_CALF'])[:100])
assert repr(_FV['ER_MIL'])[:60] == "'students_travel_a_fortiori'", ('ER_MIL', repr(_FV['ER_MIL'])[:100])
assert repr(_FV['ST_THERE'])[:60] == '"there Aaron died (10:6) — the tape\'s garments_transferred_a', ('ST_THERE', repr(_FV['ST_THERE'])[:100])
assert repr(_FV['ST_BURIED'])[:60] == '"and he was buried there (10:6) — the Torah\'s one seat; Numb', ('ST_BURIED', repr(_FV['ST_BURIED'])[:100])
assert repr(_FV['ST_WALK'])[:60] == '"walk after His attributes (Sotah 14a:3-4) — \'after the LORD', ('ST_WALK', repr(_FV['ST_WALK'])[:100])
assert repr(_FV['ST_PLACE'])[:60] == "{'name': 'the place of the death', 'verses': 'Deut 10:6; Num", ('ST_PLACE', repr(_FV['ST_PLACE'])[:100])
assert repr(_FV['IS_INCENSE'])[:60] == '[1, 1, 1, 2]', ('IS_INCENSE', repr(_FV['IS_INCENSE'])[:100])
assert repr(_FV['IS_SHEKEL'])[:60] == "['Exod 30:12']", ('IS_SHEKEL', repr(_FV['IS_SHEKEL'])[:100])
assert repr(_FV['IS_RANSOM'])[:60] == "['Deut 21:8', 'Exod 21:30', 'Exod 29:33', 'Exod 30:12', 'Num", ('IS_RANSOM', repr(_FV['IS_RANSOM'])[:100])
assert repr(_FV['BK_MOST_HIGH'])[:60] == '"\'knows the knowledge of the Most High\' = fixes the moment o', ('BK_MOST_HIGH', repr(_FV['BK_MOST_HIGH'])[:100])
assert repr(_FV['BK_STAR'])[:60] == "'r_akiva_bar_koziba'", ('BK_STAR', repr(_FV['BK_STAR'])[:100])
assert repr(_FV['OS_MTN'])[:60] == '"the mountain of Abarim (27:12) — Nebo and Pisgah its other ', ('OS_MTN', repr(_FV['OS_MTN'])[:100])
assert repr(_FV['OS_DEBIT'])[:60] == "'the debit (27:12) — see the land from Abarim: commanded on ", ('OS_DEBIT', repr(_FV['OS_DEBIT'])[:100])
assert repr(_FV['OS_HAND'])[:60] == '"the hand laid (27:18, 23) — one hand commanded, two laid (t', ('OS_HAND', repr(_FV['OS_HAND'])[:100])
assert repr(_FV['OS_HONOR'])[:60] == "'of your honor (27:20) — not all of it: the sun and the moon", ('OS_HONOR', repr(_FV['OS_HONOR'])[:100])
assert repr(_FV['OS_ROUTE'])[:60] == '"the route (2:8) — Elath and Ezion-geber, the way of Moab\'s ', ('OS_ROUTE', repr(_FV['OS_ROUTE'])[:100])
assert repr(_FV['OS_FRAME'])[:60] == "{'words_of_1_1': 22, 'places': ['the wilderness', 'the Araba", ('OS_FRAME', repr(_FV['OS_FRAME'])[:100])
assert repr(_FV['RW_ONE'])[:60] == '"one witness for any iniquity (19:15) — the general rule fro', ('RW_ONE', repr(_FV['RW_ONE'])[:100])
assert repr(_FV['RW_SAYING'])[:60] == '{\'onkelos\': "\'the priests shall say\' — the subjectless verb ', ('RW_SAYING', repr(_FV['RW_SAYING'])[:100])
assert repr(_FV['CP_GRADES'])[:60] == '"the distinguished judge and the three grades (17:8) — \'too ', ('CP_GRADES', repr(_FV['CP_GRADES'])[:100])
assert repr(_FV['CP_YAVNEH'])[:60] == '"the court at Yavneh and the priests (17:9-10) — Yavneh incl', ('CP_YAVNEH', repr(_FV['CP_YAVNEH'])[:100])
assert repr(_FV['CP_JUDGE'])[:60] == '"the judge of those days (17:9) — a judge fit and establishe', ('CP_JUDGE', repr(_FV['CP_JUDGE'])[:100])
assert repr(_FV['FJ_TIMES'])[:60] == '"the three times (16:16) — all the males appear three times ', ('FJ_TIMES', repr(_FV['FJ_TIMES'])[:100])
assert repr(_FV['FJ_WHO'])[:60] == '"who appears (16:16) — all obligated except the twelve exemp', ('FJ_WHO', repr(_FV['FJ_WHO'])[:100])
assert repr(_FV['FJ_INTERCAL'])[:60] == "{'the_rows': {'position': 'after_month_12', 'length': 30}, '", ('FJ_INTERCAL', repr(_FV['FJ_INTERCAL'])[:100])
assert repr(_FV['GL_GROWTH'])[:60] == '"the growth\'s list (8:12-13) — 6:10-11\'s gift made the growt', ('GL_GROWTH', repr(_FV['GL_GROWTH'])[:100])
assert repr(_FV['GL_SPECIES'])[:60] == "{'the_one_verse': ['Deut 8:8'], 'three_or_more': [('Deut 8:8", ('GL_SPECIES', repr(_FV['GL_SPECIES'])[:100])
assert repr(_FV['GL_R'])[:60] == '[]', ('GL_R', repr(_FV['GL_R'])[:100])
assert repr(_FV['BC_DRINKS'])[:60] == '"drinks by the rain of heaven (11:11) — the one seat; THE SO', ('BC_DRINKS', repr(_FV['BC_DRINKS'])[:100])
assert repr(_FV['BC_RAIN'])[:60] == '{\'mention_from\': "the last festival day of Sukkot — the eigh', ('BC_RAIN', repr(_FV['BC_RAIN'])[:100])
assert repr(_FV['RL_NEEDY'])[:60] == '{\'the_blessings_arm\': "\'there shall be no needy among you\' w', ('RL_NEEDY', repr(_FV['RL_NEEDY'])[:100])
assert repr(_FV['RL_LEND'])[:60] == '{\'28_12_the_twin\': "\'lend\' for \'pledge\' — 6 in order", \'28_4', ('RL_LEND', repr(_FV['RL_LEND'])[:100])
assert repr(_FV['RL_BLESS'])[:60] == '{\'only_in_the_land\': \'114:2\', \'the_conquest_first\': "114:3 —', ('RL_BLESS', repr(_FV['RL_BLESS'])[:100])
assert repr(_FV['RL_HAND'])[:60] == '"the needy\'s ranks (15:7) — \'among you\', \'one of your brothe', ('RL_HAND', repr(_FV['RL_HAND'])[:100])
assert repr(_FV['PP_RB'])[:60] == "'the readback table (22:1-25:19) — 96 rows one per verse, EX", ('PP_RB', repr(_FV['PP_RB'])[:100])
assert repr(_FV['PP_OLIVES'])[:60] == '"the named tree not forgotten; the olive of two seahs; R. Me', ('PP_OLIVES', repr(_FV['PP_OLIVES'])[:100])
assert repr(_FV['BM_TOTAL'])[:60] == "'603550 = the twelve summed'", ('BM_TOTAL', repr(_FV['BM_TOTAL'])[:100])
assert repr(_FV['BM_HOUSES'])[:60] == "'7500 + 8600 + 6200 = 22300'", ('BM_HOUSES', repr(_FV['BM_HOUSES'])[:100])
assert repr(_FV['BM_AARON'])[:60] == 'True', ('BM_AARON', repr(_FV['BM_AARON'])[:100])
assert repr(_FV['NS_COND'])[:60] == "'six: lain with, hidden, secreted, defiled, no witness, not ", ('NS_COND', repr(_FV['NS_COND'])[:100])
assert repr(_FV['NS_FACE'])[:60] == "'when_they_do_his_will'", ('NS_FACE', repr(_FV['NS_FACE'])[:100])
assert repr(_FV['KO_DONKEY'])[:60] == "'exempt — a priest or a Levite (the son and the donkey)'", ('KO_DONKEY', repr(_FV['KO_DONKEY'])[:100])
assert repr(_FV['KO_24'])[:60] == "'24 — twelve in the sanctuary, twelve in the borders (Sifrei", ('KO_24', repr(_FV['KO_24'])[:100])
assert repr(_FV['KO_TITHE'])[:60] == "'levite'", ('KO_TITHE', repr(_FV['KO_TITHE'])[:100])
assert repr(_FV['VE_NAME'])[:60] == "('חשן משפט', 'חשן המשפט')", ('VE_NAME', repr(_FV['VE_NAME'])[:100])
assert repr(_FV['VE_SHOULDERS'])[:60] == '2', ('VE_SHOULDERS', repr(_FV['VE_SHOULDERS'])[:100])
assert repr(_FV['PR_ADDR'])[:60] == "{'sons_of_aaron': 'bound', 'daughters_of_aaron': 'free', 'ch", ('PR_ADDR', repr(_FV['PR_ADDR'])[:100])
assert repr(_FV['PR_AGE'])[:60] == "{'minor': 'unfit_even_whole', 'valid_from': 'two_hairs', 'ad", ('PR_AGE', repr(_FV['PR_AGE'])[:100])
assert repr(_FV['ZE_PLEA'])[:60] == '"no son and no son\'s line — the daughters claim; a son\'s dau', ('ZE_PLEA', repr(_FV['ZE_PLEA'])[:100])
assert repr(_FV['ZE_COUNSEL'])[:60] == "'the counsel — the mercies of the Place are on males and fem", ('ZE_COUNSEL', repr(_FV['ZE_COUNSEL'])[:100])
assert repr(_FV['ZE_REACH'])[:60] == "'this_generation'", ('ZE_REACH', repr(_FV['ZE_REACH'])[:100])
assert repr(_FV['S2_COUNTS'])[:60] == '"twelve at both seats, the parser\'s"', ('S2_COUNTS', repr(_FV['S2_COUNTS'])[:100])
assert repr(_FV['S2_LOT'])[:60] == "'the place by lot — Joshua 14-19 the run'", ('S2_LOT', repr(_FV['S2_LOT'])[:100])
assert repr(_FV['S2_13'])[:60] == "'twelve_now_thirteen_to_come'", ('S2_13', repr(_FV['S2_13'])[:100])
assert repr(_FV['BR_LAND'])[:60] == '"the land of Canaan (34:2) read as a title claim (Sanhedrin ', ('BR_LAND', repr(_FV['BR_LAND'])[:100])
assert repr(_FV['BR_SIDES'])[:60] == "OrderedDict({'south': {'verses': [3, 4, 5], 'points': [(3, '", ('BR_SIDES', repr(_FV['BR_SIDES'])[:100])
assert repr(_FV['PN_TRIBES'])[:60] == '"in one of your tribes (12:14) — [1] the chapter\'s one numbe', ('PN_TRIBES', repr(_FV['PN_TRIBES'])[:100])
assert repr(_FV['PN_NAME'])[:60] == '"the Name pronounced only there (12:5) — the priestly blessi', ('PN_NAME', repr(_FV['PN_NAME'])[:100])
assert repr(_FV['PN_ENTRY'])[:60] == "['a king (17:14-15)', 'Amalek cut off (25:17-19)', 'the chos", ('PN_ENTRY', repr(_FV['PN_ENTRY'])[:100])
assert repr(_FV['OH_KNOW'])[:60] == '"know this day (4:39) — the creed\'s second seat: Rahab\'s and', ('OH_KNOW', repr(_FV['OH_KNOW'])[:100])
assert repr(_FV['OH_FORM'])[:60] == '"no form seen (4:15) — the guard\'s reason: the voice without', ('OH_FORM', repr(_FV['OH_FORM'])[:100])
assert repr(_FV['OH_CREED'])[:60] == "['Deut 4:35', 'Deut 4:39']", ('OH_CREED', repr(_FV['OH_CREED'])[:100])
assert repr(_FV['OH_CHAIN'])[:60] == "{'this_chapter': 'Deut 4:26', 'the_chain': ['Deut 4:26', 'De", ('OH_CHAIN', repr(_FV['OH_CHAIN'])[:100])
assert repr(_FV['OH_FRAME'])[:60] == "{'deut_4_44_45': 'the_second_speech_s_head', 'write': None}", ('OH_FRAME', repr(_FV['OH_FRAME'])[:100])
assert repr(_FV['SN_CHOSE'])[:60] == '"chose you (7:6-7) — the choice of the people after 4:37\'s c', ('SN_CHOSE', repr(_FV['SN_CHOSE'])[:100])
assert repr(_FV['SN_FEW'])[:60] == '"the fewest (7:7) — \'not because you were more\': the humbles', ('SN_FEW', repr(_FV['SN_FEW'])[:100])
assert repr(_FV['HI_HEAR'])[:60] == '"hear, O Israel (6:4) — the creed\'s call: Jacob\'s sons\' answ', ('HI_HEAR', repr(_FV['HI_HEAR'])[:100])
assert repr(_FV['HI_ONE'])[:60] == '"the LORD is one (6:4) — the two seats of the pair (6:4, Zec', ('HI_ONE', repr(_FV['HI_ONE'])[:100])
assert repr(_FV['HI_TERMS'])[:60] == "{'heart': 'with both inclinations — the good and the evil', ", ('HI_TERMS', repr(_FV['HI_TERMS'])[:100])
assert repr(_FV['MD_SUK'])[:60] == 'None', ('MD_SUK', repr(_FV['MD_SUK'])[:100])
assert repr(_FV['MD_RH'])[:60] == 'None', ('MD_RH', repr(_FV['MD_RH'])[:100])
assert repr(_FV['OF_PLACE'])[:60] == "'anywhere_courtyard'", ('OF_PLACE', repr(_FV['OF_PLACE'])[:100])
assert repr(_FV['OF_FAT'])[:60] == 'None', ('OF_FAT', repr(_FV['OF_FAT'])[:100])
assert repr(_FV['FE_EAGLE'])[:60] == '"a nation from the end of the earth as the eagle flies (28:4', ('FE_EAGLE', repr(_FV['FE_EAGLE'])[:100])
assert repr(_FV['FE_MEASURE'])[:60] == "'the corner, the first fruits, the appearing, the acts of ki", ('FE_MEASURE', repr(_FV['FE_MEASURE'])[:100])
assert repr(_FV['FE_SIX'])[:60] == '{\'28:63\': "the parser\'s [6] is the verb \'rejoiced\' — the num', ('FE_SIX', repr(_FV['FE_SIX'])[:100])
assert repr(_FV['FE_FIRST'])[:60] == '"when you come into the land and dwell in it (26:1) — the fi', ('FE_FIRST', repr(_FV['FE_FIRST'])[:100])
assert repr(_FV['SH_NAME'])[:60] == "'Hoshea to Joshua at 13:16 — the new name at 8 seats before ", ('SH_NAME', repr(_FV['SH_NAME'])[:100])
assert repr(_FV['JR_DATE'])[:60] == '"Aaron died on (40, 5, 1) (33:38) — the tape\'s marker at 20:', ('JR_DATE', repr(_FV['JR_DATE'])[:100])
assert repr(_FV['JR_NOWRITE'])[:60] == '"no write for 33:38-40 — the death and the hearing are the t', ('JR_NOWRITE', repr(_FV['JR_NOWRITE'])[:100])
assert repr(_FV['MI_KINGS'])[:60] == '"five kings — Evi, Rekem, Zur, Hur, Reba (31:8; the parser\'s', ('MI_KINGS', repr(_FV['MI_KINGS'])[:100])
assert repr(_FV['MI_BALAAM'])[:60] == '"Balaam killed with the sword (31:8) — come for his wages (S', ('MI_BALAAM', repr(_FV['MI_BALAAM'])[:100])
assert repr(_FV['MI_LINEAGE'])[:60] == "'joseph_and_jethro_both'", ('MI_LINEAGE', repr(_FV['MI_LINEAGE'])[:100])
assert repr(_FV['MA_THREE'])[:60] == '3', ('MA_THREE', repr(_FV['MA_THREE'])[:100])
assert repr(_FV['MA_LOT'])[:60] == "'abrahams_house'", ('MA_LOT', repr(_FV['MA_LOT'])[:100])
assert repr(_FV['PS_SEVEN'])[:60] == "{'commanded': 'courts', 'the_LORD': 'blasphemy', 'God': 'ido", ('PS_SEVEN', repr(_FV['PS_SEVEN'])[:100])
assert repr(_FV['PS_LIST'])[:60] == "['courts', 'blasphemy', 'idolatry', 'unions', 'bloodshed', '", ('PS_LIST', repr(_FV['PS_LIST'])[:100])


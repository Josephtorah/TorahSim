#!/usr/bin/env python3
# DEUTERONOMY 34:1-12 — THE DEATH OF MOSES (and Moses went up from the plains of Moab to Mount Nebo, the top of Pisgah, over against Jericho, and the LORD showed him all the
# land — Gilead as far as Dan, Naphtali, Ephraim and Manasseh, Judah as far as the hinder sea, the South and the Plain, the valley of Jericho, the city of palms, as far as Zoar;
# and the LORD said to him: this is the land which I swore to Abraham, to Isaac and to Jacob, saying: to your seed I will give it; I have caused you to see it with your eyes, but
# you shall not cross over there. And Moses the servant of the LORD died there in the land of Moab by the mouth of the LORD; and He buried him in the valley in the land of Moab
# over against Beth-peor, and no man knows his grave to this day. And Moses was a hundred and twenty years old when he died; his eye was not dim, nor his natural force abated;
# and the children of Israel wept for Moses in the plains of Moab thirty days, and the days of weeping in the mourning for Moses were ended. And Joshua the son of Nun was full of
# the spirit of wisdom, for Moses had laid his hands upon him; and the children of Israel hearkened to him and did as the LORD commanded Moses. And there arose not a prophet since
# in Israel like Moses, whom the LORD knew face to face — all the signs and the wonders in the land of Egypt, and the mighty hand and the great terror which Moses wrought in the
# sight of all Israel); THE READBACK'S FORMS ON FILE, NO NEW FORM (THE DEUTERONOMY WALK sitting 22b — THE LEAN PASS, 2026-09-30; World/step9/DEUTERONOMY_WALK.md "Sitting 22b";
# the state doc's #244). ONE RUNNER OVER ONE CHAPTER AND ONE UNIT (deu_34_moses_death — the death 34:1-12; the span one range), THE BOOK'S LAST; SIX own-day lines IN TWO FORMS —
# 5 ACTS of the narrator (moses_went_up_to_nebo_and_saw_the_land 34:1-3, moses_died_and_was_buried 34:5-6, moses_hundred_and_twenty_israel_wept_thirty_days 34:7-8,
# joshua_full_of_the_spirit_israel_hearkened 34:9, no_prophet_like_moses_declared 34:10-12 — the epilogue's 'there arose not' a narrative past) and 1 SPEECH of the LORD
# (oath_land_shown_not_crossed_declared 34:4 — the subject god): EVERY LINE AT MOSES' LAST DAY (40, 12, 7) after 19b's ONE MARKER at 31:1 — NO MARKER HERE (the seventh of Adar,
# the death THAT day; THE THIRTY DAYS OF WEEPING A DURATION by the design's ruling — no timer, the counter unmoved). FIFTEEN writes on THREE ledgers (twelve NEW, all STATUSES, no
# block, no heaven entry — moses 6, israel_people 5, yehoshua 1; THREE REUSES at their own forward seats — see_the_land_from_afar_not_go_there at 34:4 on moses (a heaven entry — the
# song's owed pointer PAID), gathered_to_his_people at 34:5 on moses (Aaron's word — the song's second owed pointer PAID), mourned_thirty_days at 34:8 on israel_people (the registry's
# TIMER row written WITHOUT A DUE — no timer set)). THE PARSER'S TWO NUMBERS as DATA rows (34:7's 120 — 31:2's number on the marker's day; 34:8's 30 — Aaron's thirty), no guard, no
# count in the world. THE KIN'S CELLS BY CALL (twenty runners, every edge REFERENCE — the chapter's pasts RUN CITATIONS against the tape's own lines: the summons 32:49, Exodus 33:1's
# oath, Aaron's death in Aaron's words, the commission Numbers 27:18-23, the signs and the tablets broken); THE THREE POINTER ROWS 34:4, 34:5, 34:6 (the song's two and the blessing's
# one PAID, grade R); THE RECEIPT ROW 34:9 (the register's seat re-declared from the gate's print); THE BOOK'S EDGE at 34:12. Six cells and the table; every token probed (zero-report
# law); effects on every cell (the effects law); THE EXAM THE FIVE MISHNAH ROWS AND THE ONE TOSEFTA ROW THE LEDGER CITES (Avot 1:1, Nazir 1:3, Sanhedrin 10:1, Sotah 1:7, Sotah 1:9,
# Tosefta Sotah 4:4 — read whole; the Mishnah's Sotah 4:4 the regex's misread, read whole and excluded; no docket, the lean form); the parameters the runner's DATA rows (nine), NO
# clock datum (19b's death date THE DAY). The daemon law_moses_death given_at Deut 34:1, installed_by boot (the Deuteronomy daemons' form). Reading ledger:
# logic/oral_triage/deu_34_moses_death_2026-09-30.md; the lean exam: deu_34_moses_death_exam_2026-09-30.md.

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
import cold_run_song_charge_nebo as SC            # THE EDGE: moses_death -> song_charge_nebo CALL, reference (32:49's summons OBEYED at 34:1 — a RUN CITATION; 32:52's denial REUSED at 34:4 and 32:50's death executed at 34:5 — THE SONG'S TWO OWED POINTERS PAID; the_readback's form)
import cold_run_covenant_return_charge as CR    # THE EDGE: moses_death -> covenant_return_charge CALL, reference (31:2's hundred and twenty on the marker's day — 34:7, no second marker; 31:7 and 31:23 Joshua's charge and commission — 34:9; the three gifts' merits owed at 34:5; the death date the seventh of Adar)
import cold_run_blessing_of_moses as BL          # THE EDGE: moses_death -> blessing_of_moses CALL, reference (Onkelos 33:21's grave in Gad's portion — 34:6, THE BLESSING'S OWED POINTER PAID; Avot 1:1's chain the parameter read again at 34:9; 33:1's 'before his death' THIS day)
import cold_run_gad_reuben as GR                 # THE EDGE: moses_death -> gad_reuben CALL, reference (Numbers 32:38's Nebo — Reuben's Nebo and Gad's field, Sotah 13b: the grave at 34:6; 34:1's Mount Nebo the land east's)
import cold_run_chukat as CK                     # THE EDGE: moses_death -> chukat CALL, reference (Numbers 20:24-29 AARON'S DEATH — the gathering REUSED at 34:5, the thirty days REUSED at 34:8 without a due; Miriam's well the three gifts' first event; the sentence at Meribah read not rewritten)
import cold_run_journeys as JR                   # THE EDGE: moses_death -> journeys CALL, reference (Numbers 33:38-39 'by the mouth of the LORD', 'when he died' — Aaron's words at 34:5 and 34:7; the retelling that never writes)
import cold_run_second_tablets as ST             # THE EDGE: moses_death -> second_tablets CALL, reference (10:6 Aaron buried there; Sotah 14a's burying the dead — the burial by the LORD at 34:6; 9:17's tablets broken — 34:12's great terror by the Sifrei 357:44)
import cold_run_zelophehad as ZE                 # THE EDGE: moses_death -> zelophehad CALL, reference (Numbers 27:18-23 THE COMMISSION — invested_office on yehoshua; 34:9's 'Moses had laid his hands upon him' the receipt, a RUN CITATION)
import cold_run_opening_speech as OS             # THE EDGE: moses_death -> opening_speech CALL, reference (3:27's Pisgah refused — 34:1 granted; Numbers 27:12-13's debit — 34:4 PAID; the hand laid — 34:9; 3:29's Beth-peor — 34:6)
import cold_run_beha as BH                       # THE EDGE: moses_death -> beha CALL, reference (Taanit 9a's three gifts by three merits — the third death at 34:5; Numbers 12:8's 'mouth to mouth' — 34:10's 'face to face' the twin by sense)
import cold_run_naso as NS                       # THE EDGE: moses_death -> naso CALL, reference (Numbers 6:4's 'the days' — THE NAZIRITE'S TERM taught from 34:8's 'the days of weeping' by I2; Nazir 1:3 the case; nazir_default_days the callee's row)
import cold_run_courts_prophet as CP             # THE EDGE: moses_death -> courts_prophet CALL, reference (18:15's and 18:18's prophet LIKE Moses promised — 34:10's none arisen; the_prophets_bound the parameter)
import cold_run_erection as ER                   # THE EDGE: moses_death -> erection CALL, reference (Exodus 33:1's oath TAKEN WHOLE at 34:4 — a RUN CITATION; 33:11's face to face — 34:10; 34:29's shining face — 34:7's undimmed eye; the tablets broken — 34:12)
import cold_run_exodus_story as ES               # THE EDGE: moses_death -> exodus_story CALL, reference (Exodus 7:3's signs and wonders, the plagues and the sea — 34:11-12 RUN CITATIONS; the seventh of Adar Moses' birthday and death day)
import cold_run_joseph as JO                     # THE EDGE: moses_death -> joseph CALL, reference (Joseph's bones and the oath — Sotah 1:9's measure at 34:6: Moses merited Joseph's bones, the Place attended Moses'; the three deaths' burials)
import cold_run_family as FA                     # THE EDGE: moses_death -> family CALL, reference (the testament's 'gathered to his people' — the formula REUSED at 34:5; the purchase's holding by burial — 34:6's grave)
import cold_run_mamre as MA                      # THE EDGE: moses_death -> mamre CALL, reference (Genesis 12:7 and 15:18's promise to Abraham — 34:4's 'which I swore to Abraham'; 14:14's 'as far as Dan' — 34:1)
import cold_run_hear_o_israel as HI              # THE EDGE: moses_death -> hear_o_israel CALL, reference (6:10's three fathers — 34:4's oath; the receipt's form without the Name — 34:9's receipt with it)
import cold_run_obey_horeb as OH                 # THE EDGE: moses_death -> obey_horeb CALL, reference (3:29's and 4:46's 'over against Beth-peor' — 34:6's three seats; the witnesses' chain and the second frame)
import cold_run_shelach as SHL                   # THE EDGE: moses_death -> shelach CALL, reference (Numbers 13:16 Hoshea renamed Joshua — 34:9's Joshua the son of Nun; the deaths ceased)

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
def W34(v): return words('Deut', 34, v)
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
CHS = (34,)
NV = {c: len({v for (b, cc, v) in by if b == 'Deut' and cc == c}) for c in CHS}; assert NV == {34: 12}, NV   # twelve verses (the reading's divisions assert — the identity)
TOKN = {c: sum(len(W(c, v)) for v in range(1, NV[c] + 1)) for c in CHS}
print('THE TOKENS (printed before they are asserted):', TOKN)
TOKN_EXPECTED = {34: 176}   # the reading's own count (ch34_ink.py — 176 tokens over the twelve verses; the first derive's print)
if TOKN_EXPECTED: assert TOKN == TOKN_EXPECTED, (TOKN, TOKN_EXPECTED)
SPAN = [(34, v) for v in range(1, 13)]
assert len(SPAN) == 12

P_ = []   # the provenance trail of the case being run
def ink(ref, note):  P_.append(('INK',  'Deut %s — %s' % (ref, note) if not ref[:1].isupper() else '%s — %s' % (ref, note)))
def move(src, note): P_.append(('MOVE', '%s — %s' % (src, note)))
def dat(note):       P_.append(('DATA', note))
def hyp(note):       P_.append(('HYP',  note))     # THE LINK REVIEW LAW: a hypothesis — no teacher; counted apart, never as compiled
def out(verdict, effects):
    """verdict + registry-validated effects (the engine contract)"""
    FX.validate([e for e in effects if e != FX.NONE])
    return verdict, effects, list(P_)

# ---- THE INK, computed (the parser and the tokens; the reading's facts the expectations — every assert PROVEN at the reading, ch34_ink.py — LIFTED from the reading's instrument and glossed: the kin, the twins, the formulas, the names, the frames; the store-, shelf-, Onkelos- and register-bound asserts left to the reading; the parser's facts typed from the measure's print as the ink instrument asserted them) ----
def MARKS(c, v): return [t for t in verse_words('Deut', c, v) if t[-1] in '#~^%@|*']
PARSE = {(c, v): (ink_numbers(verse_words('Deut', c, v)), ink_ordinals(verse_words('Deut', c, v)), MARKS(c, v)) for (c, v) in SPAN}
NUMV = [k for k in PARSE if PARSE[k][0]]; ORDV = [k for k in PARSE if PARSE[k][1]]; STARV = [k for k in PARSE if PARSE[k][2]]
print('THE INK (printed before it is asserted): PARSE %s, NUMV %s, ORDV %s, STARV %s, TOKN %s' % ({k: p for k, p in PARSE.items() if p[0] or p[1] or p[2]}, NUMV, ORDV, STARV, TOKN))
assert {k: p for k, p in PARSE.items() if p[0] or p[1] or p[2]} == {(34, 7): ([120], [], []), (34, 8): ([30], [], [])}, {k: p for k, p in PARSE.items() if p[0] or p[1] or p[2]}   # the reading's parser assert (ch34_ink.py from ch34_measure_lean.out): TWO NUMBERS COUNTED — 34:7's 120 (31:2's number on the marker's day), 34:8's 30 (Aaron's thirty): DATA rows, no count in the world
assert NUMV == [(34, 7), (34, 8)] and ORDV == [] and STARV == []
assert W(34, 7)[:5] == [_G('ומשה (and Moses)'), _G('בן (aged)'), _G('מאה (a hundred)'), _G('ועשרים (and twenty)'), _G('שנה (years)')] and W(34, 8)[7:9] == [_G('שלשים (thirty)'), _G('יום (days)')]   # the two number seats: a hundred and twenty years (34:7 — 31:2's number), thirty days (34:8 — Numbers 20:29's)
NEG = {(c, v): [x for x in W(c, v) if x in NEG_T] for (c, v) in SPAN if any(x in NEG_T for x in W(c, v))}
NAME_BARE = sum(1 for (c, v) in SPAN for x in W(c, v) if x == _G('יהוה (the LORD)'))   # (the LORD)
print('THE NEGATIONS AND THE NAME (printed before they are asserted):', NEG, NAME_BARE)
NAME_BARE_EXPECTED = 7   # the reading's count (ch34_ink.py — the Name SEVEN times bare: 34:1, 4, 5 twice, 9, 10, 11)
if NAME_BARE_EXPECTED: assert NAME_BARE == NAME_BARE_EXPECTED, (NAME_BARE, NAME_BARE_EXPECTED)
NEG_EXPECTED = {'34:4': 1, '34:6': 1, '34:7': 2, '34:10': 1}   # the negations per verse (the reading's assert — 'not' five times: you shall not cross over, no man knows, the eye not dim and the force not abated, no prophet arose)
if NEG_EXPECTED: assert {'%d:%d' % k: len(v) for k, v in NEG.items()} == NEG_EXPECTED, {'%d:%d' % k: len(v) for k, v in NEG.items()}
assert [f'{c}:{v}' for c, v in SPAN if _G('לאמר (saying)') in W(c, v)] == ['34:4'] and [(c, v) for c, v in SPAN if _G('אם (if)') in W(c, v) or _G('ואם (and if)') in W(c, v)] == [] and [(c, v, x) for c, v in SPAN for x in W(c, v) if x == _G('פן (lest)')] == [] and [(c, v) for c, v in SPAN if _G('כי (for)') in W(c, v)] == [(34, 9)]   # ("saying" — 34:4 alone, the oath's frame; "if" — none; "lest" — none; "for" — 34:9 alone) — the reading's frames assert
assert [(c, v, x) for c, v in SPAN for x in W(c, v) if x in (_G('אמר (he said)'), _G('ויאמר (and He said)'))] == [(34, 4, _G('ויאמר (and He said)'))] and [(c, v) for c, v in SPAN for i, x in enumerate(W(c, v)[:-1]) if x == _G('ויאמר (and He said)') and W(c, v)[i + 1] == _G('יהוה (the LORD)')] == [(34, 4)]   # the one "he said" — the LORD's at 34:4
NARR = {v: [x for x, m in wm('Deut', 34, v) if m and re.search(r'V.w', m)] for _, v in SPAN if any(m and re.search(r'V.w', m) for _, m in wm('Deut', 34, v))}
assert NARR == {1: [_G('ויעל (and he went up)'), _G('ויראהו (and He showed him)')], 4: [_G('ויאמר (and He said)')], 5: [_G('וימת (and he died)')], 6: [_G('ויקבר (and He buried)')], 8: [_G('ויבכו (and they wept)'), _G('ויתמו (and they were ended)')], 9: [_G('וישמעו (and they hearkened)'), _G('ויעשו (and they did)')]}, NARR   # the narrative past — nine acts in six verses; 34:2-3, 7, 10-12 verbless or descriptive (the register test's frame — every act's own verb within its verses)
assert [(v, x) for _, v in SPAN for x, m in wm('Deut', 34, v) if m and re.search(r'^HV..v', m)] == [] and [(v, x) for _, v in SPAN for x, m in wm('Deut', 34, v) if m and re.search(r'1c[sp]', m) and m.startswith('HV')] == [(4, _G('נשבעתי (I swore)')), (4, _G('אתננה (I will give it)')), (4, _G('הראיתיך (I have caused you to see)'))] and {v: sum(1 for _, m in wm('Deut', 34, v) if m and '2ms' in m) for _, v in SPAN if any(m and '2ms' in m for _, m in wm('Deut', 34, v))} == {4: 4}   # no imperative; the first person at 34:4 alone (I swore, I will give it, I have caused you to see); the second person singular at 34:4 alone
assert [(x, m) for x, m in wm('Deut', 34, 4)][:2] == [(_G('ויאמר (and He said)'), 'HC/Vqw3ms'), (_G('יהוה (the LORD)'), 'HNp')] and [(x, m) for x, m in wm('Deut', 34, 5)][0] == (_G('וימת (and he died)'), 'HC/Vqw3ms') and [(x, m) for x, m in wm('Deut', 34, 9)][3] == (_G('מלא (full)'), 'HAamsa') and [(x, m) for x, m in wm('Deut', 34, 9)][7] == (_G('סמך (had laid)'), 'HVqp3ms')   # the one frame; the death the narrative past; Joshua 'full' an adjective, 'laid' the perfect
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
# THE KIN BY COMPUTATION: the ascent's kin is the command to ascend — 34:1 with 32:49 (eight shared, "over against Jericho" four in order); THE OATH IS EXODUS 33:1's — 34:4 with Exodus 33:1 ten shared, nine in order; the years' kin 31:2 (the marker's verse); the weeping's kin the plains of Moab of Numbers' own footer (26:63); Joshua's kin the tabernacle's receipt formula (Exodus 12:28); the signs' kin 29:1 (Pharaoh, his servants, his land); 34:3, 34:5, 34:6 and 34:10 kin only to the Writings and the Prophets by the instrument — cited never read; no verse of the chapter shares no two tokens with any verse
assert [v for c, v in SPAN if not KINC[(c, v)]] == [], [v for c, v in SPAN if not KINC[(c, v)]]
assert KINC[(34, 1)][0] == ('Deut 32:49', 5, 8) and KINC[(34, 4)][0] == ('Exod 33:1', 7, 10) and KINC[(34, 7)][0] == ('Deut 31:2', 4, 5) and KINC[(34, 8)][0] == ('Num 26:63', 5, 4) and KINC[(34, 9)][0] == ('Exod 12:28', 5, 7) and KINC[(34, 11)][0] == ('Deut 29:1', 5, 9) and KINC[(34, 12)][0] == ('Deut 29:1', 4, 2), (KINC[(34, 1)][0], KINC[(34, 4)][0], KINC[(34, 7)][0], KINC[(34, 8)][0], KINC[(34, 9)][0], KINC[(34, 11)][0], KINC[(34, 12)][0])
assert KINC[(34, 3)][0] == ('2Chr 28:15', 3, 3) and KINC[(34, 2)][0] == ('1Chr 9:3', 3, 2) and KINC[(34, 5)][0] == ('1Chr 1:46', 2, 2) and KINC[(34, 6)][0] == ('1Sam 17:25', 3, 1) and KINC[(34, 10)][0] == ('1Chr 19:10', 2, 1), (KINC[(34, 3)][0], KINC[(34, 2)][0], KINC[(34, 5)][0], KINC[(34, 6)][0], KINC[(34, 10)][0])
# THE TWINS DIFFED (shared / the longest run): the oath 34:4 with Exodus 33:1 NINE IN ORDER and with 6:10 the three fathers; "you shall not cross over" 34:4 with 3:27; the ascent 34:1 with 32:49 four in order and with 3:27 "the top of Pisgah"; THE DEATH IS AARON'S — 34:5 with Numbers 33:38 "by the mouth of the LORD", 34:7 with Numbers 33:39 "when he died", 34:8 with Numbers 20:29 "thirty days", and 34:5 with 32:50 SHARES NO TOKEN — the twin by sense alone; "Moses the servant of the LORD" 34:5 with Joshua 1:1 (cited never read); the years 34:7 with 31:2 four in order; Joshua 34:9 with Numbers 27:23 "his hands upon him" (six shared); "face to face" 34:10 with Exodus 33:11 and with Numbers 12:8's "mouth to mouth" ONE token; 34:12 with 9:17 (the Sifrei's join at 357:44) SHARES NOTHING; 34:6 with 33:21 SHARES NOTHING — Onkelos alone joined them
assert SHARED(('Deut', 34, 4), ('Exod', 33, 1)) == [_G('הארץ (the land)'), _G('אשר (which)'), _G('נשבעתי (I swore)'), _G('לאברהם (to Abraham)'), _G('ליצחק (to Isaac)'), _G('וליעקב (and to Jacob)'), _G('לאמר (saying)'), _G('לזרעך (to your seed)'), _G('אתננה (I will give it)')] and SHN(('Deut', 34, 4), ('Exod', 33, 1)) == 10 and SHARED(('Deut', 34, 4), ('Deut', 6, 10)) == [_G('לאברהם (to Abraham)'), _G('ליצחק (to Isaac)'), _G('וליעקב (and to Jacob)')] and SHN(('Deut', 34, 4), ('Deut', 6, 10)) == 7 and SHARED(('Deut', 34, 4), ('Deut', 3, 27)) == [_G('לא (not)'), _G('תעבר (you shall cross over)')]   # the land which I swore to Abraham, to Isaac and to Jacob, saying: to your seed I will give it — Exodus 33:1's nine in order; the three fathers; you shall not cross
assert SHARED(('Deut', 34, 1), ('Deut', 32, 49)) == [_G('אשר (which)'), _G('על (over)'), _G('פני (against)'), _G('ירחו (Jericho)')] and SHN(('Deut', 34, 1), ('Deut', 32, 49)) == 8 and SHARED(('Deut', 34, 1), ('Deut', 3, 27)) == [_G('ראש (the top of)'), _G('הפסגה (Pisgah)')] and SHARED(('Deut', 34, 1), ('Num', 27, 12)) == [_G('אל (to)'), _G('הר (mount)')] and SHN(('Deut', 34, 1), ('Num', 27, 12)) == 4   # over against Jericho — 32:49's four in order; the top of Pisgah — 3:27's; to the mount — Numbers 27:12's
assert SHARED(('Deut', 34, 5), ('Num', 33, 38)) == [_G('על (by)'), _G('פי (the mouth of)'), _G('יהוה (the LORD)')] and SHN(('Deut', 34, 5), ('Deut', 32, 50)) == 0 and SHARED(('Deut', 34, 5), ('Josh', 1, 1)) == [_G('משה (Moses)'), _G('עבד (the servant of)'), _G('יהוה (the LORD)')] and SHN(('Deut', 34, 5), ('Josh', 1, 1)) == 4 and SHARED(('Deut', 34, 5), ('Num', 20, 28)) == [_G('וימת (and he died)')]   # by the mouth of the LORD — Aaron's at Numbers 33:38; 32:50 shares no token; Moses the servant of the LORD — Joshua 1:1's; and he died — Aaron's at Numbers 20:28
assert SHARED(('Deut', 34, 6), ('Deut', 3, 29)) == [_G('מול (over against)'), _G('בית (Beth)'), _G('פעור (Peor)')] and SHARED(('Deut', 34, 6), ('Deut', 4, 46)) == [_G('מול (over against)'), _G('בית (Beth)'), _G('פעור (Peor)')] and SHN(('Deut', 34, 6), ('Deut', 33, 21)) == 0 and SHARED(('Deut', 34, 6), ('Gen', 50, 13)) == [_G('אתו (him)')]   # over against Beth-peor — 3:29's and 4:46's; 33:21 shares nothing (Onkelos alone joined the grave to the portion); Jacob's burial shares 'him'
assert SHARED(('Deut', 34, 7), ('Deut', 31, 2)) == [_G('בן (aged)'), _G('מאה (a hundred)'), _G('ועשרים (and twenty)'), _G('שנה (years)')] and SHN(('Deut', 34, 7), ('Deut', 31, 2)) == 5 and SHARED(('Deut', 34, 7), ('Gen', 6, 3)) == [_G('מאה (a hundred)'), _G('ועשרים (and twenty)'), _G('שנה (years)')] and SHARED(('Deut', 34, 7), ('Num', 33, 39)) == [_G('שנה (years)'), _G('במתו (when he died)')] and SHN(('Deut', 34, 7), ('Num', 33, 39)) == 4 and SHARED(('Deut', 34, 7), ('Exod', 7, 7)) == [_G('ומשה (and Moses)'), _G('בן (aged)')] and SHN(('Deut', 34, 7), ('Gen', 27, 1)) == 0   # a hundred and twenty years — 31:2's four in order, Genesis 6:3's three; when he died — Aaron's at Numbers 33:39; and Moses was aged — Exodus 7:7's; Isaac's dim eyes share nothing
assert SHARED(('Deut', 34, 8), ('Num', 20, 29)) == [_G('שלשים (thirty)'), _G('יום (days)')] and SHN(('Deut', 34, 8), ('Num', 20, 29)) == 4 and SHARED(('Deut', 34, 8), ('Gen', 50, 3)) == [_G('ויבכו (and they wept)')] and SHARED(('Deut', 34, 8), ('Gen', 50, 10)) == [_G('אבל (the mourning of)')]   # thirty days — Aaron's at Numbers 20:29; and they wept — Egypt's for Jacob; the mourning — Jacob's at Atad
assert SHARED(('Deut', 34, 9), ('Num', 27, 23)) == [_G('את (the object marker)'), _G('ידיו (his hands)'), _G('עליו (upon him)')] and SHN(('Deut', 34, 9), ('Num', 27, 23)) == 6 and SHARED(('Deut', 34, 9), ('Num', 27, 18)) == [_G('בן (the son of)'), _G('נון (Nun)')] and SHN(('Deut', 34, 9), ('Num', 27, 18)) == 5 and SHN(('Deut', 34, 9), ('Deut', 31, 23)) == 6 and SHARED(('Deut', 34, 9), ('Exod', 28, 3)) == [_G('רוח (the spirit of)'), _G('חכמה (wisdom)')] and SHARED(('Deut', 34, 9), ('Isa', 11, 2)) == [_G('רוח (the spirit of)'), _G('חכמה (wisdom)')] and SHARED(('Deut', 34, 9), ('Num', 27, 20)) == [_G('בני (the children of)'), _G('ישראל (Israel)')]   # his hands upon him — Numbers 27:23's six shared; the son of Nun — 27:18's; 31:23's six; the spirit of wisdom — Exodus 28:3's and Isaiah 11:2's (cited never read); the children of Israel — 27:20's
assert SHARED(('Deut', 34, 10), ('Exod', 33, 11)) == [_G('פנים (face)'), _G('אל (to)'), _G('פנים (face)')] and SHN(('Deut', 34, 10), ('Exod', 33, 11)) == 4 and SHARED(('Deut', 34, 10), ('Gen', 32, 31)) == [_G('פנים (face)'), _G('אל (to)'), _G('פנים (face)')] and SHARED(('Deut', 34, 10), ('Judg', 6, 22)) == [_G('יהוה (the LORD)'), _G('פנים (face)'), _G('אל (to)'), _G('פנים (face)')] and SHARED(('Deut', 34, 10), ('Ezek', 20, 35)) == [_G('פנים (face)'), _G('אל (to)'), _G('פנים (face)')] and SHARED(('Deut', 34, 10), ('Num', 12, 8)) == [_G('ולא (and not)')] and SHARED(('Deut', 34, 10), ('Deut', 18, 15)) == [_G('נביא (a prophet)')] and SHARED(('Deut', 34, 10), ('Deut', 18, 18)) == [_G('נביא (a prophet)')]   # face to face — Exodus 33:11's, Jacob's at Peniel, Gideon's and Ezekiel's (cited never read); Numbers 12:8's mouth to mouth shares 'and not' alone — the twin by sense; a prophet — 18:15's and 18:18's
assert SHARED(('Deut', 34, 11), ('Exod', 7, 3)) == [_G('בארץ (in the land of)'), _G('מצרים (Egypt)')] and SHARED(('Deut', 34, 11), ('Jer', 32, 20)) == [_G('בארץ (in the land of)'), _G('מצרים (Egypt)')] and SHN(('Deut', 34, 11), ('Jer', 32, 20)) == 3 and SHARED(('Deut', 34, 12), ('Exod', 14, 31)) == [_G('אשר (which)'), _G('עשה (did)')] and SHN(('Deut', 34, 12), ('Exod', 14, 31)) == 3 and SHARED(('Deut', 34, 12), ('Deut', 4, 34)) == [_G('אשר (which)'), _G('עשה (did)')] and SHN(('Deut', 34, 12), ('Deut', 9, 17)) == 0 and SHARED(('Deut', 34, 12), ('Deut', 7, 19)) == [_G('החזקה (the mighty)')] and SHARED(('Deut', 34, 12), ('Deut', 3, 24)) == [_G('החזקה (the mighty)')]   # in the land of Egypt — Exodus 7:3's signs and Jeremiah 32:20's (cited never read); which … did — the great hand at the sea; 9:17's tablets broken share nothing (the Sifrei's own join); the mighty hand's seats
assert SHARED(('Deut', 34, 2), ('Deut', 11, 24)) == [_G('הים (the sea)'), _G('האחרון (the hinder)')] and SHARED(('Deut', 34, 3), ('2Chr', 28, 15)) == [_G('ירחו (Jericho)'), _G('עיר (the city of)'), _G('התמרים (the palms)')] and SHARED(('Deut', 34, 3), ('Judg', 3, 13)) == [_G('עיר (the city of)'), _G('התמרים (the palms)')] and SHARED(('Deut', 34, 3), ('Judg', 1, 16)) == [_G('התמרים (the palms)')]   # the hinder sea — 11:24's; Jericho the city of palms — the Writings' and the Prophets' seats cited never read
# THE FORMULAS: TWENTY-THREE phrases of the chapter ONCE in the Bible over the measure's list; THE PAIRS — "Mount Nebo" and "over against Jericho" 32:49 and 34:1 alone; "to your seed I will give it" Exodus 33:1 and 34:4 alone; "a hundred and twenty years old" 31:2 and 34:7 alone; "when he died" 34:7 and Numbers 33:39 (Aaron) alone; "thirty days" 34:8 and Numbers 20:29 (Aaron) alone; "to Pharaoh and to all his servants" 29:1 and 34:11 alone; "in the sight of all Israel" 31:7 and 34:12 in the Torah; "the servant of the LORD" ONCE IN THE TORAH and nineteen in the Bible; "and Moses went up" five — Sinai's four ascents and this last; "in the plains of Moab" eight; "by the mouth of the LORD" eighteen in the Torah; "as the LORD commanded Moses" thirty-eight in the Torah and 34:9 the last — THE RECEIPT; "face to face" three in the Torah; "the LORD your God" 192 seats in the Torah and NONE in the chapter; the Name SEVEN times bare, no "God"
Q34 = [(_G('מערבת (from the plains of)'), _G('מואב (Moab)')), (_G('ויראהו (and He showed him)'), _G('יהוה (the LORD)')), (_G('ואת (and the object marker)'), _G('כל (all)'), _G('נפתלי (Naphtali)')), (_G('ארץ (the land of)'), _G('אפרים (Ephraim)'), _G('ומנשה (and Manasseh)')), (_G('כל (all)'), _G('ארץ (the land of)'), _G('יהודה (Judah)')), (_G('בקעת (the valley of)'), _G('ירחו (Jericho)')), (_G('הראיתיך (I have caused you to see)'),), (_G('ושמה (and there)'), _G('לא (not)'), _G('תעבר (you shall cross over)')), (_G('וימת (and he died)'), _G('שם (there)'), _G('משה (Moses)')), (_G('ולא (and not)'), _G('ידע (knows)'), _G('איש (a man)')), (_G('קברתו (his grave)'),), (_G('לא (not)'), _G('כהתה (was dim)'), _G('עינו (his eye)')), (_G('ולא (and not)'), _G('נס (abated)'), _G('לחה (his natural force)')), (_G('ויבכו (and they wept)'), _G('בני (the children of)'), _G('ישראל (Israel)')), (_G('ימי (the days of)'), _G('בכי (weeping)')), (_G('אבל (the mourning of)'), _G('משה (Moses)')), (_G('מלא (full)'), _G('רוח (the spirit of)'), _G('חכמה (wisdom)')), (_G('סמך (had laid)'), _G('משה (Moses)'), _G('את (the object marker)'), _G('ידיו (his hands)'), _G('עליו (upon him)')), (_G('ולא (and not)'), _G('קם (arose)'), _G('נביא (a prophet)')), (_G('כמשה (like Moses)'),), (_G('אשר (whom)'), _G('ידעו (knew him)'), _G('יהוה (the LORD)')), (_G('היד (the hand)'), _G('החזקה (the mighty)')), (_G('המורא (the terror)'), _G('הגדול (the great)'))]   # the measure's list: from the plains of Moab … the great terror — twenty-three phrases once in the Bible
ONCE = [seq for seq in Q34 if len(P(*seq, books=None)) == 1 and P(*seq, books=None)[0].startswith('Deut 34:')]
assert len(ONCE) == 23 and len(Q34) == 23, (len(ONCE), [s for s in Q34 if s not in ONCE])
assert P(_G('הר (mount)'), _G('נבו (Nebo)'), books=None) == ['Deut 32:49', 'Deut 34:1'] and P(_G('על (over)'), _G('פני (against)'), _G('ירחו (Jericho)'), books=None) == ['Deut 32:49', 'Deut 34:1'] and P(_G('לזרעך (to your seed)'), _G('אתננה (I will give it)'), books=None) == ['Deut 34:4', 'Exod 33:1'] and P(_G('בן (aged)'), _G('מאה (a hundred)'), _G('ועשרים (and twenty)'), _G('שנה (years)'), books=None) == ['Deut 31:2', 'Deut 34:7'] and P(_G('במתו (when he died)'), books=None) == ['Deut 34:7', 'Num 33:39'] and P(_G('שלשים (thirty)'), _G('יום (days)'), books=None) == ['Deut 34:8', 'Num 20:29'] and P(_G('לפרעה (to Pharaoh)'), _G('ולכל (and to all)'), _G('עבדיו (his servants)'), books=None) == ['Deut 29:1', 'Deut 34:11'] and P(_G('לעיני (in the sight of)'), _G('כל (all)'), _G('ישראל (Israel)'), books=T) == ['Deut 31:7', 'Deut 34:12']   # the pairs: Mount Nebo; over against Jericho; to your seed I will give it; a hundred and twenty years old; when he died; thirty days; to Pharaoh and to all his servants; in the sight of all Israel
assert len(P(_G('עבד (the servant of)'), _G('יהוה (the LORD)'), books=T)) == 1 and len(P(_G('עבד (the servant of)'), _G('יהוה (the LORD)'), books=None)) == 19 and P(_G('ויעל (and he went up)'), _G('משה (Moses)'), books=None) == ['Deut 34:1', 'Exod 19:20', 'Exod 24:13', 'Exod 24:15', 'Exod 24:9'] and len(P(_G('בערבת (in the plains of)'), _G('מואב (Moab)'), books=None)) == 8 and 'Num 36:13' in P(_G('בערבת (in the plains of)'), _G('מואב (Moab)'), books=None) and len(P(_G('על (by)'), _G('פי (the mouth of)'), _G('יהוה (the LORD)'), books=T)) == 18 and 'Num 33:38' in P(_G('על (by)'), _G('פי (the mouth of)'), _G('יהוה (the LORD)'), books=T) and len(P(_G('כאשר (as)'), _G('צוה (commanded)'), _G('יהוה (the LORD)'), _G('את (the object marker)'), _G('משה (Moses)'), books=T)) == 38 and len(P(_G('פנים (face)'), _G('אל (to)'), _G('פנים (face)'), books=T)) == 3 and len(P(_G('פנים (face)'), _G('אל (to)'), _G('פנים (face)'), books=None)) == 5   # the servant of the LORD once in the Torah; and Moses went up five; in the plains of Moab eight (Numbers' footer among them); by the mouth of the LORD eighteen; as the LORD commanded Moses thirty-eight; face to face three in the Torah, five in the Bible
RECEIPT_SEATS = [s for s in P(_G('כאשר (as)'), _G('צוה (commanded)'), _G('יהוה (the LORD)'), _G('את (the object marker)'), _G('משה (Moses)'), books=T) if s.startswith('Deut 34:')]   # THE RECEIPT FORMULA's seats in the chapter — computed from the DB (the register census's receipt form; the finder's own count)
assert RECEIPT_SEATS == ['Deut 34:9'], RECEIPT_SEATS
assert P(_G('מול (over against)'), _G('בית (Beth)'), _G('פעור (Peor)'), books=None) == ['Deut 34:6', 'Deut 3:29', 'Deut 4:46'] and P(_G('רוח (the spirit of)'), _G('חכמה (wisdom)'), books=None) == ['Deut 34:9', 'Exod 28:3', 'Isa 11:2'] and P(_G('ויקבר (and He buried)'), _G('אתו (him)'), books=None) == ['2Kgs 21:26', 'Deut 34:6'] and P(_G('עד (as far as)'), _G('צער (Zoar)'), books=None) == ['Deut 34:3', 'Isa 15:5'] and P(_G('עיר (the city of)'), _G('התמרים (the palms)'), books=None) == ['2Chr 28:15', 'Deut 34:3', 'Judg 3:13'] and P(_G('הים (the sea)'), _G('האחרון (the hinder)'), books=T) == ['Deut 11:24', 'Deut 34:2'] and P(_G('עד (as far as)'), _G('דן (Dan)'), books=T) == ['Deut 34:1', 'Gen 14:14'] and len(P(_G('ראש (the top of)'), _G('הפסגה (Pisgah)'), books=None)) == 4   # over against Beth-peor three; the spirit of wisdom three; and He buried him two (the Writings' seat cited never read); as far as Zoar; the city of palms; the hinder sea; as far as Dan; the top of Pisgah four
assert len(P(_G('יהוה (the LORD)'), _G('אלהיך (your God)'), books=T)) == 192 and not [v for c, v in SPAN if any(a == _G('יהוה (the LORD)') and b == _G('אלהיך (your God)') for a, b in zip(W(c, v), W(c, v)[1:]))] and sum(1 for c, v in SPAN for x in W(c, v) if x == _G('יהוה (the LORD)')) == 7   # the LORD your God — 192 seats in the Torah and NONE in the chapter; the Name seven times bare
# THE NAMES AND THE PARTICLES (the measure's C): Moses eight times and "like Moses" once; Israel at 34:8, 9, 12 and "in Israel" 34:10; Moab four; "there" and "thither"; "all" nine; "as far as" four; no "God" — the two-letter "el" the PREPOSITION at 34:1 and 34:10 (a homograph of the Name's scans)
assert [(c, v) for c, v in SPAN for x in W(c, v) if x in (_G('משה (Moses)'), _G('ומשה (and Moses)'))] == [(34, 1), (34, 5), (34, 7), (34, 8), (34, 8), (34, 9), (34, 9), (34, 12)] and [(c, v, x) for c, v in SPAN for x in W(c, v) if x in (_G('שם (there)'), _G('ושמה (and there)'), _G('שמה (there)'))] == [(34, 4, _G('ושמה (and there)')), (34, 5, _G('שם (there)'))] and sum(1 for c, v in SPAN for x in W(c, v) if x in (_G('כל (all)'), _G('וכל (and all)'), _G('ולכל (and to all)'), _G('לכל (to all)'), _G('בכל (in all)'))) == 9 and sum(1 for c, v in SPAN for x in W(c, v) if x == _G('עד (as far as)')) == 4   # Moses eight; there and thither; all nine; as far as four
assert [(c, v) for c, v in SPAN if _G('ישראל (Israel)') in W(c, v)] == [(34, 8), (34, 9), (34, 12)] and _G('בישראל (in Israel)') in W(34, 10) and _G('כמשה (like Moses)') in W(34, 10) and [(c, v) for c, v in SPAN if _G('מואב (Moab)') in W(c, v)] == [(34, 1), (34, 5), (34, 6), (34, 8)] and _G('מערבת (from the plains of)') in W(34, 1) and _G('בערבת (in the plains of)') in W(34, 8)   # Israel at 34:8, 9, 12 and in Israel 34:10; Moab FOUR times (the plains at 34:1 and 34:8, the land at 34:5 and 34:6)
assert [(c, v, x) for c, v in SPAN for x in W(c, v) if x in NAME] == [(34, 1, _G('יהוה (the LORD)')), (34, 4, _G('יהוה (the LORD)')), (34, 5, _G('יהוה (the LORD)')), (34, 5, _G('יהוה (the LORD)')), (34, 9, _G('יהוה (the LORD)')), (34, 10, _G('יהוה (the LORD)')), (34, 11, _G('יהוה (the LORD)'))] and not any(x in (_G('אלהים (God)'), _G('האלהים (God)'), _G('אלהיך (your God)'), _G('אלהי (the God of)'), _G('אלוה (God)')) for c, v in SPAN for x in W(c, v)) and [(c, v) for c, v in SPAN if _G('אל (to)') in W(c, v)] == [(34, 1), (34, 10)]   # the Name SEVEN times bare; no God in the chapter — the two-letter el at 34:1 (to Mount Nebo) and 34:10 (face to face) the PREPOSITION, FALSE for the Name's scans
assert all(t in W(34, 1) for t in (_G('משה (Moses)'), _G('נבו (Nebo)'), _G('הפסגה (Pisgah)'), _G('ירחו (Jericho)'), _G('הגלעד (Gilead)'), _G('דן (Dan)'))) and all(t in W(34, 2) for t in (_G('נפתלי (Naphtali)'), _G('אפרים (Ephraim)'), _G('ומנשה (and Manasseh)'), _G('יהודה (Judah)'))) and _G('צער (Zoar)') in W(34, 3) and all(t in W(34, 4) for t in (_G('לאברהם (to Abraham)'), _G('ליצחק (to Isaac)'), _G('וליעקב (and to Jacob)'))) and _G('פעור (Peor)') in W(34, 6) and all(t in W(34, 9) for t in (_G('ויהושע (and Joshua)'), _G('נון (Nun)'))) and all(t in W(34, 11) for t in (_G('מצרים (Egypt)'), _G('לפרעה (to Pharaoh)')))   # the names: Nebo, Pisgah, Jericho, Gilead, Dan; Naphtali, Ephraim, Manasseh, Judah; Zoar; the three fathers; Peor; Joshua the son of Nun; Egypt, Pharaoh
assert W(34, 11)[:3] == [_G('לכל (for all)'), _G('האתות (the signs)'), _G('והמופתים (and the wonders)')] and W(34, 12)[:6] == [_G('ולכל (and to all)'), _G('היד (the hand)'), _G('החזקה (the mighty)'), _G('ולכל (and to all)'), _G('המורא (the terror)'), _G('הגדול (the great)')] and (len(W(34, 1)), len(W(34, 4)), len(W(34, 7)), len(W(34, 9)), len(W(34, 12))) == (22, 18, 12, 22, 12)   # the signs and the wonders; the mighty hand and the great terror; the verses' lengths

# ---- THE COUNTER'S DAY (a bare world on the exodus epoch; Moses' last day (40, 12, 7) — 19b's ONE MARKER at 31:1 stands, NO MARKER here; the death THAT day; the death date 19b's clock datum on the calendar's keys, read here; THE THIRTY DAYS A DURATION — no timer, the counter unmoved) ----
with contextlib.redirect_stdout(io.StringIO()):
    _WC = WE.World(era='Moses\' last day — chapter 34 on a bare world (the exodus epoch)', epoch='exodus')
_EX = _WC.clock.eras['exodus']
def DAY(y, m, d): return _WC.clock.day_in('exodus', y, m, d)
def DATE(day): return _EX.date(day)
MOSES_120 = DAY(40, 12, 7); COUNTER = MOSES_120
CLOCK = {'counter': DATE(COUNTER), 'marker': None, 'marker_verse': None, 'marker_at': None, 'days_walked': 0, 'the_day_by': "19b's marker at Deut 31:1 (the number's verse 31:2) — the_death_date_of_moses on the calendar's keys; the thirty days of weeping a DURATION, no timer (the design's ruling)", 'clock_data': ['the_death_date_of_moses']}
print('THE CLOCK (printed before it is asserted):', CLOCK)
assert CLOCK['counter'] == (40, 12, 7) and CLOCK['marker'] is None and CLOCK['days_walked'] == 0, CLOCK
assert all(k in WE.CAL_PARAMS for k in CLOCK['clock_data']), [k for k in CLOCK['clock_data'] if k not in WE.CAL_PARAMS]   # 19b's calendar parameter on file — the received channel
assert WE.CAL_PARAMS['the_death_date_of_moses']['exercised_by'] == ['covenant_return_charge'], WE.CAL_PARAMS['the_death_date_of_moses']['exercised_by']   # 19b's row UNTOUCHED (add_types_ch34_b.py — the calendar untouched)

# ---- THE ONE DATABASE SCANNED (the holes' ground — nothing names the twelve on their three ledgers before this sitting; the references' entities and counts as the spec computed them — DP3) ----
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
    """the entries of an effect in ONE full run of the tape (DP3's counts — the running world's): the one database folds several runs' rows under their sources (the checkpoint sections' names); the largest source is a whole run — None where the database is not built"""
    if not _os.path.exists(_WDB): return None
    c_ = sqlite3.connect('file:%s?mode=ro' % _WDB, uri=True)
    src = c_.execute("SELECT source FROM run_ledger GROUP BY source ORDER BY COUNT(*) DESC, source LIMIT 1").fetchone()[0]
    return c_.execute("SELECT COUNT(*) FROM run_ledger WHERE effect=? AND source=?", (effect, src)).fetchone()[0]
OWN12 = ('moses_went_up_to_nebo_as_commanded', 'the_whole_land_shown_to_moses_gilead_to_zoar', 'land_sworn_to_the_fathers_shown_at_the_end_declared', 'moses_died_by_the_mouth_of_the_lord', 'buried_by_the_lord_grave_unknown', 'three_gifts_merits_withdrawn_at_the_third_death', 'died_at_a_hundred_and_twenty_eye_undimmed', 'days_of_weeping_for_moses_ended', 'spirit_of_wisdom_by_the_hands_laid', 'israel_hearkened_to_joshua_as_the_lord_commanded_moses', 'no_prophet_like_moses_face_to_face_declared', 'signs_mighty_hand_great_terror_in_the_sight_of_all_israel_declared')
assert len(OWN12) == 12 and len(set(OWN12)) == 12
LEDGERS3 = ('moses', 'israel_people', 'yehoshua')
HOLE_WORDS = r"^(moses_went_up_to_nebo\w*|the_whole_land_shown\w*|land_sworn_to_the_fathers\w*|moses_died_by_the_mouth\w*|buried_by_the_lord\w*|three_gifts_merits\w*|died_at_a_hundred\w*|days_of_weeping_for_moses\w*|spirit_of_wisdom_by\w*|israel_hearkened_to_joshua\w*|no_prophet_like_moses_face\w*|signs_mighty_hand\w*)$"
_hs = {ent: ledger_scan(ent, HOLE_WORDS) for ent in LEDGERS3}; HOLE_SCAN = None if any(v is None for v in _hs.values()) else {ent: [e for e in v if e not in OWN12] for ent, v in _hs.items()}   # this sitting's own names excluded once the fold carries them
KIN24 = ('go_up_to_nebo_see_the_land_commanded', 'die_in_the_mountain_gathered_to_your_people_commanded', 'as_aaron_died_in_hor_and_was_gathered', 'see_the_land_from_afar_not_go_there', 'barred_from_the_land', 'gathered_to_his_people', 'mourned_thirty_days', 'garments_transferred', 'invested_office', 'joshua_commissioned_to_bring_israel_in', 'joshua_charged_to_bring_israel_in', 'lord_with_joshua_promised', 'moses_to_sleep_with_the_fathers', 'corruption_after_moses_death_foretold', 'prophet_like_moses_promised', 'face_radiant', 'signs_in_hand', 'manna_provided', 'well_given', 'camp_moves_by_the_cloud', 'bones_oath', 'buried', 'wept', 'blessing_given_before_moses_death')
KIN_EXPECTED = (1, 1, 1, 1, 2, 5, 1, 1, 6, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 1, 9, 12, 1)   # DP3 BEFORE — the spec's KIN_BEFORE computed on the one database at the design (ch34b_spec.out); the probe Q51's KIN tuple holds KIN_AFTER (the three reuses +1)
assert len(KIN24) == 24 == len(KIN_EXPECTED)
KIN_COUNTS = {k: count_scan(k) for k in KIN24}
REUSE3 = ('see_the_land_from_afar_not_go_there', 'gathered_to_his_people', 'mourned_thirty_days')   # THE THREE REUSES at their own forward seats — the denial 32:52 -> 34:4 (a heaven entry), the gathering 32:50 -> 34:5 (Aaron's word, a status), Aaron's thirty days Numbers 20:29 -> 34:8 (the timer row, written without a due)
REUSE_BEFORE = {'see_the_land_from_afar_not_go_there': 1, 'gathered_to_his_people': 5, 'mourned_thirty_days': 1}   # the spec's REUSE_BEFORE (computed, printed)
REUSE_AFTER = {'see_the_land_from_afar_not_go_there': 2, 'gathered_to_his_people': 6, 'mourned_thirty_days': 2}    # the spec's REUSE_AFTER — the tape's print decides (DP3)
REUSE_COUNTS = {k: count_scan(k) for k in REUSE3}
SCANS = {k: effect_scan(k) for k in KIN24[:9] + ('garments_transferred_and_aaron_died', 'blessing_given_before_moses_death', 'prophet_like_moses_promised', 'face_radiant', 'bones_oath')}
del _hs   # 9b's lesson: the raw scans are the database's state at import — the derived lists are equal on the cached and the full load
_FXV = yaml.safe_load(open(_os.path.join(HERE, 'effect_vocabulary.yaml'), encoding='utf-8'))['effects']
print('THE SCANS (printed before they are asserted): holes %s; the kin counts %s; the reuses %s; the entities %s' % (HOLE_SCAN, KIN_COUNTS, REUSE_COUNTS, SCANS))
assert HOLE_SCAN is None or all(v == [] for v in HOLE_SCAN.values()), HOLE_SCAN   # THE HOLES' GROUND — nothing on the three ledgers named the twelve before this sitting (DP3)
assert all(v is None for v in KIN_COUNTS.values()) or tuple(KIN_COUNTS.values()) == KIN_EXPECTED or tuple(KIN_COUNTS.values()) == tuple(KIN_EXPECTED[i] + (1 if k in REUSE3 else 0) for i, k in enumerate(KIN24)), [(k, KIN_COUNTS[k], e) for k, e in zip(KIN24, KIN_EXPECTED) if KIN_COUNTS[k] != e]   # the references' counts as the spec computed them (DP3 — before the tape's run; after it the three reuses +1, the fold carrying this chapter's lines)
assert all(v is None for v in REUSE_COUNTS.values()) or REUSE_COUNTS == REUSE_BEFORE or REUSE_COUNTS == REUSE_AFTER, REUSE_COUNTS   # the three reuses' counts: BEFORE at this run, AFTER once the fold carries the chapter (the tape's print decides)
SCANS_EXPECTED = {'go_up_to_nebo_see_the_land_commanded': ['moses'], 'die_in_the_mountain_gathered_to_your_people_commanded': ['moses'], 'as_aaron_died_in_hor_and_was_gathered': ['moses'], 'see_the_land_from_afar_not_go_there': ['moses'], 'barred_from_the_land': ['aaron', 'moses'], 'gathered_to_his_people': ['aaron', 'abraham', 'isaac', 'ishmael', 'jacob', 'moses'], 'mourned_thirty_days': ['israel_people'], 'garments_transferred': ['aaron'], 'invested_office': ['aaron-and-sons', 'eleazar_son_of_aaron', 'pinchas', 'the-firstborn', 'the_levites', 'yehoshua'], 'garments_transferred_and_aaron_died': [], 'blessing_given_before_moses_death': ['israel_people'], 'prophet_like_moses_promised': ['israel_people'], 'face_radiant': ['moses'], 'bones_oath': ['israel_people']}   # THE DEUTERONOMY WALK 22b (2026-09-30/10-01; LEAN): the entity lists MOVED BY THE DEATH'S REUSES — gathered_to_his_people ['aaron', 'abraham', 'isaac', 'ishmael', 'jacob'] -> ['aaron', 'abraham', 'isaac', 'ishmael', 'jacob', 'moses'] — retyped from the one database's own print after the fold carried chapter 34 (the chain's first pass fell at this assert on the tape, the probes and the register gate: 20b's precedent); the prior literal the entities per effect — typed from the first derive's print by patch_part1_ch34.py (the callees' way — printed before typed)
if SCANS_EXPECTED and any(v is not None for v in SCANS.values()): assert SCANS == SCANS_EXPECTED, [(k, SCANS[k], SCANS_EXPECTED.get(k)) for k in SCANS if SCANS[k] != SCANS_EXPECTED.get(k)]
assert all(k in _FXV for k in OWN12) and sum(1 for k in OWN12 if _FXV[k]['ledger_op'] == 'block') == 0 and sum(1 for k in OWN12 if _FXV[k]['ledger_op'] == 'status') == 12 and sum(1 for k in OWN12 if _FXV[k]['ledger_op'] == 'heaven') == 0, 'the twelve on the registry (add_types_ch34_a.py)'
assert _FXV['see_the_land_from_afar_not_go_there']['ledger_op'] == 'heaven' and _FXV['gathered_to_his_people']['ledger_op'] == 'status' and _FXV['mourned_thirty_days']['ledger_op'] == 'timer' and _FXV['barred_from_the_land']['ledger_op'] == 'heaven', 'the reused rows\' ops (read from the registry at the types — the thirty days a TIMER row, written here WITHOUT A DUE: no timer set)'
assert all(_FXV[e].get(s) for e, s in (('see_the_land_from_afar_not_go_there', 'second_seat'), ('gathered_to_his_people', 'sixth_seat'), ('mourned_thirty_days', 'second_seat'))), 'the reused rows amended with their forward seats (add_types_ch34_a.py)'
# THE TWINS DIFFED on the DB (the reading's kin asserts read again here — DP3; the shared run SH)
TWIN = {'34:4 vs Exod 33:1': SH(DV(34, 4), ('Exod', 33, 1)), '34:4 vs 6:10': SH(DV(34, 4), DV(6, 10)), '34:4 vs 3:27': SH(DV(34, 4), DV(3, 27)), '34:4 vs 32:52': SH(DV(34, 4), DV(32, 52)), '34:1 vs 32:49': SH(DV(34, 1), DV(32, 49)), '34:1 vs 3:27': SH(DV(34, 1), DV(3, 27)), '34:1 vs Num 27:12': SH(DV(34, 1), ('Num', 27, 12)),
        '34:5 vs Num 33:38': SH(DV(34, 5), ('Num', 33, 38)), '34:5 vs 32:50': SH(DV(34, 5), DV(32, 50)), '34:5 vs Josh 1:1': SH(DV(34, 5), ('Josh', 1, 1)), '34:5 vs Num 20:28': SH(DV(34, 5), ('Num', 20, 28)), '34:6 vs 3:29': SH(DV(34, 6), DV(3, 29)), '34:6 vs 33:21': SH(DV(34, 6), DV(33, 21)), '34:6 vs Gen 50:13': SH(DV(34, 6), ('Gen', 50, 13)),
        '34:7 vs 31:2': SH(DV(34, 7), DV(31, 2)), '34:7 vs Gen 6:3': SH(DV(34, 7), ('Gen', 6, 3)), '34:7 vs Num 33:39': SH(DV(34, 7), ('Num', 33, 39)), '34:7 vs Exod 34:29': SH(DV(34, 7), ('Exod', 34, 29)), '34:8 vs Num 20:29': SH(DV(34, 8), ('Num', 20, 29)), '34:8 vs Num 6:4': SH(DV(34, 8), ('Num', 6, 4)), '34:8 vs Num 36:13': SH(DV(34, 8), ('Num', 36, 13)),
        '34:9 vs Num 27:23': SH(DV(34, 9), ('Num', 27, 23)), '34:9 vs Num 27:18': SH(DV(34, 9), ('Num', 27, 18)), '34:9 vs 31:23': SH(DV(34, 9), DV(31, 23)), '34:9 vs 31:7': SH(DV(34, 9), DV(31, 7)), '34:9 vs Exod 28:3': SH(DV(34, 9), ('Exod', 28, 3)), '34:9 vs Exod 12:28': SH(DV(34, 9), ('Exod', 12, 28)),
        '34:10 vs Exod 33:11': SH(DV(34, 10), ('Exod', 33, 11)), '34:10 vs Num 12:8': SH(DV(34, 10), ('Num', 12, 8)), '34:10 vs 18:15': SH(DV(34, 10), DV(18, 15)), '34:10 vs 18:18': SH(DV(34, 10), DV(18, 18)), '34:11 vs Exod 7:3': SH(DV(34, 11), ('Exod', 7, 3)), '34:11 vs 29:1': SH(DV(34, 11), DV(29, 1)), '34:12 vs Exod 14:31': SH(DV(34, 12), ('Exod', 14, 31)), '34:12 vs 9:17': SH(DV(34, 12), DV(9, 17)), '34:12 vs 31:7': SH(DV(34, 12), DV(31, 7)), '34:12 vs 4:34': SH(DV(34, 12), DV(4, 34)),
        '34:2 vs 11:24': SH(DV(34, 2), DV(11, 24)), '34:3 vs 2Chr 28:15': SH(DV(34, 3), ('2Chr', 28, 15)), '34:1 vs Gen 14:14': SH(DV(34, 1), ('Gen', 14, 14))}
print('THE TWINS DIFFED (printed before they are asserted):', TWIN)
TWIN_EXPECTED = {'34:4 vs Exod 33:1': 10, '34:4 vs 6:10': 7, '34:4 vs 3:27': 3, '34:4 vs 32:52': 2, '34:1 vs 32:49': 8, '34:1 vs 3:27': 3, '34:1 vs Num 27:12': 4, '34:5 vs Num 33:38': 3, '34:5 vs 32:50': 0, '34:5 vs Josh 1:1': 4, '34:5 vs Num 20:28': 3, '34:6 vs 3:29': 3, '34:6 vs 33:21': 0, '34:6 vs Gen 50:13': 2, '34:7 vs 31:2': 5, '34:7 vs Gen 6:3': 3, '34:7 vs Num 33:39': 4, '34:7 vs Exod 34:29': 2, '34:8 vs Num 20:29': 4, '34:8 vs Num 6:4': 1, '34:8 vs Num 36:13': 4, '34:9 vs Num 27:23': 6, '34:9 vs Num 27:18': 5, '34:9 vs 31:23': 6, '34:9 vs 31:7': 3, '34:9 vs Exod 28:3': 3, '34:9 vs Exod 12:28': 7, '34:10 vs Exod 33:11': 4, '34:10 vs Num 12:8': 2, '34:10 vs 18:15': 2, '34:10 vs 18:18': 2, '34:11 vs Exod 7:3': 2, '34:11 vs 29:1': 9, '34:12 vs Exod 14:31': 3, '34:12 vs 9:17': 0, '34:12 vs 31:7': 4, '34:12 vs 4:34': 2, '34:2 vs 11:24': 3, '34:3 vs 2Chr 28:15': 3, '34:1 vs Gen 14:14': 3}   # typed from the first derive's print by patch_part1_ch34.py (the callees' way — printed before typed)
if TWIN_EXPECTED: assert TWIN == TWIN_EXPECTED, [(k, TWIN[k], TWIN_EXPECTED.get(k)) for k in TWIN if TWIN[k] != TWIN_EXPECTED.get(k)]
assert TWIN['34:4 vs Exod 33:1'] >= 9 and TWIN['34:1 vs 32:49'] >= 8 and TWIN['34:9 vs Num 27:23'] >= 6 and TWIN['34:7 vs 31:2'] >= 5 and TWIN['34:5 vs 32:50'] == 0 and TWIN['34:6 vs 33:21'] == 0 and TWIN['34:12 vs 9:17'] == 0, TWIN   # the reading's largest twins (the oath nine in order, the summons eight, the hands laid six, the years five) and the three twins by sense without a shared token

# ---- THE CALLEES' FACTS (every edge live at the cells that consume them; the values PRINTED at the first pass and ASSERTED from that print at the second — 10b's lesson 2, the callees' way; the q-style cells called with their keys, an absent key printed, never guessed silently; EVERY CALLEE CALLED BY ITS LITERAL NAME `alias.name(` — the dependency gate reads the source, a DATA read is not a live edge (19b's lesson); the bindings ASSIGNMENTS, never a helper writing globals() — 20b's tail lesson) ----
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
# song_charge_nebo — the summons 32:49 OBEYED at 34:1 (a RUN CITATION), the death 32:50 COMMANDED (a STATUS on moses), the denial 32:52 REUSED at 34:4; Aaron's death the receipt; the_readback's fifty-two rows the form
SC_DEATH = DK(SC, 'moses_death_ahead'); F('SC_DEATH', SC_DEATH); SC_RB = DK(SC, 'the_readback'); F('SC_RB', SC_RB); SC_AARON = DK(SC, 'aarons_death_the_receipt'); F('SC_AARON', SC_AARON)
SC_GOUP = SC.the_summons_to_nebo({'ask': 'go_up_into_this_mountain_of_abarim_mount_nebo_and_behold_the_land_of_canaan'}, DD(SC)); F('SC_GOUP', SC_GOUP); SC_NEBO = SC.the_summons_to_nebo({'ask': 'die_in_the_mount_where_you_go_up_and_be_gathered_to_your_people'}, DD(SC)); F('SC_NEBO', SC_NEBO)
SC_ASAARON = SC.the_summons_to_nebo({'ask': 'as_aaron_your_brother_died_in_mount_hor_and_was_gathered_to_his_people'}, DD(SC)); F('SC_ASAARON', SC_ASAARON); SC_DENIAL = SC.meribah_and_the_seeing({'ask': 'you_shall_see_the_land_before_you_but_there_you_shall_not_go'}, DD(SC)); F('SC_DENIAL', SC_DENIAL); SC_TABLE = SC.the_readback({'ask': 'the_table'}, DD(SC)); F('SC_TABLE', SC_TABLE)
# covenant_return_charge — 31:2's hundred and twenty on the marker's day (34:7), the death date (the seventh of Adar), the three gifts and their merits (the daemon owed), Joshua's charge and commission (31:7, 31:23 — 34:9), 'you shall sleep with your fathers' (31:16), the corruption after the death (31:29)
CR_120 = CR.the_charge_and_the_crossing({'ask': 'a_hundred_and_twenty_years_old_this_day'}, DD(CR)); F('CR_120', CR_120); CR_CALLED = CR.the_charge_and_the_crossing({'ask': 'moses_called_joshua_in_the_sight_of_all_israel'}, DD(CR)); F('CR_CALLED', CR_CALLED)
CR_COMM = CR.the_tent_and_the_commission({'ask': 'he_commissioned_joshua_be_strong_and_of_good_courage'}, DD(CR)); F('CR_COMM', CR_COMM); CR_BRING = CR.the_tent_and_the_commission({'ask': 'you_shall_bring_the_children_of_israel_into_the_land_i_swore'}, DD(CR)); F('CR_BRING', CR_BRING)
CR_SLEEP = CR.the_apostasy_foretold({'ask': 'you_shall_sleep_with_your_fathers'}, DD(CR)); F('CR_SLEEP', CR_SLEEP); CR_AFTER = CR.the_book_beside_the_ark_and_the_assembly({'ask': 'after_my_death_you_will_corrupt_and_turn_evil_will_befall_you'}, DD(CR)); F('CR_AFTER', CR_AFTER)
CR_DEATH = DK(CR, 'the_death_date_of_moses'); F('CR_DEATH', CR_DEATH); CR_GIFTS = DK(CR, 'the_three_gifts_and_their_merits'); F('CR_GIFTS', CR_GIFTS)
# blessing_of_moses — MOSES' GRAVE AHEAD (33:21 -> 34:6, the pointer PAID), the chain of transmission (Avot 1:1 — 34:9's 'received'), the pointers ahead, the law the inheritance (33:4), the lawgiver's portion (33:21)
BL_GRAVE = DK(BL, 'moses_grave_ahead'); F('BL_GRAVE', BL_GRAVE); BL_CHAIN = DK(BL, 'the_chain_of_transmission'); F('BL_CHAIN', BL_CHAIN); BL_AHEAD = DK(BL, 'the_pointers_ahead'); F('BL_AHEAD', BL_AHEAD)
BL_LAW = BL.the_prologue_law_and_king({'ask': 'moses_commanded_us_a_law_the_inheritance_of_the_congregation_of_jacob'}, DD(BL)); F('BL_LAW', BL_LAW); BL_PORTION = BL.the_gad_lioness_and_the_lawgivers_portion({'ask': 'he_chose_a_first_part_for_himself_for_there_a_portion_of_a_ruler_was_reserved'}, DD(BL)); F('BL_PORTION', BL_PORTION)
# gad_reuben — MOSES' GRAVE (Reuben's Nebo, Gad's field — Sotah 13b), the deaths ceased, the cities (the grave's ask)
GR_GRAVE = DK(GR, 'moses_grave'); F('GR_GRAVE', GR_GRAVE); GR_CEASED = DK(GR, 'deaths_ceased'); F('GR_CEASED', GR_CEASED); GR_CITY = GR.the_cities({'ask': 'moses_grave'}, DD(GR)); F('GR_CITY', GR_CITY)
# chukat — AARON'S DEATH (the dates, the succession, the thirty days, the age), Miriam's well by merit (the three gifts' first event), the kiss, the burial near the death, the sentence at Meribah (read, not rewritten), 'there'/'there'
CK_DATES = CK.edom_and_hor({'ask': 'death_dates'}, DD(CK)); F('CK_DATES', CK_DATES); CK_SUCC = CK.edom_and_hor({'ask': 'succession'}, DD(CK)); F('CK_SUCC', CK_SUCC); CK_THIRTY = CK.edom_and_hor({'ask': 'thirty_days'}, DD(CK)); F('CK_THIRTY', CK_THIRTY); CK_AGE = CK.edom_and_hor({'ask': 'aaron_age'}, DD(CK)); F('CK_AGE', CK_AGE)
CK_WELL = CK.meribah({'ask': 'well_by_merit'}, DD(CK)); F('CK_WELL', CK_WELL); CK_KISS = CK.meribah({'ask': 'death_by_the_kiss'}, DD(CK)); F('CK_KISS', CK_KISS); CK_BURIAL = CK.meribah({'ask': 'burial_near_death'}, DD(CK)); F('CK_BURIAL', CK_BURIAL); CK_SENT = CK.meribah({'ask': 'sentence'}, DD(CK)); F('CK_SENT', CK_SENT); CK_THERE = CK.meribah({'ask': 'there_there'}, DD(CK)); F('CK_THERE', CK_THERE)
CK_WELLD = DK(CK, 'well_by_merit'); F('CK_WELLD', CK_WELLD); CK_MOURNED = DK(CK, 'aaron_mourned_by_all'); F('CK_MOURNED', CK_MOURNED); CK_MANNA = DK(CK, 'manna_absorbed'); F('CK_MANNA', CK_MANNA)
# journeys — Aaron's death RETOLD (33:38-39: the date, by the mouth — the kiss, Moses' seventh of Adar, the verbal analogy, no write), the death date, Aaron's age
JR_DATE = JR.aarons_death_retold({'ask': 'the_date'}, DD(JR)); F('JR_DATE', JR_DATE); JR_MOUTH = JR.aarons_death_retold({'ask': 'by_the_mouth_kiss'}, DD(JR)); F('JR_MOUTH', JR_MOUTH); JR_ADAR = JR.aarons_death_retold({'ask': 'moses_seventh_adar'}, DD(JR)); F('JR_ADAR', JR_ADAR)
JR_ANALOGY = JR.aarons_death_retold({'ask': 'verbal_analogy'}, DD(JR)); F('JR_ANALOGY', JR_ANALOGY); JR_NOWRITE = JR.aarons_death_retold({'ask': 'no_write'}, DD(JR)); F('JR_NOWRITE', JR_NOWRITE); JR_DDATE = DK(JR, 'the_death_date'); F('JR_DDATE', JR_DDATE); JR_AGE = DK(JR, 'aarons_age'); F('JR_AGE', JR_AGE)
# second_tablets — the burial by the LORD among His attributes (Sotah 14a — 34:6), Aaron buried there (10:6), the place of the death, the fragments in the ark (9:17's tablets broken — 34:12 by the Sifrei 357:44), the receipt 10:5 (the precedent's class), the charge to Joshua
ST_WALK = ST.the_stations_and_the_death({'ask': 'walk_after_his_attributes'}, DD(ST)); F('ST_WALK', ST_WALK); ST_BURIED = ST.the_stations_and_the_death({'ask': 'and_he_was_buried_there'}, DD(ST)); F('ST_BURIED', ST_BURIED); ST_PLACE = ST.the_stations_and_the_death({'ask': 'the_place_of_the_death'}, DD(ST)); F('ST_PLACE', ST_PLACE)
ST_FRAG = ST.the_tablets_and_the_ark({'ask': 'the_fragments_in_the_ark'}, DD(ST)); F('ST_FRAG', ST_FRAG); ST_R105 = ST.the_tablets_and_the_ark({'ask': 'the_receipt_10_5'}, DD(ST)); F('ST_R105', ST_R105); ST_ATTR = DK(ST, 'the_burial_among_the_attributes'); F('ST_ATTR', ST_ATTR); ST_CHARGE = DK(ST, 'the_charge_to_joshua'); F('ST_CHARGE', ST_CHARGE)
# zelophehad — THE COMMISSION Numbers 27:18-23 (the chapter's runner — the run, the execution; the reach), invested_office on yehoshua the receipt's referent
ZE_RUN = ZE.the_daughters({'ask': 'the_run'}, DD(ZE)); F('ZE_RUN', ZE_RUN); ZE_EXEC = ZE.the_daughters({'ask': 'execution'}, DD(ZE)); F('ZE_EXEC', ZE_EXEC); ZE_REACH = DK(ZE, 'tribe_transfer_reach'); F('ZE_REACH', ZE_REACH)
# opening_speech — THE COMMISSION (the mountain, the hand laid, the receipt, the debit PAID at 34:4, the honor), THE PLEA (Pisgah 3:27 — 34:1; Beth-peor 3:29 — 34:6; command Joshua; the refusal)
OS_MTN = OS.the_commission({'ask': 'the_mountain'}, DD(OS)); F('OS_MTN', OS_MTN); OS_HAND = OS.the_commission({'ask': 'the_hand_laid'}, DD(OS)); F('OS_HAND', OS_HAND); OS_RECEIPT = OS.the_commission({'ask': 'the_receipt'}, DD(OS)); F('OS_RECEIPT', OS_RECEIPT); OS_DEBIT = OS.the_commission({'ask': 'the_debit'}, DD(OS)); F('OS_DEBIT', OS_DEBIT)
OS_PISGAH = OS.the_plea({'ask': 'pisgah'}, DD(OS)); F('OS_PISGAH', OS_PISGAH); OS_PEOR = OS.the_plea({'ask': 'beth_peor'}, DD(OS)); F('OS_PEOR', OS_PEOR); OS_CMDJ = OS.the_plea({'ask': 'command_joshua'}, DD(OS)); F('OS_CMDJ', OS_CMDJ); OS_REFUSAL = OS.the_plea({'ask': 'the_refusal'}, DD(OS)); F('OS_REFUSAL', OS_REFUSAL); OS_COMM = DK(OS, 'the_commission'); F('OS_COMM', OS_COMM)
# beha — THE THREE GIFTS by three merits (Taanit 9a), the manna fell, Miriam's 'mouth to mouth' (12:8 — 34:10's twin by sense), as one dead, measure for measure, the spirit on the seventy
BH_GIFTS = BH.taberah_and_quail({'ask': 'three_gifts'}, DD(BH)); F('BH_GIFTS', BH_GIFTS); BH_FELL = BH.taberah_and_quail({'ask': 'manna_fell'}, DD(BH)); F('BH_FELL', BH_FELL); BH_DIBBUR = BH.miriam({'ask': 'dibbur'}, DD(BH)); F('BH_DIBBUR', BH_DIBBUR)
BH_DEAD = BH.miriam({'ask': 'as_one_dead'}, DD(BH)); F('BH_DEAD', BH_DEAD); BH_MEASURE = BH.miriam({'ask': 'measure_for_measure'}, DD(BH)); F('BH_MEASURE', BH_MEASURE); BH_SPIRIT = BH.seventy_elders({'ask': 'spirit'}, DD(BH)); F('BH_SPIRIT', BH_SPIRIT); BH_CLOUDS = DK(BH, 'seven_clouds'); F('BH_CLOUDS', BH_CLOUDS)
# naso — THE NAZIRITE'S TERM (the thirty days from 34:8 by I2 — Nazir 1:3), the default days the callee's own row
NS_TERM = NS.nazirite({'ask': 'term', 'form': 'unspecified'}, DD(NS)); F('NS_TERM', NS_TERM); NS_DAYS = DK(NS, 'nazir_default_days'); F('NS_DAYS', NS_DAYS)   # the term's ask takes a form — 'unspecified' (Nazir 1:3's first arm; the first pass's KeyError 'form'); the second pass's NameError NS_DAYS — the fix's comment had swallowed the line's tail
# courts_prophet — THE PROPHET (18:15 from your midst, of your brothers; 18:18 My words in his mouth; the test by the event), the prophets' order, the succession
CP_MIDST = CP.the_prophet({'ask': 'from_your_midst_of_your_brothers'}, DD(CP)); F('CP_MIDST', CP_MIDST); CP_WORDS = CP.the_prophet({'ask': 'my_words_in_his_mouth'}, DD(CP)); F('CP_WORDS', CP_WORDS); CP_TEST = CP.the_prophet({'ask': 'the_test_by_the_event'}, DD(CP)); F('CP_TEST', CP_TEST)
CP_ORDER = DK(CP, 'the_prophets_order'); F('CP_ORDER', CP_ORDER); CP_SUCC = DK(CP, 'the_succession'); F('CP_SUCC', CP_SUCC)
# erection — the presence (the pillar's face — Exodus 33:11's face to face), the tablets (the breaking ratified — 9:17's tablets broken; the radiance — 34:29's shining face, 34:7's undimmed eye; Sinai's reading), the calf (the three deaths; the plague)
ER_FACE = ER.presence('pillar_face'); F('ER_FACE', ER_FACE); ER_AVOT = ER.presence('sheet_avot_1_1'); F('ER_AVOT', ER_AVOT); ER_BREAK = ER.tablets('breaking_ratified'); F('ER_BREAK', ER_BREAK); ER_RADIANCE = ER.tablets('radiance'); F('ER_RADIANCE', ER_RADIANCE)
ER_FRAG = ER.tablets('fragments_by_call'); F('ER_FRAG', ER_FRAG); ER_3DEATHS = ER.calf('three_deaths'); F('ER_3DEATHS', ER_3DEATHS); ER_PLAGUE = ER.calf('plague'); F('ER_PLAGUE', ER_PLAGUE)
# exodus_story — the signs (the count, the seats of believing), the plagues (ten), the sea (the ten at the sea, the bones — Joseph's), the birth (the seventh of Adar — Moses' birthday and death day)
ES_SIGNS = ES.signs('count'); F('ES_SIGNS', ES_SIGNS); ES_BELIEVED = ES.signs('believed_seats'); F('ES_BELIEVED', ES_BELIEVED); ES_TEN = ES.plagues('ten'); F('ES_TEN', ES_TEN); ES_SEA = ES.sea('ten_at_sea'); F('ES_SEA', ES_SEA); ES_BONES = ES.sea('bones'); F('ES_BONES', ES_BONES); ES_BIRTH = ES.birth('birthday'); F('ES_BIRTH', ES_BIRTH)
# joseph — JOSEPH'S BONES (the oath sworn, the burial command's seat, the oath closed on the tape; the coffin — the bones closed on the tape, 'with you when you go up'), the three deaths (buried by both, the gathering's seat)
JO_OATH = JO.the_oath('oath_sworn'); F('JO_OATH', JO_OATH); JO_CMD = JO.the_oath('burial_command_seat'); F('JO_CMD', JO_CMD); JO_CLOSED = JO.the_oath('oath_closed_on_tape'); F('JO_CLOSED', JO_CLOSED)
JO_BONES = JO.coffin('bones_closed_on_tape'); F('JO_BONES', JO_BONES); JO_WITHYOU = JO.coffin('with_you_when_you_go_up'); F('JO_WITHYOU', JO_WITHYOU); JO_BOTH = JO.three_deaths('buried_by_both'); F('JO_BOTH', JO_BOTH); JO_GATHERED = JO.three_deaths('gathered_seat'); F('JO_GATHERED', JO_GATHERED)
# family — the testament (gathered — the formula's Genesis seats; buried named; the burial command), the purchase (possession by burial — Machpelah's holding)
FA_GATHERED = FA.testament('gathered'); F('FA_GATHERED', FA_GATHERED); FA_BURIED = FA.testament('buried_named'); F('FA_BURIED', FA_BURIED); FA_CMD = FA.testament('burial_command'); F('FA_CMD', FA_CMD); FA_POSS = FA.purchase('possession_by_burial'); F('FA_POSS', FA_POSS)
# mamre — the three men (18:2), Abraham's end (the seed multiplied closed, the promise closed here — 34:4's oath to Abraham)
MA_THREE = MA.mamre('three_men'); F('MA_THREE', MA_THREE); MA_SEED = MA.abraham_end('seed_multiplied_closed'); F('MA_SEED', MA_SEED); MA_PROMISE = MA.abraham_end('promise_closed_here'); F('MA_PROMISE', MA_PROMISE)
# hear_o_israel — the receipt's form (6:20-25's son's question — the receipt without the Name), the oath by the Name (6:13 — 34:4's 'which I swore')
HI_RECEIPT = HI.the_sons_question({'ask': 'the_receipt'}, DD(HI)); F('HI_RECEIPT', HI_RECEIPT); HI_OATH = DK(HI, 'the_oath_by_the_name'); F('HI_OATH', HI_OATH); HI_NONAME = DK(HI, 'the_receipt_without_the_name'); F('HI_NONAME', HI_NONAME)
# obey_horeb — Baal-peor seen (4:3 — 34:6's Beth-peor), the witnesses' chain, the second frame (4:44)
OH_PEOR = OH.the_exhortation({'ask': 'baal_peor_seen'}, DD(OH)); F('OH_PEOR', OH_PEOR); OH_CHAIN = DK(OH, 'the_witnesses_chain'); F('OH_CHAIN', OH_CHAIN); OH_FRAME = DK(OH, 'the_second_frame'); F('OH_FRAME', OH_FRAME)
# shelach — Hoshea to Joshua (13:16), Joshua and Caleb equal, the deaths ceased
SH_NAME = SHL.spies({'ask': 'joshua_name'}, DD(SHL)); F('SH_NAME', SH_NAME); SH_EQUAL = SHL.spies({'ask': 'joshua_caleb_equal'}, DD(SHL)); F('SH_EQUAL', SH_EQUAL); SH_CEASED = DK(SHL, 'deaths_ceased'); F('SH_CEASED', SH_CEASED)   # the alias SHL — SH is the shared-run measure (the first pass's AttributeError: 'function' object has no attribute 'spies')
print('THE CALLEES\' FACTS (printed before they are asserted — %d):' % len(FACTS_PRINT))
for _n, _v in FACTS_PRINT: print('  FACT %s = %s' % (_n, repr(_v)[:150]))
# ---- THE FACTS ASSERTED FROM THE FIRST PASS'S PRINT (parse_ch34_fastcheck.py writes ch34_fact_asserts.py from ch34_fastcheck_run0.out — the repr's first sixty characters; patch_part1_ch34.py pastes them below this line; a moved callee fails here, not in a cell) ----
_FV = dict(FACTS_PRINT)
assert repr(_FV['SC_DEATH'])[:60] == "{'the_command': 'Deut 32:50 — die in the mount and be gather", ('SC_DEATH', repr(_FV['SC_DEATH'])[:100])
assert repr(_FV['SC_RB'])[:60] == "[{'verses': 'Deut 32:1', 'told': 'give ear, O heavens, and I", ('SC_RB', repr(_FV['SC_RB'])[:100])
assert repr(_FV['SC_AARON'])[:60] == "{'the_tape': 'Numbers 20:28 — garments_transferred_and_aaron", ('SC_AARON', repr(_FV['SC_AARON'])[:100])
assert repr(_FV['SC_GOUP'])[:60] == '"go up into this mountain of Abarim, Mount Nebo, and behold ', ('SC_GOUP', repr(_FV['SC_GOUP'])[:100])
assert repr(_FV['SC_NEBO'])[:60] == '"die in the mount where you go up, and be gathered to your p', ('SC_NEBO', repr(_FV['SC_NEBO'])[:100])
assert repr(_FV['SC_ASAARON'])[:60] == '"as Aaron your brother died in Mount Hor and was gathered to', ('SC_ASAARON', repr(_FV['SC_ASAARON'])[:100])
assert repr(_FV['SC_DENIAL'])[:60] == '"you shall see the land before you, but there you shall not ', ('SC_DENIAL', repr(_FV['SC_DENIAL'])[:100])
assert repr(_FV['SC_TABLE'])[:60] == "'the readback table (32:1-52) — 52 rows one per verse, SHORT", ('SC_TABLE', repr(_FV['SC_TABLE'])[:100])
assert repr(_FV['CR_120'])[:60] == '"a hundred and twenty years old this day (31:2) — the parser', ('CR_120', repr(_FV['CR_120'])[:100])
assert repr(_FV['CR_CALLED'])[:60] == '"Moses called Joshua in the sight of all Israel (31:7) — the', ('CR_CALLED', repr(_FV['CR_CALLED'])[:100])
assert repr(_FV['CR_COMM'])[:60] == '"He commissioned Joshua: be strong and of good courage (31:2', ('CR_COMM', repr(_FV['CR_COMM'])[:100])
assert repr(_FV['CR_BRING'])[:60] == '"you shall bring the children of Israel into the land I swor', ('CR_BRING', repr(_FV['CR_BRING'])[:100])
assert repr(_FV['CR_SLEEP'])[:60] == '"you shall sleep with your fathers (31:16) — the death\'s sec', ('CR_SLEEP', repr(_FV['CR_SLEEP'])[:100])
assert repr(_FV['CR_AFTER'])[:60] == '"after my death you will corrupt and turn, evil will befall ', ('CR_AFTER', repr(_FV['CR_AFTER'])[:100])
assert repr(_FV['CR_DEATH'])[:60] == '"THE SEVENTH OF ADAR OF THE FORTIETH YEAR — the year the ink', ('CR_DEATH', repr(_FV['CR_DEATH'])[:100])
assert repr(_FV['CR_GIFTS'])[:60] == '"THREE GIFTS BY THREE MERITS — the well by Miriam\'s, the pil', ('CR_GIFTS', repr(_FV['CR_GIFTS'])[:100])
assert repr(_FV['BL_GRAVE'])[:60] == '{\'the_verse\': \'Deut 33:21\', \'the_teaching\': "Onkelos 33:21 —', ('BL_GRAVE', repr(_FV['BL_GRAVE'])[:100])
assert repr(_FV['BL_CHAIN'])[:60] == "'Moses received the Torah from Sinai and handed it to Joshua", ('BL_CHAIN', repr(_FV['BL_CHAIN'])[:100])
assert repr(_FV['BL_AHEAD'])[:60] == '{\'forward\': ["Deut 34:6 — Moses\' grave in Gad\'s portion (33:', ('BL_AHEAD', repr(_FV['BL_AHEAD'])[:100])
assert repr(_FV['BL_LAW'])[:60] == "'Moses commanded us a law, the inheritance of the congregati", ('BL_LAW', repr(_FV['BL_LAW'])[:100])
assert repr(_FV['BL_PORTION'])[:60] == '"he chose a first part, for there a portion of a ruler was r', ('BL_PORTION', repr(_FV['BL_PORTION'])[:100])
assert repr(_FV['GR_GRAVE'])[:60] == "'reubens_nebo_gads_field'", ('GR_GRAVE', repr(_FV['GR_GRAVE'])[:100])
assert repr(_FV['GR_CEASED'])[:60] == '(40, 5, 15)', ('GR_CEASED', repr(_FV['GR_CEASED'])[:100])
assert repr(_FV['GR_CITY'])[:60] == '"Nebo Reuben\'s (32:37-38) — Moses died in Reuben\'s portion (', ('GR_CITY', repr(_FV['GR_CITY'])[:100])
assert repr(_FV['CK_DATES'])[:60] == "'Aaron (40, 5, 1) by the ink, aged 123; Miriam the tenth of ", ('CK_DATES', repr(_FV['CK_DATES'])[:100])
assert repr(_FV['CK_SUCC'])[:60] == "'the garments to Eleazar and the office with them — Exod 29:", ('CK_SUCC', repr(_FV['CK_SUCC'])[:100])
assert repr(_FV['CK_THIRTY'])[:60] == '"thirty days\' weeping by all the house of Israel — a timer d', ('CK_THIRTY', repr(_FV['CK_THIRTY'])[:100])
assert repr(_FV['CK_AGE'])[:60] == "'Aaron 123 at his death (33:39 — [123])'", ('CK_AGE', repr(_FV['CK_AGE'])[:100])
assert repr(_FV['CK_WELL'])[:60] == '"the well gone at Miriam\'s death, returned by Moses\' and Aar', ('CK_WELL', repr(_FV['CK_WELL'])[:100])
assert repr(_FV['CK_KISS'])[:60] == '\'Miriam too by the kiss — "there" / "there" with Deut 34:5 (', ('CK_KISS', repr(_FV['CK_KISS'])[:100])
assert repr(_FV['CK_BURIAL'])[:60] == '"buried near the death — the woman\'s bier not set down in th', ('CK_BURIAL', repr(_FV['CK_BURIAL'])[:100])
assert repr(_FV['CK_SENT'])[:60] == '"barred from the land — Moses and Aaron; Aaron\'s closed at 2', ('CK_SENT', repr(_FV['CK_SENT'])[:100])
assert repr(_FV['CK_THERE'])[:60] == '\'benefit from a corpse forbidden — "there" / "there" with th', ('CK_THERE', repr(_FV['CK_THERE'])[:100])
assert repr(_FV['CK_WELLD'])[:60] == "'miriams_gone_at_her_death_returned'", ('CK_WELLD', repr(_FV['CK_WELLD'])[:100])
assert repr(_FV['CK_MOURNED'])[:60] == "'the_men_and_the_women'", ('CK_MOURNED', repr(_FV['CK_MOURNED'])[:100])
assert repr(_FV['CK_MANNA'])[:60] == "'light_absorbed_in_the_limbs'", ('CK_MANNA', repr(_FV['CK_MANNA'])[:100])
assert repr(_FV['JR_DATE'])[:60] == '"Aaron died on (40, 5, 1) (33:38) — the tape\'s marker at 20:', ('JR_DATE', repr(_FV['JR_DATE'])[:100])
assert repr(_FV['JR_MOUTH'])[:60] == '"by the mouth of the LORD at the death (33:38) — the kiss (B', ('JR_MOUTH', repr(_FV['JR_MOUTH'])[:100])
assert repr(_FV['JR_ADAR'])[:60] == '"Moses\' seventh of Adar — computed backward from the tenth o', ('JR_ADAR', repr(_FV['JR_ADAR'])[:100])
assert repr(_FV['JR_ANALOGY'])[:60] == '"the fortieth year / the fortieth year — Deuteronomy 1:3\'s b', ('JR_ANALOGY', repr(_FV['JR_ANALOGY'])[:100])
assert repr(_FV['JR_NOWRITE'])[:60] == '"no write for 33:38-40 — the death and the hearing are the t', ('JR_NOWRITE', repr(_FV['JR_NOWRITE'])[:100])
assert repr(_FV['JR_DDATE'])[:60] == '(40, 5, 1)', ('JR_DDATE', repr(_FV['JR_DDATE'])[:100])
assert repr(_FV['JR_AGE'])[:60] == '123', ('JR_AGE', repr(_FV['JR_AGE'])[:100])
assert repr(_FV['ST_WALK'])[:60] == '"walk after His attributes (Sotah 14a:3-4) — \'after the LORD', ('ST_WALK', repr(_FV['ST_WALK'])[:100])
assert repr(_FV['ST_BURIED'])[:60] == '"and he was buried there (10:6) — the Torah\'s one seat; Numb', ('ST_BURIED', repr(_FV['ST_BURIED'])[:100])
assert repr(_FV['ST_PLACE'])[:60] == '"the place of the death — Moserah in the retelling (10:6), M', ('ST_PLACE', repr(_FV['ST_PLACE'])[:100])
assert repr(_FV['ST_FRAG'])[:60] == '"the fragments in the ark (10:2, 10:5) — \'and you shall put ', ('ST_FRAG', repr(_FV['ST_FRAG'])[:100])
assert repr(_FV['ST_R105'])[:60] == '"the receipt 10:5 — \'as the LORD commanded me\' (4:5 the pair', ('ST_R105', repr(_FV['ST_R105'])[:100])
assert repr(_FV['ST_ATTR'])[:60] == '{\'the_row\': "Sotah 14a:3-4 — \'after the LORD your God you sh', ('ST_ATTR', repr(_FV['ST_ATTR'])[:100])
assert repr(_FV['ST_CHARGE'])[:60] == '{\'31_7\': "Moses to Joshua — \'for you shall go with this peop', ('ST_CHARGE', repr(_FV['ST_CHARGE'])[:100])
assert repr(_FV['ZE_RUN'])[:60] == '"given in the sixth book by the mouth of the LORD — the hold', ('ZE_RUN', repr(_FV['ZE_RUN'])[:100])
assert repr(_FV['ZE_EXEC'])[:60] == "'married the sons of their uncles; the inheritance remained ", ('ZE_EXEC', repr(_FV['ZE_EXEC'])[:100])
assert repr(_FV['ZE_REACH'])[:60] == "'this_generation'", ('ZE_REACH', repr(_FV['ZE_REACH'])[:100])
assert repr(_FV['OS_MTN'])[:60] == '"the mountain of Abarim (27:12) — Nebo and Pisgah its other ', ('OS_MTN', repr(_FV['OS_MTN'])[:100])
assert repr(_FV['OS_HAND'])[:60] == '"the hand laid (27:18, 23) — one hand commanded, two laid (t', ('OS_HAND', repr(_FV['OS_HAND'])[:100])
assert repr(_FV['OS_RECEIPT'])[:60] == '"the receipt (27:22-23) — \'as the LORD commanded him\': the c', ('OS_RECEIPT', repr(_FV['OS_RECEIPT'])[:100])
assert repr(_FV['OS_DEBIT'])[:60] == "'the debit (27:12) — see the land from Abarim: commanded on ", ('OS_DEBIT', repr(_FV['OS_DEBIT'])[:100])
assert repr(_FV['OS_PISGAH'])[:60] == '"Pisgah (3:27) — 27:12\'s command read back with Pisgah for A', ('OS_PISGAH', repr(_FV['OS_PISGAH'])[:100])
assert repr(_FV['OS_PEOR'])[:60] == '"Beth-peor (3:29) — the last camp by CALL (22:1; 36:13; Deut', ('OS_PEOR', repr(_FV['OS_PEOR'])[:100])
assert repr(_FV['OS_CMDJ'])[:60] == '"command Joshua (3:28) — the commission read back (Kiddushin', ('OS_CMDJ', repr(_FV['OS_CMDJ'])[:100])
assert repr(_FV['OS_REFUSAL'])[:60] == '"the refusal (3:26) — \'let it suffice you\' the singular\'s on', ('OS_REFUSAL', repr(_FV['OS_REFUSAL'])[:100])
assert repr(_FV['OS_COMM'])[:60] == "{'mountain_names': ['Abarim (27:12; 33:47-48; Deut 32:49)', ", ('OS_COMM', repr(_FV['OS_COMM'])[:100])
assert repr(_FV['BH_GIFTS'])[:60] == "'the well, the cloud, the manna — three gifts by three sheph", ('BH_GIFTS', repr(_FV['BH_GIFTS'])[:100])
assert repr(_FV['BH_FELL'])[:60] == "'by rank — the righteous at their doors, the average outside", ('BH_FELL', repr(_FV['BH_FELL'])[:100])
assert repr(_FV['BH_DIBBUR'])[:60] == "'harsh speech (dibbur)'", ('BH_DIBBUR', repr(_FV['BH_DIBBUR'])[:100])
assert repr(_FV['BH_DEAD'])[:60] == "'the leper among the four as dead'", ('BH_DEAD', repr(_FV['BH_DEAD'])[:100])
assert repr(_FV['BH_MEASURE'])[:60] == '"an hour at the Nile, seven days\' halt — measure for measure', ('BH_MEASURE', repr(_FV['BH_MEASURE'])[:100])
assert repr(_FV['BH_SPIRIT'])[:60] == '"set apart — Moses\' spirit undiminished"', ('BH_SPIRIT', repr(_FV['BH_SPIRIT'])[:100])
assert repr(_FV['BH_CLOUDS'])[:60] == '7', ('BH_CLOUDS', repr(_FV['BH_CLOUDS'])[:100])
assert repr(_FV['NS_TERM'])[:60] == "'30 days'", ('NS_TERM', repr(_FV['NS_TERM'])[:100])
assert repr(_FV['NS_DAYS'])[:60] == '30', ('NS_DAYS', repr(_FV['NS_DAYS'])[:100])
assert repr(_FV['CP_MIDST'])[:60] == '"from your midst, of your brothers (18:15, 18:18) — not from', ('CP_MIDST', repr(_FV['CP_MIDST'])[:100])
assert repr(_FV['CP_WORDS'])[:60] == '"My words in his mouth (18:18) — not face to face, no interp', ('CP_WORDS', repr(_FV['CP_WORDS'])[:100])
assert repr(_FV['CP_TEST'])[:60] == '"the test by the event (18:21-22) — Jeremiah against Hanania', ('CP_TEST', repr(_FV['CP_TEST'])[:100])
assert repr(_FV['CP_ORDER'])[:60] == '{\'not_face_to_face\': "My words in his mouth — the Holy Spiri', ('CP_ORDER', repr(_FV['CP_ORDER'])[:100])
assert repr(_FV['CP_SUCC'])[:60] == "'the son stands in his place — for the king and for every pr", ('CP_SUCC', repr(_FV['CP_SUCC'])[:100])
assert repr(_FV['ER_FACE'])[:60] == '(6, 5)', ('ER_FACE', repr(_FV['ER_FACE'])[:100])
assert repr(_FV['ER_AVOT'])[:60] == "'moses_joshua_elders_prophets_great_assembly'", ('ER_AVOT', repr(_FV['ER_AVOT'])[:100])
assert repr(_FV['ER_BREAK'])[:60] == "'yishar_kochakha'", ('ER_BREAK', repr(_FV['ER_BREAK'])[:100])
assert repr(_FV['ER_RADIANCE'])[:60] == '(3, 3)', ('ER_RADIANCE', repr(_FV['ER_RADIANCE'])[:100])
assert repr(_FV['ER_FRAG'])[:60] == "'both_in_the_ark'", ('ER_FRAG', repr(_FV['ER_FRAG'])[:100])
assert repr(_FV['ER_3DEATHS'])[:60] == "{'sword': 'witnesses_and_warning', 'plague': 'witnesses_no_w", ('ER_3DEATHS', repr(_FV['ER_3DEATHS'])[:100])
assert repr(_FV['ER_PLAGUE'])[:60] == '(5, 31)', ('ER_PLAGUE', repr(_FV['ER_PLAGUE'])[:100])
assert repr(_FV['ES_SIGNS'])[:60] == '3', ('ES_SIGNS', repr(_FV['ES_SIGNS'])[:100])
assert repr(_FV['ES_BELIEVED'])[:60] == '[(4, 31), (14, 31)]', ('ES_BELIEVED', repr(_FV['ES_BELIEVED'])[:100])
assert repr(_FV['ES_TEN'])[:60] == '10', ('ES_TEN', repr(_FV['ES_TEN'])[:100])
assert repr(_FV['ES_SEA'])[:60] == '10', ('ES_SEA', repr(_FV['ES_SEA'])[:100])
assert repr(_FV['ES_BONES'])[:60] == "'moses_merited_the_bones_of_joseph'", ('ES_BONES', repr(_FV['ES_BONES'])[:100])
assert repr(_FV['ES_BIRTH'])[:60] == '(12, 7)', ('ES_BIRTH', repr(_FV['ES_BIRTH'])[:100])
assert repr(_FV['JO_OATH'])[:60] == "'Gen 47:31'", ('JO_OATH', repr(_FV['JO_OATH'])[:100])
assert repr(_FV['JO_CMD'])[:60] == "'law_joseph_47_29'", ('JO_CMD', repr(_FV['JO_CMD'])[:100])
assert repr(_FV['JO_CLOSED'])[:60] == "'Gen 50:13'", ('JO_CLOSED', repr(_FV['JO_CLOSED'])[:100])
assert repr(_FV['JO_BONES'])[:60] == "'Exod 13:19'", ('JO_BONES', repr(_FV['JO_BONES'])[:100])
assert repr(_FV['JO_WITHYOU'])[:60] == "'when_you_go_up'", ('JO_WITHYOU', repr(_FV['JO_WITHYOU'])[:100])
assert repr(_FV['JO_BOTH'])[:60] == "('esau', 'jacob')", ('JO_BOTH', repr(_FV['JO_BOTH'])[:100])
assert repr(_FV['JO_GATHERED'])[:60] == "'law_joseph_35_29'", ('JO_GATHERED', repr(_FV['JO_GATHERED'])[:100])
assert repr(_FV['FA_GATHERED'])[:60] == "['Gen 25:8', 'Gen 25:17', 'Gen 35:29', 'Gen 49:33', 'Gen 49:", ('FA_GATHERED', repr(_FV['FA_GATHERED'])[:100])
assert repr(_FV['FA_BURIED'])[:60] == '(8, False)', ('FA_BURIED', repr(_FV['FA_BURIED'])[:100])
assert repr(_FV['FA_CMD'])[:60] == 'True', ('FA_CMD', repr(_FV['FA_CMD'])[:100])
assert repr(_FV['FA_POSS'])[:60] == "'burial_is_the_first_act'", ('FA_POSS', repr(_FV['FA_POSS'])[:100])
assert repr(_FV['MA_THREE'])[:60] == '3', ('MA_THREE', repr(_FV['MA_THREE'])[:100])
assert repr(_FV['MA_SEED'])[:60] == "'Gen 25:16'", ('MA_SEED', repr(_FV['MA_SEED'])[:100])
assert repr(_FV['MA_PROMISE'])[:60] == "'buried_in_peace'", ('MA_PROMISE', repr(_FV['MA_PROMISE'])[:100])
assert repr(_FV['HI_RECEIPT'])[:60] == '"the receipt (6:25) — \'as he commanded us\' without the Name:', ('HI_RECEIPT', repr(_FV['HI_RECEIPT'])[:100])
assert repr(_FV['HI_OATH'])[:60] == '{\'deut_6_13\': "\'by his name you shall swear\' — a POSITIVE cl', ('HI_OATH', repr(_FV['HI_OATH'])[:100])
assert repr(_FV['HI_NONAME'])[:60] == '{\'deut_6_25\': "\'as he commanded us\' — k/834 + 6680 with the ', ('HI_NONAME', repr(_FV['HI_NONAME'])[:100])
assert repr(_FV['OH_PEOR'])[:60] == '"Baal-peor seen (4:3) — Numbers 25:3-9 READ BACK, SHORTENED:', ('OH_PEOR', repr(_FV['OH_PEOR'])[:100])
assert repr(_FV['OH_CHAIN'])[:60] == "{'this_chapter': 'Deut 4:26', 'the_chain': ['Deut 4:26', 'De", ('OH_CHAIN', repr(_FV['OH_CHAIN'])[:100])
assert repr(_FV['OH_FRAME'])[:60] == "{'deut_4_44_45': 'the_second_speech_s_head', 'write': None}", ('OH_FRAME', repr(_FV['OH_FRAME'])[:100])
assert repr(_FV['SH_NAME'])[:60] == "'Hoshea to Joshua at 13:16 — the new name at 8 seats before ", ('SH_NAME', repr(_FV['SH_NAME'])[:100])
assert repr(_FV['SH_EQUAL'])[:60] == "'equal — Caleb first at 13:6, Joshua at 13:8 (Tosefta Kerito", ('SH_EQUAL', repr(_FV['SH_EQUAL'])[:100])
assert repr(_FV['SH_CEASED'])[:60] == '(40, 5, 15)', ('SH_CEASED', repr(_FV['SH_CEASED'])[:100])

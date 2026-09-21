#!/usr/bin/env python3
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
def W12(v): return words('Deut', 12, v)
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
assert {v: len(W12(v)) for v in range(1, 32)} == {1: 21, 2: 24, 3: 18, 4: 5, 5: 18, 6: 14, 7: 15, 8: 12, 9: 14, 10: 17, 11: 29, 12: 18, 13: 9, 14: 17, 15: 20, 16: 8, 17: 18, 18: 27, 19: 10, 20: 22, 21: 25, 22: 13, 23: 14, 24: 6, 25: 12, 26: 13, 27: 17, 28: 23, 29: 17, 30: 22, 31: 22}
# THE ENGINE'S PARSER on every verse — MEASURED before the compile is asked: ONE NUMBER VERSE (12:14 "in one of your tribes" [1]) and ONE STARRED TOKEN (12:17 "tithe" — the ten-word's homograph, starred at every tithe seat of the book: 12:17, 14:23, 14:28, 26:12); the kin's numbers — the third year's [3] (14:28), Exodus 34:24's three times [3]
PARSE = {v: (ink_numbers(verse_words('Deut', 12, v)), ink_ordinals(verse_words('Deut', 12, v)), [t for t in verse_words('Deut', 12, v) if t[-1] in '#~^%@|*']) for v in range(1, 32)}
assert {v: p for v, p in PARSE.items() if any(p)} == {14: ([1], [], []), 17: ([], [], ['מעשר*'])}, {v: p for v, p in PARSE.items() if any(p)}
assert sorted({(c, v) for (b, c, v) in by if b == 'Deut' for t in verse_words(b, c, v) if t.startswith('מעשר') and t.endswith('*')}) == [(12, 17), (14, 23), (14, 28), (26, 12)] and [(v, x) for v in range(1, 32) for x in W12(v) if x in ('אחד', 'באחד', 'אחת')] == [(14, 'באחד')]
KINNUM = {k: ink_numbers(verse_words(*k)) for k in [('Num', 18, 26), ('Deut', 14, 22), ('Deut', 14, 28), ('Lev', 27, 30), ('Lev', 27, 32), ('Deut', 15, 22), ('Lev', 17, 3), ('Lev', 17, 11), ('Gen', 9, 4), ('Exod', 20, 21), ('Deut', 7, 5), ('Num', 33, 52), ('Deut', 14, 23), ('Deut', 16, 2), ('Deut', 26, 12), ('Judg', 17, 6), ('Deut', 19, 8), ('Exod', 34, 24), ('Num', 18, 21), ('Deut', 12, 14)]}
assert KINNUM == {('Num', 18, 26): [], ('Deut', 14, 22): [], ('Deut', 14, 28): [3], ('Lev', 27, 30): [], ('Lev', 27, 32): [], ('Deut', 15, 22): [], ('Lev', 17, 3): [], ('Lev', 17, 11): [], ('Gen', 9, 4): [], ('Exod', 20, 21): [], ('Deut', 7, 5): [], ('Num', 33, 52): [], ('Deut', 14, 23): [], ('Deut', 16, 2): [], ('Deut', 26, 12): [], ('Judg', 17, 6): [], ('Deut', 19, 8): [], ('Exod', 34, 24): [3], ('Num', 18, 21): [], ('Deut', 12, 14): [1]}, KINNUM
# THE REGISTER, computed on the morphology: THE CHAPTER SWITCHES NUMBER AT ITS MIDDLE — the second person PLURAL ONLY in eight verses (2-4, 6, 8, 10-12), BOTH in five (1, 5, 7, 9, 16 — the singular inside the plural verse; 12:16's "you (pl.) shall not eat" the one plural in the singular half), SINGULAR ONLY in eighteen (13-15, 17-31), NEITHER in none; THE FIRST PERSON: Moses' "I" three (11, 14, 28) and "I have commanded you" (21), the eater's "let me eat" (20), the seeker's "and I will do so, I too" (30); "we" once (8); the imperatives FIVE (13, 19, 30 "take heed" — the niphal; 23 "be steadfast"; 28 "observe"); the infinitive absolute ONE (2 "destroy, you shall destroy"); THE CONSECUTIVE PERFECTS TWENTY-THREE in fifteen verses — the law's form; NO wayyiqtol — no narrative verb in the chapter; the prohibitions EIGHT (4, 8, 16, 17, 23, 24, 25, 31; 12:9's "not" a perfect); "saying" once (30 — the seeker's speech), no divine frame
NUM = {v: (sum(1 for _, m in wm('Deut', 12, v) if m and '2mp' in m), sum(1 for _, m in wm('Deut', 12, v) if m and '2ms' in m)) for v in range(1, 32)}
assert NUM == {1: (2, 2), 2: (2, 0), 3: (5, 0), 4: (2, 0), 5: (3, 1), 6: (9, 0), 7: (6, 2), 8: (1, 0), 9: (1, 1), 10: (7, 0), 11: (9, 0), 12: (9, 0), 13: (0, 5), 14: (0, 5), 15: (0, 6), 16: (1, 1), 17: (0, 11), 18: (0, 12), 19: (0, 5), 20: (0, 6), 21: (0, 10), 22: (0, 1), 23: (0, 2), 24: (0, 2), 25: (0, 5), 26: (0, 5), 27: (0, 6), 28: (0, 8), 29: (0, 5), 30: (0, 5), 31: (0, 2)}
assert [v for v, (p, s) in NUM.items() if s and not p] == [13, 14, 15, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31] and [v for v, (p, s) in NUM.items() if p and s] == [1, 5, 7, 9, 16] and [v for v, (p, s) in NUM.items() if not p and not s] == [] and [v for v, (p, s) in NUM.items() if p and not s] == [2, 3, 4, 6, 8, 10, 11, 12]
assert [(x, m) for x, m in wm('Deut', 12, 16) if m and '2mp' in m] == [('תאכלו', 'HVqi2mp')] and [(x, m) for x, m in wm('Deut', 12, 1) if m and '2ms' in m] == [('אבתיך', 'HNcmpc/Sp2ms'), ('לך', 'HR/Sp2ms')] and [(x, m) for x, m in wm('Deut', 12, 5) if m and '2ms' in m] == [('ובאת', 'HC/Vqq2ms')] and [(x, m) for x, m in wm('Deut', 12, 9) if m and '2ms' in m] == [('אלהיך', 'HNcmpc/Sp2ms')]
assert {v: [(x, m) for x, m in wm('Deut', 12, v) if m and '1cs' in m] for v in range(1, 32) if any(m and '1cs' in m for _, m in wm('Deut', 12, v))} == {11: [('אנכי', 'HPp1cs')], 14: [('אנכי', 'HPp1cs')], 20: [('אכלה', 'HVqh1cs')], 21: [('צויתך', 'HVpp1cs/Sp2ms')], 28: [('אנכי', 'HPp1cs')], 30: [('ואעשה', 'HC/Vqi1cs'), ('אני', 'HPp1cs')]} and {v: [(x, m) for x, m in wm('Deut', 12, v) if m and '1cp' in m] for v in range(1, 32) if any(m and '1cp' in m for _, m in wm('Deut', 12, v))} == {8: [('אנחנו', 'HPp1cp')]}
assert {v: [(x, m) for x, m in wm('Deut', 12, v) if m and re.match(r'^HV.?.?v', m)] for v in range(1, 32) if any(m and re.match(r'^HV.?.?v', m) for _, m in wm('Deut', 12, v))} == {13: [('השמר', 'HVNv2ms')], 19: [('השמר', 'HVNv2ms')], 23: [('חזק', 'HVqv2ms')], 28: [('שמר', 'HVqv2ms')], 30: [('השמר', 'HVNv2ms')]}
assert {v: [(x, m) for x, m in wm('Deut', 12, v) if m and re.match(r'^H(?:C/)?V.a$', m)] for v in range(1, 32) if any(m and re.match(r'^H(?:C/)?V.a$', m) for _, m in wm('Deut', 12, v))} == {2: [('אבד', 'HVpa')]}
WEQ = {v: [x for x, m in wm('Deut', 12, v) if m and re.search(r'^HC/V.q', m)] for v in range(1, 32) if any(m and re.search(r'^HC/V.q', m) for _, m in wm('Deut', 12, v))}
assert WEQ == {3: ['ונתצתם', 'ושברתם', 'ואבדתם'], 5: ['ובאת'], 6: ['והבאתם'], 7: ['ואכלתם', 'ושמחתם'], 10: ['ועברתם', 'וישבתם', 'והניח', 'וישבתם'], 11: ['והיה'], 12: ['ושמחתם'], 15: ['ואכלת'], 18: ['ושמחת'], 20: ['ואמרת'], 21: ['וזבחת', 'ואכלת'], 26: ['ובאת'], 27: ['ועשית'], 28: ['ושמעת'], 29: ['וירשת', 'וישבת']} and sum(len(x) for x in WEQ.values()) == 23 and len(WEQ) == 15
assert {v: [x for x, m in wm('Deut', 12, v) if m and re.search(r'^HC/V.w', m)] for v in range(1, 32) if any(m and re.search(r'^HC/V.w', m) for _, m in wm('Deut', 12, v))} == {}
PTC = {v: [(x, m) for x, m in wm('Deut', 12, v) if m and re.search(r'^H(?:C/|R/|Td/|C/R/)?V.r', m)] for v in range(1, 32) if any(m and re.search(r'^H(?:C/|R/|Td/|C/R/)?V.r', m) for _, m in wm('Deut', 12, v))}
assert sum(len(x) for x in PTC.values()) == 10 and len(PTC) == 8 and PTC[2] == [('ירשים', 'HVqrmpa'), ('הרמים', 'HTd/Vqrmpa')] and PTC[10] == [('מנחיל', 'HVhrmsa'), ('איביכם', 'HVqrmpc/Sp2mp')] and PTC[9] == [('נתן', 'HVqrmsa')] and PTC[29] == [('בא', 'HVqrmsa')]
I2 = {v: [(x, m) for x, m in wm('Deut', 12, v) if m and re.search(r'^H(?:Ti/)?V.i2', m)] for v in range(1, 32) if any(m and re.search(r'^H(?:Ti/)?V.i2', m) for _, m in wm('Deut', 12, v))}
assert sum(len(x) for x in I2.values()) == 33 and len(I2) == 24 and I2[3] == [('תשרפון', 'HVqi2mp/Sn'), ('תגדעון', 'HVpi2mp/Sn')] and I2[17] == [('תוכל', 'HVqi2ms'), ('תדר', 'HVqi2ms')] and I2[30] == [('תנקש', 'HVNi2ms'), ('תדרש', 'HVqi2ms')]
assert [x for v in range(1, 32) for x, m in wm('Deut', 12, v) if m and m.endswith('/Sn')] == ['תשמרון', 'תאבדון', 'תשרפון', 'תגדעון', 'תעשון', 'תעשון']   # THE PARAGOGIC NUN six times, all in the plural half (1-8)
PROH = {v: [(x, m) for i, (x, m) in enumerate(wm('Deut', 12, v)) if i and wm('Deut', 12, v)[i - 1][0] in NEG and m and re.search(r'^HV.i2', m)] for v in range(1, 32)}
assert {v: x for v, x in PROH.items() if x} == {4: [('תעשון', 'HVqi2mp/Sn')], 8: [('תעשון', 'HVqi2mp/Sn')], 16: [('תאכלו', 'HVqi2mp')], 17: [('תוכל', 'HVqi2ms')], 23: [('תאכל', 'HVqi2ms')], 24: [('תאכלנו', 'HVqi2ms/Sp3ms')], 25: [('תאכלנו', 'HVqi2ms/Sp3ms')], 31: [('תעשה', 'HVqi2ms')]} and {v: [x for x in W12(v) if x in NEG] for v in range(1, 32) if any(x in NEG for x in W12(v))} == {4: ['לא'], 8: ['לא'], 9: ['לא'], 16: ['לא'], 17: ['לא'], 23: ['ולא'], 24: ['לא'], 25: ['לא'], 31: ['לא']}
assert {f'12:{v}': [x for x in W12(v) if x in ('כי', 'אם', 'ואם', 'או', 'פן', 'ופן')] for v in range(1, 32) if any(x in ('כי', 'אם', 'ואם', 'או', 'פן', 'ופן') for x in W12(v))} == {'12:5': ['כי', 'אם'], '12:9': ['כי'], '12:12': ['כי'], '12:13': ['פן'], '12:14': ['כי', 'אם'], '12:18': ['כי', 'אם'], '12:19': ['פן'], '12:20': ['כי', 'כי'], '12:21': ['כי'], '12:23': ['כי'], '12:25': ['כי'], '12:28': ['כי'], '12:29': ['כי'], '12:30': ['פן', 'ופן'], '12:31': ['כי', 'כי']}
assert [v for v in range(1, 32) if 'לאמר' in W12(v)] == [30] and [v for v in range(1, 32) if any(W12(v)[i] in ('ויאמר', 'וידבר') and W12(v)[i + 1] == 'יהוה' for i in range(len(W12(v)) - 1))] == []
assert {v: [x for x in W12(v) if x in ('למען', 'ולמען')] for v in range(1, 32) if any(x in ('למען', 'ולמען') for x in W12(v))} == {25: ['למען'], 28: ['למען']} and len(U('למען', 'ולמען', books=('Deut',))) == 43
assert sum(1 for v in range(1, 32) for x in W12(v) if x == 'יהוה') == 23 and [v for v in range(1, 32) if any(W12(v)[i:i + 2] == ['יהוה', 'אלהיך'] for i in range(len(W12(v)) - 1))] == [7, 9, 15, 18, 20, 21, 27, 28, 29] and [v for v in range(1, 32) if any(W12(v)[i:i + 2] == ['יהוה', 'אלהיכם'] for i in range(len(W12(v)) - 1))] == [5, 7, 10, 11, 12] and [v for v in range(1, 32) if 'ליהוה' in W12(v)] == [4, 11, 31]
assert [v for v in range(1, 32) for x in W12(v) if x in ('ישראל', 'מצרים', 'מצרימה', 'משה')] == [] and [v for v in range(1, 32) for x in W12(v) if x == 'היום'] == [8] and [v for v in range(1, 32) for x in W12(v) if x == 'הירדן'] == [10]
assert Counter(int(s.split()[1].split(':')[0]) for s in U('משה', 'למשה', 'ומשה', books=('Deut',))) == Counter({31: 10, 34: 6, 4: 4, 1: 3, 27: 3, 32: 3, 33: 2, 15: 1, 28: 1, 29: 1, 5: 1})   # MOSES UNNAMED FROM CHAPTER 6 TO 14 (chapter 10's find, held)
assert {v: [x for x in W12(v) if x in ('שם', 'שמה', 'ושם')] for v in range(1, 32) if any(x in ('שם', 'שמה', 'ושם') for x in W12(v))} == {2: ['שם'], 5: ['שם', 'שמה'], 6: ['שמה'], 7: ['שם'], 11: ['שם', 'שמה'], 14: ['שם', 'ושם'], 21: ['שם'], 29: ['שמה']}   # "there" eleven times — the chapter's word for the place
assert {v: [x for x in W12(v) if x in ('אלהיהם', 'לאלהיהם')] for v in range(1, 32) if any(x in ('אלהיהם', 'לאלהיהם') for x in W12(v))} == {2: ['אלהיהם'], 3: ['אלהיהם'], 30: ['לאלהיהם', 'אלהיהם'], 31: ['לאלהיהם', 'לאלהיהם']}
OWN = {lab: [s for s, _, _ in LEMT(lem, books=('Deut',)) if s.startswith('Deut 12:')] for lab, lem in (('place', '4725'), ('gate', '8179'), ('eat', '398'), ('flesh', '1320'), ('blood', '1818'), ('soul', '5315'), ('burnt', '5930 a'), ('sacrifice-n', '2077'), ('sacrifice-v', '2076'), ('tithe', '4643'), ('vow-n', '5088'), ('vow-v', '5087'), ('freewill', '5071'), ('heave', '8641'), ('firstling', '1062'), ('rejoice', '8055'), ('nations', '1471 a'), ('choose', '977'), ('seek', '1875'), ('levite', '3881'))}
assert {k: len(v) for k, v in OWN.items()} == {'place': 9, 'gate': 5, 'eat': 18, 'flesh': 7, 'blood': 5, 'soul': 6, 'burnt': 5, 'sacrifice-n': 3, 'sacrifice-v': 2, 'tithe': 3, 'vow-n': 4, 'vow-v': 2, 'freewill': 2, 'heave': 3, 'firstling': 2, 'rejoice': 3, 'nations': 3, 'choose': 6, 'seek': 2, 'levite': 3}, {k: len(v) for k, v in OWN.items()}
assert OWN['eat'][:3] == ['Deut 12:7', 'Deut 12:15', 'Deut 12:15'] and OWN['blood'] == ['Deut 12:16', 'Deut 12:23', 'Deut 12:23', 'Deut 12:27', 'Deut 12:27'] and OWN['choose'] == ['Deut 12:5', 'Deut 12:11', 'Deut 12:14', 'Deut 12:18', 'Deut 12:21', 'Deut 12:26'] and OWN['seek'] == ['Deut 12:5', 'Deut 12:30'] and len(LEMT('977', books=('Deut',))) == 31 and len(LEMT('3881', books=('Deut',))) == 19 and len(LEMT('7535', books=('Deut',))) == 20 and len(LEMT('8441', books=('Deut',))) == 17
# ---- THE PHRASES, censused over the whole DB (the measure's B print) ----
DT = ('Deut',)
assert P('אלה', 'החקים', 'והמשפטים') == ['Deut 12:1', 'Lev 26:46'] and P('החקים', 'והמשפטים') == ['Deut 12:1', 'Deut 6:1', 'Lev 26:46']   # THE HEADER'S TWIN IS THE FOLD'S FOOTER — "these are the statutes and the judgments" stands at 12:1 and at Leviticus 26:46 alone
assert U('תשמרון') == ['2Kgs 17:37', 'Deut 11:22', 'Deut 12:1', 'Deut 6:17', 'Deut 8:1'] and P('יהוה', 'אלהי', 'אבתיך') == ['Deut 12:1', 'Deut 1:21', 'Deut 27:3', 'Deut 6:3'] and P('כל', 'הימים', 'אשר', 'אתם', 'חיים', 'על', 'האדמה') == ['Deut 12:1', 'Deut 31:13'] and len(P('על', 'האדמה', books=DT)) == 13
assert P('אבד', 'תאבדון') == ['Deut 12:2', 'Deut 30:18', 'Deut 4:26', 'Deut 8:19'] and [(s, x, m) for s, x, m in LEMT('6', books=DT) if s.startswith('Deut 12:')] == [('Deut 12:2', 'אבד', 'HVpa'), ('Deut 12:2', 'תאבדון', 'HVpi2mp/Sn'), ('Deut 12:3', 'ואבדתם', 'HC/Vpq2mp')]   # THE VERB OF ISRAEL'S PERISHING TURNED ON THE SHRINES — the doubled "perish, you shall perish" of 4:26, 8:19, 30:18 said here as "destroy, you shall destroy" (the piel)
assert P('כל', 'המקמות') == ['Deut 12:2', 'Jer 45:5'] and P('אשר', 'עבדו', 'שם', 'הגוים') == ['Deut 12:2'] and P('על', 'ההרים', 'הרמים') == ['Deut 12:2'] and P('תחת', 'כל', 'עץ', 'רענן') == ['Isa 57:5', 'Jer 3:13', 'Jer 3:6'] and len(P('כל', 'עץ', 'רענן')) == 10 and len(U('רענן')) == 17 and P('כל', 'עץ', 'רענן')[:5] == ['1Kgs 14:23', '2Chr 28:4', '2Kgs 16:4', '2Kgs 17:10', 'Deut 12:2']   # THE KINGS' FORMULA — "under every leafy tree" the prophets' and the Kings' phrase for the high places, its Torah seat this one
assert [(s, x) for s, x, _ in LEMT('5422', books=T)] == [('Deut 7:5', 'תתצו'), ('Deut 12:3', 'ונתצתם'), ('Exod 34:13', 'תתצון'), ('Lev 11:35', 'יתץ'), ('Lev 14:45', 'ונתץ')] and U('תשרפון') == ['Deut 12:3', 'Deut 7:25', 'Deut 7:5'] and len(LEMT('1438')) == 22 and [(s, x) for s, x, _ in LEMT('1438', books=T)] == [('Deut 7:5', 'תגדעון'), ('Deut 12:3', 'תגדעון')] and P('ואבדתם', 'את', 'שמם') == ['Deut 12:3'] and P('מן', 'המקום', 'ההוא') == ['Deut 12:3', 'Deut 17:10'] and len(P('המקום', 'ההוא')) == 13
assert SH(D12(3), ('Exod', 34, 13)) == 3 and SH(D12(3), ('Deut', 7, 5)) == 2 and SH(D12(2), ('Deut', 7, 5)) == 0 and SH(D12(2), ('Num', 33, 52)) == 4 and SH(D12(2), ('2Kgs', 17, 10)) == 5   # THE DEMOLITION SAID IN NEW WORDS — 12:3 shares two tokens in order with 7:5 (the burning), three with Exodus 34:13; 12:2 none with 7:5
assert P('לא', 'תעשון', 'כן', 'ליהוה', 'אלהיכם') == ['Deut 12:4'] and P('לא', 'תעשה', 'כן') == ['Deut 12:31'] and SH(D12(4), ('Deut', 12, 31)) == 3   # THE PAIR'S TWO SEATS — plural at the shrines (12:4), singular at the abomination (12:31)
assert P('המקום', 'אשר', 'יבחר', 'יהוה') == ['Deut 12:11', 'Deut 12:21', 'Deut 12:26', 'Deut 12:5', 'Deut 14:24', 'Deut 14:25', 'Deut 16:6', 'Deut 17:8', 'Deut 18:6', 'Deut 26:2'] and P('במקום', 'אשר', 'יבחר', 'יהוה') == ['Deut 12:14', 'Deut 12:18', 'Deut 15:20', 'Deut 16:11', 'Deut 16:15', 'Deut 16:2', 'Deut 16:7'] and len(U('יבחר', books=DT)) == 23   # THE PLACE WHICH THE LORD WILL CHOOSE — six of the chapter's verses, twenty-three seats of "will choose" in the book, none before chapter 12
assert P('מכל', 'שבטיכם') == ['Deut 12:5'] and P('באחד', 'שבטיך') == ['Deut 12:14'] and P('לשום', 'את', 'שמו', 'שם') == ['1Kgs 14:21', '2Chr 12:13', 'Deut 12:5'] and P('לשום', 'שמו', 'שם') == ['Deut 12:21', 'Deut 14:24'] and P('לשכן', 'שמו', 'שם') == ['Deut 12:11', 'Deut 14:23', 'Deut 16:11', 'Deut 16:2', 'Deut 16:6', 'Deut 26:2'] and U('לשכנו') == ['Deut 12:5']   # "to put His name there" the chapter's form (12:5, 21), "to make His name dwell" its other (12:11) — Kings quotes the first; "His dwelling" ONE seat in the Bible
assert U('תדרשו') == ['Amos 5:5', 'Deut 12:5', 'Ezra 9:12'] and [(s, x, m) for s, x, m in LEMT('1875', books=DT) if s.startswith('Deut 12:')] == [('Deut 12:5', 'תדרשו', 'HVqi2mp'), ('Deut 12:30', 'תדרש', 'HVqi2ms')] and P('ובאת', 'שמה') == ['2Kgs 9:2', 'Deut 12:5']   # ONE VERB FOR TWO SEEKINGS — "seek" His dwelling (12:5) and "inquire" after their gods (12:30)
assert P('עלתיכם', 'וזבחיכם') == ['Deut 12:6'] and U('מעשרתיכם') == ['Amos 4:4', 'Deut 12:11', 'Deut 12:6', 'Num 18:28'] and P('תרומת', 'ידכם') == ['Deut 12:6'] and P('ותרומת', 'ידך') == ['Deut 12:17'] and P('ונדריכם', 'ונדבתיכם') == ['Deut 12:6'] and P('ובכרת', 'בקרכם', 'וצאנכם') == ['Deut 12:6'] and P('ובכרת', 'בקרך', 'וצאנך') == ['Deut 12:17', 'Deut 14:23'] and P('מבחר', 'נדריכם') == ['Deut 12:11'] and P('מעשר', 'דגנך', 'ותירשך', 'ויצהרך') == ['Deut 12:17'] and P('דגנך', 'ותירשך', 'ויצהרך') == ['Deut 11:14', 'Deut 12:17', 'Deut 7:13']
assert P('ואכלתם', 'שם', 'לפני', 'יהוה', 'אלהיכם') == ['Deut 12:7'] and U('ושמחתם', 'ושמחת', books=DT) == ['Deut 12:12', 'Deut 12:18', 'Deut 12:7', 'Deut 14:26', 'Deut 16:11', 'Deut 16:14', 'Deut 26:11', 'Deut 27:7'] and len(LEMT('8055', books=DT)) == 10 and P('משלח', 'ידכם') == ['Deut 12:7'] and P('משלח', 'ידך') == ['Deut 12:18', 'Deut 15:10', 'Deut 23:21', 'Deut 28:20', 'Deut 28:8'] and P('אתם', 'ובתיכם') == ['Deut 12:7'] and P('אשר', 'ברכך', 'יהוה', 'אלהיך') == ['Deut 12:7', 'Deut 15:14']
assert P('איש', 'כל', 'הישר', 'בעיניו') == ['Deut 12:8'] and P('הישר', 'בעיניו', 'יעשה') == ['Judg 17:6', 'Judg 21:25'] and P('פה', 'היום') == ['Deut 12:8', 'Deut 5:3'] and U('אנחנו', books=DT) == ['Deut 12:8', 'Deut 1:28', 'Deut 1:41', 'Deut 5:25', 'Deut 5:3'] and SH(D12(8), ('Judg', 17, 6)) == 3   # "EVERY MAN WHAT IS RIGHT IN HIS EYES" — the chapter's phrase is Judges' refrain (17:6, 21:25 "in those days there was no king"); "we" the book's five
assert P('המנוחה', 'ואל', 'הנחלה') == ['Deut 12:9'] and [(s, x) for s, x, _ in LEMT('4496', books=T)] == [('Deut 12:9', 'המנוחה'), ('Gen 49:15', 'מנחה'), ('Num 10:33', 'מנוחה')] and len(LEMT('4496')) == 22 and P('עד', 'עתה', books=DT) == ['Deut 12:9']   # "the rest" — Numbers 10:33's ark seeking a resting place (2:2's row), Issachar's (Genesis 49:15)
assert P('והניח', 'לכם', 'מכל', 'איביכם', 'מסביב') == ['Deut 12:10'] and P('מכל', 'איביך', 'מסביב') == ['Deut 25:19'] and P('וישבתם', 'בטח') == ['Deut 12:10'] and U('בטח', 'לבטח', books=T) == ['Deut 12:10', 'Deut 28:52', 'Deut 33:12', 'Deut 33:28', 'Gen 34:25', 'Lev 25:18', 'Lev 25:19', 'Lev 26:5'] and SH(D12(10), ('Josh', 23, 1)) == 4 and SH(D12(10), ('2Sam', 7, 1)) == 1
assert P('והלוי', 'אשר', 'בשעריכם') == ['Deut 12:12'] and P('והלוי', 'אשר', 'בשעריך') == ['Deut 12:18', 'Deut 14:27', 'Deut 16:11'] and P('אין', 'לו', 'חלק', 'ונחלה') == ['Deut 12:12', 'Deut 14:27', 'Deut 14:29'] and P('חלק', 'ונחלה') == ['Deut 10:9', 'Deut 12:12', 'Deut 14:27', 'Deut 14:29', 'Deut 18:1', 'Gen 31:14'] and P('ובניכם', 'ובנתיכם', 'ועבדיכם', 'ואמהתיכם') == ['Deut 12:12'] and P('אתה', 'ובנך', 'ובתך', 'ועבדך', 'ואמתך') == ['Deut 12:18', 'Deut 16:11', 'Deut 16:14', 'Deut 5:14']   # THE SABBATH'S LIST at the eating (12:18) — 5:14's household said again at the place, at the feasts
assert P('השמר', 'לך', 'פן') == ['Deut 12:13', 'Deut 12:19', 'Deut 12:30', 'Deut 15:9', 'Deut 6:12', 'Deut 8:11', 'Exod 34:12', 'Gen 24:6', 'Gen 31:24'] and P('השמרו', 'לכם', 'פן') == ['Deut 11:16', 'Deut 4:23'] and len(U('השמר', books=DT)) == 8 and P('בכל', 'מקום', 'אשר', 'תראה') == ['Deut 12:13'] and P('שם', 'תעלה', 'עלתיך') == ['Deut 12:14'] and P('כל', 'אשר', 'אנכי', 'מצוך', books=DT) == ['Deut 12:14']   # "take heed to yourself lest" THREE TIMES in one chapter (13, 19, 30) — nine in the Bible
assert [s for s, _, _ in LEMT('7535', books=DT) if s.startswith('Deut 12:')] == ['Deut 12:15', 'Deut 12:16', 'Deut 12:23', 'Deut 12:26'] and [s for s, _, _ in LEMT('389', books=DT) if s.startswith('Deut 12:')] == ['Deut 12:22'] and P('בכל', 'אות', 'נפשך') == ['Deut 12:15', 'Deut 12:20', 'Deut 12:21'] and [(s, x) for s, x, _ in LEMT('185')] == [('1Sam 23:20', 'אות'), ('Deut 12:15', 'אות'), ('Deut 12:20', 'אות'), ('Deut 12:21', 'אות'), ('Deut 18:6', 'אות'), ('Hos 10:10', 'באותי'), ('Jer 2:24', 'באות')] and [(s, x) for s, x, _ in LEMT('183', books=T)] == [('Deut 5:21', 'תתאוה'), ('Deut 12:20', 'תאוה'), ('Deut 14:26', 'תאוה'), ('Num 11:4', 'התאוו'), ('Num 11:34', 'המתאוים')]   # "only" FOUR times (15, 16, 23, 26) and "but" once (22) — the restrictive clauses the shelf reads; "the desire of your soul" the chapter's three of the noun's four Torah seats; the craving's verb the quails' (Numbers 11:4, 34) and the tenth word's (5:21)
assert P('תזבח', 'ואכלת', 'בשר') == ['Deut 12:15'] and P('כברכת', 'יהוה', 'אלהיך', 'אשר', 'נתן', 'לך') == ['Deut 12:15', 'Deut 16:17'] and len(P('בכל', 'שעריך', books=DT)) == 4 and P('הטמא', 'והטהור') == ['Deut 12:15', 'Deut 12:22', 'Deut 15:22'] and P('כצבי', 'וכאיל') == ['Deut 12:15', 'Deut 15:22'] and P('הצבי', 'ואת', 'האיל') == ['Deut 12:22'] and len(LEMT('6643 b')) == 14 and [(s, x) for s, x, _ in LEMT('6643 b') if s.startswith('Deut')] == [('Deut 12:15', 'כצבי'), ('Deut 12:22', 'הצבי'), ('Deut 14:5', 'וצבי'), ('Deut 15:22', 'כצבי')] and ('2Sam 1:19', 'הצבי') in [(s, x) for s, x, _ in LEMT('6643 a')]   # THE GAZELLE'S HOMOGRAPH — the same consonants are "the beauty" (2 Samuel 1:19, Isaiah 13:19, Daniel 8:9): the DB's lemma 6643 b the animal, 6643 a the glory; the store glossed the animal "splendor"
assert SH(D12(15), ('Lev', 17, 3)) == 1 and SH(D12(15), ('Lev', 17, 4)) == 1 and SH(D12(15), ('Lev', 17, 5)) == 1 and SH(D12(15), ('Deut', 15, 22)) == 4 and SH(D12(21), ('Lev', 17, 3)) == 2   # THE SLAUGHTER LAW SAID IN NEW WORDS — Leviticus 17:3-5 (every slaughter at the tent's door) shares one token in order with 12:15; the release from it named nowhere by Leviticus's words
assert P('רק', 'הדם', 'לא', 'תאכלו') == ['Deut 12:16'] and P('דם', 'לא', 'תאכלו') == ['Lev 3:17', 'Lev 7:26'] and P('כל', 'דם', 'לא', 'תאכלו') == [] and P('על', 'הארץ', 'תשפכנו', 'כמים') == ['Deut 12:16', 'Deut 12:24', 'Deut 15:23'] and U('כמים', books=T) == ['Deut 12:16', 'Deut 12:24', 'Deut 15:23', 'Gen 49:4'] and SH(D12(16), ('Deut', 15, 23)) == 6 and SH(D12(16), ('Lev', 17, 13)) == 0   # "on the earth you shall pour it like water" the book's three (12:16, 12:24, 15:23) — Leviticus 17:13 covers the blood with dust, Deuteronomy pours it like water: no token shared
assert P('לא', 'תוכל', 'לאכל', 'בשעריך') == ['Deut 12:17'] and P('לא', 'תוכל', books=DT) == ['Deut 12:17', 'Deut 14:24', 'Deut 16:5', 'Deut 17:15', 'Deut 22:3', 'Deut 28:27', 'Deut 28:35', 'Deut 7:22'] and P('נדריך', 'אשר', 'תדר') == ['Deut 12:17'] and SH(D12(17), ('Deut', 14, 23)) == 6
assert P('כי', 'אם', 'לפני', 'יהוה', 'אלהיך', 'תאכלנו') == ['Deut 12:18'] and U('תאכלנו', books=DT) == ['Deut 12:18', 'Deut 12:22', 'Deut 12:24', 'Deut 12:25', 'Deut 15:20', 'Deut 15:22', 'Deut 28:39', 'Deut 5:25'] and P('במקום', 'אשר', 'יבחר', 'יהוה', 'אלהיך', 'בו') == ['Deut 12:18', 'Deut 16:7'] and SH(D12(18), ('Deut', 16, 11)) == 13 and SH(D12(18), ('Deut', 5, 14)) == 8   # 12:18 and the Feast of Weeks' verse (16:11) share thirteen tokens in order — the chapter's closest kin in the book
assert P('פן', 'תעזב', 'את', 'הלוי') == ['Deut 12:19'] and P('כל', 'ימיך', 'על', 'אדמתך') == ['Deut 12:19']   # THE LEVITE'S VERSE ALONE (KINC[19] asserted empty below, after the computation) — no verse of the Bible shares two non-stop tokens with 12:19
assert P('כי', 'ירחיב', 'יהוה', 'אלהיך', 'את', 'גבולך') == ['Deut 12:20'] and [(s, x, m) for s, x, m in LEMT('7337', books=T) if m and 'Vh' in m] == [('Deut 12:20', 'ירחיב', 'HVhi3ms'), ('Deut 19:8', 'ירחיב', 'HVhi3ms'), ('Deut 33:20', 'מרחיב', 'HVhrmsc'), ('Exod 34:24', 'והרחבתי', 'HC/Vhq1cs'), ('Gen 26:22', 'הרחיב', 'HVhp3ms')] and 'גבלך' in words('Deut', 19, 8) and 'גבולך' in W12(20)   # the border's two spellings — plene here, defective at 19:8
assert P('כאשר', 'דבר', 'לך', books=DT) == ['Deut 12:20', 'Deut 15:6', 'Deut 26:18', 'Deut 29:12'] and len(P('כאשר', 'דבר', books=DT)) == 16 and P('אכלה', 'בשר') == ['Deut 12:20'] and P('כי', 'תאוה', 'נפשך', 'לאכל', 'בשר') == ['Deut 12:20'] and sum(1 for v in range(1, 32) for x in W12(v) if x in ('בשר', 'הבשר', 'והבשר')) == 7   # "AS HE HAS SPOKEN TO YOU" (12:20) — the AS_WHEN form, four seats in the book (11:25's is "as He spoke to YOU (pl.)"); "flesh" seven times, four of them in 12:20
assert P('כי', 'ירחק', 'ממך', 'המקום') == ['Deut 12:21', 'Deut 14:24'] and P('כאשר', 'צויתך') == ['Deut 12:21', 'Exod 23:15'] and len(P('כאשר', 'צויתי')) == 6 and len(P('כאשר', 'צוה', books=DT)) == 3 and P('ואכלת', 'בשעריך') == ['Deut 12:21'] and SH(D12(21), ('Deut', 14, 24)) == 12   # THE RECEIPT WITHOUT THE NAME — "as I have commanded you" (12:21) has ONE kin in the Bible, Exodus 23:15's unleavened bread; the finder's forms carry the Name and list no seat here (measured below)
assert P('כאשר', 'יאכל', 'את', 'הצבי', 'ואת', 'האיל') == ['Deut 12:22'] and U('יחדו', books=DT) == ['Deut 12:22', 'Deut 15:22', 'Deut 22:10', 'Deut 22:11', 'Deut 25:11', 'Deut 25:5', 'Deut 33:17']
assert P('רק', 'חזק', 'לבלתי', 'אכל', 'הדם') == ['Deut 12:23'] and [(s, x, m) for s, x, m in LEMT('2388', books=DT) if m and m.endswith('v2ms')] == [('Deut 1:38', 'חזק', 'HVpv2ms'), ('Deut 12:23', 'חזק', 'HVqv2ms'), ('Deut 31:7', 'חזק', 'HVqv2ms'), ('Deut 31:23', 'חזק', 'HVqv2ms')] and P('כי', 'הדם', 'הוא', 'הנפש') == ['Deut 12:23'] and P('ולא', 'תאכל', 'הנפש', 'עם', 'הבשר') == ['Deut 12:23'] and SH(D12(23), ('Lev', 17, 11)) == 3 and SH(D12(23), ('Gen', 9, 4)) == 0   # "BE STRONG" said to a man about the blood — the word said to Joshua (1:38, 31:7, 23); "the blood is the life" Leviticus 17:11's clause turned (there "the life of the flesh is in the blood"), Genesis 9:4's shares nothing
assert P('לא', 'תאכלנו') == ['Deut 12:24', 'Deut 12:25'] and P('למען', 'ייטב', 'לך', 'ולבניך', 'אחריך') == ['Deut 12:25', 'Deut 12:28'] and P('כי', 'תעשה', 'הישר', 'בעיני', 'יהוה') == ['Deut 12:25', 'Deut 21:9'] and P('הטוב', 'והישר') == ['2Chr 14:1', '2Chr 31:20', '2Kgs 10:3', 'Deut 12:28'] and len(P('הישר', 'בעיני', 'יהוה')) == 21 and SH(D12(25), ('Deut', 12, 28)) == 9 and SH(D12(28), ('Deut', 4, 40)) == 10   # "that it may go well with you and your children after you" — 12:25 and 12:28 alone (4:40's "after you" the kin); "the good and the right" 6:18's pair, Kings' measure of a king
assert P('רק', 'קדשיך', 'אשר', 'יהיו', 'לך', 'ונדריך') == ['Deut 12:26'] and U('קדשיך') == ['Deut 12:26'] and P('תשא', 'ובאת', 'אל', 'המקום') == ['Deut 12:26'] and P('ועשית', 'עלתיך', 'הבשר', 'והדם') == ['Deut 12:27'] and P('ודם', 'זבחיך', 'ישפך', 'על', 'מזבח') == ['Deut 12:27'] and U('ישפך', books=T) == ['Deut 12:27', 'Deut 19:10', 'Gen 9:6', 'Lev 4:18', 'Lev 4:25', 'Lev 4:30', 'Lev 4:34', 'Lev 4:7'] and P('מזבח', 'יהוה', 'אלהיך') == ['Deut 12:27', 'Deut 16:21', 'Deut 26:4', 'Deut 27:6'] and P('והבשר', 'תאכל') == ['Deut 12:27'] and SH(D12(27), ('Lev', 4, 7)) == 5 and SH(D12(27), ('Lev', 17, 6)) == 3   # "shall be poured" — the sin offering's verb (Leviticus 4:7, 18, 25, 30, 34: the rest of the blood at the altar's base) said of the sacrifices' blood
assert P('שמר', 'ושמעת', 'את', 'כל', 'הדברים', 'האלה') == ['Deut 12:28'] and len(P('כל', 'הדברים', 'האלה', books=DT)) == 4 and P('עד', 'עולם', books=DT) == ['Deut 12:28', 'Deut 23:4', 'Deut 28:46', 'Deut 29:28'] and words('Deut', 13, 1) == ['את', 'כל', 'הדבר', 'אשר', 'אנכי', 'מצוה', 'אתכם', 'אתו', 'תשמרו', 'לעשות', 'לא', 'תסף', 'עליו', 'ולא', 'תגרע', 'ממנו']   # THE DB'S 13:1 IS THE ENGLISH'S 12:32 — "you shall not add to it nor take from it" opens the next chapter in the Hebrew numbering: chapter 13's reading
assert P('כי', 'יכרית', 'יהוה', 'אלהיך', 'את', 'הגוים') == ['Deut 12:29', 'Deut 19:1'] and P('אשר', 'אתה', 'בא', 'שמה', 'לרשת', 'אותם') == ['Deut 12:29'] and P('וירשת', 'אתם', 'וישבת', 'בארצם') == ['Deut 12:29'] and SH(D12(29), ('Deut', 19, 1)) == 8 and SH(D12(29), ('Deut', 7, 1)) == 8 and words('Deut', 19, 1)[-3:] == ['וישבת', 'בעריהם', 'ובבתיהם']
assert P('פן', 'תנקש', 'אחריהם') == ['Deut 12:30'] and [(s, x, m) for s, x, m in LEMT('5367')] == [('1Sam 28:9', 'מתנקש', 'HVtrmsa'), ('Deut 12:30', 'תנקש', 'HVNi2ms'), ('Ps 9:17', 'נוקש', 'HVqrmsa'), ('Ps 38:13', 'וינקשו', 'HC/Vpw3mp'), ('Ps 109:11', 'ינקש', 'HVpi3ms')] and [(s, x, m) for s, x, m in LEMT('3369', books=T)] == [('Deut 7:25', 'תוקש', 'HVNi2ms')] and P('אחרי', 'השמדם', 'מפניך') == ['Deut 12:30'] and P('ופן', 'תדרש', 'לאלהיהם') == ['Deut 12:30'] and U('איכה', books=T) == ['Deut 12:30', 'Deut 18:21', 'Deut 1:12', 'Deut 32:30', 'Deut 7:17', 'Gen 3:9'] and P('ואעשה', 'כן', 'גם', 'אני') == ['Deut 12:30']   # "lest you be ENSNARED" — the snare's root here (נקש) is not 7:25's (יקש): the Torah's one seat of each niphal
assert P('כל', 'תועבת', 'יהוה', 'אשר', 'שנא') == ['Deut 12:31'] and len(P('תועבת', 'יהוה')) == 19 and [s for s in P('תועבת', 'יהוה') if s.startswith('Deut')] == ['Deut 12:31', 'Deut 17:1', 'Deut 18:12', 'Deut 22:5', 'Deut 23:19', 'Deut 25:16', 'Deut 27:15', 'Deut 7:25'] and P('אשר', 'שנא') == ['Deut 12:31', 'Deut 16:22'] and P('כי', 'גם', 'את', 'בניהם', 'ואת', 'בנתיהם', 'ישרפו', 'באש', 'לאלהיהם') == ['Deut 12:31'] and P('בניהם', 'ואת', 'בנתיהם') == ['Deut 12:31', 'Jer 7:31'] and P('לשרף', 'את', 'בניהם') == ['Jer 19:5', 'Jer 7:31'] and P('מעביר', 'בנו', 'ובתו', 'באש') == ['Deut 18:10'] and SH(D12(31), ('Jer', 7, 31)) == 6 and SH(D12(31), ('2Kgs', 17, 31)) == 4 and SH(D12(31), ('Lev', 18, 21)) == 3
assert 'Lev 18:21' in U('למלך') and 'Lev 20:2' in U('למלך') and 'Lev 20:3' in U('למלך') and len(U('למלך')) > 150   # THE KING-WORD'S HOMOGRAPH — Molech's consonants are "to the king" (the census's slip at 7:8 and 11:3); 12:31 names no Molech: "to their gods"
# ---- THE KIN FOUND BY COMPUTATION (the measure's A print, recomputed): the closest verses of the Bible by shared distinct tokens ----
STOP = set(('את ואת אשר כל וכל על ועל אל ואל '   # (the object marker, and-it, which, all, on, to — the particles)
            'לא ולא כי אם יהוה אלהיך אלהיכם '   # (not, for, if; the LORD, your God)
            'לך לכם בו שם שמה גם מן ממך עד '   # (to you, in it, there, also, from, until)
            'הוא היא אתם אתה אנכי אני לו לה '   # (he, she, you, I, to him, to her)
            'בכל כאשר כן הימים היום אלה האלה '   # (in all, as, so, the days, today, these)
            'בארץ הארץ אשר ואם או פן ופן').split())   # (in the land, the land, which, and if, or, lest) — the stopword set glossed piece by piece (the lint's ninety-character window)
ORD = {k: i for i, k in enumerate(by)}
TOK = {k: set(words(*k)) - STOP for k in by}
KINC = {}
for v in range(1, 32):
    me = D12(v); t = TOK[me]
    sc = sorted(((len(t & TOK[k]), k) for k in by if k != me and len(t & TOK[k]) >= 2), key=lambda x: (-x[0], ORD[x[1]]))[:8]
    KINC[v] = [(f'{k[0]} {k[1]}:{k[2]}', n, SH(me, k) if i < 3 else None) for i, (n, k) in enumerate(sc)]
assert KINC[18][0] == ('Deut 16:11', 10, 13) and KINC[17][0] == ('Deut 14:23', 6, 6) and KINC[21][0] == ('Deut 14:24', 5, 12) and KINC[28][:2] == [('Deut 12:25', 6, 9), ('Deut 4:40', 4, 10)] and KINC[2][:3] == [('2Chr 28:4', 4, 6), ('2Kgs 16:4', 4, 6), ('Ezek 6:13', 4, 6)] and KINC[8][3:5] == [('Judg 17:6', 3, None), ('Judg 21:25', 3, None)] and KINC[31][:2] == [('2Kgs 17:31', 3, 4), ('Deut 20:18', 3, 4)] and KINC[12][0] == ('Deut 14:27', 4, 7) and KINC[29][:3] == [('Deut 9:5', 4, 5), ('Deut 9:4', 3, 5), ('Deut 19:1', 3, 8)] and KINC[19] == []

# ---- THE COUNTER'S DAY AND THE TWO PARAMETERS (a bare world on the exodus epoch; no clock walk this chapter — no marker, no stretch) ----
with contextlib.redirect_stdout(io.StringIO()):
    _WC = WE.World(era='the counter\'s day — chapter 12 on a bare world (the exodus epoch)', epoch='exodus')
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
PLACE_WORDS = r"\b(place_chosen\w*|rejoicing_before\w*|profane_slaughter\w*|holy_things_in_the_gates\w*|levite_forsaking\w*|name_erasure\w*|foreign_rite\w*|the place which the LORD (?:your God )?will choose|profane slaughter|forsake the Levite)\b"
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

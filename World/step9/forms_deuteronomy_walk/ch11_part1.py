#!/usr/bin/env python3
# DEUTERONOMY 11:1-32 — THE DISCIPLINE RETOLD, THE LAND WATERED BY HEAVEN, THE SECOND PARAGRAPH, THE BORDERS AND THE DREAD, THE BLESSING AND THE CURSE —
# THE READBACK'S FORMS ON FILE, NO NEW FORM (THE DEUTERONOMY WALK sitting 9b, 2026-09-20; World/step9/DEUTERONOMY_WALK.md "Sitting 9b"; the state doc's #199).
# The chapter retells the discipline (11:1-7 — the exodus, the sea, Dathan and Abiram, the wilderness: EVERY ACT WITH A LINE ON THE TAPE, measured — no retrograde
# marker; the tape already leaves Korah unnamed at the swallowing as the chapter does; 11:5 the STATE row, SUPPLIED with no write — chapter 8's fifth form),
# praises the land (11:8-12 by CALL — the land watered by heaven, first: Ta'anit 10a:2-3), gives THE SECOND PARAGRAPH (11:13-21 — THE RAIN CONDITIONAL WITH NO
# CELL ANYWHERE IN THE MACHINE, compiled at the chapter's own day (40, 11, 1): the line second_paragraph_declared writing rain_in_its_season and
# heavens_shut_for_turning — conditional HEAVEN entries, Leviticus 26:4 and 26:19-20 by CALL — and yoke_of_the_commandments_accepted, THE ANSWER SHEET'S OWN NAME
# (Mishnah Berakhot 2:2; Berakhot 14b:11); the duties 6:6-9's said again by CALL, no second shema line; 11:16's warning by CALL, no second block), restates the
# borders and the dread (11:22-25 by CALL; 11:25's 'as He spoke to you' A RUN_CITATION POINTER to Exodus 23:27 — the fourth receipt shape, two teachers: the
# Sifrei 52:4, Tosefta Sotah 8:6), and sets THE BLESSING AND THE CURSE (11:26-32 — THE CHAPTER'S LAW compiled at its own day: the line blessing_and_curse_set
# writing blessing_and_curse_set — a STATUS — and gerizim_ebal_ceremony_owed — a DEBIT on Israel toward Heaven OPEN to Joshua 8:30-35, the run outside the
# Torah's tape; the ceremony's form, tongue, day and forty-eight covenants from the shelf; its place a three-arm PARAMETER). TWO own-day lines, NO marker;
# FIVE writes; the open debits on Israel 9 -> 10. The daemon law_blessing_and_curse given_at Deut 11:1, installed_by boot (the Deuteronomy daemons' form).
# Six cells; every token probed (zero-report law); effects on every cell (the effects law); the DATA rows the docket added (the shutting's value and threshold,
# 'in its season' the free variable after the decree, the cattle before the man, the pointer's second teacher, the place's three arms, the ceremony's day and
# tongue and count, the dispossession the crossing's condition, the Samaritan variant, the rain's source a dispute, the causes a parameter, the empty export
# row). Reading ledger: logic/oral_triage/deu_11_ekev_reeh_2026-09-20.md (210 sources, 6 claims); the exam's docket: deu_11_ekev_reeh_exam_2026-09-20.md
# (1,048 rows — 477 READ WHOLE here, 571 carried with their ledgers' own verdicts: LAW 258 / DERIVATION 150 / DISPUTE 113 / CONTEXT 423 / OUTSIDE 104).

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
import cold_run_hear_o_israel as HI            # THE EDGE: blessing_and_curse -> hear_o_israel CALL, reference (11:18-20's duties 6:6-9's said again; 11:9's milk and honey; 11:21's sons; 11:13's heart and soul; 11:1's love)
import cold_run_good_land as GL                # THE EDGE: blessing_and_curse -> good_land CALL, reference (11:8-9 = 8:1's frame; 11:2's discipline; 11:5's wilderness the state row; 11:10-12's land; 11:15's eat and be satisfied; 11:16's serve and bow; 11:28's not hearken)
import cold_run_seven_nations as SN            # THE EDGE: blessing_and_curse -> seven_nations CALL, reference (11:23's nations; 11:14's grain, wine and oil; 11:27's blessing; 11:25's no man shall stand; 11:7's trials)
import cold_run_not_righteousness as NR        # THE EDGE: blessing_and_curse -> not_righteousness CALL, reference (11:23's 'greater and mightier than you' 9:1's; 11:28's 'turn aside from the way' the calf's; 11:5's wilderness 9:7's)
import cold_run_obey_horeb as OH               # THE EDGE: blessing_and_curse -> obey_horeb CALL, reference (11:23's dispossession 4:38's; 11:32's statutes and judgments 4:8's; 4:4's cleaving the state; 11:16's 'take heed' 4:23's form)
import cold_run_second_tablets as ST           # THE EDGE: blessing_and_curse -> second_tablets CALL, reference (11:1's five duties 10:12's; 11:22's cleaving 10:20's; 11:25's receipt shape beside 10:9's)
import cold_run_covenant_at_horeb as CH        # THE EDGE: blessing_and_curse -> covenant_at_horeb CALL, reference (11:16's 'serve other gods and bow' the second word's pair — the block other_gods_barred standing, no second block)
import cold_run_tochacha as TC                 # THE EDGE: blessing_and_curse -> tochacha CALL, reference (11:14's rains in their season Leviticus 26:4's; 11:17's shut heavens 26:19-20's iron heavens — no line on the tape, the cells)
import cold_run_ordinances as OR               # THE EDGE: blessing_and_curse -> ordinances CALL, reference (11:25's terror Exodus 23:27's — the pointer's target; 11:24's extents 23:31's; the hornet, little by little)
import cold_run_borders as BR                  # THE EDGE: blessing_and_curse -> borders CALL, reference (11:24's four extents against Numbers 34's spec; the land-bound rule; Joshua's receipts)
import cold_run_korach as KR                   # THE EDGE: blessing_and_curse -> korach CALL, reference (11:6's Dathan and Abiram swallowed — Korah unnamed on the tape as in the chapter; the death mode the open row; Korah's wealth)
import cold_run_second_census as SC            # THE EDGE: blessing_and_curse -> second_census CALL, reference (11:6's 'this is Dathan and Abiram' 26:9-11's; 11:2's children who have not known the census's generation)
import cold_run_exodus_story as ES             # THE EDGE: blessing_and_curse -> exodus_story CALL, reference (11:3's signs and deeds the ten plagues; 11:4's sea — saved at the sea, the song, the ten miracles)
import cold_run_primeval as PR                 # THE EDGE: blessing_and_curse -> primeval CALL, reference (11:6's 'every living thing' the flood's word; 11:10's 'like the land of Egypt' Lot's clause; 11:30's terebinths of Moreh Abram's)

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
def W11(v): return words('Deut', 11, v)
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
D11 = lambda v: ('Deut', 11, v)
NEG = ('לא', 'ולא')
NAME = ('יהוה', 'ליהוה', 'ויהוה', 'ביהוה', 'מיהוה')

P_ = []   # the provenance trail of the case being run
def ink(ref, note):  P_.append(('INK',  'Deut %s — %s' % (ref, note) if not ref[:1].isupper() else '%s — %s' % (ref, note)))
def move(src, note): P_.append(('MOVE', '%s — %s' % (src, note)))
def dat(note):       P_.append(('DATA', note))
def hyp(note):       P_.append(('HYP',  note))     # THE LINK REVIEW LAW: a hypothesis — no teacher; counted apart, never as compiled
def out(verdict, effects):
    """verdict + registry-validated effects (the engine contract)"""
    FX.validate([e for e in effects if e != FX.NONE])
    return verdict, effects, list(P_)

# ---- THE INK, computed (the parser and the tokens; the reading's facts the expectations — every assert PROVEN at the reading, ch11_ink.py — COPIED from the reading's instrument by content markers, the sequence module's names made the exec'd parser's; the store-bound asserts left to the reading) ----
SPAN = [(11, v) for v in range(1, 33)]
def MARKS(c, v): return [t for t in verse_words('Deut', c, v) if t[-1] in '#~^%@|*']
def N(b, c, v): return ink_numbers(verse_words(b, c, v))
NUMS = {v: ink_numbers(verse_words('Deut', 11, v)) for v in range(1, 33)}
ORDS = {v: ink_ordinals(verse_words('Deut', 11, v)) for v in range(1, 33)}
PARSED = {(11, v): n for v, n in NUMS.items() if n}
assert PARSED == {} and all(o == [] for o in ORDS.values()), (PARSED, ORDS)   # NO NUMBER VERSE IN THE CHAPTER (the book's first such chapter since the walk began — measured at the reading)
TOK = sum(len(W11(v)) for v in range(1, 33)); LET = sum(len(x) for v in range(1, 33) for x in W11(v))
assert TOK == 508 and LET == 1992, (TOK, LET)
assert {v: len(W11(v)) for v in range(1, 33)} == {1: 11, 2: 23, 3: 13, 4: 21, 5: 9, 6: 26, 7: 10, 8: 19, 9: 16, 10: 22, 11: 13, 12: 16, 13: 20, 14: 10, 15: 6, 16: 11, 17: 24, 18: 17, 19: 12, 20: 5, 21: 17, 22: 22, 23: 12, 24: 21, 25: 19, 26: 7, 27: 13, 28: 23, 29: 23, 30: 17, 31: 18, 32: 12}
# THE ENGINE'S PARSER on every verse — MEASURED before the compile is asked: NO NUMBER VERSE IN THE CHAPTER (chapter 10 had five); "swore" (11:9, 11:21) the seven-stem homograph no number; "be satisfied" starred at 11:15 (chapter 8's lesson); the kin's numbers — Korah's two hundred and fifty (Numbers 16:2, 17, 35; 26:10), the plague's 14,700 (17:14), the six hundred chariots (Exodus 14:7), the six hundred thousand (12:37), the creed's [1] (6:4), the seven nations [7] (7:1)
PARSE = {v: (ink_numbers(verse_words('Deut', 11, v)), ink_ordinals(verse_words('Deut', 11, v)), [t for t in verse_words('Deut', 11, v) if t[-1] in '#~^%@|*']) for v in range(1, 33)}
assert all(n == [] and o == [] for n, o, _ in PARSE.values()) and {v: m for v, (_, _, m) in PARSE.items() if m} == {15: ['ושבעת*']}, {v: p for v, p in PARSE.items() if any(p)}
assert [s for s, x, _ in LEMT('7650') if s.startswith('Deut 11:')] == ['Deut 11:9', 'Deut 11:21'] and 'נשבע' in W11(9) and 'נשבע' in W11(21)
KINNUM = {k: ink_numbers(verse_words(*k)) for k in [('Num', 16, 2), ('Num', 16, 17), ('Num', 16, 35), ('Num', 17, 14), ('Num', 26, 10), ('Exod', 14, 7), ('Exod', 12, 37), ('Deut', 6, 4), ('Deut', 7, 1), ('Num', 26, 9), ('Exod', 13, 16), ('Deut', 6, 8), ('Gen', 15, 18), ('Josh', 1, 3), ('Josh', 1, 4), ('Deut', 27, 12), ('Deut', 27, 13), ('Gen', 12, 6), ('Josh', 8, 33)]}
assert KINNUM == {('Num', 16, 2): [250], ('Num', 16, 17): [250], ('Num', 16, 35): [250], ('Num', 17, 14): [14700], ('Num', 26, 10): [250], ('Exod', 14, 7): [600], ('Exod', 12, 37): [600000], ('Deut', 6, 4): [1], ('Deut', 7, 1): [7], ('Num', 26, 9): [], ('Exod', 13, 16): [], ('Deut', 6, 8): [], ('Gen', 15, 18): [], ('Josh', 1, 3): [], ('Josh', 1, 4): [], ('Deut', 27, 12): [], ('Deut', 27, 13): [], ('Gen', 12, 6): [], ('Josh', 8, 33): []}, KINNUM
# THE REGISTER, computed on the morphology: the second person PLURAL in nineteen verses, SINGULAR in five (1, 12, 15, 20, 29), BOTH in five (8, 10, 14, 19, 26 — "See" the singular imperative over "before you" plural), NEITHER in three (3, 6, 30); GOD'S FIRST PERSON INSIDE MOSES' SPEECH — "My commandments" (13), "and I will give" (14, 15), "My words" (18) — beside Moses' seven "I"; the imperatives TWO (16 "take heed", 26 "See"); the infinitive absolutes TWO (13 "hearken diligently", 22 "keep diligently"); THE CONSECUTIVE PERFECTS THIRTY-TWO in seventeen verses — the law's form; the wayyiqtol TWO (4 "and He destroyed them", 6 "and swallowed them") — the retelling's two narrative verbs; NO prohibition on Israel (every "not" a condition or a consequence); no "saying", no divine frame
NUM = {v: (sum(1 for _, m in wm('Deut', 11, v) if m and '2mp' in m), sum(1 for _, m in wm('Deut', 11, v) if m and '2ms' in m)) for v in range(1, 33)}
assert NUM == {1: (0, 3), 2: (3, 0), 3: (0, 0), 4: (1, 0), 5: (2, 0), 6: (0, 0), 7: (1, 0), 8: (5, 1), 9: (2, 0), 10: (1, 5), 11: (1, 0), 12: (0, 2), 13: (5, 0), 14: (1, 4), 15: (0, 4), 16: (6, 0), 17: (3, 0), 18: (6, 0), 19: (2, 5), 20: (0, 3), 21: (3, 0), 22: (3, 0), 23: (3, 0), 24: (3, 0), 25: (6, 0), 26: (1, 1), 27: (3, 0), 28: (5, 0), 29: (0, 4), 30: (0, 0), 31: (5, 0), 32: (2, 0)}
assert [v for v, (p, s) in NUM.items() if s and not p] == [1, 12, 15, 20, 29] and [v for v, (p, s) in NUM.items() if p and s] == [8, 10, 14, 19, 26] and [v for v, (p, s) in NUM.items() if not p and not s] == [3, 6, 30] and len([v for v, (p, s) in NUM.items() if p and not s]) == 19
assert {v: [(x, m) for x, m in wm('Deut', 11, v) if m and '1cs' in m] for v in range(1, 33) if any(m and '1cs' in m for _, m in wm('Deut', 11, v))} == {8: [('אנכי', 'HPp1cs')], 13: [('מצותי', 'HNcfpc/Sp1cs'), ('אנכי', 'HPp1cs')], 14: [('ונתתי', 'HC/Vqq1cs')], 15: [('ונתתי', 'HC/Vqq1cs')], 18: [('דברי', 'HNcmpc/Sp1cs')], 22: [('אנכי', 'HPp1cs')], 26: [('אנכי', 'HPp1cs')], 27: [('אנכי', 'HPp1cs')], 28: [('אנכי', 'HPp1cs')], 32: [('אנכי', 'HPp1cs')]}
assert {v: [(x, m) for x, m in wm('Deut', 11, v) if m and re.match(r'^HV.?.?v', m)] for v in range(1, 33) if any(m and re.match(r'^HV.?.?v', m) for _, m in wm('Deut', 11, v))} == {16: [('השמרו', 'HVNv2mp')], 26: [('ראה', 'HVqv2ms')]}
assert {v: [(x, m) for x, m in wm('Deut', 11, v) if m and re.match(r'^H(?:C/)?V.a$', m)] for v in range(1, 33) if any(m and re.match(r'^H(?:C/)?V.a$', m) for _, m in wm('Deut', 11, v))} == {13: [('שמע', 'HVqa')], 22: [('שמר', 'HVqa')]}
WEQ = {v: [x for x, m in wm('Deut', 11, v) if m and re.search(r'^HC/V.q', m)] for v in range(1, 33) if any(m and re.search(r'^HC/V.q', m) for _, m in wm('Deut', 11, v))}
assert WEQ == {1: ['ואהבת', 'ושמרת'], 2: ['וידעתם'], 8: ['ושמרתם', 'ובאתם', 'וירשתם'], 10: ['והשקית'], 13: ['והיה'], 14: ['ונתתי', 'ואספת'], 15: ['ונתתי', 'ואכלת', 'ושבעת'], 16: ['וסרתם', 'ועבדתם', 'והשתחויתם'], 17: ['וחרה', 'ועצר', 'ואבדתם'], 18: ['ושמתם', 'וקשרתם', 'והיו'], 19: ['ולמדתם'], 20: ['וכתבתם'], 23: ['והוריש', 'וירשתם'], 28: ['וסרתם'], 29: ['והיה', 'ונתתה'], 31: ['וירשתם', 'וישבתם'], 32: ['ושמרתם']} and sum(len(x) for x in WEQ.values()) == 32 and len(WEQ) == 17
assert {v: [x for x, m in wm('Deut', 11, v) if m and re.search(r'^HC/V.w', m)] for v in range(1, 33) if any(m and re.search(r'^HC/V.w', m) for _, m in wm('Deut', 11, v))} == {4: ['ויאבדם'], 6: ['ותבלעם']}
PTC = {v: [(x, m) for x, m in wm('Deut', 11, v) if m and re.search(r'^H(?:C/|R/|Td/|C/R/)?V.r', m)] for v in range(1, 33) if any(m and re.search(r'^H(?:C/|R/|Td/|C/R/)?V.r', m) for _, m in wm('Deut', 11, v))}
assert sum(len(x) for x in PTC.values()) == 18 and len(PTC) == 16 and PTC[12] == [('דרש', 'HVqrmsa')] and PTC[7] == [('הראת', 'HTd/Vqrfpa')] and PTC[30] == [('הישב', 'HTd/Vqrmsa')] and PTC[9] == [('זבת', 'HVqrfsc')]
assert {v: [(x, m) for x, m in wm('Deut', 11, v) if m and re.search(r'^H(?:Ti/)?V.i2', m)] for v in range(1, 33) if any(m and re.search(r'^H(?:Ti/)?V.i2', m) for _, m in wm('Deut', 11, v))} == {8: [('תחזקו', 'HVqi2mp')], 9: [('תאריכו', 'HVhi2mp')], 10: [('תזרע', 'HVqi2ms')], 13: [('תשמעו', 'HVqi2mp')], 22: [('תשמרון', 'HVqi2mp/Sn')], 25: [('תדרכו', 'HVqi2mp')], 27: [('תשמעו', 'HVqi2mp')], 28: [('תשמעו', 'HVqi2mp')]}
assert {v: [x for x in W11(v) if x in NEG] for v in range(1, 33) if any(x in NEG for x in W11(v))} == {2: ['לא', 'לא', 'לא'], 10: ['לא'], 17: ['ולא', 'לא'], 25: ['לא'], 28: ['לא', 'לא']}   # no "not" before a second-person imperfect: no prohibition on Israel in the chapter
assert {f'11:{v}': [x for x in W11(v) if x in ('כי', 'אם', 'ואם', 'או', 'פן')] for v in range(1, 33) if any(x in ('כי', 'אם', 'ואם', 'או', 'פן') for x in W11(v))} == {'11:2': ['כי'], '11:7': ['כי'], '11:10': ['כי'], '11:13': ['אם'], '11:16': ['פן'], '11:22': ['כי', 'אם'], '11:28': ['אם'], '11:29': ['כי'], '11:31': ['כי']}
assert [v for v in range(1, 33) if 'לאמר' in W11(v)] == [] and [v for v in range(1, 33) if any(W11(v)[i] in ('ויאמר', 'וידבר') and W11(v)[i + 1] == 'יהוה' for i in range(len(W11(v)) - 1))] == []
assert {v: [x for x in W11(v) if x in ('למען', 'ולמען')] for v in range(1, 33) if any(x in ('למען', 'ולמען') for x in W11(v))} == {8: ['למען'], 9: ['ולמען'], 21: ['למען']} and len(U('למען', 'ולמען', books=('Deut',))) == 43
assert sum(1 for v in range(1, 33) for x in W11(v) if x == 'יהוה') == 18 and [v for v in range(1, 33) if any(W11(v)[i:i + 2] == ['יהוה', 'אלהיך'] for i in range(len(W11(v)) - 1))] == [1, 12, 29] and [v for v in range(1, 33) if any(W11(v)[i:i + 2] == ['יהוה', 'אלהיכם'] for i in range(len(W11(v)) - 1))] == [2, 13, 22, 25, 27, 28, 31]
assert [v for v in range(1, 33) for x in W11(v) if x == 'ישראל'] == [6] and [v for v in range(1, 33) for x in W11(v) if x in ('מצרים', 'מצרימה')] == [3, 3, 4, 10] and [v for v in range(1, 33) for x in W11(v) if x == 'משה'] == [] and sum(1 for v in range(1, 33) for x in W11(v) if x == 'היום') == 8
assert Counter(int(s.split()[1].split(':')[0]) for s in U('משה', 'למשה', 'ומשה', books=('Deut',))) == Counter({31: 10, 34: 6, 4: 4, 1: 3, 27: 3, 32: 3, 33: 2, 15: 1, 28: 1, 29: 1, 5: 1})   # MOSES UNNAMED FROM CHAPTER 6 TO 14 (chapter 10's find extended: no "Moses" token in 6-14)
# THE KIN DIFFED (computed token by token, the shared tokens counted in order — the measure's A print)
import difflib
def SH(a, b_): return sum(s for _, _, s in difflib.SequenceMatcher(a=words(*a), b=words(*b_)).get_matching_blocks())
D11 = lambda v: ('Deut', 11, v)
assert SH(D11(1), ('Deut', 30, 16)) == 5 and SH(D11(1), ('Deut', 6, 5)) == 4 and SH(D11(1), ('Gen', 26, 5)) == 0 and SH(D11(1), ('1Kgs', 2, 3)) == 5
assert SH(D11(2), ('Deut', 31, 13)) == 7 and SH(D11(2), ('Deut', 8, 5)) == 3 and SH(D11(3), ('Deut', 29, 1)) == 6 and SH(D11(3), ('Deut', 34, 11)) == 5
assert SH(D11(4), ('Deut', 34, 6)) == 4 and SH(D11(4), ('Josh', 24, 6)) == 3 and max((SH(D11(4), ('Exod', 14, v)), v) for v in range(1, 32)) == (3, 31) and max(SH(D11(4), ('Exod', 15, v)) for v in range(1, 22)) == 2   # THE SEA TOLD IN NEW WORDS: no verse of Exodus 14-15 shares more than three tokens (14:31's 'which the LORD did against Egypt' the three)
assert SH(D11(5), ('Deut', 9, 7)) == 6 and SH(D11(5), ('Deut', 1, 31)) == 5
assert SH(D11(6), ('Num', 16, 32)) == 8 and SH(D11(6), ('Num', 16, 30)) == 5 and SH(D11(6), ('Gen', 7, 4)) == 5 and SH(D11(6), ('Gen', 7, 23)) == 4 and SH(D11(6), ('Num', 26, 10)) == 4 and SH(D11(6), ('Ps', 106, 17)) == 0
assert SH(D11(7), ('Judg', 2, 7)) == 6 and SH(D11(7), ('Josh', 24, 31)) == 6 and SH(D11(7), ('Deut', 3, 21)) == 5 and SH(D11(7), ('Deut', 4, 3)) == 5   # JOSHUA'S AND JUDGES' EPILOGUE read the elders' generation from this verse
assert SH(D11(8), ('Deut', 8, 1)) == 12 and SH(D11(8), ('Deut', 4, 1)) == 8 and SH(D11(9), ('Deut', 11, 21)) == 8 and SH(D11(9), ('Josh', 5, 6)) == 8 and SH(D11(9), ('Num', 16, 13)) == 3 and SH(D11(9), ('Num', 16, 14)) == 4
assert SH(D11(10), ('Deut', 11, 29)) == 8 and SH(D11(10), ('Deut', 7, 1)) == 7 and SH(D11(10), ('Gen', 13, 10)) == 3 and SH(D11(11), ('Deut', 8, 7)) == 2 and SH(D11(12), ('Ps', 34, 16)) == 2 and SH(D11(12), ('Zech', 4, 10)) == 2
assert SH(D11(13), ('Josh', 22, 5)) == 11 and SH(D11(13), ('Deut', 11, 22)) == 10 and SH(D11(13), ('Deut', 13, 4)) == 9 and SH(D11(13), ('Deut', 28, 1)) == 6 and SH(D11(13), ('Deut', 6, 5)) == 4
assert SH(D11(14), ('Deut', 7, 13)) == 3 and SH(D11(14), ('Lev', 26, 4)) == 1 and SH(D11(15), ('Deut', 6, 11)) == 2 and SH(D11(15), ('Deut', 8, 10)) == 2
assert SH(D11(16), ('Josh', 23, 16)) == 5 and SH(D11(16), ('1Kgs', 9, 6)) == 5 and SH(D11(17), ('Josh', 23, 16)) == 11 and SH(D11(17), ('Deut', 4, 26)) == 6 and SH(D11(17), ('Lev', 26, 20)) == 5 and SH(D11(17), ('2Chr', 6, 26)) == 5   # JOSHUA'S FAREWELL (23:16) reads 11:16-17 back — five and eleven tokens
assert SH(D11(18), ('Deut', 6, 8)) == 5 and SH(D11(18), ('Exod', 13, 9)) == 3 and SH(D11(18), ('Exod', 13, 16)) == 3 and SH(D11(19), ('Deut', 6, 7)) == 7 and SH(D11(20), ('Deut', 6, 9)) == 4 and SH(D11(21), ('Deut', 11, 9)) == 8 and SH(D11(21), ('Deut', 30, 20)) == 7
assert SH(D11(22), ('Josh', 22, 5)) == 12 and SH(D11(22), ('Deut', 19, 9)) == 10 and SH(D11(22), ('Deut', 11, 13)) == 10 and SH(D11(23), ('Deut', 31, 3)) == 5 and SH(D11(23), ('Josh', 23, 13)) == 5
assert SH(D11(24), ('Josh', 1, 3)) == 7 and SH(D11(24), ('Josh', 1, 4)) == 7 and SH(D11(24), ('Deut', 1, 7)) == 5 and SH(D11(24), ('Gen', 15, 18)) == 3 and SH(D11(24), ('Exod', 23, 31)) == 1   # JOSHUA 1:3-4 reads the borders from this verse, seven and seven
assert SH(D11(25), ('Josh', 1, 5)) == 5 and SH(D11(25), ('Deut', 7, 24)) == 3 and SH(D11(25), ('Deut', 2, 25)) == 4 and SH(D11(26), ('Deut', 4, 8)) == 4 and SH(D11(26), ('Deut', 11, 32)) == 4 and SH(D11(26), ('Deut', 30, 15)) == 2
assert SH(D11(27), ('Deut', 11, 28)) == 10 and SH(D11(28), ('Deut', 28, 14)) == 9 and SH(D11(28), ('Deut', 13, 3)) == 7 and SH(D11(29), ('Deut', 7, 1)) == 11 and SH(D11(29), ('Deut', 6, 10)) == 8 and SH(D11(29), ('Josh', 8, 33)) == 6
assert SH(D11(30), ('Deut', 1, 1)) == 4 and SH(D11(30), ('Gen', 12, 6)) == 1 and SH(D11(31), ('Josh', 1, 11)) == 13 and SH(D11(31), ('Deut', 12, 10)) == 7 and SH(D11(32), ('Deut', 5, 1)) == 7 and SH(D11(32), ('Deut', 7, 11)) == 7   # JOSHUA 1:11 repeats 11:31 — thirteen of eighteen tokens
# THE PHRASE CENSUSES (the B print) — 11:1-7 THE DISCIPLINE SEEN
assert P('ואהבת', 'את', 'יהוה', 'אלהיך') == ['Deut 11:1', 'Deut 6:5'] and U('ואהבת', books=T) == ['Deut 11:1', 'Deut 6:5', 'Lev 19:18', 'Lev 19:34'] and U('לאהבה', 'ולאהבה', books=('Deut',)) == ['Deut 10:12', 'Deut 10:15', 'Deut 11:13', 'Deut 11:22', 'Deut 19:9', 'Deut 30:16', 'Deut 30:20', 'Deut 30:6'] and len(LEMT('157', books=('Deut',))) == 22
assert P('ושמרת', 'משמרתו') == ['Deut 11:1'] and [(s, x) for s, x, _ in LEMT('4931', books=T) if x == 'משמרתו'] == [('Deut 11:1', 'משמרתו'), ('Num 3:7', 'משמרתו')] and P('משמרתי', 'מצותי', 'חקותי', 'ותורתי') == ['Gen 26:5'] and P('וחקתיו', 'ומשפטיו', 'ומצותיו') == ['Deut 11:1'] and len(P('כל', 'הימים', books=('Deut',))) == 12
assert [(s, x) for s, x, _ in LEMT('4148', books=T)] == [('Deut 11:2', 'מוסר')] and len(LEMT('4148')) == 50 and P('מוסר', 'יהוה') == ['Deut 11:2', 'Prov 3:11'] and [(s, x) for s, x, _ in LEMT('3256', books=('Deut',))] == [('Deut 4:36', 'ליסרך'), ('Deut 8:5', 'ייסר'), ('Deut 8:5', 'מיסרך'), ('Deut 21:18', 'ויסרו'), ('Deut 22:18', 'ויסרו')]   # "DISCIPLINE" THE NOUN — the Torah's ONE seat; "the discipline of the LORD" here and Proverbs 3:11
assert P('ידו', 'החזקה', 'וזרעו', 'הנטויה') == ['Deut 11:2'] and P('ביד', 'חזקה', 'ובזרע', 'נטויה') == ['Deut 26:8', 'Deut 5:15'] and [s for s in U('גדלו') if s.startswith('Deut')] == ['Deut 11:2', 'Deut 5:24'] and 'Deut 3:24' in U('גדלך') and P('אשר', 'לא', 'ידעו', 'ואשר', 'לא', 'ראו') == ['Deut 11:2']
assert P('אתתיו', 'ואת', 'מעשיו') == ['Deut 11:3'] and P('בתוך', 'מצרים') == ['Deut 11:3', 'Exod 11:4'] and P('לפרעה', 'מלך', 'מצרים', 'ולכל', 'ארצו') == ['Deut 11:3'] and P('ולכל', 'ארצו') == ['Deut 11:3', 'Deut 29:1', 'Deut 34:11']
assert P('לחיל', 'מצרים') == ['Deut 11:4'] and P('לסוסיו', 'ולרכבו') == ['Deut 11:4'] and [(s, x, m) for s, x, m in LEMT('6687')] == [('2Kgs 6:6', 'ויצף', 'HC/Vhw3ms'), ('Deut 11:4', 'הציף', 'HVhp3ms'), ('Lam 3:54', 'צפו', 'HVqp3cp')] and P('ים', 'סוף', books=('Deut',)) == ['Deut 11:4', 'Deut 1:40', 'Deut 2:1'] and len(P('ים', 'סוף', books=T)) == 7   # "MADE FLOW" — the hiphil's one seat in the Bible (the axe-head floated, the waters flowed over Lamentations' head)
assert P('מי', 'ים', 'סוף') == ['Deut 11:4', 'Josh 2:10'] and P('ברדפם', 'אחריכם') == ['Deut 11:4'] and 'Num 16:33' in U('ויאבדם', 'ויאבדו', 'ואבדם') and len(P('עד', 'היום', 'הזה', books=('Deut',))) == 6 and len(P('עד', 'היום', 'הזה', books=T)) == 12   # RAHAB reads "the waters of the Red Sea" from this verse (Joshua 2:10 the phrase's other seat)
assert P('עד', 'באכם', 'עד', 'המקום', 'הזה') == ['Deut 11:5', 'Deut 1:31', 'Deut 9:7'] and len(U('במדבר', books=('Deut',))) == 9
assert U('דתן', 'לדתן', 'ודתן') == U('אבירם', 'ולאבירם', 'ואבירם') == ['Deut 11:6', 'Num 16:1', 'Num 16:12', 'Num 16:24', 'Num 16:25', 'Num 16:27', 'Num 26:9', 'Ps 106:17'] and P('בני', 'אליאב') == ['Deut 11:6', 'Num 16:1', 'Num 16:12']   # DATHAN AND ABIRAM never apart — eight seats, always the pair
assert P('פצתה', 'הארץ', 'את', 'פיה') == ['Deut 11:6'] and P('ופצתה', 'האדמה', 'את', 'פיה') == ['Num 16:30'] and P('ותפתח', 'הארץ', 'את', 'פיה') == ['Num 16:32', 'Num 26:10'] and P('ותבלע', 'אתם') == ['Num 16:32', 'Num 26:10'] and 'Exod 15:12' in U('ותבלעם', 'תבלעמו', 'ותבלע', 'ויבלעם')
assert P('ואת', 'בתיהם') == ['Deut 11:6', 'Num 16:32'] and P('ואת', 'אהליהם') == ['Deut 11:6'] and [(s, x) for s, x, _ in LEMT('3351')] == [('Deut 11:6', 'היקום'), ('Gen 7:4', 'היקום'), ('Gen 7:23', 'היקום')] and P('בקרב', 'כל', 'ישראל') == ['Deut 11:6'] and P('אשר', 'ברגליהם') == ['2Kgs 3:9', 'Deut 11:6']   # "EVERY LIVING THING" — THE FLOOD'S WORD, the Bible's three seats: Genesis 7:4, 7:23 and the swallowing
assert P('עיניכם', 'הראת') == ['Deut 11:7', 'Deut 4:3'] and P('עיניך', 'הראת') == ['Deut 3:21'] and P('מעשה', 'יהוה', 'הגדל') == ['Deut 11:7'] and P('כל', 'מעשה', 'יהוה') == ['Deut 11:7', 'Josh 24:31', 'Judg 2:7']
# 11:8-12 THE LAND NOT LIKE EGYPT
assert P('את', 'כל', 'המצוה', books=('Deut',)) == ['Deut 11:22', 'Deut 11:8', 'Deut 15:5', 'Deut 19:9', 'Deut 27:1', 'Deut 5:31', 'Deut 6:25'] and P('למען', 'תחזקו') == ['Deut 11:8', 'Ezra 9:12'] and P('ובאתם', 'וירשתם', 'את', 'הארץ') == ['Deut 11:8', 'Deut 4:1', 'Deut 8:1'] and len(U('לרשתה', books=('Deut',))) == 25 and [s for s in U('לרשתה') if s.startswith('Deut 11:')] == ['Deut 11:10', 'Deut 11:11', 'Deut 11:29', 'Deut 11:8']   # EZRA 9:12 reads "that you may be strong" from this verse
assert P('אשר', 'אתם', 'עברים', 'שמה', 'לרשתה') == ['Deut 11:11', 'Deut 11:8', 'Deut 4:14', 'Deut 6:1'] and len(LEMT('748', books=('Deut',))) == 11 and [(s, x) for s, x, _ in LEMT('748', books=('Deut',)) if s.startswith('Deut 11:')] == [('Deut 11:9', 'תאריכו')]
assert P('על', 'האדמה', 'אשר', 'נשבע', 'יהוה', 'לאבתיכם') == ['Deut 11:21', 'Deut 11:9'] and len(U('לאבתיכם')) == 10 and len(U('לאבתיך', books=('Deut',))) == 11 and len(P('ארץ', 'זבת', 'חלב', 'ודבש')) == 14 and 'Num 16:14' in P('ארץ', 'זבת', 'חלב', 'ודבש') and len(P('זבת', 'חלב', 'ודבש')) == 20 and len(P('זבת', 'חלב', 'ודבש', books=T)) == 15
assert words('Num', 16, 13)[3:7] == ['מארץ', 'זבת', 'חלב', 'ודבש'] and words('Num', 16, 14)[3:7] == ['ארץ', 'זבת', 'חלב', 'ודבש']   # DATHAN AND ABIRAM'S OWN WORDS: the land of milk and honey said of EGYPT (16:13) and denied of Canaan (16:14) — the chapter names them (11:6) and promises it (11:9)
assert P('לא', 'כארץ', 'מצרים') == ['Deut 11:10'] and P('כארץ', 'מצרים') == ['Deut 11:10', 'Gen 13:10'] and P('כגן', 'יהוה', 'כארץ', 'מצרים') == ['Gen 13:10'] and P('כגן', 'הירק') == ['Deut 11:10'] and 'Deut 11:10' in U('הירק', 'ירק', 'וירק', 'כירק') and '1Kgs 21:2' in U('הירק', 'ירק', 'וירק', 'כירק')   # "LIKE THE LAND OF EGYPT" twice in the Bible: Lot's plain "like the garden of the LORD, like the land of Egypt" and this "not like the land of Egypt … like a garden of herbs" (Naboth's vineyard the herb garden's kin)
assert [(s, x) for s, x, _ in LEMT('1588', books=T)][0] == ('Deut 11:10', 'כגן') and len(LEMT('1588', books=T)) == 15 and all(s.startswith('Gen ') for s, _, _ in LEMT('1588', books=T)[1:]) and P('והשקית', 'ברגלך') == ['Deut 11:10'] and P('תזרע', 'את', 'זרעך') == ['Deut 11:10'] and P('אשר', 'יצאתם', 'משם') == ['Deut 11:10']   # "garden" in the Torah: Eden's thirteen, Lot's one, and this — the only garden outside Genesis
assert P('ארץ', 'הרים', 'ובקעת') == ['Deut 11:11'] and P('בבקעה', 'ובהר') == ['Deut 8:7'] and P('למטר', 'השמים', 'תשתה', 'מים') == ['Deut 11:11'] and [(s, x) for s, x, _ in LEMT('4306', books=T)] == [('Deut 11:11', 'למטר'), ('Deut 11:14', 'מטר'), ('Deut 11:17', 'מטר'), ('Deut 28:12', 'מטר'), ('Deut 28:24', 'מטר'), ('Deut 32:2', 'כמטר'), ('Exod 9:33', 'ומטר'), ('Exod 9:34', 'המטר')] and [(s, x) for s, x, _ in LEMT('1653', books=T)] == [('Gen 7:12', 'הגשם'), ('Gen 8:2', 'הגשם'), ('Lev 26:4', 'גשמיכם')]   # THE TWO WORDS FOR RAIN: the flood's and Leviticus's גשם ("rain") three seats; Deuteronomy's מטר ("rain") — six in the book, three in this chapter, Exodus's hail-rain the other two
assert P('תשתה', 'מים') == ['1Kgs 13:9', 'Deut 11:11'] and [(s, x, m) for s, x, m in LEMT('1875', books=('Deut',)) if m == 'HVqrmsa'] == [('Deut 11:12', 'דרש', 'HVqrmsa')] and P('עיני', 'יהוה') == ['Deut 11:12', 'Prov 15:3', 'Prov 22:12', 'Prov 5:21', 'Ps 34:16', 'Zech 4:10'] and U('תמיד', books=('Deut',)) == ['Deut 11:12']   # "ALWAYS" — the book's one seat; "the eyes of the LORD" the Torah's one
assert P('מרשית', 'השנה', 'ועד', 'אחרית', 'שנה') == ['Deut 11:12'] and U('מרשית') == ['Deut 11:12'] and Counter(x for _, x, _ in LEMT('7225'))['ראשית'] == 28 and Counter(x for _, x, _ in LEMT('7225'))['מראשית'] == 4 and PT('Deut', 11, 12, 'מרשית') == ['מֵֽרֵשִׁית'] and P('אחרית', 'שנה') == ['Deut 11:12'] and len(LEMT('319', books=T)) == 10   # מרשית ("from the beginning of") WITHOUT THE ALEPH — the spelling's one seat in the Bible (the shelf's reading at 40:8)
# 11:13-21 THE SECOND PARAGRAPH OF THE SHEMA
assert P('והיה', 'אם', 'שמע', 'תשמעו') == ['Deut 11:13'] and P('והיה', 'אם', 'שמוע', 'תשמע') == ['Deut 28:1'] and P('אם', 'שמוע', 'תשמע') == ['Deut 15:5', 'Deut 28:1', 'Exod 15:26'] and P('אם', 'שמע', 'תשמע') == ['Exod 23:22'] and P('שמוע', 'תשמעו') == ['Exod 19:5']   # the doubled hearing: plural and defective here alone
assert P('אל', 'מצותי') == ['Deut 11:13'] and U('מצותי', books=('Deut',)) == ['Deut 11:13', 'Deut 5:29'] and len(U('מצותי', books=T)) == 9 and P('אשר', 'אנכי', 'מצוה', 'אתכם', 'היום') == ['Deut 11:13', 'Deut 11:27', 'Deut 11:28', 'Deut 27:1', 'Deut 27:4', 'Deut 28:14'] and len(P('אשר', 'אנכי', 'מצוך', 'היום')) == 19   # "MY COMMANDMENTS" in the book: 5:29 inside God's quoted word, 11:13 INSIDE MOSES' OWN SPEECH
assert P('לאהבה', 'את', 'יהוה', 'אלהיכם', 'ולעבדו') == ['Deut 11:13'] and P('בכל', 'לבבכם', 'ובכל', 'נפשכם') == ['Deut 11:13', 'Deut 13:4', 'Josh 22:5', 'Josh 23:14'] and len(P('בכל', 'לבבך', 'ובכל', 'נפשך', books=('Deut',))) == 7
assert P('ונתתי', 'מטר', 'ארצכם', 'בעתו') == ['Deut 11:14'] and U('ונתתי', books=('Deut',)) == ['Deut 11:14', 'Deut 11:15', 'Deut 18:18'] and P('יורה', 'ומלקוש') == ['Deut 11:14'] and len(U('ומלקוש', 'מלקוש', 'למלקוש', 'כמלקוש')) == 8 and P('דגנך', 'ותירשך', 'ויצהרך') == ['Deut 11:14', 'Deut 12:17', 'Deut 7:13'] and P('ואספת', 'דגנך') == ['Deut 11:14'] and P('ונתתי', 'גשמיכם', 'בעתם') == ['Lev 26:4']   # "AND I WILL GIVE" — God's weqatal in the book three times, twice here and once in His quoted word (18:18): the speaker's "I" is God's for two verses
assert P('ונתתי', 'עשב') == ['Deut 11:15'] and len(LEMT('6212', books=T)) == 15 and P('ואכלת', 'ושבעת') == ['Deut 11:15', 'Deut 6:11', 'Deut 8:10'] and P('ואכלו', 'ושבעו') == ['Deut 14:29'] and P('ואכל', 'ושבע') == ['Deut 31:20']
assert P('השמרו', 'לכם') == ['Deut 11:16', 'Deut 4:23', 'Exod 19:12'] and len(P('השמר', 'לך')) == 12 and P('פן', 'יפתה', 'לבבכם') == ['Deut 11:16'] and P('וסרתם', 'ועבדתם', 'אלהים', 'אחרים', 'והשתחויתם', 'להם') == ['Deut 11:16'] and len(P('אלהים', 'אחרים', books=('Deut',))) == 17 and P('והשתחויתם', 'להם') == ['1Kgs 9:6', '2Chr 7:19', 'Deut 11:16', 'Josh 23:16']   # "take heed to yourselves" plural — 4:23's and Sinai's (Exodus 19:12); "and bow down to them" — Solomon's warning and Joshua's farewell the other seats
assert P('וחרה', 'אף', 'יהוה', 'בכם') == ['Deut 11:17', 'Deut 7:4', 'Josh 23:16'] and P('ועצר', 'את', 'השמים') == ['Deut 11:17'] and [(s, x) for s, x, _ in LEMT('6113', books=T)] == [('Deut 11:17', 'ועצר'), ('Deut 32:36', 'עצור'), ('Gen 16:2', 'עצרני'), ('Gen 20:18', 'עצר'), ('Gen 20:18', 'עצר'), ('Num 17:13', 'ותעצר'), ('Num 17:15', 'נעצרה'), ('Num 25:8', 'ותעצר')] and P('ולא', 'יהיה', 'מטר') == ['1Kgs 8:35', '2Chr 6:26', '2Chr 7:13', 'Deut 11:17']   # THE SHUTTING — Abimelech's wombs (Genesis 20:18, the shelf's proof at 306:6), the plagues stayed (Numbers 17, 25); "that there be no rain" SOLOMON'S PRAYER reads back (1 Kings 8:35)
assert P('והאדמה', 'לא', 'תתן', 'את', 'יבולה') == ['Deut 11:17'] and P('ונתנה', 'הארץ', 'יבולה') == ['Lev 26:4'] and P('ולא', 'תתן', 'ארצכם', 'את', 'יבולה') == ['Lev 26:20'] and len(LEMT('2981')) == 13 and P('ואבדתם', 'מהרה', 'מעל', 'הארץ', 'הטבה') == ['Deut 11:17'] and P('ואבדתם', 'מהרה', 'מעל', 'הארץ', 'הטובה') == ['Josh 23:16'] and P('אבד', 'תאבדון', 'מהר') == ['Deut 4:26'] and U('מהרה', books=('Deut',)) == ['Deut 11:17'] and P('אשר', 'יהוה', 'נתן', 'לכם', books=('Deut',)) == ['Deut 11:17']
assert P('ושמתם', 'את', 'דברי', 'אלה') == ['Deut 11:18'] and P('על', 'לבבכם', 'ועל', 'נפשכם') == ['Deut 11:18'] and P('והיו', 'הדברים', 'האלה') == ['Deut 6:6'] and P('וקשרתם', 'אתם', 'לאות', 'על', 'ידכם') == ['Deut 11:18'] and P('וקשרתם', 'לאות', 'על', 'ידך') == ['Deut 6:8'] and P('לאות', 'על', 'ידך') == ['Deut 6:8', 'Exod 13:9'] and P('לאות', 'על', 'ידכה') == ['Exod 13:16'] and U('ידכה') == ['Exod 13:16']
assert [(s, x) for s, x, _ in LEMT('2903')] == [('Deut 6:8', 'לטטפת'), ('Deut 11:18', 'לטוטפת'), ('Exod 13:16', 'ולטוטפת')] and PT('Deut', 11, 18, 'לטוטפת') == ['לְטוֹטָפֹת'] and PT('Deut', 6, 8, 'לטטפת') == ['לְטֹטָפֹת'] and PT('Exod', 13, 16, 'ולטוטפת') == ['וּלְטוֹטָפֹת']   # THE FRONTLETS' THREE SEATS AND THEIR SPELLINGS: 6:8 defective, 11:18 and Exodus 13:16 with the first vav — the shelf's count of four (35:4; Sanhedrin 4b, Menachot 34b) the compile's open row (4b's)
assert P('בין', 'עיניכם') == ['Deut 11:18', 'Deut 14:1'] and P('בין', 'עיניך') == ['Deut 6:8', 'Exod 13:16', 'Exod 13:9']   # "between your eyes" plural: the frontlets here and the baldness of mourning at 14:1
assert P('ולמדתם', 'אתם', 'את', 'בניכם') == ['Deut 11:19'] and P('ושננתם', 'לבניך') == ['Deut 6:7'] and [(s, x, m) for s, x, m in LEMT('3925', books=('Deut',)) if x == 'ולמדתם'] == [('Deut 5:1', 'ולמדתם', 'HC/Vqq2mp'), ('Deut 11:19', 'ולמדתם', 'HC/Vpq2mp')] and P('לדבר', 'בם') == ['Deut 11:19'] and P('ודברת', 'בם') == ['Deut 6:7'] and P('בשבתך', 'בביתך', 'ובלכתך', 'בדרך', 'ובשכבך', 'ובקומך') == ['Deut 11:19', 'Deut 6:7']   # THE SAME CONSONANTS, TWO STEMS: 5:1's "and you shall LEARN them" (qal) and 11:19's "and you shall TEACH them" (piel) — the DB's morphology divides the homograph; 6:7's "repeat" the other verb
assert P('וכתבתם', 'על', 'מזוזות', 'ביתך', 'ובשעריך') == ['Deut 11:20'] and P('וכתבתם', 'על', 'מזוזת', 'ביתך', 'ובשעריך') == ['Deut 6:9'] and [(s, x) for s, x, _ in LEMT('4201', books=('Deut',))] == [('Deut 6:9', 'מזוזת'), ('Deut 11:20', 'מזוזות')] and PT('Deut', 11, 20, 'מזוזות') == ['מְזוּזוֹת'] and len(LEMT('4201')) == 19   # THE DOORPOSTS: 6:9 with one vav, 11:20 with two — the shelf's inclusion after inclusion (36:3) on the pair
assert P('למען', 'ירבו', 'ימיכם') == ['Deut 11:21'] and P('כימי', 'השמים', 'על', 'הארץ') == ['Deut 11:21'] and P('כימי', 'שמים') == ['Ps 89:30'] and P('אשר', 'נשבע', 'יהוה', 'לאבתיכם', 'לתת', 'להם') == ['Deut 11:21', 'Deut 11:9'] and P('נשבע', 'יהוה', 'לאבתיכם') == ['Deut 11:21', 'Deut 11:9', 'Deut 1:8', 'Deut 8:1']
# 11:22-25 THE BORDERS AND THE DREAD
assert P('כי', 'אם', 'שמר', 'תשמרון') == ['Deut 11:22'] and P('שמור', 'תשמרון') == ['Deut 6:17'] and U('תשמרון', books=('Deut',)) == ['Deut 11:22', 'Deut 12:1', 'Deut 6:17', 'Deut 8:1'] and P('את', 'כל', 'המצוה', 'הזאת') == ['Deut 11:22', 'Deut 15:5', 'Deut 19:9', 'Deut 6:25'] and P('ללכת', 'בכל', 'דרכיו') == ['1Kgs 8:58', 'Deut 10:12', 'Deut 11:22'] and P('ולדבקה', 'בו') + P('לדבקה', 'בו') == ['Deut 11:22', 'Deut 30:20', 'Josh 22:5'] and len(LEMT('1692', books=('Deut',))) == 7 and U('לעשתה', books=('Deut',)) == ['Deut 11:22', 'Deut 19:9']
assert P('והוריש', 'יהוה', 'את', 'כל', 'הגוים', 'האלה', 'מלפניכם') == ['Deut 11:23'] and [(s, x) for s, x, m in LEMT('3423', books=('Deut',)) if m and 'Vh' in m] == [('Deut 4:38', 'להוריש'), ('Deut 7:17', 'להורישם'), ('Deut 9:3', 'והורשתם'), ('Deut 9:4', 'מורישם'), ('Deut 9:5', 'מורישם'), ('Deut 11:23', 'והוריש'), ('Deut 18:12', 'מוריש')] and P('גוים', 'גדלים', 'ועצמים', 'מכם') == ['Deut 11:23'] and P('גוים', 'גדלים', 'ועצמים', 'ממך') == ['Deut 4:38', 'Deut 9:1'] and P('רבים', 'ועצומים', 'ממך') == ['Deut 7:1']   # "greater and mightier THAN YOU" — plural here, singular at 4:38 and 9:1 (chapter 7's find on the number)
assert P('כל', 'המקום', 'אשר', 'תדרך', 'כף', 'רגלכם', 'בו') == ['Deut 11:24'] and P('כל', 'מקום', 'אשר', 'תדרך', 'כף', 'רגלכם', 'בו') == ['Josh 1:3'] and words('Josh', 1, 3)[7:] == ['לכם', 'נתתיו', 'כאשר', 'דברתי', 'אל', 'משה'] and P('מן', 'המדבר', 'והלבנון') == ['Deut 11:24'] and P('מהמדבר', 'והלבנון') == ['Josh 1:4']   # JOSHUA 1:3 quotes the verse with the article dropped and ends "AS I SPOKE TO MOSES" — the run's receipt of this verse
assert P('הנהר', 'נהר', 'פרת') == ['Deut 11:24'] and P('הנהר', 'הגדל', 'נהר', 'פרת') == ['Deut 1:7', 'Gen 15:18'] and P('הנהר', 'הגדול', 'נהר', 'פרת') == ['Josh 1:4'] and len(P('נהר', 'פרת')) == 9 and P('הים', 'האחרון') == ['Deut 11:24', 'Deut 34:2', 'Joel 2:20', 'Zech 14:8'] and U('גבלכם', 'גבולכם') == ['Deut 11:24', 'Josh 1:4'] and P('ושתי', 'את', 'גבלך') == ['Exod 23:31']
assert P('לא', 'יתיצב', 'איש', 'בפניכם') == ['Deut 11:25'] and P('לא', 'יתיצב', 'איש', 'בפניך') == ['Deut 7:24'] and P('לא', 'יתיצב', 'איש', 'לפניך') == ['Josh 1:5'] and len(U('יתיצב')) == 8 and P('פחדכם', 'ומוראכם') == ['Deut 11:25'] and P('פחדך', 'ויראתך') == ['Deut 2:25'] and len(P('על', 'פני', 'כל', 'הארץ')) == 11
assert P('כאשר', 'דבר', 'לכם') == ['Deut 11:25', 'Deut 1:11', 'Josh 23:10'] and P('כאשר', 'דבר', 'לך', books=('Deut',)) == ['Deut 12:20', 'Deut 15:6', 'Deut 26:18', 'Deut 29:12'] and len(P('כאשר', 'דבר', books=('Deut',))) == 16 and len(P('כאשר', 'צוה', books=('Deut',))) == 3 and len(P('כאשר', 'צוך', books=('Deut',))) == 3 and len(P('כאשר', 'צוני', books=('Deut',))) == 2   # THE RECEIPT BY "SPOKE": sixteen in the book against eight by "commanded" — the finder's third form (4b's owed item) weighs twice the first two
# 11:26-32 THE BLESSING AND THE CURSE
assert P('ראה', 'אנכי', 'נתן', 'לפניכם', 'היום') == ['Deut 11:26'] and P('ראה', 'נתתי', 'לפניך', 'היום') == ['Deut 30:15'] and P('ברכה', 'וקללה') == ['Deut 11:26'] and P('הברכה', 'והקללה') == ['Deut 30:1', 'Deut 30:19', 'Josh 8:34'] and P('קללה', 'ולא', 'ברכה') == ['Gen 27:12'] and len(LEMT('1293', books=('Deut',))) == 12 and len(LEMT('7045', books=('Deut',))) == 11
assert [(s, x) for s, x, m in LEMT('7200', books=('Deut',)) if m == 'HVqv2ms'] == [('Deut 1:8', 'ראה'), ('Deut 1:21', 'ראה'), ('Deut 2:24', 'ראה'), ('Deut 2:31', 'ראה'), ('Deut 4:5', 'ראה'), ('Deut 11:26', 'ראה'), ('Deut 30:15', 'ראה')] and P('אנכי', 'נתן', 'לפניכם', 'היום') == ['Deut 11:26', 'Deut 11:32', 'Deut 4:8']   # "SEE" the singular imperative seven in the book — at 1:8 and 11:26 over a plural "before you"; the frame "which I set before you today" 4:8, 11:26, 11:32
assert P('את', 'הברכה', 'אשר', 'תשמעו') == ['Deut 11:27'] and P('והקללה', 'אם', 'לא', 'תשמעו') == ['Deut 11:28'] and P('אל', 'מצות', 'יהוה', 'אלהיכם') == ['Deut 11:27', 'Deut 11:28'] and P('וסרתם', 'מן', 'הדרך') == ['Deut 11:28', 'Deut 31:29'] and P('סרו', 'מהר', 'מן', 'הדרך', 'אשר', 'צויתם') == ['Deut 9:12', 'Exod 32:8'] and P('מן', 'הדרך', books=('Deut',)) == ['Deut 11:28', 'Deut 13:6', 'Deut 31:29', 'Deut 9:12', 'Deut 9:16']   # THE CALF'S FORMULA "turned aside from the way" (Exodus 32:8, 9:12, 9:16) said of the curse
assert P('ללכת', 'אחרי', 'אלהים', 'אחרים') == ['Deut 11:28', 'Deut 28:14', 'Judg 2:19'] and P('אלהים', 'אחרים', 'אשר', 'לא', 'ידעתם') == ['Deut 11:28', 'Deut 13:14', 'Deut 13:3', 'Jer 7:9'] and P('אשר', 'לא', 'ידעת', books=('Deut',)) == ['Deut 13:7', 'Deut 28:33', 'Deut 28:36', 'Deut 28:64', 'Deut 8:3'] and P('אשר', 'לא', 'ידעום') == ['Deut 29:25', 'Jer 19:4', 'Jer 44:3', 'Zech 7:14']
assert P('והיה', 'כי', 'יביאך', 'יהוה', 'אלהיך', 'אל', 'הארץ') == ['Deut 11:29', 'Deut 6:10'] and P('כי', 'יביאך', 'יהוה', 'אלהיך') == ['Deut 11:29', 'Deut 6:10', 'Deut 7:1'] and len(P('אשר', 'אתה', 'בא', 'שמה', 'לרשתה')) == 7 and P('ונתתה', 'את', 'הברכה', 'על', 'הר', 'גרזים') == ['Deut 11:29']
assert U('גרזים') == ['Deut 11:29', 'Deut 27:12', 'Josh 8:33', 'Judg 9:7'] and U('עיבל', 'ועיבל') == ['1Chr 1:22', '1Chr 1:40', 'Deut 11:29', 'Deut 27:13', 'Deut 27:4', 'Gen 36:23', 'Josh 8:30', 'Josh 8:33'] and P('הר', 'עיבל') == ['Deut 11:29', 'Josh 8:33'] and P('בהר', 'עיבל') == ['Deut 27:13', 'Deut 27:4', 'Josh 8:30'] and words('Deut', 27, 12)[:3] == ['אלה', 'יעמדו', 'לברך'] and words('Josh', 8, 33)[-10:-6] == ['כאשר', 'צוה', 'משה', 'עבד']   # GERIZIM four seats, EBAL eight — three of them a man (Genesis 36:23's Ebal, the Chronicler's): the homograph for the census; JOSHUA 8:33 "as Moses the servant of the LORD commanded" the run's receipt
assert len(P('בעבר', 'הירדן', books=('Deut',))) == 9 and P('אחרי', 'דרך', 'מבוא', 'השמש') == ['Deut 11:30'] and P('מבוא', 'השמש') == ['Deut 11:30', 'Josh 1:4', 'Josh 23:4', 'Zech 8:7'] and U('מבוא', 'ומבוא', 'למבוא', books=T) == ['Deut 11:30', 'Gen 24:62'] and P('הכנעני', 'הישב', 'בערבה') == ['Deut 11:30'] and U('בערבה', books=('Deut',)) == ['Deut 11:30', 'Deut 1:1', 'Deut 1:7']
assert [s for s in U('הגלגל', 'גלגל', 'הגלגלה', 'בגלגל', 'מהגלגל', 'גלגלה') if s.startswith(('Gen', 'Exod', 'Lev', 'Num', 'Deut'))] == ['Deut 11:30'] and len(U('הגלגל', 'גלגל', 'הגלגלה', 'בגלגל', 'מהגלגל', 'גלגלה')) == 41   # GILGAL — the Torah's ONE seat (forty in the Prophets and Writings)
assert P('אצל', 'אלוני', 'מרה') == ['Deut 11:30'] and P('אלון', 'מורה') == ['Gen 12:6'] and [(s, x) for s, x, _ in LEMT('436')] == [('1Sam 10:3', 'אלון'), ('Deut 11:30', 'אלוני'), ('Gen 12:6', 'אלון'), ('Gen 13:18', 'באלני'), ('Gen 14:13', 'באלני'), ('Gen 18:1', 'באלני'), ('Judg 4:11', 'אלון'), ('Judg 9:6', 'אלון'), ('Judg 9:37', 'אלון')] and lemma_of('Deut', 11, 30, 'מרה') == ['4176'] and lemma_of('Exod', 15, 23, 'מרה') == ['4785'] and 'Exod 15:23' in U('מרה') and len(U('מרה')) == 11   # "THE TEREBINTHS OF MOREH" plural and defective (Genesis 12:6 singular, plene); מרה THE HOMOGRAPH — Moreh here, MARAH the bitter station at Exodus 15:23, "bitter" elsewhere: the DB divides them by lemma
assert P('כי', 'אתם', 'עברים', 'את', 'הירדן') == ['Deut 11:31', 'Num 33:51', 'Num 35:10'] and len(P('אתם', 'עברים', 'את', 'הירדן')) == 7 and P('לבא', 'לרשת', 'את', 'הארץ') == ['Deut 11:31', 'Judg 18:9'] and P('וירשתם', 'אתה', 'וישבתם', 'בה') == ['Deut 11:31'] and P('והורשתם', 'את', 'הארץ', 'וישבתם', 'בה') == ['Num 33:53'] and len(P('אשר', 'יהוה', 'אלהיכם', 'נתן', 'לכם', books=('Deut',))) == 1
assert P('ושמרתם', 'לעשות', 'את', 'כל', 'החקים', 'ואת', 'המשפטים') == ['Deut 11:32'] and P('החקים', 'ואת', 'המשפטים') == ['1Chr 22:13', '2Kgs 17:37', 'Deut 11:32', 'Deut 5:1', 'Deut 7:11', 'Neh 1:7'] and P('החקים', 'והמשפטים') == ['Deut 12:1', 'Deut 6:1', 'Lev 26:46'] and P('ושמרתם', 'לעשות', books=('Deut',)) == ['Deut 11:32', 'Deut 5:32'] and words('Deut', 12, 1)[:6] == ['אלה', 'החקים', 'והמשפטים', 'אשר', 'תשמרון', 'לעשות']   # the chapter's last verse is the next chapter's head — "keep to do the statutes and the judgments" / "these are the statutes and the judgments which you shall keep to do"

# ---- THE COUNTER'S DAY AND THE TWO PARAMETERS (a bare world on the exodus epoch; no clock walk this chapter — no marker, no stretch) ----
with contextlib.redirect_stdout(io.StringIO()):
    _WC = WE.World(era='the counter\'s day — chapter 11 on a bare world (the exodus epoch)', epoch='exodus')
_EX = _WC.clock.eras['exodus']
def DAY(y, m, d): return _WC.clock.day_in('exodus', y, m, d)
def DATE(day): return _EX.date(day)
COUNTER = DAY(40, 11, 1)
RAIN_DATES = WE.CAL_PARAMS['rain_dates']['value']; GERIZIM_EBAL_PLACE = WE.CAL_PARAMS['gerizim_ebal_place']['value']   # THE TWO PARAMETERS read (exercised_by blessing_and_curse) — never a constant in the code
CLOCK = {'counter': DATE(COUNTER), 'rain_dates_keys': sorted(RAIN_DATES), 'place_arms': sorted(GERIZIM_EBAL_PLACE), 'no_marker': True}
assert CLOCK == {'counter': (40, 11, 1), 'rain_dates_keys': ['early_rain', 'fasts_community', 'fasts_individuals', 'late_rain', 'mention_from', 'mention_to', 'request_from_diaspora', 'request_from_land'], 'place_arms': ['r_elazar', 'r_eliezer_ben_yaakov', 'r_yehuda'], 'no_marker': True}, CLOCK
assert RAIN_DATES['late_rain'].startswith('Nisan') and RAIN_DATES['early_rain'].startswith('Marcheshvan') and RAIN_DATES['request_from_land'].startswith('the seventh of Marcheshvan') and GERIZIM_EBAL_PLACE['r_yehuda'].startswith('Shechem'), (RAIN_DATES, GERIZIM_EBAL_PLACE)

# ---- THE ONE DATABASE SCANNED (the holes' ground — nothing names the rain, the heavens shut, the yoke, the blessing-and-curse pair or the ceremony on Israel before this sitting) ----
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
OWN5 = ('rain_in_its_season', 'heavens_shut_for_turning', 'yoke_of_the_commandments_accepted', 'blessing_and_curse_set', 'gerizim_ebal_ceremony_owed')
RAIN_WORDS = r"\b(rain\w*|heavens? shut|shut up the heavens|yoke of the commandments|gerizim|ebal|blessing and (?:the )?curse|rain_in_its_season|heavens_shut_for_turning|yoke_of_the_commandments_accepted|blessing_and_curse_set|gerizim_ebal_ceremony_owed)\b"
_rs = ledger_scan('israel_people', RAIN_WORDS); RAIN_SCAN = None if _rs is None else [e for e in _rs if e not in OWN5]   # this sitting's own five excluded once the fold carries them
_cs = effect_scan('gerizim_ebal_ceremony_owed'); CEREMONY_SCAN = None if _cs is None else [e for e in _cs if e != 'israel_people']
_FXV = yaml.safe_load(open(_os.path.join(HERE, 'effect_vocabulary.yaml'), encoding='utf-8'))['effects']
RAIN_VOCAB = sorted(k for k in _FXV if 'rain' in k)
assert RAIN_SCAN in ([], None), RAIN_SCAN   # THE HOLE'S GROUND — nothing on Israel named the rain, the heavens shut, the yoke, the pair or the ceremony before this sitting (DC4)
assert CEREMONY_SCAN in ([], None), CEREMONY_SCAN   # the ceremony's debit on no other entity
assert 'rain_in_its_season' in RAIN_VOCAB and [k for k in RAIN_VOCAB if k.startswith('rain_')] == ['rain_in_its_season'], RAIN_VOCAB   # the vocabulary's rain effects — this sitting's the one naming the rain of the land (the others the registry's own, read at add_types_ch11.out)

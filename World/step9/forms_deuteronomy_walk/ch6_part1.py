#!/usr/bin/env python3
# DEUTERONOMY 6:1-25 — THE SHEMA: THE CREED AND THE FOUR DUTIES COMPILED FOR THE FIRST TIME, THE TEST AT MASSAH A RUN CITATION BY NAME, THE
# RIGHT AND THE GOOD, AND THE SON'S QUESTION — THE READBACK'S THIRD FORM, A RETELLING INSIDE A LAW (THE DEUTERONOMY WALK sitting 4b, 2026-09-17;
# World/step9/DEUTERONOMY_WALK.md "Sitting 4b"; the state doc's #190-#192). THE CHAPTER'S OWN LINES: no runner held a cell for the recitation, the
# teaching, the tefillin or the mezuzah (the recon over all sixty runners) — F3 compiles the four duties from the ink with the answer sheet Mishnah
# Berakhot 1:1-3:6, 2:2, 9:5, Menachot 3:7, Sotah 7:1, the Sifrei 31-36 and the Talmud's rows as the compile rules; shema_commanded a STATUS on
# Israel at the chapter's own day (40, 11, 1), NO marker (the retrograde stretch of 5:23 ended at 5:32); the test at Massah (6:16) a BLOCK
# test_barred, Massah the tape's own named line (Exodus 17:7) FOUND; THE COMPARTMENTS FOUR A PARAMETER taught by the shelf (the Sifrei 35:3-4;
# Menachot 34b-35a; Sanhedrin 4b:12-14), its derivation from the three spellings reading 11:18 defective where the ink is plene — THE OPEN ROW
# (the DATA row the_spellings), the cell returning the parameter, never a count from the ink; THE RECEIPT WITHOUT THE NAME (6:25 "as He commanded
# us") a RUN CITATION of the charge's line, the register gate's finder BLIND to it (measured, asserted — the finder's third form owed to a gate
# sitting); THE READBACK'S THIRD FORM (T1): "and you shall say to your son" is itself a law's clause — the answer's rows REFERENCE ROWS graded
# against the tape (VERBATIM 3 / EXPANDED 3 / SHORTENED 1), the cell F6 returning its verdict on the answer's form. The daemon law_hear_o_israel
# given_at Deut 6:4, installed_by boot (the two Deuteronomy daemons' form). Six cells; every token probed (zero-report law); effects on every
# cell (the effects law); eighteen DATA rows. Reading ledger: logic/oral_triage/deu_06_vaetchanan_2026-09-17.md (97 sources, 6 claims); the exam's
# docket: logic/oral_triage/deu_06_vaetchanan_exam_2026-09-17.md (747 rows REREAD WHOLE: LAW 346 / DERIVATION 57 / DISPUTE 83 / CONTEXT 261).

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
import cold_run_covenant_at_horeb as CH        # THE EDGE: hear_o_israel -> covenant_at_horeb CALL, reference (the second word's clauses at 6:14-15 — other_gods_barred stands; the charge's line stand_here_commanded — 6:1's reference row, 6:25's receipt)
import cold_run_obey_horeb as OH               # THE EDGE: hear_o_israel -> obey_horeb CALL, reference (the FORGET census — 6:12; the testimonies' header 4:45; 4:29's 'with all your heart'; the readback's second chapter)
import cold_run_decalogue as DC                # THE EDGE: hear_o_israel -> decalogue CALL, reference (the third word's cell — the oath's prohibition beside 6:13's positive clause)
import cold_run_exodus_story as ES             # THE EDGE: hear_o_israel -> exodus_story CALL, reference (the trials' census — Massah; the plagues and the going out read back)
import cold_run_pesach as PE                   # THE EDGE: hear_o_israel -> pesach CALL, reference (the son's question at Exodus 13:14 — the firstborn cell's seat; the sign on the hand at 13:9, 13:16)
import cold_run_opening_speech as OS           # THE EDGE: hear_o_israel -> opening_speech CALL, reference (1:8's oath seats; the frame's write torah_expounded; the readback's first form)
import cold_run_mamre as MA                    # THE EDGE: hear_o_israel -> mamre CALL, reference (the oath's lines sworn_by_himself 22:16-18 and oath_upheld 26:3-5)
import cold_run_joseph as JS                   # THE EDGE: hear_o_israel -> joseph CALL, reference (the oath's third line visitation_promised 50:24)
import cold_run_mekoshesh as MK                # THE EDGE: hear_o_israel -> mekoshesh CALL, reference (the third passage recited — the fringes' verses in its span, REFERENCE)
import cold_run_erection as ER                 # THE EDGE: hear_o_israel -> erection CALL, reference (Exodus 24:12's 'to teach them' — the charge's debit; the covenant's book)

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
by, byp, byl, byw = {}, {}, {}, {}
for _b, _c, _v, _he, _m, _lem, _wt in _rows:
    by.setdefault((_b, _c, _v), []).append((plain(_he), _m)); byp.setdefault((_b, _c, _v), []).append(pointed(_he)); byl.setdefault((_b, _c, _v), []).append((_lem or '').split('/')[-1].strip()); byw.setdefault((_b, _c, _v), []).append(_wt)
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
def W6(v): return words('Deut', 6, v)
def PT(b, c, v, tok): return [NF(x) for x in byp[(b, c, v)] if plain(x) == tok]
def DIFF(a, b_):
    import difflib
    A, B = words(*a), words(*b_)
    return [(op, A[i1:i2], B[j1:j2]) for op, i1, i2, j1, j2 in difflib.SequenceMatcher(None, A, B).get_opcodes() if op != 'equal']
def SHARED(a, b_):
    import difflib
    A, B = words(*a), words(*b_)
    m = difflib.SequenceMatcher(None, A, B).find_longest_match(0, len(A), 0, len(B))
    return A[m.a:m.a + m.size]
def LEN(b, c, v): return len(words(b, c, v))
def verse_text(ch, vs, book='Deut'): return ' '.join(words(book, ch, vs))

P_ = []   # the provenance trail of the case being run
def ink(ref, note):  P_.append(('INK',  'Deut %s — %s' % (ref, note) if not ref[:1].isupper() else '%s — %s' % (ref, note)))
def move(src, note): P_.append(('MOVE', '%s — %s' % (src, note)))
def dat(note):       P_.append(('DATA', note))
def hyp(note):       P_.append(('HYP',  note))     # THE LINK REVIEW LAW: a hypothesis — no teacher; counted apart, never as compiled
def out(verdict, effects):
    """verdict + registry-validated effects (the engine contract)"""
    FX.validate([e for e in effects if e != FX.NONE])
    return verdict, effects, list(P_)

# ---- THE INK, computed (the parser and the tokens; the reading's facts the expectations — every assert PROVEN at the reading, ch6_ink.py) ----
SPAN = [(6, v) for v in range(1, 26)]
PARSED = {(c, v): ink_numbers(verse_words('Deut', c, v)) for (c, v) in SPAN if ink_numbers(verse_words('Deut', c, v))}
def MARKS(c, v): return [t for t in verse_words('Deut', c, v) if t[-1] in '#~^%@|*']
assert PARSED == {(6, 4): [1]} and {(c, v): ink_ordinals(verse_words('Deut', c, v)) for (c, v) in SPAN if ink_ordinals(verse_words('Deut', c, v))} == {} and [((c, v), t) for (c, v) in SPAN for t in MARKS(c, v)] == [((6, 11), 'ושבעת*')], PARSED   # ONE number verse — the creed's word the numeral; no ordinal; NO GAP
assert ink_numbers(verse_words('Zech', 14, 9)) == [1, 1] and ink_numbers(verse_words('Gen', 2, 24)) == [1] and ink_numbers(verse_words('Deut', 17, 6)) == [2, 3, 1] and ink_numbers(verse_words('Deut', 4, 35)) == [] and ink_numbers(verse_words('Exod', 17, 7)) == []
assert lemma_of('Deut', 6, 11, 'ושבעת') == ['7646'] and lemma_of('Deut', 6, 10, 'נשבע') == ['7650'] and lemma_of('Deut', 6, 13, 'תשבע') == ['7650'] and lemma_of('Deut', 6, 4, 'אחד') == ['259'] and wm('Deut', 6, 4) == [('שמע', 'HVqv2ms'), ('ישראל', 'HNp'), ('יהוה', 'HNp'), ('אלהינו', 'HNcmpc/Sp1cp'), ('יהוה', 'HNp'), ('אחד', 'HAcmsa')]
ONE = PARSED[(6, 4)][0]
TOK = sum(len(W6(v)) for v in range(1, 26)); LET = sum(len(x) for v in range(1, 26) for x in W6(v))
assert TOK == 318 and LET == 1295 and {v: len(W6(v)) for v in range(1, 26)} == {1: 17, 2: 23, 3: 20, 4: 6, 5: 10, 6: 9, 7: 10, 8: 8, 9: 5, 10: 21, 11: 19, 12: 12, 13: 8, 14: 9, 15: 16, 16: 8, 17: 10, 18: 17, 19: 8, 20: 14, 21: 11, 22: 11, 23: 13, 24: 18, 25: 15}, TOK
SHEMA_TOK = (sum(len(W6(v)) for v in range(4, 10)), sum(len(x) for v in range(4, 10) for x in W6(v)), sum(len(x) for x in W6(4)))
assert SHEMA_TOK == (48, 205, 25) and Counter(wt for v in range(1, 26) for wt in byw[('Deut', 6, v)]) == Counter({None: 318})   # no written-and-read pair in the chapter
# THE FRAMES AND THE REGISTER: NO divine frame — the whole chapter Moses' voice; ONE "saying" (the son's, 6:20); the narrative verbs only inside the answer
DIV = [(c, v) for (c, v) in SPAN if any(W6(v)[i] in ('ויאמר', 'וידבר') and W6(v)[i + 1] == 'יהוה' for i in range(len(W6(v)) - 1))]
assert DIV == [] and [(c, v) for (c, v) in SPAN if 'לאמר' in W6(v)] == [(6, 20)] and [(c, v) for (c, v) in SPAN if 'משה' in W6(v)] == [] and [v for v in range(1, 26) if 'ישראל' in W6(v)] == [3, 4]
REG = {v: [x for x, m in by[('Deut', 6, v)] if m and re.search(r'^HC/V.w', m)] for v in range(1, 26) if any(m and re.search(r'^HC/V.w', m) for _, m in by[('Deut', 6, v)])}
assert REG == {21: ['ויוציאנו'], 22: ['ויתן'], 24: ['ויצונו']}, REG
CASE_TOK = {f'6:{v}': [x for x in W6(v) if x in ('כי', 'אם', 'ואם', 'או', 'פן')] for v in range(1, 26) if any(x in ('כי', 'אם', 'ואם', 'או', 'פן') for x in W6(v))}
assert CASE_TOK == {'6:10': ['כי'], '6:12': ['פן'], '6:15': ['כי', 'פן'], '6:20': ['כי'], '6:25': ['כי']}, CASE_TOK
NUM2 = {v: (sum(1 for _, m in by[('Deut', 6, v)] if m and '2mp' in m), sum(1 for _, m in by[('Deut', 6, v)] if m and '2ms' in m)) for v in range(1, 26)}
SG_ONLY = [v for v, (p_, s_) in NUM2.items() if s_ and not p_]; PL_ONLY = [v for v, (p_, s_) in NUM2.items() if p_ and not s_]; BOTH = [v for v, (p_, s_) in NUM2.items() if p_ and s_]; NEITHER = [v for v, (p_, s_) in NUM2.items() if not p_ and not s_]
assert SG_ONLY == [2, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 15, 18, 19, 21] and PL_ONLY == [1, 14, 16, 17] and BOTH == [3, 20] and NEITHER == [22, 23, 24, 25], (SG_ONLY, PL_ONLY, BOTH, NEITHER)
ONE_CP = {v: [(x, m) for x, m in by[('Deut', 6, v)] if m and '1cp' in m] for v in range(1, 26) if any(m and '1cp' in m for _, m in by[('Deut', 6, v)])}
assert sorted(ONE_CP) == [4, 20, 21, 22, 23, 24, 25] and ONE_CP[21] == [('היינו', 'HVqp1cp'), ('ויוציאנו', 'HC/Vhw3ms/Sp1cp')] and ONE_CP[25] == [('לנו', 'HR/Sp1cp'), ('נשמר', 'HVqi1cp'), ('אלהינו', 'HNcmpc/Sp1cp'), ('צונו', 'HVpp3ms/Sp1cp')]   # THE ANSWER IN THE FIRST PERSON PLURAL
IMPER = {v: [(x, m) for x, m in by[('Deut', 6, v)] if m and re.match(r'^HV.?.?v', m)] for v in range(1, 26) if any(m and re.match(r'^HV.?.?v', m) for _, m in by[('Deut', 6, v)])}
assert IMPER == {4: [('שמע', 'HVqv2ms')], 12: [('השמר', 'HVNv2ms')]}, IMPER   # TWO IMPERATIVES: hear; take heed
INFA = {v: [(x, m) for x, m in by[('Deut', 6, v)] if m and re.match(r'^HV.a$', m)] for v in range(1, 26) if any(m and re.match(r'^HV.a$', m) for _, m in by[('Deut', 6, v)])}
assert INFA == {17: [('שמור', 'HVqa')]} and [(s_, m) for s_, x, m in LEMT('8104') if x == 'שמור' and m == 'HVqa'] == [('Deut 5:12', 'HVqa'), ('Deut 6:17', 'HVqa'), ('Deut 16:1', 'HVqa')]   # ONE INFINITIVE ABSOLUTE — the book's three
WEQATAL = {v: [x for x, m in by[('Deut', 6, v)] if m and re.search(r'^HC/V.q', m)] for v in range(1, 26) if any(m and re.search(r'^HC/V.q', m) for _, m in by[('Deut', 6, v)])}
assert WEQATAL == {3: ['ושמעת', 'ושמרת'], 5: ['ואהבת'], 6: ['והיו'], 7: ['ושננתם', 'ודברת'], 8: ['וקשרתם', 'והיו'], 9: ['וכתבתם'], 10: ['והיה'], 11: ['ואכלת', 'ושבעת'], 15: ['והשמידך'], 18: ['ועשית', 'ובאת', 'וירשת'], 21: ['ואמרת']}, WEQATAL
YIQ2 = {v: [(x, m) for x, m in by[('Deut', 6, v)] if m and re.search(r'^HV.i2', m)] for v in range(1, 26) if any(m and re.search(r'^HV.i2', m) for _, m in by[('Deut', 6, v)])}
assert YIQ2 == {2: [('תירא', 'HVqi2ms')], 3: [('תרבון', 'HVqi2mp/Sn')], 12: [('תשכח', 'HVqi2ms')], 13: [('תירא', 'HVqi2ms'), ('תעבד', 'HVqi2ms'), ('תשבע', 'HVNi2ms')], 14: [('תלכון', 'HVqi2mp/Sn')], 16: [('תנסו', 'HVpi2mp')], 17: [('תשמרון', 'HVqi2mp/Sn')]}, YIQ2   # the second-person imperfects — fear, serve, swear at 6:13
PROHIB = {v: [(by[('Deut', 6, v)][i + 1][0], by[('Deut', 6, v)][i + 1][1]) for i, (x, _) in enumerate(by[('Deut', 6, v)][:-1]) if x == 'לא' and by[('Deut', 6, v)][i + 1][1] and re.search(r'^HV.i2', by[('Deut', 6, v)][i + 1][1])] for v in range(1, 26)}
PROHIB = {v: l for v, l in PROHIB.items() if l}
assert PROHIB == {14: [('תלכון', 'HVqi2mp/Sn')], 16: [('תנסו', 'HVpi2mp')]}, PROHIB   # TWO PROHIBITIONS, both PLURAL, in a singular chapter
YG_SG = [v for v in range(1, 26) for i in range(len(W6(v)) - 1) if W6(v)[i:i + 2] == ['יהוה', 'אלהיך']]; YG_PL = [v for v in range(1, 26) for i in range(len(W6(v)) - 1) if W6(v)[i:i + 2] == ['יהוה', 'אלהיכם']]; YG_OUR = [v for v in range(1, 26) for i in range(len(W6(v)) - 1) if W6(v)[i:i + 2] == ['יהוה', 'אלהינו']]
assert YG_SG == [2, 5, 10, 13, 15, 15] and YG_PL == [1, 16, 17] and YG_OUR == [4, 20, 24, 25] and len(P('יהוה', 'אלהינו', books=('Deut',))) == 20
NAME = Counter(x for v in range(1, 26) for x in W6(v) if x in ('יהוה', 'ויהוה', 'ביהוה', 'כיהוה', 'ליהוה'))
assert NAME == Counter({'יהוה': 22}) and {v: [x for x in W6(v) if x in ('אלהים', 'האלהים', 'אלהי', 'מאלהי')] for v in range(1, 26) if any(x in ('אלהים', 'האלהים', 'אלהי', 'מאלהי') for x in W6(v))} == {3: ['אלהי'], 14: ['אלהים', 'מאלהי']}
# F1's facts — 6:1-3 THE HEADER: the triad 5:31 / 6:1 / 7:11; "to teach you" 4:14 and 6:1; the land flowing with milk and honey THE BOOK'S FIRST
assert P('וזאת', 'המצוה') == ['Deut 6:1'] and P('ללמד', 'אתכם') == S_('Deut 4:14', 'Deut 6:1') and P('אשר', 'אתם', 'עברים', 'שמה', 'לרשתה') == S_('Deut 11:11', 'Deut 11:8', 'Deut 4:14', 'Deut 6:1')
TRIAD = [(s_, [x for x in words(*[s_.split()[0], *map(int, s_.split()[1].split(':'))]) if x in ('המצוה', 'החקים', 'והחקים', 'והמשפטים', 'המשפטים', 'ואת')]) for s_ in U('המצוה', books=('Deut',)) if s_ in U('והמשפטים', 'המשפטים', books=('Deut',))]
assert TRIAD == [('Deut 5:31', ['המצוה', 'והחקים', 'והמשפטים']), ('Deut 6:1', ['המצוה', 'החקים', 'והמשפטים']), ('Deut 7:11', ['המצוה', 'ואת', 'החקים', 'ואת', 'המשפטים'])], TRIAD
assert P('למען', 'תירא', 'את', 'יהוה', 'אלהיך') == ['Deut 6:2'] and P('אתה', 'ובנך', 'ובן', 'בנך') == ['Deut 6:2'] and P('ובן', 'בנך') == S_('Deut 6:2', 'Exod 10:2') and P('כל', 'ימי', 'חייך') == S_('Deut 16:3', 'Deut 4:9', 'Deut 6:2', 'Gen 3:14', 'Gen 3:17', 'Josh 1:5', 'Ps 128:5')
assert P('ולמען', 'יארכן', 'ימיך') == ['Deut 6:2'] and len(P('אשר', 'אנכי', 'מצוך', 'היום', books=('Deut',))) == 18 and [v for v in range(1, 26) if 'מצוך' in W6(v)] == [2, 6]
assert P('ושמעת', 'ישראל') == ['Deut 6:3'] and P('ושמרת', 'לעשות') == S_('Deut 17:10', 'Deut 6:3') and P('ייטב', 'לך', books=('Deut',)) == S_('Deut 12:25', 'Deut 12:28', 'Deut 22:7', 'Deut 4:40', 'Deut 5:16', 'Deut 6:18', 'Deut 6:3') and P('תרבון', 'מאד') == ['Deut 6:3']
MILK = P('ארץ', 'זבת', 'חלב', 'ודבש', books=T)
assert MILK == S_('Deut 11:9', 'Deut 26:15', 'Deut 26:9', 'Deut 27:3', 'Deut 6:3', 'Exod 13:5', 'Exod 33:3', 'Exod 3:17', 'Exod 3:8', 'Lev 20:24', 'Num 16:14') and P('כאשר', 'דבר', 'יהוה', books=('Deut',)) == S_('Deut 10:9', 'Deut 1:21', 'Deut 27:3', 'Deut 2:1', 'Deut 31:3', 'Deut 6:19', 'Deut 6:3', 'Deut 9:3')
# F2/F3's facts — 6:4-9 THE SHEMA: the four seats of "hear, O Israel"; the two seats of "the LORD one"; the might's ONE seat; the four seats of the sign, the three spellings of the frontlets, the doorposts' one-letter pair
assert P('שמע', 'ישראל') == S_('Deut 20:3', 'Deut 5:1', 'Deut 6:4', 'Deut 9:1') and P('יהוה', 'אחד') == S_('Deut 6:4', 'Zech 14:9') and words('Zech', 14, 9)[-4:] == ['יהוה', 'אחד', 'ושמו', 'אחד']
assert P('ואהבת', 'את', 'יהוה', 'אלהיך') == S_('Deut 11:1', 'Deut 6:5') and U('ואהבת') == S_('Deut 11:1', 'Deut 6:5', 'Jer 31:3', 'Lev 19:18', 'Lev 19:34', 'Mic 6:8')
HEART_SOUL = P('בכל', 'לבבך', 'ובכל', 'נפשך')
assert HEART_SOUL == S_('Deut 10:12', 'Deut 26:16', 'Deut 30:10', 'Deut 30:2', 'Deut 30:6', 'Deut 4:29', 'Deut 6:5') and P('בכל', 'לבבכם', 'ובכל', 'נפשכם') == S_('Deut 11:13', 'Deut 13:4', 'Josh 22:5', 'Josh 23:14')
assert U('מאדך', 'מאדכם', 'ומאדך') == ['Deut 6:5'] and hits('מאדך', exact=False) == ['Deut 6:5']   # "with all your might" — THE BIBLE'S ONE SEAT of the noun with a suffix
assert P('הדברים', 'האלה', books=('Deut',)) == S_('Deut 12:28', 'Deut 30:1', 'Deut 31:1', 'Deut 31:28', 'Deut 32:45', 'Deut 4:30', 'Deut 5:22', 'Deut 6:6') and P('על', 'לבבך') == S_('Deut 6:6', 'Ezek 38:10') and P('על', 'לבבכם') == S_('Deut 11:18', 'Jer 51:50')
assert LEMV('8150') == S_('Deut 32:41', 'Deut 6:7', 'Isa 5:28', 'Prov 25:18', 'Ps 120:4', 'Ps 140:4', 'Ps 45:6', 'Ps 64:4', 'Ps 73:21') and U('ושננתם') == ['Deut 6:7'] and P('ודברת', 'בם') == ['Deut 6:7'] and P('בשבתך', 'בביתך', 'ובלכתך', 'בדרך', 'ובשכבך', 'ובקומך') == S_('Deut 11:19', 'Deut 6:7')
SIGN = [(s_, [x for x in words(*[s_.split()[0], *map(int, s_.split()[1].split(':'))]) if x.startswith('יד')]) for s_ in P('לאות', 'על') if s_ in U('ידך', 'ידכה', 'ידכם')]
assert SIGN == [('Deut 11:18', ['ידכם']), ('Deut 6:8', ['ידך']), ('Exod 13:16', ['ידכה', 'יד']), ('Exod 13:9', ['ידך'])], SIGN
FRONT = [(s_, [x for x in words(*[s_.split()[0], *map(int, s_.split()[1].split(':'))]) if 'טפת' in x and x.startswith(('ל', 'ול'))]) for s_ in S_('Deut 6:8', 'Deut 11:18', 'Exod 13:16')]
assert FRONT == [('Deut 11:18', ['לטוטפת']), ('Deut 6:8', ['לטטפת']), ('Exod 13:16', ['ולטוטפת'])] and sorted(hits('טטפת', exact=False) + hits('טוטפת', exact=False)) == S_('Deut 6:8', 'Deut 11:18', 'Exod 13:16'), FRONT   # THE THREE SPELLINGS — 11:18 PLENE in the ink
assert P('בין', 'עיניך') + P('בין', 'עיניכם') == ['Deut 6:8', 'Exod 13:16', 'Exod 13:9', 'Deut 11:18', 'Deut 14:1'] and U('וכתבתם') == S_('Deut 11:20', 'Deut 6:9') and len(U('מזוזת', 'מזזות', 'מזוזות', 'המזוזת', 'המזוזות')) == 13 and U('ובשעריך') == S_('Deut 11:20', 'Deut 6:9')
assert P('וכתבתם', 'על', 'מזוזת', 'ביתך', 'ובשעריך') == ['Deut 6:9'] and words('Deut', 11, 20)[2] == 'מזוזות' and DIFF(('Deut', 6, 9), ('Deut', 11, 20)) == [('replace', ['מזוזת'], ['מזוזות'])]
# F4's facts — 6:10-15 THE GIFT AND THE WARNING: the oath's seats; the list's two retellings; the forgetting; fear, serve, swear (10:20 the pair); the plural prohibition; the jealous God
OATH_SEATS = P('אשר', 'נשבע', 'לאבתיך', books=('Deut',))
assert OATH_SEATS == S_('Deut 6:10', 'Deut 7:12', 'Deut 7:13', 'Deut 8:18') and len(P('לאברהם', 'ליצחק', 'וליעקב')) == 11 and P('נשבע', 'לאבתינו') == ['Deut 6:23'] and len(U('נשבע', books=('Deut',))) == 22 and [v for v in range(1, 26) if 'נשבע' in W6(v)] == [10, 18, 23]
assert P('ערים', 'גדלת', 'וטבת') == ['Deut 6:10'] and P('ובתים', 'מלאים', 'כל', 'טוב') == ['Deut 6:11'] and P('וברת', 'חצובים') == ['Deut 6:11'] and P('כרמים', 'וזיתים') == S_('Deut 6:11', 'Josh 24:13', 'Neh 9:25') and P('ואכלת', 'ושבעת') == S_('Deut 11:15', 'Deut 6:11', 'Deut 8:10')
FORGET_SEATS = P('השמר', 'לך', 'פן', 'תשכח')
assert FORGET_SEATS == S_('Deut 6:12', 'Deut 8:11') and [s_ for s_ in P('מבית', 'עבדים') if s_ in U('הוציאך', 'הוצאתיך', 'המוציאך')] == S_('Deut 13:11', 'Deut 5:6', 'Deut 6:12', 'Deut 8:14', 'Exod 20:2') and len(P('בית', 'עבדים') + P('מבית', 'עבדים')) == 12
assert P('את', 'יהוה', 'אלהיך', 'תירא') == S_('Deut 10:20', 'Deut 6:13') and P('ובשמו', 'תשבע') == S_('Deut 10:20', 'Deut 6:13') and P('ואתו', 'תעבד') + P('אתו', 'תעבד') == ['Deut 6:13', 'Deut 10:20'] and DIFF(('Deut', 6, 13), ('Deut', 10, 20)) == [('replace', ['ואתו'], ['אתו']), ('insert', [], ['ובו', 'תדבק'])]
assert len(P('אחרי', 'אלהים', 'אחרים')) == 16 and P('אחרי', 'אלהים', 'אחרים', books=('Deut',)) == S_('Deut 11:28', 'Deut 13:3', 'Deut 28:14', 'Deut 6:14', 'Deut 8:19') and P('לא', 'תלכון') == S_('Deut 6:14', 'Isa 52:12') and P('מאלהי', 'העמים', 'אשר', 'סביבותיכם') == ['Deut 6:14']
JEALOUS = P('אל', 'קנא')
assert JEALOUS == S_('Deut 4:24', 'Deut 5:9', 'Deut 6:15', 'Exod 20:5', 'Exod 34:14') and len(U('בקרבך', books=('Deut',))) == 11 and P('פן', 'יחרה', 'אף', 'יהוה') == ['Deut 6:15'] and P('והשמידך', 'מעל', 'פני', 'האדמה') == ['Deut 6:15'] and len(P('מעל', 'פני', 'האדמה')) == 13 and 'Gen 6:7' in P('מעל', 'פני', 'האדמה')
# F5's facts — 6:16-19 MASSAH, KEEP, THE RIGHT AND THE GOOD: "you shall not test" three seats; Massah four; the test lemma's fourteen Torah seats; the testimonies' three Deuteronomy seats; "the right and the good" the pair 6:18 / 12:28
assert U('תנסו', 'תנסה', 'תנסון') == S_('Deut 6:16', 'Exod 17:2', 'Isa 30:17') and U('מסה', 'במסה', 'ומסה', 'המסה') == S_('Deut 33:8', 'Deut 6:16', 'Exod 17:7', 'Ps 95:8') and U('נסיתם', 'נסיתו', 'נסיתי') == S_('1Sam 17:39', 'Deut 33:8', 'Deut 6:16', 'Eccl 7:23')
TEST_LEM = LEMV('5254', books=T)
assert TEST_LEM == S_('Deut 13:4', 'Deut 28:56', 'Deut 33:8', 'Deut 4:34', 'Deut 6:16', 'Deut 8:16', 'Deut 8:2', 'Exod 15:25', 'Exod 16:4', 'Exod 17:2', 'Exod 17:7', 'Exod 20:20', 'Gen 22:1', 'Num 14:22') and words('Exod', 17, 7)[:4] == ['ויקרא', 'שם', 'המקום', 'מסה'] and words('Num', 14, 22)[-4:-1] == ['פעמים', 'ולא', 'שמעו']   # typed from the print
assert P('שמור', 'תשמרון') == ['Deut 6:17'] and P('ועדתיו', 'וחקיו') == ['Deut 6:17'] and P('העדת', 'והחקים', 'והמשפטים') == S_('Deut 4:45', 'Deut 6:20') and [s_ for s_ in U('עדת', 'העדת', 'עדתיו', 'ועדתיו', 'עדותיו', 'ועדותיו', books=T) if s_.startswith('Deut')] == S_('Deut 4:45', 'Deut 6:17', 'Deut 6:20')
assert P('ועשית', 'הישר', 'והטוב') == ['Deut 6:18'] and P('הישר', 'והטוב') + P('הטוב', 'והישר') == ['Deut 6:18', '2Chr 14:1', '2Chr 31:20', '2Kgs 10:3', 'Deut 12:28'] and P('הישר', 'בעיני', 'יהוה', books=T) == S_('Deut 12:25', 'Deut 13:19', 'Deut 21:9')
assert P('להדף', 'את', 'כל', 'איביך') == ['Deut 6:19'] and LEMV('1920') == S_('2Kgs 4:27', 'Deut 6:19', 'Deut 9:4', 'Ezek 34:21', 'Isa 22:19', 'Jer 46:15', 'Job 18:18', 'Josh 23:5', 'Num 35:20', 'Num 35:22', 'Prov 10:3')
# F6's facts — 6:20-25 THE SON'S QUESTION AND THE ANSWER: 6:20 = Exodus 13:14 verbatim to "saying"; the answer's seats; "as He commanded us" 6:25 and Ezra 4:3 — the receipt WITHOUT THE NAME
assert P('כי', 'ישאלך', 'בנך', 'מחר') == S_('Deut 6:20', 'Exod 13:14') and DIFF(('Deut', 6, 20), ('Exod', 13, 14))[0] == ('insert', [], ['והיה']) and words('Exod', 13, 14)[1:6] == ['כי', 'ישאלך', 'בנך', 'מחר', 'לאמר'] and W6(20)[:5] == ['כי', 'ישאלך', 'בנך', 'מחר', 'לאמר']
ASKINGS = [s_ for s_ in U('מחר') if s_ in U('ישאלך', 'ישאלון', 'ישאלו', 'בניכם', 'בנך')]
assert ASKINGS == S_('2Kgs 6:28', 'Deut 6:20', 'Exod 13:14', 'Josh 22:24', 'Josh 22:27', 'Josh 4:21', 'Josh 4:6') and len(P('מה', 'זאת')) == 10 and P('מה', 'העדת') == ['Deut 6:20'] and words('Exod', 12, 26)[:5] == ['והיה', 'כי', 'יאמרו', 'אליכם', 'בניכם'] and words('Exod', 13, 8)[:2] == ['והגדת', 'לבנך']
assert P('ואמרת', 'לבנך') == ['Deut 6:21'] and P('והגדת', 'לבנך') == ['Exod 13:8'] and P('עבדים', 'היינו', 'לפרעה') == ['Deut 6:21'] and P('ביד', 'חזקה', books=T) == S_('Deut 26:8', 'Deut 5:15', 'Deut 6:21', 'Deut 7:8', 'Deut 9:26', 'Exod 13:9', 'Exod 3:19', 'Exod 6:1')
assert [s_ for s_ in U('אתת', 'אותת', 'ואתת') if s_ in U('ומפתים', 'ומופתים', 'ובמפתים', 'ובמופתים')] == S_('Deut 6:22', 'Neh 9:10') and W6(22)[2:4] == ['אותת', 'ומפתים'] and P('גדלים', 'ורעים') == ['Deut 6:22'] and U('לעינינו') == S_('Deut 6:22', 'Josh 24:17', 'Ps 79:10')
assert P('ואותנו', 'הוציא', 'משם') == ['Deut 6:23'] and P('הביא', 'אתנו', 'לתת', 'לנו') == ['Deut 6:23'] and P('ויצונו', 'יהוה') == ['Deut 6:24'] and P('ליראה', 'את', 'יהוה', 'אלהינו') == ['Deut 6:24'] and P('לטוב', 'לנו', 'כל', 'הימים') == ['Deut 6:24']
assert P('לחיתנו', 'כהיום', 'הזה') == ['Deut 6:24'] and P('כהיום', 'הזה') == S_('Deut 6:24', 'Ezra 9:15', 'Ezra 9:7', 'Gen 39:11', 'Jer 44:22', 'Neh 9:10')
RECEIPT_NO_NAME = P('כאשר', 'צונו')
assert P('וצדקה', 'תהיה', 'לנו') == ['Deut 6:25'] and U('צדקה', 'וצדקה', 'לצדקה', 'צדקתך', 'ובצדקתך', 'בצדקתי', 'בצדקתך', books=T) == S_('Deut 24:13', 'Deut 6:25', 'Deut 9:4', 'Deut 9:5', 'Deut 9:6', 'Gen 15:6', 'Gen 18:19', 'Gen 38:26') and RECEIPT_NO_NAME == S_('Deut 6:25', 'Ezra 4:3') and P('כל', 'המצוה', 'הזאת') == S_('Deut 11:22', 'Deut 15:5', 'Deut 19:9', 'Deut 6:25')
assert P('כאשר', 'צוה', 'יהוה') and 'Deut 6:25' not in P('כאשר', 'צוה', 'יהוה') and [v for v in range(1, 26) if 'צונו' in W6(v)] == [25] and morphs('Deut', 6, 25)[-1] == 'HVpp3ms/Sp1cp'   # the receipt's finder scans "as commanded the LORD" — 6:25 carries the suffix and no Name
# THE TAPE'S FIRST TELLINGS the answer retells (the ink of the seats the readback names — the tape's lines are found on the running world at CO3/CO4/CO8)
assert words('Exod', 12, 51)[:6] == ['ויהי', 'בעצם', 'היום', 'הזה', 'הוציא', 'יהוה'] and words('Exod', 7, 20)[:2] == ['ויעשו', 'כן'] and words('Exod', 12, 29)[:3] == ['ויהי', 'בחצי', 'הלילה'] and words('Gen', 22, 16)[:2] == ['ויאמר', 'בי'] and words('Gen', 26, 3)[:3] == ['גור', 'בארץ', 'הזאת'] and words('Gen', 50, 24)[:3] == ['ויאמר', 'יוסף', 'אל']
assert words('Exod', 17, 2)[:3] == ['וירב', 'העם', 'עם'] and words('Exod', 17, 6)[:2] == ['הנני', 'עמד'] and words('Deut', 5, 28)[:3] == ['וישמע', 'יהוה', 'את'] and words('Deut', 5, 31)[-1] == 'לרשתה' and words('Deut', 4, 10)[:2] == ['יום', 'אשר']
# THE RETELLINGS' DELTAS RECOMPUTED (the narrative rows' measures — the token counts and the longest shared run, from the DB)
HEADER_DELTA = (LEN('Deut', 6, 1), LEN('Deut', 5, 31), len(SHARED(('Deut', 6, 1), ('Deut', 5, 31))))
MASSAH_DELTA = (LEN('Deut', 6, 16), LEN('Exod', 17, 7), len(SHARED(('Deut', 6, 16), ('Exod', 17, 7))), LEN('Exod', 17, 2))
OUT_DELTA = (LEN('Deut', 6, 21), LEN('Exod', 12, 51), len(SHARED(('Deut', 6, 21), ('Exod', 12, 51))), len(SHARED(('Deut', 6, 21), ('Exod', 13, 9))))
PLAGUE_DELTA = (LEN('Deut', 6, 22), sum(LEN('Exod', c, v) for c, v in ((7, 20), (8, 2), (8, 13), (8, 20), (9, 6), (9, 10), (9, 23), (10, 13), (10, 22), (12, 29))))
OATH_DELTA = (LEN('Deut', 6, 23), sum(LEN('Gen', 22, v) for v in (16, 17, 18)), sum(LEN('Gen', 26, v) for v in (3, 4, 5)), LEN('Gen', 50, 24), len(SHARED(('Deut', 6, 23), ('Gen', 50, 24))))
CHARGE_DELTA = (LEN('Deut', 6, 24), LEN('Deut', 5, 31), len(SHARED(('Deut', 6, 24), ('Deut', 5, 31))), LEN('Deut', 6, 25), len(SHARED(('Deut', 6, 25), ('Deut', 5, 31))))
assert HEADER_DELTA == (17, 20, 2) and MASSAH_DELTA == (8, 19, 2, 19) and OUT_DELTA == (11, 13, 1, 2) and PLAGUE_DELTA == (11, 190) and OATH_DELTA == (13, 46, 47, 22, 3) and CHARGE_DELTA == (18, 20, 2, 15, 3), (HEADER_DELTA, MASSAH_DELTA, OUT_DELTA, PLAGUE_DELTA, OATH_DELTA, CHARGE_DELTA)   # typed from the fast checker's print

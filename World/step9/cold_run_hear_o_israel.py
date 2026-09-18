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
assert GUARDED == 42, ("the guard counted %d expectations, the tripwire holds 42" % GUARDED)   # the cells' asks summed by the generator before the first graded run (F1 F1)
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

# ---- THE READBACK'S THIRD FORM — A RETELLING INSIDE A LAW (T1): "and you shall say to your son" (6:21) is itself a law's clause; the answer's five rows,
# the header's one and the test's one are REFERENCE ROWS graded against the tape (never a second act, R1); the cell F6 returns its verdict on the answer's form ----
GRADES = ('VERBATIM', 'VARIANT', 'TURNED', 'SHORTENED', 'EXPANDED', 'SUPPLIED', 'DISAGREES')
def rb(verses, told, tape_kind, tape_verse, entry, grade, why, open_=False, law=False, cell=None):
    assert grade in GRADES, grade
    return {'verses': verses, 'told': told, 'tape_kind': tape_kind, 'tape_verse': tape_verse, 'entry': entry, 'grade': grade, 'why': why, 'open': open_, 'law': law, 'cell': cell}
READBACK = [
    rb('Deut 6:1', "and this is the commandment, the statutes and the judgments which the LORD your God commanded to teach you, to do them in the land which you are crossing over to possess", 'stand_here_commanded', 'Deut 5:28', "commanded on moses valued teach_the_commandment — the charge 'all the commandment and the statutes and the judgments which you shall teach them' (5:31), CLOSED by the prior run (Deut 1:5)", 'VERBATIM', "THE CHARGE EXECUTED — the triad's three seats 5:31 / 6:1 / 7:11 (computed: seventeen tokens against 5:31's twenty, two shared); 'to teach you' 4:14's and 6:1's; the header opens the charge's fulfilment, no write (the debit's close by the prior run unmoved — CO7); the frame R6", law=True, cell='F1 the_header (this runner); CH.the_answer_and_the_charge by CALL'),
    rb('Deut 6:16', "you shall not test the LORD your God, as you tested him at Massah", 'named', 'Exod 17:7', "named — the-place-rephidim 'Massah and Meribah' by Moses (17:7); murmured at 17:2-3 ('give us water'), rock_struck at 17:6", 'VERBATIM', "A RUN CITATION BY NAME: the tape's own named line (eight tokens against 17:7's nineteen, two shared — 'Massah' the name the tape wrote); the trials counted ten on the shelf (Arakhin 15a — 'two at the water': Marah and Rephidim; ES.trials by CALL); the block test_barred written at this line (CO3)", law=True, cell='F5 the_test_and_the_right (this runner); ES.trials by CALL'),
    rb('Deut 6:21', "and you shall say to your son: we were slaves to Pharaoh in Egypt, and the LORD brought us out of Egypt with a strong hand", 'brought_out', 'Exod 12:51', "brought_out — israel (12:51 'the LORD brought out the sons of Israel'; the closes sent_to_pharaoh on moses, to_be_brought_out on israel)", 'EXPANDED', "the going out in the first person plural (eleven tokens against 12:51's thirteen, one shared) with 'WITH A STRONG HAND' added — 13:9's own ink (the passover's 'for with a strong hand the LORD brought you out'; two shared with 13:9); 'we were slaves to Pharaoh' the Bible's one seat — the Haggadah's opening (Mishnah Pesachim 10:4 'he begins with disgrace')", law=True, cell='F6 the_sons_question (this runner); PE.firstborn by CALL'),
    rb('Deut 6:22', "and the LORD gave signs and wonders, great and grievous, upon Egypt, upon Pharaoh and upon all his house, before our eyes", 'plague_struck', 'Exod 7:20', "plague_struck on egypt_people TEN — blood, frogs, lice, swarms, pestilence, boils, hail, locusts, darkness, the_firstborn (Exodus 7:20 to 12:29; four closed by their removals)", 'SHORTENED', "TEN LINES TO ONE CLAUSE — eleven tokens for the ten lines' hundred and ninety (computed): 'signs and wonders' the pairing of 6:22 and Nehemiah 9:10 alone (6:22's 'signs' plene); 'great and grievous' one seat; 'all his house' — Onkelos 'all the MEN of his house' supplied; 'before our eyes' 6:22, Joshua 24:17, Psalm 79:10", law=True, cell='F6 the_sons_question (this runner); ES.plagues by REFERENCE'),
    rb('Deut 6:23', "and us he brought out from there, that he might bring us in, to give us the land which he swore to our fathers", 'sworn_by_himself', 'Gen 22:16', "sworn_by_himself — abraham (22:16-18 'by myself I have sworn'); oath_upheld — isaac (26:3-5); visitation_promised — joseph to the sons (50:24 'the land which he swore to Abraham, to Isaac and to Jacob')", 'EXPANDED', "THE PURPOSE CLAUSE ADDED — 'that he might bring us in, to give us the land' (thirteen tokens; the oath's three lines forty-six, forty-seven and twenty-one; three shared with 50:24 — the three names' first joint telling on the tape); 'swore to OUR fathers' the one seat (the answer's plural), 6:10 and 6:18's 'to your fathers' the chapter's other two; the RUN_CITATION pointers at Deut 6:10 / 6:18 / 6:23 name the three lines (MA and JS by CALL)", law=True, cell='F6 the_sons_question (this runner); MA.moriah, MA.isaac_gerar, JS.the_oath by CALL'),
    rb('Deut 6:24', "and the LORD commanded us to do all these statutes, to fear the LORD our God, for our good always, to keep us alive as at this day", 'ten_words_declared', 'Deut 4:10', "covenant_declared on israel_people dated (1, 3, 7) — the giving (2b's supplied line at Deut 4:10-13); stand_here_commanded (5:28-31) the charge's line — 'all the commandment and the statutes and the judgments'", 'EXPANDED', "THE THREE PURPOSE CLAUSES ADDED — 'to fear the LORD our God, for our good always, to keep us alive as at this day' (eighteen tokens against 5:31's twenty, two shared; 'for our good always' and 'to keep us alive' the Bible's one seats each); 'and the LORD commanded us' the answer's third narrative verb (6:21, 6:22, 6:24 — the retold exodus); the ten words the giving the son is told of (4:10-13 FOUND, CO4)", law=True, cell='F6 the_sons_question (this runner); OS.the_frame by CALL'),
    rb('Deut 6:25', "and it shall be righteousness for us, if we observe to do all this commandment before the LORD our God, AS HE COMMANDED US", 'stand_here_commanded', 'Deut 5:28', "commanded on moses valued teach_the_commandment — 'all the commandment' (5:31) the referent; the giving's ten_words_declared the second", 'VERBATIM', "THE RECEIPT WITHOUT THE NAME — 'as he commanded us' (6:25; Ezra 4:3 the one other seat): a RUN CITATION of the charge's line (5:31 'all the commandment … which you shall teach them'; 'all this commandment' four seats), VERBATIM in kind; the register gate's finder scans 'as commanded the LORD' and is BLIND to the suffixed form without the Name (measured, CO6) — the pointer RUN_CITATION at Deut 6:25 on file, the finder's third form owed to a gate sitting; 'righteousness for us' Genesis 15:6's kin and 24:13's 'it shall be righteousness for you' (Onkelos 'merit' at both)", law=True, cell='F6 the_sons_question (this runner); CH.the_answer_and_the_charge by CALL'),
]
RB_GRADES = collections.Counter(r['grade'] for r in READBACK)
assert len(READBACK) == 7 and RB_GRADES == collections.Counter({'VERBATIM': 3, 'EXPANDED': 3, 'SHORTENED': 1}) and not any(r['open'] for r in READBACK) and all(r['law'] for r in READBACK), (len(READBACK), RB_GRADES)

DATA = {
    'the_readback': {'value': READBACK, 'settings': {'the_third_form': "THE_LOOP.md step 6's third form (T1, THE DEUTERONOMY WALK 4b, 2026-09-17): a retelling INSIDE A LAW — 'and you shall say to your son' (6:21) is a law's clause, so the answer's rows are REFERENCE ROWS graded against the tape (R1 — never a second act) AND the cell that compiles the duty to answer returns its verdict on the answer's form; SEVEN rows — the answer's five (6:21-25), the header's (6:1), the test's (6:16): VERBATIM 3 / EXPANDED 3 / SHORTENED 1; every row's entry FOUND on the running world by kind and first verse (CO4); no row OPEN; the deltas recomputed from the DB", 'the_first_two_forms': "the first form (1b — the speech against the tape, R1-R6) and the laws' form (3b — the code's second copy against the cells, L1-L6) both hold here; the new rule T1 alone", 'the_four_askings': "Exodus 12:26 (the sons, 'what is this service to you'), 13:8 ('you shall tell your son' — no asking), 13:14 ('when your son asks you tomorrow: what is this'), 6:20 ('what are the testimonies and the statutes and the judgments') — the four sons of Pesachim 116a-b (the wise 6:20, the wicked 12:26, the simple 13:14, the one who cannot ask 13:8; Mishnah Pesachim 10:4 'according to the son's understanding')"}},
    'the_large_letters': {'value': {'deut_6_4': ['ayin of hear', 'dalet of one'], 'lev_11_42': 'vav of belly', 'num_27_5': 'nun of their case', 'store': 'DROPPED — the store reads shm for hear and ach for one'}, 'settings': {'parked': "the owner's word (2026-09-17): a HYPOTHESIS of a second channel of the program (a count check, a halt, an attestation) measured by large_letter_probes.py (6/6) and PARKED — no edge, no work; Kiddushin 30a:11's three middles diverge from the text's count (the docket's row)"}},
    'the_spellings': {'value': {'deut_6_8': 'לטטפת (defective — "for frontlets", the two waws absent)', 'deut_11_18': 'לטוטפת (PLENE in the ink — "for frontlets", one waw)', 'exod_13_16': 'ולטוטפת (plene — "and for frontlets")', 'the_shelf_count': '1 + 1 + 2 = 4 — reads 11:18 DEFECTIVE', 'the_ink': "11:18 plene: the shelf's count does not run on the store — THE OPEN ROW"}, 'settings': {'the_compartments': "FOUR a PARAMETER taught by the shelf — the Sifrei 35:3-4 ('frontlets, frontlets, frontlets — four'), Menachot 34b:12-35a:2 (R. Yishmael: tat in Katpi is two, pat in Afriki is two; R. Akiva: the three spellings), Sanhedrin 4b:12-14 (THE PRINCIPLE — the vocalization against the written tradition: R. Yishmael's academy reads the count from the written form), Zevachim 37b: the cell returns the parameter, never a count from the ink", 'recorded': "RESEARCH_LOG 2026-09-17 — recorded at the reading, not resolved; the cell's DATA row names the divergence; the hand's ONE compartment from 'a sign' singular (the Sifrei 35:3; Menachot 34b:7)"}},
    'the_two_sets': {'value': {'recited': ['Deut 6:4-9', 'Deut 11:13-21', 'Num 15:37-41'], 'bound': ['Exod 13:1-10', 'Exod 13:11-16', 'Deut 6:4-9', 'Deut 11:13-21'], 'in_both': ['Deut 6:4-9', 'Deut 11:13-21'], 'recited_not_bound': ['Num 15:37-41'], 'bound_not_recited': ['Exod 13:1-10', 'Exod 13:11-16'], 'in_neither': 'the ten words'}, 'settings': {'the_sifrei': "34:2-3 — 'these words': the fringes recited though not bound, Exodus 13's passages bound though not recited (they speak of the going out, not of the yoke); the ten words in neither — read daily by the priests in the Temple and abolished for the heretics' grievance (Berakhot 12a, credited from 3b)", 'menachot_3_7': "'the four passages in the tefillin invalidate each other — even one letter invalidates' (the answer sheet's row)"}},
    'the_recitation_times': {'value': {'evening_from': 'when the priests enter to eat their terumah (the stars)', 'evening_until': {'r_eliezer': 'the end of the first watch', 'the_sages': 'midnight', 'rabban_gamliel': 'the dawn'}, 'morning_from': 'when one distinguishes blue from white (R. Eliezer: blue from leek-green)', 'morning_until': {'r_eliezer': 'sunrise', 'r_yehoshua': 'three hours'}}, 'settings': {'the_ink': "'when you lie down and when you rise up' (6:7; 11:19) — the TIMES of lying and rising, not the postures (Hillel, Mishnah Berakhot 1:3)", 'mishnah_berakhot_1_1_2': "the evening from the priests' entering (Berakhot 2a-2b — the stars, from Nehemiah 4:15 by the Gemara), until the first watch / midnight / dawn — the sages' fence 'to keep a man far from transgression' (Rabban Gamliel's sons from the wedding, 1:1); the morning from blue against white until sunrise / three hours — 'the way of kings to rise at three hours' (1:2)", 'the_exam_person': "the priest entering to eat his terumah — the evening's time begins (ACCEPTED)"}},
    'the_postures': {'value': {'beit_shammai': 'evening reclining, morning standing — by the letter of "when you lie down and when you rise up"', 'beit_hillel': 'every man in his way — "when you walk by the way"', 'the_time_reading': "'when you lie down' the TIME of lying, 'when you rise' the time of rising (Hillel)"}, 'settings': {'mishnah_berakhot_1_3': "R. Tarfon reclined by the road as Beit Shammai and was endangered by robbers — 'you deserved to lose your life, for you transgressed the words of Beit Hillel' (1:3; Berakhot 10b-11a); the Sifrei 34:9-10 the same dispute on the spine", 'the_exam_person': "the reader reclining by the road — Hillel's way holds, the letter's reading refused (ACCEPTED)"}},
    'the_exemptions': {'value': {'the_mourner': 'exempt — one whose dead lies before him (3:1)', 'the_bridegroom': "exempt the first night until the Sabbath's end if he did not act (2:5); Rabban Gamliel recited (2:5); not everyone may take the name (2:8)", 'women_slaves_minors': 'exempt from the Shema and the tefillin; obligated in prayer, the mezuzah and the grace (3:3)', 'the_daughters': "'your sons' — not your daughters (Kiddushin 29b; 34a:3 the exemption from Torah study by 6:7)", 'the_one_who_did_not_hear': "R. Yose: did not fulfil — 'HEAR' (2:3; the Sifrei 31:7); the sages: fulfilled (Berakhot 15a-15b)", 'any_language': "Sotah 7:1 — 'HEAR': in any language you hear (Berakhot 13a)", 'intention': "2:1 — reading in the Torah at the time, with intent fulfilled; the first verse needs intent (Berakhot 13a-13b)"}, 'settings': {'mishnah_berakhot_2_1_3_6': "the answer sheet's rows on who recites and how; the laborers recite in the tree and on the wall (2:4); the bath and the emission (3:4-6) the other engine's", 'the_exam_persons': "the bridegroom EXEMPT (2:5; Berakhot 16a); the daughter EXEMPT from the teaching (Kiddushin 29b, 34a:3 — a whole-row find of 2026-09-17)"}},
    'the_passages_order': {'value': ['Deut 6:4-9 — the yoke of heaven first', 'Deut 11:13-21 — the yoke of the commandments', 'Num 15:37-41 — by day alone'], 'settings': {'mishnah_berakhot_2_2': "R. Yehoshua ben Korcha: why does 'hear' precede 'and it shall come to pass'? that one accept the yoke of heaven first and the yoke of the commandments after; 'and it shall come to pass' before 'and the LORD said' — the one by day and night, the other by day alone", 'the_third_passage': "the fringes' verses sit in mekoshesh's span (Numbers 15:37-41 — its cell compiles the wood-gatherer alone): the recitation's third passage a REFERENCE into that span; the fringes' own law read on the docket (Menachot 43b), no cell — the 4b box's owed line"}},
    'the_tefillin_table': {'value': {'passages': ['Exod 13:1-10', 'Exod 13:11-16', 'Deut 6:4-9', 'Deut 11:13-21'], 'compartments': {'hand': 1, 'head': 4}, 'arm': 'the left — the weak hand (your hand written with a he: yad kehah); the bicep against the heart', 'order': 'the hand bound first, the head; the head removed first (the hand while both are on)', 'head': "the hairline — the place where the skull is soft (between your eyes = the seat of the mourners' baldness, 14:1)"}, 'settings': {'the_sifrei': "35:1-12 — the passages (35:1-2), the hand ONE from 'a sign' (35:3), the head FOUR from the frontlets (35:4), the left (35:5-10 — the amputee, the left-handed), the order (35:11), the head's place (35:12)", 'menachot': "34b-37b — the compartments (34b-35a), the left arm and the amputee (36b-37a), the order (36a: 'when he puts on, the hand first; when he removes, the head first'), the head's place (37a-b: 'between your eyes' the high place of the head), the strap's knot, the four passages' order in the compartments (34b: the dispute of the order — Rashi and Rabbenu Tam the later dispute, outside the shelf)", 'the_exam_persons': "the four-compartment maker ACCEPTED (the parameter); the left-handed — binds on the right, his weak hand (Menachot 37a) ACCEPTED"}},
    'the_mezuzah_table': {'value': {'writing': 'a scroll in ink, not on the stones of the post — the perfect letters', 'post': 'ONE post suffices; the right of the entrance as one enters; within the upper third', 'gates': "the dwelling's — house, courtyard, city, country gates; NOT the bathhouse, the tannery, the shed; the Temple's gates and chambers exempt except the chambers with a dwelling"}, 'settings': {'the_sifrei': "36:1-8 — 'you shall write' (36:1-2: on the post, in ink, not on stone), 'doorposts' (36:3-5: one post, the right, the height), 'your house and your gates' (36:6-8: the dwelling's gates; the Temple's excluded)", 'menachot_shabbat_yoma': "Menachot 31b-34a (the mezuzah's scroll, the closed and open forms, the post, the side — 33a-34a; 34a:11 THE RULE parchment not stones — a whole-row find of 2026-09-17), Shabbat 103b (the letters written perfectly), Yoma 11a (the gates: the bathhouse, the tannery, the Temple's chambers), Maaser Sheni 3:8 (the chambers built in the holy and open to the profane)", 'the_exam_persons': "the scroll-writer ACCEPTED (a scroll in ink); the bathhouse owner EXEMPT (Yoma 11a — no dwelling)"}},
    'the_seven': {'value': ['the tefillin of the head', 'the tefillin of the arm', 'the four fringes', 'the mezuzah'], 'settings': {'menachot_43b': "'beloved are Israel — the Holy One surrounded them with commandments: tefillin on their heads, tefillin on their arms, fringes on their garments, a mezuzah on their doors' (Menachot 43b; the Sifrei 36:9 on 'your gates' — the same seven); David in the bathhouse counted the circumcision the eighth", 'the_count': "seven — the head, the arm, four fringes, the mezuzah: a DATA row, no cell counts them"}},
    'the_list': {'value': ['great and good cities which you did not build', 'houses full of all good which you did not fill', 'hewn cisterns which you did not hew', 'vineyards and olive trees which you did not plant'], 'settings': {'the_retellings': "Joshua 24:13 and Nehemiah 9:25 — the list retold (the run outside the Torah); 'and you shall eat and be satisfied' 6:11, 8:10 (the grace's seat), 11:15", 'the_sifrei': "38:10 — the merit (the fathers' — the land given by the oath); 201:3 — THE SPOIL OF THE SEVEN NATIONS PERMITTED by 6:11 ('houses full of all good' — even swine's flesh): the war chapter's CALL into 6:11 declared OWED FORWARD when chapter 20 compiles (the 4b box)", 'the_oath': "'which he swore to your fathers, to Abraham, to Isaac and to Jacob' (6:10) — the RUN_CITATION pointers at 6:10 / 6:18 / 6:23 name the tape's sworn_by_himself, oath_upheld, visitation_promised"}},
    'the_oath_by_the_name': {'value': {'deut_6_13': "'by his name you shall swear' — a POSITIVE clause: the true oath commanded", 'the_prohibition': "the third word — the vain oath and the false future oath lashed (decalogue.vain_name by CALL)", 'shevuot_35a': 'the Name in an oath'}, 'settings': {'temurah_3b_4a': "3b:16 — Exodus 22:10's bailee's oath; 3b:17 — THE TRUE OATH FROM 6:13 ('you shall swear' a command when one swears truly — R. Giddel in Rav's name); 3b:18 — 10:20's 'and by his name you shall swear'; 4a:2 — 'you shall fear' REFUSED as a positive warning for the lashes (the whole-row finds of 2026-09-17 — the cut had put the true-oath proof on both rows)", 'onkelos': "'serve BEFORE him' (6:13, 10:20, 13:5) — the reverential 'before'; 'swear by his name' (6:13, 10:20)", 'the_exam_person': "the true swearer ACCEPTED (the positive clause holds; the prohibition's side the decalogue's)"}},
    'the_abutter': {'value': {'rule': "the buyer of a field adjoining another's field yields to the neighbor (the abutter) — 'you shall do the right and the good'", 'source': 'Bava Metzia 108a:1-4', 'kind': "a rule beyond the letter seated in the ink's own words — the shelf's teaching, no link of our own"}, 'settings': {'the_ink': "'and you shall do the right and the good in the eyes of the LORD' (6:18) — the pair 6:18 / 12:28 ('the good and the right' reversed there); 'right in the eyes of the LORD' three Torah seats", 'the_exam_person': "the abutter's buyer ACCEPTED — the neighbor's right holds against him (Bava Metzia 108a)"}},
    'the_four_sons': {'value': {'wise': 'Deut 6:20 — what are the testimonies, the statutes and the judgments', 'wicked': 'Exod 12:26 — what is this service TO YOU', 'simple': 'Exod 13:14 — what is this', 'cannot_ask': 'Exod 13:8 — you shall tell your son'}, 'settings': {'pesachim_116a_b': "the four sons and their answers — the wise told the laws of the passover to the last (afikoman), the wicked answered 'for me, not for him', the simple 'with a strong hand', the one who cannot ask opened for (116a-116b); Pesachim 116b:12 THE BLIND OBLIGATED in the Haggadah (a whole-row find of 2026-09-17)", 'mishnah_pesachim_10_4': "'according to the son's understanding his father teaches him; he begins with disgrace and ends with praise, and expounds from a wandering Aramean until he finishes the whole portion'", 'the_first_telling': "Exodus 13:14 VERBATIM with 6:20 to 'saying' (computed: 6:20 adds 'and it shall be' before) — the passover runner's firstborn cell holds 13:13-14 (PE.firstborn by CALL)", 'the_exam_person': "the wise son ACCEPTED (the four askings' row); the son who asks tomorrow ACCEPTED (the answer's rows graded)"}},
    'the_receipt_without_the_name': {'value': {'deut_6_25': "'as he commanded us' — k/834 + 6680 with the suffix, NO Name", 'ezra_4_3': 'the one other Bible seat', 'the_finder': "BLIND — register_census.receipts scans 'as (k/834) commanded (6680) the LORD (3068) within three' and the second form 'according to all that the LORD commanded'", 'the_pointer': 'RUN_CITATION at Deut 6:25 (form AS_WHEN) — the referent stand_here_commanded (5:31), the giving the second', 'owed': "THE FINDER'S THIRD FORM — a gate change across the whole Torah, owed to a gate sitting (the 4b box's PAID line)"}, 'settings': {'the_measure': "the recon's section (7) — the finder's own code (read 2026-09-17): 6:25 not scanned, the gate lists no seat in chapter 6, DECLARED 100 unmoved; CO6 asserts the blindness by CALL to the gate's own finder"}},
    'the_creed_terms': {'value': {'heart': 'with both inclinations — the good and the evil', 'soul': 'even if he takes your soul', 'might': 'with all your money; whatever measure he measures you'}, 'settings': {'mishnah_berakhot_9_5': "'with all your heart' — with your two inclinations; 'with all your soul' — even if he takes your soul; 'with all your might' — with all your money; another reading: with whatever measure he measures out to you, thank him greatly", 'berakhot_61b': "R. Akiva — 'with all your soul: even if he takes your soul' — the martyr's recitation, 'one' on his last breath", 'sanhedrin_74a': "the three transgressions for which one dies rather than transgress — idolatry from 'with all your soul' (R. Eliezer), the martyr's row on the docket", 'the_sifrei': "32:1-7 — love and fear (32:1; Sotah 31a: the lover's reward), the heart's two inclinations (32:2-4), the soul (32:5-6 — R. Akiva on 'even if he takes your soul'), THE MIGHT — money or measure (32:7)", 'onkelos': "'and with all your PROPERTY' (6:5 — the one seat of the word in the book)"}},
    'the_files_diverge': {'value': {'sifrei_36_10': {'hebrew': "the parable of the king's wife", 'english': 'its own 37:2 repeated'}}, 'settings': {'the_caution': "recorded at the reading (2026-09-17): the export's two files diverge at one row of the spine; a Genesis credit stood on the English text, the Hebrew read fresh — a credit is a credit on the file that was read; confirmed by the whole-row read of all 67 Hebrew rows (the fix's part (b))"}},
}
assert len(DATA) == 18, len(DATA)

# ===== THE CELLS — six, each returning out(verdict, effects) =========================================================================
def the_header(case, data):
    """F1 — Deut 6:1-3: the commandment's header (the triad 5:31 / 6:1 / 7:11; the charge EXECUTED — a reference row, no write); fear, the son's son, the land flowing"""
    del P_[:]
    ask = case['ask']
    if ask == 'the_triad':
        ink('6:1', '"and this is the commandment, the statutes and the judgments which the LORD your God commanded to teach you" — "and this is the commandment" %s; the triad\'s three seats %s (5:31 the charge, 6:1 its fulfilment opens, 7:11); "to teach you" %s' % (P('וזאת', 'המצוה'), [s_ for s_, _ in TRIAD], P('ללמד', 'אתכם')))
        dat('the readback row 6:1 VERBATIM — the charge\'s words in the header\'s (computed %s tokens against 5:31\'s %s, %s shared)' % HEADER_DELTA)
        return out("the triad (6:1) — the commandment, the statutes and the judgments: 5:31's charge opened here, 7:11 forward; the header's stamp, no write", ['accepted'])
    if ask == 'the_charge_executed':
        ink('6:1', '"which the LORD your God commanded to teach you, to do them in the land which you are crossing over to possess" — "which you are crossing over to possess" %s; the charge 5:31 "which you shall teach them" the tape\'s stand_here_commanded' % (P('אשר', 'אתם', 'עברים', 'שמה', 'לרשתה'),))
        st = CH.the_answer_and_the_charge({'ask': 'stand_here_with_me'}, CH.DATA); tm = ER.ascent('torah_mitzvah')
        move('cold_run_covenant_at_horeb (CALL) — CH.the_answer_and_the_charge(stand_here_with_me) = %s; cold_run_erection (CALL) — ER.ascent(torah_mitzvah) = %s' % (st[0][:60], tm['v']), "the charge to teach a DEBIT on Moses CLOSED by the prior run (Deut 1:5); Exodus 24:12's 'to teach them' the pair's seat (2)")
        dat('the readback row 6:1 — REFERENCE against stand_here_commanded (5:28-31): the debit\'s close by the prior run unmoved (CO7); no write (R6)')
        return out("the charge executed (6:1) — 'to teach you' runs 5:31's 'which you shall teach them': a REFERENCE row against stand_here_commanded, its debit closed by the prior run (Deut 1:5); NO write", ['accepted'])
    if ask == 'hear_and_observe':
        ink('6:3', '"and you shall hear, O Israel, and observe to do" — "and you shall hear, O Israel" %s (5:1\'s "hear, O Israel" the kin); "observe to do" %s; "that it may be well with you" %s Deuteronomy seats; "that you may multiply greatly" %s' % (P('ושמעת', 'ישראל'), P('ושמרת', 'לעשות'), len(P('ייטב', 'לך', books=('Deut',))), P('תרבון', 'מאד')))
        dat('the frame (R6) — no write; the register: 6:1, 6:3 plural, the body singular (%s plural-only, %s both)' % (PL_ONLY, BOTH))
        return out("hear and observe (6:3) — the frame's charge: no write; 'that it may be well with you' the book's refrain (seven seats)", ['accepted'])
    if ask == 'the_land_flowing':
        ink('6:3', '"as the LORD God of your fathers has spoken to you, a land flowing with milk and honey" — the phrase %d Torah seats, 6:3 THE BOOK\'S FIRST (%s); "as the LORD has spoken" %s' % (len(MILK), [s_ for s_ in MILK if s_.startswith('Deut')], P('כאשר', 'דבר', 'יהוה', books=('Deut',))))
        fw = OS.the_frame({'ask': 'the_write'}, OS.DATA)
        move('cold_run_opening_speech (CALL) — OS.the_frame(the_write) = %s' % (fw[1],), "the book's opening line torah_expounded (1:1-5) — the oath's seats at 1:8 'the land which the LORD swore to your fathers' the speech's own")
        dat("the oath's seats in the chapter: %s (6:10, 6:18 'to your fathers', 6:23 'to our fathers') — the RUN_CITATION pointers name the tape's lines" % ([v for v in range(1, 26) if 'נשבע' in W6(v)],))
        return out("the land flowing (6:3) — the book's first 'milk and honey' (eleven Torah seats); the oath's promise the covenant's, its lines on the tape", ['accepted'])
    if ask == 'your_sons_son':
        ink('6:2', '"that you may fear the LORD your God … you and your son and your son\'s son, all the days of your life" — "you and your son and your son\'s son" %s; "your son\'s son" %s (Exodus 10:2 the kin — the exodus told to the son\'s son); "all the days of your life" %d seats' % (P('אתה', 'ובנך', 'ובן', 'בנך'), P('ובן', 'בנך'), len(P('כל', 'ימי', 'חייך'))))
        dat("three generations named — the teaching's reach (the Sifrei 34:1-4 'your sons' the disciples; Kiddushin 30a the grandfather's duty at 4:9): a DATA note")
        return out("your son's son (6:2) — three generations in the fear; Exodus 10:2's kin: a DATA note, no write", ['accepted'])
    return out('no verdict in span', [FX.NONE])

def the_creed(case, data):
    """F2 — Deut 6:4-5: hear, O Israel; the LORD is one; with all your heart, soul and might; love and fear"""
    del P_[:]
    ask = case['ask']
    if ask == 'hear_o_israel':
        ink('6:4', '"HEAR, O ISRAEL" — the four seats, all this book\'s %s; the imperative %s; Israel named twice in the chapter (%s)' % (P('שמע', 'ישראל'), wm('Deut', 6, 4)[0], [v for v in range(1, 26) if 'ישראל' in W6(v)]))
        move('the Sifrei 31:1, 31:6; Pesachim 56a:2-4', "the creed's first saying JACOB'S SONS' ANSWER at his bed — 'Israel' the father: 'hear, O Israel our father, as there is no doubt in your heart of us, so there is none in ours'; Jacob's response 'blessed be the name of the glory of his kingdom' the whispered line")
        dat("the recitation's forms: in any language (Sotah 7:1 — 'hear'); audibly (R. Yose from 'hear', the sages otherwise — Mishnah Berakhot 2:3; the Sifrei 31:7); with intent for the first verse (Berakhot 13a-13b)")
        return out("hear, O Israel (6:4) — the creed's call: Jacob's sons' answer the first saying (Pesachim 56a); the four seats all this book's", ['accepted'])
    if ask == 'the_lord_is_one':
        ink('6:4', '"the LORD our God, the LORD is ONE" — the pair "the LORD one" at %s alone in the Bible (Zechariah 14:9 "and his name one"); the parser reads the creed\'s word as the numeral [%d] — the chapter\'s one number verse' % (P('יהוה', 'אחד'), ONE))
        dat('the row the_large_letters: %s (PARKED)' % (data['the_large_letters']['value'],))
        dat("Onkelos 'the LORD is one' (chad — the one seat of the pair in the book; the word twelve)")
        return out("the LORD is one (6:4) — the two seats of the pair (6:4, Zechariah 14:9); the numeral the parser's [1]; the large letters a parked hypothesis", ['accepted'])
    if ask == 'with_all_your_heart':
        ink('6:5', '"with all your heart" — "with all your heart and with all your soul" %d seats, all Deuteronomy\'s (4:29 the first: %s); the plural form %d' % (len(HEART_SOUL), HEART_SOUL[-2], len(P('בכל', 'לבבכם', 'ובכל', 'נפשכם'))))
        sk = OH.the_exile_case({'ask': 'seek_and_find'}, OH.DATA)
        move('cold_run_obey_horeb (CALL) — OH.the_exile_case(seek_and_find) = %s' % (sk[0][:50],), "4:29's 'with all your heart and with all your soul' the case's second arm — the creed's words forward")
        dat('the row the_creed_terms: %s' % (data['the_creed_terms']['value'],))
        return out("with all your heart (6:5) — the two inclinations (Mishnah Berakhot 9:5; the Sifrei 32:2-4); 4:29's kin (OH by CALL)", ['accepted'])
    if ask == 'with_all_your_soul':
        ink('6:5', '"and with all your soul" — the soul\'s term; the martyr\'s row on the docket (Sanhedrin 74a) and R. Akiva\'s (Berakhot 61b)')
        move('Mishnah Berakhot 9:5; Berakhot 61b:5-8; Sanhedrin 74a:5-7; the Sifrei 32:5-6', "'even if he takes your soul' — R. Akiva's recitation under the combs, 'one' on his last breath; idolatry the transgression one dies for rather than transgress (74a — from 'with all your soul', R. Eliezer)")
        return out("with all your soul (6:5) — even if he takes your soul: the martyr's clause (R. Akiva, Berakhot 61b; Sanhedrin 74a)", ['accepted'])
    if ask == 'with_all_your_might':
        ink('6:5', '"and with all your might" — the noun with a suffix THE BIBLE\'S ONE SEAT %s' % (U('מאדך', 'מאדכם', 'ומאדך'),))
        move('Mishnah Berakhot 9:5; the Sifrei 32:7', "'with all your might' — with all your money; another reading: with whatever measure he measures out to you; Onkelos 'with all your property'")
        return out("with all your might (6:5) — the Bible's one seat of the word: money, measure and thanks (9:5; the Sifrei 32:7); Onkelos 'your property'", ['accepted'])
    if ask == 'love_and_fear':
        ink('6:5', '"and you shall love the LORD your God" — the phrase %s; "and you shall love" %d seats over the Bible (the neighbor and the stranger Leviticus 19:18, 34)' % (P('ואהבת', 'את', 'יהוה', 'אלהיך'), len(U('ואהבת'))))
        move('the Sifrei 32:1; Sotah 31a:3-6', "love against fear — the one who acts from love greater than the one from fear (Sotah 31a: Job and Abraham); 'you shall love' after 'hear' (the Sifrei 32:1)")
        return out("love and fear (6:5) — 'you shall love' the creed's command after its call; the one who acts from love greater (Sotah 31a; the Sifrei 32:1)", ['accepted'])
    return out('no verdict in span', [FX.NONE])

def the_four_duties(case, data):
    """F3 — Deut 6:6-9: THE FOUR DUTIES compiled for the first time — the recitation (times, postures, who, the passages), the teaching, the tefillin, the mezuzah; the write shema_commanded"""
    del P_[:]
    ask = case['ask']
    if ask == 'recite_when':
        ink('6:7', '"and you shall speak of them … when you lie down and when you rise up" — the six clauses %s (11:19 the pair)' % (P('בשבתך', 'בביתך', 'ובלכתך', 'בדרך', 'ובשכבך', 'ובקומך'),))
        move('Mishnah Berakhot 1:1-2; Berakhot 2a:1-2b:6', "the evening from when the priests enter to eat their terumah (the stars — Nehemiah 4:15) until the first watch (R. Eliezer) / midnight (the sages, a fence) / the dawn (Rabban Gamliel — his sons from the wedding); the morning from blue against white until sunrise (R. Eliezer) / three hours (R. Yehoshua)")
        dat('the row the_recitation_times: %s' % (data['the_recitation_times']['value'],))
        return out("when to recite (6:7) — the evening from the priests' entering, the morning from blue against white: the times' table (Mishnah Berakhot 1:1-2; Berakhot 2a-2b) — the priest entering to eat his terumah begins it", ['accepted'])
    if ask == 'recite_how':
        ink('6:7', '"when you lie down and when you rise up" — the times of lying and rising (Hillel) or the postures (Shammai); "when you walk by the way" %s' % (P('ובלכתך', 'בדרך'),))
        move('Mishnah Berakhot 1:3; Berakhot 10b:9-11a:6; the Sifrei 34:9-10', "Beit Shammai: recline in the evening, stand in the morning; Beit Hillel: every man in his way — 'when you walk by the way'; R. Tarfon's danger on the road: 'you deserved to lose your life, for you transgressed the words of Beit Hillel'")
        dat('the row the_postures: %s' % (data['the_postures']['value'],))
        return out("how to recite (6:7) — in his way (Hillel: the times, not the postures; R. Tarfon rebuked, Mishnah Berakhot 1:3): the reader by the road holds", ['accepted'])
    if ask == 'recite_who':
        ink('6:7', '"and you shall speak of them" — the duty on the one addressed; the exemptions the answer sheet\'s rows')
        move('Mishnah Berakhot 2:5, 2:8, 3:1, 3:3; Berakhot 16a:12-16b:4', "the bridegroom EXEMPT the first night until the Sabbath's end if he did not act (Rabban Gamliel recited — 'I will not remove the kingdom of heaven from me even an hour'); not everyone who wishes may take the name (2:8); one whose dead lies before him exempt (3:1); women, slaves and minors exempt from the Shema and the tefillin, obligated in prayer, the mezuzah and the grace (3:3)")
        dat('the row the_exemptions: %s' % (data['the_exemptions']['value'],))
        return out("who recites (6:7) — the bridegroom EXEMPT the first night (Mishnah Berakhot 2:5; Berakhot 16a); the mourner, women, slaves and minors the table's other rows", ['exempt'])
    if ask == 'daughters_exempt':
        ink('6:7', '"and you shall teach them diligently to YOUR SONS" — "your sons", not your daughters; "teach diligently" the root\'s one seat of the word %s (sharpen, whet — the arrows, the sword, the tongue)' % (U('ושננתם'),))
        move('Kiddushin 29b:5-7; 34a:3', "'and you shall teach them to your sons' — your sons and not your daughters: the daughter exempt from being taught and from teaching (29b); Torah study a positive command not bound by time from which women are exempt by 6:7 (34a:3 — the whole row read 2026-09-17)")
        return out("the daughters (6:7) — 'your sons', not your daughters: the daughter EXEMPT from the teaching (Kiddushin 29b, 34a)", ['exempt'])
    if ask == 'the_passages':
        ink('6:6', '"and these words which I command you this day shall be upon your heart" — "these words" %d seats in the book; "upon your heart" %s (the plural at 11:18)' % (len(P('הדברים', 'האלה', books=('Deut',))), P('על', 'לבבך')))
        mk = MK.the_gatherer({'ask': 'the_case'}, MK.DATA)
        move('Mishnah Berakhot 2:2; the Sifrei 34:2-3; cold_run_mekoshesh (CALL) — MK.the_gatherer(the_case) = %s' % (mk[1],), "the three passages in their order — the yoke of heaven, the yoke of the commandments, the fringes by day (2:2); the fringes recited, not bound; Exodus 13's bound, not recited; the ten words in neither — the third passage's verses in mekoshesh's span (REFERENCE), its cell the gatherer's")
        dat('the row the_two_sets: %s' % (data['the_two_sets']['value'],))
        dat('the row the_passages_order: %s' % (data['the_passages_order']['value'],))
        return out("the passages (6:6) — three recited in order (Mishnah Berakhot 2:2), four bound (Menachot 3:7); two sets with two members each way, the ten words in neither (the Sifrei 34:2-3)", ['accepted'])
    if ask == 'teach_your_sons':
        ink('6:7', '"and you shall teach them diligently to your sons and speak of them" — "and speak of them" %s; the diligent teaching\'s one seat' % (P('ודברת', 'בם'),))
        move('the Sifrei 34:1-4; Kiddushin 29a:12-30b:6', "'your sons' — the disciples (the Sifrei 34:1); the father's duties — to circumcise, redeem, teach Torah, take a wife, teach a trade (Kiddushin 29a); the grandfather's duty from 4:9 (30a — 2b's cell by CALL); 'sharp' — the words in your mouth, that if one asks you answer at once (30a:9 — the whole row read 2026-09-17)")
        return out("teach your sons (6:7) — the father's duty to teach Torah, the disciples 'sons' (the Sifrei 34:1; Kiddushin 29a-30b); sharp in the mouth (30a)", ['accepted'])
    if ask == 'tefillin_passages':
        ink('6:8', '"and you shall bind them for a sign upon your hand" — the four seats of the sign with four spellings of the hand %s' % (SIGN,))
        move('Mishnah Menachot 3:7; Menachot 34b:3-6; the Sifrei 35:1-2', "'the four passages in the tefillin invalidate each other — even one letter': Exodus 13:1-10, 13:11-16, Deuteronomy 6:4-9, 11:13-21 (the passages that say 'a sign upon your hand')")
        dat('the row the_tefillin_table (passages): %s' % (data['the_tefillin_table']['value']['passages'],))
        return out("the tefillin's passages (6:8) — the four that say 'a sign upon your hand' (Menachot 3:7: each invalidates the others)", ['accepted'])
    if ask == 'tefillin_compartments':
        ink('6:8', '"and they shall be for FRONTLETS between your eyes" — the three seats, three spellings %s: 6:8 defective, 11:18 PLENE, Exodus 13:16 plene' % (FRONT,))
        move('the Sifrei 35:3-4; Menachot 34b:12-35a:2; Sanhedrin 4b:12-14', "the hand ONE from 'a sign' (singular); the head FOUR — 'frontlets, frontlets, frontlets' (R. Yishmael: two defective and one plene, 1 + 1 + 2; R. Akiva: tat in Katpi two, pat in Afriki two); THE PRINCIPLE at Sanhedrin 4b:12-14 — the count from the written form against the read: THE OPEN ROW, the ink's 11:18 plene")
        dat('the row the_spellings: %s' % (data['the_spellings']['value'],))
        dat("the compartments %s — A PARAMETER taught by the shelf, never a count from the ink" % (data['the_tefillin_table']['value']['compartments'],))
        return out("the compartments (6:8) — the hand one, the head FOUR: a PARAMETER (the Sifrei 35:3-4; Menachot 34b-35a; Sanhedrin 4b), its derivation from the spellings the open row (11:18 plene in the ink)", ['accepted'])
    if ask == 'tefillin_arm':
        ink('6:8', '"upon your hand" — the hand written with a he at Exodus 13:16 (%s) — "your weak hand" (Menachot 37a); the bicep' % (SIGN[2][1],))
        move('the Sifrei 35:5-10; Menachot 36b:8-37a:12', "'upon your hand' — the left (the weak hand: yad kehah; 'her hand to the peg, her right hand to the hammer' — Judges 5:26); the bicep against the heart ('upon your heart'); the amputee exempt or on the right; the left-handed binds on his right")
        dat('the row the_tefillin_table (arm): %s' % (data['the_tefillin_table']['value']['arm'],))
        return out("the arm (6:8) — the left, the weak hand (Menachot 36b-37a; the Sifrei 35:5-10); the left-handed on his right, the amputee's arm the table's row", ['accepted'])
    if ask == 'tefillin_order':
        ink('6:8', '"and you shall bind them for a sign upon your hand, and they shall be for frontlets between your eyes" — the hand named FIRST')
        move('the Sifrei 35:11; Menachot 36a:2-4', "'when he puts on, the hand first and then the head; when he removes, the head first' — 'and they shall be' (plural): while both are on")
        return out("the order (6:8) — the hand bound first, the head removed first (Menachot 36a; the Sifrei 35:11)", ['accepted'])
    if ask == 'tefillin_head':
        ink('6:8', '"between your eyes" — the five seats %s (14:1 the fifth — the mourners\' baldness "between your eyes")' % (P('בין', 'עיניך') + P('בין', 'עיניכם'),))
        move('the Sifrei 35:12; Menachot 37a:14-37b:2', "'between your eyes' — the high place of the head where the skull of a child is soft (the verbal analogy with 14:1's baldness — the place of hair); not literally between the eyes")
        return out("the head (6:8) — the hairline, not between the eyes: the place of hair by 14:1's analogy (Menachot 37a-b; the Sifrei 35:12)", ['accepted'])
    if ask == 'mezuzah_writing':
        ink('6:9', '"and you shall write them upon the doorposts of your house" — "and you shall write them" %s; the doorposts\' one-letter pair (6:9 defective, 11:20 plene: %s)' % (U('וכתבתם'), DIFF(('Deut', 6, 9), ('Deut', 11, 20))))
        move('the Sifrei 36:1-2; Menachot 34a:11; Shabbat 103b:6-10', "'you shall write them' — a writing on a scroll, not on the stones of the post (Menachot 34a:11 — parchment, not stones: the whole row read 2026-09-17); the letters perfect (Shabbat 103b — the alef not an ayin, the bet not a kaf); the closed and open forms by custom (Menachot 32a)")
        dat('the row the_mezuzah_table (writing): %s' % (data['the_mezuzah_table']['value']['writing'],))
        return out("the mezuzah's writing (6:9) — a scroll in ink with perfect letters, not the stones (Menachot 34a; Shabbat 103b; the Sifrei 36:1-2): the scroll-writer holds", ['accepted'])
    if ask == 'mezuzah_doorpost':
        ink('6:9', '"upon the doorposts of your house" — "doorposts" %d seats (Exodus 12\'s three the passover\'s); the plural read for ONE post' % (len(U('מזוזת', 'מזזות', 'מזוזות', 'המזוזת', 'המזוזות')),))
        move('the Sifrei 36:3-5; Menachot 33a:8-34a:9', "'doorposts' — one post suffices (R. Meir: the plural; the Rabbis: one — 34a:8's arm); the right of the entrance as one enters ('your house — your coming'); within the upper third of the height (33a)")
        dat('the row the_mezuzah_table (post): %s' % (data['the_mezuzah_table']['value']['post'],))
        return out("the doorpost (6:9) — one post, the right as one enters, the upper third (Menachot 33a-34a; the Sifrei 36:3-5)", ['accepted'])
    if ask == 'mezuzah_gates':
        ink('6:9', '"and upon your gates" — the two seats %s (11:20 the pair)' % (U('ובשעריך'),))
        move('the Sifrei 36:6-8; Yoma 11a:9-11b:2; Mishnah Maaser Sheni 3:8', "'your gates' — the dwelling's gates: the house, the courtyard, the city, the country; NOT the bathhouse, the tannery, the shed (no dwelling); the Temple's gates and chambers exempt except the chambers with a dwelling (the parhedrin chamber — Yoma 10a-11a; the chambers built in the holy and open to the profane)")
        dat('the row the_mezuzah_table (gates): %s' % (data['the_mezuzah_table']['value']['gates'],))
        return out("the gates (6:9) — the dwelling's, not the bathhouse's (Yoma 11a; the Sifrei 36:6-8): the bathhouse owner EXEMPT", ['exempt'])
    if ask == 'the_seven':
        ink('6:8-9', 'the tefillin (6:8) and the mezuzah (6:9) with the fringes (Numbers 15:38) — the seven commandments that surround a man')
        move('the Sifrei 36:9; Menachot 43b:5-8', "'beloved are Israel, whom the Holy One surrounded with commandments — tefillin on their heads and on their arms, fringes on their garments, a mezuzah on their doors'; Mishnah Berakhot 1:2's morning start grounded in the fringes' verse (43b:5 — the whole row read 2026-09-17)")
        dat('the row the_seven: %s' % (data['the_seven']['value'],))
        return out("the seven (6:8-9) — the head, the arm, four fringes, the mezuzah surround a man (Menachot 43b; the Sifrei 36:9): a DATA row", ['accepted'])
    if ask == 'the_write':
        ink('6:4-9', 'the creed and the four duties given at the chapter\'s own line — %d tokens, %d letters in the six verses (computed)' % SHEMA_TOK[:2])
        dat("the WRITE shema_commanded — a STATUS on Israel at shema_declared (6:4-9), the counter's own day (40, 11, 1), NO marker")
        return out("the write (6:4-9) — shema_commanded on Israel: the four duties standing from the chapter's own line", ['shema_commanded'])
    return out('no verdict in span', [FX.NONE])

def the_gift_and_the_warning(case, data):
    """F4 — Deut 6:10-15: the list; lest you forget; fear, serve, swear; no other gods; the jealous God"""
    del P_[:]
    ask = case['ask']
    if ask == 'the_list':
        ink('6:10-11', '"great and good cities which you did not build, houses full of all good … hewn cisterns … vineyards and olive trees which you did not plant" — the cities %s, the houses %s, the cisterns %s, "vineyards and olive trees" %s (Joshua 24:13 and Nehemiah 9:25 THE LIST\'S TWO RETELLINGS); "and you shall eat and be satisfied" %s' % (P('ערים', 'גדלת', 'וטבת'), P('ובתים', 'מלאים', 'כל', 'טוב'), P('וברת', 'חצובים'), P('כרמים', 'וזיתים'), P('ואכלת', 'ושבעת')))
        mo = MA.moriah('test_verb_seats'); ig = MA.isaac_gerar('famine_ordinal')
        move('the Sifrei 38:10, 201:3; cold_run_mamre (CALL) — MA.moriah(test_verb_seats) = %s, MA.isaac_gerar(famine_ordinal) = %s' % (mo['v'], ig['v']), "the land by the fathers' merit (38:10); THE SPOIL OF THE SEVEN NATIONS PERMITTED by 6:11's 'houses full of all good' — even swine's flesh (201:3): the war chapter's CALL into 6:11 OWED FORWARD; the oath's lines the tape's (22:16-18, 26:3-5)")
        dat('the row the_list: %s' % (data['the_list']['value'],))
        return out("the list (6:10-11) — cities, houses, cisterns, vineyards and olives 'which you did not …': a DATA row; the spoil permitted by 6:11 (the Sifrei 201:3) owed to the war chapter", ['accepted'])
    if ask == 'lest_you_forget':
        ink('6:12', '"take heed to yourself lest you forget the LORD who brought you out of the land of Egypt, from the house of bondage" — "take heed lest you forget" %s (8:11 the pair); "house of bondage" with the bringing-out %s; the imperative %s' % (FORGET_SEATS, [s_ for s_ in P('מבית', 'עבדים') if s_ in U('הוציאך', 'הוצאתיך', 'המוציאך')], IMPER[12]))
        th = OH.horeb_retold({'ask': 'take_heed_lest_you_forget'}, OH.DATA)
        move('cold_run_obey_horeb (CALL) — OH.FORGET %d seats, 6:12 among them (%s); OH.horeb_retold(take_heed_lest_you_forget) = %s' % (len(OH.FORGET), 'Deut 6:12' in OH.FORGET, th[1]), "the forgetter's prohibition (Menachot 99b; Avot 3:8) at 4:9's seat — 6:12 the same census's thirteenth seat; 'lest' a prohibition (R. Avin)")
        dat("Onkelos 6:12 'lest you forget THE FEAR OF the LORD' — the export's parenthesised variant (one of the book's ten)")
        return out("lest you forget (6:12) — obey_horeb's forgetting census (thirteen seats, 6:12 among them); the prohibition's seat 4:9 (OH by CALL)", ['accepted'])
    if ask == 'fear_serve_swear':
        ink('6:13', '"the LORD your God you shall fear, and him you shall serve, and by his name you shall swear" — 6:13 and 10:20 the pair %s (10:20 adds "and to him you shall cleave": %s); the three verbs %s' % (P('ובשמו', 'תשבע'), DIFF(('Deut', 6, 13), ('Deut', 10, 20)), YIQ2[13]))
        vo = DC.vain_name({'ask': 'vain_oath'}, DC.DATA); ff = DC.vain_name({'ask': 'false_future_oath'}, DC.DATA)
        move('Temurah 3b:16-4a:2; Shevuot 35a; cold_run_decalogue (CALL) — DC.vain_name(vain_oath) = %s, (false_future_oath) = %s' % (vo[1], ff[1]), "'by his name you shall swear' A POSITIVE CLAUSE — the true oath commanded (Temurah 3b:17; 10:20 at 3b:18); 'you shall fear' refused as the lashes' warning (4a:2); the prohibition's side the third word's cell — the vain and the false oath lashed")
        dat('the row the_oath_by_the_name: %s' % (data['the_oath_by_the_name']['value'],))
        dat("Onkelos 'serve BEFORE him' (6:13, 10:20, 13:5) — the reverential 'before'")
        return out("fear, serve, swear (6:13) — the true oath a positive clause (Temurah 3b-4a), its prohibition the third word's (DC by CALL); the true swearer holds", ['accepted'])
    if ask == 'no_other_gods':
        ink('6:14', '"you shall not go after other gods, of the gods of the peoples around you" — "after other gods" %d seats, %d this book\'s; "you shall not go" with the nun %s; a PLURAL prohibition in a singular chapter %s' % (len(P('אחרי', 'אלהים', 'אחרים')), len(P('אחרי', 'אלהים', 'אחרים', books=('Deut',))), P('לא', 'תלכון'), PROHIB[14]))
        ng = CH.the_second_word({'ask': 'no_other_gods'}, CH.DATA)
        move('cold_run_covenant_at_horeb (CALL) — CH.the_second_word(no_other_gods) = %s; Tosefta Avodah Zarah 1:3' % (ng[1],), "the second word's block other_gods_barred stands from 3b (written at the giving's line) — NO second write (CO5); 'you shall not go after' read as going along with the idolaters' caravan (the Tosefta's row — a whole-row find of 2026-09-17)")
        return out("no other gods (6:14) — the second word's clause: other_gods_barred stands from the giving (CH by CALL), no second write; the idolaters' companion the Tosefta's row", ['accepted'])
    if ask == 'the_jealous_god':
        ink('6:15', '"for the LORD your God is a jealous God in your midst, lest the anger of the LORD your God be kindled against you and he destroy you from the face of the ground" — "a jealous God" %s; "in your midst" %d Deuteronomy seats; "from the face of the ground" %d seats (Genesis 6:7 the flood\'s); the case tokens %s' % (JEALOUS, len(U('בקרבך', books=('Deut',))), len(P('מעל', 'פני', 'האדמה')), CASE_TOK['6:15']))
        vi = CH.the_second_word({'ask': 'the_visiting'}, CH.DATA)
        move('cold_run_covenant_at_horeb (CALL) — CH.the_second_word(the_visiting) = %s' % (vi[1],), "the jealous God's visiting the second word's DATA row (Berakhot 7a; Makkot 24a); Onkelos 'his SHEKHINAH is in your midst' (6:15, 7:21)")
        return out("the jealous God (6:15) — 4:24 and 5:9's word at its third Deuteronomy seat; the visiting's arms the second word's (CH by CALL); Onkelos the Shekhinah", ['accepted'])
    return out('no verdict in span', [FX.NONE])

def the_test_and_the_right(case, data):
    """F5 — Deut 6:16-19: you shall not test (Massah — a run citation by name; the write test_barred); surely keep; the right and the good; thrust out"""
    del P_[:]
    ask = case['ask']
    if ask == 'you_shall_not_test':
        ink('6:16', '"you shall not test the LORD your God, as you tested him at MASSAH" — "you shall not test" %s; Massah %s; "as you tested" %s; the test lemma\'s fourteen Torah seats %s; a PLURAL prohibition %s' % (U('תנסו', 'תנסה', 'תנסון'), U('מסה', 'במסה', 'ומסה', 'המסה'), U('נסיתם', 'נסיתו', 'נסיתי'), TEST_LEM, PROHIB[16]))
        tl = ES.trials('ten_list'); cx = ES.trials('count_by_exodus')
        move('cold_run_exodus_story (CALL) — ES.trials(ten_list) = %s; ES.trials(count_by_exodus) = %s' % (tl['v'], cx['v']), "Arakhin 15a:14 — ten trials, 'two at the water' (Marah, Rephidim); the tape's Rephidim lines FOUND by kind and first verse — murmured at 17:2, rock_struck at 17:6, named at 17:7 'Massah and Meribah' (CO3)")
        dat('the readback row 6:16 VERBATIM — a RUN CITATION BY NAME (computed %s tokens against 17:7\'s %s, %s shared; 17:2\'s %s)' % MASSAH_DELTA)
        return out("you shall not test (6:16) — Massah the tape's named line (Exodus 17:7), a run citation by name; the ten trials (Arakhin 15a; ES by CALL): the block test_barred on Israel", ['accepted'])
    if ask == 'surely_keep':
        ink('6:17', '"you shall SURELY KEEP the commandments of the LORD your God, and his testimonies and his statutes which he commanded you" — the infinitive absolute %s (the book\'s three: 5:12, 6:17, 16:1); "his testimonies" — Deuteronomy\'s three seats %s' % (INFA[17], [s_ for s_ in U('עדת', 'העדת', 'עדתיו', 'ועדתיו', 'עדותיו', 'ועדותיו', books=T) if s_.startswith('Deut')]))
        sf = OH.the_cities_and_the_frame({'ask': 'the_second_frame'}, OH.DATA)
        move('cold_run_obey_horeb (CALL) — OH.the_cities_and_the_frame(the_second_frame) = %s' % (sf[1],), "4:45's header 'the testimonies, the statutes and the judgments' — the register's footer (DAEMONS, daemons 2); 6:17 and 6:20 its two kin seats")
        return out("surely keep (6:17) — the infinitive absolute (the book's three); the testimonies' three seats with 4:45's header (OH by CALL): no write", ['accepted'])
    if ask == 'the_right_and_the_good':
        ink('6:18', '"and you shall do the right and the good in the eyes of the LORD" — %s; the pair 6:18 / 12:28 %s; "right in the eyes of the LORD" %s' % (P('ועשית', 'הישר', 'והטוב'), P('הישר', 'והטוב') + P('הטוב', 'והישר'), P('הישר', 'בעיני', 'יהוה', books=T)))
        move('Bava Metzia 108a:1-4', "THE ABUTTER — the buyer of a field adjoining another's yields to the neighbor: 'you shall do the right and the good' — a rule beyond the letter seated in the ink's own words (the exam's case row)")
        dat('the row the_abutter: %s' % (data['the_abutter']['value'],))
        return out("the right and the good (6:18) — the abutter's rule (Bava Metzia 108a): the buyer of the adjoining field yields to the neighbor", ['accepted'])
    if ask == 'thrust_out_enemies':
        ink('6:19', '"to thrust out all your enemies from before you, as the LORD has spoken" — %s; the root\'s eleven seats %s (the manslayer\'s "thrust" Numbers 35:20, 22; 9:4 forward); "as the LORD has spoken" 6:3 and 6:19 the chapter\'s two' % (P('להדף', 'את', 'כל', 'איביך'), LEMV('1920')))
        dat("9:4 'when the LORD thrusts them out from before you' — FORWARD; Onkelos 'shatter'; a DATA note, no write")
        return out("thrust out (6:19) — the enemies thrust out 'as the LORD has spoken': 9:4 forward, the manslayer's verb: a DATA note", ['accepted'])
    if ask == 'the_write':
        ink('6:16-19', 'the test barred at the chapter\'s second line — "you shall not test … as you tested at Massah"')
        dat("the WRITE test_barred — a BLOCK on Israel at testing_barred (6:16-19), the counter's own day (40, 11, 1), NO marker")
        return out("the write (6:16-19) — test_barred on Israel: the block at the chapter's second line", ['test_barred'])
    return out('no verdict in span', [FX.NONE])

def the_sons_question(case, data):
    """F6 — Deut 6:20-25: the son's question (the four askings), the answer's rows graded (T1), the receipt without the Name, righteousness for us"""
    del P_[:]
    ask = case['ask']
    if ask == 'the_four_askings':
        ink('6:20', '"when your son asks you tomorrow, saying: what are the testimonies and the statutes and the judgments which the LORD our God commanded you" — 6:20 and Exodus 13:14 THE TWO SEATS %s, verbatim to "saying" (the diff %s); the askings with "tomorrow" %s; "what are the testimonies" %s' % (P('כי', 'ישאלך', 'בנך', 'מחר'), DIFF(('Deut', 6, 20), ('Exod', 13, 14)), ASKINGS, P('מה', 'העדת')))
        fb = PE.firstborn({'kind': 'human'}, PE.DATA)
        move('Pesachim 116a:6-116b:3; Mishnah Pesachim 10:4; cold_run_pesach (CALL) — PE.firstborn(human) = %s' % (fb[0][:30],), "THE FOUR SONS — the wise (6:20), the wicked (12:26), the simple (13:14), the one who cannot ask (13:8): 'according to the son's understanding'; the passover runner's firstborn cell holds 13:13-14's seat; the blind obligated (116b:12)")
        dat('the row the_four_sons: %s' % (data['the_four_sons']['value'],))
        return out("the four askings (6:20) — the wise son's question, verbatim with Exodus 13:14 to 'saying' (the four sons, Pesachim 116a-b; PE by CALL)", ['accepted'])
    if ask == 'the_answer_rows':
        ink('6:21-24', '"and you shall say to your son: we were slaves to Pharaoh in Egypt, and the LORD brought us out … signs and wonders … and us he brought out from there … to give us the land which he swore to our fathers; and the LORD commanded us …" — the answer in the FIRST PERSON PLURAL %s; the narrative verbs %s; "we were slaves to Pharaoh" %s; "signs and wonders" %s' % (sorted(ONE_CP), REG, P('עבדים', 'היינו', 'לפרעה'), W6(22)[2:4]))
        jo = JS.the_oath('kindness_and_truth')
        move('cold_run_joseph (CALL) — JS.the_oath(kindness_and_truth) = %s; THE_LOOP.md step 6 (T1)' % (jo['v'],), "THE RETELLING IS COMMANDED — the answer's five rows REFERENCE ROWS graded against the tape: 6:21 EXPANDED (brought_out 12:51 with 'a strong hand'), 6:22 SHORTENED (the ten plague_struck lines to one clause), 6:23 EXPANDED (the oath's three lines — Genesis 22:16, 26:3, 50:24), 6:24 EXPANDED (the giving and the charge), 6:25 VERBATIM (the receipt); every entry FOUND on the running world (CO4)")
        dat('the readback\'s deltas computed — the going out %s, the plagues %s, the oath %s, the charge %s' % (OUT_DELTA, PLAGUE_DELTA, OATH_DELTA, CHARGE_DELTA))
        return out("the answer's rows (6:21-24) — the exodus retold in the first person plural: EXPANDED, SHORTENED, EXPANDED, EXPANDED against the tape's lines (T1); no second act", ['accepted'])
    if ask == 'the_receipt':
        ink('6:25', '"and it shall be righteousness for us, if we observe to do all this commandment before the LORD our God, AS HE COMMANDED US" — "as he commanded us" %s (Ezra 4:3 the one other seat); "all this commandment" %s; the suffix and NO Name (%s)' % (RECEIPT_NO_NAME, P('כל', 'המצוה', 'הזאת'), morphs('Deut', 6, 25)[-1]))
        ch = CH.the_answer_and_the_charge({'ask': 'the_charge'}, CH.DATA); bc = ER.blood_covenant('book_of_covenant')
        move('cold_run_covenant_at_horeb (CALL) — CH.the_answer_and_the_charge(the_charge) = %s; cold_run_erection (CALL) — ER.blood_covenant(book_of_covenant) = %s' % (ch[1], bc['v']), "THE RECEIPT WITHOUT THE NAME — a RUN CITATION of the charge's line (5:31 'all the commandment … which you shall teach them'), the giving the second referent; the register gate's finder BLIND (measured; CO6); the pointer RUN_CITATION at Deut 6:25 on file; the finder's third form owed")
        dat('the row the_receipt_without_the_name: %s' % (data['the_receipt_without_the_name']['value'],))
        return out("the receipt (6:25) — 'as he commanded us' without the Name: a run citation of the charge (5:31), VERBATIM in kind; the gate's finder blind, the pointer on file", ['accepted'])
    if ask == 'righteousness_for_us':
        ink('6:25', '"and it shall be RIGHTEOUSNESS for us" — %s; "righteousness" eight Torah seats %s (Genesis 15:6 the first, 24:13 the pledge\'s "it shall be righteousness for you")' % (P('וצדקה', 'תהיה', 'לנו'), U('צדקה', 'וצדקה', 'לצדקה', 'צדקתך', 'ובצדקתך', 'בצדקתי', 'בצדקתך', books=T)))
        dat("Onkelos 'MERIT' at 6:25 and 24:13 — the two seats; Genesis 15:6's kin: a DATA note, no write")
        return out("righteousness for us (6:25) — Genesis 15:6's word at the answer's close; 24:13's pledge the kin; Onkelos 'merit': a DATA note", ['accepted'])
    if ask == 'the_readback_table':
        ink('6:1-25', 'the seven rows of the third form — the header\'s (6:1), the test\'s (6:16), the answer\'s five (6:21-25)')
        dat('the readback table — %d rows: %s; every row a law\'s row; no row open' % (len(READBACK), dict(RB_GRADES)))
        return out("the readback table — seven rows graded (VERBATIM 3, EXPANDED 3, SHORTENED 1); every row inside a law (T1); no row open", ['accepted'])
    return out('no verdict in span', [FX.NONE])

# ---- THE CALLEES' FACTS (every edge live at the cells that consume them; the values asserted from the callees' own prints — ch6_callees.out) ----
CH_NOG = CH.the_second_word({'ask': 'no_other_gods'}, CH.DATA); CH_VIS = CH.the_second_word({'ask': 'the_visiting'}, CH.DATA); CH_STAND = CH.the_answer_and_the_charge({'ask': 'stand_here_with_me'}, CH.DATA); CH_CHARGE = CH.the_answer_and_the_charge({'ask': 'the_charge'}, CH.DATA)
assert CH_NOG[1] == ['accepted'] and CH_NOG[0].startswith('no other gods before me (5:7)') and CH_VIS[1] == ['accepted'] and CH_STAND[1] == ['commanded'] and CH_CHARGE[1] == ['accepted'] and len(CH.READBACK) == 21 and dict(CH.RB_GRADES) == {'VERBATIM': 5, 'VARIANT': 5, 'EXPANDED': 5, 'TURNED': 4, 'SUPPLIED': 2}, (CH_NOG[:2], CH_STAND[1], len(CH.READBACK))
OH_TAKE = OH.horeb_retold({'ask': 'take_heed_lest_you_forget'}, OH.DATA); OH_FRAME = OH.the_cities_and_the_frame({'ask': 'the_second_frame'}, OH.DATA); OH_SEEK = OH.the_exile_case({'ask': 'seek_and_find'}, OH.DATA)
assert len(OH.FORGET) == 13 and 'Deut 6:12' in OH.FORGET and 'Deut 4:9' in OH.FORGET and OH_TAKE[1] == ['accepted'] and OH_FRAME[1] == ['accepted'] and OH_SEEK[0].startswith('seek and find (4:29)') and OH.DATA['the_creed']['value'] == ['Deut 4:35', 'Deut 4:39'] and len(OH.READBACK) == 11, (len(OH.FORGET), OH_TAKE[1], OH_SEEK[0][:30])
DC_VO = DC.vain_name({'ask': 'vain_oath'}, DC.DATA); DC_FF = DC.vain_name({'ask': 'false_future_oath'}, DC.DATA)
assert DC_VO[:2] == ('lashes', ['lashes']) and DC_FF[:2] == ('lashes', ['lashes']) and len(DC.CASES) == 13, (DC_VO[:2], DC_FF[:2])
ES_TEN = ES.trials('ten_list'); ES_SIX = ES.trials('count_by_exodus')
assert ES_TEN['v'] == ('two_at_the_sea', 'two_at_the_water', 'two_at_the_manna', 'two_at_the_quail', 'one_at_the_calf', 'one_at_paran') and ES_TEN['fx'] == ['tested_the_lord'] and ES_SIX['v'] == 6, (ES_TEN['v'], ES_SIX['v'])
PE_HUMAN = PE.firstborn({'kind': 'human'}, PE.DATA)
assert PE_HUMAN[0].startswith('redeem') and 'pays' in PE_HUMAN[1], PE_HUMAN[:2]
OS_WRITE = OS.the_frame({'ask': 'the_write'}, OS.DATA); OS_WORDS = OS.the_frame({'ask': 'the_words'}, OS.DATA)
assert OS_WRITE[1] == ['torah_expounded'] and OS_WORDS[1] == ['accepted'] and len(OS.READBACK) == 42, (OS_WRITE[1], OS_WORDS[1], len(OS.READBACK))
MA_TEST = MA.moriah('test_verb_seats'); MA_TEN = MA.moriah('ten_trials_sheet'); MA_FAM = MA.isaac_gerar('famine_ordinal')
assert MA_TEST['v'] == 1 and MA_TEST['fx'] == ['tried'] and MA_TEN['v'] == 10 and MA_FAM['v'] == 'the_second', (MA_TEST['v'], MA_TEN['v'], MA_FAM['v'])
JS_17 = JS.the_oath('seventeen_years'); JS_147 = JS.the_oath('hundred_forty_seven'); JS_KT = JS.the_oath('kindness_and_truth')
assert JS_17['v'] == 17 and JS_147['v'] == 147 and JS_KT['v'] == 'kindness_and_truth', (JS_17['v'], JS_147['v'], JS_KT['v'])
MK_CASE = MK.the_gatherer({'ask': 'the_case'}, MK.DATA)
assert MK_CASE[1] == ['warned_specifying_the_labor', 'put_to_death', 'in_custody', 'stoned'], MK_CASE[1]
ER_TORAH = ER.ascent('torah_mitzvah'); ER_BOOK = ER.blood_covenant('book_of_covenant')
assert ER_TORAH['v'] == 2 and ER_BOOK['v'] == 4 and ER_BOOK['fx'] == ['oral_law_unwritten'], (ER_TORAH['v'], ER_BOOK['v'], ER_BOOK['fx'])


# ===== THE WRAP (D9-iv): the daemon over the cells — the ledger written, no event emitted =====================
def law_hear_o_israel(event, world):
    """Deut 6:1-25 (cold_run_hear_o_israel.py F1-F6). given_at Deut 6:4 — THE SHEMA'S FIRST AND ONLY GIVING, the chapter's own line on the counter's
    day (40, 11, 1), NO marker; installed_by boot (the two Deuteronomy daemons' form). TWO TAPE LINES of its own: shema_declared (6:4-9 — the creed and
    the four duties: shema_commanded a STATUS on Israel) and testing_barred (6:16-19 — Massah the tape's named line, a run citation by name:
    test_barred a BLOCK on Israel). The exam's case kind dispatches to the cells in EXPLICIT branches with LITERAL effects per kind (an unnamed effect
    is a KeyError). No timer; no close; the second word's block and the charge's debit UNMOVED (CO5, CO7)."""
    k, src = event['kind'], event['case_source']
    E_ = lambda eff, s, cp=None, amount=None, due=None, law='', value=None: {'effect': eff, 'subject': s, 'counterparty': cp, 'amount': amount, 'due': due, 'value': value if value is not None else True, 'source_law': law, 'case_source': src}
    if k == 'shema_declared':
        return [E_('shema_commanded', 'israel', value={'creed': 'hear, O Israel: the LORD our God, the LORD is one (6:4)', 'love': 'with all your heart, with all your soul, with all your might (6:5)', 'duties': ['the recitation — when you lie down and when you rise up (6:7)', 'the teaching — to your sons (6:7)', 'the tefillin — a sign upon your hand, frontlets between your eyes (6:8)', 'the mezuzah — the doorposts of your house and your gates (6:9)'], 'compartments': {'hand': 1, 'head': 4, 'kind': 'PARAMETER (the Sifrei 35:3-4; Menachot 34b-35a; Sanhedrin 4b:12-14) — the open row the_spellings'}, 'day': 'the counter\'s (40, 11, 1), no marker'}, law="F3 [INK 6:4-9 'hear, O Israel … and you shall write them upon the doorposts of your house and upon your gates' — THE FOUR DUTIES compiled at THE DEUTERONOMY WALK 4b from the ink with the answer sheet Mishnah Berakhot 1:1-3:6, 2:2, 9:5, Menachot 3:7, Sotah 7:1 (no cell in any runner before): a STATUS on Israel at the chapter's own line; the compartments a parameter, the derivation from the spellings the open row (11:18 plene in the ink); the third passage in mekoshesh's span by REFERENCE]")]
    if k == 'testing_barred':
        return [E_('test_barred', 'israel', value={'the_word': 'you shall not test the LORD your God, as you tested him at Massah (6:16)', 'massah': "the tape's named line — Exodus 17:7 'Massah and Meribah' (murmured 17:2-3, rock_struck 17:6)", 'the_trials': 'ten (Arakhin 15a — two at the water: Marah, Rephidim)', 'with_it': "surely keep (6:17); the right and the good — the abutter (6:18, Bava Metzia 108a); thrust out (6:19, 9:4 forward)"}, law="F5 [INK 6:16-19 'you shall not test the LORD your God, as you tested him at Massah' — a BLOCK on Israel at the chapter's second line; Massah A RUN CITATION BY NAME (the tape's Exodus 17:7 line FOUND by kind and first verse — CO3; ES.trials by CALL); 'surely keep' the infinitive absolute, the testimonies' three seats; 'the right and the good' Bava Metzia 108a's abutter]")]
    if k == 'shema_case':
        fn = {'header': the_header, 'creed': the_creed, 'duties': the_four_duties, 'gift': the_gift_and_the_warning, 'test': the_test_and_the_right, 'son': the_sons_question}[event['cell']]
        v, e, _ = fn({'ask': event['ask']}, DATA); L = '%s [%s]' % ({'header': 'F1', 'creed': 'F2', 'duties': 'F3', 'gift': 'F4', 'test': 'F5', 'son': 'F6'}[event['cell']], event['ask']); s_ = event['person']
        W = {'accepted': E_('accepted', s_, value=v, law=L), 'exempt': E_('exempt', s_, value=v, law=L)}
        return [W[x] for x in e if x != FX.NONE]
    return []


LINES = [
    ('Deut 6:4-9 — hear, O Israel: the LORD our God, the LORD is one; and you shall love the LORD your God with all your heart and with all your soul and with all your might; and these words which I command you this day shall be upon your heart; and you shall teach them diligently to your sons and speak of them when you sit in your house and when you walk by the way and when you lie down and when you rise up; and you shall bind them for a sign upon your hand and they shall be for frontlets between your eyes; and you shall write them upon the doorposts of your house and upon your gates',),
    ('Deut 6:16-19 — you shall not test the LORD your God, as you tested him at Massah; you shall surely keep the commandments of the LORD your God and his testimonies and his statutes which he commanded you; and you shall do the right and the good in the eyes of the LORD, that it may be well with you and that you may go in and possess the good land which the LORD swore to your fathers, to thrust out all your enemies from before you, as the LORD has spoken',),
]
CLOSES = "none — no close this chapter: the charge to teach (commanded on Moses) stays CLOSED by the prior run (6:1 a reference row); the second word's block stands (6:14 no second write); the refuge debit OPEN; the header, the gift and the answer no write"

PERSONS = [
    ('the-priest-entering-to-eat-terumah', 'duties', 'recite_when', "Mishnah Berakhot 1:1; Berakhot 2a-2b — the exam's row recite_when"),
    ('the-reader-by-the-road', 'duties', 'recite_how', "Mishnah Berakhot 1:3; Berakhot 10b-11a — the exam's row recite_how"),
    ('the-bridegroom', 'duties', 'recite_who', "Mishnah Berakhot 2:5; Berakhot 16a — the exam's row recite_who"),
    ('the-daughter', 'duties', 'daughters_exempt', "Kiddushin 29b; 34a:3 — the exam's row daughters_exempt"),
    ('the-four-compartment-maker', 'duties', 'tefillin_compartments', "the Sifrei 35:3-4; Menachot 34b-35a; Sanhedrin 4b:12-14 — the exam's row tefillin_compartments"),
    ('the-left-handed', 'duties', 'tefillin_arm', "the Sifrei 35:5-10; Menachot 36b-37a — the exam's row tefillin_arm"),
    ('the-scroll-writer', 'duties', 'mezuzah_writing', "the Sifrei 36:1-2; Menachot 34a:11; Shabbat 103b — the exam's row mezuzah_writing"),
    ('the-bathhouse-owner', 'duties', 'mezuzah_gates', "the Sifrei 36:6-8; Yoma 11a — the exam's row mezuzah_gates"),
    ('the-true-swearer', 'gift', 'fear_serve_swear', "Temurah 3b:17-4a:2; Shevuot 35a — the exam's row fear_serve_swear"),
    ('the-idolaters-companion', 'gift', 'no_other_gods', "Tosefta Avodah Zarah 1:3 — the exam's row no_other_gods"),
    ('the-tester-at-massah', 'test', 'you_shall_not_test', "Exodus 17:2-7; Arakhin 15a — the exam's row you_shall_not_test"),
    ('the-abutters-buyer', 'test', 'the_right_and_the_good', "Bava Metzia 108a:1-4 — the exam's row the_right_and_the_good"),
    ('the-wise-son', 'son', 'the_four_askings', "Pesachim 116a-b; Mishnah Pesachim 10:4 — the exam's row the_four_askings"),
    ('the-son-who-asks-tomorrow', 'son', 'the_answer_rows', "Deut 6:20-25; THE_LOOP.md step 6 (T1) — the exam's row the_answer_rows"),
]


def scene():
    """THE SCENE — the exam's rows replayed on the world engine (the exodus epoch): the exam's persons through shema_case — the priest at evening,
    the reader by the road, the bridegroom and the daughter (exempt), the compartments, the left-handed, the scroll, the bathhouse (exempt), the true
    swearer, the idolaters' companion, the tester, the abutter's buyer, the wise son, the son who asks tomorrow."""
    with contextlib.redirect_stdout(io.StringIO()):
        w = WE.World(era='Deut 6:1-25: chapter 6 on the shelf — Berakhot, Menachot, Kiddushin, Sanhedrin, Temurah, Bava Metzia, Pesachim, Yoma on the engine (the exodus epoch)', epoch='exodus')
        w.laws = [law_hear_o_israel]
        w.advance(w.clock.day_in('exodus', 40, 11, 1))
        # THE DAEMON GATE READS LITERAL SUBMITS ONLY — the fourteen persons typed out from PERSONS
        w.submit({'kind': 'shema_case', 'subject': 'the-priest-entering-to-eat-terumah', 'person': 'the-priest-entering-to-eat-terumah', 'cell': 'duties', 'ask': 'recite_when', 'case_source': "Mishnah Berakhot 1:1; Berakhot 2a-2b — the exam's row recite_when"})
        w.submit({'kind': 'shema_case', 'subject': 'the-reader-by-the-road', 'person': 'the-reader-by-the-road', 'cell': 'duties', 'ask': 'recite_how', 'case_source': "Mishnah Berakhot 1:3; Berakhot 10b-11a — the exam's row recite_how"})
        w.submit({'kind': 'shema_case', 'subject': 'the-bridegroom', 'person': 'the-bridegroom', 'cell': 'duties', 'ask': 'recite_who', 'case_source': "Mishnah Berakhot 2:5; Berakhot 16a — the exam's row recite_who"})
        w.submit({'kind': 'shema_case', 'subject': 'the-daughter', 'person': 'the-daughter', 'cell': 'duties', 'ask': 'daughters_exempt', 'case_source': "Kiddushin 29b; 34a:3 — the exam's row daughters_exempt"})
        w.submit({'kind': 'shema_case', 'subject': 'the-four-compartment-maker', 'person': 'the-four-compartment-maker', 'cell': 'duties', 'ask': 'tefillin_compartments', 'case_source': "the Sifrei 35:3-4; Menachot 34b-35a; Sanhedrin 4b:12-14 — the exam's row tefillin_compartments"})
        w.submit({'kind': 'shema_case', 'subject': 'the-left-handed', 'person': 'the-left-handed', 'cell': 'duties', 'ask': 'tefillin_arm', 'case_source': "the Sifrei 35:5-10; Menachot 36b-37a — the exam's row tefillin_arm"})
        w.submit({'kind': 'shema_case', 'subject': 'the-scroll-writer', 'person': 'the-scroll-writer', 'cell': 'duties', 'ask': 'mezuzah_writing', 'case_source': "the Sifrei 36:1-2; Menachot 34a:11; Shabbat 103b — the exam's row mezuzah_writing"})
        w.submit({'kind': 'shema_case', 'subject': 'the-bathhouse-owner', 'person': 'the-bathhouse-owner', 'cell': 'duties', 'ask': 'mezuzah_gates', 'case_source': "the Sifrei 36:6-8; Yoma 11a — the exam's row mezuzah_gates"})
        w.submit({'kind': 'shema_case', 'subject': 'the-true-swearer', 'person': 'the-true-swearer', 'cell': 'gift', 'ask': 'fear_serve_swear', 'case_source': "Temurah 3b:17-4a:2; Shevuot 35a — the exam's row fear_serve_swear"})
        w.submit({'kind': 'shema_case', 'subject': 'the-idolaters-companion', 'person': 'the-idolaters-companion', 'cell': 'gift', 'ask': 'no_other_gods', 'case_source': "Tosefta Avodah Zarah 1:3 — the exam's row no_other_gods"})
        w.submit({'kind': 'shema_case', 'subject': 'the-tester-at-massah', 'person': 'the-tester-at-massah', 'cell': 'test', 'ask': 'you_shall_not_test', 'case_source': "Exodus 17:2-7; Arakhin 15a — the exam's row you_shall_not_test"})
        w.submit({'kind': 'shema_case', 'subject': 'the-abutters-buyer', 'person': 'the-abutters-buyer', 'cell': 'test', 'ask': 'the_right_and_the_good', 'case_source': "Bava Metzia 108a:1-4 — the exam's row the_right_and_the_good"})
        w.submit({'kind': 'shema_case', 'subject': 'the-wise-son', 'person': 'the-wise-son', 'cell': 'son', 'ask': 'the_four_askings', 'case_source': "Pesachim 116a-b; Mishnah Pesachim 10:4 — the exam's row the_four_askings"})
        w.submit({'kind': 'shema_case', 'subject': 'the-son-who-asks-tomorrow', 'person': 'the-son-who-asks-tomorrow', 'cell': 'son', 'ask': 'the_answer_rows', 'case_source': "Deut 6:20-25; THE_LOOP.md step 6 (T1) — the exam's row the_answer_rows"})
    n = lambda eid, eff: len([e for e in w.entity(eid).ledger if e['effect'] == eff])
    tset = len([l for l in w.log if l[0] == 'TIMER-SET']); tfire = len([l for l in w.log if l[0] == 'TIMER-FIRE']); tcan = len([l for l in w.log if l[0] == 'TIMER-CANCEL'])
    closes = len([e for ent in w.entities.values() for e in ent.ledger if e.get('closed_by')])
    return (tuple(n(p, 'accepted') + n(p, 'exempt') for p, _, _, _ in PERSONS), (n('the-bridegroom', 'exempt'), n('the-daughter', 'exempt'), n('the-bathhouse-owner', 'exempt')), (tset, tfire, tcan, len(w.timers)), len(w.entities), closes), w
SCENE, _W = scene()
# THE PREDICTION (typed before the first run — the design's arithmetic): every exam person written once; the three exempt arms ONE each; no timer;
# ENTITIES the fourteen persons; CLOSES 0.
SCENE_PREDICTED = ((1,) * 14, (1, 1, 1), (0, 0, 0, 0), 14, 0)
assert SCENE == SCENE_PREDICTED, ('THE DEUTERONOMY WALK 4b: the scene moved from its prediction', SCENE, SCENE_PREDICTED)


def narrative():
    """THE DEUTERONOMY WALK 4b (2026-09-17): the chapter's own acts AS HISTORY — the two lines on the counter's own day (40, 11, 1), NO marker (the
    retrograde stretch of 5:23 ended at 5:32's forward marker) — on a world with this runner's daemon: 2 writes (shema_commanded, test_barred), no
    timer, ONE entity (Israel), the counter at (11, 1), no close, no row, no dated line. Recorded by the sequential run's recorder and stitched onto
    the tape (page_order after the last Deuteronomy 5 line). Not a graded cell: the tuple below is a tripwire typed from the design."""
    with contextlib.redirect_stdout(io.StringIO()):
        w = WE.World(era='Deut 6:1-25 on the tape — the Shema declared and the test barred, the counter\'s own day (the exodus epoch)', epoch='exodus')
        w.laws = [law_hear_o_israel]
        w.advance(w.clock.day_in('exodus', 40, 11, 1))
        # THE DAEMON GATE READS LITERAL SUBMITS ONLY — the two lines typed out; no marker; no field named `until`, `days` or `due`
        w.submit({'kind': 'shema_declared', 'subject': 'israel', 'creed': 'hear, O Israel: the LORD our God, the LORD is one (6:4)', 'duties': ['recite', 'teach', 'bind', 'write'], 'case_source': LINES[0][0]})
        w.submit({'kind': 'testing_barred', 'subject': 'israel', 'first_telling': 'Exod 17:2-7', 'massah': 'as you tested at Massah (6:16) — the tape\'s named line Exod 17:7', 'case_source': LINES[1][0]})
    writes = len([l for l in w.log if l[0] == 'WRITE'])
    closes = len([e for ent in w.entities.values() for e in ent.ledger if e.get('closed_by')])
    rows = len([l for l in w.log if l[0] == 'ROW'])
    dated = len([l for l in w.log if l[0] == 'EVENT' and l[2].get('dated') is not None])
    return (writes, len([l for l in w.log if l[0] == 'TIMER-SET']), len(w.entities), w.clock.eras['exodus'].date(w.clock.day)[1:], closes, rows, len(w.tables['population']), dated), w


NARRATIVE, _WN = narrative()
NARRATIVE_PREDICTED = (2, 0, 1, (11, 1), 0, 0, 0, 0)   # DEUTERONOMY_WALK.md "Sitting 4b": 2 writes, no timer, ONE entity, the counter's day (11, 1), no close, no row, no population row, no dated line
assert NARRATIVE == NARRATIVE_PREDICTED, ('THE DEUTERONOMY WALK 4b: the chapter\'s narrative moved from its prediction', NARRATIVE, NARRATIVE_PREDICTED)
_isr = _WN.entity('israel').ledger
assert [e['effect'] for e in _isr] == ['shema_commanded', 'test_barred'] and _isr[0]['value']['compartments']['head'] == 4 and not any(e.get('closed_by') for e in _isr), [e['effect'] for e in _isr]


# =====================================================================
# Motion 2 — THE TEST DATA: the answer sheet's rows (the docket's LAW rows and the cells' asks) — GENERATED FROM THE CELLS' OWN ASKS by ch6_cases_gen.py
# (1b's lesson: a mistyped expected string grades nothing), then frozen as literals under the honest-pairing guard.
# =====================================================================
CASES = [
    # F1 — the_header
    ('Deut 6:1 — the_triad', lambda: the_header({'ask': 'the_triad'}, DATA), "the triad (6:1) — the commandment, the statutes and the judgments: 5:31's charge opened here, 7:11 forward; the header's stamp, no write"),
    ('Deut 6:1 — the_charge_executed', lambda: the_header({'ask': 'the_charge_executed'}, DATA), "the charge executed (6:1) — 'to teach you' runs 5:31's 'which you shall teach them': a REFERENCE row against stand_here_commanded, its debit closed by the prior run (Deut 1:5); NO write"),
    ('Deut 6:3 — hear_and_observe', lambda: the_header({'ask': 'hear_and_observe'}, DATA), "hear and observe (6:3) — the frame's charge: no write; 'that it may be well with you' the book's refrain (seven seats)"),
    ('Deut 6:3 — the_land_flowing', lambda: the_header({'ask': 'the_land_flowing'}, DATA), "the land flowing (6:3) — the book's first 'milk and honey' (eleven Torah seats); the oath's promise the covenant's, its lines on the tape"),
    ('Deut 6:2 — your_sons_son', lambda: the_header({'ask': 'your_sons_son'}, DATA), "your son's son (6:2) — three generations in the fear; Exodus 10:2's kin: a DATA note, no write"),
    # F2 — the_creed
    ('Deut 6:4; Pesachim 56a — hear_o_israel', lambda: the_creed({'ask': 'hear_o_israel'}, DATA), "hear, O Israel (6:4) — the creed's call: Jacob's sons' answer the first saying (Pesachim 56a); the four seats all this book's"),
    ('Deut 6:4 — the_lord_is_one', lambda: the_creed({'ask': 'the_lord_is_one'}, DATA), "the LORD is one (6:4) — the two seats of the pair (6:4, Zechariah 14:9); the numeral the parser's [1]; the large letters a parked hypothesis"),
    ('Deut 6:5; Mishnah Berakhot 9:5 — with_all_your_heart', lambda: the_creed({'ask': 'with_all_your_heart'}, DATA), "with all your heart (6:5) — the two inclinations (Mishnah Berakhot 9:5; the Sifrei 32:2-4); 4:29's kin (OH by CALL)"),
    ('Deut 6:5; Berakhot 61b — with_all_your_soul', lambda: the_creed({'ask': 'with_all_your_soul'}, DATA), "with all your soul (6:5) — even if he takes your soul: the martyr's clause (R. Akiva, Berakhot 61b; Sanhedrin 74a)"),
    ('Deut 6:5; the Sifrei 32:7 — with_all_your_might', lambda: the_creed({'ask': 'with_all_your_might'}, DATA), "with all your might (6:5) — the Bible's one seat of the word: money, measure and thanks (9:5; the Sifrei 32:7); Onkelos 'your property'"),
    ('Deut 6:5; Sotah 31a — love_and_fear', lambda: the_creed({'ask': 'love_and_fear'}, DATA), "love and fear (6:5) — 'you shall love' the creed's command after its call; the one who acts from love greater (Sotah 31a; the Sifrei 32:1)"),
    # F3 — the_four_duties
    ('Deut 6:7; Mishnah Berakhot 1:1-2 — recite_when', lambda: the_four_duties({'ask': 'recite_when'}, DATA), "when to recite (6:7) — the evening from the priests' entering, the morning from blue against white: the times' table (Mishnah Berakhot 1:1-2; Berakhot 2a-2b) — the priest entering to eat his terumah begins it"),
    ('Deut 6:7; Mishnah Berakhot 1:3 — recite_how', lambda: the_four_duties({'ask': 'recite_how'}, DATA), 'how to recite (6:7) — in his way (Hillel: the times, not the postures; R. Tarfon rebuked, Mishnah Berakhot 1:3): the reader by the road holds'),
    ('shelf: Mishnah Berakhot 2:5 — recite_who', lambda: the_four_duties({'ask': 'recite_who'}, DATA), "who recites (6:7) — the bridegroom EXEMPT the first night (Mishnah Berakhot 2:5; Berakhot 16a); the mourner, women, slaves and minors the table's other rows"),
    ('shelf: Kiddushin 29b — daughters_exempt', lambda: the_four_duties({'ask': 'daughters_exempt'}, DATA), "the daughters (6:7) — 'your sons', not your daughters: the daughter EXEMPT from the teaching (Kiddushin 29b, 34a)"),
    ('Deut 6:6; Mishnah Berakhot 2:2 — the_passages', lambda: the_four_duties({'ask': 'the_passages'}, DATA), 'the passages (6:6) — three recited in order (Mishnah Berakhot 2:2), four bound (Menachot 3:7); two sets with two members each way, the ten words in neither (the Sifrei 34:2-3)'),
    ('Deut 6:7; Kiddushin 29a-30b — teach_your_sons', lambda: the_four_duties({'ask': 'teach_your_sons'}, DATA), "teach your sons (6:7) — the father's duty to teach Torah, the disciples 'sons' (the Sifrei 34:1; Kiddushin 29a-30b); sharp in the mouth (30a)"),
    ('Deut 6:8; Mishnah Menachot 3:7 — tefillin_passages', lambda: the_four_duties({'ask': 'tefillin_passages'}, DATA), "the tefillin's passages (6:8) — the four that say 'a sign upon your hand' (Menachot 3:7: each invalidates the others)"),
    ('Deut 6:8; the Sifrei 35:3-4 — tefillin_compartments', lambda: the_four_duties({'ask': 'tefillin_compartments'}, DATA), 'the compartments (6:8) — the hand one, the head FOUR: a PARAMETER (the Sifrei 35:3-4; Menachot 34b-35a; Sanhedrin 4b), its derivation from the spellings the open row (11:18 plene in the ink)'),
    ('Deut 6:8; Menachot 36b-37a — tefillin_arm', lambda: the_four_duties({'ask': 'tefillin_arm'}, DATA), "the arm (6:8) — the left, the weak hand (Menachot 36b-37a; the Sifrei 35:5-10); the left-handed on his right, the amputee's arm the table's row"),
    ('Deut 6:8; Menachot 36a — tefillin_order', lambda: the_four_duties({'ask': 'tefillin_order'}, DATA), 'the order (6:8) — the hand bound first, the head removed first (Menachot 36a; the Sifrei 35:11)'),
    ('Deut 6:8; Menachot 37a-b — tefillin_head', lambda: the_four_duties({'ask': 'tefillin_head'}, DATA), "the head (6:8) — the hairline, not between the eyes: the place of hair by 14:1's analogy (Menachot 37a-b; the Sifrei 35:12)"),
    ('Deut 6:9; Menachot 34a — mezuzah_writing', lambda: the_four_duties({'ask': 'mezuzah_writing'}, DATA), "the mezuzah's writing (6:9) — a scroll in ink with perfect letters, not the stones (Menachot 34a; Shabbat 103b; the Sifrei 36:1-2): the scroll-writer holds"),
    ('Deut 6:9; Menachot 33a-34a — mezuzah_doorpost', lambda: the_four_duties({'ask': 'mezuzah_doorpost'}, DATA), 'the doorpost (6:9) — one post, the right as one enters, the upper third (Menachot 33a-34a; the Sifrei 36:3-5)'),
    ('shelf: Yoma 11a — mezuzah_gates', lambda: the_four_duties({'ask': 'mezuzah_gates'}, DATA), "the gates (6:9) — the dwelling's, not the bathhouse's (Yoma 11a; the Sifrei 36:6-8): the bathhouse owner EXEMPT"),
    ('Deut 6:8-9; Menachot 43b — the_seven', lambda: the_four_duties({'ask': 'the_seven'}, DATA), 'the seven (6:8-9) — the head, the arm, four fringes, the mezuzah surround a man (Menachot 43b; the Sifrei 36:9): a DATA row'),
    ('the write — the_write', lambda: the_four_duties({'ask': 'the_write'}, DATA), "the write (6:4-9) — shema_commanded on Israel: the four duties standing from the chapter's own line"),
    # F4 — the_gift_and_the_warning
    ('Deut 6:10-11 — the_list', lambda: the_gift_and_the_warning({'ask': 'the_list'}, DATA), "the list (6:10-11) — cities, houses, cisterns, vineyards and olives 'which you did not …': a DATA row; the spoil permitted by 6:11 (the Sifrei 201:3) owed to the war chapter"),
    ('Deut 6:12 — lest_you_forget', lambda: the_gift_and_the_warning({'ask': 'lest_you_forget'}, DATA), "lest you forget (6:12) — obey_horeb's forgetting census (thirteen seats, 6:12 among them); the prohibition's seat 4:9 (OH by CALL)"),
    ('Deut 6:13; Temurah 3b-4a — fear_serve_swear', lambda: the_gift_and_the_warning({'ask': 'fear_serve_swear'}, DATA), "fear, serve, swear (6:13) — the true oath a positive clause (Temurah 3b-4a), its prohibition the third word's (DC by CALL); the true swearer holds"),
    ('Deut 6:14 — no_other_gods', lambda: the_gift_and_the_warning({'ask': 'no_other_gods'}, DATA), "no other gods (6:14) — the second word's clause: other_gods_barred stands from the giving (CH by CALL), no second write; the idolaters' companion the Tosefta's row"),
    ('Deut 6:15 — the_jealous_god', lambda: the_gift_and_the_warning({'ask': 'the_jealous_god'}, DATA), "the jealous God (6:15) — 4:24 and 5:9's word at its third Deuteronomy seat; the visiting's arms the second word's (CH by CALL); Onkelos the Shekhinah"),
    # F5 — the_test_and_the_right
    ('Deut 6:16; Arakhin 15a — you_shall_not_test', lambda: the_test_and_the_right({'ask': 'you_shall_not_test'}, DATA), "you shall not test (6:16) — Massah the tape's named line (Exodus 17:7), a run citation by name; the ten trials (Arakhin 15a; ES by CALL): the block test_barred on Israel"),
    ('Deut 6:17 — surely_keep', lambda: the_test_and_the_right({'ask': 'surely_keep'}, DATA), "surely keep (6:17) — the infinitive absolute (the book's three); the testimonies' three seats with 4:45's header (OH by CALL): no write"),
    ('Deut 6:18; Bava Metzia 108a — the_right_and_the_good', lambda: the_test_and_the_right({'ask': 'the_right_and_the_good'}, DATA), "the right and the good (6:18) — the abutter's rule (Bava Metzia 108a): the buyer of the adjoining field yields to the neighbor"),
    ('Deut 6:19 — thrust_out_enemies', lambda: the_test_and_the_right({'ask': 'thrust_out_enemies'}, DATA), "thrust out (6:19) — the enemies thrust out 'as the LORD has spoken': 9:4 forward, the manslayer's verb: a DATA note"),
    ('the write — the_write', lambda: the_test_and_the_right({'ask': 'the_write'}, DATA), "the write (6:16-19) — test_barred on Israel: the block at the chapter's second line"),
    # F6 — the_sons_question
    ('Deut 6:20; Pesachim 116a-b — the_four_askings', lambda: the_sons_question({'ask': 'the_four_askings'}, DATA), "the four askings (6:20) — the wise son's question, verbatim with Exodus 13:14 to 'saying' (the four sons, Pesachim 116a-b; PE by CALL)"),
    ('Deut 6:21-24 — the_answer_rows', lambda: the_sons_question({'ask': 'the_answer_rows'}, DATA), "the answer's rows (6:21-24) — the exodus retold in the first person plural: EXPANDED, SHORTENED, EXPANDED, EXPANDED against the tape's lines (T1); no second act"),
    ('Deut 6:25 — the_receipt', lambda: the_sons_question({'ask': 'the_receipt'}, DATA), "the receipt (6:25) — 'as he commanded us' without the Name: a run citation of the charge (5:31), VERBATIM in kind; the gate's finder blind, the pointer on file"),
    ('Deut 6:25 — righteousness_for_us', lambda: the_sons_question({'ask': 'righteousness_for_us'}, DATA), "righteousness for us (6:25) — Genesis 15:6's word at the answer's close; 24:13's pledge the kin; Onkelos 'merit': a DATA note"),
    ('Deut 6:1-25 — the_readback_table', lambda: the_sons_question({'ask': 'the_readback_table'}, DATA), 'the readback table — seven rows graded (VERBATIM 3, EXPANDED 3, SHORTENED 1); every row inside a law (T1); no row open'),
]


if __name__ == '__main__':
    ok = 0
    frac = {'INK': 0, 'MOVE': 0, 'DATA': 0, 'HYP': 0}
    used_effects = []
    print()
    for label, fn, want in CASES:
        got, effects, prov = fn()
        hit = got == want
        ok += hit
        kinds = [k for k, _ in prov]
        cls = 'HYP' if 'HYP' in kinds else ('INK' if all(k == 'INK' for k in kinds) else ('MOVE' if 'MOVE' in kinds else 'DATA'))
        frac[cls] += 1
        print('%s  [%s]  %s' % ('PASS' if hit else 'MISS', cls, label))
        if not hit:
            print('      expected: %s' % (want,))
            print('      got     : %s' % (got,))
        used_effects += effects
        for line in FX.render(effects):
            print('        ->%s' % line)
    print()
    print('WATCH COVERAGE (the wrap):')
    _W.print_coverage()
    print('MATRIX: %d/%d cells match the answer sheet' % (ok, len(CASES)))
    tot = len(CASES)
    print('FRACTIONS: pure ink %d/%d (%.0f%%) · named moves %d/%d (%.0f%%) · data %d/%d (%.0f%%) · hypotheses %d/%d (the H class, counted apart — never as compiled)' %
          (frac['INK'], tot, 100.0 * frac['INK'] / tot, frac['MOVE'], tot, 100.0 * frac['MOVE'] / tot, frac['DATA'], tot, 100.0 * frac['DATA'] / tot, frac['HYP'], tot))
    ops = FX.summarize(used_effects)
    print('LEDGER OPS this span writes:', ', '.join('%s x%d' % kv for kv in sorted(ops.items())))
    print('THE INK: the one number verse %s; no frame %s; the case tokens %s; the register singular-only %s, plural-only %s, both %s, the answer\'s first person plural %s; the imperatives %s; the infinitive absolute %s; the two plural prohibitions %s' % (sorted(PARSED.items()), DIV, dict(collections.Counter(x for l in CASE_TOK.values() for x in l)), SG_ONLY, PL_ONLY, BOTH, sorted(ONE_CP), IMPER, INFA, PROHIB))
    print('THE READBACK\'S THIRD FORM: %d rows — %s; every row inside a law %s; the deltas: the header %s; Massah %s; the going out %s; the plagues %s; the oath %s; the charge %s' % (len(READBACK), dict(RB_GRADES), all(r['law'] for r in READBACK), HEADER_DELTA, MASSAH_DELTA, OUT_DELTA, PLAGUE_DELTA, OATH_DELTA, CHARGE_DELTA))
    print('THE SPELLINGS (the open row): %s; the sign\'s four seats %s' % (FRONT, SIGN))
    print('THE RECEIPT WITHOUT THE NAME: %s (the finder blind — CO6)' % (RECEIPT_NO_NAME,))
    print('THE CALLEES: the trials %s / %s; the forgetting %d seats; the vain oath %s; the firstborn %s; the oath lines %s / %s / %s; the charge %s' % (ES_TEN['v'], ES_SIX['v'], len(OH.FORGET), DC_VO[:2], PE_HUMAN[0][:20], MA_TEST['v'], MA_FAM['v'], JS_KT['v'], ER_TORAH['v']))
    print('THE SCENE on the bench: %s; the exempt arms %s; the timers (set, fired, cancelled, pending) %s; entities %d; closes %d' % (SCENE[0], SCENE[1], SCENE[2], SCENE[3], SCENE[4]))
    print('THE NARRATIVE: %s' % (NARRATIVE,))
    print('THE PARAMETER ROWS: ' + '; '.join('%s = %s' % (k, DATA[k]['value'] if k != 'the_readback' else '%d rows' % len(DATA[k]['value'])) for k in DATA) + ' (the other settings recorded in DATA)')
    if ok == len(CASES):
        print('\nTHE COMPILE OF CHAPTER 6: the answer sheet REPRODUCED — %d/%d' % (ok, len(CASES)))
    sys.exit(0 if ok == len(CASES) else 1)

#!/usr/bin/env python3
# DEUTERONOMY 5:1-33 — THE COVENANT AT HOREB RETOLD: THE SECOND COPY OF THE TEN WORDS, THE VOICE AND THE TABLETS, THE REQUEST FOR A MEDIATOR AND
# THE ANSWER (THE DEUTERONOMY WALK sitting 3b, 2026-09-16; World/step9/DEUTERONOMY_WALK.md "Sitting 3b"; the state doc's #188). THE LAWS' READBACK
# — THE FIRST FORM (R1)-(R6) ON LAW (THE_LOOP.md step 6, its laws' half): the DATA table the_readback carries SIXTEEN law rows (one per verse of the
# code, 5:6-21) graded against THE RUNNER'S CELL THAT COMPILES EACH WORD — VERBATIM / VARIANT (a spelling or a conjunction moved, the sense unchanged
# — the new grade) / EXPANDED / TURNED — and FIVE narrative rows (EXPANDED / SUPPLIED / TURNED), the deltas RECOMPUTED from the DB; THE CODE'S HOLE
# FOUND — no runner compiled the SECOND word (no other gods, no image, no bowing) nor the TENTH (covet, desire): both compiled HERE from both copies'
# ink (F2, F5), their BLOCKS written on Israel AT THE CODE'S OWN LINE (2b's supplied ten_words_declared, dated (1, 3, 7)), never at the retelling's;
# THE TAPE'S SECOND HOLE FOUND — no line for Exodus 20:18-21 (the people's request): the request (5:23-27) and the answer (5:28-31, told only here)
# two SUPPLIED lines written ONCE at their own time by ONE retrograde marker at Deut 5:23 (the giving's day), a forward marker at 5:32 ending the
# stretch; THE CHARGE TO TEACH a DEBIT on Moses CLOSED AT ONCE BY THE PRIOR RUN (the closer Deut 1:1-5's expounding — the book itself the run);
# "return to your tents" a STATUS on Israel (the separation of Exodus 19:15 released); the receipts INSIDE the code (5:12, 5:16; 5:32 the plural)
# RUN CITATIONS of the giving — the register seats CHAPTER, the teacher reading them as Marah (Sanhedrin 56b). The daemon law_covenant_at_horeb
# given_at Exodus 20:3 (the second word's first giving), installed_by covenant_blood_thrown (law_decalogue's own installer). Seven cells; every
# token probed (zero-report law); effects on every cell (the effects law); the parameters the ink leaves open recorded in DATA with their arms;
# twenty DATA rows. Reading ledger: logic/oral_triage/deu_05_vaetchanan_2026-09-16.md (38 sources, 6 claims); the exam's docket:
# logic/oral_triage/deu_05_vaetchanan_exam_2026-09-16.md (275 rows: LAW 77 / DERIVATION 19 / DISPUTE 14 / CONTEXT 165).

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
import cold_run_decalogue as DC               # THE EDGE: covenant_at_horeb -> decalogue CALL, reference (the third, fourth and eighth words' cells; 'vain and false in one utterance'; the second and the tenth words have NO cell there — compiled here)
import cold_run_obey_horeb as OH              # THE EDGE: covenant_at_horeb -> obey_horeb CALL, reference (5:22's ten words and tablets FOUND — 2b's supplied lines; the no-image list; the readback's second chapter)
import cold_run_erection as ER                # THE EDGE: covenant_at_horeb -> erection CALL, reference (the covenant's book and blood; 'speech with speech'; the ten words' seats; 'to teach them' — the charge's debit)
import cold_run_exodus_story as ES            # THE EDGE: covenant_at_horeb -> exodus_story CALL, reference (Rabbi Yose's days — the marker at 5:23; 'we will do' seats; the tub; Marah's statutes — the receipts' teacher)
import cold_run_opening_speech as OS          # THE EDGE: covenant_at_horeb -> opening_speech CALL, reference (1:22 and 1:34 read again; the frame's write the charge's closer; the readback's first form)
import cold_run_holiness as HO                # THE EDGE: covenant_at_horeb -> holiness CALL, reference (the fifth word's cell at Leviticus 19:3 — the honor and the fear defined, the order, the three partners, the woman)
import cold_run_mishpatim_3 as M3             # THE EDGE: covenant_at_horeb -> mishpatim_3 CALL, reference (the sixth word's code at 21:12-14; the parents' striker and curser)
import cold_run_sanctions as SA               # THE EDGE: covenant_at_horeb -> sanctions CALL, reference (the seventh word's code at Leviticus 20:10; the curser at 20:9)
import cold_run_refuge as RF                  # THE EDGE: covenant_at_horeb -> refuge CALL, reference (the murderer's definition at Numbers 35)
import cold_run_ordinances as OR              # THE EDGE: covenant_at_horeb -> ordinances CALL, reference (the ninth word's kin at 23:1 — the false report, the witness of violence)
import cold_run_pre_sinai as PS               # THE EDGE: covenant_at_horeb -> pre_sinai CALL, reference (the creation ground of 20:11 — the fourth word's two grounds; procreation repeated at Sinai)

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
def W5(v): return words('Deut', 5, v)
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
def letters(b, c, lo, hi): return sum(len(x) for v in range(lo, hi + 1) for x in words(b, c, v))
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

# ---- THE INK, computed (the parser and the tokens; the reading's facts the expectations — every assert PROVEN at the reading, ch5_ink.py) ----
SPAN = [(5, v) for v in range(1, 34)]
PARSED = {(c, v): ink_numbers(verse_words('Deut', c, v)) for (c, v) in SPAN if ink_numbers(verse_words('Deut', c, v))}
assert PARSED == {(5, 13): [6], (5, 22): [2]} and {(c, v): ink_ordinals(verse_words('Deut', c, v)) for (c, v) in SPAN if ink_ordinals(verse_words('Deut', c, v))} == {(5, 14): [7]}, PARSED   # THREE number verses in thirty-three, no gap
assert [((c, v), t) for (c, v) in SPAN for t in verse_words('Deut', c, v) if t[-1] in '#~^%@|*'] == [((5, 9), 'שלשים*'), ((5, 22), 'שני^')]   # the third generation STARRED (not thirty); the construct "two"
assert ink_numbers(verse_words('Exod', 20, 9)) == [6] and ink_ordinals(verse_words('Exod', 20, 10)) == [7] and ink_numbers(verse_words('Exod', 20, 11)) == [6] and ink_numbers(verse_words('Deut', 4, 13)) == [10, 2] and ink_numbers(verse_words('Exod', 31, 18)) == [2]
SIX_DAYS, TWO_TABLETS, SEVENTH = PARSED[(5, 13)][0], PARSED[(5, 22)][0], 7
TOK = sum(len(by[('Deut', 5, v)]) for v in range(1, 34)); assert TOK == 472, TOK
assert byw[('Deut', 5, 10)] == [None] * 5 + ['x-ketiv'] and W5(10)[-1] == 'מצותו' and words('Exod', 20, 6)[-1] == 'מצותי' and Counter(wt for v in range(1, 34) for wt in byw[('Deut', 5, v)]) == Counter({None: 471, 'x-ketiv': 1})   # THE KETIV AT 5:10: the written "his", Exodus's "my"
# THE FRAMES AND THE REGISTER
DIV = [(c, v) for (c, v) in SPAN if any(W5(v)[i] in ('ויאמר', 'וידבר') and W5(v)[i + 1] == 'יהוה' for i in range(len(W5(v)) - 1))]
assert DIV == [(5, 28)] and len(P('ויאמר', 'יהוה', 'אלי', books=('Deut',))) == 11 and [(c, v) for (c, v) in SPAN if 'לאמר' in W5(v)] == [(5, 5)]
REG = {v: [x for x, m in by[('Deut', 5, v)] if m and re.search(r'V.w', m)] for v in range(1, 34) if any(m and re.search(r'V.w', m) for x, m in by[('Deut', 5, v)])}
assert REG == {1: ['ויקרא', 'ויאמר'], 15: ['ויצאך'], 22: ['ויכתבם', 'ויתנם'], 23: ['ויהי', 'ותקרבון'], 24: ['ותאמרו'], 26: ['ויחי'], 28: ['וישמע', 'ויאמר']}, REG
CASE_TOK = {f'{c}:{v}': [x for x in W5(v) if x in ('כי', 'אם', 'ואם', 'או', 'פן', 'ופן')] for (c, v) in SPAN if any(x in ('כי', 'אם', 'ואם', 'או', 'פן', 'ופן') for x in W5(v))}
assert CASE_TOK == {'5:3': ['כי'], '5:5': ['כי'], '5:9': ['כי'], '5:11': ['כי'], '5:15': ['כי'], '5:24': ['כי'], '5:25': ['כי', 'אם'], '5:26': ['כי']} and Counter(x for l in CASE_TOK.values() for x in l) == Counter({'כי': 8, 'אם': 1}), CASE_TOK
NUM2 = {v: (sum(1 for _, m in by[('Deut', 5, v)] if m and '2mp' in m), sum(1 for _, m in by[('Deut', 5, v)] if m and '2ms' in m)) for v in range(1, 34)}
SG_ONLY = [v for v, (p, s) in NUM2.items() if s and not p]; PL_ONLY = [v for v, (p, s) in NUM2.items() if p and not s]; BOTH = [v for v, (p, s) in NUM2.items() if p and s]; NEITHER = [v for v, (p, s) in NUM2.items() if not p and not s]
assert SG_ONLY == [6, 7, 8, 9, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 27, 31] and PL_ONLY == [4, 5, 22, 23, 24, 32, 33] and BOTH == [1, 28, 30] and NEITHER == [2, 3, 10, 25, 26, 29], (SG_ONLY, PL_ONLY, BOTH, NEITHER)   # THE TEN WORDS IN THE SINGULAR
IMPER = {v: [(x, m) for x, m in by[('Deut', 5, v)] if m and re.match(r'^HV.v', m)] for v in range(1, 34) if any(m and re.match(r'^HV.v', m) for _, m in by[('Deut', 5, v)])}
assert IMPER == {1: [('שמע', 'HVqv2ms')], 27: [('קרב', 'HVqv2ms')], 30: [('לך', 'HVqv2ms'), ('אמר', 'HVqv2ms'), ('שובו', 'HVqv2mp')], 31: [('עמד', 'HVqv2ms')]}, IMPER
INFA = {v: [(x, m) for x, m in by[('Deut', 5, v)] if m and re.match(r'^HV.a', m)] for v in range(1, 34) if any(m and re.match(r'^HV.a', m) for _, m in by[('Deut', 5, v)])}
assert INFA == {12: [('שמור', 'HVqa')], 16: [('כבד', 'HVpa')]} and wm('Exod', 20, 8)[0] == ('זכור', 'HVqa') and wm('Exod', 20, 12)[0] == ('כבד', 'HVpa'), INFA   # KEEP and HONOR the infinitive absolutes; REMEMBER the first copy's
PROHIB = {v: [x for i, (x, m) in enumerate(by[('Deut', 5, v)]) if i and by[('Deut', 5, v)][i - 1][0] in ('לא', 'ולא') and m and m.startswith('HV') and 'i2' in m] for v in range(1, 34)}
PROHIB = {v: l for v, l in PROHIB.items() if l}
assert PROHIB == {8: ['תעשה'], 9: ['תשתחוה', 'תעבדם'], 11: ['תשא'], 14: ['תעשה'], 17: ['תרצח'], 18: ['תנאף'], 19: ['תגנב'], 20: ['תענה'], 21: ['תחמד', 'תתאוה'], 32: ['תסרו']} and sum(len(l) for l in PROHIB.values()) == 12, PROHIB
YG_SG = [v for v in range(1, 34) for i in range(len(W5(v)) - 1) if W5(v)[i:i + 2] == ['יהוה', 'אלהיך']]; YG_PL = [v for v in range(1, 34) for i in range(len(W5(v)) - 1) if W5(v)[i:i + 2] == ['יהוה', 'אלהיכם']]
assert YG_SG == [6, 9, 11, 12, 15, 15, 16, 16] and YG_PL == [32, 33] and [v for v in range(1, 34) for i in range(len(W5(v)) - 1) if W5(v)[i:i + 2] == ['יהוה', 'אלהינו']] == [2, 24, 25, 27, 27]
NAME = Counter(x for v in range(1, 34) for x in W5(v) if x in ('יהוה', 'ויהוה', 'ביהוה', 'כיהוה', 'ליהוה'))
assert NAME == Counter({'יהוה': 23, 'ליהוה': 1}) and sum(NAME.values()) == 24 and [v for v in range(1, 34) if 'משה' in W5(v)] == [1]
assert [(x, m) for x, m in by[('Deut', 5, 28)] if m and '1cs' in m] == [('אלי', 'HR/Sp1cs'), ('אלי', 'HR/Sp1cs'), ('שמעתי', 'HVqp1cs')] and [(x, m) for x, m in by[('Deut', 5, 31)] if m and '1cs' in m] == [('עמדי', 'HR/Sp1cs'), ('ואדברה', 'HC/Vph1cs'), ('אנכי', 'HPp1cs')]
# F1's facts: the assembly called, the covenant, face in face, the mediator
assert P('ויקרא', 'משה', 'אל', 'כל', 'ישראל') == S_('Deut 29:1', 'Deut 5:1') and len(P('ויקרא', 'משה')) == 7 and P('שמע', 'ישראל') == S_('Deut 20:3', 'Deut 5:1', 'Deut 6:4', 'Deut 9:1') and wm('Deut', 5, 1)[7] == ('שמע', 'HVqv2ms')
assert P('אשר', 'אנכי', 'דבר', 'באזניכם', 'היום') == ['Deut 5:1'] and U('באזניכם') == S_('Deut 5:1', 'Jer 26:11', 'Jer 26:15', 'Job 13:17') and P('ולמדתם', 'אתם') == S_('Deut 11:19', 'Deut 5:1') and P('ושמרתם', 'לעשתם') == ['Deut 5:1'] and sorted(set(P('ושמרתם', 'לעשות')) | set(P('ושמרת', 'לעשות'))) == S_('Deut 11:32', 'Deut 17:10', 'Deut 5:32', 'Deut 6:3')
assert len(P('יהוה', 'אלהינו', books=('Deut',))) == 20 and P('כרת', 'עמנו', 'ברית') == ['Deut 5:2'] and P('לא', 'את', 'אבתינו') == ['Deut 5:3'] and U('אבתינו', books=T) == S_('Deut 26:7', 'Deut 5:3', 'Gen 46:34', 'Num 20:15', 'Num 36:3', 'Num 36:4')
assert P('הברית', 'הזאת', books=T) == S_('Deut 29:13', 'Deut 29:8', 'Deut 5:3') and P('כי', 'אתנו') == ['Deut 5:3'] and P('פה', 'היום') == S_('Deut 12:8', 'Deut 5:3') and P('כלנו', 'חיים') == ['Deut 5:3'] and lemma_of('Deut', 5, 2, 'בחרב') == ['2722'] and morphs('Deut', 5, 2)[5] == 'HR/Np'
assert P('פנים', 'בפנים') == ['Deut 5:4'] and P('פנים', 'אל', 'פנים') == S_('Deut 34:10', 'Exod 33:11', 'Ezek 20:35', 'Gen 32:31', 'Judg 6:22') and P('דבר', 'יהוה', 'עמכם') == S_('Deut 5:4', 'Deut 9:10') and P('בהר', 'מתוך', 'האש') == S_('Deut 10:4', 'Deut 5:22', 'Deut 5:4', 'Deut 9:10') and len(P('מתוך', 'האש')) == 11
assert P('אנכי', 'עמד', 'בין') == ['Deut 5:5'] and P('עמד', 'בין') == S_('1Chr 21:16', 'Deut 5:5', 'Zech 1:8') and len(P('בעת', 'ההוא', books=('Deut',))) == 15 and P('להגיד', 'לכם') == ['Deut 5:5'] and P('כי', 'יראתם') == ['Deut 5:5'] and P('מפני', 'האש') == S_('Deut 5:5', 'Mic 1:4') and P('ולא', 'עליתם', 'בהר') == ['Deut 5:5']
FRAME_DIFF = (LEN('Deut', 5, 1), LEN('Deut', 4, 1), len(SHARED(('Deut', 5, 1), ('Deut', 4, 1))), LEN('Deut', 5, 3), LEN('Deut', 29, 13), len(SHARED(('Deut', 5, 3), ('Deut', 29, 13))))
# F3/F4's facts: THE TWO COPIES DIFFED (the sixteen rows' deltas — computed, the reading's asserts reused)
assert DIFF(('Deut', 5, 6), ('Exod', 20, 2)) == [] and DIFF(('Deut', 5, 7), ('Exod', 20, 3)) == [] and DIFF(('Deut', 5, 11), ('Exod', 20, 7)) == [] and DIFF(('Deut', 5, 13), ('Exod', 20, 9)) == [] and DIFF(('Deut', 5, 17), ('Exod', 20, 13)) == []   # FIVE VERBATIM
assert DIFF(('Deut', 5, 8), ('Exod', 20, 4)) == [('replace', ['כל'], ['וכל'])] and DIFF(('Deut', 5, 9), ('Exod', 20, 5)) == [('replace', ['אבות'], ['אבת']), ('replace', ['ועל'], ['על'])] and DIFF(('Deut', 5, 10), ('Exod', 20, 6)) == [('replace', ['מצותו'], ['מצותי'])]
assert DIFF(('Deut', 5, 12), ('Exod', 20, 8)) == [('replace', ['שמור'], ['זכור']), ('delete', ['כאשר', 'צוך', 'יהוה', 'אלהיך'], [])] and DIFF(('Deut', 5, 14), ('Exod', 20, 10)) == [('replace', ['ועבדך'], ['עבדך']), ('replace', ['ושורך', 'וחמרך', 'וכל', 'בהמתך'], ['ובהמתך']), ('delete', ['למען', 'ינוח', 'עבדך', 'ואמתך', 'כמוך'], [])]
assert SHARED(('Deut', 5, 15), ('Exod', 20, 11)) == ['את', 'יום', 'השבת'] and [op for op, _, _ in DIFF(('Deut', 5, 15), ('Exod', 20, 11))] == ['delete', 'replace', 'replace', 'replace', 'delete', 'insert'] and DIFF(('Deut', 5, 16), ('Exod', 20, 12)) == [('delete', ['כאשר', 'צוך', 'יהוה', 'אלהיך'], []), ('replace', ['יאריכן'], ['יארכון']), ('delete', ['ולמען', 'ייטב', 'לך'], [])]
assert all(DIFF(('Deut', 5, v), ('Exod', 20, v - 4)) == [('replace', ['ולא'], ['לא'])] for v in (18, 19)) and DIFF(('Deut', 5, 20), ('Exod', 20, 16)) == [('replace', ['ולא'], ['לא']), ('replace', ['שוא'], ['שקר'])]
assert DIFF(('Deut', 5, 21), ('Exod', 20, 17)) == [('replace', ['ולא'], ['לא', 'תחמד', 'בית', 'רעך', 'לא']), ('delete', ['ולא', 'תתאוה', 'בית', 'רעך', 'שדהו'], []), ('replace', ['שורו'], ['ושורו'])]
COPIES = ((sum(len(words('Exod', 20, v)) for v in range(2, 18)), letters('Exod', 20, 2, 17)), (sum(len(W5(v)) for v in range(6, 22)), letters('Deut', 5, 6, 21)))
assert COPIES == ((172, 620), (189, 708)), COPIES
WORD_TOK = [(v, v - 4, LEN('Exod', 20, v - 4), LEN('Deut', 5, v)) for v in range(6, 22)]
assert WORD_TOK == [(6, 2, 9, 9), (7, 3, 7, 7), (8, 4, 16, 16), (9, 5, 21, 21), (10, 6, 6, 6), (11, 7, 17, 17), (12, 8, 5, 9), (13, 9, 6, 6), (14, 10, 18, 26), (15, 11, 26, 23), (16, 12, 15, 22), (17, 13, 2, 2), (18, 14, 2, 2), (19, 15, 2, 2), (20, 16, 5, 5), (21, 17, 15, 16)], WORD_TOK
assert P('אנכי', 'יהוה', 'אלהיך') == S_('Deut 5:6', 'Deut 5:9', 'Exod 20:2', 'Exod 20:5', 'Ps 81:11') and len(sorted(set(P('מבית', 'עבדים')) | set(P('בית', 'עבדים')))) == 12 and (len(P('אלהים', 'אחרים', books=T)), len(P('אלהים', 'אחרים', books=('Deut',)))) == (19, 17) and P('אלהים', 'אחרים', 'על', 'פני') == S_('Deut 5:7', 'Exod 20:3')
assert len(U('פסל', 'ופסל', books=T)) == 9 and P('פסל', 'וכל', 'תמונה') == ['Exod 20:4'] and P('פסל', 'כל', 'תמונה') == ['Deut 5:8'] and len(P('בשמים', 'ממעל')) == 5 and P('במים', 'מתחת', 'לארץ') == S_('Deut 4:18', 'Deut 5:8', 'Exod 20:4') and P('לא', 'תשתחוה', 'להם', 'ולא', 'תעבדם') == S_('Deut 5:9', 'Exod 20:5')
assert P('אל', 'קנא') == S_('Deut 4:24', 'Deut 5:9', 'Deut 6:15', 'Exod 20:5', 'Exod 34:14') and P('פקד', 'עון', 'אבות', 'על', 'בנים') == S_('Deut 5:9', 'Exod 34:7', 'Num 14:18') and P('על', 'שלשים', 'ועל', 'רבעים') == S_('Exod 20:5', 'Exod 34:7', 'Num 14:18') and U('לשנאי') == S_('Deut 5:9', 'Exod 20:5')
assert LEMV('8029') == S_('Deut 5:9', 'Exod 20:5', 'Exod 34:7', 'Gen 50:23', 'Num 14:18') and all(PT(*[s.split()[0], *map(int, s.split()[1].split(':'))], 'שלשים') == ['שִׁלֵּשִׁים'] for s in LEMV('8029')) and lemma_of('Deut', 5, 10, 'לאלפים') == ['505'] and morphs('Deut', 5, 10)[2] == 'HR/Acbpa'
assert U('לאלפים') == S_('Deut 5:10', 'Exod 20:6', 'Exod 34:7', 'Jer 32:18') and P('לאהבי', 'ולשמרי', 'מצותי') == ['Exod 20:6'] and P('לאהבי', 'ולשמרי', 'מצותו') == ['Deut 5:10'] and U('מצותו') == S_('Deut 27:10', 'Deut 5:10', 'Deut 7:9', 'Deut 8:2', 'Num 15:31')
assert len(U('לשוא')) == 9 and len(P('לא', 'ינקה')) == 12 and P('שמור', 'את', 'יום', 'השבת') == ['Deut 5:12'] and P('זכור', 'את', 'יום', 'השבת') == ['Exod 20:8'] and len(U('לקדשו')) == 6
RECEIPT_SG = P('כאשר', 'צוך', 'יהוה', 'אלהיך'); RECEIPT_PL = P('כאשר', 'צוה', 'יהוה', 'אלהיכם', 'אתכם')
assert RECEIPT_SG == S_('Deut 20:17', 'Deut 5:12', 'Deut 5:16') and P('כאשר', 'צוך') == RECEIPT_SG and RECEIPT_PL == ['Deut 5:32']   # THE RECEIPT INSIDE THE CODE (5:12, 5:16), its plural (5:32) — the register's three seats
assert P('ששת', 'ימים', 'תעבד') == S_('Deut 5:13', 'Exod 20:9', 'Exod 34:21') and P('ושורך', 'וחמרך', 'וכל', 'בהמתך') == ['Deut 5:14'] and P('וגרך', 'אשר', 'בשעריך') == S_('Deut 31:12', 'Deut 5:14', 'Exod 20:10') and P('למען', 'ינוח', 'עבדך', 'ואמתך') == ['Deut 5:14'] and len(U('ינוח')) == 8 and len(U('כמוך', books=T)) == 7
assert P('וזכרת', 'כי', 'עבד', 'היית') == S_('Deut 15:15', 'Deut 16:12', 'Deut 24:18', 'Deut 24:22', 'Deut 5:15') and U('ויצאך') == ['Deut 5:15'] and P('ביד', 'חזקה', 'ובזרע', 'נטויה') == S_('Deut 26:8', 'Deut 5:15') and P('על', 'כן', 'צוך', 'יהוה', 'אלהיך') == ['Deut 5:15'] and P('לעשות', 'את', 'יום', 'השבת') == ['Deut 5:15'] and P('כי', 'ששת', 'ימים', 'עשה', 'יהוה') == S_('Exod 20:11', 'Exod 31:17')
assert P('כבד', 'את', 'אביך', 'ואת', 'אמך') == S_('Deut 5:16', 'Exod 20:12') and P('למען', 'יאריכן', 'ימיך') == ['Deut 5:16'] and P('למען', 'יארכון', 'ימיך') == ['Exod 20:12'] and P('ולמען', 'ייטב', 'לך') == ['Deut 5:16'] and P('על', 'האדמה', 'אשר', 'יהוה', 'אלהיך', 'נתן', 'לך') == S_('Deut 25:15', 'Deut 4:40', 'Deut 5:16', 'Exod 20:12')
assert P('לא', 'תרצח') == S_('Deut 5:17', 'Exod 20:13') and U('תנאף') == S_('Deut 5:18', 'Exod 20:14') and U('תגנב') == S_('Deut 5:19', 'Exod 20:15') and P('לא', 'תגנבו') == ['Lev 19:11'] and P('עד', 'שוא') == ['Deut 5:20'] and P('עד', 'שקר') == S_('Deut 19:18', 'Exod 20:16', 'Prov 14:5', 'Prov 25:18', 'Prov 6:19') and U('שוא', 'לשוא', books=T) == S_('Deut 5:11', 'Deut 5:20', 'Exod 20:7', 'Exod 23:1')
assert U('תחמד') == S_('Deut 5:21', 'Deut 7:25', 'Exod 20:17', 'Prov 6:25') and P('ולא', 'תחמד') == ['Deut 5:21'] and P('אשת', 'רעך') == S_('Deut 5:21', 'Exod 20:17') and U('תתאוה') == ['Deut 5:21'] and len(LEMV('183')) == 25 and 'Num 11:4' in LEMV('183') and P('בית', 'רעך') == S_('Deut 5:21', 'Exod 20:17')
assert len(U('שדהו')) == 6 and P('שורו', 'וחמרו') == ['Deut 5:21'] and P('וכל', 'אשר', 'לרעך') == S_('Deut 5:21', 'Exod 20:17') and sum(W5(v).count(t) for v in range(1, 34) for t in ('רעך', 'ברעך', 'לרעך')) == 4
# F6's facts: the voice and the tablets, the request
assert P('את', 'הדברים', 'האלה', 'דבר', 'יהוה') == ['Deut 5:22'] and P('אל', 'כל', 'קהלכם') == ['Deut 5:22'] and U('קהלכם') == ['Deut 5:22'] and P('האש', 'הענן', 'והערפל') == ['Deut 5:22'] and len(P('קול', 'גדול')) == 9
assert P('ולא', 'יסף') == S_('1Sam 15:35', 'Deut 5:22', 'Gen 38:26', 'Judg 13:21') and [(s, m) for s, x, m in LEMT('3254') if x == 'יסף' and m == 'HVqp3ms'] == [('1Sam 15:35', 'HVqp3ms'), ('Deut 5:22', 'HVqp3ms'), ('Gen 38:26', 'HVqp3ms'), ('Jer 45:3', 'HVqp3ms'), ('Judg 13:21', 'HVqp3ms')]
assert sorted(set(P('שני', 'לחת', 'אבנים')) | set(P('שני', 'לחת', 'האבנים')) | set(P('שני', 'לחות', 'אבנים'))) == S_('Deut 10:3', 'Deut 4:13', 'Deut 5:22', 'Deut 9:11', 'Exod 34:1', 'Exod 34:4') and P('ויתנם', 'אלי') == ['Deut 5:22'] and SHARED(('Deut', 5, 22), ('Deut', 4, 13)) == ['ויכתבם', 'על', 'שני'] and PT('Deut', 5, 22, 'לחת') == ['לֻחֹת']
assert P('כשמעכם', 'את', 'הקול') == ['Deut 5:23'] and P('מתוך', 'החשך') == ['Deut 5:23'] and P('וההר', 'בער', 'באש') == S_('Deut 4:11', 'Deut 5:23', 'Deut 9:15') and P('ותקרבון', 'אלי') == S_('Deut 1:22', 'Deut 5:23') and U('ותקרבון') == S_('Deut 1:22', 'Deut 4:11', 'Deut 5:23') and SHARED(('Deut', 5, 23), ('Deut', 1, 22)) == ['ותקרבון', 'אלי']
assert P('ראשי', 'שבטיכם') == S_('Deut 1:15', 'Deut 5:23') and U('וזקניכם') == ['Deut 5:23'] and U('ותאמרו', books=('Deut',)) == S_('Deut 1:14', 'Deut 1:22', 'Deut 1:27', 'Deut 1:41', 'Deut 5:24') and P('הן', 'הראנו', 'יהוה', 'אלהינו') == ['Deut 5:24'] and P('את', 'כבדו', 'ואת', 'גדלו') == ['Deut 5:24']
assert P('ואת', 'קלו', 'שמענו', 'מתוך', 'האש') == ['Deut 5:24'] and P('כי', 'ידבר', 'אלהים', 'את', 'האדם', 'וחי') == ['Deut 5:24'] and P('למה', 'נמות') == S_('Deut 5:25', 'Gen 47:19') and P('האש', 'הגדלה', 'הזאת') == S_('Deut 18:16', 'Deut 5:25') and U('יספים') == ['Deut 5:25'] and U('ומתנו') == S_('1Kgs 17:12', '2Kgs 7:4', 'Deut 5:25')
assert P('כי', 'מי', 'כל', 'בשר') == ['Deut 5:26'] and P('אלהים', 'חיים') == S_('1Sam 17:26', '1Sam 17:36', 'Deut 5:26', 'Jer 10:10', 'Jer 23:36') and P('מדבר', 'מתוך', 'האש') == S_('Deut 4:33', 'Deut 5:26') and P('כמנו', 'ויחי') == ['Deut 5:26'] and SHARED(('Deut', 5, 26), ('Deut', 4, 33)) == ['מדבר', 'מתוך', 'האש']
assert P('קרב', 'אתה', 'ושמע') == ['Deut 5:27'] and [s for s, x, m in LEMT('7126') if x == 'קרב' and m and m.startswith('HVqv')] == S_('2Sam 20:16', 'Deut 5:27', 'Isa 65:5', 'Lev 9:7') and P('ואת', 'תדבר', 'אלינו') == ['Deut 5:27'] and P('ושמענו', 'ועשינו') == ['Deut 5:27'] and P('נעשה', 'ונשמע') == ['Exod 24:7'] and P('אשר', 'דבר', 'יהוה', 'נעשה') == S_('Exod 19:8', 'Exod 24:3', 'Exod 24:7')
assert words('Exod', 20, 18)[:4] == ['וכל', 'העם', 'ראים', 'את'] and words('Exod', 20, 19)[:5] == ['ויאמרו', 'אל', 'משה', 'דבר', 'אתה'] and words('Exod', 20, 21)[:2] == ['ויעמד', 'העם'] and words('Exod', 20, 22)[-5:] == ['כי', 'מן', 'השמים', 'דברתי', 'עמכם']   # the request's first telling and the LORD's other answer
# F7's facts: the answer and the charge
assert P('וישמע', 'יהוה', 'את', 'קול', 'דבריכם') == S_('Deut 1:34', 'Deut 5:28') and SHARED(('Deut', 5, 28), ('Deut', 1, 34)) == ['וישמע', 'יהוה', 'את', 'קול', 'דבריכם'] and P('שמעתי', 'את', 'קול', 'דברי', 'העם', 'הזה') == ['Deut 5:28'] and P('היטיבו', 'כל', 'אשר', 'דברו') == ['Deut 5:28'] and U('היטיבו') == S_('Deut 18:17', 'Deut 5:28', 'Hos 10:1', 'Jer 26:13', 'Jer 7:3', 'Ps 33:3')
assert len(P('מי', 'יתן')) == 17 and len([s for s in P('מי', 'יתן') if s.startswith('Job')]) == 9 and P('מי', 'יתן', 'והיה', 'לבבם', 'זה', 'להם') == ['Deut 5:29'] and P('ליראה', 'אתי') == S_('Deut 4:10', 'Deut 5:29') and U('לעלם', books=('Deut',)) == S_('Deut 32:40', 'Deut 5:29')
assert P('לך', 'אמר', 'להם') == ['Deut 5:30'] and P('שובו', 'לכם', 'לאהליכם') == ['Deut 5:30'] and U('לאהליכם') == S_('Deut 5:30', 'Josh 22:4') and P('ואתה', 'פה', 'עמד', 'עמדי') == ['Deut 5:31'] and len(U('עמדי', books=T)) == 20 and P('ואדברה', 'אליך') == S_('2Sam 20:16', 'Deut 5:31')
assert P('את', 'כל', 'המצוה', 'והחקים', 'והמשפטים') == ['Deut 5:31'] and P('המצוה', 'החקים', 'והמשפטים') == ['Deut 6:1'] and P('אשר', 'תלמדם') == ['Deut 5:31'] and P('אשר', 'אנכי', 'נתן', 'להם', 'לרשתה') == ['Deut 5:31'] and words('Exod', 24, 12)[-1] == 'להורתם' and P('ללמד', 'אתכם') == S_('Deut 4:14', 'Deut 6:1')
assert P('ושמרתם', 'לעשות', 'כאשר', 'צוה', 'יהוה', 'אלהיכם', 'אתכם') == ['Deut 5:32'] and P('לא', 'תסרו', 'ימין', 'ושמאל') == ['Deut 5:32'] and P('ימין', 'ושמאל') == S_('Deut 17:11', 'Deut 5:32') and U('תסרו') == ['Deut 5:32'] and SHARED(('Deut', 5, 32), ('Deut', 17, 11)) == ['ימין', 'ושמאל']
assert len(P('בכל', 'הדרך')) == 6 and P('אשר', 'צוה', 'יהוה', 'אלהיכם', 'אתכם', 'תלכו') == ['Deut 5:33'] and len(U('תחיון', 'תחיו')) == 6 and P('וטוב', 'לכם') == ['Deut 5:33'] and P('והארכתם', 'ימים') == ['Deut 5:33'] and U('תירשון') == ['Deut 5:33']
assert words('Deut', 1, 5)[:5] == ['בעבר', 'הירדן', 'בארץ', 'מואב', 'הואיל'] and words('Deut', 4, 5)[:2] == ['ראה', 'למדתי'] and words('Deut', 18, 17)[:5] == ['ויאמר', 'יהוה', 'אלי', 'היטיבו', 'אשר']   # the charge's run (1:5, 4:5) and the answer cited forward (18:17)
# THE RETELLINGS' DELTAS RECOMPUTED (the narrative rows' measures — the token counts and the longest shared run, from the DB)
VOICE_DELTA = (LEN('Deut', 5, 22), LEN('Deut', 4, 13), len(SHARED(('Deut', 5, 22), ('Deut', 4, 13))), LEN('Exod', 20, 1), LEN('Exod', 31, 18))
REQUEST_DELTA = (sum(LEN('Deut', 5, v) for v in range(23, 28)), LEN('Exod', 20, 18), LEN('Exod', 20, 19), len(SHARED(('Deut', 5, 27), ('Exod', 20, 19))))
HEAR_DO_DELTA = (LEN('Deut', 5, 27), LEN('Exod', 24, 7), len(SHARED(('Deut', 5, 27), ('Exod', 24, 7))))
ANSWER_DELTA = (sum(LEN('Deut', 5, v) for v in range(28, 32)), LEN('Deut', 18, 17), len(SHARED(('Deut', 5, 28), ('Deut', 18, 17))), len(SHARED(('Deut', 5, 28), ('Deut', 1, 34))))
assert FRAME_DIFF == (22, 24, 3, 16, 11, 3) and VOICE_DELTA == (24, 15, 3, 7, 16) and REQUEST_DELTA == (91, 18, 13, 1) and HEAR_DO_DELTA == (21, 13, 2) and ANSWER_DELTA == (68, 6, 3, 5), (FRAME_DIFF, VOICE_DELTA, REQUEST_DELTA, HEAR_DO_DELTA, ANSWER_DELTA)

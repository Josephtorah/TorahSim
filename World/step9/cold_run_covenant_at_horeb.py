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
assert GUARDED == 49, ("the guard counted %d expectations, the tripwire holds 49" % GUARDED)   # the cells' asks summed by the generator before the first graded run (F1 F1 5, F2 8, F3 9, F4 9, F5 4, F6 6, F7 8)
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

# ---- THE LAWS' READBACK — the first form's (R1)-(R6) ON LAW: SIXTEEN law rows (one per verse of the code, 5:6-21) graded against the runner's
# cell that compiles each word, and FIVE narrative rows; the deltas recomputed above; VARIANT the grade the code's copy adds ----
GRADES = ('VERBATIM', 'VARIANT', 'TURNED', 'SHORTENED', 'EXPANDED', 'SUPPLIED', 'DISAGREES')
def rb(verses, told, tape_kind, tape_verse, entry, grade, why, open_=False, law=False, cell=None):
    assert grade in GRADES, grade
    return {'verses': verses, 'told': told, 'tape_kind': tape_kind, 'tape_verse': tape_verse, 'entry': entry, 'grade': grade, 'why': why, 'open': open_, 'law': law, 'cell': cell}
def lr(v, grade, cell, told, why):
    e = v - 4
    d = DIFF(('Deut', 5, v), ('Exod', 20, e))
    return rb('Deut 5:%d' % v, told, 'ten_words_declared', 'Deut 4:10', "covenant_declared on israel_people dated (1, 3, 7) — the code's giving on the tape (Exodus 20:%d the first copy; 2b's supplied line at Deut 4:10-13)" % e, grade, '%s [the diff computed against Exodus 20:%d: %s; tokens %d against %d]' % (why, e, d if d else 'none', LEN('Deut', 5, v), LEN('Exod', 20, e)), law=True, cell=cell)
READBACK = [
    lr(6, 'VERBATIM', 'NO CELL', "I am the LORD your God, who brought you out of the land of Egypt, out of the house of bondage", "THE FIRST WORD — a declaration, not a case: NO CELL in any runner and none owed; heard from the Almighty's mouth with the second (Makkot 24a:1 — the two of the six hundred thirteen); nine words the same"),
    lr(7, 'VERBATIM', 'F2 the_second_word (this runner)', "you shall have no other gods before me", "THE SECOND WORD'S HEAD — NO CELL in any runner until this one (the 2b debt): compiled here from both copies; Onkelos 'another god except me'; the second heard from the Almighty's mouth (Makkot 24a:1); the block other_gods_barred written at the giving's line"),
    lr(8, 'VARIANT', 'F2 the_second_word (this runner)', "you shall not make for yourself a graven image, any form of what is in the heavens above or on the earth beneath or in the waters under the earth", "'any form' for 'and any form' — one letter, the conjunction dropped, the sense unchanged; the no-image list of 4:16-19 the parameter table (the obey_horeb runner's DATA row by CALL); the images for study credited (Rosh Hashanah 24a-24b)"),
    lr(9, 'VARIANT', 'F2 the_second_word (this runner)', "you shall not bow down to them nor serve them, for I the LORD your God am a jealous God, visiting the iniquity of the fathers upon the sons and upon the third and upon the fourth generation of those who hate me", "'fathers' plene and 'AND upon the third' — a letter and a conjunction; 'the third generation' starred by the parser (not thirty); the visiting's arms DATA (Berakhot 7a; Makkot 24a:30 — revoked by Ezekiel); the bower's death by 17:5's juxtaposition (Sanhedrin 60b:11), the prohibition's seat 34:14 (60b:12)"),
    lr(10, 'VARIANT', 'F2 the_second_word (this runner)', "and doing mercy to thousands of those who love me and keep his commandments", "THE KETIV — the written 'his commandments' where Exodus writes 'my' (the DB's one written-and-read token of the chapter; the store's seventh token the read 'my'): a DATA note, no line moves; 'to thousands' a bare plural, no number"),
    lr(11, 'VERBATIM', 'decalogue.vain_name', "you shall not take the name of the LORD your God in vain, for the LORD will not hold guiltless him who takes his name in vain", "seventeen words the same: decalogue.vain_name by CALL — the vain oath and the broken future oath lashed, 'vain and false SPOKEN AS ONE UTTERANCE, like remember and observe' the cell's own ask (Shevuot 20b:9); Mishnah Shevuot 3:8-9 the answer sheet"),
    lr(12, 'EXPANDED', 'decalogue.sabbath_clauses', "KEEP the sabbath day to sanctify it, AS THE LORD YOUR GOD COMMANDED YOU", "'keep' for 'remember' (the infinitive absolute in both copies) and THE RECEIPT INSIDE THE CODE added — nine words for five: KEEP AND REMEMBER IN ONE UTTERANCE (Shevuot 20b:9; Rosh Hashanah 27a:2, 27a:6; Berakhot 20b:10 — women obligated in kiddush; the Sifrei 233:1 the reading's exhibit); the receipt a RUN CITATION of the giving — the register seat CHAPTER; the teacher's referent Marah (Sanhedrin 56b:16; Shabbat 87b:1); decalogue.sabbath_clauses('remember') by CALL"),
    lr(13, 'VERBATIM', 'decalogue.sabbath_clauses', "six days you shall labor and do all your work", "six words the same; [6] the parser's number at both copies; decalogue.sabbath_clauses the cell (20:8-10's span)"),
    lr(14, 'EXPANDED', 'decalogue.sabbath_clauses', "but the seventh day is a sabbath to the LORD your God: you shall not do any work — you, your son, your daughter, AND your servant, your maidservant, YOUR OX AND YOUR ASS AND ALL your cattle, your stranger within your gates — THAT YOUR SERVANT AND YOUR MAIDSERVANT MAY REST LIKE YOU", "twenty-six words for eighteen — 'and your servant', 'your ox and your ass and all your cattle', 'that your servant and your maidservant may rest like you': THE OX AND THE ASS EVERY ANIMAL (Bava Kamma 54b:13 — R. Yosei in R. Yishmael's name reads the expansion itself), the rest 'like you' the analogy's limit (54b:28), the circumcised slave and the righteous convert (Yevamot 48b:5-6); decalogue.sabbath_clauses('labor_scope', 'laden_beast') by CALL"),
    lr(15, 'TURNED', 'decalogue.sabbath_clauses', "and you shall remember that you were a slave in the land of Egypt, and the LORD your God brought you out from there with a mighty hand and an outstretched arm; therefore the LORD your God commanded you to do the sabbath day", "THE GROUND TURNED WHOLE — the exodus for the creation (twenty-three words for twenty-six; 'the sabbath day' the one shared run): the fourth word's TWO GROUNDS a DATA row (the creation of 20:11 the pre-Sinai runner's by CALL; 'remember that you were a slave' five seats, all this book's); decalogue.sabbath_clauses the cell"),
    lr(16, 'EXPANDED', 'holiness.frame', "honor your father and your mother, AS THE LORD YOUR GOD COMMANDED YOU, that your days may be long AND THAT IT MAY GO WELL WITH YOU on the ground which the LORD your God gives you", "twenty-two words for fifteen — the receipt and 'that it may go well with you' added, 'be long' a longer form: NO CELL AT THE DECALOGUE'S SEAT — the fifth word compiled at its kin's, Leviticus 19:3 (holiness.frame by CALL — the honor and the fear defined, the order, the three partners, the woman: Kiddushin 30b-31b); THE EXPANSION'S OWN ROW (Bava Kamma 55a:1 — 'good' not in the first tablets; Kiddushin 39b-40a; Chullin 142a); the sanctions' seats mishpatim_3.parent_striker and parent_curser, sanctions.curser by CALL; the receipt CHAPTER (Marah — Sanhedrin 56b:16)"),
    lr(17, 'VERBATIM', 'mishpatim_3.killer', "you shall not murder", "two words the same: the sixth word's code at Exodus 21:12-14 (mishpatim_3.killer by CALL — the sword) and Numbers 35 (refuge.the_murderer by CALL); the context of the eighth word's reading (Sanhedrin 86a:16)"),
    lr(18, 'VARIANT', 'sanctions.adultery', "and you shall not commit adultery", "'and not' for 'not' — the conjunction; the seventh word's code at Leviticus 20:10 (sanctions.adultery by CALL — strangling, both)"),
    lr(19, 'VARIANT', 'decalogue.theft_commandment', "and you shall not steal", "the conjunction; THE THEFT OF PERSONS by the context (Sanhedrin 86a:15-17 — the decalogue runner's own move): decalogue.theft_commandment('kidnapper') by CALL; Leviticus 19:11's of property by its context"),
    lr(20, 'TURNED', 'ordinances.courts', "and you shall not answer against your neighbor a VAIN witness", "'vain' for 'false' and the conjunction — the ninth word's parameter a DATA row (Onkelos 'false' at both copies): NO CELL AT THE DECALOGUE'S SEAT — the kin at Exodus 23:1 (ordinances.courts('false_report', 'witness_of_violence') by CALL); the conspiring witnesses Deuteronomy 19:16-21 forward"),
    lr(21, 'TURNED', 'F5 the_tenth_word (this runner)', "and you shall not covet your neighbor's wife; and you shall not DESIRE your neighbor's house, HIS FIELD, or his servant or his maidservant, his ox or his ass, or anything that is your neighbor's", "THE WIFE FIRST (the house first in Exodus), DESIRE for the second 'covet', 'his field' added, 'and his ox' — sixteen words for fifteen: NO CELL in any runner until this one — compiled here (Bava Metzia 5b:19-20 the coveter who pays); the block coveting_barred written at the giving's line"),
    rb('Deut 5:1-5, 32-33', "and Moses called all Israel and said to them: hear, O Israel, the statutes and the judgments which I speak in your ears this day; learn them, and keep to do them; the LORD our God made a covenant with us in Horeb — not with our fathers, but with us, we who are all here alive this day; face in face the LORD spoke with you in the mountain out of the midst of the fire, I standing between the LORD and you at that time … and you shall observe to do as the LORD your God commanded you; you shall not turn aside right or left", 'speech_opened', 'Deut 1:1', "torah_expounded on israel_people at (40, 11, 1) — the book's one act of its own day", 'EXPANDED', "THE FRAME'S SECOND SEAT AGAIN (R6): the second speech's opening and its charge — NO WRITE; 5:1 against 4:1 (twenty-two tokens for twenty-four, three shared — computed); 5:2-3 the covenant against the tape's covenant_offered (Exod 19:5-6), people_answered (19:8, 24:3, 24:7) and covenant_blood_thrown (24:8) — 'not with our fathers' against 29:13-14 a DATA note; 5:4 'face IN face' the Bible's one seat (Onkelos 'speech with speech' — ER.presence by CALL); the covenants counted forty-eight per mitzva times the guarantors (Sotah 37b); 5:32-33 the charge NO WRITE, the receipt CHAPTER"),
    rb('Deut 5:22', "these words the LORD spoke to all your assembly in the mountain out of the midst of the fire, the cloud and the thick darkness, with a great voice, and he added no more; and he wrote them on two tablets of stone and gave them to me", 'ten_words_declared', 'Deut 4:10', "covenant_declared on israel_people dated (1, 3, 7) and tablets_delivered on moses dated (1, 4, 17) — 2b's two SUPPLIED lines, FOUND (no second write)", 'EXPANDED', "twenty-four tokens for 4:13's fifteen, three shared ('and he wrote them on two' — computed); Exodus 20:1's seven and 31:18's sixteen the first tellings; 'to all your assembly' the Bible's one seat; 'ADDED NO MORE' a DATA note with Onkelos 'did not cease' (Sanhedrin 17a:12 — Eldad and Medad; Sotah 10b:12 — Judah); the tablets defective here, plene at 4:13; OH.horeb_retold by CALL"),
    rb('Deut 5:23-27', "and it came to pass, when you heard the voice out of the midst of the darkness, while the mountain burned with fire, that you came near to me, all the heads of your tribes and your elders, and you said: … go you near and hear all that the LORD our God shall say, and you speak to us all that the LORD our God speaks to you, and we will hear and do", 'mediator_requested', 'Deut 5:23', "torah_through_moses on israel_people dated (1, 3, 7) — THE SUPPLIED LINE (Exodus 20:18-19 the first telling, no line on the tape)", 'SUPPLIED', "THE TAPE'S SECOND HOLE: Exodus 20:18-19's 'and all the people saw the thunders … speak you with us and we will hear' has no line on the tape (20:18 sits in no runner's span; 20:19-21 are the ordinances' law cells): written ONCE at its own time, dated (1, 3, 7) by the retrograde marker at Deut 5:23 (the ink's own 'when you heard the voice'); ninety-one tokens for 20:18's eighteen and 20:19's thirteen; 'you came near to me' 1:22's phrase (the mob there, the heads and elders here — the Sifrei 20:1; OS by CALL); the first two words from the Almighty's mouth, the rest through Moses (Makkot 24a:1); 5:5 'I stood between' folded here"),
    rb('Deut 5:27', "go you near and hear all that the LORD our God shall say, and you speak to us all that the LORD our God speaks to you, AND WE WILL HEAR AND DO", 'people_answered', 'Exod 24:7', "people_answered at Exod 24:7 — 'the book of the covenant read: we will do and we will hear' (the erection's W7 line)", 'TURNED', "THE ORDER TURNED: 'we will hear and do' against 24:7's 'we will do and hear' (twenty-one tokens against thirteen, two shared — computed; 'we will do' at 19:8, 24:3, 24:7 by ES.sinai('we_will_do_seats')); R. Simai's two crowns for 'we will do' before 'we will hear' (Shabbat 88a:7), the angels' secret (88a:8), the heretic's 'impulsive nation' (88a:9); Onkelos 'we will accept and do'"),
    rb('Deut 5:28-31', "and the LORD heard the voice of your words when you spoke to me; and the LORD said to me: … they have done well in all that they have spoken; who would give that they had such a heart … go say to them: return to your tents; but as for you, stand here with me, and I will speak to you all the commandment and the statutes and the judgments which you shall teach them", 'stand_here_commanded', 'Deut 5:28', "commanded on moses valued teach_the_commandment — written and CLOSED inside the daemon by the prior run (the closer Deut 1:1-5); returned_to_tents on israel_people dated (1, 3, 7) — THE SUPPLIED LINE (told only here; 18:16-17 forward)", 'SUPPLIED', "TOLD ONLY IN THE RETELLING (Exodus 20:22's answer another speech; 18:17's 'they have well said' cites this verdict forward — six tokens, three shared, computed): written ONCE at its own time inside the retrograde stretch of 5:23; 'the LORD heard the voice of your words' 1:34's five words (OS by CALL); THE CHARGE TO TEACH a DEBIT on Moses CLOSED AT ONCE BY THE PRIOR RUN — the book's expounding at 1:5 and 4:5's receipt the run (Exodus 24:12's 'to teach them' — ER.ascent by CALL); 'return to your tents' the separation of 19:15 released (Beitzah 5a-b; Shabbat 87a; Yevamot 62a); 'stand here with me' the Torah received standing (Megillah 21a; the Sifrei 357:40)"),
]
RB_GRADES = collections.Counter(r['grade'] for r in READBACK)
assert len(READBACK) == 21 and RB_GRADES == collections.Counter({'VERBATIM': 5, 'VARIANT': 5, 'EXPANDED': 5, 'TURNED': 4, 'SUPPLIED': 2}) and not any(r['open'] for r in READBACK), (len(READBACK), RB_GRADES)
assert sum(1 for r in READBACK if r['law']) == 16 and [r['verses'] for r in READBACK if r['law'] and r['cell'] == 'NO CELL'] == ['Deut 5:6'] and sum(1 for r in READBACK if r['law'] and r['cell'] != 'NO CELL') == 15

DATA = {
    'the_readback': {'value': READBACK, 'settings': {'the_first_form_on_law': "THE_LOOP.md step 6's laws' half (the owner's 'go', 2026-09-16): a word of the code retold is a REFERENCE ROW graded against the runner's cell that compiles it — VERBATIM / VARIANT / EXPANDED / TURNED — and names its cell or NO CELL; TWENTY-ONE rows: sixteen law rows (VERBATIM 5, VARIANT 5, EXPANDED 3, TURNED 3) and five narrative rows (EXPANDED 2, SUPPLIED 2, TURNED 1); the deltas recomputed from the DB; THE CODE'S HOLE (the second and the tenth words) filled here; THE TAPE'S SECOND HOLE (Exodus 20:18-21) written once at its own time", 'the_ten_as_a_unit': "the ten words a unit on the shelf — read daily by the priests in the Temple, sought outside and ABOLISHED for the heretics' grievance (Berakhot 12a:4-8); the nations conceded the first two words when the fifth was said ('the words of Your mouth', Kiddushin 31a:6-7): the schema question's second exhibit", 'the_third_telling': "R. Akiva — the generals and the details said at Sinai, repeated at the Tent, and REITERATED A THIRD TIME by Moses in the plains of Moab; R. Yishmael — the generals at Sinai only (Sotah 37b:3; Tosefta Sotah 8:11): the second copy's own status on the shelf — the readback's teacher", 'the_second_numbering': "the shelf's English cites chapter 5 by TWO numberings (the export's and one a verse lower around the short words): every docket verdict names the DB verse by the row's quoted words"}},
    'the_second_word': {'value': {'prohibitions': ['no other gods before me', 'no graven image nor any form', 'not bow down to them', 'not serve them'], 'liable_to_death': ['worship in its way', 'slaughter', 'incense', 'libation', 'bowing'], 'a_prohibition_without_death': ['hug', 'kiss', 'sweep', 'sprinkle', 'wash', 'anoint', 'dress', 'shoe', 'a vow or oath by its name'], 'mode': 'stoning', 'sanction_seat': 'Deut 17:2-7 (forward; a REFERENCE the ink makes — by juxtaposition, Sanhedrin 60b:11)'}, 'settings': {'the_answer_sheet': "Mishnah Sanhedrin 7:6 with Sanhedrin 60b:1-19 — the idolater stoned for worship in its way and for the Temple's four rites even not in its way (slaughter, incense, libation, bowing — 'except to the LORD alone', Exodus 22:19 emptied the rites to the Name; R. Yirmeya, 60b:5); the hugger and the kisser a prohibition without death (60b:2, 60b:13); Peor's exposure and Markulis's stone their own service (60b:3)", 'the_bowers_death': "by the juxtaposition of 'and bowed to them' (Deut 17:3) to 'you shall stone them' (17:5) — Sanhedrin 60b:11; the PROHIBITION of bowing from 'you shall bow to no other god' (Exodus 34:14 — 60b:12), not from the second word's 'to them' (said of the images)", 'the_disputed_arm': "Rava bar Rav Chanan: any HONORABLE service capital, not the Temple's rites only (60b:18)", 'the_first_two_words': "'I am' and 'you shall have no other gods' heard from the Almighty's mouth — 611 and 2 (Makkot 24a:1)", 'onkelos': "'another god EXCEPT ME' (5:7); 'rebellious children … when the children complete to sin after their fathers' the translation's supplied condition at 5:9"}},
    'the_visiting': {'value': {'generations': 'the third and the fourth of those who hate me', 'mercy': 'thousands of those who love me', 'ketiv': "his commandments (written) / my commandments (read; Exodus 20:6's word)"}, 'settings': {'berakhot_7a': "'visiting the iniquity of the fathers upon the sons' against 'the sons shall not die for the fathers' (24:16) — when they hold their fathers' deeds in their hands (Berakhot 7a:27, credited from the Decalogue's block)", 'makkot_24a': "Moses' decree 'he visits the transgression of the fathers upon the sons' (Exodus 34:7) REVOKED by Ezekiel — 'the soul that sins, it shall die' (18:4) (Makkot 24a:30)", 'the_parser': "'the third generation' STARRED — not thirty (rule 15); 'to thousands' a bare plural; the lemma's five seats (Genesis 50:23 the first)", 'the_ketiv': "the DB's one x-ketiv token of the chapter (5:10); the store carries both glosses; no line moves"}},
    'the_no_image_list': {'value': OH.DATA['the_no_image_list']['value'], 'settings': {'by_call': "the obey_horeb runner's DATA row — 4:16-19's forms restating Exodus 20:4's 'any likeness' in seven kinds and the host: the second word's parameter table; the images for study (Mishnah Rosh Hashanah 2:8; Rosh Hashanah 24a-24b) and the statues (Mishnah Avodah Zarah 3:1-3) credited from 2b's docket"}},
    'the_tenth_word': {'value': {'verbs': ['covet (the wife)', 'desire (the house, the field, the servants, the beasts, all)'], 'order': "the wife first here, the house first in Exodus", 'added': 'his field', 'the_coveter_who_pays': 'transgresses — taking by force or deceit even with payment (Rav Acha of Difti); most people read it as taking without payment, so the bailee who pays is not disqualified (Bava Metzia 5b:19-20)'}, 'settings': {'the_mekhilta': "covet in deed, desire in the heart — the Mekhilta d'Rabbi Yishmael Bahodesh 8 (the first copy's spine, named, unopened)", 'onkelos': "'AND DO NOT DESIRE' (5:21)", 'the_root': "the desire-root's twenty-five seats (Numbers 11:4, 34 the craving); 'covet' 2ms four seats"}},
    'the_sabbath_grounds': {'value': {'exodus_20_11': 'the creation — six days he made the heavens and the earth, rested the seventh', 'deut_5_15': 'the exodus — you were a slave in Egypt and the LORD brought you out'}, 'settings': {'by_call': "the creation ground the pre-Sinai runner's (PS.sabbath('delta_20_11') — Genesis 2:2-3 against Exodus 20:11 by token); 'remember that you were a slave' five seats, all this book's (15:15, 16:12, 24:18, 24:22); the readback row 5:15 TURNED"}},
    'the_ninth_word': {'value': {'exodus_20_16': 'a false witness', 'deut_5_20': 'a vain witness', 'onkelos': 'false at both'}, 'settings': {'the_kin': "Exodus 23:1's 'you shall not take up a false report … a witness of violence' (ordinances.courts by CALL); the conspiring witnesses Deuteronomy 19:16-21 forward; 'vain' four Torah seats (5:11, 5:20, Exodus 20:7, 23:1); the witnesses to half a matter (Sanhedrin 86a:18-19)"}},
    'keep_and_remember': {'value': 'one_utterance', 'settings': {'shevuot_20b': "'remember' and 'keep' spoken in one utterance — what the mouth cannot say nor the ear hear; the vain and the false oath 'one' by the same rule (20b:9 — the decalogue runner's ask vain_and_false_utterance)", 'rosh_hashanah_27a': "two sounds from ONE source cannot be discerned — Sinai's miracle (27a:2, 27a:6)", 'berakhot_20b': "whoever is in 'keep' is in 'remember' — women obligated in kiddush by the Torah (Rava, 20b:10)", 'shabbat_33b': "the two bundles of myrtle (33b:8)", 'the_sifrei': "233:1 on 22:11-12 with 5:12 and Exodus 20:8 — the reading's exhibit (the schema question)"}},
    'the_reward_clause': {'value': {'deut_5_16': 'that your days may be long AND THAT IT MAY GO WELL WITH YOU', 'exodus_20_12': 'that your days may be long'}, 'settings': {'bava_kamma_55a': "why 'good' here and not in the first tablets? R. Chiya bar Abba sends to R. Tanchum bar Chanilai (55a:1; the answer in the following segment, named: the first tablets were to be broken)", 'the_court': "a positive mitzva whose reward is stated beside it — the court below not warned to enforce it (Chullin 110b:3)", 'the_world': "the reward after the resurrection (R. Yaakov — Chullin 142a:3; Kiddushin 39b:7) or in this world (Rava — Kiddushin 40a:5): the arms"}},
    'the_honor_by_call': {'value': {'honor': HO.frame('honor_defined')['v'], 'fear': HO.frame('fear_defined')['v'], 'order': HO.frame('parents_order')['v'], 'partners': HO.frame('three_partners')['v'], 'woman': HO.frame('woman_included')['v']}, 'settings': {'kiddushin_30b_31b': "what is fear and what is honor (31b:14); the three equations — honor with wealth, fear with fear, cursing with cursing, striking not equated (30b:18-20); the three partners (30b:21); the father first in 'honor', the mother first in 'fear' (30b:22-31a:1); the woman under her husband, divorced equal (30b:16-17); the father first when both ask (31a:4-5); how far — Dama ben Netina (31a:8-13); the manner — pheasant and the millstone (31a:14); in life and in death (31b:10-13)", 'the_sanctions': "the striker (Exodus 21:15) strangled, the curser (21:17; Leviticus 20:9) stoned — mishpatim_3 and sanctions by CALL"}},
    'the_receipts': {'value': {'Deut 5:12': 'CHAPTER', 'Deut 5:16': 'CHAPTER', 'Deut 5:32': 'CHAPTER'}, 'settings': {'the_ink': "'as the LORD your God commanded you' INSIDE the ten words (5:12, 5:16; 20:17 the third seat) and the plural at 5:32 — a law citing its prior giving: RUN CITATIONS of the tape's ten_words_declared (Exodus 20:8, 20:12, 20:1-17 the first tellings); no ledger write pays a receipt (R5)", 'the_teacher': "Rav Yehuda — commanded AT MARAH (Exodus 15:25: the Sabbath and honoring parents among Marah's statutes — Sanhedrin 56b:16; Shabbat 87b:1; ES.marah('statute_list') by CALL): the pointers name both referents", 'the_gate': "the class from the gate's own code: no write's source contains the verses (the second copy is no line), the chapter holds a closed entry (the charge to teach, closed inside the daemon) — CHAPTER"}},
    'the_two_copies': {'value': {'exodus_20_2_17': COPIES[0], 'deut_5_6_21': COPIES[1], 'per_word': WORD_TOK}, 'settings': {'computed': "tokens and letters (consonants, no maqaf) recomputed from the DB; the per-verse tokens (DB verse, Exodus verse, Exodus tokens, Deuteronomy tokens)"}},
    'the_second_hole': {'value': {'exod_20_18': 'in no runner\'s span', 'exod_20_19_21': "the ordinances' law cells, no narrative line", 'the_tape': 'runs from Exod 19:20 to 24:1'}, 'settings': {'the_answer': "R3's form — the request written ONCE at its own time from the retelling's seat (mediator_requested, dated (1, 3, 7) by the retrograde marker at 5:23); the answer told only here (stand_here_commanded, the same day); a forward marker at 5:32 ends the stretch"}},
    'the_export_division': {'value': {'export': 30, 'db': 33, 'the_map': '1-16 = 1-16; 17 = 17-20; 18 = 21; 19-30 = 22-33'}, 'settings': {'the_citations': "the shelf's English cites the chapter by two numberings — Sanhedrin 17a:12 cites 5:19 and Sotah 10b:12 cites 5:18 for one verse (the DB's 22); the quoted words fix the verse"}},
    'the_mediator': {'value': {'deut_5_5': 'I stood between the LORD and you', 'deut_5_27': 'you speak to us … and we will hear and do', 'deut_5_31': 'stand here with me and I will speak to you all the commandment'}, 'settings': {'makkot_24a': "'I am' and 'you shall have no other gods' from the Almighty's mouth; 611 through Moses (24a:1)", 'avot_1_1': "'Moses received the Torah from Sinai and handed it on' — the vocabulary of the status torah_through_moses", 'onkelos': "'between the MEMRA of the LORD and you' (5:5)", 'moses_separation': "Moses separated from his wife by an a fortiori, and God agreed — 'and you, stand here with me' (Shabbat 87a:4; Yevamot 62a:2)"}},
    'the_return_to_tents': {'value': 'the_separation_of_exodus_19_15_released', 'settings': {'beitzah_5a': "a matter forbidden by a count needs a count to permit — Rav Yosef from 'return to your tents' after 'do not come near a woman' (5a:7, 5b:3)", 'his_tent': "'his tent' is his wife (Moed Katan 7b:5, 15b:13)", 'procreation': "repeated at Sinai — Israel's by the framework (Sanhedrin 59b:3-4; PS.noahide by CALL)"}},
    'the_charge_to_teach': {'value': {'debit': 'teach_the_commandment', 'on': 'moses', 'closed_by': 'Deut 1:5 — the prior run (the book itself)'}, 'settings': {'the_ink': "'stand here with me and I will speak to you all the commandment and the statutes and the judgments WHICH YOU SHALL TEACH THEM' (5:31); Exodus 24:12's 'to teach them' (ER.ascent('torah_mitzvah') by CALL); 4:14 'the LORD commanded me at that time to teach you'; 4:5 'I have taught you … as the LORD my God commanded me' (the register seat ACT since 2b)", 'the_form': "THE CLOSE BY A PRIOR RUN (R3) — the opening speech's _closed_by_prior_run: the debit written and closed inside the daemon with the tape's EARLIER line as the closer (speech_opened at Deut 1:1-5, 'Moses undertook to expound this Torah')"}},
    'the_face_in_face': {'value': {'deut_5_4': 'face IN face (the one seat)', 'the_other_form': 'face TO face (five seats — Jacob, Moses at the tent 33:11, 34:10, Gideon, Ezekiel)'}, 'settings': {'onkelos': "'speech with speech' — as at Exodus 33:11 (ER.presence('speech_with_speech') by CALL)", 'yoma_4b': "'He called to Moses' — Moses and all Israel standing and listening: all Israel heard the voice at Horeb; at the Tent Moses alone (Numbers 7:89) (4b:7-8)", 'the_day': "the sixth or the seventh of Sivan (Yoma 4b:3; Shabbat 88a:2-3) — the sinai_days row's two settings, Rabbi Yose's the running one"}},
    'the_fathers_and_us': {'value': {'deut_5_3': 'not with our fathers did the LORD make this covenant, but with us, we who are all here alive this day', 'deut_29_13_14': 'not with you alone … but with him who stands here with us this day and with him who is not here'}, 'settings': {'computed': "5:3 against 29:13 (sixteen tokens for eleven, three shared); 'our fathers' six Torah seats; 'this covenant' three; a DATA note — no teacher joins them here (the Sifrei silent); the guarantors — every one of Israel a guarantor for the rest, 603,550 covenants (Sotah 37b:5-6)"}},
    'the_hear_and_do': {'value': {'deut_5_27': 'we will hear and do', 'exodus_24_7': 'we will do and hear', 'exodus_19_8_24_3': 'all that the LORD has spoken we will do'}, 'settings': {'shabbat_88a': "R. Simai — 'we will do' before 'we will hear': two crowns on each, removed at the calf (88a:7); the angels' secret (88a:8); the heretic to Rava (88a:9); the mountain overturned like a tub and the caveat (88a:5 — ES.sinai('tub') by CALL)", 'onkelos': "'we will ACCEPT and do' (5:27)"}},
}
assert len(DATA) == 20, len(DATA)

# ===== F1: THE ASSEMBLY CALLED — the frame's second seat (Deut 5:1-5) ====================================
def the_assembly_called(case, data):
    del P_[:]
    ask = case['ask']
    if ask == 'hear_learn_keep_do':
        ink('5:1', '"and Moses called all Israel and said to them: hear, O Israel, the statutes and the judgments which I speak in your ears this day; learn them, and keep to do them" — "and Moses called all Israel" %s (the book\'s two convocations); "hear, O Israel" %s; "in your ears" %s the Torah\'s one seat; "keep to do them" one seat; "hear" the imperative %s' % (P('ויקרא', 'משה', 'אל', 'כל', 'ישראל'), P('שמע', 'ישראל'), U('באזניכם'), IMPER[1]))
        move('Yevamot 109b:5', "Rav Pappa — 'that you may learn them and keep to do them': whoever is engaged in doing is engaged in learning; not doing, not even Torah")
        dat('the row the_readback: 5:1-5 with 5:32-33 EXPANDED against speech_opened (Deut 1:1) — NO WRITE (R6)')
        return out("hear, learn, keep, do (5:1) — the second speech opened: Moses' call to all Israel, the four verbs in order; the frame's second seat, no write", ['accepted'])
    if ask == 'the_covenant_at_horeb':
        ink('5:2', '"the LORD our God made a covenant with us in Horeb" — "made a covenant with us" %s the one seat; Horeb the name (lemma %s)' % (P('כרת', 'עמנו', 'ברית'), lemma_of('Deut', 5, 2, 'בחרב')))
        move('Sotah 37b:1-6', "the covenants counted — four general and four specific, with blessings and curses sixteen, at Sinai, the Tent and Moab: forty-eight per mitzva, times 603,550 guarantors (R. Shimon ben Yehuda of Kefar Akko)")
        move('Sotah 37b:3', "R. Akiva — the generals and the details said at Sinai, repeated at the Tent, reiterated a third time at Moab; R. Yishmael — the generals at Sinai only: the second copy's own status")
        dat("the tape's covenant: covenant_offered (Exod 19:5-6), people_answered (19:8, 24:3, 24:7), covenant_blood_thrown (24:8) — the book of the covenant %d seats, 'one voice' %d (ER by CALL)" % (ER_BOOK['v'], ER_VOICE1['v']))
        return out("the covenant at Horeb (5:2) — the tape's covenant READ BACK: the book and the blood (ER by CALL); forty-eight covenants per mitzva (Sotah 37b); the second copy a third saying (R. Akiva)", ['accepted'])
    if ask == 'not_with_our_fathers':
        ink('5:3', '"not with our fathers did the LORD make this covenant, but with us, we who are all here alive this day" — "not with our fathers" %s; "this covenant" %s in the Torah; "all of us alive" %s; against 29:13-14 (the diff computed: %s tokens for %s, %s shared)' % (P('לא', 'את', 'אבתינו'), P('הברית', 'הזאת', books=T), P('כלנו', 'חיים'), FRAME_DIFF[3], FRAME_DIFF[4], FRAME_DIFF[5]))
        dat('the row the_fathers_and_us: a DATA note — no teacher joins 5:3 to 29:13-14 here; the guarantors (Sotah 37b:5)')
        return out("not with our fathers (5:3) — the covenant with the living here: a DATA note against 29:13-14, no link of our own", ['accepted'])
    if ask == 'face_in_face':
        ink('5:4', '"face in face the LORD spoke with you in the mountain out of the midst of the fire" — "face IN face" %s THE BIBLE\'S ONE SEAT; "face to face" %s; "in the mountain from the midst of the fire" %s' % (P('פנים', 'בפנים'), P('פנים', 'אל', 'פנים'), P('בהר', 'מתוך', 'האש')))
        move('Onkelos Deut 5:4 (ER.presence by CALL)', "'speech with speech' — the rendering of Exodus 33:11's 'face to face' (%s)" % ER_SPEECH['v'])
        move('Yoma 4b:7-8', "R. Elazar — 'He called to Moses': Moses and all Israel standing and listening; all Israel heard the voice at Horeb, at the Tent Moses alone (Numbers 7:89)")
        return out("face in face (5:4) — the one seat of the form; Onkelos 'speech with speech' (ER by CALL); all Israel heard the voice (Yoma 4b)", ['accepted'])
    if ask == 'i_stood_between':
        ink('5:5', '"I stood between the LORD and you at that time to declare to you the word of the LORD, for you were afraid of the fire and did not go up the mountain, saying" — "I stood between" %s; "stood between" %s; "at that time" fifteen seats in the book; "saying" the chapter\'s one seat; the Memra between (Onkelos)' % (P('אנכי', 'עמד', 'בין'), P('עמד', 'בין')))
        move('Makkot 24a:1', "'I am' and 'you shall have no other gods' heard from the Almighty's mouth; the rest through Moses — the mediator's row")
        dat('the row the_mediator: 5:5 folded into the request\'s SUPPLIED row (5:23-27); Exodus 20:21 "Moses drew near to the thick darkness" the first telling of the standing between')
        return out("I stood between (5:5) — the mediator: the first two words direct, the rest through Moses (Makkot 24a); the request's row", ['accepted'])
    return out('no verdict in span', [FX.NONE])


# ===== F2: THE SECOND WORD — compiled here from both copies (Deut 5:7-10; Exodus 20:3-6) ===================
def the_second_word(case, data):
    del P_[:]
    ask = case['ask']
    if ask == 'no_other_gods':
        ink('5:7', '"you shall have no other gods before me" — %s the two copies verbatim; "other gods" %d Torah seats, %d this book\'s; Onkelos "another god EXCEPT ME"' % (P('אלהים', 'אחרים', 'על', 'פני'), len(P('אלהים', 'אחרים', books=T)), len(P('אלהים', 'אחרים', books=('Deut',)))))
        move('Makkot 24a:1', "the second of the two words heard from the Almighty's mouth — 611 and 2")
        move('Sanhedrin 60b:12', "the PROHIBITION of bowing from 'you shall bow to no other god' (Exodus 34:14) — the second word's 'to them' said of the images")
        dat('the row the_second_word: NO CELL in any runner until this one — the code\'s hole filled from the retelling\'s seat')
        return out("no other gods before me (5:7) — the second word's head, compiled here: the block other_gods_barred on Israel at the giving's line", ['accepted'])
    if ask == 'no_image':
        ink('5:8', '"you shall not make for yourself a graven image, any form of what is in the heavens above or on the earth beneath or in the waters under the earth" — "any form" for Exodus\'s "and any form" (%s / %s); "a graven image" %d Torah seats; "in the waters under the earth" %s' % (P('פסל', 'כל', 'תמונה'), P('פסל', 'וכל', 'תמונה'), len(U('פסל', 'ופסל', books=T)), P('במים', 'מתחת', 'לארץ')))
        dat("the row the_no_image_list (OH by CALL): %d kinds — 4:16-19's parameter table; the images for study (Rosh Hashanah 24a-24b) and the statues (Mishnah Avodah Zarah 3:1-3) credited" % len(data['the_no_image_list']['value']))
        return out("no image (5:8) — the making barred; the no-image list of 4:16-19 the parameter table (OH by CALL); the images for study credited", ['accepted'])
    if ask == 'bow_and_serve':
        ink('5:9', '"you shall not bow down to them nor serve them" — %s the two copies; the prohibitions %s; "a jealous God" %s' % (P('לא', 'תשתחוה', 'להם', 'ולא', 'תעבדם'), PROHIB[9], P('אל', 'קנא')))
        move('Mishnah Sanhedrin 7:6; Sanhedrin 60b:1, 60b:5', "the idolater STONED — the worshipper in its way, the slaughterer, the incense-burner, the libation-pourer, the BOWER (even not in its way — the Temple's rites emptied to the Name, 'except to the LORD alone', Exodus 22:19: 60b:8-9), the one who accepts it as a god, 'you are my god'")
        move('Sanhedrin 60b:11', "the bower's death by the juxtaposition of 'and bowed to them' (Deut 17:3) to 'you shall stone them' (17:5) — the mode STONING, 17:2-7's procedure chapter 17's sitting")
        move('Sanhedrin 60b:18', "Rava bar Rav Chanan — any honorable service capital? the disputed arm (DATA)")
        return out("bow and serve (5:9) — the bower stoned: the second word's answer sheet (Mishnah Sanhedrin 7:6; the four services, Sanhedrin 60b); the mode by 17:5's juxtaposition", ['put_to_death'])
    if ask == 'in_its_way':
        ink('5:9', '"nor serve them" — the service in its own manner: Peor\'s exposure and Markulis\'s stone (the balak runner\'s Peor the kin)')
        move('Mishnah Sanhedrin 7:6; Sanhedrin 60b:3, 60b:5', "one who defecates before Peor or throws a stone at Markulis is liable — that is its worship (R. Yirmeya: worship in its typical manner liable)")
        return out("in its way (5:9) — Peor's exposure, Markulis's stone: liable, the idol's own service (Mishnah Sanhedrin 7:6)", ['put_to_death'])
    if ask == 'the_embracer':
        ink('5:9', '"you shall not bow down to them nor serve them" — the acts below service')
        move('Mishnah Sanhedrin 7:6; Sanhedrin 60b:2, 60b:13', "the hugger, the kisser, the sweeper, the sprinkler, the washer, the anointer, the dresser, the shoer — a PROHIBITION, not liable to death (excluded by 'he who sacrifices'); the vow and the oath by its name a prohibition")
        return out("the embracer (5:9) — a prohibition without death: the hugger, the kisser, the dresser exempt from the sanction (Mishnah Sanhedrin 7:6)", ['exempt'])
    if ask == 'the_visiting':
        ink('5:9-10', '"visiting the iniquity of the fathers upon the sons and upon the third and upon the fourth generation of those who hate me, and doing mercy to thousands of those who love me and keep his commandments" — "visiting the iniquity of fathers upon sons" %s (not Exodus 20:5 — its "fathers" defective); the third generation starred (the lemma\'s seats %s); "to thousands" %s' % (P('פקד', 'עון', 'אבות', 'על', 'בנים'), LEMV('8029'), U('לאלפים')))
        move('Berakhot 7a:27 (credited); Makkot 24a:30', "when they hold their fathers' deeds in their hands; Moses' decree revoked by Ezekiel 18:4 — the two arms")
        dat('the row the_visiting: %s' % data['the_visiting']['value'])
        return out("the visiting (5:9-10) — the generations and the thousands a DATA row: when they hold their fathers' deeds (Berakhot 7a); revoked by Ezekiel (Makkot 24a)", ['accepted'])
    if ask == 'the_ketiv':
        ink('5:10', '"keep his commandments" — the written "his" (%s), Exodus 20:6\'s "my" (%s); the DB\'s one written-and-read token of the chapter' % (P('לאהבי', 'ולשמרי', 'מצותו'), P('לאהבי', 'ולשמרי', 'מצותי')))
        dat("the ketiv: wtype x-ketiv at 5:10's last token; the store carries both glosses ('his commandments', 'my commandments'); no line moves")
        return out("the ketiv (5:10) — 'his' written, 'my' read: a DATA note, no line", ['accepted'])
    if ask == 'the_write':
        ink('5:7-10', 'the second word whole — the block written on Israel AT THE GIVING\'S LINE (ten_words_declared, dated (1, 3, 7)), never at the retelling\'s')
        dat("the write: other_gods_barred on israel — law_covenant_at_horeb watches ten_words_declared (2b's supplied line); THE REST's one declared delta")
        return out("the write (5:7-10) — other_gods_barred on Israel: the code's hole filled at the code's own line", ['other_gods_barred'])
    return out('no verdict in span', [FX.NONE])


# ===== F3: THE FIRST TABLET — the words one to four read back (Deut 5:6-15) =============================
def _row(v): return [r for r in READBACK if r['verses'] == 'Deut 5:%d' % v][0]
def the_first_tablet(case, data):
    del P_[:]
    ask = case['ask']
    if ask == 'the_first_word':
        r = _row(6)
        ink('5:6', '"I am the LORD your God, who brought you out of the land of Egypt, out of the house of bondage" — %s VERBATIM (the diff %s); "I am the LORD your God" %s; "house of bondage" twelve seats' % (r['grade'], DIFF(('Deut', 5, 6), ('Exod', 20, 2)) or 'none', P('אנכי', 'יהוה', 'אלהיך')))
        move('Makkot 24a:1', "the first of the six hundred thirteen, from the Almighty's mouth")
        dat('the row: NO CELL — a declaration, not a case')
        return out("the first word (5:6) — VERBATIM; NO CELL: a declaration heard from the Almighty's mouth", ['accepted'])
    if ask == 'the_second_word_row':
        rows = [_row(v) for v in (7, 8, 9, 10)]
        ink('5:7-10', 'the second word\'s four verses — %s; the diffs %s' % ([r['grade'] for r in rows], [DIFF(('Deut', 5, v), ('Exod', 20, v - 4)) for v in (7, 8, 9, 10)]))
        dat("the rows name F2 the_second_word (this runner) — the code's hole filled")
        return out("the second word (5:7-10) — VERBATIM, VARIANT, VARIANT, VARIANT: the cell F2 (compiled here)", ['accepted'])
    if ask == 'the_third_word':
        ink('5:11', '"you shall not take the name of the LORD your God in vain" — VERBATIM (%s); "in vain" %d seats; "will not hold guiltless" %d' % (DIFF(('Deut', 5, 11), ('Exod', 20, 7)) or 'none', len(U('לשוא')), len(P('לא', 'ינקה'))))
        move('decalogue.vain_name by CALL', "the vain oath lashed (%r), the broken future oath lashed, 'vain and false spoken as one — like remember and observe' (%r)" % (DC_VAINOATH[0], DC_VAIN[0]))
        move('Mishnah Shevuot 3:8-9', "the vain oath defined — the known falsehood, the impossible, the oath against a mitzva, the witnesses' oath; the oath against an oath")
        return out("the third word (5:11) — VERBATIM: decalogue.vain_name by CALL (the vain oath lashed; Mishnah Shevuot 3:8-9)", ['accepted'])
    if ask == 'the_fourth_word':
        rows = [_row(v) for v in (12, 13, 14, 15)]
        ink('5:12-15', 'the fourth word\'s four verses — %s; the tokens %s against Exodus 20:8-11\'s %s' % ([r['grade'] for r in rows], [LEN('Deut', 5, v) for v in (12, 13, 14, 15)], [LEN('Exod', 20, v) for v in (8, 9, 10, 11)]))
        move('decalogue.sabbath_clauses by CALL', "remember → %r; labor_scope → %r; laden_beast → %r" % (DC_REM[0], DC_SCOPE[0], DC_LADEN[0]))
        return out("the fourth word (5:12-15) — EXPANDED, VERBATIM, EXPANDED, TURNED: decalogue.sabbath_clauses by CALL", ['accepted'])
    if ask == 'keep_and_remember':
        ink('5:12', '"KEEP the sabbath day to sanctify it" against "REMEMBER the sabbath day to sanctify it" — %s / %s; both the infinitive absolute (%s; Exodus 20:8 %s)' % (P('שמור', 'את', 'יום', 'השבת'), P('זכור', 'את', 'יום', 'השבת'), INFA[12], wm('Exod', 20, 8)[0]))
        move('Shevuot 20b:9; Rosh Hashanah 27a:2, 27a:6', "'remember' and 'keep' spoken in ONE UTTERANCE — what the mouth cannot say nor the ear hear; two sounds from one source")
        move('Berakhot 20b:10', "Rava — whoever is in 'keep' is in 'remember': women obligated in kiddush by the Torah")
        dat('the row keep_and_remember; the Sifrei 233:1 the reading\'s exhibit')
        return out("keep and remember (5:12) — one utterance: the diff's first word the tradition's exhibit; women's kiddush (Berakhot 20b)", ['accepted'])
    if ask == 'the_ox_and_the_ass':
        ink('5:14', '"your ox and your ass and all your cattle" %s the one seat — Exodus 20:10\'s "your cattle"; the diff %s' % (P('ושורך', 'וחמרך', 'וכל', 'בהמתך'), DIFF(('Deut', 5, 14), ('Exod', 20, 10))[1]))
        move('Bava Kamma 54b:13', "R. Yosei in R. Yishmael's name — the ox and the ass specified inside 'all cattle' to teach EVERY ANIMAL wherever 'ox and ass' are written: muzzling (54b:10), diverse kinds (54b:11), unloading (54b:9, 54b:25)")
        move('decalogue.sabbath_clauses by CALL', "the laden beast — %r" % DC_LADEN[0])
        return out("the ox and the ass (5:14) — every animal by the verbal analogy: the expansion read by the tradition itself (Bava Kamma 54b)", ['accepted'])
    if ask == 'the_servants_rest':
        ink('5:14', '"that your servant and your maidservant may rest like you" %s the one seat; "like you" seven Torah seats' % P('למען', 'ינוח', 'עבדך', 'ואמתך'))
        move('Bava Kamma 54b:28', "Rav Acha bar Yaakov — people equated with animals for RESTING only: the analogy's limit")
        move('Yevamot 48b:5-6', "the circumcised slave rests by this clause, the uncircumcised by 23:12's; 'your stranger within your gates' the righteous convert, 23:12's the resident alien")
        return out("the servants' rest (5:14) — the circumcised slave and the righteous convert (Yevamot 48b); the analogy's limit (Bava Kamma 54b)", ['accepted'])
    if ask == 'the_two_grounds':
        ink('5:15', '"remember that you were a slave in Egypt … therefore the LORD your God commanded you to do the sabbath day" — the exodus for the creation; "the sabbath day" the shared run %s; "remember that you were a slave" %s' % (SHARED(('Deut', 5, 15), ('Exod', 20, 11)), P('וזכרת', 'כי', 'עבד', 'היית')))
        move('pre_sinai.sabbath by CALL', "the creation ground of 20:11 against Genesis 2:2-3 by token — %r" % (PS_DELTA['v'],))
        dat('the row the_sabbath_grounds: %s' % data['the_sabbath_grounds']['value'])
        return out("the two grounds (5:15) — the creation (20:11, PS by CALL) and the exodus: a DATA row; the readback row TURNED", ['accepted'])
    if ask == 'the_receipt_5_12':
        ink('5:12', '"AS THE LORD YOUR GOD COMMANDED YOU" — the receipt inside the code %s; the plural 5:32 %s' % (RECEIPT_SG, RECEIPT_PL))
        move('Sanhedrin 56b:16; Shabbat 87b:1 (ES.marah by CALL)', "Rav Yehuda — commanded AT MARAH: %s" % (ES_MARAH['v'],))
        dat("the row the_receipts: RUN CITATION of the giving (the tape's ten_words_declared); the register seat CHAPTER")
        return out("the receipt at 5:12 — a run citation of the giving (the ink) read as Marah (the teacher): the seat CHAPTER", ['accepted'])
    return out('no verdict in span', [FX.NONE])


# ===== F4: THE SECOND TABLET — the words five to ten read back (Deut 5:16-21) ============================
def the_second_tablet(case, data):
    del P_[:]
    ask = case['ask']
    if ask == 'the_fifth_word':
        ink('5:16', '"honor your father and your mother" %s — the infinitive absolute (%s); the diff %s' % (P('כבד', 'את', 'אביך', 'ואת', 'אמך'), INFA[16], DIFF(('Deut', 5, 16), ('Exod', 20, 12))))
        move('holiness.frame by CALL (Kiddushin 30b-31b)', "honor %s; fear %s; the order %r; the partners %s; the woman %r" % (HO_HONOR['v'], HO_FEAR['v'], HO_ORDER['v'], HO_THREE['v'], HO_WOMAN['v']))
        move('mishpatim_3 and sanctions by CALL', "the striker %r, the curser %r (the woman %r)" % (M3_STRIKE['v'], SA_CURSER['v'], M3_CURSE['v']))
        return out("the fifth word (5:16) — EXPANDED: NO CELL at the Decalogue's seat, holiness.frame by CALL (the honor and the fear defined, Kiddushin 31b)", ['accepted'])
    if ask == 'the_sixth_word':
        ink('5:17', '"you shall not murder" %s VERBATIM' % P('לא', 'תרצח'))
        move('mishpatim_3.killer and refuge.the_murderer by CALL', "the mode %r; %r" % (M3_KILL['v'], RF_MURD[0][:40]))
        return out("the sixth word (5:17) — VERBATIM: mishpatim_3.killer and refuge.the_murderer by CALL", ['accepted'])
    if ask == 'the_seventh_word':
        ink('5:18', '"and you shall not commit adultery" — the conjunction; %s' % U('תנאף'))
        move('sanctions.adultery by CALL', "the mode %r; %r" % (SA_ADULT['v'], SA_BOTH['v']))
        return out("the seventh word (5:18) — VARIANT: sanctions.adultery by CALL (Leviticus 20:10)", ['accepted'])
    if ask == 'the_eighth_word':
        ink('5:19', '"and you shall not steal" — the conjunction; %s; Leviticus 19:11\'s plural %s' % (U('תגנב'), P('לא', 'תגנבו')))
        move('decalogue.theft_commandment by CALL', "the kidnapper %r; money theft %r" % (DC_KID[0], DC_MONEY[0]))
        move('Sanhedrin 86a:15-17', "R. Yoshiya from 'you shall not steal' and R. Yochanan from Leviticus 25:42; the theft of PERSONS by the context; 19:11's of property by its context")
        return out("the eighth word (5:19) — VARIANT: the theft of persons by the context (Sanhedrin 86a); decalogue.theft_commandment by CALL", ['accepted'])
    if ask == 'the_ninth_word':
        ink('5:20', '"a VAIN witness" %s against "a FALSE witness" %s; "vain" %s' % (P('עד', 'שוא'), P('עד', 'שקר'), U('שוא', 'לשוא', books=T)))
        move('ordinances.courts by CALL', "the false report %r; the witness of violence %r" % (OR_FALSE['v'], OR_VIOL['v']))
        dat('the row the_ninth_word: %s' % data['the_ninth_word']['value'])
        return out("the ninth word (5:20) — TURNED: vain for false, the parameter a DATA row; ordinances.courts by CALL (23:1)", ['accepted'])
    if ask == 'the_tenth_word_row':
        ink('5:21', 'the tenth word — the diff %s' % DIFF(('Deut', 5, 21), ('Exod', 20, 17)))
        dat("the row names F5 the_tenth_word (this runner) — the code's hole filled")
        return out("the tenth word (5:21) — TURNED: the cell F5 (compiled here)", ['accepted'])
    if ask == 'the_reward_clause':
        ink('5:16', '"that your days may be long AND THAT IT MAY GO WELL WITH YOU" — %s the one seat; "be long" %s / %s' % (P('ולמען', 'ייטב', 'לך'), P('למען', 'יאריכן', 'ימיך'), P('למען', 'יארכון', 'ימיך')))
        move('Bava Kamma 55a:1', "why is 'good' written here and not in the first tablets? — sent to R. Tanchum bar Chanilai (the answer named: the first tablets were to be broken)")
        move('Chullin 110b:3; Chullin 142a:3; Kiddushin 39b:7, 40a:5', "the court not warned to enforce a mitzva whose reward is stated; the reward after the resurrection (R. Yaakov) or in this world (Rava)")
        return out("the reward clause (5:16) — the expansion's own Talmud row: 'good' not in the first tablets (Bava Kamma 55a)", ['accepted'])
    if ask == 'the_receipt_5_16':
        ink('5:16', '"AS THE LORD YOUR GOD COMMANDED YOU" — the second receipt inside the code (%s)' % RECEIPT_SG)
        move('Sanhedrin 56b:16', "honoring parents commanded at Marah (Rav Yehuda) — the teacher's referent; the ink's the giving (20:12)")
        return out("the receipt at 5:16 — a run citation of the giving read as Marah: the seat CHAPTER", ['accepted'])
    if ask == 'the_counts':
        ink('5:6-21', 'the two copies %s (tokens, letters) against %s; per word %s' % (COPIES[1], COPIES[0], WORD_TOK))
        dat('the row the_two_copies — recomputed from the DB')
        return out("the counts (5:6-21) — 189 tokens / 708 letters against 172 / 620: recomputed", ['accepted'])
    return out('no verdict in span', [FX.NONE])


# ===== F5: THE TENTH WORD — compiled here from both copies (Deut 5:21; Exodus 20:17) =======================
def the_tenth_word(case, data):
    del P_[:]
    ask = case['ask']
    if ask == 'covet_and_desire':
        ink('5:21', '"you shall not covet your neighbor\'s wife; you shall not DESIRE your neighbor\'s house" — "covet" %s; "desire" %s the hitpael\'s one seat (the root\'s %d seats)' % (U('תחמד'), U('תתאוה'), len(LEMV('183'))))
        dat("the row the_tenth_word: covet in deed, desire in the heart — the Mekhilta d'Rabbi Yishmael Bahodesh 8 (named, unopened); Onkelos 'and do not desire'")
        return out("covet and desire (5:21) — the two verbs: the tenth word compiled here; the block coveting_barred on Israel at the giving's line", ['accepted'])
    if ask == 'the_wife_first':
        ink('5:21', 'THE WIFE FIRST — Exodus 20:17 "your neighbor\'s house" first; "his field" added (%d seats); the diff %s' % (len(U('שדהו')), DIFF(('Deut', 5, 21), ('Exod', 20, 17))))
        dat("the row the_tenth_word: the order and 'his field' DATA — the readback row TURNED")
        return out("the wife first (5:21) — the order turned, his field added: a DATA row", ['accepted'])
    if ask == 'the_coveter_who_pays':
        ink('5:21', '"you shall not covet" — the bailee who keeps the deposit and pays')
        move('Bava Metzia 5b:19', "Rav Acha of Difti — taking by force or deceit violates 'you shall not covet' EVEN WITH PAYMENT")
        move('Bava Metzia 5b:20', "most people read 'you shall not covet' as taking WITHOUT payment — the bailee unaware, his oath credible: not disqualified as a robber")
        return out("the coveter who pays (5:21) — the prohibition stands (Rav Acha), the people's reading spares his oath: not a robber (Bava Metzia 5b)", ['exempt'])
    if ask == 'the_write':
        ink('5:21', 'the tenth word whole — the block written on Israel AT THE GIVING\'S LINE, never at the retelling\'s')
        dat("the write: coveting_barred on israel — law_covenant_at_horeb watches ten_words_declared")
        return out("the write (5:21) — coveting_barred on Israel: the code's hole filled at the code's own line", ['coveting_barred'])
    return out('no verdict in span', [FX.NONE])


# ===== F6: THE VOICE AND THE REQUEST (Deut 5:22-27) =========================================================
def the_voice_and_the_request(case, data):
    del P_[:]
    ask = case['ask']
    if ask == 'added_no_more':
        ink('5:22', '"these words the LORD spoke to all your assembly … with a great voice, and he added no more" — "to all your assembly" %s; "and added no more" %s; against 4:13 (tokens %d for %d, %d shared)' % (P('אל', 'כל', 'קהלכם'), P('ולא', 'יסף'), VOICE_DELTA[0], VOICE_DELTA[1], VOICE_DELTA[2]))
        move('obey_horeb.horeb_retold by CALL', "2b's supplied lines FOUND — %r; %r" % (OH_VOICE[1], OH_TABLETS[1]))
        move('Sanhedrin 17a:12; Sotah 10b:12', "'did not cease' — Eldad and Medad who did not stop; Judah who did not cease: Onkelos's reading")
        dat("'added no more' / 'did not cease' a DATA note; the readback row EXPANDED")
        return out("added no more (5:22) — 2b's ten words and tablets FOUND (OH by CALL); 'did not cease' the Talmud's and Onkelos's reading", ['accepted'])
    if ask == 'the_tablets_given_to_me':
        ink('5:22', '"and he wrote them on two tablets of stone and gave them to me" — "and gave them to me" %s; the tablets defective here (%s), plene at 4:13; [2] the parser\'s' % (P('ויתנם', 'אלי'), PT('Deut', 5, 22, 'לחת')))
        move('erection.tablets by CALL', "'the ten words' at %d seats" % ER_TEN['v'])
        return out("the tablets given to me (5:22) — tablets_given FOUND at (1, 4, 17); no second write", ['accepted'])
    if ask == 'you_came_near':
        ink('5:23', '"you came near to me, all the heads of your tribes and your elders" — %s the two seats (1:22 the mob); "the heads of your tribes" %s' % (P('ותקרבון', 'אלי'), P('ראשי', 'שבטיכם')))
        move('opening_speech.the_spies_read_back by CALL', "1:22's asking — %r" % OS_ASK[0][:60])
        move('the Sifrei 20:1 (credited at sitting 1)', "the mob there against the elders and the heads here")
        return out("you came near (5:23) — 1:22's phrase at its second seat: the mob and the elders (OS by CALL; the Sifrei 20:1)", ['accepted'])
    if ask == 'the_request':
        ink('5:24-27', '"go you near and hear … and you speak to us … and we will hear and do" — %s; "why should we die" %s; "the living God" %s; ninety-one tokens against Exodus 20:18\'s eighteen and 20:19\'s thirteen' % (P('קרב', 'אתה', 'ושמע'), P('למה', 'נמות'), P('אלהים', 'חיים')))
        dat("THE TAPE'S SECOND HOLE: Exodus 20:18-19 has no line (20:18 in no span; 20:19-21 the ordinances' cells) — SUPPLIED, dated (1, 3, 7) by the retrograde marker at 5:23 (Rabbi Yose's seventh, ES by CALL: %s)" % (ES_DAYS['v'],))
        move('Makkot 24a:1', "the first two words direct, the rest through Moses — the mediator's row")
        return out("the request (5:24-27) — SUPPLIED: the tape's second hole written once at its own time; the mediator asked for (Makkot 24a)", ['accepted'])
    if ask == 'hear_and_do':
        ink('5:27', '"WE WILL HEAR AND DO" %s against Exodus 24:7\'s "we will do and hear" %s; "we will do" at %s' % (P('ושמענו', 'ועשינו'), P('נעשה', 'ונשמע'), ES_SEATS['v']))
        move('Shabbat 88a:7-9', "R. Simai — 'we will do' before 'we will hear': two crowns; the angels' secret (R. Elazar); the heretic's 'impulsive nation'")
        move('Shabbat 88a:5 (ES.sinai by CALL)', "the mountain overturned like a tub — %r" % ES_TUB['v'])
        return out("hear and do (5:27) — TURNED against 24:7's 'do and hear' (Shabbat 88a); Onkelos 'accept and do'", ['accepted'])
    if ask == 'the_write':
        ink('5:23-27', 'the request whole — the SUPPLIED line writes torah_through_moses on Israel')
        dat("the write: torah_through_moses on israel dated (1, 3, 7) — Avot 1:1's vocabulary; Makkot 24a's two words")
        return out("the write (5:23-27) — torah_through_moses on Israel: the mediator's status", ['torah_through_moses'])
    return out('no verdict in span', [FX.NONE])


# ===== F7: THE ANSWER AND THE CHARGE (Deut 5:28-33) ========================================================
def the_answer_and_the_charge(case, data):
    del P_[:]
    ask = case['ask']
    if ask == 'the_lord_heard':
        ink('5:28', '"and the LORD heard the voice of your words" %s — 1:34\'s five words (the wrath there, the praise here); the one divine frame %s' % (P('וישמע', 'יהוה', 'את', 'קול', 'דבריכם'), DIV))
        move('opening_speech.the_spies_read_back by CALL', "1:34's oath — %r" % OS_OATH[0][:40])
        return out("the LORD heard (5:28) — 1:34's phrase at its second seat (OS by CALL)", ['accepted'])
    if ask == 'done_well':
        ink('5:28', '"they have done well in all that they have spoken" %s — 18:17 cites it forward (%s)' % (P('היטיבו', 'כל', 'אשר', 'דברו'), U('היטיבו')))
        dat("'they have done well' a DATA note; the prophet's promise (18:15-19) chapter 18's sitting; Onkelos 'rightly'")
        return out("they have done well (5:28) — cited forward at 18:17: a DATA note", ['accepted'])
    if ask == 'who_would_give':
        ink('5:29', '"who would give that they had such a heart as this always" %s — "who would give" %d seats (Job\'s nine)' % (P('מי', 'יתן', 'והיה', 'לבבם', 'זה', 'להם'), len(P('מי', 'יתן'))))
        move('Avodah Zarah 4b:17-5a:21', "the calf made to give a claim to penitents; 'with their children forever' those who stood at Sinai; the Angel of Death's decree; 'ingrates' — they should have said 'give us the heart'")
        return out("who would give (5:29) — the calf and the penitents (Avodah Zarah 4b-5a): an aggadah on the answer's verse", ['accepted'])
    if ask == 'return_to_your_tents':
        ink('5:30', '"go say to them: return to your tents" %s — "to your tents" %s; the imperatives %s' % (P('שובו', 'לכם', 'לאהליכם'), U('לאהליכם'), IMPER[30]))
        move('Beitzah 5a:7, 5b:3', "Rav Yosef — the separation of 19:15 released by an explicit word: a matter forbidden by a count needs a count to permit")
        move('Moed Katan 7b:5; Sanhedrin 59b:3-4 (PS.noahide by CALL)', "'his tent' his wife; procreation repeated at Sinai — %r" % PS_PROCR['v'])
        return out("return to your tents (5:30) — the separation released: returned_to_tents on Israel (Beitzah 5a-b)", ['returned_to_tents'])
    if ask == 'stand_here_with_me':
        ink('5:31', '"and you, stand here with me, and I will speak to you all the commandment and the statutes and the judgments which you shall teach them" %s; "which you shall teach them" %s; "all the commandment and the statutes and the judgments" %s (6:1 without "all")' % (P('ואתה', 'פה', 'עמד', 'עמדי'), P('אשר', 'תלמדם'), P('את', 'כל', 'המצוה', 'והחקים', 'והמשפטים')))
        move('erection.ascent by CALL', "Exodus 24:12's 'to teach them' — the pair at %d seats" % ER_TORAH['v'])
        move('Megillah 21a:14; the Sifrei 357:40 (credited)', "the Torah received standing; Moses prophesied standing")
        dat("THE CHARGE TO TEACH a DEBIT on Moses CLOSED AT ONCE BY THE PRIOR RUN — the closer speech_opened at 1:1-5 (OS.the_frame: %r); 4:5's receipt the same run" % OS_WRITE[1])
        return out("stand here with me (5:31) — SUPPLIED: the charge to teach a debit on Moses closed by the prior run (Deut 1:5); the Torah received standing", ['commanded'])
    if ask == 'the_charge':
        ink('5:32-33', '"you shall observe to do as the LORD your God commanded you; you shall not turn aside right or left" %s — "right or left" %s (17:11 the judges\'); "in all the way" six seats; the plural receipt %s' % (P('לא', 'תסרו', 'ימין', 'ושמאל'), P('ימין', 'ושמאל'), RECEIPT_PL))
        dat("NO WRITE (the frame's charge); the receipt 5:32 a run citation of the giving — the seat CHAPTER; the forward marker at 5:32 ends the stretch")
        return out("the charge (5:32-33) — no write: the frame's close; the plural receipt's seat CHAPTER", ['accepted'])
    if ask == 'the_readback_table':
        dat('the row the_readback: %d rows — %s; the law rows %d, the cells named %d, NO CELL %s' % (len(READBACK), dict(RB_GRADES), sum(1 for r in READBACK if r['law']), sum(1 for r in READBACK if r['law'] and r['cell'] != 'NO CELL'), [r['verses'] for r in READBACK if r['cell'] == 'NO CELL']))
        return out("the readback table — twenty-one rows graded (sixteen on the code, five on the narrative); no row open", ['accepted'])
    if ask == 'the_register_seats':
        dat('the row the_receipts: %s; Deut 4:45 DAEMONS 2 unmoved (the new daemon\'s seat Exodus 20:3 outside the block)' % data['the_receipts']['value'])
        return out("the register seats — Deut 5:12, 5:16, 5:32 CHAPTER (the gate's code); 4:45 DAEMONS 2", ['accepted'])
    return out('no verdict in span', [FX.NONE])

# ---- THE CALLEES' FACTS (every edge live at the cells that consume them; the values asserted from the callees' own prints — ch5_callees.out) ----
DC_VAINOATH = DC.vain_name({'ask': 'vain_oath'}, DC.DATA); DC_VAIN = DC.vain_name({'ask': 'vain_and_false_utterance'}, DC.DATA); DC_REM = DC.sabbath_clauses({'ask': 'remember'}, DC.DATA); DC_SCOPE = DC.sabbath_clauses({'ask': 'labor_scope'}, DC.DATA); DC_LADEN = DC.sabbath_clauses({'ask': 'laden_beast'}, DC.DATA); DC_KID = DC.theft_commandment({'ask': 'kidnapper'}, DC.DATA); DC_MONEY = DC.theft_commandment({'ask': 'money_theft_here'}, DC.DATA)
assert DC_VAINOATH[:2] == ('lashes', ['lashes']) and DC_VAIN[0] == 'spoken as one' and DC_REM[:2] == ('sanctify over wine', ['sanctify_day']) and DC_SCOPE[:2] == ('the whole household barred', ['labor_barred', 'rest_required']) and DC_LADEN[:2] == ('driving the laden beast barred', ['labor_barred']) and DC_KID[:2] == ('capital — the kidnapper', ['put_to_death']) and DC_MONEY[0] == 'routed to the ordinances span' and DC.GUARDED == 13, (DC_VAIN[0], DC_KID[:2])
OH_LIST = OH.DATA['the_no_image_list']['value']; OH_HOLE = OH.DATA['the_horeb_hole']['value']; OH_VOICE = OH.horeb_retold({'ask': 'the_voice_and_no_form'}, OH.DATA); OH_TABLETS = OH.horeb_retold({'ask': 'the_ten_words_and_the_tablets'}, OH.DATA)
assert len(OH_LIST) == 11 and OH_LIST[0] == 'a graven image' and OH_HOLE == {'exod_20_1': 'no_line_on_the_tape', 'exod_31_18': 'no_line_on_the_tape'} and OH_VOICE[1] == ['covenant_declared'] and OH_TABLETS[1] == ['tablets_delivered'] and len(OH.READBACK) == 11 and OH.GRADES == ('VERBATIM', 'TURNED', 'SHORTENED', 'EXPANDED', 'SUPPLIED', 'DISAGREES'), (len(OH_LIST), OH_VOICE[1])
ER_SPEECH = ER.presence('speech_with_speech'); ER_BOOK = ER.blood_covenant('book_of_covenant'); ER_VOICE1 = ER.blood_covenant('one_voice'); ER_TEN = ER.tablets('ten_words'); ER_TORAH = ER.ascent('torah_mitzvah')
assert ER_SPEECH['v'] == 'speech_with_speech' and ER_BOOK['v'] == 4 and ER_VOICE1['v'] == 2 and ER_TEN['v'] == 3 and ER_TORAH['v'] == 2, (ER_SPEECH['v'], ER_BOOK['v'], ER_VOICE1['v'], ER_TEN['v'], ER_TORAH['v'])
ES_DAYS = ES.sinai('days_r_yose'); ES_SEATS = ES.sinai('we_will_do_seats'); ES_TUB = ES.sinai('tub'); ES_MARAH = ES.marah('statute_list')
assert ES_DAYS['v'] == (2, 3, 4, 7) and ES_SEATS['v'] == [(19, 8), (24, 3), (24, 7)] and ES_TUB['v'] == 'the_mountain_held_over_them_like_a_tub' and ES_MARAH['v'] == ('seven_of_the_sons_of_noah', 'courts', 'sabbath', 'honoring_father_and_mother'), (ES_DAYS['v'], ES_SEATS['v'], ES_MARAH['v'])
OS_ASK = OS.the_spies_read_back({'ask': 'the_asking'}, OS.DATA); OS_OATH = OS.the_spies_read_back({'ask': 'the_oath'}, OS.DATA); OS_WRITE = OS.the_frame({'ask': 'the_write'}, OS.DATA)
assert OS_ASK[0].startswith('the asking (1:22)') and OS_OATH[0].startswith('the oath (1:34-36)') and OS_WRITE[1] == ['torah_expounded'] and len(OS.READBACK) == 42 and callable(OS._closed_by_prior_run), (OS_ASK[0][:30], OS_OATH[0][:30], OS_WRITE[1])
HO_HONOR = HO.frame('honor_defined'); HO_FEAR = HO.frame('fear_defined'); HO_ORDER = HO.frame('parents_order'); HO_THREE = HO.frame('three_partners'); HO_WOMAN = HO.frame('woman_included')
assert HO_HONOR['v'] == ['feed', 'give_drink', 'clothe', 'cover', 'bring_in', 'take_out'] and HO_FEAR['v'] == ['not_sit_in_his_place', 'not_speak_in_his_place', 'not_contradict_him'] and HO_ORDER['v'] == 'mother_first_here_father_first_at_Sinai_both_equal' and HO_THREE['v'] == ['God', 'father', 'mother'] and HO_WOMAN['v'] == 'woman_bound_to_fear_when_able', (HO_HONOR['v'], HO_FEAR['v'], HO_ORDER['v'])
M3_KILL = M3.killer('mode'); M3_STRIKE = M3.parent_striker('mode'); M3_CURSE = M3.parent_curser('the_woman')
assert M3_KILL['v'] == 'the_sword' and M3_STRIKE['v'] == 'strangling' and M3_CURSE['v'] == 'included', (M3_KILL['v'], M3_STRIKE['v'], M3_CURSE['v'])
SA_ADULT = SA.adultery('mode'); SA_BOTH = SA.adultery('both'); SA_CURSER = SA.curser('mode')
assert SA_ADULT['v'] == 'strangling' and SA_BOTH['v'] == 'the_adulterer_and_the_adulteress' and SA_CURSER['v'] == 'stoning', (SA_ADULT['v'], SA_BOTH['v'], SA_CURSER['v'])
RF_MURD = RF.the_murderer({'ask': 'he_is_a_murderer'}, RF.DATA)
assert RF_MURD[0].startswith('he is a murderer (35:16-18, 21)') and RF_MURD[1] == ['put_to_death'], RF_MURD[:2]
OR_FALSE = OR.courts('false_report'); OR_VIOL = OR.courts('witness_of_violence')
assert OR_FALSE['v'] == 'hapax' and OR_VIOL['v'] == 'robbers_disqualified', (OR_FALSE['v'], OR_VIOL['v'])
PS_DELTA = PS.sabbath('delta_20_11'); PS_REPEAT = PS.noahide('repeated_at_sinai'); PS_PROCR = PS.noahide('procreation_israel')
assert PS_DELTA['v'] == (18, 22, True, True) and PS_REPEAT['v'] == 'the_repetition_is_the_edge' and PS_PROCR['v'] == 'israel_only_by_the_framework', (PS_DELTA['v'], PS_REPEAT['v'], PS_PROCR['v'])


# ===== THE WRAP (D9-iv): the daemon over the cells — the ledger written, no event emitted =====================
def law_covenant_at_horeb(event, world):
    """Deut 5:1-33 (cold_run_covenant_at_horeb.py F1-F7). given_at Exodus 20:3 — THE SECOND WORD'S FIRST GIVING, its code compiled here from the
    second copy (5:7-10) with the first, and the tenth word's (5:21 with 20:17): THE CODE'S HOLE FILLED FROM THE RETELLING'S SEAT; installed_by
    covenant_blood_thrown (law_decalogue's own installer). THE BLOCKS WRITTEN AT THE CODE'S OWN LINE: the daemon watches 2b's supplied line
    ten_words_declared (dated (1, 3, 7)) and writes other_gods_barred and coveting_barred there — never at the retelling's (THE REST's one declared
    delta). TWO TAPE LINES of its own, both SUPPLIED and dated (1, 3, 7) by the retrograde marker at Deut 5:23: the request for a mediator (the
    tape's second hole — torah_through_moses on Israel) and the answer (the charge to teach a DEBIT on Moses CLOSED AT ONCE BY THE PRIOR RUN — the
    opening speech's form, the closer Deut 1:5; return to your tents a STATUS on Israel). The exam's case kind dispatches to the cells in EXPLICIT
    branches with LITERAL effects per kind (an unnamed effect is a KeyError). No timer."""
    k, src = event['kind'], event['case_source']
    E_ = lambda eff, s, cp=None, amount=None, due=None, law='', value=None: {'effect': eff, 'subject': s, 'counterparty': cp, 'amount': amount, 'due': due, 'value': value if value is not None else True, 'source_law': law, 'case_source': src}
    if k == 'ten_words_declared':
        return [E_('other_gods_barred', 'israel', value='no other gods before me; no graven image nor any form; not bow down to them nor serve them — the bower, the slaughterer, the incense-burner, the libation-pourer stoned (Mishnah Sanhedrin 7:6; Sanhedrin 60b), the hugger and the kisser a prohibition; the visiting to the third and the fourth generation, mercy to thousands (5:7-10 / 20:3-6)', law='F2 [INK 5:7-10 with Exodus 20:3-6 — THE SECOND WORD, compiled at THE DEUTERONOMY WALK 3b from its second copy (no cell in any runner before): a BLOCK on Israel written at the giving\'s own line (2b\'s ten_words_declared, dated (1, 3, 7)); the answer sheet Mishnah Sanhedrin 7:6 with Sanhedrin 60b:1-19 — the mode stoning by the juxtaposition of Deut 17:3 to 17:5, the prohibition of bowing from Exodus 34:14; the no-image list 4:16-19 the parameter table (OH by CALL)]'),
                E_('coveting_barred', 'israel', value="you shall not covet your neighbor's wife; you shall not desire your neighbor's house, his field, his servant, his maidservant, his ox, his ass, anything that is your neighbor's (5:21 / 20:17) — taking by force or deceit even with payment (Bava Metzia 5b:19); most people read it as without payment (5b:20)", law="F5 [INK 5:21 with Exodus 20:17 — THE TENTH WORD, compiled at THE DEUTERONOMY WALK 3b from its second copy (no cell in any runner before): a BLOCK on Israel written at the giving's own line; the wife first here, the house first there, 'desire' for the second covet, 'his field' added; Bava Metzia 5b:19-20 the answer sheet]")]
    if k == 'mediator_requested':
        return [E_('torah_through_moses', 'israel', value={'the_request': 'go you near and hear all that the LORD our God shall say, and you speak to us all that the LORD our God speaks to you, and we will hear and do (5:27)', 'the_first_telling': 'Exodus 20:18-19 — speak you with us and we will hear, but let not God speak with us lest we die', 'dated': (1, 3, 7), 'the_hole': "no line on the tape for Exodus 20:18-21 until this one (the laws' readback's finding)", 'makkot_24a': "the first two words from the Almighty's mouth, the rest through Moses"}, law="F6 [INK 5:23-27 'when you heard the voice … you came near to me, all the heads of your tribes and your elders … go you near and hear … and we will hear and do' — THE TAPE'S SECOND HOLE (Exodus 20:18-19 the first telling; 20:18 in no runner's span, 20:19-21 the ordinances' law cells): written ONCE at its own time, dated (1, 3, 7) by the retrograde marker at 5:23 (Rabbi Yose's seventh, ES.sinai by CALL); a STATUS on Israel — Avot 1:1's vocabulary, Makkot 24a:1's count; 'we will hear and do' against 24:7's order (Shabbat 88a)]")]
    if k == 'stand_here_commanded':
        eff = E_('commanded', 'moses', value='teach_the_commandment', law="F7 [INK 5:31 'and you, stand here with me, and I will speak to you all the commandment and the statutes and the judgments WHICH YOU SHALL TEACH THEM' — TOLD ONLY IN THE RETELLING (Exodus 20:22's answer another speech; 18:16-17 forward): written once, dated (1, 3, 7) inside the retrograde stretch of 5:23, CLOSED AT ONCE BY THE PRIOR RUN — the book's own expounding (1:5) and 4:5's 'I have taught you … as the LORD my God commanded me' (Exodus 24:12's 'to teach them', ER.ascent by CALL); Megillah 21a:14 the Torah received standing; the Sifrei 357:40]")
        eff['written_by'] = 'law_covenant_at_horeb'
        OS._closed_by_prior_run(world, event, eff, "Deut 1:5 — beyond the Jordan, in the land of Moab, Moses undertook to expound this Torah, saying: THE CLOSE BY A PRIOR RUN (R3) — the charge to teach given at Horeb (5:31, told only in the retelling) ran at the book's own opening (the frame's line 1:1-5, torah_expounded) and at the exhortation's receipt 'I have taught you statutes and judgments as the LORD my God commanded me' (4:5), the tape's earlier lines; the command came to the reader after its execution (the closer names 1:5 alone — a range would fold 1:3's receipt into a CLOSE, the gate's class by containment)")
        return [E_('returned_to_tents', 'israel', value={'the_word': 'go say to them: return to your tents (5:30)', 'released': "the separation of Exodus 19:15 — 'do not come near a woman' (the tape's people_sanctified, 19:10-15)", 'dated': (1, 3, 7), 'beitzah_5a': 'a matter forbidden by a count needs a count to permit (Rav Yosef)', 'moses': "and you, stand here with me — Moses' own separation agreed (Shabbat 87a; Yevamot 62a)"}, law="F7 [INK 5:30 'go say to them: return to your tents' — a STATUS on Israel: the separation of Exodus 19:15 released by an explicit word (Beitzah 5a:7-5b:3; Moed Katan 7b:5 'his tent' his wife; Sanhedrin 59b:3-4 procreation repeated at Sinai — PS.noahide by CALL); told only in the retelling, dated (1, 3, 7)]")]
    if k == 'horeb_covenant_case':
        fn = {'assembly': the_assembly_called, 'second': the_second_word, 'first_tablet': the_first_tablet, 'second_tablet': the_second_tablet, 'tenth': the_tenth_word, 'voice': the_voice_and_the_request, 'answer': the_answer_and_the_charge}[event['cell']]
        v, e, _ = fn({'ask': event['ask']}, DATA); L = '%s [%s]' % ({'assembly': 'F1', 'second': 'F2', 'first_tablet': 'F3', 'second_tablet': 'F4', 'tenth': 'F5', 'voice': 'F6', 'answer': 'F7'}[event['cell']], event['ask']); s_ = event['person']
        W = {'accepted': E_('accepted', s_, value=v, law=L), 'exempt': E_('exempt', s_, value=v, law=L), 'put_to_death': E_('put_to_death', s_, value='stoned — ' + v, law=L)}
        return [W[x] for x in e if x != FX.NONE]
    return []


LINES = [
    ('Deut 5:23-27 — and it came to pass, when you heard the voice out of the midst of the darkness, while the mountain burned with fire, that you came near to me, all the heads of your tribes and your elders, and you said: behold, the LORD our God has shown us his glory and his greatness, and his voice we have heard out of the midst of the fire; this day we have seen that God speaks with man and he lives; now therefore why should we die? for this great fire will consume us; if we hear the voice of the LORD our God any more, we shall die; for who is there of all flesh that has heard the voice of the living God speaking out of the midst of the fire, as we have, and lived? go you near and hear all that the LORD our God shall say, and you speak to us all that the LORD our God speaks to you, and we will hear and do',),
    ('Deut 5:28-31 — and the LORD heard the voice of your words when you spoke to me; and the LORD said to me: I have heard the voice of the words of this people which they have spoken to you; they have done well in all that they have spoken; who would give that they had such a heart as this always, to fear me and keep all my commandments, that it might be well with them and with their children forever; go say to them: return to your tents; but as for you, stand here with me, and I will speak to you all the commandment and the statutes and the judgments which you shall teach them, that they may do them in the land which I give them to possess',),
]
CLOSES = "one — the charge to teach (commanded on Moses, teach_the_commandment) CLOSED inside the daemon by the prior run, the closer Deut 1:5's expounding; no second write at 5:22 (the voice and the tablets FOUND); the frame and the charge no write"

PERSONS = [
    ('the-bower', 'second', 'bow_and_serve', "Mishnah Sanhedrin 7:6; Sanhedrin 60b:11 — the exam's row bow_and_serve"),
    ('the-stone-thrower-at-markulis', 'second', 'in_its_way', "Mishnah Sanhedrin 7:6; Sanhedrin 60b:3 — the exam's row in_its_way"),
    ('the-embracer', 'second', 'the_embracer', "Mishnah Sanhedrin 7:6; Sanhedrin 60b:2 — the exam's row the_embracer"),
    ('the-coveter-who-pays', 'tenth', 'the_coveter_who_pays', "Bava Metzia 5b:19-20 — the exam's row the_coveter_who_pays"),
    ('the-woman-at-kiddush', 'first_tablet', 'keep_and_remember', "Berakhot 20b:10 — the exam's row keep_and_remember"),
    ('the-laden-beast-s-driver', 'first_tablet', 'the_ox_and_the_ass', "Bava Kamma 54b:13 — the exam's row the_ox_and_the_ass"),
    ('the-circumcised-slave', 'first_tablet', 'the_servants_rest', "Yevamot 48b:5 — the exam's row the_servants_rest"),
    ('the-vain-swearer', 'first_tablet', 'the_third_word', "Mishnah Shevuot 3:8 — the exam's row the_third_word"),
    ('the-son-who-feeds-pheasant', 'second_tablet', 'the_fifth_word', "Kiddushin 31a:14 — the exam's row the_fifth_word"),
    ('the-abductor-of-persons', 'second_tablet', 'the_eighth_word', "Sanhedrin 86a:16 — the exam's row the_eighth_word"),
    ('the-one-who-said-we-will-do-first', 'voice', 'hear_and_do', "Shabbat 88a:7 — the exam's row hear_and_do"),
]


def scene():
    """THE SCENE — the exam's rows replayed on the world engine (the exodus epoch): the exam's persons through horeb_covenant_case — the second
    word's idolater and embracer, the coveter who pays, the woman at kiddush, the laden beast, the slave's rest, the vain oath, the honor, the
    theft of persons, 'we will do' first."""
    with contextlib.redirect_stdout(io.StringIO()):
        w = WE.World(era='Deut 5:1-33: chapter 5 on the shelf — Sanhedrin, Bava Metzia, Berakhot, Bava Kamma, Yevamot, Shevuot, Kiddushin, Shabbat on the engine (the exodus epoch)', epoch='exodus')
        w.laws = [law_covenant_at_horeb]
        w.advance(w.clock.day_in('exodus', 40, 11, 1))
        # THE DAEMON GATE READS LITERAL SUBMITS ONLY — the eleven persons typed out from PERSONS
        w.submit({'kind': 'horeb_covenant_case', 'subject': 'the-bower', 'person': 'the-bower', 'cell': 'second', 'ask': 'bow_and_serve', 'case_source': "Mishnah Sanhedrin 7:6; Sanhedrin 60b:11 — the exam's row bow_and_serve"})
        w.submit({'kind': 'horeb_covenant_case', 'subject': 'the-stone-thrower-at-markulis', 'person': 'the-stone-thrower-at-markulis', 'cell': 'second', 'ask': 'in_its_way', 'case_source': "Mishnah Sanhedrin 7:6; Sanhedrin 60b:3 — the exam's row in_its_way"})
        w.submit({'kind': 'horeb_covenant_case', 'subject': 'the-embracer', 'person': 'the-embracer', 'cell': 'second', 'ask': 'the_embracer', 'case_source': "Mishnah Sanhedrin 7:6; Sanhedrin 60b:2 — the exam's row the_embracer"})
        w.submit({'kind': 'horeb_covenant_case', 'subject': 'the-coveter-who-pays', 'person': 'the-coveter-who-pays', 'cell': 'tenth', 'ask': 'the_coveter_who_pays', 'case_source': "Bava Metzia 5b:19-20 — the exam's row the_coveter_who_pays"})
        w.submit({'kind': 'horeb_covenant_case', 'subject': 'the-woman-at-kiddush', 'person': 'the-woman-at-kiddush', 'cell': 'first_tablet', 'ask': 'keep_and_remember', 'case_source': "Berakhot 20b:10 — the exam's row keep_and_remember"})
        w.submit({'kind': 'horeb_covenant_case', 'subject': 'the-laden-beast-s-driver', 'person': 'the-laden-beast-s-driver', 'cell': 'first_tablet', 'ask': 'the_ox_and_the_ass', 'case_source': "Bava Kamma 54b:13 — the exam's row the_ox_and_the_ass"})
        w.submit({'kind': 'horeb_covenant_case', 'subject': 'the-circumcised-slave', 'person': 'the-circumcised-slave', 'cell': 'first_tablet', 'ask': 'the_servants_rest', 'case_source': "Yevamot 48b:5 — the exam's row the_servants_rest"})
        w.submit({'kind': 'horeb_covenant_case', 'subject': 'the-vain-swearer', 'person': 'the-vain-swearer', 'cell': 'first_tablet', 'ask': 'the_third_word', 'case_source': "Mishnah Shevuot 3:8 — the exam's row the_third_word"})
        w.submit({'kind': 'horeb_covenant_case', 'subject': 'the-son-who-feeds-pheasant', 'person': 'the-son-who-feeds-pheasant', 'cell': 'second_tablet', 'ask': 'the_fifth_word', 'case_source': "Kiddushin 31a:14 — the exam's row the_fifth_word"})
        w.submit({'kind': 'horeb_covenant_case', 'subject': 'the-abductor-of-persons', 'person': 'the-abductor-of-persons', 'cell': 'second_tablet', 'ask': 'the_eighth_word', 'case_source': "Sanhedrin 86a:16 — the exam's row the_eighth_word"})
        w.submit({'kind': 'horeb_covenant_case', 'subject': 'the-one-who-said-we-will-do-first', 'person': 'the-one-who-said-we-will-do-first', 'cell': 'voice', 'ask': 'hear_and_do', 'case_source': "Shabbat 88a:7 — the exam's row hear_and_do"})
    n = lambda eid, eff: len([e for e in w.entity(eid).ledger if e['effect'] == eff])
    tset = len([l for l in w.log if l[0] == 'TIMER-SET']); tfire = len([l for l in w.log if l[0] == 'TIMER-FIRE']); tcan = len([l for l in w.log if l[0] == 'TIMER-CANCEL'])
    closes = len([e for ent in w.entities.values() for e in ent.ledger if e.get('closed_by')])
    return (tuple(n(p, 'accepted') + n(p, 'exempt') + n(p, 'put_to_death') for p, _, _, _ in PERSONS), (n('the-embracer', 'exempt'), n('the-coveter-who-pays', 'exempt'), n('the-bower', 'put_to_death'), n('the-stone-thrower-at-markulis', 'put_to_death')), (tset, tfire, tcan, len(w.timers)), len(w.entities), closes), w
SCENE, _W = scene()
# THE PREDICTION (typed before the first run — the design's arithmetic): every exam person written once; the two exempt arms and the two stoned
# ONE each; no timer; ENTITIES the eleven persons; CLOSES 0.
SCENE_PREDICTED = ((1,) * 11, (1, 1, 1, 1), (0, 0, 0, 0), 11, 0)
assert SCENE == SCENE_PREDICTED, ('THE DEUTERONOMY WALK 3b: the scene moved from its prediction', SCENE, SCENE_PREDICTED)


def narrative():
    """THE DEUTERONOMY WALK 3b (2026-09-16): the chapter's own acts AS HISTORY — the two SUPPLIED lines dated (1, 3, 7) by the RETROGRADE marker at
    Deut 5:23 (the giving's day), the stretch ENDED by a FORWARD marker at 5:32 back to the speech's day — on a world with this runner's daemon:
    3 writes (torah_through_moses; the charge's debit; returned_to_tents), no timer, TWO entities (Israel, Moses), the counter at (11, 1), ONE close
    (the charge closed by the prior run — the closer's line absent from this bare world, the close still the daemon's own), no row, TWO dated lines.
    The blocks at the giving's line are the TAPE's (the giving line is 2b's, not replayed here — the recorder attributes every submit to its scene).
    Recorded by the sequential run's recorder and stitched onto the tape (the markers the stitcher's rows). Not a graded cell: the tuple below is a
    tripwire typed from the design."""
    with contextlib.redirect_stdout(io.StringIO()):
        w = WE.World(era='Deut 5:1-33 on the tape — the request for a mediator and the answer, dated at the giving (the exodus epoch)', epoch='exodus')
        w.laws = [law_covenant_at_horeb]
        w.advance(w.clock.day_in('exodus', 40, 11, 1))
        # THE DAEMON GATE READS LITERAL SUBMITS ONLY — the two lines typed out; no field named `until`, `days` or `due`
        w.marker('Deut 5:23', w.clock.day_in('exodus', 1, 3, 7), value='the request told — dated at the giving (Exod 19:16): RETROGRADE', placement='reading_placed')
        w.submit({'kind': 'mediator_requested', 'subject': 'israel', 'first_telling': 'Exod 20:18-19', 'dated': 'the giving (1, 3, 7)', 'request': 'go you near and hear … and we will hear and do (5:27)', 'case_source': LINES[0][0]})
        w.submit({'kind': 'stand_here_commanded', 'subject': 'moses', 'first_telling': 'told only here — Deut 18:16-17 forward', 'dated': 'the giving (1, 3, 7)', 'answer': 'they have done well; return to your tents; stand here with me (5:28-31)', 'case_source': LINES[1][0]})
        w.marker('Deut 5:32', w.clock.day_in('exodus', 40, 11, 1), value='the charge at the speech\'s own day — the stretch ENDED: FORWARD (2b\'s lesson 1)')
    writes = len([l for l in w.log if l[0] == 'WRITE'])
    closes = len([e for ent in w.entities.values() for e in ent.ledger if e.get('closed_by')])
    rows = len([l for l in w.log if l[0] == 'ROW'])
    dated = len([l for l in w.log if l[0] == 'EVENT' and l[2].get('dated') is not None])
    return (writes, len([l for l in w.log if l[0] == 'TIMER-SET']), len(w.entities), w.clock.eras['exodus'].date(w.clock.day)[1:], closes, rows, len(w.tables['population']), dated), w


NARRATIVE, _WN = narrative()
NARRATIVE_PREDICTED = (3, 0, 2, (11, 1), 1, 0, 0, 2)   # DEUTERONOMY_WALK.md "Sitting 3b": 3 writes, no timer, TWO entities, the counter's day (11, 1), ONE close (the charge by the prior run), no row, TWO dated lines
assert NARRATIVE == NARRATIVE_PREDICTED, ('THE DEUTERONOMY WALK 3b: the chapter\'s narrative moved from its prediction', NARRATIVE, NARRATIVE_PREDICTED)
_isr = _WN.entity('israel').ledger
assert [e['effect'] for e in _isr] == ['torah_through_moses', 'returned_to_tents'] and [(e['effect'], e.get('value'), bool(e.get('closed_by'))) for e in _WN.entity('moses').ledger] == [('commanded', 'teach_the_commandment', True)], ([e['effect'] for e in _isr], [e['effect'] for e in _WN.entity('moses').ledger])
assert [ex.date(l[2]['dated']) for l in _WN.log if l[0] == 'EVENT' and l[2].get('dated') is not None for ex in [_WN.clock.eras['exodus']]] == [(1, 3, 7), (1, 3, 7)], 'the two supplied lines dated by the marker at 5:23'


# =====================================================================
# Motion 2 — THE TEST DATA: the answer sheet's rows (the docket's LAW rows and the cells' asks) — GENERATED FROM THE CELLS' OWN ASKS by ch5_cases_gen.py
# (1b's lesson: a mistyped expected string grades nothing), then frozen as literals under the honest-pairing guard.
# =====================================================================
CASES = [
    # F1 — the_assembly_called
    ('Deut 5:1 — hear_learn_keep_do', lambda: the_assembly_called({'ask': 'hear_learn_keep_do'}, DATA), "hear, learn, keep, do (5:1) — the second speech opened: Moses' call to all Israel, the four verbs in order; the frame's second seat, no write"),
    ('Deut 5:2 — the_covenant_at_horeb', lambda: the_assembly_called({'ask': 'the_covenant_at_horeb'}, DATA), "the covenant at Horeb (5:2) — the tape's covenant READ BACK: the book and the blood (ER by CALL); forty-eight covenants per mitzva (Sotah 37b); the second copy a third saying (R. Akiva)"),
    ('Deut 5:3 — not_with_our_fathers', lambda: the_assembly_called({'ask': 'not_with_our_fathers'}, DATA), 'not with our fathers (5:3) — the covenant with the living here: a DATA note against 29:13-14, no link of our own'),
    ('Deut 5:4 — face_in_face', lambda: the_assembly_called({'ask': 'face_in_face'}, DATA), "face in face (5:4) — the one seat of the form; Onkelos 'speech with speech' (ER by CALL); all Israel heard the voice (Yoma 4b)"),
    ('Deut 5:5 — i_stood_between', lambda: the_assembly_called({'ask': 'i_stood_between'}, DATA), "I stood between (5:5) — the mediator: the first two words direct, the rest through Moses (Makkot 24a); the request's row"),
    # F2 — the_second_word
    ('Deut 5:7 — no_other_gods', lambda: the_second_word({'ask': 'no_other_gods'}, DATA), "no other gods before me (5:7) — the second word's head, compiled here: the block other_gods_barred on Israel at the giving's line"),
    ('Deut 5:8 — no_image', lambda: the_second_word({'ask': 'no_image'}, DATA), 'no image (5:8) — the making barred; the no-image list of 4:16-19 the parameter table (OH by CALL); the images for study credited'),
    ('Deut 5:9; Mishnah Sanhedrin 7:6 — bow_and_serve', lambda: the_second_word({'ask': 'bow_and_serve'}, DATA), "bow and serve (5:9) — the bower stoned: the second word's answer sheet (Mishnah Sanhedrin 7:6; the four services, Sanhedrin 60b); the mode by 17:5's juxtaposition"),
    ('shelf: Sanhedrin 60b:3 — in_its_way', lambda: the_second_word({'ask': 'in_its_way'}, DATA), "in its way (5:9) — Peor's exposure, Markulis's stone: liable, the idol's own service (Mishnah Sanhedrin 7:6)"),
    ('shelf: Sanhedrin 60b:2 — the_embracer', lambda: the_second_word({'ask': 'the_embracer'}, DATA), 'the embracer (5:9) — a prohibition without death: the hugger, the kisser, the dresser exempt from the sanction (Mishnah Sanhedrin 7:6)'),
    ('Deut 5:9-10 — the_visiting', lambda: the_second_word({'ask': 'the_visiting'}, DATA), "the visiting (5:9-10) — the generations and the thousands a DATA row: when they hold their fathers' deeds (Berakhot 7a); revoked by Ezekiel (Makkot 24a)"),
    ('Deut 5:10 — the_ketiv', lambda: the_second_word({'ask': 'the_ketiv'}, DATA), "the ketiv (5:10) — 'his' written, 'my' read: a DATA note, no line"),
    ('the write — the_write', lambda: the_second_word({'ask': 'the_write'}, DATA), "the write (5:7-10) — other_gods_barred on Israel: the code's hole filled at the code's own line"),
    # F3 — the_first_tablet
    ('Deut 5:6 — the_first_word', lambda: the_first_tablet({'ask': 'the_first_word'}, DATA), "the first word (5:6) — VERBATIM; NO CELL: a declaration heard from the Almighty's mouth"),
    ('Deut 5:7-10 — the_second_word_row', lambda: the_first_tablet({'ask': 'the_second_word_row'}, DATA), 'the second word (5:7-10) — VERBATIM, VARIANT, VARIANT, VARIANT: the cell F2 (compiled here)'),
    ('Deut 5:11 — the_third_word', lambda: the_first_tablet({'ask': 'the_third_word'}, DATA), 'the third word (5:11) — VERBATIM: decalogue.vain_name by CALL (the vain oath lashed; Mishnah Shevuot 3:8-9)'),
    ('Deut 5:12-15 — the_fourth_word', lambda: the_first_tablet({'ask': 'the_fourth_word'}, DATA), 'the fourth word (5:12-15) — EXPANDED, VERBATIM, EXPANDED, TURNED: decalogue.sabbath_clauses by CALL'),
    ('Deut 5:12; Shevuot 20b — keep_and_remember', lambda: the_first_tablet({'ask': 'keep_and_remember'}, DATA), "keep and remember (5:12) — one utterance: the diff's first word the tradition's exhibit; women's kiddush (Berakhot 20b)"),
    ('Deut 5:14; Bava Kamma 54b — the_ox_and_the_ass', lambda: the_first_tablet({'ask': 'the_ox_and_the_ass'}, DATA), 'the ox and the ass (5:14) — every animal by the verbal analogy: the expansion read by the tradition itself (Bava Kamma 54b)'),
    ('Deut 5:14; Yevamot 48b — the_servants_rest', lambda: the_first_tablet({'ask': 'the_servants_rest'}, DATA), "the servants' rest (5:14) — the circumcised slave and the righteous convert (Yevamot 48b); the analogy's limit (Bava Kamma 54b)"),
    ('Deut 5:15 — the_two_grounds', lambda: the_first_tablet({'ask': 'the_two_grounds'}, DATA), 'the two grounds (5:15) — the creation (20:11, PS by CALL) and the exodus: a DATA row; the readback row TURNED'),
    ('Deut 5:12; Sanhedrin 56b — the_receipt_5_12', lambda: the_first_tablet({'ask': 'the_receipt_5_12'}, DATA), 'the receipt at 5:12 — a run citation of the giving (the ink) read as Marah (the teacher): the seat CHAPTER'),
    # F4 — the_second_tablet
    ('Deut 5:16 — the_fifth_word', lambda: the_second_tablet({'ask': 'the_fifth_word'}, DATA), "the fifth word (5:16) — EXPANDED: NO CELL at the Decalogue's seat, holiness.frame by CALL (the honor and the fear defined, Kiddushin 31b)"),
    ('Deut 5:17 — the_sixth_word', lambda: the_second_tablet({'ask': 'the_sixth_word'}, DATA), 'the sixth word (5:17) — VERBATIM: mishpatim_3.killer and refuge.the_murderer by CALL'),
    ('Deut 5:18 — the_seventh_word', lambda: the_second_tablet({'ask': 'the_seventh_word'}, DATA), 'the seventh word (5:18) — VARIANT: sanctions.adultery by CALL (Leviticus 20:10)'),
    ('Deut 5:19; Sanhedrin 86a — the_eighth_word', lambda: the_second_tablet({'ask': 'the_eighth_word'}, DATA), 'the eighth word (5:19) — VARIANT: the theft of persons by the context (Sanhedrin 86a); decalogue.theft_commandment by CALL'),
    ('Deut 5:20 — the_ninth_word', lambda: the_second_tablet({'ask': 'the_ninth_word'}, DATA), 'the ninth word (5:20) — TURNED: vain for false, the parameter a DATA row; ordinances.courts by CALL (23:1)'),
    ('Deut 5:21 — the_tenth_word_row', lambda: the_second_tablet({'ask': 'the_tenth_word_row'}, DATA), 'the tenth word (5:21) — TURNED: the cell F5 (compiled here)'),
    ('Deut 5:16; Bava Kamma 55a — the_reward_clause', lambda: the_second_tablet({'ask': 'the_reward_clause'}, DATA), "the reward clause (5:16) — the expansion's own Talmud row: 'good' not in the first tablets (Bava Kamma 55a)"),
    ('Deut 5:16; Sanhedrin 56b — the_receipt_5_16', lambda: the_second_tablet({'ask': 'the_receipt_5_16'}, DATA), 'the receipt at 5:16 — a run citation of the giving read as Marah: the seat CHAPTER'),
    ('Deut 5:6-21 — the_counts', lambda: the_second_tablet({'ask': 'the_counts'}, DATA), 'the counts (5:6-21) — 189 tokens / 708 letters against 172 / 620: recomputed'),
    # F5 — the_tenth_word
    ('Deut 5:21 — covet_and_desire', lambda: the_tenth_word({'ask': 'covet_and_desire'}, DATA), "covet and desire (5:21) — the two verbs: the tenth word compiled here; the block coveting_barred on Israel at the giving's line"),
    ('Deut 5:21 — the_wife_first', lambda: the_tenth_word({'ask': 'the_wife_first'}, DATA), 'the wife first (5:21) — the order turned, his field added: a DATA row'),
    ('shelf: Bava Metzia 5b:19-20 — the_coveter_who_pays', lambda: the_tenth_word({'ask': 'the_coveter_who_pays'}, DATA), "the coveter who pays (5:21) — the prohibition stands (Rav Acha), the people's reading spares his oath: not a robber (Bava Metzia 5b)"),
    ('the write — the_write', lambda: the_tenth_word({'ask': 'the_write'}, DATA), "the write (5:21) — coveting_barred on Israel: the code's hole filled at the code's own line"),
    # F6 — the_voice_and_the_request
    ('Deut 5:22 — added_no_more', lambda: the_voice_and_the_request({'ask': 'added_no_more'}, DATA), "added no more (5:22) — 2b's ten words and tablets FOUND (OH by CALL); 'did not cease' the Talmud's and Onkelos's reading"),
    ('Deut 5:22 — the_tablets_given_to_me', lambda: the_voice_and_the_request({'ask': 'the_tablets_given_to_me'}, DATA), 'the tablets given to me (5:22) — tablets_given FOUND at (1, 4, 17); no second write'),
    ('Deut 5:23 — you_came_near', lambda: the_voice_and_the_request({'ask': 'you_came_near'}, DATA), "you came near (5:23) — 1:22's phrase at its second seat: the mob and the elders (OS by CALL; the Sifrei 20:1)"),
    ('Deut 5:24-27 — the_request', lambda: the_voice_and_the_request({'ask': 'the_request'}, DATA), "the request (5:24-27) — SUPPLIED: the tape's second hole written once at its own time; the mediator asked for (Makkot 24a)"),
    ('Deut 5:27; Shabbat 88a — hear_and_do', lambda: the_voice_and_the_request({'ask': 'hear_and_do'}, DATA), "hear and do (5:27) — TURNED against 24:7's 'do and hear' (Shabbat 88a); Onkelos 'accept and do'"),
    ('the write — the_write', lambda: the_voice_and_the_request({'ask': 'the_write'}, DATA), "the write (5:23-27) — torah_through_moses on Israel: the mediator's status"),
    # F7 — the_answer_and_the_charge
    ('Deut 5:28 — the_lord_heard', lambda: the_answer_and_the_charge({'ask': 'the_lord_heard'}, DATA), "the LORD heard (5:28) — 1:34's phrase at its second seat (OS by CALL)"),
    ('Deut 5:28 — done_well', lambda: the_answer_and_the_charge({'ask': 'done_well'}, DATA), 'they have done well (5:28) — cited forward at 18:17: a DATA note'),
    ('Deut 5:29; Avodah Zarah 4b-5a — who_would_give', lambda: the_answer_and_the_charge({'ask': 'who_would_give'}, DATA), "who would give (5:29) — the calf and the penitents (Avodah Zarah 4b-5a): an aggadah on the answer's verse"),
    ('Deut 5:30; Beitzah 5a-b — return_to_your_tents', lambda: the_answer_and_the_charge({'ask': 'return_to_your_tents'}, DATA), 'return to your tents (5:30) — the separation released: returned_to_tents on Israel (Beitzah 5a-b)'),
    ('Deut 5:31 — stand_here_with_me', lambda: the_answer_and_the_charge({'ask': 'stand_here_with_me'}, DATA), 'stand here with me (5:31) — SUPPLIED: the charge to teach a debit on Moses closed by the prior run (Deut 1:5); the Torah received standing'),
    ('Deut 5:32-33 — the_charge', lambda: the_answer_and_the_charge({'ask': 'the_charge'}, DATA), "the charge (5:32-33) — no write: the frame's close; the plural receipt's seat CHAPTER"),
    ('Deut 5:1-33 — the_readback_table', lambda: the_answer_and_the_charge({'ask': 'the_readback_table'}, DATA), 'the readback table — twenty-one rows graded (sixteen on the code, five on the narrative); no row open'),
    ('Deut 5:12, 16, 32 — the_register_seats', lambda: the_answer_and_the_charge({'ask': 'the_register_seats'}, DATA), "the register seats — Deut 5:12, 5:16, 5:32 CHAPTER (the gate's code); 4:45 DAEMONS 2"),
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
    print('THE INK: numbers %s; the one frame %s; the case tokens %s; the register singular-only %s, plural-only %s, both %s; the ketiv at 5:10' % (sorted(PARSED.items()), DIV, dict(collections.Counter(x for l in CASE_TOK.values() for x in l)), SG_ONLY, PL_ONLY, BOTH))
    print('THE LAWS\' READBACK: %d rows — %s; the law rows %d (the cells named %d, NO CELL %s); the deltas: the frame %s; the voice %s; the request %s; hear and do %s; the answer %s' % (len(READBACK), dict(RB_GRADES), sum(1 for r in READBACK if r['law']), sum(1 for r in READBACK if r['law'] and r['cell'] != 'NO CELL'), [r['verses'] for r in READBACK if r['cell'] == 'NO CELL'], FRAME_DIFF, VOICE_DELTA, REQUEST_DELTA, HEAR_DO_DELTA, ANSWER_DELTA))
    print('THE TWO COPIES: %s (tokens, letters) — Exodus 20:2-17 against Deuteronomy 5:6-21; per word %s' % (COPIES, WORD_TOK))
    print('THE HOLES: the tape\'s first (2b) %s; the second — Exodus 20:18-21 no line (this sitting); the code\'s — the second and the tenth words compiled here' % (OH_HOLE,))
    print('THE CALLEES: the honor %s; the fear %s; the days %s; we will do %s; Marah %s' % (HO_HONOR['v'], HO_FEAR['v'], ES_DAYS['v'], ES_SEATS['v'], ES_MARAH['v']))
    print('THE SCENE on the bench: %s; the exempt and stoned arms %s; the timers (set, fired, cancelled, pending) %s; entities %d; closes %d' % (SCENE[0], SCENE[1], SCENE[2], SCENE[3], SCENE[4]))
    print('THE NARRATIVE: %s' % (NARRATIVE,))
    print('THE PARAMETER ROWS: ' + '; '.join('%s = %s' % (k, DATA[k]['value'] if k != 'the_readback' else '%d rows' % len(DATA[k]['value'])) for k in DATA) + ' (the other settings recorded in DATA)')
    if ok == len(CASES):
        print('\nTHE COMPILE OF CHAPTER 5: the answer sheet REPRODUCED — %d/%d' % (ok, len(CASES)))
    sys.exit(0 if ok == len(CASES) else 1)

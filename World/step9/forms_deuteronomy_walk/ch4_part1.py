#!/usr/bin/env python3
# DEUTERONOMY 4:1-49 — THE OBEDIENCE AT HOREB, THE ONE LAW AND THE ONE CASE, THE THREE CITIES (THE DEUTERONOMY WALK sitting 2b, 2026-09-16;
# World/step9/DEUTERONOMY_WALK.md "Sitting 2b"; the state doc's #186). THE READBACK'S FIRST FORM ON ITS SECOND CHAPTER (THE_LOOP.md step 6): the
# DATA table the_readback carries ELEVEN reference rows graded against the tape (SHORTENED / EXPANDED / SUPPLIED / DISAGREES), the deltas
# RECOMPUTED from the DB; THE TAPE'S HOLE FOUND — no line for the speaking of the ten words (Exodus 20:1) nor the giving of the first tablets
# (31:18): the two SUPPLIED lines written ONCE at their own time by RETROGRADE markers at Deut 4:10 (the giving, (1, 3, 7)) and 4:13 (the tablets,
# (1, 4, 17)); the bar's THIRD telling (4:21-22) a DISAGREES row beside 1:37's, OPEN. THE ONE LAW: 4:2's "you shall not add … nor diminish" — a
# BLOCK adding_barred on Israel, the exam's rows on bal tosif's time and intent and the addition that spoils; the receipt 4:5 the register seat
# ACT (the teaching's run). THE ONE CASE: 4:25-31's "when you beget sons" — heaven_and_earth_witness on Israel, the arms DATA, no timer. THE
# THREE CITIES: 4:41-43 Moses' act — cities_set_apart on Israel, THE REFUGE DEBIT LEFT OPEN on Mishnah Makkot 2:4's own row. THE SECOND FRAME
# (4:44-49) NO WRITE (R6). The daemon law_obey_horeb given_at Deut 4:2, installed_by BOOT with the class NAMED (a law in Moses' voice with no
# divine frame). Six cells; every token probed (zero-report law); effects on every cell (the effects law); the parameters the ink leaves open
# recorded in DATA with their arms; nineteen DATA rows. Reading ledger: logic/oral_triage/deu_04_vaetchanan_2026-09-16.md (55 sources, 7 claims);
# the exam's docket: logic/oral_triage/deu_04_vaetchanan_exam_2026-09-16.md (327 rows: LAW 76 / DERIVATION 70 / DISPUTE 12 / CONTEXT 169).

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
from fractions import Fraction
import effects_layer as FX
import world_engine as WE
import cold_run_balak as BK                   # THE EDGE: obey_horeb -> balak CALL, reference (4:3 Baal-peor READ BACK — the plague's count, the service; 4:46's valley the last camp)
import cold_run_refuge as RF                  # THE EDGE: obey_horeb -> refuge CALL, reference (4:41-43 the three cities — the six's row, the debit READ OPEN; 4:42 the manslayer's clauses)
import cold_run_opening_speech as OS          # THE EDGE: obey_horeb -> opening_speech CALL, reference (4:21-22 the bar's third telling; 4:44-49 the speech's own frame and borders; the readback's first form)
import cold_run_erection as ER                # THE EDGE: obey_horeb -> erection CALL, reference (4:13 the ten words and the tablets; the fortieth day; 4:5 and 4:14 the teaching commanded; Horeb plene)
import cold_run_exodus_story as ES            # THE EDGE: obey_horeb -> exodus_story CALL, reference (4:10 the assembly's day; 4:34 the instruments; 4:20 and 4:37 brought out)
import cold_run_tochacha as TC                # THE EDGE: obey_horeb -> tochacha CALL, reference (4:27 scattered, 4:31 the covenant not forgotten — Leviticus 26's arms)
import cold_run_pre_sinai as PS               # THE EDGE: obey_horeb -> pre_sinai CALL, reference (4:32 'created' — Genesis 1:27)
import cold_run_primeval as PR                # THE EDGE: obey_horeb -> primeval CALL, reference (4:20 the furnace-word's first seat; 4:37-38 the fathers' land)
import cold_run_decalogue as DC               # THE EDGE: obey_horeb -> decalogue CALL, reference (4:36 Exodus 20:22's 'from heaven'; the second word OWED — no cell)
import cold_run_chukat as CK                  # THE EDGE: obey_horeb -> chukat CALL, reference (4:46-47 the two kings READ BACK a second time)
import cold_run_borders as BO                 # THE EDGE: obey_horeb -> borders CALL, reference (4:48-49 the east's extents)

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
_rows = db.execute("SELECT v.book, v.chapter, v.verse, w.he, w.morph, w.lemma FROM words w JOIN verses v ON w.verse_id=v.id ORDER BY v.id, w.idx").fetchall()
by, byp, byl = {}, {}, {}
for _b, _c, _v, _he, _m, _lem in _rows:
    by.setdefault((_b, _c, _v), []).append((plain(_he), _m)); byp.setdefault((_b, _c, _v), []).append(pointed(_he)); byl.setdefault((_b, _c, _v), []).append((_lem or '').split('/')[-1].strip())
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
def W4(v): return words('Deut', 4, v)
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

# ---- THE INK, computed (the parser and the tokens; the reading's facts the expectations — every assert PROVEN at the reading, ch4_ink.py) ----
SPAN = [(4, v) for v in range(1, 50)]
PARSED = {(c, v): ink_numbers(verse_words('Deut', c, v)) for (c, v) in SPAN if ink_numbers(verse_words('Deut', c, v))}
assert PARSED == {(4, 13): [10, 2], (4, 41): [3], (4, 42): [1], (4, 47): [2]}, PARSED   # FOUR number verses in forty-nine, no ordinal
assert {(c, v): ink_ordinals(verse_words('Deut', c, v)) for (c, v) in SPAN if ink_ordinals(verse_words('Deut', c, v))} == {} and [((c, v), t) for (c, v) in SPAN for t in verse_words('Deut', c, v) if t[-1] in '#~^%@|*'] == [((4, 13), 'שני^'), ((4, 47), 'שני^')]
assert ink_numbers(verse_words('Deut', 10, 4)) == [10] and ink_numbers(verse_words('Exod', 34, 28)) == [40, 40, 10] and ink_numbers(verse_words('Num', 35, 14)) == [3, 3]
TEN_TWO, THREE_CITIES_N, ONE_CITY, TWO_KINGS = PARSED[(4, 13)], PARSED[(4, 41)][0], PARSED[(4, 42)][0], PARSED[(4, 47)][0]
TOK = sum(len(by[('Deut', 4, v)]) for v in range(1, 50)); assert TOK == 813, TOK
# THE FRAMES AND THE REGISTER
DIV = [(c, v) for (c, v) in SPAN if any(W4(v)[i] in ('ויאמר', 'וידבר') and W4(v)[i + 1] == 'יהוה' for i in range(len(W4(v)) - 1))]
assert DIV == [(4, 12)] and P('וידבר', 'יהוה', 'אליכם') == ['Deut 4:12'] and P('דבר', 'יהוה', 'אליכם') == S_('Deut 10:4', 'Deut 4:15') and [(c, v) for (c, v) in SPAN if 'לאמר' in W4(v)] == []
REG = {v: [x for x, m in by[('Deut', 4, v)] if m and re.search(r'V.w', m)] for v in range(1, 50) if any(m and re.search(r'V.w', m) for x, m in by[('Deut', 4, v)])}
assert REG == {11: ['ותקרבון', 'ותעמדון'], 12: ['וידבר'], 13: ['ויגד', 'ויכתבם'], 20: ['ויוצא'], 21: ['וישבע'], 33: ['ויחי'], 37: ['ויבחר', 'ויוצאך'], 47: ['ויירשו']}, REG
CASE_TOK = {f'{c}:{v}': [x for x in W4(v) if x in ('כי', 'אם', 'ואם', 'או', 'פן')] for (c, v) in SPAN if any(x in ('כי', 'אם', 'ואם', 'או', 'פן') for x in W4(v))}
assert collections.Counter(x for l in CASE_TOK.values() for x in l) == collections.Counter({'כי': 15, 'פן': 3, 'או': 3}) and 'אם' not in collections.Counter(x for l in CASE_TOK.values() for x in l) and 'ופן' in W4(19) and 'ופן' in W4(9)
assert CASE_TOK['4:25'] == ['כי'] and W4(25)[0] == 'כי' and morphs('Deut', 4, 25)[1] == 'HVhi2ms'   # THE ONE CASE opens with "when" and the imperfect
NUM2 = {v: (sum(1 for _, m in by[('Deut', 4, v)] if m and '2mp' in m), sum(1 for _, m in by[('Deut', 4, v)] if m and '2ms' in m)) for v in range(1, 50)}
SG_ONLY = [v for v, (p, s) in NUM2.items() if s and not p]; PL_ONLY = [v for v, (p, s) in NUM2.items() if p and not s]; BOTH = [v for v, (p, s) in NUM2.items() if p and s]; NEITHER = [v for v, (p, s) in NUM2.items() if not p and not s]
assert SG_ONLY == [10, 19, 24, 30, 31, 32, 33, 35, 36, 37, 38, 39, 40] and PL_ONLY == [2, 4, 6, 8, 11, 12, 13, 14, 15, 16, 20, 22, 26, 27, 28] and BOTH == [1, 3, 5, 9, 21, 23, 25, 29, 34] and NEITHER == [7, 17, 18] + list(range(41, 50)), (SG_ONLY, PL_ONLY, BOTH, NEITHER)
IMPER = {v: [(x, m) for x, m in by[('Deut', 4, v)] if m and re.match(r'^HV.v', m)] for v in range(1, 50) if any(m and re.match(r'^HV.v', m) for _, m in by[('Deut', 4, v)])}
assert IMPER == {1: [('שמע', 'HVqv2ms')], 5: [('ראה', 'HVqv2ms')], 9: [('השמר', 'HVNv2ms')], 10: [('הקהל', 'HVhv2ms')], 23: [('השמרו', 'HVNv2mp')], 32: [('שאל', 'HVqv2ms')]}, IMPER
PROHIB = {v: [x for i, (x, m) in enumerate(by[('Deut', 4, v)]) if i and by[('Deut', 4, v)][i - 1][0] in ('לא', 'פן', 'ופן', 'ולא') and m and m.startswith('HV') and 'i2' in m] for v in range(1, 50)}
PROHIB = {v: l for v, l in PROHIB.items() if l}
assert PROHIB == {2: ['תספו', 'תגרעו'], 9: ['תשכח'], 16: ['תשחתון'], 19: ['תשא'], 23: ['תשכחו'], 26: ['תאריכן']}, PROHIB
YG_SG = [v for v in range(1, 50) for i in range(len(W4(v)) - 1) if W4(v)[i:i + 2] == ['יהוה', 'אלהיך']]; YG_PL = [v for v in range(1, 50) for i in range(len(W4(v)) - 1) if W4(v)[i:i + 2] == ['יהוה', 'אלהיכם']]
assert YG_SG == [3, 10, 19, 21, 23, 24, 25, 29, 30, 31, 40] and YG_PL == [2, 23, 34]
NAME = collections.Counter(x for v in range(1, 50) for x in W4(v) if x in ('יהוה', 'ויהוה', 'ביהוה', 'כיהוה', 'ליהוה'))
assert sum(NAME.values()) == 29 and [v for v in range(1, 50) if 'משה' in W4(v)] == [41, 44, 45, 46]
# F1's facts: the exhortation and the one law
assert P('ועתה', 'ישראל') == S_('Deut 10:12', 'Deut 4:1') and P('שמע', 'ישראל') == S_('Deut 20:3', 'Deut 5:1', 'Deut 6:4', 'Deut 9:1') and wm('Deut', 4, 1)[2] == ('שמע', 'HVqv2ms') and wm('Deut', 4, 1)[10] == ('אתכם', 'HTo/Sp2mp')
assert P('חקים', 'ומשפטים') == S_('Deut 4:14', 'Deut 4:5', 'Deut 4:8', 'Mal 3:22') and P('ואל', 'המשפטים') == ['Deut 4:1'] and LEMV('3925', T) and len(LEMV('3925', T)) == 16 and min(LEMV('3925', T), key=lambda s: (int(s.split()[1].split(':')[0]), int(s.split(':')[1]))) == 'Deut 4:1'
ADD_PL = P('לא', 'תספו', 'על', 'הדבר'); DIMINISH = sorted(set(P('ולא', 'תגרעו')) | set(P('ולא', 'תגרע')))
assert ADD_PL == ['Deut 4:2'] and P('לא', 'תספו') == ['Deut 4:2'] and DIMINISH == S_('Deut 13:1', 'Deut 4:2') and W4(2)[:2] == ['לא', 'תספו'] and words('Deut', 13, 1)[10:16] == ['לא', 'תסף', 'עליו', 'ולא', 'תגרע', 'ממנו']
DIMINISH_LEM = LEMV('1639', T)
assert 'Deut 4:2' in DIMINISH_LEM and 'Exod 5:8' in DIMINISH_LEM and 'Num 27:4' in DIMINISH_LEM and 'Num 36:3' in DIMINISH_LEM, DIMINISH_LEM
assert P('למען', 'תחיו', books=T) == ['Deut 4:1'] and P('ובאתם', 'וירשתם', 'את', 'הארץ') == S_('Deut 11:8', 'Deut 4:1', 'Deut 8:1')
PEOR = P('בעל', 'פעור'); PEOR_ALL = U('פעור')
assert PEOR == S_('Deut 4:3', 'Hos 9:10') and P('בבעל', 'פעור') == ['Deut 4:3'] and len(PEOR_ALL) == 12 and P('בית', 'פעור') == S_('Deut 34:6', 'Deut 3:29', 'Deut 4:46') and P('עיניכם', 'הראת') == S_('Deut 11:7', 'Deut 4:3')
assert P('השמידו', 'יהוה', 'אלהיך', 'מקרבך') == ['Deut 4:3'] and PT('Deut', 4, 3, 'הראת') == ['הָֽרֹאֹת'] and PT('Deut', 4, 35, 'הראת') == ['הָרְאֵתָ'] and morphs('Deut', 4, 3)[1] == 'HTd/Vqrfpa' and morphs('Deut', 4, 35)[1] == 'HVHp2ms'
CLEAVE = LEMV('1695')
assert CLEAVE == S_('2Chr 3:12', 'Deut 4:4', 'Prov 18:24') and P('ואתם', 'הדבקים', 'ביהוה') == ['Deut 4:4'] and P('חיים', 'כלכם', 'היום') == ['Deut 4:4']
RECEIPT_ME = P('כאשר', 'צוני', 'יהוה'); RECEIPT_MY_GOD = P('כאשר', 'צוני', 'יהוה', 'אלהי')
assert RECEIPT_MY_GOD == ['Deut 4:5'] and RECEIPT_ME == S_('Deut 10:5', 'Deut 4:5') and U('צוני') == S_('1Sam 21:3', '2Sam 14:19', 'Deut 10:5', 'Deut 4:5', 'Ezek 37:10') and P('ראה', 'למדתי', 'אתכם') == ['Deut 4:5']
assert P('חכמתכם', 'ובינתכם') == ['Deut 4:6'] and P('חכם', 'ונבון') == S_('1Kgs 3:12', 'Deut 4:6') and P('הגוי', 'הגדול', 'הזה') == ['Deut 4:6'] and P('לעיני', 'העמים') == ['Deut 4:6']
assert P('גוי', 'גדול') == S_('Deut 4:7', 'Deut 4:8') and P('אלהים', 'קרבים') == ['Deut 4:7'] and morphs('Deut', 4, 7)[6] == 'HNcmpa' and P('חקים', 'ומשפטים', 'צדיקם') == ['Deut 4:8'] and P('ככל', 'התורה', 'הזאת') == ['Deut 4:8']
# F2's facts: Horeb retold
assert P('רק', 'השמר', 'לך') == ['Deut 4:9'] and len(P('השמר', 'לך')) == 12 and P('ושמר', 'נפשך', 'מאד') == ['Deut 4:9'] and P('לבניך', 'ולבני', 'בניך') == ['Deut 4:9'] and U('והודעתם') == S_('Deut 4:9', 'Josh 4:22')
FORGET = LEMV('7911', ('Deut',))
assert FORGET == S_('Deut 24:19', 'Deut 25:19', 'Deut 26:13', 'Deut 31:21', 'Deut 32:18', 'Deut 4:23', 'Deut 4:31', 'Deut 4:9', 'Deut 6:12', 'Deut 8:11', 'Deut 8:14', 'Deut 8:19', 'Deut 9:7')
HOREB = LEMV('2722'); HOREB_T = LEMV('2722', T)
assert P('יום', 'אשר', 'עמדת') == ['Deut 4:10'] and P('לפני', 'יהוה', 'אלהיך', 'בחרב') == ['Deut 4:10'] and len(HOREB) == 17 and len(HOREB_T) == 12 and 'Exod 33:6' in HOREB
assert P('הקהל', 'לי', 'את', 'העם') == ['Deut 4:10'] and 'Deut 31:12' in U('הקהל') and P('ליראה', 'אתי', 'כל', 'הימים') == ['Deut 4:10'] and P('ואת', 'בניהם', 'ילמדון') == ['Deut 4:10']
LEARN_TEACH = [(x, m) for x, m in by[('Deut', 4, 10)] if x == 'ילמדון']
assert LEARN_TEACH == [('ילמדון', 'HVqi3mp/Sn'), ('ילמדון', 'HVpi3mp/Sn')] and PT('Deut', 4, 10, 'ילמדון') == ['יִלְמְדוּן', 'יְלַמֵּדֽוּן']   # ONE written form, qal and piel by the pointing alone
assert P('ותקרבון', 'ותעמדון') == ['Deut 4:11'] and P('תחת', 'ההר') == S_('Deut 4:11', 'Exod 24:4', 'Exod 32:19') and P('בער', 'באש') == S_('Deut 4:11', 'Deut 5:23', 'Deut 9:15', 'Exod 3:2') and P('עד', 'לב', 'השמים') == ['Deut 4:11']
assert P('חשך', 'ענן', 'וערפל') == ['Deut 4:11'] and P('האש', 'הענן', 'והערפל') == ['Deut 5:22']
FROM_FIRE = P('מתוך', 'האש')
assert FROM_FIRE == S_('Deut 10:4', 'Deut 4:12', 'Deut 4:15', 'Deut 4:33', 'Deut 4:36', 'Deut 5:22', 'Deut 5:24', 'Deut 5:26', 'Deut 5:4', 'Deut 9:10', 'Ezek 1:4') and P('קול', 'דברים') == ['Deut 4:12'] and P('זולתי', 'קול') == ['Deut 4:12']
FORM_LEM = LEMV('8544')
assert FORM_LEM == S_('Deut 4:12', 'Deut 4:15', 'Deut 4:16', 'Deut 4:23', 'Deut 4:25', 'Deut 5:8', 'Exod 20:4', 'Job 4:16', 'Num 12:8', 'Ps 17:15') and P('לא', 'ראיתם', 'כל', 'תמונה') == ['Deut 4:15']
TEN_WORDS = P('עשרת', 'הדברים'); TABLETS_PLENE = U('לחות'); TABLETS_DEF = U('לחת')
assert U('בריתו', books=T) == S_('Deut 17:2', 'Deut 4:13', 'Deut 8:18', 'Exod 2:24') and P('בריתו', 'אשר', 'צוה', 'אתכם') == ['Deut 4:13'] and TEN_WORDS == S_('Deut 10:4', 'Deut 4:13', 'Exod 34:28') and P('שני', 'לחות', 'אבנים') == ['Deut 4:13'] and P('ויכתבם', 'על') == S_('Deut 4:13', 'Deut 5:22')
assert TABLETS_PLENE == S_('1Kgs 8:9', 'Deut 4:13', 'Deut 9:11') and PT('Deut', 4, 13, 'לחות') == ['לֻחוֹת'] and TABLETS_DEF == S_('Deut 10:3', 'Deut 5:22', 'Deut 9:11', 'Deut 9:15', 'Exod 24:12', 'Exod 27:8', 'Exod 31:18', 'Exod 32:15', 'Exod 34:1', 'Exod 34:29', 'Exod 34:4', 'Exod 38:7')
assert words('Exod', 20, 1)[:4] == ['וידבר', 'אלהים', 'את', 'כל'] and words('Exod', 31, 18)[:5] == ['ויתן', 'אל', 'משה', 'ככלתו', 'לדבר'] and words('Exod', 32, 15)[:4] == ['ויפן', 'וירד', 'משה', 'מן']   # the two first tellings and the descent with the tablets
assert P('ואתי', 'צוה', 'יהוה', 'בעת', 'ההוא') == ['Deut 4:14'] and P('ללמד', 'אתכם') == S_('Deut 4:14', 'Deut 6:1') and words('Exod', 24, 12)[-1] == 'להורתם'
# F3's facts: no image, the host, the furnace, the bar
assert P('ונשמרתם', 'מאד', 'לנפשתיכם') == S_('Deut 4:15', 'Josh 23:11') and P('פן', 'תשחתון') == ['Deut 4:16']
IMAGE = U('פסל', 'ופסל')
assert len(IMAGE) == 23 and P('פסל', 'תמונת', 'כל') == S_('Deut 4:16', 'Deut 4:23', 'Deut 4:25') and words('Exod', 20, 4)[:5] == ['לא', 'תעשה', 'לך', 'פסל', 'וכל'] and words('Deut', 5, 8)[:5] == ['לא', 'תעשה', 'לך', 'פסל', 'כל']
LIKENESS_N = sum(W4(v).count('תבנית') for v in range(1, 50))
assert U('סמל') == S_('Deut 4:16', 'Ezek 8:3', 'Ezek 8:5') and LIKENESS_N == 5 and P('זכר', 'או', 'נקבה') == S_('Deut 4:16', 'Lev 3:6') and P('צפור', 'כנף') == ['Deut 4:17'] and P('רמש', 'באדמה') == ['Deut 4:18'] and U('דגה') == ['Deut 4:18'] and P('במים', 'מתחת', 'לארץ') == S_('Deut 4:18', 'Deut 5:8', 'Exod 20:4')
HOST = P('כל', 'צבא', 'השמים'); APPORTIONED = [(s, x) for s, x, m in LEMT('2505 a') if m and m.startswith('HVqp3ms')]
assert P('תשא', 'עיניך', 'השמימה') == ['Deut 4:19'] and P('השמש', 'ואת', 'הירח', 'ואת', 'הכוכבים') == ['Deut 4:19'] and HOST == S_('Deut 4:19', 'Isa 34:4') and U('ונדחת') == S_('Deut 30:17', 'Deut 4:19')
assert APPORTIONED == [('2Chr 23:18', 'חלק'), ('2Chr 28:21', 'חלק'), ('Deut 4:19', 'חלק'), ('Deut 29:25', 'חלק'), ('Job 39:17', 'חלק')] and P('אשר', 'חלק', 'יהוה', 'אלהיך') == ['Deut 4:19'] and P('לכל', 'העמים', 'תחת', 'כל', 'השמים') == ['Deut 4:19']
FURNACE = U('מכור', 'כור')
assert FURNACE == S_('1Kgs 8:51', 'Deut 4:20', 'Ezek 22:18', 'Ezek 22:20', 'Ezek 22:22', 'Jer 11:4') and P('לעם', 'נחלה') == ['Deut 4:20'] and P('ואתכם', 'לקח', 'יהוה') == ['Deut 4:20'] and 'תנור' in words('Gen', 15, 17)
ANGRY = LEMV('599', T)
assert P('התאנף', 'בי') == ['Deut 4:21'] and ANGRY == S_('Deut 1:37', 'Deut 4:21', 'Deut 9:20', 'Deut 9:8') and U('בגללכם') == S_('Deut 1:37', 'Mic 3:12') and P('על', 'דבריכם') == ['Deut 4:21'] and P('וישבע', 'לבלתי', 'עברי') == ['Deut 4:21'] and 'למענכם' in words('Deut', 3, 26)
assert 'האמנתם' in words('Num', 20, 12) and P('כי', 'אנכי', 'מת') == ['Deut 4:22'] and P('אינני', 'עבר', 'את', 'הירדן') == ['Deut 4:22']
assert P('פן', 'תשכחו', 'את', 'ברית') == ['Deut 4:23'] and P('אש', 'אכלה') == S_('Deut 4:24', 'Deut 9:3', 'Joel 1:19', 'Joel 2:5') and P('אל', 'קנא') == S_('Deut 4:24', 'Deut 5:9', 'Deut 6:15', 'Exod 20:5', 'Exod 34:14') and len(W4(24)) == 8
# F4's facts: the exile case
assert P('כי', 'תוליד', 'בנים') == ['Deut 4:25'] and U('ונושנתם') == ['Deut 4:25'] and P('הרע', 'בעיני', 'יהוה', books=T) == S_('Deut 17:2', 'Deut 31:29', 'Deut 4:25', 'Deut 9:18', 'Num 32:13')
WITNESS_CALL = U('העידתי'); HEAVEN_EARTH_D = P('את', 'השמים', 'ואת', 'הארץ', books=('Deut',))
assert WITNESS_CALL == S_('Deut 30:19', 'Deut 4:26', 'Jer 42:19') and HEAVEN_EARTH_D == S_('Deut 30:19', 'Deut 31:28', 'Deut 4:26') and words('Deut', 30, 19)[:7] == W4(26)[:7]
assert P('אבד', 'תאבדון', 'מהר') == ['Deut 4:26'] and P('לא', 'תאריכן', 'ימים') == S_('Deut 30:18', 'Deut 4:26') and P('השמד', 'תשמדון') == ['Deut 4:26']
assert P('והפיץ', 'יהוה', 'אתכם', 'בעמים') == ['Deut 4:27'] and P('מתי', 'מספר') == S_('1Chr 16:19', 'Deut 4:27', 'Gen 34:30', 'Jer 44:28', 'Ps 105:12') and 'אזרה' in words('Lev', 26, 33)
assert P('מעשה', 'ידי', 'אדם', 'עץ', 'ואבן') == S_('2Kgs 19:18', 'Deut 4:28', 'Isa 37:19') and P('עץ', 'ואבן') == S_('2Kgs 19:18', 'Deut 28:36', 'Deut 28:64', 'Deut 29:16', 'Deut 4:28', 'Ezek 20:32', 'Isa 37:19')
HEART_SOUL = P('בכל', 'לבבך', 'ובכל', 'נפשך')
assert P('ובקשתם', 'משם') == ['Deut 4:29'] and HEART_SOUL == S_('Deut 10:12', 'Deut 26:16', 'Deut 30:10', 'Deut 30:2', 'Deut 30:6', 'Deut 4:29', 'Deut 6:5') and U('ומצאת') == S_('1Sam 10:2', 'Deut 4:29', 'Neh 9:8')
END_OF_DAYS = P('באחרית', 'הימים', books=T)
assert P('בצר', 'לך') == ['Deut 4:30'] and END_OF_DAYS == S_('Deut 31:29', 'Deut 4:30', 'Gen 49:1', 'Num 24:14') and P('ושבת', 'עד', 'יהוה', 'אלהיך') == S_('Deut 30:2', 'Deut 4:30') and P('ושמעת', 'בקלו') == S_('Deut 30:2', 'Deut 4:30')
assert P('אל', 'רחום') == S_('Deut 4:31', 'Exod 34:6', 'Ps 86:15') and U('ירפך') == S_('1Chr 28:20', 'Deut 31:6', 'Deut 31:8', 'Deut 4:31') and P('ברית', 'אבתיך') == ['Deut 4:31'] and 'וזכרתי' in words('Lev', 26, 42)
# F5's facts: the one God
CREATED = LEMV('1254 a', T)
assert P('שאל', 'נא', 'לימים') == ['Deut 4:32'] and P('לימים', 'ראשנים') == ['Deut 4:32'] and P('אשר', 'ברא', 'אלהים', 'אדם') == ['Deut 4:32'] and CREATED == S_('Deut 4:32', 'Exod 34:10', 'Gen 1:1', 'Gen 1:21', 'Gen 1:27', 'Gen 2:3', 'Gen 2:4', 'Gen 5:1', 'Gen 5:2', 'Gen 6:7', 'Num 16:30')
assert P('השמים', 'ועד', 'קצה', 'השמים') == ['Deut 4:32'] and lemma_of('Deut', 4, 32, 'ראשנים') == ['7223']
assert P('השמע', 'עם', 'קול', 'אלהים') == ['Deut 4:33'] and [(s, x) for s, x, m in LEMT('2421', ('Deut',)) if m == 'HC/Vqw3ms'] == [('Deut 4:33', 'ויחי'), ('Deut 5:26', 'ויחי')]
STRONG_HAND = sorted(set(P('ביד', 'חזקה')) | set(P('וביד', 'חזקה')) | set(P('יד', 'חזקה'))); OUTSTRETCHED = sorted(set(P('ובזרוע', 'נטויה')) | set(P('ובזרע', 'נטויה')) | set(P('בזרוע', 'נטויה')) | set(P('בזרע', 'נטויה')) | set(P('זרוע', 'נטויה')))
assert P('הנסה', 'אלהים') == ['Deut 4:34'] and P('גוי', 'מקרב', 'גוי') == ['Deut 4:34'] and P('במסת', 'באתת', 'ובמופתים') == ['Deut 4:34'] and len(STRONG_HAND) == 16 and OUTSTRETCHED == S_('2Kgs 17:36', 'Deut 26:8', 'Deut 4:34', 'Deut 5:15', 'Exod 6:6', 'Ezek 20:33', 'Ezek 20:34', 'Ps 136:12')
assert words('Deut', 26, 8)[-6:] == ['ובזרע', 'נטויה', 'ובמרא', 'גדל', 'ובאתות', 'ובמפתים'] and P('ובמוראים', 'גדלים') == ['Deut 4:34'] and 'ובזרוע' in W4(34) and 'ובזרע' in words('Deut', 26, 8)   # the arm plene here, defective there
CREED = P('יהוה', 'הוא', 'האלהים'); NONE_ELSE = P('אין', 'עוד')
assert P('אתה', 'הראת', 'לדעת') == ['Deut 4:35'] and CREED == S_('1Kgs 18:39', '1Kgs 8:60', '2Chr 33:13', 'Deut 4:35', 'Deut 4:39') and NONE_ELSE == S_('1Kgs 8:60', '2Kgs 4:6', 'Deut 4:35', 'Deut 4:39', 'Jer 48:2', 'Ps 74:9') and U('מלבדו') == ['Deut 4:35']
assert P('מן', 'השמים', 'השמיעך') == ['Deut 4:36'] and U('ליסרך') == ['Deut 4:36'] and P('אשו', 'הגדולה') == ['Deut 4:36'] and words('Exod', 20, 22)[-5:] == ['כי', 'מן', 'השמים', 'דברתי', 'עמכם']
SEED_AFTER = sorted(set(P('זרעו', 'אחריו')) | set(P('בזרעו', 'אחריו')) | set(P('זרעך', 'אחריך')) | set(P('וזרעך', 'אחריך')) | set(P('לזרעך', 'אחריך')) | set(P('בזרעם', 'אחריהם')) | set(P('זרעם', 'אחריהם')))
assert P('ותחת', 'כי', 'אהב') == ['Deut 4:37'] and P('ויבחר', 'בזרעו', 'אחריו') == ['Deut 4:37'] and SEED_AFTER == S_('1Chr 17:11', '2Sam 7:12', 'Deut 10:15', 'Deut 4:37', 'Gen 17:10', 'Gen 17:7', 'Gen 17:9', 'Gen 48:4') and P('בכחו', 'הגדל') == ['Deut 4:37']
assert P('גוים', 'גדלים', 'ועצמים', 'ממך') == S_('Deut 4:38', 'Deut 9:1') and U('להביאך') == ['Deut 4:38'] and 'והורשתם' in words('Num', 33, 52) and 'תורישו' in words('Num', 33, 55)
assert P('וידעת', 'היום', 'והשבת', 'אל', 'לבבך') == ['Deut 4:39'] and P('בשמים', 'ממעל', 'ועל', 'הארץ', 'מתחת') == S_('1Kgs 8:23', 'Deut 4:39', 'Josh 2:11') and P('בשמים', 'ממעל') == S_('1Kgs 8:23', 'Deut 4:39', 'Deut 5:8', 'Exod 20:4', 'Josh 2:11')
assert P('אשר', 'ייטב', 'לך') == S_('Deut 4:40', 'Deut 6:3', 'Ruth 3:1') and P('תאריך', 'ימים', 'על', 'האדמה') == ['Deut 4:40'] and P('על', 'האדמה', 'אשר', 'יהוה', 'אלהיך', 'נתן', 'לך') == S_('Deut 25:15', 'Deut 4:40', 'Deut 5:16', 'Exod 20:12')
# F6's facts: the cities and the frame
THEN_IMPF = [(s, ws[i + 1][0]) for (b, c, v), ws in by.items() if b in T for i, (x, m) in enumerate(ws) if x == 'אז' and i + 1 < len(ws) and ws[i + 1][1] and ws[i + 1][1][:4] in ('HVqi', 'HVhi') for s in [f'{b} {c}:{v}']]
assert P('אז', 'יבדיל') == ['Deut 4:41'] and len(U('אז', books=T)) == 14 and THEN_IMPF == [('Deut 4:41', 'יבדיל'), ('Deut 29:19', 'יעשן'), ('Exod 15:1', 'ישיר'), ('Lev 26:34', 'תרצה'), ('Lev 26:34', 'תשבת'), ('Num 21:17', 'ישיר')]   # the DB's verse order is alphabetical by book
SET_APART = LEMV('914', ('Deut',))
assert SET_APART == S_('Deut 10:8', 'Deut 19:2', 'Deut 19:7', 'Deut 29:20', 'Deut 4:41') and P('שלש', 'ערים') == S_('Amos 4:8', 'Deut 19:7', 'Deut 19:9', 'Deut 4:41') and P('שלש', 'הערים') == ['Num 35:14']
assert P('בעבר', 'הירדן', 'מזרחה', 'שמש') == ['Deut 4:41'] and sorted(set(P('מזרחה', 'שמש', books=T)) | set(P('מזרח', 'שמש', books=T))) == S_('Deut 4:41', 'Deut 4:47')
MANSLAYER = U('רוצח', 'רצח', 'הרצח', 'הרוצח')
assert P('לנס', 'שמה', 'רוצח') == ['Deut 4:42'] and P('לנס', 'שמה') == S_('Deut 4:42', 'Num 35:6') and len(MANSLAYER) == 28 and len([s for s in MANSLAYER if s.startswith('Num 35')]) == 14 and PT('Deut', 4, 42, 'רוצח') == ['רוֹצֵחַ']
NO_KNOWLEDGE = P('בבלי', 'דעת'); NOT_HIS_ENEMY = P('והוא', 'לא', 'שנא', 'לו')
assert NO_KNOWLEDGE == S_('Deut 19:4', 'Deut 4:42', 'Job 35:16', 'Josh 20:3', 'Josh 20:5') and NOT_HIS_ENEMY == S_('Deut 19:4', 'Deut 4:42') and U('וחי', books=('Deut', 'Num')) == S_('Deut 19:4', 'Deut 19:5', 'Deut 4:42', 'Deut 5:24', 'Num 21:8', 'Num 21:9')
MANSLAYER_DIFF = DIFF(('Deut', 4, 42), ('Deut', 19, 4)); MANSLAYER_SHARED = SHARED(('Deut', 4, 42), ('Deut', 19, 4))
assert MANSLAYER_DIFF[2:4] == [('replace', ['ירצח'], ['יכה']), ('replace', ['מתמול', 'שלשום', 'ונס', 'אל', 'אחת', 'מן', 'הערים', 'האל', 'וחי'], ['מתמל', 'שלשם'])] and MANSLAYER_SHARED == ['את', 'רעהו', 'בבלי', 'דעת', 'והוא', 'לא', 'שנא', 'לו']
GOLAN = U('גולן', 'גלון')
assert GOLAN == S_('1Chr 6:56', 'Deut 4:43', 'Josh 20:8', 'Josh 21:27') and 'Deut 4:43' in U('בצר') and 'Josh 20:8' in U('בצר') and 'Deut 4:43' in U('ראמת') and words('Josh', 20, 8)[17] == 'גלון' and W4(43)[11] == 'גולן' and SHARED(('Deut', 4, 43), ('Josh', 20, 8)) == ['את', 'בצר', 'במדבר']
assert U('לגדי') == ['Deut 4:43'] and U('למנשי') == ['Deut 4:43'] and U('בגלעד', books=T) == ['Deut 4:43']
assert P('וזאת', 'התורה') == ['Deut 4:44'] and P('אשר', 'שם', 'משה', 'לפני') == ['Deut 4:44'] and P('לפני', 'בני', 'ישראל', books=('Deut',)) == ['Deut 4:44']
TESTIMONIES = LEMV('5713 b', T)
assert P('אלה', 'העדת') == ['Deut 4:45'] and P('העדת', 'והחקים', 'והמשפטים') == S_('Deut 4:45', 'Deut 6:20') and TESTIMONIES == S_('Deut 4:45', 'Deut 6:17', 'Deut 6:20') and P('אשר', 'דבר', 'משה') == S_('Deut 1:1', 'Deut 4:45') and SHARED(('Deut', 4, 45), ('Deut', 1, 1)) == ['אשר', 'דבר', 'משה', 'אל'] and P('בצאתם', 'ממצרים') == S_('2Chr 5:10', 'Deut 4:45', 'Deut 4:46', 'Josh 5:4', 'Josh 5:5')
assert P('בגיא', 'מול', 'בית', 'פעור') == S_('Deut 3:29', 'Deut 4:46') and P('סיחן', 'מלך', 'האמרי', 'אשר', 'יושב', 'בחשבון') == S_('Deut 1:4', 'Deut 4:46') and SHARED(('Deut', 4, 46), ('Deut', 1, 4)) == ['סיחן', 'מלך', 'האמרי', 'אשר', 'יושב', 'בחשבון']
assert P('ויירשו', 'את', 'ארצו') == S_('Deut 4:47', 'Num 21:35') and P('שני', 'מלכי', 'האמרי') == S_('Deut 3:8', 'Deut 4:47', 'Josh 24:12') and SHARED(('Deut', 4, 47), ('Deut', 3, 8)) == ['שני', 'מלכי', 'האמרי', 'אשר', 'בעבר', 'הירדן']
assert P('מערער', 'אשר', 'על', 'שפת', 'נחל', 'ארנן') == S_('Deut 2:36', 'Deut 4:48') and P('הר', 'שיאן') == ['Deut 4:48'] and U('שיאן') == ['Deut 4:48'] and U('שרין', 'שריון') == S_('1Sam 17:38', 'Dan 3:25', 'Deut 3:9') and U('שניר', 'ושניר') == S_('1Chr 5:23', 'Deut 3:9', 'Song 4:8') and P('הוא', 'חרמון') == ['Deut 4:48']
assert P('ים', 'הערבה') == S_('2Kgs 14:25', 'Deut 3:17', 'Deut 4:49', 'Josh 12:3', 'Josh 3:16') and P('אשדת', 'הפסגה') == S_('Deut 3:17', 'Deut 4:49') and words('Deut', 3, 17)[4:7] == ['ועד', 'ים', 'הערבה'] and words('Josh', 12, 3)[-2:] == ['אשדות', 'הפסגה']
# THE RETELLINGS' DELTAS RECOMPUTED (the readback rows' measures — the token counts and the longest shared run, from the DB)
def LEN(b, c, v): return len(words(b, c, v))
PEOR_DELTA = (LEN('Deut', 4, 3), LEN('Num', 25, 3), LEN('Num', 25, 5), LEN('Num', 25, 9)); HOREB_DELTA = (LEN('Deut', 4, 11), LEN('Exod', 19, 17), LEN('Exod', 19, 18), len(SHARED(('Deut', 4, 11), ('Exod', 19, 17))))
TABLETS_DELTA = (LEN('Deut', 4, 13), LEN('Exod', 31, 18), LEN('Exod', 34, 28), len(SHARED(('Deut', 4, 13), ('Exod', 34, 28)))); BAR_DELTA = (LEN('Deut', 4, 21), LEN('Deut', 1, 37), LEN('Deut', 3, 26), LEN('Num', 20, 12), len(SHARED(('Deut', 4, 21), ('Deut', 1, 37))))
INSTR_DELTA = (LEN('Deut', 4, 34), LEN('Deut', 26, 8), LEN('Deut', 7, 19)); FRAME_DELTA = (LEN('Deut', 4, 45), LEN('Deut', 1, 1), len(SHARED(('Deut', 4, 45), ('Deut', 1, 1))))
BORDERS_DELTA = ((LEN('Deut', 4, 46), LEN('Deut', 1, 4), len(SHARED(('Deut', 4, 46), ('Deut', 1, 4)))), (LEN('Deut', 4, 47), LEN('Deut', 3, 8), len(SHARED(('Deut', 4, 47), ('Deut', 3, 8)))), (LEN('Deut', 4, 48), LEN('Deut', 2, 36), len(SHARED(('Deut', 4, 48), ('Deut', 2, 36)))), (LEN('Deut', 4, 49), LEN('Deut', 3, 17), len(SHARED(('Deut', 4, 49), ('Deut', 3, 17)))))
assert PEOR_DELTA == (20, 8, 11, 6) and HOREB_DELTA == (13, 11, 18, 1) and TABLETS_DELTA == (15, 16, 22, 2) and BAR_DELTA == (21, 11, 19, 25, 1) and INSTR_DELTA == (27, 11, 25) and FRAME_DELTA == (12, 22, 4), (PEOR_DELTA, HOREB_DELTA, TABLETS_DELTA, BAR_DELTA, INSTR_DELTA, FRAME_DELTA)
assert BORDERS_DELTA == ((20, 17, 6), (16, 17, 6), (11, 23, 6), (11, 13, 3)), BORDERS_DELTA

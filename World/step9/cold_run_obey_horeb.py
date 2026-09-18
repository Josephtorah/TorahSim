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
assert GUARDED == 52, ("the guard counted %d expectations, the tripwire holds 52" % GUARDED)   # the cells' asks summed by the generator before the first graded run (F1 )
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

# ---- THE READBACK ON CHAPTER 4 — the first form's (R1)-(R6) applied a second time: ELEVEN reference rows, the deltas recomputed above ----
GRADES = ('VERBATIM', 'TURNED', 'SHORTENED', 'EXPANDED', 'SUPPLIED', 'DISAGREES')
def rb(verses, told, tape_kind, tape_verse, entry, grade, why, open_=False):
    assert grade in GRADES, grade
    return {'verses': verses, 'told': told, 'tape_kind': tape_kind, 'tape_verse': tape_verse, 'entry': entry, 'grade': grade, 'why': why, 'open': open_}
READBACK = [
    rb('Deut 4:3-4', "your eyes have seen what the LORD did at Baal-peor: every man who followed Baal-peor the LORD your God destroyed from your midst; you who cleave to the LORD are alive this day", 'israel_yoked_to_baal_peor', 'Num 25:3', 'yoked_to_baal_peor on israel_people (25:3); plague_struck CLOSED at 25:8 with the twenty-four thousand in the close', 'SHORTENED', "twenty tokens for 25:3-9's telling (25:3 eight, 25:5 eleven, 25:9 six — computed): the yoking, the judges' slaying and the plague's count folded into 'destroyed from your midst'; 'you who cleave' the survivors — the plague's close READ; BK.peor by CALL"),
    rb('Deut 4:10-11', "the day you stood before the LORD your God at Horeb … you came near and stood under the mountain, and the mountain burned with fire to the heart of heaven, darkness, cloud and thick darkness", 'lord_descended', 'Exod 19:18', 'lord_descended on the-mountain (19:18, 19:20) at the giving\'s day (1, 3, 7); thunder_and_horn (19:16); people_sanctified (19:10-15)', 'EXPANDED', "thirteen tokens for 19:17's eleven and 19:18's eighteen, one shared ('the mountain' — computed): 'under the mountain' 19:17's phrase (Exod 24:4, 32:19 its other seats); the heart of heaven, the darkness, cloud and thick darkness told larger than 19:18's smoke (5:22's kin)"),
    rb('Deut 4:12, 15', "and the LORD spoke to you from the midst of the fire: a voice of words you heard, but no form, only a voice; you saw no form on the day the LORD spoke to you at Horeb", 'ten_words_declared', 'Deut 4:10', 'covenant_declared on israel_people dated (1, 3, 7) — THE SUPPLIED LINE (Exod 20:1 the first telling, no line on the tape)', 'SUPPLIED', "THE TAPE'S HOLE: Exodus 20:1's 'and God spoke all these words' has no line on the tape (the tape runs from Exod 19:20 to 24:1 — the Decalogue compiled as the law layer, no narrative line): written ONCE at its own time, dated (1, 3, 7) by the retrograde marker at Deut 4:10 (the ink's own 'the day you stood'); 'from the midst of the fire' eleven seats, 'a voice of words' one"),
    rb('Deut 4:13', "and he declared to you his covenant which he commanded you to do, the ten words, and he wrote them on two tablets of stone", 'tablets_given', 'Deut 4:13', 'tablets_delivered on moses dated (1, 4, 17) — THE SUPPLIED LINE (Exod 31:18 the first telling, no line on the tape)', 'SUPPLIED', "THE TAPE'S HOLE: Exodus 31:18's giving of the two tablets has no line on the tape (the erection runner folded the tablets into the ascent's line at W7): written ONCE at its own time, dated (1, 4, 17) by the retrograde marker at Deut 4:13 — the fortieth day of the ascent, the breaking's day (Taanit 28b:9 — given and broken on one day); 'the ten words' three seats; the tablets PLENE here (4:13, 9:11, 1 Kings 8:9), defective at every Exodus seat"),
    rb('Deut 4:20', "the LORD took you and brought you out of the iron furnace, out of Egypt, to be a people of inheritance to him as this day", 'brought_out', 'Exod 12:51', 'brought_out on israel_people (12:51, 12:41) — the exodus day', 'EXPANDED', "'the iron furnace' told only here in the Torah (1 Kings 8:51 and Jeremiah 11:4 outside; the furnace-word's six seats computed; Genesis 15:17's smoking furnace another word — PR.pieces('furnace') by CALL); 'a people of inheritance' one seat"),
    rb('Deut 4:21-22', "the LORD was angry with me on your account and swore that I should not cross the Jordan nor come into the good land; for I die in this land, I do not cross the Jordan", 'sentence_at_meribah', 'Num 20:12', 'barred_from_the_land on moses OPEN (20:12) — the tape\'s one entry', 'DISAGREES', "THE THIRD TELLING OF THE BAR: 'on your account' (4:21) with 1:37's 'for your sakes' and 3:26's 'was wroth for your sakes' against Numbers 20:12's 'because you did not believe in Me'; AND AN OATH the tape never wrote ('and swore that I should not cross') — the 1b row 1:37 WIDENED by a telling: the tape's one entry stands, no oath written (an oath told only in a retelling of a sentence the tape carries is the sentence read back); Psalm 106:32 outside, read, not run; OS.the_spies_read_back('the_bars_ground') by CALL — an OPEN row", open_=True),
    rb('Deut 4:32', "ask now of the former days which were before you, since the day God created man upon the earth, from one end of heaven to the other", 'evening_and_morning', 'Gen 1:31', "the sixth day's marker at Gen 1:31 ('Adam created (1:27)', the era life:the_human); formed_from_dust on adam (Gen 2:7)", 'SHORTENED', "a time-reference clause for the creation's telling — 'created' Genesis 1:27's verb, the book's one seat (the verb's eleven Torah seats computed; PS.creation('created_made') by CALL); Chagigah 11b:21-24 the bounds of inquiry from this verse"),
    rb('Deut 4:34', "or has a god tried to come and take him a nation from the midst of a nation, by trials, by signs, by wonders, by war, by a mighty hand, by an outstretched arm and by great terrors, according to all the LORD your God did for you in Egypt before your eyes", 'brought_out', 'Exod 12:51', 'brought_out on israel_people (12:51); the ten plagues\' HEAVEN entries on Egypt; the sea', 'EXPANDED', "THE SEVEN INSTRUMENTS told here (twenty-seven tokens; 26:8's four in eleven, 7:19's five in twenty-five — computed): the plagues' ten (ES.plagues('ten') by CALL) and the sea's ten (ES.sea('ten_at_sea')) the first tellings; 'the mighty hand' sixteen seats, 'the outstretched arm' eight; the arm PLENE here, defective at 26:8; the Sifrei 301:21 glosses 26:8 by this verse (the Haggadah's row)"),
    rb('Deut 4:37-38', "because he loved your fathers he chose their seed after them and brought you out with his presence, with his great power, out of Egypt, to dispossess nations greater and mightier than you, to bring you in, to give you their land for an inheritance as this day", 'brought_out', 'Exod 12:51', "brought_out on israel_people (12:51); land_granted since Genesis 15:18 (PR.call('land_seats') by CALL); the dispossess debit on israel_people OPEN (Num 33:50-56)", 'EXPANDED', "'because he loved your fathers' 10:15's kin; 'their seed after them' the covenant's phrase at eight seats (Genesis 17:7-10, 48:4, 2 Samuel 7:12 — computed); 'with his presence' Onkelos 'with his Memra'; 'to dispossess nations greater and mightier' 9:1's kin — the OPEN dispossess debit READ; 'as this day' six seats in the book"),
    rb('Deut 4:44-45', "and this is the Torah which Moses set before the children of Israel; these are the testimonies, the statutes and the judgments which Moses spoke to the children of Israel when they came out of Egypt", 'speech_opened', 'Deut 1:1', 'torah_expounded on israel_people at (40, 11, 1) — the book\'s one act of its own day', 'EXPANDED', "THE SECOND FRAME (R6): twelve tokens with 1:1's twenty-two, four shared ('which Moses spoke to' — computed); 'the testimonies, the statutes and the judgments' for 'the words'; 'when they came out of Egypt' the era's stamp, no day — NO WRITE, the first frame's status stands; the footer 4:45 closes the block (Deut 1:1, Deut 4:45] with two daemons"),
    rb('Deut 4:46-49', "beyond the Jordan in the valley over against Beth-peor, in the land of Sihon king of the Amorites who dwelt in Heshbon, whom Moses and the children of Israel smote … and they possessed his land and the land of Og king of Bashan, the two kings of the Amorites beyond the Jordan toward the sunrise; from Aroer on the bank of the brook Arnon to Mount Sion which is Hermon, and all the Arabah beyond the Jordan eastward to the sea of the Arabah under the slopes of Pisgah", 'sihon_smitten_land_possessed', 'Num 21:24', "land_possessed on israel_people (21:24-25, 21:35); kings_smitten on sihon and og; encamped_at the plains of Moab (22:1)", 'SHORTENED', "THE RETELLING OF A RETELLING: the speech's own 1:4 (six shared with 4:46), 3:8 (six with 4:47), 2:36 (six with 4:48), 3:17 (three with 4:49) quoted in their own clauses (computed); Mount Sion the fourth name for Hermon (3:9's Sirion and Senir); the valley opposite Beth-peor 3:29's (BK.the_call('last_camp') by CALL); CK.well_and_kings('deut3_delta') and BO.the_four_sides('the_promised_extents') by CALL"),
]
RB_GRADES = collections.Counter(r['grade'] for r in READBACK)
assert len(READBACK) == 11 and RB_GRADES == collections.Counter({'EXPANDED': 5, 'SHORTENED': 3, 'SUPPLIED': 2, 'DISAGREES': 1}) and [r['verses'] for r in READBACK if r['open']] == ['Deut 4:21-22'], (len(READBACK), RB_GRADES)

DATA = {
    'the_readback': {'value': READBACK, 'settings': {'the_first_form': "THE_LOOP.md step 6 (the owner's 'Yes 1. Go', 2026-09-15) on its second chapter: a retelling is a REFERENCE ROW, never a second act; ELEVEN rows — SHORTENED 3, EXPANDED 5, SUPPLIED 2, DISAGREES 1; the deltas recomputed from the DB; THE TAPE'S HOLE (Exodus 20:1, 31:18 — first tellings with no line) written once at its own time by the retrograde markers at Deut 4:10 and 4:13; the bar's DISAGREES row widened, OPEN", 'the_laws_half': "the laws re-read against the ledger from chapter 5 on — OWED to its own sitting (4:16-19's image law is its forerunner: the second word restated, its engine OWED)"}},
    'the_law_bal_tosif': {'value': {'time': 'in_its_time_no_intent__out_of_its_time_intent', 'spoils': 'an_addition_that_voids_the_mitzva', 'pair': 'adding_an_act__diminishing_an_omission'}, 'settings': {'rava': "bal tosif in the mitzva's time needs no intent; out of its time needs intent — the sleeper in the sukkah on the eighth day exempt without intent (Rosh Hashanah 28b:8-9, 28b:23-24; Eruvin 96a:5)", 'the_priest': "the priest who adds a blessing of his own — 'you shall not add' (Rosh Hashanah 28b:10); in the middle of the text (28b:11); the whole day his time, another congregation may come (28b:13)", 'the_tefillin': "a second pair on the Sabbath — a time for tefillin (the first tanna: an addition) or not (Rabban Gamliel: no addition), the dispute recast on intent thrice (Eruvin 95b:19-96a:4); R. Natan: at night one may keep them on, no bal tosif (96a:11)", 'the_elder': "the rebellious elder liable only where the addition SPOILS — five compartments made as one; a fifth placed beside as well — R. Zeira: an outer compartment not exposed to the air is unfit, so the fifth spoils either way (89a:2; retyped 2026-09-17 from the whole row); the lulav by the binding, the fringes by the upper knot (Sanhedrin 88b:14-89a:2; Mishnah Sanhedrin 11:3)", 'the_pair': "R. Eliezer's four sprinklings against R. Yehoshua's one on mixed bloods — 'do not add' against 'do not diminish'; diminishing an omission, adding an act with the hand (Rosh Hashanah 28b:15-18)", 'the_sifrei': "the Sifrei 82:5 on 13:1 — a fifth species, a fifth fringe, a fifth blessing: the exhibit (credited by name)"}, 'source': "4:2 the plural's one seat; 13:1 the singular's (forward)"},
    'the_teach_your_sons': {'value': {'who': 'the_sons_and_the_sons_sons', 'not': 'the_daughters', 'extent': 'bible_alone'}, 'settings': {'kiddushin': "the grandfather's duty from 'your sons' sons' (4:9) against 11:19's 'your sons'; whoever teaches his son is credited through the generations; the daughters excluded; Zevulun ben Dan taught by his father's father — Bible alone in the extent (Kiddushin 30a:3-6)", 'as_from_sinai': "teaching a son's son — as if received from Sinai: 4:9 juxtaposed to 4:10's 'the day you stood at Horeb' (Kiddushin 30a:7)", 'in_awe': "the same juxtaposition: as at Sinai in awe, fear, quaking and trembling, so Torah in every generation (Berakhot 22a:4; Moed Katan 15a:18); the seminal-emission decree from it (Berakhot 21b:8; Ezra's — another engine)", 'the_forgetter': "whoever forgets a matter of his study violates a prohibition — 'take heed … lest you forget' (Menachot 99b:3; Avot 3:8 — as if guilty of death, unless it was too hard); R. Avin: 'take heed', 'lest', 'do not' are prohibitions (Shevuot 36a:20 the self-curse at the same clause)"}, 'source': "4:9 'make them known to your sons and to your sons' sons'"},
    'the_horeb_hole': {'value': {'exod_20_1': 'no_line_on_the_tape', 'exod_31_18': 'no_line_on_the_tape'}, 'settings': {'measured': "the tape runs from Exod 19:20 (moses_went_up, the third ascent) to Exod 24:1 (elders_ascended): the decalogue runner (span 20:1-17; law_decalogue installed_by covenant_blood_thrown) compiled the law layer and wrote no narrative line; the erection runner folded the tablets into the ascent's line at W7 ('the tablets at 31:18' inside moses_ascended's source) and wrote no line at 31:18", 'the_readbacks_answer': "R3's form — the act told in the retelling with no line on the tape is written ONCE at its own time from the retelling's seat: ten_words_declared dated (1, 3, 7) at the retrograde marker Deut 4:10, tablets_given dated (1, 4, 17) at Deut 4:13", 'd2_candidate': "FILED to the second pass: law_decalogue's installed_by may turn from covenant_blood_thrown (24:8) to ten_words_declared (20:1) — the installing act now on the tape", 'the_second_word': "FILED: the Decalogue's second word (Exodus 20:3-6 — no other gods, no image, no bowing) has NO CELL in any runner; 4:16-19 restates it — the edge obey_horeb -> decalogue names the debt; chapter 5's sitting"}},
    'the_ten_words_seats': {'value': ['Exod 34:28', 'Deut 4:13', 'Deut 10:4'], 'settings': {'computed': "'the ten words' at three Bible seats — Exodus 34:28 alone in Exodus (never at chapter 20), twice in Deuteronomy (ER.tablets('ten_words') by CALL = 3)"}},
    'the_tablets_plene': {'value': {'plene': ['1Kgs 8:9', 'Deut 4:13', 'Deut 9:11'], 'defective_seats': 12}, 'settings': {'computed': "the tablets-word written PLENE (with the vav) at 4:13, 9:11 and 1 Kings 8:9 alone; DEFECTIVE at twelve seats — every Exodus seat and 5:22, 9:15, 10:3 (the reading's crown; the erection's c_tablets_forms by CALL: the Torah's forms counted)"}},
    'the_no_image_list': {'value': ['a graven image', 'the form of any figure', 'the likeness of male or female', 'any beast on the earth', 'any winged bird that flies in the heavens', 'anything that creeps on the ground', 'any fish in the waters under the earth', 'the sun', 'the moon', 'the stars', 'all the host of heaven'], 'settings': {'the_second_word': "Exodus 20:4's 'any likeness of what is in the heavens above, or on the earth beneath, or in the waters under the earth' restated in seven kinds and the host (4:16-19; the likeness-word five times in 16-18, computed) — THE SECOND WORD'S PARAMETER TABLE; its engine OWED (no cell compiles the image law)", 'the_baraita': "Rosh Hashanah 24b:6-7 on Exodus 20:4: 'in heaven' the sun, moon, stars, constellations; 'above' the ministering angels; 'in the earth' mountains, hills, seas, rivers; 'beneath' a tiny worm — the whole baraita about WORSHIP, not making", 'for_study': "Rabban Gamliel's moon forms — 'you shall not make with Me' (Exodus 20:20): the reproducible attendants only (Abaye); the human face by 'not Me'; others made them; in pieces; to teach himself — 'you shall not learn TO DO' (18:9) (Mishnah Rosh Hashanah 2:8; Rosh Hashanah 24a:18-24b:13)", 'the_statues': "all statues forbidden for benefit (R. Meir) / with a staff, bird or orb (the Rabbis); a hand or a foot; the sun, moon or dragon on vessels — cast into the Dead Sea (Mishnah Avodah Zarah 3:1-3)", 'corruption': "'corruption' is idolatry from 4:16 and licentiousness from the flood (the school of R. Yishmael — Chullin 23a:3; Avodah Zarah 23b:9; Bekhorot 57a:12; Temurah 28b:17; Sanhedrin 57a:1); 'any winged bird' the birds' scope (Chullin 139b:17)"}},
    'the_host_apportioned': {'value': 'a_data_note_no_link', 'settings': {'the_pair': "'which the LORD your God APPORTIONED to all the peoples under the whole heaven' (4:19) with 29:25's 'which he had not apportioned to them' — the Sifrei 148:8 on 17:3 reads the two together (not given to the nations for worship): the qal perfect's five Bible seats (computed), two in the Torah", 'rav': "Avodah Zarah 55a:9 — Rav: He let them slip (the same letters read 'made slippery') into their delusion, to drive them from the world; Reish Lakish (55a:10): the one who comes to defile himself is given the opening", 'the_septuagint': "Megillah 9b:1 — the elders added 'to give light' for Ptolemy", 'onkelos': "'prepared' for 'apportioned' — the translation's guard (the reading's row); no link of our own beyond the Sifrei's pair"}},
    'the_bars_third_telling': {'value': ['Deut 1:37', 'Deut 3:26', 'Deut 4:21'], 'settings': {'the_grounds': "'for your sakes' (1:37, at the spies' oath), 'was wroth for your sakes' (3:26, at the plea), 'on your account and SWORE' (4:21) against Numbers 20:12's 'because you did not believe in Me' — the anger-root's four Torah seats all this book's (1:37, 4:21, 9:8, 9:20; computed)", 'the_oath': "4:21's oath ('that I should not cross the Jordan') the tape never wrote — the sentence read back with an oath supplied: no second write (the 1b decision (R4) held: a disagreement is an OPEN row)", 'outside': "Psalm 106:32 'it went ill with Moses for their sakes' — the ink's own bridge outside the Torah, read, not run"}, 'source': "OS.the_spies_read_back('the_bars_ground') by CALL — 1b's DISAGREES row; this chapter's beside it"},
    'the_exile_case': {'value': {'head': 'when_you_beget_sons_and_grow_old_and_corrupt', 'arms': ['perish quickly', 'not prolong days', 'scattered among the peoples', 'few in number', 'serve wood and stone', 'seek and find', 'return and hearken', 'mercy — the covenant not forgotten'], 'timer': None}, 'settings': {'the_case_token': "'when' (4:25) with the imperfect — the chapter's one case; the arms 4:26-31", 'no_timer': "'in the end of days' (4:30) — a prophecy, not a due: no clock item; the four Torah seats of the phrase computed (Genesis 49:1, Numbers 24:14, Deuteronomy 4:30, 31:29)", 'the_tochacha': "the arms' first tellings Leviticus 26:33 (scattered_among_nations) and 26:42 (covenant_remembered) — TC.recovery(True, True) and TC.NOT_BROKEN by CALL; 28:36, 28:64 forward; no exile on the tape, no entry written", 'hastened': "Gittin 88a:15-17 — 'grown old' (venoshantem — 'grown old') by its letters eight hundred and fifty-two, the exile hastened by two years (Sanhedrin 38a:6 Ulla's righteousness); after grandchildren a matter is old; seven dynasties from the seven verbs", 'the_reading': "Megillah 31b:2 — the Ninth of Av's Torah reading 4:25-40 (some say)"}},
    'the_witnesses_chain': {'value': {'this_chapter': 'Deut 4:26', 'the_chain': ['Deut 4:26', 'Deut 30:19', 'Deut 31:28', 'Deut 32:1']}, 'settings': {'sifrei_306_1': "the Sifrei 306:1 on 32:1 — the heavens and the earth called to witness: 4:26 the third of eleven (read at the reading); 30:19's first seven words identical to 4:26's (computed); 'I call to witness' three Bible seats (4:26, 30:19, Jeremiah 42:19)"}},
    'the_creed': {'value': ['Deut 4:35', 'Deut 4:39'], 'settings': {'computed': "'the LORD, he is God' five Bible seats — 4:35, 4:39, Elijah's (1 Kings 18:39), Solomon's (1 Kings 8:60), Manasseh's (2 Chronicles 33:13); 'none else' six; 'none else beside him' one (4:35); 'in heaven above and on the earth beneath' Rahab's and Solomon's (Joshua 2:11, 1 Kings 8:23)", 'kingship': "Rosh Hashanah 32b:17 — 4:39 and 4:35 verses of kingship (R. Yosei) or not (R. Yehuda); Tosefta Rosh Hashanah 2:11", 'even_sorcery': "'none else beside him' — R. Chanina: even sorcery (Chullin 7b:14; Sanhedrin 67b:7)", 'the_seventh_son': "Gittin 57b:17 — 4:39 the seventh son's creed"}},
    'the_inquiry_limits': {'value': {'from': 'the_day_god_created_man', 'within': 'one_end_of_heaven_to_the_other', 'to': 'one_student'}, 'settings': {'chagigah': "'ask now of the days past' (4:32) singular — one may inquire of creation, not two; 'from one end of heaven to the other' — within the world's bounds, not above, below, before, after (Chagigah 11b:21-24; Tosefta Chagigah 2:3; Mishnah Chagigah 2:1)", 'adams_height': "from one end to the other, diminished after the sin (Chagigah 12a:2; Sanhedrin 38b:7)"}},
    'the_instruments': {'value': {'deut_4_34': ['trials', 'signs', 'wonders', 'war', 'a mighty hand', 'an outstretched arm', 'great terrors'], 'deut_26_8': ['a mighty hand', 'an outstretched arm', 'great terror', 'signs', 'wonders'], 'deut_7_19': ['the great trials', 'the signs', 'the wonders', 'the mighty hand', 'the outstretched arm']}, 'settings': {'the_haggadah': "Mishnah Pesachim 10:4 — 'he expounds from a wandering Aramean until he finishes the whole portion' (26:5-8): the Sifrei 301:21 glosses 26:8's 'great terror' by 4:34's 'great terrors' — the revelation of the Shekhinah (the reading's row)", 'plene': "the arm PLENE at 4:34, defective at 26:8 (computed)", 'tefillin': "Berakhot 6a:24 — 4:7, 4:8 and 4:34 in the compartments of God's tefillin; Megillah 11a:9 — Rav Ashi's introduction to Esther from 4:34"}},
    'the_three_cities': {'value': {'east': ['Bezer (Reuben)', 'Ramoth in Gilead (Gad)', 'Golan in Bashan (Manasseh)'], 'west_forward': ['Kedesh', 'Shechem', 'Hebron'], 'debit': 'OPEN'}, 'settings': {'not_until_all_six': "Mishnah Makkot 2:4 / Makkot 9b:14 — until the three in the land of Canaan were selected, the three beyond the Jordan did not admit; 'six cities of refuge SHALL THEY BE' (Numbers 35:13): the appointment ONE of six — THE DEBIT LEFT OPEN (the design's (d); Joshua 20:7-8 the close outside the Torah, the readback's)", 'a_mitzva_that_came': "R. Simlai (Makkot 10a:15-16): 'toward the sunrise' — shine the sun for murderers; Moses knew and said 'a mitzva that came my way, I will fulfill it'", 'two_rows': "Makkot 9b:18 — Hebron against Bezer, Shechem against Ramoth, Kadesh against Golan; Gilead's murderers (9b:19-10a:3); Reuben first — Joseph's rescue (10a:14)", 'the_names': "RF.DATA['the_six_cities'] by CALL — the names outside Numbers 35, computed by seat; Joshua 20:8 'Gaulon' without the vav, 4:43 'Golan' with it (computed)", 'bezer': "Bezer is not Bozrah (Avodah Zarah 58b:8)"}},
    'the_manslayer_definition': {'value': {'deut_4_42': "who slays his neighbor unawares and hated him not in time past", 'deut_19_4': "who smites his neighbor unawares and hated him not in time past", 'num_35_11': "who smites a soul unwittingly"}, 'settings': {'computed': "4:42 = 19:4's words with 'slays' for 'smites' (the diff: two replacements; the shared run 'his neighbor unawares and hated him not' eight tokens); 'without knowledge' five Bible seats; the murder-verb PLENE at 4:42 (the refuge runner's own assert)", 'the_rows': "'and live' (4:42) — make life livable: the teacher exiled with his school (Makkot 10a:9-11); the slave's surplus (Gittin 12a:11); the quarreling scholars (Sotah 49a:4); 'hated him not' — the enemy not exiled (Mishnah Makkot 2:3; RF.the_manslayer('not_his_enemy') by CALL); 'without seeing' / 'without knowledge' the blind (Makkot 9b:5-8; RF.the_manslayer('without_seeing') by CALL)"}},
    'the_second_frame': {'value': {'deut_4_44_45': 'the_second_speech_s_head', 'write': None}, 'settings': {'r6': "the frame is the book's one act of its own day — at its second seat too: 4:44-45 a stamp of place and era ('when they came out of Egypt' — no day): NO WRITE; torah_expounded stands; the footer 4:45 closes the block (Deut 1:1, Deut 4:45] with two daemons", 'the_word': "'this is nothing but Torah' (the Sifrei 323:1 on 32:29 from 4:44 — the reading's row); 'which Moses SET' read as the drug of life or death (Yoma 72b:14); Torah provides refuge — 4:43's cities juxtaposed to 4:44 (Makkot 10a:11); the nations' plea (Avodah Zarah 2b:6)", 'the_borders': "4:46-49 quote the speech's own 1:4, 3:8, 2:36, 3:17 in their own clauses (computed shared runs 6, 6, 6, 3); Mount Sion the fourth name for Hermon (3:9's Sirion and Senir; 4:48's one seat)"}},
    'the_number_switching': {'value': {'singular_only': [10, 19, 24, 30, 31, 32, 33, 35, 36, 37, 38, 39, 40], 'plural_only': [2, 4, 6, 8, 11, 12, 13, 14, 15, 16, 20, 22, 26, 27, 28], 'both': [1, 3, 5, 9, 21, 23, 25, 29, 34], 'neither': [7, 17, 18, 41, 42, 43, 44, 45, 46, 47, 48, 49]}, 'settings': {'computed': "the second person's number by verse from the morphology (the reading's crown): 'the LORD your God' eleven singular, three plural; the imperatives singular but 4:23's; the frame 41-49 in the third person"}},
    'the_export_chapter_5': {'value': {'export': 30, 'db': 33}, 'settings': {'measured': "Onkelos Deuteronomy's export gives chapter 5 THIRTY verses against the DB's thirty-three (the Decalogue's division) — the one disagreeing chapter; the recorder and the stitcher address by the DB; chapter 5's reading measures the mapping FIRST (nothing built here)"}},
}
assert len(DATA) == 19, len(DATA)

# ===== F1: THE EXHORTATION AND THE ONE LAW (Deut 4:1-8) =====================================================
def the_exhortation(case, data):
    del P_[:]
    ask = case['ask']
    if ask == 'hear_and_do':
        ink('4:1', '"and now, Israel, hear the statutes and the judgments which I teach you, to do them, that you may live and go in and possess the land" — "and now, Israel" %s; "hear" the singular imperative with the PLURAL object "you"; "that you may live" %s; "go in and possess the land" %s; the teach-root\'s sixteen Torah seats all this book\'s, the first here' % (P('ועתה', 'ישראל'), P('למען', 'תחיו', books=T), P('ובאתם', 'וירשתם', 'את', 'הארץ')))
        dat('the row the_number_switching: the second person singular and plural by turns — 4:1 both')
        return out("hear and do (4:1) — the exhortation's head: the singular imperative, the plural object; the teach-root's first seat", ['accepted'])
    if ask == 'add_nothing':
        ink('4:2', '"YOU SHALL NOT ADD to the word which I command you" — the plural %s ONE seat; 13:1 the singular\'s ("you shall not add to it"); the prohibition\'s verbs %s' % (ADD_PL, PROHIB[2]))
        move('Rosh Hashanah 28b:8-9, 28b:23-24; Eruvin 96a:5', "Rava: bal tosif IN ITS TIME needs no intent, OUT OF ITS TIME needs intent — the sleeper in the sukkah on the eighth day; the priest who adds a blessing (28b:10-13 — the whole day his time)")
        move('Sanhedrin 88b:14-89a:2; Mishnah Sanhedrin 11:3', "the addition that SPOILS — five compartments made as one, and a fifth placed beside as well — R. Zeira (89a:2): the outer compartment must meet the air, so the fifth spoils either way; the lulav by the binding, the fringes by the upper knot")
        dat('the row the_law_bal_tosif: %s' % data['the_law_bal_tosif']['value'])
        return out("you shall not add (4:2) — THE CHAPTER'S ONE LAW: a BLOCK on Israel (adding_barred); the exam's parameters — in its time without intent, out of its time with intent (Rava); an addition that spoils (the elder's fifth compartment)", ['accepted'])
    if ask == 'diminish_nothing':
        ink('4:2', '"NOR DIMINISH from it" — the pair\'s two seats %s; the diminish-root\'s Torah seats include Exodus 5:8\'s bricks and the daughters\' 27:4, 36:3 (%d seats)' % (DIMINISH, len(DIMINISH_LEM)))
        move('Rosh Hashanah 28b:15-18', "R. Eliezer's four sprinklings against R. Yehoshua's one on mixed bloods — 'do not add' against 'do not diminish': diminishing an OMISSION, adding an ACT with the hand")
        return out("nor diminish (4:2) — the pair's other arm: an omission where adding is an act (R. Yehoshua); 13:1 the second seat forward", ['accepted'])
    if ask == 'add_out_of_its_time':
        ink('4:2', '"you shall not add" — the addition OUT OF THE MITZVA\'S TIME: the sleeper in the sukkah on the eighth day, the second pair of tefillin on a day no time for tefillin')
        move('Rosh Hashanah 28b:9, 28b:24; Eruvin 96a:5', "Rava: out of its time bal tosif needs intent — the sleeper without intent EXEMPT; the eighth day outside the land kept by the Sages")
        return out("an addition out of its time (Rosh Hashanah 28b) — no intent, no transgression: the sleeper on the eighth day exempt", ['exempt'])
    if ask == 'add_beside':
        ink('4:2', '"you shall not add" — a fifth compartment PLACED BESIDE four made: the challenge says the four stand alone and the fifth stands alone; R. ZEIRA ANSWERS — an outer compartment not exposed to the air makes the head tefillin unfit, so the fifth spoils placed beside as it does made as one (Sanhedrin 89a:2; RETYPED 2026-09-17 from the whole row — the cut had typed the challenge as the ruling); what stands alone is the lulav\'s added species where no binding is required and the fringes\' added thread where no knot is (88b:17-89a:1)')
        move('Sanhedrin 88b:15-89a:2', "the elder liable only where the addition SPOILS — the fifth compartment spoils beside the four as it does among them (R. Zeira); only the unbound species stands alone: the Mishnah 11:3's row resolved")
        return out("an addition placed beside (Sanhedrin 89a:2) — R. Zeira: the fifth compartment spoils the four even beside them; the transgression stands: accepted", ['accepted'])
    if ask == 'baal_peor_seen':
        ink('4:3', '"your eyes have seen what the LORD did at Baal-peor: every man who followed Baal-peor the LORD your God destroyed from your midst" — "Baal-peor" %s; Peor at %d seats; "destroyed from your midst" %s; the retelling %d tokens for Numbers 25:3-9\'s' % (PEOR, len(PEOR_ALL), P('השמידו', 'יהוה', 'אלהיך', 'מקרבך'), PEOR_DELTA[0]))
        move('cold_run_balak (CALL) — BK.peor(plague_count) = %s; BK.peor(peor_service) = %s' % (BK_PLAGUE[0][:60], BK_SERVICE[0][:60]), "the twenty-four thousand; baring oneself to Peor its worship (Mishnah Sanhedrin 7:6)")
        dat('the readback row 4:3-4 SHORTENED — israel_yoked_to_baal_peor (Num 25:3) found; the plague CLOSED at 25:8 read')
        return out("Baal-peor seen (4:3) — Numbers 25:3-9 READ BACK, SHORTENED: the yoking, the slaying and the plague's count in one clause (BK by CALL)", ['accepted'])
    if ask == 'the_cleaving':
        ink('4:4', '"but you who cleave to the LORD your God are alive, all of you, this day" — the cleaving adjective\'s three Bible seats %s; "alive all of you this day" %s' % (CLEAVE, P('חיים', 'כלכם', 'היום')))
        move('Sifrei Devarim 49:2 (the reading); Ketubot 111b:6-8', "how cleave to a consuming fire (4:24)? — cleave to the sages: marry a daughter to a scholar, do business for scholars, benefit scholars (I13 resolved)")
        move('Sanhedrin 64a:11; Sanhedrin 90b:13', "Peor's cord against the dates lightly touching (the reading's crown at its seat); alive even on the day all are dead")
        return out("you who cleave (4:4) — the survivors of Peor; cleaving to a consuming fire resolved as cleaving to the sages (the Sifrei 49:2; Ketubot 111b)", ['accepted'])
    if ask == 'taught_as_commanded':
        ink('4:5', '"behold, I have taught you statutes and judgments AS THE LORD MY GOD COMMANDED ME" — %s one seat; the receipt form "as the LORD commanded me" %s (10:5 the pair); "I have taught you" %s' % (RECEIPT_MY_GOD, RECEIPT_ME, P('ראה', 'למדתי', 'אתכם')))
        move('cold_run_erection (CALL) — ER.ascent(torah_mitzvah) = %s' % (ER_TORAH_MITZVAH['v'],), "Exodus 24:12's 'the torah and the commandment which I have written TO TEACH THEM' — the command the receipt answers; 4:14 'the LORD commanded me at that time to teach you'")
        move('Bekhorot 29a:7-8; Nedarim 37a:2', "as I learned for free, you learned for free — the judge who takes wages, the teacher of Bible: the receipt's own reading")
        dat("the register seat Deut 4:5 ACT — the exhortation's write (adding_barred) carries the verse in its source: the teaching's run (R5)")
        return out("taught as commanded (4:5) — THE RECEIPT in Moses' own voice: the teaching's run of Exodus 24:12's command (ER by CALL); the register seat ACT; free teaching (Bekhorot 29a)", ['accepted'])
    if ask == 'wisdom_before_the_peoples':
        ink('4:6', '"for this is your wisdom and your understanding in the eyes of the peoples" — %s one seat; "a wise and understanding people" %s; "wise and understanding" this and Solomon\'s %s' % (P('חכמתכם', 'ובינתכם'), P('עם', 'חכם', 'ונבון'), P('חכם', 'ונבון')))
        move('Shabbat 75a:4; Avodah Zarah 4b:16', "the mitzva to reckon the seasons and constellations — the wisdom named; 'in the eyes' — the mitzvot strike the nations' faces")
        return out("your wisdom before the peoples (4:6) — the reckoning of the seasons (Shabbat 75a); Solomon's pair the kin", ['accepted'])
    if ask == 'god_so_near':
        ink('4:7', '"for what great nation has God so NEAR to it as the LORD our God whenever we call upon him" — "great nation" %s; "God near" %s — the adjective PLURAL with the plural noun (%s), "upon him" singular' % (P('גוי', 'גדול'), P('אלהים', 'קרבים'), morphs('Deut', 4, 7)[6]))
        move('Sanhedrin 38b:15', "the heretics' verse and its own answer — 'near' plural, 'upon Him' singular (the reading's find at its seat)")
        move('Rosh Hashanah 18a:10; Yevamot 105a:17; Berakhot 6a:24', "a community's sealed sentence torn up — 'whenever we call'; the verse in God's tefillin")
        return out("God so near (4:7) — the plural adjective with the singular 'upon him' (Sanhedrin 38b); a community's sentence never sealed (Rosh Hashanah 18a)", ['accepted'])
    if ask == 'righteous_statutes':
        ink('4:8', '"and what great nation has statutes and judgments so righteous as all this Torah which I set before you this day" — "righteous statutes" %s; "like all this Torah" %s; "which I set before you this day" %s' % (P('חקים', 'ומשפטים', 'צדיקם'), P('ככל', 'התורה', 'הזאת'), P('אשר', 'אנכי', 'נתן', 'לפניכם', 'היום')))
        return out("righteous statutes (4:8) — the exhortation's close: the Torah set before them this day (11:32 the pair)", ['accepted'])
    if ask == 'the_write':
        ink('4:1-8', 'the exhortation with the law inside it — the line add_nothing_commanded')
        dat("adding_barred on israel_people — a BLOCK (the chapter's one law); the line's source 4:1-8 holds the receipt 4:5 (the register seat ACT)")
        return out("the write (4:1-8) — adding_barred on Israel: the one law's block; the receipt inside the line's source", ['adding_barred'])
    return out('no verdict in span', [FX.NONE])


# ===== F2: HOREB RETOLD (Deut 4:9-14) =======================================================================
def horeb_retold(case, data):
    del P_[:]
    ask = case['ask']
    if ask == 'take_heed_lest_you_forget':
        ink('4:9', '"only take heed to yourself and keep your soul diligently, lest you forget the things your eyes saw … and make them known to your sons and to your sons\' sons" — "only take heed to yourself" %s; "keep your soul diligently" %s; the forget-root\'s thirteen seats in the book; "to your sons and your sons\' sons" %s; "make known" %s' % (P('רק', 'השמר', 'לך'), P('ושמר', 'נפשך', 'מאד'), P('לבניך', 'ולבני', 'בניך'), U('והודעתם')))
        move('Menachot 99b:3; Pirkei Avot 3:8; Shevuot 36a:20', "the forgetter violates a prohibition — 'take heed', 'lest', 'do not' (R. Avin); as if guilty of death unless it was too hard; the self-curse's warning at the same clause")
        move('Kiddushin 30a:3-6; Berakhot 22a:4; Moed Katan 15a:18', "the grandfather's duty from 'your sons' sons'; the daughters excluded; the juxtaposition to 4:10 — Torah in awe as at Sinai")
        dat('the row the_teach_your_sons: %s' % data['the_teach_your_sons']['value'])
        return out("take heed lest you forget (4:9) — the forgetter's prohibition (Menachot 99b; Avot 3:8); the grandsons included, the daughters excluded (Kiddushin 30a)", ['accepted'])
    if ask == 'the_daughters_excluded':
        ink('4:9', '"make them known to your sons and to your sons\' sons" — 11:19\'s "your sons" and this verse\'s "sons\' sons": the grandsons taught, the daughters not (the baraita\'s reading of "sons")')
        move('Kiddushin 30a:6', "'your sons' — not your daughters; 'your sons' sons' — the grandsons included: the answer sheet's row")
        return out("the daughters excluded (Kiddushin 30a) — 'your sons' not your daughters; the grandsons taught: exempt from the duty's addressees", ['exempt'])
    if ask == 'the_day_at_horeb':
        ink('4:10', '"the day you stood before the LORD your God at Horeb" — %s one seat; Horeb\'s twelve Torah seats (%d in the Bible), plene at Exodus 33:6 alone; "assemble the people to me" %s (31:12\'s Hakhel the kin)' % (P('יום', 'אשר', 'עמדת'), len(HOREB), P('הקהל', 'לי', 'את', 'העם')))
        move('cold_run_exodus_story (CALL) — ES.sinai(days_r_yose) = %s' % (ES_DAYS['v'],), "Rabbi Yose's days of Sivan — the giving on the seventh (Shabbat 86b:5): the tape's marker at Exodus 19:16, THE DAY the retrograde marker at Deut 4:10 reads")
        move('Kiddushin 30a:7', "teaching a son's son — as if received from Sinai: 4:9 juxtaposed to 'the day you stood at Horeb'")
        move('cold_run_erection (CALL) — ER.presence(horev_plene) = %s' % (ER_HOREB['v'],), "Horeb written plene at Exodus 33:6 alone")
        dat("the readback row 4:10-11 EXPANDED — lord_descended (Exod 19:18) found at (1, 3, 7)")
        return out("the day at Horeb (4:10) — the assembly's day (1, 3, 7) by Rabbi Yose's seventh (ES by CALL); the retrograde marker's day at Deut 4:10", ['accepted'])
    if ask == 'learn_and_teach':
        ink('4:10', '"that they may LEARN to fear me all the days … and that they may TEACH their sons" — the two occurrences one consonantal word, qal and piel by the pointing alone: %s; "to fear me all the days" %s' % (LEARN_TEACH, P('ליראה', 'אתי', 'כל', 'הימים')))
        dat("the reading's crown: learn and teach ONE WORD (the store one gloss; Onkelos one verb twice) — a DATA note on the verse's form")
        return out("learn and teach are one word (4:10) — qal and piel by the pointing alone: the reading's crown, DATA", ['accepted'])
    if ask == 'the_mountain_burning':
        ink('4:11', '"and you came near and stood under the mountain, and the mountain burned with fire to the heart of heaven, darkness, cloud and thick darkness" — "under the mountain" %s; "burned with fire" %s; "to the heart of heaven" %s; the retelling %d tokens for 19:17\'s %d and 19:18\'s %d, %d shared' % (P('תחת', 'ההר'), P('בער', 'באש'), P('עד', 'לב', 'השמים'), HOREB_DELTA[0], HOREB_DELTA[1], HOREB_DELTA[2], HOREB_DELTA[3]))
        dat("the readback row 4:10-11 EXPANDED against Exodus 19:17-18 (the diff recomputed)")
        return out("the mountain burning (4:11) — Exodus 19:17-18 READ BACK, EXPANDED: the heart of heaven, the darkness, cloud and thick darkness told larger than the smoke", ['accepted'])
    if ask == 'the_voice_and_no_form':
        ink('4:12, 15', '"and the LORD spoke to you from the midst of the fire: a voice of words you heard, but no form, only a voice" — the one divine frame %s; "from the midst of the fire" %d seats; "a voice of words" %s; the form-word\'s ten seats, five this chapter\'s; 4:15 "you saw no form" %s' % (DIV, len(FROM_FIRE), P('קול', 'דברים'), P('לא', 'ראיתם', 'כל', 'תמונה')))
        dat("THE TAPE'S HOLE — Exodus 20:1 'and God spoke all these words' has no line on the tape: the readback's finding (the row the_horeb_hole); the SUPPLIED line ten_words_declared dated (1, 3, 7) at the retrograde marker Deut 4:10 writes covenant_declared on Israel")
        return out("the voice and no form (4:12, 15) — THE TAPE'S HOLE: Exodus 20:1's speaking written once at its own time (1, 3, 7) — covenant_declared on Israel (SUPPLIED)", ['covenant_declared'])
    if ask == 'the_ten_words_and_the_tablets':
        ink('4:13', '"and he declared to you his covenant which he commanded you to do, THE TEN WORDS, and he wrote them on two tablets of stone" — "the ten words" %s; "two tablets of stone" %s; the tablets PLENE %s, defective at %d seats; the parser %s' % (TEN_WORDS, P('שני', 'לחות', 'אבנים'), TABLETS_PLENE, len(TABLETS_DEF), TEN_TWO))
        move('cold_run_erection (CALL) — ER.tablets(ten_words) = %s; ER.ascent(seventeenth_tammuz) = %s; ER.tablets(finger_and_forms) = %s' % (ER_TEN['v'], ER_TAMMUZ['v'], ER_FORMS['v']), "'the ten words' three seats; the seventh of Sivan plus forty = the seventeenth of Tammuz (Taanit 28b:9) — the tablets given and broken on one day; the tablets-word's forms")
        dat("THE TAPE'S HOLE — Exodus 31:18's giving has no line: the SUPPLIED line tablets_given dated (1, 4, 17) at the retrograde marker Deut 4:13 writes tablets_delivered on Moses (the erection's effect at its first tape seat)")
        return out("the ten words and the tablets (4:13) — three seats of 'the ten words' (ER by CALL); the tablets plene; Exodus 31:18's giving written once at (1, 4, 17) — tablets_delivered on Moses (SUPPLIED)", ['tablets_delivered'])
    if ask == 'commanded_to_teach':
        ink('4:14', '"and the LORD commanded me at that time to teach you statutes and judgments" — %s one seat; "at that time" fifteen seats in the book; "to teach you" %s' % (P('ואתי', 'צוה', 'יהוה', 'בעת', 'ההוא'), P('ללמד', 'אתכם')))
        move('Nedarim 38a:5; Sanhedrin 21b:25; Nedarim 37a:2', "Rav Chisda's objection — commanded to teach from the outset? the Torah commanded to Moses, the teaching his own; Ezra's kin; the free teaching")
        dat("the row the_horeb_hole's kin: the command to teach (Exodus 24:12) the receipt 4:5 answers")
        return out("commanded to teach (4:14) — the command 4:5's receipt answers (Exodus 24:12); who was commanded disputed (Nedarim 38a)", ['accepted'])
    return out('no verdict in span', [FX.NONE])


# ===== F3: NO IMAGE (Deut 4:15-24) ==========================================================================
def no_image(case, data):
    del P_[:]
    ask = case['ask']
    if ask == 'no_form_seen':
        ink('4:15', '"take good heed to yourselves — for you saw no form on the day the LORD spoke to you at Horeb from the midst of the fire" — %s (Joshua 23:11 the kin); "no form" %s' % (P('ונשמרתם', 'מאד', 'לנפשתיכם'), P('לא', 'ראיתם', 'כל', 'תמונה')))
        return out("no form seen (4:15) — the guard's reason: the voice without a form (4:12 read back)", ['accepted'])
    if ask == 'the_image_list':
        ink('4:16-18', '"lest you corrupt yourselves and make a graven image, the form of any figure, the likeness of male or female, of any beast, of any winged bird, of anything that creeps, of any fish" — the image-word\'s %d seats; "a graven image, the form of any" %s; the likeness-word %d times in 16-18; "male or female" %s; "winged bird" %s; "fish" %s' % (len(IMAGE), P('פסל', 'תמונת', 'כל'), LIKENESS_N, P('זכר', 'או', 'נקבה'), P('צפור', 'כנף'), U('דגה')))
        move('Rosh Hashanah 24b:6-7; Mishnah Rosh Hashanah 2:8; Rosh Hashanah 24a:18-24b:13', "the second word's parameter table on Exodus 20:4 — the sun, moon, stars, constellations; the angels; mountains, hills, seas, rivers; a tiny worm; the forms for study (Rabban Gamliel's moon)")
        move('Mishnah Avodah Zarah 3:1-3; Chullin 23a:3; Chullin 139b:17', "the statues, a hand or a foot, the sun and moon on vessels; 'corruption' is idolatry from 4:16; 'any winged bird' the birds' scope")
        dat('the row the_no_image_list: %s — THE SECOND WORD RESTATED; its engine OWED (no cell compiles Exodus 20:3-6)' % data['the_no_image_list']['value'])
        return out("the no-image list (4:16-18) — Exodus 20:4's likeness restated in seven kinds: THE SECOND WORD'S PARAMETER TABLE as DATA; its engine OWED (chapter 5's sitting)", ['accepted'])
    if ask == 'image_for_study':
        ink('4:16-19', 'the forms of the sun, moon and stars (4:19) — Rabban Gamliel\'s moon forms on the tablet for the witnesses')
        move('Mishnah Rosh Hashanah 2:8; Rosh Hashanah 24b:9-13', "others made them; in pieces; to teach himself — 'you shall not learn TO DO' (18:9): for study permitted")
        return out("the images for study (Rosh Hashanah 24b) — Rabban Gamliel's forms permitted: made by others, in pieces, to teach himself — exempt", ['exempt'])
    if ask == 'image_of_the_host':
        ink('4:19', '"the sun, the moon and the stars, all the host of heaven" — forming their images: "you shall not make with Me" (Exodus 20:20) My attendants')
        move('Rosh Hashanah 24b:8; Mishnah Avodah Zarah 3:3', "the sun, the moon, the stars, the constellations — forming them prohibited (Abaye's answer rejected); the sun and the moon on vessels cast into the Dead Sea")
        return out("an image of the host (Rosh Hashanah 24b:8) — forming the sun and the moon prohibited: the second word's row holds (its engine OWED)", ['accepted'])
    if ask == 'the_host_apportioned':
        ink('4:19', '"and lest you lift your eyes to heaven and see the sun, the moon and the stars, all the host of heaven, and be drawn away and bow to them and serve them — which the LORD your God APPORTIONED to all the peoples under the whole heaven" — "the sun, the moon and the stars" %s; "all the host of heaven" %s; "apportioned" the qal perfect at %s; "to all the peoples under the whole heaven" %s' % (P('השמש', 'ואת', 'הירח', 'ואת', 'הכוכבים'), HOST, [s for s, _ in APPORTIONED], P('לכל', 'העמים', 'תחת', 'כל', 'השמים')))
        move('Sifrei Devarim 148:8 (the reading); Avodah Zarah 55a:9-10; Megillah 9b:1', "4:19 with 29:25 — not given to the nations for worship; Rav: He let them slip into their delusion; the Septuagint's 'to give light'")
        dat('the row the_host_apportioned: a DATA note, no link of our own (Onkelos "prepared")')
        return out("the host apportioned (4:19) — with 29:25 by the Sifrei 148:8's pair; Rav's reading (Avodah Zarah 55a): a DATA note, no link of our own", ['accepted'])
    if ask == 'the_iron_furnace':
        ink('4:20', '"but you the LORD took and brought out of the iron furnace, out of Egypt, to be a people of inheritance to him as this day" — the furnace-word\'s seats %s (1 Kings 8:51 and Jeremiah 11:4 the kin); "a people of inheritance" %s; "the LORD took you" %s' % (FURNACE, P('לעם', 'נחלה'), P('ואתכם', 'לקח', 'יהוה')))
        move('cold_run_primeval (CALL) — PR.pieces(furnace) = %s' % (PR_FURNACE['v'],), "Genesis 15:17's smoking furnace another word; Bereshit Rabbah 44:13's furnace of fire at 15:7 — the furnace's first seat in the fathers' story")
        dat("the readback row 4:20 EXPANDED — brought_out (Exod 12:51) found")
        return out("the iron furnace (4:20) — the exodus READ BACK, EXPANDED: the furnace told only here in the Torah (1 Kings 8:51 outside; PR by CALL)", ['accepted'])
    if ask == 'the_bar_third_telling':
        ink('4:21-22', '"and the LORD was angry with me on your account, and swore that I should not cross the Jordan nor come into the good land … for I die in this land" — "was angry with me" %s; the anger-root\'s four Torah seats %s; "on your account" %s; "and swore that I should not cross" %s; "for I die" %s' % (P('התאנף', 'בי'), ANGRY, P('על', 'דבריכם'), P('וישבע', 'לבלתי', 'עברי'), P('כי', 'אנכי', 'מת')))
        move('cold_run_opening_speech (CALL) — OS.the_spies_read_back(the_bars_ground) = %s; OS.the_plea(the_refusal) = %s' % (OS_BAR[0][:70], OS_REFUSAL[0][:60]), "1:37's 'for your sakes' and 3:26's 'was wroth for your sakes' — the 1b DISAGREES row; the refusal 'let it suffice you'")
        dat('the row the_bars_third_telling: %s — the OATH the tape never wrote; the 1b row WIDENED, OPEN; barred_from_the_land on Moses unmoved' % data['the_bars_third_telling']['value'])
        return out("the bar's third telling (4:21-22) — 'on your account' and an oath against Numbers 20:12's 'because you did not believe': DISAGREES, the 1b row widened, an OPEN row; no oath written", ['accepted'])
    if ask == 'the_covenant_not_forgotten':
        ink('4:23', '"take heed to yourselves lest you forget the covenant of the LORD your God which he cut with you, and make a graven image" — %s; "which he cut with you" %s; the second word\'s kin' % (P('פן', 'תשכחו', 'את', 'ברית'), P('אשר', 'כרת', 'עמכם')))
        return out("the covenant not forgotten (4:23) — the guard's second seat: the covenant cut at Horeb (the tape's covenant_blood_thrown) and the image", ['accepted'])
    if ask == 'consuming_fire_jealous_god':
        ink('4:24', '"for the LORD your God is a consuming fire, a jealous God" — "a consuming fire" %s; "a jealous God" %s (Exodus 20:5\'s word); the verse %d tokens' % (P('אש', 'אכלה'), P('אל', 'קנא'), len(W4(24))))
        move('Sifrei Devarim 49:2 (the reading); Ketubot 111b:6; Sotah 14a:3', "how cleave to a consuming fire? — the sages; walk after His attributes")
        move('Avodah Zarah 54b:18, 55a:2-3; Nedarim 62b:3', "the philosopher's and Agrippas's questions to Rabban Gamliel — jealousy at the worshipper, not the idol (the dog named after the king; the second wife)")
        return out("a consuming fire, a jealous God (4:24) — the second word's 'jealous' (Exodus 20:5 by reference); jealousy at the worshipper, not the idol (Avodah Zarah 54b-55a)", ['accepted'])
    return out('no verdict in span', [FX.NONE])


# ===== F4: THE EXILE CASE (Deut 4:25-31) ====================================================================
def the_exile_case(case, data):
    del P_[:]
    ask = case['ask']
    if ask == 'the_case_head':
        ink('4:25', '"WHEN you beget sons and sons\' sons and have grown old in the land and deal corruptly and make a graven image … and do evil in the eyes of the LORD your God to provoke him" — the case token %s with the imperfect; "when you beget sons" %s; "grown old" %s one seat; "evil in the eyes of the LORD" five Torah seats' % (CASE_TOK['4:25'], P('כי', 'תוליד', 'בנים'), U('ונושנתם')))
        move('Gittin 88a:15-17; Sanhedrin 38a:6; Megillah 31b:2', "'grown old' by its letters eight hundred and fifty-two — the exile hastened by two years; seven dynasties counted from 'you will beget' (one) and 'children' said thrice (two each); the Ninth of Av's reading")
        dat('the row the_exile_case: %s' % data['the_exile_case']['value'])
        return out("the case head (4:25) — THE CHAPTER'S ONE CASE: 'when' with the imperfect; the arms DATA; the exile hastened by two years (Gittin 88a)", ['accepted'])
    if ask == 'the_witnesses':
        ink('4:26', '"I call heaven and earth to witness against you this day" — "I call to witness" %s; "heaven and earth" summoned in the book at %s; 30:19\'s first seven words identical' % (WITNESS_CALL, HEAVEN_EARTH_D))
        move('Sifrei Devarim 306:1 (the reading)', "the chain of witnesses — 4:26 the third of eleven; 31:28 and 32:1 forward")
        dat('the row the_witnesses_chain: %s — the write heaven_and_earth_witness on Israel' % data['the_witnesses_chain']['value'])
        return out("the witnesses (4:26) — heaven and earth called: a STATUS on Israel (the Sifrei 306:1's chain, the third of eleven)", ['heaven_and_earth_witness'])
    if ask == 'perish_and_scatter':
        ink('4:26-27', '"you shall surely perish quickly … you shall not prolong days upon it but be utterly destroyed; and the LORD will scatter you among the peoples and you shall be left few in number" — "surely perish" %s; "not prolong days" %s; "scatter you among the peoples" %s; "few in number" %s' % (P('אבד', 'תאבדון'), P('לא', 'תאריכן', 'ימים'), P('והפיץ', 'יהוה', 'אתכם', 'בעמים'), P('מתי', 'מספר')))
        move('cold_run_tochacha (CALL) — TC.NOT_BROKEN = %s' % (TC_NOT_BROKEN['v'],), "Leviticus 26:33's scattering the first telling (scattered_among_nations); 28:64 forward; the covenant survives the transfer")
        dat("no exile on the tape — no entry written; the arm DATA")
        return out("perish and scatter (4:26-27) — the case's first arm: Leviticus 26:33's scattering by CALL (TC), no entry written", ['accepted'])
    if ask == 'serve_wood_and_stone':
        ink('4:28', '"and there you shall serve gods the work of men\'s hands, wood and stone, which neither see nor hear nor eat nor smell" — "the work of men\'s hands, wood and stone" %s; "wood and stone" seven seats; "neither see nor hear" %s' % (P('מעשה', 'ידי', 'אדם', 'עץ', 'ואבן'), P('לא', 'יראון', 'ולא', 'ישמעון')))
        return out("serve wood and stone (4:28) — 28:36 and 28:64 forward; Psalm 115:5 the kin", ['accepted'])
    if ask == 'seek_and_find':
        ink('4:29', '"and you will seek the LORD your God from there and find him, if you seek him with all your heart and all your soul" — "seek from there" %s; "with all your heart and all your soul" %s (6:5 the Shema\'s); "and find" %s' % (P('ובקשתם', 'משם'), HEART_SOUL, U('ומצאת')))
        return out("seek and find (4:29) — the case's second arm: the Shema's words (6:5 forward); 30:10's kin", ['accepted'])
    if ask == 'in_your_distress_return':
        ink('4:30', '"in your distress, when all these things find you, in the end of days, you will return to the LORD your God and hearken to his voice" — "in your distress" %s; "in the end of days" the Torah\'s four seats %s; "return to the LORD your God" %s; "hearken to his voice" %s' % (P('בצר', 'לך'), END_OF_DAYS, P('ושבת', 'עד', 'יהוה', 'אלהיך'), P('ושמעת', 'בקלו')))
        move('cold_run_tochacha (CALL) — TC.recovery(True, True) = %s' % (TC_RECOVERY['v'],), "confession and the humbled heart — covenant_remembered (Leviticus 26:40-42)")
        dat("'in the end of days' a PROPHECY — no timer, no clock item")
        return out("in your distress, return (4:30) — the case's third arm: 30:2's kin; 'the end of days' a prophecy, no timer (TC by CALL)", ['accepted'])
    if ask == 'the_merciful_god':
        ink('4:31', '"for the LORD your God is a merciful God: he will not fail you nor destroy you nor forget the covenant of your fathers which he swore to them" — "a merciful God" %s (Exodus 34:6\'s attribute); "not fail you" %s; "the covenant of your fathers" %s; "which he swore to them" %s' % (P('אל', 'רחום'), U('ירפך'), P('ברית', 'אבתיך'), P('אשר', 'נשבע', 'להם')))
        return out("the merciful God (4:31) — Exodus 34:6's attribute; the fathers' covenant sworn (Genesis 22:16, 26:3 by reference); Leviticus 26:42 the first telling", ['accepted'])
    return out('no verdict in span', [FX.NONE])


# ===== F5: THE ONE GOD (Deut 4:32-40) =======================================================================
def the_one_god(case, data):
    del P_[:]
    ask = case['ask']
    if ask == 'the_former_days':
        ink('4:32', '"ask now of the former days which were before you, since the day God created man upon the earth, from one end of heaven to the other" — "ask now of the days" %s; "former" the adjective (%s); "God created man" %s — the create-verb\'s eleven Torah seats %s, the book\'s one' % (P('שאל', 'נא', 'לימים'), lemma_of('Deut', 4, 32, 'ראשנים'), P('אשר', 'ברא', 'אלהים', 'אדם'), CREATED))
        move('cold_run_pre_sinai (CALL) — PS.creation(created_made) = %s' % (PS_CREATED['v'],), "'created' six, 'made' ten in the creation chapter — Genesis 1:27's man; the sixth day's marker on the tape")
        move('Chagigah 11b:21-24; Tosefta Chagigah 2:3; Chagigah 12a:2; Sanhedrin 38b:7', "one may inquire of creation, not two; within the world's bounds; Adam's height from one end to the other")
        dat('the row the_inquiry_limits: %s; the readback row 4:32 SHORTENED — the sixth day (Gen 1:31) found' % data['the_inquiry_limits']['value'])
        return out("the former days (4:32) — the creation READ BACK as a time-reference (PS by CALL); the limits of inquiry (Chagigah 11b)", ['accepted'])
    if ask == 'the_voice_and_lived':
        ink('4:33', '"did a people ever hear the voice of God speaking from the midst of the fire as you heard, and live?" — %s; "and live" the consecutive perfect at 4:33 and 5:26 alone in the book' % (P('השמע', 'עם', 'קול', 'אלהים'),))
        return out("the voice and lived (4:33) — 5:26's kin; the assembly's lord_descended by reference", ['accepted'])
    if ask == 'the_nation_from_a_nation':
        ink('4:34', '"or has a god tried to come and take him a nation from the midst of a nation, by trials, by signs, by wonders, by war, by a mighty hand, by an outstretched arm and by great terrors" — "has a god tried" %s; "a nation from the midst of a nation" %s; "the mighty hand" %d seats; "the outstretched arm" %s; the arm PLENE here, defective at 26:8' % (P('הנסה', 'אלהים'), P('גוי', 'מקרב', 'גוי'), len(STRONG_HAND), OUTSTRETCHED))
        move('cold_run_exodus_story (CALL) — ES.plagues(ten) = %s; ES.sea(ten_at_sea) = %s; ES.night(sent_formula) = %s' % (ES_TEN['v'], ES_SEA['v'], ES_SENT['v']), "the ten plagues, the ten miracles at the sea, the sending — the instruments' first tellings")
        move('Mishnah Pesachim 10:4; Sifrei Devarim 301:21 (the reading); Berakhot 6a:24; Megillah 11a:9', "the Haggadah's exposition from 'a wandering Aramean' — 26:8's 'great terror' glossed by 4:34's; the tefillin's compartments; Esther's introduction")
        dat('the row the_instruments: %s' % data['the_instruments']['value']['deut_4_34'])
        return out("a nation from the midst of a nation (4:34) — the seven instruments: the exodus READ BACK, EXPANDED (ES by CALL); the Haggadah's row (Pesachim 10:4)", ['accepted'])
    if ask == 'you_were_shown':
        ink('4:35', '"you were shown, to know that the LORD, he is God; there is none else beside him" — %s; "the LORD, he is God" %s; "none else" %s; "beside him" %s one seat; the hophal %s against 4:3\'s participle' % (P('אתה', 'הראת', 'לדעת'), CREED, NONE_ELSE, U('מלבדו'), morphs('Deut', 4, 35)[1]))
        move('Chullin 7b:14; Sanhedrin 67b:7; Rosh Hashanah 32b:17', "'none else' — even sorcery (R. Chanina); a verse of kingship (R. Yosei) or not (R. Yehuda)")
        dat('the row the_creed: %s' % data['the_creed']['value'])
        return out("you were shown (4:35) — the creed's first seat: 'none else beside him' (even sorcery — Chullin 7b); the kingship verses disputed", ['accepted'])
    if ask == 'from_heaven_the_voice':
        ink('4:36', '"from heaven he made you hear his voice to instruct you, and on earth he showed you his great fire, and his words you heard from the midst of the fire" — %s; "to instruct you" %s; "his great fire" %s; Exodus 20:22\'s "from heaven I spoke with you" %s' % (P('מן', 'השמים', 'השמיעך'), U('ליסרך'), P('אשו', 'הגדולה'), words('Exod', 20, 22)[-5:]))
        move('cold_run_decalogue (CALL) — DC.altar_rules(steps) = %s' % (DC_STEPS[0][:50],), "the altar rule's seat (20:22-26) — 'from heaven I spoke with you' the first telling; the Mekhilta's question credited by name")
        return out("from heaven the voice (4:36) — Exodus 20:22 READ BACK (DC by CALL for the seat; the Mekhilta credited by name)", ['accepted'])
    if ask == 'because_he_loved_your_fathers':
        ink('4:37', '"and because he loved your fathers he chose their seed after them and brought you out with his presence, with his great power, out of Egypt" — "because he loved" %s; "their seed after them" %s; "with his presence" %s (Onkelos "with his Memra"); "with his great power" %s' % (P('ותחת', 'כי', 'אהב'), P('ויבחר', 'בזרעו', 'אחריו'), U('בפניו'), P('בכחו', 'הגדל')))
        move('cold_run_primeval (CALL) — PR.call(land_seats) = %s' % (PR_LAND['v'],), "Genesis 15:18's land granted — the covenant's phrase 'your seed after you' at eight seats")
        dat("the readback row 4:37-38 EXPANDED — brought_out (Exod 12:51) found; land_granted since 15:18")
        return out("because he loved your fathers (4:37) — the choice of the seed (Genesis 17's phrase; PR by CALL); the outbringing READ BACK", ['accepted'])
    if ask == 'to_dispossess_nations':
        ink('4:38', '"to dispossess nations greater and mightier than you from before you, to bring you in, to give you their land for an inheritance as this day" — %s (9:1 the kin); "to bring you in" %s; Numbers 33:52\'s "you shall dispossess" the debit\'s spec' % (P('גוים', 'גדלים', 'ועצמים', 'ממך'), U('להביאך')))
        dat("the dispossess debit on israel_people (Num 33:50-56) OPEN — READ, not rewritten (CC6)")
        return out("to dispossess nations (4:38) — the open dispossess debit of Numbers 33:50-56 READ; 9:1 the kin", ['accepted'])
    if ask == 'know_this_day':
        ink('4:39', '"know this day and lay it to your heart that the LORD, he is God in heaven above and on the earth beneath; there is none else" — %s; "in heaven above and on the earth beneath" %s (Rahab\'s and Solomon\'s); "in heaven above" %s' % (P('וידעת', 'היום', 'והשבת', 'אל', 'לבבך'), P('בשמים', 'ממעל', 'ועל', 'הארץ', 'מתחת'), P('בשמים', 'ממעל')))
        move('Rosh Hashanah 32b:17; Gittin 57b:17', "a verse of kingship (R. Yosei); the seventh son's creed")
        return out("know this day (4:39) — the creed's second seat: Rahab's and Solomon's words outside the Torah; the seventh son's (Gittin 57b)", ['accepted'])
    if ask == 'keep_the_statutes':
        ink('4:40', '"and you shall keep his statutes and his commandments which I command you this day, that it may go well with you and with your sons after you, and that you may prolong days upon the land" — "that it may go well with you" %s; "prolong days upon the land" %s; "upon the land which the LORD your God gives you" %s (5:16 the pair)' % (P('אשר', 'ייטב', 'לך'), P('תאריך', 'ימים', 'על', 'האדמה'), P('על', 'האדמה', 'אשר', 'יהוה', 'אלהיך', 'נתן', 'לך')))
        return out("keep the statutes (4:40) — the reward clause: well with you, prolonged days (5:16's pair forward)", ['accepted'])
    return out('no verdict in span', [FX.NONE])


# ===== F6: THE CITIES AND THE FRAME (Deut 4:41-49) ==========================================================
def the_cities_and_the_frame(case, data):
    del P_[:]
    ask = case['ask']
    if ask == 'then_moses_set_apart':
        ink('4:41', '"THEN Moses set apart three cities beyond the Jordan toward the sunrise" — "then" with the imperfect at %s (the Song\'s form); the set-apart root\'s seats in the book %s; "three cities" %s; "beyond the Jordan toward the sunrise" %s; the parser [%d]' % (THEN_IMPF, SET_APART, P('שלש', 'ערים'), P('בעבר', 'הירדן', 'מזרחה', 'שמש'), THREE_CITIES_N))
        move('Makkot 10a:15-16', "R. Simlai: shine the sun for murderers; Moses knew the three would admit no one until Joshua's three — 'a mitzva that came my way, I will fulfill it'")
        dat("cities_set_apart on israel_people — a STATUS valued the three; the refuge debit READ OPEN")
        return out("then Moses set apart (4:41) — Moses' own act in the third person: cities_set_apart on Israel (the Song's 'then' form; R. Simlai's mitzva that came his way)", ['cities_set_apart'])
    if ask == 'not_until_all_six':
        ink('4:41; Num 35:13-14', '"three cities" here against Numbers 35:14\'s "the three cities … and the three cities": "six cities of refuge shall they be" (35:13, [6]); the parser on 35:14 %s' % (ink_numbers(verse_words('Num', 35, 14)),))
        move('cold_run_refuge (CALL) — RF.the_refuge_law(six_cities) = %s; RF.the_refuge_law(the_debit) = %s' % (RF_SIX[0][:70], RF_DEBIT[0][:70]), "the six's DATA row; the debit appoint_six_cities_of_refuge OPEN by design")
        move('Mishnah Makkot 2:4; Makkot 9b:14', "until the three in the land of Canaan were selected, the three beyond the Jordan did not admit — THE ANSWER SHEET'S ROW THAT KEEPS THE DEBIT OPEN")
        dat('the row the_three_cities: %s — THE DEBIT LEFT OPEN (the design\'s (d)); Joshua 20:7-8 the close outside the Torah' % data['the_three_cities']['value'])
        return out("not until all six (Makkot 2:4) — the three east admitted no one: the refuge debit on Israel READ OPEN and left open (RF by CALL); the manslayer's refuge exempt until Joshua's three", ['exempt'])
    if ask == 'the_manslayer_defined':
        ink('4:42', '"that the manslayer might flee there, who slays his neighbor unawares and hated him not in time past, and that fleeing to one of these cities he might live" — 4:42 = 19:4\'s words with "slays" for "smites" (the diff %s; the shared run %s); "unawares" %s; "hated him not" %s; the manslayer-word\'s %d seats, %d in Numbers 35; PLENE here %s' % (MANSLAYER_DIFF[2:4], MANSLAYER_SHARED, NO_KNOWLEDGE, NOT_HIS_ENEMY, len(MANSLAYER), len([s for s in MANSLAYER if s.startswith('Num 35')]), PT('Deut', 4, 42, 'רוצח')))
        move('cold_run_refuge (CALL) — RF.the_manslayer(not_his_enemy) = %s; RF.the_manslayer(without_seeing) = %s' % (RF_ENEMY[0][:60], RF_BLIND[0][:60]), "the enemy not exiled (Mishnah Makkot 2:3); 'without seeing' / 'without knowledge' the blind (Makkot 9b:5-8)")
        move('Makkot 10a:9-11; Gittin 12a:11; Sotah 49a:4', "'and live' — the teacher exiled with his school; the slave's surplus; the quarreling scholars")
        dat('the row the_manslayer_definition: %s' % data['the_manslayer_definition']['value'])
        return out("the manslayer defined (4:42) — 19:4's words with 'slays' for 'smites' (computed); the refuge runner's clauses by CALL; 'and live' the teacher exiled with his school (Makkot 10a)", ['accepted'])
    if ask == 'the_three_names':
        ink('4:43', '"Bezer in the wilderness in the plain for the Reubenites, Ramoth in Gilead for the Gadites, Golan in Bashan for the Manassites" — Golan\'s seats %s (Joshua 20:8 "Gaulon" without the vav; %s here); "in the plain" %s; the shared run with Joshua 20:8 %s' % (GOLAN, W4(43)[11], U('המישר', books=T), SHARED(('Deut', 4, 43), ('Josh', 20, 8))))
        move('cold_run_refuge (CALL) — RF.DATA[the_six_cities] = %s' % (RF.DATA['the_six_cities']['value']['beyond_the_jordan'],), "the names outside Numbers 35, computed by seat")
        move('Makkot 9b:18-10a:3, 10a:14; Avodah Zarah 58b:8', "two rows of vines — Hebron against Bezer, Shechem against Ramoth, Kadesh against Golan; Gilead's murderers; Reuben first; Bezer not Bozrah")
        return out("the three names (4:43) — Bezer, Ramoth, Golan (RF's row by CALL); the two rows of vines (Makkot 9b:18); Joshua 20:8's Gaulon", ['accepted'])
    if ask == 'the_second_frame':
        ink('4:44-45', '"and this is the Torah which Moses set before the children of Israel; these are the testimonies, the statutes and the judgments which Moses spoke to the children of Israel when they came out of Egypt" — "and this is the Torah" %s; "which Moses set before" %s; "these are the testimonies" %s; "which Moses spoke" %s (1:1 the other); the shared run with 1:1 %s; "when they came out of Egypt" %s' % (P('וזאת', 'התורה'), P('אשר', 'שם', 'משה', 'לפני'), P('אלה', 'העדת'), P('אשר', 'דבר', 'משה'), SHARED(('Deut', 4, 45), ('Deut', 1, 1)), P('בצאתם', 'ממצרים')))
        move('cold_run_opening_speech (CALL) — OS.the_frame(after_sihon) = %s' % (OS_AFTER[0][:60],), "the first frame's order — after Sihon (1:4); torah_expounded on Israel at (40, 11, 1) the book's one act of its own day")
        move('Sifrei Devarim 323:1 (the reading); Yoma 72b:14; Makkot 10a:11; Avodah Zarah 2b:6', "'this' is nothing but Torah; a drug of life or death; Torah provides refuge — the cities juxtaposed to the frame; the nations' plea")
        dat('the row the_second_frame: %s — NO WRITE (R6); the footer 4:45 closes the block (Deut 1:1, Deut 4:45] with two daemons' % data['the_second_frame']['value'])
        return out("the second frame (4:44-45) — the second speech's head: a stamp of place and era, NO WRITE (R6); EXPANDED against 1:1-5 (OS by CALL)", ['accepted'])
    if ask == 'the_borders_verbatim':
        ink('4:46-49', '"beyond the Jordan in the valley over against Beth-peor, in the land of Sihon … whom Moses and the children of Israel smote … from Aroer on the bank of the brook Arnon to Mount Sion which is Hermon … to the sea of the Arabah under the slopes of Pisgah" — the shared runs with 1:4, 3:8, 2:36, 3:17: %s; "Mount Sion" %s one seat (Sirion %s, Senir %s the other names); "the sea of the Arabah" %s; "under the slopes of Pisgah" %s' % (BORDERS_DELTA, U('שיאן'), U('שרין', 'שריון'), U('שניר', 'ושניר'), P('ים', 'הערבה'), P('אשדת', 'הפסגה')))
        move('cold_run_chukat (CALL) — CK.well_and_kings(deut3_delta) = %s; cold_run_borders (CALL) — BO.the_four_sides(the_promised_extents) = %s; cold_run_opening_speech (CALL) — OS.sihon_and_og(hermon) = %s; cold_run_balak (CALL) — BK.the_call(last_camp) = %s' % (CK_DELTA[0][:50], BO_EXTENTS[0][:50], OS_HERMON[0][:50], BK_LAST[0][:50]), "the two kings' lines; the east's extents; Hermon's names; the valley opposite Beth-peor the last camp")
        dat("the readback row 4:46-49 SHORTENED — sihon_smitten_land_possessed (Num 21:24) found; the speech's own borders quoted verbatim")
        return out("the borders verbatim (4:46-49) — the retelling of a retelling: the speech's own 1:4, 3:8, 2:36, 3:17 in their own clauses (computed); Mount Sion the fourth name (CK, BO, OS, BK by CALL)", ['accepted'])
    if ask == 'the_readback_table':
        ink('4:3-49', 'the readback table — %d rows: %s' % (len(data['the_readback']['value']), dict(RB_GRADES)))
        dat("every retold act's entry found on the running world (CC4); the two SUPPLIED rows the tape's hole; the DISAGREES row 4:21-22 OPEN")
        return out("the readback table — eleven reference rows graded; the two supplied lines the tape's hole; the one disagreement widened, open (CC4)", ['accepted'])
    return out('no verdict in span', [FX.NONE])

# ---- THE CALLEES' FACTS (every edge live at the cells that consume them; the values asserted from the callees' own prints) ----
BK_PLAGUE = BK.peor({'ask': 'plague_count'}, BK.DATA); BK_SERVICE = BK.peor({'ask': 'peor_service'}, BK.DATA); BK_LAST = BK.the_call({'ask': 'last_camp'}, BK.DATA)
RF_SIX = RF.the_refuge_law({'ask': 'six_cities'}, RF.DATA); RF_DEBIT = RF.the_refuge_law({'ask': 'the_debit'}, RF.DATA); RF_ENEMY = RF.the_manslayer({'ask': 'not_his_enemy'}, RF.DATA); RF_BLIND = RF.the_manslayer({'ask': 'without_seeing'}, RF.DATA)
OS_BAR = OS.the_spies_read_back({'ask': 'the_bars_ground'}, OS.DATA); OS_REFUSAL = OS.the_plea({'ask': 'the_refusal'}, OS.DATA); OS_HERMON = OS.sihon_and_og({'ask': 'hermon'}, OS.DATA); OS_AFTER = OS.the_frame({'ask': 'after_sihon'}, OS.DATA); OS_ROWS = OS.READBACK
ER_TEN = ER.tablets('ten_words'); ER_TAMMUZ = ER.ascent('seventeenth_tammuz'); ER_FORMS = ER.tablets('finger_and_forms'); ER_TORAH_MITZVAH = ER.ascent('torah_mitzvah'); ER_HOREB = ER.presence('horev_plene')
ES_DAYS = ES.sinai('days_r_yose'); ES_DESC = ES.sinai('descents'); ES_TEN = ES.plagues('ten'); ES_SEA = ES.sea('ten_at_sea'); ES_SENT = ES.night('sent_formula')
TC_RECOVERY = TC.recovery(True, True); TC_NOT_BROKEN = TC.NOT_BROKEN
PS_CREATED = PS.creation('created_made')
PR_FURNACE = PR.pieces('furnace'); PR_LAND = PR.call('land_seats')
DC_STEPS = DC.altar_rules({'ask': 'steps'}, DC.DATA)
CK_DELTA = CK.well_and_kings({'ask': 'deut3_delta'}, CK.DATA)
BO_EXTENTS = BO.the_four_sides({'ask': 'the_promised_extents'}, BO.DATA)
assert ER_TEN['v'] == 3 and ER_TAMMUZ['v'] == '17_tammuz' and ER_HOREB['v'] == 1 and ER_TORAH_MITZVAH['v'] == 2 and ER_FORMS['v']['לוחת'] == 3 and ER_FORMS['v']['לחת'] == 12, (ER_TEN['v'], ER_TAMMUZ['v'], ER_HOREB['v'], ER_TORAH_MITZVAH['v'], ER_FORMS['v'])   # 'the ten words' three seats; the seventeenth of Tammuz; Horeb plene once; 24:12's pair; the tablets' forms
assert ES_DAYS['v'] == (2, 3, 4, 7) and ES_DESC['v'] == 'one_of_ten' and ES_TEN['v'] == 10 and ES_SEA['v'] == 10 and ES_SENT['v'] == 'the_mouth_that_said_i_will_not_send', (ES_DAYS['v'], ES_DESC['v'], ES_TEN['v'], ES_SEA['v'], ES_SENT['v'])   # Rabbi Yose's days — the giving on the seventh; the ten plagues, the ten at the sea
assert PS_CREATED['v'] == (6, 10) and PR_FURNACE['v'] == ('michael', 'the_holy_one_himself') and TC_RECOVERY['v'] == 'covenant_remembered' and TC_NOT_BROKEN['v'] == 'never_broken' and len(OS_ROWS) == 42, (PS_CREATED['v'], PR_FURNACE['v'], TC_RECOVERY['v'], TC_NOT_BROKEN['v'], len(OS_ROWS))
assert RF_SIX[0].startswith('six cities (35:13-15)') and RF_DEBIT[0].startswith('the debit (35:11-14)') and OS_BAR[0].startswith("the bar's ground (1:37)") and DC_STEPS[0].startswith('a ramp') and RF.DATA['the_six_cities']['value']['beyond_the_jordan'] == ['Bezer (Reuben)', 'Ramoth in Gilead (Gad)', 'Golan in Bashan (Manasseh)'], (RF_SIX[0][:60], RF_DEBIT[0][:60], OS_BAR[0][:60], DC_STEPS[0][:40])
assert [r['verses'] for r in OS_ROWS if r['grade'] == 'DISAGREES'] == ['Deut 1:37', 'Deut 2:29'], 'the 1b DISAGREES rows this chapter\'s 4:21-22 joins'


# ===== THE WRAP (D9-iv): the daemon over the cells — the ledger written, no event emitted =====================
def law_obey_horeb(event, world):
    """Deut 4:1-49 (cold_run_obey_horeb.py F1-F6). given_at Deut 4:2; installed_by boot — A LAW IN MOSES' VOICE WITH NO DIVINE FRAME ('the word
    which I command you', 4:2 — the vows' class; the second pass's D2 question). FIVE TAPE LINES: the exhortation with the one law (a BLOCK on
    Israel — adding_barred; the receipt 4:5 in the line's source), the two SUPPLIED Horeb lines (the tape's hole — covenant_declared on Israel dated
    (1, 3, 7); tablets_delivered on Moses dated (1, 4, 17)), the witnesses called (a STATUS on Israel — the one case's evidence), the three cities set
    apart (a STATUS on Israel — the refuge debit READ OPEN, not closed). The exam's case kind dispatches to the cells in EXPLICIT branches with
    LITERAL effects per kind (an unnamed effect is a KeyError). No close, no timer."""
    k, src = event['kind'], event['case_source']
    E_ = lambda eff, s, cp=None, amount=None, due=None, law='', value=None: {'effect': eff, 'subject': s, 'counterparty': cp, 'amount': amount, 'due': due, 'value': value if value is not None else True, 'source_law': law, 'case_source': src}
    if k == 'add_nothing_commanded':
        return [E_('adding_barred', 'israel', value='you shall not add to the word which I command you, nor diminish from it (4:2) — in its time without intent, out of its time with intent (Rosh Hashanah 28b:24); an addition that spoils (Sanhedrin 89a:2); 13:1 the second seat', law='F1 [INK 4:2 "you shall not add to the word which I command you, nor diminish from it" — THE CHAPTER\'S ONE LAW: a BLOCK on Israel; the line 4:1-8 holds the receipt "as the LORD my God commanded me" (4:5) — the register seat ACT, the teaching\'s run of Exodus 24:12\'s command (ER by CALL); the exam\'s rows Rosh Hashanah 28b, Eruvin 95b-96a, Sanhedrin 88b-89a]')]
    if k == 'ten_words_declared':
        return [E_('covenant_declared', 'israel', value={'the_ten_words': 'his covenant which he commanded you to do, the ten words (4:13) — Exodus 20:1-17 the first telling', 'dated': (1, 3, 7), 'the_hole': 'no line on the tape for Exodus 20:1 until this one (the readback\'s finding)'}, law='F2 [INK 4:12-13 "the LORD spoke to you from the midst of the fire: a voice of words you heard, but no form … and he declared to you his covenant, the ten words" — TOLD HERE with no line on the tape (Exodus 20:1 the first telling; the tape runs from 19:20 to 24:1): written ONCE at its own time, dated (1, 3, 7) by the retrograde marker at 4:10 — the giving\'s day by Rabbi Yose (ES.sinai by CALL); the ten words three seats (ER by CALL)]')]
    if k == 'tablets_given':
        return [E_('tablets_delivered', 'moses', value='two tablets of stone written with the finger of God (Exodus 31:18; Deuteronomy 4:13 — the tablets plene) — given at the fortieth day of the ascent and broken the same day (Taanit 28b:9)', law='F2 [INK 4:13 "and he wrote them on two tablets of stone" — Exodus 31:18\'s giving TOLD HERE with no line on the tape (the erection runner folded the tablets into the ascent\'s line): written ONCE at its own time, dated (1, 4, 17) by the retrograde marker at 4:13 — the seventh of Sivan plus forty (ER.ascent by CALL); the erection\'s effect at its first tape seat]')]
    if k == 'witnesses_called':
        return [E_('heaven_and_earth_witness', 'israel', value='I call heaven and earth to witness against you this day (4:26) — the exile case\'s witnesses: corrupt → perish, scatter, few, serve wood and stone; seek → find; return → mercy; the end of days a prophecy, no timer', law='F4 [INK 4:25-31 "when you beget sons … I call heaven and earth to witness against you this day" — THE CHAPTER\'S ONE CASE: a STATUS on Israel, the Sifrei 306:1\'s chain (the third of eleven; 30:19, 31:28 forward); the arms DATA — Leviticus 26:33 and 26:42 the first tellings (TC by CALL), no exile written; Gittin 88a the exile hastened]')]
    if k == 'three_cities_set_apart':
        return [E_('cities_set_apart', 'israel', value=['Bezer (Reuben)', 'Ramoth in Gilead (Gad)', 'Golan in Bashan (Manasseh)'], law='F6 [INK 4:41-43 "then Moses set apart three cities beyond the Jordan toward the sunrise … Bezer … Ramoth … Golan" — Moses\' own ACT in the third person: a STATUS on Israel valued the three (RF.DATA the_six_cities by CALL); THE REFUGE DEBIT appoint_six_cities_of_refuge READ OPEN AND NOT CLOSED — Mishnah Makkot 2:4: the three east admitted no one until Joshua\'s three, "six cities of refuge shall they be" (35:13); Makkot 10a:15-16 R. Simlai; Joshua 20:7-8 the close outside the Torah]')]
    if k == 'horeb_case':
        fn = {'exhortation': the_exhortation, 'horeb': horeb_retold, 'image': no_image, 'exile': the_exile_case, 'god': the_one_god, 'cities': the_cities_and_the_frame}[event['cell']]
        v, e, _ = fn({'ask': event['ask']}, DATA); L = '%s [%s]' % ({'exhortation': 'F1', 'horeb': 'F2', 'image': 'F3', 'exile': 'F4', 'god': 'F5', 'cities': 'F6'}[event['cell']], event['ask']); s_ = event['person']
        W = {'accepted': E_('accepted', s_, value=v, law=L), 'exempt': E_('exempt', s_, value=v, law=L)}
        return [W[x] for x in e if x != FX.NONE]
    return []


LINES = [
    ('Deut 4:1-8 — and now, Israel, hear the statutes and the judgments which I teach you, to do them, that you may live and go in and possess the land which the LORD, the God of your fathers, gives you; you shall not add to the word which I command you, nor diminish from it, to keep the commandments of the LORD your God which I command you; your eyes have seen what the LORD did at Baal-peor, for every man who followed Baal-peor the LORD your God destroyed from your midst; but you who cleave to the LORD your God are alive, all of you, this day; behold, I have taught you statutes and judgments, as the LORD my God commanded me, to do so in the midst of the land which you go in to possess; keep them and do them, for this is your wisdom and your understanding in the eyes of the peoples, who will hear all these statutes and say: surely this great nation is a wise and understanding people; for what great nation has God so near to it as the LORD our God is whenever we call upon him; and what great nation has statutes and judgments so righteous as all this Torah which I set before you this day',),
    ('Deut 4:10-13 — the day you stood before the LORD your God at Horeb, when the LORD said to me: assemble the people to me, and I will make them hear my words, that they may learn to fear me all the days they live on the earth, and that they may teach their sons; and you came near and stood under the mountain, and the mountain burned with fire to the heart of heaven, darkness, cloud and thick darkness; and the LORD spoke to you from the midst of the fire: a voice of words you heard, but no form, only a voice; and he declared to you his covenant which he commanded you to do, the ten words, and he wrote them on two tablets of stone',),
    ('Deut 4:13 — and he wrote them on two tablets of stone (Exodus 31:18 — and He gave to Moses, when He finished speaking with him on Mount Sinai, two tablets of the testimony, tablets of stone written with the finger of God)',),
    ('Deut 4:25-31 — when you beget sons and sons\' sons and have grown old in the land and deal corruptly and make a graven image, the form of anything, and do evil in the eyes of the LORD your God to provoke him: I call heaven and earth to witness against you this day that you shall surely perish quickly from the land which you cross the Jordan to possess; you shall not prolong your days upon it but shall be utterly destroyed; and the LORD will scatter you among the peoples and you shall be left few in number among the nations where the LORD will lead you; and there you shall serve gods the work of men\'s hands, wood and stone, which neither see nor hear nor eat nor smell; and from there you will seek the LORD your God and find him, if you seek him with all your heart and all your soul; in your distress, when all these things find you in the end of days, you will return to the LORD your God and hearken to his voice; for the LORD your God is a merciful God: he will not fail you nor destroy you nor forget the covenant of your fathers which he swore to them',),
    ('Deut 4:41-43 — then Moses set apart three cities beyond the Jordan toward the sunrise, that the manslayer might flee there, who slays his neighbor unawares and hated him not in time past, and that fleeing to one of these cities he might live: Bezer in the wilderness in the plain for the Reubenites, and Ramoth in Gilead for the Gadites, and Golan in Bashan for the Manassites',),
]
CLOSES = 'none — the refuge debit appoint_six_cities_of_refuge stays OPEN (Mishnah Makkot 2:4: not until all six; Joshua 20:7-8 the close outside the Torah); no oath written at 4:21 (the sentence read back); the second frame no write'

PERSONS = [
    ('the-priest-who-adds', 'exhortation', 'add_nothing', "Rosh Hashanah 28b:10 — the exam's row add_nothing"),
    ('the-sleeper-on-the-eighth', 'exhortation', 'add_out_of_its_time', "Rosh Hashanah 28b:8-9; Eruvin 96a:5 — the exam's row add_out_of_its_time"),
    ('the-fifth-beside', 'exhortation', 'add_beside', "Sanhedrin 89a:2 — the exam's row add_beside"),
    ('the-one-sprinkling', 'exhortation', 'diminish_nothing', "Rosh Hashanah 28b:16-18 — the exam's row diminish_nothing"),
    ('the-paid-teacher', 'exhortation', 'taught_as_commanded', "Bekhorot 29a:7; Nedarim 37a:2 — the exam's row taught_as_commanded"),
    ('the-scholar-s-father-in-law', 'exhortation', 'the_cleaving', "Ketubot 111b:6-7 — the exam's row the_cleaving"),
    ('the-community-s-sentence', 'exhortation', 'god_so_near', "Rosh Hashanah 18a:10; Yevamot 105a:17 — the exam's row god_so_near"),
    ('the-grandfather', 'horeb', 'take_heed_lest_you_forget', "Kiddushin 30a:3-6; Menachot 99b:3; Avot 3:8 — the exam's row take_heed_lest_you_forget"),
    ('the-daughters', 'horeb', 'the_daughters_excluded', "Kiddushin 30a:6 — the exam's row the_daughters_excluded"),
    ('the-one-commanded-to-teach', 'horeb', 'commanded_to_teach', "Nedarim 38a:5 — the exam's row commanded_to_teach"),
    ('the-moon-forms', 'image', 'image_for_study', "Mishnah Rosh Hashanah 2:8; Rosh Hashanah 24b:13 — the exam's row image_for_study"),
    ('the-vessel-with-the-sun', 'image', 'image_of_the_host', "Rosh Hashanah 24b:8; Mishnah Avodah Zarah 3:3 — the exam's row image_of_the_host"),
    ('the-allotted-host', 'image', 'the_host_apportioned', "Avodah Zarah 55a:9 — the exam's row the_host_apportioned"),
    ('the-grown-old', 'exile', 'the_case_head', "Gittin 88a:15-17 — the exam's row the_case_head"),
    ('the-inquirer', 'god', 'the_former_days', "Chagigah 11b:21-24 — the exam's row the_former_days"),
    ('the-sorcerer-s-victim', 'god', 'you_were_shown', "Chullin 7b:14 — the exam's row you_were_shown"),
    ('the-haggadah-s-expounder', 'god', 'the_nation_from_a_nation', "Mishnah Pesachim 10:4 — the exam's row the_nation_from_a_nation"),
    ('the-manslayer-in-moses-three', 'cities', 'not_until_all_six', "Mishnah Makkot 2:4 — the exam's row not_until_all_six"),
    ('the-teacher-exiled', 'cities', 'the_manslayer_defined', "Makkot 10a:11 — the exam's row the_manslayer_defined"),
]


def scene():
    """THE SCENE — the exam's rows replayed on the world engine (the exodus epoch): the exam's persons through horeb_case — bal tosif's arms, the
    teaching, the images, the host, the exile, the inquiry, the creed, the Haggadah, the cities."""
    with contextlib.redirect_stdout(io.StringIO()):
        w = WE.World(era='Deut 4:1-49: chapter 4 on the shelf — Rosh Hashanah, Eruvin, Sanhedrin, Kiddushin, Bekhorot, Ketubot, Avodah Zarah, Chagigah, Chullin, Gittin, Makkot, Pesachim on the engine (the exodus epoch)', epoch='exodus')
        w.laws = [law_obey_horeb]
        w.advance(w.clock.day_in('exodus', 40, 11, 1))
        # THE DAEMON GATE READS LITERAL SUBMITS ONLY — the nineteen persons typed out from PERSONS
        w.submit({'kind': 'horeb_case', 'subject': 'the-priest-who-adds', 'person': 'the-priest-who-adds', 'cell': 'exhortation', 'ask': 'add_nothing', 'case_source': "Rosh Hashanah 28b:10 — the exam's row add_nothing"})
        w.submit({'kind': 'horeb_case', 'subject': 'the-sleeper-on-the-eighth', 'person': 'the-sleeper-on-the-eighth', 'cell': 'exhortation', 'ask': 'add_out_of_its_time', 'case_source': "Rosh Hashanah 28b:8-9; Eruvin 96a:5 — the exam's row add_out_of_its_time"})
        w.submit({'kind': 'horeb_case', 'subject': 'the-fifth-beside', 'person': 'the-fifth-beside', 'cell': 'exhortation', 'ask': 'add_beside', 'case_source': "Sanhedrin 89a:2 — the exam's row add_beside"})
        w.submit({'kind': 'horeb_case', 'subject': 'the-one-sprinkling', 'person': 'the-one-sprinkling', 'cell': 'exhortation', 'ask': 'diminish_nothing', 'case_source': "Rosh Hashanah 28b:16-18 — the exam's row diminish_nothing"})
        w.submit({'kind': 'horeb_case', 'subject': 'the-paid-teacher', 'person': 'the-paid-teacher', 'cell': 'exhortation', 'ask': 'taught_as_commanded', 'case_source': "Bekhorot 29a:7; Nedarim 37a:2 — the exam's row taught_as_commanded"})
        w.submit({'kind': 'horeb_case', 'subject': 'the-scholar-s-father-in-law', 'person': 'the-scholar-s-father-in-law', 'cell': 'exhortation', 'ask': 'the_cleaving', 'case_source': "Ketubot 111b:6-7 — the exam's row the_cleaving"})
        w.submit({'kind': 'horeb_case', 'subject': 'the-community-s-sentence', 'person': 'the-community-s-sentence', 'cell': 'exhortation', 'ask': 'god_so_near', 'case_source': "Rosh Hashanah 18a:10; Yevamot 105a:17 — the exam's row god_so_near"})
        w.submit({'kind': 'horeb_case', 'subject': 'the-grandfather', 'person': 'the-grandfather', 'cell': 'horeb', 'ask': 'take_heed_lest_you_forget', 'case_source': "Kiddushin 30a:3-6; Menachot 99b:3; Avot 3:8 — the exam's row take_heed_lest_you_forget"})
        w.submit({'kind': 'horeb_case', 'subject': 'the-daughters', 'person': 'the-daughters', 'cell': 'horeb', 'ask': 'the_daughters_excluded', 'case_source': "Kiddushin 30a:6 — the exam's row the_daughters_excluded"})
        w.submit({'kind': 'horeb_case', 'subject': 'the-one-commanded-to-teach', 'person': 'the-one-commanded-to-teach', 'cell': 'horeb', 'ask': 'commanded_to_teach', 'case_source': "Nedarim 38a:5 — the exam's row commanded_to_teach"})
        w.submit({'kind': 'horeb_case', 'subject': 'the-moon-forms', 'person': 'the-moon-forms', 'cell': 'image', 'ask': 'image_for_study', 'case_source': "Mishnah Rosh Hashanah 2:8; Rosh Hashanah 24b:13 — the exam's row image_for_study"})
        w.submit({'kind': 'horeb_case', 'subject': 'the-vessel-with-the-sun', 'person': 'the-vessel-with-the-sun', 'cell': 'image', 'ask': 'image_of_the_host', 'case_source': "Rosh Hashanah 24b:8; Mishnah Avodah Zarah 3:3 — the exam's row image_of_the_host"})
        w.submit({'kind': 'horeb_case', 'subject': 'the-allotted-host', 'person': 'the-allotted-host', 'cell': 'image', 'ask': 'the_host_apportioned', 'case_source': "Avodah Zarah 55a:9 — the exam's row the_host_apportioned"})
        w.submit({'kind': 'horeb_case', 'subject': 'the-grown-old', 'person': 'the-grown-old', 'cell': 'exile', 'ask': 'the_case_head', 'case_source': "Gittin 88a:15-17 — the exam's row the_case_head"})
        w.submit({'kind': 'horeb_case', 'subject': 'the-inquirer', 'person': 'the-inquirer', 'cell': 'god', 'ask': 'the_former_days', 'case_source': "Chagigah 11b:21-24 — the exam's row the_former_days"})
        w.submit({'kind': 'horeb_case', 'subject': 'the-sorcerer-s-victim', 'person': 'the-sorcerer-s-victim', 'cell': 'god', 'ask': 'you_were_shown', 'case_source': "Chullin 7b:14 — the exam's row you_were_shown"})
        w.submit({'kind': 'horeb_case', 'subject': 'the-haggadah-s-expounder', 'person': 'the-haggadah-s-expounder', 'cell': 'god', 'ask': 'the_nation_from_a_nation', 'case_source': "Mishnah Pesachim 10:4 — the exam's row the_nation_from_a_nation"})
        w.submit({'kind': 'horeb_case', 'subject': 'the-manslayer-in-moses-three', 'person': 'the-manslayer-in-moses-three', 'cell': 'cities', 'ask': 'not_until_all_six', 'case_source': "Mishnah Makkot 2:4 — the exam's row not_until_all_six"})
        w.submit({'kind': 'horeb_case', 'subject': 'the-teacher-exiled', 'person': 'the-teacher-exiled', 'cell': 'cities', 'ask': 'the_manslayer_defined', 'case_source': "Makkot 10a:11 — the exam's row the_manslayer_defined"})
    n = lambda eid, eff: len([e for e in w.entity(eid).ledger if e['effect'] == eff])
    tset = len([l for l in w.log if l[0] == 'TIMER-SET']); tfire = len([l for l in w.log if l[0] == 'TIMER-FIRE']); tcan = len([l for l in w.log if l[0] == 'TIMER-CANCEL'])
    closes = len([e for ent in w.entities.values() for e in ent.ledger if e.get('closed_by')])
    return (tuple(n(p, 'accepted') + n(p, 'exempt') for p, _, _, _ in PERSONS), (n('the-sleeper-on-the-eighth', 'exempt'), n('the-fifth-beside', 'accepted'), n('the-daughters', 'exempt'), n('the-moon-forms', 'exempt'), n('the-manslayer-in-moses-three', 'exempt')), (tset, tfire, tcan, len(w.timers)), len(w.entities), closes), w
SCENE, _W = scene()
# THE PREDICTION (typed before the first run — the design's arithmetic): every exam person written once; the four exempt arms ONE each and the fifth compartment ACCEPTED (retyped 2026-09-17 from the whole row); no timer;
# ENTITIES the nineteen persons; CLOSES 0.
SCENE_PREDICTED = ((1,) * 19, (1, 1, 1, 1, 1), (0, 0, 0, 0), 19, 0)
assert SCENE == SCENE_PREDICTED, ('THE DEUTERONOMY WALK 2b: the scene moved from its prediction', SCENE, SCENE_PREDICTED)


def narrative():
    """THE DEUTERONOMY WALK 2b (2026-09-16): the chapter's own acts AS HISTORY — the three own-day lines at the speech's day (40, 11, 1) and the two
    SUPPLIED Horeb lines dated by the RETROGRADE markers at Deut 4:10 (1, 3, 7) and 4:13 (1, 4, 17), the stretch ENDED by a FORWARD marker at 4:25 back to the speech's day (the engine's stretch runs to the next marker — the first generator run's finding), and the chapter OPENED by a forward marker at 4:1 (1b's Deut 2:2 stretch still open on the tape — the first stitch's finding) — on a world with this runner's daemon: 5 writes
    (one effect per line), no timer, TWO entities (Israel, Moses), the counter at (11, 1), NO close, no row, TWO dated lines. Recorded by the
    sequential run's recorder and stitched onto the tape (the markers the stitcher's rows). Not a graded cell: the tuple below is a tripwire typed
    from the design."""
    with contextlib.redirect_stdout(io.StringIO()):
        w = WE.World(era='Deut 4:1-49 on the tape — the one law, the two supplied Horeb lines, the one case, the three cities (the exodus epoch)', epoch='exodus')
        w.laws = [law_obey_horeb]
        w.advance(w.clock.day_in('exodus', 40, 11, 1))
        # THE DAEMON GATE READS LITERAL SUBMITS ONLY — the five lines typed out; no field named `until`, `days` or `due`
        w.marker('Deut 4:1', w.clock.day_in('exodus', 40, 11, 1), value='chapter 4 opens at the speech\'s own day — on the tape this FORWARD marker ends 1b\'s retrograde stretch (Deut 2:2\'s); here the counter\'s own day re-asserted')
        w.submit({'kind': 'add_nothing_commanded', 'subject': 'israel', 'law': 'you shall not add nor diminish (4:2)', 'receipt': 'as the LORD my God commanded me (4:5)', 'case_source': LINES[0][0]})
        w.marker('Deut 4:10', w.clock.day_in('exodus', 1, 3, 7), value='the ten words told — dated at the giving (Exod 19:16): RETROGRADE', placement='reading_placed')
        w.submit({'kind': 'ten_words_declared', 'subject': 'israel', 'first_telling': 'Exod 20:1-17', 'dated': 'the giving (1, 3, 7)', 'case_source': LINES[1][0]})
        w.marker('Deut 4:13', w.clock.day_in('exodus', 1, 4, 17), value='the tablets told — dated at the breaking (Exod 32:19): RETROGRADE', placement='reading_placed')
        w.submit({'kind': 'tablets_given', 'subject': 'moses', 'first_telling': 'Exod 31:18', 'dated': 'the fortieth day (1, 4, 17)', 'plene': 'the tablets written plene (4:13)', 'case_source': LINES[2][0]})
        w.marker('Deut 4:25', w.clock.day_in('exodus', 40, 11, 1), value='the stretch ends at the speech\'s day — the counter\'s own day re-asserted after the two dated lines: FORWARD (the first generator run found the two own-day lines after 4:13 dated at Tammuz — a retrograde stretch runs to the next marker)')
        w.submit({'kind': 'witnesses_called', 'subject': 'israel', 'case': 'when you beget sons (4:25)', 'witnesses': 'heaven and earth (4:26)', 'case_source': LINES[3][0]})
        w.submit({'kind': 'three_cities_set_apart', 'subject': 'israel', 'cities': ['Bezer', 'Ramoth', 'Golan'], 'manslayer': 'who slays his neighbor unawares (4:42)', 'case_source': LINES[4][0]})
    writes = len([l for l in w.log if l[0] == 'WRITE'])
    closes = len([e for ent in w.entities.values() for e in ent.ledger if e.get('closed_by')])
    rows = len([l for l in w.log if l[0] == 'ROW'])
    dated = len([l for l in w.log if l[0] == 'EVENT' and l[2].get('dated') is not None])
    return (writes, len([l for l in w.log if l[0] == 'TIMER-SET']), len(w.entities), w.clock.eras['exodus'].date(w.clock.day)[1:], closes, rows, len(w.tables['population']), dated), w


NARRATIVE, _WN = narrative()
NARRATIVE_PREDICTED = (5, 0, 2, (11, 1), 0, 0, 0, 2)   # DEUTERONOMY_WALK.md "Sitting 2b": 5 writes (one per line), no timer, TWO entities, the counter's day (11, 1), NO close, no row, TWO dated lines (the retrograde stretches')
assert NARRATIVE == NARRATIVE_PREDICTED, ('THE DEUTERONOMY WALK 2b: the chapter\'s narrative moved from its prediction', NARRATIVE, NARRATIVE_PREDICTED)
_isr = _WN.entity('israel').ledger
assert [e['effect'] for e in _isr] == ['adding_barred', 'covenant_declared', 'heaven_and_earth_witness', 'cities_set_apart'] and [e['effect'] for e in _WN.entity('moses').ledger] == ['tablets_delivered'], ([e['effect'] for e in _isr], [e['effect'] for e in _WN.entity('moses').ledger])
assert [ex.date(l[2]['dated']) for l in _WN.log if l[0] == 'EVENT' and l[2].get('dated') is not None for ex in [_WN.clock.eras['exodus']]] == [(1, 3, 7), (1, 4, 17)], 'the two supplied lines dated by their markers'


# =====================================================================
# Motion 2 — THE TEST DATA: the answer sheet's rows (the docket's LAW rows and the cells' asks) — GENERATED FROM THE CELLS' OWN ASKS by ch4_cases_gen.py
# (1b's lesson: a mistyped expected string grades nothing), then frozen as literals under the honest-pairing guard.
# =====================================================================
CASES = [
    # F1 — the_exhortation
    ('Deut 4:1 — hear_and_do', lambda: the_exhortation({'ask': 'hear_and_do'}, DATA), "hear and do (4:1) — the exhortation's head: the singular imperative, the plural object; the teach-root's first seat"),
    ('Deut 4:2 — add_nothing', lambda: the_exhortation({'ask': 'add_nothing'}, DATA), "you shall not add (4:2) — THE CHAPTER'S ONE LAW: a BLOCK on Israel (adding_barred); the exam's parameters — in its time without intent, out of its time with intent (Rava); an addition that spoils (the elder's fifth compartment)"),
    ('Deut 4:2 — diminish_nothing', lambda: the_exhortation({'ask': 'diminish_nothing'}, DATA), "nor diminish (4:2) — the pair's other arm: an omission where adding is an act (R. Yehoshua); 13:1 the second seat forward"),
    ('shelf: Rosh Hashanah 28b:9 — add_out_of_its_time', lambda: the_exhortation({'ask': 'add_out_of_its_time'}, DATA), 'an addition out of its time (Rosh Hashanah 28b) — no intent, no transgression: the sleeper on the eighth day exempt'),
    ('shelf: Sanhedrin 89a:2 — add_beside', lambda: the_exhortation({'ask': 'add_beside'}, DATA), "an addition placed beside (Sanhedrin 89a:2) — R. Zeira: the fifth compartment spoils the four even beside them; the transgression stands: accepted"),
    ('Deut 4:3 — baal_peor_seen', lambda: the_exhortation({'ask': 'baal_peor_seen'}, DATA), "Baal-peor seen (4:3) — Numbers 25:3-9 READ BACK, SHORTENED: the yoking, the slaying and the plague's count in one clause (BK by CALL)"),
    ('Deut 4:4 — the_cleaving', lambda: the_exhortation({'ask': 'the_cleaving'}, DATA), 'you who cleave (4:4) — the survivors of Peor; cleaving to a consuming fire resolved as cleaving to the sages (the Sifrei 49:2; Ketubot 111b)'),
    ('Deut 4:5 — taught_as_commanded', lambda: the_exhortation({'ask': 'taught_as_commanded'}, DATA), "taught as commanded (4:5) — THE RECEIPT in Moses' own voice: the teaching's run of Exodus 24:12's command (ER by CALL); the register seat ACT; free teaching (Bekhorot 29a)"),
    ('Deut 4:6 — wisdom_before_the_peoples', lambda: the_exhortation({'ask': 'wisdom_before_the_peoples'}, DATA), "your wisdom before the peoples (4:6) — the reckoning of the seasons (Shabbat 75a); Solomon's pair the kin"),
    ('Deut 4:7 — god_so_near', lambda: the_exhortation({'ask': 'god_so_near'}, DATA), "God so near (4:7) — the plural adjective with the singular 'upon him' (Sanhedrin 38b); a community's sentence never sealed (Rosh Hashanah 18a)"),
    ('Deut 4:8 — righteous_statutes', lambda: the_exhortation({'ask': 'righteous_statutes'}, DATA), "righteous statutes (4:8) — the exhortation's close: the Torah set before them this day (11:32 the pair)"),
    ('Deut 4:1-8 — the_write', lambda: the_exhortation({'ask': 'the_write'}, DATA), "the write (4:1-8) — adding_barred on Israel: the one law's block; the receipt inside the line's source"),
    # F2 — horeb_retold
    ('Deut 4:9 — take_heed_lest_you_forget', lambda: horeb_retold({'ask': 'take_heed_lest_you_forget'}, DATA), "take heed lest you forget (4:9) — the forgetter's prohibition (Menachot 99b; Avot 3:8); the grandsons included, the daughters excluded (Kiddushin 30a)"),
    ('shelf: Kiddushin 30a:6 — the_daughters_excluded', lambda: horeb_retold({'ask': 'the_daughters_excluded'}, DATA), "the daughters excluded (Kiddushin 30a) — 'your sons' not your daughters; the grandsons taught: exempt from the duty's addressees"),
    ('Deut 4:10 — the_day_at_horeb', lambda: horeb_retold({'ask': 'the_day_at_horeb'}, DATA), "the day at Horeb (4:10) — the assembly's day (1, 3, 7) by Rabbi Yose's seventh (ES by CALL); the retrograde marker's day at Deut 4:10"),
    ('Deut 4:10 — learn_and_teach', lambda: horeb_retold({'ask': 'learn_and_teach'}, DATA), "learn and teach are one word (4:10) — qal and piel by the pointing alone: the reading's crown, DATA"),
    ('Deut 4:11 — the_mountain_burning', lambda: horeb_retold({'ask': 'the_mountain_burning'}, DATA), 'the mountain burning (4:11) — Exodus 19:17-18 READ BACK, EXPANDED: the heart of heaven, the darkness, cloud and thick darkness told larger than the smoke'),
    ('Deut 4:12 — the_voice_and_no_form', lambda: horeb_retold({'ask': 'the_voice_and_no_form'}, DATA), "the voice and no form (4:12, 15) — THE TAPE'S HOLE: Exodus 20:1's speaking written once at its own time (1, 3, 7) — covenant_declared on Israel (SUPPLIED)"),
    ('Deut 4:13 — the_ten_words_and_the_tablets', lambda: horeb_retold({'ask': 'the_ten_words_and_the_tablets'}, DATA), "the ten words and the tablets (4:13) — three seats of 'the ten words' (ER by CALL); the tablets plene; Exodus 31:18's giving written once at (1, 4, 17) — tablets_delivered on Moses (SUPPLIED)"),
    ('Deut 4:14 — commanded_to_teach', lambda: horeb_retold({'ask': 'commanded_to_teach'}, DATA), "commanded to teach (4:14) — the command 4:5's receipt answers (Exodus 24:12); who was commanded disputed (Nedarim 38a)"),
    # F3 — no_image
    ('Deut 4:15 — no_form_seen', lambda: no_image({'ask': 'no_form_seen'}, DATA), "no form seen (4:15) — the guard's reason: the voice without a form (4:12 read back)"),
    ('Deut 4:16-18 — the_image_list', lambda: no_image({'ask': 'the_image_list'}, DATA), "the no-image list (4:16-18) — Exodus 20:4's likeness restated in seven kinds: THE SECOND WORD'S PARAMETER TABLE as DATA; its engine OWED (chapter 5's sitting)"),
    ('shelf: Rosh Hashanah 24b:13 — image_for_study', lambda: no_image({'ask': 'image_for_study'}, DATA), "the images for study (Rosh Hashanah 24b) — Rabban Gamliel's forms permitted: made by others, in pieces, to teach himself — exempt"),
    ('shelf: Rosh Hashanah 24b:8 — image_of_the_host', lambda: no_image({'ask': 'image_of_the_host'}, DATA), "an image of the host (Rosh Hashanah 24b:8) — forming the sun and the moon prohibited: the second word's row holds (its engine OWED)"),
    ('Deut 4:19 — the_host_apportioned', lambda: no_image({'ask': 'the_host_apportioned'}, DATA), "the host apportioned (4:19) — with 29:25 by the Sifrei 148:8's pair; Rav's reading (Avodah Zarah 55a): a DATA note, no link of our own"),
    ('Deut 4:20 — the_iron_furnace', lambda: no_image({'ask': 'the_iron_furnace'}, DATA), 'the iron furnace (4:20) — the exodus READ BACK, EXPANDED: the furnace told only here in the Torah (1 Kings 8:51 outside; PR by CALL)'),
    ('Deut 4:21-22 — the_bar_third_telling', lambda: no_image({'ask': 'the_bar_third_telling'}, DATA), "the bar's third telling (4:21-22) — 'on your account' and an oath against Numbers 20:12's 'because you did not believe': DISAGREES, the 1b row widened, an OPEN row; no oath written"),
    ('Deut 4:23 — the_covenant_not_forgotten', lambda: no_image({'ask': 'the_covenant_not_forgotten'}, DATA), "the covenant not forgotten (4:23) — the guard's second seat: the covenant cut at Horeb (the tape's covenant_blood_thrown) and the image"),
    ('Deut 4:24 — consuming_fire_jealous_god', lambda: no_image({'ask': 'consuming_fire_jealous_god'}, DATA), "a consuming fire, a jealous God (4:24) — the second word's 'jealous' (Exodus 20:5 by reference); jealousy at the worshipper, not the idol (Avodah Zarah 54b-55a)"),
    # F4 — the_exile_case
    ('Deut 4:25 — the_case_head', lambda: the_exile_case({'ask': 'the_case_head'}, DATA), "the case head (4:25) — THE CHAPTER'S ONE CASE: 'when' with the imperfect; the arms DATA; the exile hastened by two years (Gittin 88a)"),
    ('Deut 4:26 — the_witnesses', lambda: the_exile_case({'ask': 'the_witnesses'}, DATA), "the witnesses (4:26) — heaven and earth called: a STATUS on Israel (the Sifrei 306:1's chain, the third of eleven)"),
    ('Deut 4:26-27 — perish_and_scatter', lambda: the_exile_case({'ask': 'perish_and_scatter'}, DATA), "perish and scatter (4:26-27) — the case's first arm: Leviticus 26:33's scattering by CALL (TC), no entry written"),
    ('Deut 4:28 — serve_wood_and_stone', lambda: the_exile_case({'ask': 'serve_wood_and_stone'}, DATA), 'serve wood and stone (4:28) — 28:36 and 28:64 forward; Psalm 115:5 the kin'),
    ('Deut 4:29 — seek_and_find', lambda: the_exile_case({'ask': 'seek_and_find'}, DATA), "seek and find (4:29) — the case's second arm: the Shema's words (6:5 forward); 30:10's kin"),
    ('Deut 4:30 — in_your_distress_return', lambda: the_exile_case({'ask': 'in_your_distress_return'}, DATA), "in your distress, return (4:30) — the case's third arm: 30:2's kin; 'the end of days' a prophecy, no timer (TC by CALL)"),
    ('Deut 4:31 — the_merciful_god', lambda: the_exile_case({'ask': 'the_merciful_god'}, DATA), "the merciful God (4:31) — Exodus 34:6's attribute; the fathers' covenant sworn (Genesis 22:16, 26:3 by reference); Leviticus 26:42 the first telling"),
    # F5 — the_one_god
    ('Deut 4:32 — the_former_days', lambda: the_one_god({'ask': 'the_former_days'}, DATA), 'the former days (4:32) — the creation READ BACK as a time-reference (PS by CALL); the limits of inquiry (Chagigah 11b)'),
    ('Deut 4:33 — the_voice_and_lived', lambda: the_one_god({'ask': 'the_voice_and_lived'}, DATA), "the voice and lived (4:33) — 5:26's kin; the assembly's lord_descended by reference"),
    ('Deut 4:34 — the_nation_from_a_nation', lambda: the_one_god({'ask': 'the_nation_from_a_nation'}, DATA), "a nation from the midst of a nation (4:34) — the seven instruments: the exodus READ BACK, EXPANDED (ES by CALL); the Haggadah's row (Pesachim 10:4)"),
    ('Deut 4:35 — you_were_shown', lambda: the_one_god({'ask': 'you_were_shown'}, DATA), "you were shown (4:35) — the creed's first seat: 'none else beside him' (even sorcery — Chullin 7b); the kingship verses disputed"),
    ('Deut 4:36 — from_heaven_the_voice', lambda: the_one_god({'ask': 'from_heaven_the_voice'}, DATA), 'from heaven the voice (4:36) — Exodus 20:22 READ BACK (DC by CALL for the seat; the Mekhilta credited by name)'),
    ('Deut 4:37 — because_he_loved_your_fathers', lambda: the_one_god({'ask': 'because_he_loved_your_fathers'}, DATA), "because he loved your fathers (4:37) — the choice of the seed (Genesis 17's phrase; PR by CALL); the outbringing READ BACK"),
    ('Deut 4:38 — to_dispossess_nations', lambda: the_one_god({'ask': 'to_dispossess_nations'}, DATA), 'to dispossess nations (4:38) — the open dispossess debit of Numbers 33:50-56 READ; 9:1 the kin'),
    ('Deut 4:39 — know_this_day', lambda: the_one_god({'ask': 'know_this_day'}, DATA), "know this day (4:39) — the creed's second seat: Rahab's and Solomon's words outside the Torah; the seventh son's (Gittin 57b)"),
    ('Deut 4:40 — keep_the_statutes', lambda: the_one_god({'ask': 'keep_the_statutes'}, DATA), "keep the statutes (4:40) — the reward clause: well with you, prolonged days (5:16's pair forward)"),
    # F6 — the_cities_and_the_frame
    ('Deut 4:41 — then_moses_set_apart', lambda: the_cities_and_the_frame({'ask': 'then_moses_set_apart'}, DATA), "then Moses set apart (4:41) — Moses' own act in the third person: cities_set_apart on Israel (the Song's 'then' form; R. Simlai's mitzva that came his way)"),
    ('Deut 4:41; Num 35:13-14 — not_until_all_six', lambda: the_cities_and_the_frame({'ask': 'not_until_all_six'}, DATA), "not until all six (Makkot 2:4) — the three east admitted no one: the refuge debit on Israel READ OPEN and left open (RF by CALL); the manslayer's refuge exempt until Joshua's three"),
    ('Deut 4:42 — the_manslayer_defined', lambda: the_cities_and_the_frame({'ask': 'the_manslayer_defined'}, DATA), "the manslayer defined (4:42) — 19:4's words with 'slays' for 'smites' (computed); the refuge runner's clauses by CALL; 'and live' the teacher exiled with his school (Makkot 10a)"),
    ('Deut 4:43 — the_three_names', lambda: the_cities_and_the_frame({'ask': 'the_three_names'}, DATA), "the three names (4:43) — Bezer, Ramoth, Golan (RF's row by CALL); the two rows of vines (Makkot 9b:18); Joshua 20:8's Gaulon"),
    ('Deut 4:44-45 — the_second_frame', lambda: the_cities_and_the_frame({'ask': 'the_second_frame'}, DATA), "the second frame (4:44-45) — the second speech's head: a stamp of place and era, NO WRITE (R6); EXPANDED against 1:1-5 (OS by CALL)"),
    ('Deut 4:46-49 — the_borders_verbatim', lambda: the_cities_and_the_frame({'ask': 'the_borders_verbatim'}, DATA), "the borders verbatim (4:46-49) — the retelling of a retelling: the speech's own 1:4, 3:8, 2:36, 3:17 in their own clauses (computed); Mount Sion the fourth name (CK, BO, OS, BK by CALL)"),
    ('Deut 4:3-49 — the_readback_table', lambda: the_cities_and_the_frame({'ask': 'the_readback_table'}, DATA), "the readback table — eleven reference rows graded; the two supplied lines the tape's hole; the one disagreement widened, open (CC4)"),
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
    print('THE INK: numbers %s; the one frame %s; the case tokens %s; the register singular-only %s, plural-only %s, both %s' % (sorted(PARSED.items()), DIV, dict(collections.Counter(x for l in CASE_TOK.values() for x in l)), SG_ONLY, PL_ONLY, BOTH))
    print('THE READBACK: %d rows — %s; the deltas: Peor %s; Horeb %s; the tablets %s; the bar %s; the instruments %s; the frame %s; the borders %s' % (len(READBACK), dict(RB_GRADES), PEOR_DELTA, HOREB_DELTA, TABLETS_DELTA, BAR_DELTA, INSTR_DELTA, FRAME_DELTA, BORDERS_DELTA))
    print('THE HOLE: the ten words %s seats; the tablets plene %s; the giving\'s day %s (Rabbi Yose); the fortieth day %s' % (TEN_WORDS, TABLETS_PLENE, ES_DAYS['v'], ER_TAMMUZ['v']))
    print('THE CITIES: %s; the debit %s; the manslayer\'s diff %s' % (RF.DATA['the_six_cities']['value']['beyond_the_jordan'], RF_DEBIT[0][:60], MANSLAYER_DIFF[2:4]))
    print('THE SCENE on the bench: %s; the exempt arms %s; the timers (set, fired, cancelled, pending) %s; entities %d; closes %d' % (SCENE[0], SCENE[1], SCENE[2], SCENE[3], SCENE[4]))
    print('THE NARRATIVE: %s' % (NARRATIVE,))
    print('THE PARAMETER ROWS: ' + '; '.join('%s = %s' % (k, DATA[k]['value'] if k != 'the_readback' else '%d rows' % len(DATA[k]['value'])) for k in DATA) + ' (the other settings recorded in DATA)')
    if ok == len(CASES):
        print('\nTHE COMPILE OF CHAPTER 4: the answer sheet REPRODUCED — %d/%d' % (ok, len(CASES)))
    sys.exit(0 if ok == len(CASES) else 1)

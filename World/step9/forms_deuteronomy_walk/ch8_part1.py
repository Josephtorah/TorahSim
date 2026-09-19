#!/usr/bin/env python3
# DEUTERONOMY 8:1-20 — THE GOOD LAND: THE GRACE AFTER THE MEAL AND THE FORGETTING BARRED COMPILED FOR THE FIRST TIME (THE CODE'S HOLES), THE
# TESTIMONY'S EFFECT REUSED, AND THE READBACK'S FIFTH FORM — THE RETELLING OF A STATE (THE DEUTERONOMY WALK sitting 6b, 2026-09-19;
# World/step9/DEUTERONOMY_WALK.md "Sitting 6b"; the state doc's #196). THE CHAPTER'S OWN LINES: no runner held a cell for "and you shall eat and be
# satisfied and bless the LORD your God" (8:10 — the Torah's one command to bless him) and 6:12's cell held "take heed to yourself lest you forget" as
# an ask WITHOUT A WRITE (the recon's regex over all sixty-two runners) — F3 and F4 compile them from the ink with the answer sheet Mishnah Berakhot
# 6:1-7:5, Mishnah Bikkurim 1, Mishnah Sukkah 2:5 and the Talmud's rows as the compile rules (the docket deu_08_ekev_exam_2026-09-19.md, 451 rows read
# whole); bless_after_eating_commanded a STATUS and forgetting_barred a BLOCK on Israel, heaven_and_earth_witness (law_obey_horeb's effect at 4:26)
# REUSED at 8:19 — all at the chapter's own day (40, 11, 1), NO marker (the speech continuing from chapter 7's own-day lines). THE READBACK'S FIFTH
# FORM (THE LOOP's step 6): chapter 8 retells the wilderness as the REASON for a law ("remember … lest you forget"), so its rows are REFERENCE ROWS
# graded against the tape's lines by kind and first verse or the kin's cells by CALL, never a second write — and ONE row retells a STATE the tape
# never wrote and cannot write as an act: the garment that did not wear out and the foot that did not swell over forty years (8:4), graded SUPPLIED
# with NO retrograde write (the design's decision, open to the owner); eighteen rows (VERBATIM 6 / VARIANT 5 / EXPANDED 4 / TURNED 2 / SUPPLIED 1).
# The daemon law_good_land given_at Deut 8:1, installed_by boot (the Deuteronomy daemons' form). Six cells; every token probed (zero-report law);
# effects on every cell (the effects law); eighteen DATA rows (the four the docket added: the grace conditional on eating, the four blessings' three
# divisions, the blessing before refuted, the heart lifted). Reading ledger: logic/oral_triage/deu_08_ekev_2026-09-18.md (36 sources, 6 claims); the exam's docket: deu_08_ekev_exam_2026-09-19.md
# (451 rows READ WHOLE FROM THE START: LAW 80 / DERIVATION 82 / DISPUTE 36 / CONTEXT 160 / OUTSIDE 93).

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
import cold_run_obey_horeb as OH               # THE EDGE: good_land -> obey_horeb CALL, reference (4:1's exhortation, 4:9's take heed, 4:26's testimony — the effect REUSED)
import cold_run_exodus_story as ES             # THE EDGE: good_land -> exodus_story CALL, reference (the manna, the rock at Horeb, the going out, the trials' direction)
import cold_run_shelach as SL                  # THE EDGE: good_land -> shelach CALL, reference (the decree's forty years — a day for a year)
import cold_run_beha as BH                     # THE EDGE: good_land -> beha CALL, reference (the craving's manna described — its tastes and forms)
import cold_run_chukat as CK                   # THE EDGE: good_land -> chukat CALL, reference (the fiery serpents; Meribah's second rock)
import cold_run_hear_o_israel as HI            # THE EDGE: good_land -> hear_o_israel CALL, reference (6:12's clause — the ask without a write; 6:10-11's gift; 6:3's land; the triad)
import cold_run_opening_speech as OS           # THE EDGE: good_land -> opening_speech CALL, reference (2:7's lacking nothing; 1:31's carrying; 1:19's wilderness)
import cold_run_covenant_at_horeb as CH        # THE EDGE: good_land -> covenant_at_horeb CALL, reference (the second word's clause reversed; 5:6's formula)
import cold_run_seven_nations as SN            # THE EDGE: good_land -> seven_nations CALL, reference (7:8's oath, 7:11's triad, 7:12's heel, the ban's nations)
import cold_run_ordinances as OR               # THE EDGE: good_land -> ordinances CALL, reference (23:25's bread and water blessed — the Sifrei 40:10's kin)
import cold_run_sanctions as SA                # THE EDGE: good_land -> sanctions CALL, reference (Leviticus 18:5's 'and live by them' — 8:1's and 8:3's living)
import cold_run_mamre as MA                    # THE EDGE: good_land -> mamre CALL, reference (the oath's lines sworn_by_himself 22:16-18 and oath_upheld 26:3-5; the test verb)
import cold_run_joseph as JS                   # THE EDGE: good_land -> joseph CALL, reference (the oath's third line visitation_promised 50:24)

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
def W8(v): return words('Deut', 8, v)
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

# ---- THE INK, computed (the parser and the tokens; the reading's facts the expectations — every assert PROVEN at the reading, ch8_ink.py) ----
SPAN = [(8, v) for v in range(1, 21)]
PARSED = {(c, v): ink_numbers(verse_words('Deut', c, v)) for (c, v) in SPAN if ink_numbers(verse_words('Deut', c, v))}
def MARKS(c, v): return [t for t in verse_words('Deut', c, v) if t[-1] in '#~^%@|*']
def N(b, c, v): return ink_numbers(verse_words(b, c, v))
assert PARSED == {(8, 2): [40], (8, 4): [40]} and {(c, v): ink_ordinals(verse_words('Deut', c, v)) for (c, v) in SPAN if ink_ordinals(verse_words('Deut', c, v))} == {} and [((c, v), t) for (c, v) in SPAN for t in MARKS(c, v)] == [((8, 10), 'ושבעת*'), ((8, 12), 'ושבעת*')], PARSED   # TWO number verses — the forty years twice; the sated verb starred twice; no ordinal; NO GAP
assert N('Deut', 2, 7) == [40] and N('Deut', 29, 4) == [40] and N('Exod', 16, 35) == [40] and N('Num', 14, 33) == [40] and N('Num', 14, 34) == [40, 40] and N('Num', 32, 13) == [40] and N('Deut', 1, 3) == [40, 11, 1] and N('Deut', 6, 11) == [] and N('Deut', 11, 15) == [] and N('Deut', 31, 20) == [] and N('Deut', 4, 26) == [] and N('Deut', 30, 18) == [] and MARKS(6, 11) == ['ושבעת*'] and MARKS(11, 15) == ['ושבעת*'] and MARKS(31, 20) == ['ושבע*']
assert lemma_of('Deut', 8, 1, 'נשבע') == ['7650'] and lemma_of('Deut', 8, 18, 'נשבע') == ['7650'] and lemma_of('Deut', 8, 10, 'ושבעת') == ['7646'] and lemma_of('Deut', 8, 12, 'ושבעת') == ['7646'] and lemma_of('Deut', 8, 2, 'ארבעים') == ['705'] and morphs('Deut', 8, 2)[9] == 'HAcbpa' and morphs('Deut', 8, 4)[8] == 'HAcbpa'
FORTY = PARSED[(8, 2)][0]
assert [(s, x) for s, x, m in LEMT('7646', books=('Deut',))] == [('Deut 6:11', 'ושבעת'), ('Deut 8:10', 'ושבעת'), ('Deut 8:12', 'ושבעת'), ('Deut 11:15', 'ושבעת'), ('Deut 14:29', 'ושבעו'), ('Deut 26:12', 'ושבעו'), ('Deut 31:20', 'ושבע')] and P('זה', 'ארבעים', 'שנה') == ['Deut 2:7', 'Deut 8:2', 'Deut 8:4'] and len(P('ארבעים', 'שנה')) == 31
TOK = sum(len(W8(v)) for v in range(1, 21)); LET = sum(len(x) for v in range(1, 21) for x in W8(v))
assert TOK == 293 and LET == 1148 and {v: len(W8(v)) for v in range(1, 21)} == {1: 19, 2: 23, 3: 28, 4: 10, 5: 12, 6: 9, 7: 15, 8: 10, 9: 18, 10: 12, 11: 16, 12: 7, 13: 11, 14: 11, 15: 16, 16: 13, 17: 10, 18: 20, 19: 20, 20: 13}, TOK
assert byw[('Deut', 8, 2)][20] == 'x-ketiv' and W8(2)[20] == 'מצותו' and Counter(wt for v in range(1, 21) for wt in byw[('Deut', 8, v)]) == Counter({None: 292, 'x-ketiv': 1}) and U('מצותו') == ['Deut 27:10', 'Deut 5:10', 'Deut 7:9', 'Deut 8:2', 'Num 15:31']   # THE WRITTEN/READ PAIR at 8:2 — 7:9's and 5:10's kin (the store's extra token, kept out of every check)
# THE FRAMES AND THE REGISTER: NO divine frame, NO "saying"; the narrative verbs THREE (8:3 — God's acts); ONE imperative (8:11); TWO infinitive absolutes (8:19); the prohibition form twice, neither a command
NUM = {v: (sum(1 for m in morphs('Deut', 8, v) if m and '2mp' in m), sum(1 for m in morphs('Deut', 8, v) if m and '2ms' in m)) for v in range(1, 21)}
SG_ONLY = [v for v, (p, s) in NUM.items() if s and not p]; PL_ONLY = [v for v, (p, s) in NUM.items() if p and not s]; BOTH = [v for v, (p, s) in NUM.items() if p and s]; NEITHER = [v for v, (p, s) in NUM.items() if not p and not s]
assert SG_ONLY == [2, 3, 4, 5, 6, 7, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18] and PL_ONLY == [20] and BOTH == [1, 19] and NEITHER == [8]
DIV = [v for v in range(1, 21) if any(V in ('ויאמר', 'וידבר') and W8(v)[i + 1] == 'יהוה' for i, V in enumerate(W8(v)[:-1]))]
assert DIV == [] and [v for v in range(1, 21) if 'לאמר' in W8(v)] == [] and [v for v in range(1, 21) if 'משה' in W8(v) or 'ישראל' in W8(v)] == []
REG = {v: [x for x, m in wm('Deut', 8, v) if m and re.search(r'^HC/V.w', m)] for v in range(1, 21) if any(m and re.search(r'^HC/V.w', m) for _, m in wm('Deut', 8, v))}
assert REG == {3: ['ויענך', 'וירעבך', 'ויאכלך']}, REG
IMPER = {v: [(x, m) for x, m in wm('Deut', 8, v) if m and re.match(r'^HV.?.?v', m)] for v in range(1, 21) if any(m and re.match(r'^HV.?.?v', m) for _, m in wm('Deut', 8, v))}
INFA = {v: [(x, m) for x, m in wm('Deut', 8, v) if m and re.match(r'^H(?:C/)?V.a$', m)] for v in range(1, 21) if any(m and re.match(r'^H(?:C/)?V.a$', m) for _, m in wm('Deut', 8, v))}
assert IMPER == {11: [('השמר', 'HVNv2ms')]} and INFA == {19: [('שכח', 'HVqa'), ('אבד', 'HVqa')]}, (IMPER, INFA)
WEQATAL_V = sorted(v for v in range(1, 21) if any(m and re.search(r'^HC/V.q', m) for _, m in wm('Deut', 8, v)))
assert WEQATAL_V == [1, 2, 5, 6, 10, 12, 14, 17, 18, 19] and [x for x, m in wm('Deut', 8, 10) if re.search(r'^HC/V.q', m)] == ['ואכלת', 'ושבעת', 'וברכת'] and [x for x, m in wm('Deut', 8, 19) if re.search(r'^HC/V.q', m)] == ['והיה', 'והלכת', 'ועבדתם', 'והשתחוית']
NEG = ('לא', 'ולא')
PRO = {v: [(W8(v)[i + 1], morphs('Deut', 8, v)[i + 1]) for i, x in enumerate(W8(v)[:-1]) if x in NEG and morphs('Deut', 8, v)[i + 1] and morphs('Deut', 8, v)[i + 1].startswith('HV')] for v in range(1, 21) if any(x in NEG for x in W8(v))}
assert PRO == {2: [], 3: [('ידעת', 'HVqp2ms'), ('ידעון', 'HVqp3cp/Sn')], 4: [('בלתה', 'HVqp3fs'), ('בצקה', 'HVqp3fs')], 9: [('תחסר', 'HVqi2ms')], 16: [('ידעון', 'HVqp3cp/Sn')], 20: [('תשמעון', 'HVqi2mp/Sn')]}, PRO
assert sum(1 for v in PRO for _, m in PRO[v] if 'i2' in m) == 2 and sum(1 for v in PRO for _, m in PRO[v] if 'i3' in m) == 0   # the two prohibition forms a promise (8:9) and a report (8:20), neither a command
CASE_TOK = {f'8:{v}': [x for x in W8(v) if x in ('כי', 'אם', 'ואם', 'או', 'פן')] for v in range(1, 21) if any(x in ('כי', 'אם', 'ואם', 'או', 'פן') for x in W8(v))}
assert CASE_TOK == {'8:2': ['אם'], '8:3': ['כי', 'כי'], '8:5': ['כי'], '8:7': ['כי'], '8:11': ['פן'], '8:12': ['פן'], '8:18': ['כי'], '8:19': ['אם', 'כי']}
LEMAAN = {v: [x for x in W8(v) if x in ('למען', 'ולמען')] for v in range(1, 21) if any(x in ('למען', 'ולמען') for x in W8(v))}
assert LEMAAN == {1: ['למען'], 2: ['למען'], 3: ['למען'], 16: ['למען', 'ולמען'], 18: ['למען']} and len(U('למען', 'ולמען', books=('Deut',))) == 43
ONE_CS = {v: [(x, m) for x, m in wm('Deut', 8, v) if m and '1cs' in m] for v in range(1, 21) if any(m and '1cs' in m for _, m in wm('Deut', 8, v))}
assert ONE_CS == {1: [('אנכי', 'HPp1cs')], 11: [('אנכי', 'HPp1cs')], 17: [('כחי', 'HNcmsc/Sp1cs'), ('ידי', 'HNcbsc/Sp1cs'), ('לי', 'HR/Sp1cs')], 19: [('העדתי', 'HVhp1cs')]} and not any('1cp' in (m or '') for v in range(1, 21) for _, m in wm('Deut', 8, v))   # the first person Moses' (8:1, 8:11, 8:19) and the boaster's (8:17); no "we"
CHAIN = [(v, x) for v in range(1, 21) for x, m in wm('Deut', 8, v) if m and m.startswith('HTd/V') and 'r' in m[6:8]]
assert CHAIN == [(14, 'המוציאך'), (15, 'המוליכך'), (15, 'המוציא'), (16, 'המאכלך'), (18, 'הנתן')]   # the article + participle chain of five: who brought you out, who led you, who brought out water, who fed you, who gives
NAME = Counter(x for v in range(1, 21) for x in W8(v) if x in ('יהוה', 'ויהוה', 'ביהוה', 'כיהוה', 'ליהוה'))
YG_SG = [v for v in range(1, 21) for i in range(len(W8(v)) - 1) if W8(v)[i:i + 2] == ['יהוה', 'אלהיך']]; YG_PL = [v for v in range(1, 21) for i in range(len(W8(v)) - 1) if W8(v)[i:i + 2] == ['יהוה', 'אלהיכם']]
assert NAME == Counter({'יהוה': 13}) and YG_SG == [2, 5, 6, 7, 10, 11, 14, 18, 19] and YG_PL == [20] and [v for v in range(1, 21) for i in range(len(W8(v))) if W8(v)[i] == 'יהוה' and (i + 1 >= len(W8(v)) or W8(v)[i + 1] not in ('אלהיך', 'אלהיכם'))] == [1, 3, 20]
assert {v: [x for x in W8(v) if x in ('פרעה', 'לפרעה', 'מצרים')] for v in range(1, 21) if any(x in ('פרעה', 'לפרעה', 'מצרים') for x in W8(v))} == {14: ['מצרים']} and {v: [x for x in W8(v) if 'אבת' in x] for v in range(1, 21) if any('אבת' in x for x in W8(v))} == {1: ['לאבתיכם'], 3: ['אבתיך'], 16: ['אבתיך'], 18: ['לאבתיך']}
NUN = {v: [x for x, m in wm('Deut', 8, v) if m and m.endswith('/Sn')] for v in range(1, 21) if any(m and m.endswith('/Sn') for _, m in wm('Deut', 8, v))}
assert NUN == {1: ['תשמרון', 'תחיון'], 3: ['ידעון'], 13: ['ירבין'], 16: ['ידעון'], 19: ['תאבדון'], 20: ['תאבדון', 'תשמעון']}   # THE PARAGOGIC NUN eight — the book's densest chapter after 4
# THE RECEIPT FINDER'S RULE on the chapter (register_census.receipts: as (k/834) commanded (6680) the LORD (3068) within three; or according to all (k/3605) that (834) commanded (6680) the LORD (3068)) — NO SEAT
def receipt_seats(ch):
    outv = []
    for v in range(1, len([k for k in by if k[0] == 'Deut' and k[1] == ch]) + 1):
        s = byraw[('Deut', ch, v)]
        for i, lm in enumerate(s):
            if lm.startswith('k/834') and i + 1 < len(s) and s[i + 1].startswith('6680') and any(x.startswith('3068') for x in s[i + 2:i + 5]): outv.append(v); break
            if lm.startswith('k/3605') and i + 3 < len(s) and s[i + 1].startswith('834') and s[i + 2].startswith('6680') and s[i + 3].startswith('3068'): outv.append(v); break
    return outv
assert receipt_seats(8) == [] and receipt_seats(5) == [12, 16, 32] and receipt_seats(1) == [3, 19, 41], (receipt_seats(8), receipt_seats(5), receipt_seats(1))   # the finder's rule replicated: chapter 5's three receipts and chapter 1's three found (1:19 the CHAPTER seat the probes list — typed from the fast checker's print), chapter 8 none — "which I command you" the giving
# THE KIN DIFFED (the DB's tokens): the shared runs between the chapter's verses and their first tellings — the readback's measures
assert SHARED(('Deut', 8, 1), ('Deut', 4, 1)) == ['ובאתם', 'וירשתם', 'את', 'הארץ', 'אשר'] and SHARED(('Deut', 8, 1), ('Deut', 11, 8)) == ['כל', 'המצוה', 'אשר', 'אנכי', 'מצוך', 'היום'] and SHARED(('Deut', 8, 2), ('Deut', 29, 4)) == ['ארבעים', 'שנה', 'במדבר'] and SHARED(('Deut', 8, 2), ('Exod', 16, 4)) == ['אם', 'לא']
assert SHARED(('Deut', 8, 3), ('Exod', 16, 15)) == ['כי', 'לא'] and SHARED(('Deut', 8, 3), ('Deut', 8, 16)) == ['ידעון', 'אבתיך', 'למען'] and SHARED(('Deut', 8, 4), ('Deut', 29, 4)) == ['לא', 'בלתה'] and SHARED(('Deut', 8, 5), ('Deut', 1, 31)) == ['איש', 'את', 'בנו']
assert SHARED(('Deut', 8, 7), ('Exod', 3, 8)) == ['אל', 'ארץ', 'טובה'] and SHARED(('Deut', 8, 10), ('Deut', 6, 11)) == ['ואכלת', 'ושבעת'] and SHARED(('Deut', 8, 11), ('Deut', 6, 12)) == ['השמר', 'לך', 'פן', 'תשכח', 'את', 'יהוה'] and SHARED(('Deut', 8, 13), ('Deut', 17, 17)) == ['וכסף', 'וזהב']
assert SHARED(('Deut', 8, 14), ('Deut', 5, 6)) == ['מארץ', 'מצרים', 'מבית', 'עבדים'] and SHARED(('Deut', 8, 14), ('Deut', 13, 11)) == ['יהוה', 'אלהיך', 'המוציאך', 'מארץ', 'מצרים', 'מבית', 'עבדים'] and SHARED(('Deut', 8, 15), ('Deut', 1, 19)) == ['והנורא'] and SHARED(('Deut', 8, 15), ('Exod', 17, 6)) == ['מים']
assert SHARED(('Deut', 8, 16), ('Exod', 16, 35)) == [] and SHARED(('Deut', 8, 18), ('Deut', 7, 12)) == ['אשר', 'נשבע', 'לאבתיך'] and SHARED(('Deut', 8, 19), ('Deut', 4, 26)) == ['כי', 'אבד', 'תאבדון'] and SHARED(('Deut', 8, 19), ('Deut', 6, 14)) == ['אחרי', 'אלהים', 'אחרים'] and SHARED(('Deut', 8, 20), ('Deut', 28, 45)) == ['בקול', 'יהוה'] and DIFF(('Deut', 8, 3), ('Deut', 8, 16))[1] == ('delete', ['ידעת', 'ולא'], [])
# THE PHRASE CENSUSES (the crowns) — F1's facts: the frame
assert P('כל', 'המצוה') == ['Deut 11:22', 'Deut 11:8', 'Deut 15:5', 'Deut 19:9', 'Deut 27:1', 'Deut 5:31', 'Deut 6:25', 'Deut 8:1'] and len(P('אשר', 'אנכי', 'מצוך', 'היום', books=('Deut',))) == 18 and P('למען', 'תחיון') + P('למען', 'תחיה') + P('למען', 'תחיו') == ['Deut 5:33', 'Deut 8:1', 'Deut 16:20', 'Deut 30:19', 'Amos 5:14', 'Deut 4:1', 'Jer 35:7'] and U('ורביתם') == ['Deut 8:1'] and P('ובאתם', 'וירשתם') == ['Deut 11:8', 'Deut 4:1', 'Deut 8:1']
assert len(LEMV('7650', books=('Deut',))) == 33 and [x for x, l in zip(W8(1), byl[('Deut', 8, 1)]) if l == '7621'] == [] and [x for x, l in zip(W8(18), byl[('Deut', 8, 18)]) if l == '7621'] == [] and P('אשר', 'נשבע', 'לאבתיך') == ['Deut 6:10', 'Deut 7:12', 'Deut 7:13', 'Deut 8:18', 'Exod 13:5']
# F2's facts: the forty years, the test, the humbling, the manna, not by bread alone, the garment and the foot, the discipline, walk and fear
assert U('וזכרת') == ['1Sam 25:31', 'Deut 15:15', 'Deut 16:12', 'Deut 24:18', 'Deut 24:22', 'Deut 5:15', 'Deut 8:18', 'Deut 8:2', 'Ezek 16:61'] and P('את', 'כל', 'הדרך') == ['Deut 8:2'] and U('הליכך', 'הוליכך', 'ואולך', 'המוליכך') == ['Amos 2:10', 'Deut 29:4', 'Deut 8:15', 'Deut 8:2', 'Josh 24:3', 'Lev 26:13']
assert [v for v in range(1, 21) if 'במדבר' in W8(v)] == [2, 15, 16] and [(s, x) for s, x, m in LEMT('6031 b', books=('Deut',))] == [('Deut 8:2', 'ענתך'), ('Deut 8:3', 'ויענך'), ('Deut 8:16', 'ענתך'), ('Deut 21:14', 'עניתה'), ('Deut 22:24', 'ענה'), ('Deut 22:29', 'ענה'), ('Deut 26:6', 'ויענונו')]
TEST_SEATS = [(s, x) for s, x, m in LEMT('5254', books=T)]
assert TEST_SEATS == [('Deut 4:34', 'הנסה'), ('Deut 6:16', 'תנסו'), ('Deut 6:16', 'נסיתם'), ('Deut 8:2', 'לנסתך'), ('Deut 8:16', 'נסתך'), ('Deut 13:4', 'מנסה'), ('Deut 28:56', 'נסתה'), ('Deut 33:8', 'נסיתו'), ('Exod 15:25', 'נסהו'), ('Exod 16:4', 'אנסנו'), ('Exod 17:2', 'תנסון'), ('Exod 17:7', 'נסתם'), ('Exod 20:20', 'נסות'), ('Gen 22:1', 'נסה'), ('Num 14:22', 'וינסו')]
WHETHER = [f'{b} {c}:{v}' for (b, c, v), ws in by.items() if [x for x, _ in ws][-2:] == ['אם', 'לא']]
assert P('לדעת', 'את', 'אשר', 'בלבבך') == ['Deut 8:2'] and WHETHER == ['Deut 8:2', 'Exod 16:4', 'Gen 24:21', 'Gen 27:21', 'Gen 37:32', 'Judg 2:22', 'Num 11:23'] and P('התשמר', 'מצותו') == ['Deut 8:2'] and [(s, x) for s, x, m in LEMT('8104', books=('Deut',)) if m and m.startswith('HTi')] == [('Deut 8:2', 'התשמר')]
MANNA_SEATS = [(s, x) for s, x, m in LEMT('4478 a')]
assert MANNA_SEATS == [('Deut 8:3', 'המן'), ('Deut 8:16', 'מן'), ('Exod 16:31', 'מן'), ('Exod 16:33', 'מן'), ('Exod 16:35', 'המן'), ('Exod 16:35', 'המן'), ('Josh 5:12', 'המן'), ('Josh 5:12', 'מן'), ('Neh 9:20', 'ומנך'), ('Num 11:6', 'המן'), ('Num 11:7', 'והמן'), ('Num 11:9', 'המן'), ('Ps 78:24', 'מן')] and P('ידעון', 'אבתיך') == ['Deut 8:16', 'Deut 8:3']
assert P('לא', 'על', 'הלחם', 'לבדו') == ['Deut 8:3'] and P('כל', 'מוצא', 'פי', 'יהוה') == ['Deut 8:3'] and P('יחיה', 'האדם') == ['Deut 8:3', 'Eccl 11:8'] and P('וחי', 'בהם') == ['Ezek 20:11', 'Ezek 20:13', 'Ezek 20:21', 'Lev 18:5'] and len(P('פי', 'יהוה', books=T)) == 25
GARMENT = P('שמלתך', 'לא', 'בלתה') + P('שלמתיהם', 'לא', 'בלו'); SWELL = [(s, x) for s, x, m in LEMT('1216')]
assert GARMENT == ['Deut 8:4', 'Neh 9:21'] and [(s, x) for s, x, m in LEMT('1086', books=T)] == [('Deut 8:4', 'בלתה'), ('Deut 29:4', 'בלו'), ('Deut 29:4', 'בלתה'), ('Gen 18:12', 'בלתי')] and SWELL == [('Deut 8:4', 'בצקה'), ('Neh 9:21', 'בצקו')]   # "did not swell" — the verb's TWO seats in the Bible
assert P('כאשר', 'ייסר', 'איש', 'את', 'בנו') == ['Deut 8:5'] and [(s, x) for s, x, m in LEMT('3256', books=T)] == [('Deut 4:36', 'ליסרך'), ('Deut 8:5', 'ייסר'), ('Deut 8:5', 'מיסרך'), ('Deut 21:18', 'ויסרו'), ('Deut 22:18', 'ויסרו'), ('Lev 26:18', 'ליסרה'), ('Lev 26:23', 'תוסרו'), ('Lev 26:28', 'ויסרתי')] and P('איש', 'את', 'בנו') == ['2Kgs 23:10', 'Deut 1:31', 'Deut 8:5']
assert P('ללכת', 'בדרכיו') == ['1Kgs 2:3', 'Deut 30:16', 'Deut 8:6'] and P('וליראה', 'אתו') == ['Deut 8:6'] and sorted(set(P('ליראה', 'את', 'יהוה', books=('Deut',)))) == ['Deut 10:12', 'Deut 14:23', 'Deut 17:19', 'Deut 31:13', 'Deut 6:24']
# F3's facts: the good land, the waters, the seven species, honey, poverty and lack, iron and copper, eat and be satisfied and bless
GOOD_LAND = sorted(P('ארץ', 'טובה') + P('הארץ', 'הטובה') + P('הארץ', 'הטבה') + P('ארץ', 'טבה'))
assert GOOD_LAND == ['1Chr 28:8', 'Deut 11:17', 'Deut 1:35', 'Deut 3:25', 'Deut 4:21', 'Deut 4:22', 'Deut 6:18', 'Deut 8:10', 'Deut 8:7', 'Deut 9:6', 'Exod 3:8', 'Josh 23:16'] and P('נחלי', 'מים') == ['Deut 10:7', 'Deut 8:7', 'Jer 31:9'] and P('עינת', 'ותהמת') == ['Deut 8:7'] and U('תהמת', 'ותהמת', books=T) == ['Deut 8:7', 'Exod 15:5', 'Exod 15:8'] and P('בבקעה', 'ובהר') == ['Deut 8:7']
SPECIES = ('2406', '8184', '1612', '8384', '7416', '2132', '1706')
SPC = Counter(s for lem in SPECIES for s in LEMV(lem))
SEVEN_SEATS = [s for s, n in SPC.items() if n >= 7]; THREE_OR_MORE = sorted((s, n) for s, n in SPC.items() if n >= 3)
assert P('ארץ', 'חטה', 'ושערה') == ['Deut 8:8'] and P('ארץ', 'זית', 'שמן', 'ודבש') == ['Deut 8:8'] and SEVEN_SEATS == ['Deut 8:8'] and THREE_OR_MORE == [('Deut 8:8', 7), ('Hab 3:17', 3), ('Hag 2:19', 4), ('Jer 41:8', 3), ('Joel 1:12', 3), ('Num 20:5', 3)] and [lemma_of('Deut', 8, 8, x)[0] for x in W8(8)] == ['776', '2406', '8184', '1612', '8384', '7416', '776', '2132', '8081', '1706']
MILK_HONEY = len(P('זבת', 'חלב', 'ודבש'))
assert MILK_HONEY == 20 and [v for v in range(1, 21) if 'חלב' in W8(v)] == [] and [(s, x) for s, x, m in LEMT('4544')] == [('Deut 8:9', 'במסכנת')] and P('לא', 'תחסר', 'כל') == ['Deut 8:9'] and P('לא', 'חסרת', 'דבר') == ['Deut 2:7'] and len(LEMT('2637', books=T)) == 7
IRON = U('ברזל', 'וברזל', 'הברזל', books=('Deut',)); COPPER = U('נחשת', 'ונחשת', books=('Deut',))
assert P('אשר', 'אבניה', 'ברזל') == ['Deut 8:9'] and IRON == ['Deut 19:5', 'Deut 27:5', 'Deut 28:23', 'Deut 28:48', 'Deut 33:25', 'Deut 3:11', 'Deut 4:20', 'Deut 8:9'] and COPPER == ['Deut 28:23', 'Deut 33:25', 'Deut 8:9'] and [(s, x) for s, x, m in LEMT('2672', books=T)] == [('Deut 6:11', 'חצובים'), ('Deut 6:11', 'חצבת'), ('Deut 8:9', 'תחצב')]
EAT_SAT = sorted(P('ואכלת', 'ושבעת') + P('תאכל', 'ושבעת') + P('ואכל', 'ושבע') + P('ואכלו', 'ושבעו'))
assert P('ואכלת', 'ושבעת', 'וברכת') == ['Deut 8:10'] and EAT_SAT == ['Deut 11:15', 'Deut 14:29', 'Deut 31:20', 'Deut 6:11', 'Deut 8:10', 'Deut 8:12'] and P('וברכת', 'את', 'יהוה') == ['Deut 8:10'] and P('הארץ', 'הטבה', 'אשר', 'נתן', 'לך') == ['Deut 8:10'] and P('אשר', 'נתן', 'לך', books=('Deut',)) == ['Deut 12:15', 'Deut 16:17', 'Deut 26:11', 'Deut 28:53', 'Deut 8:10']
# F4's facts: take heed lest, the triad, the growth, silver and gold, the heart lifted, the exodus formula
TAKE_HEED = P('השמר', 'לך', 'פן')
assert TAKE_HEED == ['Deut 12:13', 'Deut 12:19', 'Deut 12:30', 'Deut 15:9', 'Deut 6:12', 'Deut 8:11', 'Exod 34:12', 'Gen 24:6', 'Gen 31:24'] and len([1 for s, x, m in LEMT('8104', books=T) if m and m.startswith('HVNv')]) == 17 and P('פן', 'תשכח', 'את', 'יהוה') == ['Deut 6:12', 'Deut 8:11']
FORGET_LORD = sorted(P('תשכח', 'את', 'יהוה') + P('ושכחת', 'את', 'יהוה') + P('שכחו', 'את', 'יהוה') + P('וישכחו', 'את', 'יהוה'))
assert FORGET_LORD == ['1Sam 12:9', 'Deut 6:12', 'Deut 8:11', 'Deut 8:14', 'Deut 8:19', 'Jer 3:21', 'Judg 3:7'] and len(LEMT('7911', books=('Deut',))) == 14 and [(s, x) for s, x, m in LEMT('7911') if m == 'HVqa'] == [('Deut 8:19', 'שכח')]
TRIAD = sorted(set(LEMV('4687')) & (set(LEMV('2706')) | set(LEMV('2708'))) & set(LEMV('4941')))
assert P('מצותיו', 'ומשפטיו', 'וחקתיו') == ['Deut 8:11'] and len(TRIAD) == 17 and [s for s in TRIAD if s.startswith('Deut')] == ['Deut 11:1', 'Deut 26:17', 'Deut 30:16', 'Deut 5:31', 'Deut 6:1', 'Deut 7:11', 'Deut 8:11']
assert P('פן', 'תאכל', 'ושבעת') == ['Deut 8:12'] and P('ובתים', 'טובים', 'תבנה', 'וישבת') == ['Deut 8:12'] and P('בית', 'תבנה', 'ולא', 'תשב', 'בו') == ['Deut 28:30'] and P('ובקרך', 'וצאנך') + P('בקרך', 'וצאנך') == ['Deut 8:13', 'Deut 12:17', 'Deut 14:23']
SILVER_GOLD = sorted(P('וכסף', 'וזהב', books=T) + P('כסף', 'וזהב', books=T))
assert SILVER_GOLD == ['Deut 17:17', 'Deut 29:16', 'Deut 7:25', 'Deut 8:13', 'Gen 24:35', 'Num 22:18', 'Num 24:13'] and P('וכסף', 'וזהב', 'ירבה') + P('וכסף', 'וזהב', 'לא', 'ירבה') == ['Deut 8:13', 'Deut 17:17'] and [x for x, l in zip(W8(13), byl[('Deut', 8, 13)]) if l == '7235 a'] == ['ירבין', 'ירבה', 'ירבה']
HEART_LIFTED = [s for s in LEMV('7311 a') if any(x.startswith(('לבב', 'לבו', 'לבם', 'לבך', 'ולבב', 'ולבו', 'ולבם')) for x in words(*SEAT(s)))]
assert P('ורם', 'לבבך') == ['Deut 8:14'] and P('לבלתי', 'רום', 'לבבו') == ['Deut 17:20'] and HEART_LIFTED == ['Dan 11:12', 'Dan 12:7', 'Deut 17:20', 'Deut 1:28', 'Deut 8:14', 'Ezek 31:10', 'Hos 13:6', 'Job 17:4'] and P('ושכחת', 'את', 'יהוה', 'אלהיך') == ['Deut 8:14']
HOUSE_BONDAGE = P('מבית', 'עבדים')
assert P('המוציאך', 'מארץ', 'מצרים', 'מבית', 'עבדים') == ['Deut 13:11', 'Deut 8:14'] and HOUSE_BONDAGE == ['Deut 13:11', 'Deut 13:6', 'Deut 5:6', 'Deut 6:12', 'Deut 7:8', 'Deut 8:14', 'Exod 13:14', 'Exod 13:3', 'Exod 20:2', 'Jer 34:13', 'Josh 24:17', 'Judg 6:8'] and U('המוציאך', 'המוציא', 'המוציאם', 'המוצא', books=T) == ['Deut 13:11', 'Deut 13:6', 'Deut 8:14', 'Deut 8:15', 'Exod 6:7', 'Lev 22:33']
# F5's facts: the wilderness, the serpents, the rock of flint, the manna to do you good, my power, the covenant established
GREAT_TERRIBLE = sorted(set(P('הגדול', 'והנורא') + P('הגדל', 'והנורא')))
assert GREAT_TERRIBLE == ['Dan 9:4', 'Deut 1:19', 'Deut 8:15', 'Joel 3:4', 'Mal 3:23', 'Neh 1:5', 'Neh 4:8'] and P('נחש', 'שרף') + P('הנחשים', 'השרפים') == ['Deut 8:15', 'Num 21:6'] and lemma_of('Deut', 8, 15, 'שרף') == ['8314 a'] and lemma_of('Num', 21, 8, 'שרף') == ['8314 a']
SCORPION = [(s, x) for s, x, m in LEMT('6137')]; THIRST = [(s, x) for s, x, m in LEMT('6774')]; NO_WATER = sorted(set(P('אשר', 'אין', 'מים') + P('ואין', 'מים') + P('אין', 'מים')))
assert SCORPION == [('1Kgs 12:11', 'בעקרבים'), ('1Kgs 12:14', 'בעקרבים'), ('2Chr 10:11', 'בעקרבים'), ('2Chr 10:14', 'בעקרבים'), ('Deut 8:15', 'ועקרב'), ('Ezek 2:6', 'עקרבים')] and THIRST == [('Deut 8:15', 'וצמאון'), ('Isa 35:7', 'וצמאון'), ('Ps 107:33', 'לצמאון')] and NO_WATER == ['Deut 8:15', 'Exod 17:1', 'Jer 38:6', 'Num 21:5', 'Zech 9:11']
FLINT = [(s, x) for s, x, m in LEMT('2496')]
assert P('המוציא', 'לך', 'מים', 'מצור', 'החלמיש') == ['Deut 8:15'] and FLINT == [('Deut 8:15', 'החלמיש'), ('Deut 32:13', 'מחלמיש'), ('Isa 50:7', 'כחלמיש'), ('Job 28:9', 'בחלמיש'), ('Ps 114:8', 'חלמיש')] and lemma_of('Deut', 8, 15, 'מצור') == ['6697'] and lemma_of('Exod', 17, 6, 'הצור') == ['6697'] and lemma_of('Num', 20, 8, 'הסלע') == ['5553', '5553'] and lemma_of('Num', 20, 11, 'הסלע') == ['5553']   # THE TWO ROCKS' TWO WORDS — Exodus' tzur (17:6, 8:15), Numbers' sela (20:8-11)
END_SEATS = [(s, x) for s, x, m in LEMT('319', books=T)]
assert P('המאכלך', 'מן', 'במדבר') == ['Deut 8:16'] and P('להיטבך', 'באחריתך') == ['Deut 8:16'] and END_SEATS == [('Deut 4:30', 'באחרית'), ('Deut 8:16', 'באחריתך'), ('Deut 11:12', 'אחרית'), ('Deut 31:29', 'באחרית'), ('Deut 32:20', 'אחריתם'), ('Deut 32:29', 'לאחריתם'), ('Gen 49:1', 'באחרית'), ('Num 23:10', 'אחריתי'), ('Num 24:14', 'באחרית'), ('Num 24:20', 'ואחריתו')]
assert P('ואמרת', 'בלבבך') == ['Deut 8:17', 'Isa 49:21'] and P('כחי', 'ועצם', 'ידי') == ['Deut 8:17'] and P('עשה', 'לי', 'את', 'החיל', 'הזה') == ['Deut 8:17'] and P('כי', 'הוא', 'הנתן', 'לך', 'כח', 'לעשות', 'חיל') == ['Deut 8:18'] and sorted(P('לעשות', 'חיל') + P('עשה', 'חיל') + P('יעשה', 'חיל') + P('עשו', 'חיל') + P('נעשה', 'חיל')) == ['Deut 8:18', 'Num 24:18', 'Prov 31:29', 'Ps 108:14', 'Ps 118:15', 'Ps 118:16', 'Ps 60:14']
ESTABLISH_COV = len([s for s in LEMV('6965 b') if s in LEMV('1285')])
assert P('למען', 'הקים', 'את', 'בריתו') == ['Deut 8:18'] and ESTABLISH_COV == 23 and P('כיום', 'הזה', books=('Deut',)) == ['Deut 10:15', 'Deut 29:27', 'Deut 2:30', 'Deut 4:20', 'Deut 4:38', 'Deut 8:18'] and len(P('כיום', 'הזה')) == 21
# F6's facts: if you surely forget, other gods, serve and bow, I testify, surely perish, like the nations, because, hearken
assert P('והיה', 'אם', 'שכח', 'תשכח') == ['Deut 8:19'] and P('והלכת', 'אחרי', 'אלהים', 'אחרים') == ['Deut 8:19'] and len(P('אחרי', 'אלהים', 'אחרים')) == 16 and len(P('אלהים', 'אחרים', books=('Deut',))) == 17 and P('ועבדתם', 'והשתחוית', 'להם') == ['Deut 8:19']
BOWSERVE = [(s, [x for x, l in zip(words(*SEAT(s)), byl[SEAT(s)]) if l in ('5647', '7812')]) for s in sorted(set(LEMV('5647', books=T)) & set(LEMV('7812', books=T)))]
assert BOWSERVE == [('Deut 11:16', ['ועבדתם', 'והשתחויתם']), ('Deut 17:3', ['ויעבד', 'וישתחו']), ('Deut 29:25', ['ויעבדו', 'וישתחוו']), ('Deut 30:17', ['והשתחוית', 'ועבדתם']), ('Deut 4:19', ['והשתחוית', 'ועבדתם']), ('Deut 5:9', ['תשתחוה', 'תעבדם']), ('Deut 8:19', ['ועבדתם', 'והשתחוית']), ('Exod 20:5', ['תשתחוה', 'תעבדם']), ('Exod 23:24', ['תשתחוה', 'תעבדם']), ('Gen 27:29', ['יעבדוך', 'וישתחו', 'וישתחוו'])], BOWSERVE
SERVE_FIRST = [s for s, l in BOWSERVE if l[0].lstrip('ו').startswith(('עבד', 'יעבד', 'תעבד'))]
TESTIFY = [(s, x) for s, x, m in LEMT('5749 b', books=T)]
assert P('העדתי', 'בכם', 'היום') == ['Deut 8:19'] and TESTIFY == [('Deut 4:26', 'העידתי'), ('Deut 8:19', 'העדתי'), ('Deut 30:19', 'העידתי'), ('Deut 31:28', 'ואעידה'), ('Deut 32:46', 'מעיד'), ('Exod 19:21', 'העד'), ('Exod 19:23', 'העדתה'), ('Exod 21:29', 'והועד'), ('Gen 43:3', 'העד'), ('Gen 43:3', 'העד')] and P('כי', 'אבד', 'תאבדון') == ['Deut 30:18', 'Deut 4:26', 'Deut 8:19'] and [(s, x) for s, x, m in LEMT('6') if m == 'HVqa'] == [('Deut 4:26', 'אבד'), ('Deut 8:19', 'אבד'), ('Deut 30:18', 'אבד')]
HEEL = [(s, m) for s, x, m in LEMT('6118') if s.startswith(('Deut', 'Gen', 'Num'))]
assert P('כגוים', 'אשר', 'יהוה', 'מאביד', 'מפניכם') == ['Deut 8:20'] and P('כן', 'תאבדון') == ['Deut 8:20'] and HEEL == [('Deut 7:12', 'HNcmsc'), ('Deut 8:20', 'HNcmsc'), ('Gen 22:18', 'HNcmsa'), ('Gen 26:5', 'HNcmsa'), ('Num 14:24', 'HC')] and len(LEMT('6118')) == 15 and P('עקב', 'לא', 'תשמעון') == ['Deut 8:20']
HEARKEN = P('בקול', 'יהוה', 'אלהיך', books=('Deut',)) + P('בקול', 'יהוה', 'אלהיכם', books=('Deut',))
assert HEARKEN == ['Deut 13:19', 'Deut 15:5', 'Deut 27:10', 'Deut 28:1', 'Deut 28:15', 'Deut 28:2', 'Deut 28:45', 'Deut 28:62', 'Deut 30:10', 'Deut 8:20'] and sorted(set(P('לא', 'תשמעון', 'בקול') + P('לא', 'תשמע', 'בקול') + P('לא', 'שמעת', 'בקול', books=('Deut',)))) == ['Deut 28:15', 'Deut 28:45', 'Deut 28:62', 'Deut 8:20']
# THE TAPE'S FIRST TELLINGS the chapter reads back (the ink of the seats the readback names — the tape's lines found on the running world at CU4/CU8)
assert words('Exod', 16, 4)[:3] == ['ויאמר', 'יהוה', 'אל'] and words('Exod', 16, 4)[-2:] == ['אם', 'לא'] and words('Exod', 16, 13)[:1] == ['ויהי'] and words('Exod', 12, 51)[:6] == ['ויהי', 'בעצם', 'היום', 'הזה', 'הוציא', 'יהוה'] and words('Exod', 17, 6)[:2] == ['הנני', 'עמד'] and words('Num', 21, 6)[:2] == ['וישלח', 'יהוה']
assert words('Num', 14, 26)[:2] == ['וידבר', 'יהוה'] and N('Num', 14, 34) == [40, 40] and words('Gen', 22, 16)[:2] == ['ויאמר', 'בי'] and words('Gen', 26, 3)[:1] == ['גור'] and words('Gen', 50, 24)[:2] == ['ויאמר', 'יוסף'] and words('Deut', 4, 26)[:1] == ['העידתי'] and words('Deut', 7, 1)[:2] == ['כי', 'יביאך'] and words('Num', 20, 10)[:2] == ['ויקהלו', 'משה']
# THE STATE'S LEDGER SCAN (the fifth form's assertion at build): the one database's run_ledger — no effect on israel_people naming a garment, clothing, a shoe or a swelling (CU7 runs the same scan on the running world)
_WDB = _os.path.join(_ROOT, 'World', 'journal', 'data', 'world.sqlite')
def ledger_scan(entity, pattern):
    """the effects on an entity in the one database whose name or value matches the pattern — None where the database is not built (a fresh clone before build_world)"""
    if not _os.path.exists(_WDB): return None
    c_ = sqlite3.connect('file:%s?mode=ro' % _WDB, uri=True)
    rx = re.compile(pattern, re.I)
    return sorted({e for e, v in c_.execute("SELECT DISTINCT effect, value FROM run_ledger WHERE entity=?", (entity,)).fetchall() if rx.search('%s %s' % (e, v if v is not None else ''))})
STATE_WORDS = r'\b(garment|garments|clothing|clothes|cloth|shoe|shoes|sandal|sandals|swell|swelled|swollen|wore out|wear out)\b'   # word-bounded: the first pass's bare 'wore' matched 'swore' in the blessings' value (the fast checker's print)
GARMENT_SCAN = ledger_scan('israel_people', STATE_WORDS)
assert GARMENT_SCAN in ([], None), GARMENT_SCAN   # no entry names the state on Israel: the SUPPLIED grade's ground
# THE READBACK'S DELTAS RECOMPUTED (the reference rows' measures — the token counts and the longest shared run, from the DB); the tuple typed from the fast checker's print
DELTA = {
    'live_8_1': (LEN('Deut', 8, 1), LEN('Deut', 4, 1), len(SHARED(('Deut', 8, 1), ('Deut', 4, 1)))),
    'forty_8_2': (LEN('Deut', 8, 2), LEN('Num', 14, 33) + LEN('Num', 14, 34), len(SHARED(('Deut', 8, 2), ('Num', 14, 33)))),
    'whether_8_2': (LEN('Deut', 8, 2), LEN('Exod', 16, 4), len(SHARED(('Deut', 8, 2), ('Exod', 16, 4)))),
    'manna_8_3': (LEN('Deut', 8, 3), LEN('Exod', 16, 15), len(SHARED(('Deut', 8, 3), ('Exod', 16, 15)))),
    'garment_8_4': (LEN('Deut', 8, 4), LEN('Deut', 29, 4), len(SHARED(('Deut', 8, 4), ('Deut', 29, 4)))),
    'discipline_8_5': (LEN('Deut', 8, 5), LEN('Deut', 1, 31), len(SHARED(('Deut', 8, 5), ('Deut', 1, 31)))),
    'land_8_7_9': (LEN('Deut', 8, 7) + LEN('Deut', 8, 8) + LEN('Deut', 8, 9), LEN('Deut', 6, 10) + LEN('Deut', 6, 11), len(SHARED(('Deut', 8, 7), ('Deut', 6, 3)))),
    'lack_8_9': (LEN('Deut', 8, 9), LEN('Deut', 2, 7), len(SHARED(('Deut', 8, 9), ('Deut', 2, 7)))),
    'heed_8_11': (LEN('Deut', 8, 11), LEN('Deut', 6, 12), len(SHARED(('Deut', 8, 11), ('Deut', 6, 12)))),
    'growth_8_12_13': (LEN('Deut', 8, 12) + LEN('Deut', 8, 13), LEN('Deut', 6, 10) + LEN('Deut', 6, 11), len(SHARED(('Deut', 8, 12), ('Deut', 6, 11)))),
    'exodus_8_14': (LEN('Deut', 8, 14), LEN('Exod', 12, 51), LEN('Deut', 5, 6), len(SHARED(('Deut', 8, 14), ('Deut', 5, 6)))),
    'serpents_8_15': (LEN('Deut', 8, 15), LEN('Num', 21, 6), len(SHARED(('Deut', 8, 15), ('Num', 21, 6)))),
    'rock_8_15': (LEN('Deut', 8, 15), LEN('Exod', 17, 6), LEN('Num', 20, 11), len(SHARED(('Deut', 8, 15), ('Exod', 17, 6)))),
    'manna_8_16': (LEN('Deut', 8, 16), LEN('Deut', 8, 3), len(SHARED(('Deut', 8, 16), ('Deut', 8, 3)))),
    'oath_8_18': (LEN('Deut', 8, 18), LEN('Gen', 22, 16), LEN('Deut', 7, 12), len(SHARED(('Deut', 8, 18), ('Deut', 7, 12)))),
    'gods_8_19': (LEN('Deut', 8, 19), LEN('Deut', 5, 9), len(SHARED(('Deut', 8, 19), ('Deut', 5, 9)))),
    'testify_8_19': (LEN('Deut', 8, 19), LEN('Deut', 4, 26), len(SHARED(('Deut', 8, 19), ('Deut', 4, 26)))),
    'nations_8_20': (LEN('Deut', 8, 20), LEN('Deut', 7, 1), len(SHARED(('Deut', 8, 20), ('Deut', 7, 1)))),
}
assert DELTA == {'live_8_1': (19, 24, 5), 'forty_8_2': (23, 33, 2), 'whether_8_2': (23, 22, 2), 'manna_8_3': (28, 24, 2), 'garment_8_4': (10, 14, 2), 'discipline_8_5': (12, 21, 3), 'land_8_7_9': (43, 40, 1), 'lack_8_9': (18, 22, 1), 'heed_8_11': (16, 12, 6), 'growth_8_12_13': (18, 40, 1), 'exodus_8_14': (11, 13, 9, 4), 'serpents_8_15': (16, 13, 0), 'rock_8_15': (16, 20, 15, 1), 'manna_8_16': (13, 28, 3), 'oath_8_18': (20, 18, 20, 3), 'gods_8_19': (20, 21, 2), 'testify_8_19': (20, 27, 3), 'nations_8_20': (13, 27, 1)}, DELTA   # typed from the fast checker's print (ch8_fastcheck1.out)

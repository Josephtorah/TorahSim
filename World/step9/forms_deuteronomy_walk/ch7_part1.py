#!/usr/bin/env python3
# DEUTERONOMY 7:1-26 — THE SEVEN NATIONS: THE BAN, NO FAVOR, NO PITY AND THE ABOMINATION INTO THE HOUSE COMPILED FOR THE FIRST TIME (THE CODE'S FOUR
# HOLES), THE OLD CODE SAID AGAIN FOR THE NEW PLACE — THE READBACK ON THE KIN (THE DEUTERONOMY WALK sitting 5b, 2026-09-18; World/step9/DEUTERONOMY_WALK.md
# "Sitting 5b"; the state doc's #194-#195). THE CHAPTER'S OWN LINES: no runner held a cell for the ban on the seven nations, for "show them no favor",
# for "your eye shall not pity" or for "you shall not bring an abomination into your house" (the recon's regex over all sixty-one runners) — F1, F4 and
# F6 compile them from the ink with the answer sheet Mishnah Avodah Zarah 1:1-4:12, Kiddushin 3:12 and the Talmud's rows as the compile rules (the
# docket deu_07_vaetchanan_ekev_exam_2026-09-18.md, 520 rows read whole); commanded valued devote_the_seven_nations a DEBIT on Israel OPEN to Joshua,
# favor_barred, pity_barred and house_abomination_barred BLOCKS, blessings_for_hearing a conditional HEAVEN entry (the design's name blessing_promised was Abram's, the registry decided), covenant_barred and intermarriage_barred
# (Exodus 23:32's and 34:16's effects) written on the tape for the first time — all at the chapter's own day (40, 11, 1), NO marker (the speech
# continuing from chapter 6's own-day lines). THE READBACK ON THE KIN (THE LOOP's step 6, the laws' form L1-L6 of 3b run on ANOTHER chapter's code):
# the row's first telling is a KIN CELL — Exodus 23's (ordinances.land), 34's (erection.covenant), Numbers 33's (journeys.the_command), the two words'
# (covenant_at_horeb) — graded by CALL, or a tape line found by kind and first verse; twenty-one REFERENCE ROWS (VERBATIM 4 / VARIANT 5 / EXPANDED 8 /
# TURNED 3 / SHORTENED 1), never a second write; what has no first telling is THE CODE'S HOLE, compiled here. The daemon law_seven_nations given_at
# Deut 7:1, installed_by boot (the Deuteronomy daemons' form). Six cells; every token probed (zero-report law); effects on every cell (the effects law);
# nineteen DATA rows (the three the docket added: the calf's agency, the ban's condition, the pity's row). Reading ledger:
# logic/oral_triage/deu_07_vaetchanan_ekev_2026-09-17.md (29 sources, 6 claims); the exam's docket: deu_07_vaetchanan_ekev_exam_2026-09-18.md
# (520 rows READ WHOLE FROM THE START: LAW 145 / DERIVATION 34 / DISPUTE 110 / CONTEXT 156 / OUTSIDE 75).

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
import cold_run_ordinances as OR                # THE EDGE: seven_nations -> ordinances CALL, reference (the angel's clauses Exodus 23:20-33 — no covenant, the snare, bread and water, no barren, the hornet, little by little, the borders; the readback's rows on the kin)
import cold_run_erection as ER                 # THE EDGE: seven_nations -> erection CALL, reference (the renewed covenant 34:11-16 — the six-name list in seven orders, no covenant, the daughters both ways, the child follows the mother, the four objects; the exam's Mishnah Avodah Zarah credits)
import cold_run_journeys as JO                 # THE EDGE: seven_nations -> journeys CALL, reference (the dispossession Numbers 33:50-56 — drive out, the three objects; the demolition's OPEN debit the reference row's entry)
import cold_run_covenant_at_horeb as CH        # THE EDGE: seven_nations -> covenant_at_horeb CALL, reference (the second word's visiting clause at 7:9-10; the tenth word's verb at 7:25 — other_gods_barred and coveting_barred stand)
import cold_run_decalogue as DC                # THE EDGE: seven_nations -> decalogue CALL, reference (the first copies 20:5-6, 20:17; the third word's cell beside the oath's noun at 7:8)
import cold_run_exodus_story as ES             # THE EDGE: seven_nations -> exodus_story CALL, reference (the treasure at 19:5-6, the plagues, the sea, the healer, the trials, Amalek's phrase — the tape's lines read back)
import cold_run_obey_horeb as OH               # THE EDGE: seven_nations -> obey_horeb CALL, reference (4:37's 'because he loved your fathers', 4:35/39's 'he is God', 4:38's dispossession)
import cold_run_hear_o_israel as HI            # THE EDGE: seven_nations -> hear_o_israel CALL, reference (the triad's third seat 7:11; 6:15's 'in your midst' pair at 7:21)
import cold_run_opening_speech as OS           # THE EDGE: seven_nations -> opening_speech CALL, reference (1:28's fear read back at 7:17; the east's devotings on the tape)
import cold_run_mamre as MA                    # THE EDGE: seven_nations -> mamre CALL, reference (the oath's lines sworn_by_himself 22:16-18 and oath_upheld 26:3-5)
import cold_run_joseph as JS                   # THE EDGE: seven_nations -> joseph CALL, reference (the oath's third line visitation_promised 50:24)
import cold_run_balak as BK                    # THE EDGE: seven_nations -> balak CALL, reference (the Shittim exhibit — Numbers 25:1-3, the marriage bar's reason on the tape)
import cold_run_shemini as SH                  # THE EDGE: seven_nations -> shemini CALL, reference (Leviticus 11:43's detesting verb — the idol's impurity in the creeping animal's form)

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
def W7(v): return words('Deut', 7, v)
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

# ---- THE INK, computed (the parser and the tokens; the reading's facts the expectations — every assert PROVEN at the reading, ch7_ink.py) ----
SPAN = [(7, v) for v in range(1, 27)]
PARSED = {(c, v): ink_numbers(verse_words('Deut', c, v)) for (c, v) in SPAN if ink_numbers(verse_words('Deut', c, v))}
def MARKS(c, v): return [t for t in verse_words('Deut', c, v) if t[-1] in '#~^%@|*']
def N(b, c, v): return ink_numbers(verse_words(b, c, v))
assert PARSED == {(7, 1): [7], (7, 9): [1000]} and {(c, v): ink_ordinals(verse_words('Deut', c, v)) for (c, v) in SPAN if ink_ordinals(verse_words('Deut', c, v))} == {} and [((c, v), t) for (c, v) in SPAN for t in MARKS(c, v)] == [((7, 8), 'השבעה*')], PARSED   # TWO number verses — the list counted, the thousand generations; the oath's noun starred; no ordinal; NO GAP
assert N('1Chr', 16, 15) == [1000] and N('Ps', 105, 8) == [1000] and N('Exod', 20, 6) == [] and N('Deut', 5, 10) == [] and N('Exod', 34, 7) == [] and N('Exod', 23, 29) == [1] and N('Exod', 23, 30) == [] and N('Deut', 20, 17) == [] and N('Josh', 3, 10) == [] and N('Josh', 24, 11) == [] and N('Exod', 23, 23) == [] and N('Exod', 34, 11) == []
assert lemma_of('Deut', 7, 8, 'השבעה') == ['7621'] and PT('Deut', 7, 8, 'השבעה') == ['הַשְּׁבֻעָה'] and lemma_of('Deut', 7, 8, 'נשבע') == ['7650'] and lemma_of('Deut', 7, 1, 'שבעה') == ['7651'] and lemma_of('Deut', 7, 9, 'לאלף') == ['505'] and morphs('Deut', 7, 1)[22] == 'HAcmsa' and morphs('Deut', 7, 9)[14] == 'HR/Acbsa'
SEVEN_COUNT = PARSED[(7, 1)][0]; THOUSAND = PARSED[(7, 9)][0]
NG7 = [x for x, m in wm('Deut', 7, 1) if 'Ng' in m]
assert NG7 == ['החתי', 'והגרגשי', 'והאמרי', 'והכנעני', 'והפרזי', 'והחוי', 'והיבוסי'] and len(NG7) == 7 == SEVEN_COUNT   # the numeral's witness in the verse itself
SEVEN = {'2850', '1622', '567', '3669 a', '6522', '2340', '2983'}   # the seven nations' lemmas (Hittite, Girgashite, Amorite, Canaanite, Perizzite, Hivite, Jebusite) — from 7:1's DB row
assert [lemma_of('Deut', 7, 1, x)[0] for x in NG7] == ['2850', '1622', '567', '3669 a', '6522', '2340', '2983']
NAT = {f'{b} {c}:{v}': set(l for l in byl[(b, c, v)] if l in SEVEN) for (b, c, v) in by}
SEVEN_LISTS = sorted(s for s, ls in NAT.items() if len(ls) == 7); SIX_LISTS = sorted(s for s, ls in NAT.items() if len(ls) == 6)
assert SEVEN_LISTS == ['Deut 7:1', 'Josh 24:11', 'Josh 3:10'] and SIX_LISTS == ['Deut 20:17', 'Exod 23:23', 'Exod 33:2', 'Exod 34:11', 'Exod 3:17', 'Exod 3:8', 'Josh 11:3', 'Josh 12:8', 'Josh 9:1', 'Judg 3:5', 'Neh 9:8'], (SEVEN_LISTS, SIX_LISTS)   # the seven-name lists: this verse and Joshua's two; the six-name lists eleven — the Girgashite absent from every Exodus list
assert LEMV('1622') == ['1Chr 1:14', 'Deut 7:1', 'Gen 10:16', 'Gen 15:21', 'Josh 24:11', 'Josh 3:10', 'Neh 9:8']   # the Girgashite's seven seats
TOK = sum(len(W7(v)) for v in range(1, 27)); LET = sum(len(x) for v in range(1, 27) for x in W7(v))
assert TOK == 412 and LET == 1637 and (sum(len(W7(v)) for v in range(1, 12)), sum(len(W7(v)) for v in range(12, 27))) == (176, 236), TOK   # the portion's edge at 7:12 inside the unit
assert byw[('Deut', 7, 9)][13] == 'x-ketiv' and W7(9)[13] == 'מצותו' and Counter(wt for v in range(1, 27) for wt in byw[('Deut', 7, v)]) == Counter({None: 411, 'x-ketiv': 1}) and byw[('Deut', 5, 10)][-1] == 'x-ketiv' and words('Deut', 5, 10)[-1] == 'מצותו' and words('Exod', 20, 6)[-1] == 'מצותי'   # THE WRITTEN/READ PAIR at 7:9 — 5:10's kin
# THE FRAMES AND THE REGISTER: NO divine frame, NO "saying" — the whole chapter Moses' voice; the narrative verbs two (7:7, 7:8); no imperative; five infinitive absolutes; the prohibitions eleven second-person and five third
NUM = {v: (sum(1 for m in morphs('Deut', 7, v) if m and '2mp' in m), sum(1 for m in morphs('Deut', 7, v) if m and '2ms' in m)) for v in range(1, 27)}
SG_ONLY = [v for v, (p, s) in NUM.items() if s and not p]; PL_ONLY = [v for v, (p, s) in NUM.items() if p and not s]; BOTH = [v for v, (p, s) in NUM.items() if p and s]; NEITHER = [v for v, (p, s) in NUM.items() if not p and not s]
assert SG_ONLY == [1, 2, 3, 6, 9, 11, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 26] and PL_ONLY == [5, 7] and BOTH == [4, 8, 12, 25] and NEITHER == [10]
DIV = [v for v in range(1, 27) if any(V in ('ויאמר', 'וידבר') and W7(v)[i + 1] == 'יהוה' for i, V in enumerate(W7(v)[:-1]))]
assert DIV == [] and [v for v in range(1, 27) if 'לאמר' in W7(v)] == [] and [v for v in range(1, 27) if 'משה' in W7(v) or 'ישראל' in W7(v)] == []
REG = {v: [x for x, m in wm('Deut', 7, v) if m and re.search(r'^HC/V.w', m)] for v in range(1, 27) if any(m and re.search(r'^HC/V.w', m) for _, m in wm('Deut', 7, v))}
assert REG == {7: ['ויבחר'], 8: ['ויפדך']}, REG
IMPER = {v: [x for x, m in wm('Deut', 7, v) if m and re.match(r'^HV.?.?v', m)] for v in range(1, 27) if any(m and re.match(r'^HV.?.?v', m) for _, m in wm('Deut', 7, v))}
INFA = {v: [(x, m) for x, m in wm('Deut', 7, v) if m and re.match(r'^H(?:C/)?V.a$', m)] for v in range(1, 27) if any(m and re.match(r'^H(?:C/)?V.a$', m) for _, m in wm('Deut', 7, v))}
assert IMPER == {} and INFA == {2: [('החרם', 'HVha')], 4: [('מהר', 'HVpa')], 18: [('זכר', 'HVqa')], 22: [('מהר', 'HVpa')], 26: [('שקץ', 'HVpa'), ('ותעב', 'HC/Vpa')]}, (IMPER, INFA)
WEQATAL_V = sorted(v for v in range(1, 27) if any(m and re.search(r'^HC/V.q', m) for _, m in wm('Deut', 7, v)))
assert WEQATAL_V == [1, 2, 4, 9, 11, 12, 13, 15, 16, 22, 23, 24, 25, 26] and [x for x, m in wm('Deut', 7, 13) if re.search(r'^HC/V.q', m)] == ['ואהבך', 'וברכך', 'והרבך', 'וברך']
NEG = ('לא', 'ולא')
PRO = {v: [(W7(v)[i + 1], morphs('Deut', 7, v)[i + 1]) for i, x in enumerate(W7(v)[:-1]) if x in NEG and morphs('Deut', 7, v)[i + 1] and morphs('Deut', 7, v)[i + 1].startswith('HV')] for v in range(1, 27) if any(x in NEG for x in W7(v))}
assert PRO == {2: [('תכרת', 'HVqi2ms'), ('תחנם', 'HVqi2ms/Sp3mp')], 3: [('תתחתן', 'HVti2ms'), ('תתן', 'HVqi2ms'), ('תקח', 'HVqi2ms')], 7: [], 10: [('יאחר', 'HVpi3ms')], 14: [('יהיה', 'HVqi3ms')], 15: [('ישימם', 'HVqi3ms/Sp3mp')], 16: [('תחס', 'HVqi3fs'), ('תעבד', 'HVqi2ms')], 18: [('תירא', 'HVqi2ms')], 21: [('תערץ', 'HVqi2ms')], 22: [('תוכל', 'HVqi2ms')], 24: [('יתיצב', 'HVti3ms')], 25: [('תחמד', 'HVqi2ms')], 26: [('תביא', 'HVhi2ms')]}, PRO
assert sum(1 for v in PRO for _, m in PRO[v] if 'i2' in m) == 11 and sum(1 for v in PRO for _, m in PRO[v] if 'i3' in m) == 5   # eleven in the second person; five in the third (7:16's "your eye shall not pity" the eye's — 3fs)
CASE_TOK = {f'7:{v}': [x for x in W7(v) if x in ('כי', 'אם', 'ואם', 'או', 'פן')] for v in range(1, 27) if any(x in ('כי', 'אם', 'ואם', 'או', 'פן') for x in W7(v))}
assert CASE_TOK == {'7:1': ['כי'], '7:4': ['כי'], '7:5': ['כי', 'אם'], '7:6': ['כי'], '7:7': ['כי'], '7:8': ['כי'], '7:9': ['כי'], '7:16': ['כי'], '7:17': ['כי'], '7:21': ['כי'], '7:22': ['פן'], '7:25': ['פן', 'כי'], '7:26': ['כי']}
ONE_CS = {v: [(x, m) for x, m in wm('Deut', 7, v) if m and '1cs' in m] for v in range(1, 27) if any(m and '1cs' in m for _, m in wm('Deut', 7, v))}
assert ONE_CS == {4: [('מאחרי', 'HR/R/Sp1cs')], 11: [('אנכי', 'HPp1cs')], 17: [('ממני', 'HR/Sp1cs'), ('אוכל', 'HVqi1cs')]} and not any('1cp' in (m or '') for v in range(1, 27) for _, m in wm('Deut', 7, v))   # the first person God's (7:4, 7:11) and the doubter's (7:17)
NAME = Counter(x for v in range(1, 27) for x in W7(v) if x in ('יהוה', 'ויהוה', 'ביהוה', 'כיהוה', 'ליהוה'))
YG_SG = [v for v in range(1, 27) for i in range(len(W7(v)) - 1) if W7(v)[i:i + 2] == ['יהוה', 'אלהיך']]
assert NAME == Counter({'יהוה': 19, 'ליהוה': 1}) and YG_SG == [1, 2, 6, 9, 12, 16, 18, 19, 19, 20, 21, 22, 23, 25] and [v for v in range(1, 27) for i in range(len(W7(v)) - 1) if W7(v)[i:i + 2] == ['יהוה', 'אלהיכם']] == []
assert {v: [x for x in W7(v) if x in ('פרעה', 'לפרעה', 'מצרים')] for v in (8, 15, 18)} == {8: ['פרעה', 'מצרים'], 15: ['מצרים'], 18: ['לפרעה', 'מצרים']}
# THE KIN DIFFED (the DB's tokens): the shared runs between the chapter's verses and their first tellings — the readback's measures
assert DIFF(('Deut', 7, 6), ('Deut', 14, 2)) == [('replace', ['בך'], ['ובך']), ('delete', ['אלהיך'], [])] and SHARED(('Deut', 7, 6), ('Deut', 14, 2)) == ['להיות', 'לו', 'לעם', 'סגלה', 'מכל', 'העמים', 'אשר', 'על', 'פני', 'האדמה']
assert SHARED(('Deut', 7, 9), ('Exod', 20, 6)) == ['ולשמרי'] and SHARED(('Deut', 7, 9), ('Deut', 5, 10)) == ['ולשמרי', 'מצותו'] and SHARED(('Deut', 7, 2), ('Exod', 23, 32)) == ['לא', 'תכרת', 'להם'] and SHARED(('Deut', 7, 3), ('Exod', 34, 16)) == []
assert SHARED(('Deut', 7, 22), ('Exod', 23, 30)) == ['מעט', 'מעט'] and SHARED(('Deut', 7, 20), ('Exod', 23, 28)) == ['את', 'הצרעה'] and SHARED(('Deut', 7, 24), ('Josh', 1, 5)) == ['לא', 'יתיצב', 'איש'] and SHARED(('Deut', 7, 25), ('Exod', 20, 17)) == ['לא', 'תחמד'] and SHARED(('Deut', 7, 25), ('Deut', 5, 21)) == ['תחמד']
assert SHARED(('Deut', 7, 13), ('Deut', 28, 4)) == ['פרי', 'בטנך', 'ופרי', 'אדמתך'] and SHARED(('Deut', 7, 5), ('Deut', 12, 3)) == ['תשרפון', 'באש'] and SHARED(('Deut', 7, 19), ('Deut', 29, 2)) == ['הגדלת', 'אשר', 'ראו', 'עיניך'] and SHARED(('Deut', 7, 21), ('Deut', 6, 15)) == ['יהוה', 'אלהיך', 'בקרבך']
assert SHARED(('Deut', 7, 4), ('Deut', 11, 17)) == ['וחרה', 'אף', 'יהוה', 'בכם'] and SHARED(('Deut', 7, 16), ('Exod', 23, 33)) == ['תעבד', 'את', 'אלהיהם', 'כי'] and SHARED(('Deut', 7, 18), ('Deut', 20, 1)) == ['לא', 'תירא', 'מהם'] and SHARED(('Deut', 7, 11), ('Deut', 6, 1)) == ['המצוה'] and SHARED(('Deut', 7, 23), ('Deut', 7, 2)) == ['ונתנם', 'יהוה', 'אלהיך', 'לפניך']
# THE PHRASE CENSUSES (the crowns) — F1's facts: the seven nations, the ban, no covenant, no favor, no marriage, the four objects
assert P('שבעה', 'גוים') == ['Deut 7:1'] and U('שבעה', books=('Deut',)) == ['Deut 16:9', 'Deut 7:1'] and P('רבים', 'ועצומים', 'ממך') + P('גדלים', 'ועצמים', 'ממך') == ['Deut 7:1', 'Deut 4:38', 'Deut 9:1'] and len(P('גוים', 'רבים')) == 15
assert U('ונשל') == ['Deut 19:5', 'Deut 7:1', 'Deut 7:22'] and P('החרם', 'תחרים') + P('החרם', 'תחרימם') == ['Deut 7:2', 'Deut 20:17'] and P('לא', 'תכרת', 'להם', 'ברית') + P('לא', 'תכרת', 'להם', 'ולאלהיהם', 'ברית') == ['Deut 7:2', 'Exod 23:32'] and P('פן', 'תכרת', 'ברית') == ['Exod 34:12', 'Exod 34:15']
assert U('תחנם') == ['Deut 7:2'] and len([1 for s, x, m in LEMT('2603 a', books=T) if m.startswith('HV')]) == 6 and lemma_of('Deut', 7, 2, 'תחנם') == ['2603 a']
assert U('תתחתן', 'התחתנו', 'התחתן', 'ותתחתנו', 'התחתנתם', 'תתחתנו') == ['1Sam 18:21', '1Sam 18:22', '1Sam 18:23', 'Deut 7:3'] and LEMV('2859 b', books=T) == ['Deut 7:3', 'Gen 34:9'] and P('בתך', 'לא', 'תתן', 'לבנו') == ['Deut 7:3'] and P('ולקחת', 'מבנתיו', 'לבניך') == ['Exod 34:16']
assert P('כי', 'יסיר', 'את', 'בנך', 'מאחרי') == ['Deut 7:4'] and P('וחרה', 'אף', 'יהוה', 'בכם') == ['Deut 11:17', 'Deut 7:4', 'Josh 23:16'] and P('והשמידך', 'מהר') == ['Deut 7:4'] and U('מהר', books=('Deut',)) == ['Deut 28:20', 'Deut 33:2', 'Deut 4:26', 'Deut 7:22', 'Deut 7:4', 'Deut 9:12', 'Deut 9:16', 'Deut 9:3']
assert P('מזבחתיהם', 'תתצו') + P('מזבחתם', 'תתצון') == ['Deut 7:5', 'Exod 34:13'] and U('ואשירהם', 'ואשריהם', 'אשריהם', 'ואשריו', 'אשריו', books=T) == ['Deut 12:3', 'Deut 7:5', 'Exod 34:13'] and U('תגדעון', 'תגדע', 'וגדעתם', 'תגדעו', books=T) == ['Deut 12:3', 'Deut 7:5'] and P('תשרפון', 'באש') == ['Deut 12:3', 'Deut 7:25', 'Deut 7:5']
assert sorted(LEMV('6456', books=T) + LEMV('6459', books=T)) == ['Deut 12:3', 'Deut 27:15', 'Deut 4:16', 'Deut 4:23', 'Deut 4:25', 'Deut 5:8', 'Deut 7:25', 'Deut 7:5', 'Exod 20:4', 'Lev 26:1']
# F2's facts: the holy people, the treasure, chose you, the fewest, the love, the oath, redeemed
assert P('עם', 'קדוש') + P('עם', 'קדש') == ['Deut 14:2', 'Deut 14:21', 'Deut 7:6', 'Dan 12:7', 'Deut 26:19'] and U('סגלה', 'לסגלה', 'וסגלה') == ['1Chr 29:3', 'Deut 14:2', 'Deut 26:18', 'Deut 7:6', 'Exod 19:5', 'Mal 3:17'] and P('בך', 'בחר', 'יהוה', 'אלהיך') == ['Deut 7:6'] and P('מכל', 'העמים', 'אשר', 'על', 'פני', 'האדמה') == ['Deut 14:2', 'Deut 7:6']
assert U('מרבכם') == ['Deut 7:7'] and LEMV('2836 a') == ['1Kgs 9:19', '2Chr 8:6', 'Deut 10:15', 'Deut 21:11', 'Deut 7:7', 'Gen 34:8', 'Isa 38:17', 'Ps 91:14'] and P('ויבחר', 'בכם') == ['Deut 7:7'] and P('אתם', 'המעט', 'מכל', 'העמים') == ['Deut 7:7'] and U('מעט', 'המעט', 'מעטים', 'ומעט', books=('Deut',)) == ['Deut 26:5', 'Deut 28:38', 'Deut 28:62', 'Deut 7:22', 'Deut 7:7']
OATH_NOUN = [(s, x) for s, x, m in LEMT('7621', books=T)]
assert P('מאהבת', 'יהוה', 'אתכם') == ['Deut 7:8'] and P('השבעה', 'אשר', 'נשבע', 'לאבתיכם') == ['Deut 7:8'] and OATH_NOUN == [('Deut 7:8', 'השבעה'), ('Exod 22:10', 'שבעת'), ('Gen 24:8', 'משבעתי'), ('Gen 26:3', 'השבעה'), ('Lev 5:4', 'בשבעה'), ('Num 5:21', 'בשבעת'), ('Num 5:21', 'ולשבעה'), ('Num 30:3', 'שבעה'), ('Num 30:11', 'בשבעה'), ('Num 30:14', 'שבעת')]
assert P('הוציא', 'יהוה', 'אתכם', 'ביד', 'חזקה') == ['Deut 7:8'] and P('ויפדך', 'מבית', 'עבדים') == ['Deut 7:8'] and [(s, x) for s, x, m in LEMT('6299', books=('Deut',))] == [('Deut 7:8', 'ויפדך'), ('Deut 9:26', 'פדית'), ('Deut 13:6', 'והפדך'), ('Deut 15:15', 'ויפדך'), ('Deut 21:8', 'פדית'), ('Deut 24:18', 'ויפדך')] and P('מיד', 'פרעה', 'מלך', 'מצרים') == ['Deut 7:8']
OATH_SEATS = [v for v in range(1, 27) if 'נשבע' in W7(v)]
assert OATH_SEATS == [8, 12, 13] and P('אשר', 'נשבע', 'לאבתיך', books=('Deut',)) == S_('Deut 6:10', 'Deut 7:12', 'Deut 7:13', 'Deut 8:18')
# F3's facts: the faithful God, he is God, the covenant and the kindness, a thousand generations, the hater repaid, the triad
assert P('האל', 'הנאמן') == ['Deut 7:9'] and P('יהוה', 'אלהיך', 'הוא', 'האלהים') + P('יהוה', 'הוא', 'האלהים') == ['Deut 7:9', '1Kgs 18:39', '1Kgs 8:60', '2Chr 33:13', 'Deut 4:35', 'Deut 4:39'] and P('שמר', 'הברית', 'והחסד') == ['1Kgs 8:23', '2Chr 6:14', 'Dan 9:4', 'Deut 7:9'] and P('הברית', 'ואת', 'החסד') == ['Deut 7:12']
assert P('לאהביו', 'ולשמרי', 'מצותו') == ['Deut 7:9'] and P('לאהבי', 'ולשמרי', 'מצותי') == ['Exod 20:6'] and P('לאלף', 'דור') == ['1Chr 16:15', 'Deut 7:9', 'Ps 105:8'] and U('לאלפים') == ['Deut 5:10', 'Exod 20:6', 'Exod 34:7', 'Jer 32:18'] and U('אלף', 'לאלף', 'ואלף', books=('Deut',)) == ['Deut 1:11', 'Deut 32:30', 'Deut 7:9']
assert P('ומשלם', 'לשנאיו', 'אל', 'פניו') == ['Deut 7:10'] and U('להאבידו') == ['2Kgs 24:2', 'Deut 7:10'] and P('לא', 'יאחר') == ['Deut 7:10', 'Hab 2:3'] and U('לשנאי', 'לשנאיו', 'שנאיו', 'לשנאו', 'ולשנאיו', 'משנאיו', books=T) == ['Deut 5:9', 'Deut 7:10', 'Exod 20:5', 'Gen 24:60'] and P('פקד', 'עון', 'אבת') + P('פקד', 'עון', 'אבות') == ['Exod 20:5', 'Deut 5:9', 'Exod 34:7', 'Num 14:18']
TRIAD = [s for s in U('המצוה', books=('Deut',)) if s in U('והמשפטים', 'המשפטים', books=('Deut',))]
assert P('ושמרת', 'את', 'המצוה', 'ואת', 'החקים', 'ואת', 'המשפטים') == ['Deut 7:11'] and TRIAD == ['Deut 5:31', 'Deut 6:1', 'Deut 7:11'] and len(P('אשר', 'אנכי', 'מצוך', 'היום', books=('Deut',))) == 18
# F4's facts: because (the heel), the covenant kept, the blessing's list, the flock's word, no barren, the diseases, consume, no pity, the snare
HEEL = [(s, m) for s, x, m in LEMT('6118') if s.startswith(('Deut', 'Gen', 'Num'))]
assert P('והיה', 'עקב', 'תשמעון') == ['Deut 7:12'] and HEEL == [('Deut 7:12', 'HNcmsc'), ('Deut 8:20', 'HNcmsc'), ('Gen 22:18', 'HNcmsa'), ('Gen 26:5', 'HNcmsa'), ('Num 14:24', 'HC')] and U('תשמעון', books=('Deut',)) == ['Deut 18:15', 'Deut 1:17', 'Deut 7:12', 'Deut 8:20'] and P('ושמר', 'יהוה', 'אלהיך', 'לך', 'את', 'הברית') == ['Deut 7:12']
assert P('ואהבך', 'וברכך', 'והרבך') == ['Deut 7:13'] and P('פרי', 'בטנך', 'ופרי', 'אדמתך') == ['Deut 28:18', 'Deut 28:4', 'Deut 7:13'] and P('דגנך', 'ותירשך', 'ויצהרך') == ['Deut 11:14', 'Deut 12:17', 'Deut 7:13'] and P('שגר', 'אלפיך', 'ועשתרת', 'צאנך') == ['Deut 28:51', 'Deut 7:13'] and U('שגר', 'ושגר') == ['Deut 28:18', 'Deut 28:4', 'Deut 28:51', 'Deut 7:13', 'Exod 13:12']
MORPH_TAG = [(s, x, m) for s, x, m in LEMT('6251')]
assert MORPH_TAG == [('Deut 7:13', 'ועשתרת', 'HC/Np'), ('Deut 28:4', 'ועשתרות', 'HC/Np'), ('Deut 28:18', 'ועשתרות', 'HC/Np'), ('Deut 28:51', 'ועשתרת', 'HC/Np')]   # the flock's "young" tagged a NAME (Np) at its four seats — the goddess's homograph in the DB's morph
assert P('ברוך', 'תהיה', 'מכל', 'העמים') == ['Deut 7:14'] and P('לא', 'יהיה', 'בך', 'עקר', 'ועקרה') == ['Deut 7:14'] and U('עקר', 'עקרה', 'ועקרה', 'ועקר', books=T) == ['Deut 7:14', 'Exod 23:26', 'Gen 11:30', 'Gen 25:21', 'Gen 29:31'] and P('לא', 'תהיה', 'משכלה', 'ועקרה') == ['Exod 23:26']
assert P('והסיר', 'יהוה', 'ממך', 'כל', 'חלי') == ['Deut 7:15'] and P('מדוי', 'מצרים', 'הרעים') == ['Deut 7:15'] and U('מדוי', 'מדוה', 'ומדוה', 'במדוה') == ['Deut 28:60', 'Deut 7:15'] and P('כל', 'המחלה', 'אשר', 'שמתי', 'במצרים') == ['Exod 15:26'] and P('אשר', 'ידעת', books=('Deut',)) == ['Deut 7:15']
PITY_SEATS = sorted(P('לא', 'תחס', 'עינך') + P('ולא', 'תחס', 'עינך') + P('לא', 'תחוס', 'עינך') + P('ולא', 'תחוס', 'עינך') + P('לא', 'תחס', 'עינכם'))
assert P('ואכלת', 'את', 'כל', 'העמים') == ['Deut 7:16'] and PITY_SEATS == ['Deut 13:9', 'Deut 19:13', 'Deut 19:21', 'Deut 25:12', 'Deut 7:16'] and P('כי', 'מוקש', 'הוא', 'לך') == ['Deut 7:16'] and U('מוקש', 'למוקש', 'ולמוקש', 'מוקשים', books=T) == ['Deut 7:16', 'Exod 10:7', 'Exod 23:33', 'Exod 34:12'] and P('תעבד', 'את', 'אלהיהם') == ['Deut 7:16', 'Exod 23:33']
# F5's facts: the doubt, remember Pharaoh, the trials, the hornet, terrified, in your midst, little by little, the beasts, the confusion, the kings, the name, no man shall stand
assert P('כי', 'תאמר', 'בלבבך') == ['Deut 7:17'] and P('ואמרת', 'בלבבך') == ['Deut 8:17', 'Isa 49:21'] and P('רבים', 'הגוים', 'האלה', 'ממני') == ['Deut 7:17'] and P('איכה', 'אוכל') == ['Deut 7:17'] and U('להורישם', books=T) == ['Deut 7:17'] and U('להורישם') == ['Deut 7:17', 'Josh 15:63']
assert P('לא', 'תירא', 'מהם') == ['Deut 20:1', 'Deut 7:18'] and P('זכר', 'תזכר') == ['Deut 7:18'] and [(s, m) for s, x, m in LEMT('2142') if x == 'זכר' and m == 'HVqa'] == [('Deut 7:18', 'HVqa'), ('Jer 31:20', 'HVqa')] and P('עשה', 'יהוה', 'אלהיך', 'לפרעה', 'ולכל', 'מצרים') + P('עשה', 'יהוה', 'לפרעה') == ['Deut 7:18', 'Exod 18:8']
assert P('המסת', 'הגדלת') == ['Deut 7:19'] and U('מסת', 'המסת', 'במסת', 'ומסת') == ['Deut 16:10', 'Deut 4:34', 'Deut 7:19'] and lemma_of('Deut', 7, 19, 'המסת') == ['4531 b'] and lemma_of('Deut', 16, 10, 'מסת') != ['4531 b']   # the freewill offering's "measure" (16:10) the homograph
SIGNS_WONDERS = sorted(P('והאתת', 'והמפתים') + P('האתת', 'והמפתים') + P('האתות', 'והמופתים') + P('באתות', 'ובמופתים') + P('אתת', 'ומפתים'))
assert SIGNS_WONDERS == ['Deut 29:2', 'Deut 34:11', 'Deut 7:19', 'Jer 32:21', 'Neh 9:10'] and P('והיד', 'החזקה', 'והזרע', 'הנטויה') == ['Deut 7:19'] and P('ביד', 'חזקה', 'ובזרע', 'נטויה') == ['Deut 26:8', 'Deut 5:15'] and P('כן', 'יעשה', 'יהוה', 'אלהיך', 'לכל', 'העמים') == ['Deut 7:19'] and P('אשר', 'אתה', 'ירא', 'מפניהם') == ['Deut 7:19']
HORNET = U('הצרעה', 'צרעה')
assert HORNET == ['2Chr 11:10', 'Deut 7:20', 'Exod 23:28', 'Josh 19:41', 'Josh 24:12', 'Judg 13:25', 'Judg 16:31', 'Judg 18:8'] and P('ושלחתי', 'את', 'הצרעה', 'לפניך') == ['Exod 23:28'] and P('עד', 'אבד', 'הנשארים', 'והנסתרים') == ['Deut 7:20'] and U('הנסתרים', 'והנסתרים', 'נסתרים') == ['Deut 7:20']
assert P('לא', 'תערץ', 'מפניהם') == ['Deut 7:21'] and LEMV('6206', books=T) == ['Deut 1:29', 'Deut 20:3', 'Deut 31:6', 'Deut 7:21'] and P('יהוה', 'אלהיך', 'בקרבך') == ['Deut 6:15', 'Deut 7:21', 'Zeph 3:17'] and P('אל', 'גדול', 'ונורא') == ['Deut 7:21'] and P('האל', 'הגדל', 'הגבר', 'והנורא') == ['Deut 10:17']
assert P('מעט', 'מעט') == ['Deut 7:22', 'Exod 23:30'] and P('לא', 'תוכל', 'כלתם', 'מהר') == ['Deut 7:22'] and P('פן', 'תרבה', 'עליך', 'חית', 'השדה') == ['Deut 7:22'] and P('חית', 'השדה', books=T) == ['Deut 7:22', 'Exod 23:11', 'Exod 23:29', 'Gen 2:19', 'Gen 2:20', 'Gen 3:1', 'Gen 3:14', 'Lev 26:22'] and P('בשנה', 'אחת') == ['1Kgs 10:14', '2Chr 9:13', 'Exod 23:29']
assert P('ונתנם', 'יהוה', 'אלהיך', 'לפניך') == ['Deut 7:2', 'Deut 7:23'] and P('והמם', 'מהומה', 'גדלה') == ['Deut 7:23'] and len(U('השמדם', 'השמדך', 'השמדו', 'להשמידם', 'להשמידך')) == 12 and P('ונתן', 'מלכיהם', 'בידך') == ['Deut 7:24'] and P('והאבדת', 'את', 'שמם', 'מתחת', 'השמים') == ['Deut 7:24']
UNDER_HEAVEN = P('מתחת', 'השמים')
assert UNDER_HEAVEN == ['2Kgs 14:27', 'Deut 25:19', 'Deut 29:19', 'Deut 7:24', 'Deut 9:14', 'Exod 17:14', 'Gen 1:9', 'Gen 6:17'] and P('לא', 'יתיצב', 'איש', 'בפניך') + P('לא', 'יתיצב', 'איש', 'לפניך') == ['Deut 7:24', 'Josh 1:5'] and P('תמחה', 'את', 'זכר') + P('מחה', 'אמחה', 'את', 'זכר') + P('ומחה', 'יהוה', 'את', 'שמו') == ['Deut 25:19', 'Exod 17:14', 'Deut 29:19']
# F6's facts: the images burned, not covet, the snare, an abomination to the LORD, into your house, devoted like it, detest and abhor, for it is devoted
assert P('פסילי', 'אלהיהם', 'תשרפון', 'באש') == ['Deut 7:25'] and P('לא', 'תחמד') == ['Deut 7:25', 'Exod 20:17'] and P('ולא', 'תחמד') + P('ולא', 'תתאוה') == ['Deut 5:21', 'Deut 5:21'] and [s for s in P('כסף', 'וזהב') if s in U('תחמד', 'ואחמדם', 'ולקחת', 'ואקחם')] == ['Deut 7:25', 'Zech 6:11'] and P('פן', 'תוקש', 'בו') == ['Deut 7:25']
ABOM_LORD_GOD = sorted(set(P('תועבת', 'יהוה', 'אלהיך'))); ABOM_LORD = sorted(set(P('תועבת', 'יהוה', books=T)))
assert ABOM_LORD_GOD == ['Deut 17:1', 'Deut 22:5', 'Deut 23:19', 'Deut 25:16', 'Deut 7:25'] and ABOM_LORD == ['Deut 12:31', 'Deut 17:1', 'Deut 18:12', 'Deut 22:5', 'Deut 23:19', 'Deut 25:16', 'Deut 27:15', 'Deut 7:25'] and len(set(P('תועבת', 'יהוה'))) == 19
ABOM_DEUT = U('תועבה', 'תועבת', 'התועבה', 'התועבת', 'תועבות', 'התועבות', 'ותועבת', books=('Deut',))
assert ABOM_DEUT == ['Deut 12:31', 'Deut 13:15', 'Deut 14:3', 'Deut 17:1', 'Deut 17:4', 'Deut 18:12', 'Deut 22:5', 'Deut 23:19', 'Deut 24:4', 'Deut 25:16', 'Deut 27:15', 'Deut 7:25', 'Deut 7:26']
DETEST = [(s, x) for s, x, m in LEMT('8262', books=T)]; ABHOR = [(s, x) for s, x, m in LEMT('8581', books=T)]
assert P('ולא', 'תביא', 'תועבה', 'אל', 'ביתך') == ['Deut 7:26'] and P('והיית', 'חרם', 'כמהו') == ['Deut 7:26'] and P('שקץ', 'תשקצנו', 'ותעב', 'תתעבנו') == ['Deut 7:26'] and DETEST == [('Deut 7:26', 'שקץ'), ('Deut 7:26', 'תשקצנו'), ('Lev 11:11', 'תשקצו'), ('Lev 11:13', 'תשקצו'), ('Lev 11:43', 'תשקצו'), ('Lev 20:25', 'תשקצו')] and ABHOR == [('Deut 7:26', 'ותעב'), ('Deut 7:26', 'תתעבנו'), ('Deut 23:8', 'תתעב'), ('Deut 23:8', 'תתעב')] and P('כי', 'חרם', 'הוא') == ['Deut 7:26']
assert lemma_of('Deut', 7, 26, 'חרם') == ['2764 a', '2764 a'] and lemma_of('Deut', 7, 2, 'החרם') == ['2763 a'] and lemma_of('Deut', 7, 2, 'תחרים') == ['2763 a'] and lemma_of('Deut', 20, 17, 'תחרימם') == ['2763 a']   # THE TWO LEMMAS — the ban's verb (7:2, 20:17) and the devoted thing's noun (7:26, 13:18)
# THE TAPE'S FIRST TELLINGS the chapter reads back (the ink of the seats the readback names — the tape's lines found on the running world at CQ4/CQ8)
assert words('Exod', 19, 5)[:3] == ['ועתה', 'אם', 'שמוע'] and words('Exod', 12, 51)[:6] == ['ויהי', 'בעצם', 'היום', 'הזה', 'הוציא', 'יהוה'] and words('Exod', 15, 26)[:2] == ['ויאמר', 'אם'] and words('Exod', 7, 20)[:2] == ['ויעשו', 'כן'] and words('Deut', 5, 28)[:3] == ['וישמע', 'יהוה', 'את'] and words('Deut', 5, 31)[-1] == 'לרשתה'
assert words('Exod', 23, 23)[:2] == ['כי', 'ילך'] and words('Exod', 23, 32)[:2] == ['לא', 'תכרת'] and words('Exod', 34, 16)[:1] == ['ולקחת'] and words('Exod', 34, 13)[:3] == ['כי', 'את', 'מזבחתם'] and words('Num', 33, 52)[:1] == ['והורשתם'] and words('Exod', 17, 14)[:3] == ['ויאמר', 'יהוה', 'אל']
# THE READBACK'S DELTAS RECOMPUTED (the reference rows' measures — the token counts and the longest shared run, from the DB); the tuple typed from the fast checker's print
DELTA = {
    'list_7_1': (LEN('Deut', 7, 1), LEN('Exod', 23, 23), LEN('Exod', 34, 11), len(SHARED(('Deut', 7, 1), ('Exod', 23, 23))), len(SHARED(('Deut', 7, 1), ('Exod', 34, 11)))),
    'covenant_7_2': (LEN('Deut', 7, 2), LEN('Exod', 23, 32), len(SHARED(('Deut', 7, 2), ('Exod', 23, 32)))),
    'marriage_7_3': (LEN('Deut', 7, 3), LEN('Exod', 34, 16), len(SHARED(('Deut', 7, 3), ('Exod', 34, 16)))),
    'objects_7_5': (LEN('Deut', 7, 5), LEN('Exod', 34, 13), LEN('Num', 33, 52), len(SHARED(('Deut', 7, 5), ('Exod', 34, 13)))),
    'treasure_7_6': (LEN('Deut', 7, 6), LEN('Exod', 19, 5) + LEN('Exod', 19, 6), len(SHARED(('Deut', 7, 6), ('Exod', 19, 5))), len(SHARED(('Deut', 7, 6), ('Exod', 19, 6)))),
    'brought_out_7_8': (LEN('Deut', 7, 8), LEN('Exod', 12, 51), len(SHARED(('Deut', 7, 8), ('Exod', 12, 51)))),
    'thousand_7_9': (LEN('Deut', 7, 9), LEN('Exod', 20, 6), LEN('Deut', 5, 10), len(SHARED(('Deut', 7, 9), ('Exod', 20, 6))), len(SHARED(('Deut', 7, 9), ('Deut', 5, 10)))),
    'hater_7_10': (LEN('Deut', 7, 10), LEN('Deut', 5, 9), len(SHARED(('Deut', 7, 10), ('Deut', 5, 9)))),
    'triad_7_11': (LEN('Deut', 7, 11), LEN('Deut', 5, 31), LEN('Deut', 6, 1), len(SHARED(('Deut', 7, 11), ('Deut', 5, 31))), len(SHARED(('Deut', 7, 11), ('Deut', 6, 1)))),
    'because_7_12': (LEN('Deut', 7, 12), LEN('Exod', 19, 5), len(SHARED(('Deut', 7, 12), ('Exod', 19, 5)))),
    'barren_7_14': (LEN('Deut', 7, 14), LEN('Exod', 23, 26), len(SHARED(('Deut', 7, 14), ('Exod', 23, 26)))),
    'diseases_7_15': (LEN('Deut', 7, 15), LEN('Exod', 15, 26), len(SHARED(('Deut', 7, 15), ('Exod', 15, 26)))),
    'snare_7_16': (LEN('Deut', 7, 16), LEN('Exod', 23, 33), len(SHARED(('Deut', 7, 16), ('Exod', 23, 33)))),
    'plagues_7_18_19': (LEN('Deut', 7, 18) + LEN('Deut', 7, 19), sum(LEN('Exod', c, v) for c, v in ((7, 20), (8, 2), (8, 13), (8, 20), (9, 6), (9, 10), (9, 23), (10, 13), (10, 22), (12, 29)))),
    'hornet_7_20': (LEN('Deut', 7, 20), LEN('Exod', 23, 28), len(SHARED(('Deut', 7, 20), ('Exod', 23, 28)))),
    'little_7_22': (LEN('Deut', 7, 22), LEN('Exod', 23, 29) + LEN('Exod', 23, 30), len(SHARED(('Deut', 7, 22), ('Exod', 23, 30)))),
    'kings_7_23_24': (LEN('Deut', 7, 23) + LEN('Deut', 7, 24), LEN('Exod', 23, 27) + LEN('Exod', 23, 31), len(SHARED(('Deut', 7, 23), ('Exod', 23, 27))), len(SHARED(('Deut', 7, 24), ('Josh', 1, 5)))),
    'covet_7_25': (LEN('Deut', 7, 25), LEN('Exod', 20, 17), LEN('Deut', 5, 21), len(SHARED(('Deut', 7, 25), ('Exod', 20, 17)))),
}
assert DELTA == {'list_7_1': (27, 13, 17, 1, 3), 'covenant_7_2': (14, 5, 3), 'marriage_7_3': (11, 12, 0), 'objects_7_5': (14, 10, 19, 1), 'treasure_7_6': (20, 31, 3, 1), 'brought_out_7_8': (22, 13, 2), 'thousand_7_9': (16, 6, 6, 1, 2), 'hater_7_10': (12, 21, 1), 'triad_7_11': (12, 20, 17, 2, 1), 'because_7_12': (20, 17, 1), 'barren_7_14': (10, 9, 1), 'diseases_7_15': (17, 27, 1), 'snare_7_16': (21, 15, 4), 'plagues_7_18_19': (38, 190), 'hornet_7_20': (12, 12, 2), 'little_7_22': (18, 23, 2), 'kings_7_23_24': (24, 36, 1, 3), 'covet_7_25': (19, 15, 16, 2)}, DELTA   # typed from the fast checker's print (ch7_fastcheck1.out)


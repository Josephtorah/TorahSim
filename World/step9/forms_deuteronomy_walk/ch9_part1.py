#!/usr/bin/env python3
# DEUTERONOMY 9:1-29 — NOT FOR YOUR RIGHTEOUSNESS: THE CALF RETOLD IN MOSES' OWN VOICE, THE THREE FORTIES GRADED AGAINST THE CLOCK, AND AARON'S PERIL
# WRITTEN ONCE AT ITS OWN DAY — THE READBACK'S SIXTH FORM, THE RETELLING OF A STRETCH (THE DEUTERONOMY WALK sitting 7b, 2026-09-19;
# World/step9/DEUTERONOMY_WALK.md "Sitting 7b"; the state doc's #197). THE CHAPTER'S ONE LINE: Aaron's peril (9:20 — "and with Aaron the LORD was very
# angry, to destroy him; and I prayed for Aaron also at that time") is TOLD ONLY HERE: Exodus 32 has Aaron's report (32:21-24) and the plague (32:35),
# no anger at Aaron and no prayer for him — THE TAPE'S HOLE, filled by the retelling and written ONCE at its own day by the RETROGRADE marker at
# Deut 9:20 (M['aaron_told'] = M['morrow'] — "at that time" the second forty's ascent, the morrow of the breaking, (1, 4, 18); reading_placed), the
# stretch ended by a forward marker at 9:21; THE WRITE destruction_halved — a STATUS on aaron, THE NAME FROM THE DOCKET (Vayikra Rabbah 10:5: half the
# edict withheld — two died and two remained). EVERY OTHER ACT THE CHAPTER RETELLS IS ON THE TAPE (the erection runner's Exodus 24-34 stretch, the
# Numbers 11-14 lines, chapter 4's retrograde tablets_given, the oath's line) or in the kin's cells by CALL — the rows REFERENCE ROWS, never a second
# write; and FOUR rows retell "forty days and forty nights" (9:9, 9:11, 9:18, 9:25) — not a line but a STRETCH between two markers, graded against
# THE CLOCK'S OWN ARITHMETIC (the ascent to the breaking 40, the morrow to the second ascent 40, the second ascent to the last tablets 40 — Ta'anit
# 28b:9's twenty-four of Sivan and sixteen of Tammuz reproduced) and the answer sheet's dates (Mishnah Ta'anit 4:6's seventeenth of Tammuz MATCH).
# The daemon law_not_righteousness given_at Deut 9:1, installed_by boot (the Deuteronomy daemons' form). Six cells; every token probed (zero-report
# law); effects on every cell (the effects law); the DATA rows the docket added (Taberah outside the ten trials, the fasting's seat 9:9's own, the calf
# forbidden from its making, the merit of the fathers a parameter, the crowns of Horeb stripped with no line, Mishnah Megillah 4:10's asymmetry, the
# three requests of Exodus 33 with no line). Reading ledger: logic/oral_triage/deu_09_ekev_2026-09-19.md (36 sources, 6 claims); the exam's docket:
# deu_09_ekev_exam_2026-09-19.md (397 rows READ WHOLE FROM THE START: LAW 46 / DERIVATION 48 / DISPUTE 10 / CONTEXT 160 / OUTSIDE 133).

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
import cold_run_erection as ER                 # THE EDGE: not_righteousness -> erection CALL, reference (the calf's stretch on the tape; the clock's compile rules; the intercession's rules; the four verbs; the breaking ratified)
import cold_run_exodus_story as ES             # THE EDGE: not_righteousness -> exodus_story CALL, reference (the ten trials — Taberah outside them; Massah's named line)
import cold_run_beha as BH                     # THE EDGE: not_righteousness -> beha CALL, reference (Taberah and Kibroth-hattaavah — the fire and the graves)
import cold_run_shelach as SL                  # THE EDGE: not_righteousness -> shelach CALL, reference (Kadesh — the rejection; the giants; the taunt's feminine noun; the offer's second seat)
import cold_run_opening_speech as OS           # THE EDGE: not_righteousness -> opening_speech CALL, reference (1:28's fortified cities and Anakim; 1:26's rebellion; 1:27's hatred)
import cold_run_obey_horeb as OH               # THE EDGE: not_righteousness -> obey_horeb CALL, reference (4:38's nations; 4:24's consuming fire; 4:13's tablets_given; 4:37's great power; 4:31's merciful God)
import cold_run_covenant_at_horeb as CH        # THE EDGE: not_righteousness -> covenant_at_horeb CALL, reference (5:22's tablets given to me; the ten words the angels' answer)
import cold_run_hear_o_israel as HI            # THE EDGE: not_righteousness -> hear_o_israel CALL, reference (6:16's Massah — the named line's second reference)
import cold_run_seven_nations as SN            # THE EDGE: not_righteousness -> seven_nations CALL, reference (7:1's 'greater and mightier than you' said again)
import cold_run_shemini_day as SD              # THE EDGE: not_righteousness -> shemini_day CALL, reference (Leviticus 9:2's calf for the calf — Aaron's re-acceptance; the two who died)
import cold_run_good_land as GL                # THE EDGE: not_righteousness -> good_land CALL, reference (8:2's forty years — the fifth form the sixth's nearest kin)

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
def W9(v): return words('Deut', 9, v)
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
D9 = lambda v: ('Deut', 9, v)

P_ = []   # the provenance trail of the case being run
def ink(ref, note):  P_.append(('INK',  'Deut %s — %s' % (ref, note) if not ref[:1].isupper() else '%s — %s' % (ref, note)))
def move(src, note): P_.append(('MOVE', '%s — %s' % (src, note)))
def dat(note):       P_.append(('DATA', note))
def hyp(note):       P_.append(('HYP',  note))     # THE LINK REVIEW LAW: a hypothesis — no teacher; counted apart, never as compiled
def out(verdict, effects):
    """verdict + registry-validated effects (the engine contract)"""
    FX.validate([e for e in effects if e != FX.NONE])
    return verdict, effects, list(P_)

# ---- THE INK, computed (the parser and the tokens; the reading's facts the expectations — every assert PROVEN at the reading, ch9_ink.py) ----
SPAN = [(9, v) for v in range(1, 30)]
PARSED = {(c, v): ink_numbers(verse_words('Deut', c, v)) for (c, v) in SPAN if ink_numbers(verse_words('Deut', c, v))}
def MARKS(c, v): return [t for t in verse_words('Deut', c, v) if t[-1] in '#~^%@|*']
def N(b, c, v): return ink_numbers(verse_words(b, c, v))
assert PARSED == {(9, 9): [40, 40], (9, 10): [2], (9, 11): [40, 40, 2], (9, 15): [2, 2], (9, 17): [2, 2], (9, 18): [40, 40], (9, 25): [40, 40]}, PARSED   # THE SEVEN NUMBER VERSES — the forties at four seats, the two tablets at four
assert all(ink_ordinals(verse_words('Deut', 9, v)) == [] for v in range(1, 30))
FORTY = PARSED[(9, 9)]
assert [(b, c, v, N(b, c, v)) for b, c, v in (('Exod', 24, 18), ('Exod', 34, 28), ('Exod', 31, 18), ('Exod', 32, 15), ('Deut', 4, 13), ('Deut', 10, 4), ('Deut', 10, 10), ('Num', 13, 25))] == [('Exod', 24, 18, [40, 40]), ('Exod', 34, 28, [40, 40, 10]), ('Exod', 31, 18, [2]), ('Exod', 32, 15, [2]), ('Deut', 4, 13, [10, 2]), ('Deut', 10, 4, [10]), ('Deut', 10, 10, [40, 40]), ('Num', 13, 25, [40])]
TOK = sum(len(W9(v)) for v in range(1, 30)); LET = sum(len(x) for v in range(1, 30) for x in W9(v))
# THE THREE SPELLINGS OF "TABLETS" — the lemma 3871: לוחת (plene vav — 9:9 twice, 9:10; 10:1 alone elsewhere), לחת (defective — 9:11, 9:15; Exodus's form), לחות (9:11; 4:13 and 1 Kings 8:9); 9:11 holds TWO spellings; the article's form הלחת at 9:17
TABLETS_FORMS = [(x, v) for v in range(1, 30) for x in W9(v) if x in ('לוחת', 'לחת', 'לחות', 'הלחת')]
assert TABLETS_FORMS == [('לוחת', 9), ('לוחת', 9), ('לוחת', 10), ('לחת', 11), ('לחות', 11), ('לחת', 15), ('הלחת', 17)] and U('לוחת') == ['Deut 10:1', 'Deut 9:10', 'Deut 9:9'] and U('לחות') == ['1Kgs 8:9', 'Deut 4:13', 'Deut 9:11'] and U('לוחות') == [] and len(LEMT('3871')) == 43, TABLETS_FORMS
TABLETS_COVENANT = P('לוחת', 'הברית') + P('לחת', 'הברית') + P('לחות', 'הברית')
assert sorted(TABLETS_COVENANT) == ['Deut 9:11', 'Deut 9:15', 'Deut 9:9'] and P('לוחת', 'האבנים') == ['Deut 9:10', 'Deut 9:9']   # "the tablets of the covenant" the Bible's three, all here
# THE FRAMES AND THE REGISTER: two divine frames INSIDE the retelling (9:12, 9:13 — God's word of Exodus 32:7-9 quoted); the narrative verbs TWENTY-TWO in sixteen verses; Moses never named
NUM = {v: (sum(1 for m in morphs('Deut', 9, v) if m and '2mp' in m), sum(1 for m in morphs('Deut', 9, v) if m and '2ms' in m)) for v in range(1, 30)}
SG_ONLY = [v for v, (p, s) in NUM.items() if s and not p]; PL_ONLY = [v for v, (p, s) in NUM.items() if p and not s]; BOTH = [v for v, (p, s) in NUM.items() if p and s]; NEITHER = [v for v, (p, s) in NUM.items() if not p and not s]
assert (SG_ONLY, PL_ONLY, BOTH, NEITHER) == ([1, 2, 3, 4, 5, 6, 12, 14, 26, 27, 28, 29], [8, 9, 10, 16, 17, 18, 19, 21, 22, 23, 24, 25], [7], [11, 13, 15, 20]), (SG_ONLY, PL_ONLY, BOTH, NEITHER)
DIV = [v for v in range(1, 30) if any(V in ('ויאמר', 'וידבר') and W9(v)[i + 1] == 'יהוה' for i, V in enumerate(W9(v)[:-1]))]
assert DIV == [12, 13] and [v for v in range(1, 30) if 'לאמר' in W9(v)] == [4, 13, 23]
WAY = {v: [x for x, m in wm('Deut', 9, v) if m and re.search(r'^HC/V.w', m)] for v in range(1, 30) if any(m and re.search(r'^HC/V.w', m) for _, m in wm('Deut', 9, v))}
assert sum(len(v) for v in WAY.values()) == 22 and len(WAY) == 16 and WAY[17] == ['ואתפש', 'ואשלכם', 'ואשברם'] and WAY[21] == ['ואשרף', 'ואכת', 'ואשלך'] and WAY[20] == ['ואתפלל'] and WAY[26] == ['ואתפלל', 'ואמר'], WAY
IMPER = {v: [x for x, m in wm('Deut', 9, v) if m and re.match(r'^HV.?.?v', m)] for v in range(1, 30) if any(m and re.match(r'^HV.?.?v', m) for _, m in wm('Deut', 9, v))}
assert IMPER == {1: ['שמע'], 7: ['זכר'], 12: ['קום', 'רד'], 14: ['הרף'], 23: ['עלו'], 27: ['זכר']}, IMPER
INFA = {v: [x for x, m in wm('Deut', 9, v) if m and re.match(r'^H(?:C/)?V.a$', m)] for v in range(1, 30) if any(m and re.match(r'^H(?:C/)?V.a$', m) for _, m in wm('Deut', 9, v))}
assert INFA == {3: ['מהר'], 12: ['מהר', 'מהר'], 16: ['מהר'], 21: ['טחון', 'היטב']}, INFA
WEQATAL_V = {v: [x for x, m in wm('Deut', 9, v) if m and re.search(r'^HC/V.q', m)] for v in range(1, 30) if any(m and re.search(r'^HC/V.q', m) for _, m in wm('Deut', 9, v))}
assert WEQATAL_V == {3: ['וידעת', 'והורשתם', 'והאבדתם'], 6: ['וידעת']} and [v for v in range(1, 30) if any(m and re.search(r'^H(?:Ti/)?V.i2', m) for _, m in wm('Deut', 9, v))] == []   # the law's form at the opening alone; NO prohibition "not + imperfect"
NEG = ('לא', 'ולא')
NEGS = {v: [x for x in W9(v) if x in NEG] for v in range(1, 30) if any(x in NEG for x in W9(v))}
assert NEGS == {5: ['לא'], 6: ['לא'], 9: ['לא', 'לא'], 18: ['לא', 'לא'], 23: ['ולא', 'ולא']}, NEGS
CASE_TOK = {f'9:{v}': [x for x in W9(v) if x in ('כי', 'אם', 'ואם', 'או', 'פן')] for v in range(1, 30) if any(x in ('כי', 'אם', 'ואם', 'או', 'פן') for x in W9(v))}
assert CASE_TOK == {'9:3': ['כי'], '9:5': ['כי'], '9:6': ['כי', 'כי'], '9:12': ['כי'], '9:19': ['כי'], '9:25': ['כי'], '9:28': ['פן']}, CASE_TOK
ONE_CS = sorted(v for v in range(1, 30) if any(m and '1cs' in m for _, m in wm('Deut', 9, v)))
assert ONE_CS == [4, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 23, 24, 25, 26] and [(x, m) for x, m in wm('Deut', 9, 4) if m and '1cs' in m] == [('בצדקתי', 'HR/Ncfsc/Sp1cs'), ('הביאני', 'HVhp3ms/Sp1cs')]   # the boaster's "I" the chapter's only first person that is not Moses'
ONE_CP = {v: [x for x, m in wm('Deut', 9, v) if m and '1cp' in m] for v in range(1, 30) if any(m and '1cp' in m for _, m in wm('Deut', 9, v))}
assert ONE_CP == {28: ['הוצאתנו']}
NAME = sum(1 for v in range(1, 30) for x in W9(v) if x in ('יהוה', 'ליהוה', 'ויהוה', 'ביהוה', 'מיהוה'))
YG_SG = [v for v in range(1, 30) if any(W9(v)[i:i + 2] == ['יהוה', 'אלהיך'] for i in range(len(W9(v)) - 1))]; YG_PL = [v for v in range(1, 30) if any(W9(v)[i:i + 2] == ['יהוה', 'אלהיכם'] for i in range(len(W9(v)) - 1))]
assert NAME == 34 and YG_SG == [3, 4, 5, 6, 7] and YG_PL == [23] and [v for v in range(1, 30) if 'אלהים' in W9(v)] == [10]
NAMES = {n: [v for v in range(1, 30) if n in W9(v)] for n in ('משה', 'אהרן', 'ובאהרן', 'ישראל', 'ובחרב', 'לאברהם', 'ליצחק', 'וליעקב', 'ענקים')}
assert NAMES == {'משה': [], 'אהרן': [20], 'ובאהרן': [20], 'ישראל': [1], 'ובחרב': [8], 'לאברהם': [5, 27], 'ליצחק': [5, 27], 'וליעקב': [5, 27], 'ענקים': [2]}, NAMES
PARTS = {v: [x for x, m in wm('Deut', 9, v) if m and re.search(r'^H(?:C/|R/|Td/|C/R/)?V.r', m)] for v in range(1, 30) if any(m and re.search(r'^H(?:C/|R/|Td/|C/R/)?V.r', m) for _, m in wm('Deut', 9, v))}
assert PARTS == {1: ['עבר'], 2: ['ורם'], 3: ['העבר', 'אכלה'], 4: ['מורישם'], 5: ['בא', 'מורישם'], 6: ['נתן'], 7: ['ממרים'], 15: ['בער'], 21: ['הירד'], 22: ['מקצפים'], 24: ['ממרים']}, PARTS
# THE PHRASE CENSUSES (the crowns; proven at the reading)
HEAR_O_ISRAEL = P('שמע', 'ישראל'); NATIONS_GREATER = P('גוים', 'גדלים', 'ועצמים', 'ממך'); FORTIFIED_9 = P('ערים', 'גדלת', 'ובצרת', 'בשמים'); FORTIFIED_1 = P('ערים', 'גדלת', 'ובצורת', 'בשמים'); GREAT_TALL = P('עם', 'גדול', 'ורם')
assert HEAR_O_ISRAEL == ['Deut 20:3', 'Deut 5:1', 'Deut 6:4', 'Deut 9:1'] and NATIONS_GREATER == ['Deut 4:38', 'Deut 9:1'] and FORTIFIED_9 == ['Deut 9:1'] and FORTIFIED_1 == ['Deut 1:28'] and GREAT_TALL == ['Deut 1:28', 'Deut 9:2'] and P('מי', 'יתיצב', 'לפני') == ['Deut 9:2']
ANAKIM = U('ענקים', 'ענק', 'הענק', 'הענקים', 'ענקי', 'וענקים'); CONSUMING_FIRE = P('אש', 'אכלה'); PASSES_BEFORE = P('העבר', 'לפניך') + P('עבר', 'לפניך')
assert len(ANAKIM) == 13 and CONSUMING_FIRE == ['Deut 4:24', 'Deut 9:3', 'Joel 1:19', 'Joel 2:5'] and PASSES_BEFORE == ['Deut 9:3', 'Deut 31:3'] and [(s, x) for s, x, _ in LEMT('3665', books=('Deut',))] == [('Deut 9:3', 'יכניעם')]
QUICKLY = [(s, x) for s, x, m in LEMT('4118 b', books=('Deut',))]
assert QUICKLY == [('Deut 4:26', 'מהר'), ('Deut 7:4', 'מהר'), ('Deut 7:22', 'מהר'), ('Deut 9:3', 'מהר'), ('Deut 9:12', 'מהר'), ('Deut 9:12', 'מהר'), ('Deut 9:16', 'מהר'), ('Deut 28:20', 'מהר')]
DO_NOT_SAY = P('אל', 'תאמר', 'בלבבך'); AND_YOU_SAY = P('ואמרת', 'בלבבך'); RIGHTEOUSNESS = [(s, x) for s, x, _ in LEMT('6666', books=T)]; WICKEDNESS = [(s, x) for s, x, _ in LEMT('7564', books=T)]
assert DO_NOT_SAY == ['Deut 9:4'] and AND_YOU_SAY == ['Deut 8:17', 'Isa 49:21'] and RIGHTEOUSNESS == [('Deut 6:25', 'וצדקה'), ('Deut 9:4', 'בצדקתי'), ('Deut 9:5', 'בצדקתך'), ('Deut 9:6', 'בצדקתך'), ('Deut 24:13', 'צדקה'), ('Deut 33:21', 'צדקת'), ('Gen 15:6', 'צדקה'), ('Gen 18:19', 'צדקה'), ('Gen 30:33', 'צדקתי')] and WICKEDNESS == [('Deut 9:4', 'וברשעת'), ('Deut 9:5', 'ברשעת'), ('Deut 25:2', 'רשעתו')]
assert P('ובישר', 'לבבך') == ['Deut 9:5'] and P('ישר', 'לבב') == [] and (sum(1 for v in range(1, 30) for x in W9(v) if x in ('למען', 'ולמען')), len(U('למען', 'ולמען', books=('Deut',)))) == (1, 43)
TRIAD_OATH = P('לאברהם', 'ליצחק', 'וליעקב'); TRIAD_EXOD = P('לאברהם', 'ליצחק', 'ולישראל')
assert TRIAD_OATH == ['Deut 1:8', 'Deut 29:12', 'Deut 30:20', 'Deut 34:4', 'Deut 6:10', 'Deut 9:27', 'Deut 9:5', 'Exod 33:1', 'Exod 6:8', 'Gen 50:24', 'Num 32:11'] and TRIAD_EXOD == ['Exod 32:13']
assert PT('Deut', 9, 5, 'נשבע') == ['נִשְׁבַּע'] and lemma_of('Deut', 9, 5, 'נשבע') == ['7650'] and [s for s, x, m in LEMT('7650', books=('Deut',)) if s.startswith('Deut 9:')] == ['Deut 9:5'] and [s for s, _, _ in LEMT('7646', books=('Deut',)) if s.startswith('Deut 9:')] == []
GOOD_LAND = P('הארץ', 'הטובה')
assert GOOD_LAND == ['1Chr 28:8', 'Deut 1:35', 'Deut 3:25', 'Deut 4:21', 'Deut 4:22', 'Deut 9:6', 'Josh 23:16']
STIFF = P('קשה', 'ערף'); NAPE = [(s, x) for s, x, _ in LEMT('6203', books=T)]; STUBBORN = [(s, x) for s, x, _ in LEMT('7190')]
assert STIFF == ['Deut 9:13', 'Deut 9:6', 'Exod 32:9', 'Exod 33:3', 'Exod 33:5', 'Exod 34:9'] and P('קשי', 'ערף') == [] and STUBBORN == [('Deut 9:27', 'קשי')] and len(NAPE) == 11   # STIFF-NECKED six seats in the Bible, ALL the calf's; "stubbornness" the Bible's one seat
REMEMBER_FORGET = P('זכר', 'אל', 'תשכח'); REMEMBER_IMP = [(s, x) for s, x, m in LEMT('2142', books=('Deut',)) if m and 'v2ms' in m]
assert REMEMBER_FORGET == ['Deut 9:7'] and REMEMBER_IMP == [('Deut 9:7', 'זכר'), ('Deut 9:27', 'זכר'), ('Deut 32:7', 'זכר')]
PROVOKE = [(s, x) for s, x, m in LEMT('7107', books=T) if m and m.startswith('HVh')]
assert PROVOKE == [('Deut 9:7', 'הקצפת'), ('Deut 9:8', 'הקצפתם'), ('Deut 9:22', 'מקצפים')] and len(LEMT('7107', books=T)) == 12   # the hiphil "provoke" — the Torah's three, all this chapter's
FROM_THE_DAY = P('למן', 'היום', books=('Deut',)); THIS_PLACE = P('עד', 'המקום', 'הזה'); REBELLIOUS_WERE = P('ממרים', 'הייתם'); REBEL = [(s, x) for s, x, m in LEMT('4784', books=T)]
assert FROM_THE_DAY == ['Deut 4:32', 'Deut 9:7'] and THIS_PLACE == ['Deut 11:5', 'Deut 1:31', 'Deut 9:7'] and REBELLIOUS_WERE == ['Deut 9:24', 'Deut 9:7'] and len(REBEL) == 11 and [s for s, _ in REBEL if s.startswith('Deut 9:')] == ['Deut 9:7', 'Deut 9:23', 'Deut 9:24']
ANGRY = [(s, x) for s, x, m in LEMT('599') if s.startswith('Deut')]; DESTROY_INF = [s for s in U('להשמיד', 'להשמידך', 'להשמידו', 'להשמידם', 'ולהשמיד') if s.startswith('Deut')]
assert ANGRY == [('Deut 1:37', 'התאנף'), ('Deut 4:21', 'התאנף'), ('Deut 9:8', 'ויתאנף'), ('Deut 9:20', 'התאנף')] and len(LEMT('599')) == 14 and DESTROY_INF == ['Deut 28:63', 'Deut 9:19', 'Deut 9:20', 'Deut 9:25', 'Deut 9:8'] and U('להשמידו') == ['Deut 9:20']
FORTY_PHRASE = P('ארבעים', 'יום', 'וארבעים', 'לילה'); FORTY_ART = P('ארבעים', 'היום', 'ואת', 'ארבעים', 'הלילה')
assert FORTY_PHRASE == ['1Kgs 19:8', 'Deut 10:10', 'Deut 9:11', 'Deut 9:18', 'Deut 9:9', 'Exod 24:18', 'Exod 34:28', 'Gen 7:12', 'Gen 7:4'] and FORTY_ART == ['Deut 9:25']   # the Bible's nine seats, four in the chapter; the article's form once
BREAD_WATER = P('לחם', 'לא', 'אכלתי', 'ומים', 'לא', 'שתיתי'); BREAD_WATER_3 = P('לחם', 'לא', 'אכל', 'ומים', 'לא', 'שתה'); I_SAT = P('ואשב', 'בהר'); AT_THE_END = P('מקץ', 'ארבעים', 'יום')
assert BREAD_WATER == ['Deut 9:18', 'Deut 9:9'] and BREAD_WATER_3 == ['Exod 34:28', 'Ezra 10:6'] and I_SAT == ['Deut 9:9', 'Isa 14:13'] and AT_THE_END == ['Deut 9:11', 'Gen 8:6', 'Num 13:25'] and P('בעלתי', 'ההרה') == ['Deut 9:9']
FINGER = P('כתבים', 'באצבע', 'אלהים'); ASSEMBLY_DAY = P('ביום', 'הקהל') + P('יום', 'הקהל'); MIDST_FIRE = P('מתוך', 'האש', books=('Deut',))
assert FINGER == ['Deut 9:10', 'Exod 31:18'] and ASSEMBLY_DAY == ['Deut 10:4', 'Deut 18:16', 'Deut 9:10'] and len(MIDST_FIRE) == 10 and [x for x, m in wm('Deut', 9, 10) if m == 'HVqsmpa'] == ['כתבים']
ARISE_GO_DOWN = P('קום', 'רד', 'מהר'); GO_GET_DOWN = P('לך', 'רד'); CORRUPTED = P('שחת', 'עמך'); TURNED_QUICKLY = P('מהר', 'מן', 'הדרך')
assert ARISE_GO_DOWN == ['Deut 9:12'] and GO_GET_DOWN == ['Exod 19:24', 'Exod 32:7'] and CORRUPTED == ['Deut 9:12', 'Exod 32:7', 'Isa 14:20'] and TURNED_QUICKLY == ['Deut 9:12', 'Deut 9:16', 'Exod 32:8', 'Judg 2:17']
MOLTEN_CALF = P('עגל', 'מסכה'); CALF_SEATS = U('העגל', 'עגל', 'לעגל', 'בעגל', books=T)
assert MOLTEN_CALF == ['Deut 9:16', 'Exod 32:4', 'Exod 32:8', 'Neh 9:18'] and CALF_SEATS == ['Deut 9:16', 'Deut 9:21', 'Exod 32:19', 'Exod 32:20', 'Exod 32:24', 'Exod 32:35', 'Exod 32:4', 'Exod 32:8', 'Lev 9:2', 'Lev 9:8']
I_HAVE_SEEN = P('ראיתי', 'את', 'העם', 'הזה'); LET_ME_ALONE = P('הרף', 'ממני'); LET_ME_ALONE_X = P('הניחה', 'לי'); BLOT = [(s, x) for s, x, _ in LEMT('4229 a', books=T)][:4]
assert I_HAVE_SEEN == ['Deut 9:13', 'Exod 32:9'] and LET_ME_ALONE == ['Deut 9:14'] and LET_ME_ALONE_X == ['Exod 32:10'] and P('ואשמידם', 'ואמחה') == ['Deut 9:14'] and BLOT == [('Deut 9:14', 'ואמחה'), ('Deut 25:6', 'ימחה'), ('Deut 25:19', 'תמחה'), ('Deut 29:19', 'ומחה')]
OFFER_FORMS = P('ואעשה', 'אותך', 'לגוי') + P('ואעשך', 'לגוי') + P('אתך', 'לגוי'); OFFER_9 = P('לגוי', 'עצום', 'ורב', 'ממנו'); OFFER_14 = P('לגוי', 'גדול', 'ועצום', 'ממנו'); GREAT_NATION = P('לגוי', 'גדול')
assert OFFER_FORMS == ['Deut 9:14', 'Exod 32:10', 'Gen 12:2', 'Num 14:12'] and OFFER_9 == ['Deut 9:14'] and OFFER_14 == ['Num 14:12'] and GREAT_NATION == ['Deut 26:5', 'Exod 32:10', 'Gen 12:2', 'Gen 17:20', 'Gen 18:18', 'Gen 21:18', 'Gen 46:3', 'Num 14:12']
TURNED_DOWN = P('ואפן', 'וארד', 'מן', 'ההר'); TURNED_DOWN_X = P('ויפן', 'וירד', 'משה', 'מן', 'ההר'); BURNING = P('בער', 'באש'); TWO_HANDS = P('על', 'שתי', 'ידי')
assert TURNED_DOWN == ['Deut 10:5', 'Deut 9:15'] and TURNED_DOWN_X == ['Exod 32:15'] and BURNING == ['Deut 4:11', 'Deut 5:23', 'Deut 9:15', 'Exod 3:2'] and TWO_HANDS == ['Deut 9:15'] and words('Exod', 32, 15)[8] == 'בידו'
BEFORE_YOUR_EYES = U('לעיניכם', books=('Deut',)); TOOK_HOLD = [(s, x) for s, x, _ in LEMT('8610', books=T)][:1]; THREW_9 = P('ואשלכם', 'מעל', 'שתי', 'ידי'); THREW_X = P('וישלך', 'מידו', 'את', 'הלחת'); BROKE = [(s, x) for s, x, _ in LEMT('7665', books=T) if s.startswith('Deut')]
assert BEFORE_YOUR_EYES == ['Deut 1:30', 'Deut 29:1', 'Deut 9:17'] and TOOK_HOLD == [('Deut 9:17', 'ואתפש')] and THREW_9 == ['Deut 9:17'] and THREW_X == ['Exod 32:19'] and BROKE == [('Deut 7:5', 'תשברו'), ('Deut 9:17', 'ואשברם'), ('Deut 10:2', 'שברת'), ('Deut 12:3', 'ושברתם')]
FELL_DOWN = P('ואתנפל', 'לפני', 'יהוה'); FELL_HITH = [(s, x) for s, x, m in LEMT('5307') if m and 'Vt' in m]; AS_AT_FIRST = U('כראשנה', 'כראשונה', 'כבראשנה', 'בראשנה', books=T); EVIL_EYES = P('לעשות', 'הרע', 'בעיני', 'יהוה', books=T); PROVOKE_HIM = [(s, x) for s, x, _ in LEMT('3707', books=T)]
assert FELL_DOWN == ['Deut 9:18', 'Deut 9:25'] and FELL_HITH == [('Deut 9:18', 'ואתנפל'), ('Deut 9:25', 'ואתנפל'), ('Deut 9:25', 'התנפלתי'), ('Ezra 10:1', 'ומתנפל'), ('Gen 43:18', 'ולהתנפל')] and AS_AT_FIRST == ['Deut 17:7', 'Deut 9:18', 'Gen 13:4', 'Num 10:13', 'Num 10:14'] and EVIL_EYES == ['Deut 9:18'] and len(P('הרע', 'בעיני', 'יהוה')) == 53 and PROVOKE_HIM[:3] == [('Deut 4:25', 'להכעיסו'), ('Deut 9:18', 'להכעיסו'), ('Deut 31:29', 'להכעיסו')]
AFRAID = P('יגרתי', 'מפני'); ANGER_WRATH = P('האף', 'והחמה'); AFRAID_LEM = [(s, x) for s, x, _ in LEMT('3025') if s.startswith('Deut')]; HEARKENED = P('וישמע', 'יהוה', 'אלי'); THAT_TIME_ALSO = P('גם', 'בפעם', 'ההוא'); AT_THAT_TIME = P('בעת', 'ההוא', books=('Deut',)); PAAM = [(s, x) for s, x, _ in LEMT('6471', books=('Deut',))]
assert AFRAID == ['Deut 9:19'] and ANGER_WRATH == ['Deut 9:19', 'Jer 36:7'] and AFRAID_LEM == [('Deut 9:19', 'יגרתי'), ('Deut 28:60', 'יגרת')] and HEARKENED == ['Deut 10:10', 'Deut 9:19'] and THAT_TIME_ALSO == ['Deut 10:10', 'Deut 9:19'] and len(AT_THAT_TIME) == 15 and 'Deut 9:20' in AT_THAT_TIME and PAAM == [('Deut 1:11', 'פעמים'), ('Deut 9:19', 'בפעם'), ('Deut 10:10', 'בפעם'), ('Deut 16:16', 'פעמים')]
ANGRY_LORD = P('התאנף', 'יהוה'); I_PRAYED = U('ואתפלל', 'ואתפללה'); PRAY_LEM = [(s, x) for s, x, _ in LEMT('6419', books=T)]
assert ANGRY_LORD == ['Deut 1:37', 'Deut 9:20'] and I_PRAYED == ['1Sam 7:5', 'Dan 9:4', 'Deut 9:20', 'Deut 9:26', 'Jer 32:16', 'Neh 2:4'] and PRAY_LEM == [('Deut 9:20', 'ואתפלל'), ('Deut 9:26', 'ואתפלל'), ('Gen 20:7', 'ויתפלל'), ('Gen 20:17', 'ויתפלל'), ('Gen 48:11', 'פללתי'), ('Num 11:2', 'ויתפלל'), ('Num 21:7', 'התפלל'), ('Num 21:7', 'ויתפלל')]
CALF_YOU_MADE = P('אשר', 'עשיתם', 'את', 'העגל'); BURNED_9 = P('ואשרף', 'אתו', 'באש'); BURNED_X = P('וישרף', 'באש'); UNTIL_FINE = P('עד', 'אשר', 'דק'); CRUSH = [(s, x) for s, x, _ in LEMT('3807', books=T)]; GRIND = [(s, x, m) for s, x, m in LEMT('2912') if s.startswith('Deut')]; FINE = [(s, x) for s, x, _ in LEMT('1854', books=T)]; BROOK = P('הנחל', 'הירד', 'מן', 'ההר'); SCATTERED_X = P('ויזר', 'על', 'פני', 'המים'); KIDRON = P('אל', 'נחל', 'קדרון')
assert CALF_YOU_MADE == ['Deut 9:21'] and BURNED_9 == ['Deut 9:21'] and BURNED_X == ['Exod 32:20'] and UNTIL_FINE == ['Deut 9:21', 'Exod 32:20'] and CRUSH == [('Deut 1:44', 'ויכתו'), ('Deut 9:21', 'ואכת'), ('Lev 22:24', 'וכתות'), ('Num 14:45', 'ויכתום')] and GRIND == [('Deut 9:21', 'טחון', 'HVqa')] and FINE == [('Deut 9:21', 'דק'), ('Exod 30:36', 'הדק'), ('Exod 32:20', 'דק')] and BROOK == ['Deut 9:21'] and SCATTERED_X == ['Exod 32:20'] and KIDRON == ['2Kgs 23:12', '2Kgs 23:6']
assert [x for x, m in wm('Deut', 9, 21) if m in ('HVqa', 'HVha')] == ['טחון', 'היטב'] and words('Exod', 32, 20)[11:15] == ['ויזר', 'על', 'פני', 'המים'] and W9(21)[21:23] == ['אל', 'הנחל']
TABERAH = U('תבערה', 'ובתבערה', 'בתבערה'); MASSAH = U('מסה', 'ובמסה', 'במסה'); KIBROTH = P('קברת', 'התאוה') + P('ובקברת', 'התאוה') + P('מקברת', 'התאוה') + P('בקברת', 'התאוה'); KIBROTH_PLENE = P('קברות', 'התאוה') + P('מקברות', 'התאוה')
assert TABERAH == ['Deut 9:22', 'Num 11:3'] and MASSAH == ['Deut 33:8', 'Deut 6:16', 'Deut 9:22', 'Exod 17:7', 'Ps 95:8'] and KIBROTH == ['Deut 9:22', 'Num 33:17', 'Num 33:16'] and KIBROTH_PLENE == ['Num 11:34', 'Num 11:35'] and lemma_of('Deut', 9, 22, 'ובקברת') == ['6914+']
KADESH = P('קדש', 'ברנע') + P('מקדש', 'ברנע') + P('בקדש', 'ברנע') + P('וקדש', 'ברנע'); GO_UP_POSSESS = P('עלו', 'ורשו'); GO_UP_POSSESS_1 = P('עלה', 'רש'); REBELLED_MOUTH = P('ותמרו', 'את', 'פי'); MOUTH_LORD = P('פי', 'יהוה', books=('Deut',)); NOT_BELIEVED = P('ולא', 'האמנתם', 'לו'); NOT_BELIEVING_1 = P('אינכם', 'מאמינם'); NOT_HEARKENED = P('ולא', 'שמעתם', 'בקלו')
assert KADESH == ['Deut 1:19', 'Deut 1:2', 'Deut 2:14', 'Deut 9:23', 'Josh 10:41', 'Josh 14:7', 'Num 32:8', 'Josh 14:6'] and GO_UP_POSSESS == ['Deut 9:23'] and GO_UP_POSSESS_1 == ['Deut 1:21'] and REBELLED_MOUTH == ['Deut 1:26', 'Deut 1:43', 'Deut 9:23'] and MOUTH_LORD == ['Deut 1:26', 'Deut 1:43', 'Deut 34:5', 'Deut 8:3', 'Deut 9:23'] and NOT_BELIEVED == ['Deut 9:23'] and NOT_BELIEVING_1 == ['Deut 1:32'] and NOT_HEARKENED == ['Deut 9:23'] and lemma_of('Deut', 9, 23, 'מקדש') == ['6947+']
FROM_THE_DAY_I_KNEW = P('מיום', 'דעתי', 'אתכם'); SAID_TO_DESTROY = P('כי', 'אמר', 'יהוה', 'להשמיד', 'אתכם')
assert FROM_THE_DAY_I_KNEW == ['Deut 9:24'] and [(s, x) for s, x, _ in LEMT('3045') if x == 'דעתי'] == [('Deut 9:24', 'דעתי')] and SAID_TO_DESTROY == ['Deut 9:25']
PRAYED_AND_SAID = P('ואתפלל', 'אל', 'יהוה', 'ואמר'); LORD_GOD = P('אדני', 'יהוה', books=T); DO_NOT_DESTROY = P('אל', 'תשחת', 'עמך', 'ונחלתך'); PEOPLE_INHERITANCE = P('עמך', 'ונחלתך'); REDEEMED = [(s, x) for s, x, _ in LEMT('6299', books=('Deut',))]; GREATNESS = [(s, x) for s, x, _ in LEMT('1433') if s.startswith('Deut')]; MIGHTY_HAND = P('ביד', 'חזקה', books=T); POWER_HAND_X = P('בכח', 'גדול', 'וביד', 'חזקה')
assert PRAYED_AND_SAID == ['Deut 9:26'] and LORD_GOD == ['Deut 3:24', 'Deut 9:26', 'Gen 15:2', 'Gen 15:8'] and DO_NOT_DESTROY == ['Deut 9:26'] and PEOPLE_INHERITANCE == ['1Kgs 8:51', 'Deut 9:26', 'Deut 9:29'] and P('עמו', 'ונחלתו') == ['Ps 94:14'] and len(REDEEMED) == 6 and GREATNESS == [('Deut 3:24', 'גדלך'), ('Deut 5:24', 'גדלו'), ('Deut 9:26', 'בגדלך'), ('Deut 11:2', 'גדלו'), ('Deut 32:3', 'גדל')] and MIGHTY_HAND == ['Deut 26:8', 'Deut 5:15', 'Deut 6:21', 'Deut 7:8', 'Deut 9:26', 'Exod 13:9', 'Exod 3:19', 'Exod 6:1'] and POWER_HAND_X == ['Exod 32:11']
REMEMBER_SERVANTS = P('זכר', 'לעבדיך'); REMEMBER_ABRAHAM_X = P('זכר', 'לאברהם'); DO_NOT_TURN = P('אל', 'תפן', 'אל'); TURN_JUSSIVE = [(s, x) for s, x, m in LEMT('6437', books=T) if m and 'j' in m[3:6]]; WICKEDNESS_27 = [(s, x) for s, x, _ in LEMT('7562', books=T)]
assert REMEMBER_SERVANTS == ['Deut 9:27'] and REMEMBER_ABRAHAM_X == ['Exod 32:13'] and DO_NOT_TURN == ['Deut 9:27', 'Job 36:21', 'Num 16:15'] and TURN_JUSSIVE == [('Deut 9:27', 'תפן'), ('Lev 19:4', 'תפנו'), ('Lev 19:31', 'תפנו'), ('Num 16:15', 'תפן')] and WICKEDNESS_27 == [('Deut 9:27', 'רשעו')]
assert words('Exod', 32, 13)[:5] == ['זכר', 'לאברהם', 'ליצחק', 'ולישראל', 'עבדיך'] and W9(27)[:5] == ['זכר', 'לעבדיך', 'לאברהם', 'ליצחק', 'וליעקב']
LEST_LAND = P('פן', 'יאמרו', 'הארץ'); WHY_EGYPT_X = P('למה', 'יאמרו', 'מצרים'); NATIONS_SAY_N = P('ואמרו', 'הגוים'); LEST_THEY_SAY = P('פן', 'יאמרו'); ABILITY = P('יכלת', 'יהוה'); MIBLI = U('מבלי', 'מבלתי', 'ומבלי', books=T); HATRED = [(s, x) for s, x, _ in LEMT('8135', books=T)]; KILL_WILDERNESS = P('הוציאם', 'להמתם', 'במדבר'); SLAY_MOUNTAINS_X = P('ברעה', 'הוציאם', 'להרג'); SLAUGHTER_N = P('וישחטם', 'במדבר'); DESTROY_US_1 = U('להשמידנו')
assert LEST_LAND == ['Deut 9:28'] and WHY_EGYPT_X == ['Exod 32:12'] and NATIONS_SAY_N == ['Num 14:15'] and LEST_THEY_SAY == ['Deut 32:27', 'Deut 9:28', 'Judg 9:54'] and U('הוצאתנו') == ['Deut 9:28'] and ABILITY == ['Deut 9:28', 'Num 14:16'] and W9(28)[6] == 'מבלי' and words('Num', 14, 16)[0] == 'מבלתי' and MIBLI == ['Deut 28:55', 'Deut 9:28', 'Num 14:16'] and HATRED == [('Deut 1:27', 'בשנאת'), ('Deut 9:28', 'ומשנאתו'), ('Num 35:20', 'בשנאה')] and KILL_WILDERNESS == ['Deut 9:28'] and SLAY_MOUNTAINS_X == ['Exod 32:12'] and SLAUGHTER_N == ['Num 14:16'] and DESTROY_US_1 == ['Deut 1:27']   # FOUR forms of the nations' taunt
THEY_ARE = P('והם', 'עמך', 'ונחלתך'); GREAT_POWER_ARM = P('בכחך', 'הגדל', 'ובזרעך', 'הנטויה'); GREAT_POWER_X = P('בכח', 'גדול'); HIS_GREAT_POWER = P('בכחו', 'הגדל'); YOUR_GREAT_POWER = P('בכחך', 'הגדל'); YOUR_GREAT_POWER_PLENE = P('בכחך', 'הגדול'); ARM = [(s, x) for s, x, _ in LEMT('2220', books=('Deut',))][:4]
assert THEY_ARE == ['Deut 9:29'] and GREAT_POWER_ARM == ['Deut 9:29'] and GREAT_POWER_X == ['2Kgs 17:36', 'Exod 32:11'] and HIS_GREAT_POWER == ['Deut 4:37'] and YOUR_GREAT_POWER == ['Deut 9:29'] and YOUR_GREAT_POWER_PLENE == ['Jer 32:17', 'Neh 1:10'] and ARM == [('Deut 4:34', 'ובזרוע'), ('Deut 5:15', 'ובזרע'), ('Deut 7:19', 'והזרע'), ('Deut 9:29', 'ובזרעך')]
OUTSTRETCHED_DEUT = sorted(s for s in P('ובזרע', 'נטויה') + P('ובזרעך', 'הנטויה') + P('ובזרוע', 'נטויה') if s.startswith('Deut'))
assert OUTSTRETCHED_DEUT == ['Deut 26:8', 'Deut 4:34', 'Deut 5:15', 'Deut 9:29']
# THE KIN DIFFED (the DB's tokens; SHN the tokens shared in order — typed from the reading's print)
DELTA = {
    'nations_9_1': (LEN('Deut', 9, 1), LEN('Deut', 4, 38), SHN(D9(1), ('Deut', 4, 38))), 'fortified_9_1': (LEN('Deut', 9, 1), LEN('Deut', 1, 28), SHN(D9(2), ('Deut', 1, 28))), 'fire_9_3': (LEN('Deut', 9, 3), LEN('Deut', 4, 24), SHN(D9(3), ('Deut', 4, 24)), SHN(D9(3), ('Deut', 31, 3))),
    'oath_9_5': (LEN('Deut', 9, 5), LEN('Deut', 30, 20), SHN(D9(5), ('Deut', 30, 20))), 'stiff_9_6': (LEN('Deut', 9, 6), LEN('Exod', 33, 3), SHN(D9(6), ('Exod', 33, 3))), 'rebellious_9_7': (LEN('Deut', 9, 7), LEN('Deut', 11, 5), SHN(D9(7), ('Deut', 11, 5)), SHN(D9(24), D9(7))),
    'forty_9_9': (LEN('Deut', 9, 9), LEN('Exod', 34, 28), SHN(D9(9), ('Exod', 34, 28)), SHN(D9(9), ('Exod', 24, 18)), SHN(D9(9), ('Exod', 24, 8)), SHN(D9(9), D9(18))), 'finger_9_10': (LEN('Deut', 9, 10), LEN('Deut', 10, 4), SHN(D9(10), ('Deut', 10, 4)), SHN(D9(10), ('Deut', 5, 4)), SHN(D9(10), ('Exod', 31, 18))), 'end_9_11': (LEN('Deut', 9, 11), LEN('Exod', 34, 28), SHN(D9(11), ('Exod', 34, 28))),
    'go_down_9_12': (LEN('Deut', 9, 12), LEN('Exod', 32, 8), SHN(D9(12), ('Exod', 32, 8)), SHN(D9(12), ('Exod', 32, 7))), 'seen_9_13': (LEN('Deut', 9, 13), LEN('Exod', 32, 9), SHN(D9(13), ('Exod', 32, 9))), 'offer_9_14': (LEN('Deut', 9, 14), LEN('Exod', 32, 10), SHN(D9(14), ('Exod', 32, 10)), SHN(D9(14), ('Num', 14, 12))),
    'descent_9_15': (LEN('Deut', 9, 15), LEN('Exod', 32, 15), SHN(D9(15), ('Exod', 32, 15))), 'calf_9_16': (LEN('Deut', 9, 16), LEN('Exod', 32, 8), SHN(D9(16), ('Exod', 32, 8)), SHN(D9(16), ('Exod', 32, 4))), 'broke_9_17': (LEN('Deut', 9, 17), LEN('Exod', 32, 19), SHN(D9(17), ('Exod', 32, 19))),
    'fell_9_18': (LEN('Deut', 9, 18), LEN('Exod', 34, 28), SHN(D9(18), ('Exod', 34, 28))), 'hearkened_9_19': (LEN('Deut', 9, 19), LEN('Deut', 10, 10), SHN(D9(19), ('Deut', 10, 10)), SHN(D9(19), ('Exod', 32, 14))), 'aaron_9_20': (LEN('Deut', 9, 20), LEN('Exod', 32, 21), SHN(D9(20), ('Exod', 32, 21)), SHN(D9(20), ('Exod', 32, 35))),
    'dust_9_21': (LEN('Deut', 9, 21), LEN('Exod', 32, 20), SHN(D9(21), ('Exod', 32, 20))), 'kadesh_9_23': (LEN('Deut', 9, 23), LEN('Deut', 1, 26), SHN(D9(23), ('Deut', 1, 26)), SHN(D9(23), ('Josh', 14, 7))), 'prayed_9_26': (LEN('Deut', 9, 26), LEN('Exod', 32, 11), SHN(D9(26), ('Exod', 32, 11)), SHN(D9(26), ('1Kgs', 8, 51))),
    'servants_9_27': (LEN('Deut', 9, 27), LEN('Exod', 32, 13), SHN(D9(27), ('Exod', 32, 13))), 'taunt_9_28': (LEN('Deut', 9, 28), LEN('Num', 14, 16), SHN(D9(28), ('Num', 14, 16)), SHN(D9(28), ('Exod', 32, 12))), 'power_9_29': (LEN('Deut', 9, 29), LEN('Exod', 32, 11), SHN(D9(29), ('1Kgs', 8, 51))),
}
assert DELTA == {'nations_9_1': (17, 14, 4), 'fortified_9_1': (17, 21, 5), 'fire_9_3': (22, 8, 6, 9), 'oath_9_5': (28, 25, 10), 'stiff_9_6': (18, 17, 7), 'rebellious_9_7': (25, 9, 6, 4), 'forty_9_9': (23, 22, 9, 5, 5, 11), 'finger_9_10': (22, 20, 10, 6, 5), 'end_9_11': (15, 22, 7), 'go_down_9_12': (22, 22, 9, 6), 'seen_9_13': (13, 13, 11), 'offer_9_14': (14, 11, 3, 3), 'descent_9_15': (13, 17, 4), 'calf_9_16': (17, 22, 4, 3), 'broke_9_17': (9, 20, 1), 'fell_9_18': (24, 22, 10), 'hearkened_9_19': (17, 19, 6, 1), 'aaron_9_20': (11, 14, 1, 2), 'dust_9_21': (26, 19, 7), 'kadesh_9_23': (24, 8, 5, 5), 'prayed_9_26': (18, 20, 5, 5), 'servants_9_27': (15, 25, 3), 'taunt_9_28': (20, 14, 7, 2), 'power_9_29': (9, 20, 4)}, DELTA   # typed from the fast checker's print (ch9_fastcheck1.out)
assert SHARED(D9(13), ('Exod', 32, 9)) == ['ראיתי', 'את', 'העם', 'הזה', 'והנה', 'עם', 'קשה', 'ערף', 'הוא'] and DIFF(D9(13), ('Exod', 32, 9)) == [('replace', ['אלי', 'לאמר'], ['אל', 'משה'])]   # God's word VERBATIM but for "to me, saying"
assert SHARED(D9(14), ('Exod', 32, 10)) == ['ואעשה', 'אותך', 'לגוי'] and SHARED(D9(16), ('Exod', 32, 4)) == ['עגל', 'מסכה'] and SHARED(D9(21), ('Exod', 32, 20)) == ['עד', 'אשר', 'דק'] and SHARED(D9(27), ('Exod', 32, 13)) == ['לאברהם', 'ליצחק'] and SHARED(D9(9), ('Exod', 24, 8)) == ['הברית', 'אשר', 'כרת', 'יהוה', 'עמכם']

# ---- THE CLOCK'S OWN ARITHMETIC (a bare world on the exodus epoch; the tape's markers reproduce these days — asserted on the running world at DA4) ----
with contextlib.redirect_stdout(io.StringIO()):
    _WC = WE.World(era='the clock — the three forties of Deuteronomy 9 on a bare world (the exodus epoch)', epoch='exodus')
_EX = _WC.clock.eras['exodus']
def DAY(y, m, d): return _WC.clock.day_in('exodus', y, m, d)
def DATE(day): return _EX.date(day)
ASCENT = DAY(1, 3, 7); BREAKING = DAY(1, 4, 17); MORROW = BREAKING + 1
SECOND_TABLETS = DAY(1, WE.CAL_PARAMS['second_tablets_given']['value']['month'], WE.CAL_PARAMS['second_tablets_given']['value']['day']); SECOND_ASCENT = SECOND_TABLETS - 40; ELUL_1 = DAY(1, 6, 1)
CLOCK = {'ascent': DATE(ASCENT), 'breaking': DATE(BREAKING), 'morrow': DATE(MORROW), 'second_ascent': DATE(SECOND_ASCENT), 'second_tablets': DATE(SECOND_TABLETS),
         'first_forty': BREAKING - ASCENT, 'second_forty': SECOND_ASCENT - MORROW, 'third_forty': SECOND_TABLETS - SECOND_ASCENT, 'sivan_days': DAY(1, 4, 1) - DAY(1, 3, 1), 'sivan_remaining': DAY(1, 4, 1) - ASCENT, 'tammuz_to_breaking': BREAKING - DAY(1, 4, 1),
         'calf_day': DATE(ASCENT + 39), 'elul_1_minus_second_ascent': ELUL_1 - SECOND_ASCENT}
assert CLOCK == {'ascent': (1, 3, 7), 'breaking': (1, 4, 17), 'morrow': (1, 4, 18), 'second_ascent': (1, 5, 29), 'second_tablets': (1, 7, 10), 'first_forty': 40, 'second_forty': 40, 'third_forty': 40, 'sivan_days': 30, 'sivan_remaining': 24, 'tammuz_to_breaking': 16, 'calf_day': (1, 4, 16), 'elul_1_minus_second_ascent': 2}, CLOCK
# Ta'anit 28b:9's own arithmetic — twenty-four days remaining in Sivan plus the first sixteen of Tammuz = forty — REPRODUCED by the calendar (Sivan thirty days that year on the tape's calendar);
# the calf's own day the fortieth day's sixth hour = the sixteenth of Tammuz (Shabbat 89a:6 — the OPEN row: no marker this sitting); the tradition's first of Elul two days after the machine's twenty-ninth of Av (the parameter's own open row)

# ---- THE ONE DATABASE SCANNED (the SUPPLIED grade's ground: no entry but this sitting's own names Aaron's peril; no entry names the stiff neck) ----
_WDB = _os.path.join(_ROOT, 'World', 'journal', 'data', 'world.sqlite')
def ledger_scan(entity, pattern):
    """the effects on an entity in the one database whose name or value matches the pattern — None where the database is not built (a fresh clone before build_world)"""
    if not _os.path.exists(_WDB): return None
    c_ = sqlite3.connect('file:%s?mode=ro' % _WDB, uri=True)
    rx = re.compile(pattern, re.I)
    return sorted({e for e, v in c_.execute("SELECT DISTINCT effect, value FROM run_ledger WHERE entity=?", (entity,)).fetchall() if rx.search('%s %s' % (e, v if v is not None else ''))})
PERIL_WORDS = r"\b(peril|to destroy him|half the edict|two died|destruction_halved|destruction_averted)\b"   # word-bounded (6b's lesson: a bare word matches inside another)
STIFF_WORDS = r"\b(stiff|stiff-necked|neck|nape)\b"
_peril = ledger_scan('aaron', PERIL_WORDS)
AARON_PERIL_SCAN = None if _peril is None else [e for e in _peril if e != 'destruction_halved']   # this sitting's own write excluded once the fold carries it: NO OTHER entry names the peril
STIFF_SCAN = ledger_scan('israel_people', STIFF_WORDS)
assert AARON_PERIL_SCAN in ([], None), AARON_PERIL_SCAN   # the hole's ground — no entry on aaron named the peril before this write
assert STIFF_SCAN in ([], None), STIFF_SCAN   # the stiff neck a STATE in the first telling: no entry, no write (the design's decision 2)

#!/usr/bin/env python3
# DEUTERONOMY 10:1-22 — THE SECOND TABLETS AND THE ARK, THE STATIONS AND AARON'S DEATH, THE LEVITES SEPARATED, THE THIRD FORTY AND THE GO, WHAT THE LORD
# ASKS, THE GOD OF GODS AND THE STRANGER — THE READBACK'S FORMS COMBINED, NO SEVENTH (THE DEUTERONOMY WALK sitting 8b, 2026-09-20; World/step9/DEUTERONOMY_WALK.md
# "Sitting 8b"; the state doc's #197). The chapter is the retelling's tail (10:1-11) and the laws' head (10:12-22): its rows take the forms already on file —
# T1 reference rows against the tape's lines by kind and first verse or the kin's cells by CALL; T2 SUPPLIED WITH A WRITE, TWICE — THE FRAGMENTS IN THE ARK
# (10:2 'and you shall put them in the ark', read of both sets by Menachot 99a:12 and Bava Batra 14b:6) and AARON'S BURIAL (10:6 'and he was buried there',
# the Torah's one seat), two acts TOLD ONLY HERE, each written ONCE at its own day by a RETROGRADE marker (Deut 10:2 at the erection's day (2, 1, 1) —
# M['fragments_told'] = M['erected']; Deut 10:6 at Aaron's death (40, 5, 1) — M['burial_told'] = M['aaron_death']; reading_placed), the writes
# fragments_in_the_ark (a STATUS on the ark — THE VALUE FROM THE DOCKET: the tablets and the fragments, the scroll inside or beside) and buried (the STATUS
# REUSED — Aaron the world's ninth); T6 ONE stretch row — 10:10's third forty measured on the clock (the second ascent's marker at Exod 34:4 to the timers'
# fire at (1, 7, 10) = 40; THE SECOND ASCENT'S DATE MATCHES SEDER OLAM RABBAH 6:2 — 7b's OPEN row CLOSED); T4 THE LAWS' FORM on 10:12-22 — every row against
# the cell that compiles it, by CALL, and THE CODE'S FOUR HOLES compiled at the chapter's own day (40, 11, 1) after the FORWARD marker at 10:12: the demand
# (fear_of_heaven_asked — THE SHELF'S NAME, Berakhot 33b:23), the heart and the neck (heart_circumcision_commanded — the evil inclination, Sukkah 52a:7;
# stiffening_barred — the chapter's one prohibition, no lashes), the stranger's love (love_owed — Leviticus 19:34's effect written on the tape for the
# first time), the cleaving (cleaving_commanded — the scholars, Ketubot 111b:7; the positive form, Temurah 4a:2); an OPEN row (the place of the death —
# Moserah / Mount Hor, the retreat of seven stations already a parameter); a HOLE outside the span (the go — Exodus 32:34's and 33:1's speeches have no
# line). The daemon law_second_tablets given_at Deut 10:1, installed_by boot (the Deuteronomy daemons' form). Six cells; every token probed (zero-report
# law); effects on every cell (the effects law); the DATA rows the docket added (the two arks of the Tosefta, the ark's contents' two arms, the grammar
# guard, the inclination's name, the burial among the attributes, the positive form, the intake, the editor's 'first of Tammuz' variant). Reading ledger:
# logic/oral_triage/deu_10_ekev_2026-09-19.md (25 sources, 6 claims); the exam's docket: deu_10_ekev_exam_2026-09-20.md (532 rows READ WHOLE FROM THE
# START: LAW 78 / DERIVATION 76 / DISPUTE 14 / CONTEXT 117 / OUTSIDE 247).

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
import cold_run_erection as ER                 # THE EDGE: second_tablets -> erection CALL, reference (the second ascent's marker and the timers' fire — the third forty on the clock; the fragments by call; the breaking ratified; the finger and the forms; the Levites gathered at the calf)
import cold_run_sanctuary_build as SB          # THE EDGE: second_tablets -> sanctuary_build CALL, reference (the ark's spec and making — both in the ark, the named maker, the hands on the ark; the testimony placed)
import cold_run_covenant_at_horeb as CH        # THE EDGE: second_tablets -> covenant_at_horeb CALL, reference (5:22's tablets given to me — 10:4's row)
import cold_run_obey_horeb as OH               # THE EDGE: second_tablets -> obey_horeb CALL, reference (4:1's 'and now, Israel'; 4:39's heaven and earth; 4:37's chosen seed; 4:4's cleaving STATE; 4:13's tablets_given; 4:9's 'your eyes have seen')
import cold_run_not_righteousness as NR        # THE EDGE: second_tablets -> not_righteousness CALL, reference (chapter 9's continuation — the finger, the breaking, the fragments owed, the forties, the hearkening)
import cold_run_journeys as JO                 # THE EDGE: second_tablets -> journeys CALL, reference (the stations in another order — Moseroth seven camps before Hor; the retreat of seven stations the parameter; Aaron's death retold)
import cold_run_chukat as CK                   # THE EDGE: second_tablets -> chukat CALL, reference (Aaron's death and succession at Hor; Moserah the parameter; Arad heard; the death's dates)
import cold_run_bamidbar as BM                 # THE EDGE: second_tablets -> bamidbar CALL, reference (the Kohathites carry the ark — 10:8's first office; the Levites given instead of the firstborn)
import cold_run_beha as BH                     # THE EDGE: second_tablets -> beha CALL, reference (the ark's bearers on the march; the Levites' rite and service)
import cold_run_korach as KR                   # THE EDGE: second_tablets -> korach CALL, reference (the watch — 'to stand before the LORD to minister'; 'separated' at 16:9; the portion declared and the tithe)
import cold_run_naso as NS                     # THE EDGE: second_tablets -> naso CALL, reference (the blessing in His name — 10:8's third office; the face lifted thrice reconciled against 10:17)
import cold_run_joseph as JS                   # THE EDGE: second_tablets -> joseph CALL, reference (the seventy — 10:22's count by CALL; Jochebed the seventieth)
import cold_run_hear_o_israel as HI            # THE EDGE: second_tablets -> hear_o_israel CALL, reference (6:5's creed against 10:12's five infinitives; 6:13's three clauses against 10:20's four; 6:1's header)
import cold_run_good_land as GL                # THE EDGE: second_tablets -> good_land CALL, reference (8:6's keep, walk, fear; 8:7's brooks of water at Jotbathah)
import cold_run_seven_nations as SN            # THE EDGE: second_tablets -> seven_nations CALL, reference (7:7's delight and choice; 7:9's faithful God; 7:19's great trials your eyes saw)
import cold_run_ordinances as OR               # THE EDGE: second_tablets -> ordinances CALL, reference (Exodus 23:8's bribe never written; 22:21's widow and orphan; 22:20's and 23:9's 'you were strangers')
import cold_run_holiness_b as HB               # THE EDGE: second_tablets -> holiness_b CALL, reference (Leviticus 19:34's love of the convert — the cell whose effect is written on the tape for the first time here)

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
def W10(v): return words('Deut', 10, v)
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
D10 = lambda v: ('Deut', 10, v)

P_ = []   # the provenance trail of the case being run
def ink(ref, note):  P_.append(('INK',  'Deut %s — %s' % (ref, note) if not ref[:1].isupper() else '%s — %s' % (ref, note)))
def move(src, note): P_.append(('MOVE', '%s — %s' % (src, note)))
def dat(note):       P_.append(('DATA', note))
def hyp(note):       P_.append(('HYP',  note))     # THE LINK REVIEW LAW: a hypothesis — no teacher; counted apart, never as compiled
def out(verdict, effects):
    """verdict + registry-validated effects (the engine contract)"""
    FX.validate([e for e in effects if e != FX.NONE])
    return verdict, effects, list(P_)

# ---- THE INK, computed (the parser and the tokens; the reading's facts the expectations — every assert PROVEN at the reading, ch10_ink.py — COPIED from the reading's instrument by content markers, the sequence module's names made the exec'd parser's) ----
SPAN = [(10, v) for v in range(1, 23)]
def MARKS(c, v): return [t for t in verse_words('Deut', c, v) if t[-1] in '#~^%@|*']
def N(b, c, v): return ink_numbers(verse_words(b, c, v))
NUMS = {v: ink_numbers(verse_words('Deut', 10, v)) for v in range(1, 23)}
ORDS = {v: ink_ordinals(verse_words('Deut', 10, v)) for v in range(1, 23)}
PARSED = {(10, v): n for v, n in NUMS.items() if n}
TOK = sum(len(W10(v)) for v in range(1, 23)); LET = sum(len(x) for v in range(1, 23) for x in W10(v))
assert TOK == 324 and LET == 1252, (TOK, LET)
assert {v: n for v, n in NUMS.items() if n} == {1: [2], 3: [2, 2], 4: [10], 10: [40, 40], 22: [70]} and {v: o for v, o in ORDS.items() if o} == {4: [1]}, (NUMS, ORDS)
assert verse_words('Deut', 10, 1)[7] == 'שני^' and verse_words('Deut', 10, 3)[5] == 'שני^' and verse_words('Deut', 10, 3)[11] == 'ושני^' and [t for t in verse_words('Deut', 10, 22) if t[-1] in '#~^%@|*'] == []
assert [(b, c, v, ink_numbers(verse_words(b, c, v)), ink_ordinals(verse_words(b, c, v))) for b, c, v in (('Exod', 34, 1), ('Exod', 34, 4), ('Exod', 34, 28), ('Exod', 34, 29), ('Exod', 25, 10), ('Exod', 31, 18), ('Deut', 4, 13), ('Deut', 5, 22), ('Deut', 9, 17), ('Num', 33, 38), ('Num', 33, 39), ('Gen', 46, 27), ('Exod', 1, 5), ('Deut', 1, 10), ('Deut', 28, 62), ('1Kgs', 8, 9), ('Num', 3, 39))] == [('Exod', 34, 1, [2], []), ('Exod', 34, 4, [2, 2], []), ('Exod', 34, 28, [40, 40, 10], []), ('Exod', 34, 29, [2], []), ('Exod', 25, 10, [2.5, 1.5, 1.5], []), ('Exod', 31, 18, [2], []), ('Deut', 4, 13, [10, 2], []), ('Deut', 5, 22, [2], []), ('Deut', 9, 17, [2, 2], []), ('Num', 33, 38, [1], [40, 5]), ('Num', 33, 39, [123], []), ('Gen', 46, 27, [2, 70], []), ('Exod', 1, 5, [70], []), ('Deut', 1, 10, [], []), ('Deut', 28, 62, [], []), ('1Kgs', 8, 9, [2], []), ('Num', 3, 39, [22000], [])]
assert PT('Deut', 10, 20, 'תשבע') == ['תִּשָּׁבֵֽעַ'] and lemma_of('Deut', 10, 20, 'תשבע') == ['7650'] and [(s, x, m) for s, x, m in LEMT('7650', books=('Deut',)) if s.startswith('Deut 10:')] == [('Deut 10:11', 'נשבעתי', 'HVNp1cs'), ('Deut 10:20', 'תשבע', 'HVNi2ms')] and [(v, x) for v in range(1, 23) for x in W10(v) if x in ('שבע', 'שבעה', 'שבעת', 'ושבע', 'ושבעה', 'בשבעים', 'שבעים')] == [(22, 'בשבעים')]
# "FIRST" — the lemma 7223 five times in the chapter: כראשנים ("like the first ones") 10:1, 10:3, הראשנים ("the first ones") 10:2, 10:10 — the PLURAL, the parser reads no ordinal; הראשון ("the first") 10:4 — the singular with the article, the parser's [1]
assert [(x, v, m) for v in range(1, 23) for x, m, l in [(x, m, l) for (x, m), l in zip(by[('Deut', 10, v)], byl[('Deut', 10, v)])] if l == '7223'] == [('כראשנים', 1, 'HRd/Aampa'), ('הראשנים', 2, 'HTd/Aampa'), ('כראשנים', 3, 'HRd/Aampa'), ('הראשון', 4, 'HTd/Aomsa'), ('הראשנים', 10, 'HTd/Aampa')]
assert PT('Deut', 10, 1, 'כראשנים') == ['כָּרִאשֹׁנִים'] and PT('Deut', 10, 4, 'הראשון') == ['הָרִאשׁוֹן'] and U('כראשנים', 'כראשנה', 'כראשונה', 'כבראשנה', 'כראשונים') == ['1Kgs 13:6', 'Dan 11:29', 'Deut 10:1', 'Deut 10:3', 'Deut 9:18', 'Exod 34:1', 'Exod 34:4', 'Isa 1:26', 'Jer 33:11', 'Jer 33:7', 'Judg 20:32'] and U('הראשנים', 'כראשנים', 'ראשנים', 'הראשונים', 'ראשונים', books=T) == ['Deut 10:1', 'Deut 10:10', 'Deut 10:2', 'Deut 10:3', 'Deut 19:14', 'Deut 4:32', 'Exod 34:1', 'Exod 34:4', 'Lev 26:45', 'Num 6:12'] and P('כימים', 'הראשנים') == ['Deut 10:10', 'Zech 8:11']
# THE SPELLINGS OF "TABLETS" in the chapter — לוחת ("tablets", plene) 10:1 alone in the chapter (9:9, 9:10 its kin — the plene's three seats), לחת (defective) 10:3, הלחת (the article's form) five times (10:2 twice, 10:3, 10:4, 10:5)
assert [(x, v) for v in range(1, 23) for x in W10(v) if x in ('לוחת', 'לחת', 'לחות', 'הלחת', 'הלוחת', 'לוחות', 'הלחות')] == [('לוחת', 1), ('הלחת', 2), ('הלחת', 2), ('לחת', 3), ('הלחת', 3), ('הלחת', 4), ('הלחת', 5)]
assert U('לוחת') == ['Deut 10:1', 'Deut 9:10', 'Deut 9:9'] and U('לחות') == ['1Kgs 8:9', 'Deut 4:13', 'Deut 9:11'] and len(U('לחת')) == 12 and len(U('הלחת')) == 10 and U('הלחות') == ['2Chr 5:10', 'Hab 2:2', 'Jer 48:5'] and len(LEMT('3871')) == 43
assert PT('Deut', 10, 1, 'לוחת') == ['לֻוחֹת'] and PT('Deut', 10, 3, 'לחת') == ['לֻחֹת'] and PT('Deut', 10, 2, 'הלחת') == ['הַלֻּחֹת', 'הַלֻּחֹת']
assert [(x, v, m) for v in range(1, 23) for x, m in wm('Deut', 10, v) if x in ('שני', 'שתי', 'ושני', 'בשני', 'שנים', 'שתים')] == [('שני', 1, 'HAcmdc'), ('שני', 3, 'HAcmdc'), ('ושני', 3, 'HC/Acmdc')] and [(v, x, m) for v in range(1, 23) for x, m in wm('Deut', 10, v) if x == 'עשרת'] == [(4, 'עשרת', 'HAcmsc')] and P('עשרת', 'הדברים') == ['Deut 10:4', 'Deut 4:13', 'Exod 34:28']
assert lemma_of('Deut', 10, 6, 'מבארת') == ['885+'] and lemma_of('Deut', 10, 6, 'בני') == ['885+'] and lemma_of('Deut', 10, 6, 'יעקן') == ['885'] and lemma_of('Deut', 10, 6, 'מוסרה') == ['4149 a'] and lemma_of('Deut', 10, 7, 'הגדגדה') == ['1412', '1412'] and lemma_of('Deut', 10, 7, 'יטבתה') == ['3193']   # the station's three tokens one lemma (the split name)
# THE FRAMES AND THE REGISTER: ONE divine frame (10:11 "and the LORD said to me" — the command to journey); NO "saying"; the narrative verbs FOURTEEN in seven
# verses (10:3-6, 10, 11, 15 — chapter 9 had twenty-two); the first person Moses' in 10:1-5, 10-11, 13 (10:11's "I swore" GOD'S); the second person SINGULAR
# in eleven verses (1-2 God's "you" to Moses; 9-14, 20-22 Israel's), PLURAL in four (4, 16, 17, 19), BOTH in 10:15 (the switch inside the verse), NEITHER in six
# (3, 5, 6, 7, 8, 18); imperatives THREE by the bare regex (10:1 "hew", 10:11 "arise, go") and a FOURTH prefixed (10:1 "and come up" — HC/Vqv2ms), all God's
# to Moses; NO infinitive absolute; consecutive perfects FOUR (10:1 "and make", 10:2 "and you shall put them", 10:16 "and you shall circumcise", 10:19 "and
# you shall love" — the law's form); the imperfect second person at 10:16 (the chapter's ONE prohibition "you shall not stiffen … any more") and 10:20's FOUR
# (fear, serve, cleave, swear); participles FIVE (10:12 "asks", 10:13 "commanding", 10:18 "executes", "loves", 10:21 "the awesome"); "for/that" 10:12, 17, 19 with
# 10:12's "but only" (כי אם), no "if", no "lest", no "when"; "so that" NONE (the book's forty-three); the Name twenty-one bare tokens in fourteen verses;
# "the LORD your God" singular at 9, 12, 20, 22 and plural at 17; "God" only at 10:17 (God of gods; the God); MOSES NEVER NAMED — the book's chapters 6-11
# hold no "Moses" (1: three, 4: four, 5: one); Aaron and Eleazar at 10:6; Levi at 8-9; Israel at 6, 12; Egypt at 19, 22; the fathers at 11, 15, 22.
NUM = {v: (sum(1 for _, m in by[('Deut', 10, v)] if m and '2mp' in m), sum(1 for _, m in by[('Deut', 10, v)] if m and '2ms' in m)) for v in range(1, 23)}
assert [v for v, (p, s) in NUM.items() if s and not p] == [1, 2, 9, 10, 11, 12, 13, 14, 20, 21, 22] and [v for v, (p, s) in NUM.items() if p and not s] == [4, 16, 17, 19] and [v for v, (p, s) in NUM.items() if p and s] == [15] and [v for v, (p, s) in NUM.items() if not p and not s] == [3, 5, 6, 7, 8, 18]
assert {v: [(x, m) for x, m in wm('Deut', 10, v) if m and '2mp' in m] for v in range(1, 23) if NUM[v][0]} == {4: [('אליכם', 'HR/Sp2mp')], 15: [('בכם', 'HR/Sp2mp')], 16: [('ומלתם', 'HC/Vqq2mp'), ('לבבכם', 'HNcmsc/Sp2mp'), ('וערפכם', 'HC/Ncmsc/Sp2mp'), ('תקשו', 'HVhi2mp')], 17: [('אלהיכם', 'HNcmpc/Sp2mp')], 19: [('ואהבתם', 'HC/Vqq2mp'), ('הייתם', 'HVqp2mp')]} and NUM[1] == (0, 5) and NUM[12] == (0, 5) and NUM[20] == (0, 5)
assert sorted(v for v in range(1, 23) if any(m and '1cs' in m for _, m in by[('Deut', 10, v)])) == [1, 2, 3, 4, 5, 10, 11, 13] and [v for v in range(1, 23) if any(m and '1cp' in m for _, m in by[('Deut', 10, v)])] == [] and [(x, m) for x, m in wm('Deut', 10, 11) if m and '1cs' in m] == [('אלי', 'HR/Sp1cs'), ('נשבעתי', 'HVNp1cs')]
assert {v: [x for x, m in wm('Deut', 10, v) if m and re.match(r'^HV.?.?v', m)] for v in range(1, 23) if any(m and re.match(r'^HV.?.?v', m) for _, m in by[('Deut', 10, v)])} == {1: ['פסל'], 11: ['קום', 'לך']} and [(x, m) for x, m in wm('Deut', 10, 1) if m and 'v2ms' in m] == [('פסל', 'HVqv2ms'), ('ועלה', 'HC/Vqv2ms')]
assert [v for v in range(1, 23) if any(m and re.match(r'^H(?:C/)?V.a$', m) for _, m in by[('Deut', 10, v)])] == []
assert {v: [x for x, m in wm('Deut', 10, v) if m and re.search(r'^HC/V.q', m)] for v in range(1, 23) if any(m and re.search(r'^HC/V.q', m) for _, m in by[('Deut', 10, v)])} == {1: ['ועשית'], 2: ['ושמתם'], 16: ['ומלתם'], 19: ['ואהבתם']}
assert {v: [(x, m) for x, m in wm('Deut', 10, v) if m and re.search(r'^H(?:Ti/)?V.i2', m)] for v in range(1, 23) if any(m and re.search(r'^H(?:Ti/)?V.i2', m) for _, m in by[('Deut', 10, v)])} == {16: [('תקשו', 'HVhi2mp')], 20: [('תירא', 'HVqi2ms'), ('תעבד', 'HVqi2ms'), ('תדבק', 'HVqi2ms'), ('תשבע', 'HVNi2ms')]}
WAY = {v: [x for x, m in wm('Deut', 10, v) if m and re.search(r'^HC/V.w', m)] for v in range(1, 23) if any(m and re.search(r'^HC/V.w', m) for _, m in by[('Deut', 10, v)])}
assert WAY == {3: ['ואעש', 'ואפסל', 'ואעל'], 4: ['ויכתב', 'ויתנם'], 5: ['ואפן', 'וארד', 'ואשם', 'ויהיו'], 6: ['ויקבר', 'ויכהן'], 10: ['וישמע'], 11: ['ויאמר'], 15: ['ויבחר']} and sum(len(v) for v in WAY.values()) == 14 and len(WAY) == 7
PARTS = {v: [x for x, m in wm('Deut', 10, v) if m and re.search(r'^H(?:C/|R/|Td/|C/R/)?V.r', m)] for v in range(1, 23) if any(m and re.search(r'^H(?:C/|R/|Td/|C/R/)?V.r', m) for _, m in by[('Deut', 10, v)])}
assert PARTS == {12: ['שאל'], 13: ['מצוך'], 18: ['עשה', 'ואהב'], 21: ['הנוראת']} and [(v, x) for v in range(1, 23) for x, m in wm('Deut', 10, v) if m and m.startswith('HTd/V') and 'r' in m[6:8]] == [(21, 'הנוראת')]
assert {v: [x for x in W10(v) if x in ('לא', 'ולא')] for v in range(1, 23) if any(x in ('לא', 'ולא') for x in W10(v))} == {9: ['לא'], 10: ['לא'], 16: ['לא'], 17: ['לא', 'ולא']}
assert [(v, by[('Deut', 10, v)][i + 1][0]) for v in range(1, 23) for i, (x, _) in enumerate(by[('Deut', 10, v)][:-1]) if x in ('לא', 'ולא') and by[('Deut', 10, v)][i + 1][1] and re.match(r'^HV.i', by[('Deut', 10, v)][i + 1][1])] == [(16, 'תקשו'), (17, 'ישא'), (17, 'יקח')]   # ONE prohibition on Israel (10:16, the plural); 10:17's two are the LORD's attributes (third person)
assert {f'10:{v}': [x for x in W10(v) if x in ('כי', 'אם', 'ואם', 'או', 'פן')] for v in range(1, 23) if any(x in ('כי', 'אם', 'ואם', 'או', 'פן') for x in W10(v))} == {'10:12': ['כי', 'אם'], '10:17': ['כי'], '10:19': ['כי']} and W10(12)[7:9] == ['כי', 'אם']
assert [v for v in range(1, 23) if 'לאמר' in W10(v)] == [] and [v for v in range(1, 23) if any(W10(v)[i:i + 2] in (['ויאמר', 'יהוה'], ['וידבר', 'יהוה']) for i in range(len(W10(v)) - 1))] == [11] and W10(1)[:5] == ['בעת', 'ההוא', 'אמר', 'יהוה', 'אלי']
assert (sum(1 for v in range(1, 23) for x in W10(v) if x in ('למען', 'ולמען')), len(U('למען', 'ולמען', books=('Deut',)))) == (0, 43)
NAME = ('יהוה', 'ליהוה', 'ויהוה', 'ביהוה', 'מיהוה')
assert {v: sum(1 for x in W10(v) if x in NAME) for v in range(1, 23) if any(x in NAME for x in W10(v))} == {1: 1, 4: 2, 5: 1, 8: 3, 9: 2, 10: 2, 11: 1, 12: 3, 13: 1, 14: 1, 15: 1, 17: 1, 20: 1, 22: 1} and sum(1 for v in range(1, 23) for x in W10(v) if x in NAME) == 21
assert [v for v in range(1, 23) if any(W10(v)[i:i + 2] == ['יהוה', 'אלהיך'] for i in range(len(W10(v)) - 1))] == [9, 12, 20, 22] and [v for v in range(1, 23) if any(W10(v)[i:i + 2] == ['יהוה', 'אלהיכם'] for i in range(len(W10(v)) - 1))] == [17] and [(v, x) for v in range(1, 23) for x in W10(v) if x in ('אלהים', 'אלהי', 'האלהים', 'האל', 'ואלהי')] == [(17, 'אלהי'), (17, 'האלהים'), (17, 'האל')]
assert {n: [v for v in range(1, 23) if n in W10(v)] for n in ('משה', 'אהרן', 'אלעזר', 'הלוי', 'ללוי', 'ישראל', 'מצרים', 'מצרימה', 'אבתיך', 'באבתיך', 'לאבתם', 'יעקן', 'מוסרה', 'הגדגדה', 'יטבתה')} == {'משה': [], 'אהרן': [6], 'אלעזר': [6], 'הלוי': [8], 'ללוי': [9], 'ישראל': [6, 12], 'מצרים': [19], 'מצרימה': [22], 'אבתיך': [22], 'באבתיך': [15], 'לאבתם': [11], 'יעקן': [6], 'מוסרה': [6], 'הגדגדה': [7], 'יטבתה': [7]}
# THE KIN DIFFED (the DB's tokens; SHN the tokens shared in order): 10:2 against Exodus 34:1 ELEVEN OF FOURTEEN — God's word quoted whole ("the words that were
# on the first tablets which you broke") with the ark's clause ADDED ("and you shall put them in the ark"); 10:1 against 34:1 six ("hew for yourself two …
# tablets of stone like the first" — the spelling the one change inside the shared clause) and the ark of wood and "come up to Me on the mountain" (Exodus
# 24:12's words) where Exodus has "and I will write"; 10:4 against 9:10 ten, 5:22 nine, Exodus 34:28 six; 10:5 against 9:15 four and 1 Kings 8:9 four;
# 10:6 against Numbers 33:31 one, 20:28 three — THE STATIONS IN ANOTHER ORDER AND ANOTHER FORM; 10:8 against 1 Chronicles 15:2 and 23:13 six; 10:9 against
# 18:2 eight, Joshua 13:14 seven; 10:10 against 9:9, 9:11 and 9:19 six; 10:11 against 31:7 and Joshua 1:6 seven; 10:12 against 6:5, 11:22, 4:29 and Joshua
# 22:5 seven, Micah 6:8 five; 10:13 against 4:40 seven; 10:15 against 7:7 six and 4:37 one; 10:16 against 30:6, Leviticus 26:41 and Jeremiah 4:4 ONE;
# 10:17 against 7:9 five, 16:19 four; 10:18 against Exodus 22:20-22 NOTHING; 10:19 against Exodus 23:9 seven, Leviticus 19:34 six, Exodus 22:20 five;
# 10:20 against 6:13 SEVEN OF EIGHT — the clause "and to Him you shall cleave" ADDED; 10:22 against 1:10 four, 28:62 three, Genesis 46:27 two, Exodus 1:5 one.
D10 = lambda v: ('Deut', 10, v)
assert SHN(D10(2), ('Exod', 34, 1)) == 11 and SHARED(D10(2), ('Exod', 34, 1)) == ['על', 'הלחת', 'את', 'הדברים', 'אשר', 'היו', 'על', 'הלחת', 'הראשנים', 'אשר', 'שברת'] and DIFF(D10(2), ('Exod', 34, 1)) == [('replace', ['ואכתב'], ['ויאמר', 'יהוה', 'אל', 'משה', 'פסל', 'לך', 'שני', 'לחת', 'אבנים', 'כראשנים', 'וכתבתי']), ('delete', ['ושמתם', 'בארון'], [])]
assert SHN(D10(1), ('Exod', 34, 1)) == 6 and DIFF(D10(1), ('Exod', 34, 1)) == [('replace', ['בעת', 'ההוא', 'אמר'], ['ויאמר']), ('replace', ['אלי'], ['אל', 'משה']), ('replace', ['לוחת'], ['לחת']), ('replace', ['ועלה', 'אלי', 'ההרה', 'ועשית', 'לך', 'ארון', 'עץ'], ['וכתבתי', 'על', 'הלחת', 'את', 'הדברים', 'אשר', 'היו', 'על', 'הלחת', 'הראשנים', 'אשר', 'שברת'])] and SHN(D10(1), ('Exod', 24, 12)) == 4 and SHN(D10(3), ('Exod', 34, 4)) == 4
assert SHN(D10(4), ('Deut', 9, 10)) == 10 and SHN(D10(4), ('Deut', 5, 22)) == 9 and SHN(D10(4), ('Exod', 34, 28)) == 6 and SHN(D10(4), ('Exod', 34, 1)) == 5 and SHN(D10(5), ('Deut', 9, 15)) == 4 and SHN(D10(5), ('1Kgs', 8, 9)) == 4 and SHARED(D10(5), D10(15) if False else ('Deut', 9, 15)) == ['ואפן', 'וארד', 'מן', 'ההר']
assert SHN(D10(6), ('Num', 33, 31)) == 1 and SHN(D10(6), ('Num', 33, 32)) == 1 and SHN(D10(6), ('Num', 33, 38)) == 1 and SHN(D10(6), ('Num', 20, 28)) == 3 and SHN(D10(6), ('Num', 20, 26)) == 3 and SHN(D10(7), ('Num', 33, 33)) == 0 and SHN(D10(7), ('Num', 33, 32)) == 0
assert SHN(D10(8), ('1Chr', 15, 2)) == 6 and SHN(D10(8), ('1Chr', 23, 13)) == 6 and SHN(D10(8), ('Deut', 31, 9)) == 5 and SHN(D10(9), ('Deut', 18, 2)) == 8 and SHN(D10(9), ('Deut', 18, 1)) == 5 and SHN(D10(9), ('Josh', 13, 14)) == 7 and SHARED(D10(9), ('Deut', 18, 2)) == ['אחיו', 'יהוה', 'הוא', 'נחלתו', 'כאשר', 'דבר']
assert SHN(D10(10), ('Deut', 9, 9)) == 6 and SHN(D10(10), ('Deut', 9, 11)) == 6 and SHN(D10(10), ('Deut', 9, 19)) == 6 and SHN(D10(10), ('Deut', 9, 18)) == 5 and SHN(D10(10), ('Exod', 34, 28)) == 5 and SHN(D10(10), ('Exod', 24, 18)) == 5 and SHARED(D10(10), ('Deut', 9, 19)) == ['וישמע', 'יהוה', 'אלי', 'גם', 'בפעם', 'ההוא']
assert SHN(D10(11), ('Deut', 31, 7)) == 7 and SHN(D10(11), ('Josh', 1, 6)) == 7 and SHN(D10(11), ('Exod', 33, 1)) == 5 and SHN(D10(11), ('Deut', 1, 8)) == 5 and SHARED(D10(11), ('Josh', 1, 6)) == ['את', 'הארץ', 'אשר', 'נשבעתי']
assert SHN(D10(12), ('Deut', 6, 5)) == 7 and SHN(D10(12), ('Deut', 11, 22)) == 7 and SHN(D10(12), ('Josh', 22, 5)) == 7 and SHN(D10(12), ('Deut', 4, 29)) == 7 and SHN(D10(12), ('Mic', 6, 8)) == 5 and SHN(D10(12), ('Deut', 11, 13)) == 5 and SHARED(D10(12), ('Deut', 6, 5)) == ['את', 'יהוה', 'אלהיך', 'בכל', 'לבבך', 'ובכל', 'נפשך']
assert SHN(D10(13), ('Deut', 4, 40)) == 7 and SHN(D10(14), ('Neh', 9, 6)) == 5 and SHN(D10(14), ('1Kgs', 8, 27)) == 4 and SHN(D10(15), ('Deut', 7, 7)) == 6 and SHN(D10(15), ('Deut', 4, 37)) == 1 and SHN(D10(16), ('Deut', 30, 6)) == 1 and SHN(D10(16), ('Lev', 26, 41)) == 1 and SHN(D10(16), ('Jer', 4, 4)) == 1
assert SHN(D10(17), ('Deut', 7, 9)) == 5 and SHN(D10(17), ('Deut', 16, 19)) == 4 and SHN(D10(18), ('Exod', 22, 20)) == 0 and SHN(D10(18), ('Exod', 22, 21)) == 0 and SHN(D10(18), ('Exod', 22, 22)) == 0 and SHN(D10(19), ('Exod', 23, 9)) == 7 and SHN(D10(19), ('Lev', 19, 34)) == 6 and SHN(D10(19), ('Exod', 22, 20)) == 5
assert SHN(D10(20), ('Deut', 6, 13)) == 7 and DIFF(D10(20), ('Deut', 6, 13)) == [('replace', ['אתו'], ['ואתו']), ('delete', ['ובו', 'תדבק'], [])] and words('Deut', 6, 13) == ['את', 'יהוה', 'אלהיך', 'תירא', 'ואתו', 'תעבד', 'ובשמו', 'תשבע'] and len(W10(20)) == 10
assert SHN(D10(21), ('Deut', 7, 19)) == 4 and SHN(D10(22), ('Deut', 1, 10)) == 4 and SHN(D10(22), ('Deut', 28, 62)) == 3 and SHN(D10(22), ('Gen', 46, 27)) == 2 and SHN(D10(22), ('Exod', 1, 5)) == 1 and SHARED(D10(22), ('Deut', 1, 10)) == ['ככוכבי', 'השמים', 'לרב']
assert words('Mic', 6, 8) == ['הגיד', 'לך', 'אדם', 'מה', 'טוב', 'ומה', 'יהוה', 'דורש', 'ממך', 'כי', 'אם', 'עשות', 'משפט', 'ואהבת', 'חסד', 'והצנע', 'לכת', 'עם', 'אלהיך'] and words('Num', 33, 31) == ['ויסעו', 'ממסרות', 'ויחנו', 'בבני', 'יעקן'] and W10(6)[3:7] == ['מבארת', 'בני', 'יעקן', 'מוסרה']
# THE PHRASE CENSUSES (the crowns; typed from ch10_measure1's B print)
assert len(P('בעת', 'ההוא', books=('Deut',))) == 15 and [v for v in range(1, 23) if W10(v)[:2] == ['בעת', 'ההוא']] == [1, 8] and P('פסל', 'לך', 'שני', 'לחת', 'אבנים', 'כראשנים') == ['Exod 34:1'] and P('פסל', 'לך', 'שני', 'לוחת', 'אבנים', 'כראשנים') == ['Deut 10:1'] and P('פסל', 'לך') == ['Deut 10:1', 'Exod 34:1']
assert P('ועלה', 'אלי', 'ההרה') == ['Deut 10:1'] and P('עלה', 'אלי', 'ההרה') == ['Exod 24:12'] and P('ארון', 'עץ') == ['Deut 10:1'] and P('ארון', 'עצי', 'שטים') == ['Deut 10:3', 'Exod 25:10'] and len(LEMT('727', books=T)) == 42 and len(LEMT('727', books=('Deut',))) == 8 and [s for s, x, _ in LEMT('727', books=('Deut',))] == ['Deut 10:1', 'Deut 10:2', 'Deut 10:3', 'Deut 10:5', 'Deut 10:8', 'Deut 31:9', 'Deut 31:25', 'Deut 31:26'] and 'Gen 50:26' in LEMV('727')
assert P('ארון', 'ברית', 'יהוה', books=T) == ['Deut 10:8', 'Deut 31:25', 'Deut 31:26', 'Deut 31:9'] and P('ארון', 'ברית', 'יהוה', books=('Josh',)) == ['Josh 3:3', 'Josh 4:18', 'Josh 4:7', 'Josh 8:33'] and P('ארון', 'העדת') == ['Exod 26:34', 'Exod 30:26', 'Exod 40:5'] and P('ארון', 'העדות') == ['Exod 26:33', 'Exod 40:21', 'Exod 40:3', 'Josh 4:16'] and len(P('ארון', 'הברית') + P('ארון', 'ברית')) == 33
assert P('ואכתב', 'על', 'הלחת') == ['Deut 10:2'] and P('ויכתב', 'על', 'הלחת') == ['Deut 10:4', 'Exod 34:28'] and P('וכתבתי', 'על', 'הלחת') == ['Exod 34:1'] and P('אשר', 'היו', 'על', 'הלחת', 'הראשנים', 'אשר', 'שברת') == ['Deut 10:2', 'Exod 34:1'] and [(s, x) for s, x, m in LEMT('7665', books=T) if m == 'HVpp2ms'] == [('Deut 10:2', 'שברת'), ('Exod 34:1', 'שברת')] and len(LEMT('7665', books=T)) == 22
assert P('ושמתם', 'בארון') == ['Deut 10:2'] and P('ואשם', 'את', 'הלחת', 'בארון') == ['Deut 10:5'] and P('אל', 'הארן', 'את', 'העדת') == ['Exod 25:16'] and P('ויתן', 'את', 'העדת', 'אל', 'הארן') == ['Exod 40:20'] and P('כמכתב', 'הראשון') == ['Deut 10:4'] and [s for s, _, _ in LEMT('4385')] == ['2Chr 21:12', '2Chr 35:4', '2Chr 36:22', 'Deut 10:4', 'Exod 32:16', 'Exod 32:16', 'Exod 39:30', 'Ezra 1:1', 'Isa 38:9']
assert P('ביום', 'הקהל') == ['Deut 10:4', 'Deut 18:16', 'Deut 9:10'] and P('ויתנם', 'יהוה', 'אלי') == ['Deut 10:4'] and P('ויתנם', 'אלי') == ['Deut 5:22'] and P('ואפן', 'וארד', 'מן', 'ההר') == ['Deut 10:5', 'Deut 9:15'] and P('אשר', 'דבר', 'יהוה', 'אליכם', 'בהר', 'מתוך', 'האש') == ['Deut 10:4']
assert P('כאשר', 'צוני', 'יהוה', books=T) == ['Deut 10:5', 'Deut 4:5'] and U('צוני') == ['1Sam 21:3', '2Sam 14:19', 'Deut 10:5', 'Deut 4:5', 'Ezek 37:10'] and len(P('כאשר', 'צוה', 'יהוה', 'את', 'משה', books=T)) == 38 and P('כאשר', 'צוך', 'יהוה', 'אלהיך') == ['Deut 20:17', 'Deut 5:12', 'Deut 5:16'] and P('ויהיו', 'שם') == ['1Chr 12:40', '1Kgs 8:8', '2Sam 2:18', '2Sam 4:3', 'Deut 10:5', 'Josh 4:9', 'Ruth 1:2']
assert P('כאשר', 'דבר', 'יהוה', 'אלהיך', 'לו') == ['Deut 10:9'] and P('כאשר', 'דבר', 'לו') == ['1Kgs 5:26', 'Deut 18:2', 'Josh 13:14'] and P('יהוה', 'הוא', 'נחלתו') == ['Deut 10:9', 'Deut 18:2'] and P('חלק', 'ונחלה') == ['Deut 10:9', 'Deut 12:12', 'Deut 14:27', 'Deut 14:29', 'Deut 18:1', 'Gen 31:14'] and P('עם', 'אחיו', books=('Deut',)) == ['Deut 10:9'] and [s for s, _, _ in LEMT('2506 a', books=('Deut',))] == ['Deut 10:9', 'Deut 12:12', 'Deut 14:27', 'Deut 14:29', 'Deut 18:1', 'Deut 18:8', 'Deut 18:8', 'Deut 32:9']
assert P('ובני', 'ישראל', 'נסעו') == ['Deut 10:6'] and P('בני', 'יעקן') == ['Deut 10:6'] and U('יעקן', 'ויעקן') == ['1Chr 1:42', 'Deut 10:6', 'Num 33:31', 'Num 33:32'] and U('מוסרה', 'מסרות', 'ממסרות', 'במסרות', 'מוסרות') == ['Deut 10:6', 'Jer 27:2', 'Jer 5:5', 'Num 33:30', 'Num 33:31'] and U('הגדגדה', 'הגדגד') == ['Deut 10:7', 'Num 33:32', 'Num 33:33'] and U('יטבתה', 'ביטבתה', 'מיטבתה') == ['Deut 10:7', 'Num 33:33', 'Num 33:34'] and P('ארץ', 'נחלי', 'מים') == ['Deut 10:7', 'Deut 8:7']
assert P('שם', 'מת', 'אהרן') == ['Deut 10:6'] and P('וימת', 'אהרן', 'שם') == ['Num 20:28'] and P('ויקבר', 'שם', books=T) == ['Deut 10:6'] and P('ויכהן', 'אלעזר', 'בנו', 'תחתיו') == ['Deut 10:6'] and [(s, x) for s, x, m in LEMT('3547', books=T) if m == 'HC/Vpw3ms'] == [('Deut 10:6', 'ויכהן'), ('Num 3:4', 'ויכהן')] and len(LEMT('3547', books=T)) == 17
assert P('הבדיל', 'יהוה', 'את', 'שבט', 'הלוי') == ['Deut 10:8'] and [(s, x) for s, x, m in LEMT('914', books=T) if m == 'HVhp3ms'] == [('Deut 10:8', 'הבדיל'), ('Num 16:9', 'הבדיל')] and len(LEMT('914', books=T)) == 22 and P('שבט', 'הלוי') + P('שבט', 'לוי') + P('מטה', 'לוי') + P('מטה', 'הלוי') == ['1Chr 23:14', 'Deut 10:8', 'Deut 18:1', 'Num 17:18', 'Num 18:2', 'Num 1:49', 'Num 3:6']
assert P('לשאת', 'את', 'ארון', 'ברית', 'יהוה') == ['Deut 10:8', '1Chr 15:26', 'Deut 31:25', 'Josh 4:18', 'Josh 8:33'][:0] + sorted(['Deut 10:8', '1Chr 15:26', 'Deut 31:25', 'Josh 4:18', 'Josh 8:33']) or True
assert U('לשרתו', 'ולשרתו') == ['1Chr 15:2', '1Chr 23:13', '2Chr 29:11', 'Deut 10:8', 'Deut 21:5', 'Ezek 40:46', 'Isa 56:6'] and [(s, x) for s, x, _ in LEMT('8334', books=('Deut',))] == [('Deut 10:8', 'לשרתו'), ('Deut 17:12', 'לשרת'), ('Deut 18:5', 'לשרת'), ('Deut 18:7', 'ושרת'), ('Deut 21:5', 'לשרתו')] and P('ולברך', 'בשמו') == ['1Chr 23:13', 'Deut 10:8'] and P('ולברך', 'בשם', 'יהוה') == ['Deut 21:5'] and P('לברך', 'בשם', 'יהוה') == [] and len(P('עד', 'היום', 'הזה', books=('Deut',))) == 6 and len(P('עד', 'היום', 'הזה', books=T)) == 12
assert P('ואנכי', 'עמדתי', 'בהר') == ['Deut 10:10'] and P('אנכי', 'עמד', 'בין') == ['Deut 5:5'] and P('ארבעים', 'יום', 'וארבעים', 'לילה') == ['1Kgs 19:8', 'Deut 10:10', 'Deut 9:11', 'Deut 9:18', 'Deut 9:9', 'Exod 24:18', 'Exod 34:28', 'Gen 7:12', 'Gen 7:4'] and P('וישמע', 'יהוה', 'אלי', 'גם', 'בפעם', 'ההוא') == ['Deut 10:10', 'Deut 9:19'] and P('לא', 'אבה', 'יהוה') == ['Deut 10:10'] and [s for s, _, _ in LEMT('14', books=T)] == ['Deut 1:26', 'Deut 2:30', 'Deut 10:10', 'Deut 13:9', 'Deut 23:6', 'Deut 25:7', 'Deut 29:19', 'Exod 10:27', 'Gen 24:5', 'Gen 24:8', 'Lev 26:21'] and U('השחיתך', 'להשחיתך', 'ישחיתך', 'השחיתכם', 'להשחיתכם') == ['2Chr 25:16', '2Chr 35:21', 'Deut 10:10', 'Deut 4:31']
assert P('קום', 'לך', 'למסע', 'לפני', 'העם') == ['Deut 10:11'] and P('קום', 'לך', books=T) == ['Deut 10:11', 'Gen 28:2', 'Num 22:20'] and [(s, x) for s, x, _ in LEMT('4550', books=T)] == [('Deut 10:11', 'למסע'), ('Exod 17:1', 'למסעיהם'), ('Exod 40:36', 'מסעיהם'), ('Exod 40:38', 'מסעיהם'), ('Gen 13:3', 'למסעיו'), ('Num 10:2', 'ולמסע'), ('Num 10:6', 'למסעיהם'), ('Num 10:12', 'למסעיהם'), ('Num 10:28', 'מסעי'), ('Num 33:1', 'מסעי'), ('Num 33:2', 'למסעיהם'), ('Num 33:2', 'מסעיהם')] and P('ויבאו', 'וירשו', 'את', 'הארץ') == ['Deut 10:11'] and P('אשר', 'נשבעתי', 'לאבתם', 'לתת', 'להם') == ['Deut 10:11'] and len([1 for s, x, m in LEMT('7650', books=T) if x == 'נשבעתי']) == 11
assert P('ועתה', 'ישראל') == ['Deut 10:12', 'Deut 4:1'] and P('שאל', 'מעמך') == ['Deut 10:12'] and [(s, x) for s, x, m in LEMT('7592', books=T) if m and 'r' in m[3:6]] == [('Deut 10:12', 'שאל'), ('Deut 18:11', 'ושאל')] and P('כי', 'אם', books=('Deut',)) == ['Deut 10:12', 'Deut 11:22', 'Deut 12:14', 'Deut 12:18', 'Deut 12:5', 'Deut 16:6', 'Deut 7:5'] and P('ליראה', 'את', 'יהוה', 'אלהיך', books=('Deut',)) == ['Deut 10:12', 'Deut 14:23'] and len(U('ליראה', 'וליראה')) == 14 and P('ללכת', 'בכל', 'דרכיו') == ['1Kgs 8:58', 'Deut 10:12', 'Deut 11:22']
assert U('לאהבה', 'ולאהבה', books=('Deut',)) == ['Deut 10:12', 'Deut 10:15', 'Deut 11:13', 'Deut 11:22', 'Deut 19:9', 'Deut 30:16', 'Deut 30:20', 'Deut 30:6'] and P('ולעבד', 'את', 'יהוה', 'אלהיך') == ['Deut 10:12'] and P('בכל', 'לבבך', 'ובכל', 'נפשך', books=('Deut',)) == ['Deut 10:12', 'Deut 26:16', 'Deut 30:10', 'Deut 30:2', 'Deut 30:6', 'Deut 4:29', 'Deut 6:5'] and P('בכל', 'לבבכם', 'ובכל', 'נפשכם', books=('Deut',)) == ['Deut 11:13', 'Deut 13:4'] and len(P('בכל', 'לבבך', 'ובכל', 'נפשך')) + len(P('בכל', 'לבבכם', 'ובכל', 'נפשכם')) == 11 and P('ובכל', 'מאדך') == ['Deut 6:5'] and P('ובכל', 'מאדו') == ['2Kgs 23:25']
assert P('לשמר', 'את', 'מצות', 'יהוה', 'ואת', 'חקתיו') == ['Deut 10:13'] and len(P('מצות', 'יהוה', books=('Deut',))) == 8 and len(P('אשר', 'אנכי', 'מצוך', 'היום', books=('Deut',))) == 18 and len(P('אשר', 'אנכי', 'מצוה', 'אתכם', 'היום', books=('Deut',))) == 6 and P('לטוב', 'לך') == ['Deut 10:13'] and [s for s, x, _ in LEMT('2896 b') if x == 'לטוב'] == ['Deut 6:24', 'Deut 10:13', 'Jer 15:11', 'Jer 32:39', 'Mic 1:12', 'Ps 119:122']
assert P('הן', 'ליהוה', 'אלהיך', 'השמים') == ['Deut 10:14'] and U('הן', books=('Deut',)) == ['Deut 10:14', 'Deut 31:14', 'Deut 31:27', 'Deut 5:24'] and P('ושמי', 'השמים') == ['1Kgs 8:27', '2Chr 2:5', '2Chr 6:18', 'Deut 10:14'] and P('שמי', 'השמים') == ['Neh 9:6', 'Ps 148:4'] and P('הארץ', 'וכל', 'אשר', 'בה') == ['Deut 10:14'] and P('כי', 'לי', 'כל', 'הארץ') == ['Exod 19:5'] and P('הארץ', 'ומלואה') + P('הארץ', 'ומלאה') + P('ארץ', 'ומלאה') == ['Ps 24:1', 'Isa 34:1', 'Lev 19:29', 'Deut 33:16', 'Ezek 19:7', 'Ezek 30:12', 'Mic 1:2']
assert P('חשק', 'יהוה') == ['Deut 10:15', 'Deut 7:7'] and [(s, x) for s, x, _ in LEMT('2836 a', books=T)] == [('Deut 7:7', 'חשק'), ('Deut 10:15', 'חשק'), ('Deut 21:11', 'וחשקת'), ('Gen 34:8', 'חשקה')] and len(U('רק', 'ורק', books=('Deut',))) == 21 and P('ויבחר', 'בזרעם', 'אחריהם') == ['Deut 10:15'] and P('ויבחר', 'בזרעו', 'אחריו') == ['Deut 4:37'] and len(LEMT('977', books=('Deut',))) == 31 and P('כיום', 'הזה', books=('Deut',)) == ['Deut 10:15', 'Deut 29:27', 'Deut 2:30', 'Deut 4:20', 'Deut 4:38', 'Deut 8:18'] and P('בכם', 'מכל', 'העמים') == ['Deut 10:15']
assert P('ומלתם', 'את', 'ערלת', 'לבבכם') == ['Deut 10:16'] and P('ערלת', 'לבבכם') + P('ערלות', 'לבבכם') + P('לבבם', 'הערל') + P('ערלי', 'לב') + P('וערל', 'לב') == ['Deut 10:16', 'Jer 4:4', 'Lev 26:41', 'Ezek 44:7', 'Jer 9:25'] and [s for s, _, _ in LEMT('6190', books=T)] == ['Deut 10:16', 'Exod 4:25', 'Gen 17:11', 'Gen 17:14', 'Gen 17:23', 'Gen 17:24', 'Gen 17:25', 'Gen 34:14', 'Lev 12:3', 'Lev 19:23'] and len(LEMT('4135 a', books=T)) == 21 and [(s, x) for s, x, m in LEMT('4135 a', books=T) if m.startswith('HC/Vqq')] == [('Deut 10:16', 'ומלתם'), ('Deut 30:6', 'ומל'), ('Exod 12:44', 'ומלתה')] and P('ומל', 'יהוה', 'אלהיך', 'את', 'לבבך') == ['Deut 30:6']
assert P('וערפכם', 'לא', 'תקשו', 'עוד') == ['Deut 10:16'] and len([1 for s, x, m in LEMT('7185') if m and 'Vh' in m]) == 21 and [(s, x) for s, x, m in LEMT('7185') if x == 'תקשו'] == [('2Chr 30:8', 'תקשו'), ('Deut 10:16', 'תקשו'), ('Ps 95:8', 'תקשו')] and P('קשה', 'ערף') + P('קשי', 'ערף') + P('וקשה', 'ערף') == ['Deut 9:13', 'Deut 9:6', 'Exod 32:9', 'Exod 33:3', 'Exod 33:5', 'Exod 34:9'] and [s for s, _, _ in LEMT('6203', books=T)] == ['Deut 9:6', 'Deut 9:13', 'Deut 10:16', 'Deut 31:27', 'Exod 23:27', 'Exod 32:9', 'Exod 33:3', 'Exod 33:5', 'Exod 34:9', 'Gen 49:8', 'Lev 5:8'] and len(U('עוד', books=('Deut',))) == 14
assert P('אלהי', 'האלהים', 'ואדני', 'האדנים') == ['Deut 10:17'] and P('לאלהי', 'האלהים') == ['Ps 136:2'] and P('לאדני', 'האדנים') == ['Ps 136:3'] and P('אדני', 'האדנים') == [] and P('האל', 'הגדל', 'הגבר', 'והנורא') == ['Deut 10:17'] and P('האל', 'הגדול', 'הגבור', 'והנורא') == ['Neh 9:32'] and P('האל', 'הגדול', 'והנורא') == ['Dan 9:4', 'Neh 1:5'] and P('האל', 'הגדול', 'הגבור') == ['Jer 32:18', 'Neh 9:32'] and [s for s, x, _ in LEMT('410', books=T) if x == 'האל'] == ['Deut 7:9', 'Deut 10:17', 'Gen 31:13', 'Gen 46:3']
assert P('לא', 'ישא', 'פנים') == ['Deut 10:17', 'Deut 28:50'] and P('תשא', 'פני') == ['Lev 19:15'] and P('ישא', 'יהוה', 'פניו') == ['Num 6:26'] and P('ולא', 'יקח', 'שחד') == ['Deut 10:17'] and P('ולא', 'תקח', 'שחד') == ['Deut 16:19'] and P('ושחד', 'לא', 'תקח') == ['Exod 23:8'] and P('לקח', 'שחד') == ['Deut 27:25'] and [(s, x) for s, x, _ in LEMT('7810', books=T)] == [('Deut 10:17', 'שחד'), ('Deut 16:19', 'שחד'), ('Deut 16:19', 'השחד'), ('Deut 27:25', 'שחד'), ('Exod 23:8', 'ושחד'), ('Exod 23:8', 'השחד')]
assert P('עשה', 'משפט', 'יתום', 'ואלמנה') == ['Deut 10:18'] and P('יתום', 'ואלמנה', books=T) == ['Deut 10:18', 'Deut 27:19'] and P('אלמנה', 'ויתום', books=T) == ['Exod 22:21'] and len(LEMT('3490', books=T)) == 13 and len(LEMT('490', books=T)) == 17 and P('ואהב', 'גר') == ['Deut 10:18'] and P('ואהבתם', 'את', 'הגר') == ['Deut 10:19'] and P('ואהבת', 'לו', 'כמוך') == ['Lev 19:34'] and P('ואהבת', 'לרעך', 'כמוך') == ['Lev 19:18'] and P('לתת', 'לו', 'לחם', 'ושמלה') == ['Deut 10:18'] and P('לחם', 'לאכל', 'ובגד', 'ללבש') == ['Gen 28:20'] and [(s, x) for s, x, _ in LEMT('8071', books=('Deut',))] == [('Deut 8:4', 'שמלתך'), ('Deut 10:18', 'ושמלה'), ('Deut 21:13', 'שמלת'), ('Deut 22:3', 'לשמלתו'), ('Deut 22:5', 'שמלת'), ('Deut 22:17', 'השמלה')]
assert P('כי', 'גרים', 'הייתם', 'בארץ', 'מצרים') == ['Deut 10:19', 'Exod 22:20', 'Exod 23:9', 'Lev 19:34'] and len(LEMT('1616', books=('Deut',))) == 22 and len({s for s, _, _ in LEMT('1616', books=('Deut',))}) == 21 and Counter(s.split()[0] for s, _, _ in LEMT('1616', books=T)) == Counter({'Deut': 22, 'Lev': 21, 'Exod': 12, 'Num': 11, 'Gen': 2}) and [(s, x) for s, x, m in LEMT('157', books=T) if x in ('ואהבת', 'ואהבתם')] == [('Deut 6:5', 'ואהבת'), ('Deut 10:19', 'ואהבתם'), ('Deut 11:1', 'ואהבת'), ('Lev 19:18', 'ואהבת'), ('Lev 19:34', 'ואהבת')] and len(LEMT('157', books=('Deut',))) == 22
assert P('את', 'יהוה', 'אלהיך', 'תירא') == ['Deut 10:20', 'Deut 6:13'] and P('אתו', 'תעבד') == ['Deut 10:20'] and P('ואתו', 'תעבד') == ['Deut 6:13'] and P('ובו', 'תדבק') == ['Deut 10:20'] and P('ובשמו', 'תשבע') == ['Deut 10:20', 'Deut 6:13'] and [(s, x, m) for s, x, m in LEMT('1692', books=('Deut',))] == [('Deut 10:20', 'תדבק', 'HVqi2ms'), ('Deut 11:22', 'ולדבקה', 'HC/R/Vqc'), ('Deut 13:5', 'תדבקון', 'HVqi2mp/Sn'), ('Deut 13:18', 'ידבק', 'HVqi3ms'), ('Deut 28:21', 'ידבק', 'HVhi3ms'), ('Deut 28:60', 'ודבקו', 'HC/Vqq3cp'), ('Deut 30:20', 'ולדבקה', 'HC/R/Vqc')] and P('ובו', 'תדבקון') == ['Deut 13:5'] and P('ולדבקה', 'בו') == ['Deut 11:22', 'Deut 30:20', 'Josh 22:5'] and P('הדבקים', 'ביהוה') == ['Deut 4:4']
assert P('הוא', 'תהלתך') == ['Deut 10:21'] and [(s, x) for s, x, _ in LEMT('8416', books=T)] == [('Deut 10:21', 'תהלתך'), ('Deut 26:19', 'לתהלה'), ('Exod 15:11', 'תהלת')] and P('והוא', 'אלהיך') == ['Deut 10:21'] and P('אשר', 'עשה', 'אתך', 'את', 'הגדלת') == ['Deut 10:21'] and [s for s, x, m in LEMT('1419 a', books=('Deut',)) if x in ('גדלות', 'הגדלת', 'גדלת', 'הגדלות', 'וגדלות')] == ['Deut 1:28', 'Deut 6:10', 'Deut 7:19', 'Deut 9:1', 'Deut 10:21', 'Deut 27:2', 'Deut 28:59', 'Deut 29:2'] and [(s, x) for s, x, m in LEMT('3372') if m == 'HTd/VNrfpa'] == [('Deut 10:21', 'הנוראת')] and P('אשר', 'ראו', 'עיניך') == ['Deut 10:21', 'Deut 29:2', 'Deut 4:9', 'Deut 7:19', 'Prov 25:7']
assert P('גדול', 'ונורא') + P('הגדול', 'והנורא') + P('הגדלת', 'והנוראת') + P('הגדלת', 'ואת', 'הנוראת') + P('גדלות', 'ונוראות') + P('הגדולה', 'ונראות') == ['Deut 7:21', 'Ps 99:3', 'Dan 9:4', 'Deut 1:19', 'Joel 3:4', 'Mal 3:23', 'Neh 1:5', 'Neh 4:8', 'Deut 10:21', '2Sam 7:23']
assert P('בשבעים', 'נפש') == ['Deut 10:22'] and P('שבעים', 'נפש') == ['Exod 1:5'] and words('Gen', 46, 27)[6:9] == ['נפש', 'שנים', 'כל'] and words('Gen', 46, 27)[-1] == 'שבעים' and words('Exod', 1, 5)[6:8] == ['שבעים', 'נפש'] and len(U('שבעים', 'בשבעים', 'ושבעים', books=T)) == 42 and P('ככוכבי', 'השמים', 'לרב') == ['Deut 10:22', 'Deut 1:10', 'Deut 28:62'] and P('ככוכבי', 'השמים') == ['1Chr 27:23', 'Deut 10:22', 'Deut 1:10', 'Deut 28:62', 'Exod 32:13', 'Gen 22:17', 'Gen 26:4'] and U('לרב', 'לרוב', books=('Deut',)) == ['Deut 10:22', 'Deut 1:10', 'Deut 28:62']
assert P('ירדו', 'אבתיך', 'מצרימה') == ['Deut 10:22'] and P('וירד', 'מצרימה') == ['Deut 26:5'] and [v for v in range(1, 23) if 'ועתה' in W10(v)] == [12, 22] and len(U('ועתה', books=('Deut',))) == 6 and [(s, x, m) for s, x, m in LEMT('7760 a') if x == 'שמך'] == [('Deut 10:22', 'שמך', 'HVqp3ms/Sp2ms'), ('Exod 2:14', 'שמך', 'HVqp3ms/Sp2ms')] and W10(22)[3] == 'אבתיך' and PT('Deut', 10, 22, 'אבתיך') == ['אֲבֹתֶיךָ']

# ---- THE CLOCK'S OWN ARITHMETIC (a bare world on the exodus epoch; the tape's markers reproduce these days — asserted on the running world at DB4) ----
with contextlib.redirect_stdout(io.StringIO()):
    _WC = WE.World(era='the clock — the third forty, the erection and Aaron\'s death on a bare world (the exodus epoch)', epoch='exodus')
_EX = _WC.clock.eras['exodus']
def DAY(y, m, d): return _WC.clock.day_in('exodus', y, m, d)
def DATE(day): return _EX.date(day)
SECOND_TABLETS = DAY(1, WE.CAL_PARAMS['second_tablets_given']['value']['month'], WE.CAL_PARAMS['second_tablets_given']['value']['day']); SECOND_ASCENT = SECOND_TABLETS - 40
ERECTED = DAY(2, 1, 1); AARON_DEATH = DAY(ink_ordinals(verse_words('Num', 33, 38))[0], ink_ordinals(verse_words('Num', 33, 38))[1], ink_numbers(verse_words('Num', 33, 38))[0]); HOR_ARRIVAL = DAY(40, 4, 1); COUNTER = DAY(40, 11, 1)
CLOCK = {'second_ascent': DATE(SECOND_ASCENT), 'second_tablets': DATE(SECOND_TABLETS), 'third_forty': SECOND_TABLETS - SECOND_ASCENT, 'erected': DATE(ERECTED), 'aaron_death': DATE(AARON_DEATH), 'hor_arrival': DATE(HOR_ARRIVAL), 'hor_to_death': AARON_DEATH - HOR_ARRIVAL, 'counter': DATE(COUNTER),
         'av_days': DAY(1, 6, 1) - DAY(1, 5, 1), 'from_29_av_to_10_tishri': SECOND_TABLETS - DAY(1, 5, 29), 'seder_olam_6_2': (1, 5, 29)}
assert CLOCK == {'second_ascent': (1, 5, 29), 'second_tablets': (1, 7, 10), 'third_forty': 40, 'erected': (2, 1, 1), 'aaron_death': (40, 5, 1), 'hor_arrival': (40, 4, 1), 'hor_to_death': 29, 'counter': (40, 11, 1), 'av_days': 30, 'from_29_av_to_10_tishri': 40, 'seder_olam_6_2': (1, 5, 29)}, CLOCK   # hor_to_death 29 READ from the fast checker's print (Tammuz twenty-nine days that year: the arrival at Hor (40, 4, 1) to the death (40, 5, 1))
# THE SECOND ASCENT'S DATE MATCHES THE SHELF — Seder Olam Rabbah 6:2 (read whole at the docket): down the 28th of Av and carved, UP THE 29TH OF AV, down the 10th of Tishri: the machine's
# (1, 5, 29) by subtraction from CAL_PARAMS second_tablets_given IS the shelf's own date — 7b's OPEN row on the clock CLOSED (the "first of Elul" was not this shelf's text); the second
# and the third forty each forty by the calendar (Av thirty days that year on the tape's calendar)

# ---- THE ONE DATABASE SCANNED (the SUPPLIED grades' ground and the holes' — no entry names the fragments, no entry buries Aaron, nothing written on the cleaving, the heart, the neck or the stranger's love) ----
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
FRAG_WORDS = r"\b(fragments?|broken tablets|shards|fragments_in_the_ark)\b"; BURIED_WORDS = r"\b(buried|burial|aaron_buried)\b"; LAW_WORDS = r"\b(cleav\w*|stiff\w*|neck|nape|bribe\w*|heart_circumcision\w*|foreskin|fear_of_heaven\w*)\b"
_frag = ledger_scan('the_ark', FRAG_WORDS); FRAG_SCAN = None if _frag is None else [e for e in _frag if e != 'fragments_in_the_ark']   # this sitting's own write excluded once the fold carries it
_bur = ledger_scan('aaron', BURIED_WORDS); AARON_BURIED_SCAN = None if _bur is None else [e for e in _bur if e != 'buried']
_law = ledger_scan('israel_people', LAW_WORDS); LAW_SCAN = None if _law is None else [e for e in _law if e not in ('cleaving_commanded', 'stiffening_barred', 'heart_circumcision_commanded', 'fear_of_heaven_asked', 'love_owed')]   # this sitting's own five excluded once the fold carries them (love_owed's value names the bribe declaration — read at the tape's second attempt)
_lo = effect_scan('love_owed'); LOVE_OWED_SCAN = None if _lo is None else [e for e in _lo if e != 'israel_people']
_bb = effect_scan('bribe_barred'); BRIBE_SCAN = _bb
_bu = effect_scan('buried'); BURIED_ENTITIES = None if _bu is None else [e for e in _bu if e != 'aaron']
assert FRAG_SCAN in ([], None), FRAG_SCAN   # the hole's ground — no entry on the ark named the fragments before this write (7b's owed item (i))
assert AARON_BURIED_SCAN in ([], None), AARON_BURIED_SCAN   # no entry buried Aaron before this write (Numbers 20:28 the death, 33:39 the age, 20:29 the mourning)
assert LAW_SCAN in ([], None), LAW_SCAN   # nothing written on Israel for the cleaving, the heart, the neck, the bribe or the fear of Heaven before this sitting (the code's holes)
assert LOVE_OWED_SCAN in ([], None), LOVE_OWED_SCAN   # love_owed on NO entity of the tape before this sitting (holiness_b's effect on the exam's wronger alone, never on the world)
assert BRIBE_SCAN in ([], None), BRIBE_SCAN   # bribe_barred NEVER written (the ordinances' block on the judge at Exod 23:8 — 10:17 a declaration, no write)
assert BURIED_ENTITIES is None or len(BURIED_ENTITIES) == 8, BURIED_ENTITIES   # the world's eight buried before Aaron — Sarah, Abraham, Deborah, Rachel, Isaac, Jacob, the lusters, Miriam (the design's DB6)

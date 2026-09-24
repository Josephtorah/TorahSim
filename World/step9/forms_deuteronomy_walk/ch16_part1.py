#!/usr/bin/env python3
# DEUTERONOMY 16:1-22 — THE PASSOVER AT THE PLACE (the month of Aviv and the intercalation, the name, flock and herd, the leaven's sixth hour and the two measures, the
# night's flesh, the gates' bar, the three phrases of the clock, the cooking, the lodging, six and seven, the seventh day's assembly and the intermediate days handed
# to the sages), THE WEEKS FROM THE SICKLE (the omer's three rules, reaping by night, the freewill measure, the three commandments of the pilgrimage, the household,
# the slave remembered), THE FEAST OF BOOTHS (the gathering, the booth's ownership, the roofing, the seven days at the place, the compensation, the joy's offering),
# THE THREE PILGRIMAGES (all the males, who appears, the order of the names, none empty, the two amounts, the gift of the hand, the guard of the land), THE JUDGES IN
# EVERY GATE (the court for all Israel and the three tiers, the qualified judge, no wresting, no faces, no bribe — its first entry, justice pursued and the acquittal
# final) and THE ASHERAH AND THE PILLAR (beside the altar, any tree, the pillar hated — the fathers' love on the tape); THE READBACK'S FORMS ON FILE, NO NEW FORM
# (THE DEUTERONOMY WALK sitting 14b — THE LEAN PASS, 2026-09-23; World/step9/DEUTERONOMY_WALK.md "Sitting 14b"; the state doc's #210). FIVE own-day lines at the
# counter's day (40, 11, 1), NO marker: passover_at_the_place_declared (16:1-8 — passover_at_the_place_commanded and seventh_day_assembly_commanded STATUSES;
# passover_in_the_gates_barred, leaven_with_the_passover_barred, flesh_till_morning_barred BLOCKS), weeks_and_booths_declared (16:9-15 — weeks_at_the_place_commanded,
# booths_at_the_place_commanded STATUSES), three_pilgrimages_declared (16:16-17 — three_pilgrimages_commanded a STATUS, empty_appearance_barred a BLOCK),
# judges_in_every_gate_commanded (16:18-20 — judges_and_officers_commanded and justice_pursuit_commanded STATUSES; judgment_wresting_barred, person_respecting_barred
# BLOCKS; bribe_barred REUSED — its FIRST entry anywhere), asherah_and_pillar_barred (16:21-22 — asherah_beside_the_altar_barred, pillar_barred BLOCKS). THE KIN'S
# CELLS BY CALL (fifteen runners, every edge REFERENCE); THE TAPE'S LINES BY KIND (the Passover kept, the courts established, the judges charged, the place chosen,
# the second tithe's rejoicing). Six cells and the table; every token probed (zero-report law); effects on every cell (the effects law); THE EXAM THE EIGHT MISHNAH
# ROWS THE SPINE CITES (Berakhot 1:5, Pesachim 3:7, Beitzah 1:1, Sukkah 1:4, Chagigah 1:1, 1:2, 1:4, 1:5 — read whole; no docket, the lean form); the parameters the
# runner's DATA rows (no clock datum added — the festivals' dates and the intercalation on file). The daemon law_festivals_judges given_at Deut 16:1, installed_by boot
# (the Deuteronomy daemons' form). Reading ledger: logic/oral_triage/deu_16_reeh_shoftim_2026-09-23.md; the lean exam: deu_16_reeh_shoftim_exam_2026-09-23.md.

# ---- THE HONEST-PAIRING GUARD ----------------------------------------------------------------------------
import os as _os, sys as _sys
_sys.path.insert(0, _os.path.dirname(_os.path.abspath(__file__)))
_ROOT = _os.path.normpath(_os.path.join(_os.path.dirname(_os.path.abspath(__file__)), '..', '..'))   # THE PORTABLE REPO: the repo root from this file's own place
from compile_guards import check_honest_pairing as _chp
_P = _os.path.abspath(__file__)
GUARDED = _chp(_P, 'CASES', 2)
assert GUARDED == 0, ("the guard counted %d expectations, the tripwire holds 0" % GUARDED)   # RETYPED after the generator (the cells' asks summed)
print('guard: %d expectations checked, every one a literal from the answer sheet [honest-pairing guard satisfied]' % GUARDED)
import sqlite3, sys, io, re, contextlib, collections, unicodedata, yaml, inspect
from collections import Counter
import effects_layer as FX
import world_engine as WE
import cold_run_pesach as PS                   # THE EDGE: festivals_judges -> pesach CALL, reference (16:1-7's Passover by name — the name, the eating until midnight, roasted only, the remainder burned; the leaven's window)
import cold_run_moadim as MO                   # THE EDGE: festivals_judges -> moadim CALL, reference (Leviticus 23's feasts by name — the slaughter window, the omer's morrow and count, the booths' seven, the seventh day's work class)
import cold_run_musafim as MU                  # THE EDGE: festivals_judges -> musafim CALL, reference (Numbers 28-29's dates, the seventh, Shavuot's redress by Deut 16:16's own analogy, the eighth)
import cold_run_calendar as CA                 # THE EDGE: festivals_judges -> calendar CALL, reference (Exodus 23:14-18's three times, the males, the leaven and the fat)
import cold_run_erection as ER                 # THE EDGE: festivals_judges -> erection CALL, reference (Exodus 34:18-26's repeats — the empty appearance's standing liability, the fourteenth's festival offering, the ingathering's turn, the cow grazes; 34:13's asherim by the answer sheet)
import cold_run_place_name as PN               # THE EDGE: festivals_judges -> place_name CALL, reference (the place formula's six seats; the rejoicing and the household; 12:17's gates; 12:3's asherim)
import cold_run_opening_speech as OP           # THE EDGE: festivals_judges -> opening_speech CALL, reference (1:16-17's charge — the qualities, no faces, the court of three)
import cold_run_exodus_story as ES             # THE EDGE: festivals_judges -> exodus_story CALL, reference (Exodus 18:21-25's courts — 78,600 judges, the Sanhedrin's sizes)
import cold_run_ordinances as OR               # THE EDGE: festivals_judges -> ordinances CALL, reference (Exodus 23:2-8's court — the poor, the majority, the bribe's block declared and never written)
import cold_run_holiness as HO                 # THE EDGE: festivals_judges -> holiness CALL, reference (Leviticus 19:15's two faces, the judge's five effects, the bribed judge's eyes)
import cold_run_second_tablets as ST           # THE EDGE: festivals_judges -> second_tablets CALL, reference (10:17's 'lifts no face and takes no bribe' — DB7's declaration; the permitted fee)
import cold_run_seven_nations as SN            # THE EDGE: festivals_judges -> seven_nations CALL, reference (7:5's asherim — the shade, the wood, the four objects)
import cold_run_covenant_at_horeb as CH        # THE EDGE: festivals_judges -> covenant_at_horeb CALL, reference (5:15's slave remembered — 16:12 verbatim in kind)
import cold_run_journeys as JR                 # THE EDGE: festivals_judges -> journeys CALL, reference (Numbers 33:52's figured stones — Leviticus 26:1's pillar by name)
import cold_run_pesach_sheni as PSH            # THE EDGE: festivals_judges -> pesach_sheni CALL, reference (the Passover in its season; the distant way)

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
def W16(v): return words('Deut', 16, v)
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
D16 = lambda v: ('Deut', 16, v)
NEG_T = ('לא', 'ולא')   # (not; and not)
NAME = ('יהוה', 'ליהוה', 'ויהוה', 'ביהוה', 'מיהוה')   # (the LORD; to the LORD; and the LORD; in the LORD; from the LORD)
import difflib
def SH(a, b_): return sum(s for _, _, s in difflib.SequenceMatcher(a=words(*a), b=words(*b_)).get_matching_blocks())   # the reading's shared-run measure
NV = len({v for (b, c, v) in by if b == 'Deut' and c == 16}); assert NV == 22, NV   # twenty-two verses in both numberings (the identity — the reading's divisions assert)
TOKN = sum(len(W16(v)) for v in range(1, 23)); assert TOKN == 334, TOKN   # the chapter's tokens (the reading's divisions assert)

P_ = []   # the provenance trail of the case being run
def ink(ref, note):  P_.append(('INK',  'Deut %s — %s' % (ref, note) if not ref[:1].isupper() else '%s — %s' % (ref, note)))
def move(src, note): P_.append(('MOVE', '%s — %s' % (src, note)))
def dat(note):       P_.append(('DATA', note))
def hyp(note):       P_.append(('HYP',  note))     # THE LINK REVIEW LAW: a hypothesis — no teacher; counted apart, never as compiled
def out(verdict, effects):
    """verdict + registry-validated effects (the engine contract)"""
    FX.validate([e for e in effects if e != FX.NONE])
    return verdict, effects, list(P_)

# ---- THE INK, computed (the parser and the tokens; the reading's facts the expectations — every assert PROVEN at the reading, ch16_ink.py — COPIED from the reading's instrument by content markers in four blocks; the store-, shelf- and Onkelos-bound asserts left to the reading; the parser's facts typed from the ink's own asserts) ----
SPAN = [(16, v) for v in range(1, 23)]
def MARKS(c, v): return [t for t in verse_words('Deut', c, v) if t[-1] in '#~^%@|*']
PARSE = {v: (ink_numbers(verse_words('Deut', 16, v)), ink_ordinals(verse_words('Deut', 16, v)), MARKS(16, v)) for v in range(1, 23)}
NUMV = [v for v in PARSE if PARSE[v][0]]; ORDV = [v for v in PARSE if PARSE[v][1]]; STARV = [v for v in PARSE if PARSE[v][2]]
print('THE INK (printed before it is asserted): PARSE %s, NUMV %s, ORDV %s, STARV %s, TOKN %d' % ({v: p for v, p in PARSE.items() if p[0] or p[1] or p[2]}, NUMV, ORDV, STARV, TOKN))
assert {v: p for v, p in PARSE.items() if p[0] or p[1] or p[2]} == {3: ([7], [], []), 4: ([7], [1], []), 5: ([1], [], []), 8: ([6], [7], []), 9: ([7, 7], [], ['שבעת*']), 13: ([7], [], []), 15: ([7], [], []), 16: ([3], [], [])}, {v: p for v, p in PARSE.items() if p[0] or p[1] or p[2]}   # EIGHT NUMBER VERSES, TWO ORDINALS (16:4 the first day, 16:8 the seventh), ONE STARRED token (16:9 "weeks" — the number word inside it, the mark glossed at the reading); the reading's parser assert
assert NUMV == [3, 4, 5, 8, 9, 13, 15, 16] and ORDV == [4, 8] and STARV == [9]
# THE KIN FOUND BY COMPUTATION (the measure's A section, recomputed here so the asserts read the same instrument): the shared distinct tokens outside the stop list, the top eight, the three closest re-scored in order
STOP = set(('את ואת אשר כל וכל על ועל אל ואל '   # (the object marker, and-it, which, all, on, to — the particles)
            'לא ולא כי אם יהוה אלהיך אלהיכם '   # (not, for, if; the LORD, your God)
            'לך לכם בו שם שמה גם מן ממך עד '   # (to you, in it, there, also, from, until)
            'הוא היא אתם אתה אנכי אני לו לה '   # (he, she, you, I, to him, to her)
            'בכל כאשר כן הימים היום אלה האלה '   # (in all, as, so, the days, today, these)
            'בארץ הארץ אשר ואם או פן ופן '   # (in the land, the land, which, and if, or, lest)
            'ואת זה וזה הם המה').split())   # (and-it, this, and this, they, they) — the stopword set glossed piece by piece (the lint's ninety-character window)
ORD = {k: i for i, k in enumerate(by)}
TOK = {k: set(words(*k)) - STOP for k in by}
KINC = {}
for _v in range(1, NV + 1):
    _me = D16(_v); _t = TOK[_me]
    _sc = sorted(((len(_t & TOK[k]), k) for k in by if k != _me and len(_t & TOK[k]) >= 2), key=lambda x: (-x[0], ORD[x[1]]))[:8]
    KINC[_v] = [(f'{k[0]} {k[1]}:{k[2]}', n, SH(_me, k) if i < 3 else None) for i, (n, k) in enumerate(_sc)]
DT = ('Deut',)
# ---- THE FRAMES AND THE REGISTER (computed on the morphology): THE CHAPTER SINGULAR FROM END TO END; no divine frame, no "saying", no first person, no narrative form, no imperative; one infinitive absolute — "observe", the chapter's first word ----
MORPH = {v: [(x, m) for x, m in by[('Deut', 16, v)]] for v in range(1, 23)}
assert all(sum(1 for _, m in MORPH[v] if m and '2mp' in m) == 0 for v in range(1, 23)) and all(sum(1 for _, m in MORPH[v] if m and '2ms' in m) >= 1 for v in range(1, 23)) and sum(sum(1 for _, m in MORPH[v] if m and '2ms' in m) for v in range(1, 23)) == 95, sum(sum(1 for _, m in MORPH[v] if m and '2ms' in m) for v in range(1, 23))
assert [(v, x) for v in range(1, 23) for x, m in MORPH[v] if m and re.search(r'V[a-zA-Z]a$', m)] == [(1, 'שמור')] and [(v, x) for v in range(1, 23) for x, m in MORPH[v] if m and re.search(r'V[a-zA-Z]w', m)] == [] and [(v, x) for v in range(1, 23) for x, m in MORPH[v] if m and re.search(r'V[a-zA-Z]v', m)] == [] and [(v, x) for v in range(1, 23) for x, m in MORPH[v] if m and '1c' in m] == []
assert [(v, x) for v in range(1, 23) for x, m in MORPH[v] if m and re.search(r'V[a-zA-Z]r', m)] == [(5, 'נתן'), (18, 'שפטים'), (18, 'ושטרים'), (18, 'נתן'), (20, 'נתן')]   # "judges and officers" participles; "gives" thrice
NEG = {v: sum(1 for x in W16(v) if x in ('לא', 'ולא')) for v in range(1, 23) if any(x in ('לא', 'ולא') for x in W16(v))}
assert NEG == {3: 1, 4: 2, 5: 1, 8: 1, 16: 1, 19: 3, 21: 1, 22: 1} and sum(NEG.values()) == 11 and [v for v in range(1, 23) if W16(v)[0] in ('כי', 'וכי', 'אם')] == [6] and W16(6)[:2] == ['כי', 'אם'] and [v for v in range(1, 23) if 'לאמר' in W16(v)] == [] and [v for v in range(1, 23) if 'למען' in W16(v)] == [3, 20], NEG
NAME_BARE = sum(1 for v in range(1, 23) for x in W16(v) if x == 'יהוה'); NAME_L = sum(1 for v in range(1, 23) for x in W16(v) if x == 'ליהוה')
YOURGOD = [v for v in range(1, 23) if any(a == 'יהוה' and b == 'אלהיך' for a, b in zip(W16(v), W16(v)[1:]))]; NONAME = [v for v in range(1, 23) if not any('יהוה' in x for x in W16(v))]
assert NAME_BARE == 17 and NAME_L == 5 and YOURGOD == [1, 5, 6, 7, 10, 11, 15, 16, 17, 18, 20, 21, 22] and NONAME == [3, 4, 9, 12, 13, 14, 19], (NAME_BARE, NAME_L, YOURGOD, NONAME)
with contextlib.redirect_stdout(io.StringIO()):
    import register_census as RC
    _ink = RC.read_ink()
assert [k for k in RC.receipts(_ink) if k[0] == 'Deut' and k[1] == 16] == [] and [x for x in RC.footers(_ink) if x[0][0] == 'Deut' and x[0][1] == 16] == [] and [x for x in RC.register_headers(_ink) if x[0][0] == 'Deut' and x[0][1] == 16] == [] and [k for k in RC.receipts(_ink) if k[0] == 'Deut' and k[1] <= 16] == [('Deut', 1, 3), ('Deut', 1, 19), ('Deut', 1, 41), ('Deut', 4, 5), ('Deut', 5, 12), ('Deut', 5, 16), ('Deut', 5, 32), ('Deut', 10, 5)] and ([k for k in RC.count_lines(_ink) if k[0] == 'Deut' and k[1] == 16] if hasattr(RC, 'count_lines') else []) == []
# ---- THE KIN BY COMPUTATION (the closest three re-scored in order) and THE TWINS DIFFED ----
assert KINC[1][0] == ('Exod 34:18', 4, 7) and KINC[1][1] == ('Exod 23:15', 3, 5) and KINC[3][:3] == [('Exod 12:15', 5, 5), ('Exod 23:15', 5, 6), ('Exod 34:18', 5, 6)] and KINC[8][:2] == [('Exod 35:2', 7, 6), ('Lev 23:3', 7, 5)] and KINC[9] == [] and KINC[22] == [] and KINC[11][:2] == [('Deut 12:18', 10, 13), ('Deut 16:14', 10, 11)] and KINC[14][0] == ('Deut 16:11', 10, 11) and KINC[16][:3] == [('2Chr 8:13', 8, 9), ('Exod 23:17', 5, 7), ('Exod 34:23', 5, 8)] and KINC[19][0] == ('Exod 23:8', 5, 7) and KINC[12][0] == ('Deut 24:18', 4, 6) and KINC[5][:2] == [('Deut 15:7', 3, 7), ('Deut 17:2', 3, 7)], (KINC[1], KINC[9], KINC[16])
D = lambda v: ('Deut', 16, v)
assert SHN(D(1), ('Exod', 34, 18)) == 7 and SHARED(D(1), ('Exod', 34, 18)) == ['כי', 'בחדש', 'האביב'] and SHN(D(1), ('Exod', 23, 15)) == 5 and SHN(D(1), ('Exod', 13, 4)) == 2 and SHARED(D(1), ('Exod', 13, 4)) == ['בחדש', 'האביב']
assert SHN(D(4), ('Exod', 13, 7)) == 6 and SHARED(D(4), ('Exod', 13, 7)) == ['ולא', 'יראה', 'לך', 'שאר', 'בכל', 'גבלך'] and SHN(D(4), ('Exod', 34, 25)) == 3 and SHARED(D(4), ('Exod', 34, 25)) == ['ולא', 'ילין']   # "no leaven seen in all your border" Exodus 13:7's six words; "shall not remain overnight" 34:25's Passover clause
assert SHN(D(6), ('Exod', 12, 6)) == 0 and SHN(D(6), ('Lev', 23, 5)) == 0 and SHN(D(6), ('Num', 9, 3)) == 0 and 'בין' not in W16(6) and W16(6)[14:19] == ['בערב', 'כבוא', 'השמש', 'מועד', 'צאתך']   # "between the evenings" NOWHERE in the chapter: "at evening, at the going down of the sun, the season of your going out"
assert SHN(D(7), ('Exod', 12, 8)) == 0 and SHN(D(7), ('Exod', 12, 9)) == 0 and W16(7)[0] == 'ובשלת' and words('Exod', 12, 9)[3:7] == ['נא', 'ובשל', 'מבשל', 'במים'] and words('2Chr', 35, 13)[:3] == ['ויבשלו', 'הפסח', 'באש']   # "you shall boil" against "nor boiled in water" — the Chronicler's "they boiled the Passover with fire"
assert SHN(D(8), ('Exod', 13, 6)) == 5 and DIFF(D(8), ('Exod', 13, 6))[:2] == [('replace', ['ששת'], ['שבעת']), ('replace', ['מצות'], ['מצת'])] and SHN(D(8), ('Exod', 12, 16)) == 3 and SHN(D(8), ('Lev', 23, 8)) == 3   # SIX days here against SEVEN there — the shelf's question
assert SHN(D(9), ('Lev', 23, 15)) == 0 and SHN(D(9), ('Lev', 23, 16)) == 0 and W16(9)[:2] == ['שבעה', 'שבעת'] and W16(9)[-2:] == ['שבעה', 'שבעות'] and W16(9)[4:7] == ['מהחל', 'חרמש', 'בקמה']   # the count from the sickle, not from "the morrow of the sabbath"; "seven weeks" said twice, spelled two ways
assert SHN(D(11), ('Deut', 12, 18)) == 13 and SHARED(D(11), ('Deut', 12, 18)) == ['אתה', 'ובנך', 'ובתך', 'ועבדך', 'ואמתך', 'והלוי', 'אשר', 'בשעריך'] and SHN(D(11), D(14)) == 11 and SHN(D(11), ('Deut', 12, 12)) == 4 and [x for x in W16(11) if x in ('אתה', 'ובנך', 'ובתך', 'ועבדך', 'ואמתך', 'והלוי', 'והגר', 'והיתום', 'והאלמנה')] == [x for x in W16(14) if x in ('אתה', 'ובנך', 'ובתך', 'ועבדך', 'ואמתך', 'והלוי', 'והגר', 'והיתום', 'והאלמנה')] == ['אתה', 'ובנך', 'ובתך', 'ועבדך', 'ואמתך', 'והלוי', 'והגר', 'והיתום', 'והאלמנה']   # THE HOUSEHOLD LIST — nine members, identical at 16:11 and 16:14; 12:18's six (no sojourner, fatherless, widow); 12:12's plural
assert SHN(D(12), ('Deut', 24, 18)) == 6 and SHARED(D(12), ('Deut', 24, 18)) == ['וזכרת', 'כי', 'עבד', 'היית', 'במצרים'] and SHN(D(12), ('Deut', 5, 15)) == 5 and SHN(D(12), ('Deut', 15, 15)) == 5 and SHN(D(12), ('Deut', 24, 22)) == 5   # "remember that you were a slave" — the book's five seats (5:15, 15:15, 16:12, 24:18, 24:22), 24:18 the closest
assert SHN(D(16), ('Exod', 34, 23)) == 8 and SHARED(D(16), ('Exod', 34, 23)) == ['פעמים', 'בשנה', 'יראה', 'כל', 'זכורך', 'את', 'פני'] and SHN(D(16), ('Exod', 23, 17)) == 7 and DIFF(D(16), ('Exod', 34, 23))[0] == ('replace', ['שלוש'], ['שלש']) and SHN(D(16), ('Exod', 23, 14)) == 1 and words('Exod', 23, 14)[:2] == ['שלש', 'רגלים']   # "three times" spelled full here, defective in Exodus; "three feet" (regalim) Exodus 23:14's word
assert SHN(D(17), ('Deut', 12, 15)) == 6 and SHARED(D(17), ('Deut', 12, 15)) == ['כברכת', 'יהוה', 'אלהיך', 'אשר', 'נתן', 'לך'] and W16(17)[:3] == ['איש', 'כמתנת', 'ידו']
assert SHN(D(18), ('Deut', 1, 16)) == 2 and SHN(D(18), ('Exod', 18, 21)) == 1 and SHN(D(18), ('Exod', 18, 25)) == 1 and W16(18)[:2] == ['שפטים', 'ושטרים'] and W16(18)[-2:] == ['משפט', 'צדק']   # the judges' appointment shares nothing in order with Jethro's or Horeb's — a new command
assert SHN(D(19), ('Exod', 23, 8)) == 7 and SHARED(D(19), ('Exod', 23, 8)) == ['כי', 'השחד', 'יעור'] and [x for x in W16(19) if x in ('חכמים', 'פקחים')] == ['חכמים'] and [x for x in words('Exod', 23, 8) if x in ('חכמים', 'פקחים')] == ['פקחים'] and ('replace', ['צדיקם'], ['צדיקים']) in DIFF(D(19), ('Exod', 23, 8)) and SHN(D(19), ('Exod', 23, 6)) == 3 and SHARED(D(19), ('Exod', 23, 6)) == ['לא', 'תטה', 'משפט'] and SHN(D(19), ('Deut', 24, 17)) == 4 and SHN(D(19), ('Deut', 1, 17)) == 3   # "the eyes of THE WISE" here, "the OPEN-EYED" in Exodus; "the righteous" spelled defective here
assert SHN(D(20), ('Deut', 4, 1)) == 6 and SHN(D(20), ('Deut', 8, 1)) == 5 and W16(20)[:3] == ['צדק', 'צדק', 'תרדף'] and SHN(D(21), ('Deut', 7, 5)) == 0 and SHN(D(21), ('Deut', 12, 3)) == 0 and SHN(D(21), ('Exod', 34, 13)) == 0 and SHN(D(22), ('Deut', 12, 31)) == 2 and SHARED(D(22), ('Deut', 12, 31)) == ['אשר', 'שנא'] and SHN(D(22), ('Lev', 26, 1)) == 1
# ---- THE FORMULAS OVER THE TORAH AND THE BIBLE (by consonants) ----
assert P('חדש', 'האביב', books=None) == ['Deut 16:1', 'Exod 23:15', 'Exod 34:18'] and P('לחם', 'עני', books=None) == ['Deut 16:3'] and P('כבוא', 'השמש', books=None) == ['Deut 16:6'] and P('ששת', 'ימים', 'תאכל', books=None) == ['Deut 16:8'] and P('שבעה', 'שבעת', books=None) == ['Deut 16:9'] and P('חג', 'שבעות', books=None) == ['Deut 16:10', 'Ezek 45:21'] and P('שלוש', 'פעמים', 'בשנה', books=None) == ['2Chr 8:13', 'Deut 16:16'] and P('יראה', 'כל', 'זכורך', books=None) == ['Deut 16:16', 'Exod 23:17', 'Exod 34:23'] and P('פני', 'יהוה', 'ריקם', books=None) == ['Deut 16:16']
assert P('שפטים', 'ושטרים', books=None) == ['Deut 16:18'] and P('בכל', 'שעריך', books=None) == ['Deut 12:15', 'Deut 16:18', 'Deut 28:52', 'Deut 28:55'] and P('לא', 'תטה', 'משפט', books=None) == ['Deut 16:19', 'Deut 24:17', 'Exod 23:6'] and P('צדק', 'צדק', books=None) == ['Deut 16:20'] and P('למען', 'תחיה', 'וירשת', books=None) == ['Deut 16:20'] and P('אשר', 'שנא', 'יהוה', books=None) == ['Deut 16:22'] and P('לא', 'תכיר', 'פנים', books=None) == ['Deut 16:19'] and P('לא', 'תכירו', 'פנים', books=None) == ['Deut 1:17'] and P('השחד', 'יעור', books=None) == ['Deut 16:19', 'Exod 23:8'] and U('שחד', 'השחד', 'ושחד', books=T) == ['Deut 10:17', 'Deut 16:19', 'Deut 27:25', 'Exod 23:8']
PLACE = P('במקום', 'אשר', 'יבחר', books=None); assert PLACE == ['Deut 12:14', 'Deut 12:18', 'Deut 14:23', 'Deut 15:20', 'Deut 16:11', 'Deut 16:15', 'Deut 16:16', 'Deut 16:2', 'Deut 16:7', 'Deut 23:17', 'Deut 31:11'] and [(v, i) for v in range(1, 23) for i, x in enumerate(W16(v)) if x in ('במקום', 'המקום') and W16(v)[i + 1] == 'אשר' and W16(v)[i + 2] == 'יבחר'] == [(2, 6), (6, 3), (7, 2), (11, 17), (15, 5), (16, 10)] and P('לשכן', 'שמו', 'שם', books=None) == ['Deut 12:11', 'Deut 14:23', 'Deut 16:11', 'Deut 16:2', 'Deut 16:6', 'Deut 26:2']   # THE PLACE six times in the chapter (16:2, 6, 7, 11, 15, 16), "to make His name dwell there" three of its six
PESACH = U('פסח', 'הפסח', books=T); assert len(PESACH) == 23 and 'Deut 15:21' in PESACH and 'Lev 21:18' in PESACH and [s for s in PESACH if s.startswith('Deut 16')] == ['Deut 16:1', 'Deut 16:2', 'Deut 16:5', 'Deut 16:6'] and len(U('פסח', 'הפסח', books=None)) == 53 and lemma_of('Deut', 16, 1, 'פסח') == ['6453'] and lemma_of('Deut', 15, 21, 'פסח') == ['6455']   # THE HOMOGRAPH: "lame" (15:21, Leviticus 21:18) sits in the Passover's consonantal census — told apart by lemma (13b's lesson)
assert hits('בחפזון') == ['Deut 16:3', 'Exod 12:11', 'Isa 52:12'] and hits('עצרת', T) == ['Deut 16:8', 'Lev 23:36', 'Num 29:35'] and hits('חרמש') == ['Deut 16:9', 'Deut 23:26'] and U('אשרה', 'אשריו', 'אשרים', books=T) == ['Deut 16:21', 'Exod 34:13'] and 'ואשריהם' in words('Deut', 12, 3) and 'ואשירהם' in words('Deut', 7, 5) and U('מצבה', 'מצבת', 'מצבתם', 'מצבתיהם', books=T) == ['Deut 12:3', 'Deut 16:22', 'Exod 23:24', 'Exod 24:4', 'Exod 34:13', 'Gen 28:18', 'Gen 28:22', 'Gen 31:13', 'Gen 31:45', 'Gen 35:14', 'Gen 35:20'] and 'ומצבה' in words('Lev', 26, 1)   # "in haste" three in the Bible (the exodus, here, Isaiah's "not in haste"); "solemn assembly" the Torah's three; the sickle's two; the asherah bare here and at Exodus 34:13 (7:5 and 12:3 carry suffixes); the pillar's Torah seats — Jacob's six, Sinai's, the ban's
assert U('ושמחת', 'ושמחתם', books=DT) == ['Deut 12:12', 'Deut 12:18', 'Deut 12:7', 'Deut 14:26', 'Deut 16:11', 'Deut 16:14', 'Deut 26:11', 'Deut 27:7'] and [(v, x) for v in range(1, 23) for x in W16(v) if x.startswith('ושמח') or x == 'שמח'] == [(11, 'ושמחת'), (14, 'ושמחת'), (15, 'שמח')] and W16(15)[-3:] == ['והיית', 'אך', 'שמח']
assert P('חג', 'הסכת', books=None) == ['Deut 16:13'] and P('חג', 'הסכות', books=None) == ['Ezra 3:4', 'Lev 23:34', 'Zech 14:16', 'Zech 14:18', 'Zech 14:19'] and P('ובחג', 'הסכות', books=None) == ['2Chr 8:13', 'Deut 16:16'] and P('חג', 'המצות', books=None) == ['2Chr 30:13', '2Chr 30:21', '2Chr 35:17', 'Exod 23:15', 'Exod 34:18', 'Lev 23:6'] and P('בחג', 'המצות', books=None) == ['2Chr 8:13', 'Deut 16:16']   # "the feast of booths" spelled DEFECTIVE at 16:13 alone in the Bible (הסכת), full at 16:16; 2 Chronicles 8:13 the one verse that names all three feasts with 16:16's words
SEVEN = P('שבעת', 'ימים', books=T); assert [s for s in SEVEN if s.startswith('Deut')] == ['Deut 16:13', 'Deut 16:15', 'Deut 16:3', 'Deut 16:4'] and len(SEVEN) == 53 and {v: [x for x in W16(v) if x in ('שבעת', 'שבעה', 'שבעות', 'השבעות', 'שבע')] for v in range(1, 23) if any(x in ('שבעת', 'שבעה', 'שבעות', 'השבעות', 'שבע') for x in W16(v))} == {3: ['שבעת'], 4: ['שבעת'], 9: ['שבעה', 'שבעת', 'שבעה', 'שבעות'], 10: ['שבעות'], 13: ['שבעת'], 15: ['שבעת'], 16: ['השבעות']}   # "seven days" the book's only four seats all in this chapter; SEVEN at nine seats in seven verses
assert [(v, x) for v in range(1, 23) for x in W16(v) if x in ('תזכר', 'וזכרת')] == [(3, 'תזכר'), (12, 'וזכרת')] and [(v, x) for v in range(1, 23) for x in W16(v) if 'מצרים' in x] == [(1, 'ממצרים'), (3, 'מצרים'), (3, 'מצרים'), (6, 'ממצרים'), (12, 'במצרים')] and [(v, x) for v in range(1, 23) for x in W16(v) if 'שעריך' in x] == [(5, 'שעריך'), (11, 'בשעריך'), (14, 'בשעריך'), (18, 'שעריך')] and U('ובשלת', 'ובשל', 'מבשל', 'תבשל', books=T) == ['Deut 14:21', 'Deut 16:7', 'Exod 12:9', 'Exod 23:19', 'Exod 29:31', 'Exod 34:26', 'Lev 6:21']

# ---- THE COUNTER'S DAY, THE CALENDAR'S ROWS READ AND THE ONE DATABASE SCANNED (a bare world on the exodus epoch; no clock walk this chapter — no marker, no stretch, no clock datum added: the festivals' dates, the omer's day and the intercalation on file, read here never typed) ----
with contextlib.redirect_stdout(io.StringIO()):
    _WC = WE.World(era='the counter\'s day — chapter 16 on a bare world (the exodus epoch)', epoch='exodus')
_EX = _WC.clock.eras['exodus']
def DAY(y, m, d): return _WC.clock.day_in('exodus', y, m, d)
def DATE(day): return _EX.date(day)
COUNTER = DAY(40, 11, 1)
CAL_FEST = WE.CAL_PARAMS['festival_dates']['value']; CAL_OMER = WE.CAL_PARAMS['omer_day']['value']; CAL_LEAP = WE.CAL_PARAMS['intercalated_month']['value']; CAL_THRESH = WE.CAL_PARAMS['intercalation_threshold_days']['value']; CAL_GROUNDS = WE.CAL_PARAMS['intercalation_grounds']['value']
CAL_LEAP_BY = WE.CAL_PARAMS['intercalated_month'].get('exercised_by'); CAL_BTE = WE.CAL_PARAMS['between_the_evenings_from']['value']['hour']
SLOTS = [d['name'] for d in yaml.safe_load(open(_os.path.join(HERE, 'calendar_parameters.yaml'), encoding='utf-8'))['day_slots']]
CLOCK = {'counter': DATE(COUNTER), 'passover': (CAL_FEST['passover']['month'], CAL_FEST['passover']['day']), 'passover_1': (CAL_FEST['passover_1']['month'], CAL_FEST['passover_1']['day']), 'passover_7': CAL_FEST['passover_7'], 'atzeret': CAL_FEST['atzeret'], 'sukkot_1': (CAL_FEST['sukkot_1']['month'], CAL_FEST['sukkot_1']['day']), 'omer_day': (CAL_OMER['month'], CAL_OMER['day']), 'leap': CAL_LEAP, 'threshold': CAL_THRESH, 'grounds': CAL_GROUNDS, 'leap_by': CAL_LEAP_BY, 'slots': SLOTS, 'between_the_evenings_from': CAL_BTE, 'no_marker': True}
print('THE CLOCK (printed before it is asserted):', CLOCK)
assert CLOCK['counter'] == (40, 11, 1) and CLOCK['passover'] == (1, 14) and CLOCK['passover_1'] == (1, 15) and CLOCK['passover_7'] == {'from': 'passover_1', 'plus': 6} and CLOCK['atzeret'] == {'from': 'omer', 'plus': 49} and CLOCK['sukkot_1'] == (7, 15) and CLOCK['omer_day'] == (1, 16), CLOCK   # Leviticus 23's own keys on the registry (exercised_by moadim and pesach_sheni); the omer's day the sixteenth (the Sages against the Boethusians)
assert CLOCK['leap'] == {'position': 'after_month_12', 'length': 30} and CLOCK['threshold'] == 16 and CLOCK['grounds'] == ['spring_grain', 'tree_fruit', 'season'] and CLOCK['leap_by'] == ['count'] and CLOCK['slots'] == ['evening', 'night', 'midnight', 'dawn', 'morning', 'noon', 'between_the_evenings', 'sunset'] and CLOCK['between_the_evenings_from'] == 6.5, CLOCK   # THE INTERCALATION ON FILE FOR THE COUNT ERA ALONE (Sanhedrin 12b, 13a, 11b) — the exodus era's Aviv OWED (the debt line); the day slots the three phrases' seats (16:6)

# ---- THE ONE DATABASE SCANNED (the holes' ground — nothing names the Passover at the place, the gates' bar, the leaven with it, the flesh till morning, the seventh day's assembly, the weeks or the booths at the place, the three pilgrimages, the empty appearance, the judges and officers, the wresting, the faces, the pursuit of justice, the asherah or the pillar on Israel before this sitting; the bribe's block NEVER written before — DB7; the kin's entities before) ----
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
OWN15 = ('passover_at_the_place_commanded', 'passover_in_the_gates_barred', 'leaven_with_the_passover_barred', 'flesh_till_morning_barred', 'seventh_day_assembly_commanded', 'weeks_at_the_place_commanded', 'booths_at_the_place_commanded', 'three_pilgrimages_commanded', 'empty_appearance_barred', 'judges_and_officers_commanded', 'judgment_wresting_barred', 'person_respecting_barred', 'justice_pursuit_commanded', 'asherah_beside_the_altar_barred', 'pillar_barred')
HOLE_WORDS = r"^(passover_at_the\w*|passover_in_the_gates\w*|leaven_with\w*|flesh_till\w*|seventh_day_assembly\w*|weeks_at\w*|booths_at\w*|three_pilgrim\w*|empty_appearance\w*|judges_and_officers\w*|judgment_wrest\w*|person_respect\w*|justice_pursuit\w*|asherah\w*|pillar_barred)\b"
_hs = ledger_scan('israel_people', HOLE_WORDS); HOLE_SCAN = None if _hs is None else [e for e in _hs if e not in OWN15]   # this sitting's own names excluded once the fold carries them
BRIBE_SCAN = effect_scan('bribe_barred'); BURN_SCAN = effect_scan('burn_remainder'); PLACE_SCAN = effect_scan('place_chosen_required'); REJOICE_SCAN = effect_scan('rejoicing_before_the_lord_commanded'); BOOTHS_SCAN = effect_scan('dwells_in_booths'); OMER_SCAN = effect_scan('counts_omer')
COURTS_SCAN = effect_scan('courts_established'); JUDGES_SCAN = effect_scan('judges_charged'); APPEAR_SCAN = (effect_scan('appearance_owed'), effect_scan('appearance_gift_owed')); PILLAR_SCAN = (effect_scan('pillar_anointed'), effect_scan('pillar_raised')); PERVERT_SCAN = effect_scan('judgment_perverted')
del _hs   # 9b's lesson: the raw scans are the database's state at import — the derived lists are equal on the cached and the full load
_FXV = yaml.safe_load(open(_os.path.join(HERE, 'effect_vocabulary.yaml'), encoding='utf-8'))['effects']
print('THE SCANS (printed before they are asserted): holes %s; bribe %s; burn %s; place %s; rejoice %s; booths %s; omer %s; courts %s; judges %s; appear %s; pillars %s; pervert %s' % (HOLE_SCAN, BRIBE_SCAN, BURN_SCAN, PLACE_SCAN, REJOICE_SCAN, BOOTHS_SCAN, OMER_SCAN, COURTS_SCAN, JUDGES_SCAN, APPEAR_SCAN, PILLAR_SCAN, PERVERT_SCAN))
assert HOLE_SCAN in ([], None), HOLE_SCAN   # THE HOLES' GROUND — nothing on Israel named the fifteen before this sitting (DH4)
assert BRIBE_SCAN in ([], None, ['israel_people']), BRIBE_SCAN   # bribe_barred NEVER written before this sitting (DB7); ['israel_people'] once the fold carries 16:19's line — the scan's ground moved by this chapter's own write (the second-tablets callee's assert widened the same way)
assert BURN_SCAN in (['aaron-and-sons'], None) and PLACE_SCAN in (['israel_people'], None) and REJOICE_SCAN in (['israel_people'], None) and BOOTHS_SCAN in ([], None) and OMER_SCAN in ([], None) and COURTS_SCAN in (['israel_people'], None) and (JUDGES_SCAN is None or JUDGES_SCAN in (['the_court'], ['the-court'])) and APPEAR_SCAN in (([], []), (None, None)) and PILLAR_SCAN in ((['the_pillar_of_bethel'], ['the_pillar_of_gilead']), (None, None)) and PERVERT_SCAN in ([], None), (BURN_SCAN, PLACE_SCAN, REJOICE_SCAN, BOOTHS_SCAN, OMER_SCAN, COURTS_SCAN, JUDGES_SCAN, APPEAR_SCAN, PILLAR_SCAN, PERVERT_SCAN)   # the kin's entities as the recon read them from the snapshot: the pillars JACOB'S — the fathers' love on the tape (146:1)
assert all(k in _FXV for k in OWN15) and sum(1 for k in OWN15 if _FXV[k]['ledger_op'] == 'block') == 8 and sum(1 for k in OWN15 if _FXV[k]['ledger_op'] == 'status') == 7 and _FXV['bribe_barred']['ledger_op'] == 'block' and 'THE DEUTERONOMY WALK 14b' in _FXV['bribe_barred']['ink'], 'the fifteen on the registry; the bribe amended (add_types_ch16_a.py)'
# THE DB'S OWN SEATS for the DATA rows (every one computed here — the ink block above proves them at the reading's grain)
INF_ABS = [(v, x) for v in range(1, 23) for x, m in by[('Deut', 16, v)] if m and re.match(r'^H(?:C/)?V.a$', m)]
assert INF_ABS == [(1, 'שמור')], INF_ABS   # ONE infinitive absolute — "observe", the chapter's first word (the reading's frames assert)
TWIN = {'16:1 vs Exod 34:18': SH(D16(1), ('Exod', 34, 18)), '16:1 vs Exod 23:15': SH(D16(1), ('Exod', 23, 15)), '16:4 vs Exod 13:7': SH(D16(4), ('Exod', 13, 7)), '16:4 vs Exod 34:25': SH(D16(4), ('Exod', 34, 25)), '16:6 vs Exod 12:6': SH(D16(6), ('Exod', 12, 6)), '16:8 vs Exod 13:6': SH(D16(8), ('Exod', 13, 6)), '16:9 vs Lev 23:15': SH(D16(9), ('Lev', 23, 15)), '16:11 vs 12:18': SH(D16(11), ('Deut', 12, 18)), '16:11 vs 16:14': SH(D16(11), D16(14)), '16:12 vs 5:15': SH(D16(12), ('Deut', 5, 15)), '16:12 vs 24:18': SH(D16(12), ('Deut', 24, 18)), '16:16 vs Exod 34:23': SH(D16(16), ('Exod', 34, 23)), '16:16 vs Exod 23:17': SH(D16(16), ('Exod', 23, 17)), '16:17 vs 12:15': SH(D16(17), ('Deut', 12, 15)), '16:18 vs 1:16': SH(D16(18), ('Deut', 1, 16)), '16:19 vs Exod 23:8': SH(D16(19), ('Exod', 23, 8)), '16:20 vs 4:1': SH(D16(20), ('Deut', 4, 1)), '16:21 vs 7:5': SH(D16(21), ('Deut', 7, 5)), '16:22 vs 12:31': SH(D16(22), ('Deut', 12, 31))}
print('THE TWINS DIFFED (printed before they are asserted):', TWIN)
assert TWIN == {'16:1 vs Exod 34:18': 7, '16:1 vs Exod 23:15': 5, '16:4 vs Exod 13:7': 6, '16:4 vs Exod 34:25': 3, '16:6 vs Exod 12:6': 0, '16:8 vs Exod 13:6': 5, '16:9 vs Lev 23:15': 0, '16:11 vs 12:18': 13, '16:11 vs 16:14': 11, '16:12 vs 5:15': 5, '16:12 vs 24:18': 6, '16:16 vs Exod 34:23': 8, '16:16 vs Exod 23:17': 7, '16:17 vs 12:15': 6, '16:18 vs 1:16': 2, '16:19 vs Exod 23:8': 7, '16:20 vs 4:1': 6, '16:21 vs 7:5': 0, '16:22 vs 12:31': 2}, TWIN   # the twin laws diffed on the DB (DH4) — the reading's kin asserts read again here (SHN at the reading = the shared run)

# ---- THE CALLEES' FACTS (every edge live at the cells that consume them; the values asserted from the callees' own prints — ch16_callees.out and ch16_callees2.out, read BEFORE any assert was typed; 10b's lesson 2) ----
def V(x): return x[0] if isinstance(x, tuple) else x
MO_PASS = MO.passover(); MO_OMER = MO.omer(); MO_SUK = MO.sukkot(); MO_WORK7 = MO.work_class('passover_7')['v']
MO_WINDOW = MO_PASS['slaughter_window']['v']; MO_MORROW = MO_OMER['morrow_reading']['v']; MO_COUNT = MO_OMER['count_length']['v']; MO_SUK_LEN = MO_SUK['length']['v']; MO_SUK_DWELL = MO_SUK['dwelling_days']['v']; MO_SUK_EIGHTH = MO_SUK['eighth']['v']
assert MO_PASS['date']['v'] == '14th_of_1st' and MO_WINDOW == 'after_midday' and MO_PASS['matzot_days']['v'] == 7 and MO_PASS['eating_time']['v'] == 'night only, until midnight' and MO_PASS['matzot_window']['v'] == '14th evening to 21st evening', {k: v['v'] for k, v in MO_PASS.items()}
assert MO_MORROW == 'festival' and MO_COUNT == 49 and MO_OMER['new_grain_gate_with_temple']['v'] == 'the_omer' and MO_SUK['date']['v'] == '15th_of_7th' and MO_SUK_LEN == 7 and MO_SUK_DWELL == 7 and MO_SUK_EIGHTH == 'atzeret' and MO_SUK['women']['v'] == 'exempt' and MO_WORK7 == 'servile_only' and MO.work_class('passover_1')['v'] == 'servile_only' and MO.work_class('sukkot_1')['v'] == 'servile_only', (MO_MORROW, MO_COUNT, MO_SUK_LEN, MO_SUK_EIGHTH, MO_WORK7)
PS_EAT = PS.paschal_procedure({'ask': 'eating_time'}, PS.DATA)[0]; PS_PREP = PS.paschal_procedure({'ask': 'preparation'}, PS.DATA)[0]; PS_LEFT = PS.paschal_procedure({'ask': 'leftover'}, PS.DATA)[0]; PS_NAME = PS.paschal_procedure({'ask': 'for_its_sake'}, PS.DATA)[0]
assert (PS_EAT, PS_PREP, PS_LEFT, PS_NAME) == ('night only, until midnight', 'roasted only', 'burn on the 16th', 'invalid if not for its sake'), (PS_EAT, PS_PREP, PS_LEFT, PS_NAME)
CA_MALE = CA.pilgrimage({'kind': 'able_male'}, CA.DATA)[0]; CA_WOMAN = CA.pilgrimage({'kind': 'woman'}, CA.DATA)[0]; CA_LAME = CA.pilgrimage({'kind': 'lame'}, CA.DATA)[0]; CA_EYE = CA.pilgrimage({'kind': 'blind_one_eye'}, CA.DATA)[0]
CA_MATZAH = CA.matzah({'ask': 'as_commanded'}, CA.DATA)[0]; CA_LEAVEN = CA.offering_windows({'ask': 'leaven_beside_offering'}, CA.DATA)[0]; CA_FAT = CA.offering_windows({'ask': 'fat_overnight'}, CA.DATA)[0]
assert (CA_MALE, CA_WOMAN, CA_LAME, CA_EYE) == ('owes the three appearings', 'exempt', 'exempt', 'exempt') and CA_MATZAH == 'seven days of unleavened bread = 14th evening to 21st evening (CALLED pesach)' and CA_LEAVEN == 'the slaughterer with leaven transgresses' and CA_FAT == 'disqualified at morning off the altar', (CA_MALE, CA_MATZAH, CA_LEAVEN, CA_FAT)
ER_STAND = ER.repeats('empty_where_it_stands')['v']; ER_CHAG = ER.repeats('chagigah_overnight')['v']; ER_NIGHT = ER.repeats('until_morning_forms')['v']; ER_PURGE = ER.repeats('purge_before_slaughter')['v']; ER_GRAZE = ER.repeats('warranty_read')['v']; ER_TURN = ER.repeats('equinox')['v']; ER_AMOUNTS = ER.repeats('appearance_amounts')['v']; ER_EMPTY2 = ER.repeats('empty_two_seats')['v']
ER_MADE = ER.covenant('sheet_az_3_5')['v']; ER_ALTAR = ER.covenant('sheet_az_4_2')['v']; ER_DEMOL = ER.covenant('demolition_grows')['v']
assert (ER_STAND, ER_CHAG, ER_NIGHT, ER_PURGE, ER_GRAZE, ER_TURN) == ('standing_liability_like_the_appearance_offering', 'chagigah_of_the_fourteenth_not_overnight', 'all_night_on_the_altar', 'purge_before_the_slaughter', 'cow_grazes_unharmed', 'ingathering_after_the_turn') and ER_AMOUNTS == ('two_silver', 'maah') and ER_EMPTY2 == [('Exod', 23, 15), ('Exod', 34, 20)] and ER_MADE == 'made_objects_not_the_ground' and ER_ALTAR == 'altar_class_forbidden' and ER_DEMOL == [3, 4, 5], (ER_STAND, ER_CHAG, ER_AMOUNTS, ER_MADE, ER_DEMOL)
assert ER.repeats('empty_where_it_stands')['fx'] == ['appearance_gift_owed'] and ER.repeats('warranty_read')['fx'] == ['pilgrim_land_guarded'] and ER.repeats('equinox')['fx'] == ['appearance_owed'] and ER.covenant('sheet_az_3_5')['fx'] == ['demolished']
MU_DATES = MU.pesach_shavuot({'ask': 'the_dates'}, MU.DATA)[0]; MU_SEVENTH = MU.pesach_shavuot({'ask': 'the_seventh'}, MU.DATA)[0]; MU_REDRESS = MU.pesach_shavuot({'ask': 'redress_days'}, MU.DATA)[0]; MU_SUK_DATES = MU.sukkot({'ask': 'the_dates'}, MU.DATA)[0]; MU_EIGHTH = MU.sukkot({'ask': 'the_eighth'}, MU.DATA)[0]
assert MU_DATES == 'the fourteenth and the fifteenth — Leviticus 23 by call' and MU_SEVENTH == 'the seventh a convocation — the same class' and MU_REDRESS == "seven days of redress — Pesach's analogy" and MU_SUK_DATES == 'the fifteenth, seven days, the eighth an assembly — Leviticus 23 by call' and MU_EIGHTH == 'the eighth its own festival — one bull, [1, 1, 7]', (MU_DATES, MU_SEVENTH, MU_REDRESS, MU_SUK_DATES, MU_EIGHTH)
PN_PLACE = PN.the_place_chosen({'ask': 'the_place_which_the_lord_will_choose'}, PN.DATA)[0]; PN_REJOICE = PN.the_place_chosen({'ask': 'eat_there_and_rejoice'}, PN.DATA)[0]; PN_HOUSE = PN.the_place_chosen({'ask': 'your_households'}, PN.DATA)[0]; PN_WOMAN = PN.the_place_chosen({'ask': 'the_womans_rejoicing'}, PN.DATA)[0]
PN_ASHERIM = PN.the_header_and_the_demolition({'ask': 'the_three_asherim'}, PN.DATA)[0]; PN_GATES = PN.the_profane_slaughter_the_blood_and_the_gates({'ask': 'you_may_not_eat_within_your_gates'}, PN.DATA)[0]
assert PN_PLACE.startswith('the place which the LORD will choose (12:5) — installed here') and PN_REJOICE.startswith('eat there and rejoice (12:7) — the peace offerings of rejoicing') and PN_HOUSE.startswith("your households (12:12, 12:18) — 5:14's list") and PN_WOMAN.startswith("the woman's rejoicing (12:7, 12:12, 12:18)") and PN_ASHERIM.startswith('the three Asherim (12:3) — planted, shaped, an idol set under it') and PN_GATES.startswith("you may not eat within your gates (12:17) — 'you are not permitted'"), (PN_PLACE[:40], PN_REJOICE[:40], PN_ASHERIM[:40], PN_GATES[:40])
OP_QUAL = OP.the_officers_and_the_judges({'ask': 'the_qualities'}, OP.DATA)[0]; OP_CHARGE = OP.the_officers_and_the_judges({'ask': 'the_charge'}, OP.DATA)[0]; OP_FACES = OP.the_officers_and_the_judges({'ask': 'no_faces'}, OP.DATA)[0]; OP_RIGHT = OP.the_officers_and_the_judges({'ask': 'judge_righteously'}, OP.DATA)[0]; OP_THREE = OP.the_officers_and_the_judges({'ask': 'the_court_of_three'}, OP.DATA)[0]; OP_PERVERT = OP.the_officers_and_the_judges({'ask': 'the_perverting_judge'}, OP.DATA)[0]
assert OP_QUAL.startswith('the qualities (1:13, 15) — seven asked, three found') and OP_CHARGE.startswith('the charge (1:16-17) — the six clauses each one seat: judges_charged on the court') and OP_FACES.startswith('no faces (1:17) — befriend / estrange disputed (Sanhedrin 7b:18)') and OP_RIGHT.startswith('judge righteously (1:16) — the true judgment truly') and OP_THREE.startswith('the court of three (Mishnah Sanhedrin 1:1, 3:1-3)') and OP_PERVERT.startswith('the perverting judge — the five effects'), (OP_QUAL[:40], OP_CHARGE[:40], OP_FACES[:40])
ES_JUDGES = ES.jethro('judges')['v']; ES_DENOM = ES.jethro('denominations')['v']; ES_SIZES = ES.jethro('sanhedrin_sizes')['v']
assert ES_JUDGES == 78600 and ES_DENOM == 4 and ES_SIZES == (71, 23) and ES.jethro('sanhedrin_sizes')['fx'] == ['courts_established'], (ES_JUDGES, ES_DENOM, ES_SIZES)
OR_POOR = OR.courts('poor_not_glorified')['v']; OR_ASYM = OR.courts('asymmetry')['v']; OR_23 = OR.courts('twenty_three')['v']; OR_ONE_TWO = OR.courts('one_vs_two')['v']; OR_DISS = OR.courts('dissenter')['v']; OR_BRIBE = OR.courts('bribe')['v']; OR_ABS = OR.courts('bribe_absolute')['v']
assert (OR_POOR, OR_ASYM, OR_23, OR_ONE_TWO, OR_DISS, OR_BRIBE, OR_ABS) == ('each_verse_its_referent', 'acquit_by_one_convict_by_two', 23, 'merit_by_one_liability_by_two', 'bound_and_silent', 'the_bribed_judges_eyes_dim', 'even_to_judge_truly') and OR.courts('bribe')['fx'] == ['bribe_barred', 'judgment_perverted'] and OR.courts('bribe_absolute')['fx'] == ['bribe_barred'], (OR_POOR, OR_ASYM, OR_23, OR_ONE_TWO, OR_DISS, OR_BRIBE, OR_ABS)
HO_FAVOR = HO.conduct('no_favor', who='poor')['v']; HO_MERIT = HO.conduct('scale_of_merit')['v']; HO_FIVE = HO.conduct('five_effects')['v']; HO_MEASURE = HO.conduct('judge_is_measurer')['v']; HO_BRIBE = HO.conduct('bribe')['v']; HO_EQUAL = HO.conduct('equal_treatment')['v']
assert HO_FAVOR == 'banned' and HO_MERIT == 'judge_every_person_toward_merit' and HO_FIVE == ['defiles_the_land', 'profanes_the_Name', 'removes_the_Presence', 'fells_by_the_sword', 'exiles'] and HO_MEASURE == 'one_clause_at_two_seats' and HO_BRIBE == 'the_bribed_judges_eyes_dim' and HO_EQUAL == ['not_one_at_length_and_one_cut_short', 'not_one_standing_and_one_sitting'] and HO.conduct('no_favor', who='poor')['fx'] == ['judgment_perverted'], (HO_FAVOR, HO_MERIT, HO_FIVE, HO_MEASURE)
ST_BRIBE = ST.the_god_of_gods_and_the_stranger({'ask': 'takes_no_bribe'}, ST.DATA)[0]; ST_FEE = ST.the_god_of_gods_and_the_stranger({'ask': 'the_permitted_fee'}, ST.DATA)[0]; ST_FACE = ST.the_god_of_gods_and_the_stranger({'ask': 'lifts_no_face'}, ST.DATA)[0]; ST_SALARY = ST.the_god_of_gods_and_the_stranger({'ask': 'a_salary_voids'}, ST.DATA)[0]
assert ST_BRIBE.startswith("takes no bribe (10:17) — Exodus 23:8's block never written on the tape") and "16:19 the command's seat forward" in ST_BRIBE and ST_FEE.startswith("the permitted fee (Ketubot 105a:17-19) — Karna's fee") and ST_FACE.startswith("lifts no face (10:17) — Numbers 6:26's") and ST_SALARY.startswith('a salary voids (Kiddushin 58b; Mishnah Bekhorot 4:6)'), (ST_BRIBE[:60], ST_FEE[:40])
SN_SHADE = SN.the_seven_nations({'ask': 'the_asherah_shade'}, SN.DATA)[0]; SN_WOOD = SN.the_seven_nations({'ask': 'the_asherah_wood'}, SN.DATA); SN_FOUR = SN.the_seven_nations({'ask': 'the_four_objects'}, SN.DATA)[0]
assert SN_SHADE.startswith("the Asherah's shade (7:5) — not sat in, even the shade of its shade") and SN_WOOD[0].startswith("the Asherah's wood (7:5, 7:26) — used, its user is FLOGGED") and SN_WOOD[1] == ['lashes'] and SN_FOUR.startswith('the four objects (7:5) — four verbs where 34:13 had three'), (SN_SHADE[:40], SN_WOOD[0][:40], SN_FOUR[:40])
CH_FOURTH = CH.the_first_tablet({'ask': 'the_fourth_word'}, CH.DATA)[0]; CH_KEEP = CH.the_first_tablet({'ask': 'keep_and_remember'}, CH.DATA)[0]; CH_REST = CH.the_first_tablet({'ask': 'the_servants_rest'}, CH.DATA)[0]
assert CH_FOURTH.startswith('the fourth word (5:12-15) — EXPANDED, VERBATIM, EXPANDED, TURNED') and CH_KEEP.startswith('keep and remember (5:12) — one utterance') and CH_REST.startswith("the servants' rest (5:14) — the circumcised slave and the righteous convert"), (CH_FOURTH[:40], CH_KEEP[:40], CH_REST[:40])
JR_STONES = JR.the_command({'ask': 'figured_stones'}, JR.DATA)[0]; JR_HIGH = JR.the_command({'ask': 'high_places'}, JR.DATA)[0]; JR_THREE = JR.the_command({'ask': 'three_objects_own'}, JR.DATA)[0]; JR_ERAS = JR.the_command({'ask': 'private_altar_eras'}, JR.DATA)[0]
assert JR_STONES.startswith("their figured stones (33:52) — Leviticus 26:1's word at its ban's seat, uncompiled") and JR_HIGH.startswith("their high places (33:52) — Leviticus 26:30's curse") and JR_THREE.startswith("the three objects (33:52) are the chapter's own") and JR_ERAS.startswith("the private altar's eras (Mishnah Zevachim 14:4-8)"), (JR_STONES[:40], JR_THREE[:40])
PSH_DIST = PSH.second_passover({'ask': 'distance'}, PSH.DATA)[0]
assert PSH_DIST == "from Modi'im and beyond (fifteen mil)", PSH_DIST
print('THE CALLEES (asserted from their prints): MO window %s, morrow %s, count %s, booths %s, the seventh %s; PS %s / %s / %s / %s; CA male %s; ER stand %s, amounts %s, made %s; MU redress %s; PN place %s; OP charge %s; ES sizes %s; OR one-two %s, bribe %s / %s; HO five %s; ST bribe %s; SN wood %s; CH keep %s; JR three %s; PSH %s' % (MO_WINDOW, MO_MORROW, MO_COUNT, MO_SUK_LEN, MO_WORK7, PS_EAT, PS_PREP, PS_LEFT, PS_NAME, CA_MALE, ER_STAND, ER_AMOUNTS, ER_MADE, MU_REDRESS, PN_PLACE[:30], OP_CHARGE[:30], ES_SIZES, OR_ONE_TWO, OR_BRIBE, OR_ABS, len(HO_FIVE), ST_BRIBE[:30], SN_WOOD[1], CH_KEEP[:24], JR_THREE[:24], PSH_DIST))

# THE PORTABLE REPO (2026-09-15): this form never compiled (an unterminated string literal); its paths renamed by text, not by the pass
#!/usr/bin/env python3
# O8 S3 — assembles cold_run_mamre.py: the header, the probes, the helpers, the answer sheet and the shelf rows, the cells (the hand's),
# the daemon and the scene (from the generator, the hand-model's own table), the slots, the headline cells, the tests (the hand's),
# the grading tail. The tuple in the tests is the model's print, typed as a literal (the honest-pairing guard reads it).
import json
S = '<scratch>/'
G = json.load(open(S + 'o8_s3_gen.json', encoding='utf-8'))
cells = open(S + 's3_cells_A.py', encoding='utf-8').read() + '\n' + open(S + 's3_cells_B.py', encoding='utf-8').read()
tests = open(S + 's3_tests.py', encoding='utf-8').read().replace('__PRED__', repr(tuple(G['PRED'])))
HEADER = '''#!/usr/bin/env python3
"""cold_run_mamre.py — FROM MAMRE TO THE HEAP (O8 S3, 2026-09-08; World/step9/NARRATIVE_GAPS.md section 7): Genesis 18-20, 22,
25-31's narrative on the world engine — the visit and the plea, Sodom's night and the overthrow, Gerar's dream and the first
prayer, the binding, Abraham's end and Ishmael's twelve, the twins and the birthright, Isaac at Gerar and the wells, the
blessing and the grudge, Bethel's ladder and vow, the well and the stone, the two sevens and the switched bride, the twelve
names, the speckled wage, the flight, the pursuit and the heap with its two tongues. The third of the four narrative sittings
of O8 (the census: NARRATIVE_GAPS.md section 1). Genesis 21, 23 and 24 are the pre-Sinai and family engines'; this runner's
span is the story's verses alone (dependency_dispositions.yaml), and the story's acts fetch those engines' law by call.

The form: (1) the acts and speeches of the ink at their narrative verses (the register test), each a registered type with
its witness cut from the verse's consonants; (2) the answer sheet — the Mishnah's rows on this stretch read whole from the
shelf, each verified by a token in its own ink (Bava Kamma 8:7 the forgiveness, Avot 5:3 the ten trials, Bava Metzia 7:8 the
four keepers, Bava Batra 8:5 the firstborn's portion, Bekhorot 8:1 the firstborn by the head, Moed Katan 1:7 the joy rule,
Sanhedrin 10:3 Sodom); (3) the shelf — the Babylonian rows and the Genesis spine's rows located by script this sitting, each
verified by a token; (4) seventeen cells in the text's order, every cell a value with its provenance and its registered
effects; (5) the scene: the stretch's acts on a bare world, the tuple predicted by a hand-model before this file was typed
(scratchpad o8_s3_predict.py); (6) the wrap: law_mamre, the forty-second daemon, whose writes per event are the model's own
table. Five engines CALLED where the ink names their institution: the pre-Sinai code (the covenant's eighth day on every male
birth — the scene's laws carry law_pre_sinai beside law_mamre, as S1), the offerings (22:13's ram, 31:54's sacrifice), the
substitution engine (28:22's tithe), the family engine (25:5, 25:10), the guardians (THE PAID KEEPER on 31:38-40). The dating
lives on the sequential tape (convention 13). Zero-report law: every claimed ink token is probed before anything runs.
"""
import sqlite3, sys, os, json, re, io, contextlib
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import effects_layer as FX
from compile_guards import check_honest_pairing

GUARDED = check_honest_pairing(os.path.abspath(__file__))
print('honest-pairing guard: %d tests checked, every expectation a literal' % GUARDED)

DB = '<repo>/Data/tanakh.sqlite'
con = sqlite3.connect('file:%s?mode=ro' % DB, uri=True)


def strip(s): return re.sub(r'[֑-ׇ]', '', s)


def toks(ch, vs, book='Gen'):
    r = con.execute("select id from verses where book=? and chapter=? and verse=?", (book, ch, vs)).fetchone()
    return [re.sub(r'[֑-ׇ/]', '', h) for (h,) in con.execute("select he from words where verse_id=? order by idx", (r[0],))]


NV = {c: n for c, n in con.execute("select chapter, count(*) from verses where book='Gen' group by chapter")}
SPAN = [18, 19, 20, 22, 25, 26, 27, 28, 29, 30, 31]


# ---- (0) THE PROBES: every kind's witnesses in the span and the rosters' names — a run of consonants found contiguous in its verse, or the run stops ----
PROBES = __PROBES__
_T = {}
for ch, vs, run in PROBES:
    ws = _T.setdefault((ch, vs), toks(ch, vs)); want = run.split()
    assert any(ws[i:i + len(want)] == want for i in range(len(ws) - len(want) + 1)), 'PROBE FAILED: %r not in Gen %d:%d' % (run, ch, vs)
print('probes: %d ink runs verified in their verses (Gen 18-31)' % len(PROBES))

I, M, A, D, P, H = 'INK', 'MOVE', 'ANSWER-SHEET', 'DATA', 'IMPORT', 'HYPOTHESIS'


def cell(v, p, why, effects):
    FX.validate(effects)
    return {'v': v, 'p': p, 'why': why, 'fx': effects}


with contextlib.redirect_stdout(io.StringIO()), contextlib.redirect_stderr(io.StringIO()):   # the callees grade themselves at import — their reports stay their own
    import cold_run_pre_sinai as PS_       # THE LIVE EDGES (dependency_dispositions.yaml): the covenant's eighth day on every male birth; the covenant's heads at 26:3
    import cold_run_offerings as OF        # the burnt offering (22:13); the peace offering's shape (31:54)
    import cold_run_temurah as TM          # the tithe vowed (28:22), as 14:20's
    import cold_run_family as FA           # all that he had (25:5); the purchased field (25:10)
    import cold_run_guardians as GD        # THE PAID KEEPER: Jacob's account of 31:38-40 against the four keepers' verdict table
import world_engine as WE


# ---- (1) the ink censuses the cells read (recomputed here; every count a measurement) ----
def _seats(pred, ch_lo, ch_hi):
    return [(ch, vs) for ch in SPAN if ch_lo <= ch <= ch_hi for vs in range(1, NV[ch] + 1) if pred(toks(ch, vs))]


# ---- (2) the answer sheet — the Mishnah's rows as TEST DATA, each verified by a token in its own ink ----
def _load(path):
    d = json.load(open(path, encoding='utf-8')); return d['text'] if isinstance(d, dict) and 'text' in d else d
def mishnah(tractate, ch, m, must):
    txt = strip(re.sub(r'<[^>]+>', '', _load('<repo>/Data/mishnah_%s_he.json' % tractate)[ch - 1][m - 1]))
    assert must in txt, 'answer-sheet check failed: %r not in Mishnah %s %d:%d' % (must, tractate, ch, m)
_BAV = {}
def _bavli(tr, daf, side, seg, must):
    T = _BAV.setdefault(tr, _load('<repo>/Data/bavli_%s_he.json' % tr))
    txt = strip(re.sub(r'<[^>]+>', '', T[2 * daf - 2 + (1 if side == 'b' else 0)][seg - 1]))
    assert must in txt, 'shelf check failed: %r not in %s %d%s:%d' % (must, tr, daf, side, seg)
_BR = None
def _br(par, row, must):
    global _BR
    if _BR is None: _BR = _load('<repo>/Data/bereshit_rabbah_he.json')
    txt = strip(re.sub(r'<[^>]+>', '', _BR[par - 1][row - 1]))
    assert must in txt, 'Bereshit Rabbah check failed: %r not in %d:%d' % (must, par, row)
SHEET = [
    ('bava_kamma', 8, 7, 'ויתפלל אברהם'), ('pirkei_avot', 5, 3, 'עשרה נסיונות'), ('bava_metzia', 7, 8, 'ארבעה שומרין'), ('bava_batra', 8, 5, 'לא יטל פי שנים'),
    ('bekhorot', 8, 1, 'בכור לנחלה'), ('moed_katan', 1, 7, 'אין נושאין נשים במועד'), ('sanhedrin', 10, 3, 'אנשי סדום'),
]
for t, ch, m, must in SHEET: mishnah(t, ch, m, must)
SHEET2 = [   # the Babylonian rows (file index 2*daf-2, +1 for b) and the Genesis spine's rows (Bereshit Rabbah, parashah:row) — every one located by script this sitting
    ('B', 'megillah', 17, 'a', 5, 'בבית עבר'), ('B', 'megillah', 17, 'a', 6, 'עשרים ושתים'), ('B', 'yevamot', 64, 'a', 6, 'בן ארבעים שנה'), ('B', 'yoma', 28, 'b', 10, 'עירובי תבשילין'),
    ('B', 'kiddushin', 82, 'a', 10, 'כל התורה כולה'), ('B', 'bava_batra', 16, 'b', 11, 'תבשיל של עדשים'), ('B', 'bava_batra', 16, 'b', 12, 'עדשה'), ('B', 'bava_kamma', 92, 'a', 4, 'ויתפלל אברהם'),
    ('B', 'bava_kamma', 92, 'a', 16, 'ויתפלל אברהם'), ('B', 'bava_metzia', 93, 'b', 3, 'אכלני חורב'), ('B', 'bava_metzia', 86, 'b', 3, 'בן בקר'), ('B', 'bava_metzia', 86, 'b', 7, 'בן בקר'),
    ('B', 'shabbat', 127, 'a', 13, 'הכנסת אורחין'), ('B', 'sanhedrin', 89, 'b', 8, 'נסה את אברהם'), ('B', 'sanhedrin', 89, 'b', 9, 'דבריו של שטן'), ('B', 'sanhedrin', 89, 'b', 14, 'ישמעאל'),
    ('B', 'sanhedrin', 91, 'a', 16, 'מתנות'), ('B', 'sanhedrin', 109, 'a', 8, 'אנשי סדום'), ('B', 'moed_katan', 8, 'b', 9, 'שמחה בשמחה'), ('B', 'moed_katan', 9, 'a', 4, 'שמחה בשמחה'),
    ('B', 'chullin', 91, 'b', 8, 'מאבני המקום'), ('B', 'rosh_hashanah', 10, 'b', 10, 'בפסח נולד יצחק'), ('B', 'rosh_hashanah', 11, 'a', 2, 'בפסח נולד יצחק'), ('B', 'rosh_hashanah', 11, 'a', 16, 'נפקדה שרה'),
    ('B', 'rosh_hashanah', 16, 'a', 16, 'עקידת יצחק'), ('B', 'berakhot', 6, 'b', 8, 'אשר עמד שם'), ('B', 'berakhot', 26, 'b', 4, 'תפלות אבות תקנום'), ('B', 'berakhot', 26, 'b', 5, 'אברהם תקן תפלת שחרית'),
    ('B', 'berakhot', 26, 'b', 14, 'אבות תקנום'), ('B', 'ketubot', 50, 'a', 3, 'עשר אעשרנו'),
    ('R', 48, 12, 'פרוס הפסח'), ('R', 49, 6, 'חמשים ושתים'), ('R', 49, 8, 'הגשה לתפלה'), ('R', 49, 9, 'חמשים'), ('R', 49, 12, 'מחמשים לחמשה'), ('R', 50, 4, 'ויעש להם משתה'), ('R', 51, 5, 'נציב מלח'),
    ('R', 55, 1, 'נסיון אחר נסיון'), ('R', 56, 9, 'איל אחר'), ('R', 56, 11, 'נסיון עשירי'), ('R', 58, 5, 'מהר המוריה'), ('R', 61, 4, 'זו הגר'), ('R', 62, 1, 'בשיבה טובה'), ('R', 64, 3, 'עולה תמימה'),
    ('R', 64, 6, 'מפני המעשרות'), ('R', 65, 1, 'בן ארבעים'), ('R', 65, 14, 'שני גדיי'), ('R', 68, 5, 'ששים ושלש'), ('R', 68, 10, 'כיבא השמש'), ('R', 68, 11, 'ארבע עשרה'), ('R', 70, 7, 'עשר אעשרנו'),
    ('R', 70, 19, 'שמחה בשמחה'), ('R', 72, 2, 'דודאים'), ('R', 72, 3, 'הפסידה'), ('R', 72, 5, 'דודאים'), ('R', 73, 1, 'בראש השנה'), ('R', 74, 3, 'עשרת מנים'), ('R', 74, 4, 'לא יחיה'),
    ('R', 74, 5, 'ותגנב רחל'), ('R', 74, 6, 'שלשת ימים'), ('R', 74, 9, 'לא יחיה'), ('R', 74, 11, 'עשרת מנים'),
]
for row in SHEET2:
    if row[0] == 'B': _bavli(*row[1:])
    else: _br(*row[1:])
print('answer sheet: %d Mishnah rows verified in their own ink; shelf: %d rows (Babylonian and Bereshit Rabbah) verified by token' % (len(SHEET), len(SHEET2)))
'''
SLOTS_CODE = "SLOTS = [   # the slot order of the tuple — fixed by scratchpad o8_s3_predict.py before this file was typed\n" + ''.join("    %r,\n" % (tuple(x),) for x in G['SLOTS']) + "]\n"
BUILD = '''
def build(q):
    if q == 'world':
        return cell(SCENE, I, "THE SCENE on the world engine — the three hundred and fifty-seven effect slots of the declaration in order, then the opens, the timers set and fired, the closes, the day (the hand-model's print, scratchpad o8_s3_predict.py); the four story timers and the thirteen eighth days fire inside the scene; the one-year timer of 18:10 finds no birth here", ['son_promised_at_the_season', 'return_at_the_season', 'seven_years_service', 'week_of_the_feast', 'second_seven_service'])
    if q == 'headline_join':
        return cell('the_season_joins_two_shelf_rows', M, "THE HEADLINE (1): the visit placed on Passover of the year before (Bereshit Rabbah 48:12) and Isaac's birth placed on Passover (Rosh Hashanah 10b:10) are two independent rows; the ink's own 'at this living season' (18:10, 18:14) and 'at the set time' (21:2) join them — the one-year timer set at the visit fires on the birth's day (the sequence runner CH0)", ['return_at_the_season', 'son_promised_at_the_season'])
    if q == 'headline_installation':
        return cell('the_covenants_daemon_runs_on_the_stretchs_births', D, "THE HEADLINE (2): the twins and the eleven sons are `born` under Genesis 17, and the pre-Sinai daemon writes their eighth-day debits by the statute's own run — thirteen, none on Dinah (17:12 'every male', the field read); Lot's daughters' and Nahor's births are `bore` and `begot`, outside the covenant — the naming stand-in for installation (THE TIME CONSENSUS's T1)", ['daughter_born', 'begotten'])
    if q == 'headline_keeper':
        return cell('the_paid_keeper_grades_jacobs_account', P, "THE HEADLINE (3): 31:38-40 laid on the four keepers' verdict table by call — theft PAY, the witnessed accident OATH, the loss PAY; Jacob paid for the torn too: the keeper's ceiling exceeded, as Bava Metzia 93b:3 reads it ('is Jacob our father a city watchman?!')", ['keeper_account', 'torn_borne_beyond_duty'])
    if q == 'headline_fourteen':
        return cell('the_fourteen_hidden_years_fall_out_of_the_inks_numbers', M, "THE HEADLINE (4): Ishmael's death (16:16 + 25:17) sets Jacob's sixty-three (25:26) — Bereshit Rabbah 68:5's number by the ink's arithmetic; Megillah 17a's fourteen from there places the departure; the two sevens and Joseph's birth from Pharaoh's side (41:46, 45:6, 47:9) meet at the fourteen's end — the sequence runner CH3, CH4, CH5", ['seven_years_service', 'second_seven_service', 'twenty_years_served'])
    if q == 'headline_two_tongues':
        return cell('one_heap_two_names', I, "THE HEADLINE (5): 'and Laban called it Jegar-sahadutha, and Jacob called it Galeed' (31:47) — one heap, the Aramaic and the Hebrew, both name_given on the ledger; then Galeed by the report formula (31:48) and Mizpah (31:49): four namings on one witness", ['name_given', 'heap_made', 'witness_declared'])
    return cell('no_case', I, '', [FX.NONE])

'''
TAIL = '''
if __name__ == '__main__':
    print()
    ok = 0
    frac = {I: 0, M: 0, A: 0, D: 0, P: 0, H: 0}
    misses = []
    for name, c, want in TESTS:
        hit = c['v'] == want
        ok += hit
        frac[c['p']] += 1
        if not hit: misses.append((name, c['v']))
        print('%s %-76s [%s] %s' % ('OK ' if hit else 'MISS', name[:76], c['p'], '' if hit else 'got=%r' % (c['v'],)))
        print('     effects: %s' % ', '.join(c['fx']))
    n = len(TESTS)
    assert n == GUARDED, (n, GUARDED)
    print()
    print('MATRIX: %d/%d cells match the answer sheet' % (ok, n))
    print('FRACTIONS: pure ink %d/%d (%d%%) · recorded moves %d/%d (%d%%) · answer-sheet %d/%d · data %d/%d · imports %d/%d · hypotheses %d/%d' % (
          frac[I], n, 100 * frac[I] // n, frac[M], n, 100 * frac[M] // n, frac[A], n, frac[D], n, frac[P], n, frac[H], n))
    print('effects: every cell carries REGISTERED effects — two hundred and twenty-seven discovered in the stretch\\'s own words and registered first (visitors_received ... ate_and_lodged) [effects law satisfied]')
    print('SCENE: %r' % (SCENE,))
    _W.print_coverage()
    if ok == n:
        print()
        print('FROM MAMRE TO THE HEAP STANDS — the visit and the plea, Sodom and the pillar of salt, the first prayer, the binding, the good old age, the twins and the birthright, the wells, the blessing, the ladder and the vow, the stone, the two sevens, the twelve names, the speckled wage, the flight, the heap with its two tongues: %d/%d' % (ok, n))
    else:
        print('MISSES (%d):' % len(misses))
        for m_ in misses: print('  -', m_[0][:80], '->', m_[1])
        sys.exit('MISSES REMAIN — a miss is evidence, never a retype: read it.')
'''
src = HEADER.replace('__PROBES__', repr([tuple(p) for p in G['PROBES']])) + '\n' + cells + '\n' + G['DAEMON'] + '\n' + SLOTS_CODE + '\n' + G['SCENE_CODE'] + '\n' + BUILD + '\n' + tests + '\n' + TAIL
open('<repo>/World/step9/cold_run_mamre.py', 'w', encoding='utf-8').write(src)
print('cold_run_mamre.py assembled: %d lines' % src.count('\n'))

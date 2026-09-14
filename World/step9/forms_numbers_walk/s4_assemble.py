#!/usr/bin/env python3
# O8 S4 — assembles cold_run_joseph.py: the header, the probes, the helpers, the answer sheet and the shelf rows, the rosters, the cells (the hand's),
# the daemon and the scene (from the generator, the hand-model's own table), the slots, the headline cells, the tests (the hand's),
# the grading tail. The tuple in the tests is the model's print, typed as a literal (the honest-pairing guard reads it).
import json
S = '<scratch>/'
G = json.load(open(S + 'o8_s4_gen.json', encoding='utf-8'))
cells = open(S + 's4_cells_A.py', encoding='utf-8').read() + '\n' + open(S + 's4_cells_B.py', encoding='utf-8').read()
tests = open(S + 's4_tests.py', encoding='utf-8').read().replace('__PRED__', repr(tuple(G['PRED'])))
HEADER = '''#!/usr/bin/env python3
"""cold_run_joseph.py — FROM THE FORD TO THE COFFIN (O8 S4, 2026-09-08; World/step9/NARRATIVE_GAPS.md section 8): Genesis 32-37, 39-47,
50's narrative on the world engine — the night at the Jabbok and the meeting, Shechem's field and Dinah, Bethel again and the three
deaths, Edom's roster, the dreamer sold, Potiphar's house and the prison, the two dreams and Pharaoh's, the rise, the two descents,
the cup and the surety, I am Joseph, the seventy, Goshen and the fifth, the oath, the mourning and the coffin. The last of the four
narrative sittings of O8 (the census: NARRATIVE_GAPS.md section 1). Genesis 38, 48 and 49 are the family engine's, as are its seats
inside the span (32:29, 32:33, 50:12-13); this runner's span is the story's verses alone (dependency_dispositions.yaml), and the
story's acts fetch the engines' law by call.

The form: (1) the acts and speeches of the ink at their narrative verses (the register test), each a registered type with its
witness cut from the verse's consonants; (2) the answer sheet — the Mishnah's rows on this stretch read whole from the shelf, each
verified by a token in its own ink (Megillah 4:10 Reuben's act, Sotah 1:9 Joseph's burial of his father, Bava Batra 10:8 and Bava
Metzia 5:11 the surety, Shabbat 19:3 the third day, Pesachim 1:1 the search, Bava Kamma 8:7 forgiveness, Ketubot 3:4 the seducer,
Yevamot 6:6 be fruitful, Bava Batra 8:2 the inheritance order); (3) the shelf — the Babylonian rows and the Genesis spine's rows
located by script this sitting, each verified by a token; (4) twenty-three cells in the text's order, every cell a value with its
provenance and its registered effects; (5) the scene: the stretch's acts on a bare world, the tuple predicted by a hand-model
before this file was typed (scratchpad o8_s4_predict.py); (6) the wrap: law_joseph, the forty-third daemon, whose writes per event
are the model's own table. Six engines CALLED where the ink names their institution: the pre-Sinai code (the covenant's eighth day
on Benjamin, Manasseh and Ephraim — the scene's laws carry law_pre_sinai beside law_joseph, as S1 and S3), the offerings (46:1's
sacrifices; 35:14's libation by the token), the family engine (33:19's purchase, 47:29's burial command, the census against the
inheritance order), the ordinances (THE MOHAR of 34:12 against Exodus 22:15-16; THE THIEF SOLD of 44:9-17 against Exodus 22:2),
the vestments (37:31's dipped tunic as the source of the tunic's atonement — THE FLOW REVERSED). The dating lives on the
sequential tape (convention 13). Zero-report law: every claimed ink token is probed before anything runs.
"""
import sqlite3, sys, os, json, re, io, contextlib
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import effects_layer as FX
from compile_guards import check_honest_pairing

GUARDED = check_honest_pairing(os.path.abspath(__file__))
print('honest-pairing guard: %d tests checked, every expectation a literal' % GUARDED)

DB = '<repo-old>/elijah_docket/tanakh.sqlite'
con = sqlite3.connect('file:%s?mode=ro' % DB, uri=True)


def strip(s): return re.sub(r'[֑-ׇ]', '', s)


def toks(ch, vs, book='Gen'):
    r = con.execute("select id from verses where book=? and chapter=? and verse=?", (book, ch, vs)).fetchone()
    return [re.sub(r'[֑-ׇ/]', '', h) for (h,) in con.execute("select he from words where verse_id=? order by idx", (r[0],))]


NV = {c: n for c, n in con.execute("select chapter, count(*) from verses where book='Gen' group by chapter")}
SPAN = [32, 33, 34, 35, 36, 37, 39, 40, 41, 42, 43, 44, 45, 46, 47, 50]


# ---- (0) THE PROBES: every kind's witnesses in the span and the rosters' names — a run of consonants found contiguous in its verse, or the run stops ----
PROBES = __PROBES__
_T = {}
for ch, vs, run in PROBES:
    ws = _T.setdefault((ch, vs), toks(ch, vs)); want = run.split()
    assert any(ws[i:i + len(want)] == want for i in range(len(ws) - len(want) + 1)), 'PROBE FAILED: %r not in Gen %d:%d' % (run, ch, vs)
print('probes: %d ink runs verified in their verses (Gen 32-50)' % len(PROBES))
ROSTERS = __ROSTERS__   # the seventy by register (46:8-25), the twelve (35:23-26), the eight kings (36:32-39) — every name among the probes

I, M, A, D, P, H = 'INK', 'MOVE', 'ANSWER-SHEET', 'DATA', 'IMPORT', 'HYPOTHESIS'


def cell(v, p, why, effects):
    FX.validate(effects)
    return {'v': v, 'p': p, 'why': why, 'fx': effects}


with contextlib.redirect_stdout(io.StringIO()), contextlib.redirect_stderr(io.StringIO()):   # the callees grade themselves at import — their reports stay their own
    import cold_run_pre_sinai as PS_       # THE LIVE EDGES (dependency_dispositions.yaml): the covenant's eighth day on every male birth; the covenant's heads
    import cold_run_offerings as OF        # the peace offering's shape (46:1); the libation's token (35:14)
    import cold_run_family as FA           # the purchase (33:19); the inheritance order (43:33, 46:8)
    import cold_run_mishpatim_2 as MP2     # THE MOHAR (34:12 against Exodus 22:15-16)
    import cold_run_mishpatim_3 as MP3     # THE THIEF SOLD (44:9-17 against Exodus 22:2)
    import cold_run_vestments as VS        # the tunic's atonement for bloodshed (37:31 — Arakhin 16a:13, Zevachim 88b:6)
import world_engine as WE


# ---- (1) the ink censuses the cells read (recomputed here; every count a measurement) ----
def _seats(pred, ch_lo, ch_hi):
    return [(ch, vs) for ch in SPAN if ch_lo <= ch <= ch_hi for vs in range(1, NV[ch] + 1) if pred(toks(ch, vs))]


# ---- (2) the answer sheet — the Mishnah's rows as TEST DATA, each verified by a token in its own ink ----
def _load(path):
    d = json.load(open(path, encoding='utf-8')); return d['text'] if isinstance(d, dict) and 'text' in d else d
def mishnah(tractate, ch, m, must):
    txt = strip(re.sub(r'<[^>]+>', '', _load('<repo-old>/Data/mishnah_%s_he.json' % tractate)[ch - 1][m - 1]))
    assert must in txt, 'answer-sheet check failed: %r not in Mishnah %s %d:%d' % (must, tractate, ch, m)
_BAV = {}
def _bavli(tr, daf, side, seg, must):
    T = _BAV.setdefault(tr, _load('<repo-old>/Data/bavli_%s_he.json' % tr))
    txt = strip(re.sub(r'<[^>]+>', '', T[2 * daf - 2 + (1 if side == 'b' else 0)][seg - 1]))
    assert must in txt, 'shelf check failed: %r not in %s %d%s:%d' % (must, tr, daf, side, seg)
_BR = None
def _br(par, row, must):
    global _BR
    if _BR is None: _BR = _load('<repo-old>/Data/bereshit_rabbah_he.json')
    txt = strip(re.sub(r'<[^>]+>', '', _BR[par - 1][row - 1]))
    assert must in txt, 'Bereshit Rabbah check failed: %r not in %d:%d' % (must, par, row)
SHEET = [
    ('megillah', 4, 10, 'מעשה ראובן'), ('sotah', 1, 9, 'יוסף זכה לקבר את אביו'), ('bava_batra', 10, 8, 'ערב היוצא לאחר חתום שטרות'), ('bava_metzia', 5, 11, 'והערב'),
    ('shabbat', 19, 3, 'בהיותם כאבים'), ('pesachim', 1, 1, 'בודקין את החמץ'), ('bava_kamma', 8, 7, 'אין נמחל לו עד שיבקש ממנו'), ('ketubot', 3, 4, 'המפתה נותן שלשה דברים'),
    ('yevamot', 6, 6, 'לא יבטל אדם מפריה ורביה'), ('bava_batra', 8, 2, 'סדר נחלות'),
]
for t, ch, m, must in SHEET: mishnah(t, ch, m, must)
SHEET2 = [   # the Babylonian rows (file index 2*daf-2, +1 for b) and the Genesis spine's rows (Bereshit Rabbah, parashah:row) — every one located by script this sitting
    ('B', 'megillah', 16, 'b', 2, 'צוארי בנימן'), ('B', 'megillah', 16, 'b', 3, 'עיני אחי בנימין'), ('B', 'megillah', 16, 'b', 4, 'עשרה חמורים'), ('B', 'megillah', 16, 'b', 5, 'תעלא בעידניה'),
    ('B', 'megillah', 16, 'b', 6, 'ראש המטה'), ('B', 'megillah', 16, 'b', 7, 'עשרה נרות'), ('B', 'megillah', 17, 'a', 2, 'ששים ושלש'), ('B', 'megillah', 17, 'a', 3, 'בן שלשים שנה'),
    ('B', 'megillah', 17, 'a', 4, 'שלשים ומאת שנה'), ('B', 'megillah', 17, 'a', 5, 'בבית עבר'), ('B', 'megillah', 17, 'a', 6, 'עשרים ושתים שנה'), ('B', 'megillah', 17, 'a', 7, 'שמונה עשר חודש'),
    ('B', 'megillah', 18, 'a', 17, 'אל אלהי ישראל'), ('B', 'bava_batra', 115, 'b', 4, 'שבא צבעון על אמו'), ('B', 'bava_batra', 123, 'b', 1, 'זו יוכבד'), ('B', 'bava_batra', 173, 'b', 9, 'אנכי אערבנו'),
    ('B', 'bava_batra', 173, 'b', 10, 'קבלנות'), ('B', 'chullin', 95, 'b', 14, 'דאיתחזק תלתא זימני'), ('B', 'chullin', 101, 'b', 9, 'לאחר מעשה'), ('B', 'pesachim', 7, 'b', 14, 'מציאה מחיפוש'),
    ('B', 'pesachim', 119, 'a', 6, 'כל כסף וזהב שבעולם'), ('B', 'sotah', 10, 'b', 7, 'הכר נא הכתנת'), ('B', 'sotah', 13, 'b', 12, 'בא גבריאל ופירעו'), ('B', 'sotah', 36, 'b', 9, 'בנימן כתיב'),
    ('B', 'sotah', 36, 'b', 19, 'גנוני מלכות'), ('B', 'nedarim', 31, 'b', 14, 'סכנה היא'), ('B', 'yevamot', 65, 'b', 5, 'פרה ורבה'), ('B', 'yevamot', 65, 'b', 7, 'לשנות בדבר השלום'),
    ('B', 'ketubot', 111, 'a', 23, 'ארבע מאות פרסה'), ('B', 'taanit', 10, 'b', 6, 'למה תתראו'), ('B', 'taanit', 10, 'b', 11, 'בכי טוב'), ('B', 'taanit', 11, 'a', 4, 'בשני רעבון'),
    ('B', 'sanhedrin', 6, 'b', 5, 'מה בצע'), ('B', 'sanhedrin', 92, 'a', 3, 'המשביר'), ('B', 'sanhedrin', 99, 'b', 8, 'נפק מינה עמלק'), ('B', 'arakhin', 16, 'a', 13, 'כתונת מכפרת על שפיכות דמים'),
    ('B', 'berakhot', 12, 'b', 28, 'לא יקרא שמך עוד יעקב'), ('B', 'berakhot', 34, 'b', 3, 'השתחואה'), ('B', 'berakhot', 42, 'a', 8, 'בגלל יוסף'), ('B', 'berakhot', 55, 'b', 2, 'עד עשרים ושתים שנה'),
    ('B', 'beitzah', 16, 'a', 3, 'לישנא דמזוני'), ('B', 'bava_kamma', 92, 'a', 19, 'שהוכפלו בשמות'), ('B', 'avodah_zarah', 25, 'b', 8, 'ירחיב לו את הדרך'), ('B', 'horayot', 10, 'b', 11, 'ותשא אשת אדניו'),
    ('B', 'nazir', 5, 'a', 5, 'שנתים ימים'), ('B', 'chagigah', 3, 'a', 14, 'נחשים ועקרבים'), ('B', 'chagigah', 4, 'b', 8, 'תוכחה של בשר ודם'), ('B', 'bava_metzia', 39, 'b', 8, 'בלא חתימת זקן'),
    ('R', 78, 8, 'אחרון אחרון חביב'), ('R', 78, 9, 'נקוד עליו'), ('R', 78, 11, 'כתות כתות'), ('R', 78, 12, 'מה פני אלהים דין'), ('R', 78, 14, 'יעבר נא אדני'), ('R', 79, 5, 'שלם בגופו'),
    ('R', 79, 7, 'במאה קשיטה'), ('R', 79, 8, 'אלוה בעליונים'), ('R', 80, 6, 'ואיש תבונות יחריש'), ('R', 80, 8, 'רמיות דברים'), ('R', 80, 9, 'מרחיצין את הקטן'), ('R', 80, 10, 'שלא נטלו עצה מיעקב'),
    ('R', 80, 12, 'צלולה היתה החבית'), ('R', 81, 1, 'מוקש אדם ילע קדש'), ('R', 81, 2, 'אם נבלת בהתנשא'), ('R', 81, 5, 'לשון יונית'), ('R', 82, 9, 'בר צערי'), ('R', 82, 10, 'אין עושין נפשות לצדיקים'),
    ('R', 82, 11, 'שלשלת יוחסין'), ('R', 82, 14, 'פילגש לאליפז'), ('R', 82, 15, 'ענה ענה תרי זמני'), ('R', 83, 1, 'נמשלו עובדי כוכבים כספינה'), ('R', 84, 7, 'מעשה נערות'), ('R', 84, 8, 'זיו איקונין'),
    ('R', 84, 16, 'זה הפינס'), ('R', 84, 17, 'עברתן של שבטים'), ('R', 84, 18, 'עברו אותן הדינים'), ('R', 84, 19, 'בשקו ובתעניתו'), ('R', 84, 21, 'כמה בנות היו לו'), ('R', 86, 3, 'הקנויין קונין'),
    ('R', 87, 5, 'בדבר מצוה ממאנין'), ('R', 87, 10, 'שמושו היה ערב לרבו'), ('R', 88, 5, 'אלו ישראל'), ('R', 88, 7, 'ואני לא אשכחהו'), ('R', 89, 1, 'קץ שם לחשך'), ('R', 90, 3, 'משלו נתנו לו'),
    ('R', 90, 5, 'לקמצים'), ('R', 91, 3, 'לעדה שהיא עשרה'), ('R', 91, 7, 'נעשה נכרי להם'), ('R', 91, 8, 'לשון דרומי'), ('R', 92, 8, 'עשרה בני אדם'), ('R', 92, 9, 'בכסף ראשון'),
    ('R', 93, 9, 'פיוס ליוסף'), ('R', 93, 12, 'שני בית המקדשות'), ('R', 94, 5, 'חזרתי על כל בעלי אגדה'), ('R', 94, 9, 'ששים וששה כוסות'), ('R', 95, 4, 'שלא היו גבורים'), ('R', 96, 5, 'למה לא קרא לא לראובן'),
    ('R', 100, 8, 'שלא זמנן לסעודה'), ('R', 100, 9, 'שמדבר על הלב'), ('R', 100, 11, 'כשתהיו עולין'),
]
for row in SHEET2:
    if row[0] == 'B': _bavli(*row[1:])
    else: _br(*row[1:])
print('answer sheet: %d Mishnah rows verified in their own ink; shelf: %d rows (Babylonian and Bereshit Rabbah) verified by token' % (len(SHEET), len(SHEET2)))
'''
SLOTS_CODE = "SLOTS = [   # the slot order of the tuple — fixed by scratchpad o8_s4_predict.py before this file was typed\n" + ''.join("    %r,\n" % (tuple(x),) for x in G['SLOTS']) + "]\n"
BUILD = '''
def build(q):
    if q == 'world':
        return cell(SCENE, I, "THE SCENE on the world engine — the two hundred and eighty-eight effect slots of the declaration in order, then the opens, the timers set and fired, the closes, the day (the hand-model's print, scratchpad o8_s4_predict.py); the nine story timers and the three eighth days fire inside the scene", ['head_lifted_up_due', 'head_lifted_off_due', 'custody_three_days', 'plenty_seven_years', 'famine_seven_years', 'five_years_of_famine_left', 'embalming_forty_days', 'egypt_wept_seventy', 'seven_days_mourning'])
    if q == 'headline_flow_reversed':
        return cell('narrative_verses_feed_law_rows', M, "THE HEADLINE (1): two narrative verses are the SOURCE of two law rows — 'they dipped the tunic in the blood' (37:31) for the tunic's atonement (Arakhin 16a:13, the vestments engine's row read by call) and 'he searched ... and found' (44:12) for the search for leaven (Pesachim 7b:14 on Mishnah Pesachim 1:1): the flow runs from the story into the law, not the reverse", ['coat_dipped', 'cup_found'])
    if q == 'headline_thief_sold':
        return cell('three_verdicts_on_the_rules_shape', P, "THE HEADLINE (2): 44:9, 44:10, 44:17 laid on Exodus 22:2's compiled 'sold for his theft' by call — the brothers' 'let him die' outside the rule, the steward's and Joseph's 'my slave' inside it; the mohar of 34:12 on Exodus 22:15-16 the same way: the story's speeches graded by the law's function", ['finder_a_slave_ruled', 'mohar_offered_unbounded'])
    if q == 'headline_two_absences':
        return cell('twenty_two_on_two_chains', M, "THE HEADLINE (3): Megillah 17a:6's twenty-two years computed on two independent chains of the tape — Jacob's absence off Ishmael's death and the fourteen (S3's chain) and Joseph's off Pharaoh's side (41:46, 45:6) — the sequence runner CJ0, a JOIN of the two sittings' markers", ['years_confessed', 'thirty_at_the_standing'])
    if q == 'headline_seventy':
        return cell('the_missing_one_filed_open', I, "THE HEADLINE (4): the seventy's sub-totals meet (33 + 16 + 14 + 7 = 70; 66 = 70 − 4) and the names do not (Leah's 32 living against 33) — the DIVERGE filed OPEN with the shelf's five answers named, none the ink's (CJ3)", ['souls_counted'])
    if q == 'headline_closes_by_seat':
        return cell('four_closes_by_seat', D, "THE HEADLINE (5): law_joseph closes four of its own entries on OTHER ENGINES' events by seat — brought_up_promised and burial_in_canaan_sworn on the family's burial (50:13), visitation_promised on the exodus story's belief (Exod 4:31), bones_oath on its bones_taken (Exod 13:19) — the ink's own receipts across engines and books (CJ7)", ['brought_up_promised', 'burial_in_canaan_sworn', 'visitation_promised', 'bones_oath'])
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
    print('effects: every cell carries REGISTERED effects — two hundred and twenty-four discovered in the stretch\\'s own words and registered first [effects law satisfied]')
    print('SCENE: %r' % (SCENE,))
    _W.print_coverage()
    if ok == n:
        print()
        print('FROM THE FORD TO THE COFFIN STANDS — the Jabbok, the meeting, Shechem, Bethel again, the three deaths, Edom, the dreamer, Potiphar, the prison, Pharaoh, the rise, the two descents, the cup, I am Joseph, the seventy, Goshen, the fifth, the oath, the mourning, the coffin: %d/%d' % (ok, n))
    else:
        print('MISSES (%d):' % len(misses))
        for m_ in misses: print('  -', m_[0][:80], '->', m_[1])
        sys.exit('MISSES REMAIN — a miss is evidence, never a retype: read it.')
'''
src = (HEADER.replace('__PROBES__', repr([tuple(p) for p in G['PROBES']])).replace('__ROSTERS__', repr({k: [tuple(x) for x in v] for k, v in G['ROSTERS'].items()}))
       + '\n' + cells + '\n' + G['DAEMON'] + '\n' + SLOTS_CODE + '\n' + G['SCENE_CODE'] + '\n' + BUILD + '\n' + tests + '\n' + TAIL)
open('<repo-old>/World/step9/cold_run_joseph.py', 'w', encoding='utf-8').write(src)
print('cold_run_joseph.py assembled: %d lines' % src.count('\n'))

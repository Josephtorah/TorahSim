#!/usr/bin/env python3
"""cold_run_primeval.py — FROM EDEN TO HAGAR (O8 S2, 2026-09-08; World/step9/NARRATIVE_GAPS.md section 6): Genesis 2:4-16:16's
narrative on the world engine — the garden and the breach, the sentences and the exile, Cain and Abel, the two lines, the
ledger of Adam, the flood's prologue, the ark, the boarding, the rise, the remembering, the exit and the first altar, the
vineyard and the first human curse, the nations, Babel, Shem's line, the call, the descent to Egypt, the separation, the
war of the kings, the covenant between the pieces, Hagar. The second of the four narrative sittings of O8 (the census:
NARRATIVE_GAPS.md section 1). The pre-Sinai engine keeps 2:16-17, 2:24 and 9:1-17; this runner's span is the story's verses
alone (dependency_dispositions.yaml), and the story's acts fetch that engine's law by call.

The form: (1) the acts and speeches of the ink at their narrative verses (the register test), each a registered type with
its witness cut from the verse's consonants; (2) the answer sheet — the Mishnah's rows on this stretch read whole from the
shelf, each verified by a token in its own ink (Sanhedrin 10:3 the three generations, 4:5 the bloods, Avot 5:2 the ten
generations, 5:3 the trials, Eduyot 2:10 the twelve months, Yevamot 6:6 the ten years, Megillah 1:8 the Greek); (3) the run
— the scene on a bare world, the tuple predicted by script (scratchpad o8_s2_predict.py) before this file was typed;
(4) the misses filled by NAMED recorded readings — the Genesis spine Bereshit Rabbah 16-45 read row by row, and the
Babylonian Talmud at Sanhedrin 107b-109b, 37b, 70a, Nedarim 32a-b, Sotah 14a, Megillah 9b, 14a, Berakhot 40a, Kiddushin 30b,
Bava Batra 100a, Yevamot 64a, Chullin 89a, Eruvin 53a, Pesachim 118a, Rosh Hashanah 11b, Shabbat 55b; (5) the graded
matrix with per-cell provenance and EFFECTS on every verdict — a hundred and forty-three discovered in the stretch's own
words and registered first; (6) THE WRAP — law_primeval over the cells, declared first (the gate run to fail), consuming
the stretch's acts and writing the ledger: the promises as HEAVEN entries closed by the ink's own fulfillment statements
(the three land promises closed by 15:18's perfect), the decrees as HEAVEN entries closed by the narrated execution
(6:7's wiping at 7:23), the debits closed by their receipts (the ark, the boarding, the exit, the going, the pieces), the
two timers (the reprieve of a hundred and twenty years — retrograde-dated on the tape; the seven days before the flood).
Eight engines CALLED where the ink names their institution. The dating lives on the sequential tape (convention 13).
Zero-report law: every claimed ink token is probed before anything runs; the answer sheet is verified in its own ink.
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


# ---- (0) THE PROBES: every ink claim below is a run of consonants found contiguous in its verse, or the run stops ----
PROBES = [
 (2, 7, 'ויהי האדם לנפש חיה'), (2, 15, 'לעבדה ולשמרה'), (2, 20, 'ויקרא האדם שמות'), (2, 21, 'תרדמה'), (2, 22, 'ויבן יהוה אלהים את הצלע'), (2, 23, 'זאת הפעם'),
 (3, 6, 'ותקח מפריו ותאכל ותתן גם לאישה עמה ויאכל'), (3, 7, 'ותפקחנה עיני שניהם'), (3, 11, 'אשר צויתיך'), (3, 13, 'הנחש השיאני ואכל'), (3, 14, 'ארור אתה מכל הבהמה'),
 (3, 16, 'הרבה ארבה עצבונך והרנך'), (3, 17, 'ארורה האדמה בעבורך'), (3, 19, 'כי עפר אתה ואל עפר תשוב'), (3, 20, 'חוה כי הוא היתה אם כל חי'), (3, 21, 'כתנות עור וילבשם'),
 (3, 24, 'לשמר את דרך עץ החיים'), (4, 1, 'קניתי איש את יהוה'), (4, 3, 'מנחה ליהוה'), (4, 4, 'מבכרות צאנו ומחלבהן'), (4, 4, 'וישע יהוה אל הבל'), (4, 7, 'לפתח חטאת רבץ'),
 (4, 8, 'ויקם קין אל הבל אחיו ויהרגהו'), (4, 10, 'קול דמי אחיך צעקים'), (4, 12, 'נע ונד תהיה בארץ'), (4, 15, 'שבעתים יקם'), (4, 16, 'וישב בארץ נוד'), (4, 17, 'ויהי בנה עיר'),
 (4, 19, 'שתי נשים'), (4, 24, 'שבעים ושבעה'), (4, 25, 'שת לי אלהים זרע אחר'), (4, 26, 'אז הוחל לקרא בשם יהוה'), (5, 3, 'שלשים ומאת שנה'), (5, 5, 'תשע מאות שנה ושלשים שנה'),
 (5, 24, 'ואיננו כי לקח אתו אלהים'), (5, 29, 'זה ינחמנו'), (5, 32, 'בן חמש מאות שנה'), (6, 2, 'מכל אשר בחרו'), (6, 3, 'מאה ועשרים שנה'), (6, 5, 'רבה רעת האדם'),
 (6, 7, 'אמחה את האדם'), (6, 8, 'מצא חן'), (6, 13, 'קץ כל בשר'), (6, 15, 'שלש מאות אמה'), (6, 16, 'תחתים שנים ושלשים'), (6, 18, 'והקמתי את בריתי אתך'), (6, 18, 'אתה ובניך ואשתך'),
 (7, 2, 'שבעה שבעה איש ואשתו'), (7, 4, 'לימים עוד שבעה'), (7, 4, 'ארבעים יום וארבעים לילה'), (7, 6, 'שש מאות שנה'), (7, 11, 'נבקעו כל מעינת תהום רבה'), (7, 16, 'ויסגר יהוה בעדו'),
 (7, 22, 'מכל אשר בחרבה מתו'), (7, 23, 'וישאר אך נח'), (7, 24, 'חמשים ומאת יום'), (8, 1, 'ויזכר אלהים את נח'), (8, 4, 'בחדש השביעי בשבעה עשר יום'), (8, 6, 'מקץ ארבעים יום'),
 (8, 9, 'מנוח'), (8, 10, 'שבעת ימים אחרים'), (8, 11, 'עלה זית טרף בפיה'), (8, 13, 'באחת ושש מאות שנה'), (8, 14, 'בשבעה ועשרים יום'), (8, 16, 'אתה ואשתך'), (8, 20, 'ויעל עלת במזבח'),
 (8, 21, 'ריח הניחח'), (8, 22, 'לא ישבתו'), (9, 20, 'ויטע כרם'), (9, 21, 'ויתגל'), (9, 24, 'בנו הקטן'), (9, 25, 'עבד עבדים'), (9, 27, 'יפת אלהים ליפת'), (10, 8, 'החל להיות גבר'),
 (10, 10, 'ראשית ממלכתו'), (10, 25, 'בימיו נפלגה הארץ'), (11, 1, 'שפה אחת'), (11, 4, 'ונעשה לנו שם'), (11, 5, 'וירד יהוה לראת'), (11, 7, 'הבה נרדה'), (11, 8, 'ויפץ יהוה אתם משם'),
 (11, 9, 'ומשם הפיצם יהוה'), (11, 10, 'שנתים אחר המבול'), (11, 26, 'שבעים שנה'), (11, 28, 'על פני תרח אביו'), (11, 29, 'יסכה'), (11, 30, 'עקרה'), (11, 32, 'חמש שנים ומאתים שנה'),
 (12, 1, 'לך לך'), (12, 2, 'לגוי גדול'), (12, 4, 'חמש שנים ושבעים שנה'), (12, 7, 'לזרעך אתן את הארץ הזאת'), (12, 8, 'ויקרא בשם יהוה'), (12, 13, 'אחתי את'), (12, 15, 'ותקח האשה'),
 (12, 17, 'נגעים גדלים'), (12, 20, 'וישלחו אתו'), (13, 2, 'כבד מאד'), (13, 7, 'ויהי ריב'), (13, 11, 'ויפרדו'), (13, 13, 'רעים וחטאים'), (13, 15, 'ולזרעך עד עולם'), (13, 16, 'כעפר הארץ'),
 (13, 17, 'קום התהלך בארץ'), (14, 4, 'שתים עשרה שנה'), (14, 4, 'ושלש עשרה שנה מרדו'), (14, 5, 'ובארבע עשרה שנה'), (14, 13, 'לאברם העברי'), (14, 14, 'שמנה עשר ושלש מאות'),
 (14, 15, 'ויחלק עליהם לילה'), (14, 18, 'כהן לאל עליון'), (14, 20, 'מעשר מכל'), (14, 22, 'הרימתי ידי'), (15, 1, 'אנכי מגן לך'), (15, 2, 'הולך ערירי'), (15, 4, 'לא יירשך זה'),
 (15, 5, 'וספר הכוכבים'), (15, 6, 'והאמן ביהוה'), (15, 7, 'הוצאתיך מאור כשדים'), (15, 9, 'עגלה משלשת'), (15, 10, 'ואת הצפר לא בתר'), (15, 12, 'ותרדמה נפלה על אברם'),
 (15, 13, 'ארבע מאות שנה'), (15, 14, 'ברכש גדול'), (15, 16, 'ודור רביעי'), (15, 17, 'בין הגזרים'), (15, 18, 'לזרעך נתתי'), (16, 3, 'מקץ עשר שנים'), (16, 3, 'לו לאשה'),
 (16, 4, 'ותקל גברתה'), (16, 5, 'ישפט יהוה ביני וביניך'), (16, 6, 'ותענה שרי ותברח'), (16, 9, 'שובי אל גברתך'), (16, 11, 'וקראת שמו ישמעאל'), (16, 12, 'פרא אדם'), (16, 13, 'אל ראי'),
 (16, 16, 'שמנים שנה ושש שנים'),
]
_T = {}
for ch, vs, run in PROBES:
    ws = _T.setdefault((ch, vs), toks(ch, vs)); want = run.split()
    assert any(ws[i:i + len(want)] == want for i in range(len(ws) - len(want) + 1)), 'PROBE FAILED: %r not in Gen %d:%d' % (run, ch, vs)
print('probes: %d ink runs verified in their verses (Gen 2-16)' % len(PROBES))

I, M, A, D, P, H = 'INK', 'MOVE', 'ANSWER-SHEET', 'DATA', 'IMPORT', 'HYPOTHESIS'


def cell(v, p, why, effects):
    FX.validate(effects)
    return {'v': v, 'p': p, 'why': why, 'fx': effects}


with contextlib.redirect_stdout(io.StringIO()), contextlib.redirect_stderr(io.StringIO()):   # the callees grade themselves at import — their reports stay their own
    import cold_run_pre_sinai as PS_   # THE LIVE EDGES (dependency_dispositions.yaml): the first rule (3:6 against 2:16-17), the blessing (8:17), the covenant (6:18, 15:18), the bloods (4:10 against 9:6)
    import cold_run_offerings as OF    # the burnt offering (8:20); the fat of the firstlings (4:4)
    import cold_run_minchah as MI      # Cain's minchah (4:3); the turtledove and the pigeon (15:9)
    import cold_run_temurah as TM      # the firstling's seat (4:4 — Lev 27:26); the tithe (14:20 — Lev 27:30)
    import cold_run_shemini as SH      # the clean beasts (7:2, 8:20)
    import cold_run_family as FA       # the marriage formula (4:19, 6:2, 11:29, 16:3); the heir (15:3-4); the three modes (13:17)
    import cold_run_priesthood as PR   # the priest (14:18)
    import cold_run_sanctions as SAN   # 'childless' (15:2 — Lev 20:20-21)
import world_engine as WE


# ---- the ink censuses the cells read (recomputed here; every count a measurement) ----
def _seats(pred, ch_lo, ch_hi):
    out = []
    for ch in range(ch_lo, ch_hi + 1):
        n = con.execute("select count(*) from verses where book='Gen' and chapter=?", (ch,)).fetchone()[0]
        for vs in range(1, n + 1):
            if (ch == 2 and vs < 4) or (ch == 16 and vs > 16): continue
            if pred(_T.setdefault((ch, vs), toks(ch, vs))): out.append((ch, vs))
    return out


c_named = _seats(lambda ws: any(ws[i] in ('ויקרא', 'ותקרא', 'ויקראו', 'קרא', 'יקרא') and any(x in ('שם', 'שמו', 'שמה', 'שמם', 'שמות') for x in ws[i + 1:i + 5]) for i in range(len(ws))), 2, 16)
c_cursed = _seats(lambda ws: any(w in ('ארור', 'ארורה') for w in ws), 2, 16)
c_begot = _seats(lambda ws: 'ויולד' in ws, 5, 11)
c_bore = _seats(lambda ws: 'ותלד' in ws, 2, 16)
c_died = _seats(lambda ws: 'וימת' in ws, 2, 16)
c_altar = _seats(lambda ws: 'מזבח' in ws and any(w in ('ויבן',) for w in ws), 2, 16)
c_covenant = _seats(lambda ws: any(w in ('בריתי', 'ברית') for w in ws), 2, 16)
c_ten_generations = (['adam', 'seth', 'enosh', 'kenan', 'mahalalel', 'jared', 'enoch', 'methuselah', 'lamech', 'noah'], ['shem', 'arpachshad', 'shelah', 'eber', 'peleg', 'reu', 'serug', 'nahor', 'terah', 'abram'])


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
    ('sanhedrin', 10, 3, 'דור המבול'), ('sanhedrin', 10, 3, 'דור הפלגה'), ('sanhedrin', 10, 3, 'אנשי סדום'), ('sanhedrin', 4, 5, 'דמי אחיך'), ('pirkei_avot', 5, 2, 'עשרה דורות'),
    ('pirkei_avot', 5, 3, 'עשרה נסיונות'), ('eduyot', 2, 10, 'דור המבול'), ('yevamot', 6, 6, 'עשר שנים'), ('yevamot', 6, 6, 'זכר ונקבה בראם'), ('megillah', 1, 8, 'יונית'),
]
for t, ch, m, must in SHEET: mishnah(t, ch, m, must)
SHEET2 = [   # the Babylonian rows (file index 2*daf-2, +1 for b — every file checked to carry its 1a/1b) and the Genesis spine's rows (Bereshit Rabbah, parashah:row)
    ('B', 'sanhedrin', 107, 'b', 18, 'דור המבול'), ('B', 'sanhedrin', 108, 'a', 5, 'וימח את כל היקום'), ('B', 'sanhedrin', 108, 'a', 9, 'גלגל העין'), ('B', 'sanhedrin', 108, 'a', 10, 'ברבה קלקלו'),
    ('B', 'sanhedrin', 108, 'a', 11, 'שהרביעו'), ('B', 'sanhedrin', 108, 'a', 12, 'בגזל'), ('B', 'sanhedrin', 108, 'a', 14, 'ונח מצא חן'), ('B', 'sanhedrin', 108, 'a', 15, 'קברות'),
    ('B', 'sanhedrin', 108, 'a', 20, 'חופה לבנו'), ('B', 'sanhedrin', 108, 'a', 21, 'ולא דגים שבים'), ('B', 'sanhedrin', 108, 'b', 3, 'ברותחין'), ('B', 'sanhedrin', 108, 'b', 5, 'אבילות של מתושלח'),
    ('B', 'sanhedrin', 108, 'b', 7, 'שהעבירן לפני התיבה'), ('B', 'sanhedrin', 108, 'b', 11, 'תחתיים לזבל'), ('B', 'sanhedrin', 108, 'b', 12, 'תשובה ניצחת'), ('B', 'sanhedrin', 108, 'b', 14, 'שנאסרו בתשמיש המטה'),
    ('B', 'sanhedrin', 108, 'b', 15, 'כלב ועורב וחם'), ('B', 'sanhedrin', 108, 'b', 17, 'עלה זית'), ('B', 'sanhedrin', 109, 'a', 5, 'נחלקו'), ('B', 'sanhedrin', 109, 'a', 6, 'לשם עבודת כוכבים'),
    ('B', 'sanhedrin', 109, 'a', 7, 'שליש נשרף'), ('B', 'sanhedrin', 109, 'a', 9, 'רעים בגופן'), ('B', 'sanhedrin', 37, 'b', 10, 'חבורות חבורות'), ('B', 'sanhedrin', 37, 'b', 11, 'שפתחה הארץ'),
    ('B', 'sanhedrin', 37, 'b', 12, 'גלות מכפרת'), ('B', 'sanhedrin', 70, 'a', 18, 'סרסו'), ('B', 'sanhedrin', 70, 'a', 19, 'ברביעי'), ('B', 'sanhedrin', 70, 'a', 22, 'גפן היה'),
    ('B', 'nedarim', 32, 'a', 9, 'אין מזל לישראל'), ('B', 'nedarim', 32, 'a', 14, 'אנגרייא'), ('B', 'nedarim', 32, 'a', 15, 'תן לי הנפש'), ('B', 'nedarim', 32, 'a', 16, 'בזהב'),
    ('B', 'nedarim', 32, 'a', 17, 'אליעזר כנגד כולם'), ('B', 'nedarim', 32, 'b', 6, 'כהונה משם'), ('B', 'sotah', 14, 'a', 4, 'כתנות עור'), ('B', 'sotah', 14, 'a', 6, 'גמילות חסדים'),
    ('B', 'megillah', 9, 'b', 4, 'יפת אלהים ליפת'), ('B', 'megillah', 9, 'b', 5, 'יפיותו של יפת'), ('B', 'megillah', 14, 'a', 13, 'יסכה זו שרה'), ('B', 'berakhot', 40, 'a', 14, 'גפן היה'),
    ('B', 'kiddushin', 30, 'b', 5, 'ואתה תמשל בו'), ('B', 'bava_batra', 100, 'a', 7, 'קום התהלך'), ('B', 'yevamot', 64, 'a', 5, 'מקץ עשר שנים'), ('B', 'chullin', 89, 'a', 7, 'לנמרוד'),
    ('B', 'eruvin', 53, 'a', 7, 'נמרוד שמו'), ('B', 'pesachim', 118, 'a', 20, 'כבשן האש'), ('B', 'rosh_hashanah', 11, 'b', 6, 'באייר'), ('B', 'rosh_hashanah', 11, 'b', 7, 'במרחשון'),
    ('B', 'shabbat', 55, 'b', 3, 'בעטיו של נחש'), ('B', 'pesachim', 6, 'b', 7, 'מוקדם ומאוחר'),
    ('R', 16, 5, 'עלה אותו'), ('R', 17, 3, 'אם זכה עזר'), ('R', 17, 5, 'שלש תרדמות'), ('R', 19, 5, 'שלשה דברים'), ('R', 19, 8, 'אלף שנים'), ('R', 20, 4, 'שבעים ואחד'), ('R', 20, 7, 'ארבע תשוקות'),
    ('R', 20, 9, 'קשה היא הפרנסה'), ('R', 20, 12, 'כתנות אור'), ('R', 21, 7, 'שלחו מגן עדן'), ('R', 21, 8, 'כבת כהן'), ('R', 22, 4, 'חמשים יום'), ('R', 22, 5, 'מן הפסולת'), ('R', 22, 11, 'גדול עוני'),
    ('R', 22, 12, 'נתכנסו'), ('R', 23, 2, 'ויקח לו למך'), ('R', 23, 4, 'למחר המבול'), ('R', 23, 7, 'לשון מרד'), ('R', 25, 1, 'חנף'), ('R', 25, 2, 'לא המדרש הוא השם'), ('R', 25, 3, 'עשרה שני רעבון'),
    ('R', 26, 5, 'בני דיניא'), ('R', 27, 4, 'תוהות'), ('R', 28, 9, 'שנים עשר חדש'), ('R', 29, 1, 'ונח מצא חן'), ('R', 30, 7, 'מאה ועשרים שנה'), ('R', 31, 5, 'חמס אינו שוה פרוטה'), ('R', 32, 5, 'לארבעים יום'),
    ('R', 32, 7, 'אבלות של מתושלח'), ('R', 33, 7, 'אחד עשר יום'), ('R', 34, 7, 'נאסרה לו'), ('R', 34, 9, 'מזבח הגדול'), ('R', 34, 11, 'בריתן קימת'), ('R', 36, 3, 'נתחלל'), ('R', 36, 4, 'בו ביום נטע'),
    ('R', 36, 6, 'זכה שם לטלית'), ('R', 36, 7, 'חם חטא וכנען נתקלל'), ('R', 36, 8, 'זה כרש'), ('R', 37, 4, 'ננערו'), ('R', 37, 7, 'נביא גדול היה עבר'), ('R', 38, 6, 'דברים חדים'), ('R', 38, 8, 'מצרים אמר לכוש'),
    ('R', 38, 9, 'מעשר ירידות'), ('R', 38, 10, 'הבה ארדה'), ('R', 38, 13, 'עובד צלמים'), ('R', 38, 14, 'גדול מנחור'), ('R', 39, 7, 'ששים וחמש'), ('R', 39, 11, 'ואעשך'), ('R', 39, 16, 'שלשה מזבחות'),
    ('R', 40, 5, 'נתנה בתבה'), ('R', 40, 6, 'צא וכבש את הדרך'), ('R', 41, 2, 'בראתן'), ('R', 41, 5, 'זמומה'), ('R', 41, 7, 'לשון ערוה'), ('R', 41, 10, 'הלוך קנה'), ('R', 42, 6, 'עשרים וחמשה'),
    ('R', 42, 8, 'הוא עוג'), ('R', 43, 3, 'הלילה נחלק'), ('R', 43, 6, 'צדק נקראת ירושלים'), ('R', 43, 9, 'עשאן תרומה'), ('R', 44, 4, 'תרתין'), ('R', 44, 12, 'שוקקי שמיא'), ('R', 44, 13, 'מיכאל ירד'),
    ('R', 44, 14, 'שלשה מיני פרים'), ('R', 44, 15, 'זו בבל'), ('R', 44, 16, 'פגרים'), ('R', 44, 17, 'שלשה תרדמות'), ('R', 44, 18, 'משיראה לך זרע'), ('R', 44, 19, 'ארבעה גליות'), ('R', 44, 20, 'עשר מכות'),
    ('R', 44, 21, 'ארבעה דברים הראה לו'), ('R', 44, 22, 'העולם הבא'), ('R', 44, 23, 'עשרה עממים'), ('R', 45, 3, 'עשר שנים'), ('R', 45, 4, 'מביאה ראשונה'), ('R', 45, 5, 'חומסני'), ('R', 45, 6, 'לא תתעמר'),
    ('R', 45, 8, 'שלשה הן'), ('R', 45, 9, 'פרא אדם'), ('R', 45, 10, 'להשיח עם האשה'),
]
for row in SHEET2:
    if row[0] == 'B': _bavli(*row[1:])
    else: _br(*row[1:])
print('answer sheet: %d Mishnah rows and %d shelf rows verified by their own tokens (Sanhedrin 10:3, 4:5, Avot 5:2-3, Eduyot 2:10, Yevamot 6:6, Megillah 1:8; Sanhedrin 107b-109b, 37b, 70a, Nedarim 32a-b, Sotah 14a, Megillah 9b, 14a, Berakhot 40a, Kiddushin 30b, Bava Batra 100a, Yevamot 64a, Chullin 89a, Eruvin 53a, Pesachim 118a, 6b, Rosh Hashanah 11b, Shabbat 55b; Bereshit Rabbah 16-45)' % (len(SHEET), len(SHEET2)))


# =====================================================================
# THE CELLS — the ink first; the shelf's rows as MOVE lines; the institutions named fetched by call
# =====================================================================
def garden(q):
    if q == 'living_soul': return cell(1, I, "'and the man became a LIVING SOUL' (2:7) — the phrase as the man's predicate at 2:7 alone in Genesis (measured); Bereshit Rabbah 14:9 the five soul-names (the frozen unit's read)", ['living_soul'])
    if q == 'office': return cell(('work', 'keep'), I, "'to work it and to keep it' (2:15) — the pair's only seat in the Tanakh (measured): the first office; split at the exile (3:23 'to work the ground'; 3:24 the cherubim 'to keep the way')", ['to_work_and_keep'])
    if q == 'took': return cell(('elevated', 'persuaded'), M, "Bereshit Rabbah 16:5 — 'and the LORD God TOOK the man' (2:15): R. Yehuda — He elevated him (Isa 14:2 'and peoples shall take them'); R. Nechemya — He persuaded him (Hos 14:3 'take words with you')", ['to_work_and_keep'])
    if q == 'helper': return cell(('a_help', 'against_him'), M, "Bereshit Rabbah 17:3 — 'a help matching him' (2:18): if he merits, a help; if not, against him", ['helper_made'])
    if q == 'couple_sheet': return cell(('two_males', 'male_and_female'), A, "Mishnah Yevamot 6:6 — Beit Shammai: two males; Beit Hillel: a male and a female, 'as it is said: male and female He created them' (5:2) — the couple's row on the ledger's head", ['helper_made'])
    if q == 'deep_sleeps': return cell(('sleep', 'prophecy', 'stupor'), M, "Bereshit Rabbah 17:5 and 44:17 — the SAME three at both seats of the stretch: the deep sleep of sleep ('and the LORD God caused a deep sleep to fall on the man', 2:21), of prophecy ('a deep sleep fell on Abram', 15:12), of stupor (1 Sam 26:12) — the noun tardemah at 2:21 and 15:12 (the type's two seats)", ['deep_sleep_fell'])
    if q == 'names_count': return cell(len(c_named), I, "the naming clauses of Genesis 2:4-16:16 (a call-verb with 'name' within four words): %r — fourteen seats: the beasts (2:20), Woman (2:23), Eve (3:20), the city (4:17), Seth (4:25 by Eve; 5:3 by Adam), Enosh (4:26), Adam (5:2), Noah (5:29), Babel (11:9), El Roi (16:13), the well (16:14), Ishmael (16:15)" % (c_named,), ['name_given'])
    return cell('no_case', I, '', [FX.NONE])


def breach(q):
    if q == 'first_rule_by_call': return cell(PS_.noahide('root_tokens')['v'][:6], P, "CALLED cold_run_pre_sinai.noahide('root_tokens') -> 2:16's tokens, the FIRST COMMAND [IMPORT, live]: the breach of 3:6 is an act against that engine's rule, cited back at 3:11 and 3:17 'the tree of which I COMMANDED you' (a RUN_CITATION into its span)", ['breached_the_first_rule'])
    if q == 'four_verbs': return cell(4, I, "'and she TOOK of its fruit and ATE, and GAVE also to her husband with her, and he ATE' (3:6) — the four verbs of the breach, the trigger chain (the frozen unit's export)", ['breached_the_first_rule'])
    if q == 'tree_identity': return cell(('vine', 'wheat', 'fig'), M, "Berakhot 40a:14 — the tree of which the first man ate: R. Meir — a vine (nothing brings wailing on man like wine, 9:21); R. Yehuda — wheat (a child does not know to call father and mother until it tastes grain); R. Nechemya — a fig (with the thing they were corrupted they were mended, 3:7); Sanhedrin 70a:21-22 (Rav Chisda to Noah: learn from the first man whom wine alone undid — as R. Meir)", ['breached_the_first_rule'])
    if q == 'three_things': return cell(3, M, "Bereshit Rabbah 19:5 — R. Yose bar Zimra: three things were said of that tree — good for food, a delight to the eyes, adds wisdom — all three in one verse (3:6)", ['breached_the_first_rule'])
    if q == 'eyes': return cell('were_they_blind', M, "Bereshit Rabbah 19:6 — 'and the eyes of both of them were opened' (3:7): were they blind? R. Yudan in R. Yochanan ben Zakkai's name — the villager before the glassmaker's shop", ['eyes_opened'])
    if q == 'deceived_seat': return cell(1, I, "'the serpent DECEIVED me and I ate' (3:13) — the verb's only seat in the Tanakh (measured): the woman's own admission, the ledger's word", ['deceived'])
    if q == 'no_sub_day': return cell('recorded_not_run', D, "the day's hours (the sixth day: created, sinned, judged, banished — the tradition's hour-table) are SUB-DAY: OUT by the clock consensus (round two, 2026-09-07) — recorded as a remark, no timer; the breach sits at the counter", [FX.NONE])
    return cell('no_case', I, '', [FX.NONE])


def sentences(q):
    if q == 'curse_seats': return cell(c_cursed, I, "'cursed' (ארור / ארורה) in the stretch: %r — the serpent (3:14), the ground (3:17), Cain (4:11), Canaan (9:25): the corpus's four curses, the serpent's and the ground's first, the man never cursed (the frozen unit's export)" % (c_cursed,), ['serpent_cursed', 'ground_cursed', 'cursed_from_the_ground', 'canaan_cursed'])
    if q == 'seventy_one': return cell(71, M, "Bereshit Rabbah 20:4 — R. Yehuda bar Simon in R. Hoshaya's name: from the book's beginning to here (3:14) SEVENTY-ONE mentions of the Name — it tells that the serpent was judged by a full Sanhedrin (Mishnah Sanhedrin 1:6's seventy-one)", ['serpent_cursed'])
    if q == 'four_desires': return cell(4, M, "Bereshit Rabbah 20:7 — 'and to your husband shall be your desire' (3:16): four desires — the woman's for her husband, the inclination's for Cain and his fellows (4:7 'to you is its desire'), the rains' for the earth, the Holy One's for Israel", ['ruled_by_the_husband'])
    if q == 'livelihood': return cell('harder_than_birth', M, "Bereshit Rabbah 20:9 — Rav Asi: livelihood is harder than childbirth, twice over — of birth 'in PAIN you shall bear' (3:16), of livelihood 'in TOIL you shall eat' (3:17)", ['ground_cursed', 'sweat_bread'])
    if q == 'thousand_year_day': return cell((1000, 930, 70), M, "Bereshit Rabbah 19:8 — 'in the day you eat of it you shall surely die' (2:17): I give him one day of MINE, which is a thousand years — he lived nine hundred and thirty and left seventy to his sons (Ps 90:10): the mortality entry OPEN on the tape, Adam's total the proleptic marker (the sequence runner CG9)", ['return_to_dust'])
    if q == 'serpent_counsel': return cell(4, M, "Shabbat 55b:3-4 — four died by the serpent's counsel alone (no sin of their own): Benjamin son of Jacob, Amram father of Moses, Jesse father of David, Chileab son of David — the mortality decree's reach", ['return_to_dust'])
    if q == 'garments_kindness': return cell('begins_and_ends_with_kindness', M, "Sotah 14a:4-6 — 'and the LORD God made for the man and for his wife garments of skin and clothed them' (3:21): walk after His attributes — He clothes the naked, so you clothe the naked; R. Simlai: the Torah begins with an act of kindness and ends with one (Moses buried, Deut 34:6); Rav and Shmuel on 'skin': a thing that comes from the skin / a thing the skin enjoys", ['clothed_in_skins'])
    if q == 'garments_of_light': return cell('kutnot_or_with_an_aleph', M, "Bereshit Rabbah 20:12 — in R. Meir's Torah they found written 'garments of LIGHT' (with an aleph): the first man's garments, like a lamp, wide below and narrow above", ['clothed_in_skins'])
    if q == 'expelled_two_worlds': return cell(('this_world_and_the_next', 'this_world_only'), M, "Bereshit Rabbah 21:7 — 'and He sent him out of the garden of Eden' (3:23): R. Yehuda — sent from Eden in this world and from Eden in the world to come; R. Nechemya — in this world, not the world to come", ['expelled'])
    if q == 'divorced_daughter': return cell(('priests_daughter_cannot_return', 'israelites_daughter_can'), M, "Bereshit Rabbah 21:8 — 'and He DROVE OUT the man' (3:24): R. Yochanan — like a priest's daughter divorced, who cannot return; Reish Lakish — like an Israelite's daughter divorced, who can return", ['expelled'])
    if q == 'east_receives': return cell(('adam', 'cain', 'the_manslayer'), M, "Bereshit Rabbah 21:9 — 'at the EAST of the garden' (3:24): Rav — everywhere the east wind receives: the first man (3:24), Cain (4:16 'east of Eden'), the manslayer (Deut 4:41 'toward the sunrise') — the refuge's direction", ['way_guarded', 'settled_in_nod'])
    return cell('no_case', I, '', [FX.NONE])


def cain(q):
    if q == 'minchah_by_call': return cell(MI.odor_classes()['v'], P, "CALLED cold_run_minchah.odor_classes() -> the three classes of 'a fire-offering of pleasing odor' in Lev 1-2 [IMPORT, live]: 'Cain brought of the fruit of the ground a MINCHAH to the LORD' (4:3) names the meal-offering engine's institution before its law (a REFERENCE); 8:21's 'pleasing savor' the same engine's phrase at Noah's altar", ['not_regarded'])
    if q == 'firstling_by_call': return cell(TM.consecrate('firstborn')['v'], P, "CALLED cold_run_temurah.consecrate('firstborn') -> the firstling's own status, Lev 27:26 'no man shall sanctify it, it IS the LORD's' [IMPORT, live]: 'Abel brought of the FIRSTLINGS of his flock' (4:4) — the institution by name (a REFERENCE)", ['regarded'])
    if q == 'fat_by_call': return cell(sorted(OF.fat_inventory('lamb').keys())[:2], P, "CALLED cold_run_offerings.fat_inventory('lamb') -> the lamb's fat parts [IMPORT, live]: 'and of their FAT' (4:4) — the pointer names the species (the flock's firstlings): the offering engine's fat inventory at its first narrative seat", ['regarded'])
    if q == 'regard_seats': return cell([(4, 4)], I, "'and the LORD REGARDED Abel and his offering' (4:4) — the regard verb's only seat in the Torah (measured; Judg 3:31, 1 Sam 23:5, 2 Sam 8:6, Job 5:15, Prov 20:22 elsewhere); 4:5 'but to Cain and his offering He did not regard'", ['regarded', 'not_regarded'])
    if q == 'refuse': return cell(('from_the_refuse', 'the_firstlings'), M, "Bereshit Rabbah 22:5 — Cain's 'of the fruit of the ground': from the refuse (the bad tenant who eats the firstfruits and honors the owner with the last); Abel's 'of the firstlings of his flock and of their fat' — R. Elazar: the first minchah", ['not_regarded', 'regarded'])
    if q == 'abel_days': return cell(WE.CAL_PARAMS['abel_days_bound']['value'], D, "the row abel_days_bound — Bereshit Rabbah 22:4: 'at the end of days' (4:3): R. Eliezer (the world created in Tishrei — from the festival to Chanukah) and R. Yehoshua (in Nisan — from Passover to Shavuot); by both, Abel was not in the world more than FIFTY days — recorded as a remark (the stretch carries no stamp)", [FX.NONE])
    if q == 'first_if': return cell('rule_over_it', M, "Kiddushin 30b:5 — 'sin couches at the door ... and to you is its desire, but you shall RULE over it' (4:7): if you wish, you rule over it — the corpus's first IF (the frozen unit's export), the inclination's desire from 3:16's pair", ['sin_at_the_door'])
    if q == 'wounds': return cell('wounds_upon_wounds', M, "Sanhedrin 37b:10 — Rav Yehuda son of R. Chiya: Cain made in Abel his brother wounds upon wounds, bruises upon bruises, for he did not know from where the soul goes out — until he reached his neck", ['slain'])
    if q == 'bloods_sheet': return cell('his_blood_and_the_blood_of_his_descendants', A, "Mishnah Sanhedrin 4:5 — 'the voice of your brother's BLOODS cries' (4:10): it does not say 'blood' but 'bloods' — his blood and the blood of his descendants; another reading: his blood was cast on the trees and the stones; therefore man was created alone — whoever destroys one soul destroys a whole world", ['bloods_cry'])
    if q == 'bloods_seats': return cell([(4, 10), (4, 11)], I, "'your brother's bloods' (דמי אחיך) at 4:10 and 4:11 alone in the Tanakh (measured) — the plural at both seats", ['bloods_cry'])
    if q == 'earth_mouth': return cell('opened_once_for_abel', M, "Sanhedrin 37b:11 — from the day the earth opened its mouth and received Abel's blood it never opened again (Isa 24:16 'from the wing of the earth' — not from its mouth); Korach's (Num 16:32) — for evil it opened, for good it did not", ['bloods_cry'])
    if q == 'exile_half': return cell(('fugitive_and_wanderer', 'dwelt_in_nod'), M, "Sanhedrin 37b:12 — Rav Yehuda son of R. Chiya: EXILE atones half — at first 'a fugitive and a wanderer' (4:14), at the end 'he dwelt in the land of Nod' (4:16); the pair at 4:12 and 4:14 alone in the Tanakh (measured)", ['fugitive_and_wanderer', 'settled_in_nod'])
    if q == 'greater_than_father': return cell('a_light_command_vs_bloodshed', M, "Bereshit Rabbah 22:11 — 'my iniquity is greater than can be borne' (4:13): greater than my father's — father transgressed a light command and was banished from the garden; this one, bloodshed, all the more", ['cursed_from_the_ground'])
    if q == 'mark_arms': return cell(('a_dog', 'a_horn', 'leprosy'), M, "Bereshit Rabbah 22:12 — 'and the LORD set a mark for Cain' (4:15): a dog He gave him; a horn He grew on him; leprosy — the arms; R. Yehuda: the beasts gathered to claim Abel's blood — 'therefore whoever slays Cain'", ['mark_set'])
    if q == 'sevenfold_seats': return cell([(4, 15), (4, 24)], I, "'sevenfold' (שבעתים) at 4:15 and 4:24 in Genesis (measured) — the LORD's handler and Lamech's quotation with the number changed: seventy and sevenfold (4:24)", ['sevenfold_vengeance', 'seventy_sevenfold_claimed'])
    if q == 'lamech_wives': return cell('refused_tomorrow_the_flood', M, "Bereshit Rabbah 23:4 — 'Adah and Zillah, hear my voice' (4:23): R. Yose bar Chanina — he demanded marital relations; they said: tomorrow the flood comes, shall we bear for a curse? 'for I have killed a man for my wound' — that wounds come on me for him", ['seventy_sevenfold_claimed'])
    if q == 'two_wives': return cell(('for_offspring', 'for_pleasure'), M, "Bereshit Rabbah 23:2 — 'and Lamech took him two wives' (4:19): the generation of the flood did so — one for offspring, one for pleasure; the marriage formula's institution (the family engine by call)", ['wife_taken'])
    if q == 'rebellion_three': return cell(3, M, "Bereshit Rabbah 23:7 — R. Simon: at three places the beginning verb is a language of REBELLION — 'then it was begun to call on the name' (4:26), 'when man began to multiply' (6:1), 'he began to be a mighty one' (10:8)", ['idolatry_begun', 'multiplied_on_the_earth', 'kingdom_founded'])
    if q == 'city_seat': return cell(1, I, "'and he was building a city, and called the city's name after his son's name, Enoch' (4:17) — the corpus's first human build (the frozen unit's export); Bereshit Rabbah 23:1 (they called lands by their names)", ['city_built'])
    return cell('no_case', I, '', [FX.NONE])


def lines(q):
    if q == 'begot_seats': return cell(len(c_begot), I, "'and he begot' (ויולד) at %d seats of Genesis 5-11 (measured): the ledger's refrain — Gen 5's rows (5:3-32) and Shem's (11:10-26) with the after-begetting rows" % len(c_begot), ['begotten'])
    if q == 'bore_seats': return cell(len(c_bore), I, "'and she bore' (ותלד) at %d seats of Genesis 2-16 (measured): Cain, Abel, Enoch, Jabal, Seth, Ishmael the story's births — the mother's verb before the covenant (the eighth-day timer is the pre-Sinai daemon's run from 17:12)" % len(c_bore), ['begotten'])
    if q == 'died_seats': return cell(len(c_died), I, "'and he died' (וימת) at %d seats of Genesis 2-16 (measured): the eight closing totals of Gen 5, Noah's (9:29), Haran's (11:28), Terah's (11:32) — the totals are PROLEPTIC markers on the tape (SEQUENTIAL_RUN.md section 2), no event; Haran's death alone is narrated in sequence (the type `died` at 11:28)" % len(c_died), ['died_before_his_father'])
    if q == 'ten_generations': return cell((len(c_ten_generations[0]), len(c_ten_generations[1])), A, "Mishnah Avot 5:2 — ten generations from Adam to Noah, ten from Noah to Abraham: %r and %r — counted on the tape's own life eras (the sequence runner CG0)" % c_ten_generations, ['begotten'])
    if q == 'enoch_taken': return cell('hypocrite_taken_while_righteous', M, "Bereshit Rabbah 25:1 — 'and he was not, for God took him' (5:24): R. Aivu — Enoch was a hypocrite, sometimes righteous, sometimes wicked; the Holy One said: while he is righteous I will take him; 'and he was not' at 5:24 alone in Genesis (measured)", ['taken_by_god'])
    if q == 'noah_name': return cell('the_name_is_not_the_exposition', M, "Bereshit Rabbah 25:2 — 'and he called his name Noah, saying: this one shall COMFORT us' (5:29): R. Yochanan — the exposition is not the name and the name is not the exposition (Noah — 'shall give us rest'; Nachman — 'shall comfort'); Reish Lakish: the name is the exposition", ['name_given'])
    if q == 'ten_famines': return cell(('adam', 'lamech', 'abraham'), M, "Bereshit Rabbah 25:3 and 40:3 — TEN famines came to the world: one in the first man's days ('cursed is the ground', 3:17), one in Lamech's ('from the ground which the LORD cursed', 5:29), one in Abraham's ('there was a famine in the land', 12:10) — the stretch's three; the ledger's famine entry the third alone (the first two are the curses)", ['famine'])
    if q == 'two_lines_names': return cell(('enoch', 'lamech'), I, "two men named Enoch (4:17 Cain's son; 5:18 Jared's) and two named Lamech (4:18 Methushael's son; 5:25 Methuselah's) — the lines share names at the lemma level (the frozen unit's export); the registry keeps them apart", ['begotten'])
    if q == 'seth_twice': return cell(2, I, "Seth's birth stated twice — 'and she bore a son and called his name Seth' (4:25, the mother's verb) and 'and he begot in his likeness after his image and called his name Seth' (5:3, the father's): two acts, two namings, two parents — the ledger carries both", ['begotten', 'name_given'])
    return cell('no_case', I, '', [FX.NONE])


def prologue(q):
    if q == 'sons_of_god': return cell('sons_of_the_judges', M, "Bereshit Rabbah 26:5 — 'and the sons of God saw' (6:2): R. Shimon ben Yochai called them the sons of the JUDGES and cursed whoever calls them sons of gods; 'from all they chose' — the marriage formula's institution by call; the registry holds the collective UNCERTAIN", ['wife_taken'])
    if q == 'reading_row': return cell(WE.CAL_PARAMS['gen6_3_reading']['value'], D, "the row gen6_3_reading — 'and his days shall be a hundred and twenty years' (6:3): the REPRIEVE before the flood (the running setting; Bereshit Rabbah 30:7: all hundred and twenty years Noah planted cedars and cut them; Onkelos: an extension is given them, if they repent) against the lifespan reading (recorded, UNEXERCISED)", ['reprieve_of_a_hundred_and_twenty'])
    if q == 'reprieve_number': return cell(120, I, "'a hundred and twenty years' (6:3) — the number parsed from the ink, the only seat of the number in Genesis (measured; Deut 31:2, 34:7 Moses' — book-bound); the timer's due the speaking + 120 years", ['reprieve_of_a_hundred_and_twenty'])
    if q == 'retrograde': return cell((600, 120, 480, 500), M, "THE RETROGRADE DATING of 6:3 on the tape: the flood in Noah's 600th year (7:6, 7:11) minus 120 = Noah's 480 — BEFORE 5:32's five hundred (the sons' begetting) where the tape's counter stands: Pesachim 6b:7 ('there is no earlier and later in the Torah' — the tape's standing principle at Lev 8:2 and Num 9:1); the teacher for the placement Bereshit Rabbah 30:7 (the 120 years ran before the flood); the timer fires on the flood's own day (the sequence runner CG2)", ['reprieve_of_a_hundred_and_twenty'])
    if q == 'wickedness_great': return cell('with_great_they_sinned_with_great_judged', M, "Sanhedrin 108a:10 — R. Yochanan: the generation of the flood sinned with 'GREAT' ('the wickedness of man was great', 6:5) and were judged with 'great' ('the fountains of the GREAT deep', 7:11)", ['wickedness_great', 'fountains_split'])
    if q == 'regret_two': return cell(('well_did_i_prepare_graves', 'not_well'), M, "Sanhedrin 108a:15-16 — 'and the LORD regretted that He had made man on the earth' (6:6): Rav Dimi — the Holy One said: well did I do that I prepared graves for them in the earth (50:21's comfort); others: not well (Exod 32:14's regret); Bereshit Rabbah 27:4 (R. Yehuda: I regret that I made him below; R. Nechemya: I am comforted that I made him below)", ['regretted_making_man'])
    if q == 'wipe_two_worlds': return cell(('this_world', 'the_world_to_come'), M, "Sanhedrin 108a:5 — R. Akiva: 'and He wiped out every living thing' (7:23) — in this world; 'and they were wiped from the earth' — from the world to come; R. Yehuda ben Beteira: they neither live nor are judged — 'My spirit shall not JUDGE' (6:3); the resolve's entry (6:7 'I will wipe out') closed by the execution", ['to_be_wiped', 'wiped_out'])
    if q == 'favor_even_noah': return cell('the_decree_sealed_on_noah_too', M, "Sanhedrin 108a:14 — the school of R. Yishmael: even on Noah the decree was sealed, but he found favor in the eyes of the LORD — 'I regret that I made them; but Noah found favor' (6:7-8); the favor word's first token (measured, the frozen unit's export)", ['found_favor'])
    if q == 'flood_month_row': return cell(('iyar', 'cheshvan'), M, "Rosh Hashanah 11b:6-7 — 'in the second month, on the seventeenth day' (7:11): R. Yehoshua — the seventeenth of Iyar, the day the Pleiades set; R. Eliezer — the seventeenth of Cheshvan, the day the Pleiades rise (the world created in Nisan / in Tishrei): the tape's ordinal reading printed beside C2 (the ordinal second month from Tishrei is Cheshvan — R. Eliezer's, the running count)", ['fountains_split'])
    return cell('no_case', I, '', [FX.NONE])


def ark(q):
    if q == 'corrupt_five': return cell('mated_across_kinds', M, "Sanhedrin 108a:11 — 'for all flesh had corrupted its way on the earth' (6:12): R. Yochanan — it teaches that they mated beast with wild beast and wild beast with beast, and all with man, and man with all; the corrupt root five times both ways (the frozen unit's export)", ['earth_corrupted'])
    if q == 'robbery_seals': return cell('robbery', M, "Sanhedrin 108a:12 — 'the end of all flesh has come before Me, for the earth is filled with VIOLENCE' (6:13): R. Yochanan — come and see how great the power of robbery is: the generation of the flood transgressed everything, and their decree was not sealed until they stretched their hands to robbery; Bereshit Rabbah 31:5 (violence less than a perutah, robbery a perutah)", ['sealed_for_violence'])
    if q == 'spec_numbers': return cell((300, 50, 30), I, "'three hundred cubits the length of the ark, fifty cubits its breadth, thirty cubits its height' (6:15) — the numbers parsed; 'lower, second and third decks' (6:16)", ['ark_spec'])
    if q == 'decks': return cell(('dung', 'beasts', 'man'), M, "Sanhedrin 108b:11 — 'lower, second and third decks' (6:16): a tanna taught — the lowest for the dung, the middle for the beasts, the top for man; 108b:9 the light: R. Yochanan — set in it precious stones and pearls to shine like noon (or a window — Bereshit Rabbah 31:11's two arms)", ['ark_spec'])
    if q == 'covenant_by_call': return cell(PS_.covenant('covenant_heads')['v'], P, "CALLED cold_run_pre_sinai.covenant('covenant_heads') -> 9:9's addressees 'with you and with your seed after you' [IMPORT, live]: 'and I will establish My COVENANT with you' (6:18) is the covenant word's FIRST token (the frozen unit's export), a promise closed at 9:9-11 by that engine's act — the story's scene issues the close at 9:11 (a REFERENCE)", ['covenant_promised'])
    if q == 'covenant_seats': return cell(c_covenant, I, "the bare noun 'covenant' in the stretch: %r — 6:18 the promise (this runner), 9:9-16 the establishment (the pre-Sinai engine's span; 9:12 and 9:17 carry the ARTICLED form, a second census), 14:13 'the masters of Abram's covenant' (the allies), 15:18 the cutting with Abram (this runner)" % (c_covenant,), ['covenant_promised', 'covenant_cut'])
    if q == 'receipt': return cell('thus_did_noah', I, "'and Noah did according to all that God commanded him, so he did' (6:22) — the receipt that closes the ark's debit; the refrain at 7:5, 7:9, 7:16 (the census's INTERNAL pointers)", ['ark_built'])
    if q == 'clean_by_call': return cell(SH.classify({'clazz': 'land', 'hoof': True, 'cud': True})[0], P, "CALLED cold_run_shemini.classify(land, split hoof, cud) -> 'pure' [IMPORT, live]: 'of every CLEAN beast take seven and seven' (7:2), 'of every clean beast and of every clean fowl' (8:20) — the Shemini engine's institution named before its law (a REFERENCE); Sanhedrin 108b:6-7: how did Noah know? Rav Chisda — he passed them before the ark, those the ark received; R. Abbahu — those that came of themselves", ['olah_offered'])
    if q == 'seven_days_arms': return cell(('methuselahs_mourning', 'the_sun_reversed', 'a_taste_of_the_world_to_come'), M, "Sanhedrin 108b:4-5 — 'and it was after the SEVEN days' (7:10): what were the seven days? Rav — the days of mourning for Methuselah (the eulogy of the righteous holds back the punishment); another: the Holy One changed the order of creation for them — the sun rising in the west; another: a great time and then a small time; another: He let them taste the world to come; Bereshit Rabbah 32:7 the same", ['seven_days_reprieve'])
    if q == 'forty_arms': return cell(('the_torah_in_forty', 'the_embryos_forty'), M, "Bereshit Rabbah 32:5 — 'forty days and forty nights' (7:4): R. Shimon ben Yochai — they transgressed the Torah given in forty days, therefore forty; R. Yochanan ben Zakkai — they corrupted the form that is formed in forty days", ['seven_days_reprieve'])
    if q == 'intercourse_order': return cell(('barred_at_6_18', 'permitted_at_8_16'), M, "Sanhedrin 108b:14 — 'you and your sons, and your wife and your sons' wives' (6:18) against 'you and your wife, and your sons and your sons' wives' (8:16): R. Yochanan — from here they said they were forbidden marital relations in the ark, and permitted on going out; Bereshit Rabbah 34:7", ['ark_intercourse_barred', 'intercourse_permitted'])
    if q == 'three_smitten': return cell(('the_dog', 'the_raven', 'ham'), M, "Sanhedrin 108b:15 — three cohabited in the ark and all were smitten: the dog, the raven, and Ham — the dog is tied, the raven spits, Ham was smitten in his skin (the value on Ham's row; the ink narrates nothing of it)", ['ark_intercourse_barred'])
    return cell('no_case', I, '', [FX.NONE])


def flood(q):
    if q == 'eyeball': return cell('judged_by_water_like_the_eyeball', M, "Sanhedrin 108a:9 — R. Yose: the generation of the flood grew proud only on account of the eyeball, which is like water ('and they took them wives from all they chose', 6:2); therefore He judged them with water, which is like the eyeball ('all the fountains of the great deep were split', 7:11)", ['fountains_split'])
    if q == 'beasts_guilt': return cell('the_wedding_canopy', M, "Sanhedrin 108a:19-20 — 'and He wiped out every living thing' (7:23): if man sinned, what did the beast sin? a tanna in R. Yehoshua ben Korcha's name — a man made a wedding canopy for his son and prepared every kind of feast; his son died and he scattered the canopy: what did I create beast and wild beast for but for man? now that man sins, what do I need them for", ['wiped_out'])
    if q == 'not_the_fish': return cell('not_the_fish', I, "'all that was on the DRY LAND died' (7:22) — Sanhedrin 108a:21: and not the fish of the sea; the ink's own scope on the destroy entry", ['wiped_out'])
    if q == 'remnant': return cell(1, I, "'and only Noah REMAINED, and those with him in the ark' (7:23) — the clause's only seat in the Tanakh (measured): the remnant root's first token (the frozen unit's export)", ['only_noah_remained'])
    if q == 'hundred_fifty': return cell(150, I, "'and the waters prevailed on the earth a hundred and fifty days' (7:24) — the number parsed; 8:3 the same number at the decrease; the tape's C1 (7:11 to 8:4 by the Calendar — the ink's 150 against the modeled months)", ['waters_prevailed_a_hundred_and_fifty'])
    if q == 'three_rows_sheet': return cell(('the_flood', 'the_dispersion', 'sodom'), A, "Mishnah Sanhedrin 10:3 — three generations of this stretch have no share in the world to come, each from its own verse: the flood ('My spirit shall not judge', 6:3 — neither judgment nor spirit), the dispersion ('and the LORD scattered them' this world, 'from there He scattered them' the world to come, 11:8-9), the men of Sodom ('wicked' this world, 'sinners' the world to come, 13:13 — but they stand in judgment; R. Nechemya: neither stand); three HEAVEN entries on the ledger (the sequence runner CG7)", ['no_share_in_the_world_to_come'])
    if q == 'twelve_months_sheet': return cell(12, A, "Mishnah Eduyot 2:10 — five judgments of twelve months: the generation of the flood's judgment twelve months (R. Akiva); Bereshit Rabbah 33:7's own arithmetic on 7:11 to 8:14: 'why the twenty-seventh and not the sixteenth of the second month? these are the eleven days by which the solar year exceeds the lunar' — the sequence runner CG1 grades the stretch as twelve months plus the ink's days", ['ground_seen_dry'])
    return cell('no_case', I, '', [FX.NONE])


def remembering(q):
    if q == 'remember_seats': return cell([(8, 1)], I, "'and God REMEMBERED Noah' (8:1) — the remember verb's Torah debut (the frozen unit's export); 'and God remembered' at 8:1, 19:29, 30:22 in Genesis (measured — Lot for Abraham's sake, Rachel: S3's seats)", ['remembered_by_god'])
    if q == 'boiling': return cell('subsided_like_the_kings_wrath', M, "Sanhedrin 108b:3 — Rav Chisda: with boiling water they sinned and with boiling water they were judged — 'and the waters SUBSIDED' (8:1) here, 'and the king's wrath subsided' at Esther 7:10", ['waters_receding'])
    if q == 'three_fountains': return cell(3, M, "Bereshit Rabbah 33:4 — 'and the fountains of the deep were stopped' (8:2): but not ALL the fountains — three stayed open: the fountain of Tiberias, Abalonis, and the cave of Paneas (Sanhedrin 108a:10's three by another list)", ['waters_receding'])
    if q == 'window_from': return cell(WE.CAL_PARAMS['window_count_from']['value'], D, "the row window_count_from — 'and it was at the end of forty days that Noah opened the window' (8:6): the forty counted from 8:5's first of the tenth month, the nearest date the ink states (channel ink, said so); the dove's two waits of seven days (8:10, 8:12) from the window's day", ['ground_seen_dry'])
    if q == 'raven_retort': return cell('your_master_hates_me_and_you_hate_me', M, "Sanhedrin 108b:12-13 — 'and he sent out the raven' (8:7): Reish Lakish — the raven gave Noah a winning retort: your Master hates me (seven of the clean, two of the unclean) and you hate me (you leave the kind of seven and send the kind of two); Noah: wicked one — what is permitted to me is forbidden to me, what is forbidden to me all the more", ['raven_sent'])
    if q == 'dove_three': return cell(('returned', 'the_olive_leaf', 'did_not_return'), I, "the dove's three sendings: found no rest and returned (8:9 — 'rest' the noun at 8:9 alone in the Torah, measured), came in at evening with the olive leaf plucked (8:11), did not return again (8:12) — the value per sending; the two waits of seven days the markers (the sequence runner CG4)", ['dove_returned'])
    if q == 'olive_bitter': return cell('bitter_from_your_hand_not_sweet_from_flesh_and_blood', M, "Sanhedrin 108b:17 — 'and behold, an olive leaf plucked in her mouth' (8:11): R. Elazar — the dove said before the Holy One: let my food be bitter as the olive and given from Your hand, and not sweet as honey and given from the hand of flesh and blood (Prov 30:8 'feed me my allotted bread' — 'plucked' a language of food)", ['dove_returned'])
    if q == 'clean_birds': return cell('dwell_with_the_righteous', M, "Sanhedrin 108b:16 — 'and he sent out the dove from him' (8:8): R. Yirmeya — from here, the dwelling of clean birds is with the righteous", ['dove_returned'])
    if q == 'year_and_days': return cell((1, 10), I, "7:11 (the six hundredth year, the second month, the seventeenth) to 8:14 (the second month, the twenty-seventh) — a year and ten days by the ink's own dates (the calendar row life_year_reading's witness); Bereshit Rabbah 33:7 reads the days as the solar excess", ['ground_seen_dry'])
    return cell('no_case', I, '', [FX.NONE])


def exit(q):
    if q == 'by_permission': return cell('entered_and_went_out_by_permission', M, "Bereshit Rabbah 34:4 — 'go out from the ark' (8:16): Noah said, as I did not enter the ark but by permission, so I do not go out but by permission — 'come into the ark' (7:1), 'and Noah came' (7:7), 'go out' (8:16), 'and Noah went out' (8:18): the two debits and their receipts", ['exit_owed', 'out_of_the_ark'])
    if q == 'by_families': return cell('by_families_not_they', M, "Sanhedrin 108b:18-19 — 'by their families they went out of the ark' (8:19): R. Yochanan — by their families, and not they (no mixing of kinds); Rav Chana bar Bizna: Eliezer to Shem the Great — how did you fare? great distress was ours in the ark: the creature that eats by day we fed by day, by night by night", ['out_of_the_ark'])
    if q == 'olah_by_call': return cell(OF.dispatch('olah')['place']['v'], P, "CALLED cold_run_offerings.dispatch('olah') -> the burnt offering's place (north) [IMPORT, live]: 'and offered BURNT OFFERINGS on the altar' (8:20) names the institution the offering engine compiles — the first altar and the first burnt offerings (a REFERENCE)", ['olah_offered'])
    if q == 'altar_seats': return cell(c_altar, I, "'and he built an altar' in the stretch: %r — Noah's (8:20), Abram's at Shechem (12:7), at Bethel (12:8), at Hebron (13:18): four altars" % (c_altar,), ['altar_built'])
    if q == 'great_altar': return cell('the_great_altar_of_jerusalem', M, "Bereshit Rabbah 34:9 — 'and Noah built an altar to the LORD' (8:20): R. Elazar ben Yaakov — on the great altar of Jerusalem, where the first man offered; 'built' — 'he considered': why did the Holy One command me to take more of the clean than the unclean? to offer of them", ['altar_built', 'olah_offered'])
    if q == 'savor_seat': return cell(1, I, "'and the LORD smelled the PLEASING SAVOR' (8:21) — the phrase's only seat in Genesis (measured): the offering engine's phrase (Lev 1:9 onward) at its first narrative seat; the offering-regard class's second firing after Abel's (the frozen unit's export)", ['savor_smelled'])
    if q == 'heart_resolve': return cell('the_righteous_rule_their_hearts', M, "Bereshit Rabbah 34:10 — 'and the LORD said to His heart' (8:21): the wicked are in the power of their hearts ('the fool said in his heart', 'Esau said in his heart', 'Jeroboam said in his heart', 'Haman said in his heart'); the righteous — their hearts are in their power", ['ground_not_cursed_again'])
    if q == 'seasons_standing': return cell('as_long_as_heaven_and_earth_stand', M, "Bereshit Rabbah 34:11 — 'while the earth remains, seedtime and harvest ... shall not cease' (8:22): R. Yudan in R. Shmuel's name — what do the sons of Noah suppose, that their covenant stands forever? as long as heaven and earth stand their covenant stands; 'shall not cease' the Sabbath root's consonants — a homograph named at the census", ['seasons_pledged'])
    if q == 'blessing_by_call': return cell(PS_.creation('three_blessings')['v'], P, "CALLED cold_run_pre_sinai.creation('three_blessings') -> the blessing's three verse positions (the fish, the man, the day) [IMPORT, live]: 'and be fruitful and multiply on the earth' (8:17 — the exit command's formula is 1:28's and 9:1's, that engine's institution: a REFERENCE)", ['exit_owed'])
    return cell('no_case', I, '', [FX.NONE])


def vineyard(q):
    if q == 'profaned': return cell('became_common', M, "Bereshit Rabbah 36:3 — 'and Noah the man of the ground BEGAN' (9:20): he was profaned and became common — why? 'and planted a vineyard': had he nothing else fit to plant? ('planted a vineyard' the phrase's only seat in the Tanakh, measured)", ['vineyard_planted'])
    if q == 'same_day': return cell('planted_drank_disgraced_in_one_day', M, "Bereshit Rabbah 36:4 — R. Chiya bar Abba: on the same day he planted, on the same day he drank, on the same day he was disgraced; 'and he WAS UNCOVERED' (9:21 — the reflexive at 9:21 alone in the Tanakh, measured): it is not written 'he uncovered' — he caused exile for himself and for the generations", ['drunk', 'uncovered'])
    if q == 'learn_from_adam': return cell('wine_alone_undid_the_first_man', M, "Sanhedrin 70a:21 — 'and Noah the man of the ground began and planted a vineyard': Rav Chisda in Rav Ukva's name — the Holy One said to Noah: Noah, could you not have learned from the first man, whom wine alone undid? as the one who says the tree the first man ate of was a vine (R. Meir, 70a:22)", ['vineyard_planted'])
    if q == 'ham_deed': return cell(('castrated', 'lay_with'), M, "Sanhedrin 70a:18-20 — 'and Noah awoke from his wine and knew what his youngest son had done to him' (9:24): Rav and Shmuel — one said he castrated him, one said he lay with him; the one who says castrated — since he spoiled him for a fourth son, he cursed him by his fourth (Canaan); the one who says lay with him — 'saw' here (9:22) and 'saw' at Shechem (34:2)", ['saw_and_told', 'canaan_cursed'])
    if q == 'canaan_puzzle': return cell('ham_sinned_and_canaan_is_cursed', M, "Bereshit Rabbah 36:7 — 'cursed be Canaan' (9:25): Ham sinned and Canaan is cursed?! R. Yehuda: since it is written 'and God blessed Noah and his sons' (9:1), there is no cursing where there is blessing — therefore 'cursed be Canaan'; R. Nechemya: Canaan saw and told them", ['canaan_cursed'])
    if q == 'slave_tokens': return cell(4, I, "'a slave of slaves shall he be to his brothers' (9:25), 'a slave to them' (9:26, 9:27) — the slave word's first four Torah tokens inside one curse (the frozen unit's export; the phrase 'a slave of slaves' at 9:25 alone in the Tanakh, measured); the slave engines' homograph named at the census", ['canaan_cursed'])
    if q == 'shem_began': return cell(('shem_the_tallit', 'japheth_the_burial'), M, "Bereshit Rabbah 36:6 — 'and Shem and Japheth took the garment' (9:23): R. Yochanan — Shem began the commandment and Japheth came and listened to him; therefore Shem merited the tallit and Japheth the burial (Ezek 39:11)", ['covered_the_father'])
    if q == 'greek_sheet': return cell('greek_alone', A, "Mishnah Megillah 1:8 — the books may be written in any language; Rabban Shimon ben Gamliel: even for the books they permitted only GREEK; Megillah 9b:4-5 (R. Yochanan: his reason — 'God enlarge Japheth, and he shall dwell in the tents of Shem': the words of Japheth shall be in the tents of Shem; R. Chiya bar Abba: the beauty of Japheth — Greek, the most beautiful of Japheth's tongues)", ['japheth_enlarged'])
    if q == 'cyrus': return cell('the_presence_only_in_the_tents_of_shem', M, "Bereshit Rabbah 36:8 — 'God enlarge Japheth' (9:27): this is Cyrus who decreed that the Temple be built; even so, 'and He shall dwell in the tents of Shem' — the Presence rests only in the tents of Shem; bar Kappara: let the words of Torah be said in the language of Japheth in the tents of Shem", ['japheth_enlarged', 'shem_blessed'])
    return cell('no_case', I, '', [FX.NONE])


def nations(q):
    if q == 'nimrod_greatness': return cell('i_gave_greatness_to_nimrod', M, "Chullin 89a:7 — I gave greatness to Nimrod and he said 'come, let us build us a city' (11:4); to Pharaoh — 'who is the LORD'; to Sennacherib, to Nebuchadnezzar, to Hiram: the four who said 'I' — 'he began to be a mighty one in the earth' (10:8, the rebellion's third seat, Bereshit Rabbah 23:7)", ['kingdom_founded'])
    if q == 'amraphel': return cell(('nimrod_is_his_name', 'amraphel_is_his_name'), M, "Eruvin 53a:7 — 'and it was in the days of Amraphel' (14:1): Rav and Shmuel — one said Nimrod is his name, and why Amraphel? because he SAID (amar) and CAST (hipil) Abraham our father into the furnace of fire; one said Amraphel is his name, and why Nimrod? because he made (himrid) the whole world rebel against Him in his kingdom", ['kingdom_founded'])
    if q == 'shinar': return cell(('the_dead_shaken_out', 'shakes_off_the_commandments'), M, "Bereshit Rabbah 37:4 — 'in the land of Shinar' (10:10): Reish Lakish — where the dead of the generation of the flood were shaken out (nin'aru); another: which shakes off (mena'eret) the commandments — no terumah, no tithes, no sabbatical", ['kingdom_founded'])
    if q == 'peleg_prophet': return cell('eber_a_great_prophet', M, "Bereshit Rabbah 37:7 — 'the name of the one was Peleg, for in his days the earth was divided' (10:25): R. Yose ben Chalafta — Eber was a great prophet, who named for the event; the division verb at 10:25 and 1 Chr 1:19 alone (measured); the dispersion's YEAR not on the local shelf — Babel undated on the tape (its events at the counter)", ['peleg_named_for_the_division'])
    if q == 'shem_or_japheth_elder': return cell('japheth_the_elder', M, "Bereshit Rabbah 37:7 — 'Shem ... the brother of Japheth the elder' (10:21): we do not know whether Shem is the elder or Japheth — from 'Shem a son of a hundred years begot Arpachshad two years after the flood' (11:10), Japheth is the elder (the sequence runner's C4: Shem's hundred against 5:32's five hundred)", ['begotten'])
    if q == 'cities_four': return cell(4, I, "'and built Nineveh and Rehoboth-ir and Calah, and Resen' (10:11-12) — the table's four installs (the frozen unit's export); 'that is the great city' — Resen, or Nineveh: the ink's own ambiguity kept", ['cities_built'])
    return cell('no_case', I, '', [FX.NONE])


def babel(q):
    if q == 'one_language': return cell(1, I, "'and the whole earth was of ONE language and of few words' (11:1) — the phrase's only seat in the Tanakh (measured); Bereshit Rabbah 38:6 (R. Elazar: 'few words' — sharp words against 'the LORD our God, the LORD is one' and 'Abraham was one')", ['tower_undertaken'])
    if q == 'three_parties': return cell(('to_dwell', 'to_serve_idols', 'to_make_war'), M, "Sanhedrin 109a:5 — R. Yirmeya bar Elazar: they split into three parties — one said let us go up and dwell there (them the LORD scattered), one said let us go up and serve idols ('there the LORD confounded the language'), one said let us go up and make war (they became apes, spirits, demons and night-demons); 109a:6 R. Natan: all of them intended idolatry — 'let us make us a NAME' here and 'the name of other gods' (Exod 23:13) there", ['tower_undertaken'])
    if q == 'who_to_whom': return cell('mitzrayim_to_cush', M, "Bereshit Rabbah 38:8 — 'and they said one to another' (11:3): who said to whom? R. Berekhya — Mitzrayim said to Cush: 'come, let us make bricks' — these nations are destined to be burned out of the world (the burning verb)", ['tower_undertaken'])
    if q == 'ten_descents': return cell('one_of_the_ten', M, "Bereshit Rabbah 38:9 — 'and the LORD came down to see the city and the tower' (11:5): R. Shimon bar Chalafta taught — this is one of the ten descents written in the Torah (the same list the Mekhilta counts at Exod 19:11, S1's row: one type, lord_descended, at its Genesis seat)", ['descended_to_see'])
    if q == 'ptolemy': return cell('let_ME_go_down', M, "Bereshit Rabbah 38:10 — 'come, let US go down' (11:7): one of the things they changed for King Ptolemy — 'come, let ME go down and confound' (Megillah 9a's list, S1's row for 12:40); R. Abba bar Kahana: 'from their language I will make a disgrace' — one asked his fellow for an axe and he handed him a spade", ['language_confounded'])
    if q == 'thirds': return cell(('burned', 'swallowed', 'stands'), M, "Sanhedrin 109a:7 — R. Yochanan: the tower — a third burned, a third swallowed, a third stands; Rav: the tower's air makes one forget; Rav Yosef: Babel and Borsif are a bad sign for Torah", ['building_ceased'])
    if q == 'two_scatterings': return cell(('this_world', 'the_world_to_come'), A, "Mishnah Sanhedrin 10:3 — 'and the LORD scattered them from there' (11:8) — in this world; 'and from there the LORD scattered them' (11:9) — in the world to come: the second row of the stretch's three, the HEAVEN entry on the builders", ['no_share_in_the_world_to_come', 'scattered'])
    if q == 'scatter_seats': return cell([(11, 8)], I, "'and the LORD SCATTERED them' (ויפץ) at 11:8 in Genesis (measured; Exod 5:12, 1 Sam 13:8 elsewhere) — the scatter verb's Torah debut inside the table's brackets (the frozen unit's export; 10:18, 10:32, 11:4 the passive and the fear)", ['scattered'])
    return cell('no_case', I, '', [FX.NONE])


def shem_line(q):
    if q == 'two_years_after': return cell((100, 2), I, "'Shem a son of a hundred years begot Arpachshad two years after the flood' (11:10) — the numbers parsed; the tape's marker (C4: Shem's hundred against 5:32's five hundred — Japheth the elder)", ['begotten'])
    if q == 'haran_furnace': return cell('terah_the_idol_maker', M, "Bereshit Rabbah 38:13 — 'and Haran died in the presence of Terah his father' (11:28): R. Chiya son of Rav Adda of Jaffa — Terah was an idol-maker; the story of the shop, the woman with the bowl of flour, the stick in the greatest idol's hand; Nimrod's furnace — Haran: if Abram wins I am his, if Nimrod I am his — he was burned: 'in the presence of his father'", ['died_before_his_father'])
    if q == 'died_in_sequence': return cell(1, I, "of the eleven 'and he died' seats of the stretch (measured), Haran's alone (11:28) is narrated IN SEQUENCE before his father's total — the type `died` at its Genesis seat (the family engine's daemon seat-checked to Gen 23); the ten totals ride the proleptic markers", ['died_before_his_father'])
    if q == 'iscah': return cell('iscah_is_sarah', M, "Megillah 14a:13 — 'the father of Milcah and the father of Iscah' (11:29): R. Yitzchak — Iscah is Sarah; why Iscah? because she gazed (sakhta) by the holy spirit ('all that Sarah says to you, listen to her voice', 21:12); another: all gazed at her beauty — the registry holds Iscah UNCERTAIN (named, not made)", ['wife_taken'])
    if q == 'marriage_by_call': return cell(FA.commission('marriage_formula')['v'], P, "CALLED cold_run_family.commission('marriage_formula') -> the formula's five verbs at Gen 24:67 [IMPORT, live]: 'and Lamech took him two wives' (4:19), 'and they took them wives' (6:2), 'and Abram and Nahor took them wives' (11:29), 'and gave her to Abram her husband to him AS A WIFE' (16:3 — the formula's own token, measured at seven Genesis seats) — the taking side at the stretch's seats before Gen 24 (a REFERENCE; the family daemon seat-checked to Gen 24)", ['wife_taken'])
    if q == 'barren_seat': return cell(1, I, "'and Sarai was barren, she had no child' (11:30) — the clause's only seat in the Tanakh (measured): the barren field's debut, a doubled absence (the frozen unit's export)", ['barren'])
    if q == 'terah_death_gap': return cell((70, 75, 205, 60), I, "Terah seventy at Abram's birth (11:26), Abram seventy-five at the going out (12:4), Terah's days two hundred and five (11:32): the going out precedes Terah's death by SIXTY years by the ink's own numbers — the tape's proleptic marker against the age marker (the sequence runner CG8)", ['begotten'])
    if q == 'terah_death_midrash': return cell('the_wicked_called_dead_in_their_lifetime', M, "Bereshit Rabbah 39:7 — 'and Terah died in Haran' (11:32) written before 'go you' (12:1): R. Yitzchak — if for the reckoning, sixty-five more years are wanted for him; rather, the wicked are called dead in their lifetime — the midrash's own number (sixty-five) printed beside the tape's sixty", ['begotten'])
    if q == 'abram_elder': return cell('abram_a_year_older_than_nahor', M, "Bereshit Rabbah 38:14 — 'and Abram and Nahor took them wives' (11:29): Abram was a year older than Nahor and Nahor a year older than Haran — Haran two years younger than Abraham; Haran begets at six, and Abram does not beget?!", ['begotten'])
    return cell('no_case', I, '', [FX.NONE])


def call(q):
    if q == 'go_receipt': return cell('as_the_lord_had_spoken', I, "'go you' (12:1) — the corpus's first object-withheld command (the frozen unit's export); 'and Abram went AS THE LORD HAD SPOKEN to him' (12:4) — the receipt that closes the debit (the census's INTERNAL pointer)", ['go_owed'])
    if q == 'two_go_you': return cell(('aram_naharaim_and_aram_nachor', 'the_pieces_to_haran'), M, "Bereshit Rabbah 39:8 — 'go you' twice (12:1, 22:2): R. Yehuda — one from Aram Naharaim and one from Aram Nachor; R. Nechemya — one from both, and one when He flew him from between the pieces and brought him to Haran; R. Levi (39:9): which is dearer? from 'to the land of Moriah' the second", ['go_owed'])
    if q == 'new_creature': return cell('i_will_MAKE_you', M, "Bereshit Rabbah 39:11 — 'and I will make you a great nation' (12:2): R. Berekhya — 'I will give you' or 'I will set you' is not written but 'I will MAKE you' — once I make you a new creature you are fruitful and multiply; 'great' — the nation of which it is said 'what great nation' (Deut 4:7)", ['great_nation_promised'])
    if q == 'ladder': return cell(('bless_you', 'make_your_name_great', 'be_a_blessing', 'bless_your_blessers', 'curse_your_curser', 'all_families_blessed_in_you'), I, "the promise ladder of 12:2-3 — six clauses after the great nation; Bereshit Rabbah 39:12 (R. Yirmeya: the Holy One was stricter about the honor of the righteous than about His own — 'those who bless you I will bless, and him who curses you I will curse')", ['blessing_promised'])
    if q == 'land_seats': return cell([(12, 7), (13, 15), (15, 7), (15, 18)], I, "the land promised to Abram's seed at 12:7 ('I will give'), 13:15 ('to you and to your seed forever'), 15:7 ('to give you this land to inherit it') — three HEAVEN entries — and CLOSED at 15:18 by the ink's own perfect 'to your seed I HAVE GIVEN' (the phrase's only seat in the Tanakh, measured): the give-arc's receipt (the frozen unit's export)", ['land_promised', 'land_granted'])
    if q == 'three_altars': return cell(3, M, "Bereshit Rabbah 39:16 — 'and he built there an altar' (12:8): R. Elazar — three altars he built: one for the tidings of the land of Israel (12:7), one for its acquisition (12:8), one that his sons not fall at Ai (13:18 — Josh 7:6); the fourth of the stretch Noah's", ['altar_built'])
    if q == 'called_seats': return cell([(12, 8), (26, 25)], I, "'and he CALLED on the name of the LORD' (ויקרא בשם יהוה) at 12:8 and 26:25 in Genesis (measured; 13:4 'and Abram called there on the name' the second seat of the stretch; 4:26 the profanation's 'to call on the name')", ['called_on_the_name'])
    if q == 'seventy_five': return cell(75, I, "'and Abram was a son of seventy-five years at his going out from Haran' (12:4) — the number parsed; the tape's age marker; Hagar's ten years (16:3) run from the arrival in the same year (the sequence runner CG6)", ['encamped_at'])
    if q == 'stations': return cell(7, I, "Abram's stations of the stretch: Canaan (12:5), Shechem (12:6), east of Bethel (12:8), the Negev (12:9), Egypt (12:10), Bethel again (13:1-3), Hebron (13:18) — seven; Terah's Haran (11:31), the builders' Shinar (11:2), Lot's plain (13:12) beside them — the itinerary verbs the tape's own (S1's journeyed at its Genesis seats)", ['encamped_at'])
    return cell('no_case', I, '', [FX.NONE])


def egypt(q):
    if q == 'famine_third': return cell('the_third_of_ten', M, "Bereshit Rabbah 40:3 — 'and there was a famine in the land' (12:10): the third of the ten famines (25:3's list: Adam's, Lamech's, Abraham's, Isaac's, Jacob's ...); 40:2 (he went out and the famine leaped on him — 'happy is the man whom You chasten')", ['famine'])
    if q == 'first_speech': return cell('behold_now_i_know', I, "'behold now, I know that you are a woman of beautiful appearance' (12:11) — Abram's first recorded speech (the frozen unit's export, census-verified); 'say, I pray you, that you are my sister' (12:13)", ['presented_as_sister'])
    if q == 'chest': return cell('hidden_in_a_chest_at_the_customs', M, "Bereshit Rabbah 40:5 — 'and it was, when Abram came into Egypt' (12:14): and where was Sarah? he put her in a chest and locked it; at the customs they said: pay the duty — 'I will pay'; 'you carry garments' — 'I will pay for garments'; 'gold' — 'for gold' ... 'pearls' — 'for pearls'; open it and let us see", ['presented_as_sister'])
    if q == 'passive_take': return cell('taken_passive', I, "'and the woman WAS TAKEN to Pharaoh's house' (12:15) — the passive (the phrase's only seat in Genesis, measured); 'and I took her to me as a wife' (12:19 — the formula's token in Pharaoh's mouth); the take verb's triad on one woman (the frozen unit's export): the BODY entry on Sarai, closed at 12:20", ['taken_to_pharaohs_house'])
    if q == 'raatan': return cell('raatan', M, "Bereshit Rabbah 41:2 — 'and the LORD plagued Pharaoh with great plagues' (12:17): Reish Lakish in bar Kappara's name — with ra'atan Pharaoh was struck; Rabban Shimon ben Gamliel: twenty-four kinds of boils, and none harder than ra'atan — the affliction engine's datum (PARAMETER), the plague entry S1's plague_struck by the noun shared with Exod 11:1", ['plague_struck'])
    if q == 'pattern': return cell('whatever_is_written_of_abraham_is_written_of_his_sons', M, "Bereshit Rabbah 40:6 — 'and he dealt well with Abram for her sake ... and Pharaoh commanded men concerning him and they sent him away' (12:16, 12:20): R. Pinchas in R. Hoshaya's name — the Holy One said to Abraham: go and tread the road before your sons: whatever is written of Abraham is written of his sons — 'a famine in the land' / 'the famine was heavy in the land'; 'to sojourn there' / 'to sojourn in the land'; 'they will kill me' / 'every son born, cast him'; 'and the LORD plagued Pharaoh' / 'one more plague'; 'and Pharaoh commanded men' / 'Pharaoh commanded all his people'; the sending here and at the exodus: the TRANSFER's teacher for sent_out at 12:20 and the pattern for enriched_for_her_sake", ['enriched_for_her_sake', 'sent_out'])
    if q == 'silver_and_gold': return cell('brought_them_out_with_silver_and_gold', M, "Bereshit Rabbah 41:3 — 'and Abram was very rich in cattle, in silver and in gold' (13:2): 'and He brought them out with silver and gold' (Ps 105:37) — the pattern's second seat; R. Elazar son of R. Menachem: 'he went on his journeys' — to pay his debts", ['very_rich'])
    return cell('no_case', I, '', [FX.NONE])


def separation(q):
    if q == 'muzzled': return cell('abrahams_beasts_muzzled_lots_not', M, "Bereshit Rabbah 41:5 — 'and there was strife between the herdsmen' (13:7): R. Berekhya in R. Yehuda son of R. Simon's name — the beasts of Abraham our father went out muzzled, and Lot's did not; Abraham's herdsmen said: is robbery permitted? Lot's: the land is given to Abraham and he has no heir — Lot inherits; 'and the Canaanite and the Perizzite then dwelt in the land' — not yet", ['strife_between_herdsmen'])
    if q == 'lewdness': return cell('the_whole_verse_a_language_of_lewdness', M, "Bereshit Rabbah 41:7 — 'and Lot lifted up his eyes and saw all the plain of the Jordan' (13:10): R. Yose bar Chanina — the whole verse is a language of lewdness ('and his master's wife lifted up her eyes', 39:7 ...); 'and Lot journeyed EAST' (13:11) — he removed himself from the Ancient One of the world", ['chose_the_plain'])
    if q == 'parted_seat': return cell(1, I, "'and they SEPARATED each from his brother' (13:11) — the verb's form at 13:11 alone in Genesis (measured); 2:10's river 'parted' the root's Eden seat (the frozen unit's export); 13:9 the request, 13:14 'after Lot was separated from him'", ['parted'])
    if q == 'sodom_sheet': return cell(('wicked_this_world', 'sinners_the_world_to_come', 'but_they_stand_in_judgment'), A, "Mishnah Sanhedrin 10:3 — 'the men of Sodom have no share in the world to come, as it is said: and the men of Sodom were wicked and sinners against the LORD exceedingly (13:13) — wicked in this world, sinners in the world to come; but they stand in judgment' — the Mishnah's own proof-text is this stretch's narrator clause: the third HEAVEN entry", ['no_share_in_the_world_to_come'])
    if q == 'sodom_arms': return cell(('wicked_in_body_sinners_in_money', 'wicked_in_money_sinners_in_body'), M, "Sanhedrin 109a:9 — Rav Yehuda: 'wicked' with their bodies, 'sinners' with their money (39:9 'this great evil and sin against God'; Deut 15:9 'and it be sin in you'); the baraita reversed — wicked with their money, sinners with their bodies; 'exceedingly' — that they intended and sinned", ['no_share_in_the_world_to_come'])
    if q == 'dust': return cell('as_the_dust_blessed_only_by_water', M, "Bereshit Rabbah 41:9 — 'and I will make your seed as the dust of the earth' (13:16): as the dust from one end of the world to the other, so your sons scattered from end to end; as the dust is blessed only by water, so your sons by the merit of the Torah; 'as the dust of the earth' at 13:16 and 28:14 in Genesis (measured)", ['seed_as_dust'])
    if q == 'walk_by_call': return cell(FA.purchase('three_modes')['v'], P, "CALLED cold_run_family.purchase('three_modes') -> the Mishnah's money, deed, possession run at Machpelah [IMPORT, live]: 'arise, WALK through the land in its length and in its breadth, for to you I will give it' (13:17) — Bava Batra 100a:7 (R. Elazar: R. Eliezer's reason — walking acquires, 'for to you I will give it'; the sages: out of affection He said so, that it be easy for his sons to conquer) — the walking as a fourth mode is a TRANSFER the cell carries with its teacher; the debit on Abram stays OPEN (the walk is never narrated; 13:18 moves the tent)", ['land_walk_commanded'])
    return cell('no_case', I, '', [FX.NONE])


def war(q):
    if q == 'years_chain': return cell((12, 13, 14), I, "'twelve years they served Chedorlaomer, and in the thirteenth year they rebelled; and in the fourteenth year came Chedorlaomer' (14:4-5) — the numbers parsed: 12 + 1 + 1 = 14, the ink's own chain (the sequence runner CG5)", ['rebelled'])
    if q == 'years_arms': return cell((25, 13), M, "Bereshit Rabbah 42:6 — R. Yose: twelve and thirteen — twenty-five years; Rabban Shimon ben Gamliel: all of them were thirteen years — and 'in the fourteenth year'? in the fourteenth of their rebellion: the two sums beside the ink's chain", ['rebelled'])
    if q == 'annal': return cell(0, I, "the war annal 14:1-11 — eleven verses with ZERO speech (the frozen unit's export): the kings' clock, the sweep, the pits, the taking of the goods", ['defeated'])
    if q == 'og': return cell('the_escapee_is_og', M, "Bereshit Rabbah 42:8 — 'and the escapee came' (14:13): Reish Lakish in bar Kappara's name — he is Og, he is the escapee; why Og? he found Abram sitting occupied with the commandment of cakes (uggot); not for Heaven's sake did he come: 'your nephew is taken — he goes out to war and is killed, and I take Sarai' — the registry holds the escapee UNCERTAIN", ['called_the_hebrew'])
    if q == 'hebrew_arms': return cell(('from_eber', 'from_beyond_the_river', 'the_language'), M, "Bereshit Rabbah 42:8 — 'Abram the HEBREW' (14:13 — the token at 14:13 and 39:17 in Genesis, measured): R. Yehuda — the whole world on one side (ever) and he on the other; R. Nechemya — from Eber; the rabbis — from beyond the river, and he speaks the language of beyond the river", ['called_the_hebrew'])
    if q == 'three_eighteen': return cell(318, I, "'three hundred and eighteen' (14:14) — the number parsed (the phrase's only seat in the Tanakh, measured)", ['muster_of_three_hundred_and_eighteen'])
    if q == 'eliezer': return cell('eliezer_alone', M, "Nedarim 32a:17 — 'three hundred and eighteen': R. Ami bar Abba — Eliezer alone, equal to them all; some say: Eliezer, whose letter-count is thus (318); 32a:16 (Rav: he made them pale with Torah; Shmuel: with gold)", ['muster_of_three_hundred_and_eighteen'])
    if q == 'punished_210': return cell(('pressed_scholars_into_service', 'whereby_shall_i_know', 'give_me_the_persons'), M, "Nedarim 32a:14-15 — R. Abahu in R. Elazar's name: why was Abraham our father punished and his sons enslaved to Egypt two hundred and ten years? because he pressed Torah scholars into service — 'he led out his trained men' (14:14); Shmuel: because he went too far in testing the Holy One's attributes — 'whereby shall I know' (15:8); R. Yochanan: because he kept people from entering under the wings of the Presence — 'give me the persons and take the goods' (14:21): the CAUSE the tradition names for the decree of 15:13", ['seed_to_serve_four_hundred'])
    if q == 'night_halves': return cell(('of_itself', 'its_maker_divided_it'), M, "Bereshit Rabbah 43:3 — 'and he divided himself against them by night' (14:15): R. Binyamin bar Yefet in R. Yonatan's name — the night divided of itself; the rabbis — its Maker divided it: the Holy One said, their father acted with Me at midnight, I too act with his sons at midnight — 'and it was at midnight' (Exod 12:29, S1's night)", ['night_divided'])
    if q == 'children_not_returned': return cell('men_and_women_returned_the_children_not', M, "Bereshit Rabbah 43:4 — 'and also the women and the people' (14:16): R. Yudan — men and women he returned, the children he did not return; they arose and converted and fenced the nakedness of their fathers", ['goods_brought_back'])
    if q == 'priest_by_call': return cell(sorted(PR.family('addressees')['v'].keys())[:2], P, "CALLED cold_run_priesthood.family('addressees') -> the office's four populations from Lev 21:1 [IMPORT, live]: 'and he was PRIEST of God Most High' (14:18 — 'priest' at 14:18, 41:45, 41:50, 46:20 in Genesis, measured; the priest of On the others) — the office named before its law (a REFERENCE)", ['bread_and_wine'])
    if q == 'priesthood_from_shem': return cell('taken_from_shem_given_to_abraham', M, "Nedarim 32b:6 — R. Zekharya in R. Yishmael's name: the Holy One sought to bring the priesthood out of Shem — 'and he was priest of God Most High'; since he set Abraham's blessing before the Place's blessing ('blessed be Abram ... and blessed be God Most High', 14:19-20), He brought it out of Abraham ('you are a priest forever on account of Melchizedek', Ps 110:4)", ['blessed_by_the_priest', 'priesthood_removed'])
    if q == 'salem': return cell('salem_is_jerusalem', M, "Bereshit Rabbah 43:6 — 'and Melchizedek king of SALEM' (14:18): this place makes its inhabitants righteous — Melchizedek, Adonizedek (Josh 10:1); Jerusalem is called righteousness (Isa 1:21)", ['bread_and_wine'])
    if q == 'tithe_by_call': return cell(TM.tithe('land_tithe_status')['v'], P, "CALLED cold_run_temurah.tithe('land_tithe_status') -> 'holy to the LORD' (Lev 27:30) [IMPORT, live]: 'and he gave him a TENTH of all' (14:20 — 'a tenth' at 14:20 alone in Genesis, measured; 28:22 Jacob's vow S3's) — the tithe's institution named at its first seat (a REFERENCE); Bereshit Rabbah 43:8", ['tithe_given'])
    if q == 'raised_hand': return cell(('terumah', 'an_oath'), M, "Bereshit Rabbah 43:9 — 'I have lifted my hand to the LORD' (14:22 — the phrase's only seat in the Tanakh, measured): R. Yehuda — he made them terumah ('you shall lift up the terumah', Num 18:26); R. Nechemya — he made them an oath", ['sworn_to_take_nothing'])
    if q == 'thread_to_latchet': return cell('not_a_thread_nor_a_shoe_latchet', I, "'that I will not take from a thread to a shoe-latchet, nor anything that is yours' (14:23) — the refusal ruling (the frozen unit's export); 'save only what the young men have eaten, and the portion of the men who went with me — Aner, Eshcol and Mamre' (14:24)", ['sworn_to_take_nothing', 'portion_reserved'])
    return cell('no_case', I, '', [FX.NONE])


def pieces(q):
    if q == 'two_fears': return cell(('a_righteous_man_among_the_slain', 'the_reward_consumed'), M, "Bereshit Rabbah 44:4 — 'fear not, Abram; I am a shield to you' (15:1 — the phrase's only seat in the Tanakh, measured): R. Levi — two: Abraham feared and said, perhaps among those hosts I killed was one righteous man; and: perhaps I have received my reward in this world; the rabbis — one", ['shield_promised'])
    if q == 'childless_by_call': return cell(SAN.sanction('uncle_wife')['v'], P, "CALLED cold_run_sanctions.sanction('uncle_wife') -> Lev 20:20's row (the warning 18:14, the sanction 20:20, no court mode, the karet: 'childless they shall die') [IMPORT, live]: 'I go CHILDLESS' (15:2 — ערירי, ariri: the word at Gen 15:2 and Jer 22:30 in the Tanakh, the plural at Lev 20:20-21 alone, measured) — the sanctions engine's word at its narrative seat (a REFERENCE by lemma); the HEAVEN entry on Abram closed at 16:15 by the son born", ['childless'])
    if q == 'heir_by_call': return cell(FA.inheritance('inheritance_order_owed')['v'], P, "CALLED cold_run_family.inheritance('inheritance_order_owed') -> the seats owed forward (Num 27:8, Deut 25:5) [IMPORT, live]: 'one born in my house is my HEIR' (15:3), 'this one shall not be your heir, but he who shall come out of your loins shall be your heir' (15:4) — the inheritance institution by name (a REFERENCE); the entry OPEN to Isaac (S3)", ['heir_from_the_loins'])
    if q == 'astrology': return cell('no_constellation_for_israel', M, "Nedarim 32a:9 — 'and He brought him outside' (15:5): Abraham said before Him: I looked at my constellation and I have but one son; He said: go out of your astrology — there is no constellation for Israel; Bereshit Rabbah 44:12 (He raised him above the vault of the heavens — 'look now toward the heavens')", ['seed_as_stars'])
    if q == 'faith_merit': return cell('inherited_both_worlds_by_faith', M, "the Mekhilta Shirata ch.1 row 1 (S1's own row, read again here): so you find that Abraham our father inherited this world and the world to come only in the merit of faith, as it is said 'and he believed in the LORD' (15:6) — the faith verb's first seat, joined by the Mekhilta itself to Exod 14:31 (one type, believed, at its Genesis seat)", ['believed', 'reckoned_righteousness'])
    if q == 'reckoned_both_ways': return cell('staged_both_ways', I, "'and he believed in the LORD, and He reckoned it to him as righteousness' (15:6 — the clause's only seat in the Tanakh, measured): who reckoned to whom — the frozen unit staged both readings; the ledger's status carries the note", ['reckoned_righteousness'])
    if q == 'furnace': return cell(('michael', 'the_holy_one_himself'), M, "Bereshit Rabbah 44:13 — 'I am the LORD who brought you out of Ur of the Chaldeans' (15:7): R. Eliezer ben Yaakov — Michael went down and saved him from the furnace of fire; the rabbis — the Holy One Himself saved him; Pesachim 118a:20 (Gabriel: I will go down and cool the furnace and save the righteous one); Eruvin 53a:7 (Amraphel who cast him in)", ['brought_out_of_ur'])
    if q == 'by_what_merit': return cell('by_the_atonements', M, "Bereshit Rabbah 44:14 — 'whereby shall I know that I shall inherit it?' (15:8): R. Chiya son of R. Chanina — not as one complaining, but he said: by what merit? He said: by the atonements I give before you — 'take Me a three-year-old heifer' (15:9): three kinds of bulls, three of goats, three of rams", ['pieces_owed'])
    if q == 'birds_by_call': return cell(MI.bird('species')['v'], P, "CALLED cold_run_minchah.bird('species') -> 'turtledoves or young pigeons' (Lev 1:14) [IMPORT, live]: 'a turtledove and a young pigeon' (15:9) — the bird offering's two species named before their law (a REFERENCE); 'but the bird he did not cut' (15:10)", ['pieces_cut'])
    if q == 'kingdoms': return cell(('babylon', 'media', 'greece', 'israel_the_bird'), M, "Bereshit Rabbah 44:15 — 'a three-year-old heifer' — Babylon, which raised three kings; 'a three-year-old she-goat' — Media, three kings; 'a three-year-old ram' — Greece; 'a turtledove and a young pigeon' — Israel; 44:16 ('and the birds of prey came down on the carcasses, and Abram drove them away' — the nations; his merit stands for his sons)", ['pieces_cut'])
    if q == 'four_hundred': return cell(400, I, "'four hundred years' (15:13) — the number parsed; the seed 'from when you have seed' — Bereshit Rabbah 44:18 (משיראה לך זרע): the running setting seed_isaac's teacher on the shelf; the sequence runner's C3b (the exodus = Isaac's birth + 400 to the day)", ['seed_to_serve_four_hundred'])
    if q == 'also_that_nation': return cell(('egypt', 'the_four_exiles'), M, "Bereshit Rabbah 44:19 — 'and ALSO that nation whom they shall serve I will judge' (15:14): it should have said 'also'; what is 'and also'? 'also' — Egypt; 'and also' — to include the four exiles; R. Elazar in R. Yose bar Zimra's name: with these two letters the Holy One assured Abraham; the judgment's entry closed by S1's scene at Exod 12:29 (the twelve months of Eduyot 2:10, S1's CS9)", ['nation_to_be_judged'])
    if q == 'after_ten_plagues': return cell('after_i_bring_ten_plagues', M, "Bereshit Rabbah 44:20 — 'and AFTERWARD they shall go out with great substance' (15:14): R. Acha — 'after that' is not written but 'afterward': after I bring ten plagues on them, afterward they go out with great substance; the entry closed by S1's scene at Exod 12:36 (Berakhot 9a:29-9b:1 — 'so that the righteous one will not say', S1's row)", ['to_go_out_with_substance'])
    if q == 'fourth_generation': return cell(4, I, "'and in the FOURTH generation they shall return here' (15:16) — the ordinal parsed; Exod 6:16-20's four (Levi, Kohath, Amram, Moses — S1's roster); OPEN to Joshua", ['fourth_generation_return', 'amorite_not_full'])
    if q == 'four_things': return cell(('gehenna', 'the_kingdoms', 'the_giving_of_the_torah', 'the_temple'), M, "Bereshit Rabbah 44:21 — 'a smoking furnace and a torch of fire that passed between these pieces' (15:17 — 'between the pieces' the phrase's only seat in the Tanakh, measured): Shimon bar Abba in R. Yochanan's name — four things He showed him: Gehenna, the kingdoms, the giving of the Torah, and the Temple", ['passed_between_the_pieces'])
    if q == 'covenant_cut_seat': return cell(1, I, "'on that day the LORD CUT a covenant with Abram' (15:18) — the cutting verb with the covenant noun: Exod 34's covenant_cut at Genesis' first cutting (a REFERENCE by lemma); Bereshit Rabbah 44:22 (this world revealed to him — and the world to come? R. Yudan, Rabban Yochanan ben Zakkai, R. Akiva)", ['covenant_cut'])
    if q == 'ten_nations': return cell((10, 7, 3), M, "Bereshit Rabbah 44:23 — 'the Kenite and the Kenizzite and the Kadmonite ...' (15:19-21): ten nations named, seven given — the Kenite, the Kenizzite and the Kadmonite for the future (Edom, Moab and Ammon); the value of land_granted", ['land_granted'])
    return cell('no_case', I, '', [FX.NONE])


def hagar(q):
    if q == 'ten_years_sheet': return cell('may_not_neglect_procreation', A, "Mishnah Yevamot 6:6 — 'he married a woman and waited with her ten years and she did not bear: he may not neglect (procreation)' — the rule whose source the Talmud names in this verse: Yevamot 64a:5 ('though there is no proof of the matter, there is an allusion: at the end of TEN YEARS of Abram's dwelling in the land of Canaan' — to teach that dwelling outside the land does not count in the number; likewise he sick, or she, or both imprisoned); Bereshit Rabbah 45:3", ['ten_years_childless'])
    if q == 'ten_years_number': return cell(10, I, "'at the end of ten years of Abram's dwelling in the land of Canaan' (16:3) — the number parsed: from the arrival (12:5) in the year of the going out at seventy-five (12:4) — Abram eighty-five; Ishmael at eighty-six (16:16): the sequence runner CG6", ['ten_years_childless'])
    if q == 'as_a_wife': return cell(7, I, "'to him AS A WIFE' (לו לאשה) at seven Genesis seats (measured: 16:3, 24:67, 25:20, 28:9, 29:28, 34:8, 38:14) — the marriage formula's own token at Hagar's giving; Bereshit Rabbah 45:3: as a wife, not a concubine", ['wife_taken'])
    if q == 'first_union': return cell(('from_the_first_union', 'never_from_the_first'), M, "Bereshit Rabbah 45:4 — 'and he went in to Hagar, and she conceived' (16:4): R. Levi bar Chaita — from the first union she conceived; R. Elazar — a woman never conceives from the first union (Lot's daughters — they controlled themselves)", ['conceived'])
    if q == 'despised_seat': return cell(1, I, "'her mistress was DESPISED in her eyes' (16:4 — the verb's form at 16:4 alone in the Tanakh, measured); 16:5 'and I was despised in her eyes'; Bereshit Rabbah 45:4 (the matrons visiting Sarai: go and visit the wretched one within)", ['mistress_despised'])
    if q == 'wrong_with_words': return cell('you_wrong_me_with_words', M, "Bereshit Rabbah 45:5 — 'my wrong be on you' (16:5 — the clause's only seat in the Tanakh, measured): R. Yudan in R. Yehuda bar Simon's name — you wrong me with words: you hear my disgrace and are silent; R. Berekhya: I want my case with you — 'the LORD judge between me and you' (the tradition's 'she was punished first' searched on the local shelf under its forms and not found: OPEN, a remark)", ['judgment_invoked'])
    if q == 'affliction_reading': return cell('not_obliged_for_her_good_or_ill', M, "Bereshit Rabbah 45:6 — 'behold, your maid is in your hand; do to her what is good in your eyes' (16:6): he said to her, what do I care — neither for her good nor her ill; it is written 'you shall not deal with her as a slave, because you have afflicted her' (Deut 21:14), and this one, after we have afflicted her, we enslave her? — 'and Sarai afflicted her' (the affliction verb's form at 16:6 alone in Genesis, measured)", ['afflicted'])
    if q == 'flight_seat': return cell('the_exodus_daemon_seat_checked', I, "'and she fled from before her' (16:6), 'from before Sarai my mistress I am fleeing' (16:8) — the flight verb of Exod 2:15 (S1's fled) at its Genesis seat: one type, the Exodus daemon seat-checked to Exod 2 (its sought_to_kill is Moses' body threat, not this) — the status here fled_from_the_mistress", ['fled_from_the_mistress'])
    if q == 'return_open': return cell('return_never_narrated', I, "'return to your mistress and submit yourself under her hands' (16:9) — the DEBIT on Hagar; the ink narrates the son born in Abram's house (16:15), never the return: the corpus's demand OPEN, the entry OPEN", ['return_owed'])
    if q == 'named_before_birth': return cell(('isaac', 'solomon', 'josiah'), M, "Bereshit Rabbah 45:8 — 'and you shall call his name Ishmael' (16:11): R. Yitzchak — three were called by their names before they were formed: Isaac ('you shall call his name Isaac', 17:19), Solomon (1 Chr 22:9), Josiah (1 Kgs 13:2) — Ishmael beside them by this verse; 'behold, you are with child' at Gen 16:11 and Judg 13:5, 13:7 (measured — Samson's annunciation)", ['ishmael_announced'])
    if q == 'you_shall_call_vs_abram_called': return cell(('you_shall_call', 'abram_called'), I, "16:11 'and YOU shall call his name Ishmael' (to Hagar) against 16:15 'and ABRAM called the name of his son whom Hagar bore, Ishmael' — the ink's own delta between the annunciation and the naming: the HEAVEN entry closed at the birth", ['ishmael_announced', 'name_given'])
    if q == 'wild_ass': return cell(('grows_in_the_wilderness', 'plunders_souls'), M, "Bereshit Rabbah 45:9 — 'and he shall be a wild ass of a man' (16:12 — the phrase at Gen 16:12 and Job 11:12 in the Tanakh, measured): R. Yochanan — all grow up in settlement and he grows up in the wilderness; Reish Lakish — a wild ass of a man indeed: all plunder property and he plunders souls", ['wild_ass_of_a_man'])
    if q == 'god_of_seeing': return cell('never_conversed_with_a_woman_but_through_an_angel', M, "Bereshit Rabbah 45:10 — 'and she called the name of the LORD who spoke to her: You are a God of seeing' (16:13 — 'a God of seeing' at 16:13 alone in the Tanakh, measured): R. Yehuda bar Simon and R. Yochanan in R. Elazar bar Shimon's name — the Holy One never conversed with a woman but with that righteous one, and she too through a cause (an angel); the name given on the LORD's own entry, the well named for it (16:14)", ['name_given'])
    return cell('no_case', I, '', [FX.NONE])


# ---- (6) THE WRAP: the daemon over the cells — consumes the stretch's acts, writes the ledger, never emits an event ----
_S3_SHARED = frozenset(['appeared', 'named', 'married', 'born', 'bore', 'begot', 'died', 'buried', 'journeyed', 'remembered', 'sent_away', 'fled', 'pursued', 'decree_issued', 'return_commanded', 'famine_came', 'sister_asked', 'woman_taken', 'altar_erected', 'called_on_the_name', 'olah_offered', 'barren', 'anger_burned', 'gifts_given', 'lord_descended', 'believed', 'sentenced', 'land_promised', 'counsel_given'])   # O8 S4 (2026-09-08): + the kinds FROM THE FORD TO THE COFFIN shares (land_promised at 35:12 reached this branch on the tape and read a field it never carries — the leak the tape caught; convention 14 both ways)
def law_primeval(event, world):
    """FROM EDEN TO HAGAR's daemon: the acts of Genesis 2:4-16:16 -> the statuses the tradition names, the promises and
    decrees as HEAVEN entries, the debits with their receipts, the two timers; the closes are the scene's (the ink's own
    fulfillment statements). The day read from the event inside a retrograde-dated stretch (6:3 on the tape), else the clock."""
    k, subj, src = event['kind'], event['subject'], event['case_source']
    day = event.get('day', world.clock.day)
    E_ = lambda eff, s, due=None, cp=None, value=None: {'effect': eff, 'subject': s, 'counterparty': cp, 'amount': None, 'due': due, 'value': value if value is not None else True, 'source_law': 'S2', 'case_source': src}
    gen = WE.seat(src) is not None and WE.seat(src)[0] == 'Gen' and 2 <= WE.seat(src)[1] <= 16   # O8 S3 (2026-09-08): NARROWED to this daemon's own chapters (7k) — S3's stretch shares the kinds below
    if k in _S3_SHARED and not gen: return []   # ONE TYPE UNDER TWO LAW LAYERS, both ways: a shared kind at another seat is another daemon's (Gen 18-31 law_mamre's)
    if k == 'formed_from_dust': return [E_('living_soul', subj)]
    if k == 'placed_in_the_garden': return [E_('to_work_and_keep', subj, value=garden('office')['v'])]
    if k == 'named': return [E_('name_given', subj, value=event['name'])] if gen else []   # ONE TYPE UNDER TWO LAW LAYERS: the Exodus seats are law_exodus_story's
    if k == 'woman_built': return [E_('helper_made', subj, value=garden('helper')['v'])]
    if k == 'deep_sleep_fell': return [E_('deep_sleep_fell', subj, value=event['kind_of_sleep'])] + ([E_('dread_and_darkness', subj)] if WE.seat(src) == ('Gen', 15) else [])
    if k == 'serpent_spoke': return []   # the act kept on the tape for the record; no state the shelf names at this sitting (NARRATIVE_GAPS.md 6d)
    if k == 'ate_of_the_tree': return [E_('breached_the_first_rule', subj, value=breach('tree_identity')['v']), E_('breached_the_first_rule', event['gave_to'], value=breach('tree_identity')['v'])]
    if k == 'eyes_opened': return [E_('eyes_opened', subj), E_('girdles_made', subj)]
    if k == 'hid_from_the_voice': return []   # the act kept on the tape for the record (6d)
    if k == 'interrogated': return [E_('deceived', 'eve', value='the serpent deceived me (3:13)')]
    if k == 'sentenced' and WE.seat(src) in (('Gen', 3), ('Gen', 4)):   # ONE TYPE UNDER TWO LAW LAYERS: Judah's sentence (Gen 38:24) is law_family's — found by the sequence tape's first run (KeyError on the family's event)
        s = event['sentence']
        if s == 'serpent': return [E_('serpent_cursed', subj, value=sentences('seventy_one')['v']), E_('enmity_set', subj, cp='eve')]
        if s == 'woman': return [E_('pain_multiplied', subj), E_('ruled_by_the_husband', subj, value=sentences('four_desires')['v'])]
        if s == 'man': return [E_('ground_cursed', 'the-ground', cp=subj), E_('sweat_bread', subj), E_('return_to_dust', subj, cp='HEAVEN', value=sentences('thousand_year_day')['v'])]
        if s == 'cain': return [E_('cursed_from_the_ground', subj), E_('fugitive_and_wanderer', subj, value=cain('exile_half')['v'])]
        return []
    if k == 'clothed_in_skins': return [E_('clothed_in_skins', subj, value=sentences('garments_kindness')['v'])]
    if k == 'expelled': return [E_('expelled', subj, value=sentences('divorced_daughter')['v']), E_('way_guarded', 'the-garden')]
    if k == 'bore': return [E_('begotten', event['child'], cp=subj)]
    if k == 'begot': return [E_('begotten', c, cp=subj) for c in event['children']] + ([E_('peleg_named_for_the_division', 'peleg', value=nations('peleg_prophet')['v'])] if 'peleg' in event['children'] else [])
    if k == 'first_offerings_brought': return [E_('regarded', subj, cp='HEAVEN', value=event['what'])] if subj == 'abel' else [E_('not_regarded', subj, value=cain('refuse')['v'][0])]
    if k == 'anger_burned': return []   # the act kept on the tape for the record (6d)
    if k == 'counsel_given': return [E_('sin_at_the_door', subj, value=cain('first_if')['v'])]
    if k == 'killed': return [E_('slain', event['victim'], cp=subj, value=cain('wounds')['v']), E_('bloods_cry', subj, cp='HEAVEN', value=cain('bloods_sheet')['v'])]
    if k == 'mark_promised': return [E_('mark_set', subj, value=cain('mark_arms')['v']), E_('sevenfold_vengeance', subj, cp='HEAVEN')]
    if k == 'went_out_from_the_presence': return [E_('settled_in_nod', subj)]
    if k == 'city_built': return [E_('city_built', event['city'], cp=subj)]
    if k == 'married': return ([E_('wife_taken', subj, cp=event['husband'])] + ([E_('ten_years_childless', 'sarai', value=hagar('ten_years_number')['v'])] if src.startswith('Gen 16:3') else [])) if gen and WE.seat(src)[1] <= 16 else []   # ONE TYPE UNDER TWO LAW LAYERS: Rebekah's (Gen 24) is law_family's, Moses' (Exod 2) law_exodus_story's
    if k == 'lamech_sang': return [E_('seventy_sevenfold_claimed', subj, value=cain('lamech_wives')['v'])]
    if k == 'profanation_begun': return [E_('idolatry_begun', subj, value=cain('rebellion_three')['v'])]
    if k == 'enoch_taken': return [E_('taken_by_god', subj, value=lines('enoch_taken')['v'])]
    if k == 'multiplied': return [E_('multiplied_on_the_earth', subj)]
    if k == 'decree_of_the_reprieve': return [E_('reprieve_of_a_hundred_and_twenty', subj, due=(world.clock.calendar.add(day, event['years'], 'year') if world.clock.epoch else day + 365 * event['years']), value=prologue('reading_row')['v'])]
    if k == 'wickedness_seen': return [E_('wickedness_great', subj, value=prologue('wickedness_great')['v'])] if subj == 'humankind' else [E_('earth_corrupted', subj, value=ark('corrupt_five')['v'])]
    if k == 'regretted': return [E_('regretted_making_man', subj, value=prologue('regret_two')['v'])]
    if k == 'wipe_resolved': return [E_('to_be_wiped', subj, cp='HEAVEN')]
    if k == 'favor_found': return [E_('found_favor', subj, value=prologue('favor_even_noah')['v'])]
    if k == 'end_decreed': return [E_('sealed_for_violence', subj, value=ark('robbery_seals')['v'])]
    if k == 'ark_commanded': return [E_('ark_owed', subj, cp='HEAVEN'), E_('ark_spec', 'the-ark', value=event['dimensions']), E_('covenant_promised', subj, cp='HEAVEN')]
    if k == 'ark_made': return [E_('ark_built', 'the-ark', cp=subj)]
    if k == 'boarding_commanded': return [E_('boarding_owed', subj, cp='HEAVEN'), E_('seven_days_reprieve', 'the-generation-of-the-flood', due=day + event['days'], value=ark('seven_days_arms')['v'])]
    if k == 'entered_the_ark': return [E_('in_the_ark', subj), E_('ark_intercourse_barred', subj, value=ark('intercourse_order')['v'][0]), E_('shut_in', 'noah', cp='HEAVEN')]
    if k == 'flood_came': return [E_('fountains_split', subj, value=flood('eyeball')['v'])]
    if k == 'all_flesh_expired': return [E_('wiped_out', subj, cp='HEAVEN', value=flood('not_the_fish')['v']), E_('only_noah_remained', 'noah'), E_('no_share_in_the_world_to_come', subj, cp='HEAVEN', value=prologue('wipe_two_worlds')['v'])]
    if k == 'waters_prevailed': return [E_('waters_prevailed_a_hundred_and_fifty', subj, value=event['days'])]
    if k == 'remembered': return [E_('remembered_by_god', subj)]
    if k == 'waters_receded': return [E_('waters_receding', subj, value=remembering('boiling')['v'])]
    if k == 'ark_rested': return [E_('rested_on_ararat', subj)]
    if k == 'bird_sent': return [E_('raven_sent', 'the-raven', value=remembering('raven_retort')['v'])] if event['bird'] == 'raven' else [E_('dove_returned', 'the-dove', value=event['result'])]
    if k == 'cover_removed': return [E_('ground_seen_dry', subj)]
    if k == 'exit_commanded': return [E_('exit_owed', subj, cp='HEAVEN'), E_('intercourse_permitted', 'noah-and-sons', value=ark('intercourse_order')['v'][1])]
    if k == 'exited_the_ark': return [E_('out_of_the_ark', subj, value=exit('by_families')['v'])]
    if k == 'altar_erected': return [E_('altar_built', event['at'], cp=subj)]
    if k == 'olah_offered': return [E_('olah_offered', subj, value=exit('olah_by_call')['v'])]
    if k == 'savor_smelled': return [E_('savor_smelled', subj)]
    if k == 'never_again_resolved': return [E_('ground_not_cursed_again', 'the-ground', cp=subj), E_('seasons_pledged', 'the-earth', cp=subj, value=exit('seasons_standing')['v'])]
    if k == 'vineyard_planted': return [E_('vineyard_planted', subj, value=vineyard('profaned')['v'])]
    if k == 'drunk_and_uncovered': return [E_('drunk', subj), E_('uncovered', subj, value=vineyard('same_day')['v'])]
    if k == 'nakedness_seen_and_told': return [E_('saw_and_told', subj, value=vineyard('ham_deed')['v'])]
    if k == 'covered_backward': return [E_('covered_the_father', subj, value=vineyard('shem_began')['v'])]
    if k == 'awoke_and_knew': return []   # the act kept on the tape for the record (6d)
    if k == 'cursed_canaan': return [E_('canaan_cursed', subj, cp=event['by'], value=vineyard('canaan_puzzle')['v'])]
    if k == 'blessed_shem_and_japheth': return [E_('shem_blessed', 'shem', cp=event['by']), E_('japheth_enlarged', 'japheth', cp='HEAVEN', value=vineyard('greek_sheet')['v'])]
    if k == 'kingdom_begun': return [E_('kingdom_founded', subj, value=nations('amraphel')['v'])]
    if k == 'cities_built': return [E_('cities_built', subj, value=nations('cities_four')['v'])]
    if k == 'journeyed': return [E_('encamped_at', subj, value=event['to'])] if gen else []   # ONE TYPE UNDER TWO LAW LAYERS: the Exodus stations are law_exodus_story's
    if k == 'tower_proposed': return [E_('tower_undertaken', subj, value=babel('three_parties')['v'])]
    if k == 'lord_descended': return [E_('descended_to_see', 'the-city-and-tower', value=babel('ten_descents')['v'])] if gen else []   # Sinai's descent is law_exodus_story's
    if k == 'confounded_and_scattered': return [E_('language_confounded', subj), E_('scattered', subj), E_('building_ceased', 'the-city-and-tower', value=babel('thirds')['v']), E_('no_share_in_the_world_to_come', subj, cp='HEAVEN', value=babel('two_scatterings')['v'])]
    if k == 'died': return [E_('died_before_his_father', subj, value=shem_line('haran_furnace')['v'])] if WE.seat(src) == ('Gen', 11) else []   # Sarah's (Gen 23) is law_family's
    if k == 'barren': return [E_('barren', subj)]
    if k == 'call_given': return [E_('go_owed', subj, cp='HEAVEN'), E_('great_nation_promised', subj, cp='HEAVEN', value=call('new_creature')['v']), E_('blessing_promised', subj, cp='HEAVEN', value=call('ladder')['v'])]
    if k == 'went': return []   # the receipt: the scene closes go_owed at 12:4 (6d)
    if k == 'appeared': return []   # the act kept on the tape for the record (6d)
    if k == 'land_promised':
        out = [E_('land_promised', subj, cp='HEAVEN', value=event['seat'])]
        if event['seat'] == '13:15': out += [E_('seed_as_dust', subj, cp='HEAVEN', value=separation('dust')['v']), E_('land_walk_commanded', subj, cp='HEAVEN', value=separation('walk_by_call')['v'])]
        if event['seat'] == '15:7': out += [E_('brought_out_of_ur', subj, value=pieces('furnace')['v'])]
        return out
    if k == 'called_on_the_name': return [E_('called_on_the_name', subj)]
    if k == 'famine_came': return [E_('famine', subj, value=egypt('famine_third')['v'])]
    if k == 'sister_asked': return [E_('presented_as_sister', subj, cp=event['by'])]
    if k == 'woman_taken': return [E_('taken_to_pharaohs_house', subj, cp=event['by'])]
    if k == 'dealt_well': return [E_('enriched_for_her_sake', event['to'], cp=subj, value=egypt('pattern')['v'])]
    if k == 'plagued': return [E_('plague_struck', subj, cp='HEAVEN', value=event['plague'])]
    if k == 'pharaoh_protested': return []   # the act kept on the tape for the record (6d)
    if k == 'sent_away': return [E_('sent_out', 'abram', cp=subj, value=egypt('pattern')['v'])]
    if k == 'strife_arose': return [E_('strife_between_herdsmen', subj, value=separation('muzzled')['v'])]
    if k == 'separation_proposed': return []   # the request: the act closes at 13:11 (6d)
    if k == 'lot_chose': return [E_('chose_the_plain', subj, value=separation('lewdness')['v'])]
    if k == 'separated': return [E_('parted', subj), E_('parted', event['with'])]
    if k == 'sodom_wicked': return [E_('no_share_in_the_world_to_come', subj, cp='HEAVEN', value=separation('sodom_arms')['v'])]
    if k == 'war_waged': return [E_('rebelled', event['against'], value=event['years']), E_('defeated', event['against'], cp=subj)]
    if k == 'lot_taken': return [E_('taken_captive', event['captive'], cp=subj)]
    if k == 'escapee_told': return [E_('called_the_hebrew', 'abram', value=war('hebrew_arms')['v'])]
    if k == 'mustered_and_pursued': return [E_('muster_of_three_hundred_and_eighteen', subj, value=event['count']), E_('night_divided', subj, value=war('night_halves')['v']), E_('kings_smitten', 'the-four-kings', cp=subj)]
    if k == 'brought_back': return [E_('goods_brought_back', 'the-king-of-sodom', cp=subj, value=war('children_not_returned')['v'])]
    if k == 'bread_and_wine_brought': return [E_('bread_and_wine', event['to'], cp=subj), E_('blessed_by_the_priest', event['to'], cp=subj), E_('priesthood_removed', subj, cp=event['to'], value=war('priesthood_from_shem')['v'])]
    if k == 'tithe_given': return [E_('tithe_given', subj, cp=event['to'], value=war('tithe_by_call')['v'])]
    if k == 'kings_demand_refused': return [E_('sworn_to_take_nothing', subj, value=war('raised_hand')['v']), E_('portion_reserved', 'the-allies')]
    if k == 'word_came': return [E_('shield_promised', subj, cp='HEAVEN', value=pieces('two_fears')['v'])]
    if k == 'heir_questioned': return [E_('childless', subj, cp='HEAVEN', value='going childless (15:2) — the steward of my house is my heir')]
    if k == 'heir_declared': return [E_('heir_from_the_loins', subj, cp='HEAVEN')]
    if k == 'stars_shown': return [E_('seed_as_stars', subj, cp='HEAVEN', value=pieces('astrology')['v'])]
    if k == 'believed': return [E_('believed', subj, value=event['in']), E_('reckoned_righteousness', subj, value=pieces('reckoned_both_ways')['v'])] if gen else []   # Exodus' faith clauses are law_exodus_story's
    if k == 'sign_asked': return []   # the act kept on the tape for the record; its ledger weight the decree's cause (Nedarim 32a:15)
    if k == 'pieces_commanded': return [E_('pieces_owed', subj, cp='HEAVEN')]
    if k == 'pieces_cut': return [E_('pieces_cut', 'the-pieces', cp=subj, value=pieces('kingdoms')['v'])]
    if k == 'passed_between_the_pieces': return [E_('passed_between_the_pieces', subj, value=pieces('four_things')['v'])]
    if k == 'decree_of_the_sojourn': return [E_('seed_to_serve_four_hundred', subj, cp='HEAVEN', value=event['years']), E_('nation_to_be_judged', subj, cp='HEAVEN', value=pieces('also_that_nation')['v']), E_('to_go_out_with_substance', subj, cp='HEAVEN'), E_('buried_in_peace', 'abram', cp='HEAVEN'), E_('fourth_generation_return', subj, cp='HEAVEN'), E_('amorite_not_full', 'the-amorite')]
    if k == 'covenant_cut_with_abram': return [E_('covenant_cut', subj, value=ark('covenant_by_call')['v']), E_('land_granted', 'the-seed-of-abraham', value=pieces('ten_nations')['v'])]
    if k == 'hagar_offered': return []   # the request: the act at 16:3-4 (6d)
    if k == 'conceived_and_despised': return [E_('conceived', subj, value=hagar('first_union')['v']), E_('mistress_despised', subj, cp='sarai')]
    if k == 'wrong_claimed': return [E_('judgment_invoked', subj, cp='abram', value=hagar('wrong_with_words')['v'])]
    if k == 'maid_released': return []   # the permission: the affliction's act follows (6d)
    if k == 'afflicted': return [E_('afflicted', event['whom'], cp=subj, value=hagar('affliction_reading')['v'])]
    if k == 'fled': return [E_('fled_from_the_mistress', subj, cp=event['from'])] if gen else []   # Moses' flight (Exod 2:15) is law_exodus_story's
    if k == 'angel_found': return []   # the act kept on the tape for the record (6d)
    if k == 'return_commanded': return [E_('return_owed', subj, cp='the-angel-of-the-lord')]
    if k == 'seed_promised_to_hagar': return [E_('seed_multiplied', subj, cp='HEAVEN')]
    if k == 'ishmael_announced': return [E_('ishmael_announced', subj, cp='HEAVEN', value=hagar('named_before_birth')['v']), E_('wild_ass_of_a_man', 'ishmael', value=hagar('wild_ass')['v'])]
    return []


SLOTS = [   # the slot order of the tuple — fixed by scratchpad o8_s2_predict.py before this file was typed
 ('adam', 'living_soul'), ('adam', 'to_work_and_keep'), ('the-beasts', 'name_given'), ('adam', 'deep_sleep_fell'), ('adam', 'helper_made'), ('eve', 'name_given'), ('eve', 'breached_the_first_rule'), ('adam', 'breached_the_first_rule'),
 ('adam-and-eve', 'eyes_opened'), ('adam-and-eve', 'girdles_made'), ('eve', 'deceived'), ('the-serpent', 'serpent_cursed'), ('the-serpent', 'enmity_set'), ('eve', 'pain_multiplied'), ('eve', 'ruled_by_the_husband'), ('the-ground', 'ground_cursed'),
 ('adam', 'sweat_bread'), ('adam', 'return_to_dust'), ('adam-and-eve', 'clothed_in_skins'), ('adam-and-eve', 'expelled'), ('the-garden', 'way_guarded'), ('cain', 'begotten'), ('abel', 'begotten'), ('cain', 'not_regarded'), ('abel', 'regarded'),
 ('cain', 'sin_at_the_door'), ('abel', 'slain'), ('cain', 'bloods_cry'), ('cain', 'cursed_from_the_ground'), ('cain', 'fugitive_and_wanderer'), ('cain', 'mark_set'), ('cain', 'sevenfold_vengeance'), ('cain', 'settled_in_nod'),
 ('enoch-son-of-cain', 'begotten'), ('the-city-of-enoch', 'city_built'), ('the-city-of-enoch', 'name_given'), ('irad', 'begotten'), ('mehujael', 'begotten'), ('methushael', 'begotten'), ('lamech-son-of-methushael', 'begotten'),
 ('adah', 'wife_taken'), ('zillah', 'wife_taken'), ('jabal', 'begotten'), ('tubal-cain', 'begotten'), ('lamech-son-of-methushael', 'seventy_sevenfold_claimed'), ('seth', 'begotten'), ('seth', 'name_given'), ('enosh', 'name_given'),
 ('the-generation-of-enosh', 'idolatry_begun'), ('adam-and-eve', 'name_given'), ('enosh', 'begotten'), ('kenan', 'begotten'), ('mahalalel', 'begotten'), ('jared', 'begotten'), ('enoch', 'begotten'), ('methuselah', 'begotten'),
 ('lamech', 'begotten'), ('enoch', 'taken_by_god'), ('noah', 'begotten'), ('noah', 'name_given'), ('shem', 'begotten'), ('ham', 'begotten'), ('japheth', 'begotten'), ('humankind', 'multiplied_on_the_earth'),
 ('the-daughters-of-men', 'wife_taken'), ('humankind', 'wickedness_great'), ('god', 'regretted_making_man'), ('the-generation-of-the-flood', 'to_be_wiped'), ('noah', 'found_favor'), ('the-earth', 'earth_corrupted'),
 ('the-generation-of-the-flood', 'sealed_for_violence'), ('noah', 'ark_owed'), ('the-ark', 'ark_spec'), ('noah', 'covenant_promised'), ('the-ark', 'ark_built'), ('noah', 'boarding_owed'), ('the-generation-of-the-flood', 'seven_days_reprieve'),
 ('noah-and-sons', 'in_the_ark'), ('noah-and-sons', 'ark_intercourse_barred'), ('noah', 'shut_in'), ('the-earth', 'fountains_split'), ('the-generation-of-the-flood', 'wiped_out'), ('noah', 'only_noah_remained'),
 ('the-generation-of-the-flood', 'no_share_in_the_world_to_come'), ('the-earth', 'waters_prevailed_a_hundred_and_fifty'), ('noah', 'remembered_by_god'), ('the-earth', 'waters_receding'), ('the-ark', 'rested_on_ararat'), ('the-raven', 'raven_sent'),
 ('the-dove', 'dove_returned'), ('noah', 'ground_seen_dry'), ('noah', 'exit_owed'), ('noah-and-sons', 'intercourse_permitted'), ('noah-and-sons', 'out_of_the_ark'), ('the-altar-of-noah', 'altar_built'), ('noah', 'olah_offered'),
 ('god', 'savor_smelled'), ('the-ground', 'ground_not_cursed_again'), ('the-earth', 'seasons_pledged'), ('noah', 'vineyard_planted'), ('noah', 'drunk'), ('noah', 'uncovered'), ('ham', 'saw_and_told'), ('shem-and-japheth', 'covered_the_father'),
 ('canaan', 'canaan_cursed'), ('shem', 'shem_blessed'), ('japheth', 'japheth_enlarged'), ('nimrod', 'begotten'), ('nimrod', 'kingdom_founded'), ('asshur', 'cities_built'), ('peleg', 'begotten'), ('joktan', 'begotten'),
 ('peleg', 'peleg_named_for_the_division'), ('the-builders', 'encamped_at'), ('the-builders', 'tower_undertaken'), ('the-city-and-tower', 'descended_to_see'), ('the-builders', 'language_confounded'), ('the-builders', 'scattered'),
 ('the-city-and-tower', 'building_ceased'), ('the-builders', 'no_share_in_the_world_to_come'), ('the-city-and-tower', 'name_given'), ('arpachshad', 'begotten'), ('shelah', 'begotten'), ('eber', 'begotten'), ('reu', 'begotten'),
 ('serug', 'begotten'), ('nahor', 'begotten'), ('terah', 'begotten'), ('abram', 'begotten'), ('nahor-son-of-terah', 'begotten'), ('haran', 'begotten'), ('lot', 'begotten'), ('haran', 'died_before_his_father'), ('sarai', 'wife_taken'),
 ('milcah', 'wife_taken'), ('sarai', 'barren'), ('terah', 'encamped_at'), ('abram', 'go_owed'), ('abram', 'great_nation_promised'), ('abram', 'blessing_promised'), ('abram', 'encamped_at'), ('abram', 'land_promised'),
 ('the-altar-at-shechem', 'altar_built'), ('the-altar-at-bethel', 'altar_built'), ('abram', 'called_on_the_name'), ('the-land-of-canaan', 'famine'), ('sarai', 'presented_as_sister'), ('sarai', 'taken_to_pharaohs_house'),
 ('abram', 'enriched_for_her_sake'), ('pharaoh-of-abram', 'plague_struck'), ('abram', 'sent_out'), ('the-herdsmen', 'strife_between_herdsmen'), ('lot', 'chose_the_plain'), ('abram', 'parted'), ('lot', 'parted'), ('lot', 'encamped_at'),
 ('the-men-of-sodom', 'no_share_in_the_world_to_come'), ('abram', 'seed_as_dust'), ('abram', 'land_walk_commanded'), ('the-altar-at-hebron', 'altar_built'), ('the-five-kings', 'rebelled'), ('the-five-kings', 'defeated'), ('lot', 'taken_captive'),
 ('abram', 'called_the_hebrew'), ('abram', 'muster_of_three_hundred_and_eighteen'), ('abram', 'night_divided'), ('the-four-kings', 'kings_smitten'), ('the-king-of-sodom', 'goods_brought_back'), ('abram', 'bread_and_wine'), ('abram', 'blessed_by_the_priest'),
 ('melchizedek', 'priesthood_removed'), ('abram', 'tithe_given'), ('abram', 'sworn_to_take_nothing'), ('the-allies', 'portion_reserved'), ('abram', 'shield_promised'), ('abram', 'childless'), ('abram', 'heir_from_the_loins'),
 ('abram', 'seed_as_stars'), ('abram', 'believed'), ('abram', 'reckoned_righteousness'), ('abram', 'brought_out_of_ur'), ('abram', 'pieces_owed'), ('the-pieces', 'pieces_cut'), ('abram', 'deep_sleep_fell'), ('abram', 'dread_and_darkness'),
 ('the-seed-of-abraham', 'seed_to_serve_four_hundred'), ('the-seed-of-abraham', 'nation_to_be_judged'), ('the-seed-of-abraham', 'to_go_out_with_substance'), ('abram', 'buried_in_peace'), ('the-seed-of-abraham', 'fourth_generation_return'),
 ('the-amorite', 'amorite_not_full'), ('the-pieces', 'passed_between_the_pieces'), ('abram', 'covenant_cut'), ('the-seed-of-abraham', 'land_granted'), ('hagar', 'wife_taken'), ('sarai', 'ten_years_childless'), ('hagar', 'conceived'),
 ('hagar', 'mistress_despised'), ('sarai', 'judgment_invoked'), ('hagar', 'afflicted'), ('hagar', 'fled_from_the_mistress'), ('hagar', 'return_owed'), ('hagar', 'seed_multiplied'), ('hagar', 'ishmael_announced'), ('ishmael', 'wild_ass_of_a_man'),
 ('god', 'name_given'), ('the-well-lachai-roi', 'name_given'), ('ishmael', 'begotten'), ('ishmael', 'name_given'),
]
LEDGER5 = [('adam', ['seth'], 'Gen 5:3'), ('seth', ['enosh'], 'Gen 5:6'), ('enosh', ['kenan'], 'Gen 5:9'), ('kenan', ['mahalalel'], 'Gen 5:12'), ('mahalalel', ['jared'], 'Gen 5:15'), ('jared', ['enoch'], 'Gen 5:18'),
           ('enoch', ['methuselah'], 'Gen 5:21'), ('methuselah', ['lamech'], 'Gen 5:25'), ('lamech', ['noah'], 'Gen 5:28')]
LEDGER11 = [('shem', ['arpachshad'], 'Gen 11:10'), ('arpachshad', ['shelah'], 'Gen 11:12; Gen 10:24'), ('shelah', ['eber'], 'Gen 11:14; Gen 10:24'), ('peleg', ['reu'], 'Gen 11:18'), ('reu', ['serug'], 'Gen 11:20'),
            ('serug', ['nahor'], 'Gen 11:22'), ('nahor', ['terah'], 'Gen 11:24'), ('terah', ['abram', 'nahor-son-of-terah', 'haran'], 'Gen 11:26; Gen 11:27')]


def scene():
    """THE SCENE — the stretch's acts on a bare world in the text's order (scene days; the tape carries the ink's markers)"""
    closes = [0]
    def close(eid, eff, note, value=None):
        closes[0] += bool(w.close(eid, eff, note, value=value))
    with contextlib.redirect_stdout(io.StringIO()):
        w = WE.World(era='FROM EDEN TO HAGAR — Genesis 2:4-16:16 (clock unit: days; the tape\'s own order)')
        w.laws = [law_primeval]   # no birth of the stretch is under the covenant of Gen 17: the pre-Sinai daemon is not registered here (on the tape it watches and does not fire)
        w.advance(1)   # ---- Gen 2 ----
        w.submit({'kind': 'formed_from_dust', 'subject': 'adam', 'case_source': 'Gen 2:7'})
        w.submit({'kind': 'placed_in_the_garden', 'subject': 'adam', 'case_source': 'Gen 2:8; Gen 2:15'})
        w.submit({'kind': 'named', 'subject': 'the-beasts', 'name': 'the names of all cattle, the fowl of the heavens and every beast of the field (2:20)', 'by': 'adam', 'case_source': 'Gen 2:20'})
        w.submit({'kind': 'deep_sleep_fell', 'subject': 'adam', 'kind_of_sleep': 'the deep sleep of sleep (Bereshit Rabbah 17:5)', 'case_source': 'Gen 2:21'})
        w.submit({'kind': 'woman_built', 'subject': 'adam', 'case_source': 'Gen 2:21-22; Gen 2:18'})
        w.submit({'kind': 'named', 'subject': 'eve', 'name': 'Woman (אשה — for from man she was taken, 2:23)', 'by': 'adam', 'case_source': 'Gen 2:23'})
        w.advance(2)   # ---- Gen 3 ----
        w.submit({'kind': 'serpent_spoke', 'subject': 'the-serpent', 'to': 'eve', 'case_source': 'Gen 3:1; Gen 3:4-5'})
        w.submit({'kind': 'ate_of_the_tree', 'subject': 'eve', 'gave_to': 'adam', 'case_source': 'Gen 3:6; Gen 2:16-17'})
        w.submit({'kind': 'eyes_opened', 'subject': 'adam-and-eve', 'case_source': 'Gen 3:7'})
        w.submit({'kind': 'hid_from_the_voice', 'subject': 'adam-and-eve', 'case_source': 'Gen 3:8'})
        w.submit({'kind': 'interrogated', 'subject': 'adam-and-eve', 'case_source': 'Gen 3:9-13'})
        w.submit({'kind': 'sentenced', 'subject': 'the-serpent', 'sentence': 'serpent', 'case_source': 'Gen 3:14-15'})
        w.submit({'kind': 'sentenced', 'subject': 'eve', 'sentence': 'woman', 'case_source': 'Gen 3:16'})
        w.submit({'kind': 'sentenced', 'subject': 'adam', 'sentence': 'man', 'case_source': 'Gen 3:17-19'})
        w.submit({'kind': 'named', 'subject': 'eve', 'name': 'Eve (חוה — the mother of all living, 3:20)', 'by': 'adam', 'case_source': 'Gen 3:20'})
        w.submit({'kind': 'clothed_in_skins', 'subject': 'adam-and-eve', 'case_source': 'Gen 3:21'})
        w.submit({'kind': 'expelled', 'subject': 'adam-and-eve', 'case_source': 'Gen 3:23-24'})
        w.advance(3)   # ---- Gen 4 ----
        w.submit({'kind': 'bore', 'subject': 'eve', 'child': 'cain', 'case_source': 'Gen 4:1'})
        w.submit({'kind': 'bore', 'subject': 'eve', 'child': 'abel', 'case_source': 'Gen 4:2'})
        w.submit({'kind': 'first_offerings_brought', 'subject': 'cain', 'what': 'of the fruit of the ground (4:3)', 'case_source': 'Gen 4:3'})
        w.submit({'kind': 'first_offerings_brought', 'subject': 'abel', 'what': 'of the firstlings of his flock and of their fat (4:4)', 'case_source': 'Gen 4:4'})
        w.submit({'kind': 'anger_burned', 'subject': 'cain', 'case_source': 'Gen 4:5'})
        w.submit({'kind': 'counsel_given', 'subject': 'cain', 'case_source': 'Gen 4:6-7'})
        w.submit({'kind': 'killed', 'subject': 'cain', 'victim': 'abel', 'case_source': 'Gen 4:8'})
        w.submit({'kind': 'sentenced', 'subject': 'cain', 'sentence': 'cain', 'case_source': 'Gen 4:11-12'})
        w.submit({'kind': 'mark_promised', 'subject': 'cain', 'case_source': 'Gen 4:15'})
        w.submit({'kind': 'went_out_from_the_presence', 'subject': 'cain', 'case_source': 'Gen 4:16'})
        w.submit({'kind': 'bore', 'subject': 'cains-wife', 'child': 'enoch-son-of-cain', 'case_source': 'Gen 4:17'})
        w.submit({'kind': 'city_built', 'subject': 'cain', 'city': 'the-city-of-enoch', 'case_source': 'Gen 4:17'})
        w.submit({'kind': 'named', 'subject': 'the-city-of-enoch', 'name': 'Enoch (after his son, 4:17)', 'by': 'cain', 'case_source': 'Gen 4:17'})
        for f, c in (('enoch-son-of-cain', 'irad'), ('irad', 'mehujael'), ('mehujael', 'methushael'), ('methushael', 'lamech-son-of-methushael')):
            w.submit({'kind': 'begot', 'subject': f, 'children': [c], 'case_source': 'Gen 4:18'})
        w.submit({'kind': 'married', 'subject': 'adah', 'husband': 'lamech-son-of-methushael', 'case_source': 'Gen 4:19'})
        w.submit({'kind': 'married', 'subject': 'zillah', 'husband': 'lamech-son-of-methushael', 'case_source': 'Gen 4:19'})
        w.submit({'kind': 'bore', 'subject': 'adah', 'child': 'jabal', 'case_source': 'Gen 4:20'})
        w.submit({'kind': 'bore', 'subject': 'zillah', 'child': 'tubal-cain', 'case_source': 'Gen 4:22'})
        w.submit({'kind': 'lamech_sang', 'subject': 'lamech-son-of-methushael', 'case_source': 'Gen 4:23-24'})
        w.submit({'kind': 'bore', 'subject': 'eve', 'child': 'seth', 'case_source': 'Gen 4:25'})
        w.submit({'kind': 'named', 'subject': 'seth', 'name': 'Seth (שת — God has set me another seed, 4:25)', 'by': 'eve', 'case_source': 'Gen 4:25'})
        w.submit({'kind': 'named', 'subject': 'enosh', 'name': 'Enosh (4:26)', 'by': 'seth', 'case_source': 'Gen 4:26'})
        w.submit({'kind': 'profanation_begun', 'subject': 'the-generation-of-enosh', 'case_source': 'Gen 4:26'})
        w.advance(4)   # ---- Gen 5 ----
        w.submit({'kind': 'named', 'subject': 'adam-and-eve', 'name': 'Adam (5:2 — their name, male and female)', 'by': 'god', 'case_source': 'Gen 5:2'})
        for f, cs, src in LEDGER5:
            w.submit({'kind': 'begot', 'subject': f, 'children': cs, 'case_source': src})
            if f == 'adam': w.submit({'kind': 'named', 'subject': 'seth', 'name': 'Seth (5:3 — by his father)', 'by': 'adam', 'case_source': 'Gen 5:3'})
            if f == 'jared': pass
        w.submit({'kind': 'enoch_taken', 'subject': 'enoch', 'case_source': 'Gen 5:24'})
        w.submit({'kind': 'named', 'subject': 'noah', 'name': 'Noah (נח — this one shall comfort us, 5:29)', 'by': 'lamech', 'case_source': 'Gen 5:29'})
        w.submit({'kind': 'begot', 'subject': 'noah', 'children': ['shem', 'ham', 'japheth'], 'case_source': 'Gen 5:32; Gen 6:10'})
        w.advance(5)   # ---- Gen 6:1-8 ----
        w.submit({'kind': 'multiplied', 'subject': 'humankind', 'case_source': 'Gen 6:1'})
        w.submit({'kind': 'married', 'subject': 'the-daughters-of-men', 'husband': 'the-sons-of-god', 'case_source': 'Gen 6:2'})
        w.submit({'kind': 'decree_of_the_reprieve', 'subject': 'the-generation-of-the-flood', 'years': 120, 'case_source': 'Gen 6:3'})   # the timer: due beyond the bare scene's end (set, not fired); on the tape retrograde-dated at the flood minus 120
        w.submit({'kind': 'wickedness_seen', 'subject': 'humankind', 'case_source': 'Gen 6:5'})
        w.submit({'kind': 'regretted', 'subject': 'god', 'case_source': 'Gen 6:6'})
        w.submit({'kind': 'wipe_resolved', 'subject': 'the-generation-of-the-flood', 'case_source': 'Gen 6:7'})
        w.submit({'kind': 'favor_found', 'subject': 'noah', 'case_source': 'Gen 6:8'})
        w.advance(6)   # ---- Gen 6:9-22 ----
        w.submit({'kind': 'wickedness_seen', 'subject': 'the-earth', 'case_source': 'Gen 6:11-12'})
        w.submit({'kind': 'end_decreed', 'subject': 'the-generation-of-the-flood', 'case_source': 'Gen 6:13'})
        w.submit({'kind': 'ark_commanded', 'subject': 'noah', 'dimensions': (300, 50, 30), 'case_source': 'Gen 6:14-21'})
        w.submit({'kind': 'ark_made', 'subject': 'noah', 'case_source': 'Gen 6:22'})
        close('noah', 'ark_owed', 'Gen 6:22 — and Noah did according to all that God commanded him, so he did')
        w.advance(7)   # ---- Gen 7:1-4 ----
        w.submit({'kind': 'boarding_commanded', 'subject': 'noah', 'days': 7, 'case_source': 'Gen 7:1-4'})   # the seven days: the timer at day 14
        w.advance(14)  # ---- Gen 7:7-16: the flood's day (the timer FIRES) ----
        w.submit({'kind': 'entered_the_ark', 'subject': 'noah-and-sons', 'case_source': 'Gen 7:7; Gen 7:13; Gen 7:15-16'})
        close('noah', 'boarding_owed', 'Gen 7:7 — and Noah came into the ark')
        w.submit({'kind': 'flood_came', 'subject': 'the-earth', 'case_source': 'Gen 7:11; Gen 7:17-18'})
        w.advance(54)  # ---- Gen 7:17-24: the forty days ----
        w.submit({'kind': 'all_flesh_expired', 'subject': 'the-generation-of-the-flood', 'case_source': 'Gen 7:21-23'})
        close('the-generation-of-the-flood', 'to_be_wiped', 'Gen 7:23 — and He wiped out every living thing (Sanhedrin 108a:5)')
        w.submit({'kind': 'waters_prevailed', 'subject': 'the-earth', 'days': 150, 'case_source': 'Gen 7:24; Gen 7:18-20'})
        w.advance(164)  # ---- Gen 8:1-5: the hundred and fifty days ----
        w.submit({'kind': 'remembered', 'subject': 'noah', 'case_source': 'Gen 8:1'})
        w.submit({'kind': 'waters_receded', 'subject': 'the-earth', 'case_source': 'Gen 8:1-3'})
        w.submit({'kind': 'ark_rested', 'subject': 'the-ark', 'case_source': 'Gen 8:4'})
        w.advance(250)  # ---- Gen 8:6-12: the window and the birds ----
        w.submit({'kind': 'bird_sent', 'subject': 'noah', 'bird': 'raven', 'sending': 1, 'result': 'went to and fro (8:7)', 'case_source': 'Gen 8:7'})
        w.submit({'kind': 'bird_sent', 'subject': 'noah', 'bird': 'dove', 'sending': 1, 'result': 'returned — found no rest (8:9)', 'case_source': 'Gen 8:8-9'})
        w.submit({'kind': 'bird_sent', 'subject': 'noah', 'bird': 'dove', 'sending': 2, 'result': 'the olive leaf (8:11)', 'case_source': 'Gen 8:10-11'})
        w.submit({'kind': 'bird_sent', 'subject': 'noah', 'bird': 'dove', 'sending': 3, 'result': 'did not return (8:12)', 'case_source': 'Gen 8:12'})
        w.advance(300)  # ---- Gen 8:13-14 ----
        w.submit({'kind': 'cover_removed', 'subject': 'noah', 'case_source': 'Gen 8:13'})
        w.advance(356)  # ---- Gen 8:15-22 ----
        w.submit({'kind': 'exit_commanded', 'subject': 'noah', 'case_source': 'Gen 8:15-17'})
        w.submit({'kind': 'exited_the_ark', 'subject': 'noah-and-sons', 'case_source': 'Gen 8:18-19'})
        close('noah', 'exit_owed', 'Gen 8:18 — and Noah went out')
        w.submit({'kind': 'altar_erected', 'subject': 'noah', 'at': 'the-altar-of-noah', 'case_source': 'Gen 8:20'})
        w.submit({'kind': 'olah_offered', 'subject': 'noah', 'case_source': 'Gen 8:20; Gen 7:2'})
        w.submit({'kind': 'savor_smelled', 'subject': 'god', 'case_source': 'Gen 8:21'})
        w.submit({'kind': 'never_again_resolved', 'subject': 'god', 'case_source': 'Gen 8:21-22'})
        close('noah', 'covenant_promised', 'Gen 9:11 — and I will establish My covenant with you (the pre-Sinai engine\'s act; the promise of 6:18 kept)')
        w.advance(357)  # ---- Gen 9:18-29 ----
        w.submit({'kind': 'vineyard_planted', 'subject': 'noah', 'case_source': 'Gen 9:20'})
        w.submit({'kind': 'drunk_and_uncovered', 'subject': 'noah', 'case_source': 'Gen 9:21'})
        w.submit({'kind': 'nakedness_seen_and_told', 'subject': 'ham', 'case_source': 'Gen 9:22'})
        w.submit({'kind': 'covered_backward', 'subject': 'shem-and-japheth', 'case_source': 'Gen 9:23'})
        w.submit({'kind': 'awoke_and_knew', 'subject': 'noah', 'case_source': 'Gen 9:24'})
        w.submit({'kind': 'cursed_canaan', 'subject': 'canaan', 'by': 'noah', 'case_source': 'Gen 9:25'})
        w.submit({'kind': 'blessed_shem_and_japheth', 'subject': 'shem', 'by': 'noah', 'case_source': 'Gen 9:26-27'})
        w.advance(358)  # ---- Gen 10 ----
        w.submit({'kind': 'begot', 'subject': 'cush', 'children': ['nimrod'], 'case_source': 'Gen 10:8; Gen 10:10'})   # 10:10 cited second for the tape's register test: 10:8's 'begot' is a qatal and the window looks back ten verses over a table with no narrative verb (a finding); the position stays 10:8
        w.submit({'kind': 'kingdom_begun', 'subject': 'nimrod', 'case_source': 'Gen 10:10; Gen 10:8-9'})
        w.submit({'kind': 'cities_built', 'subject': 'asshur', 'case_source': 'Gen 10:11-12'})
        w.submit({'kind': 'begot', 'subject': 'eber', 'children': ['peleg', 'joktan'], 'case_source': 'Gen 10:25; Gen 11:16'})
        w.advance(359)  # ---- Gen 11:1-9 ----
        w.submit({'kind': 'journeyed', 'subject': 'the-builders', 'to': 'the plain in the land of Shinar', 'case_source': 'Gen 11:2'})
        w.submit({'kind': 'tower_proposed', 'subject': 'the-builders', 'case_source': 'Gen 11:3-4'})
        w.submit({'kind': 'lord_descended', 'subject': 'god', 'case_source': 'Gen 11:5'})
        w.submit({'kind': 'confounded_and_scattered', 'subject': 'the-builders', 'case_source': 'Gen 11:7-9'})
        w.submit({'kind': 'named', 'subject': 'the-city-and-tower', 'name': 'Babel (בבל — for there the LORD confounded, 11:9)', 'by': 'the-builders', 'case_source': 'Gen 11:9'})
        w.advance(360)  # ---- Gen 11:10-32 ----
        for f, cs, src in LEDGER11:
            w.submit({'kind': 'begot', 'subject': f, 'children': cs, 'case_source': src})
        w.submit({'kind': 'begot', 'subject': 'haran', 'children': ['lot'], 'case_source': 'Gen 11:27'})
        w.submit({'kind': 'died', 'subject': 'haran', 'dead': 'haran', 'case_source': 'Gen 11:28'})
        w.submit({'kind': 'married', 'subject': 'sarai', 'husband': 'abram', 'case_source': 'Gen 11:29'})
        w.submit({'kind': 'married', 'subject': 'milcah', 'husband': 'nahor-son-of-terah', 'case_source': 'Gen 11:29'})
        w.submit({'kind': 'barren', 'subject': 'sarai', 'case_source': 'Gen 11:30'})
        w.submit({'kind': 'journeyed', 'subject': 'terah', 'to': 'Haran', 'case_source': 'Gen 11:31'})
        w.advance(361)  # ---- Gen 12:1-9 ----
        w.submit({'kind': 'call_given', 'subject': 'abram', 'case_source': 'Gen 12:1-3'})
        w.submit({'kind': 'went', 'subject': 'abram', 'case_source': 'Gen 12:4-5'})
        close('abram', 'go_owed', 'Gen 12:4 — and Abram went as the LORD had spoken to him')
        w.submit({'kind': 'journeyed', 'subject': 'abram', 'to': 'the land of Canaan', 'case_source': 'Gen 12:5'})
        w.submit({'kind': 'journeyed', 'subject': 'abram', 'to': 'the place of Shechem', 'case_source': 'Gen 12:6'})
        w.submit({'kind': 'appeared', 'subject': 'god', 'to': 'abram', 'case_source': 'Gen 12:7'})
        w.submit({'kind': 'land_promised', 'subject': 'abram', 'seat': '12:7', 'case_source': 'Gen 12:7'})
        w.submit({'kind': 'altar_erected', 'subject': 'abram', 'at': 'the-altar-at-shechem', 'case_source': 'Gen 12:7'})
        w.submit({'kind': 'journeyed', 'subject': 'abram', 'to': 'the mountain east of Bethel', 'case_source': 'Gen 12:8'})
        w.submit({'kind': 'altar_erected', 'subject': 'abram', 'at': 'the-altar-at-bethel', 'case_source': 'Gen 12:8'})
        w.submit({'kind': 'called_on_the_name', 'subject': 'abram', 'case_source': 'Gen 12:8'})
        w.submit({'kind': 'journeyed', 'subject': 'abram', 'to': 'the Negev', 'case_source': 'Gen 12:9'})
        w.advance(362)  # ---- Gen 12:10-20 ----
        w.submit({'kind': 'famine_came', 'subject': 'the-land-of-canaan', 'case_source': 'Gen 12:10'})
        w.submit({'kind': 'journeyed', 'subject': 'abram', 'to': 'Egypt', 'case_source': 'Gen 12:10'})
        w.submit({'kind': 'sister_asked', 'subject': 'sarai', 'by': 'abram', 'case_source': 'Gen 12:11-13'})
        w.submit({'kind': 'woman_taken', 'subject': 'sarai', 'by': 'pharaoh-of-abram', 'case_source': 'Gen 12:15; Gen 12:14'})
        w.submit({'kind': 'dealt_well', 'subject': 'pharaoh-of-abram', 'to': 'abram', 'case_source': 'Gen 12:16'})
        w.submit({'kind': 'plagued', 'subject': 'pharaoh-of-abram', 'plague': 'great plagues (12:17 — ra\'atan, Bereshit Rabbah 41:2)', 'case_source': 'Gen 12:17'})
        w.submit({'kind': 'pharaoh_protested', 'subject': 'pharaoh-of-abram', 'case_source': 'Gen 12:18-19'})
        w.submit({'kind': 'sent_away', 'subject': 'pharaoh-of-abram', 'case_source': 'Gen 12:20'})
        close('sarai', 'taken_to_pharaohs_house', 'Gen 12:20 — and they sent him away, and his wife')
        w.advance(363)  # ---- Gen 13 ----
        w.submit({'kind': 'journeyed', 'subject': 'abram', 'to': 'Bethel again, the place of the altar', 'case_source': 'Gen 13:1-3'})
        w.submit({'kind': 'called_on_the_name', 'subject': 'abram', 'case_source': 'Gen 13:4'})
        w.submit({'kind': 'strife_arose', 'subject': 'the-herdsmen', 'case_source': 'Gen 13:7; Gen 13:5-6'})
        w.submit({'kind': 'separation_proposed', 'subject': 'abram', 'case_source': 'Gen 13:8-9'})
        w.submit({'kind': 'lot_chose', 'subject': 'lot', 'case_source': 'Gen 13:10-11'})
        w.submit({'kind': 'separated', 'subject': 'abram', 'with': 'lot', 'case_source': 'Gen 13:11-12'})
        w.submit({'kind': 'journeyed', 'subject': 'lot', 'to': 'the cities of the plain, his tent to Sodom', 'case_source': 'Gen 13:12'})
        w.submit({'kind': 'sodom_wicked', 'subject': 'the-men-of-sodom', 'case_source': 'Gen 13:13'})
        w.submit({'kind': 'land_promised', 'subject': 'abram', 'seat': '13:15', 'case_source': 'Gen 13:14-17'})
        w.submit({'kind': 'journeyed', 'subject': 'abram', 'to': 'the terebinths of Mamre at Hebron', 'case_source': 'Gen 13:18'})
        w.submit({'kind': 'altar_erected', 'subject': 'abram', 'at': 'the-altar-at-hebron', 'case_source': 'Gen 13:18'})
        w.advance(364)  # ---- Gen 14 ----
        w.submit({'kind': 'war_waged', 'subject': 'the-four-kings', 'against': 'the-five-kings', 'years': (12, 13, 14), 'case_source': 'Gen 14:1-2; Gen 14:4-11'})
        w.submit({'kind': 'lot_taken', 'subject': 'the-four-kings', 'captive': 'lot', 'case_source': 'Gen 14:12'})
        w.submit({'kind': 'escapee_told', 'subject': 'the-escapee', 'case_source': 'Gen 14:13'})
        w.submit({'kind': 'mustered_and_pursued', 'subject': 'abram', 'count': 318, 'case_source': 'Gen 14:14-15'})
        w.submit({'kind': 'brought_back', 'subject': 'abram', 'case_source': 'Gen 14:16'})
        close('lot', 'taken_captive', 'Gen 14:16 — and also Lot his brother and his goods he brought back')
        w.submit({'kind': 'bread_and_wine_brought', 'subject': 'melchizedek', 'to': 'abram', 'case_source': 'Gen 14:18-20'})
        w.submit({'kind': 'tithe_given', 'subject': 'abram', 'to': 'melchizedek', 'case_source': 'Gen 14:20'})
        w.submit({'kind': 'kings_demand_refused', 'subject': 'abram', 'case_source': 'Gen 14:21-24'})
        w.advance(365)  # ---- Gen 15 ----
        w.submit({'kind': 'word_came', 'subject': 'abram', 'case_source': 'Gen 15:1; Gen 15:2'})   # 15:2 cited second for the tape's register test: 15:1's 'the word of the LORD came' is a qatal and the window stays inside the chapter (a finding — S1's 15:1 the same shape); the position stays 15:1
        w.submit({'kind': 'heir_questioned', 'subject': 'abram', 'case_source': 'Gen 15:2-3'})
        w.submit({'kind': 'heir_declared', 'subject': 'abram', 'case_source': 'Gen 15:4'})
        w.submit({'kind': 'stars_shown', 'subject': 'abram', 'case_source': 'Gen 15:5'})
        w.submit({'kind': 'believed', 'subject': 'abram', 'in': 'the LORD (15:6)', 'case_source': 'Gen 15:6'})
        w.submit({'kind': 'land_promised', 'subject': 'abram', 'seat': '15:7', 'case_source': 'Gen 15:7'})
        w.submit({'kind': 'sign_asked', 'subject': 'abram', 'case_source': 'Gen 15:8'})
        w.submit({'kind': 'pieces_commanded', 'subject': 'abram', 'case_source': 'Gen 15:9'})
        w.submit({'kind': 'pieces_cut', 'subject': 'abram', 'case_source': 'Gen 15:10-11'})
        close('abram', 'pieces_owed', 'Gen 15:10 — and he took him all these')
        w.submit({'kind': 'deep_sleep_fell', 'subject': 'abram', 'kind_of_sleep': 'the deep sleep of prophecy (Bereshit Rabbah 44:17)', 'case_source': 'Gen 15:12'})
        w.submit({'kind': 'decree_of_the_sojourn', 'subject': 'the-seed-of-abraham', 'years': 400, 'case_source': 'Gen 15:13-16'})
        w.submit({'kind': 'passed_between_the_pieces', 'subject': 'the-pieces', 'case_source': 'Gen 15:17'})
        w.submit({'kind': 'covenant_cut_with_abram', 'subject': 'abram', 'case_source': 'Gen 15:18-21'})
        for _ in range(3): close('abram', 'land_promised', 'Gen 15:18 — to your seed I HAVE GIVEN this land (the perfect: the three promises kept)')
        w.advance(366)  # ---- Gen 16 ----
        w.submit({'kind': 'hagar_offered', 'subject': 'sarai', 'case_source': 'Gen 16:2'})
        w.submit({'kind': 'married', 'subject': 'hagar', 'husband': 'abram', 'case_source': 'Gen 16:3'})
        w.submit({'kind': 'conceived_and_despised', 'subject': 'hagar', 'case_source': 'Gen 16:4'})
        w.submit({'kind': 'wrong_claimed', 'subject': 'sarai', 'case_source': 'Gen 16:5'})
        w.submit({'kind': 'maid_released', 'subject': 'sarai', 'case_source': 'Gen 16:6'})
        w.submit({'kind': 'afflicted', 'subject': 'sarai', 'whom': 'hagar', 'case_source': 'Gen 16:6'})
        w.submit({'kind': 'fled', 'subject': 'hagar', 'from': 'sarai', 'case_source': 'Gen 16:6; Gen 16:8'})
        w.submit({'kind': 'angel_found', 'subject': 'the-angel-of-the-lord', 'whom': 'hagar', 'case_source': 'Gen 16:7-8'})
        w.submit({'kind': 'return_commanded', 'subject': 'hagar', 'case_source': 'Gen 16:9'})
        w.submit({'kind': 'seed_promised_to_hagar', 'subject': 'hagar', 'case_source': 'Gen 16:10'})
        w.submit({'kind': 'ishmael_announced', 'subject': 'hagar', 'case_source': 'Gen 16:11-12'})
        w.submit({'kind': 'named', 'subject': 'god', 'name': 'You are a God of seeing (אל ראי, 16:13)', 'by': 'hagar', 'case_source': 'Gen 16:13'})
        w.submit({'kind': 'named', 'subject': 'the-well-lachai-roi', 'name': 'Beer-lahai-roi (16:14)', 'by': 'hagar', 'case_source': 'Gen 16:14'})
        w.submit({'kind': 'bore', 'subject': 'hagar', 'child': 'ishmael', 'case_source': 'Gen 16:15'})
        close('hagar', 'ishmael_announced', 'Gen 16:15 — and Hagar bore Abram a son')
        close('abram', 'childless', 'Gen 16:15 — a son born to Abram')
        w.submit({'kind': 'named', 'subject': 'ishmael', 'name': 'Ishmael (ישמעאל — for the LORD has heard, 16:11, 16:15)', 'by': 'abram', 'case_source': 'Gen 16:15'})
    n = lambda eid, eff: len([e for e in w.entity(eid).ledger if e['effect'] == eff])
    open_total = sum(len(ent.open_entries()) for ent in w.entities.values())
    tset = len([l for l in w.log if l[0] == 'TIMER-SET']); fired = len([l for l in w.log if l[0] == 'TIMER-FIRE'])
    return tuple(n(eid, eff) for eid, eff in SLOTS) + (open_total, tset, fired, closes[0], w.clock.day), w
SCENE, _W = scene()


def build(q):
    if q == 'world':
        return cell(SCENE, I, "THE SCENE on the world engine — the two hundred and nine effect slots of the declaration in order (the garden's statuses, the breach on two, the four sentences, the garments and the exile, the births of Gen 4 with the offerings, the killing and the bloods, Cain's four, the line of Cain and Lamech's song, the ledger's begettings, Enoch taken, the prologue's states and the reprieve's timer set beyond the scene, the wiping decreed and closed, the ark owed and built, the boarding and the seven days fired, the flood's entries, the birds, the exit and the first altar, the vineyard and Canaan's curse, the nations, Babel, Shem's line and Haran's death, the call's three promises with the going closed, Abram's seven stations, the three land promises closed at the covenant's perfect, Egypt's body entry closed, the separation, the war's captive closed, the priest and the tithe, the pieces owed and closed, the decree's six entries, Hagar's), then the open entries, the timers set and fired, the closes performed, the clock: %r" % (SCENE,), ['begotten', 'land_promised'])
    if q == 'headline_promises':
        return cell('the_promises_of_the_land_close_on_the_inks_own_perfect', M, "THE HEADLINE (1): the land is promised at 12:7, 13:15 and 15:7 — three HEAVEN entries — and the covenant's own clause closes them: 'to your seed I HAVE GIVEN this land' (15:18, the perfect, the phrase's only seat in the Tanakh): the give-arc's receipt the frozen unit had exported is a close on the ledger; the seed's four entries of 15:13-16 stay open for Exodus (S1's scene now closes three of them at 12:29, 12:36, 12:41) and Joshua", ['land_promised', 'land_granted'])
    if q == 'headline_generations':
        return cell('the_three_generations_of_sanhedrin_10_3_are_three_heaven_entries', A, "THE HEADLINE (2): Mishnah Sanhedrin 10:3's three rows of this stretch — the flood generation, the dispersion generation, the men of Sodom — are three entries of no_share_in_the_world_to_come, each written at the Mishnah's own proof-text (7:23, 11:8-9, 13:13) and open forever; the answer sheet graded on the ledger (the sequence runner CG7)", ['no_share_in_the_world_to_come'])
    if q == 'headline_retrograde':
        return cell('the_reprieve_is_a_retrograde_dated_timer', M, "THE HEADLINE (3): 6:3's hundred and twenty years are a TIMER whose speaking the tape dates BEFORE the counter (the flood minus a hundred and twenty = Noah's 480, before 5:32's five hundred where the tape stands — Pesachim 6b:7's principle, Bereshit Rabbah 30:7's teaching), so it fires on the flood's own day (CG2); the seven days of 7:4 fire there too (CG3): the ink's two countdowns to one date", ['reprieve_of_a_hundred_and_twenty', 'seven_days_reprieve'])
    if q == 'headline_ledger':
        return cell('the_ledgers_deaths_ride_the_proleptic_markers', I, "THE HEADLINE (4): of the eleven 'and he died' of the stretch, ten are closing totals — proleptic markers on the tape, no event — and one, Haran's, is narrated in sequence and consumed as an act; Adam's mortality entry (3:19) stays open on the ledger with his total beside it, and Bereshit Rabbah 19:8's thousand-year day grades it (CG9)", ['return_to_dust', 'died_before_his_father'])
    if q == 'headline_two_layers':
        return cell('seven_kinds_under_two_law_layers', M, "THE HEADLINE (5): named, married, journeyed, lord_descended, died, believed, fled — one type each at Genesis and at Exodus or Gen 23-24: the older daemons gained the seat check their span implies (convention 14) and this daemon writes the Genesis statuses; the tape's double writes stay the two mornings of Exod 36:3", ['name_given', 'wife_taken', 'encamped_at'])
    return cell('no_case', I, '', [FX.NONE])


TESTS = [
 # ---- Gen 2: the garden ----
 ('a living soul — the phrase once as the man\'s predicate', garden('living_soul'), 1),
 ('the first office: work and keep', garden('office'), ('work', 'keep')),
 ('"took" — elevated or persuaded (Bereshit Rabbah 16:5)', garden('took'), ('elevated', 'persuaded')),
 ('a help, or against him (Bereshit Rabbah 17:3)', garden('helper'), ('a_help', 'against_him')),
 ('the couple\'s row (Yevamot 6:6)', garden('couple_sheet'), ('two_males', 'male_and_female')),
 ('the three deep sleeps at both seats (Bereshit Rabbah 17:5, 44:17)', garden('deep_sleeps'), ('sleep', 'prophecy', 'stupor')),
 ('the naming predicate\'s twelve seats', garden('names_count'), 12),   # FIRST RUN (2026-09-08): the design counted the scene's fourteen naming ACTS and typed 14; the census's predicate (a call-verb with the NOUN 'name' within four words) measures twelve — 2:23 ('she shall be called Woman') and 16:14 ('the well was called') name by the verb alone, and 13:4's 'called on the name of the LORD' is the liturgy's call caught by the noun. The miss is the model's (a predicate mistaken for an act count), recorded; the literal corrected beside it (14 -> 12)
 # ---- Gen 3: the breach ----
 ('the first rule fetched from the pre-Sinai engine (by call)', breach('first_rule_by_call'), ['ויצו', 'יהוה', 'אלהים', 'על', 'האדם', 'לאמר']),
 ('the four verbs of the breach', breach('four_verbs'), 4),
 ('the tree — vine, wheat, fig (Berakhot 40a; Sanhedrin 70a)', breach('tree_identity'), ('vine', 'wheat', 'fig')),
 ('three things said of the tree (Bereshit Rabbah 19:5)', breach('three_things'), 3),
 ('were they blind (Bereshit Rabbah 19:6)', breach('eyes'), 'were_they_blind'),
 ('"deceived" once in the Tanakh', breach('deceived_seat'), 1),
 ('the day\'s hours — sub-day is OUT', breach('no_sub_day'), 'recorded_not_run'),
 # ---- the sentences ----
 ('the four curses of the stretch', sentences('curse_seats'), [(3, 14), (3, 17), (4, 11), (9, 25)]),
 ('seventy-one mentions of the Name (Bereshit Rabbah 20:4)', sentences('seventy_one'), 71),
 ('four desires (Bereshit Rabbah 20:7)', sentences('four_desires'), 4),
 ('livelihood harder than birth (Bereshit Rabbah 20:9)', sentences('livelihood'), 'harder_than_birth'),
 ('the thousand-year day (Bereshit Rabbah 19:8)', sentences('thousand_year_day'), (1000, 930, 70)),
 ('four died by the serpent\'s counsel (Shabbat 55b)', sentences('serpent_counsel'), 4),
 ('the garments — kindness first and last (Sotah 14a)', sentences('garments_kindness'), 'begins_and_ends_with_kindness'),
 ('garments of light (Bereshit Rabbah 20:12)', sentences('garments_of_light'), 'kutnot_or_with_an_aleph'),
 ('expelled from two worlds? (Bereshit Rabbah 21:7)', sentences('expelled_two_worlds'), ('this_world_and_the_next', 'this_world_only')),
 ('driven out like a divorced daughter (Bereshit Rabbah 21:8)', sentences('divorced_daughter'), ('priests_daughter_cannot_return', 'israelites_daughter_can')),
 ('the east receives (Bereshit Rabbah 21:9)', sentences('east_receives'), ('adam', 'cain', 'the_manslayer')),
 # ---- Gen 4: Cain and Abel ----
 ('Cain\'s minchah names the meal-offering engine (by call)', cain('minchah_by_call'), 3),
 ('the firstling\'s seat, Lev 27:26 (by call)', cain('firstling_by_call'), 'cannot_be_sanctified_to_the_altar'),
 ('the fat inventory of the lamb (by call)', cain('fat_by_call'), ['parts', 'pointer_4_10']),
 ('the regard verb once in the Torah', cain('regard_seats'), [(4, 4)]),
 ('from the refuse; the firstlings (Bereshit Rabbah 22:5)', cain('refuse'), ('from_the_refuse', 'the_firstlings')),
 ('Abel no more than fifty days (the row; Bereshit Rabbah 22:4)', cain('abel_days'), 50),
 ('the first IF — rule over it (Kiddushin 30b)', cain('first_if'), 'rule_over_it'),
 ('wounds upon wounds (Sanhedrin 37b)', cain('wounds'), 'wounds_upon_wounds'),
 ('the bloods — his and his descendants\' (Sanhedrin 4:5)', cain('bloods_sheet'), 'his_blood_and_the_blood_of_his_descendants'),
 ('"your brother\'s bloods" at two seats', cain('bloods_seats'), [(4, 10), (4, 11)]),
 ('the earth\'s mouth opened once (Sanhedrin 37b)', cain('earth_mouth'), 'opened_once_for_abel'),
 ('exile atones half (Sanhedrin 37b)', cain('exile_half'), ('fugitive_and_wanderer', 'dwelt_in_nod')),
 ('greater than my father\'s (Bereshit Rabbah 22:11)', cain('greater_than_father'), 'a_light_command_vs_bloodshed'),
 ('the mark — three arms (Bereshit Rabbah 22:12)', cain('mark_arms'), ('a_dog', 'a_horn', 'leprosy')),
 ('"sevenfold" at two seats', cain('sevenfold_seats'), [(4, 15), (4, 24)]),
 ('Lamech\'s wives refused (Bereshit Rabbah 23:4)', cain('lamech_wives'), 'refused_tomorrow_the_flood'),
 ('two wives — offspring and pleasure (Bereshit Rabbah 23:2)', cain('two_wives'), ('for_offspring', 'for_pleasure')),
 ('the rebellion verb at three places (Bereshit Rabbah 23:7)', cain('rebellion_three'), 3),
 ('the first city', cain('city_seat'), 1),
 # ---- the lines and the ledger ----
 ('"and he begot" at thirty-seven seats of Genesis 5-11', lines('begot_seats'), 37),   # FIRST RUN (2026-09-08): the 39 was typed from a whole-book count of the token (scratchpad o8_s2_effects.py's measurement); the cell measures chapters 5-11 alone — 37. The literal corrected beside the miss (39 -> 37)
 ('"and she bore" at five seats of the stretch', lines('bore_seats'), 5),   # FIRST RUN (2026-09-08): the design's seven births counted by ANY verb (4:2 'she again bore' and 4:22 'she also bore' are other forms of the root); the token itself sits at five (4:1, 4:17, 4:20, 4:25, 16:15). The literal corrected beside the miss (7 -> 5)
 ('"and he died" at eleven seats', lines('died_seats'), 11),
 ('ten generations twice (Avot 5:2)', lines('ten_generations'), (10, 10)),
 ('Enoch taken while righteous (Bereshit Rabbah 25:1)', lines('enoch_taken'), 'hypocrite_taken_while_righteous'),
 ('Noah\'s name is not its exposition (Bereshit Rabbah 25:2)', lines('noah_name'), 'the_name_is_not_the_exposition'),
 ('the ten famines — the stretch\'s three (Bereshit Rabbah 25:3, 40:3)', lines('ten_famines'), ('adam', 'lamech', 'abraham')),
 ('two Enochs, two Lamechs', lines('two_lines_names'), ('enoch', 'lamech')),
 ('Seth\'s birth stated twice', lines('seth_twice'), 2),
 # ---- Gen 6: the prologue ----
 ('the sons of the judges (Bereshit Rabbah 26:5)', prologue('sons_of_god'), 'sons_of_the_judges'),
 ('the row gen6_3_reading', prologue('reading_row'), 'reprieve'),
 ('a hundred and twenty years parsed', prologue('reprieve_number'), 120),
 ('THE RETROGRADE DATING of 6:3', prologue('retrograde'), (600, 120, 480, 500)),
 ('with "great" they sinned (Sanhedrin 108a)', prologue('wickedness_great'), 'with_great_they_sinned_with_great_judged'),
 ('the regret — two arms (Sanhedrin 108a)', prologue('regret_two'), ('well_did_i_prepare_graves', 'not_well')),
 ('wiped in two worlds (Sanhedrin 108a; Avot? no — Sanhedrin 10:3)', prologue('wipe_two_worlds'), ('this_world', 'the_world_to_come')),
 ('even on Noah the decree was sealed (Sanhedrin 108a)', prologue('favor_even_noah'), 'the_decree_sealed_on_noah_too'),
 ('the flood\'s month — Iyar or Cheshvan (Rosh Hashanah 11b)', prologue('flood_month_row'), ('iyar', 'cheshvan')),
 # ---- the ark ----
 ('mated across kinds (Sanhedrin 108a)', ark('corrupt_five'), 'mated_across_kinds'),
 ('robbery sealed the decree (Sanhedrin 108a)', ark('robbery_seals'), 'robbery'),
 ('the spec\'s numbers', ark('spec_numbers'), (300, 50, 30)),
 ('the three decks (Sanhedrin 108b)', ark('decks'), ('dung', 'beasts', 'man')),
 ('the covenant\'s heads (by call)', ark('covenant_by_call'), 'you_and_your_seed_after_you'),
 ('"covenant" in the stretch — the bare noun\'s seats', ark('covenant_seats'), [(6, 18), (9, 9), (9, 11), (9, 13), (9, 15), (9, 16), (14, 13), (15, 18)]),   # FIRST RUN (2026-09-08): the design's list was typed from memory and carried the ARTICLED 'the covenant' of 9:12 and 9:17 (a second census — the standing lesson) while missing 14:13's 'the masters of Abram's covenant' (the allies); the cell measures the bare noun — the literal corrected beside the miss
 ('the receipt: thus did Noah', ark('receipt'), 'thus_did_noah'),
 ('the clean beast by the classifier (by call)', ark('clean_by_call'), 'pure'),
 ('the seven days — three arms (Sanhedrin 108b)', ark('seven_days_arms'), ('methuselahs_mourning', 'the_sun_reversed', 'a_taste_of_the_world_to_come')),
 ('the forty — two arms (Bereshit Rabbah 32:5)', ark('forty_arms'), ('the_torah_in_forty', 'the_embryos_forty')),
 ('intercourse barred and permitted by the word order (Sanhedrin 108b)', ark('intercourse_order'), ('barred_at_6_18', 'permitted_at_8_16')),
 ('three smitten in the ark (Sanhedrin 108b)', ark('three_smitten'), ('the_dog', 'the_raven', 'ham')),
 # ---- the flood ----
 ('judged by water like the eyeball (Sanhedrin 108a)', flood('eyeball'), 'judged_by_water_like_the_eyeball'),
 ('the beasts\' guilt — the wedding canopy (Sanhedrin 108a)', flood('beasts_guilt'), 'the_wedding_canopy'),
 ('not the fish', flood('not_the_fish'), 'not_the_fish'),
 ('only Noah remained', flood('remnant'), 1),
 ('a hundred and fifty days', flood('hundred_fifty'), 150),
 ('three generations (Sanhedrin 10:3)', flood('three_rows_sheet'), ('the_flood', 'the_dispersion', 'sodom')),
 ('twelve months (Eduyot 2:10)', flood('twelve_months_sheet'), 12),
 # ---- the remembering ----
 ('"and God remembered" — the debut', remembering('remember_seats'), [(8, 1)]),
 ('boiling water (Sanhedrin 108b)', remembering('boiling'), 'subsided_like_the_kings_wrath'),
 ('three fountains stayed open (Bereshit Rabbah 33:4)', remembering('three_fountains'), 3),
 ('the row window_count_from', remembering('window_from'), 'mountaintops'),
 ('the raven\'s retort (Sanhedrin 108b)', remembering('raven_retort'), 'your_master_hates_me_and_you_hate_me'),
 ('the dove\'s three sendings', remembering('dove_three'), ('returned', 'the_olive_leaf', 'did_not_return')),
 ('bitter from Your hand (Sanhedrin 108b)', remembering('olive_bitter'), 'bitter_from_your_hand_not_sweet_from_flesh_and_blood'),
 ('clean birds dwell with the righteous (Sanhedrin 108b)', remembering('clean_birds'), 'dwell_with_the_righteous'),
 ('a year and ten days by the ink', remembering('year_and_days'), (1, 10)),
 # ---- the exit ----
 ('entered and went out by permission (Bereshit Rabbah 34:4)', exit('by_permission'), 'entered_and_went_out_by_permission'),
 ('by families, not they (Sanhedrin 108b)', exit('by_families'), 'by_families_not_they'),
 ('the burnt offering\'s place (by call)', exit('olah_by_call'), 'north'),
 ('four altars', exit('altar_seats'), [(8, 20), (12, 7), (12, 8), (13, 18)]),
 ('the great altar (Bereshit Rabbah 34:9)', exit('great_altar'), 'the_great_altar_of_jerusalem'),
 ('the pleasing savor once in Genesis', exit('savor_seat'), 1),
 ('the righteous rule their hearts (Bereshit Rabbah 34:10)', exit('heart_resolve'), 'the_righteous_rule_their_hearts'),
 ('as long as heaven and earth stand (Bereshit Rabbah 34:11)', exit('seasons_standing'), 'as_long_as_heaven_and_earth_stand'),
 ('8:17 runs the blessing (by call)', exit('blessing_by_call'), [22, 28, 103]),
 # ---- the vineyard ----
 ('profaned (Bereshit Rabbah 36:3)', vineyard('profaned'), 'became_common'),
 ('planted, drank, disgraced in one day (Bereshit Rabbah 36:4)', vineyard('same_day'), 'planted_drank_disgraced_in_one_day'),
 ('learn from the first man (Sanhedrin 70a)', vineyard('learn_from_adam'), 'wine_alone_undid_the_first_man'),
 ('Ham\'s deed — Rav and Shmuel (Sanhedrin 70a)', vineyard('ham_deed'), ('castrated', 'lay_with')),
 ('Ham sinned and Canaan is cursed (Bereshit Rabbah 36:7)', vineyard('canaan_puzzle'), 'ham_sinned_and_canaan_is_cursed'),
 ('the slave word\'s four tokens', vineyard('slave_tokens'), 4),
 ('Shem the tallit, Japheth the burial (Bereshit Rabbah 36:6)', vineyard('shem_began'), ('shem_the_tallit', 'japheth_the_burial')),
 ('Greek alone (Megillah 1:8; 9b)', vineyard('greek_sheet'), 'greek_alone'),
 ('Cyrus, and the tents of Shem (Bereshit Rabbah 36:8)', vineyard('cyrus'), 'the_presence_only_in_the_tents_of_shem'),
 # ---- the nations ----
 ('greatness to Nimrod (Chullin 89a)', nations('nimrod_greatness'), 'i_gave_greatness_to_nimrod'),
 ('Amraphel is Nimrod (Eruvin 53a)', nations('amraphel'), ('nimrod_is_his_name', 'amraphel_is_his_name')),
 ('Shinar (Bereshit Rabbah 37:4)', nations('shinar'), ('the_dead_shaken_out', 'shakes_off_the_commandments')),
 ('Eber a great prophet (Bereshit Rabbah 37:7)', nations('peleg_prophet'), 'eber_a_great_prophet'),
 ('Japheth the elder (Bereshit Rabbah 37:7)', nations('shem_or_japheth_elder'), 'japheth_the_elder'),
 ('four cities', nations('cities_four'), 4),
 # ---- Babel ----
 ('one language — once', babel('one_language'), 1),
 ('three parties (Sanhedrin 109a)', babel('three_parties'), ('to_dwell', 'to_serve_idols', 'to_make_war')),
 ('Mitzrayim to Cush (Bereshit Rabbah 38:8)', babel('who_to_whom'), 'mitzrayim_to_cush'),
 ('one of the ten descents (Bereshit Rabbah 38:9)', babel('ten_descents'), 'one_of_the_ten'),
 ('changed for Ptolemy (Bereshit Rabbah 38:10)', babel('ptolemy'), 'let_ME_go_down'),
 ('the tower\'s thirds (Sanhedrin 109a)', babel('thirds'), ('burned', 'swallowed', 'stands')),
 ('two scatterings (Sanhedrin 10:3)', babel('two_scatterings'), ('this_world', 'the_world_to_come')),
 ('the scatter verb\'s debut', babel('scatter_seats'), [(11, 8)]),
 # ---- Shem\'s line ----
 ('two years after the flood', shem_line('two_years_after'), (100, 2)),
 ('Terah the idol-maker (Bereshit Rabbah 38:13)', shem_line('haran_furnace'), 'terah_the_idol_maker'),
 ('the one death in sequence', shem_line('died_in_sequence'), 1),
 ('Iscah is Sarah (Megillah 14a)', shem_line('iscah'), 'iscah_is_sarah'),
 ('the marriage formula\'s five verbs (by call)', shem_line('marriage_by_call'), 5),
 ('Sarai barren — once', shem_line('barren_seat'), 1),
 ('Terah\'s death sixty years after the going out', shem_line('terah_death_gap'), (70, 75, 205, 60)),
 ('the wicked called dead in their lifetime (Bereshit Rabbah 39:7)', shem_line('terah_death_midrash'), 'the_wicked_called_dead_in_their_lifetime'),
 ('Abram a year older than Nahor (Bereshit Rabbah 38:14)', shem_line('abram_elder'), 'abram_a_year_older_than_nahor'),
 # ---- the call ----
 ('the going\'s receipt', call('go_receipt'), 'as_the_lord_had_spoken'),
 ('two "go you" (Bereshit Rabbah 39:8)', call('two_go_you'), ('aram_naharaim_and_aram_nachor', 'the_pieces_to_haran')),
 ('I will MAKE you (Bereshit Rabbah 39:11)', call('new_creature'), 'i_will_MAKE_you'),
 ('the ladder\'s six clauses', call('ladder'), ('bless_you', 'make_your_name_great', 'be_a_blessing', 'bless_your_blessers', 'curse_your_curser', 'all_families_blessed_in_you')),
 ('the land promised thrice, closed at 15:18', call('land_seats'), [(12, 7), (13, 15), (15, 7), (15, 18)]),
 ('three altars (Bereshit Rabbah 39:16)', call('three_altars'), 3),
 ('"called on the name" at two Genesis seats', call('called_seats'), [(12, 8), (26, 25)]),
 ('seventy-five', call('seventy_five'), 75),
 ('seven stations of Abram', call('stations'), 7),
 # ---- Egypt ----
 ('the third famine (Bereshit Rabbah 40:3)', egypt('famine_third'), 'the_third_of_ten'),
 ('Abram\'s first speech', egypt('first_speech'), 'behold_now_i_know'),
 ('the chest at the customs (Bereshit Rabbah 40:5)', egypt('chest'), 'hidden_in_a_chest_at_the_customs'),
 ('the passive taking', egypt('passive_take'), 'taken_passive'),
 ('ra\'atan (Bereshit Rabbah 41:2)', egypt('raatan'), 'raatan'),
 ('the pattern of the sons (Bereshit Rabbah 40:6)', egypt('pattern'), 'whatever_is_written_of_abraham_is_written_of_his_sons'),
 ('silver and gold (Bereshit Rabbah 41:3)', egypt('silver_and_gold'), 'brought_them_out_with_silver_and_gold'),
 # ---- the separation ----
 ('muzzled (Bereshit Rabbah 41:5)', separation('muzzled'), 'abrahams_beasts_muzzled_lots_not'),
 ('a language of lewdness (Bereshit Rabbah 41:7)', separation('lewdness'), 'the_whole_verse_a_language_of_lewdness'),
 ('"they separated" once', separation('parted_seat'), 1),
 ('Sodom\'s row (Sanhedrin 10:3)', separation('sodom_sheet'), ('wicked_this_world', 'sinners_the_world_to_come', 'but_they_stand_in_judgment')),
 ('Sodom — body and money (Sanhedrin 109a)', separation('sodom_arms'), ('wicked_in_body_sinners_in_money', 'wicked_in_money_sinners_in_body')),
 ('the dust blessed by water (Bereshit Rabbah 41:9)', separation('dust'), 'as_the_dust_blessed_only_by_water'),
 ('the walk — the three modes (by call; Bava Batra 100a)', separation('walk_by_call'), ['money', 'deed', 'possession']),
 # ---- the war ----
 ('the years\' chain', war('years_chain'), (12, 13, 14)),
 ('twenty-five or thirteen (Bereshit Rabbah 42:6)', war('years_arms'), (25, 13)),
 ('an annal with no speech', war('annal'), 0),
 ('the escapee is Og (Bereshit Rabbah 42:8)', war('og'), 'the_escapee_is_og'),
 ('the Hebrew — three arms (Bereshit Rabbah 42:8)', war('hebrew_arms'), ('from_eber', 'from_beyond_the_river', 'the_language')),
 ('three hundred and eighteen', war('three_eighteen'), 318),
 ('Eliezer alone (Nedarim 32a)', war('eliezer'), 'eliezer_alone'),
 ('the two hundred and ten years — three causes (Nedarim 32a)', war('punished_210'), ('pressed_scholars_into_service', 'whereby_shall_i_know', 'give_me_the_persons')),
 ('the night\'s halves (Bereshit Rabbah 43:3)', war('night_halves'), ('of_itself', 'its_maker_divided_it')),
 ('the children not returned (Bereshit Rabbah 43:4)', war('children_not_returned'), 'men_and_women_returned_the_children_not'),
 ('the priest\'s office (by call)', war('priest_by_call'), ['blemished_and_minors', 'chalalim']),
 ('the priesthood from Shem (Nedarim 32b)', war('priesthood_from_shem'), 'taken_from_shem_given_to_abraham'),
 ('Salem is Jerusalem (Bereshit Rabbah 43:6)', war('salem'), 'salem_is_jerusalem'),
 ('the tithe\'s seat (by call)', war('tithe_by_call'), 'holy_to_the_LORD'),
 ('the raised hand (Bereshit Rabbah 43:9)', war('raised_hand'), ('terumah', 'an_oath')),
 ('a thread to a shoe-latchet', war('thread_to_latchet'), 'not_a_thread_nor_a_shoe_latchet'),
 # ---- the pieces ----
 ('two fears (Bereshit Rabbah 44:4)', pieces('two_fears'), ('a_righteous_man_among_the_slain', 'the_reward_consumed')),
 ('"childless" — Lev 20:20\'s row (by call)', pieces('childless_by_call'), (14, 20, None, True)),
 ('the heir — the inheritance owed forward (by call)', pieces('heir_by_call'), ['Deut 25:5', 'Num 27:8']),
 ('no constellation for Israel (Nedarim 32a)', pieces('astrology'), 'no_constellation_for_israel'),
 ('inherited both worlds by faith (the Mekhilta)', pieces('faith_merit'), 'inherited_both_worlds_by_faith'),
 ('reckoned — staged both ways', pieces('reckoned_both_ways'), 'staged_both_ways'),
 ('the furnace (Bereshit Rabbah 44:13)', pieces('furnace'), ('michael', 'the_holy_one_himself')),
 ('by what merit (Bereshit Rabbah 44:14)', pieces('by_what_merit'), 'by_the_atonements'),
 ('the bird offering\'s species (by call)', pieces('birds_by_call'), 'turtledoves_or_young_pigeons'),
 ('the kingdoms and the bird (Bereshit Rabbah 44:15)', pieces('kingdoms'), ('babylon', 'media', 'greece', 'israel_the_bird')),
 ('four hundred years', pieces('four_hundred'), 400),
 ('also that nation (Bereshit Rabbah 44:19)', pieces('also_that_nation'), ('egypt', 'the_four_exiles')),
 ('after ten plagues (Bereshit Rabbah 44:20)', pieces('after_ten_plagues'), 'after_i_bring_ten_plagues'),
 ('the fourth generation', pieces('fourth_generation'), 4),
 ('four things shown (Bereshit Rabbah 44:21)', pieces('four_things'), ('gehenna', 'the_kingdoms', 'the_giving_of_the_torah', 'the_temple')),
 ('the covenant cut — Exod 34\'s word', pieces('covenant_cut_seat'), 1),
 ('ten named, seven given (Bereshit Rabbah 44:23)', pieces('ten_nations'), (10, 7, 3)),
 # ---- Hagar ----
 ('ten years (Yevamot 6:6; 64a)', hagar('ten_years_sheet'), 'may_not_neglect_procreation'),
 ('the ten years parsed', hagar('ten_years_number'), 10),
 ('"to him as a wife" at seven Genesis seats', hagar('as_a_wife'), 7),
 ('from the first union (Bereshit Rabbah 45:4)', hagar('first_union'), ('from_the_first_union', 'never_from_the_first')),
 ('"despised" once', hagar('despised_seat'), 1),
 ('you wrong me with words (Bereshit Rabbah 45:5)', hagar('wrong_with_words'), 'you_wrong_me_with_words'),
 ('the affliction\'s reading (Bereshit Rabbah 45:6)', hagar('affliction_reading'), 'not_obliged_for_her_good_or_ill'),
 ('the flight — one type, two layers', hagar('flight_seat'), 'the_exodus_daemon_seat_checked'),
 ('the return never narrated', hagar('return_open'), 'return_never_narrated'),
 ('named before birth (Bereshit Rabbah 45:8)', hagar('named_before_birth'), ('isaac', 'solomon', 'josiah')),
 ('"you shall call" against "Abram called"', hagar('you_shall_call_vs_abram_called'), ('you_shall_call', 'abram_called')),
 ('the wild ass (Bereshit Rabbah 45:9)', hagar('wild_ass'), ('grows_in_the_wilderness', 'plunders_souls')),
 ('a God of seeing (Bereshit Rabbah 45:10)', hagar('god_of_seeing'), 'never_conversed_with_a_woman_but_through_an_angel'),
 # ---- THE SCENE AND THE HEADLINES ----
 ('THE SCENE on the world engine', build('world'), (1, 1, 1, 1, 1, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 3, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 7, 3, 1, 1, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 25, 2, 1, 14, 366)),
 ('HEADLINE: the land promises close on the perfect', build('headline_promises'), 'the_promises_of_the_land_close_on_the_inks_own_perfect'),
 ('HEADLINE: three generations, three heaven entries', build('headline_generations'), 'the_three_generations_of_sanhedrin_10_3_are_three_heaven_entries'),
 ('HEADLINE: the reprieve is a retrograde-dated timer', build('headline_retrograde'), 'the_reprieve_is_a_retrograde_dated_timer'),
 ('HEADLINE: the ledger\'s deaths ride the proleptic markers', build('headline_ledger'), 'the_ledgers_deaths_ride_the_proleptic_markers'),
 ('HEADLINE: seven kinds under two law layers', build('headline_two_layers'), 'seven_kinds_under_two_law_layers'),
]

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
    print('effects: every cell carries REGISTERED effects — a hundred and forty-three discovered in the stretch\'s own words and registered first (living_soul ... wild_ass_of_a_man) [effects law satisfied]')
    print('SCENE: %r' % (SCENE,))
    _W.print_coverage()
    if ok == n:
        print()
        print('FROM EDEN TO HAGAR STANDS — the garden and the breach, the four sentences, Cain and the bloods, the two lines and the ledger, the reprieve and the ark, the flood and the birds, the exit and the first altar, the vineyard, the nations, Babel, Shem\'s line, the call, Egypt, the separation, the war, the pieces, Hagar — on one ledger, eight engines called.')
    else:
        print('MISSES (%d):' % len(misses))
        for m_ in misses: print('  -', m_[0][:80], '->', m_[1])
        sys.exit('MISSES REMAIN — a miss is evidence, never a retype: read it.')

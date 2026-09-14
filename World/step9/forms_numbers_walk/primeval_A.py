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

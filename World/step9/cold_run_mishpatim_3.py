#!/usr/bin/env python3
"""cold_run_mishpatim_3.py — THE EXODUS LAW'S FIVE CASE HEADS (O7, 2026-09-07; REPORT_EXODUS_HEADS.md): Exod 21:7-11 the
maidservant (X1), 21:13-15 and 21:17 the capital clauses (X2), 21:20-21 the slave struck (X3), 22:1-2 the burglar (X4);
22:16 the father's refusal (X5) lives in cold_run_mishpatim_2.py beside the seducer it branches from.

The six motions: (1) the code from the BARE INK of the five heads — the sale of a daughter, the designation, the three,
the two exits, the refuge, the altar, the parents struck and cursed, the rod and the day, the tunnel and the sun, the
sale for the theft; (2) the Mishnah's rows as TEST DATA read whole from the shelf, each verified by a token in its own
ink (Kiddushin 1:2, Sotah 3:8, Makkot 2:1-3, Sanhedrin 7:8, 8:6, 9:1, 11:1, Ketubot 3:4, 5:6); (3) the run; (4) the
misses filled by NAMED recorded arguments — the Mekhilta d'Rabbi Yishmael Nezikin 7-11, 13-15, 17, 20-21 and its
continuation 1-2, Kiddushin 3b-4a, 18a-19a, Sanhedrin 41a, 52b, 72a-b, 85b, Yoma 85a, Bava Kamma 90a, Ketubot 47b-48a,
Sotah 23b; (5) the graded matrix with per-cell provenance and EFFECTS on every verdict — four discovered in the span's
own verbs and registered first: taken_from_altar, beheaded (the sword the tradition reads in 'avenged'), not_diminished,
has_blood; (6) THE WRAP — law_mishpatim_3 over the cells, declared first, the scene as literal submits with the tuple
predicted by script (scratchpad o7_predict.py) before this file was typed. The 21:17 seat CALLS the Leviticus seat's
curser (cold_run_sanctions.py) — the same clause at two seats, a REFERENCE.
Zero-report law: every claimed ink token is probed before anything runs; the answer sheet is verified in its own ink.
"""
import sqlite3, sys, os, json, re, io, contextlib
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import effects_layer as FX
from compile_guards import check_honest_pairing

GUARDED = check_honest_pairing(os.path.abspath(__file__))
print('honest-pairing guard: %d tests checked, every expectation a literal' % GUARDED)

ROOT = '<repo-old>'
db = sqlite3.connect('file:' + ROOT + '/elijah_docket/tanakh.sqlite?mode=ro', uri=True)


def strip(s):
    return ''.join(c for c in s if c != '/' and not (0x0591 <= ord(c) <= 0x05C7))


def toks(ch, vs):
    rows = db.execute("""SELECT w.he FROM words w JOIN verses v ON w.verse_id=v.id
        WHERE v.book='Exod' AND v.chapter=? AND v.verse=? ORDER BY w.idx""", (ch, vs)).fetchall()
    return [strip(r[0]) for r in rows]


T = {(ch, vs): toks(ch, vs) for ch, vss in ((21, list(range(7, 12)) + [13, 14, 15, 17, 20, 21]), (22, [1, 2])) for vs in vss}

# ---- (1) ink probes — each MUST fire or the run refuses -------------
PROBES = [
    ('when a man SELLS his daughter',          21, 7, 'ימכר'),
    ('as a MAIDSERVANT',                       21, 7, 'לאמה'),
    ('not as the male SLAVES go out',          21, 7, 'העבדים'),
    ('who did not DESIGNATE her',              21, 8, 'יעדה'),
    ('he shall let her be REDEEMED',           21, 8, 'והפדה'),
    ('to a FOREIGN people',                    21, 8, 'נכרי'),
    ('for his SON he designates her',          21, 9, 'לבנו'),
    ('as the law of the DAUGHTERS',            21, 9, 'הבנות'),
    ('her FOOD (her flesh)',                   21, 10, 'שארה'),
    ('her CLOTHING',                           21, 10, 'כסותה'),
    ('her CONJUGAL RIGHT (her season)',        21, 10, 'וענתה'),
    ('he shall not DIMINISH',                  21, 10, 'יגרע'),
    ('these THREE',                            21, 11, 'שלש'),
    ('she goes out FREE',                      21, 11, 'חנם'),
    ('WITHOUT money',                          21, 11, 'אין'),
    ('did not LIE IN WAIT',                    21, 13, 'צדה'),
    ('a PLACE where he shall flee',            21, 13, 'מקום'),
    ('he shall FLEE there',                    21, 13, 'ינוס'),
    ('acts PRESUMPTUOUSLY',                    21, 14, 'יזד'),
    ('with GUILE',                             21, 14, 'בערמה'),
    ('from My ALTAR',                          21, 14, 'מזבחי'),
    ('you shall TAKE him to die',              21, 14, 'תקחנו'),
    ('he who STRIKES his father and mother',   21, 15, 'ומכה'),
    ('he who CURSES his father and mother',    21, 17, 'ומקלל'),
    ('his SLAVE',                              21, 20, 'עבדו'),
    ('with the ROD',                           21, 20, 'בשבט'),
    ('UNDER his hand',                         21, 20, 'תחת'),
    ('AVENGED he shall be avenged',            21, 20, 'ינקם'),
    ('a DAY or two days',                      21, 21, 'יום'),
    ('for he is his MONEY',                    21, 21, 'כספו'),
    ('in the TUNNEL',                          22, 1, 'במחתרת'),
    ('the THIEF found',                        22, 1, 'הגנב'),
    ('he has no BLOOD',                        22, 1, 'דמים'),
    ('the SUN shone',                          22, 2, 'השמש'),
    ('he shall surely PAY',                    22, 2, 'ישלם'),
    ('SOLD for his theft',                     22, 2, 'ונמכר'),
]
failed = [(n, ch, vs, tok) for n, ch, vs, tok in PROBES if tok not in T[(ch, vs)]]
if failed:
    sys.exit('ZERO-REPORT LAW: probes failed to fire: %r — refusing to run' % failed)
print('probes: all %d token probes fired  [zero-report law satisfied]' % len(PROBES))

I, M, A, D, H = 'INK', 'MOVE', 'ANSWER-SHEET', 'DATA', 'HYPOTHESIS'   # H: THE LINK REVIEW LAW (LR3) — an untaught transfer, kept and labeled


def cell(v, p, why, effects):
    FX.validate(effects)
    return {'v': v, 'p': p, 'why': why, 'fx': effects}


with contextlib.redirect_stdout(io.StringIO()):     # the Leviticus seat grades itself at import — its report stays its own
    import cold_run_sanctions as SA    # THE LIVE EDGE: 21:17 is the first seat of Lev 20:9 — the curser's mode and readings by call (a REFERENCE)

MK = 'Mekhilta d\'Rabbi Yishmael Nezikin '


# ---- X1 THE MAIDSERVANT — Exod 21:7-11 ---------------------------------
def maidservant(q, **k):
    if q == 'who_sells':
        return cell('the_father_alone', M, MK + '7 2 — וכי ימכר איש (and when a MAN sells): the man sells his daughter, the '
                    'woman does not (Mishnah Sotah 3:8); not his son (7 3); not herself, nor is she sold for her theft or '
                    'pierced (7 4)', ['term_clock'])
    if q == 'her_age':
        return cell('a_minor', M, MK + '7 1 — the signs take her out of her father\'s hand; all the more she is not sold '
                    'once they have come', ['term_clock'])
    if q == 'exits':
        return cell(['years', 'jubilee', 'deduction', 'signs'], A, 'Mishnah Kiddushin 1:2 — the Hebrew maidservant acquires '
                    'herself by these and by the SIGNS beyond him; לא תצא כצאת העבדים (she shall not go out as the male '
                    'slaves go out, 21:7) — not by the tooth and the eye, but by the years and the jubilee (' + MK +
                    '7 8, from Deut 15:12); redeemed against his will, not sold twice (Kiddushin 18a:5)', ['term_clock', 'goes_free'])
    if q == 'designation':
        return cell('betrothal_with_her_consent', M, 'Kiddushin 18b:3-4 — designation makes BETROTHAL, the first money '
                    'given for it; 19a:7 Rabbi Yannai: no designation except of an adult, because none except with '
                    'consent; designation before redemption (' + MK + '8 1; Mishnah Bekhorot 1:6); for his son, not his '
                    'brother (9 1)', ['wife_taken'])
    if q == 'the_three':
        return cell(['food', 'clothing', 'conjugal_right'], I, 'שארה כסותה וענתה לא יגרע (her food, her clothing and her '
                    'conjugal right he shall not diminish) at 21:10 — which noun is which a recorded dispute (' + MK +
                    '10 2: Rabbi Yoshiya שאר food / עונה conjugal; Rabbi the reverse; Ketubot 47b:10-11); כמשפט הבנות '
                    '(as the law of the daughters, 21:9) comes to teach and is taught — the three for every daughter of '
                    'Israel (9 2); the quantities the answer sheet\'s data (Mishnah Ketubot 5:6, 5:8-9)', ['not_diminished'])
    if q == 'the_two_exits':
        return cell({'free': 'maturity', 'without_money': 'youth'}, M, 'ויצאה חנם אין כסף (she goes out FREE, WITHOUT '
                    'MONEY) at 21:11 — Kiddushin 4a:3, 4a:11 and ' + MK + '11 3-4: "free" the days of maturity, "without '
                    'money" the days of youth (the signs); "let this come and teach that" (Rabbah)', ['goes_free'])
    if q == 'money_for_another':
        return cell('the_father', M, 'Kiddushin 3b:5, 4a:4 — אין כסף לאדון זה אבל יש כסף לאדון אחר (no money for THIS master, '
                    'but money for another master): the father\'s right to her betrothal money', [FX.NONE])
    if q == 'these_three':
        return cell(['designate_for_himself', 'designate_for_his_son', 'redeem'], M, MK + '11 1 — ואם שלש אלה (and if '
                    'these THREE he does not do): designate her for himself, for his son, or redeem her — not the food, '
                    'clothing and conjugal right; free of the money, not free of the bill of divorce (11 2)', ['goes_free'])
    if q == 'redemption':
        return cell('against_his_will', M, 'והפדה (he shall let her be redeemed) at 21:8 — Kiddushin 18a:5: redeemed '
                    'against his will; by deduction of money (Mishnah Kiddushin 1:2)', ['redemption_right', 'goes_free'])
    if q == 'foreign_sale':
        return cell('barred_a_warning_to_the_court', M, 'לעם נכרי לא ימשל למכרה (to a foreign people he has no power to '
                    'sell her) at 21:8 — ' + MK + '8 3: a warning to the court; בבגדו בה (in his betraying her) — Rabbi '
                    'Yishmael: the master who bought her to designate and did not (8 4)', ['barred_from_it'])
    raise ValueError(q)


# ---- X2 THE CAPITAL CLAUSES — Exod 21:13-15, 21:17 ------------------------
def killer(q, **k):
    if q == 'refuge_by_descent':
        return cell({'descent': 'exile', 'ascent': 'no_exile'}, A, 'Mishnah Makkot 2:1 — rolling down, lowering the '
                    'barrel, descending the ladder: exile; pulling up, drawing up, ascending: no exile — כל שבדרך ירידתו '
                    'גולה (all in the manner of descent goes into exile); ' + MK + '13 1 the same rows on 21:13',
                    ['flees_to_refuge', 'exempt'])
    if q == 'the_place':
        return cell('levite_cities_for_the_generations_levite_camps_for_the_hour', M, 'ושמתי לך מקום (I will appoint '
                    'you a place) at 21:13 — ' + MK + '13 2: the refuge for the hour and the refuge for the generations; '
                    'the Levites\' cities receive, so the Levites\' camps received', ['flees_to_refuge'])
    if q == 'father_and_son':
        return cell('each_exiles_for_the_other', A, 'Mishnah Makkot 2:3 — the father goes into exile for the son and '
                    'the son for the father', ['flees_to_refuge'])
    if q == 'guile_excludes':
        return cell(['deaf_mute', 'minor', 'physician_who_killed', 'court_agent', 'father_disciplining', 'teacher'], M,
                    'להרגו בערמה (to kill him with guile) at 21:14 — ' + MK + '14 1-3: the deaf-mute and the minor do '
                    'not scheme; the physician who killed, the court\'s agent, the father and the teacher are deliberate '
                    'but not scheming; Mishnah Makkot 2:2 (Abba Shaul): no exile for them either', ['exempt'])
    if q == 'forewarning':
        return cell('warned_and_still_deliberate', M, 'Sanhedrin 41a:2 — the school of Chizkiyah: בערמה (with guile) — '
                    'that they WARNED him and he is still deliberate', ['beheaded'])
    if q == 'the_altar':
        return cell('from_beside_not_from_upon', M, 'מעם מזבחי תקחנו למות (from My altar you shall take him to die) at '
                    '21:14 — they void the service from his hand and he goes out to be killed (' + MK + '14 4); FROM '
                    'BESIDE My altar, not from UPON it — to put to death, but to save life even from upon it (Yoma '
                    '85a:15-85b:1; Sanhedrin 35b:5, 36a:4 the daily offering); "to die" — not to be judged, lashed or '
                    'exiled (14 7); the Sanhedrin sits beside the altar (14 8)', ['taken_from_altar'])
    if q == 'mode':
        return cell('the_sword', M, 'Mishnah Sanhedrin 9:1 — the murderer among the beheaded; Sanhedrin 52b:13 = ' + MK +
                    '20 6 (Rabbi Natan): נקם ינקם (he shall surely be avenged, 21:20) with חרב נקמת (a sword avenging, '
                    'Lev 26:25) — a verbal analogy the tradition records', ['beheaded'])
    if q == 'his_fellow':
        return cell('includes_the_minor_victim', M, MK + '14 2 — איש (a man) excludes the minor striker; רעהו (his '
                    'fellow) includes the minor victim', ['beheaded'])
    raise ValueError(q)


def parent_striker(q):
    if q == 'wound':
        return cell('a_blow_with_a_wound', A, 'Mishnah Sanhedrin 11:1 — המכה אביו ואמו אינו חייב עד שיעשה בהן חבורה (not '
                    'liable until he makes a wound in them); ' + MK + '15 3', ['put_to_death'])
    if q == 'mode':
        return cell('strangling', A, 'Mishnah Sanhedrin 11:1 lists him among the strangled; ' + MK + '15 4: the '
                    'unspecified death is strangling (Rabbi Yonatan) — a death that leaves no mark (Rabbi)', ['put_to_death'])
    if q == 'after_death':
        return cell('exempt', A, 'Mishnah Sanhedrin 11:1 — the striker after death exempt, the curser after death liable '
                    '(Sanhedrin 85b:3)', ['exempt'])
    if q == 'either_parent':
        return cell('either', M, MK + '15 2 — his father without his mother, his mother without his father (Rabbi '
                    'Yoshiya; Rabbi Yonatan: "both" unless the verse says "together")', ['put_to_death'])
    raise ValueError(q)


def parent_curser(q):
    """Exod 21:17 — THE FIRST SEAT of Lev 20:9's clause: the mode and the readings by CALL into the Leviticus seat."""
    if q == 'the_woman':
        return cell('included', M, MK + '17 1 — "I have only a man (Lev 20:9\'s any man); a woman, a tumtum, an '
                    'androgynos? — ומקלל אביו ואמו (and he who curses his father and his mother, 21:17)"', ['stoned'])
    if q in ('mode', 'one_parent', 'after_death', 'by_the_name'):
        c = SA.curser(q)
        return cell(c['v'], M, ('IMPORT — cold_run_sanctions.curser(%s): %s | 21:17 the first seat: the mode by the '
                    'blood-formula analogy דמיו בו / דמיהם בם (' + MK + '17 3)') % (q, c['why'][:90]), ['stoned'])
    raise ValueError(q)


# ---- X3 THE SLAVE STRUCK — Exod 21:20-21 ----------------------------------
def slave_struck(q):
    if q == 'whose_slave':
        return cell('the_canaanite_wholly_his', M, MK + '20 3 — Rabbi Eliezer: the Canaanite; Rabbi Yishmael from כי '
                    'כספו הוא (for he is his money): a permanent acquisition wholly in his domain — the Hebrew slave, '
                    'the jointly owned and the half-free EXCLUDED, they stand under the general clause', ['avenged'])
    if q == 'the_rod':
        return cell('a_thing_that_can_kill_at_a_place_that_can_kill', M, 'בשבט (with the rod) at 21:20 — ' + MK + '20 4',
                    ['avenged'])
    if q == 'under_his_hand':
        return cell('the_blow_and_the_death_in_his_domain', M, 'ומת תחת ידו (and he dies under his hand) at 21:20 — ' +
                    MK + '20 5: struck him, sold him, and he died — exempt', ['avenged', 'exempt'])
    if q == 'avenged_is':
        return cell('death_by_the_sword', M, 'נקם ינקם (avenged he shall be avenged) at 21:20 — ' + MK + '20 6 (Rabbi '
                    'Natan) and Sanhedrin 52b:13: death, by the sword, from Lev 26:25', ['avenged'])
    if q == 'a_day_or_two':
        return cell('from_time_to_time_twenty_four_hours', M, 'אך אם יום או יומים (but if a day or two days, 21:21) — ' +
                    MK + '21 1: a day that is like two days, two days that are like a day — from time to time', ['exempt'])
    if q == 'his_money_arms':
        return cell(['first_master — Rabbi Meir', 'second_master — Rabbi Yehuda', 'both — Rabbi Yose', 'neither — Rabbi Eliezer'], A,
                    'Bava Kamma 90a:5-9 — the slave sold with thirty days\' service reserved: who stands in the day-or-two '
                    'law; Rava: כספו המיוחד לו (his money — wholly his)', ['exempt', 'beheaded'])
    raise ValueError(q)


# ---- X4 THE BURGLAR — Exod 22:1-2 -----------------------------------------
def burglar(q):
    if q == 'the_doubt':
        return cell('came_to_steal_or_to_kill', M, MK + 'continuation 1 1; Sanhedrin 72a:4 (Rava): a man does not stand '
                    'by while his money is taken — "if he comes to kill you, rise early and kill him"', ['has_blood'])
    if q == 'judged_by_his_end':
        return cell('no_blood', A, 'Mishnah Sanhedrin 8:6 — הבא במחתרת נדון על שם סופו (the one who comes by tunneling is '
                    'judged by his end); אין לו דמים (he has no blood, 22:1)', ['has_blood', 'exempt'])
    if q == 'the_sun':
        return cell('clarity_that_he_is_at_peace', M, 'אם זרחה השמש עליו (if the sun shone upon him, 22:2) — ' + MK +
                    'continuation 2 1 (Rabbi Yishmael): did the sun shine on him ALONE? — if it is clear as the sun that '
                    'he is at peace with you; day and night not divided; Sanhedrin 72a:15-16', ['has_blood', 'put_to_death'])
    if q == 'the_father':
        return cell('presumed_merciful', M, 'Sanhedrin 72b:1-2 — the two baraitot resolved: the father against the son, '
                    'presumed merciful as a father on a son — kill only on certainty', ['has_blood'])
    if q == 'struck_by_whom':
        return cell('any_person_any_death', M, 'והכה ומת (and is struck and dies, 22:1) — Sanhedrin 72b:6-8: by any '
                    'person, by any death', ['exempt'])
    if q == 'the_barrel':
        return cell({'no_blood': 'exempt', 'blood': 'pays'}, A, 'Mishnah Sanhedrin 8:6 — broke a barrel: with blood '
                    'liable, without blood exempt (the greater penalty absorbs the lesser, 72a:8-10)', ['exempt', 'pays'])
    if q == 'the_sabbath':
        return cell('the_same_and_the_pile_cleared', M, 'Sanhedrin 72b:3-5 — blood and no blood alike on the Sabbath; '
                    'Rav Sheshet: the pile is cleared from him', ['has_blood'])
    if q == 'the_sale':
        return cell('six_years_for_the_principal', M, 'ונמכר בגנבתו (and he is sold for his theft, 22:2) — ' + MK +
                    'continuation 2 3: six years, from שש שנים יעבד (21:2) — a reference to the Hebrew slave\'s term; '
                    'Kiddushin 18a:8: for the principal, not the double; not for less than the theft (2 4)',
                    ['sold_for_theft', 'term_clock'])
    if q == 'the_woman':
        return cell('not_sold', A, 'Mishnah Sotah 3:8 — the man is sold for his theft, the woman is not; Sotah 23b:12: '
                    'בגניבתו ולא בגניבתה (for HIS theft and not for hers); ' + MK + '7 4', ['pays'])
    raise ValueError(q)


# ---- (2) the answer sheet, read whole from the shelf and verified in its own ink ----
def mishnah(tractate, ch, m, must):
    d = json.load(open(ROOT + '/Data/mishnah_%s_he.json' % tractate))
    t = d['text'] if isinstance(d, dict) and 'text' in d else d
    row = strip(re.sub(r'<[^>]+>', '', t[ch - 1][m - 1]))
    assert must in row, 'answer-sheet check failed: %r not in Mishnah %s %d:%d' % (must, tractate, ch, m)


def _mekhilta(tr, ch, n, must):
    d = json.load(open(ROOT + '/Data/mekhilta_he.json'))
    t = d['text'] if isinstance(d, dict) and 'text' in d else d
    row = strip(re.sub(r'<[^>]+>', '', t[tr][ch - 1][n - 1]))
    assert must in row, 'answer-sheet check failed: %r not in Mekhilta tractate %d chapter %d row %d' % (must, tr, ch, n)


def _bavli(tr, daf, side, seg, must):
    d = json.load(open(ROOT + '/Data/bavli_%s_he.json' % tr))
    t = d['text'] if isinstance(d, dict) and 'text' in d else d
    row = strip(re.sub(r'<[^>]+>', '', t[2 * daf - 2 + (1 if side == 'b' else 0)][seg - 1]))
    assert must in row, 'answer-sheet check failed: %r not in %s %d%s:%d' % (must, tr, daf, side, seg)


SHEET = [
    ('kiddushin', 1, 2, 'בסימנין'), ('sotah', 3, 8, 'בגנבתה'), ('makkot', 2, 1, 'ירידתו'), ('makkot', 2, 2, 'הרודה'),
    ('makkot', 2, 3, 'גולה'), ('sanhedrin', 7, 8, 'בשם'), ('sanhedrin', 8, 6, 'סופו'), ('sanhedrin', 9, 1, 'הנהרגים'),
    ('sanhedrin', 11, 1, 'חבורה'), ('ketubot', 3, 4, 'בעציצו'), ('ketubot', 5, 6, 'העונה'),
]
SHEET2 = [   # the Mekhilta (tractate index 20 = Nezikin, 21 = its continuation) and the Babylonian rows the cells cite
    ('mekhilta', 20, 7, 2, 'מוכרת'), ('mekhilta', 20, 8, 3, 'אזהרה'), ('mekhilta', 20, 9, 2, 'ונמצא למד'),
    ('mekhilta', 20, 10, 2, 'מזונותיה'), ('mekhilta', 20, 11, 1, 'ייעד לך'), ('mekhilta', 20, 11, 3, 'בבגר'),
    ('mekhilta', 20, 13, 2, 'ערי הלוים'), ('mekhilta', 20, 14, 3, 'מרפא'), ('mekhilta', 20, 14, 4, 'מבטלים'),
    ('mekhilta', 20, 15, 4, 'בחנק'), ('mekhilta', 20, 17, 1, 'אשה'), ('mekhilta', 20, 20, 3, 'בכנעני'),
    ('mekhilta', 20, 20, 6, 'חרב'), ('mekhilta', 20, 21, 1, 'מעת לעת'), ('mekhilta', 21, 1, 1, 'להרוג'),
    ('mekhilta', 21, 2, 1, 'שלום'), ('mekhilta', 21, 2, 3, 'שש שנים'),
    ('bavli', 'kiddushin', 4, 'a', 3, 'בגרות'), ('bavli', 'kiddushin', 18, 'a', 5, 'בסימנין'), ('bavli', 'kiddushin', 19, 'a', 7, 'מדעת'),
    ('bavli', 'sanhedrin', 41, 'a', 2, 'שהתרו'), ('bavli', 'sanhedrin', 52, 'b', 13, 'סייף'), ('bavli', 'sanhedrin', 72, 'a', 4, 'השכם'),
    ('bavli', 'sanhedrin', 72, 'b', 2, 'כרחם אב'), ('bavli', 'yoma', 85, 'a', 15, 'מעל מזבחי'), ('bavli', 'bava_kamma', 90, 'a', 9, 'המיוחד'),
    ('bavli', 'sotah', 23, 'b', 12, 'בגניבתה'), ('bavli', 'ketubot', 47, 'b', 10, 'מזונות'),
]
for tr, ch, m, must in SHEET:
    mishnah(tr, ch, m, must)
for kind, *ref in SHEET2:
    (_mekhilta if kind == 'mekhilta' else _bavli)(*ref)
print('answer sheet: %d Mishnah rows + %d Mekhilta/Talmud rows read whole from the shelf, each verified by a token in its own ink'
      % (len(SHEET), len(SHEET2)))


# ---- (6) THE WRAP — the daemon over the cells, declared first ----------------
import world_engine as WE


def law_mishpatim_3(event, world):
    """Exod 21:7-11, 21:13-15, 21:17, 21:20-21, 22:1-2 (cold_run_mishpatim_3.py — maidservant, killer, parent_striker,
    parent_curser, slave_struck, burglar): every value a call into the cells; the ledger written, never an event emitted."""
    k, src = event['kind'], event['case_source']
    E_ = lambda eff, s, cp=None, amount=None, due=None, law='', value=None: {'effect': eff, 'subject': s, 'counterparty': cp, 'amount': amount, 'due': due, 'value': value if value is not None else True, 'source_law': law, 'case_source': src}
    if k == 'daughter_sold':
        d = event['daughter']; m = event['master']
        if event.get('seller', 'father') != 'father' or event.get('daughter_age', 'minor') != 'minor':
            return []                                                # the mother cannot sell; a minor only — the silence (X1 who_sells / her_age)
        ds = event.get('designated_for')
        if ds in ('master', 'son'):
            husband = m if ds == 'master' else event.get('son', m + '-son')
            return [E_('wife_taken', d, cp=husband, value=maidservant('designation')['v'], law='X1 [INK 21:8-9 "who designated her" / "for his son he designates her" — %s]' % maidservant('designation')['why'][:70]),
                    E_('not_diminished', husband, cp=d, value=maidservant('the_three')['v'], law='X1 [INK 21:10 "her food, her clothing and her conjugal right he shall not diminish"; 21:9 "as the law of the daughters" — the pointer INTERNAL]')]
        if event.get('signs'):
            return [E_('goes_free', d, cp=m, value='without_money — youth (the signs)', law='X1 [INK 21:11 "without money" — %s; Mishnah Kiddushin 1:2 by the signs]' % maidservant('the_two_exits')['why'][:60])]
        if event.get('matured'):
            return [E_('goes_free', d, cp=m, value='free — maturity', law='X1 [INK 21:11 "she shall go out free" — the days of maturity (Kiddushin 4a:3)]')]
        if event.get('redeemed'):
            return [E_('goes_free', d, cp=m, value='redeemed — ' + maidservant('redemption')['v'], law='X1 [INK 21:8 "he shall let her be redeemed" — Kiddushin 18a:5 against his will]')]
        return [E_('term_clock', d, cp=m, amount=6, value=maidservant('exits')['v'], law='X1 [INK 21:7 "not as the male slaves go out" — by the years and the jubilee (Mekhilta Nezikin 7 8 from Deut 15:12); the six years 21:2\'s, the library\'s form]'),
                E_('goes_free', d, cp=m, due=world.clock.after(6, 'year'), value='the seventh year', law='X1 [the term\'s fire — the same date six years on (the library\'s form)]'),
                E_('redemption_right', d, cp=event.get('father'), value=maidservant('redemption')['v'], law='X1 [INK 21:8 "he shall let her be redeemed"]'),
                E_('barred_from_it', m, cp=d, value='sale_to_a_foreign_people', law='X1 [INK 21:8 "to a foreign people he has no power to sell her" — %s]' % maidservant('foreign_sale')['v'])]
    if k == 'man_struck_dead':
        intent = event.get('intent')
        if intent is None:
            return []                                                # the Leviticus seat's plain rows (law_lev24 writes the death) — no Exodus branch here
        s = event['striker']
        if intent == 'unintentional':
            manner = event.get('manner', 'descent'); r = killer('refuge_by_descent')
            if r['v'][manner] == 'exile':
                return [E_('flees_to_refuge', s, value=killer('the_place')['v'], law='X2 [INK 21:13 "and he who did not lie in wait... a place where he shall flee" — %s: %s]' % (manner, r['v'][manner]))]
            return [E_('exempt', s, value='no_exile — not in the manner of descent', law='X2 [Mishnah Makkot 2:1 — %s: %s]' % (manner, r['v'][manner]))]
        if event.get('striker_role') in killer('guile_excludes')['v']:
            return [E_('exempt', s, value='without_guile — ' + event['striker_role'], law='X2 [INK 21:14 "with guile" — %s]' % killer('guile_excludes')['why'][:80])]
        out = []
        if event.get('at_altar'):
            out.append(E_('taken_from_altar', s, value=killer('the_altar')['v'], law='X2 [INK 21:14 "from My altar you shall take him to die" — %s]' % killer('the_altar')['why'][:90]))
        out.append(E_('beheaded', s, value=killer('mode')['v'], law='X2 [INK 21:14 "acts presumptuously... with guile" — %s; the mode %s]' % (killer('forewarning')['v'], killer('mode')['why'][:80])))
        return out
    if k == 'parent_struck':
        s = event['striker']
        if event.get('after_death'):
            return [E_('exempt', s, value=parent_striker('after_death')['v'], law='X2 [Mishnah Sanhedrin 11:1 — the striker after death exempt]')]
        if not event.get('wound', False):
            return [E_('exempt', s, value='no_wound', law='X2 [Mishnah Sanhedrin 11:1 — %s]' % parent_striker('wound')['v'])]
        return [E_('put_to_death', s, value=parent_striker('mode')['v'], law='X2 [INK 21:15 "he who strikes his father and his mother shall surely be put to death" — %s; %s]' % (parent_striker('wound')['v'], parent_striker('mode')['why'][:60]))]
    if k == 'slave_struck_by_master':
        m = event['master']; kind = event.get('slave_kind', 'canaanite')
        if kind == 'hebrew':
            return []                                                # 21:12's clause, not this one (Mekhilta Nezikin 20 3) — the silence
        if kind in ('half_free', 'joint'):
            return [E_('beheaded', m, value='not_wholly_his — the general clause, no day-or-two lenience', law='X3 [INK 21:21 "for he is his money" — %s]' % slave_struck('whose_slave')['why'][:100])]
        if not event.get('lethal_rod', True) or event.get('sold_before_death'):
            return [E_('exempt', m, value=slave_struck('the_rod')['v'] if not event.get('lethal_rod', True) else slave_struck('under_his_hand')['v'], law='X3 [INK 21:20 "with the rod... under his hand" — Mekhilta Nezikin 20 4-5]')]
        if event.get('died', 'under_his_hand') == 'under_his_hand':
            return [E_('avenged', m, value=slave_struck('avenged_is')['v'], law='X3 [INK 21:20 "avenged he shall be avenged" — %s]' % slave_struck('avenged_is')['why'][:80])]
        return [E_('exempt', m, value=slave_struck('a_day_or_two')['v'], law='X3 [INK 21:21 "a day or two days he stands, he shall not be avenged, for he is his money"]')]
    if k == 'burglar_found':
        th = event['thief']; hh = event['householder']; out = []
        blood = 'yes' if (event.get('known_peaceful') or event.get('relation') == 'father') else 'no'
        why = burglar('the_father')['v'] if event.get('relation') == 'father' else (burglar('the_sun')['v'] if blood == 'yes' else burglar('judged_by_his_end')['v'])
        out.append(E_('has_blood', th, cp=hh, value=blood + ' — ' + why, law='X4 [INK 22:1 "he has no blood" / 22:2 "he has blood" — %s%s]' % (why, '; the Sabbath the same' if event.get('on_sabbath') else '')))
        if event.get('struck_dead'):
            if blood == 'no':
                out.append(E_('exempt', hh, value='no_blood — ' + burglar('struck_by_whom')['v'], law='X4 [INK 22:1 "and is struck and dies, he has no blood" — Sanhedrin 72b:6-8]'))
            else:
                out.append(E_('put_to_death', hh, value='as_a_murderer', law='X4 [INK 22:2 "he has blood" — Mekhilta Nezikin continuation 2 1-2: he knew he was at peace with him and killed him — liable]'))
        if event.get('broke_vessel'):
            b = burglar('the_barrel')['v']
            out.append(E_('exempt', th, value=b['no_blood'], law='X4 [Mishnah Sanhedrin 8:6 — no blood: exempt from the barrel]') if blood == 'no'
                       else E_('pays', th, cp=hh, value=b['blood'], law='X4 [Mishnah Sanhedrin 8:6 — blood: liable for the barrel]'))
        if not event.get('struck_dead'):
            if event.get('has_means', True):
                out.append(E_('pays', th, cp=hh, value='the_theft', law='X4 [INK 22:2 "he shall surely pay"]'))
            elif event.get('thief_sex', 'male') == 'female':
                out.append(E_('pays', th, cp=hh, value=burglar('the_woman')['v'], law='X4 [INK 22:2 "sold for HIS theft" — %s]' % burglar('the_woman')['why'][:70]))
            else:
                out += [E_('sold_for_theft', th, cp=hh, value=burglar('the_sale')['v'], law='X4 [INK 22:2 "if he has nothing, he is sold for his theft" — %s]' % burglar('the_sale')['why'][:90]),
                        E_('term_clock', th, cp=hh, amount=6, value='six_years', law='X4 [INK 21:2 by reference — Mekhilta Nezikin continuation 2 3; the library\'s form]'),
                        E_('goes_free', th, cp=hh, due=world.clock.after(6, 'year'), value='the seventh year', law='X4 [the term\'s fire — the same date six years on]')]
        return out
    return []


def scene():
    """THE SCENE — the recorded rows replayed on the world engine (the count epoch: the day the base unit, the year derived);
    every submit a literal; the tuple predicted by scratchpad o7_predict.py before this file was typed."""
    with contextlib.redirect_stdout(io.StringIO()):
        w = WE.World(era='Mishpatim pass 3: the five case heads on the engine (the count epoch: the day the base unit, the year derived)', epoch='count')
        w.laws = [law_mishpatim_3]
        w.advance(w.clock.at_year(1))
        w.submit({'kind': 'daughter_sold', 'subject': 'the-daughter', 'father': 'the-father', 'daughter': 'the-daughter', 'master': 'the-master', 'seller': 'father', 'daughter_age': 'minor', 'case_source': 'Exod 21:7-8; Mishnah Kiddushin 1:2 — the minor sold by her father: the years, the redemption, no foreign sale'})
        w.submit({'kind': 'daughter_sold', 'subject': 'the-daughter-designated', 'father': 'the-father', 'daughter': 'the-daughter-designated', 'master': 'the-master-designating', 'designated_for': 'master', 'case_source': 'Exod 21:8-10; Kiddushin 18b-19a — designated for himself: betrothal with her consent, the three not diminished'})
        w.submit({'kind': 'daughter_sold', 'subject': 'the-daughter-for-the-son', 'father': 'the-father', 'daughter': 'the-daughter-for-the-son', 'master': 'the-master-with-a-son', 'son': 'the-son', 'designated_for': 'son', 'case_source': 'Exod 21:9; Mekhilta Nezikin 9 — designated for his son, as the law of the daughters'})
        w.submit({'kind': 'daughter_sold', 'subject': 'the-daughter-with-signs', 'father': 'the-father', 'daughter': 'the-daughter-with-signs', 'master': 'the-master', 'signs': True, 'case_source': 'Exod 21:11; Mishnah Kiddushin 1:2 — the signs: without money, the days of youth'})
        w.submit({'kind': 'daughter_sold', 'subject': 'the-daughter-matured', 'father': 'the-father', 'daughter': 'the-daughter-matured', 'master': 'the-master', 'matured': True, 'case_source': 'Exod 21:11; Kiddushin 4a:3 — free: the days of maturity'})
        w.submit({'kind': 'daughter_sold', 'subject': 'the-daughter-redeemed', 'father': 'the-father', 'daughter': 'the-daughter-redeemed', 'master': 'the-master', 'redeemed': True, 'case_source': 'Exod 21:8; Kiddushin 18a:5 — redeemed against his will'})
        w.submit({'kind': 'daughter_sold', 'subject': 'the-daughter-sold-by-mother', 'father': 'the-mother', 'daughter': 'the-daughter-sold-by-mother', 'master': 'the-master', 'seller': 'mother', 'case_source': 'Mishnah Sotah 3:8; Mekhilta Nezikin 7 2 — the woman does not sell her daughter: the silence'})
        w.submit({'kind': 'daughter_sold', 'subject': 'the-bogeret', 'father': 'the-father', 'daughter': 'the-bogeret', 'master': 'the-master', 'daughter_age': 'bogeret', 'case_source': 'Mekhilta Nezikin 7 1 — a minor only: the silence'})
        w.advance(w.clock.at_year(2))
        w.submit({'kind': 'man_struck_dead', 'subject': 'the-roller', 'striker': 'the-roller', 'victim': 'the-passer-by', 'intent': 'unintentional', 'manner': 'descent', 'case_source': 'Exod 21:13; Mishnah Makkot 2:1 — rolling down: exile'})
        w.submit({'kind': 'man_struck_dead', 'subject': 'the-puller', 'striker': 'the-puller', 'victim': 'the-passer-by', 'intent': 'unintentional', 'manner': 'ascent', 'case_source': 'Mishnah Makkot 2:1 — pulling up: no exile'})
        w.submit({'kind': 'man_struck_dead', 'subject': 'the-schemer', 'striker': 'the-schemer', 'victim': 'his-fellow', 'intent': 'deliberate', 'guile': True, 'at_altar': True, 'case_source': 'Exod 21:14; Sanhedrin 41a:2, 52b:13; Yoma 85a:15 — warned and deliberate, at the altar: taken to die by the sword'})
        w.submit({'kind': 'man_struck_dead', 'subject': 'the-physician', 'striker': 'the-physician', 'victim': 'the-patient', 'intent': 'deliberate', 'striker_role': 'physician_who_killed', 'case_source': 'Mekhilta Nezikin 14 3; Mishnah Makkot 2:2 — the physician who killed: without guile'})
        w.submit({'kind': 'parent_struck', 'subject': 'the-son-who-wounded', 'striker': 'the-son-who-wounded', 'parent': 'his-father', 'wound': True, 'case_source': 'Exod 21:15; Mishnah Sanhedrin 11:1 — a wound: strangled'})
        w.submit({'kind': 'parent_struck', 'subject': 'the-son-who-struck', 'striker': 'the-son-who-struck', 'parent': 'his-mother', 'wound': False, 'case_source': 'Mishnah Sanhedrin 11:1 — no wound: exempt'})
        w.submit({'kind': 'parent_struck', 'subject': 'the-son-after-death', 'striker': 'the-son-after-death', 'parent': 'his-father', 'wound': True, 'after_death': True, 'case_source': 'Mishnah Sanhedrin 11:1 — the striker after death exempt'})
        w.advance(w.clock.at_year(3))
        w.submit({'kind': 'slave_struck_by_master', 'subject': 'the-master-with-the-rod', 'master': 'the-master-with-the-rod', 'slave': 'the-canaanite-slave', 'slave_kind': 'canaanite', 'lethal_rod': True, 'died': 'under_his_hand', 'case_source': 'Exod 21:20; Sanhedrin 52b:13 — under his hand: avenged by the sword'})
        w.submit({'kind': 'slave_struck_by_master', 'subject': 'the-master-of-the-lingering', 'master': 'the-master-of-the-lingering', 'slave': 'the-lingering-slave', 'slave_kind': 'canaanite', 'lethal_rod': True, 'died': 'after_a_day', 'case_source': 'Exod 21:21; Mekhilta Nezikin 21 1 — a day that is like two days: not avenged'})
        w.submit({'kind': 'slave_struck_by_master', 'subject': 'the-master-of-the-hebrew', 'master': 'the-master-of-the-hebrew', 'slave': 'the-hebrew-slave', 'slave_kind': 'hebrew', 'lethal_rod': True, 'died': 'under_his_hand', 'case_source': 'Mekhilta Nezikin 20 3 — the Hebrew slave: 21:12\'s clause, the silence here'})
        w.submit({'kind': 'slave_struck_by_master', 'subject': 'the-master-of-the-half-free', 'master': 'the-master-of-the-half-free', 'slave': 'the-half-free', 'slave_kind': 'half_free', 'lethal_rod': True, 'died': 'after_a_day', 'case_source': 'Mekhilta Nezikin 20 3 (Rabbi Yitzchak, Rabbi Yishmael) — not wholly his: no day-or-two lenience'})
        w.advance(w.clock.at_year(4))
        w.submit({'kind': 'burglar_found', 'subject': 'the-stranger-thief', 'householder': 'the-householder', 'thief': 'the-stranger-thief', 'in_tunnel': True, 'struck_dead': True, 'broke_vessel': True, 'relation': 'stranger', 'case_source': 'Exod 22:1; Mishnah Sanhedrin 8:6 — no blood: the killer clear, the barrel exempt'})
        w.submit({'kind': 'burglar_found', 'subject': 'the-peaceful-thief', 'householder': 'the-householder-who-killed-the-peaceful', 'thief': 'the-peaceful-thief', 'in_tunnel': True, 'struck_dead': True, 'broke_vessel': True, 'known_peaceful': True, 'case_source': 'Exod 22:2; Mekhilta continuation 2 1-2; Sanhedrin 72a:15-16 — clear as the sun that he is at peace: blood; the killer liable, the barrel paid'})
        w.submit({'kind': 'burglar_found', 'subject': 'the-father-thief', 'householder': 'the-son-householder', 'thief': 'the-father-thief', 'in_tunnel': True, 'relation': 'father', 'case_source': 'Sanhedrin 72b:1-2 — the father against the son: presumed merciful, blood'})
        w.submit({'kind': 'burglar_found', 'subject': 'the-thief-with-means', 'householder': 'the-householder', 'thief': 'the-thief-with-means', 'in_tunnel': True, 'has_means': True, 'case_source': 'Exod 22:2 — he shall surely pay'})
        w.submit({'kind': 'burglar_found', 'subject': 'the-thief-without-means', 'householder': 'the-householder', 'thief': 'the-thief-without-means', 'in_tunnel': True, 'has_means': False, 'case_source': 'Exod 22:2; Mekhilta continuation 2 3; Kiddushin 18a:8 — sold for his theft: six years, for the principal'})
        w.submit({'kind': 'burglar_found', 'subject': 'the-woman-thief', 'householder': 'the-householder', 'thief': 'the-woman-thief', 'in_tunnel': True, 'has_means': False, 'thief_sex': 'female', 'case_source': 'Mishnah Sotah 3:8; Sotah 23b:12 — the woman is not sold for her theft'})
        w.submit({'kind': 'burglar_found', 'subject': 'the-sabbath-thief', 'householder': 'the-householder-on-the-sabbath', 'thief': 'the-sabbath-thief', 'in_tunnel': True, 'struck_dead': True, 'on_sabbath': True, 'case_source': 'Sanhedrin 72b:3-5 — on the Sabbath the same'})
        w.advance(w.clock.at_year(8))                                       # the daughter's six-year term fires at the seventh; the thief's waits
    n = lambda eid, eff: len([e for e in w.entity(eid).ledger if e['effect'] == eff])
    tset = len([l for l in w.log if l[0] == 'TIMER-SET']); fired = len([l for l in w.log if l[0] == 'TIMER-FIRE'])
    return ((n('the-daughter', 'term_clock'), n('the-daughter', 'redemption_right'), n('the-master', 'barred_from_it'),
             n('the-daughter-designated', 'wife_taken'), n('the-master-designating', 'not_diminished'), n('the-daughter-for-the-son', 'wife_taken'), n('the-son', 'not_diminished'),
             n('the-daughter-with-signs', 'goes_free'), n('the-daughter-matured', 'goes_free'), n('the-daughter-redeemed', 'goes_free'),
             n('the-daughter-sold-by-mother', 'term_clock'), n('the-bogeret', 'term_clock'),
             n('the-roller', 'flees_to_refuge'), n('the-puller', 'exempt'), n('the-schemer', 'taken_from_altar'), n('the-schemer', 'beheaded'), n('the-physician', 'exempt'),
             n('the-son-who-wounded', 'put_to_death'), n('the-son-who-struck', 'exempt'), n('the-son-after-death', 'exempt'),
             n('the-master-with-the-rod', 'avenged'), n('the-master-of-the-lingering', 'exempt'), n('the-master-of-the-hebrew', 'avenged'), n('the-master-of-the-hebrew', 'beheaded'), n('the-master-of-the-half-free', 'beheaded'),
             n('the-stranger-thief', 'has_blood'), n('the-householder', 'exempt'), n('the-stranger-thief', 'exempt'),
             n('the-peaceful-thief', 'has_blood'), n('the-householder-who-killed-the-peaceful', 'put_to_death'), n('the-peaceful-thief', 'pays'),
             n('the-father-thief', 'has_blood'), n('the-thief-with-means', 'pays'), n('the-thief-without-means', 'sold_for_theft'), n('the-thief-without-means', 'term_clock'),
             n('the-woman-thief', 'sold_for_theft'), n('the-woman-thief', 'pays'), n('the-sabbath-thief', 'has_blood'), n('the-householder-on-the-sabbath', 'exempt'),
             tset, fired, w.clock.year), w)
SCENE, _W = scene()

# ---- (5) the graded rows — (row, cell, expected literal) ----------------
TESTS = [
 ('THE SCENE — Kiddushin 1:2, Makkot 2:1-3, Sanhedrin 8:6, 9:1, 11:1, Sotah 3:8 and the Mekhilta\'s rows on the world engine (THE COUNT EPOCH; the tuple predicted by script before this file was typed)',
  cell(SCENE, I, 'the daughter\'s term and redemption, the designation and the three, the two exits, the mother\'s and the bogeret\'s silence; the refuge by descent, the altar and the sword, the guile\'s exclusion, the parent\'s wound; the rod, the day, the Hebrew\'s silence, the half-free; the tunnel\'s blood and the barrel, the father, the sale and the woman, the Sabbath',
       ['term_clock', 'goes_free', 'redemption_right', 'barred_from_it', 'wife_taken', 'not_diminished', 'flees_to_refuge', 'exempt', 'taken_from_altar', 'beheaded', 'put_to_death', 'avenged', 'has_blood', 'pays', 'sold_for_theft']),
  # the prediction (scratchpad o7_predict.py) typed slot 34 — the insolvent thief's term_clock — as 0, modeling the effect as written at its
  # FIRE (year 10, beyond the scene); the first run returned 1: the library's term form (law_slave_term) writes term_clock AT ONCE and
  # carries the freedom as the timer — the miss is the hand-model's, recorded here, the literal corrected beside it (O7, 2026-09-07)
  (1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 2, 1, 8)),
 # X1
 ('Exod 21:7; Mishnah Sotah 3:8 — the man sells his daughter, the woman does not', maidservant('who_sells'), 'the_father_alone'),
 ('Mekhilta Nezikin 7 1 — a minor: the signs take her out', maidservant('her_age'), 'a_minor'),
 ('Mishnah Kiddushin 1:2 — the maidservant\'s exits: the years, the jubilee, the deduction, and the SIGNS [ANSWER-SHEET]', maidservant('exits'), ['years', 'jubilee', 'deduction', 'signs']),
 ('Kiddushin 18b:3-4, 19a:7 — designation is betrothal, with her consent', maidservant('designation'), 'betrothal_with_her_consent'),
 ('Exod 21:10 — the three: food, clothing, conjugal right', maidservant('the_three'), ['food', 'clothing', 'conjugal_right']),
 ('Kiddushin 4a:3 — free: maturity; without money: youth', maidservant('the_two_exits'), {'free': 'maturity', 'without_money': 'youth'}),
 ('Kiddushin 3b:5 — no money for this master, money for the father', maidservant('money_for_another'), 'the_father'),
 ('Mekhilta Nezikin 11 1 — "these three": designate, designate for the son, redeem', maidservant('these_three'), ['designate_for_himself', 'designate_for_his_son', 'redeem']),
 ('Kiddushin 18a:5 — redeemed against his will', maidservant('redemption'), 'against_his_will'),
 ('Mekhilta Nezikin 8 3 — the foreign sale barred: a warning to the court', maidservant('foreign_sale'), 'barred_a_warning_to_the_court'),
 # X2
 ('Mishnah Makkot 2:1 — descent exiles, ascent does not [ANSWER-SHEET]', killer('refuge_by_descent'), {'descent': 'exile', 'ascent': 'no_exile'}),
 ('Mekhilta Nezikin 13 2 — the place: the Levites\' cities for the generations, the camps for the hour', killer('the_place'), 'levite_cities_for_the_generations_levite_camps_for_the_hour'),
 ('Mishnah Makkot 2:3 — the father for the son, the son for the father [ANSWER-SHEET]', killer('father_and_son'), 'each_exiles_for_the_other'),
 ('Mekhilta Nezikin 14 1-3 — "with guile" excludes six', killer('guile_excludes'), ['deaf_mute', 'minor', 'physician_who_killed', 'court_agent', 'father_disciplining', 'teacher']),
 ('Sanhedrin 41a:2 — with guile: warned and still deliberate', killer('forewarning'), 'warned_and_still_deliberate'),
 ('Yoma 85a:15 — from beside My altar, not from upon it', killer('the_altar'), 'from_beside_not_from_upon'),
 ('Mishnah Sanhedrin 9:1; Sanhedrin 52b:13 — the murderer\'s mode: the sword', killer('mode'), 'the_sword'),
 ('Mekhilta Nezikin 14 2 — "his fellow" includes the minor victim', killer('his_fellow'), 'includes_the_minor_victim'),
 ('Mishnah Sanhedrin 11:1 — the parent struck: a blow with a wound [ANSWER-SHEET]', parent_striker('wound'), 'a_blow_with_a_wound'),
 ('Mishnah Sanhedrin 11:1 — among the strangled [ANSWER-SHEET]', parent_striker('mode'), 'strangling'),
 ('Mishnah Sanhedrin 11:1 — the striker after death exempt [ANSWER-SHEET]', parent_striker('after_death'), 'exempt'),
 ('Mekhilta Nezikin 15 2 — either parent', parent_striker('either_parent'), 'either'),
 ('Mekhilta Nezikin 17 1 — the woman included from "and he who curses"', parent_curser('the_woman'), 'included'),
 ('Exod 21:17 by CALL into Lev 20:9\'s seat — the mode: stoning', parent_curser('mode'), 'stoning'),
 ('Exod 21:17 by CALL — either parent suffices', parent_curser('one_parent'), 'either_parent_suffices'),
 ('Exod 21:17 by CALL — the curser after death liable', parent_curser('after_death'), 'liable'),
 ('Exod 21:17 by CALL — by the Name (Mishnah Sanhedrin 7:8)', parent_curser('by_the_name'), 'liable'),
 # X3
 ('Mekhilta Nezikin 20 3 — whose slave: the Canaanite wholly his', slave_struck('whose_slave'), 'the_canaanite_wholly_his'),
 ('Mekhilta Nezikin 20 4 — the rod: a thing that can kill', slave_struck('the_rod'), 'a_thing_that_can_kill_at_a_place_that_can_kill'),
 ('Mekhilta Nezikin 20 5 — under his hand', slave_struck('under_his_hand'), 'the_blow_and_the_death_in_his_domain'),
 ('Mekhilta Nezikin 20 6; Sanhedrin 52b:13 — avenged: death by the sword', slave_struck('avenged_is'), 'death_by_the_sword'),
 ('Mekhilta Nezikin 21 1 — a day or two: from time to time', slave_struck('a_day_or_two'), 'from_time_to_time_twenty_four_hours'),
 ('Bava Kamma 90a:5-8 — "his money": the four arms [ANSWER-SHEET]', slave_struck('his_money_arms'), ['first_master — Rabbi Meir', 'second_master — Rabbi Yehuda', 'both — Rabbi Yose', 'neither — Rabbi Eliezer']),
 # X4
 ('Sanhedrin 72a:4 — the doubt: to steal or to kill', burglar('the_doubt'), 'came_to_steal_or_to_kill'),
 ('Mishnah Sanhedrin 8:6 — judged by his end: no blood [ANSWER-SHEET]', burglar('judged_by_his_end'), 'no_blood'),
 ('Mekhilta continuation 2 1 — the sun: clarity that he is at peace', burglar('the_sun'), 'clarity_that_he_is_at_peace'),
 ('Sanhedrin 72b:1-2 — the father presumed merciful', burglar('the_father'), 'presumed_merciful'),
 ('Sanhedrin 72b:6-8 — struck by any person, by any death', burglar('struck_by_whom'), 'any_person_any_death'),
 ('Mishnah Sanhedrin 8:6 — the barrel: no blood exempt, blood pays [ANSWER-SHEET]', burglar('the_barrel'), {'no_blood': 'exempt', 'blood': 'pays'}),
 ('Sanhedrin 72b:3-5 — the Sabbath the same, the pile cleared', burglar('the_sabbath'), 'the_same_and_the_pile_cleared'),
 ('Mekhilta continuation 2 3; Kiddushin 18a:8 — sold six years for the principal', burglar('the_sale'), 'six_years_for_the_principal'),
 ('Mishnah Sotah 3:8; Sotah 23b:12 — the woman is not sold [ANSWER-SHEET]', burglar('the_woman'), 'not_sold'),
]

if __name__ == '__main__':
    print()
    ok = 0
    frac = {I: 0, M: 0, A: 0, D: 0, H: 0}
    for name, c, want in TESTS:
        hit = c['v'] == want
        ok += hit
        frac[c['p']] += 1
        print('%s %-76s [%s] %s' % ('OK ' if hit else 'MISS', name[:76], c['p'], '' if hit else 'got=%r' % (c['v'],)))
        print('     effects: %s' % ', '.join(c['fx']))
    n = len(TESTS)
    assert n == GUARDED, (n, GUARDED)
    print()
    print('MATRIX: %d/%d cells match the answer sheet' % (ok, n))
    print('FRACTIONS: pure ink %d/%d (%d%%) · recorded moves %d/%d (%d%%) · answer-sheet %d/%d · data %d/%d · hypotheses %d/%d' % (
          frac[I], n, 100 * frac[I] // n, frac[M], n, 100 * frac[M] // n, frac[A], n, frac[D], n, frac[H], n))
    print('effects: every cell carries REGISTERED effects — four discovered in this span\'s own verbs: taken_from_altar, beheaded, not_diminished, has_blood [effects law satisfied]')
    _W.print_coverage()
    if ok == n:
        print()
        print('THE FIVE CASE HEADS STAND — the daughter\'s sale with its designation, its three and its two exits; the refuge by descent and the altar\'s sword; the parents\' wound and the curser\'s second seat by call; the rod, the day and "his money"; the tunnel\'s blood, the barrel, the sale for six years and the woman not sold.')
    else:
        sys.exit('MISSES REMAIN — consult the Talmud per gap and recompile.')

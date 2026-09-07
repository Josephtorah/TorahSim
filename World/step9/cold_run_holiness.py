#!/usr/bin/env python3
"""cold_run_holiness.py — THE HOLINESS LEDGER, FIRST HALF (Lev 19:1-18)
(2026-09-06, sitting L4a of THE COMPILE DEBT — World/step9/COMPILE_DEBT.md).

Span: Lev 19:1-18 — the charge (holy = separate), parents and Sabbaths,
the idols, the shelamim's two-day window with its rejection and karet,
THE POOR GIFTS (the corner, the gleanings, the small clusters, the
fallen grapes — left for the poor and the convert), theft-denial-lying-
the false oath, oppression-robbery-THE WAGE CLOCK, the deaf and the
blind with the heart clause, THE COURT (no wrong in judgment, the poor's
face, the great's face, righteousness), the talebearer and the blood,
hate in the heart and the doubled rebuke, revenge and grudge and the
love of the neighbor.

Answer sheet ROUTED BY TOPIC under the union rule: Mishnah Peah whole,
Bava Metzia 9 whole, Bava Kamma 9-10 whole, Shevuot 5-8 whole — 130
rows read whole plus the 14 link rows outside them (the ledger
logic/oral_triage/holiness_topic_docket_2026-09-06.md, coverage
computed; 161 Talmud addresses indexed on 19:1-18, opened per gap).

The five motions, in order:
 (1) code from the BARE INK — the four reaping-tokens of 19:9; the
     four gift-nouns of 19:9-10 with the leave-verb once and 'to the
     poor and the convert' once; the five verbs of 19:11-12 in their
     written order; the six tokens of 19:13 with 'until morning'; the
     four of 19:14 with 'fear your God'; the six of 19:15 and the same
     'no wrong in judgment' clause at 19:35; 'I am the LORD' at eight
     seats of the half; 'love as yourself' at 19:18 and 19:34; every
     quantity a PARAMETER (the corner's fraction, the poor's threshold,
     the count threshold, the field's minimum, the distribution times);
 (2) the Mishnah's rows as TEST DATA, each expected value a literal
     typed from the row (the honest-pairing guard runs first);
 (3) run;
 (4) misses filled by NAMED recorded arguments — the Sifra's rows (the
     units' spine, verdicted 2026-09-05) and the Talmud where opened,
     each labeled [MOVE];
 (5) the graded matrix with per-cell provenance, fractions, and EFFECTS
     on every verdict.

Cross-span receipts, labeled [IMPORT] and, where a compiled callee
exists, CALLED: cold_run_vayikra5.deposit_restitution (Lev 5:21-26 —
the principal, the fifth, the guilt ram; the recursion; the heirs; even
to Media); cold_run_tzav.rejection_machine (Lev 7:15-18 — the window,
the leftover, the rejection and its karet); cold_run_yovel.interest
(Lev 25:36-37 — the lender under the stumbling block); Exod 22:3 (the
double), Exod 22:8 (the judges' oath), Deut 24:15 (the night wage),
Deut 24:19-21 (the forgotten sheaf, the olive, the vintage), Exod 23:11
(the release to all), Exod 22:27 (the judge and prince), Lev 25:36
(the vow-opening's fifth clause).
"""
import sqlite3, sys, os, json, io, contextlib
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import effects_layer as FX
from compile_guards import check_honest_pairing
GUARDED = check_honest_pairing(os.path.abspath(__file__))
assert GUARDED == 187, ('the guard counted %d expectations, the tripwire holds 187' % GUARDED)

DB = '<repo-old>/elijah_docket/tanakh.sqlite'
db = sqlite3.connect(DB)

def strip(s):
    return ''.join(c for c in s if c != '/' and not (0x0591 <= ord(c) <= 0x05C7))

def toks(book, ch, vs):
    rows = db.execute("""SELECT w.he FROM words w JOIN verses v
        ON w.verse_id=v.id WHERE v.book=? AND v.chapter=? AND v.verse=?
        ORDER BY w.idx""", (book, ch, vs)).fetchall()
    return [strip(r[0]) for r in rows]

def phrase(book, ch, vs, words):
    t = toks(book, ch, vs); n = len(words)
    return sum(1 for i in range(len(t) - n + 1) if t[i:i + n] == words)

HALF = list(range(1, 19)); CHAP = list(range(1, 38))
def seats(pred, rng=HALF):
    return [v for v in rng if pred(toks('Lev', 19, v))]
def has(*ws):
    return lambda t: any(t[i:i + len(ws)] == list(ws) for i in range(len(t) - len(ws) + 1))
def anytok(*ws):
    return lambda t: any(w in t for w in ws)

# ---- (1) ink probes — each MUST fire or the run refuses -------------
PROBES = [
    ('speak to ALL the assembly',                    'Lev', 19, 2, 'עדת'),
    ('HOLY shall you be',                            'Lev', 19, 2, 'קדשים'),
    ('a man his MOTHER and his father shall fear',   'Lev', 19, 3, 'אמו'),
    ('My SABBATHS you shall keep',                   'Lev', 19, 3, 'שבתתי'),
    ('turn not to the IDOLS',                        'Lev', 19, 4, 'האלילים'),
    ('MOLTEN gods',                                  'Lev', 19, 4, 'מסכה'),
    ('to your ACCEPTANCE you shall slaughter it',    'Lev', 19, 5, 'לרצנכם'),
    ('on the day of your slaughter and the MORROW',  'Lev', 19, 6, 'וממחרת'),
    ('the LEFTOVER until the third day burned',      'Lev', 19, 6, 'והנותר'),
    ('PIGUL it is, not accepted',                    'Lev', 19, 7, 'פגול'),
    ('its eater bears his iniquity, CUT OFF',        'Lev', 19, 8, 'ונכרתה'),
    ('when you REAP the harvest of your land',       'Lev', 19, 9, 'ובקצרכם'),
    ('you shall not finish the CORNER of your field', 'Lev', 19, 9, 'פאת'),
    ('the GLEANINGS of your harvest',                'Lev', 19, 9, 'ולקט'),
    ('your vineyard you shall not glean SMALL CLUSTERS', 'Lev', 19, 10, 'תעולל'),
    ('the FALLEN GRAPES of your vineyard',           'Lev', 19, 10, 'ופרט'),
    ('to the POOR and the CONVERT you shall LEAVE them', 'Lev', 19, 10, 'תעזב'),
    ('you shall not STEAL',                          'Lev', 19, 11, 'תגנבו'),
    ('you shall not DENY',                           'Lev', 19, 11, 'תכחשו'),
    ('you shall not LIE, a man against his FELLOW',  'Lev', 19, 11, 'בעמיתו'),
    ('you shall not SWEAR by My name FALSELY',       'Lev', 19, 12, 'תשבעו'),
    ('and PROFANE the name of your God',             'Lev', 19, 12, 'וחללת'),
    ('you shall not OPPRESS your neighbor',          'Lev', 19, 13, 'תעשק'),
    ('nor ROB',                                      'Lev', 19, 13, 'תגזל'),
    ('the WAGE of a hired man shall not stay overnight', 'Lev', 19, 13, 'תלין'),
    ('UNTIL MORNING',                                'Lev', 19, 13, 'בקר'),
    ('curse not the DEAF',                           'Lev', 19, 14, 'חרש'),
    ('before the BLIND put no STUMBLING BLOCK',      'Lev', 19, 14, 'מכשל'),
    ('and FEAR your God',                            'Lev', 19, 14, 'ויראת'),
    ('do no WRONG in judgment',                      'Lev', 19, 15, 'עול'),
    ('lift not the face of the POOR',                'Lev', 19, 15, 'דל'),
    ('honor not the face of the GREAT',              'Lev', 19, 15, 'גדול'),
    ('in RIGHTEOUSNESS judge your fellow',           'Lev', 19, 15, 'בצדק'),
    ('go not TALEBEARING among your people',         'Lev', 19, 16, 'רכיל'),
    ('stand not on the BLOOD of your neighbor',      'Lev', 19, 16, 'דם'),
    ('hate not your brother IN YOUR HEART',          'Lev', 19, 17, 'בלבבך'),
    ('REBUKE, you shall rebuke',                     'Lev', 19, 17, 'הוכח'),
    ('and bear no SIN upon him',                     'Lev', 19, 17, 'חטא'),
    ('take no REVENGE',                              'Lev', 19, 18, 'תקם'),
    ('bear no GRUDGE',                               'Lev', 19, 18, 'תטר'),
    ('LOVE your neighbor as yourself',               'Lev', 19, 18, 'ואהבת'),
]
missing = [p for p in PROBES if p[4] not in toks(p[1], p[2], p[3])]
if missing:
    for p in missing: print('PROBE FAILED:', p)
    sys.exit('zero-report law: the ink scan is not trusted until every probe fires')
print('probes: %d/%d fired (the ink scan is trusted)' % (len(PROBES), len(PROBES)))

# ---- the censuses (TRIPWIRES — each a measured literal) ------------
c_ani = seats(lambda t: any(t[i] == 'אני' and t[i + 1] == 'יהוה' for i in range(len(t) - 1)))
assert c_ani == [2, 3, 4, 10, 12, 14, 16, 18], c_ani
c_ani_god = seats(lambda t: any(t[i:i + 3] == ['אני', 'יהוה', 'אלהיכם'] for i in range(len(t) - 2)))
assert c_ani_god == [2, 3, 4, 10], c_ani_god
c_fear = seats(lambda t: 'ויראת' in t and 'מאלהיך' in t, CHAP)
assert c_fear == [14, 32], c_fear
c_reap = [w for w in toks('Lev', 19, 9) if 'קצ' in w]
assert len(c_reap) == 4, c_reap
c_gifts = (seats(anytok('פאת'), CHAP), seats(anytok('ולקט', 'תלקט')), seats(anytok('תעולל')), seats(anytok('ופרט')))
assert c_gifts == ([9, 27], [9, 10], [10], [10]), c_gifts
c_leave = seats(anytok('תעזב')); c_poor = seats(lambda t: 'לעני' in t and 'ולגר' in t)
assert c_leave == [10] and c_poor == [10], (c_leave, c_poor)
c_verbs = [w for w in toks('Lev', 19, 11) + toks('Lev', 19, 12) if w in ('תגנבו', 'תכחשו', 'תשקרו', 'תשבעו', 'וחללת')]
assert c_verbs == ['תגנבו', 'תכחשו', 'תשקרו', 'תשבעו', 'וחללת'], c_verbs
c_amit = seats(lambda t: any('עמית' in w for w in t)); c_rea = seats(anytok('רעך', 'לרעך')); c_ach = seats(anytok('אחיך'))
c_am = seats(anytok('עמך', 'בעמיך'))
assert (c_amit, c_rea, c_ach, c_am) == ([11, 15, 17], [13, 16, 18], [17], [16, 18]), (c_amit, c_rea, c_ach, c_am)
c_13 = [w for w in toks('Lev', 19, 13) if w in ('תעשק', 'תגזל', 'תלין', 'פעלת', 'שכיר', 'בקר')]
assert len(c_13) == 6, c_13
c_14 = [w for w in toks('Lev', 19, 14) if w in ('תקלל', 'חרש', 'עור', 'מכשל')]
assert len(c_14) == 4, c_14
c_15 = [w for w in toks('Lev', 19, 15) if w in ('עול', 'במשפט', 'דל', 'גדול', 'בצדק', 'תשפט')]
assert len(c_15) == 6, c_15
c_judge_measure = seats(has('עול', 'במשפט'), CHAP)
assert c_judge_measure == [15, 35], c_judge_measure
c_love = seats(lambda t: 'ואהבת' in t and 'כמוך' in t, CHAP)
assert c_love == [18, 34], c_love
c_17 = [w for w in toks('Lev', 19, 17) if w in ('תשנא', 'בלבבך', 'הוכח', 'תוכיח', 'חטא')]
assert len(c_17) == 5, c_17
c_18 = [w for w in toks('Lev', 19, 18) if w in ('תקם', 'תטר', 'ואהבת', 'לרעך', 'כמוך')]
assert len(c_18) == 5, c_18
c_shel = (seats(anytok('פגול')), seats(anytok('והנותר')), seats(lambda t: any('כרת' in w for w in t)), seats(lambda t: 'לא' in t and 'ירצה' in t))
assert c_shel == ([7], [6], [8], [7]), c_shel
c_parents = toks('Lev', 19, 3)[:3]
assert c_parents == ['איש', 'אמו', 'ואביו'], c_parents          # the MOTHER first here; Exod 20:12 the father first
c_shabbat = seats(anytok('שבתתי'), CHAP)
assert c_shabbat == [3, 30], c_shabbat
_t23 = toks('Lev', 23, 22); _t19 = toks('Lev', 19, 9) + toks('Lev', 19, 10)
c_copy = ([w for w in _t23 if w not in _t19], [w for w in _t19 if w not in _t23])
assert c_copy == (['בקצרך'], ['לקצר', 'וכרמך', 'תעולל', 'ופרט', 'כרמך']), c_copy   # the Emor copy has no vineyard
print('censuses: "I am the LORD" at %s (with "your God" at %s) · "fear your God" at %s of the chapter · four reaping-tokens '
      'at 19:9 %s · the corner at %s, gleanings at %s, small clusters at %s, fallen grapes at %s · leave-verb at %s · '
      'poor-and-convert at %s · the five verbs of 19:11-12 in order %s · fellow at %s, neighbor at %s, brother at %s, '
      'people at %s · 19:13 six tokens · 19:14 four · 19:15 six · "no wrong in judgment" at %s (the court and the market) '
      '· love-as-yourself at %s · 19:17 five · 19:18 five · shelamim (pigul, leftover, karet, not-accepted) at %s · 19:3 '
      'opens %s · Sabbaths at %s · 23:22 vs 19:9-10 token diff %s'
      % (c_ani, c_ani_god, c_fear, c_reap, c_gifts[0], c_gifts[1], c_gifts[2], c_gifts[3], c_leave, c_poor, c_verbs,
         c_amit, c_rea, c_ach, c_am, c_judge_measure, c_love, c_shel, c_parents, c_shabbat, c_copy))

# ---- the callees (cold) --------------------------------------------
_buf = io.StringIO()
with contextlib.redirect_stdout(_buf):
    import cold_run_vayikra5 as V5
    import cold_run_tzav as TZ
    import cold_run_yovel as YV
def deposit(**claim):
    r = V5.deposit_restitution(claim, V5.DATA)
    return r[0] if isinstance(r, tuple) else r
PIGUL = TZ.rejection_machine({'ask': 'piggul_time'}, TZ.PARAMS)
LEFTOVER = TZ.rejection_machine({'ask': 'leftover'}, TZ.PARAMS)
WINDOW = TZ.rejection_machine({'ask': 'window_vow'}, TZ.PARAMS)
PLACE = TZ.rejection_machine({'ask': 'piggul_place'}, TZ.PARAMS)
INTEREST = YV.interest()['both_nouns']['v']
def tzv(r):
    return r['v'] if isinstance(r, dict) else (r[0] if isinstance(r, tuple) else r)
print('routing receipts: cold_run_vayikra5.deposit_restitution CALLED -> %r; cold_run_tzav.rejection_machine CALLED — '
      'window -> %r, leftover -> %r, piggul_time -> %r, piggul_place -> %r; cold_run_yovel.interest CALLED -> %r '
      '[IMPORT, live calls]' % (deposit(claim_kind='deposit', swore_falsely=True, value=100)[:60], tzv(WINDOW),
                                tzv(LEFTOVER), tzv(PIGUL), tzv(PLACE), INTEREST))

I, M, A, D, P, H = 'INK', 'MOVE', 'ANSWER-SHEET', 'DATA', 'IMPORT', 'HYPOTHESIS'   # H: THE LINK REVIEW LAW (LR3, 2026-09-07) — an untaught transfer, kept and labeled, never counted as compiled
def cell(v, p, why, fx):
    FX.validate(fx)
    return {'v': v, 'p': p, 'why': why, 'fx': fx}
SK = 'Sifra, Kedoshim, '

# =====================================================================
# THE CODE — from the ink of Leviticus 19:1-18 alone. Mishnah/Talmud
# appear ONLY on [MOVE] lines (motion 4) and as DATA (motion 2).
# =====================================================================

# ---- F1: THE CHARGE, THE PARENTS, THE IDOLS (19:1-4) ------------------
def frame(q, **k):
    if q == 'assembly':
        return cell('said_in_full_assembly', I, '19:2 "speak to ALL the assembly" — the one law chapter opened so '
                    '(' + SK + 'Section 1 1: "most of the Torah\'s bodies hang on it")', [FX.NONE])
    if q == 'holy':
        return cell('separate', M, '19:2 "holy shall you be, for I am holy" — ' + SK + 'Section 1 1: holy = SEPARATE; '
                    'the retinue imitates the king (Abba Shaul); the converse refused', [FX.NONE])
    if q == 'parents_order':
        return cell('mother_first_here_father_first_at_Sinai_both_equal', I, ('19:3 opens %s — the mother before the '
                    'father, the reverse of Exod 20:12 [IMPORT]: the two orders cancel to EQUALITY (' + SK +
                    'Section 1 9; Mishnah Keritot 6:9); the sages\' father-precedence reasoned (he and his mother owe '
                    'the father\'s honor)') % (c_parents,), [FX.NONE])
    if q == 'woman_included':
        return cell('woman_bound_to_fear_when_able', M, '19:3 "you shall fear" PLURAL — ' + SK + 'Section 1 2-3: the '
                    'woman included; "a man" because he has the means in hand, she is under another\'s authority',
                    [FX.NONE])
    if q == 'fear_defined':
        return cell(['not_sit_in_his_place', 'not_speak_in_his_place', 'not_contradict_him'], M, SK + 'Section 1 10 — '
                    'FEAR defined by three abstentions', [FX.NONE])
    if q == 'honor_defined':
        return cell(['feed', 'give_drink', 'clothe', 'cover', 'bring_in', 'take_out'], M, SK + 'Section 1 10 — HONOR '
                    'defined by six services (Exod 20:12\'s honor [IMPORT])', [FX.NONE])
    if q == 'override':
        return cell('parent_ordering_a_transgression_not_obeyed', I, ('19:3 juxtaposes the parents\' fear with "MY '
                    'Sabbaths you shall keep" (the Sabbaths at %s): ' + SK + 'Section 1 10 — "ALL of you owe MY honor" '
                    '— the parent\'s order to transgress is void') % (c_shabbat,), [FX.NONE])
    if q == 'three_partners':
        return cell(['God', 'father', 'mother'], M, SK + 'Section 1 4-7 — fear, honor, cursing each LINKED to God\'s; '
                    'striking has no upward analogue; the reason: three partners in a person', [FX.NONE])
    if q == 'idols_look':
        return cell('not_even_to_look_R._Yehuda', M, '19:4 "turn not to the idols" — ' + SK + 'Section 1 10; the ten '
                    'mocking names (1 11); Onkelos 19:4 "the errors"', [FX.NONE])
    if q == 'molten_warnings':
        return cell(['two_warnings', 'R._Yosei_three'], M, '19:4 "molten gods you shall not make FOR YOU" — ' + SK +
                    'Section 1 12: none for others, none by others for you; R. Yosei adds "you shall have none"',
                    [FX.NONE])
    if q == 'ani_YHWH':
        return cell(c_ani, I, '"I am the LORD" closes the law blocks at eight seats of the half; with "your God" at '
                    'four — the signature the Sifra reads as Judge and Payer (Section 8 1)', [FX.NONE])
    if q == 'persons_all':
        return cell('androgynous_liable_to_all_commandments_as_men', A, 'Mishnah Bikkurim 4:2 — the double-sexed '
                    '"like men" bound to all the commandments; linked at 19:2\'s "all the assembly"', [FX.NONE])
    raise ValueError(q)

# ---- F1b: THE SHELAMIM'S WINDOW (19:5-8) — the Tzav engine CALLED ----
def shelamim(q):
    if q == 'intent_at_slaughter':
        return cell('slaughter_on_condition_of_two_day_eating', M, '19:5 "to your ACCEPTANCE you shall slaughter it" '
                    '— ' + SK + 'Chapter 1 1: the eating clause reassigned to the SLAUGHTER — intent at the act binds; '
                    'extended to all two-day offerings (1 2)', ['accepted'])
    if q == 'not_two_heads':
        return cell('one_at_a_time', M, '19:5 "you shall slaughter IT" — ' + SK + 'Chapter 1 3', [FX.NONE])
    if q == 'window':
        return cell(tzv(WINDOW), P, '19:6 "on the day of your slaughter it shall be eaten, and on the morrow" — CALLED '
                    'cold_run_tzav.rejection_machine(window_vow) [Lev 7:16]', ['eating_window'])
    if q == 'leftover':
        return cell(tzv(LEFTOVER), P, '19:6 "the leftover until the third day shall be burned in fire" — CALLED '
                    'cold_run_tzav.rejection_machine(leftover) [Lev 7:17]', ['burn_remainder'])
    if q == 'pigul_time':
        return cell(tzv(PIGUL), P, '19:7-8 "if eaten on the third day — pigul, not accepted; its eater bears his '
                    'iniquity... cut off" (pigul at %s, karet at %s) — CALLED cold_run_tzav.rejection_machine(piggul_'
                    'time) [Lev 7:18]' % (c_shel[0], c_shel[2]), ['not_accepted', 'karet_cut_off'])
    if q == 'pigul_place':
        return cell(tzv(PLACE), P, SK + 'Chapter 1 4 — THE REASSIGNMENT: the third-day clause redundant for wrong-TIME, '
                    'GIVEN to wrong-PLACE (M-18\'s first exemplar); CALLED rejection_machine(piggul_place)',
                    ['not_accepted'])
    if q == 'karet_building_block':
        return cell('whoever_eats_the_holy_in_violation_earns_karet', M, '19:8 "for the holy of the LORD he profaned" — '
                    + SK + 'Chapter 1 5: a building block', ['karet_cut_off'])
    if q == 'eater_lashes':
        return cell('lashed_when_warned', P, 'Mishnah Makkot 3:2 — notar and pigul in the lash list (Deut 25:2-3 '
                    '[IMPORT]); the karet stands beside', ['lashes'])
    raise ValueError(q)

# ---- F2: THE POOR-GIFTS ENGINE (19:9-10; Mishnah Peah whole) ----------
GIFTS_INK = {'corner': 9, 'gleanings': 9, 'small_clusters': 10, 'fallen_grapes': 10}
GIFTS_IMPORT = {'forgotten_sheaf': 'Deut 24:19', 'forgotten_olive': 'Deut 24:20', 'poor_tithe': 'Deut 14:28'}
FIVE = ('food', 'guarded', 'land_grown', 'gathered_as_one', 'stored')
def classify(item):
    """Mishnah Peah 1:4 — the five-predicate classifier (Sifra Kedoshim Chapter 1 7)."""
    owes = all(item.get(p, False) for p in FIVE)
    return cell('owes_corner' if owes else 'exempt', M, ('"the harvest of your LAND" (19:9) read by five predicates — ' +
                SK + 'Chapter 1 7 VERBATIM: food, guarded, land-grown, gathered as one, stored for keeping; the failed: '
                '%s') % ([p for p in FIVE if not item.get(p, False)],), ['left_for_the_poor'] if owes else ['exempt'])

def gifts(q, **k):
    if q == 'kinds':
        return cell(sorted(GIFTS_INK), I, 'the four gift-nouns of 19:9-10 (corner %s, gleanings %s, small clusters %s, '
                    'fallen grapes %s); the forgotten sheaf and olive are Deut 24:19-20\'s [IMPORT], the poor tithe '
                    'Deut 14:28\'s' % c_gifts, ['left_for_the_poor'])
    if q == 'recipients':
        return cell('the_poor_and_the_convert_not_the_resident_alien', I, ('19:10 "to the POOR and the CONVERT you shall '
                    'leave them" (%s) — ' + SK + 'Chapter 3 4: the convert a covenant member, not the resident alien') % (c_poor,), ['left_for_the_poor'])
    if q == 'measure':
        return cell('no_measure_in_the_ink', I, '19:9 writes "you shall not FINISH the corner" and no fraction — the '
                    'quantity is a PARAMETER (Mishnah Peah 1:1: the corner has no measure)', ['left_for_the_poor'])
    if q == 'floor':
        return cell('one_sixtieth_by_field_poor_and_humility', D, 'Mishnah Peah 1:2 — "not less than one-sixtieth, '
                    'though they said it has no measure"; ' + SK + 'Chapter 1 9: the last sixtieth must stand; the '
                    'three scaling factors data', ['left_for_the_poor'])
    if q == 'position':
        return cell('attaches_at_the_finish_start_or_middle_counts_if_the_end_holds_the_measure', M, '19:9 "you shall '
                    'not FINISH" — ' + SK + 'Chapter 1 9: the corner attaches at the finish, needs a name, sits at the '
                    'end; given at start or middle it counts (Peah 1:3; R. Shimon\'s end-measure; R. Yehuda\'s one '
                    'stalk)', ['left_for_the_poor'])
    if q == 'four_reasons':
        return cell(['robbery_of_the_poor', 'idling_of_the_poor', 'appearances', 'the_Torah_said_so'], M, SK +
                    'Chapter 1 10 — R. Shimon\'s four reasons the corner sits at the end', [FX.NONE])
    if q == 'trees':
        return cell(['sumac', 'carobs', 'nuts', 'almonds', 'vines', 'pomegranates', 'olives', 'dates'], M, SK +
                    'Chapter 1 8 VERBATIM — the tree census (Peah 1:5); the fig fails "gathered as one"', ['left_for_the_poor'])
    if q == 'window_end':
        return cell('until_the_smoothing', A, 'Mishnah Peah 1:6 — the corner given and tithes exempt until he SMOOTHS '
                    'the pile (the tithe threshold Maasrot\'s [ROUTED])', ['left_for_the_poor'])
    if q == 'divides':
        f = k['feature']
        YES = {'stream', 'channel', 'private_road', 'public_road', 'public_path', 'private_path_fixed_both_seasons',
               'fallow', 'plowed', 'another_seed'}
        if f in YES:
            return cell('divides', M, '"YOUR field" (19:9) per field — ' + SK + 'Chapter 2 1 VERBATIM (Peah 2:1): the '
                        'divider list', [FX.NONE])
        if f == 'fodder_cut':
            return cell(['divides_R._Meir', 'only_if_plowed_sages'], M, SK + 'Chapter 2 1 — the fodder-cut dispute', [FX.NONE])
        if f == 'water_channel_not_reapable_as_one':
            return cell('divides_R._Yehuda', M, SK + 'Chapter 2 2 (Peah 2:2)', [FX.NONE])
        if f == 'terraced_hills':
            return cell('one_corner_for_all', M, SK + 'Chapter 2 2 — hills worked by the hoe (Peah 2:2)', ['left_for_the_poor'])
        if f == 'fence_for_trees':
            return cell('divides_trees_only_a_fence', M, SK + 'Chapter 2 3 (Peah 2:3)', [FX.NONE])
        if f == 'meshing_canopy':
            return cell('does_not_divide_one_corner', M, SK + 'Chapter 2 3 — the interlocking crowns rejoin the orchard',
                        ['left_for_the_poor'])
        if f == 'carobs':
            return cell('all_that_see_one_another_one_corner', M, SK + 'Chapter 2 4 VERBATIM (Peah 2:4) — line of sight',
                        ['left_for_the_poor'])
    if q == 'identity':
        kinds, floors = k['kinds'], k['floors']
        n = kinds if kinds > 1 else 1
        if kinds == 1 and k.get('same_species_varieties'):
            n = floors
        return cell(n, M, 'Mishnah Peah 2:5 — one kind even in two floors: one; two kinds even in one floor: two; two '
                    'kinds of wheat: by the floors — the field\'s identity = the kind and the floor (' + SK +
                    'Chapter 1 11 per field; "another seed" divides, Chapter 2 1); 2:6 self-labels the wheat rule a '
                    'law to Moses from Sinai (data)', ['left_for_the_poor'])
    if q == 'reaped_by':
        who = k['who']
        if who in ('robbers', 'cutheans', 'ants', 'wind', 'beast'):
            return cell('exempt', I, ('19:9 "when YOU reap" — the four reaping-tokens %s; ' + SK + 'Chapter 1 6 VERBATIM: '
                        'not what robbers reaped, ants nibbled, wind or beast broke (Peah 2:7)') % (c_reap,), ['exempt'])
        if who == 'half_robbers_half_he_after':
            return cell('exempt_duty_on_the_standing_crop', M, 'Peah 2:7 — the corner\'s duty is on the STANDING crop '
                        '(19:9\'s "harvest")', ['exempt'])
        if who == 'robbers_half_then_he_half':
            return cell('corner_from_what_he_reaped', M, 'Peah 2:8', ['left_for_the_poor'])
        if who == 'sold_half':
            return cell('the_buyer_gives_for_all', M, 'Peah 2:8', ['left_for_the_poor'])
        if who == 'consecrated_half':
            return cell('the_redeemer_gives_for_all', M, 'Peah 2:8', ['left_for_the_poor'])
        if who == 'gentile_then_converted':
            return cell(['exempt_from_leket_shikchah_peah', 'R._Yehuda_liable_in_shikchah'], M, SK + 'Chapter 1 6 '
                        'VERBATIM — the gentile\'s own reaping excluded (Peah 4:6); R. Yehuda: the forgotten sheaf '
                        'begins at the binding', ['exempt'])
    if q == 'patches':
        c = k['case']
        if c == 'grain_between_olives':
            return cell(['Shammai_each', 'Hillel_one_for_all', 'both_one_if_row_heads_mixed'], A, 'Peah 3:1', ['left_for_the_poor'])
        if c == 'patchy_harvest_moist_stalks':
            return cell(['R._Akiva_each', 'sages_one_for_all', 'both_each_for_dill_or_mustard_in_three'], A, 'Peah 3:2',
                        ['left_for_the_poor'])
        if c == 'onions_market_and_floor':
            return cell('separate_corners', A, 'Peah 3:3', ['left_for_the_poor'])
        if c == 'onion_mothers':
            return cell(['liable', 'R._Yosei_exempt'], A, 'Peah 3:4 — the classifier\'s stored predicate at the '
                        'vegetable boundary', ['left_for_the_poor'])
    if q == 'owners':
        c = k['case']
        v = {'brothers_divided': 2, 'brothers_rejoined': 1, 'two_bought_a_tree': 1, 'north_and_south': 'each_his_own',
             'tree_stalks_sold': 'each_unless_the_owner_kept_some_R._Yehuda'}[c]
        return cell(v, M, '"YOUR field" (19:9) — ' + SK + 'Chapter 1 11: ownership defines the unit (Peah 3:5)',
                    ['left_for_the_poor'])
    if q == 'field_minimum':
        return cell({'R._Eliezer': 'quarter_kav_ground', 'R._Yehoshua': 'yields_two_seahs', 'R._Tarfon': 'six_by_six',
                     'R._Yehuda_b._Beteira': 'enough_to_reap_and_repeat_THE_LAW', 'R._Akiva': 'any_ground'}, D,
                    'Peah 3:6 — the threshold is data with the ruled setting recorded', [FX.NONE])
    if q == 'attached':
        return cell('given_attached_to_the_ground_the_poor_scramble', M, '19:10 "you shall LEAVE them" — ' + SK +
                    'Chapter 3 5: lay them down and the poor scramble; even ninety-nine for division against one for the '
                    'scramble — the one is heeded (Peah 4:1)', ['left_for_the_poor'])
    if q == 'trellis':
        return cell('the_owner_brings_down_and_divides_even_ninety_nine_against_one', M, SK + 'Chapter 3 5-6 — the '
                    'danger class (the trellised vine, the palm; R. Shimon the smooth nuts): division (Peah 4:1-2)',
                    ['left_for_the_poor'])
    if q == 'seizing':
        return cell('threw_on_the_rest_nothing_fell_or_cloak_removed', A, 'Peah 4:3 — the poor acquire by the hand, not by '
                    'covering; likewise leket and the forgotten sheaf', [FX.NONE])
    if q == 'no_sickles':
        return cell('no_sickles_or_axes_that_they_not_strike_each_other', M, 'Peah 4:4 — a fence on the scramble (' + SK +
                    'Chapter 3 6\'s danger reasoning)', [FX.NONE])
    if q == 'three_times':
        return cell(['morning', 'noon', 'afternoon'], D, 'Peah 4:5 — Rabban Gamliel not fewer, R. Akiva not more; the '
                    'house of Namer per row', ['left_for_the_poor'])
    if q == 'moment':
        st = k['state_at_reaping']
        return cell('liable' if st == 'liable' else 'exempt', I, '19:9 "WHEN you reap" — the status at the moment of '
                    'reaping decides (Peah 4:7: consecrated standing and redeemed as sheaves — exempt, for at the '
                    'duty\'s hour it was exempt)', ['left_for_the_poor'] if st == 'liable' else ['exempt'])
    if q == 'for_named_poor':
        return cell(['R._Eliezer_acquired', 'sages_to_the_first_poor_found'], M, 'Peah 4:9 — ' + SK + 'Chapter 2 6: not '
                    'FOR one poor over the rest', ['left_for_the_poor'])
    if q == 'gentile_gifts_tithed':
        return cell('liable_to_tithes_unless_renounced', A, 'Peah 4:9', [FX.NONE])
    if q == 'leket':
        pos = k['position']
        if pos in ('within_hand', 'within_sickle'):
            return cell('the_poor', M, '"the gleanings of your harvest" (19:9) — ' + SK + 'Chapter 2 5 VERBATIM: from '
                        'WITHIN the hand or the sickle — the poor\'s (Peah 4:10)', ['left_for_the_poor'])
        if pos in ('behind_hand', 'behind_sickle'):
            return cell('the_owner', M, SK + 'Chapter 2 5 — from BEHIND — the owner\'s', [FX.NONE])
        if pos in ('top_of_hand', 'top_of_sickle'):
            return cell(['R._Yishmael_the_poor', 'R._Akiva_the_owner'], M, SK + 'Chapter 2 5 — the top disputed', [FX.NONE])
        if pos in ('handful', 'fistful', 'thorn', 'scorpion', 'startled'):
            return cell('the_owner', M, SK + 'Chapter 2 5 — the trigger list: not "from the reaping" (Peah 4:10)', [FX.NONE])
    if q == 'ant_holes':
        return cell({'in_the_standing_crop': 'owner', 'behind_the_reapers_upper': 'poor', 'behind_the_reapers_lower': 'owner',
                     'R._Meir': 'all_poor_doubtful_leket_is_leket'}, M, 'Peah 4:11 — ' + SK + 'Chapter 3 7: the doubt '
                    'runs to the poor', ['left_for_the_poor'])
    if q == 'doubt':
        return cell('to_the_poor', M, SK + 'Chapter 3 7 — doubt-gleaning is gleaning, doubt-forgotten forgotten, '
                    'doubt-corner corner', ['left_for_the_poor'])
    if q == 'heap':
        return cell('what_touches_the_ground_the_poor_wind_estimate', M, 'Peah 5:1 — ' + SK + 'Chapter 3 7 (wind-'
                    'scattered after separation: the poor keep gain and loss; the estimate data)', ['left_for_the_poor'])
    if q == 'ear_reaching':
        return cell('reaped_with_the_standing_owner_else_poor', A, 'Peah 5:2', [FX.NONE])
    if q == 'poor_at_the_hour':
        return cell(['sages_he_was_poor_then', 'R._Eliezer_takes_and_repays'], I, '19:10 "to the POOR" — the status at '
                    'the moment (Peah 5:4)', ['left_for_the_poor'])
    if q == 'contractor':
        return cell('barred_from_the_gifts_R._Yehuda_carve', A, 'Peah 5:5 — the reaper\'s share is not his field', [FX.NONE])
    if q == 'robs_the_poor':
        c = k['case']
        if c in ('not_letting_glean', 'one_not_another', 'assisting_one', 'basket_under_the_vine'):
            return cell('robs_the_poor', M, SK + 'Chapter 2 6 ("not FOR the poor") + Chapter 3 2 (the basket) — "move '
                        'not the boundary of the ascending" (Peah 5:6, 7:3)', ['left_for_the_poor'])
        if c == 'hire_on_condition_son_gleans':
            return cell('banned', A, 'Peah 5:6', [FX.NONE])
    if q == 'renunciation':
        return cell(['Hillel_to_the_rich_too_like_the_seventh_year', 'Shammai_to_the_poor_suffices'], M, '19:10 "leave '
                    'them to the poor and the convert" is a GIFT with named recipients; Exod 23:11\'s release is to all '
                    '[IMPORT] — Hillel keeps the two apart (Peah 6:1 = Eduyot 4:3)', ['left_for_the_poor'])
    if q == 'count':
        n, kind = k['n'], k['kind']
        v = 'gift' if n <= 2 else 'owner'
        return cell([v, 'Shammai_three_gift_four_owner'], D, 'Peah 6:5 — two grapes are peret, three not; two ears are '
                    'leket, three not (Hillel; the plural\'s minimum vs a heap); Shammai three and four', ['left_for_the_poor'] if v == 'gift' else [FX.NONE])
    if q == 'peret':
        return cell('what_falls_at_the_cutting', M, '"the fallen grapes of your vineyard" (19:10) — ' + SK + 'Chapter 3 2 '
                    'VERBATIM: only what falls BY THE CUTTING; stem-cut, tangled, scattered — the owner\'s (Peah 7:3)',
                    ['left_for_the_poor'])
    if q == 'olelet':
        sh, dr, doubt = k.get('shoulder'), k.get('drip'), k.get('doubt')
        if doubt:
            return cell('the_poor', M, SK + 'Chapter 3 3 — DOUBT, the poor\'s (Peah 7:4)', ['left_for_the_poor'])
        if not sh and not dr:
            return cell('small_cluster_the_poor', M, '"you shall not glean small clusters" (19:10) — ' + SK + 'Chapter 3 3 '
                        'VERBATIM: no shoulder and no drip', ['left_for_the_poor'])
        return cell('the_owner', M, SK + 'Chapter 3 3 — has one — the owner\'s', [FX.NONE])
    if q == 'olelet_edges':
        return cell({'knee_cluster_cut_with_the_main': 'owner', 'single_grape': ['R._Yehuda_cluster', 'sages_small_cluster']},
                    A, 'Peah 7:4', [FX.NONE])
    if q == 'thinning':
        return cell(['R._Yehuda_as_his_own', 'R._Meir_not_the_poors'], M, 'Peah 7:5 — ' + SK + 'Chapter 3 1', [FX.NONE])
    if q == 'all_small':
        return cell(['R._Akiva_the_poor', 'R._Eliezer_the_owner', 'no_claim_before_the_harvest'], M, SK + 'Chapter 3 1 '
                    'VERBATIM (Peah 7:7) — the two verses argued: Deut 24:21 "when you cut" vs 19:10 "your vineyard"',
                    ['left_for_the_poor'])
    if q == 'consecrated_before_known':
        return cell('not_the_poors_before_known_the_poors_after', A, 'Peah 7:8 — the duty\'s moment on the clusters',
                    ['left_for_the_poor'])
    if q == 'window_open_to_all':
        return cell({'gleanings': 'after_the_last_gleaners', 'peret_and_olelot': 'after_the_poor_went_and_came_back',
                     'olives': 'after_the_second_rainfall'}, D, 'Peah 8:1 — the poor\'s window closes when the poor '
                    'have left (times data)', [FX.NONE])
    if q == 'trusted':
        return cell('in_their_season_the_Levite_always', A, 'Peah 8:2 — presumption rules', [FX.NONE])
    if q == 'poor_defined':
        zuz, mortgaged, trade = k.get('zuz', 0), k.get('mortgaged', False), k.get('in_trade', False)
        if trade and zuz >= 50:
            return cell('takes_not', D, 'Peah 8:9 — fifty zuz in trade (data)', [FX.NONE])
        if zuz >= 200 and not mortgaged:
            return cell('takes_not', D, 'Peah 8:8 — TWO HUNDRED ZUZ (data): "to the POOR" (19:10) has no threshold in '
                        'the ink', [FX.NONE])
        return cell('takes', D, 'Peah 8:8 — two hundred less a dinar takes even if a thousand come at once; mortgaged '
                    'takes; not forced to sell house or tools', ['left_for_the_poor'])
    if q == 'copy_23_22':
        return cell('the_Emor_copy_omits_the_vineyard', I, 'Lev 23:22 repeats 19:9-10 with the vineyard clauses absent: '
                    'token diff %s — the grain gifts restated at the festivals, the vine gifts written once' % (c_copy,),
                    [FX.NONE])
    if q == 'implication_tithes':
        return cell('corner_implies_tithes_not_the_reverse', M, 'Mishnah Niddah 6:6 — the corner\'s five predicates '
                    'contain the tithe\'s three (food, guarded, land-grown); gathered-as-one and stored are the extra two',
                    [FX.NONE])
    raise ValueError(q)

# ---- F3: THEFT, DENIAL, THE OATH; OPPRESSION, ROBBERY, THE WAGE (19:11-13) ----
def warning(offense):
    """Sifra Kedoshim Section 2 1, 3 — THE WARNING-COMPLETION MOVE: this chapter supplies the
    missing warning for punishments written elsewhere."""
    m = {'theft': ('19:11 you shall not steal', 'Exod 22:3 double [IMPORT]'),
         'denial': ('19:11 you shall not deny', 'Lev 5:21-24 the fifth and the ram [IMPORT]'),
         'lying': ('19:11 you shall not lie', 'Lev 5:22 [IMPORT]'),
         'false_oath': ('19:12 you shall not swear by My name falsely', 'Lev 5:24 [IMPORT]')}[offense]
    return cell(m, M, SK + 'Section 2 1, 2 3 — the warning here, the punishment there: the charter as the code\'s '
                'missing-clause file (LV19A-05)', [FX.NONE])

def theft(q, **k):
    if q == 'benign':
        return cell('banned_even_to_vex_or_to_repay_double', M, SK + 'Section 2 2 — no stealing to vex, no stealing to '
                    'repay double or four-and-five', [FX.NONE])
    if q == 'steal_back_own':
        return cell('banned_lest_you_look_a_thief_ben_Bag_Bag', M, SK + 'Section 2 2', [FX.NONE])
    if q == 'fellow':
        return cell('woman_to_man_and_man_to_woman_included', M, ('19:11 "a man against his FELLOW" (fellow at %s) — '
                    + SK + 'Section 2 4') % (c_amit,), [FX.NONE])
    if q == 'escalation':
        return cell(['steal', 'deny', 'lie', 'swear_falsely', 'profane'], I, ('the five verbs of 19:11-12 in their '
                    'written order %s — ' + SK + 'Section 2 5 reads them as a causal cascade') % (c_verbs,), ['name_profaned'])
    if q == 'by_my_name':
        return cell('every_name_including_the_substitutes', M, '19:12 "by MY name" — ' + SK + 'Section 2 6 (Mishnah '
                    'Shevuot 4:13: the substitute names bind)', ['name_profaned'])
    if q == 'profanation':
        return cell('the_Name_profaned', I, '19:12 "and you profane the name of your God" — ' + SK + 'Section 2 7',
                    ['name_profaned'])

def deposit_case(q, **k):
    if q == 'oath_track':
        s = deposit(claim_kind='deposit', swore_falsely=True, object_exists=False, value=100)
        v = 'principal_fifth_and_ram' if ('fifth' in s and 'ram' in s) else s
        return cell(v, P, '19:11-12 the warnings; the punishment CALLED — cold_run_vayikra5.deposit_restitution -> %r '
                    '(Bava Kamma 9:7; Shevuot 8:3: confessed — principal, fifth, guilt offering)' % s, ['restores', 'adds_fifth', 'atoned_forgiven'])
    if q == 'no_oath':
        s = deposit(claim_kind='deposit', swore_falsely=False, value=100)
        return cell(s, P, 'denial without an oath — CALLED -> the principal alone (19:11\'s denial, no 19:12)', ['restores'])
    if q == 'fine_class':
        s = deposit(claim_kind='fine', swore_falsely=True, value=100)
        return cell(s, P, ('Shevuot 5:4-5 — the raped daughter\'s fine, the four-and-five, the slave\'s thirty, the '
                    'tooth and eye: OUTSIDE the deposit oath — CALLED -> %r; ' + SK + 'Section 2 9 bounds the clause '
                    'to the MONEY class: "whoever pays by his own admission is liable"') % s, ['exempt'])
    if q == 'money_class':
        return cell('liable', P, 'Shevuot 5:4-5 — the shame and blemish, the ox that killed an ox, the wound: money '
                    'payable on admission — the deposit oath binds', ['restores', 'adds_fifth'])
    if q == 'even_to_media':
        s = deposit(claim_kind='robbery', swore_falsely=True, object_exists=False, value=1, owner_far=True)
        return cell('carry_it_after_him_even_to_media' if 'Media' in s else s, P, 'Bava Kamma 9:5 — CALLED -> %r (Lev '
                    '5:24 "to whom it belongs" [IMPORT]); a perutah\'s worth; not to his son or agent but the court\'s'
                    % s, ['restores'])
    if q == 'fifth_on_fifth':
        s = deposit(claim_kind='deposit', swore_falsely=True, object_exists=False, value=100, swore_on_fifth=True)
        return cell('fifth_on_the_fifth_to_the_perutah_floor' if 'fifth on the fifth' in s else s, P, 'Bava Kamma 9:7 — '
                    'CALLED -> %r (Lev 5:24\'s plural "fifths")' % s, ['adds_fifth'])
    if q == 'father':
        s = deposit(claim_kind='robbery', swore_falsely=True, object_exists=False, value=100, victim='father_deceased')
        return cell('principal_to_the_heirs_fifth_and_ram_on_his_own_oath' if 'heirs' in s else s, P, 'Bava Kamma 9:9 — '
                    'CALLED -> %r' % s, ['restores', 'adds_fifth'])
    if q == 'stolen_claim':
        return cell('double_by_witnesses_principal_fifth_ram_by_confession', P, 'Bava Kamma 9:8 / Shevuot 8:3 — the '
                    'keeper who claims theft is a thief (Exod 22:8 [IMPORT]): the fine track and the oath track '
                    'exclusive', ['pays_double'])
    if q == 'market_thief':
        return cell({'denied_witnesses': 'double', 'slaughtered_or_sold': 'four_and_five', 'confessed_seeing_witnesses': 'principal_only'},
                    P, 'Shevuot 8:4 — Exod 22:3, 21:37 [IMPORT]; the confession carve', ['pays_double', 'pays_four_five'])
    if q == 'oath_form':
        return cell('adjured_and_answered_amen_is_an_oath', A, 'Shevuot 5:2 — "I adjure you" — "amen"', ['oath_imposed'])
    if q == 'oath_count':
        d = k['denials']
        return cell(d, A, 'Shevuot 5:2-3 — adjured five times and denied — liable on each (R. Shimon: he could have '
                    'confessed); one oath over five claimants — one; "not to you, not to you" — each', ['name_profaned'])
    if q == 'scope':
        return cell('men_women_near_far_fit_unfit_in_court_and_out_by_his_own_mouth', A, 'Shevuot 5:1 — the deposit '
                    'oath\'s scope; by others\' mouth — R. Meir until he denies in court, the sages once he denied',
                    ['oath_imposed'])
    if q == 'false_oath_predicate':
        ch = k['change']
        liable = ch == 'liability_to_exemption'
        return cell('liable' if liable else 'exempt', A, 'Shevuot 8:6 — THE RULE: whoever swears to lighten himself is '
                    'liable, to burden himself exempt; 19:12 "falsely" bites only where the oath would have moved money '
                    '(the keeper\'s states Exod 22:6-14 [IMPORT])', ['name_profaned'] if liable else ['exempt'])
    if q == 'judges_oath':
        return cell('claim_two_silver_admission_a_perutah_of_the_claims_kind', D, 'Shevuot 6:1 — Exod 22:8 "this is it" '
                    '[IMPORT]; the thresholds data', ['oath_imposed'])
    if q == 'swear_and_take':
        return cell(['the_hired_man', 'the_robbed', 'the_injured', 'opponent_suspect', 'the_shopkeeper_on_his_ledger'], A,
                    'Shevuot 7:1 — all Torah oaths swear and do not pay; these swear AND take', ['oath_imposed'])
    if q == 'suspect':
        return cell(['dice_player', 'usurer', 'pigeon_flyer', 'seventh_year_trader'], A, 'Shevuot 7:4 — the false '
                    'swearer\'s status flip (19:12): the opponent swears and takes; both suspect — R. Yosei returns, R. '
                    'Meir divides', ['oath_imposed'])
    raise ValueError(q)

def robbery(q, **k):
    if q == 'value_at_time':
        return cell('pays_as_at_the_time_of_the_robbery', P, '19:13 "you shall not rob" the warning; Lev 5:23 "he shall '
                    'RETURN the robbery WHICH HE ROBBED" [IMPORT] — as it was then (Bava Kamma 9:1: wood made vessels, '
                    'wool made garments; the pregnant cow)', ['restores'])
    if q == 'here_is_yours':
        ch = k['change']
        if ch == 'visible':
            return cell('pays_as_at_the_robbery', P, 'Bava Kamma 9:2 — aged, cracked, rotted, soured: a visible change '
                        'makes it his to pay for', ['restores'])
        return cell('here_is_yours_before_you', P, 'Bava Kamma 9:2 — invalidated coin, defiled terumah, leaven over '
                    'Passover, the beast used for a sin: an invisible change returns as is', ['restores'])
    if q == 'perutah_floor':
        return cell('need_not_go_after_him_below_a_perutah_of_principal', D, 'Bava Kamma 9:6 — the perutah floor (data); '
                    'the fifth a separate debt', [FX.NONE])
    if q == 'sons_fed':
        return cell('exempt_unless_with_surety', P, 'Bava Kamma 10:1 — the duty rides the robber\'s OWN act (Lev 5:23 '
                    '"which HE robbed" [IMPORT]); the consumers exempt', ['exempt'])
    if q == 'collectors':
        return cell('no_changing_money_from_their_box_no_charity_from_them', A, 'Bava Kamma 10:1 — presumption (scribal)',
                    [FX.NONE])
    if q == 'despair':
        return cell('his_once_the_owners_despaired', D, 'Bava Kamma 10:2 — THE DESPAIR PARAMETER (ye\'ush): the robbed '
                    'thing changes hands when the owner gives it up — the tradition\'s own transfer condition (the '
                    'swarm; the river; the troop)', ['restores'])
    if q == 'field_usurped':
        c = k['cause']
        return cell('here_is_yours_before_you' if c in ('district_blow', 'river') else 'must_provide_another_field', P,
                    'Bava Kamma 10:5 — the return of land (Lev 5:23 [IMPORT]) with the causation test', ['restores'])
    if q == 'desert':
        return cell('not_returned_in_the_desert_unless_stipulated', P, 'Bava Kamma 10:6 — "to whom it belongs he shall '
                    'give it" (Lev 5:24 [IMPORT]): into the owner\'s usable domain', ['restores'])
    if q == 'doubt':
        d = k['doubt_on']
        return cell('liable' if d == 'return' else 'exempt', A, 'Bava Kamma 10:7 — "I robbed you and do not know '
                    'whether I returned it" — liable; "I do not know whether I robbed you" — exempt: a certain debt '
                    'with a doubtful discharge pays', ['restores'] if d == 'return' else ['exempt'])
    if q == 'lamb_returned':
        return cell('liable_until_the_owners_know_or_counted_the_flock_whole', P, 'Bava Kamma 10:8 — the return requires '
                    'the owner\'s knowledge (Lev 5:24 [IMPORT]) unless the flock was counted', ['restores'])
    if q == 'convert':
        return cell('principal_and_fifth_to_the_priests_the_ram_to_the_altar', P, 'Bava Kamma 9:11 — Num 5:8 [IMPORT, '
                    'ROUTED to the Numbers walk]', ['restores', 'adds_fifth'])
    raise ValueError(q)

def wage(q, **k):
    if q == 'oppression_class':
        return cell('the_money_class_the_wage_withholder', M, '19:13 "oppress not... rob not" — ' + SK + 'Section 2 9: '
                    'oppression bounded to the MONEY class by "you shall not rob"; Onkelos: oppress not, coerce not',
                    ['wage_due_by_morning'])
    if q == 'hire_kinds':
        return cell(['man', 'beast', 'tools', 'land'], M, '19:13 "the WORK of a hired one" — ' + SK + 'Section 2 9: '
                    'beast hire, tool hire, land hire (Bava Metzia 9:12: man, beast, tools)', ['wage_due_by_morning'])
    if q == 'first_morning':
        return cell('the_first_morning_only', I, ('19:13 "shall not stay overnight with you UNTIL MORNING" (%s) — ' + SK +
                    'Section 2 10: the first morning; after it a standing debt, no new violation') % (c_13,), ['wage_due_by_morning'])
    if q == 'claimed':
        cl = k['claimed']
        return cell('violates' if cl else 'no_violation', M, '19:13 "WITH YOU" — ' + SK + 'Section 2 10: only by your '
                    'will — where the worker never came to claim, no violation (Bava Metzia 9:12)', ['wage_due_by_morning'] if cl else ['exempt'])
    if q == 'assigned':
        return cell('no_violation_the_employer_clear', M, SK + 'Section 2 11 — assigned to the shopkeeper or the '
                    'money-changer (Bava Metzia 9:12); the claim now lies against the shopkeeper (Shevuot 7:5)', ['exempt'])
    if q == 'clock':
        w = k['worker']
        if w == 'day':
            return cell('collects_all_night', I, '19:13 "until MORNING" — the day-worker\'s wage is due through the '
                        'night (' + SK + 'Section 2 12; Bava Metzia 9:11)', ['wage_due_by_morning'])
        if w == 'night':
            return cell('collects_all_day', P, 'Deut 24:15 "on his day give his wage, the sun shall not set on it" '
                        '[IMPORT] — the night-worker\'s wage due through the day (' + SK + 'Section 2 12)', ['wage_due_by_morning'])
        if w == 'hour':
            return cell('collects_all_night_and_all_day', A, 'Bava Metzia 9:11', ['wage_due_by_morning'])
        return cell('left_by_day_collects_all_day_left_by_night_all_night_and_day', A, 'Bava Metzia 9:11 — the week, '
                    'month, year, septennate worker', ['wage_due_by_morning'])
    if q == 'resident_alien':
        return cell('under_on_his_day_not_under_until_morning', A, 'Bava Metzia 9:12 — the resident alien: Deut 24:14 '
                    '"of your convert" [IMPORT] yes; 19:13 "your NEIGHBOR" (%s) no' % (c_rea[:1],), ['wage_due_by_morning'])
    if q == 'who_swears':
        return cell('the_hired_man_swears_and_takes_in_his_time', A, 'Shevuot 7:1 / Bava Metzia 9:12 — the wage clause '
                    'reverses the oath\'s direction; past his time not, unless witnesses saw him claim; R. Yehuda: with '
                    'a partial admission', ['oath_imposed'])
    if q == 'in_kind':
        return cell('not_heeded', A, 'Bava Metzia 10:5 — "take what you made as your wage": payment in kind against the '
                    'worker\'s will does not discharge (' + SK + 'Section 2 10\'s by-your-will)', ['wage_due_by_morning'])
    if q == 'shopkeeper_ledger':
        return cell(['both_swear_and_take', 'ben_Nannas_both_take_without_an_oath'], A, 'Shevuot 7:5 — "give my worker '
                    'a sela" — he says I gave, they say we did not take', ['oath_imposed'])
    raise ValueError(q)

# ---- F4: THE DEAF AND THE BLIND, THE COURT, THE TONGUE, THE HEART (19:14-18) ----
def conduct(q, **k):
    if q == 'curse_deaf':
        return cell('all_your_people_the_deaf_carves_the_living', M, '19:14 "curse not the DEAF" — ' + SK + 'Section 2 13: '
                    'all your people via the judge-and-prince verses (Exod 22:27 [IMPORT]); the deaf named to carve THE '
                    'LIVING — the dead excluded', [FX.NONE])
    if q == 'stumbling':
        c = k['case']
        if c in ('daughter_fitness', 'leave_at_dawn', 'leave_at_noon', 'sell_your_field'):
            return cell('the_blind_in_the_matter_banned', M, '19:14 "before the BLIND put no stumbling block" — ' + SK +
                        'Section 2 14: the one blind IN THE MATTER — the corrupt-advice census', ['given_to_the_heart'])
        if c == 'lender_at_interest':
            return cell(['interest_barred', 'the_lender_under_the_stumbling_block'], P, 'Mishnah Bava Metzia 5:11 — the '
                        'lender transgresses the interest bars (CALLED cold_run_yovel.interest -> %r) AND 19:14\'s '
                        'stumbling block (the fifth negative)' % INTEREST, ['interest_barred', 'given_to_the_heart'])
        if c == 'gentile_inn':
            return cell('suspicion_fences', A, 'Avodah Zarah 2:1 — no stabling, no seclusion: the stumbling block\'s '
                        'market-law fences', [FX.NONE])
    if q == 'heart':
        return cell('given_to_the_heart', I, ('19:14 "and you shall FEAR your God" (%s) — ' + SK + 'Section 2 14: the '
                    'matter is given to the heart; the clause\'s second firing at 19:32 (Chapter 7 14)') % (c_fear,),
                    ['given_to_the_heart'])
    if q == 'five_effects':
        return cell(['defiles_the_land', 'profanes_the_Name', 'removes_the_Presence', 'fells_by_the_sword', 'exiles'], M,
                    '19:15 "do no wrong in judgment" — ' + SK + 'Chapter 4 1: the judge\'s five names and five effects',
                    ['judgment_perverted'])
    if q == 'no_favor':
        who = k['who']
        return cell('banned', I, ('19:15 "lift not the face of the POOR, honor not the face of the GREAT" (%s) — ' + SK +
                    'Chapter 4 2-3: the maintenance and the shame rationales quoted and banned') % (c_15,), ['judgment_perverted'])
    if q == 'equal_treatment':
        return cell(['not_one_at_length_and_one_cut_short', 'not_one_standing_and_one_sitting'], M, SK + 'Chapter 4 4 — '
                    'the equal-treatment protocol (R. Yehuda: seat both)', [FX.NONE])
    if q == 'scale_of_merit':
        return cell('judge_every_person_toward_merit', M, '19:15 "in RIGHTEOUSNESS judge your fellow" — ' + SK +
                    'Chapter 4 4\'s second reading', [FX.NONE])
    if q == 'protocol':
        return cell('parties_heard_sent_out_judges_deliberate_the_senior_announces', M, SK + 'Chapter 4 6 — R. '
                    'Nechemiah\'s court protocol (Mishnah Sanhedrin 3:7: "so-and-so, you are clear")', [FX.NONE])
    if q == 'secrecy':
        return cell('the_leaving_judge_may_not_reveal_the_vote', M, '19:16 "go not TALEBEARING among your people" — ' +
                    SK + 'Chapter 4 7 (Mishnah Sanhedrin 3:7): "I acquitted, my colleagues outnumbered me" is the '
                    'talebearing', [FX.NONE])
    if q == 'judge_is_measurer':
        return cell('one_clause_at_two_seats', I, ('"do no wrong in judgment" stands at 19:15 (the court) and 19:35 (the '
                    'measures) — %s: the measurer is a judge (' + SK + 'Chapter 8 5 shares the five effects)') % (c_judge_measure,),
                    ['judgment_perverted'])
    if q == 'bribe':
        return cell('the_bribed_judges_eyes_dim', P, 'Peah 8:9 — Exod 23:8 [IMPORT]', ['judgment_perverted'])
    if q == 'talebearer':
        return cell('not_soft_to_one_and_harsh_to_the_other_not_the_peddler', M, '19:16 — ' + SK + 'Chapter 4 5; Onkelos '
                    '"eat no slander-morsels"', [FX.NONE])
    if q == 'blood':
        c = k['case']
        if c == 'knows_testimony':
            return cell('may_not_stay_silent', M, '19:16 "stand not on the blood of your neighbor" — ' + SK + 'Chapter 4 8: '
                        'the TESTIMONY duty', ['rescue_owed'])
        if c in ('drowning', 'bandits', 'wild_beast'):
            return cell('must_save_even_at_cost', M, SK + 'Chapter 4 8 — the RESCUE duty', ['rescue_owed'])
        if c in ('pursuer_to_kill', 'pursuer_after_the_male', 'pursuer_after_the_betrothed'):
            return cell('save_the_victim_at_the_pursuers_life', M, SK + 'Chapter 4 8 — THE PURSUER LIST', ['rescue_owed'])
    if q == 'hate':
        return cell('in_the_heart_only_is_the_ban', I, '19:17 "hate not your brother IN YOUR HEART" (%s)' % (c_17[:2],),
                    [FX.NONE])
    if q == 'rebuke':
        return cell('even_four_and_five_times_not_until_his_face_changes', M, '19:17 "REBUKE, you shall rebuke... and '
                    'bear no sin upon him" — ' + SK + 'Chapter 4 8: the doubled verb; the bound at the changed face '
                    '(Onkelos: receive no liability on his account)', ['rebuke_owed'])
    if q == 'revenge':
        return cell('refuse_because_he_refused', M, '19:18 "take no revenge" — ' + SK + 'Chapter 4 10: the sickle-and-'
                    'axe exchange', [FX.NONE])
    if q == 'grudge':
        return cell('lend_with_the_barb_I_am_not_like_you', M, '19:18 "bear no grudge" — ' + SK + 'Chapter 4 11: act '
                    'clean, speech keeps the ledger', [FX.NONE])
    if q == 'your_people':
        return cell('bounded_to_the_children_of_your_people', I, ('19:18 "the children of YOUR PEOPLE" (people at %s) — '
                    + SK + 'Chapter 4 12') % (c_am,), [FX.NONE])
    if q == 'great_rule':
        return cell(['R._Akiva_love_your_neighbor', 'ben_Azzai_the_book_of_the_generations_of_man'], M, ('19:18 "love your '
                    'neighbor as yourself" (love-as-yourself at %s: the neighbor and the convert) — ' + SK + 'Chapter 4 '
                    '12; Onkelos "show love to your fellow"') % (c_love,), ['love_owed'])
    if q == 'vow_opening':
        return cell(['no_revenge', 'no_grudge', 'no_hate_in_the_heart', 'love_your_neighbor', 'your_brother_shall_live'], I,
                    'Mishnah Nedarim 9:4 — R. Meir opens vows with 19:17-18\'s four clauses (tokens %s, %s) and Lev '
                    '25:36 [IMPORT]' % (c_17, c_18), ['love_owed', 'rebuke_owed'])
    if q == 'parents_equal':
        return cell('both_equal_the_father_precedes_by_the_sages_reason', M, 'Mishnah Keritot 6:9 — ' + SK + 'Section 1 '
                    '8-9 VERBATIM: the reversed orders (19:3 mother first) cancel to equality', [FX.NONE])
    raise ValueError(q)

import os as _os5, sys as _sys5, io as _io5, contextlib as _ctx5
_sys5.path.insert(0, _os5.path.dirname(_os5.path.abspath(__file__)))
# ---- THE WRAP (W5 HOLINESS, SANCTIONS, THE LAND, 2026-09-07): the daemon over the compiled holiness ledger, first half ----
import world_engine as WE
def law_holiness(event, world):
    """Lev 19:1-18 (cold_run_holiness.py — shelamim, classify, gifts, theft, deposit_case, robbery, wage, conduct): the ledger's debits, the wage clock, the leftover's third day."""
    k, src = event['kind'], event['case_source']
    E_ = lambda eff, s, cp=None, amount=None, due=None, law='', value=None: {'effect': eff, 'subject': s, 'counterparty': cp, 'amount': amount, 'due': due, 'value': value if value is not None else True, 'source_law': law, 'case_source': src}
    day = event.get('day', world.clock.year)
    if k == 'shelamim_slaughtered_for_acceptance':
        o = event['offerer']; out = []
        if event.get('wrong') == 'time' or event.get('eaten_on_day', 1) >= 3:
            p = shelamim('pigul_time')
            out.append(E_('not_accepted', o, value=p['v'], law='F1b [INK 19:7 "if it is eaten at all on the third day, it is rejected, it shall not be accepted" — CALLED cold_run_tzav.rejection_machine(piggul_time)]'))
            out.append(E_('karet_cut_off', o, cp='HEAVEN', value=shelamim('karet_building_block')['v'], law='F1b [INK 19:8 "its eater shall bear his iniquity... that soul shall be cut off" — %s]' % p['v']))
            if event.get('warned'):
                out.append(E_('lashes', o, value=shelamim('eater_lashes')['v'], law='F1b [Mishnah Makkot 3:2 — the pigul eater lashed when warned]'))
            return out
        if event.get('wrong') == 'place':
            p = shelamim('pigul_place')
            return [E_('not_accepted', o, value=p['v'], law='F1b [Sifra Kedoshim Chapter 1 4 — THE REASSIGNMENT: wrong-place disqualified without karet]')]
        a = shelamim('intent_at_slaughter'); w = shelamim('window'); lo = shelamim('leftover')
        return [E_('accepted', o, cp='HEAVEN', value=a['v'], law='F1b [INK 19:5 "to your ACCEPTANCE you shall slaughter it" — the intent at the slaughter binds]'),
                E_('eating_window', o, amount=2, value=w['v'], law='F1b [INK 19:6 "on the day of your slaughter it shall be eaten, and on the morrow" — CALLED tzav: %s]' % w['v']),
                E_('burn_remainder', 'the-leftover', cp=o, due=day + 2, value=lo['v'], law='F1b [INK 19:6 "the leftover until the third day shall be burned in fire" — the TIMER to the third day: %s]' % lo['v'])]
    if k == 'harvest_reaped':
        o = event.get('owner', event.get('reaper'))
        if event.get('item'):
            c = classify(event['item'])
            if 'left_for_the_poor' in c['fx']:
                return [E_('left_for_the_poor', 'the-poor', cp=o, value=c['v'], law='F2 [INK 19:9-10 the four gift-nouns on one leave-verb — the classifier\'s five predicates (Mishnah Peah 1:4): %s]' % c['v'])]
            return [E_('exempt', o, value=c['v'], law='F2 [Mishnah Peah 1:4 — a predicate fails: %s]' % c['why'][:80])]
        if event.get('reaped_by'):
            g = gifts('reaped_by', who=event['reaped_by'])
        elif event.get('state_at_reaping'):
            g = gifts('moment', state_at_reaping=event['state_at_reaping'])
        elif event.get('case'):
            g = gifts('owners', case=event['case'])
        else:
            g = gifts(event.get('gift', 'kinds'))
        if 'left_for_the_poor' in g['fx']:
            return [E_('left_for_the_poor', 'the-poor', cp=o, value=g['v'], law='F2 [%s]' % g['why'][:110])]
        return [E_('exempt', o, value=g['v'], law='F2 [%s]' % g['why'][:110])]
    if k == 'sworn_denial_admitted':
        d = event.get('claimant_against', event.get('defendant')); owner = event.get('owner'); val = event.get('value')
        if event.get('case') == 'oath_count':
            c = deposit_case('oath_count', denials=event.get('denials', 1))
            return [E_('name_profaned', d, cp='HEAVEN', amount=c['v'], value=c['v'], law='F3 [INK 19:12 "you shall not swear by My name falsely, and profane the name of your God" — Shevuot 5:2-3: liable on each of %d denials]' % c['v'])]
        if event.get('change'):
            c = deposit_case('false_oath_predicate', change=event['change'])
            if 'name_profaned' in c['fx']:
                return [E_('name_profaned', d, cp='HEAVEN', value=c['v'], law='F3 [Shevuot 8:6 — swore to lighten himself: %s]' % c['why'][:70])]
            return [E_('exempt', d, value=c['v'], law='F3 [Shevuot 8:6 — swore to burden himself: "falsely" bites only where the oath would have moved money]')]
        if event.get('claim_kind') == 'fine':
            c = deposit_case('fine_class')
            return [E_('exempt', d, value=c['v'], law='F3 [Shevuot 5:4-5 — the fine class outside the deposit oath — CALLED cold_run_vayikra5.deposit_restitution -> %s]' % c['v'])]
        if event.get('claim_kind') == 'stolen_claim':
            c = deposit_case('stolen_claim')
            return [E_('pays_double', d, cp=owner, amount=(val * 2 if val else None), value=c['v'], law='F3 [Bava Kamma 9:8 / Shevuot 8:3 — the keeper who claims theft is a thief (Exod 22:8): %s]' % c['v'])]
        if event.get('claim_kind') == 'market_thief':
            c = deposit_case('market_thief')
            return [E_('pays_double', d, cp=owner, value=c['v']['denied_witnesses'], law='F3 [Shevuot 8:4 — denied and witnesses came: double]'),
                    E_('pays_four_five', d, cp=owner, value=c['v']['slaughtered_or_sold'], law='F3 [Shevuot 8:4 — slaughtered or sold: four and five (Exod 21:37)]')]
        if not event.get('swore_falsely'):
            c = deposit_case('no_oath')
            return [E_('restores', d, cp=owner, amount=val, value=c['v'], law='F3 [INK 19:11 the denial without 19:12\'s oath — CALLED -> the principal alone: %s]' % c['v'])]
        t = theft('escalation'); c = deposit_case('oath_track')
        return [E_('name_profaned', d, cp='HEAVEN', value=theft('profanation')['v'], law='F3 [INK 19:11-12 the five verbs in their written order %s — the Name profaned]' % t['v']),
                E_('restores', d, cp=owner, amount=val, value=c['v'], law='F3 [INK 19:11 "you shall not deny" — CALLED cold_run_vayikra5.deposit_restitution -> %s (Bava Kamma 9:7)]' % c['v']),
                E_('adds_fifth', d, cp=owner, amount=(val // 5 if val else None), value=c['v'], law='F3 [Lev 5:24 the fifth — %s]' % deposit_case('fifth_on_fifth')['v']),
                E_('atoned_forgiven', d, cp='HEAVEN', value='the_ram', law='F3 [Lev 5:25 the guilt offering — the ram on the oath track]'),
                E_('oath_imposed', d, value=deposit_case('oath_form')['v'], law='F3 [Shevuot 5:2 — %s; the scope %s]' % (deposit_case('oath_form')['v'], deposit_case('scope')['v'][:40]))]
    if k == 'neighbor_robbed':
        r = event['robber']; v = event.get('victim')
        if event.get('doubt_on'):
            c = robbery('doubt', doubt_on=event['doubt_on'])
        elif event.get('change'):
            c = robbery('here_is_yours', change=event['change'])
        elif event.get('cause'):
            c = robbery('field_usurped', cause=event['cause'])
        else:
            c = robbery(event.get('case', 'value_at_time'))
        out = []
        if 'restores' in c['fx']:
            out.append(E_('restores', r, cp=v, value=c['v'], law='F3 [INK 19:13 "you shall not rob" — %s]' % c['why'][:100]))
        if 'adds_fifth' in c['fx']:
            out.append(E_('adds_fifth', r, cp=v, value=c['v'], law='F3 [%s]' % c['why'][:110]))
        if 'exempt' in c['fx']:
            out.append(E_('exempt', r, value=c['v'], law='F3 [%s]' % c['why'][:110]))
        return out
    if k == 'wage_withheld':
        e = event['employer']; wk = event['worker']
        if event.get('assigned'):
            c = wage('assigned')
            return [E_('exempt', e, value=c['v'], law='F3 [Sifra Kedoshim Section 2 11 — %s (Bava Metzia 9:12)]' % c['v'])]
        if 'claimed' in event and not event['claimed']:
            c = wage('claimed', claimed=False)
            return [E_('exempt', e, value=c['v'], law='F3 [INK 19:13 "WITH YOU" — only by your will: %s (Bava Metzia 9:12)]' % c['v'])]
        c = wage('clock', worker=event.get('worker_kind', 'day'))
        out = [E_('wage_due_by_morning', e, cp=wk, due=day + 1, value=c['v'], law='F3 [INK 19:13 "the work of a hired one shall not stay overnight with you until morning" — the TIMER to the first morning: %s]' % c['v'])]
        if event.get('in_kind'):
            ik = wage('in_kind')
            out.append(E_('wage_due_by_morning', e, cp=wk, value=ik['v'], law='F3 [Bava Metzia 10:5 — payment in kind against his will: %s, the wage still due]' % ik['v']))
        out.append(E_('oath_imposed', wk, value=wage('who_swears')['v'], law='F3 [Shevuot 7:1 / Bava Metzia 9:12 — %s]' % wage('who_swears')['v']))
        return out
    if k == 'judgment_rendered':
        j = event['judge']
        if event.get('measure'):
            return []                                                # the measures clause (19:35) is the second half's seat — the silence here
        if event.get('bribed'):
            c = conduct('bribe')
        elif event.get('favored'):
            c = conduct('no_favor', who=event['favored'])
        else:
            return []                                                # a righteous judgment perverts nothing — the silence
        return [E_('judgment_perverted', j, cp='HEAVEN', value=c['v'], law='F4 [INK 19:15 "you shall do no wrong in judgment" — %s; the five effects %s]' % (c['why'][:70], conduct('five_effects')['v']))]
    if k == 'neighbor_endangered':
        p = event['person']; nb = event.get('neighbor'); case = event.get('case'); out = []
        if event.get('stumbling'):
            c = conduct('stumbling', case=event['stumbling'])
            if 'interest_barred' in c['fx']:
                out.append(E_('interest_barred', p, cp=nb, value=c['v'], law='F4 [Mishnah Bava Metzia 5:11 — the lender under the stumbling block: CALLED cold_run_yovel.interest]'))
            if 'given_to_the_heart' in c['fx']:
                out.append(E_('given_to_the_heart', p, cp='HEAVEN', value=c['v'], law='F4 [INK 19:14 "before the BLIND put no stumbling block... and you shall FEAR your God" — %s]' % c['why'][:80]))
            return out
        if case in ('knows_testimony', 'drowning', 'bandits', 'wild_beast', 'pursuer_to_kill', 'pursuer_after_the_male', 'pursuer_after_the_betrothed'):
            c = conduct('blood', case=case)
            return [E_('rescue_owed', p, cp=nb, value=c['v'], law='F4 [INK 19:16 "stand not on the blood of your neighbor" — %s]' % c['why'][:90])]
        if case == 'sinned':
            c = conduct('rebuke')
            return [E_('rebuke_owed', p, cp=nb, value=c['v'], law='F4 [INK 19:17 "REBUKE, you shall rebuke your fellow" — %s]' % c['v'])]
        if case == 'hated':
            c = conduct('vow_opening')
            return [E_('love_owed', p, cp=nb, value=c['v'], law='F4 [INK 19:17-18 "hate not your brother in your heart... love your neighbor" — the vow opened on these clauses (Nedarim 9:4)]'),
                    E_('rebuke_owed', p, cp=nb, value=conduct('hate')['v'], law='F4 [INK 19:17 "in your heart" — the hate banned in the heart, the rebuke its remedy]')]
        c = conduct('great_rule')
        return [E_('love_owed', p, cp=nb, value=c['v'], law='F4 [INK 19:18 "love your neighbor as yourself" — %s]' % c['v'][0])]
    return []

def scene():
    """THE SCENE — Peah, Shevuot, Bava Kamma, Bava Metzia, Makkot and the Sifra's rows replayed on the world engine (clock unit: days): the leftover's third day and the wage's morning as TIMERS."""
    with _ctx5.redirect_stdout(_io5.StringIO()):
        w = WE.World(era='the holiness ledger, first half: Peah, Shevuot, Bava Kamma, Bava Metzia on the engine (clock unit: days)')
        w.laws = [law_holiness]
        w.advance(1)
        w.submit({'kind': 'shelamim_slaughtered_for_acceptance', 'subject': 'the-offerer', 'offerer': 'the-offerer', 'intent': 'to_eat_in_the_window', 'day': 1, 'case_source': 'Lev 19:5-6; Sifra Kedoshim Chapter 1 1 — slaughtered to acceptance: the window, the leftover to the third day'})
        w.submit({'kind': 'shelamim_slaughtered_for_acceptance', 'subject': 'the-third-day-eater', 'offerer': 'the-third-day-eater', 'eaten_on_day': 3, 'warned': True, 'day': 1, 'case_source': 'Lev 19:7-8; Mishnah Makkot 3:2 — eaten on the third day: rejected, karet on the eater, lashed when warned'})
        w.submit({'kind': 'shelamim_slaughtered_for_acceptance', 'subject': 'the-wrong-place', 'offerer': 'the-wrong-place', 'wrong': 'place', 'day': 1, 'case_source': 'Sifra Kedoshim Chapter 1 4 — THE REASSIGNMENT: wrong-place, no karet'})
        w.submit({'kind': 'harvest_reaped', 'subject': 'the-grain-owner', 'owner': 'the-grain-owner', 'reaper': 'the-grain-owner', 'land': 'field-1', 'item': {'food': True, 'guarded': True, 'land_grown': True, 'gathered_as_one': True, 'stored': True}, 'day': 1, 'case_source': 'Mishnah Peah 1:4 — grain: the five predicates hold, the corner owed'})
        w.submit({'kind': 'harvest_reaped', 'subject': 'the-vegetable-owner', 'owner': 'the-vegetable-owner', 'reaper': 'the-vegetable-owner', 'land': 'field-2', 'item': {'food': True, 'guarded': True, 'land_grown': True, 'gathered_as_one': True, 'stored': False}, 'day': 1, 'case_source': 'Mishnah Peah 1:4 — vegetables: not stored, exempt'})
        w.submit({'kind': 'harvest_reaped', 'subject': 'the-robbed-field', 'owner': 'the-robbed-field', 'reaper': 'robbers', 'land': 'field-3', 'reaped_by': 'robbers', 'day': 1, 'case_source': 'Mishnah Peah 2:7 — reaped by robbers: exempt (Sifra Kedoshim Chapter 1 6)'})
        w.submit({'kind': 'harvest_reaped', 'subject': 'the-consecrated-reaper', 'owner': 'the-consecrated-reaper', 'reaper': 'the-consecrated-reaper', 'land': 'field-4', 'state_at_reaping': 'exempt', 'day': 1, 'case_source': 'Mishnah Peah 4:7 — consecrated standing, redeemed as sheaves: exempt at the duty\'s hour'})
        w.submit({'kind': 'harvest_reaped', 'subject': 'the-divided-brothers', 'owner': 'the-divided-brothers', 'reaper': 'the-divided-brothers', 'land': 'field-5', 'case': 'brothers_divided', 'day': 1, 'case_source': 'Mishnah Peah 3:5 — brothers who divided: two corners'})
        w.submit({'kind': 'harvest_reaped', 'subject': 'the-vineyard-owner', 'owner': 'the-vineyard-owner', 'reaper': 'the-vineyard-owner', 'land': 'vineyard-1', 'gift': 'olelet', 'day': 1, 'case_source': 'Lev 19:10; Mishnah Peah 7:4 — the small cluster to the poor'})
        w.submit({'kind': 'sworn_denial_admitted', 'subject': 'the-denier', 'claimant_against': 'the-denier', 'owner': 'the-depositor', 'object_exists': False, 'value': 100, 'swore_falsely': True, 'day': 1, 'case_source': 'Lev 19:11-12; Bava Kamma 9:7; Shevuot 8:3 — denied and swore, then confessed: the principal, the fifth, the ram, the Name profaned'})
        w.submit({'kind': 'sworn_denial_admitted', 'subject': 'the-plain-denier', 'claimant_against': 'the-plain-denier', 'owner': 'the-depositor', 'object_exists': False, 'value': 100, 'swore_falsely': False, 'day': 1, 'case_source': 'Lev 19:11 — the denial without the oath: the principal alone'})
        w.submit({'kind': 'sworn_denial_admitted', 'subject': 'the-fine-denier', 'claimant_against': 'the-fine-denier', 'owner': 'the-claimant', 'object_exists': False, 'value': 100, 'swore_falsely': True, 'claim_kind': 'fine', 'day': 1, 'case_source': 'Mishnah Shevuot 5:4-5 — the fine class: outside the deposit oath'})
        w.submit({'kind': 'sworn_denial_admitted', 'subject': 'the-five-denials', 'claimant_against': 'the-five-denials', 'owner': 'the-claimant', 'object_exists': False, 'value': 100, 'swore_falsely': True, 'case': 'oath_count', 'denials': 5, 'day': 1, 'case_source': 'Mishnah Shevuot 5:2-3 — adjured five times and denied: liable on each'})
        w.submit({'kind': 'sworn_denial_admitted', 'subject': 'the-self-burdener', 'claimant_against': 'the-self-burdener', 'owner': 'the-claimant', 'object_exists': True, 'value': 100, 'swore_falsely': True, 'change': 'exemption_to_liability', 'day': 1, 'case_source': 'Mishnah Shevuot 8:6 — swore to burden himself: exempt'})
        w.submit({'kind': 'sworn_denial_admitted', 'subject': 'the-keeper-thief', 'claimant_against': 'the-keeper-thief', 'owner': 'the-depositor', 'object_exists': True, 'value': 100, 'swore_falsely': True, 'claim_kind': 'stolen_claim', 'day': 1, 'case_source': 'Mishnah Bava Kamma 9:8 / Shevuot 8:3 — the keeper who claimed theft: double by witnesses'})
        w.submit({'kind': 'sworn_denial_admitted', 'subject': 'the-market-thief', 'claimant_against': 'the-market-thief', 'owner': 'the-owner', 'object_exists': False, 'value': 100, 'swore_falsely': True, 'claim_kind': 'market_thief', 'day': 1, 'case_source': 'Mishnah Shevuot 8:4 — the thief: double, four and five'})
        w.submit({'kind': 'neighbor_robbed', 'subject': 'the-robber', 'robber': 'the-robber', 'victim': 'the-victim', 'day': 1, 'case_source': 'Lev 19:13; Mishnah Bava Kamma 9:1 — pays as at the time of the robbery'})
        w.submit({'kind': 'neighbor_robbed', 'subject': 'the-doubter', 'robber': 'the-doubter', 'victim': 'the-victim', 'doubt_on': 'return', 'day': 1, 'case_source': 'Mishnah Bava Kamma 10:7 — "I robbed you and do not know whether I returned it": liable'})
        w.submit({'kind': 'neighbor_robbed', 'subject': 'the-forgetter', 'robber': 'the-forgetter', 'victim': 'the-victim', 'doubt_on': 'robbed', 'day': 1, 'case_source': 'Mishnah Bava Kamma 10:7 — "I do not know whether I robbed you": exempt'})
        w.submit({'kind': 'neighbor_robbed', 'subject': 'the-ager', 'robber': 'the-ager', 'victim': 'the-victim', 'change': 'visible', 'day': 1, 'case_source': 'Mishnah Bava Kamma 9:2 — a visible change: pays as at the robbery'})
        w.submit({'kind': 'neighbor_robbed', 'subject': 'the-sons', 'robber': 'the-sons', 'victim': 'the-victim', 'case': 'sons_fed', 'day': 1, 'case_source': 'Mishnah Bava Kamma 10:1 — the sons who ate the robbery: exempt unless with surety'})
        w.submit({'kind': 'neighbor_robbed', 'subject': 'the-converts-robber', 'robber': 'the-converts-robber', 'victim': 'the-convert', 'case': 'convert', 'day': 1, 'case_source': 'Mishnah Bava Kamma 9:11 — the convert who died: principal and fifth to the priests'})
        w.submit({'kind': 'wage_withheld', 'subject': 'the-employer', 'employer': 'the-employer', 'worker': 'the-day-worker', 'worker_kind': 'day', 'day': 1, 'case_source': 'Lev 19:13; Mishnah Bava Metzia 9:11 — the day-worker collects all night: the morning TIMER'})
        w.submit({'kind': 'wage_withheld', 'subject': 'the-night-employer', 'employer': 'the-night-employer', 'worker': 'the-night-worker', 'worker_kind': 'night', 'day': 1, 'case_source': 'Deut 24:15 / Mishnah Bava Metzia 9:11 — the night-worker collects all day'})
        w.submit({'kind': 'wage_withheld', 'subject': 'the-assigner', 'employer': 'the-assigner', 'worker': 'the-assigned-worker', 'assigned': True, 'day': 1, 'case_source': 'Mishnah Bava Metzia 9:12 — assigned to the shopkeeper: the employer clear'})
        w.submit({'kind': 'wage_withheld', 'subject': 'the-unclaimed', 'employer': 'the-unclaimed', 'worker': 'the-absent-worker', 'claimed': False, 'day': 1, 'case_source': 'Sifra Kedoshim Section 2 10 — the worker never came to claim: no violation'})
        w.submit({'kind': 'wage_withheld', 'subject': 'the-in-kind-payer', 'employer': 'the-in-kind-payer', 'worker': 'the-paid-in-kind', 'worker_kind': 'day', 'in_kind': True, 'day': 1, 'case_source': 'Mishnah Bava Metzia 10:5 — payment in kind not heeded'})
        w.submit({'kind': 'judgment_rendered', 'subject': 'the-fair-judge', 'judge': 'the-fair-judge', 'day': 1, 'case_source': 'Lev 19:15 — a righteous judgment: the silence'})
        w.submit({'kind': 'judgment_rendered', 'subject': 'the-favoring-judge', 'judge': 'the-favoring-judge', 'favored': 'poor', 'day': 1, 'case_source': 'Lev 19:15; Sifra Kedoshim Chapter 4 2 — the poor favored: banned'})
        w.submit({'kind': 'judgment_rendered', 'subject': 'the-bribed-judge', 'judge': 'the-bribed-judge', 'bribed': True, 'day': 1, 'case_source': 'Mishnah Peah 8:9 — the bribed judge\'s eyes dim'})
        w.submit({'kind': 'judgment_rendered', 'subject': 'the-measurer', 'judge': 'the-measurer', 'measure': True, 'day': 1, 'case_source': 'Lev 19:35 — the measures clause: the second half\'s seat'})
        w.submit({'kind': 'neighbor_endangered', 'subject': 'the-adviser', 'person': 'the-adviser', 'neighbor': 'the-advised', 'stumbling': 'daughter_fitness', 'day': 1, 'case_source': 'Sifra Kedoshim Section 2 14 — the one blind in the matter: corrupt advice'})
        w.submit({'kind': 'neighbor_endangered', 'subject': 'the-lender', 'person': 'the-lender', 'neighbor': 'the-borrower', 'stumbling': 'lender_at_interest', 'day': 1, 'case_source': 'Mishnah Bava Metzia 5:11 — the lender at interest under the stumbling block'})
        w.submit({'kind': 'neighbor_endangered', 'subject': 'the-witness', 'person': 'the-witness', 'neighbor': 'the-litigant', 'case': 'knows_testimony', 'day': 1, 'case_source': 'Sifra Kedoshim Chapter 4 8 — knows testimony: may not stay silent'})
        w.submit({'kind': 'neighbor_endangered', 'subject': 'the-rescuer', 'person': 'the-rescuer', 'neighbor': 'the-drowning', 'case': 'drowning', 'day': 1, 'case_source': 'Sifra Kedoshim Chapter 4 8 — the rescue duty'})
        w.submit({'kind': 'neighbor_endangered', 'subject': 'the-rebuker', 'person': 'the-rebuker', 'neighbor': 'the-sinner', 'case': 'sinned', 'day': 1, 'case_source': 'Lev 19:17; Sifra Kedoshim Chapter 4 8 — rebuke, even four and five times'})
        w.submit({'kind': 'neighbor_endangered', 'subject': 'the-hater', 'person': 'the-hater', 'neighbor': 'the-hated', 'case': 'hated', 'day': 1, 'case_source': 'Lev 19:17-18; Mishnah Nedarim 9:4 — hate in the heart: the vow opened on these clauses'})
        w.submit({'kind': 'neighbor_endangered', 'subject': 'the-lover', 'person': 'the-lover', 'neighbor': 'the-neighbor', 'day': 1, 'case_source': 'Lev 19:18; Sifra Kedoshim Chapter 4 12 — the great rule'})
        w.advance(3)                                                 # the third day: the leftover burns; the mornings have passed
    n = lambda eid, eff: len([e for e in w.entity(eid).ledger if e['effect'] == eff])
    yr = lambda eid, eff: [e['year'] for e in w.entity(eid).ledger if e['effect'] == eff]
    am = lambda eid, eff: [e['amount'] for e in w.entity(eid).ledger if e['effect'] == eff]
    tset = len([l for l in w.log if l[0] == 'TIMER-SET']); fired = len([l for l in w.log if l[0] == 'TIMER-FIRE'])
    return (n('the-offerer', 'accepted'), n('the-offerer', 'eating_window'), yr('the-leftover', 'burn_remainder'), n('the-third-day-eater', 'not_accepted'), n('the-third-day-eater', 'karet_cut_off'), n('the-third-day-eater', 'lashes'), n('the-wrong-place', 'not_accepted'), n('the-wrong-place', 'karet_cut_off'),
            n('the-poor', 'left_for_the_poor'), n('the-vegetable-owner', 'exempt'), n('the-robbed-field', 'exempt'), n('the-consecrated-reaper', 'exempt'),
            n('the-denier', 'name_profaned'), n('the-denier', 'restores'), n('the-denier', 'adds_fifth'), n('the-denier', 'atoned_forgiven'), n('the-denier', 'oath_imposed'), n('the-plain-denier', 'restores'), n('the-plain-denier', 'name_profaned'), n('the-fine-denier', 'exempt'), am('the-five-denials', 'name_profaned'), n('the-self-burdener', 'exempt'), n('the-keeper-thief', 'pays_double'), n('the-market-thief', 'pays_double'), n('the-market-thief', 'pays_four_five'),
            n('the-robber', 'restores'), n('the-doubter', 'restores'), n('the-forgetter', 'exempt'), n('the-ager', 'restores'), n('the-sons', 'exempt'), n('the-converts-robber', 'adds_fifth'),
            yr('the-employer', 'wage_due_by_morning'), n('the-day-worker', 'oath_imposed'), yr('the-night-employer', 'wage_due_by_morning'), n('the-assigner', 'exempt'), n('the-unclaimed', 'exempt'), n('the-in-kind-payer', 'wage_due_by_morning'),
            n('the-fair-judge', 'judgment_perverted'), n('the-favoring-judge', 'judgment_perverted'), n('the-bribed-judge', 'judgment_perverted'), n('the-measurer', 'judgment_perverted'),
            n('the-adviser', 'given_to_the_heart'), n('the-lender', 'interest_barred'), n('the-lender', 'given_to_the_heart'), n('the-witness', 'rescue_owed'), n('the-rescuer', 'rescue_owed'), n('the-rebuker', 'rebuke_owed'), n('the-hater', 'love_owed'), n('the-hater', 'rebuke_owed'), n('the-lover', 'love_owed'),
            tset, fired, w.clock.year), w
SCENE, _W = scene()


# ---- (2) TEST DATA — the Mishnah rows, read whole from the shelf ------
def load(t):
    d = json.load(open('<repo-old>/Data/mishnah_%s_he.json' % t))
    return d['text'] if isinstance(d, dict) and 'text' in d else d
SHELF = {'Peah': load('peah'), 'Bava Metzia': load('bava_metzia'), 'Bava Kamma': load('bava_kamma'), 'Shevuot': load('shevuot'),
         'Eduyot': load('eduyot'), 'Avodah Zarah': load('avodah_zarah'), 'Sanhedrin': load('sanhedrin'), 'Nedarim': load('nedarim'),
         'Bikkurim': load('bikkurim'), 'Keritot': load('keritot'), 'Makkot': load('makkot'), 'Niddah': load('niddah')}
def mrow(book, ch, m, must):
    txt = strip(SHELF[book][ch - 1][m - 1])
    assert must in txt, 'answer-sheet check failed: %r not in Mishnah %s %d:%d' % (must, book, ch, m)
SHEET = [
    ('Peah', 1, 1, 'שעור'), ('Peah', 1, 2, 'מששים'), ('Peah', 1, 3, 'בסוף'), ('Peah', 1, 4, 'ונשמר'), ('Peah', 1, 5, 'האוג'),
    ('Peah', 1, 6, 'שימרח'), ('Peah', 2, 1, 'הנחל'), ('Peah', 2, 2, 'במעדר'), ('Peah', 2, 3, 'כותש'), ('Peah', 2, 4, 'הרואין'),
    ('Peah', 2, 5, 'גרנות'), ('Peah', 2, 7, 'לסטים'), ('Peah', 2, 8, 'הלוקח'), ('Peah', 3, 1, 'מלבנות'), ('Peah', 3, 2, 'המנמר'),
    ('Peah', 3, 3, 'בצלים'), ('Peah', 3, 4, 'האמהות'), ('Peah', 3, 5, 'האחין'), ('Peah', 3, 6, 'רבע'), ('Peah', 4, 1, 'לבוז'),
    ('Peah', 4, 2, 'בדלית'), ('Peah', 4, 3, 'טליתו'), ('Peah', 4, 4, 'במגלות'), ('Peah', 4, 5, 'אבעיות'), ('Peah', 4, 6, 'נתגיר'),
    ('Peah', 4, 7, 'ופדה'), ('Peah', 4, 9, 'שנמצא'), ('Peah', 4, 10, 'המגל'), ('Peah', 4, 11, 'הנמלים'), ('Peah', 5, 1, 'גדיש'),
    ('Peah', 5, 2, 'שבלת'), ('Peah', 5, 4, 'שעה'), ('Peah', 5, 5, 'באריסות'), ('Peah', 5, 6, 'גבול'), ('Peah', 6, 1, 'כשמטה'),
    ('Peah', 6, 5, 'גרגרים'), ('Peah', 7, 3, 'פרט'), ('Peah', 7, 4, 'כתף'), ('Peah', 7, 5, 'המדל'), ('Peah', 7, 7, 'עוללות'),
    ('Peah', 7, 8, 'המקדיש'), ('Peah', 8, 1, 'הנמושות'), ('Peah', 8, 2, 'נאמנים'), ('Peah', 8, 8, 'מאתים'), ('Peah', 8, 9, 'חמשים'),
    ('Bava Metzia', 9, 11, 'שעות'), ('Bava Metzia', 9, 12, 'שתבעו'), ('Bava Metzia', 10, 5, 'בשכרך'), ('Bava Metzia', 5, 11, 'עור'),
    ('Bava Kamma', 9, 1, 'הגזלה'), ('Bava Kamma', 9, 2, 'לפניך'), ('Bava Kamma', 9, 5, 'למדי'), ('Bava Kamma', 9, 6, 'פרוטה'),
    ('Bava Kamma', 9, 7, 'חמש'), ('Bava Kamma', 9, 8, 'כפל'), ('Bava Kamma', 9, 9, 'אביו'), ('Bava Kamma', 9, 11, 'הגר'),
    ('Bava Kamma', 10, 1, 'בניו'), ('Bava Kamma', 10, 2, 'מתיאשין'), ('Bava Kamma', 10, 5, 'מסיקין'), ('Bava Kamma', 10, 6, 'במדבר'),
    ('Bava Kamma', 10, 7, 'יודע'), ('Bava Kamma', 10, 8, 'טלה'),
    ('Shevuot', 5, 1, 'הפקדון'), ('Shevuot', 5, 2, 'אמן'), ('Shevuot', 5, 3, 'חמשה'), ('Shevuot', 5, 4, 'קנס'), ('Shevuot', 5, 5, 'שורי'),
    ('Shevuot', 6, 1, 'פרוטה'), ('Shevuot', 7, 1, 'השכיר'), ('Shevuot', 7, 4, 'בקביא'), ('Shevuot', 7, 5, 'פנקסו'), ('Shevuot', 8, 3, 'כפל'),
    ('Shevuot', 8, 4, 'טבח'), ('Shevuot', 8, 6, 'להקל'), ('Shevuot', 4, 13, 'הכנויין'),
    ('Eduyot', 4, 3, 'כשמטה'), ('Avodah Zarah', 2, 1, 'בפנדקאות'), ('Sanhedrin', 3, 7, 'רכיל'), ('Nedarim', 9, 4, 'תקם'),
    ('Bikkurim', 4, 2, 'כאנשים'), ('Keritot', 6, 9, 'שקולים'), ('Makkot', 3, 2, 'ופגול'), ('Niddah', 6, 6, 'בפאה'),
]
for b, ch, m, must in SHEET:
    mrow(b, ch, m, must)
print('answer sheet: %d Mishnah rows verified by their own tokens (Peah whole, Bava Metzia 9, Bava Kamma 9-10, Shevuot 5-8 '
      'read whole — the topic docket)' % len(SHEET))

TESTS = [
 ('THE SCENE — Peah, Shevuot, Bava Kamma, Bava Metzia and Makkot on the world engine (the leftover\'s third day and the wage\'s morning as TIMERS; the daemon\'s watch coverage printed below)', cell(SCENE, I, 'the peace offering\'s window and rejection, the poor gifts by the classifier and the gifts engine, the deposit oath\'s tracks, the robbery\'s returns, the wage clock, the court, the neighbor — every value a cell\'s', ['accepted', 'eating_window', 'burn_remainder', 'not_accepted', 'karet_cut_off', 'lashes', 'left_for_the_poor', 'exempt', 'name_profaned', 'restores', 'adds_fifth', 'atoned_forgiven', 'oath_imposed', 'pays_double', 'pays_four_five', 'wage_due_by_morning', 'judgment_perverted', 'given_to_the_heart', 'interest_barred', 'rescue_owed', 'rebuke_owed', 'love_owed']), (1, 1, [3], 1, 1, 1, 1, 0, 3, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, [5], 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, [2], 1, [2], 1, 1, 2, 0, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 4, 4, 3)),
 # ---- THE CHARGE, THE PARENTS, THE IDOLS ----
 ('Lev 19:2 — said in full assembly', frame('assembly'), 'said_in_full_assembly'),
 ('Sifra Kedoshim 1 1 — holy = separate', frame('holy'), 'separate'),
 ('Keritot 6:9 — mother first here, father first at Sinai: both equal', frame('parents_order'), 'mother_first_here_father_first_at_Sinai_both_equal'),
 ('Sifra Kedoshim 1 2-3 — the woman included', frame('woman_included'), 'woman_bound_to_fear_when_able'),
 ('Sifra Kedoshim 1 10 — fear defined', frame('fear_defined'), ['not_sit_in_his_place', 'not_speak_in_his_place', 'not_contradict_him']),
 ('Sifra Kedoshim 1 10 — honor defined', frame('honor_defined'), ['feed', 'give_drink', 'clothe', 'cover', 'bring_in', 'take_out']),
 ('Lev 19:3 — the override clause', frame('override'), 'parent_ordering_a_transgression_not_obeyed'),
 ('Sifra Kedoshim 1 7 — three partners', frame('three_partners'), ['God', 'father', 'mother']),
 ('Lev 19:4 — not even to look', frame('idols_look'), 'not_even_to_look_R._Yehuda'),
 ('Sifra Kedoshim 1 12 — the molten warnings', frame('molten_warnings'), ['two_warnings', 'R._Yosei_three']),
 ('the "I am the LORD" signature at eight seats', frame('ani_YHWH'), [2, 3, 4, 10, 12, 14, 16, 18]),
 ('Bikkurim 4:2 — the persons census', frame('persons_all'), 'androgynous_liable_to_all_commandments_as_men'),
 ('Keritot 6:9 — parents equal, the father precedes by reason', conduct('parents_equal'), 'both_equal_the_father_precedes_by_the_sages_reason'),
 # ---- THE SHELAMIM'S WINDOW (the Tzav engine CALLED) ----
 ('Lev 19:5 — intent at slaughter', shelamim('intent_at_slaughter'), 'slaughter_on_condition_of_two_day_eating'),
 ('Sifra Kedoshim 1 3 — not two heads', shelamim('not_two_heads'), 'one_at_a_time'),
 ('Lev 19:6 — the two-day window (CALLED)', shelamim('window'), 'two days and one night'),
 ('Lev 19:6 — the leftover burned (CALLED)', shelamim('leftover'), 'burned on the third day, by day'),
 ('Lev 19:7-8 — pigul with karet on the eater (CALLED)', shelamim('pigul_time'), 'rejected with karet on the eater'),
 ('Sifra Kedoshim 1 4 — the reassigned clause: wrong-place without karet (CALLED)', shelamim('pigul_place'), 'disqualified without karet'),
 ('Sifra Kedoshim 1 5 — the karet building block', shelamim('karet_building_block'), 'whoever_eats_the_holy_in_violation_earns_karet'),
 ('Makkot 3:2 — the pigul eater lashed', shelamim('eater_lashes'), 'lashed_when_warned'),
 # ---- THE POOR-GIFTS ENGINE ----
 ('Lev 19:9-10 — the four gifts of the ink', gifts('kinds'), ['corner', 'fallen_grapes', 'gleanings', 'small_clusters']),
 ('Lev 19:10 — the recipients', gifts('recipients'), 'the_poor_and_the_convert_not_the_resident_alien'),
 ('Peah 1:1 — the corner has no measure', gifts('measure'), 'no_measure_in_the_ink'),
 ('Peah 1:2 — the sixtieth floor', gifts('floor'), 'one_sixtieth_by_field_poor_and_humility'),
 ('Peah 1:3 — the corner\'s position', gifts('position'), 'attaches_at_the_finish_start_or_middle_counts_if_the_end_holds_the_measure'),
 ('Sifra Kedoshim 1 10 — the four reasons', gifts('four_reasons'), ['robbery_of_the_poor', 'idling_of_the_poor', 'appearances', 'the_Torah_said_so']),
 ('Peah 1:4 — grain: owes (five predicates)', classify({'food': True, 'guarded': True, 'land_grown': True, 'gathered_as_one': True, 'stored': True}), 'owes_corner'),
 ('Peah 1:4 — vegetables: exempt (not stored)', classify({'food': True, 'guarded': True, 'land_grown': True, 'gathered_as_one': True, 'stored': False}), 'exempt'),
 ('Peah 1:4 — figs: exempt (not gathered as one)', classify({'food': True, 'guarded': True, 'land_grown': True, 'gathered_as_one': False, 'stored': True}), 'exempt'),
 ('Peah 1:4 — the ownerless: exempt (not guarded)', classify({'food': True, 'guarded': False, 'land_grown': True, 'gathered_as_one': True, 'stored': True}), 'exempt'),
 ('Peah 1:5 — the tree census', gifts('trees'), ['sumac', 'carobs', 'nuts', 'almonds', 'vines', 'pomegranates', 'olives', 'dates']),
 ('Peah 1:6 — until the smoothing', gifts('window_end'), 'until_the_smoothing'),
 ('Peah 2:1 — the stream divides', gifts('divides', feature='stream'), 'divides'),
 ('Peah 2:1 — another seed divides', gifts('divides', feature='another_seed'), 'divides'),
 ('Peah 2:1 — the fodder-cut: disputed', gifts('divides', feature='fodder_cut'), ['divides_R._Meir', 'only_if_plowed_sages']),
 ('Peah 2:2 — the channel not reapable as one', gifts('divides', feature='water_channel_not_reapable_as_one'), 'divides_R._Yehuda'),
 ('Peah 2:2 — the terraced hills: one corner', gifts('divides', feature='terraced_hills'), 'one_corner_for_all'),
 ('Peah 2:3 — trees: only a fence', gifts('divides', feature='fence_for_trees'), 'divides_trees_only_a_fence'),
 ('Peah 2:3 — the meshing canopy', gifts('divides', feature='meshing_canopy'), 'does_not_divide_one_corner'),
 ('Peah 2:4 — carobs by line of sight', gifts('divides', feature='carobs'), 'all_that_see_one_another_one_corner'),
 ('Peah 2:5 — one kind, two floors: one corner', gifts('identity', kinds=1, floors=2), 1),
 ('Peah 2:5 — two kinds, one floor: two corners', gifts('identity', kinds=2, floors=1), 2),
 ('Peah 2:5 — two kinds of wheat, two floors: two', gifts('identity', kinds=1, floors=2, same_species_varieties=True), 2),
 ('Peah 2:7 — reaped by robbers: exempt', gifts('reaped_by', who='robbers'), 'exempt'),
 ('Peah 2:7 — nibbled by ants: exempt', gifts('reaped_by', who='ants'), 'exempt'),
 ('Peah 2:7 — half and half after: exempt (the standing crop)', gifts('reaped_by', who='half_robbers_half_he_after'), 'exempt_duty_on_the_standing_crop'),
 ('Peah 2:8 — robbers half then he half', gifts('reaped_by', who='robbers_half_then_he_half'), 'corner_from_what_he_reaped'),
 ('Peah 2:8 — sold half', gifts('reaped_by', who='sold_half'), 'the_buyer_gives_for_all'),
 ('Peah 2:8 — consecrated half', gifts('reaped_by', who='consecrated_half'), 'the_redeemer_gives_for_all'),
 ('Peah 4:6 — the gentile who then converted', gifts('reaped_by', who='gentile_then_converted'), ['exempt_from_leket_shikchah_peah', 'R._Yehuda_liable_in_shikchah']),
 ('Peah 3:1 — grain between olives', gifts('patches', case='grain_between_olives'), ['Shammai_each', 'Hillel_one_for_all', 'both_one_if_row_heads_mixed']),
 ('Peah 3:2 — the patchy harvest', gifts('patches', case='patchy_harvest_moist_stalks'), ['R._Akiva_each', 'sages_one_for_all', 'both_each_for_dill_or_mustard_in_three']),
 ('Peah 3:3 — onions for market and floor', gifts('patches', case='onions_market_and_floor'), 'separate_corners'),
 ('Peah 3:4 — onion mothers', gifts('patches', case='onion_mothers'), ['liable', 'R._Yosei_exempt']),
 ('Peah 3:5 — brothers who divided: two', gifts('owners', case='brothers_divided'), 2),
 ('Peah 3:5 — rejoined: one', gifts('owners', case='brothers_rejoined'), 1),
 ('Peah 3:5 — two bought a tree: one', gifts('owners', case='two_bought_a_tree'), 1),
 ('Peah 3:5 — north and south: each', gifts('owners', case='north_and_south'), 'each_his_own'),
 ('Peah 3:5 — tree stalks sold', gifts('owners', case='tree_stalks_sold'), 'each_unless_the_owner_kept_some_R._Yehuda'),
 ('Peah 3:6 — the field\'s minimum (five arms, the law as R. Yehuda b. Beteira)', gifts('field_minimum'),
  {'R._Eliezer': 'quarter_kav_ground', 'R._Yehoshua': 'yields_two_seahs', 'R._Tarfon': 'six_by_six', 'R._Yehuda_b._Beteira': 'enough_to_reap_and_repeat_THE_LAW', 'R._Akiva': 'any_ground'}),
 ('Peah 4:1 — given attached, the poor scramble', gifts('attached'), 'given_attached_to_the_ground_the_poor_scramble'),
 ('Peah 4:1-2 — the trellis and the palm', gifts('trellis'), 'the_owner_brings_down_and_divides_even_ninety_nine_against_one'),
 ('Peah 4:3 — seizing is not taking', gifts('seizing'), 'threw_on_the_rest_nothing_fell_or_cloak_removed'),
 ('Peah 4:4 — no sickles', gifts('no_sickles'), 'no_sickles_or_axes_that_they_not_strike_each_other'),
 ('Peah 4:5 — three distributions', gifts('three_times'), ['morning', 'noon', 'afternoon']),
 ('Peah 4:7 — consecrated standing, redeemed standing: liable', gifts('moment', state_at_reaping='liable'), 'liable'),
 ('Peah 4:7 — standing, redeemed as sheaves: exempt', gifts('moment', state_at_reaping='exempt'), 'exempt'),
 ('Peah 4:9 — for a named poor man', gifts('for_named_poor'), ['R._Eliezer_acquired', 'sages_to_the_first_poor_found']),
 ('Peah 4:9 — the gentile\'s gifts tithed', gifts('gentile_gifts_tithed'), 'liable_to_tithes_unless_renounced'),
 ('Peah 4:10 — within the hand: the poor', gifts('leket', position='within_hand'), 'the_poor'),
 ('Peah 4:10 — within the sickle: the poor', gifts('leket', position='within_sickle'), 'the_poor'),
 ('Peah 4:10 — behind the hand: the owner', gifts('leket', position='behind_hand'), 'the_owner'),
 ('Peah 4:10 — the top: disputed', gifts('leket', position='top_of_sickle'), ['R._Yishmael_the_poor', 'R._Akiva_the_owner']),
 ('Peah 4:10 — struck by a thorn: the owner', gifts('leket', position='thorn'), 'the_owner'),
 ('Peah 4:10 — a handful reaped: the owner', gifts('leket', position='handful'), 'the_owner'),
 ('Peah 4:11 — the ant holes', gifts('ant_holes'), {'in_the_standing_crop': 'owner', 'behind_the_reapers_upper': 'poor', 'behind_the_reapers_lower': 'owner', 'R._Meir': 'all_poor_doubtful_leket_is_leket'}),
 ('Sifra Kedoshim 3 7 — the doubt to the poor', gifts('doubt'), 'to_the_poor'),
 ('Peah 5:1 — the heap and the wind', gifts('heap'), 'what_touches_the_ground_the_poor_wind_estimate'),
 ('Peah 5:2 — the ear reaching the standing crop', gifts('ear_reaching'), 'reaped_with_the_standing_owner_else_poor'),
 ('Peah 5:4 — poor at the hour', gifts('poor_at_the_hour'), ['sages_he_was_poor_then', 'R._Eliezer_takes_and_repays']),
 ('Peah 5:5 — the contractor barred', gifts('contractor'), 'barred_from_the_gifts_R._Yehuda_carve'),
 ('Peah 5:6 — not letting glean: robs the poor', gifts('robs_the_poor', case='not_letting_glean'), 'robs_the_poor'),
 ('Peah 5:6 — assisting one: robs the poor', gifts('robs_the_poor', case='assisting_one'), 'robs_the_poor'),
 ('Peah 7:3 — the basket under the vine: robs the poor', gifts('robs_the_poor', case='basket_under_the_vine'), 'robs_the_poor'),
 ('Peah 5:6 — hiring on condition the son gleans', gifts('robs_the_poor', case='hire_on_condition_son_gleans'), 'banned'),
 ('Peah 6:1 — renunciation to the poor alone', gifts('renunciation'), ['Hillel_to_the_rich_too_like_the_seventh_year', 'Shammai_to_the_poor_suffices']),
 ('Peah 6:5 — two ears are leket', gifts('count', n=2, kind='ears'), ['gift', 'Shammai_three_gift_four_owner']),
 ('Peah 6:5 — three grapes are not peret', gifts('count', n=3, kind='grapes'), ['owner', 'Shammai_three_gift_four_owner']),
 ('Peah 7:3 — peret defined', gifts('peret'), 'what_falls_at_the_cutting'),
 ('Peah 7:4 — no shoulder, no drip: the poor', gifts('olelet', shoulder=False, drip=False), 'small_cluster_the_poor'),
 ('Peah 7:4 — has a shoulder: the owner', gifts('olelet', shoulder=True, drip=False), 'the_owner'),
 ('Peah 7:4 — doubt: the poor', gifts('olelet', doubt=True), 'the_poor'),
 ('Peah 7:4 — the knee cluster and the single grape', gifts('olelet_edges'), {'knee_cluster_cut_with_the_main': 'owner', 'single_grape': ['R._Yehuda_cluster', 'sages_small_cluster']}),
 ('Peah 7:5 — thinning', gifts('thinning'), ['R._Yehuda_as_his_own', 'R._Meir_not_the_poors']),
 ('Peah 7:7 — the all-small-clusters vineyard', gifts('all_small'), ['R._Akiva_the_poor', 'R._Eliezer_the_owner', 'no_claim_before_the_harvest']),
 ('Peah 7:8 — consecrated before the clusters were known', gifts('consecrated_before_known'), 'not_the_poors_before_known_the_poors_after'),
 ('Peah 8:1 — when all may take', gifts('window_open_to_all'), {'gleanings': 'after_the_last_gleaners', 'peret_and_olelot': 'after_the_poor_went_and_came_back', 'olives': 'after_the_second_rainfall'}),
 ('Peah 8:2 — trusted in their season', gifts('trusted'), 'in_their_season_the_Levite_always'),
 ('Peah 8:8 — two hundred zuz: takes not', gifts('poor_defined', zuz=200), 'takes_not'),
 ('Peah 8:8 — two hundred less a dinar: takes', gifts('poor_defined', zuz=199), 'takes'),
 ('Peah 8:8 — mortgaged: takes', gifts('poor_defined', zuz=200, mortgaged=True), 'takes'),
 ('Peah 8:9 — fifty in trade: takes not', gifts('poor_defined', zuz=50, in_trade=True), 'takes_not'),
 ('Lev 23:22 — the Emor copy omits the vineyard', gifts('copy_23_22'), 'the_Emor_copy_omits_the_vineyard'),
 ('Niddah 6:6 — the corner implies the tithes', gifts('implication_tithes'), 'corner_implies_tithes_not_the_reverse'),
 # ---- THEFT, DENIAL, THE OATH ----
 ('Sifra Kedoshim 2 1 — the warning for theft (the double)', warning('theft'), ('19:11 you shall not steal', 'Exod 22:3 double [IMPORT]')),
 ('Sifra Kedoshim 2 3 — the warning for denial', warning('denial'), ('19:11 you shall not deny', 'Lev 5:21-24 the fifth and the ram [IMPORT]')),
 ('Sifra Kedoshim 2 3 — the warning for the false oath', warning('false_oath'), ('19:12 you shall not swear by My name falsely', 'Lev 5:24 [IMPORT]')),
 ('Sifra Kedoshim 2 2 — benign theft banned', theft('benign'), 'banned_even_to_vex_or_to_repay_double'),
 ('Sifra Kedoshim 2 2 — stealing back one\'s own', theft('steal_back_own'), 'banned_lest_you_look_a_thief_ben_Bag_Bag'),
 ('Sifra Kedoshim 2 4 — his fellow of any kind', theft('fellow'), 'woman_to_man_and_man_to_woman_included'),
 ('Sifra Kedoshim 2 5 — the escalation chain in the ink\'s order', theft('escalation'), ['steal', 'deny', 'lie', 'swear_falsely', 'profane']),
 ('Shevuot 4:13 — by every name', theft('by_my_name'), 'every_name_including_the_substitutes'),
 ('Lev 19:12 — the Name profaned', theft('profanation'), 'the_Name_profaned'),
 ('Bava Kamma 9:7 / Shevuot 8:3 — confessed: principal, fifth, ram (CALLED)', deposit_case('oath_track'), 'principal_fifth_and_ram'),
 ('Lev 19:11 — denial without an oath: the principal alone (CALLED)', deposit_case('no_oath'), 'principal only'),
 ('Shevuot 5:4 — the fine class outside (CALLED)', deposit_case('fine_class'), 'exempt'),
 ('Shevuot 5:5 — the money class inside', deposit_case('money_class'), 'liable'),
 ('Bava Kamma 9:5 — even to Media (CALLED)', deposit_case('even_to_media'), 'carry_it_after_him_even_to_media'),
 ('Bava Kamma 9:7 — the fifth on the fifth (CALLED)', deposit_case('fifth_on_fifth'), 'fifth_on_the_fifth_to_the_perutah_floor'),
 ('Bava Kamma 9:9 — the father (CALLED)', deposit_case('father'), 'principal_to_the_heirs_fifth_and_ram_on_his_own_oath'),
 ('Bava Kamma 9:8 — the stolen claim', deposit_case('stolen_claim'), 'double_by_witnesses_principal_fifth_ram_by_confession'),
 ('Shevuot 8:4 — the market thief', deposit_case('market_thief'), {'denied_witnesses': 'double', 'slaughtered_or_sold': 'four_and_five', 'confessed_seeing_witnesses': 'principal_only'}),
 ('Shevuot 5:2 — the oath\'s form', deposit_case('oath_form'), 'adjured_and_answered_amen_is_an_oath'),
 ('Shevuot 5:2 — adjured five times: five', deposit_case('oath_count', denials=5), 5),
 ('Shevuot 5:3 — one oath over five claimants: one', deposit_case('oath_count', denials=1), 1),
 ('Shevuot 5:1 — the deposit oath\'s scope', deposit_case('scope'), 'men_women_near_far_fit_unfit_in_court_and_out_by_his_own_mouth'),
 ('Shevuot 8:6 — liability to exemption: liable', deposit_case('false_oath_predicate', change='liability_to_exemption'), 'liable'),
 ('Shevuot 8:6 — exemption to exemption: exempt', deposit_case('false_oath_predicate', change='exemption_to_exemption'), 'exempt'),
 ('Shevuot 8:6 — exemption to liability: exempt', deposit_case('false_oath_predicate', change='exemption_to_liability'), 'exempt'),
 ('Shevuot 6:1 — the judges\' oath thresholds', deposit_case('judges_oath'), 'claim_two_silver_admission_a_perutah_of_the_claims_kind'),
 ('Shevuot 7:1 — those who swear and take', deposit_case('swear_and_take'), ['the_hired_man', 'the_robbed', 'the_injured', 'opponent_suspect', 'the_shopkeeper_on_his_ledger']),
 ('Shevuot 7:4 — the suspect', deposit_case('suspect'), ['dice_player', 'usurer', 'pigeon_flyer', 'seventh_year_trader']),
 # ---- ROBBERY ----
 ('Bava Kamma 9:1 — as at the time of the robbery', robbery('value_at_time'), 'pays_as_at_the_time_of_the_robbery'),
 ('Bava Kamma 9:2 — a visible change', robbery('here_is_yours', change='visible'), 'pays_as_at_the_robbery'),
 ('Bava Kamma 9:2 — an invisible change: here is yours', robbery('here_is_yours', change='invisible'), 'here_is_yours_before_you'),
 ('Bava Kamma 9:6 — the perutah floor', robbery('perutah_floor'), 'need_not_go_after_him_below_a_perutah_of_principal'),
 ('Bava Kamma 10:1 — the sons fed', robbery('sons_fed'), 'exempt_unless_with_surety'),
 ('Bava Kamma 10:1 — the collectors', robbery('collectors'), 'no_changing_money_from_their_box_no_charity_from_them'),
 ('Bava Kamma 10:2 — despair', robbery('despair'), 'his_once_the_owners_despaired'),
 ('Bava Kamma 10:5 — a district blow', robbery('field_usurped', cause='district_blow'), 'here_is_yours_before_you'),
 ('Bava Kamma 10:5 — through the robber', robbery('field_usurped', cause='robber'), 'must_provide_another_field'),
 ('Bava Kamma 10:6 — the desert', robbery('desert'), 'not_returned_in_the_desert_unless_stipulated'),
 ('Bava Kamma 10:7 — doubt on the return: liable', robbery('doubt', doubt_on='return'), 'liable'),
 ('Bava Kamma 10:7 — doubt on the robbery: exempt', robbery('doubt', doubt_on='robbery'), 'exempt'),
 ('Bava Kamma 10:8 — the lamb returned', robbery('lamb_returned'), 'liable_until_the_owners_know_or_counted_the_flock_whole'),
 ('Bava Kamma 9:11 — the convert (Numbers 5, routed)', robbery('convert'), 'principal_and_fifth_to_the_priests_the_ram_to_the_altar'),
 # ---- THE WAGE CLOCK ----
 ('Sifra Kedoshim 2 9 — oppression = the money class', wage('oppression_class'), 'the_money_class_the_wage_withholder'),
 ('Bava Metzia 9:12 — the hire kinds', wage('hire_kinds'), ['man', 'beast', 'tools', 'land']),
 ('Lev 19:13 — the first morning', wage('first_morning'), 'the_first_morning_only'),
 ('Bava Metzia 9:12 — claimed: violates', wage('claimed', claimed=True), 'violates'),
 ('Bava Metzia 9:12 — not claimed: no violation', wage('claimed', claimed=False), 'no_violation'),
 ('Bava Metzia 9:12 — assigned to the shopkeeper', wage('assigned'), 'no_violation_the_employer_clear'),
 ('Bava Metzia 9:11 — the day-worker collects all night', wage('clock', worker='day'), 'collects_all_night'),
 ('Bava Metzia 9:11 — the night-worker collects all day', wage('clock', worker='night'), 'collects_all_day'),
 ('Bava Metzia 9:11 — the hour-worker', wage('clock', worker='hour'), 'collects_all_night_and_all_day'),
 ('Bava Metzia 9:11 — the term worker', wage('clock', worker='term'), 'left_by_day_collects_all_day_left_by_night_all_night_and_day'),
 ('Bava Metzia 9:12 — the resident alien', wage('resident_alien'), 'under_on_his_day_not_under_until_morning'),
 ('Shevuot 7:1 — the hired man swears and takes', wage('who_swears'), 'the_hired_man_swears_and_takes_in_his_time'),
 ('Bava Metzia 10:5 — the wage in kind', wage('in_kind'), 'not_heeded'),
 ('Shevuot 7:5 — the shopkeeper on his ledger', wage('shopkeeper_ledger'), ['both_swear_and_take', 'ben_Nannas_both_take_without_an_oath']),
 # ---- THE DEAF AND THE BLIND, THE COURT, THE TONGUE, THE HEART ----
 ('Sifra Kedoshim 2 13 — curse not the deaf: the living', conduct('curse_deaf'), 'all_your_people_the_deaf_carves_the_living'),
 ('Sifra Kedoshim 2 14 — the corrupt advice', conduct('stumbling', case='sell_your_field'), 'the_blind_in_the_matter_banned'),
 ('Bava Metzia 5:11 — the lender under the stumbling block (CALLED)', conduct('stumbling', case='lender_at_interest'), ['interest_barred', 'the_lender_under_the_stumbling_block']),
 ('Avodah Zarah 2:1 — the suspicion fences', conduct('stumbling', case='gentile_inn'), 'suspicion_fences'),
 ('Lev 19:14 — given to the heart', conduct('heart'), 'given_to_the_heart'),
 ('Sifra Kedoshim 4 1 — the judge\'s five effects', conduct('five_effects'), ['defiles_the_land', 'profanes_the_Name', 'removes_the_Presence', 'fells_by_the_sword', 'exiles']),
 ('Lev 19:15 — no favor to the poor', conduct('no_favor', who='poor'), 'banned'),
 ('Lev 19:15 — no honor to the great', conduct('no_favor', who='great'), 'banned'),
 ('Sifra Kedoshim 4 4 — equal treatment', conduct('equal_treatment'), ['not_one_at_length_and_one_cut_short', 'not_one_standing_and_one_sitting']),
 ('Sifra Kedoshim 4 4 — the scale of merit', conduct('scale_of_merit'), 'judge_every_person_toward_merit'),
 ('Sanhedrin 3:7 — the court protocol', conduct('protocol'), 'parties_heard_sent_out_judges_deliberate_the_senior_announces'),
 ('Sanhedrin 3:7 — the judge\'s secrecy', conduct('secrecy'), 'the_leaving_judge_may_not_reveal_the_vote'),
 ('Lev 19:15 = 19:35 — the judge is the measurer', conduct('judge_is_measurer'), 'one_clause_at_two_seats'),
 ('Peah 8:9 — the bribed judge', conduct('bribe'), 'the_bribed_judges_eyes_dim'),
 ('Sifra Kedoshim 4 5 — the talebearer', conduct('talebearer'), 'not_soft_to_one_and_harsh_to_the_other_not_the_peddler'),
 ('Sifra Kedoshim 4 8 — the testimony duty', conduct('blood', case='knows_testimony'), 'may_not_stay_silent'),
 ('Sifra Kedoshim 4 8 — the drowning', conduct('blood', case='drowning'), 'must_save_even_at_cost'),
 ('Sifra Kedoshim 4 8 — the pursuer', conduct('blood', case='pursuer_to_kill'), 'save_the_victim_at_the_pursuers_life'),
 ('Lev 19:17 — hate in the heart', conduct('hate'), 'in_the_heart_only_is_the_ban'),
 ('Sifra Kedoshim 4 8 — the rebuke', conduct('rebuke'), 'even_four_and_five_times_not_until_his_face_changes'),
 ('Sifra Kedoshim 4 10 — revenge', conduct('revenge'), 'refuse_because_he_refused'),
 ('Sifra Kedoshim 4 11 — the grudge', conduct('grudge'), 'lend_with_the_barb_I_am_not_like_you'),
 ('Lev 19:18 — your people', conduct('your_people'), 'bounded_to_the_children_of_your_people'),
 ('Sifra Kedoshim 4 12 — the great rule', conduct('great_rule'), ['R._Akiva_love_your_neighbor', 'ben_Azzai_the_book_of_the_generations_of_man']),
 ('Nedarim 9:4 — the vow opening\'s five clauses', conduct('vow_opening'), ['no_revenge', 'no_grudge', 'no_hate_in_the_heart', 'love_your_neighbor', 'your_brother_shall_live']),
]

# ---- (3)+(5) run, grade, effects ------------------------------------
n = len(TESTS)
assert n == GUARDED, (n, GUARDED)
print('guard: %d test rows, every expected value a literal from the answer sheet [honest-pairing guard satisfied]' % GUARDED)
print()
ok = 0
frac = {I: 0, M: 0, A: 0, D: 0, P: 0, H: 0}
used = []
misses = []
for name, c, want in TESTS:
    hit = c['v'] == want
    ok += hit
    frac[c['p']] += 1
    used += [e for e in c['fx'] if e != FX.NONE]
    if not hit: misses.append((name, c['v']))
    print('%s %-96s [%s] %s' % ('OK ' if hit else 'MISS', name[:96], c['p'], '' if hit else 'got=%r' % (c['v'],)))
    print('     effects: %s' % ', '.join(c['fx']))
print()
print('MATRIX: %d/%d cells match the answer sheet' % (ok, n))
print('FRACTIONS: pure ink %d/%d (%d%%) · recorded moves %d/%d (%d%%) · answer-sheet %d/%d · data %d/%d · imports %d/%d · hypotheses %d/%d'
      % (frac[I], n, 100 * frac[I] // n, frac[M], n, 100 * frac[M] // n, frac[A], n, frac[D], n, frac[P], n, frac[H], n))
ops = FX.summarize(used)
print('LEDGER OPS this span writes: %s' % ', '.join('%s x%d' % kv for kv in sorted(ops.items())))
print('effects: every cell carries REGISTERED effects — EIGHT discovered in these verses\' own verbs: left_for_the_poor '
      '(TRANSFER), wage_due_by_morning (TIMER), name_profaned, judgment_perverted, given_to_the_heart (HEAVEN), '
      'rebuke_owed, love_owed, rescue_owed (DEBIT) [effects law satisfied]')
_W.print_coverage()
if ok == n:
    print('THE HOLINESS LEDGER, FIRST HALF, COMPILES — the poor gifts on four nouns and one leave-verb, the five verbs '
          'of theft-to-profanation in their written order, the wage clock on "until morning", the judge and the '
          'measurer on one clause at two seats, the heart clause at two; the Lev 5, Tzav, and jubilee engines CALLED.')
else:
    print('MISSES (%d):' % len(misses))
    for m_ in misses: print('  -', m_[0][:80], '->', m_[1])
    sys.exit('MISSES REMAIN — consult the Talmud per gap and recompile.')

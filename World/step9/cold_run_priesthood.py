#!/usr/bin/env python3
"""cold_run_priesthood.py — THE PRIESTHOOD AND ITS DUES (Lev 21:1-24; 22:1-33; 24:1-9)
(2026-09-06, sitting L5 of THE COMPILE DEBT — World/step9/COMPILE_DEBT.md; the
second runner compiled under THE DEPENDENCY GATE's rule: span declared, a stub
placed, the census run, six required edges dispositioned BEFORE the first cell.)

Span: Lev 21:1-15 — THE PRIEST'S DEFILEMENT LICENSE (the six relatives by their
own six tokens, the husband split, the forced defilement), THE MOURNING MARKS
(the razor by live call into the holiness engine), THE FORBIDDEN WIVES (the
zonah three ways, the chalalah, the divorcee, the chalutzah), THE PRIEST'S
DAUGHTER BURNED (against the adulteress's strangling by call), THE HIGH PRIEST
(the one-hour rule, the onen split, the virgin command), THE PROFANED SEED;
Lev 21:16-24 — THE BLEMISH CENSUS OF THE PRIEST (twelve class heads, the
man-beast difference table, the blemished eats, the entry hierarchy); Lev
22:1-16 — THE HOLY THINGS AND THE IMPURE PRIEST (the karet extension, the
sunset gate, the zav by call), WHO EATS TERUMAH (the stranger, the household,
the daughter, the return), THE FIFTH (by call into the Lev 5 engine's own
algebra); Lev 22:17-33 — THE ACCEPTABLE ANIMAL (the vow class, the five-count,
the beast's blemish row sharing three exact tokens with the priest's, the
castration ban, the birth list, the eighth day, it-and-its-young, the day
after the night, the reassignment, the Name sanctified); Lev 24:1-9 — THE LAMP
(the restatement of Exod 27:20-21 with one token dropped) and THE TABLE (the
twelve loaves, the two rows of six, the frankincense as the memorial by call
into the meal-offering engine, the weekly exchange).

Answer sheet ROUTED BY TOPIC under the union rule: Mishnah Bekhorot 6-7,
Terumot 6-8, Yevamot 6-9, Zevachim 8-9, Temurah 6, Menachot 11, Tamid 3,
Chullin 5 read WHOLE (115 rows) + the 37 link rows outside those chapters +
four topic rows — 156 rows, the ledger logic/oral_triage/priesthood_topic_
docket_2026-09-06.md with its coverage computed; 558 Talmud addresses indexed
on the span, opened per gap.

The five motions, in order:
 (1) code from the BARE INK — the defile-verb's four seats in Lev 21; the six
     kin tokens; the take-verb doubled at 21:7 and at 21:14; the profane root's
     seven seats; the burning token's three Leviticus seats; 'blemish' five
     times in 21 and three in 22; 'shall not approach' at four seats; the
     bread token; the acceptance root's seven seats; the sanctifier formula
     six times; 'the name of My holiness' framing Lev 22 (22:2, 22:32); the
     three blemish tokens the two lists SHARE exactly (garav, yalefet, sarua);
     'and from the day' a hapax at 22:27; 'on one day' at 22:28 alone in the
     Torah; 'you shall not leave over' shared with the Passover; 'continually'
     four times in 24:1-9; Exod 27:20's tail restated token for token at 24:2
     and 'and his sons' dropped at 24:3; every quantity a PARAMETER (the
     eighty days, the vetch, the nine-to-eleven window, the dimensions);
 (2) the Mishnah's rows as TEST DATA, each expected value a literal typed
     from the row (the honest-pairing guard runs first);
 (3) run;
 (4) misses filled by NAMED recorded arguments — the Sifra Emor rows (the
     units' spine, verdicted 2026-09-05) and the Talmud where opened;
 (5) the graded matrix with per-cell provenance, fractions, and EFFECTS.

Cross-span receipts, labeled [IMPORT] and, where a compiled callee exists,
CALLED (the edges dispositioned in dependency_dispositions.yaml):
cold_run_holiness_b.body (the razor solve, the corners, the gash multipliers);
cold_run_sanctions.adultery and .burned_nine (the modes); cold_run_clocks.zav
(the zav's tier and count); cold_run_vayikra5.sacrilege (the fifth's added
quarter); cold_run_offerings.dispatch (the acceptable animal's rite and
windows); cold_run_minchah.remainder / .presentation / .frankincense_quantity /
.oil_grade (the showbread and the memorial). Exod 22:29's firstborn eighth
day is fetched by live call from cold_run_ordinances.firstling (E1 closed L5's OWED); Deut 23:2, 23:19,
25:5 and Num 18 stay imports by name.
"""
import sqlite3, sys, os, json, io, contextlib, collections
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import effects_layer as FX
from compile_guards import check_honest_pairing
GUARDED = check_honest_pairing(os.path.abspath(__file__))
assert GUARDED == 252, ("the guard counted %d expectations, the tripwire holds 252" % GUARDED)

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

L21 = list(range(1, 25)); L22 = list(range(1, 34)); L24 = list(range(1, 10))
def seats(ch, pred, rng):
    return [v for v in rng if pred(toks('Lev', ch, v))]
def has(*ws):
    return lambda t: any(t[i:i + len(ws)] == list(ws) for i in range(len(t) - len(ws) + 1))
def anytok(*ws):
    return lambda t: any(w in t for w in ws)

# the whole-Tanakh token census (23,213 verses) — for the span's rare tokens
_ALL = collections.defaultdict(list)
for he, book, ch, vs in db.execute("SELECT w.he, v.book, v.chapter, v.verse FROM words w JOIN verses v ON w.verse_id=v.id"):
    _ALL[strip(he)].append((book, ch, vs))
def tanakh(tok):
    return sorted(set(_ALL.get(tok, [])))
N_VERSES = db.execute("SELECT COUNT(*) FROM verses").fetchone()[0]
assert N_VERSES == 23213, N_VERSES

# ---- (1) ink probes — each MUST fire or the run refuses -------------
PROBES = [
    ('for a SOUL he shall not defile',                  'Lev', 21, 1, 'יטמא'),
    ('except for his KIN near to him',                  'Lev', 21, 2, 'לשארו'),
    ('his virgin SISTER',                               'Lev', 21, 3, 'ולאחתו'),
    ('a HUSBAND shall not defile among his people',     'Lev', 21, 4, 'בעל'),
    ('the corner of their beard they shall not SHAVE',  'Lev', 21, 5, 'יגלחו'),
    ('the BREAD of their God they offer',               'Lev', 21, 6, 'לחם'),
    ('a HARLOT or a profaned woman',                    'Lev', 21, 7, 'זנה'),
    ('and you shall SANCTIFY him',                      'Lev', 21, 8, 'וקדשתו'),
    ('in FIRE she shall be burned',                     'Lev', 21, 9, 'תשרף'),
    ('on whose head the anointing oil was POURED',      'Lev', 21, 10, 'יוצק'),
    ('all souls of the DEAD he shall not come',         'Lev', 21, 11, 'מת'),
    ('from the SANCTUARY he shall not go out',          'Lev', 21, 12, 'המקדש'),
    ('a wife in her VIRGINITY',                         'Lev', 21, 13, 'בבתוליה'),
    ('a WIDOW, a divorcee, a profaned, a harlot',       'Lev', 21, 14, 'אלמנה'),
    ('he shall not PROFANE his seed',                   'Lev', 21, 15, 'יחלל'),
    ('in whom is a BLEMISH shall not approach',         'Lev', 21, 17, 'מום'),
    ('BLIND or lame',                                   'Lev', 21, 18, 'עור'),
    ('BROKEN leg',                                      'Lev', 21, 19, 'שבר'),
    ('the crushed TESTICLE',                            'Lev', 21, 20, 'אשך'),
    ('shall not DRAW NEAR to offer',                    'Lev', 21, 21, 'יגש'),
    ('of the MOST HOLY he may eat',                     'Lev', 21, 22, 'הקדשים'),
    ('to the VEIL he shall not come',                   'Lev', 21, 23, 'הפרכת'),
    ('they shall SEPARATE from the holy things',        'Lev', 22, 2, 'וינזרו'),
    ('and that soul shall be CUT OFF',                  'Lev', 22, 3, 'ונכרתה'),
    ('a LEPER or a zav',                                'Lev', 22, 4, 'צרוע'),
    ('touches any SWARMING thing',                      'Lev', 22, 5, 'שרץ'),
    ('impure until the EVENING',                        'Lev', 22, 6, 'הערב'),
    ('and the SUN sets and he is pure',                 'Lev', 22, 7, 'השמש'),
    ('a CARCASS or a torn thing',                       'Lev', 22, 8, 'נבלה'),
    ('and DIE by it when they profane it',              'Lev', 22, 9, 'ומתו'),
    ('every STRANGER shall not eat holy',               'Lev', 22, 10, 'זר'),
    ('the purchase of his MONEY',                       'Lev', 22, 11, 'כספו'),
    ('the TERUMAH of the holy things',                  'Lev', 22, 12, 'בתרומת'),
    ('she RETURNS to her father\'s house',              'Lev', 22, 13, 'ושבה'),
    ('add its FIFTH to it',                             'Lev', 22, 14, 'חמשיתו'),
    ('which they RAISE to the LORD',                    'Lev', 22, 15, 'ירימו'),
    ('the iniquity of GUILT',                           'Lev', 22, 16, 'אשמה'),
    ('for a BURNT OFFERING',                            'Lev', 22, 18, 'לעלה'),
    ('WHOLE, male',                                     'Lev', 22, 19, 'תמים'),
    ('not for ACCEPTANCE for you',                      'Lev', 22, 20, 'לרצון'),
    ('a sacrifice of PEACE OFFERINGS',                  'Lev', 22, 21, 'שלמים'),
    ('blind or broken or CHARUTZ',                      'Lev', 22, 22, 'חרוץ'),
    ('SARUA or kalut',                                  'Lev', 22, 23, 'שרוע'),
    ('CRUSHED, pounded, torn, cut',                     'Lev', 22, 24, 'ומעוך'),
    ('from the hand of a FOREIGNER',                    'Lev', 22, 25, 'נכר'),
    ('seven days UNDER its mother',                     'Lev', 22, 27, 'תחת'),
    ('it and its YOUNG',                                'Lev', 22, 28, 'בנו'),
    ('a sacrifice of THANKSGIVING',                     'Lev', 22, 29, 'תודה'),
    ('you shall not LEAVE OVER until morning',          'Lev', 22, 30, 'תותירו'),
    ('and I shall be SANCTIFIED among the children of Israel', 'Lev', 22, 32, 'ונקדשתי'),
    ('pure BEATEN olive oil',                           'Lev', 24, 2, 'כתית'),
    ('OUTSIDE the veil of the testimony',               'Lev', 24, 3, 'מחוץ'),
    ('on the PURE menorah',                             'Lev', 24, 4, 'הטהרה'),
    ('TWELVE loaves',                                   'Lev', 24, 5, 'עשרה'),
    ('SIX the row',                                     'Lev', 24, 6, 'שש'),
    ('pure FRANKINCENSE for a memorial',                'Lev', 24, 7, 'לבנה'),
    ('on the SABBATH day, on the Sabbath day',          'Lev', 24, 8, 'השבת'),
    ('to Aaron and his sons, MOST HOLY',                'Lev', 24, 9, 'קדשים'),
]
missing = [p for p in PROBES if p[4] not in toks(p[1], p[2], p[3])]
if missing:
    for p in missing: print('PROBE FAILED:', p)
    sys.exit('zero-report law: the ink scan is not trusted until every probe fires')
print('probes: %d/%d fired (the ink scan is trusted; the whole-Tanakh census holds %d verses)' % (len(PROBES), len(PROBES), N_VERSES))

# ---- the censuses (TRIPWIRES — each a measured literal) ------------
c_yitma = seats(21, anytok('יטמא'), L21)
assert c_yitma == [1, 3, 4, 11], c_yitma                                        # the defile-verb: the ban, the license, the husband, the high priest
KIN = ('לאמו', 'ולאביו', 'ולבנו', 'ולבתו', 'ולאחיו', 'ולאחתו')
c_kin = [w for v in (2, 3) for w in toks('Lev', 21, v) if w in KIN]
assert c_kin == list(KIN), c_kin                                                 # the six relatives, one token each (the wife = 'his kin', 21:2)
c_take = (seats(21, anytok('יקחו'), L21), toks('Lev', 21, 7).count('יקחו'), seats(21, anytok('יקח'), L21), toks('Lev', 21, 14).count('יקח'))
assert c_take == ([7], 2, [13, 14], 2), c_take                                   # the take-verb doubled at 21:7 (the commoner) and at 21:14 (the high priest)
c_profane = [(v, [w for w in toks('Lev', 21, v) if 'חלל' in w or w == 'תחל']) for v in L21 if any('חלל' in w or w == 'תחל' for w in toks('Lev', 21, v))]
assert [v for v, _ in c_profane] == [6, 7, 9, 12, 14, 15, 23], c_profane        # the profane root's seven seats (21:9 twice)
c_holy_6_8 = [w for v in (6, 7, 8) for w in toks('Lev', 21, v) if 'קדש' in w or 'קדוש' in w]
assert len(c_holy_6_8) == 7, c_holy_6_8
c_burn = [s for s in tanakh('תשרף') if s[0] == 'Lev']
assert c_burn == [('Lev', 6, 23), ('Lev', 13, 52), ('Lev', 21, 9)], c_burn      # 'shall be burned': the sin offering, the garment, the daughter
c_mum21 = (seats(21, anytok('מום'), L21), [toks('Lev', 21, v).count('מום') for v in (17, 18, 21, 23)])
assert c_mum21 == ([17, 18, 21, 23], [1, 1, 2, 1]), c_mum21                      # 'blemish' five times in the priest's file
c_mum22 = seats(22, anytok('מום'), L22)
assert c_mum22 == [20, 21, 25], c_mum22                                          # three times in the animal's
c_approach = (seats(21, anytok('יקרב'), L21), seats(21, anytok('יגש'), L21), toks('Lev', 21, 21).count('יגש'), 'יבא' in toks('Lev', 21, 23))
assert c_approach == ([17, 18], [21, 23], 2, True), c_approach                   # 'shall not approach' x4 + 'shall not come' to the veil
c_bread = (seats(21, anytok('לחם'), L21), seats(22, anytok('לחם'), L22), seats(24, anytok('ללחם', 'לחם'), L24))
assert c_bread == ([6, 8, 17, 21, 22], [25], [7]), c_bread                       # 'bread' = the offerings (Sifra Section 3 3; Onkelos)
c_tamim = seats(22, anytok('תמים'), L22)
assert c_tamim == [19, 21], c_tamim
c_ratzon = seats(22, anytok('לרצנכם', 'לרצון', 'ירצה', 'ירצו'), L22)
assert c_ratzon == [19, 20, 21, 23, 25, 27, 29], c_ratzon                        # the acceptance root at seven seats (22:24's 'your land' a homograph)
c_ani = (seats(21, has('אני', 'יהוה'), L21), seats(22, has('אני', 'יהוה'), L22))
assert c_ani == ([8, 12, 15, 23], [2, 3, 8, 9, 16, 30, 31, 32, 33]), c_ani
c_mekadesh = [(c, v) for c, rng in ((21, L21), (22, L22)) for v in rng if any(w in ('מקדשכם', 'מקדשו', 'מקדשם') for w in toks('Lev', c, v))]
assert c_mekadesh == [(21, 8), (21, 15), (21, 23), (22, 9), (22, 16), (22, 32)], c_mekadesh   # 'I the LORD who sanctifies you/him/them' x6
c_shem = [s for s in _ALL['קדשי'] if s[0] == 'Lev' and has('שם', 'קדשי')(toks(*s))]
assert sorted(set(c_shem)) == [('Lev', 20, 3), ('Lev', 22, 2), ('Lev', 22, 32)], c_shem   # 'the name of My holiness' frames Lev 22 (and Molech's 20:3)
c_venikdashti = tanakh('ונקדשתי')
assert c_venikdashti == [('Ezek', 20, 41), ('Ezek', 28, 22), ('Ezek', 28, 25), ('Ezek', 39, 27), ('Lev', 22, 32)], c_venikdashti   # the Torah's only seat
A_ = set(w for v in (18, 19, 20) for w in toks('Lev', 21, v)); B_ = set(w for v in (22, 23, 24) for w in toks('Lev', 22, v))
c_shared = sorted(A_ & B_ - {'או', 'לא'})
assert c_shared == ['גרב', 'ילפת', 'שרוע'], c_shared                             # the two blemish lists share exactly three tokens
c_zar = seats(22, anytok('זר'), L22)
assert c_zar == [10, 12, 13], c_zar
c_terumah = [(v, w) for v in L22 for w in toks('Lev', 22, v) if 'תרומ' in w or w == 'ירימו']
assert c_terumah == [(12, 'בתרומת'), (15, 'ירימו')], c_terumah
c_fifth = tanakh('חמשיתו')
assert c_fifth == [('Lev', 22, 14), ('Lev', 27, 31)], c_fifth                     # this spelling of 'its fifth': here and the tithe's redemption
c_sunset = sorted(set(s for s in _ALL['ובא'] if has('ובא', 'השמש')(toks(*s))))
assert c_sunset == [('Eccl', 1, 5), ('Lev', 22, 7)], c_sunset                     # 'and the sun sets' — here and Ecclesiastes
c_zav = (seats(22, anytok('זב'), L22), seats(22, anytok('צרוע'), L22), has('איש', 'איש')(toks('Lev', 22, 4)))
assert c_zav == ([4], [4], True), c_zav
c_eat22 = sum(1 for v in L22 for w in toks('Lev', 22, v) if 'אכל' in w)
assert c_eat22 == 14, c_eat22                                                    # the eating verb fourteen times in Lev 22
c_umiyom = tanakh('ומיום')
assert c_umiyom == [('Lev', 22, 27)], c_umiyom                                   # 'and from the day' — a hapax: 'and from the eighth day onward'
c_one_day = sorted(set(s for s in _ALL['ביום'] if s[0] in ('Gen', 'Exod', 'Lev', 'Num', 'Deut') and has('ביום', 'אחד')(toks(*s))))
assert c_one_day == [('Lev', 22, 28)], c_one_day                                 # 'on one day' — the Torah's only seat (ben Zoma reaches Gen 1:5's 'one day' by the noun)
c_leftover = tanakh('תותירו')
assert c_leftover == [('Exod', 12, 10), ('Lev', 22, 30), ('Num', 33, 55)], c_leftover   # shared with the Passover's clause
c_pele = tanakh('לפלא')
assert c_pele == [('Lev', 22, 21), ('Num', 15, 3), ('Num', 15, 8)], c_pele
c_nekhar = [s for s in _ALL['נכר'] if s[0] == 'Lev']
assert c_nekhar == [('Lev', 22, 25)], c_nekhar
c_under = (has('שבעת', 'ימים', 'תחת', 'אמו')(toks('Lev', 22, 27)), has('שבעת', 'ימים', 'יהיה', 'עם', 'אמו')(toks('Exod', 22, 29)), 'השמיני' in toks('Exod', 22, 29))
assert c_under == (True, True, True), c_under                                     # 'UNDER its mother' here, 'WITH its mother' at Exod 22:29 — both name the eighth day
c_tamid = (seats(24, anytok('תמיד'), L24), toks('Lev', 24, 8).count('השבת'))
assert c_tamid == ([2, 3, 4, 8], 2), c_tamid                                      # 'continually' x4; 'the Sabbath' doubled at 24:8
c_pure = (seats(24, anytok('זך', 'זכה'), L24), seats(24, anytok('הטהרה', 'הטהר'), L24))
assert c_pure == ([2, 7], [4, 6]), c_pure                                         # pure oil, pure frankincense; the pure menorah, the pure table
E20, L2 = toks('Exod', 27, 20), toks('Lev', 24, 2)
c_restate = (len([w for w in L2 if w in E20]), len(L2), E20[-13:] == L2[-13:])
assert c_restate == (13, 14, True), c_restate                                     # Exod 27:20's thirteen-token tail restated at 24:2 (only the opening verb differs)
c_sons = ('ובניו' in toks('Exod', 27, 21), 'ובניו' in toks('Lev', 24, 3))
assert c_sons == (True, False), c_sons                                            # 'and his sons' at Exod 27:21, DROPPED at Lev 24:3 (Sifra Section 13 10: one priest)
c_katit = tanakh('כתית')
assert c_katit == [('1Kgs', 5, 25), ('Exod', 27, 20), ('Exod', 29, 40), ('Lev', 24, 2), ('Num', 28, 5)], c_katit
c_table = [w for v in (5, 6, 7) for w in toks('Lev', 24, v) if w in ('שתים', 'עשרה', 'שני', 'עשרנים', 'מערכות', 'שש', 'המערכת', 'לבנה', 'זכה', 'לאזכרה')]
assert c_table == ['שתים', 'עשרה', 'שני', 'עשרנים', 'שתים', 'מערכות', 'שש', 'המערכת', 'המערכת', 'לבנה', 'זכה', 'לאזכרה'], c_table
c_azkarah = [(c, v) for c in (2, 5, 6, 24) for v in range(1, 40) if any('אזכר' in w for w in toks('Lev', c, v))]
assert c_azkarah == [(2, 2), (2, 9), (2, 16), (5, 12), (6, 8), (24, 7)], c_azkarah   # the memorial noun: the meal offering's five seats and the showbread's
c_close = (seats(24, has('קדש', 'קדשים'), L24), seats(24, has('לאהרן', 'ולבניו'), L24), [(v, [w for w in toks('Lev', 24, v) if w in ('חקת', 'חק', 'ברית', 'עולם')]) for v in (3, 8, 9)])
assert c_close == ([9], [9], [(3, ['חקת', 'עולם']), (8, ['ברית', 'עולם']), (9, ['חק', 'עולם'])]), c_close
c_dorot = (seats(21, anytok('לדרתם', 'לדרתיכם'), L21), seats(22, anytok('לדרתם', 'לדרתיכם'), L22), seats(24, anytok('לדרתם', 'לדרתיכם'), L24))
assert c_dorot == ([17], [3], [3]), c_dorot
c_amav = seats(21, anytok('בעמיו', 'מעמיו'), L21)
assert c_amav == [1, 4, 14, 15], c_amav
c_betula = [(v, [w for w in toks('Lev', 21, v) if 'בתול' in w]) for v in L21 if any('בתול' in w for w in toks('Lev', 21, v))]
assert c_betula == [(3, ['הבתולה']), (13, ['בבתוליה']), (14, ['בתולה'])], c_betula
c_vows = [(v, [w for w in toks('Lev', 22, v) if 'נדב' in w or 'נדר' in w]) for v in L22 if any('נדב' in w or 'נדר' in w for w in toks('Lev', 22, v))]
assert c_vows == [(18, ['נדריהם', 'נדבותם']), (21, ['נדר', 'לנדבה']), (23, ['נדבה', 'ולנדר'])], c_vows
c_ish_ish = (has('איש', 'איש')(toks('Lev', 22, 18)), has('כל', 'איש')(toks('Lev', 21, 18)), toks('Lev', 22, 14)[:3] == ['ואיש', 'כי', 'יאכל'], toks('Lev', 22, 11)[:3] == ['וכהן', 'כי', 'יקנה'])
assert c_ish_ish == (True, True, True, True), c_ish_ish
print('censuses: defile-verb at %s · six kin tokens %s · take-verb %s · profane root at %s · burn token %s · blemish 21 %s / 22 %s · approach %s '
      '· bread %s · whole at %s · acceptance at %s · "I am the LORD" %s · the sanctifier formula at %s · "name of My holiness" %s · "I shall be sanctified" %s '
      '· SHARED blemish tokens %s · stranger at %s · terumah tokens %s · "its fifth" %s · sunset %s · zav %s · eating x%d in Lev 22 · "and from the day" %s '
      '· "on one day" (Torah) %s · leftover %s · "to set apart" %s · foreigner %s · under/with %s · continually %s · pure %s · Exod 27:20 restated %s · "and his sons" %s '
      '· beaten %s · the table tokens %s · memorial %s · the close %s · generations %s · "his people" %s · virgin %s · vows %s · man-man %s'
      % (c_yitma, c_kin, c_take, [v for v, _ in c_profane], c_burn, c_mum21, c_mum22, c_approach, c_bread, c_tamim, c_ratzon, c_ani, c_mekadesh, c_shem,
         c_venikdashti, c_shared, c_zar, c_terumah, c_fifth, c_sunset, c_zav, c_eat22, c_umiyom, c_one_day, c_leftover, c_pele, c_nekhar, c_under, c_tamid,
         c_pure, c_restate, c_sons, c_katit, c_table, c_azkarah, c_close, c_dorot, c_amav, c_betula, c_vows, c_ish_ish))

# ---- the callees (cold) --------------------------------------------
_buf = io.StringIO()
with contextlib.redirect_stdout(_buf):
    import cold_run_holiness_b as HB
    import cold_run_sanctions as SA
    import cold_run_clocks as CL
    import cold_run_vayikra5 as V5
    import cold_run_offerings as OFF
    import cold_run_minchah as MIN
    import cold_run_ordinances as ORD
FIRSTLING_8 = ORD.firstling('eighth_and_onward')['v']
RAZOR = HB.body('razor', tool='razor')['v']; SCISSORS = HB.body('razor', tool='scissors')['v']
CORNERS = HB.body('corners_count')['v']; GASH_5x1 = HB.body('multipliers', gashes=5, dead=1)['v']; GASH_DEAD = HB.body('gash_for_dead')['v']
ADULTERY_MODE = SA.adultery('mode')['v']; BURNED_NINE = SA.burned_nine()['v']
ZAV_TIER3 = CL.zav('tier', sightings=3)['v']; ZAV_START = CL.zav('count_start')['v']
FIFTH_CALL = V5.sacrilege({'kind': 'meilah', 'unwitting': True, 'benefit': True, 'damage': True, 'value': 100.0}, V5.DATA)[0]
FIFTH_DELIB = V5.sacrilege({'kind': 'meilah', 'unwitting': False}, V5.DATA)[0]
OLAH_DISP = OFF.dispatch('olah:flock')['disposition']['v']; OLAH_PLACE = OFF.dispatch('olah:flock')['place']['v']
SHEL_WINDOW = OFF.dispatch('shelamim')['window']['v']; TODAH_WINDOW = OFF.dispatch('todah_and_nazir_ram')['window']['v']
SHOW_REM = MIN.remainder('showbread')['v']; SHOW_PRES = MIN.presentation('showbread')['v']; FRANK_Q = MIN.frankincense_quantity()['v']; OIL_GRADE = MIN.oil_grade()['v']
print('routing receipts: cold_run_holiness_b.body CALLED — razor -> %r, scissors -> %r, corners -> %r; cold_run_sanctions CALLED — adultery mode -> %r, burned nine -> %d names; '
      'cold_run_clocks.zav CALLED — tier(3) -> %r, count_start -> %r; cold_run_vayikra5.sacrilege CALLED -> %r; cold_run_offerings.dispatch CALLED — olah disposition -> %r, '
      'shelamim window -> %r, todah window -> %r; cold_run_minchah CALLED — showbread remainder -> %r, presentation -> %r, frankincense -> %r, oil grade -> %r [IMPORT, live calls]'
      % (RAZOR, SCISSORS, CORNERS, ADULTERY_MODE, len(BURNED_NINE), ZAV_TIER3, ZAV_START, FIFTH_CALL, OLAH_DISP, SHEL_WINDOW, TODAH_WINDOW, SHOW_REM, SHOW_PRES, FRANK_Q, OIL_GRADE))

I, M, A, D, P, H = 'INK', 'MOVE', 'ANSWER-SHEET', 'DATA', 'IMPORT', 'HYPOTHESIS'   # H: THE LINK REVIEW LAW (LR3, 2026-09-07) — an untaught transfer, kept and labeled, never counted as compiled
def cell(v, p, why, fx):
    FX.validate(fx)
    return {'v': v, 'p': p, 'why': why, 'fx': fx}
SE = 'Sifra, Emor, '

# =====================================================================
# THE CODE — from the ink of Leviticus 21, 22, and 24:1-9 alone. Mishnah/
# Talmud appear ONLY on [MOVE] lines (motion 4) and as DATA (motion 2).
# =====================================================================

# ---- F1: THE PRIEST'S FILE (21:1-15) — defilement, marks, wives, the daughter, the high priest, the seed ----
RELATIVES = ['wife', 'mother', 'father', 'son', 'daughter', 'brother', 'virgin_sister']
def family(q, **k):
    if q == 'addressees':
        return cell({'sons_of_aaron': 'bound', 'daughters_of_aaron': 'free', 'chalalim': 'excluded', 'blemished_and_minors': 'included'}, M,
                    '21:1 "say to the PRIESTS the SONS OF AARON" — ' + SE + 'Section 1 1: four populations by two tokens (Mishnah Kiddushin 1:7: the '
                    'negatives bind women EXCEPT defiling for the dead)', ['defiled_for_kin'])
    if q == 'defile_seats':
        return cell([1, 3, 4, 11], I, 'the defile-verb at four seats of the chapter (%s): the ban (21:1), the license "for her" (21:3), the husband (21:4), '
                    'the high priest "for his father and his mother" (21:11)' % (c_yitma,), [FX.NONE])
    if q == 'soul_scope':
        return cell({'corpse': 'defiles', 'blood_quarter_log': 'defiles', 'departing_impurities': 'included'}, M,
                    '21:1 "for a SOUL" — ' + SE + 'Section 1 2-3: blood included by Deut 12:23 ("the blood is the soul"), a quarter-log; what departs from the dead', ['defiled_for_kin'])
    if q == 'met_mitzvah':
        return cell('defiles_for_the_abandoned_corpse', M, '21:1 "among his people" — ' + SE + 'Section 1 3: when his people are there he does not defile; the '
                    'abandoned corpse has none — he DOES (21:11 for the high priest too, Section 2 4)', ['defiled_for_kin'])
    if q == 'relatives':
        return cell(RELATIVES, I, ('the six kin tokens %s at 21:2-3, one per relative, and 21:2 "his KIN near to him" = the wife (' + SE +
                    'Section 1 4: "she is your father\'s flesh"); seven in all') % (c_kin,), ['defiled_for_kin'])
    if q == 'relative_table':
        return cell({'wife': 'the_near_kin_betrothed_and_divorced_excluded', 'mother': 'profanable_line', 'father': 'presumption', 'children': 'viable_not_stillborn',
                     'siblings': 'paternal_who_inherit_him', 'sister': 'minor_virgin_not_betrothed_R_Meir_incl_betrothed', 'brother': 'minor_or_adult'}, M,
                    SE + 'Section 1 4-10: THE RELATIVE TABLE BY TOKEN PAIRS — every relative proven non-derivable from its neighbor by a mirrored argument', ['defiled_for_kin'])
    if q == 'sister_predicate':
        return cell({'raped_or_seduced': 'excluded_by_virgin', 'wood_injured': 'included_not_by_a_man', 'betrothed': 'included_by_the_near', 'adult': 'included_by_to_him'}, M,
                    '21:3 "the virgin... who has not been to a man" — ' + SE + 'Section 1 11-12: the agent-of-loss test', ['defiled_for_kin'])
    if q == 'forced':
        return cell('a_command_enforced_against_his_will', M, '21:3 "for her he SHALL defile" — ' + SE + 'Section 1 12: Yosef the priest on Passover eve, '
                    'pushed and defiled by the sages (Mishnah Bekhorot 7:7: the refuser disqualified until he accepts)', ['defiled_for_kin'])
    if q == 'certain_only':
        return cell({'doubtful': 'no', 'others_alongside': 'no', 'limb_of_living_parent': 'no', 'barley_bone': ['yes', 'R._Yosei_no']}, M,
                    SE + 'Section 1 13 — "for her": the certain, not the doubtful; not for her limbs', [FX.NONE])
    if q == 'husband':
        w = k.get('wife')
        if w == 'fit':
            return cell('defiles', M, '21:4 "a HUSBAND shall not defile among his people" — ' + SE + 'Section 1 15: there is a husband who defiles (for a fit wife)', ['defiled_for_kin'])
        if w == 'unfit':
            return cell('does_not_defile', M, SE + 'Section 1 15: for an unfit wife (a forbidden marriage) he does not', [FX.NONE])
    if q == 'husband_fork':
        return cell({'sifra': 'husband', 'onkelos': 'the_great_one_among_his_people'}, M, '21:4 בַּעַל read two ways — ' + SE + 'Section 1 15 (husband) vs Onkelos Lev 21:4 '
                    '("the GREAT ONE among his people shall not defile") — a recorded fork on one token', [FX.NONE])
    if q == 'toggles':
        return cell('profane_while_occupied_holy_on_withdrawal', M, '21:4 "to profane himself" — ' + SE + 'Section 1 16: a status that toggles with the act, not a stain', ['defiled_for_kin'])
    if q == 'marks':
        return cell({'baldness': 'per_spot_whole_head', 'beard': 'per_corner', 'gash': 'per_gash_for_the_dead'}, M,
                    '21:5 the three marks — ' + SE + 'Chapter 1 1-5: per bald spot, the whole head (not only "between the eyes", Deut 14:1), per gash; '
                    'THE TWO-WAY TRANSFER: per-spot and whole-head carried to Israel, for-the-dead-only carried to the priests (baldness-baldness, gash-gash)', ['lashes'])
    if q == 'razor':
        return cell(RAZOR, P, '21:5 "the corner of their beard they shall not SHAVE" is the razor\'s SECOND constraint — Lev 19:27 "destroy" AND 21:5 "shave" = '
                    'shaving with destruction (M-21): CALLED cold_run_holiness_b.body(razor) -> %r; scissors -> %r [IMPORT, live call]' % (RAZOR, SCISSORS), ['lashes'])
    if q == 'corners':
        return cell(CORNERS, P, 'the corners counted at the home cell (Mishnah Makkot 3:5: two on the head, five on the beard): CALLED cold_run_holiness_b.body(corners_count) '
                    '-> %r' % (CORNERS,), ['lashes'])
    if q == 'gash_multiplier':
        return cell(GASH_5x1, P, 'five gashes for one dead: CALLED cold_run_holiness_b.body(multipliers) -> %r; the gash %r (21:5 "in their flesh" with 19:28 "for a soul")'
                    % (GASH_5x1, GASH_DEAD), ['lashes'])
    if q == 'holy_by_compulsion':
        return cell({'compelled': True, 'levites': 'excluded', 'blemished': 'included'}, M, '21:6 "holy they SHALL BE to their God" — ' + SE + 'Chapter 1 6: by compulsion; '
                    '"the bread of their God THEY offer" — not the Levites; holiness not service-conditioned', [FX.NONE])
    if q == 'bread_is_offering':
        return cell([6, 8, 17, 21, 22], I, ('"bread" at five seats of the chapter (%s) — Onkelos Lev 21:6 renders it "the OFFERING of their God" (' + SE +
                    'Section 3 3: the daily offerings are called bread, Num 28:2)') % (c_bread[0],), [FX.NONE])
    if q == 'zonah':
        return cell({'R._Yehuda': 'the_aylonit', 'sages': ['the_convert', 'the_freed_slavewoman', 'illicit_intercourse'], 'R._Eliezer': 'even_unmarried_not_for_marriage', 'onkelos': 'one_who_goes_astray'}, M,
                    '21:7 "a woman ZONAH" — ' + SE + 'Chapter 1 7 (Mishnah Yevamot 6:5 verbatim); Onkelos Lev 21:7 on the sages\' arm', ['profaned_seed'])
    if q == 'chalalah':
        return cell('born_of_a_disqualified_union', M, '21:7 "or a PROFANED woman" — ' + SE + 'Chapter 1 8', ['profaned_seed'])
    if q == 'chalutzah':
        return cell(['barred_by_a_fortiori_from_the_divorcee', 'the_rival_refutes', 'and_a_woman_amplifies', 'the_rival_out_by_from_her_husband'], M,
                    '21:7 "a woman divorced FROM HER HUSBAND" — ' + SE + 'Chapter 1 9-10: the chalutzah in, the rival wife out (Mishnah Makkot 3:1: divorcee-and-chalutzah ONE name)', ['profaned_seed'])
    if q == 'husbands_hand':
        return cell('the_second_bill_does_not_disqualify_her', M, SE + 'Chapter 1 11 — R. Elazar b. Matya: "divorced from her HUSBAND", not from one who is not '
                    '(Mishnah Yevamot 10:3 verbatim)', [FX.NONE])
    if q == 'take_doubled':
        return cell({'21:7': 2, '21:14': 2}, I, ('the take-verb DOUBLED at 21:7 and at 21:14 (%s) — ' + SE + 'Chapter 1 12: the woman is warned through the man '
                    '(Mishnah Yevamot 6:2: intercourse with the disqualified DISQUALIFIES HER)') % (c_take,), ['profaned_seed'])
    if q == 'sanctify_him':
        return cell({'by_force': 'beat_him_if_he_refuses', 'warned': 'the_court', 'blemished': 'holy'}, M, ('21:8 "and you shall SANCTIFY him... I the LORD sanctify you" — ' + SE +
                    'Chapter 1 13: the court warned; the sanctifier formula at %s') % (c_mekadesh,), [FX.NONE])
    if q == 'daughter_mode':
        return cell('burning', I, '21:9 "in FIRE she shall be burned" — the burn token\'s three Leviticus seats %s (the sin offering, the garment, the daughter); '
                    'the adulteress\'s default is CALLED from the sanctions engine -> %r (unwritten mode = strangling): 21:9 OVERRIDES it for the priest\'s daughter' % (c_burn, ADULTERY_MODE), ['burned_by_court'])
    if q == 'daughter_in_burned_list':
        return cell(True, P, 'Mishnah Sanhedrin 9:1 "these are burned: a woman and her daughter, and the PRIEST\'S DAUGHTER who played the harlot" — the nine of the first '
                    'clause CALLED from cold_run_sanctions.burned_nine (%d names); this span supplies the tenth' % len(BURNED_NINE), ['burned_by_court'])
    if q == 'daughter_predicate':
        return cell({'by': 'whoring_with_a_husbands_bond', 'not_by': 'other_profanations', 'ages': 'all', 'husbands': 'israelite_levite_netin_mamzer', 'partner': 'not_burned', 'perjured': 'not_burned', 'father': ['R._Eliezer_with_her_father_burning', 'with_her_father_in_law_stoning']}, M,
                    SE + 'Chapter 1 14-18 (Mishnah Sanhedrin 11:1: the perjured strangled; Terumot 7:2: burning even married to an Israelite)', ['burned_by_court'])
    if q == 'onkelos_daughter':
        return cell('strays_from_her_fathers_holiness', M, 'Onkelos Lev 21:9 — the profanation as departure from the father\'s sanctity', [FX.NONE])
    if q == 'greatness':
        return cell(['beauty', 'wealth', 'strength', 'wisdom', 'appearance', 'made_great_from_his_brothers'], M, '21:10 "the priest GREATER than his brothers" — ' + SE + 'Section 2 1', ['invested_office'])
    if q == 'one_hour':
        return cell('office_attaches_at_the_pouring', M, '21:10 "on whose head the anointing oil was POURED" — ' + SE + 'Section 2 2: even one hour (Exod 29:30\'s seven days bounded); '
                    'the many-garmented by "the crown of the oil" (Section 2 6; Mishnah Horayot 3:4)', ['invested_office'])
    if q == 'hair_rend':
        return cell({'R._Yehuda': 'not_at_all', 'R._Meir': 'not_for_his_dead', 'geometry': 'high_priest_below_commoner_above'}, M, '21:10 "his head he shall not let grow wild, his garments not rend" — ' + SE + 'Section 2 3', [FX.NONE])
    if q == 'high_priest_dead':
        return cell({'two_prohibitions': ['shall_not_come', 'shall_not_defile'], 'commoner_carries_both': 'by_not_defile_not_defile', 'two_corpses_blood': 'R._Akiva_defiles', 'parents': 'no', 'met_mitzvah': 'yes'}, M,
                    '21:11 — ' + SE + 'Section 2 4', ['defiled_for_kin'])
    if q == 'not_out':
        return cell({'R._Meir': 'after_them_hidden_and_revealed_to_the_city_gate', 'R._Yehuda': 'not_at_all'}, M, '21:12 "from the sanctuary he shall not go out" — ' + SE +
                    'Section 2 5 (Mishnah Sanhedrin 2:1 verbatim)', [FX.NONE])
    if q == 'onen':
        rank = k.get('rank')
        if rank == 'high':
            return cell('valid', M, '21:12 "shall not profane" — he does not: ' + SE + 'Section 2 6, the high priest serving as an onen', ['accepted'])
        return cell('invalid', M, SE + 'Section 2 6: the commoner onen\'s service invalid', ['service_profaned'])
    if q == 'nezer':
        return cell('the_crown_of_the_oil_the_many_garmented_included', M, ('21:12 "the CROWN of the anointing oil" (%s; Onkelos "crown") — ' + SE + 'Section 2 6') % (seats(21, anytok('נזר'), L21),), ['invested_office'])
    if q == 'virgin_command':
        return cell({'king_nazirite': 'excluded', 'war_priest': 'included', 'adult': ['excluded', 'R._Eliezer_R._Shimon_permit'], 'betrothed_then_appointed': 'marries', 'yevamah_by_maamar': 'not'}, M,
                    ('21:13 "HE... a wife in her virginity" — ' + SE + 'Section 2 7 + Chapter 2 6 (Mishnah Yevamot 6:4 verbatim); the virgin root at %s') % (c_betula,), [FX.NONE])
    if q == 'four_barred':
        return cell(['widow', 'divorcee', 'profaned', 'harlot'], I, '21:14 the four nouns in the verse\'s order; the widow written for the high priest ALONE (21:14; the commoner\'s '
                    'list at 21:7 lacks her) — Mishnah Yevamot 6:4, Makkot 3:1', ['profaned_seed'])
    if q == 'seed':
        return cell({'status': 'chalal_not_mamzer', 'widow_written': 'stringent_her_seed_profaned', 'divorcee_written': 'lenient_not_mamzer', 'commoner': 'exported_by_zonah_zonah', 'niddah': 'not_chalal_by_these', 'she_herself': 'profaned', 'chalals_daughter': 'disqualified'}, M,
                    '21:14-15 "THESE he shall not take... he shall not profane his seed" — ' + SE + 'Chapter 2 1-8: the demonstrative fences the karet a-fortiori', ['profaned_seed'])
    if q == 'profane_seats':
        return cell([6, 7, 9, 12, 14, 15, 23], I, 'the profane root at seven seats of the chapter (%s; 21:9 twice): the Name, the wife, the daughter, the sanctuary, the wife again, '
                    'the seed, the sanctuaries' % ([v for v, _ in c_profane],), [FX.NONE])
    if q == 'yevamot_table':
        her, his_rank, brother_rank = k['her'], k['rank'], k['brother']
        def barred(status, rank):
            return status in ('divorcee', 'chalutzah', 'zonah', 'chalalah') or (status == 'widow' and rank == 'high') or rank == 'chalal' and status == 'fit_for_chalal_only'
        to_husband = 'forbidden' if barred(her, his_rank) else 'permitted'
        to_levir = 'forbidden' if barred(her, brother_rank) else 'permitted'
        return cell({'husband': to_husband, 'levir': to_levir}, I, '21:7 / 21:14 as a two-parameter predicate (her status, his RANK) run for the husband and again for the brother '
                    '(Mishnah Yevamot 9:1-2\'s table); the levirate transfer Deut 25:5 [IMPORT]', ['profaned_seed'])
    if q == 'conduct_bars':
        return cell({'marries_in_transgression': 'disqualified_until_he_vows_off_benefit', 'defiles_for_the_dead': 'disqualified_until_he_accepts'}, A,
                    'Mishnah Bekhorot 7:7 — the two conduct bars of 21:7 and 21:1 joined to the blemish table: the priest\'s status toggles with his acts', ['service_profaned'])
    if q == 'lash_count':
        return cell({'all_day': 'one', 'warned_each_time': 'each', 'in_the_furrow_of_eight': 'one_of_the_eight'}, A, 'Mishnah Makkot 3:8-9 on 21:1\'s defilement', ['lashes'])
    if q == 'lost_object':
        return cell('does_not_defile_nor_obey_his_father', A, 'Mishnah Bava Metzia 2:10 — the lost object in the cemetery; the parent\'s "defile" not obeyed (Lev 19:3\'s override)', [FX.NONE])
    if q == 'women':
        return cell('the_daughters_of_aaron_free', A, 'Mishnah Kiddushin 1:7 — "do not defile for the dead" among the three negatives women are free of; = ' + SE + 'Section 1 1', [FX.NONE])
    if q == 'not_transferable':
        return cell('perjured_not_made_chalal_forty_lashes', A, 'Mishnah Makkot 1:1 — the chalal status is a birth, not a sentence', ['lashes'])
    if q == 'war_front':
        return cell('does_not_return', A, 'Mishnah Sotah 8:3 — the widow to the high priest, the divorcee and chalutzah to the commoner: a transgression-marriage does not send him home', [FX.NONE])
    if q == 'amav_seats':
        return cell([1, 4, 14, 15], I, '"his people" at four seats (%s): the defilement (1, 4), the virgin "from his people" (14), the seed "among his people" (15)' % (c_amav,), [FX.NONE])
    if q == 'ketubah':
        return cell('has_a_ketubah', A, 'Mishnah Yevamot 9:3 — the widow to the high priest and the divorcee to the commoner have a ketubah (the secondary degrees self-labeled "from the scribes")', [FX.NONE])
    raise ValueError(q)

# ---- F2: THE BLEMISH CENSUS OF THE PRIEST (21:16-24) ----
HEADS = ['blind', 'lame', 'charum', 'sarua', 'broken_leg', 'broken_hand', 'giben', 'dak', 'tevallul', 'garav', 'yalefet', 'meroach_ashekh']
MEMBERS = {'blind': ['both_eyes_or_one', 'permanent_cataract', 'permanent_water'], 'lame': ['both_legs_or_one', 'hollow_or_sickle_foot'],
           'charum': ['sunken_nose', 'blocked', 'bridgeless', 'dripping'], 'sarua': ['dislocated_hip', 'extra_bone_from_the_thumb', 'heel_jutting_back', 'goose_wide_foot'],
           'broken_leg': ['bent', 'twisted', 'bandy'], 'broken_hand': ['fingers_joined_below_the_joint'], 'giben': ['no_eyebrows_or_one', 'R._Dosa_lying', 'R._Chanina_two_backs_two_spines'],
           'dak': ['the_cloud', 'the_snail', 'the_serpent', 'the_grape'], 'tevallul': ['white_breaking_the_ring_into_the_black', 'R._Yosei_no_blemish_in_the_white'],
           'garav': ['the_dry_scab'], 'yalefet': ['the_egyptian_lichen'], 'meroach_ashekh': ['R._Yishmael_crushed', 'R._Akiva_wind', 'R._Chanina_dark_complexion']}
def blemish(q, **k):
    if q == 'age_ladder':
        return cell({'minor': 'unfit_even_whole', 'valid_from': 'two_hairs', 'admitted_at': 'twenty'}, M, '21:17 "a MAN of your seed" — ' + SE + 'Section 3 1: validity vs admission split', [FX.NONE])
    if q == 'future_tense':
        return cell('before_or_after_the_utterance_or_born_so', M, '21:17 "in whom there SHALL BE a blemish" — ' + SE + 'Section 3 2', ['blemish_barred'])
    if q == 'blemish_tokens':
        return cell({'lev_21': 5, 'lev_22': 3}, I, '"blemish" five times in the priest\'s file (%s) and three in the animal\'s (%s)' % (c_mum21, c_mum22), [FX.NONE])
    if q == 'approach_seats':
        return cell({'shall_not_approach': [17, 18, 21, 21], 'shall_not_draw_near': [21, 23], 'shall_not_come': 23}, I,
                    'the approach-verbs %s: "shall not approach" (17, 18), "shall not draw near" (21 twice, 23), "shall not come" to the veil (23) — the BLOCK written four times' % (c_approach,), ['blemish_barred'])
    if q == 'service_census':
        return cell({'in_the_ban': ['fats', 'the_handful', 'frankincense', 'incense', 'the_priests_meal_offerings', 'the_libation_meal_offerings', 'pourings', 'mixings', 'wavings', 'presentings', 'scoopings', 'breakings', 'saltings', 'pinchings', 'receivings'], 'liable_only_for': 'service_like_bread'}, M,
                    '21:21 "shall not draw near to offer" — ' + SE + 'Section 3 4; blood by 1:5\'s "shall bring the blood" (3 3)', ['blemish_barred'])
    if q == 'aaron_passing':
        return cell({'aaron_himself': 'included', 'passing_blemish': 'included'}, M, ('21:18 "EVERY man in whom is a blemish" (%s) — ' + SE +
                    'Section 3 5 (Mishnah Bekhorot 7:1: permanent or passing disqualify in man)') % (has('כל', 'איש')(toks('Lev', 21, 18)),), ['blemish_barred'])
    if q == 'heads':
        return cell(HEADS, I, 'the twelve class heads in the ink\'s order at 21:18-20 — blind, lame, charum, sarua (18); broken leg, broken hand (19); giben, dak, tevallul, garav, yalefet, '
                    'meroach ashekh (20)', ['blemish_barred'])
    if q == 'members':
        h = k['head']
        return cell(MEMBERS[h], M, SE + 'Section 3 6-15 — each head amplified by its "or" (Mishnah Bekhorot 7:2-7:6 carry the same members); Onkelos Lev 21:20 rules the testicle '
                    'dispute for R. Yishmael ("crushed") and writes yalefet as the Sifra\'s lichen', ['blemish_barred'])
    if q == 'shared_tokens':
        return cell(['garav', 'yalefet', 'sarua'], I, ('the priest\'s list (21:18-20) and the animal\'s (22:22-24) share EXACTLY three tokens %s — ' + SE +
                    'Section 7 13\'s cross-list transfer runs on the first two by name (garav-garav, yalefet-yalefet), and Onkelos writes both lists with one Aramaic word each') % (c_shared,), [FX.NONE])
    if q == 'other_blemishes':
        return cell('amplified_by_blemish_blemish', M, '21:17 + 21:21 "blemish... blemish" — ' + SE + 'Chapter 3 1 (Mishnah Bekhorot 6:8-9, 7:1, 7:4: the recorded accretions)', ['blemish_barred'])
    if q == 'kushite_class':
        return cell({'in_man': 'unfit', 'in_beast': 'fit', 'members': ['kushite', 'ruddy', 'albino', 'hunchback', 'dwarf', 'deaf', 'fool', 'drunk', 'pure_afflictions']}, M,
                    '21:17 + 21:18 "man... man" — ' + SE + 'Chapter 3 2-4 (Mishnah Bekhorot 7:6 verbatim)', ['blemish_barred'])
    if q == 'beast_unfits_in_man':
        return cell({'it_and_its_young': 'fit', 'terefah': 'fit', 'caesarean': 'fit'}, M, '21:21 "blemish IN HIM" — ' + SE + 'Chapter 3 3-5: the three beast-unfits FIT in man '
                    '(Mishnah Bekhorot 7:7 verbatim); the reverse a-fortiori refused', [FX.NONE])
    if q == 'passed_blemish':
        return cell('fit', M, '21:23 "blemish in him" — ' + SE + 'Chapter 3 6-7: one whose blemish passed is fit, in man as in the beast (Mishnah Eruvin 10:13: the wart cut in the Temple)', ['accepted'])
    if q == 'eats':
        return cell({'most_holy': 'eats', 'holy': 'eats', 'in_the_division': 'takes_a_share'}, I, '21:22 "of the most holy and of the holy he may EAT" — both written (' + SE +
                    'Chapter 3 8-9: the tevul yom takes no share, the blemished does)', ['due_to_priest'])
    if q == 'veil_altar':
        return cell({'veil': 'shall_not_come', 'altar': 'shall_not_draw_near', 'beaten_plates': 'may_enter'}, M, '21:23 both written — ' + SE + 'Chapter 3 10-11: "but" — he enters to make the plates', ['blemish_barred'])
    if q == 'entry_hierarchy':
        return cell(['priests', 'levites', 'israelites', 'impure', 'blemished'], M, SE + 'Chapter 3 11 — the fallback chain for sanctuary labor', [FX.NONE])
    if q == 'served':
        return cell({'service': 'invalid', 'death': ['R._Yehuda_yes_by_profanation_profanation', 'sages_warning_only']}, M, '21:23 "he shall not profane My sanctuaries" — ' + SE +
                    'Chapter 3 11 (Mishnah Terumot 8:1: found blemished — his service invalid)', ['service_profaned'])
    if q == 'transmission':
        return cell(['moses_to_aaron', 'aaron_to_his_sons', 'the_sons_to_israel', 'the_sons_to_each_other'], M, '21:24 the addressee list — ' + SE + 'Chapter 3 12: a warning graph', [FX.NONE])
    if q == 'bald':
        return cell('no_hair_line_ear_to_ear', A, 'Mishnah Bekhorot 7:2 — the bald defined; with a line, fit', ['blemish_barred'])
    if q == 'eye_positions':
        return cell(['both_up', 'both_down', 'one_each', 'sees_room_and_loft', 'sun_hater', 'unmatched', 'the_dripping', 'lashes_fallen_for_appearance'], M,
                    SE + 'Section 3 14 (Mishnah Bekhorot 7:3) — "in his eye"; the fallen lashes a FENCE ("for the appearance to the eye")', ['blemish_barred'])
    if q == 'proportions':
        return cell(['eyes_as_a_calf_or_a_goose', 'body_vs_limbs', 'nose_vs_limbs', 'small_ears', 'sponge_ears'], A, 'Mishnah Bekhorot 7:4 — the recorded additions', ['blemish_barred'])
    if q == 'fingers':
        j = k['joined_to']
        if j == 'joint':
            return cell('fit', M, '21:19 "broken hand" — ' + SE + 'Section 3 11: joined to the joint fit (Mishnah Bekhorot 7:6)', ['accepted'])
        return cell('unfit', M, SE + 'Section 3 11: below the joint unfit; cut apart — fit', ['blemish_barred'])
    if q == 'extra_finger':
        return cell({'cut_with_bone': 'unfit', 'cut_without_bone': 'fit', 'six_and_six': ['R._Yehuda_fit', 'sages_unfit'], 'ambidextrous': ['Rabbi_unfit', 'sages_fit']}, A, 'Mishnah Bekhorot 7:6', ['blemish_barred'])
    if q == 'dorot':
        return cell({'lev_21': [17], 'lev_22': [3], 'lev_24': [3]}, I, '"to their/your generations" once in each file (%s): the blemish ban, the karet, the lamp — three perpetual clauses' % (c_dorot,), [FX.NONE])
    raise ValueError(q)

# ---- F3: THE HOLY THINGS, THE EATERS OF TERUMAH, THE FIFTH (22:1-16) ----
FEEDERS = {'wife': 'eats', 'slave_bought': 'eats', 'slave_born': 'eats', 'slaves_slave': 'eats', 'hebrew_slave': 'no_money_in_him', 'half_slave': 'not_HIS_money',
           'worthless_born': 'eats', 'animal': 'vetch_only', 'dead_priests_household': 'nobody'}
def holy_food(q, **k):
    if q == 'separation':
        return cell('separation_performed_by_onkelos', M, '22:2 וינזרו — ' + SE + 'Section 4 1 (Ezek 14:7, Isa 1:4 the lexical witnesses); Onkelos Lev 22:2 "they shall SEPARATE"', [FX.NONE])
    if q == 'whose_holy_things':
        return cell({'israels': 'liable', 'gentiles': 'not', 'priests_own': 'included'}, M, '22:2 "the holy things of the children of Israel... which they sanctify TO ME" — ' + SE + 'Section 4 1', [FX.NONE])
    if q == 'name_frame':
        return cell([2, 32], I, '"the name of My holiness" at 22:2 and 22:32 (%s) — the chapter FRAMED by the Name; its third Leviticus seat is Molech\'s 20:3' % (sorted(set(c_shem)),), ['name_profaned'])
    if q == 'chillul_import':
        return cell(['time', 'death', 'acceptance_dependence', 'R._Yehuda_karet_by_I_the_LORD'], M, '"profanation"-"profanation" (Lev 19:8; Zevachim 44a:8, 45a:9 — the notar-from-impurity analogy) —  ' + SE + 'Section 4 2: one verbal analogy, three parameters', [FX.NONE])
    if q == 'karet_extension':
        return cell({'from': 'shelamim_only_at_7_20', 'to': 'all_holy_things', 'piggul_a_fortiori': 'refused_by_the_four_way_difference'}, M,
                    '22:3 "who approaches... to the holy things... with his impurity on him — cut off" (ונכרתה) — ' + SE + 'Section 4 5', ['karet_cut_off'])
    if q == 'readiness':
        return cell({'with_permitters': 'after_the_permitters_are_offered', 'without': 'after_vessel_sanctification'}, M, '22:3 "who APPROACHES" = until it is fit to approach — ' + SE + 'Section 4 7 (R. Elazar: is a toucher liable?!)', [FX.NONE])
    if q == 'body_impurity':
        return cell('impurity_of_the_body_not_the_flesh_four_routes', M, '22:3 "HIS impurity on him" — ' + SE + 'Section 4 8', [FX.NONE])
    if q == 'zav_tier':
        return cell(ZAV_TIER3, P, '22:4 "or a ZAV shall not eat of the holy things until he is pure" — the zav\'s tier is the clocks engine\'s: CALLED cold_run_clocks.zav(tier, sightings=3) -> %r; '
                    'count_start -> %r [IMPORT, live call]; the leper the affliction engine\'s output datum' % (ZAV_TIER3, ZAV_START), ['stranger_barred'])
    if q == 'until_pure':
        return cell('sunset', M, ('22:4 "until he is PURE" = 22:7 "the sun sets and he is pure" (purity-purity) — ' + SE + 'Chapter 4 2; "and the sun sets" stands at %s') % (c_sunset,), ['impure_until_evening'])
    if q == 'tithe_tevul_yom':
        return cell({'israelites_tithe': 'as_tevul_yom', 'aaron_and_sons_terumah': 'at_sunset'}, M, SE + 'Chapter 4 1 — the a-fortiori from the tithe', ['stranger_barred'])
    if q == 'measures':
        return cell({'corpse': 'contact_only', 'seed_emitter': 'included', 'toucher_of_semen': 'by_or_a_man', 'swarming_thing': 'included', 'carcass': 'by_or_a_man',
                     'zavim_zavot_niddot_yoldot': 'his_impurity', 'lies_with_a_niddah': 'who_becomes_impure', 'swallows_a_pure_birds_carcass': 'to_him'}, M,
                    '22:4-5 — ' + SE + 'Chapter 4 3-4: THE MEASURES CENSUS mapped onto Lev 5:3\'s tokens', ['stranger_barred'])
    if q == 'touch_not_move':
        return cell('touch_only_heset_excluded', M, '22:6 "a soul that TOUCHES it" — ' + SE + 'Chapter 4 5', [FX.NONE])
    if q == 'mixture_grid':
        return cell('one_in_a_hundred_both_directions', M, '22:6 "shall not eat of the holy" / 22:7 "afterwards he may eat" — ' + SE + 'Chapter 4 5-6, 4 9-10: eight food/drink combinations', [FX.NONE])
    if q == 'whole_body':
        return cell('not_limb_by_limb', M, '22:6 "unless he washes his flesh in water" — ' + SE + 'Chapter 4 7: as sunset is at once, so the immersion', ['immersed'])
    if q == 'two_gates':
        return cell({'sunset': 'gates_terumah', 'atonement_offering': 'does_not'}, M, '22:7 — ' + SE + 'Chapter 4 8 (Mishnah Chagigah 3:3; Berakhot 1:1\'s evening = the priests\' terumah)', ['stranger_barred'])
    if q == 'his_bread':
        return cell('raise_wheat_and_trim_vegetables_as_he_likes_trimmings_holy', M, '22:7 "for it is his BREAD" — ' + SE + 'Chapter 4 11', ['terumah_fed'])
    if q == 'gullet':
        a = k['animal']
        if a == 'bird':
            return cell('defiles_in_the_gullet', M, '22:8 "IN it" — ' + SE + 'Chapter 4 13: the bird carcass', ['impure_until_evening'])
        return cell('does_not_defile_in_the_gullet', M, SE + 'Chapter 4 12: the beast carcass defiles before it is eaten (Lev 17\'s swallow-house)', [FX.NONE])
    if q == 'charge':
        return cell({'warned': 'the_court', 'bear_sin_over': 'the_holy_things_not_the_carcass', 'onkelos': 'receive_upon_it_a_debt'}, M, '22:9 — ' + SE + 'Chapter 4 14; Onkelos Lev 22:9', ['death_by_heaven'])
    if q == 'die_by_it':
        return cell({'deliberate_impure_eater': 'death_by_heaven', 'tithe': 'no', 'pure_eater_of_impure': 'no'}, M, '22:9 "and DIE by it when they profane it" — ' + SE + 'Chapter 4 15', ['death_by_heaven'])
    if q == 'stranger':
        return cell({'who': 'levite_and_israelite_by_EVERY_stranger', 'eating': 'an_olive', 'holy': 'the_border_holy_things_terumah', 'seats': [10, 12, 13]}, M,
                    ('22:10 "and EVERY stranger shall not eat holy" — the stranger at %s; ' + SE + 'Chapter 4 16 (Deut 26:13 verbal analogy)') % (c_zar,), ['stranger_barred'])
    if q == 'toshav_sachir':
        return cell({'toshav': 'acquired_forever_the_pierced_slave', 'sachir': 'acquired_for_years'}, M, '22:10 "the priest\'s RESIDENT and HIRELING" — ' + SE + 'Chapter 4 17; Onkelos "resident", "hireling"', ['stranger_barred'])
    if q == 'uncircumcised':
        return cell(['R._Yishmael_toshav_sachir_from_the_passover', 'R._Akiva_man_man'], M, SE + 'Chapter 4 18 — two routes, one verdict (Mishnah Yevamot 8:1; Shabbat 19:6)', ['stranger_barred'])
    if q == 'household':
        who = k['who']
        return cell(FEEDERS[who], M, '22:11 "when a priest acquires a soul, the purchase of his MONEY, he may eat of it; and one BORN in his house, they may eat of his bread" — ' + SE +
                    'Section 5 1-6: the acquisition of an acquisition eats; "money" excludes the Hebrew slave, "HIS" the half-slave; "in any case" the worthless-born; "they" not the animal; '
                    '"his bread" — the dead feed none (Mishnah Yevamot 7:1-2)', ['terumah_fed'] if FEEDERS[who] == 'eats' else [FX.NONE])
    if q == 'son_feeds_mother':
        return cell('the_son_feeds_the_mother', M, SE + 'Section 5 6 (R. Shimon from "born of his house... THEY shall eat"; Mishnah Yevamot 7:5: the son\'s power greater than the father\'s; Niddah 5:3)', ['terumah_fed'])
    if q == 'daughter_to_stranger':
        return cell({'stranger': 'levite_israelite', 'to_a_man': 'to_one_who_feeds', 'forbidden_union': 'disqualifies_from_terumah', 'she_feeds': 'her_mother'}, M,
                    '22:12 "a priest\'s daughter, when she is to a STRANGER man" — ' + SE + 'Section 5 7-10 (Mishnah Yevamot 6:3, 9:4)', ['stranger_barred'])
    if q == 'terumah_vs_holy':
        return cell({'holy_things': 'some_permitted_to_strangers_piggul_liability', 'terumah': 'never_permitted_no_piggul'}, M, ('22:12 "the TERUMAH of the holy things" (the only terumah noun in the span, %s) — ' + SE + 'Section 6 1') % (c_terumah,), [FX.NONE])
    if q == 'return':
        return cell({'widow_and_divorcee': 'both_written_both_need_no_seed', 'no_seed': 'to_the_seeds_seed', 'unfit_seed': 'counts', 'maidservants_seed': 'not_hers', 'levirate_bound': 'not', 'pregnant': 'not', 'her_fathers_bread': 'terumah'}, M,
                    '22:13 "a widow or divorced, and she has no seed, and she RETURNS to her father\'s house as in her youth" — ' + SE + 'Chapter 5 1-5, Chapter 6 1 (Mishnah Yevamot 9:6 quotes the verse)', ['terumah_fed'])
    if q == 'grandson_high_priest':
        return cell('feeds_his_mother_disqualifies_his_grandmother', M, SE + 'Chapter 5 3 = Mishnah Yevamot 7:6 verbatim', ['terumah_fed'])
    if q == 'eating_table':
        husband, son_alive = k['husband'], k.get('son_alive', True)
        who = husband if son_alive else k.get('after')
        if who == 'priest': return cell('terumah', I, '22:11 / 22:13 — the LAST living feeder decides (Mishnah Yevamot 9:5-6)', ['terumah_fed'])
        if who == 'levite': return cell('tithe', P, 'the Levite\'s tithe is Num 18\'s [IMPORT] (Mishnah Yevamot 9:5-6)', [FX.NONE])
        if who == 'fathers_house': return cell('terumah_returns', I, '22:13 "she returns to her father\'s house" (Mishnah Yevamot 9:6)', ['terumah_fed'])
        return cell('neither', I, '22:12 "to a stranger man — she shall not eat"', ['stranger_barred'])
    if q == 'stage':
        s = k['stage']
        return cell('does_not_eat' if s in ('betrothed', 'pregnant', 'levirate_bound', 'deaf_mute', 'nine_and_a_day') else 'eats', M,
                    '22:11 "acquires" — marriage, not betrothal; ' + SE + 'Chapter 6 1 (the levirate-bound and the pregnant); Mishnah Yevamot 7:4\'s five who disqualify and do not feed, 9:4', ['stranger_barred'] if s != 'married' else ['terumah_fed'])
    if q == 'fetus':
        return cell('disqualifies_does_not_feed', M, '22:11 "BORN in his house" — the unborn is not born: ' + SE + 'Section 5 6 bounded; Mishnah Yevamot 7:3-4 (R. Yosei)', [FX.NONE])
    if q == 'slaves_of_forbidden_wife':
        t = k['type']
        return cell('eat' if t == 'iron_flock' else 'do_not_eat', A, 'Mishnah Yevamot 7:1 — 22:11\'s "HIS money": whose loss decides (the iron-flock slaves are his)', ['terumah_fed'] if t == 'iron_flock' else [FX.NONE])
    if q == 'rapist_seducer_fool':
        return cell({'fit': 'neither_disqualify_nor_feed', 'unfit_to_enter': 'disqualify', 'slave': 'disqualifies_by_intercourse_not_seed', 'mamzer': 'disqualifies_and_feeds'}, M, SE + 'Chapter 5 4-5 = Mishnah Yevamot 7:5', [FX.NONE])
    if q == 'crushed_priest':
        return cell({'he_and_his_slaves': 'eat', 'his_wives': 'do_not_eat', 'wife_from_before': 'eats'}, A, 'Mishnah Yevamot 8:1 — Deut 23:2\'s union forbidden [IMPORT], so she is "to a man" who does not feed (' + SE + 'Section 5 7)', ['stranger_barred'])
    if q == 'eunuch_priest':
        return cell({'sun_eunuch': 'feeds_his_wife', 'androgynos': 'R._Yosei_R._Shimon_feeds', 'tumtum_torn_male': 'R._Yehuda_as_a_eunuch'}, A, 'Mishnah Yevamot 8:6 — 22:11\'s feeder is the priest as such', ['terumah_fed'])
    if q == 'fifth_algebra':
        return cell(FIFTH_CALL, P, ('22:14 "he shall add its FIFTH to it" — the added quarter is the Lev 5 engine\'s own algebra (5:16\'s clause): CALLED cold_run_vayikra5.sacrilege(meilah, value=100) -> %r '
                    '[IMPORT, live call]; ' + SE + 'Chapter 6 4: it and its fifth = five') % (FIFTH_CALL,), ['adds_fifth'])
    if q == 'fifth_spelling':
        return cell([('Lev', 22, 14), ('Lev', 27, 31)], I, 'this spelling of "its fifth" (%s) — here and the tithe\'s redemption; the guilt offering\'s 5:16 spells it with the yod' % (c_fifth,), [FX.NONE])
    if q == 'error_gate':
        d = k['deliberate']
        if d: return cell({'principal': 'pays', 'fifth': 'no', 'payment': 'common_priest_may_forgive', 'death': 'by_heaven_if_impure_eater'}, M, ('22:14 "IN ERROR" — the deliberate outside the fifth (' + SE + 'Chapter 6 4; Mishnah Terumot 7:1); the deliberate sacrilege CALLED -> %r') % (FIFTH_DELIB,), ['pays'])
        return cell({'principal': 'pays', 'fifth': 'adds', 'payment': 'becomes_terumah_priest_cannot_forgive'}, M, '22:14 "eats holy in error... add its fifth... give the priest the holy" (Mishnah Terumot 6:1, 7:4); the payment sanctified by the GIVING (' + SE + 'Chapter 6 7, R. Meir)', ['adds_fifth', 'pays'])
    if q == 'fifth_gates':
        return cell({'non_strangers': 'exempt', 'minor': 'exempt_nine_and_a_day_a_man', 'less_than_olive': 'exempt', 'terumah_abroad': 'exempt', 'eater_drinker_anointer': 'all_liable'}, M,
                    ('22:14 "a MAN who eats" (%s) — ' + SE + 'Chapter 6 2-3, 6 8 (Mishnah Terumot 7:2-3, 6:1)') % (toks('Lev', 22, 14)[:3] == ['ואיש', 'כי', 'יאכל'],), ['adds_fifth'])
    if q == 'payment_material':
        return cell({'R._Meir': 'fit_to_become_holy_not_gleanings_corner_ownerless', 'sages': 'from_all'}, M, '22:14 "give the priest THE HOLY" — ' + SE + 'Chapter 6 5 = Mishnah Terumot 6:5', ['pays'])
    if q == 'kind_for_kind':
        return cell({'R._Akiva': 'kind_for_kind_wait_for_the_cucumbers', 'R._Eliezer': 'any_kind_better_for_worse'}, M, SE + 'Chapter 6 6 = Mishnah Terumot 6:6: "the holy" — the class or the instance', ['pays'])
    if q == 'two_payees':
        return cell({'principal': 'to_the_owner', 'fifth': 'to_any_priest'}, A, 'Mishnah Terumot 6:2 — "give the priest" names the class', ['pays'])
    if q == 'workers':
        return cell({'R._Meir': 'he_the_principal_they_the_fifth', 'sages': 'they_both_he_their_meal'}, A, 'Mishnah Terumot 6:3', ['adds_fifth'])
    if q == 'thief':
        return cell({'not_eaten': 'double_of_the_terumahs_value', 'eaten': 'two_principals_and_a_fifth', 'consecrated_terumah_eaten': 'two_fifths_and_a_principal_no_double'}, A,
                    'Mishnah Terumot 6:4 — 22:14\'s fifth stacked on Exod 22:3\'s double [IMPORT: the mishpatim engine]', ['adds_fifth', 'pays_double'])
    if q == 'daughter_who_ate':
        return cell({'R._Meir': {'to_israelite': 'principal_no_fifth_burning', 'to_disqualified': 'principal_and_fifth_strangling'}, 'sages': 'both_principal_no_fifth_burning'}, A,
                    'Mishnah Terumot 7:2 — 22:12 (no fifth for the non-stranger) with 21:9 (burning)', ['burned_by_court'])
    if q == 'learns':
        return cell({'wife_or_slave_told': ['R._Eliezer_principal_and_fifth', 'R._Yehoshua_exempt'], 'chalal_serving': ['R._Eliezer_invalid', 'R._Yehoshua_valid'], 'found_blemished': 'service_invalid'}, A,
                    'Mishnah Terumot 8:1 — three of this span\'s machines in one row (22:12-13, 21:15, 21:17-23)', ['service_profaned'])
    if q == 'in_the_mouth':
        return cell({'told_now_impure': ['R._Eliezer_swallow', 'R._Yehoshua_spit'], 'was_impure_or_tevel_or_a_bug': 'spit_out'}, A, 'Mishnah Terumot 8:2 — 22:6-7 at the mouth\'s threshold', ['stranger_barred'])
    if q == 'warning_object':
        return cell('eating_not_defiling', M, 'Mishnah Terumot 8:11 (R. Yehoshua: "not the terumah I am warned against DEFILING but against EATING") = ' + SE + 'Chapter 6 10: the sower and the defiler excluded from "when they eat"', [FX.NONE])
    if q == 'profaners':
        return cell({'raised_not_untithed': True, 'death_even_on_tevel': True, 'sower_and_defiler': 'excluded', 'onkelos': 'in_impurity_inserted'}, M,
                    '22:15-16 "which they RAISE... when they eat their holy things" — ' + SE + 'Chapter 6 9-10; Onkelos Lev 22:16', ['death_by_heaven'])
    if q == 'asham_homograph':
        return cell('the_noun_guilt_not_the_offering', I, '22:16 "the iniquity of GUILT" — the span\'s only asham token is the noun (dependency_dispositions: FALSE to tzav); the fifth\'s engine is called at 22:14 instead', [FX.NONE])
    if q == 'eat_count':
        return cell(14, I, 'the eating verb fourteen times in Lev 22 (%d) — the chapter is an eaters\' file' % c_eat22, [FX.NONE])
    raise ValueError(q)

# ---- F4: THE ACCEPTABLE ANIMAL (22:17-33) ----
BEAST_HEADS = ['blind', 'broken', 'charutz', 'wart', 'garav', 'yalefet']
ALTAR_FORBIDDEN = ['copulator', 'copulated', 'set_aside', 'worshipped', 'hire', 'price', 'hybrid', 'terefah', 'caesarean']
def acceptable(q, **k):
    if q == 'vow_class':
        return cell({'gentiles': 'vow_and_offer_freely', 'widened_by_all': ['shelamim', 'todah', 'birds', 'meal_offerings', 'wine', 'frankincense', 'wood'], 'nazirite': 'excluded', 'public': 'not_compelled'}, M,
                    ('22:18 "MAN, MAN... of the house of Israel and of the convert in Israel... for all their vows and all their freewill offerings... for a burnt offering" (%s) — ' + SE +
                    'Section 7 1-2 (Mishnah Shekalim 1:5: the gentile\'s shekels not accepted, his vows accepted)') % (c_ish_ish[0],), ['accepted'])
    if q == 'whole_male':
        return cell({'beasts': 'whole_and_male', 'birds': 'not_whole_not_male_but_not_the_maimed'}, M, ('22:19 "whole, male, in cattle, in sheep, in goats" (%s) — ' + SE +
                    'Section 7 2: a bird with a dried wing, a gouged eye, a cut leg barred by "from the bird" (Lev 1:14); Mishnah Temurah 6:4\'s premise (no blemish disqualifies the bird)') % (c_tamim,), ['accepted'])
    if q == 'olah_rite':
        return cell(OLAH_DISP, P, '22:18 "for a BURNT OFFERING" — the whole male enters Lev 1\'s rite: CALLED cold_run_offerings.dispatch(olah:flock) -> disposition %r, place %r [IMPORT, live call]' % (OLAH_DISP, OLAH_PLACE), ['accepted'])
    if q == 'shelamim_window':
        return cell(SHEL_WINDOW, P, '22:21 "a sacrifice of PEACE OFFERINGS" — its window is the offering engine\'s: CALLED cold_run_offerings.dispatch(shelamim) -> %r; the todah\'s %r (22:29-30)' % (SHEL_WINDOW, TODAH_WINDOW), ['eating_window'])
    if q == 'acceptance_seats':
        return cell([19, 20, 21, 23, 25, 27, 29], I, 'the acceptance root at seven seats of the chapter (%s; 22:24\'s "your land" a homograph): for-your-acceptance, not-for-acceptance, accepted, '
                    'not-accepted, not-accepted-for-you, accepted, for-your-acceptance' % (c_ratzon,), ['not_accepted'])
    if q == 'passing_blemish':
        return cell('included', M, '22:20 "ALL in which is a blemish" — ' + SE + 'Section 7 3 (Mishnah Zevachim 9:3: R. Akiva\'s narrower arm)', ['not_accepted'])
    if q == 'two_jobs':
        return cell({'22:20': 'bal_takdish_consecrating', '22:22': 'bal_tishchat_slaughtering', '22:24': 'bal_tekabel_receiving_R._Yosei_b._R._Yehuda'}, M,
                    '"you shall not offer" at 22:20, 22:22, 22:24 — ' + SE + 'Section 7 4, Chapter 7 1, 7 10: one verb, three jobs by position', ['not_accepted'])
    if q == 'five_count':
        return cell({'sages': 5, 'R._Yosei_b._R._Yehuda': 6, 'acts': ['consecrate', 'slaughter', 'throw', 'burn_fat', 'burn_part', 'receive']}, M, SE + 'Section 7 5 — the five-count on the blemished consecrated', ['lashes'])
    if q == 'individual_public':
        return cell({'individual': 'freewill_shelamim', 'partners': 'included_by_the_vav', 'public': 'excluded'}, M, '22:21 "and a MAN who offers" — ' + SE + 'Section 7 6-7', [FX.NONE])
    if q == 'class_sweep':
        return cell(['burnt_offering', 'todah', 'yoledet_and_nazirite', 'sin_and_guilt', 'tithe', 'offspring_and_substitutes'], M, ('22:21 "shelamim... to set apart a vow or freewill, in cattle or in flock" (the vow tokens %s; לפלא at %s) — ' + SE + 'Section 7 8; Onkelos "to SPECIFY a vow"') % (c_vows, c_pele), ['not_accepted'])
    if q == 'positive_negative':
        return cell({'whole_for_acceptance': 'positive', 'no_blemish_in_it': 'negative', 'fell_and_broke': 'no_transgression'}, M, '22:21 — ' + SE + 'Section 7 9: "do not PUT a blemish in it"', ['lashes'])
    if q == 'blood_rush':
        return cell({'R._Yehuda': 'no_bloodletting', 'sages': 'let_blood_no_blemish', 'R._Shimon': 'even_the_blemish_if_it_saves'}, M, SE + 'Section 7 10 — the firstling with a blood rush', [FX.NONE])
    if q == 'beast_heads':
        return cell(BEAST_HEADS, I, 'the six class heads of 22:22 in the ink\'s order: blind, broken, charutz, wart, garav, yalefet', ['not_accepted'])
    if q == 'beast_members':
        h = k['head']
        MB = {'blind': ['both_or_one'], 'broken': ['the_tail_not_a_rib', 'visible_non_healing'], 'charutz': ['eyelid_pierced_notched_split', 'lip_likewise', 'outer_teeth_notched_inner_uprooted', 'not_from_the_molars_inward'],
              'wart': ['in_the_eye_R._Chanina'], 'garav': ['the_dry_scab_the_curable_form_no_slaughter'], 'yalefet': ['the_lichen_the_curable_form_no_slaughter']}
        return cell(MB[h], M, SE + 'Section 7 11-12 (Mishnah Bekhorot 6:1-6:4, 6:10, 6:12); Onkelos Lev 22:22 "SPLIT" for charutz', ['not_accepted'])
    if q == 'cross_list':
        return cell({'to_the_beast': ['dak', 'tevallul'], 'to_the_man': ['wart'], 'by': ['garav_garav', 'yalefet_yalefet']}, M, (SE + 'Section 7 13 — two verbal analogies unify the two tables; the tokens shared exactly: %s') % (c_shared,), [FX.NONE])
    if q == 'worked_with':
        return cell('permitted', M, '22:22 "THESE you shall not offer" — ' + SE + 'Chapter 7 2-3: these no, one worked with yes (the heifer a-fortiori refused)', ['accepted'])
    if q == 'four_tokens':
        return cell({'a_fire_offering': 'the_fats', 'of_them': 'even_part', 'on_the_altar': 'the_blood', 'to_the_LORD': 'the_dispatched_goat'}, M, '22:22 — ' + SE + 'Chapter 7 4 (Mishnah Zevachim 8:5 the limb, 8:8 the blood)', ['not_accepted'])
    if q == 'blemished_limb':
        return cell({'R._Eliezer': 'if_one_head_offered_all_heads', 'sages': 'to_the_burning_place'}, A, 'Mishnah Zevachim 8:5 — "of them, even part"', ['not_accepted'])
    if q == 'blemished_blood':
        return cell('poured_to_the_channel', A, 'Mishnah Zevachim 8:8 — "on the altar" = the blood', ['not_accepted'])
    if q == 'sarua_kalut':
        return cell({'sarua': 'dislocated_hip', 'kalut': 'hoof_like_a_horse_or_donkey', 'onkelos': 'extra_and_lacking'}, M, '22:23 (sarua shared with 21:18) — ' + SE + 'Chapter 7 6; Onkelos Lev 22:23 a recorded fork (Mishnah Bekhorot 6:7: five legs or three; kalut like a donkey\'s)', ['not_accepted'])
    if q == 'upkeep':
        return cell({'freewill_or_vow': 'temple_upkeep', 'the_altar': 'not_accepted', 'whole_animal_for_upkeep': ['positive_transgression', 'R._Yehuda_negative_too']}, M,
                    '22:23 "a freewill you may make IT, and for a vow it shall not be accepted" — ' + SE + 'Chapter 7 6-8 (Mishnah Shekalim 4:8)', ['consecrated'])
    if q == 'castration':
        return cell({'anatomies': ['R._Yehuda_testicles', 'R._Eliezer_member', 'R._Yosei_two_and_two'], 'do_not_do': 'not_only_offer', 'birds': 'included', 'abroad': 'included', 'humans': 'by_revocalization_and_in_you', 'females': ['included', 'R._Yehuda_not']}, M,
                    '22:24 "crushed, pounded, torn, cut... and in your land you shall not DO" — ' + SE + 'Chapter 7 9, 7 11-12 (ben Chakinai: ובארצכם read ובכם, M-16); Mishnah Yevamot 8:2 the human\'s crushed testicle "even one"', ['lashes'])
    if q == 'no_shekels':
        return cell({'shekels': 'not_accepted', 'vows': 'accepted', 'blemished_from_gentiles': 'not_accepted'}, M, ('22:25 "from the hand of a FOREIGNER you shall not offer the bread of your God of all these" (%s) — ' + SE + 'Chapter 7 12 = Mishnah Shekalim 1:5') % (c_nekhar,), ['not_accepted'])
    if q == 'corruption':
        return cell(ALTAR_FORBIDDEN, M, '22:25 "their CORRUPTION is in them, a blemish in them" — the class beyond bodily blemish: Mishnah Temurah 6:1\'s nine (the hybrid and the Caesarean from ' + SE +
                    'Section 8 3\'s "ox or sheep... when born", the terefah by the tithe transfer, the copulator and the worshipped the sanctions engine\'s beasts [IMPORT], the hire and price Deut 23:19 [IMPORT])', ['not_accepted'])
    if q == 'any_amount':
        return cell('forbid_in_any_amount', A, 'Mishnah Temurah 6:1 — no ratio nullifies (Zevachim 8:1: even one in a myriad)', ['not_accepted'])
    if q == 'offspring':
        return cell({'offspring': 'permitted', 'terefahs_offspring': ['R._Eliezer_not', 'sages_offered'], 'holy_become_terefah': 'not_redeemed'}, A, 'Mishnah Temurah 6:5 — the corruption is IN THEM, not in their seed', ['accepted'])
    if q == 'descends':
        return cell({'sages': 'descends', 'R._Akiva': 'the_blemished_stays'}, A, 'Mishnah Zevachim 9:3 — not disqualified IN the holy: the blemished never accepted, so never received', ['not_accepted'])
    if q == 'not_a_human':
        return cell('an_ox_when_born_not_a_human', M, '22:27 "an ox... when it is BORN" — ' + SE + 'Section 8 1-2', [FX.NONE])
    if q == 'birth_list':
        return cell({'hybrid': 'ox_or_sheep', 'look_alike': 'or_goat', 'caesarean': 'when_born', 'under_age': 'seven_days', 'orphan': 'under_its_mother', 'tithe': 'all_these_by_under_under'}, M,
                    '22:27 — ' + SE + 'Section 8 3 (R. Yishmael b. R. Yochanan b. Beroka: "under"-"under" of Lev 27:32 carries the list to the tithe and the terefah back)', ['eighth_day_fit'])
    if q == 'one_hour':
        return cell('alive_with_the_mother_one_hour_suffices', M, ('"UNDER its mother" here vs "WITH its mother" at Exod 22:29 (%s) — ' + SE + 'Section 8 4 (R. Yosei HaGelili)') % (c_under,), ['eighth_day_fit'])
    if q == 'eighth_day_by_call':
        return cell(FIRSTLING_8, P, "Exod 22:29's firstling — CALLED cold_run_ordinances.firstling(eighth_and_onward) -> %r [IMPORT, live call — the OWED of sitting L5 closed at E1, 2026-09-06]: 'on the eighth day you shall give it to Me' read with 'from the eighth day and onward' here by its-mother/its-mother (Sifra Emor Section 8 5); 'WITH its mother' there against 'UNDER its mother' here, each phrase a Tanakh hapax" % (FIRSTLING_8,), ['eighth_day_fit'])
    if q == 'eighth_day':
        return cell({'here': 'from_the_eighth_day_onward', 'firstling_exod_22_29': 'on_the_eighth_day', 'join': 'both_by_its_mother_its_mother'}, M,
                    ('22:27 "and from the day, the eighth, and onward" — "and from the day" a HAPAX (%s); ' + SE + 'Section 8 5: each seat could exclude the other\'s reading, the analogy carries both; '
                    'the firstling\'s seat compiled at E1 (cold_run_ordinances.firstling) — fetched by live call in the next cell') % (c_umiyom,), ['eighth_day_fit'])
    if q == 'accepted_for':
        return cell({'the_fire': 'accepted', 'upkeep': 'by_for_an_offering', 'dispatched_goat': 'under_age_barred'}, M, '22:27 "accepted as an offering, a fire offering to the LORD" — ' + SE + 'Section 8 6', ['accepted'])
    if q == 'under_age_outside':
        return cell({'blemished_outside': 'exempt', 'under_age_outside': ['exempt', 'R._Shimon_a_prohibition_without_karet']}, A, 'Mishnah Zevachim 14:2 — 22:27\'s timer against Lev 17\'s outside-slaughter', ['exempt'])
    if q == 'not_wild_not_bird':
        return cell({'wild': 'excluded_by_ox', 'bird': 'excluded_by_sheep', 'either_one': 'or_sheep'}, M, '22:28 "an OX or a SHEEP" — ' + SE + 'Section 8 8-10', [FX.NONE])
    if q == 'female_rule':
        return cell({'males': 'not_as_females', 'by': 'its_young_that_follows_it', 'onkelos': 'a_cow_or_a_ewe_HER_and_HER_young'}, M, '22:28 "it and its YOUNG" — ' + SE + 'Chapter 8 1; Onkelos Lev 22:28 feminizes every noun and pronoun', ['same_day_slaughter_barred'])
    if q == 'it_and_its_mother':
        return cell('two_by_the_plural_you_shall_not_slaughter', M, SE + 'Chapter 8 2', ['same_day_slaughter_barred'])
    if q == 'order_cases':
        seq = k['seq']
        if seq == 'cow_then_two_young': return cell(80, M, SE + 'Chapter 8 3 = Mishnah Chullin 5:3: the mother then five — each one', ['lashes'])
        if seq == 'two_young_then_cow': return cell(40, M, SE + 'Chapter 8 3: five siblings then the mother — ONE liability', ['lashes'])
        if seq == 'her_daughter_granddaughter': return cell(80, M, SE + 'Chapter 8 3-4 = Mishnah Chullin 5:3', ['lashes'])
        if seq == 'her_granddaughter_then_daughter': return cell([40, 'Sumchos_80'], M, SE + 'Chapter 8 3: the middle one last — forty; Sumchos in R. Meir\'s name eighty', ['lashes'])
    if q == 'cells':
        kind, place, order = k['kind'], k['place'], k['order']
        second = 'flogged'
        if kind == 'common' and place == 'outside': first = 'valid_exempt'; validity = 'both_valid'
        elif kind == 'consecrated' and place == 'outside': first = 'karet'; validity = 'both_invalid_both_flogged'
        elif kind == 'common' and place == 'inside': first = 'invalid_exempt'; validity = 'both_invalid'
        else: first = 'valid_exempt'; validity = 'second_invalid'
        return cell({'first': first, 'second': second, 'validity': validity}, I, '22:28 "you shall not slaughter" — the SECOND slaughter completes the pair and is the one flogged; the karet of consecrated outside is Lev 17:4\'s '
                    '[IMPORT: cold_run_sanctions.outside], the common inside invalid by Deut 12 [IMPORT], the second consecrated disqualified by ' + SE + 'Section 8 7 (Mishnah Chullin 5:1-2)', ['lashes', 'same_day_slaughter_barred'])
    if q == 'everywhere':
        return cell({'land': 'yes', 'abroad': 'yes', 'with_the_house': 'yes', 'without': 'yes', 'common': 'yes', 'consecrated': 'yes'}, I, '22:28 carries no "in the land" clause (contrast 22:24) — Mishnah Chullin 5:1', ['same_day_slaughter_barred'])
    if q == 'slaughter_verb':
        return cell({'became_a_carcass': 'exempt', 'stabber_tearer': 'exempt', 'for_gentiles_or_dogs': 'included', 'terefah_idolatry_red_cow_stoned_ox_heifer': ['R._Meir_liable', 'R._Shimon_exempt']}, M, '22:28 "you shall not SLAUGHTER" — ' + SE + 'Chapter 8 5-6 (Mishnah Chullin 5:3)', ['lashes'])
    if q == 'four_periods':
        return cell({'periods': ['eve_of_the_last_day_of_sukkot', 'eve_of_the_first_of_passover', 'eve_of_atzeret', 'eve_of_rosh_hashanah', 'R._Yosei_HaGelili_eve_of_yom_kippur_in_the_galilee'], 'seller': 'must_inform', 'R._Yehuda': 'only_without_an_interval', 'groom_and_bride': 'agreed'}, M,
                    SE + 'Chapter 8 8 = Mishnah Chullin 5:3', ['forewarned'])
    if q == 'compelled_butcher':
        return cell({'compelled': True, 'died_in_the_periods': 'the_buyers_loss', 'rest_of_the_year': 'the_sellers'}, M, SE + 'Chapter 8 9 = Mishnah Chullin 5:4', [FX.NONE])
    if q == 'day_boundary':
        return cell('the_day_follows_the_night', M, ('22:28 "on ONE DAY" — the Torah\'s only seat of the phrase (%s); ben Zoma reaches Gen 1:5\'s "one day" by verbal analogy (' + SE + 'Chapter 8 9 = Mishnah Chullin 5:5): the civil day imported into a chapter whose offerings run night-after-day') % (c_one_day,), ['same_day_slaughter_barred'])
    if q == 'reassignment':
        return cell({'eating_clause': 'redundant_for_eating_Lev_7_15', 'reassigned_to': 'slaughter_on_condition_of_eating_within_the_day', 'scope': 'all_one_day_offerings'}, M,
                    ('22:29-30 "on that day it shall be eaten, you shall not leave over until morning" (the leftover token shared with Exod 12:10: %s) — ' + SE + 'Chapter 9 1-2 (M-18)') % (c_leftover,), ['eating_window'])
    if q == 'todah_window':
        return cell(TODAH_WINDOW, P, '22:30 — the thanksgiving\'s window is the offering engine\'s: CALLED cold_run_offerings.dispatch(todah_and_nazir_ram) -> %r' % (TODAH_WINDOW,), ['eating_window'])
    if q == 'keep_and_do':
        return cell({'keep': 'mishnah', 'do': 'deed', 'not_in_mishnah': 'not_in_deed'}, M, '22:31 — ' + SE + 'Chapter 9 3: the canon channel\'s fifth seat', [FX.NONE])
    if q == 'sanctify_name':
        return cell({'hand_yourself_over': True, 'among': 'the_many', 'on_condition_of_a_miracle': 'none'}, M, ('22:32 "and I shall be SANCTIFIED among the children of Israel" — the Torah\'s only seat of the verb (%s); ' + SE + 'Chapter 9 4-5') % (c_venikdashti,), ['name_profaned'])
    if q == 'exodus_condition':
        return cell('on_condition_that_you_hand_yourselves_over', M, '22:33 — ' + SE + 'Chapter 9 6', [FX.NONE])
    if q == 'ani_seats':
        return cell({'lev_21': [8, 12, 15, 23], 'lev_22': [2, 3, 8, 9, 16, 30, 31, 32, 33]}, I, '"I am the LORD" at %s — the sanctifier formula at %s' % (c_ani, c_mekadesh), [FX.NONE])
    if q == 'firstling_table':
        return cell({'slaughter_on': 'the_permanent_blemishes', 'not_on': 'the_passing_the_old_the_sick_the_foul_the_sinned_with_the_killer_the_doubtful_sex', 'disqualified_consecrated': 'redeemed_on_the_same'}, A,
                    'Mishnah Bekhorot 6:11-12 — the table\'s closing rule: one list serves the firstling (Deut 15:21 [IMPORT]) and Lev 27\'s redemption', ['not_accepted'])
    if q == 'cataract_timer':
        return cell({'permanent_cataract': 'eighty_days', 'R._Chanina': 'examined_three_times', 'permanent_water': 'dry_after_moist'}, D, 'Mishnah Bekhorot 6:3 — PERMANENCE as a timer with a data threshold', [FX.NONE])
    if q == 'ear':
        return cell({'notched_from_the_cartilage': 'blemish', 'from_the_skin': 'not', 'pierced_a_vetch': 'blemish', 'dried': 'no_drop_of_blood'}, D, 'Mishnah Bekhorot 6:1 — the thresholds the data channel under 22:22\'s "charutz"', ['not_accepted'])
    if q == 'testicles':
        return cell({'none_or_one': 'blemish', 'R._Yishmael': 'two_sacs_two', 'R._Akiva': 'press_it', 'case': ['R._Akiva_permitted', 'R._Yochanan_b._Nuri_forbade']}, A, 'Mishnah Bekhorot 6:6 — 22:24 in the testicles', ['not_accepted'])
    if q == 'accretion':
        return cell({'ila_at_yavneh': 'agreed', 'his_three_more': 'the_later_court_accepted', 'jaw_and_ear_and_tail': 'ruled_case_by_case'}, A, 'Mishnah Bekhorot 6:8-9 — the recorded accretion by named courts ("blemish... blemish" amplifies, ' + SE + 'Chapter 3 1)', ['not_accepted'])
    raise ValueError(q)

# ---- F5: THE LAMP AND THE TABLE (24:1-9) ----
def lamp_table(q, **k):
    if q == 'restatement':
        return cell({'shared_tail': 13, 'of': 14, 'opening_verb': 'command_for_and_you_shall_command'}, I, 'Lev 24:2 restates Exod 27:20 TOKEN FOR TOKEN from "the children of Israel" on (%s) — the spec\'s lamp clause '
                    'returned inside Leviticus; "beaten" at %s' % (c_restate, c_katit), ['lamp_arranged'])
    if q == 'command':
        return cell({'command': 'urging_now_and_for_generations', 'R._Shimon': 'where_there_is_monetary_loss', 'take_to_you': 'you_the_treasurer'}, M, '24:2 "COMMAND... take TO YOU" — ' + SE + 'Section 13 1', ['lamp_arranged'])
    if q == 'oil':
        return cell({'olive': 'not_sesame_nut_radish', 'three_olives': ['treetop', 'roof', 'pressed_and_dried'], 'three_flows': ['crushed_in_the_basket', 'under_the_beam', 'ground_again'], 'for_the_menorah': 'the_first_of_each'}, M,
                    '24:2 "olive oil, pure, beaten" — ' + SE + 'Section 13 1-3 = Mishnah Menachot 8:4', ['lamp_arranged'])
    if q == 'nine_grades':
        return cell(['1of1', '2of1=1of2', '3of1=2of2=1of3', '3of2=2of3', '3of3'], M, SE + 'Section 13 5 = Mishnah Menachot 8:5 — a total order over the nine flows', [FX.NONE])
    if q == 'beaten_scope':
        return cell({'for_the_light': 'required', 'meal_offerings': OIL_GRADE}, P, ('24:2 "beaten FOR THE LIGHT" — ' + SE + 'Section 13 6 (Exod 29:40: beaten oil valid for the meal offerings): the meal-offering engine\'s own '
                    'grade cell CALLED cold_run_minchah.oil_grade -> %r [IMPORT, live call]') % (OIL_GRADE,), ['lamp_arranged'])
    if q == 'R_Yehuda_method':
        return cell(['crushed_in_a_mortar_not_a_mill', 'stones_not_the_beam', 'around_the_basket_not_in_it'], M, SE + 'Section 13 4 = Mishnah Menachot 8:4', [FX.NONE])
    if q == 'pure_tokens':
        return cell({'oil_and_frankincense': [2, 7], 'menorah_and_table': [4, 6]}, I, ('PURE written four times in nine verses (%s): the oil, the frankincense; the menorah, the table — ' + SE + 'Section 13 6 (clean), 13 12 (on the menorah\'s own purity: no props), Chapter 18 4 (the table\'s: the props do not lift the bread)') % (c_pure,), ['lamp_arranged'])
    if q == 'western_lamp':
        return cell({'flame': 'rises_on_its_own', 'western': 'always_burning_begin_from_it_end_at_it', 'found_out': ['Sifra_relight_from_the_outer_altar', 'Tamid_from_the_burning_lamps']}, M,
                    '24:2 "to raise a lamp continually" — ' + SE + 'Section 13 7; Mishnah Tamid 3:9 (found the two eastern lamps burning — clear the rest and leave them; found out — light them from the burning ones): a recorded fork on the relighting source', ['lamp_arranged'])
    if q == 'continually':
        return cell({'seats': [2, 3, 4, 8], 'means': ['even_on_the_sabbath', 'even_in_impurity']}, I, ('"continually" four times in 24:1-9 (%s) — ' + SE + 'Section 13 7, 13 11-12') % (c_tamid[0],), ['lamp_arranged'])
    if q == 'position':
        return cell('nearer_the_veil_than_the_entrance', M, '24:3 "outside the veil... in the tent" — ' + SE + 'Section 13 8: Exod 40:24 left it open, fixed by cross-reference', [FX.NONE])
    if q == 'one_priest':
        return cell({'exod_27_21': 'aaron_and_his_sons', 'lev_24_3': 'aaron', 'staffing': 'one_priest_arranges_seven_lamps'}, I, ('"and his sons" at Exod 27:21, DROPPED at Lev 24:3 (%s) — ' + SE + 'Section 13 10: "to raise a LAMP" singular, "Aaron... arrange" — one priest') % (c_sons,), ['lamp_arranged'])
    if q == 'evening_to_morning':
        return cell({'measure': 'enough_to_burn_evening_to_morning', 'exclusive': 'no_other_service_in_that_interval'}, M, '24:3 — ' + SE + 'Section 13 11', ['lamp_arranged'])
    if q == 'tending':
        found = k['found']
        if found == 'two_eastern_burning': return cell('clear_the_rest_leave_them_burning', A, 'Mishnah Tamid 3:9', ['lamp_arranged'])
        return cell('clear_and_light_from_the_burning_ones_then_the_rest', A, 'Mishnah Tamid 3:9 (the Sifra: from the outer altar)', ['lamp_arranged'])
    if q == 'wheat_bought':
        return cell({'wheat': 'may_be_bought_for_this', 'other_meal_offerings': 'not_as_wheat'}, M, '24:5 "take fine flour and bake IT" — ' + SE + 'Chapter 18 1', ['bread_set_weekly'])
    if q == 'loaves':
        return cell({'count': 12, 'each': 'two_tenths', 'equal': True, 'kneaded': 'one_by_one', 'baked': 'two_at_a_time', 'molds': 3}, I,
                    ('24:5 "TWELVE loaves, two tenths the one loaf" (%s) — ' + SE + 'Chapter 18 2 = Mishnah Menachot 11:1') % (c_table[:4],), ['bread_set_weekly'])
    if q == 'arrangement':
        return cell({'rows': 2, 'per_row': 6, 'pinned_by': 'three_verses'}, I, ('24:6 "two rows, six the row" with 24:5\'s twelve (%s) — ' + SE + 'Chapter 18 3: eight-and-four? "six the row"; six-six-six? "twelve"; four-four-four? "two rows, six" — "until three verses say it we have not heard"') % (c_table[4:7],), ['bread_set_weekly'])
    if q == 'props_reeds':
        return cell({'golden_props': 4, 'reeds': 28, 'per_row': 14, 'lie': 'lengthwise_with_the_house', 'except': 'the_ark'}, M, '24:6 "on the PURE table" — ' + SE + 'Chapter 18 4, 18 8 = Mishnah Menachot 11:6', ['bread_set_weekly'])
    if q == 'both_rows':
        return cell('both_rows_by_row_row', M, '24:7 "on THE row" — ' + SE + 'Chapter 18 5', ['bread_set_weekly'])
    if q == 'frankincense':
        return cell({'pure': 'clear', 'status': 'an_obligation_to_the_bread_indispensable_renders_piggul', 'where': 'two_dishes_with_rims_not_on_the_bread', 'oil': 'none'}, M,
                    '24:7 "pure frankincense on the row, for the bread, for a memorial" — ' + SE + 'Chapter 18 6; Mishnah Menachot 5:3 (frankincense without oil), 3:6 (the rows and the dishes block each other)', ['azkarah_to_fire'])
    if q == 'dishes_place':
        return cell({'sages': 'ON_the_row', 'Abba_Shaul': 'BESIDE_by_Num_2_20'}, A, 'Mishnah Menachot 11:5 — 24:7\'s preposition disputed by a Numbers usage', [FX.NONE])
    if q == 'memorial':
        return cell(FRANK_Q, P, ('24:7 "for a MEMORIAL" — the memorial noun\'s six Leviticus seats %s are the meal offering\'s five and this one: the quantity is the meal-offering engine\'s fistful, CALLED cold_run_minchah.frankincense_quantity -> %r; ' + SE +
                    'Chapter 18 7 (R. Shimon: memorial-memorial, Lev 5:12 — a full handful, one per row)') % (c_azkarah, FRANK_Q), ['azkarah_to_fire'])
    if q == 'not_the_fires':
        return cell(SHOW_REM, P, '24:9 "it shall be for Aaron and his sons" — the loaves themselves never go to the altar: CALLED cold_run_minchah.remainder(showbread) -> %r (Mishnah Zevachim 9:5: the showbread descends if it ascended); '
                    'presentation CALLED -> %r (Menachot 5:6: neither waved nor presented)' % (SHOW_REM, SHOW_PRES), ['due_to_priest'])
    if q == 'sabbath_exchange':
        return cell({'doubled': 2, 'new': 'arranged_on_the_sabbath', 'old': 'burned_on_the_sabbath', 'reeds': 'removed_friday_not_set_on_the_sabbath', 'after': 'three_under_each_two_under_the_top'}, I,
                    ('24:8 "on the Sabbath day, on the Sabbath day" — the token doubled (%d) — ' + SE + 'Chapter 18 8-9 = Mishnah Menachot 11:6-7') % (c_tamid[1],), ['bread_set_weekly'])
    if q == 'exchange_protocol':
        return cell({'in': 'four_priests_two_rows_two_dishes', 'out': 'four_before_them', 'stand': 'enterers_north_removers_south', 'continually': 'ones_handbreadth_against_the_others', 'R._Yosei': 'even_take_then_place'}, A,
                    'Mishnah Menachot 11:7 — Exod 25:30\'s "before Me CONTINUALLY" [IMPORT] read as an unbroken table', ['bread_set_weekly'])
    if q == 'invalid_arrangements':
        return cell({'bread_on_sabbath_dishes_after': 'invalid_no_piggul', 'both_on_sabbath_burned_after': 'invalid', 'both_after_burned_on_sabbath': 'invalid', 'remedy': 'leave_it_for_the_coming_sabbath'}, A,
                    'Mishnah Menachot 11:8 — the frankincense the permitter (' + SE + 'Chapter 18 6); the remedy = the weekly timer\'s next tick', ['bread_set_weekly'])
    if q == 'window':
        days = k['case']
        W = {'plain': 9, 'festival_on_friday': 10, 'two_days_rosh_hashanah': 11}
        return cell(W[days], A, 'Mishnah Menachot 11:9 — baked Friday, set on the Sabbath, eaten the next Sabbath: nine; the baking pushed back by a festival (ten) or Rosh Hashanah\'s two days (eleven); overrides neither Sabbath nor festival', ['bread_set_weekly'])
    if q == 'covenant':
        return cell({'from_the_children_of_israel': 'by_their_consent', 'eternal_covenant': 'from_Him_whose_it_is'}, M, '24:8 — ' + SE + 'Chapter 18 9', ['bread_set_weekly'])
    if q == 'eating':
        return cell({'place': 'a_holy_place', 'kneading_shaping': ['holy_place_too', 'R._Yehuda_all_inside', 'R._Shimon_valid_at_beit_pagi'], 'one_broken': 'all_disqualified', 'aaron': 'without_division', 'sons': 'in_division', 'after': 'the_fires_gift'}, M,
                    ('24:9 "to Aaron and his sons... in a holy place... most holy... from the fire offerings" (%s) — ' + SE + 'Chapter 18 10-11 = Mishnah Menachot 11:2') % (c_close,), ['due_to_priest', 'most_holy'])
    if q == 'dimensions':
        return cell({'loaf': 'ten_by_five_horns_seven', 'table': ['R._Yehuda_ten_by_five', 'R._Meir_twelve_by_six'], 'faces': 'ben_Zoma_from_Exod_25_30'}, D, 'Mishnah Menachot 11:4-5 — the data channel', [FX.NONE])
    if q == 'two_tables':
        return cell({'marble': 'at_entry', 'gold_in_the_porch': 'at_exit', 'gold_inside': 'the_bread_continually', 'rule': 'raise_in_holiness_never_lower'}, A, 'Mishnah Menachot 11:7', [FX.NONE])
    if q == 'workshop':
        return cell('the_showbread_chamber_northwest', D, 'Mishnah Tamid 3:3 — the chamber where they made the showbread (24:5\'s baking inside, Menachot 11:2)', [FX.NONE])
    if q == 'sieves':
        return cell({'showbread': 11, 'two_loaves': 12, 'omer': 13, 'R._Shimon': 'no_number'}, D, 'Mishnah Menachot 6:7 — 24:5 "fine flour" (the data channel)', [FX.NONE])
    if q == 'close':
        return cell({'24:3': 'an_eternal_statute', '24:8': 'an_eternal_covenant', '24:9': 'an_eternal_statute'}, I, 'the three perpetual clauses closing the lamp, the setting, the eating (%s)' % (c_close[2],), [FX.NONE])
    raise ValueError(q)

import os as _os5, sys as _sys5, io as _io5, contextlib as _ctx5
_sys5.path.insert(0, _os5.path.dirname(_os5.path.abspath(__file__)))
# ---- THE WRAP (W5 HOLINESS, SANCTIONS, THE LAND, 2026-09-07): the daemon over the compiled priesthood engine ----
import world_engine as WE
def _fx_union(cells):
    fx, why = set(), {}
    for c in cells:
        for f in c['fx']:
            fx.add(f); why.setdefault(f, c)
    return fx, why
def law_priesthood(event, world):
    """Lev 21, 22, 24:1-9 (cold_run_priesthood.py — family, blemish, holy_food, acceptable, lamp_table): the priest's file, the blemish census, the eaters, the acceptable animal, the lamp's morning and the bread's week as TIMERS."""
    k, src = event['kind'], event['case_source']
    E_ = lambda eff, s, cp=None, amount=None, due=None, law='', value=None: {'effect': eff, 'subject': s, 'counterparty': cp, 'amount': amount, 'due': due, 'value': value if value is not None else True, 'source_law': law, 'case_source': src}
    day = event.get('day', world.clock.day)
    if k == 'priest_defiled_for_dead':
        p = event['priest']; dead = event.get('dead'); rank = event.get('rank', 'common')
        if event.get('onen'):
            c = family('onen')
            return [E_('service_profaned', p, value=c['v'], law='F1 [Mishnah Zevachim 2:1 — the onen\'s service %s]' % c['v'])]
        if rank == 'high':
            c = family('high_priest_dead')
            return [E_('lashes', p, amount=2, value=str(c['v'])[:70], law='F1 [INK 21:11 "to any dead soul he shall not come, for his father and for his mother he shall not be defiled" — two prohibitions]')]
        if dead == 'wife':
            c = family('husband', wife=event.get('wife', 'fit'))
            if 'defiled_for_kin' in c['fx']:
                return [E_('defiled_for_kin', p, cp=dead, value=c['v'], law='F1 [INK 21:4 "a HUSBAND shall not be defiled among his people to profane himself" — %s]' % c['v'])]
            return []                                                # an unfit wife: he does not defile (Sifra Emor Section 1 15) — the silence
        if dead == 'abandoned_corpse':
            c = family('met_mitzvah')
            return [E_('defiled_for_kin', p, cp=dead, value=c['v'], law='F1 [Sifra Emor Section 1 3 — %s]' % c['v'])]
        rel = family('relatives')
        if dead in rel['v']:
            f = family('forced')
            return [E_('defiled_for_kin', p, cp=dead, value=(f['v'] if event.get('forced') else dead), law='F1 [INK 21:2-3 "except for his near kin" — the seven relatives on six tokens: %s]' % rel['v'])]
        c = family('addressees')
        return [E_('lashes', p, value='defiled_for_a_stranger', law='F1 [INK 21:1 "for a soul he shall not be defiled among his people" — %s not a relative (the sons of Aaron %s)]' % (dead, c['v']['sons_of_aaron']))]
    if k == 'priest_body_marked':
        p = event['priest']; act = event.get('act', 'beard')
        if act == 'gash':
            g = family('gash_multiplier'); n = event.get('gashes', 1) * event.get('dead', 1)
            return [E_('lashes', p, amount=n, value=g['v'], law='F1 [INK 21:5 "in their flesh they shall not gash a gash" — the multiplier %s (Mishnah Makkot 3:5)]' % g['v'])]
        if act == 'baldness':
            m = family('marks')
            return [E_('lashes', p, value=m['v']['baldness'], law='F1 [INK 21:5 "they shall not make a baldness on their head" — %s]' % m['v']['baldness'])]
        r = family('razor'); lc = family('lash_count'); corners = family('corners')
        return [E_('lashes', p, amount=(corners['v']['beard'] if event.get('warned_each_time') else 1), value=r['v'], law='F1 [INK 21:5 "the corner of their beard they shall not shave" — the razor %s; %s]' % (r['v'], lc['v']))]
    if k == 'priest_married':
        p = event['priest']; her = event.get('her', 'fit'); rank = event.get('rank', 'common')
        if event.get('brother_rank'):
            c = family('yevamot_table', her=her, rank=rank, brother=event['brother_rank'])
            if c['v']['husband'] == 'forbidden' or c['v']['levir'] == 'forbidden':
                return [E_('profaned_seed', p, cp='the-wife', value=str(c['v']), law='F1 [INK 21:7 / 21:14 as a two-parameter predicate (her status, his rank) for the husband and the levir (Mishnah Yevamot 9:1-2): %s]' % c['v'])]
            return []
        fb = family('four_barred')
        barred = (her in fb['v']) if rank == 'high' else (her in ('divorcee', 'profaned', 'harlot', 'chalutzah'))
        if not barred:
            return []                                                # a fit wife — the silence
        seed = family('seed'); cb = family('conduct_bars'); nt = family('not_transferable')
        return [E_('profaned_seed', p, cp='the-wife', value=seed['v']['status'], law='F1 [INK 21:15 "he shall not profane his seed among his people" — %s: the seed %s]' % (her, seed['v']['status'])),
                E_('lashes', p, value=nt['v'], law='F1 [INK 21:7 "they shall not take" — the take doubled: %s]' % family('take_doubled')['v']),
                E_('service_profaned', p, value=cb['v']['marries_in_transgression'], law='F1 [Mishnah Bekhorot 7:7 — %s]' % cb['v']['marries_in_transgression'])]
    if k == 'priest_daughter_whored':
        d = event['daughter']
        if event.get('by') == 'unmarried':
            return []                                                # not by a husband's bond: no burning (Sifra Emor Chapter 1 14) — the silence
        pred = family('daughter_predicate'); mode = family('daughter_mode'); lst = family('daughter_in_burned_list')
        return [E_('burned_by_court', d, cp=event.get('father'), value=mode['v'], law='F1 [INK 21:9 "in fire she shall be burned" — %s; in the burned list: %s (CALLED cold_run_sanctions.census)]' % (pred['v']['by'], lst['v']))]
    if k == 'head_anointed':
        if WE.seat(src) != ('Lev', 21): return []                                # O2 (2026-09-07): this daemon reads its own span — the run's 8:12 is the investiture's act (anointed); 21:10's statute row is this runner's
        p = event.get('priest', event.get('subject', 'aaron'))
        oh = family('one_hour'); gr = family('greatness'); nz = family('nezer')
        return [E_('invested_office', p, value=oh['v'], law='F1 [INK 21:10 "on whose head the anointing oil was poured and who was invested to wear the garments" — %s; the greatness %s; %s]' % (oh['v'], gr['v'], nz['v']))]
    if k == 'blemished_priest_approached':
        p = event['priest']
        if event.get('passing') == 'healed':
            cells = [blemish('passed_blemish')]
        else:
            if event.get('joined_to'):
                c0 = blemish('fingers', joined_to=event['joined_to'])
            elif event.get('head'):
                c0 = blemish('members', head=event['head'])
            else:
                c0 = blemish('heads')
            cells = [c0]
            if 'blemish_barred' in c0['fx']:
                cells.append(blemish('veil_altar'))
                if event.get('served'):
                    cells.append(blemish('served'))
                if event.get('eats'):
                    cells.append(blemish('eats'))
        fx, why = _fx_union(cells); out = []
        if 'blemish_barred' in fx:
            out.append(E_('blemish_barred', p, value=str(why['blemish_barred']['v'])[:70], law='F2 [INK 21:17-23 "in whom is a blemish shall not approach" — %s]' % why['blemish_barred']['why'][:80]))
        if 'accepted' in fx:
            out.append(E_('accepted', p, value=why['accepted']['v'], law='F2 [%s]' % why['accepted']['why'][:100]))
        if 'service_profaned' in fx:
            out.append(E_('service_profaned', p, value=str(why['service_profaned']['v'])[:70], law='F2 [Mishnah Zevachim 2:1 — the blemished priest\'s service invalid]'))
        if 'due_to_priest' in fx:
            out.append(E_('due_to_priest', p, value=str(why['due_to_priest']['v'])[:70], law='F2 [INK 21:22 "the bread of his God, of the most holy and of the holy, he may eat"]'))
        if 'most_holy' in fx:
            out.append(E_('most_holy', 'the-bread-of-his-god', cp=p, value=str(why['most_holy']['v'])[:70], law='F2 [INK 21:22 — of the most holy he eats]'))
        return out
    if k == 'priest_impure_approached_holy':
        p = event['priest']; imp = event.get('impurity', 'corpse'); act = event.get('act', 'eat')
        cells = [holy_food('until_pure'), holy_food('two_gates'), holy_food('name_frame')]
        if event.get('deliberate'):
            cells += [holy_food('karet_extension') if act == 'approach' else holy_food('die_by_it'), holy_food('profaners')]
        if imp == 'zav':
            cells.append(holy_food('zav_tier'))
        if event.get('bathed'):
            cells.append(holy_food('whole_body'))
        fx, why = _fx_union(cells); out = []
        if 'karet_cut_off' in fx:
            out.append(E_('karet_cut_off', p, cp='HEAVEN', value=str(why['karet_cut_off']['v'])[:70], law='F3 [INK 22:3 "with his impurity upon him, that soul shall be cut off from before Me" — %s]' % why['karet_cut_off']['why'][:70]))
        if 'death_by_heaven' in fx:
            out.append(E_('death_by_heaven', p, cp='HEAVEN', value=str(why['death_by_heaven']['v'])[:70], law='F3 [INK 22:9 "lest they bear sin for it and die by it" — %s]' % why['death_by_heaven']['why'][:70]))
        if 'impure_until_evening' in fx:
            out.append(E_('impure_until_evening', p, value=why['impure_until_evening']['v'], law='F3 [INK 22:6-7 "impure until evening... and the sun sets and he is pure"]'))
        if 'immersed' in fx:
            out.append(E_('immersed', p, value=why['immersed']['v'], law='F3 [INK 22:6 "unless he has bathed his flesh in water" — %s]' % why['immersed']['v']))
        if 'stranger_barred' in fx:
            out.append(E_('stranger_barred', p, value=str(why['stranger_barred']['v'])[:70], law='F3 [INK 22:4 "shall not eat of the holy things until he is pure" — %s]' % why['stranger_barred']['why'][:70]))
        if 'name_profaned' in fx:
            out.append(E_('name_profaned', p, cp='HEAVEN', value=str(why['name_profaned']['v'])[:70], law='F3 [INK 22:2 / 22:32 "and not profane My holy name" — the name frame at %s]' % why['name_profaned']['v']))
        return out
    if k == 'terumah_eaten':
        e = event['eater']; cells = []
        if event.get('who'):
            cells.append(holy_food('household', who=event['who']))
        if event.get('husband'):
            cells.append(holy_food('eating_table', husband=event['husband'], son_alive=event.get('son_alive', True), after=event.get('after')))
        if event.get('stage'):
            cells.append(holy_food('stage', stage=event['stage']))
        if event.get('type'):
            cells.append(holy_food('slaves_of_forbidden_wife', type=event['type']))
        if 'deliberate' in event:
            cells.append(holy_food('error_gate', deliberate=event['deliberate']))
            if not event['deliberate']:
                cells.append(holy_food('fifth_gates'))               # the fifth rides the ERRING eater alone (22:14 "in error"; Mishnah Terumot 7:1) — the probe caught the deliberate eater's fifth
        if event.get('case'):
            cells.append(holy_food(event['case']))
        fx, why = _fx_union(cells); out = []
        if 'terumah_fed' in fx:
            out.append(E_('terumah_fed', e, value=str(why['terumah_fed']['v'])[:70], law='F3 [INK 22:11 / 22:13 — %s]' % why['terumah_fed']['why'][:90]))
        if 'stranger_barred' in fx:
            out.append(E_('stranger_barred', e, value=str(why['stranger_barred']['v'])[:70], law='F3 [INK 22:10 / 22:12 "no stranger shall eat a holy thing" — %s]' % why['stranger_barred']['why'][:80]))
        if 'adds_fifth' in fx:
            out.append(E_('adds_fifth', e, cp='the-priest', value=str(why['adds_fifth']['v'])[:70], law='F3 [INK 22:14 "he shall add its fifth to it and give the holy thing to the priest" — %s]' % why['adds_fifth']['why'][:70]))
        if 'pays' in fx:
            out.append(E_('pays', e, cp='the-priest', value=str(why['pays']['v'])[:70], law='F3 [INK 22:14 the principal — %s]' % why['pays']['why'][:80]))
        if 'pays_double' in fx:
            out.append(E_('pays_double', e, cp='the-priest', value=str(why['pays_double']['v'])[:70], law='F3 [Mishnah Terumot 6:4 — the thief: %s]' % why['pays_double']['why'][:70]))
        if 'burned_by_court' in fx:
            out.append(E_('burned_by_court', e, value=str(why['burned_by_court']['v'])[:70], law='F3 [%s]' % why['burned_by_court']['why'][:100]))
        if 'death_by_heaven' in fx:
            out.append(E_('death_by_heaven', e, cp='HEAVEN', value=str(why['death_by_heaven']['v'])[:70], law='F3 [%s]' % why['death_by_heaven']['why'][:100]))
        return out
    if k == 'offering_vowed':
        o = event['offerer']; cells = []
        if event.get('offerer_class') == 'foreigner':
            cells.append(acceptable('vow_class'))
        if event.get('head'):
            cells += [acceptable('beast_members', head=event['head']), acceptable('descends')]
            if event.get('place') == 'outside':
                cells.append(acceptable('under_age_outside'))
        elif event.get('castrated'):
            cells.append(acceptable('castration'))
        elif event.get('vow_kind') == 'todah':
            cells.append(acceptable('todah_window'))
        elif event.get('vow_kind') == 'shelamim':
            cells += [acceptable('shelamim_window'), acceptable('whole_male')]
        elif event.get('vow_kind') == 'upkeep':
            cells.append(acceptable('upkeep'))
        elif not event.get('case'):
            cells += [acceptable('whole_male'), acceptable('olah_rite')]
        if event.get('case'):
            cells.append(acceptable(event['case']))
        fx, why = _fx_union(cells); out = []
        if 'accepted' in fx:
            out.append(E_('accepted', o, cp='HEAVEN', value=str(why['accepted']['v'])[:70], law='F4 [INK 22:19 "to your acceptance, whole, male" — %s]' % why['accepted']['why'][:80]))
        if 'not_accepted' in fx:
            out.append(E_('not_accepted', 'the-blemished-offering', cp=o, value=str(why['not_accepted']['v'])[:70], law='F4 [INK 22:20 "anything in which is a blemish you shall not bring, for it shall not be to acceptance for you" — %s]' % why['not_accepted']['why'][:70]))
        if 'consecrated' in fx:
            out.append(E_('consecrated', 'the-vowed-thing', cp=o, value=str(why['consecrated']['v'])[:70], law='F4 [%s]' % why['consecrated']['why'][:100]))
        if 'lashes' in fx:
            out.append(E_('lashes', o, value=str(why['lashes']['v'])[:70], law='F4 [INK 22:24 "and in your land you shall not do" — %s]' % why['lashes']['why'][:80]))
        if 'name_profaned' in fx:
            out.append(E_('name_profaned', o, cp='HEAVEN', value=str(why['name_profaned']['v'])[:70], law='F4 [INK 22:32 "and you shall not profane My holy name, and I will be sanctified" — %s]' % why['name_profaned']['why'][:70]))
        if 'exempt' in fx:
            out.append(E_('exempt', o, value=str(why['exempt']['v'])[:70], law='F4 [%s]' % why['exempt']['why'][:100]))
        if 'forewarned' in fx:
            out.append(E_('forewarned', o, value=str(why['forewarned']['v'])[:70], law='F4 [Mishnah Chullin 5:3 — the four periods: %s]' % why['forewarned']['why'][:70]))
        if 'eating_window' in fx:
            out.append(E_('eating_window', o, value=str(why['eating_window']['v'])[:70], law='F4 [INK 22:30 "on that day it shall be eaten, you shall not leave of it until morning" — %s]' % why['eating_window']['why'][:70]))
        return out
    if k == 'firstling_born':
        a = event['animal']; o = event.get('owner'); d0 = event.get('day', day)
        e8 = acceptable('eighth_day_by_call'); bl = acceptable('birth_list'); oh = acceptable('one_hour')
        if event.get('birth') in ('hybrid', 'look_alike'):
            return [E_('eighth_day_fit', a, cp=o, due=d0 + 7, value=bl['v'][event['birth']], law='F4 [Mishnah Chullin 4:5 / Sifra Emor Chapter 8 — %s]' % bl['v'][event['birth']])]
        return [E_('eighth_day_fit', a, cp=o, due=d0 + 7, value=e8['v'], law='F4 [INK 22:27 "from the eighth day and onward it shall be accepted" — CALLED cold_run_ordinances (Exod 22:29, one timer at two seats): %s]' % e8['v']),
                E_('accepted', a, cp='HEAVEN', due=d0 + 7, value=oh['v'], law='F4 [INK 22:27 "seven days under its mother" — %s]' % oh['v'])]
    if k == 'mother_and_young_slaughtered':
        s_ = event['slaughterer']; cells = []
        if event.get('seq'):
            cells.append(acceptable('order_cases', seq=event['seq']))
        if event.get('animal_kind'):
            cells.append(acceptable('cells', kind=event['animal_kind'], place=event.get('place', 'outside'), order=event.get('order', 'first')))
        cells += [acceptable('it_and_its_mother'), acceptable('day_boundary')]
        if event.get('sex') == 'male':
            cells.append(acceptable('female_rule'))
        fx, why = _fx_union(cells); out = []
        if 'same_day_slaughter_barred' in fx:
            out.append(E_('same_day_slaughter_barred', s_, value=why['same_day_slaughter_barred']['v'], law='F4 [INK 22:28 "it and its young you shall not slaughter on one day" — %s]' % why['same_day_slaughter_barred']['why'][:80]))
        if 'lashes' in fx:
            v = why['lashes']['v']
            out.append(E_('lashes', s_, amount=(v if isinstance(v, int) else None), value=str(v)[:60], law='F4 [Mishnah Chullin 5:3 — %s]' % why['lashes']['why'][:80]))
        return out
    if k == 'lamps_raised':
        if WE.seat(src) != ('Lev', 24): return []                                # O2: the erection's act at Exod 40:25 is law_erection's; this daemon reads the statute's own rows (Lev 24:2-4)
        p = event.get('priest', 'aaron')
        c = lamp_table('tending', found=event['found']) if event.get('found') else lamp_table('evening_to_morning')
        return [E_('lamp_arranged', 'the-lampstand', cp=p, due=day + 1, value=str(c['v'])[:70], law='F5 [INK 24:3 "Aaron shall arrange it from evening to morning before the LORD continually" — the morning TIMER; %s]' % str(c['v'])[:70])]
    if k == 'bread_arranged':
        if WE.seat(src) != ('Lev', 24): return []                                # O2: the erection's act at Exod 40:23 is law_erection's; this daemon reads the statute's own rows (Lev 24:5-9)
        p = event.get('priest', 'aaron'); lv = lamp_table('loaves'); se = lamp_table('sabbath_exchange'); me = lamp_table('memorial'); ea = lamp_table('eating'); nf = lamp_table('not_the_fires')
        wd = lamp_table('window', case=event.get('case', 'plain'))
        return [E_('bread_set_weekly', 'the-table', cp=p, amount=lv['v']['count'], due=day + 7, value=se['v']['new'], law='F5 [INK 24:8 "on the sabbath day, on the sabbath day he shall arrange it" — the weekly TIMER; the window %d days (Mishnah Menachot 11:9)]' % wd['v']),
                E_('azkarah_to_fire', 'the-frankincense', cp=p, value=me['v'], law='F5 [INK 24:7 "pure frankincense... for the bread a memorial, a fire offering" — %s]' % me['v']),
                E_('due_to_priest', 'the-loaves', cp='the-priests', due=day + 7, value=nf['v'], law='F5 [INK 24:9 "it shall be for Aaron and for his sons" — %s]' % nf['v']),
                E_('most_holy', 'the-loaves', value=ea['v']['place'], law='F5 [INK 24:9 "they shall eat it in a holy place, for it is most holy"]')]
    return []

def scene():
    """THE SCENE — Yevamot 6-9, Bekhorot 6-7, Terumot 6-8, Chullin 5, Menachot 11, Tamid 3 and the Sifra's rows replayed on the world engine (clock unit: days): the firstling's eighth day, the lamp's morning, the bread's week as TIMERS."""
    with _ctx5.redirect_stdout(_io5.StringIO()):
        w = WE.World(era='the priesthood and its dues: Yevamot, Bekhorot, Terumot, Chullin 5, Menachot 11 on the engine (clock unit: days)')
        w.laws = [law_priesthood]
        w.advance(1)
        for who, ev in (('the-mourning-priest', {'dead': 'mother'}), ('the-husband', {'dead': 'wife', 'wife': 'fit'}), ('the-husband-of-the-unfit', {'dead': 'wife', 'wife': 'unfit'}), ('the-finder', {'dead': 'abandoned_corpse'}),
                        ('the-onen', {'dead': 'father', 'onen': True}), ('the-high-priest', {'rank': 'high', 'dead': 'father'}), ('the-defiled-for-a-stranger', {'dead': 'neighbor'})):
            w.submit(dict({'kind': 'priest_defiled_for_dead', 'subject': who, 'priest': who, 'day': 1, 'case_source': 'Lev 21:1-4, 21:11; Sifra Emor Section 1 — %s' % who}, **ev))
        w.submit({'kind': 'priest_body_marked', 'subject': 'the-gashing-priest', 'priest': 'the-gashing-priest', 'act': 'gash', 'gashes': 5, 'dead': 1, 'day': 1, 'case_source': 'Lev 21:5; Mishnah Makkot 3:5 — five gashes'})
        w.submit({'kind': 'priest_body_marked', 'subject': 'the-bald-priest', 'priest': 'the-bald-priest', 'act': 'baldness', 'day': 1, 'case_source': 'Lev 21:5 — a baldness on the head'})
        w.submit({'kind': 'priest_body_marked', 'subject': 'the-razor-priest', 'priest': 'the-razor-priest', 'act': 'beard', 'warned_each_time': True, 'day': 1, 'case_source': 'Lev 21:5; Mishnah Makkot 3:5 — the five corners of the beard, each warned'})
        w.submit({'kind': 'priest_married', 'subject': 'the-priest-of-the-divorcee', 'priest': 'the-priest-of-the-divorcee', 'her': 'divorcee', 'day': 1, 'case_source': 'Lev 21:7; Mishnah Yevamot 6:2 — the divorcee'})
        w.submit({'kind': 'priest_married', 'subject': 'the-high-priest-of-the-widow', 'priest': 'the-high-priest-of-the-widow', 'rank': 'high', 'her': 'widow', 'day': 1, 'case_source': 'Lev 21:14 — the widow barred to the high priest alone'})
        w.submit({'kind': 'priest_married', 'subject': 'the-priest-of-the-widow', 'priest': 'the-priest-of-the-widow', 'rank': 'common', 'her': 'widow', 'day': 1, 'case_source': 'Lev 21:7 — the widow permitted to the common priest: the silence'})
        w.submit({'kind': 'priest_married', 'subject': 'the-levir-case', 'priest': 'the-levir-case', 'rank': 'common', 'her': 'widow', 'brother_rank': 'high', 'day': 1, 'case_source': 'Mishnah Yevamot 9:1 — permitted to the husband, forbidden to the levir'})
        w.submit({'kind': 'priest_daughter_whored', 'subject': 'the-priests-daughter', 'daughter': 'the-priests-daughter', 'father': 'the-priest', 'by': 'betrothed', 'day': 1, 'case_source': 'Lev 21:9; Mishnah Sanhedrin 9:1 — burned'})
        w.submit({'kind': 'priest_daughter_whored', 'subject': 'the-unmarried-daughter', 'daughter': 'the-unmarried-daughter', 'father': 'the-priest', 'by': 'unmarried', 'day': 1, 'case_source': 'Sifra Emor Chapter 1 14 — not by a husband\'s bond: the silence'})
        w.submit({'kind': 'head_anointed', 'subject': 'aaron', 'priest': 'aaron', 'by': 'oil', 'day': 1, 'case_source': 'Lev 21:10; Sifra Emor Chapter 2 — the office attaches at the pouring'})
        w.submit({'kind': 'blemished_priest_approached', 'subject': 'the-blind-priest', 'priest': 'the-blind-priest', 'head': 'blind', 'served': True, 'eats': True, 'day': 1, 'case_source': 'Lev 21:18-23; Mishnah Bekhorot 7:3; Zevachim 2:1 — the blind priest: barred, his service invalid, he eats'})
        w.submit({'kind': 'blemished_priest_approached', 'subject': 'the-healed-priest', 'priest': 'the-healed-priest', 'passing': 'healed', 'day': 1, 'case_source': 'Sifra Emor Section 3 — the passing blemish healed: fit'})
        w.submit({'kind': 'blemished_priest_approached', 'subject': 'the-joined-finger', 'priest': 'the-joined-finger', 'joined_to': 'joint', 'day': 1, 'case_source': 'Mishnah Bekhorot 7:6 — the extra finger joined to the joint: fit'})
        w.submit({'kind': 'priest_impure_approached_holy', 'subject': 'the-impure-eater', 'priest': 'the-impure-eater', 'impurity': 'corpse', 'act': 'eat', 'deliberate': True, 'day': 1, 'case_source': 'Lev 22:4-9; Mishnah Sanhedrin 9:6 — the deliberate impure eater: death by Heaven'})
        w.submit({'kind': 'priest_impure_approached_holy', 'subject': 'the-impure-approacher', 'priest': 'the-impure-approacher', 'impurity': 'corpse', 'act': 'approach', 'deliberate': True, 'day': 1, 'case_source': 'Lev 22:3; Mishnah Keritot 1:1 — the impure approach: karet'})
        w.submit({'kind': 'priest_impure_approached_holy', 'subject': 'the-zav-priest', 'priest': 'the-zav-priest', 'impurity': 'zav', 'act': 'eat', 'bathed': True, 'day': 1, 'case_source': 'Lev 22:4, 22:6-7 — the zav until pure, the whole body immersed'})
        w.submit({'kind': 'terumah_eaten', 'subject': 'the-priests-wife', 'eater': 'the-priests-wife', 'husband': 'priest', 'son_alive': True, 'day': 1, 'case_source': 'Lev 22:11; Mishnah Yevamot 9:5 — the priest\'s wife eats'})
        w.submit({'kind': 'terumah_eaten', 'subject': 'the-returned-daughter', 'eater': 'the-returned-daughter', 'husband': 'israelite', 'son_alive': False, 'after': 'fathers_house', 'day': 1, 'case_source': 'Lev 22:13; Mishnah Yevamot 9:6 — widowed without seed, returned'})
        w.submit({'kind': 'terumah_eaten', 'subject': 'the-strangers-wife', 'eater': 'the-strangers-wife', 'husband': 'israelite', 'son_alive': True, 'day': 1, 'case_source': 'Lev 22:12 — to a stranger man: she shall not eat'})
        w.submit({'kind': 'terumah_eaten', 'subject': 'the-erring-eater', 'eater': 'the-erring-eater', 'deliberate': False, 'day': 1, 'case_source': 'Lev 22:14; Mishnah Terumot 6:1 — in error: the principal and the fifth'})
        w.submit({'kind': 'terumah_eaten', 'subject': 'the-deliberate-eater', 'eater': 'the-deliberate-eater', 'deliberate': True, 'day': 1, 'case_source': 'Mishnah Terumot 7:1 — deliberate: the principal, no fifth'})
        w.submit({'kind': 'terumah_eaten', 'subject': 'the-terumah-thief', 'eater': 'the-terumah-thief', 'case': 'thief', 'day': 1, 'case_source': 'Mishnah Terumot 6:4 — the thief: double'})
        w.submit({'kind': 'terumah_eaten', 'subject': 'the-workers', 'eater': 'the-workers', 'case': 'workers', 'day': 1, 'case_source': 'Mishnah Terumot 6:3 — the workers: the fifth'})
        w.submit({'kind': 'terumah_eaten', 'subject': 'the-daughter-who-ate', 'eater': 'the-daughter-who-ate', 'case': 'daughter_who_ate', 'day': 1, 'case_source': 'Mishnah Terumot 7:2 — the priest\'s daughter married to an Israelite who ate'})
        w.submit({'kind': 'terumah_eaten', 'subject': 'the-betrothed', 'eater': 'the-betrothed', 'stage': 'betrothed', 'day': 1, 'case_source': 'Mishnah Yevamot 7:4 — betrothed: does not eat'})
        w.submit({'kind': 'terumah_eaten', 'subject': 'the-iron-flock-slave', 'eater': 'the-iron-flock-slave', 'type': 'iron_flock', 'day': 1, 'case_source': 'Mishnah Yevamot 7:1 — the iron-flock slaves eat'})
        for who, ev in (('the-vower', {}), ('the-blind-offering-bringer', {'head': 'blind'}), ('the-castrator', {'castrated': True}), ('the-todah-bringer', {'vow_kind': 'todah'}), ('the-shelamim-vower', {'vow_kind': 'shelamim'}), ('the-upkeep-vower', {'vow_kind': 'upkeep'}),
                        ('the-foreigner', {'offerer_class': 'foreigner'}), ('the-outside-blemished', {'head': 'blind', 'place': 'outside'}), ('the-forewarned', {'case': 'four_periods'}), ('the-name-sanctifier', {'case': 'sanctify_name'})):
            w.submit(dict({'kind': 'offering_vowed', 'subject': who, 'offerer': who, 'day': 1, 'case_source': 'Lev 22:17-33; Mishnah Bekhorot 6, Temurah 6, Zevachim 5 — %s' % who}, **ev))
        w.submit({'kind': 'firstling_born', 'subject': 'the-firstling', 'animal': 'the-firstling', 'owner': 'the-herdsman', 'day': 1, 'case_source': 'Lev 22:27 — seven days under its mother, from the eighth accepted (the second seat)'})
        w.submit({'kind': 'mother_and_young_slaughtered', 'subject': 'the-slaughterer', 'slaughterer': 'the-slaughterer', 'seq': 'cow_then_two_young', 'day': 1, 'case_source': 'Lev 22:28; Mishnah Chullin 5:3 — the mother then her young: each'})
        w.submit({'kind': 'mother_and_young_slaughtered', 'subject': 'the-consecrated-slaughterer', 'slaughterer': 'the-consecrated-slaughterer', 'animal_kind': 'consecrated', 'place': 'outside', 'order': 'first', 'day': 1, 'case_source': 'Mishnah Chullin 5:1 — consecrated outside: karet for the first, the second flogged'})
        w.submit({'kind': 'mother_and_young_slaughtered', 'subject': 'the-plain-slaughterer', 'slaughterer': 'the-plain-slaughterer', 'day': 1, 'case_source': 'Lev 22:28 — it and its young on one day'})
        w.submit({'kind': 'lamps_raised', 'subject': 'the-lampstand', 'priest': 'aaron', 'found': 'two_eastern_burning', 'day': 1, 'case_source': 'Lev 24:2-4; Mishnah Tamid 3:9 — the lamps tended, evening to morning'})
        w.submit({'kind': 'bread_arranged', 'subject': 'the-table', 'priest': 'aaron', 'case': 'plain', 'day': 1, 'case_source': 'Lev 24:5-9; Mishnah Menachot 11:1-9 — twelve loaves, the frankincense, the sabbath exchange'})
        w.advance(9)                                                 # the eighth day passed, the week's exchange fired
    n = lambda eid, eff: len([e for e in w.entity(eid).ledger if e['effect'] == eff])
    yr = lambda eid, eff: [e['day'] for e in w.entity(eid).ledger if e['effect'] == eff]
    am = lambda eid, eff: [e['amount'] for e in w.entity(eid).ledger if e['effect'] == eff]
    tset = len([l for l in w.log if l[0] == 'TIMER-SET']); fired = len([l for l in w.log if l[0] == 'TIMER-FIRE'])
    return (n('the-mourning-priest', 'defiled_for_kin'), n('the-husband', 'defiled_for_kin'), n('the-husband-of-the-unfit', 'defiled_for_kin'), n('the-finder', 'defiled_for_kin'), n('the-onen', 'service_profaned'), am('the-high-priest', 'lashes'), n('the-defiled-for-a-stranger', 'lashes'),
            am('the-gashing-priest', 'lashes'), n('the-bald-priest', 'lashes'), am('the-razor-priest', 'lashes'),
            n('the-priest-of-the-divorcee', 'profaned_seed'), n('the-priest-of-the-divorcee', 'lashes'), n('the-priest-of-the-divorcee', 'service_profaned'), n('the-high-priest-of-the-widow', 'profaned_seed'), n('the-priest-of-the-widow', 'profaned_seed'), n('the-levir-case', 'profaned_seed'),
            n('the-priests-daughter', 'burned_by_court'), n('the-unmarried-daughter', 'burned_by_court'), n('aaron', 'invested_office'),
            n('the-blind-priest', 'blemish_barred'), n('the-blind-priest', 'service_profaned'), n('the-blind-priest', 'due_to_priest'), n('the-blind-priest', 'accepted'), n('the-healed-priest', 'accepted'), n('the-joined-finger', 'accepted'), n('the-joined-finger', 'blemish_barred'),
            n('the-impure-eater', 'death_by_heaven'), n('the-impure-eater', 'karet_cut_off'), n('the-impure-eater', 'stranger_barred'), n('the-impure-eater', 'impure_until_evening'), n('the-impure-eater', 'name_profaned'), n('the-impure-approacher', 'karet_cut_off'), n('the-zav-priest', 'immersed'), n('the-zav-priest', 'death_by_heaven'),
            n('the-priests-wife', 'terumah_fed'), n('the-returned-daughter', 'terumah_fed'), n('the-strangers-wife', 'stranger_barred'), n('the-erring-eater', 'adds_fifth'), n('the-erring-eater', 'pays'), n('the-deliberate-eater', 'pays'), n('the-deliberate-eater', 'adds_fifth'), n('the-terumah-thief', 'pays_double'), n('the-workers', 'adds_fifth'), n('the-daughter-who-ate', 'burned_by_court'), n('the-betrothed', 'stranger_barred'), n('the-iron-flock-slave', 'terumah_fed'),
            n('the-vower', 'accepted'), n('the-blemished-offering', 'not_accepted'), n('the-castrator', 'lashes'), n('the-todah-bringer', 'eating_window'), n('the-shelamim-vower', 'eating_window'), n('the-shelamim-vower', 'accepted'), n('the-vowed-thing', 'consecrated'), n('the-foreigner', 'accepted'), n('the-outside-blemished', 'exempt'), n('the-forewarned', 'forewarned'), n('the-name-sanctifier', 'name_profaned'),
            yr('the-firstling', 'eighth_day_fit'), yr('the-firstling', 'accepted'), n('the-slaughterer', 'same_day_slaughter_barred'), am('the-slaughterer', 'lashes'), n('the-consecrated-slaughterer', 'lashes'), n('the-plain-slaughterer', 'same_day_slaughter_barred'),
            yr('the-lampstand', 'lamp_arranged'), yr('the-table', 'bread_set_weekly'), n('the-frankincense', 'azkarah_to_fire'), yr('the-loaves', 'due_to_priest'), n('the-loaves', 'most_holy'),
            tset, fired, w.clock.day), w
SCENE, _W = scene()


# ---- (2) the answer sheet — the Mishnah rows as TEST DATA (verified by their own tokens) ----
def load(t):
    d = json.load(open('<repo-old>/Data/mishnah_%s_he.json' % t))
    return d['text'] if isinstance(d, dict) and 'text' in d else d
SHELF = {'Bekhorot': load('bekhorot'), 'Terumot': load('terumot'), 'Yevamot': load('yevamot'), 'Zevachim': load('zevachim'), 'Temurah': load('temurah'),
         'Menachot': load('menachot'), 'Tamid': load('tamid'), 'Chullin': load('chullin'), 'Sanhedrin': load('sanhedrin'), 'Makkot': load('makkot'),
         'Kiddushin': load('kiddushin'), 'Bava Metzia': load('bava_metzia'), 'Sotah': load('sotah'), 'Shekalim': load('shekalim'), 'Chagigah': load('chagigah'),
         'Eruvin': load('eruvin'), 'Berakhot': load('berakhot'), 'Shabbat': load('shabbat'), 'Horayot': load('horayot'), 'Ketubot': load('ketubot')}
def mrow(book, ch, m, must):
    txt = strip(SHELF[book][ch - 1][m - 1])
    assert must in txt, 'answer-sheet check failed: %r not in Mishnah %s %d:%d' % (must, book, ch, m)
SHEET = [
    ('Bekhorot', 6, 1, 'כרשינה'), ('Bekhorot', 6, 3, 'שמונים'), ('Bekhorot', 6, 6, 'ביצים'), ('Bekhorot', 6, 7, 'קלוטות'), ('Bekhorot', 6, 8, 'ביבנה'), ('Bekhorot', 6, 11, 'נפדין'),
    ('Bekhorot', 6, 12, 'גרב'), ('Bekhorot', 7, 1, 'עוברין'), ('Bekhorot', 7, 2, 'גבן'), ('Bekhorot', 7, 3, 'החרום'), ('Bekhorot', 7, 4, 'אוז'), ('Bekhorot', 7, 5, 'מרוח'),
    ('Bekhorot', 7, 6, 'הכושי'), ('Bekhorot', 7, 7, 'דפן'),
    ('Terumot', 6, 1, 'וחמש'), ('Terumot', 6, 2, 'לעצמה'), ('Terumot', 6, 3, 'פועליו'), ('Terumot', 6, 4, 'כפל'), ('Terumot', 6, 5, 'הלקט'), ('Terumot', 6, 6, 'קשואין'),
    ('Terumot', 7, 1, 'מזיד'), ('Terumot', 7, 2, 'בשרפה'), ('Terumot', 7, 3, 'קטנים'), ('Terumot', 7, 4, 'הכלל'), ('Terumot', 8, 1, 'מום'), ('Terumot', 8, 2, 'יפלט'), ('Terumot', 8, 11, 'מלאכלה'),
    ('Yevamot', 6, 2, 'פסל'), ('Yevamot', 6, 3, 'הארוסין'), ('Yevamot', 6, 4, 'הבוגרת'), ('Yevamot', 6, 5, 'זונה'), ('Yevamot', 7, 1, 'ברזל'), ('Yevamot', 7, 2, 'עבדים'), ('Yevamot', 7, 3, 'מעברת'),
    ('Yevamot', 7, 4, 'מאכילין'), ('Yevamot', 7, 5, 'האונס'), ('Yevamot', 7, 6, 'גדול'), ('Yevamot', 8, 1, 'הערל'), ('Yevamot', 8, 2, 'הביצים'), ('Yevamot', 8, 5, 'זנות'), ('Yevamot', 8, 6, 'חמה'),
    ('Yevamot', 9, 1, 'ליבמיהן'), ('Yevamot', 9, 2, 'שקדש'), ('Yevamot', 9, 3, 'סופרים'), ('Yevamot', 9, 4, 'מארסת'), ('Yevamot', 9, 5, 'במעשר'), ('Yevamot', 9, 6, 'כנעוריה'),
    ('Zevachim', 8, 1, 'ברבוא'), ('Zevachim', 8, 5, 'מומין'), ('Zevachim', 8, 8, 'לאמה'), ('Zevachim', 9, 3, 'מומין'), ('Zevachim', 9, 5, 'הפנים'), ('Zevachim', 14, 2, 'מומין'),
    ('Temurah', 6, 1, 'שהן'), ('Temurah', 6, 4, 'עופות'), ('Temurah', 6, 5, 'ולדותיהן'),
    ('Menachot', 11, 1, 'שנים'), ('Menachot', 11, 2, 'פאגי'), ('Menachot', 11, 4, 'עשרה'), ('Menachot', 11, 5, 'בזיכי'), ('Menachot', 11, 6, 'סניפין'), ('Menachot', 11, 7, 'שיש'),
    ('Menachot', 11, 8, 'הבאה'), ('Menachot', 11, 9, 'מתשעה'), ('Menachot', 8, 4, 'זיתים'), ('Menachot', 8, 5, 'כתית'), ('Menachot', 6, 7, 'נפה'), ('Menachot', 5, 3, 'לבונה'), ('Menachot', 5, 6, 'הפנים'), ('Menachot', 3, 6, 'הבזיכין'),
    ('Tamid', 3, 3, 'הפנים'), ('Tamid', 3, 9, 'מזרחיים'),
    ('Chullin', 5, 1, 'כרת'), ('Chullin', 5, 2, 'סופג'), ('Chullin', 5, 3, 'פרקים'), ('Chullin', 5, 4, 'כרחו'), ('Chullin', 5, 5, 'הלילה'),
    ('Sanhedrin', 9, 1, 'כהן'), ('Sanhedrin', 2, 1, 'באלמנה'), ('Sanhedrin', 11, 1, 'זוממי'), ('Makkot', 3, 1, 'אלמנה'), ('Makkot', 3, 5, 'בתער'), ('Makkot', 3, 8, 'למתים'), ('Makkot', 3, 9, 'ונזיר'), ('Makkot', 1, 1, 'גרושה'),
    ('Kiddushin', 1, 7, 'תטמא'), ('Bava Metzia', 2, 10, 'הקברות'), ('Sotah', 8, 3, 'אלמנה'), ('Shekalim', 1, 5, 'נכרי'), ('Shekalim', 4, 8, 'עולות'), ('Chagigah', 3, 3, 'לתרומה'),
    ('Eruvin', 10, 13, 'יבלת'), ('Berakhot', 1, 1, 'בתרומתן'), ('Shabbat', 19, 6, 'בתרומה'), ('Horayot', 3, 4, 'הבתולה'), ('Ketubot', 5, 3, 'היבם'),
]
for b, ch, m, must in SHEET:
    mrow(b, ch, m, must)
print('answer sheet: %d Mishnah rows verified by their own tokens (Bekhorot 6-7, Terumot 6-8, Yevamot 6-9, Zevachim 8-9, Temurah 6, Menachot 11, Tamid 3, Chullin 5 read whole — the topic docket)' % len(SHEET))

TESTS = [
 ('THE SCENE — Yevamot 6-9, Bekhorot 6-7, Terumot 6-8, Chullin 5, Menachot 11, Tamid 3 on the world engine (the firstling\'s eighth day, the lamp\'s morning, the bread\'s week as TIMERS; the daemon\'s watch coverage printed below)', cell(SCENE, I, 'the priest\'s file, the blemish census by head, the impure priest\'s gates, the eaters of terumah, the acceptable animal, the mother and its young, the lamp and the table — every value a cell\'s', ['defiled_for_kin', 'service_profaned', 'lashes', 'profaned_seed', 'burned_by_court', 'invested_office', 'blemish_barred', 'due_to_priest', 'most_holy', 'accepted', 'karet_cut_off', 'death_by_heaven', 'impure_until_evening', 'immersed', 'stranger_barred', 'name_profaned', 'terumah_fed', 'adds_fifth', 'pays', 'pays_double', 'not_accepted', 'consecrated', 'exempt', 'forewarned', 'eating_window', 'eighth_day_fit', 'same_day_slaughter_barred', 'lamp_arranged', 'bread_set_weekly', 'azkarah_to_fire']), (1, 1, 0, 1, 1, [2], 1, [5], 1, [5], 1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 0, 1, 1, 0, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, [8], [8], 1, [80], 1, 1, [2], [8], 1, [8], 1, 5, 5, 9)),
 # ---- THE PRIEST'S FILE (21:1-15) ----
 ('Sifra Emor Section 1 1 / Kiddushin 1:7 — the addressee census', family('addressees'), {'sons_of_aaron': 'bound', 'daughters_of_aaron': 'free', 'chalalim': 'excluded', 'blemished_and_minors': 'included'}),
 ('Lev 21 — the defile-verb at four seats', family('defile_seats'), [1, 3, 4, 11]),
 ('Sifra Emor Section 1 2-3 — the soul\'s scope', family('soul_scope'), {'corpse': 'defiles', 'blood_quarter_log': 'defiles', 'departing_impurities': 'included'}),
 ('Sifra Emor Section 1 3 — the abandoned corpse', family('met_mitzvah'), 'defiles_for_the_abandoned_corpse'),
 ('Lev 21:2-3 — the seven relatives on six tokens', family('relatives'), ['wife', 'mother', 'father', 'son', 'daughter', 'brother', 'virgin_sister']),
 ('Sifra Emor Section 1 4-10 — the relative table', family('relative_table'), {'wife': 'the_near_kin_betrothed_and_divorced_excluded', 'mother': 'profanable_line', 'father': 'presumption', 'children': 'viable_not_stillborn', 'siblings': 'paternal_who_inherit_him', 'sister': 'minor_virgin_not_betrothed_R_Meir_incl_betrothed', 'brother': 'minor_or_adult'}),
 ('Sifra Emor Section 1 11-12 — the sister\'s predicate', family('sister_predicate'), {'raped_or_seduced': 'excluded_by_virgin', 'wood_injured': 'included_not_by_a_man', 'betrothed': 'included_by_the_near', 'adult': 'included_by_to_him'}),
 ('Sifra Emor Section 1 12 — the forced defilement', family('forced'), 'a_command_enforced_against_his_will'),
 ('Sifra Emor Section 1 13 — the certain only', family('certain_only'), {'doubtful': 'no', 'others_alongside': 'no', 'limb_of_living_parent': 'no', 'barley_bone': ['yes', 'R._Yosei_no']}),
 ('Sifra Emor Section 1 15 — the fit wife', family('husband', wife='fit'), 'defiles'),
 ('Sifra Emor Section 1 15 — the unfit wife', family('husband', wife='unfit'), 'does_not_defile'),
 ('Onkelos Lev 21:4 — the fork on the token', family('husband_fork'), {'sifra': 'husband', 'onkelos': 'the_great_one_among_his_people'}),
 ('Sifra Emor Section 1 16 — the toggling status', family('toggles'), 'profane_while_occupied_holy_on_withdrawal'),
 ('Sifra Emor Chapter 1 1-5 — the three marks and the two-way transfer', family('marks'), {'baldness': 'per_spot_whole_head', 'beard': 'per_corner', 'gash': 'per_gash_for_the_dead'}),
 ('Lev 21:5 + 19:27 — the razor (CALLED)', family('razor'), 'liable'),
 ('Makkot 3:5 — the corners (CALLED)', family('corners'), {'head': 2, 'beard': 5}),
 ('Makkot 3:5 — five gashes for one dead (CALLED)', family('gash_multiplier'), 5),
 ('Sifra Emor Chapter 1 6 — holy by compulsion', family('holy_by_compulsion'), {'compelled': True, 'levites': 'excluded', 'blemished': 'included'}),
 ('Lev 21 — bread at five seats = the offerings', family('bread_is_offering'), [6, 8, 17, 21, 22]),
 ('Sifra Emor Chapter 1 7 / Yevamot 6:5 — the zonah', family('zonah'), {'R._Yehuda': 'the_aylonit', 'sages': ['the_convert', 'the_freed_slavewoman', 'illicit_intercourse'], 'R._Eliezer': 'even_unmarried_not_for_marriage', 'onkelos': 'one_who_goes_astray'}),
 ('Sifra Emor Chapter 1 8 — the chalalah', family('chalalah'), 'born_of_a_disqualified_union'),
 ('Sifra Emor Chapter 1 9-10 / Makkot 3:1 — the chalutzah', family('chalutzah'), ['barred_by_a_fortiori_from_the_divorcee', 'the_rival_refutes', 'and_a_woman_amplifies', 'the_rival_out_by_from_her_husband']),
 ('Sifra Emor Chapter 1 11 / Yevamot 10:3 — the husband\'s hand', family('husbands_hand'), 'the_second_bill_does_not_disqualify_her'),
 ('Lev 21:7 + 21:14 — the take-verb doubled / Yevamot 6:2', family('take_doubled'), {'21:7': 2, '21:14': 2}),
 ('Sifra Emor Chapter 1 13 — sanctify him', family('sanctify_him'), {'by_force': 'beat_him_if_he_refuses', 'warned': 'the_court', 'blemished': 'holy'}),
 ('Lev 21:9 — burning against strangling (CALLED)', family('daughter_mode'), 'burning'),
 ('Sanhedrin 9:1 — the daughter in the burned list (CALLED)', family('daughter_in_burned_list'), True),
 ('Sifra Emor Chapter 1 14-18 / Sanhedrin 11:1 — the daughter\'s predicate', family('daughter_predicate'), {'by': 'whoring_with_a_husbands_bond', 'not_by': 'other_profanations', 'ages': 'all', 'husbands': 'israelite_levite_netin_mamzer', 'partner': 'not_burned', 'perjured': 'not_burned', 'father': ['R._Eliezer_with_her_father_burning', 'with_her_father_in_law_stoning']}),
 ('Onkelos Lev 21:9 — from her father\'s holiness', family('onkelos_daughter'), 'strays_from_her_fathers_holiness'),
 ('Sifra Emor Section 2 1 — the greatness', family('greatness'), ['beauty', 'wealth', 'strength', 'wisdom', 'appearance', 'made_great_from_his_brothers']),
 ('Sifra Emor Section 2 2 / Horayot 3:4 — the one-hour rule', family('one_hour'), 'office_attaches_at_the_pouring'),
 ('Sifra Emor Section 2 3 — the hair and the rending', family('hair_rend'), {'R._Yehuda': 'not_at_all', 'R._Meir': 'not_for_his_dead', 'geometry': 'high_priest_below_commoner_above'}),
 ('Sifra Emor Section 2 4 — the high priest and the dead', family('high_priest_dead'), {'two_prohibitions': ['shall_not_come', 'shall_not_defile'], 'commoner_carries_both': 'by_not_defile_not_defile', 'two_corpses_blood': 'R._Akiva_defiles', 'parents': 'no', 'met_mitzvah': 'yes'}),
 ('Sifra Emor Section 2 5 / Sanhedrin 2:1 — not out of the sanctuary', family('not_out'), {'R._Meir': 'after_them_hidden_and_revealed_to_the_city_gate', 'R._Yehuda': 'not_at_all'}),
 ('Sifra Emor Section 2 6 — the onen: the high priest', family('onen', rank='high'), 'valid'),
 ('Sifra Emor Section 2 6 — the onen: the commoner', family('onen', rank='commoner'), 'invalid'),
 ('Lev 21:12 — the crown of the oil', family('nezer'), 'the_crown_of_the_oil_the_many_garmented_included'),
 ('Sifra Emor Section 2 7 + Chapter 2 6 / Yevamot 6:4 — the virgin command', family('virgin_command'), {'king_nazirite': 'excluded', 'war_priest': 'included', 'adult': ['excluded', 'R._Eliezer_R._Shimon_permit'], 'betrothed_then_appointed': 'marries', 'yevamah_by_maamar': 'not'}),
 ('Lev 21:14 — the four barred', family('four_barred'), ['widow', 'divorcee', 'profaned', 'harlot']),
 ('Sifra Emor Chapter 2 1-8 — the profaned seed', family('seed'), {'status': 'chalal_not_mamzer', 'widow_written': 'stringent_her_seed_profaned', 'divorcee_written': 'lenient_not_mamzer', 'commoner': 'exported_by_zonah_zonah', 'niddah': 'not_chalal_by_these', 'she_herself': 'profaned', 'chalals_daughter': 'disqualified'}),
 ('Lev 21 — the profane root at seven seats', family('profane_seats'), [6, 7, 9, 12, 14, 15, 23]),
 ('Yevamot 9:1 — commoner priest, widow, high-priest brother', family('yevamot_table', her='widow', rank='commoner', brother='high'), {'husband': 'permitted', 'levir': 'forbidden'}),
 ('Yevamot 9:2 — high priest betrothed a widow, commoner brother', family('yevamot_table', her='widow', rank='high', brother='commoner'), {'husband': 'forbidden', 'levir': 'permitted'}),
 ('Yevamot 9:2 — high priest, widow, high-priest brother', family('yevamot_table', her='widow', rank='high', brother='high'), {'husband': 'forbidden', 'levir': 'forbidden'}),
 ('Yevamot 9:2 — a divorcee to any priest', family('yevamot_table', her='divorcee', rank='commoner', brother='commoner'), {'husband': 'forbidden', 'levir': 'forbidden'}),
 ('Yevamot 9:2 — the rest permitted to both', family('yevamot_table', her='fit', rank='commoner', brother='commoner'), {'husband': 'permitted', 'levir': 'permitted'}),
 ('Bekhorot 7:7 — the conduct bars', family('conduct_bars'), {'marries_in_transgression': 'disqualified_until_he_vows_off_benefit', 'defiles_for_the_dead': 'disqualified_until_he_accepts'}),
 ('Makkot 3:8-9 — the lash count', family('lash_count'), {'all_day': 'one', 'warned_each_time': 'each', 'in_the_furrow_of_eight': 'one_of_the_eight'}),
 ('Bava Metzia 2:10 — the lost object', family('lost_object'), 'does_not_defile_nor_obey_his_father'),
 ('Kiddushin 1:7 — the daughters of Aaron', family('women'), 'the_daughters_of_aaron_free'),
 ('Makkot 1:1 — not transferable', family('not_transferable'), 'perjured_not_made_chalal_forty_lashes'),
 ('Sotah 8:3 — the war front', family('war_front'), 'does_not_return'),
 ('Lev 21 — "his people" at four seats', family('amav_seats'), [1, 4, 14, 15]),
 ('Yevamot 9:3 — the ketubah', family('ketubah'), 'has_a_ketubah'),
 # ---- THE BLEMISH CENSUS OF THE PRIEST (21:16-24) ----
 ('Sifra Emor Section 3 1 — the age ladder', blemish('age_ladder'), {'minor': 'unfit_even_whole', 'valid_from': 'two_hairs', 'admitted_at': 'twenty'}),
 ('Sifra Emor Section 3 2 — the future tense', blemish('future_tense'), 'before_or_after_the_utterance_or_born_so'),
 ('Lev 21 + 22 — the blemish tokens', blemish('blemish_tokens'), {'lev_21': 5, 'lev_22': 3}),
 ('Lev 21:17-23 — the approach-verbs', blemish('approach_seats'), {'shall_not_approach': [17, 18, 21, 21], 'shall_not_draw_near': [21, 23], 'shall_not_come': 23}),
 ('Sifra Emor Section 3 3-4 — the service census', blemish('service_census'), {'in_the_ban': ['fats', 'the_handful', 'frankincense', 'incense', 'the_priests_meal_offerings', 'the_libation_meal_offerings', 'pourings', 'mixings', 'wavings', 'presentings', 'scoopings', 'breakings', 'saltings', 'pinchings', 'receivings'], 'liable_only_for': 'service_like_bread'}),
 ('Sifra Emor Section 3 5 / Bekhorot 7:1 — Aaron himself, the passing blemish', blemish('aaron_passing'), {'aaron_himself': 'included', 'passing_blemish': 'included'}),
 ('Lev 21:18-20 — the twelve class heads', blemish('heads'), ['blind', 'lame', 'charum', 'sarua', 'broken_leg', 'broken_hand', 'giben', 'dak', 'tevallul', 'garav', 'yalefet', 'meroach_ashekh']),
 ('Sifra Emor Section 3 6 — blind', blemish('members', head='blind'), ['both_eyes_or_one', 'permanent_cataract', 'permanent_water']),
 ('Sifra Emor Section 3 7 — charum', blemish('members', head='charum'), ['sunken_nose', 'blocked', 'bridgeless', 'dripping']),
 ('Sifra Emor Section 3 9 — sarua', blemish('members', head='sarua'), ['dislocated_hip', 'extra_bone_from_the_thumb', 'heel_jutting_back', 'goose_wide_foot']),
 ('Sifra Emor Section 3 12 / Bekhorot 7:2 — giben', blemish('members', head='giben'), ['no_eyebrows_or_one', 'R._Dosa_lying', 'R._Chanina_two_backs_two_spines']),
 ('Sifra Emor Section 3 12 / Bekhorot 6:2 — dak', blemish('members', head='dak'), ['the_cloud', 'the_snail', 'the_serpent', 'the_grape']),
 ('Sifra Emor Section 3 13 / Bekhorot 6:2 — tevallul', blemish('members', head='tevallul'), ['white_breaking_the_ring_into_the_black', 'R._Yosei_no_blemish_in_the_white']),
 ('Sifra Emor Section 3 15 / Bekhorot 7:5 + Onkelos 21:20 — the testicle reading', blemish('members', head='meroach_ashekh'), ['R._Yishmael_crushed', 'R._Akiva_wind', 'R._Chanina_dark_complexion']),
 ('Lev 21:18-20 vs 22:22-24 — the three shared tokens', blemish('shared_tokens'), ['garav', 'yalefet', 'sarua']),
 ('Sifra Emor Chapter 3 1 — the other blemishes', blemish('other_blemishes'), 'amplified_by_blemish_blemish'),
 ('Sifra Emor Chapter 3 2 / Bekhorot 7:6 — the Kushite class', blemish('kushite_class'), {'in_man': 'unfit', 'in_beast': 'fit', 'members': ['kushite', 'ruddy', 'albino', 'hunchback', 'dwarf', 'deaf', 'fool', 'drunk', 'pure_afflictions']}),
 ('Sifra Emor Chapter 3 3-5 / Bekhorot 7:7 — the beast\'s unfits in man', blemish('beast_unfits_in_man'), {'it_and_its_young': 'fit', 'terefah': 'fit', 'caesarean': 'fit'}),
 ('Sifra Emor Chapter 3 6-7 / Eruvin 10:13 — the passed blemish', blemish('passed_blemish'), 'fit'),
 ('Sifra Emor Chapter 3 8-9 — the blemished eats', blemish('eats'), {'most_holy': 'eats', 'holy': 'eats', 'in_the_division': 'takes_a_share'}),
 ('Sifra Emor Chapter 3 10-11 — the veil and the altar', blemish('veil_altar'), {'veil': 'shall_not_come', 'altar': 'shall_not_draw_near', 'beaten_plates': 'may_enter'}),
 ('Sifra Emor Chapter 3 11 — the entry hierarchy', blemish('entry_hierarchy'), ['priests', 'levites', 'israelites', 'impure', 'blemished']),
 ('Sifra Emor Chapter 3 11 / Terumot 8:1 — served', blemish('served'), {'service': 'invalid', 'death': ['R._Yehuda_yes_by_profanation_profanation', 'sages_warning_only']}),
 ('Sifra Emor Chapter 3 12 — the transmission chain', blemish('transmission'), ['moses_to_aaron', 'aaron_to_his_sons', 'the_sons_to_israel', 'the_sons_to_each_other']),
 ('Bekhorot 7:2 — the bald', blemish('bald'), 'no_hair_line_ear_to_ear'),
 ('Sifra Emor Section 3 14 / Bekhorot 7:3 — the eye positions', blemish('eye_positions'), ['both_up', 'both_down', 'one_each', 'sees_room_and_loft', 'sun_hater', 'unmatched', 'the_dripping', 'lashes_fallen_for_appearance']),
 ('Bekhorot 7:4 — the proportions', blemish('proportions'), ['eyes_as_a_calf_or_a_goose', 'body_vs_limbs', 'nose_vs_limbs', 'small_ears', 'sponge_ears']),
 ('Sifra Emor Section 3 11 / Bekhorot 7:6 — fingers joined to the joint', blemish('fingers', joined_to='joint'), 'fit'),
 ('Sifra Emor Section 3 11 — fingers joined below', blemish('fingers', joined_to='below'), 'unfit'),
 ('Bekhorot 7:6 — the extra finger and the rest', blemish('extra_finger'), {'cut_with_bone': 'unfit', 'cut_without_bone': 'fit', 'six_and_six': ['R._Yehuda_fit', 'sages_unfit'], 'ambidextrous': ['Rabbi_unfit', 'sages_fit']}),
 ('Lev 21:17, 22:3, 24:3 — the generations clause once per file', blemish('dorot'), {'lev_21': [17], 'lev_22': [3], 'lev_24': [3]}),
 # ---- THE HOLY THINGS, THE EATERS, THE FIFTH (22:1-16) ----
 ('Sifra Emor Section 4 1 + Onkelos 22:2 — the separation', holy_food('separation'), 'separation_performed_by_onkelos'),
 ('Sifra Emor Section 4 1 — whose holy things', holy_food('whose_holy_things'), {'israels': 'liable', 'gentiles': 'not', 'priests_own': 'included'}),
 ('Lev 22:2 + 22:32 — the Name frames the chapter', holy_food('name_frame'), [2, 32]),
 ('Sifra Emor Section 4 2 — the chillul triple import', holy_food('chillul_import'), ['time', 'death', 'acceptance_dependence', 'R._Yehuda_karet_by_I_the_LORD']),
 ('Sifra Emor Section 4 5 — the karet extension', holy_food('karet_extension'), {'from': 'shelamim_only_at_7_20', 'to': 'all_holy_things', 'piggul_a_fortiori': 'refused_by_the_four_way_difference'}),
 ('Sifra Emor Section 4 7 — the readiness threshold', holy_food('readiness'), {'with_permitters': 'after_the_permitters_are_offered', 'without': 'after_vessel_sanctification'}),
 ('Sifra Emor Section 4 8 — body impurity', holy_food('body_impurity'), 'impurity_of_the_body_not_the_flesh_four_routes'),
 ('Lev 22:4 — the zav\'s tier (CALLED)', holy_food('zav_tier'), 'full_zav_with_offering'),
 ('Sifra Emor Chapter 4 2 — until pure = sunset', holy_food('until_pure'), 'sunset'),
 ('Sifra Emor Chapter 4 1 — the tithe and the tevul yom', holy_food('tithe_tevul_yom'), {'israelites_tithe': 'as_tevul_yom', 'aaron_and_sons_terumah': 'at_sunset'}),
 ('Sifra Emor Chapter 4 3-4 — the measures census', holy_food('measures'), {'corpse': 'contact_only', 'seed_emitter': 'included', 'toucher_of_semen': 'by_or_a_man', 'swarming_thing': 'included', 'carcass': 'by_or_a_man', 'zavim_zavot_niddot_yoldot': 'his_impurity', 'lies_with_a_niddah': 'who_becomes_impure', 'swallows_a_pure_birds_carcass': 'to_him'}),
 ('Sifra Emor Chapter 4 5 — touch not move', holy_food('touch_not_move'), 'touch_only_heset_excluded'),
 ('Sifra Emor Chapter 4 5-10 — the mixture grid', holy_food('mixture_grid'), 'one_in_a_hundred_both_directions'),
 ('Sifra Emor Chapter 4 7 — the whole body', holy_food('whole_body'), 'not_limb_by_limb'),
 ('Sifra Emor Chapter 4 8 / Chagigah 3:3 — the two gates', holy_food('two_gates'), {'sunset': 'gates_terumah', 'atonement_offering': 'does_not'}),
 ('Sifra Emor Chapter 4 11 — his bread', holy_food('his_bread'), 'raise_wheat_and_trim_vegetables_as_he_likes_trimmings_holy'),
 ('Sifra Emor Chapter 4 13 — the bird in the gullet', holy_food('gullet', animal='bird'), 'defiles_in_the_gullet'),
 ('Sifra Emor Chapter 4 12 — the beast in the gullet', holy_food('gullet', animal='beast'), 'does_not_defile_in_the_gullet'),
 ('Sifra Emor Chapter 4 14 + Onkelos 22:9 — the charge', holy_food('charge'), {'warned': 'the_court', 'bear_sin_over': 'the_holy_things_not_the_carcass', 'onkelos': 'receive_upon_it_a_debt'}),
 ('Sifra Emor Chapter 4 15 — die by it', holy_food('die_by_it'), {'deliberate_impure_eater': 'death_by_heaven', 'tithe': 'no', 'pure_eater_of_impure': 'no'}),
 ('Sifra Emor Chapter 4 16 — the stranger', holy_food('stranger'), {'who': 'levite_and_israelite_by_EVERY_stranger', 'eating': 'an_olive', 'holy': 'the_border_holy_things_terumah', 'seats': [10, 12, 13]}),
 ('Sifra Emor Chapter 4 17 — resident and hireling', holy_food('toshav_sachir'), {'toshav': 'acquired_forever_the_pierced_slave', 'sachir': 'acquired_for_years'}),
 ('Sifra Emor Chapter 4 18 / Yevamot 8:1 — the uncircumcised', holy_food('uncircumcised'), ['R._Yishmael_toshav_sachir_from_the_passover', 'R._Akiva_man_man']),
 ('Sifra Emor Section 5 1 / Yevamot 7:2 — the wife', holy_food('household', who='wife'), 'eats'),
 ('Sifra Emor Section 5 1 — the slaves\' slave', holy_food('household', who='slaves_slave'), 'eats'),
 ('Sifra Emor Section 5 2 — the Hebrew slave', holy_food('household', who='hebrew_slave'), 'no_money_in_him'),
 ('Sifra Emor Section 5 3 — the half-slave', holy_food('household', who='half_slave'), 'not_HIS_money'),
 ('Sifra Emor Section 5 4 — the worthless-born', holy_food('household', who='worthless_born'), 'eats'),
 ('Sifra Emor Section 5 6 — the animal', holy_food('household', who='animal'), 'vetch_only'),
 ('Sifra Emor Section 5 6 — the dead priest', holy_food('household', who='dead_priests_household'), 'nobody'),
 ('Sifra Emor Section 5 6 / Yevamot 7:5 — the son feeds the mother', holy_food('son_feeds_mother'), 'the_son_feeds_the_mother'),
 ('Sifra Emor Section 5 7-10 / Yevamot 6:3 — the daughter to a stranger', holy_food('daughter_to_stranger'), {'stranger': 'levite_israelite', 'to_a_man': 'to_one_who_feeds', 'forbidden_union': 'disqualifies_from_terumah', 'she_feeds': 'her_mother'}),
 ('Sifra Emor Section 6 1 — terumah vs holy things', holy_food('terumah_vs_holy'), {'holy_things': 'some_permitted_to_strangers_piggul_liability', 'terumah': 'never_permitted_no_piggul'}),
 ('Sifra Emor Chapter 5 1-5 + Chapter 6 1 / Yevamot 9:6 — the return', holy_food('return'), {'widow_and_divorcee': 'both_written_both_need_no_seed', 'no_seed': 'to_the_seeds_seed', 'unfit_seed': 'counts', 'maidservants_seed': 'not_hers', 'levirate_bound': 'not', 'pregnant': 'not', 'her_fathers_bread': 'terumah'}),
 ('Sifra Emor Chapter 5 3 / Yevamot 7:6 — the grandson high priest', holy_food('grandson_high_priest'), 'feeds_his_mother_disqualifies_his_grandmother'),
 ('Yevamot 9:5 — married to a priest', holy_food('eating_table', husband='priest'), 'terumah'),
 ('Yevamot 9:5 — married to a Levite', holy_food('eating_table', husband='levite'), 'tithe'),
 ('Yevamot 9:5 — married to an Israelite', holy_food('eating_table', husband='israelite'), 'neither'),
 ('Yevamot 9:6 — her son from the Israelite died: she returns', holy_food('eating_table', husband='israelite', son_alive=False, after='fathers_house'), 'terumah_returns'),
 ('Yevamot 9:5 — her son from the Levite died: back to terumah', holy_food('eating_table', husband='levite', son_alive=False, after='priest'), 'terumah'),
 ('Yevamot 9:4 — the betrothed does not eat', holy_food('stage', stage='betrothed'), 'does_not_eat'),
 ('Yevamot 7:4 — the levirate-bound does not eat', holy_food('stage', stage='levirate_bound'), 'does_not_eat'),
 ('Yevamot 7:4 — the nine-and-a-day', holy_food('stage', stage='nine_and_a_day'), 'does_not_eat'),
 ('Lev 22:11 — the married wife eats', holy_food('stage', stage='married'), 'eats'),
 ('Yevamot 7:3-4 — the fetus', holy_food('fetus'), 'disqualifies_does_not_feed'),
 ('Yevamot 7:1 — the forbidden wife\'s iron-flock slaves', holy_food('slaves_of_forbidden_wife', type='iron_flock'), 'eat'),
 ('Yevamot 7:1 — her usufruct slaves', holy_food('slaves_of_forbidden_wife', type='usufruct'), 'do_not_eat'),
 ('Sifra Emor Chapter 5 4-5 / Yevamot 7:5 — rapist, seducer, fool, slave, mamzer', holy_food('rapist_seducer_fool'), {'fit': 'neither_disqualify_nor_feed', 'unfit_to_enter': 'disqualify', 'slave': 'disqualifies_by_intercourse_not_seed', 'mamzer': 'disqualifies_and_feeds'}),
 ('Yevamot 8:1 — the crushed priest', holy_food('crushed_priest'), {'he_and_his_slaves': 'eat', 'his_wives': 'do_not_eat', 'wife_from_before': 'eats'}),
 ('Yevamot 8:6 — the eunuch priest feeds', holy_food('eunuch_priest'), {'sun_eunuch': 'feeds_his_wife', 'androgynos': 'R._Yosei_R._Shimon_feeds', 'tumtum_torn_male': 'R._Yehuda_as_a_eunuch'}),
 ('Lev 22:14 — the fifth\'s algebra (CALLED)', holy_food('fifth_algebra'), 'repay the principal to the fund struck; add the fifth (25.00); ram at the valuation floor (two sela (Mishnah Keritot 5:2; Zevachim 10:5 class))'),
 ('Lev 22:14 + 27:31 — the spelling\'s two seats', holy_food('fifth_spelling'), [('Lev', 22, 14), ('Lev', 27, 31)]),
 ('Terumot 6:1, 7:4 — the erring eater', holy_food('error_gate', deliberate=False), {'principal': 'pays', 'fifth': 'adds', 'payment': 'becomes_terumah_priest_cannot_forgive'}),
 ('Terumot 7:1 — the deliberate eater (CALLED)', holy_food('error_gate', deliberate=True), {'principal': 'pays', 'fifth': 'no', 'payment': 'common_priest_may_forgive', 'death': 'by_heaven_if_impure_eater'}),
 ('Sifra Emor Chapter 6 2-3, 6 8 / Terumot 7:2-3 — the fifth\'s gates', holy_food('fifth_gates'), {'non_strangers': 'exempt', 'minor': 'exempt_nine_and_a_day_a_man', 'less_than_olive': 'exempt', 'terumah_abroad': 'exempt', 'eater_drinker_anointer': 'all_liable'}),
 ('Sifra Emor Chapter 6 5 / Terumot 6:5 — the payment material', holy_food('payment_material'), {'R._Meir': 'fit_to_become_holy_not_gleanings_corner_ownerless', 'sages': 'from_all'}),
 ('Sifra Emor Chapter 6 6 / Terumot 6:6 — kind for kind', holy_food('kind_for_kind'), {'R._Akiva': 'kind_for_kind_wait_for_the_cucumbers', 'R._Eliezer': 'any_kind_better_for_worse'}),
 ('Terumot 6:2 — the two payees', holy_food('two_payees'), {'principal': 'to_the_owner', 'fifth': 'to_any_priest'}),
 ('Terumot 6:3 — the workers', holy_food('workers'), {'R._Meir': 'he_the_principal_they_the_fifth', 'sages': 'they_both_he_their_meal'}),
 ('Terumot 6:4 — the thief', holy_food('thief'), {'not_eaten': 'double_of_the_terumahs_value', 'eaten': 'two_principals_and_a_fifth', 'consecrated_terumah_eaten': 'two_fifths_and_a_principal_no_double'}),
 ('Terumot 7:2 — the daughter who ate', holy_food('daughter_who_ate'), {'R._Meir': {'to_israelite': 'principal_no_fifth_burning', 'to_disqualified': 'principal_and_fifth_strangling'}, 'sages': 'both_principal_no_fifth_burning'}),
 ('Terumot 8:1 — the eater who learns', holy_food('learns'), {'wife_or_slave_told': ['R._Eliezer_principal_and_fifth', 'R._Yehoshua_exempt'], 'chalal_serving': ['R._Eliezer_invalid', 'R._Yehoshua_valid'], 'found_blemished': 'service_invalid'}),
 ('Terumot 8:2 — terumah in the mouth', holy_food('in_the_mouth'), {'told_now_impure': ['R._Eliezer_swallow', 'R._Yehoshua_spit'], 'was_impure_or_tevel_or_a_bug': 'spit_out'}),
 ('Terumot 8:11 = Sifra Emor Chapter 6 10 — the warning\'s object', holy_food('warning_object'), 'eating_not_defiling'),
 ('Sifra Emor Chapter 6 9-10 + Onkelos 22:16 — the profaners', holy_food('profaners'), {'raised_not_untithed': True, 'death_even_on_tevel': True, 'sower_and_defiler': 'excluded', 'onkelos': 'in_impurity_inserted'}),
 ('Lev 22:16 — the asham homograph', holy_food('asham_homograph'), 'the_noun_guilt_not_the_offering'),
 ('Lev 22 — the eating verb fourteen times', holy_food('eat_count'), 14),
 # ---- THE ACCEPTABLE ANIMAL (22:17-33) ----
 ('Sifra Emor Section 7 1-2 / Shekalim 1:5 — the vow class', acceptable('vow_class'), {'gentiles': 'vow_and_offer_freely', 'widened_by_all': ['shelamim', 'todah', 'birds', 'meal_offerings', 'wine', 'frankincense', 'wood'], 'nazirite': 'excluded', 'public': 'not_compelled'}),
 ('Sifra Emor Section 7 2 — whole and male: beasts not birds', acceptable('whole_male'), {'beasts': 'whole_and_male', 'birds': 'not_whole_not_male_but_not_the_maimed'}),
 ('Lev 22:18 — the burnt offering\'s rite (CALLED)', acceptable('olah_rite'), 'wholly_to_fires'),
 ('Lev 22:21 — the peace offering\'s window (CALLED)', acceptable('shelamim_window'), 'two_days_one_night'),
 ('Lev 22 — the acceptance root at seven seats', acceptable('acceptance_seats'), [19, 20, 21, 23, 25, 27, 29]),
 ('Sifra Emor Section 7 3 — the passing blemish', acceptable('passing_blemish'), 'included'),
 ('Sifra Emor Section 7 4, Chapter 7 1, 7 10 — one verb, three jobs', acceptable('two_jobs'), {'22:20': 'bal_takdish_consecrating', '22:22': 'bal_tishchat_slaughtering', '22:24': 'bal_tekabel_receiving_R._Yosei_b._R._Yehuda'}),
 ('Sifra Emor Section 7 5 — the five-count', acceptable('five_count'), {'sages': 5, 'R._Yosei_b._R._Yehuda': 6, 'acts': ['consecrate', 'slaughter', 'throw', 'burn_fat', 'burn_part', 'receive']}),
 ('Sifra Emor Section 7 6-7 — the individual, the partners, the public', acceptable('individual_public'), {'individual': 'freewill_shelamim', 'partners': 'included_by_the_vav', 'public': 'excluded'}),
 ('Sifra Emor Section 7 8 + Onkelos 22:21 — the class sweep', acceptable('class_sweep'), ['burnt_offering', 'todah', 'yoledet_and_nazirite', 'sin_and_guilt', 'tithe', 'offspring_and_substitutes']),
 ('Sifra Emor Section 7 9 — positive and negative; fell and broke', acceptable('positive_negative'), {'whole_for_acceptance': 'positive', 'no_blemish_in_it': 'negative', 'fell_and_broke': 'no_transgression'}),
 ('Sifra Emor Section 7 10 — the blood-rush firstling', acceptable('blood_rush'), {'R._Yehuda': 'no_bloodletting', 'sages': 'let_blood_no_blemish', 'R._Shimon': 'even_the_blemish_if_it_saves'}),
 ('Lev 22:22 — the six class heads', acceptable('beast_heads'), ['blind', 'broken', 'charutz', 'wart', 'garav', 'yalefet']),
 ('Sifra Emor Section 7 11 / Bekhorot 6:5 — broken = the tail', acceptable('beast_members', head='broken'), ['the_tail_not_a_rib', 'visible_non_healing']),
 ('Sifra Emor Section 7 12 / Bekhorot 6:1-4 + Onkelos 22:22 — charutz', acceptable('beast_members', head='charutz'), ['eyelid_pierced_notched_split', 'lip_likewise', 'outer_teeth_notched_inner_uprooted', 'not_from_the_molars_inward']),
 ('Bekhorot 6:12 — garav the curable form', acceptable('beast_members', head='garav'), ['the_dry_scab_the_curable_form_no_slaughter']),
 ('Sifra Emor Section 7 13 — the cross-list transfer', acceptable('cross_list'), {'to_the_beast': ['dak', 'tevallul'], 'to_the_man': ['wart'], 'by': ['garav_garav', 'yalefet_yalefet']}),
 ('Sifra Emor Chapter 7 2-3 — worked with: permitted', acceptable('worked_with'), 'permitted'),
 ('Sifra Emor Chapter 7 4 — the four-token assignment', acceptable('four_tokens'), {'a_fire_offering': 'the_fats', 'of_them': 'even_part', 'on_the_altar': 'the_blood', 'to_the_LORD': 'the_dispatched_goat'}),
 ('Zevachim 8:5 — the blemished limb', acceptable('blemished_limb'), {'R._Eliezer': 'if_one_head_offered_all_heads', 'sages': 'to_the_burning_place'}),
 ('Zevachim 8:8 — the blemished blood', acceptable('blemished_blood'), 'poured_to_the_channel'),
 ('Sifra Emor Chapter 7 6 + Onkelos 22:23 / Bekhorot 6:7 — sarua and kalut', acceptable('sarua_kalut'), {'sarua': 'dislocated_hip', 'kalut': 'hoof_like_a_horse_or_donkey', 'onkelos': 'extra_and_lacking'}),
 ('Sifra Emor Chapter 7 6-8 / Shekalim 4:8 — for upkeep, not the altar', acceptable('upkeep'), {'freewill_or_vow': 'temple_upkeep', 'the_altar': 'not_accepted', 'whole_animal_for_upkeep': ['positive_transgression', 'R._Yehuda_negative_too']}),
 ('Sifra Emor Chapter 7 9, 7 11-12 / Yevamot 8:2 — the castration ban', acceptable('castration'), {'anatomies': ['R._Yehuda_testicles', 'R._Eliezer_member', 'R._Yosei_two_and_two'], 'do_not_do': 'not_only_offer', 'birds': 'included', 'abroad': 'included', 'humans': 'by_revocalization_and_in_you', 'females': ['included', 'R._Yehuda_not']}),
 ('Sifra Emor Chapter 7 12 / Shekalim 1:5 — no shekels from gentiles', acceptable('no_shekels'), {'shekels': 'not_accepted', 'vows': 'accepted', 'blemished_from_gentiles': 'not_accepted'}),
 ('Lev 22:25 / Temurah 6:1 — the corruption class', acceptable('corruption'), ['copulator', 'copulated', 'set_aside', 'worshipped', 'hire', 'price', 'hybrid', 'terefah', 'caesarean']),
 ('Temurah 6:1 / Zevachim 8:1 — in any amount', acceptable('any_amount'), 'forbid_in_any_amount'),
 ('Temurah 6:5 — the offspring', acceptable('offspring'), {'offspring': 'permitted', 'terefahs_offspring': ['R._Eliezer_not', 'sages_offered'], 'holy_become_terefah': 'not_redeemed'}),
 ('Zevachim 9:3 — the blemished descends', acceptable('descends'), {'sages': 'descends', 'R._Akiva': 'the_blemished_stays'}),
 ('Sifra Emor Section 8 1-2 — not a human', acceptable('not_a_human'), 'an_ox_when_born_not_a_human'),
 ('Sifra Emor Section 8 3 — the birth list', acceptable('birth_list'), {'hybrid': 'ox_or_sheep', 'look_alike': 'or_goat', 'caesarean': 'when_born', 'under_age': 'seven_days', 'orphan': 'under_its_mother', 'tithe': 'all_these_by_under_under'}),
 ('Sifra Emor Section 8 4 — one hour with the mother', acceptable('one_hour'), 'alive_with_the_mother_one_hour_suffices'),
 ('Sifra Emor Section 8 5 — the eighth-day join (the OWED of L5, closed at E1)', acceptable('eighth_day'), {'here': 'from_the_eighth_day_onward', 'firstling_exod_22_29': 'on_the_eighth_day', 'join': 'both_by_its_mother_its_mother'}),
 ('Exod 22:29 by live call — the firstling\'s eighth day and onward (E1 compiled the callee)', acceptable('eighth_day_by_call'), 'on_the_eighth_day_and_onward'),
 ('Sifra Emor Section 8 6 — accepted for the fire', acceptable('accepted_for'), {'the_fire': 'accepted', 'upkeep': 'by_for_an_offering', 'dispatched_goat': 'under_age_barred'}),
 ('Zevachim 14:2 — the under-age offered outside', acceptable('under_age_outside'), {'blemished_outside': 'exempt', 'under_age_outside': ['exempt', 'R._Shimon_a_prohibition_without_karet']}),
 ('Sifra Emor Section 8 8-10 — not wild, not bird, either one', acceptable('not_wild_not_bird'), {'wild': 'excluded_by_ox', 'bird': 'excluded_by_sheep', 'either_one': 'or_sheep'}),
 ('Sifra Emor Chapter 8 1 + Onkelos 22:28 — the female rule', acceptable('female_rule'), {'males': 'not_as_females', 'by': 'its_young_that_follows_it', 'onkelos': 'a_cow_or_a_ewe_HER_and_HER_young'}),
 ('Sifra Emor Chapter 8 2 — it and its mother', acceptable('it_and_its_mother'), 'two_by_the_plural_you_shall_not_slaughter'),
 ('Chullin 5:3 — the cow then her two young', acceptable('order_cases', seq='cow_then_two_young'), 80),
 ('Chullin 5:3 — her two young then the cow', acceptable('order_cases', seq='two_young_then_cow'), 40),
 ('Chullin 5:3 — her, her daughter, her granddaughter', acceptable('order_cases', seq='her_daughter_granddaughter'), 80),
 ('Chullin 5:3 — the middle one last', acceptable('order_cases', seq='her_granddaughter_then_daughter'), [40, 'Sumchos_80']),
 ('Chullin 5:1 — common outside', acceptable('cells', kind='common', place='outside', order='mother_first'), {'first': 'valid_exempt', 'second': 'flogged', 'validity': 'both_valid'}),
 ('Chullin 5:1 — consecrated outside', acceptable('cells', kind='consecrated', place='outside', order='mother_first'), {'first': 'karet', 'second': 'flogged', 'validity': 'both_invalid_both_flogged'}),
 ('Chullin 5:1 — common inside', acceptable('cells', kind='common', place='inside', order='mother_first'), {'first': 'invalid_exempt', 'second': 'flogged', 'validity': 'both_invalid'}),
 ('Chullin 5:1 — consecrated inside', acceptable('cells', kind='consecrated', place='inside', order='mother_first'), {'first': 'valid_exempt', 'second': 'flogged', 'validity': 'second_invalid'}),
 ('Chullin 5:1 — everywhere', acceptable('everywhere'), {'land': 'yes', 'abroad': 'yes', 'with_the_house': 'yes', 'without': 'yes', 'common': 'yes', 'consecrated': 'yes'}),
 ('Sifra Emor Chapter 8 5-6 / Chullin 5:3 — the slaughter verb', acceptable('slaughter_verb'), {'became_a_carcass': 'exempt', 'stabber_tearer': 'exempt', 'for_gentiles_or_dogs': 'included', 'terefah_idolatry_red_cow_stoned_ox_heifer': ['R._Meir_liable', 'R._Shimon_exempt']}),
 ('Sifra Emor Chapter 8 8 / Chullin 5:3 — the four periods', acceptable('four_periods'), {'periods': ['eve_of_the_last_day_of_sukkot', 'eve_of_the_first_of_passover', 'eve_of_atzeret', 'eve_of_rosh_hashanah', 'R._Yosei_HaGelili_eve_of_yom_kippur_in_the_galilee'], 'seller': 'must_inform', 'R._Yehuda': 'only_without_an_interval', 'groom_and_bride': 'agreed'}),
 ('Sifra Emor Chapter 8 9 / Chullin 5:4 — the compelled butcher', acceptable('compelled_butcher'), {'compelled': True, 'died_in_the_periods': 'the_buyers_loss', 'rest_of_the_year': 'the_sellers'}),
 ('Sifra Emor Chapter 8 9 / Chullin 5:5 — the day after the night', acceptable('day_boundary'), 'the_day_follows_the_night'),
 ('Sifra Emor Chapter 9 1-2 — the reassignment', acceptable('reassignment'), {'eating_clause': 'redundant_for_eating_Lev_7_15', 'reassigned_to': 'slaughter_on_condition_of_eating_within_the_day', 'scope': 'all_one_day_offerings'}),
 ('Lev 22:30 — the thanksgiving\'s window (CALLED)', acceptable('todah_window'), 'day_night_to_midnight'),
 ('Sifra Emor Chapter 9 3 — keep and do', acceptable('keep_and_do'), {'keep': 'mishnah', 'do': 'deed', 'not_in_mishnah': 'not_in_deed'}),
 ('Sifra Emor Chapter 9 4-5 — the Name sanctified', acceptable('sanctify_name'), {'hand_yourself_over': True, 'among': 'the_many', 'on_condition_of_a_miracle': 'none'}),
 ('Sifra Emor Chapter 9 6 — the Exodus condition', acceptable('exodus_condition'), 'on_condition_that_you_hand_yourselves_over'),
 ('Lev 21-22 — "I am the LORD" at thirteen seats', acceptable('ani_seats'), {'lev_21': [8, 12, 15, 23], 'lev_22': [2, 3, 8, 9, 16, 30, 31, 32, 33]}),
 ('Bekhorot 6:11-12 — the firstling\'s table', acceptable('firstling_table'), {'slaughter_on': 'the_permanent_blemishes', 'not_on': 'the_passing_the_old_the_sick_the_foul_the_sinned_with_the_killer_the_doubtful_sex', 'disqualified_consecrated': 'redeemed_on_the_same'}),
 ('Bekhorot 6:3 — the cataract timer', acceptable('cataract_timer'), {'permanent_cataract': 'eighty_days', 'R._Chanina': 'examined_three_times', 'permanent_water': 'dry_after_moist'}),
 ('Bekhorot 6:1 — the ear', acceptable('ear'), {'notched_from_the_cartilage': 'blemish', 'from_the_skin': 'not', 'pierced_a_vetch': 'blemish', 'dried': 'no_drop_of_blood'}),
 ('Bekhorot 6:6 — the testicles', acceptable('testicles'), {'none_or_one': 'blemish', 'R._Yishmael': 'two_sacs_two', 'R._Akiva': 'press_it', 'case': ['R._Akiva_permitted', 'R._Yochanan_b._Nuri_forbade']}),
 ('Bekhorot 6:8-9 — the recorded accretion', acceptable('accretion'), {'ila_at_yavneh': 'agreed', 'his_three_more': 'the_later_court_accepted', 'jaw_and_ear_and_tail': 'ruled_case_by_case'}),
 # ---- THE LAMP AND THE TABLE (24:1-9) ----
 ('Exod 27:20 restated at Lev 24:2', lamp_table('restatement'), {'shared_tail': 13, 'of': 14, 'opening_verb': 'command_for_and_you_shall_command'}),
 ('Sifra Emor Section 13 1 — command; you the treasurer', lamp_table('command'), {'command': 'urging_now_and_for_generations', 'R._Shimon': 'where_there_is_monetary_loss', 'take_to_you': 'you_the_treasurer'}),
 ('Sifra Emor Section 13 1-3 / Menachot 8:4 — the three olives', lamp_table('oil'), {'olive': 'not_sesame_nut_radish', 'three_olives': ['treetop', 'roof', 'pressed_and_dried'], 'three_flows': ['crushed_in_the_basket', 'under_the_beam', 'ground_again'], 'for_the_menorah': 'the_first_of_each'}),
 ('Sifra Emor Section 13 5 / Menachot 8:5 — the nine grades', lamp_table('nine_grades'), ['1of1', '2of1=1of2', '3of1=2of2=1of3', '3of2=2of3', '3of3']),
 ('Sifra Emor Section 13 6 — beaten for the light only (CALLED)', lamp_table('beaten_scope'), {'for_the_light': 'required', 'meal_offerings': 'not_required_pure_beaten'}),
 ('Sifra Emor Section 13 4 — R. Yehuda\'s method', lamp_table('R_Yehuda_method'), ['crushed_in_a_mortar_not_a_mill', 'stones_not_the_beam', 'around_the_basket_not_in_it']),
 ('Lev 24 — pure written four times', lamp_table('pure_tokens'), {'oil_and_frankincense': [2, 7], 'menorah_and_table': [4, 6]}),
 ('Sifra Emor Section 13 7 / Tamid 3:9 — the western lamp', lamp_table('western_lamp'), {'flame': 'rises_on_its_own', 'western': 'always_burning_begin_from_it_end_at_it', 'found_out': ['Sifra_relight_from_the_outer_altar', 'Tamid_from_the_burning_lamps']}),
 ('Lev 24 — continually four times', lamp_table('continually'), {'seats': [2, 3, 4, 8], 'means': ['even_on_the_sabbath', 'even_in_impurity']}),
 ('Sifra Emor Section 13 8 — the position', lamp_table('position'), 'nearer_the_veil_than_the_entrance'),
 ('Exod 27:21 vs Lev 24:3 — "and his sons" dropped', lamp_table('one_priest'), {'exod_27_21': 'aaron_and_his_sons', 'lev_24_3': 'aaron', 'staffing': 'one_priest_arranges_seven_lamps'}),
 ('Sifra Emor Section 13 11 — evening to morning', lamp_table('evening_to_morning'), {'measure': 'enough_to_burn_evening_to_morning', 'exclusive': 'no_other_service_in_that_interval'}),
 ('Tamid 3:9 — found the two eastern lamps burning', lamp_table('tending', found='two_eastern_burning'), 'clear_the_rest_leave_them_burning'),
 ('Tamid 3:9 — found them out', lamp_table('tending', found='out'), 'clear_and_light_from_the_burning_ones_then_the_rest'),
 ('Sifra Emor Chapter 18 1 — wheat bought', lamp_table('wheat_bought'), {'wheat': 'may_be_bought_for_this', 'other_meal_offerings': 'not_as_wheat'}),
 ('Lev 24:5 / Sifra Emor Chapter 18 2 / Menachot 11:1 — the loaves', lamp_table('loaves'), {'count': 12, 'each': 'two_tenths', 'equal': True, 'kneaded': 'one_by_one', 'baked': 'two_at_a_time', 'molds': 3}),
 ('Lev 24:6 / Sifra Emor Chapter 18 3 — two rows of six by three verses', lamp_table('arrangement'), {'rows': 2, 'per_row': 6, 'pinned_by': 'three_verses'}),
 ('Sifra Emor Chapter 18 4, 18 8 / Menachot 11:6 — the props and reeds', lamp_table('props_reeds'), {'golden_props': 4, 'reeds': 28, 'per_row': 14, 'lie': 'lengthwise_with_the_house', 'except': 'the_ark'}),
 ('Sifra Emor Chapter 18 5 — both rows', lamp_table('both_rows'), 'both_rows_by_row_row'),
 ('Sifra Emor Chapter 18 6 / Menachot 5:3, 3:6 — the frankincense', lamp_table('frankincense'), {'pure': 'clear', 'status': 'an_obligation_to_the_bread_indispensable_renders_piggul', 'where': 'two_dishes_with_rims_not_on_the_bread', 'oil': 'none'}),
 ('Menachot 11:5 — the dishes\' place disputed', lamp_table('dishes_place'), {'sages': 'ON_the_row', 'Abba_Shaul': 'BESIDE_by_Num_2_20'}),
 ('Lev 24:7 — the memorial (CALLED)', lamp_table('memorial'), 'a_fistful'),
 ('Lev 24:9 / Zevachim 9:5, Menachot 5:6 — not the fire\'s (CALLED)', lamp_table('not_the_fires'), 'to_priests_none_to_altar'),
 ('Lev 24:8 / Sifra Emor Chapter 18 8-9 — the Sabbath exchange', lamp_table('sabbath_exchange'), {'doubled': 2, 'new': 'arranged_on_the_sabbath', 'old': 'burned_on_the_sabbath', 'reeds': 'removed_friday_not_set_on_the_sabbath', 'after': 'three_under_each_two_under_the_top'}),
 ('Menachot 11:7 — the exchange protocol', lamp_table('exchange_protocol'), {'in': 'four_priests_two_rows_two_dishes', 'out': 'four_before_them', 'stand': 'enterers_north_removers_south', 'continually': 'ones_handbreadth_against_the_others', 'R._Yosei': 'even_take_then_place'}),
 ('Menachot 11:8 — the invalid arrangements', lamp_table('invalid_arrangements'), {'bread_on_sabbath_dishes_after': 'invalid_no_piggul', 'both_on_sabbath_burned_after': 'invalid', 'both_after_burned_on_sabbath': 'invalid', 'remedy': 'leave_it_for_the_coming_sabbath'}),
 ('Menachot 11:9 — the window: nine', lamp_table('window', case='plain'), 9),
 ('Menachot 11:9 — a festival on Friday: ten', lamp_table('window', case='festival_on_friday'), 10),
 ('Menachot 11:9 — Rosh Hashanah\'s two days: eleven', lamp_table('window', case='two_days_rosh_hashanah'), 11),
 ('Sifra Emor Chapter 18 9 — the covenant', lamp_table('covenant'), {'from_the_children_of_israel': 'by_their_consent', 'eternal_covenant': 'from_Him_whose_it_is'}),
 ('Sifra Emor Chapter 18 10-11 / Menachot 11:2 — the eating', lamp_table('eating'), {'place': 'a_holy_place', 'kneading_shaping': ['holy_place_too', 'R._Yehuda_all_inside', 'R._Shimon_valid_at_beit_pagi'], 'one_broken': 'all_disqualified', 'aaron': 'without_division', 'sons': 'in_division', 'after': 'the_fires_gift'}),
 ('Menachot 11:4-5 — the dimensions', lamp_table('dimensions'), {'loaf': 'ten_by_five_horns_seven', 'table': ['R._Yehuda_ten_by_five', 'R._Meir_twelve_by_six'], 'faces': 'ben_Zoma_from_Exod_25_30'}),
 ('Menachot 11:7 — the two tables', lamp_table('two_tables'), {'marble': 'at_entry', 'gold_in_the_porch': 'at_exit', 'gold_inside': 'the_bread_continually', 'rule': 'raise_in_holiness_never_lower'}),
 ('Tamid 3:3 — the showbread chamber', lamp_table('workshop'), 'the_showbread_chamber_northwest'),
 ('Menachot 6:7 — the sieves', lamp_table('sieves'), {'showbread': 11, 'two_loaves': 12, 'omer': 13, 'R._Shimon': 'no_number'}),
 ('Lev 24:3, 24:8, 24:9 — the three perpetual clauses', lamp_table('close'), {'24:3': 'an_eternal_statute', '24:8': 'an_eternal_covenant', '24:9': 'an_eternal_statute'}),
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
print('effects: every cell carries REGISTERED effects — NINE discovered in these verses\' own verbs: defiled_for_kin, profaned_seed, terumah_fed (STATUS), '
      'blemish_barred, stranger_barred, same_day_slaughter_barred (BLOCK), eighth_day_fit, lamp_arranged, bread_set_weekly (TIMER) [effects law satisfied]')
_W.print_coverage()
if ok == n:
    print('THE PRIESTHOOD AND ITS DUES COMPILE — the six relatives on six tokens, the razor and the daughter\'s burning by call, the blemish census on twelve '
          'class heads with three tokens shared exactly by the animal\'s list, the zav and the fifth by call, the eaters\' file on the feeder predicate, the '
          'acceptable animal with the hapax "and from the day" and the Torah\'s only "on one day", the lamp as Exod 27:20 restated with one token dropped, the '
          'table\'s memorial by call; the holiness, sanctions, clocks, Lev 5, offering, and meal-offering engines CALLED.')
else:
    print('MISSES (%d):' % len(misses))
    for m_ in misses: print('  -', m_[0][:80], '->', m_[1])
    sys.exit('MISSES REMAIN — consult the Talmud per gap and recompile.')

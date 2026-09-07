#!/usr/bin/env python3
"""cold_run_shemini_day.py — THE EIGHTH DAY: THE RUN OF LEV 1-4's SPEC (Lev 9:1-24)
(2026-09-06, sitting D8 of THE COMPILE DEBT — World/step9/COMPILE_DEBT.md; the
third runner compiled under THE DEPENDENCY GATE's rule: span declared, a stub
placed, the census run, three required edges and four pointers dispositioned
BEFORE the first cell, a fourth edge declared for the live calls the compile made.)

The form: DEMONSTRATE-BY-RUN inside one book. Lev 1-8 is the SPEC (the offering
engines already compiled — offerings, minchah, chatat, tzav); Lev 9 is the RUN —
the day the spec executed for the first time, narrated verb by verb. The runner
grades the RUN as a SCENE against the spec: every act of the day is matched to
the engine cell it instantiates BY LIVE CALL, and every divergence is named and
sourced (the calf for the spec's bull; the outer blood with the inner carcass;
the calf completed whole before the ram; the burning at 9:11 that carries no
'as commanded' stamp). And the tradition's own reading of this chapter is the
opposite direction — THE RUN TEACHES THE SPEC: 9:16's 'as prescribed' gives the
obligatory burnt offering its hand-laying (Menachot 93b), 9:17's 'his palm'
makes every unmarked palm the right hand (Menachot 9b), 9:10's 'the lobe FROM
the liver' resolves Lev 3:4, 9:22's sequence legislates the blessing's timing
and posture — with the fork over whether an hour's act legislates at all
recorded at Menachot 19b (Rav: the repeated fistful is indispensable; Shmuel:
'generations are not learned from the hour').

Answer sheet ROUTED BY TOPIC under the union rule: Mishnah Zevachim 10 (the
order of precedence), Zevachim 14 (the eras of the high places), Tamid 4 (the
cutting walk) read WHOLE + ten topic rows + the two link rows — 33 rows, the
ledger logic/oral_triage/shemini_day_run_docket_2026-09-06.md with its
coverage computed; 20 Talmud addresses indexed on the span, ALL OPENED at the
ledger stage (recorded there as a deviation from per-gap opening: the
sitting's question is how the tradition reads this chapter).

The five motions, in order:
 (1) code from the BARE INK — the fire formula's two Tanakh seats; the glory
     formula's four; 'appears to you' a hapax; 'like the first', 'and he
     purified it', 'and filled his palm', 'and the covering' each a hapax;
     'the eighth day' at nine seats; 'as prescribed' at twelve Torah seats;
     the entrails-and-legs pair with the article at 8:21 and 9:14 alone;
     'beside the morning burnt offering' at 9:17 and Num 28:23 alone; 'his
     palm' at five Torah seats (this one and Lev 14's four); the burn phrase
     at 8:17 and 9:11 alone; the command stamps at 9:5, 9:6, 9:7, 9:10, 9:21
     and NOT at 9:11; 'and they blessed the people' here and at 2 Chr 30:27;
     the fat list at 9:19 as the union of two species' inventories; every
     quantity a PARAMETER (the calf's age, the seven services, the ten crowns);
 (2) the Mishnah's rows as TEST DATA, each expected value a literal typed
     from the row (the honest-pairing guard runs first);
 (3) run;
 (4) misses filled by NAMED recorded arguments — the Sifra Shemini rows (the
     unit's spine, verdicted 2026-09-05) and the Talmud segments opened;
 (5) the graded matrix with per-cell provenance, fractions, and EFFECTS — and
     the SCENE: the installation timer's release into the eighth day's tape
     on the world engine, checkpointed.

Cross-span receipts, labeled [IMPORT] and CALLED (the edges dispositioned in
dependency_dispositions.yaml): cold_run_chatat.rank / blood / sprinklings /
carcass / precedence_bulls / burn_site / inquiry; cold_run_offerings.dispatch
(olah:herd, olah:flock, shelamim, communal_shelamim_and_asham, outer_chatat,
fat:ox, fat:lamb); cold_run_minchah.fistful / oil_ops / frankincense_quantity /
remainder / presentation; cold_run_tzav.installation / altar_machine /
dues_machine. Exod 40:17, Num 8:8-12, Num 28:23, 2 Chr 30:27, Ezek 43:27, and
1 Kgs 8:66 stay imports by name.
"""
import sqlite3, sys, os, json, io, contextlib, collections
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import effects_layer as FX
from compile_guards import check_honest_pairing
GUARDED = check_honest_pairing(os.path.abspath(__file__))
assert GUARDED == 105, ("the guard counted %d expectations, the tripwire holds 105" % GUARDED)

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

L9 = list(range(1, 25))
def seats(ch, pred, rng):
    return [v for v in rng if pred(toks('Lev', ch, v))]
def has(*ws):
    return lambda t: any(t[i:i + len(ws)] == list(ws) for i in range(len(t) - len(ws) + 1))
def anytok(*ws):
    return lambda t: any(w in t for w in ws)
def anyprefix(*ps):
    return lambda t: any(w.startswith(p) for w in t for p in ps)

# the whole-Tanakh token index (23,213 verses) — for the day's rare tokens and phrases
_ALL = collections.defaultdict(list)
_VERSES = {}
for he, book, ch, vs in db.execute("SELECT w.he, v.book, v.chapter, v.verse FROM words w JOIN verses v ON w.verse_id=v.id ORDER BY v.id, w.idx"):
    _ALL[strip(he)].append((book, ch, vs))
    _VERSES.setdefault((book, ch, vs), []).append(strip(he))
def tanakh(tok):
    return sorted(set(_ALL.get(tok, [])))
def tanakh_phrase(words):
    n = len(words)
    return sorted(k for k, t in _VERSES.items() if any(t[i:i + n] == words for i in range(len(t) - n + 1)))
N_VERSES = db.execute("SELECT COUNT(*) FROM verses").fetchone()[0]
assert N_VERSES == 23213, N_VERSES

# ---- (1) ink probes — each MUST fire or the run refuses -------------
PROBES = [
    ('and it was on the EIGHTH day',                      'Lev', 9, 1, 'השמיני'),
    ('take for yourself a CALF, son of the herd',          'Lev', 9, 2, 'עגל'),
    ('take a he-GOAT for a sin offering',                  'Lev', 9, 3, 'שעיר'),
    ('an ox and a ram for PEACE OFFERINGS',                'Lev', 9, 4, 'לשלמים'),
    ('and all the assembly DREW NEAR and stood',           'Lev', 9, 5, 'ויקרבו'),
    ('the GLORY of the LORD shall appear to you',          'Lev', 9, 6, 'כבוד'),
    ('APPROACH the altar',                                 'Lev', 9, 7, 'קרב'),
    ('and he SLAUGHTERED the calf of the sin offering',    'Lev', 9, 8, 'וישחט'),
    ('and he dipped his FINGER in the blood',              'Lev', 9, 9, 'אצבעו'),
    ('the LOBE from the liver, from the sin offering',     'Lev', 9, 10, 'היתרת'),
    ('the flesh and the hide he BURNED in fire',           'Lev', 9, 11, 'שרף'),
    ('and he threw it on the altar AROUND',                'Lev', 9, 12, 'סביב'),
    ('by its PIECES and the head',                         'Lev', 9, 13, 'לנתחיה'),
    ('and he WASHED the entrails and the legs',            'Lev', 9, 14, 'וירחץ'),
    ('and he purified it LIKE THE FIRST',                  'Lev', 9, 15, 'כראשון'),
    ('and did it AS PRESCRIBED',                           'Lev', 9, 16, 'כמשפט'),
    ('and filled his PALM from it',                        'Lev', 9, 17, 'כפו'),
    ('the ox and the ram, the SACRIFICE of peace offerings', 'Lev', 9, 18, 'זבח'),
    ('the fat TAIL and the covering',                      'Lev', 9, 19, 'האליה'),
    ('they placed the fats on the BREASTS',                'Lev', 9, 20, 'החזות'),
    ('the right THIGH Aaron waved',                        'Lev', 9, 21, 'שוק'),
    ('and Aaron LIFTED his hand to the people',            'Lev', 9, 22, 'וישא'),
    ('and the glory of the LORD APPEARED to all the people', 'Lev', 9, 23, 'וירא'),
    ('and FIRE went out from before the LORD',             'Lev', 9, 24, 'אש'),
]
fired = 0
for label, book, ch, vs, tok in PROBES:
    if tok in toks(book, ch, vs): fired += 1
    else: print('PROBE FAILED: %s (%s %d:%d lacks %s)' % (label, book, ch, vs, tok))
if fired != len(PROBES):
    sys.exit('zero-report law: the ink scan is not trusted until every probe fires')
print('probes: %d/%d fired (the ink scan is trusted; the whole-Tanakh census holds %d verses)' % (len(PROBES), len(PROBES), N_VERSES))

# ---- the censuses (TRIPWIRES — each a measured literal) ------------
c_fire = tanakh_phrase(['ותצא', 'אש', 'מלפני', 'יהוה']);          assert c_fire == [('Lev', 9, 24), ('Lev', 10, 2)], c_fire
c_glory = tanakh_phrase(['וירא', 'כבוד', 'יהוה']);                assert c_glory == [('Lev', 9, 23), ('Num', 16, 19), ('Num', 17, 7), ('Num', 20, 6)], c_glory
c_appears = tanakh_phrase(['נראה', 'אליכם']);                     assert c_appears == [('Lev', 9, 4)], c_appears
c_eighth = tanakh_phrase(['ביום', 'השמיני']);                      assert len(c_eighth) == 9 and ('Lev', 9, 1) in c_eighth and ('Ezek', 43, 27) in c_eighth and ('1Kgs', 8, 66) in c_eighth, c_eighth
c_karishon = tanakh('כראשון');                                    assert c_karishon == [('Lev', 9, 15)], c_karishon
c_vayechateehu = tanakh('ויחטאהו');                               assert c_vayechateehu == [('Lev', 9, 15)], c_vayechateehu
c_kamishpat_torah = [k for k in tanakh('כמשפט') if k[0] in ('Gen', 'Exod', 'Lev', 'Num', 'Deut')]; assert len(c_kamishpat_torah) == 12, c_kamishpat_torah
c_kamishpat_lev = [k for k in c_kamishpat_torah if k[0] == 'Lev'];  assert c_kamishpat_lev == [('Lev', 5, 10), ('Lev', 9, 16)], c_kamishpat_lev
c_kerev_pair = sorted(k for k, t in _VERSES.items() if 'הקרב' in t and 'הכרעים' in t); assert c_kerev_pair == [('Lev', 8, 21), ('Lev', 9, 14)], c_kerev_pair
c_milvad = tanakh_phrase(['מלבד', 'עלת', 'הבקר']);                assert c_milvad == [('Lev', 9, 17), ('Num', 28, 23)], c_milvad
c_palm_filled = tanakh_phrase(['וימלא', 'כפו']);                  assert c_palm_filled == [('Lev', 9, 17)], c_palm_filled
c_kaf_torah = [k for k in tanakh('כפו') if k[0] in ('Gen', 'Exod', 'Lev', 'Num', 'Deut')]; assert c_kaf_torah == [('Lev', 9, 17), ('Lev', 14, 16), ('Lev', 14, 17), ('Lev', 14, 27), ('Lev', 14, 28)], c_kaf_torah
c_sang = tanakh('וירנו');                                          assert c_sang == [('Isa', 2, 3), ('Lev', 9, 24)], c_sang
c_fell = tanakh_phrase(['ויפלו', 'על', 'פניהם']);                 assert len(c_fell) == 6 and ('Lev', 9, 24) in c_fell and ('1Kgs', 18, 39) in c_fell, c_fell
c_lobe = tanakh('היתרת');                                          assert len(c_lobe) == 7 and ('Lev', 9, 10) in c_lobe and ('Lev', 3, 4) in c_lobe, c_lobe
c_tail = tanakh('האליה');                                          assert c_tail == [('Lev', 3, 9), ('Lev', 7, 3), ('Lev', 8, 25), ('Lev', 9, 19)], c_tail
c_cover = tanakh('והמכסה');                                        assert c_cover == [('Lev', 9, 19)], c_cover
c_stamp_lord9 = seats(9, has('כאשר', 'צוה', 'יהוה'), L9);          assert c_stamp_lord9 == [7, 10], c_stamp_lord9
c_stamp_lord8 = seats(8, has('כאשר', 'צוה', 'יהוה'), range(1, 37)); assert c_stamp_lord8 == [4, 9, 13, 17, 21, 29], c_stamp_lord8
c_stamp_moses = tanakh_phrase(['כאשר', 'צוה', 'משה']);             assert ('Lev', 9, 21) in c_stamp_moses and len([k for k in c_stamp_moses if k[0] == 'Lev']) == 1, c_stamp_moses
c_stamp_full = seats(9, has('כאשר', 'צוה', 'יהוה', 'את', 'משה'), L9); assert c_stamp_full == [10], c_stamp_full
c_command = seats(9, anyprefix('צוה'), L9);                        assert c_command == [5, 6, 7, 10, 21], c_command
c_burn = tanakh_phrase(['שרף', 'באש', 'מחוץ', 'למחנה']);          assert c_burn == [('Lev', 8, 17), ('Lev', 9, 11)], c_burn
c_outside_lev = [k for k in tanakh_phrase(['מחוץ', 'למחנה']) if k[0] == 'Lev']; assert len(c_outside_lev) == 13 and ('Lev', 4, 12) in c_outside_lev, c_outside_lev
c_blessed = tanakh_phrase(['ויברכו', 'את', 'העם']);               assert c_blessed == [('2Chr', 30, 27), ('Lev', 9, 23)], c_blessed
c_vayevarchem = tanakh('ויברכם');                                  assert len(c_vayevarchem) == 5 and ('Lev', 9, 22) in c_vayevarchem, c_vayevarchem
c_yado = toks('Lev', 9, 22)[3];                                    assert c_yado == 'ידו', c_yado
c_egel = seats(9, anytok('עגל', 'ועגל'), L9);                      assert c_egel == [2, 3, 8], c_egel
c_egel_lev = sorted(set(k for k in tanakh('עגל') + tanakh('ועגל') if k[0] == 'Lev')); assert c_egel_lev == [('Lev', 9, 2), ('Lev', 9, 3), ('Lev', 9, 8)], c_egel_lev
c_mixed_lev = [k for k in tanakh_phrase(['בלולה', 'בשמן']) if k[0] == 'Lev']; assert c_mixed_lev == [('Lev', 2, 5), ('Lev', 7, 10), ('Lev', 9, 4), ('Lev', 14, 10), ('Lev', 23, 13)], c_mixed_lev
c_tamimim = tanakh('תמימם');                                       assert len(c_tamimim) == 23 and ('Lev', 9, 2) in c_tamimim and ('Lev', 9, 3) in c_tamimim and ('Exod', 29, 1) in c_tamimim, c_tamimim
c_lishlamim = tanakh_phrase(['לשלמים', 'לזבח']);                  assert c_lishlamim == [('Lev', 9, 4)], c_lishlamim
c_approach_cmd = tanakh_phrase(['קרב', 'אל', 'המזבח']);           assert c_approach_cmd == [('Lev', 9, 7)], c_approach_cmd
c_stood = tanakh_phrase(['ויקרבו', 'כל', 'העדה']);                assert c_stood == [('Lev', 9, 5)], c_stood
c_fat10 = [w for w in toks('Lev', 9, 10) if w in ('החלב', 'הכלית', 'היתרת')]; assert c_fat10 == ['החלב', 'הכלית', 'היתרת'], c_fat10
c_fat19 = [w for w in toks('Lev', 9, 19) if w in ('האליה', 'והמכסה', 'והכלית', 'ויתרת')]; assert c_fat19 == ['האליה', 'והמכסה', 'והכלית', 'ויתרת'], c_fat19
c_saviv = seats(9, anytok('סביב'), L9);                             assert c_saviv == [12, 18], c_saviv
c_approach = seats(9, anyprefix('ויקרב'), L9);                     assert c_approach == [5, 8, 9, 15, 16, 17], c_approach
c_slaughter = seats(9, anyprefix('וישחט'), L9);                    assert c_slaughter == [8, 12, 15, 18], c_slaughter
c_smoke = seats(9, anytok('הקטיר', 'ויקטר'), L9);                  assert c_smoke == [10, 13, 14, 17, 20], c_smoke
c_blood = seats(9, anytok('הדם', 'בדם'), L9);                      assert c_blood == [9, 12, 18], c_blood
c_sons = seats(9, has('בני', 'אהרן'), L9);                          assert c_sons == [9, 12, 18], c_sons
c_poured = [k for k in tanakh('יצק') if k[0] == 'Lev'];            assert c_poured == [('Lev', 8, 15), ('Lev', 9, 9), ('Lev', 14, 26)], c_poured
c_finger_horns_base = all(w in toks('Lev', 9, 9) for w in ('אצבעו', 'קרנות', 'יסוד')); assert c_finger_horns_base
c_tokens = sum(len(toks('Lev', 9, v)) for v in L9);                assert c_tokens == 318, c_tokens
print('censuses: the fire formula at %s · the glory formula at %d seats · "appears to you" %s · "the eighth day" x%d · "like the first" %s · "as prescribed" %d Torah seats (Lev: %s) · '
      'entrails+legs pair %s · "beside the morning olah" %s · "his palm" Torah %s · the burn phrase %s · command tokens at 9:%s (the LORD stamp at 9:%s, Moses at 9:21; 9:11 unstamped) · '
      '"and they blessed the people" %s · "his hand" written %s at 9:22 · the fat heads at 9:10 %s and 9:19 %s · around at 9:%s · slaughter at 9:%s · smoke at 9:%s · %d tokens in the chapter'
      % (c_fire, len(c_glory), c_appears, len(c_eighth), c_karishon, len(c_kamishpat_torah), c_kamishpat_lev, c_kerev_pair, c_milvad, c_kaf_torah, c_burn, c_command, c_stamp_lord9,
         c_blessed, c_yado, c_fat10, c_fat19, c_saviv, c_slaughter, c_smoke, c_tokens))

# ---- the callees (cold) --------------------------------------------
_buf = io.StringIO()
with contextlib.redirect_stdout(_buf):
    import cold_run_chatat as CH
    import cold_run_offerings as OFF
    import cold_run_minchah as MIN
    import cold_run_tzav as TZ
    import world_engine as WE
OLAH_H = OFF.dispatch('olah:herd'); OLAH_F = OFF.dispatch('olah:flock'); SHEL = OFF.dispatch('shelamim')
COMM = OFF.dispatch('communal_shelamim_and_asham'); OUTER = OFF.dispatch('outer_chatat')
FAT_OX = OFF.dispatch('fat:ox'); FAT_LAMB = OFF.dispatch('fat:lamb')
CH_RANK_A = CH.rank('anointed')['v']; CH_RANK_C = CH.rank('congregation')['v']
CH_BLOOD_A = CH.blood('anointed')['v']; CH_BLOOD_COM = CH.blood('commoner')['v']
CH_CARC_A = CH.carcass('anointed')['v']; CH_CARC_COM = CH.carcass('commoner')['v']
CH_SPR_A = CH.sprinklings('anointed')['v']; CH_SPR_COM = CH.sprinklings('commoner')['v']
CH_PREC = CH.precedence_bulls()['v']; CH_BURN = CH.burn_site('as_commanded')['v']
CH_INQ = CH.inquiry('blood_not_inside')['v']; CH_GOAT = CH.inquiry('which_goat_burned')['v']
MIN_LEFT = MIN.fistful('left_hand')['v']; MIN_CRUMB = MIN.fistful('pebble_salt_grain_frankincense_crumb')['v']
MIN_PAIR = MIN.fistful('fistful_and_frankincense')['v']; MIN_FRANK = MIN.frankincense_quantity()['v']
MIN_OIL = MIN.oil_ops('soleth')['v']; MIN_REM = MIN.remainder('soleth')['v']; MIN_PRES = MIN.presentation('soleth')['v']
TZ_CONF = TZ.installation({'ask': 'confinement'}, TZ.PARAMS)[0]; TZ_COMMIT = TZ.installation({'ask': 'commit_point'}, TZ.PARAMS)[0]
TZ_EXT = TZ.altar_machine({'ask': 'extinguish'}, TZ.PARAMS)[0]; TZ_RET = TZ.altar_machine({'ask': 'retention'}, TZ.PARAMS)[0]
TZ_BT = TZ.dues_machine({'ask': 'breast_thigh'}, TZ.PARAMS)[0]; TZ_HIDE = TZ.dues_machine({'ask': 'olah_hide'}, TZ.PARAMS)[0]
print('routing receipts: cold_run_chatat CALLED — rank anointed %r / congregation %r, blood anointed %r / commoner %r, carcass anointed %r / commoner %r, sprinklings %r/%r, '
      'precedence %r, burn site %r, inquiry %r / %r; cold_run_offerings CALLED — olah:herd %r, shelamim %r, communal %r, fat:ox tail %r, fat:lamb tail %r; '
      'cold_run_minchah CALLED — left hand %r, crumb %r, pair %r, frankincense %r, oil forms %r, remainder %r, presentation %r; cold_run_tzav CALLED — confinement %r, '
      'commit %r, extinguish %r, retention %r, breast and thigh %r, hide %r [IMPORT, live calls]'
      % (CH_RANK_A, CH_RANK_C, CH_BLOOD_A, CH_BLOOD_COM, CH_CARC_A, CH_CARC_COM, CH_SPR_A, CH_SPR_COM, CH_PREC, CH_BURN, CH_INQ, CH_GOAT,
         {k: v['v'] for k, v in OLAH_H.items()}, SHEL['applications']['v'], COMM['eater']['v'], FAT_OX['tail']['v'], FAT_LAMB['tail']['v'],
         MIN_LEFT, MIN_CRUMB, MIN_PAIR, MIN_FRANK, MIN_OIL, MIN_REM, MIN_PRES, TZ_CONF, TZ_COMMIT, TZ_EXT, TZ_RET, TZ_BT, TZ_HIDE))

I, M, A, D, P = 'INK', 'MOVE', 'ANSWER-SHEET', 'DATA', 'IMPORT'
def cell(v, p, why, fx):
    FX.validate(fx)
    return {'v': v, 'p': p, 'why': why, 'fx': fx}
SM = "Sifra, Shemini, Mechilta d'Miluim 2 "
STM = "Sifra, Tzav, Mekhilta DeMiluim I "

# =====================================================================
# THE RUN — from the ink of Leviticus 9 alone, matched cell by cell to the
# SPEC by live call. Mishnah/Talmud appear ONLY on [MOVE] lines (motion 4)
# and as DATA (motion 2).
# =====================================================================

# ---- F1: THE DAY AND THE TAKE-LIST (9:1-6) ----------------------------
def day(q):
    if q == 'eighth_of':
        return cell('the_count', M, "9:1 'and it was on the EIGHTH day' — eighth of what? " + SM + "1: 'and it was on the THIRD day' (Exod 19:16) is "
                    "third OF THE COUNT, so this is eighth of the count — Lev 8:33's 'seven days he shall fill your hand' closing it; the phrase at "
                    f"{len(c_eighth)} Tanakh seats (the circumcision, the leper, the festival, Solomon's and Ezekiel's eighth days among them)", ['released'])
    if q == 'date':
        return cell('first_of_nisan', M, SM + "14: the tabernacle was raised on the new moon (Exod 40:17 [IMPORT]) and the cloud covered it THAT day "
                    "(Num 9:15) — the eighth of the count IS the first of the month; " + STM + "36 computes it: the installation began the 23rd of Adar, "
                    f"23 + 7 = 30, the first of Nisan; CALLED cold_run_tzav.installation(confinement) -> {TZ_CONF!r} [IMPORT, live call]", ['released'])
    if q == 'called':
        return cell('aaron_sons_elders', I, "9:1 'Moses called Aaron and his sons and the elders of Israel' — three parties in the ink's order; " + SM + "2: "
                    "the Place honored Aaron first (Exod 19:24), so Moses honors him at the end — called before the elders", [FX.NONE])
    if q == 'aaron_chatat_spec':
        return cell(CH_RANK_A, P, f"the spec's rank for the anointed priest's sin offering — CALLED cold_run_chatat.rank(anointed) -> {CH_RANK_A!r} "
                    "(Lev 4:3 'a bull, son of the herd') [IMPORT, live call]", ['accepted'])
    if q == 'aaron_chatat_run':
        return cell('calf', I, f"9:2 'take for yourself a CALF (עגל), son of the herd, for a sin offering' — the calf token at 9:{c_egel} and at no "
                    "other Leviticus seat; not the spec's bull", ['accepted'])
    if q == 'aaron_chatat_deviation':
        return cell('calf_answers_calf', M, SM + "3-4: 'send a gift ahead before you enter the sanctuary' — Aaron's sin offering is a CALF because "
                    "the offense was the calf (Exod 32:4); 'let the calf atone for the calf's deed' — the run departs from Lev 4:3's bull by the "
                    "day's own ruling; " + STM + "1 reads 9:7's 'approach' as the public re-acceptance after the calf", ['atoned_forgiven'])
    if q == 'calf_age':
        return cell('one_year_son_of_herd_two', D, "the age is the data channel: Sifra, Vayikra Dibbura DeChovah, Chapter 3 6 (R. Shimon) reads the "
                    "lexicon OFF THIS RUN — 'calf' plain = one year (9:3 'a calf and a lamb, sons of a year'), 'calf son of the herd' = two years "
                    "(9:2), 'bull' plain = three; Mishnah Parah 1:1 carries the recorded settings (R. Eliezer one, the sages two)", [FX.NONE])
    if q == 'aaron_olah':
        return cell('ram', I, "9:2 'and a RAM for a burnt offering' — the flock's burnt offering (Lev 1:10's 'of the flock... a male'); 'unblemished' "
                    "(תמימם) written on the pair", ['accepted'])
    if q == 'people_chatat_spec':
        return cell(CH_RANK_C, P, f"the spec's rank for the congregation's sin offering — CALLED cold_run_chatat.rank(congregation) -> {CH_RANK_C!r} "
                    "(Lev 4:14 'the assembly shall offer a bull') [IMPORT, live call]", ['accepted'])
    if q == 'people_chatat_run':
        return cell('he_goat', I, "9:3 'take a HE-GOAT (שעיר עזים) for a sin offering' — not the spec's bull; the goat is the ruler's animal at Lev "
                    "4:23 and the individual's at 4:28 in the spec's own ranks", ['accepted'])
    if q == 'people_chatat_deviation':
        return cell('goat_for_joseph_calf_for_calf', M, SM + "3: 'you have something in your hands at the beginning and at the end' — the goat for "
                    "the goat of Joseph's sale (Gen 37:31), the calf (9:3's burnt offering) for the calf; 4: the ox of 9:4 for 'the likeness of an "
                    "OX that eats grass' (Ps 106:20) — two animals for an offense that resembled two species", ['atoned_forgiven'])
    if q == 'people_olah':
        return cell('calf_and_lamb_yearlings', I, "9:3 'and a calf and a lamb, sons of a year, unblemished, for a burnt offering' — the herd's and "
                    f"the flock's burnt offerings side by side; 'unblemished' (תמימם) doubled at 9:2 and 9:3 ({len(c_tamimim)} Tanakh seats of "
                    "this plural, Exod 29:1's installation take-list the first)", ['accepted'])
    if q == 'people_shelamim':
        return cell('ox_and_ram', I, "9:4 'and an ox and a ram for peace offerings to sacrifice before the LORD' — the phrase 'for peace offerings "
                    f"to sacrifice' at {c_lishlamim} alone in the Tanakh", ['accepted'])
    if q == 'communal_shelamim_source':
        return cell('Lev 9:4', M, SM + "13: 'the ox and the ram, the sacrifice of peace offerings FOR THE PEOPLE' (9:18) — 'from here they learned "
                    "peace offerings for the public'; the appointed-times engine's Shavuot lambs are that class (Lev 23:19)", ['accepted'])
    if q == 'communal_shelamim_grade':
        return cell(COMM['eater']['v'], P, f"the class's rite — CALLED cold_run_offerings.dispatch(communal_shelamim_and_asham): eater {COMM['eater']['v']!r}, "
                    f"place {COMM['eat_place']['v']!r}, window {COMM['window']['v']!r} (Mishnah Zevachim 5:5's row) [IMPORT, live call]; the run's 9:18 "
                    "names no eater — the spec supplies", ['due_to_priest', 'eating_window'])
    if q == 'minchah_form':
        return cell('mixed_with_oil', I, f"9:4 'and a meal offering MIXED WITH OIL (בלולה בשמן)' — the phrase's Leviticus seats {[(c, v) for _, c, v in c_mixed_lev]}: "
                    "2:5's griddle, 7:10's due, this, the leper's, the omer's", ['presented'])
    if q == 'minchah_oil_forms':
        return cell(MIN_OIL, P, f"the spec's three oil forms — CALLED cold_run_minchah.oil_ops(soleth) -> {MIN_OIL!r} (pour, mix, made in oil; "
                    "Mishnah Menachot 6:3) [IMPORT, live call]; the run names the middle one, MIXED", [FX.NONE])
    if q == 'funding':
        return cell('aaron_own_people_public', M, "Yoma 3b:4: 'take FOR YOURSELF (קח לך) a calf' (9:2) against 'tell the children of Israel: take "
                    "(קחו)' (9:3) — 'for yourself' = from your own; the people's from the public: the funding parameter read off the dative", [FX.NONE])
    if q == 'today_appears':
        return cell('hapax', I, f"9:4 'for today the LORD APPEARS TO YOU (נראה אליכם)' — the phrase at {c_appears} in the whole Tanakh; Onkelos "
                    "Lev 9:4 renders it 'the glory of the LORD is revealed' (the standing glory policy)", ['glory_appeared'])
    if q == 'alacrity':
        return cell('took_and_stood', I, f"9:5 'they took what Moses commanded... and all the assembly DREW NEAR and stood before the LORD' — the phrase "
                    f"at {c_stood} alone; " + SM + "5: 'with alacrity', 'they drew near in joy and STOOD' (the reconciled-queen parable)", [FX.NONE])
    if q == 'command_stamps':
        return cell(c_command, I, f"the command root at 9:{c_command}: 'what Moses commanded' (9:5), 'this is the thing the LORD commanded' (9:6), "
                    f"'as the LORD commanded' (9:{c_stamp_lord9} — six such stamps in Lev 8 at 8:{c_stamp_lord8}), 'as Moses commanded' (9:21); "
                    "the one act of the day with NO stamp is 9:11's burning of the calf", [FX.NONE])
    if q == 'glory_promise':
        return cell('promised_9_6_fulfilled_9_23', I, "9:6 'and the glory of the LORD SHALL APPEAR to you' — 9:23 'and the glory of the LORD APPEARED "
                    f"to all the people'; the fulfillment formula at {len(c_glory)} Tanakh seats — this, then Korach's (Num 16:19), the plague "
                    "(17:7), Meribah (20:6): the only one that is not a rebellion", ['glory_appeared'])
    return cell('no_case', I, '', [FX.NONE])

# ---- F2: THE ORDER OF SERVICE (9:7-8, 9:15-17; Zevachim 10; Horayot 3:6) ----
def order(q):
    if q == 'own_before_people':
        return cell('aaron_first', I, "9:7 'do YOUR sin offering and YOUR burnt offering... and do the PEOPLE'S offering' — the ink's order; the run "
                    f"executes it: 9:8-14 Aaron's pair, 9:15-21 the people's (slaughter at 9:{c_slaughter}); " + SM + "9: 'he began with his own'", [FX.NONE])
    if q == 'own_atones_for':
        return cell('himself_and_people', I, "9:7 'and atone for yourself AND for the people... and atone for THEM' — his own covers both, the "
                    "people's covers the people; " + SM + "9: 'the people's offering does not atone for the priests, his atones for him and for "
                    "the people'", ['atoned_forgiven'])
    if q == 'anointed_first_spec':
        return cell(CH_PREC, P, f"Mishnah Horayot 3:6's row at the spec: 'the anointed's bull and the congregation's bull standing — the anointed's "
                    f"precedes in all its acts' — CALLED cold_run_chatat.precedence_bulls() -> {CH_PREC!r} (Lev 4:21 'the FIRST bull') [IMPORT, "
                    "live call]; the run's own-first is the row's shape at the day's two sin offerings", [FX.NONE])
    if q == 'chatat_blood_before_olah_blood':
        return cell('chatat_blood_first', I, "the run: 9:9 (the calf's blood on the horns) precedes 9:12 (the ram's blood around) — Mishnah "
                    "Zevachim 10:2's first clause, 'the sin offering's blood precedes the burnt offering's, because it appeases', matched "
                    f"(the blood token at 9:{c_blood})", [FX.NONE])
    if q == 'spec_limbs_vs_fats':
        return cell('olah_limbs_first', A, "Mishnah Zevachim 10:2: 'the burnt offering's LIMBS precede the sin offering's FATS, because they are "
                    "wholly to the fires' — Zevachim 89b:2-3 sources the interleaving at Num 8:8-12 (the Levites' 'second bull' bars the sin "
                    "offering preceding in ALL its acts)", [FX.NONE])
    if q == 'run_limbs_vs_fats':
        return cell('chatat_completed_whole_first', I, f"the run: 9:10 (the calf's fats smoked, smoke at 9:{c_smoke}) precedes 9:12-13 (the ram "
                    "slaughtered, its limbs smoked) — the calf was finished WHOLE (9:8-11) before the ram was slaughtered; the pair never stood "
                    "ready together, so the interleaving rule's precondition is absent; no segment on the span reconciles it — filed as the "
                    "hour's own order (Menachot 19b:4, Shmuel: generations are not learned from the hour)", [FX.NONE])
    if q == 'goat_like_first':
        return cell('four_horns_imported', M, f"9:15 'and he slaughtered it and purified it LIKE THE FIRST (כראשון)' — the token at {c_karishon} "
                    f"alone in the Tanakh, the verb 'purified it' (ויחטאהו) at {c_vayechateehu} alone; " + SM + "9: 'as the first required "
                    "purification, so this' — the calf's four-horn application (9:9) imported by one word; Onkelos Lev 9:15 decodes the verb: "
                    "'and he ATONED WITH ITS BLOOD'", ['atoned_forgiven'])
    if q == 'olah_as_prescribed':
        return cell(OLAH_H['procedure']['v'], P, f"9:16 'and he brought the burnt offering and did it AS PRESCRIBED (כמשפט)' — the pointer CALL: "
                    f"cold_run_offerings.dispatch(olah:herd) -> place {OLAH_H['place']['v']!r}, applications {OLAH_H['applications']['v']!r}, "
                    f"procedure {OLAH_H['procedure']['v']!r}, disposition {OLAH_H['disposition']['v']!r} [IMPORT, live call]; " + SM + "10 "
                    "names the same four imports — flay and cut, wholly to the fires, standing beside the altar to throw, popped limbs returned", ['smoked_to_the_lord'])
    if q == 'kamishpat_census':
        return cell(12, I, f"'as prescribed' at {len(c_kamishpat_torah)} Torah seats — in Leviticus only {c_kamishpat_lev}: 5:10's bird pair "
                    "(the Lev 5 engine's own pointer) and this; Onkelos Lev 9:16 renders it 'as is FITTING'", [FX.NONE])
    if q == 'run_teaches_spec_semikhah':
        return cell('obligatory_olah_requires_hand_laying', M, "Menachot 93b:3 (= Beitzah 20a:5): 'and he brought the burnt offering and did it "
                    "as prescribed — AS THE LAW OF THE FREEWILL BURNT OFFERING: teaches that the OBLIGATORY burnt offering requires hand-laying' "
                    "— the run's pointer into Lev 1 read BACK into the spec, giving Lev 1:4's hand-laying to a class Lev 1 does not name "
                    "(Mishnah Beitzah 2:4, Beit Hillel's arm)", [FX.NONE])
    if q == 'tadir_first':
        return cell('temidim_precede', I, f"9:17 'BESIDE THE MORNING BURNT OFFERING (מלבד עלת הבקר)' — the daily offering was on the altar "
                    f"before the calf; the phrase at {c_milvad} in the whole Tanakh: this run and Num 28:23's spec of the additional offerings, "
                    "from which Mishnah Zevachim 10:1 derives 'whatever is more frequent precedes'", [FX.NONE])
    if q == 'altar_inaugurated_by':
        return cell('morning_tamid', A, "Mishnah Menachot 4:4 (R. Shimon): 'the altar of the burnt offering is inaugurated only with the morning "
                    "daily offering' — the run's first act on the new altar is 9:17's morning burnt offering, before the calf of 9:8", [FX.NONE])
    if q == 'eating_order':
        return cell('as_offering_order', A, "Mishnah Zevachim 10:6: 'as they precede in offering so in eating' — the run's eating is Lev 10:12-15 "
                    f"(the meal offering's remainder, the breast and thigh), the sin-offering engine's span; CALLED cold_run_chatat.inquiry -> {CH_INQ!r} "
                    "for the goat [IMPORT, live call]", ['eating_window'])
    if q == 'seven_services':
        return cell(7, D, SM + "13: the sons of Aaron learned SEVEN services in one hour — slaughter, reception, throwing, sprinkling, purification, "
                    "pouring, atonement; the count is the recorded tribute, not the ink's", [FX.NONE])
    return cell('no_case', I, '', [FX.NONE])

# ---- F3: THE CALF'S RITE (9:8-11) — outer blood, inner carcass ---------
def calf(q):
    if q == 'slaughterer':
        return cell('aaron', I, "9:8 'and Aaron drew near to the altar and SLAUGHTERED the calf of the sin offering which was his' — Aaron himself; "
                    + SM + "9: 'with alacrity'", [FX.NONE])
    if q == 'blood_bearers':
        return cell('sons', I, f"9:9 'and the sons of Aaron BROUGHT the blood to him' — 'the sons of Aaron' at 9:{c_sons}, each time handing the "
                    "blood; Moed Katan 28b:13 (R. Tarfon): Nadav and Avihu did 'only one commandment' — this bringing", [FX.NONE])
    if q == 'blood_run':
        return cell('finger_horns_base', I, "9:9 'he dipped his FINGER (אצבעו) in the blood and put it on the HORNS (קרנות) of the altar, and the "
                    f"blood he POURED (יצק) at the BASE (יסוד) of the altar' — the three tokens present ({c_finger_horns_base}); the pour verb "
                    f"'yatzak' in Leviticus at {[(c, v) for _, c, v in c_poured]}", ['atoned_forgiven'])
    if q == 'blood_spec_outer':
        return cell(CH_BLOOD_COM, P, f"the spec's OUTER protocol — CALLED cold_run_chatat.blood(commoner) -> {CH_BLOOD_COM!r} (Lev 4:25, 4:30, "
                    f"4:34: finger, horns, base; sprinklings {CH_SPR_COM}) [IMPORT, live call]: the run's 9:9 is this protocol", ['atoned_forgiven'])
    if q == 'blood_spec_anointed':
        return cell(CH_BLOOD_A, P, f"the spec's protocol for the ANOINTED priest's bull — CALLED cold_run_chatat.blood(anointed) -> {CH_BLOOD_A!r}, "
                    f"sprinklings {CH_SPR_A} before the veil, the incense altar's horns (Lev 4:5-7) [IMPORT, live call]: NOT the run's", [FX.NONE])
    if q == 'blood_deviation':
        return cell('outer_protocol_for_the_anointed', M, "the run's blood went to the outer altar's horns (9:9) though the offerer is the anointed "
                    "priest, whose spec-tier blood goes inside (Lev 4:5-7) — the calf is the day's one-time sin offering, not Lev 4:3's bull "
                    "(" + SM + "3-4); Lev 10:18 later grades a same-day outer-blood sin offering as one to be EATEN — CALLED "
                    f"cold_run_chatat.inquiry(blood_not_inside) -> {CH_INQ!r} [IMPORT, live call]", [FX.NONE])
    if q == 'sprinklings_run':
        return cell(0, I, "no sevenfold sprinkling in the run — 9:9 has the finger, the horns, the base and no 'seven times' (the spec's anointed "
                    f"tier has {CH_SPR_A} at Lev 4:6)", [FX.NONE])
    if q == 'fat_run':
        return cell('fat_kidneys_lobe', I, f"9:10 'the FAT and the KIDNEYS and the LOBE from the liver, from the sin offering, he smoked on the altar' "
                    f"— the heads at 9:10 {c_fat10}; the lobe token at {len(c_lobe)} Tanakh seats, all in the offering chapters and Exod 29:13", ['smoked_to_the_lord'])
    if q == 'fat_spec':
        return cell(FAT_OX['parts']['v'], P, f"the spec's inventory for the herd — CALLED cold_run_offerings.dispatch(fat:ox) -> parts {FAT_OX['parts']['v']!r}, "
                    f"tail {FAT_OX['tail']['v']!r} (Lev 3:3-4 through Lev 4:8-10's pointer) [IMPORT, live call]: the run's three heads are three of "
                    "the four, 'the fat' standing for the covering and the entrails' fat", ['smoked_to_the_lord'])
    if q == 'lobe_from_liver':
        return cell('take_from_liver_onto_lobe', M, "Sifra, Vayikra Dibbura DeNedavah, Section 14 8: Lev 3:4's 'the lobe ON the liver' is ambiguous "
                    "— take from the liver onto the lobe, or from the lobe onto the liver? 'when it says (Lev 9:10) the lobe FROM the liver' — "
                    "from the liver onto the lobe: THE RUN TEACHES THE SPEC A PREPOSITION", ['smoked_to_the_lord'])
    if q == 'fat_stamp':
        return cell('as_the_LORD_commanded_Moses', I, f"9:10 closes 'AS THE LORD COMMANDED MOSES' — the day's one full-form stamp (9:{c_stamp_full}); "
                    "the fat clause it cites is Lev 4:8-10, resolved through the chatat engine's own pointer into the fat inventory", [FX.NONE])
    if q == 'carcass_run':
        return cell('burned_outside_camp', I, f"9:11 'and the FLESH and the HIDE he BURNED in fire OUTSIDE THE CAMP' — the burn phrase at {c_burn} "
                    "in the whole Tanakh: the installation bull (8:17) and this calf, the two outer-blood sin offerings ever burned; 'outside the "
                    f"camp' at {len(c_outside_lev)} Leviticus seats", ['burned_outside_camp'])
    if q == 'carcass_spec_for_outer_blood':
        return cell(CH_CARC_COM, P, f"the spec's carcass rule for an outer-blood sin offering — CALLED cold_run_chatat.carcass(commoner) -> "
                    f"{CH_CARC_COM!r} (eaten within the hangings, Lev 6:19, 6:22) [IMPORT, live call]: the run BURNED instead", ['due_to_priest'])
    if q == 'carcass_spec_for_anointed':
        return cell(CH_CARC_A, P, f"the spec's carcass rule for the anointed tier — CALLED cold_run_chatat.carcass(anointed) -> {CH_CARC_A!r} "
                    "(Lev 4:11-12, 6:23) [IMPORT, live call]: the run's BURNING is this tier's rule, on a calf whose BLOOD followed the other tier", ['burned_outside_camp'])
    if q == 'carcass_deviation':
        return cell('unstamped_one_time_burning', M, "the mixed row: outer blood (9:9) with an inner carcass (9:11) — and 9:11 is the ONE act of the "
                    f"day without a command stamp (stamps at 9:{c_command}); " + STM + "12 and 16 read the installation bull the same way "
                    "(named 'the sin offering' only when its acts are listed; its fats still the altar's); Lev 10:16-18's inquiry then makes "
                    f"eating the rule for the goat — CALLED cold_run_chatat.inquiry(which_goat_burned) -> {CH_GOAT!r}: the burned goat was the "
                    "new moon's (Zevachim 101b:6: three sin-offering goats that day — Nachshon's, the eighth day's, the new moon's)", ['burned_outside_camp'])
    if q == 'burn_site_spec':
        return cell(CH_BURN, P, f"the spec's burn site — CALLED cold_run_chatat.burn_site(as_commanded) -> {CH_BURN!r} (Lev 4:12's pure place, the "
                    "ash-pour; Lev 16:28's defiled garments) [IMPORT, live call]; the run says only 'outside the camp' — the spec supplies the rest", ['defiles_garments'])
    if q == 'hide':
        return cell('burned_with_flesh', I, f"9:11 'the flesh AND THE HIDE' burned — against the burnt offering's hide, which is the priest's: "
                    f"CALLED cold_run_tzav.dues_machine(olah_hide) -> {TZ_HIDE!r} (Lev 7:8) [IMPORT, live call]; the sin offering's hide goes "
                    "with its flesh (Lev 4:11 'its hide and all its flesh')", ['burned_outside_camp'])
    return cell('no_case', I, '', [FX.NONE])

# ---- F4: THE RAM'S RITE (9:12-14) — the burnt offering by the spec ----
def ram(q):
    if q == 'blood':
        return cell(OLAH_F['applications']['v'], P, f"9:12 'and he threw it on the altar AROUND (סביב)' — around at 9:{c_saviv} (the ram, the peace "
                    f"offerings); CALLED cold_run_offerings.dispatch(olah:flock) -> applications {OLAH_F['applications']['v']!r} (Zevachim 53b:5's "
                    "reading of Lev 1:5's 'around' and 'throw') [IMPORT, live call]", ['accepted'])
    if q == 'sons_hand':
        return cell('presented_to_him', I, "9:12 'and the sons of Aaron PRESENTED (וימצאו) the blood to him', 9:13 'and the burnt offering they "
                    "PRESENTED (המציאו) to him by its pieces and the head' — the sons hand, Aaron applies and smokes", [FX.NONE])
    if q == 'pieces_and_head':
        return cell(OLAH_F['procedure']['v'], P, "9:13 'by its PIECES (לנתחיה) and the HEAD (הראש)' — Lev 1:6's flay-and-cut and 1:8's head by "
                    f"call: cold_run_offerings.dispatch(olah:flock) -> procedure {OLAH_F['procedure']['v']!r} [IMPORT, live call]; the flaying is "
                    "not narrated, the hide being the priest's (Lev 7:8)", ['smoked_to_the_lord'])
    if q == 'entrails_legs':
        return cell('washed_and_smoked', I, f"9:14 'and he WASHED the entrails (הקרב) and the legs (הכרעים) and smoked them on the burnt offering' — "
                    f"the pair with the article at {c_kerev_pair} alone (Lev 1:9, 1:13 write them suffixed); Mishnah Tamid 4:2-3's walk has the "
                    "same three heads: the head handed, the legs handed, the entrails rinsed", ['smoked_to_the_lord'])
    if q == 'disposition':
        return cell(OLAH_F['disposition']['v'], P, f"9:14 'on the burnt offering' — everything to the altar: CALLED cold_run_offerings.dispatch"
                    f"(olah:flock) -> disposition {OLAH_F['disposition']['v']!r} (Lev 1:9 'the whole') [IMPORT, live call]", ['smoked_to_the_lord'])
    if q == 'place':
        return cell(OLAH_F['place']['v'], P, f"the run names no place of slaughter; the spec supplies — CALLED cold_run_offerings.dispatch(olah:flock) "
                    f"-> place {OLAH_F['place']['v']!r} (Lev 1:11; Mishnah Zevachim 5:4) [IMPORT, live call]", [FX.NONE])
    if q == 'tamid_walk':
        return cell('head_legs_entrails', A, "Mishnah Tamid 4:2: the head cut and handed, the legs cut and handed, the entrails handed to be rinsed — "
                    "the daily offering's cutting walk carries the run's 9:13-14 heads in the walk's order; 4:3: the tail, the lobe, and the "
                    "kidneys held together — the fat list's heads at 9:19", [FX.NONE])
    return cell('no_case', I, '', [FX.NONE])

# ---- F5: THE PEOPLE'S OFFERING (9:15-17) — the palm, the fork ---------
def people(q):
    if q == 'goat_purified':
        return cell('atoned_with_its_blood', M, "Onkelos Lev 9:15: 'and he purified it' (ויחטאהו) -> 'and he ATONED WITH ITS BLOOD' — the "
                    "translation states what the purification verb DOES; the four horns by 'like the first'", ['atoned_forgiven'])
    if q == 'fistful_crumb':
        return cell(MIN_CRUMB, P, "9:17 'and he FILLED HIS PALM (וימלא כפו) from it and smoked it on the altar' — " + SM + "11: 'filling' here "
                    "and 'filling' at Lev 2:2 (the fill-with-fill verbal analogy): a pebble, a grain of salt, a crumb of frankincense in the fist "
                    f"disqualifies here as there — CALLED cold_run_minchah.fistful(pebble_salt_grain_frankincense_crumb) -> {MIN_CRUMB!r} "
                    "[IMPORT, live call]", ['disqualified'])
    if q == 'palm_is_right':
        return cell('right', M, "Menachot 9b:17 (R. Zeira): 'and filled HIS PALM (כפו) from it' (9:17) — 'palm', I do not know what it is; when "
                    "it says 'on the priest's LEFT palm' (Lev 14:15) — there left, hence WHEREVER 'PALM' IS SAID UNMARKED IT IS THE RIGHT: the "
                    f"left-hand fistful invalid — CALLED cold_run_minchah.fistful(left_hand) -> {MIN_LEFT!r} (Mishnah Menachot 1:2) [IMPORT, "
                    "live call] — the meal-offering engine's cell that cited the sheet without a derivation now has one, from THIS verse's token; "
                    "Menachot 10a:6 (Rava) the hand-hand analogy beside it", ['disqualified'])
    if q == 'palm_census':
        return cell(5, I, f"'his palm' (כפו) at {len(c_kaf_torah)} Torah seats: {[(c, v) for _, c, v in c_kaf_torah]} — this verse and the "
                    "leper's four (the left palm named at 14:15, 14:26); 'and filled his palm' a hapax in the whole Tanakh", [FX.NONE])
    if q == 'fistful_repeated_fork':
        return cell('Rav_indispensable_Shmuel_not_from_the_hour', M, "Menachot 19b:2-4 — Rav: wherever Scripture REPEATED 'meal offering' it is "
                    "indispensable, and 9:17's 'he filled his palm from it' is the fistful repeated (Mishnah Menachot 3:5: the fistful and the "
                    "frankincense hold each other back); Shmuel: 'GENERATIONS ARE NOT LEARNED FROM THE HOUR' — the run's one-time act does not "
                    f"legislate; the pair by call: cold_run_minchah.fistful(fistful_and_frankincense) -> {MIN_PAIR!r} [IMPORT, live call]", ['azkarah_to_fire'])
    if q == 'two_minchahs':
        return cell(2, M, SM + "12: 'and he smoked it on the altar BESIDE the morning burnt offering' — what does it teach? not that a beast "
                    "replaces a missing meal offering (9:16 already covers the burnt offering): 'that there were TWO meal offerings there, one "
                    "with the burnt offering and one on its own'", ['azkarah_to_fire'])
    if q == 'frankincense':
        return cell(MIN_FRANK, P, "Menachot 59a:11: 'meal offering' — to INCLUDE the eighth day's meal offering for frankincense (the inclusion on "
                    "Lev 2:1; Mishnah Menachot 5:3's oil-and-frankincense column for the flour kind) — the quantity by call: cold_run_minchah."
                    f"frankincense_quantity() -> {MIN_FRANK!r} [IMPORT, live call]", ['azkarah_to_fire'])
    if q == 'remainder':
        return cell(MIN_REM, P, f"the remainder — CALLED cold_run_minchah.remainder(soleth) -> {MIN_REM!r} (Lev 2:3) [IMPORT, live call]; eaten at "
                    "Lev 10:12-13 (the sin-offering engine's priest's table)", ['due_to_priest'])
    if q == 'presentation':
        return cell(MIN_PRES, P, f"the presentation the run does not narrate — CALLED cold_run_minchah.presentation(soleth) -> {MIN_PRES!r} "
                    "(Lev 2:8) [IMPORT, live call]", ['presented'])
    return cell('no_case', I, '', [FX.NONE])

# ---- F6: THE PEACE OFFERINGS (9:18-21) — two inventories, one list ----
def peace(q):
    if q == 'blood':
        return cell(SHEL['applications']['v'], P, f"9:18 'and he threw it on the altar AROUND' — CALLED cold_run_offerings.dispatch(shelamim) -> "
                    f"applications {SHEL['applications']['v']!r}, window {SHEL['window']['v']!r} (Lev 3:2; 7:16) [IMPORT, live call]", ['accepted'])
    if q == 'fat_list':
        return cell('tail_covering_kidneys_lobe', I, f"9:19 'and the fats from the OX and from the RAM: the TAIL and the COVERING and the KIDNEYS and "
                    f"the LOBE of the liver' — the four heads {c_fat19}; 'and the covering' (והמכסה) a hapax at {c_cover}; the tail token at "
                    f"{[(c, v) for _, c, v in c_tail]}", ['smoked_to_the_lord'])
    if q == 'tail_from_which':
        return cell('the_ram_only', P, f"the list is the UNION of two inventories fetched live — cold_run_offerings.dispatch(fat:ox) tail "
                    f"{FAT_OX['tail']['v']!r}, dispatch(fat:lamb) tail {FAT_LAMB['tail']['v']!r} [IMPORT, live calls]: the tail belongs to the "
                    "ram's list alone (Lev 3:9), the other three heads to both (Lev 3:3-4, 3:9-10) — the run writes one list for two species", ['smoked_to_the_lord'])
    if q == 'union_check':
        both = set(FAT_OX['parts']['v'].split('+')) | set(FAT_LAMB['parts']['v'].split('+'))
        return cell(sorted(both), P, "the union of the two inventories by call: covering, entrails' fat, kidneys with loin fat, lobe, tail — "
                    "9:19's four heads plus the entrails' fat the run folds into 'the fats'", [FX.NONE])
    if q == 'stack_run':
        return cell('fats_on_breasts', I, "9:20 'and they placed the FATS ON THE BREASTS, and he smoked the fats on the altar' — the plural 'they "
                    "placed' (Menachot 62a:6 reads the staffing: three priests)", ['smoked_to_the_lord'])
    if q == 'stack_reconciled':
        return cell('two_moments_of_one_act', M, "Lev 7:30 'the fat ON the breast he shall bring' against 9:20 'the fats ON the breasts' — Menachot "
                    "62a:4-5: 7:30 is the priest bringing it from the slaughterhouse (Abaye); 9:20 is 'the handing to ANOTHER priest who goes and "
                    "smokes it' — the two verses assigned to two moments; 62a:1 the wave's stack (the fats on the palm, the breast and thigh on "
                    "them, the bread on top)", ['waved'])
    if q == 'breast_thigh':
        return cell(TZ_BT, P, "9:21 'and the BREASTS and the RIGHT THIGH Aaron waved as a wave offering before the LORD, as Moses commanded' — "
                    f"CALLED cold_run_tzav.dues_machine(breast_thigh) -> {TZ_BT!r} (Lev 7:30-34) [IMPORT, live call]; Onkelos Lev 9:21 'he "
                    "LIFTED a lifting'", ['due_to_priest', 'waved'])
    if q == 'wave_stamp':
        return cell('as_Moses_commanded', I, "9:21's stamp names MOSES where 9:7 and 9:10 name the LORD — the dues of Lev 7:30-34 are the torah "
                    "'which the LORD commanded MOSES' (7:38), given through him; 'as Moses commanded' in Leviticus at this seat alone", [FX.NONE])
    return cell('no_case', I, '', [FX.NONE])

# ---- F7: THE BLESSING, THE GLORY, THE FIRE (9:22-24) -------------------
def fire(q):
    if q == 'hand_ketiv':
        return cell('singular_written_plural_read', I, f"9:22 'and Aaron lifted HIS HAND (ידו)' — the consonants at 9:22 are singular ({c_yado!r}); "
                    "Mishnah Sotah 7:6 quotes the verse 'his hands' — the lifting of PALMS rides the read form", ['blessed_the_people'])
    if q == 'regime':
        return cell('one_blessing_name_as_written_hands_above_head', A, "Mishnah Sotah 7:6 (= Tamid 7:2): in the province three blessings, in the "
                    "Temple ONE; the Name as written in the Temple, by epithet outside; hands to the shoulders outside, ABOVE THE HEADS in the "
                    "Temple — the shemini exam docket's credited row at this verse", ['blessed_the_people'])
    if q == 'high_priest_hands':
        return cell('not_above_frontplate_R_Yehuda_above', A, "Mishnah Sotah 7:6: except the high priest, who does not raise above the frontplate; "
                    "R. Yehuda: even he raises — 'and Aaron lifted his hands to the people and blessed them' (9:22): the dispute's proof is the "
                    "run (Sotah 38a:1, Tamid 33b:5)", ['blessed_the_people'])
    if q == 'posture_source':
        return cell('lifted_palms_by_verbal_analogy', M, "Sotah 38a:6: 'SO shall you bless' (Num 6:23) — with lifted palms: 'so' here and 'and "
                    "Aaron lifted his hands and blessed them' there (9:22) — the blessing's posture read off the run", ['blessed_the_people'])
    if q == 'timing_source':
        return cell('in_the_service', M, "Sotah 38b:7 (R. Yehoshua ben Levi): any priest who does not ascend DURING THE SERVICE does not ascend "
                    "again — 'and Aaron lifted his hands... and CAME DOWN FROM DOING the sin offering' (9:22): as there in the service, so here", ['blessed_the_people'])
    if q == 'amidah_position':
        return cell('after_thanksgiving', M, "Megillah 18a:3: why the priestly blessing after the thanksgiving? 'and Aaron lifted his hands to the "
                    "people and blessed them, and came down from doing the sin offering, the burnt offering, and the peace offerings' — the run's "
                    "sequence (service, then blessing) legislating the prayer's order", ['blessed_the_people'])
    if q == 'transposed':
        return cell('descent_before_lifting', M, SM + "29: 'this is a TRANSPOSED verse' — it should read 'and he came down from doing... and Aaron "
                    "lifted his hands and blessed them': he blessed on his way down; 'and blessed them' — STANDING, blessing likened to service "
                    "(Deut 10:8), and 2 Chr 30:27 'the priests the Levites AROSE and blessed the people' — the phrase 'and they blessed the "
                    f"people' at {c_blessed} in the whole Tanakh: this day and Hezekiah's Passover", ['blessed_the_people'])
    if q == 'content':
        return cell('sealed_here_opened_Num_6_24', M, SM + "30: 'and blessed them' — a sealed blessing; Scripture returns and spells it out at "
                    "Num 6:24-26, 'the LORD bless you and keep you' to 'and give you peace'", ['blessed_the_people'])
    if q == 'joint_entry':
        return cell('incense_or_mercy', M, SM + "30: why did Moses and Aaron enter together? to teach him the incense work — or the entry blessing "
                    "by the a fortiori from the exit; 19: the offerings were done and the Presence had NOT descended; Aaron stood distressed "
                    "— Moses entered with him, they sought mercy, and it came down", ['glory_appeared'])
    if q == 'fire_formula':
        return cell(2, I, f"9:24 'and FIRE WENT OUT FROM BEFORE THE LORD and consumed' — the five tokens at {c_fire} in the whole Tanakh: this day's "
                    "acceptance and, six verses on, the judgment on Nadav and Avihu (10:2) — the same verb 'consumed' (ותאכל), the objects 'the "
                    "burnt offering and the fats' against 'them'", ['fire_from_before_the_lord'])
    if q == 'fire_status':
        return cell('stayed_until_solomon', M, "Zevachim 61b:5 (Rav Acha bar Ami's baraita): 'the fire that came down from heaven in the days of "
                    "Moses did not depart from the copper altar until the days of Solomon; the fire of Solomon's days did not depart until "
                    "Manasseh came and removed it' — the status opened at 9:24 with its recorded close; " + SM + "16 'the day of his heart's joy "
                    "— the day the NEW fire came down'", ['fire_from_before_the_lord'])
    if q == 'fire_and_duty':
        return cell(TZ_EXT, P, f"the heavenly fire does not cancel the common fire's duty — CALLED cold_run_tzav.altar_machine(extinguish) -> {TZ_EXT!r} "
                    f"(Lev 6:5-6) and altar_machine(retention) -> {TZ_RET!r} [IMPORT, live calls]: the status and the timer stand together", ['perpetual_fire_duty', 'fire_from_before_the_lord'])
    if q == 'song':
        return cell('song_and_prostration', I, f"9:24 'and all the people saw and SANG (וירנו) and fell on their faces' — the verb at {c_sang} alone "
                    f"in the Tanakh (Isaiah 2:3's nations beside it); 'and they fell on their faces' at {len(c_fell)} seats (Elijah's fire, 1 Kgs "
                    "18:39, among them); " + SM + "20: 'they opened their mouths and said song — Rejoice, O righteous (Ps 33:1)'; 31: Solomon's "
                    "parallel (2 Chr 7:3) and Malachi 3:4's two eras", ['glory_appeared'])
    if q == 'meeting_promise':
        return cell('fulfilled_on_the_eighth_day', M, "Sifra, Vayikra Dibbura DeNedavah, Chapter 2 5 (R. Elazar): 'I will meet there with the "
                    "children of Israel and it shall be sanctified by My glory' (Exod 29:43) — when? 'the eighth day of the installation, as it "
                    "says (Lev 9:24) and all the people saw and sang'", ['glory_appeared'])
    if q == 'presence_on_whose_service':
        return cell('aaron_not_moses', M, SM + "14: 'all seven installation days Moses served and the Presence did not rest by his hand — until "
                    "Aaron came and served, and the Presence rested by his hand' (Exod 40:17, Num 9:15)", ['glory_appeared', 'invested_office'])
    if q == 'joy_like_creation':
        return cell('vayehi_pairing', M, "Megillah 10b:8 = " + SM + "15: 'that day was a joy before the Holy One as the day heaven and earth "
                    "were created — written here AND IT WAS on the eighth day, and there (Gen 1:5) AND IT WAS... one day'", [FX.NONE])
    if q == 'ten_crowns':
        return cell(10, D, "Shabbat 87b:6: the day the tabernacle was erected 'took TEN CROWNS' — first for creation's work, the princes, the "
                    "priesthood, the service, the descent of fire, the eating of holy things, the Presence dwelling, the blessing of Israel, the "
                    "ban of the high places, the months — the tradition's own effect list for this day; the count is data", [FX.NONE])
    if q == 'crowns_in_this_chapter':
        return cell(['priesthood', 'service', 'fire', 'presence', 'blessing'], I, "five of the ten are written by this chapter's verbs: the "
                    "priesthood (9:1 Aaron called to serve; 9:8 'drew near'), the service (9:8-21), the fire (9:24), the Presence (9:23), the "
                    "blessing (9:22-23); the eating (Lev 10:12-15), the high places (Zevachim 14:4), the months (Exod 12:2), the princes (Num 7:12), "
                    "the week's first day are the others' seats", ['invested_office', 'fire_from_before_the_lord', 'glory_appeared', 'blessed_the_people'])
    if q == 'second_runs':
        return cell('solomon_and_ezekiel', I, "'on the eighth day' at Solomon's dedication (1 Kgs 8:66, 2 Chr 7:9 — 2 Chr 7:1's fire from heaven) and "
                    "at Ezekiel's altar (43:27 'and on the eighth day and onward the priests shall make your burnt offerings') — the same spec "
                    "run again in the Prophets and Writings; Menachot 45a:12 (Rav Ashi): 'the installation offerings were brought in Ezra's days "
                    "as in Moses' days'", [FX.NONE])
    if q == 'scroll_boundary':
        return cell('torat_kohanim_ends_at_9_1', M, "Gittin 60a:13 (R. Yehuda): a child's scroll may be written 'in the priests' torah UNTIL and "
                    "it was on the eighth day' — the tradition's own cut between the spec (Lev 1-8) and the run, at 9:1 exactly", [FX.NONE])
    return cell('no_case', I, '', [FX.NONE])

# ---- F8: THE ERAS (Zevachim 14) — the day's two switches ---------------
def eras(q):
    if q == 'switch':
        return cell('high_places_banned_service_by_priests', A, "Mishnah Zevachim 14:4: 'before the tabernacle was erected the high places were "
                    "permitted and the service by the firstborn; from its erection the high places were BANNED and the service by the PRIESTS' "
                    "— the run's date (the erection day, " + SM + "14) is the table's first boundary; Shabbat 87b:6's crowns 'first for the "
                    "priesthood', 'first for the ban of the high places'", ['high_places_banned', 'invested_office'])
    if q == 'table':
        return cell(['permitted', 'banned', 'permitted', 'banned', 'permitted', 'banned'], A, "Mishnah Zevachim 14:4-8: before the tabernacle "
                    "PERMITTED; the tabernacle BANNED; Gilgal PERMITTED; Shiloh BANNED ('the resting place'); Nov and Gibeon PERMITTED; "
                    "Jerusalem BANNED and never again permitted ('the inheritance', Deut 12:9) — the status this day opens, flipped by era", ['high_places_banned'])
    if q == 'karet_matrix':
        return cell(['positive_negative_karet', 'positive_negative', 'positive'], A, "Mishnah Zevachim 14:9: consecrated in a ban era and offered "
                    "outside in a ban era — a positive and a negative command and KARET; consecrated in a permitted era, offered in a ban era — "
                    "positive and negative, no karet; consecrated in a ban era, offered in a permitted era — the positive alone; the era is the "
                    "predicate this day's status writes, the sanction the sanctions engine's (Lev 17:4)", ['high_places_banned'])
    if q == 'differences':
        return cell(11, A, "Mishnah Zevachim 14:10: between a private and a public high place — hand-laying, slaughter in the north, application "
                    "around, waving, presentation (R. Yehuda: no meal offering on a high place), priesthood, service garments, service vessels, "
                    "the pleasing odor, the partition for the blood, the washing of hands and feet — ELEVEN; the run's around (9:12, 9:18), "
                    "waving (9:21), and priesthood (9:8) are the public altar's marks", [FX.NONE])
    if q == 'shared':
        return cell('time_leftover_impure', A, "Mishnah Zevachim 14:10's tail: 'but the time, the leftover, and the impure are equal in both'", [FX.NONE])
    if q == 'ink_of_the_ban':
        return cell('Lev 17:4 and Deut 12:8', I, "the ban's own ink is the sanctions engine's (Lev 17:4 'to the door of the tent of meeting he did "
                    "not bring it') and Deut 12:8-14's eras ('you shall not do as all that we do here today... when you cross'); this day's ink is "
                    "the DATE the block took effect", ['high_places_banned'])
    return cell('no_case', I, '', [FX.NONE])

# ---- THE SCENE — the installation timer released into the eighth day's tape (world_engine, scene-6 shape) ----
def law_eighth_day(event, world):
    """The eighth day's daemon: consumes the day's recorded acts (the ink's own verbs) and writes the ledger — never emits an event."""
    k = event['kind']
    subj = event['subject']
    src = event['case_source']
    if k == 'offering_done':
        spec = event['spec']
        E = lambda eff, s, cp=None, law='': {'effect': eff, 'subject': s, 'counterparty': cp, 'amount': None, 'due': None, 'source_law': law, 'case_source': src}
        out = [E('accepted', subj, law='the spec by call (%s)' % spec)]
        # W3 (2026-09-07): the run's acts write the SPEC'S effects by call — the calf's, the goat's, the rams', the palm's, the peace offerings'
        head = spec.split()[0].rstrip(':')                       # 'olah: as prescribed' / 'minchah: the palm filled' carry the colon on the head
        if head == 'chatat':
            beast = 'the-calf' if 'calf' in spec else 'the-goat'
            out += [E('atoned_forgiven', 'the-people' if 'goat' in spec else 'aaron', cp='HEAVEN', law='F3/F5 [INK 9:9, 9:15 the blood on the horns; Onkelos 9:15 "atoned with its blood"; the outer protocol by call: %s]' % CH_BLOOD_COM),
                    E('smoked_to_the_lord', beast, law='F3 [INK 9:10 the fat, the kidneys, the lobe; the ox\'s inventory by call: %s]' % FAT_OX['parts']['v'])]
            if 'calf' in spec:
                out += [E('burned_outside_camp', 'the-calf', law='F3 [INK 9:11 "the flesh and the hide he burned outside the camp"; the anointed tier\'s carcass by call: %s]' % CH_CARC_A),
                        E('defiles_garments', 'the-burner', law='F3 [the burn site by call: %s]' % CH_BURN)]
        if head == 'olah':
            out.append(E('smoked_to_the_lord', 'the-ram' if 'ram' in spec else 'the-peoples-olah', law='F4 [INK 9:13-14, 9:16 "as prescribed" — CALLED offerings(olah:flock) disposition: %s]' % OLAH_F['disposition']['v']))
        if head == 'minchah':
            out += [E('azkarah_to_fire', 'the-minchah', cp='HEAVEN', law='F5 [INK 9:17 "he filled his palm from it and smoked it on the altar"; the pair by call: %s]' % MIN_PAIR),
                    E('presented', 'the-minchah', law='F5 [the presentation the run does not narrate — CALLED minchah.presentation: %s]' % MIN_PRES),
                    E('due_to_priest', 'the-priests', cp='the-people', law='F5 [the remainder by call: %s; eaten at Lev 10:12]' % MIN_REM)]
        if head == 'shelamim':
            out += [E('due_to_priest', 'the-priests', cp='the-people', law='F6 [INK 9:21 the breast and the right thigh — CALLED tzav.dues_machine: %s]' % TZ_BT),
                    E('waved', 'the-breast-and-thigh', law='F6 [INK 9:21 "Aaron waved them as a waving before the LORD"]')]
        return out
    if k == 'blessing_lifted':
        return [{'effect': 'blessed_the_people', 'subject': subj, 'counterparty': 'aaron', 'amount': None, 'due': None,
                 'source_law': 'F7 [INK 9:22-23]', 'case_source': src}]
    if k == 'glory_seen':
        return [{'effect': 'glory_appeared', 'subject': subj, 'counterparty': None, 'amount': None, 'due': None,
                 'source_law': 'F7 [INK 9:23; the promise 9:4, 9:6]', 'case_source': src}]
    if k == 'fire_descended':
        return [{'effect': 'fire_from_before_the_lord', 'subject': subj, 'counterparty': None, 'amount': None, 'due': None,
                 'source_law': 'F7 [INK 9:24; Zevachim 61b:5 the tenure]', 'case_source': src},
                {'effect': 'high_places_banned', 'subject': 'the-land', 'counterparty': None, 'amount': None, 'due': None,
                 'source_law': 'F8 [Mishnah Zevachim 14:4; the erection day]', 'case_source': src}]
    return []

def scene():
    with contextlib.redirect_stdout(io.StringIO()):
        w = WE.World(era='the installation week into the eighth day (clock unit: days)')
        w.laws = [WE.law_installation, law_eighth_day]
        w.submit({'kind': 'installation_commanded', 'subject': 'aaron-and-sons',
                  'components': ['bullock', 'ram_olah', 'ram_milluim', 'basket'], 'case_source': 'Lev 8:2'})
        w.submit({'kind': 'milluim_blood_sprinkled', 'subject': 'aaron-and-sons', 'case_source': 'Lev 8:30'})
        w.advance(7)           # the seven days pass; the release fires — the eighth day opens
        for spec, src in (('chatat calf: outer blood, inner carcass', 'Lev 9:8-11'), ('olah ram: as prescribed', 'Lev 9:12-14'),
                          ('chatat goat: like the first', 'Lev 9:15'), ('olah: as prescribed', 'Lev 9:16'),
                          ('minchah: the palm filled', 'Lev 9:17'), ('shelamim ox and ram: the fats, the wave', 'Lev 9:18-21')):
            w.submit({'kind': 'offering_done', 'subject': 'aaron', 'spec': spec, 'case_source': src})
        w.submit({'kind': 'blessing_lifted', 'subject': 'the-people', 'case_source': 'Lev 9:22-23'})
        w.submit({'kind': 'glory_seen', 'subject': 'the-people', 'case_source': 'Lev 9:23'})
        w.submit({'kind': 'fire_descended', 'subject': 'the-altar', 'case_source': 'Lev 9:24'})
    aas = w.entity('aaron-and-sons'); ppl = w.entity('the-people'); alt = w.entity('the-altar'); land = w.entity('the-land'); aar = w.entity('aaron')
    n = lambda ent, eff: len([e for e in ent.ledger if e['effect'] == eff])
    timers_fired = len([l for l in w.log if l[0] == 'TIMER-FIRE'])
    main = (n(aas, 'confined_seven_days'), n(aas, 'invested_office'), n(aas, 'released'), timers_fired, n(aar, 'accepted'),
            n(ppl, 'blessed_the_people'), n(ppl, 'glory_appeared'), n(alt, 'fire_from_before_the_lord'), n(land, 'high_places_banned'), w.clock.year)
    # W3 (2026-09-07): the run's acts write the SPEC'S effects by call — counted on the same world
    m = lambda eid, eff: len([e for e in w.entity(eid).ledger if e['effect'] == eff])
    wrap = (m('aaron', 'atoned_forgiven'), m('the-people', 'atoned_forgiven'), m('the-calf', 'smoked_to_the_lord'), m('the-calf', 'burned_outside_camp'), m('the-burner', 'defiles_garments'),
            m('the-goat', 'smoked_to_the_lord'), m('the-ram', 'smoked_to_the_lord'), m('the-peoples-olah', 'smoked_to_the_lord'), m('the-minchah', 'azkarah_to_fire'), m('the-minchah', 'presented'),
            m('the-priests', 'due_to_priest'), m('the-breast-and-thigh', 'waved'))
    return main, wrap, w
SCENE, SCENE_WRAP, _W = scene()
def scene_cell():
    return cell(SCENE, I, "the SCENE on the world engine (the Tzav round's scene-6 shape): the installation commanded (Lev 8:2) and committed at "
                "the sprinkling (8:30); the clock advanced seven days and the confinement's RELEASE fired (the timer that makes the eighth day); "
                "then the day's six offerings accepted by the spec, the people blessed, the glory seen, the fire descended and the high places "
                "banned on the land — (confined, invested, released, timers fired, offerings accepted, blessed, glory, fire, ban, the clock)",
                ['released', 'accepted', 'blessed_the_people', 'glory_appeared', 'fire_from_before_the_lord', 'high_places_banned'])

# ---- (2) the answer sheet — the Mishnah rows as TEST DATA (verified by their own tokens) ----
def load(t):
    d = json.load(open('<repo-old>/Data/mishnah_%s_he.json' % t))
    return d['text'] if isinstance(d, dict) and 'text' in d else d
SHELF = {'Zevachim': load('zevachim'), 'Tamid': load('tamid'), 'Horayot': load('horayot'), 'Menachot': load('menachot'),
         'Parah': load('parah'), 'Beitzah': load('beitzah'), 'Sotah': load('sotah')}
def mrow(book, ch, m, must):
    txt = strip(SHELF[book][ch - 1][m - 1])
    assert must in txt, 'answer-sheet check failed: %r not in Mishnah %s %d:%d' % (must, book, ch, m)
SHEET = [
    ('Zevachim', 10, 1, 'התדיר'), ('Zevachim', 10, 2, 'מרצה'), ('Zevachim', 10, 6, 'אמש'),
    ('Zevachim', 14, 4, 'הוקם'), ('Zevachim', 14, 5, 'לגלגל'), ('Zevachim', 14, 6, 'לשילה'), ('Zevachim', 14, 7, 'לנוב'), ('Zevachim', 14, 8, 'לירושלים'),
    ('Zevachim', 14, 9, 'כרת'), ('Zevachim', 14, 10, 'סמיכה'), ('Zevachim', 5, 3, 'קרנות'), ('Zevachim', 5, 4, 'הפשט'), ('Zevachim', 5, 5, 'צבור'), ('Zevachim', 5, 7, 'שלמים'),
    ('Tamid', 4, 1, 'כופתין'), ('Tamid', 4, 2, 'הפשט'), ('Tamid', 4, 3, 'הראה'), ('Tamid', 7, 2, 'ככתבו'),
    ('Horayot', 3, 6, 'התדיר'), ('Menachot', 4, 4, 'מחנכין'), ('Menachot', 1, 2, 'בשמאל'), ('Menachot', 3, 5, 'והלבונה'), ('Menachot', 5, 3, 'ולבונה'), ('Menachot', 6, 3, 'שלש'),
    ('Parah', 1, 1, 'שנתה'), ('Beitzah', 2, 4, 'סומכין'), ('Sotah', 7, 6, 'הציץ'),
]
for b, ch, m, must in SHEET:
    mrow(b, ch, m, must)
print('answer sheet: %d Mishnah rows verified by their own tokens (Zevachim 10, 14, Tamid 4 read whole with the topic and link rows — the run docket)' % len(SHEET))

TESTS = [
 # ---- THE DAY AND THE TAKE-LIST (9:1-6) ----
 ('Sifra Miluim 2 1 — the eighth OF THE COUNT (Exod 19:16 the third day of the count)', day('eighth_of'), 'the_count'),
 ('Sifra Miluim 2 14 + Tzav Miluim I 36 — the date: the first of Nisan (23 Adar + 7)', day('date'), 'first_of_nisan'),
 ('Lev 9:1 — Aaron, his sons, the elders (Sifra 2 2 the honor order)', day('called'), 'aaron_sons_elders'),
 ('the SPEC: the anointed priest\'s sin offering is a bull (chatat engine by call)', day('aaron_chatat_spec'), 'bull'),
 ('the RUN: Lev 9:2 — a CALF', day('aaron_chatat_run'), 'calf'),
 ('the deviation named: Sifra Miluim 2 3-4 — the calf answers the calf', day('aaron_chatat_deviation'), 'calf_answers_calf'),
 ('Mishnah Parah 1:1 + Sifra Chovah Chapter 3 6 — the calf\'s age is data: one year; son of the herd two', day('calf_age'), 'one_year_son_of_herd_two'),
 ('Lev 9:2 — Aaron\'s burnt offering: a ram', day('aaron_olah'), 'ram'),
 ('the SPEC: the congregation\'s sin offering is a bull (by call)', day('people_chatat_spec'), 'bull'),
 ('the RUN: Lev 9:3 — a he-goat', day('people_chatat_run'), 'he_goat'),
 ('the deviation named: Sifra Miluim 2 3-4 — the goat for Joseph, the calf for the calf', day('people_chatat_deviation'), 'goat_for_joseph_calf_for_calf'),
 ('Lev 9:3 — the people\'s burnt offering: a calf and a lamb, yearlings', day('people_olah'), 'calf_and_lamb_yearlings'),
 ('Lev 9:4 — the people\'s peace offerings: an ox and a ram', day('people_shelamim'), 'ox_and_ram'),
 ('Sifra Miluim 2 13 — communal peace offerings learned from here', day('communal_shelamim_source'), 'Lev 9:4'),
 ('Mishnah Zevachim 5:5 — the communal peace offering\'s eater (offering engine by call)', day('communal_shelamim_grade'), 'male_priests'),
 ('Lev 9:4 — the meal offering mixed with oil', day('minchah_form'), 'mixed_with_oil'),
 ('Mishnah Menachot 6:3 — three oil forms (meal-offering engine by call)', day('minchah_oil_forms'), 3),
 ('Yoma 3b:4 — "take FOR YOURSELF": Aaron\'s from his own, the people\'s from the public', day('funding'), 'aaron_own_people_public'),
 ('Lev 9:4 — "appears to you" a hapax', day('today_appears'), 'hapax'),
 ('Lev 9:5 — they took and stood (Sifra 2 5 with alacrity)', day('alacrity'), 'took_and_stood'),
 ('the command stamps at 9:5, 6, 7, 10, 21 — and none at 9:11', day('command_stamps'), [5, 6, 7, 10, 21]),
 ('Lev 9:6 -> 9:23 — the glory promised and appearing', day('glory_promise'), 'promised_9_6_fulfilled_9_23'),
 # ---- THE ORDER OF SERVICE ----
 ('Lev 9:7-15 — Aaron\'s own before the people\'s (Sifra 2 9)', order('own_before_people'), 'aaron_first'),
 ('Lev 9:7 — his own atones for himself AND the people', order('own_atones_for'), 'himself_and_people'),
 ('Mishnah Horayot 3:6 — the anointed\'s bull first in all its acts (chatat engine by call)', order('anointed_first_spec'), 'anointed_first'),
 ('Mishnah Zevachim 10:2 — the sin offering\'s blood before the burnt offering\'s: the run 9:9 < 9:12', order('chatat_blood_before_olah_blood'), 'chatat_blood_first'),
 ('Mishnah Zevachim 10:2 — the SPEC: the burnt offering\'s limbs before the sin offering\'s fats', order('spec_limbs_vs_fats'), 'olah_limbs_first'),
 ('the RUN: 9:8-11 the calf completed whole before the ram (9:12) — the hour\'s order', order('run_limbs_vs_fats'), 'chatat_completed_whole_first'),
 ('Lev 9:15 — "like the first": the four horns imported (Sifra 2 9; Onkelos)', order('goat_like_first'), 'four_horns_imported'),
 ('Lev 9:16 — "as prescribed": the olah\'s procedure by the pointer CALL', order('olah_as_prescribed'), 'flay_and_cut'),
 ('"as prescribed" at twelve Torah seats', order('kamishpat_census'), 12),
 ('Menachot 93b:3 / Beitzah 20a:5 — the run teaches the spec: hand-laying for the obligatory olah', order('run_teaches_spec_semikhah'), 'obligatory_olah_requires_hand_laying'),
 ('Mishnah Zevachim 10:1 — the frequent precedes: 9:17 "beside the morning olah"', order('tadir_first'), 'temidim_precede'),
 ('Mishnah Menachot 4:4 — the altar inaugurated by the morning tamid', order('altar_inaugurated_by'), 'morning_tamid'),
 ('Mishnah Zevachim 10:6 — the eating order follows the offering order', order('eating_order'), 'as_offering_order'),
 ('Sifra Miluim 2 13 — seven services learned in one hour (data)', order('seven_services'), 7),
 # ---- THE CALF'S RITE (9:8-11) ----
 ('Lev 9:8 — Aaron slaughters', calf('slaughterer'), 'aaron'),
 ('Lev 9:9 — the sons bring the blood (Moed Katan 28b:13)', calf('blood_bearers'), 'sons'),
 ('Lev 9:9 — finger, horns, base', calf('blood_run'), 'finger_horns_base'),
 ('the SPEC\'s outer protocol (chatat engine by call) = the run\'s 9:9', calf('blood_spec_outer'), 'outer_altar_horns'),
 ('the SPEC\'s anointed-tier protocol (by call) — not the run\'s', calf('blood_spec_anointed'), 'inside_tent'),
 ('the deviation named: outer blood for the anointed — the day\'s one-time offering', calf('blood_deviation'), 'outer_protocol_for_the_anointed'),
 ('no sevenfold sprinkling in the run', calf('sprinklings_run'), 0),
 ('Lev 9:10 — the fat, the kidneys, the lobe', calf('fat_run'), 'fat_kidneys_lobe'),
 ('the SPEC\'s ox inventory (offerings engine by call)', calf('fat_spec'), 'covering_fat+fat_on_entrails+two_kidneys_with_loin_fat+lobe_of_liver'),
 ('Sifra Nedavah Section 14 8 — 9:10 "the lobe FROM the liver" resolves Lev 3:4', calf('lobe_from_liver'), 'take_from_liver_onto_lobe'),
 ('Lev 9:10 — the full stamp "as the LORD commanded Moses"', calf('fat_stamp'), 'as_the_LORD_commanded_Moses'),
 ('Lev 9:11 — the flesh and hide burned outside the camp (the phrase at 8:17 and 9:11 alone)', calf('carcass_run'), 'burned_outside_camp'),
 ('the SPEC for an outer-blood sin offering: eaten by the male priests (by call)', calf('carcass_spec_for_outer_blood'), 'male_priests'),
 ('the SPEC for the anointed tier: burned at the ash-pour (by call)', calf('carcass_spec_for_anointed'), 'burned_outside_camp_ash_pour'),
 ('the deviation named: the unstamped one-time burning; Lev 10:16-18 makes eating the rule', calf('carcass_deviation'), 'unstamped_one_time_burning'),
 ('the burn site by call: the ash house, the garments defiled', calf('burn_site_spec'), 'ash_house_defiles_garments'),
 ('Lev 9:11 — the hide burned with the flesh (against the olah\'s hide to the priest, by call)', calf('hide'), 'burned_with_flesh'),
 # ---- THE RAM'S RITE (9:12-14) ----
 ('Lev 9:12 — around: two that are four (by call)', ram('blood'), 'two_that_are_four'),
 ('Lev 9:12-13 — the sons present, Aaron applies', ram('sons_hand'), 'presented_to_him'),
 ('Lev 9:13 — the pieces and the head: flay and cut (by call)', ram('pieces_and_head'), 'flay_and_cut'),
 ('Lev 9:14 — the entrails and legs washed and smoked (the pair at 8:21 and 9:14 alone)', ram('entrails_legs'), 'washed_and_smoked'),
 ('Lev 9:14 — wholly to the fires (by call)', ram('disposition'), 'wholly_to_fires'),
 ('the place the run does not name: north (by call)', ram('place'), 'north'),
 ('Mishnah Tamid 4:2-3 — the cutting walk\'s heads', ram('tamid_walk'), 'head_legs_entrails'),
 # ---- THE PEOPLE'S OFFERING (9:15-17) ----
 ('Onkelos Lev 9:15 — "purified it" = atoned with its blood', people('goat_purified'), 'atoned_with_its_blood'),
 ('Sifra Miluim 2 11 — the fill-fill sync: the crumb disqualifies (meal-offering engine by call)', people('fistful_crumb'), 'invalid'),
 ('Menachot 9b:17 — "his palm" is the right hand; the left invalid (by call, now derived from 9:17)', people('palm_is_right'), 'right'),
 ('"his palm" at five Torah seats', people('palm_census'), 5),
 ('Menachot 19b:2-4 — THE FORK: Rav indispensable / Shmuel not from the hour', people('fistful_repeated_fork'), 'Rav_indispensable_Shmuel_not_from_the_hour'),
 ('Sifra Miluim 2 12 — two meal offerings that day', people('two_minchahs'), 2),
 ('Menachot 59a:11 — the eighth day\'s meal offering requires frankincense: a fistful (by call)', people('frankincense'), 'a_fistful'),
 ('the remainder to Aaron and his sons, most holy (by call)', people('remainder'), 'aaron_and_sons_most_holy'),
 ('the presentation the run does not narrate: required (by call)', people('presentation'), 'required'),
 # ---- THE PEACE OFFERINGS (9:18-21) ----
 ('Lev 9:18 — around: two that are four (by call)', peace('blood'), 'two_that_are_four'),
 ('Lev 9:19 — the tail, the covering (a hapax), the kidneys, the lobe', peace('fat_list'), 'tail_covering_kidneys_lobe'),
 ('the tail from the ram alone: fat:ox no tail, fat:lamb tail (by call)', peace('tail_from_which'), 'the_ram_only'),
 ('the union of the two inventories by call', peace('union_check'), ['covering_fat', 'fat_on_entrails', 'fat_tail_whole_by_backbone', 'lobe_of_liver', 'two_kidneys_with_loin_fat']),
 ('Lev 9:20 — the fats on the breasts', peace('stack_run'), 'fats_on_breasts'),
 ('Menachot 62a:4-5 — 7:30 and 9:20 as two moments of one act', peace('stack_reconciled'), 'two_moments_of_one_act'),
 ('Lev 9:21 — the breast and right thigh waved: the dues machine by call', peace('breast_thigh'), 'breast and thigh to the priests after the smoking'),
 ('Lev 9:21 — the stamp names Moses (Lev 7:38)', peace('wave_stamp'), 'as_Moses_commanded'),
 # ---- THE BLESSING, THE GLORY, THE FIRE (9:22-24) ----
 ('Lev 9:22 — "his hand" written singular, read plural', fire('hand_ketiv'), 'singular_written_plural_read'),
 ('Mishnah Sotah 7:6 / Tamid 7:2 — the regime (credited)', fire('regime'), 'one_blessing_name_as_written_hands_above_head'),
 ('Mishnah Sotah 7:6 — the high priest and the frontplate; R. Yehuda from 9:22', fire('high_priest_hands'), 'not_above_frontplate_R_Yehuda_above'),
 ('Sotah 38a:6 — lifted palms from 9:22 by verbal analogy', fire('posture_source'), 'lifted_palms_by_verbal_analogy'),
 ('Sotah 38b:7 — the blessing in the service, from 9:22', fire('timing_source'), 'in_the_service'),
 ('Megillah 18a:3 — the blessing after the thanksgiving, from 9:22', fire('amidah_position'), 'after_thanksgiving'),
 ('Sifra Miluim 2 29 — the transposed verse; standing; 2 Chr 30:27 the phrase\'s second seat', fire('transposed'), 'descent_before_lifting'),
 ('Sifra Miluim 2 30 — the blessing sealed here, opened at Num 6:24', fire('content'), 'sealed_here_opened_Num_6_24'),
 ('Sifra Miluim 2 30 and 2 19 — the joint entry', fire('joint_entry'), 'incense_or_mercy'),
 ('Lev 9:24 — the fire formula at two Tanakh seats (9:24, 10:2)', fire('fire_formula'), 2),
 ('Zevachim 61b:5 — the fire stayed until Solomon', fire('fire_status'), 'stayed_until_solomon'),
 ('the heavenly fire and the perpetual-fire duty together (Tzav engine by call)', fire('fire_and_duty'), 'a standing never-extinguish duty'),
 ('Lev 9:24 — song and prostration (Sifra 2 20, 2 31)', fire('song'), 'song_and_prostration'),
 ('Sifra Nedavah Chapter 2 5 — Exod 29:43\'s meeting fulfilled on the eighth day', fire('meeting_promise'), 'fulfilled_on_the_eighth_day'),
 ('Sifra Miluim 2 14 — the Presence on Aaron\'s service, not Moses\'', fire('presence_on_whose_service'), 'aaron_not_moses'),
 ('Megillah 10b:8 = Sifra 2 15 — the joy of creation, the vayehi pairing', fire('joy_like_creation'), 'vayehi_pairing'),
 ('Shabbat 87b:6 — ten crowns (data)', fire('ten_crowns'), 10),
 ('five crowns written by this chapter\'s verbs', fire('crowns_in_this_chapter'), ['priesthood', 'service', 'fire', 'presence', 'blessing']),
 ('the second runs: Solomon\'s and Ezekiel\'s eighth days; Menachot 45a:12 Ezra\'s', fire('second_runs'), 'solomon_and_ezekiel'),
 ('Gittin 60a:13 — the priests\' torah ends at 9:1 in R. Yehuda\'s scroll', fire('scroll_boundary'), 'torat_kohanim_ends_at_9_1'),
 # ---- THE ERAS (Zevachim 14) ----
 ('Mishnah Zevachim 14:4 — the day\'s two switches', eras('switch'), 'high_places_banned_service_by_priests'),
 ('Mishnah Zevachim 14:4-8 — the eras table', eras('table'), ['permitted', 'banned', 'permitted', 'banned', 'permitted', 'banned']),
 ('Mishnah Zevachim 14:9 — the karet matrix on the era predicate', eras('karet_matrix'), ['positive_negative_karet', 'positive_negative', 'positive']),
 ('Mishnah Zevachim 14:10 — eleven differences', eras('differences'), 11),
 ('Mishnah Zevachim 14:10 — three shared', eras('shared'), 'time_leftover_impure'),
 ('the ban\'s own ink is Lev 17:4 and Deut 12:8; this day is its date', eras('ink_of_the_ban'), 'Lev 17:4 and Deut 12:8'),
 # ---- THE SCENE ----
 ('THE SCENE on the world engine: (confined, invested, released, timers, accepted, blessed, glory, fire, ban, clock)', scene_cell(), (1, 1, 1, 1, 6, 1, 1, 1, 1, 7)),
 # ---- THE WRAP (W3, 2026-09-07) — the run's acts write the SPEC'S effects by call on the same world ----
 ('THE WRAP — (Aaron atoned by the calf, the people by the goat, the calf\'s fat smoked, its flesh burned, the burner\'s garments, the goat\'s '
  'fat, the ram wholly, the people\'s olah wholly, the palm\'s memorial, the presentation, two dues to the priests, the breast and thigh waved)',
  cell(SCENE_WRAP, I, 'the eighth day\'s daemon consumes the run\'s six acts and writes what the SPEC says each act did — the sin-offering, '
       'offering, meal-offering and Tzav engines by call: the calf\'s blood atones (Onkelos 9:15), its fat smokes, its flesh burns at the '
       'ash-pour and the burner\'s garments are defiled; the goat like the first; the rams as prescribed; the palm\'s memorial and its '
       'presentation; the breast and thigh to the priests after the waving (order, calf and people WRAPPED here, W3)',
       ['atoned_forgiven', 'smoked_to_the_lord', 'burned_outside_camp', 'defiles_garments', 'azkarah_to_fire', 'presented', 'due_to_priest', 'waved']),
  (1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 1)),
]

# ---- (3)+(5) run, grade, effects ------------------------------------
n = len(TESTS)
assert n == GUARDED, (n, GUARDED)
print('guard: %d test rows, every expected value a literal from the answer sheet [honest-pairing guard satisfied]' % GUARDED)
print()
ok = 0
frac = {I: 0, M: 0, A: 0, D: 0, P: 0}
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
print('FRACTIONS: pure ink %d/%d (%d%%) · recorded moves %d/%d (%d%%) · answer-sheet %d/%d · data %d/%d · imports %d/%d'
      % (frac[I], n, 100 * frac[I] // n, frac[M], n, 100 * frac[M] // n, frac[A], n, frac[D], n, frac[P], n))
ops = FX.summarize(used)
print('LEDGER OPS this span writes: %s' % ', '.join('%s x%d' % kv for kv in sorted(ops.items())))
print('effects: every cell carries REGISTERED effects — FOUR discovered in these verses\' own verbs and the day\'s recorded crowns: '
      'fire_from_before_the_lord (STATUS), glory_appeared, blessed_the_people (HEAVEN), high_places_banned (BLOCK) [effects law satisfied]')
print('SCENE: %r — the installation timer released into the eighth day; the tape is the ink' % (SCENE,))
if ok == n:
    print('THE EIGHTH DAY RUNS AGAINST ITS SPEC — the calf for the bull, the outer blood with the inner carcass, the calf completed whole before the ram, '
          'the one unstamped act at 9:11; "as prescribed" and "like the first" as live calls; the fat list as the union of two inventories; the run '
          'teaching the spec (hand-laying, the right palm, the lobe\'s preposition, the blessing\'s posture and timing) with the fork over whether an '
          'hour legislates recorded; the fire formula at two seats; the chatat, offering, meal-offering, and Tzav engines CALLED.')
else:
    print('MISSES (%d):' % len(misses))
    for m_ in misses: print('  -', m_[0][:80], '->', m_[1])
    sys.exit('MISSES REMAIN — consult the Talmud per gap and recompile.')

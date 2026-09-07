#!/usr/bin/env python3
"""cold_run_sanctuary_build.py — THE SANCTUARY SPEC GRADED AGAINST ITS OWN CONSTRUCTION RUN
(Exod 25:1-27:21 the SPEC; Exod 35:30-38:31 the RUN — 2026-09-06, sitting E2 of THE COMPILE
DEBT, World/step9/COMPILE_DEBT.md; the fifth runner compiled under THE DEPENDENCY GATE's rule:
span declared, a stub placed, the census run, three required edges and two pointers
dispositioned BEFORE the first cell, four more declared for the live calls the compile made,
and the run's cross-references into Exod 30 — the incense altar, the laver, the half shekel,
the anointing oil — made VISIBLE to the gate by extending its vocabulary, OWED to E4.)

The form: DEMONSTRATE-BY-RUN inside one book (the D8 shape, moved from Leviticus to Exodus).
Exod 25-27 is the SPEC — the offering, the ark, the table, the lampstand, the curtains, the
boards, the veil and screen, the altar, the court, the lamp's oil; Exod 35:30-38:31 is the RUN —
the workforce, the overflow and the halt, then every vessel built verb by verb, then the
accounts. The runner compiles the spec from its ink (every measure in the cubit of Moses, a
PARAMETER whose recorded settings the sheet supplies) and grades the run as a SCENE against
it: each run verse aligned to its spec verse by token, the ORDER of the build against the order
of the command, the verses the run DROPS (every use-clause and every pattern-clause), the
tokens the run ADDS (the silver heads of the pillars, the named maker of the ark, 'one to one'
for 'a woman to her sister'), the arithmetic the spec's own numbers close (forty cubits of
curtain over thirty of length and ten of height; ninety-six sockets under the boards and four
under the veil = the accounts' hundred talents, a talent a socket; the talent itself computed
as three thousand shekels from the census silver), and the divergences named and sourced: the
run builds the HOUSE before the ARK against the spec's ark-first — the recorded fork at Berakhot
55a (the run's order is God's, Moses reversed it) against the spine's recension (the roles
reversed) — THE RUN RESTORES THE SPEC'S ORDER, move M-22 in a new form.

Answer sheet ROUTED BY TOPIC under the union rule: Mishnah Middot WHOLE (the descendant floor
plan as DATA), Shekalim 4-6, Yoma 5, Kelim 1, Menachot 11 and Tamid 3 (credited from sitting
L5) + ten topic rows + the fifteen link rows — 109 rows, the ledger
logic/oral_triage/sanctuary_build_docket_2026-09-06.md with its coverage computed; 133
Talmud addresses indexed on the span, 20 opened PER GAP (the order fork, the altar's height
fork, the table's vessels and faces, the lampstand's counts, the carrying labor's seat), 54
credited from the sanctuary block of round 26.

The five motions, in order:
 (1) code from the BARE INK — the censuses below (the four shown-pattern clauses each a
     hapax; 'and I will meet' a hapax; 'they shall not be removed' a hapax; 'and it shall
     divide' a hapax; 'the tabernacle shall be one' at four seats; the pattern-word's Torah
     seats the blueprint and the image ban; 'standing' at two Torah seats; 'beaten work' at
     eight; the crown's consonants at twenty-eight seats mixing two words; the stamp absent
     from 36-38 and fourteen times in 39-40; the run's thirty-seven unsubjected 'and he
     made' with ONE named maker; the altar named 'of the burnt offering' first at 30:28;
     the base never built, named by its use in Leviticus; the sanctuary shekel at three
     seats of the accounts; 'a beka a head' with Rebekah's nose-ring; the census number
     with Numbers 1:46) — and the ARITHMETIC (curtains, boards, sockets, pillars, the
     court's perimeter and area, the talent, the maneh, the lampstand's cups and knobs);
     every quantity the ink does not state a PARAMETER (the cubit, the board's thickness,
     the lampstand's height, the plating's thickness, the veil's thread count);
 (2) the Mishnah's rows as TEST DATA, each expected value a literal typed from the row (the
     honest-pairing guard runs first);
 (3) run;
 (4) misses filled by NAMED recorded arguments — the Tanchuma and Onkelos rows (the unit's
     substitute spine, verdicted 2026-09-01/02), the sanctuary block's 49 segments (credited),
     and the 20 opened per gap this sitting;
 (5) the graded matrix with per-cell provenance, fractions, EFFECTS — and the SCENE on the
     world engine: the offering brought, the halt proclaimed, the vessels made, the accounts
     rendered; the two HEAVEN entries the spec promises (the Presence dwelling, the meeting
     at the cover) left UNFIRED — the run stops at 38:31; the erection (E5) fires them.

Cross-span receipts, labeled [IMPORT] and CALLED (the edges dispositioned in
dependency_dispositions.yaml): cold_run_offerings.dispatch (olah:herd, shelamim — the lower
bloods below the red line); cold_run_chatat.blood (the upper bloods on the horns);
cold_run_tzav.altar_machine (the perpetual fire on a wooden altar); cold_run_priesthood.lamp_table
(the lamp and the table at their law seat, Lev 24 — one function at two seats);
cold_run_ordinances.altar (the earth-filled hollow altar, the hewn ban, the ramp — Exod 20:24-26
compiled at E1). Num 8:4, Num 1:46, Num 4:26, Deut 4:16-18, Deut 10:1, 1 Kgs 6:2-20, 1 Sam 2:22,
2 Chr 4:1, Gen 8:2, Gen 24:22, Ezek 40:4, Ezek 43:9 stay imports by name. The incense altar
(37:25-28), the anointing oil and incense (37:29), the laver (38:8), and the half-shekel census
(38:24-26) are E4's: OWED, on the gate's worklist.
"""
import sqlite3, sys, os, json, io, contextlib, collections, math
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import effects_layer as FX
from compile_guards import check_honest_pairing
GUARDED = check_honest_pairing(os.path.abspath(__file__))
assert GUARDED == 258, ("the guard counted %d expectations, the tripwire holds 258" % GUARDED)   # W6: +1 (the altar's fire duty scene)

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

SPEC = [(c, v) for c, a, z in [(25, 1, 40), (26, 1, 37), (27, 1, 21)] for v in range(a, z + 1)]
RUN = [(c, v) for c, a, z in [(35, 30, 35), (36, 1, 38), (37, 1, 29), (38, 1, 31)] for v in range(a, z + 1)]
def seats(pred, rng):
    return [k for k in rng if pred(toks('Exod', k[0], k[1]))]
def has(*ws):
    return lambda t: any(t[i:i + len(ws)] == list(ws) for i in range(len(t) - len(ws) + 1))
def anytok(*ws):
    return lambda t: any(w in t for w in ws)
def anyprefix(*ps):
    return lambda t: any(w.startswith(p) for w in t for p in ps)
def count(words, rng):
    return sum(phrase('Exod', c, v, words) for c, v in rng)

# the whole-Tanakh token index (23,213 verses) — for the span's rare tokens and phrases
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
TORAH = ('Gen', 'Exod', 'Lev', 'Num', 'Deut')
def torah(tok):
    return [k for k in tanakh(tok) if k[0] in TORAH]
def fmt(ks): return ['%s %d:%d' % k for k in ks]
def fmt2(ks): return ['%d:%d' % k[1:] for k in ks]
def fmt3(ks): return ['%d:%d' % k for k in ks]
N_VERSES = db.execute("SELECT COUNT(*) FROM verses").fetchone()[0]
assert N_VERSES == 23213, N_VERSES

# ---- (1) ink probes — each MUST fire or the run refuses -------------
PROBES = [
    ('let them take Me an OFFERING',                        'Exod', 25, 2, 'תרומה'),
    ('whose HEART makes him willing',                        'Exod', 25, 2, 'לבו'),
    ('and I will DWELL among them',                          'Exod', 25, 8, 'ושכנתי'),
    ('the PATTERN of the tabernacle',                        'Exod', 25, 9, 'תבנית'),
    ('an ARK of acacia wood',                                'Exod', 25, 10, 'ארון'),
    ('a CROWN of gold around',                               'Exod', 25, 11, 'זר'),
    ('they shall NOT BE REMOVED from it',                    'Exod', 25, 15, 'יסרו'),
    ('the TESTIMONY which I shall give you',                 'Exod', 25, 16, 'העדת'),
    ('a COVER of pure gold',                                 'Exod', 25, 17, 'כפרת'),
    ('two CHERUBIM of beaten work',                          'Exod', 25, 18, 'כרבים'),
    ('and I will MEET with you there',                       'Exod', 25, 22, 'ונועדתי'),
    ('a TABLE of acacia wood',                               'Exod', 25, 23, 'שלחן'),
    ('a frame of a HANDBREADTH around',                      'Exod', 25, 25, 'טפח'),
    ('bread of the FACE before Me continually',              'Exod', 25, 30, 'פנים'),
    ('a LAMPSTAND of pure gold, beaten work',                'Exod', 25, 31, 'מקשה'),
    ('six BRANCHES going out of its sides',                  'Exod', 25, 32, 'קנים'),
    ('three ALMOND cups on the one branch',                  'Exod', 25, 33, 'משקדים'),
    ('its LAMPS seven',                                      'Exod', 25, 37, 'שבעה'),
    ('a TALENT of pure gold',                                'Exod', 25, 39, 'ככר'),
    ('ten CURTAINS of twined linen',                         'Exod', 26, 1, 'יריעת'),
    ('and the tabernacle shall be ONE',                      'Exod', 26, 6, 'אחד'),
    ('the BOARDS for the tabernacle, standing',              'Exod', 26, 15, 'עמדים'),
    ('forty SOCKETS of silver',                              'Exod', 26, 19, 'אדני'),
    ('the middle BAR from end to end',                       'Exod', 26, 28, 'והבריח'),
    ('according to its FASHION shown in the mountain',       'Exod', 26, 30, 'כמשפטו'),
    ('a VEIL of blue and purple',                            'Exod', 26, 31, 'פרכת'),
    ('and the veil shall DIVIDE for you',                    'Exod', 26, 33, 'והבדילה'),
    ('the ALTAR five cubits, SQUARE',                        'Exod', 27, 1, 'רבוע'),
    ('the net to the HALF of the altar',                     'Exod', 27, 5, 'חצי'),
    ('HOLLOW of boards you shall make it',                   'Exod', 27, 8, 'נבוב'),
    ('the COURT of the tabernacle, hangings',                'Exod', 27, 9, 'קלעים'),
    ('a hundred by fifty, five high',                        'Exod', 27, 18, 'וקמה'),
    ('pure olive oil, CRUSHED, for the light',               'Exod', 27, 20, 'כתית'),
    ('SEE, the LORD has called by name Bezalel',             'Exod', 35, 30, 'בצלאל'),
    ('WISDOM, understanding, and knowledge',                 'Exod', 35, 31, 'בחכמה'),
    ('MORNING BY MORNING they brought',                      'Exod', 36, 3, 'בבקר'),
    ('and the people were RESTRAINED from bringing',         'Exod', 36, 6, 'ויכלא'),
    ('enough... and there was LEFT OVER',                    'Exod', 36, 7, 'והותר'),
    ('and BEZALEL made the ark',                             'Exod', 37, 1, 'בצלאל'),
    ('the altar of the BURNT OFFERING',                      'Exod', 38, 1, 'העלה'),
    ('the MIRRORS of the assembling women',                  'Exod', 38, 8, 'במראת'),
    ('THESE ARE THE ACCOUNTS of the tabernacle',             'Exod', 38, 21, 'פקודי'),
    ('a BEKA a head, half a shekel',                         'Exod', 38, 26, 'בקע'),
    ('a TALENT A SOCKET',                                    'Exod', 38, 27, 'לאדן'),
]
fired = 0
for label, book, ch, vs, tok in PROBES:
    if tok in toks(book, ch, vs): fired += 1
    else: print('PROBE FAILED: %s (%s %d:%d lacks %s)' % (label, book, ch, vs, tok))
if fired != len(PROBES):
    sys.exit('zero-report law: the ink scan is not trusted until every probe fires')
print('probes: %d/%d fired (the ink scan is trusted; the whole-Tanakh census holds %d verses)' % (len(PROBES), len(PROBES), N_VERSES))

# ---- the censuses (TRIPWIRES — each a measured literal) ------------
c_shown9 = tanakh_phrase(['אני', 'מראה', 'אותך']);                 assert c_shown9 == [('Exod', 25, 9), ('Ezek', 40, 4)], c_shown9
c_shown40 = tanakh_phrase(['מראה', 'בהר']);                       assert c_shown40 == [('Exod', 25, 40)], c_shown40
c_shown30 = tanakh_phrase(['הראית', 'בהר']);                      assert c_shown30 == [('Exod', 26, 30)], c_shown30
c_shown8 = tanakh_phrase(['הראה', 'אתך', 'בהר']);                 assert c_shown8 == [('Exod', 27, 8)], c_shown8
c_tavnit = torah('תבנית');                                        assert c_tavnit == [('Deut', 4, 16), ('Deut', 4, 17), ('Deut', 4, 18), ('Exod', 25, 9)], c_tavnit
c_terumah = [w for v in (2, 3) for w in toks('Exod', 25, v) if 'תרומ' in w]; assert c_terumah == ['תרומה', 'תרומתי', 'התרומה'], c_terumah
c_five = [w in toks('Exod', 25, 2) for w in ('דבר', 'לבו', 'איש', 'תקחו', 'ישראל')]; assert all(c_five), c_five
c_chain = [toks('Exod', 25, v)[0][:1] for v in range(3, 8)];      assert c_chain == ['ו', 'ו', 'ו', 'ש', 'א'], c_chain
c_veasu = seats(anytok('ועשו'), SPEC);                             assert c_veasu == [(25, 8), (25, 10)], c_veasu
c_veasita = len(seats(anytok('ועשית'), SPEC));                    assert c_veasita == 30, c_veasita
c_taasu = seats(anytok('תעשו'), SPEC);                             assert c_taasu == [(25, 9), (25, 19)], c_taasu
c_dwell = tanakh_phrase(['ושכנתי', 'בתוכם']);                     assert c_dwell == [('Exod', 25, 8), ('Ezek', 43, 9)], c_dwell
c_meet = tanakh('ונועדתי');                                       assert c_meet == [('Exod', 25, 22)], c_meet
c_staves = tanakh_phrase(['לא', 'יסרו', 'ממנו']);                 assert c_staves == [('Exod', 25, 15)], c_staves
c_zer_span = seats(anytok('זר'), SPEC + RUN);                      assert c_zer_span == [(25, 11), (25, 24), (25, 25), (37, 2), (37, 11), (37, 12), (37, 26)], c_zer_span
c_zer_all = len(tanakh('זר'));                                     assert c_zer_all == 28, c_zer_all
c_mikshah = torah('מקשה');                                        assert c_mikshah == [('Exod', 25, 18), ('Exod', 25, 31), ('Exod', 25, 36), ('Exod', 37, 7), ('Exod', 37, 17), ('Exod', 37, 22), ('Num', 8, 4), ('Num', 10, 2)], c_mikshah
c_almond = tanakh('משקדים');                                      assert c_almond == [('Exod', 25, 33), ('Exod', 25, 34), ('Exod', 37, 19), ('Exod', 37, 20)], c_almond
c_kaporet25 = [v for v in range(1, 41) if 'הכפרת' in toks('Exod', 25, v)]; assert c_kaporet25 == [18, 19, 20, 21, 22], c_kaporet25
c_tefach = tanakh('טפח');                                         assert c_tefach == [('1Kgs', 7, 26), ('2Chr', 4, 5), ('Exod', 25, 25), ('Exod', 37, 12), ('Ezek', 40, 43)], c_tefach
c_no_cubit_menorah = [w for v in range(31, 41) for w in toks('Exod', 25, v) if w in ('אמה', 'באמה', 'אמות', 'אמתים', 'האמה', 'ואמה')]; assert c_no_cubit_menorah == [], c_no_cubit_menorah
c_cubit_spec = sum(1 for k in SPEC for w in toks('Exod', *k) if w in ('אמה', 'באמה', 'אמות', 'אמתים', 'האמה', 'ואמה')); assert c_cubit_spec == 25, c_cubit_spec
c_cubit_run = sum(1 for k in RUN for w in toks('Exod', *k) if w in ('אמה', 'באמה', 'אמות', 'אמתים', 'האמה', 'ואמה'));  assert c_cubit_run == 27, c_cubit_run
c_one = seats(anytok('אחד'), [(26, 6), (26, 11), (36, 13), (36, 18)]); assert c_one == [(26, 6), (26, 11), (36, 13), (36, 18)], c_one
c_sister_spec = count(['אשה', 'אל', 'אחתה'], SPEC);               assert c_sister_spec == 5, c_sister_spec
c_sister_run = count(['אשה', 'אל', 'אחתה'], RUN);                 assert c_sister_run == 0, c_sister_run
c_one_one_spec = count(['אחת', 'אל', 'אחת'], SPEC);               assert c_one_one_spec == 0, c_one_one_spec
c_one_one_run = count(['אחת', 'אל', 'אחת'], RUN);                 assert c_one_one_run == 5, c_one_one_run
c_omdim = torah('עמדים');                                         assert c_omdim == [('Exod', 26, 15), ('Exod', 36, 20)], c_omdim
c_kemishpato = tanakh('כמשפטו');                                  assert c_kemishpato == [('1Kgs', 5, 8), ('Exod', 26, 30)], c_kemishpato
c_divide = tanakh('והבדילה');                                     assert c_divide == [('Exod', 26, 33)], c_divide
c_between = tanakh_phrase(['בין', 'הקדש', 'ובין', 'קדש', 'הקדשים']); assert c_between == [('Exod', 26, 33)], c_between
c_choshev = len(tanakh_phrase(['מעשה', 'חשב']));                  assert c_choshev == 8, c_choshev
c_rokem = len(tanakh_phrase(['מעשה', 'רקם']));                    assert c_rokem == 6, c_rokem
c_ravua = torah('רבוע');                                          assert c_ravua == [('Exod', 27, 1), ('Exod', 28, 16), ('Exod', 30, 2), ('Exod', 37, 25), ('Exod', 38, 1), ('Exod', 39, 9)], c_ravua
c_definite = 'המזבח' in toks('Exod', 27, 1);                      assert c_definite
c_mimenu = ('ממנו' in toks('Exod', 27, 2), 'ממנו' in toks('Exod', 38, 2)); assert c_mimenu == (True, True), c_mimenu
c_navuv = tanakh('נבוב');                                         assert c_navuv == [('Exod', 27, 8), ('Exod', 38, 7), ('Jer', 52, 21), ('Job', 11, 12)], c_navuv
c_olah_name = [k for k in tanakh_phrase(['מזבח', 'העלה']) if k[0] == 'Exod']; assert c_olah_name == [('Exod', 30, 28), ('Exod', 31, 9), ('Exod', 35, 16), ('Exod', 38, 1), ('Exod', 40, 6), ('Exod', 40, 10), ('Exod', 40, 29)], c_olah_name
c_yesod = tanakh_phrase(['יסוד', 'המזבח']);                       assert c_yesod == [('Exod', 29, 12), ('Lev', 4, 30), ('Lev', 4, 34), ('Lev', 5, 9), ('Lev', 8, 15), ('Lev', 9, 9)], c_yesod
c_yesod_span = seats(anyprefix('יסוד'), SPEC + RUN);               assert c_yesod_span == [], c_yesod_span
c_stems = [all(any(s in w for w in toks('Exod', c, v)) for s in ('סיר', 'יע', 'מזרק', 'מזלג', 'מחת')) for c, v in ((27, 3), (38, 3))]; assert c_stems == [True, True], c_stems
c_kelaim = len(tanakh('קלעים')) + len(tanakh('קלעי'));             assert c_kelaim == 16, c_kelaim
c_kelaim_torah = len(torah('קלעים')) + len(torah('קלעי'));         assert c_kelaim_torah == 14, c_kelaim_torah
c_heads_run = [v for v in range(1, 32) if phrase('Exod', 38, v, ['וצפוי', 'ראשיהם'])]; assert c_heads_run == [17, 19], c_heads_run
c_heads_spec = [v for v in range(1, 22) if 'ראשיהם' in toks('Exod', 27, v)]; assert c_heads_spec == [], c_heads_spec
c_heads_36 = ('ראשיהם' in toks('Exod', 36, 38), 'ראשיהם' in toks('Exod', 26, 37)); assert c_heads_36 == (True, False), c_heads_36
c_tail = toks('Lev', 24, 2)[-13:] == toks('Exod', 27, 20)[-13:];  assert c_tail
c_sons = ('ובניו' in toks('Exod', 27, 21), 'ובניו' in toks('Lev', 24, 3)); assert c_sons == (True, False), c_sons
c_named = tanakh('בצלאל') + tanakh('ובצלאל');                      assert [k for k in c_named if k[0] == 'Exod'] == [('Exod', 31, 2), ('Exod', 35, 30), ('Exod', 36, 1), ('Exod', 36, 2), ('Exod', 37, 1), ('Exod', 38, 22)], c_named
c_vayaas = {ch: len([v for v in range(1, 40) if ('Exod', ch, v) in _VERSES and 'ויעש' in _VERSES[('Exod', ch, v)]]) for ch in (36, 37, 38)}; assert c_vayaas == {36: 13, 37: 16, 38: 8}, c_vayaas
c_maker = [k for k in RUN if toks('Exod', *k)[:2] == ['ויעש', 'בצלאל']]; assert c_maker == [(37, 1)], c_maker
c_see = (tanakh_phrase(['ראה', 'קראתי', 'בשם']), tanakh_phrase(['ראו', 'קרא', 'יהוה', 'בשם'])); assert c_see == ([('Exod', 31, 2)], [('Exod', 35, 30)]), c_see
c_wise = len(tanakh_phrase(['חכם', 'לב']));                       assert c_wise == 6, c_wise
c_morning = [k for k in tanakh_phrase(['בבקר', 'בבקר']) if k[0] in TORAH]; assert c_morning == [('Exod', 16, 21), ('Exod', 30, 7), ('Exod', 36, 3), ('Lev', 6, 5)], c_morning
c_restrained = tanakh('ויכלא');                                   assert c_restrained == [('Exod', 36, 6), ('Gen', 8, 2)], c_restrained
c_enough = tanakh('דים');                                         assert c_enough == [('Exod', 36, 7), ('Jer', 49, 9), ('Obad', 1, 5)], c_enough
c_over = tanakh('והותר');                                         assert c_over == [('2Chr', 31, 10), ('2Kgs', 4, 43), ('Exod', 36, 7)], c_over
c_stamp = [k for k in tanakh_phrase(['כאשר', 'צוה', 'יהוה', 'את', 'משה']) if k[0] == 'Exod' and 35 <= k[1] <= 40]; assert len(c_stamp) == 14 and all(k[1] in (39, 40) for k in c_stamp), c_stamp
c_stamp_run = seats(has('כאשר', 'צוה'), RUN);                      assert c_stamp_run == [], c_stamp_run
c_all_cmd = tanakh_phrase(['את', 'כל', 'אשר', 'צוה', 'יהוה', 'את', 'משה']); assert c_all_cmd == [('Exod', 38, 22)], c_all_cmd
c_pekudei = tanakh_phrase(['אלה', 'פקודי']);                      assert c_pekudei == [('Exod', 38, 21), ('Num', 2, 32), ('Num', 4, 37), ('Num', 4, 41), ('Num', 4, 45), ('Num', 26, 51), ('Num', 26, 63)], c_pekudei
c_itamar = tanakh_phrase(['ביד', 'איתמר']);                       assert c_itamar == [('Exod', 38, 21), ('Num', 4, 28), ('Num', 4, 33), ('Num', 7, 8)], c_itamar
c_beka = torah('בקע');                                            assert c_beka == [('Exod', 38, 26), ('Gen', 24, 22)], c_beka
c_census = tanakh_phrase(['מאות', 'אלף', 'ושלשת', 'אלפים', 'וחמש', 'מאות', 'וחמשים']); assert c_census == [('Exod', 38, 26), ('Num', 1, 46), ('Num', 2, 32)], c_census
c_socket = tanakh_phrase(['ככר', 'לאדן']);                        assert c_socket == [('Exod', 38, 27)], c_socket
c_shekel_span = seats(has('בשקל', 'הקדש'), RUN);                   assert c_shekel_span == [(38, 24), (38, 25), (38, 26)], c_shekel_span
c_shekel_all = len(tanakh_phrase(['בשקל', 'הקדש']));              assert c_shekel_all == 25, c_shekel_all
c_bronze_items = sum(1 for v in (30, 31) for w in toks('Exod', 38, v) if w in ('ואת', 'את')); assert c_bronze_items == 8, c_bronze_items
c_mirrors = (tanakh('במראת'), tanakh('הצבאת'), tanakh('הצבאות'));  assert c_mirrors == ([('Exod', 38, 8), ('Gen', 46, 2)], [('Exod', 38, 8)], [('1Chr', 27, 3), ('1Sam', 2, 22), ('Amos', 3, 13), ('Amos', 6, 14), ('Amos', 9, 5), ('Hos', 12, 6)]), c_mirrors
c_e4 = [(k, w) for k in RUN for w in toks('Exod', *k) if 'קטרת' in w or 'כיור' in w or 'משחה' in w]; assert c_e4 == [((37, 25), 'הקטרת'), ((37, 29), 'המשחה'), ((37, 29), 'קטרת'), ((38, 8), 'הכיור')], c_e4
c_tachat = seats(anytok('תחת'), SPEC + RUN);                       assert len(c_tachat) == 11 and (25, 35) in c_tachat and (27, 5) in c_tachat, c_tachat
c_tokens = (sum(len(toks('Exod', *k)) for k in SPEC), sum(len(toks('Exod', *k)) for k in RUN)); assert c_tokens == (1182, 1362), c_tokens
c_metals = {m: (sum(1 for k in SPEC for w in toks('Exod', *k) if m in w), sum(1 for k in RUN for w in toks('Exod', *k) if m in w)) for m in ('זהב', 'כסף', 'נחשת')}
assert c_metals == {'זהב': (25, 30), 'כסף': (9, 15), 'נחשת': (13, 18)}, c_metals
c_dims_eq = (toks('Exod', 37, 1)[-10:] == toks('Exod', 25, 10)[-10:], toks('Exod', 37, 10)[-8:] == toks('Exod', 25, 23)[-8:], toks('Exod', 37, 6)[-7:] == toks('Exod', 25, 17)[-7:]); assert c_dims_eq == (True, True, True), c_dims_eq
print('censuses: the shown-pattern clauses at %s, %s, %s, %s (each once) · the pattern-word\'s Torah seats %s · the offering-tokens %s · the plural making-verb at %s · '
      '"I will meet" %s · "not removed" %s · the crown-consonants at %d seats (%d in the span) · beaten work %d Torah seats · "one" at %s · "a woman to her sister" spec %d / run %d against "one to one" spec %d / run %d · '
      '"standing" %s · "square" %d Torah seats · the altar named "of the burnt offering" first at %s · the base never in the span (%s) · the stamp %d times in 39-40 and %d in 36-38 · '
      '"and he made" per chapter %s with ONE named maker at %s · the census number at %s · "a talent a socket" %s · the sanctuary shekel at %s · the E4 tokens %s · %d "under" homographs · tokens %s'
      % (c_shown9[0], c_shown40, c_shown30, c_shown8, c_tavnit, c_terumah, c_veasu, c_meet, c_staves, c_zer_all, len(c_zer_span), len(c_mikshah), c_one, c_sister_spec, c_sister_run, c_one_one_spec, c_one_one_run,
         c_omdim, len(c_ravua), c_olah_name[0], c_yesod_span, len(c_stamp), len(c_stamp_run), c_vayaas, c_maker, c_census, c_socket, c_shekel_span, [w for _, w in c_e4], len(c_tachat), c_tokens))

# ---- THE ALIGNMENT ENGINE — every run verse to its spec verse by token, block by block ----
def norm(w):
    if w in ('את', 'ואת', 'אתו', 'אתם', 'אתה'): return None
    if w[:1] == 'ו' and len(w) > 3: w = w[1:]
    if w[:1] == 'ה' and len(w) > 3: w = w[1:]
    return w
def bag(k):
    return set(x for x in map(norm, toks('Exod', *k)) if x)
BLOCKS = [('ark', (25, 10, 22), (37, 1, 9)), ('table', (25, 23, 30), (37, 10, 16)), ('menorah', (25, 31, 40), (37, 17, 24)),
          ('curtains', (26, 1, 14), (36, 8, 19)), ('boards', (26, 15, 30), (36, 20, 34)), ('veil_screen', (26, 31, 37), (36, 35, 38)),
          ('altar', (27, 1, 8), (38, 1, 7)), ('court', (27, 9, 19), (38, 9, 20)), ('lamp', (27, 20, 21), None)]
NUM = {'אחד', 'אחת', 'שני', 'שתי', 'שנים', 'שלש', 'שלשה', 'שלשת', 'ארבע', 'ארבעה', 'חמש', 'חמשה', 'שש', 'ששה', 'שבע', 'שבעה', 'שמנה', 'תשע', 'עשר', 'עשרה',
       'עשרים', 'שלשים', 'ארבעים', 'חמשים', 'מאה', 'מאת', 'אלף', 'אמתים', 'וחצי', 'חצי', 'עשתי', 'ששת', 'ארבעת'}
ALIGN = {}
for name, (sc, sa, sz), run in BLOCKS:
    spec = [(sc, v) for v in range(sa, sz + 1)]
    if run is None:
        ALIGN[name] = {'spec': len(spec), 'run': 0, 'matched': 0, 'dropped': ['%d:%d' % s for s in spec], 'numerals_equal': None}; continue
    rc, ra, rz = run; rv = [(rc, v) for v in range(ra, rz + 1)]
    m = {}
    for k in rv:
        best = max(spec, key=lambda s: len(bag(k) & bag(s)) / max(1, len(bag(k) | bag(s))))
        j = len(bag(k) & bag(best)) / max(1, len(bag(k) | bag(best)))
        if j >= 0.3: m.setdefault(best, []).append(k)
    ns = collections.Counter(w.lstrip('ו') for s in spec for w in toks('Exod', *s) if w.lstrip('ו') in NUM)
    nr = collections.Counter(w.lstrip('ו') for k in rv for w in toks('Exod', *k) if w.lstrip('ו') in NUM)
    ALIGN[name] = {'spec': len(spec), 'run': len(rv), 'matched': len(m), 'run_matched': sum(len(x) for x in m.values()),
                   'dropped': ['%d:%d' % s for s in spec if s not in m], 'numerals_equal': ns == nr}
A_TOTAL = (sum(a['spec'] for a in ALIGN.values()), sum(a['run'] for a in ALIGN.values()), sum(a['matched'] for a in ALIGN.values()),
           sum(a.get('run_matched', 0) for a in ALIGN.values()), sum(len(a['dropped']) for a in ALIGN.values()))
assert A_TOTAL == (89, 74, 65, 67, 24), A_TOTAL
A_DROPPED = [d for a in ALIGN.values() for d in a['dropped']]
assert A_DROPPED == ['25:15', '25:16', '25:21', '25:22', '25:30', '25:37', '25:40', '26:12', '26:13', '26:30', '26:33', '26:34', '26:35', '26:37',
                     '27:3', '27:4', '27:5', '27:8', '27:15', '27:17', '27:18', '27:19', '27:20', '27:21'], A_DROPPED
A_NUM_EQ = sorted(n for n, a in ALIGN.items() if a['numerals_equal']); assert A_NUM_EQ == ['table', 'veil_screen'], A_NUM_EQ
HEADS = [('ark', ('ארון', 'הארן')), ('table', ('שלחן', 'השלחן')), ('menorah', ('מנרת', 'המנרה')), ('curtains', ('יריעת',)), ('boards', ('הקרשים',)),
         ('veil', ('פרכת', 'הפרכת')), ('screen', ('מסך',)), ('incense_altar', ('הקטרת',)), ('anointing_oil', ('המשחה',)), ('laver', ('הכיור',)), ('court', ('חצר', 'החצר'))]
def first(rng, tks):
    for k in rng:
        if any(w in tks for w in toks('Exod', *k)): return k
def altar_first(rng):
    for k in rng:
        if 'המזבח' in toks('Exod', *k) or has('מזבח', 'העלה')(toks('Exod', *k)): return k
SPEC_ORDER = [n for k, n in sorted([(first([s for s in SPEC if s >= (25, 10)], t), n) for n, t in HEADS if first([s for s in SPEC if s >= (25, 10)], t)] + [(altar_first(SPEC), 'altar')])]
RUN_ORDER = [n for k, n in sorted([(first([r for r in RUN if r >= (36, 8)], t), n) for n, t in HEADS if first([r for r in RUN if r >= (36, 8)], t)] + [(altar_first([r for r in RUN if r >= (36, 8)]), 'altar')])]
assert SPEC_ORDER == ['ark', 'table', 'menorah', 'curtains', 'boards', 'veil', 'screen', 'altar', 'court'], SPEC_ORDER
assert RUN_ORDER == ['curtains', 'boards', 'veil', 'screen', 'ark', 'table', 'menorah', 'incense_altar', 'anointing_oil', 'altar', 'laver', 'court'], RUN_ORDER
print('alignment: spec %d verses, run %d; spec matched %d, run matched %d, dropped %d — %s; numerals equal in %s; SPEC order %s; RUN order %s'
      % (A_TOTAL + (A_DROPPED, A_NUM_EQ, SPEC_ORDER, RUN_ORDER)))

# ---- the callees (cold) --------------------------------------------
_buf = io.StringIO()
with contextlib.redirect_stdout(_buf):
    import cold_run_offerings as OFF
    import cold_run_chatat as CH
    import cold_run_tzav as TZ
    import cold_run_priesthood as PR
    import cold_run_ordinances as ORD
    import world_engine as WE
OLAH_H = OFF.dispatch('olah:herd'); SHEL = OFF.dispatch('shelamim')
CH_HORNS = CH.blood('commoner')['v']
TZ_EXT = TZ.altar_machine({'ask': 'extinguish'}, TZ.PARAMS)[0]; TZ_RET = TZ.altar_machine({'ask': 'retention'}, TZ.PARAMS)[0]
PR_OIL = PR.lamp_table('oil')['v']; PR_GRADES = PR.lamp_table('nine_grades')['v']; PR_WEST = PR.lamp_table('western_lamp')['v']
PR_EXCH = PR.lamp_table('exchange_protocol')['v']; PR_LOAVES = PR.lamp_table('loaves')['v']; PR_DIMS = PR.lamp_table('dimensions')['v']
PR_TWO = PR.lamp_table('two_tables')['v']; PR_EVE = PR.lamp_table('evening_to_morning')['v']; PR_ONE = PR.lamp_table('one_priest')['v']
PR_REST = PR.lamp_table('restatement')['v']; PR_POS = PR.lamp_table('position')['v']
ORD_EARTH = ORD.altar('earth_altar')['v']; ORD_HEWN = ORD.altar('hewn')['v']; ORD_STEPS = ORD.altar('steps')['v']
ORD_RAMP = ORD.altar('ramp')['v']; ORD_STONES = ORD.altar('stones_source')['v']; ORD_RECIPE = ORD.altar('recipe')['v']
print('routing receipts: cold_run_offerings CALLED — olah:herd applications %r place %r, shelamim applications %r; cold_run_chatat CALLED — commoner blood %r; '
      'cold_run_tzav CALLED — extinguish %r, retention %r; cold_run_priesthood CALLED — oil %r, grades %r, western %r, exchange %r, loaves %r, dimensions %r, two tables %r, '
      'evening %r, one priest %r, restatement %r, position %r; cold_run_ordinances CALLED — earth %r, hewn %r, steps %r, ramp %r, stones %r, recipe %r [IMPORT, live calls]'
      % (OLAH_H['applications']['v'], OLAH_H['place']['v'], SHEL['applications']['v'], CH_HORNS, TZ_EXT, TZ_RET, PR_OIL, PR_GRADES, PR_WEST, PR_EXCH, PR_LOAVES, PR_DIMS, PR_TWO,
         PR_EVE, PR_ONE, PR_REST, PR_POS, ORD_EARTH, ORD_HEWN, ORD_STEPS, ORD_RAMP, ORD_STONES, ORD_RECIPE))

I, M, A, D, P, H = 'INK', 'MOVE', 'ANSWER-SHEET', 'DATA', 'IMPORT', 'HYPOTHESIS'   # H: THE LINK REVIEW LAW (LR3, 2026-09-07) — an untaught transfer, kept and labeled, never counted as compiled
def cell(v, p, why, fx):
    FX.validate(fx)
    return {'v': v, 'p': p, 'why': why, 'fx': fx}
TT = "Midrash Tanchuma, "
SB = "the sanctuary block (round 26, credited): "

# =====================================================================
# THE SPEC — compiled from the ink of Exodus 25-27; THE RUN — Exodus 35:30-38:31 matched to it.
# Mishnah/Talmud appear ONLY on [MOVE] lines (motion 4) and as DATA (motion 2).
# =====================================================================

# ---- F1: THE OFFERING AND THE WORKFORCE (25:1-9; 35:30-36:7) ----------
def offering(q):
    if q == 'three_tokens':
        return cell(len(c_terumah), I, "25:2-3 — the offering-token three times in two verses: %s ('an offering', 'My offering', 'the offering') — the ink's own count" % (c_terumah,), ['set_apart_before_me'])
    if q == 'set_apart':
        return cell('set_apart_before_me', M, "25:2 'let them take Me an offering' — Onkelos: 'let them SET APART before Me a separation' (the priestly dues' vocabulary; the audience-preposition, not 'to' Me): the gift a formal act of setting-apart", ['set_apart_before_me'])
    if q == 'trigger':
        return cell('willing_heart', I, "25:2 'from every man whose HEART makes him willing you shall take' — the sole trigger; no amount in the ink (the amount is a PARAMETER: the half shekel is 30:13's, E4's)", ['set_apart_before_me'])
    if q == 'five_tokens_present':
        return cell(5, I, "25:2 — the five tokens the tradition reads for the five who may not separate all present in the verse: 'speak' (דבר), 'his heart' (לבו), 'man' (איש), 'you shall take' (תקחו), 'Israel' (ישראל) — %s" % (c_five,), ['set_apart_before_me'])
    if q == 'five_barred':
        return cell(['deaf_mute', 'incompetent', 'minor', 'not_his', 'gentile'], M, TT + "Terumah 3 (end) + Buber 2 — Reish Lakish word by word from 25:2: 'SPEAK' excludes the deaf-mute (he neither hears nor speaks), 'whose HEART makes him willing' the incompetent, 'every MAN' the minor, 'from... you shall TAKE' (from your own) the one who separates another's, 'the children of ISRAEL' the gentile = Mishnah Terumot 1:1's five", ['set_apart_before_me'])
    if q == 'material_segments':
        return cell([11, 2, 2], I, "25:3-7 — the conjunction chain: every verse-head from 25:3 to 25:5 begins with the joining vav (%s), 25:6 'oil' and 25:7 'stones' do NOT — three segments: the eleven materials (gold, silver, bronze; blue, purple, crimson, linen, goat hair; ram skins, tachash skins, acacia), the oil and the spices, the two stones" % (c_chain,), [FX.NONE])
    if q == 'thirteen':
        return cell(13, M, TT + "Terumah 5 + Buber 4 (R. Yehudah bar Simon) — THIRTEEN items answering the thirteen things done for Israel in Egypt (Ezek 16:10-13): the first segment's eleven plus the oil and the spices; the two stones are the priests' (for the ephod and breastplate — 25:7's own clause); " + SB + "Avodah Zarah 24a:2 — 'onyx stones' without the vav BREAKS the list", [FX.NONE])
    if q == 'plural_making':
        return cell(c_veasu, I, "the plural making-verb 'and THEY shall make' at exactly two seats of the spec, %s — 25:8 the sanctuary and 25:10 the ARK; every other vessel 'and YOU shall make' (%d seats); 'you shall make (pl.)' at %s" % (c_veasu, c_veasita, c_taasu), [FX.NONE])
    if q == 'ark_they':
        return cell('all_israel', M, TT + "Vayakhel 8:1 — for every vessel 'THOU shalt make', for the ark 'THEY shall make': all Israel commanded, so that none says 'I gave more to the ark, the Torah is more mine'; " + SB + "Yoma 3b:3 harmonizes 25:10's 'they' with Deut 10:1's 'make YOURSELF an ark of wood' — a WILL-INDEXED dispatch (the public when Israel does the will, the leader alone when not)", [FX.NONE])
    if q == 'dwell_phrase':
        return cell(2, I, "25:8 'and I will dwell among them' — the phrase at %s alone in the Tanakh (Ezekiel's temple vision the second seat); the verb 'and I will dwell' at 29:45 with 'in the midst of the children of Israel'" % (c_dwell,), ['presence_dwells'])
    if q == 'dwells_in':
        return cell('the_people_not_the_building', M, "Onkelos 25:8 'and I will make My Presence dwell AMONG THEM' — the indwelling lands in the people (בתוכם, 'among them'), not in the sanctuary the verse commissions; the sanctuary is made 'before Me'; the promise's HEAVEN entry fires at 40:34 (E5), not in this run", ['presence_dwells'])
    if q == 'shown_clauses':
        return cell(4, I, "the shown-pattern clause at four seats of the spec, each phrase once in the Tanakh: 25:9 'all that I show you' (%s — Ezek 40:4 the second), 25:40 'shown in the mountain' %s, 26:30 'which you were shown in the mountain' %s, 27:8 'as He showed you in the mountain' %s — the pointers dispositioned INTERNAL" % (c_shown9, c_shown40, c_shown30, c_shown8), [FX.NONE])
    if q == 'pattern_word_torah':
        return cell(['Deut 4:16', 'Deut 4:17', 'Deut 4:18', 'Exod 25:9'], I, "the pattern-word (תבנית, 'pattern/likeness') in the Torah at %s — the sanctuary's BLUEPRINT (25:9 twice; 25:40 'according to their pattern') and the IMAGE BAN's noun (Deut 4:16-18: 'the likeness of any figure'): one word for the licensed pattern and the forbidden one" % (fmt(c_tavnit),), [FX.NONE])
    if q == 'so_shall_you_make':
        return cell('extension_constitution', A, "25:9 'and SO shall you make' — Mishnah Shevuot 2:2 + Sanhedrin 1:5: the city and the courts are extended only by the original constitution's elements; " + SB + "Sanhedrin 16b:4 reads the clause for every generation's extension; Onkelos: the pattern 'a likeness' shown twice", [FX.NONE])
    if q == 'extension_requirements':
        return cell(['king', 'prophet', 'urim_tummim', 'sanhedrin_71', 'two_thanksgivings', 'song'], D, "Mishnah Shevuot 2:2 — the six requirements (data): a king, a prophet, the Urim and Tummim, a Sanhedrin of seventy-one, two thanksgiving offerings, and song; lacking any, one who enters the addition is not liable", [FX.NONE])
    if q == 'craftsmen_pay':
        return cell('from_the_house_fund', M, SB + "Temurah 31b:7 — R. Abahu: 'and they shall make ME' (25:8) = 'from what is MINE': the craftsmen paid from MAINTENANCE consecrations, never from ALTAR consecrations — the sanctuary's two purses divided at the sanctuary verse", ['set_apart_before_me'])
    if q == 'wages_mechanism':
        return cell('R_Akiva_direct_ben_Azzai_desacralize', A, "Mishnah Shekalim 4:6 — consecrated items fit for public offerings: R. Akiva gives them to the craftsmen as wages; ben Azzai — 'that is not the method': the wages separated, the items desacralized onto the craftsmen's money, given, bought back from the new offering", ['set_apart_before_me'])
    if q == 'surplus':
        return cell('gold_leaf_holy_of_holies', A, "Mishnah Shekalim 4:4 — 'the surplus of the offering, what was done with it? gold leaf, plating for the house of the Holy of Holies' — " + TT + "Terumah 1 opens the whole reading with this row's question at 25:8; the run's 36:7 'and there was left over' is the surplus written", ['surplus_to_the_house'])
    if q == 'surplus_arms':
        return cell({'R_Yishmael': 'service_vessels', 'R_Akiva': 'altar_summer', 'R_Chananya': 'service_vessels'}, D, "Mishnah Shekalim 4:4 — the three named arms for the OFFERING's surplus: R. Yishmael service vessels, R. Akiva the altar's summer offerings, R. Chananya the deputy service vessels (each pairing it against the fruits' or the libations' surplus)", ['surplus_to_the_house'])
    if q == 'timestamp':
        return cell('day_of_atonement_after_the_calf', M, TT + "Terumah 8 — 'there is no earlier and later in the Torah': the section spoken on the Day of Atonement, AFTER the calf though written before it — 'let the gold of the tabernacle atone for the gold of the calf'; hence 'the tabernacle of TESTIMONY' (38:21)", [FX.NONE])
    # ---- the RUN: 35:30-36:7 ----
    if q == 'named_by_name':
        return cell(2, I, "'see, I have called by name' at %s (to Moses) and 'see, the LORD has called by name' at %s (to the people) — the appointment announced twice, each phrase once" % (c_see[0], c_see[1]), [FX.NONE])
    if q == 'two_audiences':
        return cell('angels_and_israel', M, TT + "Pekudei 3:1 — praised ABOVE (31:2, to the angels) and BELOW (35:30, to Israel): the two 'see' tokens as two audiences", [FX.NONE])
    if q == 'consent':
        return cell('god_moses_israel', M, "Berakhot 55a:11 (opened per gap) — R. Yitzchak: no leader over the public without consulting the public — 'is Bezalel acceptable to you?' asked of Moses, then of Israel: three-party consent at 35:30", [FX.NONE])
    if q == 'nepotism':
        return cell('answered_by_the_verse', M, TT + "Vayakhel 3:2 — Israel murmured (Moses king, Aaron high priest, his sons deputies, Eleazar the Levites' chief, and now the works to his kinsman); Moses SHOWS THEM THE VERSE 'see, the LORD has called by name' — the appointment published against the conflict-of-interest charge", [FX.NONE])
    if q == 'three_attributes':
        return cell(3, I, "35:31 'in WISDOM, in UNDERSTANDING, and in KNOWLEDGE' — three tokens; Prov 3:19-20 [IMPORT by name]: 'the LORD by wisdom founded the earth, established the heavens by understanding, by His knowledge the depths were broken'", [FX.NONE])
    if q == 'toolchain':
        return cell('creation_tabernacle_temple_future', M, TT + "Vayakhel 5:1-2 — the three attributes are the world's own toolchain (world, tabernacle, Temple by Hiram, the house to come); Berakhot 55a:13 (opened) — Rav: Bezalel knew how to combine the letters by which heaven and earth were created", [FX.NONE])
    if q == 'wise_hearted':
        return cell(6, I, "'wise of heart' at %d seats in the Tanakh (31:6, 35:10, 36:1, 36:2, 36:8, Prov 10:8); 'wisdom of heart' at 35:25 and 35:35 — the workforce's predicate" % c_wise, [FX.NONE])
    if q == 'teaching':
        return cell('to_teach_in_his_heart', I, "35:34 'and TO TEACH He put in his heart' — Bezalel and Oholiab; Onkelos converts even the design-words to teaching-words (35:35 'teachers of craftsmanship'); " + TT + "Vayakhel 2:1 — wisdom given only to those who already have it", [FX.NONE])
    if q == 'two_mornings':
        return cell(2, I, ("36:3 'morning by morning' (בבקר בבקר) — the doubled token counted as two; " + TT + "Pekudei 5:4 — R. Yochanan: TWO mornings brought everything; the Torah's seats of the doubling %s") % (fmt(c_morning),), ['set_apart_before_me'])
    if q == 'halt':
        return cell('bringing_halted', I, "36:6 'let neither man nor woman do any more work for the offering of the sanctuary — and the people were RESTRAINED from bringing': the verb at %s alone (the flood's rain restrained, Gen 8:2 [IMPORT by name]); Onkelos 'the people stopped bringing'" % (c_restrained,), ['bringing_halted'])
    if q == 'carrying_labor':
        return cell('from_private_to_public_domain', M, "Shabbat 96b:1 (opened per gap) — R. Yochanan: 'and Moses commanded and they proclaimed through the camp' — Moses sat in the Levites' camp, a PUBLIC DOMAIN, and told Israel 'do not carry out from your private domain to the public': the Sabbath's carrying labor sourced to 36:6", ['bringing_halted'])
    if q == 'carryings':
        return cell(4, A, "Mishnah Shevuot 1:1 — 'the carryings-out of the Sabbath, two that are four' (the Vayakhel-Pekudei exam's module, credited)", ['bringing_halted'])
    if q == 'halt_dated':
        return cell('sabbath_by_analogy_or_weekday_full_buffer', M, "Shabbat 96b:2 (opened) — 'perhaps a weekday, because the work was complete (36:7)?' — answered by the verbal analogy 'proclaiming'-'proclaiming' from the Day of Atonement (Lev 25:9): the halt dated to a Sabbath; the objection's plain sense (a full buffer on a weekday) carried beside", ['bringing_halted'])
    if q == 'enough_and_over':
        return cell('surplus', I, "36:7 'and the work was ENOUGH for all the work to do it, AND THERE WAS LEFT OVER' — 'enough' (דים) at %s, 'left over' (והותר) at %s; the surplus the treasury law disposes" % (c_enough, c_over), ['surplus_to_the_house'])
    if q == 'surplus_declared':
        return cell('tabernacle_of_the_testimony', M, TT + "Pekudei 5:5 — Moses asks what to do with the remainder: 'make with it a tabernacle for the testimony'; at the accounting he declares it — 'with the excess I made the tabernacle of the testimony' (38:21's doubled 'tabernacle')", ['surplus_to_the_house'])
    return cell('no_case', I, '', [FX.NONE])

# ---- F2: THE ARK (25:10-22; 37:1-9) ----------------------------------
def ark(q):
    if q == 'dimensions':
        return cell((2.5, 1.5, 1.5), I, "25:10 'two cubits and a half its length, a cubit and a half its width, a cubit and a half its height' — in the cubit (a PARAMETER: the cubit of Moses, Mishnah Kelim 17:9)", [FX.NONE])
    if q == 'run_dimensions':
        return cell(True, I, "37:1's ten tokens after 'and Bezalel made the ark' EQUAL 25:10's ten after 'and they shall make an ark' — %s; the table's and the cover's tails likewise %s" % (c_dims_eq[0], c_dims_eq[1:]), [FX.NONE])
    if q == 'named_maker':
        return cell([(37, 1)], I, "'and he made' subjectless %s times in the run (%s) — ONE with a named maker: 37:1 'and BEZALEL made the ark' %s; Bezalel's Exodus seats %s" % (sum(c_vayaas.values()), c_vayaas, c_maker, ['%d:%d' % k[1:] for k in c_named if k[0] == 'Exod']), [FX.NONE])
    if q == 'hands_on_the_ark':
        return cell('bezalel_alone_the_rest_at_his_word', M, TT + "Vayakhel 7:1 — Bezalel's hands only on the ark; the rest made 'at his word and counsel' — because the Holy One compresses His Presence there ('the shade of God', 25:22); Vayakhel 10:3 — the attribution law: his name on every stage because he gave his soul (38:22 'Bezalel made all')", [FX.NONE])
    if q == 'overlay_both_sides':
        return cell(True, I, "25:11 'inside and outside you shall overlay it' — %s; 37:2 'and he overlaid it inside and outside'" % ('מבית' in toks('Exod', 25, 11) and 'ומחוץ' in toks('Exod', 25, 11),), [FX.NONE])
    if q == 'three_chests':
        return cell('wood_between_two_gold', M, TT + "Vayakhel 7:3 — R. Chanina of Sepphoris: THREE chests, two of gold and one of wood, the wood inside the gold and gold inside the wood, the lips covered — executing 'inside and outside'; the rule derived: a scholar's inside like his outside", [FX.NONE])
    if q == 'crown_consonants':
        return cell('zar_stranger_zer_crown', M, SB + "Yoma 72b:7 — written זר ('stranger'), read זֵר ('crown'): merited, it is his crown; not, he is estranged from it — a written-versus-read verdict on the ark's own molding; " + TT + "Vayakhel 8:3 the same", [FX.NONE])
    if q == 'crown_seats':
        return cell((7, 28), I, "the consonants זר in the span at %s (the ark, the table twice, the incense altar — the crown) and at %d seats in the Tanakh, most of them 'stranger' (Exod 30:33, Lev 22:10, Num 17:5...): the unpointed text carries both words in one shape" % (fmt3(c_zer_span), c_zer_all), [FX.NONE])
    if q == 'three_crowns':
        return cell({'ark': 'torah', 'table': 'kingship', 'altar': 'priesthood'}, M, SB + "Yoma 72b:6 — three crowns: the altar's (Aaron's), the table's (David's), the ark's — still lying, whoever wishes may take it; " + TT + "Vayakhel 8:3 maps them to the vessels' rims, Vayakhel 7:4 the crown of a good name above them", [FX.NONE])
    if q == 'rings':
        return cell(4, I, "25:12 'four rings of gold... two on its one side and two on its other side' — the ring-tokens twenty-four times in the span", [FX.NONE])
    if q == 'staves':
        return cell('never_removed', I, "25:15 'in the rings of the ark shall the staves be; they shall NOT BE REMOVED from it' — the phrase at %s alone in the Tanakh; the chapter's one standing prohibition inside the architecture" % (c_staves,), ['staves_fixed'])
    if q == 'staves_prohibition':
        return cell('lashes', M, SB + "Yoma 72a:9 — R. Elazar: one who removes the ark's staves is flogged (with the breastplate's detaching, 28:28 — the two standing prohibitions); Rav Acha's design-spec probe ('perhaps so that it not tear?') answered by the bare negative's ink", ['staves_fixed'])
    if q == 'loose_not_slipping':
        return cell('mitparkin_ve_ein_nishmatin', M, SB + "Yoma 72a:10 — 'the staves shall be in the rings' against the insertion verses: 'they loosen but do not slip out' — the rings hold loose staves: a mechanical spec from two verses", ['staves_fixed'])
    if q == 'run_states_ban':
        return cell(False, I, "37:5 inserts the staves ('to carry the ark') and states NO ban — 25:15 is among the spec verses the run drops (%s): the run builds, the spec legislates" % ('25:15' in A_DROPPED,), ['staves_fixed'])
    if q == 'yom_kippur_staves':
        return cell('fire_pan_between_the_two_staves', A, "Mishnah Yoma 5:1 — reaching the ark 'he puts the fire-pan BETWEEN THE TWO STAVES': the poles standing in their rings on the Day of Atonement — the ban's consequence on the sheet", ['staves_fixed'])
    if q == 'testimony':
        return cell('dropped_in_run', I, "25:16 'and you shall put into the ark the testimony' and 25:21 again — both dropped by the run (%s); the placing is 40:20's (E5)" % ('25:16' in A_DROPPED and '25:21' in A_DROPPED,), [FX.NONE])
    if q == 'tablets_and_fragments':
        return cell('both_in_the_ark', M, TT + "Vayakhel 7:4 — 'you shall put into the ark' — the tablets AND the fragments of the tablets: honor the scholar who forgot his learning", [FX.NONE])
    if q == 'cover':
        return cell((2.5, 1.5), I, "25:17 'a cover of pure gold, two cubits and a half its length and a cubit and a half its width' — no height (the cover's thickness a PARAMETER); 'the cover' at 25:%s" % (c_kaporet25,), [FX.NONE])
    if q == 'cherubim_one_piece':
        return cell('from_the_cover', I, "25:19 'FROM the cover you shall make the cherubim on its two ends' — one piece; 25:18 'beaten work' (%d Torah seats: the cherubim, the lampstand thrice, the run's three, Num 8:4's lampstand, Num 10:2's trumpets)" % len(c_mikshah), [FX.NONE])
    if q == 'faces':
        return cell('each_to_his_brother_toward_the_cover', I, "25:20 'their faces each to his brother; toward the cover shall the faces of the cherubim be' — two directions in one verse", [FX.NONE])
    if q == 'faces_will_indexed':
        return cell('each_other_when_doing_the_will', M, SB + "Bava Batra 99a:6-7 — toward each other (R. Yochanan) / toward the House (R. Elazar): resolved will-indexed; the toward-the-House arm against 25:20 'each to his brother'? — ANGLED: 'ONKELOS THE CONVERT said: child-faced work, angled, like a student taking leave of his teacher' — the corpus' own translator named on this unit's ink", [FX.NONE])
    if q == 'meeting':
        return cell('hapax', I, "25:22 'and I will MEET with you there' — the form (ונועדתי) at %s alone; 'and I will speak with you from above the cover, from between the two cherubim' — the oracle address" % (c_meet,), ['meeting_appointed'])
    if q == 'oracle_layer':
        return cell('the_word', M, "Onkelos 25:22 'and I will APPOINT MY WORD for you there' — the meeting routed through the Word-layer: the cover between the cherubim the standing interface for 'all that I shall command you'; the entry fires at Num 7:89 [IMPORT by name], not in this run", ['meeting_appointed'])
    if q == 'meeting_dropped':
        return cell(True, I, "25:22 among the run's dropped verses (%s): the run builds the cover (37:6-9) and never speaks from it" % ('25:22' in A_DROPPED,), ['meeting_appointed'])
    if q == 'whereabouts':
        return cell('hidden_under_the_wood_storehouse', A, "Mishnah Shekalim 6:1-2 — the fourteenth prostration opposite the wood storehouse 'for a tradition in their hands from their fathers that THERE THE ARK WAS HIDDEN'; the priest who saw the floor differ and died before finishing", [FX.NONE])
    if q == 'after_removal':
        return cell('foundation_stone_three_fingers', A, "Mishnah Yoma 5:2 — 'from when the ark was taken, a stone was there from the days of the first prophets, called Shetiyah, three fingers above the ground, and on it he set the fire-pan' — the second Temple's Holy of Holies without the vessel the run built", [FX.NONE])
    if q == 'hidden_with':
        return cell('manna_jar_oil_staff', M, SB + "Yoma 52b:14-15 — R. Elazar's three verbal-analogy chains ('there-there', 'generations-generations', 'keeping-keeping') from the manna jar's verse (16:33-34) to the ark's terms: the jar, the anointing oil, and Aaron's staff hidden WITH the ark", [FX.NONE])
    if q == 'run_dropped':
        return cell(['25:15', '25:16', '25:21', '25:22'], I, "the ark's spec verses with no run counterpart, computed by the alignment: %s — the ban, the testimony twice, the meeting: every USE clause; the nine run verses all matched (%d of %d spec verses)" % (ALIGN['ark']['dropped'], ALIGN['ark']['matched'], ALIGN['ark']['spec']), [FX.NONE])
    if q == 'road_and_rome':
        return cell('cover_seen_in_rome', M, TT + "Vayakhel 10:2 — R. Elazar son of R. Yosei: 'I SAW THE ARK COVER IN ROME, and on it drops of blood' — from the Day of Atonement sprinklings (Mishnah Yoma 5:3-4's target); a tanna's first-person testimony to the vessel this chapter builds", [FX.NONE])
    return cell('no_case', I, '', [FX.NONE])

# ---- F3: THE TABLE (25:23-30; 37:10-16) -------------------------------
def table(q, cubit=None):
    if q == 'dimensions':
        return cell((2, 1, 1.5), I, "25:23 'two cubits its length, a cubit its width, a cubit and a half its height' — the run's 37:10 tail equal token for token (%s)" % (c_dims_eq[1],), [FX.NONE])
    if q == 'cubit_reference':
        return cell('cubit_of_moses', A, "Mishnah Kelim 17:9 — 'the cubit they spoke of is the medium cubit'; the two cubits in Shushan the Palace exceed MOSES' CUBIT by half a finger and a finger: the parameter's reference named after this span's own author; its absolute size never in the ink", [FX.NONE])
    if q == 'handbreadths':
        hb = {'vessels_five': 5, 'medium_six': 6}[cubit]
        return cell((2 * hb, 1 * hb), D, "25:23's two cubits by one under the cubit setting %r (%d handbreadths — Mishnah Kelim 17:10: R. Yehuda the vessels' cubit five, the building's six; R. Meir all medium) = %d by %d handbreadths — Mishnah Menachot 11:5's two arms by the same two names (R. Yehuda ten by five, R. Meir twelve by six); Menachot 96a:7 opened at its seat" % (cubit, hb, 2 * hb, hb), [FX.NONE])
    if q == 'sheet_table':
        return cell(PR_DIMS['table'], P, "the priesthood engine's table dimensions by CALL — cold_run_priesthood.lamp_table(dimensions)['table'] -> %r [IMPORT, live call]: the two arms the arithmetic above reproduces" % (PR_DIMS['table'],), [FX.NONE])
    if q == 'bread_faces':
        return cell('must_have_faces', M, "Menachot 96a:6 (opened per gap) = Mishnah Menachot 11:4 — ben Zoma: 'bread of the FACE before Me continually' (25:30) — that it have faces: the bread's name a form requirement; the loaf ten by five with horns of seven fingers", ['bread_set_weekly'])
    if q == 'bread_dims':
        return cell(PR_DIMS['loaf'], P, "the loaf by CALL — lamp_table(dimensions)['loaf'] -> %r; Mishnah Menachot 11:4's ten by five matches the table's ten by five under R. Yehuda's cubit" % (PR_DIMS['loaf'],), ['bread_set_weekly'])
    if q == 'fold':
        return cell({'R_Yehuda': 2.5, 'R_Meir': 2}, A, "Mishnah Menachot 11:5 — the loaf laid across the table's width and folded: two and a half handbreadths each side (R. Yehuda, the ten-wide loaf on the five-wide table... its length filling the table's width), two each side with two of air between 'that the wind blow' (R. Meir); Abba Shaul: the frankincense dishes in the gap ('beside him the tribe of Manasseh', Num 2:20)", ['bread_set_weekly'])
    if q == 'frame':
        return cell('handbreadth', I, "25:25 'a frame of a HANDBREADTH around, and a crown of gold for its frame' — the handbreadth-token at %s (the sea of Solomon, 1 Kgs 7:26; the run's 37:12); Menachot 96b:1 (opened) 'but there is its frame' — the below-or-above dispute not pursued" % (fmt(c_tefach),), [FX.NONE])
    if q == 'vessels':
        return cell(4, I, "25:29 'its dishes, its pans, its jars, and its bowls with which to pour' — four vessel nouns, all pure gold; the run's 37:16 names the same four with 'the vessels that are on the table'", [FX.NONE])
    if q == 'props_reeds_source':
        return cell('Exod 25:29', M, "Menachot 97a:5 (opened per gap) — 'four golden props were there' (Mishnah 11:6): from where? Rav Ketina: Scripture says 'and you shall make its dishes and its pans and its jars and its bowls' — the sheet's props and reeds sourced to the verse's four nouns", ['bread_set_weekly'])
    if q == 'props_reeds':
        return cell((4, 28), A, "Mishnah Menachot 11:6 — four golden props forked at the top (two per row) and twenty-eight reeds like half a hollow reed (fourteen per row); neither set nor removed on the Sabbath — removed on the eve and laid along the table", ['bread_set_weekly'])
    if q == 'orientation':
        return cell('along_the_house', A, "Mishnah Menachot 11:6 — 'all the vessels in the Temple, their length along the house's length'; 26:35's floor plan puts the table on the north side outside the veil", [FX.NONE])
    if q == 'continually':
        return cell('lifnei_tamid', I, "25:30 'and you shall set on the table bread of the face BEFORE ME CONTINUALLY' — the continuity-token (Onkelos 'continually'): a standing duty, not a one-time setting; the run drops the verse (%s) — the setting is 40:23's" % ('25:30' in A_DROPPED,), ['bread_set_weekly'])
    if q == 'exchange':
        return cell(PR_EXCH['continually'], P, "the exchange by CALL — cold_run_priesthood.lamp_table(exchange_protocol) -> %r [IMPORT]: Mishnah Menachot 11:7 'this one's handbreadth against that one's, AS IT IS SAID: before Me continually' (25:30 quoted); R. Yosei: even these remove and then these set" % (PR_EXCH,), ['bread_set_weekly'])
    if q == 'loaves':
        return cell(PR_LOAVES['count'], P, "the bread's law at its home (Lev 24:5-9, sitting L5) by CALL — lamp_table(loaves) -> %r [IMPORT]: twelve loaves of two tenths, two rows — one function at two seats, the spec's 25:30 and the law's 24:5" % (PR_LOAVES,), ['bread_set_weekly'])
    if q == 'thirteen_tables':
        return cell(13, A, "Mishnah Shekalim 6:4 — thirteen tables in the Temple: eight of marble in the slaughterhouse, two west of the ramp, two in the porch (marble in, gold out), and ONE OF GOLD WITHIN 'on which the showbread lies continually' — the spec's one table is the sheet's thirteenth; the other twelve are the descendant's", ['bread_set_weekly'])
    if q == 'ascend':
        return cell(PR_TWO['rule'], P, ("the two porch tables by CALL — lamp_table(two_tables) -> %r [IMPORT]; " + SB + "Tamid 31b:10 'ascend in holiness, never descend': marble at the entering, gold at the exiting; 31b:11 'no poverty in the place of wealth' — then why marble? metal scalds the bread") % (PR_TWO,), ['bread_set_weekly'])
    if q == 'run_dropped':
        return cell(['25:30'], I, "the table's spec verses with no run counterpart: %s — the bread clause alone; the seven run verses all matched; the numerals of spec and run EQUAL (%s)" % (ALIGN['table']['dropped'], ALIGN['table']['numerals_equal']), [FX.NONE])
    return cell('no_case', I, '', [FX.NONE])

# ---- F4: THE LAMPSTAND (25:31-40; 37:17-24) ----------------------------
def menorah(q, middah=None):
    if q == 'material':
        return cell('pure_gold_beaten', I, "25:31 'a lampstand of pure gold; beaten work shall the lampstand be made; its base and its shaft, its cups, its knobs, and its flowers shall be OF IT' — 25:36 'all of it one beaten work of pure gold' (Onkelos 'one drawn piece')", [FX.NONE])
    if q == 'valid_materials':
        arm = {'general_detail': 'of_metal', 'amplify_limit': 'all_but_earthenware'}[middah]
        return cell(arm, M, (SB + "Sukkah 50b:6-7 — THE METHOD FORK on this verse's own tokens: 'you shall make a lampstand' (general), 'pure gold' (detail), 'beaten shall the lampstand be made' (general) — Rebbi by general-detail-general: like the detail, OF METAL; R. Yosei son of R. Yehuda by amplify-limit-amplify: all but EARTHENWARE — the middah passed as the parameter %r") % (middah,), [FX.NONE])
    if q == 'no_dimensions':
        return cell(True, I, "25:31-40 hold NO cubit token (%s) — the lampstand is the one vessel the spec measures by weight (a talent) and count (seven, six, three, four, twenty-two), never by length: its height is a PARAMETER (the tradition's eighteen handbreadths, Menachot 28b, at the address index, not opened)" % (c_no_cubit_menorah == [],), [FX.NONE])
    if q == 'branches':
        return cell(7, I, "25:32 'six branches going out of its sides, three from the one side and three from the other' + the shaft (25:31 'its shaft') = seven", ['lamp_arranged'])
    if q == 'lamps':
        return cell(7, I, "25:37 'and you shall make its lamps SEVEN'; the run's 37:23 counts them in the making verse ('and he made its lamps seven')", ['lamp_arranged'])
    if q == 'indispensable':
        return cell('seven_invalidate_each_other', A, "Mishnah Menachot 3:7 — 'the seven branches of the lampstand invalidate one another; its seven lamps invalidate one another': the verse's count as a blocking rule — six branches is no lampstand", ['lamp_arranged'])
    if q == 'cups':
        return cell(22, I, "25:33 three almond cups on each of the six branches (eighteen) + 25:34 four on the shaft = 22 — Menachot 28b:17 (opened) counts the same from the same two verses; 'almond-shaped' at %s alone in the Tanakh" % (fmt2(c_almond),), [FX.NONE])
    if q == 'knobs':
        return cell(11, M, "Menachot 29a:1 (opened) — 'the knobs too, eleven: two of its own (25:34 'its knobs' — the plural read as two, the minimum plural), six of the branches (a knob per branch, 25:33), and a knob, a knob, a knob (25:35 under each pair)' — the ink gives 6 + 3 + a plural; the tradition's minimum-plural rule makes it 11", [FX.NONE])
    if q == 'knobs_under_pairs':
        return cell(3, I, "25:35 'a knob UNDER two branches of it' three times — the three 'under' tokens the gate flagged as the talion homograph, dispositioned FALSE (eleven 'under' seats in the span, %d)" % len(c_tachat), [FX.NONE])
    if q == 'flowers_exodus':
        return cell(8, I, "25:33's flower per branch (six) + 25:34's 'its flowers' on the shaft (the minimum plural, two) = 8 from Exodus alone", [FX.NONE])
    if q == 'flowers_with_numbers':
        return cell(9, M, "Menachot 29a:2 (opened) — 'the flowers, nine — from where? two of its own and six of the branches are eight' — Rav Shalman: 'to its base, to its FLOWER, beaten work' (Num 8:4 [IMPORT by name]) — the ninth flower at the base from the Numbers seat", [FX.NONE])
    if q == 'talent':
        return cell('one_talent_all_vessels', I, "25:39 'a talent of pure gold he shall make it, with all these vessels'; the run's 37:24 'a talent of pure gold he made it and all its vessels'; the talent = 3000 shekels COMPUTED from the accounts (see books)", [FX.NONE])
    if q == 'tongs_firepans':
        return cell(2, I, "25:38 'its tongs and its fire-pans, pure gold' — two kinds; the sheet's basket and jug (Mishnah Tamid 3:6) are the descendant's additions", ['lamp_arranged'])
    if q == 'lamps_face':
        return cell('toward_its_face', I, "25:37 'and he shall cause its lamps to ascend, and it shall give light toward its face' — the lamps facing the shaft; 'cause to ascend' (והעלה) the verb the gate read as the burnt offering's noun (a homograph, at 25:37 and 27:20)", ['lamp_arranged'])
    if q == 'western_lamp':
        return cell(PR_WEST['western'], P, "the western lamp by CALL — cold_run_priesthood.lamp_table(western_lamp) -> %r [IMPORT]: Lev 24:3-4's law at its home" % (PR_WEST,), ['lamp_arranged'])
    if q == 'tending':
        return cell('two_eastern_found_burning', A, "Mishnah Tamid 3:9 — the priest enters and finds the two eastern lamps burning, trims the rest and leaves these; found out, he lights them from the burning ones; a stone with three steps before the lampstand on which he stands — the height implied, never stated", ['lamp_arranged'])
    if q == 'run_dropped':
        return cell(['25:37', '25:40'], I, "the lampstand's spec verses with no run counterpart: %s — the lighting (40:25's) and the pattern clause; the eight run verses all matched" % (ALIGN['menorah']['dropped'],), [FX.NONE])
    if q == 'pattern_numbers':
        return cell('Num 8:4', I, "Num 8:4 [IMPORT by name] 'this is the work of the lampstand: beaten work of gold, to its base, to its flower, beaten work — according to the appearance the LORD SHOWED MOSES, so he made the lampstand' — the shown-pattern clause's Numbers seat, for this vessel alone", [FX.NONE])
    return cell('no_case', I, '', [FX.NONE])

# ---- F5: THE CURTAINS (26:1-14; 36:8-19) -------------------------------
def curtains(q, thickness=None):
    if q == 'linen':
        return cell((10, 28, 4), I, "26:1-2 'ten curtains of twined linen, blue, purple, and crimson, cherubim of designer's work; the length of one curtain twenty-eight cubits, the width four' — one measure for all", ['made_one'])
    if q == 'linen_width':
        return cell(40, I, "10 curtains x 4 cubits = 40 — the joined sheet's width across the tabernacle's length", ['made_one'])
    if q == 'tabernacle_length':
        return cell(30, I, "26:18 twenty boards on the south side x 26:16's board width of a cubit and a half = 30 cubits", [FX.NONE])
    if q == 'covers_length_and_back':
        return cell(True, I, "40 (the ten curtains) = 30 (the length) + 10 (26:16's board height, the back wall): the linen sheet covers the top and the back exactly — %s" % (10 * 4 == 20 * 1.5 + 10,), ['made_one'])
    if q == 'width_hang':
        return cell({'interior': 10, 'per_side': 9}, I, "28 (the curtain's length, hung crosswise) = 10 (the interior width: 26:22's six western boards x 1.5 = 9, plus the two corner boards, minus the two walls' thickness — the thickness a PARAMETER) + 9 hanging down each side of the 10-cubit wall", [FX.NONE])
    if q == 'exposed':
        ex = {'cubit_throughout': 2, 'tapering': 1}[thickness]
        return cell(ex, M, (SB + "Shabbat 98b:6 — the overhang arithmetic cascades from the taper dispute (98b:2): boards a cubit thick throughout (R. Nechemiah) leave TWO cubits of wall showing above the sockets; boards tapering to a fingerbreadth (R. Yehuda) leave ONE — the sockets' cubit; the thickness passed as the parameter %r -> %d exposed") % (thickness, ex), [FX.NONE])
    if q == 'board_thickness_in_ink':
        return cell(False, I, "26:16 gives the board's length (ten) and width (a cubit and a half) and NO thickness — the parameter the two arms set", [FX.NONE])
    if q == 'clasps':
        return cell((50, 'gold'), I, "26:5-6 'fifty loops... fifty clasps of gold, and you shall join the curtains one to another with the clasps'", ['made_one'])
    if q == 'one':
        return cell('made_one', I, "26:6 'AND THE TABERNACLE SHALL BE ONE'; 36:13 'and the tabernacle WAS one'; 26:11 'and it shall be one' (the tent), 36:18 'to be one' — the unity clause at %s" % (fmt3(c_one),), ['made_one'])
    if q == 'sister_idiom':
        return cell({'spec': 5, 'run': 0}, I, "'a woman to her sister' (אשה אל אחתה) — the spec's idiom for the curtains' joining at %d seats (26:3 twice, 26:5, 26:6, 26:17) and NOWHERE in the run (%d)" % (c_sister_spec, c_sister_run), [FX.NONE])
    if q == 'one_to_one':
        return cell({'spec': 0, 'run': 5}, I, "'one to one' (אחת אל אחת) — the run's phrase at %d seats (36:10 twice, 36:12, 36:13, 36:22) and NOWHERE in the spec (%d): the construction chapters replace the spec's kinship idiom with the numeral at every seat — a systematic lexical shift the alignment surfaced (the curtains' numerals differ by exactly this)" % (c_one_one_run, c_one_one_spec), [FX.NONE])
    if q == 'goat':
        return cell((11, 30, 4), I, "26:7-8 'curtains of goat hair for a tent over the tabernacle, ELEVEN; the length of one thirty cubits, the width four'", ['made_one'])
    if q == 'goat_extra':
        return cell({'front_doubled': 2, 'back_hang': 2}, I, "11 x 4 = 44 against the linen's 40: the extra four cubits are 26:9's sixth curtain DOUBLED at the tent's front (two) and 26:12's 'half curtain remaining hangs over the back' (two) — 44 - 40 = %d = 2 + 2" % (11 * 4 - 10 * 4,), [FX.NONE])
    if q == 'goat_width_extra':
        return cell(2, I, "30 - 28 = %d: 26:13 'the cubit on this side and the cubit on that side of the excess in the length of the tent's curtains shall hang over the sides of the tabernacle to cover it' — the spec's own overhang statement verified by its numbers" % (30 - 28,), [FX.NONE])
    if q == 'goat_clasps':
        return cell((50, 'bronze'), I, "26:10-11 'fifty loops... fifty clasps of BRONZE' — the tent's clasps bronze against the tabernacle's gold", ['made_one'])
    if q == 'covers':
        return cell(['ram_skins_red', 'tachash'], I, "26:14 'a covering for the tent of rams' skins dyed red, and a covering of tachash skins above'", [FX.NONE])
    if q == 'tachash':
        return cell({'Onkelos': 'a_name_sasgona', 'R_Yehuda': 'real_beast_one_horn', 'R_Nechemiah': 'miracle_for_the_hour'}, M, "Onkelos 25:5 renders the creature as a NAME (sasgona), not an identification; " + TT + "Terumah 6 + Buber 5: R. Yehudah — a real pure beast of the wilderness, one horn, six colors; R. Nechemiah — a miracle-work created for its hour and hidden (whence a thirty-cubit hide?)", [FX.NONE])
    if q == 'designer_vs_embroiderer':
        return cell('choshev_two_faces_rokem_one', M, (SB + "Yoma 72b:18-19 — 'designer's work' (26:1, 26:31) against 'embroiderer's work' (26:36): R. Elazar 'they embroider where they design'; R. Nechemiah — embroidery is needle work, one face; design is weaving, two faces: 'designer's work' at %d seats, 'embroiderer's work' at %d") % (c_choshev, c_rokem), [FX.NONE])
    if q == 'craft_grades':
        return cell('inner_master_outer_embroiderer', M, "Onkelos 26:1, 26:31, 26:36 — the designer rendered 'the work of the MASTER-CRAFTSMAN' for the inner fabrics, the embroiderer for the door screen: two named grades, the higher inside", [FX.NONE])
    if q == 'run_dropped':
        return cell(['26:12', '26:13'], I, "the curtains' spec verses with no run counterpart: %s — the two OVERHANG clauses: the run states the sizes and never restates the hang; all twelve run verses matched" % (ALIGN['curtains']['dropped'],), [FX.NONE])
    if q == 'run_subject':
        return cell('all_the_wise_hearted', I, "36:8 'and ALL THE WISE-HEARTED among the doers of the work made the tabernacle' — the run's one plural named subject, at the first vessel built", [FX.NONE])
    if q == 'goat_hair_descent':
        return cell('contained_voice', M, TT + "Terumah 9 + Buber 7-8 — 'I left the upper ones and said: make Me curtains of goat hair and I will dwell with you'; the Voice that burst into the nations' tents before the tabernacle stood is CONTAINED by it — the oracle interface from the other side", ['presence_dwells'])
    return cell('no_case', I, '', [FX.NONE])

# ---- F6: THE BOARDS (26:15-30; 36:20-34) -------------------------------
def boards(q):
    if q == 'board':
        return cell((10, 1.5), I, "26:16 'ten cubits the length of the board, and a cubit and a half the width of the one board' — no thickness (a PARAMETER)", [FX.NONE])
    if q == 'standing':
        return cell('as_they_grow', M, "the Terumah exam's F-034 (Sukkah 45b, credited) — 'acacia wood STANDING' (26:15): commandment objects held the way they grow; 'standing' (עמדים) at %s alone in the Torah" % (fmt(c_omdim),), [FX.NONE])
    if q == 'counts':
        return cell({'south': 20, 'north': 20, 'west': 6, 'corners': 2}, I, "26:18 twenty south, 26:20 twenty north, 26:22 six west, 26:23 two for the corners — 48 boards", [FX.NONE])
    if q == 'sockets_boards':
        return cell(96, I, "26:19 forty under the twenty, 26:21 forty under the twenty, 26:25 'eight boards and their sockets of silver, SIXTEEN sockets' (the ink's own sum for the west) — 40 + 40 + 16 = %d silver sockets under the boards" % (40 + 40 + 16,), [FX.NONE])
    if q == 'sockets_total':
        return cell(100, I, "96 under the boards + 26:32's four silver sockets under the veil's pillars = %d = 38:27's 'a hundred sockets from the hundred talents, a TALENT A SOCKET' (%s — a hapax): the spec's counts sum to the accounts' total" % (96 + 4, c_socket), ['accounts_rendered'])
    if q == 'corner_boards':
        return cell('twins_below_whole_at_top', I, "26:24 'and they shall be twins below, and together they shall be whole at its top to the one ring' — the corner boards' joint; the run's 36:29 'and they were twins... whole to its top' (the spelling shifts, twins written full)", [FX.NONE])
    if q == 'taper_fork':
        return cell({'R_Yehuda': 'fingerbreadth_at_top', 'R_Nechemiah': 'cubit_throughout'}, M, SB + "Shabbat 98b:2-4 — the boards a cubit thick below: R. Yehuda tapering to a FINGERBREADTH at the top ('whole at its top' read with 'ended, cut off'); R. Nechemiah a cubit THROUGHOUT ('together'); each answers the other's token; the corner geometry computed for each arm", [FX.NONE])
    if q == 'bars':
        return cell(15, I, "26:26-27 five bars for each of the three walls = %d; 26:28 'and the MIDDLE bar in the midst of the boards, running from end to end'" % (5 * 3,), [FX.NONE])
    if q == 'middle_bar_miracle':
        return cell('stood_by_miracle', M, SB + "Shabbat 98b:5 — 'from end to end' (26:28): taught, 'BY MIRACLE it stood' — the bar threading the three walls recorded as a standing miracle, the architecture's own honest impossibility", [FX.NONE])
    if q == 'middle_bar_provenance':
        return cell('jacobs_hand_to_egypt', M, TT + "Terumah 9 (end) + Buber 9 — Jacob planted the cedars going down to Egypt so the boards would stand ready; 'THE MIDDLE BAR went down to Egypt in Jacob's hand' — the end-to-end bar given a Genesis provenance", [FX.NONE])
    if q == 'gold':
        return cell('boards_rings_bars_overlaid', I, "26:29 'and the boards you shall overlay with gold, and their rings you shall make of gold, houses for the bars, and you shall overlay the bars with gold'", [FX.NONE])
    if q == 'interior':
        return cell({'length': 30, 'width': 10, 'height': 10}, I, "20 x 1.5 = 30 long; 10 high (26:16); the width: eight western boards x 1.5 = 12 outside, 10 inside under the cubit-thick parameter — the box the curtains' arithmetic covers", [FX.NONE])
    if q == 'raise':
        return cell('kemishpato', I, "26:30 'and you shall raise the tabernacle ACCORDING TO ITS FASHION which you were shown in the mountain' — the form at %s (Solomon's house 'according to its rule', 1 Kgs 5:8 [IMPORT by name]); the pointer dispositioned INTERNAL (the shown pattern); the raising's run is 40:17-33 (E5)" % (c_kemishpato,), [FX.NONE])
    if q == 'its_halakhah':
        return cell('according_to_its_halakhah', M, "Onkelos 26:30 — 'you shall raise the tabernacle ACCORDING TO ITS HALAKHAH': the received translation applies the law-word to the building's assembly order — the architecture has a halakhah", [FX.NONE])
    if q == 'fruit_tree_rule':
        return cell('non_fruit_acacia', M, TT + "Vayakhel 9:1 — the King to whom all belongs built His house from NON-fruit-bearing acacia: how much more must a man spare fruit trees (R. Tachalifa of Caesarea) — the waste ban's a-fortiori on the planks' species", [FX.NONE])
    if q == 'pledge':
        return cell('mishkan_mashkon', M, TT + "Vayakhel 9:2, Pekudei 2:4 — 'tabernacle' read 'PLEDGE': if Israel incurs guilt the tabernacle is seized as collateral; the doubled 'tabernacle, tabernacle' (38:21) the double mortgage — the two destructions", [FX.NONE])
    if q == 'run_dropped':
        return cell(['26:30'], I, "the boards' spec verses with no run counterpart: %s — the raising clause alone; the fifteen run verses all matched" % (ALIGN['boards']['dropped'],), [FX.NONE])
    return cell('no_case', I, '', [FX.NONE])

# ---- F7: THE VEIL AND THE SCREEN (26:31-37; 36:35-38) -------------------
def veil(q):
    if q == 'veil_spec':
        return cell(('four_colors', 'designer', 'cherubim'), I, "26:31 'a veil of blue, purple, crimson, and twined linen, designer's work, with cherubim' — the inner grade; 26:32 four acacia pillars overlaid with gold, gold hooks, four SILVER sockets", ['veil_divides'])
    if q == 'position':
        return cell('under_the_clasps', I, "26:33 'and you shall put the veil UNDER THE CLASPS' — the clasps join the first five curtains to the second five", ['veil_divides'])
    if q == 'veil_at':
        return cell(20, I, "the first five curtains span 5 x 4 = %d cubits from the front: the clasps, and the veil under them, stand at twenty" % (5 * 4,), ['veil_divides'])
    if q == 'holy_of_holies':
        return cell((10, 10, 10), I, "30 (the length) - 20 (the veil) = %d deep; 10 wide (the interior); 10 high — a CUBE" % (30 - 20,), ['veil_divides'])
    if q == 'holy':
        return cell((20, 10, 10), I, "the outer room: twenty deep, ten wide, ten high — the table north and the lampstand south (26:35)", ['veil_divides'])
    if q == 'solomon_double':
        return cell({'house': (60, 20, 30), 'heikhal': 40, 'debir': (20, 20, 20)}, I, "1 Kgs 6:2, 6:17, 6:20 [IMPORT by name] — Solomon's house sixty by twenty by thirty; the sanctuary before the inmost room forty; the inmost room twenty by twenty by twenty: the tabernacle's 30/20/10 DOUBLED in length and width (the height tripled), the inmost room a cube in both", [FX.NONE])
    if q == 'sheet_plan':
        return cell({'heikhal': 40, 'traksin': 1, 'holy_of_holies': 20}, D, "Mishnah Middot 4:7 — east to west a hundred: the porch's wall five, the porch eleven, the sanctuary's wall six, its interior FORTY, THE CUBIT PARTITION, THE HOLY OF HOLIES TWENTY... — the second Temple keeps Solomon's forty and twenty (data)", [FX.NONE])
    if q == 'divides':
        return cell('veil_divides', I, "26:33 'AND THE VEIL SHALL DIVIDE for you between the Holy and the Holy of Holies' — 'and it shall divide' at %s alone; the five-token phrase at %s alone in the Tanakh" % (c_divide, c_between), ['veil_divides'])
    if q == 'one_or_two':
        return cell({'Mishnah': 'two_a_cubit_apart', 'R_Yosei': 'one_from_26_33'}, A, "Mishnah Yoma 5:1 — the high priest walks 'between the two curtains dividing the Holy from the Holy of Holies, a cubit between them'; R. Yosei: 'there was only ONE curtain there, AS IT IS SAID: and the veil shall divide for you between the Holy and the Holy of Holies' — 26:33 quoted verbatim", ['veil_divides'])
    if q == 'second_temple_reason':
        return cell('cubit_partition_status_doubtful', M, SB + "Yoma 51b:5-6 — the Rabbis' resolution: R. Yosei's verse is the TABERNACLE's; the second Temple, missing the first's cubit-thick wall (Mishnah Middot 4:7's 'cubit partition') and doubtful of its status, made two curtains — the partition's ink meeting the descendant's architectural doubt", ['veil_divides'])
    if q == 'ladder':
        return cell(10, A, "Mishnah Kelim 1:6-9 — TEN sanctities from the land of Israel up to the Holy of Holies; the top two rungs bear 26:33's two names", ['veil_divides'])
    if q == 'spec_rungs':
        return cell(3, I, "the rungs the tabernacle's spec builds: the COURT (27:9 — 'outside the hangings', Makkot 3:3's lash boundary), the HOLY, and the HOLY OF HOLIES (26:33) — three of the ten; the rest are the land's and the descendant's", ['veil_divides'])
    if q == 'floor_plan':
        return cell({'ark': 'holy_of_holies', 'table': 'north', 'menorah': 'south'}, I, "26:34 'the cover on the ark of the testimony in the Holy of Holies'; 26:35 'the table outside the veil, and the lampstand opposite the table on the south side, and the table on the north side' — the stations as standing law (dropped by the run: the placing is 40:20-24's)", [FX.NONE])
    if q == 'lamp_not_needed':
        return cell(PR_POS, P, ("the lampstand's position by CALL — cold_run_priesthood.lamp_table(position) -> %r [IMPORT]; " + TT + "Tetzaveh 2 — 'not that I NEED its light': were the light needed, the lampstand would stand by the ark, not OUTSIDE the veil; the Temple's windows inverted so the light flows out") % (PR_POS,), ['lamp_arranged'])
    if q == 'screen':
        return cell((5, 'bronze_sockets', 'embroiderer'), I, "26:36-37 'a screen for the tent's door... embroiderer's work; five acacia pillars overlaid with gold, gold hooks, five sockets of BRONZE' — the outer grade, the bronze sockets", [FX.NONE])
    if q == 'run_adds_heads':
        return cell(True, I, "36:38 'and their heads' overlay and their bands, gold' — 'their heads' (ראשיהם) in the run's verse and NOT in 26:37 (%s); the band-root (חשק) absent from the whole veil-and-screen spec and present in 36:38 (%s): the run ADDS the pillar heads' plating and bands the spec never states" % (c_heads_36, (not any('חשק' in w for v in range(31, 38) for w in toks('Exod', 26, v)), any('חשק' in w for w in toks('Exod', 36, 38)))), [FX.NONE])
    if q == 'run_dropped':
        return cell(['26:33', '26:34', '26:35', '26:37'], I, "the veil block's spec verses with no run counterpart by the alignment: %s — the three PLACEMENT clauses, and 26:37 whose run verse (36:38) fell below the token threshold BECAUSE of its additions; the numerals of spec and run EQUAL (%s)" % (ALIGN['veil_screen']['dropped'], ALIGN['veil_screen']['numerals_equal']), [FX.NONE])
    return cell('no_case', I, '', [FX.NONE])

# ---- F8: THE ALTAR (27:1-8; 38:1-7) -------------------------------------
def altar(q):
    if q == 'dimensions':
        return cell((5, 5, 3), I, "27:1 'five cubits long and five cubits wide — SQUARE shall the altar be — and three cubits its height'; the run's 38:1 repeats five, five, square, three", [FX.NONE])
    if q == 'square':
        return cell(6, I, "'square' (רבוע) at %d Torah seats — the altar, the breastplate, the incense altar, and their three runs (%s)" % (len(c_ravua), fmt2(c_ravua)), [FX.NONE])
    if q == 'run_names_it':
        return cell('altar_of_the_burnt_offering', I, "38:1 'and he made THE ALTAR OF THE BURNT OFFERING' — the spec (27:1-8) calls it only 'the altar'; the name's Exodus seats %s: FIRST at 30:28, the verse after the incense altar's spec (30:1-10) makes a second altar — the name arrives when disambiguation does" % (fmt2(c_olah_name),), [FX.NONE])
    if q == 'horns':
        return cell('from_it', I, "27:2 'its horns on its four corners; FROM IT shall its horns be' — one piece (%s at the spec and the run); overlaid with bronze" % (c_mimenu,), [FX.NONE])
    if q == 'vessels':
        return cell(5, I, "27:3 'its pots for its ashes, its shovels, its basins, its forks, its fire-pans — all its vessels bronze'; the five stems present at 27:3 and 38:3 (%s) though the run's articled forms share no token with the spec's suffixed ones" % (c_stems,), [FX.NONE])
    if q == 'ash_duty':
        return cell('ash_removal_named_in_the_vessel_list', M, "Onkelos 27:3 'to REMOVE its ashes' — the dawn service's first act named in the vessel list; the Tzav engine holds the removal (Lev 6:3-4)", [FX.NONE])
    if q == 'pot_second_service':
        return cell('psakhter_over_the_creeping_thing', A, "Mishnah Eruvin 10:15 (the Terumah exam's F-035) — elsewhere in the sanctuary 'they overturn the PSAKHTER over it': the bronze ash-pot's second service; Tamid 5:5's three services", [FX.NONE])
    if q == 'net':
        return cell('to_the_half', I, "27:4-5 'a grate of network of bronze... under the altar's ledge beneath, and THE NET SHALL REACH TO THE HALF OF THE ALTAR' — 'its ledge' (כרכבו) at 38:4 alone", [FX.NONE])
    if q == 'red_line':
        return cell('the_torah_gave_the_partition', M, SB + "Zevachim 53a:9 — the crimson thread girding the altar at its middle to divide the upper bloods from the lower — whence? Rav Acha bar Rav Katina: 'and the net shall reach to the HALF of the altar' — THE TORAH GAVE THE PARTITION", [FX.NONE])
    if q == 'red_line_sheet':
        return cell('crimson_thread_at_the_middle', A, "Mishnah Middot 3:1 — 'and a thread of crimson girds it at the middle, to divide between the upper bloods and the lower bloods'", [FX.NONE])
    if q == 'upper_bloods':
        return cell(CH_HORNS, P, "the bloods ABOVE the line by CALL — cold_run_chatat.blood(commoner) -> %r [IMPORT, live call]: the sin offering's four horns (Mishnah Zevachim 5:3, credited)" % (CH_HORNS,), [FX.NONE])
    if q == 'lower_bloods':
        return cell(OLAH_H['applications']['v'], P, "the bloods BELOW the line by CALL — cold_run_offerings.dispatch(olah:herd)['applications'] -> %r, the peace offering's %r [IMPORT, live calls]: the edge the gate REQUIRED at 38:1's 'altar of the burnt offering', made live" % (OLAH_H['applications']['v'], SHEL['applications']['v']), [FX.NONE])
    if q == 'base':
        return cell('not_in_the_spec', I, "the BASE (יסוד) — no token in 25-27 or 36-38 (%s); 'the base of the altar' at %s: the member enters the tabernacle's altar by its USE in the offering code (Exod 29:12, Lev 4:7...), never by its build" % (c_yesod_span == [], fmt(c_yesod)), [FX.NONE])
    if q == 'base_extent':
        return cell('north_west_whole_south_east_one_cubit', A, "Mishnah Middot 3:1 — 'the base ran along the whole north and the whole west, and ate one cubit in the south and one in the east'", [FX.NONE])
    if q == 'remainders':
        return cell({'inner': 'western_base', 'outer': 'southern_base'}, A, "Mishnah Yoma 5:6 — the inner blood's remainder on the WESTERN base of the outer altar, the outer altar's on the SOUTHERN; both to the Kidron, sold to gardeners, sacrilege in them", [FX.NONE])
    if q == 'indispensables':
        return cell(['corner', 'ramp', 'base', 'square'], M, (SB + "Zevachim 62a:8 — corner, ramp, base, and square are indispensable; the measures of length, width, height are not — Rav Huna: 'THE altar' (27:1 %s): wherever the definite article stands it binds") % (c_definite,), [FX.NONE])
    if q == 'ramp':
        return cell(ORD_STEPS, P, "the ramp by CALL — cold_run_ordinances.altar(steps) -> %r [IMPORT]: 20:26's 'not by steps' compiled at E1; NO ramp in 27:1-8 or 38:1-7 — the ramp is the ordinances' derivation, the sheet's datum %r (Mishnah Middot 3:3)" % (ORD_STEPS, ORD_RAMP), [FX.NONE])
    if q == 'hollow':
        return cell('navuv_luchot', I, "27:8 'HOLLOW of boards you shall make it'; the run keeps it at 38:7 'hollow of boards he made it' (%s); the word at %s — Solomon's pillars hollow (Jer 52:21 [IMPORT by name])" % ('נבוב' in toks('Exod', 38, 7), fmt(c_navuv)), [FX.NONE])
    if q == 'earth_fill':
        return cell(ORD_EARTH, P, "the earth altar by CALL — cold_run_ordinances.altar(earth_altar) -> %r [IMPORT]: 20:24 'an altar of EARTH you shall make Me' meets 27:8's hollow box — the two verses' intersection (move M-21's form): a hollow shell filled with earth at every encampment" % (ORD_EARTH,), [FX.NONE])
    if q == 'hewn_ban':
        return cell(ORD_HEWN, P, "the hewn ban by CALL — altar(hewn) -> %r; the stones' source %r; the recipe %r [IMPORT]: the LAND's stone altar (Mishnah Middot 3:4); the tabernacle's is acacia and bronze — no stone in 27:1-8" % (ORD_HEWN, ORD_STONES, ORD_RECIPE), [FX.NONE])
    if q == 'perpetual_fire':
        return cell(TZ_EXT, P, "the perpetual fire by CALL — cold_run_tzav.altar_machine(extinguish) -> %r, retention %r [IMPORT]: Lev 6:6's fire on THIS wooden altar" % (TZ_EXT, TZ_RET), ['perpetual_fire_duty'])
    if q == 'fire_objection':
        return cell('wood_under_bronze_answered', M, TT + "Terumah 11 — Moses: You said an acacia altar plated bronze, and You said 'a perpetual fire shall burn on the altar' — the fire will pass the plating and burn the wood! The answer: the measures above (fire-angels under water-firmaments), the precedents (Aaron's staff, Moses in the fire); R. Nechemiah: the plating a DINAR's thickness (data)", ['perpetual_fire_duty'])
    if q == 'height_fork':
        return cell({'R_Yehuda': (10, 10, 3), 'R_Yosei': (5, 5, 10)}, M, "Zevachim 59b:4-8 (opened per gap) — R. Yosei: 'five by five' as written; R. Yehuda: 'square' here and at Ezek 43:16 — measured FROM THE MIDDLE, ten by ten; on the HEIGHT the arms swap: R. Yehuda 'three' as written, R. Yosei by the same analogy twice the length — ten: each authority literal on one dimension and analogical on the other", [FX.NONE])
    if q == 'height_objection':
        return cell('priest_seen_from_outside', M, "Zevachim 59b:9-10 (opened) — R. Yehuda: 'the court... its height five' (27:18) — could a priest on a ten-cubit altar be seen by all from outside? R. Yosei: 'the hangings BY the tabernacle and BY the altar' (Num 4:26 [IMPORT by name]) — as the tabernacle ten, so the altar ten; 'fifteen cubits of hangings'...", [FX.NONE])
    if q == 'three_reread':
        return cell('from_the_surround_upward', M, "Zevachim 60a:1-2 (opened) — 38:18's 'five cubits' read from the altar's edge upward, 27:1's 'three cubits its height' from the SURROUND's edge upward: the sheet's ten-cubit altar (Middot 3:1) and the spec's three reconciled by assigning the spec's number to the top segment; the fork stands", [FX.NONE])
    if q == 'sheet_altar':
        return cell(32, A, "Mishnah Middot 3:1 — 'the altar was thirty-two by thirty-two' (rising and drawing in: the base, the surround, the horns, the priests' walk, the pile twenty-four); R. Yosei: at first twenty-eight, the returning exiles added four south and west from Ezek 43:16's twelve measured from the middle — the descendant's growth from five", [FX.NONE])
    if q == 'solomon_altar':
        return cell((20, 20, 10), I, "2 Chr 4:1 [IMPORT by name] 'a bronze altar twenty cubits long, twenty wide, ten high' — four times the tabernacle's width; " + TT + "Terumah 11: Solomon kept the BRONZE altar's name on his own", [FX.NONE])
    if q == 'tabernacle_material':
        return cell('acacia_bronze_not_stone', I, "27:1 'the altar of acacia wood', 27:2 'overlay it with bronze', 38:30 'the bronze altar' — the tabernacle's altar is wood and bronze; the stone altar is the land's (20:25, Deut 27:5-6)", [FX.NONE])
    if q == 'acrostic':
        return cell('pardon_merit_blessing_life', M, TT + "Terumah 10 — 'altar' (מזבח) read as an acrostic: pardon, merit, blessing, life; the five-by-five against the two tablets' five and five, the three of height against the three deliverers, the four horns against Sinai's — the letter-arithmetic family, recorded as such", [FX.NONE])
    if q == 'run_dropped':
        return cell(['27:3', '27:4', '27:5', '27:8'], I, "the altar's spec verses with no run counterpart by the alignment: %s — but 38:3-5 build the vessels, the net, and the rings in ARTICLED forms sharing no token with the spec's SUFFIXED ones (the five stems present at both, %s), and 38:7 keeps 'hollow of boards' while dropping the shown-clause: three of the four are alignment artifacts of grammar, one (27:8's pointer) a true drop" % (ALIGN['altar']['dropped'], c_stems), [FX.NONE])
    return cell('no_case', I, '', [FX.NONE])

# ---- F9: THE COURT (27:9-19; 38:9-20) -----------------------------------
def court(q):
    if q == 'dimensions':
        return cell((100, 50, 5), I, "27:18 'the length of the court a hundred cubits, the width fifty by fifty, the height five cubits, twined linen, their sockets bronze'", [FX.NONE])
    if q == 'hangings':
        return cell(280, I, "27:9 south a hundred, 27:11 north a hundred, 27:12 west fifty, 27:14-15 east fifteen and fifteen = %d cubits of hangings" % (100 + 100 + 50 + 15 + 15,), [FX.NONE])
    if q == 'perimeter_closes':
        return cell(True, I, "280 + the gate's twenty-cubit screen (27:16) = %d = the perimeter 2 x (100 + 50) = %d: the spec's own numbers close the enclosure" % (280 + 20, 2 * (100 + 50)), [FX.NONE])
    if q == 'east':
        return cell((15, 20, 15), I, "27:13-16 the east fifty: fifteen of hangings to one shoulder, the twenty-cubit screen, fifteen to the other — 15 + 20 + 15 = %d" % (15 + 20 + 15,), [FX.NONE])
    if q == 'pillars':
        return cell(60, I, "27:10 twenty, 27:11 twenty, 27:12 ten, 27:14 three, 27:15 three, 27:16 four = %d pillars, each on a bronze socket — sixty bronze sockets; with the screen's five (26:37) sixty-five bronze against the hundred silver" % (20 + 20 + 10 + 3 + 3 + 4,), [FX.NONE])
    if q == 'silver':
        return cell('hooks_and_bands', I, "27:10, 27:11, 27:17 'the hooks of the pillars and their bands silver' — the court's silver is hooks and bands; 38:28's 1775 shekels made 'hooks for the pillars, and overlaid their heads, and banded them'", ['accounts_rendered'])
    if q == 'run_adds_silver_heads':
        return cell(True, I, "38:17 and 38:19 'AND THE OVERLAY OF THEIR HEADS silver' (%s) — 'their heads' at no verse of 27 (%s); the accounts confirm it (38:28 'and overlaid their heads', %d): the run adds a member the spec never states, and its own books account for it" % (c_heads_run, c_heads_spec, phrase('Exod', 38, 28, ['וצפה', 'ראשיהם'])), ['accounts_rendered'])
    if q == 'gate_screen':
        return cell((20, 5, 'embroiderer'), I, "27:16 'a screen of twenty cubits, blue, purple, crimson, twined linen, embroiderer's work'; 38:18 adds its height 'five cubits, corresponding to the court's hangings'", [FX.NONE])
    if q == 'court_height_read':
        return cell('five_above_the_altar', M, "Zevachim 60a:1 (opened) — R. Yosei's reading of 38:18's 'five cubits': from the altar's edge upward — the hangings fifteen (27:14's number read as height), the altar ten, five showing; R. Yehuda: five as written", [FX.NONE])
    if q == 'hangings_word':
        return cell(14, I, "'hangings' (קלעים / קלעי) at %d Torah seats, all the court's (27:9-15, 35:17, 38:9-18, 39:40, Num 4:26); %d in the Tanakh (1 Kgs 6:34's carvings and 2 Chr 26:14's slings homographs)" % (c_kelaim_torah, c_kelaim), [FX.NONE])
    if q == 'outside_the_curtains':
        return cell('forty_lashes_most_holy', A, "Mishnah Makkot 3:3 — 'most-holy offerings eaten OUTSIDE THE HANGINGS' among the forty-lashes list: 27:9's court hangings as the eating boundary's own fixture (credited)", [FX.NONE])
    if q == 'area':
        return cell(5000, I, "100 x 50 = %d square cubits" % (100 * 50,), [FX.NONE])
    if q == 'two_seah':
        return cell(70, I, "the square of the court's area: sqrt(5000) = %.2f — 'SEVENTY CUBITS AND A REMAINDER' squared (the integer part %d)" % (math.sqrt(5000), int(math.sqrt(5000))), [FX.NONE])
    if q == 'two_seah_sheet':
        return cell('R_Yosei_length_double_width', A, "Mishnah Eruvin 2:5 — the garden and enclosure 'seventy cubits and a remainder by seventy and a remainder' — the space of two seah, the tabernacle's court; R. Eliezer: a cubit's excess of length kills it; R. YOSEI: even length DOUBLE its width — 27:18's own hundred by fifty (credited)", [FX.NONE])
    if q == 'pegs':
        return cell('bronze', I, "27:19 'all the vessels of the tabernacle in all its service, and all its pegs, and all the pegs of the court, bronze'; 38:20 the same", [FX.NONE])
    if q == 'descendant':
        return cell({'temple_mount': 500, 'whole_court': (187, 135)}, D, "Mishnah Middot 2:1 — the Temple mount five hundred by five hundred; Middot 5:1 — the whole court a hundred and eighty-seven by a hundred and thirty-five: the descendant enclosures as data against the spec's hundred by fifty", [FX.NONE])
    if q == 'run_dropped':
        return cell(['27:15', '27:17', '27:18', '27:19'], I, "the court's spec verses with no run counterpart by the alignment: %s — 38:15 restates 27:15 with 'on this side and that, to the court's gate' (below threshold), 38:16-17 gather 27:17-18's totals into two summary verses with the added heads, 38:20 keeps 27:19's pegs: the run reorganizes the court's summary; seven of eleven spec verses matched" % (ALIGN['court']['dropped'],), [FX.NONE])
    return cell('no_case', I, '', [FX.NONE])

# ---- F10: THE LAMP'S OIL (27:20-21; no run verse in the span) ----------
def lamp(q):
    if q == 'tail_identity':
        return cell(13, I, "Lev 24:2's last thirteen tokens EQUAL 27:20's last thirteen (%s): 'the children of Israel, and let them take to you pure olive oil, crushed, for the light, to cause a lamp to ascend continually' — the law's seat (sitting L5, the priesthood engine) restates the spec's word for word" % (c_tail,), ['lamp_arranged'])
    if q == 'restatement':
        return cell(PR_REST['shared_tail'], P, "the identity by CALL from the law's seat — cold_run_priesthood.lamp_table(restatement) -> %r [IMPORT]: one function at two seats" % (PR_REST,), ['lamp_arranged'])
    if q == 'opening_verb':
        return cell('you_shall_command', I, "27:20 'AND YOU SHALL COMMAND the children of Israel' against Lev 24:2's 'COMMAND the children of Israel' — the spec's verb addresses Moses in the second person", ['lamp_arranged'])
    if q == 'oil':
        return cell(PR_OIL['for_the_menorah'], P, "the oil by CALL — lamp_table(oil) -> %r [IMPORT]: the three olives and three flows (Mishnah Menachot 8:4), the first of each for the lampstand" % (PR_OIL,), ['lamp_arranged'])
    if q == 'nine_grades':
        return cell(PR_GRADES, P, "the nine grades by CALL — lamp_table(nine_grades) -> %r [IMPORT] (Mishnah Menachot 8:5)" % (PR_GRADES,), ['lamp_arranged'])
    if q == 'crushed_for_light':
        return cell('not_for_meal_offerings', A, "Mishnah Menachot 8:5 — the a-fortiori (the lampstand not for eating demands pure crushed oil; the meal offerings, eaten, all the more) REFUTED: 'Scripture says (Exod 27) PURE, CRUSHED, FOR THE LIGHT — and not pure-crushed for the meal offerings'; " + TT + "Tetzaveh 3 carries the same scoping verbatim", ['lamp_arranged'])
    if q == 'evening_to_morning':
        return cell(PR_EVE['measure'], P, "27:21 'Aaron and his sons shall arrange it from evening to morning before the LORD' — by CALL lamp_table(evening_to_morning) -> %r [IMPORT] (Sifra Emor 13 11)" % (PR_EVE,), ['lamp_arranged'])
    if q == 'staffing':
        return cell(PR_ONE['staffing'], P, "27:21 'Aaron AND HIS SONS' — Lev 24:3 drops 'and his sons' (%s): the one-priest staffing rule read off the drop at sitting L5 — by CALL lamp_table(one_priest) -> %r [IMPORT]" % (c_sons, PR_ONE), ['lamp_arranged'])
    if q == 'everlasting':
        return cell('chukat_olam_ledorotam', I, "27:21 'an everlasting statute for their generations from the children of Israel' — the priesthood's first standing assignment, given before the priesthood is clothed (28:1); Onkelos 'an everlasting covenant-bond'", ['lamp_arranged'])
    if q == 'not_need':
        return cell('windows_inverted_light_flows_out', M, TT + "Tetzaveh 2, 4, 6-8 — 'not that I need its light': the lampstand outside the veil, at the table's right where kings keep their lamp at the left (26:35's stations as proof); the Temple windows narrow within and wide without", ['lamp_arranged'])
    if q == 'run_in_span':
        return cell(0, I, "the oil verses have NO run in 35:30-38:31 (%s): the lampstand is built (37:17-24) but not lit — the lighting is 40:25's (E5), the oil's law 24:2-4's" % (ALIGN['lamp']['run'],), [FX.NONE])
    return cell('no_case', I, '', [FX.NONE])

# ---- F11: THE ACCOUNTS (38:21-31) ----------------------------------------
def books(q):
    if q == 'formula':
        return cell(7, I, "38:21 'THESE ARE THE ACCOUNTS of the tabernacle' — the formula at %d seats, the other six Numbers' censuses (%s): the run's books written in the census register" % (len(c_pekudei), fmt(c_pekudei)), ['accounts_rendered'])
    if q == 'two_signatories':
        return cell(['moses', 'ithamar'], I, "38:21 'counted at the word of Moses; the service of the Levites BY THE HAND OF ITHAMAR son of Aaron the priest' — two names on the books; 'by the hand of Ithamar' at %s" % (fmt(c_itamar),), ['accounts_rendered'])
    if q == 'rule':
        return cell('no_authority_in_money_under_two', A, "Mishnah Shekalim 5:2 — 'no fewer than three treasurers and seven supervisors, and no authority is appointed over the public in money with fewer than two' — the run's two signatories satisfy the sheet's rule", ['accounts_rendered'])
    if q == 'exemption_declined':
        return cell('reckons_through_others', M, TT + "Pekudei 3:2, 5:2 — Moses the exception by divine character-witness ('trusted in all My house'), yet 'he CALLS OTHERS and reckons through them' — Ithamar: the single-signatory exemption declined in practice", ['accounts_rendered'])
    if q == 'dress':
        return cell('no_hemmed_cloak', A, "Mishnah Shekalim 3:2 — the collector enters the chamber in no hemmed cloak, shoes, tefillin, or amulet, 'for a man must satisfy men as he satisfies Heaven — and you shall be clean before the LORD and before Israel' (Num 32:22)", ['accounts_rendered'])
    if q == 'why_audit':
        return cell('the_scoffers', M, TT + "Pekudei 7:4 — 'they looked after Moses' (33:8): 'a man over the tabernacle's talents without check or count — you want him NOT rich?'; Moses vowed the accounting; 7:1 — everything 'by NUMBER and by WEIGHT' because Israel is contentious", ['accounts_rendered'])
    if q == 'missing_1775':
        return cell('found_on_the_hooks', M, TT + "Pekudei 7:3 — mid-accounting Moses forgets what the 1,775 became; the Holy One illuminates his eyes and he SEES THE HOOKS ON THE PILLARS — 'and the thousand seven hundred seventy-five he made hooks for the pillars' (38:28): the audit reconciled against the physical inventory", ['accounts_rendered'])
    if q == 'stamp_absent':
        return cell(0, I, "'as the LORD commanded Moses' at NO verse of 36-38 (%s) and at %d verses of 39-40 — the sanctuary's build stands unstamped verse by verse; the stamps arrive with the vestments and the erection (E3, E5); 38:22's 'all that the LORD commanded Moses' (%s) is the one summary" % (c_stamp_run, len(c_stamp), c_all_cmd), [FX.NONE])
    if q == 'gold':
        return cell((29, 730), I, "38:24 'the gold of the wave offering twenty-nine talents and seven hundred and thirty shekels, by the shekel of the sanctuary'", ['accounts_rendered'])
    if q == 'silver':
        return cell((100, 1775), I, "38:25 'the silver of those counted of the congregation a hundred talents and a thousand seven hundred seventy-five shekels'", ['accounts_rendered'])
    if q == 'census':
        return cell(603550, I, "38:26 'for six hundred thousand and three thousand five hundred and fifty' — the number at %s: Numbers 1:46 and 2:32 [IMPORT by name] count the same men" % (fmt(c_census),), ['accounts_rendered'])
    if q == 'beka':
        return cell(2, I, "38:26 'a BEKA a head, half a shekel by the sanctuary shekel' — 'beka' at %s in the Torah: the census half-shekel and Rebekah's nose-ring (Gen 24:22 [IMPORT by name], 'a beka its weight')" % (fmt(c_beka),), [FX.NONE])
    if q == 'talent':
        t = (603550 // 2 - 1775) // 100
        return cell(t, I, "THE TALENT COMPUTED: 603,550 half-shekels = %d shekels = 100 talents + 1,775 -> a talent = (%d - 1775) / 100 = %d shekels — the metrological constant derived from the accounts' own arithmetic, no tradition consulted" % (603550 // 2, 603550 // 2, t), ['accounts_rendered'])
    if q == 'talent_check':
        return cell(True, I, "100 x 3000 + 1775 = %d = 603,550 / 2 = %d — the books balance to the shekel" % (100 * 3000 + 1775, 603550 // 2), ['accounts_rendered'])
    if q == 'sockets':
        return cell(100, I, "38:27 'the hundred talents of silver to cast the sockets of the sanctuary and the sockets of the veil: a hundred sockets to the hundred talents, a talent a socket' — the spec's 96 + 4 (26:19-25, 26:32) = %d" % (96 + 4,), ['accounts_rendered'])
    if q == 'hooks':
        return cell(1775, I, "38:28 'and the thousand seven hundred seventy-five he made hooks for the pillars, and overlaid their heads, and banded them' — the remainder to the last shekel", ['accounts_rendered'])
    if q == 'bronze':
        return cell((70, 2400), I, "38:29 'the bronze of the wave offering seventy talents and two thousand four hundred shekels' — 2,400 < 3,000: the books do not round up to a talent", ['accounts_rendered'])
    if q == 'bronze_maneh':
        return cell(96, I, "2,400 shekels / 25 shekels per ordinary maneh (a hundred dinars) = %d maneh — the number the tradition names at this verse" % (2400 // 25,), [FX.NONE])
    if q == 'double_maneh':
        return cell('sanctuary_maneh_double', M, (SB + "Bekhorot 5a:18 — 'ninety-six maneh stand there and the verse counted them in small change rather than a talent: learn that THE SANCTUARY MANEH WAS DOUBLE' — a talent of 3,000 shekels is sixty maneh of fifty (= %d), not of twenty-five") % (3000 // 50,), [FX.NONE])
    if q == 'bronze_items':
        return cell(8, I, "38:30-31 — the bronze's disposition to eight objects (%d 'and the' items): the door's sockets, the bronze altar, its net, its vessels, the court's sockets, the gate's sockets, the tabernacle's pegs, the court's pegs" % (c_bronze_items,), ['accounts_rendered'])
    if q == 'sanctuary_shekel':
        return cell(3, I, "'by the shekel of the sanctuary' at %s in the accounts — %d seats in the Tanakh; the shekel's definition ('twenty gerahs', 30:13) is E4's" % (fmt3(c_shekel_span), c_shekel_all), [FX.NONE])
    if q == 'conversion_layer':
        return cell('selaim_of_the_sanctuary', M, "Onkelos 38:24-26 — 'shekel' rendered 'SELAIM, by the selaim of the sanctuary'; 'half a shekel' 'half a sela': the translation layer converting the currency at the audit lines", [FX.NONE])
    if q == 'oholiab':
        return cell('dan_named_for_praise', M, TT + "Vayakhel 4:5 + Buber 3:1 — named with pedigree for praise (Oholiab of DAN, Bezalel of JUDAH) and for scorn (Shelomith of Dan — Lev 24:11's blasphemer's mother, the lev24 runner's span; Achan of Judah): the pedigree convention's 2x2 table", [FX.NONE])
    if q == 'mirrors':
        return cell({'Onkelos': 'praying_women', 'Tanchuma': 'mirrors_of_desire_accepted'}, M, "38:8 the laver 'from the MIRRORS of the assembling women who assembled at the door of the tent of meeting' — Onkelos: the women 'who came to PRAY'; " + TT + "Pekudei 9:4: Moses angry, the Holy One — 'these mirrors raised all the hosts in Egypt: take them' — the two tracks of one word, both carried; the laver itself E4's (30:18)", [FX.NONE])
    if q == 'assembling_women':
        return cell({'defective': 'Exod 38:8', 'plene': '1Sam 2:22'}, I, "'the assembling women' at 38:8 (הצבאת, defective) and at 1 Sam 2:22 (הצבאות, plene — the women 'who assembled at the door of the tent of meeting' with whom Eli's sons lay; the plene form's other five seats are 'the hosts' of the divine title, Amos, Hosea, Chronicles) — the same women at two seats with two spellings; 'mirrors' (במראת) with Gen 46:2's 'visions of the night'", [FX.NONE])
    if q == 'e4_owed':
        return cell(['הקטרת', 'המשחה', 'קטרת', 'הכיור'], I, "the run's tokens whose spec is Exod 30 (%s): the incense altar (37:25-28), the anointing oil and the incense (37:29), the laver (38:8) — OWED to E4 on the gate's worklist; the shekel tokens at 38:24-29 likewise" % (c_e4,), [FX.NONE])
    if q == 'creation_map':
        return cell(7, M, TT + "Pekudei 2:3 — the tabernacle equals creation day by day: the curtains the heavens, the veil the dividing firmament, the laver the gathered waters, the lampstand the lights, the cherubim the winged, the anointed priest Adam, 'the work was completed' the seventh — heaven and earth witnesses, the tabernacle the testimony", [FX.NONE])
    return cell('no_case', I, '', [FX.NONE])

# ---- F12: THE SCENE — the order, the alignment, the world engine --------
def law_sanctuary_build(event, world):
    """The build's daemon: consumes the run's recorded acts (the ink's own verbs) and writes the ledger — never emits an event."""
    k, subj, src = event['kind'], event['subject'], event['case_source']
    E = lambda eff, s, cp=None, value=None, law=None: {'effect': eff, 'subject': s, 'counterparty': cp, 'amount': None, 'due': None, 'value': value if value is not None else True, 'source_law': law or 'F%s' % event.get('law', '1'), 'case_source': src}
    if k == 'offering_brought': return [E('set_apart_before_me', subj, 'the-sanctuary')]
    if k == 'overflow_reported': return []      # W6 (2026-09-07): CONSUMED with no ledger write — 36:5's report is the halt's cause; the halt (36:6) is the act that writes
    if k == 'halt_proclaimed': return [E('bringing_halted', subj)]
    if k == 'vessel_made':
        v = event['vessel']
        if v == 'curtains': return [E('made_one', 'the-tabernacle')]
        if v == 'ark': return [E('staves_fixed', 'the-ark')]
        if v == 'veil': return [E('veil_divides', 'the-house')]
        if v == 'altar': return [E('perpetual_fire_duty', 'the-altar', value=altar('perpetual_fire')['v'], law='F8 [W6: the altar MADE (38:1-7) carries Lev 6:6\'s fire duty from its making — CALLED cold_run_tzav.altar_machine(extinguish) -> %s; Midrash Tanchuma Terumah 11: Moses\' objection raised AT THE SPEC (a wooden altar under a perpetual fire) — %s]' % (altar('perpetual_fire')['v'], altar('fire_objection')['v']))]
        return []      # the table, lampstand, boards, screen, court: made, no ledger entry until their use; E4's three: no law here
    if k == 'accounts_rendered': return [E('accounts_rendered', subj), E('surplus_to_the_house', subj, 'the-house')]
    return []

def scene():
    with contextlib.redirect_stdout(io.StringIO()):
        w = WE.World(era='the construction (clock unit: days)')
        w.laws = [law_sanctuary_build]
        for src in ('Exod 36:3 (the first morning)', 'Exod 36:3 (the second morning)'):
            w.submit({'kind': 'offering_brought', 'subject': 'the-people', 'case_source': src, 'law': '1'})
        w.submit({'kind': 'overflow_reported', 'subject': 'the-craftsmen', 'case_source': 'Exod 36:5', 'law': '1'})
        w.submit({'kind': 'halt_proclaimed', 'subject': 'the-camp', 'case_source': 'Exod 36:6', 'law': '1'})
        for v, src in (('curtains', 'Exod 36:8-19'), ('boards', 'Exod 36:20-34'), ('veil', 'Exod 36:35-36'), ('screen', 'Exod 36:37-38'), ('ark', 'Exod 37:1-9'),
                       ('table', 'Exod 37:10-16'), ('menorah', 'Exod 37:17-24'), ('incense_altar', 'Exod 37:25-28'), ('anointing_oil', 'Exod 37:29'),
                       ('altar', 'Exod 38:1-7'), ('laver', 'Exod 38:8'), ('court', 'Exod 38:9-20')):
            w.submit({'kind': 'vessel_made', 'subject': 'the-craftsmen', 'vessel': v, 'case_source': src, 'law': '12'})
        w.submit({'kind': 'accounts_rendered', 'subject': 'the-treasury', 'case_source': 'Exod 38:21-31', 'law': '11'})
    n = lambda eid, eff: len([e for e in w.entity(eid).ledger if e['effect'] == eff])
    events = len([l for l in w.log if l[0] == 'EVENT'])
    return (n('the-people', 'set_apart_before_me'), n('the-camp', 'bringing_halted'), n('the-tabernacle', 'made_one'), n('the-ark', 'staves_fixed'),
            n('the-house', 'veil_divides'), n('the-treasury', 'accounts_rendered'), n('the-treasury', 'surplus_to_the_house'),
            n('the-people', 'presence_dwells'), n('the-ark', 'meeting_appointed'), events), (n('the-altar', 'perpetual_fire_duty'), len([l for l in w.log if l[0] == 'EVENT' and l[2]['kind'] == 'overflow_reported']), events), w
SCENE, SCENE_W6, _W = scene()
def build(q):
    if q == 'world_w6':
        return cell(SCENE_W6, I, "THE W6 SCENE on the same world — the altar made (38:1-7) now carries the PERPETUAL FIRE DUTY from its making (Lev 6:6 by call; Tanchuma Terumah 11's objection raised at the spec), and the overflow report (36:5) is CONSUMED by the daemon with no ledger write — the halt writes: (fire duty on the altar, the overflow reports on the tape, events)", ['perpetual_fire_duty'])
    if q == 'spec_order':
        return cell(SPEC_ORDER, I, "the spec's order of first mention from 25:10: %s — the VESSELS first (ark, table, lampstand), then the HOUSE (curtains, boards, veil, screen), then the altar and the court" % (SPEC_ORDER,), [FX.NONE])
    if q == 'run_order':
        return cell(RUN_ORDER, I, "the run's order of first mention from 36:8: %s — the HOUSE first, then the vessels, then E4's three (the incense altar, the oil, the laver) interleaved, the altar, the court" % (RUN_ORDER,), [FX.NONE])
    if q == 'house_first':
        return cell(('vessels_first', 'house_first'), I, "the spec puts the ark before the curtains (%s); the run puts the curtains before the ark (%s) — the build REVERSES the command's order, and no verse of either stratum says why" % (SPEC_ORDER.index('ark') < SPEC_ORDER.index('curtains'), RUN_ORDER.index('curtains') < RUN_ORDER.index('ark')), [FX.NONE])
    if q == 'order_fork':
        return cell({'Berakhot_55a': 'gods_order_house_first_moses_reversed', 'Tanchuma_Vayakhel_6_5': 'bezalel_ark_first_moses_house_first'}, M, "Berakhot 55a:12 (opened per gap) — God told Moses 'tabernacle, ark, vessels'; Moses REVERSED it to 'ark, vessels, tabernacle'; Bezalel: 'the custom of the world — a man builds a house and then brings in vessels... perhaps God said tabernacle, ark, vessels?' — 'perhaps you were in God's shadow and knew': THE RUN'S ORDER IS THE ORIGINAL, the spec's written order Moses' inversion; " + TT + "Vayakhel 6:5 + Buber 8:3 carry the roles REVERSED (Bezalel ark-first against Moses house-first) — a two-recension dispute over which scheduling argument the exchange carried; both tracks carried", [FX.NONE])
    if q == 'run_teaches_spec':
        return cell('the_order_restored', M, "move M-22 (the run read back into the spec) in a new form: at D8 the run gave the spec a COLUMN (hand-laying, the right palm); here the run gives the spec its ORDER — the Babylonian seat reads the construction sequence as the command's original and the written command as the messenger's inversion", [FX.NONE])
    if q == 'alignment':
        return cell(A_TOTAL, I, "the alignment engine: (spec verses, run verses, spec matched, run matched, dropped) = %s — every run verse aligned to its block's spec verse by normalized token overlap at threshold 0.3" % (A_TOTAL,), [FX.NONE])
    if q == 'dropped':
        return cell(A_DROPPED, I, "the twenty-four spec verses with no run counterpart: %s — the ban (25:15), the testimony (25:16, 25:21), the meeting (25:22), the bread (25:30), the lighting (25:37), the pattern (25:40, 26:30, 27:8), the overhang (26:12-13), the placements (26:33-35), the oil (27:20-21), and the grammar artifacts named in each block" % (A_DROPPED,), [FX.NONE])
    if q == 'dropped_kinds':
        return cell('use_clauses_and_the_pattern', I, "what the run drops is of one kind: every clause that USES a vessel (put, set, light, divide, meet, not-remove) and every SHOWN-PATTERN clause — the run is the making alone; the use is the law layer (Lev 24; Exod 40) and the pattern is the vision", [FX.NONE])
    if q == 'numerals_equal':
        return cell(['table', 'veil_screen'], I, "the blocks whose numeral multisets match exactly between spec and run: %s — the others differ by the idiom shift ('one to one'), the run's added counts (37:23's seven lamps, 38:18's five), and grammar" % (A_NUM_EQ,), [FX.NONE])
    if q == 'verbs':
        return cell({'spec_you_shall_make': 30, 'spec_they_shall_make': 2, 'run_and_he_made': 37, 'run_named_makers': 1}, I, "the spec's 'and you shall make' %d times and 'and they shall make' %d; the run's 'and he made' %d times (%s) with the maker named once (37:1)" % (c_veasita, len(c_veasu), sum(c_vayaas.values()), c_vayaas), [FX.NONE])
    if q == 'metals':
        return cell({'gold': (25, 30), 'silver': (9, 15), 'bronze': (13, 18)}, I, "the metal-tokens spec vs run: %s — the run names each metal more often than the spec (the accounts add silver and bronze lines)" % (c_metals,), [FX.NONE])
    if q == 'tokens':
        return cell((1182, 1362), I, "the spec's 98 verses hold %d tokens, the run's 104 hold %d: the run is longer by the workforce (35:30-36:7) and the accounts (38:21-31), shorter by every use-clause" % c_tokens, [FX.NONE])
    if q == 'world':
        return cell(SCENE, I, "THE SCENE on the world engine: two mornings of offering brought (set apart), the overflow reported (no law), the halt proclaimed (the camp blocked), twelve vessels made — the curtains write 'made one', the ark 'staves fixed', the veil 'divides', the rest and E4's three write nothing — the accounts rendered and the surplus transferred; the two HEAVEN entries the spec PROMISES (the Presence dwelling, the meeting at the cover) NOT fired: the run ends at 38:31 — (set apart, halted, one, staves, divides, accounts, surplus, presence, meeting, events)", ['set_apart_before_me', 'bringing_halted', 'made_one', 'staves_fixed', 'veil_divides', 'accounts_rendered', 'surplus_to_the_house'])
    return cell('no_case', I, '', [FX.NONE])

# ---- (2) the answer sheet — the Mishnah rows as TEST DATA (verified by their own tokens) ----
def load(t):
    d = json.load(open('<repo-old>/Data/mishnah_%s_he.json' % t))
    return d['text'] if isinstance(d, dict) and 'text' in d else d
SHELF = {t: load(t.lower()) for t in ('Middot', 'Shekalim', 'Yoma', 'Kelim', 'Menachot', 'Tamid', 'Eruvin', 'Makkot', 'Sanhedrin', 'Shevuot', 'Sukkah', 'Terumot', 'Zevachim')}
def mrow(book, ch, m, must):
    txt = strip(SHELF[book][ch - 1][m - 1])
    assert must in txt, 'answer-sheet check failed: %r not in Mishnah %s %d:%d' % (must, book, ch, m)
SHEET = [
    ('Middot', 2, 1, 'חמש'), ('Middot', 3, 1, 'סקרא'), ('Middot', 3, 3, 'וכבש'), ('Middot', 3, 4, 'כרם'), ('Middot', 4, 7, 'טרקסין'), ('Middot', 5, 1, 'הכפרת'),
    ('Shekalim', 4, 4, 'רקועי'), ('Shekalim', 4, 6, 'האמנין'), ('Shekalim', 5, 2, 'גזברין'), ('Shekalim', 5, 6, 'חשאים'), ('Shekalim', 6, 1, 'נגנז'), ('Shekalim', 6, 2, 'נגנז'),
    ('Shekalim', 6, 4, 'שלחנות'), ('Shekalim', 1, 4, 'בוכרי'),
    ('Yoma', 5, 1, 'פרכת'), ('Yoma', 5, 2, 'שתיה'), ('Yoma', 5, 6, 'קדרון'),
    ('Kelim', 1, 6, 'קדשות'), ('Kelim', 1, 8, 'הבית'), ('Kelim', 1, 9, 'הקדשים'), ('Kelim', 17, 9, 'משה'), ('Kelim', 17, 10, 'טפחים'),
    ('Menachot', 11, 4, 'פנים'), ('Menachot', 11, 5, 'עשרה'), ('Menachot', 11, 6, 'סניפין'), ('Menachot', 11, 7, 'תמיד'), ('Menachot', 3, 7, 'מנורה'), ('Menachot', 8, 4, 'זיתים'), ('Menachot', 8, 5, 'למאור'),
    ('Tamid', 3, 9, 'מזרחיים'), ('Eruvin', 2, 5, 'ושירים'), ('Eruvin', 10, 15, 'פסכתר'), ('Makkot', 3, 3, 'לקלעים'), ('Sanhedrin', 1, 5, 'העזרות'),
    ('Shevuot', 1, 1, 'יציאות'), ('Shevuot', 2, 2, 'ותמים'), ('Sukkah', 3, 14, 'הלולב'), ('Terumot', 1, 1, 'החרש'), ('Zevachim', 5, 3, 'קרנות'),
]
for b, ch, m, must in SHEET:
    mrow(b, ch, m, must)
print('answer sheet: %d Mishnah rows verified by their own tokens (Middot whole, Shekalim 4-6, Yoma 5, Kelim 1, Menachot 11, Tamid 3 with the topic and link rows — the sanctuary docket)' % len(SHEET))

TESTS = [
 # ---- THE OFFERING AND THE WORKFORCE (25:1-9; 35:30-36:7) ----
 ('Exod 25:2-3 — the offering-token three times', offering('three_tokens'), 3),
 ('Onkelos Exod 25:2 — set apart BEFORE Me', offering('set_apart'), 'set_apart_before_me'),
 ('Exod 25:2 — the willing heart the sole trigger; no amount in the ink', offering('trigger'), 'willing_heart'),
 ('Exod 25:2 — the five tokens present', offering('five_tokens_present'), 5),
 ('Tanchuma Terumah 3 = Mishnah Terumot 1:1 — the five who may not separate, word by word', offering('five_barred'), ['deaf_mute', 'incompetent', 'minor', 'not_his', 'gentile']),
 ('Exod 25:3-7 — the conjunction chain breaks at the oil and the stones', offering('material_segments'), [11, 2, 2]),
 ('Tanchuma Terumah 5 — thirteen (the stones the priests\')', offering('thirteen'), 13),
 ('Exod 25:8, 25:10 — "they shall make" at two seats only', offering('plural_making'), [(25, 8), (25, 10)]),
 ('Tanchuma Vayakhel 8:1 + Yoma 3b:3 — the ark: all Israel; the will-indexed dispatch', offering('ark_they'), 'all_israel'),
 ('Exod 25:8 — "and I will dwell among them" at two Tanakh seats', offering('dwell_phrase'), 2),
 ('Onkelos Exod 25:8 — the Presence dwells in the people', offering('dwells_in'), 'the_people_not_the_building'),
 ('the shown-pattern clause at four seats, each a hapax', offering('shown_clauses'), 4),
 ('the pattern-word in the Torah: the blueprint and the image ban', offering('pattern_word_torah'), ['Deut 4:16', 'Deut 4:17', 'Deut 4:18', 'Exod 25:9']),
 ('Mishnah Shevuot 2:2 + Sanhedrin 1:5 — "so shall you make" the extension constitution', offering('so_shall_you_make'), 'extension_constitution'),
 ('Mishnah Shevuot 2:2 — the six requirements (data)', offering('extension_requirements'), ['king', 'prophet', 'urim_tummim', 'sanhedrin_71', 'two_thanksgivings', 'song']),
 ('Temurah 31b:7 — "make ME" = from what is Mine: the craftsmen from the house fund', offering('craftsmen_pay'), 'from_the_house_fund'),
 ('Mishnah Shekalim 4:6 — R. Akiva / ben Azzai on the craftsmen\'s wages', offering('wages_mechanism'), 'R_Akiva_direct_ben_Azzai_desacralize'),
 ('Mishnah Shekalim 4:4 — the surplus: gold leaf for the Holy of Holies', offering('surplus'), 'gold_leaf_holy_of_holies'),
 ('Mishnah Shekalim 4:4 — the three arms (data)', offering('surplus_arms'), {'R_Yishmael': 'service_vessels', 'R_Akiva': 'altar_summer', 'R_Chananya': 'service_vessels'}),
 ('Tanchuma Terumah 8 — no earlier and later: spoken on the Day of Atonement', offering('timestamp'), 'day_of_atonement_after_the_calf'),
 ('Exod 31:2 / 35:30 — "called by name" twice, two phrases', offering('named_by_name'), 2),
 ('Tanchuma Pekudei 3:1 — two audiences', offering('two_audiences'), 'angels_and_israel'),
 ('Berakhot 55a:11 — three-party consent', offering('consent'), 'god_moses_israel'),
 ('Tanchuma Vayakhel 3:2 — the nepotism charge answered by the verse', offering('nepotism'), 'answered_by_the_verse'),
 ('Exod 35:31 — three attributes', offering('three_attributes'), 3),
 ('Tanchuma Vayakhel 5:1-2 + Berakhot 55a:13 — one toolchain, four builds', offering('toolchain'), 'creation_tabernacle_temple_future'),
 ('"wise of heart" at six seats', offering('wise_hearted'), 6),
 ('Exod 35:34 — to teach, in his heart', offering('teaching'), 'to_teach_in_his_heart'),
 ('Exod 36:3 — morning by morning = two (Tanchuma Pekudei 5:4)', offering('two_mornings'), 2),
 ('Exod 36:6 — the people restrained from bringing', offering('halt'), 'bringing_halted'),
 ('Shabbat 96b:1 — the carrying labor sourced to the halt order', offering('carrying_labor'), 'from_private_to_public_domain'),
 ('Mishnah Shevuot 1:1 — the carryings-out, two that are four', offering('carryings'), 4),
 ('Shabbat 96b:2 — the halt dated: a Sabbath by analogy, or a weekday\'s full buffer', offering('halt_dated'), 'sabbath_by_analogy_or_weekday_full_buffer'),
 ('Exod 36:7 — enough, and left over', offering('enough_and_over'), 'surplus'),
 ('Tanchuma Pekudei 5:5 — the surplus declared in the accounts', offering('surplus_declared'), 'tabernacle_of_the_testimony'),
 # ---- THE ARK (25:10-22; 37:1-9) ----
 ('Exod 25:10 — two and a half by one and a half by one and a half', ark('dimensions'), (2.5, 1.5, 1.5)),
 ('Exod 37:1 — the run\'s dimensions equal the spec\'s token for token', ark('run_dimensions'), True),
 ('Exod 37:1 — the ONE named maker among thirty-seven "and he made"', ark('named_maker'), [(37, 1)]),
 ('Tanchuma Vayakhel 7:1, 10:3 — Bezalel\'s hands on the ark alone', ark('hands_on_the_ark'), 'bezalel_alone_the_rest_at_his_word'),
 ('Exod 25:11 — inside and outside', ark('overlay_both_sides'), True),
 ('Tanchuma Vayakhel 7:3 — three chests', ark('three_chests'), 'wood_between_two_gold'),
 ('Yoma 72b:7 — written stranger, read crown', ark('crown_consonants'), 'zar_stranger_zer_crown'),
 ('the crown-consonants: seven in the span, twenty-eight in the Tanakh', ark('crown_seats'), (7, 28)),
 ('Yoma 72b:6 / Tanchuma Vayakhel 8:3 — three crowns', ark('three_crowns'), {'ark': 'torah', 'table': 'kingship', 'altar': 'priesthood'}),
 ('Exod 25:12 — four rings', ark('rings'), 4),
 ('Exod 25:15 — never removed (a hapax)', ark('staves'), 'never_removed'),
 ('Yoma 72a:9 — lashes', ark('staves_prohibition'), 'lashes'),
 ('Yoma 72a:10 — they loosen but do not slip out', ark('loose_not_slipping'), 'mitparkin_ve_ein_nishmatin'),
 ('Exod 37:5 — the run states no ban', ark('run_states_ban'), False),
 ('Mishnah Yoma 5:1 — the fire-pan between the two staves', ark('yom_kippur_staves'), 'fire_pan_between_the_two_staves'),
 ('Exod 25:16, 25:21 — the testimony dropped in the run', ark('testimony'), 'dropped_in_run'),
 ('Tanchuma Vayakhel 7:4 — the tablets and their fragments', ark('tablets_and_fragments'), 'both_in_the_ark'),
 ('Exod 25:17 — the cover two and a half by one and a half, no height', ark('cover'), (2.5, 1.5)),
 ('Exod 25:19 — the cherubim from the cover', ark('cherubim_one_piece'), 'from_the_cover'),
 ('Exod 25:20 — faces each to his brother, toward the cover', ark('faces'), 'each_to_his_brother_toward_the_cover'),
 ('Bava Batra 99a:6-7 — will-indexed; Onkelos named: angled', ark('faces_will_indexed'), 'each_other_when_doing_the_will'),
 ('Exod 25:22 — "and I will meet" a hapax', ark('meeting'), 'hapax'),
 ('Onkelos Exod 25:22 — the Word appointed', ark('oracle_layer'), 'the_word'),
 ('Exod 25:22 — dropped in the run', ark('meeting_dropped'), True),
 ('Mishnah Shekalim 6:1-2 — where the ark was hidden', ark('whereabouts'), 'hidden_under_the_wood_storehouse'),
 ('Mishnah Yoma 5:2 — the foundation stone after the ark', ark('after_removal'), 'foundation_stone_three_fingers'),
 ('Yoma 52b:14-15 — hidden with the jar, the oil, the staff', ark('hidden_with'), 'manna_jar_oil_staff'),
 ('the ark\'s dropped spec verses: the four use clauses', ark('run_dropped'), ['25:15', '25:16', '25:21', '25:22']),
 ('Tanchuma Vayakhel 10:2 — the cover seen in Rome', ark('road_and_rome'), 'cover_seen_in_rome'),
 # ---- THE TABLE (25:23-30; 37:10-16) ----
 ('Exod 25:23 — two by one by one and a half', table('dimensions'), (2, 1, 1.5)),
 ('Mishnah Kelim 17:9 — the cubit of Moses as the reference', table('cubit_reference'), 'cubit_of_moses'),
 ('Mishnah Kelim 17:10 / Menachot 11:5 — R. Yehuda\'s vessels-cubit: ten by five', table('handbreadths', cubit='vessels_five'), (10, 5)),
 ('Mishnah Kelim 17:10 / Menachot 11:5 — R. Meir\'s medium cubit: twelve by six', table('handbreadths', cubit='medium_six'), (12, 6)),
 ('the priesthood engine\'s table by call', table('sheet_table'), ['R._Yehuda_ten_by_five', 'R._Meir_twelve_by_six']),
 ('Menachot 96a:6 / Mishnah 11:4 — ben Zoma: that it have faces', table('bread_faces'), 'must_have_faces'),
 ('the loaf by call: ten by five, horns seven', table('bread_dims'), 'ten_by_five_horns_seven'),
 ('Mishnah Menachot 11:5 — the fold under each arm', table('fold'), {'R_Yehuda': 2.5, 'R_Meir': 2}),
 ('Exod 25:25 — a frame of a handbreadth', table('frame'), 'handbreadth'),
 ('Exod 25:29 — four vessel nouns', table('vessels'), 4),
 ('Menachot 97a:5 — the props and reeds sourced to 25:29', table('props_reeds_source'), 'Exod 25:29'),
 ('Mishnah Menachot 11:6 — four props, twenty-eight reeds', table('props_reeds'), (4, 28)),
 ('Mishnah Menachot 11:6 — along the house', table('orientation'), 'along_the_house'),
 ('Exod 25:30 — before Me continually', table('continually'), 'lifnei_tamid'),
 ('Mishnah Menachot 11:7 by call — this one\'s handbreadth against that one\'s', table('exchange'), 'ones_handbreadth_against_the_others'),
 ('Lev 24:5 by call — twelve loaves (one function at two seats)', table('loaves'), 12),
 ('Mishnah Shekalim 6:4 — thirteen tables, the spec\'s the inner gold one', table('thirteen_tables'), 13),
 ('Tamid 31b:10 by call — raise in holiness, never lower', table('ascend'), 'raise_in_holiness_never_lower'),
 ('the table\'s dropped spec verse: the bread clause', table('run_dropped'), ['25:30']),
 # ---- THE LAMPSTAND (25:31-40; 37:17-24) ----
 ('Exod 25:31, 25:36 — pure gold, beaten, one piece', menorah('material'), 'pure_gold_beaten'),
 ('Sukkah 50b:6 — Rebbi by general-detail-general: of metal', menorah('valid_materials', middah='general_detail'), 'of_metal'),
 ('Sukkah 50b:7 — R. Yosei son of R. Yehuda by amplify-limit-amplify: all but earthenware', menorah('valid_materials', middah='amplify_limit'), 'all_but_earthenware'),
 ('Exod 25:31-40 — no cubit token: the height a parameter', menorah('no_dimensions'), True),
 ('Exod 25:32 — six branches and the shaft: seven', menorah('branches'), 7),
 ('Exod 25:37 — seven lamps', menorah('lamps'), 7),
 ('Mishnah Menachot 3:7 — the seven invalidate one another', menorah('indispensable'), 'seven_invalidate_each_other'),
 ('Exod 25:33-34 — twenty-two cups (Menachot 28b:17)', menorah('cups'), 22),
 ('Menachot 29a:1 — eleven knobs by the minimum plural', menorah('knobs'), 11),
 ('Exod 25:35 — three knobs under the pairs (the "under" homographs)', menorah('knobs_under_pairs'), 3),
 ('Exod 25:33-34 — eight flowers from Exodus alone', menorah('flowers_exodus'), 8),
 ('Menachot 29a:2 — nine with Num 8:4\'s base flower', menorah('flowers_with_numbers'), 9),
 ('Exod 25:39 — one talent, all the vessels', menorah('talent'), 'one_talent_all_vessels'),
 ('Exod 25:38 — tongs and fire-pans: two kinds', menorah('tongs_firepans'), 2),
 ('Exod 25:37 — the lamps face the shaft', menorah('lamps_face'), 'toward_its_face'),
 ('Lev 24:3-4 by call — the western lamp', menorah('western_lamp'), 'always_burning_begin_from_it_end_at_it'),
 ('Mishnah Tamid 3:9 — the two eastern lamps found burning', menorah('tending'), 'two_eastern_found_burning'),
 ('the lampstand\'s dropped spec verses: the lighting and the pattern', menorah('run_dropped'), ['25:37', '25:40']),
 ('Num 8:4 — the pattern clause\'s Numbers seat', menorah('pattern_numbers'), 'Num 8:4'),
 # ---- THE CURTAINS (26:1-14; 36:8-19) ----
 ('Exod 26:1-2 — ten curtains, twenty-eight by four', curtains('linen'), (10, 28, 4)),
 ('ten times four = forty', curtains('linen_width'), 40),
 ('twenty boards times a cubit and a half = thirty', curtains('tabernacle_length'), 30),
 ('forty = thirty + ten: the linen covers the top and the back', curtains('covers_length_and_back'), True),
 ('twenty-eight = ten across + nine down each side', curtains('width_hang'), {'interior': 10, 'per_side': 9}),
 ('Shabbat 98b:6 — R. Nechemiah\'s cubit-thick boards: two cubits exposed', curtains('exposed', thickness='cubit_throughout'), 2),
 ('Shabbat 98b:6 — R. Yehuda\'s tapering boards: one cubit exposed', curtains('exposed', thickness='tapering'), 1),
 ('Exod 26:16 — no thickness in the ink', curtains('board_thickness_in_ink'), False),
 ('Exod 26:6 — fifty gold clasps', curtains('clasps'), (50, 'gold')),
 ('Exod 26:6 / 36:13 — and the tabernacle shall be ONE', curtains('one'), 'made_one'),
 ('"a woman to her sister" — the spec\'s idiom, five seats, none in the run', curtains('sister_idiom'), {'spec': 5, 'run': 0}),
 ('"one to one" — the run\'s phrase, five seats, none in the spec', curtains('one_to_one'), {'spec': 0, 'run': 5}),
 ('Exod 26:7-8 — eleven goat-hair curtains, thirty by four', curtains('goat'), (11, 30, 4)),
 ('forty-four minus forty: the doubled front and the back\'s hang', curtains('goat_extra'), {'front_doubled': 2, 'back_hang': 2}),
 ('thirty minus twenty-eight: the cubit on each side (26:13)', curtains('goat_width_extra'), 2),
 ('Exod 26:11 — fifty bronze clasps', curtains('goat_clasps'), (50, 'bronze')),
 ('Exod 26:14 — two coverings', curtains('covers'), ['ram_skins_red', 'tachash']),
 ('Onkelos + Tanchuma Terumah 6 — the tachash, three readings', curtains('tachash'), {'Onkelos': 'a_name_sasgona', 'R_Yehuda': 'real_beast_one_horn', 'R_Nechemiah': 'miracle_for_the_hour'}),
 ('Yoma 72b:18-19 — designer two faces, embroiderer one', curtains('designer_vs_embroiderer'), 'choshev_two_faces_rokem_one'),
 ('Onkelos — two craft grades', curtains('craft_grades'), 'inner_master_outer_embroiderer'),
 ('the curtains\' dropped spec verses: the two overhang clauses', curtains('run_dropped'), ['26:12', '26:13']),
 ('Exod 36:8 — all the wise-hearted made', curtains('run_subject'), 'all_the_wise_hearted'),
 ('Tanchuma Terumah 9 — the contained voice', curtains('goat_hair_descent'), 'contained_voice'),
 # ---- THE BOARDS (26:15-30; 36:20-34) ----
 ('Exod 26:16 — ten by a cubit and a half', boards('board'), (10, 1.5)),
 ('Sukkah 45b (F-034) — standing: the way they grow', boards('standing'), 'as_they_grow'),
 ('Exod 26:18-23 — twenty, twenty, six, two', boards('counts'), {'south': 20, 'north': 20, 'west': 6, 'corners': 2}),
 ('Exod 26:19-25 — ninety-six silver sockets under the boards', boards('sockets_boards'), 96),
 ('with the veil\'s four: a hundred = 38:27\'s hundred talents', boards('sockets_total'), 100),
 ('Exod 26:24 — twins below, whole at the top', boards('corner_boards'), 'twins_below_whole_at_top'),
 ('Shabbat 98b:2 — the taper fork', boards('taper_fork'), {'R_Yehuda': 'fingerbreadth_at_top', 'R_Nechemiah': 'cubit_throughout'}),
 ('Exod 26:26-27 — fifteen bars', boards('bars'), 15),
 ('Shabbat 98b:5 — the middle bar stood by miracle', boards('middle_bar_miracle'), 'stood_by_miracle'),
 ('Tanchuma Terumah 9 — the middle bar in Jacob\'s hand', boards('middle_bar_provenance'), 'jacobs_hand_to_egypt'),
 ('Exod 26:29 — boards, rings, bars overlaid', boards('gold'), 'boards_rings_bars_overlaid'),
 ('the interior thirty by ten by ten', boards('interior'), {'length': 30, 'width': 10, 'height': 10}),
 ('Exod 26:30 — according to its fashion (two Tanakh seats)', boards('raise'), 'kemishpato'),
 ('Onkelos Exod 26:30 — according to its halakhah', boards('its_halakhah'), 'according_to_its_halakhah'),
 ('Tanchuma Vayakhel 9:1 — the fruit-tree rule at the boards', boards('fruit_tree_rule'), 'non_fruit_acacia'),
 ('Tanchuma Vayakhel 9:2 — tabernacle as pledge', boards('pledge'), 'mishkan_mashkon'),
 ('the boards\' dropped spec verse: the raising', boards('run_dropped'), ['26:30']),
 # ---- THE VEIL AND THE SCREEN (26:31-37; 36:35-38) ----
 ('Exod 26:31-32 — four colors, designer, cherubim; four pillars on silver', veil('veil_spec'), ('four_colors', 'designer', 'cherubim')),
 ('Exod 26:33 — under the clasps', veil('position'), 'under_the_clasps'),
 ('five curtains times four: the veil at twenty', veil('veil_at'), 20),
 ('the Holy of Holies a cube of ten', veil('holy_of_holies'), (10, 10, 10)),
 ('the Holy twenty by ten by ten', veil('holy'), (20, 10, 10)),
 ('1 Kgs 6 — Solomon doubles the tabernacle', veil('solomon_double'), {'house': (60, 20, 30), 'heikhal': 40, 'debir': (20, 20, 20)}),
 ('Mishnah Middot 4:7 — forty, the cubit partition, twenty (data)', veil('sheet_plan'), {'heikhal': 40, 'traksin': 1, 'holy_of_holies': 20}),
 ('Exod 26:33 — and the veil shall divide (a hapax phrase)', veil('divides'), 'veil_divides'),
 ('Mishnah Yoma 5:1 — two curtains / R. Yosei one, quoting 26:33', veil('one_or_two'), {'Mishnah': 'two_a_cubit_apart', 'R_Yosei': 'one_from_26_33'}),
 ('Yoma 51b:5-6 — the second Temple\'s doubt over the cubit partition', veil('second_temple_reason'), 'cubit_partition_status_doubtful'),
 ('Mishnah Kelim 1:6-9 — ten sanctities', veil('ladder'), 10),
 ('the spec builds three rungs: court, Holy, Holy of Holies', veil('spec_rungs'), 3),
 ('Exod 26:34-35 — the floor plan', veil('floor_plan'), {'ark': 'holy_of_holies', 'table': 'north', 'menorah': 'south'}),
 ('the lampstand\'s position by call; Tanchuma Tetzaveh 2', veil('lamp_not_needed'), 'nearer_the_veil_than_the_entrance'),
 ('Exod 26:36-37 — the screen: five pillars, bronze sockets, embroiderer', veil('screen'), (5, 'bronze_sockets', 'embroiderer')),
 ('Exod 36:38 — the run adds the pillars\' heads and bands', veil('run_adds_heads'), True),
 ('the veil block\'s dropped spec verses: the placements, and 26:37 by its additions', veil('run_dropped'), ['26:33', '26:34', '26:35', '26:37']),
 # ---- THE ALTAR (27:1-8; 38:1-7) ----
 ('Exod 27:1 — five by five by three, square', altar('dimensions'), (5, 5, 3)),
 ('"square" at six Torah seats', altar('square'), 6),
 ('Exod 38:1 — the run names it "of the burnt offering"; first at 30:28', altar('run_names_it'), 'altar_of_the_burnt_offering'),
 ('Exod 27:2 — the horns from it', altar('horns'), 'from_it'),
 ('Exod 27:3 — five vessel kinds, at spec and run', altar('vessels'), 5),
 ('Onkelos Exod 27:3 — the ash removal named', altar('ash_duty'), 'ash_removal_named_in_the_vessel_list'),
 ('Mishnah Eruvin 10:15 — the pot\'s second service', altar('pot_second_service'), 'psakhter_over_the_creeping_thing'),
 ('Exod 27:5 — the net to the half', altar('net'), 'to_the_half'),
 ('Zevachim 53a:9 — the Torah gave the partition', altar('red_line'), 'the_torah_gave_the_partition'),
 ('Mishnah Middot 3:1 — the crimson thread at the middle', altar('red_line_sheet'), 'crimson_thread_at_the_middle'),
 ('the upper bloods by call: the sin offering\'s horns', altar('upper_bloods'), 'outer_altar_horns'),
 ('the lower bloods by call: two that are four', altar('lower_bloods'), 'two_that_are_four'),
 ('the base: never in the spec, named by its use', altar('base'), 'not_in_the_spec'),
 ('Mishnah Middot 3:1 — the base\'s extent', altar('base_extent'), 'north_west_whole_south_east_one_cubit'),
 ('Mishnah Yoma 5:6 — the remainders on the western and southern base', altar('remainders'), {'inner': 'western_base', 'outer': 'southern_base'}),
 ('Zevachim 62a:8 — corner, ramp, base, square indispensable', altar('indispensables'), ['corner', 'ramp', 'base', 'square']),
 ('the ramp by call (Exod 20:26 at E1)', altar('ramp'), 'a ramp; and temperance beside it'),
 ('Exod 27:8 / 38:7 — hollow of boards', altar('hollow'), 'navuv_luchot'),
 ('the earth altar by call: the hollow box filled', altar('earth_fill'), 'attached_to_the_ground'),
 ('the hewn ban by call: the land\'s stone altar', altar('hewn_ban'), 'iron-touched stone disqualified'),
 ('the perpetual fire by call (Lev 6:6)', altar('perpetual_fire'), 'a standing never-extinguish duty'),
 ('Tanchuma Terumah 11 — the wood under the bronze', altar('fire_objection'), 'wood_under_bronze_answered'),
 ('Zevachim 59b:4-8 — the width and height fork', altar('height_fork'), {'R_Yehuda': (10, 10, 3), 'R_Yosei': (5, 5, 10)}),
 ('Zevachim 59b:9-10 — the court\'s five and the priest seen', altar('height_objection'), 'priest_seen_from_outside'),
 ('Zevachim 60a:1-2 — the three re-read from the surround', altar('three_reread'), 'from_the_surround_upward'),
 ('Mishnah Middot 3:1 — thirty-two (data)', altar('sheet_altar'), 32),
 ('2 Chr 4:1 — Solomon\'s bronze altar twenty by twenty by ten', altar('solomon_altar'), (20, 20, 10)),
 ('the tabernacle\'s altar acacia and bronze, not stone', altar('tabernacle_material'), 'acacia_bronze_not_stone'),
 ('Tanchuma Terumah 10 — the acrostic', altar('acrostic'), 'pardon_merit_blessing_life'),
 ('the altar\'s dropped spec verses: grammar artifacts and the pointer', altar('run_dropped'), ['27:3', '27:4', '27:5', '27:8']),
 # ---- THE COURT (27:9-19; 38:9-20) ----
 ('Exod 27:18 — a hundred by fifty by five', court('dimensions'), (100, 50, 5)),
 ('the hangings: two hundred and eighty cubits', court('hangings'), 280),
 ('with the screen three hundred = the perimeter', court('perimeter_closes'), True),
 ('Exod 27:13-16 — fifteen, twenty, fifteen', court('east'), (15, 20, 15)),
 ('sixty pillars on sixty bronze sockets', court('pillars'), 60),
 ('Exod 27:10, 17 — hooks and bands silver', court('silver'), 'hooks_and_bands'),
 ('Exod 38:17, 19 — the run adds the silver heads (38:28 confirms)', court('run_adds_silver_heads'), True),
 ('Exod 27:16 / 38:18 — the gate screen twenty, five high', court('gate_screen'), (20, 5, 'embroiderer')),
 ('Zevachim 60a:1 — R. Yosei reads 38:18\'s five above the altar', court('court_height_read'), 'five_above_the_altar'),
 ('"hangings" at fourteen Torah seats', court('hangings_word'), 14),
 ('Mishnah Makkot 3:3 — outside the hangings, forty lashes', court('outside_the_curtains'), 'forty_lashes_most_holy'),
 ('a hundred by fifty = five thousand', court('area'), 5000),
 ('the square root: seventy and a remainder', court('two_seah'), 70),
 ('Mishnah Eruvin 2:5 — R. Yosei: length double the width', court('two_seah_sheet'), 'R_Yosei_length_double_width'),
 ('Exod 27:19 — the pegs bronze', court('pegs'), 'bronze'),
 ('Mishnah Middot 2:1, 5:1 — the descendant enclosures (data)', court('descendant'), {'temple_mount': 500, 'whole_court': (187, 135)}),
 ('the court\'s dropped spec verses: the run\'s reorganized summary', court('run_dropped'), ['27:15', '27:17', '27:18', '27:19']),
 # ---- THE LAMP'S OIL (27:20-21) ----
 ('Lev 24:2 = Exod 27:20 — thirteen tokens', lamp('tail_identity'), 13),
 ('the identity by call from the law\'s seat', lamp('restatement'), 13),
 ('Exod 27:20 — "and you shall command"', lamp('opening_verb'), 'you_shall_command'),
 ('Mishnah Menachot 8:4 by call — the first of each olive', lamp('oil'), 'the_first_of_each'),
 ('Mishnah Menachot 8:5 by call — the nine grades', lamp('nine_grades'), ['1of1', '2of1=1of2', '3of1=2of2=1of3', '3of2=2of3', '3of3']),
 ('Mishnah Menachot 8:5 — crushed for the light, not for the meal offerings', lamp('crushed_for_light'), 'not_for_meal_offerings'),
 ('Exod 27:21 by call — evening to morning', lamp('evening_to_morning'), 'enough_to_burn_evening_to_morning'),
 ('Exod 27:21 vs Lev 24:3 — Aaron and his sons; the sons dropped', lamp('staffing'), 'one_priest_arranges_seven_lamps'),
 ('Exod 27:21 — an everlasting statute', lamp('everlasting'), 'chukat_olam_ledorotam'),
 ('Tanchuma Tetzaveh 2 — not that I need its light', lamp('not_need'), 'windows_inverted_light_flows_out'),
 ('no run of the oil in the span', lamp('run_in_span'), 0),
 # ---- THE ACCOUNTS (38:21-31) ----
 ('"these are the accounts" at seven seats', books('formula'), 7),
 ('Exod 38:21 — Moses and Ithamar', books('two_signatories'), ['moses', 'ithamar']),
 ('Mishnah Shekalim 5:2 — no authority in money under two', books('rule'), 'no_authority_in_money_under_two'),
 ('Tanchuma Pekudei 5:2 — the exemption declined', books('exemption_declined'), 'reckons_through_others'),
 ('Mishnah Shekalim 3:2 — the collector\'s dress', books('dress'), 'no_hemmed_cloak'),
 ('Tanchuma Pekudei 7:4 — why audit: the scoffers', books('why_audit'), 'the_scoffers'),
 ('Tanchuma Pekudei 7:3 — the missing 1,775 found on the hooks', books('missing_1775'), 'found_on_the_hooks'),
 ('no stamp in 36-38; fourteen in 39-40', books('stamp_absent'), 0),
 ('Exod 38:24 — gold twenty-nine talents, seven hundred and thirty', books('gold'), (29, 730)),
 ('Exod 38:25 — silver a hundred talents, 1,775', books('silver'), (100, 1775)),
 ('Exod 38:26 — 603,550 (= Num 1:46)', books('census'), 603550),
 ('"beka" at two Torah seats', books('beka'), 2),
 ('THE TALENT COMPUTED: three thousand shekels', books('talent'), 3000),
 ('the books balance', books('talent_check'), True),
 ('Exod 38:27 — a hundred sockets = the spec\'s 96 + 4', books('sockets'), 100),
 ('Exod 38:28 — 1,775 to the hooks, heads, bands', books('hooks'), 1775),
 ('Exod 38:29 — bronze seventy talents, 2,400', books('bronze'), (70, 2400)),
 ('2,400 / 25 = ninety-six maneh', books('bronze_maneh'), 96),
 ('Bekhorot 5a:18 — the sanctuary maneh double', books('double_maneh'), 'sanctuary_maneh_double'),
 ('Exod 38:30-31 — eight bronze objects', books('bronze_items'), 8),
 ('"by the sanctuary shekel" three times in the accounts', books('sanctuary_shekel'), 3),
 ('Onkelos Exod 38:24-26 — selaim of the sanctuary', books('conversion_layer'), 'selaim_of_the_sanctuary'),
 ('Tanchuma Vayakhel 4:5 — Oholiab of Dan named for praise', books('oholiab'), 'dan_named_for_praise'),
 ('Exod 38:8 — the mirrors, two tracks', books('mirrors'), {'Onkelos': 'praying_women', 'Tanchuma': 'mirrors_of_desire_accepted'}),
 ('the assembling women at two seats, two spellings', books('assembling_women'), {'defective': 'Exod 38:8', 'plene': '1Sam 2:22'}),
 ('the run\'s E4 tokens — OWED', books('e4_owed'), ['הקטרת', 'המשחה', 'קטרת', 'הכיור']),
 ('Tanchuma Pekudei 2:3 — the seven days mapped', books('creation_map'), 7),
 # ---- THE SCENE ----
 ('the spec\'s order: vessels, then house', build('spec_order'), ['ark', 'table', 'menorah', 'curtains', 'boards', 'veil', 'screen', 'altar', 'court']),
 ('the run\'s order: house, then vessels', build('run_order'), ['curtains', 'boards', 'veil', 'screen', 'ark', 'table', 'menorah', 'incense_altar', 'anointing_oil', 'altar', 'laver', 'court']),
 ('the reversal', build('house_first'), ('vessels_first', 'house_first')),
 ('Berakhot 55a:12 vs Tanchuma Vayakhel 6:5 — the order fork', build('order_fork'), {'Berakhot_55a': 'gods_order_house_first_moses_reversed', 'Tanchuma_Vayakhel_6_5': 'bezalel_ark_first_moses_house_first'}),
 ('move M-22 — the run restores the spec\'s order', build('run_teaches_spec'), 'the_order_restored'),
 ('the alignment engine\'s totals', build('alignment'), (89, 74, 65, 67, 24)),
 ('the twenty-four dropped spec verses', build('dropped'), ['25:15', '25:16', '25:21', '25:22', '25:30', '25:37', '25:40', '26:12', '26:13', '26:30', '26:33', '26:34', '26:35', '26:37', '27:3', '27:4', '27:5', '27:8', '27:15', '27:17', '27:18', '27:19', '27:20', '27:21']),
 ('what the run drops: the use clauses and the pattern', build('dropped_kinds'), 'use_clauses_and_the_pattern'),
 ('the blocks whose numerals match exactly', build('numerals_equal'), ['table', 'veil_screen']),
 ('the verbs: thirty "you shall make", two "they shall make", thirty-seven "and he made", one named', build('verbs'), {'spec_you_shall_make': 30, 'spec_they_shall_make': 2, 'run_and_he_made': 37, 'run_named_makers': 1}),
 ('the metal-tokens spec vs run', build('metals'), {'gold': (25, 30), 'silver': (9, 15), 'bronze': (13, 18)}),
 ('the token counts', build('tokens'), (1182, 1362)),
 ('THE SCENE on the world engine', build('world'), (2, 1, 1, 1, 1, 1, 1, 0, 0, 17)),
 ('THE W6 SCENE — the altar\'s fire duty, the overflow consumed', build('world_w6'), (1, 1, 17)),
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
print('effects: every cell carries REGISTERED effects — NINE discovered in these verses\' own verbs: set_apart_before_me, surplus_to_the_house (TRANSFER), '
      'presence_dwells, meeting_appointed (HEAVEN — promised, unfired), staves_fixed, bringing_halted (BLOCK), made_one, veil_divides, accounts_rendered (STATUS) [effects law satisfied]')
print('SCENE: %r — the offering, the halt, the vessels, the accounts; the two promises unfired' % (SCENE,))
print('SCENE (W6): %r — the altar\'s fire duty, the overflow consumed' % (SCENE_W6,))
print('WATCH COVERAGE (the construction):')
_W.print_coverage()
if ok == n:
    print('THE SANCTUARY RUNS AGAINST ITS SPEC — the house built before the ark against the ark-first command, the fork recorded at Berakhot 55a; every use-clause and '
          'pattern-clause dropped by the run; the spec\'s counts summing to the accounts\' hundred sockets; the talent computed at three thousand shekels; the '
          'silver heads the run adds; "one to one" for "a woman to her sister"; the altar named by its use only in the run, its base by Leviticus alone; the '
          'offerings, sin-offering, Tzav, priesthood, and ordinances engines CALLED.')
else:
    print('MISSES (%d):' % len(misses))
    for m_ in misses: print('  -', m_[0][:80], '->', m_[1])
    sys.exit('MISSES REMAIN — consult the Talmud per gap and recompile.')

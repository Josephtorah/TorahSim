#!/usr/bin/env python3
"""cold_run_vestments.py — THE VESTMENTS' SPEC GRADED AGAINST ITS OWN RUN
(Exod 28:1-43 the SPEC; Exod 39:1-43 the RUN — 2026-09-06, sitting E3 of THE COMPILE DEBT,
World/step9/COMPILE_DEBT.md; the sixth runner compiled under THE DEPENDENCY GATE's rule: span
declared, a stub placed, the census run — it required NO type edge (the span names no offering
type) and EIGHT pointers (the run's stamp 'as the LORD commanded Moses' at seven verses and an
eighth without 'Moses' at the inspection), every one dispositioned RUN_CITATION before the first
cell; the run's Exod 30 inventory at 39:38-39 declared OWED to E4; four edges declared for the
live calls the compile makes.)

The form: DEMONSTRATE-BY-RUN inside one book (the E2 shape). Exod 28 is the SPEC — the office,
the ephod with its two stones, the breastplate of judgment with the Urim and Tummim, the robe with
its bells, the plate, the tunic, turban and sash, the sons' four, the investiture verse, the
breeches and the wear-or-die statute; Exod 39 is the RUN — the garments made in the run's own
order, the work completed, the delivery manifest, the inspection and the blessing. The runner
compiles the spec from its ink (every count the ink states computed, every count it does not —
the thread, the bells, the span — a PARAMETER whose recorded settings the sheet and the opened
segments supply) and grades the run as a SCENE against it: each run verse aligned to its spec
verse by token, the ORDER of the making against the order of the command (the plate moves from
fourth to last), the verses the run DROPS (every Presence-clause — 'before the LORD' stands at
five seats of the spec and none of the run — every function clause, the sound, the death, the
investiture), the tokens the run ADDS ('twined' at three garments, a second 'doubled', the
process verse 39:3 with four hapaxes, the writing verb on the plate, the sash's materials), and
THE HEADLINE: THE RUN'S ADDED TOKENS ARE THE SPEC'S PARAMETERS — the tradition derives the
sixfold thread from the run's five 'fine linen' tokens (39:27-28), the twined eight from the run's
added 'twined' (39:24), the gold thread's count from the run's added process verse (39:3): Yoma
71b-72a runs on Exod 39, not Exod 28 — move M-22 in a third form (at D8 a column, at E2 the
order, here the PARAMETER), and the derivation itself is a homograph read: the material-word
שש ('fine linen') IS the numeral שש ('six').

Answer sheet ROUTED BY TOPIC under the union rule: Mishnah Yoma 7 WHOLE (the Day's two garment
sets, the immersions, THE EIGHT AND THE FOUR), Zevachim 2 WHOLE (the disqualified receivers —
one lacking garments — and the piggul rows) + thirteen topic rows + the five link rows outside —
28 rows, the ledger logic/oral_triage/vestments_docket_2026-09-06.md with its coverage computed;
61 Talmud addresses indexed on the span, 46 opened PER GAP (the looms, the atonement table, the
collectors in twos, the homographs, the writing, the lashes, the whole-body entry, the plate's
scope), 10 credited from the vestments block of round 27.

The five motions, in order:
 (1) code from the BARE INK — the censuses below ('to serve Me as priest' at three seats; 'for
     honor and for splendor' at two; the six nouns of 28:4 plus the plate and the breeches = eight;
     the four sons' garments; the gold-bearing blocks = the four the high priest adds; 'in their
     birth order' a hapax; signet engravings at six seats — three objects, spec and run; the
     breastplate-word's seventeen seats all in the sanctuary chapters; the Urim's five seats with
     the Psalm's lights, the Tummim's three with 'whole' at forty-seven; 'shall not be detached'
     at two seats; 'shall not be torn' at two; 'its sound shall be heard' a hapax; the plate-word
     the flower's word; 'holy to the LORD' at sixteen seats with the horses' bells; the forehead
     with Goliath's; the twelve stone-names, four of them homographs of common words, nine of
     them in Ezekiel's Eden; the run's three singular 'and he made' against eleven plural; the
     stamp at seven plus one; the process verse's four hapaxes; 'fine linen' twice in the spec's
     tunic verse and five times in the run's; the completion verb of Genesis 2; the blessing verb
     of Genesis 1) — every quantity the ink does not state a PARAMETER (the thread count, the
     bells, the span, the stones' engraver, the garments' price);
 (2) the Mishnah's rows as TEST DATA, each expected value a literal typed from the row (the
     honest-pairing guard runs first);
 (3) run;
 (4) misses filled by NAMED recorded arguments — the Onkelos and Tanchuma rows (the unit's
     substitute spine, verdicted 2026-09-01/02), the vestments block's 60 segments (credited),
     and the 46 opened per gap this sitting;
 (5) the graded matrix with per-cell provenance, fractions, EFFECTS — and the SCENE on the world
     engine: the garments made, the work completed, the delivery, the inspection, the blessing;
     the four USE entries the spec promises (the names borne, the judgment borne, the entry
     announced, the plate propitiating) left UNFIRED — the run makes and never wears; the
     investiture (E4, Lev 8) fires them.

Cross-span receipts, labeled [IMPORT] and CALLED (the edges dispositioned in
dependency_dispositions.yaml): cold_run_sanctuary_build.ark/table/menorah/court (the delivery
manifest's vessels at their spec — the staves in the ark's manifest line, the bread, the lamps,
the hangings); cold_run_priesthood.family (the many-garmented high priest at Lev 21:10's 'crown
of the oil'; the rending's geometry) and lamp_table (the lamps of the arrangement);
cold_run_ordinances.altar (the nakedness clause of 20:26 the breeches answer); cold_run_yoma
.service_order (the linen donned at 16:4, the relocated stripping at 16:23). Lev 8:7-9, 8:13,
16:4, 21:10, Exod 29:5-9, Num 27:21, Deut 33:8, Ezek 28:13, 44:17-18, Zech 14:20, Gen 3:21,
37:31, 1 Sam 14:41, Ezra 2:63 stay imports by name. The anointing oil, the incense, and the
laver of the manifest (39:38-39) are E4's: OWED, on the gate's worklist.
"""
import os as _os
_ROOT = _os.path.normpath(_os.path.join(_os.path.dirname(_os.path.abspath(__file__)), '..', '..'))   # THE PORTABLE REPO (2026-09-15): the repo root from this file's own place
import sqlite3, sys, os, json, io, contextlib, collections
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import effects_layer as FX
from compile_guards import check_honest_pairing
GUARDED = check_honest_pairing(os.path.abspath(__file__))
assert GUARDED == 196, ("the guard counted %d expectations, the tripwire holds 196" % GUARDED)

DB = (_ROOT + '/Data/tanakh.sqlite')
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

SPEC = [(28, v) for v in range(1, 44)]
RUN = [(39, v) for v in range(1, 44)]
def seats(pred, rng):
    return [k for k in rng if pred(toks('Exod', k[0], k[1]))]
def has(*ws):
    return lambda t: any(t[i:i + len(ws)] == list(ws) for i in range(len(t) - len(ws) + 1))
def anytok(*ws):
    return lambda t: any(w in t for w in ws)
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
def tanakh_any(*toks_):
    return sorted(set(k for t in toks_ for k in _ALL.get(t, [])))
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
    ('bring near Aaron your brother TO SERVE ME AS PRIEST',   'Exod', 28, 1, 'לכהנו'),
    ('holy garments FOR HONOR and for splendor',              'Exod', 28, 2, 'לכבוד'),
    ('all the WISE OF HEART whom I have filled',              'Exod', 28, 3, 'חכמי'),
    ('these are the garments: a BREASTPLATE',                 'Exod', 28, 4, 'חשן'),
    ('the EPHOD of gold, blue, purple',                       'Exod', 28, 6, 'האפד'),
    ('two ONYX stones',                                       'Exod', 28, 9, 'שהם'),
    ('IN THE ORDER OF THEIR BIRTH',                           'Exod', 28, 10, 'כתולדתם'),
    ('SIGNET engravings',                                     'Exod', 28, 11, 'חתם'),
    ('stones of REMEMBRANCE',                                 'Exod', 28, 12, 'זכרן'),
    ('a breastplate of JUDGMENT',                             'Exod', 28, 15, 'משפט'),
    ('SQUARE, doubled, a SPAN',                               'Exod', 28, 16, 'זרת'),
    ('four ROWS of stone',                                    'Exod', 28, 17, 'טורים'),
    ('twelve, each on his name, for the twelve TRIBES',       'Exod', 28, 21, 'שבט'),
    ('it shall NOT BE DETACHED',                              'Exod', 28, 28, 'יזח'),
    ('the URIM and the Tummim',                               'Exod', 28, 30, 'האורים'),
    ('the robe WHOLLY blue',                                  'Exod', 28, 31, 'כליל'),
    ('like the mouth of a COAT OF MAIL, not torn',            'Exod', 28, 32, 'תחרא'),
    ('a golden BELL and a pomegranate',                       'Exod', 28, 34, 'פעמן'),
    ('and its SOUND shall be heard',                          'Exod', 28, 35, 'קולו'),
    ('a PLATE of pure gold',                                  'Exod', 28, 36, 'ציץ'),
    ('on the FOREHEAD of Aaron',                              'Exod', 28, 38, 'מצח'),
    ('the CHECKERED tunic',                                   'Exod', 28, 39, 'ושבצת'),
    ('CAPS for honor and splendor',                           'Exod', 28, 40, 'ומגבעות'),
    ('and you shall FILL THEIR HAND',                         'Exod', 28, 41, 'ומלאת'),
    ('linen BREECHES to cover the flesh of nakedness',        'Exod', 28, 42, 'ערוה'),
    ('an EVERLASTING statute for him and his seed',           'Exod', 28, 43, 'חקת'),
    ('garments of SERAD for serving in the Holy',             'Exod', 39, 1, 'שרד'),
    ('they BEAT the gold plates and cut threads',             'Exod', 39, 3, 'וירקעו'),
    ('the ephod band IS of it',                               'Exod', 39, 5, 'הוא'),
    ('square, DOUBLED... doubled',                            'Exod', 39, 9, 'כפול'),
    ('the pomegranates TWINED',                               'Exod', 39, 24, 'משזר'),
    ('the ornamental CAPS of fine linen',                     'Exod', 39, 28, 'פארי'),
    ('the plate, THE HOLY CROWN — they WROTE on it',          'Exod', 39, 30, 'ויכתבו'),
    ('and all the work was COMPLETED',                        'Exod', 39, 32, 'ותכל'),
    ('and they BROUGHT the tabernacle to Moses',              'Exod', 39, 33, 'ויביאו'),
    ('the lamps of the ARRANGEMENT',                          'Exod', 39, 37, 'המערכה'),
    ('and Moses SAW all the work',                            'Exod', 39, 43, 'וירא'),
    ('and Moses BLESSED them',                                'Exod', 39, 43, 'ויברך'),
]
fired = 0
for label, book, ch, vs, tok in PROBES:
    if tok in toks(book, ch, vs): fired += 1
    else: print('PROBE FAILED: %s (%s %d:%d lacks %s)' % (label, book, ch, vs, tok))
if fired != len(PROBES):
    sys.exit('zero-report law: the ink scan is not trusted until every probe fires')
print('probes: %d/%d fired (the ink scan is trusted; the whole-Tanakh census holds %d verses)' % (len(PROBES), len(PROBES), N_VERSES))

# ---- the censuses (TRIPWIRES — each a measured literal) ------------
c_lekhahano = tanakh_phrase(['לכהנו', 'לי']);                     assert c_lekhahano == [('Exod', 28, 1), ('Exod', 28, 3), ('Exod', 28, 4)], c_lekhahano
c_priest_verb = seats(anytok('לכהנו', 'וכהנו', 'לכהן'), SPEC + RUN); assert c_priest_verb == [(28, 1), (28, 3), (28, 4), (28, 41), (39, 41)], c_priest_verb
c_sons = toks('Exod', 28, 1)[-6:-2];                               assert c_sons == ['נדב', 'ואביהוא', 'אלעזר', 'ואיתמר'], c_sons
c_lev10 = [k for k, t in _VERSES.items() if k[0] == 'Lev' and k[1] == 10 and 'נדב' in t]; assert c_lev10 == [('Lev', 10, 1)], c_lev10
c_purpose = tanakh_phrase(['לכבוד', 'ולתפארת']);                  assert c_purpose == [('Exod', 28, 2), ('Exod', 28, 40)], c_purpose
c_six = toks('Exod', 28, 4)[4:11];                                assert c_six == ['חשן', 'ואפוד', 'ומעיל', 'וכתנת', 'תשבץ', 'מצנפת', 'ואבנט'], c_six
c_tashbetz = (tanakh('תשבץ'), tanakh('ושבצת'));                    assert c_tashbetz == ([('Exod', 28, 4)], [('Exod', 28, 39)]), c_tashbetz
c_bigdei_kodesh = tanakh_phrase(['בגדי', 'קדש']);                 assert c_bigdei_kodesh == [('Exod', 28, 2), ('Exod', 28, 4), ('Lev', 16, 4)], c_bigdei_kodesh
c_bigdei_hakodesh = tanakh_phrase(['בגדי', 'הקדש']);              assert c_bigdei_hakodesh == [('Exod', 31, 10), ('Exod', 35, 19), ('Exod', 39, 1), ('Exod', 39, 41), ('Exod', 40, 13), ('Lev', 16, 32)], c_bigdei_hakodesh
c_serad = tanakh_phrase(['בגדי', 'שרד']) + tanakh_phrase(['בגדי', 'השרד']); assert c_serad == [('Exod', 39, 1), ('Exod', 31, 10), ('Exod', 35, 19), ('Exod', 39, 41)], c_serad
c_choshev = tanakh_phrase(['מעשה', 'חשב']);                       assert len(c_choshev) == 8 and all(k[0] == 'Exod' for k in c_choshev), c_choshev
c_rokem = tanakh_phrase(['מעשה', 'רקם']);                         assert len(c_rokem) == 6 and (('Exod', 28, 39) in c_rokem) and (('Exod', 39, 29) in c_rokem), c_rokem
c_oreg = tanakh_phrase(['מעשה', 'ארג']);                          assert c_oreg == [('Exod', 28, 32), ('Exod', 39, 22), ('Exod', 39, 27)], c_oreg
c_avot = tanakh_phrase(['מעשה', 'עבת']);                          assert c_avot == [('Exod', 28, 14), ('Exod', 28, 22), ('Exod', 39, 15)], c_avot
c_toledot = tanakh('כתולדתם');                                    assert c_toledot == [('Exod', 28, 10)], c_toledot
c_pituchei = sorted(tanakh_phrase(['פתוחי', 'חתם']) + tanakh_phrase(['פתוחי', 'חותם'])); assert c_pituchei == [('Exod', 28, 11), ('Exod', 28, 21), ('Exod', 28, 36), ('Exod', 39, 6), ('Exod', 39, 14), ('Exod', 39, 30)], c_pituchei
c_cm = (tanakh_phrase(['חשן', 'משפט']), tanakh_phrase(['חשן', 'המשפט'])); assert c_cm == ([('Exod', 28, 15)], [('Exod', 28, 30)]), c_cm
c_cm29 = 'בחשן' in toks('Exod', 28, 29) and 'המשפט' in toks('Exod', 28, 29); assert c_cm29
c_choshen_all = tanakh_any('חשן', 'החשן');                         assert len(c_choshen_all) == 17 and all((k[0] == 'Exod' and 28 <= k[1] <= 39) or k == ('Lev', 8, 8) for k in c_choshen_all), c_choshen_all
c_urim = tanakh('האורים') + tanakh('אורים') + tanakh('באורים');    assert c_urim == [('Exod', 28, 30), ('Lev', 8, 8), ('Num', 27, 21), ('Ps', 136, 7), ('1Sam', 28, 6)], c_urim
c_tummim = tanakh('התמים');                                       assert c_tummim == [('Exod', 28, 30), ('Lev', 8, 8)], c_tummim
c_tummim_sam = 'תמים' in toks('1Sam', 14, 41);                      assert c_tummim_sam
c_tamim_n = len(tanakh('תמים'));                                  assert c_tamim_n == 47, c_tamim_n
c_yizach = tanakh('יזח');                                         assert c_yizach == [('Exod', 28, 28), ('Exod', 39, 21)], c_yizach
c_yikarea = tanakh_phrase(['לא', 'יקרע']);                        assert c_yikarea == [('Exod', 28, 32), ('Exod', 39, 23)], c_yikarea
c_tachra = tanakh('תחרא');                                        assert c_tachra == [('Exod', 28, 32), ('Exod', 39, 23)], c_tachra
c_kolo = tanakh_phrase(['ונשמע', 'קולו']);                        assert c_kolo == [('Exod', 28, 35)], c_kolo
c_uvtzeto = tanakh('ובצאתו');                                     assert c_uvtzeto == [('2Chr', 23, 7), ('Exod', 28, 35)], c_uvtzeto
c_lo_yamut = len(tanakh_phrase(['ולא', 'ימות']));                 assert c_lo_yamut == 8, c_lo_yamut
c_tzitz = tanakh('ציץ');                                          assert c_tzitz == [('Exod', 28, 36), ('Exod', 39, 30), ('Isa', 40, 7), ('Isa', 40, 8), ('Jer', 48, 9), ('Lev', 8, 9), ('Num', 17, 23)], c_tzitz
c_nezer = tanakh_phrase(['נזר', 'הקדש']);                         assert c_nezer == [('Exod', 29, 6), ('Exod', 39, 30), ('Lev', 8, 9)], c_nezer
c_kodesh_l = tanakh_phrase(['קדש', 'ליהוה']);                     assert len(c_kodesh_l) == 16 and ('Zech', 14, 20) in c_kodesh_l and ('Exod', 16, 23) in c_kodesh_l and ('Exod', 31, 15) in c_kodesh_l, c_kodesh_l
c_metzach = tanakh('מצח') + tanakh('מצחו');                       assert c_metzach == [('Exod', 28, 38), ('Ezek', 3, 7), ('1Sam', 17, 49), ('Exod', 28, 38)], c_metzach
c_leratzon = tanakh_phrase(['לרצון', 'להם']);                     assert c_leratzon == [('Exod', 28, 38)], c_leratzon
c_avon_h = tanakh_phrase(['עון', 'הקדשים']);                      assert c_avon_h == [('Exod', 28, 38)], c_avon_h
c_tamid = seats(anytok('תמיד'), SPEC + RUN);                       assert c_tamid == [(28, 29), (28, 30), (28, 38)], c_tamid
c_michnesei = tanakh_phrase(['מכנסי', 'בד']);                     assert c_michnesei == [('Exod', 28, 42)], c_michnesei
c_besar_ervah = tanakh_phrase(['בשר', 'ערוה']);                   assert c_besar_ervah == [('Exod', 28, 42)], c_besar_ervah
c_michnasayim = tanakh_any('מכנסי', 'מכנסים', 'ומכנסי', 'המכנסים'); assert c_michnasayim == [('Exod', 28, 42), ('Exod', 39, 28), ('Ezek', 44, 18), ('Lev', 6, 3), ('Lev', 16, 4)], c_michnasayim
c_ervah20 = 'ערותך' in toks('Exod', 20, 26);                      assert c_ervah20
c_chukat = tanakh_phrase(['חקת', 'עולם', 'לו', 'ולזרעו', 'אחריו']); assert c_chukat == [('Exod', 28, 43)], c_chukat
c_yisu = tanakh_phrase(['ולא', 'ישאו', 'עון']);                   assert c_yisu == [('Exod', 28, 43)], c_yisu
c_lev22_9 = toks('Lev', 22, 9)[3:9];                              assert c_lev22_9 == ['ולא', 'ישאו', 'עליו', 'חטא', 'ומתו', 'בו'], c_lev22_9
c_stamp7 = seats(has('כאשר', 'צוה', 'יהוה', 'את', 'משה'), RUN);    assert c_stamp7 == [(39, 1), (39, 5), (39, 7), (39, 21), (39, 26), (39, 29), (39, 31)], c_stamp7
c_stamp8 = seats(has('כאשר', 'צוה', 'יהוה'), RUN);                 assert c_stamp8 == c_stamp7 + [(39, 43)], c_stamp8
c_kekhol = seats(anytok('ככל'), RUN);                              assert c_kekhol == [(39, 32), (39, 42)], c_kekhol
c_stamp_spec = seats(anytok('צוה'), SPEC);                         assert c_stamp_spec == [], c_stamp_spec
c_stamp_39_40 = [k for k in tanakh_phrase(['כאשר', 'צוה', 'יהוה', 'את', 'משה']) if k[0] == 'Exod' and 39 <= k[1] <= 40]; assert len(c_stamp_39_40) == 14, c_stamp_39_40
c_vayaas = seats(anytok('ויעש'), RUN);                             assert c_vayaas == [(39, 2), (39, 8), (39, 22)], c_vayaas
c_vayaasu = seats(anytok('ויעשו'), RUN);                           assert c_vayaasu == [(39, 1), (39, 6), (39, 15), (39, 16), (39, 19), (39, 20), (39, 24), (39, 25), (39, 27), (39, 30), (39, 32)], c_vayaasu
c_veasita = seats(anytok('ועשית'), SPEC);                          assert len(c_veasita) == 12, c_veasita
c_veasu = seats(anytok('ועשו'), SPEC);                             assert c_veasu == [(28, 3), (28, 4), (28, 6)], c_veasu
c_taaseh = seats(anytok('תעשה'), SPEC);                            assert c_taaseh == [(28, 11), (28, 14), (28, 15), (28, 39), (28, 40)], c_taaseh
c_process = (tanakh('וירקעו'), tanakh('פחי'), tanakh('וקצץ'), tanakh('פתילם')); assert c_process == ([('Exod', 39, 3)], [('Exod', 39, 3)], [('Exod', 39, 3), ('Ps', 46, 10)], [('Exod', 39, 3)]), c_process
c_betokh = toks('Exod', 39, 3).count('בתוך') + toks('Exod', 39, 3).count('ובתוך'); assert c_betokh == 4, c_betokh
c_shoham = tanakh_any('שהם', 'השהם', 'ושהם');                      assert len(c_shoham) == 14 and ('Gen', 2, 12) in c_shoham and ('Ezek', 28, 13) in c_shoham, c_shoham
c_zeret = tanakh('זרת');                                          assert c_zeret == [('Exod', 28, 16), ('Exod', 39, 9), ('Ezek', 43, 13)], c_zeret
c_kaful = (toks('Exod', 28, 16).count('כפול'), toks('Exod', 39, 9).count('כפול')); assert c_kaful == (1, 2), c_kaful
c_ravua = torah('רבוע');                                          assert c_ravua == [('Exod', 27, 1), ('Exod', 28, 16), ('Exod', 30, 2), ('Exod', 37, 25), ('Exod', 38, 1), ('Exod', 39, 9)], c_ravua
STONES = ['אדם', 'פטדה', 'ברקת', 'נפך', 'ספיר', 'יהלם', 'לשם', 'שבו', 'אחלמה', 'תרשיש', 'שהם', 'ישפה']
c_names_spec = [w.lstrip('ו') for v in (17, 18, 19, 20) for w in toks('Exod', 28, v) if w.lstrip('ו') in STONES]
c_names_run = [w.lstrip('ו') for v in (10, 11, 12, 13) for w in toks('Exod', 39, v) if w.lstrip('ו') in STONES]
assert c_names_spec == STONES and c_names_run == STONES, (c_names_spec, c_names_run)
c_rows = [len([w for w in toks('Exod', 28, v) if w.lstrip('ו') in STONES]) for v in (17, 18, 19, 20)]; assert c_rows == [3, 3, 3, 3], c_rows
c_stone_seats = {s: len(tanakh_any(s, 'ו' + s, 'ה' + s)) for s in STONES}
assert c_stone_seats == {'אדם': 492, 'פטדה': 3, 'ברקת': 3, 'נפך': 3, 'ספיר': 9, 'יהלם': 3, 'לשם': 36, 'שבו': 54, 'אחלמה': 2, 'תרשיש': 25, 'שהם': 14, 'ישפה': 4}, c_stone_seats
c_ezek = set(w.lstrip('ו') for w in toks('Ezek', 28, 13)); c_ezek_in = [s for s in STONES if s in c_ezek]; c_ezek_out = [s for s in STONES if s not in c_ezek]
assert len(c_ezek_in) == 9 and c_ezek_out == ['לשם', 'שבו', 'אחלמה'], (c_ezek_in, c_ezek_out)
c_ish = tanakh_phrase(['איש', 'על', 'שמו']);                       assert c_ish == [('Exod', 28, 21), ('Exod', 39, 14)], c_ish
c_rings = (sum(1 for v in range(15, 31) for w in toks('Exod', 28, v) if 'טבע' in w), sum(1 for v in range(8, 22) for w in toks('Exod', 39, v) if 'טבע' in w)); assert c_rings == (7, 7), c_rings
c_leumat = tanakh_phrase(['לעמת', 'מחברתו']);                     assert c_leumat == [('Exod', 28, 27), ('Exod', 39, 20)], c_leumat
c_mimenu = (tanakh_phrase(['ממנו', 'יהיה']), tanakh_phrase(['ממנו', 'הוא'])); assert c_mimenu == ([('Exod', 28, 8)], [('Exod', 39, 5)]), c_mimenu
c_nasa = tanakh_phrase(['ונשא', 'אהרן']);                         assert c_nasa == [('Exod', 28, 12), ('Exod', 28, 29), ('Exod', 28, 30), ('Exod', 28, 38)], c_nasa
c_lifnei = (seats(has('לפני', 'יהוה'), SPEC), seats(has('לפני', 'יהוה'), RUN)); assert c_lifnei == ([(28, 12), (28, 29), (28, 30), (28, 35), (28, 38)], []), c_lifnei
c_kelil = tanakh_phrase(['כליל', 'תכלת']);                        assert c_kelil == [('Exod', 28, 31), ('Exod', 39, 22), ('Num', 4, 6)], c_kelil
c_bells = tanakh_any('פעמן', 'פעמני', 'ופעמני', 'הפעמנים');                  assert c_bells == [('Exod', 28, 33), ('Exod', 28, 34), ('Exod', 39, 25), ('Exod', 39, 26)], c_bells
c_alt = (phrase('Exod', 28, 34, ['פעמן', 'זהב', 'ורמון']), phrase('Exod', 39, 26, ['פעמן', 'ורמן'])); assert c_alt == (2, 2), c_alt
c_mashzar = (sum(1 for k in SPEC for w in toks('Exod', *k) if w == 'משזר'), sum(1 for k in RUN for w in toks('Exod', *k) if w == 'משזר')); assert c_mashzar == (3, 6), c_mashzar
c_mashzar_added = [k for k in ((39, 24), (39, 28), (39, 29)) if 'משזר' in toks('Exod', *k)]; assert c_mashzar_added == [(39, 24), (39, 28), (39, 29)], c_mashzar_added
c_mashzar_spec_absent = [k for k in ((28, 33), (28, 39), (28, 42)) if 'משזר' in toks('Exod', *k)]; assert c_mashzar_spec_absent == [], c_mashzar_spec_absent
c_shesh = (toks('Exod', 28, 39).count('שש'), sum(toks('Exod', 39, v).count('שש') for v in (27, 28, 29))); assert c_shesh == (2, 5), c_shesh
c_shesh_all = len(tanakh('שש'));                                  assert c_shesh_all == 102, c_shesh_all
c_migbaot = tanakh_any('מגבעות', 'מגבעת', 'המגבעת', 'ומגבעות');    assert len(c_migbaot) == 11 and [k for k in c_migbaot if k[0] in TORAH] == [('Exod', 28, 40), ('Exod', 29, 9), ('Exod', 39, 28), ('Lev', 8, 13), ('Num', 23, 9)], c_migbaot
c_paarei = (tanakh('פארי'), tanakh('פאר'));                        assert c_paarei == ([('Exod', 39, 28), ('Ezek', 44, 18)], [('Isa', 61, 3), ('Isa', 61, 10)]), c_paarei
c_avnet = tanakh_any('אבנט', 'ואבנט', 'האבנט', 'אבנטים', 'באבנט'); assert c_avnet == [('Exod', 28, 4), ('Exod', 28, 39), ('Exod', 28, 40), ('Exod', 29, 9), ('Exod', 39, 29), ('Lev', 8, 7), ('Lev', 8, 13)], c_avnet
c_mitznefet = tanakh_any('מצנפת', 'המצנפת', 'ומצנפת', 'והמצנפת', 'ובמצנפת'); assert len(c_mitznefet) == 9 and ('Ezek', 21, 31) in c_mitznefet and ('Lev', 16, 4) in c_mitznefet, c_mitznefet
c_meil_n = len(tanakh_any('מעיל', 'המעיל', 'ומעיל', 'מעילו', 'מעילים', 'במעיל')); assert c_meil_n == 18, c_meil_n
c_efod_n = len(tanakh_any('אפד', 'אפוד', 'האפד', 'האפוד', 'ואפוד', 'לאפד', 'לאפוד', 'באפוד')); assert c_efod_n == 40, c_efod_n
c_efod_bad = tanakh_phrase(['אפוד', 'בד']);                       assert c_efod_bad == [('1Chr', 15, 27), ('1Sam', 2, 18), ('1Sam', 22, 18), ('2Sam', 6, 14)], c_efod_bad
c_efod_torah = [k for k in tanakh_any('אפד', 'אפוד', 'האפד', 'האפוד', 'ואפוד', 'לאפד', 'לאפוד', 'באפוד') if k[0] in TORAH and k[1] not in (28, 39)]
assert c_efod_torah == [('Exod', 25, 7), ('Exod', 29, 5), ('Exod', 35, 9), ('Exod', 35, 27), ('Lev', 8, 7), ('Num', 34, 23)], c_efod_torah
c_kutonet = [k for k in tanakh_any('כתנת', 'הכתנת', 'וכתנת', 'כתנות', 'כתנתו', 'הכתנות', 'בכתנת', 'ככתנת') if k[0] in TORAH]
assert len(c_kutonet) == 16 and ('Gen', 3, 21) in c_kutonet and ('Gen', 37, 31) in c_kutonet, c_kutonet
c_vayalbishem = tanakh('וילבשם');                                 assert c_vayalbishem == [('Gen', 3, 21), ('Lev', 8, 13)], c_vayalbishem
c_vehilbashta = tanakh('והלבשת');                                 assert c_vehilbashta == [('Exod', 28, 41), ('Exod', 29, 5), ('Exod', 40, 13), ('Exod', 40, 14)], c_vehilbashta
c_verbs41 = [w for w in toks('Exod', 28, 41) if w.startswith('ו') and len(w) > 4]; assert c_verbs41 == ['והלבשת', 'ומשחת', 'ומלאת', 'וקדשת', 'וכהנו'], c_verbs41
c_fill = (tanakh_phrase(['ומלאת', 'את', 'ידם']), tanakh_phrase(['ומלא', 'את', 'ידו'])); assert c_fill == ([('Exod', 28, 41)], [('Lev', 21, 10)]), c_fill
c_mashachta = tanakh_phrase(['ומשחת', 'אתם']);                    assert c_mashachta == [('Exod', 28, 41), ('Exod', 40, 15)], c_mashachta
c_kidashta = tanakh_phrase(['וקדשת', 'אתם']);                     assert c_kidashta == [('Exod', 28, 41), ('Exod', 30, 29), ('Exod', 30, 30)], c_kidashta
c_lev16 = (toks('Lev', 16, 4).count('בד'), toks('Lev', 6, 3).count('בד')); assert c_lev16 == (4, 2), c_lev16
c_lev21 = toks('Lev', 21, 10)[9:15];                              assert c_lev21 == ['ומלא', 'את', 'ידו', 'ללבש', 'את', 'הבגדים'], c_lev21
c_ezek44 = (toks('Ezek', 44, 18)[:2], toks('Ezek', 44, 18)[-3:]); assert c_ezek44 == (['פארי', 'פשתים'], ['לא', 'יחגרו', 'ביזע']), c_ezek44
c_vatekhel = tanakh('ותכל');                                      assert c_vatekhel == [('2Sam', 13, 39), ('Exod', 39, 32), ('Gen', 24, 19), ('Num', 17, 25)], c_vatekhel
c_vaykhal = tanakh('ויכל');                                       assert ('Gen', 2, 2) in c_vaykhal and ('Exod', 40, 33) in c_vaykhal and len(c_vaykhal) == 15, c_vaykhal
c_vaykhulu = tanakh('ויכלו');                                     assert ('Gen', 2, 1) in c_vaykhulu and len(c_vaykhulu) == 9, c_vaykhulu
c_kol_avodat = tanakh_phrase(['כל', 'עבדת', 'משכן']);             assert c_kol_avodat == [('Exod', 39, 32)], c_kol_avodat
c_vayaviu = tanakh_phrase(['ויביאו', 'את', 'המשכן']);             assert c_vayaviu == [('Exod', 39, 33)], c_vayaviu
c_manifest = [sum(1 for w in toks('Exod', 39, v) if w in ('את', 'ואת')) for v in range(33, 42)]; assert c_manifest == [3, 3, 3, 3, 4, 4, 6, 6, 3] and sum(c_manifest) == 35, c_manifest
c_nerot = tanakh_phrase(['נרת', 'המערכה']);                       assert c_nerot == [('Exod', 39, 37)], c_nerot
c_e4 = [(k, w) for k in RUN for w in toks('Exod', *k) if w in ('המשחה', 'הסמים', 'הכיר', 'קטרת')]; assert c_e4 == [((39, 38), 'המשחה'), ((39, 38), 'קטרת'), ((39, 38), 'הסמים'), ((39, 39), 'הכיר')], c_e4
c_vayar = tanakh_phrase(['וירא', 'משה']);                         assert c_vayar == [('Exod', 32, 25), ('Exod', 39, 43)], c_vayar
c_kol_melakhah = tanakh_phrase(['את', 'כל', 'המלאכה']);           assert c_kol_melakhah == [('1Kgs', 7, 40), ('Exod', 39, 43)], c_kol_melakhah
c_vehineh = tanakh_phrase(['והנה', 'עשו']);                       assert c_vehineh == [('Exod', 39, 43), ('Gen', 33, 1)], c_vehineh
c_vayvarekh = tanakh_phrase(['ויברך', 'אתם']);                    assert c_vayvarekh == [('Exod', 39, 43), ('Gen', 1, 22), ('Gen', 1, 28), ('Gen', 5, 2)], c_vayvarekh
c_vayvarekh_m = tanakh_phrase(['ויברך', 'אתם', 'משה']);           assert c_vayvarekh_m == [('Exod', 39, 43)], c_vayvarekh_m
c_ken_asu = len(tanakh_phrase(['כן', 'עשו']));                    assert c_ken_asu == 15, c_ken_asu
c_tokens = (sum(len(toks('Exod', *k)) for k in SPEC), sum(len(toks('Exod', *k)) for k in RUN)); assert c_tokens == (595, 568), c_tokens
c_gold = (sum(1 for k in SPEC for w in toks('Exod', *k) if 'זהב' in w), sum(1 for k in RUN for w in toks('Exod', *k) if 'זהב' in w)); assert c_gold == (17, 15), c_gold
c_tekhelet = (sum(1 for k in SPEC for w in toks('Exod', *k) if 'תכלת' in w), sum(1 for k in RUN for w in toks('Exod', *k) if 'תכלת' in w)); assert c_tekhelet == (8, 10), c_tekhelet
c_aharon = (sum(1 for k in SPEC for w in toks('Exod', *k) if 'אהרן' in w), sum(1 for k in RUN for w in toks('Exod', *k) if 'אהרן' in w)); assert c_aharon == (16, 3), c_aharon
c_shani = len([w for k in SPEC + RUN for w in toks('Exod', *k) if w in ('השני', 'השנית')]); assert c_shani == 6, c_shani
c_isa61 = toks('Isa', 61, 10)[13:16];                             assert c_isa61 == ['כחתן', 'יכהן', 'פאר'], c_isa61
c_zech = toks('Zech', 14, 20)[4:8];                               assert c_zech == ['מצלות', 'הסוס', 'קדש', 'ליהוה'], c_zech
c_gen3 = toks('Gen', 3, 21)[-3:];                                 assert c_gen3 == ['כתנות', 'עור', 'וילבשם'], c_gen3
print('censuses: "to serve Me as priest" %s · the six nouns of 28:4 %s · signet engravings %s · the breastplate-word %d seats · the Urim %s · the Tummim %s ("whole" %d) · '
      '"not detached" %s · "not torn" %s · the plate-word %s · "holy to the LORD" %d seats · the forehead %s · the twelve stones at %s seats each, %d in Ezekiel (missing %s) · '
      'the stamp %s + %s · "and he made" %s vs "and they made" %d · the process verse %s · "fine linen" spec/run %s · "twined" %s · "before the LORD" %s · '
      '"and he blessed them" %s · the manifest %s · tokens %s · gold %s'
      % (fmt(c_lekhahano), c_six, fmt(c_pituchei), len(c_choshen_all), fmt(c_urim), fmt(c_tummim), c_tamim_n, fmt(c_yizach), fmt(c_yikarea), fmt(c_tzitz), len(c_kodesh_l),
         fmt(c_metzach), c_stone_seats, len(c_ezek_in), c_ezek_out, fmt3(c_stamp7), fmt3(c_stamp8[-1:]), fmt3(c_vayaas), len(c_vayaasu), c_process, c_shesh, c_mashzar, c_lifnei,
         fmt(c_vayvarekh), c_manifest, c_tokens, c_gold))

# ---- THE ALIGNMENT ENGINE — every run verse to its spec verse by token, block by block (E2's engine reused) ----
def norm(w):
    if w in ('את', 'ואת', 'אתו', 'אתם', 'אתה'): return None
    if w[:1] == 'ו' and len(w) > 3: w = w[1:]
    if w[:1] == 'ה' and len(w) > 3: w = w[1:]
    return w
def bag(k):
    return set(x for x in map(norm, toks('Exod', *k)) if x)
BLOCKS = [('office', (28, 1, 5), (39, 1, 1)), ('ephod', (28, 6, 14), (39, 2, 7)), ('breastplate', (28, 15, 30), (39, 8, 21)),
          ('robe', (28, 31, 35), (39, 22, 26)), ('plate', (28, 36, 38), (39, 30, 31)), ('tunics', (28, 39, 43), (39, 27, 29))]
NUM = {'אחד', 'אחת', 'שני', 'שתי', 'שנים', 'שלש', 'שלשה', 'שלשת', 'ארבע', 'ארבעה', 'חמש', 'חמשה', 'שש', 'ששה', 'הששה', 'שבע', 'שבעה', 'שמנה', 'תשע', 'עשר', 'עשרה',
       'עשרים', 'שלשים', 'ארבעים', 'חמשים', 'מאה', 'מאת', 'אלף', 'אמתים', 'וחצי', 'חצי', 'עשתי', 'ששת', 'ארבעת'}
ALIGN = {}
for name, (sc, sa, sz), (rc, ra, rz) in BLOCKS:
    spec = [(sc, v) for v in range(sa, sz + 1)]; rv = [(rc, v) for v in range(ra, rz + 1)]
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
           sum(a['run_matched'] for a in ALIGN.values()), sum(len(a['dropped']) for a in ALIGN.values()))
assert A_TOTAL == (43, 31, 22, 24, 21), A_TOTAL
A_DROPPED = [d for a in ALIGN.values() for d in a['dropped']]
assert A_DROPPED == ['28:1', '28:2', '28:3', '28:4', '28:5', '28:9', '28:10', '28:11', '28:13', '28:14', '28:29', '28:30', '28:33', '28:35', '28:37', '28:38',
                     '28:39', '28:40', '28:41', '28:42', '28:43'], A_DROPPED
A_NUM_EQ = sorted(n for n, a in ALIGN.items() if a['numerals_equal']); assert A_NUM_EQ == ['office', 'plate', 'robe'], A_NUM_EQ
A_BP = ALIGN['breastplate']; assert (A_BP['spec'], A_BP['run'], A_BP['matched'], A_BP['dropped']) == (16, 14, 14, ['28:29', '28:30']), A_BP
HEADS = [('ephod', ('האפד', 'האפוד', 'אפד', 'אפוד')), ('breastplate', ('חשן', 'החשן')), ('robe', ('מעיל', 'המעיל')), ('plate', ('ציץ',)), ('tunic', ('הכתנת', 'כתנת')),
         ('turban', ('מצנפת', 'המצנפת')), ('sash', ('ואבנט', 'אבנט', 'האבנט', 'אבנטים', 'באבנט')), ('caps', ('ומגבעות', 'המגבעת', 'מגבעות', 'מגבעת')), ('breeches', ('מכנסי', 'ומכנסי'))]
def first(rng, tks):
    for k in rng:
        if any(w in tks for w in toks('Exod', *k)): return k
def order_of(rng):
    return [n for k, n in sorted([(first(rng, t), n) for n, t in HEADS if first(rng, t)])]
SPEC_ORDER = order_of([s for s in SPEC if s >= (28, 6)]); RUN_ORDER = order_of([r for r in RUN if (39, 2) <= r <= (39, 31)])
assert SPEC_ORDER == ['ephod', 'breastplate', 'robe', 'plate', 'turban', 'sash', 'tunic', 'caps', 'breeches'], SPEC_ORDER
assert RUN_ORDER == ['ephod', 'breastplate', 'robe', 'tunic', 'breeches', 'caps', 'turban', 'sash', 'plate'], RUN_ORDER
SPEC_FIRST = {n: first([s for s in SPEC if s >= (28, 6)], t) for n, t in HEADS}
assert SPEC_FIRST['turban'] == (28, 37) and SPEC_FIRST['tunic'] == (28, 39) and SPEC_FIRST['sash'] == (28, 39), SPEC_FIRST
def order_by_name(seq):
    return [n for n, t in sorted(HEADS, key=lambda x: next((i for i, w in enumerate(seq) if w in x[1]), 999)) if any(w in t for w in seq)]
LEV8 = [w for v in (7, 8, 9, 13) for w in toks('Lev', 8, v)]; LEV8_ORDER = order_by_name(LEV8)
assert LEV8_ORDER == ['tunic', 'sash', 'robe', 'ephod', 'breastplate', 'turban', 'plate', 'caps'], LEV8_ORDER
E29 = [w for v in (5, 6, 8, 9) for w in toks('Exod', 29, v)]; E29_ORDER = order_by_name(E29)
assert E29_ORDER == ['tunic', 'robe', 'ephod', 'breastplate', 'turban', 'sash', 'caps'], E29_ORDER
GOLD_BLOCK = {name: (sum(1 for v in range(sa, sz + 1) for w in toks('Exod', sc, v) if 'זהב' in w), sum(1 for v in range(ra, rz + 1) for w in toks('Exod', rc, v) if 'זהב' in w))
              for name, (sc, sa, sz), (rc, ra, rz) in BLOCKS}
assert GOLD_BLOCK == {'office': (1, 0), 'ephod': (5, 4), 'breastplate': (7, 8), 'robe': (3, 1), 'plate': (1, 1), 'tunics': (0, 0)}, GOLD_BLOCK
GOLD_GARMENTS = sorted(n for n, g in GOLD_BLOCK.items() if g[0] and n != 'office'); assert GOLD_GARMENTS == ['breastplate', 'ephod', 'plate', 'robe'], GOLD_GARMENTS
print('alignment: spec %d verses, run %d; spec matched %d, run matched %d, dropped %d — %s; numerals equal in %s; SPEC order %s; RUN order %s; Lev 8 order %s; Exod 29 order %s; gold per block %s'
      % (A_TOTAL + (A_DROPPED, A_NUM_EQ, SPEC_ORDER, RUN_ORDER, LEV8_ORDER, E29_ORDER, GOLD_BLOCK)))

# ---- the callees (cold) --------------------------------------------
_buf = io.StringIO()
with contextlib.redirect_stdout(_buf):
    import cold_run_sanctuary_build as SB
    import cold_run_priesthood as PR
    import cold_run_ordinances as ORD
    import cold_run_yoma as YOMA
    import world_engine as WE
SB_STAVES = SB.ark('staves')['v']; SB_BREAD = SB.table('continually')['v']; SB_LAMPS = SB.menorah('lamps')['v']; SB_HANGINGS = SB.court('hangings')['v']
PR_NEZER = PR.family('nezer')['v']; PR_REND = PR.family('hair_rend')['v']; PR_ARR = PR.lamp_table('arrangement')['v']
ORD_NAKED = ORD.altar('nakedness')['v']
YOMA_SEQ = YOMA.service_order(); YOMA_LINEN = [x for x in YOMA_SEQ if x[0] == '16:4'][0][1]; YOMA_STRIP = [x for x in YOMA_SEQ if x[0] == '16:23'][0][1]
assert YOMA_SEQ.index([x for x in YOMA_SEQ if x[0] == '16:23'][0]) > YOMA_SEQ.index([x for x in YOMA_SEQ if x[0] == '16:24'][0])
print('routing receipts: cold_run_sanctuary_build CALLED — the ark\'s staves %r, the bread %r, the lamps %r, the hangings %r; cold_run_priesthood CALLED — the crown of the oil %r, '
      'the rending %r, the arrangement %r; cold_run_ordinances CALLED — nakedness %r; cold_run_yoma CALLED — 16:4 %r, 16:23 %r (relocated after 16:25) [IMPORT, live calls]'
      % (SB_STAVES, SB_BREAD, SB_LAMPS, SB_HANGINGS, PR_NEZER, PR_REND, PR_ARR, ORD_NAKED, YOMA_LINEN, YOMA_STRIP))

I, M, A, D, P, H = 'INK', 'MOVE', 'ANSWER-SHEET', 'DATA', 'IMPORT', 'HYPOTHESIS'   # H: THE LINK REVIEW LAW (LR3, 2026-09-07) — an untaught transfer, kept and labeled, never counted as compiled
def cell(v, p, why, fx):
    FX.validate(fx)
    return {'v': v, 'p': p, 'why': why, 'fx': fx}
TT = "Midrash Tanchuma, "
VB = "the vestments block (round 27, credited): "

# =====================================================================
# THE SPEC — compiled from the ink of Exodus 28; THE RUN — Exodus 39 matched to it.
# Mishnah/Talmud appear ONLY on [MOVE] lines (motion 4) and as DATA (motion 2).
# =====================================================================

# ---- F1: THE OFFICE AND THE SET (28:1-5; 39:1) --------------------------
def office(q):
    if q == 'priest_phrase':
        return cell(3, I, "'to serve Me as priest' (לכהנו לי) at %s — three seats in the Tanakh, all in this chapter's opening; with 28:41's 'and they shall serve Me as priest' and the run's 39:41 'to serve as priest' the priest-verb stands at five seats of the span" % (fmt(c_lekhahano),), ['invested_office'])
    if q == 'serve_before_me':
        return cell('service_before_the_presence', M, "Onkelos Exod 28:1 + 28:3 + 28:4 + 28:41 — 'to SERVE BEFORE ME' five times: the priest-verb decoded as audience-service, the office defined as standing service in the Presence-space (the Terumah reading's 'before Me' at the separation, E2)", ['invested_office'])
    if q == 'four_sons':
        return cell(['נדב', 'ואביהוא', 'אלעזר', 'ואיתמר'], I, "28:1 names the four sons %s — the office's first roster; two of the four die at Lev 10:1 (%s) in the garments' first week [IMPORT by name]" % (c_sons, fmt(c_lev10)), ['invested_office'])
    if q == 'purpose':
        return cell(2, I, "'for honor and for splendor' (לכבוד ולתפארת) at %s alone in the Tanakh — stated for Aaron's garments (28:2) and repeated verbatim for the sons' (28:40): one purpose clause for both sets" % (fmt(c_purpose),), [FX.NONE])
    if q == 'purpose_read':
        return cell('ahasuerus_wore_them', M, "Megillah 12a:7 (opened per gap) — 'when he showed the riches of the GLORY of his kingdom' (Esth 1:4): R. Yosei bar Chanina — he wore the priestly garments, 'the honor of the SPLENDOR of his greatness' there and 'for honor and for SPLENDOR' here — the purpose clause's splendor-word carried to the feast by verbal analogy", [FX.NONE])
    if q == 'wise_hearted':
        return cell('they_make', I, "28:3 'speak to all the WISE OF HEART whom I have filled with the spirit of wisdom, and THEY shall make Aaron's garments' — the making delegated to the workforce; 'and they shall make' at %s (the garments, the set, the ephod) against 'and YOU shall make' at %d seats" % (fmt3(c_veasu), len(c_veasita)), [FX.NONE])
    if q == 'six_nouns':
        return cell(6, I, "28:4 'and these are the garments they shall make' — the verse's own list %s: breastplate, ephod, robe, checkered tunic, turban, sash — SIX garments (the tunic's 'checkered' a hapax, %s)" % (c_six, fmt(c_tashbetz[0])), [FX.NONE])
    if q == 'eight':
        return cell(8, I, "the six of 28:4 plus the PLATE (28:36, outside the list) plus the BREECHES (28:42, after the investiture verse) = EIGHT — Mishnah Yoma 7:5's count computed from the chapter's own inventory: the list names six, the chapter makes eight", [FX.NONE])
    if q == 'eight_sheet':
        return cell(['כתנת', 'מכנסים', 'מצנפת', 'אבנט', 'חשן', 'אפוד', 'מעיל', 'ציץ'], A, "Mishnah Yoma 7:5 — 'the high priest serves in EIGHT vessels and the common priest in FOUR: tunic, breeches, turban, sash; the high priest adds the breastplate, ephod, robe, plate' — the sheet's eight in the sheet's order", [FX.NONE])
    if q == 'four_common':
        return cell(4, I, "28:40 'for Aaron's sons you shall make tunics, sashes, and caps' + 28:42 'make THEM linen breeches' = FOUR for the sons — the sheet's common-priest four; the ink calls the sons' headgear CAPS (מגבעות, 28:40) where the sheet's list says turban (מצנפת) — the sheet names the sons' four by the high priest's word", [FX.NONE])
    if q == 'gold_sets':
        return cell(GOLD_GARMENTS, I, "the metal census per garment block: gold-tokens in the spec's blocks %s — the ephod, breastplate, robe (its bells), and plate carry gold; the tunic, turban, sash, breeches carry NO metal token: the gold-bearing four are EXACTLY Yoma 7:5's four the high priest ADDS, and the metal-less four its common-priest four — the sheet's 'gold garments' and 'white garments' (Yoma 7:3-4) are one census of the ink's metal tokens" % (GOLD_BLOCK,), [FX.NONE])
    if q == 'gold_white_sheet':
        return cell(['gold', 'white', 'gold', 'white', 'gold', 'own'], A, "Mishnah Yoma 3:4, 3:6, 7:3, 7:4 — the Day's dressing sequence: gold (dawn), white (the inner service), gold (the rams), white (the ladle), gold (the afternoon incense), then HIS OWN garments — five changes, five immersions, ten sanctifications", [FX.NONE])
    if q == 'linen_lev16':
        return cell(4, I, "Lev 16:4's four garments each with 'linen' (בד): the count of the linen-word in the verse %d — tunic, breeches, sash, turban — the white set = the ink's metal-less four [IMPORT by name]; Lev 6:3 the priest's 'linen garment and linen breeches' (%d)" % c_lev16, [FX.NONE])
    if q == 'yoma_linen_by_call':
        return cell(YOMA_LINEN, P, "CALLED cold_run_yoma.service_order() -> the entry at 16:4: %r; and the stripping at 16:23 relocated after 16:25 (%r) — the white set's donning and doffing in the Day engine's own program counter [IMPORT, live call]" % (YOMA_LINEN, YOMA_STRIP), [FX.NONE])
    if q == 'materials_five':
        return cell(['הזהב', 'התכלת', 'הארגמן', 'תולעת השני', 'השש'], I, "28:5 'and THEY shall take the gold, the blue, the purple, the crimson, and the fine linen' — five materials, each with the article: the set's whole palette in one verse", [FX.NONE])
    if q == 'they_take':
        return cell('two_collectors', M, "Bava Batra 8b:9 (opened per gap) — 'no authority over the public in money with fewer than two — from where? Rav Nachman: AND THEY SHALL TAKE THE GOLD' (28:5): the plural take-verb read as the two-collector rule (EX28-10's seat at its Talmud derivation)", [FX.NONE])
    if q == 'two_collectors_sheet':
        return cell((3, 7, 2), A, "Mishnah Shekalim 5:2 — no fewer than three treasurers and seven supervisors; no authority over the public in money with fewer than two (credited)", [FX.NONE])
    if q == 'holy_garments':
        return cell((3, 6), I, "'holy garments' bare at %s (28:2, 28:4, and Lev 16:4's white set) and 'THE holy garments' at %s — the run's 39:1 and 39:41 use the articled form: the spec commissions 'holy garments', the run delivers 'THE holy garments'" % (fmt(c_bigdei_kodesh), fmt(c_bigdei_hakodesh)), [FX.NONE])
    if q == 'serad':
        return cell(4, I, "the run's 39:1 opens with a class the spec never names — 'garments of SERAD (שרד) for serving in the Holy' — at %s (bare at 39:1; with the article at 31:10, 35:19, 39:41): a second garment class beside 'the holy garments for Aaron' in the same verse" % (fmt(c_serad),), [FX.NONE])
    if q == 'from_the_stock':
        return cell(['התכלת', 'והארגמן', 'ותולעת השני'], I, "39:1 'and FROM the blue and the purple and the crimson they made' — the run names the public stock as the source (three colors; no gold, no linen in the 'from' list)", [FX.NONE])
    if q == 'garment_value':
        return cell({'R_Meir': (12, 800), 'sages': (18, 12, 30), 'source': 'public', 'surplus': 'his_own'}, D, "Mishnah Yoma 3:7 — the high priest's linen: morning Pelusian of twelve maneh, afternoon Indian of eight hundred zuz (R. Meir); the sages eighteen and twelve, thirty in all — FROM THE PUBLIC, and he may add from his own: the price is data; the public source is 28:5's plural take-verb", [FX.NONE])
    if q == 'convert':
        return cell('the_list_read_aloud', M, "Shabbat 31a:7 (opened per gap) — a gentile heard a scribe reading 'AND THESE ARE THE GARMENTS THEY SHALL MAKE: A BREASTPLATE AND AN EPHOD' (28:4), asked whose they were, and came to convert to be made high priest; Shammai's cubit, Hillel's conversion — the office not open to the convert (Num 1:51 [IMPORT by name])", ['stranger_barred'])
    if q == 'run_stamp_first':
        return cell((39, 1), I, "the run's first verse closes with the stamp 'as the LORD commanded Moses' — the first of seven with 'Moses' (%s) and an eighth without at 39:43; no verse of Exod 28 carries the stamp (%s)" % (fmt3(c_stamp7), c_stamp_spec), [FX.NONE])
    if q == 'tokens':
        return cell(c_tokens, I, "the spec's 43 verses hold %d tokens, the run's 43 hold %d — the run shorter in the garments (31 verses for the spec's 43) and longer by the completion and the manifest (39:32-43)" % c_tokens, [FX.NONE])
    return cell('no_case', I, '', [FX.NONE])

# ---- F2: THE EPHOD AND ITS STONES (28:6-14; 39:2-7) ----------------------
def ephod(q):
    if q == 'materials':
        return cell(['זהב', 'תכלת', 'וארגמן', 'תולעת שני', 'ושש משזר'], I, "28:6 'the ephod of gold, blue, purple, crimson, and twined fine linen, DESIGNER'S WORK' — five materials; 'designer's work' (מעשה חשב) at %d seats of the Tanakh, all in Exodus (the curtains, the veil, the ephod, the breastplate, their runs)" % len(c_choshev), [FX.NONE])
    if q == 'they_vs_he':
        return cell(('ועשו', 'ויעש'), I, "the spec's 28:6 'and THEY shall make the ephod' (the wise-hearted) against the run's 39:2 'and HE made the ephod' — the run's singular at %s (the ephod, the breastplate, the robe: the high priest's three woven garments) against its plural 'and they made' at %d seats" % (fmt3(c_vayaas), len(c_vayaasu)), [FX.NONE])
    if q == 'shoulders':
        return cell(2, I, "28:7 'two shoulder-pieces joined shall it have at its two ends' = 39:4 'shoulder-pieces they made for it, joined, at its two ends it was joined' — the run's verse a rearrangement of the spec's tokens", [FX.NONE])
    if q == 'band_is':
        return cell(('ממנו יהיה', 'ממנו הוא'), I, "28:8 'the band of its ephod upon it, as its work, OF IT SHALL BE' (%s) against 39:5 'of it IT IS, as its work' (%s) — each phrase once in the Tanakh: the spec's future becomes the run's present in one token" % (fmt(c_mimenu[0]), fmt(c_mimenu[1])), [FX.NONE])
    if q == 'two_stones':
        return cell(2, I, "28:9 'two ONYX stones' — the onyx-word at %d seats of the Tanakh: the Garden's river (Gen 2:12), the sanctuary's offering (25:7, 35:9, 35:27), the ephod and breastplate, David's treasure, Ezekiel's Eden (28:13) [IMPORT by name]" % len(c_shoham), [FX.NONE])
    if q == 'six_six':
        return cell((6, 6), I, "28:10 'six of their names on the one stone and the names of the six remaining on the second stone, IN THEIR BIRTH ORDER' — the ordering word (כתולדתם) at %s alone in the Tanakh" % (fmt(c_toledot),), ['names_borne'])
    if q == 'six_six_talmud':
        return cell({'first_stone': 'judah_advanced', 'second': 'by_birth', 'letters': (50, 25)}, M, VB + "Sotah 36a:12-13 — six and six; the SECOND stone 'according to their birth', the first not (Judah advanced); fifty letters, twenty-five per stone — the engraving order argued at the verse", ['names_borne'])
    if q == 'engravings':
        return cell(6, I, "'signet engravings' (פתוחי חתם) at %s — three objects (the shoulder stones 28:11, the breastplate's twelve 28:21, the plate 28:36) at the spec and the same three at the run (39:6, 39:14, 39:30): WRITING enters the vestments at exactly three places, each stamped by the run" % (fmt(c_pituchei),), ['names_borne'])
    if q == 'clear_script':
        return cell('ketav_mefarash', M, "Onkelos Exod 28:11 + 28:21 + 28:36 — 'CLEAR SCRIPT' (כתב מפרש) for the engraving formula at all three objects; the run's 39:6 'engraved with script made clear' where the Hebrew has 'signet engravings' (Onkelos Exod 39:1-7)", ['names_borne'])
    if q == 'engraver':
        return cell('shamir', M, "28:11 'the work of a STONE ENGRAVER' — the tool is a PARAMETER the ink leaves open; EX28-12 (credited, Sotah 48b): the stones written by the shamir of the twilight census, 'in their fullness' (28:20) uncut", ['names_borne'])
    if q == 'remembrance':
        return cell(4, I, "'and Aaron shall BEAR' (ונשא אהרן) at %s — the names on his shoulders (28:12), the names on his heart (28:29), the judgment (28:30), the iniquity of the holy things (28:38): the chapter's carrying-verb four times, each a different load" % (fmt(c_nasa),), ['names_borne'])
    if q == 'remembrance_run':
        return cell(True, I, "39:7 'and he set them on the ephod's shoulder-pieces, stones of REMEMBRANCE for the children of Israel' — the run keeps the remembrance noun and drops 'and Aaron shall bear their names before the LORD': the run mounts the stones, the spec wears them", ['names_borne'])
    if q == 'settings_chains':
        return cell(3, I, "28:13-14 'settings of gold; two chains of pure gold, twisted, CORD-WORK' — 'cord-work' (מעשה עבת) at %s; the chain-word at six seats of the Tanakh, three of them Solomon's Temple (1 Kgs 7:17, 2 Chr 3:5, 3:16) [IMPORT by name]" % (fmt(c_avot),), [FX.NONE])
    if q == 'process_verse':
        return cell(4, I, "39:3 'and they BEAT the gold PLATES and CUT THREADS to work into the blue, into the purple, into the crimson, into the fine linen' — the run's ADDED verse with no spec counterpart: 'they beat' %s, 'plates' %s, 'threads' %s each once in the Tanakh, 'he cut' %s (with the Psalm's spear); 'into' four times (%d)" % (fmt(c_process[0]), fmt(c_process[1]), fmt(c_process[3]), fmt(c_process[2]), c_betokh), [FX.NONE])
    if q == 'process_onkelos':
        return cell('beat_and_cut', M, "Onkelos Exod 39:1-7 — 'they BEAT the gold into plates and CUT threads' — the execution-only manufacturing verse: the one process the run adds where the spec gave outcome", [FX.NONE])
    if q == 'gold_thread_count':
        return cell(4, M, "Yoma 72a:6 (opened per gap) — 'and say gold too is six? Rav Acha bar Yaakov: AND HE CUT THREADS (39:3) — thread, threads: FOUR' — the gold thread's count derived from the run's added verse, not from the spec", [FX.NONE])
    if q == 'gold_thread_placement':
        return cell('one_gold_thread_per_color', M, "Yoma 72a:7 (opened) — Rav Ashi: 'TO WORK INTO THE BLUE AND INTO THE PURPLE' (39:3) — four of two each? 'AND YOU SHALL MAKE: all its makings equal' — ONE gold thread into EACH of the four colors: the run's fourfold 'into' is the count's own repetition", [FX.NONE])
    if q == 'thread_28':
        return cell(28, M, "Yoma 72a:5 (opened) — the breastplate and ephod TWENTY-EIGHT: 28:15's five materials — 'four of six each, twenty-four; gold four' — 4 × 6 + 4 = 28, the sixfold thread from the run's five 'fine linen' tokens (71b:6) and the gold's four from the run's process verse: BOTH parameters supplied by the run", [FX.NONE])
    if q == 'run_teaches_parameter':
        return cell('the_parameter_supplied', M, "move M-22 (the run read back into the spec) in a THIRD form: at D8 the run gave the spec a COLUMN, at E2 its ORDER, here its PARAMETERS — Yoma 71b-72a's thread counts run on Exod 39's tokens ('fine linen' five times at 39:27-28, 'twined' added at 39:24, the process verse 39:3), not on Exod 28's", [FX.NONE])
    if q == 'ephod_elsewhere':
        return cell(40, I, "the ephod-word at %d seats of the Tanakh — the priests' at the sanctuary chapters and Lev 8:7; 'a LINEN ephod' at %s (Samuel, Nob's priests, David dancing); Gideon's and Micah's ephods; the Torah's seats outside this span %s (Num 34:23 the NAME Ephod, a homograph)" % (c_efod_n, fmt(c_efod_bad), fmt(c_efod_torah)), [FX.NONE])
    if q == 'ephod_atones':
        return cell('idolatry', M, "Zevachim 88b:7 (opened per gap) — the EPHOD atones for idolatry: 'no ephod and teraphim' (Hos 3:4) — the garment's function assigned by its word's idolatrous seats", [FX.NONE])
    if q == 'stamps':
        return cell([(39, 5), (39, 7)], I, "the ephod's run stamped twice — after the band (39:5) and after the stones (39:7): two of the seven 'as the LORD commanded Moses'", [FX.NONE])
    if q == 'alignment':
        return cell((9, 6, 4, 5), I, "the ephod block: 9 spec verses, 6 run verses, 4 spec matched, 5 run matched — %s dropped: the stones' engraving and settings (28:9-11, 13-14) restated by the run in fewer verses (39:6 folds 28:9-11 into one)" % (ALIGN['ephod']['dropped'],), [FX.NONE])
    return cell('no_case', I, '', [FX.NONE])

# ---- F3: THE BREASTPLATE OF JUDGMENT (28:15-30; 39:8-21) ------------------
def breastplate(q):
    if q == 'name':
        return cell(('חשן משפט', 'חשן המשפט'), I, "'a breastplate of JUDGMENT' bare at %s and 'the breastplate of THE judgment' at %s (28:29 with the prefix) — the garment named by its function at three seats of the spec; the run never says 'judgment' (39:8 'the breastplate')" % (fmt(c_cm[0]), fmt(c_cm[1])), ['judgment_borne'])
    if q == 'word_seats':
        return cell(17, I, "the breastplate-word at %d seats of the Tanakh — every one in Exodus 25-39 or Lev 8:8: a vessel that exists only in the sanctuary chapters and their run" % len(c_choshen_all), [FX.NONE])
    if q == 'like_the_ephod':
        return cell('internal_pointer', I, "28:15 'designer's work LIKE THE WORK OF THE EPHOD you shall make it' — an internal pointer to 28:6's recipe (the comparative kaf on a vessel, not a procedure of another span)", [FX.NONE])
    if q == 'for_this_alone':
        return cell('taasenu_this_not_another', M, "Yoma 71b:13 (opened) — Rav Mari: 'YOU SHALL MAKE IT (תעשנו) is written — for this and not for another': the pointer's scope read from its object suffix", [FX.NONE])
    if q == 'equal_threads':
        return cell('all_makings_equal', M, "Yoma 71b:14 (opened) — Rav Ashi: 'AND YOU SHALL MAKE is written — that all its makings be equal' (not three of ten or two of nine): the thread-equality rule on the bare making-verb (the spec's 'and you shall make' at twelve seats)", [FX.NONE])
    if q == 'square_span':
        return cell(('רבוע', 'כפול', 'זרת'), I, "28:16 'SQUARE it shall be, DOUBLED, a SPAN its length and a span its width' — 'square' at %d Torah seats (the altars, the breastplate, their runs); the span-word at %s alone (Ezekiel's altar the third); the run's 39:9 writes 'doubled' TWICE (%s)" % (len(c_ravua), fmt(c_zeret), c_kaful), [FX.NONE])
    if q == 'span_parameter':
        return cell('a_hand_measure', M, "Menachot 11a:5 (opened per gap) — 'THIS IS A SPAN, this is the fistful' — the span a bodily unit like the cubit of Moses: the breastplate's size a PARAMETER of the hand", [FX.NONE])
    if q == 'four_rows':
        return cell([3, 3, 3, 3], I, "28:17-20 'four rows of stone' — the stone-names per row %s = twelve; 39:10-13 repeats the twelve names in the same order (%s)" % (c_rows, c_names_run == STONES), ['names_borne'])
    if q == 'names_equal':
        return cell(True, I, "the run's stone list equals the spec's token for token (%s); the run's fourth row drops the vav of 'and onyx' and rewrites 'set in gold in their fullness' as 'surrounded with settings of gold in their fullness'" % (c_names_spec == c_names_run,), [FX.NONE])
    if q == 'homographs':
        return cell({'אדם': 492, 'לשם': 36, 'שבו': 54, 'תרשיש': 25}, I, "the twelve stone-names' seats in the whole Tanakh %s — FOUR are homographs of common words in the unpointed text (אדם 'man', לשם 'to the name', שבו 'they returned', תרשיש the port), six are rare (two to four seats), two (sapphire, onyx) mid-range" % (c_stone_seats,), [FX.NONE])
    if q == 'tarshish_read':
        return cell('the_minister_is_the_stone', M, "Megillah 12b:10 (opened per gap) — the seven ministers as the angels' plea: 'TARSHISH — did they serve before You in the priestly garments, of which it is written (28:20) TARSHISH AND ONYX AND JASPER?' — the port's name read as the fourth row's first stone: the homograph read at the sheet's seat", [FX.NONE])
    if q == 'ezekiel_nine':
        return cell(['לשם', 'שבו', 'אחלמה'], I, "Ezek 28:13's covering of the king of Tyre lists %d of the twelve stone-names [IMPORT by name]; the missing three are the THIRD ROW entire (%s) — the prophet's Eden wears three rows of the breastplate" % (len(c_ezek_in), c_ezek_out), [FX.NONE])
    if q == 'twelve_names':
        return cell(12, I, "28:21 'the stones shall be on the names of the children of Israel, TWELVE on their names, signet engravings, EACH ON HIS NAME, for the twelve tribes' — 'each on his name' at %s alone (spec and run)" % (fmt(c_ish),), ['names_borne'])
    if q == 'fullness':
        return cell('uncut', M, "28:20 'in their FULLNESS' (במלאתם) — EX28-12 (credited): the stones set whole, uncut, written by the shamir; the fullness-word shares its consonants with the installation offering (מלאים) and the fill-the-hand idiom — one root for filling a setting, a hand, an office", ['names_borne'])
    if q == 'rings_cords':
        return cell((7, 7), I, "the ring-tokens in the spec's breastplate verses and the run's: %s — the hardware restated one for one; 'opposite its joining' at %s and 'toward its front' at %s (spec and run each)" % (c_rings, fmt(c_leumat), fmt3([(28, 27), (39, 20)])), [FX.NONE])
    if q == 'not_detached':
        return cell('breastplate_fixed', I, "28:28 'they shall bind the breastplate by its rings to the ephod's rings with a blue cord... AND THE BREASTPLATE SHALL NOT BE DETACHED from the ephod' — the verb at %s alone in the Tanakh: the spec's ban, and the run RESTATES it at 39:21 and stamps it" % (fmt(c_yizach),), ['breastplate_fixed'])
    if q == 'not_detached_onkelos':
        return cell('la_yitparek', M, "Onkelos Exod 28:28 + 28:32 — 'the breastplate shall NOT BE DETACHED from upon the ephod' and 'it shall NOT BE TORN': the two standing prohibitions inside the garment spec, the poles-never-removed class extended", ['breastplate_fixed'])
    if q == 'lashes':
        return cell('lashes', M, "Yoma 72a:9 (opened) — R. Elazar: one who DETACHES the breastplate from the ephod, and one who removes the ark's staves, is FLOGGED — 'it shall not be detached' (28:28), 'they shall not be removed' (25:15); Makkot 22a:8 (opened): Abaye adds both to the lashes count with these two warnings", ['lashes'])
    if q == 'design_objection':
        return cell('lo_not_shelo', M, "Yoma 72a:8-9 (opened) — Rav Acha bar Yaakov's objection at both bans: 'perhaps the Merciful One said: fasten them well SO THAT it not be detached?' — 'is it written שלא (so that not)? it is written לא (not)' — the design-spec read refused by the particle: the same test the E2 staves passed", ['breastplate_fixed'])
    if q == 'staves_by_call':
        return cell(SB_STAVES, P, "CALLED cold_run_sanctuary_build.ark(staves) -> %r — the ark's ban, the breastplate's twin under one particle test (Yoma 72a:9 names both in one sentence) [IMPORT, live call]" % (SB_STAVES,), ['breastplate_fixed'])
    if q == 'bears_names':
        return cell('on_his_heart', I, "28:29 'and Aaron shall bear the names of the children of Israel in the breastplate of judgment ON HIS HEART when he enters the Holy, for a remembrance before the LORD continually' — the names carried twice (shoulders 28:12, heart 28:29)", ['names_borne'])
    if q == 'urim':
        return cell(('האורים', 'התמים'), I, "28:30 'and you shall put into the breastplate of judgment THE URIM AND THE TUMMIM' — the Urim's seats %s (the fifth the Psalm's 'great LIGHTS'); the Tummim's %s (1 Sam 14:41's 'give Tummim' in the bare form); 'whole' (תמים) at %d seats — the oracle's two names are two common words" % (fmt(c_urim), fmt(c_tummim), c_tamim_n), ['judgment_borne'])
    if q == 'judgment_borne':
        return cell('judgment_borne', I, "28:30 'and Aaron shall bear THE JUDGMENT of the children of Israel on his heart before the LORD continually' — the organ's function on the wearer: the portable oracle (Num 27:21 'he shall inquire for him by the judgment of the Urim' [IMPORT by name])", ['judgment_borne'])
    if q == 'judgment_onkelos':
        return cell('dina', M, "Onkelos Exod 28:15 + 28:29-30 — 'the breastplate of JUDGMENT' (דינא) and 'Aaron bears THE JUDGMENT of the sons of Israel... continually', the Urim and Tummim INSIDE it — the judgment organ as a portable query interface (EX28-03)", ['judgment_borne'])
    if q == 'urim_authorization':
        return cell(['king', 'court', 'public_need'], A, "Mishnah Yoma 7:5 — 'in these (the eight) the Urim and Tummim are consulted, and only for the KING, the COURT, or one whom the PUBLIC needs' — the petitioner class is data the ink does not state (EX28-09, credited)", ['judgment_borne'])
    if q == 'urim_end':
        return cell('first_prophets', D, "Mishnah Sotah 9:12 — 'when the first prophets died the Urim and Tummim ceased' — the organ's end date; Ezra 2:63 'until a priest stands with Urim and Tummim' [IMPORT by name]", ['judgment_borne'])
    if q == 'tamid':
        return cell(3, I, "'continually' (תמיד) at %s — the names (28:29), the judgment (28:30), the plate (28:38): three continuous functions, all three in the spec's dropped verses" % (fmt3(c_tamid),), [FX.NONE])
    if q == 'before_the_lord':
        return cell((5, 0), I, "'before the LORD' at %s of the spec and NONE of the run — every Presence-clause is the spec's: the run mounts, binds, and stamps; it never says where the garment stands" % (fmt3(c_lifnei[0]),), [FX.NONE])
    if q == 'atones_judgments':
        return cell('judgments', M, "Zevachim 88b:7 + Arakhin 16a:15 (opened per gap) — the BREASTPLATE atones for judgments: 'you shall make a breastplate of JUDGMENT' — the function from the garment's own name", [FX.NONE])
    if q == 'alignment':
        return cell((16, 14, 14, ['28:29', '28:30']), I, "the breastplate block aligns one for one — 14 run verses to 14 spec verses (39:8-21 to 28:15-28); dropped exactly %s: the bearing of the names and the Urim — the two USE verses" % (A_BP['dropped'],), [FX.NONE])
    return cell('no_case', I, '', [FX.NONE])

# ---- F4: THE ROBE AND ITS BELLS (28:31-35; 39:22-26) --------------------
def robe(q):
    if q == 'wholly_blue':
        return cell(3, I, "28:31 'the robe of the ephod WHOLLY BLUE' — the phrase at %s (the ark's covering cloth of Num 4:6 the third [IMPORT by name]); the robe-word at %d seats of the Tanakh (Samuel's, Saul's, Job's, Ezra's)" % (fmt(c_kelil), c_meil_n), [FX.NONE])
    if q == 'run_cited_for_spec':
        return cell('39:22_cited', M, "Zevachim 88b:2 (opened per gap) — 'the robe was wholly of blue, AS IT IS SAID (39:22) AND HE MADE THE ROBE OF THE EPHOD, WOVEN WORK, WHOLLY BLUE' — the baraita cites the RUN verse for the spec's fact: the citation form of the run-teaches-spec move", [FX.NONE])
    if q == 'dye_test':
        return cell('test_dyeing_invalid', M, "Menachot 42b:13 (opened) — 'a test-dyeing is invalid because it is said WHOLLY BLUE (28:31) — R. Chanina ben Gamliel': the adverb read for the dye's purity", [FX.NONE])
    if q == 'twelve_threads':
        return cell(12, M, "Yoma 71b:15-72a:1 (opened) — the robe TWELVE: 'wholly blue' by analogy blue-blue from the veil (six), doubled by 'wholly'; 72a:2-3: not eight from its own hem — 'a vessel from a vessel, not from an ornament' — the robe a VESSEL, its pomegranates an ORNAMENT", [FX.NONE])
    if q == 'collar':
        return cell(('מעשה ארג', 'תחרא', 'לא יקרע'), I, "28:32 'its head's opening in its midst, a border around its opening, WOVEN WORK, like the opening of a COAT OF MAIL it shall have — IT SHALL NOT BE TORN' — 'woven work' at %s alone (all this span); the mail-word at %s alone; 'not torn' at %s alone" % (fmt(c_oreg), fmt(c_tachra), fmt(c_yikarea)), ['robe_uncut'])
    if q == 'woven_not_needle':
        return cell('woven_with_sleeve_exception', M, VB + "Yoma 72b:3 — priestly garments are not made needle-work but WOVEN (28:32's 'woven work'); Abaye: the needle serves only the SLEEVES — woven apart, attached, reaching the palm", ['robe_uncut'])
    if q == 'tear_lashes':
        return cell('lashes', M, "Yoma 72a:8 (opened; the standing read of round 27) — Rachva in Rav Yehuda's name: one who tears the priestly garments is FLOGGED, 'it shall not be torn'; Rav Acha bar Yaakov's 'perhaps a border so that it not tear?' — 'is it written SO THAT?' — the particle test", ['lashes'])
    if q == 'launder':
        return cell('less_than_three_by_three', M, "Zevachim 95a:4 (opened) — Reish Lakish: a robe that became impure is brought in less than three by three fingers at a time and laundered, because 'it shall not be torn' — the ban governs even cleaning: no cutting the robe to wash it", ['robe_uncut'])
    if q == 'rend_by_call':
        return cell(PR_REND, P, "CALLED cold_run_priesthood.family(hair_rend) -> %r — Lev 21:10's 'his garments he shall not rend' (the mourner's rending of ORDINARY garments, the high priest below, the commoner above — Horayot 3:5) beside 28:32's ban on the ROBE'S collar: two tearing laws in two books [IMPORT, live call]" % (PR_REND,), [FX.NONE])
    if q == 'bells':
        return cell(4, I, "28:33-34 'pomegranates of blue, purple, crimson on its hem around, and BELLS of gold between them: a golden bell and a pomegranate, a golden bell and a pomegranate' — the bell-word at %s: four seats in the whole Tanakh, ALL in this span; the alternation written twice at 28:34 and twice at 39:26 (%s)" % (fmt(c_bells), c_alt), ['entry_announced'])
    if q == 'bell_count':
        return cell({'sages': 72, 'R_Dosa': 36}, D, "Zevachim 88b:3 (opened) — seventy-two bells with seventy-two clappers, thirty-six a side; R. Dosa in R. Yehuda's name thirty-six, eighteen a side — the COUNT the ink never states (only the alternation): a parameter with two recorded settings", ['entry_announced'])
    if q == 'twined_added':
        return cell(True, I, "the run's 39:24 'pomegranates of blue, purple, crimson, TWINED' adds 'twined' (משזר) absent from the spec's 28:33 (%s); the run's twined-tokens %d against the spec's %d — added at the pomegranates, the breeches, the sash" % ('משזר' in toks('Exod', 39, 24) and 'משזר' not in toks('Exod', 28, 33), c_mashzar[1], c_mashzar[0]), [FX.NONE])
    if q == 'twined_eight':
        return cell(8, M, "Yoma 71b:10 (opened) — 'twined — EIGHT, from where? it is written (39:24) AND THEY MADE ON THE ROBE'S HEM POMEGRANATES... TWINED — twined-twined from the veil: twenty-four there, twenty-four here, each color eight' — the run's ADDED token is the derivation's seat; 71b:11-12: settled through the sash (a garment without gold)", [FX.NONE])
    if q == 'sound':
        return cell('entry_announced', I, "28:35 'and it shall be on Aaron TO SERVE, and ITS SOUND SHALL BE HEARD when he enters the Holy before the LORD and when he goes out, THAT HE NOT DIE' — 'its sound shall be heard' at %s alone; 'and when he goes out' with 2 Chr 23:7 alone; 'that he not die' at %d Tanakh seats" % (fmt(c_kolo), c_lo_yamut), ['entry_announced'])
    if q == 'sound_onkelos':
        return cell('audible_entry_with_death_sanction', M, "Onkelos Exod 28:33-35 — 'and its SOUND SHALL BE HEARD... that he not DIE': an audible-entry protocol carrying a death sanction — the garment announces its wearer (EX28-05)", ['entry_announced', 'death_by_heaven'])
    if q == 'run_drops_sound':
        return cell(['28:33', '28:35'], I, "the robe block's dropped spec verses %s — 39:26 'a bell and a pomegranate... TO SERVE, as the LORD commanded Moses' keeps 'to serve' and drops 'its sound shall be heard' and 'that he not die': the run makes the bells, the spec hears them" % (ALIGN['robe']['dropped'],), ['entry_announced'])
    if q == 'sounding_ring':
        return cell('ring_on_the_pan', M, VB + "Yoma 44b:16 — every other day the fire-pan had no rattle-ring; on the Day it had one (ben HaSegan) — read against 28:35's 'its sound shall be heard': the entry announced even where the robe is absent (the Day's white set has no robe)", ['entry_announced'])
    if q == 'samson_bell':
        return cell('the_presence_rang', M, "Sotah 9b:22 (opened) — 'to move him (לפעמו) in the camp of Dan' (Judg 13:25): the Presence rang before Samson LIKE A BELL — 'to move him' here and 'A BELL AND A POMEGRANATE' (28:34) there: the bell-word's verb form read back to the hem", [FX.NONE])
    if q == 'atones_speech':
        return cell('evil_speech', M, "Zevachim 88b:8 + Arakhin 16a:15 (opened) — the ROBE atones for evil speech: 'let a thing of SOUND come and atone for the sound of evil' — the function read from 28:35's sound clause", [FX.NONE])
    if q == 'run_singular':
        return cell((39, 22), I, "39:22 'and HE made the robe of the ephod, woven work, wholly blue' — the third and last singular making-verb of the run (with the ephod and the breastplate): the three garments of designer's and woven work made by one hand; the hem's pomegranates and bells 'THEY made' (39:24-25)", [FX.NONE])
    if q == 'alignment':
        return cell((5, 5, 3, 4), I, "the robe block: 5 spec, 5 run, 3 spec matched, 4 run matched — numerals equal (%s); 39:24's pomegranates fall below the threshold against 28:33 by the added 'twined' and the dropped bells" % (ALIGN['robe']['numerals_equal'],), [FX.NONE])
    return cell('no_case', I, '', [FX.NONE])

# ---- F5: THE PLATE (28:36-38; 39:30-31) ----------------------------------
def plate(q):
    if q == 'word':
        return cell(7, I, "'plate' (ציץ) at %s — the sanctuary's plate three times (28:36, 39:30, Lev 8:9) and the FLOWER four times (Aaron's rod's blossom at Num 17:23, Isaiah's fading flower, Jeremiah's): the plate-word is the flower-word" % (fmt(c_tzitz),), ['plate_propitiates'])
    if q == 'holy_to_the_lord':
        return cell(16, I, "28:36 'engrave on it signet engravings: HOLY TO THE LORD' — the phrase at %d seats of the Tanakh: the Sabbath (Exod 16:23, 31:15), the tithes and devoted things (Lev 27), and Zech 14:20's 'on the BELLS OF THE HORSES: holy to the LORD' [IMPORT by name] — the plate's inscription on bells, the robe's bells beside it" % len(c_kodesh_l), ['plate_propitiates'])
    if q == 'engrave_vs_write':
        return cell(('ופתחת', 'ויכתבו'), I, "the spec's 28:36 'you shall ENGRAVE on it signet engravings' against the run's 39:30 'and they WROTE on it a WRITING of signet engravings' — the run adds the writing verb and its noun (מכתב) where the spec had only the engraving", ['plate_propitiates'])
    if q == 'writing_read':
        return cell('embossed_from_behind', M, "Gittin 20b:1 (opened per gap) — 'I need WRITING and there is none? like gold dinars — protruding... there from inside, here from outside' — the plate's letters as the exemplar of embossed writing: the run's verb delta is the Talmud's datum", [FX.NONE])
    if q == 'holy_crown':
        return cell(3, I, "the run names it 'the plate, THE HOLY CROWN' (39:30) — 'the holy crown' (נזר הקדש) at %s: the name enters at 29:6 (E4's investiture spec) and the run and Lev 8:9 keep it; the spec's 28:36 never says 'crown'" % (fmt(c_nezer),), ['plate_propitiates'])
    if q == 'crown_onkelos':
        return cell('kelila_dekudsha', M, "Onkelos Exod 39:27-31 — 'the diadem, the HOLY CROWN of pure gold, engraved in CLEAR SCRIPT: holy to the LORD' — the clear-script token's third strike in one chapter", ['plate_propitiates'])
    if q == 'blue_cord':
        return cell(('על המצנפת', 'מלמעלה'), I, "28:37 'put it on a blue cord, on the turban, toward the FRONT of the turban' against 39:31 'a blue cord to set on the turban ABOVE' — the run replaces the front with 'above'; the turban first named in the spec at 28:37 (%s), before its own making at 28:39" % (SPEC_FIRST['turban'],), [FX.NONE])
    if q == 'wool_cap':
        return cell('cap_between', M, "Chullin 138a:6 (opened) — 'a cap of wool was placed on the high priest's head and on it the plate, to fulfill AND YOU SHALL PUT IT ON A BLUE CORD' — the cap the ink lacks (Arakhin 3b:14's hair showing between plate and turban, credited)", [FX.NONE])
    if q == 'forehead':
        return cell(4, I, "28:38 'and it shall be on Aaron's FOREHEAD... on his forehead continually' — the forehead-word at %s: twice here, Goliath's (1 Sam 17:49), Ezekiel's (3:7) [IMPORT by name]" % (fmt(c_metzach),), ['plate_propitiates'])
    if q == 'bears_iniquity':
        return cell('plate_propitiates', I, "28:38 'and Aaron shall BEAR THE INIQUITY OF THE HOLY THINGS which the children of Israel consecrate in all their holy gifts... FOR ACCEPTANCE FOR THEM before the LORD' — 'the iniquity of the holy things' at %s alone; 'for acceptance for them' at %s alone" % (fmt(c_avon_h), fmt(c_leratzon)), ['plate_propitiates'])
    if q == 'bears_onkelos':
        return cell('atones_offering_defects', M, "Onkelos Exod 28:38 — 'and Aaron shall BEAR THE INIQUITY of the sacred offerings... CONTINUALLY... for ACCEPTANCE for them' — the plate ATONES for offering-defects (EX28-06)", ['plate_propitiates'])
    if q == 'which_iniquity':
        return cell('impurity', M, "Menachot 25a:2 + Yoma 7a:10 (opened) — 'which iniquity does he bear? if piggul — it is already said it shall not be reckoned; if notar — it is already said it shall not be accepted' — by elimination, the IMPURITY of the offering", ['plate_propitiates'])
    if q == 'scope_sheet':
        return cell({'impure': 'propitiates', 'went_out': 'does_not'}, A, "Mishnah Zevachim 8:12 — 'the plate propitiates for the IMPURE and does not propitiate for what WENT OUT' (EX28-11, credited)", ['plate_propitiates'])
    if q == 'state_machine':
        return cell({'broken': 'none', 'on_peg': {'R_Yehuda': 'no', 'R_Shimon': 'yes'}}, M, VB + "Yoma 7b:4-5 — Abaye: broken, all agree it does not accept; hanging on a peg, the dispute: R. Yehuda 'on the forehead... and he shall bear' (contact), R. Shimon 'ALWAYS for acceptance' (the always-word moved from the wearing to the function) — EX28-13's state machine", ['plate_propitiates'])
    if q == 'polarity':
        return cell('acceptance_not_calamity', M, VB + "Yevamot 60b:13 — 'for acceptance FOR THEM': for acceptance and not for calamity; Rav Ashi: for Israel acceptance-only — the instrument's polarity scoped by its dative", ['plate_propitiates'])
    if q == 'attention':
        return cell('touch_tefillin_every_hour', M, VB + "Shabbat 12a:4 — from the plate with ONE Name 'on his forehead ALWAYS — that he not divert his attention', the tefillin with many Names all the more: the plate's continuous clause become the tefillin's handling law", [FX.NONE])
    if q == 'leratzon_word':
        return cell(11, I, "'for acceptance' (לרצון) at %d seats of the Tanakh — the offering engine's own word (Lev 1:3 'for his acceptance', 22:19-21, 23:11): the plate's function stated in the offerings' acceptance vocabulary" % len(tanakh_any('לרצון', 'לרצנכם', 'לרצנו')), ['plate_propitiates'])
    if q == 'atones_brazenness':
        return cell('brazenness', M, "Zevachim 88b:8 + Arakhin 16a:16 (opened) — the PLATE atones for brazenness: 'on Aaron's FOREHEAD' (28:38) with 'the forehead of a harlot woman' (Jer 3:3) — the function by the forehead-word's two seats", [FX.NONE])
    if q == 'run_last':
        return cell(('plate', 8), I, "the run makes the plate LAST — RUN_ORDER %s puts it ninth of nine, the spec's %s fourth: the tunics, caps, breeches, and sash all made before the plate in the run" % (RUN_ORDER, SPEC_ORDER), [FX.NONE])
    if q == 'run_drops':
        return cell(['28:37', '28:38'], I, "the plate block drops %s — the cord's placement (rewritten) and the whole function verse: the run writes the inscription and never says what it does" % (ALIGN['plate']['dropped'],), ['plate_propitiates'])
    return cell('no_case', I, '', [FX.NONE])

# ---- F6: THE TUNIC, TURBAN, SASH; THE SONS' FOUR; THE BREECHES (28:39-40, 42-43; 39:27-29) ----
def tunics(q):
    if q == 'checkered':
        return cell(('תשבץ', 'ושבצת'), I, "28:4's 'checkered tunic' (%s) and 28:39's 'you shall CHECKER the tunic of fine linen' (%s) — each once in the Tanakh; the settings-word of the stones (משבצת) at nine seats with Ps 45:14's 'settings of gold' — one root for the stone's setting and the tunic's weave" % (fmt(c_tashbetz[0]), fmt(c_tashbetz[1])), [FX.NONE])
    if q == 'shesh_spec_vs_run':
        return cell((2, 5), I, "'fine linen' (שש) in the spec's tunic verse 28:39: %d (the tunic, the turban; the sash gets no material) — in the run's 39:27-29: %d (the tunics, the turban, the caps, the breeches, the sash): the run names the material five times where the spec named it twice" % c_shesh, [FX.NONE])
    if q == 'sixfold':
        return cell(6, M, "Yoma 71b:6 (opened per gap) — 'their thread doubled SIX — from where? (39:27-28) AND THEY MADE THE TUNICS OF FINE LINEN, THE TURBAN OF FINE LINEN, THE ORNAMENTAL CAPS OF FINE LINEN, THE LINEN BREECHES OF FINE LINEN TWINED — five are written: one for flax, one for sixfold, one for twined, one for the other garments, one to make it indispensable' — THE RUN'S FIVE TOKENS ARE THE SPEC'S PARAMETER", [FX.NONE])
    if q == 'shesh_is_six':
        return cell('homograph', I, "the derivation's engine is the word itself: שש 'fine linen' and שש 'six' are one token in the unpointed text (%d seats of the Tanakh carry the form, linen and numeral together) — the thread count is the material-word read as its numeral" % c_shesh_all, [FX.NONE])
    if q == 'flax':
        return cell('linen_from_bad', M, "Yoma 71b:7-9 (opened) — 'fine linen is flax: R. Yosei b. R. Chanina from בד (28:42's 'linen') — a thing that grows stalk by stalk'; Ravina from Ezek 44:18's 'LINEN TURBANS' — Rav Ashi: a received tradition Ezekiel supported by a verse", [FX.NONE])
    if q == 'ezekiel_run':
        return cell(('פארי פשתים', 'לא יחגרו ביזע'), I, "Ezek 44:17-18 [IMPORT by name] — the prophet's priestly code: linen garments, no wool, 'LINEN TURBANS on their heads and linen breeches on their loins — they shall not gird in sweat' (%s, %s): the turban-word פארי at Exod 39:28 and Ezek 44:18 alone in that form (%s)" % (c_ezek44[0], c_ezek44[1], fmt(c_paarei[0])), [FX.NONE])
    if q == 'bridegroom':
        return cell(('כחתן', 'יכהן', 'פאר'), I, "Isa 61:10 'as a bridegroom PRIESTS himself with a turban' (%s) [IMPORT by name] — the turban-word's other two seats (Isa 61:3, 61:10) carry the priest-verb: the headgear is the office's own metaphor" % (c_isa61,), [FX.NONE])
    if q == 'embroiderer':
        return cell(('מעשה חשב', 'מעשה רקם'), I, "28:39 'a sash you shall make, EMBROIDERER'S WORK' — 'embroiderer's work' at %d seats (the screens 26:36, 27:16 and the sash, with their runs) against the ephod's 'DESIGNER'S work' at %d: two craft grades, the sash the lower (EX26-01's taxonomy)" % (len(c_rokem), len(c_choshev)), [FX.NONE])
    if q == 'sash_materials_added':
        return cell(['שש משזר', 'ותכלת', 'וארגמן', 'ותולעת שני'], I, "the run's 39:29 gives the sash FOUR materials — twined linen, blue, purple, crimson — where the spec's 28:39 gives it NONE (only the craft): the run adds the recipe", [FX.NONE])
    if q == 'sash_no_gold':
        return cell('learned_from_the_sash', M, "Yoma 71b:12 (opened) — the twined-eight settled 'from the SASH: a garment and a thing without gold' — the sash's run-recipe (four colors, no gold) is the analogy's anchor", [FX.NONE])
    if q == 'sons_four':
        return cell(['כתנת', 'אבנטים', 'ומגבעות', 'מכנסי בד'], I, "28:40 'for Aaron's sons make TUNICS, SASHES, and CAPS, for honor and splendor' + 28:42 'linen BREECHES' — the sons' four; the run's 39:27 'the tunics of fine linen, woven work, for Aaron AND FOR HIS SONS' makes the tunics for both in one verse", [FX.NONE])
    if q == 'caps_homograph':
        return cell(11, I, "the caps-word (מגבעת) at %d seats of the Tanakh — four the priests' caps (28:40, 29:9, 39:28, Lev 8:13) and the rest 'from the HILL' (Judg 7:1's hill of Moreh, Isa 2:2's hills, Num 23:9's 'and from the hills'): the headgear and the hill one written form" % len(c_migbaot), [FX.NONE])
    if q == 'run_verb_split':
        return cell((3, 11), I, "the run's making-verbs: singular 'and he made' at %s (ephod, breastplate, robe) and plural 'and they made' at %d seats — the tunics, turban, caps, breeches, sash, and plate all 'THEY made'" % (fmt3(c_vayaas), len(c_vayaasu)), [FX.NONE])
    if q == 'tunic_torah':
        return cell(16, I, "the tunic-word at %d Torah seats — the first garments God made ('coats of skin, and He clothed them', Gen 3:21: %s — 'and He clothed them' at Gen 3:21 and Lev 8:13 alone, %s), Joseph's tunic (Gen 37:3-33), the priests' [IMPORT by name]" % (len(c_kutonet), c_gen3, fmt(c_vayalbishem)), [FX.NONE])
    if q == 'tunic_atones':
        return cell('bloodshed_by_josephs_tunic', M, "Zevachim 88b:6 (opened) — the TUNIC atones for bloodshed: 'they slaughtered a goat and dipped the TUNIC in the blood' (Gen 37:31) — the function assigned by the word's Genesis seat", [FX.NONE])
    if q == 'turban_sash_atone':
        return cell({'turban': 'arrogance_by_height', 'sash': 'the_hearts_thoughts_by_position'}, M, "Zevachim 88b:6-7 + Arakhin 16a:14 (opened) — the TURBAN for arrogance ('a thing of height for height'), the SASH for the heart's thoughts ('where it is') — the two garments without a function clause given one by height and position", [FX.NONE])
    if q == 'no_metal':
        return cell((0, 0), I, "the tunics block (28:39-43; 39:27-29) carries no metal token in spec or run %s — the four garments of the common priest are metal-less: the sheet's 'white garments'" % (GOLD_BLOCK['tunics'],), [FX.NONE])
    if q == 'breeches':
        return cell('nakedness_covered', I, "28:42 'make them LINEN BREECHES to cover the FLESH OF NAKEDNESS, from the loins to the thighs' — 'linen breeches' at %s alone in that form; 'the flesh of nakedness' at %s alone; the breeches-word at %s" % (fmt(c_michnesei), fmt(c_besar_ervah), fmt(c_michnasayim)), ['nakedness_covered'])
    if q == 'nakedness_by_call':
        return cell(ORD_NAKED, P, "CALLED cold_run_ordinances.altar(nakedness) -> %r — 20:26's 'that your NAKEDNESS not be uncovered on it' (the ramp's reason clause; %s) answered on the body by 28:42's breeches: the altar's law and the garment's law on one root [IMPORT, live call]" % (ORD_NAKED, c_ervah20), ['nakedness_covered'])
    if q == 'breeches_first':
        return cell('first_on_last_off', A, "Mishnah Tamid 5:3 — the attendants stripped them of their garments 'and left on them only the BREECHES': the spec's last garment (28:42) is the body's first — Lev 16:4 'linen breeches shall be on his FLESH' [IMPORT by name]", ['nakedness_covered'])
    if q == 'trousers_gap':
        return cell('imported_by_this_is_the_thing', M, VB + "Yoma 5b:4 — R. Yosei b. Chanina: the BREECHES are not written in the investiture portion (Exod 29); 'and THIS is the THING you shall do' (29:1) imports them — the ink's own gap and the clause that supplies it (E4's verse)", ['nakedness_covered'])
    if q == 'breeches_atone':
        return cell('sexual_sin', M, "Zevachim 88b:6 + Arakhin 16a:13 (opened) — the BREECHES atone for sexual sin: 'to cover the flesh of nakedness' — the function the verse itself states", ['nakedness_covered'])
    if q == 'wear_or_die':
        return cell('death_by_heaven', I, "28:43 'they shall be on Aaron and on his sons when they enter the tent of meeting or approach the altar to serve in the Holy, THAT THEY NOT BEAR INIQUITY AND DIE — an everlasting statute for him and his seed after him' — 'that they not bear iniquity' at %s alone; the full perpetuity clause at %s alone; Lev 22:9's parallel %s [IMPORT by name]" % (fmt(c_yisu), fmt(c_chukat), c_lev22_9), ['death_by_heaven'])
    if q == 'wear_or_die_onkelos':
        return cell('condition_of_service_under_perpetuity', M, "Onkelos Exod 28:42-43 — 'that they not bear guilt and DIE' — 'an EVERLASTING STATUTE': the garments as a wear-or-die condition of service (EX28-07)", ['death_by_heaven'])
    if q == 'two_loci':
        return cell(['אהל מועד', 'המזבח'], I, "28:43's two service-sites — ENTERING the tent of meeting OR APPROACHING the altar — the tent and the altar named once each in the spec (both at 28:43 alone): the garments' jurisdiction is the whole public service", ['death_by_heaven'])
    if q == 'great_altar_only':
        return cell('public_altar', M, VB + "Zevachim 119b:18 — the GREAT altar requires a priest and the service garments ('to serve in the Holy', 28:43); the private altar needs neither — the garments' jurisdiction bounded to the public house", [FX.NONE])
    if q == 'whole_entry':
        return cell('until_all_of_him_enters', M, "Zevachim 26a:21 (opened) — 'he is inside and his fringe outside?' — 'WHEN THEY ENTER the tent of meeting (28:43) — until the whole of him enters': the entering clause read for the whole body", [FX.NONE])
    if q == 'stranger':
        return cell('garments_off_priesthood_off', M, VB + "Sanhedrin 83b:13-14 — from where that one lacking vestments who served dies? 'gird them with the sash' (29:9): while their garments are on them their priesthood is on them; garments off, priesthood off — THEY ARE STRANGERS, and a stranger who served dies by Heaven: the office literally worn", ['stranger_barred', 'death_by_heaven'])
    if q == 'lacking_garments_sheet':
        return cell('invalid', A, "Mishnah Zevachim 2:1 — all offerings whose blood was received by a stranger... ONE LACKING GARMENTS... one standing on vessels — INVALID: the wear-or-die statute read from the offering's side", ['disqualified'])
    if q == 'lacking_garments_ink':
        return cell(('לשרת בקדש', 'ולא ישאו עון ומתו'), I, "the row's disqualifier is 28:43's own clause: the garments 'to serve in the Holy' and the sanction 'that they not bear iniquity and die' — 'to serve in the Holy' at six Tanakh seats (28:43, 29:30, 35:19, 39:1, 39:41, Ezek 44:27)", ['disqualified'])
    if q == 'reading_optional':
        return cell('own_white_robe_allowed', A, "Mishnah Yoma 7:1 — the high priest reads 'in the linen garments if he wished, or in a white robe OF HIS OWN': the reading is not service — 28:35 'to serve' and 28:43 'to serve in the Holy' bound the garments to SERVICE, and the row is the ink's negative case", [FX.NONE])
    if q == 'alignment':
        return cell((5, 3, 0, 0), I, "the tunics block: 5 spec, 3 run, NONE matched at the threshold — the run's 39:27-29 reshuffle 28:39-42 (tunics with the sons, the caps and breeches of 28:40/42 in 39:28, the sash with its new recipe) below the token overlap; the investiture verse 28:41 and the statute 28:43 have no run at all", [FX.NONE])
    return cell('no_case', I, '', [FX.NONE])

# ---- F7: THE INVESTITURE VERSE (28:41) — the office's five verbs; its run is Leviticus 8 (E4) ----
def investiture(q):
    if q == 'five_verbs':
        return cell(['והלבשת', 'ומשחת', 'ומלאת', 'וקדשת', 'וכהנו'], I, "28:41 'and you shall CLOTHE them — Aaron your brother and his sons with him — and ANOINT them and FILL THEIR HAND and SANCTIFY them, and they shall SERVE ME as priests' — five verbs in one verse (%s): the whole investiture in the spec's grammar, its run Lev 8 (E4)" % (c_verbs41,), ['invested_office'])
    if q == 'clothe':
        return cell(4, I, "'and you shall clothe' (והלבשת) at %s — the spec (28:41), the investiture spec (29:5), and the erection (40:13-14): Moses the dresser at every seat; the sons 'and he clothed them' (Lev 8:13) with the one other seat, Gen 3:21 [IMPORT by name]" % (fmt(c_vehilbashta),), ['invested_office'])
    if q == 'fill_hand':
        return cell(('ומלאת את ידם', 'ומלא את ידו'), I, "'and you shall fill their hand' at %s alone; 'and he filled his hand' at %s (Lev 21:10's high priest 'who was consecrated to wear the garments') — the idiom's two seats bracket the office [IMPORT by name]" % (fmt(c_fill[0]), fmt(c_fill[1])), ['invested_office'])
    if q == 'fill_hand_onkelos':
        return cell('offer_their_offering', M, "Onkelos Exod 28:1 + 28:3 + 28:4 + 28:41 — 'and you shall FILL THEIR HAND' rendered 'and you shall OFFER THEIR OFFERING': the fill-the-hand idiom decoded as a sacrificial act — office entered by offering (EX28-01)", ['invested_office'])
    if q == 'anoint':
        return cell(2, I, "'and you shall anoint them' at %s — the spec and the erection (40:15); the oil itself is 30:22-33's (E4, OWED)" % (fmt(c_mashachta),), ['consecrated'])
    if q == 'sanctify':
        return cell(3, I, "'and you shall sanctify them' at %s — the priests (28:41), the altar and vessels (30:29), Aaron and his sons again (30:30)" % (fmt(c_kidashta),), ['consecrated'])
    if q == 'lev8_order':
        return cell(LEV8_ORDER, I, "Lev 8:7-9, 13 [IMPORT by name] — the DRESSING order on the body: %s — the tunic first, the sash, the robe, the ephod, the breastplate (with the Urim), the turban, the plate; the sons' tunics, sash, caps — the breeches never named (Yoma 5b:4)" % (LEV8_ORDER,), ['invested_office'])
    if q == 'exod29_order':
        return cell(E29_ORDER, I, "Exod 29:5-6, 8-9 [IMPORT by name; E4's spec] — the investiture's dressing order %s — matches Lev 8's except the sash (29:5 lists tunic, robe, ephod, breastplate; the sash at 29:9 with the sons)" % (E29_ORDER,), ['invested_office'])
    if q == 'three_orders':
        return cell({'making_spec': SPEC_ORDER[:4], 'making_run': RUN_ORDER[-4:], 'dressing': LEV8_ORDER[:4]}, I, "three orders for one set: the spec MAKES ephod-breastplate-robe-plate first, the run makes the plate LAST, the body DRESSES tunic-sash-robe-ephod first — the order of making is not the order of wearing, and Yoma 7:5 lists by rank (the common four, then the added four)", [FX.NONE])
    if q == 'many_garmented':
        return cell(PR_NEZER, P, "CALLED cold_run_priesthood.family(nezer) -> %r — Lev 21:10's two clauses ('on whose head the anointing oil was poured' AND 'who was consecrated to wear THE GARMENTS', %s): the eight garments are the office's SECOND ROUTE when the oil ceased [IMPORT, live call]" % (PR_NEZER, c_lev21), ['invested_office'])
    if q == 'many_garmented_sheet':
        return cell('bull_only', A, "Mishnah Horayot 3:4 + Megillah 1:9 — 'between the priest anointed with the oil and the MANY-GARMENTED only the bull for all the commandments' — the many-garmented named by his garments; equal in the Day's service, the virgin, the widow, the dead, the hair, the rending", ['invested_office'])
    if q == 'judges':
        return cell('judges_and_is_judged', A, "Mishnah Sanhedrin 2:1 — the high priest judges and is judged, testifies and is testified against, barred from the widow, 'from the sanctuary he shall not go out' — the wearer of the breastplate of JUDGMENT is himself a judge (credited; the priesthood engine's cells)", [FX.NONE])
    if q == 'substitute':
        return cell('another_priest_prepared', A, "Mishnah Yoma 1:1 — seven days before the Day another priest is prepared 'lest a disqualification befall him' — the garments transferable (29:29-30 'the holy garments of Aaron shall be his sons' after him', E4)", ['invested_office'])
    if q == 'dresser':
        return cell(('פנחס על המלבוש', 'לשכת פנחס המלביש'), D, "Mishnah Shekalim 5:1 + Middot 1:4 — Pinchas over the vestments; the chamber of Pinchas the dresser at Nicanor's gate — the descendant's standing officer and storeroom for the run's craft (data)", [FX.NONE])
    return cell('no_case', I, '', [FX.NONE])

# ---- F8: THE COMPLETION, THE DELIVERY, THE INSPECTION (39:32-43) --------
def completion(q):
    if q == 'completed':
        return cell('work_completed', I, "39:32 'and all the work of the tabernacle of the tent of meeting WAS COMPLETED' — 'all the work of the tabernacle' at %s alone; 'and it was completed' (ותכל) at %s; the creation's 'and they were finished' (Gen 2:1) and 'and He finished' (Gen 2:2, with Exod 40:33 among %d seats) the same root [IMPORT by name]" % (fmt(c_kol_avodat), fmt(c_vatekhel), len(c_vaykhal)), ['work_completed'])
    if q == 'completed_onkelos':
        return cell('service_completed', M, "Onkelos Exod 39:32 — 'and all the SERVICE of the tabernacle was COMPLETED' — the seventh day's verb at the tabernacle's close (EX39-03's schema)", ['work_completed'])
    if q == 'kekhol':
        return cell([(39, 32), (39, 42)], I, "'ACCORDING TO ALL that the LORD commanded Moses, so they did' at %s — the citation in the 'according to all' form the pointer census does not scan (ככל, not כאשר): two whole-run citations bracketing the manifest" % (fmt3(c_kekhol),), ['inspected_as_commanded'])
    if q == 'brought':
        return cell('to_moses', I, "39:33 'and they BROUGHT the tabernacle to Moses' — the phrase at %s alone: the finished kit carried to the one man who made none of it" % (fmt(c_vayaviu),), [FX.NONE])
    if q == 'deadlock':
        return cell('erection_reserved_for_moses', M, TT + "Pekudei 11:5 + 11:6 + 11:7 — the work done, all sat waiting and the Presence did not come; the wise-hearted raised it and it fell; Moses grieved that he had no share — so the raising was concealed from all hands and the kit CARRIED TO MOSES (39:33 explained), each part shown against the spec item by item; 'busy your hands with it — it will rise of itself'", [FX.NONE])
    if q == 'manifest_count':
        return cell(35, I, "the delivery manifest 39:33-41 — the object-marker (את/ואת) per verse %s = %d items marked: the tent and its hardware, the covers and the veil, the ark with its staves and cover, the table and the bread, the lampstand and its lamps, the golden altar with the oil and the incense, the bronze altar with its grate and the laver, the court, the garments" % (c_manifest, sum(c_manifest)), [FX.NONE])
    if q == 'ark_line':
        return cell(SB_STAVES, P, "39:35 'the ark of the testimony and its STAVES and the cover' — the manifest carries the staves with the ark: CALLED cold_run_sanctuary_build.ark(staves) -> %r (25:15's ban; the staves never leave the ark, even in the hand-off) [IMPORT, live call]" % (SB_STAVES,), ['staves_fixed'])
    if q == 'table_line':
        return cell(SB_BREAD, P, "39:36 'the table, all its vessels, and the bread of the face' — CALLED cold_run_sanctuary_build.table(continually) -> %r: the bread delivered with the table (25:30 'before Me continually') [IMPORT, live call]" % (SB_BREAD,), [FX.NONE])
    if q == 'lamp_line':
        return cell((SB_LAMPS, PR_ARR), P, "39:37 'the pure lampstand, its lamps, THE LAMPS OF THE ARRANGEMENT, all its vessels, and the oil for the light' — 'the lamps of the arrangement' at %s alone: CALLED cold_run_sanctuary_build.menorah(lamps) -> %r and cold_run_priesthood.lamp_table(arrangement) -> %r [IMPORT, live calls]" % (fmt(c_nerot), SB_LAMPS, PR_ARR), [FX.NONE])
    if q == 'e4_line':
        return cell(['המשחה', 'קטרת', 'הסמים', 'הכיר'], I, "39:38-39 'the golden altar, the ANOINTING OIL, the INCENSE of spices... the LAVER and its base' — E4's four tokens in the manifest %s: OWED to cold_run_incense_shekel on the gate's worklist" % ([w for _, w in c_e4],), [FX.NONE])
    if q == 'court_line':
        return cell(SB_HANGINGS, P, "39:40 'the hangings of the court, its pillars and sockets, the screen for the court's gate, its cords and pegs' — CALLED cold_run_sanctuary_build.court(hangings) -> %r cubits (27:9-15's 280) [IMPORT, live call]" % (SB_HANGINGS,), [FX.NONE])
    if q == 'garments_last':
        return cell('last_item', I, "39:41 'the garments of serad to serve in the Holy, THE HOLY GARMENTS for Aaron the priest and his sons' garments to serve as priest' — the manifest's LAST line is this span's own product; 'to serve as priest' (לכהן) the span's fifth priest-verb", [FX.NONE])
    if q == 'moses_saw':
        return cell('inspected_as_commanded', I, "39:43 'and Moses SAW all the work, and BEHOLD they had done it as the LORD commanded, so they had done' — 'and Moses saw' at %s (the calf and the tabernacle: the two things Moses saw); 'all the work' with Hiram's (1 Kgs 7:40); 'and behold they had done' with Gen 33:1 [IMPORT by name]" % (fmt(c_vayar),), ['inspected_as_commanded'])
    if q == 'stamp_without_moses':
        return cell((39, 43), I, "the inspection's stamp 'as the LORD commanded' lacks 'Moses' — Moses is the inspector; the seven with 'Moses' (%s) plus this eighth; fourteen in 39-40 in all (%d)" % (fmt3(c_stamp7), len(c_stamp_39_40)), ['inspected_as_commanded'])
    if q == 'inspection_onkelos':
        return cell('saw_behold_blessed', M, "Onkelos Exod 39:42-43 — 'and Moses SAW all the work... and BEHOLD they had done it as the LORD commanded... and Moses BLESSED them' — the acceptance test passed and the seventh day's second verb (EX39-05)", ['inspected_as_commanded', 'blessed_the_people'])
    if q == 'blessed':
        return cell(4, I, "39:43 'and Moses BLESSED them' — 'and he blessed them' at %s: the creation's three blessings (the creatures, the man, Adam's line) and Moses' — the fourth seat of the phrase in the Tanakh is the tabernacle's; 'and Moses blessed them' once (%s)" % (fmt(c_vayvarekh), fmt(c_vayvarekh_m)), ['blessed_the_people'])
    if q == 'blessing_text':
        return cell({'sages': 'Deut 1:11', 'R_Meir': 'may_the_presence_rest_in_the_work_of_your_hands', 'answer': 'Ps 90:17'}, M, TT + "Pekudei 11:9 — the blessing's text filled in: the sages give 'may the LORD add to you' (Deut 1:11); R. Meir — 'may the Presence REST in the work of your hands', answered 'let the pleasantness of the LORD be upon us' (Ps 90:17)", ['blessed_the_people'])
    if q == 'countersignature':
        return cell('name_on_every_item', M, TT + "Pekudei 11:9 + 11:10 — the refrain written again and again because they suspected Moses: 'since you criticized him, I WRITE MY NAME on every single item I commanded him' — the stamp as the divine countersignature on each audit line", ['inspected_as_commanded'])
    if q == 'six_months':
        return cell({'building': 3, 'folded': 3}, M, "Midrash Tanchuma Buber, Pekudei 6:1 — R. Chanina: six months occupied — three building, three folded away unassembled; the murmurers ended carrying it to Moses", [FX.NONE])
    if q == 'ken_asu':
        return cell(15, I, "'so they did' (כן עשו) at %d seats of the Tanakh — three in this chapter's close (39:32, 42, 43): the obedience formula of Exod 7:6, 12:28, 12:50 and Numbers' censuses" % c_ken_asu, ['inspected_as_commanded'])
    return cell('no_case', I, '', [FX.NONE])

# ---- F9: THE SCENE — the orders, the alignment, the world engine ---------
def law_vestments(event, world):
    """The vestments' daemon: consumes the run's recorded acts and writes the ledger — never emits an event."""
    k, subj, src = event['kind'], event['subject'], event['case_source']
    E = lambda eff, s, cp=None: {'effect': eff, 'subject': s, 'counterparty': cp, 'amount': None, 'due': None, 'source_law': 'F%s' % event.get('law', '9'), 'case_source': src}
    if k == 'garment_made':
        g = event['garment']
        if g == 'breastplate': return [E('breastplate_fixed', 'the-ephod')]
        if g == 'robe': return [E('robe_uncut', 'the-robe')]
        if g == 'breeches': return [E('nakedness_covered', 'the-priest')]
        return []      # the ephod, plate, tunics, turban, caps, sash: made, no ledger entry until worn (E4's investiture)
    if k == 'work_completed': return [E('work_completed', 'the-tabernacle')]
    if k == 'delivered': return []
    if k == 'inspected': return [E('inspected_as_commanded', 'the-work'), E('blessed_the_people', 'the-people', 'moses')]
    return []

def scene():
    with contextlib.redirect_stdout(io.StringIO()):
        w = WE.World(era='the vestments (clock unit: days)')
        w.laws = [law_vestments]
        for g, src in (('ephod', 'Exod 39:2-7'), ('breastplate', 'Exod 39:8-21'), ('robe', 'Exod 39:22-26'), ('tunics', 'Exod 39:27'), ('turban_caps', 'Exod 39:28'),
                       ('breeches', 'Exod 39:28'), ('sash', 'Exod 39:29'), ('plate', 'Exod 39:30-31')):
            w.submit({'kind': 'garment_made', 'subject': 'the-craftsmen', 'garment': g, 'case_source': src, 'law': '9'})
        w.submit({'kind': 'work_completed', 'subject': 'the-tabernacle', 'case_source': 'Exod 39:32', 'law': '8'})
        w.submit({'kind': 'delivered', 'subject': 'the-people', 'case_source': 'Exod 39:33-41', 'law': '8'})
        w.submit({'kind': 'inspected', 'subject': 'moses', 'case_source': 'Exod 39:42-43', 'law': '8'})
    n = lambda eid, eff: len([e for e in w.entity(eid).ledger if e['effect'] == eff])
    events = len([l for l in w.log if l[0] == 'EVENT'])
    return (n('the-ephod', 'breastplate_fixed'), n('the-robe', 'robe_uncut'), n('the-priest', 'nakedness_covered'), n('the-tabernacle', 'work_completed'),
            n('the-work', 'inspected_as_commanded'), n('the-people', 'blessed_the_people'),
            n('the-priest', 'names_borne'), n('the-priest', 'judgment_borne'), n('the-priest', 'entry_announced'), n('the-priest', 'plate_propitiates'), events)
SCENE = scene()
def build(q):
    if q == 'spec_order':
        return cell(SPEC_ORDER, I, "the spec's order of first mention from 28:6: %s — the ephod, the breastplate, the robe, the PLATE, then the turban (first named at 28:37 as the plate's seat), the sash and tunic (28:39), the caps (28:40), the breeches (28:42)" % (SPEC_ORDER,), [FX.NONE])
    if q == 'run_order':
        return cell(RUN_ORDER, I, "the run's order of first mention from 39:2: %s — the same three first, then the tunic, breeches, caps, turban, sash — and THE PLATE LAST" % (RUN_ORDER,), [FX.NONE])
    if q == 'plate_moves':
        return cell((3, 8), I, "the plate's position: fourth in the spec (index %d), ninth in the run (index %d) — the one garment the run relocates; no verse of either stratum says why (the run groups the gold-bearing three, then the white four, then the plate)" % (SPEC_ORDER.index('plate'), RUN_ORDER.index('plate')), [FX.NONE])
    if q == 'dressing_order':
        return cell(LEV8_ORDER, I, "the third order — the BODY's (Lev 8:7-9, 13): %s — neither the spec's nor the run's: the tunic under everything, the plate on top; the making and the wearing are two programs" % (LEV8_ORDER,), [FX.NONE])
    if q == 'alignment':
        return cell(A_TOTAL, I, "the alignment engine: (spec verses, run verses, spec matched, run matched, dropped) = %s — every run garment-verse (39:1-31) aligned to its block's spec verse by normalized token overlap at threshold 0.3; the completion (39:32-43) has no spec in Exod 28" % (A_TOTAL,), [FX.NONE])
    if q == 'dropped':
        return cell(A_DROPPED, I, "the twenty-one spec verses with no run counterpart: %s — the office (28:1-5: the call, the purpose, the workforce, the list, the materials), the stones' engraving folded (28:9-11, 13-14), the names and the Urim borne (28:29-30), the bells' spec and the sound (28:33, 35), the plate's cord and function (28:37-38), the tunics reshuffled (28:39-40), the investiture (28:41), the breeches and the statute (28:42-43)" % (A_DROPPED,), [FX.NONE])
    if q == 'dropped_kinds':
        return cell('function_clauses_and_the_office', I, "what the run drops is of one kind again (E2's finding at the vestments): every clause that says what a garment DOES (bears, is heard, propitiates, that he not die), every Presence-clause ('before the LORD' five to none), the investiture, and the office's call — the run is the making alone; the wearing is Lev 8's run of Exod 29 (E4)", [FX.NONE])
    if q == 'numerals_equal':
        return cell(A_NUM_EQ, I, "the blocks whose numeral multisets match: %s — the ephod's differ by 'six and six' (28:10, the run drops the count), the breastplate's by the second 'doubled', the tunics' by the five 'fine linen'" % (A_NUM_EQ,), [FX.NONE])
    if q == 'verbs':
        return cell({'spec_you_shall_make': 12, 'spec_they_shall_make': 3, 'spec_you_shall_make_2': 5, 'run_and_he_made': 3, 'run_and_they_made': 11}, I, "the spec's 'and you shall make' %d, 'and they shall make' %d, 'you shall make' %d; the run's 'and he made' %d and 'and they made' %d" % (len(c_veasita), len(c_veasu), len(c_taaseh), len(c_vayaas), len(c_vayaasu)), [FX.NONE])
    if q == 'metals_colors':
        return cell({'gold': (17, 15), 'blue': (8, 10), 'twined': (3, 6), 'Aaron': (16, 3)}, I, "spec vs run: gold-tokens %s, blue-tokens %s, 'twined' %s, 'Aaron' %s — the run names the wearer three times where the spec names him sixteen: the run has no wearer" % (c_gold, c_tekhelet, c_mashzar, c_aharon), [FX.NONE])
    if q == 'second_homograph':
        return cell(6, I, "'the second' (השני, השנית) at %d seats of the span — the crimson-word 'שני' (tolaat SHANI) and the ordinal 'second' share their consonants: the second stone, the second row, and the crimson thread are one written form" % c_shani, [FX.NONE])
    if q == 'world':
        return cell(SCENE, I, "THE SCENE on the world engine: eight garments made — the breastplate writes 'fixed' on the ephod, the robe 'uncut', the breeches 'nakedness covered', the rest nothing — the work completed, the kit delivered (no law), the inspection writing 'as commanded' and Moses' blessing; the four USE entries the spec promises (names borne, judgment borne, entry announced, plate propitiates) NOT fired: the run makes and never wears — (fixed, uncut, covered, completed, inspected, blessed, names, judgment, entry, plate, events)", ['breastplate_fixed', 'robe_uncut', 'nakedness_covered', 'work_completed', 'inspected_as_commanded', 'blessed_the_people'])
    return cell('no_case', I, '', [FX.NONE])

# ---- (2) the answer sheet — the Mishnah rows as TEST DATA (verified by their own tokens) ----
def load(t):
    d = json.load(open((_ROOT + '/Data/mishnah_%s_he.json') % t))
    return d['text'] if isinstance(d, dict) and 'text' in d else d
SHELF = {t: load(t.lower()) for t in ('Yoma', 'Zevachim', 'Horayot', 'Megillah', 'Sotah', 'Sanhedrin', 'Tamid', 'Shekalim', 'Middot', 'Kelim', 'Chagigah', 'Shabbat')}
def mrow(book, ch, m, must):
    txt = strip(SHELF[book][ch - 1][m - 1])
    assert must in txt, 'answer-sheet check failed: %r not in Mishnah %s %d:%d' % (must, book, ch, m)
SHEET = [
    ('Yoma', 7, 1, 'בוץ'), ('Yoma', 7, 3, 'זהב'), ('Yoma', 7, 4, 'לבן'), ('Yoma', 7, 5, 'בשמנה'), ('Yoma', 3, 4, 'זהב'), ('Yoma', 3, 6, 'הפרוה'), ('Yoma', 3, 7, 'פלוסין'), ('Yoma', 1, 1, 'פלהדרין'),
    ('Zevachim', 2, 1, 'בגדים'), ('Zevachim', 8, 12, 'הציץ'), ('Horayot', 3, 4, 'בבגדים'), ('Horayot', 3, 5, 'פורם'), ('Megillah', 1, 9, 'בגדים'), ('Sotah', 9, 12, 'ותמים'),
    ('Sanhedrin', 2, 1, 'באלמנה'), ('Tamid', 5, 3, 'מכנסים'), ('Shekalim', 5, 1, 'המלבוש'), ('Shekalim', 5, 2, 'גזברין'), ('Middot', 1, 4, 'המלביש'), ('Kelim', 1, 9, 'הקדשים'),
    ('Chagigah', 3, 8, 'הזהב'), ('Shabbat', 6, 9, 'בזוגין'), ('Shabbat', 10, 6, 'צפרניו'),
]
for b, ch, m, must in SHEET:
    mrow(b, ch, m, must)
print('answer sheet: %d Mishnah rows verified by their own tokens (Yoma 7 whole, Zevachim 2 whole with the topic and link rows — the vestments docket)' % len(SHEET))

TESTS = [
 # ---- THE OFFICE AND THE SET (28:1-5; 39:1) ----
 ('Exod 28:1, 3, 4 — "to serve Me as priest" at three seats', office('priest_phrase'), 3),
 ('Onkelos Exod 28:1 + 28:3 + 28:4 + 28:41 — to SERVE BEFORE ME', office('serve_before_me'), 'service_before_the_presence'),
 ('Exod 28:1 — the four sons named', office('four_sons'), ['נדב', 'ואביהוא', 'אלעזר', 'ואיתמר']),
 ('Exod 28:2, 28:40 — "for honor and for splendor" at two seats', office('purpose'), 2),
 ('Megillah 12a:7 — Ahasuerus wore them (the splendor-word)', office('purpose_read'), 'ahasuerus_wore_them'),
 ('Exod 28:3 — the wise of heart shall make', office('wise_hearted'), 'they_make'),
 ('Exod 28:4 — the list names six', office('six_nouns'), 6),
 ('Exod 28:4 + 28:36 + 28:42 — six plus the plate plus the breeches = eight', office('eight'), 8),
 ('Mishnah Yoma 7:5 — the eight in the sheet\'s order', office('eight_sheet'), ['כתנת', 'מכנסים', 'מצנפת', 'אבנט', 'חשן', 'אפוד', 'מעיל', 'ציץ']),
 ('Exod 28:40 + 28:42 — the sons\' four', office('four_common'), 4),
 ('the gold-bearing blocks = Yoma 7:5\'s four the high priest adds', office('gold_sets'), ['breastplate', 'ephod', 'plate', 'robe']),
 ('Mishnah Yoma 3:4, 3:6, 7:3, 7:4 — gold, white, gold, white, gold, own', office('gold_white_sheet'), ['gold', 'white', 'gold', 'white', 'gold', 'own']),
 ('Lev 16:4 — "linen" four times: the white set', office('linen_lev16'), 4),
 ('CALLED cold_run_yoma.service_order — the linen donned at 16:4', office('yoma_linen_by_call'), 'linen garments donned (immersed first)'),
 ('Exod 28:5 — the five materials with the article', office('materials_five'), ['הזהב', 'התכלת', 'הארגמן', 'תולעת השני', 'השש']),
 ('Bava Batra 8b:9 — "and THEY shall take": two collectors', office('they_take'), 'two_collectors'),
 ('Mishnah Shekalim 5:2 — three, seven, two', office('two_collectors_sheet'), (3, 7, 2)),
 ('"holy garments" bare at three seats, articled at six', office('holy_garments'), (3, 6)),
 ('Exod 39:1 — "garments of serad" at four seats', office('serad'), 4),
 ('Exod 39:1 — from the blue, the purple, the crimson', office('from_the_stock'), ['התכלת', 'והארגמן', 'ותולעת השני']),
 ('Mishnah Yoma 3:7 — the garments\' value from the public (data)', office('garment_value'), {'R_Meir': (12, 800), 'sages': (18, 12, 30), 'source': 'public', 'surplus': 'his_own'}),
 ('Shabbat 31a:7 — the convert heard 28:4 read aloud', office('convert'), 'the_list_read_aloud'),
 ('Exod 39:1 — the first stamp', office('run_stamp_first'), (39, 1)),
 ('the spec 595 tokens, the run 568', office('tokens'), (595, 568)),
 # ---- THE EPHOD AND ITS STONES (28:6-14; 39:2-7) ----
 ('Exod 28:6 — five materials, designer\'s work', ephod('materials'), ['זהב', 'תכלת', 'וארגמן', 'תולעת שני', 'ושש משזר']),
 ('Exod 28:6 "they shall make" vs 39:2 "he made"', ephod('they_vs_he'), ('ועשו', 'ויעש')),
 ('Exod 28:7 = 39:4 — two shoulder-pieces', ephod('shoulders'), 2),
 ('Exod 28:8 "of it shall be" vs 39:5 "of it it is"', ephod('band_is'), ('ממנו יהיה', 'ממנו הוא')),
 ('Exod 28:9 — two onyx stones (the word at fourteen seats)', ephod('two_stones'), 2),
 ('Exod 28:10 — six and six, in their birth order (a hapax)', ephod('six_six'), (6, 6)),
 ('Sotah 36a:12-13 — Judah advanced; fifty letters', ephod('six_six_talmud'), {'first_stone': 'judah_advanced', 'second': 'by_birth', 'letters': (50, 25)}),
 ('signet engravings at six seats — three objects, spec and run', ephod('engravings'), 6),
 ('Onkelos Exod 28:11 + 28:21 + 28:36 — clear script', ephod('clear_script'), 'ketav_mefarash'),
 ('Exod 28:11 — the engraver a parameter; the shamir (EX28-12)', ephod('engraver'), 'shamir'),
 ('"and Aaron shall bear" at four seats', ephod('remembrance'), 4),
 ('Exod 39:7 — the run keeps "remembrance", drops the bearing', ephod('remembrance_run'), True),
 ('Exod 28:14 — cord-work at three seats', ephod('settings_chains'), 3),
 ('Exod 39:3 — the process verse: four hapaxes', ephod('process_verse'), 4),
 ('Onkelos Exod 39:1-7 — they beat and cut', ephod('process_onkelos'), 'beat_and_cut'),
 ('Yoma 72a:6 — the gold threads four, from 39:3', ephod('gold_thread_count'), 4),
 ('Yoma 72a:7 — one gold thread per color, from 39:3', ephod('gold_thread_placement'), 'one_gold_thread_per_color'),
 ('Yoma 72a:5 — the breastplate and ephod twenty-eight', ephod('thread_28'), 28),
 ('move M-22 in a third form — the run supplies the parameter', ephod('run_teaches_parameter'), 'the_parameter_supplied'),
 ('the ephod-word at forty seats; the linen ephod at four', ephod('ephod_elsewhere'), 40),
 ('Zevachim 88b:7 — the ephod atones for idolatry', ephod('ephod_atones'), 'idolatry'),
 ('Exod 39:5, 39:7 — two stamps', ephod('stamps'), [(39, 5), (39, 7)]),
 ('the ephod block aligned (9, 6, 4, 5)', ephod('alignment'), (9, 6, 4, 5)),
 # ---- THE BREASTPLATE OF JUDGMENT (28:15-30; 39:8-21) ----
 ('"breastplate of judgment" bare and articled', breastplate('name'), ('חשן משפט', 'חשן המשפט')),
 ('the breastplate-word at seventeen seats, all sanctuary', breastplate('word_seats'), 17),
 ('Exod 28:15 — like the work of the ephod: an internal pointer', breastplate('like_the_ephod'), 'internal_pointer'),
 ('Yoma 71b:13 — "you shall make IT": for this alone', breastplate('for_this_alone'), 'taasenu_this_not_another'),
 ('Yoma 71b:14 — all makings equal', breastplate('equal_threads'), 'all_makings_equal'),
 ('Exod 28:16 — square, doubled, a span', breastplate('square_span'), ('רבוע', 'כפול', 'זרת')),
 ('Menachot 11a:5 — the span a hand measure', breastplate('span_parameter'), 'a_hand_measure'),
 ('Exod 28:17-20 — four rows of three', breastplate('four_rows'), [3, 3, 3, 3]),
 ('Exod 39:10-13 — the names equal the spec\'s', breastplate('names_equal'), True),
 ('four stone-names are homographs of common words', breastplate('homographs'), {'אדם': 492, 'לשם': 36, 'שבו': 54, 'תרשיש': 25}),
 ('Megillah 12b:10 — Tarshish the minister is the stone', breastplate('tarshish_read'), 'the_minister_is_the_stone'),
 ('Ezek 28:13 — nine of twelve; the third row missing', breastplate('ezekiel_nine'), ['לשם', 'שבו', 'אחלמה']),
 ('Exod 28:21 — twelve, each on his name', breastplate('twelve_names'), 12),
 ('Exod 28:20 — in their fullness: uncut (EX28-12)', breastplate('fullness'), 'uncut'),
 ('the rings seven and seven', breastplate('rings_cords'), (7, 7)),
 ('Exod 28:28 — it shall not be detached (two seats)', breastplate('not_detached'), 'breastplate_fixed'),
 ('Onkelos Exod 28:28 + 28:32 — not detached, not torn', breastplate('not_detached_onkelos'), 'la_yitparek'),
 ('Yoma 72a:9 + Makkot 22a:8 — the detacher flogged', breastplate('lashes'), 'lashes'),
 ('Yoma 72a:8-9 — "not", not "so that not"', breastplate('design_objection'), 'lo_not_shelo'),
 ('CALLED cold_run_sanctuary_build.ark(staves) — the twin ban', breastplate('staves_by_call'), 'never_removed'),
 ('Exod 28:29 — the names on his heart', breastplate('bears_names'), 'on_his_heart'),
 ('Exod 28:30 — the Urim and the Tummim (two common words)', breastplate('urim'), ('האורים', 'התמים')),
 ('Exod 28:30 — the judgment borne', breastplate('judgment_borne'), 'judgment_borne'),
 ('Onkelos Exod 28:15 + 28:29-30 — the breastplate of JUDGMENT', breastplate('judgment_onkelos'), 'dina'),
 ('Mishnah Yoma 7:5 — consulted only for the king, the court, the public', breastplate('urim_authorization'), ['king', 'court', 'public_need']),
 ('Mishnah Sotah 9:12 — ceased with the first prophets', breastplate('urim_end'), 'first_prophets'),
 ('"continually" at three seats of the spec', breastplate('tamid'), 3),
 ('"before the LORD" five in the spec, none in the run', breastplate('before_the_lord'), (5, 0)),
 ('Zevachim 88b:7 — the breastplate atones for judgments', breastplate('atones_judgments'), 'judgments'),
 ('the breastplate block aligned one for one; 28:29-30 dropped', breastplate('alignment'), (16, 14, 14, ['28:29', '28:30'])),
 # ---- THE ROBE AND ITS BELLS (28:31-35; 39:22-26) ----
 ('Exod 28:31 — wholly blue at three seats', robe('wholly_blue'), 3),
 ('Zevachim 88b:2 — the baraita cites 39:22 for the spec', robe('run_cited_for_spec'), '39:22_cited'),
 ('Menachot 42b:13 — a test-dyeing invalid', robe('dye_test'), 'test_dyeing_invalid'),
 ('Yoma 71b:15-72a:3 — the robe twelve; a vessel not an ornament', robe('twelve_threads'), 12),
 ('Exod 28:32 — woven work, the coat of mail, not torn', robe('collar'), ('מעשה ארג', 'תחרא', 'לא יקרע')),
 ('Yoma 72b:3 — woven, not needle; the sleeves', robe('woven_not_needle'), 'woven_with_sleeve_exception'),
 ('Yoma 72a:8 — the tearer flogged; the particle test', robe('tear_lashes'), 'lashes'),
 ('Zevachim 95a:4 — laundered in less than three by three', robe('launder'), 'less_than_three_by_three'),
 ('CALLED cold_run_priesthood.family(hair_rend) — Lev 21:10\'s rending', robe('rend_by_call'), {'R._Yehuda': 'not_at_all', 'R._Meir': 'not_for_his_dead', 'geometry': 'high_priest_below_commoner_above'}),
 ('the bell-word at four seats, all in this span', robe('bells'), 4),
 ('Zevachim 88b:3 — seventy-two / thirty-six (data)', robe('bell_count'), {'sages': 72, 'R_Dosa': 36}),
 ('Exod 39:24 — the run adds "twined"', robe('twined_added'), True),
 ('Yoma 71b:10 — twined eight, from 39:24', robe('twined_eight'), 8),
 ('Exod 28:35 — its sound shall be heard, that he not die', robe('sound'), 'entry_announced'),
 ('Onkelos Exod 28:33-35 — the audible entry with a death sanction', robe('sound_onkelos'), 'audible_entry_with_death_sanction'),
 ('the run drops 28:33 and 28:35 — the sound and the death', robe('run_drops_sound'), ['28:33', '28:35']),
 ('Yoma 44b:16 — the sounding ring', robe('sounding_ring'), 'ring_on_the_pan'),
 ('Sotah 9b:22 — the Presence rang before Samson like a bell', robe('samson_bell'), 'the_presence_rang'),
 ('Zevachim 88b:8 — the robe atones for evil speech', robe('atones_speech'), 'evil_speech'),
 ('Exod 39:22 — the run\'s third singular', robe('run_singular'), (39, 22)),
 ('the robe block aligned (5, 5, 3, 4)', robe('alignment'), (5, 5, 3, 4)),
 # ---- THE PLATE (28:36-38; 39:30-31) ----
 ('the plate-word at seven seats — the flower\'s word', plate('word'), 7),
 ('"holy to the LORD" at sixteen seats, the horses\' bells among them', plate('holy_to_the_lord'), 16),
 ('Exod 28:36 "engrave" vs 39:30 "they wrote a writing"', plate('engrave_vs_write'), ('ופתחת', 'ויכתבו')),
 ('Gittin 20b:1 — the plate\'s letters embossed', plate('writing_read'), 'embossed_from_behind'),
 ('Exod 39:30 — "the holy crown" at three seats, none in the spec', plate('holy_crown'), 3),
 ('Onkelos Exod 39:27-31 — the diadem, the holy crown', plate('crown_onkelos'), 'kelila_dekudsha'),
 ('Exod 28:37 "the front" vs 39:31 "above"', plate('blue_cord'), ('על המצנפת', 'מלמעלה')),
 ('Chullin 138a:6 — the wool cap under the plate', plate('wool_cap'), 'cap_between'),
 ('the forehead at four seats, Goliath\'s among them', plate('forehead'), 4),
 ('Exod 28:38 — bears the iniquity of the holy things, for acceptance', plate('bears_iniquity'), 'plate_propitiates'),
 ('Onkelos Exod 28:38 — atones for offering-defects', plate('bears_onkelos'), 'atones_offering_defects'),
 ('Menachot 25a:2 + Yoma 7a:10 — which iniquity: impurity', plate('which_iniquity'), 'impurity'),
 ('Mishnah Zevachim 8:12 — for the impure, not for what went out', plate('scope_sheet'), {'impure': 'propitiates', 'went_out': 'does_not'}),
 ('Yoma 7b:4-5 — the frontplate\'s state machine (EX28-13)', plate('state_machine'), {'broken': 'none', 'on_peg': {'R_Yehuda': 'no', 'R_Shimon': 'yes'}}),
 ('Yevamot 60b:13 — acceptance, not calamity', plate('polarity'), 'acceptance_not_calamity'),
 ('Shabbat 12a:4 — the attention a-fortiori', plate('attention'), 'touch_tefillin_every_hour'),
 ('"for acceptance" at eleven seats — the offerings\' word', plate('leratzon_word'), 11),
 ('Zevachim 88b:8 — the plate atones for brazenness', plate('atones_brazenness'), 'brazenness'),
 ('the run makes the plate last', plate('run_last'), ('plate', 8)),
 ('the plate block drops 28:37-38', plate('run_drops'), ['28:37', '28:38']),
 # ---- THE TUNIC, TURBAN, SASH; THE SONS' FOUR; THE BREECHES (28:39-43; 39:27-29) ----
 ('Exod 28:4, 28:39 — checkered (two hapaxes)', tunics('checkered'), ('תשבץ', 'ושבצת')),
 ('"fine linen" twice in the spec\'s verse, five times in the run\'s', tunics('shesh_spec_vs_run'), (2, 5)),
 ('Yoma 71b:6 — the sixfold thread from the run\'s five tokens', tunics('sixfold'), 6),
 ('"fine linen" IS "six" — the homograph', tunics('shesh_is_six'), 'homograph'),
 ('Yoma 71b:7-9 — flax from "linen"; Ezekiel\'s support', tunics('flax'), 'linen_from_bad'),
 ('Ezek 44:17-18 — linen turbans, not in sweat', tunics('ezekiel_run'), ('פארי פשתים', 'לא יחגרו ביזע')),
 ('Isa 61:10 — as a bridegroom priests himself with a turban', tunics('bridegroom'), ('כחתן', 'יכהן', 'פאר')),
 ('Exod 28:39 — embroiderer\'s work against designer\'s work', tunics('embroiderer'), ('מעשה חשב', 'מעשה רקם')),
 ('Exod 39:29 — the run adds the sash\'s four materials', tunics('sash_materials_added'), ['שש משזר', 'ותכלת', 'וארגמן', 'ותולעת שני']),
 ('Yoma 71b:12 — learned from the sash', tunics('sash_no_gold'), 'learned_from_the_sash'),
 ('Exod 28:40, 42 — the sons\' four', tunics('sons_four'), ['כתנת', 'אבנטים', 'ומגבעות', 'מכנסי בד']),
 ('the caps-word at eleven seats — the hill', tunics('caps_homograph'), 11),
 ('the run\'s verbs: three singular, eleven plural', tunics('run_verb_split'), (3, 11)),
 ('the tunic-word at sixteen Torah seats — Gen 3:21 first', tunics('tunic_torah'), 16),
 ('Zevachim 88b:6 — the tunic atones for bloodshed (Joseph\'s)', tunics('tunic_atones'), 'bloodshed_by_josephs_tunic'),
 ('Zevachim 88b:6-7 — the turban and the sash', tunics('turban_sash_atone'), {'turban': 'arrogance_by_height', 'sash': 'the_hearts_thoughts_by_position'}),
 ('the tunics block: no metal token', tunics('no_metal'), (0, 0)),
 ('Exod 28:42 — linen breeches to cover the flesh of nakedness', tunics('breeches'), 'nakedness_covered'),
 ('CALLED cold_run_ordinances.altar(nakedness) — 20:26\'s clause', tunics('nakedness_by_call'), 'the_ramps_reason'),
 ('Mishnah Tamid 5:3 — the breeches first on, last off', tunics('breeches_first'), 'first_on_last_off'),
 ('Yoma 5b:4 — the trousers imported by "this is the thing"', tunics('trousers_gap'), 'imported_by_this_is_the_thing'),
 ('Zevachim 88b:6 — the breeches atone for sexual sin', tunics('breeches_atone'), 'sexual_sin'),
 ('Exod 28:43 — that they not bear iniquity and die; an everlasting statute', tunics('wear_or_die'), 'death_by_heaven'),
 ('Onkelos Exod 28:42-43 — wear or die, forever', tunics('wear_or_die_onkelos'), 'condition_of_service_under_perpetuity'),
 ('Exod 28:43 — the tent and the altar', tunics('two_loci'), ['אהל מועד', 'המזבח']),
 ('Zevachim 119b:18 — the great altar only', tunics('great_altar_only'), 'public_altar'),
 ('Zevachim 26a:21 — until the whole of him enters', tunics('whole_entry'), 'until_all_of_him_enters'),
 ('Sanhedrin 83b:13-14 — garments off, priesthood off: strangers', tunics('stranger'), 'garments_off_priesthood_off'),
 ('Mishnah Zevachim 2:1 — one lacking garments: invalid', tunics('lacking_garments_sheet'), 'invalid'),
 ('Exod 28:43 — the row\'s disqualifier in the ink', tunics('lacking_garments_ink'), ('לשרת בקדש', 'ולא ישאו עון ומתו')),
 ('Mishnah Yoma 7:1 — the reading in his own robe: not service', tunics('reading_optional'), 'own_white_robe_allowed'),
 ('the tunics block: none matched at the threshold', tunics('alignment'), (5, 3, 0, 0)),
 # ---- THE INVESTITURE VERSE (28:41) ----
 ('Exod 28:41 — five verbs', investiture('five_verbs'), ['והלבשת', 'ומשחת', 'ומלאת', 'וקדשת', 'וכהנו']),
 ('"and you shall clothe" at four seats — Moses the dresser', investiture('clothe'), 4),
 ('"fill their hand" / "filled his hand" — the idiom\'s two seats', investiture('fill_hand'), ('ומלאת את ידם', 'ומלא את ידו')),
 ('Onkelos Exod 28:41 — offer their offering', investiture('fill_hand_onkelos'), 'offer_their_offering'),
 ('"and you shall anoint them" at two seats', investiture('anoint'), 2),
 ('"and you shall sanctify them" at three seats', investiture('sanctify'), 3),
 ('Lev 8:7-9, 13 — the dressing order on the body', investiture('lev8_order'), ['tunic', 'sash', 'robe', 'ephod', 'breastplate', 'turban', 'plate', 'caps']),
 ('Exod 29:5-9 — the investiture\'s order', investiture('exod29_order'), ['tunic', 'robe', 'ephod', 'breastplate', 'turban', 'sash', 'caps']),
 ('three orders for one set', investiture('three_orders'), {'making_spec': ['ephod', 'breastplate', 'robe', 'plate'], 'making_run': ['caps', 'turban', 'sash', 'plate'], 'dressing': ['tunic', 'sash', 'robe', 'ephod']}),
 ('CALLED cold_run_priesthood.family(nezer) — the many-garmented', investiture('many_garmented'), 'the_crown_of_the_oil_the_many_garmented_included'),
 ('Mishnah Horayot 3:4 + Megillah 1:9 — only the bull', investiture('many_garmented_sheet'), 'bull_only'),
 ('Mishnah Sanhedrin 2:1 — judges and is judged', investiture('judges'), 'judges_and_is_judged'),
 ('Mishnah Yoma 1:1 — another priest prepared', investiture('substitute'), 'another_priest_prepared'),
 ('Mishnah Shekalim 5:1 + Middot 1:4 — Pinchas the dresser (data)', investiture('dresser'), ('פנחס על המלבוש', 'לשכת פנחס המלביש')),
 # ---- THE COMPLETION, THE DELIVERY, THE INSPECTION (39:32-43) ----
 ('Exod 39:32 — and all the work was completed (Gen 2\'s verb)', completion('completed'), 'work_completed'),
 ('Onkelos Exod 39:32 — the service completed', completion('completed_onkelos'), 'service_completed'),
 ('Exod 39:32, 39:42 — "according to all" twice', completion('kekhol'), [(39, 32), (39, 42)]),
 ('Exod 39:33 — brought to Moses (a hapax)', completion('brought'), 'to_moses'),
 ('Tanchuma Pekudei 11:5-7 — the erection deadlock', completion('deadlock'), 'erection_reserved_for_moses'),
 ('the manifest\'s thirty-five marked items', completion('manifest_count'), 35),
 ('CALLED cold_run_sanctuary_build.ark(staves) — 39:35\'s staves', completion('ark_line'), 'never_removed'),
 ('CALLED cold_run_sanctuary_build.table(continually) — 39:36\'s bread', completion('table_line'), 'lifnei_tamid'),
 ('CALLED sanctuary_build.menorah(lamps) + priesthood.lamp_table(arrangement) — 39:37', completion('lamp_line'), (7, {'rows': 2, 'per_row': 6, 'pinned_by': 'three_verses'})),
 ('Exod 39:38-39 — E4\'s four tokens in the manifest (OWED)', completion('e4_line'), ['המשחה', 'קטרת', 'הסמים', 'הכיר']),
 ('CALLED cold_run_sanctuary_build.court(hangings) — 39:40', completion('court_line'), 280),
 ('Exod 39:41 — the garments the manifest\'s last item', completion('garments_last'), 'last_item'),
 ('Exod 39:43 — and Moses saw all the work', completion('moses_saw'), 'inspected_as_commanded'),
 ('Exod 39:43 — the eighth stamp, without Moses', completion('stamp_without_moses'), (39, 43)),
 ('Onkelos Exod 39:42-43 — saw, behold, blessed', completion('inspection_onkelos'), 'saw_behold_blessed'),
 ('"and he blessed them" at four seats — the creation\'s three and Moses\'', completion('blessed'), 4),
 ('Tanchuma Pekudei 11:9 — the blessing\'s text', completion('blessing_text'), {'sages': 'Deut 1:11', 'R_Meir': 'may_the_presence_rest_in_the_work_of_your_hands', 'answer': 'Ps 90:17'}),
 ('Tanchuma Pekudei 11:9-10 — the countersignature', completion('countersignature'), 'name_on_every_item'),
 ('Tanchuma Buber Pekudei 6:1 — six months', completion('six_months'), {'building': 3, 'folded': 3}),
 ('"so they did" at fifteen seats', completion('ken_asu'), 15),
 # ---- THE SCENE ----
 ('the spec\'s order of first mention', build('spec_order'), ['ephod', 'breastplate', 'robe', 'plate', 'turban', 'sash', 'tunic', 'caps', 'breeches']),
 ('the run\'s order — the plate last', build('run_order'), ['ephod', 'breastplate', 'robe', 'tunic', 'breeches', 'caps', 'turban', 'sash', 'plate']),
 ('the plate moves from fourth to ninth', build('plate_moves'), (3, 8)),
 ('the body\'s order (Lev 8)', build('dressing_order'), ['tunic', 'sash', 'robe', 'ephod', 'breastplate', 'turban', 'plate', 'caps']),
 ('the alignment engine (43, 31, 22, 24, 21)', build('alignment'), (43, 31, 22, 24, 21)),
 ('the twenty-one dropped verses', build('dropped'), ['28:1', '28:2', '28:3', '28:4', '28:5', '28:9', '28:10', '28:11', '28:13', '28:14', '28:29', '28:30', '28:33', '28:35', '28:37', '28:38', '28:39', '28:40', '28:41', '28:42', '28:43']),
 ('what the run drops: the function clauses and the office', build('dropped_kinds'), 'function_clauses_and_the_office'),
 ('numerals equal in office, plate, robe', build('numerals_equal'), ['office', 'plate', 'robe']),
 ('the making-verbs counted', build('verbs'), {'spec_you_shall_make': 12, 'spec_they_shall_make': 3, 'spec_you_shall_make_2': 5, 'run_and_he_made': 3, 'run_and_they_made': 11}),
 ('gold, blue, twined, Aaron — spec vs run', build('metals_colors'), {'gold': (17, 15), 'blue': (8, 10), 'twined': (3, 6), 'Aaron': (16, 3)}),
 ('"the second" and the crimson — one written form', build('second_homograph'), 6),
 ('THE SCENE on the world engine — the four use-entries unfired', build('world'), (1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 11)),
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
print('effects: every cell carries REGISTERED effects — NINE discovered in these verses\' own verbs: names_borne, judgment_borne, entry_announced, plate_propitiates (STATUS — the '
      'garments\' USE, promised at the spec, unfired in the run), breastplate_fixed, robe_uncut (BLOCK), nakedness_covered, work_completed, inspected_as_commanded (STATUS) [effects law satisfied]')
print('SCENE: %r — the garments made, the work completed, the delivery, the inspection and the blessing; the four use-entries unfired' % (SCENE,))
if ok == n:
    print('THE VESTMENTS RUN AGAINST THEIR SPEC — the run\'s added tokens are the spec\'s parameters (the sixfold thread from five "fine linen", the twined eight from an added '
          '"twined", the gold\'s four from the process verse — Yoma 71b-72a running on Exod 39); the plate made last; every function clause and Presence-clause dropped; '
          'eight = six plus two from the chapter\'s own list; the gold-bearing four the sheet\'s added four; the sanctuary, priesthood, ordinances, and Day engines CALLED.')
else:
    print('MISSES (%d):' % len(misses))
    for m_ in misses: print('  -', m_[0][:80], '->', m_[1])
    sys.exit('MISSES REMAIN — consult the Talmud per gap and recompile.')

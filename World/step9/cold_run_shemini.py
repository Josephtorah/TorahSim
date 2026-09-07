#!/usr/bin/env python3
"""cold_run_shemini.py — THE SPECIES CLASSIFIER, COMPILED COLD
(Lev 11, parashat Shemini — 2026-09-05, the rhythm's compile
movement).

The five motions:
 (1) code from the BARE INK of Lev 11 alone: the land predicate
     (split hoof AND cud — the conjunction enforced by the ink's
     own four counter-stated exceptions), the water predicate
     (fins and scales), the BIRD BLACKLIST (the ink names twenty
     forbidden kinds and gives NO signs — the ink's own shape),
     the locust clause (jumping joints above the feet, with the
     lo-ketiv), the eight swarmers by name, and the carcass
     status machine (touch -> impure until evening; carry -> wash
     garments + impure until evening).
 (2) the answer sheet: Mishnah Chullin 3:6-7 read whole from the
     local shelf — AND THE SHEET SELF-LABELS ITS OWN LAYERS:
     'the signs of the BEAST were said FROM THE TORAH; the signs
     of the BIRD were NOT said — but the SAGES said: every
     clawer impure; extra toe, crop, peelable gizzard — pure.'
     The code/data separation attested by the answer sheet's own
     words. Plus Mishnah Niddah 6:9's sign correlations and the
     four exceptions as recorded rows.
 (3) run;
 (4) misses filled per gap by the named recorded layer — here the
     bird-sign predicate enters as [SAGES], the label the Mishnah
     itself supplies (with the Sifra's exemplar-training route,
     Chapter 5 6, beside it), and the koy's both-classes row
     rides the derived class-inclusion claim;
 (5) matrix with provenance + EFFECTS on every verdict (the
     effects law): eating a forbidden kind -> lashes (Makkot
     3:2's own list); carcass touch -> impure_until_evening (the
     49th registered effect, harvested this sitting from the
     chapter's own eightfold clause).
Zero-report law: every ink token probed before the run. The
Lev 11:42 probe targets the CURRENT evidence line (the truncated
belly-word) — the toolchain finding stands on the record, the
repair deferred to the owner.
"""
import sqlite3, sys, os, json, io, contextlib
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import effects_layer as FX

DB = '<repo-old>/elijah_docket/tanakh.sqlite'
db = sqlite3.connect(DB)

def strip(s):
    return ''.join(c for c in s if c != '/' and not (0x0591 <= ord(c) <= 0x05C7))

def toks(ch, vs):
    return [strip(r[0]) for r in db.execute(
        "SELECT w.he FROM words w JOIN verses v ON w.verse_id=v.id "
        "WHERE v.book='Lev' AND v.chapter=? AND v.verse=? ORDER BY w.idx",
        (ch, vs))]

PROBES = [
    ('split hoof (mafreset parsah)',   11, 3,  'מפרסת'),
    ('cud (maalat gerah)',             11, 3,  'מעלת'),
    ('camel: cud yes hoof no',         11, 4,  'הגמל'),
    ('hyrax counter-stated',           11, 5,  'השפן'),
    ('hare counter-stated',            11, 6,  'הארנבת'),
    ('pig: hoof yes cud no',           11, 7,  'החזיר'),
    ('fins (snapir)',                  11, 9,  'סנפיר'),
    ('scales (kaskeset)',              11, 9,  'וקשקשת'),
    ('the bird blacklist head: eagle', 11, 13, 'הנשר'),
    ('the locust joints (kraayim)',    11, 21, 'כרעים'),
    ('the lo-ketiv at the joints',     11, 21, 'לא'),
    ('the four locusts: arbeh',        11, 22, 'הארבה'),
    ('the eight head: the weasel',     11, 29, 'החלד'),
    ('touch -> impure until evening',  11, 24, 'הערב'),
    ('carry -> wash garments',         11, 25, 'יכבס'),
    ('the truncated belly-word (the standing toolchain finding)',
                                       11, 42, 'גח'),
]
for label, ch, vs, tok in PROBES:
    if not any(tok == w or tok in w for w in toks(ch, vs)):
        sys.exit('ZERO-REPORT LAW: probe %r failed at Lev %d:%d' % (label, ch, vs))
print('probes: all %d ink-token probes fired [zero-report law satisfied]'
      % len(PROBES))

# ---- (1) the classifier from ink ------------------------------------
I, M, S, D = 'INK', 'MOVE', 'SAGES', 'DATA'

def classify(kind):
    """kind: dict(clazz, signs...) -> (verdict, provenance, why)"""
    c = kind['clazz']
    if c == 'land':
        both = kind.get('hoof') and kind.get('cud')
        if both:
            return ('pure', I, 'Lev 11:3 — split hoof AND cud; the conjunction enforced by the four counter-stated exceptions (11:4-7)')
        return ('impure', I, 'one sign or none — the pincer of the exceptions bars the one-sign escape')
    if c == 'water':
        if kind.get('fin') and kind.get('scale'):
            return ('pure', I, 'Lev 11:9 — fins and scales')
        return ('impure', I, 'Lev 11:10-12')
    if c == 'bird':
        if kind.get('named_in_list'):
            return ('impure', I, 'Lev 11:13-19 — the ink names the forbidden twenty; a blacklist, not a predicate')
        # the sign predicate is the sages' layer — the Mishnah's own label
        if kind.get('claws_and_eats'):
            return ('impure', S, "Chullin 3:6 — 'the signs of the bird were NOT said; but the SAGES said: every clawer impure'")
        if kind.get('extra_toe') and kind.get('crop') and kind.get('peelable_gizzard'):
            return ('pure', S, 'Chullin 3:6 — the three positive signs (the Sifra trains the same predicate from the eagle/dove exemplars, Chapter 5 6)')
        return ('unresolved_check_tradition', S, 'outside both paradigm sets — the recorded practice defers to received kinds')
    if c == 'locust':
        if (kind.get('four_legs') and kind.get('four_wings')
                and kind.get('jumping_joints') and kind.get('wings_cover_most')):
            v = ('pure', I, 'Lev 11:21-22 — the joints clause (with the lo-ketiv read forward: joints that will grow count) + the four named kinds')
            if kind.get('name_known_chagav') is False:
                return ('pure_per_ink_named_arm_open', D, "R. Yosei's name condition (Chullin 3:7) carried as a recorded arm")
            return v
        return ('impure', I, 'Lev 11:20, 11:23')
    if c == 'swarmer':
        if kind.get('one_of_eight'):
            return ('impure_contaminates', I, 'Lev 11:29-30 — the eight by name; person and vessels')
        return ('impure_no_contamination', I, 'Lev 11:41 — eaten-banned, not a contaminator class')
    raise ValueError(c)

def touch_effect(event):
    if event == 'touch_carcass':
        return ('impure_until_evening', I, 'Lev 11:24 — the eightfold clause')
    if event == 'carry_carcass':
        return ('wash_and_evening', I, 'Lev 11:25 — wash garments + until evening')
    if event == 'eat_forbidden':
        return ('lashes', I, 'the ban layer; the answer sheet: Makkot 3:2 lists the eaters of carcasses, terefot, detestables and swarmers')
    raise ValueError(event)

# ---- THE WRAP (W3 THE OFFERING ENGINE, D9-iii, 2026-09-07) — the daemon and the scene --------------
# Two case heads: a kind eaten (11:4, 11:8, 11:42 — the classifier by call: the pure kind writes NOTHING,
# the forbidden kind lashes) and a carcass touched or carried (11:24-25, 11:39 — impure until evening).
# The daemon writes the ledger and never emits an event.
import world_engine as WE
SIGNS = ('clazz', 'hoof', 'cud', 'fin', 'scale', 'named_in_list', 'claws_and_eats', 'extra_toe', 'crop', 'peelable_gizzard',
         'four_legs', 'four_wings', 'jumping_joints', 'wings_cover_most', 'one_of_eight', 'name_known_chagav')
def law_shemini(event, world):
    """Lev 11 (cold_run_shemini.py — the species classifier and the carcass status machine)."""
    k, src = event['kind'], event['case_source']
    E_ = lambda eff, s, cp=None, amount=None, due=None, law='', value=None: {'effect': eff, 'subject': s, 'counterparty': cp, 'amount': amount, 'due': due, 'value': value if value is not None else True, 'source_law': law, 'case_source': src}
    if k == 'forbidden_kind_eaten':
        verdict, prov, why = classify({f: event[f] for f in SIGNS if f in event})
        if verdict.startswith('pure') or verdict == 'unresolved_check_tradition':
            return []                                            # the pure kind (and the kind outside both paradigm sets): nothing written — the silence
        return [E_('lashes', event['eater'], amount=40, value=verdict, law='[INK Lev 11:4, 11:8, 11:11, 11:42 "you shall not eat"; Mishnah Makkot 3:2 — %s]' % why[:70])]
    if k == 'carcass_touched':
        v, prov, why = touch_effect('carry_carcass' if event['contact'] == 'carry' else 'touch_carcass')
        return [E_('impure_until_evening', event['person'], value=v, law='[INK Lev 11:24-25, 11:39-40 — %s]' % why)]
    return []

# ---- (2) the answer sheet ------------------------------------------
mc = json.load(open('<repo-old>/Data/mishnah_chullin_he.json'))
mct = mc['text'] if isinstance(mc, dict) and 'text' in mc else mc
ch36, ch37 = strip(mct[2][5]), strip(mct[2][6])
for tok in ('נאמרו מן התורה', 'לא נאמרו', 'הדורס', 'אצבע יתרה', 'וזפק'):
    assert tok in ch36, 'answer-sheet check: %r not in Chullin 3:6' % tok
for tok in ('קרסלים', 'חופין את רבו', 'ושמו חגב', 'סנפיר וקשקשת', 'שני קשקשין'):
    assert tok in ch37, 'answer-sheet check: %r not in Chullin 3:7' % tok
print('answer sheet: Mishnah Chullin 3:6-7 read whole; THE SHEET SELF-LABELS '
      "— 'the beast's signs SAID FROM THE TORAH... the bird's signs NOT "
      "said, but the SAGES said' [the code/data separation attested]")

TESTS = [
 # (label, input, expected verdict, [effects])
 ('ox (hoof+cud)',        dict(clazz='land', hoof=True, cud=True),  'pure', []),
 ('camel (cud only)',     dict(clazz='land', hoof=False, cud=True), 'impure', ['lashes']),
 ('hyrax (cud only)',     dict(clazz='land', hoof=False, cud=True), 'impure', ['lashes']),
 ('hare (cud only)',      dict(clazz='land', hoof=False, cud=True), 'impure', ['lashes']),
 ('pig (hoof only)',      dict(clazz='land', hoof=True, cud=False), 'impure', ['lashes']),
 ('horse (neither)',      dict(clazz='land', hoof=False, cud=False),'impure', ['lashes']),
 ('salmon (fin+scale)',   dict(clazz='water', fin=True, scale=True),'pure', []),
 ('catfish (fin only)',   dict(clazz='water', fin=True, scale=False),'impure', ['lashes']),
 ('scale-haver (Niddah 6:9: every scale-haver HAS a fin)',
                          dict(clazz='water', fin=True, scale=True),'pure', []),
 ('eagle (named)',        dict(clazz='bird', named_in_list=True),   'impure', ['lashes']),
 ('hawk-like clawer',     dict(clazz='bird', claws_and_eats=True),  'impure', ['lashes']),
 ('dove (3 signs, no claw)', dict(clazz='bird', extra_toe=True, crop=True,
                               peelable_gizzard=True),              'pure', []),
 ('arbeh (all four)',     dict(clazz='locust', four_legs=True, four_wings=True,
                               jumping_joints=True, wings_cover_most=True), 'pure', []),
 ('flying swarmer (no joints)', dict(clazz='locust', four_legs=True,
                               four_wings=True, jumping_joints=False,
                               wings_cover_most=True),              'impure', ['lashes']),
 ('weasel (of the eight)', dict(clazz='swarmer', one_of_eight=True),
                           'impure_contaminates', ['impure_until_evening']),
 ('snake (not of the eight)', dict(clazz='swarmer', one_of_eight=False),
                           'impure_no_contamination', ['lashes']),
]
EVENTS = [
 ('touch a carcass',  'touch_carcass', 'impure_until_evening', ['impure_until_evening']),
 ('carry a carcass',  'carry_carcass', 'wash_and_evening', ['impure_until_evening']),
 ('eat a forbidden kind', 'eat_forbidden', 'lashes', ['lashes']),
]

def scene():
    """THE SCENE — the sixteen classified kinds and the carcass rows replayed on the world engine (clock unit: days)."""
    with contextlib.redirect_stdout(io.StringIO()):
        w = WE.World(era='the kinds and the carcass: Chullin 3:6-7, Makkot 3:2, Kelim 1:1 on the engine (clock unit: days)')
        w.laws = [law_shemini]
        w.advance(1)
        for label, kind, want, effs in TESTS:
            w.submit({'kind': 'forbidden_kind_eaten', 'subject': 'the-eater', 'eater': 'the-eater', 'case_source': 'Mishnah Chullin 3:6-7 — ' + label, **kind})
        w.submit({'kind': 'carcass_touched', 'subject': 'the-toucher', 'person': 'the-toucher', 'contact': 'touch', 'case_source': 'Lev 11:24; Mishnah Kelim 1:1 — touched: until evening'})
        w.submit({'kind': 'carcass_touched', 'subject': 'the-carrier', 'person': 'the-carrier', 'contact': 'carry', 'case_source': 'Lev 11:25; Mishnah Zavim 5:2 — carried: the garments washed, until evening'})
    n = lambda eid, eff: len([e for e in w.entity(eid).ledger if e['effect'] == eff])
    seen, fired, _ = w.coverage()['law_shemini']
    return (n('the-eater', 'lashes'), seen - fired, n('the-toucher', 'impure_until_evening'), n('the-carrier', 'impure_until_evening'), w.clock.year), w
SCENE, _W = scene()

# ---- (3)+(5) run + grade + effects ----------------------------------
print()
total = ok = 0
frac = {'INK': 0, 'SAGES': 0, 'MOVE': 0, 'DATA': 0}
for label, kind, want, effs in TESTS:
    got, prov, why = classify(kind)
    total += 1
    hit = got == want
    ok += hit
    frac[prov] += 1
    FX.validate(effs)
    print('%s %-42s -> %-24s [%s]%s' % ('OK ' if hit else 'MISS', label, got,
          prov, '' if hit else ' want=' + want))
for label, ev, want, effs in EVENTS:
    got, prov, why = touch_effect(ev)
    total += 1
    hit = got == want
    ok += hit
    frac[prov] += 1
    FX.validate(effs)
    print('%s %-42s -> %-24s [%s]' % ('OK ' if hit else 'MISS', label, got, prov))
# ---- THE WRAP (W3, 2026-09-07) — the sixteen kinds and the carcass on the world engine ----
SCENES = [('THE SCENE — (lashed, the pure kinds\' silence, the toucher, the carrier, the clock)', SCENE, (11, 5, 1, 1, 1), ['lashes', 'impure_until_evening'])]
for label, got, want, effs in SCENES:
    total += 1
    hit = got == want
    ok += hit
    frac['INK'] += 1
    FX.validate(effs)
    print('%s %-42s -> %s [INK]%s' % ('OK ' if hit else 'MISS', label[:42], got, '' if hit else ' want=%r' % (want,)))
print()
print('MATRIX: %d/%d cells match the recorded classifications' % (ok, total))
print('SCENE: %r — the daemon\'s watch coverage:' % (SCENE,))
_W.print_coverage()
print('FRACTIONS: pure ink %d/%d (%d%%) · the sages\' self-labeled layer '
      '%d/%d · data %d/%d' % (frac['INK'], total, 100*frac['INK']//total,
      frac['SAGES'], total, frac['DATA'], total))
print('effects: every verdict row validated against the registry '
      '(impure_until_evening = the 49th effect, harvested from the '
      'chapter\'s own eightfold clause) [effects law satisfied]')
if ok == total:
    print()
    print('THE SPECIES CLASSIFIER COMPILES COLD — the land and water and '
          'locust predicates pure ink; the bird layer arrives SELF-LABELED '
          'by the answer sheet itself: the Mishnah\'s own words divide the '
          'Torah\'s code from the sages\' predicate.')
else:
    sys.exit('MISSES REMAIN — consult per gap and recompile.')

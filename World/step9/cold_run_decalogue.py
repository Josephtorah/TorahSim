#!/usr/bin/env python3
# THE DECALOGUE'S LAW LAYER (Exod 20) — the third span compiled under
# the effects law (2026-09-03). The utterances that carry CASE LAW in
# this span's own ink: the vain name, the Sabbath clauses, the theft
# commandment, and the altar rules at the chapter's tail. (The
# person-to-person capital laws' CODE lives in the ordinances span,
# already compiled; the parents' honor case-law lives outside this
# span's answer sheets — both honestly left to their own spans.)
# Effects from birth, targeting the world_engine contract.
# Versification note: this word-database splits the short commandments
# (theft = 20:15, altar clauses = 20:25-26); the probes pin the
# addresses actually used. Read-only; model layer.

# ---- THE HONEST-PAIRING GUARD (sitting C retrofit, 2026-09-05) ------------
# Every expected value this runner grades against must be a LITERAL typed from
# the answer sheet; the parser checks the source before anything runs, and the
# count below is the tripwire — it fails loudly the day the table changes.
import os as _os, sys as _sys
_sys.path.insert(0, _os.path.dirname(_os.path.abspath(__file__)))
from compile_guards import check_honest_pairing as _chp, check_honest_dict as _chd, check_honest_calls as _chc
_P = _os.path.abspath(__file__)
GUARDED = _chp(_P, 'CASES', 2)
assert GUARDED == 13, ('the guard counted %d expectations, the tripwire holds 13' % GUARDED)
print('guard: %d expectations checked, every one a literal from the answer sheet [honest-pairing guard satisfied]' % GUARDED)
import sqlite3, sys
import effects_layer as FX

db = sqlite3.connect('<repo-old>/elijah_docket/tanakh.sqlite')

def strip(s):
    return ''.join(c for c in s if c != '/' and not (0x0591 <= ord(c) <= 0x05C7))

def verse_text(ch, vs):
    rows = db.execute("""SELECT w.he FROM words w JOIN verses v
        ON w.verse_id=v.id WHERE v.book='Exod' AND v.chapter=? AND
        v.verse=? ORDER BY w.idx""", (ch, vs)).fetchall()
    return ' '.join(strip(h) for (h,) in rows)

PROBES = [
    ('ינקה',  20, 7,  'will not hold guiltless — the lash hook'),
    ('לקדשו', 20, 8,  'to sanctify it'),
    ('מלאכה', 20, 10, 'any labor'),
    ('תגנב',  20, 15, 'you shall not steal'),
    ('גזית',  20, 25, 'hewn stone'),
    ('חרבך',  20, 25, 'your sword — the iron ban'),
    ('במעלת', 20, 26, 'by steps'),
]
for tok, ch, vs, note in PROBES:
    if tok not in verse_text(ch, vs):
        sys.exit('ZERO-REPORT LAW: probe %r (%s) failed at Exod %d:%d'
                 % (tok, note, ch, vs))
print('probes: all %d fired  [zero-report law satisfied]\n' % len(PROBES))

P = []
def ink(ref, note):  P.append(('INK',  'Exod %s — %s' % (ref, note)))
def move(src, note): P.append(('MOVE', '%s — %s' % (src, note)))

def out(verdict, effects):
    FX.validate([e for e in effects if e != FX.NONE])
    return verdict, effects, list(P)


# ===== F1: THE NAME IN VAIN (20:7) ===================================
def vain_name(case, data):
    del P[:]
    ink('20:7', '"you shall not take the name of the LORD your God in '
        'vain, for the LORD WILL NOT HOLD GUILTLESS (לא ינקה) him who '
        'takes His name in vain" — the clause that powers the court\'s '
        'own hand')
    if case['ask'] == 'vain_oath':
        move('Shevuot 21a:6 (triage LAW row)', 'R. Yochanan in the '
             'name of R. Shimon ben Yochai: He does not hold guiltless '
             '— but the COURT lashes him and he is cleared: the lash '
             'derivation')
        return out('lashes', ['lashes'])
    if case['ask'] == 'false_future_oath':
        move('Shevuot 20b:6 (triage LAW row)', 'the broken I-will-eat '
             'oath — its prohibition located at this clause; lashes '
             'where an act was done')
        return out('lashes', ['lashes'])
    if case['ask'] == 'vain_and_false_utterance':
        move('Shevuot 20b:9 (triage LAW row)', 'vain and false were '
             'SPOKEN AS ONE UTTERANCE — like remember and observe: a '
             'teaching about the giving, not a new entry')
        return out('spoken as one', [FX.NONE])
    return out('no verdict in span', [FX.NONE])


# ===== F2: THE SABBATH CLAUSES (20:8-10) =============================
def sabbath_clauses(case, data):
    del P[:]
    if case['ask'] == 'remember':
        ink('20:8', '"REMEMBER the Sabbath day TO SANCTIFY IT '
            '(לקדשו)" — the duty is a declaration')
        move('Pesachim 106a:5 (triage LAW row)', 'remember it OVER '
             'WINE — the kiddush, by night and again by day')
        return out('sanctify over wine', ['sanctify_day'])
    if case['ask'] == 'labor_scope':
        ink('20:10', '"you shall not do ANY LABOR (כל מלאכה) — you, '
            'your son and daughter, your slave, your beast, and your '
            'stranger within your gates" — the household enumerated')
        return out('the whole household barred',
                   ['labor_barred', 'rest_required'])
    if case['ask'] == 'causing':
        ink('20:10', '"you shall not DO (לא תעשה)" — the verb bars '
            'the deed')
        move('Shabbat 120b:11 (triage LAW row)', 'performance is '
             'barred, causation is not — the barrier of jugs may '
             'stand while the fire comes to it')
        return out('causing permitted', [FX.NONE])
    if case['ask'] == 'laden_beast':
        ink('20:10', '"...and your BEAST" — the animal\'s rest is in '
            'the commandment')
        move('Shabbat 153b:7 (triage LAW row)', 'the driver of the '
             'laden animal — the mechamer question rides this clause')
        return out('driving the laden beast barred', ['labor_barred'])
    return out('no verdict in span', [FX.NONE])


# ===== F3: THE THEFT COMMANDMENT (20:15) =============================
def theft_commandment(case, data):
    del P[:]
    ink('20:15', '"you shall not STEAL (לא תגנב)" — spoken amid '
        '"you shall not murder" and "you shall not commit adultery": '
        'capital neighbors')
    move('Sanhedrin 86a:15-16 (triage LAW rows)', 'a matter learned '
         'from its CONTEXT — the middah named on this very verse: '
         'the Decalogue\'s theft is the theft of PERSONS; money-theft '
         'has its own seat at the ordinances')
    if case['ask'] == 'kidnapper':
        move('Mishnah Sanhedrin 11:1 (the answer sheet)', 'the '
             'abductor is on the strangled list — with the sold-and-'
             'exploited conditions of the ordinances\' own clause '
             '(21:16)')
        return out('capital — the kidnapper', ['put_to_death'])
    if case['ask'] == 'money_theft_here':
        return out('routed to the ordinances span', [FX.NONE])
    return out('no verdict in span', [FX.NONE])


# ===== F4: THE ALTAR RULES (20:24-26) ================================
def altar_rules(case, data):
    del P[:]
    if case['ask'] == 'hewn_stones':
        ink('20:25', '"you shall not build them HEWN (גזית), for you '
            'have lifted YOUR SWORD (חרבך) upon it and profaned it" — '
            'iron\'s touch profanes the stone')
        move('Mishnah Middot 3:4 (the answer sheet)', 'the altar\'s '
             'stones — whole stones the iron never touched; a stone '
             'iron scratched is DISQUALIFIED')
        return out('iron-touched stone disqualified', ['disqualified'])
    if case['ask'] == 'build_recipe':
        move('Zevachim 54a:8 (triage LAW row)', 'Levi\'s baraita: the '
             'frame, the whole stones, the lime — the construction '
             'recipe honoring the iron ban')
        return out('whole stones, frame and lime', [FX.NONE])
    if case['ask'] == 'steps':
        ink('20:26', '"neither shall you go up BY STEPS (במעלת) onto '
            'My altar, that your nakedness be not uncovered upon it" '
            '— a ramp, not stairs')
        move('Sanhedrin 7b:12 (triage LAW row)', 'and the ordinances '
             'follow at the next verse: bar Kappara\'s juxtaposition '
             '— be temperate in judgment')
        return out('a ramp; and temperance beside it', [FX.NONE])
    return out('no verdict in span', [FX.NONE])


# ---- THE WRAP (W1 THE EXODUS LAW, D9-iii, 2026-09-07) — the daemon and the scene --------------
# The four case heads of the law layer (20:7, 20:8, 20:10, 20:15 with 21:16), each a case-form type
# of event_vocabulary.yaml; the altar rule (20:24-26) is wrapped by the ordinances daemon at its
# call site. The daemon writes the ledger and never emits an event.
import io, contextlib, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import world_engine as WE
def law_decalogue(event, world):
    """Exod 20:7, 20:8-10, 20:15 (cold_run_decalogue.py F1-F3)."""
    k, src = event['kind'], event['case_source']
    E_ = lambda eff, s, cp=None, amount=None, due=None, law='', value=None: {'effect': eff, 'subject': s, 'counterparty': cp, 'amount': amount, 'due': due, 'value': value if value is not None else True, 'source_law': law, 'case_source': src}
    if k == 'name_sworn_in_vain':
        return [E_('lashes', event['swearer'], value=event['oath'], law="F1 [INK 20:7 'the LORD will not hold guiltless'; Shevuot 21a:6: the court lashes him and he is cleared; Mishnah Shevuot 3:10-11]")]
    if k == 'sabbath_remembered':
        return [E_('sanctify_day', event['household'], cp='HEAVEN', law="F2 [INK 20:8 'remember the Sabbath day to sanctify it'; Pesachim 106a:5: over wine]")]
    if k == 'sabbath_labor':
        if event['act'] == 'cause':
            return []                                            # Shabbat 120b:11 — performance is barred, causation is not
        return [E_('labor_barred', event['household'], value=event['actor'], law="F2 [INK 20:10 'you shall not do any labor — you, your son and your daughter, your slave and your maidservant and your beast and your stranger'; the laden beast, Shabbat 153b:7]"),
                E_('rest_required', event['household'], law="F2 [INK 20:10 the household enumerated]")]
    if k == 'person_stolen':
        if event['sold']:
            return [E_('put_to_death', event['thief'], value='strangled', law="F3 [INK 20:15 in its context, Sanhedrin 86a:15-16; 21:16 'steals a man and sells him... shall surely be put to death'; Mishnah Sanhedrin 11:1]")]
        return []                                                # not sold: the ordinances' own condition unmet (21:16)
    return []

def scene():
    """THE SCENE — the recorded cases replayed on the world engine (clock unit: days)."""
    with contextlib.redirect_stdout(io.StringIO()):
        w = WE.World(era='the Decalogue\'s law layer: Shevuot 3, Shabbat 120b, 153b, Sanhedrin 11:1 on the engine (clock unit: days)')
        w.laws = [law_decalogue]
        w.advance(1)
        w.submit({'kind': 'name_sworn_in_vain', 'subject': 'the-swearer', 'swearer': 'the-swearer', 'oath': 'vain', 'case_source': 'Mishnah Shevuot 3:10-11 — the vain oath'})
        w.submit({'kind': 'name_sworn_in_vain', 'subject': 'the-oath-breaker', 'swearer': 'the-oath-breaker', 'oath': 'false_future', 'case_source': 'Shevuot 20b:6 — the broken I-will-eat oath'})
        w.advance(2)
        w.submit({'kind': 'sabbath_remembered', 'subject': 'the-household', 'household': 'the-household', 'case_source': 'Pesachim 106a:5 — remember it over wine'})
        w.submit({'kind': 'sabbath_labor', 'subject': 'the-household', 'household': 'the-household', 'actor': 'self', 'act': 'do', 'case_source': "Exod 20:10 — the ink's own list"})
        w.submit({'kind': 'sabbath_labor', 'subject': 'the-household', 'household': 'the-household', 'actor': 'self', 'act': 'cause', 'case_source': 'Shabbat 120b:11 — causing permitted'})
        w.submit({'kind': 'sabbath_labor', 'subject': 'the-household', 'household': 'the-household', 'actor': 'beast', 'act': 'drive_laden', 'case_source': 'Shabbat 153b:7 — the laden beast'})
        w.advance(3)
        w.submit({'kind': 'person_stolen', 'subject': 'the-kidnapper', 'thief': 'the-kidnapper', 'victim': 'the-victim', 'sold': True, 'case_source': 'Mishnah Sanhedrin 11:1 — the kidnapper who sold'})
        w.submit({'kind': 'person_stolen', 'subject': 'the-second-kidnapper', 'thief': 'the-second-kidnapper', 'victim': 'the-victim', 'sold': False, 'case_source': 'Mishnah Sanhedrin 11:1 — not sold: not liable'})
        w.advance(4)
    n = lambda eid, eff: len([e for e in w.entity(eid).ledger if e['effect'] == eff])
    return (n('the-swearer', 'lashes'), n('the-oath-breaker', 'lashes'), n('the-household', 'sanctify_day'), n('the-household', 'labor_barred'), n('the-household', 'rest_required'),
            n('the-kidnapper', 'put_to_death'), n('the-second-kidnapper', 'put_to_death'), w.clock.year), w
SCENE, _W = scene()

# ---- the test data; run, grade, effects -----------------------------
DATA = {}
CASES = [
    ('Mishnah Shevuot 3:10-11 — the vain oath draws lashes',
     lambda: vain_name({'ask': 'vain_oath'}, DATA), 'lashes'),
    ('Shevuot 3:? class — the broken future oath',
     lambda: vain_name({'ask': 'false_future_oath'}, DATA), 'lashes'),
    ('the one-utterance teaching (vain and false together)',
     lambda: vain_name({'ask': 'vain_and_false_utterance'}, DATA),
     'spoken as one'),
    ('remember over wine — the kiddush duty',
     lambda: sabbath_clauses({'ask': 'remember'}, DATA),
     'sanctify over wine'),
    ('the household labor ban (the ink\'s own list)',
     lambda: sabbath_clauses({'ask': 'labor_scope'}, DATA),
     'the whole household barred'),
    ('doing barred, causing not (Shabbat 120b)',
     lambda: sabbath_clauses({'ask': 'causing'}, DATA),
     'causing permitted'),
    ('the laden beast (Shabbat 153b)',
     lambda: sabbath_clauses({'ask': 'laden_beast'}, DATA),
     'driving the laden beast barred'),
    ('Mishnah Sanhedrin 11:1 — the Decalogue\'s theft is of persons',
     lambda: theft_commandment({'ask': 'kidnapper'}, DATA),
     'capital — the kidnapper'),
    ('money theft routed to its own span',
     lambda: theft_commandment({'ask': 'money_theft_here'}, DATA),
     'routed to the ordinances span'),
    ('Mishnah Middot 3:4 — iron disqualifies the stone',
     lambda: altar_rules({'ask': 'hewn_stones'}, DATA),
     'iron-touched stone disqualified'),
    ('Zevachim 54a — the build recipe',
     lambda: altar_rules({'ask': 'build_recipe'}, DATA),
     'whole stones, frame and lime'),
    ('the ramp and the juxtaposition (Sanhedrin 7b)',
     lambda: altar_rules({'ask': 'steps'}, DATA),
     'a ramp; and temperance beside it'),
    # ---- THE WRAP (W1): the scene on the world engine — the recorded cases on the daemon ----
    ('THE SCENE on the world engine — the wrap (W1): the vain and the broken oath lashed, the day sanctified, the household barred twice (the deed, the laden beast) and causing free, the kidnapper who sold strangled and the one who did not sell unwritten',
     lambda: (SCENE, [FX.NONE], [('INK', 'Exod 20:7-15 — the recorded cases replayed: Shevuot 3:10-11, Pesachim 106a, Shabbat 120b, 153b, Sanhedrin 11:1')]),
     (1, 1, 1, 2, 2, 1, 0, 4)),
]

ok = 0
frac = {'INK': 0, 'MOVE': 0, 'DATA': 0}
used = []
print()
for label, fn, want in CASES:
    got, effects, prov = fn()
    hit = got == want
    ok += hit
    kinds = [k for k, _ in prov]
    cls = 'INK' if all(k == 'INK' for k in kinds) else \
          ('MOVE' if 'MOVE' in kinds else 'DATA')
    frac[cls] += 1
    print('%s  [%s]  %s' % ('PASS' if hit else 'MISS', cls, label))
    if not hit:
        print('      expected: %s' % want)
        print('      got     : %s' % got)
    used += effects
    for line in FX.render(effects):
        print('        ->%s' % line)
print()
print('WATCH COVERAGE (the wrap):')
_W.print_coverage()
print('MATRIX: %d/%d cells match the answer sheet' % (ok, len(CASES)))
tot = len(CASES)
print('FRACTIONS: pure ink %d/%d (%.0f%%) · named moves %d/%d (%.0f%%)'
      % (frac['INK'], tot, 100.0 * frac['INK'] / tot,
         frac['MOVE'], tot, 100.0 * frac['MOVE'] / tot))
ops = FX.summarize(used)
print('LEDGER OPS this span writes:',
      ', '.join('%s x%d' % kv for kv in sorted(ops.items())))
if ok == len(CASES):
    print('\nTHE DECALOGUE\'S LAW LAYER COMPILES — the third span '
          'under the effects law.')

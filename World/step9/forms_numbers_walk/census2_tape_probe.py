import os as _os
_ROOT = _os.path.normpath(_os.path.join(_os.path.dirname(_os.path.abspath(__file__)), '..', '..', '..'))   # THE PORTABLE REPO (2026-09-15): the repo root from this file's own place
#!/usr/bin/env python3
# THE NUMBERS WALK 8b (2026-09-11): THE TAPE PROBE before the design — the running world built once; the ledgers of the persons the second
# census names (Er, Onan, Dathan, Abiram, Korach, Nadab, Abihu, Caleb, Joshua, Jochebed, Miriam, the daughters, Zelophehad, the Levites) —
# their effects with open flags and days; the decree's timer fire (carcasses_fall_in_the_wilderness) and its day against the census's
# day (40, 6, 1); the Levites' inheritance_barred block; the open plague entries (Korach's debt); the entity ids that exist.
import sys, io, contextlib
sys.path.insert(0, (_ROOT + '/World/step9'))
with contextlib.redirect_stdout(io.StringIO()):
    import cold_run_sequence as CS
    reg = CS.registry_map()
    w, M = CS.run_world(CS.PARAMS['sojourn_start']['value'], reg, 'probe')
ex = w.clock.eras['exodus']; C = w.clock.calendar
D = lambda d: ((w.clock.year if False else C.year(d)),) + C.date(d)[1:]   # the creation calendar's (year, month, day) — a Genesis day has no exodus date
print('the clock ends at day %d = %r; entities %d' % (w.clock.day, D(w.clock.day), len(w.entities)))
for eid in ('er', 'onan', 'dathan', 'abiram', 'korach', 'nadab', 'abihu', 'nadab-and-abihu', 'caleb', 'yehoshua', 'joshua', 'jochebed', 'miriam', 'the_daughters_of_zelophehad', 'zelophehad', 'the_levites', 'the-two-hundred-fifty', 'the_two_hundred_fifty', 'amram', 'serah', 'eleazar_son_of_aaron', 'israel_people'):
    e = w.entities.get(eid)
    if e is None:
        print('  %-28s NO ENTITY' % eid); continue
    print('  %-28s %d entries: %s' % (eid, len(e.ledger), '; '.join('%s%s@%s%s' % (x['effect'], ('=' + str(x.get('value'))[:30]) if x.get('value') not in (True, None) else '', D(x['day']), ' OPEN' if x.get('open') else '') for x in e.ledger)[:900]))
fires = [(l[1], l[2]) for l in w.log if l[0] == 'TIMER-FIRE' and l[2]['effect'] == 'carcasses_fall_in_the_wilderness']
print('carcasses_fall fires: %s' % [(d, D(d), f['subject']) for d, f in fires])
print('the census day (40, 6, 1) = %d; the fire before it: %s' % (w.clock.day_in('exodus', 40, 6, 1), [d < w.clock.day_in('exodus', 40, 6, 1) for d, _ in fires]))
opl = [(ent.eid, e['effect'], e.get('value'), D(e['day'])) for ent in w.entities.values() for e in ent.ledger if e['effect'] == 'plague_struck']
print('plague_struck entries: %s' % opl)
print('open plague entries: %s' % [(ent.eid, e.get('value'), D(e['day'])) for ent in w.entities.values() for e in ent.ledger if e['effect'] == 'plague_struck' and e.get('open')])
ib = [(ent.eid, e.get('value'), D(e['day']), e.get('open')) for ent in w.entities.values() for e in ent.ledger if e['effect'] == 'inheritance_barred']
print('inheritance_barred entries: %s' % ib)
sc = [(ent.eid, e.get('value'), D(e['day'])) for ent in w.entities.values() for e in ent.ledger if e['effect'] == 'counted']
print('counted entries: %s' % sc)
print('death-class effects on the named: %s' % sorted({e['effect'] for eid in ('er', 'onan', 'dathan', 'abiram', 'korach') if eid in w.entities for e in w.entities[eid].ledger}))
print('the last EVENT: %s' % [l[2].get('case_source', '')[:60] for l in w.log if l[0] == 'EVENT'][-1])
print('events with subject jochebed / er / onan: %s' % [(l[2]['kind'], l[2].get('case_source', '')[:40]) for l in w.log if l[0] == 'EVENT' and l[2].get('subject') in ('jochebed', 'er', 'onan')])

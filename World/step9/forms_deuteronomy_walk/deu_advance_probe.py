#!/usr/bin/env python3
# THE DEUTERONOMY WALK 1b — THE CLOCK'S COST MEASURED before the design: the running world (the tape to Numbers 36:13, the counter at (40, 6, 1))
# advanced IN MEMORY to Deuteronomy 1:3's date (40, 11, 1) with no line submitted — what fires, what re-arms, what is written, what closes; and
# the same to the death's date (41, 1, 10 less 33 days = the seventh of Adar, the shelf's) for the record. NOTHING WRITTEN TO DISK (the journal dir
# is a scratch folder; the live session's source name never touched).
import os, sys, io, contextlib, collections, subprocess
ROOT = subprocess.check_output(['git', 'rev-parse', '--show-toplevel'], text=True).strip()
SCR = os.path.dirname(os.path.abspath(__file__))
os.environ['WORLD_JOURNAL_DIR'] = f'{SCR}/adv_journal'
os.makedirs(os.environ['WORLD_JOURNAL_DIR'], exist_ok=True)
sys.path.insert(0, f'{ROOT}/World/step9')
with contextlib.redirect_stdout(io.StringIO()):
    import cold_run_sequence as CS
    import register_census as RG
    w = RG.running_world()
ex = w.clock.eras['exodus']
def snap(w):
    return dict(day=w.clock.day, date=ex.date(w.clock.day), log=len(w.log), classes=dict(collections.Counter(l[0] for l in w.log)), timers=len(w.timers), entities=len(w.entities),
                writes=sum(1 for l in w.log if l[0] == 'WRITE'), fires=sum(1 for l in w.log if l[0] == 'TIMER-FIRE'), sets=sum(1 for l in w.log if l[0] == 'TIMER-SET'), closes=sum(1 for l in w.log if l[0] == 'CLOSE'))
before = snap(w)
print('BEFORE', before)
print('pending timers before:', sorted((t[0], t[1]['subject'], t[1]['effect'], str(t[1].get('value'))[:40]) for t in w.timers))
n0 = len(w.log)
target = w.clock.day_in('exodus', 40, 11, 1)
with contextlib.redirect_stdout(io.StringIO()) as buf:
    w.advance(target)
after = snap(w)
print('AFTER advance to (40, 11, 1) = day %d:' % target, after)
print('DELTA: log +%d, writes +%d, fires +%d, sets +%d, closes +%d, timers pending %d -> %d, entities %d -> %d' % (after['log'] - before['log'], after['writes'] - before['writes'], after['fires'] - before['fires'], after['sets'] - before['sets'], after['closes'] - before['closes'], before['timers'], after['timers'], before['entities'], after['entities']))
new = w.log[n0:]
print('the new log lines by class:', dict(collections.Counter(l[0] for l in new)))
for l in new:
    d = l[2] if len(l) > 2 else {}
    print('   %-11s day %-14s %s' % (l[0], ex.date(l[1]) if isinstance(l[1], int) else l[1], str({k: str(v)[:60] for k, v in (d.items() if isinstance(d, dict) else [])})[:260]))
print('pending timers after:', sorted((t[0], ex.date(t[0]), t[1]['subject'], t[1]['effect'], str(t[1].get('value'))[:40]) for t in w.timers))
print('the advance printed:', buf.getvalue()[:600])
# the altar's ledger tail and israel's musaf entries
alt = w.entities.get('the-altar')
if alt: print('the-altar ledger %d; tail: %s' % (len(alt.ledger), [(x['effect'], str(x.get('value'))[:40], ex.date(x.get('day'))) for x in alt.ledger[-12:]]))

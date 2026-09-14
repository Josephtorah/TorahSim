#!/usr/bin/env python3
"""loop_baseline.py — the BEFORE run of the sequence tape on the unchanged engine: the log's classes, the payload types (JSON-safe or not),
the shared-object facts the sink must record, and the runtime. Read, never recited."""
import os, sys, time, json, collections
sys.path.insert(0, '<repo-old>/World/step9')
os.chdir('<repo-old>/World/step9')
import cold_run_sequence as CS
t0 = time.time()
reg = CS.registry_map()
w, M = CS.run_world(CS.PARAMS['sojourn_start']['value'], reg, 'baseline')
print('run_world elapsed %.1fs' % (time.time() - t0))
print('log lines', len(w.log), 'classes', dict(collections.Counter(l[0] for l in w.log)))
print('tuple', CS.tuple_of(w))
bad = collections.Counter(); ids = collections.Counter(); keys = collections.defaultdict(collections.Counter)
def walk(x, path):
    if isinstance(x, dict):
        for k, v in x.items(): walk(v, path + '.' + str(k))
    elif isinstance(x, (list, tuple)):
        for v in x: walk(v, path + '[]')
    elif x is None or isinstance(x, (str, int, float, bool)): pass
    else: bad[(path, type(x).__name__)] += 1
for kind, day, payload in w.log:
    walk(payload, kind); ids[id(payload)] += 1
    for k in payload: keys[kind][k] += 1
print('non-JSON leaves:', dict(bad) or 'NONE')
print('payload dicts shared by >1 log line:', sum(1 for v in ids.values() if v > 1))
for kind in sorted(keys): print('  keys of', kind, ':', dict(keys[kind]))
# subject resolution and provenance fields present
ev = [p for k, d, p in w.log if k == 'EVENT']
print('EVENT subject present', sum(1 for e in ev if 'subject' in e), 'of', len(ev), '; case_source present', sum(1 for e in ev if 'case_source' in e))
wr = [p for k, d, p in w.log if k in ('WRITE', 'RETRO-WRITE', 'TIMER-SET', 'TIMER-FIRE', 'TIMER-CANCEL')]
print('effect lines with subject', sum(1 for e in wr if 'subject' in e), 'of', len(wr), '; source_law', sum(1 for e in wr if 'source_law' in e), '; case_source', sum(1 for e in wr if 'case_source' in e))
print('entities', len(w.entities), 'timers pending', len(w.timers), 'clock day', w.clock.day)
json.dumps([[k, d, p] for k, d, p in w.log], sort_keys=True, ensure_ascii=False, default=str)
print('json.dumps of the whole log with default=str: ok; total elapsed %.1fs' % (time.time() - t0))

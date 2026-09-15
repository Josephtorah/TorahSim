#!/usr/bin/env python3
"""loop_measure_mutation.py — THE LOOP THAT WAITS, the measurement before the design (2026-09-14).
Question: which journal payloads change AFTER the engine logs them? Three snapshots of every log line of the running world:
  (a) at append time (the moment self.log.append runs), (b) at the end of the outermost engine call (submit / marker / close /
  row / cancel_timers / advance returning at depth 0 — the atomic block), (c) at the run's end (what the sink writes today).
Printed per class: lines differing (a) vs (c), (b) vs (c), and WHICH KEYS differ at (b) vs (c). The design rides on this print.
Runs the running world only, journaling into a temp dir (the repo's data dir untouched)."""
import os as _os
_ROOT = _os.path.normpath(_os.path.join(_os.path.dirname(_os.path.abspath(__file__)), '..', '..', '..', '..'))   # THE PORTABLE REPO (2026-09-15): the repo root from this file's own place
import os, sys, json, collections, tempfile, io, contextlib, time
TD = tempfile.mkdtemp(prefix='loop_measure_')
os.environ['WORLD_JOURNAL_DIR'] = TD
sys.path.insert(0, (_ROOT + '/World/step9'))
sys.path.insert(0, (_ROOT + '/World/journal'))
import world_engine as WE
import world_journal as WJ
from worldledger import canon


def snap(payload):
    return canon(WJ._jsonable(payload, collections.Counter()))


class Log(list):
    def __init__(self):
        super().__init__(); self.atlog = []
    def append(self, item):
        super().append(item); self.atlog.append(snap(item[2]))


def wrap(name):
    orig = getattr(WE.World, name)
    def f(self, *a, **k):
        try:
            return orig(self, *a, **k)
        finally:
            if getattr(self, '_depth', 0) == 0 and isinstance(self.log, Log):
                st = self.__dict__.setdefault('_blockend', [])
                while len(st) < len(self.log):
                    st.append(snap(self.log[len(st)][2]))
    f.__name__ = name
    setattr(WE.World, name, f)


for n in ('submit', 'marker', 'close', 'row', 'cancel_timers', 'advance'):
    wrap(n)
_init = WE.World.__init__
def init(self, *a, **k):
    _init(self, *a, **k); self.log = Log()
WE.World.__init__ = init

t0 = time.time()
import cold_run_sequence as CS
t1 = time.time()
reg = CS.registry_map()
with contextlib.redirect_stdout(io.StringIO()):
    w, M = CS.run_world(CS.PARAMS['sojourn_start']['value'], reg, 'measure')
t2 = time.time()
print('import %.1fs, the running world %.1fs; log %d lines; temp %s' % (t1 - t0, t2 - t1, len(w.log), TD))
end = [snap(l[2]) for l in w.log]
blockend = w._blockend
atlog = w.log.atlog
assert len(end) == len(blockend) == len(atlog), (len(end), len(blockend), len(atlog))
classes = [l[0] for l in w.log]
per = collections.OrderedDict()
keys_b = collections.Counter()
examples = {}
for i, cls in enumerate(classes):
    p = per.setdefault(cls, {'lines': 0, 'a_vs_c': 0, 'b_vs_c': 0})
    p['lines'] += 1
    if atlog[i] != end[i]:
        p['a_vs_c'] += 1
    if blockend[i] != end[i]:
        p['b_vs_c'] += 1
        b, c = json.loads(blockend[i]), json.loads(end[i])
        for k in sorted(set(b) | set(c)):
            if b.get(k) != c.get(k):
                keys_b[(cls, k)] += 1
                examples.setdefault((cls, k), (i, b.get(k), c.get(k)))
print('\nCLASS         lines  differ at append  differ at block end   (each against the run\'s end)')
for cls, p in per.items():
    print('%-12s %6d  %16d  %19d' % (cls, p['lines'], p['a_vs_c'], p['b_vs_c']))
print('\nKEYS THAT DIFFER between the block-end snapshot and the run\'s end:')
for (cls, k), n in sorted(keys_b.items()):
    i, b, c = examples[(cls, k)]
    print('  %-12s %-12s %5d lines   e.g. line %d: block end %r -> run end %r' % (cls, k, n, i + 1, b, c))
# the masked comparison: bound[1] -> None at the run's end; does everything else agree?
def mask(s):
    d = json.loads(s)
    if isinstance(d.get('bound'), list) and len(d['bound']) == 2:
        d['bound'] = [d['bound'][0], None]
    return canon(d)
left = sum(1 for i in range(len(end)) if blockend[i] != mask(end[i]))
print('\nAFTER MASKING bound[1] on the run-end snapshot: %d of %d lines still differ from the block-end snapshot' % (left, len(end)))
# at-append vs block-end: which keys change inside the block?
keys_a = collections.Counter()
for i, cls in enumerate(classes):
    if atlog[i] != blockend[i]:
        a, b = json.loads(atlog[i]), json.loads(blockend[i])
        for k in sorted(set(a) | set(b)):
            if a.get(k) != b.get(k):
                keys_a[(cls, k)] += 1
print('\nKEYS THAT CHANGE INSIDE THE BLOCK (append time -> block end):')
for (cls, k), n in sorted(keys_a.items()):
    print('  %-12s %-12s %5d lines' % (cls, k, n))

# THE 26: which lines still differ after the mask — their class, the bound at the seal and at the end
odd = [(i, classes[i], json.loads(blockend[i]).get('bound'), json.loads(end[i]).get('bound')) for i in range(len(end)) if blockend[i] != mask(end[i])]
print('\nTHE LINES STILL DIFFERING AFTER THE MASK (%d): class, bound at the seal -> bound at the end' % len(odd))
for i, cls, b, c in odd:
    print('  line %5d %-11s %r -> %r' % (i + 1, cls, b, c))

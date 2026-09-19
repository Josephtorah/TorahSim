import os as _os
_ROOT = _os.path.normpath(_os.path.join(_os.path.dirname(_os.path.abspath(__file__)), '..', '..', '..'))   # THE PORTABLE REPO (2026-09-15): the repo root from this file's own place
# THE GATES CUT (2026-09-19): can the replayed running world be saved and reloaded? — the import cost, the replay cost, the pickle's size, the reload cost
import sys, os, io, time, pickle, contextlib, subprocess
ROOT = _ROOT
sys.path.insert(0, ROOT + '/World/step9'); os.chdir(ROOT + '/World/step9')
t0 = time.time()
with contextlib.redirect_stdout(io.StringIO()):
    import cold_run_sequence as CS
t1 = time.time(); print('import cold_run_sequence: %.1f s' % (t1 - t0), flush=True)
with contextlib.redirect_stdout(io.StringIO()):
    reg = CS.registry_map()
    w, M = CS.run_world(CS.PARAMS['sojourn_start']['value'], reg, 'snapshot-test')
t2 = time.time(); print('run_world (the replay with the journal attached): %.1f s' % (t2 - t1), flush=True)
attrs = {k: type(v).__name__ for k, v in vars(w).items()}
print('world attrs:', attrs)
laws, sink = w.laws, getattr(w, 'sink', None)
w.laws = []
for k, v in list(vars(w).items()):
    if 'sink' in k or 'journal' in k or 'conn' in k: print('stripping', k, type(v).__name__); setattr(w, k, None)
SP = os.path.dirname(os.path.abspath(__file__))
try:
    b = pickle.dumps(w, protocol=pickle.HIGHEST_PROTOCOL)
    open(SP + '/running_world_test.pickle', 'wb').write(b)
    print('pickle: %.1f MB in %.1f s' % (len(b) / 1e6, time.time() - t2), flush=True)
    t3 = time.time(); w2 = pickle.loads(b); print('unpickle in-process: %.2f s; events %d entities %d log %d' % (time.time() - t3, len([l for l in w2.log if l[0] == 'EVENT']), len(w2.entities), len(w2.log)))
    print('M keys', len(M), 'pickle M ok', len(pickle.dumps(M)))
except Exception as e:
    import traceback; traceback.print_exc(); print('PICKLE FAILED', type(e).__name__, str(e)[:300])

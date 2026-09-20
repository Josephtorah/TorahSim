import sys, io, contextlib, pickle, hashlib
sys.path.insert(0, '/Users/Shared/TorahSim/World/step9')
with contextlib.redirect_stdout(io.StringIO()): import cold_run_sequence as CS
import cold_run_balak as B
w = B._W
h = lambda v: hashlib.sha256(pickle.dumps(v, protocol=5)).hexdigest()[:16]
print('pickle twice same?', h(w) == h(w), '| type', type(w).__name__, '| attrs', sorted(vars(w))[:12])
proj = {'day': getattr(getattr(w, 'clock', None), 'day', None), 'log': len(getattr(w, 'log', [])), 'entities': sorted(getattr(w, 'entities', {}))[:6], 'n_entities': len(getattr(w, 'entities', {})), 'laws': len(getattr(w, 'laws', [])), 'log_hash': h([tuple(map(str, l)) if isinstance(l, (list, tuple)) else str(l) for l in getattr(w, 'log', [])])}
print('projection', proj)
for k, v in sorted(vars(w).items()):
    try: print('  attr %-14s %s' % (k, h(v)))
    except Exception as e: print('  attr %-14s unpicklable %s' % (k, type(e).__name__))

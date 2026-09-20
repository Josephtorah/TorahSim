import os as _os
_ROOT = _os.path.normpath(_os.path.join(_os.path.dirname(_os.path.abspath(__file__)), '..', '..', '..'))   # THE PORTABLE REPO (2026-09-15): the repo root from this file's own place
import sys, os, subprocess, json, io, contextlib, re
ROOT = _ROOT; sys.path.insert(0, os.path.join(ROOT, 'World', 'step9'))
with contextlib.redirect_stdout(io.StringIO()):
    import cold_run_sequence, cold_run_balak as B
def canon(v, depth=0):
    if depth > 40: return re.sub(r' at 0x[0-9a-f]+', '', repr(v))[:200]
    if isinstance(v, (set, frozenset)): return ['set', sorted((canon(x, depth + 1) for x in v), key=repr)]
    if isinstance(v, dict): return ['dict', sorted(([canon(k, depth + 1), canon(x, depth + 1)] for k, x in v.items()), key=repr)]
    if isinstance(v, (list, tuple)): return [type(v).__name__, [canon(x, depth + 1) for x in v]]
    if isinstance(v, (str, bytes, int, float, bool, type(None))): return v if not isinstance(v, bytes) else repr(v)
    if hasattr(v, '__dict__'): return [type(v).__module__ + '.' + type(v).__name__, sorted(([k, canon(x, depth + 1)] for k, x in vars(v).items() if not callable(x)), key=repr)]
    return re.sub(r' at 0x[0-9a-f]+', '', repr(v))[:200]
json.dump({'_W': canon(B._W), '_WN': canon(B._WN)}, open(sys.argv[1], 'w'), ensure_ascii=False)

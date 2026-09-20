import os as _os
_ROOT = _os.path.normpath(_os.path.join(_os.path.dirname(_os.path.abspath(__file__)), '..', '..', '..'))   # THE PORTABLE REPO (2026-09-15): the repo root from this file's own place
import sys, os, subprocess, json
ROOT = _ROOT
sys.path.insert(0, os.path.join(ROOT, 'World', 'step9'))
import cold_run_sequence, cold_run_balak as B
out = {}
out['P'] = repr(B.P)
for nm in ('_W', '_WN'):
    w = getattr(B, nm)
    out[nm] = {k: repr(getattr(w, k))[:400] for k in sorted(vars(w))}
json.dump(out, open(sys.argv[1], 'w'), indent=1, ensure_ascii=False)

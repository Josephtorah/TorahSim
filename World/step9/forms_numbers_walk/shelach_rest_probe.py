import os as _os
_ROOT = _os.path.normpath(_os.path.join(_os.path.dirname(_os.path.abspath(__file__)), '..', '..', '..'))   # THE PORTABLE REPO (2026-09-15): the repo root from this file's own place
import sys, io, contextlib, collections
sys.path.insert(0, (_ROOT + '/World/step9'))
with contextlib.redirect_stdout(io.StringIO()):
    import cold_run_sequence as CS
reg = CS.registry_map()
with contextlib.redirect_stdout(io.StringIO()):
    w = CS.rest_world(reg)
cov = w.coverage()
print('THE REST: daemons fired', sorted((n, f) for n, (s, f, k) in cov.items() if f))
fired_kinds = {n: sorted(k) for n, (s, f, k) in cov.items() if f}
print('law_shelach in REST:', cov.get('law_shelach'))
# the writes by writer
wr = collections.Counter(l[2].get('written_by') if isinstance(l[2], dict) else None for l in w.log if l[0] == 'WRITE')
print('WRITE by writer:', sorted(wr.items(), key=lambda x: -x[1])[:60])

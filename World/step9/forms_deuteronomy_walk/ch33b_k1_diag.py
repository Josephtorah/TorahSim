import os as _os
_ROOT = _os.path.normpath(_os.path.join(_os.path.dirname(_os.path.abspath(__file__)), '..', '..', '..'))   # THE PORTABLE REPO (2026-09-15): the repo root from this file's own place
#!/usr/bin/env python3
# THE DEUTERONOMY WALK 21b TAIL: K1's steps repeated by hand — the whole world by run_to(beyond the tape), checkpoints(), the DN and DO rows' declared against computed,
# printed whole (the probe prints the first difference's index alone: 314 = DO1). Reads only; writes nothing (K7). RUN FROM THE REPO ROOT.
import os, sys, io, contextlib, subprocess
ROOT = _ROOT
HERE = os.path.join(ROOT, 'World', 'step9'); sys.path.insert(0, HERE); sys.path.insert(0, os.path.join(ROOT, 'World', 'journal')); sys.path.insert(0, ROOT)
os.chdir(HERE)
with contextlib.redirect_stdout(io.StringIO()):
    import cold_run_sequence as CS
    import checkpoint_probes as KP
target = KP.beyond_the_tape(); print('beyond the tape:', target, flush=True)
with contextlib.redirect_stdout(io.StringIO()):
    w, M, n = CS.run_to(target)
print('run_to done: log lines', len(w.log), 'entities', len(w.entities), 'n', n, flush=True)
with contextlib.redirect_stdout(io.StringIO()):
    rows, _cx = CS.checkpoints(w, M, CS.registry_map())
v = KP.verdicts_of(rows); print('rows', len(rows), '| equal', v == CS.VERDICTS, '| differences:', [(i, a, b) for i, (a, b) in enumerate(zip(v, CS.VERDICTS)) if a != b])
for r in rows:
    nm = r['name'].split(' ')[0]
    if nm.startswith('DO') or nm in ('DN1', 'DN5'):
        print('----', nm, 'ok', r['ok']); print('  declared:', repr(r['declared'])[:1500]); print('  computed:', repr(r['computed'])[:1500])
# the eleven events' log positions and the last Deut 32 line, as DO1 reads them
ev = [(i, l[2]['kind'], l[2].get('case_source', '')[:40], l[1] if len(l) > 1 else None) for i, l in enumerate(w.log) if l[0] == 'EVENT' and str(l[2].get('case_source', '')).startswith('Deut 33:')]
d32 = [i for i, l in enumerate(w.log) if l[0] == 'EVENT' and str(l[2].get('case_source', '')).startswith('Deut 32:')]
print('Deut 33 events in the log:', len(ev), ev[:14]); print('the last Deut 32 event index', max(d32) if d32 else None, '| the log tail kinds', [(l[0], l[2].get('kind') if len(l) > 2 and isinstance(l[2], dict) else None) for l in w.log[-6:]])

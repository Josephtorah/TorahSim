import sys, io, time, contextlib, collections
sys.path.insert(0, '<repo-old>/World/step9'); sys.path.insert(0, '<repo-old>/World/journal'); sys.path.insert(0, '<repo-old>')
t0 = time.time()
with contextlib.redirect_stdout(io.StringIO()):
    import cold_run_sequence as CS
    w, M, n = CS.run_to('Deut 1:1')
t1 = time.time()
buf = io.StringIO()
with contextlib.redirect_stdout(buf):
    rows, cx = CS.checkpoints(w, M, CS.registry_map())
t2 = time.time()
v = ['%s %s' % (r['name'].split(' ')[0], 'MATCH' if r['ok'] else 'DIVERGE') for r in rows]
print('world built in %.1f s (%d log lines); checkpoints() in %.1f s: %d rows; verdicts == VERDICTS: %s; exported %s' % (t1 - t0, n, t2 - t1, len(rows), v == CS.VERDICTS, list(cx)))
if v != CS.VERDICTS:
    print('first difference at', next((i for i, (a, b) in enumerate(zip(v, CS.VERDICTS)) if a != b), None), len(v), len(CS.VERDICTS))
names = [r['name'].split(' ')[0] for r in rows]
print('duplicate prefixes:', [k for k, c in collections.Counter(names).items() if c > 1])
print('the print of the block, first 3 lines:', buf.getvalue().strip().split('\n')[:3])

#!/usr/bin/env python3
"""ink_cache_probes.py — THE VERIFIED-IMPORT CACHE'S OWN PROBES (2026-09-19; ink_cache.py, THE_LOOP D38): the whole engine loaded twice in two fresh
processes — FULL (INK_CACHE=0, every runner's checks run) and CACHED (the verified constants restored) — and compared: every runner's module-level
picklable values in canonical form (sets and dicts sorted — the state, not the byte order), the daemons by module and name, the registry map, and the tape's own verdict line (the checkpoints and RUN). The
cached world must be the full world. Run: python3 World/step9/ink_cache_probes.py — a probe suite (N/N) of the gates chain's probes step."""
import re as _re, ast, os, sys, subprocess, json, hashlib, pickle, time
HERE = os.path.dirname(os.path.abspath(__file__))
DUMP = r'''
import sys, os, io, contextlib, pickle, hashlib, types, json, ast, re as _re
sys.path.insert(0, %r)
with contextlib.redirect_stdout(io.StringIO()):
    import cold_run_sequence as CS
def canon(v, depth=0):
    """a value in a canonical form before hashing: sets and dicts sorted (a set's iteration order changes with the process's hash seed — equal sets pickle to
    different bytes in two processes), objects by class and sorted attributes; the STATE compared, never the byte order"""
    if depth > 40: return _re.sub(r' at 0x[0-9a-f]+', '', repr(v))[:200]
    if isinstance(v, (set, frozenset)): return ('set', sorted((canon(x, depth + 1) for x in v), key=repr))
    if isinstance(v, dict): return ('dict', sorted(((canon(k, depth + 1), canon(x, depth + 1)) for k, x in v.items()), key=repr))
    if isinstance(v, (list, tuple)): return (type(v).__name__, [canon(x, depth + 1) for x in v])
    if isinstance(v, (str, bytes, int, float, bool, type(None))): return v
    if hasattr(v, '__dict__'): return (type(v).__module__ + '.' + type(v).__name__, sorted(((k, canon(x, depth + 1)) for k, x in vars(v).items() if not callable(x)), key=repr))
    return _re.sub(r' at 0x[0-9a-f]+', '', repr(v))[:200]   # an object's address is the process's, never the state's
def chash(v): return hashlib.sha256(repr(canon(v)).encode('utf-8')).hexdigest()[:24]   # over the canonical form's TEXT: a pickle's bytes memoize repeated objects, and two processes intern strings differently
out = {'modules': {}, 'daemons': [(f.__module__, f.__name__) for f in CS.daemons()], 'registry': chash(CS.registry_map()), 'ids': [], 'shared': {}}
for name, mod in sorted(sys.modules.items()):
    if not name.startswith('cold_run_') or not isinstance(mod, types.ModuleType): continue
    vals = {}
    for k, v in vars(mod).items():
        if k.startswith('__') or isinstance(v, (types.ModuleType, types.FunctionType, types.BuiltinFunctionType, type)) or callable(v): continue
        try: pickle.dumps(v, protocol=5); vals[k] = chash(v)
        except Exception: vals[k] = '<unpicklable>'
        if isinstance(v, (list, dict, set)): out['ids'].append((name, k, id(v)))
    out['modules'][name] = vals
import ink_cache as _IC
out['stats'] = {'executed': _IC.STATS['executed'], 'restored': _IC.STATS['restored'], 'slow': sorted(_IC.STATS['slow'], reverse=True)[:6]}
for name in ('world_engine', 'effects_layer', 'events_layer', 'compile_guards', 'world_journal'):   # the engine's own modules: a runner's import-time call into them (a registration) is a side effect the cache must not lose
    mod = sys.modules.get(name)
    if mod is None: continue
    vals = {}
    for k, v in vars(mod).items():
        if k.startswith('__') or isinstance(v, (types.ModuleType, types.FunctionType, types.BuiltinFunctionType, type)) or callable(v): continue
        try: pickle.dumps(v, protocol=5); vals[k] = chash(v)
        except Exception: vals[k] = '<unpicklable>'
    out['shared'][name] = vals
json.dump(out, open(sys.argv[1], 'w'))
'''
def dump(label, env):
    p = os.path.join(os.environ.get('TMPDIR', '/tmp'), 'ink_probe_%s_%d.json' % (label, os.getpid()))
    t = time.time()
    r = subprocess.run([sys.executable, '-c', DUMP % HERE, p], cwd=HERE, env=dict(os.environ, **env), capture_output=True, text=True)
    assert r.returncode == 0, (label, r.stderr[-800:])
    return json.load(open(p)), time.time() - t
results = []
def probe(name, ok, note=''): results.append((name, bool(ok))); print('  %s %s%s' % ('PASS' if ok else 'FAIL', name, (': ' + note) if note else ''))
print('INK CACHE PROBES — the full load against the cached load, two fresh processes')
full, t_full = dump('full', {'INK_CACHE': '0'})
_, t_warm = dump('warm', {'INK_CACHE': '1'})   # a cold cache harvests here (a miss); the load timed and compared is the next one, a hit
cached, t_cached = dump('cached', {'INK_CACHE': '1'})
print('  the full load %.0f s, the warm load (a harvest on a cold cache) %.0f s, the cached load %.0f s' % (t_full, t_warm, t_cached))
print('  the cached load restored %d statements and ran %d; the slowest run: %s' % (cached['stats']['restored'], cached['stats']['executed'], cached['stats']['slow'][:4]))
probe('C1 the same runners loaded', set(full['modules']) == set(cached['modules']), '%d modules' % len(full['modules']))
diffs = [(m, k) for m in full['modules'] for k in full['modules'][m] if full['modules'][m][k] != '<unpicklable>' and cached['modules'].get(m, {}).get(k) != full['modules'][m][k]]
probe('C2 every picklable module value equal in canonical form', not diffs, ('%d values; the first differences: %s' % (sum(len(v) for v in full['modules'].values()), diffs[:6])) if diffs else '%d values compared, nothing set aside' % sum(1 for v in full['modules'].values() for h in v.values() if h != '<unpicklable>'))
missing = [(m, k) for m in full['modules'] for k in full['modules'][m] if full['modules'][m][k] != '<unpicklable>' and k not in cached['modules'].get(m, {})]   # a name that does not pickle (a case table of functions) is the fixpoint's to drop when nothing running reads it
probe('C3 no module name lost on the cached path', not missing, 'the first: %s' % missing[:6] if missing else '')
probe('C4 the daemons the same, by module and name, in order', full['daemons'] == cached['daemons'], '%d daemons' % len(full['daemons']))
probe('C5 the registry map the same', full['registry'] == cached['registry'])
def groups(d):   # the sets of (module, name) that are ONE object — an alias (erection's VS_LEV8 is vestments' LEV8_ORDER) is real sharing in both loads; the cache must add none
    ids = {}
    for m, k, i in d['ids']: ids.setdefault(i, []).append((m, k))
    return {frozenset(v) for v in ids.values() if len(v) > 1}
extra = groups(cached) - groups(full); lost = groups(full) - groups(cached)
probe('C6 the objects shared between names are the same groups in both loads (no sharing added by the cache)', not extra and not lost, 'added: %s; lost: %s' % ([sorted(g)[:3] for g in list(extra)[:2]], [sorted(g)[:3] for g in list(lost)[:2]]) if (extra or lost) else '%d shared groups' % len(groups(full)))
probe('C7 the cached load at least three times faster than the full', t_cached * 3 <= t_full, '%.0f s against %.0f s' % (t_cached, t_full))
sdiffs = [(m, k) for m in full['shared'] for k in full['shared'][m] if full['shared'][m][k] != '<unpicklable>' and cached['shared'].get(m, {}).get(k) != full['shared'][m][k]]
probe("C8 the engine's own modules hold the same state after both loads (no registration lost to a restored statement)", not sdiffs and set(full['shared']) == set(cached['shared']), ('the first differences: %s' % sdiffs[:6]) if sdiffs else '%d values in %s' % (sum(len(v) for v in full['shared'].values()), ', '.join(sorted(full['shared']))))
n = sum(1 for _, ok in results if ok)
print('%d/%d probes' % (n, len(results)))
sys.exit(0 if n == len(results) else 1)

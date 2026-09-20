#!/usr/bin/env python3
"""ink_cache.py — THE VERIFIED-IMPORT CACHE (2026-09-19; the owner: "ok do it make it permanent" after the measurement — the sixty-three runners' import
costs 135 s, all of it the runners' OWN SELF-CHECKS at load: the whole-text scans, the censuses, the asserts, the honest-pairing guard).

THE LAW: A RUNNER'S CHECKS RUN IN FULL WHEN ITS SOURCE OR THE TEXT IT READS HAS MOVED, AND ALWAYS IN THE SWEEP; EVERY OTHER LOADER RESTORES THE RUNNER'S
VERIFIED CONSTANTS AND RUNS ONLY ITS DEFINITIONS. A stamp is written by a successful full import only, keyed on the runner's source digest and the SHARED
KEY (the text store, the shelf's data files, the snapshot store, the engine's modules, the registries). Any move is a miss, and a miss is the full import.

HOW: a meta-path finder for the modules named cold_run_* in this folder (the sequence itself loads before the finder is installed and always runs
whole). With INK_CACHE=0 the module runs whole, natively. On a MISS the module runs statement by statement and after EACH statement the values are
harvested — every name the statement bound or may have mutated, every name a function of the module may mutate (a static scan of its defs: a
mutating method, a subscript or attribute store, an augassign, a global, a call argument), every small container, every container whose length
moved, every object with attributes — each value that pickles (never a module, a function, a class, a connection) into a content-addressed blob
(World/journal/data/ink_cache/, gitignored), recorded on that statement when its content changed; and the OTHER runners whose functions ran inside
the statement (sys.monitoring, one event per code object per statement, re-entrant across the imports a statement nests) have their own mutable
names re-examined and any change recorded on that statement as module::name (a callee's trail appended, its counter moved). An object that IS
another name's live object (a callee's cell value handed out as is, a loop's last value) is recorded as an alias [hash, module, name]; an element
of a value that is one (a self-test's result tuple holding the callee's trail) as a nested alias with its path. The index is written only if
nothing raised. On a HIT the module's top-level statements go one by one: a statement that only BINDS recorded names (an assignment, a loop, a
with-block, a branch), an assert, a print, or a method call on a recorded name is SKIPPED and its names bound from the cache at that point — a
fresh object for a binding, IN PLACE for a name a call had mutated (its identity kept for every alias), the live object for an alias, the callee's
container in place for a module::name entry, and a name passed to a call and unchanged left as it stands; everything else runs as written — imports,
defs, classes, calls into modules, an alias assignment (X = MOD.Y), ANY BLOCK HOLDING AN IMPORT (so the modules load in the full path's order), and
statements binding what does not pickle; THE FIXPOINT un-skips a skipped statement that binds a name some running statement reads without a
recorded value, until nothing moves. THE VALUES ARE EACH STATEMENT'S OWN, never the module's final state. The daemons are functions gathered by
name from the modules (cold_run_sequence.daemons) — defined, never cached. A blob's bytes load once per process; every binding gets ITS OWN
object (a shared object would let one runner's run-time appends fill another's list — the slip that found the rule). INK_CACHE_TRACE=<module,…>
prints every statement's SKIP/EXEC with its names (INK_CACHE_TRACE_FILE the file); STATS holds the counts and the slowest executed statements.

THE HONESTY GUARDS: (1) the sweep (run_cold_all.py) runs every runner with INK_CACHE=0 — the checks in full, every time it grades; (2) the chain's --full
sets INK_CACHE=0 for every step; (3) ink_cache_probes.py imports the whole engine twice — full and cached — in two processes and asserts the modules' values
and the daemons equal — EIGHT PROBES: the same runners, every picklable value equal in canonical form (nothing set aside), no name lost, the daemons, the
registry map, the same sharing groups (no alias gained or lost), three times faster, the engine's own modules' state the same; (4) a stamp is written only by an
import that raised nothing; (5) a cached-path statement that raises names the module, the line and the values it read, and says to run INK_CACHE=0. Usage:
    INK_CACHE=0 python3 …            # the cache off for this process (the sweep's way)
    python3 World/step9/ink_cache.py --status     # the stamps: hits, misses, the blobs' size
    python3 World/step9/ink_cache.py --clear      # every stamp and blob removed (the next import is full)
"""
import ast, hashlib, importlib.abc, importlib.machinery, importlib.util, json, os, pickle, sys, time, types, zlib
HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.normpath(os.path.join(HERE, '..', '..'))
CACHE = os.path.join(ROOT, 'World', 'journal', 'data', 'ink_cache')
ENABLED = os.environ.get('INK_CACHE', '1') not in ('0', 'off', 'no')
_BLOBS = {}            # in-process memo: blob hash -> the decompressed pickle BYTES (the objects are never shared)
_SHARED = None
STATS = {'hit': [], 'miss': [], 'restored': 0, 'executed': 0, 'seconds': 0.0, 'load_seconds': 0.0, 'exec_seconds': 0.0, 'slow': []}
SHARED_FILES = ['world_engine.py', 'effects_layer.py', 'events_layer.py', 'compile_guards.py', 'world_journal.py', 'calendar_parameters.yaml', 'population_schema.yaml']

def _sha(path):
    h = hashlib.sha256()
    with open(path, 'rb') as f:
        for chunk in iter(lambda: f.read(1 << 20), b''): h.update(chunk)
    return h.hexdigest()

def shared_key():
    """the digest of everything a runner may read at import besides its own source: the text store (by content), the Data/ files the runners open
    (by path, size and mtime — 6,000 files, listed), the snapshot store (size, mtime), the engine's modules and the registries (by content)"""
    global _SHARED
    if _SHARED: return _SHARED
    h = hashlib.sha256()
    h.update(_sha(os.path.join(ROOT, 'Data', 'tanakh.sqlite')).encode())
    for dirpath, dirs, files in os.walk(os.path.join(ROOT, 'Data')):
        dirs.sort()
        for f in sorted(files):
            if f == 'tanakh.sqlite': continue
            p = os.path.join(dirpath, f); st = os.stat(p)
            h.update(('%s|%d|%d\n' % (os.path.relpath(p, ROOT), st.st_size, int(st.st_mtime))).encode())
    for f in sorted(os.listdir(ROOT)):
        if f.endswith('.sqlite') and f.startswith('torah_grok'):
            st = os.stat(os.path.join(ROOT, f)); h.update(('%s|%d|%d\n' % (f, st.st_size, int(st.st_mtime))).encode())
    for f in sorted(os.listdir(HERE)):
        if f in SHARED_FILES or f.endswith(('_vocabulary.yaml', '_dispositions.yaml')) or f.startswith(('calendar_parameters', 'population_schema')):
            h.update(f.encode() + b'|' + _sha(os.path.join(HERE, f)).encode() + b'\n')
    reg = os.path.join(ROOT, 'logic', 'corpus', 'entity_registry.yaml')
    if os.path.exists(reg): h.update(b'entity_registry|' + _sha(reg).encode())
    _SHARED = h.hexdigest(); return _SHARED

def _bound_names(node):
    """the names a top-level statement binds at MODULE scope (Store targets, loop and with targets, walrus) — a comprehension's or a lambda's own
    variables are its own and never module names; defs, classes and imports bind too but are never restorable"""
    if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef, ast.ClassDef)): return {node.name}   # a def binds its name only — its body's stores are its locals
    if isinstance(node, (ast.Import, ast.ImportFrom)): return {(a.asname or a.name).split('.')[0] for a in node.names}
    out = set(); stack = [node]
    while stack:
        n = stack.pop()
        if isinstance(n, (ast.ListComp, ast.SetComp, ast.DictComp, ast.GeneratorExp, ast.Lambda, ast.FunctionDef, ast.AsyncFunctionDef, ast.ClassDef)) and n is not node: continue
        if isinstance(n, ast.Name) and isinstance(n.ctx, ast.Store): out.add(n.id)
        elif isinstance(n, ast.NamedExpr): out.add(n.target.id)
        stack.extend(ast.iter_child_nodes(n))
    return out

def _is_print(node): return isinstance(node, ast.Expr) and isinstance(node.value, ast.Call) and isinstance(node.value.func, ast.Name) and node.value.func.id == 'print'
def _method_on(node):
    """an expression statement that calls a method on a plain name (X.append(...), X.update(...)) — the name it mutates, else None"""
    if isinstance(node, ast.Expr) and isinstance(node.value, ast.Call) and isinstance(node.value.func, ast.Attribute) and isinstance(node.value.func.value, ast.Name):
        return node.value.func.value.id
    return None

RESTORABLE = (ast.Assign, ast.AnnAssign, ast.AugAssign, ast.For, ast.While, ast.With, ast.If, ast.Try, ast.Assert, ast.Expr)

def _picklable(v):
    if isinstance(v, (types.ModuleType, types.FunctionType, types.BuiltinFunctionType, types.MethodType, type)) or (callable(v) and not isinstance(v, (dict, list, tuple, set, frozenset, str, bytes, int, float))): return None
    try:
        return pickle.dumps(v, protocol=5)
    except Exception:
        return None

def _base(e):
    """the plain name at the root of an expression chain — X in X[k].append, X.a.b, X.setdefault(k, []).append — else None"""
    while True:
        if isinstance(e, ast.Name): return e.id
        if isinstance(e, (ast.Subscript, ast.Attribute)): e = e.value
        elif isinstance(e, ast.Call): e = e.func
        else: return None

def _touched(node):
    """the module-level names a statement may MUTATE without binding them: the root name of a method call's target (X.append(...),
    X[k].append(...), X.setdefault(k, []).append(...)), of a subscript store or delete (X[k] = v; del X[k][j]), of an augmented target
    (X[k] += 1), and any plain name passed as an argument to a call (f(X) — conservative)"""
    out = set()
    for n in ast.walk(node):
        if isinstance(n, ast.Call):
            if isinstance(n.func, ast.Attribute):
                b = _base(n.func.value)
                if b: out.add(b)
            for a in n.args:
                if isinstance(a, ast.Name): out.add(a.id)
        elif isinstance(n, ast.Subscript) and isinstance(n.ctx, (ast.Store, ast.Del)):
            b = _base(n.value)
            if b: out.add(b)
        elif isinstance(n, ast.AugAssign):
            b = _base(n.target)
            if b: out.add(b)
    return out

def _index_path(name): return os.path.join(CACHE, name + '.json')
def _blob_path(h): return os.path.join(CACHE, 'blobs', h + '.pz')

def _load_blob(h):
    """a FRESH object for every binding (the bytes are memoized, the object is not): two runners' empty lists must never be one list — a runner's
    trail is appended at run time, and a shared object would fill every runner's (the slip that found this rule)"""
    t = time.time()
    if h not in _BLOBS:
        with open(_blob_path(h), 'rb') as f: _BLOBS[h] = zlib.decompress(f.read())
    v = pickle.loads(_BLOBS[h]); STATS['load_seconds'] += time.time() - t
    return v

IDENT = {}   # id(object) -> (object, module, name): the FIRST module-level name an object was recorded or restored under — the origin an alias points to
_MISSING = object()
def _shareable(v): return isinstance(v, (list, dict, set)) or (hasattr(v, '__dict__') and not isinstance(v, (types.ModuleType, types.FunctionType, type)))
def _identity(v, name, n):
    """the (module, name) this object already lives under when it IS another name's live object (a callee's cell value handed out as is — erection's
    VS_E29 is vestments' E29_ORDER; a loop's last value is the table's cell): the cached path binds THAT object, never a copy; None for an atom or a
    first appearance; None too when the origin name has moved on (the object verified live under it, here and now)"""
    if not _shareable(v): return None
    ent = IDENT.get(id(v))
    if ent is None or ent[0] is not v or (ent[1], ent[2]) == (name, n): return None
    src = sys.modules.get(ent[1])
    if src is None or src.__dict__.get(ent[2], _MISSING) is not v: return None
    return [ent[1], ent[2]]
def _register(v, name, n):
    if _shareable(v): IDENT.setdefault(id(v), (v, name, n))   # the reference held: the id is never reused while the entry stands

FORM = 7
MUTABLES = {}          # runner -> the module-level names its own functions may mutate (the static scan: a mutating method, a subscript or attribute store, an augassign, a global, a call argument)
CROSS_LAST = {}        # (runner, name) -> the hash last recorded for it, in this process — the baseline a callee's mutation is measured against
_SIZE = {}             # blob hash -> the pickle's length (a small container is re-examined after every statement)
_MUT_METHODS = {'append', 'extend', 'insert', 'pop', 'remove', 'clear', 'sort', 'reverse', 'update', 'setdefault', 'add', 'discard', 'popitem'}
def _mutables(tree):
    out = set()
    def root(e):
        while isinstance(e, (ast.Attribute, ast.Subscript)): e = e.value
        return e.id if isinstance(e, ast.Name) else None
    for fn in ast.walk(tree):
        if not isinstance(fn, (ast.FunctionDef, ast.AsyncFunctionDef, ast.Lambda)): continue
        for x in ast.walk(fn):
            if isinstance(x, ast.Call):
                if isinstance(x.func, ast.Attribute) and x.func.attr in _MUT_METHODS:
                    r = root(x.func.value)
                    if r: out.add(r)
                for a in x.args:
                    if isinstance(a, ast.Name): out.add(a.id)
            elif isinstance(x, (ast.Assign, ast.AugAssign, ast.Delete, ast.AnnAssign)):
                for t in (x.targets if isinstance(x, (ast.Assign, ast.Delete)) else [x.target]):
                    if isinstance(t, (ast.Subscript, ast.Attribute)):
                        r = root(t.value)
                        if r: out.add(r)
            elif isinstance(x, ast.Global): out.update(x.names)
    return out
_MON = sys.monitoring; _TOOL = 4; _RAN_STACK = []; _MON_ON = []   # a stack: a statement's import nests whole harvests inside it, and each level keeps its own set
def _mon_cb(code, offset):
    if _RAN_STACK: _RAN_STACK[-1].add(code.co_filename)
    return _MON.DISABLE   # once per code object per statement (restart_events re-arms it)
def _mon_on():
    if _MON_ON: return
    _MON.use_tool_id(_TOOL, 'ink_cache'); _MON.register_callback(_TOOL, _MON.events.PY_START, _mon_cb); _MON_ON.append(True)
def _nested(v, name, n, path=(), depth=0, out=None):
    """the elements of a value that ARE other names' live objects (a self-test's result tuple holding the callee's trail): [path, module, name] each"""
    if out is None: out = []
    if depth >= 4 or len(out) >= 64: return out
    if isinstance(v, (list, tuple)): items = enumerate(v)
    elif isinstance(v, dict): items = ((k, x) for k, x in v.items() if isinstance(k, (str, int)))
    else: return out
    for i, (k, x) in enumerate(items):
        if i >= 500: break
        if _shareable(x):
            ident = _identity(x, name, n)
            if ident: out.append([list(path) + [k], ident[0], ident[1]]); continue
        if isinstance(x, (list, tuple, dict)): _nested(x, name, n, path + (k,), depth + 1, out)
    return out
def _patch(obj, path, target):
    if not path: return target
    k = path[0]
    try: child = obj[k]
    except (KeyError, IndexError, TypeError): return obj
    new = _patch(child, path[1:], target)
    if new is child: return obj
    if isinstance(obj, tuple): return obj[:k] + (new,) + obj[k + 1:]
    obj[k] = new; return obj
def _bind(d, n, new, in_place):
    """a value into a namespace: in place (the object's identity kept — every alias sees the change) when the name already holds one of the same type
    and the statement did not bind it afresh"""
    cur = d.get(n, _MISSING)
    if in_place and cur is not _MISSING and type(cur) is type(new) and cur is not new:
        if isinstance(cur, list): cur[:] = new; return
        if isinstance(cur, (dict, set)): cur.clear(); cur.update(new); return
        if hasattr(cur, '__dict__') and not isinstance(cur, type): cur.__dict__.clear(); cur.__dict__.update(new.__dict__); return
    d[n] = new

def _store(v):
    """a value into a content-addressed blob; its hash, or None when it does not pickle"""
    b = _picklable(v)
    if b is None: return None
    h = hashlib.sha256(b).hexdigest()[:32]
    _SIZE[h] = len(b)
    p = _blob_path(h)
    if not os.path.exists(p):
        tmp = p + '.%d.tmp' % os.getpid()
        with open(tmp, 'wb') as f: f.write(zlib.compress(b, 1))
        os.replace(tmp, p)
    return h

class InkCacheLoader(importlib.abc.Loader):
    def __init__(self, path): self.path = path
    def create_module(self, spec): return None
    def exec_module(self, module):
        t0 = time.time()
        name = module.__name__
        src = open(self.path, encoding='utf-8').read()
        key = hashlib.sha256(src.encode('utf-8')).hexdigest() + '|' + shared_key() + ('|' + _sha(os.path.join(ROOT, 'World', 'step9', 'cold_run_sequence.py')) if 'cold_run_sequence.py' in src else '')   # THE DEUTERONOMY WALK 7b (2026-09-19): THE EIGHTEENTH SLIP — a runner that READS THE SEQUENCE FILE at import (the INK block, the stitcher's way: _SRC) restored the OLD text after the tape was re-stitched (ink_cache_probes C2 fell on _SRC in every such module): the sequence file's digest joins the key for those modules alone
        idx = None
        if ENABLED and os.path.exists(_index_path(name)):
            try:
                cand = json.load(open(_index_path(name), encoding='utf-8'))
                if cand.get('key') == key and cand.get('form') == FORM and all(os.path.exists(_blob_path(h if isinstance(h, str) else h[0])) for rec in cand['stmts'].values() for h in rec.values() if h is not None): idx = cand
            except Exception: idx = None
        if not ENABLED:
            exec(compile(src, self.path, 'exec'), module.__dict__); STATS['miss'].append(name); STATS['seconds'] += time.time() - t0; return
        tree = ast.parse(src)
        MUTABLES[name] = _mutables(tree) if name not in MUTABLES else MUTABLES[name]
        if idx is None:
            # THE FULL IMPORT, statement by statement: every check runs; after each statement the names it bound or may have mutated are pickled AS OF
            # THAT STATEMENT (a name bound twice keeps both values at their own places); the index is written only if nothing raised
            os.makedirs(os.path.join(CACHE, 'blobs'), exist_ok=True)
            stmts = {}; last = {}; lens = {}; _mon_on()
            for pos, node in enumerate(tree.body):
                _RAN_STACK.append(set()); _MON.restart_events()
                if len(_RAN_STACK) == 1: _MON.set_events(_TOOL, _MON.events.PY_START)
                try: exec(compile(ast.Module(body=[node], type_ignores=[]), self.path, 'exec'), module.__dict__)
                finally:
                    ran_files = _RAN_STACK.pop()
                    if _RAN_STACK: _RAN_STACK[-1] |= ran_files   # the outer statement ran everything its nested statements ran
                    else: _MON.set_events(_TOOL, 0)
                ran = {os.path.basename(f)[:-3] for f in ran_files if f.startswith(HERE) and os.path.basename(f).startswith('cold_run_')} - {name}   # the OTHER runners whose functions ran inside this statement (a callee appends its trail, counts its provenance)
                names = _bound_names(node) | _touched(node)
                # a self-test mutates through the functions it calls — nothing in its own source names the container: every name a function of this module
                # may mutate (the static scan), every small container, every container whose length moved and every object with attributes is re-examined
                # after each statement, and recorded when changed
                for n, v in list(module.__dict__.items()):
                    if n.startswith('__') or n in names: continue
                    if isinstance(v, (list, dict, set)):
                        if n in MUTABLES[name] or lens.get(n) != len(v) or _SIZE.get(last.get(n), 1 << 30) < 4096: names.add(n)
                    elif hasattr(v, '__dict__') and not isinstance(v, (types.ModuleType, types.FunctionType, type)) and not callable(v): names.add(n)
                rec = {}
                for n in names:
                    if n in module.__dict__ and not n.startswith('__'):
                        v = module.__dict__[n]
                        h = _store(v)
                        if h is None: continue
                        if isinstance(v, (list, dict, set)): lens[n] = len(v)
                        if last.get(n) != h or n in _bound_names(node):
                            ident = _identity(v, name, n)   # [hash, module, name]: the object IS another name's live object — the cached path binds that object
                            nested = [] if ident else _nested(v, name, n)   # [hash, None, None, [[path, module, name], …]]: an element of it is (a callee's trail returned by reference)
                            rec[n] = [h] + ident if ident else ([h, None, None, nested] if nested else h)
                            last[n] = h; CROSS_LAST[(name, n)] = h; _register(v, name, n)
                        elif n in _touched(node): rec[n] = None   # passed to a call and UNCHANGED: recorded as kept — the cached path leaves the object as it stands (an alias stays one object)
                for A in sorted(ran):   # the callees' own mutables, re-examined: a change is recorded on THIS statement as module::name and restored in place there
                    am = sys.modules.get(A)
                    if am is None: continue
                    for x in MUTABLES.get(A, ()):
                        v = am.__dict__.get(x, _MISSING)
                        if v is _MISSING or not _shareable(v): continue
                        h = _store(v)
                        if h is None: continue
                        if CROSS_LAST.get((A, x)) != h:
                            if (A, x) in CROSS_LAST: rec[A + '::' + x] = h
                            CROSS_LAST[(A, x)] = h
                if rec or isinstance(node, ast.Assert) or _is_print(node): stmts[str(pos)] = rec   # keyed by the statement's position, never its line (two statements may share a line)
            tmp = _index_path(name) + '.%d.tmp' % os.getpid()
            with open(tmp, 'w', encoding='utf-8') as f: json.dump({'key': key, 'form': FORM, 'when': time.strftime('%Y-%m-%d %H:%M'), 'stmts': stmts}, f)
            os.replace(tmp, _index_path(name))
            STATS['miss'].append(name)
        else:
            stmts = idx['stmts']
            body = list(tree.body)
            recs = [stmts.get(str(k)) for k in range(len(body))]
            bound = [_bound_names(n) for n in body]; touched = [_touched(n) for n in body]
            loads = [{x.id for x in ast.walk(n) if isinstance(x, ast.Name) and isinstance(x.ctx, ast.Load)} for n in body]
            data_names = set()   # the names some statement RECORDED (picklable data) — a module, a function, a live connection is no restore target: a
            for rec in recs:     # statement that only reads through such a name (db.execute(...)) is skippable when its own bindings are recorded
                if rec: data_names |= set(rec)
            skip = []
            for k, node in enumerate(body):
                rec = recs[k]; ok = False
                if rec is not None and isinstance(node, RESTORABLE) and not (isinstance(node, ast.Assign) and isinstance(node.value, (ast.Name, ast.Attribute))) and not any(isinstance(x, (ast.Import, ast.ImportFrom)) for x in ast.walk(node)):   # an alias runs; a block holding an import runs (the modules load in the full path's order — a callee's trail is written by the calls after the import, and an alias resolves against a module already loaded)
                    if isinstance(node, ast.Assert) or _is_print(node): ok = True
                    elif isinstance(node, ast.Expr):
                        m = _method_on(node); ok = m is not None and m in rec
                    elif bound[k]: ok = all(n in rec for n in bound[k] if n in data_names) and all(t in rec for t in touched[k] if t in data_names)   # every bound or mutated data name recorded at THIS statement; a name recorded nowhere (a world, a function) is the fixpoint's; a module as a call's base is no mutation
                skip.append(ok)
            # THE FIXPOINT: a name a RUNNING statement reads (an import, a def's body, a class, a call, anything executed) must be bound — a skipped statement that
            # binds it without a recorded value (it did not pickle: a world, a function) is unskipped, and the unskipping repeats until nothing moves
            while True:
                needed = set()
                for k in range(len(body)):
                    if not skip[k]: needed |= loads[k]
                moved = False
                for k in range(len(body)):
                    if skip[k] and any(n in needed and n not in recs[k] for n in bound[k]): skip[k] = False; moved = True
                if not moved: break
            trace = name in os.environ.get('INK_CACHE_TRACE', '').split(',')
            for k, node in enumerate(body):
                if trace: print('  ink_cache %s line %d %s %s bound=%s touched=%s rec=%s' % (name, node.lineno, 'SKIP' if skip[k] else 'EXEC', type(node).__name__, sorted(bound[k])[:6], sorted(touched[k])[:6], sorted(recs[k])[:6] if recs[k] else None), file=open(os.environ.get('INK_CACHE_TRACE_FILE', '/dev/stderr'), 'a'))
                if skip[k]:
                    for n, h in recs[k].items():
                        if h is None: continue   # kept as it stands
                        if '::' in n:   # a callee's container the statement's call mutated: restored IN PLACE in the callee (its identity kept for every alias)
                            A, x = n.split('::', 1); am = sys.modules.get(A)
                            if am is not None: _bind(am.__dict__, x, _load_blob(h), True); CROSS_LAST[(A, x)] = h
                            continue
                        hh = h if isinstance(h, str) else h[0]
                        if isinstance(h, list) and h[1] is not None:   # an alias: the live object under (module, name), as the harvest saw it; the blob only if that name is gone
                            srcm = sys.modules.get(h[1]); o = srcm.__dict__.get(h[2], _MISSING) if srcm is not None else _MISSING   # THE DEUTERONOMY WALK 8b (2026-09-20): srcm, not src — the module's SOURCE TEXT `src` was shadowed here and at the patch loop, so the cached path's own error report (a node raising) and the slow-node record crashed on get_source_segment(a module): THE NINETEENTH SLIP, the cache's own reporting; FORM unmoved
                            module.__dict__[n] = o if o is not _MISSING else _load_blob(hh)
                        else:
                            o = _load_blob(hh)
                            if isinstance(h, list) and len(h) > 3:
                                for path, mod, nm in h[3]:
                                    srcm = sys.modules.get(mod)
                                    if srcm is not None and nm in srcm.__dict__: o = _patch(o, path, srcm.__dict__[nm])
                            _bind(module.__dict__, n, o, n not in bound[k])   # a name re-recorded because a call mutated it keeps its object; a binding is a fresh object
                        _register(module.__dict__[n], name, n); CROSS_LAST[(name, n)] = hh
                    STATS['restored'] += 1
                else:
                    te = time.time()
                    try:
                        exec(compile(ast.Module(body=[node], type_ignores=[]), self.path, 'exec'), module.__dict__)
                    except BaseException as e:
                        raise RuntimeError('ink_cache: %s line %d (%s) raised on the cached path: %r; the names it reads: %s — run INK_CACHE=0 or clear the cache' % (name, node.lineno, ast.get_source_segment(src, node).split(chr(10))[0][:100], e, {n: repr(module.__dict__.get(n))[:90] for n in sorted(loads[k]) if n in module.__dict__ and not isinstance(module.__dict__[n], (types.ModuleType, types.FunctionType, type))})) from e
                    STATS['executed'] += 1; te = time.time() - te; STATS['exec_seconds'] += te
                    if te > 0.3: STATS['slow'].append((round(te, 1), name, node.lineno, ast.get_source_segment(src, node).split(chr(10))[0][:80]))
                    for n, h in (recs[k] or {}).items():
                        if h is None or '::' in n or n not in module.__dict__: continue
                        _register(module.__dict__[n], name, n); CROSS_LAST[(name, n)] = h if isinstance(h, str) else h[0]
            STATS['hit'].append(name)
        STATS['seconds'] += time.time() - t0

class InkCacheFinder(importlib.abc.MetaPathFinder):
    def find_spec(self, fullname, path=None, target=None):
        if not fullname.startswith('cold_run_') or '.' in fullname: return None
        p = os.path.join(HERE, fullname + '.py')
        if not os.path.exists(p): return None
        return importlib.util.spec_from_file_location(fullname, p, loader=InkCacheLoader(p))

def install():
    if not any(isinstance(f, InkCacheFinder) for f in sys.meta_path): sys.meta_path.insert(0, InkCacheFinder())

def status():
    idx = sorted(f[:-5] for f in os.listdir(CACHE) if f.endswith('.json')) if os.path.isdir(CACHE) else []
    blobs = os.path.join(CACHE, 'blobs'); nb = len(os.listdir(blobs)) if os.path.isdir(blobs) else 0
    size = sum(os.path.getsize(os.path.join(blobs, f)) for f in os.listdir(blobs)) if os.path.isdir(blobs) else 0
    key = shared_key()
    current = sum(1 for n in idx if json.load(open(_index_path(n), encoding='utf-8')).get('key', '').endswith(key))

    print('INK CACHE: %d runners stamped (%d current under the shared key %s…), %d blobs, %.1f MB; enabled=%s; cache dir %s' % (len(idx), current, key[:12], nb, size / 1e6, ENABLED, CACHE))

def clear():
    import shutil
    if os.path.isdir(CACHE): shutil.rmtree(CACHE)
    print('INK CACHE cleared —', CACHE)

if __name__ == '__main__':
    if '--clear' in sys.argv: clear()
    else: status()

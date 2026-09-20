import os as _os
_ROOT = _os.path.normpath(_os.path.join(_os.path.dirname(_os.path.abspath(__file__)), '..', '..', '..'))   # THE PORTABLE REPO (2026-09-15): the repo root from this file's own place
import ast, os, sys, subprocess, glob, collections
ROOT = _ROOT; HERE = os.path.join(ROOT, 'World', 'step9')
MUT = {'append', 'extend', 'insert', 'pop', 'remove', 'clear', 'sort', 'reverse', 'update', 'setdefault', 'add', 'discard', 'popitem'}
def mutables(tree):
    """(module alias or None, name) pairs a function body of this module may mutate: a mutating method, a subscript or attribute store, an augassign, a global, a call argument"""
    aliases = {a.asname or a.name: a.name for x in ast.walk(tree) if isinstance(x, ast.Import) for a in x.names if a.name.startswith('cold_run_')}
    out = set()
    def root(e):
        if isinstance(e, ast.Name): return (None, e.id)
        if isinstance(e, ast.Attribute) and isinstance(e.value, ast.Name) and e.value.id in aliases: return (aliases[e.value.id], e.attr)
        if isinstance(e, (ast.Attribute, ast.Subscript)): return root(e.value)
        return None
    for fn in ast.walk(tree):
        if not isinstance(fn, (ast.FunctionDef, ast.AsyncFunctionDef, ast.Lambda)): continue
        for x in ast.walk(fn):
            if isinstance(x, ast.Call):
                if isinstance(x.func, ast.Attribute) and x.func.attr in MUT:
                    r = root(x.func.value); r and out.add(r)
                for a in x.args:
                    if isinstance(a, ast.Name): out.add((None, a.id))
            elif isinstance(x, (ast.Assign, ast.AugAssign, ast.Delete, ast.AnnAssign)):
                for t in (x.targets if isinstance(x, (ast.Assign, ast.Delete)) else [x.target]):
                    if isinstance(t, (ast.Subscript, ast.Attribute)):
                        r = root(t.value); r and out.add(r)
            elif isinstance(x, ast.Global): out.update((None, n) for n in x.names)
    return out
tot = collections.Counter(); ex = {}
for p in sorted(glob.glob(os.path.join(HERE, 'cold_run_*.py'))):
    m = mutables(ast.parse(open(p, encoding='utf-8').read()))
    top = {n for k, n in m if k is None}; cross = {(k, n) for k, n in m if k}
    tot['own'] += len(top); tot['cross'] += len(cross); ex[os.path.basename(p)] = (sorted(top)[:12], sorted(cross)[:4])
print(tot); import itertools
for k, v in itertools.islice(ex.items(), 0, 8): print(k, v)

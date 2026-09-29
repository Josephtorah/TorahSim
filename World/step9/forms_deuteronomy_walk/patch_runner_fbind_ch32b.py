import os as _os
_ROOT = _os.path.normpath(_os.path.join(_os.path.dirname(_os.path.abspath(__file__)), '..', '..', '..'))   # THE PORTABLE REPO (2026-09-15): the repo root from this file's own place
#!/usr/bin/env python3
"""patch_runner_fbind_ch32b.py — THE DEUTERONOMY WALK 20b's tail (2026-09-28): THE CALLEE BINDINGS RETYPED AS ASSIGNMENTS. The song's runner bound
its callees' values through F('NAME', value) — a helper writing globals(): a binding the import cache's skip cannot see (it reads a statement's ast
Store targets), so every such statement RAN on the cached path and held the LIVE callee object while the older runners' names for the same DATA rows
(covenant_return_charge's JR_FOUR, JR_DEATH and OH_CHAIN; refuge_war_family's and courts_prophet's RG_ONE) were restored copies — the cache probe C6
read the sharing groups lost on the chain's second pass, after the cache had been cleared whole (18b's lesson 11 did not reach it). The fix, by ast:
every module-level F('NAME', expr) becomes `NAME = expr; F('NAME', NAME)` and F's globals() write is removed — the name bound by assignment (the
older runners' form), the fact recorded beside it. --check prints only. Run from the repo root."""
import ast, sys, subprocess
ROOT = _ROOT
P = f'{ROOT}/World/step9/cold_run_song_charge_nebo.py'
CHECK = '--check' in sys.argv
src = open(P, encoding='utf-8').read()
t = ast.parse(src)
allF = [n for n in ast.walk(t) if isinstance(n, ast.Call) and isinstance(n.func, ast.Name) and n.func.id == 'F']
top = [n for n in t.body if isinstance(n, ast.Expr) and isinstance(n.value, ast.Call) and isinstance(n.value.func, ast.Name) and n.value.func.id == 'F']
print('F calls in the file: %d; module-level F statements: %d (lines %d-%d)' % (len(allF), len(top), top[0].lineno, top[-1].lineno))
assert len(allF) == len(top), ('F CALLED OUTSIDE THE MODULE LEVEL', len(allF), len(top))
for n in top:
    assert len(n.value.args) == 2 and not n.value.keywords and isinstance(n.value.args[0], ast.Constant) and isinstance(n.value.args[0].value, str) and n.value.args[0].value.isidentifier(), ast.get_source_segment(src, n)[:120]
names = [n.value.args[0].value for n in top]; assert len(set(names)) == len(names), 'a name bound twice'
already_name = [n.value.args[0].value for n in top if isinstance(n.value.args[1], ast.Name)]
b = src.encode('utf-8'); starts = [0]
for line in b.split(b'\n'): starts.append(starts[-1] + len(line) + 1)
def span(n): return starts[n.lineno - 1] + n.col_offset, starts[n.end_lineno - 1] + n.end_col_offset
edits = 0
for n in sorted(top, key=lambda n: span(n)[0], reverse=True):
    s, e = span(n); name = n.value.args[0].value; seg2 = ast.get_source_segment(src, n.value.args[1])
    assert b[s:e].decode('utf-8').startswith("F(%r" % name) and seg2 in b[s:e].decode('utf-8'), (name, b[s:e][:80])
    b = b[:s] + ('%s = %s; F(%r, %s)' % (name, seg2, name, name)).encode('utf-8') + b[e:]; edits += 1
new = b.decode('utf-8')
OLD_F = 'def F(name, val):\n    globals()[name] = val; FACTS_PRINT.append('
assert new.count(OLD_F) == 1, new.count(OLD_F)
COMMENT = ("# THE DEUTERONOMY WALK 20b's tail (2026-09-28): THE MODULE-LEVEL NAME IS BOUND BY ASSIGNMENT beside this call, never through globals() — the import\n"
           "# cache's skip reads a statement's ast Store targets; a name bound through a call RAN on the cached path and held the live callee object while the older\n"
           "# runners' names for the same DATA rows (covenant_return_charge's JR_FOUR, JR_DEATH, OH_CHAIN; refuge_war_family's and courts_prophet's RG_ONE) were\n"
           "# restored copies, and the cache probe C6 read the sharing groups lost on the chain's second pass after the cache was cleared whole (18b's lesson 11 did\n"
           "# not reach it). Retyped by patch_runner_fbind_ch32b.py: every F('NAME', expr) above became `NAME = expr; F('NAME', NAME)`; F records the fact alone.\n")
new = new.replace(OLD_F, COMMENT + 'def F(name, val):\n    FACTS_PRINT.append(')
t2 = ast.parse(new)
assigned = {x.id for n in t2.body if isinstance(n, ast.Assign) for x in n.targets if isinstance(x, ast.Name)}
assert set(names) <= assigned, sorted(set(names) - assigned)[:8]
top2 = [n for n in t2.body if isinstance(n, ast.Expr) and isinstance(n.value, ast.Call) and isinstance(n.value.func, ast.Name) and n.value.func.id == 'F']
assert len(top2) == len(top) and all(isinstance(n.value.args[1], ast.Name) and n.value.args[1].id == n.value.args[0].value for n in top2)
fdef = next(n for n in t2.body if isinstance(n, ast.FunctionDef) and n.name == 'F'); assert 'globals' not in ast.get_source_segment(new, fdef)
compile(new, P, 'exec')
print('names already bound to a plain name (an alias that runs): %s' % (already_name,))
print('the file %d -> %d bytes; the def F at line %d' % (len(src.encode()), len(new.encode()), fdef.lineno))
if CHECK: print('edits %d over lines %d-%d; F\'s globals write removed | CHECK ONLY' % (edits, top[0].lineno, top[-1].lineno))
else:
    open(P, 'w', encoding='utf-8').write(new)
    print('edits %d over lines %d-%d; F\'s globals write removed | WRITTEN' % (edits, top[0].lineno, top[-1].lineno))

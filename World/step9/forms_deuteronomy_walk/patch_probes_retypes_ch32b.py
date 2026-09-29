import os as _os
_ROOT = _os.path.normpath(_os.path.join(_os.path.dirname(_os.path.abspath(__file__)), '..', '..', '..'))   # THE PORTABLE REPO (2026-09-15): the repo root from this file's own place
#!/usr/bin/env python3
# THE DEUTERONOMY WALK 20b (2026-09-28; LEAN) — THE TAIL, after the gates chain's first pass: THE READBACK PROBES MOVED BY THE SONG'S REUSES AND ITS RAIN, RETYPED FROM THE
# PROBES' OWN PRINT (the chain's probe_readback.out: 45/49 — Q20, Q30, Q47, Q48 FAIL; Q49, this sitting's, PASSES): heaven_and_earth_witness 4 -> 5 on Israel by THE CHAIN
# OF WITNESSES' FIFTH SEAT at 32:1 (Q20's count and the LAST entry's source head at ten characters — the song's line's range head, its tenth character the hyphen; Q47's kin
# tuple's fifteenth; Q48's RE list — its number sits inside a generator expression, retyped BY NAME from the print's tuple); THE SONG'S DOCTRINE AS RAIN joins chapter 11's two
# rain lists (Q30 — doctrine_as_rain_and_dew_likened on Israel's ledger and in the registry: both lists replaced whole from the print); THE TWO HEAVEN REUSES
# (face_hidden_and_forsaken_foretold 32:20, length_of_days_on_the_land_promised 32:47) — Q48's heaven count and its w59 generator's two seats at 2, BY NAME (19b's Q47 form:
# an element inside a generator expression hides from the walker — 19b's lesson 16, met before the chain's second pass this time).
# THE METHOD (19b's, by ast): each failing probe's `return got == (…)` literal walked beside the print's got tuple — a CONSTANT element that differs is replaced by the print's
# value; a tuple or list recursed, a list whose length differs replaced whole; an expression (a call, a name) left alone; then the generator-hidden numbers of q48 read from the
# print and substituted by name inside q48's own span; a 20b comment line above each return. --check prints only. RUN FROM THE REPO ROOT.
import re, ast, sys, os, subprocess
ROOT = _ROOT
SP = os.path.dirname(os.path.abspath(__file__))
CHECK = '--check' in sys.argv
F = f'{ROOT}/World/step9/readback_probes.py'; src = open(F, encoding='utf-8').read()
PRINT = sys.argv[sys.argv.index('--print') + 1] if '--print' in sys.argv else f'{SP}/ch32b_gates/probe_readback.out'
PR = open(PRINT, encoding='utf-8').read().split('\n')
GOT = {}
for l in PR:
    m = re.match(r'\s*FAIL (Q\d+) .*? = (\(.*\))\s*$', l)
    if m:
        try: GOT[m.group(1).lower()] = ast.literal_eval(m.group(2))
        except Exception as e: print('UNPARSED', m.group(1), str(e)[:80], m.group(2)[:120])
print('failing probes read from the print:', sorted(GOT, key=lambda q: int(q[1:])))
assert GOT and 'q49' not in GOT and set(GOT) == {'q20', 'q30', 'q47', 'q48'}, sorted(GOT)
lines = src.split('\n'); starts = [0]
for l in lines: starts.append(starts[-1] + len(l) + 1)
def boff(ln, col):
    b = lines[ln - 1].encode('utf-8'); return starts[ln - 1] + len(b[:col].decode('utf-8'))
def walk(node, got, path=()):
    if isinstance(node, ast.Constant):
        if node.value != got and type(node.value) in (int, str, bool, float) and type(got) in (int, str, bool, float, tuple, list):
            return [(boff(node.lineno, node.col_offset), boff(node.end_lineno, node.end_col_offset), repr(got), path, node.value)]
        return []
    if isinstance(node, (ast.Tuple, ast.List)) and isinstance(got, (tuple, list)):
        if len(node.elts) != len(got):
            return [(boff(node.lineno, node.col_offset), boff(node.end_lineno, node.end_col_offset), repr(got if isinstance(node, ast.Tuple) else list(got)), path, '<%d elements>' % len(node.elts))]
        out = []
        for k, (e, g) in enumerate(zip(node.elts, got)): out += walk(e, g, path + (k,))
        return out
    return []   # an expression — left alone
tree = ast.parse(src); edits = []; report = []; ret_lines = {}; fns = {}
for fn in [n for n in tree.body if isinstance(n, ast.FunctionDef) and n.name in GOT]:
    fns[fn.name] = fn
    rets = [n for n in ast.walk(fn) if isinstance(n, ast.Return) and isinstance(n.value, ast.Tuple) and isinstance(n.value.elts[0], ast.Compare)]
    assert len(rets) == 1, (fn.name, len(rets))
    cmp = rets[0].value.elts[0]; lit = cmp.comparators[0]
    e = walk(lit, GOT[fn.name])
    edits += e; ret_lines[fn.name] = rets[0].lineno
    report.append((fn.name, [(p, old, new[:70]) for a, b, new, p, old in e]))
    if not e: print('   NO CONSTANT DIFFERS in', fn.name, '— an expression hides the change')
for r in report: print(r)
paths = {q: [p for _, _, _, p, _ in e_] for q, e_ in ((r[0], [t for t in edits if t[3] in [x[0] for x in r[1]]]) for r in report)}
P = {q: sorted(p for p, _, _ in r[1]) for q, r in zip([r[0] for r in report], report)}
assert P['q20'] == [(7,), (10,)] and P['q30'] == [(1,), (2,)] and P['q47'] == [(10, 14)] and P['q48'] == [(9,)], P   # the walker's finds, as the print's diff names them
# ---- q48's GENERATOR-HIDDEN NUMBERS, BY NAME FROM THE PRINT ----
q48 = fns['q48']; got48 = GOT['q48']
RE_node = next(n for n in ast.walk(q48) if isinstance(n, ast.Assign) and getattr(n.targets[0], 'id', None) == 'RE').value
RE_names = [e.elts[0].value for e in RE_node.elts]; RE_old = [e.elts[1].value for e in RE_node.elts]; RE_new = list(got48[7])
assert len(RE_names) == len(RE_new) == 7, (len(RE_names), len(RE_new))
for e, old, new in zip(RE_node.elts, RE_old, RE_new):
    if old != new:
        c = e.elts[1]; edits.append((boff(c.lineno, c.col_offset), boff(c.end_lineno, c.end_col_offset), repr(new), ('RE', e.elts[0].value), old)); print('   q48 RE', e.elts[0].value, old, '->', new)
RE_moved = [(n, o, w) for n, o, w in zip(RE_names, RE_old, RE_new) if o != w]; assert len(RE_moved) == 1 and RE_moved[0][0] == 'heaven_and_earth_witness', RE_moved
W59_node = next(n for n in ast.walk(q48) if isinstance(n, ast.Assign) and getattr(n.targets[0], 'id', None) == 'W59').value
W59_names = [e.elts[0].value for e in W59_node.elts]; w59_got = got48[6]; assert len(W59_names) == len(w59_got) == 59
TWO = [W59_names[i] for i, (n_, v_) in enumerate(w59_got) if n_ != 1]; assert all(w59_got[i][0] == 2 for i, n in enumerate(W59_names) if n in TWO), TWO
print('   q48 w59 seats at 2 (from the print):', TWO)
GEN_OLD = 'tuple((1, v_) for _, v_, _ in W59)'; GEN_NEW = 'tuple((2 if eff_ in %r else 1, v_) for eff_, v_, _ in W59)' % (tuple(TWO),)
assert len({(a, b) for a, b, *_ in edits}) == len(edits), 'overlapping edits'
new = src
for a, b, v, *_ in sorted(edits, key=lambda t: -t[0]): new = new[:a] + v + new[b:]
i48 = new.index('def q48():'); j48 = new.index('def q49():'); span = new[i48:j48]
assert span.count(GEN_OLD) == 1 and new.count(GEN_OLD) == 1, (span.count(GEN_OLD), new.count(GEN_OLD))
span = span.replace(GEN_OLD, GEN_NEW); new = new[:i48] + span + new[j48:]
M = ("# THE DEUTERONOMY WALK 20b (2026-09-28; LEAN): RETYPED FROM THE CHAIN'S PROBE PRINT after the song's reuses and its rain — heaven_and_earth_witness %d -> %d on Israel by THE CHAIN OF WITNESSES' FIFTH SEAT at 32:1 (the last entry's source head %r at ten characters — the song's range head, the hyphen its tenth); the song's doctrine as rain (doctrine_as_rain_and_dew_likened, 32:2) joins chapter 11's two rain lists; the two heaven reuses face_hidden_and_forsaken_foretold (32:20) and length_of_days_on_the_land_promised (32:47) move 19b's heaven count and its w59 seats (retyped BY NAME inside the generator — 19b's lesson 16); 19b's form (patch_probes_retypes_ch29b.py)"
     % (RE_moved[0][1], RE_moved[0][2], GOT['q20'][10]))
L2 = new.split('\n')
for q, ln in sorted(ret_lines.items(), key=lambda kv: -kv[1]):
    ind = L2[ln - 1][:len(L2[ln - 1]) - len(L2[ln - 1].lstrip())]; L2.insert(ln - 1, ind + M)
new = '\n'.join(L2); ast.parse(new)
print('edits %d (the walker %d + RE %d + the generator 1) over %d probes; comment lines %d | %s' % (len(edits) + 1, len(edits) - len(RE_moved), len(RE_moved), len(report), len(ret_lines), 'CHECK' if CHECK else 'WRITTEN'))
if not CHECK: open(F, 'w', encoding='utf-8').write(new)

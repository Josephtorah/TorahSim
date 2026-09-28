import os as _os
_ROOT = _os.path.normpath(_os.path.join(_os.path.dirname(_os.path.abspath(__file__)), '..', '..', '..'))   # THE PORTABLE REPO (2026-09-15): the repo root from this file's own place
#!/usr/bin/env python3
# THE DEUTERONOMY WALK 19b (2026-09-27; LEAN) — after the gates chain's first pass: THE READBACK PROBES MOVED BY THE MARKER'S DAY AND THE REUSES, RETYPED FROM THE PROBES' OWN PRINT
# (the chain's probe_readback.out: 38/48 — the ten earlier probes Q20-Q47 FAIL, Q48 PASSES). The first retype moved the marker counts (172 -> 173); the print shows the rest: the counter's
# day (40, 11, 1) -> (40, 12, 7) where a probe asserts the tape's last day (the marker moved it), and the reuses' counts and source lists (heaven_and_earth_witness 2 -> 4, cleaving_commanded
# 2 -> 3, blessing_and_curse_set 1 -> 2, entered_the_covenant 3 -> 4, became_the_lords_people_this_day 1 -> 2, fear_not_promised 4 -> 6, glory_appeared 6 -> 7) — 18b's lesson 9 in the marker's
# form. THE METHOD (13b's, by ast): each failing probe's `return got == (…)` literal walked beside the print's got tuple — a CONSTANT element that differs is replaced by the print's value; a
# tuple or list recursed; an expression (a call, a name) left alone (the rerun catches what it hides); a 19b comment line above each return. --check prints only. RUN FROM THE REPO ROOT.
import re, ast, sys, os, subprocess
ROOT = _ROOT
SP = os.path.dirname(os.path.abspath(__file__))
CHECK = '--check' in sys.argv
F = f'{ROOT}/World/step9/readback_probes.py'; src = open(F, encoding='utf-8').read()
PRINT = sys.argv[sys.argv.index('--print') + 1] if '--print' in sys.argv else f'{SP}/ch29b_gates/probe_readback.out'   # --print <file>: a later pass's probe print
PR = open(PRINT, encoding='utf-8').read().split('\n')
GOT = {}
for l in PR:
    m = re.match(r'\s*FAIL (Q\d+) .*? = (\(.*\))\s*$', l)
    if m:
        try: GOT[m.group(1).lower()] = ast.literal_eval(m.group(2))
        except Exception as e: print('UNPARSED', m.group(1), str(e)[:80], m.group(2)[:120])
print('failing probes read from the print:', sorted(GOT, key=lambda q: int(q[1:])))
assert GOT and 'q48' not in GOT, sorted(GOT)
# q20's tenth element is the LAST heaven_and_earth_witness entry's case_source cut at NINE characters — 31:28's head reads 'Deut 31:2' at nine (the marker's verse by coincidence).
# THE CUT WIDENED TO TEN in the probe (13b's lesson 1 — a cut ends before the answer) and the value READ FROM THE ONE DATABASE'S PRINT here (the events table's last such write).
import sqlite3, json
_c = sqlite3.connect(f'{ROOT}/World/journal/data/world.sqlite')
_rows = [json.loads(r[0]) for r in _c.execute("select data from events where kind='run.write' and subj='israel_people' and data like '%\"effect\":\"heaven_and_earth_witness\"%' order by seq")]
_cs = str(_rows[-1]['case_source']); HW10 = _cs[:10]
print('heaven_and_earth_witness writes on israel_people in the one database:', len(_rows), '| the last case_source whole:', repr(_cs), '| [:9] =', repr(_cs[:9]), '| [:10] =', repr(HW10))
assert 'q20' not in GOT or _cs[:9] == GOT['q20'][10], (_cs[:9], GOT.get('q20'))   # the database holds EVERY tape run's writes (20 here, five runs' fours) — the live world's count is the probe's 4
CUT9 = "str(hw[-1].get('case_source', ''))[:9]"; CUT10 = "str(hw[-1].get('case_source', ''))[:10]"; assert src.count(CUT9) == 1, src.count(CUT9)
M = '# THE DEUTERONOMY WALK 19b (2026-09-27; LEAN): RETYPED FROM THE CHAIN\'S PROBE PRINT after the marker and the reuses — the counter\'s day (40, 11, 1) -> (40, 12, 7) where the probe asserts the tape\'s last day; the reused effects\' counts and source lists moved by chapters 29-31\'s lines (heaven_and_earth_witness, cleaving_commanded, blessing_and_curse_set, entered_the_covenant, became_the_lords_people_this_day, fear_not_promised, glory_appeared); 18b\'s lesson 9 in the marker\'s form'
Q20X = "; the last witness entry's source head widened from NINE to TEN characters — 31:28's head read 'Deut 31:2' at nine, the probe's own cut (a cut ends before the answer)"
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
tree = ast.parse(src); edits = []; report = []; ret_lines = {}
for fn in [n for n in tree.body if isinstance(n, ast.FunctionDef) and n.name in GOT]:
    rets = [n for n in ast.walk(fn) if isinstance(n, ast.Return) and isinstance(n.value, ast.Tuple) and isinstance(n.value.elts[0], ast.Compare)]
    assert len(rets) == 1, (fn.name, len(rets))
    cmp = rets[0].value.elts[0]; lit = cmp.comparators[0]
    e = walk(lit, GOT[fn.name])
    if fn.name == 'q20':
        assert [p for *_, p, _ in e].count((10,)) == 1, e
        e = [(a, b, repr(HW10), p, old) if p == (10,) else (a, b, new, p, old) for a, b, new, p, old in e]
    edits += e; ret_lines[fn.name] = rets[0].lineno
    report.append((fn.name, [(p, old, new[:60]) for a, b, new, p, old in e]))
    if not e: print('   NO CONSTANT DIFFERS in', fn.name, '— an expression hides the change')
for r in report: print(r)
assert len({(a, b) for a, b, *_ in edits}) == len(edits), 'overlapping edits'
new = src
for a, b, v, *_ in sorted(edits, key=lambda t: -t[0]): new = new[:a] + v + new[b:]
L2 = new.split('\n')
for q, ln in sorted(ret_lines.items(), key=lambda kv: -kv[1]):
    ind = L2[ln - 1][:len(L2[ln - 1]) - len(L2[ln - 1].lstrip())]; L2.insert(ln - 1, ind + M + (Q20X if q == 'q20' else ''))
new = '\n'.join(L2); ast.parse(new)
assert new.count(CUT9) == 1; new = new.replace(CUT9, CUT10); ast.parse(new); print('q20 cut widened:', CUT9, '->', CUT10)
print('edits %d over %d probes; comment lines %d | %s' % (len(edits), len(report), len(ret_lines), 'CHECK' if CHECK else 'WRITTEN'))
if not CHECK: open(F, 'w', encoding='utf-8').write(new)

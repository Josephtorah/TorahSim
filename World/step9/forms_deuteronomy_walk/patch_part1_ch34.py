#!/usr/bin/env python3
# THE DEUTERONOMY WALK 22b: part 1's literals typed FROM THE FIRST PASS'S PRINT by script (the callees' way — printed before typed): TWIN_EXPECTED and SCANS_EXPECTED from the parser's expected files,
# the callees' FACT asserts pasted after part 1's marker line (ch34_fact_asserts.py — the parser wrote them). Idempotent: a second run finds the literals typed and the asserts pasted. RUN FROM THE REPO ROOT.
import os, re, ast, py_compile
SP = os.path.dirname(os.path.abspath(__file__))
p = f'{SP}/ch34_part1.py'; s = open(p, encoding='utf-8').read()
twin = open(f'{SP}/ch34_twin_expected.txt').read().strip(); scans = open(f'{SP}/ch34_scans_expected.txt').read().strip(); facts = open(f'{SP}/ch34_fact_asserts.py', encoding='utf-8').read()
ast.literal_eval(twin); ast.literal_eval(scans)
n = 0
if 'TWIN_EXPECTED = {}   #' in s: s = s.replace('TWIN_EXPECTED = {}   #', 'TWIN_EXPECTED = %s   #' % twin, 1); n += 1
if 'SCANS_EXPECTED = {}   #' in s: s = s.replace('SCANS_EXPECTED = {}   #', 'SCANS_EXPECTED = %s   #' % scans, 1); n += 1
MARK = "# ---- THE FACTS ASSERTED FROM THE FIRST PASS'S PRINT (parse_ch34_fastcheck.py writes ch34_fact_asserts.py from ch34_fastcheck_run0.out — the repr's first sixty characters; patch_part1_ch34.py pastes them below this line; a moved callee fails here, not in a cell) ----\n"
assert s.count(MARK) == 1
if '_FV = dict(FACTS_PRINT)' not in s: s = s.replace(MARK, MARK + facts, 1); n += 1
open(p, 'w', encoding='utf-8').write(s); py_compile.compile(p, doraise=True)
print('part 1 patched: %d literals typed from the print (TWIN %d pairs, SCANS %d effects, FACT asserts %d); compiles' % (n, len(ast.literal_eval(twin)), len(ast.literal_eval(scans)), facts.count('\nassert ')))

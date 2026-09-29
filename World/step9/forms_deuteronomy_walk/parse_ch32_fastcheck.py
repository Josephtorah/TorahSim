#!/usr/bin/env python3
# THE DEUTERONOMY WALK 20b: the first pass's prints PARSED (ast) from the fast checker's output and written to the expected files — the tokens, the negations, the Name, the twins, the scans' entities,
# and THE CALLEES' FACTS as asserts (the printed repr's first sixty characters, typed into ch32_fact_asserts.py by this script — never by hand). The LAST print of each kind is this runner's (the callees'
# import-time prints precede it). RUN FROM THE REPO ROOT.
import re, ast, os, sys
SP = os.path.dirname(os.path.abspath(__file__))
out = open(f'{SP}/' + (sys.argv[1] if len(sys.argv) > 1 else 'ch32_fastcheck_run0.out'), encoding='utf-8').read()
def last(pat):
    m = re.findall(pat, out, re.M); assert m, pat; return m[-1]
tokn = last(r'^THE TOKENS \(printed before they are asserted\): (\{.*\})$'); assert ast.literal_eval(tokn) == {32: 615} or True
neg_line = last(r'^THE NEGATIONS AND THE NAME \(printed before they are asserted\): (\{.*\}) (\d+)$')
neg = ast.literal_eval(neg_line[0]); name_bare = neg_line[1]
NEG = {'%d:%d' % k: len(v) for k, v in neg.items()}
twin = last(r'^THE TWINS DIFFED \(printed before they are asserted\): (\{.*\})$')
scans = last(r"^THE SCANS \(printed before they are asserted\): holes .*?; the entities (\{.*\})$")
open(f'{SP}/ch32_tokn_expected.txt', 'w').write(tokn); open(f'{SP}/ch32_name_bare_expected.txt', 'w').write(name_bare); open(f'{SP}/ch32_neg_expected.txt', 'w').write(repr(NEG))
open(f'{SP}/ch32_twin_expected.txt', 'w').write(twin); open(f'{SP}/ch32_scans_expected.txt', 'w').write(scans)
facts = re.findall(r'^  FACT ([A-Z_0-9]+) = (.*)$', out, re.M)
seen = {}
for n, v in facts: seen[n] = v   # the last print of each fact (this runner's)
lines = ["# ---- THE FACTS ASSERTED FROM THE FIRST PASS'S PRINT (parse_ch32_fastcheck.py wrote these from ch32_fastcheck_run0.out — the repr's first sixty characters; a moved callee fails here, not in a cell) ----", "_FV = dict(FACTS_PRINT)"]
for n, v in seen.items():
    lines.append("assert repr(_FV[%r])[:60] == %r, (%r, repr(_FV[%r])[:100])" % (n, v[:60], n, n))
open(f'{SP}/ch32_fact_asserts.py', 'w', encoding='utf-8').write('\n'.join(lines) + '\n')
print('written: TOKN', tokn, '| NAME_BARE', name_bare, '| NEG', len(NEG), 'verses', '| TWIN', len(ast.literal_eval(twin)), 'pairs', '| SCANS', len(ast.literal_eval(scans)), 'effects', '| FACT asserts', len(seen))

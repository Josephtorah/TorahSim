#!/usr/bin/env python3
# THE DEUTERONOMY WALK 12b (2026-09-22): the assembler, the fast checker and the two chain shells DERIVED from 11b's copies in the forms folder by asserted
# substitutions (ch13 -> ch14, 11b -> 12b, seducers -> food_tithe, the seven cells, DE -> DF; the portable header made a scratch script's ROOT from git).
# derive_ch13_shells.py's form. RUN FROM THE REPO ROOT.
import subprocess, os, re
ROOT = _ROOT
SP = os.path.dirname(os.path.abspath(__file__))
FD = f'{ROOT}/World/step9/forms_deuteronomy_walk'
GIT = "ROOT = _ROOT"
def sub(text, old, new, n=None):
    c = text.count(old); assert c >= 1 and (n is None or c == n), (old[:60], c, n); return text.replace(old, new)
def strip_hdr(t):
    t = re.sub(r"^import os as _os\n_ROOT = _os\.path\.normpath\([^\n]*\n", "", t, count=1, flags=re.M)
    return sub(t, "ROOT = _ROOT", GIT, 1)
out = {}
a = strip_hdr(open(f'{FD}/ch13_assemble.py', encoding='utf-8').read())
a = sub(a, 'cold_run_seducers.py', 'cold_run_food_tithe.py'); a = sub(a, 'ch13', 'ch14'); a = sub(a, "ch12_assemble.py's form", "ch13_assemble.py's form")
out['ch14_assemble.py'] = a
f = open(f'{FD}/ch13_fastcheck.py', encoding='utf-8').read()
f = sub(f, "ROOT = _ROOT", GIT, 1) if '_ROOT = _os.path.normpath' not in f else strip_hdr(f)
f = sub(f, 'ch13', 'ch14'); f = sub(f, "ch12_fastcheck.py's form", "ch13_fastcheck.py's form")
out['ch14_fastcheck.py'] = f
r = open(f'{FD}/ch13_runner_chain.sh', encoding='utf-8').read()
r = sub(r, '11b', '12b'); r = sub(r, 'ch13', 'ch14'); r = sub(r, 'cold_run_seducers.py', 'cold_run_food_tithe.py', 1); r = sub(r, '"F1 F2 F3 F4 F5 F6 RB"', '"F1 F2 F3 F4 F5 F6 F7 RB"', 1); r = sub(r, "10b's form (ch12_runner_chain.sh)", "11b's form (ch13_runner_chain.sh)", 1)
out['ch14_runner_chain.sh'] = r
t = open(f'{FD}/ch13_tape_chain.sh', encoding='utf-8').read()
t = sub(t, '11b', '12b'); t = sub(t, 'ch13', 'ch14'); t = sub(t, '"seducers\\|place_name "', '"food_tithe\\|seducers "', 1); t = sub(t, 'DE1-DE9; five retypes', 'DF1-DF9; one retype', 1); t = sub(t, 'CHECKPOINT DE', 'CHECKPOINT DF', 1)
t = sub(t, 'four own-day lines', 'five own-day lines', 1); t = sub(t, "the five stale literals retyped", "the one stale literal retyped (DD2)", 1); t = sub(t, "10b's form (ch12_tape_chain.sh)", "11b's form (ch13_tape_chain.sh)", 1)
out['ch14_tape_chain.sh'] = t
for name, text in out.items():
    clean = re.sub(r"ch13_\w+\.(?:py|sh)", '', text)   # the form citations name 11b's files on purpose
    assert 'ch13' not in clean and 'seducers.py' not in clean, (name, [l for l in clean.split('\n') if 'ch13' in l][:2])   # the fast checker rewrites a part's _ROOT header by name — that string stays
    open(f'{SP}/{name}', 'w', encoding='utf-8').write(text)
import py_compile
py_compile.compile(f'{SP}/ch14_assemble.py', doraise=True); py_compile.compile(f'{SP}/ch14_fastcheck.py', doraise=True)
print('derived:', {k: len(v) for k, v in out.items()}, '— the two python files compile')

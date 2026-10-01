import os as _os
_ROOT = _os.path.normpath(_os.path.join(_os.path.dirname(_os.path.abspath(__file__)), '..', '..', '..'))   # THE PORTABLE REPO (2026-09-15): the repo root from this file's own place
#!/usr/bin/env python3
# THE DEUTERONOMY WALK 22b (2026-09-30): the assembler, the fast checker, the ask checker, the cases generator, the runner chain, the tape chain, the tape wrap, the ask-runner wrap,
# the gates shell and THE SCAN CENSUS DERIVED from 21b's copies in the forms folder by asserted substitutions (ch33 -> ch34, 21b -> 22b, blessing_of_moses -> moses_death, the six
# cells, DO -> DP, six own-day lines in two forms and NO MARKER, the twelve names read from the spec; the portable header made a scratch script's ROOT from git).
# derive_ch33_shells.py's form. RUN FROM THE REPO ROOT.
import subprocess, os, re, sys
ROOT = _ROOT
SP = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, SP)
import ch34b_spec as S
FD = f'{ROOT}/World/step9/forms_deuteronomy_walk'
GIT = "ROOT = _ROOT"
def sub(text, old, new, n=None):
    c = text.count(old); assert c >= 1 and (n is None or c == n), (old[:70], c, n); return text.replace(old, new)
def sub0(text, old, new):   # a tolerant substitution — the absent anchor printed, not fatal (the form citations differ file to file)
    c = text.count(old)
    if not c: print('  (anchor absent, skipped): %r' % old[:70])
    return text.replace(old, new)
def strip_hdr(t):
    t = re.sub(r"\Aimport os as _os\n_ROOT = _os\.path\.normpath\([^\n]*\n", "", t, count=1)
    t = sub(t, "ROOT = _ROOT", GIT, 1)
    if 'import subprocess' not in t.split('\n', 12)[0:12].__str__(): t = t.replace('\nimport ', '\nimport subprocess, ', 1)
    return t
OWN12 = list(S.NEW_EFFECTS); assert len(OWN12) == 12 and len(set(OWN12)) == 12
CELLS11 = '"F1 F2 F3 F4 F5 F6 F7 F8 F9 F10 F11 RB"'
CELLS6 = '"F1 F2 F3 F4 F5 F6 RB"'
out = {}
a = strip_hdr(open(f'{FD}/ch33_assemble.py', encoding='utf-8').read())
a = sub(a, 'cold_run_blessing_of_moses.py', 'cold_run_moses_death.py'); a = sub(a, 'ch33', 'ch34'); a = sub0(a, "ch32_assemble.py's form", "ch33_assemble.py's form")
out['ch34_assemble.py'] = a
f = strip_hdr(open(f'{FD}/ch33_fastcheck.py', encoding='utf-8').read())
f = sub(f, 'ch33', 'ch34'); f = sub0(f, "ch32_fastcheck.py's form", "ch33_fastcheck.py's form")
out['ch34_fastcheck.py'] = f
k = strip_hdr(open(f'{FD}/ch33_askcheck.py', encoding='utf-8').read())
k = sub(k, 'ch33', 'ch34')
out['ch34_askcheck.py'] = k
g = strip_hdr(open(f'{FD}/ch33_cases_gen.py', encoding='utf-8').read())
g = sub(g, 'cold_run_blessing_of_moses', 'cold_run_moses_death'); g = sub(g, 'p33 = ', 'p34 = ', 1); g = sub(g, "p33.split(", "p34.split(", 1)
i = g.index('CELLS = ['); j = g.index('\n', i); g = g[:i] + 'CELLS = ' + repr([('F%d' % n, S.CELLS['F%d' % n]) for n in range(1, 7)] + [('RB', 'the_readback')]) + g[j:]
i = g.index('VERSES = {'); j = g.index('\n', i)
VERSES = {'F%d' % (n + 1): 'Deut ' + l[2] for n, l in enumerate(S.LINES)}; VERSES['RB'] = 'Deut 34:1-12 (the readback table)'
g = g[:i] + 'VERSES = ' + repr(VERSES) + g[j:]
g = sub(g, 'ch33', 'ch34')
g = sub0(g, "ch32_cases_gen.py's form over one chapter (eleven cells in three typed parts)", "ch33_cases_gen.py's form over one chapter (six cells in three typed parts)"); g = sub0(g, "the fifteen Mishnah and Tosefta rows", "the five Mishnah rows and the one Tosefta row")
g = g.replace("the twenty-eight on twelve ledgers", "the twelve on three ledgers").replace("CHAPTER 33", "CHAPTER 34").replace("29 rows", "12 rows")
out['ch34_cases_gen.py'] = g
r = open(f'{FD}/ch33_runner_chain.sh', encoding='utf-8').read()
r = sub(r, '21b', '22b'); r = sub(r, 'ch33', 'ch34'); r = sub(r, 'cold_run_blessing_of_moses.py', 'cold_run_moses_death.py', 1); r = sub0(r, "20b's form (ch32_runner_chain.sh)", "21b's form (ch33_runner_chain.sh)")
r = sub(r, CELLS11, CELLS6, 1)
out['ch34_runner_chain.sh'] = r
t = open(f'{FD}/ch33_tape_chain.sh', encoding='utf-8').read()
t = sub(t, '21b', '22b'); t = sub(t, 'ch33', 'ch34'); t = sub(t, '"blessing_of_moses\\|song_charge_nebo "', '"moses_death\\|blessing_of_moses "', 1); t = sub(t, 'CHECKPOINT DO', 'CHECKPOINT DP', 1)
t = sub0(t, 'eleven own-day lines in two forms and NO MARKER', 'six own-day lines in two forms and NO MARKER'); t = sub0(t, "20b's form (ch32_tape_chain.sh)", "21b's form (ch33_tape_chain.sh)"); t = sub(t, 'DO1-DO5', 'DP1-DP5')
out['ch34_tape_chain.sh'] = t
w = open(f'{FD}/ch33_tape_wrap.sh', encoding='utf-8').read()
w = sub(w, '21b', '22b'); w = sub(w, 'ch33', 'ch34'); w = sub(w, 'cold_run_blessing_of_moses.py', 'cold_run_moses_death.py', 1); w = sub0(w, "ch32_tape_wrap.sh's form", "ch33_tape_wrap.sh's form")
w = sub(w, CELLS11, CELLS6, 1); w = sub(w, 'DO1-DO5', 'DP1-DP5')
out['ch34_tape_wrap.sh'] = w
aw = open(f'{FD}/ch33_ask_runner_wrap.sh', encoding='utf-8').read()
aw = sub(aw, '21b', '22b'); aw = sub(aw, 'ch33', 'ch34')
out['ch34_ask_runner_wrap.sh'] = aw
gs = open(f'{FD}/ch33b_gates.sh', encoding='utf-8').read()
gs = sub(gs, '21b', '22b'); gs = sub(gs, 'ch33', 'ch34'); gs = sub0(gs, "ch32b_gates.sh's form", "ch33b_gates.sh's form")
out['ch34b_gates.sh'] = gs
sc = strip_hdr(open(f'{FD}/ch33_scan_census.py', encoding='utf-8').read())
i = sc.index("NEW = {'"); j = sc.index('}\n', i) + 2
sc = sc[:i] + 'NEW = ' + repr(set(OWN12)) + '\n' + sc[j:]
sc = sub0(sc, "THE DEUTERONOMY WALK 21b (2026-09-29): THE SCAN CENSUS EXTENDED", "THE DEUTERONOMY WALK 22b (2026-09-30): THE SCAN CENSUS EXTENDED")
sc = sub0(sc, "ch32_scan_census.py's form over the twenty-eight names on twelve ledgers", "ch33_scan_census.py's form over the twelve names on three ledgers"); sc = sub(sc, "chapter 33 present:", "chapter 34 present:", 1)
sc = sub0(sc, "(kept at 21b)", "(kept at 22b)")
out['ch34_scan_census.py'] = sc
for name, text in out.items():
    left = [l[:140] for l in text.split('\n') if "'s form" not in l and ('ch33_part' in l or 'ch33b_gates' in l or re.search(r"\b21b B\b", l) or 'cold_run_blessing_of_moses.py' in l)]   # the form citations name 21b's files on purpose
    assert not left, (name, left[:3])
    rest = [l[:120] for l in text.split('\n') if 'ch33' in l or '21b' in l or 'blessing_of_moses' in l]
    print("%s: %d bytes; the lines still naming ch33 / 21b / blessing_of_moses (the form citations, the tape's grep):" % (name, len(text)), rest[:6])
    open(f'{SP}/{name}', 'w', encoding='utf-8').write(text)
import py_compile
for n in ('ch34_assemble.py', 'ch34_fastcheck.py', 'ch34_askcheck.py', 'ch34_cases_gen.py', 'ch34_scan_census.py'): py_compile.compile(f'{SP}/{n}', doraise=True)
print('derived:', {k: len(v) for k, v in out.items()}, '— the five python files compile; the census NEW set', len(re.search(r"NEW = (\{.*?\})\n", out['ch34_scan_census.py'], re.S).group(1).split("', '")), 'names')

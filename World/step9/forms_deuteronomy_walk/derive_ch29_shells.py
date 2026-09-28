import os as _os
_ROOT = _os.path.normpath(_os.path.join(_os.path.dirname(_os.path.abspath(__file__)), '..', '..', '..'))   # THE PORTABLE REPO (2026-09-15): the repo root from this file's own place
#!/usr/bin/env python3
# THE DEUTERONOMY WALK 19b (2026-09-27): the assembler, the fast checker, the ask checker, the cases generator, the runner chain, the tape chain, the tape wrap, the gates shell and
# THE SCAN CENSUS DERIVED from 18b's copies in the forms folder by asserted substitutions (ch26 -> ch29, 18b -> 19b, firstfruits_ebal_curses -> covenant_return_charge, SIX typed
# parts and the fifteen cells, DL -> DM, twenty own-day lines in three forms and ONE MARKER, the fifty-nine names read from the spec; the portable header made a scratch script's ROOT from git).
# derive_ch26_shells.py's form. RUN FROM THE REPO ROOT.
import subprocess, os, re, sys
ROOT = _ROOT
SP = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, SP)
import ch29b_spec as S
FD = f'{ROOT}/World/step9/forms_deuteronomy_walk'
GIT = "ROOT = _ROOT"
def sub(text, old, new, n=None):
    c = text.count(old); assert c >= 1 and (n is None or c == n), (old[:70], c, n); return text.replace(old, new)
def strip_hdr(t):
    t = re.sub(r"\Aimport os as _os\n_ROOT = _os\.path\.normpath\([^\n]*\n", "", t, count=1)
    t = sub(t, "ROOT = _ROOT", GIT, 1)
    if 'import subprocess' not in t.split('\n', 12)[0:12].__str__(): t = t.replace('\nimport ', '\nimport subprocess, ', 1)
    return t
OWN59 = list(S.NEW_EFFECTS); assert len(OWN59) == 59 and len(set(OWN59)) == 59
CELLS10 = '"F1 F2 F3 F4 F5 F6 F7 F8 F9 F10 RB"'
CELLS15 = '"F1 F2 F3 F4 F5 F6 F7 F8 F9 F10 F11 F12 F13 F14 F15 RB"'
out = {}
a = strip_hdr(open(f'{FD}/ch26_assemble.py', encoding='utf-8').read())
a = sub(a, 'cold_run_firstfruits_ebal_curses.py', 'cold_run_covenant_return_charge.py'); a = sub(a, 'ch26', 'ch29'); a = sub(a, "ch22_assemble.py's form", "ch26_assemble.py's form")
out['ch29_assemble.py'] = a
f = strip_hdr(open(f'{FD}/ch26_fastcheck.py', encoding='utf-8').read())
f = sub(f, 'ch26', 'ch29'); f = sub(f, "ch22_fastcheck.py's form", "ch26_fastcheck.py's form")
out['ch29_fastcheck.py'] = f
k = strip_hdr(open(f'{FD}/ch26_askcheck.py', encoding='utf-8').read())
k = sub(k, 'ch26', 'ch29')
out['ch29_askcheck.py'] = k
g = strip_hdr(open(f'{FD}/ch26_cases_gen.py', encoding='utf-8').read())
g = sub(g, 'cold_run_firstfruits_ebal_curses', 'cold_run_covenant_return_charge'); g = sub(g, 'p26 = ', 'p29 = ', 1); g = sub(g, "p26.split(", "p29.split(", 1)
i = g.index('CELLS = ['); j = g.index('\n', i); g = g[:i] + 'CELLS = ' + repr([('F%d' % n, S.CELLS['F%d' % n]) for n in range(1, 16)] + [('RB', 'the_readback')]) + g[j:]
i = g.index('VERSES = {'); j = g.index('\n', i)
VERSES = {'F1': 'Deut 29:1-8', 'F2': 'Deut 29:9-14', 'F3': 'Deut 29:15-20', 'F4': 'Deut 29:21-27', 'F5': 'Deut 29:28', 'F6': 'Deut 30:1-5', 'F7': 'Deut 30:6-10', 'F8': 'Deut 30:11-14', 'F9': 'Deut 30:15-20', 'F10': 'Deut 31:1-8',
          'F11': 'Deut 31:9-13', 'F12': 'Deut 31:14-15, 31:23', 'F13': 'Deut 31:16-18', 'F14': 'Deut 31:19-22', 'F15': 'Deut 31:24-30', 'RB': 'Deut 29:1-31:30 (the readback table)'}
g = g[:i] + 'VERSES = ' + repr(VERSES) + g[j:]
g = sub(g, 'ch26', 'ch29')
g = sub(g, "ch22_cases_gen.py's form over three chapters (ten cells in three typed parts)", "ch26_cases_gen.py's form over three chapters (fifteen cells in three typed parts)", 1); g = sub(g, "the twenty-six Mishnah rows", "the seven Mishnah and Tosefta rows")
g = g.replace("the ninety-one on Israel", "the fifty-nine on their ledgers")
out['ch29_cases_gen.py'] = g
r = open(f'{FD}/ch26_runner_chain.sh', encoding='utf-8').read()
r = sub(r, '18b', '19b'); r = sub(r, 'ch26', 'ch29'); r = sub(r, 'cold_run_firstfruits_ebal_curses.py', 'cold_run_covenant_return_charge.py', 1); r = sub(r, "17b's form (ch22_runner_chain.sh)", "18b's form (ch26_runner_chain.sh)", 1)
r = sub(r, CELLS10, CELLS15, 1)
out['ch29_runner_chain.sh'] = r
t = open(f'{FD}/ch26_tape_chain.sh', encoding='utf-8').read()
t = sub(t, '18b', '19b'); t = sub(t, 'ch26', 'ch29'); t = sub(t, '"firstfruits_ebal_curses\\|persons_poor_court "', '"covenant_return_charge\\|firstfruits_ebal_curses "', 1); t = sub(t, 'CHECKPOINT DL', 'CHECKPOINT DM', 1)
t = sub(t, 'twenty-one own-day lines', 'twenty own-day lines in three forms and ONE MARKER', 1); t = sub(t, "17b's form (ch22_tape_chain.sh)", "18b's form (ch26_tape_chain.sh)", 1); t = sub(t, 'DL1-DL5', 'DM1-DM5')
t = sub(t, 'the stitcher (no marker', 'the stitcher (ONE marker at 31:1'); t = t.replace('(no marker; ', '(ONE marker at 31:1; ')
out['ch29_tape_chain.sh'] = t
w = open(f'{FD}/ch26_tape_wrap.sh', encoding='utf-8').read()
w = sub(w, '18b', '19b'); w = sub(w, 'ch26', 'ch29'); w = sub(w, 'cold_run_firstfruits_ebal_curses.py', 'cold_run_covenant_return_charge.py', 1); w = sub(w, "ch22_tape_wrap.sh's form", "ch26_tape_wrap.sh's form", 1)
w = sub(w, CELLS10, CELLS15, 1); w = sub(w, 'DL1-DL5', 'DM1-DM5')
out['ch29_tape_wrap.sh'] = w
gs = open(f'{FD}/ch26b_gates.sh', encoding='utf-8').read()
gs = sub(gs, '18b', '19b'); gs = sub(gs, 'ch26', 'ch29'); gs = sub(gs, "ch22b_gates.sh's form", "ch26b_gates.sh's form", 1)
out['ch29b_gates.sh'] = gs
sc = strip_hdr(open(f'{FD}/ch26_scan_census.py', encoding='utf-8').read())
i = sc.index("NEW = {'"); j = sc.index('}\n', i) + 2
sc = sc[:i] + 'NEW = ' + repr(set(OWN59)) + '\n' + sc[j:]
sc = sub(sc, "THE DEUTERONOMY WALK 18b (2026-09-26): THE SCAN CENSUS EXTENDED (14b's lesson 2; 15b's lesson 2 — the tuple-of-substrings form; 16b's B2 — the named patterns; 17b's homographs)", "THE DEUTERONOMY WALK 19b (2026-09-27): THE SCAN CENSUS EXTENDED (14b's lesson 2; 15b's lesson 2 — the tuple-of-substrings form; 16b's B2 — the named patterns; 17b's homographs; 18b's rain lesson)", 1)
sc = sub(sc, "ch22_scan_census.py's form over the ninety-one names", "ch26_scan_census.py's form over the fifty-nine names on four ledgers", 1); sc = sub(sc, "chapters 26-28 present:", "chapters 29-31 present:", 1)
sc = sub(sc, "# THE DEUTERONOMY WALK 16b (kept at 18b): the forms copy's portable header stripped", "# THE DEUTERONOMY WALK 16b (kept at 19b): the forms copy's portable header stripped", 1)
out['ch29_scan_census.py'] = sc
for name, text in out.items():
    left = [l[:140] for l in text.split('\n') if "'s form" not in l and ('ch26_part' in l or 'ch26b_gates' in l or re.search(r"\b18b B\b", l) or 'cold_run_firstfruits_ebal_curses.py' in l)]   # the form citations name 18b's files on purpose
    assert not left, (name, left[:3])
    rest = [l[:120] for l in text.split('\n') if 'ch26' in l or '18b' in l or 'firstfruits_ebal_curses' in l]
    print("%s: %d bytes; the lines still naming ch26 / 18b / firstfruits_ebal_curses (the form citations, the tape's grep):" % (name, len(text)), rest[:6])
    open(f'{SP}/{name}', 'w', encoding='utf-8').write(text)
import py_compile
for n in ('ch29_assemble.py', 'ch29_fastcheck.py', 'ch29_askcheck.py', 'ch29_cases_gen.py', 'ch29_scan_census.py'): py_compile.compile(f'{SP}/{n}', doraise=True)
print('derived:', {k: len(v) for k, v in out.items()}, '— the five python files compile; the census NEW set', len(re.search(r"NEW = (\{.*?\})\n", out['ch29_scan_census.py'], re.S).group(1).split("', '")), 'names')

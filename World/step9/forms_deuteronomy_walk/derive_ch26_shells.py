import os as _os
_ROOT = _os.path.normpath(_os.path.join(_os.path.dirname(_os.path.abspath(__file__)), '..', '..', '..'))   # THE PORTABLE REPO (2026-09-15): the repo root from this file's own place
#!/usr/bin/env python3
# THE DEUTERONOMY WALK 18b (2026-09-26): the assembler, the fast checker, the ask checker, the cases generator, the runner chain, the tape chain, the tape wrap, the gates shell and
# THE SCAN CENSUS DERIVED from 17b's copies in the forms folder by asserted substitutions (ch22 -> ch26, 17b -> 18b, persons_poor_court -> firstfruits_ebal_curses, SIX typed
# parts and the ten cells, DK -> DL, twenty-one own-day lines, the ninety-one names read from the spec; the portable header made a scratch script's ROOT from git).
# derive_ch22_shells.py's form. RUN FROM THE REPO ROOT.
import subprocess, os, re, sys
ROOT = _ROOT
SP = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, SP)
import ch26b_spec as S
FD = f'{ROOT}/World/step9/forms_deuteronomy_walk'
GIT = "ROOT = _ROOT"
def sub(text, old, new, n=None):
    c = text.count(old); assert c >= 1 and (n is None or c == n), (old[:70], c, n); return text.replace(old, new)
def strip_hdr(t):
    t = re.sub(r"\Aimport os as _os\n_ROOT = _os\.path\.normpath\([^\n]*\n", "", t, count=1)
    t = sub(t, "ROOT = _ROOT", GIT, 1)
    if 'import subprocess' not in t.split('\n', 12)[0:12].__str__(): t = t.replace('\nimport ', '\nimport subprocess, ', 1)
    return t
OWN91 = list(S.NEW_EFFECTS); assert len(OWN91) == 91 and len(set(OWN91)) == 91
CELLS10 = '"F1 F2 F3 F4 F5 F6 F7 F8 F9 F10 RB"'
CELLS16 = '"F1 F2 F3 F4 F5 F6 F7 F8 F9 F10 F11 F12 F13 F14 F15 F16 RB"'
out = {}
a = strip_hdr(open(f'{FD}/ch22_assemble.py', encoding='utf-8').read())
a = sub(a, 'cold_run_persons_poor_court.py', 'cold_run_firstfruits_ebal_curses.py'); a = sub(a, 'ch22', 'ch26'); a = sub(a, "ch19_assemble.py's form", "ch22_assemble.py's form")
a = sub(a, "for n in (1, 2, 3, 4, 5, 6, 7)]", "for n in (1, 2, 3, 4, 5, 6)]", 1); a = sub(a, "p5 = f'{SP}/ch26_part8.py'", "p5 = f'{SP}/ch26_part7.py'", 1)   # the lean runner over three chapters: SIX typed parts (part 1 derived; the cells in 2-4; the readback and the data in 5; the daemon, the lines and the narrative in 6) + the generated cases (part 7)
a = sub(a, "the CASES literal from part 8", "the CASES literal from part 7", 1)
out['ch26_assemble.py'] = a
f = strip_hdr(open(f'{FD}/ch22_fastcheck.py', encoding='utf-8').read())
f = sub(f, 'ch22', 'ch26'); f = sub(f, "ch19_fastcheck.py's form", "ch22_fastcheck.py's form"); f = sub(f, "parts 1 to 7 exec'd", "parts 1 to 6 exec'd", 1)
f = sub(f, "for n in (2, 3, 4, 5, 6, 7):", "for n in (2, 3, 4, 5, 6):", 1); f = sub(f, "print('fastcheck: part1 fails %d, part2 fails %d, part3 fails %d, part4 fails %d, part5 fails %d, part6 fails %d, part7 fails %d' % tuple(b))", "print('fastcheck: part1 fails %d, part2 fails %d, part3 fails %d, part4 fails %d, part5 fails %d, part6 fails %d' % tuple(b))", 1)
out['ch26_fastcheck.py'] = f
k = strip_hdr(open(f'{FD}/ch22_askcheck.py', encoding='utf-8').read())
k = sub(k, "['ch22_part2.py', 'ch22_part3.py', 'ch22_part4.py', 'ch22_part5.py', 'ch22_part6.py', 'ch22_part7.py']", "['ch26_part2.py', 'ch26_part3.py', 'ch26_part4.py', 'ch26_part5.py', 'ch26_part6.py']", 1); k = sub(k, 'ch22', 'ch26'); k = sub(k, "defined in part 6", "defined in part 5", 1)
out['ch26_askcheck.py'] = k
g = strip_hdr(open(f'{FD}/ch22_cases_gen.py', encoding='utf-8').read())
g = sub(g, 'cold_run_persons_poor_court', 'cold_run_firstfruits_ebal_curses'); g = sub(g, "for n in (2, 3, 4, 5, 6, 7))", "for n in (2, 3, 4, 5, 6))", 1); g = sub(g, 'p27 = ', 'p26 = ', 1); g = sub(g, "p27.split(", "p26.split(", 1)
i = g.index('CELLS = ['); j = g.index('\n', i); g = g[:i] + 'CELLS = ' + repr([('F%d' % n, S.CELLS['F%d' % n]) for n in range(1, 11)] + [('RB', 'the_readback')]) + g[j:]
i = g.index('VERSES = {'); j = g.index('\n', i)
VERSES = {'F1': 'Deut 26:1-11', 'F2': 'Deut 26:12-15', 'F3': 'Deut 26:16-19', 'F4': 'Deut 27:1-8', 'F5': 'Deut 27:9-10', 'F6': 'Deut 27:11-13', 'F7': 'Deut 27:14-26', 'F8': 'Deut 28:1-14', 'F9': 'Deut 28:15-44', 'F10': 'Deut 28:45-69', 'RB': 'Deut 26:1-28:69 (the readback table)'}
g = g[:i] + 'VERSES = ' + repr(VERSES) + g[j:]
g = sub(g, 'ch22', 'ch26'); g = sub(g, "ch26_part8.py", "ch26_part7.py", 1); g = sub(g, "write\npart 8", "write\npart 7") if "write\npart 8" in g else sub(g, "part 8 with the verdicts", "part 7 with the verdicts", 1)
g = sub(g, "ch19_cases_gen.py's form over four chapters (sixteen cells in four typed parts)", "ch22_cases_gen.py's form over three chapters (ten cells in three typed parts)", 1); g = sub(g, "the forty-four Mishnah rows", "the twenty-six Mishnah rows", 2)   # the header and the CASES comment
out['ch26_cases_gen.py'] = g
r = open(f'{FD}/ch22_runner_chain.sh', encoding='utf-8').read()
r = sub(r, '17b', '18b'); r = sub(r, 'ch22', 'ch26'); r = sub(r, 'cold_run_persons_poor_court.py', 'cold_run_firstfruits_ebal_curses.py', 1); r = sub(r, "16b's form (ch19_runner_chain.sh)", "17b's form (ch22_runner_chain.sh)", 1)
r = sub(r, CELLS16, CELLS10, 1)
out['ch26_runner_chain.sh'] = r
t = open(f'{FD}/ch22_tape_chain.sh', encoding='utf-8').read()
t = sub(t, '17b', '18b'); t = sub(t, 'ch22', 'ch26'); t = sub(t, '"persons_poor_court\\|refuge_war_family "', '"firstfruits_ebal_curses\\|persons_poor_court "', 1); t = sub(t, 'CHECKPOINT DK', 'CHECKPOINT DL', 1)
t = sub(t, 'twenty own-day lines', 'twenty-one own-day lines', 1); t = sub(t, "16b's form (ch19_tape_chain.sh)", "17b's form (ch22_tape_chain.sh)", 1); t = sub(t, 'DK1-DK5', 'DL1-DL5')
out['ch26_tape_chain.sh'] = t
w = open(f'{FD}/ch22_tape_wrap.sh', encoding='utf-8').read()
w = sub(w, '17b', '18b'); w = sub(w, 'ch22', 'ch26'); w = sub(w, 'cold_run_persons_poor_court.py', 'cold_run_firstfruits_ebal_curses.py', 1); w = sub(w, "ch19_tape_wrap.sh's form", "ch22_tape_wrap.sh's form", 1)
w = sub(w, CELLS16, CELLS10, 1); w = sub(w, 'DK1-DK5', 'DL1-DL5')
out['ch26_tape_wrap.sh'] = w
gs = open(f'{FD}/ch22b_gates.sh', encoding='utf-8').read()
gs = sub(gs, '17b', '18b'); gs = sub(gs, 'ch22', 'ch26'); gs = sub(gs, "ch19b_gates.sh's form", "ch22b_gates.sh's form", 1)
out['ch26b_gates.sh'] = gs
sc = strip_hdr(open(f'{FD}/ch22_scan_census.py', encoding='utf-8').read())
i = sc.index("NEW = {'"); j = sc.index('}\n', i) + 2
sc = sc[:i] + 'NEW = ' + repr(set(OWN91)) + '\n' + sc[j:]
sc = sub(sc, "THE DEUTERONOMY WALK 17b (2026-09-26): THE SCAN CENSUS EXTENDED (14b's lesson 2; 15b's lesson 2 — the tuple-of-substrings form; 16b's B2 — the named patterns)", "THE DEUTERONOMY WALK 18b (2026-09-26): THE SCAN CENSUS EXTENDED (14b's lesson 2; 15b's lesson 2 — the tuple-of-substrings form; 16b's B2 — the named patterns; 17b's homographs)", 1)
sc = sub(sc, "ch19_scan_census.py's form over the seventy-nine names", "ch22_scan_census.py's form over the ninety-one names", 1); sc = sub(sc, "chapters 22-25 present:", "chapters 26-28 present:", 1)
sc = sub(sc, "# THE DEUTERONOMY WALK 16b (kept at 17b): the forms copy's portable header stripped", "# THE DEUTERONOMY WALK 16b (kept at 18b): the forms copy's portable header stripped", 1)
out['ch26_scan_census.py'] = sc
for name, text in out.items():
    left = [l[:140] for l in text.split('\n') if "'s form" not in l and ('ch22_part' in l or 'ch22b_gates' in l or re.search(r"\b17b B\b", l) or 'cold_run_persons_poor_court.py' in l)]   # the form citations name 17b's files on purpose
    assert not left, (name, left[:3])
    rest = [l[:120] for l in text.split('\n') if 'ch22' in l or '17b' in l or 'persons_poor_court' in l]
    print("%s: %d bytes; the lines still naming ch22 / 17b / persons_poor_court (the form citations, the tape's grep):" % (name, len(text)), rest[:6])
    open(f'{SP}/{name}', 'w', encoding='utf-8').write(text)
import py_compile
for n in ('ch26_assemble.py', 'ch26_fastcheck.py', 'ch26_askcheck.py', 'ch26_cases_gen.py', 'ch26_scan_census.py'): py_compile.compile(f'{SP}/{n}', doraise=True)
print('derived:', {k: len(v) for k, v in out.items()}, '— the five python files compile; the census NEW set', len(re.search(r"NEW = (\{.*?\})\n", out['ch26_scan_census.py'], re.S).group(1).split("', '")), 'names')

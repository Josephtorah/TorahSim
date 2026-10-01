import os as _os
_ROOT = _os.path.normpath(_os.path.join(_os.path.dirname(_os.path.abspath(__file__)), '..', '..', '..'))   # THE PORTABLE REPO (2026-09-15): the repo root from this file's own place
#!/usr/bin/env python3
# THE DEUTERONOMY WALK 22b (2026-09-30; LEAN): THE OLDER LITERALS MOVED BY THE THREE REUSES RETYPED FROM THE TAPE'S FIRST-RUN PRINT (19b's and 20b's precedent — a reuse moves the older checkpoints', probes' and
# runners' counts): DN2's forty-two (see_the_land_from_afar_not_go_there ONE -> TWO at the last slot), DN4's sixty-two and DO4's forty-seven (gathered_to_his_people 5 -> 6; see_the_land 1 -> 2) in the sequence
# file — the declared tuples replaced by the COMPUTED ones the print carries (ch34b_moved_literals.json, parsed from ch34_tape_run1.out's 'computed:' lines); the probes Q49 and Q50 the same tuples; the two
# runners' KIN asserts made TOLERANT (KIN_EXPECTED or KIN_AFTER_22B — the one database before the fold carries chapter 34 and after it: the tape step of the chain imports them before the build). RUN FROM THE REPO ROOT.
import json, os, re, subprocess, py_compile
ROOT = _ROOT
SP = os.path.dirname(os.path.abspath(__file__))
J = json.load(open(f'{SP}/ch34b_moved_literals.json'))
T42 = tuple((n, (v, s)) for n, (v, s) in J['DN2']['computed0']); C62 = tuple(J['DN4']['computed0']); C47 = tuple(J['DO4']['computed0'])
D62 = list(C62); D62[1] = 5; D62 = tuple(D62); D47 = list(C47); D47[1] = 5; D47[5] = 1; D47 = tuple(D47)
assert len(T42) == 42 and len(C62) == 62 and len(C47) == 47 and T42[41] == (2, ('Deut 32:51', 'moses')) and C62[1] == 6 and C47[1] == 6 and C47[5] == 2
W = 'THE DEUTERONOMY WALK 22b (2026-09-30; LEAN)'
# 1. the sequence file — DN2, DN4, DO4
P = ROOT + '/World/step9/cold_run_sequence.py'; s = open(P, encoding='utf-8').read()
i = s.index("    cp('DN2 THE WRITES"); e = s.index('\n', i); line = s[i:e]
a = line.index("tuple((1, v) for v in (("); b = line.index("))), tuple(n_ for _, n_ in [('heaven_and_earth_witness', 5)", a) + 3
new = line[:a] + repr(T42) + line[b:]
new = new.replace("the forty-two NEW ONE each on their subjects with their lines\\' first verses", "the forty-two NEW ONE each on their subjects with their lines\\' first verses (see_the_land_from_afar_not_go_there TWO since %s\\'s reuse at 34:4 — retyped from the tape\\'s first-run print, 20b\\'s precedent)" % W.split(' (')[0], 1)
assert new != line and new.count(repr(T42)) == 1; s = s.replace(line, new)
for name, old, com, lab_old, lab_new in (('DN4', D62, C62, "gathered_to_his_people 5 — Aaron\\'s the fifth", "gathered_to_his_people 6 — Aaron\\'s the fifth, Moses\\' the sixth (%s\\'s reuse at 34:5; retyped from the tape\\'s first-run print)" % W.split(' (')[0]),
                                        ('DO4', D47, C47, "gathered_to_his_people 5, counted 22", "gathered_to_his_people 6 (Moses\\' the sixth — %s\\'s reuse at 34:5), see_the_land_from_afar_not_go_there 2 (%s\\'s reuse at 34:4; both retyped from the tape\\'s first-run print), counted 22" % (W.split(' (')[0], W.split(' (')[0]))):
    i = s.index("    cp('%s THE KIN" % name); e = s.index('\n', i); line = s[i:e]
    assert line.count(repr(old)) == 1 and line.count(lab_old) == 1, (name, line.count(repr(old)), line.count(lab_old))
    s = s.replace(line, line.replace(repr(old), repr(com)).replace(lab_old, lab_new))
open(P, 'w', encoding='utf-8').write(s); py_compile.compile(P, doraise=True); print('the sequence file: DN2 (the forty-two), DN4 (the sixty-two), DO4 (the forty-seven) retyped from the print; compiles')
# 2. the probes Q49 and Q50
P = ROOT + '/World/step9/readback_probes.py'; s = open(P, encoding='utf-8').read()
for old, com, note in ((D62, C62, "Q49: gathered_to_his_people 5 -> 6 (Moses' death's REUSE at 34:5)"), (D47, C47, "Q50: gathered_to_his_people 5 -> 6 and see_the_land_from_afar_not_go_there 1 -> 2 (the death's REUSES at 34:5 and 34:4)")):
    assert s.count(repr(old)) == 1, (note, s.count(repr(old)))
    k = s.index(repr(old)); ls = s.rfind('\n', 0, k) + 1
    assert s[ls:].startswith('    return got =='), s[ls:ls + 40]
    s = s[:ls] + "    # %s: %s — retyped from the tape's first-run print (DN4/DO4 DIVERGE, declared against computed; 19b's and 20b's precedent — a reuse moves the older probes' counts)\n" % (W, note) + s[ls:].replace(repr(old), repr(com), 1)
open(P, 'w', encoding='utf-8').write(s); py_compile.compile(P, doraise=True); print('the probes Q49 and Q50 retyped from the print; compiles')
# 3. the two runners — the KIN asserts tolerant of the counts before and after the fold carries chapter 34
for fn, com, cpname in (('cold_run_song_charge_nebo.py', C62, 'DN4'), ('cold_run_blessing_of_moses.py', C47, 'DO4')):
    P = ROOT + '/World/step9/' + fn; s = open(P, encoding='utf-8').read()
    m = re.search(r"^KIN_EXPECTED = \((.*?)\)   #.*$", s, re.M); assert m, fn
    assert 'KIN_AFTER_22B' not in s
    s = s[:m.end()] + "\nKIN_AFTER_22B = %r   # %s: the same counts AFTER the death's reuses (gathered_to_his_people 6%s) — the one database before the fold carries chapter 34 holds KIN_EXPECTED, after it this tuple (the chain's tape step imports this runner before the build); typed from the tape's first-run print (%s computed)" % (com, W, "; see_the_land_from_afar_not_go_there 2" if cpname == 'DO4' else '', cpname) + s[m.end():]
    old = "or tuple(KIN_COUNTS.values()) == KIN_EXPECTED, ["; assert s.count(old) == 1, (fn, s.count(old))
    s = s.replace(old, "or tuple(KIN_COUNTS.values()) in (KIN_EXPECTED, KIN_AFTER_22B), [")
    open(P, 'w', encoding='utf-8').write(s); py_compile.compile(P, doraise=True); print(fn, '— KIN_AFTER_22B added, the assert tolerant; compiles')
print('RETYPED: 3 checkpoints, 2 probes, 2 runners')

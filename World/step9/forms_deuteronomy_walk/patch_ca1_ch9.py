import os as _os
_ROOT = _os.path.normpath(_os.path.join(_os.path.dirname(_os.path.abspath(__file__)), '..', '..', '..'))   # THE PORTABLE REPO (2026-09-15): the repo root from this file's own place
#!/usr/bin/env python3
# THE DEUTERONOMY WALK 7b (2026-09-19): ONE OLDER CHECKPOINT MOVED at the tape's first run (9/10) — CA1 (chapter 1b's LINES checkpoint) holds THE
# DEUTERONOMY MARKERS' LIST as a literal (every retrograde marker with its stated day, every forward marker's day) and grows with each new Deuteronomy
# marker: the 9/10 print showed CA1 DIVERGE alone — the design's DA9 note had named only the 'markers 167' COUNT literals (nine retyped by
# patch_seq_literals_ch9.py); the LIST literal is retyped here from the print (5b's and 6b's lesson on a stale literal, a third time: a literal that
# LISTS the markers moves as surely as one that counts them). patch_cc7_ch8.py's form.
import subprocess
ROOT = _ROOT
P = ROOT + '/World/step9/cold_run_sequence.py'
s = open(P, encoding='utf-8').read()
def rep(old, new, n=1):
    global s
    assert s.count(old) == n, (s.count(old), old[:100])
    s = s.replace(old, new)
rep("[(40, 11, 1), (40, 11, 1), (40, 11, 1), (40, 11, 1)], [((2, 2, 20), 'Deut 1:6'), ((1, 2, 16), 'Deut 1:9'), ((40, 6, 1), 'Deut 2:2'), ((1, 3, 7), 'Deut 4:10'), ((1, 4, 17), 'Deut 4:13'), ((1, 3, 7), 'Deut 5:23')]",
    "[(40, 11, 1), (40, 11, 1), (40, 11, 1), (40, 11, 1), (40, 11, 1)], [((2, 2, 20), 'Deut 1:6'), ((1, 2, 16), 'Deut 1:9'), ((40, 6, 1), 'Deut 2:2'), ((1, 3, 7), 'Deut 4:10'), ((1, 4, 17), 'Deut 4:13'), ((1, 3, 7), 'Deut 5:23'), ((1, 4, 18), 'Deut 9:20')]")
rep("AS OF THE DEUTERONOMY WALK 3b (2026-09-16) six retrograde — chapter 5\\'s at 5:23 (1, 3, 7) joins — and four forward (5:32 the charge)'",
    "AS OF THE DEUTERONOMY WALK 3b (2026-09-16) six retrograde — chapter 5\\'s at 5:23 (1, 3, 7) joins — and four forward (5:32 the charge); AS OF THE DEUTERONOMY WALK 7b (2026-09-19) SEVEN retrograde — chapter 9\\'s at 9:20 (1, 4, 18), Aaron\\'s peril at the morrow of the breaking — and FIVE forward (9:21 the stretch\\'s end): the list literal retyped from the tape\\'s first print (9/10)'")
open(P, 'w', encoding='utf-8').write(s)
import py_compile; py_compile.compile(P, doraise=True)
print('CA1 retyped from the print: the seventh retrograde marker (Deut 9:20, (1, 4, 18)) and the fifth forward (9:21); compiles')

import os as _os
_ROOT = _os.path.normpath(_os.path.join(_os.path.dirname(_os.path.abspath(__file__)), '..', '..', '..'))   # THE PORTABLE REPO (2026-09-15): the repo root from this file's own place
#!/usr/bin/env python3
# THE DEUTERONOMY WALK 14b (LEAN): DD4 RETYPED FROM THE TAPE'S PRINT — chapter 12's hole scan (the effects naming the place, the gates' bar, the rejoicing … on Israel)
# matched THIS chapter's passover_in_the_gates_barred by the substring 'in_the_gates' (the tape's first run 9/10; checkpoint_check's 19th miss): the later chapter's own
# write excluded from the earlier chapter's scan with the sitting's note — 13b's DG7 lesson (a later filing moves the checkpoint that counts the file) and 14b's own
# lesson (a hole pattern is the effect's own name). The declared tuple unmoved. RUN FROM THE REPO ROOT; then the tape again (a pass after any source change starts at the tape).
import subprocess
ROOT = _ROOT
P = ROOT + '/World/step9/cold_run_sequence.py'
s = open(P, encoding='utf-8').read()
old = "    holes_pn = sorted({e['effect'] for e in LG('israel') if any(t in e['effect'] for t in ('place_chosen', 'rejoicing_before', 'profane_slaughter', 'in_the_gates', 'levite_forsaking', 'name_erasure', 'foreign_rite'))})\n"
new = "    holes_pn = sorted({e['effect'] for e in LG('israel') if any(t in e['effect'] for t in ('place_chosen', 'rejoicing_before', 'profane_slaughter', 'in_the_gates', 'levite_forsaking', 'name_erasure', 'foreign_rite')) and e['effect'] != 'passover_in_the_gates_barred'})   # THE DEUTERONOMY WALK 14b (2026-09-23; LEAN): passover_in_the_gates_barred — chapter 16's own block at 16:5, its name carrying 'in_the_gates' — excluded from chapter 12's scan (the tape's first run 9/10: the later chapter's write moved the earlier chapter's hole count; retyped from the print)\n"
assert s.count(old) == 1, s.count(old)
s = s.replace(old, new)
old2 = "the seven names absent from both registries at the commit 4af2953 (asserted at add_types_ch12.py)', (sorted(OWN7_PN), True, True, 3), (holes_pn,"
new2 = "the seven names absent from both registries at the commit 4af2953 (asserted at add_types_ch12.py); THE DEUTERONOMY WALK 14b (2026-09-23): chapter 16\\'s passover_in_the_gates_barred excluded from this scan — a later chapter\\'s write, its name carrying the gates\\' substring', (sorted(OWN7_PN), True, True, 3), (holes_pn,"
assert s.count(old2) == 1, s.count(old2)
s = s.replace(old2, new2)
open(P, 'w', encoding='utf-8').write(s)
import py_compile; py_compile.compile(P, doraise=True); print('DD4 retyped: chapter 16\'s block excluded from chapter 12\'s hole scan; the file compiles')

import os as _os
_ROOT = _os.path.normpath(_os.path.join(_os.path.dirname(_os.path.abspath(__file__)), '..', '..', '..'))   # THE PORTABLE REPO (2026-09-15): the repo root from this file's own place
# THE DEUTERONOMY WALK 18b (2026-09-26; LEAN) — RUN B: persons_poor_court's import-time KIN_EXPECTED (17b's DK4 counts on the fold) moved by 28:1's reuse of
# blessings_for_hearing (2 -> 3) — the runner's fifth graded run and the tape's third run tripped at IMPORT ([('blessings_for_hearing', 3, 2)]); retyped from that print
# with the 18b note (13b's "since" form). A FOURTH scan form the census had not covered: an older runner's KIN_EXPECTED counts over the fold — the lesson for the AS BUILT.
import subprocess
ROOT = _ROOT
F = f'{ROOT}/World/step9/cold_run_persons_poor_court.py'; t = open(F, encoding='utf-8').read()
old = "KIN_EXPECTED = (2, 1, 7, 2, 0, 1, 1, 1, 1, 9, 2, 2, 1, 1, 1, 1, 1, 1, 1, 0, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 1, 2, 2, 2, 1, 1, 0, 0, 0, 0, 0)   # DK4 — the recon's counts on the running world (ch22_compile_recon.out, section G; the probe Q46's KIN tuple)"
assert t.count(old) == 1
new = "KIN_EXPECTED = (2, 1, 7, 2, 0, 1, 1, 1, 1, 9, 2, 2, 1, 1, 1, 1, 1, 1, 1, 0, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 1, 2, 3, 2, 1, 1, 0, 0, 0, 0, 0)   # DK4 — the recon's counts on the running world (ch22_compile_recon.out, section G; the probe Q46's KIN tuple); blessings_for_hearing (the thirty-fourth) TWO -> THREE since THE DEUTERONOMY WALK 18b (2026-09-26; LEAN): 28:1's third entry on the line blessings_condition_declared — THE REUSE; read at the fifth graded run's import ([('blessings_for_hearing', 3, 2)]) once the fold carried it"
t = t.replace(old, new); open(F, 'w', encoding='utf-8').write(t); print('persons_poor_court KIN_EXPECTED[33] 2 -> 3')

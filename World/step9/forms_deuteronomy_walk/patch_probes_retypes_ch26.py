import os as _os
_ROOT = _os.path.normpath(_os.path.join(_os.path.dirname(_os.path.abspath(__file__)), '..', '..', '..'))   # THE PORTABLE REPO (2026-09-15): the repo root from this file's own place
# THE DEUTERONOMY WALK 18b (2026-09-26; LEAN) — RUN B: THE READBACK PROBES THAT COUNT A REUSED EFFECT RETYPED BEFORE THE TAPE'S SECOND RUN — the grep decided (13b's
# precedent, readback_probes.py's 13b comments): the tape's first print (ch26_tape_run1.out) moved blessings_for_hearing 2 -> 3 (28:1), rejoicing 2 -> 4 (26:11, 27:7),
# poor_tithe_owed 1 -> 2 (26:12), rain_in_its_season 1 -> 2 (28:12) — the design's REUSE_AFTER; eight probe lines hold the old counts (found by grep on the four names;
# every `return got ==` in the file read). Each edit asserted on its own line; an 18b comment line above each return.
import subprocess, sys
ROOT = _ROOT
F = f'{ROOT}/World/step9/readback_probes.py'; L = open(F, encoding='utf-8').read().split('\n')
M = '# THE DEUTERONOMY WALK 18b (2026-09-26; LEAN): '
E = [
 (228, "(1, 1, 1, False, 172, 1, 1, 1, 1, 2, 2, 1, 'Deut 7:1', 'Deut 7:25')", "(1, 1, 1, False, 172, 1, 1, 1, 1, 3, 2, 1, 'Deut 7:1', 'Deut 7:25')", "blessings_for_hearing TWO -> THREE on israel_people (28:1's third entry on the line blessings_condition_declared — THE REUSE; retyped BEFORE the tape's second run, the first run's print decided)"),
 (268, "(1, 2, 1, 1, 1, 1, 2, 1, True, 'Deut 8:1', 'boot')", "(1, 2, 1, 1, 1, 1, 3, 1, True, 'Deut 8:1', 'boot')", "blessings_for_hearing TWO -> THREE on israel_people (28:1's third entry — THE REUSE; retyped BEFORE the tape's second run)"),
 (415, "((1, 'Deut 11:13'), (1, 'Deut 11:13'), (1, 'Deut 11:13'), (1, 'Deut 11:26'), (1, 'Deut 11:26'))", "((2, 'Deut 11:13'), (1, 'Deut 11:13'), (1, 'Deut 11:13'), (1, 'Deut 11:26'), (1, 'Deut 11:26'))", "rain_in_its_season ONE -> TWO on israel_people (28:12's second entry on the line heavens_treasure_lending_declared — THE REUSE; the first source's head 'Deut 11:13' stands; retyped BEFORE the tape's second run)"),
 (434, "((1, 1, 2, 2, 1, 2, 1, 1, 1, 1), ", "((1, 1, 3, 2, 1, 2, 1, 1, 1, 1), ", "blessings_for_hearing (the third) TWO -> THREE on israel_people (28:1's third entry — THE REUSE; retyped BEFORE the tape's second run)"),
 (477, "(2, 'Deut 12:5'), (1, 'Deut 12:15')", "(4, 'Deut 12:5'), (1, 'Deut 12:15')", "rejoicing_before_the_lord_commanded TWO -> FOUR on israel_people (26:11's third and 27:7's fourth entries on the lines first_fruits_declared and stones_altar_declared — THE REUSES; retyped BEFORE the tape's second run)"),
 (600, "(1, 'Deut 14:28')), ((2, ['Deut 12:5', 'Deut 14:22']), (2, ['Deut 12:15', 'Deut 14:22']))", "(2, 'Deut 14:28')), ((4, ['Deut 12:5', 'Deut 14:22', 'Deut 26:1', 'Deut 27:1']), (2, ['Deut 12:15', 'Deut 14:22']))", "poor_tithe_owed ONE -> TWO (26:12's second entry on the line tithe_confession_declared) and rejoicing TWO -> FOUR with the sources 26:1 and 27:1 (the lines' first verses) on israel_people — THE REUSES; retyped BEFORE the tape's second run"),
 (663, "((2, ['Deut 7:12', 'Deut 15:1']), (2, ['Exod 2:23', 'Deut 15:7'])", "((3, ['Deut 7:12', 'Deut 15:1', 'Deut 28:1']), (2, ['Exod 2:23', 'Deut 15:7'])", "blessings_for_hearing TWO -> THREE with the third source 28:1 on israel_people — THE REUSE; retyped BEFORE the tape's second run"),
 (803, "(2, 1, 7, 2, 0, 1, 1, 1, 1, 9, 2, 2, 1, 1, 1, 1, 1, 1, 1, 0, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 1, 2, 2, 2, 1, 1, 0, 0, 0, 0, 0)", "(2, 1, 7, 2, 0, 1, 1, 1, 1, 9, 2, 2, 1, 1, 1, 1, 1, 1, 1, 0, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 1, 2, 3, 2, 1, 1, 0, 0, 0, 0, 0)", "blessings_for_hearing (the thirty-fourth of KIN) TWO -> THREE on israel_people (28:1's third entry — THE REUSE; retyped BEFORE the tape's second run)"),
]
for ln, old, new, note in E:
    l = L[ln - 1]; assert l.count(old) == 1 and l.lstrip().startswith('return got =='), (ln, l.count(old), l[:60])
    L[ln - 1] = l.replace(old, new)
for ln, old, new, note in sorted(E, key=lambda e: -e[0]):
    ind = L[ln - 1][:len(L[ln - 1]) - len(L[ln - 1].lstrip())]; L.insert(ln - 1, ind + M + note)
open(F, 'w', encoding='utf-8').write('\n'.join(L)); print('readback_probes.py: %d lines retyped, %d comment lines added' % (len(E), len(E)))

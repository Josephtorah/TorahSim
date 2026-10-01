import os as _os
_ROOT = _os.path.normpath(_os.path.join(_os.path.dirname(_os.path.abspath(__file__)), '..', '..', '..'))   # THE PORTABLE REPO (2026-09-15): the repo root from this file's own place
#!/usr/bin/env python3
# THE DEUTERONOMY WALK 22b (2026-09-30; LEAN) — RUN B: THE DEPENDENCY GATE'S DEMANDS FILED FROM ITS FIRST PRINT (ch34b_dependency_first.out — two failures): (1) THE POINTER Deut 34:9 AS_WHEN
# in moses_death ("as the LORD commanded" — the receipt formula the gate's pointer finder reads): RUN_CITATION, reference — THE RECEIPT of the chapter, its referent BEHIND on the tape (the
# commission Numbers 27:18-23 — joshua_commissioned at 27:22, invested_office on yehoshua; 31:7 and 31:23); 20:17's form (16b); (2) THE REGISTRATION EDGE sequence -> moses_death (the live
# edge the gate reads — the import line patched FIRST this sitting, before the stitcher: the sequence file asserts the daemon order at import, 22b's find); NO token edge demanded (the gate's
# print names none — the two-letter 'to' at 34:1 and 34:10 raised no demand); the twenty CALL edges every one LIVE at the first print. 21b's form (patch_deps_ch33.py). RUN FROM THE REPO ROOT.
import subprocess, yaml, sys
ROOT = _ROOT
F = f'{ROOT}/World/step9/dependency_dispositions.yaml'
t = open(F, encoding='utf-8').read()
d0 = yaml.safe_load(t); E0, P0 = len(d0['edges']), len(d0['pointers']); print('before: edges', E0, 'pointers', P0)
M = 'THE DEUTERONOMY WALK 22b (2026-09-30; LEAN)'
R = 'moses_death'
assert E0 == 1001 and P0 == 230, (E0, P0)   # THE TYPES' print (ch34b_types_b.out): 'edges 1001, pointers 230'
# 1. THE REGISTRATION EDGE after the sequence -> blessing_of_moses edge (the gate's first failure: LIVE EDGE sequence -> moses_death has NO ENTRY on file)
i = t.index('  - {from: sequence, to: blessing_of_moses, disposition: CALL, link: none,\n'); j = t.index('\n', t.index('\n', i) + 1) + 1
assert t[j:].startswith('  - {from: '), t[j:j + 80]
REG = (f'  - {{from: sequence, to: {R}, disposition: CALL, link: none,\n'
       f'     why: "{M} | THE REGISTRATION EDGE — the sequence file imports cold_run_moses_death (the live edge the gate reads; DAEMON_ORDER carries law_moses_death) so chapter 34\'s six own-day lines in two forms join the tape after the last Deuteronomy 33 line with NO MARKER (Moses\' last day, 19b\'s; the thirty days a duration) — THE BOOK\'S LAST RUNNER; filed from the gate\'s first print (FAIL LIVE EDGE sequence -> moses_death has NO ENTRY on file); the import line patched BEFORE the stitcher this sitting (the sequence file asserts the daemon order against the dispositions at import — the register gate run alone before the registration fell at that assert: 22b\'s find)"}}\n')
t = t[:j] + REG + t[j:]
# 2. THE POINTER Deut 34:9 AS_WHEN — after the last pointer entry (32:50's, 20b's)
anchor = '  - {verse: "Deut 32:50", form: AS_WHEN, runner: song_charge_nebo, disposition: RUN_CITATION, link: reference, why: "'
i = t.index(anchor); j = t.index('\n', i) + 1
assert t[j:].strip() == '' or t[j:].startswith('\n') or t[j:].startswith('  - {'), repr(t[j:j + 60])
PTR = ('  - {verse: "Deut 34:9", form: AS_WHEN, runner: %s, disposition: RUN_CITATION, link: reference, why: "%s | \'and the children of Israel hearkened to him, and did AS THE LORD COMMANDED MOSES\' (the gate\'s own print: the AS_WHEN pointer at 34:9 — the receipt formula, thirty-eight Torah seats and this the last) — THE RECEIPT of chapter 34, BEHIND on the tape: the run citation of THE COMMISSION Numbers 27:18-23 (joshua_commissioned at 27:22 — invested_office on yehoshua; 31:7 and 31:23 the charge and the commission at the tent; the readback\'s RECEIPT ROW 34:9 against it — tape_kind joshua_commissioned, first verse Num 27:22; zelophehad and opening_speech.the_commission the_hand_laid by CALL); the register\'s one seat in the chapter (the formula\'s seats over Deut 34 = [\'Deut 34:9\']) dispositioned in register_dispositions.yaml from the register gate\'s print after the stitcher; no pointer row of the readback (the receipt behind) — 16b\'s Deut 20:17 and 15b\'s Deut 18:2 precedent; predicted at the design (DEUTERONOMY_WALK.md \'Sitting 22b\' THE KIN BY CALL — the receipt a RUN CITATION)"}\n' % (R, M))
t = t[:j] + PTR + t[j:]
d1 = yaml.safe_load(t); E1, P1 = len(d1['edges']), len(d1['pointers']); print('after: edges', E1, 'pointers', P1)
assert E1 == E0 + 1 and P1 == P0 + 1, (E1, P1)
assert [p for p in d1['pointers'] if p['verse'] == 'Deut 34:9'][0]['disposition'] == 'RUN_CITATION'
open(F, 'w', encoding='utf-8').write(t); print('WRITTEN; the departures: the registration edge sequence -> moses_death (the first failure) and the AS_WHEN pointer Deut 34:9 RUN_CITATION, reference (the second — the receipt behind, 20:17\'s form); NO token edge demanded; every CALL edge live at the first print')

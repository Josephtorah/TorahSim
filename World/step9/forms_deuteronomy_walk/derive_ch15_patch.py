#!/usr/bin/env python3
# THE DEUTERONOMY WALK sitting 13 — CHAPTER 15 (2026-09-22, the tail): derives ch15_patch_overrides.py from the FORMS' ch14_patch_overrides.py by ASSERTED
# substitutions (each old string present exactly once); sitting 12's derive_ch14_patch.py the form. The source is the forms' copy — its portable header
# (_ROOT from the file's own place) stripped and the scratch form's ROOT (from git) restored, so the derived script runs from the scratchpad. The two counts
# (44 by gloss, 168 by reference) READ FROM THE INK'S THIRD-PASS PRINT (ch15_ink_run3.out), never typed from the hand. RUN FROM THE REPO ROOT.
import subprocess
ROOT = _ROOT
SP = __file__.rsplit('/', 1)[0]
t = open(f'{ROOT}/World/step9/forms_deuteronomy_walk/ch14_patch_overrides.py', encoding='utf-8').read()
HDR = "import os as _os\n_ROOT = _os.path.normpath(_os.path.join(_os.path.dirname(_os.path.abspath(__file__)), '..', '..', '..'))   # THE PORTABLE REPO (2026-09-15): the repo root from this file's own place\n"
assert t.startswith(HDR) and t.count('ROOT = _ROOT\n') == 1
t = t[len(HDR):].replace('ROOT = _ROOT\n', "ROOT = _ROOT\n")
assert '_ROOT' not in t
p3 = open(f'{SP}/ch15_ink_run3.out', encoding='utf-8').read()
import re
m = re.search(r'THE DISPLAY PATCH PREDICTED — by gloss (\d+) by reference (\d+)', p3); assert m and '0 failing statements' in p3
NG, NR = m.groups()
subs = [
 ('# THE DEUTERONOMY WALK sitting 12 — CHAPTER 14 (2026-09-21)', '# THE DEUTERONOMY WALK sitting 13 — CHAPTER 15 (2026-09-22)'),
 ('(the census in ch14_ink.py, GLOSS_FAMILY asserted against the store)', '(the census in ch15_ink.py, GLOSS_FAMILY asserted against the store)'),
 ("THE ROWS ARE READ FROM ch14_ink.py's OWN LISTS", "THE ROWS ARE READ FROM ch15_ink.py's OWN LISTS"),
 ("Sitting 11's form (ch13_patch_overrides.py): the anchors the LAST ROWS of sitting 11's two blocks — the by_gloss block's last row found by\n# walking from sitting 11's marker (never typed), the by_ref block's last row 13:19's.", "Sitting 12's form (ch14_patch_overrides.py): the anchors the LAST ROWS of sitting 12's two blocks — the by_gloss block's last row found by\n# walking from sitting 12's marker (never typed), the by_ref block's last row 14:29's."),
 ('    import ch14_ink as I\n', '    import ch15_ink as I\n'),
 ('assert len(GL) == 49 and len(REF) == 131, (len(GL), len(REF))', f'assert len(GL) == {NG} and len(REF) == {NR}, (len(GL), len(REF))   # the counts read from the ink\'s third-pass print'),
 ('assert \'"Deut.14.\' not in t and all(', 'assert \'"Deut.15.\' not in t and all('),
 ("MARK = 'THE DEUTERONOMY WALK sitting 12 (2026-09-21, Deuteronomy 14)'", "MARK = 'THE DEUTERONOMY WALK sitting 13 (2026-09-22, Deuteronomy 15)'"),
 ("M5 = 'THE DEUTERONOMY WALK sitting 11 (2026-09-21, Deuteronomy 13)'", "M5 = 'THE DEUTERONOMY WALK sitting 12 (2026-09-21, Deuteronomy 14)'"),
 ("assert len(rows) == 34, len(rows)   # sitting 11's thirty-four by-gloss rows", "assert len(rows) == 49, len(rows)   # sitting 12's forty-nine by-gloss rows"),
 ("(censused in the reading\\'s ink script, ch14_ink.GLOSS_FAMILY)", "(censused in the reading\\'s ink script, ch15_ink.GLOSS_FAMILY)"),
 ('m2 = re.search(r\'^  "Deut\\.13\\.19:15": "in-the-eyes-of"[^\\n]*\\n\', t, re.M); assert m2 and t.count(\'"Deut.13.19:15": "in-the-eyes-of"\') == 1', 'm2 = re.search(r\'^  "Deut\\.14\\.29:23": "you-do"[^\\n]*\\n\', t, re.M); assert m2 and t.count(\'"Deut.14.29:23": "you-do"\') == 1'),
]
for a, b in subs:
    assert t.count(a) == 1, ('NOT ONCE', t.count(a), a[:80])
    t = t.replace(a, b)
assert 'ch14_ink' not in t and 'sitting 12 — CHAPTER' not in t and '13.19' not in t and 'ch13_' not in t, [l for l in t.splitlines() if 'ch14_ink' in l or '13.19' in l or 'ch13_' in l]
open(f'{SP}/ch15_patch_overrides.py', 'w', encoding='utf-8').write(t)
print('derived', len(t), 'bytes,', len(subs), 'substitutions; the counts from the print:', NG, NR)

#!/usr/bin/env python3
# THE DEUTERONOMY WALK sitting 12 — CHAPTER 14 (2026-09-21, the tail): derives ch14_patch_overrides.py from the FORMS' ch13_patch_overrides.py by ASSERTED
# substitutions (each old string present exactly once); sitting 11's derive_ch13_patch.py the form. The source is the forms' copy — its portable header
# (_ROOT from the file's own place) stripped and the scratch form's ROOT (from git) restored, so the derived script runs from the scratchpad.
# RUN FROM THE REPO ROOT.
import subprocess
ROOT = _ROOT
SP = __file__.rsplit('/', 1)[0]
t = open(f'{ROOT}/World/step9/forms_deuteronomy_walk/ch13_patch_overrides.py', encoding='utf-8').read()
HDR = "import os as _os\n_ROOT = _os.path.normpath(_os.path.join(_os.path.dirname(_os.path.abspath(__file__)), '..', '..', '..'))   # THE PORTABLE REPO (2026-09-15): the repo root from this file's own place\n"
assert t.startswith(HDR) and t.count('ROOT = _ROOT\n') == 1
t = t[len(HDR):].replace('ROOT = _ROOT\n', "ROOT = _ROOT\n")
assert '_ROOT' not in t
subs = [
 ('# THE DEUTERONOMY WALK sitting 11 — CHAPTER 13 (2026-09-21)', '# THE DEUTERONOMY WALK sitting 12 — CHAPTER 14 (2026-09-21)'),
 ('(the census in ch13_ink.py, GLOSS_FAMILY asserted against the store)', '(the census in ch14_ink.py, GLOSS_FAMILY asserted against the store)'),
 ("THE ROWS ARE READ FROM ch13_ink.py's OWN LISTS", "THE ROWS ARE READ FROM ch14_ink.py's OWN LISTS"),
 ("Sitting 10's form (ch12_patch_overrides.py): the anchors the LAST ROWS of sitting 10's two blocks — the by_gloss block's last row found by\n# walking from sitting 10's marker (never typed), the by_ref block's last row 12:31's.", "Sitting 11's form (ch13_patch_overrides.py): the anchors the LAST ROWS of sitting 11's two blocks — the by_gloss block's last row found by\n# walking from sitting 11's marker (never typed), the by_ref block's last row 13:19's."),
 ('    import ch13_ink as I\n', '    import ch14_ink as I\n'),
 ('assert len(GL) == 34 and len(REF) == 139, (len(GL), len(REF))', 'assert len(GL) == 49 and len(REF) == 131, (len(GL), len(REF))'),
 ('assert \'"Deut.13.\' not in t and all(', 'assert \'"Deut.14.\' not in t and all('),
 ("MARK = 'THE DEUTERONOMY WALK sitting 11 (2026-09-21, Deuteronomy 13)'", "MARK = 'THE DEUTERONOMY WALK sitting 12 (2026-09-21, Deuteronomy 14)'"),
 ("M5 = 'THE DEUTERONOMY WALK sitting 10 (2026-09-20, Deuteronomy 12)'", "M5 = 'THE DEUTERONOMY WALK sitting 11 (2026-09-21, Deuteronomy 13)'"),
 ("assert len(rows) == 69, len(rows)   # sitting 10's sixty-nine by-gloss rows", "assert len(rows) == 34, len(rows)   # sitting 11's thirty-four by-gloss rows"),
 ("(censused in the reading\\'s ink script, ch13_ink.GLOSS_FAMILY)", "(censused in the reading\\'s ink script, ch14_ink.GLOSS_FAMILY)"),
 ('m2 = re.search(r\'^  "Deut\\.12\\.31:19": "they-burn"[^\\n]*\\n\', t, re.M); assert m2 and t.count(\'"Deut.12.31:19": "they-burn"\') == 1', 'm2 = re.search(r\'^  "Deut\\.13\\.19:15": "in-the-eyes-of"[^\\n]*\\n\', t, re.M); assert m2 and t.count(\'"Deut.13.19:15": "in-the-eyes-of"\') == 1'),
]
for a, b in subs:
    assert t.count(a) == 1, ('NOT ONCE', t.count(a), a[:80])
    t = t.replace(a, b)
assert 'ch13_ink' not in t and 'sitting 11 — CHAPTER' not in t and '12.31' not in t and 'ch12_' not in t, [l for l in t.splitlines() if 'ch13_ink' in l or '12.31' in l or 'ch12_' in l]
open(f'{SP}/ch14_patch_overrides.py', 'w', encoding='utf-8').write(t)
print('derived', len(t), 'bytes,', len(subs), 'substitutions')

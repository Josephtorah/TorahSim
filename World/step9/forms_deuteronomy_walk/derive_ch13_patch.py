import os as _os
_ROOT = _os.path.normpath(_os.path.join(_os.path.dirname(_os.path.abspath(__file__)), '..', '..', '..'))   # THE PORTABLE REPO (2026-09-15): the repo root from this file's own place
# derives ch13_patch_overrides.py from the chapter-12 form by ASSERTED substitutions (each old string present exactly once); sitting 10's derive_ch12_patch.py the form
# (the source the scratchpad's ch12_patch_overrides.py — the scratch form with ROOT from git; no _ROOT to strip)
import subprocess
ROOT = _ROOT
SP = __file__.rsplit('/', 1)[0]
t = open(f'{SP}/ch12_patch_overrides.py', encoding='utf-8').read()
assert '_ROOT' not in t
subs = [
 ('# THE DEUTERONOMY WALK sitting 10 — CHAPTER 12 (2026-09-20)', '# THE DEUTERONOMY WALK sitting 11 — CHAPTER 13 (2026-09-21)'),
 ('(the census in ch12_ink.py, GLOSS_FAMILY asserted against the store)', '(the census in ch13_ink.py, GLOSS_FAMILY asserted against the store)'),
 ("THE ROWS ARE READ FROM ch12_ink.py's OWN LISTS", "THE ROWS ARE READ FROM ch13_ink.py's OWN LISTS"),
 ("Sitting 9's form (ch11_patch_overrides.py): the anchors the LAST ROWS of sitting 9's two blocks — the by_gloss block's last row found by\n# walking from sitting 9's marker (never typed), the by_ref block's last row 11:32's.", "Sitting 10's form (ch12_patch_overrides.py): the anchors the LAST ROWS of sitting 10's two blocks — the by_gloss block's last row found by\n# walking from sitting 10's marker (never typed), the by_ref block's last row 12:31's."),
 ('    import ch12_ink as I\n', '    import ch13_ink as I\n'),
 ('assert len(GL) == 69 and len(REF) == 124, (len(GL), len(REF))', 'assert len(GL) == 34 and len(REF) == 139, (len(GL), len(REF))'),
 ('assert \'"Deut.12.\' not in t and all(', 'assert \'"Deut.13.\' not in t and all('),
 ("MARK = 'THE DEUTERONOMY WALK sitting 10 (2026-09-20, Deuteronomy 12)'", "MARK = 'THE DEUTERONOMY WALK sitting 11 (2026-09-21, Deuteronomy 13)'"),
 ("M5 = 'THE DEUTERONOMY WALK sitting 9 (2026-09-20, Deuteronomy 11)'", "M5 = 'THE DEUTERONOMY WALK sitting 10 (2026-09-20, Deuteronomy 12)'"),
 ("assert len(rows) == 64, len(rows)   # sitting 9's sixty-four by-gloss rows", "assert len(rows) == 69, len(rows)   # sitting 10's sixty-nine by-gloss rows"),
 ("(censused in the reading\\'s ink script, ch12_ink.GLOSS_FAMILY)", "(censused in the reading\\'s ink script, ch13_ink.GLOSS_FAMILY)"),
 ('m2 = re.search(r\'^  "Deut\\.11\\.32:11": "today"[^\\n]*\\n\', t, re.M); assert m2 and t.count(\'"Deut.11.32:11": "today"\') == 1', 'm2 = re.search(r\'^  "Deut\\.12\\.31:19": "they-burn"[^\\n]*\\n\', t, re.M); assert m2 and t.count(\'"Deut.12.31:19": "they-burn"\') == 1'),
]
for a, b in subs:
    assert t.count(a) == 1, ('NOT ONCE', t.count(a), a[:80])
    t = t.replace(a, b)
assert 'ch12_ink' not in t and 'sitting 10 — CHAPTER' not in t and '11.32' not in t, [l for l in t.splitlines() if 'ch12_ink' in l or '11.32' in l]
open(f'{SP}/ch13_patch_overrides.py', 'w', encoding='utf-8').write(t)
print('derived', len(t), 'bytes,', len(subs), 'substitutions')

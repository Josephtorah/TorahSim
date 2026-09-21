# derives ch12_patch_overrides.py from the chapter-11 form by ASSERTED substitutions (each old string present exactly once); sitting 9's derive_ch11_patch.py the form
import subprocess
ROOT = _ROOT
SP = __file__.rsplit('/', 1)[0]
t = open(f'{ROOT}/World/step9/forms_deuteronomy_walk/ch11_patch_overrides.py', encoding='utf-8').read()
GIT = "ROOT = _ROOT\n"
subs = [
 ("import os as _os\n_ROOT = _os.path.normpath(_os.path.join(_os.path.dirname(_os.path.abspath(__file__)), '..', '..', '..'))   # THE PORTABLE REPO (2026-09-15): the repo root from this file's own place\n", ''),
 ('ROOT = _ROOT\n', GIT),
 ('# THE DEUTERONOMY WALK sitting 9 — CHAPTER 11 (2026-09-20)', '# THE DEUTERONOMY WALK sitting 10 — CHAPTER 12 (2026-09-20)'),
 ('(the census in ch11_ink.py, GLOSS_FAMILY asserted against the store)', '(the census in ch12_ink.py, GLOSS_FAMILY asserted against the store)'),
 ("THE ROWS ARE READ FROM ch11_ink.py's OWN LISTS", "THE ROWS ARE READ FROM ch12_ink.py's OWN LISTS"),
 ("Sitting 8's form (ch10_patch_overrides.py): the anchors the LAST ROWS of sitting 8's two blocks — the by_gloss block's last row found by\n# walking from sitting 8's marker (never typed), the by_ref block's last row 10:22's.", "Sitting 9's form (ch11_patch_overrides.py): the anchors the LAST ROWS of sitting 9's two blocks — the by_gloss block's last row found by\n# walking from sitting 9's marker (never typed), the by_ref block's last row 11:32's."),
 ('    import ch11_ink as I\n', '    import ch12_ink as I\n'),
 ('assert len(GL) == 64 and len(REF) == 158, (len(GL), len(REF))', 'assert len(GL) == 69 and len(REF) == 124, (len(GL), len(REF))'),
 ('assert \'"Deut.11.\' not in t and all(', 'assert \'"Deut.12.\' not in t and all('),
 ("MARK = 'THE DEUTERONOMY WALK sitting 9 (2026-09-20, Deuteronomy 11)'", "MARK = 'THE DEUTERONOMY WALK sitting 10 (2026-09-20, Deuteronomy 12)'"),
 ("M5 = 'THE DEUTERONOMY WALK sitting 8 (2026-09-19, Deuteronomy 10)'", "M5 = 'THE DEUTERONOMY WALK sitting 9 (2026-09-20, Deuteronomy 11)'"),
 ("assert len(rows) == 38, len(rows)   # sitting 8's thirty-eight by-gloss rows", "assert len(rows) == 64, len(rows)   # sitting 9's sixty-four by-gloss rows"),
 ("(censused in the reading\\'s ink script, ch11_ink.GLOSS_FAMILY)", "(censused in the reading\\'s ink script, ch12_ink.GLOSS_FAMILY)"),
 ('m2 = re.search(r\'^  "Deut\\.10\\.22:6": "has-made-you"[^\\n]*\\n\', t, re.M); assert m2 and t.count(\'"Deut.10.22:6": "has-made-you"\') == 1', 'm2 = re.search(r\'^  "Deut\\.11\\.32:11": "today"[^\\n]*\\n\', t, re.M); assert m2 and t.count(\'"Deut.11.32:11": "today"\') == 1'),
]
for a, b in subs:
    assert t.count(a) == 1, ('NOT ONCE', t.count(a), a[:80])
    t = t.replace(a, b)
assert 'ch11_ink' not in t and 'sitting 9 — CHAPTER' not in t and '_ROOT' not in t, [l for l in t.splitlines() if 'ch11_ink' in l or '_ROOT' in l]
open(f'{SP}/ch12_patch_overrides.py', 'w', encoding='utf-8').write(t)
print('derived', len(t), 'bytes,', len(subs), 'substitutions')

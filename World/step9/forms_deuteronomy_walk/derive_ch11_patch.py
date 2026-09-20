# derives ch11_patch_overrides.py from the chapter-10 form by ASSERTED substitutions (each old string present exactly once)
import subprocess
ROOT = _ROOT
SP = __file__.rsplit('/', 1)[0]
t = open(f'{ROOT}/World/step9/forms_deuteronomy_walk/ch10_patch_overrides.py', encoding='utf-8').read()
subs = [
 ("import os as _os\n_ROOT = _os.path.normpath(_os.path.join(_os.path.dirname(_os.path.abspath(__file__)), '..', '..', '..'))   # THE PORTABLE REPO (2026-09-15): the repo root from this file's own place\n", ''),
 ('ROOT = _ROOT\n', "ROOT = _ROOT\n"),
 ('# THE DEUTERONOMY WALK sitting 8 — CHAPTER 10 (2026-09-19)', '# THE DEUTERONOMY WALK sitting 9 — CHAPTER 11 (2026-09-20)'),
 ('(the census in ch10_ink.py, GLOSS_FAMILY asserted against the store)', '(the census in ch11_ink.py, GLOSS_FAMILY asserted against the store)'),
 ("THE ROWS ARE READ FROM ch10_ink.py's OWN LISTS", "THE ROWS ARE READ FROM ch11_ink.py's OWN LISTS"),
 ("Sitting 7's form (ch9_patch_overrides.py): the anchors the LAST ROWS of sitting 7's two blocks — the by_gloss block's last row found by\n# walking from sitting 7's marker (never typed), the by_ref block's last row 9:5's.", "Sitting 8's form (ch10_patch_overrides.py): the anchors the LAST ROWS of sitting 8's two blocks — the by_gloss block's last row found by\n# walking from sitting 8's marker (never typed), the by_ref block's last row 10:22's."),
 ('    import ch10_ink as I\n', '    import ch11_ink as I\n'),
 ('assert len(GL) == 38 and len(REF) == 89, (len(GL), len(REF))', 'assert len(GL) == 64 and len(REF) == 158, (len(GL), len(REF))'),
 ('assert \'"Deut.10.\' not in t and all(', 'assert \'"Deut.11.\' not in t and all('),
 ("MARK = 'THE DEUTERONOMY WALK sitting 8 (2026-09-19, Deuteronomy 10)'", "MARK = 'THE DEUTERONOMY WALK sitting 9 (2026-09-20, Deuteronomy 11)'"),
 ("M5 = 'THE DEUTERONOMY WALK sitting 7 (2026-09-19, Deuteronomy 9)'", "M5 = 'THE DEUTERONOMY WALK sitting 8 (2026-09-19, Deuteronomy 10)'"),
 ("assert len(rows) == 36, len(rows)   # sitting 7's thirty-six by-gloss rows", "assert len(rows) == 38, len(rows)   # sitting 8's thirty-eight by-gloss rows"),
 ("(censused in the reading\\'s ink script, ch10_ink.GLOSS_FAMILY)", "(censused in the reading\\'s ink script, ch11_ink.GLOSS_FAMILY)"),
 ('m2 = re.search(r\'^  "Deut\\.9\\.5:18": "to-establish"[^\\n]*\\n\', t, re.M); assert m2 and t.count(\'"Deut.9.5:18": "to-establish"\') == 1', 'm2 = re.search(r\'^  "Deut\\.10\\.22:6": "has-made-you"[^\\n]*\\n\', t, re.M); assert m2 and t.count(\'"Deut.10.22:6": "has-made-you"\') == 1'),
]
for a, b in subs:
    assert t.count(a) == 1, ('NOT ONCE', t.count(a), a[:80])
    t = t.replace(a, b)
assert 'ch10_ink' not in t and 'sitting 8 — CHAPTER' not in t, [l for l in t.splitlines() if 'ch10_ink' in l]   # the form's own name (ch10_patch_overrides.py) stays in the comment
open(f'{SP}/ch11_patch_overrides.py', 'w', encoding='utf-8').write(t)
print('derived', len(t), 'bytes,', len(subs), 'substitutions')

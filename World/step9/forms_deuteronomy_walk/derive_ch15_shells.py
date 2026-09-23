import os as _os
_ROOT = _os.path.normpath(_os.path.join(_os.path.dirname(_os.path.abspath(__file__)), '..', '..', '..'))   # THE PORTABLE REPO (2026-09-15): the repo root from this file's own place
#!/usr/bin/env python3
# THE DEUTERONOMY WALK sitting 13 — CHAPTER 15 (2026-09-22, the tail): the three shells (the chain, the fold, the gates) DERIVED from sitting 12's copies in the
# forms folder by asserted substitutions — the form's own name protected in every shell (chapter 12's lesson 12), the fold's prediction 228 → 229 / 2252 → 2259,
# the unit deu_15_release_firstborn, then ch14 → ch15 everywhere else. Sitting 12's form (the reading's derive_ch14_shells.py, overwritten in the forms by 12b's
# compile derive of the same name — this script retypes the form's shape). RUN FROM THE REPO ROOT.
import subprocess, os, re
ROOT = _ROOT
SP = os.path.dirname(os.path.abspath(__file__))
FD = f'{ROOT}/World/step9/forms_deuteronomy_walk'
def sub(text, old, new, n=1):
    c = text.count(old); assert c == n, (old[:70], c, n); return text.replace(old, new)
out = {}
c = open(f'{FD}/ch14_chain.sh', encoding='utf-8').read()
c = sub(c, 'sitting 12 — CHAPTER 14 (the one run and its tail)', 'sitting 13 — CHAPTER 15 (two runs and the tail)')
c = sub(c, "Sitting 11's form (ch13_chain.sh)", "Sitting 12's form (@@FORM@@)")
c = sub(c, 'deu_14_food_tithe', 'deu_15_release_firstborn')   # once — the loop's name; the outputs use $u
c = c.replace('ch14', 'ch15').replace('@@FORM@@', 'ch14_chain.sh')
out['ch15_chain.sh'] = c
f = open(f'{FD}/ch14_fold.sh', encoding='utf-8').read()
f = sub(f, 'sitting 12 — CHAPTER 14 (the one run and its tail)', 'sitting 13 — CHAPTER 15 (two runs and the tail)')
f = sub(f, '(units 227 → 228,\n# standing 2245 → 2252, the hash unmoved', '(units 228 → 229,\n# standing 2252 → 2259, the hash unmoved')
f = sub(f, "Sitting 11's form (ch13_fold.sh)", "Sitting 12's form (@@FORM@@)")
f = sub(f, 'deu_14_food_tithe', 'deu_15_release_firstborn')
f = sub(f, "'assert len(W[\"units\"]) == 228\\n'", "'assert len(W[\"units\"]) == 229\\n'")
f = sub(f, "'assert len(W[\"units\"]) == 227\\n'", "'assert len(W[\"units\"]) == 228\\n'")
f = sub(f, "'assert len(W[\"standing\"]) == 2252\\n'", "'assert len(W[\"standing\"]) == 2259\\n'")
f = sub(f, "'assert len(W[\"standing\"]) == 2245\\n'", "'assert len(W[\"standing\"]) == 2252\\n'")
f = sub(f, "the tripwire set to the prediction: units 228, standing 2252, hash 8b8fff1fa28953af unmoved", "the tripwire set to the prediction: units 229, standing 2259, hash 8b8fff1fa28953af unmoved")
f = f.replace('ch14', 'ch15').replace('@@FORM@@', 'ch14_fold.sh')
out['ch15_fold.sh'] = f
g = open(f'{FD}/ch14_gates.sh', encoding='utf-8').read()
g = sub(g, "sitting 12 — CHAPTER 14 (the one run and its tail; sitting 11's form ch13_gates.sh)", "sitting 13 — CHAPTER 15 (two runs and the tail; sitting 12's form @@FORM@@)")
g = sub(g, 'deu_14_food_tithe', 'deu_15_release_firstborn')
g = g.replace('ch14', 'ch15').replace('@@FORM@@', 'ch14_gates.sh')
out['ch15_gates.sh'] = g
for name, text in out.items():
    clean = re.sub(r"ch14_\w+\.(?:py|sh)", '', text)   # the form citations name sitting 12's files on purpose
    assert 'ch14' not in clean and 'food_tithe' not in clean and '@@' not in text and 'sitting 12 —' not in text, (name, [l for l in clean.split('\n') if 'ch14' in l or 'food_tithe' in l][:2])
    open(f'{SP}/{name}', 'w', encoding='utf-8').write(text)
assert "== 227" not in out['ch15_fold.sh'] and "== 2245" not in out['ch15_fold.sh'] and out['ch15_fold.sh'].count('== 229') == 1 and out['ch15_fold.sh'].count('== 2259') == 1
print('derived:', {k: len(v) for k, v in out.items()})

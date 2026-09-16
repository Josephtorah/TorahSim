import os as _os
_ROOT = _os.path.normpath(_os.path.join(_os.path.dirname(_os.path.abspath(__file__)), '..', '..', '..'))   # THE PORTABLE REPO (2026-09-15): the repo root from this file's own place
#!/usr/bin/env python3
# THE DEUTERONOMY WALK sitting 1 — THE OPENING SPEECH (2026-09-15): the store's glosses at the three chapters' seats read back into the display
# layer's override file — BY GLOSS where the store's every token of the gloss is the one word (the census in deu_ink.py, GLOSS_FAMILY asserted
# against the store) and BY REFERENCE where the family is mixed. Display only; the draft units untouched. THE ROWS ARE READ FROM deu_ink.py's
# OWN LITERALS (one source of truth: the ink asserts the same rows present after this patch). Run ONCE (the anchors assert the rows absent
# first). Sitting 15's form (patch_overrides_ref.py).
import ast, os, re, subprocess, yaml
ROOT = _ROOT
SP = os.path.dirname(os.path.abspath(__file__))
src = open(f'{SP}/deu_ink.py', encoding='utf-8').read()
tree = ast.parse(src)
LIT = {n.targets[0].id: ast.literal_eval(n.value) for n in tree.body if isinstance(n, ast.Assign) and isinstance(n.targets[0], ast.Name) and n.targets[0].id in ('OVERRIDE_REF3', 'OVERRIDE_GLOSS')}
REF = [(k, v) for k, v, _ in LIT['OVERRIDE_REF3']]; GL = LIT['OVERRIDE_GLOSS']
TOK = {k: t for k, _, t in LIT['OVERRIDE_REF3']}
P = f'{ROOT}/logic/glosses/word_gloss_overrides.yaml'
t = open(P, encoding='utf-8').read()
assert '"Deut.1.' not in t and '"Deut.2.' not in t and '"Deut.3.' not in t and all(f'"{k}": ' not in t for k, _ in GL), [k for k, _ in GL if f'"{k}": ' in t]
m1 = re.search(r'^  "circle-them/their": "round-about-them"[^\n]*\n', t, re.M); assert m1 and t.count('"circle-them/their": "round-about-them"') == 1
A1 = m1.group(0)
gl_block = A1 + '\n  # THE DEUTERONOMY WALK sitting 1 (2026-09-15, Deuteronomy 1-3): the store\'s glosses whose every token is the one word (censused in the reading\'s ink script, deu_ink.GLOSS_FAMILY) — RESEARCH_LOG.md\n' + ''.join(f'  "{k}": "{v}"\n' for k, v in GL)
t = t.replace(A1, gl_block)
m2 = re.search(r'^  "Num\.35\.34:13": "I"[^\n]*\n', t, re.M); assert m2 and t.count('"Num.35.34:13": "I"') == 1
A2 = m2.group(0)
ref_block = A2 + '  # THE DEUTERONOMY WALK sitting 1 (2026-09-15, Deuteronomy 1-3): the store\'s glosses at the three chapters\' seats, by reference — the token named beside each — RESEARCH_LOG.md\n' + ''.join(f'  "{k}": "{v}"   # {TOK[k]}\n' for k, v in REF)
t = t.replace(A2, ref_block)
open(P, 'w', encoding='utf-8').write(t)
d = yaml.safe_load(open(P, encoding='utf-8'))
assert all(d['by_ref'][k] == v for k, v in REF) and all(d['by_gloss'][k] == v for k, v in GL)
print('override rows written: by_ref', len(REF), 'by_gloss', len(GL), '| by_ref total', len(d['by_ref']), '| by_gloss total', len(d['by_gloss']))

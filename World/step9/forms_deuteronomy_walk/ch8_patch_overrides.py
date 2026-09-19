#!/usr/bin/env python3
# THE DEUTERONOMY WALK sitting 6 — CHAPTER 8 (2026-09-18): the store's glosses at the chapter's seats read back into the display layer's override file — BY
# GLOSS where the store's every token of the gloss is the one word (the census in ch8_ink.py, GLOSS_FAMILY asserted against the store) and BY REFERENCE
# where the family is mixed. Display only; the draft unit untouched. THE ROWS ARE READ FROM ch8_ink.py's OWN LISTS. Run ONCE (the anchors assert the rows
# absent first). Sitting 5's form (ch7_patch_overrides.py): the anchors the LAST ROWS of sitting 5's two blocks — the by_gloss block's last row found by
# walking from sitting 5's marker (never typed), the by_ref block's last row 7:24's.
import os, re, subprocess, sys, io, contextlib, yaml
ROOT = subprocess.check_output(['git', 'rev-parse', '--show-toplevel'], text=True).strip()
SP = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, SP)
with contextlib.redirect_stdout(io.StringIO()):
    import ch8_ink as I
assert not I.PATCHED, 'already patched'
REF = I.OVERRIDE_REF; GL = I.OVERRIDE_GLOSS; TOK = {k: t for k, _, t in I.OVERRIDE_REF3}
assert len(GL) == 32 and len(REF) == 20, (len(GL), len(REF))
P = f'{ROOT}/logic/glosses/word_gloss_overrides.yaml'
t = open(P, encoding='utf-8').read()
assert '"Deut.8.' not in t and all(f'"{k}": ' not in t for k, _ in GL), [k for k, _ in GL if f'"{k}": ' in t]
MARK = 'THE DEUTERONOMY WALK sitting 6 (2026-09-18, Deuteronomy 8)'
assert MARK not in t
M5 = 'THE DEUTERONOMY WALK sitting 5 (2026-09-17, Deuteronomy 7)'
i = t.index(f'  # {M5}: the store\'s glosses whose every token')
j = t.index('\n', i) + 1
rows = []
while True:
    m = re.match(r'  "[^"]+": "[^"]*"[^\n]*\n', t[j:])
    if not m: break
    rows.append(m.group(0)); j += len(m.group(0))
assert len(rows) == 49, len(rows)   # sitting 5's forty-nine by-gloss rows
A1 = rows[-1]; assert t.count(A1) == 1
gl_block = A1 + f'\n  # {MARK}: the store\'s glosses whose every token is the one word (censused in the reading\'s ink script, ch8_ink.GLOSS_FAMILY) — RESEARCH_LOG.md\n' + ''.join(f'  "{k}": "{v}"\n' for k, v in GL)
t = t.replace(A1, gl_block)
m2 = re.search(r'^  "Deut\.7\.24:9": "shall-stand"[^\n]*\n', t, re.M); assert m2 and t.count('"Deut.7.24:9": "shall-stand"') == 1
A2 = m2.group(0)
ref_block = A2 + f'  # {MARK}: the store\'s glosses at the chapter\'s seats, by reference — the token named beside each; the indices the store\'s own — RESEARCH_LOG.md\n' + ''.join(f'  "{k}": "{v}"   # {TOK[k]}\n' for k, v in REF)
t = t.replace(A2, ref_block)
open(P, 'w', encoding='utf-8').write(t)
d = yaml.safe_load(open(P, encoding='utf-8'))
assert all(d['by_ref'][k] == v for k, v in REF) and all(d['by_gloss'][k] == v for k, v in GL)
print('override rows written: by_ref', len(REF), 'by_gloss', len(GL), '| by_ref total', len(d['by_ref']), '| by_gloss total', len(d['by_gloss']))

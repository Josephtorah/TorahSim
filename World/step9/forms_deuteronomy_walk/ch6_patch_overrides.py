#!/usr/bin/env python3
# THE DEUTERONOMY WALK sitting 4 — CHAPTER 6 (2026-09-17, run 3): the store's glosses at the chapter's seats read back into the display layer's
# override file — BY GLOSS where the store's every token of the gloss is the one word (the census in ch6_ink.py, GLOSS_FAMILY asserted against
# the store) and BY REFERENCE where the family is mixed. Display only; the draft unit untouched. THE ROWS ARE READ FROM ch6_ink.py's OWN
# LISTS (one source of truth: the ink asserts the same rows present after this patch — the by-reference keys computed from the store's own
# indices, never typed). Run ONCE (the anchors assert the rows absent first). Sitting 3's form (ch5_patch_overrides.py): the anchors the last
# rows of sitting 3's two blocks.
import os, re, subprocess, sys, io, contextlib, yaml
ROOT = subprocess.check_output(['git', 'rev-parse', '--show-toplevel'], text=True).strip()
SP = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, SP)
with contextlib.redirect_stdout(io.StringIO()):
    import ch6_ink as I
assert not I.PATCHED, 'already patched'
REF = I.OVERRIDE_REF; GL = I.OVERRIDE_GLOSS; TOK = {k: t for k, _, t in I.OVERRIDE_REF3}
assert len(GL) == 33 and len(REF) == 24, (len(GL), len(REF))
P = f'{ROOT}/logic/glosses/word_gloss_overrides.yaml'
t = open(P, encoding='utf-8').read()
assert '"Deut.6.' not in t and all(f'"{k}": ' not in t for k, _ in GL), [k for k, _ in GL if f'"{k}": ' in t]
MARK = 'THE DEUTERONOMY WALK sitting 4 (2026-09-17, Deuteronomy 6)'
assert MARK not in t
m1 = re.search(r'^  "mother-you/your": "your-mother"[^\n]*\n', t, re.M); assert m1 and t.count('"mother-you/your": "your-mother"') == 1
A1 = m1.group(0)
gl_block = A1 + f'\n  # {MARK}: the store\'s glosses whose every token is the one word (censused in the reading\'s ink script, ch6_ink.GLOSS_FAMILY) — RESEARCH_LOG.md\n' + ''.join(f'  "{k}": "{v}"\n' for k, v in GL)
t = t.replace(A1, gl_block)
m2 = re.search(r'^  "Deut\.5\.33:16": "you-shall-possess"[^\n]*\n', t, re.M); assert m2 and t.count('"Deut.5.33:16": "you-shall-possess"') == 1
A2 = m2.group(0)
ref_block = A2 + f'  # {MARK}: the store\'s glosses at the chapter\'s seats, by reference — the token named beside each; the indices the store\'s own — RESEARCH_LOG.md\n' + ''.join(f'  "{k}": "{v}"   # {TOK[k]}\n' for k, v in REF)
t = t.replace(A2, ref_block)
open(P, 'w', encoding='utf-8').write(t)
d = yaml.safe_load(open(P, encoding='utf-8'))
assert all(d['by_ref'][k] == v for k, v in REF) and all(d['by_gloss'][k] == v for k, v in GL)
print('override rows written: by_ref', len(REF), 'by_gloss', len(GL), '| by_ref total', len(d['by_ref']), '| by_gloss total', len(d['by_gloss']))

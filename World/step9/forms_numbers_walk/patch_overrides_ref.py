#!/usr/bin/env python3
# THE NUMBERS WALK, sitting 15 — THE REFUGE CITIES (2026-09-13): the store's glosses at the chapter's seats read back into the display layer's
# override file — BY REFERENCE for the chapter's own seats and BY GLOSS where the store's every token of the gloss is the one word (the census
# in ref_ink.py: the slayer, the witness, the cubit, the flee-root, suddenly, lying-in-wait, the congregation, and-eight, the pasture-land,
# pollute, the side, thither, unwittingly, the blood family, when-he-meets-him, the refuge family, to-the-land-of, enemy, his-harm, thrust-him,
# threw, anoint, the possession family, your-dwellings, shed, defile, enmity, hatred, their-beasts, wicked, according-to, from-the-avenger,
# without, round-about-them). Display only; the frozen unit untouched. THE ROWS ARE READ FROM ref_ink.py's OWN LITERALS (one source of truth:
# the ink asserts the same rows present after this patch). Run ONCE (the anchors assert the rows absent first). Sitting 14's form.
import ast, os, re, yaml
SP = os.path.dirname(os.path.abspath(__file__))
src = open(f'{SP}/ref_ink.py', encoding='utf-8').read()
tree = ast.parse(src)
LIT = {n.targets[0].id: ast.literal_eval(n.value) for n in tree.body if isinstance(n, ast.Assign) and isinstance(n.targets[0], ast.Name) and n.targets[0].id in ('OVERRIDE_REF', 'OVERRIDE_GLOSS')}
REF, GL = LIT['OVERRIDE_REF'], LIT['OVERRIDE_GLOSS']
NOTE_REF = {'Num.35.4:9': "the cubit — the store glosses 'mother' (the homograph)", 'Num.35.5:15': 'the sea as the direction', 'Num.35.11:0': "the root 'happen' in the causative — the Sifrei: designation", 'Num.35.19:0': 'the avenger of blood — the redeem-root', 'Num.35.21:7': 'the smiter — the same consonants are the smitten woman at 25:14-18', 'Num.35.30:11': "the answer-verb as testify — the store glossed it 'eye'", 'Num.35.31:2': "the ransom — the store's 'cover' is the screen's word too", 'Num.35.33:15': 'the passive: the land shall not be atoned', 'Num.35.27:8': 'the avenger "murders" — the one root for four agents', 'Num.35.16:7': "the doubled infinitive 'die, he shall be put to death'"}
NOTE_GL = {'the-dash-in-pieces': "Strong's rendering of the murder-root; fourteen tokens, every one 'the slayer'", 'concretely': "Strong's 'concretely, a witness' — the witness-noun at all seventeen", 'in-mother': "the cubit at all seventeen (Og's bed's 'by the cubit of a man' too)", 'the-stated-assemblage': 'the congregation at all sixty-five', 'and-cardinal-number': 'the number lost from the gloss — and-eight at all eight', 'mouth-in-a-figurative-sense': "the side-word at all ten (34:3's row by reference stands)", 'there-suffix': 'thither at all seventy-two', 'in-mistake': 'unwittingly at all ten', 'the-blood--of-man': 'the double hyphen family — the blood at all fifty-one', 'be-foul': 'defile at all sixty-four', 'spill-forth': 'shed at all fifteen'}
P = '<repo-old>/logic/glosses/word_gloss_overrides.yaml'
t = open(P, encoding='utf-8').read()
assert '"Num.35.' not in t and '"the-dash-in-pieces": ' not in t and '"concretely": ' not in t
A1 = '  "inherit--mode-of-descent)-you/your": "gives-you-to-inherit"\n'
assert t.count(A1) == 1
gl_block = A1 + '\n  # THE NUMBERS WALK sitting 15 (2026-09-13, Numbers 35): the store\'s glosses whose every token is the one word (censused in the reading\'s ink script) — RESEARCH_LOG.md\n' + ''.join(f'  "{k}": "{v}"' + (f'   # {NOTE_GL[k]}' if k in NOTE_GL else '') + '\n' for k, v in GL)
t = t.replace(A1, gl_block)
A2 = '  "Num.34.13:15": "to-give"\n'
assert t.count(A2) == 1
ref_block = A2 + '  # THE NUMBERS WALK sitting 15 (2026-09-13, Numbers 35): the store\'s glosses at the chapter\'s seats, by reference — RESEARCH_LOG.md\n' + ''.join(f'  "{k}": "{v}"' + (f'   # {NOTE_REF[k]}' if k in NOTE_REF else '') + '\n' for k, v in REF)
t = t.replace(A2, ref_block)
open(P, 'w', encoding='utf-8').write(t)
d = yaml.safe_load(open(P, encoding='utf-8'))
assert all(d['by_ref'][k] == v for k, v in REF) and all(d['by_gloss'][k] == v for k, v in GL)
print('override rows written: by_ref', len(REF), 'by_gloss', len(GL), '| by_ref total', len(d['by_ref']), '| by_gloss total', len(d['by_gloss']))

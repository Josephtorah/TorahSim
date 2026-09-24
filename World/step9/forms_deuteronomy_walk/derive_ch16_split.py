import os as _os
_ROOT = _os.path.normpath(_os.path.join(_os.path.dirname(_os.path.abspath(__file__)), '..', '..', '..'))   # THE PORTABLE REPO (2026-09-15): the repo root from this file's own place
#!/usr/bin/env python3
# THE DEUTERONOMY WALK sitting 14 — CHAPTER 16 (lean, 2026-09-23): split_ch16_spine.py DERIVED from the forms' split_ch15_spine.py by asserted substitutions —
# the spine 127-146 WITH PISKA 135 FOLDED IN (its head row carries no citation — "on the seventh day" is 16:8's; the dump's SPINE skipped it and listed its three
# rows among the outside rows: HEADLESS, in the spine by position), the outside rows three (52:4, 147:2, 281:1); the tails on the consonants — 126's rows do
# not carry 16:1's words (chapter 15's own check), 146's row does not carry 17:1's, 147:1 opens with 17:1's citation. RUN FROM THE REPO ROOT.
import os, re, subprocess
ROOT = _ROOT
SP = os.path.dirname(os.path.abspath(__file__))
src = open(f'{ROOT}/World/step9/forms_deuteronomy_walk/split_ch15_spine.py', encoding='utf-8').read()
lines = src.split('\n'); assert lines[0] == 'import os as _os' and lines[1].startswith('_ROOT = '), lines[:2]
s = '\n'.join(lines[2:])
REPL = [
 ("ROOT = _ROOT", "ROOT = _ROOT"),
 ("# THE DEUTERONOMY WALK sitting 13 — CHAPTER 15: the spine file split by piska for the reading (chapter 14's form, split_ch14_spine.py, WITHOUT a folded tail:\n# piska 110's five rows were all read at chapter 14's sitting and none cites 15:1 in the union; piska 127 heads on 16:1, so 126's rows are checked on their\n# consonants to stop before 16:1's words — sitting 11's lesson 1: a piska's membership is decided on the consonants); the ten outside rows written to their\n# own file. Nothing typed but the piska range read from the dump's print (111-126) and the words of 16:1 and 15:1 the consonant checks look for.",
  "# THE DEUTERONOMY WALK sitting 14 — CHAPTER 16 (LEAN): the spine file split by piska for the reading (chapter 15's form, split_ch15_spine.py): the spine\n# 127-146 WITH PISKA 135 FOLDED IN — its head row carries no citation in the Hebrew (\"on the seventh day\", 16:8's), so the dump's computed SPINE skipped it\n# and listed its three rows among the outside rows; HEADLESS, IN THE SPINE BY POSITION (between 134 on 16:7 and 136 on 16:9). The tails on the consonants:\n# 146's one row does not carry 17:1's words, 147:1 opens with 17:1's citation (sitting 11's lesson 1). The three true outside rows (52:4, 147:2, 281:1) to their own file."),
 ("spine = open(f'{SP}/ch15_sifrei_spine.txt', encoding='utf-8').read()", "spine = open(f'{SP}/ch16_sifrei_spine.txt', encoding='utf-8').read()"),
 ("outside = open(f'{SP}/ch15_sifrei_outside.txt', encoding='utf-8').read()", "outside = open(f'{SP}/ch16_sifrei_outside.txt', encoding='utf-8').read()"),
 ("SPINE = sorted({p for p, _ in rows})\nassert SPINE == list(range(111, 127)), SPINE\n",
  "SPINE = sorted({p for p, _ in rows})\nassert SPINE == [p for p in range(127, 147) if p != 135], SPINE\n# PISKA 135 FOLDED IN from the outside file (HEADLESS): its rows moved from `out` to `rows`\nfor (p, r), d in sorted(out.items()):\n    if p == 135: rows[(p, r)] = ('None', d.get('HE', ''), d.get('EN', '(no EN row)'))\nfor k in [k for k in out if k[0] == 135]: del out[k]\nSPINE = sorted({p for p, _ in rows})\nassert SPINE == list(range(127, 147)), SPINE\n"),
 ("assert sum(len(per[p]) for p in SPINE) == 99, sum(len(per[p]) for p in SPINE)", "assert sum(len(per[p]) for p in SPINE) == 111, sum(len(per[p]) for p in SPINE)"),
 ("# THE TAILS ON THE CONSONANTS: piska 110's last rows do not open 15:1 (read whole at chapter 14 regardless); piska 126's rows do not carry 16:1's words\nP110 = [plain(clean(x)) for x in he[109]]; P126 = [plain(clean(x)) for x in he[125]]; P127 = plain(clean(he[126][0]))\nassert not any('מקץ שבע שנים' in x for x in P110), [x[:80] for x in P110]\nassert not any(w in x for x in P126 for w in ('שמור את חדש האביב', 'חדש האביב')), [x[:80] for x in P126]\nassert 'חדש האביב' in P127, P127[:80]\n",
  "# THE TAILS ON THE CONSONANTS: piska 126's rows do not carry 16:1's words (chapter 15's own check, kept); piska 146's row does not carry 17:1's words; 147:1 opens with 17:1's citation\nP126 = [plain(clean(x)) for x in he[125]]; P146 = [plain(clean(x)) for x in he[145]]; P147 = plain(clean(he[146][0]))\nassert not any(w in x for x in P126 for w in ('שמור את חדש האביב', 'חדש האביב')), [x[:80] for x in P126]\nassert not any(w in x for x in P146 for w in ('לא תזבח ליהוה אלהיך שור ושה', 'שור ושה אשר יהיה בו מום')), [x[:80] for x in P146]\nassert P147.startswith('(דברים יז א) לא תזבח'), P147[:80]\n"),
 ("        f.write(f'--- {p}:{r} (head {h})\\nHE: {he_}\\nEN: {en_}\\n')\nTRUE_OUT = sorted(out)\nassert all(p not in SPINE for p, _ in TRUE_OUT) and len(TRUE_OUT) == 10, TRUE_OUT",
  "        f.write(f'--- {p}:{r} (head {h})\\nHE: {he_}\\nEN: {en_}\\n')\nTRUE_OUT = sorted(out)\nassert all(p not in SPINE for p, _ in TRUE_OUT) and len(TRUE_OUT) == 3 and TRUE_OUT == [(52, 4), (147, 2), (281, 1)], TRUE_OUT"),
 ("print('piska 110 rows (first 70 chars HE):', {(110, i + 1): x[:70] for i, x in enumerate(P110)})\nprint('piska 126 rows (first 70 chars HE):', {(126, i + 1): x[:70] for i, x in enumerate(P126)}, '| 127:1 opens:', P127[:60])",
  "print('piska 135 rows (HEADLESS, folded in; first 90 chars HE):', {(135, r): plain(clean(he[134][r - 1]))[:90] for r in range(1, len(he[134]) + 1)})\nprint('piska 146 rows (first 70 chars HE):', {(146, i + 1): x[:70] for i, x in enumerate(P146)}, '| 147:1 opens:', P147[:60])"),
]
CNT = {"ch15_spine_p{p}.txt": 2}
for old, new in REPL:
    c = s.count(old); assert c == 1, (c, old[:80]); s = s.replace(old, new)
for old, new in (("ch15_spine_p{p}.txt", "ch16_spine_p{p}.txt"), ("ch15_outside_rows.txt", "ch16_outside_rows.txt")):
    c = s.count(old); assert c == 2, (c, old); s = s.replace(old, new)
assert 'ch15' not in s.replace("split_ch15_spine.py", '') and '_ROOT' not in s and '110' not in s, re.findall(r'.{30}(?:ch15|_ROOT|110).{30}', s)
open(f'{SP}/split_ch16_spine.py', 'w', encoding='utf-8').write(s)
import ast; ast.parse(s); print('split_ch16_spine.py derived:', len(s), 'bytes')

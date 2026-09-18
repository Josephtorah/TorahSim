import os as _os
_ROOT = _os.path.normpath(_os.path.join(_os.path.dirname(_os.path.abspath(__file__)), '..', '..', '..'))   # THE PORTABLE REPO (2026-09-15): the repo root from this file's own place
#!/usr/bin/env python3
# THE WHOLE-ROW FIX, part (d) (2026-09-17): the ONE CELL of cold_run_obey_horeb.py typed from a cut row — the ask add_beside (Sanhedrin 89a:2: the cut had
# typed the Gemara's CHALLENGE, 'a fifth placed beside stands alone', as the ruling; the whole row answers by R. Zeira that the fifth spoils either way) —
# retyped from the whole row; the DATA setting, the two move citations and the 4:25 move ('seven verbs') retyped with it. Exact replacements, each once.
import subprocess
ROOT = _ROOT
P = f'{ROOT}/World/step9/cold_run_obey_horeb.py'; s = open(P, encoding='utf-8').read()
R = [
 (r'''a fifth placed beside stands alone; the lulav by the binding''',
  r'''a fifth placed beside as well — R. Zeira: an outer compartment not exposed to the air is unfit, so the fifth spoils either way (89a:2; retyped 2026-09-17 from the whole row); the lulav by the binding'''),
 (r'''five compartments made as one (liable), a fifth beside (stands alone); the lulav by the binding, the fringes by the upper knot''',
  r'''five compartments made as one, and a fifth placed beside as well — R. Zeira (89a:2): the outer compartment must meet the air, so the fifth spoils either way; the lulav by the binding, the fringes by the upper knot'''),
 (r'''a fifth compartment PLACED BESIDE four made: the four stand alone (Sanhedrin 89a:2); the lulav\'s added species without binding, the fringes\' added thread without the Torah knot''',
  r'''a fifth compartment PLACED BESIDE four made: the challenge says the four stand alone and the fifth stands alone; R. ZEIRA ANSWERS — an outer compartment not exposed to the air makes the head tefillin unfit, so the fifth spoils placed beside as it does made as one (Sanhedrin 89a:2; RETYPED 2026-09-17 from the whole row — the cut had typed the challenge as the ruling); what stands alone is the lulav\'s added species where no binding is required and the fringes\' added thread where no knot is (88b:17-89a:1)'''),
 (r'''"the elder liable only where the addition SPOILS — beside it stands alone: the Mishnah 11:3's row resolved"''',
  r'''"the elder liable only where the addition SPOILS — the fifth compartment spoils beside the four as it does among them (R. Zeira); only the unbound species stands alone: the Mishnah 11:3's row resolved"'''),
 (r'''out("an addition placed beside (Sanhedrin 89a) — the four compartments stand alone: no spoiling, exempt", ['exempt'])''',
  r'''out("an addition placed beside (Sanhedrin 89a:2) — R. Zeira: the fifth compartment spoils the four even beside them; the transgression stands: accepted", ['accepted'])'''),
 (r''''an addition placed beside (Sanhedrin 89a) — the four compartments stand alone: no spoiling, exempt')''',
  r'''"an addition placed beside (Sanhedrin 89a:2) — R. Zeira: the fifth compartment spoils the four even beside them; the transgression stands: accepted")'''),
 (r'''n('the-fifth-beside', 'exempt')''', r'''n('the-fifth-beside', 'accepted')'''),
 (r'''every exam person written once; the five exempt arms ONE each; no timer;''',
  r'''every exam person written once; the four exempt arms ONE each and the fifth compartment ACCEPTED (retyped 2026-09-17 from the whole row); no timer;'''),
 (r'''seven dynasties from the seven verbs; the Ninth of Av's reading''',
  r'''seven dynasties counted from 'you will beget' (one) and 'children' said thrice (two each); the Ninth of Av's reading'''),
]
for old, new in R:
    assert s.count(old) == 1, ('not once', s.count(old), old[:60]); s = s.replace(old, new)
open(P, 'w', encoding='utf-8').write(s); print('RETYPED', P, len(R), 'replacements')

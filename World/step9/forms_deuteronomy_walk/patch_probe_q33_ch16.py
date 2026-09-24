import os as _os
_ROOT = _os.path.normpath(_os.path.join(_os.path.dirname(_os.path.abspath(__file__)), '..', '..', '..'))   # THE PORTABLE REPO (2026-09-15): the repo root from this file's own place
#!/usr/bin/env python3
# THE DEUTERONOMY WALK 14b (LEAN): Q33 RETYPED FROM THE CHAIN'S PRINT (ch16b_gates_first/probe_readback.out — 42/43): chapter 12's readback probe scans Israel's
# effects for its seven holes by substring and matched chapter 16's passover_in_the_gates_barred through 'in_the_gates' — the fifth seat of the sitting's lesson
# (DD4 on the tape the same scan). Chapter 16's block excluded with the note; the expected tuple unmoved. Idempotent. RUN FROM THE REPO ROOT.
import subprocess
ROOT = _ROOT
P = ROOT + '/World/step9/readback_probes.py'
s = open(P, encoding='utf-8').read()
old = "    holes = sorted({e['effect'] for e in (isr.ledger if isr else []) if any(t in e['effect'] for t in ('place_chosen', 'rejoicing_before', 'profane_slaughter', 'in_the_gates', 'levite_forsaking', 'name_erasure', 'foreign_rite'))})\n    fx = _y.safe_load(open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'effect_vocabulary.yaml'), encoding='utf-8'))['effects']\n    vocab7 = all(k in fx for k in OWN7)\n    eras = PN.DATA['the_eras_table_unmoved']['value']"
assert s.count(old) == 1, s.count(old)
new = "    holes = sorted({e['effect'] for e in (isr.ledger if isr else []) if any(t in e['effect'] for t in ('place_chosen', 'rejoicing_before', 'profane_slaughter', 'in_the_gates', 'levite_forsaking', 'name_erasure', 'foreign_rite')) and e['effect'] != 'passover_in_the_gates_barred'})   # THE DEUTERONOMY WALK 14b (2026-09-23; LEAN): chapter 16's own block at 16:5, its name carrying 'in_the_gates', excluded — the later chapter's write moved this scan (the chain's first pass 42/43; DD4 on the tape the same seat; retyped from the print)\n    fx = _y.safe_load(open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'effect_vocabulary.yaml'), encoding='utf-8'))['effects']\n    vocab7 = all(k in fx for k in OWN7)\n    eras = PN.DATA['the_eras_table_unmoved']['value']"
s = s.replace(old, new)
open(P, 'w', encoding='utf-8').write(s)
import py_compile; py_compile.compile(P, doraise=True); print('Q33 retyped: chapter 16\'s block excluded from chapter 12\'s hole probe; the file compiles')

import os as _os
_ROOT = _os.path.normpath(_os.path.join(_os.path.dirname(_os.path.abspath(__file__)), '..', '..', '..'))   # THE PORTABLE REPO (2026-09-15): the repo root from this file's own place
#!/usr/bin/env python3
# THE DEUTERONOMY WALK 22b (2026-09-30; LEAN): DP4's declared class for the receipt 34:9 RETYPED in the sequence file from the register file AFTER the gate's second print (the gate run alone
# over the tape that carries chapter 34 — the first run alone, before the stitcher, saw no line at 34:9 and held NONE: 22b's find — the receipt class is computed from the REPLAYED TAPE, so the
# gate decides only after the stitcher). The declared literal in DP4 (typed by patch_seq_literals_ch34.py from the file as it then stood) replaced by the file's class now; the label retyped.
# RUN FROM THE REPO ROOT.
import re, subprocess, yaml, py_compile
ROOT = _ROOT
P = ROOT + '/World/step9/cold_run_sequence.py'
s = open(P, encoding='utf-8').read()
RG = yaml.safe_load(open(ROOT + '/World/step9/register_dispositions.yaml', encoding='utf-8')); CLS = RG['receipts']['Deut 34:9']['class']
m = re.search(r"THE RECEIPT 34:9 RE-DECLARED — the register file\\'s class ([A-Z\-]+) AS THE GATE (?:HOLDS|COMPUTES) IT \([^)]*\)', \(12, (\d+), (\d+), (\d+), \[\], \['Deut 34:4', 'Deut 34:5', 'Deut 34:6'\], 0, 0, '([A-Z\-]+)'\), \(len\(RB_cp\)", s)
assert m, 'the DP4 line as patch_seq_literals_ch34.py wrote it'
OLD_CLS = m.group(5); assert m.group(1) == OLD_CLS
new = re.sub(r"class [A-Z\-]+ AS THE GATE (?:HOLDS|COMPUTES) IT \([^)]*\)", "class %s AS THE GATE COMPUTES IT (its print after the stitcher — the tape carrying chapter 34; the first print before the stitcher held NONE)" % CLS, m.group(0)).replace("0, 0, '%s'), (len(RB_cp)" % OLD_CLS, "0, 0, '%s'), (len(RB_cp)" % CLS)
s = s.replace(m.group(0), new); open(P, 'w', encoding='utf-8').write(s); py_compile.compile(P, doraise=True)
print('DP4 retyped: the declared class %s -> %s (the register file after the gate\'s second print); compiles' % (OLD_CLS, CLS))

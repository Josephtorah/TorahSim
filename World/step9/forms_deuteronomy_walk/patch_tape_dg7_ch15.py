import os as _os
_ROOT = _os.path.normpath(_os.path.join(_os.path.dirname(_os.path.abspath(__file__)), '..', '..', '..'))   # THE PORTABLE REPO (2026-09-15): the repo root from this file's own place
#!/usr/bin/env python3
# THE DEUTERONOMY WALK 13b THE TAIL (2026-09-23): the chain's third pass — the tape's DG7 DIVERGE after the tail's own filing: DG7 counts the CALL edges from
# release_firstborn on file (twenty-one at the tape's first run); the dependency gate's first pass made mishpatim's edge PARAMETER (the F1 TABLE read — no call the gate
# can see), so the CALL rows are TWENTY. The literal retyped from the yaml's own count (computed here with the checkpoint's own expression, asserted before the write),
# the text amended; the transfer count and the homograph flags unmoved. RUN FROM THE REPO ROOT.
import subprocess, os, yaml, py_compile
ROOT = _ROOT
SEQ = ROOT + '/World/step9/cold_run_sequence.py'
dep = yaml.safe_load(open(ROOT + '/World/step9/dependency_dispositions.yaml', encoding='utf-8'))
calls = sum(1 for e in dep['edges'] if e.get('from') == 'release_firstborn' and e.get('disposition') == 'CALL')
transfers = sum(1 for e in dep['edges'] if e.get('from') == 'release_firstborn' and e.get('link') == 'transfer')
refs = sum(1 for e in dep['edges'] if e.get('from') == 'release_firstborn' and e.get('disposition') == 'CALL' and e.get('link') == 'reference')
ptr = sum(1 for p in dep['pointers'] if p.get('runner') == 'release_firstborn')
assert (calls, transfers, refs, ptr) == (20, 2, 18, 1), (calls, transfers, refs, ptr)
s = open(SEQ, encoding='utf-8').read()
OLD_T = "the CALL edges from release_firstborn on file — nineteen REFERENCE and TWO TRANSFER labeled with their teachers (seducers: the Sifrei 117:3; metzora: the Sifrei 122:5-6 and Kiddushin 15a) — the census decides the rest; no pointer from release_firstborn at the tape\\'s first run;"
NEW_T = ("the CALL edges from release_firstborn on file TWENTY since the tail (twenty-one at the tape\\'s first run: mishpatim\\'s F1 read as a TABLE, no call the gate can see — PARAMETER at the chain\\'s first pass; RETYPED FROM THE YAML\\'S OWN COUNT after the third pass\\'s DIVERGE) — eighteen REFERENCE and TWO TRANSFER labeled with their teachers "
         "(seducers: the Sifrei 117:3; metzora: the Sifrei 122:5-6 and Kiddushin 15a) — the census decides the rest (its two homograph rows FALSE and VIA, its pointer Deut 15:6 OWED filed at the tail);")
OLD_V = "(True, 21, 2, 0, (True, True, True, True)), ('Deut 12:1' not in rg_rf"
NEW_V = "(True, 20, 2, 0, (True, True, True, True)), ('Deut 12:1' not in rg_rf"
assert s.count(OLD_T) == 1 and s.count(OLD_V) == 1, (s.count(OLD_T), s.count(OLD_V))
s = s.replace(OLD_T, NEW_T).replace(OLD_V, NEW_V); open(SEQ, 'w', encoding='utf-8').write(s); py_compile.compile(SEQ, doraise=True)
print('DG7 retyped: the CALL edges 21 -> %d (reference %d, transfer %d; pointers from release_firstborn %d) — computed from dependency_dispositions.yaml' % (calls, refs, transfers, ptr))

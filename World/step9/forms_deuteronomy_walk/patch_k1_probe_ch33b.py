import os as _os
_ROOT = _os.path.normpath(_os.path.join(_os.path.dirname(_os.path.abspath(__file__)), '..', '..', '..'))   # THE PORTABLE REPO (2026-09-15): the repo root from this file's own place
#!/usr/bin/env python3
# THE DEUTERONOMY WALK 21b TAIL (2026-09-29): checkpoint_probes.beyond_the_tape() read the tape's case sources by ONE regex form — 'case_source': '(Book) c:v — and a case source whose
# text carries an apostrophe (the blessing's frame) is written into the tape literal by repr with DOUBLE quotes; every chapter 33 line is such a source, so the probe took the last
# verse as Deut 32's, run_to stopped at the left edge of Deut 33:1, the eleven lines never ran and DO1, DO2 and DO5 DIVERGED in K1's world (the positions' finals MATCH; the diagnostic
# ch33b_k1_diag.out). THE FIX: either quote. One exact-text edit with a dated comment; the probe file compiles; the new regex checked on the tape's own text. RUN FROM THE REPO ROOT.
import re, subprocess
ROOT = _ROOT
P = f'{ROOT}/World/step9/checkpoint_probes.py'; t = open(P, encoding='utf-8').read()
old = """    refs = _re.findall(r"'case_source': '(Gen|Exod|Lev|Num|Deut) (\\d+):(\\d+)", tape)\n"""
new = """    refs = _re.findall(r"'case_source': ['\\"](Gen|Exod|Lev|Num|Deut) (\\d+):(\\d+)", tape)   # THE DEUTERONOMY WALK 21b (2026-09-29): EITHER QUOTE — a case source whose text carries an apostrophe (the blessing's frame) sits in the tape literal in double quotes by repr; the single-quote form read chapter 33's eleven lines as absent, stopped run_to at 33:1 and DO1, DO2, DO5 diverged in K1's world (the positions' finals MATCH)\n"""
assert t.count(old) == 1, t.count(old)
t2 = t.replace(old, new); open(P, 'w', encoding='utf-8').write(t2)
compile(t2, P, 'exec')
s = open(f'{ROOT}/World/step9/cold_run_sequence.py', encoding='utf-8').read(); tape = s[s.find('# ==== TAPE BEGIN'):s.find('# ==== TAPE END ====')]
order = ['Gen', 'Exod', 'Lev', 'Num', 'Deut']
old_refs = re.findall(r"'case_source': '(Gen|Exod|Lev|Num|Deut) (\d+):(\d+)", tape); new_refs = re.findall(r"'case_source': ['\"](Gen|Exod|Lev|Num|Deut) (\d+):(\d+)", tape)
last_old = max(old_refs, key=lambda r: (order.index(r[0]), int(r[1]), int(r[2]))); last_new = max(new_refs, key=lambda r: (order.index(r[0]), int(r[1]), int(r[2])))
print('patched checkpoint_probes.py: the tape refs by the old form %d (last %s %s:%s), by the new form %d (last %s %s:%s); the file compiles' % (len(old_refs), *last_old, len(new_refs), *last_new))
assert last_new == ('Deut', '33', '28') and last_old[1] == '32', (last_old, last_new)

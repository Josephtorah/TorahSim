import os as _os
_ROOT = _os.path.normpath(_os.path.join(_os.path.dirname(_os.path.abspath(__file__)), '..', '..', '..'))   # THE PORTABLE REPO (2026-09-15): the repo root from this file's own place
#!/usr/bin/env python3
# THE DEUTERONOMY WALK 8b (2026-09-20): two retypes from the prints — (1) THE DESIGN'S opening_speech EDGE DROPPED at the callees' print (6b's lesson): the
# opening-speech runner holds NO cell on 1:10's 'as the stars of heaven for multitude' (no 'stars', no 'ככוכבי', no '1:10' in its source — ch10_callees.out),
# so the runner does not import it and the readback row 10:22 rests on the Joseph runner alone (1:10's phrase a DATA row by the ink): the CALL edge
# removed from dependency_dispositions.yaml (18 -> 17 CALL edges; the census decides the rest at the gate); (2) Q25's STRETCH RESOLVER extended: the
# third forty's end is the TIMERS' FIRE at (1, 7, 10) (the second ascent's line sets tablets_delivered and face_radiant), not a marker — the runner's
# stretch names 'timer:tablets_delivered' and the probe resolves it through the running world's TIMER-FIRE log (the marker verse form kept for 7b's rows).
import subprocess, yaml
ROOT = _ROOT
# (1) the edge
P = ROOT + '/World/step9/dependency_dispositions.yaml'
s = open(P, encoding='utf-8').read()
a = "  - {from: second_tablets, to: opening_speech, disposition: CALL, link: reference, carries: verdict,"
if a in s:
    i = s.index(a); j = s.index('\n', s.index('why:', i)) + 1
    s = s[:i] + s[j:]
    open(P, 'w', encoding='utf-8').write(s)
dep = yaml.safe_load(open(P, encoding='utf-8'))
n_ch = sum(1 for e in dep['edges'] if e['from'] == 'second_tablets'); assert n_ch == 17, n_ch
assert not any(e['from'] == 'second_tablets' and e['to'] == 'opening_speech' for e in dep['edges'])
print('dependency: the opening_speech edge dropped at the callees\' print — second_tablets 17 CALL edges')
# (2) the probe's resolver
P = ROOT + '/World/step9/readback_probes.py'
s = open(P, encoding='utf-8').read()
old = "    st_ok = bool(st) and all(r['stretch']['from'] in mk and r['stretch']['to'] in mk and mk[r['stretch']['to']][1] - mk[r['stretch']['from']][1] == r['stretch']['days'] for r in st)\n    ok = len(rows) == 25"
assert s.count(old) == 1, s.count(old)
new = "    def END(name):   # a stretch's end — a marker's verse, or 'timer:<effect>' the first TIMER-FIRE of that effect on the running world (the third forty ends at the timers' fire (1, 7, 10), not a marker)\n        if name in mk: return mk[name][1]\n        if name.startswith('timer:'):\n            f = [l for l in W.log if l[0] == 'TIMER-FIRE' and l[2].get('effect') == name[6:]]\n            return f[0][1] if f else None\n        return None\n    st_ok = bool(st) and all(r['stretch']['from'] in mk and END(r['stretch']['to']) is not None and END(r['stretch']['to']) - mk[r['stretch']['from']][1] == r['stretch']['days'] for r in st)\n    ok = len(rows) == 25"
s = s.replace(old, new)
open(P, 'w', encoding='utf-8').write(s)
import py_compile; py_compile.compile(P, doraise=True)
print('readback_probes.py: Q25\'s stretch resolver takes a timer\'s fire; compiles')

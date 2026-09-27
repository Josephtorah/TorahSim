import os as _os
_ROOT = _os.path.normpath(_os.path.join(_os.path.dirname(_os.path.abspath(__file__)), '..', '..', '..'))   # THE PORTABLE REPO (2026-09-15): the repo root from this file's own place
#!/usr/bin/env python3
# THE DEUTERONOMY WALK 15b (LEAN): THE REGISTRATION EDGE FILED FROM THE GATE'S PRINT (ch17b_dependency_after.out — 'LIVE EDGE sequence -> courts_prophet has NO ENTRY
# on file'): the sequential run's ('cold_run_courts_prophet', 'law_courts_prophet') tuple in DAEMON_ORDER — link none, O4's license (14b's form). Idempotent. RUN FROM THE REPO ROOT.
import subprocess, yaml
ROOT = _ROOT
P = ROOT + '/World/step9/dependency_dispositions.yaml'
s = open(P, encoding='utf-8').read()
if '{from: sequence, to: courts_prophet, disposition: CALL' not in s:
    edge = "  - {from: sequence, to: courts_prophet, disposition: CALL, link: none,\n     why: \"THE DEUTERONOMY WALK 15b (2026-09-24; LEAN) | the sequential run's REGISTRATION edge — ('cold_run_courts_prophet', 'law_courts_prophet') in DAEMON_ORDER (the runner compiles no verse: link none, O4's license); EIGHT OWN-DAY lines this sitting after the tape's last Deuteronomy 16 line, NO marker — blemished_sacrifice_barred (17:1), idolater_trial_declared (17:2-7), high_court_declared (17:8-13), king_law_declared (17:14-20), priests_dues_declared (18:1-5), levite_at_the_place_declared (18:6-8), diviners_barred (18:9-14), prophet_law_declared (18:15-22); thirty-seven writes on Israel, every one its first entry; the edge filed from the gate's own print before the chain (rule 9 — the file may not understate the code)\"}\n"
    a = "  - {from: sequence, to: festivals_judges, disposition: CALL, link: none,"
    i = s.index(a); j = s.index('\n', s.index('why:', i)) + 1
    s = s[:j] + edge + s[j:]
    open(P, 'w', encoding='utf-8').write(s)
d = yaml.safe_load(open(P, encoding='utf-8'))
assert any(e.get('from') == 'sequence' and e.get('to') == 'courts_prophet' and e.get('disposition') == 'CALL' for e in d['edges'])
print('filed: the registration edge sequence -> courts_prophet (link none); edges %d, pointers %d' % (len(d['edges']), len(d['pointers'])))

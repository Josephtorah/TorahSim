import os as _os
_ROOT = _os.path.normpath(_os.path.join(_os.path.dirname(_os.path.abspath(__file__)), '..', '..', '..'))   # THE PORTABLE REPO (2026-09-15): the repo root from this file's own place
#!/usr/bin/env python3
# THE DEUTERONOMY WALK 14b (LEAN): THE REGISTRATION EDGE FILED FROM THE CHAIN'S PRINT (ch16b_gates/dependency.out — 'LIVE EDGE sequence -> festivals_judges has NO ENTRY
# on file'): the sequential run's ('cold_run_festivals_judges', 'law_festivals_judges') tuple in DAEMON_ORDER — link none, O4's license (13b's form). Idempotent. RUN FROM THE REPO ROOT.
import subprocess, yaml
ROOT = _ROOT
P = ROOT + '/World/step9/dependency_dispositions.yaml'
s = open(P, encoding='utf-8').read()
if '{from: sequence, to: festivals_judges, disposition: CALL' not in s:
    edge = "  - {from: sequence, to: festivals_judges, disposition: CALL, link: none,\n     why: \"THE DEUTERONOMY WALK 14b (2026-09-23; LEAN) | the sequential run's REGISTRATION edge — ('cold_run_festivals_judges', 'law_festivals_judges') in DAEMON_ORDER (the runner compiles no verse: link none, O4's license); FIVE OWN-DAY lines this sitting after the tape's last Deuteronomy 15 line, NO marker — passover_at_the_place_declared (16:1-8; two STATUSES, three BLOCKS), weeks_and_booths_declared (16:9-15; two STATUSES), three_pilgrimages_declared (16:16-17; a STATUS, a BLOCK), judges_in_every_gate_commanded (16:18-20; two STATUSES, two BLOCKS, bribe_barred REUSED — its first entry anywhere), asherah_and_pillar_barred (16:21-22; two BLOCKS); the edge filed at the tail from the chain's own print (rule 9 — the file may not understate the code)\"}\n"
    a = "  - {from: sequence, to: release_firstborn, disposition: CALL, link: none,"
    i = s.index(a); j = s.index('\n', s.index('why:', i)) + 1
    s = s[:j] + edge + s[j:]
    open(P, 'w', encoding='utf-8').write(s)
d = yaml.safe_load(open(P, encoding='utf-8'))
assert any(e.get('from') == 'sequence' and e.get('to') == 'festivals_judges' and e.get('disposition') == 'CALL' for e in d['edges'])
print('filed: the registration edge sequence -> festivals_judges (link none); edges %d, pointers %d' % (len(d['edges']), len(d['pointers'])))

import os as _os
_ROOT = _os.path.normpath(_os.path.join(_os.path.dirname(_os.path.abspath(__file__)), '..', '..', '..'))   # THE PORTABLE REPO (2026-09-15): the repo root from this file's own place
#!/usr/bin/env python3
# THE DEUTERONOMY WALK sitting 4b, RUN 4 (2026-09-17): two probes retyped from the chain's print — (1) readback_probes Q13 looked for a 'found' key the
# runner's rows never carry; the row's tape entry is FOUND ON THE RUNNING WORLD by kind and first verse, as Q2 and the tape's CO4 compute it;
# (2) large_letter_probes H5 asserted 6:4 had NO tape line (the hypothesis's exhibit at sitting 4) — the compile put the Shema's statute line there:
# the exhibit retyped to the new state (a line at 6:4, still no register seat, the large-letter edge still unfiled — PARKED). Exact replacements, asserted.
import subprocess, re
ROOT = _ROOT
def patch(path, pairs):
    p = f'{ROOT}/{path}'; s = open(p, encoding='utf-8').read()
    for old, new in pairs:
        assert s.count(old) == 1, (path, s.count(old), old[:80]); s = s.replace(old, new)
    open(p, 'w', encoding='utf-8').write(s); print('patched', path, len(pairs))

Q13_OLD = """    found = sum(1 for r in rows if r.get('found'))
    ok = len(rows) == 7 and found == 7 and gs == collections.Counter({'VERBATIM': 3, 'EXPANDED': 3, 'SHORTENED': 1}) and not any(r.get('open') for r in rows)
    return ok, 'rows %d (found %d), grades %s, open %d' % (len(rows), found, dict(gs), sum(1 for r in rows if r.get('open')))"""
Q13_NEW = """    found = sum(1 for r in rows if any(e[2]['kind'] == r['tape_kind'] and WE.first_verse(e[2].get('case_source')) == WE.first_verse(r['tape_verse']) for e in EV))   # FOUND ON THE RUNNING WORLD (Q2's form; the tape's CO4) — RUN 4's retype: the rows carry no 'found' key
    law = sum(1 for r in rows if r.get('law'))
    ok = len(rows) == 7 and found == 7 and law == 7 and gs == collections.Counter({'VERBATIM': 3, 'EXPANDED': 3, 'SHORTENED': 1}) and not any(r.get('open') for r in rows)
    return ok, 'rows %d (found on the running world %d, every row a law\\'s %d), grades %s, open %d' % (len(rows), found, law, dict(gs), sum(1 for r in rows if r.get('open')))"""
Q13_DOC_OLD = "  Q13 chapter 6's table — THE READBACK'S THIRD FORM (a retelling inside a law): seven rows — the son's answer's five (6:21-25), the header's (6:1), the test's (6:16) — every row's tape entry FOUND, the grades VERBATIM 3 / EXPANDED 3 / SHORTENED 1, no row OPEN"
Q13_DOC_NEW = "  Q13 chapter 6's table — THE READBACK'S THIRD FORM (a retelling inside a law): seven rows — the son's answer's five (6:21-25), the header's (6:1), the test's (6:16) — every row a law's, every row's tape entry FOUND on the running world by kind and first verse (Q2's form), the grades VERBATIM 3 / EXPANDED 3 / SHORTENED 1, no row OPEN"
patch('World/step9/readback_probes.py', [(Q13_OLD, Q13_NEW), (Q13_DOC_OLD, Q13_DOC_NEW)])

H5_OLD = '''def h5_the_creed():
    """H5 — Deuteronomy 6:4 has NO machine class yet (no tape line, no register seat): the "witness" reading is the hypothesis, OPEN until the compile files its edge"""
    n = len(_lines_at('Deut 6:4'))
    RI = open(f'{_ROOT}/World/step9/REGISTER_INDEX.md', encoding='utf-8').read()
    H('H5 the creed unclassed (OPEN)', n == 0 and not re.search(r'Deut 6:4\\b', RI), f'tape lines at 6:4: {n}; register lines: {bool(re.search(r"Deut 6:4", RI))}')'''
H5_NEW = '''def h5_the_creed():
    """H5 — Deuteronomy 6:4 CLASSED by the compile (THE DEUTERONOMY WALK 4b, 2026-09-17: shema_declared the STATUTE line at 6:4-9, the daemon's write beside it) — still NO register seat at 6:4;
    the large-letter reading itself stays a PARKED hypothesis: no edge `link: hypothesis` at 6:4 in the dispositions. (At sitting 4 this probe asserted NO tape line — the exhibit moved when the compile filed the line; retyped from the chain's print at RUN 4.)"""
    rows = _lines_at('Deut 6:4'); n = len(rows); classes = sorted({k for _, k, _ in rows})
    RI = open(f'{_ROOT}/World/step9/REGISTER_INDEX.md', encoding='utf-8').read()
    DD = open(f'{_ROOT}/World/step9/dependency_dispositions.yaml', encoding='utf-8').read()
    hyp = bool(re.search(r'link: hypothesis[^\\n]*6:4|6:4[^\\n]*link: hypothesis', DD))
    H('H5 the creed classed by the compile, the hypothesis parked', n > 0 and any('shema_declared' in d for _, _, d in rows) and 'run.event' in classes and not re.search(r'Deut 6:4\\b', RI) and not hyp,
      f'tape lines at 6:4: {n}, classes {classes}, shema_declared present: {any("shema_declared" in d for _, _, d in rows)}; register lines: {bool(re.search(r"Deut 6:4", RI))}; a hypothesis edge at 6:4: {hyp}')'''
patch('World/step9/large_letter_probes.py', [(H5_OLD, H5_NEW)])
print('the two probes retyped')

import os as _os
_ROOT = _os.path.normpath(_os.path.join(_os.path.dirname(_os.path.abspath(__file__)), '..', '..', '..'))   # THE PORTABLE REPO (2026-09-15): the repo root from this file's own place
#!/usr/bin/env python3
# THE DEUTERONOMY WALK 15b (2026-09-24): the recorder seq_record_ch17.py and the stitcher seq_stitch_ch17.py DERIVED from 14b's copies in the forms folder by
# asserted substitutions — the portable header made a scratch script's (ROOT from git, run from the repo root); the stitcher's chapter note: 15b's EIGHT own-day lines
# over two chapters, NO marker, appended after 14b's; nothing else moves. derive_ch16_seq_tools.py's form. RUN FROM THE REPO ROOT.
import subprocess, os
ROOT = _ROOT
SP = os.path.dirname(os.path.abspath(__file__))
FD = f'{ROOT}/World/step9/forms_deuteronomy_walk'
HEAD = "import os as _os, subprocess as _sp\n_ROOT = _sp.check_output(['git', 'rev-parse', '--show-toplevel'], text=True).strip()   # THE DEUTERONOMY WALK 15b (2026-09-24): a scratch script — the repo root from git, run from the repo root (the forms copy computes it from its own place)\n"
def fix_head(src, name):
    lines = src.split('\n')
    i = [k for k, l in enumerate(lines) if l.startswith('_ROOT = _os.path.normpath(')]
    assert len(i) == 1, (name, i)
    i = i[0]; assert i <= 2, (name, i)
    pre = [l for l in lines[:i] if l.strip() and not l.startswith('import subprocess as _sp') and not l.startswith('import os as _os')]
    assert pre == [], (name, pre)
    return HEAD + '\n'.join(lines[i + 1:])
rec = open(f'{FD}/seq_record_ch16.py', encoding='utf-8').read()
rec = fix_head(rec, 'seq_record')
assert rec.count("HERE = (_ROOT + '/World/step9')") == 1
open(f'{SP}/seq_record_ch17.py', 'w', encoding='utf-8').write(rec)
st = open(f'{FD}/seq_stitch_ch16.py', encoding='utf-8').read()
st = fix_head(st, 'seq_stitch')
assert st.count("HERE = (_ROOT + '/World/step9')") == 1 and st.count("SCR = os.path.dirname(os.path.abspath(__file__))") == 1
anchor = "# you out' a clause inside the law) — no retrograde marker; the markers' list above 13b's exactly (172)\n"
assert st.count(anchor) == 1, st.count(anchor)
NOTE = anchor + "# THE DEUTERONOMY WALK 15b (2026-09-24; DEUTERONOMY_WALK.md \"Sitting 15b\" THE LEAN DESIGN): NO MARKER — chapters 17-18's EIGHT lines (blemished_sacrifice_barred 17:1,\n# idolater_trial_declared 17:2-7, high_court_declared 17:8-13, king_law_declared 17:14-20, priests_dues_declared 18:1-5, levite_at_the_place_declared 18:6-8, diviners_barred 18:9-14,\n# prophet_law_declared 18:15-22) are OWN-DAY lines at the counter's (40, 11, 1), STATUTE by form, joined after the tape's last Deuteronomy 16 line by the sort (page_order); no\n# narrative verb in either chapter (18:16-17 retell Horeb's request — REFERENCE rows against the tape's own Deuteronomy 5 lines) — no retrograde marker; the markers' list above 14b's exactly (172)\n"
st = st.replace(anchor, NOTE)
open(f'{SP}/seq_stitch_ch17.py', 'w', encoding='utf-8').write(st)
import py_compile
py_compile.compile(f'{SP}/seq_record_ch17.py', doraise=True); py_compile.compile(f'{SP}/seq_stitch_ch17.py', doraise=True)
print('derived: seq_record_ch17.py %d bytes, seq_stitch_ch17.py %d bytes (the header from git; the 15b note after the 14b note); both compile' % (len(rec), len(st)))

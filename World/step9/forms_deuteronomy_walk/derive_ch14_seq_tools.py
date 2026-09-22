#!/usr/bin/env python3
# THE DEUTERONOMY WALK 12b (2026-09-22): the recorder seq_record_ch14.py and the stitcher seq_stitch_ch14.py DERIVED from 11b's copies in the forms folder
# by asserted substitutions — the portable header (a forms-folder _ROOT from __file__) made a scratch script's (ROOT from git, run from the repo root); the
# stitcher's chapter note: 12b's FIVE own-day lines, NO marker, appended after 11b's; nothing else moves. derive_ch13_seq_tools.py's form. RUN FROM THE REPO ROOT.
import subprocess, os
ROOT = _ROOT
SP = os.path.dirname(os.path.abspath(__file__))
FD = f'{ROOT}/World/step9/forms_deuteronomy_walk'
HEAD = "import os as _os, subprocess as _sp\n_ROOT = _ROOT   # THE DEUTERONOMY WALK 12b (2026-09-22): a scratch script — the repo root from git, run from the repo root (the forms copy computes it from its own place)\n"
def fix_head(src, name):
    lines = src.split('\n')
    i = [k for k, l in enumerate(lines) if l.startswith('_ROOT = _os.path.normpath(')]
    assert len(i) == 1, (name, i)
    i = i[0]; assert i <= 2, (name, i)
    pre = [l for l in lines[:i] if l.strip() and not l.startswith('import subprocess as _sp') and not l.startswith('import os as _os')]
    assert pre == [], (name, pre)
    return HEAD + '\n'.join(lines[i + 1:])
rec = open(f'{FD}/seq_record_ch13.py', encoding='utf-8').read()
rec = fix_head(rec, 'seq_record')
assert rec.count("HERE = (_ROOT + '/World/step9')") == 1
open(f'{SP}/seq_record_ch14.py', 'w', encoding='utf-8').write(rec)
st = open(f'{FD}/seq_stitch_ch13.py', encoding='utf-8').read()
st = fix_head(st, 'seq_stitch')
assert st.count("HERE = (_ROOT + '/World/step9')") == 1 and st.count("SCR = os.path.dirname(os.path.abspath(__file__))") == 1
anchor = "# markers' list above 10b's exactly (172)\n"
assert st.count(anchor) == 1, st.count(anchor)
NOTE = anchor + "# THE DEUTERONOMY WALK 12b (2026-09-22; DEUTERONOMY_WALK.md \"Sitting 12b\" THE LINES ON THE TAPE): NO MARKER — chapter 14's FIVE lines (sons_and_mourning_declared 14:1-2,\n# food_law_declared 14:3-20, carcass_and_kid_declared 14:21, second_tithe_declared 14:22-27, third_year_tithe_declared 14:28-29) are OWN-DAY lines at the counter's\n# (40, 11, 1), STATUTE by form, joined after the tape's last Deuteronomy 13 line by the sort (page_order); no act told only here (the kin's lines measured at the design)\n# — no retrograde marker; the markers' list above 11b's exactly (172)\n"
st = st.replace(anchor, NOTE)
open(f'{SP}/seq_stitch_ch14.py', 'w', encoding='utf-8').write(st)
import py_compile
py_compile.compile(f'{SP}/seq_record_ch14.py', doraise=True); py_compile.compile(f'{SP}/seq_stitch_ch14.py', doraise=True)
print('derived: seq_record_ch14.py %d bytes, seq_stitch_ch14.py %d bytes (the header from git; the 12b note after the 11b note); both compile' % (len(rec), len(st)))

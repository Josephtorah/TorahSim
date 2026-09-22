#!/usr/bin/env python3
# THE DEUTERONOMY WALK 11b (2026-09-21): the recorder seq_record_ch13.py and the stitcher seq_stitch_ch13.py DERIVED from 10b's copies in the forms folder
# by asserted substitutions — the portable header (a forms-folder _ROOT from __file__) made a scratch script's (ROOT from git, run from the repo root); the
# stitcher's chapter note: 11b's FOUR own-day lines, NO marker, appended after 10b's; nothing else moves. derive_ch12_seq_tools.py's form. RUN FROM THE REPO ROOT.
import subprocess, os
ROOT = _ROOT
SP = os.path.dirname(os.path.abspath(__file__))
FD = f'{ROOT}/World/step9/forms_deuteronomy_walk'
HEAD = "import os as _os, subprocess as _sp\n_ROOT = _ROOT   # THE DEUTERONOMY WALK 11b (2026-09-21): a scratch script — the repo root from git, run from the repo root (the forms copy computes it from its own place)\n"
def fix_head(src, name):
    lines = src.split('\n')
    i = [k for k, l in enumerate(lines) if l.startswith('_ROOT = _os.path.normpath(')]
    assert len(i) == 1, (name, i)
    i = i[0]; assert i <= 2, (name, i)
    pre = [l for l in lines[:i] if l.strip() and not l.startswith('import subprocess as _sp') and not l.startswith('import os as _os')]
    assert pre == [], (name, pre)
    return HEAD + '\n'.join(lines[i + 1:])
rec = open(f'{FD}/seq_record_ch12.py', encoding='utf-8').read()
rec = fix_head(rec, 'seq_record')
assert rec.count("HERE = (_ROOT + '/World/step9')") == 1
open(f'{SP}/seq_record_ch13.py', 'w', encoding='utf-8').write(rec)
st = open(f'{FD}/seq_stitch_ch12.py', encoding='utf-8').read()
st = fix_head(st, 'seq_stitch')
assert st.count("HERE = (_ROOT + '/World/step9')") == 1 and st.count("SCR = os.path.dirname(os.path.abspath(__file__))") == 1
anchor = "# markers' list above 9b's exactly (172)\n"
assert st.count(anchor) == 1, st.count(anchor)
NOTE = anchor + "# THE DEUTERONOMY WALK 11b (2026-09-21; DEUTERONOMY_WALK.md \"Sitting 11b\" THE LINES ON THE TAPE): NO MARKER — chapter 13's FOUR lines (word_sealed 13:1,\n# prophet_test_declared 13:2-6, inciter_law_declared 13:7-12, condemned_city_law_declared 13:13-19) are OWN-DAY lines at the counter's (40, 11, 1), STATUTE by form,\n# joined after the tape's last Deuteronomy 12 line by the sort (page_order); no act told only here (the kin's lines measured at the design) — no retrograde marker; the\n# markers' list above 10b's exactly (172)\n"
st = st.replace(anchor, NOTE)
open(f'{SP}/seq_stitch_ch13.py', 'w', encoding='utf-8').write(st)
import py_compile
py_compile.compile(f'{SP}/seq_record_ch13.py', doraise=True); py_compile.compile(f'{SP}/seq_stitch_ch13.py', doraise=True)
print('derived: seq_record_ch13.py %d bytes, seq_stitch_ch13.py %d bytes (the header from git; the 11b note after the 10b note); both compile' % (len(rec), len(st)))

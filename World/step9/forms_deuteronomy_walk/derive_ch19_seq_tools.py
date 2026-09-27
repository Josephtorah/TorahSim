#!/usr/bin/env python3
# THE DEUTERONOMY WALK 16b (2026-09-25): the recorder seq_record_ch19.py and the stitcher seq_stitch_ch19.py DERIVED from 15b's copies in the forms folder by
# asserted substitutions — the portable header made a scratch script's (ROOT from git, run from the repo root); the stitcher's chapter note: 16b's THIRTEEN own-day
# lines over three chapters, NO marker, appended after 15b's; nothing else moves. derive_ch17_seq_tools.py's form. RUN FROM THE REPO ROOT.
import subprocess, os
ROOT = _ROOT
SP = os.path.dirname(os.path.abspath(__file__))
FD = f'{ROOT}/World/step9/forms_deuteronomy_walk'
HEAD = "import os as _os, subprocess as _sp\n_ROOT = _ROOT   # THE DEUTERONOMY WALK 16b (2026-09-25): a scratch script — the repo root from git, run from the repo root (the forms copy computes it from its own place)\n"
def fix_head(src, name):
    lines = src.split('\n')
    i = [k for k, l in enumerate(lines) if l.startswith('_ROOT = _os.path.normpath(')]
    assert len(i) == 1, (name, i)
    i = i[0]; assert i <= 2, (name, i)
    pre = [l for l in lines[:i] if l.strip() and not l.startswith('import subprocess as _sp') and not l.startswith('import os as _os')]
    assert pre == [], (name, pre)
    return HEAD + '\n'.join(lines[i + 1:])
rec = open(f'{FD}/seq_record_ch17.py', encoding='utf-8').read()
rec = fix_head(rec, 'seq_record')
assert rec.count("HERE = (_ROOT + '/World/step9')") == 1
open(f'{SP}/seq_record_ch19.py', 'w', encoding='utf-8').write(rec)
st = open(f'{FD}/seq_stitch_ch17.py', encoding='utf-8').read()
st = fix_head(st, 'seq_stitch')
assert st.count("HERE = (_ROOT + '/World/step9')") == 1 and st.count("SCR = os.path.dirname(os.path.abspath(__file__))") == 1
anchor = "# narrative verb in either chapter (18:16-17 retell Horeb's request — REFERENCE rows against the tape's own Deuteronomy 5 lines) — no retrograde marker; the markers' list above 14b's exactly (172)\n"
assert st.count(anchor) == 1, st.count(anchor)
NOTE = anchor + "# THE DEUTERONOMY WALK 16b (2026-09-25; DEUTERONOMY_WALK.md \"Sitting 16b\" THE LEAN DESIGN over THREE chapters): NO MARKER — chapters 19-21's THIRTEEN lines (refuge_cities_declared 19:1,\n# manslayer_and_murderer_declared 19:4, landmark_declared 19:14, witnesses_law_declared 19:15, war_speech_declared 20:1, siege_law_declared 20:10, seven_nations_herem_declared 20:16,\n# siege_trees_declared 20:19, heifer_rite_declared 21:1, captive_wife_declared 21:10, firstborn_portion_declared 21:15, rebellious_son_declared 21:18, hanged_burial_declared 21:22) are\n# OWN-DAY lines at the counter's (40, 11, 1), STATUTE by form, joined after the tape's last Deuteronomy 18 line by the sort (page_order); no narrative verb in the three chapters (19:8's\n# oath formula and 20:1's exodus formula REFERENCE rows against the tape's own lines) — no retrograde marker; the markers' list above 15b's exactly (172)\n"
st = st.replace(anchor, NOTE)
open(f'{SP}/seq_stitch_ch19.py', 'w', encoding='utf-8').write(st)
import py_compile
py_compile.compile(f'{SP}/seq_record_ch19.py', doraise=True); py_compile.compile(f'{SP}/seq_stitch_ch19.py', doraise=True)
print('derived: seq_record_ch19.py %d bytes, seq_stitch_ch19.py %d bytes (the header from git; the 16b note after the 15b note); both compile' % (len(rec), len(st)))

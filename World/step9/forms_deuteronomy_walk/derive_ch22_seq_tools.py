import os as _os
_ROOT = _os.path.normpath(_os.path.join(_os.path.dirname(_os.path.abspath(__file__)), '..', '..', '..'))   # THE PORTABLE REPO (2026-09-15): the repo root from this file's own place
#!/usr/bin/env python3
# THE DEUTERONOMY WALK 17b (2026-09-26): the recorder seq_record_ch22.py and the stitcher seq_stitch_ch22.py DERIVED from 16b's copies in the forms folder by
# asserted substitutions — the portable header made a scratch script's (ROOT from git, run from the repo root); the stitcher's chapter note: 17b's TWENTY own-day
# lines over four chapters, NO marker, appended after 16b's; nothing else moves. derive_ch19_seq_tools.py's form. RUN FROM THE REPO ROOT.
import subprocess, os
ROOT = _ROOT
SP = os.path.dirname(os.path.abspath(__file__))
FD = f'{ROOT}/World/step9/forms_deuteronomy_walk'
HEAD = "import os as _os, subprocess as _sp\n_ROOT = _ROOT   # THE DEUTERONOMY WALK 17b (2026-09-26): a scratch script — the repo root from git, run from the repo root (the forms copy computes it from its own place)\n"
def fix_head(src, name):
    lines = src.split('\n')
    i = [k for k, l in enumerate(lines) if l.startswith('#!/usr/bin/env python3')]
    assert len(i) == 1 and i[0] <= 4, (name, i)
    pre = lines[:i[0]]
    assert all(l.startswith(('import os as _os', '_ROOT = ')) for l in pre if l.strip()), (name, pre)   # the copier's portable header and 16b's own head — both dropped, this HEAD in their place
    return HEAD + '\n'.join(lines[i[0]:])
rec = open(f'{FD}/seq_record_ch19.py', encoding='utf-8').read()
rec = fix_head(rec, 'seq_record')
assert rec.count("HERE = (_ROOT + '/World/step9')") == 1 and '16b' not in rec.split('\n', 3)[3][:400]
open(f'{SP}/seq_record_ch22.py', 'w', encoding='utf-8').write(rec)
st = open(f'{FD}/seq_stitch_ch19.py', encoding='utf-8').read()
st = fix_head(st, 'seq_stitch')
assert st.count("HERE = (_ROOT + '/World/step9')") == 1 and st.count("SCR = os.path.dirname(os.path.abspath(__file__))") == 1
anchor = "# oath formula and 20:1's exodus formula REFERENCE rows against the tape's own lines) — no retrograde marker; the markers' list above 15b's exactly (172)\n"
assert st.count(anchor) == 1, st.count(anchor)
NOTE = anchor + "# THE DEUTERONOMY WALK 17b (2026-09-26; DEUTERONOMY_WALK.md \"Sitting 17b\" THE LEAN DESIGN over FOUR chapters): NO MARKER — chapters 22-25's TWENTY lines (lost_thing_declared 22:1,\n# garments_nest_parapet_declared 22:5, mixtures_tassels_declared 22:9, slandered_bride_declared 22:13, adultery_betrothed_seducer_declared 22:22, fathers_wife_assembly_declared 23:1,\n# camp_holiness_declared 23:10, slave_hire_interest_declared 23:16, vows_law_declared 23:22, laborer_vineyard_grain_declared 23:25, divorce_declared 24:1, newlywed_millstone_kidnapper_declared 24:5,\n# leprosy_miriam_declared 24:8, pledge_wage_declared 24:10, fathers_sons_stranger_gleanings_declared 24:16, lashes_declared 25:1, muzzle_declared 25:4, levirate_declared 25:5,\n# wrestlers_weights_declared 25:11, amalek_remembrance_declared 25:17) are OWN-DAY lines at the counter's (40, 11, 1), STATUTE by form, joined after the tape's last Deuteronomy 21 line by the\n# sort (page_order); no narrative verb in the four chapters (23:5-6's Balaam, 24:9's Miriam and 25:17-18's Amalek REMEMBRANCES — REFERENCE rows against the tape's own lines; 22:17's\n# 'saying' the father's speech inside the bride's law) — no retrograde marker; the markers' list above 16b's exactly (172)\n"
st = st.replace(anchor, NOTE)
open(f'{SP}/seq_stitch_ch22.py', 'w', encoding='utf-8').write(st)
import py_compile
py_compile.compile(f'{SP}/seq_record_ch22.py', doraise=True); py_compile.compile(f'{SP}/seq_stitch_ch22.py', doraise=True)
print('derived: seq_record_ch22.py %d bytes, seq_stitch_ch22.py %d bytes (the header from git; the 17b note after the 16b note); both compile' % (len(rec), len(st)))

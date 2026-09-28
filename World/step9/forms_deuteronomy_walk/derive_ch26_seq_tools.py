import os as _os
_ROOT = _os.path.normpath(_os.path.join(_os.path.dirname(_os.path.abspath(__file__)), '..', '..', '..'))   # THE PORTABLE REPO (2026-09-15): the repo root from this file's own place
#!/usr/bin/env python3
# THE DEUTERONOMY WALK 18b (2026-09-26): the recorder seq_record_ch26.py and the stitcher seq_stitch_ch26.py DERIVED from 17b's copies in the forms folder by
# asserted substitutions — the portable header made a scratch script's (ROOT from git, run from the repo root); the stitcher's chapter note: 18b's TWENTY-ONE own-day
# lines over three chapters, NO marker, appended after 17b's; nothing else moves. derive_ch22_seq_tools.py's form. RUN FROM THE REPO ROOT.
import subprocess, os
ROOT = _ROOT
SP = os.path.dirname(os.path.abspath(__file__))
FD = f'{ROOT}/World/step9/forms_deuteronomy_walk'
HEAD = "import os as _os, subprocess as _sp\n_ROOT = _ROOT   # THE DEUTERONOMY WALK 18b (2026-09-26): a scratch script — the repo root from git, run from the repo root (the forms copy computes it from its own place)\n"
def fix_head(src, name):
    lines = src.split('\n')
    i = [k for k, l in enumerate(lines) if l.startswith('#!/usr/bin/env python3')]
    assert len(i) == 1 and i[0] <= 4, (name, i)
    pre = lines[:i[0]]
    assert all(l.startswith(('import os as _os', '_ROOT = ')) for l in pre if l.strip()), (name, pre)   # the copier's portable header and 17b's own head — both dropped, this HEAD in their place
    return HEAD + '\n'.join(lines[i[0]:])
rec = open(f'{FD}/seq_record_ch22.py', encoding='utf-8').read()
rec = fix_head(rec, 'seq_record')
assert rec.count("HERE = (_ROOT + '/World/step9')") == 1 and '17b' not in rec.split('\n', 3)[3][:400]
open(f'{SP}/seq_record_ch26.py', 'w', encoding='utf-8').write(rec)
st = open(f'{FD}/seq_stitch_ch22.py', encoding='utf-8').read()
st = fix_head(st, 'seq_stitch')
assert st.count("HERE = (_ROOT + '/World/step9')") == 1 and st.count("SCR = os.path.dirname(os.path.abspath(__file__))") == 1
anchor = "# 'saying' the father's speech inside the bride's law) — no retrograde marker; the markers' list above 16b's exactly (172)\n"
assert st.count(anchor) == 1, st.count(anchor)
NOTE = anchor + "# THE DEUTERONOMY WALK 18b (2026-09-26; DEUTERONOMY_WALK.md \"Sitting 18b\" THE LEAN DESIGN over THREE chapters): NO MARKER — chapters 26-28's TWENTY-ONE lines (first_fruits_declared 26:1,\n# tithe_confession_declared 26:12, covenant_formula_declared 26:16, stones_altar_declared 27:1, people_this_day_declared 27:9, gerizim_ebal_tribes_declared 27:11, twelve_curses_declared 27:14,\n# blessings_condition_declared 28:1, enemies_storehouses_blessing_declared 28:7, holy_people_fear_declared 28:9, heavens_treasure_lending_declared 28:11, curses_condition_declared 28:15,\n# curse_diseases_brass_declared 28:20, defeat_carcass_boil_madness_declared 28:25, wife_house_vineyard_king_taken_declared 28:30, harvests_failed_stranger_head_declared 28:38,\n# curses_pursue_iron_yoke_declared 28:45, eagle_nation_siege_declared 28:49, sons_flesh_siege_declared 28:53, plagues_scattered_declared 28:58, trembling_ships_covenant_declared 28:65) are\n# OWN-DAY lines at the counter's (40, 11, 1), STATUTE by form, joined after the tape's last Deuteronomy 25 line by the sort (page_order); chapter 27's three narrative frames (27:1 Moses and the\n# elders commanded, 27:9 Moses and the priests the Levites spoke, 27:11 Moses commanded 'that day') are the SPEAKER of three lines, not acts of their own — 'that day' the counter's; 26:5-10's\n# recital a RETELLING of the tape's own story (REFERENCE rows) — no retrograde marker; the markers' list above 17b's exactly (172)\n"
st = st.replace(anchor, NOTE)
open(f'{SP}/seq_stitch_ch26.py', 'w', encoding='utf-8').write(st)
import py_compile
py_compile.compile(f'{SP}/seq_record_ch26.py', doraise=True); py_compile.compile(f'{SP}/seq_stitch_ch26.py', doraise=True)
print('derived: seq_record_ch26.py %d bytes, seq_stitch_ch26.py %d bytes (the header from git; the 18b note after the 17b note); both compile' % (len(rec), len(st)))

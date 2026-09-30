import os as _os
_ROOT = _os.path.normpath(_os.path.join(_os.path.dirname(_os.path.abspath(__file__)), '..', '..', '..'))   # THE PORTABLE REPO (2026-09-15): the repo root from this file's own place
#!/usr/bin/env python3
# THE DEUTERONOMY WALK 21b (2026-09-29): the recorder seq_record_ch33.py and the stitcher seq_stitch_ch33.py DERIVED from 20b's copies in the forms folder by
# asserted substitutions — the portable header made a scratch script's (ROOT from git, run from the repo root); the stitcher's chapter note: 21b's ELEVEN own-day
# lines IN TWO FORMS over ONE chapter, appended after 20b's note (itself after 19b's note and its marker row); NO MARKER ROW of our own (the blessing stands on 19b's marker
# at 31:1 — Moses' last day (40, 12, 7); 33:1's 'before his death' THAT day); markers 173 UNMOVED. derive_ch32_seq_tools.py's form. RUN FROM THE REPO ROOT.
import subprocess, os, re
ROOT = _ROOT
SP = os.path.dirname(os.path.abspath(__file__))
FD = f'{ROOT}/World/step9/forms_deuteronomy_walk'
HEAD = "import os as _os, subprocess as _sp\n_ROOT = _ROOT   # THE DEUTERONOMY WALK 21b (2026-09-29): a scratch script — the repo root from git, run from the repo root (the forms copy computes it from its own place)\n"
def fix_head(src, name):
    lines = src.split('\n')
    i = [k for k, l in enumerate(lines) if l.startswith('#!/usr/bin/env python3')]
    assert len(i) == 1 and i[0] <= 4, (name, i)
    pre = lines[:i[0]]
    assert all(l.startswith(('import os as _os', '_ROOT = ')) for l in pre if l.strip()), (name, pre)   # the copier's portable header and 20b's own head — both dropped, this HEAD in their place
    return HEAD + '\n'.join(lines[i[0]:])
rec = open(f'{FD}/seq_record_ch32.py', encoding='utf-8').read()
rec = fix_head(rec, 'seq_record')
assert rec.count("HERE = (_ROOT + '/World/step9')") == 1
open(f'{SP}/seq_record_ch33.py', 'w', encoding='utf-8').write(rec)
st = open(f'{FD}/seq_stitch_ch32.py', encoding='utf-8').read()
st = fix_head(st, 'seq_stitch')
assert st.count("HERE = (_ROOT + '/World/step9')") == 1 and st.count("SCR = os.path.dirname(os.path.abspath(__file__))") == 1
ANCH = "# marker, no marker of its own; the parser's two guards (the false eight at 32:15, the joined thousand at 32:30) DATA rows, no count; the markers' list above 19b's EXACTLY (173)\n"
assert st.count(ANCH) == 1, "20b's note's last line — the anchor"
m = re.search(re.escape(ANCH), st)
assert st.count("mk('Deut 31:2'") == 1 and st.count("mk('Deut 32:") == 0, 'the 19b marker row stands alone; 20b wrote none'
NOTE = ("# THE DEUTERONOMY WALK 21b (2026-09-29; DEUTERONOMY_WALK.md \"Sitting 21b\" THE LEAN DESIGN over ONE chapter — THE BLESSING, one unit): NO MARKER — chapter 33's ELEVEN lines IN TWO FORMS\n"
        "# (1 ACT: the frame moses_blessed_israel_before_his_death 33:1; 10 SPEECHES: the prologue blessing_prologue_law_and_king_declared 33:3, the ten blessings at the reading's seats blessing_reuben_and_judah_declared 33:6,\n"
        "# blessing_levi_declared 33:8, blessing_benjamin_declared 33:12, blessing_joseph_declared 33:13, blessing_zebulun_and_issachar_declared 33:18, blessing_gad_declared 33:20, blessing_dan_naphtali_asher_declared 33:22,\n"
        "# and the coda's two blessing_rider_of_the_heaven_declared 33:26, blessing_israel_dwells_alone_declared 33:28) are OWN-DAY lines joined after the tape's last Deuteronomy 32 line by the sort (page_order), EVERY ONE at\n"
        "# MOSES' LAST DAY (40, 12, 7) AFTER 19b's ONE MARKER at 31:1 above — 33:1's 'before his death' names THAT day (the Sifrei 342:1 — the hard words first, the blessing after); the blessing's pasts (33:2 Sinai, 33:8 Massah\n"
        "# and Meribah, 33:9 the calf's sword, 33:16 the bush, 33:17 Ephraim before Manasseh) RUN CITATIONS against the tape's own lines (REFERENCE rows), Moses' grave at 33:21 FORWARD to 34:6 (the death's sitting's), the\n"
        "# blessings' futures STATUSES on the tribes' own ledgers — no retrograde marker, no marker of its own; the parser's false seven (33:23 'sated') a DATA row, no count; the markers' list above 19b's EXACTLY (173)\n")
st = st[:m.end()] + NOTE + st[m.end():]
assert st.count("mk('Deut 33:") == 0 and st.count('THE DEUTERONOMY WALK 21b') == 2   # the header's and the note's
open(f'{SP}/seq_stitch_ch33.py', 'w', encoding='utf-8').write(st)
import py_compile
py_compile.compile(f'{SP}/seq_record_ch33.py', doraise=True); py_compile.compile(f'{SP}/seq_stitch_ch33.py', doraise=True)
print('derived: seq_record_ch33.py %d bytes, seq_stitch_ch33.py %d bytes (the header from git; the 21b note after the 20b note; NO marker row of our own — markers 173 unmoved); both compile' % (len(rec), len(st)))

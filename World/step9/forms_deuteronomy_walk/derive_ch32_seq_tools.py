import os as _os
_ROOT = _os.path.normpath(_os.path.join(_os.path.dirname(_os.path.abspath(__file__)), '..', '..', '..'))   # THE PORTABLE REPO (2026-09-15): the repo root from this file's own place
#!/usr/bin/env python3
# THE DEUTERONOMY WALK 20b (2026-09-28): the recorder seq_record_ch32.py and the stitcher seq_stitch_ch32.py DERIVED from 19b's copies in the forms folder by
# asserted substitutions — the portable header made a scratch script's (ROOT from git, run from the repo root); the stitcher's chapter note: 20b's SIXTEEN own-day
# lines IN THREE FORMS over ONE chapter, appended after 19b's note AND ITS MARKER ROW; NO MARKER ROW of our own (the song stands on 19b's marker at 31:1 — Moses' last day
# (40, 12, 7); 32:48's selfsame day THAT day); markers 173 UNMOVED. derive_ch29_seq_tools.py's form. RUN FROM THE REPO ROOT.
import subprocess, os, re
ROOT = _ROOT
SP = os.path.dirname(os.path.abspath(__file__))
FD = f'{ROOT}/World/step9/forms_deuteronomy_walk'
HEAD = "import os as _os, subprocess as _sp\n_ROOT = _ROOT   # THE DEUTERONOMY WALK 20b (2026-09-28): a scratch script — the repo root from git, run from the repo root (the forms copy computes it from its own place)\n"
def fix_head(src, name):
    lines = src.split('\n')
    i = [k for k, l in enumerate(lines) if l.startswith('#!/usr/bin/env python3')]
    assert len(i) == 1 and i[0] <= 4, (name, i)
    pre = lines[:i[0]]
    assert all(l.startswith(('import os as _os', '_ROOT = ')) for l in pre if l.strip()), (name, pre)   # the copier's portable header and 19b's own head — both dropped, this HEAD in their place
    return HEAD + '\n'.join(lines[i[0]:])
rec = open(f'{FD}/seq_record_ch29.py', encoding='utf-8').read()
rec = fix_head(rec, 'seq_record')
assert rec.count("HERE = (_ROOT + '/World/step9')") == 1
open(f'{SP}/seq_record_ch32.py', 'w', encoding='utf-8').write(rec)
st = open(f'{FD}/seq_stitch_ch29.py', encoding='utf-8').read()
st = fix_head(st, 'seq_stitch')
assert st.count("HERE = (_ROOT + '/World/step9')") == 1 and st.count("SCR = os.path.dirname(os.path.abspath(__file__))") == 1
m = re.search(r"^mk\('Deut 31:2', 'F', \[120\], .*\n", st, re.M); assert m and st.count("mk('Deut 31:2'") == 1, 'the 19b marker row — the anchor'
NOTE = ("# THE DEUTERONOMY WALK 20b (2026-09-28; DEUTERONOMY_WALK.md \"Sitting 20b\" THE LEAN DESIGN over ONE chapter — THE SONG and its frame, two units): NO MARKER — chapter 32's SIXTEEN lines IN THREE\n"
        "# FORMS (14 SPEECHES: the song's twelve stanzas song_witnesses_called_declared 32:1, song_crooked_generation_declared 32:5, song_nations_divided_lords_portion_declared 32:7, song_found_in_the_desert_declared 32:10,\n"
        "# song_heights_honey_rock_declared 32:13, song_jeshurun_fat_kicked_declared 32:15, song_face_hidden_foolish_nation_declared 32:19, song_evils_heaped_declared 32:23, song_enemys_boast_declared 32:26,\n"
        "# song_one_chasing_a_thousand_declared 32:29, song_vengeance_in_store_declared 32:34, song_i_am_he_declared 32:39, and the LORD's two to Moses nebo_summons_die_as_aaron 32:48, meribah_trespass_not_go_there_declared 32:51;\n"
        "# 1 ACT: song_spoken_by_moses_and_hoshea 32:44; 1 STATUTE: set_your_heart_no_empty_matter_declared 32:46) are OWN-DAY lines joined after the tape's last Deuteronomy 31 line by the sort (page_order), EVERY ONE at\n"
        "# MOSES' LAST DAY (40, 12, 7) AFTER 19b's ONE MARKER at 31:1 above — 32:48's 'that selfsame day' names THAT day (the Sifrei 337:1 — the flood's boarding and the exodus the kin); the song's past (32:7-14 — the desert,\n"
        "# the manna, the eagle, the honey from the rock) RUN CITATIONS against the tape's own lines (REFERENCE rows), Aaron's death at 32:50 a reference row on Numbers 20:28, Moses' death AHEAD at 34:5 — no retrograde\n"
        "# marker, no marker of its own; the parser's two guards (the false eight at 32:15, the joined thousand at 32:30) DATA rows, no count; the markers' list above 19b's EXACTLY (173)\n")
st = st[:m.end()] + NOTE + st[m.end():]
assert st.count("mk('Deut 32:") == 0 and st.count('THE DEUTERONOMY WALK 20b') == 2   # the header's and the note's
open(f'{SP}/seq_stitch_ch32.py', 'w', encoding='utf-8').write(st)
import py_compile
py_compile.compile(f'{SP}/seq_record_ch32.py', doraise=True); py_compile.compile(f'{SP}/seq_stitch_ch32.py', doraise=True)
print('derived: seq_record_ch32.py %d bytes, seq_stitch_ch32.py %d bytes (the header from git; the 20b note after the 19b note and its marker row; NO marker row of our own — markers 173 unmoved); both compile' % (len(rec), len(st)))

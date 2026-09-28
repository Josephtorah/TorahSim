import os as _os
_ROOT = _os.path.normpath(_os.path.join(_os.path.dirname(_os.path.abspath(__file__)), '..', '..', '..'))   # THE PORTABLE REPO (2026-09-15): the repo root from this file's own place
#!/usr/bin/env python3
# THE DEUTERONOMY WALK 19b (2026-09-27): the recorder seq_record_ch29.py and the stitcher seq_stitch_ch29.py DERIVED from 18b's copies in the forms folder by
# asserted substitutions — the portable header made a scratch script's (ROOT from git, run from the repo root); the stitcher's chapter note: 19b's TWENTY own-day
# lines IN THREE FORMS over three chapters, appended after 18b's; AND THE ONE MARKER ROW in section 4 — Deut 31:2's hundred and twenty (Moses' last day, the day
# (40, 12, 7): the year the ink's, the month and the day the answer sheet's) placed AT 31:1 (Genesis 7:1's precedent), the class TYPED reading_placed (a shelf
# number sits in the code — the stitcher's rule (ii)); markers 172 -> 173. derive_ch26_seq_tools.py's form. RUN FROM THE REPO ROOT.
import subprocess, os
ROOT = _ROOT
SP = os.path.dirname(os.path.abspath(__file__))
FD = f'{ROOT}/World/step9/forms_deuteronomy_walk'
HEAD = "import os as _os, subprocess as _sp\n_ROOT = _ROOT   # THE DEUTERONOMY WALK 19b (2026-09-27): a scratch script — the repo root from git, run from the repo root (the forms copy computes it from its own place)\n"
def fix_head(src, name):
    lines = src.split('\n')
    i = [k for k, l in enumerate(lines) if l.startswith('#!/usr/bin/env python3')]
    assert len(i) == 1 and i[0] <= 4, (name, i)
    pre = lines[:i[0]]
    assert all(l.startswith(('import os as _os', '_ROOT = ')) for l in pre if l.strip()), (name, pre)   # the copier's portable header and 18b's own head — both dropped, this HEAD in their place
    return HEAD + '\n'.join(lines[i[0]:])
rec = open(f'{FD}/seq_record_ch26.py', encoding='utf-8').read()
rec = fix_head(rec, 'seq_record')
assert rec.count("HERE = (_ROOT + '/World/step9')") == 1 and '18b' not in rec.split('\n', 3)[3][:400]
open(f'{SP}/seq_record_ch29.py', 'w', encoding='utf-8').write(rec)
st = open(f'{FD}/seq_stitch_ch26.py', encoding='utf-8').read()
st = fix_head(st, 'seq_stitch')
assert st.count("HERE = (_ROOT + '/World/step9')") == 1 and st.count("SCR = os.path.dirname(os.path.abspath(__file__))") == 1
anchor = "# recital a RETELLING of the tape's own story (REFERENCE rows) — no retrograde marker; the markers' list above 17b's exactly (172)\n"
assert st.count(anchor) == 1, st.count(anchor)
VALUE = ("a hundred and twenty years old this day (31:2) — the last day of Moses: the year from the ink (Exodus 7:7 — eighty at the exodus, plus the forty years), the month and the day from the answer sheet "
         "(the 7th of Adar — Tosefta Sotah 11:3, computed backward from Joshua 4:19; Seder Olam 10:2 as chukat holds it); the counter moves from (40, 11, 1) at 1:3 for the first time in the book; "
         "positioned at 31:1, the first verse of the line crossing_charge_declared (Genesis 7:1 the precedent — the number at 7:4, the position 7:1)")
assert "'" not in VALUE and '"' not in VALUE
MKROW = ("mk('Deut 31:2', 'F', [120], \"M['moses_120'] = w.clock.day_in('exodus', 40, 12, 7); w.marker('Deut 31:1', M['moses_120'], value='%s')\", "
         "\"Moses' last day — the year the ink's (Exodus 7:7 + 40), the month and the day the answer sheet's (the 7th of Adar); the class TYPED reading_placed: a shelf number sits in the code (the stitcher's rule ii); nums [120] the parser's own at 31:2\", at='Deut 31:1', place='reading_placed')\n" % VALUE)
NOTE = anchor + ("# THE DEUTERONOMY WALK 19b (2026-09-27; DEUTERONOMY_WALK.md \"Sitting 19b\" THE LEAN DESIGN over THREE chapters — A NARRATIVE CHAPTER among them): ONE MARKER — chapters 29-31's TWENTY lines IN\n"
                 "# THREE FORMS (13 STATUTES: moab_recital_declared 29:1, covenant_oath_entered_declared 29:9, hidden_idolater_curse_declared 29:15, land_desolation_answer_declared 29:21, hidden_and_revealed_declared 29:28,\n"
                 "# return_and_gathering_declared 30:1, heart_circumcised_declared 30:6, commandment_near_declared 30:11, life_and_death_choice_declared 30:15, crossing_charge_declared 31:1, hakhel_reading_declared 31:10,\n"
                 "# book_beside_the_ark_declared 31:24, assembly_and_song_spoken_declared 31:28; 4 ACTS: joshua_charged_before_israel 31:7, law_written_given 31:9, tent_summons_cloud_appeared 31:14, song_written_taught 31:22;\n"
                 "# 3 SPEECHES OF THE LORD: apostasy_and_hidden_face_foretold 31:16, song_witness_commanded 31:19, joshua_commissioned_at_tent 31:23) are OWN-DAY lines joined after the tape's last Deuteronomy 28 line by\n"
                 "# the sort (page_order); the 9 of chapters 29-30 at the counter's (40, 11, 1), the 11 of chapter 31 at MOSES' LAST DAY (40, 12, 7) AFTER THE ONE MARKER BELOW — Deut 31:2 'I am a hundred and twenty years\n"
                 "# old THIS DAY': the year the ink's (Exodus 7:7's eighty + forty), the month and the day the answer sheet's (the 7th of Adar — Tosefta Sotah 11:3 read whole at the design), placed AT 31:1 for the line's\n"
                 "# first verse (Genesis 7:1's precedent), the class TYPED reading_placed; 29:1-7's recital a RETELLING of the tape's own story (REFERENCE rows) and chapter 31's acts the narrator's present at the\n"
                 "# marker's day — no retrograde marker; the markers' list above 18b's PLUS ONE (172 -> 173)\n") + MKROW
st = st.replace(anchor, NOTE)
assert st.count("mk('Deut 31:2'") == 1 and st.count("place='reading_placed'") >= 1
open(f'{SP}/seq_stitch_ch29.py', 'w', encoding='utf-8').write(st)
import py_compile
py_compile.compile(f'{SP}/seq_record_ch29.py', doraise=True); py_compile.compile(f'{SP}/seq_stitch_ch29.py', doraise=True)
print('derived: seq_record_ch29.py %d bytes, seq_stitch_ch29.py %d bytes (the header from git; the 19b note after the 18b note; THE MARKER ROW mk(Deut 31:2, F, [120], … at=Deut 31:1, place=reading_placed)); both compile' % (len(rec), len(st)))

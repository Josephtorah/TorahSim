import os as _os
_ROOT = _os.path.normpath(_os.path.join(_os.path.dirname(_os.path.abspath(__file__)), '..', '..', '..'))   # THE PORTABLE REPO (2026-09-15): the repo root from this file's own place
#!/usr/bin/env python3
# THE DEUTERONOMY WALK 22b (2026-09-30): the recorder seq_record_ch34.py and the stitcher seq_stitch_ch34.py DERIVED from 21b's copies in the forms folder by
# asserted substitutions — the portable header made a scratch script's (ROOT from git, run from the repo root); the stitcher's chapter note: 22b's SIX own-day
# lines IN TWO FORMS over ONE chapter, appended after 21b's note (itself after 20b's and 19b's note with its marker row); NO MARKER ROW of our own (the death falls on 19b's
# marker's day (40, 12, 7) — the thirty days of weeping a DURATION by the design's ruling); markers 173 UNMOVED. derive_ch33_seq_tools.py's form. RUN FROM THE REPO ROOT.
import subprocess, os, re
ROOT = _ROOT
SP = os.path.dirname(os.path.abspath(__file__))
FD = f'{ROOT}/World/step9/forms_deuteronomy_walk'
HEAD = "import os as _os, subprocess as _sp\n_ROOT = _ROOT   # THE DEUTERONOMY WALK 22b (2026-09-30): a scratch script — the repo root from git, run from the repo root (the forms copy computes it from its own place)\n"
def fix_head(src, name):
    lines = src.split('\n')
    i = [k for k, l in enumerate(lines) if l.startswith('#!/usr/bin/env python3')]
    assert len(i) == 1 and i[0] <= 4, (name, i)
    pre = lines[:i[0]]
    assert all(l.startswith(('import os as _os', '_ROOT = ')) for l in pre if l.strip()), (name, pre)   # the copier's portable header and 21b's own head — both dropped, this HEAD in their place
    return HEAD + '\n'.join(lines[i[0]:])
rec = open(f'{FD}/seq_record_ch33.py', encoding='utf-8').read()
rec = fix_head(rec, 'seq_record')
assert rec.count("HERE = (_ROOT + '/World/step9')") == 1
open(f'{SP}/seq_record_ch34.py', 'w', encoding='utf-8').write(rec)
st = open(f'{FD}/seq_stitch_ch33.py', encoding='utf-8').read()
st = fix_head(st, 'seq_stitch')
assert st.count("HERE = (_ROOT + '/World/step9')") == 1 and st.count("SCR = os.path.dirname(os.path.abspath(__file__))") == 1
ANCH = "# blessings' futures STATUSES on the tribes' own ledgers — no retrograde marker, no marker of its own; the parser's false seven (33:23 'sated') a DATA row, no count; the markers' list above 19b's EXACTLY (173)\n"
assert st.count(ANCH) == 1, "21b's note's last line — the anchor"
m = re.search(re.escape(ANCH), st)
assert st.count("mk('Deut 31:2'") == 1 and st.count("mk('Deut 32:") == 0 and st.count("mk('Deut 33:") == 0, 'the 19b marker row stands alone; 20b and 21b wrote none'
NOTE = ("# THE DEUTERONOMY WALK 22b (2026-09-30; DEUTERONOMY_WALK.md \"Sitting 22b\" THE LEAN DESIGN over ONE chapter — THE DEATH OF MOSES, one unit, THE BOOK'S LAST): NO MARKER — chapter 34's SIX lines IN TWO FORMS\n"
        "# (5 ACTS of the narrator: moses_went_up_to_nebo_and_saw_the_land 34:1, moses_died_and_was_buried 34:5, moses_hundred_and_twenty_israel_wept_thirty_days 34:7, joshua_full_of_the_spirit_israel_hearkened 34:9,\n"
        "# no_prophet_like_moses_declared 34:10 — the epilogue's 'there arose not' a narrative past; 1 SPEECH of the LORD: oath_land_shown_not_crossed_declared 34:4 — the subject god) are OWN-DAY lines joined after the tape's\n"
        "# last Deuteronomy 33 line by the sort (page_order), EVERY ONE at MOSES' LAST DAY (40, 12, 7) AFTER 19b's ONE MARKER at 31:1 above — the seventh of Adar, the death THAT day; THE THIRTY DAYS OF WEEPING (34:8) A DURATION,\n"
        "# NOT A MARKER (the design's ruling — a marker is the ink's own date statement, a duration an act's length; no timer, the counter unmoved, the next book's first marker walks it — cited never read); the chapter's pasts\n"
        "# (34:1 the summons 32:49, 34:4 Exodus 33:1's oath and the commission's debit, 34:5 Aaron's death in Aaron's words, 34:9 the commission Numbers 27:18-23, 34:11-12 the signs and the tablets broken) RUN CITATIONS against the\n"
        "# tape's own lines (REFERENCE rows); THREE REUSES at their own forward seats (the denial 32:52 -> 34:4 a heaven entry, the gathering 32:50 -> 34:5 a status, Aaron's thirty days Numbers 20:29 -> 34:8 the timer row written\n"
        "# WITHOUT A DUE — no timer set); the parser's 120 (34:7) and 30 (34:8) DATA rows, no count; THE BOOK'S EDGE at 34:12 — the Torah's tape ends; the markers' list above 19b's EXACTLY (173)\n")
st = st[:m.end()] + NOTE + st[m.end():]
assert st.count("mk('Deut 34:") == 0 and st.count('THE DEUTERONOMY WALK 22b') == 2   # the header's and the note's
open(f'{SP}/seq_stitch_ch34.py', 'w', encoding='utf-8').write(st)
import py_compile
py_compile.compile(f'{SP}/seq_record_ch34.py', doraise=True); py_compile.compile(f'{SP}/seq_stitch_ch34.py', doraise=True)
print('derived: seq_record_ch34.py %d bytes, seq_stitch_ch34.py %d bytes (the header from git; the 22b note after the 21b note; NO marker row of our own — markers 173 unmoved); both compile' % (len(rec), len(st)))

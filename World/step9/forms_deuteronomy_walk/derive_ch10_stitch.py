import os as _os
_ROOT = _os.path.normpath(_os.path.join(_os.path.dirname(_os.path.abspath(__file__)), '..', '..', '..'))   # THE PORTABLE REPO (2026-09-15): the repo root from this file's own place
#!/usr/bin/env python3
# THE DEUTERONOMY WALK 8b (2026-09-20): seq_stitch_ch10.py derived from 7b's stitcher by asserted substitutions — the portable ROOT made the scratch form, and
# THE THREE MARKERS of chapter 10 typed after 7b's two: TWO RETROGRADE (Deut 10:2 the fragments in the ark at the erection's day — M['fragments_told'] =
# M['erected']; Deut 10:6 Aaron's burial at his death — M['burial_told'] = M['aaron_death']; both reading_placed) and ONE FORWARD (Deut 10:12 'and now,
# Israel' — M['speech_resumed_10'] = M['speech'], the counter's day re-asserted); 'second_tablets' joined to the span order after 'not_righteousness'.
import subprocess, os, re
ROOT = _ROOT
SP = os.path.dirname(os.path.abspath(__file__))
s = open(f'{ROOT}/World/step9/forms_deuteronomy_walk/seq_stitch_ch9.py', encoding='utf-8').read()
n = len(re.findall(r"^_ROOT = _os\.path\.normpath.*$", s, re.M)); assert n == 2, n
s = re.sub(r"^_ROOT = _os\.path\.normpath.*$", "_ROOT = _ROOT", s, flags=re.M)
anchor = "mk('Deut 9:21', 'F', [],"
assert s.count(anchor) == 1
i = s.index(anchor); j = s.index('\n', i) + 1
NEW = '''# THE DEUTERONOMY WALK 8b (2026-09-20; DEUTERONOMY_WALK.md "Sitting 8b" THE LINES ON THE TAPE): THE FORMS COMBINED — TWO RETROGRADE markers dating two acts
# TOLD ONLY HERE (the fragments in the ark at the erection's day — Exod 40:20's testimony placed, (2, 1, 1); Aaron's burial at his death — Num 20:28's
# (40, 5, 1) from 33:38's ordinals; reading_placed TYPED: the retelling gives no number, the days the tape's own placements of the acts the lines belong
# beside) and ONE FORWARD marker ending the stretch at the speech's own pivot ('and now, Israel' — 4:1's word, 10:12) before the four own-day lines
mk('Deut 10:2', 'R', [], "M['fragments_told'] = M['erected']; w.marker('Deut 10:2', M['fragments_told'], value='and you shall put them in the ark (10:2) — THE FRAGMENTS IN THE ARK TOLD ONLY HERE with no line on the tape (Exodus 34:1 has no ark clause; 40:20 places the whole tablets alone: the tape hole named at 7b): dated at the erection day, the testimony placed, Exod 40:20 (2, 1, 1) — the shelf reads the clause of both sets (Menachot 99a:12; Bava Batra 14b:6): RETROGRADE after 9:21 (40, 11, 1) — Pesachim 6b:7 class; the supplied line writes fragments_in_the_ark on the ark (the tablets and the fragments; the scroll inside or beside — Bava Batra 14a-b)')", 'the fragments in the ark told: retrograde at the erection\\'s day (Exod 40:17)', place='reading_placed')
mk('Deut 10:6', 'R', [], "M['burial_told'] = M['aaron_death']; w.marker('Deut 10:6', M['burial_told'], value='and he was buried there (10:6) — AARON BURIED, TOLD ONLY HERE with no line on the tape (Numbers 20:28 the death, 20:29 the mourning, 33:38-39 the date and the age — never the burial): dated at his death, Num 20:28 (40, 5, 1) from 33:38 ordinals: RETROGRADE after 10:2 (2, 1, 1) — the second retrograde marker of the chapter; the supplied line writes buried on aaron (the status REUSED — the ninth buried); the place OPEN inside the line (Moserah in the retelling, Mount Hor on the tape — Seder Olam Rabbah 9:2 the retreat of seven stations, the parameter)')", 'Aaron\\'s burial told: retrograde at his death (Num 20:28)', place='reading_placed')
mk('Deut 10:12', 'F', [], "M['speech_resumed_10'] = M['speech']; w.marker('Deut 10:12', M['speech_resumed_10'], value='and now, Israel (10:12) — the speech resumes at its own day: the retrograde stretch of the burial ENDED, the counter own day (40, 11, 1) re-asserted (a retrograde stretch runs to the next marker — 2b lesson 1); FORWARD at the same day, 4:25, 5:32 and 9:21 form; the four own-day lines follow with no marker of their own (the laws restated — STATUTE by form)')", 'the stretch ends at the pivot (10:12) — a forward marker to the counter\\'s own day')
'''
s = s[:j] + NEW + s[j:]
m = re.search(r"^SPAN_ORDER = \[(.*?)\]", s, re.M | re.S); assert m
if "'not_righteousness'" in m.group(1):
    assert "'second_tablets'" not in m.group(1)
    s = s.replace("'not_righteousness'", "'not_righteousness', 'second_tablets'", 1)
    print('SPAN_ORDER: second_tablets after not_righteousness')
else:
    print('SPAN_ORDER: not_righteousness absent (7b did not join it) — second_tablets not joined either')
open(f'{SP}/seq_stitch_ch10.py', 'w', encoding='utf-8').write(s)
import py_compile; py_compile.compile(f'{SP}/seq_stitch_ch10.py', doraise=True)
print('seq_stitch_ch10.py derived: %d bytes; the three markers typed; compiles' % len(s))

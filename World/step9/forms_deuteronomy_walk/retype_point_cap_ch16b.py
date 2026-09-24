# THE DEUTERONOMY WALK 14b: the recovery page's lines trimmed under the cap (10,377 > 10,240 at the check) — the point writer's texts and the tail writer's anchors retyped together.
import os
SP = os.path.dirname(os.path.abspath(__file__))
def edit(name, pairs):
    p = f'{SP}/{name}'; s = open(p, encoding='utf-8').read()
    for old, new in pairs:
        assert s.count(old) == 1, (name, s.count(old), old[:80]); s = s.replace(old, new)
    open(p, 'w', encoding='utf-8').write(s); print(name, 'retyped:', len(pairs))
edit('write_ch16b_point.py', [
    ("'- NUMBERS CLOSED. DEUTERONOMY 1:1-16:22 ON THE TAPE (PUSHED through e824e52 — 15 and 13b; 16 and 14/14b uncommitted).'", "'- NUMBERS CLOSED. DEUTERONOMY 1:1-16:22 ON THE TAPE (PUSHED through e824e52 — 15/13b; 16 uncommitted).'"),
    ("'- THE TAPE at RUN (%s, pairs, 127), markers 172, closes 127; %s (DH1-DH5); the chain of 14b LAUNCHED, its summary unread.' % (RUN, TAPE_CP)", "'- THE TAPE at RUN (%s, pairs, 127), markers 172, closes 127; %s (DH1-DH5); 14b\\'s chain LAUNCHED, summary unread.' % (RUN, TAPE_CP)"),
    ("'- SITTING 14/14b (ch 16 READ + COMPILED, LEAN) at #210: 136 sources; 8 claims; festivals_judges %s; 5 lines, %d writes, %d parameters; the exam the 8 Mishnah rows; the tape %s; UNCOMMITTED. NEXT: THE TAIL (the summary once; records; forms; message), then the commit.' % (MATRIX, W, NPAR, TAPE_CP)", "'- SITTING 14/14b (ch 16 READ + COMPILED, LEAN) at #210: 136 sources; runner %s; 5 lines, %d writes, %d parameters; the tape %s; UNCOMMITTED. NEXT: THE TAIL (summary once; records; forms; message), then the commit.' % (MATRIX, W, NPAR, TAPE_CP)"),
    ("rec2 = sub1(rec2, '70 runners, 75 daemons; 1166 kinds / 1073 effects.', '71 runners, 76 daemons; 1171 kinds / 1088 effects.', 'the counts')", "rec2 = sub1(rec2, '70 runners, 75 daemons; 1166 kinds / 1073 effects.', '71 runners, 76 daemons; 1171 kinds / 1088 effects.', 'the counts')\nrec2 = sub1(rec2, '- SITTING 13/13b (ch 15): 132 sources; the docket 974 rows; release_firstborn 91/91; 4 lines, 15 writes, 27 parameters; PUSHED e824e52.', '- SITTING 13/13b (ch 15): 132 sources; docket 974; release_firstborn 91/91; PUSHED e824e52.', 'the 13b line')"),
])
edit('write_ch16b_records.py', [
    ("rec2 = sub1(rec, 'the chain of 14b LAUNCHED, its summary unread.', 'the chain of 14b ALL GREEN once (sweep %s).' % SWEEP, 'the RUN line')", "rec2 = sub1(rec, '14b\\'s chain LAUNCHED, summary unread.', '14b\\'s chain ALL GREEN once (sweep %s).' % SWEEP, 'the RUN line')"),
    ("rec2 = sub1(rec2, 'UNCOMMITTED. NEXT: THE TAIL (the summary once; records; forms; message), then the commit.', 'chain green; UNCOMMITTED. NEXT: the commit; then 15 (ch 17-18 READ, lean) after a compaction.', 'the sitting line')", "rec2 = sub1(rec2, 'UNCOMMITTED. NEXT: THE TAIL (summary once; records; forms; message), then the commit.', 'chain green; UNCOMMITTED. NEXT: the commit; then 15 (ch 17-18 READ, lean) after a compaction.', 'the sitting line')"),
])

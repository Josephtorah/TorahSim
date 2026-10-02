#!/usr/bin/env python3
# THE DEUTERONOMY WALK 22b TAIL (2026-10-01 18:40): write_ch34b_tail.py retyped for THE SIXTH PASS KILLED AND RESUMED — ten steps green, killed inside the sweep on the owner's
# "just stop" (18:35), resumed --from sweep on his "ok lets give it a try" (ch34b_gates6b.sh, the same folder; the ten lines kept as ch34b_gates6_SUMMARY_killed.txt). The sixth's
# summary MERGED (the killed ten + the resumed two), CHAIN6 the killed row (by hand, rc 137), CHAIN6R the resumed row; the departures 17, the lessons 19 (the cheaper form PROPOSED,
# not ruled). Every replacement asserted ONCE. RUN FROM THE REPO ROOT: python3 World/step9/forms_deuteronomy_walk/retype_writer_resume_ch34.py
import os, subprocess
SP = os.path.dirname(os.path.abspath(__file__)); W = f'{SP}/write_ch34b_tail.py'
s = open(W, encoding='utf-8').read(); n0 = len(s)
R = []
R.append(("S6, V6, T6 = summary(rd(f'{G6}/SUMMARY.txt')) if os.path.exists(f'{G6}/SUMMARY.txt') else ({}, 'PARTIAL', '')\nS3, V3, T3 = dict(S6), V6, T6   # the sixth pass read whole\n",
          "S6K, V6K, _ = summary(R('ch34b_gates6_SUMMARY_killed.txt')); assert V6K == 'PARTIAL' and len(S6K) == 10 and all(v[0] == 'PASS' for v in S6K.values()), S6K   # THE SIXTH PASS KILLED in the sweep (18:35, the owner's 'just stop'): its ten green lines kept\n"
          "S6R, V6, T6 = summary(rd(f'{G6}/SUMMARY.txt')) if os.path.exists(f'{G6}/SUMMARY.txt') else ({}, 'PARTIAL', '')   # THE SIXTH PASS RESUMED --from sweep (ch34b_gates6b.sh, the same folder): the sweep, the unmoved check, the verdict\n"
          "S6 = dict(S6K); S6.update({k: v for k, v in S6R.items() if v[0] != 'SKIP'}); S3, V3, T3 = dict(S6), V6, T6   # the sixth pass read whole: the killed ten and the resumed two\n"))
R.append(("CHAIN6 = int(CH[5][2]) if len(CH) > 5 else 0; assert len(CH) >= 5 and CH[3][3].strip() == '1' and 'FOURTH' in CH[3][1] and CH[4][3].strip() == '1' and 'FIFTH' in CH[4][1] and (len(CH) < 6 or 'SIXTH' in CH[5][1]), CH[3:]   # the fourth pass's row rc 1 (K1), the fifth's rc 1 (the sweep); the sixth's the last\n",
          "CHAIN6 = int(CH[5][2]) if len(CH) > 5 else 0; CHAIN6R = int(CH[6][2]) if len(CH) > 6 else 0; assert len(CH) >= 6 and CH[3][3].strip() == '1' and 'FOURTH' in CH[3][1] and CH[4][3].strip() == '1' and 'FIFTH' in CH[4][1] and CH[5][3].strip() == '137' and 'SIXTH' in CH[5][1] and 'KILLED' in CH[5][1] and (len(CH) < 7 or 'RESUMED' in CH[6][1]), CH[3:]   # the fourth's row rc 1 (K1), the fifth's rc 1 (the sweep), the sixth's killed row rc 137 (by hand from the prints' own times); the resumed row the last\n"))
R.append(("CHAIN4=CHAIN4, CHAIN5=CHAIN5, CHAIN6=CHAIN6,", "CHAIN4=CHAIN4, CHAIN5=CHAIN5, CHAIN6=CHAIN6, CHAIN6R=CHAIN6R,"))
R.append(("('a stale print', _n)   # every print read is the SIXTH pass's — newer than the fifth's summary, than the fourth's, than the second's\n",
          "('a stale print', _n)   # every print read is the SIXTH pass's — newer than the fifth's summary, than the fourth's, than the second's\n    assert all(os.path.getmtime(f'{G6}/{_n}.out') > os.path.getmtime(f'{SP}/ch34b_gates6_SUMMARY_killed.txt') for _n in ('sweep', 'unmoved')), 'the resumed steps older than the killed summary'\n"))
R.append(("the cache cleared whole and THE SIXTH PASS from the tape %(V3)s — and these records;",
          "the cache cleared whole and THE SIXTH PASS from the tape — ten steps green, killed inside the sweep on the owner's 'just stop' and RESUMED from the sweep on his word — %(V3)s — and these records;"))
R.append(("THE SIXTH PASS from the tape (ch34b_gates6.sh; %(CHAIN6)d s, done %(T3)s) %(V3)s — the tape %(TAPE3)s (%(TAPE3_S)d s, the cache harvested whole),",
          "THE SIXTH PASS from the tape (ch34b_gates6.sh) TEN STEPS GREEN in %(CHAIN6)d s and KILLED inside the sweep at 18:35 on the owner's 'just stop' ('this process is broken. no way it should take this long' — three and a half hours a pass, the positions two of them, and each late miss a whole pass again), its ten lines kept (ch34b_gates6_SUMMARY_killed.txt), the older runners' cases read for the counts moved by the reuses (none left but the literals already retyped), RESUMED --from sweep on his 'ok lets give it a try' (ch34b_gates6b.sh — the chain's own --from into the same folder; %(CHAIN6R)d s, done %(T3)s) %(V3)s — the tape %(TAPE3)s (%(TAPE3_S)d s, the cache harvested whole),"))
R.append(("THE SIXTH PASS from the tape %(V3)s — its prints read whole by this writer, the fourth's and the fifth's by name.\\n\\n\")",
          "THE SIXTH PASS from the tape — its prints read whole by this writer, the fourth's and the fifth's by name; (17) THE SIXTH PASS KILLED IN THE SWEEP AND RESUMED FROM IT — the owner's 'just stop' at 18:35 with ten steps green (%(CHAIN6)d s): the whole-chain rerun after the song's runner's retype followed the resume's step 3 as written (a runner edited: the cache cleared, the pass from the tape), yet a CASES literal is graded by the sweep alone and the tape, the probes and the gates read nothing it changed — the rerun from the tape cost a pass of three and a half hours for a thirty-minute step; on his 'ok lets give it a try' the chain RESUMED --from sweep into the same folder (%(CHAIN6R)d s) %(V3)s; the killed row written by hand from the prints' own times. PROPOSED for his ruling, not ruled: after a late-step fix that touches only what the failed step reads, resume from that step; the whole chain from the tape only when the tape, the probes or the gates themselves read what moved.\\n\\n\")"))
R.append(("a runner moved means the cache cleared and the pass from the tape.\\n\\n\")",
          "a runner moved means the cache cleared and the pass from the tape — AS WRITTEN; (19) THE LENGTH OF A PASS IS THE COST OF EVERY LATE MISS — three and a half hours (the positions two, the sweep half an hour): the ten green steps stand when nothing they read has moved, and the chain's --from (19b's and 21b's form) resumes from the step that fell; reading the older runners' cases for a moved count before a launch costs a minute and would have saved a pass; the whole-chain rule after any runner edit is the owner's to narrow (PROPOSED in departure 17).\\n\\n\")"))
R.append(("THE SIXTH PASS from the tape (%(CHAIN6)d s) %(V3)s: the tape %(TAPE3)s",
          "THE SIXTH PASS from the tape ten steps green in %(CHAIN6)d s, KILLED in the sweep on the owner's 'just stop' (the pass's length his objection), RESUMED --from sweep on his word (%(CHAIN6R)d s) %(V3)s: the tape %(TAPE3)s"))
R.append(("the departures 1-16 and the lessons 1-18,", "the departures 1-17 and the lessons 1-19,"))
R.append(("- THE TAPE at RUN %(RUN)s; %(TAPE3)s; the sixth pass %(V3)s; MARKERS 173", "- THE TAPE at RUN %(RUN)s; %(TAPE3)s; MARKERS 173"))
R.append(("the sixth from the tape %(V3)s). NEXT: the commit on his word; then his word on what follows.", "the sixth from the tape, killed in the sweep on his word and resumed there %(V3)s). NEXT: the commit on his word; then his word."))
R.append(("pass 6 from the tape %(V3)s;", "pass 6 from the tape — killed in the sweep on his word, resumed there — %(V3)s;"))
R.append(("no marker, the thirty days a TIMER row without a due; the receipt", "no marker; the receipt"))
R.append(("the chain\\'s sixth pass %(V3)s (the fourth red at K1", "the chain\\'s sixth pass, resumed from the sweep on his word, %(V3)s (the fourth red at K1"))
R.append(("THE SIXTH PASS from the tape (%(CHAIN6)d s) %(V3)s (the tape %(TAPE3)s;",
          "THE SIXTH PASS from the tape (%(CHAIN6)d s to ten green steps, KILLED in the sweep on the owner's 'just stop' — the pass's length his objection; RESUMED --from sweep on his word, %(CHAIN6R)d s) %(V3)s (the tape %(TAPE3)s;"))
R.append(("the departures 1-16, the lessons 1-18;", "the departures 1-17, the lessons 1-19;"))
R.append(("after a reuse, the older runners' cases are read for the moved effect's count. DEUTERONOMY CLOSED",
          "after a reuse, the older runners' cases are read for the moved effect's count; a late miss costs a whole pass — resume from the step that fell (PROPOSED for his ruling). DEUTERONOMY CLOSED"))
R.append(("pass 6 from the tape %(V3)s (the positions %(POS)s; the sweep %(SWEEP)s);", "pass 6 from the tape, killed in the sweep on the owner's word and resumed from it %(V3)s (the positions %(POS)s; the sweep %(SWEEP)s);"))
R.append(("THE SIXTH FROM THE TAPE %(V3)s TO THE UNMOVED CHECK", "THE SIXTH FROM THE TAPE TEN STEPS GREEN, KILLED IN THE SWEEP ON THE OWNER'S \\\"JUST STOP\\\" AND RESUMED FROM THE SWEEP ON HIS WORD %(V3)s TO THE UNMOVED CHECK"))
R.append(("SIXTEEN DEPARTURES AND EIGHTEEN LESSONS", "SEVENTEEN DEPARTURES AND NINETEEN LESSONS"))
R.append(("the chains' rows the background runs' — the six passes among them):", "the chains' rows the background runs' — the six passes among them, the sixth in two rows):"))
for i, (a, b) in enumerate(R):
    c = s.count(a); assert c == 1, (i, c, a[:100]); s = s.replace(a, b)
open(W, 'w', encoding='utf-8').write(s)
print('retyped %d replacements; %d -> %d bytes' % (len(R), n0, len(s)))
subprocess.run(['python3', '-m', 'py_compile', W], check=True); print('compiles')

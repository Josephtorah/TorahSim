import os as _os
_ROOT = _os.path.normpath(_os.path.join(_os.path.dirname(_os.path.abspath(__file__)), '..', '..', '..'))   # THE PORTABLE REPO (2026-09-15): the repo root from this file's own place
#!/usr/bin/env python3
# RUN 2 OF SITTING 4b CLOSED (2026-09-17): the checkpoint — the state doc's #190 addendum 6 (naming RUN 3's first step), the memory note, the index
# line. The docket's numbers parsed from its own coverage line; the probes' print parsed; the caps asserted; --check prints the plan only.
import os, re, subprocess, sys
ROOT = _ROOT
MEM = os.path.expanduser('~/.claude/projects/-Users-Shared-TorahSim/memory')
CHECK = '--check' in sys.argv
def rd(p): return open(p, encoding='utf-8').read()
D = rd(f'{ROOT}/logic/oral_triage/deu_06_vaetchanan_exam_2026-09-17.md')
m = re.search(r'\*\*read: (\d+) of \1 — COMPLETE\*\* \(the link-driven rows (\d+): ([^;]+); the topic windows (\d+): ([^;]+); all rows: ([^;]+); credited (\d+)', D)
N, NL, LINKV, NT, TOPV, ALLV, NCRED = m.groups(); NB = len(D.encode())
assert N == '747' and NL == '95' and NT == '652' and NCRED == '168'
pr = subprocess.run([sys.executable, f'{ROOT}/World/step9/readback_probes.py'], capture_output=True, text=True).stdout
assert 'readback_probes: 12/15' in pr and 'FAIL Q13' in pr and 'FAIL Q14' in pr and 'FAIL Q15' in pr, pr[-300:]
lint = subprocess.run([sys.executable, f'{ROOT}/logic/solo_tools/gloss_lint.py', f'{ROOT}/logic/oral_triage/deu_06_vaetchanan_exam_2026-09-17.md'], capture_output=True, text=True).stdout
assert 'gloss_lint: 0 flag' in lint, lint[-200:]
DATE = '2026-09-17'
STATE = (f'\n\n#190 ADDENDUM 6 ({DATE} — RUN 2 OF SITTING 4b CLOSED, on the owner\'s "One more run" at 661k: the probes to FAIL and THE DOCKET). THE PROBES: readback_probes.py Q13-Q15 written to FAIL before the runner exists (Q13 the runner\'s the_readback table — seven rows found, VERBATIM 3 / EXPANDED 3 / SHORTENED 1; Q14 the two lines on the speech\'s day with NO marker, markers 167, shema_commanded and test_barred on Israel; Q15 the register gate\'s finder blind at Deut 6:25, the RUN_CITATION pointer on file, the daemon registered) — the suite 12/15 as designed. '
         f'THE DOCKET (ch6_docket_scan.py rerun with the Berakhot cut — 2a-2b, 10b-11a, 13a-13b, 15a-16a, 61b; the dump 747 rows; the rows read at a short cut on ch6_docket_rows.py, 170 characters, in four chunks; the verdicts in four parts A-D as SPEC lists over the dump\'s own addresses (ch6_docket_common.py — a part can never invent an address); the writer write_ch6_docket.py from 3b\'s form): logic/oral_triage/deu_06_vaetchanan_exam_{DATE}.md — {N} rows ({NB:,} bytes), the link-driven rows {NL} ({LINKV}), the topic windows {NT} ({TOPV}); all rows {ALLV}; credited {NCRED}; LAW by cell F2 23 / F3 288 / F4 4 / F5 11 / F6 17 — the four duties the docket\'s mass; Berakhot 2a-16a\'s remainder (541 rows) enumerated outside declared scope; coverage computed (missing 0, extra 0); lint 0 after one fix (a hyphenated transliteration flagged — the lint reads Hebrew-derived jargon too). THE CROWNS (twenty-one in the docket): the times from "lie down" and "rise"; the postures; the exemption from "the way"; "hear" read twice; the intention and the first verse — "one" prolonged in the dalet (the store\'s dropped letter); the three terms; the four passages and the compartments (the spellings\' open row at Sanhedrin 4b:2 — the vocalization against the tradition); the left arm from "yadkha" with a heh — THE INK\'S FOURTH SPELLING read by the shelf; the head from "between your eyes" at 14:1 — THE INK\'S FIFTH SEAT; the order; the mezuzah\'s writing (the two analogies), post, side, gates; the seven; the father\'s duty; the creed at Jacob\'s bed; THE SON\'S ANSWER IS THE HAGGADAH\'S — "we were slaves" (6:21) and "He took us out from there" (6:23) the telling\'s obligatory clauses (Pesachim 116a:11, 116b:7): the readback\'s third form taught by the shelf; the true oath permitted by 6:13; the abutter; the tithe\'s exception to "you shall not test"; the conquest\'s houses; the blind exempt from 6:1; the large letters\' Talmud seat left parked. ONE FORM LESSON: two parts\' slices overlapped by two rows (the amud boundary) — the common helper\'s UNMATCHED assert caught it before the writer. '
         f'NOTHING MID-FLIGHT — A CLEAN COMPACTION POINT. The tree: the map, the state doc, readback_probes.py, the new docket, the memory (uncommitted since a7955cc). THE WORD FOR THE NEXT SITTING — RUN 3 OF 4b, its first step: the types by script — add_types_ch6.py from add_types_ch5.py (the forms folder) by sed: two tape kinds shema_declared (speech, 6:4-9) and testing_barred (speech, 6:16-19, the first telling Exodus 17:2-7), one case kind shema_case, two effects shema_commanded (status) and test_barred (block), the daemon block law_hear_o_israel (given_at Deut 6:4, installed_by boot; the watches), the functions block hear_o_israel (six cells), the span [[Deut, 6, 1, 25]], the CALL edges and the RUN_CITATION pointers named in the design; then the recorder and the stitcher (seq_record_ch6.py, seq_stitch_ch6.py — SPAN_ORDER + \'hear_o_israel\', no marker row), the gates to FAIL (daemon, dependency), the runner in four parts with the fast checker and the generated CASES, the literals CO1-CO9 (patch_seq_literals_ch6.py), checkpoint_check.py --all, the tape to 10/10 with THE REST; the checkpoint #190 addendum 7. POST-COMPACTION REREADS: the recovery page, the map\'s "Sitting 4b … THE DESIGN", MEMORY.md.\n')
MN = (f'\nSITTING 4b RUN 2 DONE {DATE} (on "One more run"): readback Q13-Q15 written to FAIL (12/15); THE DOCKET logic/oral_triage/deu_06_vaetchanan_exam_{DATE}.md — {N} rows (link {NL}, topic {NT}; {ALLV}; credited {NCRED}), four parts A-D as SPEC lists over the dump\'s addresses (ch6_docket_common.py), Berakhot 2a-16a cut to its verse-anchored amudim (the remainder enumerated outside scope), lint 0. THE CROWNS: the son\'s answer is the Haggadah\'s (6:21, 6:23 the obligatory clauses — Pesachim 116a-b); the spellings\' open row at Sanhedrin 4b:2; the fourth spelling of "your hand" and the fifth seat of "between your eyes" read by the shelf; "one" prolonged in the dalet. Clean point (#190 addendum 6). NEXT: RUN 3 — add_types_ch6.py (two tape kinds, one case kind, two effects, the daemon, the functions block, the span, the edges and pointers), the recorder and the stitcher, the gates to FAIL, the runner in parts, CO1-CO9, the tape to 10/10.\n')
plans = []
P = f'{ROOT}/logic/pre_logic_methods_2026-07-28/PROMPT_continue_solo_era_2026-08-06.md'; s = rd(P); assert '#190 ADDENDUM 6' not in s and '#190 ADDENDUM 5' in s
plans.append((P, s.rstrip('\n') + STATE))
P = f'{MEM}/deuteronomy-walk.md'; s = rd(P); assert 'SITTING 4b RUN 2 DONE' not in s
plans.append((P, s.rstrip('\n') + '\n' + MN))
P = f'{MEM}/MEMORY.md'; s = rd(P)
old = 'SITTING 4b RUN 1 DONE 2026-09-17 (the design); NEXT: RUN 2 the docket'
new = 'SITTING 4b RUNS 1-2 DONE 2026-09-17 (the docket 747); NEXT: RUN 3 the runner'
assert s.count(old) == 1, s.count(old)
s2 = s.replace(old, new); assert len(s2.encode('utf-8')) < 17000, len(s2.encode('utf-8'))
plans.append((P, s2))
for p, s2 in plans: assert s2 != rd(p), p
if CHECK:
    for p, s2 in plans: print('WOULD WRITE', p, len(rd(p)), '->', len(s2))
    sys.exit(0)
for p, s2 in plans:
    open(p, 'w', encoding='utf-8').write(s2); print('WROTE', p, len(s2.encode('utf-8')))
print('run 2 checkpoint written')

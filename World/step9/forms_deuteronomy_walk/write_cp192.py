import os as _os
_ROOT = _os.path.normpath(_os.path.join(_os.path.dirname(_os.path.abspath(__file__)), '..', '..', '..'))   # THE PORTABLE REPO (2026-09-15): the repo root from this file's own place
#!/usr/bin/env python3
# COMPACTION POINT #192 (2026-09-17, on the owner's "Ok get ready to compact" after the whole-row rule and its fix's parts (a)-(c)): the state doc's
# block, the recovery page's two lines (under 10,240 bytes), the memory note's compaction line. Every text built here; the caps asserted first.
import os, subprocess
ROOT = _ROOT
MEM = os.path.expanduser('~/.claude/projects/-Users-Shared-TorahSim/memory')
def rd(p): return open(p, encoding='utf-8').read()
plans = []
P = f'{ROOT}/logic/pre_logic_methods_2026-07-28/PROMPT_continue_solo_era_2026-08-06.md'; s = rd(P)
assert 'COMPACTION POINT #192' not in s and '#191 ADDENDUM 3' in s
CP = ('\n\n═══ COMPACTION POINT #192 (2026-09-17 — after THE WHOLE-ROW RULE and its fix\'s parts (a)-(c), between 4b\'s RUN 2 and RUN 3; the owner: "Ok get ready to compact" at 553k) ═══\n'
      'THE STATE: CHAPTER 6 READ AND FROZEN, COMMITTED a7955cc (NOT pushed). SITTING 4b RUNS 1-2 DONE (the design, the probes Q13-Q15 to FAIL, the docket). THEN, ON THE OWNER\'S RULING of this date ("OK, never ever cut corners with the Talmud go back and fix the ones where the shortcut was taken and write it in the rules forever" — after his questions "Are you still running every case by the Talmud?" and "Did we recently change this or have we always done it this way?"): THE WHOLE-ROW RULE written into the memory (talmud-rows-whole.md; the index; cost-rules-no-polling.md; full-oral-torah-law.md; deuteronomy-walk.md), the recovery page, THE_STEPS, RECORD_FORMS.md, the map (the four-run rule amended; the tail section "THE WHOLE-ROW RULE" with "THE FIX — AS BUILT"), THE_BRIEFING, the addenda §39, the state doc (#191 addenda 1-3). THE FIX: (a) chapter 6\'s docket reread whole — 70 of 747 rows corrected, 21 verdicts changed (the open row\'s principle at Sanhedrin 4b:12-14, not 4b:2; six rows had carried another row\'s content), the docket rewritten (204,382 bytes, lint 0; the WHOLE overlays in the scratchpad\'s ch6_docket_A-D.py, apply_whole in ch6_docket_common.py); (b) sitting 4\'s Sifrei rows past the cap and the 67 Hebrew rows whole — nothing lacking, 36:10 the one divergence, an appended section on the committed ledger; (c) 3b\'s 82 rows over 650 whole — no verdict changed, an appended section on the committed docket. The tape UNTOUCHED (3b\'s RUN); every gate as at the commit except readback 12/15 by design. NOTHING MID-FLIGHT. '
      'THE TREE (uncommitted since a7955cc): THE_BRIEFING.md, THE_STEPS.md, World/step9/DEUTERONOMY_WALK.md, World/step9/RECORD_FORMS.md, World/step9/readback_probes.py, the two appended oral_triage files, the new chapter 6 docket, this state doc, the recovery page, the addenda; the scratchpad holds the sitting\'s scripts (write_whole_row_rule.py, write_whole_fix_1.py, write_whole_fix_2.py, the ch6 docket parts with their WHOLE dicts, write_ch6_docket.py) — ⚠ the scratchpad\'s WHOLE overlays and the corrected writer are NOT yet in the forms folder: copy them at 4b\'s RUN 4 (copy_ch6b_forms.py).\n'
      'THE WORD FOR THE NEXT SITTING — THE FIX\'S PART (d), then 4b\'s RUN 3: (d) 2b\'s 114 rows over 650 characters (of 327; World/step9/forms_deuteronomy_walk/ch4_docket_dump.txt with ch4_docket_A-D.py) and 1b\'s 215 (of 864; the scratchpad\'s deu_docket_dump.txt with deu_docket_A-H.py) printed WHOLE with the verdict and note each received (the instrument of write_whole_fix_2\'s sitting: a python loop over the dump\'s blocks, len > 650, NOTE from the parts\' SPEC lines — chunks of forty to sixty rows), read against the verdict; an APPENDED "REREAD WHOLE" section on each committed docket (ls logic/oral_triage/ first — the 2b docket deu_04_*exam*, the 1b docket deu_01_03_*exam*), a cell retyped only if a verdict changes; the state doc\'s #192 addendum 1; the memory. THEN 4b\'s RUN 3 as the design and #191 wrote it: add_types_ch6.py first (from add_types_ch5.py by sed), the recorder and the stitcher, the gates to FAIL, the runner in parts, CO1-CO9, checkpoint_check.py --all, the tape to 10/10 with THE REST; then RUN 4.\n'
      'POST-COMPACTION REREADS (nothing else unasked): the recovery page, the map\'s NEWEST section ("THE WHOLE-ROW RULE" with "THE FIX — AS BUILT") and, before RUN 3, the map\'s "Sitting 4b — THE COMPILE OF CHAPTER 6 … THE DESIGN"; MEMORY.md.\n')
plans.append((P, s.rstrip('\n') + CP))
P = f'{ROOT}/logic/pre_logic_methods_2026-07-28/RECOVERY_new_thread_2026-09-12.md'; s = rd(P)
a = '- LAST COMMIT a7955cc (2026-09-17, NOT pushed): sitting 4 whole. Uncommitted: 4b\'s runs 1-2 — the design, the probes, the docket.'
b = '- LAST COMMIT a7955cc (2026-09-17, NOT pushed): sitting 4 whole. Uncommitted: 4b\'s runs 1-2; the whole-row rule and its fix (a)-(c).'
c = '- IN FLIGHT: THE WHOLE-ROW FIX (the map\'s tail section) — the cut rows reread whole; then 4b RUN 3 (the map\'s "Sitting 4b … THE DESIGN").'
d = '- IN FLIGHT: THE WHOLE-ROW FIX (d) — 2b\'s 114 and 1b\'s 215 long rows whole (the map\'s tail); then 4b RUN 3 ("Sitting 4b … THE DESIGN").'
assert s.count(a) == 1 and s.count(c) == 1, (s.count(a), s.count(c))
s2 = s.replace(a, b).replace(c, d); assert len(s2.encode('utf-8')) <= 10240, len(s2.encode('utf-8')); plans.append((P, s2))
P = f'{MEM}/deuteronomy-walk.md'; s = rd(P); assert 'COMPACTION #192' not in s
plans.append((P, s.rstrip('\n') + '\nCOMPACTION #192 (2026-09-17, after the whole-row rule and its fix (a)-(c); the owner: "Ok get ready to compact"): the state doc\'s block written; the reread after: the recovery page, the map\'s tail ("THE WHOLE-ROW RULE" + "THE FIX — AS BUILT"), MEMORY.md; NEXT the fix\'s (d) — 2b\'s 114 and 1b\'s 215 long rows whole; then 4b RUN 3 (the map\'s "Sitting 4b … THE DESIGN").\n'))
for p, s2 in plans: assert s2 != rd(p), p
for p, s2 in plans:
    open(p, 'w', encoding='utf-8').write(s2); print('WROTE', p, len(s2.encode('utf-8')))
print('compaction point #192 written')

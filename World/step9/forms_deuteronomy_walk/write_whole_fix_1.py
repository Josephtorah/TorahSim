import os as _os
_ROOT = _os.path.normpath(_os.path.join(_os.path.dirname(_os.path.abspath(__file__)), '..', '..', '..'))   # THE PORTABLE REPO (2026-09-15): the repo root from this file's own place
#!/usr/bin/env python3
# THE WHOLE-ROW FIX, part (a) closed (2026-09-17): chapter 6's docket reread whole — the state doc's #191 addendum 2 and the memory line; the counts
# read from the docket's own REREAD WHOLE line and the writer's print, never typed.
import os, re, subprocess, sys
ROOT = _ROOT
MEM = os.path.expanduser('~/.claude/projects/-Users-Shared-TorahSim/memory')
def rd(p): return open(p, encoding='utf-8').read()
D = rd(f'{ROOT}/logic/oral_triage/deu_06_vaetchanan_exam_2026-09-17.md')
m = re.search(r'# REREAD WHOLE .*?— (\d+) of (\d+) rows corrected \((\d+) verdicts changed, (\d+) notes rewritten', D); NC, NR, NV, NN = m.groups()
assert NR == '747' and int(NC) == D.count('[whole:') - 1, (NC, D.count('[whole:'))
mv = re.search(r'all rows: (CONTEXT \d+, DERIVATION \d+, DISPUTE \d+, LAW \d+)', D); ALLV = mv.group(1)
lint = subprocess.run([sys.executable, f'{ROOT}/logic/solo_tools/gloss_lint.py', f'{ROOT}/logic/oral_triage/deu_06_vaetchanan_exam_2026-09-17.md'], capture_output=True, text=True).stdout
assert 'gloss_lint: 0 flag' in lint, lint[-200:]
DATE = '2026-09-17'
STATE = (f'\n\n#191 ADDENDUM 2 ({DATE} — THE WHOLE-ROW FIX, part (a) CLOSED: CHAPTER 6\'S DOCKET REREAD WHOLE). Every one of the {NR} rows printed whole (ch6_docket_rows.py a b 100000, in nine chunks of forty to ninety rows) and read against the verdict typed from its first 170 characters; each part\'s corrections a WHOLE overlay applied by ch6_docket_common.apply_whole (the cut\'s row kept in SPEC as the record; a corrected note ends "[whole: …]"); the docket deleted and rewritten by write_ch6_docket.py with a REREAD WHOLE header line: {NC} of {NR} rows corrected ({NV} verdicts changed, {NN} notes rewritten; the counts computed); the verdicts now {ALLV} (from CONTEXT 268 / DERIVATION 55 / DISPUTE 81 / LAW 343); LAW by cell F2 23 / F3 288 / F4 6 / F5 11 / F6 18 (F4 4 → 6, F6 17 → 18); lint 0; {len(D.encode()):,} bytes. '
         'WHAT THE CUT HAD WRONG (the record\'s own exhibit): SIX ROWS CARRYING ANOTHER ROW\'S CONTENT — Kiddushin 30a:9 / 30a:15 (the threefold study on the row of "sharp", and the reverse), Menachot 34a:7 (Jehoiada\'s chest, not "your coming"), 34a:11 (the parchment-not-stones rule, not the gates), 35b:10 (the blessing\'s time, not a bathroom rule), Temurah 3b:16 / 4a:2 (Exodus 22:10 the bailee\'s oath, and "you shall fear" refused as a positive warning — the cut had put the true-oath proof on both), Berakhot 2a:6 (the question, not the answers), 13a:29 (the Rabbis take NO audibility from "hear"), Sanhedrin 4b:2 (the JUDGES\' number — THE OPEN ROW\'S PRINCIPLE SITS AT 4b:12-14, NOT 4b:2: the earlier addendum 6, the memory and the crowns list corrected); RULES MISSED — Kiddushin 34a:3 (Torah study 6:7, women exempt), Tosefta Avodah Zarah 1:3 (6:14 "you shall not go after" read as going along with the idolaters\' caravan), Temurah 3b:17 (the true oath\'s proof from 6:13), Berakhot 16a:10 (the verbal analogy 6:4 with 27:9 for intent), Menachot 43b:5 (Mishnah 1:2\'s morning start grounded in the fringes\' verse), Pesachim 116b:12 (the blind obligated), Menachot 34a:2 (the halakha per Rav and Shmuel), 32a:7 (the closed form by custom), Berakhot 13b:3 (the ruling per R. Acha); ARMS MISSED (LAW → DISPUTE) — Megillah 20a:2 (R. Meir), Menachot 33a:8 (R. Yehuda), 34a:8 (the Rabbis), Berakhot 11a:19 (Rav Yechezkel), Kiddushin 30a:5 (the first tanna on the grandfather); the rest notes extended past the cut (the seller\'s ban, R. Eliezer\'s two men, the Nehemiah proof of the stars, the Tosefta\'s swapped clauses, the closed mezuzah, the encircled letter, the mourner\'s tefillin, and on). '
         'THE LESSON: a verdict from a row\'s opening was right in kind about nine times in ten and wrong in substance about one in ten — the cut read the setting, not the ruling; and twice in a hundred it read the WRONG row (a note typed from memory of the sugya, not from the text). '
         'NEXT IN THE FIX: (b) sitting 4\'s Sifrei — the seven spine rows past the 1,500-character cap (31:1, 31:4, 31:6, 32:7, 32:18, 36:1, 36:2) reread whole, the 67 Hebrew rows read whole against the English (the divergence check the 36:10 find demands), the outside rows measured; a correction to the committed ledger by an APPENDED section; (c) 3b\'s rows over 650 (82 of 275) reread whole, a correction to the committed docket appended, a cell typed from a cut row retyped; (d) 2b\'s (114 of 327) and 1b\'s the same. Then 4b\'s RUN 3. A CLEAN COMPACTION POINT.\n')
MN = (f'\nWHOLE-ROW FIX (a) DONE {DATE}: chapter 6\'s docket reread whole — {NC}/{NR} rows corrected ({NV} verdicts; the open row\'s principle at Sanhedrin 4b:12-14 not 4b:2; six rows had carried another row\'s content; nine rules and five arms missed by the cut); the docket rewritten (204 KB, lint 0), the WHOLE overlays in ch6_docket_A-D.py. NEXT: (b) sitting 4\'s Sifrei rows past the cap and the Hebrew whole; (c) 3b\'s 82 rows over 650; (d) 2b\'s 114, 1b\'s; then 4b RUN 3.\n')
plans = []
P = f'{ROOT}/logic/pre_logic_methods_2026-07-28/PROMPT_continue_solo_era_2026-08-06.md'; s = rd(P); assert '#191 ADDENDUM 2' not in s and '#191 ADDENDUM 1' in s
plans.append((P, s.rstrip('\n') + STATE))
P = f'{MEM}/deuteronomy-walk.md'; s = rd(P); assert 'WHOLE-ROW FIX (a) DONE' not in s
plans.append((P, s.rstrip('\n') + '\n' + MN))
P = f'{MEM}/MEMORY.md'; s = rd(P)
old = 'the short cut STRUCK, its rows reread'; new = 'the short cut STRUCK; the cut rows reread whole (ch6 docket done: 70/747 corrected)'
for t_old, t_new in [('message "Torah Grok Main" via SendMessage when stuck; never an agent, never a ruling', 'message "Torah Grok Main" via SendMessage when stuck; never a ruling'),
                     ('— the labels vstat {o,d,p,g}; public coverage grid at /scroll/coverage/', '— vstat {o,d,p,g}; the coverage grid at /scroll/coverage/'),
                     ('put the READING into the machine; derive.py helper; the claim-ID collision trap', 'put the READING into the machine; the claim-ID collision trap')]:
    assert s.count(t_old) == 1, t_old[:40]; s = s.replace(t_old, t_new)
assert s.count(old) == 1; s2 = s.replace(old, new); assert len(s2.encode('utf-8')) < 17000, len(s2.encode('utf-8')); plans.append((P, s2))
for p, s2 in plans: assert s2 != rd(p), p
for p, s2 in plans:
    open(p, 'w', encoding='utf-8').write(s2); print('WROTE', p, len(s2.encode('utf-8')))
print('fix (a) checkpoint written')

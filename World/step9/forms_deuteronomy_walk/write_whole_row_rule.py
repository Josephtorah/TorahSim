import os as _os
_ROOT = _os.path.normpath(_os.path.join(_os.path.dirname(_os.path.abspath(__file__)), '..', '..', '..'))   # THE PORTABLE REPO (2026-09-15): the repo root from this file's own place
#!/usr/bin/env python3
# THE WHOLE-ROW RULE (owner-ruled 2026-09-17: "OK, never ever cut corners with the Talmud go back and fix the ones where the shortcut was taken and
# write it in the rules forever") — written into every record that carries the four-run rule's "short cut" clause, and into the memory. Every text
# built here; every anchor asserted once; the caps asserted (the recovery page <= 10,240 bytes, MEMORY.md < 17,000) before any file is opened.
import os, re, subprocess, sys
ROOT = _ROOT
MEM = os.path.expanduser('~/.claude/projects/-Users-Shared-TorahSim/memory')
CHECK = '--check' in sys.argv
def rd(p): return open(p, encoding='utf-8').read()
def one(s, old): assert s.count(old) == 1, (old[:60], s.count(old)); return True
plans = []
DATE = '2026-09-17'
WORD = 'OK, never ever cut corners with the Talmud go back and fix the ones where the shortcut was taken and write it in the rules forever'

RULE = ('THE WHOLE-ROW RULE (owner-ruled 2026-09-17: "never ever cut corners with the Talmud"): EVERY ROW OF THE SHELF — Talmud, Mishnah, Tosefta, '
        'midrash, Onkelos — IS READ WHOLE BEFORE ITS VERDICT IS TYPED. No character cap on a row, ever; no verdict from a row\'s opening; a range '
        'read is every row of the range whole. The four-run rule\'s "short cut" clause (2026-09-16) is STRUCK: a docket takes as many runs as its whole '
        'reading needs (the run count yields, the clean point after each run stands); a prior sitting\'s SCRIPT is still derived by sed and read where it '
        'differs — that economy is on our own text, never on the shelf\'s. THE CUTS TAKEN ARE REREAD WHOLE AND CORRECTED: a corrected verdict on an '
        'uncommitted docket by an overlay in its part (the cut\'s verdict kept beside it as the record); a correction to a committed ledger or docket by '
        'an APPENDED section (append-only); a cell typed from a cut row retyped from the whole one. THE MEASURE THAT RULED IT: the first forty rows of '
        'chapter 6\'s docket reread whole against their 170-character verdicts — two verdicts wrong, one row carrying another row\'s content, nine notes '
        'short of the row\'s point.')

# ---- 1. the memory: a new file, the index line, the cost-rules amendment, the oral-law note, the walk note
P = f'{MEM}/talmud-rows-whole.md'; assert not os.path.exists(P), P
plans.append((P, '''---
name: talmud-rows-whole
description: OWNER-RULED 2026-09-17 — never a cut on a shelf row; every Talmud/Mishnah/midrash row read WHOLE before its verdict; the short cut STRUCK, its rows reread
metadata:
  type: feedback
---

''' + RULE + '''

**Why:** the owner, 2026-09-17, after asking whether every case still runs by the Talmud and hearing where a cut could slip (the 170-character
docket read of chapter 6, the 650-character topic rows of 3b, the 1,500-character Sifrei rows of sitting 4): "''' + WORD + '''". The cut was my
economy inside the four-run rule (2026-09-16), one day old, and the whole read of forty rows showed what it missed.

**How to apply:** print a shelf row whole or not at all (the instruments take N = 100000, never 170 or 650); a docket run that runs long closes at a
clean point and continues — never at a cut; write "reread whole" and the counts (verdicts changed, notes extended) into a docket's header when a
correction pass is made; the four-run rule's text in every record carries the strike. Linked: [[cost-rules-no-polling]], [[full-oral-torah-law]],
[[deuteronomy-walk]].
'''))
P = f'{MEM}/MEMORY.md'; s = rd(P)
trims = [
 ('- [Machine transfer 2026-08-09](machine_transfer_2026-08-09.md) — moved Macs mid-run; all recovered; <repo-old> is sole truth',
  '- [Machine transfer 2026-08-09](machine_transfer_2026-08-09.md) — moved Macs mid-run; recovered'),
 ('- [Agent derivation trial](agent-derivation-trial.md) — REVOKED/BROADENED 2026-08-09: NO agents of any type, all work in the main thread; no task lists',
  '- [Agent derivation trial](agent-derivation-trial.md) — REVOKED 2026-08-09: NO agents, main thread only'),
 ('- [Grok full-control handoff](grok-full-control-handoff.md) — the handoff CLOSED 2026-08-06; SOLO MODE, never propose human-pasted relays',
  '- [Grok full-control handoff](grok-full-control-handoff.md) — CLOSED 2026-08-06; SOLO MODE'),
 ('- [Two-window workflow](two-window-workflow.md) — the CANON FLIP (⚠ 2026-09-01): Torah_Grok IS canon and FIRST — info flows TO TorahSim only; relay at owner direction',
  '- [Two-window workflow](two-window-workflow.md) — the CANON FLIP (⚠ 2026-09-01): Torah_Grok IS canon; info flows TO TorahSim only'),
 ('- [External review standing law](external-review-standing-law.md) — REVISED 2026-08-08: freeze review WAIVED for forward-era units — mechanical gates only',
  '- [External review standing law](external-review-standing-law.md) — REVISED 2026-08-08: freeze review WAIVED; mechanical gates only'),
 ('- [Triage deferral policy](triage-deferral-policy.md) — owner 2026-08-05: triages stay OPEN by default, never push for rulings',
  '- [Triage deferral policy](triage-deferral-policy.md) — owner 2026-08-05: triages stay OPEN by default'),
 ('- [Python rendering layer](python-rendering-layer.md) — every frozen unit gets logic/py_units/<uid>.py, embedded in its page; ritual step after freeze',
  '- [Python rendering layer](python-rendering-layer.md) — every frozen unit gets logic/py_units/<uid>.py; ritual step after freeze'),
 ('⚠ FOUR RUNS a sitting, a clean point each, ≤200k; the chain, the fast check, the sheet',
  '⚠ FOUR RUNS a sitting, a clean point each; NO CUT ON A SHELF ROW; the chain, the fast check, the sheet'),
 ('- [⚠ THE DEUTERONOMY WALK](deuteronomy-walk.md)',
  '- [⚠⚠ THE WHOLE-ROW RULE](talmud-rows-whole.md) — OWNER-RULED 2026-09-17: NEVER a cut on a shelf row; every Talmud/Mishnah/midrash row READ WHOLE before its verdict; the short cut STRUCK, its rows reread\n- [⚠ THE DEUTERONOMY WALK](deuteronomy-walk.md)'),
]
for a, b in trims: one(s, a); s = s.replace(a, b)
assert len(s.encode('utf-8')) < 17000, len(s.encode('utf-8')); plans.append((P, s))
P = f'{MEM}/cost-rules-no-polling.md'; s = rd(P)
a = 'Inside a run: the docket\'s rows read at a short cut; a prior sitting\'s form derived by sed and read only where it differs, never whole;'
b = ('Inside a run: EVERY SHELF ROW READ WHOLE — the "short cut" STRUCK 2026-09-17 on the owner\'s word ([[talmud-rows-whole]]; a docket takes the runs '
     'its whole reading needs); a prior sitting\'s form derived by sed and read only where it differs, never whole;')
one(s, a); plans.append((P, s.replace(a, b)))
P = f'{MEM}/full-oral-torah-law.md'; s = rd(P); assert 'WHOLE-ROW RULE' not in s
plans.append((P, s.rstrip('\n') + '\n\nTHE WHOLE-ROW RULE (owner-ruled 2026-09-17): every shelf row READ WHOLE before its verdict — no character cap, ever; the speed rulings above never cut a row, only the depth of the note. See [[talmud-rows-whole]].\n'))
P = f'{MEM}/deuteronomy-walk.md'; s = rd(P); assert 'WHOLE-ROW RULE' not in s
plans.append((P, s.rstrip('\n') + f'\nTHE WHOLE-ROW RULE {DATE} (the owner: "never ever cut corners with the Talmud … write it in the rules forever" — [[talmud-rows-whole]]): the short cut STRUCK; THE FIX IN PROGRESS: chapter 6\'s docket (747 rows at 170) reread whole in eight chunks with a WHOLE overlay per part (ch6_docket_common.apply_whole), the docket rewritten with the counts; then sitting 4\'s seven Sifrei rows past 1,500 characters and the Hebrew whole, 3b\'s topic rows past 650 (part C\'s fifteen and the rest over 650), 2b\'s and 1b\'s rows past 650 — corrections to committed files APPENDED. Then 4b\'s RUN 3.\n'))

# ---- 2. the recovery page (under 10,240 bytes)
P = f'{ROOT}/logic/pre_logic_methods_2026-07-28/RECOVERY_new_thread_2026-09-12.md'; s = rd(P)
a = 'gates chain, the records, the forms — each near 150-200k, never 600k; a reading sitting the same; the docket\'s rows at a short cut; a prior\n  form by sed, read where it differs.'
b = 'gates chain, the records, the forms — each near 150-200k, never 600k; a reading sitting the same; a prior form by sed, read where it differs.\n  ⚠ EVERY SHELF ROW READ WHOLE, NEVER A CUT (owner-ruled 2026-09-17); a docket takes the runs it needs.'
one(s, a); s = s.replace(a, b)
for a, b in [('- The Decalogue-schema question: the state doc\'s #185 addendum 1 and the map\'s tail (ON THE TABLE).', '- The Decalogue-schema question: the state doc\'s #185 addendum 1 (ON THE TABLE).'),
             ('The project review: §18.\n', '§18 the project review.\n'),
             (' "frontlets" defective where the ink is plene (the compile\'s open row); the large letters', ' "frontlets" defective where the ink is plene; the large letters'),
             ('- The whole standing-law text, the old staging form, the corpus bake: the addenda §3-4. The two sitting shapes in full: the addenda §5.', '- The standing laws in full, the old staging form, the corpus bake: the addenda §3-4; the two sitting shapes in full: §5.'),
             ('- NEXT ON HIS WORD: 4b RUN 3 — the types, the runner, the stitch, the tape to 10/10 (the map\'s "Sitting 4b … THE DESIGN"); then RUN 4.',
              '- IN FLIGHT: THE WHOLE-ROW FIX (the map\'s tail section) — the cut rows reread whole; then 4b RUN 3 (the map\'s "Sitting 4b … THE DESIGN").')]:
    one(s, a); s = s.replace(a, b)
assert len(s.encode('utf-8')) <= 10240, len(s.encode('utf-8')); plans.append((P, s))

# ---- 3. THE_STEPS, RECORD_FORMS, the map (the amendment note + the tail section), the state doc, THE_BRIEFING, the addenda
P = f'{ROOT}/THE_STEPS.md'; s = rd(P)
a = 'Two economies inside a run:\nthe docket\'s rows are read at a short cut, and a prior sitting\'s script is derived by substitution and read only where it differs. The reason is\nhis:'
b = ('One economy inside a run:\na prior sitting\'s script is derived by substitution and read only where it differs. The shelf\'s rows are never an economy: every row is read\n'
     'whole before its verdict is typed (Brian\'s rule, 2026-09-17: "never ever cut corners with the Talmud" — a short cut on the docket\'s rows stood one\n'
     'day, was struck, and its rows were reread whole). The reason for the four runs is\nhis:')
one(s, a); plans.append((P, s.replace(a, b)))
P = f'{ROOT}/World/step9/RECORD_FORMS.md'; s = rd(P)
a = 'Inside a run: the docket\'s rows read at a short cut; a prior sitting\'s form derived by sed and read only where it differs, never whole;'
b = 'Inside a run: EVERY SHELF ROW READ WHOLE (THE WHOLE-ROW RULE, owner-ruled 2026-09-17 — the short cut STRUCK; a docket takes the runs it needs); a prior sitting\'s form derived by sed and read only where it differs, never whole;'
one(s, a); plans.append((P, s.replace(a, b)))
P = f'{ROOT}/World/step9/DEUTERONOMY_WALK.md'; s = rd(P)
a = 'Inside a run: the docket\'s rows read at a short cut; a prior sitting\'s form derived by sed and read only where it differs, never whole; the state doc\'s checkpoint at each run\'s end names the next run\'s first step.'
assert s.count(a) == 1, s.count(a)
s = s.replace(a, a + ' [AMENDED 2026-09-17: "the docket\'s rows read at a short cut" STRUCK on the owner\'s word — THE WHOLE-ROW RULE, the map\'s tail.]')
assert s.rstrip('\n').endswith('→ the forms copied.'), s[-80:]
TAIL = (f'\n\n## THE WHOLE-ROW RULE (owner-ruled {DATE}: "{WORD}") — written between 4b\'s RUN 2 and RUN 3\n\n'
        + RULE + '\n\n'
        'WHERE THE CUT WAS TAKEN (measured on the record before the fix): (1) SITTING 4b — chapter 6\'s docket, all 747 rows printed at 170 characters '
        '(708 rows longer than the cut; the dump 407,226 characters); (2) SITTING 4 — the Sifrei\'s 67 spine rows printed with the English capped at 1,500 '
        'characters and the Hebrew\'s opening 150 (seven rows past the cap: 31:1, 31:4, 31:6, 32:7, 32:18, 36:1, 36:2; the ledger COMMITTED at a7955cc); '
        '(3) SITTING 3b — the docket\'s part C (rows 140-209) printed at 650 characters on the record (fifteen rows longer), the other parts\' print not on '
        'record (82 of 275 rows longer than 650; the docket COMMITTED at 7c8554e); (4) SITTINGS 2b AND 1b — the instrument existed with N a parameter and '
        'the print not on record (2b: 114 of 327 rows longer than 650; 1b\'s dump in the scratchpad); the link rows of 1b-3b "read whole" by their parts\' '
        'own headers. Before the four-run rule (2026-09-16) — the Numbers walk\'s dockets — every row was read whole from the dump by the parts\' own headers.\n\n'
        'THE FIX (in this order; each chunk\'s corrections on disk before the next is read): (a) chapter 6\'s docket reread whole in chunks of forty rows on '
        'ch6_docket_rows.py with N = 100000; each part carries a WHOLE overlay {address: (verdict, note)} applied by ch6_docket_common.apply_whole (the '
        'cut\'s verdict stays above it; a corrected note ends "[whole: what the cut missed]"); the docket (uncommitted) deleted and rewritten with the counts '
        'in its header; (b) sitting 4\'s seven Sifrei rows reread past the cap and the 67 Hebrew rows whole — a correction to the committed ledger an APPENDED '
        'section; (c) 3b\'s rows over 650 reread whole — a correction to the committed docket an appended section, a cell typed from a cut row retyped; '
        '(d) 2b\'s and 1b\'s rows over 650 the same. Then 4b\'s RUN 3 as designed.\n')
plans.append((P, s.rstrip('\n') + TAIL))
P = f'{ROOT}/logic/pre_logic_methods_2026-07-28/PROMPT_continue_solo_era_2026-08-06.md'; s = rd(P); assert 'WHOLE-ROW RULE' not in s and 'COMPACTION POINT #191' in s
plans.append((P, s.rstrip('\n') + f'\n\n#191 ADDENDUM 1 ({DATE} — THE WHOLE-ROW RULE, owner-ruled on "{WORD}", after the reread and his two questions: "Are you still running every case by the Talmud?" and "Did we recently change this or have we always done it this way?"). ' + RULE + ' WRITTEN INTO: the memory (talmud-rows-whole.md, the index, cost-rules-no-polling.md, full-oral-torah-law.md, deuteronomy-walk.md), the recovery page, THE_STEPS, RECORD_FORMS.md, the map (the four-run rule amended; the tail section "THE WHOLE-ROW RULE" with the cuts measured and the fix\'s order), THE_BRIEFING, the addenda §39. THE FIX IN FLIGHT: chapter 6\'s docket reread whole (chunks of forty; the WHOLE overlays), then sitting 4\'s Sifrei rows, 3b\'s, 2b\'s and 1b\'s rows over their cuts; then 4b\'s RUN 3. IF THIS COMPACTS MID-FIX: the map\'s tail section names the order; the parts\' WHOLE dicts show the chunks done (the last address corrected); continue at the next chunk of forty.\n'))
P = f'{ROOT}/THE_BRIEFING.md'; s = rd(P); assert 'THE WHOLE-ROW RULE' not in s
i = s.index('\n### '); assert i > 0
ENTRY = (f'\n### {DATE} — THE WHOLE-ROW RULE: NO CUT ON THE SHELF, EVER\n\n'
         'You asked whether every case still runs by the Talmud, and then where a case could slip. The answer was a cut I had made one day earlier inside the\n'
         'four-run rule: the docket\'s rows printed at their first 170 characters, the verdict typed from the opening. Reading the first forty rows of chapter 6\'s\n'
         'docket whole against those verdicts found two verdicts wrong, one row carrying another row\'s content, and nine notes short of the row\'s point. Your\n'
         'word: "never ever cut corners with the Talmud, go back and fix the ones where the shortcut was taken, and write it in the rules forever." So: every\n'
         'row of the shelf is read whole before its verdict, no character cap ever; a docket takes as many runs as that needs; the rows that were cut (chapter\n'
         '6\'s docket, the Sifrei rows of sitting 4 past 1,500 characters, the topic rows of chapters 5, 4 and 1-3 past 650) are reread whole and corrected, a\n'
         'committed file by an appended section. The economy that stays is on our own scripts, never on the shelf.\n')
plans.append((P, s[:i] + ENTRY + s[i:]))
P = f'{ROOT}/logic/pre_logic_methods_2026-07-28/RECOVERY_addenda_2026-09-12.md'; s = rd(P); assert '## 39.' not in s and '## 38.' in s
plans.append((P, s.rstrip('\n') + f'\n\n## 39. ADDENDUM ({DATE}, THE WHOLE-ROW RULE — owner-ruled between 4b\'s RUN 2 and RUN 3 on "{WORD}")\n\n' + RULE + '\n\nThe cuts measured and the fix\'s order: the map\'s tail section "THE WHOLE-ROW RULE"; the memory talmud-rows-whole.md; the state doc\'s #191 addendum 1.\n'))

for p, s2 in plans:
    if os.path.exists(p): assert s2 != rd(p), p
if CHECK:
    for p, s2 in plans: print('WOULD WRITE', p, len(s2.encode('utf-8')))
    sys.exit(0)
for p, s2 in plans:
    open(p, 'w', encoding='utf-8').write(s2); print('WROTE', p, len(s2.encode('utf-8')))
print('the whole-row rule written')

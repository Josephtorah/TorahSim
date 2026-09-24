#!/usr/bin/env python3
# THE DEUTERONOMY WALK 13b — AFTER THE COMMIT AND THE PUSH (2026-09-23, the owner's "Commit and push"): the records that named the tree uncommitted amended to name the
# commit (e824e52, pushed — 049f55c..e824e52 carried b0eaa56 and e824e52); every replacement asserted once; the caps asserted. These edits stay uncommitted until the next
# commit (the precedent: "the tree clean but for the docket gitlink and the commit's own records"). RUN FROM THE REPO ROOT.
import os, re, subprocess
ROOT = subprocess.check_output(['git', 'rev-parse', '--show-toplevel'], text=True).strip()
MEM = os.path.expanduser('~/.claude/projects/-Users-Shared-TorahSim/memory')
H = subprocess.check_output(['git', 'rev-parse', '--short', 'HEAD'], cwd=ROOT, text=True).strip(); assert H == 'e824e52', H
R = subprocess.check_output(['git', 'rev-parse', '--short', 'origin/main'], cwd=ROOT, text=True).strip(); assert R == H, R
def edit(p, reps, cap=None):
    q = p if p.startswith('/') else f'{ROOT}/{p}'; s = open(q, encoding='utf-8').read()
    for a, b in reps:
        assert s.count(a) == 1, (p, a[:60], s.count(a)); s = s.replace(a, b)
    if cap: assert len(s.encode('utf-8')) <= cap, (p, len(s.encode('utf-8')))
    open(q, 'w', encoding='utf-8').write(s); print('edited', p.replace(MEM, '<memory>'), len(s.encode('utf-8')))
edit('logic/pre_logic_methods_2026-07-28/RECOVERY_new_thread_2026-09-12.md', [
    ("(PUSHED through 049f55c; 15 COMMITTED b0eaa56 not pushed; 13b uncommitted).", "(PUSHED through e824e52 — 15 and 13b)."),
    ("- 13b DONE (#207 add. 5). NEXT ON HIS WORD: commit (<scratch>/commit_msg_ch15b.txt); push on \"push\"; ch 16's reading (16:1-22), two runs + tail.", "- 13b DONE, COMMITTED e824e52 AND PUSHED (#207 add. 5). NEXT ON HIS WORD: ch 16's reading (16:1-22), two runs + the tail.")], cap=10240)
edit(f'{MEM}/MEMORY.md', [
    ("ch 1-14 COMPILED AND PUSHED through 049f55c; 15 READ, FROZEN, COMMITTED b0eaa56 (not pushed); 13b DONE (91/91; 4 lines; 4 reuses; 27 params); uncommitted; commit next, ch 16", "ch 1-15 COMPILED AND PUSHED through e824e52 (13b: 91/91; 4 lines; 4 reuses; 27 params); NEXT: ch 16's reading")], cap=17000)
edit(f'{MEM}/deuteronomy-walk.md', [
    ('description: "COMMITTED THROUGH b0eaa56 (2026-09-22, chapter 15\'s reading; NOT PUSHED — pushed through 049f55c) — SITTING 13b DONE 2026-09-23', 'description: "COMMITTED AND PUSHED THROUGH e824e52 (2026-09-23 — chapter 15\'s reading b0eaa56 and 13b) — SITTING 13b DONE 2026-09-23'),
    ("13b uncommitted; NEXT on his word: the commit, the push on \\\"push\\\", then chapter 16\'s reading (16:1-22) in two runs + the tail\"", "NEXT on his word: chapter 16\'s reading (16:1-22) in two runs + the tail\""),
    ("UNCOMMITTED since b0eaa56: 13b (the message <scratch>/commit_msg_ch15b.txt). NEXT on his word: the commit; the push on\n\"push\"; chapter 16's reading", "COMMITTED e824e52 AND PUSHED 2026-09-23 on \"Commit and push\" (049f55c..e824e52 — b0eaa56 and e824e52). NEXT on his word:\nchapter 16's reading")])
edit('World/RESUME.md', [("# UNCOMMITTED since b0eaa56: 13b (the message at <scratch>/commit_msg_ch15b.txt). NEXT on the owner's word: the commit; the push on \"push\"; chapter 16's reading.", "# COMMITTED e824e52 AND PUSHED (2026-09-23, \"Commit and push\" — 049f55c..e824e52). NEXT on the owner's word: chapter 16's reading (16:1-22).")])
edit('THE_BRIEFING.md', [("{TAPE}; {CHAIN}. Uncommitted since b0eaa56.\n".replace('{TAPE}', "the tape 10/10 on its THIRD run (CU5's stale count read from the first run's print; the retype's apostrophes; the scan's ground fixed to exclude the daemon's own writes)").replace('{CHAIN}', "the gates chain in three passes (Q17 and the dependency gate's five demands from the first pass, the positions table by four workers, then all green)"), "the tape 10/10 on its third run; the chain in five passes. Committed e824e52 and pushed 2026-09-23.\n")])
D = 'logic/pre_logic_methods_2026-07-28/PROMPT_continue_solo_era_2026-08-06.md'; s = open(f'{ROOT}/{D}', encoding='utf-8').read(); assert '#207 ADDENDUM 5' in s and '#207 ADDENDUM 5 — NOTE' not in s
s = s.rstrip('\n') + "\n\n#207 ADDENDUM 5 — NOTE (2026-09-23, on the owner's \"Commit and push\"): COMMITTED e824e52 (221 files, 26478 insertions, 208 deletions — 13b whole: the runner, the forms, the records) AND PUSHED (049f55c..e824e52 — chapter 15's reading b0eaa56 and 13b; gh switched to Josephtorah for the push and back). The records naming the tree uncommitted amended (post_commit_ch15b.py — the recovery page, MEMORY.md, the walk note, RESUME, THE_BRIEFING's bullet, this NOTE); these edits ride the next commit. NEXT ON HIS WORD: CHAPTER 16's reading (16:1-22) in two runs + the tail.\n"
open(f'{ROOT}/{D}', 'w', encoding='utf-8').write(s); print('the state doc NOTE appended')

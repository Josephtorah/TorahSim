import os as _os
_ROOT = _os.path.normpath(_os.path.join(_os.path.dirname(_os.path.abspath(__file__)), '..', '..', '..'))   # THE PORTABLE REPO (2026-09-15): the repo root from this file's own place
#!/usr/bin/env python3
# THE DEUTERONOMY WALK sitting 22 — THE POST-PUSH RECORDS (2026-09-30, on the owner's "commit push" after the tail): the commit id READ FROM GIT, never typed; the three
# records that said UNCOMMITTED now say PUSHED (MEMORY.md's walk line, the recovery page's section 2, the walk memory's description and its last paragraph) and a PUSH line
# appended under the state doc's NOTE. Every text built whole before a file is opened; the caps and the lints asserted. RUN FROM THE REPO ROOT after the push.
import os, re, subprocess
ROOT = _ROOT
MEM = os.path.expanduser('~/.claude/projects/-Users-Shared-TorahSim/memory')
H = subprocess.check_output(['git', 'rev-parse', '--short', 'HEAD'], text=True).strip(); assert re.fullmatch(r'[0-9a-f]{7}', H), H
SUBJ = subprocess.check_output(['git', 'log', '-1', '--format=%s'], text=True); assert SUBJ.startswith('CHAPTER 34 READ AND FROZEN IN THE LEAN FORM (SITTING 22'), SUBJ[:80]
NP = len(subprocess.check_output(['git', 'diff-tree', '--no-commit-id', '--name-only', '-r', 'HEAD'], text=True).split())
RM = subprocess.check_output(['git', 'ls-remote', 'origin', 'main'], text=True).split()[0]; assert RM.startswith(H), (RM, H)
ST = [l for l in subprocess.check_output(['git', 'status', '--short'], text=True).split('\n') if l.strip()]; assert ST == [' M elijah_docket'], ST
SD = f'{ROOT}/logic/pre_logic_methods_2026-07-28/PROMPT_continue_solo_era_2026-08-06.md'; REC = f'{ROOT}/logic/pre_logic_methods_2026-07-28/RECOVERY_new_thread_2026-09-12.md'; IDX = f'{MEM}/MEMORY.md'; WALK = f'{MEM}/deuteronomy-walk.md'
def rd(p): return open(p, encoding='utf-8').read()
def sub1(t, a, b):
    assert t.count(a) == 1, (t.count(a), a[:80]); return t.replace(a, b)
idx = rd(IDX)
idx = sub1(idx, "32's compile PUSHED 472d2a3 (2026-09-29);", f"32's compile PUSHED 472d2a3 (2026-09-29), 33 READ + COMPILED and 34 READ PUSHED {H} (2026-09-30);")
idx = sub1(idx, "the pointer 33:21 -> 34:6 owed), UNCOMMITTED; 21b DONE", f"the pointer 33:21 -> 34:6 owed — PAID at 22), PUSHED {H}; 21b DONE")
idx = sub1(idx, "the long form in the file), UNCOMMITTED with 21 since 472d2a3; 22 (ch 34", f"the long form in the file), PUSHED {H}; 22 (ch 34")
idx = sub1(idx, "the ink 67 asserts 2/0/1/0), UNCOMMITTED with 21 and 21b since 472d2a3; NEXT: the commit on his word (21, 21b, 22), then 22b (the compile of 34) after a compaction — DEUTERONOMY CLOSES", f"the ink 67 asserts 2/0/1/0), PUSHED {H} 2026-09-30 (21 + 21b + 22 together, on 'commit push'); NEXT: 22b (the compile of 34) after a compaction — DEUTERONOMY CLOSES")
assert 'UNCOMMITTED' not in idx.split('THE DEUTERONOMY WALK](deuteronomy-walk.md)')[1].split('\n')[0]
assert len(idx.encode('utf-8')) <= 17000, len(idx.encode('utf-8'))
rec = rd(REC)
rec = sub1(rec, '## 2. WHERE IT STANDS (2026-09-30; #243 + its NOTE — sitting 22 DONE, newest)', f'## 2. WHERE IT STANDS (2026-09-30; #243 + its NOTE — sitting 22 DONE and PUSHED {H}, newest)')
rec = sub1(rec, '(1-32 PUSHED through 472d2a3; 33 READ + COMPILED, 34 READ — uncommitted); 34 not yet on the tape.', f'(ALL PUSHED through {H}, 2026-09-30 — 33 READ + COMPILED, 34 READ); 34 not yet on the tape.')
rec = sub1(rec, 'UNCOMMITTED with 21 and 21b since 472d2a3. NEXT: the commit on his word; then 22b (the compile of 34) — DEUTERONOMY CLOSES.', f'PUSHED {H} 2026-09-30 with 21 and 21b. NEXT: 22b (the compile of 34) after a compaction — DEUTERONOMY CLOSES.')
assert 'uncommitted' not in rec.lower().split('## 3.')[0]
assert len(rec.encode('utf-8')) <= 10240, len(rec.encode('utf-8'))
wk = rd(WALK)
wk = sub1(wk, 'UNCOMMITTED with 21 and 21b; NEXT the commit on his word, then 22b the compile — DEUTERONOMY CLOSES)', f'PUSHED {H} 2026-09-30 with 21 and 21b; NEXT 22b the compile — DEUTERONOMY CLOSES)')
wk = sub1(wk, 'UNCOMMITTED since 472d2a3 (21, 21b and 22 whole). NEXT on his word: the commit; then 22b', f'PUSHED {H} 2026-09-30 (21, 21b and 22 whole, on "commit push"). NEXT: 22b')
wk = wk.rstrip('\n') + f'\n\nPUSHED {H} 2026-09-30 — sittings 21, 21b and 22 together on the owner\'s "commit push" after the tail ({NP} paths in the commit; the message commit_msg_ch34.txt with 21b\'s and 21\'s folded beneath; the pre-commit home-path gate GREEN; origin/main at {H}; the tree clean but the elijah_docket gitlink, never staged). NEXT after a compaction ("Reread", then "Go"): 22b — the compile of chapter 34, and DEUTERONOMY CLOSES.\n'
sd = rd(SD); assert 'NOTE UNDER #243' in sd and f'PUSHED {H}' not in sd
PUSH = f'\n\nPUSHED (2026-09-30, on the owner\'s "commit push" after the tail of sitting 22): {H} — sittings 21, 21b and 22 together ({NP} paths in the commit, staged by the form; the message commit_msg_ch34.txt with 21b\'s and 21\'s messages folded beneath, the trailers once; the pre-commit home-path gate GREEN); origin/main at {H}; the tree clean but the elijah_docket gitlink (never staged). DEUTERONOMY 1:1-34:12 READ AND FROZEN AND PUSHED; 1-33 on the tape. NEXT after a compaction ("Reread", then "Go"): 22b — THE COMPILE OF CHAPTER 34, and DEUTERONOMY CLOSES. POST-COMPACTION REREADS: the recovery page, the map\'s newest section ("Sitting 22 — CHAPTER 34 — AS BUILT — LEAN"), MEMORY.md; then #243, its NOTE and this line.\n'
for txt in (idx, rec, wk, PUSH): assert os.path.expanduser('~') not in txt and '/private/tmp' not in txt and not re.search('[' + chr(0x5d0) + '-' + chr(0x5ea) + ']', PUSH)
def lint(p): r = subprocess.run(['python3', f'{ROOT}/logic/solo_tools/gloss_lint.py', p], capture_output=True, text=True); return int(re.search(r'(\d+) flag', r.stdout).group(1))
L0 = {os.path.basename(p): lint(p) for p in (SD, REC, IDX, WALK)}
open(IDX, 'w', encoding='utf-8').write(idx); open(REC, 'w', encoding='utf-8').write(rec); open(WALK, 'w', encoding='utf-8').write(wk); open(SD, 'a', encoding='utf-8').write(PUSH)
L1 = {os.path.basename(p): lint(p) for p in (SD, REC, IDX, WALK)}; assert L0 == L1, (L0, L1)
print(f'THE POST-PUSH RECORDS WRITTEN: {H} ({NP} paths; origin/main {RM[:12]}); MEMORY.md {len(idx.encode())} bytes; the recovery page {len(rec.encode())}; the walk note {len(wk.encode())}; the PUSH line {len(PUSH.encode())}; the lints unmoved {L1}')

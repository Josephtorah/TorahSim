import subprocess, sys, os
ROOT = subprocess.check_output(['git','rev-parse','--show-toplevel'], text=True).strip()
MEM = os.path.expanduser('~/.claude/projects/-Users-Shared-TorahSim/memory')
CID = subprocess.check_output(['git','rev-parse','--short','HEAD'], text=True, cwd=ROOT).strip()
assert CID == 'b0eaa56', CID
PARENT = subprocess.check_output(['git','rev-parse','--short','HEAD~1'], text=True, cwd=ROOT).strip()
assert PARENT == '049f55c', PARENT
NPATHS = len(subprocess.check_output(['git','diff-tree','--no-commit-id','--name-only','-r','HEAD'], text=True, cwd=ROOT).split())
REC = f'{ROOT}/logic/pre_logic_methods_2026-07-28/RECOVERY_new_thread_2026-09-12.md'
STATE = f'{ROOT}/logic/pre_logic_methods_2026-07-28/PROMPT_continue_solo_era_2026-08-06.md'
RESUME = f'{ROOT}/World/RESUME.md'
MEMI = f'{MEM}/MEMORY.md'
WALK = f'{MEM}/deuteronomy-walk.md'
TOUCH = [REC, STATE, RESUME, MEMI, WALK]
def rd(p): return open(p, encoding='utf-8').read()
def wr(p, s): open(p, 'w', encoding='utf-8').write(s)
def lint(p):
    r = subprocess.run([sys.executable, f'{ROOT}/logic/solo_tools/gloss_lint.py', p], capture_output=True, text=True, cwd=ROOT)
    import re
    m = re.findall(r'(\d+)\s+flag', r.stdout + r.stderr)
    return int(m[-1]) if m else (0 if r.returncode == 0 else -1)
def rep1(p, old, new):
    s = rd(p); n = s.count(old)
    assert n == 1, (p, n, old[:60])
    wr(p, s.replace(old, new))
BEFORE = {p: lint(p) for p in TOUCH}
print('LINT BEFORE', {os.path.basename(p): v for p, v in BEFORE.items()})
# the recovery page (section 2)
rep1(REC, '## 2. WHERE IT STANDS (2026-09-22, after sitting 13; the state doc #206 addendum 3 the newest)',
          '## 2. WHERE IT STANDS (2026-09-22, after sitting 13 and its commit; the state doc #206 addendum 3\'s commit note the newest)')
rep1(REC, '15 READ AND FROZEN (UNCOMMITTED).', f'15 READ AND FROZEN (COMMITTED {CID}, NOT PUSHED).')
rep1(REC, '- UNCOMMITTED since 049f55c: 15 (<scratch>/commit_msg_ch15.txt). NEXT ON HIS WORD: the commit; then 13b.',
          f'- COMMITTED {CID} (2026-09-22, no push; 1-14 pushed through 049f55c). NEXT ON HIS WORD: 13b.')
n = len(rd(REC).encode()); assert n <= 10240, n
# the memory index line
rep1(MEMI, '15 READ AND FROZEN (sitting 13 — two runs + the tail; 132/132; the 229th unit); UNCOMMITTED; NEXT: the commit, then 13b',
           f'15 READ, FROZEN AND COMMITTED {CID}, NOT PUSHED (sitting 13 — two runs + the tail; 132/132; the 229th unit); NEXT: 13b')
m = len(rd(MEMI).encode()); assert m < 17000, m
# the walk note: the description, then the appended line
rep1(WALK, 'UNCOMMITTED; NEXT on his word: the commit, then 13b', f'COMMITTED {CID}, not pushed; NEXT on his word: 13b')
WALKLINE = (f'COMMITTED {CID} on "Commit" (2026-09-22, NOT PUSHED) — sitting 13 alone ({PARENT}..{CID}; {NPATHS} paths; the home-path gate green at the hook); '
            'the records after the commit (the recovery page\'s section 2, the index line, this note and its description, RESUME\'s newest note, the state doc\'s commit note; '
            'the timing table re-copied into the forms with the note\'s and the commit\'s rows) ride 13b\'s commit. NEXT on the ruling: 13b, two runs + the tail — '
            'or the Decalogue-schema sitting first; the push on his word.\n')
s = rd(WALK); assert s.endswith('\n'); wr(WALK, s + WALKLINE)
# RESUME's newest note
rep1(RESUME, 'NEXT on the owner\'s word: the commit (<scratch>/commit_msg_ch15.txt — chapter 15 alone, uncommitted since 049f55c); then 13b —',
             f'COMMITTED {CID} on "Commit" (2026-09-22, not pushed; chapter 15 alone, {PARENT}..{CID}). NEXT on the owner\'s word: 13b —')
# the state doc: the commit note appended
NOTE = (f'\n#206 ADDENDUM 3 — THE COMMIT NOTE (2026-09-22, on the owner\'s "Commit" after the compaction and the rereads — the recovery page, the map\'s "Sitting 13 — CHAPTER 15 — AS BUILT", MEMORY.md, addendum 3 and its NOTE): '
        f'SITTING 13 COMMITTED {CID} ({PARENT}..{CID} — chapter 15 alone, {NPATHS} paths staged by the standing form, the docket gitlink left; the home-path gate GREEN at the hook; NOT PUSHED — "Commit" alone is no push). '
        'THE RECORDS AFTER THE COMMIT: the recovery page\'s section 2, the memory index line and the walk note (its description and a COMMITTED line), RESUME\'s newest note, this note; the timing table re-copied into the forms with the note\'s and the commit\'s rows — these ride 13b\'s commit. NOTHING MID-FLIGHT. '
        'NEXT ON HIS WORD: 13b, the compile of chapter 15, in two runs + the tail (RUN A the rereads, the measurements, the design, the probes to FAIL, the docket by the union rule — its own run past ~700 rows; RUN B the types, the runner, the tape to 10/10, the chain LAUNCHED; THE TAIL the records) — or the Decalogue-schema sitting first; the push when he says "push". '
        'POST-COMPACTION REREADS unchanged: the recovery page, the map\'s "Sitting 13 — CHAPTER 15 — AS BUILT", MEMORY.md; then #206 addendum 3, its NOTE and this commit note.\n')
s = rd(STATE); assert s.endswith('\n') and s.rstrip().endswith('then #206 addendum 3 and this NOTE.'); wr(STATE, s + NOTE)
AFTER = {p: lint(p) for p in TOUCH}
print('LINT AFTER ', {os.path.basename(p): v for p, v in AFTER.items()})
for p in TOUCH: assert AFTER[p] <= BEFORE[p], (p, BEFORE[p], AFTER[p])
print(f'WRITTEN: commit {CID} ({PARENT}..{CID}, {NPATHS} paths); the recovery page {n} B; MEMORY.md {m} B; the walk note {len(rd(WALK).encode())} B')

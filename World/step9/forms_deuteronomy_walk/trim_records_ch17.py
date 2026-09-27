import os as _os
_ROOT = _os.path.normpath(_os.path.join(_os.path.dirname(_os.path.abspath(__file__)), '..', '..', '..'))   # THE PORTABLE REPO (2026-09-15): the repo root from this file's own place
#!/usr/bin/env python3
# THE DEUTERONOMY WALK sitting 15 — CHAPTERS 17-18 (LEAN, 2026-09-24): THE TRIM BEFORE THE SITTING WRITES — MEMORY.md within a few bytes of its 17,000 cap
# and the recovery page within twenty of 10,240 (the #210 READY note: "the next sitting trims both before it writes"). MEMORY.md: THE LOOP RULING's index line
# (the longest, 4,453 bytes) MOVED VERBATIM into the-loop-ruling.md under its own dated header (step9-exam-era.md's precedent, 2026-09-08 and 2026-09-12) and
# replaced by a short pointer; the recovery page: the chapter-15 line of section 2 dropped (14/14b the newest) and section 5's parenthetical shortened.
# Every size read from the file after the write; the lint on both (baselines MEMORY.md 4, the page 0). RUN FROM THE REPO ROOT.
import os, re, subprocess, sys
ROOT = _ROOT
MEM = os.path.expanduser('~/.claude/projects/-Users-Shared-TorahSim/memory')
mp = f'{MEM}/MEMORY.md'; lp = f'{MEM}/the-loop-ruling.md'; rp = f'{ROOT}/logic/pre_logic_methods_2026-07-28/RECOVERY_new_thread_2026-09-12.md'
m = open(mp, encoding='utf-8').read(); before_m = len(m.encode('utf-8'))
lines = m.split('\n')
li = [i for i, l in enumerate(lines) if l.startswith('- [⚠⚠ THE LOOP RULING](the-loop-ruling.md)')]
assert len(li) == 1, li
old = lines[li[0]]; assert len(old.encode('utf-8')) > 4000, len(old.encode('utf-8'))
loop = open(lp, encoding='utf-8').read()
assert 'AS IT STOOD ON 2026-09-24' not in loop
hdr = "\n\n## THE MEMORY.md INDEX LINE AS IT STOOD ON 2026-09-24 (moved here verbatim at sitting 15's trim — MEMORY.md was 16,929 of its 17,000 bytes; the index now carries a short pointer)\n\n"
open(lp, 'w', encoding='utf-8').write(loop.rstrip('\n') + hdr + old + '\n')
new = ("- [⚠⚠ THE LOOP RULING](the-loop-ruling.md) — OWNER-RULED PERMANENT 2026-09-09: the step-9 engine is a RUNNING SIMULATION WITH MEMORY (map World/step9/THE_LOOP.md): "
       "steps 1-7 BUILT (the sink, the index, installation, the cursor, scenarios, write-as-you-go, the stepper, the port), D7's MERGE done 2026-09-14 — ONE DATABASE World/journal/data/world.sqlite; "
       "the board (world_board.py + world_board.html; it drives the engine), the checkpoints as they fall (checkpoint_positions.yaml), the portable repo and the username scrub (2026-09-15; the folder /Users/Shared/TorahSim), THE TENT closed 2026-09-09; "
       "⚠ STANDING DUTY: THE_LOOP.md \"TO FINISH THE LOOP — THE LIST\" kept current at every loop sitting and echoed in the reply; ⚠ probes only under WORLD_JOURNAL_DIR while an engine is live; STEP 6 THE READBACK owed (design at Deuteronomy). "
       "The full index line as it stood on 2026-09-24 (D1-D33, the sittings, the owner's decisions) is IN THE FILE, moved verbatim at sitting 15's trim.")
lines[li[0]] = new
m2 = '\n'.join(lines); open(mp, 'w', encoding='utf-8').write(m2)
r = open(rp, encoding='utf-8').read(); before_r = len(r.encode('utf-8'))
drop = "- SITTING 13/13b (ch 15): 132 sources; release_firstborn 91/91; PUSHED e824e52.\n"
assert r.count(drop) == 1; r = r.replace(drop, '')
o5 = '## 5. THE SITTING SHAPES (the long forms: the addenda\'s section 5; the newest instances: the map\'s "Sitting 13b" and "Sitting 13")'
n5 = '## 5. THE SITTING SHAPES (the long forms: the addenda §5; the newest instances the map\'s "Sitting 14" and "Sitting 14b", lean)'
assert r.count(o5) == 1; r = r.replace(o5, n5)
open(rp, 'w', encoding='utf-8').write(r)
after_m = os.path.getsize(mp); after_r = os.path.getsize(rp)
print(f'MEMORY.md {before_m} -> {after_m} bytes (cap 17000); the recovery page {before_r} -> {after_r} bytes (cap 10240); the-loop-ruling.md {os.path.getsize(lp)} bytes')
assert after_m < 17000 - 3000 and after_r < 10240 - 100
for f, base in ((mp, 4), (rp, 0)):
    p = subprocess.run([sys.executable, f'{ROOT}/logic/solo_tools/gloss_lint.py', f], capture_output=True, text=True)
    n = int(re.search(r'gloss_lint: (\d+) flag', p.stdout + p.stderr).group(1)); print(' lint', os.path.basename(f), n, 'baseline', base); assert n == base, (f, n)
p = subprocess.run([sys.executable, f'{ROOT}/logic/solo_tools/scrub_home_paths.py', '--check'], capture_output=True, text=True); print(' home gate rc', p.returncode, (p.stdout + p.stderr).strip()[-120:])

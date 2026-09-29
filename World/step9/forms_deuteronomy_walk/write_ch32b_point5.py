import os as _os
_ROOT = _os.path.normpath(_os.path.join(_os.path.dirname(_os.path.abspath(__file__)), '..', '..', '..'))   # THE PORTABLE REPO (2026-09-15): the repo root from this file's own place
#!/usr/bin/env python3
# THE DEUTERONOMY WALK 20b (LEAN): THE CLEAN COMPACTION POINT AT THE TAIL'S THIRD PART — the state doc's #236 ADDENDUM 3, the recovery page's section-2 last bullet, MEMORY.md's
# walk line's tail — written in ONE call after the chain's third summary was read (green to the stamp, RED at the sweep's 900 s limit on the song's runner alone), the limit
# raised and the third tail job launched (the fourth pass from the stamp); every number READ FROM ITS PRINT (the third SUMMARY, the sweep's print, the limit's print, the timing
# table); the caps and the lints asserted. --check prints without writing. RUN FROM THE REPO ROOT.
import os, re, sys, subprocess
ROOT = _ROOT
SP = os.path.dirname(os.path.abspath(__file__)); MEM = os.path.expanduser('~/.claude/projects/-Users-Shared-TorahSim/memory')
CHECK = '--check' in sys.argv
SD = f'{ROOT}/logic/pre_logic_methods_2026-07-28/PROMPT_continue_solo_era_2026-08-06.md'; REC = f'{ROOT}/logic/pre_logic_methods_2026-07-28/RECOVERY_new_thread_2026-09-12.md'; MM = f'{MEM}/MEMORY.md'
def rd(p): return open(p, encoding='utf-8').read()
def R(pat, text, name, g=1):
    m = re.search(pat, text, re.M); assert m, (name, pat); return m.group(g)
done2 = rd(f'{SP}/ch32b_tail_chain2.DONE'); assert R(r'^runner rc=(\d+)$', done2, 'runner rc') == '0' and R(r'^chain rc=(\d+)$', done2, 'chain rc') == '1', done2
summ3 = rd(f'{SP}/ch32b_gates3_SUMMARY.txt'); STEPS3 = re.findall(r'^(PASS|FAIL|SKIP) (\w+)(?: rc=\d+)? \((\d+)s\)', summ3, re.M)
assert [(v, n) for v, n, _ in STEPS3] == [('PASS', 'tape'), ('PASS', 'probes'), ('PASS', 'daemon'), ('PASS', 'dependency'), ('PASS', 'build'), ('PASS', 'journal'), ('PASS', 'register'), ('PASS', 'positions'), ('PASS', 'checkpoint'), ('PASS', 'stamp'), ('FAIL', 'sweep')] and 'SKIP unmoved (an earlier step failed)' in summ3, STEPS3
CHAIN3 = sum(int(t) for _, _, t in STEPS3); POS_S = int([t for _, n, t in STEPS3 if n == 'positions'][0])
IC3 = R(r'^  ink_cache: (\d+/\d+)$', rd(f'{SP}/ch32b_gates3/probes.out'), 'the cache probe third'); assert IC3 == '8/8', IC3
POS = R(r'THE FALLS: (\d+ checkpoints? over \d+ pauses in \d+ s \(\d+ workers\))', rd(f'{SP}/ch32b_gates3/positions.out'), 'the positions')
sw3 = rd(f'{SP}/ch32b_gates3/sweep.out'); SWEEP3 = R(r'(\d+/\d+) runners green', sw3, 'sweep third'); SWT = R(r'^FAIL\s+cold_run_song_charge_nebo\.py rc=124\s+score=rc-only \(no score line printed\)\s+([\d.]+)s$', sw3, 'the song timed out')
SW_TOP = sorted(((float(t), n) for n, t in re.findall(r'^PASS\s+(cold_run_\w+)\.py rc=0\s+score=\d+/\d+\s+([\d.]+)s$', sw3, re.M)), reverse=True)[:3]; SW_TOP = '; '.join('%s %.1f s' % (n[9:], t) for t, n in SW_TOP)
SWTO = R(r'^the sweep limit (900 -> 2400) \(--timeout N\); three edits \| WRITTEN$', rd(f'{SP}/ch32b_sweep_timeout.out'), 'the limit')
tsv = rd(f'{SP}/ch32b_timing.tsv'); rows = [l.split('\t') for l in tsv.strip().split('\n') if l.split('\t')[1:2] and l.split('\t')[1].startswith('20b')]; NSTEP = len(rows); SECS = sum(int(r[2]) for r in rows)
assert not os.path.exists(f'{SP}/ch32b_tail_chain3.DONE'), 'the third job has ended — run the records writer, not this point'
for f in ('ch32b_tail_facts.py', 'ch32b_asbuilt.txt', 'write_ch32b_records.py', 'write_ch32b_commit_msg.py', 'copy_ch32_forms.py', 'ch32b_writers_edit3.out'): assert os.path.exists(f'{SP}/{f}'), f
assert 'WRITTEN' in rd(f'{SP}/ch32b_writers_edit3.out').split('\n')[-2:][0] + rd(f'{SP}/ch32b_writers_edit3.out'), 'the writers amended'
sd = rd(SD); assert '\n#236 ADDENDUM 2 (' in sd and '\n#236 ADDENDUM 3 (' not in sd and sd.find('\n#2', sd.index('\n#236 ADDENDUM 2 (') + 5) < 0
ADD = ('\n\n#236 ADDENDUM 3 (2026-09-29, at THE TAIL\'s third part — sitting 20b, on the owner\'s "Continue" in addendum 2\'s window (no compaction; /context 249.5k at his word); A CLEAN COMPACTION POINT WITH THE THIRD TAIL JOB RUNNING IN THE BACKGROUND): '
       'THE SECOND JOB\'S DONE FILE AND THE CHAIN\'S THIRD SUMMARY READ ONCE (runner rc=0, chain rc=1; ch32b_gates3_SUMMARY.txt; %d s): the tape PASS; the probes PASS — the import cache %s (THE SHARING GROUPS KEPT: the bindings\' retype the cause and the cure), every suite full; the daemon, dependency, build, journal and register --strict gates PASS; the positions PASS — %s, %d s in the summary (ten times the 548-657 s of sittings 14b-18b, as 19b\'s 6043 s at two workers: A FINDING, OWED a measurement of the step since 19b\'s marker); the checkpoint probes 7/7; the journal stamped; THE SWEEP FAIL — %s runners green, the song\'s runner alone rc=124 at the sweep\'s 900 s per-runner limit under INK_CACHE=0 (%s s; the slowest beside it %s — A RUNNER\'S SWEEP TIME IS ITS CALLEES\' FULL LOADS, and the song\'s forty-two ran past the limit set at the gates cut, 2026-09-19); the unmoved check skipped. '
       'THE LIMIT RAISED (patch_sweep_timeout_ch32b.py — run_cold_all.py\'s bound %s s as --timeout N, a dated comment and a docstring line; nothing the tape, the probes or the sweep\'s stamp key reads moved — the chain resumes at the stamp, 13b\'s precedent). '
       'THE THIRD TAIL JOB LAUNCHED in one background wrapper (ch32b_tail_chain3.sh; DONE file <scratch>/ch32b_tail_chain3.DONE): the chain\'s fourth pass --from stamp into ch32b_gates4 (the journal stamped, the sweep whole under the raised limit, the journal unmoved) — RUNNING, its SUMMARY copied to ch32b_gates4_SUMMARY.txt when it ends (the launch waited on a five-second smoke sweep of the tool that ran its runners one by one to their five-second kills — a Bash slip, harmless: the runners\' own processes, no stamp written by a red sweep). '
       'THE RECORDS\' WRITERS AMENDED again (edit_ch32b_tail3_writers.py — the facts module reads the third summary, the sweep\'s lines, the limit\'s print and the FOURTH summary; the AS BUILT\'s departure 17 and lessons 20-21; the records writer, the commit message, the copier). %d timed steps, %d machine seconds so far. '
       'NEXT: after the compaction, on his word — THE REREADS; the job\'s DONE file and SUMMARY read once (cat <scratch>/ch32b_tail_chain3.DONE; cat <scratch>/ch32b_gates4_SUMMARY.txt); if ALL GREEN (the stamp, the sweep, unmoved): from the repo root with PYTHONPATH the scratchpad, write_ch32b_records.py --check then without --check, write_ch32b_commit_msg.py, the forms (copy_ch32_forms.py), the home-path gate; if the sweep is RED: its print read, the demand filed; THE COMMIT ON HIS WORD ONLY. POST-COMPACTION REREADS: the recovery page, the map\'s newest section, MEMORY.md; then this addendum.'
       % (CHAIN3, IC3, POS, POS_S, SWEEP3, SWT, SW_TOP, SWTO, NSTEP, SECS))
rec = rd(REC); old = [l for l in rec.split('\n') if l.startswith('- SITTING 20b TAIL (ch 32 COMPILE, LEAN) at #236 + add. 2:')]; assert len(old) == 1, old
NEWB = ('- SITTING 20b TAIL (ch 32 COMPILE, LEAN) at #236 + add. 3: pass 3 green to the stamp (cache %s), the sweep\'s 900 s limit fell on the runner alone (raised to 2400); JOB 3 RUNNING (pass 4 from the stamp: the sweep, unmoved; DONE <scratch>/ch32b_tail_chain3.DONE). NEXT: its SUMMARY once; the records writer --check, then write; message; forms; commit on his word.' % IC3)
rec2 = rec.replace(old[0], NEWB); rec2 = rec2.replace('## 2. WHERE IT STANDS (2026-09-28; #236 + add. 2 — sitting 20b TAIL, newest)', '## 2. WHERE IT STANDS (2026-09-29; #236 + add. 3 — sitting 20b TAIL, newest)'); assert rec2 != rec
mm = rd(MM)
OLDS = [("readback 45/49 + the cache probe 7/8 RED (the reuses, the rain) — retyped from the print, the cache cleared; pass 2:", "readback 45/49 + cache 7/8 RED (the reuses, the rain — retyped; cleared); pass 2:"),
        ("(C6 — the runner bound its callees via globals(), unseen by the cache's skip: 129 retyped as assignments), the cache cleared again, pass 3 from the tape RUNNING in the background); NEXT: THE TAIL's third part after a compaction",
         "(C6 — the runner's globals() bindings, 129 retyped as assignments), cleared again; pass 3 green to the stamp, the sweep's 900 s limit fell on the song's runner (raised to 2400); pass 4 from the stamp RUNNING); NEXT: THE TAIL's fourth part after a compaction")]
mm2 = mm
for o, n in OLDS: assert mm2.count(o) == 1, o[:60]; mm2 = mm2.replace(o, n)
for t in (ADD, NEWB) + tuple(n for _, n in OLDS): assert not re.search(r'[֐-׿]', t) and os.path.expanduser('~') not in t and SP not in t
print('sizes: the old bullet %d -> %d bytes; the recovery page %d; MEMORY.md %d -> %d' % (len(old[0].encode()), len(NEWB.encode()), len(rec2.encode()), len(mm.encode()), len(mm2.encode())))
assert len(rec2.encode()) <= 10240 and len(mm2.encode()) < 17000, (len(rec2.encode()), len(mm2.encode()))
LINT = {}
for p in (SD, REC, MM):
    r = subprocess.run(['python3', f'{ROOT}/logic/solo_tools/gloss_lint.py', p], capture_output=True, text=True); LINT[os.path.basename(p)] = int(re.search(r'(\d+) flag', r.stdout).group(1))
print('THE POINT %s: addendum %d bytes; the recovery page %d; MEMORY.md %d; the lints before %s' % ('CHECKED' if CHECK else 'WRITTEN', len(ADD.encode()), len(rec2.encode()), len(mm2.encode()), LINT))
if not CHECK:
    open(SD, 'a', encoding='utf-8').write(ADD); open(REC, 'w', encoding='utf-8').write(rec2); open(MM, 'w', encoding='utf-8').write(mm2)
    L2 = {}
    for p in (SD, REC, MM):
        r = subprocess.run(['python3', f'{ROOT}/logic/solo_tools/gloss_lint.py', p], capture_output=True, text=True); L2[os.path.basename(p)] = int(re.search(r'(\d+) flag', r.stdout).group(1))
    assert L2 == LINT, (LINT, L2); print('every lint unmoved:', L2)

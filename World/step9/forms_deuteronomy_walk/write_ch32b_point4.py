import os as _os
_ROOT = _os.path.normpath(_os.path.join(_os.path.dirname(_os.path.abspath(__file__)), '..', '..', '..'))   # THE PORTABLE REPO (2026-09-15): the repo root from this file's own place
#!/usr/bin/env python3
# THE DEUTERONOMY WALK 20b (LEAN): THE CLEAN COMPACTION POINT AT THE TAIL'S SECOND HALF — the state doc's #236 ADDENDUM 2, the recovery page's section-2 last bullet, MEMORY.md's
# walk line's tail — written in ONE call after the chain's second summary was read (RED on the cache probe again), the cause read in the cache's code and the runner's source, the
# runner's callee bindings retyped as assignments and the second tail job launched; every number READ FROM ITS PRINT (the second SUMMARY, the cache probe print, the retype's print,
# the lint, the fifth graded run, the timing table); the caps and the lints asserted. --check prints without writing. RUN FROM THE REPO ROOT.
import os, re, sys, subprocess
ROOT = _ROOT
SP = os.path.dirname(os.path.abspath(__file__)); MEM = os.path.expanduser('~/.claude/projects/-Users-Shared-TorahSim/memory')
CHECK = '--check' in sys.argv
SD = f'{ROOT}/logic/pre_logic_methods_2026-07-28/PROMPT_continue_solo_era_2026-08-06.md'; REC = f'{ROOT}/logic/pre_logic_methods_2026-07-28/RECOVERY_new_thread_2026-09-12.md'; MM = f'{MEM}/MEMORY.md'
def rd(p): return open(p, encoding='utf-8').read()
def R(pat, text, name, g=1):
    m = re.search(pat, text, re.M); assert m, (name, pat); return m.group(g)
done = rd(f'{SP}/ch32b_tail_chain.DONE'); assert R(r'^probes rc=(\d+)$', done, 'probes rc') == '0' and R(r'^chain rc=(\d+)$', done, 'chain rc') == '1', done
summ2 = rd(f'{SP}/ch32b_gates2_SUMMARY.txt'); A2 = re.findall(r'^(PASS|FAIL|SKIP) (\w+)(?: rc=\d+)? \((\d+)s\)', summ2, re.M)
assert [(v, n) for v, n, _ in A2] == [('PASS', 'tape'), ('FAIL', 'probes'), ('PASS', 'daemon'), ('PASS', 'dependency'), ('PASS', 'build'), ('PASS', 'journal'), ('PASS', 'register')], A2
CHAIN2 = sum(int(t) for _, _, t in A2)
ic2 = rd(f'{SP}/ch32b_gates2/probe_ink_cache.out'); IC2 = R(r'^(\d+/8 probes)$', ic2, 'ink cache second'); C6G2 = R(r'^\s*FAIL C6 [^\n]*?: (added: \[.*\]; lost: \[.*\])$', ic2, 'C6 groups')
RB2 = R(r'(readback_probes: \d+/\d+)', rd(f'{SP}/ch32b_gates2/probe_readback.out'), 'readback second'); assert RB2.split(': ')[1].split('/')[0] == RB2.split('/')[1], RB2
RB1 = R(r'(readback_probes: \d+/\d+)', rd(f'{SP}/ch32b_gates/probe_readback.out'), 'readback first'); IC1 = R(r'^(\d+/8 probes)$', rd(f'{SP}/ch32b_gates/probe_ink_cache.out'), 'ink cache first')
fb = rd(f'{SP}/ch32b_runner_fbind.out'); NFB, FBL1, FBL2 = re.search(r"^edits (\d+) over lines (\d+)-(\d+); F's globals write removed \| WRITTEN$", fb, re.M).groups()
LINT2 = R(r'^gloss_lint: (\d+) flag\(s\)$', rd(f'{SP}/ch32b_runner_lint2.out'), 'lint'); assert LINT2 == '0'
MATRIX5 = R(r'^MATRIX: (\d+/\d+) cells match the answer sheet$', rd(f'{SP}/ch32_runner_run5.out'), 'the fifth run'); assert MATRIX5 == '72/72', MATRIX5
CLEAR2 = R(r'^(INK CACHE cleared)', rd(f'{SP}/ch32b_cache_clear2.out'), 'cleared again')
tsv = rd(f'{SP}/ch32b_timing.tsv'); rows = [l.split('\t') for l in tsv.strip().split('\n') if l.split('\t')[1:2] and l.split('\t')[1].startswith('20b')]
RUN5_S = [int(r[2]) for r in rows if 'fifth graded run' in r[1]]; assert len(RUN5_S) == 1; RUN5_S = RUN5_S[0]; NSTEP = len(rows); SECS = sum(int(r[2]) for r in rows)
assert not os.path.exists(f'{SP}/ch32b_tail_chain2.DONE'), 'the second job has ended — run the records writer, not this point'
for f in ('ch32b_tail_facts.py', 'ch32b_asbuilt.txt', 'write_ch32b_records.py', 'write_ch32b_commit_msg.py', 'copy_ch32_forms.py'): assert os.path.exists(f'{SP}/{f}'), f
sd = rd(SD); assert '\n#236 ADDENDUM 1 (' in sd and '\n#236 ADDENDUM 2 (' not in sd and sd.find('\n#2', sd.index('\n#236 ADDENDUM 1 (') + 5) < 0
ADD = ('\n\n#236 ADDENDUM 2 (2026-09-28, at THE TAIL\'s second half — sitting 20b, on the owner\'s "Reread and go" after the compaction at addendum 1; A CLEAN COMPACTION POINT WITH THE SECOND TAIL JOB RUNNING IN THE BACKGROUND): THE REREADS done (the recovery page, the map\'s newest section — the 20b design whole, MEMORY.md, #236 addendum 1). '
       'THE FIRST JOB\'S DONE FILE AND THE CHAIN\'S SECOND SUMMARY READ ONCE (probes rc=0, chain rc=1; ch32b_gates2_SUMMARY.txt; %d s): the tape PASS; the probes FAIL ON ONE SUITE — the import cache %s, C6 AGAIN with OTHER groups (%s; %s and every other suite green); the daemon, dependency, build, journal and register --strict gates PASS; the long steps skipped. '
       'THE CAUSE READ IN THE CACHE\'S CODE AND THE RUNNER\'S SOURCE (ink_cache.py\'s skip rule — a statement is skipped and its names restored only when its ast Store targets are recorded; ink_cache_probes.py\'s C6 — the sharing groups by id over the runners\' module-level lists, dicts and sets, TWO of the differing groups printed and the sets unordered, so the printed groups differ between passes; the runner\'s helper F): the song\'s runner bound its callees\' values through F(\'NAME\', value) — a helper writing globals() — %s statements over the runner\'s lines %s-%s; these statements have no Store target, so each RAN on the cached path and held the LIVE callee object while the older runners\' names for the same DATA rows (covenant_return_charge\'s JR_FOUR, JR_DEATH and OH_CHAIN; refuge_war_family\'s and courts_prophet\'s RG_ONE) were restored copies: the sharing groups lost, and no cache clear reaches it (18b\'s lesson 11 is the harvest\'s half of the rule; this its binding half — the AS BUILT\'s lesson 19, departure 16). '
       'THE RETYPE BY AST (patch_runner_fbind_ch32b.py — --check then written: every module-level F(\'NAME\', expr) became NAME = expr; F(\'NAME\', NAME), F\'s globals() write removed with a comment above the def; the file parses; the lint %s flags). '
       'THE SECOND TAIL JOB LAUNCHED in one background wrapper (ch32b_tail_chain2.sh; DONE file <scratch>/ch32b_tail_chain2.DONE): (1) the runner\'s fifth graded run — MATRIX %s in %d s (a miss for its module alone; the wrapper read the MATRIX line before going on); (2) %s whole again; (3) the chain\'s third pass from the tape into ch32b_gates3 (the positions at four workers) — RUNNING, its SUMMARY copied to ch32b_gates3_SUMMARY.txt when it ends. '
       'THE RECORDS\' WRITERS AMENDED while the job runs (edit_ch32b_tail2_writers.py — the facts module reads the second summary, the C6 groups, the retype\'s print, the fifth run and the THIRD summary; the AS BUILT template\'s departure 16 and lesson 19 and its tail told whole; the records writer\'s NOTE, debt line, recovery section and memory line; the commit message — the script wrote its four files and tripped on its own last check, an f-string being an ast.JoinedStr, not a Constant; the copier\'s lists by edit_ch32b_copier_lists.py with the check corrected). %d timed steps, %d machine seconds so far. '
       'NEXT: after the compaction, on his word — THE REREADS; the job\'s DONE file and SUMMARY read once (cat <scratch>/ch32b_tail_chain2.DONE; cat <scratch>/ch32b_gates3_SUMMARY.txt); if ALL GREEN: from the repo root with PYTHONPATH the scratchpad, write_ch32b_records.py --check then without --check, write_ch32b_commit_msg.py, the forms (copy_ch32_forms.py), the home-path gate; if a step is RED: the demand read from its print and filed, then a pass from the tape again (the cache cleared first if a runner changed); THE COMMIT ON HIS WORD ONLY. POST-COMPACTION REREADS: the recovery page, the map\'s newest section, MEMORY.md; then this addendum.'
       % (CHAIN2, IC2, C6G2, RB2, NFB, FBL1, FBL2, LINT2, MATRIX5, RUN5_S, CLEAR2, NSTEP, SECS))
rec = rd(REC); old = [l for l in rec.split('\n') if l.startswith('- SITTING 20b TAIL (ch 32 COMPILE, LEAN) at #236 + add. 1:')]; assert len(old) == 1, old
NEWB = ('- SITTING 20b TAIL (ch 32 COMPILE, LEAN) at #236 + add. 2: pass 2 — cache C6 RED again (the runner bound callees via globals(): %s retyped as assignments); JOB 2 RUNNING (run %s; cache cleared; pass 3 from the tape; DONE <scratch>/ch32b_tail_chain2.DONE). NEXT: its SUMMARY once; the records writer --check, then write; message; forms; commit on his word.' % (NFB, MATRIX5))
rec2 = rec.replace(old[0], NEWB); rec2 = rec2.replace('## 2. WHERE IT STANDS (2026-09-28; #236 + add. 1 — sitting 20b TAIL, newest)', '## 2. WHERE IT STANDS (2026-09-28; #236 + add. 2 — sitting 20b TAIL, newest)'); assert rec2 != rec
mm = rd(MM)
OLDT = "the chain's first pass: %s + the cache probe %s RED (the reuses, the rain) — retyped from the print, the cache cleared, the second pass from the tape RUNNING in the background); NEXT: THE TAIL's second half after a compaction (the job's SUMMARY once, the records, the message, the forms), then the commit on his word" % (RB1.replace('readback_probes: ', 'readback '), IC1.replace(' probes', ''))
assert mm.count(OLDT) == 1, mm.count(OLDT)
NEWT = "the chain's first pass: %s + the cache probe %s RED (the reuses, the rain) — retyped from the print, the cache cleared; pass 2: the cache probe %s RED AGAIN (C6 — the runner bound its callees via globals(), unseen by the cache's skip: %s retyped as assignments), the cache cleared again, pass 3 from the tape RUNNING in the background); NEXT: THE TAIL's third part after a compaction (the SUMMARY once, the records, the message, the forms), then the commit on his word" % (RB1.replace('readback_probes: ', 'readback '), IC1.replace(' probes', ''), IC2.replace(' probes', ''), NFB)
OLDO = "20b OPENED 2026-09-28 on 'continue' in the tail's window (the exam rows 24 citations and the recon printed, UNREAD — RUN A proper after a compaction, 19b's lesson 1); "; assert mm.count(OLDO) == 1
mm2 = mm.replace(OLDT, NEWT).replace(OLDO, "20b OPENED 2026-09-28 on 'continue' (RUN A proper after a compaction, 19b's lesson 1); ")
for t in (ADD, NEWB, NEWT): assert not re.search(r'[֐-׿]', t) and os.path.expanduser('~') not in t and SP not in t
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

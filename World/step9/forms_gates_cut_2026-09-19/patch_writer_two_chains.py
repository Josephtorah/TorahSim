import re, ast
P = '<scratch>/write_gates_cut_records.py'; s = open(P, encoding='utf-8').read()
R = []
R.append(("CHAIN = os.path.join(SP, 'gates_cut_1')\n", "CHAIN = os.path.join(SP, 'gates_cut_1'); CHAIN2 = os.path.join(SP, 'gates_cut_2')   # the first chain (everything full) and the second (nothing moved — the steady state)\n"))
R.append(("""summ = R(os.path.join(CHAIN, 'SUMMARY.txt'))
steps = {}
for m in re.finditer(r'^(PASS|FAIL|SKIP) (\\w+)(?: rc=\\d+)? \\((\\d+)s\\) ?(.*)$', summ, re.M):
    steps[m.group(2)] = (m.group(1), int(m.group(3)), m.group(4).strip())
assert 'GATES CHAIN DONE — ALL GREEN' in summ, 'the chain is not ALL GREEN:\\n' + summ
""", """def parse_chain(d):
    summ = R(os.path.join(d, 'SUMMARY.txt')); st = {}
    for m in re.finditer(r'^(PASS|FAIL|SKIP) (\\w+)(?: rc=\\d+)? \\((\\d+)s\\) ?(.*)$', summ, re.M):
        st[m.group(2)] = (m.group(1), int(m.group(3)), m.group(4).strip())
    assert 'GATES CHAIN DONE — ALL GREEN' in summ, 'the chain %s is not ALL GREEN:\\n%s' % (d, summ)
    return st
steps, steps2 = parse_chain(CHAIN), parse_chain(CHAIN2)
"""))
R.append(("after = {s: steps[s][1] for s in ORDER}\ntotal_before = sum(BEFORE.values()); total_after = sum(after.values())\n",
          "after = {s: steps[s][1] for s in ORDER}; after2 = {s: steps2[s][1] for s in ORDER}\ntotal_before = sum(BEFORE.values()); total_after = sum(after.values()); total_after2 = sum(after2.values())\n"))
R.append(("""wall = None
try:
    t0 = R(os.path.join(SP, 'gates_cut_1.start')).strip(); log = R(os.path.join(SP, 'gates_cut_1.log'))
    t1 = [t for t in re.findall(r'^(\\d\\d:\\d\\d:\\d\\d)$', log, re.M) if t != t0][-1]   # the log prints the end stamp, then the start file's
    h = lambda t: int(t[:2]) * 3600 + int(t[3:5]) * 60 + int(t[6:8]); wall = h(t1) - h(t0)
except Exception as e: print('  (wall not read: %s)' % e)
""", """def wall_of(name):
    try:
        t0 = R(os.path.join(SP, name + '.start')).strip(); log = R(os.path.join(SP, name + '.log'))
        t1 = [t for t in re.findall(r'^(\\d\\d:\\d\\d:\\d\\d)$', log, re.M) if t != t0][-1]   # the log prints the end stamp, then the start file's
        h = lambda t: int(t[:2]) * 3600 + int(t[3:5]) * 60 + int(t[6:8]); return h(t1) - h(t0)
    except Exception as e: print('  (wall not read: %s)' % e); return None
wall, wall2 = wall_of('gates_cut_1'), wall_of('gates_cut_2')
"""))
R.append(("""pos = R(os.path.join(CHAIN, 'positions.out'))
pos_mode = re.search(r'^THE POSITIONS (FULL|INCREMENTAL): (.*)$', pos, re.M)
pos_falls = re.search(r'(\\d+) checkpoints over (\\d+) pauses', pos)
assert pos_falls, 'the positions print'
""", """pos = R(os.path.join(CHAIN, 'positions.out')); pos2 = R(os.path.join(CHAIN2, 'positions.out'))
pos_falls = re.search(r'(\\d+) checkpoints over (\\d+) pauses', pos); pos_falls2 = re.search(r'(\\d+) checkpoints over (\\d+) pauses in (\\d+) s \\((\\d+) workers\\)', pos2)
assert pos_falls and pos_falls2, 'the positions prints'
sweep2 = R(os.path.join(CHAIN2, 'sweep.out')); sw2 = re.search(r'^THE SWEEP (\\w+) \\(([^)]*)\\); jobs (\\d+); skipped (.*)$', sweep2, re.M)
assert sw2 and 'NOTHING TO GRADE' in sweep2, 'the second sweep should have nothing to grade'
"""))
R.append(("""N = dict(total_after=total_after, total_before=total_before, wall=wall, mins_after=mins(total_after), mins_wall=mins(wall) if wall else '?',
         sw=sw_sum.groups(), sw_mode=sw_mode.groups(), pos=pos_falls.groups(), pos_mode=pos_mode.groups() if pos_mode else ('?', '?'),""",
          """N = dict(total_after=total_after, total_before=total_before, wall=wall, mins_after=mins(total_after), mins_wall=mins(wall) if wall else '?',
         total_after2=total_after2, mins_after2=mins(total_after2), mins_wall2=mins(wall2) if wall2 else '?', pos2=pos_falls2.groups(), sw2=sw2.groups(),
         sw=sw_sum.groups(), sw_mode=sw_mode.groups(), pos=pos_falls.groups(), pos_mode=('WHOLE', 'the old sequential measure'),"""))
R.append(("""print('THE NUMBERS: chain %s (sum of steps; wall %s) against %s before; steps %s' % (N['mins_after'], N['mins_wall'], mins(total_before), {s: after[s] for s in ORDER}))""",
          """print('THE NUMBERS: chain 1 %s (sum of steps; wall %s), chain 2 %s (wall %s) against %s before; steps 1 %s; steps 2 %s' % (N['mins_after'], N['mins_wall'], N['mins_after2'], N['mins_wall2'], mins(total_before), {s: after[s] for s in ORDER}, {s: after2[s] for s in ORDER}))"""))
R.append(("about = '%d' % round(total_after / 60)\ntable = '\\n'.join('| %s | %s | %d | %s |' % (s, BEFORE.get(s, '—'), after[s], steps[s][2][:110]) for s in ORDER)\n",
          "about = '%d' % round(total_after2 / 60)\ntable = '\\n'.join('| %s | %s | %d | %d | %s |' % (s, BEFORE.get(s, '—'), after[s], after2[s], steps2[s][2][:100]) for s in ORDER)\n"))
# ---- 1. GATES_CHAIN AS RUN (the writer's own triple quotes inside: single-quote triples here) ----
R.append(('''## AS RUN — the first chain after the cut (%s, the same day; the six cuts built, then the chain once, ALL GREEN)

| step | seconds before | seconds after | the step's last line |
|---|---|---|---|
%s
| **total** | **%d (%s)** | **%d (%s)** | the wall clock %s |

THE SWEEP ran %s (%s) — no stamp existed, so the first sweep after the cut graded every runner (%s of %s at %s jobs; %s graded cells; %s s) and
wrote the stamp (%d runners, %d shared pieces); the next chain grades only what moved. THE POSITIONS ran %s (%s) — the old table had no regions,
so the first run measured every region (%s checkpoints over %s pauses) and wrote the table in its new form; the next chain asks only the regions
new or moved. The probes in parallel: %s. THE JOURNAL UNMOVED across the sweep (%s sources). The register gate from the snapshot (DECLARED %s,
DEBT %s, FAILS %s). Every verdict the last chain before the cut gave, this chain gave: the tape %s, the daemon gate %s daemons / %s functions,
the dependency gate %s edges / %s pointers, the journal gate %s kinds / %s rows, the sweep whole, the positions whole.

THE STEADY STATE (the chain at a compile sitting after this one): the sweep incremental (the new runner and its importers, ~3 min) and the
positions incremental (the new region only), so the chain nears the sum of its fixed steps — the tape, the probes, the journal, the checkpoint
probes — about nineteen minutes (estimated from the pieces measured after this chain: `checkpoint_positions.py --incremental` 145 s with nothing
moved, `run_cold_all.py --changed` 5 s with nothing moved; a compile moves one region and one runner).
""" % (TODAY, table, total_before, mins(total_before), total_after, N['mins_after'], N['mins_wall'], N['sw_mode'][0], N['sw_mode'][1], N['sw'][0], N['sw'][1], N['sw'][6], N['sw'][2], N['sw'][5],
       N['stamp_runners'], N['stamp_shared'], N['pos_mode'][0], N['pos_mode'][1], N['pos'][0], N['pos'][1],
       ', '.join('%s %s/%s' % (k, v[0], v[1]) for k, v in probes.items()), N['unm'], N['reg'][0], N['reg'][1], N['reg'][2], tape_score, N['dae'][0], N['dae'][1], N['dep'][0], N['dep'][1], N['jour'][0], N['jour'][1])''',
'''## AS RUN — two chains after the cut (%s, the same day; ALL GREEN both times)

The first chain: everything measured in full (no sweep stamp yet; the positions by the old sequential measure). The second chain, run after the
positions measure was rebuilt by workers and with NOTHING MOVED: the steady state a compile sitting will see.

| step | seconds before | the first chain | the second chain | the second chain's last line |
|---|---|---|---|---|
%s
| **total** | **%d (%s)** | **%d (%s)**, wall %s | **%d (%s)**, wall %s | |

THE FIRST CHAIN: the sweep %s (%s) — no stamp existed, so every runner was graded (%s of %s at %s jobs; %s graded cells; %s s) and the stamp
written (%d runners, %d shared pieces); the positions by the old sequential measure (%s checkpoints over %s pauses, 1,400 s of the block at 169
pauses). THE SECOND CHAIN: the sweep %s (%s) — NOTHING TO GRADE; the positions by %s workers, %s checkpoints over %s pauses in %s s. Both chains:
the probes in parallel (%s); THE JOURNAL UNMOVED across the sweep (%s sources); the register gate from the snapshot (DECLARED %s, DEBT %s,
FAILS %s); every verdict the last chain before the cut gave — the tape %s, the daemon gate %s daemons / %s functions, the dependency gate %s edges
/ %s pointers, the journal gate %s kinds / %s rows, the sweep whole, the positions whole.

THE STEADY STATE is the second chain: a compile sitting moves one runner (graded with its importers, a minute or two) and the positions are
always the whole measure by workers, so the chain stays near the second chain's total.

## THE FORM THAT WAS STRUCK — the incremental positions by regions (built, tested and struck %s)

The design above first cut the positions table INCREMENTALLY: the block's statements split into REGIONS (a prefix's letters — CU — its cp calls
and the helper statements beside them), each region with a digest, the table's rows kept while their region, the block's preamble and the tape
prefix (the lines minus the newest runner's) stood, only the moved regions asked at every pause. THE TEST: CU's digest altered in the table and
`--incremental` run — seven of CU's nine rows came out NOT YET: the region's checkpoints read helper names bound in OTHER regions (a partial run
skipped their binders). A dependency closure was added (every earlier statement binding a name the region reads, transitively) and measured
statically: CU's closure is 429 of the block's 630 statements, CC's 336 — the block is one chained computation, and a "partial" run is nearly
the whole run. The form was struck the same day, with its regions, digests and guards; what remains is the parse-once cache (`_cp_block`) and
the WHOLE measure by N workers (D36). THE LESSON: an incremental cut is only as good as the independence it assumes — measure the dependency
before building the guard.
""" % (TODAY, table, total_before, mins(total_before), total_after, N['mins_after'], N['mins_wall'], total_after2, N['mins_after2'], N['mins_wall2'],
       N['sw_mode'][0], N['sw_mode'][1], N['sw'][0], N['sw'][1], N['sw'][6], N['sw'][2], N['sw'][5], N['stamp_runners'], N['stamp_shared'], N['pos'][0], N['pos'][1],
       N['sw2'][0], N['sw2'][1], N['pos2'][3], N['pos2'][0], N['pos2'][1], N['pos2'][2],
       ', '.join('%s %s/%s' % (k, v[0], v[1]) for k, v in probes.items()), N['unm'], N['reg'][0], N['reg'][1], N['reg'][2], tape_score, N['dae'][0], N['dae'][1], N['dep'][0], N['dep'][1], N['jour'][0], N['jour'][1], TODAY)'''))
# ---- 2. THE_LOOP ----
R.append(("""  D36 THE INCREMENTAL POSITIONS — the checkpoints block parsed and compiled once per process; REGIONS (a prefix's letters) with source digests;
     checkpoints_partial(only=regions); the table keeps a row while its region's digest, the preamble's digest and the TAPE PREFIX (the lines
     minus the newest runner's) stand; --full remeasures everything.
""", """  D36 THE POSITIONS BY WORKERS — checkpoint_positions.py --jobs N: N workers, each stepping the WHOLE tape in its own journal folder (the live
     base copied in, so the replay stays the audit) and asking the block at pause i where i mod N is its number; the parent merges the pauses
     (every pause asked by exactly one worker; the workers' verses, ordinals and days asserted equal) and takes the falls. The table is always
     the WHOLE measure. (An incremental form by regions was built, tested against a moved region and STRUCK the same day — seven of CU's nine
     rows came out NOT YET: a region's checkpoints read helpers bound across most of the block; the record in GATES_CHAIN.md.)
"""))
R.append(("""AS RUN: the chain once after the build, ALL GREEN in %s (wall %s) against ninety minutes — every verdict the chain before the cut gave. The first
sweep FULL (no stamp) and the first positions FULL (an old-form table); the steady state near nineteen minutes (the incremental positions 145 s and
the incremental sweep 5 s measured with nothing moved). THE RECORDS: GATES_CHAIN.md (the""", """AS RUN: two chains, ALL GREEN both — the first with everything in full, %s (wall %s); the second with nothing moved, %s (wall %s) — against
ninety minutes; every verdict the chain before the cut gave. THE RECORDS: GATES_CHAIN.md (the"""))
R.append(('''memory's cost rules, the state doc's #197, the addenda §45; the forms in World/step9/forms_gates_cut_%s/. LESSONS: MEASURE BEFORE CUTTING
(the replay was never the cost); A CACHE IS KEYED ON THE SOURCES' DIGESTS, NEVER ON A DATE; A MISS FALLS BACK TO THE FULL WORK; A STAMP IS
WRITTEN BY A GREEN RUN ONLY; TWO WRITERS OF ONE FILE WRITE ATOMICALLY.
""" % (TODAY, N['mins_after'], N['mins_wall'], TODAY)''', '''memory's cost rules, the state doc's #197, the addenda §45; the forms in World/step9/forms_gates_cut_%s/. LESSONS: MEASURE BEFORE CUTTING
(the replay was never the cost); A CACHE IS KEYED ON THE SOURCES' DIGESTS, NEVER ON A DATE; A MISS FALLS BACK TO THE FULL WORK; A STAMP IS
WRITTEN BY A GREEN RUN ONLY; TWO WRITERS OF ONE FILE WRITE ATOMICALLY; AN INCREMENTAL CUT IS ONLY AS GOOD AS THE INDEPENDENCE IT ASSUMES —
TEST IT AGAINST A MOVED PIECE BEFORE TRUSTING IT (the regions form was struck by its own test).
""" % (TODAY, N['mins_after'], N['mins_wall'], N['mins_after2'], N['mins_wall2'], TODAY)'''))
# ---- 3. RESEARCH_LOG ----
R.append(('''in parallel; the journal gate's two replays concurrent; the positions table incremental by REGIONS under the tape-prefix guard; the sweep parallel
(--jobs) and incremental (--changed against sweep_stamp.json, a shared piece moved = full, the stamp by a green sweep only); the second journal
gate replaced by a digest of the live rows before and after the sweep. AS RUN: %s (wall %s), ALL GREEN, every verdict the old chain gave (the tape
%s; the sweep %s/%s, %s cells; the positions %s over %s pauses; the journal %s kinds, %s rows, UNMOVED; the register DECLARED %s / DEBT %s / FAILS %s).
THE LESSON: measure before cutting — the obvious cost (the replay) was not the cost; a cache keyed on a date lies, one keyed on the sources' digests
does not; a miss falls back to the full work, so the chain stays honest.
""" % (TODAY, N['mins_after'].upper(), N['mins_after'], N['mins_wall'], tape_score, N['sw'][0], N['sw'][1], N['sw'][2], N['pos'][0], N['pos'][1], N['jour'][0], N['jour'][1], N['reg'][0], N['reg'][1], N['reg'][2])''',
'''in parallel; the journal gate's two replays concurrent; the positions table measured WHOLE by eight workers (an incremental form by regions was
built, tested against a moved region and STRUCK the same day — seven of CU's nine rows NOT YET, the region's checkpoints reading helpers bound
across most of the block; the closure measured at 429 of 630 statements); the sweep parallel (--jobs) and incremental (--changed against
sweep_stamp.json, a shared piece moved = full, the stamp by a green sweep only); the second journal gate replaced by a digest of the live rows
before and after the sweep. AS RUN: the first chain %s (wall %s) with everything in full, the second %s (wall %s) with nothing moved — ALL GREEN
both, every verdict the old chain gave (the tape %s; the sweep %s/%s, %s cells; the positions %s over %s pauses; the journal %s kinds, %s rows,
UNMOVED; the register DECLARED %s / DEBT %s / FAILS %s). THE LESSONS: measure before cutting — the obvious cost (the replay) was not the cost; a
cache keyed on a date lies, one keyed on the sources' digests does not; a miss falls back to the full work; an incremental cut is only as good
as the independence it assumes — test it against a moved piece before trusting it.
""" % (TODAY, N['mins_after2'].upper(), N['mins_after'], N['mins_wall'], N['mins_after2'], N['mins_wall2'], tape_score, N['sw'][0], N['sw'][1], N['sw'][2], N['pos'][0], N['pos'][1], N['jour'][0], N['jour'][1], N['reg'][0], N['reg'][1], N['reg'][2])'''))
# ---- 4. THE_STEPS ----
R.append(('''them); the positions table asks only the checkpoints whose block changed. Every guard is a digest of the source, never a date: if anything moved,
the full work runs. The first chain after the cut took %s and gave every verdict the old one gave. Next: the commit on your word; then chapter 9.
""".rstrip('\\n') % (TODAY, N['mins_after']) + '\\n')''', '''them); the table of where every checkpoint falls is measured by eight workers at once instead of one. Every guard is a digest of the source,
never a date: if anything moved, the full work runs. One cut was built and thrown out the same day — asking only the changed checkpoints — because
a test showed the checkpoints lean on each other across the whole block, so a partial run was nearly the whole run; the table is always measured
whole. The first chain after the cut took %s with everything in full; the second, with nothing changed, %s; both gave every verdict the old one
gave. Next: the commit on your word; then chapter 9.
""".rstrip('\\n') % (TODAY, N['mins_after'], N['mins_after2']) + '\\n')'''))
# ---- 5. THE_BRIEFING ----
R.append(('''sweep runs eight at a time and grades only the runners that changed since the last green sweep; the checkpoint table asks only the block that
changed. What keeps it honest: every short cut is guarded by a digest of the source files it depends on, never a date, and a miss falls back to
the full work — change a shared piece and the whole sweep runs. The first chain after the cut took %s and gave every verdict the old one gave.
""" % (TODAY, N['mins_after'])''', '''sweep runs eight at a time and grades only the runners that changed since the last green sweep; the checkpoint table is measured by eight
workers at once. What keeps it honest: every short cut is guarded by a digest of the source files it depends on, never a date, and a miss falls
back to the full work — change a shared piece and the whole sweep runs. One cut was struck by its own test the same day (asking only the changed
checkpoints — they lean on each other across the whole block), which is the other half of honest: a short cut is tested against a moved piece
before it is trusted. The first chain after the cut took %s with everything in full; the second, with nothing changed, %s; every verdict the same.
""" % (TODAY, N['mins_after'], N['mins_after2'])'''))
R.append(("THE PROBES SIDE BY SIDE, THE SWEEP EIGHT AT A TIME AND ONLY WHAT MOVED, EVERY SHORT CUT GUARDED BY A DIGEST OF THE SOURCE** (%s, on your \"Yes make that change. It\\'s too long as it is\"; World/step9/GATES_CHAIN.md).\\n' % (N['mins_after'].upper(), TODAY)",
          "THE PROBES SIDE BY SIDE, THE SWEEP EIGHT AT A TIME AND ONLY WHAT MOVED, THE CHECKPOINT TABLE BY EIGHT WORKERS, EVERY SHORT CUT GUARDED BY A DIGEST OF THE SOURCE AND ONE STRUCK BY ITS OWN TEST** (%s, on your \"Yes make that change. It\\'s too long as it is\"; World/step9/GATES_CHAIN.md).\\n' % (N['mins_after2'].upper(), TODAY)"))
# ---- 6. RECORD_FORMS ----
R.append(("the positions print a mode line `THE POSITIONS FULL|INCREMENTAL: …`, the sweep a mode line", "the positions print `THE POSITIONS BY n WORKERS` and `THE FALLS: n checkpoints over n pauses in n s (n workers)`, the sweep a mode line"))
R.append(("the stamped sweep, the incremental positions; every short cut keyed on the sources' digests; GATES_CHAIN.md);\" % N['mins_after'])", "the stamped sweep, the positions by eight workers; every short cut keyed on the sources' digests; GATES_CHAIN.md);\" % N['mins_after2'])"))
# ---- 7. RESUME ----
R.append(("`--changed --jobs 8` against step9/sweep_stamp.json (a shared piece moved = full); the positions `--incremental` by regions; the second journal gate the\\n# UNMOVED digest; `gates_chain.sh <out> --full` for the whole work. NEVER a reader's replay under the live source name — the readers take the snapshot.\\n\" % N['mins_after'] + s",
          "`--changed --jobs 8` against step9/sweep_stamp.json (a shared piece moved = full); the positions `--jobs 8` (eight workers, the whole measure); the second\\n# journal gate the UNMOVED digest; `gates_chain.sh <out> --full` for the full sweep. NEVER a reader's replay under the live source name — the readers take the snapshot.\\n\" % N['mins_after2'] + s"))
# ---- 8. the recovery page ----
R.append(("the SUMMARY read once; CUT 2026-09-19 to %s — the snapshot, the parallel probes, the\\n  stamped sweep, the incremental positions, every short cut keyed on the sources' digests; `--full` for the whole work; GATES_CHAIN.md);\" % N['mins_after'])",
          "the SUMMARY read once; CUT 2026-09-19 to %s — the snapshot, the parallel probes, the\\n  stamped sweep, the positions by eight workers, every short cut keyed on the sources' digests; `--full` for the full sweep; GATES_CHAIN.md);\" % N['mins_after2'])"))
# ---- 9. the addenda ----
R.append(('''parallel; the journal gate's two replays concurrent; the positions table incremental by regions under the tape-prefix guard; the sweep parallel and
incremental against its stamp (a shared piece moved = full; the stamp by a green sweep only, tracked); the second journal gate the UNMOVED digest.
AS RUN: %s (wall %s), ALL GREEN, every verdict the old chain gave; the first sweep and positions FULL (no stamp, an old-form table). THE FILES:
run_cold_all.py, world_journal.py (sources_key, save/load_snapshot, live_digest, --stamp/--unmoved, the concurrent gate), register_census.py (Ink by
the INK block; running_world from the snapshot), cold_run_sequence.py (save_snapshot in run(); _cp_block, checkpoint_regions, tape_prefix_hash,
checkpoints_partial(only=); checkpoint_names cached), checkpoint_positions.py (--incremental), gates_chain.sh (the twelve steps; --full). THE RECORDS
on the sheet; the forms in World/step9/forms_gates_cut_%s/. NOT COMMITTED — in the chapter-8 commit on the owner's word.
""" % (TODAY, N['mins_after'], N['mins_after'], N['mins_wall'], TODAY)''', '''parallel; the journal gate's two replays concurrent; the positions table measured WHOLE by eight workers (an incremental form by regions built,
tested against a moved region and STRUCK the same day — seven of CU's nine rows NOT YET; the closure 429 of 630 statements); the sweep parallel and
incremental against its stamp (a shared piece moved = full; the stamp by a green sweep only, tracked); the second journal gate the UNMOVED digest.
AS RUN: the first chain %s (wall %s) with everything in full, the second %s (wall %s) with nothing moved — ALL GREEN both, every verdict the old
chain gave. THE FILES: run_cold_all.py, world_journal.py (sources_key, save/load_snapshot, live_digest, --stamp/--unmoved, the concurrent gate),
register_census.py (Ink by the INK block; running_world from the snapshot), cold_run_sequence.py (save_snapshot in run(); _cp_block the parse-once
cache; checkpoint_names cached), checkpoint_positions.py (--jobs, the workers), gates_chain.sh (the twelve steps; --full). THE RECORDS on the sheet;
the forms in World/step9/forms_gates_cut_%s/. NOT COMMITTED — in the chapter-8 commit on the owner's word.
""" % (TODAY, N['mins_after2'], N['mins_after'], N['mins_wall'], N['mins_after2'], N['mins_wall2'], TODAY)'''))
# ---- 10. the state doc ----
R.append(("(4) checkpoint_positions.py --incremental — cold_run_sequence._cp_block (parsed and compiled once), checkpoint_regions(), tape_prefix_hash(), checkpoints_partial(only=); the table carries regions, tape_prefix_hash, preamble_hash, each row's region; (5)",
          "(4) checkpoint_positions.py --jobs 8 — eight workers, each the WHOLE tape in its own journal folder with the live base copied in (the replay still the audit), asking the block at pause i where i mod 8 is its number; the parent merges the pauses and takes the falls; the table always whole (AN INCREMENTAL FORM BY REGIONS WAS BUILT, TESTED AGAINST A MOVED REGION AND STRUCK the same day: seven of CU's nine rows came out NOT YET — a region's checkpoints read helpers bound across most of the block, the closure 429 of 630 statements; the record in GATES_CHAIN.md); cold_run_sequence._cp_block the parse-once cache; (5)"))
R.append(("THE CHAIN AS RUN: ALL GREEN — tape %s s (%s), probes %s s (%s), daemon %s s, dependency %s s, build %s s, journal %s s (%s kinds, %s rows), register %s s (DECLARED %s / DEBT %s / FAILS %s, from the snapshot), positions %s s (%s: %s checkpoints over %s pauses), checkpoint %s s (%s/%s), stamp %s s, sweep %s s (%s: %s/%s runners, %s cells, %s jobs), unmoved %s s (%s sources); every verdict the chain before the cut gave.",
          "THE CHAIN AS RUN TWICE, ALL GREEN BOTH — the first (everything in full, %s, wall %s): tape %s s (%s), probes %s s (%s), daemon %s s, dependency %s s, build %s s, journal %s s (%s kinds, %s rows), register %s s (DECLARED %s / DEBT %s / FAILS %s, from the snapshot), positions %s s (the old sequential measure: %s checkpoints over %s pauses), checkpoint %s s (%s/%s), stamp %s s, sweep %s s (%s: %s/%s runners, %s cells, %s jobs), unmoved %s s (%s sources); the second (nothing moved — THE STEADY STATE, %s, wall %s): tape %s, probes %s, journal %s, register %s, positions %s (%s workers: %s over %s pauses in %s s), checkpoint %s, sweep %s (%s — nothing to grade), unmoved %s; every verdict the chain before the cut gave."))
R.append(('''""" % (TODAY, N['mins_after'], N['mins_wall'], after['tape'], tape_score, after['probes'], ', '.join('%s %s/%s' % (k, v[0], v[1]) for k, v in probes.items()), after['daemon'], after['dependency'], after['build'], after['journal'], N['jour'][0], N['jour'][1], after['register'], N['reg'][0], N['reg'][1], N['reg'][2], after['positions'], N['pos_mode'][0], N['pos'][0], N['pos'][1], after['checkpoint'], cp[0], cp[1], after['stamp'], after['sweep'], N['sw_mode'][0], N['sw'][0], N['sw'][1], N['sw'][2], N['sw'][6], after['unmoved'], N['unm'], TODAY)''',
          '''""" % (TODAY, N['mins_after2'], N['mins_wall2'], N['mins_after'], N['mins_wall'], after['tape'], tape_score, after['probes'], ', '.join('%s %s/%s' % (k, v[0], v[1]) for k, v in probes.items()), after['daemon'], after['dependency'], after['build'], after['journal'], N['jour'][0], N['jour'][1], after['register'], N['reg'][0], N['reg'][1], N['reg'][2], after['positions'], N['pos'][0], N['pos'][1], after['checkpoint'], cp[0], cp[1], after['stamp'], after['sweep'], N['sw_mode'][0], N['sw'][0], N['sw'][1], N['sw'][2], N['sw'][6], after['unmoved'], N['unm'],
       N['mins_after2'], N['mins_wall2'], after2['tape'], after2['probes'], after2['journal'], after2['register'], after2['positions'], N['pos2'][3], N['pos2'][0], N['pos2'][1], N['pos2'][2], after2['checkpoint'], after2['sweep'], N['sw2'][0], after2['unmoved'], TODAY)'''))
R.append(("THE STATE: chapter 8 compiled and on the tape as #196 addendum 4 says (nothing of the tape, the runners, the registries or the records of 6b touched by this work); THE GATES CHAIN CUT from ninety minutes to %s (the wall clock %s)",
          "THE STATE: chapter 8 compiled and on the tape as #196 addendum 4 says (nothing of the tape, the runners, the registries or the records of 6b touched by this work); THE GATES CHAIN CUT from ninety minutes to %s (the wall clock %s; the second chain, nothing moved — the first, everything in full, %s / wall %s)"))
# ---- 11. the memory ----
R.append(("`checkpoint_positions.py --incremental` by regions under the tape-prefix guard; `run_cold_all.py", "`checkpoint_positions.py --jobs 8` (the whole measure by eight workers — an incremental form by regions was struck by its own test); `run_cold_all.py"))
R.append(("The first chain after the cut: %s, ALL GREEN, every verdict the old chain gave. **Why:**", "The first chain after the cut (everything in full): %s; the second (nothing moved): %s — ALL GREEN both, every verdict the old chain gave. **Why:**"))
R.append(('''the stamp is written by a green sweep only, never by hand.
""" % N['mins_after']''', '''the stamp is written by a green sweep only, never by hand; a short cut is TESTED AGAINST A MOVED PIECE before it is trusted.
""" % (N['mins_after'], N['mins_after2'])'''))
# ---- 12. the commit message ----
R.append(("the journal gate's two replays concurrent; the positions table INCREMENTAL by regions (the checkpoints block parsed and compiled once; a row kept while its region's digest, the preamble's digest and the tape prefix — the lines minus the newest runner's — stand); the sweep PARALLEL",
          "the journal gate's two replays concurrent; the positions table measured WHOLE by eight workers (each the tape in its own folder with the live base copied in, asking the block at its own pauses; the checkpoints block parsed and compiled once — AN INCREMENTAL FORM BY REGIONS WAS BUILT, TESTED AGAINST A MOVED REGION AND STRUCK THE SAME DAY: seven of CU's nine rows came out NOT YET, the region's checkpoints reading helpers bound across most of the block, the closure 429 of 630 statements); the sweep PARALLEL"))
R.append(("THE CHAIN AS RUN: ALL GREEN in %s (wall %s) — the tape %s, the probes %s,", "THE CHAIN AS RUN TWICE, ALL GREEN BOTH — the first with everything in full in %s (wall %s), the second with nothing moved in %s (wall %s), the steady state — the tape %s, the probes %s,"))
R.append(("the positions %s checkpoints over %s pauses (%s), the sweep %s/%s at %s graded cells (%s) — every verdict the chain before the cut gave; the steady state near nineteen minutes (the incremental positions 145 s and the incremental sweep 5 s measured after the chain with nothing moved).",
          "the positions %s checkpoints over %s pauses (the second chain by %s workers in %s s), the sweep %s/%s at %s graded cells (%s; the second chain NOTHING TO GRADE) — every verdict the chain before the cut gave."))
R.append(('''""" % (TODAY, N['mins_after'], N['mins_wall'], tape_score, ', '.join('%s %s/%s' % (k, v[0], v[1]) for k, v in probes.items()), N['dae'][0], N['dae'][1], N['dep'][0], N['dep'][1], N['jour'][0], N['jour'][1], N['reg'][0], N['reg'][1], N['reg'][2], N['pos'][0], N['pos'][1], N['pos_mode'][0], N['sw'][0], N['sw'][1], N['sw'][2], N['sw_mode'][0], TODAY)''',
          '''""" % (TODAY, N['mins_after'], N['mins_wall'], N['mins_after2'], N['mins_wall2'], tape_score, ', '.join('%s %s/%s' % (k, v[0], v[1]) for k, v in probes.items()), N['dae'][0], N['dae'][1], N['dep'][0], N['dep'][1], N['jour'][0], N['jour'][1], N['reg'][0], N['reg'][1], N['reg'][2], N['pos'][0], N['pos'][1], N['pos2'][3], N['pos2'][2], N['sw'][0], N['sw'][1], N['sw'][2], N['sw_mode'][0], TODAY)'''))
R.append(("AND, THE SAME DAY, THE GATES CHAIN CUT FROM NINETY MINUTES TO %s — THE IMPORT WAS THE COST, NOT THE REPLAY: THE RUNNING WORLD SAVED ONCE AND READ BY THE GATES, THE PROBES IN PARALLEL, THE SWEEP EIGHT AT A TIME AND ONLY WHAT MOVED, EVERY SHORT CUT KEYED ON THE SOURCES\\' DIGESTS.' % N['mins_after'].upper()",
          "AND, THE SAME DAY, THE GATES CHAIN CUT FROM NINETY MINUTES TO %s — THE IMPORT WAS THE COST, NOT THE REPLAY: THE RUNNING WORLD SAVED ONCE AND READ BY THE GATES, THE PROBES IN PARALLEL, THE SWEEP EIGHT AT A TIME AND ONLY WHAT MOVED, THE CHECKPOINT TABLE BY EIGHT WORKERS, EVERY SHORT CUT KEYED ON THE SOURCES\\' DIGESTS AND ONE STRUCK BY ITS OWN TEST.' % N['mins_after2'].upper()"))
n = 0
for a, b in R:
    c = s.count(a)
    if c != 1: print('ANCHOR x%d: %r' % (c, a[:100])); continue
    s = s.replace(a, b); n += 1
open(P, 'w', encoding='utf-8').write(s)
ast.parse(s); print('writer rewritten: %d of %d replacements; parses' % (n, len(R)))

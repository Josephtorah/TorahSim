#!/bin/sh
# THE GATES STEP AS ONE CHAIN (2026-09-16; the owner's cost review after THE DEUTERONOMY WALK 2b — "lets do all 3"): every gate of a compile
# sitting's gates step runs in ORDER in one background job and writes ONE summary — a line per step, PASS or FAIL with the step's last printed line.
# The caller reads the summary once when the job ends (the harness notifies; NEVER poll in a loop). The long steps (positions, sweep, the final
# journal check) are skipped when the tape or a probe failed — nothing to measure on a broken tape.
#
# THE GATES CUT (2026-09-19; the owner: "Yes make that change. It's too long as it is" — the chain measured at ninety minutes, its cost the IMPORT of
# sixty-three runners paid by every step, two minutes each, against a replay of two seconds): (1) the tape's run SAVES THE RUNNING WORLD (a snapshot,
# daemons stripped, keyed by the sources' digest) and the readers — the register gate, the readback and register probes — load it in a second;
# (2) the eleven probe suites run IN PARALLEL (each its own process; none writes the live source — the readers take the snapshot, the cursor's
# replays journal nothing, the steppers write their own sources); (3) the journal gate's two runs go CONCURRENTLY; (4) the positions table is
# measured WHOLE by eight workers, each stepping the tape in its own folder and asking the block at its own pauses; (5) the sweep runs IN PARALLEL and
# INCREMENTALLY against its stamp (the runners moved and their importers; a shared piece moved = full), the sequence runner skipped (the chain's
# own first step); (6) the second journal gate is the UNMOVED check — the live rows' digest stamped before the sweep and compared after.
# --full forces the full sweep (the positions table is always the whole measure).
#
#   sh World/step9/gates_chain.sh <out_dir> [--from STEP] [--skip STEP,STEP] [--full] [--list]
#
# The steps, in the design's order: tape probes daemon dependency build journal register positions checkpoint stamp sweep unmoved
# Each step's full print is <out_dir>/<step>.out; the summary <out_dir>/SUMMARY.txt; the chain's exit code 1 if any step failed.
cd "$(dirname "$0")/../.." || exit 2
OUT="$1"; [ -n "$OUT" ] || { echo "usage: gates_chain.sh <out_dir> [--from STEP] [--skip A,B] [--full] [--list]"; exit 2; }
shift
FROM=""; SKIP=""; LIST=0; FULL=0
while [ $# -gt 0 ]; do
  case "$1" in
    --from) FROM="$2"; shift 2 ;;
    --skip) SKIP=",$2,"; shift 2 ;;
    --full) FULL=1; shift ;;
    --list) LIST=1; shift ;;
    *) echo "unknown option $1"; exit 2 ;;
  esac
done
STEPS="tape probes daemon dependency build journal register positions checkpoint stamp sweep unmoved"
if [ $LIST = 1 ]; then echo "$STEPS"; exit 0; fi
mkdir -p "$OUT"; SUM="$OUT/SUMMARY.txt"; : > "$SUM"
FAILED=0; STARTED=0; [ -z "$FROM" ] && STARTED=1
PROBES="census installation readback register clock sequence view population journal cursor large_letter"
run_step() {   # name, command...
  name="$1"; shift
  if [ $STARTED = 0 ]; then [ "$name" = "$FROM" ] && STARTED=1 || { echo "SKIP $name (before --from)" >> "$SUM"; return 0; }; fi
  case "$SKIP" in *",$name,"*) echo "SKIP $name (--skip)" >> "$SUM"; return 0 ;; esac
  case "$name" in positions|checkpoint|stamp|sweep|unmoved) [ $FAILED = 1 ] && { echo "SKIP $name (an earlier step failed)" >> "$SUM"; return 0; } ;; esac
  t0=$(date +%s)
  "$@" > "$OUT/$name.out" 2>&1; rc=$?
  t1=$(( $(date +%s) - t0 ))
  last=$(tail -1 "$OUT/$name.out" | cut -c1-150)
  if [ $rc = 0 ]; then echo "PASS $name (${t1}s) $last" >> "$SUM"; else echo "FAIL $name rc=$rc (${t1}s) $last" >> "$SUM"; FAILED=1; fi
}
run_probes() {   # THE GATES CUT: the suites in parallel, each to its own print; the fractions gathered when all have ended
  rc=0
  for p in $PROBES; do
    ( python3 "World/step9/${p}_probes.py" > "$OUT/probe_$p.out" 2>&1; echo $? > "$OUT/probe_$p.rc" ) &
  done
  wait
  for p in $PROBES; do
    prc=$(cat "$OUT/probe_$p.rc" 2>/dev/null || echo 1)
    [ "$prc" = 0 ] || { rc=1; echo "  FAIL probe $p: $(tail -1 "$OUT/probe_$p.out" | cut -c1-120)"; }
    echo "  $p: $(grep -oE '[0-9]+/[0-9]+' "$OUT/probe_$p.out" | tail -1)"
  done
  return $rc
}
POSARGS="--jobs 8"; SWEEPARGS="--changed --jobs 8 --skip cold_run_sequence.py"
[ $FULL = 1 ] && SWEEPARGS="--jobs 8 --skip cold_run_sequence.py"
run_step tape        python3 World/step9/cold_run_sequence.py
run_step probes      run_probes
run_step daemon      python3 World/step9/daemon_census.py
run_step dependency  python3 World/step9/dependency_census.py
run_step build       python3 World/build_world.py
run_step journal     python3 World/step9/world_journal.py --gate
run_step register    python3 World/step9/register_census.py --strict
run_step positions   python3 World/step9/checkpoint_positions.py $POSARGS
run_step checkpoint  python3 World/step9/checkpoint_probes.py
run_step stamp       python3 World/step9/world_journal.py --stamp "$OUT/journal_stamp.json"
run_step sweep       python3 World/step9/run_cold_all.py $SWEEPARGS
run_step unmoved     python3 World/step9/world_journal.py --unmoved "$OUT/journal_stamp.json"
echo "GATES CHAIN DONE — $( [ $FAILED = 0 ] && echo ALL GREEN || echo FAILURES ABOVE ) — $(date +%H:%M)" >> "$SUM"
cat "$SUM"
exit $FAILED

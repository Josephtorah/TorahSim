#!/bin/sh
# THE GATES STEP AS ONE CHAIN (2026-09-16; the owner's cost review after THE DEUTERONOMY WALK 2b — "lets do all 3"): every gate of a compile
# sitting's gates step runs in ORDER in one background job and writes ONE summary — a line per step, PASS or FAIL with the step's last printed line.
# The caller reads the summary once when the job ends (the harness notifies; NEVER poll in a loop). The long steps (positions, sweep, the final
# journal gate) are skipped when the tape or a probe failed — nothing to measure on a broken tape.
#
#   sh World/step9/gates_chain.sh <out_dir> [--from STEP] [--skip STEP,STEP] [--list]
#
# The steps, in the design's order: tape probes daemon dependency build journal register positions checkpoint sweep journal2
# Each step's full print is <out_dir>/<step>.out; the summary <out_dir>/SUMMARY.txt; the chain's exit code 1 if any step failed.
cd "$(dirname "$0")/../.." || exit 2
OUT="$1"; [ -n "$OUT" ] || { echo "usage: gates_chain.sh <out_dir> [--from STEP] [--skip A,B] [--list]"; exit 2; }
shift
FROM=""; SKIP=""; LIST=0
while [ $# -gt 0 ]; do
  case "$1" in
    --from) FROM="$2"; shift 2 ;;
    --skip) SKIP=",$2,"; shift 2 ;;
    --list) LIST=1; shift ;;
    *) echo "unknown option $1"; exit 2 ;;
  esac
done
STEPS="tape probes daemon dependency build journal register positions checkpoint sweep journal2"
if [ $LIST = 1 ]; then echo "$STEPS"; exit 0; fi
mkdir -p "$OUT"; SUM="$OUT/SUMMARY.txt"; : > "$SUM"
FAILED=0; STARTED=0; [ -z "$FROM" ] && STARTED=1
PROBES="census installation readback register clock sequence view population journal cursor"
run_step() {   # name, command...
  name="$1"; shift
  if [ $STARTED = 0 ]; then [ "$name" = "$FROM" ] && STARTED=1 || { echo "SKIP $name (before --from)" >> "$SUM"; return 0; }; fi
  case "$SKIP" in *",$name,"*) echo "SKIP $name (--skip)" >> "$SUM"; return 0 ;; esac
  case "$name" in positions|checkpoint|sweep|journal2) [ $FAILED = 1 ] && { echo "SKIP $name (an earlier step failed)" >> "$SUM"; return 0; } ;; esac
  t0=$(date +%s)
  "$@" > "$OUT/$name.out" 2>&1; rc=$?
  t1=$(( $(date +%s) - t0 ))
  last=$(tail -1 "$OUT/$name.out" | cut -c1-150)
  if [ $rc = 0 ]; then echo "PASS $name (${t1}s) $last" >> "$SUM"; else echo "FAIL $name rc=$rc (${t1}s) $last" >> "$SUM"; FAILED=1; fi
}
run_probes() {
  rc=0
  for p in $PROBES; do
    python3 "World/step9/${p}_probes.py" > "$OUT/probe_$p.out" 2>&1 || { rc=1; echo "  FAIL probe $p: $(tail -1 "$OUT/probe_$p.out" | cut -c1-120)"; }
    echo "  $p: $(grep -o '[0-9]*/[0-9]* probes\|[0-9]*/[0-9]*$\|PROBES: [0-9]*/[0-9]*' "$OUT/probe_$p.out" | tail -1)"
  done
  return $rc
}
run_step tape        python3 World/step9/cold_run_sequence.py
run_step probes      run_probes
run_step daemon      python3 World/step9/daemon_census.py
run_step dependency  python3 World/step9/dependency_census.py
run_step build       python3 World/build_world.py
run_step journal     python3 World/step9/world_journal.py --gate
run_step register    python3 World/step9/register_census.py --strict
run_step positions   python3 World/step9/checkpoint_positions.py
run_step checkpoint  python3 World/step9/checkpoint_probes.py
run_step sweep       python3 World/step9/run_cold_all.py
run_step journal2    python3 World/step9/world_journal.py --gate
echo "GATES CHAIN DONE — $( [ $FAILED = 0 ] && echo ALL GREEN || echo FAILURES ABOVE ) — $(date +%H:%M)" >> "$SUM"
cat "$SUM"
exit $FAILED

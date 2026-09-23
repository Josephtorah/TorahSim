#!/bin/sh
# THE DEUTERONOMY WALK 13b: the tape's FOURTH chain — the scan's ground fixed (this daemon's own writes excluded) -> the runner's graded run again (91/91 owed)
# -> the tape's third run -> checkpoint_check.py --all; every step timed; stops at the first failure. RUN FROM THE REPO ROOT (in the background — the cache law).
SP="$(cd "$(dirname "$0")" && pwd)"
cd "$(git rev-parse --show-toplevel)" || exit 2
export TIMING=$SP/ch15b_timing.tsv
sh $SP/tstep.sh "13b B the scan's ground fixed (this daemon's writes excluded)" sh -c "python3 $SP/patch_reuse_scan_ch15.py > $SP/patch_reuse_scan_ch15.out 2>&1" || { tail -4 $SP/patch_reuse_scan_ch15.out; exit 1; }
cat $SP/patch_reuse_scan_ch15.out
sh $SP/tstep.sh "13b B the runner, graded run after the scan's fix" sh -c "python3 World/step9/cold_run_release_firstborn.py > $SP/ch15_runner_run3.out 2>&1" || { tail -4 $SP/ch15_runner_run3.out; exit 1; }
/usr/bin/grep "MATRIX" $SP/ch15_runner_run3.out | tail -1 | cut -c1-200
sh $SP/tstep.sh "13b B the tape, third run" sh -c "python3 World/step9/cold_run_sequence.py > $SP/ch15_tape_run3.out 2>&1"
echo "tape rc $?"
/usr/bin/grep "checkpoints\|CHECKPOINT CU5\|MISS \|DIFF\|Traceback\|Error" $SP/ch15_tape_run3.out | cut -c1-220 | head -12
sh $SP/tstep.sh "13b B checkpoint_check --all (after the third run)" sh -c "python3 World/step9/checkpoint_check.py --all > $SP/ch15_checkpoint_check.out 2>&1"
tail -1 $SP/ch15_checkpoint_check.out | cut -c1-200

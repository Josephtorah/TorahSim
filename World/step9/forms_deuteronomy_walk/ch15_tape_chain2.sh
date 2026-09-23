#!/bin/sh
# THE DEUTERONOMY WALK 13b: the tape's SECOND chain after the first run's 9/10 — CU5 retyped from the print -> the tape's second run -> checkpoint_check.py --all;
# every step timed; stops at the first failure. RUN FROM THE REPO ROOT (launched in the background — the cache law).
SP="$(cd "$(dirname "$0")" && pwd)"
cd "$(git rev-parse --show-toplevel)" || exit 2
export TIMING=$SP/ch15b_timing.tsv
sh $SP/tstep.sh "13b B CU5 retyped from the tape's print" sh -c "python3 $SP/patch_tape_cu5_ch15.py > $SP/patch_tape_cu5_ch15.out 2>&1" || { tail -4 $SP/patch_tape_cu5_ch15.out; exit 1; }
cat $SP/patch_tape_cu5_ch15.out
sh $SP/tstep.sh "13b B the tape, second run" sh -c "python3 World/step9/cold_run_sequence.py > $SP/ch15_tape_run2.out 2>&1"
echo "tape rc $?"
/usr/bin/grep "checkpoints\|CHECKPOINT CU5\|MISS \|DIFF\|Traceback\|Error" $SP/ch15_tape_run2.out | cut -c1-220 | head -12
sh $SP/tstep.sh "13b B checkpoint_check --all (after the second run)" sh -c "python3 World/step9/checkpoint_check.py --all > $SP/ch15_checkpoint_check.out 2>&1"
tail -1 $SP/ch15_checkpoint_check.out | cut -c1-200

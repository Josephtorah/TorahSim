#!/bin/sh
# THE DEUTERONOMY WALK 13b: the tape's THIRD chain — the second run proper (the CU5 retype's apostrophes escaped after the SyntaxError) -> checkpoint_check.py --all.
SP="$(cd "$(dirname "$0")" && pwd)"
cd "$(git rev-parse --show-toplevel)" || exit 2
export TIMING=$SP/ch15b_timing.tsv
sh $SP/tstep.sh "13b B the tape, second run (the retype's apostrophes escaped)" sh -c "python3 World/step9/cold_run_sequence.py > $SP/ch15_tape_run2.out 2>&1"
echo "tape rc $?"
/usr/bin/grep "checkpoints\|CHECKPOINT CU5\|MISS \|DIFF\|Traceback\|Error" $SP/ch15_tape_run2.out | cut -c1-220 | head -12
sh $SP/tstep.sh "13b B checkpoint_check --all (after the second run)" sh -c "python3 World/step9/checkpoint_check.py --all > $SP/ch15_checkpoint_check.out 2>&1"
tail -1 $SP/ch15_checkpoint_check.out | cut -c1-200

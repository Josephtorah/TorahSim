#!/bin/sh
# THE DEUTERONOMY WALK 12b: the tape's chain — the recorder with the cache OFF (7b's lesson 1) -> the stitcher (no marker; five own-day lines) -> the literals
# patched from the stitcher's print (DE1-DE9; the one stale literal retyped (DD2)) -> the tape's first run -> checkpoint_check.py --all AFTER the tape; every step timed;
# the chain stops at the first failure. 11b's form (ch13_tape_chain.sh). RUN FROM THE REPO ROOT (launched in the background — the cache law).
SP="$(cd "$(dirname "$0")" && pwd)"
cd "$(git rev-parse --show-toplevel)" || exit 2
export TIMING=$SP/ch14_timing.tsv
sh $SP/tstep.sh "12b B the recorder (INK_CACHE=0)" sh -c "INK_CACHE=0 python3 $SP/seq_record_ch14.py > $SP/seq_record_ch14.out 2>&1" || { tail -3 $SP/seq_record_ch14.out; exit 1; }
tail -2 $SP/seq_record_ch14.out; /usr/bin/grep "food_tithe\|seducers " $SP/seq_record_ch14.out | head -3
sh $SP/tstep.sh "12b B the stitcher (no marker)" sh -c "python3 $SP/seq_stitch_ch14.py > $SP/seq_stitch_ch14.out 2>&1" || { tail -3 $SP/seq_stitch_ch14.out; exit 1; }
/usr/bin/grep "PLACEMENT LITERAL\|CENSUS tuple\|tape written" $SP/seq_stitch_ch14.out | cut -c1-260
sh $SP/tstep.sh "12b B the literals patched (DF1-DF9; one retype)" sh -c "python3 $SP/patch_seq_literals_ch14.py > $SP/patch_seq_literals_ch14.out 2>&1" || { tail -4 $SP/patch_seq_literals_ch14.out; exit 1; }
tail -1 $SP/patch_seq_literals_ch14.out | cut -c1-200
sh $SP/tstep.sh "12b B the tape, first run" sh -c "python3 World/step9/cold_run_sequence.py > $SP/ch14_tape_run1.out 2>&1"
echo "tape rc $?"
/usr/bin/grep "checkpoints\|CHECKPOINT DF\|MISS\|DIVERGE\|Traceback\|Error" $SP/ch14_tape_run1.out | cut -c1-220 | head -24
sh $SP/tstep.sh "12b B checkpoint_check --all (after the tape)" sh -c "python3 World/step9/checkpoint_check.py --all > $SP/ch14_checkpoint_check.out 2>&1"
tail -1 $SP/ch14_checkpoint_check.out | cut -c1-200

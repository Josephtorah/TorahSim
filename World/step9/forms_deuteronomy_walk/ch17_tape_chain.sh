#!/bin/sh
# THE DEUTERONOMY WALK 15b: the tape's chain — the recorder with the cache OFF (7b's lesson 1) -> the stitcher (no marker; eight own-day lines) -> the literals
# patched from the stitcher's print (DI1-DI5; the stale literals retyped as the grep reads them) -> the tape's first run -> checkpoint_check.py --all AFTER the tape; every step timed;
# the chain stops at the first failure. 14b's form (ch16_tape_chain.sh). RUN FROM THE REPO ROOT (launched in the background — the cache law).
SP="$(cd "$(dirname "$0")" && pwd)"
cd "$(git rev-parse --show-toplevel)" || exit 2
export TIMING=$SP/ch17b_timing.tsv   # 15b: the compile sitting's own table (12b's form named the reading's)
sh $SP/tstep.sh "15b B the recorder (INK_CACHE=0)" sh -c "INK_CACHE=0 python3 $SP/seq_record_ch17.py > $SP/seq_record_ch17.out 2>&1" || { tail -3 $SP/seq_record_ch17.out; exit 1; }
tail -2 $SP/seq_record_ch17.out; /usr/bin/grep "courts_prophet\|festivals_judges " $SP/seq_record_ch17.out | head -3
sh $SP/tstep.sh "15b B the stitcher (no marker)" sh -c "python3 $SP/seq_stitch_ch17.py > $SP/seq_stitch_ch17.out 2>&1" || { tail -3 $SP/seq_stitch_ch17.out; exit 1; }
/usr/bin/grep "PLACEMENT LITERAL\|CENSUS tuple\|tape written" $SP/seq_stitch_ch17.out | cut -c1-260
sh $SP/tstep.sh "15b B the literals patched (DI1-DI5; the stale literals as read)" sh -c "python3 $SP/patch_seq_literals_ch17.py > $SP/patch_seq_literals_ch17.out 2>&1" || { tail -4 $SP/patch_seq_literals_ch17.out; exit 1; }
tail -1 $SP/patch_seq_literals_ch17.out | cut -c1-200
sh $SP/tstep.sh "15b B the tape, first run" sh -c "python3 World/step9/cold_run_sequence.py > $SP/ch17_tape_run1.out 2>&1"
echo "tape rc $?"
/usr/bin/grep "checkpoints\|CHECKPOINT DI\|MISS\|DIVERGE\|Traceback\|Error" $SP/ch17_tape_run1.out | cut -c1-220 | head -24
sh $SP/tstep.sh "15b B checkpoint_check --all (after the tape)" sh -c "python3 World/step9/checkpoint_check.py --all > $SP/ch17_checkpoint_check.out 2>&1"
tail -1 $SP/ch17_checkpoint_check.out | cut -c1-200

#!/bin/sh
# THE DEUTERONOMY WALK 10b: the tape's chain — the recorder with the cache OFF (7b's lesson 1) -> the stitcher (no marker; four own-day lines) -> the literals
# patched from the stitcher's print (DD1-DD9) -> the tape's first run -> checkpoint_check.py --all AFTER the tape; every step timed; the chain stops at the first
# failure. RUN FROM THE REPO ROOT (launched in the background — the cache law).
SP=<scratch>
cd "$(git rev-parse --show-toplevel)" || exit 2
sh $SP/tstep.sh "10b B the recorder (INK_CACHE=0)" sh -c "INK_CACHE=0 python3 $SP/seq_record_ch12.py > $SP/seq_record_ch12.out 2>&1" || { tail -3 $SP/seq_record_ch12.out; exit 1; }
tail -2 $SP/seq_record_ch12.out; /usr/bin/grep "place_name\|blessing_and_curse " $SP/seq_record_ch12.out | head -3
sh $SP/tstep.sh "10b B the stitcher (no marker)" sh -c "python3 $SP/seq_stitch_ch12.py > $SP/seq_stitch_ch12.out 2>&1" || { tail -3 $SP/seq_stitch_ch12.out; exit 1; }
/usr/bin/grep "PLACEMENT LITERAL\|CENSUS tuple\|tape written" $SP/seq_stitch_ch12.out | cut -c1-260
sh $SP/tstep.sh "10b B the literals patched (DD1-DD9)" sh -c "python3 $SP/patch_seq_literals_ch12.py > $SP/patch_seq_literals_ch12.out 2>&1" || { tail -4 $SP/patch_seq_literals_ch12.out; exit 1; }
tail -1 $SP/patch_seq_literals_ch12.out | cut -c1-200
sh $SP/tstep.sh "10b B the tape, first run" sh -c "python3 World/step9/cold_run_sequence.py > $SP/ch12_tape_run1.out 2>&1"
echo "tape rc $?"
/usr/bin/grep "checkpoints\|CHECKPOINT DD\|MISS\|DIVERGE\|Traceback\|Error" $SP/ch12_tape_run1.out | cut -c1-220 | head -24
sh $SP/tstep.sh "10b B checkpoint_check --all (after the tape)" sh -c "python3 World/step9/checkpoint_check.py --all > $SP/ch12_checkpoint_check.out 2>&1"
tail -1 $SP/ch12_checkpoint_check.out | cut -c1-200

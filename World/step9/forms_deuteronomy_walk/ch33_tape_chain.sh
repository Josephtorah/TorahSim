#!/bin/sh
# THE DEUTERONOMY WALK 21b: the tape's chain — the recorder with the cache OFF (7b's lesson 1) -> the stitcher (NO marker; eleven own-day lines in two forms and NO MARKER) -> the literals
# patched from the stitcher's print (DO1-DO5; the stale literals retyped as the grep reads them) -> the tape's first run -> checkpoint_check.py --all AFTER the tape; every step timed;
# the chain stops at the first failure. 20b's form (ch32_tape_chain.sh). RUN FROM THE REPO ROOT (launched in the background — the cache law).
SP="$(cd "$(dirname "$0")" && pwd)"
cd "$(git rev-parse --show-toplevel)" || exit 2
export TIMING=$SP/ch33b_timing.tsv   # 21b: the compile sitting's own table (12b's form named the reading's)
sh $SP/tstep.sh "21b B the recorder (INK_CACHE=0)" sh -c "INK_CACHE=0 python3 $SP/seq_record_ch33.py > $SP/seq_record_ch33.out 2>&1" || { tail -3 $SP/seq_record_ch33.out; exit 1; }
tail -2 $SP/seq_record_ch33.out; /usr/bin/grep "blessing_of_moses\|song_charge_nebo " $SP/seq_record_ch33.out | head -3
sh $SP/tstep.sh "21b B the stitcher (NO marker)" sh -c "python3 $SP/seq_stitch_ch33.py > $SP/seq_stitch_ch33.out 2>&1" || { tail -3 $SP/seq_stitch_ch33.out; exit 1; }
/usr/bin/grep "PLACEMENT LITERAL\|CENSUS tuple\|tape written" $SP/seq_stitch_ch33.out | cut -c1-260
sh $SP/tstep.sh "21b B the literals patched (DO1-DO5; the stale literals as read)" sh -c "python3 $SP/patch_seq_literals_ch33.py > $SP/patch_seq_literals_ch33.out 2>&1" || { tail -4 $SP/patch_seq_literals_ch33.out; exit 1; }
tail -1 $SP/patch_seq_literals_ch33.out | cut -c1-200
sh $SP/tstep.sh "21b B the tape, first run" sh -c "python3 World/step9/cold_run_sequence.py > $SP/ch33_tape_run1.out 2>&1"
echo "tape rc $?"
/usr/bin/grep "checkpoints\|CHECKPOINT DO\|MISS\|DIVERGE\|Traceback\|Error" $SP/ch33_tape_run1.out | cut -c1-220 | head -24
sh $SP/tstep.sh "21b B checkpoint_check --all (after the tape)" sh -c "python3 World/step9/checkpoint_check.py --all > $SP/ch33_checkpoint_check.out 2>&1"
tail -1 $SP/ch33_checkpoint_check.out | cut -c1-200

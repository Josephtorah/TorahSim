#!/bin/sh
# THE DEUTERONOMY WALK 20b: the tape's chain — the recorder with the cache OFF (7b's lesson 1) -> the stitcher (NO marker; sixteen own-day lines in three forms and NO MARKER) -> the literals
# patched from the stitcher's print (DN1-DN5; the stale literals retyped as the grep reads them) -> the tape's first run -> checkpoint_check.py --all AFTER the tape; every step timed;
# the chain stops at the first failure. 19b's form (ch29_tape_chain.sh). RUN FROM THE REPO ROOT (launched in the background — the cache law).
SP="$(cd "$(dirname "$0")" && pwd)"
cd "$(git rev-parse --show-toplevel)" || exit 2
export TIMING=$SP/ch32b_timing.tsv   # 20b: the compile sitting's own table (12b's form named the reading's)
sh $SP/tstep.sh "20b B the recorder (INK_CACHE=0)" sh -c "INK_CACHE=0 python3 $SP/seq_record_ch32.py > $SP/seq_record_ch32.out 2>&1" || { tail -3 $SP/seq_record_ch32.out; exit 1; }
tail -2 $SP/seq_record_ch32.out; /usr/bin/grep "song_charge_nebo\|covenant_return_charge " $SP/seq_record_ch32.out | head -3
sh $SP/tstep.sh "20b B the stitcher (NO marker)" sh -c "python3 $SP/seq_stitch_ch32.py > $SP/seq_stitch_ch32.out 2>&1" || { tail -3 $SP/seq_stitch_ch32.out; exit 1; }
/usr/bin/grep "PLACEMENT LITERAL\|CENSUS tuple\|tape written" $SP/seq_stitch_ch32.out | cut -c1-260
sh $SP/tstep.sh "20b B the literals patched (DN1-DN5; the stale literals as read)" sh -c "python3 $SP/patch_seq_literals_ch32.py > $SP/patch_seq_literals_ch32.out 2>&1" || { tail -4 $SP/patch_seq_literals_ch32.out; exit 1; }
tail -1 $SP/patch_seq_literals_ch32.out | cut -c1-200
sh $SP/tstep.sh "20b B the tape, first run" sh -c "python3 World/step9/cold_run_sequence.py > $SP/ch32_tape_run1.out 2>&1"
echo "tape rc $?"
/usr/bin/grep "checkpoints\|CHECKPOINT DN\|MISS\|DIVERGE\|Traceback\|Error" $SP/ch32_tape_run1.out | cut -c1-220 | head -24
sh $SP/tstep.sh "20b B checkpoint_check --all (after the tape)" sh -c "python3 World/step9/checkpoint_check.py --all > $SP/ch32_checkpoint_check.out 2>&1"
tail -1 $SP/ch32_checkpoint_check.out | cut -c1-200

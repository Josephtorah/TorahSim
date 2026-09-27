#!/bin/sh
# THE DEUTERONOMY WALK 16b: the tape's chain — the recorder with the cache OFF (7b's lesson 1) -> the stitcher (no marker; thirteen own-day lines) -> the literals
# patched from the stitcher's print (DJ1-DJ5; the stale literals retyped as the grep reads them) -> the tape's first run -> checkpoint_check.py --all AFTER the tape; every step timed;
# the chain stops at the first failure. 15b's form (ch17_tape_chain.sh). RUN FROM THE REPO ROOT (launched in the background — the cache law).
SP="$(cd "$(dirname "$0")" && pwd)"
cd "$(git rev-parse --show-toplevel)" || exit 2
export TIMING=$SP/ch19b_timing.tsv   # 16b: the compile sitting's own table (12b's form named the reading's)
sh $SP/tstep.sh "16b B the recorder (INK_CACHE=0)" sh -c "INK_CACHE=0 python3 $SP/seq_record_ch19.py > $SP/seq_record_ch19.out 2>&1" || { tail -3 $SP/seq_record_ch19.out; exit 1; }
tail -2 $SP/seq_record_ch19.out; /usr/bin/grep "refuge_war_family\|courts_prophet " $SP/seq_record_ch19.out | head -3
sh $SP/tstep.sh "16b B the stitcher (no marker)" sh -c "python3 $SP/seq_stitch_ch19.py > $SP/seq_stitch_ch19.out 2>&1" || { tail -3 $SP/seq_stitch_ch19.out; exit 1; }
/usr/bin/grep "PLACEMENT LITERAL\|CENSUS tuple\|tape written" $SP/seq_stitch_ch19.out | cut -c1-260
sh $SP/tstep.sh "16b B the literals patched (DJ1-DJ5; the stale literals as read)" sh -c "python3 $SP/patch_seq_literals_ch19.py > $SP/patch_seq_literals_ch19.out 2>&1" || { tail -4 $SP/patch_seq_literals_ch19.out; exit 1; }
tail -1 $SP/patch_seq_literals_ch19.out | cut -c1-200
sh $SP/tstep.sh "16b B the tape, first run" sh -c "python3 World/step9/cold_run_sequence.py > $SP/ch19_tape_run1.out 2>&1"
echo "tape rc $?"
/usr/bin/grep "checkpoints\|CHECKPOINT DJ\|MISS\|DIVERGE\|Traceback\|Error" $SP/ch19_tape_run1.out | cut -c1-220 | head -24
sh $SP/tstep.sh "16b B checkpoint_check --all (after the tape)" sh -c "python3 World/step9/checkpoint_check.py --all > $SP/ch19_checkpoint_check.out 2>&1"
tail -1 $SP/ch19_checkpoint_check.out | cut -c1-200

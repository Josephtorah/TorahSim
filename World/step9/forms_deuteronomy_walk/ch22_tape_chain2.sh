#!/bin/sh
# THE DEUTERONOMY WALK 17b: the tape's SECOND run after the seats were widened and the runner's source changed (the import notes; the good_land word list) — the recorder
# (INK_CACHE=0), the stitcher (the literals already patched — the sentinels' section alone rewritten), the tape's second run, checkpoint_check --all, THE SCAN CENSUS
# after; every step timed; one DONE file. A PASS AFTER ANY SOURCE CHANGE STARTS AT THE TAPE. RUN FROM THE REPO ROOT.
SP="$(cd "$(dirname "$0")" && pwd)"
cd "$(git rev-parse --show-toplevel)" || exit 2
export TIMING=$SP/ch22b_timing.tsv
rm -f $SP/ch22_tape2.DONE
sh $SP/tstep.sh "17b B the recorder, second (INK_CACHE=0 — after the seats widened and the import notes amended)" sh -c "INK_CACHE=0 python3 $SP/seq_record_ch22.py > $SP/seq_record_ch22_2.out 2>&1" || { tail -3 $SP/seq_record_ch22_2.out; echo "recorder failed" > $SP/ch22_tape2.DONE; exit 1; }
tail -1 $SP/seq_record_ch22_2.out; /usr/bin/grep "persons_poor_court\|refuge_war_family " $SP/seq_record_ch22_2.out | head -3
sh $SP/tstep.sh "17b B the stitcher, second (no marker; the literals stand)" sh -c "python3 $SP/seq_stitch_ch22.py > $SP/seq_stitch_ch22_2.out 2>&1" || { tail -3 $SP/seq_stitch_ch22_2.out; echo "stitcher failed" > $SP/ch22_tape2.DONE; exit 1; }
/usr/bin/grep "PLACEMENT LITERAL\|CENSUS tuple\|tape written" $SP/seq_stitch_ch22_2.out | cut -c1-260
sh $SP/tstep.sh "17b B the tape, second run (after the seats widened)" sh -c "python3 World/step9/cold_run_sequence.py > $SP/ch22_tape_run2.out 2>&1"
echo "tape rc $?"
/usr/bin/grep "checkpoints$\|^MISS\|^OK  \|CHECKPOINT DK\|Traceback\|Error" $SP/ch22_tape_run2.out | cut -c1-200 | tail -22
sh $SP/tstep.sh "17b B checkpoint_check --all (after the second tape run)" sh -c "python3 World/step9/checkpoint_check.py --all > $SP/ch22_checkpoint_check2.out 2>&1"
tail -1 $SP/ch22_checkpoint_check2.out | cut -c1-200
sh $SP/tstep.sh "17b THE SCAN CENSUS after the second run (ch22_scan_census.py)" sh -c "python3 $SP/ch22_scan_census.py > $SP/ch22_scan_census2.out 2>&1"
/usr/bin/grep "present:\|SCAN CENSUS DONE" $SP/ch22_scan_census2.out | cut -c1-200
echo "rc=0" > $SP/ch22_tape2.DONE

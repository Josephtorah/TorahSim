#!/bin/zsh
ROOT="$(cd "$(dirname "$0")" && git rev-parse --show-toplevel)"
SP=<scratch>
cd "$ROOT"; L=$SP/ch4_chain3.log
echo "chain3 start $(date +%H:%M:%S)" > $L
python3 $SP/seq_stitch.py > $SP/seq_stitch_ch4.out 2>&1 || { echo "STITCHER FAILED" >> $L; exit 1; }
echo "patcher $(date +%H:%M:%S)" >> $L
python3 $SP/patch_seq_literals_ch4.py > $SP/patch_seq_literals_ch4.out 2>&1 || { echo "PATCHER FAILED" >> $L; exit 1; }
echo "tape run $(date +%H:%M:%S)" >> $L
python3 World/step9/cold_run_sequence.py > $SP/tape_run_ch4_1.out 2>&1; echo "tape exit $? $(date +%H:%M:%S)" >> $L
echo CHAIN3_DONE >> $L

#!/bin/zsh
ROOT="$(cd "$(dirname "$0")" && git rev-parse --show-toplevel)"
SP=<scratch>
cd "$ROOT"
L=$SP/ch4_chain2.log
echo "chain2 start $(date +%H:%M:%S)" > $L
python3 - <<EOF
import time, os
for i in range(240):
    t = open('$SP/ch4_cases_gen.out', errors='ignore').read() if os.path.exists('$SP/ch4_cases_gen.out') else ''
    if 'GEN_DONE' in t: break
    time.sleep(5)
EOF
grep -q "CASES generated" $SP/ch4_cases_gen.out || { echo "GENERATOR FAILED $(date +%H:%M:%S)" >> $L; exit 1; }
N=$(grep -o 'CASES generated: [0-9]*' $SP/ch4_cases_gen.out | grep -o '[0-9]*$')
echo "generated $N $(date +%H:%M:%S)" >> $L
PYTHONPATH=$SP python3 $SP/ch4_assemble.py --guard $N >> $L 2>&1 || { echo "ASSEMBLE FAILED" >> $L; exit 1; }
echo "runner run $(date +%H:%M:%S)" >> $L
python3 World/step9/cold_run_obey_horeb.py > $SP/ch4_run1.out 2>&1; echo "runner exit $? $(date +%H:%M:%S)" >> $L
grep -q "REPRODUCED" $SP/ch4_run1.out || { echo "RUNNER MISS" >> $L; exit 1; }
echo "recorder $(date +%H:%M:%S)" >> $L
python3 $SP/seq_record.py > $SP/seq_record_ch4.out 2>&1 || { echo "RECORDER FAILED" >> $L; exit 1; }
echo "stitcher $(date +%H:%M:%S)" >> $L
python3 $SP/seq_stitch.py > $SP/seq_stitch_ch4.out 2>&1 || { echo "STITCHER FAILED" >> $L; exit 1; }
echo "patcher $(date +%H:%M:%S)" >> $L
python3 $SP/patch_seq_literals_ch4.py > $SP/patch_seq_literals_ch4.out 2>&1 || { echo "PATCHER FAILED" >> $L; exit 1; }
echo "tape run $(date +%H:%M:%S)" >> $L
python3 World/step9/cold_run_sequence.py > $SP/tape_run_ch4_1.out 2>&1; echo "tape exit $? $(date +%H:%M:%S)" >> $L
echo CHAIN2_DONE >> $L

#!/bin/zsh
SP=<scratch>
cd <repo-old>
echo "=== seat $(date +%H:%M:%S)" > $SP/chukat_chain.log
python3 $SP/seat_chukat.py >> $SP/chukat_chain.log 2>&1 || { echo "SEAT FAILED" >> $SP/chukat_chain.log; exit 1; }
for u in num_19_parah num_20_meribah_edom_aaron num_21_snakes_conquest; do
  echo "=== verify_text $u $(date +%H:%M:%S)" >> $SP/chukat_chain.log
  python3 <repo-old>/logic/solo_tools/verify_text.py $u > $SP/chukat_vt_$u.out 2>&1; echo "exit $? $(tail -1 $SP/chukat_vt_$u.out)" >> $SP/chukat_chain.log
done
for u in num_19_parah num_20_meribah_edom_aaron num_21_snakes_conquest; do
  echo "=== ritual $u $(date +%H:%M:%S)" >> $SP/chukat_chain.log
  python3 <repo-old>/logic/solo_tools/freeze_ritual.py $u > $SP/chukat_ritual_$u.out 2>&1
  echo "exit $? $(tail -1 $SP/chukat_ritual_$u.out)" >> $SP/chukat_chain.log
done
echo ALL_DONE >> $SP/chukat_chain.log

#!/bin/zsh
SP=<scratch>
cd <repo-old>
echo "=== seat $(date +%H:%M:%S)" > $SP/shelach_chain.log
python3 $SP/seat_shelach.py >> $SP/shelach_chain.log 2>&1 || { echo "SEAT FAILED" >> $SP/shelach_chain.log; exit 1; }
for u in num_13_spies_sent num_14_rejection num_15_offerings_laws; do
  echo "=== verify_text $u $(date +%H:%M:%S)" >> $SP/shelach_chain.log
  python3 <repo-old>/logic/solo_tools/verify_text.py $u > $SP/shelach_vt_$u.out 2>&1; echo "exit $? $(tail -1 $SP/shelach_vt_$u.out)" >> $SP/shelach_chain.log
done
for u in num_13_spies_sent num_14_rejection num_15_offerings_laws; do
  echo "=== ritual $u $(date +%H:%M:%S)" >> $SP/shelach_chain.log
  python3 <repo-old>/logic/solo_tools/freeze_ritual.py $u > $SP/shelach_ritual_$u.out 2>&1
  echo "exit $? $(tail -1 $SP/shelach_ritual_$u.out)" >> $SP/shelach_chain.log
done
echo ALL_DONE >> $SP/shelach_chain.log

#!/bin/zsh
SP=<scratch>
cd <repo-old>
echo "=== chain start $(date +%H:%M:%S)" > $SP/ref_chain.log
for u in num_35_refuge_cities; do
  echo "=== seat $u $(date +%H:%M:%S)" >> $SP/ref_chain.log
  python3 $SP/seat_ref.py $u >> $SP/ref_chain.log 2>&1 || { echo "SEAT FAILED $u" >> $SP/ref_chain.log; exit 1; }
  echo "=== verify_text $u $(date +%H:%M:%S)" >> $SP/ref_chain.log
  python3 <repo-old>/logic/solo_tools/verify_text.py $u > $SP/ref_vt_$u.out 2>&1; echo "exit $? $(tail -1 $SP/ref_vt_$u.out)" >> $SP/ref_chain.log
  echo "=== ritual $u $(date +%H:%M:%S)" >> $SP/ref_chain.log
  python3 <repo-old>/logic/solo_tools/freeze_ritual.py $u > $SP/ref_ritual_$u.out 2>&1
  echo "exit $? $(tail -1 $SP/ref_ritual_$u.out)" >> $SP/ref_chain.log
  grep -q "RITUAL COMPLETE" $SP/ref_ritual_$u.out || { echo "RITUAL NOT COMPLETE $u" >> $SP/ref_chain.log; exit 1; }
done
echo ALL_DONE >> $SP/ref_chain.log

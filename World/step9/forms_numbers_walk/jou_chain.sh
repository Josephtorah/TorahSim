#!/bin/zsh
SP=<scratch>
cd <repo-old>
echo "=== chain start $(date +%H:%M:%S)" > $SP/jou_chain.log
for u in num_33_journeys; do
  echo "=== seat $u $(date +%H:%M:%S)" >> $SP/jou_chain.log
  python3 $SP/seat_jou.py $u >> $SP/jou_chain.log 2>&1 || { echo "SEAT FAILED $u" >> $SP/jou_chain.log; exit 1; }
  echo "=== verify_text $u $(date +%H:%M:%S)" >> $SP/jou_chain.log
  python3 <repo-old>/logic/solo_tools/verify_text.py $u > $SP/jou_vt_$u.out 2>&1; echo "exit $? $(tail -1 $SP/jou_vt_$u.out)" >> $SP/jou_chain.log
  echo "=== ritual $u $(date +%H:%M:%S)" >> $SP/jou_chain.log
  python3 <repo-old>/logic/solo_tools/freeze_ritual.py $u > $SP/jou_ritual_$u.out 2>&1
  echo "exit $? $(tail -1 $SP/jou_ritual_$u.out)" >> $SP/jou_chain.log
  grep -q "RITUAL COMPLETE" $SP/jou_ritual_$u.out || { echo "RITUAL NOT COMPLETE $u" >> $SP/jou_chain.log; exit 1; }
done
echo ALL_DONE >> $SP/jou_chain.log

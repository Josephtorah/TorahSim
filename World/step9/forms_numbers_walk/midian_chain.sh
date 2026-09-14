#!/bin/zsh
SP=<scratch>
cd <repo-old>
echo "=== chain start $(date +%H:%M:%S)" > $SP/midian_chain.log
for u in num_31_midian; do
  echo "=== seat $u $(date +%H:%M:%S)" >> $SP/midian_chain.log
  python3 $SP/seat_midian.py $u >> $SP/midian_chain.log 2>&1 || { echo "SEAT FAILED $u" >> $SP/midian_chain.log; exit 1; }
  echo "=== verify_text $u $(date +%H:%M:%S)" >> $SP/midian_chain.log
  python3 <repo-old>/logic/solo_tools/verify_text.py $u > $SP/midian_vt_$u.out 2>&1; echo "exit $? $(tail -1 $SP/midian_vt_$u.out)" >> $SP/midian_chain.log
  echo "=== ritual $u $(date +%H:%M:%S)" >> $SP/midian_chain.log
  python3 <repo-old>/logic/solo_tools/freeze_ritual.py $u > $SP/midian_ritual_$u.out 2>&1
  echo "exit $? $(tail -1 $SP/midian_ritual_$u.out)" >> $SP/midian_chain.log
  grep -q "RITUAL COMPLETE" $SP/midian_ritual_$u.out || { echo "RITUAL NOT COMPLETE $u" >> $SP/midian_chain.log; exit 1; }
done
echo ALL_DONE >> $SP/midian_chain.log

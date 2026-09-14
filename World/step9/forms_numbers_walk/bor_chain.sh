#!/bin/zsh
SP=<scratch>
cd <repo-old>
echo "=== chain start $(date +%H:%M:%S)" > $SP/bor_chain.log
for u in num_34_borders; do
  echo "=== seat $u $(date +%H:%M:%S)" >> $SP/bor_chain.log
  python3 $SP/seat_bor.py $u >> $SP/bor_chain.log 2>&1 || { echo "SEAT FAILED $u" >> $SP/bor_chain.log; exit 1; }
  echo "=== verify_text $u $(date +%H:%M:%S)" >> $SP/bor_chain.log
  python3 <repo-old>/logic/solo_tools/verify_text.py $u > $SP/bor_vt_$u.out 2>&1; echo "exit $? $(tail -1 $SP/bor_vt_$u.out)" >> $SP/bor_chain.log
  echo "=== ritual $u $(date +%H:%M:%S)" >> $SP/bor_chain.log
  python3 <repo-old>/logic/solo_tools/freeze_ritual.py $u > $SP/bor_ritual_$u.out 2>&1
  echo "exit $? $(tail -1 $SP/bor_ritual_$u.out)" >> $SP/bor_chain.log
  grep -q "RITUAL COMPLETE" $SP/bor_ritual_$u.out || { echo "RITUAL NOT COMPLETE $u" >> $SP/bor_chain.log; exit 1; }
done
echo ALL_DONE >> $SP/bor_chain.log

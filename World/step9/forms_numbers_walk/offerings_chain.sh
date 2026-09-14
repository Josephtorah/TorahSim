#!/bin/zsh
SP=<scratch>
cd <repo-old>
echo "=== chain start $(date +%H:%M:%S)" > $SP/offerings_chain.log
for u in num_28_daily_shabbat_rosh num_28_pesach_shavuot num_29_fall_festivals; do
  echo "=== seat $u $(date +%H:%M:%S)" >> $SP/offerings_chain.log
  python3 $SP/seat_offerings.py $u >> $SP/offerings_chain.log 2>&1 || { echo "SEAT FAILED $u" >> $SP/offerings_chain.log; exit 1; }
  echo "=== verify_text $u $(date +%H:%M:%S)" >> $SP/offerings_chain.log
  python3 <repo-old>/logic/solo_tools/verify_text.py $u > $SP/offerings_vt_$u.out 2>&1; echo "exit $? $(tail -1 $SP/offerings_vt_$u.out)" >> $SP/offerings_chain.log
  echo "=== ritual $u $(date +%H:%M:%S)" >> $SP/offerings_chain.log
  python3 <repo-old>/logic/solo_tools/freeze_ritual.py $u > $SP/offerings_ritual_$u.out 2>&1
  echo "exit $? $(tail -1 $SP/offerings_ritual_$u.out)" >> $SP/offerings_chain.log
  grep -q "RITUAL COMPLETE" $SP/offerings_ritual_$u.out || { echo "RITUAL NOT COMPLETE $u" >> $SP/offerings_chain.log; exit 1; }
done
echo ALL_DONE >> $SP/offerings_chain.log

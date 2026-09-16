#!/bin/zsh
ROOT="$(cd "$(dirname "$0")" && git rev-parse --show-toplevel)"
SP=<scratch>
cd "$ROOT"
echo "=== chain start $(date +%H:%M:%S)" > $SP/ch4_chain.log
for u in deu_04_obey_horeb deu_04_refuge_east; do
  echo "=== seat $u $(date +%H:%M:%S)" >> $SP/ch4_chain.log
  python3 $SP/seat_ch4.py $u >> $SP/ch4_chain.log 2>&1 || { echo "SEAT FAILED $u" >> $SP/ch4_chain.log; exit 1; }
  echo "=== verify_text $u $(date +%H:%M:%S)" >> $SP/ch4_chain.log
  python3 "$ROOT"/logic/solo_tools/verify_text.py $u > $SP/ch4_vt_$u.out 2>&1; echo "exit $? $(tail -1 $SP/ch4_vt_$u.out)" >> $SP/ch4_chain.log
  echo "=== ritual $u $(date +%H:%M:%S)" >> $SP/ch4_chain.log
  python3 "$ROOT"/logic/solo_tools/freeze_ritual.py $u > $SP/ch4_ritual_$u.out 2>&1
  echo "exit $? $(tail -1 $SP/ch4_ritual_$u.out)" >> $SP/ch4_chain.log
  grep -q "RITUAL COMPLETE" $SP/ch4_ritual_$u.out || { echo "RITUAL NOT COMPLETE $u" >> $SP/ch4_chain.log; exit 1; }
done
echo ALL_DONE >> $SP/ch4_chain.log

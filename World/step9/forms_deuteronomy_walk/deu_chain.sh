#!/bin/zsh
ROOT="$(cd "$(dirname "$0")" && git rev-parse --show-toplevel)"
SP=<scratch>
cd "$ROOT"
echo "=== chain start $(date +%H:%M:%S)" > $SP/deu_chain.log
for u in deu_01_frame_officers deu_01_spies_refuse deu_02_bypass_nations deu_02_sihon deu_03_og_gilead deu_03_moses_barred; do
  echo "=== seat $u $(date +%H:%M:%S)" >> $SP/deu_chain.log
  python3 $SP/seat_deu.py $u >> $SP/deu_chain.log 2>&1 || { echo "SEAT FAILED $u" >> $SP/deu_chain.log; exit 1; }
  echo "=== verify_text $u $(date +%H:%M:%S)" >> $SP/deu_chain.log
  python3 "$ROOT"/logic/solo_tools/verify_text.py $u > $SP/deu_vt_$u.out 2>&1; echo "exit $? $(tail -1 $SP/deu_vt_$u.out)" >> $SP/deu_chain.log
  echo "=== ritual $u $(date +%H:%M:%S)" >> $SP/deu_chain.log
  python3 "$ROOT"/logic/solo_tools/freeze_ritual.py $u > $SP/deu_ritual_$u.out 2>&1
  echo "exit $? $(tail -1 $SP/deu_ritual_$u.out)" >> $SP/deu_chain.log
  grep -q "RITUAL COMPLETE" $SP/deu_ritual_$u.out || { echo "RITUAL NOT COMPLETE $u" >> $SP/deu_chain.log; exit 1; }
done
echo ALL_DONE >> $SP/deu_chain.log

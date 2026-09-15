#!/bin/zsh
ROOT="$(cd "$(dirname "$0")" && git rev-parse --show-toplevel)"   # THE PORTABLE REPO (2026-09-15): the repo root from this script's own place
SP=<scratch>
cd "$ROOT"
echo "=== seat $(date +%H:%M:%S)" > $SP/balak_chain.log
python3 $SP/seat_balak.py >> $SP/balak_chain.log 2>&1 || { echo "SEAT FAILED" >> $SP/balak_chain.log; exit 1; }
for u in num_22_balak_bilam_call num_23_oracles_1_2 num_24_oracles_3_4 num_25_peor_pinchas; do
  echo "=== verify_text $u $(date +%H:%M:%S)" >> $SP/balak_chain.log
  python3 "$ROOT"/logic/solo_tools/verify_text.py $u > $SP/balak_vt_$u.out 2>&1; echo "exit $? $(tail -1 $SP/balak_vt_$u.out)" >> $SP/balak_chain.log
done
for u in num_22_balak_bilam_call num_23_oracles_1_2 num_24_oracles_3_4 num_25_peor_pinchas; do
  echo "=== ritual $u $(date +%H:%M:%S)" >> $SP/balak_chain.log
  python3 "$ROOT"/logic/solo_tools/freeze_ritual.py $u > $SP/balak_ritual_$u.out 2>&1
  echo "exit $? $(tail -1 $SP/balak_ritual_$u.out)" >> $SP/balak_chain.log
done
echo ALL_DONE >> $SP/balak_chain.log

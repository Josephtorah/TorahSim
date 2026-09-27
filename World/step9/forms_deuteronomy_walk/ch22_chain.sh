#!/bin/zsh
# THE DEUTERONOMY WALK sitting 17 — CHAPTERS 22-25 (LEAN): seat (once per unit) → verify_text → the freeze ritual, for the FOUR units in order; run from the repo root.
# Sitting 16's form (ch19_chain.sh); SP the scratchpad this script lives in.
ROOT="$(git rev-parse --show-toplevel)"
SP="$(cd "$(dirname "$0")" && pwd)"
cd "$ROOT"
echo "=== chain start $(date +%H:%M:%S) ROOT=$ROOT" > $SP/ch22_chain.log
for u in deu_22_return_sex_laws deu_23_qahal_purity_vows deu_24_divorce_poor deu_25_courts_yibbum; do
  if grep -q '^    operators:' "$ROOT"/logic/units/$u.yaml; then echo "=== seat $u already done (operators present)" >> $SP/ch22_chain.log; else
  echo "=== seat $u $(date +%H:%M:%S)" >> $SP/ch22_chain.log
  python3 $SP/seat_ch22.py $u >> $SP/ch22_chain.log 2>&1 || { echo "SEAT FAILED $u" >> $SP/ch22_chain.log; exit 1; }; fi
  echo "=== verify_text $u $(date +%H:%M:%S)" >> $SP/ch22_chain.log
  python3 "$ROOT"/logic/solo_tools/verify_text.py $u > $SP/ch22_vt_$u.out 2>&1; echo "exit $? $(tail -1 $SP/ch22_vt_$u.out)" >> $SP/ch22_chain.log
  echo "=== ritual $u $(date +%H:%M:%S)" >> $SP/ch22_chain.log
  python3 "$ROOT"/logic/solo_tools/freeze_ritual.py $u > $SP/ch22_ritual_$u.out 2>&1
  echo "exit $? $(tail -1 $SP/ch22_ritual_$u.out)" >> $SP/ch22_chain.log
  grep -q "RITUAL COMPLETE" $SP/ch22_ritual_$u.out || { echo "RITUAL NOT COMPLETE $u" >> $SP/ch22_chain.log; exit 1; }
done
echo ALL_DONE >> $SP/ch22_chain.log

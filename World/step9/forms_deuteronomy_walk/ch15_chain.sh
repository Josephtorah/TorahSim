#!/bin/zsh
# THE DEUTERONOMY WALK sitting 13 — CHAPTER 15 (two runs and the tail): seat (once) → verify_text → the freeze ritual; run from the repo root (ROOT from the cwd's git).
# Sitting 12's form (ch14_chain.sh); SP the scratchpad this script lives in.
ROOT="$(git rev-parse --show-toplevel)"
SP="$(cd "$(dirname "$0")" && pwd)"
cd "$ROOT"
echo "=== chain start $(date +%H:%M:%S) ROOT=$ROOT" > $SP/ch15_chain.log
for u in deu_15_release_firstborn; do
  if grep -q '^    operators:' "$ROOT"/logic/units/$u.yaml; then echo "=== seat $u already done (operators present)" >> $SP/ch15_chain.log; else
  echo "=== seat $u $(date +%H:%M:%S)" >> $SP/ch15_chain.log
  python3 $SP/seat_ch15.py $u >> $SP/ch15_chain.log 2>&1 || { echo "SEAT FAILED $u" >> $SP/ch15_chain.log; exit 1; }; fi
  echo "=== verify_text $u $(date +%H:%M:%S)" >> $SP/ch15_chain.log
  python3 "$ROOT"/logic/solo_tools/verify_text.py $u > $SP/ch15_vt_$u.out 2>&1; echo "exit $? $(tail -1 $SP/ch15_vt_$u.out)" >> $SP/ch15_chain.log
  echo "=== ritual $u $(date +%H:%M:%S)" >> $SP/ch15_chain.log
  python3 "$ROOT"/logic/solo_tools/freeze_ritual.py $u > $SP/ch15_ritual_$u.out 2>&1
  echo "exit $? $(tail -1 $SP/ch15_ritual_$u.out)" >> $SP/ch15_chain.log
  grep -q "RITUAL COMPLETE" $SP/ch15_ritual_$u.out || { echo "RITUAL NOT COMPLETE $u" >> $SP/ch15_chain.log; exit 1; }
done
echo ALL_DONE >> $SP/ch15_chain.log

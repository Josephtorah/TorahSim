#!/bin/zsh
# THE DEUTERONOMY WALK sitting 5 — CHAPTER 7 (run 3): seat (once) → verify_text → the freeze ritual; run from the repo root (ROOT from the cwd's git).
# Sitting 4's form (ch6_chain.sh); SP the scratchpad this script lives in.
ROOT="$(git rev-parse --show-toplevel)"
SP="$(cd "$(dirname "$0")" && pwd)"
cd "$ROOT"
echo "=== chain start $(date +%H:%M:%S) ROOT=$ROOT" > $SP/ch7_chain.log
for u in deu_07_nations_cherem; do
  if grep -q '^    operators:' "$ROOT"/logic/units/$u.yaml; then echo "=== seat $u already done (operators present)" >> $SP/ch7_chain.log; else
  echo "=== seat $u $(date +%H:%M:%S)" >> $SP/ch7_chain.log
  python3 $SP/seat_ch7.py $u >> $SP/ch7_chain.log 2>&1 || { echo "SEAT FAILED $u" >> $SP/ch7_chain.log; exit 1; }; fi
  echo "=== verify_text $u $(date +%H:%M:%S)" >> $SP/ch7_chain.log
  python3 "$ROOT"/logic/solo_tools/verify_text.py $u > $SP/ch7_vt_$u.out 2>&1; echo "exit $? $(tail -1 $SP/ch7_vt_$u.out)" >> $SP/ch7_chain.log
  echo "=== ritual $u $(date +%H:%M:%S)" >> $SP/ch7_chain.log
  python3 "$ROOT"/logic/solo_tools/freeze_ritual.py $u > $SP/ch7_ritual_$u.out 2>&1
  echo "exit $? $(tail -1 $SP/ch7_ritual_$u.out)" >> $SP/ch7_chain.log
  grep -q "RITUAL COMPLETE" $SP/ch7_ritual_$u.out || { echo "RITUAL NOT COMPLETE $u" >> $SP/ch7_chain.log; exit 1; }
done
echo ALL_DONE >> $SP/ch7_chain.log

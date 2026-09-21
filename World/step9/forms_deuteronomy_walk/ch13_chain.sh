#!/bin/zsh
# THE DEUTERONOMY WALK sitting 11 — CHAPTER 13 (the one run and its tail): seat (once) → verify_text → the freeze ritual; run from the repo root (ROOT from the cwd's git).
# Sitting 10's form (ch12_chain.sh); SP the scratchpad this script lives in.
ROOT="$(git rev-parse --show-toplevel)"
SP="$(cd "$(dirname "$0")" && pwd)"
cd "$ROOT"
echo "=== chain start $(date +%H:%M:%S) ROOT=$ROOT" > $SP/ch13_chain.log
for u in deu_13_seducers; do
  if grep -q '^    operators:' "$ROOT"/logic/units/$u.yaml; then echo "=== seat $u already done (operators present)" >> $SP/ch13_chain.log; else
  echo "=== seat $u $(date +%H:%M:%S)" >> $SP/ch13_chain.log
  python3 $SP/seat_ch13.py $u >> $SP/ch13_chain.log 2>&1 || { echo "SEAT FAILED $u" >> $SP/ch13_chain.log; exit 1; }; fi
  echo "=== verify_text $u $(date +%H:%M:%S)" >> $SP/ch13_chain.log
  python3 "$ROOT"/logic/solo_tools/verify_text.py $u > $SP/ch13_vt_$u.out 2>&1; echo "exit $? $(tail -1 $SP/ch13_vt_$u.out)" >> $SP/ch13_chain.log
  echo "=== ritual $u $(date +%H:%M:%S)" >> $SP/ch13_chain.log
  python3 "$ROOT"/logic/solo_tools/freeze_ritual.py $u > $SP/ch13_ritual_$u.out 2>&1
  echo "exit $? $(tail -1 $SP/ch13_ritual_$u.out)" >> $SP/ch13_chain.log
  grep -q "RITUAL COMPLETE" $SP/ch13_ritual_$u.out || { echo "RITUAL NOT COMPLETE $u" >> $SP/ch13_chain.log; exit 1; }
done
echo ALL_DONE >> $SP/ch13_chain.log

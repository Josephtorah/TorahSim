#!/bin/zsh
# THE DEUTERONOMY WALK sitting 22 — CHAPTER 34, THE DEATH OF MOSES (LEAN): seat (once per unit) → verify_text → the freeze ritual, for the ONE unit; run from the repo root.
# Sitting 21's form (ch34_chain.sh); SP the scratchpad this script lives in.
ROOT="$(git rev-parse --show-toplevel)"
SP="$(cd "$(dirname "$0")" && pwd)"
cd "$ROOT"
echo "=== chain start $(date +%H:%M:%S) ROOT=$ROOT" > $SP/ch34_chain.log
for u in deu_34_moses_death; do
  if grep -q '^    operators:' "$ROOT"/logic/units/$u.yaml; then echo "=== seat $u already done (operators present)" >> $SP/ch34_chain.log; else
  echo "=== seat $u $(date +%H:%M:%S)" >> $SP/ch34_chain.log
  python3 $SP/seat_ch34.py $u >> $SP/ch34_chain.log 2>&1 || { echo "SEAT FAILED $u" >> $SP/ch34_chain.log; exit 1; }; fi
  echo "=== verify_text $u $(date +%H:%M:%S)" >> $SP/ch34_chain.log
  python3 "$ROOT"/logic/solo_tools/verify_text.py $u > $SP/ch34_vt_$u.out 2>&1; echo "exit $? $(tail -1 $SP/ch34_vt_$u.out)" >> $SP/ch34_chain.log
  echo "=== ritual $u $(date +%H:%M:%S)" >> $SP/ch34_chain.log
  python3 "$ROOT"/logic/solo_tools/freeze_ritual.py $u > $SP/ch34_ritual_$u.out 2>&1
  echo "exit $? $(tail -1 $SP/ch34_ritual_$u.out)" >> $SP/ch34_chain.log
  grep -q "RITUAL COMPLETE" $SP/ch34_ritual_$u.out || { echo "RITUAL NOT COMPLETE $u" >> $SP/ch34_chain.log; exit 1; }
done
echo ALL_DONE >> $SP/ch34_chain.log

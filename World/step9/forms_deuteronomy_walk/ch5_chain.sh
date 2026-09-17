#!/bin/zsh
# THE DEUTERONOMY WALK sitting 3 — CHAPTER 5: seat (once) → verify_text → the freeze ritual; run from the repo root (ROOT from the cwd's git)
ROOT="$(git rev-parse --show-toplevel)"
SP=<scratch>
cd "$ROOT"
echo "=== chain start $(date +%H:%M:%S) ROOT=$ROOT" > $SP/ch5_chain.log
for u in deu_05_decalogue; do
  if grep -q '^    operators:' "$ROOT"/logic/units/$u.yaml; then echo "=== seat $u already done (operators present)" >> $SP/ch5_chain.log; else
  echo "=== seat $u $(date +%H:%M:%S)" >> $SP/ch5_chain.log
  python3 $SP/seat_ch5.py $u >> $SP/ch5_chain.log 2>&1 || { echo "SEAT FAILED $u" >> $SP/ch5_chain.log; exit 1; }; fi
  echo "=== verify_text $u $(date +%H:%M:%S)" >> $SP/ch5_chain.log
  python3 "$ROOT"/logic/solo_tools/verify_text.py $u > $SP/ch5_vt_$u.out 2>&1; echo "exit $? $(tail -1 $SP/ch5_vt_$u.out)" >> $SP/ch5_chain.log
  echo "=== ritual $u $(date +%H:%M:%S)" >> $SP/ch5_chain.log
  python3 "$ROOT"/logic/solo_tools/freeze_ritual.py $u > $SP/ch5_ritual_$u.out 2>&1
  echo "exit $? $(tail -1 $SP/ch5_ritual_$u.out)" >> $SP/ch5_chain.log
  grep -q "RITUAL COMPLETE" $SP/ch5_ritual_$u.out || { echo "RITUAL NOT COMPLETE $u" >> $SP/ch5_chain.log; exit 1; }
done
echo ALL_DONE >> $SP/ch5_chain.log

#!/bin/zsh
# THE DEUTERONOMY WALK sitting 18 — CHAPTERS 26-28 (LEAN): seat (once per unit) → verify_text → the freeze ritual, for the FIVE units in order; run from the repo root.
# Sitting 17's form (ch22_chain.sh); SP the scratchpad this script lives in.
ROOT="$(git rev-parse --show-toplevel)"
SP="$(cd "$(dirname "$0")" && pwd)"
cd "$ROOT"
echo "=== chain start $(date +%H:%M:%S) ROOT=$ROOT" > $SP/ch26_chain.log
for u in deu_26_bikkurim_close deu_27_ebal_curses deu_28_blessings deu_28_curses_a deu_28_curses_b; do
  if grep -q '^    operators:' "$ROOT"/logic/units/$u.yaml; then echo "=== seat $u already done (operators present)" >> $SP/ch26_chain.log; else
  echo "=== seat $u $(date +%H:%M:%S)" >> $SP/ch26_chain.log
  python3 $SP/seat_ch26.py $u >> $SP/ch26_chain.log 2>&1 || { echo "SEAT FAILED $u" >> $SP/ch26_chain.log; exit 1; }; fi
  echo "=== verify_text $u $(date +%H:%M:%S)" >> $SP/ch26_chain.log
  python3 "$ROOT"/logic/solo_tools/verify_text.py $u > $SP/ch26_vt_$u.out 2>&1; echo "exit $? $(tail -1 $SP/ch26_vt_$u.out)" >> $SP/ch26_chain.log
  echo "=== ritual $u $(date +%H:%M:%S)" >> $SP/ch26_chain.log
  python3 "$ROOT"/logic/solo_tools/freeze_ritual.py $u > $SP/ch26_ritual_$u.out 2>&1
  echo "exit $? $(tail -1 $SP/ch26_ritual_$u.out)" >> $SP/ch26_chain.log
  grep -q "RITUAL COMPLETE" $SP/ch26_ritual_$u.out || { echo "RITUAL NOT COMPLETE $u" >> $SP/ch26_chain.log; exit 1; }
done
echo ALL_DONE >> $SP/ch26_chain.log

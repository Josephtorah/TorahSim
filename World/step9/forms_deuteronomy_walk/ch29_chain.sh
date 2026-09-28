#!/bin/zsh
# THE DEUTERONOMY WALK sitting 19 — CHAPTERS 29-31 (LEAN): seat (once per unit) → verify_text → the freeze ritual, for the THREE units in order; run from the repo root.
# Sitting 18's form (ch26_chain.sh); SP the scratchpad this script lives in.
ROOT="$(git rev-parse --show-toplevel)"
SP="$(cd "$(dirname "$0")" && pwd)"
cd "$ROOT"
echo "=== chain start $(date +%H:%M:%S) ROOT=$ROOT" > $SP/ch29_chain.log
for u in deu_29_moab_covenant deu_30_teshuvah_choice deu_31_charge_torah; do
  if grep -q '^    operators:' "$ROOT"/logic/units/$u.yaml; then echo "=== seat $u already done (operators present)" >> $SP/ch29_chain.log; else
  echo "=== seat $u $(date +%H:%M:%S)" >> $SP/ch29_chain.log
  python3 $SP/seat_ch29.py $u >> $SP/ch29_chain.log 2>&1 || { echo "SEAT FAILED $u" >> $SP/ch29_chain.log; exit 1; }; fi
  echo "=== verify_text $u $(date +%H:%M:%S)" >> $SP/ch29_chain.log
  python3 "$ROOT"/logic/solo_tools/verify_text.py $u > $SP/ch29_vt_$u.out 2>&1; echo "exit $? $(tail -1 $SP/ch29_vt_$u.out)" >> $SP/ch29_chain.log
  echo "=== ritual $u $(date +%H:%M:%S)" >> $SP/ch29_chain.log
  python3 "$ROOT"/logic/solo_tools/freeze_ritual.py $u > $SP/ch29_ritual_$u.out 2>&1
  echo "exit $? $(tail -1 $SP/ch29_ritual_$u.out)" >> $SP/ch29_chain.log
  grep -q "RITUAL COMPLETE" $SP/ch29_ritual_$u.out || { echo "RITUAL NOT COMPLETE $u" >> $SP/ch29_chain.log; exit 1; }
done
echo ALL_DONE >> $SP/ch29_chain.log

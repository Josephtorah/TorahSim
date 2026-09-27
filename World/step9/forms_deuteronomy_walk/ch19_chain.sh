#!/bin/zsh
# THE DEUTERONOMY WALK sitting 16 — CHAPTERS 19-21 (LEAN): seat (once per unit) → verify_text → the freeze ritual, for the THREE units in order; run from the repo root.
# Sitting 15's form (ch17_chain.sh); SP the scratchpad this script lives in.
ROOT="$(git rev-parse --show-toplevel)"
SP="$(cd "$(dirname "$0")" && pwd)"
cd "$ROOT"
echo "=== chain start $(date +%H:%M:%S) ROOT=$ROOT" > $SP/ch19_chain.log
for u in deu_19_miklat_witness deu_20_war_rules deu_21_eglah_family; do
  if grep -q '^    operators:' "$ROOT"/logic/units/$u.yaml; then echo "=== seat $u already done (operators present)" >> $SP/ch19_chain.log; else
  echo "=== seat $u $(date +%H:%M:%S)" >> $SP/ch19_chain.log
  python3 $SP/seat_ch19.py $u >> $SP/ch19_chain.log 2>&1 || { echo "SEAT FAILED $u" >> $SP/ch19_chain.log; exit 1; }; fi
  echo "=== verify_text $u $(date +%H:%M:%S)" >> $SP/ch19_chain.log
  python3 "$ROOT"/logic/solo_tools/verify_text.py $u > $SP/ch19_vt_$u.out 2>&1; echo "exit $? $(tail -1 $SP/ch19_vt_$u.out)" >> $SP/ch19_chain.log
  echo "=== ritual $u $(date +%H:%M:%S)" >> $SP/ch19_chain.log
  python3 "$ROOT"/logic/solo_tools/freeze_ritual.py $u > $SP/ch19_ritual_$u.out 2>&1
  echo "exit $? $(tail -1 $SP/ch19_ritual_$u.out)" >> $SP/ch19_chain.log
  grep -q "RITUAL COMPLETE" $SP/ch19_ritual_$u.out || { echo "RITUAL NOT COMPLETE $u" >> $SP/ch19_chain.log; exit 1; }
done
echo ALL_DONE >> $SP/ch19_chain.log

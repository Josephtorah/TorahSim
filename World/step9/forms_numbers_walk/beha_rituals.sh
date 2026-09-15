#!/bin/zsh
ROOT="$(cd "$(dirname "$0")" && git rev-parse --show-toplevel)"   # THE PORTABLE REPO (2026-09-15): the repo root from this script's own place
SP=<scratch>
cd "$ROOT"
for u in num_08_menorah_levites num_10_trumpets_depart num_11_complaint_quail num_12_miriam num_03_aaron_levi_replace; do
  echo "=== $u $(date +%H:%M:%S)" >> $SP/beha_rituals.log
  python3 "$ROOT"/logic/solo_tools/freeze_ritual.py $u > $SP/beha_ritual_$u.out 2>&1
  echo "exit $? $(tail -1 $SP/beha_ritual_$u.out)" >> $SP/beha_rituals.log
done
echo ALL_RITUALS_DONE >> $SP/beha_rituals.log

#!/bin/zsh
ROOT="$(cd "$(dirname "$0")" && git rev-parse --show-toplevel)"   # THE PORTABLE REPO (2026-09-15): the repo root from this script's own place
SP=<scratch>
cd "$ROOT"
for u in num_04_gershon_merari num_05_camp_pure_theft num_05_sotah num_06_nazir num_06_priest_blessing num_07_carts_offerings_a num_07_offerings_b_total; do
  echo "=== $u $(date +%H:%M:%S)" >> $SP/naso_rituals.log
  python3 "$ROOT"/logic/solo_tools/freeze_ritual.py $u > $SP/naso_ritual_$u.out 2>&1
  echo "exit $? $(tail -1 $SP/naso_ritual_$u.out)" >> $SP/naso_rituals.log
done
echo ALL_RITUALS_DONE >> $SP/naso_rituals.log

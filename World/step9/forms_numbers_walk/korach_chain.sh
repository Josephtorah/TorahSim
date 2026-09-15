#!/bin/zsh
ROOT="$(cd "$(dirname "$0")" && git rev-parse --show-toplevel)"   # THE PORTABLE REPO (2026-09-15): the repo root from this script's own place
SP=<scratch>
cd "$ROOT"
echo "=== seat $(date +%H:%M:%S)" > $SP/korach_chain.log
python3 $SP/seat_korach.py >> $SP/korach_chain.log 2>&1 || { echo "SEAT FAILED" >> $SP/korach_chain.log; exit 1; }
for u in num_16_korach num_17_plague_staff num_18_priest_levite_dues; do
  echo "=== verify_text $u $(date +%H:%M:%S)" >> $SP/korach_chain.log
  python3 "$ROOT"/logic/solo_tools/verify_text.py $u > $SP/korach_vt_$u.out 2>&1; echo "exit $? $(tail -1 $SP/korach_vt_$u.out)" >> $SP/korach_chain.log
done
for u in num_16_korach num_17_plague_staff num_18_priest_levite_dues; do
  echo "=== ritual $u $(date +%H:%M:%S)" >> $SP/korach_chain.log
  python3 "$ROOT"/logic/solo_tools/freeze_ritual.py $u > $SP/korach_ritual_$u.out 2>&1
  echo "exit $? $(tail -1 $SP/korach_ritual_$u.out)" >> $SP/korach_chain.log
done
echo ALL_DONE >> $SP/korach_chain.log

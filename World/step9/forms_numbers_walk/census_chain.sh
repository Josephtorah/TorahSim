#!/bin/zsh
ROOT="$(cd "$(dirname "$0")" && git rev-parse --show-toplevel)"   # THE PORTABLE REPO (2026-09-15): the repo root from this script's own place
SP=<scratch>
cd "$ROOT"
u=num_26_second_census
echo "=== seat $(date +%H:%M:%S)" > $SP/census_chain.log
python3 $SP/seat_census.py >> $SP/census_chain.log 2>&1 || { echo "SEAT FAILED" >> $SP/census_chain.log; exit 1; }
echo "=== verify_text $u $(date +%H:%M:%S)" >> $SP/census_chain.log
python3 "$ROOT"/logic/solo_tools/verify_text.py $u > $SP/census_vt_$u.out 2>&1; echo "exit $? $(tail -1 $SP/census_vt_$u.out)" >> $SP/census_chain.log
echo "=== ritual $u $(date +%H:%M:%S)" >> $SP/census_chain.log
python3 "$ROOT"/logic/solo_tools/freeze_ritual.py $u > $SP/census_ritual_$u.out 2>&1
echo "exit $? $(tail -1 $SP/census_ritual_$u.out)" >> $SP/census_chain.log
echo ALL_DONE >> $SP/census_chain.log

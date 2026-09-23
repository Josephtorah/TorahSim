#!/bin/sh
SP="$(cd "$(dirname "$0")" && pwd)"
cd "$(git rev-parse --show-toplevel)" || exit 2
export TIMING=$SP/ch15b_timing.tsv
sh $SP/tstep.sh "13b B the types (add_types_ch15.py — the first run refused itself on the hole check's substring 'hebrew_slave' matching acquire_hebrew_slave, before any write; the pattern narrowed and rerun)" bash -c "set -o pipefail; python3 $SP/add_types_ch15.py > $SP/add_types_ch15.out 2>&1" || { tail -6 $SP/add_types_ch15.out; exit 1; }
cat $SP/add_types_ch15.out | cut -c1-320
sh $SP/tstep.sh "13b B the fast checker on part 1 alone (ch15_fastcheck.py — the ink block, the clock, the scans, the callees' facts)" bash -c "python3 $SP/ch15_fastcheck.py > $SP/ch15_fastcheck_run0.out 2>&1"
echo "fastcheck rc $?"; /usr/bin/grep -n "ASSERT FAIL\|ERROR\|fastcheck:" $SP/ch15_fastcheck_run0.out | cut -c1-400 | head -30
/usr/bin/grep -n "THE CLOCK (printed\|THE CALLEES (printed\|THE INK (printed" $SP/ch15_fastcheck_run0.out | cut -c1-600
echo CHAIN_DONE

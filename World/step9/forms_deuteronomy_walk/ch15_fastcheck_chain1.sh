#!/bin/sh
SP="$(cd "$(dirname "$0")" && pwd)"
cd "$(git rev-parse --show-toplevel)" || exit 2
export TIMING=$SP/ch15b_timing.tsv
sh $SP/tstep.sh "13b B derive the runner's part 1 again (the count era asked for before the clock's method — the fast checker's first pass stopped on the bare world's missing era)" python3 $SP/derive_ch15_part1.py || exit 1
sh $SP/tstep.sh "13b B the fast checker, parts 1-2 (ch15_fastcheck.py — the ink block, the clock, the scans, the callees' facts; F1-F3)" bash -c "python3 $SP/ch15_fastcheck.py > $SP/ch15_fastcheck_run1.out 2>&1"
echo "fastcheck rc $?"; /usr/bin/grep -n "ASSERT FAIL\|^ERROR\|Traceback\|fastcheck:" $SP/ch15_fastcheck_run1.out | cut -c1-500 | head -30
/usr/bin/grep -n "THE CLOCK (printed\|THE CALLEES (printed\|CLOCK: no era" $SP/ch15_fastcheck_run1.out | cut -c1-700
echo CHAIN_DONE

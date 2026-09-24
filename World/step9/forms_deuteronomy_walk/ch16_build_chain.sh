#!/bin/sh
# THE DEUTERONOMY WALK 14b: the runner's build in one background job — part 1 rederived, the fast checker (parts 1-3), the ask check, then the runner's chain
# (assemble empty -> the cases generated -> assemble with the guard's count -> the first graded run); every step timed; stops at the first failure. RUN FROM THE REPO ROOT.
SP="$(cd "$(dirname "$0")" && pwd)"
cd "$(git rev-parse --show-toplevel)" || exit 2
export TIMING=$SP/ch16b_timing.tsv
sh $SP/tstep.sh "14b derive the runner's part 1, fourth (the holes' pattern anchored at the effect name — two values naming the asherah had matched)" python3 $SP/derive_ch16_part1.py || exit 1
sh $SP/tstep.sh "14b the fast checker, parts 1-3 (ch16_fastcheck.py)" sh -c "python3 $SP/ch16_fastcheck.py > $SP/ch16_fastcheck_run1.out 2>&1"
tail -1 $SP/ch16_fastcheck_run1.out
/usr/bin/grep -q 'fails 0, part2 fails 0, part3 fails 0' $SP/ch16_fastcheck_run1.out || { /usr/bin/grep -A2 'ASSERT FAIL\|ERROR' $SP/ch16_fastcheck_run1.out | cut -c1-600 | head -30; exit 1; }
sh $SP/tstep.sh "14b every ask called (ch16_askcheck.py — the six cells and the table with the DATA rows)" sh -c "python3 $SP/ch16_askcheck.py ch16_part2.py ch16_part3.py > $SP/ch16_askcheck_run1.out 2>&1"
tail -1 $SP/ch16_askcheck_run1.out
/usr/bin/grep -q ' 0 failed' $SP/ch16_askcheck_run1.out || { /usr/bin/grep 'ASK FAIL' $SP/ch16_askcheck_run1.out | cut -c1-400 | head -20; exit 1; }
sh $SP/ch16_runner_chain.sh

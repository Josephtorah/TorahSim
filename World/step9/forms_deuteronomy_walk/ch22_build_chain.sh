#!/bin/sh
# THE DEUTERONOMY WALK 17b: the build chain — the fast checker over the seven parts -> the ask check (every ask called) -> the runner chain (assemble with CASES empty,
# the cases generated from the cells' own asks, assemble under the guard's count read from the generator's print, the first graded run); every step timed; the chain stops
# at the first failure; ONE DONE file at its end (the cache law — launched in the background, never polled). 16b's build chain's form. RUN FROM THE REPO ROOT.
SP="$(cd "$(dirname "$0")" && pwd)"
cd "$(git rev-parse --show-toplevel)" || exit 2
export TIMING=$SP/ch22b_timing.tsv
rm -f $SP/ch22_build.DONE
sh $SP/tstep.sh "17b B the fast checker, parts 1-7 (ch22_fastcheck.py)" sh -c "python3 $SP/ch22_fastcheck.py > $SP/ch22_fastcheck_run4.out 2>&1"
if ! /usr/bin/grep -q "fastcheck: part1 fails 0, part2 fails 0, part3 fails 0, part4 fails 0, part5 fails 0, part6 fails 0, part7 fails 0" $SP/ch22_fastcheck_run4.out; then echo "fastcheck not clean" > $SP/ch22_build.DONE; exit 1; fi
sh $SP/tstep.sh "17b B every ask called (ch22_askcheck.py — the sixteen cells and the table with the DATA rows)" sh -c "python3 $SP/ch22_askcheck.py > $SP/ch22_askcheck_run1.out 2>&1"
if ! /usr/bin/grep -q "askcheck: [0-9]* asks called, 0 failed" $SP/ch22_askcheck_run1.out; then echo "askcheck not clean" > $SP/ch22_build.DONE; exit 1; fi
sh $SP/ch22_runner_chain.sh > $SP/ch22_runner_chain.log 2>&1
echo "rc=$?" > $SP/ch22_build.DONE

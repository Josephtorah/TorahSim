#!/bin/sh
# THE DEUTERONOMY WALK 19b: the checks and the second pass in ONE background job (the cache law) — the fast checker and the ask checker on the parts after the fold's literals were
# retyped, then ch29_second_pass.sh (assemble under the guard, the third graded run, the dependency gate after the demands, the tape's second run, checkpoint_check --all); one DONE file.
SP="$(cd "$(dirname "$0")" && pwd)"
cd "$(git rev-parse --show-toplevel)" || exit 2
export TIMING=$SP/ch29b_timing.tsv
rm -f $SP/ch29_pass2.DONE
sh $SP/tstep.sh "19b the fast checker on parts 1-6 (the seventh pass — the 26-28 runner's kin counts retyped)" sh -c "python3 $SP/ch29_fastcheck.py > $SP/ch29_fastcheck_run9.out 2>&1"
/usr/bin/grep -q "fastcheck: part1 fails 0, part2 fails 0, part3 fails 0, part4 fails 0, part5 fails 0, part6 fails 0" $SP/ch29_fastcheck_run9.out || { echo "fastcheck failed" > $SP/ch29_pass2.DONE; exit 1; }
sh $SP/tstep.sh "19b the ask checker (the seventh pass)" sh -c "python3 $SP/ch29_askcheck.py > $SP/ch29_askcheck3.out 2>&1"
/usr/bin/grep -q "askcheck: 95 asks called, 0 failed" $SP/ch29_askcheck3.out || { echo "askcheck failed" > $SP/ch29_pass2.DONE; exit 1; }
sh $SP/ch29_second_pass.sh > $SP/ch29_second_pass.out 2>&1
echo "second pass rc $?" >> $SP/ch29_second_pass.out
echo "rc=0" > $SP/ch29_pass2.DONE

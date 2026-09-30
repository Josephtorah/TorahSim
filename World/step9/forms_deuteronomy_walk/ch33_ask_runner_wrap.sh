#!/bin/sh
# THE DEUTERONOMY WALK 21b: the ask checker, then (if every ask held) the runner's chain — one background job, one DONE file (the cache law)
SP="$(cd "$(dirname "$0")" && pwd)"
cd "$(git rev-parse --show-toplevel)" || exit 2
export TIMING=$SP/ch33b_timing.tsv
rm -f $SP/ch33_ask_runner.DONE
sh $SP/tstep.sh "21b the ask checker on parts 2-6 (every ask called)" sh -c "python3 $SP/ch33_askcheck.py > $SP/ch33_askcheck_run1.out 2>&1"
tail -1 $SP/ch33_askcheck_run1.out
if /usr/bin/grep -q "asks called, 0 failed" $SP/ch33_askcheck_run1.out; then
  sh $SP/ch33_runner_chain.sh > $SP/ch33_runner_chain.out 2>&1; echo "runner chain rc=$?" > $SP/ch33_ask_runner.DONE
else
  echo "askcheck failed" > $SP/ch33_ask_runner.DONE
fi

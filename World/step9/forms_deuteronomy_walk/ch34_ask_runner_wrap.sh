#!/bin/sh
# THE DEUTERONOMY WALK 22b: the ask checker, then (if every ask held) the runner's chain — one background job, one DONE file (the cache law)
SP="$(cd "$(dirname "$0")" && pwd)"
cd "$(git rev-parse --show-toplevel)" || exit 2
export TIMING=$SP/ch34b_timing.tsv
rm -f $SP/ch34_ask_runner.DONE
sh $SP/tstep.sh "22b the ask checker on parts 2-6 (every ask called)" sh -c "python3 $SP/ch34_askcheck.py > $SP/ch34_askcheck_run1.out 2>&1"
tail -1 $SP/ch34_askcheck_run1.out
if /usr/bin/grep -q "asks called, 0 failed" $SP/ch34_askcheck_run1.out; then
  sh $SP/ch34_runner_chain.sh > $SP/ch34_runner_chain.out 2>&1; echo "runner chain rc=$?" > $SP/ch34_ask_runner.DONE
else
  echo "askcheck failed" > $SP/ch34_ask_runner.DONE
fi

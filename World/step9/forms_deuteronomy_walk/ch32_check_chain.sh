#!/bin/sh
# THE DEUTERONOMY WALK 20b: the ask checker (every ask of every cell called on the parts) then the runner's chain (assemble, the cases generated, the first graded run) — one DONE file; launched in the background (the cache law)
SP="$(cd "$(dirname "$0")" && pwd)"
cd "$(git rev-parse --show-toplevel)" || exit 2
export TIMING=$SP/ch32b_timing.tsv
rm -f $SP/ch32_check_chain.DONE
sh $SP/tstep.sh "20b the ask checker on parts 2-6 (every ask called)" sh -c "PYTHONPATH=$SP python3 $SP/ch32_askcheck.py > $SP/ch32_askcheck_run1.out 2>&1"
tail -1 $SP/ch32_askcheck_run1.out
if /usr/bin/grep -q "asks called, 0 failed" $SP/ch32_askcheck_run1.out; then
  sh $SP/ch32_runner_chain.sh > $SP/ch32_runner_chain.out 2>&1
  echo "runner chain rc $?" >> $SP/ch32_runner_chain.out
fi
echo "rc=0" > $SP/ch32_check_chain.DONE

#!/bin/sh
# THE DEUTERONOMY WALK 21b: the ask checker on parts 2-6 in the background with a DONE file (the cache law — never poll)
SP="$(cd "$(dirname "$0")" && pwd)"
cd "$(git rev-parse --show-toplevel)" || exit 2
export TIMING=$SP/ch33b_timing.tsv
rm -f $SP/ch33_askcheck.DONE
sh $SP/tstep.sh "21b the ask checker on parts 2-6 (every ask called)" sh -c "python3 $SP/ch33_askcheck.py > $SP/ch33_askcheck_run1.out 2>&1"
echo "rc=$?" > $SP/ch33_askcheck.DONE

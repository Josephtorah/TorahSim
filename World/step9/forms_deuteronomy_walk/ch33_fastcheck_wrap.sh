#!/bin/sh
SP="$(cd "$(dirname "$0")" && pwd)"
cd "$(git rev-parse --show-toplevel)" || exit 2
export TIMING=$SP/ch33b_timing.tsv
rm -f $SP/ch33_fastcheck_run0.DONE
sh $SP/tstep.sh "21b the fast checker on part 1 (the first pass — the prints)" sh -c "python3 $SP/ch33_fastcheck.py > $SP/ch33_fastcheck_run0.out 2>&1"
echo "rc=$?" > $SP/ch33_fastcheck_run0.DONE

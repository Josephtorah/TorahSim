#!/bin/sh
# THE DEUTERONOMY WALK 22b: the fast checker's second pass -> the parser (the literals and the facts from the print) -> part 1 patched -> the ask checker -> the runner's chain (assemble, cases, assemble, the graded run) — one background job, one DONE file (the cache law)
SP="$(cd "$(dirname "$0")" && pwd)"
cd "$(git rev-parse --show-toplevel)" || exit 2
export TIMING=$SP/ch34b_timing.tsv
rm -f $SP/ch34_fast.DONE
sh $SP/tstep.sh "22b B the fast checker, second pass (the two fixes)" sh -c "python3 $SP/ch34_fastcheck.py > $SP/ch34_fastcheck_run1.out 2>&1"
tail -1 $SP/ch34_fastcheck_run1.out
if ! /usr/bin/grep -q "fastcheck: part1 fails 0, part2 fails 0, part3 fails 0, part4 fails 0, part5 fails 0, part6 fails 0" $SP/ch34_fastcheck_run1.out; then echo "fastcheck run1 failed" > $SP/ch34_fast.DONE; exit 1; fi
sh $SP/tstep.sh "22b B the parser (the literals and the facts from the print)" sh -c "python3 $SP/parse_ch34_fastcheck.py ch34_fastcheck_run1.out > $SP/ch34_parse.out 2>&1" || { cat $SP/ch34_parse.out; echo "parse failed" > $SP/ch34_fast.DONE; exit 1; }
tail -1 $SP/ch34_parse.out
sh $SP/tstep.sh "22b B part 1 patched (the literals typed from the print)" sh -c "python3 $SP/patch_part1_ch34.py > $SP/ch34_patch_part1.out 2>&1" || { cat $SP/ch34_patch_part1.out; echo "patch failed" > $SP/ch34_fast.DONE; exit 1; }
tail -1 $SP/ch34_patch_part1.out
sh $SP/tstep.sh "22b the ask checker on parts 2-6 (every ask called)" sh -c "python3 $SP/ch34_askcheck.py > $SP/ch34_askcheck_run1.out 2>&1"
tail -1 $SP/ch34_askcheck_run1.out
if /usr/bin/grep -q "asks called, 0 failed" $SP/ch34_askcheck_run1.out; then
  sh $SP/ch34_runner_chain.sh > $SP/ch34_runner_chain.out 2>&1; echo "runner chain rc=$?" > $SP/ch34_fast.DONE
else
  echo "askcheck failed" > $SP/ch34_fast.DONE
fi

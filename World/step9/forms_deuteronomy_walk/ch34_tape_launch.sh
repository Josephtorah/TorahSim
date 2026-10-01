#!/bin/sh
# THE DEUTERONOMY WALK 22b: the cases regenerated (the report main fixed — 21b's fact names and ledger list in the derived generator's main) then the tape wrap — one background job, the wrap's DONE file
SP="$(cd "$(dirname "$0")" && pwd)"
cd "$(git rev-parse --show-toplevel)" || exit 2
export TIMING=$SP/ch34b_timing.tsv
rm -f $SP/ch34_tape.DONE
sh $SP/tstep.sh "22b B cases regenerated (the report main fixed)" sh -c "python3 $SP/ch34_cases_gen.py > $SP/ch34_cases_gen.out 2>&1" || { tail -5 $SP/ch34_cases_gen.out; echo "cases_gen failed" > $SP/ch34_tape.DONE; exit 1; }
tail -1 $SP/ch34_cases_gen.out | cut -c1-200
sh $SP/ch34_tape_wrap.sh > $SP/ch34_tape_wrap.log 2>&1

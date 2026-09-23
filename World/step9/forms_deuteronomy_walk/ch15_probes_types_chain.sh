#!/bin/sh
# THE DEUTERONOMY WALK 13b: the probes patched and run to FAIL (RUN B's first step — 7b's lesson 2), THEN the types by script (12b's order); every step timed.
# RUN FROM THE REPO ROOT (launched in the background — the cache law).
SP="$(cd "$(dirname "$0")" && pwd)"
cd "$(git rev-parse --show-toplevel)" || exit 2
export TIMING=$SP/ch15b_timing.tsv
sh $SP/tstep.sh "13b B the probes patched (patch_probes_ch15.py — Q40-Q42 written to FAIL; Q21, Q30, Q32, Q39 retyped for the two reuses that held a count seat)" bash -c "set -o pipefail; python3 $SP/patch_probes_ch15.py > $SP/patch_probes_ch15.out 2>&1" || { tail -3 $SP/patch_probes_ch15.out; exit 1; }
tail -1 $SP/patch_probes_ch15.out | cut -c1-200
sh $SP/tstep.sh "13b B the probes run to FAIL (readback_probes.py — 35/42 expected: Q21, Q30, Q32, Q39 until the tape; Q40-Q42 until the runner)" bash -c "python3 World/step9/readback_probes.py > $SP/ch15b_probes_fail.out 2>&1"
echo "probes rc $? (1 expected)"; /usr/bin/grep "readback_probes:\|FAIL\|RAISED" $SP/ch15b_probes_fail.out | cut -c1-260
sh $SP/tstep.sh "13b B the types (add_types_ch15.py — five kinds, twelve effects, four rows amended, the daemon and the functions block, the span and twenty-one edges, I5 75, two clock parameters, the register untouched)" bash -c "set -o pipefail; python3 $SP/add_types_ch15.py > $SP/add_types_ch15.out 2>&1" || { tail -6 $SP/add_types_ch15.out; exit 1; }
cat $SP/add_types_ch15.out | cut -c1-300
echo CHAIN_DONE

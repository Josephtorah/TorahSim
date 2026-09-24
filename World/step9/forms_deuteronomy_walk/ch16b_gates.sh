#!/bin/sh
# THE DEUTERONOMY WALK 14b (LEAN): THE GATES CHAIN ONCE — gates_chain.sh in the background (the tape, the eleven probe suites, the daemon gate, the dependency gate,
# the build, the journal gate, the register gate --strict, the positions at FOUR workers (the lean pass's POSARGS), the checkpoint probes, the stamp, the sweep, the
# unmoved check); the SUMMARY read once when the job ends; every step timed by the chain's own summary, the whole by this row. RUN FROM THE REPO ROOT.
SP="$(cd "$(dirname "$0")" && pwd)"
cd "$(git rev-parse --show-toplevel)" || exit 2
export TIMING=$SP/ch16b_timing.tsv
sh $SP/tstep.sh "14b the gates chain, one pass (gates_chain.sh — the positions at four workers)" sh World/step9/gates_chain.sh $SP/ch16b_gates > $SP/ch16b_gates.log 2>&1
RC=$?
cp $SP/ch16b_gates/SUMMARY.txt $SP/ch16b_gates_SUMMARY.txt 2>/dev/null
echo "rc=$RC" > $SP/ch16b_gates.DONE

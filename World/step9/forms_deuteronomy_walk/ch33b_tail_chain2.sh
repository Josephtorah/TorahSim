#!/bin/sh
# THE DEUTERONOMY WALK 21b (LEAN) — THE TAIL'S SECOND JOB: the chain's THIRD PASS --from checkpoint after the checkpoint probe's tape reader was widened (the second pass green
# through the positions, RED at K1 by the probe's own single-quote regex — no runner, registry or tape moved; the cache warm from the second pass's harvest): the checkpoint probes,
# the stamp, the sweep (2400 limit), the unmoved check; ONE DONE file; the summary read once. ch32b_tail_chain3.sh's form. RUN FROM THE REPO ROOT.
SP="$(cd "$(dirname "$0")" && pwd)"; cd "$(git rev-parse --show-toplevel)" || exit 2; export TIMING=$SP/ch33b_timing.tsv; rm -f $SP/ch33b_tail_chain2.DONE
sh $SP/tstep.sh "21b TAIL the gates chain, third pass, from the checkpoint probes after the probe's reader was widened (gates_chain.sh --from checkpoint — the stamp, the sweep, the unmoved check)" sh World/step9/gates_chain.sh $SP/ch33b_gates3 --from checkpoint > $SP/ch33b_gates3.log 2>&1; CRC=$?; cp $SP/ch33b_gates3/SUMMARY.txt $SP/ch33b_gates3_SUMMARY.txt 2>/dev/null
echo "chain rc=$CRC" > $SP/ch33b_tail_chain2.DONE

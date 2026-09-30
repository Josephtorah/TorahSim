#!/bin/sh
# THE DEUTERONOMY WALK 21b (LEAN) — THE TAIL'S ONE BACKGROUND JOB (20b's lesson 18): the import cache CLEARED WHOLE (the cache probe C6 red on the chain's first pass —
# the new runner harvested ALONE beside cached neighbours, its OH_CHAIN, GR_GRAVE and FE_SIX recorded as plain blobs instead of aliases of the covenant's and the song's
# names: 18b's lesson 11, the harvest's half of the rule; the bindings already assignments — 20b's lesson 19 built in), then THE CHAIN'S SECOND PASS FROM THE TAPE (20b's form: the tape's ONE process harvests the cold cache whole in the sequence's order BEFORE the probes' eleven
# suites, which the chain launches at once — a cold cache under concurrent suites is a RACE: a suite restoring what a faster sibling wrote, then harvesting the rest alone beside restored
# neighbours, the fault itself; the first launch --from probes was stopped at 47 s for this and the cache cleared again; then the daemon, dependency, build, journal and register gates,
# the positions at four workers, the checkpoint probes, the stamp, the sweep at its 2400 limit, the unmoved check); ONE DONE file; the summary read once. ch32b_tail_chain2.sh's form.
SP="$(cd "$(dirname "$0")" && pwd)"; cd "$(git rev-parse --show-toplevel)" || exit 2; export TIMING=$SP/ch33b_timing.tsv; rm -f $SP/ch33b_tail_chain.DONE
sh $SP/tstep.sh "21b TAIL the import cache cleared whole a second time before the chain's second pass (ink_cache.py --clear — the first clear's harvest raced under the eleven suites, stopped at 47 s)" sh -c "python3 World/step9/ink_cache.py --clear > $SP/ch33b_cache_clear.out 2>&1"
sh $SP/tstep.sh "21b TAIL the gates chain, second pass, from the tape after the cache cleared (gates_chain.sh — the tape harvests the cache whole, the positions at four workers)" sh World/step9/gates_chain.sh $SP/ch33b_gates2 > $SP/ch33b_gates2.log 2>&1; CRC=$?; cp $SP/ch33b_gates2/SUMMARY.txt $SP/ch33b_gates2_SUMMARY.txt 2>/dev/null
echo "chain rc=$CRC" > $SP/ch33b_tail_chain.DONE

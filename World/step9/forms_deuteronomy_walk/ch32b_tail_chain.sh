#!/bin/sh
# THE DEUTERONOMY WALK 20b (LEAN) — THE TAIL, after the readback probes were retyped from the chain's first print: (1) THE READBACK SUITE ALONE (19b's lesson 16 — after a retype
# by ast the probe suite runs before the chain; sequential, no second stepper beside it; the chain's own form `python3 World/step9/readback_probes.py` from the repo root), the job
# STOPPING HERE if it is not green; (2) THE IMPORT CACHE CLEARED WHOLE (18b's lesson 11 — three older runners edited at RUN B were re-harvested alone beside cached neighbours and
# C6 fell on the first pass: an alias through a subscript keeps its sharing group only in a whole harvest); (3) THE GATES CHAIN'S SECOND PASS FROM THE TAPE (a pass after any
# source change starts at the tape) — gates_chain.sh into ch32b_gates2 (the tape, the twelve probe suites, the daemon, dependency, build, journal and register --strict gates,
# the positions at FOUR workers, the checkpoint probes, the stamp, the sweep, the unmoved check); the SUMMARY read once when the job ends; every step timed; one DONE file with
# the rcs. ch29b_gates2.sh's and ch29b_gates3.sh's forms. RUN FROM THE REPO ROOT in the background (nohup).
SP="$(cd "$(dirname "$0")" && pwd)"
cd "$(git rev-parse --show-toplevel)" || exit 2
export TIMING=$SP/ch32b_timing.tsv
rm -f $SP/ch32b_tail_chain.DONE
sh $SP/tstep.sh "20b TAIL the readback suite alone after the retypes (readback_probes.py — the chain's own form, before the chain)" sh -c "python3 World/step9/readback_probes.py > $SP/ch32b_probes_after_retypes.out 2>&1"
PRC=$?
if [ $PRC = 0 ]; then
  sh $SP/tstep.sh "20b TAIL the import cache cleared whole before the chain's second pass (ink_cache.py --clear — 18b's lesson 11)" sh -c "python3 World/step9/ink_cache.py --clear > $SP/ch32b_cache_clear.out 2>&1"
  sh $SP/tstep.sh "20b TAIL the gates chain, second pass, from the tape after the retypes and the cache cleared (gates_chain.sh — the positions at four workers)" sh World/step9/gates_chain.sh $SP/ch32b_gates2 > $SP/ch32b_gates2.log 2>&1
  CRC=$?
  cp $SP/ch32b_gates2/SUMMARY.txt $SP/ch32b_gates2_SUMMARY.txt 2>/dev/null
else
  CRC=99
fi
{ echo "probes rc=$PRC"; echo "chain rc=$CRC"; } > $SP/ch32b_tail_chain.DONE

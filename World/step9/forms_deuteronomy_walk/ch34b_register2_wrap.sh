#!/bin/sh
# THE DEUTERONOMY WALK 22b: the register gate --strict ALONE a second time — AFTER THE STITCHER (the tape carrying chapter 34; the gate classes a receipt from the replayed tape — 22b's find): the receipt 34:9's class READ from this print, then retyped
SP="$(cd "$(dirname "$0")" && pwd)"
cd "$(git rev-parse --show-toplevel)" || exit 2
export TIMING=$SP/ch34b_timing.tsv
rm -f $SP/ch34b_register2.DONE
sh $SP/tstep.sh "22b the register gate --strict alone, second print (after the stitcher — the tape carrying chapter 34)" sh -c "python3 World/step9/register_census.py --strict > $SP/ch34b_register_second.out 2>&1"
echo "rc=$?" > $SP/ch34b_register2.DONE

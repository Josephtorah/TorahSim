#!/bin/sh
# THE DEUTERONOMY WALK 22b: the register gate --strict ALONE (the design's THE REGISTER — the receipt 34:9's class READ from this print before it is retyped), one DONE file
SP="$(cd "$(dirname "$0")" && pwd)"
cd "$(git rev-parse --show-toplevel)" || exit 2
export TIMING=$SP/ch34b_timing.tsv
rm -f $SP/ch34b_register.DONE
sh $SP/tstep.sh "22b the register gate --strict alone (the receipt 34:9's class read from the print)" sh -c "python3 World/step9/register_census.py --strict > $SP/ch34b_register_first.out 2>&1"
echo "rc=$?" > $SP/ch34b_register.DONE

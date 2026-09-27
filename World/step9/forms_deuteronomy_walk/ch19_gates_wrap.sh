#!/bin/sh
# THE CACHE LAW's wrapper: the chain in the background, timed, ONE DONE file at its end (never polled — the harness notifies).
SP="$(cd "$(dirname "$0")" && pwd)"
export TIMING=$SP/ch19_timing.tsv
cd "$(git rev-parse --show-toplevel)"
sh World/step9/forms_deuteronomy_walk/tstep.sh "16 the chain (ch19_gates.sh in the background — the seats, verify_text and the ritual for three units, the fold, build_world, the journal gate, the register gate --strict, large_letter, the home gate)" zsh $SP/ch19_gates.sh > $SP/ch19_gates.log 2>&1
echo "rc=$?" > $SP/ch19_gates.DONE

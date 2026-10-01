#!/bin/sh
# THE DEUTERONOMY WALK 22b: the tape wrap's SECOND HALF — after the reassembly, the second graded run (23/23), the registration and the register gate alone (GREEN; the seat 'NONE declared | []'):
# THE RECEIPT RE-DECLARED from the gate's print (the class as the gate holds it), the dependency and daemon gates ALONE, the tape's chain, the scan census; one DONE file. RUN FROM THE REPO ROOT.
SP="$(cd "$(dirname "$0")" && pwd)"
cd "$(git rev-parse --show-toplevel)" || exit 2
export TIMING=$SP/ch34b_timing.tsv
rm -f $SP/ch34_tape.DONE
sh $SP/tstep.sh "22b THE RECEIPT 34:9 RE-DECLARED from the gate's print (patch_register_ch34.py — the class as the gate holds it)" sh -c "python3 $SP/patch_register_ch34.py > $SP/ch34b_register_patch.out 2>&1" || { cat $SP/ch34b_register_patch.out | cut -c1-600; echo "register patch failed" > $SP/ch34_tape.DONE; exit 1; }
tail -1 $SP/ch34b_register_patch.out | cut -c1-200
sh $SP/tstep.sh "22b the dependency gate alone (the demands read before the chain)" sh -c "python3 World/step9/dependency_census.py > $SP/ch34b_dependency_first.out 2>&1"
echo "dependency rc $?"; tail -3 $SP/ch34b_dependency_first.out | cut -c1-300
sh $SP/tstep.sh "22b the daemon gate alone" sh -c "python3 World/step9/daemon_census.py > $SP/ch34b_daemon_first.out 2>&1"
echo "daemon rc $?"; tail -2 $SP/ch34b_daemon_first.out | cut -c1-300
sh $SP/ch34_tape_chain.sh
echo "tape chain rc $?"
sh $SP/tstep.sh "22b THE SCAN CENSUS extended (ch34_scan_census.py — the runners' hole scans, the probes' and the tape's substring scans replayed on the one database after the tape's first run)" sh -c "python3 $SP/ch34_scan_census.py > $SP/ch34_scan_census.out 2>&1"
echo "scan census rc $?"
echo "rc=0" > $SP/ch34_tape.DONE

#!/bin/sh
# THE DEUTERONOMY WALK 17b: after the first graded run — the runner reassembled under the guard's count READ FROM THE GENERATOR'S PRINT, the second graded run,
# the dependency and daemon gates ALONE (the demands read before the chain), then the tape's chain (the recorder, the stitcher, the literals DK1-DK5, the tape's first
# run, checkpoint_check --all) and THE SCAN CENSUS extended (14b's lesson 2 — before the second run); every step timed; one DONE file at the end. ch19_tape_wrap.sh's form
# (the part-1 rederive dropped — the twins and the scans typed at the second derive already). RUN FROM THE REPO ROOT.
SP="$(cd "$(dirname "$0")" && pwd)"
cd "$(git rev-parse --show-toplevel)" || exit 2
export TIMING=$SP/ch22b_timing.tsv
rm -f $SP/ch22_tape.DONE
N=$(/usr/bin/grep -o 'CASES generated: [0-9]*' $SP/ch22_cases_gen.out | /usr/bin/grep -o '[0-9]*$')
echo "the guard's count read from the generator's print: $N"
sh $SP/tstep.sh "17b B assemble (guard $N — the parts as they stand)" python3 $SP/ch22_assemble.py --guard $N "F1 F2 F3 F4 F5 F6 F7 F8 F9 F10 F11 F12 F13 F14 F15 F16 RB" || { echo "assemble failed" > $SP/ch22_tape.DONE; exit 1; }
sh $SP/tstep.sh "17b B the runner, second graded run (after the reassembly)" sh -c "python3 World/step9/cold_run_persons_poor_court.py > $SP/ch22_runner_run2.out 2>&1"
echo "runner rc $?"; /usr/bin/grep "^MATRIX\|^THE COMPILE\|Error\|Traceback" $SP/ch22_runner_run2.out | head -5
sh $SP/tstep.sh "17b the dependency gate alone (the demands read before the chain)" sh -c "python3 World/step9/dependency_census.py > $SP/ch22b_dependency_first.out 2>&1"
echo "dependency rc $?"; tail -3 $SP/ch22b_dependency_first.out | cut -c1-300
sh $SP/tstep.sh "17b the daemon gate alone" sh -c "python3 World/step9/daemon_census.py > $SP/ch22b_daemon_first.out 2>&1"
echo "daemon rc $?"; tail -2 $SP/ch22b_daemon_first.out | cut -c1-300
sh $SP/ch22_tape_chain.sh
echo "tape chain rc $?"
sh $SP/tstep.sh "17b THE SCAN CENSUS extended (ch22_scan_census.py — the runners' hole scans, the probes' and the tape's substring scans replayed on the one database after the tape's first run)" sh -c "python3 $SP/ch22_scan_census.py > $SP/ch22_scan_census.out 2>&1"
echo "scan census rc $?"
echo "rc=0" > $SP/ch22_tape.DONE

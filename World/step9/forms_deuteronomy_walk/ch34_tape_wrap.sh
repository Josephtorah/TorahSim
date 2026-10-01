#!/bin/sh
# THE DEUTERONOMY WALK 22b: after the first graded run — the runner reassembled under the guard's count READ FROM THE GENERATOR'S PRINT, the second graded run, THE REGISTRATION FIRST
# (the import line and the DAEMON_ORDER entry — the sequence file's import asserts the daemon order against the dispositions: the register gate, the probes and the stitcher's readers
# need it; 22b's find — the gate run alone BEFORE the registration fell at that assert), the register gate --strict ALONE (the receipt 34:9's class READ from its print) and the seat
# RE-DECLARED from the print, the dependency and daemon gates ALONE (the demands read before the chain), then the tape's chain (the recorder, the stitcher, the literals DP1-DP5, the tape's
# first run, checkpoint_check --all) and THE SCAN CENSUS extended (14b's lesson 2); every step timed; one DONE file at the end. ch33_tape_wrap.sh's form WITH THE REGISTRATION AND THE REGISTER
# GATE INSERTED. RUN FROM THE REPO ROOT.
SP="$(cd "$(dirname "$0")" && pwd)"
cd "$(git rev-parse --show-toplevel)" || exit 2
export TIMING=$SP/ch34b_timing.tsv
rm -f $SP/ch34_tape.DONE
N=$(/usr/bin/grep -o 'CASES generated: [0-9]*' $SP/ch34_cases_gen.out | /usr/bin/grep -o '[0-9]*$')
echo "the guard's count read from the generator's print: $N"
sh $SP/tstep.sh "22b B assemble (guard $N — the parts as they stand)" python3 $SP/ch34_assemble.py --guard $N "F1 F2 F3 F4 F5 F6 RB" || { echo "assemble failed" > $SP/ch34_tape.DONE; exit 1; }
sh $SP/tstep.sh "22b B the runner, second graded run (after the reassembly)" sh -c "python3 World/step9/cold_run_moses_death.py > $SP/ch34_runner_run2.out 2>&1"
echo "runner rc $?"; /usr/bin/grep "^MATRIX\|^THE COMPILE\|Error\|Traceback" $SP/ch34_runner_run2.out | head -5
sh $SP/tstep.sh "22b B the registration patched first (the import line + DAEMON_ORDER — the sequence file's import asserts the daemon order)" sh -c "PYTHONPATH=$SP python3 $SP/patch_seq_literals_ch34.py --registration > $SP/patch_seq_registration_ch34.out 2>&1" || { tail -3 $SP/patch_seq_registration_ch34.out; echo "registration patch failed" > $SP/ch34_tape.DONE; exit 1; }
tail -1 $SP/patch_seq_registration_ch34.out | cut -c1-200
sh $SP/tstep.sh "22b the register gate --strict alone (after the registration — the receipt 34:9's class read from the print)" sh -c "python3 World/step9/register_census.py --strict > $SP/ch34b_register_first.out 2>&1"
echo "register rc $?"; /usr/bin/grep "Deut 34:9\|STALE\|FAIL" $SP/ch34b_register_first.out | cut -c1-240 | head -6; tail -2 $SP/ch34b_register_first.out | cut -c1-300
sh $SP/tstep.sh "22b THE RECEIPT 34:9 RE-DECLARED from the gate's print (patch_register_ch34.py)" sh -c "python3 $SP/patch_register_ch34.py > $SP/ch34b_register_patch.out 2>&1" || { cat $SP/ch34b_register_patch.out | cut -c1-600; echo "register patch failed" > $SP/ch34_tape.DONE; exit 1; }
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

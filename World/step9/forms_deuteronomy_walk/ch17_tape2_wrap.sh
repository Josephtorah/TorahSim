#!/bin/sh
# THE DEUTERONOMY WALK 15b: after the first tape run's print — the daemon's diviners branch retyped as literal calls, two callees' scans widened, the four demands filed:
# A PASS AFTER ANY SOURCE CHANGE STARTS AT THE TAPE (13b's lesson) — the runner reassembled, its third graded run, the two gates alone, the tape's second run,
# checkpoint_check --all, the scan census again; one DONE file. RUN FROM THE REPO ROOT.
SP="$(cd "$(dirname "$0")" && pwd)"
cd "$(git rev-parse --show-toplevel)" || exit 2
export TIMING=$SP/ch17b_timing.tsv
rm -f $SP/ch17_tape2.DONE
sh $SP/tstep.sh "15b B assemble, second (guard 66 — the daemon's ten diviner writes as literal calls)" python3 $SP/ch17_assemble.py --guard 66 "F1 F2 F3 F4 F5 F6 F7 F8 RB" || { echo "assemble failed" > $SP/ch17_tape2.DONE; exit 1; }
sh $SP/tstep.sh "15b B the runner, third graded run (after the daemon's retype)" sh -c "python3 World/step9/cold_run_courts_prophet.py > $SP/ch17_runner_run3.out 2>&1"
echo "runner rc $?"; /usr/bin/grep "^MATRIX\|^THE COMPILE\|Error\|Traceback" $SP/ch17_runner_run3.out | head -5
sh $SP/tstep.sh "15b the daemon gate alone, after the retype" sh -c "python3 World/step9/daemon_census.py > $SP/ch17b_daemon_after.out 2>&1"
echo "daemon rc $?"; /usr/bin/grep "DAEMON GATE\|FAIL" $SP/ch17b_daemon_after.out | cut -c1-300 | head -5
sh $SP/tstep.sh "15b the dependency gate alone, after the filing" sh -c "python3 World/step9/dependency_census.py > $SP/ch17b_dependency_after.out 2>&1"
echo "dependency rc $?"; /usr/bin/grep "DEPENDENCY GATE\|FAIL" $SP/ch17b_dependency_after.out | cut -c1-300 | head -8
sh $SP/tstep.sh "15b B the tape, second run (after the scans widened and the daemon retyped — a pass after any source change starts at the tape)" sh -c "python3 World/step9/cold_run_sequence.py > $SP/ch17_tape_run2.out 2>&1"
echo "tape rc $?"
/usr/bin/grep "checkpoints$\|CHECKPOINT DI\|CHECKPOINT DE4\|CHECKPOINT DD4\|MISS \|Traceback\|Error" $SP/ch17_tape_run2.out | cut -c1-200 | head -16
sh $SP/tstep.sh "15b B checkpoint_check --all (after the second run)" sh -c "python3 World/step9/checkpoint_check.py --all > $SP/ch17_checkpoint_check2.out 2>&1"
tail -1 $SP/ch17_checkpoint_check2.out | cut -c1-200
sh $SP/tstep.sh "15b THE SCAN CENSUS, second (after the seats widened)" sh -c "python3 $SP/ch17_scan_census.py > $SP/ch17_scan_census2.out 2>&1"
/usr/bin/grep "^ TRIPS \|SCAN CENSUS DONE" $SP/ch17_scan_census2.out | cut -c1-200
echo "rc=0" > $SP/ch17_tape2.DONE

#!/bin/sh
# THE DEUTERONOMY WALK 19b: the second pass after the first tape run's reading — the runner reassembled under the guard's count (the facts' live calls, the readback's tape
# references and the daemon's values reworded), the third graded run, the tape's second run (the literals retyped from the first print), checkpoint_check --all; every step
# timed; one DONE file at the end. RUN FROM THE REPO ROOT (launched in the background — the cache law).
SP="$(cd "$(dirname "$0")" && pwd)"
cd "$(git rev-parse --show-toplevel)" || exit 2
export TIMING=$SP/ch29b_timing.tsv
rm -f $SP/ch29_second.DONE
N=$(/usr/bin/grep -o 'CASES generated: [0-9]*' $SP/ch29_cases_gen.out | /usr/bin/grep -o '[0-9]*$')
echo "the guard's count read from the generator's print: $N"
sh $SP/tstep.sh "19b B assemble (guard $N — the parts after the first tape run's reading)" python3 $SP/ch29_assemble.py --guard $N "F1 F2 F3 F4 F5 F6 F7 F8 F9 F10 F11 F12 F13 F14 F15 RB" || { echo "assemble failed" > $SP/ch29_second.DONE; exit 1; }
sh $SP/tstep.sh "19b B the runner, third graded run (the live calls, the tape references, the values reworded)" sh -c "python3 World/step9/cold_run_covenant_return_charge.py > $SP/ch29_runner_run3.out 2>&1"
echo "runner rc $?"; /usr/bin/grep "^MATRIX\|^THE COMPILE\|Error\|Traceback" $SP/ch29_runner_run3.out | head -5
sh $SP/tstep.sh "19b the dependency gate alone, after the demands (the second print)" sh -c "python3 World/step9/dependency_census.py > $SP/ch29b_dependency_after.out 2>&1"
echo "dependency rc $?"; tail -2 $SP/ch29b_dependency_after.out | cut -c1-300
sh $SP/tstep.sh "19b B the tape, second run (the literals retyped from the first print)" sh -c "python3 World/step9/cold_run_sequence.py > $SP/ch29_tape_run2.out 2>&1"
echo "tape rc $?"
/usr/bin/grep "checkpoints$\|CHECKPOINT DM\|DIVERGE\|Traceback\|Error" $SP/ch29_tape_run2.out | /usr/bin/grep -v "OPEN" | cut -c1-200 | head -30
sh $SP/tstep.sh "19b B checkpoint_check --all (after the tape's second run)" sh -c "python3 World/step9/checkpoint_check.py --all > $SP/ch29_checkpoint_check2.out 2>&1"
tail -1 $SP/ch29_checkpoint_check2.out | cut -c1-200
echo "rc=0" > $SP/ch29_second.DONE

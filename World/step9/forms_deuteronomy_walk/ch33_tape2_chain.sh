#!/bin/sh
# THE DEUTERONOMY WALK 21b: after the retypes — the runner reassembled (part 5's tape verse), the third graded run, the tape's second run, checkpoint_check --all; one DONE file (the cache law)
SP="$(cd "$(dirname "$0")" && pwd)"
cd "$(git rev-parse --show-toplevel)" || exit 2
export TIMING=$SP/ch33b_timing.tsv
rm -f $SP/ch33_tape2.DONE
N=$(/usr/bin/grep -o 'CASES generated: [0-9]*' $SP/ch33_cases_gen.out | /usr/bin/grep -o '[0-9]*$')
sh $SP/tstep.sh "21b B assemble (guard $N — part 5's tape verse retyped)" python3 $SP/ch33_assemble.py --guard $N "F1 F2 F3 F4 F5 F6 F7 F8 F9 F10 F11 RB" || { echo "assemble failed" > $SP/ch33_tape2.DONE; exit 1; }
sh $SP/tstep.sh "21b B the runner, third graded run (after the tape verse's retype)" sh -c "python3 World/step9/cold_run_blessing_of_moses.py > $SP/ch33_runner_run3.out 2>&1"
echo "runner rc $?"; /usr/bin/grep "^MATRIX\|^THE COMPILE\|Error\|Traceback" $SP/ch33_runner_run3.out | head -5
sh $SP/tstep.sh "21b B the tape, second run (the literals retyped from the first print)" sh -c "python3 World/step9/cold_run_sequence.py > $SP/ch33_tape_run2.out 2>&1"
echo "tape rc $?"; /usr/bin/grep "checkpoints$\|CHECKPOINT DO" $SP/ch33_tape_run2.out | cut -c1-160 | tail -8
sh $SP/tstep.sh "21b B checkpoint_check --all (after the tape's second run)" sh -c "python3 World/step9/checkpoint_check.py --all > $SP/ch33_checkpoint_check2.out 2>&1"
tail -1 $SP/ch33_checkpoint_check2.out | cut -c1-200
echo "rc=0" > $SP/ch33_tape2.DONE

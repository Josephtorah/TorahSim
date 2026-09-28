#!/bin/sh
# THE DEUTERONOMY WALK 18b RUN B — the second chain in ONE background job (the cache law) after the retypes: the runner's fourth graded run (the 28:64 row's tape seat 4:25)
# -> the tape's second run -> checkpoint_check --all; the dependency gate's second print (after the literals wrote the import) read into the summary. DONE file + SUMMARY.
SP="$(cd "$(dirname "$0")" && pwd)"
cd "$(git rev-parse --show-toplevel)" || exit 2
export TIMING=$SP/ch26b_timing.tsv
S=$SP/ch26b_fourth_chain_SUMMARY.txt; : > $S
echo "DEPENDENCY (after2, the import on the tape): $(tail -1 $SP/ch26b_dependency_after2.out | cut -c1-200)" >> $S
sh $SP/tstep.sh "18b B the runner, sixth graded run (the kin count retyped)" sh -c "python3 World/step9/cold_run_firstfruits_ebal_curses.py > $SP/ch26_runner_run6.out 2>&1"
echo "RUNNER rc $?: $(/usr/bin/grep 'MATRIX: 88\|THE NARRATIVE.*(96,' $SP/ch26_runner_run6.out | cut -c1-120 | tr '\n' ' ')" >> $S
sh $SP/tstep.sh "18b B the tape, fourth run" sh -c "python3 World/step9/cold_run_sequence.py > $SP/ch26_tape_run4.out 2>&1"
echo "TAPE rc $?" >> $S
sh $SP/tstep.sh "18b B checkpoint_check --all (after the fourth run)" sh -c "python3 World/step9/checkpoint_check.py --all > $SP/ch26_checkpoint_check4.out 2>&1"
python3 $SP/ch26_tape_verdict.py $SP/ch26_tape_run4.out $SP/ch26_checkpoint_check4.out >> $S 2>&1
touch $SP/ch26b_fourth_chain.DONE

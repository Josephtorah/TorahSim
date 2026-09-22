#!/bin/sh
# THE DEUTERONOMY WALK 12b: the runner's chain — assemble (CASES empty) -> the cases generated from the cells' own asks -> assemble with the guard's count
# read from the generator's print -> the first graded run; every step timed. 11b's form (ch13_runner_chain.sh). RUN FROM THE REPO ROOT (launched in the background — the cache law).
SP="$(cd "$(dirname "$0")" && pwd)"
cd "$(git rev-parse --show-toplevel)" || exit 2
export TIMING=$SP/ch14_timing.tsv
sh $SP/tstep.sh "12b B assemble (CASES empty)" python3 $SP/ch14_assemble.py --empty || exit 1
sh $SP/tstep.sh "12b B cases generated from the cells' asks" sh -c "python3 $SP/ch14_cases_gen.py > $SP/ch14_cases_gen.out 2>&1" || { tail -5 $SP/ch14_cases_gen.out; exit 1; }
tail -1 $SP/ch14_cases_gen.out
N=$(/usr/bin/grep -o 'CASES generated: [0-9]*' $SP/ch14_cases_gen.out | /usr/bin/grep -o '[0-9]*$')
echo "the guard's count read from the generator's print: $N"
sh $SP/tstep.sh "12b B assemble (guard $N)" python3 $SP/ch14_assemble.py --guard $N "F1 F2 F3 F4 F5 F6 F7 RB" || exit 1
sh $SP/tstep.sh "12b B the runner, first graded run" sh -c "python3 World/step9/cold_run_food_tithe.py > $SP/ch14_runner_run1.out 2>&1"
echo "runner rc $?"
/usr/bin/grep -c "^PASS" $SP/ch14_runner_run1.out; /usr/bin/grep -c "^MISS" $SP/ch14_runner_run1.out; /usr/bin/grep "^MATRIX\|^THE COMPILE\|Error\|Traceback" $SP/ch14_runner_run1.out | head -5

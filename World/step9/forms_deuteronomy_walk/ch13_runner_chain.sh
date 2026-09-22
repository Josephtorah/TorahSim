#!/bin/sh
# THE DEUTERONOMY WALK 11b: the runner's chain — assemble (CASES empty) -> the cases generated from the cells' own asks -> assemble with the guard's count
# read from the generator's print -> the first graded run; every step timed. 10b's form (ch12_runner_chain.sh). RUN FROM THE REPO ROOT (launched in the background — the cache law).
SP="$(cd "$(dirname "$0")" && pwd)"
cd "$(git rev-parse --show-toplevel)" || exit 2
export TIMING=$SP/ch13_timing.tsv
sh $SP/tstep.sh "11b B assemble (CASES empty)" python3 $SP/ch13_assemble.py --empty || exit 1
sh $SP/tstep.sh "11b B cases generated from the cells' asks" sh -c "python3 $SP/ch13_cases_gen.py > $SP/ch13_cases_gen.out 2>&1" || { tail -5 $SP/ch13_cases_gen.out; exit 1; }
tail -1 $SP/ch13_cases_gen.out
N=$(/usr/bin/grep -o 'CASES generated: [0-9]*' $SP/ch13_cases_gen.out | /usr/bin/grep -o '[0-9]*$')
echo "the guard's count read from the generator's print: $N"
sh $SP/tstep.sh "11b B assemble (guard $N)" python3 $SP/ch13_assemble.py --guard $N "F1 F2 F3 F4 F5 F6 RB" || exit 1
sh $SP/tstep.sh "11b B the runner, first graded run" sh -c "python3 World/step9/cold_run_seducers.py > $SP/ch13_runner_run1.out 2>&1"
echo "runner rc $?"
/usr/bin/grep -c "^PASS" $SP/ch13_runner_run1.out; /usr/bin/grep -c "^MISS" $SP/ch13_runner_run1.out; /usr/bin/grep "^MATRIX\|^THE COMPILE\|Error\|Traceback" $SP/ch13_runner_run1.out | head -5

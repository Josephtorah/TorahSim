#!/bin/sh
# THE DEUTERONOMY WALK 16b: the runner's chain — assemble (CASES empty) -> the cases generated from the cells' own asks -> assemble with the guard's count
# read from the generator's print -> the first graded run; every step timed. 15b's form (ch17_runner_chain.sh). RUN FROM THE REPO ROOT (launched in the background — the cache law).
SP="$(cd "$(dirname "$0")" && pwd)"
cd "$(git rev-parse --show-toplevel)" || exit 2
export TIMING=$SP/ch19b_timing.tsv   # 16b: the compile sitting's own table (12b's form named the reading's)
sh $SP/tstep.sh "16b B assemble (CASES empty)" python3 $SP/ch19_assemble.py --empty || exit 1
sh $SP/tstep.sh "16b B cases generated from the cells' asks" sh -c "python3 $SP/ch19_cases_gen.py > $SP/ch19_cases_gen.out 2>&1" || { tail -5 $SP/ch19_cases_gen.out; exit 1; }
tail -1 $SP/ch19_cases_gen.out
N=$(/usr/bin/grep -o 'CASES generated: [0-9]*' $SP/ch19_cases_gen.out | /usr/bin/grep -o '[0-9]*$')
echo "the guard's count read from the generator's print: $N"
sh $SP/tstep.sh "16b B assemble (guard $N)" python3 $SP/ch19_assemble.py --guard $N "F1 F2 F3 F4 F5 F6 F7 F8 F9 RB" || exit 1
sh $SP/tstep.sh "16b B the runner, first graded run" sh -c "python3 World/step9/cold_run_refuge_war_family.py > $SP/ch19_runner_run1.out 2>&1"
echo "runner rc $?"
/usr/bin/grep -c "^PASS" $SP/ch19_runner_run1.out; /usr/bin/grep -c "^MISS" $SP/ch19_runner_run1.out; /usr/bin/grep "^MATRIX\|^THE COMPILE\|Error\|Traceback" $SP/ch19_runner_run1.out | head -5

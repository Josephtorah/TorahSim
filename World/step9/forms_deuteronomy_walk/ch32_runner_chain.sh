#!/bin/sh
# THE DEUTERONOMY WALK 20b: the runner's chain — assemble (CASES empty) -> the cases generated from the cells' own asks -> assemble with the guard's count
# read from the generator's print -> the first graded run; every step timed. 19b's form (ch29_runner_chain.sh). RUN FROM THE REPO ROOT (launched in the background — the cache law).
SP="$(cd "$(dirname "$0")" && pwd)"
cd "$(git rev-parse --show-toplevel)" || exit 2
export TIMING=$SP/ch32b_timing.tsv   # 20b: the compile sitting's own table (12b's form named the reading's)
sh $SP/tstep.sh "20b B assemble (CASES empty)" python3 $SP/ch32_assemble.py --empty || exit 1
sh $SP/tstep.sh "20b B cases generated from the cells' asks" sh -c "python3 $SP/ch32_cases_gen.py > $SP/ch32_cases_gen.out 2>&1" || { tail -5 $SP/ch32_cases_gen.out; exit 1; }
tail -1 $SP/ch32_cases_gen.out
N=$(/usr/bin/grep -o 'CASES generated: [0-9]*' $SP/ch32_cases_gen.out | /usr/bin/grep -o '[0-9]*$')
echo "the guard's count read from the generator's print: $N"
sh $SP/tstep.sh "20b B assemble (guard $N)" python3 $SP/ch32_assemble.py --guard $N "F1 F2 F3 F4 F5 F6 F7 F8 F9 F10 F11 F12 F13 F14 F15 F16 RB" || exit 1
sh $SP/tstep.sh "20b B the runner, first graded run" sh -c "python3 World/step9/cold_run_song_charge_nebo.py > $SP/ch32_runner_run1.out 2>&1"
echo "runner rc $?"
/usr/bin/grep -c "^PASS" $SP/ch32_runner_run1.out; /usr/bin/grep -c "^MISS" $SP/ch32_runner_run1.out; /usr/bin/grep "^MATRIX\|^THE COMPILE\|Error\|Traceback" $SP/ch32_runner_run1.out | head -5

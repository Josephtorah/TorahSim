#!/bin/sh
# THE DEUTERONOMY WALK 15b: the tape's third run after DE4's retype and the registration edge — a pass after any source change starts at the tape; checkpoint_check;
# the dependency gate alone; one DONE file. RUN FROM THE REPO ROOT.
SP="$(cd "$(dirname "$0")" && pwd)"
cd "$(git rev-parse --show-toplevel)" || exit 2
export TIMING=$SP/ch17b_timing.tsv
rm -f $SP/ch17_tape3.DONE
sh $SP/tstep.sh "15b B the tape, third run (after DE4's retype — a pass after any source change starts at the tape)" sh -c "python3 World/step9/cold_run_sequence.py > $SP/ch17_tape_run3.out 2>&1"
echo "tape rc $?"; /usr/bin/grep "checkpoints$\|^MISS\|^OK   THE REST\|MISSES REMAIN\|Traceback" $SP/ch17_tape_run3.out | cut -c1-200
sh $SP/tstep.sh "15b B checkpoint_check --all (after the third run)" sh -c "python3 World/step9/checkpoint_check.py --all > $SP/ch17_checkpoint_check3.out 2>&1"
tail -1 $SP/ch17_checkpoint_check3.out | cut -c1-200
sh $SP/tstep.sh "15b the dependency gate alone, after the registration edge" sh -c "python3 World/step9/dependency_census.py > $SP/ch17b_dependency_after2.out 2>&1"
echo "dependency rc $?"; /usr/bin/grep "DEPENDENCY GATE:\|FAIL" $SP/ch17b_dependency_after2.out | cut -c1-200 | head -5
echo "rc=0" > $SP/ch17_tape3.DONE

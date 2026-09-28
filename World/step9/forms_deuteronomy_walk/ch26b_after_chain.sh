#!/bin/sh
# THE DEUTERONOMY WALK 18b RUN B — the after-chain in ONE background job (the cache law): the dependency gate alone after the filing -> the runner's third graded run
# (the source changed: the two live edges by attribute) -> the literals patched (subjects 274 as read) -> the tape's first run -> checkpoint_check --all -> THE SCAN
# CENSUS after the tape. The recorder and the stitcher NOT rerun (the tape holds the 21 lines already; the submits unchanged). DONE file + SUMMARY. RUN FROM THE REPO ROOT.
SP="$(cd "$(dirname "$0")" && pwd)"
cd "$(git rev-parse --show-toplevel)" || exit 2
export TIMING=$SP/ch26b_timing.tsv
S=$SP/ch26b_after_chain_SUMMARY.txt; : > $S
sh $SP/tstep.sh "18b B the dependency gate alone (after the filing)" sh -c "python3 World/step9/dependency_census.py > $SP/ch26b_dependency_after.out 2>&1"
echo "DEPENDENCY: $(tail -1 $SP/ch26b_dependency_after.out | cut -c1-200)" >> $S; /usr/bin/grep "FAIL" $SP/ch26b_dependency_after.out | head -12 | cut -c1-220 >> $S
sh $SP/tstep.sh "18b B the runner, third graded run (the two live edges by attribute)" sh -c "python3 World/step9/cold_run_firstfruits_ebal_curses.py > $SP/ch26_runner_run3.out 2>&1"
echo "RUNNER rc $?: $(/usr/bin/grep 'MATRIX\|THE NARRATIVE' $SP/ch26_runner_run3.out | cut -c1-160 | tr '\n' ' ')" >> $S
sh $SP/tstep.sh "18b B the literals patched (DL1-DL5; subjects 274 as read)" sh -c "python3 $SP/patch_seq_literals_ch26.py > $SP/patch_seq_literals_ch26.out 2>&1" || { echo "LITERALS FAILED: $(tail -3 $SP/patch_seq_literals_ch26.out | cut -c1-300)" >> $S; touch $SP/ch26b_after_chain.DONE; exit 1; }
echo "LITERALS: $(tail -1 $SP/patch_seq_literals_ch26.out | cut -c1-200)" >> $S
sh $SP/tstep.sh "18b B the tape, first run" sh -c "python3 World/step9/cold_run_sequence.py > $SP/ch26_tape_run1.out 2>&1"
echo "TAPE rc $?" >> $S; /usr/bin/grep "checkpoints\|CHECKPOINT DL\|MISS\|DIVERGE\|Traceback\|Error" $SP/ch26_tape_run1.out | cut -c1-240 | head -30 >> $S
sh $SP/tstep.sh "18b B checkpoint_check --all (after the tape)" sh -c "python3 World/step9/checkpoint_check.py --all > $SP/ch26_checkpoint_check.out 2>&1"
echo "CHECKPOINT_CHECK: $(tail -1 $SP/ch26_checkpoint_check.out | cut -c1-200)" >> $S
sh $SP/tstep.sh "18b B THE SCAN CENSUS (after the tape's first run)" sh -c "PYTHONPATH=$SP python3 $SP/ch26_scan_census.py > $SP/ch26_scan_census.out 2>&1"
echo "SCAN CENSUS rc $?: $(tail -2 $SP/ch26_scan_census.out | cut -c1-300 | tr '\n' ' ')" >> $S
touch $SP/ch26b_after_chain.DONE

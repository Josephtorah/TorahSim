#!/bin/sh
# THE DEUTERONOMY WALK 15b: after the first graded run — part 1 rederived with the twins typed, the runner reassembled under the guard's count, the second graded run,
# the dependency and daemon gates ALONE (the demands read before the chain), then the tape's chain (the recorder, the stitcher, the literals DI1-DI5, the tape's first
# run, checkpoint_check --all) and THE SCAN CENSUS extended (14b's lesson 2 — before the second run); every step timed; one DONE file at the end. RUN FROM THE REPO ROOT.
SP="$(cd "$(dirname "$0")" && pwd)"
cd "$(git rev-parse --show-toplevel)" || exit 2
export TIMING=$SP/ch17b_timing.tsv
rm -f $SP/ch17_tape.DONE
N_DROP=0 TWIN_EXPECTED="{'17:1 vs 15:21': 6, '17:4 vs 13:15': 9, '17:6 vs 19:15': 6, '17:7 vs 13:10': 7, '17:8 vs 1:17': 2, '17:11 vs 17:20': 1, '17:13 vs 13:12': 3, '17:17 vs 8:13': 3, '17:20 vs 8:14': 0, '18:2 vs 10:9': 8, '18:2 vs Num 18:20': 2, '18:5 vs 10:8': 3, '18:10 vs Lev 20:2': 0, '18:11 vs Lev 20:27': 1, '18:13 vs Gen 17:1': 1, '18:16 vs 5:25': 5, '18:17 vs 5:28': 5, '18:19 vs 13:4': 3, '18:22 vs 13:2': 0}" sh $SP/tstep.sh "15b derive the runner's part 1, third (the twins' assert typed from the print — the chain's derive had none)" python3 $SP/derive_ch17_part1.py || { echo "derive failed" > $SP/ch17_tape.DONE; exit 1; }
sh $SP/tstep.sh "15b B assemble (guard 66 — the parts as they stand: the twins' assert, the supplied-rows wording)" python3 $SP/ch17_assemble.py --guard 66 "F1 F2 F3 F4 F5 F6 F7 F8 RB" || { echo "assemble failed" > $SP/ch17_tape.DONE; exit 1; }
sh $SP/tstep.sh "15b B the runner, second graded run (after the reassembly)" sh -c "python3 World/step9/cold_run_courts_prophet.py > $SP/ch17_runner_run2.out 2>&1"
echo "runner rc $?"; /usr/bin/grep "^MATRIX\|^THE COMPILE\|Error\|Traceback" $SP/ch17_runner_run2.out | head -5
sh $SP/tstep.sh "15b the dependency gate alone (the demands read before the chain)" sh -c "python3 World/step9/dependency_census.py > $SP/ch17b_dependency_first.out 2>&1"
echo "dependency rc $?"; tail -3 $SP/ch17b_dependency_first.out | cut -c1-300
sh $SP/tstep.sh "15b the daemon gate alone" sh -c "python3 World/step9/daemon_census.py > $SP/ch17b_daemon_first.out 2>&1"
echo "daemon rc $?"; tail -2 $SP/ch17b_daemon_first.out | cut -c1-300
sh $SP/ch17_tape_chain.sh
echo "tape chain rc $?"
sh $SP/tstep.sh "15b THE SCAN CENSUS extended (ch17_scan_census.py — the runners' hole scans, the probes' and the tape's substring scans replayed on the one database after the tape's first run)" sh -c "python3 $SP/ch17_scan_census.py > $SP/ch17_scan_census.out 2>&1"
echo "scan census rc $?"
echo "rc=0" > $SP/ch17_tape.DONE

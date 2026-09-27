#!/bin/sh
# THE DEUTERONOMY WALK 15b: the runner's build in one background job — part 1 rederived, the fast checker (parts 1-3), the ask check, then the runner's chain
# (assemble empty -> the cases generated -> assemble with the guard's count -> the first graded run); every step timed; stops at the first failure. RUN FROM THE REPO ROOT.
SP="$(cd "$(dirname "$0")" && pwd)"
cd "$(git rev-parse --show-toplevel)" || exit 2
export TIMING=$SP/ch17b_timing.tsv
sh $SP/tstep.sh "15b derive the runner's part 1 (the helpers from the chapter-16 runner, the ink blocks from ch17_ink.py, the scans, the callees' facts)" python3 $SP/derive_ch17_part1.py || exit 1
sh $SP/tstep.sh "15b the fast checker, parts 1-4 (ch17_fastcheck.py)" sh -c "python3 $SP/ch17_fastcheck.py > $SP/ch17_fastcheck_run1.out 2>&1"
tail -1 $SP/ch17_fastcheck_run1.out
/usr/bin/grep -q 'fails 0, part2 fails 0, part3 fails 0, part4 fails 0' $SP/ch17_fastcheck_run1.out || { /usr/bin/grep -A2 'ASSERT FAIL\|ERROR' $SP/ch17_fastcheck_run1.out | cut -c1-600 | head -30; exit 1; }
sh $SP/tstep.sh "15b every ask called (ch17_askcheck.py — the eight cells and the table with the DATA rows)" sh -c "python3 $SP/ch17_askcheck.py ch17_part2.py ch17_part3.py ch17_part4.py > $SP/ch17_askcheck_run1.out 2>&1"
tail -1 $SP/ch17_askcheck_run1.out
/usr/bin/grep -q ' 0 failed' $SP/ch17_askcheck_run1.out || { /usr/bin/grep 'ASK FAIL' $SP/ch17_askcheck_run1.out | cut -c1-400 | head -20; exit 1; }
sh $SP/ch17_runner_chain.sh

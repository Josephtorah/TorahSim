#!/bin/sh
SP="$(cd "$(dirname "$0")" && pwd)"
cd "$(git rev-parse --show-toplevel)" || exit 2
export TIMING=$SP/ch15b_timing.tsv
sh $SP/tstep.sh "13b B the fast checker, parts 1-4 (ch15_fastcheck.py — the readback's census, the DATA rows, the scene and the narrative against their predictions)" bash -c "python3 $SP/ch15_fastcheck.py > $SP/ch15_fastcheck_run2.out 2>&1"
echo "fastcheck rc $?"; /usr/bin/grep -n "ASSERT FAIL\|^ERROR\|Traceback\|fastcheck:" $SP/ch15_fastcheck_run2.out | cut -c1-900 | head -30
/usr/bin/grep -n "THE READBACK (the census\|THE VERSES NO ONE CITES\|THE DATA ROWS (printed\|THE SCENE (printed\|THE NARRATIVE (printed" $SP/ch15_fastcheck_run2.out | cut -c1-700
sh $SP/tstep.sh "13b B every ask called (ch15_askcheck.py — the cells F1-F7 and the table with the DATA rows)" bash -c "python3 $SP/ch15_askcheck.py ch15_part2.py ch15_part3.py ch15_part4.py > $SP/ch15_askcheck_run1.out 2>&1"
echo "askcheck rc $?"; /usr/bin/grep "ASK FAIL\|askcheck:" $SP/ch15_askcheck_run1.out | cut -c1-500
echo CHAIN_DONE

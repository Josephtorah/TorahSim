#!/bin/sh
# THE DEUTERONOMY WALK 21b: the runner's chain (assemble empty -> the cases generated -> assemble under the guard -> the first graded run) in the background with a DONE file
SP="$(cd "$(dirname "$0")" && pwd)"
cd "$(git rev-parse --show-toplevel)" || exit 2
rm -f $SP/ch33_runner.DONE
sh $SP/ch33_runner_chain.sh > $SP/ch33_runner_chain.out 2>&1
echo "rc=$?" > $SP/ch33_runner.DONE

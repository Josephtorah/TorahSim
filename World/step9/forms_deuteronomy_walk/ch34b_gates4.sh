#!/bin/sh
# THE DEUTERONOMY WALK 22b TAIL — THE FOURTH PASS of the gates chain, run FROM THE FORMS FOLDER after the owner's reboot (2026-10-01 10:38): the third pass was green
# through the register gate (the tape 10/10, the probes all full, the daemon, dependency, build, journal and register gates) and KILLED at the positions step for the reboot.
# The whole chain from the tape — the cache warm and every file unmoved since its last clear (08:23); if ANY runner, registry, probe or the sequence file is edited first:
# python3 World/step9/ink_cache.py --clear, then this. Its prints in ch34b_gates4/ beside this file, its SUMMARY copied to ch34b_gates4_SUMMARY.txt, its DONE file
# ch34b_gates4.DONE; its row in ch34b_timing.tsv (the writer write_ch34b_tail.py reads the FOURTH row named '22b the gates chain, one pass'). About three and a half hours.
# RUN FROM THE REPO ROOT: (nohup zsh World/step9/forms_deuteronomy_walk/ch34b_gates4.sh > World/step9/forms_deuteronomy_walk/ch34b_gates4_wrapper.log 2>&1 &)
# NEVER POLL: until [ -f World/step9/forms_deuteronomy_walk/ch34b_gates4.DONE ]; do sleep 60; done   (one background waiter), then the SUMMARY read ONCE.
SP="$(cd "$(dirname "$0")" && pwd)"
cd "$(git rev-parse --show-toplevel)" || exit 2
export TIMING=$SP/ch34b_timing.tsv
rm -f $SP/ch34b_gates4.DONE
sh $SP/tstep.sh "22b the gates chain, one pass (the FOURTH — from the tape after the reboot, in the new thread; the positions at four workers)" sh World/step9/gates_chain.sh $SP/ch34b_gates4 > $SP/ch34b_gates4.log 2>&1
RC=$?
cp $SP/ch34b_gates4/SUMMARY.txt $SP/ch34b_gates4_SUMMARY.txt 2>/dev/null
echo "rc=$RC" > $SP/ch34b_gates4.DONE

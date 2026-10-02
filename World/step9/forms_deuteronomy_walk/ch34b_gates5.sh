#!/bin/sh
# THE DEUTERONOMY WALK 22b TAIL — THE FIFTH PASS of the gates chain, --from checkpoint (2026-10-01, the new thread after the reboot): the fourth pass (ch34b_gates4.sh, from the tape)
# was GREEN THROUGH THE POSITIONS and RED at the checkpoint probes — K1 6/7: the probe's own beyond_the_tape() helper returned the tape's LAST verse at the Torah's end (Deut 34:10 —
# no next chapter, no next book) and run_to stopped at its LEFT EDGE, the sixth line unrun, DP1 diverged at index 319 (ch34b_gates4/checkpoint.out). The helper widened to the next
# verse of the last chapter (Deut 34:11; checkpoint_probes.py) — no runner, registry, probe suite or tape moved, the cache warm: 21b's precedent (ch33b_tail_chain2.sh), the chain
# resumed from the checkpoint probes — the checkpoint probes, the stamp, the sweep, the unmoved check. Its prints in ch34b_gates5/ beside this file, its SUMMARY copied to
# ch34b_gates5_SUMMARY.txt, its DONE file ch34b_gates5.DONE; its row in ch34b_timing.tsv (the FIFTH row named '22b the gates chain, one pass'). The fourth pass's prints kept whole
# in ch34b_gates4/ with its summary ch34b_gates_SUMMARY_pass4.txt. RUN FROM THE REPO ROOT: (nohup zsh World/step9/forms_deuteronomy_walk/ch34b_gates5.sh > World/step9/forms_deuteronomy_walk/ch34b_gates5_wrapper.log 2>&1 &)
SP="$(cd "$(dirname "$0")" && pwd)"
cd "$(git rev-parse --show-toplevel)" || exit 2
export TIMING=$SP/ch34b_timing.tsv
rm -f $SP/ch34b_gates5.DONE
sh $SP/tstep.sh "22b the gates chain, one pass (the FIFTH — from the checkpoint probes after the probe's beyond-the-tape helper was widened for the Torah's end; the stamp, the sweep, the unmoved check)" sh World/step9/gates_chain.sh $SP/ch34b_gates5 --from checkpoint > $SP/ch34b_gates5.log 2>&1
RC=$?
cp $SP/ch34b_gates5/SUMMARY.txt $SP/ch34b_gates5_SUMMARY.txt 2>/dev/null
echo "rc=$RC" > $SP/ch34b_gates5.DONE

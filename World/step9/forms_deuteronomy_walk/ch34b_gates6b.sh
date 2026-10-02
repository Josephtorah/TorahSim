#!/bin/sh
# THE DEUTERONOMY WALK 22b TAIL — THE SIXTH PASS RESUMED --from sweep (2026-10-01, on the owner's "ok lets give it a try" after his "just stop" at 18:35): the sixth pass (ch34b_gates6.sh,
# from the tape after the cache clear) was TEN STEPS GREEN — the tape, the probes, the five gates, the positions, the checkpoint probes, the stamp — and killed inside the sweep, its last
# long step. Nothing was edited since; the older runners' cases read for the counts moved by chapter 34's three reuses (none left but the literals already retyped). The chain's own
# --from option (19b's and 21b's form) runs the sweep and the unmoved check into the SAME folder ch34b_gates6/ (the stamp file the unmoved check reads is there); the chain truncates
# SUMMARY.txt, so the ten green lines are kept as ch34b_gates6_SUMMARY_killed.txt and the resumed summary copied to ch34b_gates6b_SUMMARY.txt; the DONE file ch34b_gates6b.DONE; its row
# in ch34b_timing.tsv. About thirty-five minutes. RUN FROM THE REPO ROOT: (nohup zsh World/step9/forms_deuteronomy_walk/ch34b_gates6b.sh > World/step9/forms_deuteronomy_walk/ch34b_gates6b_wrapper.log 2>&1 &)
SP="$(cd "$(dirname "$0")" && pwd)"
cd "$(git rev-parse --show-toplevel)" || exit 2
export TIMING=$SP/ch34b_timing.tsv
rm -f $SP/ch34b_gates6b.DONE
sh $SP/tstep.sh "22b the gates chain, one pass (the SIXTH RESUMED --from sweep on the owner's word after the kill, ten steps green standing; the sweep, the unmoved check)" sh World/step9/gates_chain.sh $SP/ch34b_gates6 --from sweep > $SP/ch34b_gates6b.log 2>&1
RC=$?
cp $SP/ch34b_gates6/SUMMARY.txt $SP/ch34b_gates6b_SUMMARY.txt 2>/dev/null
echo "rc=$RC" > $SP/ch34b_gates6b.DONE

#!/bin/sh
# THE DEUTERONOMY WALK 22b TAIL — THE SIXTH PASS of the gates chain, FROM THE TAPE after a cache clear (2026-10-01 ~15:05): the fifth pass (--from checkpoint) was GREEN at the
# checkpoint probes (7/7) and the stamp and RED at the sweep — the song's runner 71/72: its cell for Aaron's death as the receipt (32:48-50) reads the live kin count from the one database
# (gathered_to_his_people 6 since 34:5's reuse — Moses gathered) while its generated case froze 5; the sweep is the only gate that grades the older runners' cells (ch34b_gates5/sweep.out;
# the lone re-run ch34b_song_rerun.out). The expected count RETYPED FROM THE PRINT (cold_run_song_charge_nebo.py, 5 -> 6, a dated comment) — a runner moved, so the cache was cleared whole
# and the chain runs from the tape (the resume's step 3; a pass after a clear starts from the tape). Its prints in ch34b_gates6/ beside this file, its SUMMARY copied to ch34b_gates6_SUMMARY.txt,
# its DONE file ch34b_gates6.DONE; its row in ch34b_timing.tsv (the SIXTH row named '22b the gates chain, one pass'). About three and a half hours.
# RUN FROM THE REPO ROOT: (nohup zsh World/step9/forms_deuteronomy_walk/ch34b_gates6.sh > World/step9/forms_deuteronomy_walk/ch34b_gates6_wrapper.log 2>&1 &)
SP="$(cd "$(dirname "$0")" && pwd)"
cd "$(git rev-parse --show-toplevel)" || exit 2
export TIMING=$SP/ch34b_timing.tsv
rm -f $SP/ch34b_gates6.DONE
sh $SP/tstep.sh "22b the gates chain, one pass (the SIXTH — from the tape after the song's runner's expected count was retyped from the sweep's print and the cache cleared whole; the positions at four workers)" sh World/step9/gates_chain.sh $SP/ch34b_gates6 > $SP/ch34b_gates6.log 2>&1
RC=$?
cp $SP/ch34b_gates6/SUMMARY.txt $SP/ch34b_gates6_SUMMARY.txt 2>/dev/null
echo "rc=$RC" > $SP/ch34b_gates6.DONE

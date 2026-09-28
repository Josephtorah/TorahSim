#!/bin/sh
# THE DEUTERONOMY WALK 19b (LEAN) — THE TAIL: the chain's remaining steps after the session's memory watchdog killed the third launch at the positions step (four workers;
# three other sessions on the machine) — THE POSITIONS TABLE OUTSIDE THE CHAIN AT TWO WORKERS (13b's form: the step's own command), then gates_chain.sh --from checkpoint
# (the checkpoint probes, the stamp, the sweep, the unmoved check) into its own folder; the third launch's green rows to the register gate kept in ch29b_gates2_part1_SUMMARY.txt;
# one DONE file with both rcs. RUN FROM THE REPO ROOT in the background.
SP="$(cd "$(dirname "$0")" && pwd)"
cd "$(git rev-parse --show-toplevel)" || exit 2
export TIMING=$SP/ch29b_timing.tsv
rm -f $SP/ch29b_gates3.DONE
sh $SP/tstep.sh "19b TAIL the positions table outside the chain at two workers (checkpoint_positions.py --jobs 2 — the watchdog killed four)" sh -c "python3 World/step9/checkpoint_positions.py --jobs 2 > $SP/ch29b_gates3_positions.out 2>&1"
PRC=$?
if [ $PRC = 0 ]; then
  sh $SP/tstep.sh "19b TAIL the gates chain resumed --from checkpoint (the checkpoint probes, the stamp, the sweep, the unmoved check)" sh World/step9/gates_chain.sh $SP/ch29b_gates3 --from checkpoint > $SP/ch29b_gates3.log 2>&1
  CRC=$?
else
  CRC=99
fi
cp $SP/ch29b_gates3/SUMMARY.txt $SP/ch29b_gates3_SUMMARY.txt 2>/dev/null
{ echo "positions rc=$PRC"; echo "chain rc=$CRC"; } > $SP/ch29b_gates3.DONE

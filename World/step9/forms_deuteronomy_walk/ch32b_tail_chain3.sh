SP="$(cd "$(dirname "$0")" && pwd)"; cd "$(git rev-parse --show-toplevel)" || exit 2; export TIMING=$SP/ch32b_timing.tsv; rm -f $SP/ch32b_tail_chain3.DONE
sh $SP/tstep.sh "20b TAIL the gates chain, fourth pass, from the stamp after the sweep's limit was raised (gates_chain.sh --from stamp — the stamp, the sweep, the journal unmoved)" sh World/step9/gates_chain.sh $SP/ch32b_gates4 --from stamp > $SP/ch32b_gates4.log 2>&1; CRC=$?; cp $SP/ch32b_gates4/SUMMARY.txt $SP/ch32b_gates4_SUMMARY.txt 2>/dev/null
echo "chain rc=$CRC" > $SP/ch32b_tail_chain3.DONE

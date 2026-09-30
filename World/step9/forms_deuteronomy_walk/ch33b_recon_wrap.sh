#!/bin/sh
SP="$(cd "$(dirname "$0")" && pwd)"
cd "$(git -C "$SP" rev-parse --show-toplevel 2>/dev/null || echo /Users/Shared/TorahSim)"
S=$(date +%s); python3 $SP/ch33_compile_recon.py > $SP/ch33b_recon.out 2>&1; rc=$?; E=$(date +%s)
printf '%s\t%s\t%s\t%s\n' "$(date -r $S '+%H:%M:%S')" "21b THE RECON in the background (ch33_compile_recon.py — the tape, the registries, the dispositions, the probes, the running world)" "$((E-S))" "$rc" >> $SP/ch33b_timing.tsv
echo "rc=$rc" > $SP/ch33b_recon.DONE

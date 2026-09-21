#!/bin/sh
# usage: sh tstep.sh NAME command...   — times the command, appends a row to ch12_timing.tsv
NAME=$1; shift
TIMING=${TIMING:-<scratch>/ch12_timing.tsv}
S=$(date +%s)
"$@"
RC=$?
E=$(date +%s)
printf '%s\t%s\t%s\t%s\n' "$(date -r $S '+%H:%M:%S')" "$NAME" "$((E-S))" "$RC" >> "$TIMING"
exit $RC

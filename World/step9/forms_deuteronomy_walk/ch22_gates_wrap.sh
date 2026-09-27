#!/bin/zsh
# THE CACHE LAW's wrapper: the gates chain in the background with a DONE file; never polled — the harness notifies. Run from the repo root.
SP="$(cd "$(dirname "$0")" && pwd)"
rm -f $SP/ch22_gates.DONE
zsh $SP/ch22_gates.sh > $SP/ch22_gates.log 2>&1; echo "rc=$?" > $SP/ch22_gates.DONE

#!/bin/zsh
# THE CACHE LAW's wrapper: the gates chain in the background with a DONE file; never polled — the harness notifies. Run from the repo root. Sitting 19's form.
SP="$(cd "$(dirname "$0")" && pwd)"
rm -f $SP/ch32_gates.DONE
zsh $SP/ch32_gates.sh > $SP/ch32_gates.log 2>&1; echo "rc=$?" > $SP/ch32_gates.DONE

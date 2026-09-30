#!/bin/zsh
# THE CACHE LAW's wrapper: the gates chain in the background with a DONE file; never polled — the harness notifies. Run from the repo root. Sitting 20's form.
SP="$(cd "$(dirname "$0")" && pwd)"
rm -f $SP/ch33_gates.DONE
zsh $SP/ch33_gates.sh > $SP/ch33_gates.log 2>&1; echo "rc=$?" > $SP/ch33_gates.DONE

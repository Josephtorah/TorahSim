#!/bin/zsh
# THE CACHE LAW's wrapper: the gates chain in the background with a DONE file; never polled — the harness notifies. Run from the repo root. Sitting 21's form.
SP="$(cd "$(dirname "$0")" && pwd)"
rm -f $SP/ch34_gates.DONE
zsh $SP/ch34_gates.sh > $SP/ch34_gates.log 2>&1; echo "rc=$?" > $SP/ch34_gates.DONE

#!/bin/sh
SP="$(cd "$(dirname "$0")" && pwd)"
cd "$(git rev-parse --show-toplevel)" || exit 2
rm -f $SP/ch17_build.DONE
sh $SP/ch17_build_chain.sh > $SP/ch17_build_chain.log 2>&1
echo "rc=$?" > $SP/ch17_build.DONE

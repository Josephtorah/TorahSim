#!/usr/bin/env python3
"""THE FAST CHECKPOINT CHECK (2026-09-16; the owner's cost review after THE DEUTERONOMY WALK 2b — "lets do all 3"):
one run shows EVERY fault of a new checkpoint block at once, without a full tape run per fault.

  python3 World/step9/checkpoint_check.py CC            # the rows whose name starts with CC (one or more prefixes)
  python3 World/step9/checkpoint_check.py --all         # the whole block

The stepper walks the real tape to its end under its own session name (never the live session's — checkpoint_positions.py's form), then
checkpoints_partial (D28) runs the block one statement at a time: a statement that raises is REPORTED with its line and the run goes on, a row the
world cannot compute is NOT YET, a miss prints its declared and computed tuples. Exit 1 on any miss or raised statement. 2b's six tape runs
(one fault each, four minutes each) would have been one run of this.
"""
import os, sys, io, time, contextlib
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
SOURCE = 'checkpoint_check'                                # its own session name — never the live session's (the B7 lesson)

def main(argv):
    prefixes = [a for a in argv if not a.startswith('--')]
    if not prefixes and '--all' not in argv:
        raise SystemExit(__doc__)
    t0 = time.time()
    with contextlib.redirect_stdout(io.StringIO()):
        import cold_run_sequence as CS
        import world_stepper as WS
        reg = CS.registry_map()
        st = WS.Stepper(source=SOURCE)
        while not st.done:
            st.step('chapter')
        rows, failed = CS.checkpoints_partial(st.w, st.M, reg)
        st.close(quiet=True)
    t1 = time.time() - t0
    want = lambda r: '--all' in argv or any(r['name'].split(' ')[0].startswith(p) for p in prefixes)
    rows = [r for r in rows if want(r)]
    bad = 0
    for r in rows:
        pre = r['name'].split(' ')[0]
        if r['ok'] is True: print('  MATCH   %s' % pre)
        elif r['ok'] is None: print('  NOT YET %s' % pre)
        else:
            bad += 1; print('  MISS    %s' % r['name'][:160]); print('      declared: %r' % (r['declared'],)); print('      computed: %r' % (r['computed'],))
    for line, err in failed:
        bad += 1; print('  RAISED  line %d: %s' % (line, err))
    print('checkpoint_check: %d rows, %d miss, %d raised — the tape stepped to its end in %.0fs' % (len(rows), sum(1 for r in rows if r['ok'] is False), len(failed), t1))
    return 1 if bad else 0

if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))

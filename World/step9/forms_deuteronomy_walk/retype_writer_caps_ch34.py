#!/usr/bin/env python3
# THE DEUTERONOMY WALK 22b TAIL (2026-10-01): write_ch34b_tail.py's texts trimmed under the two caps after the fifth-pass retype — the recovery page 10,346 -> under 10,240,
# MEMORY.md 17,166 -> under 17,000 (another thread grew the index today: the public-era line) — and two stale 'THRICE' retyped to FIVE TIMES (the index line, the debt line).
# Every replacement asserted ONCE. RUN FROM THE REPO ROOT: python3 World/step9/forms_deuteronomy_walk/retype_writer_caps_ch34.py
import os, subprocess
SP = os.path.dirname(os.path.abspath(__file__)); W = f'{SP}/write_ch34b_tail.py'
s = open(W, encoding='utf-8').read(); n0 = len(s)
R = [
 ("%(TAPE3)s at the fourth pass, the fifth from the checkpoint %(V3)s; MARKERS 173", "%(TAPE3)s; the fifth pass %(V3)s; MARKERS 173"),
 ("the chain FOUR TIMES (the song's scan list; chapter 32's heaven count 10 -> 11 by the reuse; the third killed for a reboot; the fourth red at K1 — the probe's helper at the Torah's end, widened; the fifth from the checkpoint %(V3)s). NEXT: the commit of the tail on his word; then HIS WORD on what follows — nothing opens unasked.",
  "the chain FIVE TIMES (the scan list; the heaven count 10 -> 11; the third killed for a reboot; the fourth red at K1 — the probe's helper at the Torah's end; the fifth from the checkpoint %(V3)s). NEXT: the commit of the tail on his word; then his word on what follows."),
 ("(22b's RUN B, pushed mid-tail); THE TAIL's records UNCOMMITTED.", "(22b's RUN B, mid-tail); the tail's records UNCOMMITTED."),
 ("the full process OWED (COMPILE_DEBT's box (1)-(17)).\\n\"", "the full process OWED (COMPILE_DEBT's box 1-17).\\n\""),
 ("the chain THRICE — pass 1 red at the song's runner's scan list (the database written by the checkpoint check before the chain), pass 2 red at chapter 32's heaven count (10 -> 11 by 34:4's reuse — a retype reads the whole tuple), pass 3 killed at the positions step for a reboot with seven steps green, pass 4 in the new thread red at K1 (the probe's beyond-the-tape helper at the Torah's end — widened to the next verse), pass 5 from the checkpoint %(V3)s;",
  "the chain FIVE TIMES — pass 1 red at the song's runner's scan list (the database written before the chain), pass 2 at chapter 32's heaven count (10 -> 11 by 34:4's reuse — a retype reads the whole tuple), pass 3 killed at the positions for a reboot, pass 4 red at K1 (the probe's beyond-the-tape helper at the Torah's end — widened), pass 5 from the checkpoint %(V3)s;"),
 ("RUN B PUSHED %(HEAD)s mid-tail on 'commit push then finish any unfinished work'; the long form in the file); DEUTERONOMY CLOSED", "RUN B PUSHED %(HEAD)s mid-tail on 'commit push'; the long form in the file); DEUTERONOMY CLOSED"),
 ("(the lean pass's full process for 16-34 OWED — COMPILE_DEBT's box; or the Prophets' tape) — nothing opens unasked\" % F)", "(the lean pass's full process for 16-34 OWED; or the Prophets' tape) — nothing opens unasked\" % F)"),
 ("the chain THREE PASSES — C6 red (every compile clears the cache before its chain), K1 red (the probe's tape reader widened), then ALL GREEN; the long form in the file), PUSHED ec23cf1; \"", "the chain THREE PASSES — C6 red, K1 red (the reader widened), then ALL GREEN; the long form in the file), PUSHED ec23cf1; \""),
 ("PUSHED ec23cf1 2026-09-30 (21 + 21b + 22 together, on 'commit push'); \")", "PUSHED ec23cf1 2026-09-30 (with 21 + 21b); \")"),
 ("at the chain's fourth pass; the chain THRICE — pass 1", "at the chain's fourth pass; the chain FIVE TIMES — pass 1"),
]
for i, (a, b) in enumerate(R):
    c = s.count(a); assert c == 1, (i, c, a[:90]); s = s.replace(a, b)
open(W, 'w', encoding='utf-8').write(s)
print('retyped %d replacements; %d -> %d bytes' % (len(R), n0, len(s)))
subprocess.run(['python3', '-m', 'py_compile', W], check=True); print('compiles')

import os as _os
_ROOT = _os.path.normpath(_os.path.join(_os.path.dirname(_os.path.abspath(__file__)), '..', '..', '..'))   # THE PORTABLE REPO (2026-09-15): the repo root from this file's own place
#!/usr/bin/env python3
# THE DEUTERONOMY WALK 22b TAIL — INTERRUPTED 2026-10-01 10:38 for the owner's reboot ("stop everything, write a resume prompt"): the MID-TAIL NOTE appended under #245 (the state doc),
# the recovery page's section 2 rewritten under its cap, MEMORY.md's walk line (the older clauses 20-22 shortened to their long forms in the file; the 22b clause's tail retyped to
# the interruption — its head kept for write_ch34b_tail.py's anchor), the walk memory's NOTE (its description kept for the same anchor). Every text built whole; the caps and the
# lints asserted. RUN FROM THE REPO ROOT.
import re, os, sys, subprocess
ROOT = _ROOT
MEM = os.path.expanduser('~/.claude/projects/-Users-Shared-TorahSim/memory')
SD = f'{ROOT}/logic/pre_logic_methods_2026-07-28/PROMPT_continue_solo_era_2026-08-06.md'; REC = f'{ROOT}/logic/pre_logic_methods_2026-07-28/RECOVERY_new_thread_2026-09-12.md'
MM = f'{MEM}/MEMORY.md'; MW = f'{MEM}/deuteronomy-walk.md'; WRITE = '--write' in sys.argv
def rd(f): return open(f, encoding='utf-8').read()
HEB = re.compile('[%s-%s]' % (chr(0x5d0), chr(0x5ea)))
_U = os.path.basename(os.path.expanduser('~'))   # the machine's username, read not spelled (the home-path gate)
RES = 'logic/pre_logic_methods_2026-07-28/RESUME_22b_tail_2026-10-01.md'; FF = 'World/step9/forms_deuteronomy_walk'
NOTE = (" — MID-TAIL NOTE (2026-10-01 10:38; the owner: \"stop everything, write a resume prompt. I am going to reboot the system and start a new thread. you will have no memory. be complete\"): "
 "THE STATE — the tail of 22b after RUN B's push d30a31a (2026-10-01 08:22, on \"commit push then finish any unfinished work\": RUN B, the post-push records and the forms, the message naming the chain's second pass red at one count). "
 "The chain's FIRST PASS fell at the song's runner's scan list (gathered_to_his_people + moses — the one database written by the tape wrap's checkpoint_check --all before the chain; the three runners' SCANS_EXPECTED retyped from the database's own print, the cache cleared whole); "
 "the SECOND PASS at chapter 32's 'ten heaven entries' — ELEVEN since 34:4's reuse of see_the_land_from_afar_not_go_there (a heaven write on moses): DN2's declared 10 -> 11 and its label, Q49's forty-two's last slot 1 -> 2 and heaven 10 -> 11, RETYPED from the two prints (retype_heaven_ch34.py — cold_run_sequence.py and readback_probes.py, UNCOMMITTED; the first retype had read the first differing slot, not the whole tuple), the cache cleared whole; "
 "THE THIRD PASS from the tape launched 08:23 and GREEN THROUGH SEVEN STEPS — the tape 10/10 (1542 s), the probes all full (1541 s; ink_cache 8/8), the daemon, dependency, build (61 s), journal (198 s) and register --strict (GREEN) gates — then KILLED at the positions step an hour and a quarter in (8057 s from the launch; the timing row rc 137; the positions table untouched, the one database untouched — the workers run in their own folders); its prints kept as %(FF)s/ch34b_gates3/ and its partial summary ch34b_gates_SUMMARY_pass3_partial.txt. "
 "EVERY FILE THE TAIL NEEDS IS IN THE FORMS FOLDER %(FF)s/ (the scratchpad dies with the reboot): write_ch34b_tail.py (the records writer, --check then --write — it reads every print from its own folder and the fourth pass's from ch34b_gates4/), ch34b_gates4.sh (the fourth pass's wrapper), retype_heaven_ch34.py, ch34b_timing.tsv (the timing table — its FOURTH row named '22b the gates chain, one pass' will be the fourth pass's), the three summaries, RUN B's prints, commit_msg_ch34b.txt (RUN B's, used) and commit_msg_ch34b_tail.txt (the tail's draft, rewritten by the writer). UNCOMMITTED in the tree: the two retyped files, the forms folder's additions, this NOTE, the recovery page, the RESUME file. "
 "THE RESUME (a new thread without memory; its rereads first — the recovery page, the map's newest section (the 22b design; its AS BUILT not yet written), MEMORY.md, this checkpoint — then %(RES)s WHOLE; NOTHING RUNS BEFORE THE OWNER'S WORD): "
 "(1) from the repo root `(nohup zsh %(FF)s/ch34b_gates4.sh > %(FF)s/ch34b_gates4_wrapper.log 2>&1 &)` — the whole chain from the tape (no cache clear needed: every file unmoved since the clear of 08:23; if ANY runner, registry, probe or the sequence file is edited first, `python3 World/step9/ink_cache.py --clear`, then the wrapper); about three and a half hours (the positions near two, the sweep half an hour); "
 "(2) NEVER POLL — one background `until [ -f %(FF)s/ch34b_gates4.DONE ]; do sleep 60; done`, or a monitor on the SUMMARY's lines in thirty-minute arms (the session's memory watchdog has killed a waiter before); "
 "(3) read %(FF)s/ch34b_gates4_SUMMARY.txt ONCE; a red step: read its .out in ch34b_gates4/, retype from the print (a miss is evidence), `python3 World/step9/ink_cache.py --clear`, relaunch the wrapper from the tape (its row label edited to 'the FIFTH'; the writer takes the LAST chain row); "
 "(4) `python3 %(FF)s/write_ch34b_tail.py --check`, then `--write` (asserts ALL GREEN, the two caps, the lints unmoved; writes the map's AS BUILT, this NOTE's sequel, the recovery page, MEMORY.md, the walk memory, COMPILE_DEBT's line (17), the message); "
 "(5) `python3 logic/solo_tools/scrub_home_paths.py --check` GREEN and the gloss lints at their baselines (the state doc 146, MEMORY.md 4, else 0); "
 "(6) THE COMMIT ONLY ON HIS WORD — 'commit push': `git add -A -- . ':!elijah_docket' ':!DISPOSABLE_scan/*.zip'`, `git commit -q -F %(FF)s/commit_msg_ch34b_tail.txt`, `GH=/opt/homebrew/bin/gh; $GH auth switch --user Josephtorah; git push origin main; $GH auth switch --user PeerloopLLC` — and DEUTERONOMY CLOSES; what follows the Torah is his to rule. POST-REBOOT REREADS: the recovery page, the map's newest section, MEMORY.md, this checkpoint, then the RESUME file." % dict(FF=FF, RES=RES))
sd = rd(SD); assert '\n#245 (' in sd and 'MID-TAIL NOTE (' not in sd and 'THE TAIL OF 22b (' not in sd; i245 = sd.index('\n#245 ('); assert sd.find('\n#2', i245 + 5) < 0
sd2 = sd.rstrip('\n') + NOTE + '\n'
rec = rd(REC); i, j = rec.index('## 2. WHERE IT STANDS'), rec.index('\n## 3. THE STANDING LAWS'); assert 0 < i < j
SEC2 = ("## 2. WHERE IT STANDS (2026-10-01 10:38; #245 + its MID-TAIL NOTE — sitting 22b's tail INTERRUPTED for a reboot, newest)\n"
        "- NUMBERS CLOSED. DEUTERONOMY 1:1-34:12 READ, FROZEN AND COMPILED — ON THE TAPE; 1-34 PUSHED through d30a31a (22b's RUN B, pushed mid-tail); the tail's files UNCOMMITTED.\n"
        "- units 251 / standing 2377. 79 runners, 84 daemons; 1286 kinds / 1481 effects.\n"
        "- THE TAPE at RUN (1456, …, 2091, 55, 319, …, 127); 10/10 at the third pass (killed at the positions); MARKERS 173 — (40, 12, 7) at 31:1.\n"
        "- ⚠ THE LEAN PASS (#208): 16-34 lean; the full process OWED.\n"
        "- 22b MID-TAIL: the runner 23/23, the receipt ACT, passes 1-2 red at one literal each (retyped), pass 3 KILLED at the positions. ⚠ THE RESUME: read %s WHOLE, then on his word the FOURTH PASS from the forms folder (ch34b_gates4.sh), the SUMMARY once, write_ch34b_tail.py --check/--write, the home gate; the commit on his word — DEUTERONOMY CLOSES.\n" % RES)
rec2 = rec[:i] + SEC2 + rec[j:]
mm = rd(MM); a = mm.index('20 (ch 32 READ, lean'); b = mm.index("22b (the compile of 34, lean — THE BOOK'S LAST) RUN A at #244"); e = mm.index('\n', b)
SHORT = ("20 (ch 32 READ, lean — THE SONG, the spine IN FORCE 306-341) DONE 2026-09-28 (312 sources, 16 claims; the long form in the file), PUSHED 7798bee; "
         "20b DONE 2026-09-28 at #236 (the compile — the 77th runner song_charge_nebo 72/72; the chain green on its fourth pass; THE CAP BROKEN in RUN B — a big-callee compile splits RUN B; the long form in the file), PUSHED 472d2a3; "
         "21 (ch 33 READ, lean — THE BLESSING, the spine 342-356) DONE 2026-09-29 at #240 (176 sources, 11 claims by THE SEAT RULE BY ROW; the fold 250/2371; the long form in the file), PUSHED ec23cf1; "
         "21b DONE 2026-09-29 at #242 (the compile — the 78th runner blessing_of_moses 42/42; NO MARKER; the chain THREE PASSES — C6 red (every compile clears the cache before its chain), K1 red (the probe's tape reader widened), then ALL GREEN; the long form in the file), PUSHED ec23cf1; "
         "22 (ch 34 READ, lean — THE DEATH OF MOSES; the spine's LAST piska 357, 44 rows whole in ONE run + the tail, 0 cut misses) DONE 2026-09-30 at #243 (59 sources, 6 claims; the fold 251/2377; the long form in the file), PUSHED ec23cf1 2026-09-30 (21 + 21b + 22 together, on 'commit push'); ")
INTERIM = ("22b (the compile of 34, lean — THE BOOK'S LAST) RUN A at #244, RUN B at #245 2026-09-30 (the 79th runner moses_death 23/23 — six lines, 12 new + 3 reuses, no marker; the receipt 34:9 ACT from the gate's second print), RUN B PUSHED d30a31a 2026-10-01 mid-tail on 'commit push then finish any unfinished work'; "
           "⚠ THE TAIL INTERRUPTED 2026-10-01 10:38 for the owner's reboot — the chain's pass 1 red at the song's runner's scan list, pass 2 at chapter 32's heaven count (10 -> 11 by 34:4's reuse), both retyped from the prints; pass 3 green through the register gate and KILLED at the positions step; "
           "NEXT (a new thread, no memory): READ %s WHOLE, then on his word the FOURTH PASS from the forms folder (ch34b_gates4.sh — about three and a half hours; never poll), the SUMMARY once, write_ch34b_tail.py --check then --write, the home gate; the commit on his word — DEUTERONOMY CLOSES" % RES)
mm2 = mm[:a] + SHORT + INTERIM + mm[e:]
mw = rd(MW); assert re.search(r'^description: "SITTING 22b RUN B AT ITS CLEAN POINT 2026-09-30', mw, re.M) and 'TAIL INTERRUPTED' not in mw
WNOTE = ("\n\nNOTE (22b TAIL INTERRUPTED, 2026-10-01 10:38 — the owner's reboot, \"stop everything, write a resume prompt\"): RUN B pushed d30a31a mid-tail (on \"commit push then finish any unfinished work\"); the chain's first pass red at the song's runner's scan list (the one database written by the tape wrap's checkpoint check before the chain — the three runners' lists retyped from its print), the second at chapter 32's heaven count (ten entries eleven by 34:4's reuse, a heaven write on moses — a retype reads the WHOLE tuple), both retyped from the prints; the third pass from the tape green through the register gate and killed at the positions step for the reboot (its prints kept as the forms folder's ch34b_gates3/); every file the tail needs in the forms folder (the scratchpad dies with a reboot); THE RESUME in the state doc's MID-TAIL NOTE under #245 and %s — the fourth pass (ch34b_gates4.sh), the summary once, the writer, his commit word; DEUTERONOMY CLOSES there.\n" % RES)
mw2 = mw.rstrip('\n') + WNOTE
for name, text in (('note', NOTE), ('recovery', SEC2), ('memory', SHORT + INTERIM), ('walk', WNOTE)):
    assert not HEB.search(text), name; assert _U not in text and os.path.expanduser('~') not in text, name   # the username read from the environment, never spelled
print('THE INTERRUPTION RECORDS %s: the NOTE %d bytes; the recovery page %d (cap 10240); MEMORY.md %d (was %d; cap 17000); the walk note %d' % ('WRITTEN' if WRITE else 'CHECKED', len(NOTE.encode()), len(rec2.encode()), len(mm2.encode()), len(mm.encode()), len(WNOTE.encode())))
assert len(rec2.encode()) <= 10240 and len(mm2.encode()) < 17000, (len(rec2.encode()), len(mm2.encode()))
if WRITE:
    open(SD, 'w', encoding='utf-8').write(sd2); open(REC, 'w', encoding='utf-8').write(rec2); open(MM, 'w', encoding='utf-8').write(mm2); open(MW, 'w', encoding='utf-8').write(mw2)
    LINT = {}
    for f_, base in ((SD, 146), (REC, 0), (MM, 4), (MW, 0)):
        out = subprocess.run(['python3', f'{ROOT}/logic/solo_tools/gloss_lint.py', f_], capture_output=True, text=True).stdout
        n = int(re.search(r'gloss_lint: (\d+) flag', out).group(1)); LINT[os.path.basename(f_)] = (n, base)
    assert all(n == b for n, b in LINT.values()), LINT
    print('WRITTEN; the lints', LINT)

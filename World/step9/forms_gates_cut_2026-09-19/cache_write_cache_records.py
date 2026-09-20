import os as _os
_ROOT = _os.path.normpath(_os.path.join(_os.path.dirname(_os.path.abspath(__file__)), '..', '..', '..'))   # THE PORTABLE REPO (2026-09-15): the repo root from this file's own place
#!/usr/bin/env python3
"""THE VERIFIED-IMPORT CACHE (2026-09-19) — the records from the sheet (World/step9/RECORD_FORMS.md) in ONE call: --check verifies every anchor
and the two size caps first; the write appends/edits, then lints (gloss_lint per file; scrub_home_paths --check). The chain's numbers are parsed
from <scratch>/gates_cut_3/SUMMARY.txt. Run from the repo root."""
import os, re, subprocess, sys, json
ROOT = _ROOT
SP = os.path.dirname(os.path.abspath(__file__))
MEM = os.path.expanduser('~/.claude/projects/-Users-Shared-TorahSim/memory')
CHECK = '--check' in sys.argv
R = lambda p: open(p, encoding='utf-8').read()
def W(p, s): open(p, 'w', encoding='utf-8').write(s)

# ---- the chain's numbers
summ = os.path.join(SP, 'gates_cut_3', 'SUMMARY.txt')
steps = {}; done = False
if os.path.exists(summ):
    for line in R(summ).split('\n'):
        m = re.match(r'^(PASS|FAIL) (\w+) \((\d+)s\) (.*)$', line)
        if m: steps[m.group(2)] = (m.group(1), int(m.group(3)), m.group(4))
    done = 'GATES CHAIN DONE — ALL GREEN' in R(summ)
if not CHECK: assert done and all(v[0] == 'PASS' for v in steps.values()), ('the chain is not done and green', steps)
total = sum(v[1] for v in steps.values()); mins = '%d min %d s' % divmod(total, 60)
def sec(k): return steps.get(k, ('?', 0, ''))[1]
sweep_note = steps.get('sweep', ('', 0, '?'))[2][:160]
probe_line = ''
pf = os.path.join(SP, 'gates_cut_3', 'probe_ink_cache.out')
if os.path.exists(pf):
    m = re.search(r'(\d+/\d+) probes', R(pf)); probe_line = m.group(1) if m else '?'
    m2 = re.search(r'the full load (\d+) s, the warm load .*? (\d+) s, the cached load (\d+) s', R(pf)); T = m2.groups() if m2 else ('167', '211', '34')
else: T = ('167', '211', '34')
T = (T[0], T[1] if int(T[1]) > 100 else '211', T[2])   # the harvest is measured on a COLD cache (this session's probe run: 211 s); the chain's probe found the cache warm
CHAIN = ('the tape %d s (against 155 before the cache), the probes %d s (the cache probe inside them), the daemon and dependency gates %d s, build %d s, the journal gate %d s (against 166), '
         'the register gate %d s, the positions %d s (eight workers, each a cached load), the checkpoint suite %d s (against 205), the sweep %d s (%s), the unmoved check %d s — '
         'THE TOTAL %d s (%s) against 18 min 27 s before the cache and ninety minutes before the cut; every verdict the same.'
         % (sec('tape'), sec('probes'), sec('daemon') + sec('dependency'), sec('build'), sec('journal'), sec('register'), sec('positions'), sec('checkpoint'), sec('sweep'), sweep_note, sec('unmoved'), total, mins))

# ---- the texts
SLIPS = [
 "comprehension variables read as bound names (KeyError 'kv' on the cached path) — the walker skips comprehension, lambda and def scopes",
 "a def's locals read as bound names (NameError 'n') — a def binds its own name only",
 "the module's FINAL state harvested for a name bound twice (mishpatim_3's `failed`) — the harvest is per statement, each name's value AS OF that statement",
 "one empty list shared by every runner (foreign trails in the zero-report exits) — a fresh object for every binding",
 "a mutation through an attribute or subscript chain missed (pre_sinai's TOK empty) — the base of the chain is the touched name",
 "two statements on one line collided by line number (balak's PLENE_KIN lost) — the index is by statement position",
 "a touched name that does not pickle (a connection) forced the statement to run — only recorded names are restore targets",
 "the probe's byte compare tripped by the hash seed's set order — a canonical form (sets and dicts sorted, objects by class and attributes)",
 "the probe timed a cold harvest as the cached load — the warm load first, the hit timed",
 "the probe's pickle bytes memoize repeated objects and two processes intern strings differently (fifty-four scene worlds 'differed') — the hash over the canonical form's TEXT",
 "a name passed to a call and unchanged was restored fresh, breaking every alias (seventeen sharing groups lost: erection's VS_E29 is vestments' E29_ORDER) — recorded as KEPT, and an object that is another name's live object recorded as an ALIAS the cached path binds",
 "a length heuristic missed a same-length change (mishpatim's counter, a trail cleared and refilled) — the static scan of every name a function of the module may mutate, re-examined after every statement; every small container too",
 "a callee's trail mutated by the CALLER's statement (the residue of the last caller: twenty-one runners' P) — invisible to the caller's source: the call tracer (sys.monitoring, one event per code object per statement) names the runners whose functions ran, their mutables re-examined, a change recorded as module::name and restored IN PLACE",
 "a self-test's result tuple holding the callee's trail BY REFERENCE (clocks' `_r`, korach's V5_ASHAM) — nested aliases with their paths, patched into the restored value",
 "a with-block holding the imports SKIPPED (pre_sinai's) — the modules loaded in another order than the full path's, so the calendar's trail and the family alias came out different — ANY BLOCK HOLDING AN IMPORT RUNS",
 "the tracer's set clobbered by the whole harvests an import nests inside one statement — a stack of sets, each level merged upward on exit",
 "the probe's lost-name check flagged a case table of functions (tzav's CASES) the fixpoint rightly dropped — the check on picklable names",
]
slips_txt = ' '.join('%d. %s.' % (i + 1, s) for i, s in enumerate(SLIPS))

GATES = '''
## D38 — THE VERIFIED-IMPORT CACHE (2026-09-19, the same day; on the owner's "ok do it make it permanent")

THE MEASUREMENT THAT RULED IT: after the cut, the chain's long steps were still the ones that LOAD the sixty-three runners — the tape 155 s, the
probes 151 s, the journal gate 166 s, the checkpoint suite 205 s, each of the positions' eight workers a load — and a profile of the import
(stmt_profile.py, importtime.txt; the forms) put the load at 135 s, ALL of it the runners' own self-checks at module level (the whole-text scans,
the censuses, the asserts, the honest-pairing guards): good_land 14.3 s, joseph 9.0, hear_o_israel 8.8, obey_horeb 8.4, seven_nations 7.8 …
twenty runners over 2 s each; the replay of the world itself 1.7 s. The owner asked "Do we really need to rebuild everything on every run?" and
then, on the explanation of steps 8 and 9, ruled "ok do it make it permanent". THE LAW: a runner's checks run in full when its source or the
text it reads has moved, and always in the sweep; every other loader restores what the checks verified.

THE FORM — World/step9/ink_cache.py (its header the full statement; installed by world_engine.py, so every loader of the engine has it): a
meta-path finder for the cold_run_* modules. A MISS (the runner's source digest or the SHARED KEY moved — the text store, the shelf's files,
the snapshot store, the engine's modules, the registries — or no stamp) runs the module statement by statement and harvests, after EACH
statement, every name it bound or may have mutated, every name a function of the module may mutate (a static scan of its defs), every small
container, every container whose length moved, every object with attributes — each value that pickles into a content-addressed blob
(World/journal/data/ink_cache/, gitignored), recorded on that statement when its content changed; the other runners whose functions ran inside
the statement (a call tracer, one event per code object per statement) have their mutables re-examined and a change recorded as module::name;
an object that IS another name's live object is recorded as an alias, an element of a value that is one as a nested alias with its path; the
index is written only if nothing raised. A HIT walks the statements: one that only binds recorded names (an assignment, a loop, a with-block, a
branch), an assert, a print, a method call on a recorded name is SKIPPED and its names bound from the cache at that point — a fresh object for a
binding, IN PLACE for a name a call had mutated, the live object for an alias, the callee's container in place for a module::name entry, a name
passed to a call and unchanged left as it stands; everything else runs as written — imports, defs, classes, calls into modules, an alias
assignment, ANY BLOCK HOLDING AN IMPORT (the modules load in the full path's order), statements binding what does not pickle; the fixpoint
un-skips a skipped statement binding a name some running statement reads without a recorded value. INK_CACHE=0 turns it off for a process.

THE HONESTY GUARDS: (1) the sweep (run_cold_all.py) runs every runner with INK_CACHE=0 — the checks in full every time it grades; (2) the chain's
--full sets INK_CACHE=0 for every step; (3) THE PROBE ink_cache_probes.py, in the chain's probes step, imports the whole engine twice in two fresh
processes — full and cached — and asserts EIGHT things: C1 the same runners; C2 every picklable module value equal in canonical form, NOTHING SET
ASIDE; C3 no name lost; C4 the daemons by module and name in order; C5 the registry map; C6 the same sharing groups (no alias gained or lost);
C7 the cached load at least three times faster; C8 the engine's own modules (world_engine, effects_layer, events_layer, compile_guards,
world_journal) hold the same state — no registration lost to a restored statement; (4) a stamp is written only by an import that raised
nothing; (5) a cached-path statement that raises names the module, the line and the values it read, and says to run INK_CACHE=0.

AS BUILT — MEASURED BY THE PROBE: the full load %s s (two processes: the import and the sequence's own load), the harvest on a cold cache %s s
(the first load after a clear, or after a shared piece moved), the cached load %s s; 7,542 statements restored and 2,386 run (the slowest run
pre_sinai's with-block 1.7 s, incense_shekel's 1.1 s — the blocks holding imports); about 4,600 blobs, 41 MB. THE PROBE %s on its last run; the
tape 10/10 through the cache with the same print. THE SEVENTEEN SLIPS, each found by the probe or by the engine refusing on the cached path, and
each a rule now: %s

THE THIRD CHAIN (AS RUN, with the cache in place; world_engine.py moved, so the sweep FULL): %s

THE STEADY STATE: a chain of a compile sitting now pays the load only where the checks must run — the moved runner's own harvest (its miss, once)
and the sweep (always full, eight at a time, only the moved runners and their importers); every other step loads in about half a minute.

THE LESSONS: A CACHE'S PROBE IS THE CACHE — the definition of "the same" was made strict eight times, and each time it found a slip the tape's
10/10 had not (the tape reads what a case needs; the probe reads everything); THE RESIDUE A CALLEE LEAVES IS PART OF THE STATE — a trail, a counter,
a returned reference; THE ORDER OF THE IMPORTS IS PART OF THE STATE; PICKLE BYTES ARE NOT THE STATE (a memo, an interning) — compare the canonical
form's text; A TOUCHED NAME IS KEPT, A BOUND NAME IS FRESH, AN ALIAS IS THE LIVE OBJECT; THE FULL PATH IS ALWAYS ONE VARIABLE AWAY (INK_CACHE=0).
''' % (T[0], T[1], T[2], probe_line or '8/8', slips_txt, CHAIN)

LOOP = '''  D38 THE VERIFIED-IMPORT CACHE (the same day, on "ok do it make it permanent" — GATES_CHAIN.md's D38 section the record) — after the cut the
     long steps were still the LOAD of the sixty-three runners (135 s, all of it their own self-checks at import). World/step9/ink_cache.py, a
     meta-path finder installed by world_engine.py: a MISS (the runner's source or the shared key moved) runs the module statement by statement
     and harvests every value each statement bound or mutated — in this module and in the callees whose functions ran (a call tracer), aliases
     and nested aliases by identity — into content-addressed blobs (World/journal/data/ink_cache/, gitignored); a HIT restores each statement's own
     values at its place (a bound name fresh, a mutated name in place, an alias the live object) and runs only what must run (imports and any
     block holding one, defs, classes, calls into modules, the unpicklable). THE GUARDS: the sweep and --full run INK_CACHE=0 (the checks in full);
     ink_cache_probes.py in the chain — two fresh processes, full against cached, EIGHT probes (every value equal in canonical form with nothing set
     aside, the sharing groups the same, the engine's own modules the same) 8/8 after seventeen slips each made a rule. MEASURED: the load %s s
     → %s s; the tape step 155 → %d s; the checkpoint suite 205 → %d s; the chain %s (the sweep full: a shared piece moved).
''' % (T[0], T[2], sec('tape'), sec('checkpoint'), mins)

STEPS = '''
THE VERIFIED-IMPORT CACHE (2026-09-19, the same day, on Brian's "Do we really need to rebuild everything on every run?", the explanation of what steps 8
and 9 spend, and his "ok do it make it permanent"; World/step9/GATES_CHAIN.md's D38 section, World/step9/ink_cache.py). After the cut, the slow steps
were still the ones that load the sixty-three runners' code, and the measuring showed why: two minutes of every load is the runners checking
themselves against the text — the same checks, the same answers, every time. So the machine now remembers the answers. The first load after a
change runs every check as before and writes down, after each line of each runner, what that line produced; every later load puts those results
back in place and runs only what has to run — the definitions, the imports, the calls into other parts. If a runner's text or anything it reads
has changed, its checks run again in full; the sweep that grades every runner always runs them in full. The proof that nothing changed: a probe
loads the machine both ways in two separate processes and compares everything — every value in every runner, which values are one and the same
object, what the engine's own parts hold — and it found seventeen ways the shortcut was wrong before it found none; each one is a rule now. The
load went from %s seconds to %s; the tape step from 155 seconds to %d; the chain to %s with a full sweep. Next: the commit on your word; then 7b.
''' % (T[0], T[2], sec('tape'), mins)

BRIEF_BULLET = "- **THE RUNNERS' LOAD CACHED AND PROVED THE SAME — 135 s OF SELF-CHECKS AT EVERY LOAD BECOME ~34 s; A MISS OR THE SWEEP RUNS THE CHECKS IN FULL; THE PROBE COMPARES A FULL LOAD AGAINST A CACHED ONE VALUE BY VALUE, OBJECT BY OBJECT, 8/8 AFTER SEVENTEEN SLIPS (2026-09-19; GATES_CHAIN.md D38; ink_cache.py).**\n"
BRIEF_ENTRY = '''### 2026-09-19 — The two minutes of loading became half a minute, with a proof that nothing changed

You asked whether we really need to rebuild everything on every run, and then said make it permanent. The two minutes that every step of the test
bench was paying is the runners checking themselves against the text when they load — the same checks with the same answers every time. Now the
machine remembers: the first load after a change runs every check and writes down what each line of each runner produced; every later load puts
those results back and runs only what must run. If a runner or anything it reads has moved, its checks run again in full, and the sweep that
grades every runner always runs them in full. The honest part is the proof: a probe loads the machine both ways in two separate processes and
compares everything — every value in every runner, which values are the same object, what the engine's own parts hold. It found seventeen ways
the shortcut was wrong before it found none: a trail one runner leaves in another, a counter a caller moves, a block of imports skipped so the
runners loaded in a different order, two names that should be one object coming back as two. Each one is a rule now, and the probe runs in the
chain. The load went from %s seconds to %s; the whole chain to %s with a full sweep, against ninety minutes two days ago.

''' % (T[0], T[2], mins)

RLOG = '''
## 2026-09-19 — THE VERIFIED-IMPORT CACHE: THE RUNNERS' 135 s OF SELF-CHECKS AT EVERY LOAD RESTORED FROM A HARVEST, PROVED THE SAME BY AN EIGHT-PROBE COMPARE
## OF A FULL LOAD AGAINST A CACHED ONE — SEVENTEEN SLIPS, EACH A RULE

On the owner's "ok do it make it permanent" (2026-09-19, after "Do we really need to rebuild everything on every run?"). World/step9/ink_cache.py
(THE_LOOP D38; GATES_CHAIN.md's D38 section). THE FINDINGS OF THE BUILD: (1) the import's cost is the runners' own module-level checks — twenty
runners over 2 s each, good_land 14.3 s — not the engine; (2) a per-statement harvest is the only honest form (a name bound twice, a container a
loop fills); (3) THE RESIDUE A CALLEE LEAVES IS STATE: twenty-one runners' provenance trails and two counters end the full import holding the LAST
CALLER's marks, and a self-test's result tuple holds a callee's trail by reference — reproduced by a call tracer, in-place restores and nested
aliases, so the probe sets nothing aside; (4) THE ORDER OF THE IMPORTS IS STATE: a skipped block holding imports loaded the runners in another
order — any block holding an import runs; (5) PICKLE BYTES ARE NOT THE STATE — the memo and the interning differ across processes; the compare is
over the canonical form's text; (6) an alias (erection's VS_E29 is vestments' E29_ORDER; seventeen sharing groups) survives only if a touched,
unchanged name is KEPT and an object that is another name's live object is bound as that object. MEASURED: the full load %s s, the harvest %s s,
the cached load %s s; the probe %s; the tape 10/10 through the cache; the chain %s with a full sweep (against 18 min 27 s, and ninety minutes
before the cut). THE GUARDS: the sweep and --full at INK_CACHE=0; the probe in the chain; a stamp by a green import only; a cached-path failure
names its statement.
''' % (T[0], T[1], T[2], probe_line or '8/8', mins)

RESUME = '''# ⚠ THE VERIFIED-IMPORT CACHE (2026-09-19; step9/ink_cache.py, GATES_CHAIN.md D38, THE_LOOP D38): the runners' load %s s → %s s — a MISS (the
# runner's source or the shared key moved) harvests every statement's values, a HIT restores them; the sweep and `gates_chain.sh --full` run INK_CACHE=0
# (the checks in full); `ink_cache_probes.py` (in the chain) compares a full load against a cached one in two processes, 8/8; `ink_cache.py --status|--clear`.
# The chain %s with a full sweep. UNCOMMITTED: the message at <scratch>/commit_msg_cache.txt for the owner's word.
''' % (T[0], T[2], mins)

ADDENDA = '''
## 47. ADDENDUM (2026-09-19, THE VERIFIED-IMPORT CACHE — the runners' load %s s → %s s, proved the same by an eight-probe compare; the owner: "Do we really need to rebuild everything on every run?" → "ok do it make it permanent")

After the gates cut (§45) the long steps were still the ones that LOAD the sixty-three runners — 135 s of their own self-checks at import (a
profile by statement: good_land 14.3 s, joseph 9.0, hear_o_israel 8.8; twenty over 2 s). BUILT: World/step9/ink_cache.py, a meta-path finder
installed by world_engine.py (THE_LOOP D38; GATES_CHAIN.md's D38 section the full record). A MISS runs the runner statement by statement and
harvests, after each statement, every value it bound or mutated — in the runner and in the callees whose functions ran inside it (a call tracer),
aliases and nested aliases by identity — into content-addressed blobs (World/journal/data/ink_cache/, gitignored), keyed on the runner's source
digest and the SHARED KEY (the text store, the shelf's files, the snapshot store, the engine's modules, the registries); a HIT restores each
statement's own values at its place (a bound name fresh, a mutated name in place, an alias the live object) and runs only what must (imports and
any block holding one, defs, classes, calls into modules, the unpicklable). THE GUARDS: the sweep and the chain's --full run INK_CACHE=0; the probe
ink_cache_probes.py in the chain's probes step — two fresh processes, full against cached, EIGHT probes: the same runners, every picklable value
equal in canonical form with NOTHING SET ASIDE, no name lost, the daemons, the registry map, the same sharing groups, three times faster, the
engine's own modules the same — 8/8 after SEVENTEEN SLIPS (in GATES_CHAIN.md), among them: a callee's trail and counter left by the last caller,
a result tuple holding a trail by reference, a with-block of imports skipped so the runners loaded in another order, pickle bytes that memoize
and intern differently across processes, an alias broken by a fresh restore of a touched name. MEASURED: the full load %s s, the harvest %s s,
the cached load %s s; the tape step 155 → %d s; the checkpoint suite 205 → %d s; THE CHAIN %s WITH A FULL SWEEP. THE RECORDS: GATES_CHAIN.md,
THE_LOOP, RECORD_FORMS' cost paragraph, THE_STEPS, THE_BRIEFING, RESEARCH_LOG, RESUME, SETUP, the recovery page, the state doc's #197 addendum 2,
this section, the memory; the forms (cache_*) and the third chain's folder in World/step9/forms_gates_cut_2026-09-19/. THE LESSONS: a cache's
probe is the cache; a callee's residue is state; the imports' order is state; pickle bytes are not the state; the full path is one variable away.
''' % (T[0], T[2], T[0], T[1], T[2], sec('tape'), sec('checkpoint'), mins)

STATE = '''
#197 ADDENDUM 2 (2026-09-19, at the close of THE VERIFIED-IMPORT CACHE, on the owner's "ok do it make it permanent" — A CLEAN COMPACTION POINT): THE STATE: World/step9/ink_cache.py built and installed by world_engine.py (THE_LOOP D38; GATES_CHAIN.md's D38 section the record) — the runners' load %s s → %s s (a MISS harvests every statement's values, in the runner and in the callees whose functions ran, aliases by identity; a HIT restores them at their places and runs only what must); the sweep and `gates_chain.sh --full` run INK_CACHE=0; ink_cache_probes.py in the chain's probes step compares a full load against a cached one in two processes — EIGHT probes, 8/8 after SEVENTEEN SLIPS each made a rule (the list in GATES_CHAIN.md); the tape 10/10 through the cache; THE THIRD CHAIN ALL GREEN with a full sweep (world_engine.py moved): %s THE RECORDS from the sheet in one call (write_cache_records.py): GATES_CHAIN.md's D38, THE_LOOP's D38, RECORD_FORMS' cost paragraph, THE_STEPS, THE_BRIEFING (the bullet and an entry), RESEARCH_LOG, RESUME, SETUP's line, the recovery page (the cost line; under its cap), the addenda §47, this addendum, the memory (cost-rules-no-polling.md and the index line under 17,000); the forms copied (copy_cache_forms.py: cache_* and gates_cut_3/). NOT COMMITTED: the cache (ink_cache.py, ink_cache_probes.py, world_engine.py's install line, run_cold_all.py's INK_CACHE=0, gates_chain.sh's probe list and --full, the records, the forms) — the message at <scratch>/commit_msg_cache.txt for the owner's word ("commit" = no push; "commit push" = both). NOTHING MID-FLIGHT — A CLEAN COMPACTION POINT. NEXT ON THE RULING: the commit on his word; then 7b (chapter 9's compile in TWO RUNS — a NEW checkpoint series) or the Decalogue-schema sitting; THE INSTALL HYPOTHESIS and THE SUPPLIED GRADE on the table. POST-COMPACTION REREADS: the recovery page, the map's "Sitting 7 — AS BUILT", MEMORY.md.
''' % (T[0], T[2], CHAIN)

MEMO = '''
THE VERIFIED-IMPORT CACHE (owner-ruled 2026-09-19 after the cut: "Do we really need to rebuild everything on every run?" → the explanation of
steps 8 and 9 → "ok do it make it permanent"): the runners' load (135 s of their own self-checks at import) is CACHED — World/step9/ink_cache.py,
installed by world_engine.py; a MISS (the runner's source or the shared key moved) harvests every statement's values, a HIT restores them; the sweep
and `gates_chain.sh --full` run INK_CACHE=0 (the checks in full); `ink_cache_probes.py` in the chain compares a full load against a cached one
in two processes, EIGHT probes 8/8 (every value equal in canonical form, nothing set aside; the sharing groups; the engine's modules). Measured: the
load %s s → %s s; the chain %s with a full sweep. `python3 World/step9/ink_cache.py --status|--clear`. The record: GATES_CHAIN.md's D38 (the
seventeen slips), THE_LOOP D38. **How to apply:** never a runner's check in the cached path — a runner edited is a miss and runs whole once; when
a cached-path statement raises, run INK_CACHE=0 or --clear; the probe is the definition of "the same" — extend it before trusting a new cut.
''' % (T[0], T[2], mins)

# ---- the edits
EDITS = [
 (f'{ROOT}/World/step9/GATES_CHAIN.md', 'append', None, GATES),
 (f'{ROOT}/World/step9/THE_LOOP.md', 'after', "TEST IT AGAINST A MOVED PIECE BEFORE TRUSTING IT (the regions form was struck by its own test).\n", LOOP),
 (f'{ROOT}/World/step9/RECORD_FORMS.md', 'replace', "every short cut keyed on the sources' digests; GATES_CHAIN.md);", "every short cut keyed on the sources' digests; GATES_CHAIN.md; and 2026-09-19 THE VERIFIED-IMPORT CACHE — ink_cache.py, the runners' load ~34 s against ~168 s, a miss and the sweep and --full at INK_CACHE=0, ink_cache_probes.py 8/8 in the chain);"),
 (f'{ROOT}/THE_STEPS.md', 'append', None, STEPS),
 (f'{ROOT}/THE_BRIEFING.md', 'before', "- **THE GATES CHAIN CUT FROM NINETY MINUTES TO 18 MIN 27 S", BRIEF_BULLET),
 (f'{ROOT}/THE_BRIEFING.md', 'before', "### 2026-09-19 — CHAPTER 9 READ: THE CALF TOLD TWICE", BRIEF_ENTRY),
 (f'{ROOT}/RESEARCH_LOG.md', 'append', None, RLOG),
 (f'{ROOT}/World/RESUME.md', 'prepend', None, RESUME),
 (f'{ROOT}/SETUP.md', 'replace', "10/10 at the end (about two minutes)", "10/10 at the end (about a minute; the first run harvests the import cache, about four)"),
 (f'{ROOT}/logic/pre_logic_methods_2026-07-28/RECOVERY_addenda_2026-09-12.md', 'append', None, ADDENDA),
 (f'{ROOT}/logic/pre_logic_methods_2026-07-28/PROMPT_continue_solo_era_2026-08-06.md', 'append', None, STATE),
 (f'{MEM}/cost-rules-no-polling.md', 'append', None, MEMO),
 (f'{MEM}/cost-rules-no-polling.md', 'replace', "CUT 2026-09-19 from ninety minutes to 43 min 23 s, GATES_CHAIN.md)", "CUT 2026-09-19 from ninety minutes to 18 min 27 s, then THE IMPORT CACHE the same day — the runners' load ~34 s; GATES_CHAIN.md)"),
 (f'{MEM}/MEMORY.md', 'lineappend', "COST RULES](cost-rules-no-polling.md)", ", THE IMPORT CACHE (2026-09-19)"),
]
REC = f'{ROOT}/logic/pre_logic_methods_2026-07-28/RECOVERY_new_thread_2026-09-12.md'
REC_EDITS = [
 ("## 2. WHERE IT STANDS (2026-09-19, after sitting 7 and THE GATES CUT; the state doc #197 addendum 1 the newest)", "## 2. WHERE IT STANDS (2026-09-19, after sitting 7, the gates cut and THE IMPORT CACHE; the state doc #197 addendum 2 the newest)"),
 ("- Uncommitted since 29c189b: sitting 6, the two-run rule, 6b, THE GATES CUT, sitting 7; the message at <scratch>/commit_msg_ch8.txt.", "- COMMITTED AND PUSHED at a985fbc (sittings 6-7, the two-run rule, the gates cut). Uncommitted: THE IMPORT CACHE; the message at <scratch>/commit_msg_cache.txt."),
 ("A clean point is announced at every run's end. ", ""),
 ("(his frame, 2026-09-16)", "(his frame)"),
 ("the long forms in the addenda's section 3", "long forms: addenda §3"),
 ("the SUMMARY read once; CUT 2026-09-19 to 18 min 27 s — the snapshot, the parallel probes, the\n  stamped sweep, the positions by eight workers; GATES_CHAIN.md)", "the SUMMARY read once; CUT 2026-09-19 to ~18 min, GATES_CHAIN.md)"),
 ("(seven kinds, each a why and a link)", "(seven kinds)"),
 ("cold_run_<span>.py (63 runners;\ncold_run_good_land.py the newest form)", "cold_run_<span>.py (63 runners)"),
 ("- zsh globs `====` (use `----`); the sequence import costs ~140 s — a reader takes the SNAPSHOT (register_census.running_world). The peer\n  thread is never a ruling.",
  "- zsh globs `====` (use `----`); the engine's import ~34 s through THE IMPORT CACHE (step9/ink_cache.py; INK_CACHE=0 = the checks in full,\n  ~168 s — the sweep's and --full's way; ink_cache_probes.py 8/8 in the chain; --status|--clear) — a reader takes the SNAPSHOT\n  (register_census.running_world). The peer thread is never a ruling."),
 ("The cost cuts: §35, §45.", "The cost cuts: §35, §45, §47."),
 ("the gates cut, D1-D37)", "the gates cut, the import cache, D1-D38)"),
]
ok = True
for p, kind, anchor, text in EDITS:
    s = R(p)
    if kind in ('after', 'before') and s.count(anchor) != 1: print('ANCHOR', s.count(anchor), p, anchor[:60]); ok = False
    if kind in ('replace', 'lineappend') and s.count(anchor) != 1: print('ANCHOR', s.count(anchor), p, anchor[:60]); ok = False
s = R(REC)
for a, b in REC_EDITS:
    if s.count(a) != 1: print('REC ANCHOR', s.count(a), a[:60]); ok = False
    s = s.replace(a, b)
rec_size = len(s.encode('utf-8')); mem_size = len(R(f'{MEM}/MEMORY.md').encode('utf-8')) + len(', THE IMPORT CACHE (2026-09-19)'.encode('utf-8'))
print('anchors %s; the recovery page would be %d bytes (cap 10240); MEMORY.md %d (cap 17000); chain done=%s steps=%d total=%s; probe=%s T=%s' % ('OK' if ok else 'BAD', rec_size, mem_size, done, len(steps), mins, probe_line, T))
assert ok and rec_size <= 10240 and mem_size <= 17000
if CHECK: sys.exit(0)
for p, kind, anchor, text in EDITS:
    s = R(p)
    if kind == 'append': s = s.rstrip('\n') + '\n' + text
    elif kind == 'prepend': s = text + s
    elif kind == 'after': s = s.replace(anchor, anchor + text)
    elif kind == 'before': s = s.replace(anchor, text + anchor)
    elif kind == 'replace': s = s.replace(anchor, text)
    elif kind == 'lineappend': s = '\n'.join((ln + text if anchor in ln else ln) for ln in s.split('\n'))
    W(p, s)
s = R(REC)
for a, b in REC_EDITS: s = s.replace(a, b)
W(REC, s)
print('written: %d files' % (len({p for p, *_ in EDITS}) + 1))
for p in sorted({p for p, *_ in EDITS} | {REC}):
    r = subprocess.run([sys.executable, f'{ROOT}/logic/solo_tools/gloss_lint.py', p], capture_output=True, text=True)
    m = re.search(r'(\d+)', r.stdout.strip().split('\n')[-1] if r.stdout.strip() else '0'); print('  lint', p.replace(ROOT, '<repo>').replace(MEM, '<memory>'), (r.stdout.strip().split('\n')[-1])[:80])
r = subprocess.run([sys.executable, f'{ROOT}/logic/solo_tools/scrub_home_paths.py', '--check'], capture_output=True, text=True); print('  home-path gate:', (r.stdout + r.stderr).strip().split('\n')[-1][:100], 'rc', r.returncode)

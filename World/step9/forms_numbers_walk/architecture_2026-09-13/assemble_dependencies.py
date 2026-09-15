import os as _os
_ROOT = _os.path.normpath(_os.path.join(_os.path.dirname(_os.path.abspath(__file__)), '..', '..', '..', '..'))   # THE PORTABLE REPO (2026-09-15): the repo root from this file's own place
#!/usr/bin/env python3
# DEPENDENCIES.md REWRITTEN FROM THE GATES' INDEXES (2026-09-13; the owner: "Update everything except Chronicles").
# The prose below; the tables built by script from World/step9/DEPENDENCY_INDEX.md, DAEMON_INDEX.md and
# dependency_dispositions.yaml (dep_runner_table.md, dep_daemon_table.md; the owed table rebuilt here with three columns).
import yaml
SP = '<scratch>/'
OUT = (_ROOT + '/ARCHITECTURE/DEPENDENCIES.md')
runners = open(SP + 'dep_runner_table.md', encoding='utf-8').read()
daemons = open(SP + 'dep_daemon_table.md', encoding='utf-8').read()
d = yaml.safe_load(open((_ROOT + '/World/step9/dependency_dispositions.yaml')))
owed = ['| From | To | Why the call waits (the record\'s own words, cut) |', '|---|---|---|']
for e in d['edges']:
    if e.get('disposition') == 'OWED':
        why = str(e.get('why')); why = why.split('|', 1)[1].strip() if '|' in why else why
        owed.append('| `%s` | `%s` | %s |' % (e['from'], e['to'], why[:300].replace('|', '/')))
owed = '\n'.join(owed) + '\n'

text = """# DEPENDENCIES — every edge between the compiled spans and the books they reach

The dependency graph of the compiled code, as the program's own gate
draws it. Written 2026-09-05 by hand from the fourteen spans of that
day; rewritten 2026-09-13 from the gate's index at the close of the
book of Numbers. An edge is listed only where the text or the code
names it: a verse in one span naming an offering type or an
institution whose home is another span (the type census), an explicit
pointer form in the ink ("as prescribed," "as the LORD commanded," "one
law," the comparative on an offering noun), or a live Python import
verified against the source. Every edge carries two answers. Its LABEL
under the link review law — a REFERENCE the text makes itself, a
TRANSFER that names its teacher, a HYPOTHESIS no teacher taught, or
NONE, a connection that carries no rule (a homograph, a test
registering another's rules). And its DISPOSITION, how it is wired — a
live CALL, a path VIA another runner, a PARAMETER carried rather than a
procedure, a call OWED with its debt named, a REVERSE (the home already
calls this runner, so a call back would cycle), or FALSE, a homograph
refused. The gate `World/step9/dependency_census.py` runs before every
cold sweep and refuses an edge without both; its index is
`World/step9/DEPENDENCY_INDEX.md`, regenerated on every run, and the
dispositions live in `dependency_dispositions.yaml`. THE_LINKS.md in
this folder teaches the kinds from thirteen worked examples.

![the span dependency graph](diagrams/02_dependencies.svg)

*The picture above dates from 2026-09-05 and shows the fourteen spans
of that day; it is redrawn when the tools are taught the fourth book.*

## The census, 2026-09-13

- 57 runners over 4,878 verses; 42 type tokens, 5 pointer forms.
- 482 edges: 292 references, 48 transfers with teachers, 9
  hypotheses, 133 of none. By wiring: 338 live calls, 32 reverse, 20
  via another runner, 8 parameters, 6 owed, 78 homographs refused.
- 173 pointers in the ink: 145 "as when" (the doing citing its
  command), 16 "as prescribed," 8 comparatives on an offering noun, 4
  "one law." 41 of them are run citations — the text's receipt for an
  order, closing a debit on the ledger; 101 point inside their own
  span; 19 call another runner; 2 carry a parameter; 10 are none.
- The fourth book's share: 178 edges (151 references, one transfer,
  26 homographs refused, no hypothesis) and 45 pointers (16 run
  citations, 29 internal).

## The runners

One row per compiled file, in the order of the scroll. "Calls out"
and "called by" are the live imports the gate verified; the five
counts are the edges the type census demanded of this runner and how
each was wired; "pointers" are the explicit cross-reference forms
found in its verses. The sequence runner is the tape itself: it calls
every other runner's daemon and is called by none.

""" + runners + """
## Edges from a compiled span into a book or a rite not yet compiled

The gate's OWED class: the text names an institution, the home runner
exists or does not, and the call has not been made. Each names the
line in `World/step9/COMPILE_DEBT.md` where it waits; the gate refuses
an owed edge without one. Six stand today.

""" + owed + """
Beyond these, the fourth book reaches into books not yet read, and
those links cannot be dispositioned at all until the reading: the
Levites' forty-eight cities and the six cities of refuge (Joshua 20
and 21; Deuteronomy 4:41-43), the daughters' holding (Joshua 17:4),
Caleb's Hebron (Joshua 14:13), the stipulation of Gad and Reuben
(Joshua 22:1-9), the dividers' commission (Joshua 14:1, 19:51), the
manslayer's term (Joshua 24:33), the refuge law's twin (Deuteronomy
19:1-13), the heifer of the unsolved murder (Deuteronomy 21:1-9), the
witnesses (Deuteronomy 17:6, 19:15). They stand on the ledger as open
entries with the closing verse named, and in the records as forward
seats.

## Edges from a compiled span into a narrative log

A run log is a later passage of the Bible read as a test of an earlier
law: the program runs the law on the narrated act and must reproduce
the breach or the fulfillment the text records. Forty-one pointers of
the "as when" form are the Torah's own run logs — "as the LORD
commanded Moses," the doing citing its order — and close debits the
orders opened. Beyond the Torah, the compiled spans read these:

| Span | Passage | What is checked |
|---|---|---|
| `tzav` (dues machine) | 1 Samuel 2:15-17 | the sons of Eli taking meat before the fat was burned, against the after-smoking gate |
| `mishpatim` (slave release) | Jeremiah 34:14 | the prophet quoting the servant law to a nation that had stopped keeping it |
| `tochacha` (the sabbath debt) | 2 Chronicles 36:21; Jeremiah 25:11 | the seventy years as the land's overdue rests collected |
| `beha` (the Levite age) | 1 Chronicles 23:24-27 | the Levite's age re-set to twenty with the reason "there is no more carrying" — the run rewriting the spec |
| `korach` (the tithe of the tithe) | Nehemiah 10:39 | the Levites bringing the tithe of the tithe, the duty's second seat |
| `shelach` (Caleb's holding) | Joshua 14:10-11 | the forty-five years and the strength "as on the day Moses sent me" |
| `gad_reuben` (the grant) | Joshua 4:13 | the forty thousand armed crossing, the stipulation's run citation |
| `refuge` (the Levite cities) | Joshua 21:3, 21:41 | the receipt outside the Torah; the four lots summing to forty-eight by the parser |
| `journeys` (the itinerary) | Deuteronomy 10:6-7; Joshua 5:11 | the two stations run the other way and Moserah observed; the morrow of the Passover at both ends |
| `zelophehad` (the holding) | Joshua 17:4 | the daughters' holding given before Eleazar and Joshua |

## Edges into the engine

Every compiled function is wrapped: 427 functions in 56 runners, 427
wrapped, none owed, none without a writer. Each daemon declares the
verse that speaks its law ("given at") and the act that switches it on
("installed by"): 22 are on from the start, 39 by an act, one pending.
The tent daemon in the engine installs the institutions and holds the
docket. The table is the daemon gate's own index
(`World/step9/DAEMON_INDEX.md`), in the order of the scroll.

""" + daemons + """
## Exam-side cross-book gradings (layer 4, not layer 3)

These are places where an exam block for one span was answered by a
compiled or derived file from another book. They are dependencies of the
tests, recorded in `EXAM_LEDGER.md` and the block reports, not edges in
the code.

| Exam block | Answered by | What crossed |
|---|---|---|
| the Passover offering block (Exodus 12) | Tzav's wrong-intent table (Leviticus 7) | the paschal for-its-name grid |
| the Egypt and generations block (Exodus 12) | Tzav's flesh-purity file (Leviticus 7:19-20) | the impure-Passover carve-outs and the karet exemption |
| the offerings consolidation (Leviticus 1-8) | the Passover engine (Exodus 12) | the Passover regime row |
| the appointed times (Leviticus 23:5) and the Passover engine (Exodus 12:6) | both grade Mishnah Pesachim 5:3 | "between the evenings": slaughtered before midday is invalid; two spans, one answer-sheet row |
| the offerings calendar (Numbers 28-29) and the appointed times (Leviticus 23) | one table, two seats | Leviticus 23's dates with the offerings as the new column; the dates by call to the appointed-times engine |
| the vows (Numbers 30) and the stipulation of Gad and Reuben (Numbers 32) | the utterance rule at its two seats | "that which has gone out of your mouth you shall do" — 32:24 graded by a call into the vows' cell |
| the refuge cities (Numbers 35) and the burglar (Exodus 22:1) | one status, two laws | "he has no blood" — the burglar's effect reused for the manslayer outside his city |

Since 2026-09-05 every compile sitting builds its docket by the union
rule: every segment of the local shelf citing a verse of the span, plus
the implementing tractates read by address. Those dockets live in
`logic/oral_triage/*_exam_*.md` and their rows are the answer tables
inside the runners; the fourth book's run from 159 rows (chapters 1-4)
to 1,280 (the offerings calendar).

## What the graph says

- **Leviticus is upstream of Exodus.** The most famous Exodus law,
  eye for eye, is compiled through Leviticus 24, and the slave's
  "forever" is scoped by Leviticus 25. The scroll's order and the
  code's dependency order are not the same order.
- **The fourth book calls everything.** Its runners are the most wired
  in the program: the refuge cities call fifteen others, Korach fifteen,
  Balak twelve, the borders nine. Numbers is where the earlier books'
  laws are asked to act, and the calls are the asking.
- **Genesis now contributes code edges.** Four story runners carry its
  narrative as events, and the story's verses are read by the law's own
  engines at two seats — the tunic dipped in blood (37:31) and the sacks
  searched from the eldest (44:12).
- **A shared spelling is not a link.** Seventy-eight demanded edges were
  refused as homographs, twenty-six of them in the fourth book; each
  refusal is written with the vowel point or the dictionary entry that
  decided it.
- **Six calls are owed and named.** The continual meal offering, the
  Levites' bulls and their meal offering, the trumpets over the
  offerings, the figured stones' ban, and the levirate's Deuteronomy
  seat wait on their sittings, each with a debt line.
- **The run logs reach past the Torah.** Ten compiled spans check
  themselves against Prophets or Writings; the whole-Tanakh indictment
  check is the same move at scale, and the readback of Joshua's acts is
  the next design.
"""
open(OUT, 'w', encoding='utf-8').write(text)
print('written', OUT, len(text.split('\n')), 'lines')

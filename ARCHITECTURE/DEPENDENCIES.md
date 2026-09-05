# DEPENDENCIES — every edge between the compiled spans and the books they reach

The dependency graph of the compiled code, drawn whole for the first
time. An edge is listed only where the code or its printed output names
it: a Python import, a CALLED cell, a ROUTED cell, an IMPORT cell, a
census across seats, or a run-log check inside a compile. Exam-side
cross-book gradings are listed separately because they live in layer 4,
not in the compiled functions.

![the span dependency graph](diagrams/02_dependencies.svg)

## Edges inside the compiled set

| From | To | Kind | What crosses | Where it is recorded |
|---|---|---|---|---|
| cold_run_mishpatim | cold_run_lev24 | CALL | the damage cell of the injury indemnities resolves through `talion()`, compiled from Leviticus 24:18-22 | mishpatim.py line 121: "CALLED cold_run_lev24.talion()"; Bava Kamma 83b:10, 84a:1; move M-07 exemplar c |
| cold_run_offerings | cold_run_pesach | ROUTE | Mishnah Zevachim 5:8's Passover row: night only, until midnight, registered eaters; the run asserts the Passover engine is present before routing | offerings.py lines 57-58 and 132-133 |
| cold_run_offerings | cold_run_vayikra5, cold_run_tzav | LAYERING | the per-chapter compiles remain the case-law layer beneath the span-wide dispatcher | offerings.py header, lines 9-11 |
| cold_run_decalogue | the ordinances span (mishpatim) | ROUTE | money theft and the person-to-person capital laws are routed to the span where their code lives | decalogue.py line 126 and lines 182-184 |
| cold_run_mishpatim_2 | cold_run_mishpatim, cold_run_guardians | TOTAL | the running total 44/44 is reported across the three files as one Mishpatim compilation | mishpatim_2.py output: "RUNNING TOTAL with passes 1+guardians" |

## Edges from a compiled span into a book not yet compiled

| From | To | Kind | What crosses | Where it is recorded |
|---|---|---|---|---|
| mishpatim: slave-release | Leviticus 25:10, the Jubilee | IMPORT | the pierced slave's "forever" is released at the Jubilee; the Leviticus 25 units are still drafts | Kiddushin 15a:19: "written even for the pierced 'forever'" |
| mishpatim: injury indemnities | Deuteronomy 25:11-12 | IMPORT | the humiliation payment's source | the sugya at Bava Kamma 8:1 |
| mishpatim_2: the seducer's fine | Deuteronomy 22:29 | FETCH | the amount: the ink of Exodus 22:16 holds only the pointer "like the dowry of the virgins"; the fifty shekels are fetched | move M-10 the pointer-fetch |
| calendar: kid_in_milk | Deuteronomy 14:21 | CENSUS | the kid-clause counted at its three seats (Exodus 23:19, 34:26, Deuteronomy 14:21), read as cooking, eating, benefit | Mishnah Chullin 8:4 |
| offerings: five import cells | Exodus 12:4, 12:8, 27:2; Leviticus 16:14, 27:32 | IMPORT | the Passover registration and night, the altar's horns, the inner sprinkling, the tithe | the file's verse references and its IMPORT-tagged cells |
| tzav: rejection and karet | Numbers 5:31; Leviticus 19:7 | CITE | cited inside the cells | tzav.py verse references |
| lev24: curse gate | the Noahide block, Sanhedrin 56a:20 | ROUTE | the epithet arm | lev24.py line 158 |
| moadim: rosh_hashanah | Leviticus 25:9, the Jubilee's shofar | IMPORT | the day's instrument; the Leviticus 25 units are still drafts | moadim.py line 216: "imported from the Jubilee"; Sifra Emor Section 11 6 |

## Edges from a compiled span into a narrative log

| From | To | Kind | What crosses | Where it is recorded |
|---|---|---|---|---|
| tzav: dues_machine | 1 Samuel 2:15-17 | RUN LOG | the sons of Eli taking meat before the fat was burned, checked against the after-smoking gate | tzav.py output: "PASS [MOVE] 1 Samuel 2:15-17 — the sons of Eli against the gate" |
| lev24: runtime code request | Leviticus 24:23 | RUN LOG | the span's own execution report grades itself, "as the LORD commanded" | lev24.py function 1 |

## Edges into the engine

| Daemon in world_engine.py | Compiled from | Events it fires on |
|---|---|---|
| law_slave_term | mishpatim F1 slave-release | acquire_hebrew_slave, slave_pierced, jubilee_proclaimed |
| law_goring_ox | mishpatim F3 goring-ox state machine | ox_gores |
| law_guardians | cold_run_guardians (the 12-cell matrix as a table) | bailment_claim |
| law_deposit_oath | vayikra5 deposit_restitution | sworn_denial_admitted |
| law_installation | tzav F7 installation | installation_commanded, milluim_blood_sprinkled, milluim_leftover |

The remaining 54 compiled functions are not yet wrapped.

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

## What the graph says

- **Leviticus is upstream of Exodus.** The most famous Exodus law,
  eye for eye, is compiled through Leviticus 24, and the slave's
  "forever" is scoped by Leviticus 25. The scroll's order and the
  code's dependency order are not the same order.
- **Three books are reached but not compiled.** Leviticus 25 (reached
  twice: the Jubilee's release and its shofar), Deuteronomy 14, 22, and
  25, and Numbers 5 appear as import targets. Each is a measured compile
  dependency waiting for its span.
- **Genesis contributes no code edges.** It supplies the world layer and
  twelve exam blocks. Its narrative cases are not yet typed into engine
  events; see the README's last section.
- **One narrative log is already inside a compile.** The sons of Eli in
  Tzav's dues machine is the single place a compiled function checks
  itself against a passage from the Prophets. The whole-Tanakh
  indictment check is the same move at scale.

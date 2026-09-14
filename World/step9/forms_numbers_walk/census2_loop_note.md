
## The ninth class, the fifth registry, the fifth view and the fifth question — THE POPULATION TABLE (as built at THE NUMBERS WALK
## sitting 8b, 2026-09-11; the design in World/step9/NUMBERS_WALK.md "Sitting 8b"; the speculation ARCHITECTURE/DATABASE_SPECULATION.md)

The loop's memory gained a TABLE beside its ledger. The owner's recommendation taken 2026-09-11 ("Ok go"): the population table built
inside the compile of the second census, minimal and honest, the backward seeding filed.
- THE ENGINE: World.tables — the tables of the FIFTH REGISTRY World/step9/population_schema.yaml (the columns the ink's own words: tribe,
  family, gentilic, level, count, threshold, person, father, mother, status, the delta's from/to/explained/unexplained; three grains —
  counted, named, delta — each with its required and optional columns). World.row(table, row): a daemon writes a row WHILE CONSUMING AN
  EVENT — a row written by hand is refused (the law in code); the row validated against the schema (a known table, a known grain, every
  required column, no unknown column), stamped written_by / day / year / table, appended to the table, logged as the class ROW.
  World.population(**where): the daemons' query by equality — the census daemon reads its own chapter-1 rows to declare the deltas at 26.
  A row is not a ledger entry (no op, no open, no close, no counterparty) and moves no count of the RUN tuple; a subject of a row is not an
  entity (the tribes and the families stay names; the persons the roll names enter the table, the registry unchanged).
- THE JOURNAL: the NINTH log class ROW → run.row (world_journal.KINDS; the register World/journal/registers/event_kinds.yaml); the sink's
  line for a row — subj the row's subject through the registry (a named row's person id, a counted row's tribe name), unit the writing
  daemon, ref the verse the row was written from, data the row as stamped.
- THE FIFTH VIEW run_population (World/journal/run_views.sql): one row per run.row — grain, as_of (the census the row belongs to), tribe,
  family, level, person, father, status, count, delta, unexplained, day, year, written_by, verse; the views gate's population check (the
  view's rows = the run.row lines, derived from the table's own counts on every world).
- THE FIFTH QUESTION `population [<tribe>]` (world_journal.ask): every row of the running world in the run's order, or one tribe's — the
  ask-tool's fifth answer beside ledger / open / who / custody.
- THE PROBES: population_probes.py (P1-P9 — written first, 0/9 on the unchanged engine, 9/9 after: the rows and their writer, the refusal
  by hand, the three schema refusals, the query, the daemon's own delta rows from its rows, the sink's run.row lines, the view and the gate,
  the question, the RUN counts unmoved); journal_probes J3 amended (the seven engine classes the probe world exercises are KINDS less
  run.skip and run.row — the ninth class exercised by P6); journal 6/6 and view 6/6 unmoved.
- THE FIRST WRITER AND THE FIRST READERS: law_second_census (cold_run_second_census.py) writes the first roll's rows on the SHARED kinds
  census_taken and levites_counted (rows only, no effect — an empty watch), the second roll's rows, the deltas (declared: the tape's
  explanations by CALL beside the ink's number, the remainder labeled unexplained) and the named rows at its lines; the daughters' row
  (26:33 — "had no sons, only daughters" on the table BEFORE the plea at 27:1) and Jochebed's row (26:59 — CJ3b's ink witness) are the
  table's first consumers; the sequential run's CP1-CP9 grade the table on the tape.
- FILED: the backward seeding (the ark's kind table, Genesis 10's nations, Genesis 46's roster by name) — a COMPILE_DEBT line naming the
  consumer that would call for it (a daemon querying a person before Numbers 1); the second pass after Deuteronomy the natural seat.

-- run_views.sql — THE RUN VIEWS (THE LOOP step 2's remainder, 2026-09-09; decision D8; the population view 2026-09-11; the ledger's
-- close join 2026-09-12 — THE CLOSE LINE; the design in
-- World/step9/THE_LOOP.md "Step 2 THE INDEX — the remainder"). SQL VIEWS over worldledger's events table, created at every
-- reindex after the table is rebuilt (World/step9/world_journal.py views()) — rebuilt from the events table, never written
-- directly; json_extract over the row's `data` (the payload as it stood at the run's end). Every view carries `source` (the
-- segment's name — one run world each) and `seq` (the run's own order).

DROP VIEW IF EXISTS run_docket;
DROP VIEW IF EXISTS run_ledger;
DROP VIEW IF EXISTS run_timers;
DROP VIEW IF EXISTS run_clock;
DROP VIEW IF EXISTS run_population;

-- THE POPULATION TABLE (THE NUMBERS WALK 8b, 2026-09-11; World/step9/NUMBERS_WALK.md "Sitting 8b"): one row per run.row — a daemon's
-- write into the fifth registry's table (World.row; population_schema.yaml): the grain (counted / named / delta), the census it belongs
-- to (as_of), the tribe, the family and its level, the person with father and status, the count, the delta with its unexplained remainder,
-- the writing daemon, the verse. The FIFTH VIEW; the question `population [<tribe>]` reads it.
CREATE VIEW run_population AS
SELECT source, seq, subj AS subject,
       json_extract(data, '$.grain')       AS grain,
       json_extract(data, '$.as_of')       AS as_of,
       json_extract(data, '$.tribe')       AS tribe,
       json_extract(data, '$.family')      AS family,
       json_extract(data, '$.level')       AS level,
       json_extract(data, '$.person')      AS person,
       json_extract(data, '$.father')      AS father,
       json_extract(data, '$.status')      AS status,
       json_extract(data, '$.count')       AS count,
       json_extract(data, '$.delta')       AS delta,
       json_extract(data, '$.unexplained') AS unexplained,
       op                                  AS day,
       json_extract(data, '$.year')        AS year,
       unit                                AS written_by,
       ref                                 AS verse
FROM events
WHERE kind = 'run.row';

-- THE LEDGER: one row per ledger write (run.write, run.retro_write) — the entity, the effect, the day written, the day closed and
-- the closer, the writing daemon, the verse. SINCE THE LOOP step 1's amendment THE CLOSE LINE (2026-09-12; THE_LOOP.md): the write row is
-- a SNAPSHOT at write time and carries no closer; the close is its own line (run.close) naming the entry by its write ordinal
-- (data.seq = data.entry_seq), and this view JOINS the two on (source, subj, ordinal) — open = 0 when a close row exists, day_closed the
-- close row's day, closed_by the close row's note; entry_seq and close_seq the two lines' own names
CREATE VIEW run_ledger AS
SELECT w.source, w.seq, w.subj AS entity,
       json_extract(w.data, '$.effect')       AS effect,
       json_extract(w.data, '$.op')           AS ledger_op,
       w.op                                   AS day_written,
       json_extract(w.data, '$.year')         AS year,
       json_extract(w.data, '$.value')        AS value,
       json_extract(w.data, '$.counterparty') AS counterparty,
       CASE WHEN c.seq IS NOT NULL THEN 0 ELSE json_extract(w.data, '$.open') END AS open,
       c.op                                   AS day_closed,
       json_extract(c.data, '$.note')         AS closed_by,
       w.unit                                 AS written_by,
       w.ref                                  AS verse,
       w.kind,
       json_extract(w.data, '$.seq')          AS entry_seq,
       c.seq                                  AS close_seq
FROM events w
LEFT JOIN events c ON c.kind = 'run.close' AND c.source = w.source AND c.subj = w.subj
                   AND json_extract(c.data, '$.entry_seq') = json_extract(w.data, '$.seq')
WHERE w.kind IN ('run.write', 'run.retro_write');

-- THE TIMERS: one row per run.timer_set (a period timer's re-arm is its own set), joined LEFT to its fire and to its cancel on
-- (source, entity, effect, the due day = the fire's day / the cancel's recorded due): fired | cancelled | pending
CREATE VIEW run_timers AS
SELECT s.source, s.seq, s.subj AS entity,
       json_extract(s.data, '$.effect')       AS effect,
       s.op                                   AS day_set,
       json_extract(s.data, '$.due')          AS due,
       CASE WHEN f.seq IS NOT NULL THEN 'fired' WHEN c.seq IS NOT NULL THEN 'cancelled' ELSE 'pending' END AS outcome,
       f.op                                   AS day_fired,
       c.op                                   AS day_cancelled,
       json_extract(c.data, '$.cancelled_by') AS cancelled_by,
       json_extract(s.data, '$.rearmed_from') AS rearmed_from,
       s.unit                                 AS written_by,
       s.ref                                  AS verse
FROM events s
LEFT JOIN events f ON f.kind = 'run.timer_fire' AND f.source = s.source AND f.subj = s.subj
                   AND json_extract(f.data, '$.effect') = json_extract(s.data, '$.effect')
                   AND f.op = json_extract(s.data, '$.due')
                   AND json_extract(f.data, '$.value') IS json_extract(s.data, '$.value')
                   -- THE DEUTERONOMY WALK 1b (2026-09-15): the fire joined on the timer's VALUE too (null-safe) — two period timers of one effect on one
                   -- subject fall on one day (the month's musaf and Rosh Hashanah's at (40, 7, 1); the month's and the Sabbath's at (40, 11, 1), the
                   -- speech's marker day) and the join by day alone paired each set row with both fires: timers 100 for sets 96 at the first journal gate
                   -- after the walk; the value (the timer's key list) tells them apart
LEFT JOIN events c ON c.kind = 'run.timer_cancel' AND c.source = s.source AND c.subj = s.subj
                   AND json_extract(c.data, '$.effect') = json_extract(s.data, '$.effect')
                   AND json_extract(c.data, '$.due') = json_extract(s.data, '$.due')
                   AND json_extract(c.data, '$.value') IS json_extract(s.data, '$.value')
WHERE s.kind = 'run.timer_set';

-- THE CLOCK: the markers in the run's order with their class — forward (the counter walks), retrograde (the text's date earlier
-- than the counter, Pesachim 6b:7), proleptic (a paragraph's closing total; the counter unmoved, the stated day beside it)
CREATE VIEW run_clock AS
SELECT source, seq, op AS day, ref AS verse,
       json_extract(data, '$.value') AS value,
       CASE WHEN json_extract(data, '$.proleptic') = 1 THEN 'proleptic'
            WHEN json_extract(data, '$.retrograde') = 1 THEN 'retrograde'
            ELSE 'forward' END AS class,
       json_extract(data, '$.stated')    AS stated,
       json_extract(data, '$.placement') AS placement
FROM events
WHERE kind = 'run.marker';

-- THE DOCKET: the court's declarations owed (the halt on a case no standing law decides — Lev 24:12, Num 15:34), open until the
-- output verse closes them; the person the counterparty
CREATE VIEW run_docket AS
SELECT source, seq, entity, counterparty AS person, day_written, open, day_closed, closed_by, written_by, verse
FROM run_ledger
WHERE effect = 'declaration_owed';

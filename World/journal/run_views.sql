-- run_views.sql — THE FOUR RUN VIEWS (THE LOOP step 2's remainder, 2026-09-09; decision D8; the design in
-- World/step9/THE_LOOP.md "Step 2 THE INDEX — the remainder"). SQL VIEWS over worldledger's events table, created at every
-- reindex after the table is rebuilt (World/step9/world_journal.py views()) — rebuilt from the events table, never written
-- directly; json_extract over the row's `data` (the payload as it stood at the run's end). Every view carries `source` (the
-- segment's name — one run world each) and `seq` (the run's own order).

DROP VIEW IF EXISTS run_docket;
DROP VIEW IF EXISTS run_ledger;
DROP VIEW IF EXISTS run_timers;
DROP VIEW IF EXISTS run_clock;

-- THE LEDGER: one row per ledger write (run.write, run.retro_write) — the entity, the effect, the day written, the day closed
-- (the engine's closed_day stamp) and the closer (the closing act's verse note), the writing daemon, the verse
CREATE VIEW run_ledger AS
SELECT source, seq, subj AS entity,
       json_extract(data, '$.effect')       AS effect,
       json_extract(data, '$.op')           AS ledger_op,
       op                                   AS day_written,
       json_extract(data, '$.year')         AS year,
       json_extract(data, '$.value')        AS value,
       json_extract(data, '$.counterparty') AS counterparty,
       json_extract(data, '$.open')         AS open,
       json_extract(data, '$.closed_day')   AS day_closed,
       json_extract(data, '$.closed_by')    AS closed_by,
       unit                                 AS written_by,
       ref                                  AS verse,
       kind
FROM events
WHERE kind IN ('run.write', 'run.retro_write');

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
LEFT JOIN events c ON c.kind = 'run.timer_cancel' AND c.source = s.source AND c.subj = s.subj
                   AND json_extract(c.data, '$.effect') = json_extract(s.data, '$.effect')
                   AND json_extract(c.data, '$.due') = json_extract(s.data, '$.due')
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

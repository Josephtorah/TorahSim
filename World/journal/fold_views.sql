-- fold_views.sql — THE READING'S VIEWS over the world journal's index (D7'S MERGE, 2026-09-14; World/step9/THE_LOOP.md "D7'S MERGE — ONE
-- DATABASE": decision D20 THE OLD TABLES ARE VIEWS WITH THEIR OLD NAMES). The World folder's sixteen tables (World/schema.sql, kept as the
-- record of these columns) are SQL VIEWS over the fold rows of the events table (kind = 'fold.*', World/journal/build_world.py), created
-- at every reindex and at every attach by world_journal.views() beside the five run views — rebuilt from the journal, never written
-- directly. ONE EXCEPTION to the old names: the fold's `events` is `fold_events`, because `events` is the journal's own table.
-- The derived tables (entities, relations, entity_state, event_themes) are views computed here; the primary lists are rows.

DROP VIEW IF EXISTS entity_state;
DROP VIEW IF EXISTS relations;
DROP VIEW IF EXISTS entities;
DROP VIEW IF EXISTS event_themes;
DROP VIEW IF EXISTS meta;
DROP VIEW IF EXISTS checkpoints;
DROP VIEW IF EXISTS tests;
DROP VIEW IF EXISTS standing;
DROP VIEW IF EXISTS names;
DROP VIEW IF EXISTS mentions;
DROP VIEW IF EXISTS demands;
DROP VIEW IF EXISTS fold_events;
DROP VIEW IF EXISTS facts;
DROP VIEW IF EXISTS units;
DROP VIEW IF EXISTS refs;

-- the spine: every distinct verse in canonical order; ord is the world clock of the reading era
CREATE VIEW refs AS
SELECT json_extract(data, '$.ord') AS ord, json_extract(data, '$.ref') AS ref, json_extract(data, '$.book') AS book,
       json_extract(data, '$.chapter') AS chapter, json_extract(data, '$.verse') AS verse, json_extract(data, '$.unit') AS unit,
       json_extract(data, '$.first_seq') AS first_seq, json_extract(data, '$.last_seq') AS last_seq
FROM events WHERE kind = 'fold.ref';

CREATE VIEW units AS
SELECT json_extract(data, '$.seq_unit') AS seq_unit, json_extract(data, '$.unit') AS unit, json_extract(data, '$.first_ref') AS first_ref,
       json_extract(data, '$.steps') AS steps, json_extract(data, '$.facts') AS facts, json_extract(data, '$.opened') AS opened
FROM events WHERE kind = 'fold.unit';

CREATE VIEW facts AS
SELECT json_extract(data, '$.seq') AS seq, json_extract(data, '$.unit') AS unit, json_extract(data, '$.ref') AS ref, json_extract(data, '$.fact') AS fact
FROM events WHERE kind = 'fold.fact';

CREATE VIEW fold_events AS
SELECT json_extract(data, '$.seq') AS seq, json_extract(data, '$.unit') AS unit, json_extract(data, '$.ref') AS ref,
       json_extract(data, '$.verb') AS verb, json_extract(data, '$.agent') AS agent
FROM events WHERE kind = 'fold.event';

CREATE VIEW event_themes AS
SELECT json_extract(e.data, '$.seq') AS seq, t.key AS idx, t.value AS theme
FROM events e, json_each(json_extract(e.data, '$.themes')) t
WHERE e.kind = 'fold.event';

CREATE VIEW demands AS
SELECT json_extract(data, '$.seq') AS seq, json_extract(data, '$.unit') AS unit, json_extract(data, '$.ref') AS ref,
       json_extract(data, '$.speaker') AS speaker, json_extract(data, '$.mood') AS mood, json_extract(data, '$.demand') AS demand,
       json_extract(data, '$.status') AS status, json_extract(data, '$.settled_seq') AS settled_seq, json_extract(data, '$.settled_unit') AS settled_unit,
       json_extract(data, '$.settled_ref') AS settled_ref, json_extract(data, '$.settle_kind') AS settle_kind, json_extract(data, '$.basis_en') AS basis_en,
       json_extract(data, '$.uncertain') AS uncertain
FROM events WHERE kind = 'fold.demand';

CREATE VIEW mentions AS
SELECT json_extract(data, '$.seq') AS seq, json_extract(data, '$.unit') AS unit, json_extract(data, '$.ref') AS ref,
       json_extract(data, '$.token') AS token, json_extract(data, '$.role') AS role, json_extract(data, '$.entity') AS entity
FROM events WHERE kind = 'fold.mention';

CREATE VIEW names AS
SELECT json_extract(data, '$.seq') AS seq, json_extract(data, '$.unit') AS unit, json_extract(data, '$.ref') AS ref,
       json_extract(data, '$.token') AS token, json_extract(data, '$.label') AS label
FROM events WHERE kind = 'fold.name';

CREATE VIEW standing AS
SELECT json_extract(data, '$.seq') AS seq, json_extract(data, '$.unit') AS unit, json_extract(data, '$.ref') AS ref,
       json_extract(data, '$.kind') AS kind, json_extract(data, '$.payload') AS payload
FROM events WHERE kind = 'fold.standing';

CREATE VIEW tests AS
SELECT json_extract(data, '$.seq') AS seq, json_extract(data, '$.unit') AS unit, json_extract(data, '$.ref') AS ref,
       json_extract(data, '$.verdict') AS verdict, json_extract(data, '$.oracle') AS oracle, json_extract(data, '$.theme') AS theme
FROM events WHERE kind = 'fold.test';

CREATE VIEW checkpoints AS
SELECT json_extract(data, '$.seq_unit') AS seq_unit, json_extract(data, '$.unit') AS unit, json_extract(data, '$.seq') AS seq,
       json_extract(data, '$.facts_n') AS facts_n, json_extract(data, '$.open_n') AS open_n, json_extract(data, '$.state_hash') AS state_hash
FROM events WHERE kind = 'fold.checkpoint';

-- the build's own facts: the counts and the state hash as key/value rows
CREATE VIEW meta AS
SELECT j.key AS key, j.value AS value
FROM events e, json_each(e.data) j
WHERE e.kind = 'fold.meta';

-- the cast: first mention and weights (the token of a theme resolved to its entity through the mentions of the same unit)
CREATE VIEW entities AS
WITH firsts AS (SELECT entity, min(seq) AS first_seq, count(*) AS mentions, sum(role = 'agent') AS as_agent FROM mentions GROUP BY entity),
     tok AS (SELECT unit, token, min(entity) AS entity FROM mentions GROUP BY unit, token),
     themes AS (SELECT COALESCE(tok.entity, t.value) AS entity, count(*) AS as_theme
                FROM events e, json_each(json_extract(e.data, '$.themes')) t
                LEFT JOIN tok ON tok.unit = json_extract(e.data, '$.unit') AND tok.token = t.value
                WHERE e.kind = 'fold.event' GROUP BY 1)
SELECT f.entity,
       (SELECT ref FROM mentions m WHERE m.entity = f.entity AND m.seq = f.first_seq LIMIT 1) AS first_ref,
       f.first_seq,
       (SELECT unit FROM mentions m WHERE m.entity = f.entity AND m.seq = f.first_seq LIMIT 1) AS first_unit,
       f.mentions, f.as_agent, COALESCE(th.as_theme, 0) AS as_theme
FROM firsts f LEFT JOIN themes th ON th.entity = f.entity
UNION ALL
SELECT th.entity, NULL, 1000000000, NULL, 0, 0, th.as_theme FROM themes th WHERE th.entity NOT IN (SELECT entity FROM firsts);

-- relations: a projection, never invented; every row cites the seq it came from (source = event | name | demand)
CREATE VIEW relations AS
WITH tok AS (SELECT unit, token, min(entity) AS entity FROM mentions GROUP BY unit, token)
SELECT json_extract(e.data, '$.seq') AS seq, r.ord AS ord, json_extract(e.data, '$.ref') AS ref, json_extract(e.data, '$.unit') AS unit,
       COALESCE(ta.entity, json_extract(e.data, '$.agent')) AS subject, json_extract(e.data, '$.verb') AS relation,
       COALESCE(tt.entity, t.value) AS object, 'event' AS source
FROM events e, json_each(json_extract(e.data, '$.themes')) t
LEFT JOIN refs r ON r.ref = json_extract(e.data, '$.ref')
LEFT JOIN tok ta ON ta.unit = json_extract(e.data, '$.unit') AND ta.token = json_extract(e.data, '$.agent')
LEFT JOIN tok tt ON tt.unit = json_extract(e.data, '$.unit') AND tt.token = t.value
WHERE e.kind = 'fold.event'
UNION ALL
SELECT n.seq, r.ord, n.ref, n.unit, COALESCE(tn.entity, n.token), 'named', n.label, 'name'
FROM names n LEFT JOIN refs r ON r.ref = n.ref LEFT JOIN tok tn ON tn.unit = n.unit AND tn.token = n.token
UNION ALL
SELECT d.seq, r.ord, d.ref, d.unit, COALESCE(ts.entity, d.speaker), 'demands', d.demand, 'demand'
FROM demands d LEFT JOIN refs r ON r.ref = d.ref LEFT JOIN tok ts ON ts.unit = d.unit AND ts.token = d.speaker;

-- names with validity ranges: from_ord inclusive, to_ord exclusive; to_ord NULL = still holds at the corpus's end
CREATE VIEW entity_state AS
WITH tok AS (SELECT unit, token, min(entity) AS entity FROM mentions GROUP BY unit, token),
     nm AS (SELECT COALESCE(tn.entity, n.token) AS entity, n.label AS value, r.ord AS from_ord, n.ref AS from_ref, n.seq AS seq
            FROM names n LEFT JOIN refs r ON r.ref = n.ref LEFT JOIN tok tn ON tn.unit = n.unit AND tn.token = n.token)
SELECT entity, 'name' AS key, value, from_ord, from_ref,
       LEAD(from_ord) OVER (PARTITION BY entity ORDER BY from_ord, seq) AS to_ord,
       LEAD(from_ref) OVER (PARTITION BY entity ORDER BY from_ord, seq) AS to_ref,
       seq
FROM nm;

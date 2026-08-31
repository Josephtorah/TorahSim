-- world.sqlite — a QUERYABLE world, not a ledger.
--
-- Built read-only from corpus_world.fold(). Nothing here is authored by hand
-- and nothing is ever written back to the repo. Drop the file and rebuild.
--
-- Design note: the creation week is a SPECIAL CASE, not the template. There
-- are no heavens/earth/time tables and no `day` axis. The spine is `refs`
-- (corpus-scoped verse order) and everything hangs off entity + ref.

PRAGMA foreign_keys = ON;

CREATE TABLE meta (
  key   TEXT PRIMARY KEY,
  value TEXT
);

-- ---------------------------------------------------------------- the spine
-- Every distinct verse reference, in one global order across the corpus.
-- `ord` is the world clock: any state question is "as of ord N".
CREATE TABLE refs (
  ord      INTEGER PRIMARY KEY,
  ref      TEXT UNIQUE,          -- "Gen.1.2"
  book     TEXT,
  chapter  INTEGER,
  verse    INTEGER,
  unit     TEXT,
  first_seq INTEGER,
  last_seq  INTEGER
);
CREATE INDEX idx_refs_ref ON refs(ref);

CREATE TABLE units (
  seq_unit  INTEGER PRIMARY KEY,
  unit      TEXT UNIQUE,
  first_ref TEXT,
  steps     INTEGER,
  facts     INTEGER,
  opened    INTEGER
);

-- ------------------------------------------------------------- what exists
-- Corpus-resolved entities (the registry has already merged tokens that are
-- the same person across units).
CREATE TABLE entities (
  entity     TEXT PRIMARY KEY,
  first_ref  TEXT,
  first_seq  INTEGER,
  first_unit TEXT,
  mentions   INTEGER,
  as_agent   INTEGER,
  as_theme   INTEGER
);

-- The bridge from a surface token in a verse to the entity it denotes.
CREATE TABLE mentions (
  seq    INTEGER,
  unit   TEXT,
  ref    TEXT,
  token  TEXT,
  role   TEXT,
  entity TEXT
);
CREATE INDEX idx_mentions_entity ON mentions(entity);
CREATE INDEX idx_mentions_ref    ON mentions(ref);

-- NOTE: `seq` throughout is the ORDINAL OF THE OPERATOR that produced the
-- row. One operator may emit several rows, so seq is indexed, never unique.

-- ---------------------------------------------------------------- what happens
CREATE TABLE events (
  seq   INTEGER,
  unit  TEXT,
  ref   TEXT,
  verb  TEXT,
  agent TEXT
);
CREATE INDEX idx_events_agent ON events(agent);

CREATE TABLE event_themes (
  seq   INTEGER,
  idx   INTEGER,
  theme TEXT
);
CREATE INDEX idx_themes_seq ON event_themes(seq);

CREATE TABLE facts (
  seq  INTEGER,
  unit TEXT,
  ref  TEXT,
  fact TEXT
);

-- Obligations. status OPEN means the corpus never records it discharged.
CREATE TABLE demands (
  seq          INTEGER,
  unit         TEXT,
  ref          TEXT,
  speaker      TEXT,
  mood         TEXT,
  demand       TEXT,
  status       TEXT,
  settled_seq  INTEGER,
  settled_unit TEXT,
  settled_ref  TEXT,
  settle_kind  TEXT,
  basis_en     TEXT,
  uncertain    INTEGER
);
CREATE INDEX idx_demands_status ON demands(status);

CREATE TABLE names (
  seq   INTEGER,
  unit  TEXT,
  ref   TEXT,
  token TEXT,
  label TEXT
);

CREATE TABLE standing (
  seq     INTEGER,
  unit    TEXT,
  ref     TEXT,
  kind    TEXT,
  payload TEXT
);
CREATE INDEX idx_standing_kind ON standing(kind);

CREATE TABLE tests (
  seq     INTEGER,
  unit    TEXT,
  ref     TEXT,
  verdict TEXT,
  oracle  TEXT,
  theme   TEXT
);

CREATE TABLE checkpoints (
  seq_unit   INTEGER PRIMARY KEY,
  unit       TEXT,
  seq        INTEGER,
  facts_n    INTEGER,
  open_n     INTEGER,
  state_hash TEXT
);

-- --------------------------------------------------- derived: relations
-- A projection, never invented data. Every row cites the seq it came from.
--   source = event | name | demand
CREATE TABLE relations (
  seq      INTEGER,
  ord      INTEGER,          -- refs.ord, so relations are orderable in time
  ref      TEXT,
  unit     TEXT,
  subject  TEXT,
  relation TEXT,
  object   TEXT,
  source   TEXT
);
CREATE INDEX idx_rel_subject ON relations(subject);
CREATE INDEX idx_rel_object  ON relations(object);
CREATE INDEX idx_rel_ord     ON relations(ord);

-- ------------------------------------------- derived: state over time
-- Attributes with validity ranges. from_ord inclusive, to_ord exclusive;
-- to_ord NULL means "still holds at the end of the corpus".
CREATE TABLE entity_state (
  entity    TEXT,
  key       TEXT,             -- name | ...
  value     TEXT,
  from_ord  INTEGER,
  from_ref  TEXT,
  to_ord    INTEGER,
  to_ref    TEXT,
  seq       INTEGER
);
CREATE INDEX idx_state_entity ON entity_state(entity);
CREATE INDEX idx_state_key    ON entity_state(key);
CREATE INDEX idx_facts_seq ON facts(seq);
CREATE INDEX idx_names_seq ON names(seq);
CREATE INDEX idx_events_seq ON events(seq);
CREATE INDEX idx_demands_seq ON demands(seq);
CREATE INDEX idx_standing_seq ON standing(seq);
CREATE INDEX idx_tests_seq ON tests(seq);

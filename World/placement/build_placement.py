#!/usr/bin/env python3
"""PHASE 4 — fold reviewed placements into the world, with propagation.

THE STRUCTURAL FINDING OF THE PILOT: a placement layer cannot be a per-verse
tagger. Vayetze places Jacob at Haran ONCE, at 28:10, and then says nothing
about where he is for the next eighty-eight verses — the twenty years of
service happen at an unnamed well, an unnamed field, unnamed tents. A tagger
would leave Jacob's location blank for most of the parashah.

So placement is STATE: an entity is placed at an ordinal and STAYS there until
something moves it. Every row therefore carries a validity range (from_ord,
to_ord) rather than a single verse, which is the shape the world's schema
already uses for entity_state.

Rows come from two sources and each row says which:
  machine  — a proposal the extractor made and the review ACCEPTED
  reading  — a placement a human read out of the verse, cited to that verse
Nothing is invented: every row cites the verse that licenses it.
"""
import json, sqlite3, sys

WORLD = "<world-link>/world.sqlite"
REVIEW = "<world-link>/placement/reviewed_vayetze.json"

SCHEMA = """
drop table if exists placement;
create table placement (
  entity    text not null,
  relation  text not null,      -- at | to | from
  place     text not null,
  from_ord  integer not null,   -- the world clock: placement begins here
  from_ref  text not null,
  to_ord    integer,            -- null = still holds at the end of the span
  to_ref    text,
  source    text not null,      -- machine | reading
  evidence  text not null,
  unit      text
);
create index placement_entity on placement(entity);
create index placement_ord on placement(from_ord);
"""


def main():
    rows = json.load(open(REVIEW))
    accepted = [r for r in rows if r["verdict"] == "accept"]
    c = sqlite3.connect(WORLD)
    ords = {r: o for r, o in c.execute("select ref, ord from refs")}

    def to_ord(ref):
        return ords.get(ref.replace(" ", ".").replace(":", "."))

    placements = []
    for r in accepted:
        o = to_ord(r["ref"])
        if o is None:
            sys.exit(f"unknown ref {r['ref']} — refusing to write")
        placements.append(dict(entity=r["subject"], relation=r["relation"],
                               place=r["place"], from_ord=o, from_ref=r["ref"],
                               to_ord=None, to_ref=None, source=r["source"],
                               evidence=r["evidence"], unit=r.get("unit")))

    # PROPAGATION: an entity stays where it was put until the next placement
    # that moves it. "from" rows are departures and close the previous row
    # without opening a new one.
    placements.sort(key=lambda p: (p["entity"], p["from_ord"]))
    by_ent = {}
    for p in placements:
        prev = by_ent.get(p["entity"])
        if prev is not None and prev["to_ord"] is None:
            prev["to_ord"] = p["from_ord"]
            prev["to_ref"] = p["from_ref"]
        by_ent[p["entity"]] = p if p["relation"] != "from" else None
        if p["relation"] == "from":
            p["to_ord"], p["to_ref"] = p["from_ord"], p["from_ref"]

    c.executescript(SCHEMA)
    c.executemany("""insert into placement
        (entity,relation,place,from_ord,from_ref,to_ord,to_ref,source,evidence,unit)
        values (:entity,:relation,:place,:from_ord,:from_ref,:to_ord,:to_ref,
                :source,:evidence,:unit)""", placements)
    c.commit()

    print(f"REVIEWED   : {len(rows)} rows "
          f"({sum(1 for r in rows if r['source'] == 'machine')} machine, "
          f"{sum(1 for r in rows if r['source'] == 'reading')} reading)")
    print(f"ACCEPTED   : {len(accepted)}")
    print(f"REJECTED   : {len(rows) - len(accepted)}")
    print(f"WROTE      : {len(placements)} placement rows into world.sqlite\n")

    print("THE PLACEMENT TABLE — Vayetze")
    print(f"{'entity':<10} {'rel':<5} {'place':<14} {'from':<12} {'until':<12} "
          f"{'src':<8} evidence")
    for p in sorted(placements, key=lambda x: (x["from_ord"], x["entity"])):
        print(f"{p['entity']:<10} {p['relation']:<5} {p['place'][:13]:<14} "
              f"{p['from_ref']:<12} {str(p['to_ref'] or 'still'):<12} "
              f"{p['source']:<8} {p['evidence'][:38]}")

    print("\nWHAT THE PROPAGATION BUYS — 'where is Jacob at Gen 30:25?'")
    q = """select entity, place, from_ref, coalesce(to_ref,'still') from placement
           where entity='Jacob' and relation!='from'
             and from_ord <= (select ord from refs where ref='Gen.30.25')
             and (to_ord is null
                  or to_ord > (select ord from refs where ref='Gen.30.25'))"""
    got = list(c.execute(q))
    if got:
        for e, pl, fr, to in got:
            print(f"   {e} is at {pl} — placed {fr}, holds until {to}")
        print("   (the verse itself names no place at all)")
    else:
        print("   NOTHING — the propagation failed to reach it")


main()

#!/usr/bin/env python3
"""world_port.py — THE LOOP step 7 THE LOOP THAT WAITS, part (c) THE PORT (2026-09-14; the owner: "ok go c"; the design
World/step9/THE_LOOP.md "Step 7 ... part (c) THE PORT", decisions D16 THE PORT IS A QUEUE, NEVER A PROMPT / D17 A WORLD WITH INPUTS IS
ITS OWN WORLD / D18 THE ORDER OF A PAUSE; the probes port_probes.py written first, 0/9 on the unchanged tree).

THE PORT DECIDES NOTHING ABOUT WHAT THE INPUTS ARE (the owner: "we will decide what those are later"). It is the door and the waiting:
a QUEUE FILE outside the code (World/journal/port/<queue>.yaml — `items:` a list of {id, at, label, event{kind, subject, case_source,
the fields}}), read ONCE when a session opens and validated then — an unregistered kind, an unknown field, a bad position, a position
already passed by a session starting later: REFUSED at open, named; a registered field the item lacks is a WARNING (the registry's
field list is a census of what the tape submitted, not a contract — the daemon's own read is the honest failure, at submit). At every
pause of the stepper the items DUE enter in file order through World.submit — the one door — and are journaled like any line, the EVENT
line's prov.unit 'port:<queue>' and data.port {queue, id, label}. The queue file is never rewritten: the journal records what entered.
Nothing is typed at a prompt; a program or a hand may write the file, the port cannot tell and does not care.

THE POSITION of an item: `at` null — the FIRST pause of the session (its start, or the left edge of --from); `at` a verse — that verse's
LEFT EDGE, before the tape's own line there; `at` past the tape's last verse — THE END, after the last tape line and before the seal.
"""
import os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import yaml
import world_engine as WE
import events_layer as EV

UNIVERSAL = ('kind', 'subject', 'case_source', 'label')      # the keys every event carries — not fields of a kind


class Port:
    """the queue of one session: Port(path, from_key) → .items in file order; .due(next_key, at_end) → the items entering now"""

    def __init__(self, path, from_key=None):
        self.path = path
        self.name = os.path.splitext(os.path.basename(path))[0]
        with open(path, encoding='utf-8') as f:
            doc = yaml.safe_load(f) or {}
        items = doc.get('items') if isinstance(doc, dict) else None
        if not isinstance(items, list) or not items:
            raise SystemExit('PORT REFUSED: %s holds no `items:` list' % path)
        self.items, self.warnings, seen = [], [], set()
        for k, it in enumerate(items, 1):
            if not isinstance(it, dict):
                raise SystemExit('PORT REFUSED: item %d of %s is not a mapping' % (k, self.name))
            id_ = it.get('id')
            if not id_ or id_ in seen:
                raise SystemExit('PORT REFUSED: item %d of %s has no id or a duplicate id (%r)' % (k, self.name, id_))
            seen.add(id_)
            ev = it.get('event')
            if not isinstance(ev, dict) or 'kind' not in ev or 'subject' not in ev:
                raise SystemExit('PORT REFUSED: item %r of %s has no event with a kind and a subject' % (id_, self.name))
            kind = ev['kind']
            if kind not in EV.REGISTRY:
                raise SystemExit('PORT REFUSED: item %r of %s carries an unregistered kind %r — the one door refuses it; register it in event_vocabulary.yaml with its witnesses first' % (id_, self.name, kind))
            fields = EV.REGISTRY[kind].get('fields') or []
            unknown = [f for f in ev if f not in UNIVERSAL and f not in fields]
            if unknown:
                raise SystemExit('PORT REFUSED: item %r of %s carries field(s) %s that %r does not list (the registry\'s fields: %s)' % (id_, self.name, unknown, kind, fields))
            missing = [f for f in fields if f not in ev and f != 'scenario']
            if missing:
                self.warnings.append((id_, kind, missing))
            at = it.get('at')
            key = None
            if at is not None:
                key = WE.verse_key(str(at))
                if key is None:
                    raise SystemExit('PORT REFUSED: item %r of %s is positioned at %r, which is not a verse' % (id_, self.name, at))
                if from_key is not None and key < from_key:
                    raise SystemExit('PORT REFUSED: item %r of %s is positioned at %s, already passed by a session starting later — the past is not rewritten' % (id_, self.name, at))
            self.items.append({'id': id_, 'at': None if at is None else str(at), 'key': key, 'label': it.get('label') or '', 'event': dict(ev), 'consumed': False})

    def due(self, next_key, at_end=False):
        """the items entering at this pause, in file order: unpositioned ones at the first pause; a positioned one when the next tape call
        is at or after its verse (the left edge); every remaining one at the end"""
        out = []
        for it in self.items:
            if it['consumed']:
                continue
            if it['key'] is None or at_end or (next_key is not None and next_key >= it['key']):
                it['consumed'] = True
                out.append(it)
        return out

    def event_of(self, it):
        """the event as it enters the one door: the item's event with the port's mark (the journal's prov.unit 'port:<queue>')"""
        ev = dict(it['event'])
        ev['port'] = {'queue': self.name, 'id': it['id'], 'label': it['label']}
        return ev

    @property
    def pending(self):
        return [it['id'] for it in self.items if not it['consumed']]

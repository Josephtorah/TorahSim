#!/usr/bin/env python3
# THE EVENTS LAYER (2026-09-07, D9-i — THE DAEMON CAMPAIGN's seeding sitting;
# the campaign owner-ruled 2026-09-06, "that works").
#
# The registry discipline for the OTHER side of a daemon: effects_layer.py
# refuses an unregistered effect at emission; this module refuses an
# unregistered EVENT TYPE at submission, once the daemon-edge gate (D9-ii)
# hooks it into World.submit. It loads event_vocabulary.yaml — the EVENT-TYPE
# REGISTRY harvested from the existing tape — and, run as a script, LINTS it:
#   1. coverage first (types, witness runs, narrative labels scanned);
#   2. every event type carries en / he / form / witness / ink / corpus / tape /
#      fields, its form is one of the four, and its `he` carries English beside
#      the Hebrew (the glossing law);
#   3. every WITNESS RUN is found, contiguous and consonantal, in its verse of
#      the Tanakh DB — a witness typed from memory is a guess until this passes;
#   4. every effect a consumer is recorded to write is in effect_vocabulary.yaml;
#   5. every transliterated narrative label's Hebrew is verified the same way;
#   6. no two event types share a witness run at one verse unless one names the
#      other in aliases_in_code (the one-act-two-names finding, kept explicit).
# A report of zero is worth only the coverage line above it. Exit 1 on any flag.
# Model layer; read-only over the corpus and the registries; touches no unit.

import os
import re
import sqlite3
import sys
import yaml

HERE = os.path.dirname(os.path.abspath(__file__))
_REG_PATH = os.path.join(HERE, 'event_vocabulary.yaml')
_FX_PATH = os.path.join(HERE, 'effect_vocabulary.yaml')
DB = '<repo-old>/elijah_docket/tanakh.sqlite'
FORMS = ('act', 'speech', 'statute', 'case')
FIELDS = ('en', 'he', 'form', 'witness', 'ink', 'corpus', 'tape', 'fields')
HEB = re.compile(r'[֐-׿]')

with open(_REG_PATH, encoding='utf-8') as _f:
    _doc = yaml.safe_load(_f)
REGISTRY = _doc['events']
NARRATIVE = _doc.get('narrative_verbs', {})


def validate(kinds):
    """Every submitted event kind must be a registered type — or the tape refuses."""
    for k in kinds:
        if k not in REGISTRY:
            raise SystemExit(
                'EVENT-TYPE REGISTRY: %r is not in event_vocabulary.yaml — an '
                'unregistered event type may not be submitted. Register it with '
                'its ink / corpus / tape witnesses first.' % k)
    return kinds


def consumers(kind):
    """The daemons the registry records as consuming a type (from its tape line)."""
    tape = REGISTRY[kind].get('tape', '')
    m = re.search(r'consumed by (.*)$', tape)
    return [] if not m or m.group(1).startswith('NO DAEMON') else re.findall(r'(law_[a-z_0-9]+)', m.group(1))


def _strip(s):
    return ''.join(c for c in s if c != '/' and not (0x0591 <= ord(c) <= 0x05C7))


def _verse(db, ref):
    b, cv = ref.split(' ')
    ch, v = cv.split(':')
    rows = db.execute("SELECT w.he FROM words w JOIN verses v ON w.verse_id=v.id "
                      "WHERE v.book=? AND v.chapter=? AND v.verse=? ORDER BY w.idx",
                      (b, int(ch), int(v))).fetchall()
    return [_strip(r[0]) for r in rows]


def _run_in_verse(db, witness):
    ref, run = [x.strip() for x in witness.split('|', 1)]
    cons = _verse(db, ref)
    want = run.split()
    return any(cons[i:i + len(want)] == want for i in range(len(cons) - len(want) + 1)), ref, run


def lint(verbose=True):
    flags = []
    db = sqlite3.connect('file:%s?mode=ro' % DB, uri=True)
    with open(_FX_PATH, encoding='utf-8') as f:
        fx = yaml.safe_load(f)['effects']
    n_wit = 0
    seen_runs = {}
    for k, e in REGISTRY.items():
        for fld in FIELDS:
            if fld not in e:
                flags.append('%s: missing field %s' % (k, fld))
        if e.get('form') not in FORMS:
            flags.append('%s: form %r not in %s' % (k, e.get('form'), FORMS))
        he = e.get('he', '')
        if not HEB.search(he):
            flags.append('%s: he carries no Hebrew' % k)
        for chunk in he.split(';'):
            if HEB.search(chunk) and not re.search(r'\(.*[A-Za-z].*—',chunk):
                flags.append('%s: he chunk without English beside the Hebrew: %r' % (k, chunk[:60]))
        for w in e.get('witness', []):
            ok, ref, run = _run_in_verse(db, w)
            n_wit += 1
            if not ok:
                flags.append('%s: witness run NOT IN VERSE %s: %r' % (k, ref, run))
            key = (ref, run)
            if key in seen_runs and seen_runs[key] != k:
                other = seen_runs[key]
                named = (other in (e.get('aliases_in_code') or '')) or (k in (REGISTRY[other].get('aliases_in_code') or ''))
                if not named:
                    flags.append('%s and %s share the witness %s %r with no aliases_in_code naming the pair' % (k, other, ref, run))
            seen_runs.setdefault(key, k)
        for eff in re.findall(r'-> ([a-z_, ]+?)(?:;|$)', e.get('tape', '')):
            for one in [x.strip() for x in eff.split(',')]:
                if one and one != 'no ledger write' and one not in fx:
                    flags.append('%s: consumer writes unregistered effect %r' % (k, one))
    n_narr, n_trans = 0, 0
    for k, e in NARRATIVE.items():
        n_narr += 1
        if 'he' in e:
            n_trans += 1
            if not re.search(r'\(.*[A-Za-z].*—',e['he']):
                flags.append('narrative %s: he without English beside the Hebrew' % k)
            for w in e.get('witness', []):
                ok, ref, run = _run_in_verse(db, w)
                if not ok:
                    flags.append('narrative %s: witness run NOT IN VERSE %s: %r' % (k, ref, run))
    if verbose:
        print('events_layer lint: %d event types scanned (%d witness runs checked against %s), %d narrative labels (%d transliterations verified); forms: %s'
              % (len(REGISTRY), n_wit, os.path.basename(DB), n_narr, n_trans,
                 ', '.join('%s %d' % (f, sum(1 for e in REGISTRY.values() if e.get('form') == f)) for f in FORMS)))
        assert REGISTRY and n_wit, 'ZERO-REPORT: nothing scanned'
        for fl in flags:
            print('  FLAG  ' + fl)
        print('events_layer lint: %d flag(s)' % len(flags))
    return flags


if __name__ == '__main__':
    sys.exit(1 if lint() else 0)

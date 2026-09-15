import os as _os
_ROOT = _os.path.normpath(_os.path.join(_os.path.dirname(_os.path.abspath(__file__)), '..', '..'))   # THE PORTABLE REPO (2026-09-15): the repo root from this file's own place
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
#      other in aliases_in_code (the one-act-two-names finding, kept explicit);
#   7. THE LINK REVIEW LAW (owner-ruled 2026-09-07; sitting LR1): a type whose
#      witnesses sit in MORE THAN ONE CHAPTER is a link the machine's shape made
#      and carries `link:` — reference (verified: the seats share a CONTENT
#      lemma — noun, verb, or adjective — in the Tanakh DB), transfer (refused
#      without `taught_by:` naming a teacher), hypothesis (an untaught transfer,
#      kept and labeled), UNCLASSIFIED (asked, unanswered — counted, printed);
#      a multi-seat type without the field is a flag. The rule behind it: a
#      person does not derive a verbal analogy on his own (Pesachim 66a:12,
#      Niddah 19b:12; logic/MIDDOT.md under I2).
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
DB = (_ROOT + '/Data/tanakh.sqlite')
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


# ---- rule 7: the link field on a multi-seat type ----
LINKS = ('reference', 'transfer', 'hypothesis', 'UNCLASSIFIED')
_TAUGHT = re.compile(r'\b(Mishnah|Tosefta|Sifra|Sifrei|Mekhilta|Rabbah|Tanchuma|Onkelos|Talmud|Yerushalmi)\b|\b[A-Z][a-z]+ \d{1,3}[ab]:\d{1,3}\b')
_MOVE = re.compile(r'\bM-\d\d\b')
_NAMES = {'3068', '3069'}   # the divine name is not a content link


def taught_ok(s):
    if not s or not str(s).strip(): return False
    s = str(s)
    return bool(_TAUGHT.search(s) or (_MOVE.search(s) and re.search(r'exemplar', s, re.I) and re.search(r'\d+:\d+', s)))


def _content_lemmas(db, witness):
    """The content lemmas (noun / verb / adjective) of a witness run — the tokens a REFERENCE may share."""
    ref, run = [x.strip() for x in witness.split('|', 1)]
    b, cv = ref.split(' '); ch, v = cv.split(':')
    rows = db.execute("SELECT w.he, w.lemma, w.morph FROM words w JOIN verses v ON w.verse_id=v.id "
                      "WHERE v.book=? AND v.chapter=? AND v.verse=? ORDER BY w.idx", (b, int(ch), int(v))).fetchall()
    cons = [_strip(r[0]) for r in rows]; want = run.split()
    out = set()
    for i in range(len(cons) - len(want) + 1):
        if cons[i:i + len(want)] != want: continue
        for he, lemma, morph in rows[i:i + len(want)]:
            if not lemma or not morph: continue
            # the morph's segments: the first carries the language letter ('HNcmsc' -> N), the rest a prefix or a
            # SUFFIX ('Sp2ms'); the content word is the first segment whose part of speech is noun / verb / adjective
            # (LR2 fix: the last segment is the pronominal suffix on 'your name', 'its harvest', 'his fistful')
            segs = morph.split('/')
            poss = [(segs[0][1] if len(segs[0]) > 1 else '')] + [s[0] if s else '' for s in segs[1:]]
            pos = next((p for p in poss if p in 'NVA'), '')
            lem = next((x.strip() for x in lemma.split('/') if re.search(r'\d', x)), '')
            if pos and lem and lem.split()[0] not in _NAMES: out.add(lem)
        break
    return out


def link_flags(k, e, db):
    """Rule 7 on one registry entry; returns (flags, seats) — seats = chapters the witnesses sit in."""
    flags = []
    by_ch = {}
    for w in e.get('witness', []):
        ch = w.split('|')[0].strip().rsplit(':', 1)[0]
        by_ch.setdefault(ch, []).append(w)
    if len(by_ch) < 2: return flags, by_ch
    lk = e.get('link')
    if lk is None:
        flags.append('%s: MULTI-SEAT (%s) with no link field — THE TWO QUESTIONS (reference / transfer / hypothesis / UNCLASSIFIED; the link review law)' % (k, ', '.join(sorted(by_ch))))
    elif lk not in LINKS:
        flags.append('%s: unknown link %r' % (k, lk))
    elif lk == 'transfer' and not taught_ok(e.get('taught_by')):
        flags.append('%s: link transfer WITHOUT A TEACHER (taught_by must name a sugya, a Mishnah/Tosefta/Sifra/Sifrei/Mekhilta passage, or a move M-nn with its exemplar)' % k)
    elif lk == 'reference':
        lem = {ch: set().union(*(_content_lemmas(db, w) for w in ws)) for ch, ws in by_ch.items()}
        for ch in lem:
            others = set().union(*(lem[o] for o in lem if o != ch))
            if not lem[ch] & others:
                if e.get('reference_by'):
                    # a DECLARED ground where the lemma test cannot see the reference (one case paragraph whose verb and
                    # noun carry different lemma numbers) — accepted, counted apart, printed by the census as 'declared'
                    continue
                flags.append('%s: link reference but the seat %s shares NO content lemma with the other seats (%s) — a reference names one institution in one word; else transfer or hypothesis, or state the ground in reference_by' % (k, ch, ', '.join(sorted(o for o in lem if o != ch))))
    return flags, by_ch


def lint(verbose=True):
    flags = []
    db = sqlite3.connect('file:%s?mode=ro' % DB, uri=True)
    with open(_FX_PATH, encoding='utf-8') as f:
        fx = yaml.safe_load(f)['effects']
    n_wit = 0
    seen_runs = {}
    n_multi, link_census = 0, {}
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
        lf, seats = link_flags(k, e, db)
        flags.extend(lf)
        if len(seats) > 1:
            n_multi += 1
            lab = e.get('link', 'MISSING')
            if lab == 'reference' and e.get('reference_by'): lab = 'reference (declared ground)'
            link_census[lab] = link_census.get(lab, 0) + 1
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
        print('events_layer LINK CENSUS (rule 7): %d multi-seat types — %s' % (
            n_multi, ', '.join('%s %d' % (kk, link_census[kk]) for kk in LINKS + ('reference (declared ground)', 'MISSING') if link_census.get(kk)) or 'none'))
        for fl in flags:
            print('  FLAG  ' + fl)
        print('events_layer lint: %d flag(s)' % len(flags))
    return flags


if __name__ == '__main__':
    sys.exit(1 if lint() else 0)

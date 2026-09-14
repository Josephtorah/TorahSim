#!/usr/bin/env python3
"""o8_census.py — O8 THE NARRATIVE GAPS ON THE ENGINE: THE CENSUS BY SCRIPT (2026-09-08; the plan: the state doc's
compaction point #90/#97). Every Genesis (98) and Exodus (66) unit in logic/units — its verse range from meta.refs, its
genre and status — against (1) the sequential tape's events and markers (cold_run_sequence.py's sentinel section, the
case_source verses of every literal submit and the verse of every marker), (2) the corpus world's 557 narrative events
(corpus_world.sqlite, read-only), (3) the entity registry's step9-scenes members. Prints, per unit: verses, tape
events, tape markers, corpus events; then the UNCOVERED units (no tape event and no marker) grouped into contiguous
stretches, by genre. Computed, never recited."""
import re, os, sys, glob, sqlite3, collections
import yaml
ROOT = '<repo-old>'
SEQ = os.path.join(ROOT, 'World/step9/cold_run_sequence.py')
BOOK = {'Genesis': 'Gen', 'Exodus': 'Exod', 'Leviticus': 'Lev'}
BO = {'Gen': 1, 'Exod': 2, 'Lev': 3}
tdb = sqlite3.connect('file:%s/elijah_docket/tanakh.sqlite?mode=ro' % ROOT, uri=True)
NV = {}   # (book, ch) -> verse count
for b, c, n in tdb.execute("select book, chapter, count(*) from verses where book in ('Gen','Exod','Lev') group by book, chapter"):
    NV[(b, c)] = n


def expand(book, refs):
    """'2:4-3:24' | '17:1-27' | '1:1' | '32:25-33' | '9:1-17' -> the list of (book, ch, vs)"""
    refs = refs.strip()
    m = re.match(r'^(\d+):(\d+)(?:-(?:(\d+):)?(\d+))?$', refs)
    assert m, refs
    c1, v1 = int(m.group(1)), int(m.group(2))
    c2 = int(m.group(3)) if m.group(3) else c1
    v2 = int(m.group(4)) if m.group(4) else v1
    out = []
    for c in range(c1, c2 + 1):
        a = v1 if c == c1 else 1
        z = v2 if c == c2 else NV[(book, c)]
        out += [(book, c, v) for v in range(a, z + 1)]
    return out


# ---- 1. THE UNITS ----
units = []
for f in sorted(glob.glob(os.path.join(ROOT, 'logic/units/gen_*.yaml')) + glob.glob(os.path.join(ROOT, 'logic/units/exo_*.yaml'))):
    d = yaml.safe_load(open(f, encoding='utf-8'))
    m = d['meta']
    book = BOOK[m['book_en']]
    refs = str(m['refs'])
    try:
        vv = expand(book, refs)
    except AssertionError:
        vv = []
    units.append({'id': m['id'], 'book': book, 'refs': refs, 'genre': m.get('genre', '?'), 'status': m.get('status', '?'),
                  'verses': vv, 'has_claims': bool(d.get('scenarios')), 'steps': len(d.get('boot_steps') or [])})
bad = [u['id'] + ' ' + u['refs'] for u in units if not u['verses']]
print('UNITS %d (gen %d, exo %d); unparsed refs: %s' % (len(units), sum(u['book'] == 'Gen' for u in units), sum(u['book'] == 'Exod' for u in units), bad))
print('  by genre:', collections.Counter(u['genre'] for u in units).most_common())
print('  by status:', collections.Counter(u['status'] for u in units).most_common())

# ---- 2. THE TAPE ----
src = open(SEQ, encoding='utf-8').read()
tape = src.split('# ==== TAPE BEGIN')[1].split('# ==== TAPE END')[0]
VREF = re.compile(r"'case_source':\s*'((?:Gen|Exod|Lev)[^']*)'")
MREF = re.compile(r"w\.marker\('((?:Gen|Exod|Lev)\s+\d+:\d+)'")
KIND = re.compile(r"'kind':\s*'([a-z0-9_]+)'")
SUBJ = re.compile(r"'subject':\s*'([^']+)'")
RANGE = re.compile(r'(Gen|Exod|Lev)\s+(\d+):(\d+)(?:-(\d+))?')
tape_events = []   # (book, ch, vs, kind, subject, full source)
tape_markers = []
for line in tape.split('\n'):
    if 'w.submit(' in line:
        cs = VREF.search(line); k = KIND.search(line); s = SUBJ.search(line)
        if cs:
            m = RANGE.match(cs.group(1))
            tape_events.append((m.group(1), int(m.group(2)), int(m.group(3)), k.group(1) if k else '?', s.group(1) if s else '?', cs.group(1)))
    for m in MREF.finditer(line):
        mm = RANGE.match(m.group(1))
        tape_markers.append((mm.group(1), int(mm.group(2)), int(mm.group(3))))
print('TAPE: %d events, %d markers' % (len(tape_events), len(tape_markers)))
ev_by_verse = collections.defaultdict(list)
for e in tape_events:
    ev_by_verse[e[:3]].append(e)
mk_by_verse = collections.Counter(tape_markers)

# ---- 3. THE CORPUS WORLD ----
cdb = sqlite3.connect('file:%s/corpus_world.sqlite?mode=ro' % ROOT, uri=True)
corpus = collections.defaultdict(list)
corpus_by_unit = collections.Counter()
for seq, unit, ref, verb, agent, themes in cdb.execute('select seq, unit, ref, verb, agent, themes from events'):
    m = re.match(r'^(Gen|Exod|Lev)\.(\d+)\.(\d+)', ref)
    if m:
        corpus[(m.group(1), int(m.group(2)), int(m.group(3)))].append((unit, verb, agent))
    corpus_by_unit[unit] += 1
print('CORPUS WORLD: %d events on %d verses, %d units' % (sum(len(v) for v in corpus.values()), len(corpus), len(corpus_by_unit)))

# ---- 4. THE REGISTRY ----
reg = yaml.safe_load(open(os.path.join(ROOT, 'logic/corpus/entity_registry.yaml'), encoding='utf-8'))
scene_tokens = {}
for ent in reg['entities']:
    for mem in ent.get('members') or []:
        if 'step9-scenes' in (mem.get('units') or []):
            scene_tokens[mem['token']] = ent['id']
print('REGISTRY: %d entities; %d step9-scene tokens' % (len(reg['entities']), len(scene_tokens)))

# ---- 5. THE CENSUS PER UNIT ----
print('\nPER UNIT: id | refs | genre | status | verses | tape events (kinds) | markers | corpus events')
rows = []
for u in units:
    vs = set(u['verses'])
    te = [e for v in u['verses'] for e in ev_by_verse.get(v, [])]
    mk = sum(mk_by_verse.get(v, 0) for v in u['verses'])
    ce = sum(len(corpus.get(v, [])) for v in u['verses'])
    u.update(tape=len(te), kinds=sorted(set(e[3] for e in te)), markers=mk, corpus=ce)
    rows.append(u)
    flag = '' if (te or mk) else '   <-- UNCOVERED'
    print('  %-42s %-12s %-16s %-8s %3d  tape %2d %-40s mk %2d  corpus %2d%s' % (u['id'], u['refs'], u['genre'], u['status'], len(vs), len(te), ','.join(u['kinds'])[:40], mk, ce, flag))

# ---- 5b. THE CORPUS WORLD'S DEMANDS (the narrative world's own obligation ledger) per unit ----
dem_by_unit = collections.Counter(); dem_open = collections.Counter()
for unit, status in cdb.execute('select unit, status from demands'):
    dem_by_unit[unit] += 1
    if status != 'settled': dem_open[unit] += 1
for u in rows:
    u['demands'] = dem_by_unit.get(u['id'], 0); u['demands_open'] = dem_open.get(u['id'], 0)

# ---- 6. THE UNCOVERED FROZEN UNITS (no tape EVENT), by book, as contiguous stretches; markers-only named apart ----
def _next(v):
    b, c, n = v
    return (b, c, n + 1) if n < NV[(b, c)] else (b, c + 1, 1)
print('\nUNCOVERED FROZEN UNITS (no tape event; the drafts are the old tree-derived duplicates, counted apart), by book:')
frozen = [u for u in rows if u['status'] == 'frozen']
print('  frozen %d of %d (gen %d, exo %d); drafts %d' % (len(frozen), len(rows), sum(u['book'] == 'Gen' for u in frozen), sum(u['book'] == 'Exod' for u in frozen), len(rows) - len(frozen)))
LAW_GENRES = ('decision_table', 'boot_steps', 'decalogue_statute_code', 'casuistic_law_code')
for book in ('Gen', 'Exod'):
    bu = [u for u in frozen if u['book'] == book and not u['tape']]
    law = [u for u in bu if u['genre'] in LAW_GENRES]
    narr = [u for u in bu if u['genre'] not in LAW_GENRES]
    mk_only = [u for u in narr if u['markers']]
    print('  %s: %d frozen units with no tape event = %d narrative-register + %d law/spec-register (%s)' % (book, len(bu), len(narr), len(law), ', '.join(u['id'] for u in law)))
    print('     markers-only (the clock stamps ride, no act): %d — %s' % (len(mk_only), ', '.join('%s(%d)' % (u['id'], u['markers']) for u in mk_only)))
    narr.sort(key=lambda u: u['verses'][0])
    stretches = []
    for u in narr:
        a, z = u['verses'][0], u['verses'][-1]
        if stretches and a <= _next(stretches[-1]['z']):
            stretches[-1]['units'].append(u); stretches[-1]['z'] = max(stretches[-1]['z'], z)
        else:
            stretches.append({'a': a, 'z': z, 'units': [u]})
    print('     contiguous stretches of the narrative-register units:')
    for s in stretches:
        nverses = len({v for u in s['units'] for v in u['verses']})
        corpus_n = sum(u['corpus'] for u in s['units']); dem = sum(u['demands'] for u in s['units']); mk = sum(u['markers'] for u in s['units'])
        print('       %s %d:%d - %d:%d  %2d units  %3d verses  corpus events %3d  demands %3d  markers %2d  [%s]' % (book, s['a'][1], s['a'][2], s['z'][1], s['z'][2], len(s['units']), nverses, corpus_n, dem, mk, ', '.join(u['id'] for u in s['units'])))
    tot_v = len({v for u in narr for v in u['verses']})
    print('     TOTAL narrative-register frozen units with no tape event: %d units, %d verses, %d corpus events, %d demands' % (len(narr), tot_v, sum(u['corpus'] for u in narr), sum(u['demands'] for u in narr)))

# ---- 7. THE COVERED — by which runner's kinds (for the record) ----
print('\nCOVERED units and the tape kinds on them:')
for u in rows:
    if u['tape'] or u['markers']:
        print('  %-42s %-12s tape %2d mk %2d  %s' % (u['id'], u['refs'], u['tape'], u['markers'], ','.join(u['kinds'])))

# ---- 8. THE TAPE'S OWN VERSE COVERAGE — chapters of the three books with events/markers ----
print('\nTAPE VERSES BY CHAPTER (events+markers):')
ch = collections.Counter()
for e in tape_events: ch[(e[0], e[1])] += 1
for m in tape_markers: ch[(m[0], m[1])] += 1
print('  ', sorted(ch.items(), key=lambda kv: (BO[kv[0][0]], kv[0][1])))

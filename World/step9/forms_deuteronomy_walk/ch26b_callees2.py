import os as _os
_ROOT = _os.path.normpath(_os.path.join(_os.path.dirname(_os.path.abspath(__file__)), '..', '..', '..'))   # THE PORTABLE REPO (2026-09-15): the repo root from this file's own place
#!/usr/bin/env python3
# THE DEUTERONOMY WALK 18b (2026-09-26): THE Q-STYLE CALLEES printed before any assert is typed — the cells whose keys the first pass could not read (no `if ask ==` form):
# the signature and the keys READ FROM EACH SOURCE by regex, every key called, the value printed by repr (cut). RUN FROM THE REPO ROOT.
import os, sys, io, re, contextlib, subprocess, inspect
ROOT = _ROOT; sys.path.insert(0, ROOT + '/World/step9')
def load(n):
    with contextlib.redirect_stdout(io.StringIO()): return __import__('cold_run_' + n)
def keys_of(src):
    ks = re.findall(r"(?:==|in \() ?'([a-z_0-9]+)'", src); ks += re.findall(r"^\s{4,12}'([a-z_0-9]+)':\s", src, re.M)
    seen = []; [seen.append(x) for x in ks if x not in seen]; return seen
def probe(n, name, calls=None, show_src=0):
    try: M = load(n)
    except Exception as ex: print('LOAD FAIL', n, repr(ex)[:200]); return
    fn = getattr(M, name, None)
    if fn is None: print('NO CELL %s.%s (defs %s)' % (n, name, [f for f in dir(M) if callable(getattr(M, f)) and not f.startswith('_')][:50])); return
    src = inspect.getsource(fn); ks = keys_of(src)
    print('CELL %s.%s%s keys %s' % (n, name, inspect.signature(fn), ks[:40]))
    if show_src: print('   SRC:', ' | '.join(l.strip()[:110] for l in src.split('\n')[:show_src]))
    D = getattr(M, 'DATA', {})
    for c in (calls if calls is not None else [(k,) for k in ks[:24]]):
        for attempt in (lambda: fn(*c), lambda: fn({'ask': c[0]}, D), lambda: fn(c[0], D)):
            try:
                v = attempt(); print('  FACT %s.%s%r = %s' % (n, name, c, repr(v)[:330])); break
            except Exception as ex: err = '%s: %s' % (type(ex).__name__, str(ex)[:120])
        else: print('  FAIL %s.%s%r: %s' % (n, name, c, err))
probe('sanctions', 'grade'); probe('sanctions', 'curser'); probe('sanctions', 'unions_misc')
probe('mishpatim_3', 'parent_curser'); probe('mishpatim_3', 'killer')
probe('holiness', 'conduct', calls=[('stumbling',), ('stumbling', {'kind': 'blind'}), ('cursing_the_deaf',)], show_src=6)
probe('decalogue', 'altar_rules', calls=[('hewn_stones',), ('build_recipe',), ('steps',), ('earth_altar',)])
probe('ordinances', 'land'); probe('ordinances', 'courts', calls=[('enemy_ox',), ('straying',)])
probe('tochacha', 'covenant', calls=[(True, True, True), (False, False, False), (True, False, True)]); probe('tochacha', 'cascade', calls=[(1,), (2,), (3,), (4,), (5,), (0,)]); probe('tochacha', 'measures', calls=[()])
probe('calendar', 'first_fruits', calls=[({'ask': 'first'}, {}), ({'species': 'wheat'}, {})], show_src=8)
probe('chatat', 'share', calls=[('onen',), ('mourner',)], show_src=4)
probe('priesthood', 'holy_food', show_src=6); probe('joseph', 'seventy', calls=[()], show_src=4)
probe('exodus_story', 'sinai', show_src=6); probe('exodus_story', 'plagues', show_src=4)
probe('sanctuary_build', 'altar', show_src=5)
probe('primeval', 'call', show_src=5); probe('primeval', 'scene', calls=[])
probe('opening_speech', 'lemma_seats', calls=[('באר',), ('בָּאֵר',)], show_src=4)
probe('journeys', 'the_command', show_src=3); probe('journeys', 'lemma_seats', calls=[('פסל',)])
probe('hear_o_israel', 'the_creed', show_src=3); probe('hear_o_israel', 'the_header', calls=[])
probe('good_land', 'receipt_seats', calls=[(26,), (27,), (28,)]); probe('good_land', 'narrative', calls=[])
probe('borders', 'the_roster', show_src=4)
probe('naso', 'blessing', calls=[('language',), ('form', {'place': 'temple'}), ('who_blesses', {'who': 'priest'})])
print('CALLEES2 DONE')

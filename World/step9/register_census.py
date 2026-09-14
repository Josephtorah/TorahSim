#!/usr/bin/env python3
"""register_census.py — THE REGISTER GATE (2026-09-11; THE_LOOP.md "THE REGISTER GATE — the design"; ARCHITECTURE/DATABASE_SPECULATION.md
section 4). The text writes its own test oracle: footers carrying checksums, receipts closing commands, footers stamping law blocks, headers
opening registers. This gate reads those formulas OFF THE TANAKH DB (the lemma column; the numerals by the step-9 parser) and checks what the
engine already holds — the population table, the ledger, the installation registry. It adds no table, no row, no column.

THE FOUR CENSUSES (every seat classed by the world; GREEN needs nothing, every other class needs a declared why):
  A. THE COUNT LINES  a line with a count-noun ("the counted" 6485, "the number" 4557, "souls" 5315) or a register footer with a numeral;
                      each numeral classed by THE UNIT RULE (a numeral run followed within two tokens by a unit noun — year, day, month,
                      gerah, talent, shekel, city, man — is a MEASURE, else a COUNT); a count is ROW (a counted row with that count in the
                      line's chapter), LEDGER (a `counted` status with that value), ELSEWHERE (the number at another chapter), NONE.
                      GREEN: ROW, LEDGER, MEASURE-ONLY.
  B. THE RECEIPTS     "as the LORD commanded" (k/834 + 6680 + 3068): CLOSE (a ledger entry closed at the verse), ACT (a write at the verse,
                      nothing closed), EVENT (an event at the verse, nothing written), CHAPTER (a close in the chapter), NONE. GREEN: CLOSE.
  C. THE FOOTERS      "these are the statutes / commandments / judgments / words / testimonies": HEADER (a second-person imperfect verb) or
                      FOOTER; the block by the neighbouring lines; the STAMP the place word on the line (sinai / moab / jordan / none);
                      DAEMONS (a daemon's given_at inside the block) or EMPTY. GREEN: DAEMONS.
  D. THE REGISTERS    the "these are + generations / names / sons / families / the counted" headers grouped by chapter: ROWS (table rows
                      whose as_of is in that chapter) or NONE. GREEN: ROWS.
THE DISPOSITIONS (register_dispositions.yaml — counts / receipts / footers / registers, each {class, why}): a declared class that differs
from the computed one is a LIE (fail); a declaration on a seat the world has paid is STALE (fail); an undeclared non-green seat is DEBT —
printed, exit 0 — until --strict. --emit prints yaml stubs for the undeclared seats (the why typed from the reading, never generated).
Writes REGISTER_INDEX.md each run (documentation, never runtime).

Run from the repo root: python3 World/step9/register_census.py [--strict] [--emit] [--no-index]      (the running world built, ~90 s)
"""
import collections, contextlib, io, os, re, sqlite3, sys
import yaml

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(HERE))
sys.path.insert(0, HERE)
DB = os.path.join(ROOT, 'elijah_docket', 'tanakh.sqlite')
YAML = os.path.join(HERE, 'register_dispositions.yaml')
DISP = os.path.join(HERE, 'daemon_dispositions.yaml')
INDEX = os.path.join(HERE, 'REGISTER_INDEX.md')
TORAH = ['Gen', 'Exod', 'Lev', 'Num', 'Deut']
COUNT_NOUNS = {'6485': 'the counted', '4557': 'the number', '5315': 'souls'}
REGISTER_NOUNS = {'8435': 'generations', '8034': 'names', '1121': 'sons', '4940': 'families', '6485': 'the counted'}
FOOTER_NOUNS = {'2706': 'statutes', '4687': 'commandments', '4941': 'judgments', '1697': 'words', '5713': 'testimonies'}
UNIT_NOUNS = {'8141': 'year', '3117': 'day', '2320': 'month', '1626': 'gerah', '3603': 'talent', '8255': 'shekel', '5892': 'city', '376': 'man'}
STAMPS = (('5514', 'sinai'), ('4124', 'moab'), ('3383', 'jordan'))
NUMY = re.compile(r'(אחד|אחת|שנים|שתים|שני|שתי|שלש|שלוש|ארבע|חמש|שש|שבע|שמנ|תשע|עשר|מאה|מאת|מאות|אלף|אלפ|מאתים)')
GREEN = {'counts': {'ROW', 'LEDGER', 'MEASURE-ONLY'}, 'receipts': {'CLOSE'}, 'footers': {'DAEMONS'}, 'registers': {'ROWS'}}
SECTIONS = ('counts', 'receipts', 'footers', 'registers')
TALLIES = {}


# ---------------------------------------------------------------- the ink ----------------------------------------------------------------
def ref(k): return '%s %d:%d' % k
def pos(k): return (TORAH.index(k[0]), k[1], k[2])
def plain(x): return ''.join(ch for ch in x if ch != '/' and not (0x0591 <= ord(ch) <= 0x05C7))
def base(lm): return lm.split('/')[-1].split(' ')[0]


class Ink:
    """the Torah's tokens off the DB in canonical order (the DB's ids run alphabetically by book) and the parser"""
    def __init__(self):
        with contextlib.redirect_stdout(io.StringIO()):
            import cold_run_sequence as CS
        self.CS = CS
        db = sqlite3.connect('file:%s?mode=ro' % DB, uri=True)
        rows = db.execute("SELECT v.book, v.chapter, v.verse, w.idx, w.he, w.lemma, w.morph FROM words w JOIN verses v ON w.verse_id=v.id "
                          "WHERE v.book IN ('Gen','Exod','Lev','Num','Deut') ORDER BY v.id, w.idx").fetchall()
        V0 = {}
        for b, c, v, i, he, lm, m in rows:
            V0.setdefault((b, c, v), []).append((plain(he), base(lm), lm, m))
        self.keys = sorted(V0, key=pos)
        self.V = collections.OrderedDict((k, V0[k]) for k in self.keys)

    def numbers(self, k):
        return [n for n in self.CS.ink_numbers(self.CS.verse_words(*k)) if isinstance(n, int)]


def read_ink(): return Ink()


PREFIXES = ('', 'ו', 'ב', 'ל', 'כ', 'מ', 'ה', 'וב', 'ול', 'וכ', 'ומ', 'וה', 'בה', 'לה', 'כה')
DUAL_MEASURES = {'שנתים', 'יומים', 'אמתים', 'פעמים'}      # the numeral two with its unit inside the token ("two years", "two days", "two cubits", "twice")


def is_numeral(tok, units):
    """a verse_words token the parser counts: its own markers decide — a star is a homograph the points refused (not a numeral), a percent
    sign a fraction (the parser's Fraction values are not counts here), an at sign the unit noun as one; the bare word, under the parser's
    prefixes, in UNITS; a hash or caret or tilde form as its own key"""
    if tok.endswith('*') or tok.endswith('%'): return False
    t = tok.rstrip('|')
    if t.endswith('@'): return True
    marker = t[-1] if t and t[-1] in '#~^' else ''
    core = t[:-1] if marker else t
    for p in PREFIXES:
        if core.startswith(p) and len(core) > len(p):
            c = core[len(p):]
            if (c + marker) in units or (not marker and c in units): return True
    return False


def numeral_runs(vw, units):
    """maximal runs of the parser's numeral tokens: [(start, end, dual_measure)]"""
    runs, i = [], 0
    while i < len(vw):
        if is_numeral(vw[i], units):
            j = i
            while j < len(vw) and is_numeral(vw[j], units): j += 1
            dual = any(vw[x].rstrip('|~').lstrip('ובלכמה') in DUAL_MEASURES or (vw[x].endswith('~') and vw[x].rstrip('|~').lstrip('ובלכמה') != 'אלפים') or vw[x].endswith('@') for x in range(i, j))   # THE NUMBERS WALK 15b (2026-09-13): the parser's RULE 29 marks the bare dual THOUSAND (אַלְפַּיִם 'two thousand') with the same tilde the dual MEASURES wear — a NUMBER's dual (a count: Num 4:36's 2,750 Kohathites, 4:40's 2,630 Gershonites), never a unit inside the token; the gate fired STALE on both count lines the day the rule was taught and the test learned the difference
            runs.append((i, j, dual)); i = j
        else:
            i += 1
    return runs


def unit_after(ws, j):
    """the unit noun within two tokens after a run's end (the DB's lemmas, aligned with the parser's tokens), or None"""
    for t in ws[j:j + 2]:
        if t[1] in UNIT_NOUNS: return UNIT_NOUNS[t[1]]
    return None


def count_lines(ink):
    """A. every count line: [(key, {'noun', 'counts', 'measures', 'unpaired', 'values'})] — a numeral is a MEASURE when a unit noun follows
    it within two tokens, when its unit sits inside the token (the duals), or when it is ONE (a register's checksum is never one: "one soul",
    "one man for his father's house", "on the first of the month"); the rest are COUNTS"""
    out = []
    units = ink.CS.UNITS
    for k in ink.keys:
        ws = ink.V[k]; bl = [t[1] for t in ws]
        noun = next((COUNT_NOUNS[b] for b in bl if b in COUNT_NOUNS), None)
        footer = bool(ws) and ws[0][1] == '428' and len(ws) > 1 and ws[1][1] in REGISTER_NOUNS
        if noun is None and not footer: continue
        vals = ink.numbers(k)
        if not vals: continue
        vw = ink.CS.verse_words(*k)
        runs = numeral_runs(vw, units) if len(vw) == len(ws) else []
        counts, measures, unpaired = [], [], False
        if len(runs) == len(vals):
            for (i, j, dual), v in zip(runs, vals):
                (measures if (v == 1 or dual or unit_after(ws, j)) else counts).append(v)
        else:
            unpaired = True; counts = [v for v in vals if v != 1]; measures = [v for v in vals if v == 1]
        out.append((k, {'noun': noun or ('footer: these are the %s of' % REGISTER_NOUNS[ws[1][1]]), 'counts': counts, 'measures': measures, 'unpaired': unpaired, 'values': vals, 'runs': len(runs)}))
    return out


def receipts(ink):
    """B. the receipt lines: as (k/834) commanded (6680) the LORD (3068 within three); THE SECOND FORM (THE NUMBERS WALK sitting 10b,
    2026-09-12; NUMBERS_WALK.md "Sitting 10b"): according to ALL (k/3605) that (834) commanded (6680) the LORD (3068) — eleven Torah seats
    (Gen 7:5; Exod 39:32, 39:42, 40:16; Num 1:54, 2:34, 8:20, 9:5, 30:1; Deut 1:3, 1:41), Num 30:1 the one whose first word is a speech
    verb — the 9b debt (v)'s class of one, measured at the vows' reading"""
    out = []
    for k in ink.keys:
        s = [t[2] for t in ink.V[k]]
        for i, lm in enumerate(s):
            if lm.startswith('k/834') and i + 1 < len(s) and s[i + 1].startswith('6680') and any(x.startswith('3068') for x in s[i + 2:i + 5]):
                out.append(k); break
            if lm.startswith('k/3605') and i + 3 < len(s) and s[i + 1].startswith('834') and s[i + 2].startswith('6680') and s[i + 3].startswith('3068'):
                out.append(k); break
    return out


def footers(ink):
    """C. the nine lines: [(key, {'noun', 'kind', 'stamp'})] — HEADER by a second-person imperfect verb, else FOOTER"""
    out = []
    for k in ink.keys:
        ws = ink.V[k]
        if ws and ws[0][1] == '428' and len(ws) > 1 and ws[1][1] in FOOTER_NOUNS:
            kind = 'HEADER' if any(t[3].startswith('HVqi2') for t in ws) else 'FOOTER'
            bl = [t[1] for t in ws]
            stamp = next((name for code, name in STAMPS if code in bl), 'none')
            out.append((k, {'noun': FOOTER_NOUNS[ws[1][1]], 'kind': kind, 'stamp': stamp}))
    return out


def register_headers(ink):
    """D. the register headers: [(key, noun)]"""
    return [(k, REGISTER_NOUNS[ink.V[k][1][1]]) for k in ink.keys if ink.V[k] and ink.V[k][0][1] == '428' and len(ink.V[k]) > 1 and ink.V[k][1][1] in REGISTER_NOUNS]


# ---------------------------------------------------------------- the world --------------------------------------------------------------
def running_world():
    with contextlib.redirect_stdout(io.StringIO()):
        import cold_run_sequence as CS
        reg = CS.registry_map()
        w, M = CS.run_world(CS.PARAMS['sojourn_start']['value'], reg, 'register-gate')
    return w


def spans(text):
    return [(m.group(1), int(m.group(2)), int(m.group(3)), int(m.group(4) or m.group(3)))
            for m in re.finditer(r'(Gen|Exod|Lev|Num|Deut) (\d+):(\d+)(?:-(\d+))?', str(text or ''))]
def contains(text, k): return any(b == k[0] and c == k[1] and v1 <= k[2] <= v2 for b, c, v1, v2 in spans(text))
def chapter_of(text, k): return any(b == k[0] and c == k[1] for b, c, v1, v2 in spans(text))
def as_of_chapter(as_of, k): return str(as_of or '').startswith('%s %d:' % (k[0], k[1]))


def class_counts(ink, w):
    T = [r for r in w.tables.get('population', []) if r.get('grain') == 'counted' and r.get('count') is not None]
    LG = [(ent.eid, e) for ent in w.entities.values() for e in ent.ledger if e['effect'] == 'counted' and isinstance(e.get('value'), int)]
    out = collections.OrderedDict()
    for k, d in count_lines(ink):
        if not d['counts']:
            out[ref(k)] = {'class': 'MEASURE-ONLY', 'noun': d['noun'], 'values': d['values'], 'evidence': 'measures %s' % d['measures']}; continue
        row = [r for r in T if r['count'] in d['counts'] and as_of_chapter(r['as_of'], k)]
        led = [(eid, e) for eid, e in LG if e['value'] in d['counts'] and chapter_of(e.get('case_source'), k)]
        elsewhere = [r for r in T if r['count'] in d['counts']] + [e for eid, e in LG if e['value'] in d['counts']]
        cls = 'ROW' if row else ('LEDGER' if led else ('ELSEWHERE' if elsewhere else 'NONE'))
        ev = ('rows %s' % [(r['tribe'], r.get('family'), r['as_of']) for r in row][:3]) if row else \
             ('ledger %s' % [(eid, e['value'], str(e.get('case_source'))[:14]) for eid, e in led][:2]) if led else \
             ('elsewhere %s' % [(x.get('tribe') or x.get('subject'), x.get('as_of') or str(x.get('case_source'))[:14]) for x in elsewhere][:2]) if elsewhere else ''
        out[ref(k)] = {'class': cls, 'noun': d['noun'], 'values': d['values'], 'counts': d['counts'], 'measures': d['measures'], 'unpaired': d['unpaired'], 'evidence': ev}
    return out


def class_receipts(ink, w):
    ledger = [(ent.eid, e) for ent in w.entities.values() for e in ent.ledger]
    closed = [(eid, e) for eid, e in ledger if e.get('closed_by') is not None]
    EV = [l[2] for l in w.log if l[0] == 'EVENT']
    out = collections.OrderedDict()
    for k in receipts(ink):
        cl = [(eid, e['effect']) for eid, e in closed if contains(e.get('closed_by'), k) or contains(e.get('case_source'), k)]
        wr = [(eid, e['effect'], e['op']) for eid, e in ledger if contains(e.get('case_source'), k)]
        ev = [e['kind'] for e in EV if contains(e.get('case_source'), k)]
        ch = [(eid, e['effect']) for eid, e in closed if chapter_of(e.get('closed_by'), k) or chapter_of(e.get('case_source'), k)]
        cls = 'CLOSE' if cl else ('ACT' if wr else ('EVENT' if ev else ('CHAPTER' if ch else 'NONE')))
        out[ref(k)] = {'class': cls, 'evidence': {'CLOSE': cl[:3], 'ACT': wr[:3], 'EVENT': ev[:3], 'CHAPTER': ch[:3], 'NONE': []}[cls]}
    return out


def class_footers(ink):
    ga = {d: spec.get('given_at') for d, spec in yaml.safe_load(open(DISP))['daemons'].items()}
    ib = {d: str(spec.get('installed_by')).split()[0] for d, spec in yaml.safe_load(open(DISP))['daemons'].items()}
    def vpos(s):
        m = re.match(r'(\w+) (\d+):(\d+)', s or '')
        return (TORAH.index(m.group(1)), int(m.group(2)), int(m.group(3))) if m and m.group(1) in TORAH else None
    lines = footers(ink)
    out = collections.OrderedDict()
    for i, (k, d) in enumerate(lines):
        p = pos(k)
        if d['kind'] == 'FOOTER':
            lo = pos(lines[i - 1][0]) if i > 0 else (0, 0, 0); hi = p
        else:
            nxt = next((pos(kk) for kk, dd in lines[i + 1:] if dd['kind'] == 'FOOTER'), (99, 0, 0)); lo, hi = p, nxt
        inside = sorted((dn for dn, g in ga.items() if vpos(g) and lo < vpos(g) <= hi), key=lambda dn: vpos(ga[dn]))
        block = '(%s, %s]' % ('start' if lo == (0, 0, 0) else '%s %d:%d' % (TORAH[lo[0]], lo[1], lo[2]), 'end' if hi == (99, 0, 0) else '%s %d:%d' % (TORAH[hi[0]], hi[1], hi[2]))
        out[ref(k)] = {'class': 'DAEMONS' if inside else 'EMPTY', 'kind': d['kind'], 'noun': d['noun'], 'stamp': d['stamp'], 'block': block, 'daemons': len(inside),
                       'installed_by': dict(collections.Counter(ib[dn] for dn in inside)), 'evidence': ' '.join('%s@%s' % (dn, ga[dn]) for dn in inside)}
    return out


def class_registers(ink, w):
    T = w.tables.get('population', [])
    out = collections.OrderedDict()
    for k, noun in register_headers(ink):
        ch = '%s %d' % (k[0], k[1])
        d = out.setdefault(ch, {'headers': [], 'nouns': collections.Counter()})
        d['headers'].append(k[2]); d['nouns'][noun] += 1
    for ch, d in out.items():
        rows = [r for r in T if str(r.get('as_of') or '').startswith(ch + ':')]
        d['class'] = 'ROWS' if rows else 'NONE'; d['rows'] = len(rows); d['nouns'] = dict(d['nouns'])
        d['evidence'] = 'rows %d as_of %s' % (len(rows), sorted({r['as_of'] for r in rows})) if rows else ''
    return out


# ---------------------------------------------------------------- the dispositions -------------------------------------------------------
def verify(computed, declared):
    """the dispositions' law: a lie fails, a stale declaration fails, an unknown seat fails, a why is required; undeclared non-green = debt"""
    fails, debt, ok = [], [], []
    declared = declared or {}
    for sec in SECTIONS:
        comp = computed.get(sec, {}) or {}
        decl = declared.get(sec, {}) or {}
        for seat, spec in decl.items():
            if seat not in comp:
                fails.append('%s %s: declared, but the ink has no such seat' % (sec, seat))
        for seat, d in comp.items():
            cls = d['class']; spec = decl.get(seat)
            if cls in GREEN[sec]:
                if spec is not None: fails.append('%s %s: STALE — declared %s, the world now says %s (remove the declaration)' % (sec, seat, spec.get('class'), cls))
                continue
            if spec is None:
                debt.append('%s %s' % (sec, seat)); continue
            if spec.get('class') != cls:
                fails.append('%s %s: LIE — declared %s, computed %s' % (sec, seat, spec.get('class'), cls)); continue
            if not str(spec.get('why') or '').strip():
                fails.append('%s %s: a declaration without a why' % (sec, seat)); continue
            ok.append('%s %s' % (sec, seat))
    return {'fails': fails, 'debt': debt, 'declared': ok}


def load_declared():
    return yaml.safe_load(open(YAML)) if os.path.exists(YAML) else {}


# ---------------------------------------------------------------- the gate ---------------------------------------------------------------
def gate(strict=False, emit=False, index=True, ink=None, w=None):
    global TALLIES
    ink = ink or read_ink(); w = w or running_world()
    computed = {'counts': class_counts(ink, w), 'receipts': class_receipts(ink, w), 'footers': class_footers(ink), 'registers': class_registers(ink, w)}
    declared = load_declared()
    v = verify(computed, declared)
    TALLIES = {sec: dict(collections.Counter(d['class'] for d in computed[sec].values())) for sec in SECTIONS}
    lines = []
    P = lines.append
    P('THE REGISTER GATE — the ink\'s own formulas against the world (population table rows %d; ledger entries %d)' % (len(w.tables.get('population', [])), sum(len(e.ledger) for e in w.entities.values())))
    P('COVERAGE: ' + '; '.join('%s %d %s' % (sec, len(computed[sec]), TALLIES[sec]) for sec in SECTIONS))
    P('DECLARED %d; DEBT %d; FAILS %d' % (len(v['declared']), len(v['debt']), len(v['fails'])))
    titles = {'counts': 'A. THE COUNT LINES', 'receipts': 'B. THE RECEIPTS', 'footers': 'C. THE FOOTERS AND HEADERS', 'registers': 'D. THE REGISTERS'}
    for sec in SECTIONS:
        P('-- %s (%d)' % (titles[sec], len(computed[sec])))
        for seat, d in computed[sec].items():
            spec = (declared.get(sec) or {}).get(seat)
            tag = 'green' if d['class'] in GREEN[sec] else ('declared' if spec else 'DEBT')
            extra = ''
            if sec == 'counts': extra = '%s %s%s' % (d['noun'], d.get('counts', d['values']), ' UNPAIRED' if d.get('unpaired') else '')
            elif sec == 'footers': extra = '%s %s stamp %s block %s daemons %d %s' % (d['kind'], d['noun'], d['stamp'], d['block'], d['daemons'], d['installed_by'])
            elif sec == 'registers': extra = 'headers %s %s' % (d['headers'], d['nouns'])
            P('   %-11s %-13s %-8s %s | %s%s' % (seat, d['class'], tag, extra, str(d.get('evidence'))[:110], (' | why: ' + spec['why'][:100]) if spec else ''))
    if v['fails']:
        P('-- FAILS (%d)' % len(v['fails'])); [P('   ' + f) for f in v['fails']]
    if v['debt']:
        P('-- DEBT (%d undeclared non-green seats%s)' % (len(v['debt']), ' — FAIL under --strict' if strict else '')); [P('   ' + f) for f in v['debt']]
    verdict = 'FAILED' if v['fails'] or (strict and v['debt']) else 'GREEN'
    P('THE REGISTER GATE: %s%s' % (verdict, '' if verdict == 'GREEN' else ' (%d fails, %d debt)' % (len(v['fails']), len(v['debt']))))
    print('\n'.join(lines))
    if emit:
        print('\n# --emit: yaml stubs for the undeclared seats (type the why from the reading of the print)')
        stub = {}
        for item in v['debt']:
            sec, seat = item.split(' ', 1)
            stub.setdefault(sec, {})[seat] = {'class': computed[sec][seat]['class'], 'why': ''}
        print(yaml.safe_dump(stub, allow_unicode=True, sort_keys=False, width=140))
    if index:
        with open(INDEX, 'w') as f:
            f.write('# REGISTER_INDEX.md — written by register_census.py each run (documentation, never runtime)\n\n')
            f.write('\n'.join(lines) + '\n')
    return 1 if verdict == 'FAILED' else 0


if __name__ == '__main__':
    sys.exit(gate(strict='--strict' in sys.argv, emit='--emit' in sys.argv, index='--no-index' not in sys.argv))

#!/usr/bin/env python3
"""board_mockup.py — THE BOARD mockup (2026-09-14; the owner: "a stationary display… one window… I want to see what is being created"):
every thing in the world a tile that appears when it is created, lights when a law writes on it, carries a mark while it owes something and a
countdown while a timer runs on it; the page holds the journal's own rows (the running world's first 300 lines, Genesis 1 to 11:2) and
redraws the tiles as they are stepped — nothing typed. Writes mockup_board.html beside this script.
VERSION 3 (the owner's note, 2026-09-14, after D7's merge): "put a small screen to the left, in it place the box that was created in the
right as a stepper. the heavens box, then the earth box below it, then light below. The left box will scroll from bottom up as more boxes
are added. When I click on any box it will bring me back to that step in the process." — THE LEFT SCREEN: every tile, the moment it is
created on the board, is copied small into a strip on the left, oldest at the top, newest at the bottom, the strip scrolled to the bottom
as it grows; a click on any small tile replays the rows from the start to the step that created it (the board, the clock, the feed all
as they stood then); the tiles beyond that step stay in the strip, dimmed, so the same click walks forward again. The births now come from
the entities view of the one database (first mention per entity) — the August node.born rows are retired.
VERSION 4 (the owner's second note, the same sitting): "on the top right wher you have next, put a back button there. also when a new box
is created make the browser display the first created box in the middle of the broswer screen" — BACK beside Next (one step back, the
same replay); when a step creates tiles, the page scrolls so the first of them sits in the middle of the screen.
VERSION 5 (his third note, seen in Chrome): "when I click next and get the river out of eden it doesn't show it, it scrolls below to what came
after. i want it to show the first boxes created then I will navagate down to see the rest" — at Genesis 2:20's step eight things are
born at once across three groups, and the first by creation order (the tree of life, Plants) sat below the rivers (Places) on the board,
so centering it pushed the rivers above the fold. NOW: the page scrolls to the TOPMOST new tile on the board and puts it at the top of the
screen under the header, its group heading with it; every other new tile is below, reached by scrolling down.
VERSION 6 (his fourth note): "once a title (places, times, plants, etc) fills up three rows, make the full 3 rows turn into a scrollable
window. all titels should display 3 rows at all times" — every group's tile area is a window exactly three rows tall (the rows one fixed
height; a long line inside a tile clipped to two lines, the whole in its tooltip); past three rows the window scrolls inside itself; at a
step that creates tiles the window scrolls so the first new tile is its top row and the page scrolls the group's heading to the top of the
screen. (This amends the agreed shape's "no panes scrolling inside" on the owner's word.)"""
import json, html, os, re, sqlite3
import yaml
HERE = os.path.dirname(os.path.abspath(__file__))
SEG = '<repo-old>/World/journal/data/L3_run_cold_run_sequence_seed_isaac.jsonl'
REG = '<repo-old>/logic/corpus/entity_registry.yaml'
DB = '<repo-old>/World/journal/data/world.sqlite'
# THE READING ERA'S BIRTHS — the things the reading names as created (the ids are the registry's transliterations, glossed here in English as
# the law requires) and the board's group for each. Their verses are read from the entities view of the one database (the first mention of
# each id), not typed: the August tree's node.born rows are retired since D7's merge (2026-09-14). The dict's order breaks ties at one verse.
BIRTHS = {'shamayim': ('the heavens', 'The frame'), 'the_earth': ('the earth', 'The frame'), 'or': ('light', 'The frame'), 'raqia': ('the firmament', 'The frame'),
          'yabasha': ('the dry land', 'The frame'), 'deshe': ('the vegetation', 'Plants'), 'meorot': ('the lights of the firmament', 'The frame'),
          'maor_gadol': ('the great light', 'The frame'), 'maor_qaton': ('the small light', 'The frame'), 'kokhavim': ('the stars', 'The frame'),
          'taninim': ('the sea monsters', 'Creatures'), 'nefesh_chaya_romeset': ('the moving living creatures', 'Creatures'), 'of_kanaf': ('the winged fowl', 'Creatures'),
          'chayat_ha_aretz': ('the beasts of the earth', 'Creatures'), 'behemah': ('the cattle', 'Creatures'), 'remes_ha_adamah': ('the creeping things', 'Creatures'),
          'the_human': ('the human', 'People'), 'the_garden': ('the garden', 'Places'), 'etz_ha_chayim': ('the tree of life', 'Plants'),
          'etz_ha_daat_tov_va_ra': ('the tree of knowledge of good and evil', 'Plants'), 'nahar': ('the river out of Eden', 'Places'),
          'nahar_1': ('the first river, Pishon', 'Places'), 'nahar_2': ('the second river, Gihon', 'Places'), 'nahar_3': ('the third river, Hiddekel', 'Places'),
          'nahar_4': ('the fourth river, Perat', 'Places'), 'the_beasts': ('the beasts', 'Creatures'), 'of_ha_shamayim': ('the fowl of the heavens', 'Creatures'),
          'eve': ('Eve', 'People'), 'chagorot': ('the girdles of fig leaves', 'Things'), 'kotnot_or': ('the garments of skin', 'Things'),
          'the_cherubim': ('the cherubim', 'Guards'), 'lahat_ha_cherev': ('the flame of the sword', 'Guards'), 'the_city_of_enoch': ('the city of Enoch', 'Places'),
          'the_ark': ('the ark', 'Things'), 'mizbeach': ("Noah's altar", 'Things'), 'the_vineyard': ('the vineyard', 'Plants'),
          'ninveh': ('Nineveh', 'Places'), 'rechovot_ir': ('Rehoboth-ir', 'Places'), 'kalach': ('Calah', 'Places'), 'resen': ('Resen', 'Places')}
BOOK = {1: 'Gen', 2: 'Exod', 3: 'Lev', 4: 'Num', 5: 'Deut'}


def vkey(ref):
    m = re.match(r'^(Gen|Exod|Lev|Num|Deut)[ .](\d+)[:.](\d+)', ref or '')
    return ({'Gen': 1, 'Exod': 2, 'Lev': 3, 'Num': 4, 'Deut': 5}[m.group(1)], int(m.group(2)), int(m.group(3))) if m else None


def births(last_key):
    """the reading era's births up to the last verse of the embedded rows, each glossed, as board rows of the class 'born' — the verse of
    each is its first mention in the entities view of the one database; a birth the view does not know is refused and named"""
    db = sqlite3.connect(DB)
    first = {e: (ref, seq) for e, ref, seq in db.execute("select entity, first_ref, first_seq from entities where first_ref is not null")}
    db.close()
    out = []
    for n, (subj, g) in enumerate(BIRTHS.items()):
        if subj not in first:
            raise SystemExit('a birth with no first mention in the entities view: %r — the registry id changed?' % subj)
        ref, seq = first[subj]
        k = vkey(ref)
        if k is None or k > last_key:
            continue
        out.append({'k': 'born', 'e': subj, 'r': '%s %d:%d' % (BOOK[k[0]], k[1], k[2]), 'key': k, 'seq': (seq, n), 'n': g[0], 'g': g[1]})
    out.sort(key=lambda b: b['seq'])
    return out
OUT = os.path.join(HERE, 'mockup_board.html')
N = 300

NAMES = {'the-world': 'the world', 'the_human': 'the human', 'the-seventh-day': 'the seventh day', 'the_beasts': 'the beasts', 'eve': 'Eve',
         'the_serpent': 'the serpent', 'adam_and_eve': 'Adam and Eve', 'the_ground': 'the ground', 'noach': 'Noah', 'the-cloud': 'the cloud',
         'god': 'God', 'the_generation_of_the_flood': 'the generation of the flood', 'noah_and_sons': 'Noah and his sons', 'tubal_cain': 'Tubal-cain',
         'enoch_son_of_cain': 'Enoch son of Cain', 'lamech_son_of_methushael': 'Lamech son of Methushael', 'the_city_of_enoch': 'the city of Enoch',
         'the_altar_of_noah': "Noah's altar", 'shem_and_japheth': 'Shem and Japheth'}
GROUP = {'person': 'People', 'collective': 'Peoples and groups', 'people': 'Peoples and groups', 'place': 'Places', 'object': 'Things',
         'creature': 'Creatures', 'institution': 'Institutions', 'divine': 'Heaven'}
GROUP_OF_UNKNOWN = {'the-world': 'Places', 'the-seventh-day': 'Times', 'the-cloud': 'Things'}


def name(s):
    if s in NAMES:
        return NAMES[s]
    w = s.replace('_', ' ').replace('-', ' ')
    return w if w.startswith('the ') else w[:1].upper() + w[1:]


def words(s):
    return str(s).replace('_', ' ')


def head(ref):
    m = re.match(r'^\s*((?:Gen|Exod|Lev|Num|Deut)\s+\d+:\d+(?:-\d+)?)', ref or '')
    return m.group(1) if m else (ref or '')[:20]


def own(ref):
    if ref and ' — ' in ref:
        w = re.split(r' \(|;', ref.split(' — ', 1)[1])[0].strip()
        return w[:120] + ('…' if len(w) > 120 else '')
    return ''


def short(v):
    if v is True or v is None:
        return ''
    if isinstance(v, list):
        return ', '.join(words(x) for x in v)[:60]
    s = words(v)
    return s if len(s) <= 60 else s[:60] + '…'


def main():
    reg = yaml.safe_load(open(REG, encoding='utf-8'))
    ents = reg.get('entities') or []
    kind_of = {e['id']: e.get('kind', '?') for e in ents if isinstance(e, dict) and 'id' in e}
    rows, kinds = [], {}
    for l in open(SEG, encoding='utf-8').read().split('\n')[1:N + 1]:
        if not l.strip():
            continue
        e = json.loads(l); d = e['data']; k = e['kind'].replace('run.', '')
        r = {'s': e['s'], 'k': k, 'd': e['op'], 'e': e['subj'], 'r': head(e['prov'].get('ref') or ''), 'w': own(e['prov'].get('ref') or '')}
        if k == 'marker':
            r['w'] = re.split(r' — | \(', str(d.get('value') or ''))[0][:70]
        if k == 'event':
            r['a'] = words(d.get('kind', ''))
        if k in ('write', 'retro_write'):
            r.update(f=words(d.get('effect', '')), p=bool(d.get('open')), v=short(d.get('value')), q=d.get('seq'))
        if k == 'timer_set':
            r.update(f=words(d.get('effect', '')), due=d.get('due'))
        if k == 'timer_fire':
            r.update(f=words(d.get('effect', '')))
        if k == 'close':
            r.update(f=words(d.get('effect', '')), q=d.get('entry_seq'), r=head(d.get('note', '')), w=own(d.get('note', '')))
        rows.append(r)
        if e['subj'] not in ('clock', 'world') and e['subj'] not in kinds:
            kinds[e['subj']] = {'n': name(e['subj']), 'g': GROUP_OF_UNKNOWN.get(e['subj']) or GROUP.get(kind_of.get(e['subj'], '?'), 'Others')}
    # THE MERGE ON THE BOARD: each birth placed before the first tape line at or after its verse (the left edge), in verse order
    last = None
    for r in rows:
        kk = vkey(r['r'])
        if kk: last = kk if last is None or kk > last else last
    born = births(last)
    merged, bi = [], 0
    for r in rows:
        kk = vkey(r['r']) if r['k'] in ('marker', 'event') else None
        while bi < len(born) and kk is not None and born[bi]['key'] <= kk:
            b = dict(born[bi]); b.pop('key'); b.pop('seq'); merged.append(b); bi += 1
        merged.append(r)
    for b in born[bi:]:
        b = dict(b); b.pop('key'); b.pop('seq'); merged.append(b)
    for b in born:
        kinds[b['e']] = {'n': b['n'], 'g': b['g']}
    rows = merged
    page = PAGE.replace('__ROWS__', json.dumps(rows, ensure_ascii=False, separators=(',', ':'))).replace('__KINDS__', json.dumps(kinds, ensure_ascii=False, separators=(',', ':')))
    open(OUT, 'w', encoding='utf-8').write(page)
    print('%s: %d rows embedded (%d births from the entities view merged in; the first three %s), %d things named; the last row at %s'
          % (OUT, len(rows), len(born), ', '.join('%s at %s' % (b['n'], b['r']) for b in born[:3]), len(kinds), rows[-1]['r']))


PAGE = r'''<title>The Board of Things</title>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Fraunces:opsz,wght@9..144,500&family=IBM+Plex+Sans:wght@400;500;600&family=IBM+Plex+Mono:wght@400;500&display=swap">
<style>
  :root { --ground:#EEF0F3; --surface:#FFFFFF; --line:#D3D8DF; --ink:#1B1F26; --soft:#3E4753;
          --clock:#3D5A80; --new:#2E7D4F; --new-bg:#DFF0E5; --open:#B7791F; --open-bg:#FBEDD0;
          --closed:#5B4B8A; --timer:#8C2F39; --timer-bg:#F5E1E3; --lit:#FFF2C2; --strip-h:120px; }
  @media (prefers-color-scheme: dark) { :root:not([data-theme="light"]) {
          --ground:#15181D; --surface:#1E2229; --line:#353C47; --ink:#E7E9EC; --soft:#C3CAD3;
          --clock:#8FB0D8; --new:#7FC292; --new-bg:#1F3125; --open:#E0AE4C; --open-bg:#3A2E17;
          --closed:#B7A6E0; --timer:#DE7C85; --timer-bg:#3A2226; --lit:#4A3F12; } }
  :root[data-theme="dark"] {
          --ground:#15181D; --surface:#1E2229; --line:#353C47; --ink:#E7E9EC; --soft:#C3CAD3;
          --clock:#8FB0D8; --new:#7FC292; --new-bg:#1F3125; --open:#E0AE4C; --open-bg:#3A2E17;
          --closed:#B7A6E0; --timer:#DE7C85; --timer-bg:#3A2226; --lit:#4A3F12; }
  * { box-sizing:border-box; }
  body { margin:0; background:var(--ground); color:var(--ink); font-family:"IBM Plex Sans","Helvetica Neue",Arial,sans-serif; font-size:14px; line-height:1.45; padding-block:0 40px; padding-inline:20px; }
  .mono { font-family:"IBM Plex Mono",Menlo,monospace; font-variant-numeric:tabular-nums; }
  .wrap { max-width:1180px; margin:0 auto; }
  .strip { position:sticky; top:0; background:var(--surface); border-bottom:1px solid var(--line); margin-inline:-20px; padding:12px 20px; z-index:2; }
  .strip .in { max-width:1180px; margin:0 auto; display:flex; flex-wrap:wrap; align-items:center; gap:8px 22px; }
  h1 { font-family:"Fraunces",Georgia,serif; font-weight:500; font-size:21px; margin:0; }
  .k { font-size:10.5px; letter-spacing:.08em; text-transform:uppercase; color:var(--soft); font-weight:600; display:block; }
  .v { font-size:15px; font-weight:500; }
  .v.clock { color:var(--clock); }
  .ctl { margin-left:auto; display:flex; gap:8px; align-items:center; flex-wrap:wrap; }
  .btn { font:inherit; font-size:13px; padding:6px 13px; border:1px solid var(--line); background:var(--ground); color:var(--ink); border-radius:4px; cursor:pointer; }
  .btn.primary { background:var(--clock); border-color:var(--clock); color:#fff; font-weight:600; }
  .btn:focus-visible, .mini:focus-visible { outline:2px solid var(--timer); outline-offset:2px; }
  select { font:inherit; font-size:13px; padding:5px 8px; border:1px solid var(--line); border-radius:4px; background:var(--ground); color:var(--ink); }
  .act { width:100%; font-size:13px; color:var(--soft); }
  .act b { color:var(--ink); }
  .mock { font-size:12.5px; color:var(--soft); margin:12px 0 4px; }
  .main { display:grid; grid-template-columns:200px minmax(0,1fr); gap:20px; align-items:start; margin-top:8px; }
  .left { position:sticky; top:var(--strip-h); }
  .left h2, .group h2 { font-family:"Fraunces",Georgia,serif; font-weight:500; font-size:15px; margin:0 0 8px; color:var(--soft); }
  .left h2 span, .group h2 span { font-family:"IBM Plex Mono",monospace; font-size:12px; margin-left:8px; }
  .made { position:relative; height:calc(100vh - var(--strip-h) - 80px); min-height:220px; overflow-y:auto; background:var(--surface); border:1px solid var(--line); border-radius:5px; padding:6px; display:flex; flex-direction:column; gap:5px; scroll-behavior:smooth; }
  .mini { font:inherit; text-align:left; display:grid; gap:1px; padding:5px 8px; border:1px solid var(--line); border-radius:4px; background:var(--ground); color:var(--ink); cursor:pointer; flex:none; transition:opacity .3s, border-color .3s; }
  .mini:hover { border-color:var(--clock); }
  .mini.now { border-color:var(--clock); box-shadow:0 0 0 1px var(--clock); background:var(--lit); }
  .mini.ahead { opacity:.38; }
  .mini .mn { font-weight:600; font-size:12.5px; }
  .mini .mv { font-size:11px; color:var(--soft); }
  .made .empty { padding:8px 4px; }
  .right { min-width:0; }
  .groups { display:grid; gap:18px; }
  .group { scroll-margin-top:calc(var(--strip-h) + 10px); }
  .tiles { --row:92px; position:relative; display:grid; grid-template-columns:repeat(auto-fill, minmax(168px, 1fr)); grid-auto-rows:var(--row); gap:8px; align-content:start;
           height:calc(3 * var(--row) + 2 * 8px + 8px); overflow-y:auto; padding:4px; background:var(--ground); border:1px solid var(--line); border-radius:6px; scroll-behavior:smooth; }
  .tile { background:var(--surface); border:1px solid var(--line); border-radius:5px; padding:8px 10px; display:grid; gap:4px; align-content:start; overflow:hidden; transition:background .6s, box-shadow .6s; }
  .tile.lit { background:var(--lit); box-shadow:0 0 0 2px var(--open); }
  .tile.born, .mini.just { animation: born .8s ease-out; }
  @keyframes born { from { transform:scale(.85); opacity:0; } to { transform:scale(1); opacity:1; } }
  @media (prefers-reduced-motion: reduce) { .tile, .mini { transition:none; } .tile.born, .mini.just { animation:none; } .made, .tiles { scroll-behavior:auto; } }
  .tile .name { font-weight:600; font-size:13.5px; line-height:1.25; display:-webkit-box; -webkit-line-clamp:2; -webkit-box-orient:vertical; overflow:hidden; }
  .tile .last { font-size:12px; color:var(--soft); line-height:1.3; display:-webkit-box; -webkit-line-clamp:2; -webkit-box-orient:vertical; overflow:hidden; }
  .marks { display:flex; flex-wrap:wrap; gap:4px; }
  .mark { font-size:10.5px; font-weight:600; padding:1px 7px; border-radius:3px; white-space:nowrap; }
  .mark.open { color:var(--open); background:var(--open-bg); }
  .mark.timer { color:var(--timer); background:var(--timer-bg); }
  .empty { color:var(--soft); font-size:13px; padding:14px 0; }
  .feed { margin-top:18px; border-top:1px solid var(--line); padding-top:8px; font-size:13px; display:grid; gap:3px; }
  .feed .l { display:grid; grid-template-columns:70px 1fr auto; gap:10px; }
  .stamp { font-size:10.5px; font-weight:700; letter-spacing:.06em; padding:1px 7px; border-radius:3px; white-space:nowrap; }
  .stamp.new { color:var(--new); background:var(--new-bg); } .stamp.open { color:var(--open); background:var(--open-bg); }
  .stamp.closed { color:var(--closed); background:var(--surface); border:1px solid var(--closed); } .stamp.timer { color:var(--timer); background:var(--timer-bg); }
  .key { margin-top:14px; display:flex; flex-wrap:wrap; gap:8px 14px; align-items:center; font-size:12.5px; color:var(--soft); }
  @media (max-width: 760px) { .main { grid-template-columns:1fr; } .left { position:static; } .made { height:180px; min-height:0; } }
</style>
<div class="strip" id="strip"><div class="in">
  <h1>The Board of Things</h1>
  <div><span class="k">Step</span><span class="v mono" id="stepno">0</span></div>
  <div><span class="k">Day</span><span class="v clock mono" id="day">0</span></div>
  <div><span class="k">The text stands at</span><span class="v mono" id="pos">—</span></div>
  <div><span class="k">Things in the world</span><span class="v mono" id="count">0</span></div>
  <div><span class="k">Open entries</span><span class="v mono" id="open">0</span></div>
  <div class="ctl">
    <label for="speed" class="k" style="display:inline">speed</label>
    <select id="speed"><option value="1200">slow</option><option value="600" selected>medium</option><option value="200">fast</option></select>
    <button class="btn" id="auto">Auto-play</button>
    <button class="btn" id="reset">Reset</button>
    <button class="btn" id="back">‹ Back</button>
    <button class="btn primary" id="next">Next ›</button>
  </div>
  <div class="act" id="act">Press Next: the world is empty, the tape stands before Genesis 1:5.</div>
</div></div>
<div class="wrap">
  <p class="mock">Mockup, redrawn from the journal's own rows — the running world's first 300 lines (Genesis 1 to 11:2) with the reading era's births merged in at their verses (light, the firmament, the lights, the creatures…): a tile appears on the board when a thing is created or first written on, lights when a law writes on it, carries a mark while it owes something and a countdown while a timer runs. The left screen keeps every tile in the order it was created, newest at the bottom; click one to go back to that step. Nothing is typed.</p>
  <div class="main">
    <div class="left">
      <h2>Created, in order<span id="madecount">0</span></h2>
      <div class="made" id="made"><div class="empty">Nothing created yet.</div></div>
    </div>
    <div class="right">
      <div class="groups" id="groups"><div class="empty">Nothing exists yet.</div></div>
      <div class="feed" id="feed"></div>
      <div class="key"><span>Key:</span> <span class="stamp new">NEW</span> appeared <span class="stamp open">OPEN</span> owes something <span class="stamp closed">CLOSED</span> paid <span class="stamp timer">TIMER</span> a countdown runs <span>· a lit tile was just written on · a dimmed tile on the left is ahead of this step</span></div>
    </div>
  </div>
</div>
<script>
const ROWS = __ROWS__;
const KINDS = __KINDS__;
const ORDER = ['The frame', 'Places', 'Times', 'Plants', 'Creatures', 'Guards', 'People', 'Peoples and groups', 'Things', 'Institutions', 'Heaven', 'Others'];
let i = 0, day = 0, pos = '—', tiles = {}, feed = [], timer = null, stepNo = 0, history = [], added = false, created = 0;
const REDUCE = matchMedia('(prefers-reduced-motion: reduce)').matches;
const $ = id => document.getElementById(id);
function fmt(n) { return Number(n).toLocaleString('en-US'); }
function tile(id, verse) {
  if (!tiles[id]) {
    const k = KINDS[id] || {n: id, g: 'Others'};
    tiles[id] = {id, name: k.n, group: k.g, marks: [], timers: [], last: '', lit: 0, born: 1, step: stepNo, idx: created++};
    if (!history.some(h => h.id === id)) { history.push({id, name: k.n, verse: verse || pos, step: stepNo}); added = true; }   // the left screen: a small copy, once, at its step
  }
  return tiles[id];
}
function pushFeed(stamp, text, verse) { feed.unshift({stamp, text, verse}); feed = feed.slice(0, 5); }
function apply(r) {
  if (r.k === 'born') { const isNew = !tiles[r.e]; const t = tile(r.e, r.r); t.lit = 1; if (isNew) { t.last = 'created'; pushFeed('new', r.n + ' — created', r.r); } return; }
  if (r.k === 'marker') { day = r.d; pos = r.r; $('act').innerHTML = '<b>' + r.r + '</b> — the clock moves to day ' + fmt(day) + (r.w ? ', ' + esc(r.w) : ''); return; }
  if (r.k === 'event') { pos = r.r || pos; $('act').innerHTML = '<b>' + esc(r.r) + '</b> — ' + esc(nm(r.e)) + ': ' + esc(r.a) + (r.w ? ' <i>' + esc(r.w) + '</i>' : ''); return; }
  if (r.k === 'write' || r.k === 'retro_write') {
    const isNew = !tiles[r.e]; const t = tile(r.e, r.r); t.lit = 1; t.last = r.f + (r.v ? ': ' + r.v : '');
    if (r.p) t.marks.push({f: r.f, q: r.q});
    if (isNew) pushFeed('new', nm(r.e) + ' — ' + t.last, r.r); else if (r.p) pushFeed('open', nm(r.e) + ' — ' + r.f, r.r);
    return;
  }
  if (r.k === 'timer_set') { const t = tile(r.e, r.r); t.lit = 1; t.timers.push({f: r.f, due: r.due}); pushFeed('timer', nm(r.e) + ' — ' + r.f + ', due day ' + fmt(r.due), r.r); return; }
  if (r.k === 'timer_fire') { const t = tile(r.e, r.r); t.lit = 1; t.timers = t.timers.filter(x => x.f !== r.f); pushFeed('timer', 'fired — ' + nm(r.e) + ': ' + r.f, r.r); $('act').innerHTML = '<b>day ' + fmt(r.d) + '</b> — a timer fires on ' + esc(nm(r.e)) + ': ' + esc(r.f); return; }
  if (r.k === 'close') { const t = tile(r.e, r.r); t.lit = 1; const j = t.marks.findIndex(m => m.q === r.q || m.f === r.f); if (j >= 0) t.marks.splice(j, 1); pushFeed('closed', nm(r.e) + ' — ' + r.f + ', paid', r.r); return; }
}
function nm(id) { return (KINDS[id] || {n: id}).n; }
function esc(s) { return String(s).replace(/&/g, '&amp;').replace(/</g, '&lt;'); }
function step(drawIt = true) {
  if (i >= ROWS.length) { $('act').textContent = 'The end of these rows: Genesis 11:2. The real board keeps going with the tape.'; stopAuto(); return; }
  stepNo++;
  Object.values(tiles).forEach(t => { t.lit = 0; t.born = 0; });
  while (i < ROWS.length && ROWS[i].k === 'born') { apply(ROWS[i]); i++; }   // the births at this verse's left edge come with its block
  if (i < ROWS.length) {
    const r = ROWS[i]; apply(r); i++;
    // a block: an event with its consequences; a marker alone; a fire with its write; a close alone
    if (r.k === 'event' || r.k === 'timer_fire') {
      while (i < ROWS.length && ['write', 'retro_write', 'timer_set', 'close'].includes(ROWS[i].k)) { apply(ROWS[i]); i++; }
    }
  }
  if (drawIt) draw();
}
function rewind(n) {   // the click on the left screen: the rows replayed from the start to step n — the board, the clock and the feed as they stood
  stopAuto();
  i = 0; day = 0; pos = '—'; tiles = {}; feed = []; stepNo = 0; created = 0;
  while (stepNo < n && i < ROWS.length) step(false);
  draw();
  centerStrip();
}
function centerStrip() {   // the left screen scrolled so this step's tile sits mid-strip (the strip's own scroll, never the page's)
  const made = $('made'), cur = made.querySelector('.mini.now');
  if (cur) made.scrollTop = cur.offsetTop - made.clientHeight / 2 + cur.offsetHeight / 2;
}
function draw() {
  $('stepno').textContent = fmt(stepNo); $('day').textContent = fmt(day); $('pos').textContent = pos;
  const all = Object.values(tiles);
  $('count').textContent = all.length;
  $('open').textContent = all.reduce((n, t) => n + t.marks.length, 0);
  const g = $('groups'); g.innerHTML = '';
  if (!all.length) { g.innerHTML = '<div class="empty">Nothing exists yet.</div>'; }
  ORDER.forEach(name => {
    const ts = all.filter(t => t.group === name); if (!ts.length) return;
    const sec = document.createElement('div'); sec.className = 'group';
    sec.innerHTML = '<h2>' + name + '<span>' + ts.length + '</span></h2><div class="tiles"></div>';
    const box = sec.querySelector('.tiles');
    ts.forEach(t => {
      const el = document.createElement('div'); el.className = 'tile' + (t.lit ? ' lit' : '') + (t.born ? ' born' : ''); el.dataset.id = t.id;
      const marks = t.marks.map(m => '<span class="mark open">' + esc(m.f) + '</span>').join('') +
                    t.timers.map(x => '<span class="mark timer">' + esc(x.f) + ' · ' + fmt(Math.max(0, x.due - day)) + ' days</span>').join('');
      el.innerHTML = '<div class="name">' + esc(t.name) + '</div>' + (marks ? '<div class="marks">' + marks + '</div>' : '') + (t.last ? '<div class="last">' + esc(t.last) + '</div>' : '');
      el.title = t.name + (t.last ? ' — ' + t.last : '');
      box.appendChild(el);
    });
    g.appendChild(sec);
  });
  // the left screen: every tile in the order it was created; the ones of this step marked; the ones ahead of this step dimmed
  const made = $('made'); made.innerHTML = '';
  $('madecount').textContent = history.length;
  if (!history.length) made.innerHTML = '<div class="empty">Nothing created yet.</div>';
  history.forEach(h => {
    const el = document.createElement('button'); el.type = 'button'; el.dataset.step = h.step;
    el.className = 'mini' + (h.step === stepNo ? ' now' : '') + (h.step > stepNo ? ' ahead' : '') + (tiles[h.id] && tiles[h.id].born ? ' just' : '');
    el.title = 'Back to step ' + h.step + ', ' + h.verse;
    el.innerHTML = '<span class="mn">' + esc(h.name) + '</span><span class="mv mono">' + esc(h.verse) + '</span>';
    el.addEventListener('click', () => {
      rewind(h.step);
      $('act').innerHTML = '<b>Step ' + fmt(h.step) + '</b> — back to when ' + esc(h.name) + ' was created, ' + esc(h.verse) + '. Next walks forward from here.';
    });
    made.appendChild(el);
  });
  if (added) { made.scrollTop = made.scrollHeight; added = false; }   // the strip grows downward; the newest stays in view
  fitStrip();
  const first = g.querySelector('.tile.born');   // the owner: the first new box at the top, the rest below it — the group's window scrolled so the new tile is its top row, the page scrolled to the group's heading
  if (first) { const box = first.parentElement; box.scrollTop = Math.max(0, first.offsetTop - 4); box.parentElement.scrollIntoView({block: 'start', behavior: REDUCE ? 'auto' : 'smooth'}); }
}
function fitStrip() { document.documentElement.style.setProperty('--strip-h', ($('strip').offsetHeight + 12) + 'px'); }
function stopAuto() { if (timer) { clearInterval(timer); timer = null; $('auto').textContent = 'Auto-play'; } }
$('next').addEventListener('click', () => { stopAuto(); step(); });
$('back').addEventListener('click', () => { stopAuto(); if (stepNo === 0) return; rewind(stepNo - 1); $('act').innerHTML = '<b>Step ' + fmt(stepNo) + '</b> — one step back' + (stepNo ? ', the text at ' + esc(pos) : ', the world empty again') + '.'; });
$('auto').addEventListener('click', () => { if (timer) { stopAuto(); return; } $('auto').textContent = 'Pause'; timer = setInterval(step, Number($('speed').value)); });
$('speed').addEventListener('change', () => { if (timer) { stopAuto(); $('auto').click(); } });
$('reset').addEventListener('click', () => { stopAuto(); i = 0; day = 0; pos = '—'; tiles = {}; feed = []; stepNo = 0; history = []; created = 0; $('act').textContent = 'Press Next: the world is empty, the tape stands before Genesis 1:5.'; draw(); });
window.addEventListener('resize', fitStrip);
draw();
</script>
'''

if __name__ == '__main__':
    main()

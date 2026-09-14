#!/usr/bin/env python3
"""feed_mockup.py — the FEED mockup, GENERATED from the journal's own rows (the two threads' agreement of 2026-09-14, THE_LOOP.md item 10):
one line per event as it happens, the clock moving its own line, a stamp for the state, every line saying what changed; nothing typed.
Reads the running world's base segment; renders creation week through Cain (lines 1-70) and, after a gap, the flood's reprieve (the
first timer set and fired, lines 170-206). Writes mockup_feed_page.html beside this script."""
import json, html, os, re, sys
HERE = os.path.dirname(os.path.abspath(__file__))
SEG = '<repo-old>/World/journal/data/L3_run_cold_run_sequence_seed_isaac.jsonl'
OUT = os.path.join(HERE, 'mockup_feed_page.html')
RANGES = [(1, 70), (170, 206)]

NAMES = {'the-world': 'the world', 'the_human': 'the human', 'the-seventh-day': 'the seventh day', 'the_beasts': 'the beasts', 'eve': 'Eve',
         'the_serpent': 'the serpent', 'adam_and_eve': 'Adam and Eve', 'the_ground': 'the ground', 'cain': 'Cain', 'abel': 'Abel',
         'noach': 'Noah', 'the-generation-of-the-flood': 'the generation of the flood', 'the_generation_of_the_flood': 'the generation of the flood',
         'the_ark': 'the ark', 'lamech': 'Lamech', 'seth': 'Seth', 'enosh': 'Enosh', 'chanoch': 'Enoch', 'the-earth': 'the earth', 'the_earth': 'the earth'}

def name(s):
    if s in NAMES:
        return NAMES[s]
    w = s.replace('_', ' ').replace('-', ' ')
    return w if w.startswith('the ') else w[:1].upper() + w[1:]

def words(s):
    return s.replace('_', ' ')

def verse_head(ref):
    m = re.match(r'^\s*((?:Gen|Exod|Lev|Num|Deut)\s+\d+:\d+(?:-\d+)?)', ref or '')
    return m.group(1) if m else (ref or '')

def verse_words(ref):
    """the verse's own words when the reference carries them after the dash"""
    if ref and ' — ' in ref:
        w = ref.split(' — ', 1)[1]
        w = re.split(r' \(|;', w)[0].strip()
        return w[:110] + ('…' if len(w) > 110 else '')
    return ''

def value_words(v):
    if v is True or v is None:
        return ''
    if isinstance(v, list):
        return ', '.join(str(x).replace('_', ' ') for x in v)
    s = str(v).replace('_', ' ')
    return s if len(s) <= 70 else s[:70] + '…'

def load(ranges):
    lines = open(SEG, encoding='utf-8').read().split('\n')[1:]
    out = []
    for lo, hi in ranges:
        out.append([json.loads(l) for l in lines[lo - 1:hi] if l.strip()])
    return out

def render(chunks):
    seen, rows, things, day, pos = set(), [], 0, 0, ''
    for ci, chunk in enumerate(chunks):
        if ci:
            rows.append('<div class="gap">… lines %d to %d, the generations from Adam to Noah …</div>' % (RANGES[ci - 1][1] + 1, RANGES[ci][0] - 1))
        i = 0
        while i < len(chunk):
            e = chunk[i]; d = e['data']; k = e['kind']; ref = e['prov'].get('ref') or ''
            day = e['op']
            if k == 'run.marker':
                pos = verse_head(ref)
                v = str(d.get('value') or '')
                v = re.split(r' — | \(', v)[0][:80]
                rows.append('<div class="row clock"><span class="day mono">day %s</span><span class="stamp clock">CLOCK</span><div class="body"><span class="verse mono">%s</span> the clock moves to day %s — %s</div></div>'
                            % (fmt(day), html.escape(pos), fmt(day), html.escape(v)))
                i += 1; continue
            if k in ('run.event',):
                pos = verse_head(ref) or pos
                act = words(d.get('kind', ''))
                subj = name(e['subj'])
                own = verse_words(ref)
                # the consequences: the writes and timer-sets that follow this event until the next event/marker
                j = i + 1; cons = []
                while j < len(chunk) and chunk[j]['kind'] in ('run.write', 'run.retro_write', 'run.timer_set', 'run.close'):
                    cons.append(chunk[j]); j += 1
                inner = []
                for c in cons:
                    cd = c['data']; ent = c['subj']
                    if c['kind'] in ('run.write', 'run.retro_write'):
                        stamp = ''
                        if ent not in seen:
                            seen.add(ent); things += 1; stamp = '<span class="stamp new">NEW</span>'
                        elif cd.get('open'):
                            stamp = '<span class="stamp open">OPEN</span>'
                        val = value_words(cd.get('value'))
                        inner.append('<div class="chg">%s<b>%s</b>: %s%s</div>' % (stamp, html.escape(name(ent)), html.escape(words(cd.get('effect', ''))), (' — ' + html.escape(val)) if val else ''))
                    elif c['kind'] == 'run.timer_set':
                        inner.append('<div class="chg"><span class="stamp timer">TIMER</span><b>%s</b>: %s — due day %s</div>' % (html.escape(name(ent)), html.escape(words(cd.get('effect', ''))), fmt(cd.get('due'))))
                    elif c['kind'] == 'run.close':
                        inner.append('<div class="chg"><span class="stamp closed">CLOSED</span><b>%s</b>: %s — paid at %s</div>' % (html.escape(name(ent)), html.escape(words(cd.get('effect', ''))), html.escape(verse_head(cd.get('note', '')))))
                if not inner:
                    inner.append('<div class="chg none">nothing written</div>')
                rows.append('<div class="row"><span class="day mono">day %s</span><span class="stamp act">ACT</span><div class="body"><span class="verse mono">%s</span> <b>%s</b> — %s%s%s</div></div>'
                            % (fmt(day), html.escape(pos), html.escape(subj), html.escape(act), (': <i>%s</i>' % html.escape(own)) if own else '', ''.join(inner)))
                i = j; continue
            if k == 'run.timer_fire':
                cd = d; ent = e['subj']
                j = i + 1; inner = []
                while j < len(chunk) and chunk[j]['kind'] in ('run.write', 'run.retro_write', 'run.timer_set'):
                    c = chunk[j]; cd2 = c['data']
                    if c['kind'] != 'run.timer_set':
                        stamp = ''
                        if c['subj'] not in seen:
                            seen.add(c['subj']); things += 1; stamp = '<span class="stamp new">NEW</span>'
                        elif cd2.get('open'):
                            stamp = '<span class="stamp open">OPEN</span>'
                        val = value_words(cd2.get('value'))
                        inner.append('<div class="chg">%s<b>%s</b>: %s%s</div>' % (stamp, html.escape(name(c['subj'])), html.escape(words(cd2.get('effect', ''))), (' — ' + html.escape(val)) if val else ''))
                    j += 1
                rows.append('<div class="row"><span class="day mono">day %s</span><span class="stamp timer">TIMER</span><div class="body"><span class="verse mono">%s</span> the timer <b>%s</b> fires on <b>%s</b>%s</div></div>'
                            % (fmt(day), html.escape(verse_head(ref)), html.escape(words(cd.get('effect', ''))), html.escape(name(ent)), ''.join(inner)))
                i = j; continue
            if k == 'run.close':
                cd = d
                rows.append('<div class="row"><span class="day mono">day %s</span><span class="stamp closed">CLOSED</span><div class="body"><span class="verse mono">%s</span> <b>%s</b>: %s — paid</div></div>'
                            % (fmt(day), html.escape(verse_head(cd.get('note', ''))), html.escape(name(e['subj'])), html.escape(words(cd.get('effect', '')))))
                i += 1; continue
            # a stray write/timer_set not under an event (a retro-write): its own line
            cd = d
            if k in ('run.write', 'run.retro_write'):
                stamp = 'new' if e['subj'] not in seen else ('open' if cd.get('open') else '')
                if e['subj'] not in seen:
                    seen.add(e['subj']); things += 1
                rows.append('<div class="row"><span class="day mono">day %s</span><span class="stamp %s">%s</span><div class="body"><span class="verse mono">%s</span> <b>%s</b>: %s</div></div>'
                            % (fmt(day), stamp or 'act', (stamp or 'write').upper(), html.escape(verse_head(ref)), html.escape(name(e['subj'])), html.escape(words(cd.get('effect', '')))))
            i += 1
    return rows, day, pos, things

def fmt(n):
    try:
        return '{:,}'.format(int(n))
    except (TypeError, ValueError):
        return str(n)

PAGE = '''<title>A World Forming</title>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Fraunces:opsz,wght@9..144,500&family=IBM+Plex+Sans:wght@400;500;600&family=IBM+Plex+Mono:wght@400;500&display=swap">
<style>
  :root { --ground:#EEF0F3; --surface:#FFFFFF; --line:#D3D8DF; --ink:#1B1F26; --soft:#3E4753;
          --clock:#3D5A80; --clock-bg:#E1E8F2; --new:#2E7D4F; --new-bg:#DFF0E5; --open:#B7791F; --open-bg:#FBEDD0;
          --closed:#5B4B8A; --closed-bg:#E7E1F3; --timer:#8C2F39; --timer-bg:#F5E1E3; --act:#1B1F26; --act-bg:#E4E7EB; }
  @media (prefers-color-scheme: dark) { :root:not([data-theme="light"]) {
          --ground:#15181D; --surface:#1E2229; --line:#353C47; --ink:#E7E9EC; --soft:#C3CAD3;
          --clock:#8FB0D8; --clock-bg:#1F2C3D; --new:#7FC292; --new-bg:#1F3125; --open:#E0AE4C; --open-bg:#3A2E17;
          --closed:#B7A6E0; --closed-bg:#2B2440; --timer:#DE7C85; --timer-bg:#3A2226; --act:#E7E9EC; --act-bg:#2A303A; } }
  :root[data-theme="dark"] {
          --ground:#15181D; --surface:#1E2229; --line:#353C47; --ink:#E7E9EC; --soft:#C3CAD3;
          --clock:#8FB0D8; --clock-bg:#1F2C3D; --new:#7FC292; --new-bg:#1F3125; --open:#E0AE4C; --open-bg:#3A2E17;
          --closed:#B7A6E0; --closed-bg:#2B2440; --timer:#DE7C85; --timer-bg:#3A2226; --act:#E7E9EC; --act-bg:#2A303A; }
  * { box-sizing: border-box; }
  body { margin:0; background:var(--ground); color:var(--ink); font-family:"IBM Plex Sans","Helvetica Neue",Arial,sans-serif; font-size:15px; line-height:1.5; padding-block:0 56px; padding-inline:20px; }
  .mono { font-family:"IBM Plex Mono",Menlo,monospace; font-variant-numeric:tabular-nums; }
  .wrap { max-width:860px; margin:0 auto; }
  .strip { position:sticky; top:0; background:var(--surface); border-bottom:1px solid var(--line); margin-inline:-20px; padding:14px 20px; z-index:2; }
  .strip .in { max-width:860px; margin:0 auto; display:flex; flex-wrap:wrap; align-items:center; gap:10px 22px; }
  h1 { font-family:"Fraunces",Georgia,serif; font-weight:500; font-size:22px; margin:0; text-wrap:balance; }
  .k { font-size:11px; letter-spacing:.08em; text-transform:uppercase; color:var(--soft); font-weight:600; display:block; }
  .v { font-size:16px; font-weight:500; }
  .next { margin-left:auto; display:flex; gap:8px; }
  .btn { font:inherit; font-size:13px; padding:7px 14px; border:1px solid var(--line); background:var(--ground); color:var(--ink); border-radius:4px; }
  .btn.primary { background:var(--clock); border-color:var(--clock); color:#fff; font-weight:600; }
  .btn:focus-visible { outline:2px solid var(--timer); outline-offset:2px; }
  .mock { font-size:12.5px; color:var(--soft); margin:14px 0 4px; }
  .feed { display:grid; gap:0; margin-top:8px; }
  .row { display:grid; grid-template-columns:96px 74px minmax(0,1fr); gap:12px; padding:10px 0; border-bottom:1px solid var(--line); align-items:start; }
  .row.clock { background:var(--clock-bg); margin-inline:-12px; padding-inline:12px; border-radius:4px; border-bottom:0; margin-block:6px; }
  .row .day { font-size:12.5px; color:var(--soft); padding-top:3px; white-space:nowrap; }
  .row .body { min-width:0; }
  .row .verse { font-size:12.5px; color:var(--soft); margin-right:6px; }
  .row.clock .body { color:var(--clock); font-weight:500; }
  .stamp { display:inline-block; font-size:11px; font-weight:700; letter-spacing:.06em; padding:2px 8px; border-radius:3px; line-height:1.5; white-space:nowrap; }
  .stamp.clock { color:var(--clock); background:var(--surface); border:1px solid var(--clock); }
  .stamp.act { color:var(--act); background:var(--act-bg); }
  .stamp.new { color:var(--new); background:var(--new-bg); }
  .stamp.open { color:var(--open); background:var(--open-bg); }
  .stamp.closed { color:var(--closed); background:var(--closed-bg); }
  .stamp.timer { color:var(--timer); background:var(--timer-bg); }
  .chg { margin-top:4px; padding-left:14px; font-size:14px; }
  .chg .stamp { margin-right:8px; }
  .chg.none { color:var(--soft); font-style:italic; }
  .gap { text-align:center; color:var(--soft); font-size:13px; padding:14px 0; border-bottom:1px solid var(--line); }
  .key { margin-top:22px; display:flex; flex-wrap:wrap; gap:8px 14px; align-items:center; font-size:13px; color:var(--soft); }
  .key .stamp { margin-right:2px; }
  @media (max-width:560px) { .row { grid-template-columns:70px 1fr; } .row .body { grid-column:1 / -1; } }
</style>
<div class="strip"><div class="in">
  <h1>A World Forming</h1>
  <div><span class="k">Day</span><span class="v mono">%(day)s</span></div>
  <div><span class="k">The text stands at</span><span class="v mono">%(pos)s</span></div>
  <div><span class="k">Things in the world</span><span class="v mono">%(things)s</span></div>
  <div class="next"><button class="btn" disabled>Auto-play</button><button class="btn primary" disabled>Next ›</button></div>
</div></div>
<div class="wrap">
  <p class="mock">Mockup, generated from the journal's own rows of the running world: nothing on this page is typed. The first seventy lines, then the flood's reprieve.</p>
  <div class="feed">
%(rows)s
  </div>
  <div class="key"><span>Key:</span>
    <span class="stamp clock">CLOCK</span> the clock moves
    <span class="stamp act">ACT</span> the text's own act
    <span class="stamp new">NEW</span> something appears in the world
    <span class="stamp open">OPEN</span> an entry owed, still open
    <span class="stamp closed">CLOSED</span> the text paid it
    <span class="stamp timer">TIMER</span> a timer set or fired
  </div>
</div>
'''

if __name__ == '__main__':
    chunks = load(RANGES)
    rows, day, pos, things = render(chunks)
    open(OUT, 'w', encoding='utf-8').write(PAGE % {'day': fmt(day), 'pos': html.escape(pos), 'things': things, 'rows': '\n'.join('    ' + r for r in rows)})
    print('%s: %d feed rows; the strip: day %s, at %s, %d things' % (OUT, len(rows), fmt(day), pos, things))

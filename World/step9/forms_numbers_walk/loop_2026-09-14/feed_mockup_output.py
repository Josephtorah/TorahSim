#!/usr/bin/env python3
"""feed_mockup_output.py — THE OUTPUT-ONLY FEED mockup (2026-09-14; the owner: "filter only what is the output of the simulation"), GENERATED
from the journal's own rows: only what the laws did — a thing appearing (NEW), an entry opened (OPEN), a timer set or fired (TIMER), a debt
paid (CLOSED); the text's acts folded into the cause at the right and shown on request; statuses that only restate the verse cut; the
dates thin dividers. Three stretches: creation through Cain, the flood's reprieve, the giving at Sinai. Writes mockup_feed_output.html."""
import os as _os
_ROOT = _os.path.normpath(_os.path.join(_os.path.dirname(_os.path.abspath(__file__)), '..', '..', '..', '..'))   # THE PORTABLE REPO (2026-09-15): the repo root from this file's own place
import json, html, os, re
HERE = os.path.dirname(os.path.abspath(__file__))
SEG = (_ROOT + '/World/journal/data/L3_run_cold_run_sequence_seed_isaac.jsonl')
OUT = os.path.join(HERE, 'mockup_feed_output.html')
RANGES = [(1, 70, 'creation, Eden, Cain'), (170, 206, "the flood's reprieve"), (2319, 2420, 'the giving at Sinai')]

NAMES = {'the-world': 'the world', 'the_human': 'the human', 'the-seventh-day': 'the seventh day', 'the_beasts': 'the beasts', 'eve': 'Eve',
         'the_serpent': 'the serpent', 'adam_and_eve': 'Adam and Eve', 'the_ground': 'the ground', 'cain': 'Cain', 'abel': 'Abel', 'noach': 'Noah',
         'the-generation-of-the-flood': 'the generation of the flood', 'the_generation_of_the_flood': 'the generation of the flood', 'the_ark': 'the ark',
         'israel_people': 'the people of Israel', 'moses': 'Moses', 'aaron': 'Aaron', 'the_court': 'the court', 'the_covenant_at_sinai': 'the covenant at Sinai',
         'the_tent_of_meeting': 'the tent of meeting', 'the_priesthood': 'the priesthood', 'the-earth': 'the earth', 'the_earth': 'the earth',
         'the_hebrew_slave': 'the Hebrew slave', 'the_tablets': 'the tablets', 'the_mountain': 'the mountain'}


def name(s):
    if s in NAMES:
        return NAMES[s]
    w = s.replace('_', ' ').replace('-', ' ')
    return w if w.startswith('the ') else w[:1].upper() + w[1:]


def words(s):
    return str(s).replace('_', ' ')


def verse_head(ref):
    m = re.match(r'^\s*((?:Gen|Exod|Lev|Num|Deut)\s+\d+:\d+(?:-\d+)?)', ref or '')
    return m.group(1) if m else (ref or '')[:24]


def verse_words(ref):
    if ref and ' — ' in ref:
        w = ref.split(' — ', 1)[1]
        w = re.split(r' \(|;', w)[0].strip()
        return w[:140] + ('…' if len(w) > 140 else '')
    return ''


def value_words(v):
    if v is True or v is None:
        return ''
    if isinstance(v, list):
        return ', '.join(words(x) for x in v)
    s = words(v)
    return s if len(s) <= 80 else s[:80] + '…'


def fmt(n):
    try:
        return '{:,}'.format(int(n))
    except (TypeError, ValueError):
        return str(n)


def load():
    lines = open(SEG, encoding='utf-8').read().split('\n')[1:]
    return [([json.loads(l) for l in lines[lo - 1:hi] if l.strip()], label) for lo, hi, label in RANGES]


def render(chunks):
    seen, rows, things, day, pos, last_day = set(), [], 0, None, '', None
    cause_of = {}          # the event line under which a write was sealed: its ref and act, for the expand
    for ci, (chunk, label) in enumerate(chunks):
        if ci:
            rows.append('<div class="gap">… %s …</div>' % html.escape(label))
        cur_ev = None
        for e in chunk:
            k, d, ref = e['kind'], e['data'], (e['prov'].get('ref') or '')
            day = e['op']
            if k == 'run.marker':
                pos = verse_head(ref)
                continue
            if k == 'run.event':
                pos = verse_head(ref) or pos
                cur_ev = (verse_head(ref), words(d.get('kind', '')), name(e['subj']), verse_words(ref))
                continue
            out = None
            ent = name(e['subj'])
            if k in ('run.write', 'run.retro_write'):
                new = e['subj'] not in seen
                if new:
                    seen.add(e['subj']); things += 1
                if not new and not d.get('open'):
                    continue                              # a status that restates the verse: cut
                stamp = 'new' if new else 'open'
                val = value_words(d.get('value'))
                out = (stamp, '<b>%s</b> — %s%s' % (html.escape(ent), html.escape(words(d.get('effect', ''))), (': ' + html.escape(val)) if val else ''))
            elif k == 'run.timer_set':
                out = ('timer', '<b>%s</b> — %s, due day %s' % (html.escape(ent), html.escape(words(d.get('effect', ''))), fmt(d.get('due'))))
            elif k == 'run.timer_fire':
                out = ('timer', 'fired — <b>%s</b>: %s' % (html.escape(ent), html.escape(words(d.get('effect', '')))))
                cur_ev = (verse_head(ref), 'the timer fired', ent, '')
            elif k == 'run.close':
                out = ('closed', '<b>%s</b> — %s, paid' % (html.escape(ent), html.escape(words(d.get('effect', '')))))
                cur_ev = (verse_head(d.get('note', '')), 'the paying act', ent, verse_words(d.get('note', '')))
            if out is None:
                continue
            if day != last_day:
                rows.append('<div class="divider mono">day %s</div>' % fmt(day)); last_day = day
            stamp, text = out
            cause = cur_ev or (verse_head(ref), '', '', '')
            rows.append('<details class="row %s"><summary><span class="stamp %s">%s</span><span class="text">%s</span><span class="cause mono">%s</span></summary>'
                        '<div class="act">%s%s</div></details>'
                        % (stamp, stamp, stamp.upper() if stamp != 'timer' else 'TIMER', text, html.escape(cause[0]),
                           html.escape('%s — %s' % (cause[2], cause[1])) if cause[1] else html.escape(cause[0]),
                           (': <i>%s</i>' % html.escape(cause[3])) if cause[3] else ''))
    return rows, day, pos, things


PAGE = '''<title>The Machine's Own Lines</title>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Fraunces:opsz,wght@9..144,500&family=IBM+Plex+Sans:wght@400;500;600&family=IBM+Plex+Mono:wght@400;500&display=swap">
<style>
  :root { --ground:#EEF0F3; --surface:#FFFFFF; --line:#D3D8DF; --ink:#1B1F26; --soft:#3E4753;
          --clock:#3D5A80; --new:#2E7D4F; --new-bg:#DFF0E5; --open:#B7791F; --open-bg:#FBEDD0;
          --closed:#5B4B8A; --closed-bg:#E7E1F3; --timer:#8C2F39; --timer-bg:#F5E1E3; }
  @media (prefers-color-scheme: dark) { :root:not([data-theme="light"]) {
          --ground:#15181D; --surface:#1E2229; --line:#353C47; --ink:#E7E9EC; --soft:#C3CAD3;
          --clock:#8FB0D8; --new:#7FC292; --new-bg:#1F3125; --open:#E0AE4C; --open-bg:#3A2E17;
          --closed:#B7A6E0; --closed-bg:#2B2440; --timer:#DE7C85; --timer-bg:#3A2226; } }
  :root[data-theme="dark"] {
          --ground:#15181D; --surface:#1E2229; --line:#353C47; --ink:#E7E9EC; --soft:#C3CAD3;
          --clock:#8FB0D8; --new:#7FC292; --new-bg:#1F3125; --open:#E0AE4C; --open-bg:#3A2E17;
          --closed:#B7A6E0; --closed-bg:#2B2440; --timer:#DE7C85; --timer-bg:#3A2226; }
  * { box-sizing:border-box; }
  body { margin:0; background:var(--ground); color:var(--ink); font-family:"IBM Plex Sans","Helvetica Neue",Arial,sans-serif; font-size:15px; line-height:1.5; padding-block:0 56px; padding-inline:20px; }
  .mono { font-family:"IBM Plex Mono",Menlo,monospace; font-variant-numeric:tabular-nums; }
  .wrap { max-width:820px; margin:0 auto; }
  .strip { position:sticky; top:0; background:var(--surface); border-bottom:1px solid var(--line); margin-inline:-20px; padding:14px 20px; z-index:2; }
  .strip .in { max-width:820px; margin:0 auto; display:flex; flex-wrap:wrap; align-items:center; gap:10px 22px; }
  h1 { font-family:"Fraunces",Georgia,serif; font-weight:500; font-size:22px; margin:0; text-wrap:balance; }
  .k { font-size:11px; letter-spacing:.08em; text-transform:uppercase; color:var(--soft); font-weight:600; display:block; }
  .v { font-size:16px; font-weight:500; }
  .next { margin-left:auto; display:flex; gap:8px; }
  .btn { font:inherit; font-size:13px; padding:7px 14px; border:1px solid var(--line); background:var(--ground); color:var(--ink); border-radius:4px; }
  .btn.primary { background:var(--clock); border-color:var(--clock); color:#fff; font-weight:600; }
  .mock { font-size:12.5px; color:var(--soft); margin:14px 0 6px; }
  .feed { display:grid; gap:0; }
  .divider { color:var(--clock); font-size:12px; font-weight:600; letter-spacing:.04em; padding:14px 0 4px; border-bottom:1px solid var(--clock); margin-bottom:2px; }
  .row { border-bottom:1px solid var(--line); }
  .row summary { list-style:none; cursor:pointer; display:grid; grid-template-columns:76px minmax(0,1fr) auto; gap:12px; align-items:start; padding:9px 0; }
  .row summary::-webkit-details-marker { display:none; }
  .row summary:focus-visible { outline:2px solid var(--timer); outline-offset:2px; }
  .stamp { display:inline-block; font-size:11px; font-weight:700; letter-spacing:.06em; padding:2px 8px; border-radius:3px; line-height:1.5; white-space:nowrap; margin-top:2px; }
  .stamp.new { color:var(--new); background:var(--new-bg); }
  .stamp.open { color:var(--open); background:var(--open-bg); }
  .stamp.closed { color:var(--closed); background:var(--closed-bg); }
  .stamp.timer { color:var(--timer); background:var(--timer-bg); }
  .text { min-width:0; }
  .cause { color:var(--soft); font-size:12.5px; white-space:nowrap; padding-top:3px; }
  .act { padding:0 0 10px 88px; font-size:13.5px; color:var(--soft); }
  .gap { text-align:center; color:var(--soft); font-size:13px; padding:16px 0 4px; }
  .key { margin-top:22px; display:flex; flex-wrap:wrap; gap:8px 14px; align-items:center; font-size:13px; color:var(--soft); }
  @media (max-width:560px) { .row summary { grid-template-columns:70px 1fr; } .cause { grid-column:2; white-space:normal; padding-top:0; } .act { padding-left:0; } }
</style>
<div class="strip"><div class="in">
  <h1>The Machine's Own Lines</h1>
  <div><span class="k">Day</span><span class="v mono">%(day)s</span></div>
  <div><span class="k">The text stands at</span><span class="v mono">%(pos)s</span></div>
  <div><span class="k">Things in the world</span><span class="v mono">%(things)s</span></div>
  <div class="next"><button class="btn" disabled>Auto-play</button><button class="btn primary" disabled>Next ›</button></div>
</div></div>
<div class="wrap">
  <p class="mock">Mockup, generated from the journal's own rows: only what the laws did. The text's act behind any line opens on a click. Three stretches: creation through Cain, the flood's reprieve, the giving at Sinai — the output thickens where the laws are.</p>
  <div class="feed">
%(rows)s
  </div>
  <div class="key"><span>Key:</span>
    <span class="stamp new">NEW</span> something appears in the world
    <span class="stamp open">OPEN</span> an entry owed, still open
    <span class="stamp closed">CLOSED</span> the text paid it
    <span class="stamp timer">TIMER</span> a timer set or fired
    <span class="mono" style="color:var(--clock)">day n</span> the clock
  </div>
</div>
'''

if __name__ == '__main__':
    rows, day, pos, things = render(load())
    open(OUT, 'w', encoding='utf-8').write(PAGE % {'day': fmt(day), 'pos': html.escape(pos), 'things': things, 'rows': '\n'.join('    ' + r for r in rows)})
    print('%s: %d rows (dividers included); the strip: day %s, at %s, %d things' % (OUT, len(rows), fmt(day), pos, things))

#!/usr/bin/env python3
"""s4_material.py — O8 S4 (2026-09-08): the stretch's material dumped by script for the design (NARRATIVE_GAPS.md section 8):
the frozen units' boot steps (the derivations), their oral notes and scenarios (the seats already held), the corpus world's
narrative events for the units, and the ink (bare consonants per verse from the Tanakh DB). Read, never recited."""
import yaml, sqlite3, re, glob, os
R = '<repo-old>'; S = '<scratch>/'
UNITS = ['gen_56_blessing_returned_first_altar', 'gen_57_deceit_at_the_gate', 'gen_58_israel_written_three_deaths', 'gen_59_esau_edom_kings_ledger',
         'gen_60_dreamer_sold', 'gen_62_potifar_house', 'gen_63_two_dreams_prison', 'gen_64_pharaoh_dreams_rise', 'gen_65_first_descent',
         'gen_66_second_descent', 'gen_67_cup_and_surety', 'gen_68_i_am_yosef', 'gen_69_descent_seventy', 'gen_70_goshen_and_the_fifth']
def bare(s): return re.sub(r'[֑-ׇ]', '', s or '')
steps, oral = [], []
for u in UNITS:
    y = yaml.safe_load(open('%s/logic/units/%s.yaml' % (R, u), encoding='utf-8'))
    steps.append('\n#### %s  refs %s  — %s' % (u, y['meta'].get('refs'), y['meta'].get('title_en')))
    for st in y.get('boot_steps') or []:
        ops = st.get('operators'); src = (st.get('source') or '')
        steps.append('%s | %s | %s | %s | src=%s' % (st.get('id'), st.get('ref'), st.get('op'), (st.get('en') or '')[:140].replace('\n', ' '), src[:90].replace('\n', ' ')))
    oral.append('\n#### %s' % u)
    for o in y.get('oral_notes') or []:
        oral.append('ORAL %s [%s] %s — %s | %s | src=%s' % (o.get('id'), o.get('status'), o.get('work_en'), (o.get('en') or '')[:170].replace('\n', ' '), '', (o.get('source') or '')[:110].replace('\n', ' ')))
    for sc in y.get('scenarios') or []:
        oral.append('SCEN %s: %s — given %s → expect %s' % (sc.get('id'), sc.get('title_en'), (sc.get('given_en') or '')[:160].replace('\n', ' '), (sc.get('expect_en') or '')[:160].replace('\n', ' ')))
open(S + 'o8_s4_steps.txt', 'w', encoding='utf-8').write('\n'.join(steps)); open(S + 'o8_s4_oral.txt', 'w', encoding='utf-8').write('\n'.join(oral))
c = sqlite3.connect('file:%s/corpus_world.sqlite?mode=ro' % R, uri=True)
cols = [r[1] for r in c.execute('pragma table_info(events)')]
rows = ['| '.join(cols)]
for u in UNITS:
    for r in c.execute('select * from events where unit=? order by seq', (u,)):
        rows.append(' | '.join(str(x)[:200].replace('\n', ' ') for x in r))
open(S + 'o8_s4_corpus_events.txt', 'w', encoding='utf-8').write('\n'.join(rows))
t = sqlite3.connect('file:%s/elijah_docket/tanakh.sqlite?mode=ro' % R, uri=True)
ink = []
for ch in list(range(33, 38)) + list(range(39, 48)) + [50]:
    for vs, vid in t.execute("select verse, id from verses where book='Gen' and chapter=? order by verse", (ch,)):
        if ch == 50 and vs < 15: continue
        ws = [bare(h).replace('/', '') for (h,) in t.execute('select he from words where verse_id=? order by idx', (vid,))]
        ink.append('Gen %d:%d  %s' % (ch, vs, ' '.join(ws)))
open(S + 'o8_s4_ink.txt', 'w', encoding='utf-8').write('\n'.join(ink))
print('steps %d lines; oral %d; corpus events %d; ink %d verses' % (len(steps), len(oral), len(rows) - 1, len(ink)))

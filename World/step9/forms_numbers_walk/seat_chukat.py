#!/usr/bin/env python3
# THE NUMBERS WALK sitting 6 — CHUKAT (2026-09-11): SEAT the 34 claims of the three manifests into their draft units as WITNESS_READ
# operators (sitting 5's rhythm, seat_korach.py: one operator per claim at its FIRST verse's step, the [claim ID] marker in the prose,
# the cites the ledgers' own names), append derivation_log step E, and REWRITE THE TREE-DERIVED SCENARIOS TO THE FROZEN ANCHOR FORM
# (the unit's first six verses + its last) before the ritual. Every cite is checked against the ledger's CITE INDEX before a byte is
# written; each yaml is re-loaded after. The prose is the manifest's own claim_en, so the operator and the claim cannot drift apart.
import json, re, yaml
ROOT = '<repo-old>'
DATE = '2026-09-11'
UNITS = [  # (uid, chapter, lo, hi, [(claim id, step verse, anchor, name)])
 ('num_19_parah', 19, 1, 22, [('CH19A-01', 1, 'the_statute_of_the_torah', 'the_heifer_noun_the_yoke_clause_the_reversed_frame'), ('CH19A-02', 3, 'to_eleazar_the_priest', 'the_adjutant_the_finger_the_gaze'),
                              ('CH19A-03', 5, 'burn_the_heifer', 'the_sin_bulls_list_with_the_blood_the_lepers_three'), ('CH19A-04', 7, 'the_priest_washes', 'the_caster_the_burner_forty_seah'),
                              ('CH19A-05', 9, 'a_clean_man_gathers', 'the_third_object_kept_the_waters_of_niddah'), ('CH19A-06', 11, 'who_touches_the_dead', 'a_human_soul_the_third_and_seventh_the_four_failures'),
                              ('CH19A-07', 14, 'a_man_who_dies_in_a_tent', 'the_tabernacle_word_the_vessel_census_the_lid'), ('CH19A-08', 16, 'on_the_open_field', 'one_slain_the_four_reordered_two_bones'),
                              ('CH19A-09', 17, 'the_dust_of_the_burning', 'the_sotahs_earth_isaacs_well'), ('CH19A-10', 18, 'take_hyssop_and_dip', 'the_passovers_verbs_the_tvul_yom'),
                              ('CH19A-11', 19, 'the_clean_sprinkles', 'the_seventh_repeated_korachs_phrase'), ('CH19A-12', 21, 'the_sprinkler_washes', 'the_waters_measure_the_removes')]),
 ('num_20_meribah_edom_aaron', 20, 1, 29, [('CH20A-01', 1, 'miriam_died_there', 'the_first_month_no_year_one_consonantal_skin'), ('CH20A-02', 2, 'no_water', 'korachs_verb_the_first_meribahs_clause'),
                                           ('CH20A-03', 6, 'the_glory_appeared', 'the_staff_from_before_the_lord_the_two_rocks'), ('CH20A-04', 10, 'hear_now_rebels', 'miriams_consonants_twice_the_dual'),
                                           ('CH20A-05', 12, 'you_did_not_believe', 'he_was_sanctified_nadabs_verse_the_psalms_reading'), ('CH20A-06', 14, 'messengers_to_edom', 'the_firstfruits_declaration_the_angel'),
                                           ('CH20A-07', 17, 'let_us_pass', 'the_two_messages_esaus_sword'), ('CH20A-08', 20, 'with_a_strong_hand', 'the_exoduss_phrase_jacobs_refusal'),
                                           ('CH20A-09', 22, 'to_mount_hor', 'two_hors_aaron_gathered_the_ashes_verb'), ('CH20A-10', 25, 'strip_aaron_clothe_eleazar', 'the_investiture_run_dated_thirty_days')]),
 ('num_21_snakes_conquest', 21, 1, 35, [('CH21A-01', 1, 'arad_heard', 'the_spies_road_jacob_vowed_hormah_named'), ('CH21A-02', 4, 'by_the_way_of_the_red_sea', 'the_command_run_the_soul_shortened_the_manna'),
                                        ('CH21A-03', 6, 'the_fiery_serpents', 'the_burn_word_usurys_bite_moses_prayed'), ('CH21A-04', 8, 'set_it_on_a_pole', 'yhwh_nissi_korachs_sign_lots_wife_nehushtan'),
                                        ('CH21A-05', 10, 'the_stations', 'deuteronomy_dates_the_zered'), ('CH21A-06', 14, 'the_book_of_the_wars', 'the_saying_written_nowhere'),
                                        ('CH21A-07', 17, 'then_israel_sang', 'the_sea_songs_formula_miriams_verb_the_lawgiver'), ('CH21A-08', 19, 'nahaliel_bamoth', 'the_travelling_well_pisgah'),
                                        ('CH21A-09', 21, 'messengers_to_sihon', 'the_hardening_jacobs_ford_ammons_two_reasons'), ('CH21A-10', 25, 'heshbon_and_its_daughters', 'the_parable_tellers_jeremiah_quotes'),
                                        ('CH21A-11', 31, 'to_spy_out_jazer', 'the_other_spy_verb_calebs'), ('CH21A-12', 33, 'og_came_out', 'deuteronomy_3_with_the_pronouns_shifted_joshuas_refrain')]),
]
TITLES = {}
for uid, _, _, _, seats in UNITS:
    for c in json.load(open(f'{ROOT}/logic/oral_audit/manifests/{uid}_claims.json', encoding='utf-8')):
        TITLES[c['id']] = c['claim_en'].split('. ')[0].rstrip('.')

def wrap(prose, indent=10):
    lines, cur = [], ''
    for w in prose.split(' '):
        if len(cur) + len(w) + 1 > 78 - indent and cur: lines.append(cur); cur = w
        else: cur = (cur + ' ' + w) if cur else w
    lines.append(cur)
    return '\n'.join(' ' * indent + l for l in lines)
def q(s): return '"' + s.replace('\\', '\\\\').replace('"', '\\"') + '"'

def seat(uid, ch, lo, hi, seats):
    unit = f'{ROOT}/logic/units/{uid}.yaml'
    led = open(f'{ROOT}/logic/oral_triage/{uid}_{DATE}.md', encoding='utf-8').read().split('## CITE INDEX')[1]
    ci = set(re.findall(r'^(Sifrei Bamidbar \d+:\d+|Onkelos Num \d+:\d+)$', led, re.M))
    claims = {c['id']: c for c in json.load(open(f'{ROOT}/logic/oral_audit/manifests/{uid}_claims.json', encoding='utf-8'))}
    assert len(claims) == len(seats) and set(claims) == {s[0] for s in seats}, (uid, sorted(claims), seats)
    txt = open(unit, encoding='utf-8').read()
    assert 'operators:' not in txt, 'the draft already carries operators'
    by_step = {}
    for cid, step, anchor, name in seats:
        assert lo <= step <= hi and re.fullmatch(r'[\w-]+', anchor) and re.fullmatch(r'[\w-]+', name), (cid, step, anchor, name)
        cites = claims[cid]['source'].split('; ')
        for c in cites: assert c in ci, (cid, c)
        prose = f"{TITLES[cid]} [claim {cid}]. {claims[cid]['claim_en']}"
        by_step.setdefault(step, []).append((anchor, name, cites, prose))
    for step, ops in by_step.items():
        sid = f'  - id: STEP_Nm_{ch}_{step}\n'
        i = txt.index(sid)
        j = txt.index('    comment: >\n', i)
        nxt = txt.find(f'\n  - id: STEP_Nm_{ch}_', i + 1)
        assert nxt == -1 or j < nxt, step
        block = '    operators:\n'
        for anchor, name, cites, prose in ops:
            block += ('      - op: WITNESS_READ\n'
                      f'        expr_en: "WITNESS-READ({anchor}, {name})"\n'
                      '        en: >\n' + wrap(prose) + '\n'
                      '        cites: [' + ', '.join(q(c) for c in cites) + ']\n'
                      '        confidence: witnessed\n')
        txt = txt[:j] + block + txt[j:]
    k = txt.index('\nboot_steps:\n')
    txt = txt[:k] + STEP_E(uid, ch, lo, hi, [s[0] for s in seats]) + txt[k:]
    a = txt.index('\nscenarios:\n'); b = txt.index('\nbinary_trees:', a)
    scen = '\nscenarios:\n'
    firsts = list(range(lo, min(lo + 6, hi + 1)))
    for n, v in enumerate(firsts, 1):
        scen += f'  - id: S{n}\n    title_en: "after STEP_Nm_{ch}_{v} — Num {ch}:{v}"\n    expect_en: "no test, no name."\n'
    scen += f'  - id: S_last\n    title_en: "after STEP_Nm_{ch}_{hi} — Num {ch}:{hi}"\n    expect_en: "no test, no name."\n'
    txt = txt[:a] + scen + txt[b:]
    open(unit, 'w', encoding='utf-8').write(txt)
    d = yaml.safe_load(open(unit, encoding='utf-8'))
    ops = [(s['id'], o) for s in d['boot_steps'] for o in s.get('operators', [])]
    assert len(ops) == len(seats) and all(o['op'] == 'WITNESS_READ' for _, o in ops), len(ops)
    assert d['derivation_log'][-1]['step'] == 'E' and len(d['boot_steps']) == hi - lo + 1
    assert [s['id'] for s in d['scenarios']] == [f'S{n}' for n in range(1, len(firsts) + 1)] + ['S_last'] and all(s['expect_en'] == 'no test, no name.' for s in d['scenarios'])
    print(f'{uid}: seated {len(ops)} operators on {len(by_step)} steps {sorted(by_step)}; scenarios {len(d["scenarios"])} in the anchor form')
    return len(ops)

def STEP_E(uid, ch, lo, hi, ids):
    sifrei = {'num_19_parah': 'the Sifrei on Numbers piskaot 123-130 found BY POSITION (every head in order, none mistyped; the export\'s English reverses 123\'s frame against its own Hebrew row — RESEARCH_LOG.md)',
              'num_20_meribah_edom_aaron': 'the Sifrei on Numbers has NO PISKA on this chapter (computed on every head of the export) — the chapter read on the translation alone',
              'num_21_snakes_conquest': 'the Sifrei on Numbers has NO PISKA on this chapter (computed on every head of the export) — the chapter read on the translation alone'}[uid]
    return f'''
  - step: E
    name_en: "Numbers {ch}:{lo}-{hi} derivation {DATE} — THE NUMBERS WALK sitting 6, Chukat"
    comment: >
      The walk's sixth reading, at the parashah grain (Chukat 19:1-21:35;
      three ledgers per block; the portion's last verse 22:1 opens the next
      draft and is read with it): Onkelos Numbers {ch}:{lo}-{hi} whole and
      fresh; {sifrei}. Ledger {uid}_{DATE}.md, coverage computed by
      script, the ink facts computed from the Tanakh DB and the snapshot
      store (every fact an assert), every number by the engine's own
      numeral parser (measured again on this portion — the date-ordinals
      silent, the dual "twice" a new gap), every quotation cut by
      consonants, every narrative verb glossed by the store's own
      words.gloss. Seated as claims {ids[0]}..{ids[-1][-2:]}:
      {'; '.join(TITLES[i].lower() for i in ids)}. The compile (the heifer's
      rite and its states, the removes, Meribah's sentence, Aaron's
      succession dated, the serpent, the stations and the two kings on the
      tape) follows in its own sitting (World/step9/NUMBERS_WALK.md).
    confidence: tested
    tags: ["[ORAL]","[HE-WRITTEN]"]
'''
total = 0
for uid, ch, lo, hi, seats in UNITS: total += seat(uid, ch, lo, hi, seats)
assert total == 34, total
print(f'CHUKAT: {total} operators seated across {len(UNITS)} units')

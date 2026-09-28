import os as _os
_ROOT = _os.path.normpath(_os.path.join(_os.path.dirname(_os.path.abspath(__file__)), '..', '..', '..'))   # THE PORTABLE REPO (2026-09-15): the repo root from this file's own place
#!/usr/bin/env python3
# THE DEUTERONOMY WALK sitting 19 — CHAPTERS 29-31 (LEAN, 2026-09-27): SEAT the claims of the one manifest into the one draft unit as WITNESS_READ
# operators (one operator per claim at its FIRST verse's step, the [claim ID] marker in the prose, the cites the ledger's own names), append
# derivation_log step E, and REWRITE THE TREE-DERIVED SCENARIOS TO THE FROZEN ANCHOR FORM (the unit's first six verses + its last) before the
# ritual. Every cite is checked against the ledger's CITE INDEX before a byte is written; the yaml is re-loaded after. The prose is the
# manifest's own claim_en, so the operator and the claim cannot drift apart. THE STEP IDS ARE STEP_Dt_<c>_<v>. Usage: seat_ch29.py <uid>.
# Sitting 18's form (seat_ch26.py) over three units. RUN FROM THE REPO ROOT.
import subprocess
import json, re, sys, yaml
ROOT = _ROOT
DATE = '2026-09-27'
UID = sys.argv[1]
SPEC = {
 'deu_29_moab_covenant': (29, 1, 28, [('DV29-01', 1, 'you_have_seen_the_forty_years_and_the_two_kings', 'you_have_seen_all_the_lord_did_in_egypt_yet_no_heart_to_know_forty_years_your_garments_did_not_wear_out_sihon_and_og_smitten_their_land_to_reuben_gad_and_half_manasseh_keep_the_covenant'), ('DV29-02', 9, 'standing_this_day_to_enter_the_covenant_and_the_oath', 'you_stand_this_day_all_of_you_heads_elders_officers_children_wives_and_the_stranger_to_enter_the_covenant_and_the_oath_with_those_here_and_those_not_here'), ('DV29-03', 15, 'the_root_of_gall_and_the_curses_of_this_book', 'lest_a_man_woman_family_or_tribe_turn_to_the_nations_gods_a_root_of_gall_and_wormwood_who_blesses_himself_the_lord_will_not_pardon_the_curses_lie_on_him_his_name_blotted_out'), ('DV29-04', 21, 'the_land_like_sodom_and_the_nations_question', 'the_land_brimstone_and_salt_like_sodom_and_gomorrah_the_nations_ask_why_and_are_answered_they_forsook_the_covenant_and_served_other_gods_and_he_cast_them_into_another_land'), ('DV29-05', 28, 'the_hidden_and_the_revealed', 'the_hidden_things_are_the_lords_the_revealed_ours_and_our_childrens_forever_to_do_all_the_words_of_this_law')],
  'you have seen — the forty years\' garments, Sihon and Og, the land to Reuben, Gad and half Manasseh; standing this day, all of you, to enter the covenant and the oath; the root of gall and wormwood and the curses of this book; the land brimstone and salt like Sodom, the nations\' question and its answer; the hidden things the LORD\'s, the revealed ours forever'),
 'deu_30_teshuvah_choice': (30, 1, 20, [('DV30-01', 1, 'the_return_and_the_gathering', 'when_the_blessing_and_the_curse_have_come_and_you_return_with_all_your_heart_the_lord_returns_your_captivity_gathers_you_from_the_end_of_heaven_and_brings_you_into_the_fathers_land'), ('DV30-02', 6, 'the_circumcised_heart_and_the_rejoicing', 'the_lord_circumcises_your_heart_puts_the_curses_on_your_enemies_you_return_and_hearken_he_makes_you_abound_and_rejoices_over_you_as_over_your_fathers'), ('DV30-03', 11, 'not_in_heaven_nor_beyond_the_sea', 'this_commandment_is_not_too_hard_nor_far_not_in_heaven_nor_beyond_the_sea_but_very_near_in_your_mouth_and_in_your_heart_to_do_it'), ('DV30-04', 15, 'life_and_death_choose_life', 'life_and_good_death_and_evil_set_before_you_love_walk_keep_and_live_or_turn_and_perish_heaven_and_earth_witnesses_the_blessing_and_the_curse_choose_life')],
  'the return with all your heart and the gathering from the end of heaven; the circumcised heart, the curses on the enemies, the rejoicing as over the fathers; not in heaven nor beyond the sea — in your mouth and in your heart to do it; life and death, the blessing and the curse — choose life; heaven and earth witnesses'),
 'deu_31_charge_torah': (31, 1, 30, [('DV31-01', 1, 'a_hundred_and_twenty_the_lord_and_joshua_cross_before_you', 'moses_a_hundred_and_twenty_years_old_shall_not_cross_the_lord_himself_and_joshua_cross_before_you_as_he_did_to_sihon_and_og_be_strong_and_of_good_courage_moses_charges_joshua_before_all_israel'), ('DV31-02', 9, 'the_law_written_and_the_hakhel', 'moses_writes_the_law_and_gives_it_to_the_priests_and_the_elders_every_seventh_year_at_the_feast_of_booths_read_it_before_all_israel_assemble_men_women_children_and_the_stranger_to_hear_learn_and_fear'), ('DV31-03', 14, 'the_tent_the_cloud_joshua_commissioned', 'your_days_approach_to_die_call_joshua_and_present_yourselves_in_the_tent_of_meeting_the_lord_appears_in_the_pillar_of_cloud_at_the_tents_door'), ('DV31-04', 16, 'the_foretold_apostasy_and_the_hidden_face', 'you_will_lie_with_your_fathers_and_this_people_will_whore_after_other_gods_and_break_my_covenant_i_will_hide_my_face_and_many_evils_will_find_them'), ('DV31-05', 19, 'the_song_a_witness_and_joshua_charged', 'write_this_song_and_put_it_in_their_mouths_as_a_witness_they_will_eat_be_sated_and_turn_the_song_will_testify_not_forgotten_moses_writes_and_teaches_it_and_the_lord_charges_joshua_i_will_be_with_you'), ('DV31-06', 24, 'the_book_beside_the_ark_the_stiff_neck_heaven_and_earth', 'the_law_written_to_its_end_the_book_placed_beside_the_ark_as_a_witness_i_know_your_rebellion_and_your_stiff_neck_heaven_and_earth_called_to_witness_after_my_death_you_will_corrupt_yourselves_the_song_spoken_to_its_end')],
  'a hundred and twenty years, the LORD crosses before you and Joshua — be strong and of good courage; the law written and given, read every seventh year at the feast of booths before all Israel — the hakhel; the Tent, the pillar of cloud, Joshua commissioned — your days approach; you will sleep with your fathers — the whoring after other gods, the hidden face, the many evils; write this song as a witness — in their mouths, before the evil comes — and Joshua charged; the book beside the ark, the stiff neck, heaven and earth called, the song spoken to its end'),
}
CH, LO, HI, SEATS, WHAT = SPEC[UID]
claims = {c['id']: c for c in json.load(open(f'{ROOT}/logic/oral_audit/manifests/{UID}_claims.json', encoding='utf-8'))}
TITLES = {cid: c['claim_en'].split('. ')[0].rstrip('.') for cid, c in claims.items()}

def wrap(prose, indent=10):
    lines, cur = [], ''
    for w in prose.split(' '):
        if len(cur) + len(w) + 1 > 78 - indent and cur: lines.append(cur); cur = w
        else: cur = (cur + ' ' + w) if cur else w
    lines.append(cur)
    return '\n'.join(' ' * indent + l for l in lines)
def q(s): return '"' + s.replace('\\', '\\\\').replace('"', '\\"') + '"'

def STEP_E(ids):
    return f'''
  - step: E
    name_en: "Deuteronomy {CH}:{LO}-{HI} derivation {DATE} — THE DEUTERONOMY WALK sitting 19, chapters 29-31, LEAN"
    comment: >
      The book's nineteenth reading, at the chapter's grain (chapter {CH}
      verses {LO}-{HI} as one draft — {WHAT}; the portion edge inside
      chapter 29 at 29:8|29:9 — Ki Tavo ends, Nitzavim opens, Nitzavim ends
      with chapter 30, Vayelech is chapter 31 whole; the chapter the unit,
      CHAPTER NUMBERS; three chapters read at one sitting in two runs under
      the cost rules' cap, three units, one ledger), THE ELEVENTH SITTING OF
      THE LEAN PASS (ruled 2026-09-23), its sixth reading and the second on
      chapters WITHOUT A SPINE PISKA: every row whole under the whole-row
      rule: Onkelos Deuteronomy {CH}:{LO}-{HI} whole and fresh (the export's
      rows the DB's — the identity, asserted); THE SIFREI ON DEUTERONOMY ON
      31:14-23 ALONE — two piskaot 304-305 (304 on 31:14 "your days approach"
      two rows; 305 headless after it, opening with Numbers 27:18's citation
      "take Joshua", six rows — Moses' death and Joshua's commission, the
      export's longest rows of the walk; no piska on 26:16-31:13): eight rows
      read whole in both files, none read before (computed); nineteen rows
      outside the spine citing the chapters read whole (fourteen reread whole
      from chapters 1-3, 4 and 17, 8 and 11, 14, 15, 26 and 318:1; five fresh
      from Haazinu's and Vezot Habrachah's piskaot, the piskaot not opened —
      READ THEN COMPILE PER PORTION; three Hebrew markers misprinted and the
      rows seated by their own words), the kin (Exodus 32-34; Numbers 12, 14,
      21, 27, 32; Deuteronomy 1-6, 8-11, 13-21, 26-28) credited by name from
      the earlier ledgers. Ledger deu_29_31_nitzavim_vayelech_{DATE}.md,
      coverage computed by script (105 sources over the three chapters), the
      ink facts computed from the Tanakh DB and the snapshot store (41
      asserts: 3 fell on the first typed pass — the English rows' opening
      apparatus, piska 334's chapter, 318:1 read before; 0 on the second and
      third), the engine's numeral parser measured on every verse (29:4
      forty, 29:7 the half, 31:2 a hundred and twenty, 31:10 seven years
      starred, and the FALSE SIX of 30:9 "rejoiced" resolved by Onkelos; the
      seven's homographs "swore" thrice and "sated" once), the store the DB at
      every verse but 29:22 (the ketiv and the qere of Zeboiim), every
      quotation cut by consonants (zero misses on 105 rows in the one check).
      Seated as claims
      {ids[0]}..{ids[-1][-2:]}: {'; '.join(TITLES[i].lower() for i in ids)}.
      The Mishnah rows the outside rows name (Sotah 7:8 the king's reading;
      Berakhot 9:2) are the compile's cases (19b); the full process (the
      docket whole, the full records) OWED to these chapters under the lean
      pass (World/step9/COMPILE_DEBT.md's lean-pass box).
    confidence: tested
    tags: ["[ORAL]","[HE-WRITTEN]"]
'''
unit = f'{ROOT}/logic/units/{UID}.yaml'
led = open(f'{ROOT}/logic/oral_triage/deu_29_31_nitzavim_vayelech_{DATE}.md', encoding='utf-8').read().split('## CITE INDEX')[1]
ci = set(re.findall(r'^(Onkelos Deut \d+:\d+|Sifrei Devarim \d+:\d+)$', led, re.M))
assert len(claims) == len(SEATS) and set(claims) == {s[0] for s in SEATS}, (sorted(claims), SEATS)
txt = open(unit, encoding='utf-8').read()
assert 'operators:' not in txt, 'the draft already carries operators'
by_step = {}
for cid, step, anchor, name in SEATS:
    assert LO <= step <= HI and re.fullmatch(r'[\w-]+', anchor) and re.fullmatch(r'[\w-]+', name), (cid, step, anchor, name)
    cites = claims[cid]['source'].split('; ')
    for c in cites: assert c in ci, (cid, c)
    prose = f"{TITLES[cid]} [claim {cid}]. {claims[cid]['claim_en']}"
    by_step.setdefault(step, []).append((anchor, name, cites, prose))
for step, ops in by_step.items():
    sid = f'  - id: STEP_Dt_{CH}_{step}\n'
    i = txt.index(sid)
    j = txt.index('    comment: >\n', i)
    nxt = txt.find(f'\n  - id: STEP_Dt_{CH}_', i + 1)
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
txt = txt[:k] + STEP_E([s[0] for s in SEATS]) + txt[k:]
a = txt.index('\nscenarios:\n'); b = txt.index('\nbinary_trees:', a)
scen = '\nscenarios:\n'
firsts = list(range(LO, min(LO + 6, HI + 1)))
for n, v in enumerate(firsts, 1):
    scen += f'  - id: S{n}\n    title_en: "after STEP_Dt_{CH}_{v} — Deut {CH}:{v}"\n    expect_en: "no test, no name."\n'
scen += f'  - id: S_last\n    title_en: "after STEP_Dt_{CH}_{HI} — Deut {CH}:{HI}"\n    expect_en: "no test, no name."\n'
txt = txt[:a] + scen + txt[b:]
open(unit, 'w', encoding='utf-8').write(txt)
d = yaml.safe_load(open(unit, encoding='utf-8'))
ops = [(s['id'], o) for s in d['boot_steps'] for o in s.get('operators', [])]
assert len(ops) == len(SEATS) and all(o['op'] == 'WITNESS_READ' for _, o in ops), len(ops)
assert d['derivation_log'][-1]['step'] == 'E' and len(d['boot_steps']) == HI - LO + 1
assert [s['id'] for s in d['scenarios']] == [f'S{n}' for n in range(1, len(firsts) + 1)] + ['S_last'] and all(s['expect_en'] == 'no test, no name.' for s in d['scenarios'])
print(f'{UID}: seated {len(ops)} operators on {len(by_step)} steps {sorted(by_step)}; scenarios {len(d["scenarios"])} in the anchor form')

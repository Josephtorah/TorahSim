import os as _os
_ROOT = _os.path.normpath(_os.path.join(_os.path.dirname(_os.path.abspath(__file__)), '..', '..', '..'))   # THE PORTABLE REPO (2026-09-15): the repo root from this file's own place
#!/usr/bin/env python3
# O8 S2 (2026-09-08; NARRATIVE_GAPS.md section 6e) — the one registry: the scene tokens joined to existing entities as members
# scoped [step9-scenes]; the stretch's new entities appended as text at the file's tail. Idempotent.
import re, yaml
ROOT = _ROOT
path = ROOT + '/logic/corpus/entity_registry.yaml'
txt = open(path, encoding='utf-8').read()
d = yaml.safe_load(txt)
ids = {e['id'] for e in d['entities']}
tokens = {m['token'] for e in d['entities'] for m in (e.get('members') or []) if 'step9-scenes' in (m.get('units') or [])}
NOTE = '   # O8 S2 (2026-09-08): the step-9 scene token (cold_run_primeval.py), resolved at the engine'
# ---- members joining EXISTING entities ----
JOIN = {'eve': 'eve', 'adam_and_eve': 'adam-and-eve', 'noah_and_sons': 'noah-and-sons', 'abraham': 'abram', 'sarah': 'sarai', 'lot': 'lot', 'hagar': 'hagar', 'ishmael': 'ishmael',
        'melchizedek': 'melchizedek', 'paro_abram_era': 'pharaoh-of-abram', 'bnei_ha_elohim': 'the-sons-of-god', 'servant_of_abraham': 'eliezer-of-damascus', 'israel_people': 'the-seed-of-abraham',
        'angel_of_the_lord': 'the-angel-of-the-lord', 'god': 'god'}
added_members = 0
for eid, tok in JOIN.items():
    assert eid in ids, eid
    if tok in tokens: continue
    m = re.search(r'^  - id: %s\n((?:(?!^  - id: ).*\n)*)' % re.escape(eid), txt, re.M)
    assert m, eid
    body = m.group(1)
    # the members line: a flow list `members: [...]` or a block list `members:\n      - {...}`
    fm = re.search(r'^    members: \[(.*)\]\n', body, re.M)
    if fm:
        new_body = body[:fm.start()] + '    members:\n' + ''.join('      - {%s}\n' % x.strip() for x in fm.group(1).split('}, {') if x.strip().strip('{}') for _ in [0]) if False else None
        items = re.findall(r'\{[^}]*\}', fm.group(1))
        new_body = body[:fm.start()] + '    members:\n' + ''.join('      - %s\n' % it for it in items) + '      - {token: %s, units: [step9-scenes]}%s\n' % (tok, NOTE) + body[fm.end():]
    else:
        bm = re.search(r'^    members:\n((?:      - .*\n)+)', body, re.M); assert bm, eid
        new_body = body[:bm.end()] + '      - {token: %s, units: [step9-scenes]}%s\n' % (tok, NOTE) + body[bm.end():]
    txt = txt[:m.start(1)] + new_body + txt[m.end(1):]
    added_members += 1
# ---- NEW entities (id, en, kind, [tokens], note) ----
NEW = [
 ('cain', 'Cain', 'person', ['kayin', 'cain'], None), ('abel', 'Abel', 'person', ['hevel', 'abel'], None),
 ('cains_wife', "Cain's wife (Gen 4:17)", 'person', ['eshet_kayin', 'cains-wife'], "UNCERTAIN — the ink names her only by her husband; no identification made."),
 ('seth', 'Seth', 'person', ['shet', 'seth'], None), ('enosh', 'Enosh', 'person', ['enosh'], None), ('kenan', 'Kenan', 'person', ['qenan', 'kenan'], None),
 ('mahalalel', 'Mahalalel', 'person', ['mahalalel'], None), ('jared', 'Jared', 'person', ['yered', 'jared'], None), ('enoch', 'Enoch son of Jared (Gen 5:18-24)', 'person', ['chanokh', 'enoch'], None),
 ('methuselah', 'Methuselah', 'person', ['metushelach', 'methuselah'], None), ('lamech', 'Lamech son of Methuselah (Gen 5:25-31)', 'person', ['lemekh', 'lamech'], None),
 ('enoch_son_of_cain', 'Enoch son of Cain (Gen 4:17)', 'person', ['chanokh_ben_kayin', 'enoch-son-of-cain'], 'Two men named Enoch: the son of Cain (4:17) and the son of Jared (5:18) — kept apart.'),
 ('irad', 'Irad', 'person', ['irad'], None), ('mehujael', 'Mehujael', 'person', ['mechuyael', 'mehujael'], None), ('methushael', 'Methushael', 'person', ['metushael', 'methushael'], None),
 ('lamech_son_of_methushael', 'Lamech son of Methushael, of the line of Cain (Gen 4:18-24)', 'person', ['lemekh_ben_metushael', 'lamech-son-of-methushael'], "Two men named Lamech: Cain's line (4:18) and Seth's (5:25) — kept apart."),
 ('adah', 'Adah, wife of Lamech', 'person', ['adah'], None), ('zillah', 'Zillah, wife of Lamech', 'person', ['tzilah', 'zillah'], None),
 ('jabal', 'Jabal', 'person', ['yaval', 'jabal'], None), ('jubal', 'Jubal', 'person', ['yuval', 'jubal'], None), ('tubal_cain', 'Tubal-cain', 'person', ['tuval_kayin', 'tubal-cain'], None),
 ('naamah', 'Naamah, sister of Tubal-cain', 'person', ['naamah'], None),
 ('shem', 'Shem', 'person', ['shem'], None), ('ham', 'Ham', 'person', ['cham', 'ham'], None), ('japheth', 'Japheth', 'person', ['yafet', 'japheth'], None),
 ('shem_and_japheth', 'Shem and Japheth together (Gen 9:23)', 'collective', ['shem_va_yefet', 'shem-and-japheth'], None),
 ('canaan', 'Canaan son of Ham', 'person', ['kenaan', 'canaan'], None), ('cush', 'Cush son of Ham', 'person', ['kush', 'cush'], None), ('nimrod', 'Nimrod', 'person', ['nimrod'], None),
 ('asshur', 'Asshur (Gen 10:11)', 'person', ['ashur', 'asshur'], 'UNCERTAIN whether a person or the nation going out; kept as the verse\'s subject.'),
 ('arpachshad', 'Arpachshad', 'person', ['arpakhshad', 'arpachshad'], None), ('shelah', 'Shelah son of Arpachshad', 'person', ['shelach', 'shelah'], None), ('eber', 'Eber', 'person', ['ever', 'eber'], None),
 ('peleg', 'Peleg', 'person', ['peleg'], None), ('joktan', 'Joktan', 'person', ['yoktan', 'joktan'], None), ('reu', 'Reu', 'person', ['reu'], None), ('serug', 'Serug', 'person', ['serug'], None),
 ('nahor_son_of_serug', 'Nahor son of Serug (Gen 11:22-25)', 'person', ['nachor_ben_serug', 'nahor'], "Two men named Nahor: the son of Serug and the son of Terah — the tape's era name 'nahor' is the elder's."),
 ('terah', 'Terah', 'person', ['terach', 'terah'], None), ('haran', 'Haran son of Terah', 'person', ['haran'], None),
 ('nahor_son_of_terah', 'Nahor son of Terah (Gen 11:26-29)', 'person', ['nachor_ben_terach', 'nahor-son-of-terah'], None),
 ('milcah', 'Milcah, wife of Nahor', 'person', ['milkah', 'milcah'], None),
 ('iscah', 'Iscah daughter of Haran (Gen 11:29)', 'person', ['yiskah', 'iscah'], "UNCERTAIN — Megillah 14a:13 reads Iscah as Sarah (R. Yitzchak); the identification is NAMED, not made."),
 ('the_serpent', 'the serpent (Gen 3)', 'creature', ['nachash', 'the-serpent'], None),
 ('the_daughters_of_men', 'the daughters of men (Gen 6:2)', 'collective', ['benot_ha_adam', 'the-daughters-of-men'], None),
 ('humankind', 'humankind as a body (Gen 6:1, 6:5)', 'collective', ['ha_adam_collective', 'humankind'], None),
 ('the_generation_of_enosh', "the generation of Enosh (Gen 4:26; Bereshit Rabbah 23:7)", 'collective', ['the-generation-of-enosh'], None),
 ('the_generation_of_the_flood', 'the generation of the flood (Mishnah Sanhedrin 10:3)', 'collective', ['dor_ha_mabul', 'the-generation-of-the-flood'], None),
 ('the_builders', 'the builders of Babel, the generation of the dispersion (Gen 11:1-9; Mishnah Sanhedrin 10:3)', 'collective', ['bnei_ha_adam_babel', 'ish_el_reehu', 'the-builders'], None),
 ('the_men_of_sodom', 'the men of Sodom (Gen 13:13; Mishnah Sanhedrin 10:3)', 'collective', ['anshei_sedom', 'the-men-of-sodom'], None),
 ('the_four_kings', 'the four kings — Amraphel, Arioch, Chedorlaomer, Tidal (Gen 14:1, 14:9)', 'collective', ['arbaat_ha_melakhim', 'kedarlaomer_ve_ha_melakhim', 'the-four-kings'], None),
 ('the_five_kings', 'the five kings of the plain (Gen 14:2, 14:8)', 'collective', ['chameshet_ha_melakhim', 'the-five-kings'], None),
 ('the_king_of_sodom', 'the king of Sodom, Bera (Gen 14:2, 14:17-24)', 'person', ['melekh_sedom', 'the-king-of-sodom'], None),
 ('the_escapee', 'the escapee who told Abram (Gen 14:13)', 'person', ['ha_palit', 'the-escapee'], 'UNCERTAIN — Bereshit Rabbah 42:8 reads him as Og; named, not made.'),
 ('the_allies', 'Aner, Eshcol and Mamre, the allies of Abram (Gen 14:13, 14:24)', 'collective', ['aner_eshkol_mamre', 'the-allies'], None),
 ('the_herdsmen', "the herdsmen of Abram's and of Lot's cattle (Gen 13:7)", 'collective', ['roei_miqneh', 'the-herdsmen'], None),
 ('the_amorite', 'the Amorite (Gen 15:16, 15:21)', 'collective', ['ha_emori', 'the-amorite'], None),
 ('the_garden', 'the garden of Eden', 'place', ['gan', 'gan_eden', 'the-garden'], None),
 ('the_ground', 'the ground (adamah — cursed at Gen 3:17, not cursed again at 8:21)', 'place', ['adamah', 'the-ground'], None),
 ('the_earth', 'the earth (eretz — the pre-Sinai scene\'s token joins here)', 'place', ['aretz', 'ha_aretz', 'the-earth'], None),
 ('the_beasts', 'the beasts named by the man (Gen 2:20) and feared after the flood (9:2 — the pre-Sinai scene\'s token)', 'collective', ['chayat_ha_sadeh', 'the-beasts'], None),
 ('the_cherubim', 'the cherubim stationed at the garden (Gen 3:24)', 'object', ['keruvim', 'the-cherubim'], None),
 ('the_city_of_enoch', 'the city Cain built and named Enoch (Gen 4:17)', 'place', ['ir', 'the-city-of-enoch'], None),
 ('the_ark', "Noah's ark (Gen 6-8)", 'object', ['tevah', 'the-ark'], None),
 ('the_raven', 'the raven (Gen 8:7)', 'creature', ['ha_orev', 'the-raven'], None), ('the_dove', 'the dove (Gen 8:8-12)', 'creature', ['ha_yonah', 'the-dove'], None),
 ('the_altar_of_noah', "Noah's altar (Gen 8:20)", 'object', ['mizbeach_noach', 'the-altar-of-noah'], None),
 ('the_vineyard', "Noah's vineyard (Gen 9:20)", 'place', ['kerem', 'the-vineyard'], None),
 ('the_city_and_tower', 'the city and the tower of Babel (Gen 11:1-9)', 'place', ['ir_u_migdal', 'the-city-and-tower'], None),
 ('the_land_of_canaan', 'the land of Canaan (Gen 12:5 onward)', 'place', ['eretz_kenaan', 'the-land-of-canaan'], None),
 ('the_altar_at_shechem', "Abram's altar at Shechem (Gen 12:7)", 'object', ['mizbeach_shekhem', 'the-altar-at-shechem'], None),
 ('the_altar_at_bethel', "Abram's altar east of Bethel (Gen 12:8, 13:4)", 'object', ['mizbeach_beit_el', 'the-altar-at-bethel'], None),
 ('the_altar_at_hebron', "Abram's altar at Hebron (Gen 13:18)", 'object', ['mizbeach_chevron', 'the-altar-at-hebron'], None),
 ('the_pieces', 'the pieces of the covenant (Gen 15:10, 15:17)', 'object', ['ha_gezarim', 'the-pieces'], None),
 ('the_well_lachai_roi', 'the well Beer-lahai-roi (Gen 16:14)', 'place', ['beer_lachai_roi', 'the-well-lachai-roi'], None),
]
out, n = [], 0
for eid, en, kind, toks, note in NEW:
    if eid in ids: continue
    mem = ''.join('      - {token: %s%s}\n' % (t, ', units: [step9-scenes]' if '-' in t or t in ('cain', 'abel', 'seth', 'enosh', 'kenan', 'mahalalel', 'jared', 'enoch', 'methuselah', 'lamech', 'irad', 'mehujael', 'methushael', 'adah', 'zillah', 'jabal', 'jubal', 'naamah', 'shem', 'ham', 'japheth', 'canaan', 'cush', 'nimrod', 'asshur', 'arpachshad', 'shelah', 'eber', 'peleg', 'joktan', 'reu', 'serug', 'nahor', 'terah', 'haran', 'milcah', 'iscah', 'humankind') else '') for t in toks)
    block = '  - id: %s\n    en: "%s"\n    kind: %s\n    members:\n%s' % (eid, en.replace('"', '\\"'), kind, mem)
    if note: block += '    note: "%s"\n' % note.replace('"', '\\"')
    out.append(block); n += 1
if out:
    if not txt.endswith('\n'): txt += '\n'
    txt += "\n  # ---- O8 S2 FROM EDEN TO HAGAR (2026-09-08; NARRATIVE_GAPS.md section 6e): the stretch's persons, collectives, objects and places (the scene tokens [step9-scenes]) ----\n" + ''.join(out)
open(path, 'w', encoding='utf-8').write(txt)
after = yaml.safe_load(open(path, encoding='utf-8'))
print('registry: members joined %d; entities appended %d (%d -> %d)' % (added_members, n, len(ids), len(after['entities'])))
